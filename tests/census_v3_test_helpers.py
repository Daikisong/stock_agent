from __future__ import annotations

import csv
import json
import shutil
import tempfile
from pathlib import Path
from typing import Any

from e2r.census.census_runner_v3 import CensusV3RunConfig, run_census_mode_v3
from e2r.census.production_cutover_leaf_loader import ProductionCutoverLeafBundle


_CACHE: dict[str, Any] | None = None
_CACHE_TEMP_DIR: tempfile.TemporaryDirectory[str] | None = None

_REAL_SYMBOLS = (
    ("000660", "SK하이닉스"),
    ("001440", "대한전선"),
    ("001470", "삼부토건"),
    ("003090", "대웅"),
    ("003230", "삼양식품"),
    ("005930", "삼성전자"),
    ("011200", "HMM"),
    ("012450", "한화에어로스페이스"),
    ("024840", "KBI메탈"),
    ("030350", "드래곤플라이"),
    ("043260", "성호전자"),
    ("062040", "산일전기"),
    ("096530", "씨젠"),
    ("103590", "일진전기"),
    ("247540", "에코프로비엠"),
    ("257720", "실리콘투"),
    ("267260", "HD현대일렉트릭"),
    ("298040", "효성중공업"),
    ("473980", "노머스"),
)


def census_v3_artifacts() -> dict[str, Any]:
    global _CACHE, _CACHE_TEMP_DIR
    if _CACHE is None:
        _CACHE_TEMP_DIR = tempfile.TemporaryDirectory()
        temp_root = Path(_CACHE_TEMP_DIR.name)
        output_root = temp_root / "census_v3"
        universe_file = temp_root / "universe.csv"
        _write_test_universe(universe_file)
        result = run_census_mode_v3(
            CensusV3RunConfig(
                as_of_date="2026-07-01",
                output_root=str(output_root),
                universe_file=str(universe_file),
                fail_on_critical_audit=True,
                write_operational_docs=False,
                test_result_summary="unit_test_cached_run",
                test_mode=True,
                test_leaf_bundle=_test_leaf_bundle(),
            )
        )
        _CACHE = {
            "result": result,
            "output_root": output_root,
            "leaf_audit": read_json(output_root / "leaf_artifact_audit.json"),
            "stage_rows": read_jsonl(output_root / "census_stage_status.jsonl"),
            "trace_rows": read_jsonl(output_root / "claim_to_stage_trace.jsonl"),
            "source_tasks": read_jsonl(output_root / "source_tasks.jsonl"),
            "source_task_executions": read_jsonl(output_root / "source_task_executions.jsonl"),
            "accepted_claims": read_jsonl(output_root / "accepted_claims.jsonl"),
            "score_contributions": read_jsonl(output_root / "score_contributions.jsonl"),
            "timelines": read_jsonl(output_root / "source_timelines.jsonl"),
            "thesis_states": read_jsonl(output_root / "last_effective_thesis_states.jsonl"),
            "events": read_jsonl(output_root / "census_events.jsonl"),
            "reviewer_a": read_json(output_root / "reviewer_A_trace_audit.json"),
            "reviewer_b": read_json(output_root / "reviewer_B_source_audit.json"),
            "reviewer_c": read_json(output_root / "reviewer_C_stage_audit.json"),
            "self_repair": read_json(output_root / "self_repair_log.json"),
        }
    return _CACHE


def _write_test_universe(path: Path) -> None:
    rows = [
        {
            "symbol": symbol,
            "company_name": company_name,
            "market": "KOSPI",
            "listing_status": "ACTIVE",
            "instrument_type": "COMMON",
            "large_sector_id": "tracked_reference",
            "sector_source": "census_v3_test_fixture",
        }
        for symbol, company_name in _REAL_SYMBOLS
    ]
    rows.extend(
        {
            "symbol": f"{600000 + index:06d}",
            "company_name": f"검증기업 {index:04d}",
            "market": "KOSPI" if index % 2 == 0 else "KOSDAQ",
            "listing_status": "ACTIVE",
            "instrument_type": "COMMON",
            "large_sector_id": f"test_sector_{index % 8}",
            "sector_source": "census_v3_test_fixture",
        }
        for index in range(1000)
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=tuple(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def _test_leaf_bundle() -> ProductionCutoverLeafBundle:
    scored_symbols = tuple(f"{600000 + index:06d}" for index in range(12))
    task_symbols = tuple(f"{600000 + index:06d}" for index in range(60))
    candidate_events: list[dict[str, Any]] = []
    research_plans: list[dict[str, Any]] = []
    source_tasks: list[dict[str, Any]] = []
    executions: list[dict[str, Any]] = []
    documents: list[dict[str, Any]] = []
    anchors: list[dict[str, Any]] = []
    raw_assertions: list[dict[str, Any]] = []
    adjudicated_claims: list[dict[str, Any]] = []
    accepted_claims: list[dict[str, Any]] = []
    primitive_states: list[dict[str, Any]] = []
    contributions: list[dict[str, Any]] = []
    stagecourt_traces: list[dict[str, Any]] = []

    for index, symbol in enumerate(task_symbols):
        event_id = f"CE-TEST-{index:03d}"
        task_id = f"TASK-TEST-{index:03d}"
        if symbol in scored_symbols:
            candidate_events.append(
                {
                    "schema_version": "e2r_candidate_event_v1",
                    "candidate_event_id": event_id,
                    "symbol": symbol,
                    "event_date": "2026-06-30",
                    "event_title": "정기 공시에서 확인할 현재 증거 발생",
                    "event_summary": "공식 문서의 현재 사실을 Evidence OS로 검증하는 테스트 사건",
                    "source_family": "OpenDART",
                    "source_url": f"https://example.test/disclosure/{symbol}/{index}",
                    "trigger_category": "Official Filing",
                    "source_task_generation_policy": "test_fake_planner",
                }
            )
        research_plans.append(
            {
                "schema_version": "e2r_census_v3_research_brain_plan_ref_v1",
                "plan_id": f"RBPLAN-TEST-{index:03d}",
                "symbol": symbol,
                "candidate_event_id": event_id,
                "source_task_ids": [task_id],
                "planner_origin": "bounded_test_fake_planner",
                "forbidden_direct_score_stage": True,
            }
        )
        source_tasks.append(
            {
                "schema_version": "e2r_source_task_v1",
                "task_id": task_id,
                "symbol": symbol,
                "candidate_event_id": event_id,
                "primitive_gap": "current_official_fact",
                "source_family": "OpenDART",
                "budget": {"max_queries": 1, "max_candidates": 1, "max_fetches": 1, "max_retries": 0},
                "stop_condition": "accepted_claim_or_exhausted",
                "source_task_origin": "production_cutover_v3_leaf_artifact",
                "general_search_allowed": False,
            }
        )
        accepted_ids = [f"CLAIM-TEST-{index:03d}"] if symbol in scored_symbols else []
        executions.append(
            {
                "schema_version": "e2r_source_task_execution_v1",
                "task_id": task_id,
                "symbol": symbol,
                "candidate_event_id": event_id,
                "status": "EVIDENCE_OS_ACCEPTED" if accepted_ids else "NO_ACCEPTED_CLAIM",
                "accepted_claim_ids": accepted_ids,
                "fetched_document_ids": [f"DOC-TEST-{index:03d}"] if accepted_ids else [],
                "source_task_execution_origin": "production_cutover_v3_leaf_artifact",
                "claim_producing_execution": bool(accepted_ids),
                "provider_name": "OpenDART",
                "source_class": "DART",
                "requested_source_classes": ["DART"],
            }
        )

    stage_cycle = ("2", "3-Yellow", "3-Green")
    for index, symbol in enumerate(scored_symbols):
        event_id = f"CE-TEST-{index:03d}"
        claim_id = f"CLAIM-TEST-{index:03d}"
        document_id = f"DOC-TEST-{index:03d}"
        anchor_id = f"ANCHOR-TEST-{index:03d}"
        raw_id = f"RAW-TEST-{index:03d}"
        contribution_id = f"CONTRIB-TEST-{index:03d}"
        trace_id = f"SCT-TEST-{index:03d}"
        primitive_id = "information_confidence"
        mapping_id = f"MAP-TEST-{index:03d}"
        source_url = f"https://example.test/disclosure/{symbol}/{index}"
        quote_text = f"검증기업 {index:03d} 투자판단관련주요경영사항 현재 공시"
        documents.append(
            {
                "document_id": document_id,
                "symbol": symbol,
                "source_family": "OpenDART",
                "source_url": source_url,
                "published_at": "2026-06-30",
                "as_of_date": "2026-07-01",
                "content_hash": f"content-hash-{index:03d}",
            }
        )
        anchors.append(
            {
                "anchor_id": anchor_id,
                "document_id": document_id,
                "symbol": symbol,
                "quote_text": quote_text,
                "page_number": 1,
            }
        )
        raw_assertions.append(
            {
                "raw_assertion_id": raw_id,
                "claim_id": claim_id,
                "symbol": symbol,
                "document_id": document_id,
                "anchor_id": anchor_id,
                "primitive_id": primitive_id,
                "assertion_text": quote_text,
            }
        )
        claim = {
            "schema_version": "e2r_accepted_claim_v1",
            "claim_id": claim_id,
            "accepted": True,
            "symbol": symbol,
            "target_entity_id": f"TICKER:{symbol}",
            "candidate_event_id": event_id,
            "document_id": document_id,
            "anchor_id": anchor_id,
            "raw_assertion_id": raw_id,
            "primitive_id": primitive_id,
            "mapping": {
                "mapping_status": "ACCEPTED",
                "primitive_id": primitive_id,
                "rationale": "predicate:official_information_claim",
                "support_direction": "SUPPORT",
            },
            "mapping_status": "ACCEPTED",
            "support_direction": "SUPPORT",
            "target_scope_status": "DIRECT",
            "directness": "DIRECT",
            "temporal_status": "CURRENT",
            "semantic_status": "PASS",
            "polarity": "POSITIVE",
            "satisfies_source_task": True,
            "event_date": "2026-06-30",
            "as_of_date": "2026-07-01",
            "source_provider": "OpenDART",
            "source_family": "OpenDART",
            "source_url": source_url,
            "claim_status": "ACCEPTED",
            "score_eligible": True,
            "evidence_type": "direct",
            "lifecycle_status": "current",
            "quote_text": quote_text,
        }
        adjudicated_claims.append(dict(claim))
        accepted_claims.append(claim)
        primitive_states.append(
            {
                "primitive_state_id": f"PSTATE-TEST-{index:03d}",
                "symbol": symbol,
                "primitive_id": primitive_id,
                "support_claim_ids": [claim_id],
                "status": "PRESENT_CURRENT",
            }
        )
        contributions.append(
            {
                "score_contribution_id": contribution_id,
                "contribution_id": contribution_id,
                "symbol": symbol,
                "component_key": "information_confidence",
                "criterion_id": "production_cutover_information_confidence",
                "primitive_id": primitive_id,
                "support_claim_ids": [claim_id],
                "accepted_claim_ids": [claim_id],
                "raw_points": 1.0,
                "max_points": 5.0,
                "source_family": "OpenDART",
                "source_family_ids": ["OpenDART"],
                "mapping_ids": [mapping_id],
                "source_type": "official_filing",
                "source_proxy_only": False,
                "evidence_url_pending": False,
                "price_path_only": False,
            }
        )
        score = 4.0
        stagecourt_traces.append(
            {
                "schema_version": "e2r_stagecourt_trace_v1",
                "stagecourt_trace_id": trace_id,
                "trace_id": trace_id,
                "symbol": symbol,
                "candidate_event_id": event_id,
                "accepted_claim_ids": [claim_id],
                "score_contribution_ids": [contribution_id],
                "base_stage": stage_cycle[index % len(stage_cycle)],
                "score_status": "FINAL_WITH_NONMATERIAL_GAPS",
                "score_interval": {"lower": score, "upper": score},
                "missing_green_primitives": [],
                "missing_yellow_primitives": [],
                "stage_decision_reason": "bounded source-backed test fixture",
            }
        )

    _append_v4_semantic_scenarios(
        candidate_events=candidate_events,
        research_plans=research_plans,
        source_tasks=source_tasks,
        executions=executions,
        documents=documents,
        anchors=anchors,
        raw_assertions=raw_assertions,
        adjudicated_claims=adjudicated_claims,
        accepted_claims=accepted_claims,
        primitive_states=primitive_states,
        contributions=contributions,
        stagecourt_traces=stagecourt_traces,
    )

    return ProductionCutoverLeafBundle(
        candidate_events=tuple(candidate_events),
        research_brain_plans=tuple(research_plans),
        source_tasks=tuple(source_tasks),
        source_task_executions=tuple(executions),
        evidence_documents=tuple(documents),
        evidence_anchors=tuple(anchors),
        raw_assertions=tuple(raw_assertions),
        adjudicated_claims=tuple(adjudicated_claims),
        accepted_claims=tuple(accepted_claims),
        primitive_states=tuple(primitive_states),
        score_contributions=tuple(contributions),
        stagecourt_traces=tuple(stagecourt_traces),
        watchlist_rows=(),
        skipped_rows=(),
    )


def _append_v4_semantic_scenarios(**rows: list[dict[str, Any]]) -> None:
    scenarios = (
        {
            "symbol": "005930",
            "company_name": "삼성전자",
            "suffix": "SAMSUNG-DAILY",
            "primitive_id": "information_confidence",
            "quote_text": "삼성전자 현재 분기보고서 직접 확인",
            "component_key": "information_confidence",
            "criterion_id": "production_cutover_information_confidence",
            "raw_points": 1.0,
            "score": 4.0,
            "base_stage": "1",
        },
        {
            "symbol": "000660",
            "company_name": "SK하이닉스",
            "suffix": "HYNIX-DAILY",
            "primitive_id": "information_confidence",
            "quote_text": "SK하이닉스 현재 분기보고서 직접 확인",
            "component_key": "information_confidence",
            "criterion_id": "production_cutover_information_confidence",
            "raw_points": 1.0,
            "score": 4.0,
            "base_stage": "1",
        },
        {
            "symbol": "473980",
            "company_name": "노머스",
            "suffix": "BUYBACK",
            "primitive_id": "contract_quality",
            "quote_text": "노머스 주요사항보고서(자기주식취득신탁계약체결결정)",
            "component_key": "earnings_visibility",
            "criterion_id": "production_cutover_contract_quality",
            "raw_points": 4.0,
            "score": 4.4,
            "base_stage": "2",
        },
        {
            "symbol": "043260",
            "company_name": "성호전자",
            "suffix": "PLEDGE",
            "primitive_id": "contract_quality",
            "quote_text": "성호전자 최대주주변경을수반하는주식담보제공계약체결",
            "component_key": "earnings_visibility",
            "criterion_id": "production_cutover_contract_quality",
            "raw_points": 4.0,
            "score": 4.4,
            "base_stage": "2",
        },
        {
            "symbol": "003090",
            "company_name": "대웅",
            "suffix": "CAPACITY-CORRECTION",
            "primitive_id": "capacity_expansion",
            "quote_text": "대웅 [기재정정]신규시설투자등(자회사의 주요경영사항)",
            "component_key": "bottleneck_pricing",
            "criterion_id": "production_cutover_capacity_expansion",
            "raw_points": 3.0,
            "score": 1.5,
            "base_stage": "2",
        },
        {
            "symbol": "030350",
            "company_name": "드래곤플라이",
            "suffix": "CURRENT-RISK",
            "primitive_id": "information_confidence",
            "quote_text": "드래곤플라이 주권매매거래정지기간변경 (개선기간 부여)",
            "component_key": "information_confidence",
            "criterion_id": "production_cutover_information_confidence",
            "raw_points": 1.0,
            "score": 4.0,
            "base_stage": "3-Red",
        },
        {
            "symbol": "001470",
            "company_name": "삼부토건",
            "suffix": "ADMIN",
            "primitive_id": "information_confidence",
            "quote_text": "삼부토건 투자판단관련주요경영사항",
            "component_key": "information_confidence",
            "criterion_id": "production_cutover_information_confidence",
            "raw_points": 1.0,
            "score": 4.0,
            "base_stage": "1",
        },
        {
            "symbol": "001470",
            "company_name": "삼부토건",
            "suffix": "SUPPLY",
            "primitive_id": "contract_quality",
            "quote_text": "삼부토건 [기재정정]단일판매ㆍ공급계약체결",
            "component_key": "earnings_visibility",
            "criterion_id": "production_cutover_contract_quality",
            "raw_points": 4.0,
            "score": 4.4,
            "base_stage": "2",
        },
    )
    for index, scenario in enumerate(scenarios):
        suffix = str(scenario["suffix"])
        symbol = str(scenario["symbol"])
        event_id = f"CE-V4-{suffix}"
        task_id = f"TASK-V4-{suffix}"
        claim_id = f"CLAIM-V4-{suffix}"
        document_id = f"DOC-V4-{suffix}"
        anchor_id = f"ANCHOR-V4-{suffix}"
        raw_id = f"RAW-V4-{suffix}"
        mapping_id = f"MAP-V4-{suffix}"
        contribution_id = f"CONTRIB-V4-{suffix}"
        trace_id = f"SCT-V4-{suffix}"
        primitive_id = str(scenario["primitive_id"])
        quote_text = str(scenario["quote_text"])
        source_url = f"https://example.test/v4/{symbol}/{suffix.lower()}"

        rows["candidate_events"].append(
            {
                "candidate_event_id": event_id,
                "symbol": symbol,
                "company_name": scenario["company_name"],
                "event_date": "2026-06-30",
                "event_title": quote_text,
                "event_summary": quote_text,
                "source_family": "OpenDART",
                "source_url": source_url,
                "trigger_category": "Risk Trigger" if scenario["base_stage"] == "3-Red" else "Official Filing",
                "source_task_generation_policy": "bounded_test_fake_planner",
            }
        )
        rows["research_plans"].append(
            {
                "plan_id": f"RBPLAN-V4-{suffix}",
                "symbol": symbol,
                "candidate_event_id": event_id,
                "source_task_ids": [task_id],
                "planner_origin": "bounded_test_fake_planner",
                "forbidden_direct_score_stage": True,
            }
        )
        rows["source_tasks"].append(
            {
                "task_id": task_id,
                "symbol": symbol,
                "candidate_event_id": event_id,
                "primitive_gap": primitive_id,
                "source_family": "OpenDART",
                "budget": {"max_queries": 1, "max_candidates": 1, "max_fetches": 1, "max_retries": 0},
                "stop_condition": "accepted_claim_or_exhausted",
                "source_task_origin": "production_cutover_v3_leaf_artifact",
                "general_search_allowed": False,
            }
        )
        rows["executions"].append(
            {
                "task_id": task_id,
                "symbol": symbol,
                "candidate_event_id": event_id,
                "status": "EVIDENCE_OS_ACCEPTED",
                "accepted_claim_ids": [claim_id],
                "fetched_document_ids": [document_id],
                "source_task_execution_origin": "production_cutover_v3_leaf_artifact",
                "claim_producing_execution": True,
                "provider_name": "OpenDART",
                "source_class": "DART",
                "requested_source_classes": ["DART"],
            }
        )
        rows["documents"].append(
            {
                "document_id": document_id,
                "symbol": symbol,
                "source_family": "OpenDART",
                "source_url": source_url,
                "published_at": "2026-06-30",
                "as_of_date": "2026-07-01",
                "raw_text": quote_text,
            }
        )
        rows["anchors"].append(
            {
                "anchor_id": anchor_id,
                "document_id": document_id,
                "symbol": symbol,
                "quote_text": quote_text,
                "page_number": 1,
            }
        )
        assertion = {
            "raw_assertion_id": raw_id,
            "claim_id": claim_id,
            "symbol": symbol,
            "document_id": document_id,
            "anchor_id": anchor_id,
            "primitive_id": primitive_id,
            "quote_text": quote_text,
        }
        rows["raw_assertions"].append(assertion)
        claim = {
            **assertion,
            "accepted": True,
            "target_entity_id": f"TICKER:{symbol}",
            "subject_entity_id": f"TICKER:{symbol}",
            "candidate_event_id": event_id,
            "event_date": "2026-06-30",
            "as_of_date": "2026-07-01",
            "source_provider": "OpenDART",
            "source_family": "OpenDART",
            "source_url": source_url,
            "claim_status": "ACCEPTED",
            "score_eligible": True,
            "mapping": {
                "mapping_status": "ACCEPTED",
                "primitive_id": primitive_id,
                "rationale": f"predicate:{primitive_id}",
                "support_direction": "SUPPORT",
            },
            "mapping_status": "ACCEPTED",
            "support_direction": "SUPPORT",
            "target_scope_status": "DIRECT",
            "directness": "DIRECT",
            "temporal_status": "CURRENT",
            "semantic_status": "PASS",
            "polarity": "POSITIVE",
            "satisfies_source_task": True,
        }
        rows["adjudicated_claims"].append(dict(claim))
        rows["accepted_claims"].append(claim)
        rows["primitive_states"].append(
            {
                "primitive_state_id": f"PSTATE-V4-{suffix}",
                "candidate_event_id": event_id,
                "symbol": symbol,
                "primitive_id": primitive_id,
                "support_claim_ids": [claim_id],
                "counter_claim_ids": [],
                "status": "PRESENT_CURRENT",
            }
        )
        rows["contributions"].append(
            {
                "score_contribution_id": contribution_id,
                "contribution_id": contribution_id,
                "symbol": symbol,
                "component_key": scenario["component_key"],
                "criterion_id": scenario["criterion_id"],
                "primitive_id": primitive_id,
                "support_claim_ids": [claim_id],
                "accepted_claim_ids": [claim_id],
                "raw_points": scenario["raw_points"],
                "max_points": 20.0 if scenario["component_key"] != "information_confidence" else 5.0,
                "source_family": "OpenDART",
                "source_family_ids": [f"DART:{claim_id}"],
                "mapping_ids": [mapping_id],
                "source_type": "official_filing",
                "source_proxy_only": False,
                "evidence_url_pending": False,
                "price_path_only": False,
            }
        )
        rows["stagecourt_traces"].append(
            {
                "stagecourt_trace_id": trace_id,
                "trace_id": trace_id,
                "symbol": symbol,
                "candidate_event_id": event_id,
                "accepted_claim_ids": [claim_id],
                "score_contribution_ids": [contribution_id],
                "base_stage": scenario["base_stage"],
                "score_status": "FINAL_WITH_NONMATERIAL_GAPS",
                "score_interval": {"lower": scenario["score"], "upper": scenario["score"]},
                "missing_green_primitives": ["repeat_evidence_family", "cash_or_revision_conversion"],
                "missing_yellow_primitives": ["multi_source_confirmation"],
                "stage_decision_reason": "bounded semantic guard test fixture",
            }
        )


def temp_census_v3_copy() -> tuple[tempfile.TemporaryDirectory, Path]:
    artifacts = census_v3_artifacts()
    tmp = tempfile.TemporaryDirectory()
    dst = Path(tmp.name) / "census_v3"
    shutil.copytree(artifacts["output_root"], dst)
    return tmp, dst


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Any) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            text = line.strip()
            if text:
                rows.append(json.loads(text))
    return rows


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
