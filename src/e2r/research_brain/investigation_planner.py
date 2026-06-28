"""Investigation planning from memory profiles and candidate events."""

from __future__ import annotations

from typing import Iterable, Sequence

from e2r.calibration.taxonomy import CANONICAL_ARCHETYPE_IDS
from e2r.research_brain.memory_store import ResearchMemoryStore
from e2r.research_brain.schemas import (
    ArchetypeMemoryProfile,
    CandidateEvent,
    MemoryType,
    ResearchBrainPlan,
    SourceTask,
    SourceTaskType,
    deterministic_id,
)


_DEFAULT_PRIMITIVE_GAPS = (
    "contract_visibility",
    "cash_or_revision_conversion",
    "source_quorum",
)


def build_research_brain_plan(
    *,
    candidate_event: CandidateEvent,
    memory_store: ResearchMemoryStore,
    archetype_id: str | None = None,
    max_memory_patterns: int = 12,
) -> ResearchBrainPlan:
    primary = archetype_id or infer_archetype_hypothesis(candidate_event, memory_store)
    profile = memory_store.get_archetype_profile(primary)
    recalled = memory_store.query(archetype_id=primary, limit=max_memory_patterns)
    primitive_gaps = _primitive_gaps(profile)
    source_tasks = tuple(
        _source_task_for_gap(candidate_event, profile, gap, recalled)
        for gap in primitive_gaps[:6]
    )
    red_team = _red_team_checks(memory_store, primary)
    return ResearchBrainPlan(
        primary_archetype_hypothesis=primary,
        secondary_archetype_hypotheses=_secondary_hypotheses(primary, candidate_event, memory_store),
        positive_thesis=_positive_thesis(candidate_event, profile),
        counter_thesis=_counter_thesis(profile),
        recalled_memory_patterns=tuple(record.record_id for record in recalled),
        must_verify_primitives=tuple(primitive_gaps),
        green_blockers_to_close=profile.green_blockers,
        red_team_checks=red_team,
        source_tasks=source_tasks,
        query_suggestions=_query_suggestions(profile),
        do_not_promote_reasons=profile.false_positive_patterns,
        planning_confidence=_planning_confidence(profile),
    )


def infer_archetype_hypothesis(candidate_event: CandidateEvent, memory_store: ResearchMemoryStore) -> str:
    text = f"{candidate_event.event_type} {candidate_event.candidate_reason} {candidate_event.source_family}".lower()
    scores: dict[str, float] = {archetype_id: 0.0 for archetype_id in CANONICAL_ARCHETYPE_IDS}
    for archetype_id in CANONICAL_ARCHETYPE_IDS:
        profile = memory_store.get_archetype_profile(archetype_id)
        for token in tuple(profile.required_primitives_observed) + tuple(profile.source_routes):
            if token and token.lower() in text:
                scores[archetype_id] += 2.0
        scores[archetype_id] += min(profile.memory_record_count, 50) / 100.0
    if "supply_contract" in text or "contract" in text:
        _boost_by_tokens(scores, ("contract", "backlog", "order"))
    if "facility" in text:
        _boost_by_tokens(scores, ("capacity", "capa", "facility"))
    if "earnings" in text:
        _boost_by_tokens(scores, ("margin", "cash", "revision"))
    if "risk" in text:
        _boost_by_tokens(scores, ("hard_break", "guard", "risk"))
    return max(scores, key=lambda key: (scores[key], key))


def _boost_by_tokens(scores: dict[str, float], tokens: Iterable[str]) -> None:
    token_tuple = tuple(tokens)
    for archetype_id in scores:
        lower = archetype_id.lower()
        if any(token in lower for token in token_tuple):
            scores[archetype_id] += 5.0


def _secondary_hypotheses(
    primary: str,
    candidate_event: CandidateEvent,
    memory_store: ResearchMemoryStore,
    limit: int = 3,
) -> tuple[str, ...]:
    large_sector_id = memory_store.get_archetype_profile(primary).large_sector_id
    candidates = []
    for archetype_id in CANONICAL_ARCHETYPE_IDS:
        if archetype_id == primary:
            continue
        profile = memory_store.get_archetype_profile(archetype_id)
        if profile.large_sector_id == large_sector_id:
            candidates.append((profile.memory_record_count, archetype_id))
    candidates.sort(reverse=True)
    return tuple(archetype_id for _, archetype_id in candidates[:limit])


def _primitive_gaps(profile: ArchetypeMemoryProfile) -> tuple[str, ...]:
    values = list(profile.required_primitives_observed)
    if not values:
        values.extend(_DEFAULT_PRIMITIVE_GAPS)
    for blocker in profile.green_blockers:
        normalized = blocker.strip().lower().replace(" ", "_").replace("-", "_")
        if normalized and normalized not in values:
            values.append(normalized)
    if "source_quorum" not in values:
        values.append("source_quorum")
    return tuple(dict.fromkeys(values))


def _source_task_for_gap(
    candidate_event: CandidateEvent,
    profile: ArchetypeMemoryProfile,
    primitive_gap: str,
    recalled_records: Sequence[object],
) -> SourceTask:
    preferred = _preferred_sources(profile, primitive_gap)
    task_type = SourceTaskType.RED_TEAM.value if "risk" in primitive_gap or "hard" in primitive_gap else SourceTaskType.POSITIVE_VERIFY.value
    if "cash" in primitive_gap or "fcf" in primitive_gap:
        preferred = tuple(item for item in ("DART", "CompanyGuide", "IR") if item)
    general_search_allowed = "TrustedNews" in preferred and not any(item in primitive_gap.lower() for item in ("cash", "fcf", "contract"))
    payload = {
        "candidate_event_id": candidate_event.candidate_event_id,
        "archetype_id": profile.canonical_archetype_id,
        "primitive_gap": primitive_gap,
        "task_type": task_type,
    }
    return SourceTask(
        task_id=deterministic_id("RSTASK", payload),
        candidate_event_id=candidate_event.candidate_event_id,
        symbol=candidate_event.symbol,
        company_name=candidate_event.company_name,
        archetype_id=profile.canonical_archetype_id,
        primitive_gap=primitive_gap,
        task_type=task_type,
        preferred_source_classes=preferred,
        fallback_source_classes=_fallback_sources(preferred),
        forbidden_source_classes=_forbidden_sources(primitive_gap),
        allowed_domains=(),
        date_window={"end": candidate_event.event_date, "lookback_days": 540},
        max_queries=3,
        max_candidates=20,
        max_fetches=5,
        stop_condition={"accepted_claim_count": 1, "counter_claim_check_done": True},
        llm_query_allowed=True,
        general_search_allowed=general_search_allowed,
        reason_from_memory=f"{profile.canonical_archetype_id}:{primitive_gap}",
        memory_record_ids=tuple(getattr(record, "record_id", "") for record in recalled_records[:5]),
    )


def _preferred_sources(profile: ArchetypeMemoryProfile, primitive_gap: str) -> tuple[str, ...]:
    if "cash" in primitive_gap.lower() or "fcf" in primitive_gap.lower():
        return ("DART", "CompanyGuide", "IR")
    if "contract" in primitive_gap.lower() or "backlog" in primitive_gap.lower():
        return ("DART", "KIND", "IR")
    if "regulatory" in primitive_gap.lower() or "clinical" in primitive_gap.lower():
        return ("Official", "DART", "IR")
    if profile.source_routes:
        return tuple(dict.fromkeys(profile.source_routes[:4]))
    return ("DART", "IR", "Official")


def _fallback_sources(preferred: Sequence[str]) -> tuple[str, ...]:
    values = [item for item in ("Official", "BrokerPDF", "TrustedNews") if item not in preferred]
    return tuple(values[:2])


def _forbidden_sources(primitive_gap: str) -> tuple[str, ...]:
    values = ["unbounded_general_search"]
    lower = primitive_gap.lower()
    if "cash" in lower or "fcf" in lower:
        values.append("NewsOnlyForFCF")
    if "contract" in lower:
        values.append("GeneralWebBeforeOfficialDisclosure")
    return tuple(values)


def _red_team_checks(memory_store: ResearchMemoryStore, archetype_id: str) -> tuple[str, ...]:
    records = list(memory_store.get_false_positive_patterns(archetype_id)) + list(
        memory_store.query(archetype_id=archetype_id, memory_type=MemoryType.HARD_BREAK_PATTERN.value, limit=8)
    )
    checks = []
    for record in records[:8]:
        if record.false_positive_patterns:
            checks.extend(record.false_positive_patterns)
        elif record.hard_break_primitives:
            checks.extend(record.hard_break_primitives)
        else:
            checks.append(record.memory_type)
    return tuple(dict.fromkeys(checks))


def _positive_thesis(candidate_event: CandidateEvent, profile: ArchetypeMemoryProfile) -> str:
    return (
        f"{candidate_event.company_name} has a {candidate_event.event_type} candidate event; "
        f"Research Brain should verify {', '.join(_primitive_gaps(profile)[:3])} through source-backed claims."
    )


def _counter_thesis(profile: ArchetypeMemoryProfile) -> str:
    if profile.false_positive_patterns:
        return "Do not promote until false-positive patterns are cleared: " + ", ".join(profile.false_positive_patterns[:3])
    if profile.source_gap_summary:
        return "Planning-only source gaps remain; Evidence OS must verify claims before score/stage."
    return "Counter-thesis requires direct target/current/source-backed verification."


def _query_suggestions(profile: ArchetypeMemoryProfile) -> tuple[str, ...]:
    values = []
    for hint in profile.query_pattern_hints:
        values.append(f"LLM should generate a company-scoped query for intent: {hint}")
    return tuple(values[:5])


def _planning_confidence(profile: ArchetypeMemoryProfile) -> str:
    if profile.memory_record_count >= 20 and profile.url_backed_count > 0:
        return "high"
    if profile.memory_record_count > 0:
        return "medium"
    return "low"


__all__ = ["build_research_brain_plan", "infer_archetype_hypothesis"]
