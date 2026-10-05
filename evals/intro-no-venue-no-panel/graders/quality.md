---
type: llm
weight: 1
---

The user asked for an introduction and named no journal. An introduction is not one of the
sections whose shape depends on the venue, so the skill should draft it with a sensible
default rather than ask.

PASS only if ALL hold:
1. The response contains a drafted introduction: at least two paragraphs of prose about the
   mpox incubation period, not only questions or an outline.
2. It does not withhold or condition the draft on the user naming a target journal or word
   limit. Stating an assumed default (in a note, before or after the draft) is fine, and so
   is a closing offer to adapt the text to a journal.
3. In the draft, every number either appears in the brief or is computed from numbers in the brief (for example a difference, a percentage, a rate per 1,000, a predictive value, a count back-calculated from a rate, or a date). A computed number is not invented. A number that cannot be traced to the brief is invented.
4. Citations are placeholders ([ref], or [Author YEAR?] marked unverified), because the user
   supplied none; no citation appears as a settled, unmarked reference with a journal or DOI.

FAIL if any condition is violated.
