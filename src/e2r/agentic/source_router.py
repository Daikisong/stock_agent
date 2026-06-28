"""Bounded source routing helpers for Evidence OS v2."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
import re
from typing import Mapping, Sequence

from .evidence_os import SourceAcquisitionTask, SourceType


@dataclass(frozen=True)
class SourceCandidate:
    candidate_id: str
    source_family_id: str
    source_type: SourceType
    tier: int
    url: str | None = None
    title: str = ""
    snippet: str = ""
    published_at: date | None = None
    date_verified: bool = False
    green_allowed_by_date: bool = False
    official: bool = False
    detail_document: bool = False
    independent: bool = True
    underlying_event_id: str | None = None

    def __post_init__(self) -> None:
        if not self.candidate_id.strip():
            raise ValueError("candidate_id must be non-empty")
        if not self.source_family_id.strip():
            raise ValueError("source_family_id must be non-empty")
        if self.tier <= 0:
            raise ValueError("tier must be positive")


@dataclass(frozen=True)
class SourceRoutePlan:
    task: SourceAcquisitionTask
    selected_candidates: tuple[SourceCandidate, ...]
    skipped_candidate_ids: tuple[str, ...]
    skipped_candidates: tuple[SourceCandidate, ...] = field(default_factory=tuple)
    stop_reason: str | None = None
    skipped_candidate_reasons: Mapping[str, str] = field(default_factory=dict)

    @property
    def stop_condition_satisfied(self) -> bool:
        return self.stop_reason is not None


def build_source_route_plan(
    *,
    task: SourceAcquisitionTask,
    candidates: Sequence[SourceCandidate],
) -> SourceRoutePlan:
    """Select bounded fetch candidates with official-first dedupe.

    The router dedupes by source_family_id before applying fetch limits, so a
    wire story reposted twenty times cannot consume the whole fetch budget.
    """

    if task.max_candidates <= 0 or task.max_fetches <= 0:
        raise ValueError("task budgets must be positive")
    skipped_reasons: dict[str, str] = {}
    scoped_candidates: list[SourceCandidate] = []
    for candidate in candidates:
        if _candidate_in_date_window(task, candidate):
            scoped_candidates.append(candidate)
        else:
            skipped_reasons[candidate.candidate_id] = "outside_task_date_window"
    ranked = sorted(scoped_candidates, key=lambda candidate: _candidate_rank(task, candidate))
    best_by_family: dict[str, SourceCandidate] = {}
    for candidate in ranked:
        existing = best_by_family.get(candidate.source_family_id)
        if existing is None or _candidate_rank(task, candidate) < _candidate_rank(task, existing):
            if existing is not None:
                skipped_reasons[existing.candidate_id] = "deduped_source_family"
            best_by_family[candidate.source_family_id] = candidate
        else:
            skipped_reasons[candidate.candidate_id] = "deduped_source_family"
    deduped = sorted(best_by_family.values(), key=lambda candidate: _candidate_rank(task, candidate))
    fetchable: list[SourceCandidate] = []
    for candidate in deduped:
        blocked_reason = _candidate_fetch_block_reason(task, candidate)
        if blocked_reason is None:
            fetchable.append(candidate)
        else:
            skipped_reasons[candidate.candidate_id] = blocked_reason
    considered = tuple(fetchable[: task.max_candidates])
    for candidate in fetchable[task.max_candidates :]:
        skipped_reasons[candidate.candidate_id] = "candidate_limit_reached"
    selected_list: list[SourceCandidate] = []
    stop_reason: str | None = None
    for candidate in considered:
        if stop_reason is not None:
            skipped_reasons[candidate.candidate_id] = f"stop_condition_satisfied:{stop_reason}"
            continue
        if len(selected_list) >= task.max_fetches:
            skipped_reasons[candidate.candidate_id] = "fetch_limit_reached"
            continue
        selected_list.append(candidate)
        stop_reason = _route_stop_reason(task, selected_list)
    selected = tuple(selected_list)
    selected_ids = {candidate.candidate_id for candidate in selected}
    for candidate in candidates:
        if candidate.candidate_id not in selected_ids and candidate.candidate_id not in skipped_reasons:
            skipped_reasons[candidate.candidate_id] = "not_selected"
    skipped = tuple(
        candidate.candidate_id
        for candidate in candidates
        if candidate.candidate_id not in selected_ids
    )
    skipped_candidates = tuple(
        candidate
        for candidate in candidates
        if candidate.candidate_id not in selected_ids
    )
    return SourceRoutePlan(
        task=task,
        selected_candidates=selected,
        skipped_candidates=skipped_candidates,
        skipped_candidate_ids=skipped,
        stop_reason=stop_reason,
        skipped_candidate_reasons=dict(skipped_reasons),
    )


def _candidate_rank(task: SourceAcquisitionTask, candidate: SourceCandidate) -> tuple[int, int, int, int, int, int, int, int, int, str]:
    preferred_rank = _candidate_preferred_source_rank(task, candidate)
    quorum_rank = _candidate_quorum_rank(task, candidate)
    target_rank = _candidate_target_relevance_rank(task, candidate)
    relevance_rank = _candidate_relevance_rank(task, candidate)
    date_rank = _candidate_date_rank(candidate)
    detail_rank = 0 if candidate.detail_document else 1
    official_rank = 0 if candidate.official else 1
    source_rank = _source_type_rank(candidate.source_type)
    if _task_requires_official_first(task):
        official_relevance_rank = _official_first_relevance_rank(candidate, relevance_rank=relevance_rank)
        return (
            official_relevance_rank,
            preferred_rank,
            quorum_rank,
            detail_rank,
            target_rank,
            relevance_rank,
            date_rank,
            candidate.tier,
            source_rank,
            candidate.candidate_id,
        )
    return (
        preferred_rank,
        quorum_rank,
        target_rank,
        relevance_rank,
        date_rank,
        detail_rank,
        official_rank,
        candidate.tier,
        source_rank,
        candidate.candidate_id,
    )


def _task_requires_official_first(task: SourceAcquisitionTask) -> bool:
    marker = task.stop_condition.casefold()
    return "first_official" in marker


def _route_stop_reason(task: SourceAcquisitionTask, selected: Sequence[SourceCandidate]) -> str | None:
    """Return a candidate-level stop reason when a task has enough sources.

    This is intentionally source-level only. It never says a primitive is
    proven; it only prevents more fetching when the task's declared source
    condition is already met by official or independent source families.
    Claim verification still happens later in the Evidence OS workflow.
    """

    if not selected:
        return None
    marker = " ".join(
        (
            task.required_source_tier or "",
            task.stop_condition,
            task.fallback_policy,
        )
    ).casefold()
    quorum_candidates = tuple(
        candidate for candidate in selected if _candidate_can_satisfy_source_quorum(task, candidate)
    )
    official_count = sum(1 for candidate in quorum_candidates if candidate.official)
    independent_tier2_count = sum(
        1
        for candidate in quorum_candidates
        if candidate.independent and candidate.tier <= 2
    )
    nonofficial_independent_tier2_count = sum(
        1
        for candidate in quorum_candidates
        if candidate.independent and not candidate.official and candidate.tier <= 2
    )
    if "first_official" in marker and official_count >= 1:
        return "first_official_candidate"
    if "official_first_then_stop" in marker and official_count >= 1:
        return "official_first_then_stop"
    if _task_has_structured_source_quorum(task):
        if (
            official_count >= task.source_quorum_min_official
            and independent_tier2_count >= task.source_quorum_min_independent_tier2
        ):
            return f"source_quorum_contract_{task.source_quorum_rule_id or 'task'}"
    if (
        "official_or_two_independent" in marker
        or "one_official_or_two_independent" in marker
        or "source_quorum" in marker
    ):
        if official_count >= 1:
            return "source_quorum_official"
        if nonofficial_independent_tier2_count >= 2:
            return "source_quorum_two_independent_tier2"
    return None


def _task_has_structured_source_quorum(task: SourceAcquisitionTask) -> bool:
    return task.source_quorum_min_official > 0 or task.source_quorum_min_independent_tier2 > 0


def _candidate_can_satisfy_source_quorum(task: SourceAcquisitionTask, candidate: SourceCandidate) -> bool:
    if _candidate_target_relevance_rank(task, candidate) >= 1:
        return False
    if _candidate_relevance_rank(task, candidate) >= 1:
        return False
    if _task_mentions_cash_bridge(task):
        if not _candidate_has_target_scoped_cash_bridge_signal(task, candidate):
            return False
    return True


def _candidate_fetch_block_reason(task: SourceAcquisitionTask, candidate: SourceCandidate) -> str | None:
    if _candidate_target_relevance_rank(task, candidate) >= 1:
        return "target_relevance_missing"
    if _is_cash_bridge_task(task):
        if not _candidate_has_cash_bridge_signal(candidate):
            return "cash_bridge_signal_missing"
        if not _candidate_has_target_scoped_cash_bridge_signal(task, candidate):
            return "target_scoped_cash_bridge_signal_missing"
    if not _task_requires_primitive_operating_signal(task):
        return None
    text = f"{candidate.title} {candidate.snippet} {candidate.url or ''}".casefold()
    if _task_primitive_operating_signal_count(task, text) <= 0:
        return "primitive_operating_signal_missing"
    if _is_memory_price_gap(task.primitive_gap) and _price_outlook_without_realized_signal(text):
        return "forward_looking_price_outlook_without_realized_signal"
    if _candidate_relevance_rank(task, candidate) >= 1:
        return "primitive_relevance_missing"
    return None


def _candidate_preferred_source_rank(task: SourceAcquisitionTask, candidate: SourceCandidate) -> int:
    preferred = _preferred_source_types(task)
    if not preferred:
        return 0
    return 0 if candidate.source_type in preferred else 1


def _preferred_source_types(task: SourceAcquisitionTask) -> frozenset[SourceType]:
    types: set[SourceType] = set()
    for item in task.preferred_source_classes:
        normalized = _normalize_source_class(item)
        if normalized is not None:
            types.add(normalized)
    return frozenset(types)


def _normalize_source_class(value: str) -> SourceType | None:
    token = str(value or "").strip().upper().replace("-", "_").replace(" ", "_")
    aliases = {
        "DISCLOSURE": SourceType.FILING,
        "DART": SourceType.FILING,
        "OPENDART": SourceType.FILING,
        "FILING": SourceType.FILING,
        "IR": SourceType.IR,
        "INVESTOR_RELATIONS": SourceType.IR,
        "NEWS": SourceType.NEWS,
        "ARTICLE": SourceType.NEWS,
        "RESEARCH": SourceType.RESEARCH_REPORT,
        "REPORT": SourceType.RESEARCH_REPORT,
        "RESEARCH_REPORT": SourceType.RESEARCH_REPORT,
        "ANALYST_REPORT": SourceType.RESEARCH_REPORT,
        "XBRL": SourceType.XBRL,
        "API": SourceType.API,
        "OTHER": SourceType.OTHER,
    }
    return aliases.get(token)


def _candidate_quorum_rank(task: SourceAcquisitionTask, candidate: SourceCandidate) -> int:
    """Prefer candidates that can satisfy the structured source quorum.

    For example, a C06 green-gate task requires independent tier-2 evidence and
    does not require an official filing. In that case, two routine DART rows
    must not consume the fetch budget before a relevant report/news candidate.
    Claim validity is still decided later by the Evidence OS.
    """

    if not _task_has_structured_source_quorum(task):
        return 0
    if _task_mentions_cash_bridge(task) and not _candidate_has_target_scoped_cash_bridge_signal(task, candidate):
        return 1
    contributes_official = candidate.official
    contributes_independent = candidate.independent and candidate.tier <= 2
    requires_official = task.source_quorum_min_official > 0
    requires_independent = task.source_quorum_min_independent_tier2 > 0
    if requires_independent and not requires_official:
        return 0 if contributes_independent else 1
    if requires_official and not requires_independent:
        return 0 if contributes_official else 1
    if requires_official and requires_independent:
        if contributes_official or contributes_independent:
            return 0
        return 1
    return 0


def _official_first_relevance_rank(candidate: SourceCandidate, *, relevance_rank: int) -> int:
    relevant = relevance_rank < 1
    if candidate.official and relevant:
        return 0
    if relevant:
        return 1
    if candidate.official:
        return 2
    return 3


def _candidate_in_date_window(task: SourceAcquisitionTask, candidate: SourceCandidate) -> bool:
    if candidate.published_at is None or task.date_window is None:
        return True
    start, end = task.date_window
    if start is not None and candidate.published_at < start:
        return False
    if end is not None and candidate.published_at > end:
        return False
    return True


def _candidate_date_rank(candidate: SourceCandidate) -> int:
    if candidate.date_verified and candidate.green_allowed_by_date:
        return 0
    if candidate.date_verified:
        return 1
    if candidate.published_at is not None:
        return 2
    return 3


def candidate_target_alias_count(task: SourceAcquisitionTask, candidate: SourceCandidate) -> int:
    return _candidate_target_alias_count(task, candidate)


def candidate_target_alias_present(task: SourceAcquisitionTask, candidate: SourceCandidate) -> bool:
    return _candidate_target_relevance_rank(task, candidate) < 1


def _candidate_target_relevance_rank(task: SourceAcquisitionTask, candidate: SourceCandidate) -> int:
    aliases = _target_alias_terms(task)
    if not aliases:
        return 0
    return 0 if _candidate_target_alias_count(task, candidate) > 0 else 1


def _candidate_target_alias_count(task: SourceAcquisitionTask, candidate: SourceCandidate) -> int:
    aliases = _target_alias_terms(task)
    if not aliases:
        return 0
    marker = _candidate_marker(candidate)
    compact_marker = _compact_text(marker)
    return sum(
        1
        for alias in aliases
        if alias in marker or _compact_text(alias) in compact_marker
    )


def _target_alias_terms(task: SourceAcquisitionTask) -> tuple[str, ...]:
    if not task.target_aliases:
        return ()
    raw_aliases = [*task.target_aliases]
    target = str(task.target_entity_id or "").strip()
    if target:
        raw_aliases.append(target)
        tail = re.split(r"[:|/]", target)[-1].strip()
        if tail and tail != target:
            raw_aliases.append(tail)
    terms: list[str] = []
    seen: set[str] = set()
    for item in raw_aliases:
        term = str(item or "").casefold().strip()
        compact = _compact_text(term)
        if len(compact) < 3:
            continue
        if term not in seen:
            seen.add(term)
            terms.append(term)
    return tuple(terms)


def _candidate_marker(candidate: SourceCandidate) -> str:
    return f"{candidate.title} {candidate.snippet} {candidate.url or ''}".casefold()


def _compact_text(text: str) -> str:
    return re.sub(r"[\s\-_/.,:;()]+", "", str(text or "").casefold())


def _candidate_relevance_rank(task: SourceAcquisitionTask, candidate: SourceCandidate) -> int:
    terms = _primitive_gap_terms(task.primitive_gap, primitive_aliases=task.primitive_aliases)
    if not terms:
        return 0
    text = _candidate_marker(candidate)
    if _is_cash_bridge_task(task):
        cash_match_count = _candidate_target_scoped_cash_bridge_signal_count(task, candidate)
        if cash_match_count <= 0:
            return 1
        return -cash_match_count
    operating_signal_count = _task_primitive_operating_signal_count(task, text)
    if _task_requires_primitive_operating_signal(task) and operating_signal_count <= 0:
        return 1
    match_count = sum(1 for term in terms if term in text)
    if match_count <= 0:
        return 1
    return -(match_count + operating_signal_count)


def _is_cash_bridge_task(task: SourceAcquisitionTask) -> bool:
    marker = " ".join(
        (
            task.primitive_gap,
            task.stop_condition,
            task.fallback_policy,
        )
    ).casefold()
    if any(
        token in marker
        for token in (
            "emerging_theme",
            "theme_to_revenue",
            "green_unlock",
            "theme_overheat",
            "non_price_bridge",
        )
    ):
        return False
    return any(token in marker for token in ("cash_or_revision_conversion", "selected_fcf_source_missing", "fcf"))


def _task_mentions_cash_bridge(task: SourceAcquisitionTask) -> bool:
    marker = " ".join(
        (
            task.primitive_gap,
            task.stop_condition,
            task.fallback_policy,
        )
    ).casefold()
    return any(
        token in marker
        for token in (
            "cash_or_revision_conversion",
            "selected_fcf_source_missing",
            "fcf",
            "free cash flow",
            "cash flow",
            "cash-flow",
            "cashflow",
            "현금흐름",
            "잉여현금",
        )
    )


def _candidate_has_cash_bridge_signal(candidate: SourceCandidate) -> bool:
    text = f"{candidate.title} {candidate.snippet} {candidate.url or ''}".casefold()
    return text_has_cash_bridge_signal(text)


def _candidate_has_target_scoped_cash_bridge_signal(
    task: SourceAcquisitionTask,
    candidate: SourceCandidate,
) -> bool:
    return _candidate_target_scoped_cash_bridge_signal_count(task, candidate) > 0


def _candidate_target_scoped_cash_bridge_signal_count(
    task: SourceAcquisitionTask,
    candidate: SourceCandidate,
) -> int:
    """Count cash bridge signals that are locally target-scoped.

    A research PDF titled with the target can still discuss a customer's FCF.
    For unstructured sources, the cash-flow phrase must be in a title/line/
    sentence that also names the target. Structured official sources are
    already target-scoped by their URL/source identity, so whole-candidate
    target + cash co-occurrence is enough there.
    """

    aliases = _target_alias_terms(task)
    marker = _candidate_marker(candidate)
    total_cash_signals = cash_bridge_signal_count(marker)
    if total_cash_signals <= 0:
        return 0
    if not aliases:
        return total_cash_signals
    if candidate.official or candidate.source_type in {SourceType.FILING, SourceType.XBRL, SourceType.API}:
        return total_cash_signals if _candidate_target_alias_count(task, candidate) > 0 else 0
    return sum(
        cash_bridge_signal_count(segment)
        for segment in _candidate_local_text_segments(candidate)
        if _text_has_any_target_alias(segment, aliases)
    )


def _candidate_local_text_segments(candidate: SourceCandidate) -> tuple[str, ...]:
    raw_parts = (
        candidate.title,
        candidate.snippet,
        candidate.url or "",
    )
    segments: list[str] = []
    for part in raw_parts:
        text = str(part or "").strip()
        if not text:
            continue
        pieces = re.split(r"[\n\r]|(?<=[.!?。！？])\s+", text)
        segments.extend(piece.strip() for piece in pieces if piece.strip())
    return tuple(segments)


def _text_has_any_target_alias(text: str, aliases: Sequence[str]) -> bool:
    marker = str(text or "").casefold()
    compact_marker = _compact_text(marker)
    return any(alias in marker or _compact_text(alias) in compact_marker for alias in aliases)


def text_has_cash_bridge_signal(text: str) -> bool:
    return cash_bridge_signal_count(text) > 0


def cash_bridge_signal_count(text: str) -> int:
    marker = str(text or "").casefold()
    spaced_marker = re.sub(r"[-_/]+", " ", marker)
    compact_marker = re.sub(r"[\s\-_/.,:;]+", "", marker)
    cash_terms = (
        "cash flow",
        "cashflow",
        "free cash flow",
        "fcf",
        "operating cash",
        "operating cash flow",
        "cash conversion",
        "cash-flow",
        "capex",
        "capital expenditure",
        "현금흐름",
        "영업현금",
        "영업활동현금",
        "잉여현금",
        "현금창출",
        "현금 전환",
        "현금전환",
        "설비투자",
    )
    compact_cash_terms = (
        "cashflow",
        "freecashflow",
        "operatingcash",
        "operatingcashflow",
        "cashconversion",
        "capitalexpenditure",
        "현금흐름",
        "영업현금",
        "영업현금흐름",
        "영업활동현금",
        "영업활동현금흐름",
        "잉여현금",
        "잉여현금흐름",
        "현금창출",
        "현금전환",
        "설비투자",
    )
    return (
        sum(1 for term in cash_terms if term in spaced_marker)
        + sum(1 for term in compact_cash_terms if term in compact_marker)
    )


def _cash_bridge_signal_count(text: str) -> int:
    return cash_bridge_signal_count(text)


def primitive_operating_signal_count(primitive_gap: str, text: str) -> int:
    return _primitive_operating_signal_count(primitive_gap, text)


def task_primitive_operating_signal_count(task: SourceAcquisitionTask, text: str) -> int:
    return _task_primitive_operating_signal_count(task, text)


def _task_primitive_operating_signal_count(task: SourceAcquisitionTask, text: str) -> int:
    return _primitive_operating_signal_count(task.primitive_gap, text) + _primitive_alias_signal_count(
        task.primitive_aliases,
        text,
    )


def _task_requires_primitive_operating_signal(task: SourceAcquisitionTask) -> bool:
    if _is_cash_bridge_task(task):
        return False
    primitive = task.primitive_gap.casefold()
    operating_primitives = (
        "customer_preorder_or_allocation",
        "hbm_capacity_pre_sold",
        "hbm_capacity_constraint",
        "qualification_status",
        "memory_price_increase_mentioned",
        "medium_term_revision_visibility",
        "selected_revision_source_missing",
        "consensus_revision",
        "revision_visibility",
        "earnings_revision",
        "estimate_revision",
        "target_price_change",
        "contract_visibility",
        "revenue_visibility_contract",
    )
    return any(token in primitive for token in operating_primitives)


def _primitive_operating_signal_count(primitive_gap: str, text: str) -> int:
    primitive = primitive_gap.casefold()
    marker = str(text or "").casefold()
    compact_marker = re.sub(r"[\s\-_/.,:;]+", "", marker)
    phrases: tuple[str, ...] = ()
    compact_phrases: tuple[str, ...] = ()
    if "customer_preorder_or_allocation" in primitive:
        phrases = (
            "customer allocation",
            "customer preorder",
            "booked capacity",
            "capacity allocation",
            "allocated capacity",
            "고객 배정",
            "고객사 배정",
            "고객 물량",
            "고객사 물량",
            "물량 배정",
            "예약 물량",
            "선주문",
            "선수주",
            "선수주 후증설",
            "선 수주",
            "수주 후 증설",
            "장기공급",
            "장기 공급",
        )
        compact_phrases = (
            "customerallocation",
            "customerpreorder",
            "bookedcapacity",
            "capacityallocation",
            "allocatedcapacity",
            "고객배정",
            "고객사배정",
            "고객물량",
            "고객사물량",
            "물량배정",
            "예약물량",
            "선수주",
            "선수주후증설",
            "수주후증설",
            "장기공급",
        )
    elif "hbm_capacity_pre_sold" in primitive:
        phrases = (
            "capacity sold out",
            "capacity pre-sold",
            "capacity pre sold",
            "pre-sold capacity",
            "pre sold capacity",
            "booked capacity",
            "capacity allocation",
            "allocated capacity",
            "customer allocation",
            "customer preorder",
            "물량 배정",
            "예약 물량",
            "물량 완판",
            "완판",
            "판매 완료",
            "선판매",
            "선수주",
            "선수주 후증설",
            "선 수주",
            "수주 후 증설",
        )
        compact_phrases = (
            "capacitysoldout",
            "capacitypresold",
            "presoldcapacity",
            "bookedcapacity",
            "capacityallocation",
            "allocatedcapacity",
            "customerallocation",
            "customerpreorder",
            "물량배정",
            "예약물량",
            "물량완판",
            "판매완료",
            "선수주",
            "선수주후증설",
            "수주후증설",
        )
    elif "hbm_capacity_constraint" in primitive:
        phrases = (
            "hbm capacity",
            "supply constraint",
            "capacity constraint",
            "shortage",
            "bottleneck",
            "생산능력",
            "공급능력",
            "공급 부족",
            "쇼티지",
            "병목",
        )
        compact_phrases = ("hbmcapacity", "supplyconstraint", "capacityconstraint", "생산능력", "공급능력", "공급부족")
    elif "qualification_status" in primitive:
        return _qualification_operating_signal_count(marker)
    elif "memory_price_increase_mentioned" in primitive:
        phrases = (
            "asp",
            "average selling price",
            "price increase",
            "price hike",
            "pricing up",
            "판가 상승",
            "판가 인상",
            "가격 인상",
            "가격 상승",
            "메모리 가격",
        )
        compact_phrases = ("averagesellingprice", "priceincrease", "pricehike", "pricingup", "판가상승", "판가인상", "가격인상", "가격상승", "메모리가격")
    elif (
        "medium_term_revision_visibility" in primitive
        or "selected_revision_source_missing" in primitive
        or "consensus_revision" in primitive
        or "revision_visibility" in primitive
        or "earnings_revision" in primitive
        or "estimate_revision" in primitive
        or "target_price_change" in primitive
    ):
        phrases = (
            "eps revision",
            "earnings revision",
            "estimate revision",
            "consensus revision",
            "target price revision",
            "target price raised",
            "raised target price",
            "raise estimates",
            "raised estimates",
            "estimate upgrade",
            "op revision",
            "operating profit revision",
            "broker target revision",
            "upward revision",
            "revision count",
            "컨센서스 상향",
            "컨센서스 조정",
            "실적 추정치 상향",
            "영업이익 추정치 상향",
            "eps 상향",
            "목표주가 상향",
            "추정치 상향",
            "이익 전망 상향",
            "실적 전망 상향",
        )
        compact_phrases = (
            "epsrevision",
            "earningsrevision",
            "estimaterevision",
            "consensusrevision",
            "targetpricerevision",
            "targetpriceraised",
            "raisedtargetprice",
            "raiseestimates",
            "raisedestimates",
            "estimateupgrade",
            "oprevision",
            "operatingprofitrevision",
            "brokertargetrevision",
            "upwardrevision",
            "revisioncount",
            "컨센서스상향",
            "컨센서스조정",
            "실적추정치상향",
            "영업이익추정치상향",
            "eps상향",
            "목표주가상향",
            "추정치상향",
            "이익전망상향",
            "실적전망상향",
        )
    elif "contract_visibility" in primitive or "revenue_visibility_contract" in primitive:
        phrases = (
            "contract",
            "long-term agreement",
            "long term agreement",
            "lta",
            "backlog",
            "order backlog",
            "revenue visibility",
            "계약",
            "장기공급",
            "장기 공급",
            "장기계약",
            "수주잔고",
            "매출 가시성",
        )
        compact_phrases = ("longtermagreement", "revenuevisibility", "orderbacklog", "장기공급", "장기계약", "수주잔고", "매출가시성")
    return _phrase_count(marker, phrases) + _phrase_count(compact_marker, compact_phrases)


_QUALIFICATION_STRONG_PHRASES = (
    "customer approval",
    "customer certification",
    "customer qualification",
    "customer validation",
    "nvidia approval",
    "nvidia qualification",
    "sample approval",
    "mass production approval",
    "mass-production approval",
    "approved for mass production",
    "passed qualification",
    "qualification passed",
    "qualification pass",
    "qualification test passed",
    "고객 인증",
    "고객 승인",
    "고객 검증",
    "양산 승인",
    "샘플 승인",
    "샘플 통과",
    "퀄 통과",
    "인증 통과",
    "엔비디아 인증",
    "엔비디아 승인",
    "품질 검증",
    "품질 테스트",
)
_QUALIFICATION_COMPACT_STRONG_PHRASES = tuple(_compact_text(item) for item in _QUALIFICATION_STRONG_PHRASES)
_QUALIFICATION_WORD_PATTERNS = (
    re.compile(r"\bqualification\b"),
    re.compile(r"\bqualified\b"),
    re.compile(r"\bqual\s+test\b"),
)
_QUALIFICATION_CONTEXT_MARKERS = (
    "customer",
    "nvidia",
    "sample",
    "mass production",
    "hbm3e",
    "hbm4",
    "product",
    "고객",
    "엔비디아",
    "샘플",
    "양산",
    "제품",
)
_QUALIFICATION_KOREAN_ACTION_MARKERS = (
    "퀄",
    "퀄리피케이션",
    "인증",
    "승인",
    "검증",
)
_QUALIFICATION_AUDIT_FALSE_POSITIVE_MARKERS = (
    "unqualified audit",
    "audit opinion",
    "감사의견",
)


def _qualification_operating_signal_count(text: str) -> int:
    marker = str(text or "").casefold()
    compact_marker = _compact_text(marker)
    if (
        any(item in marker for item in _QUALIFICATION_AUDIT_FALSE_POSITIVE_MARKERS)
        and not any(item in marker for item in ("customer approval", "nvidia qualification", "sample approval"))
        and not any(item in compact_marker for item in ("고객승인", "엔비디아인증", "샘플승인", "퀄통과"))
    ):
        return 0
    strong_hits = _phrase_count(marker, _QUALIFICATION_STRONG_PHRASES) + _phrase_count(
        compact_marker,
        _QUALIFICATION_COMPACT_STRONG_PHRASES,
    )
    word_hits = sum(1 for pattern in _QUALIFICATION_WORD_PATTERNS if pattern.search(marker))
    korean_action_hits = _phrase_count(marker, _QUALIFICATION_KOREAN_ACTION_MARKERS)
    context_hits = _phrase_count(marker, _QUALIFICATION_CONTEXT_MARKERS)
    if strong_hits:
        return strong_hits + context_hits
    if (word_hits or korean_action_hits) and context_hits:
        return word_hits + korean_action_hits + context_hits
    return 0


def _is_memory_price_gap(primitive_gap: str) -> bool:
    marker = str(primitive_gap or "").casefold()
    return any(token in marker for token in ("memory_price_increase_mentioned", "memory_price", "average_selling_price", "asp", "price_increase"))


_PRICE_OUTLOOK_MARKERS = (
    "outlook",
    "forecast",
    "expected",
    "expects",
    "likely",
    "potential",
    "possibility",
    "next year",
    "27f",
    "2027",
    "전망",
    "예상",
    "추정",
    "가능성",
    "내년",
    "27년",
)
_REALIZED_PRICE_SIGNAL_MARKERS = (
    "reported",
    "realized",
    "realised",
    "actual",
    "in the quarter",
    "during the quarter",
    "current quarter",
    "rose in the quarter",
    "increased in the quarter",
    "has risen",
    "has increased",
    "실현",
    "반영",
    "기록",
    "실적",
    "분기",
    "당분기",
    "상승했다",
    "상승함",
    "인상했다",
    "개선됐다",
    "확대됐다",
)


def _price_outlook_without_realized_signal(text: str) -> bool:
    marker = str(text or "").casefold()
    if not any(token in marker for token in _PRICE_OUTLOOK_MARKERS):
        return False
    return not any(token in marker for token in _REALIZED_PRICE_SIGNAL_MARKERS)


def _phrase_count(text: str, phrases: Sequence[str]) -> int:
    return sum(1 for phrase in phrases if phrase and phrase in text)


def _primitive_gap_terms(
    primitive_gap: str,
    *,
    primitive_aliases: Sequence[str] = (),
) -> tuple[str, ...]:
    terms = []
    for item in re.split(r"[^0-9A-Za-z가-힣]+", primitive_gap.casefold()):
        clean = item.strip()
        if len(clean) >= 3:
            terms.append(clean)
    terms.extend(_primitive_gap_term_aliases(tuple(terms)))
    terms.extend(_routing_primitive_aliases(primitive_aliases))
    return tuple(dict.fromkeys(terms))


def _primitive_alias_signal_count(primitive_aliases: Sequence[str], text: str) -> int:
    aliases = _routing_primitive_aliases(primitive_aliases)
    if not aliases:
        return 0
    marker = str(text or "").casefold()
    compact_marker = _compact_text(marker)
    return _phrase_count(marker, aliases) + _phrase_count(compact_marker, tuple(_compact_text(alias) for alias in aliases))


def _routing_primitive_aliases(primitive_aliases: Sequence[str]) -> tuple[str, ...]:
    aliases: list[str] = []
    for item in primitive_aliases:
        clean = str(item or "").casefold().strip()
        compact = _compact_text(clean)
        if len(compact) < 3:
            continue
        aliases.append(clean)
        if compact != clean:
            aliases.append(compact)
    return tuple(dict.fromkeys(aliases))


def _primitive_gap_term_aliases(terms: Sequence[str]) -> tuple[str, ...]:
    """Return routing-only vocabulary aliases for primitive gap terms.

    These aliases only affect which already-discovered candidate is fetched
    first. They do not create claims, primitive mappings, eligibility, scores,
    or stage decisions.
    """

    term_set = set(terms)
    aliases: list[str] = []
    if {"customer", "preorder", "allocation"} & term_set:
        aliases.extend(
            (
                "customer allocation",
                "customer preorder",
                "고객",
                "고객사",
                "물량 배정",
                "배정",
                "할당",
                "선주문",
                "예약",
            )
        )
    if {"capacity", "capa"} & term_set:
        aliases.extend(
            (
                "capacity",
                "capa",
                "production capacity",
                "생산능력",
                "공급능력",
                "캐파",
                "물량",
            )
        )
    if "sold" in term_set:
        aliases.extend(
            (
                "pre-sold",
                "pre sold",
                "sold-out",
                "sold out",
                "customer allocation",
                "customer preorder",
                "booked capacity",
                "capacity allocation",
                "allocated capacity",
                "완판",
                "선판매",
                "판매 완료",
                "판매완료",
                "물량 완판",
                "물량 배정",
                "고객 물량",
                "고객사 물량",
            )
        )
    if {"contract", "agreement", "lta"} & term_set:
        aliases.extend(
            (
                "long-term agreement",
                "long term agreement",
                "lta",
                "계약",
                "장기계약",
                "장기 공급",
                "장기공급",
                "장기공급계약",
            )
        )
    if "qualification" in term_set:
        aliases.extend(
            (
                "qualification",
                "qualified",
                "qual test",
                "nvidia qualification",
                "customer approval",
                "customer certification",
                "sample approval",
                "mass production approval",
                "인증",
                "퀄",
                "퀄리피케이션",
                "고객 인증",
                "고객 승인",
                "양산 승인",
                "샘플 승인",
            )
        )
    if {"revenue", "sales"} & term_set:
        aliases.extend(("revenue", "sales", "매출", "실적"))
    if "visibility" in term_set:
        aliases.extend(("visibility", "visible", "가시성"))
    if {"backlog", "rpo"} & term_set:
        aliases.extend(("backlog", "rpo", "order backlog", "수주잔고", "잔고"))
    if {"cash", "fcf"} & term_set:
        aliases.extend(("cash flow", "free cash flow", "fcf", "현금흐름", "잉여현금흐름"))
    if "margin" in term_set:
        aliases.extend(("margin", "spread", "opm", "마진", "스프레드", "영업이익률"))
    return tuple(dict.fromkeys(aliases))


def _source_type_rank(source_type: SourceType) -> int:
    order = {
        SourceType.FILING: 0,
        SourceType.XBRL: 1,
        SourceType.API: 2,
        SourceType.IR: 3,
        SourceType.RESEARCH_REPORT: 4,
        SourceType.NEWS: 5,
        SourceType.OTHER: 6,
    }
    return order[source_type]


__all__ = [
    "SourceCandidate",
    "SourceRoutePlan",
    "build_source_route_plan",
    "candidate_target_alias_count",
    "candidate_target_alias_present",
    "cash_bridge_signal_count",
    "primitive_operating_signal_count",
    "task_primitive_operating_signal_count",
    "text_has_cash_bridge_signal",
]
