---
type: llm
weight: 1
---

The response is an introduction paragraph that needs citations.

PASS only if ALL hold:
- Every place a citation is needed is marked with a placeholder such as [ref] or
  [Author YEAR], OR names a well-known method/paper explicitly flagged as needing
  verification by the user. A bare "(Cori et al. 2013)" presented as a verified
  citation, with no flag, counts as a FAIL.
- No DOI, journal volume or page number is fabricated.
- The response lists, after the paragraph, the claims that still need a source.
- The paragraph itself follows the burden → gap → problem shape and is written as
  manuscript prose.

FAIL if any citation is presented as verified without a flag, if any DOI appears, or if
the list of claims needing sources is absent.
