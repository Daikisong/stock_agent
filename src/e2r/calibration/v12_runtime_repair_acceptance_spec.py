"""Acceptance criteria for V12 runtime repair lanes."""

from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import Any, Mapping
import json
import re


DEFAULT_BACKLOG_PATH = Path("docs/0619/v12_runtime_repair_execution_backlog_2026-06-19.json")
DEFAULT_OUTPUT_JSON_PATH = Path("docs/0619/v12_runtime_repair_acceptance_spec_2026-06-19.json")
DEFAULT_OUTPUT_MD_PATH = Path("docs/0619/v12_runtime_repair_acceptance_spec_2026-06-19.md")


LANE_ORDER = (
    "01_fixture_archive_and_candidate_funnel",
    "02_parser_feature_bridge_contract",
    "03_weighted_gate_validation_after_fields",
    "04_manual_gap_classification",
)


LANE_ACCEPTANCE_REQUIREMENTS = {
    "01_fixture_archive_and_candidate_funnel": [
        "Green/guard pair has exact as-of official universe, price history, report text snapshot, and search snapshot inputs.",
        "Both roles reach the replay candidate set by exact symbol+as_of_date, not merely same symbol or benchmark label.",
        "Green role either reaches Stage3-Green or emits source-backed field-level deficit; guard role must not reach Stage3-Green.",
        "Replay proof is point-in-time: no report, price, disclosure, or label after as_of_date is used.",
    ],
    "02_parser_feature_bridge_contract": [
        "Parser exposes the missing primitive or axis as a source-backed structured field with evidence ids.",
        "FeatureEngineer converts the field into the required runtime component or bridge diagnostic without company-name special cases.",
        "StageGateDiagnostics reports the axis value and remaining deficit instead of a generic failed gate.",
        "Positive/guard fixture pair proves the new field raises true positives without opening the guard.",
    ],
    "03_weighted_gate_validation_after_fields": [
        "Positive/guard pair has nonzero source-backed required axes before any threshold or weight discussion.",
        "Weighted component deficits are computed from archetype_component_* values and match StageClassifier gates.",
        "Any threshold or balance change improves positive recall while preserving guard rejection.",
        "Score explanation names the field-level remaining deficit if Stage3-Green is still blocked.",
    ],
    "04_manual_gap_classification": [
        "Manual row is reclassified into fixture/archive, parser-feature, or stage-gate lane with evidence.",
        "The row has an explicit Green/guard fixture status and missing input list.",
        "The row is not treated as complete while manual_review remains its stop layer.",
    ],
}


LANE_CURRENT_BLOCKERS = {
    "01_fixture_archive_and_candidate_funnel": [
        "pair_retrospective_ready is false",
        "pair_strict_pit_ready is false",
        "current runtime exact candidate match is absent",
    ],
    "02_parser_feature_bridge_contract": [
        "missing_required_bridge_axes is non-empty or primitive field contract is missing",
        "runtime candidate exists but feature/gate axis remains zero or weak",
    ],
    "03_weighted_gate_validation_after_fields": [
        "field exists but weighted total/component gate still blocks Stage3-Green",
        "positive/guard pair evidence is not yet enough to justify threshold changes",
    ],
    "04_manual_gap_classification": [
        "stop layer is still manual_review",
        "no concrete candidate/archive, parser-feature, or stage-gate owner is assigned",
    ],
}


LANE_ACCEPTANCE_TEST_TEMPLATES = {
    "01_fixture_archive_and_candidate_funnel": [
        "test_{slug}_green_guard_pair_has_exact_asof_inputs",
        "test_{slug}_fixtures_reach_runtime_candidate_set_by_exact_symbol_date",
        "test_{slug}_guard_does_not_promote_when_green_candidate_is_unlocked",
    ],
    "02_parser_feature_bridge_contract": [
        "test_{slug}_parser_extracts_missing_primitives_with_evidence_ids",
        "test_{slug}_feature_bridge_populates_missing_axes_without_name_special_case",
        "test_{slug}_stage_gate_diagnostics_reports_axis_deficit",
    ],
    "03_weighted_gate_validation_after_fields": [
        "test_{slug}_weighted_gate_uses_archetype_components_after_fields_present",
        "test_{slug}_positive_guard_pair_validates_threshold_or_balance_change",
    ],
    "04_manual_gap_classification": [
        "test_{slug}_manual_gap_is_reclassified_to_concrete_repair_lane",
    ],
}


def _read_json(path: str | Path) -> dict[str, Any]:
    path_obj = Path(path)
    if not path_obj.exists():
        return {}
    return json.loads(path_obj.read_text(encoding="utf-8"))


def _counter_dict(counter: Counter[str]) -> dict[str, int]:
    return dict(sorted(counter.items()))


def _slug(archetype: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "_", archetype.lower()).strip("_")
    return slug or "unknown_archetype"


def _acceptance_status(row: Mapping[str, Any]) -> str:
    lane = str(row.get("implementation_lane") or "")
    if lane == "01_fixture_archive_and_candidate_funnel":
        if row.get("pair_retrospective_ready") and row.get("pair_strict_pit_ready"):
            return "ready_for_exact_replay_acceptance"
        if row.get("pair_retrospective_ready"):
            return "retrospective_ready_but_strict_pit_missing"
        return "blocked_missing_exact_fixture_archive_or_candidate_funnel"
    if lane == "02_parser_feature_bridge_contract":
        missing_axes = list(row.get("missing_required_bridge_axes") or ())
        missing_primitives = list(row.get("missing_feature_parser_contract_primitives") or ())
        if not missing_axes and not missing_primitives:
            return "bridge_ready_needs_positive_guard_validation"
        return "blocked_missing_parser_feature_or_gate_axis_contract"
    if lane == "03_weighted_gate_validation_after_fields":
        return "blocked_weighted_gate_after_fields_present"
    return "blocked_manual_gap_unclassified"


def _row_blockers(row: Mapping[str, Any]) -> list[str]:
    lane = str(row.get("implementation_lane") or "")
    blockers = list(LANE_CURRENT_BLOCKERS.get(lane, ()))
    missing_axes = list(row.get("missing_required_bridge_axes") or ())
    missing_primitives = list(row.get("missing_feature_parser_contract_primitives") or ())
    readiness = row.get("readiness_summary") or {}
    funnel = row.get("funnel_summary") or {}
    if missing_axes:
        blockers.append(f"missing_required_bridge_axes={','.join(str(axis) for axis in missing_axes)}")
    if missing_primitives:
        blockers.append(
            f"missing_feature_parser_contract_primitives={','.join(str(item) for item in missing_primitives[:8])}"
        )
    if readiness.get("retrospective_missing_input_counts"):
        blockers.append(f"retrospective_missing_inputs={readiness.get('retrospective_missing_input_counts')}")
    if funnel.get("fixture_funnel_status_counts"):
        blockers.append(f"fixture_funnel_status={funnel.get('fixture_funnel_status_counts')}")
    return blockers


def _tests_for_row(row: Mapping[str, Any]) -> list[str]:
    lane = str(row.get("implementation_lane") or "")
    slug = _slug(str(row.get("canonical_archetype_id") or "unknown_archetype"))
    return [template.format(slug=slug) for template in LANE_ACCEPTANCE_TEST_TEMPLATES.get(lane, ())]


def _proof_artifacts(row: Mapping[str, Any]) -> list[str]:
    lane = str(row.get("implementation_lane") or "")
    if lane == "01_fixture_archive_and_candidate_funnel":
        return [
            "local official universe row",
            "370d as-of price history with a recent price anchor",
            "point-in-time report/search snapshots",
            "exact Green/guard replay output",
        ]
    if lane == "02_parser_feature_bridge_contract":
        return [
            "parser structured field with evidence ids",
            "FeatureEngineeringResult bridge diagnostic",
            "StageGateDiagnostics axis deficit",
            "positive/guard fixture assertion",
        ]
    if lane == "03_weighted_gate_validation_after_fields":
        return [
            "ScoreSnapshot archetype_component_* values",
            "StageClassifier gate diagnostics",
            "positive/guard parity result",
        ]
    return ["updated runtime audit row with concrete lane assignment"]


def build_v12_runtime_repair_acceptance_spec(
    *,
    backlog_payload: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Build lane and row-level acceptance requirements for runtime repairs."""

    backlog = dict(backlog_payload or _read_json(DEFAULT_BACKLOG_PATH))
    rows = list(backlog.get("rows", []))
    lane_counts: Counter[str] = Counter()
    status_counts: Counter[str] = Counter()
    row_payloads: list[dict[str, Any]] = []
    for row in rows:
        lane = str(row.get("implementation_lane") or "04_manual_gap_classification")
        status = _acceptance_status(row)
        lane_counts[lane] += 1
        status_counts[status] += 1
        row_payloads.append(
            {
                "canonical_archetype_id": row.get("canonical_archetype_id"),
                "implementation_lane": lane,
                "acceptance_status_current": status,
                "priority_score": row.get("priority_score"),
                "runtime_candidate_count": row.get("runtime_candidate_count"),
                "runtime_max_score": row.get("runtime_max_score"),
                "missing_required_bridge_axes": list(row.get("missing_required_bridge_axes") or ()),
                "missing_feature_parser_contract_primitives": list(
                    row.get("missing_feature_parser_contract_primitives") or ()
                ),
                "pair_retrospective_ready": bool(row.get("pair_retrospective_ready")),
                "pair_strict_pit_ready": bool(row.get("pair_strict_pit_ready")),
                "current_blockers": _row_blockers(row),
                "required_proof_artifacts": _proof_artifacts(row),
                "acceptance_tests_to_add": _tests_for_row(row),
                "do_not_accept": row.get("do_not_do"),
            }
        )

    row_payloads.sort(
        key=lambda item: (
            item["implementation_lane"],
            -(float(item.get("priority_score") or 0.0)),
            str(item.get("canonical_archetype_id") or ""),
        )
    )
    lane_specs = [
        {
            "implementation_lane": lane,
            "acceptance_requirements": list(LANE_ACCEPTANCE_REQUIREMENTS[lane]),
            "current_blockers": list(LANE_CURRENT_BLOCKERS[lane]),
            "test_templates": list(LANE_ACCEPTANCE_TEST_TEMPLATES[lane]),
        }
        for lane in LANE_ORDER
    ]
    return {
        "schema_version": "v12_runtime_repair_acceptance_spec_v1",
        "summary": {
            "archetype_count": len(row_payloads),
            "implementation_lane_counts": _counter_dict(lane_counts),
            "acceptance_status_counts": _counter_dict(status_counts),
            "all_pairs_retrospective_ready_count": sum(1 for row in row_payloads if row["pair_retrospective_ready"]),
            "all_pairs_strict_pit_ready_count": sum(1 for row in row_payloads if row["pair_strict_pit_ready"]),
            "plain_conclusion": (
                "수리 완료 판정은 점수 상승이 아니라 exact replay 입력, source-backed field, "
                "positive/guard gate parity가 함께 증명될 때만 가능하다."
            ),
        },
        "lane_specs": lane_specs,
        "rows": row_payloads,
    }


def render_v12_runtime_repair_acceptance_spec(payload: Mapping[str, Any]) -> str:
    summary = payload.get("summary", {})
    lane_specs = list(payload.get("lane_specs", []))
    rows = list(payload.get("rows", []))
    lines = [
        "# V12 Runtime Repair Acceptance Spec",
        "",
        "이 문서는 다음 패치가 진짜 수리인지 판정하는 완료 기준이다. 하닉/HBM만 올리는 보너스나 Green threshold 완화는 완료로 보지 않는다.",
        "",
        "## Summary",
        "",
        f"- plain_conclusion: {summary.get('plain_conclusion')}",
        f"- archetype_count: `{summary.get('archetype_count')}`",
        f"- implementation_lane_counts: `{summary.get('implementation_lane_counts')}`",
        f"- acceptance_status_counts: `{summary.get('acceptance_status_counts')}`",
        f"- all_pairs_retrospective_ready_count: `{summary.get('all_pairs_retrospective_ready_count')}`",
        f"- all_pairs_strict_pit_ready_count: `{summary.get('all_pairs_strict_pit_ready_count')}`",
        "",
        "## Lane Acceptance Requirements",
        "",
        "| lane | requirements | current blockers | test templates |",
        "| --- | --- | --- | --- |",
    ]
    for spec in lane_specs:
        lines.append(
            f"| {spec.get('implementation_lane')} | "
            f"{'<br>'.join(spec.get('acceptance_requirements') or [])} | "
            f"{'<br>'.join(spec.get('current_blockers') or [])} | "
            f"{'<br>'.join(spec.get('test_templates') or [])} |"
        )
    lines.extend(
        [
            "",
            "## Row Acceptance Matrix",
            "",
            "| archetype | lane | current status | candidates | max score | missing axes | missing primitives | required proof | acceptance tests |",
            "| --- | --- | --- | ---: | ---: | --- | --- | --- | --- |",
        ]
    )
    for row in rows:
        lines.append(
            f"| {row.get('canonical_archetype_id')} | {row.get('implementation_lane')} | "
            f"{row.get('acceptance_status_current')} | {row.get('runtime_candidate_count')} | "
            f"{row.get('runtime_max_score')} | "
            f"{', '.join(row.get('missing_required_bridge_axes') or []) or 'none'} | "
            f"{', '.join(row.get('missing_feature_parser_contract_primitives') or []) or 'none'} | "
            f"{'<br>'.join(row.get('required_proof_artifacts') or [])} | "
            f"{'<br>'.join(row.get('acceptance_tests_to_add') or [])} |"
        )
    lines.extend(
        [
            "",
            "## Easy Reading",
            "",
            "- 점수가 올라갔다고 끝이 아니다. 그 점수가 as-of 입력과 source-backed field에서 나온 것인지 보여야 한다.",
            "- Green 예시만 맞추면 안 된다. guard 예시가 같이 Green으로 뚫리지 않아야 한다.",
            "- 쉬운 예: 정답지를 보고 채점한 점수는 통과가 아니다. 시험 당시 문제지, 답안지, 채점표가 모두 남아 있어야 통과다.",
        ]
    )
    return "\n".join(lines) + "\n"


def write_v12_runtime_repair_acceptance_spec(
    *,
    output_json_path: str | Path = DEFAULT_OUTPUT_JSON_PATH,
    output_md_path: str | Path = DEFAULT_OUTPUT_MD_PATH,
) -> dict[str, Any]:
    payload = build_v12_runtime_repair_acceptance_spec()
    json_path = Path(output_json_path)
    md_path = Path(output_md_path)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    md_path.write_text(render_v12_runtime_repair_acceptance_spec(payload), encoding="utf-8")
    return {"json_path": str(json_path), "md_path": str(md_path), "summary": payload["summary"]}


if __name__ == "__main__":
    result = write_v12_runtime_repair_acceptance_spec()
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
