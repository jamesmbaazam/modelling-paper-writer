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
3. Every number in the draft comes from the brief; none is invented.
4. Citations are placeholders ([ref], or [Author YEAR?] marked unverified), because the user
   supplied none; no citation appears as a settled, unmarked reference with a journal or DOI.

FAIL if any condition is violated.
