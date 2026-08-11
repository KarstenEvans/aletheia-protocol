# Changelog

## 0.5.0-rc.2 — 2026-08-11 — Licensed Steward Review Candidate

- Recorded the attributable acceptance of `PROP-AGENTIC-001` by Karsten Evans.
- Confirmed **Aletheia Protocol** as the project name and `https://github.com/KarstenEvans/aletheia-protocol` as the canonical public repository under the accountable Originating Steward's account.
- Licensed knowledge materials under CC BY 4.0 and executable software under Apache License 2.0.
- Added the root licence scope, attribution notice and complete standard licence texts.
- Updated adoption, governance, publication and contribution guidance to match the licence decision.
- Preserved RC1 as an immutable earlier review package; RC2 supersedes it as the current candidate.

## 0.5.0-rc.1 — 2026-08-11 — Steward Review Candidate

- Preserved Principles v1.0 unchanged.
- Added the optional Agentic Systems Profile for action-capable, persistent and multi-agent projects.
- Distinguished declared rationale from observable behaviour; explanations, apologies and promises are not treated as proof of intent or future alignment.
- Added scoped authority envelopes and action receipts for consequential external actions.
- Added population-level provenance across actors, short-lived runs, persistent state and inherited artefacts.
- Required shared writable infrastructure to be considered as a potential coordination channel.
- Added boundary-event handling and substitute-path review after a channel or capability is closed.
- Added a conservative reality rule: uncertainty about simulation does not authorise real-world action.
- Added scale-aware review of action volume, rate, parallelism and persistence.
- Added a source-bounded case study based on the July 2026 OpenAI/Hugging Face and AISI incidents.
- Corrected secondary-summary drift: Hugging Face reports rebuilding one core cluster, not one third of its infrastructure; motive and generalisation claims remain bounded by source limitations.
- Added repository and publication guidance for one canonical GitHub source with generated website and release renditions.
- Corrected the Originating Steward's name to **Karsten Evans**; “Carsten” in the 0.4 collected edition was an error.
- Retained 0.4 compatibility and the frozen Principles; this candidate remained pending attributable Steward acceptance.

## 0.4.0 — 2026-08-05 — Public Review Draft

- Consolidated repeated guidance into one normative specification.
- Declared Principles v1.0 frozen.
- Added Core, Full and Profiled conformance levels.
- Expanded first-class node types beyond Observation.
- Separated lifecycle from truth status.
- Made unresolved-conflict retrieval mandatory.
- Replaced “anchor match = 100% confidence” with bounded identity/integrity language.
- Prohibited treating semantic similarity as epistemic confidence.
- Split uncertainty into integrity, source identity, epistemic support, applicability and completeness.
- Clarified stable node identity, immutable revision identity and canonical-body hashing.
- Added time, privacy, redaction and image/region locator support.
- Added claim-specific source authority and evidence limitations.
- Added proposal/decision revision workflow.
- Added explicit AI adoption states and scope.
- Clarified that provenance does not expose private chain-of-thought.
- Added human authority, safety and professional-review boundaries.
- Retained compatibility profiles for `aletheia-handover/0.3` and `aletheia-case-record/0.3`.

## Migration from 0.3

- Map old `status` into separate `lifecycle` and `truth_status`.
- Replace numerical overall confidence with separate dimensions.
- Rename deterministic “100% confidence” statements to `integrity: matched` or bounded equivalent.
- Add `conflict_set` and retrieve unresolved conflicts automatically.
- Keep stable node IDs; place versioning in `revision` and `revision_id`.
- Record similarity model, score and corpus only as retrieval metadata.
