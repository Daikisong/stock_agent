"""Real planner runtime for Research Brain v4."""

from __future__ import annotations

import json
import os
import re
import shlex
import signal
import subprocess
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.agentic.evidence_contract_v2 import load_evidence_contracts_v2
from e2r.calibration.taxonomy import CANONICAL_ARCHETYPE_IDS
from e2r.env import load_project_env
from e2r.research_brain.schemas import SourceTask, SourceTaskType, deterministic_id
from e2r.research_brain.v2_archetype_router import route_candidate_event_v2
from e2r.research_brain.v2_llm_planner import validate_llm_planner_output_v2
from e2r.research_brain.v2_schemas import ArchetypeMemoryCard, CandidateEventV2, LLMPlannerOutputV2
from e2r.research_brain.v3_llm_planner_provider import (
    FORBIDDEN_RESEARCH_BRAIN_OUTPUT_KEYS,
    PlannerProviderRejected,
    PlannerProviderUnavailable,
    validate_llm_planner_output_v3,
)
from e2r.research_brain.v4_schemas import PlannerProviderModeV4, PlannerRunV4


PLANNER_BATCH_OUTPUT_SCHEMA: Mapping[str, object] = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "plans": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "candidate_event_id": {"type": "string"},
                    "top_k_archetype_hypotheses": {
                        "type": "array",
                        "minItems": 1,
                        "items": {
                            "type": "object",
                            "additionalProperties": False,
                            "properties": {
                                "archetype_id": {"type": "string"},
                                "probability_or_score": {"type": "number"},
                                "reason": {"type": "string"},
                            },
                            "required": ["archetype_id", "probability_or_score", "reason"],
                        },
                    },
                    "positive_thesis": {"type": "string"},
                    "counter_thesis": {"type": "string"},
                    "must_verify_primitives": {"type": "array", "items": {"type": "string"}},
                    "green_blockers_to_close": {"type": "array", "items": {"type": "string"}},
                    "red_team_checks": {"type": "array", "items": {"type": "string"}},
                    "source_task_drafts": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "additionalProperties": False,
                            "properties": {
                                "task_id": {"type": "string"},
                                "primitive_gap": {"type": "string"},
                                "task_type": {"type": "string"},
                                "preferred_source_classes": {"type": "array", "items": {"type": "string"}},
                                "fallback_source_classes": {"type": "array", "items": {"type": "string"}},
                                "forbidden_source_classes": {"type": "array", "items": {"type": "string"}},
                                "date_window": {
                                    "type": "object",
                                    "additionalProperties": False,
                                    "properties": {
                                        "end": {"type": "string"},
                                        "lookback_days": {"type": "integer"},
                                    },
                                    "required": ["end", "lookback_days"],
                                },
                                "max_queries": {"type": "integer"},
                                "max_candidates": {"type": "integer"},
                                "max_fetches": {"type": "integer"},
                                "stop_condition": {
                                    "type": "object",
                                    "additionalProperties": False,
                                    "properties": {
                                        "accepted_claim_count": {"type": "integer"},
                                    },
                                    "required": ["accepted_claim_count"],
                                },
                                "llm_query_allowed": {"type": "boolean"},
                                "general_search_allowed": {"type": "boolean"},
                                "reason_from_memory": {"type": "string"},
                            },
                            "required": [
                                "task_id",
                                "primitive_gap",
                                "task_type",
                                "preferred_source_classes",
                                "fallback_source_classes",
                                "forbidden_source_classes",
                                "date_window",
                                "max_queries",
                                "max_candidates",
                                "max_fetches",
                                "stop_condition",
                                "llm_query_allowed",
                                "general_search_allowed",
                                "reason_from_memory",
                            ],
                        },
                    },
                    "query_intents": {"type": "array", "items": {"type": "string"}},
                    "do_not_promote_reasons": {"type": "array", "items": {"type": "string"}},
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
                    "top_k_archetype_hypotheses",
                    "positive_thesis",
                    "counter_thesis",
                    "must_verify_primitives",
                    "green_blockers_to_close",
                    "red_team_checks",
                    "source_task_drafts",
                    "query_intents",
                    "do_not_promote_reasons",
                    "planner_self_check",
                ],
            },
        }
    },
    "required": ["plans"],
}


class ResearchBrainPlannerProviderV4:
    provider_name = "abstract"
    provider_mode = PlannerProviderModeV4.NONE.value
    fake_provider = False
    real_provider = False
    model: str | None = None
    endpoint: str | None = None

    def plan_many(
        self,
        *,
        events: Sequence[CandidateEventV2],
        memory_cards: Sequence[ArchetypeMemoryCard],
        existing_evidence_by_event_id: Mapping[str, Mapping[str, Any]] | None = None,
    ) -> Mapping[str, LLMPlannerOutputV2]:
        raise NotImplementedError


@dataclass
class CodexCLIPlannerProviderV4(ResearchBrainPlannerProviderV4):
    """Codex CLI-backed real LLM planner.

    This is intentionally batch-oriented so a production-shadow run can exercise
    a real planner for at least ten candidates without spawning one process per
    ticker. The LLM still returns the planning JSON; deterministic code only
    validates it and converts valid drafts into SourceTask objects later.
    """

    codex_command: str = "codex"
    model: str | None = None
    profile: str | None = None
    working_directory: str | Path | None = None
    timeout_seconds: float = 180.0
    sandbox: str = "read-only"
    approval_policy: str = "never"
    extra_args: tuple[str, ...] = field(default_factory=tuple)

    provider_name = "codex_cli_planner"
    provider_mode = PlannerProviderModeV4.REAL.value
    real_provider = True
    endpoint = "codex-cli"

    def plan_many(
        self,
        *,
        events: Sequence[CandidateEventV2],
        memory_cards: Sequence[ArchetypeMemoryCard],
        existing_evidence_by_event_id: Mapping[str, Mapping[str, Any]] | None = None,
    ) -> Mapping[str, LLMPlannerOutputV2]:
        if not events:
            return {}
        payload = build_v4_planner_prompt_payload(
            events=events,
            memory_cards=memory_cards,
            existing_evidence_by_event_id=existing_evidence_by_event_id or {},
        )
        with tempfile.TemporaryDirectory(prefix="e2r_v4_planner_") as tmpdir:
            tmp = Path(tmpdir)
            schema_path = tmp / "planner_schema.json"
            output_path = tmp / "planner_output.json"
            schema_path.write_text(json.dumps(PLANNER_BATCH_OUTPUT_SCHEMA, ensure_ascii=False), encoding="utf-8")
            command = self._command(schema_path=schema_path, output_path=output_path)
            try:
                completed = _run_codex_command(
                    command,
                    prompt=_planner_prompt(payload),
                    timeout=self.timeout_seconds,
                )
            except subprocess.TimeoutExpired as exc:
                raise PlannerProviderUnavailable("codex_cli_timeout") from exc
            except OSError as exc:
                raise PlannerProviderUnavailable(f"codex_cli_os_error:{type(exc).__name__}") from exc
            raw = output_path.read_text(encoding="utf-8") if output_path.exists() else completed.stdout
        data = _json_object_from_text(raw)
        if data is None:
            if completed.returncode != 0:
                raise PlannerProviderUnavailable(_clean_provider_error(completed.stderr or completed.stdout))
            raise PlannerProviderRejected("codex planner returned non-json output")
        if _count_forbidden_keys(data):
            raise PlannerProviderRejected("codex planner output contains score/stage/final keys")
        by_event = {event.candidate_event_id: event for event in events}
        outputs: dict[str, LLMPlannerOutputV2] = {}
        for row in data.get("plans") or ():
            if not isinstance(row, Mapping):
                continue
            event_id = str(row.get("candidate_event_id") or "")
            event = by_event.get(event_id)
            if event is None:
                continue
            outputs[event_id] = validate_llm_planner_output_v4(
                row,
                event=event,
                memory_cards=memory_cards,
            )
        if not outputs:
            raise PlannerProviderRejected("codex planner returned no matching candidate plans")
        return outputs

    def _command(self, *, schema_path: Path, output_path: Path) -> list[str]:
        command = [
            self.codex_command,
            "--sandbox",
            self.sandbox,
            "--ask-for-approval",
            self.approval_policy,
            "exec",
            "--ephemeral",
            "--output-schema",
            str(schema_path),
            "--output-last-message",
            str(output_path),
            "--color",
            "never",
        ]
        if self.working_directory is not None:
            command.extend(("-C", str(self.working_directory)))
        if self.model:
            command.extend(("-m", self.model))
        if self.profile:
            command.extend(("-p", self.profile))
        command.extend(self.extra_args)
        command.append("-")
        return command


class FixturePlannerProviderV4(ResearchBrainPlannerProviderV4):
    provider_name = "fixture_fake_planner_v4"
    provider_mode = PlannerProviderModeV4.FAKE.value
    fake_provider = True

    def plan_many(
        self,
        *,
        events: Sequence[CandidateEventV2],
        memory_cards: Sequence[ArchetypeMemoryCard],
        existing_evidence_by_event_id: Mapping[str, Mapping[str, Any]] | None = None,
    ) -> Mapping[str, LLMPlannerOutputV2]:
        return {
            event.candidate_event_id: _fixture_output_for_event(event=event, memory_cards=memory_cards)
            for event in events
        }


@dataclass
class FrozenRealPlannerProviderV4(ResearchBrainPlannerProviderV4):
    """Replay planner outputs produced by an already-exercised real provider.

    Multi-day acceptance has two different checks:
    - exercise the real planner on live production-shadow days;
    - replay the same frozen planner/source snapshot three times and require
      deterministic score/stage output.

    The repeat check must not call the LLM again, because that measures LLM
    sampling/provider availability variance rather than deterministic pipeline
    repeatability. This provider keeps the "real planner provenance" while
    replaying the exact real outputs from the baseline run.
    """

    outputs_by_event_id: Mapping[str, LLMPlannerOutputV2]
    provider_name = "frozen_real_planner_snapshot_v4"
    provider_mode = PlannerProviderModeV4.REAL.value
    real_provider = True
    endpoint = "frozen-real-planner-snapshot"

    def plan_many(
        self,
        *,
        events: Sequence[CandidateEventV2],
        memory_cards: Sequence[ArchetypeMemoryCard],
        existing_evidence_by_event_id: Mapping[str, Mapping[str, Any]] | None = None,
    ) -> Mapping[str, LLMPlannerOutputV2]:
        return {
            event.candidate_event_id: self.outputs_by_event_id[event.candidate_event_id]
            for event in events
            if event.candidate_event_id in self.outputs_by_event_id
        }


class NoPlannerProviderV4(ResearchBrainPlannerProviderV4):
    provider_name = "none"
    provider_mode = PlannerProviderModeV4.NONE.value


def build_planner_provider_v4(
    *,
    mode: str,
    working_directory: str | Path | None = None,
) -> ResearchBrainPlannerProviderV4 | None:
    load_project_env()
    normalized = mode.strip().lower()
    if normalized == PlannerProviderModeV4.NONE.value:
        return None
    if normalized in {"fake", "test_fake"}:
        return FixturePlannerProviderV4()
    if normalized in {"real", "codex", "codex_cli"}:
        env = os.environ
        return CodexCLIPlannerProviderV4(
            codex_command=(env.get("E2R_CODEX_PLANNER_COMMAND") or env.get("E2R_CODEX_THEME_COMMAND") or "codex").strip()
            or "codex",
            model=_optional_env(env, "E2R_CODEX_PLANNER_MODEL"),
            profile=_optional_env(env, "E2R_CODEX_PLANNER_PROFILE"),
            working_directory=_optional_env(env, "E2R_CODEX_PLANNER_WORKDIR") or working_directory,
            timeout_seconds=_float_env(env, "E2R_CODEX_PLANNER_TIMEOUT_SECONDS", 180.0),
            sandbox=(env.get("E2R_CODEX_PLANNER_SANDBOX") or "read-only").strip() or "read-only",
            approval_policy=(env.get("E2R_CODEX_PLANNER_APPROVAL_POLICY") or "never").strip() or "never",
            extra_args=tuple(shlex.split(env.get("E2R_CODEX_PLANNER_EXTRA_ARGS") or "")),
        )
    raise ValueError(f"unknown planner provider mode: {mode}")


def run_planner_provider_v4(
    *,
    provider: ResearchBrainPlannerProviderV4 | None,
    events: Sequence[CandidateEventV2],
    memory_cards: Sequence[ArchetypeMemoryCard],
    existing_evidence_by_event_id: Mapping[str, Mapping[str, Any]] | None = None,
) -> tuple[PlannerRunV4, ...]:
    if provider is None:
        return tuple(
            PlannerRunV4(
                event=event,
                provider_name="none",
                provider_mode=PlannerProviderModeV4.NONE.value,
                real_provider_exercised=False,
                real_provider_success=False,
                fake_provider_used=False,
                provider_error="planner_provider_not_configured",
            )
            for event in events
        )
    try:
        outputs = provider.plan_many(
            events=events,
            memory_cards=memory_cards,
            existing_evidence_by_event_id=existing_evidence_by_event_id or {},
        )
    except PlannerProviderRejected as exc:
        return tuple(_failed_run(provider, event, str(exc), rejected=True) for event in events)
    except PlannerProviderUnavailable as exc:
        return tuple(_failed_run(provider, event, str(exc), rejected=False) for event in events)
    rows: list[PlannerRunV4] = []
    for event in events:
        output = outputs.get(event.candidate_event_id)
        if output is None:
            rows.append(_failed_run(provider, event, "planner_output_missing_for_candidate", rejected=False))
            continue
        rows.append(
            PlannerRunV4(
                event=event,
                provider_name=provider.provider_name,
                provider_mode=provider.provider_mode,
                real_provider_exercised=bool(provider.real_provider),
                real_provider_success=bool(provider.real_provider),
                fake_provider_used=bool(provider.fake_provider),
                output=output,
                model=getattr(provider, "model", None),
                endpoint=getattr(provider, "endpoint", None),
            )
        )
    return tuple(rows)


def source_tasks_from_planner_output_v4(
    *,
    event: CandidateEventV2,
    planner_output: LLMPlannerOutputV2,
    card_by_id: Mapping[str, ArchetypeMemoryCard],
    max_tasks: int = 5,
) -> tuple[SourceTask, ...]:
    primary = str(planner_output.top_k_archetype_hypotheses[0].get("archetype_id"))
    card = card_by_id[primary]
    tasks: list[SourceTask] = []
    for draft in planner_output.source_task_drafts[:max_tasks]:
        primitive = str(draft.get("primitive_gap") or draft.get("primitive_id") or "").strip()
        if not primitive:
            continue
        tasks.append(
            SourceTask(
                task_id=str(draft.get("task_id") or deterministic_id("RSTASKV4", (event.candidate_event_id, primary, primitive))),
                candidate_event_id=event.candidate_event_id,
                symbol=event.symbol,
                company_name=event.company_name,
                archetype_id=primary,
                primitive_gap=primitive,
                task_type=_task_type_value(draft.get("task_type")),
                preferred_source_classes=tuple(str(item) for item in draft.get("preferred_source_classes") or ("CompanyGuide", "DART")),
                fallback_source_classes=tuple(str(item) for item in draft.get("fallback_source_classes") or ("IssuerOfficial",)),
                forbidden_source_classes=tuple(
                    str(item) for item in draft.get("forbidden_source_classes") or ("unbounded_general_search",)
                ),
                date_window=draft.get("date_window") or {"end": event.event_date, "lookback_days": 540},
                max_queries=int(draft.get("max_queries") or 1),
                max_candidates=int(draft.get("max_candidates") or 10),
                max_fetches=int(draft.get("max_fetches") or 3),
                stop_condition=draft.get("stop_condition") or {"accepted_claim_count": 1},
                llm_query_allowed=bool(draft.get("llm_query_allowed", True)),
                general_search_allowed=bool(draft.get("general_search_allowed", False)),
                reason_from_memory=str(draft.get("reason_from_memory") or f"planner_v4:{primary}:{primitive}"),
                memory_record_ids=card.representative_url_backed_fixture_ids[:5],
            )
        )
    return tuple(tasks)


def build_v4_planner_prompt_payload(
    *,
    events: Sequence[CandidateEventV2],
    memory_cards: Sequence[ArchetypeMemoryCard],
    existing_evidence_by_event_id: Mapping[str, Mapping[str, Any]],
) -> Mapping[str, Any]:
    contracts = load_evidence_contracts_v2(require_all_archetypes=False)
    card_by_id = {card.archetype_id: card for card in memory_cards}
    event_payloads = []
    for event in events:
        route = route_candidate_event_v2(event, memory_cards, top_k=5)
        options = []
        for candidate in route.top_k_archetypes:
            card = card_by_id.get(candidate.archetype_id)
            contract = contracts.get(candidate.archetype_id)
            primitives = tuple(contract.required_primitives if contract else (card.required_primitives if card else ()))
            options.append(
                {
                    "archetype_id": candidate.archetype_id,
                    "router_score": candidate.probability_or_score,
                    "router_reason": candidate.reason,
                    "allowed_primitives": list(primitives[:12]),
                    "preferred_source_routes": {
                        key: list(value)
                        for key, value in (card.source_route_by_primitive.items() if card else ())
                        if key in primitives
                    },
                    "green_blockers": list(card.green_blockers[:5] if card else ()),
                    "do_not_promote_rules": list(card.do_not_promote_rules[:5] if card else ()),
                }
            )
        event_payloads.append(
            {
                "candidate_event": event.to_dict(),
                "existing_evidence_summary": dict(existing_evidence_by_event_id.get(event.candidate_event_id, {})),
                "allowed_archetype_options": options,
            }
        )
    return {
        "schema_version": "research_brain_v4_planner_prompt",
        "events": event_payloads,
        "rules": [
            "Return one plan per candidate_event_id.",
            "Use only archetype_id values listed under allowed_archetype_options.",
            "Use only allowed_primitives for source_task_drafts.primitive_gap.",
            "Do not output score, stage, hard_break final, verified final, current_score_eligible, or accepted claim final.",
            "Do not use future MFE/MAE, outcome labels, expected stage, or target score threshold.",
            "FCF, cash, revision, backlog, and contract gaps must use DART, CompanyGuide, IR, or IssuerOfficial before news/web.",
            "Every source_task_draft must set forbidden_source_classes exactly to [\"unbounded_general_search\"].",
            "Every source_task_draft must set general_search_allowed=false.",
            "For official-solvable gaps, fallback_source_classes must not include TrustedNews, News, web, or general web.",
            "R13 may be primary only when the event explicitly says red-team, false-positive, or cross-archetype review.",
        ],
        "forbidden_output_keys": sorted(FORBIDDEN_RESEARCH_BRAIN_OUTPUT_KEYS),
    }


def validate_llm_planner_output_v4(
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
        _validate_source_task_draft_v4(draft)
    return validate_llm_planner_output_v3(payload, event=event, memory_cards=memory_cards)


def _fixture_output_for_event(
    *,
    event: CandidateEventV2,
    memory_cards: Sequence[ArchetypeMemoryCard],
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
    payload = {
        "top_k_archetype_hypotheses": hypotheses,
        "positive_thesis": event.event_summary,
        "counter_thesis": "source-backed claim 전까지 score/stage로 승격하지 않는다.",
        "must_verify_primitives": list(primitives),
        "green_blockers_to_close": list(card.green_blockers[:5] if card else ()),
        "red_team_checks": list(card.false_positive_patterns[:5] if card else ()),
        "source_task_drafts": [
            _source_task_draft(event=event, card=card, primitive=primitive)
            for primitive in primitives
        ],
        "query_intents": [f"verify {primitive}" for primitive in primitives],
        "do_not_promote_reasons": list(card.do_not_promote_rules[:5] if card else ("archetype pending",)),
        "planner_self_check": {
            "score_keys_present": False,
            "stage_keys_present": False,
            "future_outcome_used": False,
        },
    }
    return validate_llm_planner_output_v4(payload, event=event, memory_cards=memory_cards)


def _source_task_draft(
    *,
    event: CandidateEventV2,
    card: ArchetypeMemoryCard | None,
    primitive: str,
) -> Mapping[str, Any]:
    preferred = tuple((card.source_route_by_primitive.get(primitive) if card else None) or ())
    if not preferred:
        preferred = ("CompanyGuide", "DART", "IR")
    if _is_official_solvable_gap(primitive):
        preferred = ("DART", "CompanyGuide", "IR")
    fallback = ["IssuerOfficial", "IR"]
    if not _is_official_solvable_gap(primitive):
        fallback.append("TrustedNews")
    return {
        "task_id": deterministic_id("RSTASKV4DRAFT", (event.candidate_event_id, card.archetype_id if card else "", primitive)),
        "primitive_gap": primitive,
        "task_type": SourceTaskType.POSITIVE_VERIFY.value,
        "preferred_source_classes": list(preferred[:4]),
        "fallback_source_classes": fallback,
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


def _validate_source_task_draft_v4(draft: Mapping[str, Any]) -> None:
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
    if "unbounded_general_search" not in tuple(str(item) for item in draft.get("forbidden_source_classes") or ()):
        raise PlannerProviderRejected(f"source_task_draft {primitive} missing unbounded general search guard")
    if _is_official_solvable_gap(primitive):
        sources = {item.lower() for item in (*preferred, *fallback)}
        if sources & {"generalweb", "web", "newsonly", "trustednews"} or bool(draft.get("general_search_allowed")):
            raise PlannerProviderRejected(f"official-solvable gap sent to general web/news: {primitive}")


def _task_type_value(value: object) -> str:
    raw = str(value or SourceTaskType.POSITIVE_VERIFY.value).strip()
    allowed = {item.value for item in SourceTaskType}
    return raw if raw in allowed else SourceTaskType.POSITIVE_VERIFY.value


def _failed_run(
    provider: ResearchBrainPlannerProviderV4,
    event: CandidateEventV2,
    provider_error: str,
    *,
    rejected: bool,
) -> PlannerRunV4:
    return PlannerRunV4(
        event=event,
        provider_name=provider.provider_name,
        provider_mode=provider.provider_mode,
        real_provider_exercised=False if provider_error else bool(provider.real_provider),
        real_provider_success=False,
        fake_provider_used=bool(provider.fake_provider),
        provider_error=provider_error,
        rejected_by_validator=rejected,
        r13_invalid_primary_rejected="R13 primary" in provider_error,
        model=getattr(provider, "model", None),
        endpoint=getattr(provider, "endpoint", None),
    )


def _planner_prompt(payload: Mapping[str, Any]) -> str:
    return "\n\n".join(
        (
            "You are Research Brain v4 Planner. Return exactly one JSON object matching the schema.",
            "You plan what evidence to acquire. You never score, stage, verify final claims, or mark current_score_eligible.",
            "Use the candidate events and allowed archetype options only.",
            "For every source_task_draft include forbidden_source_classes=[\"unbounded_general_search\"] and general_search_allowed=false.",
            json.dumps(payload, ensure_ascii=False, sort_keys=True),
        )
    )


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


def _json_object_from_text(text: str) -> Mapping[str, object] | None:
    clean = text.strip()
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


def _count_forbidden_keys(value: object) -> int:
    if isinstance(value, Mapping):
        return sum(1 for key in value if str(key) in FORBIDDEN_RESEARCH_BRAIN_OUTPUT_KEYS) + sum(
            _count_forbidden_keys(item) for item in value.values()
        )
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return sum(_count_forbidden_keys(item) for item in value)
    return 0


def _is_official_solvable_gap(primitive: str) -> bool:
    lower = primitive.lower()
    return any(token in lower for token in ("fcf", "cash", "revision", "backlog", "contract", "rpo"))


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
        or ("false" in text and "positive" in text and "review" in text)
        or ("cross" in text and "red" in text and "review" in text)
    )


def _clean_provider_error(text: str) -> str:
    clean = re.sub(r"\s+", " ", str(text)).strip()
    if len(clean) <= 360:
        return clean or "planner_provider_error"
    return f"{clean[:180]} ... {clean[-180:]}"


def _optional_env(env: Mapping[str, str], key: str) -> str | None:
    value = (env.get(key) or "").strip()
    return value or None


def _float_env(env: Mapping[str, str], key: str, default: float) -> float:
    try:
        return float(env.get(key) or default)
    except (TypeError, ValueError):
        return default


__all__ = [
    "CodexCLIPlannerProviderV4",
    "FixturePlannerProviderV4",
    "FrozenRealPlannerProviderV4",
    "NoPlannerProviderV4",
    "ResearchBrainPlannerProviderV4",
    "build_planner_provider_v4",
    "build_v4_planner_prompt_payload",
    "run_planner_provider_v4",
    "source_tasks_from_planner_output_v4",
    "validate_llm_planner_output_v4",
]
