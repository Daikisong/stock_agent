"""Real planner provider integration for Research Brain v3."""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from abc import ABC, abstractmethod
from typing import Any, Mapping, Sequence

from e2r.calibration.taxonomy import CANONICAL_ARCHETYPE_IDS
from e2r.agentic.evidence_contract_v2 import load_evidence_contracts_v2
from e2r.research_brain.schemas import SourceTask, SourceTaskType, deterministic_id
from e2r.research_brain.v2_archetype_router import route_candidate_event_v2
from e2r.research_brain.v2_llm_planner import validate_llm_planner_output_v2
from e2r.research_brain.v2_schemas import (
    FORBIDDEN_RESEARCH_BRAIN_OUTPUT_KEYS,
    ArchetypeMemoryCard,
    CandidateEventV2,
    LLMPlannerOutputV2,
)
from e2r.research_brain.v3_schemas import PlannerRunV3


class PlannerProviderUnavailable(RuntimeError):
    """Raised when a real planner provider is not configured."""


class PlannerProviderRejected(ValueError):
    """Raised when planner output violates v3 policy."""


class ResearchBrainPlannerProvider(ABC):
    provider_name = "abstract"
    fake_provider = False
    real_provider = False

    @abstractmethod
    def plan(
        self,
        event: CandidateEventV2,
        memory_cards: Sequence[ArchetypeMemoryCard],
        existing_evidence_summary: Mapping[str, Any] | None = None,
    ) -> LLMPlannerOutputV2:
        """Return a validated planner output."""


class OpenAIPlannerProvider(ResearchBrainPlannerProvider):
    """OpenAI-compatible chat-completions planner adapter.

    The adapter is intentionally idle unless called by the v3 CLI with a real
    provider mode. Tests use explicit fake providers instead of this class.
    """

    provider_name = "openai_chat_completions"
    real_provider = True

    def __init__(
        self,
        *,
        api_key: str | None = None,
        model: str | None = None,
        endpoint: str = "https://api.openai.com/v1/chat/completions",
        timeout_seconds: int = 60,
    ) -> None:
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.model = model or os.getenv("OPENAI_MODEL", "gpt-5-mini")
        self.endpoint = endpoint
        self.timeout_seconds = timeout_seconds

    def plan(
        self,
        event: CandidateEventV2,
        memory_cards: Sequence[ArchetypeMemoryCard],
        existing_evidence_summary: Mapping[str, Any] | None = None,
    ) -> LLMPlannerOutputV2:
        if not self.api_key:
            raise PlannerProviderUnavailable("OPENAI_API_KEY is not configured")
        payload = build_v3_planner_prompt_payload(
            event=event,
            memory_cards=memory_cards,
            existing_evidence_summary=existing_evidence_summary,
        )
        request_body = {
            "model": self.model,
            "response_format": {"type": "json_object"},
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are Research Brain Planner. Return only JSON. "
                        "Do not output score, stage, hard_break final, verified final, "
                        "or current_score_eligible."
                    ),
                },
                {"role": "user", "content": json.dumps(payload, ensure_ascii=False, sort_keys=True)},
            ],
        }
        request = urllib.request.Request(
            self.endpoint,
            data=json.dumps(request_body).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=self.timeout_seconds) as response:
                raw = json.loads(response.read().decode("utf-8"))
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            raise PlannerProviderUnavailable(f"planner provider error: {exc}") from exc
        content = raw.get("choices", [{}])[0].get("message", {}).get("content")
        if not content:
            raise PlannerProviderUnavailable("planner provider returned empty content")
        try:
            provider_payload = json.loads(content)
        except json.JSONDecodeError as exc:
            raise PlannerProviderRejected("planner provider returned non-JSON content") from exc
        return validate_llm_planner_output_v3(provider_payload, event=event, memory_cards=memory_cards)


class FixturePlannerProvider(ResearchBrainPlannerProvider):
    """Explicit test/fixture provider.

    This is not production-ready. Reports must record ``fake_provider_used`` when
    this provider is used.
    """

    provider_name = "fixture_fake_planner"
    fake_provider = True

    def plan(
        self,
        event: CandidateEventV2,
        memory_cards: Sequence[ArchetypeMemoryCard],
        existing_evidence_summary: Mapping[str, Any] | None = None,
    ) -> LLMPlannerOutputV2:
        route = route_candidate_event_v2(event, memory_cards, top_k=3)
        hypotheses = [
            {
                "archetype_id": item.archetype_id,
                "probability_or_score": item.probability_or_score,
                "reason": item.reason,
            }
            for item in route.top_k_archetypes
        ]
        card_by_id = {card.archetype_id: card for card in memory_cards}
        primary = route.primary_archetype or (hypotheses[0]["archetype_id"] if hypotheses else None)
        card = card_by_id.get(str(primary)) if primary else None
        contracts = load_evidence_contracts_v2(require_all_archetypes=False)
        contract = contracts.get(str(primary)) if primary else None
        primitives = tuple((contract.required_primitives if contract else card.required_primitives)[:3]) if card else ()
        drafts = tuple(_source_task_draft(event=event, card=card, primitive=primitive) for primitive in primitives)
        payload = {
            "top_k_archetype_hypotheses": hypotheses,
            "positive_thesis": event.event_summary,
            "counter_thesis": "검증 전까지 source-backed claim 없이 승급하지 않는다.",
            "must_verify_primitives": list(primitives),
            "green_blockers_to_close": list(card.green_blockers[:5] if card else ()),
            "red_team_checks": list(card.false_positive_patterns[:5] if card else ()),
            "source_task_drafts": list(drafts),
            "query_intents": [f"verify {primitive}" for primitive in primitives],
            "do_not_promote_reasons": list(card.do_not_promote_rules[:5] if card else ("archetype pending",)),
            "planner_self_check": {
                "score_keys_present": False,
                "stage_keys_present": False,
                "future_outcome_used": False,
            },
        }
        return validate_llm_planner_output_v3(payload, event=event, memory_cards=memory_cards)


def build_v3_planner_prompt_payload(
    *,
    event: CandidateEventV2,
    memory_cards: Sequence[ArchetypeMemoryCard],
    existing_evidence_summary: Mapping[str, Any] | None = None,
    as_of_date: str | None = None,
    source_gap_warnings: Sequence[str] = (),
) -> Mapping[str, Any]:
    return {
        "schema_version": "research_brain_v3_planner_prompt",
        "as_of_date": as_of_date or event.event_date,
        "candidate_event": event.to_dict(),
        "existing_evidence_summary": dict(existing_evidence_summary or {}),
        "source_route_policy": {
            "official_first": True,
            "bounded_source_task_budget_required": True,
            "general_web_fallback_requires_explicit_task_permission": True,
            "fcf_cash_revision_gaps_must_use_official_or_companyguide_first": True,
        },
        "source_gap_warnings": list(source_gap_warnings),
        "archetype_memory_cards": [
            {
                "archetype_id": card.archetype_id,
                "large_sector_id": card.large_sector_id,
                "canonical_mechanism": card.canonical_mechanism,
                "stage2_unlocks": list(card.stage2_unlocks),
                "green_blockers": list(card.green_blockers),
                "false_positive_patterns": list(card.false_positive_patterns),
                "required_primitives": list(card.required_primitives),
                "source_route_by_primitive": {k: list(v) for k, v in card.source_route_by_primitive.items()},
                "do_not_promote_rules": list(card.do_not_promote_rules),
                "source_gaps": list(card.source_gaps),
                "runtime_usage_policy": card.runtime_usage_policy,
            }
            for card in memory_cards
        ],
        "forbidden_output_keys": sorted(FORBIDDEN_RESEARCH_BRAIN_OUTPUT_KEYS),
        "forbidden_inputs": [
            "future MFE/MAE",
            "outcome label",
            "expected stage",
            "score threshold",
            "Green을 열어야 한다 같은 목적성 문장",
        ],
        "required_output_keys": [
            "top_k_archetype_hypotheses",
            "positive_thesis",
            "counter_thesis",
            "must_verify_primitives",
            "red_team_checks",
            "source_task_drafts",
            "query_intents",
            "do_not_promote_reasons",
            "planner_self_check",
        ],
    }


def validate_llm_planner_output_v3(
    payload: Mapping[str, Any],
    *,
    event: CandidateEventV2,
    memory_cards: Sequence[ArchetypeMemoryCard],
) -> LLMPlannerOutputV2:
    output = validate_llm_planner_output_v2(payload)
    valid_ids = set(CANONICAL_ARCHETYPE_IDS)
    card_ids = {card.archetype_id for card in memory_cards}
    for item in output.top_k_archetype_hypotheses:
        archetype_id = str(item.get("archetype_id") or "")
        if archetype_id not in valid_ids or archetype_id not in card_ids:
            raise PlannerProviderRejected(f"unknown or unavailable archetype_id: {archetype_id}")
    primary = str(output.top_k_archetype_hypotheses[0].get("archetype_id") or "")
    if primary.startswith("R13_") and not _explicit_r13_event(event):
        raise PlannerProviderRejected("R13 primary is only allowed for explicit red-team events")
    for draft in output.source_task_drafts:
        _validate_source_task_draft(draft)
    return output


def run_planner_provider_v3(
    *,
    provider: ResearchBrainPlannerProvider | None,
    event: CandidateEventV2,
    memory_cards: Sequence[ArchetypeMemoryCard],
    existing_evidence_summary: Mapping[str, Any] | None = None,
) -> PlannerRunV3:
    if provider is None:
        return PlannerRunV3(
            event=event,
            provider_name="none",
            real_provider_exercised=False,
            fake_provider_used=False,
            output=None,
            provider_error="planner_provider_not_configured",
        )
    try:
        output = provider.plan(event, memory_cards, existing_evidence_summary)
    except PlannerProviderRejected as exc:
        return PlannerRunV3(
            event=event,
            provider_name=provider.provider_name,
            real_provider_exercised=bool(provider.real_provider),
            fake_provider_used=bool(provider.fake_provider),
            output=None,
            provider_error=str(exc),
            rejected_by_validator=True,
        )
    except PlannerProviderUnavailable as exc:
        return PlannerRunV3(
            event=event,
            provider_name=provider.provider_name,
            real_provider_exercised=False,
            fake_provider_used=bool(provider.fake_provider),
            output=None,
            provider_error=str(exc),
        )
    return PlannerRunV3(
        event=event,
        provider_name=provider.provider_name,
        real_provider_exercised=bool(provider.real_provider),
        fake_provider_used=bool(provider.fake_provider),
        output=output,
    )


def source_tasks_from_planner_output(
    *,
    event: CandidateEventV2,
    planner_output: LLMPlannerOutputV2,
    card_by_id: Mapping[str, ArchetypeMemoryCard],
    max_tasks: int = 5,
) -> tuple[SourceTask, ...]:
    primary = str(planner_output.top_k_archetype_hypotheses[0].get("archetype_id"))
    card = card_by_id[primary]
    tasks = []
    for draft in planner_output.source_task_drafts[:max_tasks]:
        primitive = str(draft.get("primitive_gap") or draft.get("primitive_id") or "").strip()
        if not primitive:
            continue
        preferred = tuple(str(item) for item in draft.get("preferred_source_classes") or ("DART", "IR", "Official"))
        fallback = tuple(str(item) for item in draft.get("fallback_source_classes") or ("Official",))
        tasks.append(
            SourceTask(
                task_id=str(draft.get("task_id") or deterministic_id("RSTASKV3", (event.candidate_event_id, primary, primitive))),
                candidate_event_id=event.candidate_event_id,
                symbol=event.symbol,
                company_name=event.company_name,
                archetype_id=primary,
                primitive_gap=primitive,
                task_type=str(draft.get("task_type") or SourceTaskType.POSITIVE_VERIFY.value),
                preferred_source_classes=preferred,
                fallback_source_classes=fallback,
                forbidden_source_classes=tuple(str(item) for item in draft.get("forbidden_source_classes") or ("unbounded_general_search",)),
                date_window=draft.get("date_window") or {"end": event.event_date, "lookback_days": 540},
                max_queries=int(draft.get("max_queries") or 1),
                max_candidates=int(draft.get("max_candidates") or 5),
                max_fetches=int(draft.get("max_fetches") or 3),
                stop_condition=draft.get("stop_condition") or {"accepted_claim_count": 1},
                llm_query_allowed=bool(draft.get("llm_query_allowed", True)),
                general_search_allowed=bool(draft.get("general_search_allowed", False)),
                reason_from_memory=str(draft.get("reason_from_memory") or f"planner:{primary}:{primitive}"),
                memory_record_ids=card.representative_url_backed_fixture_ids[:5],
            )
        )
    return tuple(tasks)


def _source_task_draft(
    *,
    event: CandidateEventV2,
    card: ArchetypeMemoryCard | None,
    primitive: str,
) -> Mapping[str, Any]:
    preferred = card.source_route_by_primitive.get(primitive) if card else None
    preferred = tuple(preferred or ("DART", "IR", "Official"))
    if _is_fcf_or_dart_solvable_gap(primitive):
        preferred = tuple(item for item in ("DART", "CompanyGuide", "IR") if item)
    return {
        "task_id": deterministic_id("RSTASKV3DRAFT", (event.candidate_event_id, card.archetype_id if card else "", primitive)),
        "primitive_gap": primitive,
        "task_type": SourceTaskType.POSITIVE_VERIFY.value,
        "preferred_source_classes": list(preferred[:4]),
        "fallback_source_classes": ["Official", "BrokerPDF"],
        "forbidden_source_classes": ["unbounded_general_search"],
        "date_window": {"end": event.event_date, "lookback_days": 540},
        "max_queries": 2,
        "max_candidates": 10,
        "max_fetches": 3,
        "stop_condition": {"accepted_claim_count": 1},
        "llm_query_allowed": True,
        "general_search_allowed": False,
        "reason_from_memory": f"{card.archetype_id if card else 'UNKNOWN'}:{primitive}",
    }


def _validate_source_task_draft(draft: Mapping[str, Any]) -> None:
    primitive = str(draft.get("primitive_gap") or draft.get("primitive_id") or "").strip()
    if not primitive:
        raise PlannerProviderRejected("source_task_draft missing primitive_gap")
    for key in ("max_queries", "max_candidates", "max_fetches"):
        value = draft.get(key)
        if value is None or int(value) <= 0:
            raise PlannerProviderRejected(f"source_task_draft {primitive} missing bounded {key}")
    preferred = tuple(str(item) for item in draft.get("preferred_source_classes") or ())
    fallback = tuple(str(item) for item in draft.get("fallback_source_classes") or ())
    if not preferred:
        raise PlannerProviderRejected(f"source_task_draft {primitive} missing preferred_source_classes")
    if _is_fcf_or_dart_solvable_gap(primitive):
        sources = {item.lower() for item in (*preferred, *fallback)}
        if sources & {"generalweb", "web", "newsonly", "trustednews"} or bool(draft.get("general_search_allowed")):
            raise PlannerProviderRejected(f"FCF/DART-solvable gap sent to general web/news: {primitive}")


def _is_fcf_or_dart_solvable_gap(primitive: str) -> bool:
    lower = primitive.lower()
    return any(token in lower for token in ("fcf", "cash", "revision", "backlog", "contract"))


def _explicit_r13_event(event: CandidateEventV2) -> bool:
    text = " ".join(
        (
            event.event_type,
            event.event_title,
            event.event_summary,
            " ".join(event.raw_reason_codes),
        )
    ).lower()
    return (
        event.event_type in {"red_team_review", "cross_archetype_review", "false_positive_review"}
        or "explicit_r13" in text
        or ("cross" in text and "red" in text and "review" in text)
    )


__all__ = [
    "FixturePlannerProvider",
    "OpenAIPlannerProvider",
    "PlannerProviderRejected",
    "PlannerProviderUnavailable",
    "ResearchBrainPlannerProvider",
    "build_v3_planner_prompt_payload",
    "run_planner_provider_v3",
    "source_tasks_from_planner_output",
    "validate_llm_planner_output_v3",
]
