"""Typed receipts for compact, fact-scoped RepairDeltaV3."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any, Mapping

from ..ids import canonical_hash


REPAIR_DELTA_V3_SCHEMA_VERSION = "e2r_pro_repair_delta_v3"
REPAIR_ACTIONS_V3 = frozenset({"CORRECT", "REPLACE", "NARROW", "WITHDRAW"})
REPAIR_ACTION_CONTRACT = "CORRECT|REPLACE|NARROW|WITHDRAW"
PRO_REPAIRABLE_ROOT_CAUSES = frozenset(
    {
        "INITIAL_PROMPT_OUTPUT_DEFECT",
        "GENUINE_SEMANTIC_OR_SOURCE_DEFECT",
    }
)


@dataclass(frozen=True)
class CompactRepairGroupV3:
    group_id: str
    source_document_id: str
    rejection_category: str
    question_family_ids: tuple[str, ...]
    canonical_url: str
    fetched_source_text: str
    fetched_source_text_hash: str | None
    candidates: tuple[Mapping[str, Any], ...]

    @property
    def candidate_ids(self) -> tuple[str, ...]:
        return tuple(str(row.get("candidate_id") or "") for row in self.candidates)

    def to_prompt_dict(self) -> Mapping[str, Any]:
        return {
            "group_id": self.group_id,
            "grouping_key": {
                "source_document_id": self.source_document_id,
                "rejection_category": self.rejection_category,
                "question_family_ids": list(self.question_family_ids),
            },
            "canonical_url": self.canonical_url,
            "fetched_source_text": self.fetched_source_text,
            "fetched_source_text_hash": self.fetched_source_text_hash,
            "candidates": [dict(row) for row in self.candidates],
        }


@dataclass(frozen=True)
class CompiledCompactRepairPromptV3:
    job_id: str
    run_id: str
    research_pass_id: str
    parent_pass_id: str
    target: Mapping[str, Any]
    as_of_date: str
    prompt_text: str
    prompt_hash: str
    schema_hash: str
    groups: tuple[CompactRepairGroupV3, ...]
    candidate_ids: tuple[str, ...]
    prompt_char_count: int
    target_char_limit: int
    hard_char_limit: int
    repair_pass_ordinal: int

    @property
    def target_size_met(self) -> bool:
        return self.prompt_char_count <= self.target_char_limit

    def to_receipt(self) -> Mapping[str, Any]:
        payload = {
            "schema_version": "e2r_compact_repair_prompt_v3_receipt_v1",
            "status": "COMPACT_REPAIR_PROMPT_COMPILED",
            "job_id": self.job_id,
            "run_id": self.run_id,
            "research_pass_id": self.research_pass_id,
            "parent_pass_id": self.parent_pass_id,
            "target_hash": canonical_hash(self.target),
            "as_of_date": self.as_of_date,
            "prompt_hash": self.prompt_hash,
            "repair_delta_schema_hash": self.schema_hash,
            "group_count": len(self.groups),
            "candidate_count": len(self.candidate_ids),
            "candidate_ids": list(self.candidate_ids),
            "prompt_char_count": self.prompt_char_count,
            "prompt_target_char_limit": self.target_char_limit,
            "prompt_hard_char_limit": self.hard_char_limit,
            "prompt_target_size_met": self.target_size_met,
            "full_dossier_reoutput_requested_count": 0,
            "local_normalizable_candidate_count": 0,
            "source_representation_candidate_count": 0,
            "repair_pass_ordinal": self.repair_pass_ordinal,
            "score_authority": False,
            "stage_authority": False,
        }
        return {**payload, "receipt_hash": canonical_hash(payload)}


@dataclass(frozen=True)
class RepairActionOutcomeV3:
    candidate_id: str
    action: str
    replacement_candidate_id: str | None
    question_family_ids: tuple[str, ...]
    action_hash: str

    def to_dict(self) -> Mapping[str, Any]:
        payload = asdict(self)
        payload["question_family_ids"] = list(self.question_family_ids)
        return payload


@dataclass(frozen=True)
class RepairApplicationV3:
    effective_dossier: Mapping[str, Any]
    outcomes: tuple[RepairActionOutcomeV3, ...]
    prior_accepted_candidate_ids: tuple[str, ...]
    preserved_accepted_candidate_ids: tuple[str, ...]
    prior_question_states: Mapping[str, Mapping[str, Any]]
    delta_hash: str
    effective_dossier_hash: str
    repair_pass_ordinal: int

    @property
    def replacement_candidate_ids(self) -> tuple[str, ...]:
        return tuple(
            str(row.replacement_candidate_id)
            for row in self.outcomes
            if row.replacement_candidate_id is not None
        )


__all__ = [
    "CompactRepairGroupV3",
    "CompiledCompactRepairPromptV3",
    "PRO_REPAIRABLE_ROOT_CAUSES",
    "REPAIR_ACTIONS_V3",
    "REPAIR_ACTION_CONTRACT",
    "REPAIR_DELTA_V3_SCHEMA_VERSION",
    "RepairActionOutcomeV3",
    "RepairApplicationV3",
]
