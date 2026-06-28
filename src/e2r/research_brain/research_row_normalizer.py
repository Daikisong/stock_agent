"""Normalize raw research rows into ResearchMemoryRecord rows."""

from __future__ import annotations

import re
from typing import Any, Mapping, Sequence

from e2r.calibration.taxonomy import (
    CANONICAL_ARCHETYPE_IDS,
    large_sector_for_archetype,
    normalise_canonical_archetype_id,
    normalise_large_sector_id,
)
from e2r.research_brain.schemas import (
    LeakageControls,
    MemoryType,
    PriceOutcome,
    RawResearchRow,
    ResearchMemoryRecord,
    SourceQualityClass,
    deterministic_id,
)
from e2r.research_brain.source_quality_classifier import (
    classify_source_quality,
    first_url,
    source_url_status,
    usage_policy_for_quality,
)


_ARCHETYPE_RE = re.compile(r"\b(C\d{2}_[A-Za-z0-9_]+|R13_[A-Za-z0-9_]+)\b")
_SECTOR_RE = re.compile(r"\b(L\d{1,2}_[A-Za-z0-9_]+)\b")
_ROUND_RE = re.compile(r"\bR(?:ound)?[_\-\s]?(\d{1,4})\b", re.IGNORECASE)
_LOOP_RE = re.compile(r"\bloop[_\-\s]?(\d{1,4})\b", re.IGNORECASE)

_PRIMITIVE_KEYWORDS = {
    "hbm_capacity_pre_sold": ("sold-out", "sold out", "capacity allocated", "capacity allocation", "pre-sold", "선판매", "전량"),
    "customer_preorder_or_allocation": ("customer allocation", "preorder", "pre-order", "고객 배정", "qualification", "고객사"),
    "revenue_visibility_contract": ("contract", "backlog", "RPO", "수주잔고", "공급계약", "장기계약"),
    "cash_or_revision_conversion": ("fcf", "cashflow", "cash flow", "EPS revision", "컨센서스", "상향"),
    "realized_margin_bridge": ("OPM", "margin", "spread", "마진", "스프레드", "판가", "pass-through"),
    "regulatory_endpoint_bridge": ("endpoint", "approval", "regulatory", "clinical", "임상", "승인", "허가"),
    "retention_or_renewal_bridge": ("ARR", "RPO", "renewal", "retention", "churn", "갱신", "유지율"),
    "source_quorum": ("source quorum", "independent source", "official", "공식", "DART", "IR"),
}
_BRIDGE_KEYWORDS = {
    "cashflow_bridge": ("fcf", "cashflow", "cash flow", "현금흐름"),
    "margin_bridge": ("opm", "margin", "마진"),
    "contract_bridge": ("contract", "backlog", "rpo", "수주", "계약"),
    "customer_bridge": ("customer", "고객", "qualification"),
    "regulatory_bridge": ("approval", "regulatory", "clinical", "endpoint", "허가", "임상"),
    "retention_bridge": ("arr", "renewal", "retention", "churn", "갱신"),
}
_SOURCE_CLASS_KEYWORDS = {
    "DART": ("dart", "opendart", "공시", "사업보고서", "분기보고서", "xbrl"),
    "KIND": ("kind", "거래소"),
    "CompanyGuide": ("companyguide", "consensus", "컨센서스"),
    "IR": ("ir", "earnings call", "conference call", "실적발표", "presentation"),
    "Official": ("official", "issuer", "customer official", "regulator", "clinical registry", "공식"),
    "BrokerPDF": ("pdf", "report", "broker", "리포트"),
    "TrustedNews": ("reuters", "bloomberg", "trusted news", "news", "기사"),
}
_FALSE_POSITIVE_TERMS = (
    "false positive",
    "signboard",
    "keyword only",
    "sympathy",
    "weather",
    "profile only",
    "price-only",
    "가격만",
    "테마만",
)
_GREEN_BLOCKER_TERMS = ("green blocker", "green blocked", "blocks green", "green requires", "yellow", "보류")
_HARD_BREAK_TERMS = ("hard break", "4c", "thesis break", "cancellation", "failed", "failure", "취소", "실패")
_WATCH_TERMS = ("4b", "watch", "late phase", "drawdown", "peak", "고점", "watch")
_SOURCE_GAP_TERMS = ("source gap", "source_proxy_only", "evidence_url_pending", "url pending", "url repair")


def normalize_raw_research_row(row: RawResearchRow) -> tuple[ResearchMemoryRecord, ...]:
    text = _row_text(row)
    data = dict(row.data)
    archetype_id = _extract_archetype(data, text, row.source_artifact_path)
    if archetype_id is None:
        return ()
    large_sector_id = _extract_large_sector(data, text, archetype_id)
    quality = classify_source_quality(data, text)
    usage_policy = usage_policy_for_quality(quality)
    source_proxy_only = _boolish(data.get("source_proxy_only")) or "source_proxy_only" in text.lower()
    evidence_url_pending = _boolish(data.get("evidence_url_pending")) or "evidence_url_pending" in text.lower()
    source_url = first_url(data, text)
    memory_types = _infer_memory_types(data, text, quality)
    primitive_ids = _extract_primitives(data, text)
    required_bridges, missing_bridges = _extract_bridges(text)
    source_classes = _extract_source_classes(text, quality)
    forbidden_source_classes = _extract_forbidden_source_classes(text)
    price_outcome = _extract_price_outcome(data, text)
    leakage_controls = _leakage_controls_for(price_outcome, data, text)
    rows: list[ResearchMemoryRecord] = []
    for memory_type in memory_types:
        production_fixture = (
            memory_type == MemoryType.PRODUCTION_FIXTURE_CANDIDATE.value
            and quality == SourceQualityClass.A_URL_BACKED_REPLAY_READY
            and not source_proxy_only
            and not evidence_url_pending
        )
        fixture_usable = (
            memory_type in {MemoryType.REPLAY_FIXTURE_CANDIDATE.value, MemoryType.PRODUCTION_FIXTURE_CANDIDATE.value}
            and quality == SourceQualityClass.A_URL_BACKED_REPLAY_READY
            and not source_proxy_only
            and not evidence_url_pending
        )
        payload = {
            "source": row.stable_payload(),
            "memory_type": memory_type,
            "archetype_id": archetype_id,
            "source_quality": quality.value,
        }
        dedupe_key = deterministic_id("RMDEDUP", payload)
        record_id = deterministic_id("RMEM", {**payload, "dedupe_key": dedupe_key})
        rows.append(
            ResearchMemoryRecord(
                record_id=record_id,
                source_artifact_path=row.source_artifact_path,
                source_artifact_sha256=row.source_artifact_sha256,
                source_artifact_type=row.source_artifact_type,
                source_line_or_span=row.source_line_or_span,
                research_session=_as_text(data.get("research_session") or data.get("session")),
                mode=_as_text(data.get("mode")),
                round=_extract_round(data, text, row.source_artifact_path),
                loop=_extract_loop(data, text, row.source_artifact_path),
                large_sector_id=large_sector_id,
                canonical_archetype_id=archetype_id,
                fine_archetype_id=_as_text(data.get("fine_archetype_id")),
                row_type=_row_type(data, text),
                case_id=_as_text(data.get("case_id")),
                trigger_id=_as_text(data.get("trigger_id")),
                symbol=_as_text(data.get("symbol") or data.get("ticker")),
                company_name=_as_text(data.get("company_name") or data.get("company")),
                trigger_type=_as_text(data.get("trigger_type")),
                trigger_date=_as_text(data.get("trigger_date")),
                entry_date=_as_text(data.get("entry_date") or data.get("as_of_date")),
                memory_type=memory_type,
                positive_or_counterexample=_polarity(memory_type, text),
                stage_before=_as_text(data.get("stage_before")),
                stage_after=_as_text(data.get("stage_after") or data.get("stage")),
                expected_stage_effect=_expected_stage_effect(memory_type),
                primitive_ids=primitive_ids,
                required_bridges=required_bridges,
                missing_bridges=missing_bridges,
                green_blockers=_extract_pattern_list(text, _GREEN_BLOCKER_TERMS),
                guard_primitives=_extract_guard_primitives(text),
                hard_break_primitives=_extract_hard_break_primitives(text),
                false_positive_patterns=_extract_pattern_list(text, _FALSE_POSITIVE_TERMS),
                source_family=_source_family(data, text),
                source_url=source_url,
                source_quality=quality.name.lower(),
                source_quality_class=quality.value,
                evidence_url_status=source_url_status(data, text),
                source_proxy_only=source_proxy_only,
                evidence_url_pending=evidence_url_pending,
                production_ready_evidence=fixture_usable,
                fixture_usable=fixture_usable,
                ontology_usable=quality != SourceQualityClass.E_INVALID_OR_DUPLICATE,
                runtime_score_eligible=False,
                free_source_route_hints=source_classes,
                preferred_source_classes=source_classes or ("DART", "IR", "Official"),
                fallback_source_classes=_fallback_source_classes(source_classes),
                forbidden_source_classes=forbidden_source_classes,
                query_pattern_hints=_query_pattern_hints(text),
                bad_query_patterns=_bad_query_patterns(text),
                price_outcome=price_outcome,
                usage_policy=usage_policy,
                leakage_controls=leakage_controls,
                dedupe_key=dedupe_key,
                confidence=_confidence(quality, row.row_kind),
                notes=_notes(data, text, production_fixture),
            )
        )
    return tuple(rows)


def normalize_research_rows(rows: Sequence[RawResearchRow]) -> tuple[ResearchMemoryRecord, ...]:
    records: dict[str, ResearchMemoryRecord] = {}
    for row in rows:
        for record in normalize_raw_research_row(row):
            records.setdefault(record.record_id, record)
    return tuple(records.values())


def _row_text(row: RawResearchRow) -> str:
    try:
        data_text = " ".join(f"{key}={value}" for key, value in row.data.items())
    except Exception:
        data_text = str(row.data)
    return f"{row.source_artifact_path} {row.source_line_or_span} {data_text} {row.text}"


def _extract_archetype(data: Mapping[str, Any], text: str, path: str) -> str | None:
    for key in ("canonical_archetype_id", "archetype_id", "source_archetype_id"):
        value = normalise_canonical_archetype_id(data.get(key))
        if value in CANONICAL_ARCHETYPE_IDS:
            return value
    haystack = f"{path} {text}"
    match = _ARCHETYPE_RE.search(haystack)
    if match:
        value = normalise_canonical_archetype_id(match.group(1))
        if value in CANONICAL_ARCHETYPE_IDS:
            return value
    for archetype_id in CANONICAL_ARCHETYPE_IDS:
        if archetype_id in path:
            return archetype_id
    return None


def _extract_large_sector(data: Mapping[str, Any], text: str, archetype_id: str) -> str | None:
    for key in ("large_sector_id", "sector_id"):
        value = normalise_large_sector_id(data.get(key))
        if value:
            return value
    match = _SECTOR_RE.search(text)
    if match:
        value = normalise_large_sector_id(match.group(1))
        if value:
            return value
    return large_sector_for_archetype(archetype_id)


def _infer_memory_types(data: Mapping[str, Any], text: str, quality: SourceQualityClass) -> tuple[str, ...]:
    lower = text.lower()
    memory_types: list[str] = []
    if quality == SourceQualityClass.A_URL_BACKED_REPLAY_READY:
        memory_types.append(MemoryType.REPLAY_FIXTURE_CANDIDATE.value)
        memory_types.append(MemoryType.PRODUCTION_FIXTURE_CANDIDATE.value)
    if quality == SourceQualityClass.C_SOURCE_PROXY_ONTOLOGY_ONLY:
        memory_types.append(MemoryType.ONTOLOGY_ONLY_RULE_CANDIDATE.value)
    if quality == SourceQualityClass.D_PRICE_PATH_ONLY_OR_FUTURE_LEAKAGE_RISK:
        memory_types.append(MemoryType.SCORE_WEIGHT_SUPPORT.value)
    if any(term in lower for term in _SOURCE_GAP_TERMS):
        memory_types.append(MemoryType.SOURCE_GAP.value)
    if any(term in lower for term in _FALSE_POSITIVE_TERMS):
        memory_types.append(MemoryType.FALSE_POSITIVE_PATTERN.value)
        memory_types.append(MemoryType.COUNTEREXAMPLE.value)
    if any(term in lower for term in _GREEN_BLOCKER_TERMS):
        memory_types.append(MemoryType.GREEN_BLOCKER.value)
    if "yellow" in lower or "stage2 cap" in lower or "watch cap" in lower:
        memory_types.append(MemoryType.STAGE2_WATCH_CAP.value)
    if any(term in lower for term in _HARD_BREAK_TERMS):
        memory_types.append(MemoryType.HARD_BREAK_PATTERN.value)
        memory_types.append(MemoryType.FOUR_C_THESIS_BREAK_CONDITION.value)
    if any(term in lower for term in _WATCH_TERMS):
        memory_types.append(MemoryType.FOUR_B_WATCH_CONDITION.value)
    if any(token in lower for token in ("source route", "preferred source", "dart", "ir", "official", "reuters")):
        memory_types.append(MemoryType.SOURCE_ROUTE_PATTERN.value)
        memory_types.append(MemoryType.SOURCE_FAMILY_RELIABILITY.value)
    if any(token in lower for token in ("query", "검색어", "search")):
        memory_types.append(MemoryType.QUERY_SUCCESS_PATTERN.value)
    if any(token in lower for token in ("primitive", "required bridge", "evidence contract")):
        memory_types.append(MemoryType.EVIDENCE_CONTRACT_CANDIDATE.value)
    if not memory_types:
        memory_types.append(MemoryType.PRIMITIVE_PARTIAL_CASE.value)
    if any(token in lower for token in ("positive", "success", "green", "url_backed")):
        memory_types.append(MemoryType.PRIMITIVE_SUCCESS_CASE.value)
    if any(token in lower for token in ("failure", "failed", "blocked", "missing")):
        memory_types.append(MemoryType.PRIMITIVE_FAILURE_CASE.value)
    return tuple(dict.fromkeys(memory_types))


def _extract_primitives(data: Mapping[str, Any], text: str) -> tuple[str, ...]:
    values: list[str] = []
    raw = data.get("primitive_ids") or data.get("primitive_id")
    if isinstance(raw, str):
        values.extend([part.strip() for part in re.split(r"[,|]", raw) if part.strip()])
    elif isinstance(raw, Sequence) and not isinstance(raw, (str, bytes)):
        values.extend(str(item).strip() for item in raw if str(item).strip())
    lower = text.lower()
    for primitive_id, keywords in _PRIMITIVE_KEYWORDS.items():
        if any(keyword.lower() in lower for keyword in keywords):
            values.append(primitive_id)
    return tuple(dict.fromkeys(values))


def _extract_bridges(text: str) -> tuple[tuple[str, ...], tuple[str, ...]]:
    lower = text.lower()
    required: list[str] = []
    missing: list[str] = []
    for bridge, keywords in _BRIDGE_KEYWORDS.items():
        if any(keyword.lower() in lower for keyword in keywords):
            required.append(bridge)
            if any(token in lower for token in ("missing", "absent", "gap", "부족", "미확인")):
                missing.append(bridge)
    return tuple(dict.fromkeys(required)), tuple(dict.fromkeys(missing))


def _extract_source_classes(text: str, quality: SourceQualityClass) -> tuple[str, ...]:
    lower = text.lower()
    values = [source_class for source_class, keywords in _SOURCE_CLASS_KEYWORDS.items() if any(keyword.lower() in lower for keyword in keywords)]
    if not values and quality in {SourceQualityClass.A_URL_BACKED_REPLAY_READY, SourceQualityClass.B_URL_BACKED_REPAIR_NEEDED}:
        values.append("TrustedNews")
    return tuple(dict.fromkeys(values))


def _extract_forbidden_source_classes(text: str) -> tuple[str, ...]:
    lower = text.lower()
    values = ["unbounded_general_search"]
    if "fcf" in lower or "cashflow" in lower:
        values.append("NewsOnlyForFCF")
    if "source_proxy_only" in lower:
        values.append("ProductionScore")
    return tuple(dict.fromkeys(values))


def _fallback_source_classes(source_classes: Sequence[str]) -> tuple[str, ...]:
    if not source_classes:
        return ("TrustedNews",)
    fallback = [item for item in ("IR", "Official", "BrokerPDF", "TrustedNews") if item not in source_classes]
    return tuple(fallback[:2])


def _extract_price_outcome(data: Mapping[str, Any], text: str) -> PriceOutcome:
    def number(key: str) -> float | None:
        value = data.get(key)
        try:
            return float(value) if value is not None and value != "" else None
        except (TypeError, ValueError):
            return None

    lower = text.lower()
    return PriceOutcome(
        mfe_30d_pct=number("mfe_30d_pct"),
        mae_30d_pct=number("mae_30d_pct"),
        mfe_90d_pct=number("mfe_90d_pct"),
        mae_90d_pct=number("mae_90d_pct"),
        mfe_180d_pct=number("mfe_180d_pct"),
        mae_180d_pct=number("mae_180d_pct"),
        post_peak_drawdown_pct=number("post_peak_drawdown_pct"),
        corporate_action_contaminated=_boolish(data.get("corporate_action_contaminated")),
        future_outcome_zone=any(token in lower for token in ("mfe", "mae", "future_outcome", "outcome label", "post_peak")),
    )


def _leakage_controls_for(price_outcome: PriceOutcome, data: Mapping[str, Any], text: str) -> LeakageControls:
    lower = text.lower()
    contains_future = price_outcome.future_outcome_zone or any(token in lower for token in ("mfe", "mae", "future stage", "outcome label"))
    contains_stage = any(token in lower for token in ("future stage", "expected_stage", "stage_after"))
    return LeakageControls(
        contains_future_price_outcome=contains_future,
        contains_future_stage_label=contains_stage,
        may_be_seen_by_runtime_llm=False,
        may_be_seen_by_extractor_llm=False,
        may_be_seen_by_planner_llm_as_pattern_summary=True,
    )


def _extract_round(data: Mapping[str, Any], text: str, path: str) -> str | None:
    value = data.get("round")
    if value:
        return str(value)
    match = _ROUND_RE.search(f"{path} {text}")
    return f"R{match.group(1)}" if match else None


def _extract_loop(data: Mapping[str, Any], text: str, path: str) -> int | None:
    value = data.get("loop")
    try:
        return int(value) if value not in (None, "") else None
    except (TypeError, ValueError):
        pass
    match = _LOOP_RE.search(f"{path} {text}")
    return int(match.group(1)) if match else None


def _row_type(data: Mapping[str, Any], text: str) -> str:
    for key in ("row_type", "type"):
        if data.get(key):
            return str(data[key])
    lower = text.lower()
    if "shadow_weight" in lower:
        return "shadow_weight"
    if "score" in lower:
        return "score_simulation"
    if "trigger" in lower:
        return "trigger"
    if "price" in lower:
        return "price_source_validation"
    return "case"


def _source_family(data: Mapping[str, Any], text: str) -> str | None:
    for key in ("source_family", "source", "source_type"):
        if data.get(key):
            return str(data[key])
    classes = _extract_source_classes(text, SourceQualityClass.C_SOURCE_PROXY_ONTOLOGY_ONLY)
    return classes[0] if classes else None


def _extract_pattern_list(text: str, terms: Sequence[str]) -> tuple[str, ...]:
    lower = text.lower()
    return tuple(term for term in terms if term.lower() in lower)


def _extract_guard_primitives(text: str) -> tuple[str, ...]:
    values = []
    lower = text.lower()
    if any(token in lower for token in ("wrong subject", "타사", "peer", "industry")):
        values.append("target_scope_guard")
    if any(token in lower for token in ("date", "as_of", "stale", "historical", "과거")):
        values.append("temporal_lifecycle_guard")
    if any(token in lower for token in ("snippet", "source_proxy", "evidence_url_pending")):
        values.append("source_quality_guard")
    return tuple(values)


def _extract_hard_break_primitives(text: str) -> tuple[str, ...]:
    lower = text.lower()
    values = []
    if any(token in lower for token in ("accounting", "audit", "감사의견", "회계")):
        values.append("accounting_trust_break")
    if any(token in lower for token in ("cancellation", "cancelled", "취소")):
        values.append("contract_cancellation")
    if any(token in lower for token in ("clinical failure", "failed trial", "임상 실패")):
        values.append("clinical_binary_failure")
    return tuple(values)


def _query_pattern_hints(text: str) -> tuple[str, ...]:
    lower = text.lower()
    values = []
    if "earnings call" in lower:
        values.append("earnings_call_context_query")
    if "ir" in lower:
        values.append("issuer_ir_context_query")
    if "dart" in lower or "공시" in lower:
        values.append("official_disclosure_first")
    if "query" in lower or "검색" in lower:
        values.append("llm_generated_context_query")
    return tuple(dict.fromkeys(values))


def _bad_query_patterns(text: str) -> tuple[str, ...]:
    lower = text.lower()
    values = []
    if "keyword only" in lower or "signboard" in lower:
        values.append("theme_keyword_only_query")
    if "naver" in lower and ("fcf" in lower or "cashflow" in lower):
        values.append("news_only_cashflow_query")
    return tuple(values)


def _polarity(memory_type: str, text: str) -> str:
    if memory_type in {
        MemoryType.FALSE_POSITIVE_PATTERN.value,
        MemoryType.COUNTEREXAMPLE.value,
        MemoryType.HARD_BREAK_PATTERN.value,
        MemoryType.FOUR_C_THESIS_BREAK_CONDITION.value,
    }:
        return "guard"
    if memory_type in {MemoryType.PRIMITIVE_SUCCESS_CASE.value, MemoryType.STAGE2_ACTIONABLE_UNLOCK.value}:
        return "positive"
    if memory_type in {MemoryType.PRIMITIVE_FAILURE_CASE.value, MemoryType.SOURCE_GAP.value}:
        return "counterexample"
    if "mixed" in text.lower():
        return "mixed"
    return "unknown"


def _expected_stage_effect(memory_type: str) -> str:
    if memory_type == MemoryType.GREEN_BLOCKER.value:
        return "block_green_until_verified"
    if memory_type == MemoryType.STAGE2_ACTIONABLE_UNLOCK.value:
        return "unlock_stage2_actionable_if_evidence_os_accepts_claim"
    if memory_type == MemoryType.FOUR_C_THESIS_BREAK_CONDITION.value:
        return "check_current_hard_break_only"
    if memory_type == MemoryType.FALSE_POSITIVE_PATTERN.value:
        return "do_not_promote_without_bridge"
    return "planning_prior_only"


def _confidence(quality: SourceQualityClass, row_kind: str) -> str:
    if quality == SourceQualityClass.A_URL_BACKED_REPLAY_READY and row_kind in {"jsonl", "json", "csv"}:
        return "high"
    if quality in {SourceQualityClass.A_URL_BACKED_REPLAY_READY, SourceQualityClass.B_URL_BACKED_REPAIR_NEEDED}:
        return "medium"
    if quality == SourceQualityClass.E_INVALID_OR_DUPLICATE:
        return "low"
    return "medium"


def _notes(data: Mapping[str, Any], text: str, production_fixture: bool) -> str:
    if production_fixture:
        return "URL-backed replay candidate; still planning memory, not score input."
    if "source_proxy_only" in text.lower():
        return "source_proxy_only row is ontology/planning only."
    if "evidence_url_pending" in text.lower():
        return "evidence_url_pending row requires source repair before fixture use."
    return ""


def _as_text(value: Any) -> str | None:
    if value in (None, ""):
        return None
    return str(value)


def _boolish(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return value != 0
    if isinstance(value, str):
        return value.strip().lower() in {"1", "true", "yes", "y"}
    return False


__all__ = ["normalize_raw_research_row", "normalize_research_rows"]
