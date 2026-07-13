"""Provider-backed component researchers for canonical E2R v5 Researcher Mode."""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any, Mapping, Protocol, Sequence

from e2r.research_brain.intelligence_schema import stable_intelligence_id
from e2r.research_brain.planning.provider_transport import (
    CodexStructuredProviderTransport,
    StructuredProviderRejected,
    StructuredProviderUnavailable,
)

from .component_research_planner import (
    COMPONENT_RESEARCHER_ROLE_BY_COMPONENT,
)
from .schemas import (
    BusinessModelMemo,
    ComponentAnchor,
    ComponentResearchMemo,
    ComponentResearchPlan,
    EvidenceDirection,
    EvidenceFact,
    EvidenceLifecycle,
    assert_blind_research_output,
    scrub_blind_research_payload,
)
from .prompt_projection import (
    citable_fact_id_by_row_index,
    project_citable_evidence_facts,
    project_source_claims,
    project_source_document_table,
    resolve_citable_fact_row_indices,
)


class StructuredResearchProvider(Protocol):
    provider_name: str

    def complete(
        self, *, pass_name: str, payload: Mapping[str, Any]
    ) -> Mapping[str, Any]: ...


@dataclass(frozen=True)
class ComponentResearchResult:
    component_id: str
    researcher_role: str
    status: str
    memo: ComponentResearchMemo | None
    pending_reasons: tuple[str, ...]
    provider_name: str
    prompt_hash: str | None = None

    def __post_init__(self) -> None:
        if self.status not in {"COMPLETE", "PENDING"}:
            raise ValueError("unknown component research status")
        if self.status == "COMPLETE" and (
            self.memo is None or not self.memo.research_complete
        ):
            raise ValueError("COMPLETE result requires a complete memo")
        if self.status == "PENDING" and not self.pending_reasons:
            raise ValueError("PENDING result requires a reason")

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "component_id": self.component_id,
            "researcher_role": self.researcher_role,
            "status": self.status,
            "memo": self.memo.to_dict() if self.memo else None,
            "pending_reasons": list(self.pending_reasons),
            "provider_name": self.provider_name,
            "prompt_hash": self.prompt_hash,
        }


_STRING_ARRAY: Mapping[str, Any] = {
    "type": "array",
    "items": {"type": "string", "minLength": 1},
}

_NONNEGATIVE_INTEGER_ARRAY: Mapping[str, Any] = {
    "type": "array",
    "items": {"type": "integer", "minimum": 0},
}

BUSINESS_MODEL_RESEARCH_SCHEMA: Mapping[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": [
        "business_model_summary",
        "revenue_engines",
        "cost_and_cash_drivers",
        "capacity_and_supply_constraints",
        "customer_and_channel_dependencies",
        "fact_row_indices",
        "uncertainties",
        "confidence",
        "research_complete",
    ],
    "properties": {
        "business_model_summary": {"type": "string", "minLength": 1},
        "revenue_engines": {**_STRING_ARRAY, "minItems": 1},
        "cost_and_cash_drivers": _STRING_ARRAY,
        "capacity_and_supply_constraints": _STRING_ARRAY,
        "customer_and_channel_dependencies": _STRING_ARRAY,
        "fact_row_indices": _NONNEGATIVE_INTEGER_ARRAY,
        "uncertainties": _STRING_ARRAY,
        "confidence": {"type": "number", "minimum": 0, "maximum": 1},
        "research_complete": {"type": "boolean"},
    },
}

COMPONENT_RESEARCH_SCHEMA: Mapping[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": [
        "selected_fact_row_indices",
        "structured_metric_ids",
        "historical_anchor_ids",
        "nearest_positive_anchor_ids",
        "nearest_counter_anchor_ids",
        "researcher_summary",
        "positive_case",
        "counter_case",
        "uncertainties",
        "source_coverage",
        "proposed_score_lower",
        "proposed_score_mid",
        "proposed_score_upper",
        "why_not_higher",
        "why_not_lower",
        "confidence",
        "research_complete",
    ],
    "properties": {
        "selected_fact_row_indices": _NONNEGATIVE_INTEGER_ARRAY,
        "structured_metric_ids": _STRING_ARRAY,
        "historical_anchor_ids": _STRING_ARRAY,
        "nearest_positive_anchor_ids": _STRING_ARRAY,
        "nearest_counter_anchor_ids": _STRING_ARRAY,
        "researcher_summary": {"type": "string", "minLength": 1},
        "positive_case": {"type": "string", "minLength": 1},
        "counter_case": {"type": "string", "minLength": 1},
        "uncertainties": _STRING_ARRAY,
        "source_coverage": _STRING_ARRAY,
        "proposed_score_lower": {"type": "number", "minimum": 0},
        "proposed_score_mid": {"type": "number", "minimum": 0},
        "proposed_score_upper": {"type": "number", "minimum": 0},
        "why_not_higher": {"type": "string", "minLength": 1},
        "why_not_lower": {"type": "string", "minLength": 1},
        "confidence": {"type": "number", "minimum": 0, "maximum": 1},
        "research_complete": {"type": "boolean"},
    },
}

RED_TEAM_RESEARCH_SCHEMA: Mapping[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": [
        "reviewed_component_ids",
        "challenged_fact_row_indices",
        "resolved_challenges",
        "unresolved_challenges",
        "recommended_research_directions",
        "source_coverage",
        "confidence",
        "review_complete",
    ],
    "properties": {
        "reviewed_component_ids": _STRING_ARRAY,
        "challenged_fact_row_indices": _NONNEGATIVE_INTEGER_ARRAY,
        "resolved_challenges": _STRING_ARRAY,
        "unresolved_challenges": _STRING_ARRAY,
        "recommended_research_directions": _STRING_ARRAY,
        "source_coverage": _STRING_ARRAY,
        "confidence": {"type": "number", "minimum": 0, "maximum": 1},
        "review_complete": {"type": "boolean"},
    },
}

SYNTHESIS_REVIEW_SCHEMA: Mapping[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": [
        "component_memo_ids",
        "cross_component_support",
        "cross_component_tensions",
        "unresolved_material_questions",
        "synthesis_summary",
        "confidence",
        "synthesis_complete",
    ],
    "properties": {
        "component_memo_ids": {**_STRING_ARRAY, "minItems": 1},
        "cross_component_support": _STRING_ARRAY,
        "cross_component_tensions": _STRING_ARRAY,
        "unresolved_material_questions": _STRING_ARRAY,
        "synthesis_summary": {"type": "string", "minLength": 1},
        "confidence": {"type": "number", "minimum": 0, "maximum": 1},
        "synthesis_complete": {"type": "boolean"},
    },
}

COMPONENT_JUDGE_SCHEMA: Mapping[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": [
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
    ],
    "properties": {
        "anchor_comparisons": _STRING_ARRAY,
        "proposed_points": {"type": "number", "minimum": 0},
        "allowed_range": {
            "type": "array",
            "minItems": 2,
            "maxItems": 2,
            "items": {"type": "number", "minimum": 0},
        },
        "rationale": {"type": "string", "minLength": 1},
        "disagreements": _STRING_ARRAY,
        "support_fact_ids": _STRING_ARRAY,
        "counter_fact_ids": _STRING_ARRAY,
        "nearest_anchor_ids": _STRING_ARRAY,
        "why_not_higher": {"type": "string", "minLength": 1},
        "why_not_lower": {"type": "string", "minLength": 1},
    },
}

SOURCE_QUERY_GENERATION_SCHEMA: Mapping[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": [
        "suggested_queries",
        "new_source_directions",
        "unresolved_research_notes",
    ],
    "properties": {
        "suggested_queries": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": [
                    "objective_id",
                    "literal_query",
                    "source_families",
                    "rationale",
                    "counter_or_supersession_search",
                ],
                "properties": {
                    "objective_id": {"type": "string", "minLength": 1},
                    "literal_query": {"type": "string", "minLength": 1},
                    "source_families": {**_STRING_ARRAY, "minItems": 1},
                    "rationale": {"type": "string", "minLength": 1},
                    "counter_or_supersession_search": {"type": "boolean"},
                },
            },
        },
        "new_source_directions": _STRING_ARRAY,
        "unresolved_research_notes": _STRING_ARRAY,
    },
}

SOURCE_CANDIDATE_RANKING_SCHEMA: Mapping[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": ["decisions", "ranking_complete", "unresolved_notes"],
    "properties": {
        "decisions": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": [
                    "candidate_id",
                    "material_relevance",
                    "priority",
                    "objective_ids",
                    "rationale",
                ],
                "properties": {
                    "candidate_id": {"type": "string", "minLength": 1},
                    "material_relevance": {"type": "boolean"},
                    "priority": {"type": "number", "minimum": 0, "maximum": 1},
                    "objective_ids": _STRING_ARRAY,
                    "rationale": {"type": "string", "minLength": 1},
                },
            },
        },
        "ranking_complete": {"type": "boolean"},
        "unresolved_notes": _STRING_ARRAY,
    },
}

EVIDENCE_FACT_EXTRACTION_SCHEMA: Mapping[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": [
        "facts",
        "document_dispositions",
        "unresolved_document_ids",
        "unresolved_research_notes",
        "extraction_complete",
    ],
    "properties": {
        "facts": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": [
                    "document_id",
                    "question_family_id",
                    "subject_id",
                    "subject",
                    "business_segment",
                    "product_family",
                    "scope_business_segment",
                    "scope_product_family",
                    "scope_technology_family",
                    "scope_transaction_type",
                    "scope_economic_mechanism",
                    "scope_confidence",
                    "economic_mechanism",
                    "mechanism_scope_id",
                    "predicate",
                    "predicate_family",
                    "value",
                    "normalized_object",
                    "unit",
                    "period",
                    "direction",
                    "current_lifecycle",
                    "exact_quote",
                    "material",
                    "materiality",
                    "materiality_rationale",
                    "confidence",
                    "question_family_tags",
                    "primitive_tags",
                    "structured_evidence_roles",
                ],
                "properties": {
                    "document_id": {"type": "string", "minLength": 1},
                    "question_family_id": {"type": "string", "minLength": 1},
                    "subject_id": {"type": "string", "minLength": 1},
                    "subject": {"type": "string", "minLength": 1},
                    "business_segment": {"type": "string", "minLength": 1},
                    "product_family": {"type": "string", "minLength": 1},
                    "scope_business_segment": {"type": "string", "minLength": 1},
                    "scope_product_family": {"type": "string", "minLength": 1},
                    "scope_technology_family": {"type": "string", "minLength": 1},
                    "scope_transaction_type": {"type": "string", "minLength": 1},
                    "scope_economic_mechanism": {"type": "string", "minLength": 1},
                    "scope_confidence": {
                        "type": "number",
                        "minimum": 0,
                        "maximum": 1,
                    },
                    "economic_mechanism": {"type": "string", "minLength": 1},
                    "mechanism_scope_id": {"type": "string", "minLength": 1},
                    "predicate": {"type": "string", "minLength": 1},
                    "predicate_family": {"type": "string", "minLength": 1},
                    "value": {"type": "string", "minLength": 1},
                    "normalized_object": {"type": "string", "minLength": 1},
                    "unit": {"type": "string"},
                    "period": {"type": "string", "minLength": 1},
                    "direction": {
                        "type": "string",
                        "enum": ["POSITIVE", "COUNTER", "NEUTRAL", "RESOLUTION"],
                    },
                    "current_lifecycle": {
                        "type": "string",
                        "enum": ["OPEN", "CURRENT", "RESOLVED", "SUPERSEDED"],
                    },
                    "exact_quote": {"type": "string", "minLength": 1},
                    "material": {"type": "boolean"},
                    "materiality": {
                        "type": "string",
                        "enum": ["CRITICAL", "NONCRITICAL"],
                    },
                    "materiality_rationale": {"type": "string", "minLength": 1},
                    "confidence": {"type": "number", "minimum": 0, "maximum": 1},
                    "question_family_tags": _STRING_ARRAY,
                    "primitive_tags": _STRING_ARRAY,
                    "structured_evidence_roles": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "enum": [
                                "SEGMENT_CONTRIBUTION",
                                "QOQ_GROWTH",
                                "FORWARD_GUIDANCE",
                            ],
                        },
                    },
                },
            },
        },
        "document_dispositions": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": ["document_id", "status", "rationale"],
                "properties": {
                    "document_id": {"type": "string", "minLength": 1},
                    "status": {
                        "type": "string",
                        "enum": [
                            "FACTS_EXTRACTED",
                            "NO_MATERIAL_FACT",
                            "WRONG_TARGET_OR_SEGMENT",
                            "UNREADABLE",
                        ],
                    },
                    "rationale": {"type": "string", "minLength": 1},
                },
            },
        },
        "unresolved_document_ids": _STRING_ARRAY,
        "unresolved_research_notes": _STRING_ARRAY,
        "extraction_complete": {"type": "boolean"},
    },
}

RESEARCH_SUPERVISOR_SCHEMA: Mapping[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": [
        "component_findings",
        "missing_material_facts",
        "failure_assessments",
        "new_source_family_directions",
        "query_direction_briefs",
        "unresolved_material_questions",
        "next_actions",
        "counter_and_supersession_checked",
        "structured_data_complete",
        "component_memos_sufficient",
        "reasonable_positive_routes_remaining",
        "ready_for_independent_saturation_review",
        "rationale",
    ],
    "properties": {
        "component_findings": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": [
                    "component_id",
                    "memo_sufficient",
                    "missing_fact_needs",
                    "rationale",
                ],
                "properties": {
                    "component_id": {"type": "string", "minLength": 1},
                    "memo_sufficient": {"type": "boolean"},
                    "missing_fact_needs": _STRING_ARRAY,
                    "rationale": {"type": "string", "minLength": 1},
                },
            },
        },
        "missing_material_facts": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": [
                    "component_id",
                    "fact_need",
                    "why_material",
                    "direction",
                ],
                "properties": {
                    "component_id": {"type": "string", "minLength": 1},
                    "fact_need": {"type": "string", "minLength": 1},
                    "why_material": {"type": "string", "minLength": 1},
                    "direction": {
                        "type": "string",
                        "enum": ["POSITIVE", "COUNTER", "RESOLUTION"],
                    },
                },
            },
        },
        "failure_assessments": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": [
                    "failure_id",
                    "classification",
                    "rationale",
                    "retryable",
                    "source_absence_claim_allowed",
                ],
                "properties": {
                    "failure_id": {"type": "string", "minLength": 1},
                    "classification": {
                        "type": "string",
                        "enum": [
                            "PROVIDER_FAILURE",
                            "AUTH_FAILURE",
                            "RATE_LIMIT",
                            "FETCH_FAILURE",
                            "PARSER_EXTRACTOR_FAILURE",
                            "IRRELEVANT_DOCUMENT",
                            "DUPLICATE_QUERY",
                            "FUTURE_LEAKAGE",
                            "INSUFFICIENT_SEARCH",
                            "SOURCE_ABSENCE_CANDIDATE",
                        ],
                    },
                    "rationale": {"type": "string", "minLength": 1},
                    "retryable": {"type": "boolean"},
                    "source_absence_claim_allowed": {"type": "boolean"},
                },
            },
        },
        "new_source_family_directions": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": [
                    "objective_id",
                    "source_family",
                    "direction",
                    "rationale",
                    "counter_or_supersession",
                ],
                "properties": {
                    "objective_id": {"type": "string", "minLength": 1},
                    "source_family": {"type": "string", "minLength": 1},
                    "direction": {"type": "string", "minLength": 1},
                    "rationale": {"type": "string", "minLength": 1},
                    "counter_or_supersession": {"type": "boolean"},
                },
            },
        },
        "query_direction_briefs": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": [
                    "objective_id",
                    "research_need",
                    "avoid_repeating",
                    "counter_or_supersession",
                ],
                "properties": {
                    "objective_id": {"type": "string", "minLength": 1},
                    "research_need": {"type": "string", "minLength": 1},
                    "avoid_repeating": _STRING_ARRAY,
                    "counter_or_supersession": {"type": "boolean"},
                },
            },
        },
        "unresolved_material_questions": _STRING_ARRAY,
        "next_actions": _STRING_ARRAY,
        "counter_and_supersession_checked": {"type": "boolean"},
        "structured_data_complete": {"type": "boolean"},
        "component_memos_sufficient": {"type": "boolean"},
        "reasonable_positive_routes_remaining": {"type": "boolean"},
        "ready_for_independent_saturation_review": {"type": "boolean"},
        "rationale": {"type": "string", "minLength": 1},
    },
}

SEMANTIC_SATURATION_REVIEW_SCHEMA: Mapping[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": [
        "approve",
        "seven_component_memos_complete",
        "material_positive_routes_reviewed",
        "counter_and_supersession_routes_checked",
        "structured_data_complete",
        "new_source_family_directions_reviewed",
        "reasonable_positive_routes_remaining",
        "unresolved_material_questions",
        "rationale",
    ],
    "properties": {
        "approve": {"type": "boolean"},
        "seven_component_memos_complete": {"type": "boolean"},
        "material_positive_routes_reviewed": {"type": "boolean"},
        "counter_and_supersession_routes_checked": {"type": "boolean"},
        "structured_data_complete": {"type": "boolean"},
        "new_source_family_directions_reviewed": {"type": "boolean"},
        "reasonable_positive_routes_remaining": {"type": "boolean"},
        "unresolved_material_questions": _STRING_ARRAY,
        "rationale": {"type": "string", "minLength": 1},
    },
}

CLAIM_COMPONENT_IMPACT_MAPPING_SCHEMA: Mapping[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": [
        "impact_proposals",
        "non_scoring_dispositions",
        "mapping_complete",
        "unresolved_claim_ids",
        "rationale",
    ],
    "properties": {
        "impact_proposals": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": [
                    "claim_id",
                    "fact_id",
                    "component_id",
                    "direction",
                    "component_mechanism_id",
                    "fact_economic_mechanism",
                    "proposed_credit_units",
                    "rationale",
                ],
                "properties": {
                    "claim_id": {"type": "string", "minLength": 1},
                    "fact_id": {"type": "string", "minLength": 1},
                    "component_id": {"type": "string", "minLength": 1},
                    "direction": {
                        "type": "string",
                        "enum": ["SUPPORT", "COUNTER"],
                    },
                    "component_mechanism_id": {
                        "type": "string",
                        "minLength": 1,
                    },
                    "fact_economic_mechanism": {
                        "type": "string",
                        "minLength": 1,
                    },
                    "proposed_credit_units": {
                        "type": "number",
                        "exclusiveMinimum": 0,
                        "maximum": 1,
                    },
                    "rationale": {"type": "string", "minLength": 1},
                },
            },
        },
        "non_scoring_dispositions": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": [
                    "claim_id",
                    "fact_id",
                    "status",
                    "rationale",
                    "component_ids",
                ],
                "properties": {
                    "claim_id": {"type": "string", "minLength": 1},
                    "fact_id": {"type": "string", "minLength": 1},
                    "status": {
                        "type": "string",
                        "enum": [
                            "PROFILE_ONLY",
                            "WRONG_MECHANISM",
                            "REJECTED_WITH_REASON",
                        ],
                    },
                    "rationale": {"type": "string", "minLength": 1},
                    "component_ids": _STRING_ARRAY,
                },
            },
        },
        "mapping_complete": {"type": "boolean"},
        "unresolved_claim_ids": _STRING_ARRAY,
        "rationale": {"type": "string", "minLength": 1},
    },
}

STRUCTURED_PEER_SELECTION_SCHEMA: Mapping[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": [
        "peers",
        "selection_complete",
        "unresolved_research_notes",
        "selection_rationale",
    ],
    "properties": {
        "peers": {
            "type": "array",
            "minItems": 2,
            "maxItems": 5,
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": [
                    "peer_symbol",
                    "peer_name",
                    "shared_economic_drivers",
                    "material_differences",
                    "comparability_rationale",
                    "confidence",
                ],
                "properties": {
                    "peer_symbol": {
                        "type": "string",
                        "pattern": "^[0-9]{6}$",
                    },
                    "peer_name": {"type": "string", "minLength": 1},
                    "shared_economic_drivers": {**_STRING_ARRAY, "minItems": 1},
                    "material_differences": {**_STRING_ARRAY, "minItems": 1},
                    "comparability_rationale": {"type": "string", "minLength": 1},
                    "confidence": {"type": "number", "minimum": 0, "maximum": 1},
                },
            },
        },
        "selection_complete": {"type": "boolean"},
        "unresolved_research_notes": _STRING_ARRAY,
        "selection_rationale": {"type": "string", "minLength": 1},
    },
}

_PROVIDER_SCHEMAS: Mapping[str, Mapping[str, Any]] = {
    "BUSINESS_MODEL_RESEARCH": BUSINESS_MODEL_RESEARCH_SCHEMA,
    "COMPONENT_RESEARCH": COMPONENT_RESEARCH_SCHEMA,
    "RED_TEAM_RESEARCH": RED_TEAM_RESEARCH_SCHEMA,
    "SYNTHESIS_REVIEW": SYNTHESIS_REVIEW_SCHEMA,
    "COMPONENT_ANALYST_JUDGE": COMPONENT_JUDGE_SCHEMA,
    "COMPONENT_SKEPTIC_JUDGE": COMPONENT_JUDGE_SCHEMA,
    "CALIBRATION_JUDGE": COMPONENT_JUDGE_SCHEMA,
    "SOURCE_QUERY_GENERATION": SOURCE_QUERY_GENERATION_SCHEMA,
    "SOURCE_CANDIDATE_RANKING": SOURCE_CANDIDATE_RANKING_SCHEMA,
    "EVIDENCE_FACT_EXTRACTION": EVIDENCE_FACT_EXTRACTION_SCHEMA,
    "RESEARCH_SUPERVISOR_REVIEW": RESEARCH_SUPERVISOR_SCHEMA,
    "SEMANTIC_SATURATION_REVIEW": SEMANTIC_SATURATION_REVIEW_SCHEMA,
    "CLAIM_COMPONENT_IMPACT_MAPPING": CLAIM_COMPONENT_IMPACT_MAPPING_SCHEMA,
    "STRUCTURED_PEER_SELECTION": STRUCTURED_PEER_SELECTION_SCHEMA,
}

_CODEX_PROMPT_TRANSPORT_MAX_CHARS = 1_000_000


@dataclass
class CodexResearcherProvider:
    """Default structured Codex provider for open-ended research judgments."""

    transport: CodexStructuredProviderTransport
    provider_name: str = "CODEX_STRUCTURED_RESEARCHER_MODE"
    calls: list[Mapping[str, Any]] = field(default_factory=list)

    @classmethod
    def default(
        cls,
        *,
        working_directory: str | Path | None = None,
        timeout_seconds: float = 300.0,
    ) -> "CodexResearcherProvider":
        return cls(
            CodexStructuredProviderTransport(
                working_directory=working_directory or Path.cwd(),
                timeout_seconds=timeout_seconds,
                extra_args=("--ignore-user-config", "--ignore-rules"),
            )
        )

    def complete(
        self, *, pass_name: str, payload: Mapping[str, Any]
    ) -> Mapping[str, Any]:
        if pass_name not in _PROVIDER_SCHEMAS:
            raise ValueError(f"unsupported researcher pass: {pass_name}")
        safe_payload = scrub_blind_research_payload(payload)
        instruction = _pass_instruction(pass_name)
        prompt = "\n".join(
            (
                "You are an independent E2R 2.0 research analyst.",
                "Use only the supplied as-of-date sources, claims, EvidenceFacts, structured records, and blind historical anchors.",
                "Read the full economic mechanism; primitive names and question seeds are investigation hints, never score gates.",
                "For loss-accounted transport projections, decode each row with its shared field legend, review every row/group, and never treat projection hashes as research completion.",
                "Decode current_evidence_fact_graph rows with current_evidence_fact_projection.fact_fields, and decode source_claims.claims with source_claims.claim_fields.",
                "When the schema asks for fact_row_indices, return only exact non-negative fact_row_index values from those rows; deterministic code resolves immutable fact ids.",
                "Cite only ids present in the input. Do not invent facts, sources, metrics, or anchors.",
                "Never output a total score, canonical Stage, investment recommendation, MFE/MAE, or any future outcome.",
                instruction,
                "Return exactly one JSON object matching the supplied schema.",
                json.dumps(safe_payload, ensure_ascii=False, sort_keys=True),
            )
        )
        prompt_hash = hashlib.sha256(prompt.encode("utf-8")).hexdigest()
        if len(prompt) > _CODEX_PROMPT_TRANSPORT_MAX_CHARS:
            self.calls.append(
                {
                    "pass_name": pass_name,
                    "prompt_hash": prompt_hash,
                    "prompt_chars": len(prompt),
                    "payload": safe_payload,
                    "response": None,
                    "status": "PROMPT_TRANSPORT_REJECTED",
                }
            )
            raise StructuredProviderRejected(
                f"prompt_transport_too_large:{len(prompt)}:"
                f"max={_CODEX_PROMPT_TRANSPORT_MAX_CHARS}"
            )
        response = self.transport.complete(
            prompt=prompt,
            output_schema=_PROVIDER_SCHEMAS[pass_name],
            schema_name=f"e2r_v5_{pass_name.lower()}",
        )
        assert_blind_research_output(response.payload)
        self.calls.append(
            {
                "pass_name": pass_name,
                "prompt_hash": prompt_hash,
                "prompt_chars": len(prompt),
                "payload": safe_payload,
                "response": dict(response.payload),
                "status": "COMPLETE",
            }
        )
        return response.payload


class ComponentResearcher:
    component_id: str
    researcher_role: str

    def __init__(
        self,
        *,
        provider: StructuredResearchProvider,
        component_id: str | None = None,
        researcher_role: str | None = None,
    ) -> None:
        resolved_component = component_id or getattr(self, "component_id", "")
        if resolved_component not in COMPONENT_RESEARCHER_ROLE_BY_COMPONENT:
            raise ValueError("ComponentResearcher requires a canonical component")
        expected_role = COMPONENT_RESEARCHER_ROLE_BY_COMPONENT[resolved_component]
        resolved_role = researcher_role or getattr(self, "researcher_role", expected_role)
        if resolved_role != expected_role:
            raise ValueError("researcher role does not match component")
        self.provider = provider
        self.component_id = resolved_component
        self.researcher_role = resolved_role

    def research(
        self,
        *,
        plan: ComponentResearchPlan,
        business_model: BusinessModelMemo,
        evidence_facts: Sequence[EvidenceFact | Mapping[str, Any]],
        historical_anchors: Sequence[ComponentAnchor | Mapping[str, Any]],
        source_coverage: Sequence[str | Mapping[str, Any]],
        source_claims: Sequence[Mapping[str, Any]] = (),
        source_documents: Sequence[Mapping[str, Any]] = (),
        structured_metrics: Mapping[str, Any] | None = None,
    ) -> ComponentResearchResult:
        if plan.component_id != self.component_id or plan.researcher_role != self.researcher_role:
            raise ValueError("research plan was assigned to the wrong researcher")
        if (
            plan.target_id != business_model.target_id
            or plan.archetype_id != business_model.archetype_id
        ):
            raise ValueError("business model and component plan target mismatch")
        facts = tuple(_coerce_fact(row) for row in evidence_facts)
        _validate_current_facts(facts, plan.target_id, business_model.as_of_date)
        fact_by_id = {row.fact_id: row for row in facts}
        if set(fact_by_id) - set(plan.candidate_fact_ids):
            raise ValueError("component plan does not expose every current fact")
        anchors = tuple(
            _blind_anchor(row)
            for row in historical_anchors
            if _field(row, "archetype_id") == plan.archetype_id
            and _field(row, "component_id") == plan.component_id
        )
        anchor_by_id = {str(row["anchor_id"]): row for row in anchors}
        if set(anchor_by_id) - set(plan.candidate_anchor_ids):
            raise ValueError("component plan does not expose every matching anchor")
        metric_input = scrub_blind_research_payload(dict(structured_metrics or {}))
        _assert_rows_as_of(source_claims, business_model.as_of_date)
        _assert_rows_as_of(source_documents, business_model.as_of_date)
        coverage_rows = scrub_blind_research_payload(
            [_coverage_payload(row) for row in source_coverage]
        )
        coverage_labels = _coverage_labels(source_coverage)
        citable_facts = tuple(
            row
            for row in facts
            if not row.allowed_component_ids
            or self.component_id in row.allowed_component_ids
        )
        excluded_facts = tuple(
            row
            for row in facts
            if row.allowed_component_ids
            and self.component_id not in row.allowed_component_ids
        )
        fact_projection = project_citable_evidence_facts(citable_facts)
        fact_id_by_row_index = citable_fact_id_by_row_index(fact_projection)
        citable_claim_ids = {
            claim_id for row in citable_facts for claim_id in row.claim_ids
        }
        citable_source_claims = tuple(
            row
            for row in source_claims
            if str(row.get("claim_id") or "") in citable_claim_ids
        )
        excluded_fact_ids = sorted(row.fact_id for row in excluded_facts)
        excluded_source_claim_ids = sorted(
            str(row.get("claim_id") or "")
            for row in source_claims
            if str(row.get("claim_id") or "") not in citable_claim_ids
        )
        payload = scrub_blind_research_payload(
            {
                "researcher_role": self.researcher_role,
                "target_id": plan.target_id,
                "as_of_date": business_model.as_of_date,
                "archetype_id": plan.archetype_id,
                "component_id": plan.component_id,
                "component_max_points": plan.component_max_points,
                "research_plan": plan.to_dict(),
                "target_business_model": business_model.to_dict(),
                "current_evidence_fact_graph": fact_projection["facts"],
                "current_evidence_fact_projection": {
                    key: value
                    for key, value in fact_projection.items()
                    if key != "facts"
                },
                "component_fact_scope_projection": {
                    "input_fact_count": len(facts),
                    "citable_fact_count": len(citable_facts),
                    "non_citable_fact_count": len(excluded_facts),
                    "non_citable_fact_roster_hash": hashlib.sha256(
                        json.dumps(excluded_fact_ids).encode("utf-8")
                    ).hexdigest(),
                    "input_source_claim_count": len(source_claims),
                    "citable_source_claim_count": len(citable_source_claims),
                    "non_citable_source_claim_count": len(
                        excluded_source_claim_ids
                    ),
                    "non_citable_source_claim_roster_hash": hashlib.sha256(
                        json.dumps(excluded_source_claim_ids).encode("utf-8")
                    ).hexdigest(),
                    "every_input_fact_accounted": (
                        len(citable_facts) + len(excluded_facts) == len(facts)
                    ),
                    "every_input_source_claim_accounted": (
                        len(citable_source_claims)
                        + len(excluded_source_claim_ids)
                        == len(source_claims)
                    ),
                    "filter_basis": "PREEXISTING_DETERMINISTIC_ALLOWED_COMPONENT_IDS",
                    "fixed_top_n_used": False,
                    "prompt_projection_is_research_cap": False,
                    "score_authority": False,
                },
                "current_counterfacts": [
                    {
                        "fact_id": row.fact_id,
                        "current_lifecycle": row.current_lifecycle,
                    }
                    for row in citable_facts
                    if row.direction == EvidenceDirection.COUNTER.value
                    and row.current_lifecycle
                    not in {
                        EvidenceLifecycle.RESOLVED.value,
                        EvidenceLifecycle.SUPERSEDED.value,
                    }
                ],
                "historical_component_anchors": list(anchors),
                "source_coverage": coverage_rows,
                "source_claims": project_source_claims(citable_source_claims),
                "source_documents": project_source_document_table(
                    source_documents
                ),
                "structured_metrics": metric_input,
            }
        )
        try:
            response = self.provider.complete(
                pass_name="COMPONENT_RESEARCH", payload=payload
            )
        except (
            StructuredProviderUnavailable,
            StructuredProviderRejected,
            TimeoutError,
            OSError,
            RuntimeError,
        ) as exc:
            return _pending_result(self, "PROVIDER_ERROR", exc)
        prompt_hash = _provider_prompt_hash(self.provider)
        try:
            memo = _component_memo_from_response(
                response=response,
                plan=plan,
                facts=fact_by_id,
                anchors=anchor_by_id,
                coverage_labels=coverage_labels,
                structured_metrics=metric_input,
                fact_id_by_row_index=fact_id_by_row_index,
            )
        except (KeyError, TypeError, ValueError) as exc:
            return _pending_result(
                self,
                "INVALID_PROVIDER_OUTPUT",
                exc,
                prompt_hash=prompt_hash,
            )
        pending = []
        if not memo.research_complete:
            pending.append("RESEARCHER_DECLARED_INCOMPLETE")
        missing_structured = set(plan.structured_metric_requirements) - set(
            memo.structured_metrics
        )
        if missing_structured:
            pending.append(
                "STRUCTURED_METRICS_MISSING:" + ",".join(sorted(missing_structured))
            )
        if memo.research_complete and not memo.source_coverage:
            pending.append("SOURCE_COVERAGE_EMPTY")
        if pending:
            return ComponentResearchResult(
                component_id=self.component_id,
                researcher_role=self.researcher_role,
                status="PENDING",
                memo=memo,
                pending_reasons=tuple(pending),
                provider_name=_provider_name(self.provider),
                prompt_hash=prompt_hash,
            )
        return ComponentResearchResult(
            component_id=self.component_id,
            researcher_role=self.researcher_role,
            status="COMPLETE",
            memo=memo,
            pending_reasons=(),
            provider_name=_provider_name(self.provider),
            prompt_hash=prompt_hash,
        )


class EPSFCFResearcher(ComponentResearcher):
    component_id = "eps_fcf_explosion"
    researcher_role = "EPSFCFResearcher"


class EarningsVisibilityResearcher(ComponentResearcher):
    component_id = "earnings_visibility"
    researcher_role = "EarningsVisibilityResearcher"


class BottleneckPricingResearcher(ComponentResearcher):
    component_id = "bottleneck_pricing"
    researcher_role = "BottleneckPricingResearcher"


class MarketExpectationResearcher(ComponentResearcher):
    component_id = "market_mispricing"
    researcher_role = "MarketExpectationResearcher"


class ValuationResearcher(ComponentResearcher):
    component_id = "valuation_rerating"
    researcher_role = "ValuationResearcher"


class CapitalAllocationResearcher(ComponentResearcher):
    component_id = "capital_allocation"
    researcher_role = "CapitalAllocationResearcher"


class InformationConfidenceResearcher(ComponentResearcher):
    component_id = "information_confidence"
    researcher_role = "InformationConfidenceResearcher"


def build_component_researchers(
    provider: StructuredResearchProvider,
) -> tuple[ComponentResearcher, ...]:
    return (
        EPSFCFResearcher(provider=provider),
        EarningsVisibilityResearcher(provider=provider),
        BottleneckPricingResearcher(provider=provider),
        MarketExpectationResearcher(provider=provider),
        ValuationResearcher(provider=provider),
        CapitalAllocationResearcher(provider=provider),
        InformationConfidenceResearcher(provider=provider),
    )


def _component_memo_from_response(
    *,
    response: Mapping[str, Any],
    plan: ComponentResearchPlan,
    facts: Mapping[str, EvidenceFact],
    anchors: Mapping[str, Mapping[str, Any]],
    coverage_labels: set[str],
    structured_metrics: Mapping[str, Any],
    fact_id_by_row_index: Mapping[int, str],
) -> ComponentResearchMemo:
    if not isinstance(response, Mapping):
        raise TypeError("component researcher response must be an object")
    assert_blind_research_output(response)
    selected = resolve_citable_fact_row_indices(
        response["selected_fact_row_indices"],
        fact_id_by_row_index=fact_id_by_row_index,
        label="selected_fact_row_indices",
    )
    _require_ids_exist(selected, facts, "fact")
    for fact_id in selected:
        allowed = facts[fact_id].allowed_component_ids
        if allowed and plan.component_id not in allowed:
            raise ValueError(
                f"fact is outside deterministic component mechanism scope: {fact_id}"
            )
    resolution = tuple(
        fact_id
        for fact_id in selected
        if facts[fact_id].direction == EvidenceDirection.RESOLUTION.value
        or facts[fact_id].current_lifecycle
        in {
            EvidenceLifecycle.RESOLVED.value,
            EvidenceLifecycle.SUPERSEDED.value,
        }
    )
    positive = tuple(
        fact_id
        for fact_id in selected
        if fact_id not in resolution
        and facts[fact_id].direction == EvidenceDirection.POSITIVE.value
    )
    counter = tuple(
        fact_id
        for fact_id in selected
        if fact_id not in resolution
        and facts[fact_id].direction == EvidenceDirection.COUNTER.value
    )
    context = tuple(
        fact_id
        for fact_id in selected
        if fact_id not in {*positive, *counter, *resolution}
    )
    historical = _ids(response, "historical_anchor_ids")
    nearest_positive = _ids(response, "nearest_positive_anchor_ids")
    nearest_counter = _ids(response, "nearest_counter_anchor_ids")
    _require_ids_exist(
        (*historical, *nearest_positive, *nearest_counter), anchors, "anchor"
    )
    if not set((*nearest_positive, *nearest_counter)).issubset(historical):
        raise ValueError("nearest anchors must also be historical_anchor_ids")
    for anchor_id in nearest_positive:
        if str(anchors[anchor_id].get("role")) != "POSITIVE":
            raise ValueError("nearest positive anchor has the wrong role")
    for anchor_id in nearest_counter:
        if str(anchors[anchor_id].get("role")) != "COUNTER":
            raise ValueError("nearest counter anchor has the wrong role")
    returned_metric_ids = _ids(response, "structured_metric_ids")
    unknown_metrics = set(returned_metric_ids) - set(structured_metrics)
    if unknown_metrics:
        raise ValueError(f"researcher invented structured metrics: {sorted(unknown_metrics)}")
    returned_metrics = {
        key: structured_metrics[key]
        for key in returned_metric_ids
    }
    coverage = _ids(response, "source_coverage")
    if set(coverage) - coverage_labels:
        raise ValueError("researcher cited source coverage not present in input")
    payload = {
        "plan_id": plan.plan_id,
        "response": scrub_blind_research_payload(response),
        "resolved_positive_fact_ids": positive,
        "resolved_counter_fact_ids": counter,
        "resolved_resolution_fact_ids": resolution,
        "resolved_context_fact_ids": context,
        "resolved_structured_metrics": returned_metrics,
    }
    return ComponentResearchMemo(
        memo_id=stable_intelligence_id("CRMEMO", payload),
        target_id=plan.target_id,
        archetype_id=plan.archetype_id,
        component_id=plan.component_id,
        component_max_points=plan.component_max_points,
        positive_fact_ids=positive,
        counter_fact_ids=counter,
        resolution_fact_ids=resolution,
        context_fact_ids=context,
        structured_metrics=dict(returned_metrics),
        historical_anchor_ids=historical,
        researcher_summary=str(response["researcher_summary"]),
        positive_case=str(response["positive_case"]),
        counter_case=str(response["counter_case"]),
        uncertainties=_ids(response, "uncertainties"),
        source_coverage=coverage,
        proposed_score_lower=float(response["proposed_score_lower"]),
        proposed_score_mid=float(response["proposed_score_mid"]),
        proposed_score_upper=float(response["proposed_score_upper"]),
        confidence=float(response["confidence"]),
        research_complete=bool(response["research_complete"]),
        nearest_positive_anchor_ids=nearest_positive,
        nearest_counter_anchor_ids=nearest_counter,
        why_not_higher=str(response["why_not_higher"]),
        why_not_lower=str(response["why_not_lower"]),
        researcher_role=plan.researcher_role,
    )


def _coerce_fact(row: EvidenceFact | Mapping[str, Any]) -> EvidenceFact:
    if isinstance(row, EvidenceFact):
        return row
    fields = EvidenceFact.__dataclass_fields__
    payload = {key: row[key] for key in fields if key in row}
    for key in (
        "source_ids",
        "claim_ids",
        "quote_ids",
        "corroborating_independence_groups",
        "question_family_tags",
        "primitive_tags",
        "allowed_component_ids",
        "structured_evidence_roles",
    ):
        if key in payload:
            payload[key] = tuple(payload[key] or ())
    return EvidenceFact(**payload)


def _validate_current_facts(
    facts: Sequence[EvidenceFact], target_id: str, as_of_date: str
) -> None:
    ids = [row.fact_id for row in facts]
    if len(ids) != len(set(ids)):
        raise ValueError("EvidenceFact ids must be unique")
    for row in facts:
        if row.target_id != target_id:
            raise ValueError("cross-target EvidenceFact exposure is forbidden")
        if row.as_of_date != as_of_date:
            raise ValueError("EvidenceFact as_of_date must match the research run")


def _blind_anchor(row: ComponentAnchor | Mapping[str, Any]) -> Mapping[str, Any]:
    if isinstance(row, ComponentAnchor):
        value = row.to_dict()
    else:
        value = dict(row)
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
    return scrub_blind_research_payload(
        {key: value[key] for key in allowed if key in value}
    )


def _assert_rows_as_of(rows: Sequence[Mapping[str, Any]], as_of_date: str) -> None:
    cutoff = date.fromisoformat(as_of_date)
    for row in rows:
        raw = next(
            (
                str(row.get(key)).strip()
                for key in (
                    "published_at",
                    "publication_date",
                    "filed_at",
                    "observed_at",
                )
                if row.get(key)
            ),
            "",
        )
        if not raw:
            continue
        try:
            observed = date.fromisoformat(raw[:10])
        except ValueError as exc:
            raise ValueError(f"invalid source date: {raw}") from exc
        if observed > cutoff:
            raise ValueError(
                f"future source exposure is forbidden: {observed.isoformat()} > {as_of_date}"
            )


def _coverage_payload(row: str | Mapping[str, Any]) -> Any:
    return row if isinstance(row, str) else dict(row)


def _coverage_labels(rows: Sequence[str | Mapping[str, Any]]) -> set[str]:
    labels = set()
    for row in rows:
        if isinstance(row, str):
            label = row
        else:
            label = str(
                row.get("coverage_id")
                or row.get("source_family")
                or row.get("route_id")
                or ""
            )
        if label.strip():
            labels.add(label.strip())
    return labels


def _ids(response: Mapping[str, Any], key: str) -> tuple[str, ...]:
    value = response[key]
    if isinstance(value, str) or not isinstance(value, Sequence):
        raise TypeError(f"{key} must be an array")
    result = tuple(str(item).strip() for item in value)
    if any(not item for item in result) or len(result) != len(set(result)):
        raise ValueError(f"{key} must contain unique nonempty ids")
    return result


def _require_ids_exist(
    ids: Sequence[str], rows: Mapping[str, Any], lineage_name: str
) -> None:
    missing = set(ids) - set(rows)
    if missing:
        raise ValueError(
            f"researcher cited unknown {lineage_name} ids: {sorted(missing)}"
        )


def _field(row: Any, key: str) -> Any:
    return row.get(key) if isinstance(row, Mapping) else getattr(row, key)


def _provider_name(provider: StructuredResearchProvider) -> str:
    return str(getattr(provider, "provider_name", provider.__class__.__name__))


def _provider_prompt_hash(provider: StructuredResearchProvider) -> str | None:
    calls = getattr(provider, "calls", ())
    if calls and isinstance(calls[-1], Mapping):
        value = calls[-1].get("prompt_hash")
        return str(value) if value else None
    return None


def _pending_result(
    researcher: ComponentResearcher,
    code: str,
    error: Exception,
    *,
    prompt_hash: str | None = None,
) -> ComponentResearchResult:
    detail = " ".join(str(error).split())[-500:] or error.__class__.__name__
    return ComponentResearchResult(
        component_id=researcher.component_id,
        researcher_role=researcher.researcher_role,
        status="PENDING",
        memo=None,
        pending_reasons=(f"{code}:{detail}",),
        provider_name=_provider_name(researcher.provider),
        prompt_hash=prompt_hash,
    )


def _pass_instruction(pass_name: str) -> str:
    if pass_name == "BUSINESS_MODEL_RESEARCH":
        return "Explain how revenue, cost, cash conversion, capacity, and customer dependencies work before component scoring."
    if pass_name == "COMPONENT_RESEARCH":
        return (
            "Write one component memo with a bounded point range, nearest "
            "positive/counter anchors, both-side reasoning, and explicit uncertainty. "
            "Return structured_metric_ids as the identifiers of supplied "
            "structured_metrics used in the memo; never copy, alter, or invent their values."
        )
    if pass_name == "RED_TEAM_RESEARCH":
        return "Challenge every material thesis independently, distinguish current counters from resolved history, and identify new research directions."
    if pass_name == "SYNTHESIS_REVIEW":
        return "Synthesize cross-component support and tension without calculating total points or Stage."
    if pass_name == "SOURCE_QUERY_GENERATION":
        return (
            "Generate literal target-scoped discovery queries from the current facts, "
            "missing information, source failures, and open objectives. Do not reuse an "
            "executed query and do not supply a deterministic fallback template."
        )
    if pass_name == "SOURCE_CANDIDATE_RANKING":
        return (
            "Assess every discovery candidate for material relevance to the supplied "
            "research objectives. Snippets are discovery metadata only, never evidence."
        )
    if pass_name == "EVIDENCE_FACT_EXTRACTION":
        return (
            "Extract every material economic fact and counterfact from the supplied full "
            "documents. Cite an exact quote that occurs in the cited document, keep issuer, "
            "business segment, product, period, direction, and lifecycle explicit, and account "
            "for every document with one disposition. Tag SEGMENT_CONTRIBUTION, QOQ_GROWTH, "
            "or FORWARD_GUIDANCE only when the exact quote and value explicitly establish that "
            "structured role; keep value as only the reported numeric point/range, unit separately, "
            "and the time horizon in period. Otherwise return an empty structured_evidence_roles array. Tags "
            "are extraction context only and never assign points. Read prior fact-extraction retry "
            "context and correct the cited disposition/schema failure: FACTS_EXTRACTED is valid only "
            "when that same document has at least one accepted fact proposal; otherwise use the "
            "accurate non-fact disposition. Never "
            "infer absence from silence. Copy exact_quote as a literal contiguous substring of "
            "content_text without paraphrasing, punctuation edits, or whitespace normalization. "
            "Never use snippets, future outcomes, score, or Stage."
        )
    if pass_name == "RESEARCH_SUPERVISOR_REVIEW":
        return (
            "Review every component memo, fact gap, structured-data gap, prior query/source "
            "failure, and counter route. Prior failures may be loss-accounted semantic groups; "
            "classify each group failure_id exactly once and apply it to all member_failure_ids. "
            "Classify parser/extractor failure separately from "
            "source absence. Suggest semantic source/query directions; do not write literal "
            "fallback query templates and never treat zero results or a budget limit as completion."
        )
    if pass_name == "SEMANTIC_SATURATION_REVIEW":
        return (
            "Independently decide whether any reasonable material-positive, counter, "
            "supersession, structured-data, or new-source-family route remains. Zero search "
            "results and transport limits are never saturation proof."
        )
    if pass_name == "CLAIM_COMPONENT_IMPACT_MAPPING":
        return (
            "Map each primary current EvidenceFact claim to every component whose distinct "
            "economic mechanism it supports or counters. Use component mechanism ids from "
            "the supplied contract. Explicitly dispose of every other primary material claim; "
            "question-family and primitive tags are context only, never score gateways. Credit "
            "units express duplicate-credit accounting, not component points or stage authority."
        )
    if pass_name == "STRUCTURED_PEER_SELECTION":
        return (
            "Select two to five Korean-listed economic peers for structured valuation. "
            "Use the supplied current business facts to match revenue model, cyclicality, "
            "capital intensity, customer structure, and cash economics. Return the exact "
            "six-digit listing symbol and company name so deterministic code can verify the "
            "identity and fetch point-in-time structured multiples. Do not select by sector "
            "label alone, do not invent valuation values, queries, scores, or Stage, and make "
            "material differences explicit."
        )
    if pass_name == "COMPONENT_ANALYST_JUDGE":
        return (
            "Act as the independent positive analyst for exactly one broad component. "
            "Derive proposed component points and an allowed range from current support facts, "
            "economic strength, duration, and cash conversion. Account for every supplied "
            "positive component fact and compare the case with at least one nearest blind "
            "historical anchor. Explain both why the score is not higher and why it is not lower."
        )
    if pass_name == "COMPONENT_SKEPTIC_JUDGE":
        return (
            "Act as the independent skeptic for exactly one broad component. Review every "
            "supplied counterfact and explicitly reflect business phase, valuation, customer "
            "or supplier concentration, and uncertainty in proposed component points and the "
            "allowed range. Compare with a nearest blind anchor and explain both bounds."
        )
    return (
        "Act as the independent calibration judge for exactly one broad component. Compare "
        "the current support and counter fact shape with usable blind historical anchors, "
        "validate the component point scale and allowed range, and explain why the proposal "
        "is neither above nor below the selected anchor-calibrated band."
    )


__all__ = [
    "BUSINESS_MODEL_RESEARCH_SCHEMA",
    "BottleneckPricingResearcher",
    "CapitalAllocationResearcher",
    "CodexResearcherProvider",
    "COMPONENT_JUDGE_SCHEMA",
    "COMPONENT_RESEARCH_SCHEMA",
    "ComponentResearchResult",
    "ComponentResearcher",
    "EPSFCFResearcher",
    "EarningsVisibilityResearcher",
    "InformationConfidenceResearcher",
    "MarketExpectationResearcher",
    "RED_TEAM_RESEARCH_SCHEMA",
    "SOURCE_CANDIDATE_RANKING_SCHEMA",
    "SOURCE_QUERY_GENERATION_SCHEMA",
    "RESEARCH_SUPERVISOR_SCHEMA",
    "SEMANTIC_SATURATION_REVIEW_SCHEMA",
    "CLAIM_COMPONENT_IMPACT_MAPPING_SCHEMA",
    "SYNTHESIS_REVIEW_SCHEMA",
    "StructuredResearchProvider",
    "STRUCTURED_PEER_SELECTION_SCHEMA",
    "ValuationResearcher",
    "build_component_researchers",
]
