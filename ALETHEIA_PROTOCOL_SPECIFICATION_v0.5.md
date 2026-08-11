---
schema_version: aletheia-protocol/0.5
document_id: aletheia-protocol-specification
version: 0.5.0-rc.2
status: release_candidate
document_class: normative
date: 2026-08-11
content_license: CC-BY-4.0
compatibility: [aletheia-protocol/0.4, aletheia-handover/0.3, aletheia-case-record/0.3]
---

# Aletheia Protocol Specification 0.5 RC2

The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHOULD**, **SHOULD NOT** and **MAY** state requirement strength.

## 1. Scope

Aletheia defines a portable method for recording and transferring project knowledge among humans and AI systems. It specifies document roles, typed knowledge nodes, evidence links, conflict retrieval, revisions, provenance, adoption and Steward review.

It does not specify a database, embedding model, AI vendor, user interface or hidden reasoning format.

For projects involving action-capable, persistent or multi-agent systems, Aletheia also defines how a profile may record authority, external effects, cross-run lineage, shared-state interactions and boundary events. Aletheia records and tests observable evidence; it does not claim to reveal or verify private intent.

## 2. Conformance levels

An implementation MUST declare one level:

- `core`: preserves typed statements, sources, status, conflicts and review points.
- `full`: additionally implements stable identities, revision chains, proposals, provenance and privacy handling.
- `profiled`: implements Core plus a documented domain profile.

Partial implementations MUST identify omitted requirements and MUST NOT claim full conformance.

A Profiled implementation MUST identify the profile name and version. A profile MAY strengthen requirements but MUST NOT weaken Core requirements without declaring a non-conformance.

## 3. Roles

- **Steward:** accountable person or authorised body that accepts or rejects changes.
- **Contributor:** human or AI proposing material.
- **Reviewer:** independently tests evidence, logic, completeness and protocol use.
- **Custodian:** stores or controls source material; may differ from the Steward.
- **Rendition generator:** produces an output from the project specification.
- **Operator:** configures or runs a system and grants its tools, access or authority.

An AI MUST NOT claim authority, identity, verification, access or adoption it does not possess.

## 4. Document classes

Every controlled document SHOULD declare:

```yaml
document_id: stable-id
version: 1
status: draft | active | archived
document_class: normative | informative | example | historical
project_id: project-id
privacy_class: public | project-private | restricted
```

Normative requirements take precedence over guides and examples. Project specifications MAY strengthen the protocol but MUST document incompatible changes.

## 5. Knowledge node types

A material statement MUST be typed as one of:

- `Evidence`: a source artefact or bounded portion of one.
- `Observation`: something directly perceived or recorded, without causal explanation.
- `Measurement`: a value produced by an identified method, unit and conditions.
- `Estimate`: an approximate value and its method or basis.
- `Claim`: an assertion attributable to a person, organisation or source.
- `Hypothesis`: a testable possible explanation.
- `Assumption`: something temporarily treated as true for a defined purpose.
- `Conflict`: incompatible or materially tensioned nodes or sources.
- `EvidenceGap`: expected or decision-relevant evidence that is absent or unavailable.
- `Decision`: an authorised selection with reasons and consequences.
- `Action`: work proposed, in progress or completed.
- `Constraint`: a limit, prohibition, dependency or invariant.
- `Question`: unresolved discovery or decision question.

The node type describes epistemic function, not whether the statement is correct.

## 6. Minimum node schema

Core nodes MUST contain:

```yaml
node_id: stable-project-unique-id
node_type: Evidence | Observation | Measurement | Estimate | Claim | Hypothesis | Assumption | Conflict | EvidenceGap | Decision | Action | Constraint | Question
title: concise human-readable title
lifecycle: draft | active | archived
truth_status: supported | provisional | contested | refuted | superseded | unknown | not_applicable
statement: bounded statement
source_refs: []
conflict_set: []
created_at: ISO-8601 timestamp or date
created_by: attributable human, organisation, AI system, or unknown
privacy_class: public | project-private | restricted
steward_review: required | completed | not_required
```

Full-conformance nodes MUST additionally contain:

```yaml
revision: positive integer
revision_id: immutable revision identifier
previous_revision_id: identifier or null
body_sha256: SHA-256 of the canonical body, excluding body_sha256 itself
valid_from: date-time or null
valid_until: date-time or null
review_due: date-time or null
```

An identity MUST remain stable across ordinary revisions. A materially different proposition SHOULD receive a new `node_id` linked with an explicit relationship.

## 7. Type-specific requirements

### 7.1 Evidence and source references

An evidence reference SHOULD record:

```yaml
evidence_id: stable-id
title: source title
source_class: primary | secondary | derived | testimony | system-record | unknown
creator_or_speaker: name, role, pseudonym, redacted, or unknown
knowledge_basis: direct | reported | inferred | generated | unknown
source_created_at: date-time or unknown
retrieved_at: date-time
locator:
  file: filename-or-URI
  page: number-or-null
  lines: range-or-null
  region: bounding-box-or-description-or-null
integrity:
  algorithm: sha256 | none
  digest: value-or-null
claim_scope: what this source can support
limitations: []
```

A hash match MUST be described only as an integrity match. It MUST NOT be presented as proof that the source is factually correct.

### 7.2 Measurements

A Measurement MUST identify value, unit, method, operator or system, relevant conditions and uncertainty or precision where available.

### 7.3 Estimates

An Estimate MUST identify the estimation method or basis and MUST NOT be relabelled as a Measurement.

### 7.4 Claims

A Claim SHOULD identify speaker role, knowledge basis, claim scope, distance from the event and the source that records it. Official status alone MUST NOT imply authority outside the source's claim scope.

### 7.5 Hypotheses and assumptions

A Hypothesis SHOULD state supporting and contradicting evidence and what would distinguish it from alternatives. An Assumption MUST state its purpose, owner and expiry or review condition.

### 7.6 Evidence gaps

An EvidenceGap SHOULD record expected evidence, why it is expected, likely custodian, attempts made, consequence of absence, resolution route and review date.

### 7.7 Conflicts

A Conflict MUST link every known material side and MUST state whether it is unresolved, partially resolved or resolved. Resolution MUST reference a Decision or accepted proposal; deletion of one side is not resolution.

## 8. Truth Anchors

A Truth Anchor is a traceable relationship between a bounded statement and supporting source material. It MUST specify:

- the exact statement being supported;
- the source and locator;
- what the source establishes;
- what it does not establish;
- material limitations or conflicts.

The term does not mean infallible truth. It means inspectable grounding.

## 9. Retrieval

A task MUST declare `retrieval_mode` as:

- `anchor`: exact identifiers, controlled references or required constraints;
- `conceptual`: approximate discovery and contextual retrieval;
- `dual`: both.

Anchor retrieval establishes identity or integrity only to the extent tested. Conceptual similarity MUST be used for ranking or discovery, not epistemic confidence.

When a retrieved node has unresolved entries in `conflict_set`, the unresolved conflicts and their linked sides MUST also be retrieved or explicitly reported unavailable. This is **mandatory conflict retrieval**.

Retrieval logs SHOULD record query, corpus or supplied pack, retrieval system/version if known, ranks, raw scores if produced, threshold policy, included nodes and material exclusions. Scores from different systems MUST NOT be treated as directly comparable without validation.

## 10. Confidence and uncertainty

Aletheia MUST NOT create a single numerical “overall confidence” by averaging unlike measures. The following dimensions MAY be stated separately:

- `integrity`: confidence that the retrieved content matches the identified revision;
- `source_identity`: confidence that the source or speaker is correctly identified;
- `epistemic_support`: qualitative strength of support for the proposition;
- `applicability`: whether the evidence applies to the present time, scope and decision;
- `completeness`: whether material evidence or conflicts may be missing.

Qualitative labels MUST include reasons. Unknown values MUST remain unknown.

## 11. Time

Where time affects meaning, nodes SHOULD distinguish:

- `observed_at`
- `source_created_at`
- `retrieved_at`
- `valid_from`
- `valid_until`
- `review_due`

Current-state claims MUST be rechecked when their review date, validity period or external conditions require it.

## 12. Revision and change proposals

Accepted records MUST NOT be silently rewritten. A material change MUST use a proposal:

```yaml
proposal_id: prop-project-unique
target_node: node-id
change_type: revise | supersede | split | merge | archive | dispute
reason: concise reason
new_evidence: []
breaking_change: false
proposed_by: attributable contributor
proposed_at: ISO-8601
decision: pending | accepted | rejected | deferred
decided_by: authorised Steward or null
decision_reason: null
```

Accepted changes MUST preserve previous revision links and the decision record. Emergency corrections MAY be issued immediately when authorised, but the proposal and rationale MUST be recorded retrospectively.

## 13. Specifications and renditions

A project specification SHOULD define intention, success criteria, evidence, constraints, accepted decisions, known errors, mandatory exclusions, tests and required outputs.

A rendition is one replaceable output produced from that specification. Material learning from a rendition SHOULD be proposed back into the specification.

## 14. Provenance trace

A material rendition SHOULD include:

- task/specification ID;
- adoption and conformance declaration;
- trigger task;
- retrieval mode;
- anchor matches and integrity results;
- conceptual matches and retrieval metadata, if available;
- mandatory conflicts retrieved;
- material exclusions and unavailable sources;
- evidence referenced;
- uncertainty by dimension;
- changes proposed;
- Steward-review points.

When a task includes consequential external action or coordination across runs, the trace SHOULD also include actor and run identifiers, the applicable authority envelope, persistent-state reads and writes, coordination channels, action receipts and boundary events. The trace MAY link to separate logs rather than duplicate them.

A provenance trace records observable inputs and operations. It MUST NOT claim to expose private chain-of-thought.

## 15. Privacy and redaction

Projects MUST assign privacy classes. A cross-AI pack SHOULD contain only necessary information. Public or broadly shared packs SHOULD use stable redacted identifiers so source relationships survive sanitisation.

Redaction MUST NOT be represented as absence of the underlying information. Restricted evidence MAY be listed as withheld with its scope and custodian when lawful and safe.

## 16. Handover

A handover MUST state:

- project and schema identifiers;
- purpose and audience;
- reading order or included files;
- current state and priority;
- non-negotiable distinctions and constraints;
- confirmed anchors;
- unresolved conflicts and evidence gaps;
- rejected interpretations;
- required response;
- safety/privacy boundaries;
- Steward-review points;
- adoption declaration request.

For an action-capable or multi-agent project, the handover MUST also state the active authority boundaries, known persistent or shared state, unresolved boundary events and the location of relevant action receipts, or explicitly state that these records are unavailable.

## 17. Adoption declaration

Each participating AI or organisation SHOULD state one:

- `adopted`: commits to the declared conformance level for this work;
- `partially_adopted`: lists adopted and omitted requirements;
- `not_adopted`: explains incompatibilities;
- `undecided`: identifies evidence or decisions needed.

Adoption applies only to the declared task, project or organisational scope. It is not an endorsement of every conclusion in the project.

## 18. Safety, legality and professional boundaries

Aletheia does not override applicable law, consent, confidentiality, security controls, organisational policy, AI system policy or professional duties. It does not authorise external actions. Where mistakes could materially affect health, safety, liberty, employment, finances, property or rights, the handover MUST identify accountable human review.

Permission to inspect, reason, test or communicate MUST NOT be inferred as permission to take a consequential external action. Authority MUST be scoped to the actor, action, target, time and conditions actually approved; silence or technical capability is not authority.

## 19. Interoperability

The canonical representation is human-readable Markdown. YAML front matter MAY provide machine-readable metadata. Implementations MUST preserve meaning even when unsupported fields are passed through as opaque data.

Required IDs and enum values are case-sensitive ASCII. Human-readable prose MAY use any language, with translations linked as renditions of the same meaning.

## 20. Validation checklist

A conforming review asks:

1. Are material statements typed correctly?
2. Can important conclusions be traced to bounded sources?
3. Are estimates and measurements distinguished?
4. Are source authority and applicability claim-specific?
5. Do unresolved conflicts travel with retrieved claims?
6. Are missing sources represented as EvidenceGap nodes?
7. Are lifecycle and truth status separate?
8. Are identity, revision and hashes used correctly?
9. Are uncertainty dimensions kept separate?
10. Are privacy and human authority explicit?
11. Are accepted records changed only through proposals?
12. Does the rendition report provenance without inventing hidden reasoning?
13. Where external action is possible, is its authority explicit and bounded?
14. Are shared writable surfaces and cross-run state treated as possible coordination channels?
15. Are declared rationales kept distinct from observed actions and outcomes?
16. After a boundary event, were substitute paths considered rather than assuming one closed channel resolved the risk?

## 21. Versioning

Protocol versions use semantic versioning. During `0.x`, minor releases MAY contain breaking changes and MUST document them. Principles v1.0 are frozen; amendments require an explicit Principles proposal and Steward acceptance.

## 22. Agentic systems and population-level provenance

Projects within the scope of `profiles/AGENTIC_SYSTEMS_PROFILE_v0.1.md` SHOULD declare `profiled` conformance. If the profile is not used, the project MUST NOT imply that Aletheia has verified agentic authority, containment or alignment.

For such projects:

1. A declared rationale, explanation, apology or promise MUST be recorded as a Claim unless independently supported. It MUST NOT by itself establish alignment, future compliance or absence of deception.
2. Observable actions, tool calls, messages, state changes and externally confirmed outcomes SHOULD be preserved as bounded evidence or system records.
3. Shared writable infrastructure MUST be treated as a potential coordination channel whether or not it was designed for messaging.
4. Cross-run knowledge inheritance SHOULD preserve actor, run, source, write, read and revision lineage so that population-level capability does not appear to originate in a single run.
5. A consequential external action MUST be within an explicit authority envelope and SHOULD produce an action receipt. Unclear authority MUST fail closed or be escalated to the accountable human or institution.
6. Uncertainty about whether an environment, target or person is simulated MUST NOT be used to justify real-world action. When the distinction cannot be established, the system MUST treat the target as real and remain within explicit authority.
7. Closing one communication or persistence mechanism MUST NOT be recorded as resolution until materially equivalent substitute paths have been considered and the relevant controls retested.
8. Review SHOULD assess cumulative action volume, rate, parallelism and persistence, not only isolated model outputs.

The Agentic Systems Profile adds operational records for these requirements without requiring disclosure of private chain-of-thought.
