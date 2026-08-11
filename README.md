# Aletheia Protocol 0.5 RC2 — Public Review Candidate

**Release date:** 2026-08-11  
**Status:** Licensed release candidate; Agentic Systems proposal accepted; independent review pending  
**Canonical format:** UTF-8 Markdown with YAML front matter  
**Originating Steward:** Karsten Evans, developed through human–AI collaboration

## What Aletheia is

Aletheia is a human-and-AI knowledge stewardship protocol. It helps a project preserve evidence, meaning, disagreement, decisions and revision history across people, AI systems and software tools.

Its central rule is:

> Knowledge belongs to the project, not the Assistant.

Aletheia is not a truth machine. It does not make an AI authoritative, expose private chain-of-thought, or prove that a source is correct. It creates a portable record that makes claims easier to inspect, challenge, revise and hand over.

## Start here

- `ALETHEIA_PROTOCOL_SPECIFICATION_v0.5.md` — normative requirements.
- `ALETHEIA_PRINCIPLES_v1.0.md` — stable design principles.
- `ADOPTION_AND_AI_HANDOVER_GUIDE.md` — how another AI or organisation can adopt it.
- `ALETHEIA_ALL_IN_ONE_AI_BOOTSTRAP_v0.5.md` — single-file paste-ready edition.
- `profiles/AGENTIC_SYSTEMS_PROFILE_v0.1.md` — authority, action and population-provenance rules for agentic work.
- `proposals/PROP-AGENTIC-001.md` — accepted proposal, evidence review and decision record for the new profile.
- `REPOSITORY_AND_PUBLICATION.md` — canonical repository and public-site policy.
- `CHANGELOG.md` — differences from the earlier working format.
- `GOVERNANCE_AND_CONTRIBUTING.md` — proposal and review process.
- `OPEN_ADOPTION_NOTICE.md` — permission and attribution notice.
- `LICENSE` and `LICENSES/` — scope and complete CC BY 4.0 and Apache 2.0 terms.
- `templates/` — reusable project, node, handover and provenance templates.
- `examples/MINIMAL_EXAMPLE.md` — small worked example.
- `examples/AGENTIC_INCIDENTS_2026_CASE_STUDY.md` — evidence-bounded stress test for the profile.

## Minimal adoption

An AI can participate without special software:

1. Read the specification or all-in-one bootstrap.
2. State `adopted`, `partially_adopted`, `not_adopted`, or `undecided`.
3. Separate evidence from claims and hypotheses.
4. retrieve unresolved conflicts with the challenged node.
5. cite source locators and record material gaps.
6. propose changes instead of silently rewriting accepted knowledge.
7. return a provenance trace and human-review points.

If agents can act externally, coordinate across runs or inherit shared state, also declare whether the Agentic Systems Profile is adopted and identify the applicable authority envelope.

## Normative hierarchy

If documents conflict, use this order:

1. `ALETHEIA_PROTOCOL_SPECIFICATION_v0.5.md`
2. an accepted project-specific specification
3. accepted decision records
4. templates
5. guides and examples

The Principles guide interpretation but do not erase explicit protocol requirements.

## Safety and authority

Aletheia does not override law, professional duties, organisational controls, platform policy or AI safety rules. Adoption creates no authority to act. High-impact decisions remain subject to the authorised human or institution.

## Canonical repository

The confirmed project name is **Aletheia Protocol**. Its canonical public repository is `https://github.com/KarstenEvans/aletheia-protocol`, under the accountable Originating Steward's GitHub account. Markdown is authoritative; Word, ZIP and website editions are renditions generated from tagged releases. GitHub Pages may publish the same repository, while GitHub Discussions may collect questions and RFC discussion. Social channels may link to releases but MUST NOT become competing sources of truth.

## Licence

Knowledge materials are freely available under **CC BY 4.0**. Executable tools and future software explicitly identified as such are freely available under **Apache License 2.0**. See `LICENSE` for exact scope, attribution and exclusions.
