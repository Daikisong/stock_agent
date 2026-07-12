"""Independent analyst/skeptic judgments and non-scoring synthesis review."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, Sequence

from e2r.research_brain.intelligence_schema import stable_intelligence_id
from e2r.research_brain.planning.provider_transport import (
    StructuredProviderRejected,
    StructuredProviderUnavailable,
)

from .component_researcher import StructuredResearchProvider
from .schemas import (
    ComponentAnchor,
    ComponentJudgeDecision,
    ComponentJudgeRole,
    ComponentResearchMemo,
    EvidenceFact,
    RedTeamMemo,
    SynthesisMemo,
    assert_blind_research_output,
    scrub_blind_research_payload,
)


@dataclass(frozen=True)
class ComponentJudgeResult:
    status: str
    decision: ComponentJudgeDecision | None
    pending_reasons: tuple[str, ...]
    provider_name: str

    def __post_init__(self) -> None:
        if self.status not in {"COMPLETE", "PENDING"}:
            raise ValueError("unknown component judge status")
        if self.status == "COMPLETE" and self.decision is None:
            raise ValueError("complete judge result requires a decision")
        if self.status == "PENDING" and not self.pending_reasons:
            raise ValueError("pending judge result requires reasons")

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "status": self.status,
            "decision": self.decision.to_dict() if self.decision else None,
            "pending_reasons": list(self.pending_reasons),
            "provider_name": self.provider_name,
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
        if not memo.research_complete:
            return self._pending("COMPONENT_RESEARCH_INCOMPLETE")
        facts = {row.fact_id: row for row in evidence_facts}
        anchors = {
            str(_field(row, "anchor_id")): _blind_anchor(row)
            for row in historical_anchors
            if _field(row, "archetype_id") == memo.archetype_id
            and _field(row, "component_id") == memo.component_id
        }
        pass_name = {
            ComponentJudgeRole.ANALYST.value: "COMPONENT_ANALYST_JUDGE",
            ComponentJudgeRole.SKEPTIC.value: "COMPONENT_SKEPTIC_JUDGE",
            ComponentJudgeRole.CALIBRATION_JUDGE.value: "CALIBRATION_JUDGE",
        }[self.role]
        payload = scrub_blind_research_payload(
            {
                "judge_role": self.role,
                "component_id": memo.component_id,
                "component_max_points": memo.component_max_points,
                "component_research_memo": memo.to_dict(),
                "evidence_facts": [
                    facts[fact_id].to_dict()
                    for fact_id in (
                        *memo.positive_fact_ids,
                        *memo.counter_fact_ids,
                        *memo.resolution_fact_ids,
                    )
                    if fact_id in facts
                ],
                "historical_component_anchors": [
                    anchors[anchor_id]
                    for anchor_id in memo.historical_anchor_ids
                    if anchor_id in anchors
                ],
            }
        )
        try:
            response = self.provider.complete(pass_name=pass_name, payload=payload)
        except (
            StructuredProviderUnavailable,
            StructuredProviderRejected,
            TimeoutError,
            OSError,
            RuntimeError,
        ) as exc:
            return self._pending("PROVIDER_ERROR", exc)
        try:
            decision = _decision_from_response(
                response=response,
                memo=memo,
                role=self.role,
                facts=facts,
                anchors=anchors,
            )
        except (KeyError, TypeError, ValueError) as exc:
            return self._pending("INVALID_PROVIDER_OUTPUT", exc)
        return ComponentJudgeResult(
            status="COMPLETE",
            decision=decision,
            pending_reasons=(),
            provider_name=self._provider_name,
        )

    @property
    def _provider_name(self) -> str:
        return str(
            getattr(self.provider, "provider_name", self.provider.__class__.__name__)
        )

    def _pending(
        self, code: str, error: Exception | None = None
    ) -> ComponentJudgeResult:
        detail = ""
        if error is not None:
            detail = ":" + (
                " ".join(str(error).split())[-500:] or error.__class__.__name__
            )
        return ComponentJudgeResult(
            status="PENDING",
            decision=None,
            pending_reasons=(code + detail,),
            provider_name=self._provider_name,
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
    facts: Mapping[str, EvidenceFact],
    anchors: Mapping[str, Mapping[str, Any]],
) -> ComponentJudgeDecision:
    assert_blind_research_output(response)
    support_ids = _strings(response, "support_fact_ids")
    counter_ids = _strings(response, "counter_fact_ids")
    nearest_ids = _strings(response, "nearest_anchor_ids")
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
    allowed = response["allowed_range"]
    if isinstance(allowed, str) or not isinstance(allowed, Sequence) or len(allowed) != 2:
        raise TypeError("allowed_range must contain two numbers")
    lower, upper = (float(value) for value in allowed)
    proposed = float(response["proposed_points"])
    if not 0 <= lower <= proposed <= upper <= memo.component_max_points:
        raise ValueError("judge range exceeds the component maximum")
    return ComponentJudgeDecision(
        judge_id=stable_intelligence_id(
            "CJUDGE",
            {
                "memo_id": memo.memo_id,
                "role": role,
                "response": scrub_blind_research_payload(response),
            },
        ),
        memo_id=memo.memo_id,
        role=role,
        anchor_comparisons=_strings(response, "anchor_comparisons"),
        proposed_points=proposed,
        allowed_range=(lower, upper),
        rationale=str(response["rationale"]),
        disagreements=_strings(response, "disagreements"),
        support_fact_ids=support_ids,
        counter_fact_ids=counter_ids,
        nearest_anchor_ids=nearest_ids,
        why_not_higher=str(response["why_not_higher"]),
        why_not_lower=str(response["why_not_lower"]),
    )


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
    result = tuple(str(item).strip() for item in value)
    if any(not item for item in result) or len(result) != len(set(result)):
        raise ValueError(f"{key} must contain unique nonempty strings")
    return result


__all__ = [
    "AnalystJudge",
    "ComponentJudge",
    "ComponentJudgeResult",
    "SkepticJudge",
    "SynthesisJudge",
    "SynthesisResult",
]
