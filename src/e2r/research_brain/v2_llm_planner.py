"""LLM planner schema and validation hooks for Research Brain v2."""

from __future__ import annotations

from typing import Any, Mapping, Sequence

from e2r.calibration.taxonomy import CANONICAL_ARCHETYPE_IDS
from e2r.research_brain.v2_schemas import (
    FORBIDDEN_RESEARCH_BRAIN_OUTPUT_KEYS,
    ArchetypeMemoryCard,
    CandidateEventV2,
    LLMPlannerOutputV2,
)


class PlannerProviderUnavailable(RuntimeError):
    """Raised when no real planner provider is configured."""


def validate_llm_planner_output_v2(payload: Mapping[str, Any]) -> LLMPlannerOutputV2:
    _reject_forbidden(payload)
    hypotheses = tuple(payload.get("top_k_archetype_hypotheses") or ())
    if not hypotheses:
        raise ValueError("top_k_archetype_hypotheses is required")
    valid_ids = set(CANONICAL_ARCHETYPE_IDS)
    for item in hypotheses:
        archetype_id = str(item.get("archetype_id") or "")
        if archetype_id not in valid_ids:
            raise ValueError(f"unknown archetype_id: {archetype_id}")
    output = LLMPlannerOutputV2(
        top_k_archetype_hypotheses=hypotheses,
        positive_thesis=str(payload.get("positive_thesis") or ""),
        counter_thesis=str(payload.get("counter_thesis") or ""),
        must_verify_primitives=tuple(str(item) for item in payload.get("must_verify_primitives") or ()),
        green_blockers_to_close=tuple(str(item) for item in payload.get("green_blockers_to_close") or ()),
        red_team_checks=tuple(str(item) for item in payload.get("red_team_checks") or ()),
        source_task_drafts=tuple(payload.get("source_task_drafts") or ()),
        query_intents=tuple(str(item) for item in payload.get("query_intents") or ()),
        do_not_promote_reasons=tuple(str(item) for item in payload.get("do_not_promote_reasons") or ()),
        planner_self_check=payload.get("planner_self_check") or {},
    )
    return output


def build_planner_prompt_payload(
    *,
    event: CandidateEventV2,
    cards: Sequence[ArchetypeMemoryCard],
) -> Mapping[str, Any]:
    """Build a provider payload with cards but without score/stage targets."""

    return {
        "schema_version": "research_brain_v2_llm_planner_prompt",
        "candidate_event": event.to_dict(),
        "archetype_memory_cards": [
            {
                "archetype_id": card.archetype_id,
                "canonical_mechanism": card.canonical_mechanism,
                "stage2_unlocks": list(card.stage2_unlocks),
                "green_blockers": list(card.green_blockers),
                "false_positive_patterns": list(card.false_positive_patterns),
                "required_primitives": list(card.required_primitives),
                "source_route_by_primitive": card.source_route_by_primitive,
                "do_not_promote_rules": list(card.do_not_promote_rules),
            }
            for card in cards
        ],
        "forbidden_output_keys": sorted(FORBIDDEN_RESEARCH_BRAIN_OUTPUT_KEYS),
        "instructions": "Return archetype hypotheses, primitives, source task drafts, and query intents only. Do not output score or stage.",
    }


def planner_provider_status(*, real_provider_available: bool, fake_provider_used: bool) -> Mapping[str, Any]:
    if fake_provider_used:
        readiness_effect = "fake_provider_blocks_production_ready"
    elif real_provider_available:
        readiness_effect = "real_provider_available"
    else:
        readiness_effect = "planner_provider_not_exercised_shadow_only"
    return {
        "real_provider_available": real_provider_available,
        "fake_provider_used": fake_provider_used,
        "readiness_effect": readiness_effect,
    }


def _reject_forbidden(value: Any) -> None:
    if isinstance(value, Mapping):
        for key, item in value.items():
            if str(key) in FORBIDDEN_RESEARCH_BRAIN_OUTPUT_KEYS:
                raise ValueError(f"forbidden planner key: {key}")
            _reject_forbidden(item)
    elif isinstance(value, (list, tuple)):
        for item in value:
            _reject_forbidden(item)


__all__ = [
    "PlannerProviderUnavailable",
    "build_planner_prompt_payload",
    "planner_provider_status",
    "validate_llm_planner_output_v2",
]
