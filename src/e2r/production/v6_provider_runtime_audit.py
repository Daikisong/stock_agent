"""Compile the exact provider-lineage audit for the v6 cutover receipts.

This compiler reads only the sealed Phase-101 and Phase-106 receipt trees.  It
never infers a successful call from a summary count: every call and every
score-bearing fact must exist as a receipt row and must use an authorized
Codex route.
"""

from __future__ import annotations

from collections import Counter
from datetime import date
import json
import os
from pathlib import Path
import stat
from typing import Any, Mapping, Sequence

from e2r.production.v6_canary_results import (
    CANARY_COMPILATION_PASS,
    compile_cross_archetype_canary_directory,
)
from e2r.production.v6_canary_selection import (
    FORCED_SELECTION,
    ISSUER_PROFILE_MANIFEST_NAME,
    load_current_issuer_business_profile_manifest,
    load_sealed_cross_archetype_canary_selection,
)
from e2r.research_brain.researcher_mode.artifact_lifecycle import (
    FINAL_ROOT_RELATIVE,
    PROVIDER_RUNTIME_AUDIT_PASS,
    PROVIDER_RUNTIME_AUDIT_SCHEMA,
)
from e2r.research_brain.researcher_mode.tracked_receipts import (
    PHASE101_TARGET_IDS,
    VERIFICATION_PASS,
    _provider_kind,
    verify_receipts,
)


PROVIDER_RUNTIME_AUDIT_FAIL = "E2R_V6_PROVIDER_RUNTIME_AUDIT_FAIL"
_AUTHORIZED_KINDS = frozenset({"CODEX", "COLLABORATION_CODEX"})
_LOCAL_KIND_MARKERS = ("QWEN", "OLLAMA", "LLAMA_CPP", "LM_STUDIO")


def _valid_date(value: object) -> bool:
    try:
        date.fromisoformat(str(value or ""))
    except ValueError:
        return False
    return True


def _provider_error_count(row: Mapping[str, Any]) -> int:
    raw = row.get("provider_error_count")
    if isinstance(raw, int) and not isinstance(raw, bool) and raw >= 0:
        return raw
    return int(
        str(row.get("status") or "").strip().upper()
        in {"ERROR", "FAILED", "PROVIDER_ERROR"}
    )


def _is_local_kind(kind: str) -> bool:
    normalized = kind.strip().upper()
    return any(marker in normalized for marker in _LOCAL_KIND_MARKERS)


def compile_provider_runtime_audit(
    *,
    as_of_date: str,
    provider_calls: Sequence[Mapping[str, Any]],
    scoring_facts: Sequence[Mapping[str, Any]],
) -> Mapping[str, Any]:
    """Compile a deterministic audit from already validated receipt rows."""

    call_ids = tuple(str(row.get("provider_call_id") or "") for row in provider_calls)
    call_kinds = tuple(_provider_kind(row.get("provider_name")) for row in provider_calls)
    fact_kinds = tuple(
        _provider_kind(row.get("extraction_provider_name"))
        for row in scoring_facts
    )
    provider_call_counts = dict(sorted(Counter(call_kinds).items()))
    fact_lineage_counts = dict(sorted(Counter(fact_kinds).items()))
    provider_error_count = sum(_provider_error_count(row) for row in provider_calls)
    unauthorized_count = sum(kind not in _AUTHORIZED_KINDS for kind in call_kinds)
    local_count = sum(_is_local_kind(kind) for kind in call_kinds)
    unauthorized_fact_lineage_count = sum(
        kind not in _AUTHORIZED_KINDS for kind in fact_kinds
    )
    local_fact_lineage_count = sum(_is_local_kind(kind) for kind in fact_kinds)
    qwen_count = sum(kind == "QWEN" for kind in call_kinds)
    ollama_count = sum(kind == "OLLAMA" for kind in call_kinds)
    inherited_qwen_count = sum(kind == "QWEN" for kind in fact_kinds)
    inherited_ollama_count = sum(kind == "OLLAMA" for kind in fact_kinds)
    authority_count = sum(
        row.get("score_or_stage_authority") is not False
        for row in provider_calls
    )
    invalid_call_id_count = sum(not value for value in call_ids)
    duplicate_call_id_count = len(call_ids) - len(set(call_ids))
    invalid_date_count = int(not _valid_date(as_of_date))
    empty_call_roster_count = int(not provider_calls)
    empty_scored_fact_roster_count = int(not scoring_facts)
    critical_count_sum = sum(
        (
            provider_error_count,
            unauthorized_count,
            local_count,
            unauthorized_fact_lineage_count,
            local_fact_lineage_count,
            qwen_count,
            ollama_count,
            inherited_qwen_count,
            inherited_ollama_count,
            authority_count,
            invalid_call_id_count,
            duplicate_call_id_count,
            invalid_date_count,
            empty_call_roster_count,
            empty_scored_fact_roster_count,
        )
    )
    passed = critical_count_sum == 0
    return {
        "schema_version": PROVIDER_RUNTIME_AUDIT_SCHEMA,
        "status": (
            PROVIDER_RUNTIME_AUDIT_PASS
            if passed
            else PROVIDER_RUNTIME_AUDIT_FAIL
        ),
        "as_of_date": as_of_date,
        "provider_call_counts": provider_call_counts,
        "scored_fact_provider_lineage_counts": fact_lineage_counts,
        "provider_error_count": provider_error_count,
        "unauthorized_provider_call_count": unauthorized_count,
        "local_provider_call_count": local_count,
        "qwen_call_count": qwen_count,
        "ollama_call_count": ollama_count,
        "inherited_qwen_scored_fact_count": inherited_qwen_count,
        "inherited_ollama_scored_fact_count": inherited_ollama_count,
        "critical_count_sum": critical_count_sum,
        "production_readiness_authority": False,
    }


def _assert_no_symlink_ancestor(path: Path) -> None:
    absolute = path.absolute()
    current = Path(absolute.anchor)
    for part in absolute.parts[1:]:
        current = current / part
        if current.is_symlink():
            raise ValueError("provider audit input path cannot contain symlinks")


def _read_jsonl_regular(path: Path) -> tuple[Mapping[str, Any], ...]:
    _assert_no_symlink_ancestor(path)
    descriptor = os.open(path, os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0))
    try:
        metadata = os.fstat(descriptor)
        if not stat.S_ISREG(metadata.st_mode) or metadata.st_nlink != 1:
            raise ValueError("provider audit input must be one private regular file")
        chunks: list[bytes] = []
        while True:
            chunk = os.read(descriptor, 1024 * 1024)
            if not chunk:
                break
            chunks.append(chunk)
    finally:
        os.close(descriptor)
    try:
        text = b"".join(chunks).decode("utf-8")
        rows = tuple(json.loads(line) for line in text.splitlines() if line.strip())
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError("provider audit JSONL input is invalid") from exc
    if any(not isinstance(row, Mapping) for row in rows):
        raise ValueError("provider audit JSONL rows must be objects")
    return tuple(dict(row) for row in rows)


def compile_provider_runtime_audit_from_cutover(
    *,
    repo_root: str | Path = ".",
    final_root: str | Path = FINAL_ROOT_RELATIVE,
) -> Mapping[str, Any]:
    """Recompute provider honesty from the exact sealed cutover leaves."""

    repo = Path(repo_root).resolve()
    requested = Path(final_root)
    final = (requested if requested.is_absolute() else repo / requested).resolve()
    canonical = (repo / FINAL_ROOT_RELATIVE).resolve()
    if final != canonical:
        raise ValueError("provider audit requires the canonical cutover root")

    receipt_root = final / "canary_receipts" / "2026-07-12"
    phase101 = verify_receipts(receipt_root)
    if phase101.get("status") != VERIFICATION_PASS:
        raise ValueError("Phase101 tracked receipts are not independently valid")

    selection_path = final / "cross_archetype_canary_selection.json"
    selection_header = json.loads(selection_path.read_text(encoding="utf-8"))
    forced = any(
        isinstance(row, Mapping)
        and row.get("selection_mode") == FORCED_SELECTION
        for row in selection_header.get("selections") or ()
    )
    profile: Mapping[str, Any] | None = None
    if forced:
        profile = load_current_issuer_business_profile_manifest(
            final / ISSUER_PROFILE_MANIFEST_NAME,
            selection_as_of_date=str(
                selection_header.get("selection_as_of_date") or ""
            ),
        )
    selection = load_sealed_cross_archetype_canary_selection(
        selection_path,
        issuer_business_profile_manifest=profile,
    )
    phase106 = compile_cross_archetype_canary_directory(
        selection=selection,
        live_root=final / "current_live_canaries",
        issuer_business_profile_manifest=profile,
        repo_root=repo,
    )
    if phase106.get("status") != CANARY_COMPILATION_PASS:
        raise ValueError("Phase106 exact-five receipt bundle is not valid")

    roots = [receipt_root / target_id for target_id in PHASE101_TARGET_IDS]
    roots.extend(
        final
        / "current_live_canaries"
        / f"{row['archetype_id']}_{row['target_id']}"
        for row in selection.get("selections") or ()
        if isinstance(row, Mapping)
    )
    calls: list[Mapping[str, Any]] = []
    facts: list[Mapping[str, Any]] = []
    for root in roots:
        calls.extend(_read_jsonl_regular(root / "provider_calls.jsonl"))
        facts.extend(_read_jsonl_regular(root / "scoring_facts.jsonl"))
    return compile_provider_runtime_audit(
        as_of_date=str(selection.get("selection_as_of_date") or ""),
        provider_calls=calls,
        scoring_facts=facts,
    )


__all__ = [
    "PROVIDER_RUNTIME_AUDIT_FAIL",
    "compile_provider_runtime_audit",
    "compile_provider_runtime_audit_from_cutover",
]
