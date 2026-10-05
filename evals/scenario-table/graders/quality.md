---
type: llm
weight: 1
---

The response is a scenario definition table for an NPI modelling paper.

PASS only if ALL hold:
- It is a table with one row per scenario and columns for each contact setting
  (home, school, work, other), showing the percentage of baseline contacts retained
  (or the reduction) under each scenario.
- A baseline / no-intervention scenario is the first row.
- Scenarios are labelled with stable codes (A, B, C… or short names) that the text can
  reuse.
- The combined scenario is included, and its cells are consistent with the individual
  ones.
- Start date and duration are in the table or its caption.
- A caption states what the numbers are relative to.
- No numbers beyond those derivable from the brief are invented — values computed from the
  brief, such as combined-scenario percentages or an end date, are derivable (e.g. no invented
  coverage or efficacy).

FAIL if the table lacks a baseline row, lacks stable labels, or the combined scenario
contradicts its components.
