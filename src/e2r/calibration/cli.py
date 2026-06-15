"""CLI for full Stock-Web calibration ingest, validation, dedupe and promotion."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any
import json

from .aggregate import aggregate_v12_rows, aggregate_validated_rows
from .archetype_weight_profile import write_archetype_weight_runtime_profile
from .dedupe import dedupe_trigger_rows, dedupe_v12_trigger_rows
from .md_discovery import discover_markdown_documents, prompt_spec_documents, v11_result_documents, v12_result_documents
from .md_parser import ParsedMarkdown, parse_markdown_document
from .promotion import PromotionResult, promote_calibrated_profile
from .transition import build_stage_transition_summary, write_stage_transition_outputs
from .v12_apply import write_v12_rolling_profile
from .v12_shadow import write_v12_shadow_outputs
from .validation import validate_trigger_rows, validate_v12_trigger_rows


DATA_DIR = Path("data/e2r/calibration")
REPORT_DIR = Path("reports/e2r_calibration")
V12_DATA_DIR = DATA_DIR / "v12"
V12_REPORT_DIR = REPORT_DIR / "v12"


def _json_default(value: Any) -> Any:
    if isinstance(value, Path):
        return str(value)
    return value


def _write_jsonl(path: Path, rows: list[dict[str, Any]]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True, default=_json_default, allow_nan=False) + "\n")
    return path


def _write_json(path: Path, payload: Any) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, default=_json_default, allow_nan=False) + "\n", encoding="utf-8")
    return path


def _round_sort_key(round_value: str) -> int:
    try:
        return int(str(round_value).lstrip("R"))
    except ValueError:
        return 999


def run_calibration_pipeline(
    *,
    md_input_root: str | Path = "docs/round",
    data_directory: str | Path = DATA_DIR,
    report_directory: str | Path = REPORT_DIR,
    write_runtime_profiles: bool = True,
    include_archive: bool = False,
) -> dict[str, Any]:
    md_root = Path(md_input_root)
    data_dir = Path(data_directory)
    report_dir = Path(report_directory)
    documents = discover_markdown_documents(md_root, include_archive=include_archive)
    results = v11_result_documents(documents)
    prompts = prompt_spec_documents(documents)

    parsed_documents: list[ParsedMarkdown] = []
    all_rows: dict[str, list[dict[str, Any]]] = defaultdict(list)
    registry: list[dict[str, Any]] = []
    for document in results:
        parsed = parse_markdown_document(document)
        parsed_documents.append(parsed)
        registry.append(parsed.registry_row)
        for row_type, rows in parsed.rows_by_type.items():
            all_rows[row_type].extend(rows)
    _attach_case_context(all_rows)

    for prompt in prompts:
        registry.append(
            {
                "file_path": str(prompt.path),
                "sha256": prompt.sha256,
                "round": prompt.round,
                "loop": prompt.loop,
                "sector": None,
                "extraction_status": "excluded",
                "parsed_trigger_row_count": 0,
                "rejected_row_count": 0,
                "exclusion_reason": "prompt_spec_file_excluded",
            }
        )

    validation = validate_trigger_rows(all_rows["trigger"])
    representative_rows, dedupe_map = dedupe_trigger_rows(validation.valid_rows)
    aggregate_rows = aggregate_validated_rows(representative_rows)

    rounds_covered = sorted({row.get("round") for row in registry if row.get("round")}, key=_round_sort_key)
    required_rounds = {f"R{number}" for number in range(1, 14)}
    coverage_passed = len(results) >= 100 and required_rounds.issubset(set(rounds_covered))

    promotion = promote_calibrated_profile(
        representative_rows,
        coverage_passed=coverage_passed,
        output_directory=data_dir,
        write_runtime_profiles=write_runtime_profiles,
    )

    output_paths = _write_data_outputs(data_dir, registry, all_rows, validation, representative_rows, dedupe_map, aggregate_rows)
    summary = _build_summary(
        md_root=md_root,
        documents=documents,
        results=results,
        prompts=prompts,
        parsed_documents=parsed_documents,
        registry=registry,
        all_rows=all_rows,
        validation=validation,
        representative_rows=representative_rows,
        rounds_covered=rounds_covered,
        promotion=promotion,
    )
    report_paths = _write_reports(report_dir, summary, aggregate_rows, representative_rows, validation, promotion)
    if not coverage_passed:
        coverage_failure_path = report_dir / "coverage_failure_report.md"
        coverage_failure_path.write_text(_render_coverage_failure(summary), encoding="utf-8")
        report_paths["coverage_failure_report"] = coverage_failure_path
    else:
        stale_failure_report = report_dir / "coverage_failure_report.md"
        if stale_failure_report.exists():
            stale_failure_report.unlink()
    return {"summary": summary, "data_outputs": output_paths, "reports": report_paths, "promotion": promotion}


def run_v12_full_pipeline(
    *,
    md_input_root: str | Path = "docs/round",
    data_directory: str | Path = V12_DATA_DIR,
    report_directory: str | Path = V12_REPORT_DIR,
    preserve_global_profile: bool = True,
    include_archive: bool = False,
) -> dict[str, Any]:
    md_root = Path(md_input_root)
    data_dir = Path(data_directory)
    report_dir = Path(report_directory)
    active_before = Path("configs/e2r_scoring_profile_active.yaml").read_text(encoding="utf-8") if Path("configs/e2r_scoring_profile_active.yaml").exists() else ""
    documents = discover_markdown_documents(md_root, include_archive=include_archive)
    results = v12_result_documents(documents)
    prompts = prompt_spec_documents(documents)
    if not results:
        raise RuntimeError(f"zero v12 result MDs found under {md_root}")

    parsed_documents: list[ParsedMarkdown] = []
    all_rows: dict[str, list[dict[str, Any]]] = defaultdict(list)
    registry: list[dict[str, Any]] = []
    for document in results:
        parsed = parse_markdown_document(document)
        parsed_documents.append(parsed)
        registry.append(parsed.registry_row)
        for row_type, rows in parsed.rows_by_type.items():
            all_rows[row_type].extend(rows)
    _attach_case_context(all_rows)

    if not any(parsed.rows_by_type.get("trigger") for parsed in parsed_documents):
        raise RuntimeError("v12 result MDs were found, but none produced trigger rows")

    validation = validate_v12_trigger_rows(all_rows["trigger"])
    representative_rows, dedupe_map = dedupe_v12_trigger_rows(validation.valid_rows)
    aggregate_rows = aggregate_v12_rows(representative_rows)
    stage_transition_rows = build_stage_transition_summary(representative_rows)

    output_paths = _write_v12_data_outputs(
        data_dir,
        registry,
        all_rows,
        validation,
        representative_rows,
        dedupe_map,
        aggregate_rows,
        stage_transition_rows,
    )
    transition_paths = write_stage_transition_outputs(
        representative_rows,
        data_directory=data_dir,
        report_directory=report_dir,
    )
    shadow_paths = write_v12_shadow_outputs(
        representative_rows,
        aggregate_rows,
        stage_transition_rows,
        rejected_rows=validation.rejected_rows,
        data_directory=data_dir,
        report_directory=report_dir,
    )
    summary = _build_v12_summary(
        md_root=md_root,
        include_archive=include_archive,
        documents=documents,
        results=results,
        prompts=prompts,
        parsed_documents=parsed_documents,
        registry=registry,
        all_rows=all_rows,
        validation=validation,
        representative_rows=representative_rows,
        aggregate_rows=aggregate_rows,
        stage_transition_rows=stage_transition_rows,
    )
    report_paths = _write_v12_reports(report_dir, summary, aggregate_rows, validation)
    active_after = Path("configs/e2r_scoring_profile_active.yaml").read_text(encoding="utf-8") if Path("configs/e2r_scoring_profile_active.yaml").exists() else ""
    if preserve_global_profile and active_before != active_after:
        raise RuntimeError("v12 run changed configs/e2r_scoring_profile_active.yaml, which is not allowed")
    return {
        "summary": summary,
        "data_outputs": {**output_paths, **transition_paths, **shadow_paths},
        "reports": {**report_paths, **transition_paths, **shadow_paths},
    }


def run_v12_calibration_pipeline(
    *,
    md_input_root: str | Path = "docs/round",
    data_directory: str | Path = V12_DATA_DIR,
    report_directory: str | Path = V12_REPORT_DIR,
    activate_profile: bool = True,
    include_archive: bool = False,
) -> dict[str, Any]:
    """One-command v12 flow: ingest, validate, derive patches, and apply safe runtime profile."""

    result = run_v12_full_pipeline(
        md_input_root=md_input_root,
        data_directory=data_directory,
        report_directory=report_directory,
        preserve_global_profile=False,
        include_archive=include_archive,
    )
    apply_result = write_v12_rolling_profile(
        patch_specs_path=Path(data_directory) / "v12_patch_specs.jsonl",
        report_directory=report_directory,
        activate=activate_profile,
    )
    weight_result = write_archetype_weight_runtime_profile(
        aggregate_metrics_path=Path(data_directory) / "v12_aggregate_metrics.json",
        report_path=Path(report_directory) / "archetype_weight_runtime_report.md",
    )
    result["summary"].update(
        {
            "active_default_profile": apply_result["summary"]["profile_id"],
            "active_default_profile_preserved": not activate_profile,
            "production_default_scoring_changed": activate_profile,
            "rolling_calibration_profile_path": apply_result["summary"]["profile_path"],
            "rolling_calibration_applied_patch_count": apply_result["summary"]["applied_patch_count"],
            "rolling_calibration_axis_counts": apply_result["summary"]["applied_axis_counts"],
            "archetype_weight_profile_path": weight_result["profile_path"],
            "archetype_weight_report_path": weight_result["report_path"],
            "archetype_weight_count": weight_result["archetype_count"],
            "large_sector_weight_count": weight_result["large_sector_count"],
        }
    )
    result["data_outputs"]["rolling_calibration_profile"] = Path(apply_result["summary"]["profile_path"])
    result["data_outputs"]["archetype_weight_profile"] = Path(weight_result["profile_path"])
    result["reports"]["rolling_calibration_apply_report"] = Path(report_directory) / "rolling_calibration_apply_report.md"
    result["reports"]["rolling_calibration_apply_summary"] = Path(report_directory) / "rolling_calibration_apply_summary.json"
    result["reports"]["archetype_weight_runtime_report"] = Path(weight_result["report_path"])
    Path(report_directory).mkdir(parents=True, exist_ok=True)
    (Path(report_directory) / "ingest_summary.md").write_text(
        _render_v12_ingest_summary(result["summary"]),
        encoding="utf-8",
    )
    return result


def _attach_case_context(all_rows: dict[str, list[dict[str, Any]]]) -> None:
    cases_by_id = {row.get("case_id"): row for row in all_rows.get("case", []) if row.get("case_id")}
    for row in all_rows.get("trigger", []):
        case = cases_by_id.get(row.get("case_id"))
        if not case:
            continue
        for key in ("positive_or_counterexample", "case_type", "company_name", "current_profile_verdict", "fine_archetype_id"):
            if case.get(key) and not row.get(key):
                row[key] = case[key]


def _write_data_outputs(
    data_dir: Path,
    registry: list[dict[str, Any]],
    all_rows: dict[str, list[dict[str, Any]]],
    validation,
    representative_rows: list[dict[str, Any]],
    dedupe_map: list[dict[str, Any]],
    aggregate_rows: list[dict[str, Any]],
) -> dict[str, Path]:
    outputs = {
        "md_registry": _write_jsonl(data_dir / "md_registry.jsonl", registry),
        "price_source_validations": _write_jsonl(data_dir / "price_source_validations.jsonl", all_rows["price_source_validation"]),
        "extracted_cases": _write_jsonl(data_dir / "extracted_cases.jsonl", all_rows["case"]),
        "extracted_triggers_raw": _write_jsonl(data_dir / "extracted_triggers_raw.jsonl", all_rows["trigger"]),
        "trigger_rows_validated": _write_jsonl(data_dir / "trigger_rows_validated.jsonl", validation.valid_rows),
        "trigger_rows_representative": _write_jsonl(data_dir / "trigger_rows_representative.jsonl", representative_rows),
        "score_simulation_rows": _write_jsonl(data_dir / "score_simulation_rows.jsonl", all_rows["score_simulation"]),
        "profile_comparison_rows": _write_jsonl(data_dir / "profile_comparison_rows.jsonl", all_rows["profile_comparison"]),
        "shadow_weight_events": _write_jsonl(data_dir / "shadow_weight_events.jsonl", all_rows["shadow_weight"]),
        "optimization_decisions": _write_jsonl(data_dir / "optimization_decisions.jsonl", all_rows["optimization_decision"]),
        "aggregate_metric_rows": _write_jsonl(data_dir / "aggregate_metric_rows.jsonl", aggregate_rows + all_rows["aggregate_metric"]),
        "narrative_only_rows": _write_jsonl(data_dir / "narrative_only_rows.jsonl", all_rows["narrative_only"]),
        "rejected_rows": _write_jsonl(data_dir / "rejected_rows.jsonl", validation.rejected_rows),
        "dedupe_map": _write_jsonl(data_dir / "dedupe_map.jsonl", dedupe_map),
    }
    return outputs


def _write_v12_data_outputs(
    data_dir: Path,
    registry: list[dict[str, Any]],
    all_rows: dict[str, list[dict[str, Any]]],
    validation,
    representative_rows: list[dict[str, Any]],
    dedupe_map: list[dict[str, Any]],
    aggregate_rows: list[dict[str, Any]],
    stage_transition_rows: list[dict[str, Any]],
) -> dict[str, Path]:
    outputs = {
        "v12_md_registry": _write_jsonl(data_dir / "v12_md_registry.jsonl", registry),
        "v12_extracted_cases": _write_jsonl(data_dir / "v12_extracted_cases.jsonl", all_rows["case"]),
        "v12_extracted_triggers_raw": _write_jsonl(data_dir / "v12_extracted_triggers_raw.jsonl", all_rows["trigger"]),
        "v12_trigger_rows_validated": _write_jsonl(data_dir / "v12_trigger_rows_validated.jsonl", validation.valid_rows),
        "v12_trigger_rows_representative": _write_jsonl(
            data_dir / "v12_trigger_rows_representative.jsonl", representative_rows
        ),
        "rejected_v12_rows": _write_jsonl(data_dir / "rejected_v12_rows.jsonl", validation.rejected_rows),
        "v12_dedupe_map": _write_jsonl(data_dir / "v12_dedupe_map.jsonl", dedupe_map),
        "v12_aggregate_metrics": _write_json(data_dir / "v12_aggregate_metrics.json", aggregate_rows),
        "v12_raw_aggregate_metric_rows": _write_jsonl(
            data_dir / "v12_raw_aggregate_metric_rows.jsonl", all_rows["aggregate_metric"]
        ),
        "stage_transition_summary": _write_jsonl(data_dir / "stage_transition_summary.jsonl", stage_transition_rows),
        "v12_residual_contribution_rows": _write_jsonl(
            data_dir / "v12_residual_contribution_rows.jsonl", all_rows["residual_contribution"]
        ),
        "v12_raw_shadow_weight_rows": _write_jsonl(
            data_dir / "v12_raw_shadow_weight_rows.jsonl", all_rows["shadow_weight"]
        ),
        "v12_coverage_matrix_rows": _write_jsonl(data_dir / "v12_coverage_matrix_rows.jsonl", all_rows["coverage_matrix"]),
    }
    return outputs


def _build_summary(
    *,
    md_root: Path,
    documents,
    results,
    prompts,
    parsed_documents,
    registry,
    all_rows,
    validation,
    representative_rows,
    rounds_covered,
    promotion: PromotionResult,
) -> dict[str, Any]:
    rejected_reasons = Counter(
        reason
        for row in validation.rejected_rows
        for reason in row.get("rejection_reasons", row.get("validation_reasons", []))
    )
    sectors = sorted({row.get("sector") for row in all_rows["trigger"] if row.get("sector")})
    failed_docs = [parsed for parsed in parsed_documents if parsed.failed]
    metadata_only_docs = [parsed for parsed in parsed_documents if parsed.registry_row["extraction_status"] == "metadata_only"]
    duplicate_doc_count = len(results) - len({document.sha256 for document in results})
    return {
        "repo": "https://github.com/Songdaiki/stock_agent",
        "md_input_root": str(md_root),
        "discovered_md_count": len(documents),
        "discovered_result_md_count": len(results),
        "excluded_prompt_spec_count": len(prompts),
        "unique_document_count": len({document.sha256 for document in results}),
        "duplicate_document_count": duplicate_doc_count,
        "parsed_document_count": sum(1 for row in registry if row.get("extraction_status") == "parsed"),
        "failed_document_count": len(failed_docs),
        "metadata_only_document_count": len(metadata_only_docs),
        "raw_trigger_rows": len(all_rows["trigger"]),
        "validated_trigger_rows": len(validation.valid_rows),
        "aggregate_representative_trigger_rows": len(representative_rows),
        "rejected_rows": len(validation.rejected_rows),
        "rejected_rows_by_reason": dict(sorted(rejected_reasons.items())),
        "rounds_covered": rounds_covered,
        "loops_covered": sorted({str(row.get("loop")) for row in registry if row.get("loop")}),
        "sectors_covered": sectors,
        "applied_scoring_axes_count": len(promotion.applied_axes),
        "shadow_only_axes_count": len(promotion.shadow_only_axes),
        "rejected_promotion_axes_count": len(promotion.rejected_axes),
        "baseline_profile_path": str(promotion.baseline_profile_path),
        "calibrated_profile_path": str(promotion.calibrated_profile_path),
        "active_profile_path": str(promotion.active_profile_path),
        "promotion_status": promotion.promotion_status,
        "production_default_scoring_changed": promotion.production_default_scoring_changed,
        "auto_trading_changed": False,
        "brokerage_api_touched": False,
        "price_source_validation_summary": Counter(
            row.get("validation_status", "unknown") for row in all_rows["price_source_validation"]
        ),
    }


def _build_v12_summary(
    *,
    md_root: Path,
    include_archive: bool = False,
    documents,
    results,
    prompts,
    parsed_documents,
    registry,
    all_rows,
    validation,
    representative_rows,
    aggregate_rows,
    stage_transition_rows,
) -> dict[str, Any]:
    rejected_reasons = Counter(
        reason
        for row in validation.rejected_rows
        for reason in row.get("rejection_reasons", row.get("validation_reasons", []))
    )
    failed_docs = [parsed for parsed in parsed_documents if parsed.failed]
    metadata_only_docs = [parsed for parsed in parsed_documents if parsed.registry_row["extraction_status"] == "metadata_only"]
    large_sectors = sorted({row.get("large_sector_id") for row in representative_rows if row.get("large_sector_id")})
    archetypes = sorted({row.get("canonical_archetype_id") for row in representative_rows if row.get("canonical_archetype_id")})
    global_metric = next((row for row in aggregate_rows if row.get("group_name") == "global_v12"), {})
    return {
        "repo": "https://github.com/Songdaiki/stock_agent",
        "md_input_root": str(md_root),
        "include_archive": include_archive,
        "discovered_md_count": len(documents),
        "v12_result_md_count": len(results),
        "excluded_prompt_spec_count": len(prompts),
        "v12_parsed_document_count": sum(1 for row in registry if row.get("extraction_status") == "parsed"),
        "v12_failed_document_count": len(failed_docs),
        "v12_metadata_only_document_count": len(metadata_only_docs),
        "v12_raw_trigger_rows": len(all_rows["trigger"]),
        "v12_validated_trigger_rows": len(validation.valid_rows),
        "v12_representative_trigger_rows": len(representative_rows),
        "v12_rejected_rows": len(validation.rejected_rows),
        "v12_raw_aggregate_metric_rows": len(all_rows["aggregate_metric"]),
        "v12_raw_shadow_weight_rows": len(all_rows["shadow_weight"]),
        "rejected_rows_by_reason": dict(sorted(rejected_reasons.items())),
        "large_sectors_covered": large_sectors,
        "canonical_archetypes_covered": archetypes,
        "stage_transition_summary_rows": len(stage_transition_rows),
        "positive_case_count": global_metric.get("positive_case_count", 0),
        "counterexample_count": global_metric.get("counterexample_count", 0),
        "evidence_url_pending_count": global_metric.get("evidence_url_pending_count", 0),
        "source_proxy_only_count": global_metric.get("source_proxy_only_count", 0),
        "default_promotion_ready": False,
        "active_default_profile_preserved": True,
        "production_default_scoring_changed": False,
        "auto_trading_changed": False,
        "brokerage_api_touched": False,
    }


def _write_v12_reports(report_dir: Path, summary: dict[str, Any], aggregate_rows: list[dict[str, Any]], validation) -> dict[str, Path]:
    report_dir.mkdir(parents=True, exist_ok=True)
    reports = {
        "ingest_summary": report_dir / "ingest_summary.md",
        "coverage_matrix": report_dir / "coverage_matrix.md",
    }
    reports["ingest_summary"].write_text(_render_v12_ingest_summary(summary), encoding="utf-8")
    reports["coverage_matrix"].write_text(_render_v12_coverage_matrix(aggregate_rows), encoding="utf-8")
    # residual_error_report.md is also written by v12_shadow; this minimal write
    # guarantees the file exists even if shadow generation changes later.
    residual_path = report_dir / "residual_error_report.md"
    if not residual_path.exists():
        residual_path.write_text(_render_v12_validation_residuals(validation), encoding="utf-8")
    return reports


def _render_v12_ingest_summary(summary: dict[str, Any]) -> str:
    lines = [
        "# V12 Residual Calibration Ingest Summary",
        "",
        "v12는 rolling calibration 입력입니다. `run-v12-calibration`은 검증된 apply_next_patch를 기본 profile에 반영합니다.",
        "`run-v12-full`은 진단/감사용 ingest이며 active profile을 바꾸지 않습니다.",
        "case_fixture나 과거 연구 재현 성공은 live discovery 증명이 아닙니다.",
        "source proxy 또는 evidence URL 한계는 promotion blocker로 보고서에 남깁니다.",
        "",
    ]
    for key in (
        "md_input_root",
        "include_archive",
        "v12_result_md_count",
        "v12_parsed_document_count",
        "v12_failed_document_count",
        "v12_raw_trigger_rows",
        "v12_validated_trigger_rows",
        "v12_representative_trigger_rows",
        "v12_rejected_rows",
        "v12_raw_aggregate_metric_rows",
        "v12_raw_shadow_weight_rows",
        "large_sectors_covered",
        "canonical_archetypes_covered",
        "stage_transition_summary_rows",
        "evidence_url_pending_count",
        "source_proxy_only_count",
        "active_default_profile_preserved",
        "production_default_scoring_changed",
        "archetype_weight_profile_path",
        "archetype_weight_report_path",
        "archetype_weight_count",
        "large_sector_weight_count",
    ):
        lines.append(f"- {key}: `{summary.get(key)}`")
    lines.extend(["", "## Rejected Rows By Reason"])
    for reason, count in summary["rejected_rows_by_reason"].items():
        lines.append(f"- {reason}: {count}")
    return "\n".join(lines) + "\n"


def _render_v12_coverage_matrix(aggregate_rows: list[dict[str, Any]]) -> str:
    lines = [
        "# V12 Coverage Matrix",
        "",
        "v12 coverage는 rolling calibration의 근거 장부입니다. active 반영은 검증된 apply_next_patch만 scope 제한으로 적용합니다.",
        "",
        "| group | value | rows | symbols | positives | counterexamples | evidence URL pending | source proxy | good Stage2 | bad Stage2 |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in aggregate_rows:
        if row.get("group_name") not in {"global_v12", "large_sector_id", "canonical_archetype_id"}:
            continue
        lines.append(
            "| {group} | {value} | {rows} | {symbols} | {positive} | {counter} | {pending} | {proxy} | {good} | {bad} |".format(
                group=row.get("group_name"),
                value=row.get("group_value"),
                rows=row.get("row_count"),
                symbols=row.get("unique_symbol_count"),
                positive=row.get("positive_case_count"),
                counter=row.get("counterexample_count"),
                pending=row.get("evidence_url_pending_count"),
                proxy=row.get("source_proxy_only_count"),
                good=row.get("good_stage2_count"),
                bad=row.get("bad_stage2_count"),
            )
        )
    return "\n".join(lines) + "\n"


def _render_v12_validation_residuals(validation) -> str:
    lines = [
        "# V12 Residual Error Report",
        "",
        "| trigger_id | reasons |",
        "|---|---|",
    ]
    for row in validation.rejected_rows:
        lines.append(f"| {row.get('trigger_id')} | {row.get('rejection_reasons') or row.get('validation_reasons')} |")
    return "\n".join(lines) + "\n"


def _write_reports(
    report_dir: Path,
    summary: dict[str, Any],
    aggregate_rows: list[dict[str, Any]],
    representative_rows: list[dict[str, Any]],
    validation,
    promotion: PromotionResult,
) -> dict[str, Path]:
    report_dir.mkdir(parents=True, exist_ok=True)
    by_round_dir = report_dir / "by_round"
    by_round_dir.mkdir(parents=True, exist_ok=True)
    reports = {
        "ingest_summary": report_dir / "ingest_summary.md",
        "dedupe_report": report_dir / "dedupe_report.md",
        "validation_report": report_dir / "validation_report.md",
        "calibrated_profile_report": report_dir / "calibrated_profile_report.md",
        "applied_scoring_diff": report_dir / "applied_scoring_diff.md",
        "rejected_promotion_candidates": report_dir / "rejected_promotion_candidates.md",
    }
    reports["ingest_summary"].write_text(_render_ingest_summary(summary), encoding="utf-8")
    reports["dedupe_report"].write_text(_render_dedupe_report(summary), encoding="utf-8")
    reports["validation_report"].write_text(_render_validation_report(summary), encoding="utf-8")
    reports["calibrated_profile_report"].write_text(_render_profile_report(summary, promotion), encoding="utf-8")
    reports["applied_scoring_diff"].write_text(_render_applied_diff(promotion), encoding="utf-8")
    reports["rejected_promotion_candidates"].write_text(_render_rejected(promotion), encoding="utf-8")

    rounds = {row.get("round") for row in representative_rows if row.get("round")}
    for round_value in sorted(rounds, key=_round_sort_key):
        rows = [row for row in representative_rows if row.get("round") == round_value]
        path = by_round_dir / f"{round_value}.md"
        path.write_text(_render_round_report(round_value, rows, promotion), encoding="utf-8")
        reports[f"by_round_{round_value}"] = path
    return reports


def _render_ingest_summary(summary: dict[str, Any]) -> str:
    lines = ["# E2R Calibration Ingest Summary", ""]
    for key in (
        "md_input_root",
        "discovered_md_count",
        "discovered_result_md_count",
        "excluded_prompt_spec_count",
        "unique_document_count",
        "duplicate_document_count",
        "parsed_document_count",
        "failed_document_count",
        "metadata_only_document_count",
        "raw_trigger_rows",
        "validated_trigger_rows",
        "aggregate_representative_trigger_rows",
        "rejected_rows",
        "rounds_covered",
        "loops_covered",
        "sectors_covered",
    ):
        lines.append(f"- {key}: `{summary.get(key)}`")
    lines.extend(["", "## Rejected Rows By Reason"])
    for reason, count in summary["rejected_rows_by_reason"].items():
        lines.append(f"- {reason}: {count}")
    lines.extend(["", "## Price Source Validation Summary"])
    for status, count in dict(summary["price_source_validation_summary"]).items():
        lines.append(f"- {status}: {count}")
    return "\n".join(lines) + "\n"


def _render_dedupe_report(summary: dict[str, Any]) -> str:
    return "\n".join(
        [
            "# E2R Calibration Dedupe Report",
            "",
            "Repeated loops are lab-notebook revisions, not independent samples.",
            "대표 예시: 같은 `same_entry_group_id`가 여러 loop에 반복되면 raw row는 보존하지만 aggregate에는 대표 1개만 씁니다.",
            "",
            f"- raw_trigger_rows: `{summary['raw_trigger_rows']}`",
            f"- aggregate_representative_trigger_rows: `{summary['aggregate_representative_trigger_rows']}`",
            "- representative selection: same_entry_group_id > JSONL > explicit dedupe_for_aggregate > complete MFE/MAE > latest loop",
            "- fallback dedupe key: round, sector, symbol, archetype, trigger_type, trigger/entry date, rounded entry price, company",
        ]
    ) + "\n"


def _render_validation_report(summary: dict[str, Any]) -> str:
    lines = ["# E2R Calibration Validation Report", ""]
    lines.append("Rows must have Stock-Web tradable raw price paths, clean 180D MFE/MAE, representative status, and non-price evidence for positive entry calibration.")
    lines.append("")
    for reason, count in summary["rejected_rows_by_reason"].items():
        lines.append(f"- {reason}: {count}")
    return "\n".join(lines) + "\n"


def _render_profile_report(summary: dict[str, Any], promotion: PromotionResult) -> str:
    lines = [
        "# E2R Calibrated Profile Report",
        "",
        f"- promotion_status: `{promotion.promotion_status}`",
        f"- production_default_scoring_changed: `{promotion.production_default_scoring_changed}`",
        f"- active_profile_path: `{promotion.active_profile_path}`",
        f"- baseline rollback: set `E2R_SCORING_PROFILE=baseline` or edit `{promotion.active_profile_path}` to `active_profile: baseline`.",
        "- auto-trading: false",
        "- brokerage API touched: false",
        "",
        "## Applied Axes",
    ]
    for axis in promotion.applied_axes:
        lines.append(f"- {axis['axis']} / {axis['scope']}: {axis['old_value']} -> {axis['new_value']} ({axis['reason']})")
    lines.extend(["", "## Guardrails", "- 4B rows do not train positive entry weights.", "- 4C rows are thesis-break/protection only.", "- Price-only blowoff cannot promote Stage2/Stage3."])
    return "\n".join(lines) + "\n"


def _render_applied_diff(promotion: PromotionResult) -> str:
    lines = [
        "# Applied Scoring Diff",
        "",
        "| axis | scope | old baseline axis | new calibrated axis | delta | confidence | unique cases | unique rounds | reason |",
        "|---|---|---:|---:|---:|---|---:|---:|---|",
    ]
    for axis in promotion.applied_axes:
        lines.append(
            f"| {axis['axis']} | {axis['scope']} | {axis['old_value']} | {axis['new_value']} | {axis['delta']} | {axis['confidence']} | {axis['unique_case_count']} | {axis['unique_round_count']} | {axis['reason']} |"
        )
    return "\n".join(lines) + "\n"


def _render_rejected(promotion: PromotionResult) -> str:
    lines = [
        "# Rejected / Shadow-Only Promotion Candidates",
        "",
        "| axis | scope | reason | needed_for_promotion |",
        "|---|---|---|---|",
    ]
    for axis in promotion.shadow_only_axes + promotion.rejected_axes:
        lines.append(
            f"| {axis.get('axis')} | {axis.get('scope')} | {axis.get('reason')} | {axis.get('needed_for_promotion')} |"
        )
    return "\n".join(lines) + "\n"


def _render_round_report(round_value: str, rows: list[dict[str, Any]], promotion: PromotionResult) -> str:
    trigger_types = Counter(row.get("trigger_type") for row in rows)
    cases = sorted({row.get("case_id") for row in rows if row.get("case_id")})
    lines = [
        f"# {round_value} Calibration Report",
        "",
        f"- representative_triggers: `{len(rows)}`",
        f"- unique_cases: `{len(cases)}`",
        "",
        "## Trigger Types",
    ]
    for trigger_type, count in sorted(trigger_types.items()):
        lines.append(f"- {trigger_type}: {count}")
    lines.extend(["", "## Round-Specific Accepted Axes"])
    for axis in promotion.applied_axes:
        lines.append(f"- {axis['axis']}: cumulative axis applied; this round may be part of support if matching rows exist.")
    lines.extend(["", "## Rejected Axes", "- See rejected_promotion_candidates.md for held/rejected axes and missing evidence."])
    return "\n".join(lines) + "\n"


def _render_coverage_failure(summary: dict[str, Any]) -> str:
    missing_rounds = sorted({f"R{number}" for number in range(1, 14)} - set(summary["rounds_covered"]), key=_round_sort_key)
    return "\n".join(
        [
            "# E2R Calibration Coverage Failure",
            "",
            f"- discovered_result_md_count: `{summary['discovered_result_md_count']}`",
            f"- missing_result_md_count_to_100: `{max(0, 100 - summary['discovered_result_md_count'])}`",
            f"- missing_rounds: `{missing_rounds}`",
            "- promotion_status: `blocked_by_coverage_failure`",
            "- production_default_scoring_changed: `false`",
        ]
    ) + "\n"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Ingest Stock-Web E2R calibration MDs and promote validated scoring profile.")
    parser.add_argument("--md-input-root", default="docs/round")
    parser.add_argument("--data-directory", default=str(DATA_DIR))
    parser.add_argument("--report-directory", default=str(REPORT_DIR))
    subparsers = parser.add_subparsers(dest="command")
    v12_apply = subparsers.add_parser(
        "run-v12-calibration",
        help="Ingest v12 residual MDs, build stage transitions, and apply safe rolling calibration patches.",
    )
    v12_apply.add_argument("--md-input-root", default="docs/round")
    v12_apply.add_argument("--data-directory", default=str(V12_DATA_DIR))
    v12_apply.add_argument("--report-directory", default=str(V12_REPORT_DIR))
    v12_apply.add_argument("--no-activate-profile", action="store_true", default=False)
    v12_apply.add_argument(
        "--include-archive",
        action="store_true",
        default=False,
        help="Include archive folders such as docs/round/achieve for cumulative v12 recalibration.",
    )

    v12 = subparsers.add_parser("run-v12-full", help="Diagnostic v12 ingest and patch-ledger generation.")
    v12.add_argument("--md-input-root", default="docs/round")
    v12.add_argument("--data-directory", default=str(V12_DATA_DIR))
    v12.add_argument("--report-directory", default=str(V12_REPORT_DIR))
    v12.add_argument("--preserve-global-profile", action="store_true", default=True)
    v12.add_argument(
        "--include-archive",
        action="store_true",
        default=False,
        help="Include archive folders such as docs/round/achieve for cumulative v12 diagnostics.",
    )
    for alias in ("ingest-v12", "build-stage-transitions", "build-v12-shadow", "report-v12-coverage"):
        sub = subparsers.add_parser(alias, help=f"Alias for run-v12-full ({alias}).")
        sub.add_argument("--md-input-root", default="docs/round")
        sub.add_argument("--data-directory", default=str(V12_DATA_DIR))
        sub.add_argument("--report-directory", default=str(V12_REPORT_DIR))
        sub.add_argument("--preserve-global-profile", action="store_true", default=True)
        sub.add_argument(
            "--include-archive",
            action="store_true",
            default=False,
            help="Include archive folders such as docs/round/achieve for cumulative v12 diagnostics.",
        )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "run-v12-calibration":
        result = run_v12_calibration_pipeline(
            md_input_root=args.md_input_root,
            data_directory=args.data_directory,
            report_directory=args.report_directory,
            activate_profile=not args.no_activate_profile,
            include_archive=args.include_archive,
        )
    elif args.command in {"run-v12-full", "ingest-v12", "build-stage-transitions", "build-v12-shadow", "report-v12-coverage"}:
        result = run_v12_full_pipeline(
            md_input_root=args.md_input_root,
            data_directory=args.data_directory,
            report_directory=args.report_directory,
            preserve_global_profile=args.preserve_global_profile,
            include_archive=args.include_archive,
        )
    else:
        result = run_calibration_pipeline(
            md_input_root=args.md_input_root,
            data_directory=args.data_directory,
            report_directory=args.report_directory,
        )
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2, default=_json_default, allow_nan=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
