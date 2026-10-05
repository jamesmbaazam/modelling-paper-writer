#!/usr/bin/env python3
"""Fetch an open-access full text from PubMed Central into tools/.cache/ for reading.

    python3 tools/fulltext.py PMC7162546 ...     # writes tools/.cache/ft_<pmcid>.txt
    python3 tools/fulltext.py --meta 10.1371/...  # print the bibliographic record for a DOI

Used when writing a style analysis, so the analysis is written from the paper rather than from
memory. Reuses the cached, rate-limited fetchers in verify_quotes.py. Standard library only.
"""

import json
import sys
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import verify_quotes as V  # noqa: E402


def meta(doi):
    q = urllib.parse.quote(f'DOI:"{doi}"')
    url = (f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query={q}"
           "&resultType=core&format=json")
    raw = V.fetch(url, f"meta_{V.safe(doi)}.json")
    for r in json.loads(raw)["resultList"]["result"]:
        j = (r.get("journalInfo") or {}).get("journal", {})
        print(json.dumps({
            "title": r.get("title"), "authors": r.get("authorString"),
            "year": r.get("pubYear"), "journal": j.get("title"),
            "iso": j.get("isoabbreviation"), "doi": r.get("doi"),
            "pmcid": r.get("pmcid"), "oa": r.get("isOpenAccess"),
            "cited": r.get("citedByCount"),
        }, indent=1, ensure_ascii=False))


def main():
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    if args[0] == "--meta":
        for doi in args[1:]:
            meta(doi)
        return
    for pmcid in args:
        text = V.pmc_fulltext(pmcid)
        out = V.CACHE / f"ft_{pmcid}.txt"
        out.write_text(text, encoding="utf-8")
        print(f"{pmcid}: {len(text.split()):>6} words -> {out.relative_to(V.ROOT)}")


if __name__ == "__main__":
    main()
