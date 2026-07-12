"""Run and persist three independent LLM scoring memos for seven components."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
import math
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.metadata import write_json, write_jsonl

from .calibration_judge import CalibrationJudge
from .component_judge import (
    JUDGE_PASS_BY_ROLE,
    AnalystJudge,
    ComponentJudgeResult,
    SkepticJudge,
)
from .component_researcher import ComponentResearchResult, StructuredResearchProvider
from .schemas import (
    CANONICAL_COMPONENT_ORDER,
    ComponentAnchor,
    ComponentJudgeDecision,
    ComponentJudgeRole,
    ComponentResearchMemo,
    EvidenceFact,
)


REQUIRED_COMPONENT_JUDGE_ROLES = tuple(
    value.value for value in ComponentJudgeRole
)

COMPONENT_SCORING_MEMO_OUTPUT_FILES: Mapping[str, str] = {
    "component_memos": "component_scoring_memos.jsonl",
    "judge_memos": "component_judge_scoring_memos.jsonl",
    "run": "component_scoring_memo_run.json",
    "audit": "component_scoring_memo_audit.json",
}


@dataclass(frozen=True)
class ComponentScoringMemo:
    component_id: str
    component_research_memo_id: str | None
    component_max_points: float | None
    status: str
    judge_results: tuple[ComponentJudgeResult, ...]
    pending_reasons: tuple[str, ...]
    ready_for_deterministic_aggregation: bool
    production_total_score_authority: bool = False
    production_stage_authority: bool = False
    schema_version: str = "e2r_component_scoring_memo_v1"

    def __post_init__(self) -> None:
        if self.component_id not in CANONICAL_COMPONENT_ORDER:
            raise ValueError("unknown component scoring memo component")
        if self.status not in {"COMPLETE", "PENDING"}:
            raise ValueError("unknown component scoring memo status")
        if self.component_research_memo_id is None:
            if self.component_max_points is not None:
                raise ValueError("missing component memo cannot have a point maximum")
        else:
            if not self.component_research_memo_id.strip():
                raise ValueError("component research memo id cannot be blank")
            if (
                isinstance(self.component_max_points, bool)
                or self.component_max_points is None
                or not math.isfinite(float(self.component_max_points))
                or float(self.component_max_points) <= 0
            ):
                raise ValueError("component scoring memo maximum is invalid")
        roles = [row.role for row in self.judge_results]
        if len(roles) != len(set(roles)):
            raise ValueError("component scoring memo has duplicate judge roles")
        if any(row.component_id != self.component_id for row in self.judge_results):
            raise ValueError("judge result belongs to another component")
        if self.component_research_memo_id and any(
            row.memo_id != self.component_research_memo_id
            for row in self.judge_results
        ):
            raise ValueError("judge result belongs to another research memo")
        complete_contract = bool(
            self.component_research_memo_id
            and tuple(sorted(roles))
            == tuple(sorted(REQUIRED_COMPONENT_JUDGE_ROLES))
            and all(row.status == "COMPLETE" for row in self.judge_results)
            and len({row.prompt_hash for row in self.judge_results}) == 3
            and len({row.judge_call_id for row in self.judge_results}) == 3
        )
        if self.status == "COMPLETE" and (
            not complete_contract or self.pending_reasons
        ):
            raise ValueError("complete component scoring memo lacks three independent judges")
        if self.status == "PENDING" and not self.pending_reasons:
            raise ValueError("pending component scoring memo requires reasons")
        if self.ready_for_deterministic_aggregation != (
            self.status == "COMPLETE" and complete_contract
        ):
            raise ValueError("component scoring memo readiness disagrees with lineage")
        if self.production_total_score_authority or self.production_stage_authority:
            raise ValueError("component scoring memo cannot decide total score or Stage")

    @property
    def judge_decisions(self) -> tuple[ComponentJudgeDecision, ...]:
        return tuple(
            row.decision for row in self.judge_results if row.decision is not None
        )

    @property
    def prompt_hashes(self) -> tuple[str, ...]:
        return tuple(
            row.prompt_hash for row in self.judge_results if row.prompt_hash
        )

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "schema_version": self.schema_version,
            "component_id": self.component_id,
            "component_research_memo_id": self.component_research_memo_id,
            "component_max_points": self.component_max_points,
            "status": self.status,
            "judge_results": [row.to_dict() for row in self.judge_results],
            "pending_reasons": list(self.pending_reasons),
            "ready_for_deterministic_aggregation": (
                self.ready_for_deterministic_aggregation
            ),
            "production_total_score_authority": False,
            "production_stage_authority": False,
        }


@dataclass(frozen=True)
class ComponentScoringMemoRun:
    target_id: str
    archetype_id: str
    as_of_date: str
    status: str
    component_memos: tuple[ComponentScoringMemo, ...]
    audit: Mapping[str, Any]
    ready_for_deterministic_aggregation: bool
    production_total_score_authority: bool = False
    production_stage_authority: bool = False
    schema_version: str = "e2r_component_scoring_memo_run_v1"

    def __post_init__(self) -> None:
        if not self.target_id.strip() or not self.archetype_id.strip():
            raise ValueError("component scoring memo run identity is incomplete")
        date.fromisoformat(self.as_of_date)
        if self.status not in {
            "COMPONENT_SCORING_MEMOS_COMPLETE",
            "COMPONENT_SCORING_MEMOS_PENDING",
        }:
            raise ValueError("unknown component scoring memo run status")
        if tuple(row.component_id for row in self.component_memos) != tuple(
            CANONICAL_COMPONENT_ORDER
        ):
            raise ValueError("component scoring memo run requires canonical seven order")
        critical_counts = self.audit.get("critical_counts")
        if not isinstance(critical_counts, Mapping) or any(
            isinstance(value, bool)
            or not isinstance(value, int)
            or value < 0
            for value in critical_counts.values()
        ):
            raise ValueError("component scoring memo audit critical counts are invalid")
        critical_sum = sum(critical_counts.values())
        if critical_sum != self.audit.get("critical_count_sum"):
            raise ValueError("component scoring memo audit counts do not reconcile")
        expected_audit_status = (
            "COMPONENT_SCORING_MEMO_AUDIT_PASS"
            if critical_sum == 0
            else "COMPONENT_SCORING_MEMO_AUDIT_FAIL"
        )
        if self.audit.get("status") != expected_audit_status:
            raise ValueError("component scoring memo audit status is invalid")
        if (
            self.audit.get("component_count") != len(self.component_memos)
            or self.audit.get("judge_memo_count")
            != sum(len(row.judge_results) for row in self.component_memos)
        ):
            raise ValueError("component scoring memo audit leaf counts do not reconcile")
        expected_complete = bool(
            critical_sum == 0
            and all(
                row.ready_for_deterministic_aggregation
                for row in self.component_memos
            )
        )
        expected_status = (
            "COMPONENT_SCORING_MEMOS_COMPLETE"
            if expected_complete
            else "COMPONENT_SCORING_MEMOS_PENDING"
        )
        if self.status != expected_status:
            raise ValueError("component scoring memo run status contradicts audit")
        if self.ready_for_deterministic_aggregation != expected_complete:
            raise ValueError("component scoring memo run readiness contradicts audit")
        if self.production_total_score_authority or self.production_stage_authority:
            raise ValueError("component scoring memo run cannot decide total score or Stage")

    @property
    def judge_decisions(self) -> tuple[ComponentJudgeDecision, ...]:
        return tuple(
            decision
            for memo in self.component_memos
            for decision in memo.judge_decisions
        )

    def to_score_gap_context(self) -> Mapping[str, Any]:
        return {
            "component_scoring_memo_status": self.status,
            "pending_components": [
                {
                    "component_id": row.component_id,
                    "pending_reasons": list(row.pending_reasons),
                }
                for row in self.component_memos
                if row.status == "PENDING"
            ],
            "ready_for_deterministic_aggregation": (
                self.ready_for_deterministic_aggregation
            ),
        }

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "schema_version": self.schema_version,
            "target_id": self.target_id,
            "archetype_id": self.archetype_id,
            "as_of_date": self.as_of_date,
            "status": self.status,
            "component_memos": [row.to_dict() for row in self.component_memos],
            "audit": dict(self.audit),
            "ready_for_deterministic_aggregation": (
                self.ready_for_deterministic_aggregation
            ),
            "production_total_score_authority": False,
            "production_stage_authority": False,
        }


class LLMComponentScoringMemoEngine:
    """Run 21 independent role/component calls without calculating a total."""

    def __init__(
        self,
        *,
        analyst_provider: StructuredResearchProvider | None,
        skeptic_provider: StructuredResearchProvider | None = None,
        calibration_provider: StructuredResearchProvider | None = None,
    ) -> None:
        self.providers: Mapping[str, StructuredResearchProvider | None] = {
            ComponentJudgeRole.ANALYST.value: analyst_provider,
            ComponentJudgeRole.SKEPTIC.value: (
                skeptic_provider
                if skeptic_provider is not None
                else analyst_provider
            ),
            ComponentJudgeRole.CALIBRATION_JUDGE.value: (
                calibration_provider
                if calibration_provider is not None
                else analyst_provider
            ),
        }

    def build(
        self,
        *,
        target_id: str,
        archetype_id: str,
        as_of_date: str,
        component_results: Sequence[ComponentResearchResult],
        evidence_facts: Sequence[EvidenceFact],
        historical_anchors: Sequence[ComponentAnchor | Mapping[str, Any]],
    ) -> ComponentScoringMemoRun:
        if not target_id.strip() or not archetype_id.strip():
            raise ValueError("component scoring memo target/archetype is required")
        date.fromisoformat(as_of_date)
        _validate_run_facts(
            target_id=target_id,
            as_of_date=as_of_date,
            evidence_facts=evidence_facts,
        )
        grouped: dict[str, list[ComponentResearchResult]] = {}
        unexpected_component_count = 0
        for row in component_results:
            if row.component_id not in CANONICAL_COMPONENT_ORDER:
                unexpected_component_count += 1
                continue
            grouped.setdefault(row.component_id, []).append(row)

        component_memos = []
        for component_id in CANONICAL_COMPONENT_ORDER:
            candidates = grouped.get(component_id, [])
            if len(candidates) != 1:
                reason = (
                    "COMPONENT_RESEARCH_RESULT_MISSING"
                    if not candidates
                    else "DUPLICATE_COMPONENT_RESEARCH_RESULT"
                )
                component_memos.append(
                    _pending_component_without_memo(component_id, reason)
                )
                continue
            research_result = candidates[0]
            memo = research_result.memo
            if research_result.status != "COMPLETE" or memo is None:
                detail = ";".join(research_result.pending_reasons) or "UNKNOWN"
                component_memos.append(
                    _pending_component_without_memo(
                        component_id,
                        f"COMPONENT_RESEARCH_PENDING:{detail}",
                    )
                )
                continue
            if (
                memo.target_id != target_id
                or memo.archetype_id != archetype_id
                or memo.component_id != component_id
            ):
                component_memos.append(
                    _pending_component_with_memo(
                        memo,
                        (),
                        ("COMPONENT_RESEARCH_MEMO_SCOPE_MISMATCH",),
                        component_id=component_id,
                    )
                )
                continue

            judge_results = tuple(
                self._run_role(
                    role=role,
                    memo=memo,
                    evidence_facts=evidence_facts,
                    historical_anchors=historical_anchors,
                )
                for role in REQUIRED_COMPONENT_JUDGE_ROLES
            )
            pending = [
                f"{row.role}:{reason}"
                for row in judge_results
                for reason in row.pending_reasons
            ]
            prompt_hashes = [
                row.prompt_hash for row in judge_results if row.prompt_hash
            ]
            call_ids = [
                row.judge_call_id for row in judge_results if row.judge_call_id
            ]
            if len(prompt_hashes) != 3 or len(set(prompt_hashes)) != 3:
                pending.append("THREE_JUDGE_PROMPT_INDEPENDENCE_NOT_PROVEN")
            if len(call_ids) != 3 or len(set(call_ids)) != 3:
                pending.append("THREE_JUDGE_CALL_INDEPENDENCE_NOT_PROVEN")
            component_memos.append(
                _pending_component_with_memo(
                    memo,
                    judge_results,
                    tuple(dict.fromkeys(pending)),
                )
                if pending
                else ComponentScoringMemo(
                    component_id=component_id,
                    component_research_memo_id=memo.memo_id,
                    component_max_points=memo.component_max_points,
                    status="COMPLETE",
                    judge_results=judge_results,
                    pending_reasons=(),
                    ready_for_deterministic_aggregation=True,
                )
            )

        memos = tuple(component_memos)
        audit = _audit_component_scoring_memos(
            component_memos=memos,
            input_component_results=component_results,
            unexpected_component_count=unexpected_component_count,
        )
        complete = audit["critical_count_sum"] == 0
        return ComponentScoringMemoRun(
            target_id=target_id,
            archetype_id=archetype_id,
            as_of_date=as_of_date,
            status=(
                "COMPONENT_SCORING_MEMOS_COMPLETE"
                if complete
                else "COMPONENT_SCORING_MEMOS_PENDING"
            ),
            component_memos=memos,
            audit=audit,
            ready_for_deterministic_aggregation=complete,
        )

    def _run_role(
        self,
        *,
        role: str,
        memo: ComponentResearchMemo,
        evidence_facts: Sequence[EvidenceFact],
        historical_anchors: Sequence[ComponentAnchor | Mapping[str, Any]],
    ) -> ComponentJudgeResult:
        provider = self.providers[role]
        if provider is None:
            return _unconfigured_judge_result(memo=memo, role=role)
        judge = {
            ComponentJudgeRole.ANALYST.value: AnalystJudge,
            ComponentJudgeRole.SKEPTIC.value: SkepticJudge,
            ComponentJudgeRole.CALIBRATION_JUDGE.value: CalibrationJudge,
        }[role](provider=provider)
        return judge.judge(
            memo=memo,
            evidence_facts=evidence_facts,
            historical_anchors=historical_anchors,
        )


def write_component_scoring_memo_run(
    result: ComponentScoringMemoRun,
    output_directory: str | Path,
) -> Mapping[str, Path]:
    root = Path(output_directory)
    paths = {
        key: root / filename
        for key, filename in COMPONENT_SCORING_MEMO_OUTPUT_FILES.items()
    }
    write_jsonl(
        paths["component_memos"],
        (row.to_dict() for row in result.component_memos),
    )
    write_jsonl(
        paths["judge_memos"],
        (
            row.to_dict()
            for memo in result.component_memos
            for row in memo.judge_results
        ),
    )
    write_json(paths["run"], result.to_dict())
    write_json(paths["audit"], result.audit)
    return paths


def _pending_component_without_memo(
    component_id: str,
    reason: str,
) -> ComponentScoringMemo:
    return ComponentScoringMemo(
        component_id=component_id,
        component_research_memo_id=None,
        component_max_points=None,
        status="PENDING",
        judge_results=(),
        pending_reasons=(reason,),
        ready_for_deterministic_aggregation=False,
    )


def _pending_component_with_memo(
    memo: ComponentResearchMemo,
    judge_results: Sequence[ComponentJudgeResult],
    pending_reasons: tuple[str, ...],
    *,
    component_id: str | None = None,
) -> ComponentScoringMemo:
    if not pending_reasons:
        raise ValueError("pending component helper requires reasons")
    return ComponentScoringMemo(
        component_id=component_id or memo.component_id,
        component_research_memo_id=memo.memo_id,
        component_max_points=memo.component_max_points,
        status="PENDING",
        judge_results=tuple(judge_results),
        pending_reasons=pending_reasons,
        ready_for_deterministic_aggregation=False,
    )


def _unconfigured_judge_result(
    *,
    memo: ComponentResearchMemo,
    role: str,
) -> ComponentJudgeResult:
    return ComponentJudgeResult(
        component_id=memo.component_id,
        memo_id=memo.memo_id,
        role=role,
        pass_name=JUDGE_PASS_BY_ROLE[role],
        status="PENDING",
        decision=None,
        pending_reasons=("COMPONENT_JUDGE_PROVIDER_NOT_CONFIGURED",),
        provider_name="UNCONFIGURED",
        prompt_hash=None,
        response_hash=None,
        judge_call_id=None,
    )


def _validate_run_facts(
    *,
    target_id: str,
    as_of_date: str,
    evidence_facts: Sequence[EvidenceFact],
) -> None:
    ids = [row.fact_id for row in evidence_facts]
    if len(ids) != len(set(ids)):
        raise ValueError("component scoring memo EvidenceFact ids must be unique")
    if any(
        row.target_id != target_id or row.as_of_date != as_of_date
        for row in evidence_facts
    ):
        raise ValueError("component scoring memo fact target/as_of mismatch")


def _audit_component_scoring_memos(
    *,
    component_memos: Sequence[ComponentScoringMemo],
    input_component_results: Sequence[ComponentResearchResult],
    unexpected_component_count: int,
) -> Mapping[str, Any]:
    complete_judges = [
        row
        for memo in component_memos
        for row in memo.judge_results
        if row.status == "COMPLETE" and row.decision is not None
    ]
    prompt_hashes_by_component = {
        memo.component_id: [
            row.prompt_hash for row in memo.judge_results if row.prompt_hash
        ]
        for memo in component_memos
    }
    call_ids_by_component = {
        memo.component_id: [
            row.judge_call_id for row in memo.judge_results if row.judge_call_id
        ]
        for memo in component_memos
    }
    input_counts = {
        component_id: sum(
            row.component_id == component_id for row in input_component_results
        )
        for component_id in CANONICAL_COMPONENT_ORDER
    }
    critical = {
        "unexpected_component_research_result_count": unexpected_component_count,
        "missing_component_research_result_count": sum(
            value == 0 for value in input_counts.values()
        ),
        "duplicate_component_research_result_count": sum(
            value > 1 for value in input_counts.values()
        ),
        "incomplete_component_scoring_memo_count": sum(
            row.status != "COMPLETE" for row in component_memos
        ),
        "judge_result_roster_mismatch_count": sum(
            {row.role for row in memo.judge_results}
            != set(REQUIRED_COMPONENT_JUDGE_ROLES)
            for memo in component_memos
        ),
        "pending_judge_result_count": sum(
            row.status != "COMPLETE"
            for memo in component_memos
            for row in memo.judge_results
        ),
        "judge_prompt_hash_missing_count": sum(
            not row.prompt_hash for row in complete_judges
        ),
        "judge_response_hash_missing_count": sum(
            not row.response_hash for row in complete_judges
        ),
        "judge_call_id_missing_count": sum(
            not row.judge_call_id for row in complete_judges
        ),
        "within_component_duplicate_prompt_hash_count": sum(
            len(values) - len(set(values))
            for values in prompt_hashes_by_component.values()
        ),
        "within_component_duplicate_judge_call_id_count": sum(
            len(values) - len(set(values))
            for values in call_ids_by_component.values()
        ),
        "judge_nearest_anchor_missing_count": sum(
            not row.decision.nearest_anchor_ids for row in complete_judges
        ),
        "judge_bound_explanation_missing_count": sum(
            not row.decision.why_not_higher.strip()
            or not row.decision.why_not_lower.strip()
            for row in complete_judges
        ),
        "judge_component_max_violation_count": sum(
            row.decision.allowed_range[1]
            > row.decision.component_max_points + 1e-9
            or row.decision.proposed_points
            > row.decision.component_max_points + 1e-9
            for row in complete_judges
        ),
        "llm_total_score_authority_count": sum(
            row.production_total_score_authority
            or row.decision.production_total_score_authority
            for row in complete_judges
        ),
        "llm_stage_authority_count": sum(
            row.production_stage_authority
            or row.decision.production_stage_authority
            for row in complete_judges
        ),
    }
    critical_sum = sum(critical.values())
    return {
        "schema_version": "e2r_component_scoring_memo_audit_v1",
        "status": (
            "COMPONENT_SCORING_MEMO_AUDIT_PASS"
            if critical_sum == 0
            else "COMPONENT_SCORING_MEMO_AUDIT_FAIL"
        ),
        "critical_counts": critical,
        "critical_count_sum": critical_sum,
        "component_count": len(component_memos),
        "judge_memo_count": sum(
            len(row.judge_results) for row in component_memos
        ),
        "complete_judge_memo_count": len(complete_judges),
        "required_judge_roles": list(REQUIRED_COMPONENT_JUDGE_ROLES),
        "component_max_points": {
            row.component_id: row.component_max_points for row in component_memos
        },
        "independent_role_prompt_hashes_required": True,
        "prior_component_score_band_exposed_to_judges": False,
        "tiny_impact_cap_multiplication_used": False,
        "production_total_score_authority": False,
        "production_stage_authority": False,
    }


__all__ = [
    "COMPONENT_SCORING_MEMO_OUTPUT_FILES",
    "ComponentScoringMemo",
    "ComponentScoringMemoRun",
    "LLMComponentScoringMemoEngine",
    "REQUIRED_COMPONENT_JUDGE_ROLES",
    "write_component_scoring_memo_run",
]
