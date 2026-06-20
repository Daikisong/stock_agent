"""Audit where cumulative research enters weights but not runtime features."""

from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import Any, Mapping
import json


DEFAULT_WEIGHT_PROFILE_PATH = Path("configs/e2r_archetype_weight_profile_v2_2.json")
DEFAULT_REPAIR_BOARD_PATH = Path("docs/0619/v12_runtime_repair_priority_board_2026-06-19.json")
DEFAULT_SIGNAL_AUDIT_PATH = Path("docs/0619/v12_archetype_signal_runtime_translation_audit_2026-06-19.json")
DEFAULT_FIELD_AUDIT_PATH = Path("docs/0619/v12_bridge_spec_runtime_field_audit_2026-06-19.json")
DEFAULT_OUTPUT_JSON_PATH = Path("docs/0619/v12_weight_support_runtime_feature_audit_2026-06-19.json")
DEFAULT_OUTPUT_MD_PATH = Path("docs/0619/v12_weight_support_runtime_feature_audit_2026-06-19.md")


COMPONENT_KEYS = (
    "eps_fcf_explosion",
    "earnings_visibility",
    "bottleneck_pricing",
    "market_mispricing",
    "valuation_rerating",
    "capital_allocation",
    "information_confidence",
)


def _read_json(path: str | Path) -> dict[str, Any]:
    path_obj = Path(path)
    if not path_obj.exists():
        return {}
    return json.loads(path_obj.read_text(encoding="utf-8"))


def _rows_by_archetype(payload: Mapping[str, Any]) -> dict[str, dict[str, Any]]:
    return {str(row.get("canonical_archetype_id")): dict(row) for row in payload.get("rows", [])}


def _counter_dict(counter: Counter[str]) -> dict[str, int]:
    return dict(sorted(counter.items()))


def _support_metric(support: Mapping[str, Any], key: str) -> float:
    value = support.get(key)
    if value is None:
        return 0.0
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


def _weights(row: Mapping[str, Any]) -> dict[str, float]:
    weights = row.get("weights", {})
    return {key: float(weights.get(key, 0.0) or 0.0) for key in COMPONENT_KEYS}


def _top_weight_axes(weights: Mapping[str, float], limit: int = 3) -> list[str]:
    return [key for key, _ in sorted(weights.items(), key=lambda item: item[1], reverse=True)[:limit]]


def _feature_layer_status(repair_row: Mapping[str, Any], signal_row: Mapping[str, Any]) -> str:
    runtime_gap = str(repair_row.get("runtime_gap_status") or signal_row.get("runtime_gap_status") or "")
    lanes = set(repair_row.get("repair_lanes") or ())
    if runtime_gap == "not_in_current_benchmark":
        return "weight_supported_but_candidate_not_exercised"
    if runtime_gap == "runtime_input_evidence_missing":
        return "weight_supported_but_runtime_input_evidence_missing"
    if runtime_gap == "runtime_bridge_axes_missing":
        if "gate_bridge_axis_alignment" in lanes:
            return "weight_supported_but_gate_axis_not_aligned"
        return "weight_supported_but_feature_fields_missing_or_weak"
    if runtime_gap == "runtime_stage3_gate_blocked":
        return "weight_supported_but_weighted_gate_still_blocks"
    if runtime_gap == "fixture_not_ready":
        return "weight_supported_but_fixture_not_source_backed"
    if not repair_row and not signal_row:
        return "weight_supported_but_no_runtime_audit_row"
    return "weight_supported_runtime_needs_review"


def _plain_explanation(status: str) -> str:
    explanations = {
        "weight_supported_but_candidate_not_exercised": (
            "누적 연구는 weight support에 들어갔지만, current benchmark 후보가 없어 feature/scoring을 실행하지 못했다."
        ),
        "weight_supported_but_runtime_input_evidence_missing": (
            "누적 연구는 weight support에 들어갔지만, runtime 후보의 원천 입력 가족이 부족해 feature bridge를 판정하지 못했다."
        ),
        "weight_supported_but_gate_axis_not_aligned": (
            "누적 연구는 weight support에 들어갔지만, bridge spec과 Green gate required axis가 달라 field가 0점으로 남는다."
        ),
        "weight_supported_but_feature_fields_missing_or_weak": (
            "누적 연구는 weight support에 들어갔지만, parser/feature가 source-backed component field를 충분히 채우지 못했다."
        ),
        "weight_supported_but_weighted_gate_still_blocks": (
            "누적 연구는 weight support에 들어갔고 field도 일부 들어갔지만, weighted Stage3 gate가 아직 막는다."
        ),
        "weight_supported_but_fixture_not_source_backed": (
            "누적 연구는 weight support에는 들어갔지만, exact replay fixture로 쓰기에는 source-backed 입력이 부족하다."
        ),
        "weight_supported_but_no_runtime_audit_row": (
            "weight profile에는 있지만 이번 runtime Green audit 범위에서는 별도 row가 없었다."
        ),
    }
    return explanations.get(status, "weight support와 runtime feature 적용 상태를 추가 점검해야 한다.")


def build_v12_weight_support_runtime_feature_audit(
    *,
    weight_profile_payload: Mapping[str, Any] | None = None,
    repair_board_payload: Mapping[str, Any] | None = None,
    signal_audit_payload: Mapping[str, Any] | None = None,
    field_audit_payload: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Build an audit explaining why research-backed weights do not fill features."""

    profile = dict(weight_profile_payload or _read_json(DEFAULT_WEIGHT_PROFILE_PATH))
    repair_payload = dict(repair_board_payload or _read_json(DEFAULT_REPAIR_BOARD_PATH))
    signal_payload = dict(signal_audit_payload or _read_json(DEFAULT_SIGNAL_AUDIT_PATH))
    field_payload = dict(field_audit_payload or _read_json(DEFAULT_FIELD_AUDIT_PATH))
    repair_by_arch = _rows_by_archetype(repair_payload)
    signal_by_arch = _rows_by_archetype(signal_payload)
    field_by_arch = _rows_by_archetype(field_payload)
    archetype_weights = dict(profile.get("archetype_weights", {}))

    rows: list[dict[str, Any]] = []
    status_counts: Counter[str] = Counter()
    total_support_rows = 0.0
    total_positive_cases = 0.0
    total_counterexamples = 0.0
    for archetype, weight_row in sorted(archetype_weights.items()):
        support = dict(weight_row.get("support") or {})
        weights = _weights(weight_row)
        repair_row = repair_by_arch.get(archetype, {})
        signal_row = signal_by_arch.get(archetype, {})
        field_row = field_by_arch.get(archetype, {})
        status = _feature_layer_status(repair_row, signal_row)
        status_counts[status] += 1
        support_rows = _support_metric(support, "row_count")
        positive_cases = _support_metric(support, "positive_case_count")
        counterexamples = _support_metric(support, "counterexample_count")
        total_support_rows += support_rows
        total_positive_cases += positive_cases
        total_counterexamples += counterexamples
        rows.append(
            {
                "canonical_archetype_id": archetype,
                "weight_profile_present": True,
                "weight_support_row_count": int(support_rows),
                "weight_support_unique_symbol_count": int(_support_metric(support, "unique_symbol_count")),
                "weight_support_positive_case_count": int(positive_cases),
                "weight_support_counterexample_count": int(counterexamples),
                "weights": weights,
                "top_weight_axes": _top_weight_axes(weights),
                "green_policy": str(weight_row.get("green_policy") or ""),
                "feature_layer_status": status,
                "plain_explanation": _plain_explanation(status),
                "primary_repair_lane": repair_row.get("primary_repair_lane"),
                "repair_lanes": list(repair_row.get("repair_lanes") or ()),
                "research_clean_green_count": signal_row.get("research_clean_green_count"),
                "research_raw_stage3_green_count": signal_row.get("research_raw_stage3_green_count"),
                "runtime_gap_status": repair_row.get("runtime_gap_status") or signal_row.get("runtime_gap_status"),
                "runtime_candidate_count": repair_row.get("runtime_candidate_count") or signal_row.get("runtime_candidate_count"),
                "runtime_max_score": repair_row.get("runtime_max_score") or signal_row.get("runtime_max_score"),
                "missing_required_bridge_axes": list(
                    repair_row.get("missing_required_bridge_axes")
                    or signal_row.get("missing_required_bridge_axes")
                    or ()
                ),
                "missing_feature_parser_contract_count": int(
                    field_row.get("missing_feature_parser_contract_count")
                    or repair_row.get("missing_feature_parser_contract_count")
                    or 0
                ),
                "pair_retrospective_ready": bool(repair_row.get("pair_retrospective_ready")),
            }
        )

    rows.sort(
        key=lambda row: (
            row["weight_support_row_count"],
            row["weight_support_positive_case_count"],
            row["research_clean_green_count"] or 0,
        ),
        reverse=True,
    )
    return {
        "summary": {
            "profile_id": profile.get("profile_id"),
            "profile_enabled": bool(profile.get("enabled")),
            "archetype_weight_count": len(archetype_weights),
            "total_archetype_support_rows": int(total_support_rows),
            "total_archetype_positive_cases": int(total_positive_cases),
            "total_archetype_counterexamples": int(total_counterexamples),
            "feature_layer_status_counts": _counter_dict(status_counts),
            "weighted_archetypes_with_no_current_candidate": status_counts[
                "weight_supported_but_candidate_not_exercised"
            ],
            "weighted_archetypes_with_feature_or_gate_gap": sum(
                count
                for status, count in status_counts.items()
                if status
                in {
                    "weight_supported_but_gate_axis_not_aligned",
                    "weight_supported_but_feature_fields_missing_or_weak",
                    "weight_supported_but_runtime_input_evidence_missing",
                    "weight_supported_but_weighted_gate_still_blocks",
                }
            ),
            "top_support_archetypes": [
                {
                    "canonical_archetype_id": row["canonical_archetype_id"],
                    "weight_support_row_count": row["weight_support_row_count"],
                    "feature_layer_status": row["feature_layer_status"],
                }
                for row in rows[:10]
            ],
        },
        "rows": rows,
    }


def render_v12_weight_support_runtime_feature_audit(payload: Mapping[str, Any]) -> str:
    summary = payload.get("summary", {})
    rows = list(payload.get("rows", []))
    lines = [
        "# V12 Weight Support Runtime Feature Audit",
        "",
        "이 문서는 누적 연구가 점수표에 어디까지 반영됐는지 분리한다.",
        "아키타입별 weight profile에는 누적 연구 support가 들어갔지만, 그것만으로 runtime component field가 채워지지는 않는다.",
        "",
        "## Summary",
        "",
        f"- profile_id: `{summary.get('profile_id')}`",
        f"- profile_enabled: `{summary.get('profile_enabled')}`",
        f"- archetype_weight_count: `{summary.get('archetype_weight_count')}`",
        f"- total_archetype_support_rows: `{summary.get('total_archetype_support_rows')}`",
        f"- total_archetype_positive_cases: `{summary.get('total_archetype_positive_cases')}`",
        f"- total_archetype_counterexamples: `{summary.get('total_archetype_counterexamples')}`",
        f"- feature_layer_status_counts: `{summary.get('feature_layer_status_counts')}`",
        f"- weighted_archetypes_with_no_current_candidate: `{summary.get('weighted_archetypes_with_no_current_candidate')}`",
        f"- weighted_archetypes_with_feature_or_gate_gap: `{summary.get('weighted_archetypes_with_feature_or_gate_gap')}`",
        f"- top_support_archetypes: `{summary.get('top_support_archetypes')}`",
        "",
        "## Layer Split",
        "",
        "- Weight layer: 누적 연구가 `EPS/FCF`, `visibility`, `bottleneck` 같은 칸의 배점을 정한다.",
        "- Feature layer: 실제 리포트/공시/뉴스/재무에서 `contract_quality`, `backlog_rpo_visibility`, `approval_to_revenue_bridge` 같은 값을 채운다.",
        "- Gate layer: 채워진 component가 Stage3-Green 문턱을 넘는지 본다.",
        "",
        "## Archetype Rows",
        "",
        "| archetype | weight support | top weight axes | feature layer status | runtime | missing axes | field contract gaps | explanation |",
        "| --- | ---: | --- | --- | --- | --- | ---: | --- |",
    ]
    for row in rows:
        lines.append(
            f"| {row.get('canonical_archetype_id')} | "
            f"{row.get('weight_support_row_count')} rows / {row.get('weight_support_unique_symbol_count')} symbols "
            f"(+{row.get('weight_support_positive_case_count')} / guard {row.get('weight_support_counterexample_count')}) | "
            f"{', '.join(row.get('top_weight_axes') or [])} | "
            f"{row.get('feature_layer_status')} | "
            f"{row.get('runtime_gap_status')} candidates={row.get('runtime_candidate_count')} max={row.get('runtime_max_score')} | "
            f"{', '.join(row.get('missing_required_bridge_axes') or []) or 'none'} | "
            f"{row.get('missing_feature_parser_contract_count')} | "
            f"{row.get('plain_explanation')} |"
        )
    lines.extend(
        [
            "",
            "## Easy Reading",
            "",
            "- 연구자료가 점수표에 아예 안 들어간 것은 아니다. 36개 아키타입 weight profile에는 support row가 들어갔다.",
            "- 하지만 weight는 배점표다. 예를 들어 bottleneck 칸이 19점짜리여도 해당 날짜 입력에서 `backlog`와 `contract` field가 비면 실제 점수는 안 오른다.",
            "- C21 금융은 413 support rows가 weight에는 들어갔지만 current runtime 후보가 0이라 점수식을 아직 실행하지 못했다.",
            "- C06 하닉은 bridge field가 채워진 뒤에도 total/bottleneck gate가 남고, C10 삼성은 customer/backlog/contract bridge가 아직 약하다.",
            "- C01/C19/R13처럼 후보 row의 입력 가족이 약한 경우는 parser를 탓하기 전에 replay 입력부터 보강해야 한다.",
            "- 쉬운 예: 시험에서 수학 배점을 40점으로 바꿔도, 답안지의 수학 답이 빈칸이면 점수는 0점이다. 지금 문제가 그 구조다.",
        ]
    )
    return "\n".join(lines) + "\n"


def write_v12_weight_support_runtime_feature_audit(
    *,
    output_json_path: str | Path = DEFAULT_OUTPUT_JSON_PATH,
    output_md_path: str | Path = DEFAULT_OUTPUT_MD_PATH,
) -> dict[str, Any]:
    payload = build_v12_weight_support_runtime_feature_audit()
    json_path = Path(output_json_path)
    md_path = Path(output_md_path)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    md_path.write_text(render_v12_weight_support_runtime_feature_audit(payload), encoding="utf-8")
    return {"json_path": str(json_path), "md_path": str(md_path), "summary": payload["summary"]}


if __name__ == "__main__":
    result = write_v12_weight_support_runtime_feature_audit()
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
