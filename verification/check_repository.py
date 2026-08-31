#!/usr/bin/env python3
"""Dependency-free integrity checks for the public legal-research repository."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_ROW = re.compile(
    r"^\| `(?P<path>[^`]+)` \| (?P<size>[0-9,]+) \| `(?P<sha>[0-9a-f]{64})` \|$"
)
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\((?P<target>[^)]+)\)")
COMMIT = re.compile(r"^[0-9a-f]{40}$")
PR_ROW = re.compile(
    r"^\| \[#(?P<number>[1-5])\]\(https://github\.com/Sodelin/"
    r"legal-case-for-opt-in-Washington-State-sworn-statements-program-for-political-truth-program/"
    r"pull/(?P=number)\) \| Head `(?P<head>[0-9a-f]{40})`; base `(?P<base_ref>[^`@]+)@"
    r"(?P<base>[0-9a-f]{40})` \| \*\*(?P<disposition>CANONICAL REVIEW|DEPENDS_ON|SUPERSEDES|PARKED)\*\* \|"
)
ALLOWED_CLASSIFICATIONS = {"canonical", "candidate", "supplement", "archive", "withdrawn"}
ALLOWED_REVIEW_GATES = {
    "REMAND_SUPERSESSION",
    "REPOSITORY_VALIDATION",
    "INDEPENDENT_READBACK",
    "PRIMARY_AUTHORITY_AND_CITATOR",
    "ZOTERO_RECONCILIATION",
    "FACTUAL_COMPLETION",
    "COUNSEL_REVIEW",
    "METHODS_AND_COMPREHENSION",
    "LIVE_PROTOCOL_REVIEW",
}
EXPECTED_PR_RECORDS = {
    1: (
        "9b695f3e45e13d60767db71ed91cf4cc668c9d09",
        "main",
        "3905b470c2ab239cf2aae563e1d7b3a1adb73dd3",
        "PARKED",
    ),
    2: (
        "96c5388421ed6e221c8520878458feba96e14aac",
        "research/conversation-synthesis-and-evaluation-v1",
        "9b695f3e45e13d60767db71ed91cf4cc668c9d09",
        "DEPENDS_ON",
    ),
    3: (
        "08283fc190f23d69406b5f9cc810fbbc00d8b068",
        "legal/participant-protocol-and-memo-v1.1",
        "96c5388421ed6e221c8520878458feba96e14aac",
        "DEPENDS_ON",
    ),
    4: (
        "b99f7df6712a063e824922ede87b2c7ecca726f0",
        "main",
        "3905b470c2ab239cf2aae563e1d7b3a1adb73dd3",
        "CANONICAL REVIEW",
    ),
    5: (
        "73a036076096c0874478ccfdffdc5e605378765a",
        "main",
        "3905b470c2ab239cf2aae563e1d7b3a1adb73dd3",
        "PARKED",
    ),
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_bytes(path: Path) -> bytes:
    """Return bytes as stored in Git under the repository LF attributes."""
    data = path.read_bytes()
    if path.suffix.lower() in {".md", ".py", ".yml", ".yaml"}:
        return data.replace(b"\r\n", b"\n")
    return data


def manifest_rows(path: Path) -> list[tuple[str, int, str]]:
    rows: list[tuple[str, int, str]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        match = MANIFEST_ROW.match(line)
        if match:
            rows.append(
                (
                    match.group("path"),
                    int(match.group("size").replace(",", "")),
                    match.group("sha"),
                )
            )
    if not rows:
        raise ValueError(f"no checksum rows found in {path.relative_to(ROOT)}")
    return rows


def verify_manifest(manifest: Path, base: Path) -> list[str]:
    errors: list[str] = []
    try:
        rows = manifest_rows(manifest)
    except (OSError, UnicodeError, ValueError) as exc:
        return [str(exc)]

    for relative, expected_size, expected_sha in rows:
        target = base / relative
        if not target.is_file():
            errors.append(f"{manifest.relative_to(ROOT)}: missing {target.relative_to(ROOT)}")
            continue
        data = canonical_bytes(target)
        if len(data) != expected_size:
            errors.append(
                f"{target.relative_to(ROOT)}: canonical size {len(data)} != manifest {expected_size}"
            )
        actual_sha = sha256(data)
        if actual_sha != expected_sha:
            errors.append(
                f"{target.relative_to(ROOT)}: SHA-256 {actual_sha} != manifest {expected_sha}"
            )
    return errors


def verify_checksum_coverage() -> list[str]:
    errors: list[str] = []
    freeze_manifest = ROOT / "audit/CANONICAL_CHECKSUMS.md"
    archive_manifest = ROOT / "audit/ARCHIVE_CHECKSUMS.md"
    try:
        freeze_rows = manifest_rows(freeze_manifest)
        archive_rows = manifest_rows(archive_manifest)
    except (OSError, UnicodeError, ValueError) as exc:
        return [str(exc)]

    freeze_paths = [row[0] for row in freeze_rows]
    archive_paths = [row[0] for row in archive_rows]
    if len(freeze_paths) != len(set(freeze_paths)):
        errors.append("audit/CANONICAL_CHECKSUMS.md: duplicate repository paths")
    if len(archive_paths) != len(set(archive_paths)):
        errors.append("audit/ARCHIVE_CHECKSUMS.md: duplicate archive paths")

    expected_freeze = {
        path
        for path in repository_files()
        if path != "audit/CANONICAL_CHECKSUMS.md"
        and not path.startswith("archive/input-drafts/")
    }
    declared_freeze = set(freeze_paths)
    if expected_freeze - declared_freeze:
        errors.append(
            "audit/CANONICAL_CHECKSUMS.md: unhashed repository files "
            f"{sorted(expected_freeze - declared_freeze)}"
        )
    if declared_freeze - expected_freeze:
        errors.append(
            "audit/CANONICAL_CHECKSUMS.md: unexpected repository files "
            f"{sorted(declared_freeze - expected_freeze)}"
        )

    expected_archive = {
        path.relative_to(ROOT / "archive/input-drafts").as_posix()
        for path in (ROOT / "archive/input-drafts").rglob("*")
        if path.is_file()
    }
    declared_archive = set(archive_paths)
    if expected_archive != declared_archive:
        errors.append(
            "audit/ARCHIVE_CHECKSUMS.md: archive coverage mismatch; "
            f"missing={sorted(expected_archive - declared_archive)}, "
            f"unexpected={sorted(declared_archive - expected_archive)}"
        )
    return errors


def verify_local_links() -> list[str]:
    errors: list[str] = []
    for markdown in sorted(ROOT.rglob("*.md")):
        text = markdown.read_text(encoding="utf-8")
        for match in MARKDOWN_LINK.finditer(text):
            target = match.group("target").strip()
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1]
            target = target.split(maxsplit=1)[0]
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            target = unquote(target.split("#", 1)[0])
            if not target:
                continue
            resolved = (markdown.parent / target).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                errors.append(
                    f"{markdown.relative_to(ROOT)}: local link escapes repository: {target}"
                )
                continue
            if not resolved.exists():
                errors.append(f"{markdown.relative_to(ROOT)}: broken local link: {target}")
    return errors


def verify_status_controls() -> list[str]:
    errors: list[str] = []
    required = {
        "README.md": "REMANDED",
        "audit/CANONICAL_STATUS.md": "REMANDED",
        "audit/PROJECT_CONTROL.md": "REMANDED",
        "memorandum/DGG_WASHINGTON_SWORN_STATEMENT_MEMORANDUM.md": "REMANDED",
        "operations/DGG_PILOT_CONTROL_PACKET.md": "DEPRECATED FOR LIVE USE",
        "research/GAP_MATRIX.md": "REMANDED",
        "research/report-source.md": "REMANDED",
        "public/DGG_INFORMATION_PACKET.md": "PUBLICLY VISIBLE REVIEW DRAFT",
        "public/DGG_TWO_PAGE_BRIEF.md": "PUBLICLY VISIBLE REVIEW DRAFT",
        "outreach/MESSAGE_AND_CLAIMS_TOOLKIT.md": "PUBLICLY VISIBLE REVIEW TOOLKIT",
        "evidence/FACTS_AND_EVIDENCE_PACKET.md": "CANDIDATE LITIGATION-READINESS WORKPAPER",
        "research/AUTHORITY_REGISTER.md": "Candidate research infrastructure",
        "research/ZOTERO_HANDOFF.md": "READ-ONLY DEPENDENCY",
        "audit/DOCUMENT_REGISTER.md": "CANDIDATE CONTROL RECORD",
        "audit/PR_DEPENDENCY_DISPOSITION.md": "SINGLE INTEGRATION PATH",
    }
    for relative, marker in required.items():
        path = ROOT / relative
        if not path.is_file():
            errors.append(f"missing status-controlled file: {relative}")
            continue
        if marker not in path.read_text(encoding="utf-8"):
            errors.append(f"{relative}: missing status marker {marker!r}")
    return errors


def repository_files() -> set[str]:
    files: set[str] = set()
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.relative_to(ROOT).parts:
            continue
        files.add(path.relative_to(ROOT).as_posix())
    return files


def verify_artifact_manifest() -> list[str]:
    errors: list[str] = []
    manifest_path = ROOT / "audit/ARTIFACT_MANIFEST.json"
    try:
        payload = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        return [f"audit/ARTIFACT_MANIFEST.json: {exc}"]

    if payload.get("schema_version") != 1:
        errors.append("audit/ARTIFACT_MANIFEST.json: schema_version must be 1")
    if payload.get("repository_posture") != "remanded":
        errors.append("audit/ARTIFACT_MANIFEST.json: repository_posture must be 'remanded'")
    if payload.get("status_authority") != "audit/ARTIFACT_MANIFEST.json":
        errors.append("audit/ARTIFACT_MANIFEST.json: status_authority must identify itself")
    baseline = payload.get("source_baseline_commit")
    if not isinstance(baseline, str) or not COMMIT.fullmatch(baseline):
        errors.append("audit/ARTIFACT_MANIFEST.json: invalid source_baseline_commit")

    artifacts = payload.get("artifacts")
    if not isinstance(artifacts, list):
        return errors + ["audit/ARTIFACT_MANIFEST.json: artifacts must be a list"]

    paths: list[str] = []
    for index, artifact in enumerate(artifacts):
        label = f"audit/ARTIFACT_MANIFEST.json artifact[{index}]"
        if not isinstance(artifact, dict):
            errors.append(f"{label}: must be an object")
            continue

        path = artifact.get("path")
        if (
            not isinstance(path, str)
            or not path
            or "\\" in path
            or path.startswith("/")
            or ".." in Path(path).parts
        ):
            errors.append(f"{label}: invalid repository-relative POSIX path")
            continue
        paths.append(path)

        classification = artifact.get("classification")
        if classification not in ALLOWED_CLASSIFICATIONS:
            errors.append(f"{label}: invalid classification {classification!r}")

        governing_commit = artifact.get("governing_commit")
        if governing_commit is not None and (
            not isinstance(governing_commit, str)
            or not COMMIT.fullmatch(governing_commit)
        ):
            errors.append(f"{label}: governing_commit must be null or a 40-character SHA")

        live_use = artifact.get("live_use")
        if not isinstance(live_use, bool):
            errors.append(f"{label}: live_use must be boolean")
        elif live_use:
            errors.append(f"{label}: no current artifact may be used live while remanded")

        superseded_by = artifact.get("superseded_by")
        if superseded_by is not None and not isinstance(superseded_by, str):
            errors.append(f"{label}: superseded_by must be a path or null")

        gates = artifact.get("review_gates")
        if not isinstance(gates, list) or any(not isinstance(gate, str) for gate in gates):
            errors.append(f"{label}: review_gates must be a string array")
        else:
            if len(gates) != len(set(gates)):
                errors.append(f"{label}: review_gates contains duplicates")
            unknown = sorted(set(gates) - ALLOWED_REVIEW_GATES)
            if unknown:
                errors.append(f"{label}: unknown review gates {unknown}")

        if classification == "canonical":
            if governing_commit is None:
                errors.append(f"{label}: canonical artifact requires a governing_commit")
            if gates:
                errors.append(f"{label}: canonical artifact may not retain review gates")
        elif classification == "archive":
            if governing_commit is None:
                errors.append(f"{label}: archive artifact requires a governing_commit")
            if not path.startswith("archive/input-drafts/"):
                errors.append(f"{label}: archive artifact must be under archive/input-drafts/")
            if gates:
                errors.append(f"{label}: archive artifact may not retain review gates")
        elif classification in {"candidate", "supplement"}:
            if governing_commit is not None:
                errors.append(f"{label}: unreviewed artifact must not claim a governing_commit")
            if not gates:
                errors.append(f"{label}: unreviewed artifact requires at least one review gate")
        elif classification == "withdrawn" and superseded_by is None:
            errors.append(f"{label}: withdrawn artifact requires superseded_by")

    duplicates = sorted({path for path in paths if paths.count(path) > 1})
    if duplicates:
        errors.append(f"audit/ARTIFACT_MANIFEST.json: duplicate paths {duplicates}")

    declared = set(paths)
    actual = repository_files()
    missing = sorted(actual - declared)
    extra = sorted(declared - actual)
    if missing:
        errors.append(f"audit/ARTIFACT_MANIFEST.json: unclassified files {missing}")
    if extra:
        errors.append(f"audit/ARTIFACT_MANIFEST.json: nonexistent declared files {extra}")

    for artifact in artifacts:
        if not isinstance(artifact, dict):
            continue
        superseded_by = artifact.get("superseded_by")
        if isinstance(superseded_by, str) and superseded_by not in declared:
            errors.append(
                "audit/ARTIFACT_MANIFEST.json: "
                f"{artifact.get('path')!r} supersedes to undeclared {superseded_by!r}"
            )

    by_path = {
        artifact.get("path"): artifact
        for artifact in artifacts
        if isinstance(artifact, dict) and isinstance(artifact.get("path"), str)
    }
    for artifact in artifacts:
        if not isinstance(artifact, dict):
            continue
        superseded_by = artifact.get("superseded_by")
        if isinstance(superseded_by, str) and superseded_by in by_path:
            target_class = by_path[superseded_by].get("classification")
            if target_class in {"archive", "withdrawn"}:
                errors.append(
                    f"audit/ARTIFACT_MANIFEST.json: {artifact.get('path')!r} "
                    f"cannot supersede to {target_class} artifact {superseded_by!r}"
                )

    canonical_paths = {
        artifact.get("path")
        for artifact in artifacts
        if isinstance(artifact, dict) and artifact.get("classification") == "canonical"
    }
    if canonical_paths != {"audit/ARCHIVE_CHECKSUMS.md"}:
        errors.append(
            "audit/ARTIFACT_MANIFEST.json: while remanded, only the immutable archive "
            f"checksum record may be canonical; found {sorted(canonical_paths)}"
        )

    return errors


def verify_document_register() -> list[str]:
    errors: list[str] = []
    register_path = ROOT / "audit/DOCUMENT_REGISTER.md"
    manifest_path = ROOT / "audit/ARTIFACT_MANIFEST.json"
    try:
        register = register_path.read_text(encoding="utf-8")
        payload = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        return [f"document-register cross-check: {exc}"]

    by_path = {
        artifact.get("path"): artifact
        for artifact in payload.get("artifacts", [])
        if isinstance(artifact, dict) and isinstance(artifact.get("path"), str)
    }
    seen: set[str] = set()
    for line in register.splitlines():
        if not line.startswith("| DGG-"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 8:
            errors.append(f"audit/DOCUMENT_REGISTER.md: malformed row {cells[:1]}")
            continue
        match = re.fullmatch(r"\[[^\]]+\]\(([^)]+)\)", cells[1])
        if not match:
            errors.append(f"audit/DOCUMENT_REGISTER.md: invalid path cell for {cells[0]}")
            continue
        resolved = (register_path.parent / unquote(match.group(1))).resolve()
        try:
            relative = resolved.relative_to(ROOT).as_posix()
        except ValueError:
            errors.append(f"audit/DOCUMENT_REGISTER.md: path escapes repository for {cells[0]}")
            continue
        if relative in seen:
            errors.append(f"audit/DOCUMENT_REGISTER.md: duplicate path {relative}")
        seen.add(relative)

        artifact = by_path.get(relative)
        if artifact is None:
            errors.append(f"audit/DOCUMENT_REGISTER.md: unmanifested path {relative}")
            continue
        classes = [
            value
            for value in ALLOWED_CLASSIFICATIONS
            if re.search(rf"\b{re.escape(value)}\b", cells[2], flags=re.IGNORECASE)
        ]
        if classes != [artifact.get("classification")]:
            errors.append(
                f"audit/DOCUMENT_REGISTER.md: {relative} class {cells[2]!r} "
                f"does not match manifest {artifact.get('classification')!r}"
            )
        live_cell = cells[6].lower()
        if live_cell != "no" and not live_cell.startswith("repository review only"):
            errors.append(
                f"audit/DOCUMENT_REGISTER.md: {relative} has unrecognized live-use cell {cells[6]!r}"
            )
        if artifact.get("live_use") is not False:
            errors.append(f"audit/DOCUMENT_REGISTER.md: {relative} conflicts with manifest live_use")

    required = {
        "audit/ARTIFACT_MANIFEST.json",
        "audit/CANONICAL_STATUS.md",
        "audit/PR_DEPENDENCY_DISPOSITION.md",
        "public/DGG_TWO_PAGE_BRIEF.md",
        "public/DGG_INFORMATION_PACKET.md",
        "memorandum/DGG_WASHINGTON_SWORN_STATEMENT_MEMORANDUM.md",
        "evidence/FACTS_AND_EVIDENCE_PACKET.md",
        "outreach/MESSAGE_AND_CLAIMS_TOOLKIT.md",
        "output/pdf/01_DGG_Concept_Overview.pdf",
        "output/pdf/02_DGG_Legal_and_Evidence_Memorandum.pdf",
        "output/pdf/03_DGG_Implementation_and_Interview_Toolkit.pdf",
        "research/ZOTERO_HANDOFF.md",
    }
    if required - seen:
        errors.append(
            f"audit/DOCUMENT_REGISTER.md: missing durable records {sorted(required - seen)}"
        )
    return errors


def verify_pr_control() -> list[str]:
    errors: list[str] = []
    matrix_path = ROOT / "audit/PR_DEPENDENCY_DISPOSITION.md"
    try:
        text = matrix_path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        return [f"audit/PR_DEPENDENCY_DISPOSITION.md: {exc}"]

    parsed: dict[int, tuple[str, str, str, str]] = {}
    for line in text.splitlines():
        match = PR_ROW.match(line)
        if not match:
            continue
        number = int(match.group("number"))
        if number in parsed:
            errors.append(f"audit/PR_DEPENDENCY_DISPOSITION.md: duplicate PR #{number}")
        parsed[number] = (
            match.group("head"),
            match.group("base_ref"),
            match.group("base"),
            match.group("disposition"),
        )
    if parsed != EXPECTED_PR_RECORDS:
        errors.append(
            "audit/PR_DEPENDENCY_DISPOSITION.md: five-PR head/base/disposition set "
            f"does not match the frozen review set; parsed={parsed}"
        )
    canonical = [number for number, record in parsed.items() if record[3] == "CANONICAL REVIEW"]
    if canonical != [4]:
        errors.append(
            "audit/PR_DEPENDENCY_DISPOSITION.md: PR #4 must be the sole CANONICAL REVIEW"
        )
    required_phrases = {
        "REMANDED — CHANGES REQUIRED — NOT LAUNCH-CLEARED",
        "do not open a sixth PR",
        "feed PR #4 review",
        "No open PR currently receives the binding disposition **SUPERSEDES**",
    }
    for phrase in required_phrases:
        if phrase not in text:
            errors.append(f"audit/PR_DEPENDENCY_DISPOSITION.md: missing control phrase {phrase!r}")

    status = (ROOT / "audit/CANONICAL_STATUS.md").read_text(encoding="utf-8")
    status_requirements = {
        EXPECTED_PR_RECORDS[4][0],
        "PRs #1 and #5 are parked",
        "PRs #2 and #3 depend",
        "No open PR presently supersedes the remand",
        "no sixth PR is authorized",
    }
    for phrase in status_requirements:
        if phrase not in status:
            errors.append(f"audit/CANONICAL_STATUS.md: missing PR agreement phrase {phrase!r}")
    return errors


def verify_phase_zero_consistency() -> list[str]:
    errors: list[str] = []
    required = {
        "README.md": "Present Phase 0 is limited to a pure fictional mock with no real signer, oath, or notarial act.",
        "audit/CANONICAL_STATUS.md": "While the remand remains open, Phase 0 may use only a pure mock",
        "audit/PROJECT_CONTROL.md": "Phase 0 permits only a pure mock with fictional facts and no oath or notarial act.",
        "memorandum/DGG_WASHINGTON_SWORN_STATEMENT_MEMORANDUM.md": "pure mock with no real signer, oath, or notarial act",
        "operations/DGG_PILOT_CONTROL_PACKET.md": "It must not be executed while the remand remains open.",
        "public/DGG_INFORMATION_PACKET.md": "a pure mock using fictional material, with no real signer, oath, or notarial act.",
        "public/DGG_TWO_PAGE_BRIEF.md": "only fictional materials without a real signer, oath, or notarial act.",
    }
    for relative, phrase in required.items():
        path = ROOT / relative
        try:
            content = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"{relative}: {exc}")
            continue
        if phrase not in content:
            errors.append(f"{relative}: missing synthetic-only control phrase {phrase!r}")

    forbidden = {
        "research/report-source.md": [
            "presently sustained project design is nonpublic, in-person",
        ],
        "memorandum/DGG_WASHINGTON_SWORN_STATEMENT_MEMORANDUM.md": [
            "presently sustained Phase 0 design is nevertheless nonpublic, in-person",
            "presently sustained Phase 0 architecture uses an in-person tangible record",
            "Phase 0 is constrained to a pure fictional mock without an oath or to a private, in-person",
            "For Phase 0, DGG should use a concise tangible record presented and signed before the notary",
        ],
        "operations/DGG_PILOT_CONTROL_PACKET.md": [
            "present DGG Phase 0 risk-control design is nonpublic, in-person",
            "Enter the in-person notary workflow",
            "Complete the participant signature and notarial act contemporaneously",
        ],
        "audit/PROJECT_CONTROL.md": [
            "Selected Phase 0 design — in person only",
        ],
    }
    for relative, phrases in forbidden.items():
        content = (ROOT / relative).read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase in content:
                errors.append(f"{relative}: forbidden live-design phrase {phrase!r}")

    risky = re.compile(
        r"\b(in-person|wet-ink|real signer|signature|signing|swear|oath|notari\w*|"
        r"execut\w*|actual test)\b",
        flags=re.IGNORECASE,
    )
    authorization = re.compile(
        r"\b(authoriz\w*|permit\w*|allow\w*|execut\w*|conduct\w*|uses?|"
        r"includes?|requires?|requiring|may|should|will|must)\b",
        flags=re.IGNORECASE,
    )
    negated_risk_prefix = re.compile(
        r"\b(?:no|not|never|without)\b(?:\W+\w+){0,8}\W*$",
        flags=re.IGNORECASE,
    )
    modeled_risk_prefix = re.compile(
        r"\b(?:future|hypothetical|model(?:ed|s|ing)?|simulat(?:e|ed|es|ing))\b"
        r"(?:\W+\w+){0,12}\W*$",
        flags=re.IGNORECASE,
    )
    postponed_risk_suffix = re.compile(
        r"^\W*(?:\w+\W+){0,16}(?:only\W+after|after\W+reviewed|"
        r"after\W+all\W+gates|(?:is|are|remains?|be)\W+(?:not|never)\W+"
        r"(?:presently\W+)?(?:authorized|permitted|allowed|executed|conducted))\b",
        flags=re.IGNORECASE,
    )
    safety_terms = (
        "no ",
        "not ",
        "without ",
        "fictional",
        "pure mock",
        "future",
        "hypothetical",
        "model",
        "simulate",
        "possible",
        "quarantined",
        "after reviewed",
        "only after",
    )
    phase_zero_files = {
        "README.md",
        "audit/CANONICAL_STATUS.md",
        "audit/PROJECT_CONTROL.md",
        "evidence/FACTS_AND_EVIDENCE_PACKET.md",
        "memorandum/DGG_WASHINGTON_SWORN_STATEMENT_MEMORANDUM.md",
        "operations/DGG_PILOT_CONTROL_PACKET.md",
        "outreach/MESSAGE_AND_CLAIMS_TOOLKIT.md",
        "public/DGG_INFORMATION_PACKET.md",
        "public/DGG_TWO_PAGE_BRIEF.md",
        "research/AUTHORITY_REGISTER.md",
        "research/GAP_MATRIX.md",
        "research/report-source.md",
    }
    for relative in sorted(phase_zero_files):
        for line_number, line in enumerate(
            (ROOT / relative).read_text(encoding="utf-8").splitlines(), start=1
        ):
            lowered = line.lower()
            if "phase 0" not in lowered or not risky.search(line):
                continue
            for clause in re.split(r"[.;|]|\s+[—–]\s+", line):
                if (
                    "phase 0" not in clause.lower()
                    or not risky.search(clause)
                    or not authorization.search(clause)
                ):
                    continue
                for match in risky.finditer(clause):
                    prefix = clause[: match.start()]
                    suffix = clause[match.end() :]
                    if (
                        negated_risk_prefix.search(prefix)
                        or modeled_risk_prefix.search(prefix)
                        or postponed_risk_suffix.search(suffix)
                    ):
                        continue
                    errors.append(
                        f"{relative}:{line_number}: Phase 0 clause appears to authorize "
                        "a live or actual-test element without a directly governing "
                        "negative or future-gated qualifier"
                    )
                    break
            if not any(term in lowered for term in safety_terms):
                errors.append(
                    f"{relative}:{line_number}: Phase 0 line contains live-design terms "
                    "without a future, fictional, simulated, or negative qualifier"
                )
    return errors


def main() -> int:
    errors: list[str] = []
    errors.extend(verify_local_links())
    errors.extend(verify_status_controls())
    errors.extend(verify_artifact_manifest())
    errors.extend(verify_document_register())
    errors.extend(verify_pr_control())
    errors.extend(verify_phase_zero_consistency())
    errors.extend(verify_checksum_coverage())
    errors.extend(
        verify_manifest(ROOT / "audit/CANONICAL_CHECKSUMS.md", ROOT)
    )
    errors.extend(
        verify_manifest(ROOT / "audit/ARCHIVE_CHECKSUMS.md", ROOT / "archive/input-drafts")
    )

    if errors:
        print("Repository audit failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "Repository audit passed: links, status, artifact/register, PR, Phase 0, "
        "coverage, and checksums match."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
