#!/usr/bin/env python3
"""Find open-access candidates for the corpus in Europe PMC.

    python3 tools/candidates.py                  # every search below
    python3 tools/candidates.py nowcasting       # one search by name
    python3 tools/candidates.py --venues         # per-venue counts, to retune a search
    python3 tools/candidates.py --venue "PloS one"   # modelling papers in one journal

Prints real records — label, year, venue, citations, DOI, PMCID — so a paper can never be
added from memory. It cannot judge writing quality, which is the actual selection criterion:
treat the output as a shortlist to read, not a ranking to copy. See docs/reproducibility.md.

Standard library only. Responses are cached in tools/.cache/ (gitignored).
"""

import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = Path(__file__).resolve().parent / ".cache"
BASE = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
UA = ("modelling-paper-writer corpus survey "
      "(+https://github.com/jamesmbaazam/modelling-paper-writer)")

# Venues users actually target, plus the ones already in the corpus. JOURNAL: matches the
# Europe PMC journal title, which is not always the masthead ("Proceedings. Biological
# sciences" is Proc R Soc B).
VENUES = [
    "Epidemics", "Eurosurveillance", "Proceedings. Biological sciences", "BMC medicine",
    "Mathematical biosciences", "Epidemiology and infection", "Vaccine",
    "PLoS neglected tropical diseases", "Journal of the Royal Society, Interface",
    "PLoS computational biology", "BMC infectious diseases", "Nature communications",
    "The Lancet. Global health", "The Lancet. Infectious diseases", "PLoS medicine",
    "Science translational medicine", "Statistics in medicine", "Biostatistics",
    "International journal of epidemiology", "American journal of epidemiology",
    "PloS one", "PLoS biology", "Infectious diseases of poverty", "Emerging infectious diseases",
]

# One search per archetype the corpus is missing.
SEARCHES = {
    "cost-effectiveness": 'TITLE:"cost-effectiveness" OR TITLE:"economic evaluation" '
                          'OR (TITLE:"vaccination" AND TITLE:"impact" AND ABSTRACT:"averted")',
    "phylodynamics": 'TITLE:"phylodynamic" OR TITLE:"phylogeographic" '
                     'OR (TITLE:"genomic" AND TITLE:"transmission")',
    "serology": '(TITLE:"seroprevalence" OR TITLE:"serological" OR TITLE:"serocatalytic") '
                'AND (ABSTRACT:"force of infection" OR ABSTRACT:"catalytic model" '
                'OR ABSTRACT:"seroconversion rate")',
    "within-host": 'TITLE:"within-host" OR TITLE:"viral dynamics" OR TITLE:"viral load kinetics"',
    "agent-based": '(TITLE:"agent-based" OR TITLE:"individual-based") '
                   'AND (ABSTRACT:"transmission" OR ABSTRACT:"epidemic")',
    "nowcasting": 'TITLE:"nowcasting" OR TITLE:"nowcast" OR TITLE:"reporting delay" '
                  'OR TITLE:"right truncation"',
    "rapid-response": 'ABSTRACT:"real time" AND (ABSTRACT:"outbreak response" '
                      'OR ABSTRACT:"situational awareness" OR ABSTRACT:"public health response")',
    # Venue breadth: strong modelling papers in the journals the corpus under-represents.
    "venue-breadth": 'ABSTRACT:"transmission model" OR ABSTRACT:"mathematical model" '
                     'OR ABSTRACT:"modelling study" OR ABSTRACT:"modeling study"',
}

# For --venue: a wider net than venue-breadth (short abstracts, such as Emerging Infectious
# Diseases' 150 words, rarely say "mathematical model"), narrowed to infectious disease so a
# general journal such as PLoS ONE does not return protein folding and exoskeletons.
VENUE_MODELLING = (SEARCHES["venue-breadth"] + ' OR ABSTRACT:"reproduction number" '
                   'OR ABSTRACT:"compartmental model" OR ABSTRACT:"stochastic model" '
                   'OR ABSTRACT:"simulation model" OR ABSTRACT:"agent-based" '
                   'OR ABSTRACT:"we modeled" OR ABSTRACT:"we modelled" OR ABSTRACT:"force of infection"')
INFECTIOUS = ('ABSTRACT:"infectious" OR ABSTRACT:"epidemic" OR ABSTRACT:"outbreak" '
              'OR ABSTRACT:"pathogen" OR ABSTRACT:"vaccination" OR ABSTRACT:"incidence"')

VENUE_CLAUSE = "(" + " OR ".join(f'JOURNAL:"{j}"' for j in VENUES) + ")"
WINDOW = "FIRST_PDATE:[2012 TO 2025]"


def fetch(params, name):
    CACHE.mkdir(exist_ok=True)
    path = CACHE / f"cand_{name}.json"
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    url = BASE + "?" + urllib.parse.urlencode(params)
    for attempt in range(3):
        time.sleep(1 + 3 * attempt)
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=90) as r:
                data = json.loads(r.read())
            path.write_text(json.dumps(data), encoding="utf-8")
            return data
        except Exception as exc:
            print(f"  fetch failed ({exc}); retrying", file=sys.stderr)
    return {"hitCount": 0, "resultList": {"result": []}}


def search(name, clause, page_size=25):
    query = f"{VENUE_CLAUSE} AND OPEN_ACCESS:Y AND {WINDOW} AND ({clause})"
    data = fetch({"query": query, "format": "json", "pageSize": page_size,
                  "resultType": "core", "sort": "CITED desc"}, name)
    show(name, data)


def show(name, data):
    hits = data.get("hitCount", 0)
    rows = data.get("resultList", {}).get("result", [])
    print(f"\n=== {name}  ({hits} open-access hits, showing {len(rows)})")
    for r in rows:
        venue = (r.get("journalInfo") or {}).get("journal", {}).get("title", "?")
        first = (r.get("authorString") or "?").split(",")[0].split()[-1]
        print(f"  {first} {r.get('pubYear')}  {venue[:30]:30}  cit {str(r.get('citedByCount')):>5}"
              f"  {r.get('pmcid') or '-':12} {r.get('doi') or '-'}")
        print(f"      {(r.get('title') or '').strip()[:104]}")


def venue_counts():
    for journal in VENUES:
        data = fetch({"query": f'JOURNAL:"{journal}" AND OPEN_ACCESS:Y AND {WINDOW} '
                               f'AND ({SEARCHES["venue-breadth"]})',
                      "format": "json", "pageSize": 1},
                     "venue_" + re.sub(r"\W+", "_", journal))
        print(f"{journal:44} {data.get('hitCount', 0):5}")


def venue_search(journal, page_size=40):
    """Infectious disease modelling papers in one journal, most cited first."""
    if journal not in VENUES:
        sys.exit(f"unknown venue {journal!r}; use the Europe PMC title, one of: {', '.join(VENUES)}")
    clause = (f'JOURNAL:"{journal}" AND OPEN_ACCESS:Y AND {WINDOW} '
              f'AND ({VENUE_MODELLING}) AND ({INFECTIOUS})')
    data = fetch({"query": clause, "format": "json", "pageSize": page_size,
                  "resultType": "core", "sort": "CITED desc"},
                 "venue_id_" + re.sub(r"\W+", "_", journal))
    show(journal, data)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    if "--venues" in sys.argv:
        return venue_counts()
    if "--venue" in sys.argv:
        i = sys.argv.index("--venue")
        if i + 1 >= len(sys.argv):
            sys.exit('usage: candidates.py --venue "Europe PMC journal title"')
        return venue_search(sys.argv[i + 1])
    for name in (args or SEARCHES):
        if name not in SEARCHES:
            sys.exit(f"unknown search {name!r}; choose from {', '.join(SEARCHES)}")
        search(name, SEARCHES[name])


if __name__ == "__main__":
    main()
