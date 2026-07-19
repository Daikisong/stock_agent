"""Provider-backed component researchers for canonical E2R v5 Researcher Mode."""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any, Mapping, Protocol, Sequence

from e2r.research_brain.intelligence_schema import stable_intelligence_id
from e2r.research_brain.planning.provider_transport import (
    CodexStructuredProviderTransport,
    OllamaStructuredProviderTransport,
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
    project_current_decision_citable_facts,
    project_research_source_claim_profile,
    project_research_source_document_profile,
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

FACT_EXTRACTION_PAGE_FACT_LIMIT = 12

_PRIOR_FACT_DISPOSITION_ARRAY: Mapping[str, Any] = {
    "type": "array",
    "items": {
        "type": "object",
        "additionalProperties": False,
        "required": ["fact_row_index", "disposition", "reason"],
        "properties": {
            "fact_row_index": {"type": "integer", "minimum": 0},
            "disposition": {"type": "string", "enum": ["RETAIN", "OMIT"]},
            "reason": {"type": "string", "minLength": 1},
        },
    },
}

_SELECTED_FACT_GROUNDING_ARRAY: Mapping[str, Any] = {
    "type": "array",
    "items": {
        "type": "object",
        "additionalProperties": False,
        "required": [
            "fact_row_index",
            "source_predicate",
            "source_value_json",
            "source_period_json",
            "source_economic_mechanism",
            "component_interpretation",
        ],
        "properties": {
            "fact_row_index": {"type": "integer", "minimum": 0},
            "source_predicate": {"type": "string", "minLength": 1},
            "source_value_json": {"type": "string", "minLength": 1},
            "source_period_json": {"type": "string", "minLength": 1},
            "source_economic_mechanism": {
                "type": "string",
                "minLength": 1,
            },
            "component_interpretation": {"type": "string", "minLength": 1},
        },
    },
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
        "selected_fact_groundings",
        "prior_fact_dispositions",
        "structured_metric_row_indices",
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
        "selected_fact_groundings": _SELECTED_FACT_GROUNDING_ARRAY,
        "prior_fact_dispositions": _PRIOR_FACT_DISPOSITION_ARRAY,
        "structured_metric_row_indices": _NONNEGATIVE_INTEGER_ARRAY,
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
            "maxItems": FACT_EXTRACTION_PAGE_FACT_LIMIT,
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

STAGE_GATE_FACT_MAPPING_SCHEMA: Mapping[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": [
        "mappings",
        "unresolved_material_questions",
        "mapping_complete",
    ],
    "properties": {
        "mappings": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": [
                    "primitive_id",
                    "direction",
                    "claim_ids",
                    "semantic_rationale",
                ],
                "properties": {
                    "primitive_id": {"type": "string", "minLength": 1},
                    "direction": {
                        "type": "string",
                        "enum": ["SUPPORT", "COUNTER"],
                    },
                    "claim_ids": {**_STRING_ARRAY, "minItems": 1},
                    "semantic_rationale": {"type": "string", "minLength": 1},
                },
            },
        },
        "unresolved_material_questions": _STRING_ARRAY,
        "mapping_complete": {"type": "boolean"},
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
    "STAGE_GATE_FACT_MAPPING": STAGE_GATE_FACT_MAPPING_SCHEMA,
    "STRUCTURED_PEER_SELECTION": STRUCTURED_PEER_SELECTION_SCHEMA,
}

_CODEX_PROMPT_TRANSPORT_MAX_CHARS = 1_000_000
_RESEARCH_PROVIDER_RESPONSE_CACHE_SCHEMA_VERSION = (
    "e2r_v5_research_provider_response_cache_v1"
)
_PROVIDER_USAGE_LIMIT_RE = re.compile(r"\busage\s+limit\b", re.IGNORECASE)
_PROVIDER_USAGE_LIMIT_RESET_RE = re.compile(
    r"try\s+again\s+at\s+"
    r"([A-Z][a-z]{2}\s+\d{1,2}(?:st|nd|rd|th),\s+\d{4}\s+"
    r"\d{1,2}:\d{2}\s+(?:AM|PM))",
    re.IGNORECASE,
)


@dataclass
class CodexResearcherProvider:
    """Default structured Codex provider for open-ended research judgments."""

    transport: CodexStructuredProviderTransport
    provider_name: str = "CODEX_STRUCTURED_RESEARCHER_MODE"
    calls: list[Mapping[str, Any]] = field(default_factory=list)
    response_cache_directory: Path | None = None
    cache_invalidations: list[Mapping[str, Any]] = field(default_factory=list)
    _response_cache_call_start_index: int = 0
    _response_cache_invalidation_start_index: int = 0
    _terminal_provider_error: str | None = field(default=None, init=False)
    _terminal_provider_reset_hint: str | None = field(default=None, init=False)

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
                "Decode current_evidence_fact_graph rows with current_evidence_fact_projection.fact_fields and fact_value_dictionaries when dictionary indices are present. If source_claims contains a claims table, decode it with claim_fields; if it is a loss-accounted profile, review every semantic group and use the complete current/open citable fact rows for claim meaning. Resolved and superseded history is hash-accounted context and cannot drive a current score.",
                "When the schema asks for fact_row_indices, return only exact non-negative fact_row_index values from those rows; deterministic code resolves immutable fact ids.",
                "Cite only ids present in the input. Do not invent facts, sources, metrics, or anchors.",
                "Never output a total score, canonical Stage, investment recommendation, MFE/MAE, or any future outcome.",
                instruction,
                "Return exactly one JSON object matching the supplied schema.",
                json.dumps(safe_payload, ensure_ascii=False, sort_keys=True),
            )
        )
        prompt_hash = hashlib.sha256(prompt.encode("utf-8")).hexdigest()
        schema_hash = _canonical_json_hash(_PROVIDER_SCHEMAS[pass_name])
        try:
            provider_identity = self._provider_identity()
        except (
            StructuredProviderUnavailable,
            StructuredProviderRejected,
            TimeoutError,
            OSError,
            RuntimeError,
        ) as exc:
            detail = _provider_error_detail(exc)
            self.calls.append(
                {
                    "pass_name": pass_name,
                    "prompt_hash": prompt_hash,
                    "prompt_chars": len(prompt),
                    "payload": safe_payload,
                    "response": None,
                    "status": "PROVIDER_ERROR",
                    "provider_error": f"{exc.__class__.__name__}:{detail}",
                    "provider_failure_class": "IDENTITY_RESOLUTION",
                    "transport_call_attempted": True,
                    "cache_hit": False,
                    "cache_key": None,
                    "cache_read_status": "NOT_ATTEMPTED",
                    "cache_write_status": "NOT_WRITTEN",
                    "output_schema_hash": schema_hash,
                }
            )
            raise
        cache_key = _canonical_json_hash(
            {
                "cache_schema_version": (
                    _RESEARCH_PROVIDER_RESPONSE_CACHE_SCHEMA_VERSION
                ),
                "provider_name": self.provider_name,
                "provider_identity": provider_identity,
                "pass_name": pass_name,
                "prompt_hash": prompt_hash,
                "output_schema_hash": schema_hash,
            }
        )
        if len(prompt) > _CODEX_PROMPT_TRANSPORT_MAX_CHARS:
            self.calls.append(
                {
                    "pass_name": pass_name,
                    "prompt_hash": prompt_hash,
                    "prompt_chars": len(prompt),
                    "payload": safe_payload,
                    "response": None,
                    "status": "PROMPT_TRANSPORT_REJECTED",
                    "transport_call_attempted": False,
                    "cache_hit": False,
                    "cache_key": cache_key,
                    "cache_read_status": "NOT_ATTEMPTED",
                    "output_schema_hash": schema_hash,
                }
            )
            raise StructuredProviderRejected(
                f"prompt_transport_too_large:{len(prompt)}:"
                f"max={_CODEX_PROMPT_TRANSPORT_MAX_CHARS}"
            )
        cached_response, cache_read_status = self._read_cached_response(
            cache_key=cache_key,
            pass_name=pass_name,
            prompt_hash=prompt_hash,
            schema_hash=schema_hash,
        )
        if cached_response is not None:
            assert_blind_research_output(cached_response)
            self.calls.append(
                {
                    "pass_name": pass_name,
                    "prompt_hash": prompt_hash,
                    "prompt_chars": len(prompt),
                    "payload": safe_payload,
                    "response": dict(cached_response),
                    "status": "COMPLETE",
                    "transport_call_attempted": False,
                    "cache_hit": True,
                    "cache_key": cache_key,
                    "cache_read_status": cache_read_status,
                    "output_schema_hash": schema_hash,
                }
            )
            return cached_response
        if self._terminal_provider_error is not None:
            circuit_error = (
                "PROVIDER_USAGE_LIMIT_CIRCUIT_OPEN:"
                f"{self._terminal_provider_error}"
            )
            self.calls.append(
                {
                    "pass_name": pass_name,
                    "prompt_hash": prompt_hash,
                    "prompt_chars": len(prompt),
                    "payload": safe_payload,
                    "response": None,
                    "status": "PROVIDER_ERROR",
                    "provider_error": circuit_error,
                    "provider_failure_class": "USAGE_LIMIT",
                    "provider_reset_hint": self._terminal_provider_reset_hint,
                    "usage_limit_circuit_open": True,
                    "transport_call_attempted": False,
                    "cache_hit": False,
                    "cache_key": cache_key,
                    "cache_read_status": cache_read_status,
                    "cache_write_status": "NOT_WRITTEN",
                    "output_schema_hash": schema_hash,
                }
            )
            raise StructuredProviderUnavailable(circuit_error)
        try:
            response = self.transport.complete(
                prompt=prompt,
                output_schema=_PROVIDER_SCHEMAS[pass_name],
                schema_name=f"e2r_v5_{pass_name.lower()}",
            )
        except (
            StructuredProviderUnavailable,
            StructuredProviderRejected,
            TimeoutError,
            OSError,
            RuntimeError,
        ) as exc:
            detail = _provider_error_detail(exc)
            usage_limit = bool(_PROVIDER_USAGE_LIMIT_RE.search(detail))
            reset_hint = _provider_usage_limit_reset_hint(detail)
            if usage_limit:
                self._terminal_provider_error = detail
                self._terminal_provider_reset_hint = reset_hint
            self.calls.append(
                {
                    "pass_name": pass_name,
                    "prompt_hash": prompt_hash,
                    "prompt_chars": len(prompt),
                    "payload": safe_payload,
                    "response": None,
                    "status": "PROVIDER_ERROR",
                    "provider_error": f"{exc.__class__.__name__}:{detail}",
                    "provider_failure_class": (
                        "USAGE_LIMIT" if usage_limit else "OTHER"
                    ),
                    "provider_reset_hint": reset_hint,
                    "usage_limit_circuit_open": usage_limit,
                    "transport_call_attempted": True,
                    "cache_hit": False,
                    "cache_key": cache_key,
                    "cache_read_status": cache_read_status,
                    "cache_write_status": "NOT_WRITTEN",
                    "output_schema_hash": schema_hash,
                }
            )
            raise
        try:
            assert_blind_research_output(response.payload)
        except (TypeError, ValueError) as exc:
            detail = _provider_error_detail(exc)
            self.calls.append(
                {
                    "pass_name": pass_name,
                    "prompt_hash": prompt_hash,
                    "prompt_chars": len(prompt),
                    "payload": safe_payload,
                    "response": None,
                    "response_hash": _canonical_json_hash(response.payload),
                    "status": "PROVIDER_OUTPUT_REJECTED",
                    "provider_error": f"{exc.__class__.__name__}:{detail}",
                    "provider_failure_class": "BLIND_OUTPUT_REJECTED",
                    "transport_call_attempted": True,
                    "cache_hit": False,
                    "cache_key": cache_key,
                    "cache_read_status": cache_read_status,
                    "cache_write_status": "NOT_WRITTEN",
                    "output_schema_hash": schema_hash,
                }
            )
            raise StructuredProviderRejected(
                f"blind_output_rejected:{detail}"
            ) from exc
        cache_write_status = self._write_cached_response(
            cache_key=cache_key,
            pass_name=pass_name,
            prompt_hash=prompt_hash,
            schema_hash=schema_hash,
            response=response.payload,
        )
        self.calls.append(
            {
                "pass_name": pass_name,
                "prompt_hash": prompt_hash,
                "prompt_chars": len(prompt),
                "payload": safe_payload,
                "response": dict(response.payload),
                "status": "COMPLETE",
                "transport_call_attempted": True,
                "cache_hit": False,
                "cache_key": cache_key,
                "cache_read_status": cache_read_status,
                "cache_write_status": cache_write_status,
                "output_schema_hash": schema_hash,
            }
        )
        return response.payload

    def configure_response_cache(self, directory: str | Path) -> None:
        """Bind one target checkpoint cache without weakening prompt validation."""

        cache_root = Path(directory)
        cache_root.mkdir(parents=True, exist_ok=True)
        self.response_cache_directory = cache_root
        self._response_cache_call_start_index = len(self.calls)
        self._response_cache_invalidation_start_index = len(
            self.cache_invalidations
        )

    def invalidate_last_response_cache(self, reason: str) -> Mapping[str, Any]:
        """Evict only the last response after downstream semantic rejection.

        Transport/schema success is not enough to make a response reusable.  A
        component parser can still reject cross-field relations that JSON Schema
        cannot express, such as nearest anchors being a subset of cited anchors.
        """

        clean_reason = " ".join(str(reason).split())[-500:] or "unknown reason"
        latest = self.calls[-1] if self.calls else None
        event: dict[str, Any] = {
            "reason": clean_reason,
            "pass_name": None,
            "prompt_hash": None,
            "cache_key": None,
            "cache_entry_existed": False,
            "cache_entry_deleted": False,
            "status": "NO_ELIGIBLE_RESPONSE",
        }
        if not isinstance(latest, Mapping) or latest.get("status") != "COMPLETE":
            self.cache_invalidations.append(event)
            return dict(event)
        pass_name = str(latest.get("pass_name") or "")
        cache_key = str(latest.get("cache_key") or "")
        event.update(
            {
                "pass_name": pass_name or None,
                "prompt_hash": latest.get("prompt_hash"),
                "cache_key": cache_key or None,
            }
        )
        if not pass_name or not cache_key:
            self.cache_invalidations.append(event)
            return dict(event)
        path = self._cache_path(pass_name=pass_name, cache_key=cache_key)
        if path is None:
            event["status"] = "CACHE_DISABLED"
            self.cache_invalidations.append(event)
            return dict(event)
        try:
            existed = path.is_file()
            event["cache_entry_existed"] = existed
            path.unlink(missing_ok=True)
            event["cache_entry_deleted"] = existed and not path.exists()
            event["status"] = (
                "INVALID_RESPONSE_CACHE_DELETED"
                if event["cache_entry_deleted"]
                else "CACHE_ENTRY_ALREADY_ABSENT"
            )
        except OSError as exc:
            event["status"] = "CACHE_DELETE_FAILED"
            event["delete_error"] = (
                f"{exc.__class__.__name__}:"
                + (" ".join(str(exc).split())[-500:] or "no detail")
            )
        self.cache_invalidations.append(event)
        return dict(event)

    def response_cache_audit(self) -> Mapping[str, Any]:
        events = tuple(self.calls[self._response_cache_call_start_index :])
        cache_events = tuple(row for row in events if row.get("cache_key"))
        invalidations = tuple(
            self.cache_invalidations[
                self._response_cache_invalidation_start_index :
            ]
        )
        cache_root = self.response_cache_directory
        return {
            "schema_version": (
                "e2r_v5_research_provider_response_cache_audit_v2"
            ),
            "status": (
                "RESEARCH_PROVIDER_RESPONSE_CACHE_ACTIVE"
                if cache_root is not None
                else "RESEARCH_PROVIDER_RESPONSE_CACHE_DISABLED"
            ),
            "provider_name": self.provider_name,
            "cache_directory": str(cache_root) if cache_root is not None else None,
            "logical_call_count": len(events),
            "successful_call_count": sum(
                row.get("status") == "COMPLETE" for row in events
            ),
            "provider_error_count": sum(
                row.get("status") == "PROVIDER_ERROR" for row in events
            ),
            "provider_output_rejected_count": sum(
                row.get("status") == "PROVIDER_OUTPUT_REJECTED"
                for row in events
            ),
            "prompt_transport_rejected_count": sum(
                row.get("status") == "PROMPT_TRANSPORT_REJECTED"
                for row in events
            ),
            "transport_call_count": sum(
                (
                    bool(row.get("transport_call_attempted"))
                    if "transport_call_attempted" in row
                    else (
                        not bool(row.get("cache_hit"))
                        and row.get("status") != "PROMPT_TRANSPORT_REJECTED"
                    )
                )
                for row in cache_events
            ),
            "provider_usage_limit_detected": any(
                row.get("provider_failure_class") == "USAGE_LIMIT"
                for row in events
            ),
            "provider_usage_limit_reset_hints": list(
                dict.fromkeys(
                    str(row.get("provider_reset_hint"))
                    for row in events
                    if str(row.get("provider_reset_hint") or "").strip()
                )
            ),
            "provider_usage_limit_transport_error_count": sum(
                row.get("provider_failure_class") == "USAGE_LIMIT"
                and row.get("transport_call_attempted") is True
                for row in events
            ),
            "provider_usage_limit_short_circuit_count": sum(
                row.get("provider_failure_class") == "USAGE_LIMIT"
                and row.get("transport_call_attempted") is False
                for row in events
            ),
            "cache_hit_count": sum(
                bool(row.get("cache_hit")) for row in cache_events
            ),
            "cache_invalid_or_unreadable_count": sum(
                row.get("cache_read_status") == "INVALID_OR_UNREADABLE"
                for row in cache_events
            ),
            "downstream_semantic_invalidation_count": len(invalidations),
            "downstream_semantic_cache_delete_count": sum(
                row.get("status") == "INVALID_RESPONSE_CACHE_DELETED"
                for row in invalidations
            ),
            "downstream_semantic_cache_delete_failure_count": sum(
                row.get("status") == "CACHE_DELETE_FAILED"
                for row in invalidations
            ),
            "downstream_semantic_invalidations": [
                dict(row) for row in invalidations
            ],
            "cache_entry_count": (
                self._matching_cache_entry_count()
                if cache_root is not None
                else 0
            ),
            "prompt_and_schema_hash_required": True,
            "provider_identity_hash_required": True,
            "failed_provider_response_cached": False,
        }

    def _matching_cache_entry_count(self) -> int:
        cache_root = self.response_cache_directory
        if cache_root is None:
            return 0
        try:
            identity = self._provider_identity()
        except (
            StructuredProviderUnavailable,
            StructuredProviderRejected,
            TimeoutError,
            OSError,
            RuntimeError,
        ):
            return 0
        count = 0
        for path in cache_root.glob("*.json"):
            try:
                row = json.loads(path.read_text(encoding="utf-8"))
            except (
                OSError,
                UnicodeError,
                json.JSONDecodeError,
                TypeError,
                ValueError,
            ):
                continue
            if (
                isinstance(row, Mapping)
                and row.get("provider_name") == self.provider_name
                and row.get("provider_identity") == identity
            ):
                count += 1
        return count

    def _provider_identity(self) -> Mapping[str, Any]:
        identity = getattr(self.transport, "provider_identity", None)
        if callable(identity):
            return dict(identity())
        return {
            "transport_class": self.transport.__class__.__qualname__,
            "codex_command": getattr(self.transport, "codex_command", None),
            "model": getattr(self.transport, "model", None),
            "profile": getattr(self.transport, "profile", None),
            "extra_args": list(getattr(self.transport, "extra_args", ()) or ()),
        }

    def _cache_path(self, *, pass_name: str, cache_key: str) -> Path | None:
        if self.response_cache_directory is None:
            return None
        return self.response_cache_directory / (
            f"{pass_name.lower()}-{cache_key}.json"
        )

    def _read_cached_response(
        self,
        *,
        cache_key: str,
        pass_name: str,
        prompt_hash: str,
        schema_hash: str,
    ) -> tuple[Mapping[str, Any] | None, str]:
        path = self._cache_path(pass_name=pass_name, cache_key=cache_key)
        if path is None:
            return None, "DISABLED"
        if not path.is_file():
            return None, "MISS"
        try:
            cached = json.loads(path.read_text(encoding="utf-8"))
            if not isinstance(cached, Mapping):
                raise ValueError("cache entry must be an object")
            response = cached.get("response")
            if not isinstance(response, Mapping):
                raise ValueError("cache response must be an object")
            expected = {
                "schema_version": (
                    _RESEARCH_PROVIDER_RESPONSE_CACHE_SCHEMA_VERSION
                ),
                "cache_key": cache_key,
                "provider_name": self.provider_name,
                "provider_identity": self._provider_identity(),
                "pass_name": pass_name,
                "prompt_hash": prompt_hash,
                "output_schema_hash": schema_hash,
            }
            if any(cached.get(key) != value for key, value in expected.items()):
                raise ValueError("cache identity or input hash mismatch")
            if cached.get("response_hash") != _canonical_json_hash(response):
                raise ValueError("cache response hash mismatch")
            assert_blind_research_output(response)
        except (OSError, UnicodeError, json.JSONDecodeError, TypeError, ValueError):
            return None, "INVALID_OR_UNREADABLE"
        return dict(response), "HIT"

    def _write_cached_response(
        self,
        *,
        cache_key: str,
        pass_name: str,
        prompt_hash: str,
        schema_hash: str,
        response: Mapping[str, Any],
    ) -> str:
        path = self._cache_path(pass_name=pass_name, cache_key=cache_key)
        if path is None:
            return "DISABLED"
        value = {
            "schema_version": _RESEARCH_PROVIDER_RESPONSE_CACHE_SCHEMA_VERSION,
            "cache_key": cache_key,
            "provider_name": self.provider_name,
            "provider_identity": self._provider_identity(),
            "pass_name": pass_name,
            "prompt_hash": prompt_hash,
            "output_schema_hash": schema_hash,
            "response_hash": _canonical_json_hash(response),
            "response": dict(response),
        }
        temporary = path.with_suffix(path.suffix + ".tmp")
        try:
            temporary.write_text(
                json.dumps(
                    value,
                    ensure_ascii=False,
                    sort_keys=True,
                    indent=2,
                )
                + "\n",
                encoding="utf-8",
            )
            temporary.replace(path)
        except (OSError, UnicodeError, TypeError, ValueError):
            try:
                temporary.unlink(missing_ok=True)
            except OSError:
                pass
            return "WRITE_FAILED"
        return "WRITTEN"


@dataclass
class OllamaResearcherProvider(CodexResearcherProvider):
    """Explicit Ollama-backed Researcher Mode provider with identical gates."""

    transport: OllamaStructuredProviderTransport
    provider_name: str = "OLLAMA_STRUCTURED_RESEARCHER_MODE"
    fact_document_chunk_chars: int = 100_000

    def __post_init__(self) -> None:
        if (
            isinstance(self.fact_document_chunk_chars, bool)
            or self.fact_document_chunk_chars < 10_000
        ):
            raise ValueError(
                "Ollama fact document chunk size must be at least 10000"
            )

    def _provider_identity(self) -> Mapping[str, Any]:
        return {
            **super()._provider_identity(),
            "fact_document_chunk_chars": self.fact_document_chunk_chars,
            "effective_semantic_prompt_chunk_chars": (
                self.semantic_prompt_chunk_chars
            ),
        }

    @property
    def semantic_prompt_chunk_chars(self) -> int:
        """Lossless chunk target bounded by both context and output reserve.

        A source can fit in the context window yet still require more JSON
        tokens than ``num_predict`` permits.  Fact extraction is especially
        expansion-heavy because every quote carries scope and lineage fields.
        Keep each literal source chunk small enough for the configured output
        reserve; deterministic overlap accounting still covers the entire
        canonical document.
        """

        return min(
            self.fact_document_chunk_chars,
            max(
                10_000,
                (
                    int(getattr(self.transport, "context_length", 262_144))
                    - int(
                        getattr(
                            self.transport,
                            "max_output_tokens",
                            32_768,
                        )
                    )
                )
                // 2,
            ),
            max(
                10_000,
                int(
                    getattr(
                        self.transport,
                        "max_output_tokens",
                        32_768,
                    )
                )
                * 3
                // 10,
            ),
        )

    def complete(
        self, *, pass_name: str, payload: Mapping[str, Any]
    ) -> Mapping[str, Any]:
        """Review an oversized citable fact plane through exhaustive chunks.

        A long-running backfill can leave thousands of CURRENT/OPEN facts.  A
        single JSON prompt that repeats every decoded economic mechanism can
        exceed the model context even when the canonical artifacts themselves
        are valid.  Silently raising the character cap would let the model
        truncate the beginning of the prompt.  For the three memo passes that
        consume the citable fact table, split the table into disjoint,
        dictionary-remapped chunks, review every chunk, and ask the same pass
        for one final synthesis over all chunk responses.

        The row index remains the global blind citation index throughout.  No
        fact is ranked, sampled, or dropped, and deterministic callers still
        validate the final response against the immutable full fact graph.
        """

        if pass_name not in {
            "BUSINESS_MODEL_RESEARCH",
            "COMPONENT_RESEARCH",
            "RED_TEAM_RESEARCH",
        }:
            return super().complete(pass_name=pass_name, payload=payload)
        if (
            "loss_accounted_fact_chunk" in payload
            or "loss_accounted_fact_chunk_synthesis" in payload
        ):
            return super().complete(pass_name=pass_name, payload=payload)
        chunks = _loss_accounted_fact_chunk_payloads(
            payload,
            pass_name=pass_name,
            target_projection_chars=self.semantic_prompt_chunk_chars,
        )
        if len(chunks) <= 1:
            return super().complete(pass_name=pass_name, payload=payload)

        chunk_responses = []
        for chunk in chunks:
            allowed_indices = {
                int(row[0])
                for row in chunk.get("current_evidence_fact_graph") or ()
            }
            prior_indices = {
                int(row["fact_row_index"])
                for row in (
                    (
                        chunk.get("prior_component_memo_context") or {}
                    ).get("current_fact_rows")
                    or ()
                )
                if isinstance(row, Mapping)
                and isinstance(row.get("fact_row_index"), int)
            }
            attempt_payload = chunk
            validation_retry_used = False
            while True:
                response = super().complete(
                    pass_name=pass_name,
                    payload=attempt_payload,
                )
                try:
                    _validate_loss_accounted_chunk_response(
                        pass_name=pass_name,
                        response=response,
                        allowed_fact_row_indices=allowed_indices,
                        prior_fact_row_indices=prior_indices,
                    )
                    break
                except StructuredProviderRejected as exc:
                    self.invalidate_last_response_cache(str(exc))
                    if validation_retry_used:
                        raise
                    validation_retry_used = True
                    attempt_payload = scrub_blind_research_payload(
                        {
                            **chunk,
                            "loss_accounted_fact_chunk_validation_retry_context": {
                                "validation_error": str(exc),
                                "rejected_response": response,
                                "allowed_fact_row_indices": sorted(
                                    allowed_indices
                                ),
                                "required_prior_fact_row_indices": sorted(
                                    prior_indices
                                ),
                                "instruction": (
                                    "Rewrite the complete chunk response once. "
                                    "Cite only allowed_fact_row_indices. For a "
                                    "component chunk, return one exact grounding "
                                    "per selected row and dispose every required "
                                    "prior row exactly once. Do not invent evidence, "
                                    "score, or Stage."
                                ),
                            },
                        }
                    )
            chunk_meta = dict(chunk["loss_accounted_fact_chunk"])
            chunk_responses.append(
                {
                    "chunk_index": chunk_meta["chunk_index"],
                    "chunk_fact_count": chunk_meta["chunk_fact_count"],
                    "chunk_fact_row_index_roster_hash": chunk_meta[
                        "chunk_fact_row_index_roster_hash"
                    ],
                    "response": dict(response),
                }
            )

        synthesis_payload = _loss_accounted_fact_chunk_synthesis_payload(
            payload,
            pass_name=pass_name,
            chunks=chunks,
            chunk_responses=chunk_responses,
        )
        attempt_payload = synthesis_payload
        validation_retry_used = False
        while True:
            response = super().complete(
                pass_name=pass_name,
                payload=attempt_payload,
            )
            try:
                _validate_loss_accounted_synthesis_response(
                    pass_name=pass_name,
                    response=response,
                    chunk_responses=chunk_responses,
                )
                break
            except StructuredProviderRejected as exc:
                self.invalidate_last_response_cache(str(exc))
                if validation_retry_used:
                    raise
                validation_retry_used = True
                attempt_payload = scrub_blind_research_payload(
                    {
                        **synthesis_payload,
                        "loss_accounted_fact_synthesis_validation_retry_context": {
                            "validation_error": str(exc),
                            "rejected_response": response,
                            "instruction": (
                                "Rewrite the complete synthesis once. Cite only "
                                "fact rows already cited or selected in the chunk "
                                "responses. For a component synthesis, copy exact "
                                "groundings and prior dispositions from those "
                                "responses. Review every chunk; do not invent "
                                "evidence, total score, or Stage."
                            ),
                        },
                    }
                )
        return response

    @classmethod
    def default(
        cls,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "qwen3.5:27b",
        timeout_seconds: float = 900.0,
        context_length: int = 262_144,
        max_output_tokens: int = 32_768,
        prompt_character_limit: int = 500_000,
        fact_document_chunk_chars: int = 100_000,
        temperature: float = 0.0,
        seed: int = 42,
        think: bool = False,
        keep_alive: int | str = -1,
    ) -> "OllamaResearcherProvider":
        return cls(
            transport=OllamaStructuredProviderTransport(
                base_url=base_url,
                model=model,
                timeout_seconds=timeout_seconds,
                context_length=context_length,
                max_output_tokens=max_output_tokens,
                prompt_character_limit=prompt_character_limit,
                temperature=temperature,
                seed=seed,
                think=think,
                keep_alive=keep_alive,
            ),
            fact_document_chunk_chars=fact_document_chunk_chars,
        )


_LOSS_ACCOUNTED_FACT_CHUNK_PASSES = {
    "BUSINESS_MODEL_RESEARCH",
    "COMPONENT_RESEARCH",
    "RED_TEAM_RESEARCH",
}
_FACT_CHUNK_SYNTHESIS_ONLY_KEYS = {
    "business_model_validation_retry_context",
    "component_research_validation_retry_context",
}


def _loss_accounted_fact_chunk_payloads(
    payload: Mapping[str, Any],
    *,
    pass_name: str,
    target_projection_chars: int,
) -> tuple[Mapping[str, Any], ...]:
    """Partition every citable row once and remap only its local dictionaries."""

    if pass_name not in _LOSS_ACCOUNTED_FACT_CHUNK_PASSES:
        return (dict(payload),)
    raw_rows = payload.get("current_evidence_fact_graph")
    raw_projection = payload.get("current_evidence_fact_projection")
    if (
        not isinstance(raw_rows, Sequence)
        or isinstance(raw_rows, (str, bytes))
        or not isinstance(raw_projection, Mapping)
    ):
        return (dict(payload),)
    rows = tuple(raw_rows)
    if len(rows) < 2:
        return (dict(payload),)
    projection = dict(raw_projection)
    fields = tuple(str(value) for value in projection.get("fact_fields") or ())
    dictionaries = projection.get("fact_value_dictionaries")
    if (
        not fields
        or fields[0] != "fact_row_index"
        or not isinstance(dictionaries, Mapping)
    ):
        return (dict(payload),)
    width = len(fields)
    normalized_rows = []
    row_indices = []
    seen_indices: set[int] = set()
    for raw in rows:
        if (
            not isinstance(raw, Sequence)
            or isinstance(raw, (str, bytes))
            or len(raw) != width
            or isinstance(raw[0], bool)
            or not isinstance(raw[0], int)
            or raw[0] < 0
        ):
            raise ValueError("citable fact projection row is malformed")
        row = tuple(raw)
        row_index = int(row[0])
        if row_index in seen_indices:
            raise ValueError("citable fact projection row indices must be unique")
        seen_indices.add(row_index)
        row_indices.append(row_index)
        normalized_rows.append(row)

    target = max(10_000, int(target_projection_chars))
    groups: list[list[tuple[Any, ...]]] = []
    current: list[tuple[Any, ...]] = []
    current_weight = 0
    for row in normalized_rows:
        weight = _citable_fact_row_transport_weight(
            row,
            fields=fields,
            dictionaries=dictionaries,
        )
        if current and current_weight + weight > target:
            groups.append(current)
            current = []
            current_weight = 0
        current.append(row)
        current_weight += weight
    if current:
        groups.append(current)
    if len(groups) <= 1:
        return (dict(payload),)

    global_index_hash = _canonical_json_hash(row_indices)
    chunks = []
    for chunk_index, group in enumerate(groups):
        projected_rows, projected = _remap_citable_fact_chunk(
            group,
            fields=fields,
            dictionaries=dictionaries,
            global_projection=projection,
            global_fact_row_indices=row_indices,
        )
        allowed_indices = {int(row[0]) for row in projected_rows}
        chunk_payload = {
            key: value
            for key, value in dict(payload).items()
            if key not in _FACT_CHUNK_SYNTHESIS_ONLY_KEYS
        }
        chunk_payload["current_evidence_fact_graph"] = projected_rows
        chunk_payload["current_evidence_fact_projection"] = projected
        _filter_fact_row_context_for_chunk(chunk_payload, allowed_indices)
        chunk_row_indices = sorted(allowed_indices)
        chunk_payload["loss_accounted_fact_chunk"] = {
            "schema_version": "e2r_v5_loss_accounted_fact_chunk_v1",
            "pass_name": pass_name,
            "chunk_index": chunk_index,
            "chunk_count": len(groups),
            "chunk_fact_count": len(group),
            "chunk_fact_row_index_roster_hash": _canonical_json_hash(
                chunk_row_indices
            ),
            "global_fact_count": len(normalized_rows),
            "global_fact_row_index_roster_hash": global_index_hash,
            "every_global_fact_assigned_to_exactly_one_chunk": True,
            "fixed_top_n_used": False,
            "prompt_projection_is_research_cap": False,
            "score_authority": False,
            "instruction": (
                "Review every supplied fact row in this chunk. The first value "
                "is its immutable global fact_row_index. Treat research_complete "
                "or review_complete as completion of this chunk only. Return the "
                "normal pass schema and cite only rows in this chunk. Do not infer "
                "global completeness, score, or Stage from one chunk."
            ),
        }
        chunks.append(scrub_blind_research_payload(chunk_payload))

    emitted = [
        int(row[0])
        for chunk in chunks
        for row in chunk["current_evidence_fact_graph"]
    ]
    if emitted != row_indices or len(emitted) != len(set(emitted)):
        raise ValueError("loss-accounted fact chunks changed the global row roster")
    return tuple(chunks)


def _citable_fact_row_transport_weight(
    row: Sequence[Any],
    *,
    fields: Sequence[str],
    dictionaries: Mapping[str, Any],
) -> int:
    """Conservatively charge repeated values so a chunk cannot grow silently."""

    weight = len(json.dumps(row, ensure_ascii=False, separators=(",", ":")))
    for position, field in enumerate(fields[1:], start=1):
        if not field.endswith("_dictionary_index"):
            raise ValueError("citable fact field is not dictionary encoded")
        dictionary_name = field[: -len("_dictionary_index")]
        values = dictionaries.get(dictionary_name)
        index = row[position]
        if (
            not isinstance(values, Sequence)
            or isinstance(values, (str, bytes))
            or isinstance(index, bool)
            or not isinstance(index, int)
            or index < 0
            or index >= len(values)
        ):
            raise ValueError("citable fact dictionary index is invalid")
        weight += len(
            json.dumps(
                values[index],
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
            )
        )
    return weight + 64


def _remap_citable_fact_chunk(
    rows: Sequence[Sequence[Any]],
    *,
    fields: Sequence[str],
    dictionaries: Mapping[str, Any],
    global_projection: Mapping[str, Any],
    global_fact_row_indices: Sequence[int],
) -> tuple[list[list[Any]], Mapping[str, Any]]:
    local_dictionaries: dict[str, list[Any]] = {}
    index_remaps: dict[str, Mapping[int, int]] = {}
    for position, field in enumerate(fields[1:], start=1):
        dictionary_name = field[: -len("_dictionary_index")]
        global_values = dictionaries[dictionary_name]
        used = sorted({int(row[position]) for row in rows})
        local_dictionaries[dictionary_name] = [
            global_values[index] for index in used
        ]
        index_remaps[dictionary_name] = {
            global_index: local_index
            for local_index, global_index in enumerate(used)
        }
    projected_rows = []
    for row in rows:
        projected_rows.append(
            [
                int(row[0]),
                *(
                    index_remaps[
                        fields[position][: -len("_dictionary_index")]
                    ][int(row[position])]
                    for position in range(1, len(fields))
                ),
            ]
        )
    row_indices = [int(row[0]) for row in projected_rows]
    projected = {
        key: value
        for key, value in dict(global_projection).items()
        if key
        not in {
            "fact_value_dictionaries",
            "fact_id_by_row_index",
            "current_fact_id_roster",
            "closed_fact_history",
        }
    }
    projected.update(
        {
            "schema_version": (
                "e2r_v5_current_decision_citable_fact_chunk_projection_v1"
            ),
            "input_fact_count": len(projected_rows),
            "fact_count": len(projected_rows),
            "closed_fact_count": 0,
            "input_fact_roster_hash": _canonical_json_hash(row_indices),
            "current_fact_roster_hash": _canonical_json_hash(row_indices),
            "closed_fact_roster_hash": _canonical_json_hash([]),
            "fact_value_dictionaries": local_dictionaries,
            "every_input_fact_accounted": True,
            "every_current_fact_individually_citable": True,
            "global_fact_projection_accounting": (
                _global_fact_projection_accounting(
                    global_projection,
                    global_fact_row_indices=global_fact_row_indices,
                )
            ),
            "global_row_indices_preserved_in_chunk": True,
            "full_fact_records_persisted_outside_prompt": True,
            "fixed_top_n_used": False,
            "prompt_projection_is_research_cap": False,
            "score_authority": False,
        }
    )
    return projected_rows, projected


def _global_fact_projection_accounting(
    projection: Mapping[str, Any],
    *,
    global_fact_row_indices: Sequence[int],
) -> Mapping[str, Any]:
    closed_history = projection.get("closed_fact_history")
    return {
        "schema_version": "e2r_v5_global_fact_projection_accounting_v1",
        "input_fact_count": projection.get("input_fact_count"),
        "current_fact_count": projection.get("fact_count"),
        "closed_fact_count": projection.get("closed_fact_count"),
        "input_fact_roster_hash": projection.get("input_fact_roster_hash"),
        "current_fact_roster_hash": projection.get("current_fact_roster_hash"),
        "closed_fact_roster_hash": projection.get("closed_fact_roster_hash"),
        "global_fact_row_index_roster_hash": _canonical_json_hash(
            list(global_fact_row_indices)
        ),
        "closed_fact_history_projection_hash": _canonical_json_hash(
            closed_history
        ),
        "closed_history_persisted_outside_chunk_prompts": True,
        "every_global_fact_partitioned_without_sampling": True,
        "fixed_top_n_used": False,
        "prompt_projection_is_research_cap": False,
        "score_authority": False,
    }


def _filter_fact_row_context_for_chunk(
    payload: dict[str, Any], allowed_indices: set[int]
) -> None:
    counters = payload.get("current_counterfacts")
    if isinstance(counters, Sequence) and not isinstance(counters, (str, bytes)):
        payload["current_counterfacts"] = [
            row
            for row in counters
            if not isinstance(row, Mapping)
            or not isinstance(row.get("fact_row_index"), int)
            or int(row["fact_row_index"]) in allowed_indices
        ]
    prior = payload.get("prior_component_memo_context")
    if isinstance(prior, Mapping):
        projected = dict(prior)
        rows = [
            dict(row)
            for row in projected.get("current_fact_rows") or ()
            if isinstance(row, Mapping)
            and isinstance(row.get("fact_row_index"), int)
            and int(row["fact_row_index"]) in allowed_indices
        ]
        projected["current_fact_rows"] = rows
        projected["current_fact_row_count"] = len(rows)
        projected["chunk_scoped_current_fact_rows"] = True
        payload["prior_component_memo_context"] = projected


def _loss_accounted_fact_chunk_synthesis_payload(
    payload: Mapping[str, Any],
    *,
    pass_name: str,
    chunks: Sequence[Mapping[str, Any]],
    chunk_responses: Sequence[Mapping[str, Any]],
) -> Mapping[str, Any]:
    global_rows = tuple(payload.get("current_evidence_fact_graph") or ())
    row_indices = [int(row[0]) for row in global_rows]
    projection = dict(payload.get("current_evidence_fact_projection") or {})
    synthesis_projection = {
        "schema_version": "e2r_v5_fact_chunk_synthesis_projection_v1",
        "fact_fields": list(projection.get("fact_fields") or ()),
        "global_fact_projection_accounting": _global_fact_projection_accounting(
            projection,
            global_fact_row_indices=row_indices,
        ),
        "fact_semantics_transported_in_chunk_responses": True,
        "full_fact_records_persisted_outside_prompt": True,
        "fixed_top_n_used": False,
        "prompt_projection_is_research_cap": False,
        "score_authority": False,
    }
    result = dict(payload)
    result["current_evidence_fact_graph"] = []
    result["current_evidence_fact_projection"] = synthesis_projection
    result["loss_accounted_fact_chunk_synthesis"] = {
        "schema_version": "e2r_v5_loss_accounted_fact_chunk_synthesis_v1",
        "pass_name": pass_name,
        "chunk_count": len(chunks),
        "global_fact_count": len(global_rows),
        "global_fact_row_index_roster_hash": _canonical_json_hash(row_indices),
        "chunk_partition_roster_hash": _canonical_json_hash(
            [chunk["loss_accounted_fact_chunk"] for chunk in chunks]
        ),
        "chunk_responses": [dict(row) for row in chunk_responses],
        "every_chunk_response_must_be_reviewed": True,
        "fixed_top_n_used": False,
        "prompt_projection_is_research_cap": False,
        "score_authority": False,
        "instruction": (
            "Synthesize every chunk response into exactly one normal pass "
            "response. No chunk is a global conclusion. Cite only fact row "
            "indices already cited or selected by at least one chunk response. "
            "For COMPONENT_RESEARCH, copy selected fact groundings exactly from "
            "the chunk responses, reconcile every prior fact disposition once, "
            "and recalibrate one component range across all chunks. For "
            "BUSINESS_MODEL_RESEARCH and RED_TEAM_RESEARCH, integrate all support, "
            "counterevidence, dependencies, and uncertainties. Completion means "
            "all chunk responses were reviewed; never output total score or Stage."
        ),
    }
    return scrub_blind_research_payload(result)


def _validate_loss_accounted_chunk_response(
    *,
    pass_name: str,
    response: Mapping[str, Any],
    allowed_fact_row_indices: set[int],
    prior_fact_row_indices: set[int],
) -> None:
    cited = _response_fact_row_indices(pass_name, response)
    if not cited.issubset(allowed_fact_row_indices):
        raise StructuredProviderRejected(
            "loss_accounted_fact_chunk_cited_outside_chunk"
        )
    if pass_name != "COMPONENT_RESEARCH":
        return
    grounding_indices = _mapping_fact_row_indices(
        response.get("selected_fact_groundings") or ()
    )
    if grounding_indices != cited:
        raise StructuredProviderRejected(
            "loss_accounted_fact_chunk_grounding_roster_mismatch"
        )
    disposition_indices = _mapping_fact_row_indices(
        response.get("prior_fact_dispositions") or ()
    )
    if disposition_indices != prior_fact_row_indices:
        raise StructuredProviderRejected(
            "loss_accounted_fact_chunk_prior_disposition_roster_mismatch"
        )


def _validate_loss_accounted_synthesis_response(
    *,
    pass_name: str,
    response: Mapping[str, Any],
    chunk_responses: Sequence[Mapping[str, Any]],
) -> None:
    allowed = set()
    allowed_dispositions = set()
    for row in chunk_responses:
        partial = row.get("response") or {}
        if isinstance(partial, Mapping):
            allowed.update(_response_fact_row_indices(pass_name, partial))
            if pass_name == "COMPONENT_RESEARCH":
                allowed_dispositions.update(
                    _mapping_fact_row_indices(
                        partial.get("prior_fact_dispositions") or ()
                    )
                )
    cited = _response_fact_row_indices(pass_name, response)
    if not cited.issubset(allowed):
        raise StructuredProviderRejected(
            "loss_accounted_fact_synthesis_invented_fact_row"
        )
    if pass_name == "COMPONENT_RESEARCH":
        grounding_indices = _mapping_fact_row_indices(
            response.get("selected_fact_groundings") or ()
        )
        if grounding_indices != cited:
            raise StructuredProviderRejected(
                "loss_accounted_fact_synthesis_grounding_roster_mismatch"
            )
        dispositions = _mapping_fact_row_indices(
            response.get("prior_fact_dispositions") or ()
        )
        if not dispositions.issubset(allowed_dispositions):
            raise StructuredProviderRejected(
                "loss_accounted_fact_synthesis_invented_prior_disposition"
            )


def _response_fact_row_indices(
    pass_name: str, response: Mapping[str, Any]
) -> set[int]:
    field = {
        "BUSINESS_MODEL_RESEARCH": "fact_row_indices",
        "COMPONENT_RESEARCH": "selected_fact_row_indices",
        "RED_TEAM_RESEARCH": "challenged_fact_row_indices",
    }[pass_name]
    values = response.get(field)
    if not isinstance(values, Sequence) or isinstance(values, (str, bytes)):
        raise StructuredProviderRejected(
            f"loss_accounted_fact_response_missing_{field}"
        )
    output = set()
    for value in values:
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise StructuredProviderRejected(
                f"loss_accounted_fact_response_invalid_{field}"
            )
        if value in output:
            raise StructuredProviderRejected(
                f"loss_accounted_fact_response_duplicate_{field}"
            )
        output.add(value)
    return output


def _mapping_fact_row_indices(rows: Any) -> set[int]:
    if not isinstance(rows, Sequence) or isinstance(rows, (str, bytes)):
        raise StructuredProviderRejected(
            "loss_accounted_fact_response_mapping_rows_invalid"
        )
    output = set()
    for row in rows:
        if (
            not isinstance(row, Mapping)
            or isinstance(row.get("fact_row_index"), bool)
            or not isinstance(row.get("fact_row_index"), int)
            or int(row["fact_row_index"]) < 0
        ):
            raise StructuredProviderRejected(
                "loss_accounted_fact_response_mapping_row_invalid"
            )
        row_index = int(row["fact_row_index"])
        if row_index in output:
            raise StructuredProviderRejected(
                "loss_accounted_fact_response_mapping_row_duplicate"
            )
        output.add(row_index)
    return output


def _provider_error_detail(error: Exception) -> str:
    return " ".join(str(error).split())[-500:] or "no detail"


def _provider_usage_limit_reset_hint(value: str) -> str | None:
    match = _PROVIDER_USAGE_LIMIT_RESET_RE.search(str(value))
    return " ".join(match.group(1).split()) if match else None


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
        prior_memo: ComponentResearchMemo | Mapping[str, Any] | None = None,
        prior_supervisor_feedback: Mapping[str, Any] | None = None,
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
        structured_metric_id_by_row_index = {
            index: metric_id
            for index, metric_id in enumerate(sorted(metric_input))
        }
        structured_metric_rows = [
            {
                "structured_metric_row_index": row_index,
                "structured_requirement_id": metric_id,
                "immutable_source_backed_value": metric_input[metric_id],
            }
            for row_index, metric_id in structured_metric_id_by_row_index.items()
        ]
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
        fact_projection = project_current_decision_citable_facts(citable_facts)
        fact_id_by_row_index = citable_fact_id_by_row_index(fact_projection)
        fact_row_index_by_id = {
            fact_id: row_index
            for row_index, fact_id in fact_id_by_row_index.items()
        }
        prior_memo_context = _project_prior_component_memo_context(
            prior_memo=prior_memo,
            plan=plan,
            facts=fact_by_id,
            fact_id_by_row_index=fact_id_by_row_index,
        )
        supervisor_feedback_context = _project_prior_supervisor_feedback(
            feedback=prior_supervisor_feedback,
            fact_id_by_row_index=fact_id_by_row_index,
        )
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
                "research_plan": _project_component_research_plan(plan),
                "target_business_model": business_model.to_dict(),
                "current_evidence_fact_graph": fact_projection["facts"],
                "current_evidence_fact_projection": {
                    key: value
                    for key, value in fact_projection.items()
                    if key not in {"facts", "fact_id_by_row_index"}
                },
                "selected_fact_grounding_contract": {
                    "required_for_every_selected_fact": True,
                    "exactly_once": True,
                    "source_predicate_copy_exactly": True,
                    "source_economic_mechanism_copy_exactly": True,
                    "source_value_json_encoding": (
                        "compact JSON of the decoded source value"
                    ),
                    "source_period_json_encoding": (
                        "compact JSON of the decoded source period"
                    ),
                    "component_cases_must_match_groundings": True,
                    "unsupported_fact_action": "OMIT_AND_RESELECT",
                    "deterministic_code_may_repair_interpretation": False,
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
                        "fact_row_index": fact_row_index_by_id[row.fact_id],
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
                "prior_component_memo_context": prior_memo_context,
                "prior_supervisor_feedback_context": (
                    supervisor_feedback_context
                ),
                "historical_component_anchors": list(anchors),
                "source_coverage": coverage_rows,
                "source_claims": project_research_source_claim_profile(
                    citable_source_claims
                ),
                "source_documents": project_research_source_document_profile(
                    source_documents
                ),
                "structured_metric_rows": structured_metric_rows,
            }
        )
        attempt_payload = payload
        validation_retry_used = False
        while True:
            try:
                response = self.provider.complete(
                    pass_name="COMPONENT_RESEARCH",
                    payload=attempt_payload,
                )
            except (
                StructuredProviderUnavailable,
                StructuredProviderRejected,
                TimeoutError,
                OSError,
                RuntimeError,
            ) as exc:
                return _pending_result(
                    self,
                    "PROVIDER_ERROR",
                    exc,
                    prompt_hash=_provider_prompt_hash(self.provider),
                )
            prompt_hash = _provider_prompt_hash(self.provider)
            try:
                memo = _component_memo_from_response(
                    response=response,
                    plan=plan,
                    facts=fact_by_id,
                    anchors=anchor_by_id,
                    coverage_labels=coverage_labels,
                    structured_metrics=metric_input,
                    structured_metric_id_by_row_index=(
                        structured_metric_id_by_row_index
                    ),
                    fact_id_by_row_index=fact_id_by_row_index,
                    prior_memo_context=prior_memo_context,
                )
            except (KeyError, TypeError, ValueError) as exc:
                _invalidate_provider_response_cache(self.provider, exc)
                if validation_retry_used:
                    return _pending_result(
                        self,
                        "INVALID_PROVIDER_OUTPUT",
                        exc,
                        prompt_hash=prompt_hash,
                    )
                validation_retry_used = True
                attempt_payload = scrub_blind_research_payload(
                    {
                        **payload,
                        "component_research_validation_retry_context": {
                            "validation_error": (
                                " ".join(str(exc).split())[-500:]
                                or exc.__class__.__name__
                            ),
                            "rejected_response": response,
                            "expected_selected_fact_groundings": (
                                _expected_selected_fact_grounding_rows(
                                    response=response,
                                    fact_id_by_row_index=(
                                        fact_id_by_row_index
                                    ),
                                    facts=fact_by_id,
                                )
                            ),
                            "instruction": (
                                "Rewrite the complete component memo. Use only "
                                "supplied fact row indices, structured metric row "
                                "indices, coverage labels, and anchor ids. Every "
                                "nearest anchor must also appear in "
                                "historical_anchor_ids and must match its positive "
                                "or counter role. Account for every row in "
                                "prior_component_memo_context.current_fact_rows "
                                "exactly once in prior_fact_dispositions. A RETAIN "
                                "row must be selected and an OMIT row must include "
                                "a semantic reason and remain unselected. Positive "
                                "points require at least one selected current "
                                "POSITIVE fact; neutral context and structured "
                                "metrics with score_authority=false are not positive "
                                "score evidence. If no positive fact qualifies, "
                                "return a zero score range instead of narrating an "
                                "unsupported positive score. Return exactly one "
                                "selected_fact_groundings row for every selected fact. "
                                "Copy its decoded predicate and economic_mechanism "
                                "exactly, and compact-JSON encode its decoded value and "
                                "period. The expected_selected_fact_groundings rows "
                                "repeat those immutable source fields for correction; "
                                "copy them exactly but write component_interpretation "
                                "yourself. Cases, dispositions, and interpretations must "
                                "match those immutable fields; omit a fact rather than "
                                "turning it into a different comparison or mechanism. "
                                "Do not let deterministic "
                                "code repair, retain, or invent any citation."
                            ),
                        },
                    }
                )
                continue
            break
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
    structured_metric_id_by_row_index: Mapping[int, str],
    fact_id_by_row_index: Mapping[int, str],
    prior_memo_context: Mapping[str, Any],
) -> ComponentResearchMemo:
    if not isinstance(response, Mapping):
        raise TypeError("component researcher response must be an object")
    assert_blind_research_output(response)
    selected = resolve_citable_fact_row_indices(
        response["selected_fact_row_indices"],
        fact_id_by_row_index=fact_id_by_row_index,
        label="selected_fact_row_indices",
    )
    selected_fact_row_indices = tuple(
        int(row) for row in response["selected_fact_row_indices"]
    )
    _validate_selected_fact_groundings(
        response=response,
        selected_fact_row_indices=selected_fact_row_indices,
        fact_id_by_row_index=fact_id_by_row_index,
        facts=facts,
    )
    _validate_prior_fact_dispositions(
        response=response,
        selected_fact_row_indices=selected_fact_row_indices,
        prior_memo_context=prior_memo_context,
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
    proposed_score_range = tuple(
        float(response[key])
        for key in (
            "proposed_score_lower",
            "proposed_score_mid",
            "proposed_score_upper",
        )
    )
    if not positive and any(value > 0.0 for value in proposed_score_range):
        raise ValueError(
            "positive component score requires at least one selected current "
            "POSITIVE EvidenceFact; neutral context and non-authoritative "
            "structured metrics cannot support positive points"
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
    returned_metric_ids = _resolve_structured_metric_row_indices(
        response["structured_metric_row_indices"],
        structured_metric_id_by_row_index=structured_metric_id_by_row_index,
    )
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
        proposed_score_lower=proposed_score_range[0],
        proposed_score_mid=proposed_score_range[1],
        proposed_score_upper=proposed_score_range[2],
        confidence=float(response["confidence"]),
        research_complete=bool(response["research_complete"]),
        nearest_positive_anchor_ids=nearest_positive,
        nearest_counter_anchor_ids=nearest_counter,
        why_not_higher=str(response["why_not_higher"]),
        why_not_lower=str(response["why_not_lower"]),
        researcher_role=plan.researcher_role,
    )


def _project_prior_component_memo_context(
    *,
    prior_memo: ComponentResearchMemo | Mapping[str, Any] | None,
    plan: ComponentResearchPlan,
    facts: Mapping[str, EvidenceFact],
    fact_id_by_row_index: Mapping[int, str],
) -> Mapping[str, Any]:
    """Project prior LLM selections into current blind row indices.

    The prior memo is continuity context, never score authority.  Facts that no
    longer exist in the current citable plane are represented only by a count
    and roster hash so stale ids cannot be cited or deterministically carried.
    """

    empty = {
        "available": False,
        "score_authority": False,
        "deterministic_fact_carry_forward": False,
        "current_fact_rows": [],
        "current_fact_row_count": 0,
        "unavailable_prior_fact_count": 0,
        "unavailable_prior_fact_roster_hash": hashlib.sha256(b"[]").hexdigest(),
    }
    if prior_memo is None:
        return empty
    for key, expected in (
        ("target_id", plan.target_id),
        ("archetype_id", plan.archetype_id),
        ("component_id", plan.component_id),
        ("researcher_role", plan.researcher_role),
    ):
        if str(_field(prior_memo, key) or "") != expected:
            raise ValueError(f"prior component memo {key} mismatch")
    fact_row_index_by_id = {
        fact_id: row_index for row_index, fact_id in fact_id_by_row_index.items()
    }
    role_fields = (
        ("POSITIVE", "positive_fact_ids"),
        ("COUNTER", "counter_fact_ids"),
        ("RESOLUTION", "resolution_fact_ids"),
        ("CONTEXT", "context_fact_ids"),
    )
    seen: set[str] = set()
    current_rows = []
    unavailable = []
    for prior_role, field_name in role_fields:
        raw_ids = _field(prior_memo, field_name) or ()
        if isinstance(raw_ids, str) or not isinstance(raw_ids, Sequence):
            raise ValueError(f"prior component memo {field_name} must be an array")
        for raw_fact_id in raw_ids:
            fact_id = str(raw_fact_id).strip()
            if not fact_id or fact_id in seen:
                raise ValueError("prior component memo fact ids must be unique")
            seen.add(fact_id)
            row_index = fact_row_index_by_id.get(fact_id)
            if row_index is None:
                unavailable.append(fact_id)
                continue
            fact = facts[fact_id]
            current_rows.append(
                {
                    "fact_row_index": row_index,
                    "prior_role": prior_role,
                    "current_direction": fact.direction,
                    "current_lifecycle": fact.current_lifecycle,
                }
            )
    unavailable.sort()
    current_rows.sort(key=lambda row: int(row["fact_row_index"]))
    return {
        "available": True,
        "score_authority": False,
        "deterministic_fact_carry_forward": False,
        "prior_research_complete": bool(
            _field(prior_memo, "research_complete")
        ),
        "current_fact_rows": current_rows,
        "current_fact_row_count": len(current_rows),
        "unavailable_prior_fact_count": len(unavailable),
        "unavailable_prior_fact_roster_hash": hashlib.sha256(
            json.dumps(unavailable, separators=(",", ":")).encode("utf-8")
        ).hexdigest(),
    }


def _project_component_research_plan(
    plan: ComponentResearchPlan,
) -> Mapping[str, Any]:
    """Keep plan semantics without replaying the full stable fact-id roster.

    The provider selects facts exclusively through the blind row indices in
    ``current_evidence_fact_graph``.  Replaying thousands of stable fact ids in
    ``research_plan.candidate_fact_ids`` therefore duplicates the same decision
    plane, exposes a citation namespace the provider must not use, and can push
    an otherwise valid component prompt beyond the model context window.

    Deterministic code validates the complete plan roster before this
    projection is built.  The prompt carries its exact count and ordered hash,
    while the immutable full plan remains in the dossier.  No fact row is
    sampled or removed from the provider's citable fact graph.
    """

    payload = dict(plan.to_dict())
    candidate_fact_ids = tuple(
        str(value) for value in payload.pop("candidate_fact_ids", ())
    )
    encoded_roster = json.dumps(
        candidate_fact_ids,
        ensure_ascii=False,
        separators=(",", ":"),
    ).encode("utf-8")
    payload["candidate_fact_roster_projection"] = {
        "candidate_fact_count": len(candidate_fact_ids),
        "candidate_fact_roster_hash": hashlib.sha256(encoded_roster).hexdigest(),
        "provider_selection_namespace": "current_evidence_fact_graph.fact_row_index",
        "candidate_fact_ids_exposed_to_provider": False,
        "every_candidate_fact_accounted_by_count_and_hash": True,
        "full_candidate_fact_roster_persisted_in_dossier": True,
        "fixed_top_n_used": False,
        "prompt_projection_is_research_cap": False,
        "score_authority": False,
    }
    return payload


def _project_prior_supervisor_feedback(
    *,
    feedback: Mapping[str, Any] | None,
    fact_id_by_row_index: Mapping[int, str],
) -> Mapping[str, Any]:
    """Expose component-scoped supervisor diagnostics without stable fact ids.

    A supervisor finding is continuity feedback for the next LLM rewrite.  It
    is never score or Stage authority.  Current fact ids are translated back
    into the same blind row indices used by the component prompt so the model
    can correct a semantic contradiction without gaining a second citation
    namespace or being allowed to cite stale facts.
    """

    if feedback is None:
        return {
            "available": False,
            "score_authority": False,
            "stage_authority": False,
            "feedback": {},
        }
    if not isinstance(feedback, Mapping):
        raise TypeError("prior supervisor feedback must be an object")
    fact_row_index_by_id = {
        fact_id: row_index
        for row_index, fact_id in fact_id_by_row_index.items()
    }

    def project(value: Any) -> Any:
        if isinstance(value, Mapping):
            return {str(key): project(item) for key, item in value.items()}
        if isinstance(value, (list, tuple)):
            return [project(item) for item in value]
        if not isinstance(value, str):
            return value
        # Row indices are private to one prompt projection and can shift when
        # new facts arrive.  Retire every prior raw row reference before
        # translating stable fact ids into the current projection below.
        result = re.sub(
            r"\b(?:current_fact_row_index|fact_row_index|row)\s*"
            r"(?:=|:)?\s*\d+(?!\d)",
            "unavailable_prior_row",
            value,
            flags=re.IGNORECASE,
        )
        for fact_id, row_index in sorted(
            fact_row_index_by_id.items(), key=lambda item: -len(item[0])
        ):
            result = result.replace(
                fact_id, f"current_fact_row_index={row_index}"
            )
        # A stale fact may remain in an old supervisor note after source
        # retirement.  Keep the diagnostic meaning but never expose an
        # unavailable citation id to the current component decision plane.
        result = re.sub(
            r"\bEFACT-[A-Za-z0-9]+\b",
            "unavailable_prior_fact",
            result,
        )
        return result

    return {
        "available": True,
        "score_authority": False,
        "stage_authority": False,
        "instruction": (
            "Treat this as diagnostic feedback for a full semantic rewrite. "
            "Correct cited fact direction, predicate, value, and narrative "
            "consistency; independently reselect current fact rows."
        ),
        "feedback": scrub_blind_research_payload(project(dict(feedback))),
    }


def _validate_prior_fact_dispositions(
    *,
    response: Mapping[str, Any],
    selected_fact_row_indices: Sequence[int],
    prior_memo_context: Mapping[str, Any],
) -> None:
    value = response["prior_fact_dispositions"]
    if isinstance(value, (str, bytes)) or not isinstance(value, Sequence):
        raise TypeError("prior_fact_dispositions must be an array")
    expected = {
        int(row["fact_row_index"])
        for row in prior_memo_context.get("current_fact_rows") or ()
    }
    dispositions: dict[int, str] = {}
    for row in value:
        if not isinstance(row, Mapping):
            raise TypeError("prior fact disposition must be an object")
        if set(row) != {"fact_row_index", "disposition", "reason"}:
            raise ValueError("prior fact disposition fields are invalid")
        row_index = row["fact_row_index"]
        if isinstance(row_index, bool) or not isinstance(row_index, int) or row_index < 0:
            raise TypeError("prior fact disposition row index must be non-negative")
        disposition = str(row["disposition"])
        if disposition not in {"RETAIN", "OMIT"}:
            raise ValueError("prior fact disposition must be RETAIN or OMIT")
        if not str(row["reason"]).strip():
            raise ValueError("prior fact disposition requires a reason")
        if row_index in dispositions:
            raise ValueError("prior fact disposition row indices must be unique")
        dispositions[row_index] = disposition
    if set(dispositions) != expected:
        raise ValueError(
            "prior fact dispositions must account for every currently citable "
            "prior fact row exactly once"
        )
    selected = set(selected_fact_row_indices)
    retained = {
        row_index
        for row_index, disposition in dispositions.items()
        if disposition == "RETAIN"
    }
    omitted = set(dispositions) - retained
    if not retained.issubset(selected):
        raise ValueError("RETAIN prior fact rows must be selected again")
    if omitted & selected:
        raise ValueError("OMIT prior fact rows cannot remain selected")


def _validate_selected_fact_groundings(
    *,
    response: Mapping[str, Any],
    selected_fact_row_indices: Sequence[int],
    fact_id_by_row_index: Mapping[int, str],
    facts: Mapping[str, EvidenceFact],
) -> None:
    """Require the LLM to re-ground every selection in immutable fact fields."""

    value = response["selected_fact_groundings"]
    if isinstance(value, (str, bytes)) or not isinstance(value, Sequence):
        raise TypeError("selected_fact_groundings must be an array")
    expected_indices = set(selected_fact_row_indices)
    groundings: dict[int, Mapping[str, Any]] = {}
    expected_fields = {
        "fact_row_index",
        "source_predicate",
        "source_value_json",
        "source_period_json",
        "source_economic_mechanism",
        "component_interpretation",
    }
    for row in value:
        if not isinstance(row, Mapping):
            raise TypeError("selected fact grounding must be an object")
        if set(row) != expected_fields:
            raise ValueError("selected fact grounding fields are invalid")
        row_index = row["fact_row_index"]
        if (
            isinstance(row_index, bool)
            or not isinstance(row_index, int)
            or row_index < 0
        ):
            raise TypeError(
                "selected fact grounding row index must be non-negative"
            )
        if row_index in groundings:
            raise ValueError(
                "selected fact grounding row indices must be unique"
            )
        groundings[row_index] = row
    if set(groundings) != expected_indices:
        raise ValueError(
            "selected fact groundings must account for every selected fact "
            "row exactly once"
        )
    for row_index, grounding in groundings.items():
        fact_id = fact_id_by_row_index.get(row_index)
        if fact_id is None or fact_id not in facts:
            raise ValueError(
                "selected fact grounding references an unavailable fact row"
            )
        fact = facts[fact_id]
        expected = _immutable_fact_grounding_fields(fact)
        for field, expected_value in expected.items():
            if str(grounding[field]) != str(expected_value):
                raise ValueError(
                    f"selected fact grounding {field} mismatch for row "
                    f"{row_index}"
                )
        if not str(grounding["component_interpretation"]).strip():
            raise ValueError(
                "selected fact grounding requires a component interpretation"
            )


def _expected_selected_fact_grounding_rows(
    *,
    response: Any,
    fact_id_by_row_index: Mapping[int, str],
    facts: Mapping[str, EvidenceFact],
) -> list[Mapping[str, Any]]:
    """Focus a rejected rewrite on exact source fields without repairing it."""

    if not isinstance(response, Mapping):
        return []
    selected = response.get("selected_fact_row_indices")
    if isinstance(selected, (str, bytes)) or not isinstance(selected, Sequence):
        return []
    result: list[Mapping[str, Any]] = []
    seen: set[int] = set()
    for row_index in selected:
        if (
            isinstance(row_index, bool)
            or not isinstance(row_index, int)
            or row_index < 0
            or row_index in seen
        ):
            continue
        seen.add(row_index)
        fact_id = fact_id_by_row_index.get(row_index)
        if fact_id is None or fact_id not in facts:
            continue
        result.append(
            {
                "fact_row_index": row_index,
                **_immutable_fact_grounding_fields(facts[fact_id]),
            }
        )
    return result


def _immutable_fact_grounding_fields(
    fact: EvidenceFact,
) -> Mapping[str, str]:
    return {
        "source_predicate": fact.predicate,
        "source_value_json": _canonical_fact_field_json(fact.value),
        "source_period_json": _canonical_fact_field_json(fact.period),
        "source_economic_mechanism": fact.economic_mechanism,
    }


def _canonical_fact_field_json(value: Any) -> str:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        default=str,
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


def _resolve_structured_metric_row_indices(
    value: Any,
    *,
    structured_metric_id_by_row_index: Mapping[int, str],
) -> tuple[str, ...]:
    if isinstance(value, (str, bytes)) or not isinstance(value, Sequence):
        raise TypeError("structured_metric_row_indices must be an array")
    indices: list[int] = []
    for item in value:
        if isinstance(item, bool) or not isinstance(item, int) or item < 0:
            raise TypeError(
                "structured_metric_row_indices must contain non-negative integers"
            )
        indices.append(item)
    if len(indices) != len(set(indices)):
        raise ValueError(
            "structured_metric_row_indices must not contain duplicates"
        )
    unknown = sorted(set(indices) - set(structured_metric_id_by_row_index))
    if unknown:
        raise ValueError(
            "researcher selected unknown structured metric row indices: "
            f"{unknown}"
        )
    return tuple(
        structured_metric_id_by_row_index[index] for index in indices
    )


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


def _canonical_json_hash(value: Any) -> str:
    encoded = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def _provider_name(provider: StructuredResearchProvider) -> str:
    return str(getattr(provider, "provider_name", provider.__class__.__name__))


def _provider_prompt_hash(provider: StructuredResearchProvider) -> str | None:
    calls = getattr(provider, "calls", ())
    if calls and isinstance(calls[-1], Mapping):
        value = calls[-1].get("prompt_hash")
        return str(value) if value else None
    return None


def _invalidate_provider_response_cache(
    provider: StructuredResearchProvider,
    error: Exception,
) -> None:
    invalidate = getattr(provider, "invalidate_last_response_cache", None)
    if not callable(invalidate):
        return
    reason = (
        f"{error.__class__.__name__}:"
        + (" ".join(str(error).split())[-500:] or "no detail")
    )
    try:
        invalidate(reason=reason)
    except (OSError, TypeError, ValueError, RuntimeError):
        # Cache audit failures must never turn a rejected memo into an accepted
        # memo or suppress the bounded LLM correction attempt.
        return


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
            "The prior_component_memo_context is non-authoritative continuity context. "
            "Reassess every current prior fact row and account for it exactly once in "
            "prior_fact_dispositions as RETAIN or OMIT with a semantic reason; RETAIN "
            "rows must also appear in selected_fact_row_indices and OMIT rows must not. "
            "This is an LLM reselection decision, never deterministic carry-forward. "
            "When prior_supervisor_feedback_context.available is true, address its "
            "component-specific semantic findings in a complete rewrite. Treat the "
            "feedback as diagnostic continuity, not score or Stage authority. Never "
            "reverse a selected fact's predicate or value to fit the thesis; omit it "
            "or narrate its actual economic meaning. "
            "For every selected fact row, return exactly one selected_fact_groundings "
            "row. Copy the decoded predicate and economic_mechanism exactly; encode "
            "the decoded value and period as compact JSON strings. The positive_case, "
            "counter_case, prior dispositions, and component_interpretation must all "
            "remain consistent with those immutable groundings. If the real fact does "
            "not support the component thesis, OMIT it instead of changing its "
            "comparison basis, subject, period, predicate, value, or mechanism. "
            "A positive score range requires at least one selected current POSITIVE "
            "EvidenceFact. Neutral context and structured metrics marked "
            "score_authority=false cannot support positive points. "
            "Return structured_metric_row_indices using only the explicit row numbers "
            "from structured_metric_rows. The deterministic engine will restore the "
            "immutable requirement ids and values; never copy a nested record metric_id "
            "or invent a value."
        )
    if pass_name == "RED_TEAM_RESEARCH":
        return "Challenge every material thesis independently, distinguish current counters from resolved history, and identify new research directions."
    if pass_name == "SYNTHESIS_REVIEW":
        return "Synthesize cross-component support and tension without calculating total points or Stage."
    if pass_name == "SOURCE_QUERY_GENERATION":
        return (
            "Generate literal target-scoped discovery queries from the current facts, "
            "missing information, source failures, and open objectives. Do not reuse an "
            "executed query and do not supply a deterministic fallback template. When "
            "score_gap_context supplies missing_role_resolution_contracts, follow the "
            "accepted evidence roles, allowed source families, and validation conditions "
            "literally. Semantically adjacent evidence from an ineligible source is not "
            "progress; for example, a third-party estimate cannot replace an issuer-only "
            "requirement. The default web discovery backend is token-oriented Naver "
            "search: make each literal query a short natural-language request for one "
            "claim or one source route. Keep cutoff dates, evidence eligibility rules, "
            "long quoted phrases, and multi-claim instructions in the rationale rather "
            "than stuffing them into the literal query; a relevant fiscal period or year "
            "may still be part of the query. After a zero-result or irrelevant "
            "result, materially change the vocabulary and relax site, path, and exact-quote "
            "constraints instead of repeating the same query. An issuer landing page may "
            "lead to a presentation, transcript, or delegated IR asset, so generate a "
            "route that can discover the landing page as well as the final document. The "
            "LLM still owns every literal query."
        )
    if pass_name == "SOURCE_CANDIDATE_RANKING":
        return (
            "Assess every discovery candidate for material relevance to the supplied "
            "research objectives. Snippets are discovery metadata only, never evidence. "
            "Use requested_source_families, verified_official_domain_candidate, and "
            "candidate_source_family_hint as discovery provenance. When an objective "
            "requires an issuer source, prioritize an eligible verified issuer-domain "
            "candidate over a third-party retelling even when the issuer snippet is sparse. "
            "A landing page, redirect page, or document referenced by an already fetched "
            "page may be materially relevant as a route to the full original source; do "
            "not reject it merely because it is not yet evidence."
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
            "Return every distinct material fact exactly once. Repeated page headers, duplicated "
            "body copies, overlapping transport text, and the same quote/economic mechanism do "
            "not justify duplicate fact rows. This is lossless deduplication, not a top-N limit: "
            "all distinct material facts and counterfacts still must be returned. "
            f"The facts array is one transport page of at most {FACT_EXTRACTION_PAGE_FACT_LIMIT} "
            "new facts, never a total fact cap. If more distinct facts remain after this page, "
            "set extraction_complete=false and list the affected document ids in "
            "unresolved_document_ids. When fact_extraction_continuation_context is present, "
            "return only the next facts not listed there. A page that reaches the page limit "
            "must be followed by another page; an empty final page with the accurate document "
            "disposition may certify that no distinct facts remain. "
            "Never use snippets, future outcomes, score, or Stage."
        )
    if pass_name == "RESEARCH_SUPERVISOR_REVIEW":
        return (
            "Review every component memo, fact gap, structured-data gap, prior query/source "
            "failure, and counter route. Prior failures may be loss-accounted semantic groups; "
            "classify each group failure_id exactly once and apply it to all member_failure_ids. "
            "Classify parser/extractor failure separately from "
            "source absence. Suggest semantic source/query directions; do not write literal "
            "fallback query templates and never treat zero results or a budget limit as completion. "
            "When supervisor_validation_retry_context is present, rewrite the entire response "
            "once using its validation error, allowed objective ids, and deterministic current "
            "state as authoritative correction feedback. Do not repeat the rejected semantic "
            "contradiction and do not invent evidence, scores, or stages."
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
    if pass_name == "STAGE_GATE_FACT_MAPPING":
        return (
            "Map only source-backed material claim ids to exact configured Evidence Contract "
            "primitive ids. SUPPORT means a current positive mechanism and COUNTER means a "
            "current thesis risk. Primitive names are semantic labels, never score or Stage "
            "authority. Review every supplied claim, report unresolved material questions, "
            "and never calculate points, total score, canonical Stage, or an investment action."
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
    "OllamaResearcherProvider",
    "RED_TEAM_RESEARCH_SCHEMA",
    "SOURCE_CANDIDATE_RANKING_SCHEMA",
    "SOURCE_QUERY_GENERATION_SCHEMA",
    "RESEARCH_SUPERVISOR_SCHEMA",
    "SEMANTIC_SATURATION_REVIEW_SCHEMA",
    "STAGE_GATE_FACT_MAPPING_SCHEMA",
    "CLAIM_COMPONENT_IMPACT_MAPPING_SCHEMA",
    "SYNTHESIS_REVIEW_SCHEMA",
    "StructuredResearchProvider",
    "STRUCTURED_PEER_SELECTION_SCHEMA",
    "ValuationResearcher",
    "build_component_researchers",
]
