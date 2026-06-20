"""Select the first balanced V12 runtime repair slice.

The first implementation slice must not optimize only the HBM/SK Hynix case.
It should include archive/funnel, parser-feature, weighted-gate, and manual
classification examples so that fixes generalize across archetypes.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Mapping
import json


DEFAULT_ACCEPTANCE_SPEC_PATH = Path("docs/0619/v12_runtime_repair_acceptance_spec_2026-06-19.json")
DEFAULT_REPLAY_SPEC_PATH = Path("docs/0619/v12_runtime_replay_fixture_spec_2026-06-19.json")
DEFAULT_OUTPUT_JSON_PATH = Path("docs/0619/v12_runtime_first_repair_slice_2026-06-19.json")
DEFAULT_OUTPUT_MD_PATH = Path("docs/0619/v12_runtime_first_repair_slice_2026-06-19.md")


MANDATORY_ARCHETYPE_REASONS = {
    "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN": "candidate/funnel top priority and non-HBM financial capital-return example",
    "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION": "non-HBM bio commercialization candidate/funnel example",
    "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE": "non-HBM platform example with candidate/funnel plus parser primitive gaps",
    "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION": "top parser-feature bridge priority outside HBM",
    "C06_HBM_MEMORY_CUSTOMER_CAPACITY": "SK Hynix HBM field-bridge example; must not become name-specific bonus",
    "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE": "Samsung memory-recovery route example; checks HBM-adjacent route guard",
    "C02_POWER_GRID_DATACENTER_CAPEX": "weighted gate example after runtime candidates and fields are partly present",
    "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY": "manual classification example for policy/project lane",
    "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK": "manual classification example for battery call-off lane",
    "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY": "manual classification example for strategic-resource policy lane",
}


TARGET_MINIMUMS_BY_LANE = {
    "01_fixture_archive_and_candidate_funnel": 3,
    "02_parser_feature_bridge_contract": 4,
    "03_weighted_gate_validation_after_fields": 1,
    "04_manual_gap_classification": 3,
}


def _read_json(path: str | Path) -> dict[str, Any]:
    path_obj = Path(path)
    if not path_obj.exists():
        return {}
    return json.loads(path_obj.read_text(encoding="utf-8"))


def _counter_dict(counter: Counter[str]) -> dict[str, int]:
    return dict(sorted(counter.items()))


def _rows_by_archetype(payload: Mapping[str, Any], key: str = "rows") -> dict[str, dict[str, Any]]:
    return {str(row.get("canonical_archetype_id")): dict(row) for row in payload.get(key, [])}


def _rows_grouped_by_archetype(payload: Mapping[str, Any], key: str = "rows") -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in payload.get(key, []) or []:
        grouped[str(row.get("canonical_archetype_id"))].append(dict(row))
    return dict(grouped)


def _candidate_summary(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    summary: list[dict[str, Any]] = []
    for row in rows:
        candidate = dict(row.get("candidate") or {})
        summary.append(
            {
                "role": row.get("role"),
                "expected_outcome": row.get("expected_outcome"),
                "symbol": candidate.get("symbol"),
                "as_of_date": candidate.get("as_of_date"),
                "case_id": candidate.get("case_id"),
                "trigger_type": candidate.get("trigger_type"),
                "current_runtime_gap_status": row.get("current_runtime_gap_status"),
                "current_missing_required_bridge_axes": list(row.get("current_missing_required_bridge_axes") or ()),
            }
        )
    return summary


def _base_selection(rows: list[dict[str, Any]]) -> dict[str, str]:
    selected: dict[str, str] = {}
    by_lane: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        by_lane[str(row.get("implementation_lane"))].append(row)
    for lane, minimum in TARGET_MINIMUMS_BY_LANE.items():
        lane_rows = sorted(
            by_lane.get(lane, []),
            key=lambda item: (float(item.get("priority_score") or 0.0), str(item.get("canonical_archetype_id") or "")),
            reverse=True,
        )
        for row in lane_rows[:minimum]:
            archetype = str(row.get("canonical_archetype_id"))
            selected.setdefault(archetype, f"top {minimum} priority row for {lane}")
    for archetype, reason in MANDATORY_ARCHETYPE_REASONS.items():
        if any(str(row.get("canonical_archetype_id")) == archetype for row in rows):
            selected[archetype] = reason
    return selected


def _repair_sequence(lane: str) -> list[str]:
    if lane == "01_fixture_archive_and_candidate_funnel":
        return [
            "Archive exact as-of official universe, price history, report text snapshot, and search snapshot.",
            "Make the Green/guard symbols reach current replay by exact symbol+as_of_date.",
            "Run Green/guard replay; Green must reach Stage3-Green or emit field deficit, guard must not promote.",
        ]
    if lane == "02_parser_feature_bridge_contract":
        return [
            "Add parser structured fields with evidence ids for the missing primitive or axis.",
            "Map parser fields into FeatureEngineer bridge diagnostics without company-name conditions.",
            "Assert StageGateDiagnostics reports axis value and remaining deficit.",
        ]
    if lane == "03_weighted_gate_validation_after_fields":
        return [
            "Prove source-backed required axes are nonzero before changing thresholds.",
            "Compare archetype_component_* deficits with StageClassifier gate output.",
            "Only then validate any threshold or component balance adjustment with Green/guard pair.",
        ]
    return [
        "Classify the row into archive/funnel, parser-feature, or weighted-gate lane.",
        "Add explicit fixture status and missing input list.",
    ]


def build_v12_runtime_first_repair_slice(
    *,
    acceptance_spec_payload: Mapping[str, Any] | None = None,
    replay_spec_payload: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Build the first balanced implementation slice from the acceptance spec."""

    acceptance_payload = dict(acceptance_spec_payload or _read_json(DEFAULT_ACCEPTANCE_SPEC_PATH))
    replay_payload = dict(replay_spec_payload or _read_json(DEFAULT_REPLAY_SPEC_PATH))
    acceptance_rows = list(acceptance_payload.get("rows", []))
    replay_by_arch = _rows_grouped_by_archetype(replay_payload)
    selected_reasons = _base_selection(acceptance_rows)
    selected_rows: list[dict[str, Any]] = []
    lane_counts: Counter[str] = Counter()
    status_counts: Counter[str] = Counter()
    for row in acceptance_rows:
        archetype = str(row.get("canonical_archetype_id"))
        if archetype not in selected_reasons:
            continue
        lane = str(row.get("implementation_lane"))
        status = str(row.get("acceptance_status_current"))
        lane_counts[lane] += 1
        status_counts[status] += 1
        selected_rows.append(
            {
                "canonical_archetype_id": archetype,
                "selection_reason": selected_reasons[archetype],
                "implementation_lane": lane,
                "acceptance_status_current": status,
                "priority_score": row.get("priority_score"),
                "runtime_candidate_count": row.get("runtime_candidate_count"),
                "runtime_max_score": row.get("runtime_max_score"),
                "missing_required_bridge_axes": list(row.get("missing_required_bridge_axes") or ()),
                "missing_feature_parser_contract_primitives": list(
                    row.get("missing_feature_parser_contract_primitives") or ()
                ),
                "required_proof_artifacts": list(row.get("required_proof_artifacts") or ()),
                "acceptance_tests_to_add": list(row.get("acceptance_tests_to_add") or ()),
                "do_not_accept": row.get("do_not_accept"),
                "repair_sequence": _repair_sequence(lane),
                "replay_fixture_candidates": _candidate_summary(replay_by_arch.get(archetype, [])),
            }
        )
    selected_rows.sort(
        key=lambda item: (
            item["implementation_lane"],
            -(float(item.get("priority_score") or 0.0)),
            str(item.get("canonical_archetype_id") or ""),
        )
    )
    hbm_related = {
        "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
        "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE",
    }
    return {
        "schema_version": "v12_runtime_first_repair_slice_v1",
        "summary": {
            "selected_archetype_count": len(selected_rows),
            "selected_lane_counts": _counter_dict(lane_counts),
            "selected_acceptance_status_counts": _counter_dict(status_counts),
            "selected_hbm_or_samsung_related_count": sum(
                1 for row in selected_rows if row["canonical_archetype_id"] in hbm_related
            ),
            "selected_non_hbm_count": sum(1 for row in selected_rows if row["canonical_archetype_id"] not in hbm_related),
            "plain_conclusion": (
                "첫 수리 slice는 C06/C10을 포함하지만, C21/C23/C26/C20/C02도 같이 묶어 "
                "HBM 보너스가 아닌 전 아키타입 runtime 수리로 검증해야 한다."
            ),
        },
        "rows": selected_rows,
    }


def render_v12_runtime_first_repair_slice(payload: Mapping[str, Any]) -> str:
    summary = payload.get("summary", {})
    rows = list(payload.get("rows", []))
    lines = [
        "# V12 Runtime First Repair Slice",
        "",
        "이 문서는 다음 실제 구현의 첫 묶음을 고정한다. C06/C10을 포함하되, 비-HBM archive/funnel, parser-feature, weighted-gate 사례를 같이 넣어 HBM 과적합을 막는다.",
        "",
        "## Summary",
        "",
        f"- plain_conclusion: {summary.get('plain_conclusion')}",
        f"- selected_archetype_count: `{summary.get('selected_archetype_count')}`",
        f"- selected_lane_counts: `{summary.get('selected_lane_counts')}`",
        f"- selected_acceptance_status_counts: `{summary.get('selected_acceptance_status_counts')}`",
        f"- selected_hbm_or_samsung_related_count: `{summary.get('selected_hbm_or_samsung_related_count')}`",
        f"- selected_non_hbm_count: `{summary.get('selected_non_hbm_count')}`",
        "",
        "## Selected Rows",
        "",
        "| archetype | lane | reason | current status | candidates | missing axes | missing primitives | first tests |",
        "| --- | --- | --- | --- | ---: | --- | --- | --- |",
    ]
    for row in rows:
        lines.append(
            f"| {row.get('canonical_archetype_id')} | {row.get('implementation_lane')} | "
            f"{row.get('selection_reason')} | {row.get('acceptance_status_current')} | "
            f"{row.get('runtime_candidate_count')} | "
            f"{', '.join(row.get('missing_required_bridge_axes') or []) or 'none'} | "
            f"{', '.join(row.get('missing_feature_parser_contract_primitives') or []) or 'none'} | "
            f"{'<br>'.join((row.get('acceptance_tests_to_add') or [])[:3])} |"
        )
    lines.extend(
        [
            "",
            "## Repair Sequence",
            "",
            "| archetype | sequence | replay fixture candidates | do not accept |",
            "| --- | --- | --- | --- |",
        ]
    )
    for row in rows:
        fixtures = []
        for candidate in row.get("replay_fixture_candidates") or []:
            fixtures.append(
                f"{candidate.get('role')}:{candidate.get('symbol')}@{candidate.get('as_of_date')} "
                f"gap={candidate.get('current_runtime_gap_status')}"
            )
        lines.append(
            f"| {row.get('canonical_archetype_id')} | "
            f"{'<br>'.join(row.get('repair_sequence') or [])} | "
            f"{'<br>'.join(fixtures) or 'none'} | {row.get('do_not_accept')} |"
        )
    lines.extend(
        [
            "",
            "## Easy Reading",
            "",
            "- 첫 패치가 하닉만 Green으로 올리면 실패다.",
            "- C21/C23/C26은 시험지가 current replay에 들어오는지 확인하는 문제다.",
            "- C06/C10/C20은 답안지 칸, 즉 parser-feature field가 채워지는지 확인하는 문제다.",
            "- C02는 답안지 칸이 어느 정도 채워진 뒤 채점 기준이 맞는지 확인하는 문제다.",
        ]
    )
    return "\n".join(lines) + "\n"


def write_v12_runtime_first_repair_slice(
    *,
    output_json_path: str | Path = DEFAULT_OUTPUT_JSON_PATH,
    output_md_path: str | Path = DEFAULT_OUTPUT_MD_PATH,
) -> dict[str, Any]:
    payload = build_v12_runtime_first_repair_slice()
    json_path = Path(output_json_path)
    md_path = Path(output_md_path)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    md_path.write_text(render_v12_runtime_first_repair_slice(payload), encoding="utf-8")
    return {"json_path": str(json_path), "md_path": str(md_path), "summary": payload["summary"]}


if __name__ == "__main__":
    result = write_v12_runtime_first_repair_slice()
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
