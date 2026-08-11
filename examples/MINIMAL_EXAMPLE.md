# Minimal Worked Example

## Nodes

```yaml
- node_id: claim-bridge-001
  node_type: Claim
  title: Bridge inspection is current
  lifecycle: active
  truth_status: contested
  statement: "The inspection is current."
  source_refs: [ev-email-001]
  conflict_set: [conflict-bridge-001]
  created_at: 2026-08-01
  created_by: project-manager
  privacy_class: project-private
  steward_review: required

- node_id: evidence-gap-bridge-001
  node_type: EvidenceGap
  title: Signed inspection report unavailable
  lifecycle: active
  truth_status: supported
  statement: "The signed report expected to confirm inspection date and scope has not been supplied."
  source_refs: []
  conflict_set: [conflict-bridge-001]
  created_at: 2026-08-02
  created_by: reviewer
  privacy_class: project-private
  steward_review: required

- node_id: conflict-bridge-001
  node_type: Conflict
  title: Current-inspection claim versus absent report
  lifecycle: active
  truth_status: supported
  statement: "The email claim cannot presently be reconciled with the missing signed report."
  source_refs: [ev-email-001]
  conflict_set: [claim-bridge-001, evidence-gap-bridge-001]
  created_at: 2026-08-02
  created_by: reviewer
  privacy_class: project-private
  steward_review: required
```

## Correct retrieval behaviour

Retrieving `claim-bridge-001` requires retrieval of `conflict-bridge-001` and the material conflicting side `evidence-gap-bridge-001`. The email's hash may prove that the same email was retrieved; it cannot prove that the claimed inspection occurred or covered the relevant scope.

## Appropriate conclusion

The project may report that an identified person claimed the inspection was current. It must not report the inspection as confirmed until suitable evidence resolves the gap and scope.

