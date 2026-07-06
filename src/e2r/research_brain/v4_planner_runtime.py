"""Real planner runtime for Research Brain v4."""

from __future__ import annotations

import json
import hashlib
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


CONTRACT_COMPATIBLE_PRIMITIVES: frozenset[str] = frozenset(
    {
        "contract_quality",
        "contract_amount_to_prior_sales",
        "contract_duration_months",
        "contract_visibility",
        "revenue_visibility_contract",
        "order_to_revenue_bridge",
        "order_backlog_to_sales",
        "delivery_schedule",
        "export_contract",
    }
)
_REVENUE_CONTRACT_TERMS: tuple[str, ...] = (
    "단일판매",
    "판매공급계약",
    "판매ㆍ공급계약",
    "판매·공급계약",
    "공급계약",
    "판매계약",
    "계약체결",
    "수주",
    "supply contract",
    "sales contract",
    "purchase order",
    "revenue contract",
    "epc contract",
)
_NON_REVENUE_CONTRACT_TERMS: tuple[str, ...] = (
    "자기주식",
    "주식담보",
    "담보제공",
    "유상증자",
    "전환사채",
    "신주인수권",
    "타법인",
    "채무보증",
    "소송",
    "해명공시",
    "조회공시",
)

_FORBIDDEN_EXISTING_EVIDENCE_CONTEXT_KEYS: frozenset[str] = frozenset(
    {
        "accepted_claim_final",
        "current_score_eligible",
        "expected_stage",
        "green_unlock_score",
        "hard_break_final",
        "score",
        "source_base_stage",
        "source_score_contribution_ids",
        "source_stage_decision_status",
        "source_stage_signal",
        "stage",
        "target_score",
        "target_stage",
        "verified_final",
    }
)
_FORBIDDEN_EXISTING_EVIDENCE_CONTEXT_KEY_FRAGMENTS: tuple[str, ...] = (
    "current_score_eligible",
    "score_contribution",
    "stage_decision",
    "stage_signal",
)
_FORBIDDEN_PLANNER_CONTEXT_ASSIGNMENT_RE = re.compile(
    r"(^|[;\s])([A-Za-z0-9_]*(?:score|stage)[A-Za-z0-9_]*)=([^;]*)(;?)",
    re.IGNORECASE,
)


def _is_forbidden_existing_evidence_context_key(key: object) -> bool:
    normalized = str(key).strip().lower()
    if normalized in _FORBIDDEN_EXISTING_EVIDENCE_CONTEXT_KEYS:
        return True
    if normalized.endswith("_score") or normalized.endswith("_stage"):
        return True
    if normalized.startswith("source_stage"):
        return True
    return any(fragment in normalized for fragment in _FORBIDDEN_EXISTING_EVIDENCE_CONTEXT_KEY_FRAGMENTS)


def sanitize_existing_evidence_summary_v4(value: Any) -> Any:
    """Remove score/stage-like hints before planner prompt construction.

    The planner may see missing evidence and prior source failures, but it must
    not receive target scores, stage labels, or eligibility conclusions as
    context. This helper is recursive because feedback rows can contain nested
    provider/debug payloads.
    """

    if isinstance(value, Mapping):
        return {
            str(key): sanitize_existing_evidence_summary_v4(item)
            for key, item in value.items()
            if not _is_forbidden_existing_evidence_context_key(key)
        }
    if isinstance(value, (list, tuple)):
        return [sanitize_existing_evidence_summary_v4(item) for item in value]
    return value


def _sanitize_planner_context_text_v4(value: Any) -> str:
    cleaned = _FORBIDDEN_PLANNER_CONTEXT_ASSIGNMENT_RE.sub(" ", str(value or ""))
    return re.sub(r"\s+", " ", cleaned).strip(" ;")


def _is_forbidden_candidate_event_context_key(key: object) -> bool:
    normalized = str(key).strip().lower()
    if _is_forbidden_existing_evidence_context_key(normalized):
        return True
    return "score" in normalized or "stage" in normalized


def _sanitize_candidate_event_for_planner_v4(value: Any, *, parent_key: str | None = None) -> Any:
    """Remove event-board score/stage hints from planner candidate context.

    Census full-thesis seeds can carry prior event-board diagnostics such as
    source_stage_signal or source_base_stage. Those are useful audit facts, but
    they must not become planner evidence or target-stage hints.
    """

    if isinstance(value, Mapping):
        sanitized: dict[str, Any] = {}
        for key, item in value.items():
            key_text = str(key)
            if _is_forbidden_candidate_event_context_key(key_text):
                continue
            if key_text == "raw_reason_codes" and isinstance(item, (list, tuple)):
                sanitized[key_text] = [
                    _sanitize_planner_context_text_v4(code)
                    for code in item
                    if "score" not in str(code).lower() and "stage" not in str(code).lower()
                ]
                continue
            if key_text == "event_summary":
                sanitized[key_text] = _sanitize_planner_context_text_v4(item)
                continue
            sanitized[key_text] = _sanitize_candidate_event_for_planner_v4(item, parent_key=key_text)
        return sanitized
    if isinstance(value, (list, tuple)):
        return [
            _sanitize_candidate_event_for_planner_v4(item, parent_key=parent_key)
            for item in value
        ]
    if isinstance(value, str):
        return _sanitize_planner_context_text_v4(value)
    return value


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
                                "query_intents": {"type": "array", "items": {"type": "string"}},
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
                                "query_intents",
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
        self._last_rejection_by_event_id = {}
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
            try:
                outputs[event_id] = validate_llm_planner_output_v4(
                    row,
                    event=event,
                    memory_cards=memory_cards,
                )
            except (PlannerProviderRejected, ValueError) as exc:
                self._last_rejection_by_event_id[event_id] = str(exc)
        if not outputs:
            if self._last_rejection_by_event_id:
                sample = "; ".join(
                    f"{event_id}:{reason}"
                    for event_id, reason in list(self._last_rejection_by_event_id.items())[:3]
                )
                raise PlannerProviderRejected(f"codex planner returned only rejected plans: {sample}")
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
        if self.model and self.model != "codex-cli-default":
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
            model=_optional_env(env, "E2R_CODEX_PLANNER_MODEL") or "codex-cli-default",
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
    prompt_payload = _planner_prompt_payload_for_trace(
        events=events,
        memory_cards=memory_cards,
        existing_evidence_by_event_id=existing_evidence_by_event_id or {},
    )
    prompt_text = _planner_prompt(prompt_payload)
    prompt_hash = _sha256_text(prompt_text)
    if provider is not None and hasattr(provider, "_last_rejection_by_event_id"):
        setattr(provider, "_last_rejection_by_event_id", {})
    try:
        outputs = provider.plan_many(
            events=events,
            memory_cards=memory_cards,
            existing_evidence_by_event_id=existing_evidence_by_event_id or {},
        )
    except PlannerProviderRejected as exc:
        return tuple(
            _failed_run(
                provider,
                event,
                str(exc),
                rejected=True,
                prompt_payload=prompt_payload,
                prompt_text=prompt_text,
                prompt_hash=prompt_hash,
            )
            for event in events
        )
    except PlannerProviderUnavailable as exc:
        return tuple(
            _failed_run(
                provider,
                event,
                str(exc),
                rejected=False,
                prompt_payload=prompt_payload,
                prompt_text=prompt_text,
                prompt_hash=prompt_hash,
            )
            for event in events
        )
    except ValueError as exc:
        return tuple(
            _failed_run(
                provider,
                event,
                str(exc),
                rejected=True,
                prompt_payload=prompt_payload,
                prompt_text=prompt_text,
                prompt_hash=prompt_hash,
            )
            for event in events
        )
    rows: list[PlannerRunV4] = []
    rejected_by_event_id = getattr(provider, "_last_rejection_by_event_id", {}) or {}
    for event in events:
        output = outputs.get(event.candidate_event_id)
        if output is None:
            rejected_reason = rejected_by_event_id.get(event.candidate_event_id)
            rows.append(
                _failed_run(
                    provider,
                    event,
                    rejected_reason or "planner_output_missing_for_candidate",
                    rejected=bool(rejected_reason),
                    prompt_payload=prompt_payload,
                    prompt_text=prompt_text,
                    prompt_hash=prompt_hash,
                )
            )
            continue
        response_payload = {
            "schema_version": "research_brain_v4_planner_response_leaf_v1",
            "candidate_event_id": event.candidate_event_id,
            "output": output.to_dict(),
        }
        response_text = _json_dumps_stable(response_payload)
        response_hash = _sha256_text(response_text)
        planner_run_id = _planner_run_id(
            event=event,
            provider_name=provider.provider_name,
            prompt_hash=prompt_hash,
            response_hash=response_hash,
        )
        rows.append(
            PlannerRunV4(
                event=event,
                provider_name=provider.provider_name,
                provider_mode=provider.provider_mode,
                real_provider_exercised=bool(provider.real_provider),
                real_provider_success=bool(provider.real_provider),
                fake_provider_used=bool(provider.fake_provider),
                planner_run_id=planner_run_id,
                output=output,
                model=getattr(provider, "model", None),
                endpoint=getattr(provider, "endpoint", None),
                prompt_hash=prompt_hash,
                response_hash=response_hash,
                raw_prompt_path=_planner_raw_prompt_path(planner_run_id),
                raw_response_path=_planner_raw_response_path(planner_run_id),
                prompt_payload=prompt_payload,
                prompt_text=prompt_text,
                response_payload=response_payload,
                response_text=response_text,
            )
        )
    return tuple(rows)


def source_tasks_from_planner_output_v4(
    *,
    event: CandidateEventV2,
    planner_output: LLMPlannerOutputV2,
    card_by_id: Mapping[str, ArchetypeMemoryCard],
    max_tasks: int = 5,
    max_fetches_per_task: int | None = None,
) -> tuple[SourceTask, ...]:
    primary = str(planner_output.top_k_archetype_hypotheses[0].get("archetype_id"))
    card = card_by_id[primary]
    tasks: list[SourceTask] = []
    for draft in _selected_source_task_drafts(planner_output=planner_output, max_tasks=max_tasks):
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
                max_fetches=_bounded_task_fetches(
                    int(draft.get("max_fetches") or 3),
                    max_fetches_per_task=max_fetches_per_task,
                ),
                stop_condition=draft.get("stop_condition") or {"accepted_claim_count": 1},
                query_intents=_source_task_query_intents(draft=draft, planner_output=planner_output),
                llm_query_allowed=bool(draft.get("llm_query_allowed", True)),
                general_search_allowed=bool(draft.get("general_search_allowed", False)),
                reason_from_memory=str(draft.get("reason_from_memory") or f"planner_v4:{primary}:{primitive}"),
                memory_record_ids=card.representative_url_backed_fixture_ids[:5],
            )
        )
    return tuple(tasks)


def _source_task_query_intents(*, draft: Mapping[str, Any], planner_output: LLMPlannerOutputV2) -> tuple[str, ...]:
    task_specific = _clean_query_intents(draft.get("query_intents") or ())
    if task_specific:
        return task_specific
    return _clean_query_intents(planner_output.query_intents)


def _clean_query_intents(values: Sequence[Any]) -> tuple[str, ...]:
    rows: list[str] = []
    for value in values:
        text = str(value or "").strip()
        if not text:
            continue
        rows.append(text)
    return tuple(dict.fromkeys(rows))


def _bounded_task_fetches(value: int, *, max_fetches_per_task: int | None) -> int:
    if max_fetches_per_task is None:
        return max(1, value)
    return max(1, min(value, int(max_fetches_per_task)))


def _selected_source_task_drafts(*, planner_output: LLMPlannerOutputV2, max_tasks: int) -> tuple[Mapping[str, Any], ...]:
    drafts = tuple(planner_output.source_task_drafts)
    if max_tasks <= 0:
        return ()
    selected = list(drafts[:max_tasks])
    if not tuple(str(item).strip() for item in planner_output.query_intents if str(item).strip()):
        return tuple(selected)
    if any(_draft_requests_external_web(draft) for draft in selected):
        return tuple(selected)
    external = next((draft for draft in drafts[max_tasks:] if _draft_requests_external_web(draft)), None)
    if external is None:
        return tuple(selected)
    if selected:
        selected[-1] = external
    else:
        selected.append(external)
    return tuple(selected)


def _draft_requests_external_web(draft: Mapping[str, Any]) -> bool:
    primitive = str(draft.get("primitive_gap") or draft.get("primitive_id") or "")
    if _is_official_solvable_gap(primitive):
        return False
    external = {
        "naversearch",
        "generalwebsearch",
        "trustednews",
        "news",
        "industrymedia",
        "companynewsroom",
        "reportpdf",
        "brokerreportpublicpdf",
    }
    names = {
        "".join(ch for ch in str(item or "").lower() if ch.isalnum())
        for item in (
            *(draft.get("preferred_source_classes") or ()),
            *(draft.get("fallback_source_classes") or ()),
        )
    }
    return bool(names & external)


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
        signal_profile = _event_signal_profile(event)
        route = route_candidate_event_v2(event, memory_cards, top_k=5)
        options = []
        option_ids: set[str] = set()
        for candidate in route.top_k_archetypes:
            card = card_by_id.get(candidate.archetype_id)
            contract = contracts.get(candidate.archetype_id)
            option = _planner_option_payload(
                archetype_id=candidate.archetype_id,
                router_score=candidate.probability_or_score,
                router_reason=candidate.reason,
                card=card,
                contract=contract,
            )
            options.append(option)
            option_ids.add(candidate.archetype_id)
        if signal_profile["direct_revenue_contract_disclosure"]:
            for option in _contract_compatible_option_payloads(
                cards=memory_cards,
                contracts=contracts,
                card_by_id=card_by_id,
                existing_option_ids=option_ids,
            ):
                options.append(option)
                option_ids.add(str(option["archetype_id"]))
            options.sort(key=_contract_event_option_sort_key)
        event_payloads.append(
            {
                "candidate_event": _sanitize_candidate_event_for_planner_v4(event.to_dict()),
                "event_signal_profile": signal_profile,
                "existing_evidence_summary": sanitize_existing_evidence_summary_v4(
                    existing_evidence_by_event_id.get(event.candidate_event_id, {})
                ),
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
            "query_intents must be bounded company-scoped executable search queries containing the company name or ticker when external web/news fallback is needed.",
            "When different source_task_drafts need different searches, put task-specific query_intents inside each source_task_draft; those task-specific queries override the top-level query_intents for that task.",
            "If event_signal_profile.direct_revenue_contract_disclosure is true, prefer the highest event_signal_fit_score allowed_archetype_options item with contract_compatible=true and use one of its contract_compatible_primitives for source_task_drafts.primitive_gap. Prefer contract_amount_to_prior_sales or contract_duration_months over generic contract_quality when available. If you choose a non-contract-compatible archetype, you must plan source tasks that prove an issuer-specific volume, mix, margin, or cash bridge beyond the contract existence itself.",
            "If existing_evidence_summary.brain_web_acquisition_required is true, include at least one target-scoped query_intent and at least one non-official-solvable source_task_draft whose preferred_source_classes or fallback_source_classes includes TrustedNews, NaverSearch, GeneralWebSearch, ReportPDF, BrokerReportPublicPDF, IndustryMedia, or CompanyNewsroom. The query text must be written by you from the candidate context; deterministic code will only validate and execute it.",
            "If existing_evidence_summary.planner_feedback contains query_intents_empty or no_external_web_source_task, repair those exact gaps without adding scores or stages.",
            "If existing_evidence_summary.rejected_claim_feedback contains contract_compatible_route_required=true, the previous source contained contract fields but the selected primitive was incompatible. Do not repeat volume/mix/leverage primitives unless you add a separate bridge source; reroute to a contract_compatible archetype/primitive when available.",
            "If existing_evidence_summary.rejected_claim_feedback is non-empty, those fetched claims were rejected before scoring. Do not repeat the same rejected source/subject pattern; plan a different bounded source_task/query that can prove the primitive directly. Still do not output score, stage, verified final, current_score_eligible, or accepted claim final.",
            "If existing_evidence_summary.source_rejection_feedback is non-empty, previous source candidates were rejected before extraction or failed post-extraction score/source admissibility. Do not repeat the same URL/source pattern; plan a different bounded source_task/query aimed at issuer IR, DART/KIND detail, report PDF, company newsroom, trusted article original, or another source class that can prove the primitive directly. Still do not output score, stage, verified final, current_score_eligible, or accepted claim final.",
            "If source_rejection_feedback.not_eligible_reason_distribution contains source_lineage_unverified_original, treat the prior web/news/report result as discovery-only, not a verified original source. Prefer an official detail URL, issuer-hosted IR/newsroom page, report PDF original, or trusted article original before retrying generic web search.",
            "If existing_evidence_summary.rerouted_claim_feedback is non-empty, the previous claim was accepted for a different primitive but did not satisfy the requested primitive_gap. Preserve that accepted evidence as context, but plan a different bounded source_task/query for primitive_gap_unsatisfied_ids. Do not repeat the same source class/document if it only produced the rerouted primitive, and still do not output score, stage, verified final, current_score_eligible, or accepted claim final.",
            "If existing_evidence_summary.full_thesis_queue_context.planner_failure_feedback is non-empty, treat it as source-route repair guidance only. It is not score evidence. Use previous_claim_failure_primary_mode and source_route_repair_actions to avoid repeating the prior rejected claim pattern and produce source_task_drafts/query_intents that can create a new source-backed claim for the primitive_gap.",
            "If previous_claim_failure_primary_mode is ROUTE_GENERIC_DISCLOSURE_NOT_PRIMITIVE_EVIDENCE, do not plan generic disclosure cover/profile/company-overview text as the evidence route. Prefer a primitive-specific issuer section, IR material, original report, newsroom source, trusted original article, or document section that directly states the missing primitive.",
            "If previous_claim_failure_primary_mode is ROUTE_SIGNAL_FAMILY_MISMATCH, make the next source family match the primitive family. For example, a clinical trial primitive needs endpoint/regulatory/trial evidence, while a retention primitive needs ARR/RPO/renewal/retention evidence; do not repeat a mismatched contract-style route unless it directly proves the primitive.",
            "R13 may be primary only when the event explicitly says red-team, false-positive, or cross-archetype review.",
        ],
        "forbidden_output_keys": sorted(FORBIDDEN_RESEARCH_BRAIN_OUTPUT_KEYS),
    }


def _planner_option_payload(
    *,
    archetype_id: str,
    router_score: float,
    router_reason: str,
    card: ArchetypeMemoryCard | None,
    contract: Any | None,
    event_signal_fit_score: int | None = None,
) -> Mapping[str, Any]:
    required_primitives = tuple(contract.required_primitives if contract else (card.required_primitives if card else ()))
    allowed_primitives = (
        tuple(sorted(_allowed_primitives_from_contract(contract)))
        if contract is not None
        else required_primitives
    )
    contract_primitives = tuple(primitive for primitive in allowed_primitives if primitive in CONTRACT_COMPATIBLE_PRIMITIVES)
    if event_signal_fit_score is None and contract_primitives:
        event_signal_fit_score = _contract_option_fit_score(contract_primitives)
    return {
        "archetype_id": archetype_id,
        "router_score": router_score,
        "router_reason": router_reason,
        "event_signal_fit_score": event_signal_fit_score,
        "allowed_primitives": list(allowed_primitives),
        "contract_compatible": bool(contract_primitives),
        "contract_compatible_primitives": list(contract_primitives),
        "preferred_source_routes": {
            key: list(value)
            for key, value in (card.source_route_by_primitive.items() if card else ())
            if key in allowed_primitives
        },
        "green_blockers": list(card.green_blockers[:5] if card else ()),
        "do_not_promote_rules": list(card.do_not_promote_rules[:5] if card else ()),
    }


def _contract_compatible_option_payloads(
    *,
    cards: Sequence[ArchetypeMemoryCard],
    contracts: Mapping[str, Any],
    card_by_id: Mapping[str, ArchetypeMemoryCard],
    existing_option_ids: set[str],
    limit: int = 3,
) -> tuple[Mapping[str, Any], ...]:
    rows: list[tuple[int, str, Mapping[str, Any]]] = []
    for card in cards:
        if card.archetype_id in existing_option_ids:
            continue
        contract = contracts.get(card.archetype_id)
        if contract is None:
            continue
        compatible = sorted(_allowed_primitives_from_contract(contract) & CONTRACT_COMPATIBLE_PRIMITIVES)
        if not compatible:
            continue
        fit_score = _contract_option_fit_score(compatible)
        rows.append(
            (
                -fit_score,
                card.archetype_id,
                _planner_option_payload(
                    archetype_id=card.archetype_id,
                    router_score=float(fit_score),
                    router_reason="event_signal_profile:direct_revenue_contract_disclosure_contract_compatible_option_ordered_by_primitive_fit",
                    card=card_by_id.get(card.archetype_id),
                    contract=contract,
                    event_signal_fit_score=fit_score,
                ),
            )
        )
    rows.sort(key=lambda item: (item[0], item[1]))
    return tuple(row for _, _, row in rows[:limit])


def _contract_event_option_sort_key(option: Mapping[str, Any]) -> tuple[int, int, str]:
    return (
        0 if option.get("contract_compatible") else 1,
        -int(option.get("event_signal_fit_score") or 0),
        str(option.get("archetype_id") or ""),
    )


def _contract_option_fit_score(compatible_primitives: Sequence[str]) -> int:
    priorities = {
        "contract_amount_to_prior_sales": 100,
        "contract_duration_months": 80,
        "revenue_visibility_contract": 70,
        "contract_visibility": 50,
        "delivery_schedule": 40,
        "order_backlog_to_sales": 30,
        "order_to_revenue_bridge": 30,
        "export_contract": 20,
        "contract_quality": 10,
    }
    return sum(priorities.get(primitive, 1) for primitive in set(compatible_primitives))


def _event_signal_profile(event: CandidateEventV2) -> Mapping[str, Any]:
    text = _event_signal_text(event)
    contract_terms = tuple(term for term in _REVENUE_CONTRACT_TERMS if term.lower() in text)
    false_positive_terms = tuple(term for term in _NON_REVENUE_CONTRACT_TERMS if term.lower() in text)
    direct_revenue_contract = bool(contract_terms) and not bool(false_positive_terms)
    return {
        "direct_revenue_contract_disclosure": direct_revenue_contract,
        "contract_signal_terms": list(contract_terms[:8]),
        "non_revenue_contract_terms": list(false_positive_terms[:8]),
        "contract_compatible_primitive_hints": sorted(CONTRACT_COMPATIBLE_PRIMITIVES),
    }


def _event_signal_text(event: CandidateEventV2) -> str:
    structured = event.structured_payload if isinstance(event.structured_payload, Mapping) else {}
    return " ".join(
        str(value or "")
        for value in (
            event.source_family,
            event.source_id,
            event.event_type,
            event.primary_disclosure_type,
            event.event_title,
            event.event_summary,
            " ".join(str(code) for code in event.raw_reason_codes),
            json.dumps(structured, ensure_ascii=False, sort_keys=True),
        )
    ).lower()


def _planner_prompt_payload_for_trace(
    *,
    events: Sequence[CandidateEventV2],
    memory_cards: Sequence[ArchetypeMemoryCard],
    existing_evidence_by_event_id: Mapping[str, Mapping[str, Any]],
) -> Mapping[str, Any]:
    if memory_cards:
        return build_v4_planner_prompt_payload(
            events=events,
            memory_cards=memory_cards,
            existing_evidence_by_event_id=existing_evidence_by_event_id,
        )
    return {
        "schema_version": "research_brain_v4_planner_prompt_minimal_trace",
        "events": [
            {
                "candidate_event": _sanitize_candidate_event_for_planner_v4(event.to_dict()),
                "existing_evidence_summary": sanitize_existing_evidence_summary_v4(
                    existing_evidence_by_event_id.get(event.candidate_event_id, {})
                ),
                "allowed_archetype_options": [],
            }
            for event in events
        ],
        "rules": [
            "Minimal trace payload used when tests inject a planner provider without memory cards.",
            "Do not output score, stage, hard_break final, verified final, current_score_eligible, or accepted claim final.",
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
    allowed_primitives = _allowed_primitives_for_primary(primary)
    valid_must_verify = tuple(
        normalized
        for primitive in output.must_verify_primitives
        for normalized in (_normalize_planner_primitive_for_contract(primitive, allowed_primitives),)
        if normalized
    )
    valid_source_task_drafts: list[Mapping[str, Any]] = []
    for draft in output.source_task_drafts:
        sanitized_draft = _sanitize_source_task_draft_v4(draft)
        primitive = _normalize_planner_primitive_for_contract(
            str(sanitized_draft.get("primitive_gap") or sanitized_draft.get("primitive_id") or "").strip(),
            allowed_primitives,
        )
        if primitive:
            sanitized_draft = dict(sanitized_draft)
            sanitized_draft["primitive_gap"] = primitive
        _validate_source_task_draft_v4(sanitized_draft)
        primitive = str(sanitized_draft.get("primitive_gap") or sanitized_draft.get("primitive_id") or "").strip()
        if primitive in allowed_primitives:
            valid_source_task_drafts.append(sanitized_draft)
    sanitized = output.to_dict()
    sanitized["must_verify_primitives"] = list(valid_must_verify)
    sanitized["source_task_drafts"] = valid_source_task_drafts
    if output.source_task_drafts and not valid_source_task_drafts:
        raise PlannerProviderRejected(f"all source_task primitives are outside primary archetype contract: {primary}")
    return validate_llm_planner_output_v3(sanitized, event=event, memory_cards=memory_cards)


def _allowed_primitives_for_primary(primary: str) -> set[str]:
    contracts = load_evidence_contracts_v2(require_all_archetypes=False)
    contract = contracts.get(primary)
    if contract is None:
        return set()
    return _allowed_primitives_from_contract(contract)


def _allowed_primitives_from_contract(contract: Any) -> set[str]:
    values: set[str] = set(contract.required_primitives)
    values.update(contract.green_gate.primitive_ids())
    values.update(contract.alternative_primitives)
    for primitives in contract.alternative_primitives.values():
        values.update(primitives)
    for primitives in contract.score_rubric.values():
        values.update(primitives)
    values.update(contract.primitive_aliases)
    values.update(contract.freshness)
    return values


def _normalize_planner_primitive_for_contract(primitive: str, allowed_primitives: set[str]) -> str | None:
    if primitive == "contract_quality":
        for candidate in (
            "contract_amount_to_prior_sales",
            "revenue_visibility_contract",
            "contract_duration_months",
            "contract_visibility",
            "delivery_schedule",
            "export_contract",
        ):
            if candidate in allowed_primitives:
                return candidate
    if primitive in allowed_primitives:
        return primitive
    return None


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
        "query_intents": [f"verify {primitive}"],
        "reason_from_memory": f"{card.archetype_id if card else 'UNKNOWN'}:{primitive}",
    }


def _sanitize_source_task_draft_v4(draft: Mapping[str, Any]) -> Mapping[str, Any]:
    primitive = str(draft.get("primitive_gap") or draft.get("primitive_id") or "").strip()
    if not _is_official_solvable_gap(primitive):
        return dict(draft)
    sanitized = dict(draft)
    disallowed = {"generalweb", "web", "newsonly", "trustednews", "news", "naversearch", "generalwebsearch"}
    preferred = _without_external_web_sources(draft.get("preferred_source_classes") or (), disallowed=disallowed)
    fallback = _without_external_web_sources(draft.get("fallback_source_classes") or (), disallowed=disallowed)
    if not preferred:
        preferred = ("DART", "CompanyGuide", "IR")
    if not fallback:
        fallback = ("IssuerOfficial", "IR")
    sanitized["preferred_source_classes"] = list(preferred)
    sanitized["fallback_source_classes"] = list(fallback)
    sanitized["general_search_allowed"] = False
    return sanitized


def _without_external_web_sources(values: Sequence[Any], *, disallowed: set[str]) -> tuple[str, ...]:
    rows: list[str] = []
    for value in values:
        raw = str(value or "").strip()
        normalized = "".join(ch for ch in raw.lower() if ch.isalnum())
        if not raw or normalized in disallowed:
            continue
        rows.append(raw)
    return tuple(dict.fromkeys(rows))


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
    prompt_payload: Mapping[str, Any] | None = None,
    prompt_text: str | None = None,
    prompt_hash: str | None = None,
) -> PlannerRunV4:
    response_payload = {
        "schema_version": "research_brain_v4_planner_response_leaf_v1",
        "candidate_event_id": event.candidate_event_id,
        "provider_error": provider_error,
        "rejected_by_validator": rejected,
    }
    response_text = _json_dumps_stable(response_payload)
    response_hash = _sha256_text(response_text)
    planner_run_id = _planner_run_id(
        event=event,
        provider_name=provider.provider_name,
        prompt_hash=prompt_hash,
        response_hash=response_hash,
    )
    return PlannerRunV4(
        event=event,
        provider_name=provider.provider_name,
        provider_mode=provider.provider_mode,
        real_provider_exercised=False if provider_error else bool(provider.real_provider),
        real_provider_success=False,
        fake_provider_used=bool(provider.fake_provider),
        planner_run_id=planner_run_id,
        provider_error=provider_error,
        rejected_by_validator=rejected,
        r13_invalid_primary_rejected="R13 primary" in provider_error,
        model=getattr(provider, "model", None),
        endpoint=getattr(provider, "endpoint", None),
        prompt_hash=prompt_hash,
        response_hash=response_hash,
        raw_prompt_path=_planner_raw_prompt_path(planner_run_id) if prompt_hash else None,
        raw_response_path=_planner_raw_response_path(planner_run_id),
        prompt_payload=prompt_payload,
        prompt_text=prompt_text,
        response_payload=response_payload,
        response_text=response_text,
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


def _json_dumps_stable(payload: Mapping[str, Any]) -> str:
    return json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _sha256_text(text: str | None) -> str | None:
    if text is None:
        return None
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _planner_run_id(
    *,
    event: CandidateEventV2,
    provider_name: str,
    prompt_hash: str | None,
    response_hash: str | None,
) -> str:
    return deterministic_id(
        "PLANV4",
        (
            event.candidate_event_id,
            provider_name,
            prompt_hash or "",
            response_hash or "",
        ),
    )


def _planner_raw_prompt_path(planner_run_id: str) -> str:
    return f"planner_raw/prompts/{planner_run_id}.json"


def _planner_raw_response_path(planner_run_id: str) -> str:
    return f"planner_raw/responses/{planner_run_id}.json"


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


_OFFICIAL_SOLVABLE_PRIMITIVE_IDS = {
    "contract_visibility",
    "contract_amount_to_prior_sales",
    "contract_duration_months",
    "contract_quality",
    "delivery_schedule",
    "export_contract",
    "order_backlog_to_sales",
    "order_to_revenue_bridge",
    "revenue_visibility_contract",
}


def _is_official_solvable_gap(primitive: str) -> bool:
    lower = primitive.lower()
    if lower in _OFFICIAL_SOLVABLE_PRIMITIVE_IDS:
        return True
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
