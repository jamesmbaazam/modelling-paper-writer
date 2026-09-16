---
type: llm
weight: 1
---

The response is a data and code availability statement.

PASS only if ALL hold:
- It says (in the statement or a note to the user) that a GitHub link alone is not
  archival and recommends a Zenodo or equivalent DOI pinned to the submitted version,
  with a placeholder for the DOI.
- It names the language and packages (R, odin, mcstate) and leaves a placeholder for
  versions rather than inventing them.
- It states that the admissions data cannot be shared, says how a reader could obtain
  them (a placeholder for the data access process is acceptable), and offers what CAN
  be shared (e.g. aggregated data, posterior samples, or simulated data).
- It includes a role-of-the-funding-source sentence or notes that the journal will
  require one.

FAIL if it invents a Zenodo DOI or version numbers, presents the GitHub URL as
sufficient, or omits the data-sharing restriction.
