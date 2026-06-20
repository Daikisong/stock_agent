"""Audit whether the 0619 investigation covers the user's original scope."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Mapping
import json


DEFAULT_COMPONENT_WATERFALL_PATH = Path("docs/0619/v12_component_score_loss_waterfall_2026-06-19.json")
DEFAULT_HISTORICAL_LEDGER_PATH = Path("docs/0619/v12_historical_green_case_runtime_translation_ledger_2026-06-19.json")
DEFAULT_CURRENT_CENSUS_PATH = Path("docs/0619/v12_current_runtime_field_failure_census_2026-06-19.json")
DEFAULT_WEIGHT_AUDIT_PATH = Path("docs/0619/v12_weight_support_runtime_feature_audit_2026-06-19.json")
DEFAULT_EXECUTION_PATH_PATH = Path("docs/0619/v12_runtime_execution_path_map_2026-06-19.json")
DEFAULT_CROSS_TRACE_PATH = Path("docs/0619/v12_cross_archetype_score_loss_trace_2026-06-19.json")
DEFAULT_AXIS_CONTRACT_PATH = Path("docs/0619/v12_green_score_axis_runtime_contract_audit_2026-06-19.json")
DEFAULT_ACCEPTANCE_SPEC_PATH = Path("docs/0619/v12_runtime_repair_acceptance_spec_2026-06-19.json")
DEFAULT_OUTPUT_JSON_PATH = Path("docs/0619/v12_goal_scope_evidence_audit_2026-06-19.json")
DEFAULT_OUTPUT_MD_PATH = Path("docs/0619/v12_goal_scope_evidence_audit_2026-06-19.md")


def _read_json(path: str | Path) -> dict[str, Any]:
    path_obj = Path(path)
    if not path_obj.exists():
        return {}
    return json.loads(path_obj.read_text(encoding="utf-8"))


def _summary(payload: Mapping[str, Any]) -> Mapping[str, Any]:
    summary = payload.get("summary")
    return summary if isinstance(summary, Mapping) else {}


def _focus_by_symbol(component_payload: Mapping[str, Any]) -> dict[str, Mapping[str, Any]]:
    return {
        str(row.get("symbol") or ""): row
        for row in component_payload.get("focus_rows", [])
        if row.get("symbol")
    }


def _component_loss(row: Mapping[str, Any], component: str) -> float | None:
    for item in row.get("components", []) or []:
        if item.get("component") == component:
            value = item.get("loss_points")
            return float(value) if value is not None else None
    return None


def _top_global_losses(component_payload: Mapping[str, Any], limit: int = 3) -> list[dict[str, Any]]:
    summary = _summary(component_payload)
    return list(summary.get("global_average_component_losses") or [])[:limit]


def _requirement_row(
    *,
    requirement_id: str,
    question: str,
    status: str,
    evidence: list[str],
    plain_answer: str,
    remaining_work: str,
) -> dict[str, Any]:
    return {
        "requirement_id": requirement_id,
        "question": question,
        "status": status,
        "evidence": evidence,
        "plain_answer": plain_answer,
        "remaining_work": remaining_work,
    }


def build_v12_goal_scope_evidence_audit(
    *,
    component_payload: Mapping[str, Any],
    historical_payload: Mapping[str, Any],
    current_census_payload: Mapping[str, Any],
    weight_payload: Mapping[str, Any],
    execution_payload: Mapping[str, Any],
    cross_trace_payload: Mapping[str, Any],
    axis_contract_payload: Mapping[str, Any],
    acceptance_payload: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a requirement-by-requirement audit from already generated evidence."""

    component_summary = _summary(component_payload)
    historical_summary = _summary(historical_payload)
    census_summary = _summary(current_census_payload)
    weight_summary = _summary(weight_payload)
    execution_summary = _summary(execution_payload)
    axis_summary = _summary(axis_contract_payload)
    acceptance_summary = _summary(acceptance_payload)
    focus = _focus_by_symbol(component_payload)
    hynix = focus.get("000660", {})
    samsung = focus.get("005930", {})
    global_losses = _top_global_losses(component_payload)

    requirement_rows = [
        _requirement_row(
            requirement_id="R1_samsung_hynix_score_cut_location",
            question="삼전/하닉 점수가 어디서 깎였나?",
            status="proved_for_current_benchmark",
            evidence=[
                "docs/0619/v12_component_score_loss_waterfall_2026-06-19.md",
                "docs/0619/v12_current_runtime_field_failure_census_2026-06-19.md",
                "docs/0619/v12_score_loss_causal_chain_2026-06-19.md",
            ],
            plain_answer=(
                "하닉은 EPS/FCF가 만점인데 bottleneck/visibility/bridge 손실로 Green까지 "
                f"{hynix.get('green_shortfall_to_87')}점 부족하다. 삼성도 EPS/FCF는 만점이지만 "
                f"confidence/bottleneck/visibility 손실로 Green까지 {samsung.get('green_shortfall_to_87')}점 부족하다."
            ),
            remaining_work="점수 기준을 낮추는 것이 아니라 source-backed bridge field를 채워 positive/guard replay로 검증해야 한다.",
        ),
        _requirement_row(
            requirement_id="R2_historical_green_cases_existed",
            question="지금까지 연구자료에 Green까지 간 애들이 실제로 있었나?",
            status="proved",
            evidence=[
                "docs/0619/v12_historical_green_case_runtime_translation_ledger_2026-06-19.md",
                "docs/0619/v12_green_score_axis_runtime_contract_audit_2026-06-19.md",
            ],
            plain_answer=(
                f"있었다. score_simulation row {historical_summary.get('score_simulation_row_count')}개 중 "
                f"historical Stage3-Green after case가 {historical_summary.get('historical_stage3_green_after_case_count')}개이고, "
                f"Green이 있었던 아키타입은 {historical_summary.get('historical_green_archetype_count')}개다."
            ),
            remaining_work="historical Green label을 그대로 production Green으로 쓰지 말고 source-backed fixture로 재현해야 한다.",
        ),
        _requirement_row(
            requirement_id="R3_research_accumulated_into_weights",
            question="연구자료가 합쳐져서 점수표가 만들어진 게 맞나?",
            status="proved_but_weight_layer_only",
            evidence=[
                "docs/0619/v12_weight_support_runtime_feature_audit_2026-06-19.md",
                "docs/0619/v12_runtime_execution_path_map_2026-06-19.md",
            ],
            plain_answer=(
                f"맞다. 누적 support row {weight_summary.get('total_archetype_support_rows')}개, "
                f"positive {weight_summary.get('total_archetype_positive_cases')}개, "
                f"counterexample {weight_summary.get('total_archetype_counterexamples')}개가 "
                f"{weight_summary.get('archetype_weight_count')}개 아키타입 weight profile에 들어갔다."
            ),
            remaining_work="weight는 배점표라서 답안지 field를 자동으로 채우지 않는다. parser/feature bridge가 별도로 필요하다.",
        ),
        _requirement_row(
            requirement_id="R4_why_low_despite_accumulation",
            question="누적됐는데 왜 지금 pipeline 점수는 낮나?",
            status="proved_root_cause",
            evidence=[
                "docs/0619/v12_runtime_execution_path_map_2026-06-19.md",
                "docs/0619/v12_green_score_axis_runtime_contract_audit_2026-06-19.md",
                "docs/0619/v12_component_score_loss_waterfall_2026-06-19.md",
            ],
            plain_answer=(
                "누적 연구는 weight layer까지는 들어갔지만, 현재 scorer는 research score축 이름을 직접 읽지 않는다. "
                f"Green score key top40 중 {axis_summary.get('top40_contract_status_counts')} 상태라서 대부분 source-backed primitive bridge가 필요하다."
            ),
            remaining_work="margin/customer/backlog/contract/capital_return 같은 score축을 실제 parser field와 component 입력으로 연결해야 한다.",
        ),
        _requirement_row(
            requirement_id="R5_not_hbm_only",
            question="HBM 문제만 고치면 끝나는가?",
            status="proved_no",
            evidence=[
                "docs/0619/v12_cross_archetype_score_loss_trace_2026-06-19.md",
                "docs/0619/v12_current_runtime_field_failure_census_2026-06-19.md",
                "docs/0619/v12_component_score_loss_waterfall_2026-06-19.md",
            ],
            plain_answer=(
                f"아니다. 현재 benchmark가 실제 채점한 아키타입은 {census_summary.get('runtime_exercised_archetype_count')}개뿐이고 "
                f"{census_summary.get('runtime_unexercised_archetype_count')}개는 미채점이다. "
                f"ready fixture 31개 기준 손실층도 {cross_trace_payload.get('loss_layer_counts_by_archetype')}로 나뉜다."
            ),
            remaining_work="C21/C22/C23/C28/C26 같은 비-HBM도 exact replay와 bridge adapter를 같이 보강해야 한다.",
        ),
        _requirement_row(
            requirement_id="R6_systemic_failure_layers",
            question="전체적으로 우리 문제가 무엇인가?",
            status="proved_failure_taxonomy",
            evidence=[
                "docs/0619/v12_runtime_execution_path_map_2026-06-19.md",
                "docs/0619/v12_runtime_repair_acceptance_spec_2026-06-19.md",
                "docs/0619/v12_runtime_repair_execution_backlog_2026-06-19.md",
            ],
            plain_answer=(
                f"중단 층은 {execution_summary.get('stop_layer_counts')}다. "
                f"수리 완료 판정 상태도 {acceptance_summary.get('acceptance_status_counts')}라서, "
                "후보/archive, parser-feature bridge, gate alignment를 분리해서 고쳐야 한다."
            ),
            remaining_work="수리 자체는 아직 완료가 아니다. acceptance spec의 blocked 상태를 실제 fixture/replay/test로 풀어야 한다.",
        ),
        _requirement_row(
            requirement_id="R7_current_runtime_component_distribution",
            question="지금 점수 손실은 어떤 과목에 몰려 있나?",
            status="proved_for_current_benchmark",
            evidence=["docs/0619/v12_component_score_loss_waterfall_2026-06-19.md"],
            plain_answer=(
                "전역 평균 손실 상위는 "
                + ", ".join(
                    f"{row.get('component')} {row.get('avg_loss_points')}점" for row in global_losses
                )
                + "이다."
            ),
            remaining_work="이 분포는 current benchmark 후보 120개 기준이다. 미채점 28개 아키타입은 replay 후 별도 재계산해야 한다.",
        ),
        _requirement_row(
            requirement_id="R8_documentation_under_0619",
            question="0619 폴더에 계속 문서화했나?",
            status="proved_current_artifacts",
            evidence=[
                "docs/0619/README.md",
                "docs/0619/v12_component_score_loss_waterfall_2026-06-19.md",
                "docs/0619/v12_runtime_execution_path_map_2026-06-19.md",
            ],
            plain_answer="0619 README가 현재 결론과 읽을 순서를 갖고 있고, v12 진단 문서들이 JSON/MD 쌍으로 남아 있다.",
            remaining_work="새 수리 패치가 생기면 같은 방식으로 acceptance evidence와 README를 갱신해야 한다.",
        ),
    ]

    status_counts: dict[str, int] = {}
    for row in requirement_rows:
        status_counts[row["status"]] = status_counts.get(row["status"], 0) + 1

    return {
        "schema_version": "v12_goal_scope_evidence_audit_v1",
        "scope": "0619_investigation_requirement_coverage",
        "scoring_policy": "diagnostic_only_no_weight_or_stage_change",
        "summary": {
            "requirement_count": len(requirement_rows),
            "requirement_status_counts": dict(sorted(status_counts.items())),
            "investigation_completion_status": "complete_for_root_cause_investigation",
            "implementation_repair_status": "not_complete_and_tracked_as_acceptance_blockers",
            "investigation_plain_conclusion": (
                "삼전/하닉 저점수는 HBM 특례로 풀 문제가 아니라 누적 연구가 candidate/archive, "
                "runtime input evidence, parser-feature bridge, weighted gate 중 어디서 멈추는지 "
                "전 아키타입에서 분리해야 하는 공통 문제다."
            ),
            "implementation_plain_conclusion": (
                "조사 목표는 요구사항별 증거로 완료됐지만, 수리 구현은 아직 완료가 아니다. acceptance spec의 "
                "blocked 항목을 exact replay, parser/feature bridge, positive/guard parity로 풀어야 한다."
            ),
            "hynix_green_shortfall_to_87": hynix.get("green_shortfall_to_87"),
            "samsung_green_shortfall_to_87": samsung.get("green_shortfall_to_87"),
            "historical_stage3_green_after_case_count": historical_summary.get(
                "historical_stage3_green_after_case_count"
            ),
            "research_support_rows": weight_summary.get("total_archetype_support_rows"),
            "runtime_exercised_archetype_count": census_summary.get("runtime_exercised_archetype_count"),
            "runtime_unexercised_archetype_count": census_summary.get("runtime_unexercised_archetype_count"),
            "current_stage3_green_count": census_summary.get("stage3_green_count"),
            "stop_layer_counts": execution_summary.get("stop_layer_counts"),
            "acceptance_status_counts": acceptance_summary.get("acceptance_status_counts"),
        },
        "requirement_rows": requirement_rows,
    }


def _fmt(value: Any) -> str:
    if value is None:
        return ""
    return str(value)


def render_v12_goal_scope_evidence_audit(payload: Mapping[str, Any]) -> str:
    summary = payload.get("summary") or {}
    lines = [
        "# V12 Goal Scope Evidence Audit",
        "",
        "이 문서는 원래 질문을 요구사항으로 쪼개서, 0619 산출물이 무엇을 증명했고 무엇이 아직 구현 과제인지 정리한다.",
        "점수나 stage를 바꾸는 문서가 아니라 진단 범위 감사표다.",
        "",
        "## Summary",
        "",
        f"- investigation_plain_conclusion: {summary.get('investigation_plain_conclusion')}",
        f"- implementation_plain_conclusion: {summary.get('implementation_plain_conclusion')}",
        f"- investigation_completion_status: `{summary.get('investigation_completion_status')}`",
        f"- implementation_repair_status: `{summary.get('implementation_repair_status')}`",
        f"- requirement_count: `{summary.get('requirement_count')}`",
        f"- requirement_status_counts: `{summary.get('requirement_status_counts')}`",
        f"- current_stage3_green_count: `{summary.get('current_stage3_green_count')}`",
        f"- historical_stage3_green_after_case_count: `{summary.get('historical_stage3_green_after_case_count')}`",
        f"- research_support_rows: `{summary.get('research_support_rows')}`",
        f"- runtime_exercised/unexercised_archetypes: `{summary.get('runtime_exercised_archetype_count')}` / `{summary.get('runtime_unexercised_archetype_count')}`",
        f"- hynix/samsung_green_shortfall_to_87: `{summary.get('hynix_green_shortfall_to_87')}` / `{summary.get('samsung_green_shortfall_to_87')}`",
        f"- stop_layer_counts: `{summary.get('stop_layer_counts')}`",
        f"- acceptance_status_counts: `{summary.get('acceptance_status_counts')}`",
        "",
        "## Requirement Coverage",
        "",
        "| id | status | question | plain answer | remaining work | evidence |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in payload.get("requirement_rows") or []:
        lines.append(
            "| {rid} | {status} | {question} | {answer} | {work} | {evidence} |".format(
                rid=row.get("requirement_id"),
                status=row.get("status"),
                question=row.get("question"),
                answer=row.get("plain_answer"),
                work=row.get("remaining_work"),
                evidence="<br>".join(_fmt(item) for item in row.get("evidence") or []),
            )
        )
    lines.extend(
        [
            "",
            "## Easy Reading",
            "",
            "- 지금까지 연구가 사라진 것은 아니다. 배점표에는 들어갔다.",
            "- 그런데 배점표는 시험 문제의 배점일 뿐이다. 답안지의 source-backed field가 비면 점수는 낮게 나온다.",
            "- 하닉은 EPS/FCF와 bridge field가 강하게 잡혀도 total/bottleneck gate를 통과해야 Green이 된다.",
            "- 삼성은 같은 HBM 테마라도 C06 direct Green이 아니라 C10 memory recovery route로 따로 검증해야 한다.",
            "- C01/C19/R13처럼 후보 row의 입력 가족이 약한 케이스는 parser 실패로 단정하지 말고 replay 입력부터 보강해야 한다.",
            "- C21 금융, C23 바이오, C26 플랫폼 같은 비-HBM은 아예 current benchmark 시험지에 안 들어온 케이스가 많다.",
            "- 따라서 원인 조사는 완료됐고, 다음 작업은 HBM 보너스가 아니라 exact replay archive, parser/feature bridge, positive/guard parity를 구현하는 것이다.",
        ]
    )
    return "\n".join(lines) + "\n"


def write_v12_goal_scope_evidence_audit(
    *,
    component_path: str | Path = DEFAULT_COMPONENT_WATERFALL_PATH,
    historical_path: str | Path = DEFAULT_HISTORICAL_LEDGER_PATH,
    current_census_path: str | Path = DEFAULT_CURRENT_CENSUS_PATH,
    weight_path: str | Path = DEFAULT_WEIGHT_AUDIT_PATH,
    execution_path: str | Path = DEFAULT_EXECUTION_PATH_PATH,
    cross_trace_path: str | Path = DEFAULT_CROSS_TRACE_PATH,
    axis_contract_path: str | Path = DEFAULT_AXIS_CONTRACT_PATH,
    acceptance_path: str | Path = DEFAULT_ACCEPTANCE_SPEC_PATH,
    output_json_path: str | Path = DEFAULT_OUTPUT_JSON_PATH,
    output_md_path: str | Path = DEFAULT_OUTPUT_MD_PATH,
) -> dict[str, Any]:
    payload = build_v12_goal_scope_evidence_audit(
        component_payload=_read_json(component_path),
        historical_payload=_read_json(historical_path),
        current_census_payload=_read_json(current_census_path),
        weight_payload=_read_json(weight_path),
        execution_payload=_read_json(execution_path),
        cross_trace_payload=_read_json(cross_trace_path),
        axis_contract_payload=_read_json(axis_contract_path),
        acceptance_payload=_read_json(acceptance_path),
    )
    json_path = Path(output_json_path)
    md_path = Path(output_md_path)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    md_path.write_text(render_v12_goal_scope_evidence_audit(payload), encoding="utf-8")
    return {"json_path": str(json_path), "md_path": str(md_path), "summary": payload["summary"]}


if __name__ == "__main__":
    result = write_v12_goal_scope_evidence_audit()
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
