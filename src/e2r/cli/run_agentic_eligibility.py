"""Run deterministic score-eligibility checks for mapped evidence claims."""

from __future__ import annotations

import argparse
from dataclasses import asdict
from datetime import date
import hashlib
import json
from pathlib import Path
import re
from typing import Any, Mapping, Sequence

from e2r.agentic import (
    AdjudicatedClaim,
    AnchorType,
    Directness,
    EvidenceAnchor,
    EvidenceDocument,
    InvestigationStatus,
    MappingStatus,
    Polarity,
    PrimitiveMappingProposal,
    RelationToTarget,
    SemanticStatus,
    SourceType,
    SupportDirection,
    TargetScopeStatus,
    TemporalStatus,
    VerificationStatus,
    build_eligibility_result_manifest,
    build_score_contribution_task_manifest,
    decode_claim_extraction_output,
    derive_score_eligibility,
)
from e2r.agentic.evidence_contract_v2 import load_evidence_contracts_v2


DEFAULT_ELIGIBILITY_TASKS = (
    "output/0621_agentic_replay/"
    "c01_c36_provider_low_full_live_fetch_replacement_provider_seeded_v2_extracted_provider_gated_pmap_provider_v2_"
    "eligibility_tasks_from_mapping.json"
)
DEFAULT_OUTPUT_DIRECTORY = "output/0621_agentic_replay"


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run deterministic eligibility checks without scoring or staging.",
    )
    parser.add_argument("--eligibility-tasks", default=DEFAULT_ELIGIBILITY_TASKS)
    parser.add_argument("--output-directory", default=DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--output-prefix", default="c01_c36_provider_low_full_live_fetch_replacement_provider_seeded")
    parser.add_argument("--evidence-contracts-v2", default=None)
    parser.add_argument("--task-id", action="append", default=None)
    parser.add_argument("--candidate-id", action="append", default=None)
    parser.add_argument("--max-tasks", type=int, default=None)
    return parser


def run_eligibility(
    *,
    eligibility_task_manifest_path: str | Path,
    output_directory: str | Path,
    output_prefix: str = "c01_c36_provider_low_full_live_fetch_replacement_provider_seeded",
    evidence_contracts_v2_path: str | Path | None = None,
    task_ids: Sequence[str] | None = None,
    candidate_ids: Sequence[str] | None = None,
    max_tasks: int | None = None,
) -> Mapping[str, Path]:
    task_manifest = _filtered_task_manifest(
        _read_json_mapping(Path(eligibility_task_manifest_path)),
        task_ids=task_ids,
        candidate_ids=candidate_ids,
        max_tasks=max_tasks,
    )
    contracts = (
        load_evidence_contracts_v2(path=evidence_contracts_v2_path)
        if evidence_contracts_v2_path is not None
        else {}
    )
    run_manifest = _build_run_manifest(task_manifest=task_manifest, contracts_by_archetype=contracts)
    eligibility_rows = tuple(row for row in run_manifest.get("eligibility_rows") or () if isinstance(row, Mapping))
    eligibility_results = build_eligibility_result_manifest(
        eligibility_task_manifest=task_manifest,
        eligibility_rows=eligibility_rows,
    )
    score_contribution_tasks = build_score_contribution_task_manifest(
        eligibility_result_manifest=eligibility_results,
    )

    output_dir = Path(output_directory)
    output_dir.mkdir(parents=True, exist_ok=True)
    paths = {
        "run_manifest_json": output_dir / f"{output_prefix}_eligibility_run_manifest.json",
        "run_manifest_md": output_dir / f"{output_prefix}_eligibility_run_manifest.md",
        "eligibility_rows_json": output_dir / f"{output_prefix}_eligibility_rows.json",
        "eligibility_rows_md": output_dir / f"{output_prefix}_eligibility_rows.md",
        "eligibility_results_json": output_dir / f"{output_prefix}_eligibility_results_from_run.json",
        "eligibility_results_md": output_dir / f"{output_prefix}_eligibility_results_from_run.md",
        "score_contribution_tasks_json": output_dir / f"{output_prefix}_score_contribution_tasks_from_eligibility.json",
        "score_contribution_tasks_md": output_dir / f"{output_prefix}_score_contribution_tasks_from_eligibility.md",
    }
    _write_json(paths["run_manifest_json"], run_manifest)
    _write_json(paths["eligibility_rows_json"], {"rows": eligibility_rows})
    _write_json(paths["eligibility_results_json"], eligibility_results)
    _write_json(paths["score_contribution_tasks_json"], score_contribution_tasks)
    paths["run_manifest_md"].write_text(_render_summary_markdown("Eligibility Run", run_manifest), encoding="utf-8")
    paths["eligibility_rows_md"].write_text(_render_rows_markdown(eligibility_rows), encoding="utf-8")
    paths["eligibility_results_md"].write_text(
        _render_summary_markdown("Eligibility Results From Run", eligibility_results),
        encoding="utf-8",
    )
    paths["score_contribution_tasks_md"].write_text(
        _render_summary_markdown("Score Contribution Tasks From Eligibility", score_contribution_tasks),
        encoding="utf-8",
    )
    return paths


def _build_run_manifest(*, task_manifest: Mapping[str, Any], contracts_by_archetype: Mapping[str, Any] | None = None) -> Mapping[str, Any]:
    tasks = tuple(task for task in task_manifest.get("tasks") or () if isinstance(task, Mapping))
    runs: list[Mapping[str, Any]] = []
    rows: list[Mapping[str, Any]] = []
    for task in tasks:
        row = _eligibility_row_for_task(task, contracts_by_archetype=contracts_by_archetype or {})
        rows.append(row)
        status = "deterministic_eligibility_output" if row.get("ok") is not False else "input_error"
        runs.append(_run_row_for_task(task, status=status, provider_error=row.get("reason") if row.get("ok") is False else None))

    status_counts: dict[str, int] = {}
    for row in runs:
        status = str(row.get("run_status") or "")
        status_counts[status] = status_counts.get(status, 0) + 1
    return {
        "schema_version": "e2r_eligibility_run_manifest_v1",
        "source_eligibility_task_schema_version": task_manifest.get("schema_version"),
        "summary": {
            "task_count": len(tasks),
            "deterministic_eligibility_count": status_counts.get("deterministic_eligibility_output", 0),
            "input_error_count": status_counts.get("input_error", 0),
            "eligibility_row_count": len(rows),
            "production_score_fixture_count": 0,
        },
        "run_status_counts": dict(sorted(status_counts.items())),
        "runs": tuple(runs),
        "eligibility_rows": tuple(rows),
    }


def _eligibility_row_for_task(
    task: Mapping[str, Any],
    *,
    contracts_by_archetype: Mapping[str, Any] | None = None,
) -> Mapping[str, Any]:
    built, error = _eligibility_objects_for_task(task)
    if error is not None:
        return _eligibility_error_row(task, reason=error)
    document, anchor, claim, mapping, as_of, flags = built
    contract = (contracts_by_archetype or {}).get(str(task.get("archetype_id") or "").strip())
    eligibility = derive_score_eligibility(
        document=document,
        anchor=anchor,
        claim=claim,
        mapping=mapping,
        as_of_date=as_of,
        allowed_target_scopes=getattr(contract, "allowed_target_scopes", (TargetScopeStatus.DIRECT,)),
        allowed_directness=getattr(contract, "allowed_directness", (Directness.DIRECT,)),
        require_source_quorum=False,
        contradiction_resolved=not flags["unresolved_contradiction"],
    )
    reasons = list(eligibility.reasons)
    if flags["snippet_only"] and "snippet_only_source" not in reasons:
        reasons.append("snippet_only_source")
    eligible = eligibility.eligible and not flags["snippet_only"]
    return {
        "task_id": str(task.get("task_id") or ""),
        "ok": True,
        "eligibility_source": "deterministic",
        "eligible": eligible,
        "source_anchor_verified": anchor.anchor_verified,
        "future_leakage": any(reason.startswith("future_") for reason in reasons),
        "source_proxy_only": document.source_proxy_only,
        "snippet_only": flags["snippet_only"],
        "unresolved_contradiction": flags["unresolved_contradiction"],
        "reasons": tuple(reasons) if reasons else ("score_eligibility_passed",),
    }


def _eligibility_objects_for_task(
    task: Mapping[str, Any],
) -> tuple[
    tuple[EvidenceDocument, EvidenceAnchor, AdjudicatedClaim, PrimitiveMappingProposal, date, Mapping[str, bool]] | None,
    str | None,
]:
    raw_payload = task.get("raw_assertion")
    if not isinstance(raw_payload, Mapping):
        return None, "raw_assertion_missing"
    try:
        raw_assertion = decode_claim_extraction_output(
            {"status": "ok", "blocked_reason": None, "raw_assertions": [raw_payload]}
        ).raw_assertions[0]
    except Exception:
        return None, "raw_assertion_decode_failed"
    as_of = _parse_date(task.get("as_of_date"))
    if as_of is None:
        return None, "invalid_as_of_date"
    document_id = str(task.get("document_id") or "").strip()
    if not document_id:
        return None, "document_id_missing"
    text_path = Path(str(task.get("extracted_text_path") or ""))
    text = ""
    snippet_only = True
    if text_path.exists():
        text = text_path.read_text(encoding="utf-8", errors="ignore")
        snippet_only = False
    if not text.strip():
        text = raw_assertion.exact_quote or raw_assertion.object_text
        snippet_only = True
    expected_hash = str(task.get("content_hash") or "").strip()
    actual_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
    hash_matches = not _looks_like_sha256(expected_hash) or expected_hash == actual_hash
    if not hash_matches:
        snippet_only = True
    source_type = _source_type(task.get("source_type"))
    published_at = _parse_date(task.get("document_published_at"))
    document = EvidenceDocument(
        document_id=document_id,
        canonical_url=str(task.get("canonical_url") or "") or None,
        source_type=source_type,
        source_name=str(task.get("source_name") or source_type.value),
        content_hash=expected_hash if _looks_like_sha256(expected_hash) else actual_hash,
        published_at=published_at,
        available_at=published_at,
        parser_version="eligibility_input_v1",
        source_proxy_only=False,
    )
    exact_text = raw_assertion.exact_quote or raw_assertion.object_text
    anchor_verified = bool(exact_text) and _text_contains_anchor(text, exact_text) and hash_matches and not snippet_only
    anchor = EvidenceAnchor(
        anchor_id=str(task.get("anchor_id") or raw_assertion.anchor_id),
        document_id=document.document_id,
        anchor_type=AnchorType.TEXT_SPAN,
        locator=str(task.get("anchor_locator") or raw_assertion.anchor_id),
        exact_text=exact_text,
        content_hash=hashlib.sha256(exact_text.encode("utf-8")).hexdigest() if exact_text else None,
        anchor_verified=anchor_verified,
    )
    claim = AdjudicatedClaim.from_raw(
        raw=raw_assertion,
        document=document,
        anchor=anchor,
        subject_entity_id=str(task.get("subject_entity_id") or "").strip(),
        target_entity_id=str(task.get("target_entity_id") or "").strip(),
        relation_to_target=_enum_value(RelationToTarget, task.get("relation_to_target"), RelationToTarget.UNKNOWN),
        directness=_enum_value(Directness, task.get("directness"), Directness.UNKNOWN),
        verification_status=VerificationStatus.SEMANTIC_VERIFIED,
        target_scope_status=_enum_value(TargetScopeStatus, task.get("target_scope_status"), TargetScopeStatus.UNKNOWN),
        polarity=_enum_value(Polarity, task.get("polarity"), Polarity.CONDITIONAL),
        temporal_status=_enum_value(TemporalStatus, task.get("temporal_status"), TemporalStatus.UNKNOWN),
        semantic_status=_enum_value(SemanticStatus, task.get("semantic_status"), SemanticStatus.UNVERIFIED),
        investigation_status=_enum_value(
            InvestigationStatus,
            task.get("investigation_status"),
            InvestigationStatus.FOLLOWUP_REQUIRED,
        ),
        event_date=_parse_date(task.get("event_date")),
        effective_start=_parse_date(task.get("effective_start")),
        effective_end=_parse_date(task.get("effective_end")),
    )
    expected_claim_id = str(task.get("claim_id") or "").strip()
    if expected_claim_id and expected_claim_id != claim.claim_id:
        return None, "claim_id_reconstruction_mismatch"
    mapping = PrimitiveMappingProposal.build(
        claim_id=claim.claim_id,
        archetype_id=str(task.get("archetype_id") or "").strip(),
        primitive_id=str(task.get("primitive_id") or "").strip(),
        support_direction=_enum_value(SupportDirection, task.get("support_direction"), SupportDirection.NEUTRAL),
        mapping_status=_enum_value(MappingStatus, task.get("mapping_status"), MappingStatus.PROPOSED),
        rationale=str(task.get("mapping_rationale") or ""),
        contract_rule_id=str(task.get("contract_rule_id") or "") or None,
    )
    return (
        (
            document,
            anchor,
            claim,
            mapping,
            as_of,
            {
                "snippet_only": snippet_only,
                "unresolved_contradiction": claim.semantic_status == SemanticStatus.CONTRADICTED,
            },
        ),
        None,
    )


def _eligibility_error_row(task: Mapping[str, Any], *, reason: str) -> Mapping[str, Any]:
    return {
        "task_id": str(task.get("task_id") or ""),
        "ok": False,
        "reason": reason,
    }


def _run_row_for_task(
    task: Mapping[str, Any],
    *,
    status: str,
    provider_error: str | None = None,
) -> Mapping[str, Any]:
    row = {
        "task_id": str(task.get("task_id") or ""),
        "primitive_mapping_result_id": str(task.get("primitive_mapping_result_id") or ""),
        "claim_id": str(task.get("claim_id") or ""),
        "archetype_id": str(task.get("archetype_id") or ""),
        "primitive_id": str(task.get("primitive_id") or ""),
        "target_entity_id": str(task.get("target_entity_id") or ""),
        "run_status": status,
        "production_score_fixture": False,
    }
    if provider_error:
        row["provider_error"] = provider_error
    return row


def _filtered_task_manifest(
    manifest: Mapping[str, Any],
    *,
    task_ids: Sequence[str] | None,
    candidate_ids: Sequence[str] | None,
    max_tasks: int | None,
) -> Mapping[str, Any]:
    if max_tasks is not None and max_tasks < 1:
        raise ValueError("max_tasks must be positive when provided")
    requested_task_ids = {str(item).strip() for item in (task_ids or ()) if str(item).strip()}
    requested_candidate_ids = {str(item).strip() for item in (candidate_ids or ()) if str(item).strip()}
    raw_tasks = manifest.get("tasks") or ()
    if not isinstance(raw_tasks, Sequence) or isinstance(raw_tasks, (str, bytes, bytearray)):
        raise ValueError("eligibility task manifest tasks must be a sequence")
    tasks: list[Mapping[str, Any]] = []
    for task in raw_tasks:
        if not isinstance(task, Mapping):
            continue
        task_id = str(task.get("task_id") or "").strip()
        candidate_id = str(task.get("candidate_id") or "").strip()
        if requested_task_ids and task_id not in requested_task_ids:
            continue
        if requested_candidate_ids and candidate_id not in requested_candidate_ids:
            continue
        tasks.append(task)
        if max_tasks is not None and len(tasks) >= max_tasks:
            break
    filtered = dict(manifest)
    filtered["tasks"] = tasks
    filtered["eligibility_input_filter"] = {
        "task_ids": sorted(requested_task_ids),
        "candidate_ids": sorted(requested_candidate_ids),
        "max_tasks": max_tasks,
        "input_task_count": len(raw_tasks),
        "selected_task_count": len(tasks),
    }
    return filtered


def _source_type(value: Any) -> SourceType:
    text = str(value or "").strip()
    try:
        return SourceType(text)
    except ValueError:
        return SourceType.NEWS


def _enum_value(enum_cls: Any, value: Any, default: Any) -> Any:
    try:
        return enum_cls(str(value or "").strip())
    except ValueError:
        return default


def _parse_date(value: Any) -> date | None:
    try:
        return date.fromisoformat(str(value or "").strip()[:10])
    except ValueError:
        return None


def _text_contains_anchor(text: str, exact_text: str) -> bool:
    if not text or not exact_text:
        return False
    if exact_text in text:
        return True
    normalized_text = re.sub(r"\s+", " ", text).strip().casefold()
    normalized_anchor = re.sub(r"\s+", " ", exact_text).strip().casefold()
    return bool(normalized_anchor) and normalized_anchor in normalized_text


def _looks_like_sha256(value: str | None) -> bool:
    return bool(value and len(value.strip()) == 64 and all(ch in "0123456789abcdefABCDEF" for ch in value.strip()))


def _read_json_mapping(path: Path) -> Mapping[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, Mapping):
        raise ValueError(f"{path} must contain a JSON object")
    return data


def _write_json(path: Path, data: Mapping[str, Any]) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")


def _render_summary_markdown(title: str, manifest: Mapping[str, Any]) -> str:
    lines = [f"# {title}", ""]
    schema_version = manifest.get("schema_version")
    if schema_version:
        lines.extend((f"- schema_version: `{schema_version}`", ""))
    summary = manifest.get("summary")
    if isinstance(summary, Mapping):
        lines.append("## Summary")
        for key in sorted(summary):
            lines.append(f"- {key}: `{summary[key]}`")
        lines.append("")
    lines.append("Eligibility output is not a score. It only gates whether a mapped claim can proceed.")
    lines.append("")
    return "\n".join(lines)


def _render_rows_markdown(rows: Sequence[Mapping[str, Any]]) -> str:
    lines = ["# Eligibility Rows", ""]
    lines.append(f"- row_count: `{len(rows)}`")
    lines.append("")
    lines.append("Rows contain deterministic eligibility output only. They do not create production score fixtures.")
    lines.append("")
    return "\n".join(lines)


def main(argv: Sequence[str] | None = None) -> int:
    args = build_arg_parser().parse_args(argv)
    paths = run_eligibility(
        eligibility_task_manifest_path=args.eligibility_tasks,
        output_directory=args.output_directory,
        output_prefix=args.output_prefix,
        evidence_contracts_v2_path=args.evidence_contracts_v2,
        task_ids=args.task_id,
        candidate_ids=args.candidate_id,
        max_tasks=args.max_tasks,
    )
    for name, path in paths.items():
        print(f"{name}={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = [
    "DEFAULT_ELIGIBILITY_TASKS",
    "DEFAULT_OUTPUT_DIRECTORY",
    "build_arg_parser",
    "main",
    "run_eligibility",
]
