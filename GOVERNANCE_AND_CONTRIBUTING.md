# Governance and Contributing

## Stewardship model

Aletheia uses stewardship rather than model ownership. The originating Steward maintains the canonical public-review release until governance is broadened or delegated.

No AI contributor, repository maintainer or distribution channel becomes an authorised Steward merely by hosting, generating or transmitting protocol material.

## Maturity path

`Idea → RFC → Sandbox → Proven in Practice → Accepted → Protocol → Specification`

No stage should be claimed without evidence that its criteria were met.

## Proposing a change

Use:

```yaml
proposal_id: prop-aletheia-YYYYMMDD-short-name
target: document-id and section
change_type: clarify | revise | add | remove | split | merge | supersede
problem: bounded description
proposed_text: text or patch
reason: why this improves the protocol
evidence_or_case: links or included test case
compatibility: compatible | breaking | unknown
privacy_or_safety_effect: none or explanation
proposed_by: name, organisation, AI system, or pseudonym
proposed_at: ISO-8601 date
decision: pending
```

## Acceptance criteria

A normative change should be:

- understandable by humans and multiple AI systems;
- testable in a realistic project;
- no more complex than the risk requires;
- compatible where practical;
- explicit about privacy, safety and authority;
- accompanied by migration notes if breaking.

AI recommendations are proposals. Acceptance remains an attributable Steward decision.

A profile change involving external actions, persistent coordination or safety boundaries MUST include a realistic abuse or failure case, an authority analysis, evidence limitations and a test showing how the proposed control can fail.

## Independent review

Reviewers are encouraged to try to falsify assumptions, locate cases where metadata exceeds value, test non-English interchange, test restricted or missing evidence, and identify where the protocol could create false confidence.

For agentic profiles, reviewers SHOULD also test whether:

- a system can substitute another shared-state or communication path;
- short-lived runs inherit capabilities without visible lineage;
- technical capability is mistaken for permission;
- declared reasoning is treated as stronger evidence than observable action;
- many individually low-risk actions create material cumulative risk;
- shutdown, apology or apparent compliance is accepted without independent verification.

## Repository governance

The canonical repository MUST identify its Steward, current accepted release, release candidates and superseded material. Normative changes enter through proposals and attributable decisions. Website pages, Word files, ZIP bundles, social posts and AI handovers are renditions; they MUST link to or identify the canonical tagged revision and MUST NOT silently diverge.

## Contribution licensing

By submitting material for inclusion, a contributor confirms that they have the right to contribute it and agrees that an accepted contribution may be distributed under the licence applicable to the material it changes: CC BY 4.0 for knowledge materials and Apache License 2.0 for software. Material requiring different terms MUST be identified before submission and accepted explicitly by the Steward.
