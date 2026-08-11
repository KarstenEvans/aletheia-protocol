---
document_id: aletheia-repository-publication-policy
version: 1
status: release_candidate
document_class: normative
date: 2026-08-11
steward_review: required
---

# Repository and Publication Policy

## Confirmed canonical home

The Originating Steward confirmed **Aletheia Protocol** as the project name and created the canonical public repository under the accountable Steward's GitHub account on 11 August 2026:

`https://github.com/KarstenEvans/aletheia-protocol`

The repository may later be transferred to an accountable organisation without changing the project name or repository name. Any transfer MUST preserve Git history, releases, redirects and human recovery control, and MUST be recorded before the new location is described as canonical.

## One source of truth

The canonical Markdown files in the repository are authoritative. Other formats are renditions:

- tagged GitHub Releases contain reviewed ZIP and Word editions;
- GitHub Pages publishes public documentation from the same tagged or main-branch source;
- GitHub Discussions hosts questions, review and early RFC conversation;
- Issues track bounded defects and accepted work;
- pull requests contain proposed changes and review evidence;
- Facebook, LinkedIn or other social channels announce and link to releases only.

A Google Business Profile is not an appropriate canonical location. It should be considered only if a genuine organisation later provides public-facing services associated with an eligible location or service area.

## Initial repository structure

```text
aletheia-protocol/
├── .gitignore
├── README.md
├── ALETHEIA_PRINCIPLES_v1.0.md
├── ALETHEIA_PROTOCOL_SPECIFICATION_v0.5.md
├── ALETHEIA_ALL_IN_ONE_AI_BOOTSTRAP_v0.5.md
├── CHANGELOG.md
├── GOVERNANCE_AND_CONTRIBUTING.md
├── LICENSE
├── LICENSES/
├── NOTICE
├── OPEN_ADOPTION_NOTICE.md
├── REPOSITORY_AND_PUBLICATION.md
├── profiles/
├── proposals/
├── templates/
├── examples/
├── index.md
└── _config.yml
```

GitHub Pages SHOULD publish from the repository root or from a workflow tied to the same source revision. Website navigation MAY be generated, but the protocol text MUST NOT be maintained as a separately edited copy.

## Release states

- `proposal`: not part of the protocol unless accepted.
- `release candidate`: coherent package awaiting Steward decision and independent review.
- `accepted release`: attributable Steward decision recorded and tagged.
- `superseded`: retained for audit but no longer current.

Tags SHOULD use forms such as `v0.5.0-rc.1`, `v0.5.0-rc.2` and `v0.5.0`. Release notes MUST link accepted proposals, known limitations and migration guidance.

## Licence policy

- Knowledge materials, including specifications, schemas, templates and examples, use CC BY 4.0.
- Executable material in `tools/`, and future software explicitly identified as such, uses Apache License 2.0.
- The root `LICENSE` file controls scope; `LICENSES/` contains the complete standard terms.
- Third-party material is not relicensed unless explicitly stated.

## Identity and recovery

- The canonical organisation MUST remain under accountable human control.
- The primary owner SHOULD enable multi-factor authentication and retain recovery codes securely.
- At least one additional trusted human owner SHOULD be added when governance broadens.
- AI systems MAY prepare commits and proposals but MUST NOT be represented as the accountable owner or Steward.
- A domain, if acquired, SHOULD be verified before it is attached to GitHub Pages.

## Publication checks

Before a release is published:

1. confirm the Steward decision and version;
2. validate Markdown links, schemas and internal references;
3. confirm that generated Word and ZIP files match the tagged Markdown;
4. remove secrets, private evidence and unnecessary personal data;
5. identify claims that remain provisional or contested;
6. preserve superseded releases and rejected proposals;
7. verify the public website points to the current accepted tag;
8. confirm the licence scope and complete standard licence texts are present and match the release.

## Pending Steward decisions

- Initial co-owner or succession arrangement.
- Whether GitHub Discussions is enabled immediately or after the first accepted release.
