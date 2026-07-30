"""Independent analyst/skeptic judgments and non-scoring synthesis review."""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import math
from typing import Any, Mapping, Sequence

from e2r.research_brain.intelligence_schema import stable_intelligence_id
from e2r.research_brain.planning.provider_transport import (
    StructuredProviderRejected,
    StructuredProviderUnavailable,
)

from .component_researcher import StructuredResearchProvider
from .prompt_projection import project_citable_evidence_facts
from .schemas import (
    CANONICAL_COMPONENT_ORDER,
    ComponentAnchor,
    ComponentJudgeDecision,
    ComponentJudgeRole,
    ComponentResearchMemo,
    EvidenceDirection,
    EvidenceFact,
    EvidenceLifecycle,
    RedTeamMemo,
    SynthesisMemo,
    assert_blind_research_output,
    scrub_blind_research_payload,
)


JUDGE_PASS_BY_ROLE: Mapping[str, str] = {
    ComponentJudgeRole.ANALYST.value: "COMPONENT_ANALYST_JUDGE",
    ComponentJudgeRole.SKEPTIC.value: "COMPONENT_SKEPTIC_JUDGE",
    ComponentJudgeRole.CALIBRATION_JUDGE.value: "CALIBRATION_JUDGE",
}

JUDGE_REVIEW_DIMENSIONS_BY_ROLE: Mapping[str, tuple[str, ...]] = {
    ComponentJudgeRole.ANALYST.value: (
        "CURRENT_ECONOMIC_STRENGTH",
        "POSITIVE_THESIS",
        "DURATION_AND_CASH_CONVERSION",
    ),
    ComponentJudgeRole.SKEPTIC.value: (
        "COUNTEREVIDENCE",
        "BUSINESS_PHASE",
        "VALUATION",
        "CONCENTRATION",
        "UNCERTAINTY",
    ),
    ComponentJudgeRole.CALIBRATION_JUDGE.value: (
        "HISTORICAL_ANCHOR_COMPARABILITY",
        "COMPONENT_SCORE_SCALE",
        "ALLOWED_RANGE_DISCIPLINE",
    ),
}

JUDGE_RESPONSE_FIELDS = frozenset(
    {
        "anchor_comparisons",
        "proposed_points",
        "allowed_range",
        "rationale",
        "disagreements",
        "support_fact_ids",
        "counter_fact_ids",
        "nearest_anchor_ids",
        "why_not_higher",
        "why_not_lower",
    }
)

JUDGE_CONDITIONAL_SCORING_RULES: Mapping[str, Any] = {
    "positive_points_require_support": (
        "proposed_points greater than zero requires at least one exact id from "
        "allowed_support_fact_ids in support_fact_ids"
    ),
    "empty_support_plane": {
        "condition": "allowed_support_fact_ids is empty",
        "required_proposed_points": 0,
        "required_allowed_range": [0, 0],
        "required_support_fact_ids": [],
    },
}


@dataclass(frozen=True)
class ComponentJudgeResult:
    component_id: str
    memo_id: str
    role: str
    pass_name: str
    status: str
    decision: ComponentJudgeDecision | None
    pending_reasons: tuple[str, ...]
    provider_name: str
    prompt_hash: str | None
    response_hash: str | None
    judge_call_id: str | None
    production_total_score_authority: bool = False
    production_stage_authority: bool = False
    schema_version: str = "e2r_component_judge_result_v2"

    def __post_init__(self) -> None:
        if self.component_id not in CANONICAL_COMPONENT_ORDER:
            raise ValueError("unknown component judge component")
        if self.role not in JUDGE_PASS_BY_ROLE:
            raise ValueError("unknown component judge role")
        if self.pass_name != JUDGE_PASS_BY_ROLE[self.role]:
            raise ValueError("component judge role/pass mismatch")
        if not self.memo_id.strip() or not self.provider_name.strip():
            raise ValueError("component judge result identity is incomplete")
        if self.status not in {"COMPLETE", "PENDING"}:
            raise ValueError("unknown component judge status")
        if self.status == "COMPLETE":
            if (
                self.decision is None
                or not self.prompt_hash
                or not self.response_hash
                or not self.judge_call_id
            ):
                raise ValueError("complete judge result requires decision lineage")
            if (
                self.decision.component_id != self.component_id
                or self.decision.memo_id != self.memo_id
                or self.decision.role != self.role
                or self.decision.pass_name != self.pass_name
                or self.decision.prompt_hash != self.prompt_hash
                or self.decision.response_hash != self.response_hash
                or self.decision.judge_call_id != self.judge_call_id
            ):
                raise ValueError("judge result and decision lineage disagree")
            if self.pending_reasons:
                raise ValueError("complete judge result cannot have pending reasons")
        if self.status == "PENDING" and not self.pending_reasons:
            raise ValueError("pending judge result requires reasons")
        if self.status == "PENDING" and self.decision is not None:
            raise ValueError("pending judge result cannot carry a decision")
        if self.production_total_score_authority or self.production_stage_authority:
            raise ValueError("component judge result cannot decide total score or Stage")

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "schema_version": self.schema_version,
            "component_id": self.component_id,
            "memo_id": self.memo_id,
            "role": self.role,
            "pass_name": self.pass_name,
            "status": self.status,
            "decision": self.decision.to_dict() if self.decision else None,
            "pending_reasons": list(self.pending_reasons),
            "provider_name": self.provider_name,
            "prompt_hash": self.prompt_hash,
            "response_hash": self.response_hash,
            "judge_call_id": self.judge_call_id,
            "production_total_score_authority": False,
            "production_stage_authority": False,
        }


@dataclass(frozen=True)
class SynthesisResult:
    status: str
    memo: SynthesisMemo | None
    pending_reasons: tuple[str, ...]
    provider_name: str

    def __post_init__(self) -> None:
        if self.status not in {"COMPLETE", "PENDING"}:
            raise ValueError("unknown synthesis status")
        if self.status == "COMPLETE" and (
            self.memo is None or not self.memo.synthesis_complete
        ):
            raise ValueError("complete synthesis result requires a complete memo")
        if self.status == "PENDING" and not self.pending_reasons:
            raise ValueError("pending synthesis result requires reasons")

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "status": self.status,
            "memo": self.memo.to_dict() if self.memo else None,
            "pending_reasons": list(self.pending_reasons),
            "provider_name": self.provider_name,
        }


class ComponentJudge:
    """One blind component judge; it cannot output total points or Stage."""

    def __init__(
        self,
        *,
        provider: StructuredResearchProvider,
        role: str = ComponentJudgeRole.ANALYST.value,
    ) -> None:
        if role not in {value.value for value in ComponentJudgeRole}:
            raise ValueError("unknown component judge role")
        self.provider = provider
        self.role = role

    def judge(
        self,
        *,
        memo: ComponentResearchMemo,
        evidence_facts: Sequence[EvidenceFact],
        historical_anchors: Sequence[ComponentAnchor | Mapping[str, Any]],
    ) -> ComponentJudgeResult:
        pass_name = JUDGE_PASS_BY_ROLE[self.role]
        if not memo.research_complete:
            return self._pending(
                memo=memo,
                pass_name=pass_name,
                code="COMPONENT_RESEARCH_INCOMPLETE",
            )
        try:
            facts = _validated_fact_map(memo, evidence_facts)
            anchors = _validated_anchor_map(memo, historical_anchors)
        except (KeyError, TypeError, ValueError) as exc:
            return self._pending(
                memo=memo,
                pass_name=pass_name,
                code="INVALID_JUDGE_INPUT_LINEAGE",
                error=exc,
            )
        selected_fact_rows = tuple(
            facts[fact_id].to_dict()
            for fact_id in (
                *memo.positive_fact_ids,
                *memo.counter_fact_ids,
                *memo.resolution_fact_ids,
            )
            if fact_id in facts
        )
        payload = scrub_blind_research_payload(
            {
                "judge_role": self.role,
                "judge_pass_name": pass_name,
                "independent_role_mandate": list(
                    JUDGE_REVIEW_DIMENSIONS_BY_ROLE[self.role]
                ),
                "component_id": memo.component_id,
                "component_max_points": memo.component_max_points,
                "component_research_memo": _scoring_blind_memo(memo),
                "evidence_fact_projection": project_citable_evidence_facts(
                    selected_fact_rows
                ),
                "historical_component_anchors": [
                    anchors[anchor_id]
                    for anchor_id in memo.historical_anchor_ids
                    if anchor_id in anchors
                ],
                "allowed_support_fact_ids": list(memo.positive_fact_ids),
                "allowed_counter_fact_ids": list(memo.counter_fact_ids),
                "allowed_nearest_anchor_ids": list(memo.historical_anchor_ids),
                "conditional_judge_rules": JUDGE_CONDITIONAL_SCORING_RULES,
                "required_judge_output_fields": sorted(JUDGE_RESPONSE_FIELDS),
            }
        )
        attempt_payload = payload
        validation_retry_used = False
        while True:
            fallback_prompt_hash = _canonical_hash(
                {"pass_name": pass_name, "payload": attempt_payload}
            )
            try:
                response = self.provider.complete(
                    pass_name=pass_name,
                    payload=attempt_payload,
                )
            except (
                StructuredProviderUnavailable,
                StructuredProviderRejected,
                TimeoutError,
                OSError,
                RuntimeError,
            ) as exc:
                prompt_hash = _provider_prompt_hash(
                    self.provider,
                    pass_name=pass_name,
                    fallback=fallback_prompt_hash,
                )
                return self._pending(
                    memo=memo,
                    pass_name=pass_name,
                    code="PROVIDER_ERROR",
                    error=exc,
                    prompt_hash=prompt_hash,
                    judge_call_id=_judge_call_id(
                        memo=memo,
                        role=self.role,
                        pass_name=pass_name,
                        provider_name=self._provider_name,
                        prompt_hash=prompt_hash,
                    ),
                )
            prompt_hash = _provider_prompt_hash(
                self.provider,
                pass_name=pass_name,
                fallback=fallback_prompt_hash,
            )
            response_hash = _canonical_hash(response)
            judge_call_id = _judge_call_id(
                memo=memo,
                role=self.role,
                pass_name=pass_name,
                provider_name=self._provider_name,
                prompt_hash=prompt_hash,
            )
            try:
                decision = _decision_from_response(
                    response=response,
                    memo=memo,
                    role=self.role,
                    pass_name=pass_name,
                    facts=facts,
                    anchors=anchors,
                    provider_name=self._provider_name,
                    prompt_hash=prompt_hash,
                    response_hash=response_hash,
                    judge_call_id=judge_call_id,
                )
            except (KeyError, TypeError, ValueError) as exc:
                _invalidate_provider_response_cache(self.provider, exc)
                if validation_retry_used:
                    return self._pending(
                        memo=memo,
                        pass_name=pass_name,
                        code="INVALID_PROVIDER_OUTPUT",
                        error=exc,
                        prompt_hash=prompt_hash,
                        response_hash=response_hash,
                        judge_call_id=judge_call_id,
                    )
                validation_retry_used = True
                attempt_payload = scrub_blind_research_payload(
                    {
                        **payload,
                        "judge_validation_retry_context": {
                            "validation_error": _clean_error(exc),
                            "rejected_response": response,
                            "allowed_support_fact_ids": list(
                                memo.positive_fact_ids
                            ),
                            "allowed_counter_fact_ids": list(
                                memo.counter_fact_ids
                            ),
                            "allowed_nearest_anchor_ids": list(
                                memo.historical_anchor_ids
                            ),
                            "required_output_fields": sorted(
                                JUDGE_RESPONSE_FIELDS
                            ),
                            "positive_score_constraint": (
                                JUDGE_CONDITIONAL_SCORING_RULES
                            ),
                            "instruction": (
                                "Rewrite the complete judge response. Cite only "
                                "the exact supplied allowed fact and anchor ids; "
                                "do not invent, coerce, drop, or deterministically "
                                "repair citations. The analyst must account for "
                                "every allowed support fact, the skeptic must "
                                "account for every allowed counter fact, and every "
                                "judge must compare at least one usable allowed "
                                "nearest anchor. When allowed_support_fact_ids is "
                                "empty, return proposed_points=0, "
                                "allowed_range=[0,0], and support_fact_ids=[]; "
                                "never award positive points from structured "
                                "metrics or prose without an allowed support fact. "
                                "Return only the closed schema."
                            ),
                        },
                    }
                )
                continue
            break
        return ComponentJudgeResult(
            component_id=memo.component_id,
            memo_id=memo.memo_id,
            role=self.role,
            pass_name=pass_name,
            status="COMPLETE",
            decision=decision,
            pending_reasons=(),
            provider_name=self._provider_name,
            prompt_hash=prompt_hash,
            response_hash=response_hash,
            judge_call_id=judge_call_id,
        )

    @property
    def _provider_name(self) -> str:
        return str(
            getattr(self.provider, "provider_name", self.provider.__class__.__name__)
        )

    def _pending(
        self,
        *,
        memo: ComponentResearchMemo,
        pass_name: str,
        code: str,
        error: Exception | None = None,
        prompt_hash: str | None = None,
        response_hash: str | None = None,
        judge_call_id: str | None = None,
    ) -> ComponentJudgeResult:
        detail = ""
        if error is not None:
            detail = ":" + (
                " ".join(str(error).split())[-500:] or error.__class__.__name__
            )
        return ComponentJudgeResult(
            component_id=memo.component_id,
            memo_id=memo.memo_id,
            role=self.role,
            pass_name=pass_name,
            status="PENDING",
            decision=None,
            pending_reasons=(code + detail,),
            provider_name=self._provider_name,
            prompt_hash=prompt_hash,
            response_hash=response_hash,
            judge_call_id=judge_call_id,
        )


class AnalystJudge(ComponentJudge):
    def __init__(self, *, provider: StructuredResearchProvider) -> None:
        super().__init__(provider=provider, role=ComponentJudgeRole.ANALYST.value)


class SkepticJudge(ComponentJudge):
    def __init__(self, *, provider: StructuredResearchProvider) -> None:
        super().__init__(provider=provider, role=ComponentJudgeRole.SKEPTIC.value)


class SynthesisJudge:
    researcher_role = "SynthesisJudge"

    def __init__(self, *, provider: StructuredResearchProvider) -> None:
        self.provider = provider

    def synthesize(
        self,
        *,
        target_id: str,
        archetype_id: str,
        component_memos: Sequence[ComponentResearchMemo],
        red_team_memo: RedTeamMemo,
    ) -> SynthesisResult:
        memo_ids = {row.memo_id for row in component_memos}
        if len(memo_ids) != len(component_memos):
            raise ValueError("component memo ids must be unique")
        payload = scrub_blind_research_payload(
            {
                "researcher_role": self.researcher_role,
                "target_id": target_id,
                "archetype_id": archetype_id,
                "component_research_memos": [row.to_dict() for row in component_memos],
                "red_team_memo": red_team_memo.to_dict(),
            }
        )
        try:
            response = self.provider.complete(
                pass_name="SYNTHESIS_REVIEW", payload=payload
            )
        except (
            StructuredProviderUnavailable,
            StructuredProviderRejected,
            TimeoutError,
            OSError,
            RuntimeError,
        ) as exc:
            return self._pending("PROVIDER_ERROR", exc)
        try:
            assert_blind_research_output(response)
            cited_memos = _strings(response, "component_memo_ids")
            if set(cited_memos) != memo_ids:
                raise ValueError("synthesis must account for every component memo")
            memo = SynthesisMemo(
                memo_id=stable_intelligence_id(
                    "SYNMEMO",
                    {
                        "target_id": target_id,
                        "archetype_id": archetype_id,
                        "red_team_memo_id": red_team_memo.memo_id,
                        "response": scrub_blind_research_payload(response),
                    },
                ),
                target_id=target_id,
                archetype_id=archetype_id,
                component_memo_ids=cited_memos,
                cross_component_support=_strings(
                    response, "cross_component_support"
                ),
                cross_component_tensions=_strings(
                    response, "cross_component_tensions"
                ),
                unresolved_material_questions=_strings(
                    response, "unresolved_material_questions"
                ),
                synthesis_summary=str(response["synthesis_summary"]),
                confidence=float(response["confidence"]),
                synthesis_complete=bool(response["synthesis_complete"]),
            )
        except (KeyError, TypeError, ValueError) as exc:
            return self._pending("INVALID_PROVIDER_OUTPUT", exc)
        if not memo.synthesis_complete:
            return SynthesisResult(
                status="PENDING",
                memo=memo,
                pending_reasons=("SYNTHESIS_DECLARED_INCOMPLETE",),
                provider_name=self._provider_name,
            )
        return SynthesisResult(
            status="COMPLETE",
            memo=memo,
            pending_reasons=(),
            provider_name=self._provider_name,
        )

    @property
    def _provider_name(self) -> str:
        return str(
            getattr(self.provider, "provider_name", self.provider.__class__.__name__)
        )

    def _pending(self, code: str, error: Exception) -> SynthesisResult:
        detail = " ".join(str(error).split())[-500:] or error.__class__.__name__
        return SynthesisResult(
            status="PENDING",
            memo=None,
            pending_reasons=(f"{code}:{detail}",),
            provider_name=self._provider_name,
        )


def _decision_from_response(
    *,
    response: Mapping[str, Any],
    memo: ComponentResearchMemo,
    role: str,
    pass_name: str,
    facts: Mapping[str, EvidenceFact],
    anchors: Mapping[str, Mapping[str, Any]],
    provider_name: str,
    prompt_hash: str,
    response_hash: str,
    judge_call_id: str,
) -> ComponentJudgeDecision:
    if not isinstance(response, Mapping):
        raise TypeError("component judge response must be an object")
    assert_blind_research_output(response)
    if set(response) != JUDGE_RESPONSE_FIELDS:
        raise ValueError("component judge response keys do not match the closed schema")
    support_ids = _strings(response, "support_fact_ids")
    counter_ids = _strings(response, "counter_fact_ids")
    nearest_ids = _strings(response, "nearest_anchor_ids")
    anchor_comparisons = _strings(response, "anchor_comparisons")
    if set(support_ids) - set(memo.positive_fact_ids):
        raise ValueError("judge support facts are outside the component memo")
    if set(counter_ids) - set(memo.counter_fact_ids):
        raise ValueError("judge counter facts are outside the component memo")
    if set(nearest_ids) - set(memo.historical_anchor_ids):
        raise ValueError("judge anchors are outside the component memo")
    if set((*support_ids, *counter_ids)) - set(facts):
        raise ValueError("judge cited unknown facts")
    if set(nearest_ids) - set(anchors):
        raise ValueError("judge cited unknown anchors")
    if any(
        not (
            anchors[anchor_id].get("usable_as_exact_anchor")
            or anchors[anchor_id].get("usable_as_ordinal_anchor")
        )
        for anchor_id in nearest_ids
    ):
        raise ValueError("judge cited an unusable nearest anchor")
    if not nearest_ids or not anchor_comparisons:
        raise ValueError("every judge must compare at least one nearest anchor")
    if role == ComponentJudgeRole.ANALYST.value and set(
        memo.positive_fact_ids
    ) - set(support_ids):
        raise ValueError("analyst did not account for every positive component fact")
    if role == ComponentJudgeRole.SKEPTIC.value and set(
        memo.counter_fact_ids
    ) - set(counter_ids):
        raise ValueError("skeptic did not account for every component counterfact")
    allowed = response["allowed_range"]
    if isinstance(allowed, str) or not isinstance(allowed, Sequence) or len(allowed) != 2:
        raise TypeError("allowed_range must contain two numbers")
    if any(
        isinstance(value, bool) or not isinstance(value, (int, float))
        for value in allowed
    ):
        raise TypeError("allowed_range values must be numeric")
    proposed_value = response["proposed_points"]
    if isinstance(proposed_value, bool) or not isinstance(
        proposed_value, (int, float)
    ):
        raise TypeError("proposed_points must be numeric")
    lower, upper = (float(value) for value in allowed)
    proposed = float(proposed_value)
    if not all(math.isfinite(value) for value in (lower, proposed, upper)):
        raise ValueError("judge point values must be finite")
    if not 0 <= lower <= proposed <= upper <= memo.component_max_points:
        raise ValueError("judge range exceeds the component maximum")
    return ComponentJudgeDecision(
        judge_id=stable_intelligence_id(
            "CJUDGE",
            {
                "memo_id": memo.memo_id,
                "role": role,
                "pass_name": pass_name,
                "provider_name": provider_name,
                "prompt_hash": prompt_hash,
                "response_hash": response_hash,
                "judge_call_id": judge_call_id,
                "response": scrub_blind_research_payload(response),
            },
        ),
        judge_call_id=judge_call_id,
        memo_id=memo.memo_id,
        component_id=memo.component_id,
        component_max_points=memo.component_max_points,
        role=role,
        pass_name=pass_name,
        prompt_hash=prompt_hash,
        response_hash=response_hash,
        provider_name=provider_name,
        anchor_comparisons=anchor_comparisons,
        proposed_points=proposed,
        allowed_range=(lower, upper),
        rationale=_required_text(response, "rationale"),
        disagreements=_strings(response, "disagreements"),
        support_fact_ids=support_ids,
        counter_fact_ids=counter_ids,
        nearest_anchor_ids=nearest_ids,
        why_not_higher=_required_text(response, "why_not_higher"),
        why_not_lower=_required_text(response, "why_not_lower"),
    )


def _validated_fact_map(
    memo: ComponentResearchMemo,
    evidence_facts: Sequence[EvidenceFact],
) -> Mapping[str, EvidenceFact]:
    ids = [row.fact_id for row in evidence_facts]
    if len(ids) != len(set(ids)):
        raise ValueError("component judge EvidenceFact ids must be unique")
    facts = {row.fact_id: row for row in evidence_facts}
    referenced = {
        *memo.positive_fact_ids,
        *memo.counter_fact_ids,
        *memo.resolution_fact_ids,
    }
    if referenced - set(facts):
        raise ValueError("component memo references an unavailable EvidenceFact")
    if any(facts[fact_id].target_id != memo.target_id for fact_id in referenced):
        raise ValueError("component judge fact target mismatch")
    if len({facts[fact_id].as_of_date for fact_id in referenced}) > 1:
        raise ValueError("component judge facts cross as_of_date snapshots")
    for fact_id in memo.positive_fact_ids:
        fact = facts[fact_id]
        if (
            fact.direction != EvidenceDirection.POSITIVE.value
            or fact.current_lifecycle
            in {EvidenceLifecycle.RESOLVED.value, EvidenceLifecycle.SUPERSEDED.value}
        ):
            raise ValueError("positive component fact has invalid direction/lifecycle")
    for fact_id in memo.counter_fact_ids:
        fact = facts[fact_id]
        if (
            fact.direction != EvidenceDirection.COUNTER.value
            or fact.current_lifecycle
            in {EvidenceLifecycle.RESOLVED.value, EvidenceLifecycle.SUPERSEDED.value}
        ):
            raise ValueError("component counterfact has invalid direction/lifecycle")
    for fact_id in memo.resolution_fact_ids:
        fact = facts[fact_id]
        if (
            fact.direction != EvidenceDirection.RESOLUTION.value
            and fact.current_lifecycle != EvidenceLifecycle.RESOLVED.value
        ):
            raise ValueError("component resolution fact has invalid direction/lifecycle")
    return facts


def _validated_anchor_map(
    memo: ComponentResearchMemo,
    historical_anchors: Sequence[ComponentAnchor | Mapping[str, Any]],
) -> Mapping[str, Mapping[str, Any]]:
    selected = [
        _blind_anchor(row)
        for row in historical_anchors
        if _field(row, "archetype_id") == memo.archetype_id
        and _field(row, "component_id") == memo.component_id
    ]
    ids = [str(row.get("anchor_id") or "").strip() for row in selected]
    if any(not value for value in ids) or len(ids) != len(set(ids)):
        raise ValueError("component judge anchor ids must be unique and nonempty")
    anchors = dict(zip(ids, selected))
    if set(memo.historical_anchor_ids) - set(anchors):
        raise ValueError("component memo references an unavailable historical anchor")
    cited = [anchors[value] for value in memo.historical_anchor_ids]
    for row in cited:
        _validate_blind_anchor(row)
    if not cited or not any(
        row.get("usable_as_exact_anchor") or row.get("usable_as_ordinal_anchor")
        for row in cited
    ):
        raise ValueError("component scoring requires a usable historical anchor")
    if any(
        abs(float(row.get("max_points")) - memo.component_max_points) > 1e-9
        for row in cited
    ):
        raise ValueError("historical anchor and component point scales differ")
    return anchors


def _validate_blind_anchor(row: Mapping[str, Any]) -> None:
    values = tuple(
        row.get(key)
        for key in (
            "points_lower",
            "points_mid",
            "points_upper",
            "max_points",
        )
    )
    if any(
        isinstance(value, bool) or not isinstance(value, (int, float))
        for value in values
    ):
        raise TypeError("historical anchor point band must be numeric")
    lower, mid, upper, maximum = (float(value) for value in values)
    if not all(math.isfinite(value) for value in (lower, mid, upper, maximum)):
        raise ValueError("historical anchor point band must be finite")
    if not 0 <= lower <= mid <= upper <= maximum:
        raise ValueError("historical anchor point band is invalid")
    if type(row.get("usable_as_exact_anchor")) is not bool or type(
        row.get("usable_as_ordinal_anchor")
    ) is not bool:
        raise TypeError("historical anchor usability flags must be boolean")


def _scoring_blind_memo(memo: ComponentResearchMemo) -> Mapping[str, Any]:
    value = memo.to_dict()
    allowed = {
        "memo_id",
        "target_id",
        "archetype_id",
        "component_id",
        "component_max_points",
        "positive_fact_ids",
        "counter_fact_ids",
        "resolution_fact_ids",
        "structured_metrics",
        "historical_anchor_ids",
        "researcher_summary",
        "positive_case",
        "counter_case",
        "uncertainties",
        "source_coverage",
        "nearest_positive_anchor_ids",
        "nearest_counter_anchor_ids",
        "researcher_role",
        "research_complete",
    }
    return {key: value[key] for key in allowed if key in value}


def _provider_prompt_hash(
    provider: StructuredResearchProvider,
    *,
    pass_name: str,
    fallback: str,
) -> str:
    calls = getattr(provider, "calls", None)
    if isinstance(calls, list):
        for call in reversed(calls):
            if call.get("pass_name") == pass_name and call.get("prompt_hash"):
                return str(call["prompt_hash"])
    return fallback


def _invalidate_provider_response_cache(
    provider: StructuredResearchProvider,
    error: Exception,
) -> None:
    """Evict a semantically invalid response before one bounded LLM rewrite."""

    invalidate = getattr(provider, "invalidate_last_response_cache", None)
    if not callable(invalidate):
        return
    reason = f"{error.__class__.__name__}:{_clean_error(error)}"
    try:
        invalidate(reason=reason)
    except (OSError, TypeError, ValueError, RuntimeError):
        # Cache audit failure cannot make a rejected response valid or suppress
        # the bounded correction attempt.
        return


def _clean_error(error: Exception) -> str:
    return " ".join(str(error).split())[-500:] or error.__class__.__name__


def _judge_call_id(
    *,
    memo: ComponentResearchMemo,
    role: str,
    pass_name: str,
    provider_name: str,
    prompt_hash: str,
) -> str:
    return stable_intelligence_id(
        "JUDGECALL",
        {
            "memo_id": memo.memo_id,
            "component_id": memo.component_id,
            "role": role,
            "pass_name": pass_name,
            "provider_name": provider_name,
            "prompt_hash": prompt_hash,
        },
    )


def _canonical_hash(value: Any) -> str:
    encoded = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        default=str,
    )
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def _required_text(response: Mapping[str, Any], key: str) -> str:
    value = response[key]
    if not isinstance(value, str) or not value.strip():
        raise TypeError(f"{key} must be a nonempty string")
    return value.strip()


def _blind_anchor(row: ComponentAnchor | Mapping[str, Any]) -> Mapping[str, Any]:
    value = row.to_dict() if isinstance(row, ComponentAnchor) else dict(row)
    if value.get("company_name_conditioned") or value.get("target_symbol_conditioned"):
        raise ValueError("target-conditioned historical anchors are forbidden")
    allowed = {
        "anchor_id",
        "archetype_id",
        "component_id",
        "economic_fact_patterns",
        "role",
        "score_band",
        "points_lower",
        "points_mid",
        "points_upper",
        "max_points",
        "confidence",
        "usable_as_exact_anchor",
        "usable_as_ordinal_anchor",
    }
    return {key: value[key] for key in allowed if key in value}


def _field(row: Any, key: str) -> Any:
    return row.get(key) if isinstance(row, Mapping) else getattr(row, key)


def _strings(response: Mapping[str, Any], key: str) -> tuple[str, ...]:
    value = response[key]
    if isinstance(value, str) or not isinstance(value, Sequence):
        raise TypeError(f"{key} must be an array")
    if any(not isinstance(item, str) for item in value):
        raise TypeError(f"{key} must contain strings")
    result = tuple(item.strip() for item in value)
    if any(not item for item in result) or len(result) != len(set(result)):
        raise ValueError(f"{key} must contain unique nonempty strings")
    return result


__all__ = [
    "AnalystJudge",
    "ComponentJudge",
    "ComponentJudgeResult",
    "JUDGE_PASS_BY_ROLE",
    "JUDGE_RESPONSE_FIELDS",
    "JUDGE_REVIEW_DIMENSIONS_BY_ROLE",
    "SkepticJudge",
    "SynthesisJudge",
    "SynthesisResult",
]
