#!/usr/bin/env python3
"""Check the quotations in references/corpus/*.md against the papers' own text.

    python3 tools/verify_quotes.py            # all papers; writes docs/quote-verification.md
    python3 tools/verify_quotes.py 07 22      # only these ids, report to stdout
    python3 tools/verify_quotes.py --local-text   # also read tools/.cache/local_<id>.txt

A paper whose full_text is "publisher pdf" has no open full text: its analysis was written from
the publisher's PDF and its quotations checked against it at the time of writing, so they are
reported as *reviewed* rather than re-checked on every run. To check them again, put the
extracted text at tools/.cache/local_<id>.txt and pass --local-text; every quotation should then
come back *verified*, and anything *not found* is a transcription error. See CONTRIBUTING.md.

For each paper in papers.csv it gathers the open text it can reach: the abstract from Europe
PMC, plus the full text from PubMed Central when the DOI resolves to a PMCID. Every quotation
of 30 or more characters in the style file is split at ellipses and editorial brackets, and
each fragment is searched for in the source after normalising case, punctuation and
whitespace. A quotation is *verified* when every fragment is found, *not found* when the
source text is the full paper and a fragment is missing, and *unchecked* when only the
abstract was reachable and the quotation is not in it.

Downloads are cached in tools/.cache/. Standard library only.
"""

import csv
import html
import json
import re
import sys
import time
import unicodedata
import urllib.parse
import urllib.request
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CORPUS = ROOT / "references" / "corpus"
CACHE = Path(__file__).resolve().parent / ".cache"
REPORT = ROOT / "docs" / "quote-verification.md"
RULE_FILES = ["SKILL.md", "references/evidence.md", "references/examples.md",
              "references/ml-prediction.md", "references/guidance-papers.md"]
FIG_REF = r"\(\s*(?:figs?\.?|figure|table|appendix|supplementary)[^)]{0,40}\)"

# Quotations checked by hand and left as they are, with the reason. Keyed by paper label
# and the first words of the quotation.
REVIEWED = {
    ("Weitz 2015", "We find a point estimate"): "matches; PMC renders the R₀ and β symbols as images",
    ("Weitz 2015", "Importantly, the point-estimate"): "matches; PMC renders R₀ as an image",
    ("Grais 2008", "Some previous studies suggest"): "matches; the source carries author-year citations",
    ("Wynants 2020", "What is already known"): "two box headings, joined with a slash",
    ("Hellewell 2020", "Isolation of cases"): "matches; PMC leaves the reference numbers inline",
    ("Keeling 2001", "In a fully mixed system"): "matches p813 cols 2-3; the page footer falls mid-sentence",
    ("Grenfell 2001", "r = \u22120.59"): "matches the Fig. 3 legend, p719; pdftotext mangles the minus signs",
    ("Bjørnstad 2002", "Here we use a mechanistic model"): "matches p170-171; the running head falls mid-sentence",
}
UA = ("Mozilla/5.0 (compatible; modelling-paper-writer quote check; "
      "+https://github.com/jamesmbaazam/modelling-paper-writer)")
MIN_QUOTE = 30
MIN_FRAGMENT = 15


def fetch(url, cache_name):
    CACHE.mkdir(exist_ok=True)
    path = CACHE / cache_name
    if path.exists():
        return path.read_text(encoding="utf-8")
    for attempt in range(3):
        time.sleep(1 + 4 * attempt)  # stay well inside NCBI's rate guidance
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                text = r.read().decode("utf-8", errors="replace")
        except Exception as e:  # network errors are reported per paper, not fatal
            print(f"  fetch failed: {url}: {e}", file=sys.stderr)
            continue
        if "Recaptcha" in text[:5000] or "captcha" in text[:2000].lower():
            print(f"  challenge page, retrying: {url}", file=sys.stderr)
            continue
        path.write_text(text, encoding="utf-8")
        return text
    return ""


def safe(s):
    return re.sub(r"[^A-Za-z0-9._-]", "_", s)


def pmcid_for(doi):
    url = ("https://pmc.ncbi.nlm.nih.gov/tools/idconv/api/v1/articles/?format=json"
           "&tool=modelling-paper-writer&ids=" + urllib.parse.quote(doi))
    raw = fetch(url, f"idconv_{safe(doi)}.json")
    try:
        rec = json.loads(raw)["records"][0]
        return rec.get("pmcid")
    except Exception:
        return None


def abstract_for(doi):
    q = urllib.parse.quote(f'DOI:"{doi}"')
    url = (f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query={q}"
           "&resultType=core&format=json")
    raw = fetch(url, f"epmc_{safe(doi)}.json")
    try:
        res = json.loads(raw)["resultList"]["result"]
        return " ".join(r.get("abstractText", "") for r in res)
    except Exception:
        return ""


REF_NUMS = r"\d+(?:\s*[,–-]\s*\d+)*"


def drop_running_heads(text):
    """Remove running heads and footers from pdftotext output.

    pdftotext separates pages with a form feed. Only the first and last non-blank line of each
    page is a candidate, and only if it recurs on another page — so a mid-page sentence or a
    title that appears once is never touched. Left in, this furniture lands inside a sentence
    that spans a page break and makes a correct quotation look like a misquote.
    """
    pages = [p.splitlines() for p in text.split("\f")]
    if len(pages) < 3:
        return text
    edges = Counter()
    for page in pages:
        lines = [l.strip() for l in page if l.strip()]
        for line in {l for l in (lines[:1] + lines[-1:]) if 4 <= len(l) <= 150}:
            edges[line] += 1
    furniture = {line for line, n in edges.items() if n >= 2}
    out = []
    for page in pages:
        lines = [l for l in page if l.strip()]
        head = 1 if lines and lines[0].strip() in furniture else 0
        tail = len(lines) - (1 if lines and lines[-1].strip() in furniture else 0)
        out += lines[head:tail]
    return "\n".join(out)


def strip_markers(text):
    """Drop reference markers and figure pointers, which quotations rightly omit."""
    text = re.sub(r"\[\s*" + REF_NUMS + r"\s*\]", " ", text)
    text = re.sub(r"\(\s+" + REF_NUMS + r"\s*\)", " ", text)  # PMC pads linked refs
    return re.sub(FIG_REF, " ", text, flags=re.I)


def strip_tags(raw):
    """Plain text with reference markers removed, since quotations rightly omit them."""
    raw = re.sub(r"<(script|style)\b.*?</\1>", " ", raw, flags=re.S)
    raw = re.sub(r"<sup\b[^>]*>(?:\s|<[^>]+>|[\d,–-])*</sup>", " ", raw, flags=re.S)
    text = html.unescape(re.sub(r"<[^>]+>", " ", raw))
    return strip_markers(text)


def pmc_fulltext(pmcid):
    """PMC article page, else the Europe PMC open-access XML."""
    raw = fetch(f"https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/", f"pmc_{pmcid}.html")
    m = re.search(r"<article.*?</article>", raw, re.S)
    text = strip_tags(m.group(0)) if m else ""
    if len(text) < 20000:
        xml = fetch(f"https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/fullTextXML",
                    f"epmc_{pmcid}.xml")
        if xml.lstrip().startswith("<?xml") or "<article" in xml[:2000]:
            text = max(text, strip_tags(xml), key=len)
    return text


def norm(s):
    s = unicodedata.normalize("NFKC", s).lower()
    return re.sub(r"[^a-z0-9]+", "", s)


def quotations(md):
    """Yield (quotation, fragments, following text) for every quotation of MIN_QUOTE+ chars."""
    text = md.replace("“", '"').replace("”", '"')
    for m in re.finditer(r'"([^"\n]{%d,}?)"' % MIN_QUOTE, text):
        q = m.group(1)
        # A straight-quote pair can straddle the prose between two quotations; real
        # quotations do not start or end with whitespace or start with punctuation.
        if q[0].isspace() or q[-1].isspace() or q[0] in ".,;:)]":
            continue
        body = re.sub(FIG_REF, " ", q, flags=re.I)
        frags = re.split(r"\s*(?:…|\.\.\.|\[[^\]]*\])\s*", body)
        frags = [f for f in frags if len(norm(f)) >= MIN_FRAGMENT]
        if frags:
            yield q, frags, text[m.end():m.end() + 160]


PUBLISHER_PDF = "publisher pdf"
LOCAL_TEXT = "--local-text"
# Pre-Unicode journal PDFs encode ligatures as single glyphs, and `norm` would drop them along
# with the two letters they stand for. The same glyph can mean something else in another
# paper's equations (Bjørnstad 2002 uses ¯ as a macron), so the de-mangled text is searched
# *alongside* the raw text rather than replacing it.
LIGATURES = {"\u00ae": "fi", "\u00af": "fl", "\u00fe": "+", "\u00f0": "(", "\u00de": ")",
             "\u00bc": "="}  # \u00bc is Ecology Letters' "="; NFKC would read it as 1/4
SOURCES = {}


def source_for(row):
    """(basis, normalised text) for a paper, fetched once per run."""
    if row["id"] not in SOURCES:
        local = CACHE / f"local_{row['id']}.txt"
        if LOCAL_TEXT in sys.argv and local.exists():
            raw = drop_running_heads(local.read_text(encoding="utf-8", errors="replace"))
            fixed = raw
            for glyph, letters in LIGATURES.items():
                fixed = fixed.replace(glyph, letters)
            # Superscript citations in a PDF extract as bare digits glued to the preceding
            # word ("demography8,13"); quotations rightly omit them.
            # Three letters, so a symbol like R0 keeps its subscript while "demography8,13"
            # and "Wales49" lose their citation markers.
            bare = re.sub(r"(?<=[A-Za-z]{3})\d+(?:\s*[,\u2013\u00b1-]\s*\d+)*", "", fixed)
            SOURCES[row["id"]] = ("local PDF", " ".join(norm(strip_markers(v))
                                                        for v in (raw, fixed, bare)))
            return SOURCES[row["id"]]
        if row["full_text"] == PUBLISHER_PDF:
            SOURCES[row["id"]] = ("publisher PDF (hand-checked)", "")
            return SOURCES[row["id"]]
        pmcid = pmcid_for(row["doi"])
        full = pmc_fulltext(pmcid) if pmcid else ""
        abstract = abstract_for(row["doi"])
        has_full = len(norm(full)) > 5000
        basis = "full text (PMC)" if has_full else ("abstract only" if abstract else "none reachable")
        SOURCES[row["id"]] = (basis, norm(full + " " + abstract))
    return SOURCES[row["id"]]


def status_of(row, q, frags):
    basis, source = source_for(row)
    missing = [f for f in frags if norm(f) not in source]
    for (label, start), _ in REVIEWED.items():
        if label == row["label"] and q.startswith(start):
            return "reviewed", missing
    if not missing:
        return "verified", missing
    if basis.startswith("publisher PDF"):
        return "reviewed", missing
    return ("not found" if basis.startswith(("full", "local")) else "unchecked"), missing


def attributed(text_after, labels):
    """The corpus label cited right after a quotation, e.g. '… treatment" (Lauer 2020)'."""
    m = re.match(r'[^"]{0,40}?\(([^()"]{4,60})\)', text_after)
    if m:
        for label in labels:
            if label in m.group(1):
                return label
    return None


def main():
    rows = list(csv.DictReader(open(CORPUS / "papers.csv", encoding="utf-8")))
    only = {a for a in sys.argv[1:] if not a.startswith("-")}
    if only:
        rows = [r for r in rows if r["id"] in only]
    keys = ("verified", "not found", "unchecked", "reviewed")
    totals = dict.fromkeys(keys, 0)
    misses, lines = [], []

    def tally(counts, status, where, row, q, missing):
        counts[status] += 1
        totals[status] += 1
        if status == "not found":
            misses.append(f"- {where} ({row['label']}): “{q[:200]}{'…' if len(q) > 200 else ''}” "
                          f"— not found: “{missing[0][:80]}”")

    for r in rows:
        print(f"{r['id']} {r['label']}", file=sys.stderr)
        counts = dict.fromkeys(keys, 0)
        md = (CORPUS / r["file"]).read_text(encoding="utf-8")
        for q, frags, _ in quotations(md):
            status, missing = status_of(r, q, frags)
            tally(counts, status, f"`{r['file']}`", r, q, missing)
        lines.append(f"| {r['label']} | {source_for(r)[0]} | " +
                     " | ".join(str(counts[k]) for k in keys) + " |")

    by_label = {r["label"]: r for r in rows}
    rule_lines = []
    for rel in RULE_FILES:
        counts = dict.fromkeys(keys, 0)
        for q, frags, after in quotations((ROOT / rel).read_text(encoding="utf-8")):
            label = attributed(after, by_label)
            if label:
                status, missing = status_of(by_label[label], q, frags)
                tally(counts, status, f"`{rel}`", by_label[label], q, missing)
        rule_lines.append(f"| `{rel}` | " + " | ".join(str(counts[k]) for k in keys) + " |")

    report = [
        "# Quotation verification",
        "",
        f"<!-- Generated by `python3 tools/verify_quotes.py` on {date.today().isoformat()}. -->",
        "",
        "Every quotation of 30+ characters in `references/corpus/`, and every quotation in the "
        "rule files that is attributed to a corpus paper as `\"…\" (Author YEAR)`, checked "
        "against the paper's abstract (Europe PMC) and, where PubMed Central holds it, the full "
        "text. Matching ignores case, punctuation and whitespace, and treats ellipses and "
        "[editorial brackets] as gaps; reference markers and (figure/table) pointers are "
        "ignored, since quotations omit them.",
        "",
        "*Unchecked* means no open full text was reachable and the quotation is not in the "
        "abstract; it is not evidence of a misquote. *Reviewed* quotations were checked by hand "
        "and are listed with their reasons in `tools/verify_quotes.py`.",
        "",
        f"**Totals:** {totals['verified']} verified, {totals['not found']} not found, "
        f"{totals['unchecked']} unchecked, {totals['reviewed']} reviewed by hand.",
        "",
        "## Not found",
        "",
        *(misses or ["None."]),
        "",
        "## By paper (style files)",
        "",
        "| Paper | Source checked | Verified | Not found | Unchecked | Reviewed |",
        "|---|---|--:|--:|--:|--:|",
        *lines,
        "",
        "## Attributed quotations in the rule files",
        "",
        "| File | Verified | Not found | Unchecked | Reviewed |",
        "|---|--:|--:|--:|--:|",
        *rule_lines,
    ]
    out = "\n".join(report) + "\n"
    if only:
        print(out)
    else:
        REPORT.write_text(out, encoding="utf-8")
        print(f"wrote {REPORT.relative_to(ROOT)}: {totals}", file=sys.stderr)
    # A quotation the source does not contain is a misquote: fail so CI catches it.
    return 1 if totals["not found"] else 0


if __name__ == "__main__":
    sys.exit(main())
