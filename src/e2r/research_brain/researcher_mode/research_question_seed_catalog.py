"""Research seeds and guards derived from legacy question contracts.

The catalog can suggest what to investigate.  It intentionally has no method
that classifies a claim as scoring, declares absence, completes a component,
or decides Stage.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Mapping

from e2r.research_brain.scoring.question_impact_contract import (
    DEFAULT_QUESTION_CONTRACT_PATH,
    load_question_impact_contracts,
)


@dataclass(frozen=True)
class ResearchQuestionSeed:
    seed_id: str
    question_family_id: str
    archetype_id: str
    mechanism_scope: str
    research_predicates: tuple[str, ...]
    primitive_tags: tuple[str, ...]
    component_topic_hints: tuple[str, ...]
    source_route_hints: tuple[str, ...]
    counter_route_hints: tuple[str, ...]
    retrieval_keyword_hints: tuple[str, ...]
    false_positive_guard_hints: tuple[str, ...]
    production_score_authority: bool = False
    component_completion_authority: bool = False
    absence_authority: bool = False
    final_stage_authority: bool = False
    schema_version: str = "e2r_research_question_seed_v1"

    def __post_init__(self) -> None:
        if not self.seed_id or not self.question_family_id or not self.archetype_id:
            raise ValueError("research question seed identity is required")
        if any(
            (
                self.production_score_authority,
                self.component_completion_authority,
                self.absence_authority,
                self.final_stage_authority,
            )
        ):
            raise ValueError("research question seeds cannot authorize score or Stage")

    def to_dict(self) -> Mapping[str, Any]:
        return json.loads(json.dumps(asdict(self), ensure_ascii=False))


@dataclass(frozen=True)
class ResearchQuestionSeedCatalog:
    seeds: tuple[ResearchQuestionSeed, ...]
    production_score_authority: bool = False
    final_stage_authority: bool = False
    schema_version: str = "e2r_research_question_seed_catalog_v1"

    def __post_init__(self) -> None:
        if not self.seeds:
            raise ValueError("research question seed catalog cannot be empty")
        ids = [row.seed_id for row in self.seeds]
        if len(ids) != len(set(ids)):
            raise ValueError("research question seeds must be unique")
        if self.production_score_authority or self.final_stage_authority:
            raise ValueError("research question seed catalog is never a scoring authority")

    def by_archetype(self, archetype_id: str) -> tuple[ResearchQuestionSeed, ...]:
        return tuple(row for row in self.seeds if row.archetype_id == archetype_id)

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "schema_version": self.schema_version,
            "production_score_authority": self.production_score_authority,
            "final_stage_authority": self.final_stage_authority,
            "seeds": [row.to_dict() for row in self.seeds],
        }


def load_research_question_seed_catalog(
    path: str | Path = DEFAULT_QUESTION_CONTRACT_PATH,
) -> ResearchQuestionSeedCatalog:
    contracts = load_question_impact_contracts(path)
    seeds = []
    for question_id, contract in sorted(contracts.items()):
        retrieval_hints = tuple(
            dict.fromkeys(
                (
                    *contract.full_support_keywords,
                    *contract.partial_keywords,
                    *(
                        value
                        for group in contract.required_keyword_groups
                        for value in group
                    ),
                )
            )
        )
        seeds.append(
            ResearchQuestionSeed(
                seed_id=f"RQSEED-{contract.contract_hash[:24]}",
                question_family_id=question_id,
                archetype_id=contract.archetype_id,
                mechanism_scope=contract.mechanism_scope,
                research_predicates=tuple(
                    dict.fromkeys(
                        (
                            *contract.accepted_claim_predicates,
                            *contract.partial_support_predicates,
                            *contract.non_scoring_support_predicates,
                        )
                    )
                ),
                primitive_tags=contract.allowed_primitive_ids,
                component_topic_hints=contract.allowed_component_ids,
                source_route_hints=contract.required_source_routes,
                counter_route_hints=contract.required_counter_routes,
                retrieval_keyword_hints=retrieval_hints,
                false_positive_guard_hints=tuple(
                    dict.fromkeys(
                        (
                            *contract.counter_predicates,
                            *contract.counter_keywords,
                            *contract.non_scoring_support_predicates,
                        )
                    )
                ),
            )
        )
    return ResearchQuestionSeedCatalog(seeds=tuple(seeds))


__all__ = [
    "ResearchQuestionSeed",
    "ResearchQuestionSeedCatalog",
    "load_research_question_seed_catalog",
]
