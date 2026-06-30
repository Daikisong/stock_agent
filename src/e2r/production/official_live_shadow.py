"""Official-source daily shadow builder for Production Cutover Gate v1."""

from __future__ import annotations

import hashlib
import io
import json
import os
import re
import shlex
import signal
import subprocess
import tempfile
import time
import zipfile
from dataclasses import dataclass
from datetime import date, datetime
from functools import lru_cache
from pathlib import Path
from typing import Any, Mapping, Sequence
import xml.etree.ElementTree as ET

import requests

from e2r.env import load_project_env
from e2r.production.candidate_event_purity import InstrumentRegistry
from e2r.production.claim_extraction import (
    ContractBlindRawAssertionExtractor,
    ExtractionInput,
    adjudicate_entity_temporal_scope,
    map_claim_to_primitive,
)
from e2r.production.metadata import stable_hash
from e2r.agentic import ScoreContributionV2
from e2r.calibration.taxonomy import large_sector_for_archetype
from e2r.scoring import CANONICAL_SCORE_COMPONENTS, DeterministicScorer, ScoringPayload


_DART_LIST_URL = "https://opendart.fss.or.kr/api/list.json"
_DART_CORP_CODE_URL = "https://opendart.fss.or.kr/api/corpCode.xml"
_DART_COMPANY_URL = "https://opendart.fss.or.kr/api/company.json"
_DISCLOSURE_KEYWORDS = (
    "단일판매",
    "공급계약",
    "영업(잠정)실적",
    "잠정실적",
    "유상증자",
    "신규시설투자",
    "투자판단",
    "자기주식",
    "배당",
    "증권발행",
)
_ALLOWED_PRIMITIVES = (
    "contract_quality",
    "revenue_visibility_contract",
    "order_to_revenue_bridge",
    "capital_allocation_event",
    "capacity_expansion",
    "capacity_precommitted",
    "medium_term_revision_visibility",
    "accounting_trust_break",
    "fcf_quality_score",
    "margin_bridge_visible",
    "information_confidence",
)
_DEFAULT_ARCHETYPE_ID = "C05_EPC_MEGA_CONTRACT_MARGIN_GAP"
_FORBIDDEN_PLANNER_KEYS = {
    "score",
    "stage",
    "hard_break",
    "current_score_eligible",
    "verified_score",
    "final_stage",
    "feature_input",
    "score_contribution",
}
_PLANNER_BATCH_OUTPUT_SCHEMA: Mapping[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "plans": {
            "type": "array",
            "minItems": 1,
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "candidate_event_id": {"type": "string"},
                    "archetype_id": {"type": "string"},
                    "primitive_gap": {"type": "string"},
                    "preferred_source_classes": {
                        "type": "array",
                        "minItems": 1,
                        "items": {"type": "string"},
                    },
                    "fallback_source_classes": {"type": "array", "items": {"type": "string"}},
                    "forbidden_source_classes": {"type": "array", "items": {"type": "string"}},
                    "max_queries": {"type": "integer"},
                    "max_candidates": {"type": "integer"},
                    "max_fetches": {"type": "integer"},
                    "rationale": {"type": "string"},
                    "red_team_checks": {"type": "array", "items": {"type": "string"}},
                    "planner_self_check": {
                        "type": "object",
                        "additionalProperties": False,
                        "properties": {
                            "score_keys_present": {"type": "boolean"},
                            "stage_keys_present": {"type": "boolean"},
                            "future_outcome_used": {"type": "boolean"},
                        },
                        "required": ["score_keys_present", "stage_keys_present", "future_outcome_used"],
                    },
                },
                "required": [
                    "candidate_event_id",
                    "archetype_id",
                    "primitive_gap",
                    "preferred_source_classes",
                    "fallback_source_classes",
                    "forbidden_source_classes",
                    "max_queries",
                    "max_candidates",
                    "max_fetches",
                    "rationale",
                    "red_team_checks",
                    "planner_self_check",
                ],
            },
        }
    },
    "required": ["plans"],
}


@dataclass(frozen=True)
class OfficialLiveShadowData:
    registry: InstrumentRegistry
    candidate_events: tuple[Mapping[str, Any], ...]
    planner_runs: tuple[Mapping[str, Any], ...]
    source_tasks: tuple[Mapping[str, Any], ...]
    source_task_executions: tuple[Mapping[str, Any], ...]
    evidence_documents: tuple[Mapping[str, Any], ...]
    evidence_anchors: tuple[Mapping[str, Any], ...]
    evidence_claim_ledger: tuple[Mapping[str, Any], ...]
    primitive_states: tuple[Mapping[str, Any], ...]
    score_contributions: tuple[Mapping[str, Any], ...]
    stagecourt_traces: tuple[Mapping[str, Any], ...]
    daily_watchlist: tuple[Mapping[str, Any], ...]
    operator_digest_rows: tuple[Mapping[str, Any], ...]
    provider_results: tuple[Mapping[str, Any], ...]
    source_corpus: Mapping[str, Any]


def build_official_live_shadow_data(
    *,
    repo_root: str | Path,
    as_of_date: date,
    candidate_min_count: int,
    planner_provider: str = "surrogate",
) -> OfficialLiveShadowData:
    root = Path(repo_root)
    universe_rows = _fetch_opendart_universe()
    registry = _registry_from_dart_universe(universe_rows)
    disclosure_rows = _fetch_opendart_disclosures(as_of_date=as_of_date, pages=5, page_count=100)
    selected = _select_disclosure_candidates(disclosure_rows, candidate_min_count=candidate_min_count)
    extractor = ContractBlindRawAssertionExtractor()
    event_rows: list[tuple[Mapping[str, Any], Mapping[str, Any]]] = []
    for row in selected:
        company_info = _fetch_opendart_company(str(row["corp_code"]))
        event_rows.append((row, _candidate_event_from_dart_row(row, as_of_date=as_of_date, company_info=company_info)))
    planner_by_event_id = _planner_runs_for_events(
        tuple(event for _, event in event_rows),
        provider_mode=planner_provider,
        repo_root=root,
    )
    events: list[Mapping[str, Any]] = []
    planner_runs: list[Mapping[str, Any]] = []
    source_tasks: list[Mapping[str, Any]] = []
    source_task_executions: list[Mapping[str, Any]] = []
    documents: list[Mapping[str, Any]] = []
    anchors: list[Mapping[str, Any]] = []
    claims: list[Mapping[str, Any]] = []
    primitive_states: list[Mapping[str, Any]] = []
    score_contributions: list[Mapping[str, Any]] = []
    traces: list[Mapping[str, Any]] = []
    watchlist: list[Mapping[str, Any]] = []
    operator_rows: list[Mapping[str, Any]] = []
    provider_results: list[Mapping[str, Any]] = []
    for row, event in event_rows:
        events.append(event)
        planner_run = dict(planner_by_event_id[event["candidate_event_id"]])
        plan = planner_run["output"]
        planner_runs.append(planner_run)
        task = _source_task_for_event(event, plan)
        source_tasks.append(task)
        document = _document_for_dart_row(row, event=event, as_of_date=as_of_date)
        anchor = _anchor_for_document(document, row)
        documents.append(document)
        anchors.append(anchor)
        provider_results.append(
            {
                "provider_name": "OpenDART",
                "source_class": "DART",
                "mode": "live",
                "request_id": document["provider_request_id"],
                "provider_request_id": document["provider_request_id"],
                "request_params": {"rcept_no": row["rcept_no"], "stock_code": row["stock_code"]},
                "status": "FETCHED",
                "canonical_url": document["canonical_url"],
                "official_document_id": row["rcept_no"],
                "published_at": document["published_at"],
                "available_at": document["available_at"],
                "fetched_at": document["fetched_at"],
                "content_hash": document["content_hash"],
                "raw_text": document["raw_text"],
                "structured_payload": dict(row),
                "provider_error": None,
            }
        )
        source_task_execution = {
            "task_id": task["task_id"],
            "source_task": task,
            "status": "NO_EVIDENCE_FOUND",
            "fetched_document_ids": [document["document_id"]],
            "document_urls": [document["canonical_url"]],
            "document_hashes": [document["content_hash"]],
            "evidence_anchor_ids": [anchor["anchor_id"]],
            "raw_assertion_ids": [],
            "adjudicated_claim_ids": [],
            "accepted_claim_ids": [],
            "provider_errors": [],
            "budget_used": {"queries": 1, "candidates": 1, "fetches": 1},
            "stop_reason": "no_contract_blind_claim",
        }
        assertion_records = extractor.extract(
            ExtractionInput(
                target_entity_id=f"TICKER:{event['symbol']}",
                target_aliases=(event["company_name"], event["symbol"]),
                as_of_date=as_of_date.isoformat(),
                document_id=document["document_id"],
                anchor_id=anchor["anchor_id"],
                source_text=document["raw_text"],
                source_metadata=document,
                extra_context={},
            )
        )
        accepted_claim_ids: list[str] = []
        task_accepted_claim_ids: list[str] = []
        contribution_rows: list[Mapping[str, Any]] = []
        for assertion in assertion_records:
            source_task_execution["raw_assertion_ids"].append(assertion.raw_assertion_id)
            adjudication = adjudicate_entity_temporal_scope(
                assertion,
                target_aliases=(event["company_name"], event["symbol"]),
                as_of_date=as_of_date,
                source_published_at=date.fromisoformat(document["published_at"]),
            )
            mapping = map_claim_to_primitive(assertion, adjudication, allowed_primitives=_ALLOWED_PRIMITIVES)
            claim_id = _stable_id("CLM", document["document_id"], anchor["anchor_id"], assertion.raw_assertion_id, mapping.primitive_id or "")
            source_task_execution["adjudicated_claim_ids"].append(claim_id)
            claim_row = {
                "claim_id": claim_id,
                "raw_assertion_id": assertion.raw_assertion_id,
                "document_id": document["document_id"],
                "anchor_id": anchor["anchor_id"],
                "quote_text": assertion.exact_quote,
                "source_url": document["canonical_url"],
                "source_provider": "OpenDART",
                "subject_entity_id": f"TICKER:{event['symbol']}",
                "target_entity_id": f"TICKER:{event['symbol']}",
                "target_scope_status": adjudication.target_scope_status,
                "directness": adjudication.directness,
                "temporal_status": adjudication.temporal_status,
                "polarity": adjudication.polarity,
                "semantic_status": adjudication.semantic_status,
                "event_date": assertion.event_date or document["published_at"],
                "as_of_date": as_of_date.isoformat(),
                "primitive_id": mapping.primitive_id,
                "mapping_status": mapping.mapping_status,
                "support_direction": mapping.support_direction,
                "score_eligible": mapping.mapping_status == "ACCEPTED" and adjudication.semantic_status == "PASS",
                "eligibility_reasons": list(adjudication.reasons),
                "adjudication": adjudication.to_dict(),
                "mapping": mapping.to_dict(),
                "satisfies_source_task": _claim_satisfies_source_task(mapping.primitive_id, task),
                "accepted": mapping.mapping_status == "ACCEPTED" and adjudication.semantic_status == "PASS",
            }
            claims.append(claim_row)
            if not claim_row["accepted"]:
                continue
            accepted_claim_ids.append(claim_id)
            if claim_row["satisfies_source_task"]:
                task_accepted_claim_ids.append(claim_id)
            primitive_states.append(
                {
                    "candidate_event_id": event["candidate_event_id"],
                    "primitive_id": mapping.primitive_id,
                    "status": "PRESENT_CURRENT",
                    "support_claim_ids": [claim_id],
                    "counter_claim_ids": [],
                    "freshness_days": max((as_of_date - date.fromisoformat(document["published_at"])).days, 0),
                }
            )
            contribution = _score_contribution_for_claim(mapping.primitive_id or "information_confidence", claim_id)
            if contribution is not None:
                contribution_rows.append(contribution)
                score_contributions.append(contribution)
        if task_accepted_claim_ids:
            source_task_execution["status"] = "EVIDENCE_OS_ACCEPTED"
            source_task_execution["accepted_claim_ids"] = task_accepted_claim_ids
            source_task_execution["score_claim_ids"] = accepted_claim_ids
            source_task_execution["baseline_claim_ids"] = [
                claim_id for claim_id in accepted_claim_ids if claim_id not in set(task_accepted_claim_ids)
            ]
            source_task_execution["stop_reason"] = "accepted_contract_blind_claim"
        elif accepted_claim_ids:
            source_task_execution["status"] = "EVIDENCE_OS_BASELINE_ONLY"
            source_task_execution["score_claim_ids"] = accepted_claim_ids
            source_task_execution["baseline_claim_ids"] = accepted_claim_ids
            source_task_execution["stop_reason"] = "accepted_baseline_claim_without_task_primitive"
        source_task_executions.append(source_task_execution)
        score_snapshot = _score_event(event=event, as_of_date=as_of_date, contributions=contribution_rows)
        trace = _stage_trace(event=event, score_snapshot=score_snapshot, accepted_claim_ids=accepted_claim_ids, contributions=contribution_rows)
        traces.append(trace)
        watch = _watchlist_row(
            event=event,
            planner_run=planner_run,
            source_task=task,
            execution=source_task_execution,
            score_snapshot=score_snapshot,
            trace=trace,
            accepted_claim_ids=accepted_claim_ids,
            contributions=contribution_rows,
        )
        watchlist.append(watch)
        operator_rows.append(_operator_row(watch))
    return OfficialLiveShadowData(
        registry=registry,
        candidate_events=tuple(events),
        planner_runs=tuple(planner_runs),
        source_tasks=tuple(source_tasks),
        source_task_executions=tuple(source_task_executions),
        evidence_documents=tuple(documents),
        evidence_anchors=tuple(anchors),
        evidence_claim_ledger=tuple(claims),
        primitive_states=tuple(primitive_states),
        score_contributions=tuple(score_contributions),
        stagecourt_traces=tuple(traces),
        daily_watchlist=tuple(watchlist),
        operator_digest_rows=tuple(operator_rows),
        provider_results=tuple(provider_results),
        source_corpus={"opendart_disclosure_rows": selected, "opendart_universe_count": registry.official_krx_universe_count},
    )


@lru_cache(maxsize=4)
def _fetch_opendart_universe() -> tuple[Mapping[str, Any], ...]:
    load_project_env()
    key = os.environ.get("OPENDART_API_KEY") or os.environ.get("OPEN_DART_API_KEY")
    if not key:
        raise RuntimeError("OPENDART_API_KEY is required for production_shadow_live")
    response = requests.get(_DART_CORP_CODE_URL, params={"crtfc_key": key}, timeout=30)
    response.raise_for_status()
    if response.content[:2] != b"PK":
        raise RuntimeError("OpenDART corpCode did not return a zip payload")
    archive = zipfile.ZipFile(io.BytesIO(response.content))
    root = ET.fromstring(archive.read(archive.namelist()[0]))
    rows = []
    for item in root.findall("list"):
        stock_code = (item.findtext("stock_code") or "").strip()
        if not stock_code:
            continue
        rows.append(
            {
                "symbol": stock_code,
                "company_name": (item.findtext("corp_name") or "").strip(),
                "corp_code": (item.findtext("corp_code") or "").strip(),
            }
        )
    return tuple(rows)


@lru_cache(maxsize=16)
def _fetch_opendart_disclosures(*, as_of_date: date, pages: int, page_count: int) -> tuple[Mapping[str, Any], ...]:
    load_project_env()
    key = os.environ.get("OPENDART_API_KEY") or os.environ.get("OPEN_DART_API_KEY")
    if not key:
        raise RuntimeError("OPENDART_API_KEY is required for production_shadow_live")
    start = as_of_date.replace(day=1).strftime("%Y%m%d")
    end = as_of_date.strftime("%Y%m%d")
    rows: list[Mapping[str, Any]] = []
    for page_no in range(1, pages + 1):
        response = requests.get(
            _DART_LIST_URL,
            params={
                "crtfc_key": key,
                "bgn_de": start,
                "end_de": end,
                "page_no": page_no,
                "page_count": page_count,
            },
            timeout=30,
        )
        response.raise_for_status()
        payload = response.json()
        if payload.get("status") != "000":
            raise RuntimeError(f"OpenDART list failed: {payload.get('status')} {payload.get('message')}")
        rows.extend(row for row in payload.get("list") or () if row.get("stock_code"))
    return tuple(rows)


@lru_cache(maxsize=4096)
def _fetch_opendart_company(corp_code: str) -> Mapping[str, Any]:
    load_project_env()
    key = os.environ.get("OPENDART_API_KEY") or os.environ.get("OPEN_DART_API_KEY")
    if not key:
        raise RuntimeError("OPENDART_API_KEY is required for production_shadow_live")
    response = requests.get(_DART_COMPANY_URL, params={"crtfc_key": key, "corp_code": corp_code}, timeout=30)
    response.raise_for_status()
    payload = response.json()
    if payload.get("status") != "000":
        raise RuntimeError(f"OpenDART company failed: {payload.get('status')} {payload.get('message')}")
    return payload


def _registry_from_dart_universe(rows: Sequence[Mapping[str, Any]]) -> InstrumentRegistry:
    names = {str(row["symbol"]): str(row["company_name"]) for row in rows if row.get("symbol")}
    return InstrumentRegistry(
        symbols=frozenset(names),
        names_by_symbol=names,
        official_krx_universe_count=len(names),
        combined_registry_count=len(names),
        source_paths=("OpenDART corpCode.xml live API",),
    )


def _select_disclosure_candidates(
    rows: Sequence[Mapping[str, Any]],
    *,
    candidate_min_count: int,
) -> tuple[Mapping[str, Any], ...]:
    keyed = [
        row
        for row in rows
        if any(keyword in str(row.get("report_nm") or "") for keyword in _DISCLOSURE_KEYWORDS)
    ]
    selected = keyed[: max(candidate_min_count, 50)]
    if len(selected) < candidate_min_count:
        selected.extend(row for row in rows if row not in selected)
    unique: dict[str, Mapping[str, Any]] = {}
    for row in selected:
        unique[str(row.get("rcept_no"))] = row
        if len(unique) >= candidate_min_count:
            break
    return tuple(unique.values())


def _candidate_event_from_dart_row(
    row: Mapping[str, Any],
    *,
    as_of_date: date,
    company_info: Mapping[str, Any],
) -> Mapping[str, Any]:
    symbol = str(row["stock_code"])
    company = str(row["corp_name"]).strip()
    rcept_no = str(row["rcept_no"]).strip()
    event_date = _date_from_yyyymmdd(str(row.get("rcept_dt") or as_of_date.strftime("%Y%m%d")))
    report_name = " ".join(str(row.get("report_nm") or "").split())
    industry_code = str(company_info.get("induty_code") or "").strip()
    sector = _large_sector_for_industry_code(industry_code)
    trigger_category = _trigger_category_for_dart_report(report_name)
    return {
        "candidate_event_id": f"CE-LIVE-DART-{symbol}-{rcept_no}",
        "symbol": symbol,
        "company_name": company,
        "corp_code": str(row.get("corp_code") or ""),
        "industry_code": industry_code,
        "large_sector_id": sector or "UNKNOWN_SECTOR",
        "sector_classification_status": "CLASSIFIED" if sector else "UNKNOWN_SECTOR_PROVIDER_GAP",
        "sector_classification_source": "OpenDART company.json induty_code",
        "event_date": event_date.isoformat(),
        "detected_at": as_of_date.isoformat(),
        "source_family": "DART",
        "source_id": _dart_url(rcept_no),
        "event_type": report_name,
        "event_title": report_name,
        "trigger_category": trigger_category,
        "score_eligibility_policy": _score_eligibility_policy_for_trigger(trigger_category),
        "event_summary": f"{company}({symbol}) OpenDART disclosure: {report_name}",
        "issuer_directness": "DIRECT",
        "raw_reason_codes": [report_name],
        "structured_payload": dict(row),
        "company_info_payload": {
            key: company_info.get(key)
            for key in ("corp_code", "corp_name", "stock_code", "induty_code", "hm_url", "ir_url")
        },
        "research_brain_eligible": True,
    }


def _planner_response_for_dart_event(event: Mapping[str, Any]) -> Mapping[str, Any]:
    primitive = _primitive_for_event_type(str(event.get("event_type") or ""))
    return {
        "top_k_archetype_hypotheses": [
            {"archetype_id": _DEFAULT_ARCHETYPE_ID, "probability_or_score": 0.62, "reason": "DART official disclosure event"}
        ],
        "positive_thesis": "Official disclosure may provide source-backed primitive evidence.",
        "counter_thesis": "Disclosure title alone is limited; score remains low unless accepted claim maps to a primitive.",
        "must_verify_primitives": [primitive],
        "green_blockers_to_close": ["cash_or_revision_conversion", "repeat_evidence_family"],
        "red_team_checks": ["wrong subject", "historical only", "provider failure"],
        "source_task_drafts": [
            {
                "primitive_gap": primitive,
                "preferred_source_classes": ["DART"],
                "fallback_source_classes": ["IssuerOfficial"],
                "max_queries": 1,
                "max_candidates": 1,
                "max_fetches": 1,
            }
        ],
        "query_intents": [f"verify DART disclosure {primitive}"],
        "do_not_promote_reasons": ["single disclosure title is not enough for Green"],
        "planner_self_check": {"score_keys_present": False, "stage_keys_present": False, "future_outcome_used": False},
    }


def _planner_runs_for_events(
    events: Sequence[Mapping[str, Any]],
    *,
    provider_mode: str,
    repo_root: Path,
) -> Mapping[str, Mapping[str, Any]]:
    normalized = str(provider_mode or "surrogate").strip().lower()
    if normalized in {"real", "codex", "codex_cli"}:
        return _real_codex_planner_runs_for_events(events, repo_root=repo_root)
    if normalized not in {"surrogate", "deterministic_surrogate", "test_surrogate"}:
        raise ValueError(f"unknown production cutover planner provider: {provider_mode}")
    rows: dict[str, Mapping[str, Any]] = {}
    for event in events:
        prompt = _planner_prompt_payload(tuple([event]))
        plan = _planner_response_for_dart_event(event)
        rows[str(event["candidate_event_id"])] = {
            "candidate_event_id": event["candidate_event_id"],
            "provider_name": "deterministic_surrogate_planner",
            "provider_mode": "surrogate",
            "real_provider_exercised": False,
            "real_provider_success": False,
            "fake_provider_used": True,
            "endpoint": "local-deterministic-surrogate",
            "model": "surrogate-not-llm",
            "command": "deterministic_surrogate_planner",
            "prompt_hash": stable_hash(prompt),
            "response_hash": stable_hash(plan),
            "raw_prompt_path": f"planner_raw/prompts/{event['candidate_event_id']}.json",
            "raw_response_path": f"planner_raw/responses/{event['candidate_event_id']}.json",
            "schema_validation_status": "SURROGATE_ONLY_NOT_PRODUCTION_READY",
            "rejected_by_validator": False,
            "latency_ms": 0,
            "provider_mode_label": "surrogate",
            "is_real_provider": False,
            "planner_output_score_stage_key_count": _count_forbidden_planner_keys(plan),
            "output": plan,
            "prompt_payload": prompt,
        }
    return rows


def _real_codex_planner_runs_for_events(
    events: Sequence[Mapping[str, Any]],
    *,
    repo_root: Path,
) -> Mapping[str, Mapping[str, Any]]:
    batch_size = _planner_batch_size()
    if len(events) > batch_size:
        merged: dict[str, Mapping[str, Any]] = {}
        for offset in range(0, len(events), batch_size):
            batch = tuple(events[offset : offset + batch_size])
            merged.update(_real_codex_planner_runs_for_events(batch, repo_root=repo_root))
        return merged

    load_project_env()
    prompt_payload = _planner_prompt_payload(events)
    prompt_text = _planner_prompt_text(prompt_payload)
    requested_model = (os.environ.get("E2R_CODEX_PLANNER_MODEL") or "").strip()
    model = requested_model or "codex-cli-default"
    command, output_path = _codex_planner_command(repo_root=repo_root, model=requested_model)
    started = time.monotonic()
    with tempfile.TemporaryDirectory(prefix="e2r_cutover_planner_") as tmpdir:
        tmp = Path(tmpdir)
        schema_path = tmp / "planner_schema.json"
        output_file = tmp / "planner_output.json"
        schema_path.write_text(json.dumps(_PLANNER_BATCH_OUTPUT_SCHEMA, ensure_ascii=False), encoding="utf-8")
        command, output_path = _codex_planner_command(repo_root=repo_root, model=requested_model, schema_path=schema_path, output_path=output_file)
        completed = _run_codex_command(command, prompt=prompt_text, timeout=_planner_timeout_seconds())
        raw = output_file.read_text(encoding="utf-8") if output_file.exists() else completed.stdout
    latency_ms = int((time.monotonic() - started) * 1000)
    if completed.returncode != 0 and not raw.strip():
        raise RuntimeError(_clean_planner_error(completed.stderr or completed.stdout or f"codex_cli_exit_{completed.returncode}"))
    payload = _json_object_from_text(raw)
    if payload is None:
        raise RuntimeError("codex planner returned non-json output")
    if _count_forbidden_planner_keys(payload):
        raise RuntimeError("codex planner output contains forbidden score/stage keys")
    prompt_hash = stable_hash(prompt_payload)
    response_hash = stable_hash(payload)
    by_event = {str(event["candidate_event_id"]): event for event in events}
    plans = {}
    raw_plans = {}
    for row in payload.get("plans") or ():
        if isinstance(row, Mapping) and row.get("candidate_event_id") in by_event:
            event_id = str(row["candidate_event_id"])
            raw_plans[event_id] = dict(row)
            plans[event_id] = _validated_planner_plan(row, by_event[event_id])
    missing = [event_id for event_id in by_event if event_id not in plans]
    if missing:
        raise RuntimeError(f"codex planner returned no valid plan for {len(missing)} candidate events")
    command_text = " ".join(shlex.quote(part) for part in command)
    return {
        event_id: {
            "candidate_event_id": event_id,
            "provider_name": "codex_cli_planner",
            "provider_mode": "real",
            "real_provider_exercised": True,
            "real_provider_success": True,
            "fake_provider_used": False,
            "endpoint": "codex-cli",
            "model": model,
            "requested_model": requested_model or None,
            "model_identity_status": "EXPLICIT_MODEL" if requested_model else "CODEX_CLI_DEFAULT_MODEL_NOT_PINNED",
            "command": command_text,
            "prompt_hash": stable_hash({"batch_prompt_hash": prompt_hash, "candidate_event_id": event_id}),
            "response_hash": stable_hash(plans[event_id]),
            "batch_prompt_hash": prompt_hash,
            "batch_response_hash": response_hash,
            "raw_prompt_path": f"planner_raw/prompts/{event_id}.json",
            "raw_response_path": f"planner_raw/responses/{event_id}.json",
            "schema_validation_status": "PASS",
            "rejected_by_validator": False,
            "latency_ms": latency_ms,
            "provider_mode_label": "real",
            "is_real_provider": True,
            "planner_output_score_stage_key_count": _count_forbidden_planner_keys(plans[event_id]),
            "output": plans[event_id],
            "raw_response_payload": raw_plans[event_id],
            "prompt_payload": {
                "batch_prompt_hash": prompt_hash,
                "candidate_event": by_event[event_id],
                "batch_rules": prompt_payload["rules"],
                "allowed_primitives": prompt_payload["allowed_primitives"],
            },
        }
        for event_id in by_event
    }


def _planner_prompt_payload(events: Sequence[Mapping[str, Any]]) -> Mapping[str, Any]:
    return {
        "schema_version": "production_cutover_real_planner_prompt_v1",
        "events": [
            {
                "candidate_event_id": event["candidate_event_id"],
                "symbol": event["symbol"],
                "company_name": event["company_name"],
                "event_date": event["event_date"],
                "source_family": event["source_family"],
                "event_type": event["event_type"],
                "event_title": event["event_title"],
                "event_summary": event["event_summary"],
                "large_sector_id": event.get("large_sector_id"),
                "industry_code": event.get("industry_code"),
                "issuer_directness": event.get("issuer_directness"),
            }
            for event in events
        ],
        "allowed_archetypes": [_DEFAULT_ARCHETYPE_ID],
        "allowed_primitives": list(_ALLOWED_PRIMITIVES),
        "allowed_source_classes": ["DART", "KIND", "KRX", "CompanyGuide", "IssuerIR", "IssuerOfficial", "TrustedNews"],
        "rules": [
            "Return exactly one plan per candidate_event_id.",
            "Keep each plan compact: choose one primitive_gap and one bounded source task.",
            "Plan source tasks only; do not output score, stage, hard_break, current_score_eligible, or feature_input.",
            "Use only allowed_primitives for primitive_gap.",
            "Set max_queries<=2, max_candidates<=10, max_fetches<=3.",
            "forbidden_source_classes must contain unbounded_general_search.",
            "Prefer official sources before TrustedNews.",
        ],
    }


def _planner_prompt_text(payload: Mapping[str, Any]) -> str:
    return "\n\n".join(
        [
            "You are the E2R Production Cutover Research Brain Planner.",
            "Your only job is to produce bounded SourceTask drafts for live official-source evidence acquisition.",
            "Do not score. Do not stage. Do not verify final claims. Do not mark current_score_eligible.",
            "Keep the JSON concise: one primitive_gap and one source task per candidate.",
            "Return one JSON object matching the supplied output schema.",
            json.dumps(payload, ensure_ascii=False, sort_keys=True),
        ]
    )


def _validated_planner_plan(row: Mapping[str, Any], event: Mapping[str, Any]) -> Mapping[str, Any]:
    if _count_forbidden_planner_keys(row):
        raise RuntimeError("planner plan contains forbidden score/stage keys")
    event_id = str(row.get("candidate_event_id") or "")
    if event_id != event["candidate_event_id"]:
        raise RuntimeError("planner plan candidate_event_id mismatch")
    primitive = str(row.get("primitive_gap") or "")
    if primitive not in _ALLOWED_PRIMITIVES:
        raise RuntimeError(f"planner plan for {event_id} has no allowed primitive")
    max_queries = min(max(int(row.get("max_queries") or 1), 1), 2)
    max_candidates = min(max(int(row.get("max_candidates") or 1), 1), 10)
    max_fetches = min(max(int(row.get("max_fetches") or 1), 1), 3)
    forbidden = tuple(str(item) for item in row.get("forbidden_source_classes") or ())
    if "unbounded_general_search" not in forbidden:
        raise RuntimeError(f"planner plan for {event_id} missing unbounded_general_search guard")
    preferred = tuple(str(item) for item in row.get("preferred_source_classes") or ())
    if not preferred:
        raise RuntimeError(f"planner plan for {event_id} has no preferred_source_classes")
    draft = {
        "primitive_gap": primitive,
        "preferred_source_classes": list(preferred),
        "fallback_source_classes": [str(item) for item in row.get("fallback_source_classes") or ()],
        "forbidden_source_classes": list(forbidden),
        "max_queries": max_queries,
        "max_candidates": max_candidates,
        "max_fetches": max_fetches,
    }
    self_check = dict(row.get("planner_self_check") or {})
    if self_check.get("score_keys_present") or self_check.get("stage_keys_present") or self_check.get("future_outcome_used"):
        raise RuntimeError(f"planner self-check failed for {event_id}")
    return {
        "top_k_archetype_hypotheses": [
            {
                "archetype_id": str(row.get("archetype_id") or _DEFAULT_ARCHETYPE_ID),
                "probability_or_score": 0.5,
                "reason": str(row.get("rationale") or "LLM source-task planner selected this archetype"),
            }
        ],
        "positive_thesis": str(row.get("rationale") or "Official event needs source-backed verification."),
        "counter_thesis": "Single event evidence cannot promote stage without accepted claim coverage.",
        "must_verify_primitives": [primitive],
        "green_blockers_to_close": ["cash_or_revision_conversion", "repeat_evidence_family"],
        "red_team_checks": [str(item) for item in row.get("red_team_checks") or ()],
        "source_task_drafts": [draft],
        "query_intents": [f"verify {primitive} from official source"],
        "do_not_promote_reasons": ["single event evidence is not enough for Green"],
        "planner_self_check": {
            "score_keys_present": False,
            "stage_keys_present": False,
            "future_outcome_used": False,
        },
    }


def _codex_planner_command(
    *,
    repo_root: Path,
    model: str,
    schema_path: Path | None = None,
    output_path: Path | None = None,
) -> tuple[list[str], Path | None]:
    command = [
        os.environ.get("E2R_CODEX_PLANNER_COMMAND") or "codex",
        "--sandbox",
        os.environ.get("E2R_CODEX_PLANNER_SANDBOX") or "read-only",
        "--ask-for-approval",
        os.environ.get("E2R_CODEX_PLANNER_APPROVAL_POLICY") or "never",
        "exec",
        "--ephemeral",
        "-C",
        str(repo_root),
        "--color",
        "never",
    ]
    if schema_path is not None:
        command.extend(("--output-schema", str(schema_path)))
    if output_path is not None:
        command.extend(("-o", str(output_path)))
    if model:
        command.extend(("-m", model))
    extra = tuple(shlex.split(os.environ.get("E2R_CODEX_PLANNER_EXTRA_ARGS") or ""))
    command.extend(extra)
    command.append("-")
    return command, output_path


def _run_codex_command(command: Sequence[str], *, prompt: str, timeout: float) -> subprocess.CompletedProcess[str]:
    process = subprocess.Popen(
        list(command),
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        start_new_session=(os.name == "posix"),
    )
    try:
        stdout, stderr = process.communicate(prompt, timeout=timeout)
    except subprocess.TimeoutExpired:
        _terminate_process_tree(process)
        raise
    return subprocess.CompletedProcess(list(command), process.returncode, stdout, stderr)


def _terminate_process_tree(process: subprocess.Popen[str]) -> None:
    if process.poll() is not None:
        return
    if os.name == "posix":
        try:
            os.killpg(process.pid, signal.SIGTERM)
        except ProcessLookupError:
            return
        try:
            process.wait(timeout=5)
            return
        except subprocess.TimeoutExpired:
            try:
                os.killpg(process.pid, signal.SIGKILL)
            except ProcessLookupError:
                return
            process.wait(timeout=5)
            return
    process.kill()
    process.wait(timeout=5)


def _json_object_from_text(text: str) -> Mapping[str, Any] | None:
    clean = str(text).strip()
    if not clean:
        return None
    try:
        parsed = json.loads(clean)
        return parsed if isinstance(parsed, Mapping) else None
    except json.JSONDecodeError:
        pass
    decoder = json.JSONDecoder()
    for match in re.finditer(r"\{", clean):
        try:
            parsed, _ = decoder.raw_decode(clean[match.start() :])
        except json.JSONDecodeError:
            continue
        if isinstance(parsed, Mapping):
            return parsed
    return None


def _count_forbidden_planner_keys(value: object) -> int:
    if isinstance(value, Mapping):
        return sum(1 for key in value if str(key) in _FORBIDDEN_PLANNER_KEYS) + sum(
            _count_forbidden_planner_keys(item) for item in value.values()
        )
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return sum(_count_forbidden_planner_keys(item) for item in value)
    return 0


def _planner_timeout_seconds() -> float:
    try:
        return float(os.environ.get("E2R_CODEX_PLANNER_TIMEOUT_SECONDS") or 300.0)
    except ValueError:
        return 300.0


def _planner_batch_size() -> int:
    try:
        return max(int(os.environ.get("E2R_CODEX_PLANNER_BATCH_SIZE") or 50), 1)
    except ValueError:
        return 50


def _clean_planner_error(text: str) -> str:
    clean = re.sub(r"\s+", " ", str(text)).strip()
    if len(clean) <= 500:
        return clean or "codex_planner_error"
    return f"{clean[:240]} ... {clean[-240:]}"


def _source_task_for_event(event: Mapping[str, Any], plan: Mapping[str, Any]) -> Mapping[str, Any]:
    draft = dict((plan.get("source_task_drafts") or [{}])[0])
    primitive = str(draft.get("primitive_gap") or plan["must_verify_primitives"][0])
    return {
        "task_id": _stable_id("SRC-TASK", event["candidate_event_id"], primitive),
        "candidate_event_id": event["candidate_event_id"],
        "symbol": event["symbol"],
        "company_name": event["company_name"],
        "primitive_gap": primitive,
        "preferred_source_classes": list(draft.get("preferred_source_classes") or ["DART"]),
        "fallback_source_classes": list(draft.get("fallback_source_classes") or ["IssuerOfficial"]),
        "forbidden_source_classes": list(draft.get("forbidden_source_classes") or ["unbounded_general_search"]),
        "general_search_allowed": False,
        "max_queries": min(max(int(draft.get("max_queries") or 1), 1), 2),
        "max_candidates": min(max(int(draft.get("max_candidates") or 1), 1), 10),
        "max_fetches": min(max(int(draft.get("max_fetches") or 1), 1), 3),
        "stop_condition": {"accepted_claim_count": 1},
    }


def _claim_satisfies_source_task(primitive_id: str | None, task: Mapping[str, Any]) -> bool:
    task_primitive = str(task.get("primitive_gap") or "")
    return bool(primitive_id) and str(primitive_id) == task_primitive


def _document_for_dart_row(row: Mapping[str, Any], *, event: Mapping[str, Any], as_of_date: date) -> Mapping[str, Any]:
    rcept_no = str(row["rcept_no"]).strip()
    report_name = " ".join(str(row.get("report_nm") or "").split())
    published = _date_from_yyyymmdd(str(row.get("rcept_dt") or as_of_date.strftime("%Y%m%d")))
    raw_text = f"{event['company_name']}({event['symbol']}) {report_name} OpenDART 접수번호 {rcept_no} 접수일 {published.isoformat()}"
    content_hash = hashlib.sha256(json.dumps(dict(row), ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()
    return {
        "document_id": f"DOC-DART-{content_hash[:20]}",
        "provider_request_id": _stable_id("SRCREQ-DART", rcept_no),
        "canonical_url": _dart_url(rcept_no),
        "source_type": "API_RECORD",
        "source_name": "OpenDART",
        "official_document_id": rcept_no,
        "content_hash": content_hash,
        "published_at": published.isoformat(),
        "available_at": published.isoformat(),
        "fetched_at": datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "raw_text": raw_text,
        "structured_payload": dict(row),
        "mode": "live",
    }


def _anchor_for_document(document: Mapping[str, Any], row: Mapping[str, Any]) -> Mapping[str, Any]:
    anchor_id = _stable_id("ANCHOR-DART", document["document_id"], row["rcept_no"])
    return {
        "anchor_id": anchor_id,
        "document_id": document["document_id"],
        "anchor_type": "API_RECORD",
        "locator": f"opendart:list:{row['rcept_no']}",
        "exact_text": document["raw_text"],
        "normalized_value": dict(row),
        "anchor_verified": True,
    }


def _score_contribution_for_claim(primitive_id: str, claim_id: str) -> Mapping[str, Any] | None:
    component, points, max_points = {
        "contract_quality": ("earnings_visibility", 4.0, 20.0),
        "revenue_visibility_contract": ("earnings_visibility", 4.0, 20.0),
        "order_to_revenue_bridge": ("earnings_visibility", 4.0, 20.0),
        "capital_allocation_event": ("capital_allocation", 2.0, 5.0),
        "capacity_expansion": ("bottleneck_pricing", 3.0, 20.0),
        "capacity_precommitted": ("bottleneck_pricing", 3.0, 20.0),
    }.get(primitive_id, ("information_confidence", 1.0, 5.0))
    contribution = ScoreContributionV2.build(
        component_key=component,
        criterion_id=f"production_cutover_{primitive_id}",
        raw_points=points,
        max_points=max_points,
        support_claim_ids=(claim_id,),
        mapping_ids=(_stable_id("MAP", claim_id, primitive_id),),
        source_family_ids=(f"DART:{claim_id}",),
        rationale=f"OpenDART contract-blind assertion mapped to {primitive_id}",
    )
    return {
        "contribution_id": contribution.contribution_id,
        "component_key": contribution.component_key,
        "criterion_id": contribution.criterion_id,
        "raw_points": contribution.raw_points,
        "max_points": contribution.max_points,
        "support_claim_ids": list(contribution.support_claim_ids),
        "counter_claim_ids": list(contribution.counter_claim_ids),
        "mapping_ids": list(contribution.mapping_ids),
        "source_family_ids": list(contribution.source_family_ids),
        "rationale": contribution.rationale,
    }


def _score_event(
    *,
    event: Mapping[str, Any],
    as_of_date: date,
    contributions: Sequence[Mapping[str, Any]],
) -> Mapping[str, Any] | None:
    if not contributions:
        return None
    v2 = tuple(
        ScoreContributionV2.build(
            component_key=str(row["component_key"]),
            criterion_id=str(row["criterion_id"]),
            raw_points=float(row["raw_points"]),
            max_points=float(row["max_points"]),
            support_claim_ids=tuple(row["support_claim_ids"]),
            mapping_ids=tuple(row["mapping_ids"]),
            source_family_ids=tuple(row["source_family_ids"]),
            rationale=str(row["rationale"]),
        )
        for row in contributions
    )
    payload = ScoringPayload(
        symbol=str(event["symbol"]),
        as_of_date=as_of_date,
        components={component.key: 0.0 for component in CANONICAL_SCORE_COMPONENTS},
        evidence_ids=tuple(claim_id for row in contributions for claim_id in row["support_claim_ids"]),
        score_contributions_v2=v2,
        scoring_version="production-cutover-live-dart-shadow",
        large_sector_id=large_sector_for_archetype(_DEFAULT_ARCHETYPE_ID),
        canonical_archetype_id=_DEFAULT_ARCHETYPE_ID,
    )
    snapshot = DeterministicScorer().score(payload)
    return {
        "total_score": snapshot.total_score,
        "components": {
            "eps_fcf_explosion": snapshot.eps_fcf_explosion_score,
            "earnings_visibility": snapshot.earnings_visibility_score,
            "bottleneck_pricing": snapshot.bottleneck_pricing_score,
            "market_mispricing": snapshot.market_mispricing_score,
            "valuation_rerating": snapshot.valuation_rerating_score,
            "capital_allocation": snapshot.capital_allocation_score,
            "information_confidence": snapshot.information_confidence_score,
        },
        "score_contribution_ledger": snapshot.score_contribution_ledger,
    }


def _stage_trace(
    *,
    event: Mapping[str, Any],
    score_snapshot: Mapping[str, Any] | None,
    accepted_claim_ids: Sequence[str],
    contributions: Sequence[Mapping[str, Any]],
) -> Mapping[str, Any]:
    score = float(score_snapshot["total_score"]) if score_snapshot else None
    status = "FINAL_WITH_NONMATERIAL_GAPS" if score is not None and score < 10.0 else "PENDING_MATERIAL_GAPS"
    stage = "1" if score is not None and score > 0.0 else "0"
    return {
        "candidate_event_id": event["candidate_event_id"],
        "score_interval": {"lower": score, "upper": score},
        "score_status": status if score is not None else "PENDING_MATERIAL_GAPS",
        "base_stage": stage,
        "missing_green_primitives": ["repeat_evidence_family", "cash_or_revision_conversion"],
        "missing_yellow_primitives": ["multi_source_confirmation"],
        "hard_break_status": "NONE",
        "score_contribution_ids": [row["contribution_id"] for row in contributions],
        "accepted_claim_ids": list(accepted_claim_ids),
        "stage_decision_reason": "low claim-backed official disclosure score; no Green/Yellow bridge",
    }


def _watchlist_row(
    *,
    event: Mapping[str, Any],
    planner_run: Mapping[str, Any],
    source_task: Mapping[str, Any],
    execution: Mapping[str, Any],
    score_snapshot: Mapping[str, Any] | None,
    trace: Mapping[str, Any],
    accepted_claim_ids: Sequence[str],
    contributions: Sequence[Mapping[str, Any]],
) -> Mapping[str, Any]:
    verified_score = score_snapshot["total_score"] if score_snapshot else None
    return {
        "candidate_event_id": event["candidate_event_id"],
        "symbol": event["symbol"],
        "company_name": event["company_name"],
        "event_type": event["event_type"],
        "event_summary": event["event_summary"],
        "event_source": event["source_id"],
        "primary_archetype": _DEFAULT_ARCHETYPE_ID,
        "secondary_archetypes": [],
        "planner_provider": planner_run["provider_name"],
        "planner_real_provider": True,
        "research_memory_cards_used": [],
        "source_tasks": [source_task],
        "source_task_executions": [execution],
        "accepted_claim_ids": list(accepted_claim_ids),
        "top_supporting_claims": list(accepted_claim_ids[:5]),
        "score_contribution_ids": [row["contribution_id"] for row in contributions],
        "verified_score": verified_score,
        "provisional_score": None,
        "score_interval_lower": trace["score_interval"]["lower"],
        "score_interval_upper": trace["score_interval"]["upper"],
        "score_valid_status": trace["score_status"],
        "base_stage": trace["base_stage"],
        "investigation_status": "COMPLETE" if verified_score is not None else "PENDING",
        "transition_overlay": "NONE",
        "failed_stage_gates": ["missing_green_bridge"],
        "green_blockers": trace["missing_green_primitives"],
        "red_team_checks": ["wrong subject", "historical only", "provider failure"],
        "do_not_promote_reasons": ["single official disclosure is not enough for Green"],
        "follow_up_tasks": [] if verified_score is not None else [source_task],
        "operator_notes": "Official disclosure was scored only as low-stage monitoring evidence; 투자 권고가 아니다.",
        "stage_court_trace": trace,
    }


def _operator_row(watch: Mapping[str, Any]) -> Mapping[str, Any]:
    pending = watch["verified_score"] is None or watch["score_valid_status"] == "PENDING_MATERIAL_GAPS"
    return {
        "candidate_event_id": watch["candidate_event_id"],
        "symbol": watch["symbol"],
        "company_name": watch["company_name"],
        "section": _operator_section_for_watch(watch),
        "why_triggered": watch["event_summary"],
        "primary_archetype": watch["primary_archetype"],
        "research_memory_cards_used": watch["research_memory_cards_used"],
        "accepted_claims": watch["accepted_claim_ids"],
        "score_contributions": watch["score_contribution_ids"],
        "missing_primitives": watch["green_blockers"],
        "next_source_tasks": watch["follow_up_tasks"],
        "red_team_checks": watch["red_team_checks"],
        "score_stage_validity": watch["score_valid_status"],
        "next_action": "RECHECK_SOURCE" if pending else "WATCH",
        "pending_reason": "material gaps remain" if pending else None,
    }


def _operator_section_for_watch(watch: Mapping[str, Any]) -> str:
    if watch.get("verified_score") is None:
        return "Planner Pending"
    stage = str(watch.get("base_stage") or "")
    if stage == "0":
        return "NoCurrentCatalyst"
    if stage == "1":
        return "Stage1-Watch"
    if stage == "2":
        return "Stage2-Watch"
    if stage == "2-Actionable":
        return "Stage2-Actionable"
    if stage == "3-Yellow":
        return "Stage3-Yellow-Pending"
    if stage == "3-Green":
        return "Stage3-Green"
    if stage in {"3-Red", "4C"}:
        return "Reject/Red"
    if stage == "4B":
        return "4B-watch"
    return "Runtime Budget Pending"


def _primitive_for_event_type(event_type: str) -> str:
    if "단일판매" in event_type or "공급계약" in event_type:
        return "contract_quality"
    if "신규시설투자" in event_type or "투자판단" in event_type:
        return "capacity_expansion"
    if "유상증자" in event_type or "자기주식" in event_type or "배당" in event_type:
        return "capital_allocation_event"
    return "information_confidence"


def _trigger_category_for_dart_report(report_name: str) -> str:
    if any(keyword in report_name for keyword in ("계약해지", "거래정지", "횡령", "배임", "감사의견", "의견거절", "상장폐지")):
        return "Official Risk Trigger"
    if any(keyword in report_name for keyword in ("단일판매", "공급계약", "잠정실적", "영업(잠정)실적", "신규시설투자", "투자판단", "유상증자", "자기주식", "배당")):
        return "Official Positive Trigger"
    return "Information Trigger"


def _score_eligibility_policy_for_trigger(trigger_category: str) -> str:
    if trigger_category == "Market Anomaly Trigger":
        return "investigation_only_never_score"
    return "accepted_claim_required"


def _date_from_yyyymmdd(value: str) -> date:
    clean = value.strip()
    return date(int(clean[:4]), int(clean[4:6]), int(clean[6:8]))


def _dart_url(rcept_no: str) -> str:
    return f"https://dart.fss.or.kr/dsaf001/main.do?rcpNo={rcept_no}"


def _large_sector_for_industry_code(industry_code: str) -> str | None:
    """Map official OpenDART/KSIC industry codes to broad E2R large sectors.

    The mapping is intentionally industry-code based, not symbol based. Easy
    example: a 66xxx code is finance regardless of the company name, while a
    58x code is software/content regardless of the disclosure title.
    """

    code = "".join(ch for ch in industry_code if ch.isdigit())
    if not code:
        return None
    first2 = code[:2]
    first3 = code[:3]
    first4 = code[:4]
    if first2 in {"64", "65", "66"}:
        return "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL"
    if first2 in {"58", "59", "60", "61", "62", "63"}:
        return "L8_PLATFORM_CONTENT_SW_SECURITY"
    if first2 in {"26"} or first3 in {"281", "282"}:
        return "L2_AI_SEMICONDUCTOR_ELECTRONICS"
    if first2 in {"17", "20", "21", "22", "24", "25"}:
        return "L4_MATERIALS_SPREAD_RESOURCE"
    if first2 in {"10", "11", "12", "13", "14", "15", "46", "47"}:
        return "L5_CONSUMER_BRAND_DISTRIBUTION"
    if first2 in {"28", "29", "33", "35", "36", "37", "38", "39", "42"} or first3 in {"721"}:
        return "L1_INDUSTRIALS_INFRA_DEFENSE_GRID"
    if first2 in {"23", "41", "68"}:
        return "L9_CONSTRUCTION_REALESTATE_HOUSING"
    if first2 in {"30", "31", "45", "49", "50", "51", "52", "76"}:
        return "L3_BATTERY_EV_GREEN_MOBILITY"
    if first3 in {"701"} or first2 in {"27", "86", "87"}:
        return "L7_BIO_HEALTHCARE_MEDICAL"
    if first3 in {"715"}:
        return "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL"
    if first2 in {"32", "90", "91"}:
        return "L5_CONSUMER_BRAND_DISTRIBUTION"
    if first2 in {"73"}:
        return "L10_POLICY_EVENT_CROSS_REDTEAM_MISC"
    if first4 in {"8411"} or first2 in {"84"}:
        return "L10_POLICY_EVENT_CROSS_REDTEAM_MISC"
    return None


def _stable_id(prefix: str, *parts: object) -> str:
    digest = hashlib.sha256("|".join(str(part) for part in parts).encode("utf-8")).hexdigest()[:20]
    return f"{prefix}-{digest}"


__all__ = ["OfficialLiveShadowData", "build_official_live_shadow_data"]
