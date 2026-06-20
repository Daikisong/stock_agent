"""Map the V12 research-to-stage runtime execution path.

This audit is intentionally broader than the HBM/SK Hynix case.  It explains
where accumulated research enters the system, where it can still fail to become
runtime feature values, and which code layer owns each step.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import Any, Mapping
import json


DEFAULT_WEIGHT_AUDIT_PATH = Path("docs/0619/v12_weight_support_runtime_feature_audit_2026-06-19.json")
DEFAULT_REPAIR_BOARD_PATH = Path("docs/0619/v12_runtime_repair_priority_board_2026-06-19.json")
DEFAULT_FIELD_AUDIT_PATH = Path("docs/0619/v12_bridge_spec_runtime_field_audit_2026-06-19.json")
DEFAULT_HBM_TRACE_PATH = Path("docs/0619/v12_hbm_score_loss_trace_2026-06-19.json")
DEFAULT_SIGNAL_AUDIT_PATH = Path("docs/0619/v12_archetype_signal_runtime_translation_audit_2026-06-19.json")
DEFAULT_OUTPUT_JSON_PATH = Path("docs/0619/v12_runtime_execution_path_map_2026-06-19.json")
DEFAULT_OUTPUT_MD_PATH = Path("docs/0619/v12_runtime_execution_path_map_2026-06-19.md")


EXECUTION_LAYERS: tuple[dict[str, Any], ...] = (
    {
        "layer_id": "research_corpus",
        "order": 1,
        "plain_role": "누적 연구 row와 Green/guard 사례를 모은다.",
        "main_inputs": ["data/e2r/calibration/v12/v12_trigger_rows_representative.jsonl"],
        "main_code": [
            "src/e2r/calibration/archetype_weight_profile.py::build_archetype_weight_profile_payload",
        ],
        "main_outputs": ["configs/e2r_archetype_weight_profile_v2_2.json"],
        "can_fill_runtime_feature_fields": False,
        "easy_example": "시험 범위와 배점 근거를 모으는 단계다. 답안지의 실제 답은 아직 쓰지 않는다.",
    },
    {
        "layer_id": "weight_profile",
        "order": 2,
        "plain_role": "아키타입별 7개 component 배점을 정한다.",
        "main_inputs": ["configs/e2r_archetype_weight_profile_v2_2.json"],
        "main_code": [
            "src/e2r/scoring.py::_apply_archetype_runtime_weights",
        ],
        "main_outputs": ["archetype_component_* weighted components"],
        "can_fill_runtime_feature_fields": False,
        "easy_example": "수학 배점을 40점으로 정하는 단계다. 수학 답이 빈칸이면 40점을 받을 수 없다.",
    },
    {
        "layer_id": "candidate_replay_archive",
        "order": 3,
        "plain_role": "Green/guard 사례가 실제 replay 후보와 source-backed 입력으로 들어오는지 확인한다.",
        "main_inputs": [
            "docs/0619/v12_runtime_replay_fixture_spec_2026-06-19.jsonl",
            "local official/search/report archive",
        ],
        "main_code": [
            "src/e2r/backtest/asof_stage_promotion_autopsy.py",
            "src/e2r/pipeline/korea_live_lite.py",
        ],
        "main_outputs": ["runtime candidate rows", "as-of feature inputs"],
        "can_fill_runtime_feature_fields": False,
        "easy_example": "시험을 봐야 점수를 낼 수 있다. 후보가 0개면 채점도 0번이다.",
    },
    {
        "layer_id": "parser_feature_bridge",
        "order": 4,
        "plain_role": "리포트/공시/뉴스/재무 입력을 source-backed runtime field로 구조화한다.",
        "main_inputs": ["research reports", "filings", "news", "financial statements"],
        "main_code": [
            "src/e2r/research/report_parser.py",
            "src/e2r/features.py::DeterministicFeatureEngineer.engineer",
            "src/e2r/features.py::_sector_metrics",
            "src/e2r/features.py::_industrial_sub_scores",
            "src/e2r/features.py::_contract_quality_score",
            "src/e2r/features.py::_backlog_rpo_visibility_score",
        ],
        "main_outputs": [
            "contract_quality",
            "backlog_rpo_visibility",
            "capa_constraint_score",
            "customer_quality_score",
            "ScoringPayload components",
        ],
        "can_fill_runtime_feature_fields": True,
        "easy_example": "답안지에 실제 풀이를 쓰는 단계다. 여기서 빈칸이면 뒤의 배점은 살아 있어도 점수가 안 오른다.",
    },
    {
        "layer_id": "deterministic_score",
        "order": 5,
        "plain_role": "source-backed feature field를 component 점수로 합산한다.",
        "main_inputs": ["ScoringPayload", "archetype weight profile"],
        "main_code": [
            "src/e2r/scoring.py::DeterministicScorer.score",
            "src/e2r/scoring.py::_apply_archetype_runtime_weights",
        ],
        "main_outputs": ["ScoreSnapshot", "weighted component scores"],
        "can_fill_runtime_feature_fields": False,
        "easy_example": "답안지를 채점하는 단계다. 채점자가 빈칸에 임의로 점수를 줄 수 없다.",
    },
    {
        "layer_id": "stage_gate",
        "order": 6,
        "plain_role": "weighted score와 gate 조건으로 Stage 3-Green 여부를 결정한다.",
        "main_inputs": ["ScoreSnapshot", "RedTeamAssessment"],
        "main_code": [
            "src/e2r/staging.py::StageClassifier.classify",
            "src/e2r/staging.py::StageClassifier._is_stage_3_green",
            "src/e2r/stage_gate_diagnostics.py::diagnose_stage_gates",
        ],
        "main_outputs": ["StageSnapshot", "StageGateDiagnostics"],
        "can_fill_runtime_feature_fields": False,
        "easy_example": "총점과 필수 과목 과락을 같이 본다. 총점이 높아도 필수 과목이 비면 Green이 막힌다.",
    },
)


STOP_LAYER_BY_STATUS = {
    "weight_supported_but_candidate_not_exercised": "candidate_replay_archive",
    "weight_supported_but_runtime_input_evidence_missing": "candidate_replay_archive",
    "weight_supported_but_fixture_not_source_backed": "candidate_replay_archive",
    "weight_supported_but_gate_axis_not_aligned": "parser_feature_bridge",
    "weight_supported_but_feature_fields_missing_or_weak": "parser_feature_bridge",
    "weight_supported_but_weighted_gate_still_blocks": "stage_gate",
    "weight_supported_runtime_needs_review": "manual_review",
    "weight_supported_but_no_runtime_audit_row": "manual_review",
}


CODE_OWNERS_BY_LAYER = {
    "candidate_replay_archive": [
        "src/e2r/backtest/asof_stage_promotion_autopsy.py",
        "src/e2r/pipeline/korea_live_lite.py",
    ],
    "parser_feature_bridge": [
        "src/e2r/research/report_parser.py",
        "src/e2r/features.py::DeterministicFeatureEngineer.engineer",
        "src/e2r/features.py::_contract_quality_score",
        "src/e2r/features.py::_backlog_rpo_visibility_score",
    ],
    "stage_gate": [
        "src/e2r/scoring.py::_apply_archetype_runtime_weights",
        "src/e2r/staging.py::StageClassifier._is_stage_3_green",
        "src/e2r/stage_gate_diagnostics.py::diagnose_stage_gates",
    ],
    "manual_review": ["docs/0619 runtime audit outputs"],
}


NEXT_FIX_BY_LAYER = {
    "candidate_replay_archive": (
        "Green/guard fixture를 local official/search/report archive와 exact symbol+date replay 후보로 고정한다."
    ),
    "parser_feature_bridge": (
        "아키타입별 연구축을 parser output, feature field, gate required axis가 같은 이름/의미로 읽게 맞춘다."
    ),
    "stage_gate": (
        "source-backed field가 들어온 뒤에도 Green이 막히는지 weighted gate threshold와 component balance를 검증한다."
    ),
    "manual_review": "현재 audit 범위 밖이므로 후보/field/gate 중 어느 층인지 추가 trace가 필요하다.",
}


FOCUS_ARCHETYPES = (
    "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
    "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE",
    "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
    "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION",
    "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE",
    "C02_POWER_GRID_DATACENTER_CAPEX",
)


def _read_json(path: str | Path) -> dict[str, Any]:
    path_obj = Path(path)
    if not path_obj.exists():
        return {}
    return json.loads(path_obj.read_text(encoding="utf-8"))


def _rows_by_archetype(payload: Mapping[str, Any]) -> dict[str, dict[str, Any]]:
    return {str(row.get("canonical_archetype_id")): dict(row) for row in payload.get("rows", [])}


def _status_stop_layer(status: str) -> str:
    return STOP_LAYER_BY_STATUS.get(status, "manual_review")


def _counter_dict(counter: Counter[str]) -> dict[str, int]:
    return dict(sorted(counter.items()))


def _case_label(archetype: str) -> str:
    if archetype == "C06_HBM_MEMORY_CUSTOMER_CAPACITY":
        return "하닉 HBM 예시이지만 HBM 특례가 아니라 bridge 이후 gate 검증까지 보는 문제"
    if archetype == "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE":
        return "삼성전자 memory recovery route 예시"
    if archetype == "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN":
        return "금융 capital return 후보/replay gap 예시"
    if archetype == "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION":
        return "바이오 approval-to-revenue 후보/replay gap 예시"
    if archetype == "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE":
        return "플랫폼 광고/레버리지 후보/replay gap과 field contract 후속 예시"
    if archetype == "C02_POWER_GRID_DATACENTER_CAPEX":
        return "field가 일부 있어도 weighted gate가 막는 예시"
    return "전 아키타입 공통 점검 대상"


def _plain_runtime_reason(row: Mapping[str, Any], repair_row: Mapping[str, Any]) -> str:
    status = str(row.get("feature_layer_status") or "")
    missing_axes = list(row.get("missing_required_bridge_axes") or repair_row.get("missing_required_bridge_axes") or ())
    candidate_count = row.get("runtime_candidate_count")
    if status == "weight_supported_but_candidate_not_exercised":
        return f"weight support는 있지만 current runtime 후보가 {candidate_count or 0}개라 feature/scoring을 실행하지 못했다."
    if status == "weight_supported_but_runtime_input_evidence_missing":
        return "후보는 있지만 리포트/뉴스/컨센서스/충분한 공시+재무 입력 가족이 부족해 bridge field를 판정하지 못한다."
    if status == "weight_supported_but_gate_axis_not_aligned":
        return f"후보는 들어왔지만 required axis {missing_axes or ['unknown']}가 bridge/spec/feature에서 맞지 않아 Green gate가 막힌다."
    if status == "weight_supported_but_feature_fields_missing_or_weak":
        return "후보는 들어왔지만 parser/feature field가 source-backed component 값을 충분히 만들지 못한다."
    if status == "weight_supported_but_weighted_gate_still_blocks":
        return "field는 일부 들어왔지만 weighted Stage3-Green 문턱에서 아직 부족하다."
    if status == "weight_supported_but_fixture_not_source_backed":
        return "research Green은 있지만 replay fixture로 쓰기 위한 source-backed 입력이 부족하다."
    return "현재 audit만으로는 중단 지점 추가 확인이 필요하다."


def _build_path_rows(
    weight_rows: Mapping[str, dict[str, Any]],
    repair_rows: Mapping[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for archetype, row in sorted(weight_rows.items()):
        repair_row = repair_rows.get(archetype, {})
        status = str(row.get("feature_layer_status") or "weight_supported_runtime_needs_review")
        stop_layer = _status_stop_layer(status)
        rows.append(
            {
                "canonical_archetype_id": archetype,
                "case_label": _case_label(archetype),
                "weight_support_row_count": int(row.get("weight_support_row_count") or 0),
                "weight_support_positive_case_count": int(row.get("weight_support_positive_case_count") or 0),
                "weight_support_counterexample_count": int(row.get("weight_support_counterexample_count") or 0),
                "top_weight_axes": list(row.get("top_weight_axes") or ()),
                "feature_layer_status": status,
                "runtime_gap_status": row.get("runtime_gap_status") or repair_row.get("runtime_gap_status"),
                "runtime_candidate_count": row.get("runtime_candidate_count") or repair_row.get("runtime_candidate_count"),
                "runtime_max_score": row.get("runtime_max_score") or repair_row.get("runtime_max_score"),
                "missing_required_bridge_axes": list(
                    row.get("missing_required_bridge_axes")
                    or repair_row.get("missing_required_bridge_axes")
                    or ()
                ),
                "missing_feature_parser_contract_count": int(
                    row.get("missing_feature_parser_contract_count")
                    or repair_row.get("missing_feature_parser_contract_count")
                    or 0
                ),
                "stop_layer": stop_layer,
                "code_owners": list(CODE_OWNERS_BY_LAYER.get(stop_layer, CODE_OWNERS_BY_LAYER["manual_review"])),
                "next_fix": NEXT_FIX_BY_LAYER.get(stop_layer, NEXT_FIX_BY_LAYER["manual_review"]),
                "plain_runtime_reason": _plain_runtime_reason(row, repair_row),
            }
        )
    rows.sort(
        key=lambda item: (
            item["stop_layer"],
            -item["weight_support_row_count"],
            item["canonical_archetype_id"],
        )
    )
    return rows


def build_v12_runtime_execution_path_map(
    *,
    weight_audit_payload: Mapping[str, Any] | None = None,
    repair_board_payload: Mapping[str, Any] | None = None,
    field_audit_payload: Mapping[str, Any] | None = None,
    hbm_trace_payload: Mapping[str, Any] | None = None,
    signal_audit_payload: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Build the cross-archetype runtime path map from existing audits."""

    weight_payload = dict(weight_audit_payload or _read_json(DEFAULT_WEIGHT_AUDIT_PATH))
    repair_payload = dict(repair_board_payload or _read_json(DEFAULT_REPAIR_BOARD_PATH))
    field_payload = dict(field_audit_payload or _read_json(DEFAULT_FIELD_AUDIT_PATH))
    hbm_payload = dict(hbm_trace_payload or _read_json(DEFAULT_HBM_TRACE_PATH))
    signal_payload = dict(signal_audit_payload or _read_json(DEFAULT_SIGNAL_AUDIT_PATH))

    weight_rows = _rows_by_archetype(weight_payload)
    repair_rows = _rows_by_archetype(repair_payload)
    path_rows = _build_path_rows(weight_rows, repair_rows)
    stop_layer_counts = Counter(row["stop_layer"] for row in path_rows)
    focus_rows = [row for row in path_rows if row["canonical_archetype_id"] in FOCUS_ARCHETYPES]
    summary = {
        "execution_layer_count": len(EXECUTION_LAYERS),
        "archetype_path_row_count": len(path_rows),
        "research_support_rows": weight_payload.get("summary", {}).get("total_archetype_support_rows"),
        "research_positive_cases": weight_payload.get("summary", {}).get("total_archetype_positive_cases"),
        "research_counterexamples": weight_payload.get("summary", {}).get("total_archetype_counterexamples"),
        "archetype_weight_count": weight_payload.get("summary", {}).get("archetype_weight_count"),
        "feature_layer_status_counts": weight_payload.get("summary", {}).get("feature_layer_status_counts", {}),
        "stop_layer_counts": _counter_dict(stop_layer_counts),
        "repair_lane_counts": repair_payload.get("summary", {}).get("repair_lane_counts", {}),
        "primitive_support_status_counts": field_payload.get("summary", {}).get("primitive_support_status_counts", {}),
        "runtime_gap_status_counts": signal_payload.get("runtime_gap_status_counts", {}),
        "hbm_case_scores": {
            "sk_hynix_max_score": hbm_payload.get("summary", {}).get("sk_hynix_max_score"),
            "samsung_max_score": hbm_payload.get("summary", {}).get("samsung_max_score"),
            "sk_hynix_common_loss": hbm_payload.get("summary", {}).get("sk_hynix_common_loss"),
            "samsung_common_loss": hbm_payload.get("summary", {}).get("samsung_common_loss"),
        },
        "main_conclusion": (
            "누적 연구는 weight profile까지 반영됐지만, runtime feature/candidate/gate layer가 "
            "각 아키타입의 source-backed 증거를 아직 충분히 점수 field로 번역하지 못한다."
        ),
    }
    return {
        "schema_version": "v12_runtime_execution_path_map_v1",
        "summary": summary,
        "execution_layers": list(EXECUTION_LAYERS),
        "focus_rows": focus_rows,
        "archetype_rows": path_rows,
    }


def render_v12_runtime_execution_path_map(payload: Mapping[str, Any]) -> str:
    summary = payload.get("summary", {})
    layers = list(payload.get("execution_layers", []))
    focus_rows = list(payload.get("focus_rows", []))
    archetype_rows = list(payload.get("archetype_rows", []))
    lines = [
        "# V12 Runtime Execution Path Map",
        "",
        "이 문서는 삼전/하닉을 HBM 특례로 올리기 위한 문서가 아니다.",
        "삼전/하닉에서 보인 낮은 점수를 예시로 삼아, 전체 아키타입에서 연구가 실제 runtime 점수로 바뀌는 경로를 분해한다.",
        "",
        "## Short Answer",
        "",
        f"- main_conclusion: {summary.get('main_conclusion')}",
        f"- research_support_rows: `{summary.get('research_support_rows')}`",
        f"- research_positive_cases: `{summary.get('research_positive_cases')}`",
        f"- research_counterexamples: `{summary.get('research_counterexamples')}`",
        f"- archetype_weight_count: `{summary.get('archetype_weight_count')}`",
        f"- feature_layer_status_counts: `{summary.get('feature_layer_status_counts')}`",
        f"- stop_layer_counts: `{summary.get('stop_layer_counts')}`",
        f"- repair_lane_counts: `{summary.get('repair_lane_counts')}`",
        f"- primitive_support_status_counts: `{summary.get('primitive_support_status_counts')}`",
        f"- hbm_case_scores: `{summary.get('hbm_case_scores')}`",
        "",
        "## Execution Path",
        "",
        "| order | layer | role | key code | output | can fill feature fields | easy example |",
        "| ---: | --- | --- | --- | --- | --- | --- |",
    ]
    for layer in sorted(layers, key=lambda item: item.get("order", 0)):
        lines.append(
            f"| {layer.get('order')} | {layer.get('layer_id')} | {layer.get('plain_role')} | "
            f"{'<br>'.join(layer.get('main_code') or [])} | "
            f"{'<br>'.join(layer.get('main_outputs') or [])} | "
            f"{layer.get('can_fill_runtime_feature_fields')} | {layer.get('easy_example')} |"
        )

    lines.extend(
        [
            "",
            "## Focus Examples",
            "",
            "| archetype | why this matters | weight support | top weight axes | runtime status | stop layer | missing axes | code owners | next fix |",
            "| --- | --- | ---: | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for row in sorted(focus_rows, key=lambda item: item.get("canonical_archetype_id", "")):
        lines.append(
            f"| {row.get('canonical_archetype_id')} | {row.get('case_label')} | "
            f"{row.get('weight_support_row_count')} rows "
            f"(+{row.get('weight_support_positive_case_count')} / guard {row.get('weight_support_counterexample_count')}) | "
            f"{', '.join(row.get('top_weight_axes') or [])} | "
            f"{row.get('plain_runtime_reason')} | {row.get('stop_layer')} | "
            f"{', '.join(row.get('missing_required_bridge_axes') or []) or 'none'} | "
            f"{'<br>'.join(row.get('code_owners') or [])} | {row.get('next_fix')} |"
        )

    lines.extend(
        [
            "",
            "## All Archetype Stop Layers",
            "",
            "| archetype | support rows | feature status | runtime gap | stop layer | runtime candidates | max score | missing axes |",
            "| --- | ---: | --- | --- | --- | ---: | ---: | --- |",
        ]
    )
    for row in archetype_rows:
        lines.append(
            f"| {row.get('canonical_archetype_id')} | {row.get('weight_support_row_count')} | "
            f"{row.get('feature_layer_status')} | {row.get('runtime_gap_status')} | {row.get('stop_layer')} | "
            f"{row.get('runtime_candidate_count')} | {row.get('runtime_max_score')} | "
            f"{', '.join(row.get('missing_required_bridge_axes') or []) or 'none'} |"
        )

    lines.extend(
        [
            "",
            "## Easy Reading",
            "",
            "- 연구자료 누적은 배점표를 만드는 데 쓰였다. 이것은 `weight_profile` layer다.",
            "- 실제 점수는 답안지에 해당하는 runtime field가 채워져야 올라간다. 이것은 `parser_feature_bridge` layer다.",
            "- 하닉 예시는 `capacity lock`, `customer allocation`, `contract/order` 같은 신호가 field로 채워진 뒤에도 weighted gate까지 검증해야 함을 보여준다.",
            "- 삼성/C10 예시는 후보와 리포트가 있어도 customer/backlog/contract bridge가 약하면 Stage2에 남는다는 점을 보여준다.",
            "- C01/C19/R13 예시는 후보 row가 있어도 원천 입력 가족이 부족하면 parser-feature 실패로 단정하면 안 된다는 점을 보여준다.",
            "- C21 같은 비-HBM 예시는 연구와 weight는 있는데 current runtime 후보가 0개라 채점 자체를 못 한 경우다.",
            "- 쉬운 예: 시험 배점을 수학 40점으로 바꿔도, 학생 답안지의 수학 풀이가 빈칸이면 40점은 자동으로 들어오지 않는다.",
        ]
    )
    return "\n".join(lines) + "\n"


def write_v12_runtime_execution_path_map(
    *,
    output_json_path: str | Path = DEFAULT_OUTPUT_JSON_PATH,
    output_md_path: str | Path = DEFAULT_OUTPUT_MD_PATH,
) -> dict[str, Any]:
    payload = build_v12_runtime_execution_path_map()
    json_path = Path(output_json_path)
    md_path = Path(output_md_path)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    md_path.write_text(render_v12_runtime_execution_path_map(payload), encoding="utf-8")
    return {"json_path": str(json_path), "md_path": str(md_path), "summary": payload["summary"]}


if __name__ == "__main__":
    result = write_v12_runtime_execution_path_map()
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
