---
type: llm
weight: 1
---

The response is a Methods subsection defining an SEIR model, written for LaTeX.

PASS only if ALL hold:
- The four compartments are named in words on first use (susceptible, exposed/latent,
  infectious, recovered), and the flows between them are stated in prose, not only in
  equations.
- Displayed equations are given in a LaTeX environment (align or equation), not as
  markdown italics or Unicode-only text.
- Every symbol in the equations is defined, with units where relevant (β, σ, γ, N).
- It states which parameters are fixed (latent 8 d, infectious 5 d) and which is
  estimated (β), and gives R0 = β/γ or the equivalent.
- It does not invent the fitted value of β or R0; if a value is needed it uses a
  placeholder.

FAIL if compartments are only abbreviated (an unexplained "SEIR"), if equations are not
in LaTeX, if any symbol is undefined, or if a fitted value is fabricated.
