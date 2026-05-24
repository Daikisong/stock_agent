"""CLI for full Stock-Web calibration ingest, validation, dedupe and promotion."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any
import json

from .aggregate import aggregate_validated_rows
from .dedupe import dedupe_trigger_rows
from .md_discovery import discover_markdown_documents, prompt_spec_documents, result_documents
from .md_parser import ParsedMarkdown, parse_markdown_document
from .promotion import PromotionResult, promote_calibrated_profile
from .validation import validate_trigger_rows


DATA_DIR = Path("data/e2r/calibration")
REPORT_DIR = Path("reports/e2r_calibration")


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
) -> dict[str, Any]:
    md_root = Path(md_input_root)
    data_dir = Path(data_directory)
    report_dir = Path(report_directory)
    documents = discover_markdown_documents(md_root)
    results = result_documents(documents)
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
    lines.extend(["", "## Rejected Axes", "- See rejected_promotion_candidates.md for shadow-only axes and missing evidence."])
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
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    result = run_calibration_pipeline(
        md_input_root=args.md_input_root,
        data_directory=args.data_directory,
        report_directory=args.report_directory,
    )
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2, default=_json_default, allow_nan=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
