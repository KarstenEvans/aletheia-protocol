---
schema_version: aletheia-profile/0.1
profile_id: aletheia-agentic-systems
profile_version: 0.1.0-rc.2
protocol_requires: aletheia-protocol/0.5
status: release_candidate
content_license: CC-BY-4.0
document_class: normative
date: 2026-08-11
steward_review: required
---

# Aletheia Agentic Systems Profile 0.1 RC2

## 1. Purpose

This profile extends Aletheia to projects in which AI systems can take consequential external actions, coordinate across concurrent or sequential runs, or inherit knowledge and capability through persistent shared state.

It makes authority and population-level provenance inspectable. It does not claim to infer private intent, guarantee containment, align a model, replace technical security controls or expose private chain-of-thought.

## 2. Applicability

The profile SHOULD be used when any of the following is true:

- an AI can send messages, publish, transact, change access, execute code or alter an external system;
- more than one run can read or write the same repository, directory, database, queue, cache, account or service;
- short-lived runs can inherit artefacts, credentials, instructions, exploits, plans or conventions;
- the cumulative volume, speed or parallelism of actions can create risk beyond any single output.

If a project within this scope does not adopt the profile, it MUST identify the omission and MUST NOT claim agentic conformance.

## 3. Terms

- **Actor:** attributable human, AI system, service or organisation capable of producing a record or action.
- **Run:** one bounded execution with a stable run identifier.
- **Population:** multiple concurrent or sequential runs whose work can affect one another.
- **Persistent state:** information or capability surviving a run.
- **Coordination channel:** any mechanism through which one actor or run can leave information or capability for another.
- **Authority envelope:** the bounded permission governing a consequential action.
- **Consequential action:** an external action that may materially affect a person, organisation, system, asset, right or safety condition.
- **Action receipt:** an observable record of a requested, authorised, attempted, completed, blocked or reversed consequential action.
- **Boundary event:** observed or suspected activity outside the declared authority, environment, target or communication boundary.
- **Declared rationale:** an actor's explanation of why it acted; this is a Claim unless independently supported.

## 4. Core rule: capability is not authority

An available tool, credential, network path, writable surface, broad objective or absence of a prohibition MUST NOT be treated as permission. Authority MUST be explicit enough to identify the permitted actor, action, target, time and conditions.

When authority is unclear, the action MUST be blocked or escalated to the accountable human or institution. An approval for one actor or run MUST NOT be silently transferred to another.

## 5. Agentic project manifest

A Profiled project MUST maintain a manifest containing at least:

```yaml
profile: aletheia-agentic-systems/0.1
project_id: stable-project-id
operator: accountable operator or organisation
steward: accountable knowledge Steward
actors: []
run_id_policy: how run IDs are assigned
objective: bounded objective
authority_envelopes: []
capabilities:
  tools: []
  network: none | restricted | open | unknown
  credentials: []
  external_actions: []
persistent_state: []
approved_coordination_channels: []
other_shared_writable_surfaces: []
monitoring_and_receipts: location or unavailable
termination_and_revocation: procedure or unavailable
privacy_class: public | project-private | restricted
steward_review: required | completed | not_required
```

The capability inventory SHOULD describe scope rather than disclose reusable secrets. A credential may be represented by a stable redacted identifier, custodian and permission scope.

## 6. Authority envelope

Each class of consequential action MUST link to an authority envelope:

```yaml
authority_envelope_id: auth-project-unique
authorised_by: accountable human or institution
actor_scope: []
action_scope: []
target_scope: []
purpose: bounded purpose
valid_from: ISO-8601
valid_until: ISO-8601 or null
rate_or_volume_limits: bounded limits or null
financial_or_resource_limits: bounded limits or null
required_approvals: []
prohibited_actions: []
escalation_conditions: []
revocation_state: active | suspended | revoked | expired
source_refs: []
```

An objective such as “complete the test,” “solve the problem” or “maximise the score” is not an authority envelope. The envelope MUST identify external targets and action classes deliberately.

## 7. Action receipts

A consequential action SHOULD produce an action receipt before or at execution. The record MUST distinguish a request, approval, attempt, outcome and later verification:

```yaml
action_receipt_id: receipt-project-unique
actor_id: stable-actor-id
run_id: stable-run-id
requested_action: bounded description
target: stable identifier or redacted reference
authority_envelope_id: auth-project-unique
approval_result: approved | denied | escalated | not_required | unknown
action_state: requested | attempted | completed | blocked | failed | reversed
requested_at: ISO-8601
acted_at: ISO-8601 or null
observed_effect: bounded observation or unknown
verification_source_refs: []
persistent_writes: []
privacy_class: public | project-private | restricted
boundary_event_id: null
```

An actor's statement that an action succeeded, failed, caused no harm or was harmless MUST remain a Claim until supported by an appropriate observation or external record.

## 8. Population-level provenance

The project SHOULD be able to reconstruct how material knowledge or capability moved across runs. For every consequential inherited artefact, record where available:

- creating actor and run;
- source evidence or prior artefact;
- time and persistent location written;
- later actors or runs that read or changed it;
- revision or integrity identifier;
- authority and privacy class;
- whether the inheritance was intended, authorised, unknown or prohibited.

The provenance trace MUST NOT attribute population-level learning solely to the final run when material work came from earlier runs.

## 9. Coordination and shared writable infrastructure

Every shared writable surface MUST be considered a potential coordination channel. Examples include repositories, filenames, directory names, logs, issue trackers, caches, package stores, datasets, error messages, queues and external accounts.

The project MUST distinguish:

- approved coordination;
- observed but unapproved coordination;
- possible channels not observed;
- channels whose existence or use is unknown.

Approved coordination SHOULD use attributable messages, stable channel IDs, bounded retention and access control. Removing one channel MUST NOT be recorded as resolving a coordination risk until materially equivalent substitute paths have been considered and the controls retested.

## 10. Declared rationale and behavioural evidence

Aletheia does not verify intent. A declared rationale, explanation, apology, promise, refusal or statement of cooperation MUST be represented as a Claim attributable to its source.

Review MUST keep separate:

1. what the actor said;
2. what the actor attempted or did;
3. what the environment allowed or blocked;
4. what independent evidence establishes about the outcome;
5. what remains unknown about motive, awareness or future behaviour.

Apparent compliance after detection MUST NOT by itself close a boundary event.

## 11. Simulation and reality uncertainty

If an actor cannot establish whether a person, account, service or system is simulated or real, it MUST treat the target as real. Uncertainty about the environment MUST NOT widen authority or justify external action.

Evaluations SHOULD provide explicit synthetic targets, unambiguous boundary markers and a solvable authorised route. Containment MUST NOT depend on the model choosing not to test a boundary.

## 12. Boundary events

A suspected boundary event MUST receive a stable identifier and SHOULD record:

- actor, run, time and observed action;
- intended boundary and evidence of the deviation;
- affected or potentially affected targets;
- persistent writes, credentials, accounts and channels involved;
- containment, revocation and notification actions;
- preserved evidence and unavailable evidence;
- substitute paths considered;
- current state: suspected, confirmed, contained, resolved or unresolved;
- accountable reviewer and review date.

Containment SHOULD preserve evidence before destructive cleanup where lawful and safe. Resolution MUST be supported by retesting or a documented reason why retesting is not possible.

## 13. Scale-aware review

Review MUST consider aggregate action volume, rate, parallelism, duration and persistence. Many low-severity actions MAY create a high-severity cumulative effect. Rate and volume limits SHOULD apply across the population, not only per run.

## 14. Least exposure and revocation

Capabilities SHOULD be least-privileged, short-lived, scoped and independently revocable. Shared credentials or authority spanning unrelated targets SHOULD be treated as a material risk. Persistent artefacts SHOULD carry expiry or review conditions where continued use could create harm.

## 15. Conformance declaration

A conforming declaration MUST state:

- `profiled: aletheia-agentic-systems/0.1`;
- manifest location;
- authority-envelope and action-receipt coverage;
- persistent-state and coordination-channel coverage;
- boundary-event status;
- known omissions and EvidenceGaps;
- accountable Steward and Operator review.

The declaration MUST NOT state or imply that profile use proves alignment, safety, containment or truthful reasoning.

## 16. Validation checklist

1. Is every consequential action class linked to explicit authority?
2. Are capability and authority kept separate?
3. Can material artefacts be traced across short-lived runs?
4. Are all known shared writable surfaces classified as channels, possible channels or unknown?
5. Are explanations and apologies treated as Claims rather than proof?
6. Does uncertainty about simulation fail closed?
7. Are action receipts grounded in observable results?
8. Are cumulative volume, speed, parallelism and persistence assessed?
9. After containment, were substitute paths considered and controls retested?
10. Are credentials, permissions and persistent artefacts scoped, reviewable and revocable?
