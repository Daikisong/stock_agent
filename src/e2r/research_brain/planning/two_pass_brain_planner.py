"""Blind Pass A plus balanced-memory Pass B Research Brain planner."""

from __future__ import annotations

import hashlib
import json
import os
import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any, Callable, Iterable, Mapping, Sequence

from e2r.calibration.taxonomy import (
    CANONICAL_ARCHETYPE_IDS,
    LARGE_SECTOR_IDS,
    large_sector_for_archetype,
    normalise_large_sector_id,
)
from e2r.env import load_project_env
from e2r.production.metadata import write_json
from e2r.research_brain.intelligence_schema import (
    ArchetypeHypothesis,
    BalancedRetrievalRequest,
    BlindHypothesisInput,
    BlindHypothesisOutput,
    BlindMechanismHypothesis,
    CurrentEvidenceFact,
    HypothesisStrength,
    MemoryCritiqueInput,
    MemoryCritiqueOutput,
    PlannerPass,
    PlannerPending,
    PlannerSourceTaskDraft,
    PlannerStatus,
    ProviderCallTrace,
    TwoPassPlan,
    stable_intelligence_id,
)
from e2r.research_brain.planning.provider_transport import (
    CodexStructuredProviderTransport,
    StructuredProviderRejected,
    StructuredProviderUnavailable,
)
from e2r.research_brain.retrieval import (
    SemanticMemoryIndex,
    retrieve_balanced_memory,
)


TWO_PASS_PLANNER_SCHEMA_VERSION = "e2r_two_pass_research_brain_v1"

_CANONICAL_ARCHETYPE_RE = re.compile(
    r"(?:^|[^A-Za-z0-9])(?:C[0-9]{2}|R13)_[A-Z0-9_]+(?:$|[^A-Za-z0-9])",
    re.IGNORECASE,
)
_FORBIDDEN_CONTEXT_KEY_FRAGMENTS = (
    "score",
    "stage",
    "outcome",
    "mfe",
    "mae",
    "source_primary",
    "expected_archetype",
    "expected_primitive",
    "price_context",
)
_FORBIDDEN_TEXT_ASSIGNMENT_RE = re.compile(
    r"(?:^|[;\s])(?:[A-Za-z0-9_]*(?:score|stage|source_primary|"
    r"expected_archetype|expected_primitive|outcome_label|mfe|mae)[A-Za-z0-9_]*)"
    r"\s*=\s*[^;]+;?",
    re.IGNORECASE,
)
_FORBIDDEN_OUTCOME_TEXT_RE = re.compile(
    r"(?:^|[^a-z0-9])(?:mfe(?:[_-]?[0-9]+[a-z]*)?|"
    r"mae(?:[_-]?[0-9]+[a-z]*)?|future[_ -]?outcome|"
    r"outcome[_ -]?label|expected[_ -]?stage)(?:$|[^a-z0-9])",
    re.IGNORECASE,
)
_FORBIDDEN_PLANNER_CONTEXT_TEXT_RE = re.compile(
    r"(?:target[_ -]?score|expected[_ -]?stage|source[_ -]?primary|"
    r"(?:e2r|final|planner|target)\s+score\s*(?:[:=]|is|was)?\s*[0-9]|"
    r"score\s*(?:[:=]|is\s|was\s|of\s)\s*[0-9]|"
    r"(?:canonical|e2r|expected|target)\s+stage|"
    r"stage\s*[:=]\s*(?:0|1|2|3|4[abc]?|5|3-(?:green|yellow|red))|"
    r"stage\s+(?:3-(?:green|yellow|red)|4[abc]))",
    re.IGNORECASE,
)
_TARGET_DIRECT_RELATIONS = frozenset({"DIRECT", "ISSUER", "SELF", "TARGET"})
_CURRENT_FACT_STATUSES = frozenset({"ACTIVE", "CONFIRMED", "CURRENT", "EFFECTIVE"})
_OFFICIAL_FIRST_FAMILIES = frozenset(
    {
        "DART",
        "KIND",
        "KRX",
        "IssuerIR",
        "IssuerNewsroom",
        "CompanyEarningsCall",
        "CompanyGuide",
        "SEC",
        "Regulator",
        "ClinicalTrialRegistry",
        "CustomerOfficial",
        "CustomerNewsroom",
        "PeerReviewedPublication",
        "IndustryData",
    }
)
_PASS_A_TOP_LEVEL_KEYS = frozenset(
    {"input_id", "hypotheses", "ambiguity_reasons", "abstain", "abstention_reason"}
)
_PASS_A_HYPOTHESIS_KEYS = frozenset(
    {
        "hypothesis_id",
        "rank",
        "mechanism_summary",
        "strength",
        "supporting_fact_ids",
        "contradicting_fact_ids",
        "must_verify_questions",
    }
)
_PASS_B_TOP_LEVEL_KEYS = frozenset(
    {
        "input_id",
        "top_k_archetypes",
        "supporting_current_fact_ids",
        "contradicting_current_fact_ids",
        "positive_thesis",
        "counter_thesis",
        "must_verify_questions",
        "red_team_questions",
        "source_task_drafts",
        "do_not_promote_reasons",
        "ambiguity_reasons",
        "abstain",
        "abstention_reason",
    }
)
_PASS_B_ARCHETYPE_KEYS = frozenset(
    {
        "archetype_id",
        "rank",
        "reason",
        "supporting_fact_ids",
        "contradicting_fact_ids",
        "recipe_ids",
    }
)
_PASS_B_DRAFT_KEYS = frozenset(
    {
        "draft_id",
        "recipe_id",
        "question_to_answer",
        "why_material",
        "query_intent",
        "preferred_source_families",
        "fallback_source_families",
        "max_queries",
        "max_candidates",
        "max_fetches",
        "stop_condition",
    }
)


PASS_A_OUTPUT_SCHEMA: Mapping[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "input_id": {"type": "string"},
        "hypotheses": {
            "type": "array",
            "maxItems": 5,
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "hypothesis_id": {"type": "string", "minLength": 1},
                    "rank": {"type": "integer"},
                    "mechanism_summary": {"type": "string", "minLength": 1},
                    "strength": {"type": "string", "enum": ["HIGH", "MEDIUM", "LOW"]},
                    "supporting_fact_ids": {"type": "array", "minItems": 1, "items": {"type": "string"}},
                    "contradicting_fact_ids": {"type": "array", "items": {"type": "string"}},
                    "must_verify_questions": {"type": "array", "minItems": 1, "items": {"type": "string"}},
                },
                "required": list(sorted(_PASS_A_HYPOTHESIS_KEYS)),
            },
        },
        "ambiguity_reasons": {"type": "array", "items": {"type": "string"}},
        "abstain": {"type": "boolean"},
        "abstention_reason": {"type": "string"},
    },
    "required": list(sorted(_PASS_A_TOP_LEVEL_KEYS)),
}

PASS_B_OUTPUT_SCHEMA: Mapping[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "input_id": {"type": "string"},
        "top_k_archetypes": {
            "type": "array",
            "maxItems": 5,
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "archetype_id": {"type": "string", "minLength": 1},
                    "rank": {"type": "integer"},
                    "reason": {"type": "string", "minLength": 1},
                    "supporting_fact_ids": {"type": "array", "minItems": 1, "items": {"type": "string"}},
                    "contradicting_fact_ids": {"type": "array", "items": {"type": "string"}},
                    "recipe_ids": {"type": "array", "items": {"type": "string"}},
                },
                "required": list(sorted(_PASS_B_ARCHETYPE_KEYS)),
            },
        },
        "supporting_current_fact_ids": {"type": "array", "minItems": 1, "items": {"type": "string"}},
        "contradicting_current_fact_ids": {"type": "array", "items": {"type": "string"}},
        "positive_thesis": {"type": "string"},
        "counter_thesis": {"type": "string"},
        "must_verify_questions": {"type": "array", "minItems": 1, "items": {"type": "string"}},
        "red_team_questions": {"type": "array", "minItems": 1, "items": {"type": "string"}},
        "source_task_drafts": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "draft_id": {"type": "string", "minLength": 1},
                    "recipe_id": {"type": "string", "minLength": 1},
                    "question_to_answer": {"type": "string", "minLength": 1},
                    "why_material": {"type": "string", "minLength": 1},
                    "query_intent": {"type": "string", "minLength": 1},
                    "preferred_source_families": {"type": "array", "minItems": 1, "items": {"type": "string"}},
                    "fallback_source_families": {"type": "array", "items": {"type": "string"}},
                    "max_queries": {"type": "integer"},
                    "max_candidates": {"type": "integer"},
                    "max_fetches": {"type": "integer"},
                    "stop_condition": {"type": "string", "minLength": 1},
                },
                "required": list(sorted(_PASS_B_DRAFT_KEYS)),
            },
        },
        "do_not_promote_reasons": {"type": "array", "minItems": 1, "items": {"type": "string"}},
        "ambiguity_reasons": {"type": "array", "items": {"type": "string"}},
        "abstain": {"type": "boolean"},
        "abstention_reason": {"type": "string"},
    },
    "required": list(sorted(_PASS_B_TOP_LEVEL_KEYS)),
}


@dataclass(frozen=True)
class BlindInputCompilationResult:
    blind_input: BlindHypothesisInput
    audit: Mapping[str, int]


@dataclass(frozen=True)
class ProviderCompletion:
    payload: Mapping[str, Any]
    raw_response: str


class TwoPassPlannerProvider:
    provider_name = "abstract"
    real_provider = False
    fake_provider = False

    def complete(
        self,
        *,
        planner_pass: str,
        prompt: str,
        output_schema: Mapping[str, Any],
    ) -> ProviderCompletion:
        raise NotImplementedError


@dataclass
class CodexTwoPassPlannerProvider(TwoPassPlannerProvider):
    transport: CodexStructuredProviderTransport

    provider_name = "codex_cli_two_pass_planner"
    real_provider = True
    fake_provider = False

    def complete(
        self,
        *,
        planner_pass: str,
        prompt: str,
        output_schema: Mapping[str, Any],
    ) -> ProviderCompletion:
        response = self.transport.complete(
            prompt=prompt,
            output_schema=output_schema,
            schema_name=planner_pass.lower(),
        )
        return ProviderCompletion(
            payload=response.payload,
            raw_response=response.raw_response,
        )


@dataclass
class FixtureTwoPassPlannerProvider(TwoPassPlannerProvider):
    pass_a: Callable[[Mapping[str, Any]], Mapping[str, Any]]
    pass_b: Callable[[Mapping[str, Any]], Mapping[str, Any]]

    provider_name = "fixture_two_pass_planner"
    real_provider = False
    fake_provider = True

    def complete(
        self,
        *,
        planner_pass: str,
        prompt: str,
        output_schema: Mapping[str, Any],
    ) -> ProviderCompletion:
        del output_schema
        payload = _prompt_payload(prompt)
        callback = (
            self.pass_a
            if planner_pass == PlannerPass.BLIND_HYPOTHESIS.value
            else self.pass_b
        )
        response = dict(callback(payload))
        return ProviderCompletion(
            payload=response,
            raw_response=_stable_json(response),
        )


def build_codex_two_pass_planner_provider(
    *,
    working_directory: str | Path | None = None,
    env_file: str | Path | None = ".env",
    load_env: bool = True,
) -> CodexTwoPassPlannerProvider:
    """Build the fixed Codex transport after loading timeout settings."""

    if load_env:
        load_project_env(env_file)
    env = os.environ
    timeout_text = (env.get("E2R_CODEX_PLANNER_TIMEOUT_SECONDS") or "300").strip()
    try:
        timeout_seconds = float(timeout_text)
    except ValueError as exc:
        raise ValueError("E2R_CODEX_PLANNER_TIMEOUT_SECONDS must be numeric") from exc
    transport = CodexStructuredProviderTransport(
        working_directory=(
            (env.get("E2R_CODEX_PLANNER_WORKDIR") or "").strip()
            or working_directory
        ),
        timeout_seconds=timeout_seconds,
        sandbox=(env.get("E2R_CODEX_PLANNER_SANDBOX") or "read-only").strip()
        or "read-only",
        approval_policy=(
            env.get("E2R_CODEX_PLANNER_APPROVAL_POLICY") or "never"
        ).strip()
        or "never",
    )
    return CodexTwoPassPlannerProvider(transport=transport)


def compile_blind_hypothesis_input(
    *,
    target_id: str,
    target_name: str,
    target_aliases: Iterable[str],
    as_of_date: str,
    evidence_rows: Iterable[Mapping[str, Any]],
    sector_context: Iterable[str] = (),
) -> BlindInputCompilationResult:
    try:
        as_of = date.fromisoformat(as_of_date)
    except ValueError as exc:
        raise ValueError("blind input as_of_date must be an ISO date") from exc
    facts: list[CurrentEvidenceFact] = []
    input_row_count = 0
    dropped_future = 0
    dropped_outcome = 0
    dropped_invalid_date = 0
    dropped_forbidden_context = 0
    stripped_assignment = 0
    for index, row in enumerate(evidence_rows):
        input_row_count += 1
        observed_date = _first_text(
            row,
            ("observed_date", "published_date", "available_date", "event_date"),
        )
        if not observed_date:
            dropped_invalid_date += 1
            continue
        try:
            observed = date.fromisoformat(observed_date)
        except ValueError:
            dropped_invalid_date += 1
            continue
        if observed > as_of:
            dropped_future += 1
            continue
        raw_text = _first_text(
            row,
            ("text", "claim_text", "event_summary", "summary", "title"),
        )
        if not raw_text:
            continue
        if _FORBIDDEN_OUTCOME_TEXT_RE.search(raw_text):
            dropped_outcome += 1
            continue
        clean_text = _FORBIDDEN_TEXT_ASSIGNMENT_RE.sub(" ", raw_text)
        clean_text = _CANONICAL_ARCHETYPE_RE.sub(" ", clean_text)
        clean_text = re.sub(r"\s+", " ", clean_text).strip(" ;")
        if clean_text != raw_text.strip():
            stripped_assignment += 1
        if not clean_text:
            continue
        if _FORBIDDEN_PLANNER_CONTEXT_TEXT_RE.search(clean_text):
            dropped_forbidden_context += 1
            continue
        facts.append(
            CurrentEvidenceFact(
                fact_id=str(row.get("fact_id") or f"FACT-{index + 1:04d}"),
                text=clean_text,
                observed_date=observed_date,
                target_relation=str(row.get("target_relation") or "UNKNOWN").upper(),
                current_status=str(row.get("current_status") or "CURRENT").upper(),
            )
        )
    normalized_aliases = tuple(
        dict.fromkeys(str(item).strip() for item in target_aliases if str(item).strip())
    )
    normalized_sector_context = tuple(
        dict.fromkeys(str(item).strip() for item in sector_context if str(item).strip())
    )
    input_id = stable_intelligence_id(
        "blind-input",
        {
            "target_id": target_id,
            "target_name": target_name,
            "target_aliases": list(normalized_aliases),
            "as_of_date": as_of_date,
            "current_facts": [fact.to_dict() for fact in facts],
            "sector_context": list(normalized_sector_context),
        },
    )
    blind_input = BlindHypothesisInput(
        input_id=input_id,
        target_id=target_id,
        target_name=target_name,
        target_aliases=normalized_aliases,
        as_of_date=as_of_date,
        current_facts=tuple(facts),
        sector_context=normalized_sector_context,
    )
    return BlindInputCompilationResult(
        blind_input=blind_input,
        audit={
            "input_row_count": input_row_count,
            "compiled_fact_count": len(facts),
            "future_evidence_dropped_count": dropped_future,
            "outcome_evidence_dropped_count": dropped_outcome,
            "invalid_date_evidence_dropped_count": dropped_invalid_date,
            "forbidden_context_evidence_dropped_count": dropped_forbidden_context,
            "forbidden_assignment_stripped_count": stripped_assignment,
            "source_primary_field_forwarded_count": 0,
            "archetype_label_field_forwarded_count": 0,
            "score_stage_field_forwarded_count": 0,
            "sector_context_forwarded_to_pass_a_count": 0,
        },
    )


def run_two_pass_planner(
    *,
    blind_input: BlindHypothesisInput,
    memory_index: SemanticMemoryIndex,
    provider: TwoPassPlannerProvider | None,
    test_mode: bool = False,
) -> TwoPassPlan:
    plan_id = stable_intelligence_id(
        "two-pass-plan",
        {"blind_input_id": blind_input.input_id},
    )
    pass_a_payload = _pass_a_prompt_payload(blind_input)
    pass_a_prompt = build_pass_a_prompt(pass_a_payload)
    pass_a_prompt_hash = _sha256(pass_a_prompt)
    if provider is None:
        return _pending_plan(
            plan_id=plan_id,
            blind_input=blind_input,
            blind_output=None,
            failed_pass=PlannerPass.BLIND_HYPOTHESIS,
            provider_name="none",
            reason_code="PLANNER_PROVIDER_NOT_CONFIGURED",
            reason_detail="No two-pass planner provider was configured.",
            prompt_hash=pass_a_prompt_hash,
            traces=(),
        )
    if provider.fake_provider and not test_mode:
        return _pending_plan(
            plan_id=plan_id,
            blind_input=blind_input,
            blind_output=None,
            failed_pass=PlannerPass.BLIND_HYPOTHESIS,
            provider_name=provider.provider_name,
            reason_code="FAKE_PROVIDER_NOT_ALLOWED",
            reason_detail="Fixture provider is test-mode only.",
            prompt_hash=pass_a_prompt_hash,
            traces=(),
        )
    pass_a_completion: ProviderCompletion | None = None
    try:
        pass_a_completion = provider.complete(
            planner_pass=PlannerPass.BLIND_HYPOTHESIS.value,
            prompt=pass_a_prompt,
            output_schema=PASS_A_OUTPUT_SCHEMA,
        )
        blind_output = decode_blind_hypothesis_output(
            pass_a_completion.payload,
            blind_input=blind_input,
        )
    except Exception as exc:  # provider/decoder failures become PlannerPending
        failed_trace = _failed_completion_trace(
            planner_pass=PlannerPass.BLIND_HYPOTHESIS,
            provider=provider,
            prompt_hash=pass_a_prompt_hash,
            completion=pass_a_completion,
        )
        return _pending_plan(
            plan_id=plan_id,
            blind_input=blind_input,
            blind_output=None,
            failed_pass=PlannerPass.BLIND_HYPOTHESIS,
            provider_name=provider.provider_name,
            reason_code=_provider_reason_code(exc),
            reason_detail=f"{type(exc).__name__}: {exc}",
            prompt_hash=pass_a_prompt_hash,
            response_hash=(
                _sha256(pass_a_completion.raw_response)
                if pass_a_completion is not None
                else None
            ),
            traces=(failed_trace,) if failed_trace is not None else (),
        )
    pass_a_trace = ProviderCallTrace(
        planner_pass=PlannerPass.BLIND_HYPOTHESIS.value,
        provider_name=provider.provider_name,
        real_provider=bool(provider.real_provider),
        fake_provider=bool(provider.fake_provider),
        prompt_hash=pass_a_prompt_hash,
        response_hash=_sha256(pass_a_completion.raw_response),
    )
    if blind_output.abstain and not blind_output.hypotheses:
        return TwoPassPlan(
            plan_id=plan_id,
            blind_input_id=blind_input.input_id,
            status=PlannerStatus.ABSTAINED.value,
            blind_output=blind_output,
            critique_output=None,
            pending=None,
            provider_traces=(pass_a_trace,),
        )

    retrieval = retrieve_balanced_memory(
        memory_index,
        BalancedRetrievalRequest(
            request_id=f"{blind_input.input_id}:memory",
            current_evidence_text="\n".join(
                fact.text for fact in blind_input.current_facts
            ),
            as_of_date=blind_input.as_of_date,
            top_k_archetypes=3,
            max_recipe_hits=3,
        ),
    )
    balanced_memory = _balanced_memory_prompt_payload(retrieval)
    critique_input = MemoryCritiqueInput(
        input_id=stable_intelligence_id(
            "memory-critique-input",
            {
                "blind_input_id": blind_input.input_id,
                "blind_hypotheses": [
                    hypothesis.to_dict() for hypothesis in blind_output.hypotheses
                ],
                "balanced_memory": balanced_memory,
                "available_recipe_ids": list(retrieval.direct_recipe_ids),
            },
        ),
        blind_input_id=blind_input.input_id,
        as_of_date=blind_input.as_of_date,
        current_facts=blind_input.current_facts,
        blind_hypotheses=blind_output.hypotheses,
        balanced_memory=balanced_memory,
        available_recipe_ids=retrieval.direct_recipe_ids,
    )
    pass_b_payload = _pass_b_prompt_payload(critique_input)
    pass_b_prompt = build_pass_b_prompt(pass_b_payload)
    pass_b_prompt_hash = _sha256(pass_b_prompt)
    pass_b_completion: ProviderCompletion | None = None
    try:
        pass_b_completion = provider.complete(
            planner_pass=PlannerPass.MEMORY_CRITIQUE.value,
            prompt=pass_b_prompt,
            output_schema=PASS_B_OUTPUT_SCHEMA,
        )
        critique_output = decode_memory_critique_output(
            pass_b_completion.payload,
            critique_input=critique_input,
            allowed_archetype_ids=tuple(
                hit.archetype_id for hit in retrieval.archetype_hits
            ),
            sector_context=blind_input.sector_context,
        )
    except Exception as exc:  # provider/decoder failures become PlannerPending
        failed_trace = _failed_completion_trace(
            planner_pass=PlannerPass.MEMORY_CRITIQUE,
            provider=provider,
            prompt_hash=pass_b_prompt_hash,
            completion=pass_b_completion,
        )
        return _pending_plan(
            plan_id=plan_id,
            blind_input=blind_input,
            blind_output=blind_output,
            failed_pass=PlannerPass.MEMORY_CRITIQUE,
            provider_name=provider.provider_name,
            reason_code=_provider_reason_code(exc),
            reason_detail=f"{type(exc).__name__}: {exc}",
            prompt_hash=pass_b_prompt_hash,
            response_hash=(
                _sha256(pass_b_completion.raw_response)
                if pass_b_completion is not None
                else None
            ),
            traces=(
                (pass_a_trace, failed_trace)
                if failed_trace is not None
                else (pass_a_trace,)
            ),
        )
    pass_b_trace = ProviderCallTrace(
        planner_pass=PlannerPass.MEMORY_CRITIQUE.value,
        provider_name=provider.provider_name,
        real_provider=bool(provider.real_provider),
        fake_provider=bool(provider.fake_provider),
        prompt_hash=pass_b_prompt_hash,
        response_hash=_sha256(pass_b_completion.raw_response),
    )
    return TwoPassPlan(
        plan_id=plan_id,
        blind_input_id=blind_input.input_id,
        status=(
            PlannerStatus.ABSTAINED.value
            if critique_output.abstain
            else PlannerStatus.COMPLETE.value
        ),
        blind_output=blind_output,
        critique_output=critique_output,
        pending=None,
        provider_traces=(pass_a_trace, pass_b_trace),
        deterministic_stage_or_score_mutation=False,
    )


def decode_blind_hypothesis_output(
    raw: Mapping[str, Any],
    *,
    blind_input: BlindHypothesisInput,
) -> BlindHypothesisOutput:
    _require_exact_keys(raw, _PASS_A_TOP_LEVEL_KEYS, context="Pass A output")
    if _required_text(raw.get("input_id"), context="Pass A input_id") != blind_input.input_id:
        raise ValueError("Pass A output input_id mismatch")
    fact_ids = {fact.fact_id for fact in blind_input.current_facts}
    hypotheses: list[BlindMechanismHypothesis] = []
    for row in _object_array(raw.get("hypotheses"), context="Pass A hypotheses"):
        if not isinstance(row, Mapping):
            raise ValueError("Pass A hypothesis must be an object")
        _require_exact_keys(row, _PASS_A_HYPOTHESIS_KEYS, context="Pass A hypothesis")
        support = _string_array(
            row.get("supporting_fact_ids"), context="Pass A supporting_fact_ids"
        )
        contradict = _string_array(
            row.get("contradicting_fact_ids"),
            context="Pass A contradicting_fact_ids",
        )
        if not set((*support, *contradict)) <= fact_ids:
            raise ValueError("Pass A output references unknown current fact")
        hypotheses.append(
            BlindMechanismHypothesis(
                hypothesis_id=_required_text(
                    row.get("hypothesis_id"), context="Pass A hypothesis_id"
                ),
                rank=_required_integer(row.get("rank"), context="Pass A rank"),
                mechanism_summary=_required_text(
                    row.get("mechanism_summary"), context="Pass A mechanism_summary"
                ),
                strength=_required_text(
                    row.get("strength"), context="Pass A strength"
                ).upper(),
                supporting_fact_ids=support,
                contradicting_fact_ids=contradict,
                must_verify_questions=_string_array(
                    row.get("must_verify_questions"),
                    context="Pass A must_verify_questions",
                ),
            )
        )
    if len(hypotheses) > 5:
        raise ValueError("Pass A returned more than five hypotheses")
    if len({item.hypothesis_id for item in hypotheses}) != len(hypotheses):
        raise ValueError("Pass A returned duplicate hypothesis IDs")
    abstention_reason = _optional_text(
        raw.get("abstention_reason"), context="Pass A abstention_reason"
    )
    return BlindHypothesisOutput(
        input_id=blind_input.input_id,
        hypotheses=tuple(hypotheses),
        ambiguity_reasons=_string_array(
            raw.get("ambiguity_reasons"), context="Pass A ambiguity_reasons"
        ),
        abstain=_required_boolean(raw.get("abstain"), context="Pass A abstain"),
        abstention_reason=abstention_reason,
    )


def decode_memory_critique_output(
    raw: Mapping[str, Any],
    *,
    critique_input: MemoryCritiqueInput,
    allowed_archetype_ids: Sequence[str],
    sector_context: Sequence[str] = (),
) -> MemoryCritiqueOutput:
    _require_exact_keys(raw, _PASS_B_TOP_LEVEL_KEYS, context="Pass B output")
    if _required_text(raw.get("input_id"), context="Pass B input_id") != critique_input.input_id:
        raise ValueError("Pass B output input_id mismatch")
    fact_ids = {fact.fact_id for fact in critique_input.current_facts}
    allowed_archetypes = set(allowed_archetype_ids)
    available_recipes = set(critique_input.available_recipe_ids)
    hypotheses: list[ArchetypeHypothesis] = []
    for row in _object_array(
        raw.get("top_k_archetypes"), context="Pass B top_k_archetypes"
    ):
        if not isinstance(row, Mapping):
            raise ValueError("Pass B archetype hypothesis must be an object")
        _require_exact_keys(row, _PASS_B_ARCHETYPE_KEYS, context="Pass B archetype")
        archetype_id = _required_text(
            row.get("archetype_id"), context="Pass B archetype_id"
        )
        if archetype_id not in CANONICAL_ARCHETYPE_IDS:
            raise ValueError(f"impossible archetype assignment: {archetype_id}")
        if archetype_id not in allowed_archetypes:
            raise ValueError(f"archetype was not retrieved from balanced memory: {archetype_id}")
        support = _string_array(
            row.get("supporting_fact_ids"), context="Pass B supporting_fact_ids"
        )
        contradict = _string_array(
            row.get("contradicting_fact_ids"),
            context="Pass B contradicting_fact_ids",
        )
        if not set((*support, *contradict)) <= fact_ids:
            raise ValueError("Pass B output references unknown current fact")
        recipe_ids = _string_array(
            row.get("recipe_ids"), context="Pass B recipe_ids"
        )
        if not set(recipe_ids) <= available_recipes:
            raise ValueError("Pass B output references unavailable recipe")
        hypotheses.append(
            ArchetypeHypothesis(
                archetype_id=archetype_id,
                rank=_required_integer(row.get("rank"), context="Pass B rank"),
                reason=_required_text(row.get("reason"), context="Pass B reason"),
                supporting_fact_ids=support,
                contradicting_fact_ids=contradict,
                recipe_ids=recipe_ids,
            )
        )
    if len(hypotheses) > 5:
        raise ValueError("Pass B returned more than five archetypes")
    if len({item.archetype_id for item in hypotheses}) != len(hypotheses):
        raise ValueError("Pass B returned duplicate archetype IDs")

    abstain = _required_boolean(raw.get("abstain"), context="Pass B abstain")
    top_recipe_ids = hypotheses[0].recipe_ids if hypotheses else ()
    if hypotheses and not top_recipe_ids and not abstain:
        raise ValueError("unsupported top archetype requires explicit abstention")
    _validate_target_plausibility(
        hypotheses,
        critique_input.current_facts,
        abstain=abstain,
    )
    _validate_sector_plausibility(hypotheses, sector_context)

    drafts: list[PlannerSourceTaskDraft] = []
    for row in _object_array(
        raw.get("source_task_drafts"), context="Pass B source_task_drafts"
    ):
        if not isinstance(row, Mapping):
            raise ValueError("Pass B source-task draft must be an object")
        _require_exact_keys(row, _PASS_B_DRAFT_KEYS, context="Pass B source-task draft")
        draft = PlannerSourceTaskDraft(
            draft_id=_required_text(row.get("draft_id"), context="Pass B draft_id"),
            recipe_id=_required_text(
                row.get("recipe_id"), context="Pass B draft recipe_id"
            ),
            question_to_answer=_required_text(
                row.get("question_to_answer"), context="Pass B question_to_answer"
            ),
            why_material=_required_text(
                row.get("why_material"), context="Pass B why_material"
            ),
            query_intent=_required_text(
                row.get("query_intent"), context="Pass B query_intent"
            ),
            preferred_source_families=_string_array(
                row.get("preferred_source_families"),
                context="Pass B preferred_source_families",
            ),
            fallback_source_families=_string_array(
                row.get("fallback_source_families"),
                context="Pass B fallback_source_families",
            ),
            max_queries=_required_integer(
                row.get("max_queries"), context="Pass B max_queries"
            ),
            max_candidates=_required_integer(
                row.get("max_candidates"), context="Pass B max_candidates"
            ),
            max_fetches=_required_integer(
                row.get("max_fetches"), context="Pass B max_fetches"
            ),
            stop_condition=_required_text(
                row.get("stop_condition"), context="Pass B stop_condition"
            ),
        )
        if draft.recipe_id not in available_recipes:
            raise ValueError("source-task draft references unavailable recipe")
        _validate_official_first_draft(draft)
        drafts.append(draft)
    if not abstain and available_recipes and not drafts:
        raise ValueError("non-abstaining Pass B output requires a bounded source-task draft")
    if len({draft.draft_id for draft in drafts}) != len(drafts):
        raise ValueError("Pass B returned duplicate source-task draft IDs")
    if (
        not abstain
        and top_recipe_ids
        and not any(draft.recipe_id in top_recipe_ids for draft in drafts)
    ):
        raise ValueError("source-task drafts do not close a leading recipe question")

    supporting = _string_array(
        raw.get("supporting_current_fact_ids"),
        context="Pass B supporting_current_fact_ids",
    )
    contradicting = _string_array(
        raw.get("contradicting_current_fact_ids"),
        context="Pass B contradicting_current_fact_ids",
    )
    if not set((*supporting, *contradicting)) <= fact_ids:
        raise ValueError("Pass B summary references unknown current fact")
    hypothesis_support = {
        fact_id for hypothesis in hypotheses for fact_id in hypothesis.supporting_fact_ids
    }
    hypothesis_contradictions = {
        fact_id
        for hypothesis in hypotheses
        for fact_id in hypothesis.contradicting_fact_ids
    }
    if not hypothesis_support <= set(supporting):
        raise ValueError("Pass B summary omits archetype supporting facts")
    if not hypothesis_contradictions <= set(contradicting):
        raise ValueError("Pass B summary omits archetype contradicting facts")
    output = MemoryCritiqueOutput(
        input_id=critique_input.input_id,
        top_k_archetypes=tuple(hypotheses),
        supporting_current_fact_ids=supporting,
        contradicting_current_fact_ids=contradicting,
        positive_thesis=_required_text(
            raw.get("positive_thesis"), context="Pass B positive_thesis"
        ),
        counter_thesis=_required_text(
            raw.get("counter_thesis"), context="Pass B counter_thesis"
        ),
        must_verify_questions=_string_array(
            raw.get("must_verify_questions"), context="Pass B must_verify_questions"
        ),
        red_team_questions=_string_array(
            raw.get("red_team_questions"), context="Pass B red_team_questions"
        ),
        source_task_drafts=tuple(drafts),
        do_not_promote_reasons=_string_array(
            raw.get("do_not_promote_reasons"),
            context="Pass B do_not_promote_reasons",
        ),
        ambiguity_reasons=_string_array(
            raw.get("ambiguity_reasons"), context="Pass B ambiguity_reasons"
        ),
        abstain=abstain,
        abstention_reason=_optional_text(
            raw.get("abstention_reason"), context="Pass B abstention_reason"
        ),
    )
    _validate_guard_posture(output, critique_input.balanced_memory)
    return output


def build_pass_a_prompt(payload: Mapping[str, Any]) -> str:
    return "\n\n".join(
        (
            "You are the blind mechanism pass of E2R Research Brain.",
            (
                "Use only the supplied current facts. Do not infer from a preassigned "
                "taxonomy, source preference, future result, or investment classification."
            ),
            (
                "Return mechanism hypotheses, supporting and contradicting fact IDs, and "
                "questions. If evidence is insufficient or mutually ambiguous, abstain explicitly."
            ),
            "Return exactly one JSON object matching the supplied schema.",
            _stable_json(payload),
        )
    )


def build_pass_b_prompt(payload: Mapping[str, Any]) -> str:
    return "\n\n".join(
        (
            "You are the balanced-memory critique pass of E2R Research Brain.",
            (
                "Critique the blind mechanisms with direct recipes, positive cases, "
                "counterexamples, wrong-subject guards, source successes, and source failures."
            ),
            (
                "Every ranked canonical option must cite at least one supplied current fact "
                "ID; memory alone is never supporting current evidence."
            ),
            (
                "Use only retrieved canonical options. Draft bounded official-first evidence "
                "questions. Never finalize an investment classification."
            ),
            (
                "For every top_k_archetypes.recipe_ids and source_task_drafts.recipe_id, copy "
                "only an exact non-empty ID from input.available_recipe_ids. Never invent, "
                "shorten, or leave a recipe ID blank. If no exact reviewed recipe is usable, "
                "set source_task_drafts to [] and abstain with an explanation."
            ),
            (
                "supporting_current_fact_ids must contain the union of every supporting_fact_ids "
                "listed under top_k_archetypes; contradicting_current_fact_ids must do the same "
                "for contradictions."
            ),
            "If the leading option has no reviewed executable recipe or remains ambiguous, abstain and explain why.",
            "Return exactly one JSON object matching the supplied schema.",
            _stable_json(payload),
        )
    )


def write_two_pass_plan(plan: TwoPassPlan, *, output_path: str | Path) -> Path:
    path = Path(output_path)
    write_json(path, plan.to_dict())
    return path


def _pass_a_prompt_payload(blind_input: BlindHypothesisInput) -> Mapping[str, Any]:
    return {
        "schema_version": TWO_PASS_PLANNER_SCHEMA_VERSION,
        "planner_pass": PlannerPass.BLIND_HYPOTHESIS.value,
        "input": {
            "input_id": blind_input.input_id,
            "target_id": blind_input.target_id,
            "target_name": blind_input.target_name,
            "target_aliases": list(blind_input.target_aliases),
            "as_of_date": blind_input.as_of_date,
            "current_facts": [fact.to_dict() for fact in blind_input.current_facts],
        },
    }


def _pass_b_prompt_payload(critique_input: MemoryCritiqueInput) -> Mapping[str, Any]:
    return {
        "schema_version": TWO_PASS_PLANNER_SCHEMA_VERSION,
        "planner_pass": PlannerPass.MEMORY_CRITIQUE.value,
        "input": critique_input.to_dict(),
    }


def _balanced_memory_prompt_payload(retrieval: Any) -> Mapping[str, Any]:
    return {
        "ranked_archetypes": [
            {
                "rank": rank,
                "archetype_id": hit.archetype_id,
                "matched_concepts": list(hit.matched_concepts),
            }
            for rank, hit in enumerate(retrieval.archetype_hits, start=1)
        ],
        "memory_items": [
            {
                "role": item.role_slot,
                "archetype_id": item.archetype_id,
                "primitive_id": item.primitive_id,
                "recipe_id": item.recipe_id,
                "content": _compact_role_content(
                    item.role_slot,
                    _sanitize_memory_content(item.planner_payload),
                ),
            }
            for item in retrieval.items
            if item.recipe_id
        ],
        "direct_recipe_ids": list(retrieval.direct_recipe_ids),
    }


def _sanitize_memory_content(value: Any) -> Any:
    if isinstance(value, Mapping):
        clean: dict[str, Any] = {}
        for key, item in value.items():
            normalized = str(key).lower()
            if normalized == "forbidden_score_sources":
                clean["disallowed_evidence_sources"] = _sanitize_memory_content(item)
                continue
            if any(fragment in normalized for fragment in _FORBIDDEN_CONTEXT_KEY_FRAGMENTS):
                continue
            clean[str(key)] = _sanitize_memory_content(item)
        return clean
    if isinstance(value, (tuple, list)):
        return [_sanitize_memory_content(item) for item in value]
    if isinstance(value, str):
        if _FORBIDDEN_OUTCOME_TEXT_RE.search(value):
            return "[EVALUATOR_ONLY_CONTENT_REMOVED]"
        value = re.sub(r"\bscore\b", "eligibility", value, flags=re.IGNORECASE)
        value = re.sub(r"\bstage\b", "classification", value, flags=re.IGNORECASE)
        return value
    return value


def _compact_role_content(role: str, value: Any) -> Any:
    if not isinstance(value, Mapping):
        return value
    keys_by_role = {
        "DIRECT_RECIPE": (
            "kind",
            "role",
            "economic_mechanism",
            "question_to_answer",
            "accepted_claim_predicates",
            "required_entities",
            "required_values",
            "required_time_scope",
            "required_target_directness",
            "required_current_lifecycle",
            "preferred_source_families",
            "preferred_document_types",
            "preferred_sections",
            "discovery_sources",
            "rejection_conditions",
            "counter_questions",
            "supersession_questions",
            "stop_conditions",
        ),
        "POSITIVE": ("kind", "recipe_role", "examples", "accepted_predicates"),
        "COUNTEREXAMPLE_GUARD": (
            "kind",
            "examples",
            "counter_questions",
            "supersession_questions",
        ),
        "SOURCE_SUCCESS": (
            "kind",
            "examples",
            "preferred_source_families",
            "preferred_document_types",
            "preferred_sections",
        ),
        "SOURCE_FAILURE": (
            "kind",
            "examples",
            "disallowed_evidence_sources",
            "source_exhaustion_conditions",
        ),
        "SEMANTIC_GUARD": (
            "kind",
            "wrong_subject_examples",
            "rejection_conditions",
            "required_target_directness",
        ),
    }
    selected = keys_by_role.get(role, tuple(value))
    return {key: value[key] for key in selected if key in value}


def _validate_official_first_draft(draft: PlannerSourceTaskDraft) -> None:
    if draft.preferred_source_families[0] not in _OFFICIAL_FIRST_FAMILIES:
        raise ValueError("source-task draft violates official-first ordering")
    if draft.max_queries > 10 or draft.max_candidates > 100 or draft.max_fetches > 20:
        raise ValueError("source-task draft exceeds bounded planning limits")


def _validate_target_plausibility(
    hypotheses: Sequence[ArchetypeHypothesis],
    facts: Sequence[CurrentEvidenceFact],
    *,
    abstain: bool,
) -> None:
    if abstain:
        return
    fact_by_id = {fact.fact_id: fact for fact in facts}
    for hypothesis in hypotheses:
        direct_current_support = any(
            fact_by_id[fact_id].target_relation in _TARGET_DIRECT_RELATIONS
            and fact_by_id[fact_id].current_status in _CURRENT_FACT_STATUSES
            for fact_id in hypothesis.supporting_fact_ids
        )
        if not direct_current_support:
            raise ValueError(
                "non-abstaining archetype requires direct current target evidence"
            )


def _validate_sector_plausibility(
    hypotheses: Sequence[ArchetypeHypothesis],
    sector_context: Sequence[str],
) -> None:
    explicit_sectors: set[str] = set()
    for item in sector_context:
        normalized = normalise_large_sector_id(item)
        looks_explicit = str(item).strip().upper().startswith("L") and "_" in str(item)
        if normalized in LARGE_SECTOR_IDS:
            explicit_sectors.add(normalized)
        elif looks_explicit:
            raise ValueError(f"unknown explicit sector context: {item}")
    if not explicit_sectors:
        return
    if hypotheses and large_sector_for_archetype(hypotheses[0].archetype_id) not in explicit_sectors:
        raise ValueError("leading archetype is incompatible with explicit sector context")


def _validate_guard_posture(
    output: MemoryCritiqueOutput,
    balanced_memory: Mapping[str, Any],
) -> None:
    if not output.top_k_archetypes:
        return
    top = output.top_k_archetypes[0]
    guard_roles = {
        str(item.get("content", {}).get("role") or "")
        for item in balanced_memory.get("memory_items", ())
        if isinstance(item, Mapping)
        and item.get("archetype_id") == top.archetype_id
        and item.get("recipe_id") in top.recipe_ids
    }
    if guard_roles & {"GUARD", "HARD_BREAK"} and not output.do_not_promote_reasons:
        raise ValueError("guard/hard-break recipe requires a do-not-promote reason")


def _failed_completion_trace(
    *,
    planner_pass: PlannerPass,
    provider: TwoPassPlannerProvider,
    prompt_hash: str,
    completion: ProviderCompletion | None,
) -> ProviderCallTrace | None:
    if completion is None:
        return None
    return ProviderCallTrace(
        planner_pass=planner_pass.value,
        provider_name=provider.provider_name,
        real_provider=bool(provider.real_provider),
        fake_provider=bool(provider.fake_provider),
        prompt_hash=prompt_hash,
        response_hash=_sha256(completion.raw_response),
    )


def _pending_plan(
    *,
    plan_id: str,
    blind_input: BlindHypothesisInput,
    blind_output: BlindHypothesisOutput | None,
    failed_pass: PlannerPass,
    provider_name: str,
    reason_code: str,
    reason_detail: str,
    prompt_hash: str,
    response_hash: str | None = None,
    traces: tuple[ProviderCallTrace, ...],
) -> TwoPassPlan:
    preserved_response_hash = response_hash or _sha256(
        _stable_json(
            {
                "response_unavailable": True,
                "reason_code": reason_code,
                "reason_detail": reason_detail,
            }
        )
    )
    pending = PlannerPending(
        input_id=blind_input.input_id,
        failed_pass=failed_pass.value,
        reason_code=reason_code,
        reason_detail=reason_detail,
        provider_name=provider_name,
        prompt_hash=prompt_hash,
        response_hash=preserved_response_hash,
    )
    return TwoPassPlan(
        plan_id=plan_id,
        blind_input_id=blind_input.input_id,
        status=PlannerStatus.PENDING.value,
        blind_output=blind_output,
        critique_output=None,
        pending=pending,
        provider_traces=traces,
        deterministic_stage_or_score_mutation=False,
    )


def _provider_reason_code(exc: Exception) -> str:
    if isinstance(exc, StructuredProviderUnavailable):
        return "PROVIDER_UNAVAILABLE"
    if isinstance(exc, StructuredProviderRejected):
        return "PROVIDER_REJECTED"
    return "PROVIDER_OR_OUTPUT_ERROR"


def _require_exact_keys(
    value: Mapping[str, Any],
    expected: frozenset[str],
    *,
    context: str,
) -> None:
    actual = {str(key) for key in value}
    if actual != expected:
        raise ValueError(
            f"{context} keys differ: missing={sorted(expected - actual)}, "
            f"unknown={sorted(actual - expected)}"
        )
    forbidden = [
        key
        for key in actual
        if any(fragment in key.lower() for fragment in _FORBIDDEN_CONTEXT_KEY_FRAGMENTS)
    ]
    if forbidden:
        raise ValueError(f"{context} contains forbidden keys: {forbidden}")


def _prompt_payload(prompt: str) -> Mapping[str, Any]:
    for block in reversed(prompt.split("\n\n")):
        try:
            payload = json.loads(block)
        except json.JSONDecodeError:
            continue
        if isinstance(payload, Mapping):
            return payload
    raise ValueError("fixture provider could not read prompt payload")


def _first_text(row: Mapping[str, Any], keys: Sequence[str]) -> str:
    for key in keys:
        value = str(row.get(key) or "").strip()
        if value:
            return value
    return ""


def _object_array(value: Any, *, context: str) -> tuple[Mapping[str, Any], ...]:
    if not isinstance(value, (list, tuple)) or isinstance(value, (str, bytes)):
        raise ValueError(f"{context} must be an array")
    if any(not isinstance(item, Mapping) for item in value):
        raise ValueError(f"{context} items must be objects")
    return tuple(value)


def _string_array(value: Any, *, context: str) -> tuple[str, ...]:
    if not isinstance(value, (list, tuple)) or isinstance(value, (str, bytes)):
        raise ValueError(f"{context} must be an array")
    if any(not isinstance(item, str) for item in value):
        raise ValueError(f"{context} items must be strings")
    clean = tuple(item.strip() for item in value)
    if any(not item for item in clean):
        raise ValueError(f"{context} cannot contain empty strings")
    if len(set(clean)) != len(clean):
        raise ValueError(f"{context} cannot contain duplicates")
    return clean


def _required_text(value: Any, *, context: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{context} must be a non-empty string")
    return value.strip()


def _optional_text(value: Any, *, context: str) -> str | None:
    if not isinstance(value, str):
        raise ValueError(f"{context} must be a string")
    return value.strip() or None


def _required_boolean(value: Any, *, context: str) -> bool:
    if not isinstance(value, bool):
        raise ValueError(f"{context} must be a boolean")
    return value


def _required_integer(value: Any, *, context: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{context} must be an integer")
    return value


def _stable_json(value: Mapping[str, Any]) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _sha256(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


__all__ = [
    "PASS_A_OUTPUT_SCHEMA",
    "PASS_B_OUTPUT_SCHEMA",
    "TWO_PASS_PLANNER_SCHEMA_VERSION",
    "BlindInputCompilationResult",
    "CodexTwoPassPlannerProvider",
    "FixtureTwoPassPlannerProvider",
    "ProviderCompletion",
    "TwoPassPlannerProvider",
    "build_pass_a_prompt",
    "build_pass_b_prompt",
    "build_codex_two_pass_planner_provider",
    "compile_blind_hypothesis_input",
    "decode_blind_hypothesis_output",
    "decode_memory_critique_output",
    "run_two_pass_planner",
    "write_two_pass_plan",
]
