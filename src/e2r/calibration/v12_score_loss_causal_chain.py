"""Build a causal chain for why accumulated Green research still scores low."""

from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import Any, Mapping
import json


DEFAULT_HBM_SIGNAL_PATH = Path("docs/0619/v12_hbm_research_signal_translation_audit_2026-06-19.json")
DEFAULT_ARCHETYPE_SIGNAL_PATH = Path("docs/0619/v12_archetype_signal_runtime_translation_audit_2026-06-19.json")
DEFAULT_WEIGHT_AUDIT_PATH = Path("docs/0619/v12_weight_support_runtime_feature_audit_2026-06-19.json")
DEFAULT_EXECUTION_PATH_MAP_PATH = Path("docs/0619/v12_runtime_execution_path_map_2026-06-19.json")
DEFAULT_INPUT_GAP_MANIFEST_PATH = Path("docs/0619/v12_runtime_first_repair_input_gap_manifest_2026-06-19.json")
DEFAULT_OUTPUT_JSON_PATH = Path("docs/0619/v12_score_loss_causal_chain_2026-06-19.json")
DEFAULT_OUTPUT_MD_PATH = Path("docs/0619/v12_score_loss_causal_chain_2026-06-19.md")


FOCUS_ARCHETYPES = (
    "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
    "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE",
    "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
    "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION",
    "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE",
    "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION",
    "C02_POWER_GRID_DATACENTER_CAPEX",
)


RUNTIME_SCORE_FIELDS = (
    "current_stage",
    "current_score",
    "canonical_archetype_id",
    "sector_profile",
    "archetype_component_eps_fcf_explosion",
    "archetype_component_earnings_visibility",
    "archetype_component_bottleneck_pricing",
    "archetype_component_market_mispricing",
    "archetype_component_valuation_rerating",
    "archetype_component_information_confidence",
    "revision_score",
    "contract_quality",
    "backlog_rpo_visibility",
    "capa_constraint",
    "research_axis_bridge_margin",
    "research_axis_bridge_customer",
    "research_axis_bridge_backlog",
    "research_axis_bridge_contract",
    "research_axis_bridge_valuation_repricing",
    "green_gate_deficit_summary",
)


def _read_json(path: str | Path) -> dict[str, Any]:
    path_obj = Path(path)
    if not path_obj.exists():
        return {}
    return json.loads(path_obj.read_text(encoding="utf-8"))


def _counter_dict(counter: Counter[str]) -> dict[str, int]:
    return dict(sorted(counter.items()))


def _rows_by_archetype(payload: Mapping[str, Any], key: str = "rows") -> dict[str, dict[str, Any]]:
    return {str(row.get("canonical_archetype_id")): dict(row) for row in payload.get(key, []) or []}


def _manifest_by_archetype(payload: Mapping[str, Any]) -> dict[str, dict[str, Any]]:
    return _rows_by_archetype(payload)


def _runtime_view(runtime_row: Mapping[str, Any] | None) -> dict[str, Any] | None:
    if not runtime_row:
        return None
    return {field: runtime_row.get(field) for field in RUNTIME_SCORE_FIELDS}


def _runtime_bridge_zero_fields(runtime_row: Mapping[str, Any] | None) -> list[str]:
    if not runtime_row:
        return []
    zero_fields = []
    for field in (
        "research_axis_bridge_customer",
        "research_axis_bridge_backlog",
        "research_axis_bridge_contract",
        "contract_quality",
        "backlog_rpo_visibility",
        "capa_constraint",
    ):
        value = runtime_row.get(field)
        try:
            if float(str(value)) == 0.0:
                zero_fields.append(field)
        except (TypeError, ValueError):
            continue
    return zero_fields


def _plain_symbol_answer(symbol_row: Mapping[str, Any]) -> str:
    symbol = str(symbol_row.get("symbol") or "")
    runtime = symbol_row.get("runtime_best_row") or {}
    deficit = runtime.get("green_gate_deficit_summary") or "no runtime deficit"
    if symbol == "000660":
        return (
            "하닉은 EPS/revision이 깎인 것이 아니다. runtime best row가 revision, margin, customer/backlog/contract를 강하게 잡은 뒤에도 "
            f"Green gate가 `{deficit}`에서 막힌다."
        )
    if symbol == "005930":
        return (
            "삼성은 누적 HBM 장부에서도 direct C06 Green보다 qualification lag/catch-up 성격이 강하다. "
            "runtime은 C10 memory recovery route로 남고 customer/backlog/contract가 0이라 "
            f"Stage 2와 `{deficit}`에 머문다."
        )
    return "runtime field와 Green gate deficit을 확인해야 한다."


def _hbm_symbol_chain(symbol_row: Mapping[str, Any]) -> dict[str, Any]:
    runtime = symbol_row.get("runtime_best_row") or {}
    zero_fields = _runtime_bridge_zero_fields(runtime)
    return {
        "symbol": symbol_row.get("symbol"),
        "company_label": symbol_row.get("company_label"),
        "research_hbm_row_count": symbol_row.get("research_hbm_row_count", 0),
        "research_raw_stage3_green_count": symbol_row.get("research_raw_stage3_green_count", 0),
        "research_positive_or_green_worthy_count": symbol_row.get("research_positive_or_green_worthy_count", 0),
        "positive_signal_counts": dict(symbol_row.get("positive_signal_counts") or {}),
        "gap_signals": list(symbol_row.get("gap_signals") or ()),
        "runtime_best_row": _runtime_view(runtime),
        "runtime_zero_or_missing_bridge_fields": zero_fields,
        "plain_answer": _plain_symbol_answer(symbol_row),
        "causal_chain": [
            "누적 연구 row와 positive/Green-worthy 사례는 존재한다.",
            "아키타입 weight layer에는 이미 반영됐지만, weight는 배점표일 뿐 runtime field를 채우지 않는다.",
            "runtime best row에서 source-backed bridge field가 0이면 score/stage gate는 해당 증거를 없는 것으로 본다.",
            "따라서 해결은 이름 보너스가 아니라 research signal -> parser field -> feature field -> gate axis 연결이다.",
        ],
    }


def _status_to_plain(stop_layer: str, row: Mapping[str, Any]) -> str:
    missing_axes = list(row.get("missing_required_bridge_axes") or ())
    if stop_layer == "candidate_replay_archive":
        return "연구 Green은 있지만 시험지가 current replay에 없다. 점수가 낮은 게 아니라 아직 채점 자체를 못 했다."
    if stop_layer == "parser_feature_bridge":
        return f"후보는 들어왔지만 {missing_axes or ['required axis']}가 runtime field/gate에서 비어 Green 점수로 못 올라간다."
    if stop_layer == "stage_gate":
        return "source-backed field가 일부 들어왔지만 weighted Stage3-Green 총점/과락 gate에서 막힌다."
    return "현재 장부만으로는 후보, field, gate 중 어디인지 추가 분류가 필요하다."


def _archetype_chain_row(
    *,
    archetype: str,
    signal_row: Mapping[str, Any],
    weight_row: Mapping[str, Any],
    execution_row: Mapping[str, Any],
    manifest_row: Mapping[str, Any],
) -> dict[str, Any]:
    stop_layer = str(execution_row.get("stop_layer") or "manual_review")
    runtime_best = signal_row.get("runtime_best_row")
    return {
        "canonical_archetype_id": archetype,
        "case_label": execution_row.get("case_label"),
        "research_clean_green_count": signal_row.get("research_clean_green_count", 0),
        "research_raw_stage3_green_count": signal_row.get("research_raw_stage3_green_count", 0),
        "research_axis_signal_counts": dict(signal_row.get("research_axis_signal_counts") or {}),
        "weight_support_row_count": weight_row.get("weight_support_row_count", execution_row.get("weight_support_row_count", 0)),
        "weight_support_positive_case_count": weight_row.get(
            "weight_support_positive_case_count", execution_row.get("weight_support_positive_case_count", 0)
        ),
        "weight_support_counterexample_count": weight_row.get(
            "weight_support_counterexample_count", execution_row.get("weight_support_counterexample_count", 0)
        ),
        "top_weight_axes": list(weight_row.get("top_weight_axes") or execution_row.get("top_weight_axes") or ()),
        "runtime_gap_status": signal_row.get("runtime_gap_status") or execution_row.get("runtime_gap_status"),
        "runtime_candidate_count": signal_row.get("runtime_candidate_count", execution_row.get("runtime_candidate_count", 0)),
        "runtime_max_score": signal_row.get("runtime_max_score", execution_row.get("runtime_max_score")),
        "diagnosis": signal_row.get("diagnosis"),
        "stop_layer": stop_layer,
        "missing_required_bridge_axes": list(
            signal_row.get("missing_required_bridge_axes") or execution_row.get("missing_required_bridge_axes") or ()
        ),
        "runtime_best_row": _runtime_view(runtime_best),
        "runtime_zero_or_missing_bridge_fields": _runtime_bridge_zero_fields(runtime_best),
        "first_slice_role_gap_classes": list(manifest_row.get("role_gap_classes") or ()),
        "next_fix": execution_row.get("next_fix"),
        "code_owners": list(execution_row.get("code_owners") or ()),
        "plain_failure": _status_to_plain(stop_layer, signal_row or execution_row),
    }


def build_v12_score_loss_causal_chain(
    *,
    hbm_signal_payload: Mapping[str, Any] | None = None,
    archetype_signal_payload: Mapping[str, Any] | None = None,
    weight_audit_payload: Mapping[str, Any] | None = None,
    execution_path_payload: Mapping[str, Any] | None = None,
    input_gap_manifest_payload: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Join existing audits into a direct score-loss causal chain."""

    hbm_signal = dict(hbm_signal_payload or _read_json(DEFAULT_HBM_SIGNAL_PATH))
    archetype_signal = dict(archetype_signal_payload or _read_json(DEFAULT_ARCHETYPE_SIGNAL_PATH))
    weight_audit = dict(weight_audit_payload or _read_json(DEFAULT_WEIGHT_AUDIT_PATH))
    execution_path = dict(execution_path_payload or _read_json(DEFAULT_EXECUTION_PATH_MAP_PATH))
    input_manifest = dict(input_gap_manifest_payload or _read_json(DEFAULT_INPUT_GAP_MANIFEST_PATH))

    signal_by_arch = _rows_by_archetype(archetype_signal)
    weight_by_arch = _rows_by_archetype(weight_audit)
    execution_by_arch = _rows_by_archetype(execution_path, key="archetype_rows")
    manifest_by_arch = _manifest_by_archetype(input_manifest)

    hbm_symbol_rows = [_hbm_symbol_chain(row) for row in hbm_signal.get("symbol_rows", []) or []]
    focus_rows = []
    for archetype in FOCUS_ARCHETYPES:
        focus_rows.append(
            _archetype_chain_row(
                archetype=archetype,
                signal_row=signal_by_arch.get(archetype, {}),
                weight_row=weight_by_arch.get(archetype, {}),
                execution_row=execution_by_arch.get(archetype, {}),
                manifest_row=manifest_by_arch.get(archetype, {}),
            )
        )

    stop_layer_counts = Counter(str(row.get("stop_layer") or "manual_review") for row in execution_by_arch.values())
    return {
        "schema_version": "v12_score_loss_causal_chain_v1",
        "summary": {
            "plain_answer": (
                "점수표가 누적 연구를 잊은 것이 아니다. 누적 연구는 weight layer까지 들어갔지만, "
                "current pipeline은 candidate/archive, parser-feature bridge, stage gate 중 하나에서 멈춘다."
            ),
            "research_support_rows": (execution_path.get("summary") or {}).get("research_support_rows"),
            "research_positive_cases": (execution_path.get("summary") or {}).get("research_positive_cases"),
            "research_counterexamples": (execution_path.get("summary") or {}).get("research_counterexamples"),
            "archetype_weight_count": (execution_path.get("summary") or {}).get("archetype_weight_count"),
            "stop_layer_counts": _counter_dict(stop_layer_counts),
            "runtime_gap_status_counts": (execution_path.get("summary") or {}).get("runtime_gap_status_counts", {}),
            "hbm_generalization_guard": (
                "삼전/하닉은 대표 테스트 케이스다. HBM만 통과시키는 패치는 실패이며, "
                "비-HBM focus rows도 같은 chain에서 통과해야 한다."
            ),
            "first_slice_input_gap_counts": (input_manifest.get("summary") or {}).get("role_gap_class_counts", {}),
        },
        "hbm_symbol_rows": hbm_symbol_rows,
        "focus_archetype_rows": focus_rows,
    }


def _fmt(value: Any) -> str:
    if value is None:
        return ""
    return str(value)


def _join(values: list[Any]) -> str:
    return ", ".join(str(value) for value in values if str(value)) or "none"


def _runtime_short(row: Mapping[str, Any] | None) -> str:
    if not row:
        return "not scored"
    return "{stage}/{score}/{arch}; bridge m,c,b,k={margin}/{customer}/{backlog}/{contract}; deficit={deficit}".format(
        stage=row.get("current_stage"),
        score=row.get("current_score"),
        arch=row.get("canonical_archetype_id"),
        margin=row.get("research_axis_bridge_margin"),
        customer=row.get("research_axis_bridge_customer"),
        backlog=row.get("research_axis_bridge_backlog"),
        contract=row.get("research_axis_bridge_contract"),
        deficit=row.get("green_gate_deficit_summary"),
    )


def render_v12_score_loss_causal_chain(payload: Mapping[str, Any]) -> str:
    summary = payload.get("summary", {})
    lines = [
        "# V12 Score Loss Causal Chain",
        "",
        "이 문서는 '삼전/하닉이 왜 이렇게 낮게 나오나'를 전체 아키타입 문제로 연결해 설명한다.",
        "점수식을 바꾸는 문서가 아니라, 기존 0619 audit들을 합쳐 점수 손실 위치를 한 화면에 고정하는 장부다.",
        "",
        "## Summary",
        "",
        f"- plain_answer: {summary.get('plain_answer')}",
        f"- research_support_rows: `{summary.get('research_support_rows')}`",
        f"- research_positive_cases: `{summary.get('research_positive_cases')}`",
        f"- research_counterexamples: `{summary.get('research_counterexamples')}`",
        f"- archetype_weight_count: `{summary.get('archetype_weight_count')}`",
        f"- stop_layer_counts: `{summary.get('stop_layer_counts')}`",
        f"- runtime_gap_status_counts: `{summary.get('runtime_gap_status_counts')}`",
        f"- first_slice_input_gap_counts: `{summary.get('first_slice_input_gap_counts')}`",
        f"- hbm_generalization_guard: {summary.get('hbm_generalization_guard')}",
        "",
        "## HBM Symbol Chain",
        "",
        "| symbol | research HBM/raw Green/positive | positive signals | runtime best | zero/missing bridge fields | gap signals | answer |",
        "| --- | ---: | --- | --- | --- | --- | --- |",
    ]
    for row in payload.get("hbm_symbol_rows", []) or []:
        counts = "{}/{}/{}".format(
            row.get("research_hbm_row_count", 0),
            row.get("research_raw_stage3_green_count", 0),
            row.get("research_positive_or_green_worthy_count", 0),
        )
        lines.append(
            "| {symbol} {label} | {counts} | {signals} | {runtime} | {zero} | {gaps} | {answer} |".format(
                symbol=row.get("symbol"),
                label=row.get("company_label"),
                counts=counts,
                signals=row.get("positive_signal_counts"),
                runtime=_runtime_short(row.get("runtime_best_row")),
                zero=_join(row.get("runtime_zero_or_missing_bridge_fields") or []),
                gaps=_join(row.get("gap_signals") or []),
                answer=row.get("plain_answer"),
            )
        )
    lines.extend(
        [
            "",
            "## Focus Archetype Chain",
            "",
            "| archetype | research Green clean/raw | weight support/positive/guard | stop layer | runtime | missing axes | first-slice input gaps | plain failure | next fix |",
            "| --- | ---: | ---: | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for row in payload.get("focus_archetype_rows", []) or []:
        green_counts = f"{row.get('research_clean_green_count', 0)}/{row.get('research_raw_stage3_green_count', 0)}"
        weight_counts = "{}/{}/{}".format(
            row.get("weight_support_row_count", 0),
            row.get("weight_support_positive_case_count", 0),
            row.get("weight_support_counterexample_count", 0),
        )
        lines.append(
            "| {arch} | {green} | {weight} | {layer} | {runtime} | {missing} | {input_gaps} | {failure} | {next_fix} |".format(
                arch=row.get("canonical_archetype_id"),
                green=green_counts,
                weight=weight_counts,
                layer=row.get("stop_layer"),
                runtime=_runtime_short(row.get("runtime_best_row")),
                missing=_join(row.get("missing_required_bridge_axes") or []),
                input_gaps=_join(row.get("first_slice_role_gap_classes") or []),
                failure=row.get("plain_failure"),
                next_fix=row.get("next_fix"),
            )
        )
    lines.extend(
        [
            "",
            "## Easy Reading",
            "",
            "- 하닉 예: 연구에는 HBM sold-out/customer allocation이 있고, weight와 bridge field에도 반영됐다. 이제 남은 것은 total/bottleneck gate 검증이다.",
            "- 삼성 예: 삼성은 같은 C06 direct Green이 아니라 C10 memory recovery/catch-up route로 잡힌다. customer/backlog/contract bridge가 약해 Stage 2에 남는다.",
            "- C01/C19/R13 예: 후보 row는 있지만 원천 입력 가족이 부족하면 parser 실패인지 아직 판정할 수 없다.",
            "- C21/C23/C26 예: 연구 Green은 있지만 current replay 후보가 0개다. 시험지가 없으니 채점표를 아무리 잘 만들어도 점수가 안 나온다.",
            "- C02 예: 후보와 field가 있어도 Green gate 총점/필수축에서 막힐 수 있다. 이 경우에는 threshold/component balance를 positive/guard 쌍으로 검증해야 한다.",
            "- 결론: 점수표 문제 하나가 아니라 `후보 입력`, `field 번역`, `gate 검증` 세 층의 문제다. 하닉/삼전만 좋아지는 패치는 실패다.",
        ]
    )
    return "\n".join(lines) + "\n"


def write_v12_score_loss_causal_chain(
    *,
    output_json_path: str | Path = DEFAULT_OUTPUT_JSON_PATH,
    output_md_path: str | Path = DEFAULT_OUTPUT_MD_PATH,
) -> dict[str, Any]:
    payload = build_v12_score_loss_causal_chain()
    json_path = Path(output_json_path)
    md_path = Path(output_md_path)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    md_path.write_text(render_v12_score_loss_causal_chain(payload), encoding="utf-8")
    return {"json_path": str(json_path), "md_path": str(md_path), "summary": payload["summary"]}


if __name__ == "__main__":
    result = write_v12_score_loss_causal_chain()
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
