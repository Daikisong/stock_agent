"""Select one-to-three primary contracts and mandatory cross guards per job."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, Sequence

from .loader import ContractBundle, load_all_research_contracts, select_contract_bundle


@dataclass(frozen=True)
class PlannedQuestion:
    archetype_id: str
    contract_role: str
    question: Mapping[str, Any]

    @property
    def question_family_id(self) -> str:
        return str(self.question["question_family_id"])


@dataclass(frozen=True)
class ResearchQuestionPlan:
    bundle: ContractBundle
    questions: tuple[PlannedQuestion, ...]

    @property
    def mandatory_questions(self) -> tuple[PlannedQuestion, ...]:
        return tuple(
            row
            for row in self.questions
            if row.question.get("mandatory_for_full_thesis") is True
        )

    @property
    def mandatory_question_ids(self) -> tuple[str, ...]:
        return tuple(row.question_family_id for row in self.mandatory_questions)


def build_research_question_plan(
    primary_archetype_ids: Sequence[str],
) -> ResearchQuestionPlan:
    bundle = select_contract_bundle(primary_archetype_ids)
    questions = tuple(
        PlannedQuestion(
            archetype_id=str(contract["archetype_id"]),
            contract_role=str(contract["contract_role"]),
            question=question,
        )
        for contract in bundle.contracts
        for question in contract["question_families"]
    )
    ids = tuple(row.question_family_id for row in questions)
    if len(ids) != len(set(ids)):
        raise ValueError("compiled question plan contains duplicate family ids")
    return ResearchQuestionPlan(bundle=bundle, questions=questions)


def validate_archetype_reselection(candidate_archetype_id: str) -> str:
    registry = {
        str(row["archetype_id"]): str(row["contract_role"])
        for row in load_all_research_contracts()
    }
    if candidate_archetype_id not in registry:
        return "ARCHETYPE_RESELECTION_REQUIRED_UNKNOWN_REGISTRY_ID"
    if registry[candidate_archetype_id] != "PRIMARY":
        return "ARCHETYPE_RESELECTION_REQUIRED_PRIMARY_ID_ONLY"
    return "ARCHETYPE_RESELECTION_REQUIRED"


__all__ = [
    "PlannedQuestion",
    "ResearchQuestionPlan",
    "build_research_question_plan",
    "validate_archetype_reselection",
]
