"""Run contract-blind claim extraction for source-backed replay tasks.

This CLI executes only the RawAssertion extraction layer. It does not
adjudicate, map primitives, score, or stage anything.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict, replace
from datetime import date
import hashlib
import json
from pathlib import Path
import re
from typing import Any, Mapping, Sequence

from e2r.agentic import (
    AnchorType,
    ClaimExtractionInput,
    ClaimExtractionOutput,
    CodexCLIAgenticEvidenceProvider,
    EvidenceAnchor,
    EvidenceDocument,
    SourceType,
    build_claim_replay_result_manifest,
    build_default_codex_agentic_evidence_provider_bundle,
    build_adjudication_task_manifest,
    decode_claim_extraction_output,
)


DEFAULT_CLAIM_REPLAY_TASKS = (
    "output/0621_agentic_replay/"
    "c01_c36_provider_low_full_live_fetch_replacement_provider_seeded_post_verifier_claim_replay_tasks.json"
)
DEFAULT_OUTPUT_DIRECTORY = "output/0621_agentic_replay"


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run contract-blind RawAssertion extraction without scoring or staging.",
    )
    parser.add_argument("--claim-replay-tasks", default=DEFAULT_CLAIM_REPLAY_TASKS)
    parser.add_argument("--output-directory", default=DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--output-prefix", default="c01_c36_provider_low_full_live_fetch_replacement_provider_seeded")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--dry-run",
        action="store_true",
        help="Do not call an LLM provider; write provider_not_configured run rows.",
    )
    mode.add_argument(
        "--run-provider",
        action="store_true",
        help="Call the configured Codex provider for RawAssertion extraction.",
    )
    parser.add_argument("--working-directory", default=None)
    parser.add_argument("--timeout-seconds", type=float, default=None)
    parser.add_argument("--reasoning-effort", default=None)
    parser.add_argument("--task-id", action="append", default=None)
    parser.add_argument("--candidate-id", action="append", default=None)
    parser.add_argument("--max-tasks", type=int, default=None)
    return parser


def run_claim_extraction(
    *,
    claim_replay_task_manifest_path: str | Path,
    output_directory: str | Path,
    output_prefix: str = "c01_c36_provider_low_full_live_fetch_replacement_provider_seeded",
    run_provider: bool = False,
    working_directory: str | Path | None = None,
    timeout_seconds: float | None = None,
    reasoning_effort: str | None = None,
    task_ids: Sequence[str] | None = None,
    candidate_ids: Sequence[str] | None = None,
    max_tasks: int | None = None,
) -> Mapping[str, Path]:
    task_manifest = _filtered_task_manifest(
        _read_json_mapping(Path(claim_replay_task_manifest_path)),
        task_ids=task_ids,
        candidate_ids=candidate_ids,
        max_tasks=max_tasks,
    )
    provider = _build_provider(
        run_provider=run_provider,
        working_directory=working_directory,
        timeout_seconds=timeout_seconds,
        reasoning_effort=reasoning_effort,
    )
    run_manifest = _build_run_manifest(task_manifest=task_manifest, provider=provider)
    extraction_rows = tuple(row for row in run_manifest.get("extraction_rows") or () if isinstance(row, Mapping))
    claim_replay_results = build_claim_replay_result_manifest(
        claim_replay_task_manifest=task_manifest,
        extraction_rows=extraction_rows,
    )
    adjudication_tasks = build_adjudication_task_manifest(
        claim_replay_result_manifest=claim_replay_results,
    )

    output_dir = Path(output_directory)
    output_dir.mkdir(parents=True, exist_ok=True)
    paths = {
        "run_manifest_json": output_dir / f"{output_prefix}_claim_extraction_run_manifest.json",
        "run_manifest_md": output_dir / f"{output_prefix}_claim_extraction_run_manifest.md",
        "extraction_rows_json": output_dir / f"{output_prefix}_claim_extraction_rows.json",
        "extraction_rows_md": output_dir / f"{output_prefix}_claim_extraction_rows.md",
        "claim_replay_results_json": output_dir / f"{output_prefix}_claim_extraction_claim_replay_results.json",
        "claim_replay_results_md": output_dir / f"{output_prefix}_claim_extraction_claim_replay_results.md",
        "adjudication_tasks_json": output_dir / f"{output_prefix}_claim_extraction_adjudication_tasks.json",
        "adjudication_tasks_md": output_dir / f"{output_prefix}_claim_extraction_adjudication_tasks.md",
    }
    _write_json(paths["run_manifest_json"], run_manifest)
    _write_json(paths["extraction_rows_json"], {"rows": extraction_rows})
    _write_json(paths["claim_replay_results_json"], claim_replay_results)
    _write_json(paths["adjudication_tasks_json"], adjudication_tasks)
    paths["run_manifest_md"].write_text(_render_summary_markdown("Claim Extraction Run", run_manifest), encoding="utf-8")
    paths["extraction_rows_md"].write_text(_render_rows_markdown(extraction_rows), encoding="utf-8")
    paths["claim_replay_results_md"].write_text(
        _render_summary_markdown("Claim Replay Results From Extraction", claim_replay_results),
        encoding="utf-8",
    )
    paths["adjudication_tasks_md"].write_text(
        _render_summary_markdown("Adjudication Tasks From Extraction", adjudication_tasks),
        encoding="utf-8",
    )
    return paths


def _build_provider(
    *,
    run_provider: bool,
    working_directory: str | Path | None,
    timeout_seconds: float | None,
    reasoning_effort: str | None,
) -> object | None:
    if not run_provider:
        return None
    bundle = build_default_codex_agentic_evidence_provider_bundle(working_directory=working_directory)
    if bundle is None:
        return None
    provider = bundle.extractor
    if isinstance(provider, CodexCLIAgenticEvidenceProvider):
        updates: dict[str, object] = {}
        if timeout_seconds is not None:
            updates["timeout_seconds"] = timeout_seconds
        clean_effort = (reasoning_effort or "").strip()
        if clean_effort:
            updates["extra_args"] = (
                *provider.extra_args,
                "-c",
                f"model_reasoning_effort={json.dumps(clean_effort)}",
            )
        if updates:
            provider = replace(provider, **updates)
    if not hasattr(provider, "extract"):
        return None
    return provider


def _build_run_manifest(*, task_manifest: Mapping[str, Any], provider: object | None) -> Mapping[str, Any]:
    tasks = tuple(task for task in task_manifest.get("tasks") or () if isinstance(task, Mapping))
    runs: list[Mapping[str, Any]] = []
    extraction_rows: list[Mapping[str, Any]] = []
    for task in tasks:
        if provider is None:
            runs.append(_run_row_for_task(task, status="provider_not_configured"))
            continue
        extraction_input, error_row = _claim_extraction_input_for_task(task)
        if error_row is not None:
            runs.append(_run_row_for_task(task, status="input_error", provider_error=error_row["reason"]))
            extraction_rows.append(error_row)
            continue
        try:
            output = provider.extract(extraction_input)
        except Exception as exc:  # pragma: no cover - defensive CLI boundary
            reason = type(exc).__name__
            runs.append(_run_row_for_task(task, status="provider_error", provider_error=reason))
            extraction_rows.append(_extraction_error_row(task, reason=reason))
            continue
        extraction_row = _extraction_row_from_output(task, output)
        extraction_rows.append(extraction_row)
        status = "extraction_output"
        if extraction_row.get("ok") is False:
            status = "provider_error"
        runs.append(_run_row_for_task(task, status=status))

    status_counts: dict[str, int] = {}
    for row in runs:
        status = str(row.get("run_status") or "")
        status_counts[status] = status_counts.get(status, 0) + 1
    return {
        "schema_version": "e2r_claim_extraction_run_manifest_v1",
        "source_claim_replay_task_schema_version": task_manifest.get("schema_version"),
        "summary": {
            "task_count": len(tasks),
            "llm_called_count": sum(1 for row in runs if row.get("run_status") == "extraction_output"),
            "provider_not_configured_count": status_counts.get("provider_not_configured", 0),
            "provider_error_count": status_counts.get("provider_error", 0),
            "input_error_count": status_counts.get("input_error", 0),
            "extraction_output_count": status_counts.get("extraction_output", 0),
            "extraction_row_count": len(extraction_rows),
            "production_score_fixture_count": 0,
        },
        "run_status_counts": dict(sorted(status_counts.items())),
        "runs": tuple(runs),
        "extraction_rows": tuple(extraction_rows),
    }


def _claim_extraction_input_for_task(
    task: Mapping[str, Any],
) -> tuple[ClaimExtractionInput | None, Mapping[str, Any] | None]:
    text_path = Path(str(task.get("extracted_text_path") or ""))
    if not text_path.exists():
        return None, _extraction_error_row(task, reason="extracted_text_path_missing")
    text = text_path.read_text(encoding="utf-8", errors="ignore")
    if not text.strip():
        return None, _extraction_error_row(task, reason="extracted_text_empty")
    expected_hash = str(task.get("content_hash") or "").strip()
    actual_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
    if _looks_like_sha256(expected_hash) and expected_hash != actual_hash:
        return None, _extraction_error_row(task, reason="content_hash_mismatch")
    as_of = _parse_date(task.get("as_of_date"))
    if as_of is None:
        return None, _extraction_error_row(task, reason="invalid_as_of_date")
    published_at = _parse_date(task.get("document_published_at")) or as_of
    source_type = _source_type(task.get("source_type"))
    document = EvidenceDocument.from_text(
        text=text,
        canonical_url=str(task.get("canonical_url") or "") or None,
        source_type=source_type,
        source_name=str(task.get("source_name") or source_type.value),
        published_at=published_at,
        available_at=published_at,
        parser_version="claim_replay_extraction_input_v1",
        source_proxy_only=False,
        score_block_reasons=("claim_replay_pending",),
    )
    if str(task.get("document_id") or "") and document.document_id != str(task.get("document_id")):
        return None, _extraction_error_row(task, reason="document_id_mismatch")
    target_names = tuple(str(item).strip() for item in (task.get("target_names") or ()) if str(item).strip())
    anchor_text = _fixture_anchor_text(text, max_chars=1200, target_names=target_names)
    if not anchor_text:
        return None, _extraction_error_row(task, reason="anchor_text_empty")
    anchor = EvidenceAnchor(
        anchor_id=str(task.get("anchor_id") or ""),
        document_id=document.document_id,
        anchor_type=AnchorType.TEXT_SPAN,
        locator=_anchor_locator_for_text(text, anchor_text, fallback=str(task.get("anchor_locator") or "char:0:800")),
        exact_text=anchor_text,
        content_hash=hashlib.sha256(anchor_text.encode("utf-8")).hexdigest(),
        anchor_verified=anchor_text in text,
    )
    return (
        ClaimExtractionInput(
            target_entity_id=str(task.get("target_entity_id") or ""),
            target_names=target_names,
            as_of_date=as_of,
            document=document,
            document_text=text,
            anchors=(anchor,),
        ),
        None,
    )


def _extraction_row_from_output(task: Mapping[str, Any], output: Any) -> Mapping[str, Any]:
    if isinstance(output, Mapping):
        try:
            decoded = decode_claim_extraction_output(output)
        except Exception as exc:
            return _extraction_error_row(
                task,
                reason=f"provider_output_schema_violation:{type(exc).__name__}",
            )
        output = decoded
    if isinstance(output, ClaimExtractionOutput):
        return {
            "task_id": str(task.get("task_id") or ""),
            "ok": output.status != "provider_error",
            "output": _claim_extraction_output_payload(output),
        }
    return _extraction_error_row(task, reason="invalid_provider_output")


def _claim_extraction_output_payload(output: ClaimExtractionOutput) -> Mapping[str, Any]:
    return {
        "status": output.status,
        "blocked_reason": output.blocked_reason,
        "raw_assertions": tuple(_raw_assertion_payload(raw) for raw in output.raw_assertions),
    }


def _raw_assertion_payload(raw: Any) -> Mapping[str, Any]:
    payload = asdict(raw)
    polarity = payload.get("polarity_proposal")
    if hasattr(polarity, "value"):
        payload["polarity_proposal"] = polarity.value
    return payload


def _extraction_error_row(task: Mapping[str, Any], *, reason: str) -> Mapping[str, Any]:
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
        "fixture_seed_id": str(task.get("fixture_seed_id") or ""),
        "candidate_id": str(task.get("candidate_id") or ""),
        "archetype_id": str(task.get("archetype_id") or ""),
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
        raise ValueError("claim replay task manifest tasks must be a sequence")
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
    filtered["claim_extraction_input_filter"] = {
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


_ANCHOR_SIGNAL_MARKERS = (
    "customer",
    "contract",
    "order",
    "backlog",
    "capacity",
    "capa",
    "production",
    "shipment",
    "pricing",
    "price",
    "asp",
    "revenue",
    "sales",
    "profit",
    "margin",
    "guidance",
    "investment",
    "capex",
    "cash flow",
    "fcf",
    "demand",
    "supply",
    "shortage",
    "constraint",
    "bottleneck",
    "allocation",
    "preorder",
    "pre-sold",
    "sold out",
    "hbm",
    "ai server",
    "audit",
    "accounting",
    "legal",
    "lawsuit",
    "regulatory",
    "risk",
    "trial",
    "clinical trial",
    "phase 3",
    "futility",
    "discontinuation",
    "discontinue",
    "halt",
    "stopped",
    "enrollment",
    "primary objective",
    "data monitoring committee",
    "idmc",
    "dmc",
    "safety",
    "고객",
    "계약",
    "수주",
    "수주잔고",
    "생산능력",
    "출하",
    "공급",
    "수급",
    "배정",
    "선주문",
    "판매 완료",
    "가격",
    "판가",
    "매출",
    "영업이익",
    "마진",
    "가이던스",
    "현금흐름",
    "설비투자",
    "감사",
    "회계",
    "소송",
    "규제",
    "위험",
    "임상",
    "임상시험",
    "중단",
    "권고",
    "무용성",
    "환자 등록",
)

_ANCHOR_BOILERPLATE_MARKERS = (
    "accessibility statement",
    "skip navigation",
    "client login",
    "send a release",
    "searching for your content",
    "no results found",
    "resources",
    "contact",
    "privacy",
    "rss",
    "newsletter",
    "copyright",
)


def _fixture_anchor_text(text: str, *, max_chars: int, target_names: Sequence[str] = ()) -> str:
    clean = text.strip()
    if not clean:
        return ""
    lower = clean.casefold()
    candidates: list[str] = []
    for target_name in target_names:
        needle = str(target_name or "").strip().casefold()
        if not needle:
            continue
        for index in _all_occurrences(lower, needle):
            candidates.append(_window_around(clean, index, len(needle), max_chars=max_chars))
    for marker in _ANCHOR_SIGNAL_MARKERS:
        needle = marker.casefold()
        for index in _all_occurrences(lower, needle):
            candidates.append(_window_around(clean, index, len(needle), max_chars=max_chars))
            if len(candidates) >= 48:
                break
        if len(candidates) >= 48:
            break
    if candidates:
        return max(dict.fromkeys(candidates), key=lambda candidate: _anchor_signal_score(candidate, target_names)).strip()
    return clean[: max(1, max_chars)].strip()


def _window_around(text: str, index: int, needle_len: int, *, max_chars: int) -> str:
    start = max(0, index - max_chars // 3)
    end = min(len(text), index + needle_len + (max_chars * 2 // 3))
    return text[start:end].strip()


def _anchor_locator_for_text(text: str, anchor_text: str, *, fallback: str) -> str:
    index = text.find(anchor_text)
    if index < 0:
        return fallback
    return f"char:{index}:{index + len(anchor_text)}"


def _all_occurrences(text: str, needle: str) -> tuple[int, ...]:
    if not needle:
        return ()
    indexes: list[int] = []
    start = 0
    while True:
        index = text.find(needle, start)
        if index < 0:
            break
        indexes.append(index)
        start = index + max(1, len(needle))
        if len(indexes) >= 24:
            break
    return tuple(indexes)


def _anchor_signal_score(candidate: str, target_names: Sequence[str]) -> int:
    haystack = candidate.casefold()
    score = 0
    if any(str(name or "").strip().casefold() in haystack for name in target_names if str(name or "").strip()):
        score += 20
    score += 6 * sum(1 for marker in _ANCHOR_SIGNAL_MARKERS if marker in haystack)
    score += 2 * min(12, len(re.findall(r"\d", candidate)))
    score -= 5 * sum(1 for marker in _ANCHOR_BOILERPLATE_MARKERS if marker in haystack)
    return score


def _looks_like_sha256(value: str) -> bool:
    return len(value) == 64 and all(char in "0123456789abcdefABCDEF" for char in value)


def _parse_date(value: Any) -> date | None:
    try:
        return date.fromisoformat(str(value or "").strip()[:10])
    except ValueError:
        return None


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
    lines.append(
        "Claim extraction output is not score evidence until adjudication, primitive mapping, "
        "eligibility checks, and ScoreContribution construction pass."
    )
    lines.append("")
    return "\n".join(lines)


def _render_rows_markdown(rows: Sequence[Mapping[str, Any]]) -> str:
    lines = ["# Claim Extraction Rows", ""]
    lines.append(f"- row_count: `{len(rows)}`")
    lines.append("")
    lines.append("Rows contain RawAssertion extraction output only. They do not create production score fixtures.")
    lines.append("")
    return "\n".join(lines)


def main(argv: Sequence[str] | None = None) -> int:
    args = build_arg_parser().parse_args(argv)
    paths = run_claim_extraction(
        claim_replay_task_manifest_path=args.claim_replay_tasks,
        output_directory=args.output_directory,
        output_prefix=args.output_prefix,
        run_provider=bool(args.run_provider),
        working_directory=args.working_directory,
        timeout_seconds=args.timeout_seconds,
        reasoning_effort=args.reasoning_effort,
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
    "DEFAULT_CLAIM_REPLAY_TASKS",
    "DEFAULT_OUTPUT_DIRECTORY",
    "build_arg_parser",
    "main",
    "run_claim_extraction",
]
