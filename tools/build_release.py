#!/usr/bin/env python3
"""Build the Aletheia collected Markdown, checksum manifest and release ZIP."""

from __future__ import annotations

import hashlib
from pathlib import Path
import zipfile


ROOT = Path(__file__).resolve().parents[1]
COLLECTED = ROOT / "Aletheia_Protocol_0.5_RC2_Complete_Collected_Documents.md"
MANIFEST = ROOT / "MANIFEST.sha256"
ZIP_PATH = ROOT.parent / "Aletheia_Protocol_0.5_RC2_Public_Review.zip"
GITHUB_ZIP_PATH = ROOT.parent / "Aletheia_Protocol_0.5_RC2_GitHub_Source.zip"

ORDER = [
    "README.md",
    "ALETHEIA_PRINCIPLES_v1.0.md",
    "ALETHEIA_PROTOCOL_SPECIFICATION_v0.5.md",
    "profiles/AGENTIC_SYSTEMS_PROFILE_v0.1.md",
    "proposals/PROP-AGENTIC-001.md",
    "ADOPTION_AND_AI_HANDOVER_GUIDE.md",
    "GOVERNANCE_AND_CONTRIBUTING.md",
    "REPOSITORY_AND_PUBLICATION.md",
    "LICENSE",
    "OPEN_ADOPTION_NOTICE.md",
    "CHANGELOG.md",
    "templates/PROJECT_SPECIFICATION_TEMPLATE.md",
    "templates/NODE_TEMPLATE.md",
    "templates/HANDOVER_TEMPLATE.md",
    "templates/PROVENANCE_TRACE_TEMPLATE.md",
    "templates/AGENTIC_ACTION_RECEIPT_TEMPLATE.md",
    "examples/MINIMAL_EXAMPLE.md",
    "examples/AGENTIC_INCIDENTS_2026_CASE_STUDY.md",
    "ALETHEIA_ALL_IN_ONE_AI_BOOTSTRAP_v0.5.md",
]


def anchor(path: str) -> str:
    return path.lower().replace("/", "__").replace(".", "").replace("_", "-")


def build_collected() -> None:
    missing = [name for name in ORDER if not (ROOT / name).is_file()]
    if missing:
        raise SystemExit(f"Missing release files: {missing}")

    header = """---
audience: independent AI reviewer
compatibility:
  - aletheia-protocol/0.4
  - aletheia-handover/0.3
  - aletheia-case-record/0.3
date: 2026-08-11
document_class: normative_collection
document_id: aletheia-protocol-0.5-rc2-collected
protocol_status: release_candidate
protocol_version: 0.5.0-rc.2
purpose: single-file cross-AI adoption, independent review and handover
status: release_candidate
steward: Karsten Evans
title: Aletheia Protocol 0.5 RC2 — Complete Collected Documents
truth_status: provisional
---

# Aletheia Protocol 0.5 RC2 — Complete Collected Documents

This generated rendition combines the controlled Markdown files in the release package. The modular files remain canonical for editing. The Agentic Systems proposal, canonical repository and public licence are accepted; independent review remains invited before a stable 0.5 release.

"""
    sections = []
    for name in ORDER:
        text = (ROOT / name).read_text(encoding="utf-8").strip()
        sections.append(f'<div id="{anchor(name)}">\n\n{text}\n\n</div>')
    COLLECTED.write_text(header + "\n\n".join(sections) + "\n", encoding="utf-8")


def release_files() -> list[Path]:
    return sorted(
        path for path in ROOT.rglob("*")
        if path.is_file()
        and "__pycache__" not in path.parts
        and path != MANIFEST
    )


def build_manifest() -> None:
    lines = []
    for path in release_files():
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        lines.append(f"{digest}  {path.relative_to(ROOT).as_posix()}")
    MANIFEST.write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_zip() -> None:
    with zipfile.ZipFile(ZIP_PATH, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(list(release_files()) + [MANIFEST]):
            arcname = Path(ROOT.name) / path.relative_to(ROOT)
            archive.write(path, arcname.as_posix())


def build_github_zip() -> None:
    excluded = {
        COLLECTED,
        ROOT / "Aletheia_Protocol_0.5_RC2_Complete_Collected_Documents.docx",
        MANIFEST,
    }
    source_files = [path for path in release_files() if path not in excluded]
    with zipfile.ZipFile(GITHUB_ZIP_PATH, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in source_files:
            arcname = Path("aletheia-protocol") / path.relative_to(ROOT)
            archive.write(path, arcname.as_posix())


if __name__ == "__main__":
    build_collected()
    build_manifest()
    build_zip()
    build_github_zip()
    print(COLLECTED)
    print(MANIFEST)
    print(ZIP_PATH)
    print(GITHUB_ZIP_PATH)
