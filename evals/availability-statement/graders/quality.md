---
type: llm
weight: 1
---

The response is a data and code availability statement.

PASS only if ALL hold:
- It accepts the GitHub link as the code location, and does not say the link is
  insufficient or that a Zenodo or other DOI archive is required. Optionally suggesting
  a tagged release or commit is fine.
- It names the language and packages (R, odin, mcstate) and leaves a placeholder for
  versions rather than inventing them.
- It states that the admissions data cannot be shared, says how a reader could obtain
  them (a placeholder for the data access process is acceptable), and offers what CAN
  be shared (e.g. aggregated data, posterior samples, or simulated data).
- It includes a role-of-the-funding-source sentence or notes that the journal will
  require one.

FAIL if it invents a DOI or version numbers, requires or insists on a Zenodo or DOI
archive, treats the GitHub URL as inadequate, or omits the data-sharing restriction.
