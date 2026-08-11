# Aletheia Provenance and Retrieval Trace

```yaml
task_or_specification_id: task-id
protocol_version: aletheia-protocol/0.5
adoption: adopted | partially_adopted | not_adopted | undecided
conformance: core | full | profiled
profile: name/version or null
trigger_task: bounded task description
retrieval_mode: anchor | conceptual | dual
supplied_corpus: files, project pack, or system scope
retrieval_system: name/version/unknown
actor_ids: []
run_ids: []
authority_envelope_id: null
```

## Anchor matches

For each: node or evidence ID, exact locator, reason, integrity result and limitation. Do not label a hash match as factual certainty.

## Conceptual matches

For each: node ID, relevance, rank, raw score if produced, corpus and threshold policy. Treat this as retrieval metadata, not truth confidence.

## Mandatory conflicts retrieved

List unresolved conflicts and all material sides. If unavailable, state that explicitly.

## Excluded or unavailable material

List material exclusions, redactions and evidence gaps with reasons.

## Evidence used

List bounded evidence locators and what each establishes or does not establish.

## Uncertainty

- Integrity:
- Source identity:
- Epistemic support:
- Applicability:
- Completeness:

## Changes proposed

List proposal IDs or `none`.

## Agentic provenance, if applicable

- Actor and run lineage:
- Persistent-state reads:
- Persistent-state writes:
- Intended coordination channels:
- Other shared writable surfaces considered:
- Consequential action receipts:
- Boundary events:
- Substitute paths tested after containment:

Declared rationales are Claims. Keep them distinct from observed actions and externally confirmed outcomes.

## Steward review

List every material decision, ambiguity, conflict, privacy issue or high-impact conclusion requiring accountable human review.
