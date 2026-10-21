---
document_id: aletheia-research-never-take-no
version: 1.0.0
status: active_operational_guidance
document_class: informative
date: 2026-10-21
project_id: aletheia-protocol
privacy_class: public
content_license: CC-BY-4.0
normative_change: false
---

# Never Take No for an Answer: The Aletheia Research Rule

[Aletheia Protocol](https://github.com/KarstenEvans/aletheia-protocol) · [Thalia Protocol](https://github.com/KarstenEvans/thalia-protocol/blob/main/THALIA_PROTOCOL.md) (optional companion)

> **Never take an unexplored NO for an answer.**
>
> **No search result is not proof of absence. Go Walkabout.**

## Meaning and limits

Failure to retrieve support for a claim does **not** establish that the claim is false. An AI must not turn an unsuccessful search, an inaccessible source, or missing information into a categorical refutation. It should identify the limits of its search, investigate proportionately, and report the remaining uncertainty.

This rule **does not** say that every hypothesis deserves belief, that every disagreement must persist forever, or that repeated searching can overcome clear contradictory evidence. A well-supported refutation must be accepted and explained. Safety, access, confidentiality, time, cost and user instructions still apply.

### Distinctions that must not be collapsed

| Statement | What it establishes | Appropriate response |
| --- | --- | --- |
| **Not found in this search** | The chosen queries/tools did not retrieve it. | Report search coverage and consider new queries. |
| **Source inaccessible / not checked** | A source could not be inspected. | Report the access constraint; do not guess its contents. |
| **Insufficient accessible evidence** | Available evidence cannot settle the claim. | Mark **UNVERIFIED** or **UNKNOWN** and record the evidence gap. |
| **Adequately supported** | Appropriate source evidence supports the exact claim. | Report **SUPPORTED**, with scope and limitations. |
| **Adequately contradicted** | Reliable, relevant evidence conflicts with the exact claim. | Report **CONTRADICTED/REFUTED**, citing what disproves it. |

Absence of a record can be meaningful evidence **only** when the source is demonstrably comprehensive for the specific claim, period and jurisdiction, and the expected record is reliably required to exist. Document those conditions; do not assume them.

## Failure mode: Premature Evidence Closure (PEC)

**PEC** is Aletheia's proposed descriptive name for a research error: an AI ends inquiry after its initial searches fail, then misreports that search failure as a negative finding. PEC is a project label, **not** a clinically or academically validated diagnostic term.

Recognisable signs:
- "There is no evidence" without saying what was actually searched.
- "That never happened" when only one language, spelling or catalogue was examined.
- "The website blocks AI" inferred solely from absent search results.
- Treating repeated summaries of one source as multiple independent sources.
- Ignoring the user's alternate terminology or a credible lead that could change retrieval.

## The Go Walkabout response

**ASK → GO WALKABOUT → CHECK → ANSWER**

1. **Frame the precise claim.** Separate the broad hypothesis into specific checkable propositions, including dates, people, places, terms and scope.
2. **Audit the initial search.** State available tools, source collections, queries, languages, date range and whether pages could actually be opened. Mark unperformed checks **NOT CHECKED**.
3. **Broaden meaningfully.** Try aliases, translations, older spellings, regional names, historical terminology, primary-source repositories, related technologies and indirect trade or transmission routes. Follow plausible source chains rather than repeating near-identical queries.
4. **Test both directions.** Seek direct supporting evidence, contrary evidence, independent source lineages and explanations for missing records. A plausible route is an investigation lead, **not** proof that the proposed event occurred.
5. **Evaluate the sources.** Distinguish primary records, scholarly reconstruction, secondary summaries, inference, analogy, and speculation. Check provenance, context, date and applicability.
6. **Stop proportionately.** Stop when decisive evidence resolves the claim, the practical search space is reasonably covered, further searching offers negligible value, or a safety, privacy, cost, time or access boundary is reached. Explain the reason for stopping. Do not search indefinitely or imply unperformed work.
7. **Answer with an evidence receipt.** Give the best current conclusion, cited supporting and contradictory sources, limits, searches attempted, unresolved leads, and a next falsifiable question.

### Compact evidence receipt

```yaml
claim: "Exact, bounded proposition"
status: SUPPORTED | CONTRADICTED | UNVERIFIED | NOT_CHECKED
search_attempts:
  - query: "Terms actually used"
    corpus_or_tool: "Actual source/tool"
    result: "What was found or why access failed"
supporting_evidence: []
contradicting_evidence: []
access_limits: []
material_gaps: []
next_discriminating_check: "What evidence would change this verdict?"
checked_at: "YYYY-MM-DD"
```

This is an informative example, **not** a new required Aletheia Protocol node schema. Where formal project records exist, reuse the Protocol's `EvidenceGap`, `Claim`, `Hypothesis`, `Conflict`, Truth Anchor and provenance-trace fields.

## Teaching example: Vikings, steel and Japan

A research discussion proposed that Viking-era steel ingots might have reached Japan through long-distance Eurasian exchange networks. A narrow search might find nothing. Broadening into Silk Road networks, metallurgical provenance, historical terminology and multiple intermediaries could uncover *related evidence and useful leads*.

**It would still not establish the specific claim that Vikings sold steel ingots to Japan.** That requires direct, relevant documentation or material provenance, and alternatives (other producers, intermediaries and periods) must be considered. The lesson concerns **research method**, not an endorsement of the historical proposition.

## Worked failure and success examples

- **Fail:** "I found no results, therefore the event never happened."
- **Better:** "I did not find evidence in the sources I checked. My search did not cover these alternative terms and archives, so the claim remains unverified."
- **Fail:** "The AI did not cite this website, so its host must be blocking AI."
- **Better:** "Absence from the answer does not reveal whether the cause is DNS, permissions, indexing, retrieval ranking, relevance or another limit. Test each layer separately."
- **Fail:** "Indirect trade routes existed, therefore this exact shipment happened."
- **Better:** "The route makes the proposal worth investigating, but provides no shipment-level proof."

## Adoption in Aletheia

- **Aletheia Trust Check:** Apply this method to unverified fact claims. Keep `UNVERIFIED`, `NOT CHECKED` and `CONTRADICTED` distinct; record the search coverage and give proportionate `GO DEEPER` options.
- **Aletheia Improve / Site Audit:** Distinguish site access, crawl permission, index presence, AI retrieval and credibility.
- **AI Fluency:** Teach the distinction through a short worked exercise after the hallucination-and-verification lesson.
- **AIxpert (planned):** Use a test set containing inaccessible sources, translation variants, a false claim with convincing indirect context, and a genuinely refuted proposition. Grade search coverage, restraint and correct stopping decisions.
- **Protocol:** This document is **informative operational guidance** aligned with existing Principles 2, 3, 5, 7, 11 and 14. Any formal normative addition to the frozen Principles or versioned Specification requires its own reviewed proposal and decision.

## Provenance and publication

- **Origin:** User-approved Aletheia research principle and Go Walkabout conversation, 21 October 2026.
- **Conceptual background:** Kleppmann and Riccomini, *Designing Data-Intensive Applications*, second edition (2026), especially Chapters 1 and 9 on source systems, distributed information and partial failures. Applying those concepts to AI search is **Aletheia's original synthesis**, not a claim that the book prescribes this rule.
- **Proposed protocol change:** [PROP-RESEARCH-001](../proposals/PROP-RESEARCH-001.md); normative status remains pending review.

**Working motto:** *No search result is not proof of absence. Go Walkabout.*
