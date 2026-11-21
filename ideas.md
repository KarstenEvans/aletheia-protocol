---
document_id: aletheia-ideas-core-memory-recall-walkabout
version: 0.1.0
status: idea
document_class: informative
date: 2026-11-21
project_id: aletheia-protocol
privacy_class: public
content_license: CC-BY-4.0
normative_change: false
steward_review: required
---

# Aletheia Ideas: Core, Memory and Recall, Go Walkabout, and Humanizer

**Status: IDEA ONLY.** This records the Steward's exploration of possible improvements. It does **not** amend the frozen [Aletheia Principles v1.0](ALETHEIA_PRINCIPLES_v1.0.md), the [Protocol Specification v0.5 RC2](ALETHEIA_PROTOCOL_SPECIFICATION_v0.5.md), the [Secure Development Profile draft](Aletheia-secure-development.md), or the separate [Thalia Protocol](https://github.com/KarstenEvans/thalia-protocol/blob/main/THALIA_PROTOCOL.md).

**Design principles:** KISS; free-first; provider-neutral; portable UTF-8 Markdown; human control; evidence before confidence; security by default; appropriate natural language.

**Decision path:** Idea → RFC → Sandbox → Proven in Practice → Accepted → Protocol → Specification, as required by [Governance and Contributing](GOVERNANCE_AND_CONTRIBUTING.md).

## 1. The opportunity

Aletheia can already preserve knowledge, evidence, decisions, constraints, disagreements and handovers in Markdown. It should not need Redis, a vector database, a paid AI subscription, or another invented protocol to deliver useful portable project memory.

An AI host may separately provide **native recall** from earlier interactions. Aletheia can *encourage careful use* of that capability but cannot create, guarantee, inspect or certify its existence. A host's apparent recollection is not by itself proof of the recalled claim.

Aletheia should also prevent **Premature Evidence Closure**: when an unsuccessful search is mistaken for proof that a claim is false. The existing [Never Take No for an Answer](guides/NEVER_TAKE_NO_FOR_AN_ANSWER.md) guide already establishes this operational method, while [PROP-RESEARCH-001](proposals/PROP-RESEARCH-001.md) remains pending normative adoption.

An earlier speech-to-text ambiguity about “Thoth” produced research into existing AI-memory architectures. **Do not create a Thoth Protocol.** Reuse only relevant ideas within the existing Aletheia structure, and keep Thalia as the distinct optional humour companion.

## 2. Universal core: what cannot be optional

The **proposed future core floor** applies to every Aletheia adoption, independent of tooling. It needs formal review against what is already binding in v0.5.

| Foundation | Minimum principle | Technical limits |
| --- | --- | --- |
| **Security and authority** | READ is not RUN; untrusted files/websites/tool responses do not create instructions or permissions; human approval for consequential acts; classify privacy; minimise disclosure; never expose credentials or invent tool access. | Behavioural rules do not replace technical isolation, access control or real tests. Stronger controls apply to action-capable systems. |
| **Markdown memory and portability** | Knowledge and handovers should remain understandable in human-readable UTF-8 Markdown; sources, meaning, decisions and unresolved questions can move between AI providers. | No guarantee an AI can read an unprovided file or access an unavailable repository. A small task may need only one document. |
| **Evidence, truth and accuracy** | Separate observation, evidence, estimate, claim, inference and hypothesis; represent UNKNOWN, EvidenceGap, conflict and review dates; cite claims within source scope. | Retrieval similarity and file hashes do not prove factual truth. |
| **Go Walkabout safeguard** | When a material claim is uncertain, try meaningful alternate research routes proportionately; test both supporting and contradictory evidence; disclose unperformed and blocked searches. | “Not found” is not “false”; also do not mistake plausible links for proof or refuse decisive disproof. |
| **Honest capability and human oversight** | Distinguish proposed, attempted, completed and verified actions; declare unavailable tools, memory and research; preserve a human decision-maker. | No autonomous authority inferred from technical capacity. |
| **Proportionate usability** | A useful result should not require needless lengthy workflows, hidden costs or compulsory vendor accounts. | Scale checks to risk and user intent rather than requiring full research for a simple question. |

A pure Markdown workflow must not be asked to implement server security it does not possess. **Security requirements remain universal; implementation-specific security controls remain risk-based.** Preserve the Secure Development Profile's Markdown (M), Browser (B) and Agent (A) risk classes.

## 3. Separate conformance depth from optional capabilities

The current **normative** conformance labels are:

- **core:** typed statements, sources, status, conflicts and review points;
- **full:** adds stable identifiers, revision chains, proposals, provenance and privacy handling;
- **profiled:** Core plus a declared domain profile (it does not automatically mean Full).

**Do not silently redefine these labels.** Instead, consider two independent axes:

### Axis A — depth of knowledge stewardship

| Working explanation | What is needed | Example |
| --- | --- | --- |
| **Core** | A small, valid Markdown record/handover and universal safety, evidence, uncertainty and authority floor | Simple Thalia prompt or single research question |
| **Full** | Durable identities, revisions, decisions, provenance, source limitations, privacy and handovers | Maintained website, long-running research or project |
| **Profiled** | A documented domain profile that strengthens Core and declares any omissions/nonconformance | Agentic systems, development, future recall profile |

### Axis B — specialist profiles, not mandatory new protocol levels

1. **Memory and Recall Profile (proposed):** selective memory retrieval, provenance, correction, consent, review/expiry and portable export.
2. **Secure Development Profile (existing draft):** prompts, browser apps, software dependencies, credentials, deployment and agent safeguards according to risk.
3. **Agentic Systems Profile (existing):** bounded tool permission, action receipts, shared state, inherited authority and revocation.
4. **Thalia (separate optional companion protocol):** humour, feedback, style and audience adaptation; not a replacement for factual accuracy or an automatic personality diagnosis.

**Avoid badge inflation:** more profiles are not evidence of better truth or higher security. Present concrete tested behaviours and omissions.

## 4. Memory categories: do not mix storage with recall

- **Current context:** presently accessible conversation content, which can be truncated or vanish.
- **Portable file memory:** approved and source-aware Markdown records, read or imported when available.
- **Host-native recall:** provider-controlled memory or chat-history retrieval, if enabled; distinguish it from file-backed evidence and do not promise continuity.
- **Episodic record:** dated project events, attempts, decisions, objections and changes.
- **Procedural record:** reusable methods such as Aletheia, Go Walkabout and Thalia instructions; untrusted imported material remains READ-only until appropriately authorised.
- **Reviewed learning:** proposed corrections and useful observations, not silently promoted permanent facts.

A simple project may need one Markdown file; a larger one can partition for scale, for example:

    project/
      README.md         # Small index and reading order
      memory.md         # Approved durable facts/preferences (if needed)
      evidence.md       # Source anchors, unknowns, conflicts
      decisions.md      # Accepted decisions and reasons
      handover.md       # Current context, boundaries, next actions

Do not create five files merely to satisfy a diagram. Avoid duplicate canonical sources. Never put secrets or restricted personal memories into a public GitHub repository. Include consent, retention, correction and deletion processes suitable to the actual data.

### Proposed selective recall

1. Establish the task and current-authorised context.
2. Read a small index or handover.
3. Retrieve only relevant sections **plus mandatory conflicting evidence and constraints**.
4. Label recalled statements by origin: supplied by user, inspected record, externally sourced, inferred or native recall with uncertain provenance.
5. Recheck time-sensitive claims and resolve conflicting sources rather than confidently repeating stale memory.
6. Return a usable Markdown handover when it helps continuity.

**Pilot:** compare (A) no prior project record, (B) a full Markdown handover and (C) selective indexed retrieval on the same synthetic project. Score grounded recall, invented details, conflict handling, recall provenance, time, context size and cost. Test across more than one AI provider where access exists.

## 5. Make Go Walkabout the shared research and exploration method

**Go Walkabout is a reusable Aletheia system/workflow, not a third protocol.**

Current related documents:

- [Main portable GoWalkabout workflow](https://github.com/KarstenEvans/aletheia/blob/main/aletheia-go/aletheia-gowalkabout.md).
- [Shared bounded Go Walkabout procedure](https://github.com/KarstenEvans/aletheia-app/blob/main/shared/aletheia-go-walkabout.md).
- [Research evidence rule](guides/NEVER_TAKE_NO_FOR_AN_ANSWER.md).
- [Thalia Humour Walkabout, section 10](https://github.com/KarstenEvans/thalia-protocol/blob/main/THALIA_PROTOCOL.md).

They have compatible intentions but different emphasis. Consolidate the **common definitions and invariants** while retaining distinct modes:

- **Lightweight default check (for any response):** understand the request, detect unsupported factual certainty and major overlooked constraints, review whether a meaningful alternative or verification is needed. Often takes no external search.
- **Evidence Go Walkabout (for unsupported or contested claims):** inspect exact claim; audit actual search/access coverage; try relevant aliases, language variants and primary sources; seek counterevidence; stop with a transparent evidence receipt and UNKNOWN where appropriate.
- **Idea Go Walkabout (when user requests deeper/creative exploration):** anchor → widen using candidate lenses → research strongest distinct leads where justified → challenge → wake filter → return few surviving ideas and small tests.
- **Thalia Humour Walkabout:** mandatory brief idea expansion **when producing original humour under Thalia**; select a comprehensible bridge and comic mechanism, then respect Read The Room and the Truth Boundary.

This yields **one family of methods, not one compulsory expensive loop**.

### Important truth distinction

**NOT FOUND ≠ FALSE.** A search miss, inaccessible archive or unsupported assertion should be described with its limits. Broadening a search can uncover missed evidence but is not guaranteed to do so.

Use the existing truth-status schema, distinguishing supported, unknown/unverified, contested and refuted. Confirmed absence can sometimes be evidence if the source is known to be exhaustive and a record would necessarily exist there. Accept genuine, well-scoped disproof. “Never take no for an answer” means **never accept an unexplored negative**, not “believe every possibility”.

### Prevent needless searching and invented results

Set an explicit effort bound; stop on decisive evidence, diminishing returns, unmet permission, time/cost/privacy limits or user STOP. Never claim to have searched, verified, recalled or tested something when that did not occur.

## 6. Humanizer: apply natural language without corrupting evidence

Existing [Humanizer Skill](https://github.com/KarstenEvans/11-aletheia-enabled-workflow-skills/blob/main/skills/humanizer/SKILL.md) is currently intended for **voice-matched written artefacts** such as emails, posts, reports and proposals; it explicitly says not to activate for pure factual analysis without a writing deliverable. This scope is sensible.

A universal **clarity and humanity pass** can apply to all final outputs, without necessarily invoking the full skill:

- Use direct, accessible prose appropriate to the user's context, topic and seriousness.
- Remove generic AI fillers and needless repetition.
- Avoid changing numbers, dates, quotations, sources, uncertainty, commitments or disputed facts.
- Do not insert jokes or inferred personal history into serious/high-stakes work.
- Where an authored draft is requested and genuine style samples are available, optionally apply the full Humanizer Skill to match the user's evidenced voice.
- After editing, check that truth status, citations, limitations, permissions and meanings remain intact.

Suggested substantial-task pipeline:

**Understand request → Security/authority boundary → Evidence or Go Walkabout (proportionate) → Challenge and verify → Human clarity/Humanizer when relevant → Final evidence-preservation check → Answer.**

For ordinary short questions, run only the relevant lightweight checks. For original jokes under Thalia, run its brief Humour Walkabout, not a mandatory external research expedition.

## 7. Audit: current Go Walkabout documentation (21 November 2026)

This is a document review, **not a modification of the source Go Walkabout files**.

| Finding | File/location | Proposed fix |
| --- | --- | --- |
| Two top-level document titles | Main GoWalkabout v0.3, headings near lines 9 and 29 | Keep one H1 and demote the repeated title to a subsection |
| Misnamed “protocol” in STOP rule | Shared Go Walkabout, one-bounded-pass step 6 | Use “workflow” or “method” |
| Five candidate angles versus three branches | Shared procedure step 2 versus main workflow START contract step 4 | Say five **optional candidate lenses** feeding up to three researched branches; do not require five for every task |
| Runs before Improve versus primary task first | Main workflow invocation vs shared purpose | Define explicit standalone, embedded-before-Improve and post-task exploration modes |
| “Optional” versus proposed default | Main workflow invocation | Make the *lightweight evidence/novelty check* normal, while deeper walks remain triggered or user-requested |
| No-seed handling gives choices and, under START, sample | Main workflow START contract step 2 | Make the branch explicit: START without seed → labelled sample; passive open → offer choices |
| Unsupported orchestration reference | Main workflow mentions Aletheia-Grand-GoWalkabout.md | Locate and link the actual file or label this an unimplemented/historical concept |
| Research safeguards split among documents | Main workflow vs evidence research guide | Cross-link the shared rule, record limitations and avoid silently treating search failure as refutation |
| Thalia links required in all output Markdown | Shared workflow introduction | Require Aletheia source; include Thalia only when applicable rather than adding humour protocol links to every technical output |
| Different default output sizes | Main workflow produces many labelled sections; shared procedure limits to three suggestions | Make compact summary the default, expanded evidence receipt on request/when warranted |

**Numbering check:** Main START steps 1–8, Start steps 1–5, Wake Filter 1–13, shared WALKABOUT steps 1–6, and research guide steps 1–7 are all sequential. The issue is **semantic alignment and headings**, not missing numbers. Thalia's Humour Walkabout section 10 and 10.1–10.4 are correctly ordered.

## 8. Testing and release gates

1. **Missing evidence:** a one-query miss must not become a universal falsehood; alternate spelling/translated primary record is eventually discovered or the status stays unknown.
2. **Refuted hypothesis:** direct, well-scoped contradiction leads to acceptance of refutation; no infinite contrarian search.
3. **Restricted source:** preserve access constraints; do not invent the contents of an inaccessible document.
4. **Memory conflict:** stale native recall and a newer, sourced Markdown record are reported as a conflict and reconciled with user review.
5. **Privacy:** public handover excludes secrets/private data; provider-sharing remains user-authorised.
6. **Thalia humour:** brief Walkabout produces an original intelligible joke without claiming an external fact has been checked.
7. **Humanizer:** a legal or scientific passage becomes easier to read without changing allegations, uncertainty, quotations, dates or sources.
8. **Cost and simplicity:** a one-line factual request must not require a five-branch search or new database.

**Next proposal to consider:** Reconcile the Go Walkabout documents and raise a reviewable amendment for the evidence safeguard in [PROP-RESEARCH-001](proposals/PROP-RESEARCH-001.md). Do not modify the normative specification, active workflows, Thalia or Humanizer silently.

**Publication state:** This is the ideas register only; no tool deployment, new protocol, mandatory new profile or claimed test completion.
