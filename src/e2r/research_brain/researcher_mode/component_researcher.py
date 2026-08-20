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

CANDIDATE_RANKING_PAGE_CANDIDATE_LIMIT = 12
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
        "challenged_fact_row_indices": {
            **_NONNEGATIVE_INTEGER_ARRAY,
            "uniqueItems": True,
        },
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
            "maxItems": CANDIDATE_RANKING_PAGE_CANDIDATE_LIMIT,
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": [
                    "candidate_id",
                    "material_relevance",
                    "priority",
                    "objective_ids",
                    "matched_requested_source_family",
                    "rationale",
                ],
                "properties": {
                    "candidate_id": {"type": "string", "minLength": 1},
                    "material_relevance": {"type": "boolean"},
                    "priority": {"type": "number", "minimum": 0, "maximum": 1},
                    "objective_ids": _STRING_ARRAY,
                    "matched_requested_source_family": {
                        "type": "string",
                        "minLength": 1,
                    },
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
                    "value": {
                        "anyOf": [
                            {"type": "string", "minLength": 1},
                            {"type": "number"},
                        ]
                    },
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
                                "LATEST_ACTUAL_DEPRECIATION_AMORTIZATION",
                                "EPS_REVISION",
                                "OPERATING_PROFIT_REVISION",
                                "FORWARD_BOOK_VALUE",
                                "FORWARD_PB",
                                "FORWARD_EV_EBITDA",
                                "DURABLE_VISIBILITY",
                            ],
                        },
                        "maxItems": 1,
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
                            "NO_OBJECTIVE_LOCAL_FACT",
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
        "fact_dispositions",
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
                    "fact_row_indices",
                    "semantic_rationale",
                ],
                "properties": {
                    "primitive_id": {"type": "string", "minLength": 1},
                    "direction": {
                        "type": "string",
                        "enum": ["SUPPORT", "COUNTER"],
                    },
                    "fact_row_indices": {
                        "type": "array",
                        "minItems": 1,
                        "items": {"type": "integer", "minimum": 0},
                    },
                    "semantic_rationale": {"type": "string", "minLength": 1},
                },
            },
        },
        "fact_dispositions": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": [
                    "fact_row_index",
                    "status",
                    "rationale",
                ],
                "properties": {
                    "fact_row_index": {
                        "type": "integer",
                        "minimum": 0,
                    },
                    "status": {
                        "type": "string",
                        "enum": ["MAPPED", "NO_MATCH", "UNRESOLVED"],
                    },
                    "rationale": {"type": "string", "minLength": 1},
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


def _provider_output_schema(
    *,
    pass_name: str,
    payload: Mapping[str, Any],
) -> Mapping[str, Any]:
    """Bind a component chunk rewrite to exact immutable source strings.

    A structured model can preserve the selected row number while changing one
    space or attaching a different row's prose.  The retry already contains
    the exact immutable fields for the rows it may retain.  Express those
    values as JSON-schema enums so the model itself must emit a byte-exact
    source binding.  Judge roles likewise have an explicit completeness
    contract: the analyst must account for the whole supplied positive roster
    and the skeptic for the whole supplied counter roster.  Bind only that
    role-required roster as one exact array so summarization cannot silently
    drop a member before the existing semantic completeness check runs.
    COMPONENT_RESEARCH source coverage is also bound to the exact labels
    supplied in that payload, so neither a chunk nor its synthesis can invent
    a stronger source family.  No citation, interpretation, or score is
    repaired by deterministic code.
    """

    base = _PROVIDER_SCHEMAS[pass_name]
    if pass_name == "SOURCE_CANDIDATE_RANKING":
        requested_source_families = list(
            dict.fromkeys(
                str(source_family).strip()
                for candidate in payload.get("discovery_candidates") or ()
                if isinstance(candidate, Mapping)
                for source_family in candidate.get(
                    "requested_source_families"
                )
                or ()
                if str(source_family).strip()
            )
        )
        if not requested_source_families:
            raise ValueError(
                "candidate ranking schema requires requested source families"
            )
        schema = json.loads(json.dumps(base, ensure_ascii=False))
        schema["properties"]["decisions"]["items"]["properties"][
            "matched_requested_source_family"
        ] = {
            "type": "string",
            "enum": ["NONE", *requested_source_families],
        }
        return schema
    if pass_name == "EVIDENCE_FACT_EXTRACTION" and isinstance(
        payload.get("fact_extraction_scope_contract"), Mapping
    ):
        contract = payload["fact_extraction_scope_contract"]
        if contract.get("mode") == "PRODUCTION_OBJECTIVE_LOCAL":
            document_objective_rows = contract.get(
                "document_objective_ids"
            )
            if isinstance(document_objective_rows, (str, bytes)) or not isinstance(
                document_objective_rows, Sequence
            ):
                raise ValueError(
                    "production fact schema requires document objective rows"
                )
            allowed_objective_ids = list(
                dict.fromkeys(
                    str(objective_id).strip()
                    for row in document_objective_rows
                    if isinstance(row, Mapping)
                    for objective_id in row.get("objective_ids") or ()
                    if str(objective_id).strip()
                )
            )
            if not allowed_objective_ids:
                raise ValueError(
                    "production fact schema requires objective ids"
                )
            schema = json.loads(json.dumps(base, ensure_ascii=False))
            fact_item = schema["properties"]["facts"]["items"]
            fact_item["required"].extend(
                ["objective_ids", "objective_relation"]
            )
            fact_item["properties"]["objective_ids"] = {
                "type": "array",
                "minItems": 1,
                "items": {
                    "type": "string",
                    "enum": allowed_objective_ids,
                },
            }
            fact_item["properties"]["objective_relation"] = {
                "type": "string",
                "enum": ["ADVANCE", "COUNTER", "SUPERSEDE"],
            }
            return schema
    if pass_name == "BUSINESS_MODEL_RESEARCH" and isinstance(
        payload.get("loss_accounted_fact_chunk_synthesis"), Mapping
    ):
        # Every loss-accounted fact chunk has already been reviewed before
        # this call.  Here ``research_complete`` means that synthesis covered
        # that full roster; unresolved economics remain in ``uncertainties``.
        # Bind the transport contract before the COMPONENT_RESEARCH-only
        # branch below so a business-model synthesis cannot mislabel
        # uncertainty as an unread fact plane.
        schema = json.loads(json.dumps(base, ensure_ascii=False))
        schema["properties"]["research_complete"] = {
            "type": "boolean",
            "enum": [True],
        }
        chunk_fact_row_sets = (
            _business_model_synthesis_chunk_fact_row_sets(payload)
        )
        if chunk_fact_row_sets:
            allowed_fact_row_indices = list(
                dict.fromkeys(
                    row_index
                    for _, row_indices in chunk_fact_row_sets
                    for row_index in row_indices
                )
            )
            # ``contains``/``allOf`` is not accepted by every local or Codex
            # strict-schema backend.  Position-bind one model-selected
            # representative per nonempty chunk instead.  Each enum contains
            # the complete selection made by that chunk's LLM response, so
            # deterministic code chooses no economic fact.  The model remains
            # free to choose any member of each enum and may append further
            # selected rows from the loss-accounted union.
            schema["properties"]["fact_row_indices"] = {
                "type": "array",
                "prefixItems": [
                    {
                        "type": "integer",
                        "enum": list(row_indices),
                    }
                    for _, row_indices in chunk_fact_row_sets
                ],
                "items": {
                    "type": "integer",
                    "enum": allowed_fact_row_indices,
                },
                "minItems": len(chunk_fact_row_sets),
            }
        return schema
    required_judge_roster = {
        "COMPONENT_ANALYST_JUDGE": (
            "allowed_support_fact_ids",
            "support_fact_ids",
        ),
        "COMPONENT_SKEPTIC_JUDGE": (
            "allowed_counter_fact_ids",
            "counter_fact_ids",
        ),
    }.get(pass_name)
    if required_judge_roster is not None:
        payload_field, response_field = required_judge_roster
        required_ids = [
            str(value)
            for value in payload.get(payload_field) or ()
            if isinstance(value, str) and value.strip()
        ]
        schema = json.loads(json.dumps(base, ensure_ascii=False))
        schema["properties"][response_field] = (
            {
                "type": "array",
                "prefixItems": [
                    {"type": "string", "enum": [fact_id]}
                    for fact_id in required_ids
                ],
                "items": {
                    "type": "string",
                    "enum": required_ids,
                },
                "minItems": len(required_ids),
                "maxItems": len(required_ids),
            }
            if required_ids
            else {
                "type": "array",
                "items": {"type": "string"},
                "maxItems": 0,
            }
        )
        if pass_name == "COMPONENT_SKEPTIC_JUDGE":
            allowed_support_ids = [
                str(value)
                for value in payload.get("allowed_support_fact_ids") or ()
                if isinstance(value, str) and value.strip()
            ]
            schema["properties"]["support_fact_ids"] = (
                {
                    "type": "array",
                    "items": {
                        "type": "string",
                        "enum": allowed_support_ids,
                    },
                }
                if allowed_support_ids
                else {
                    "type": "array",
                    "items": {"type": "string"},
                    "maxItems": 0,
                }
            )
        return schema
    if pass_name == "STAGE_GATE_FACT_MAPPING":
        allowed_row_indices = _payload_fact_row_indices(payload)
        schema = json.loads(json.dumps(base, ensure_ascii=False))
        if allowed_row_indices:
            mapping_indices = schema["properties"]["mappings"]["items"][
                "properties"
            ]["fact_row_indices"]
            mapping_indices["items"] = {
                "type": "integer",
                "enum": allowed_row_indices,
            }
            dispositions = schema["properties"]["fact_dispositions"]
            dispositions["minItems"] = len(allowed_row_indices)
            dispositions["maxItems"] = len(allowed_row_indices)
            dispositions["items"]["properties"]["fact_row_index"] = {
                "type": "integer",
                "enum": allowed_row_indices,
            }
        else:
            schema["properties"]["mappings"]["maxItems"] = 0
            schema["properties"]["fact_dispositions"]["maxItems"] = 0
        return schema
    if pass_name == "RED_TEAM_RESEARCH":
        allowed_row_indices: list[int] = []
        if isinstance(payload.get("loss_accounted_fact_chunk"), Mapping):
            allowed_row_indices = [
                int(row["fact_row_index"])
                for row in payload.get("current_evidence_fact_graph") or ()
                if isinstance(row, Mapping)
                and isinstance(row.get("fact_row_index"), int)
                and not isinstance(row.get("fact_row_index"), bool)
            ]
        synthesis = payload.get("loss_accounted_fact_chunk_synthesis")
        if isinstance(synthesis, Mapping):
            allowed_row_indices = [
                int(row_index)
                for chunk_response in synthesis.get("chunk_responses") or ()
                if isinstance(chunk_response, Mapping)
                for response in (chunk_response.get("response"),)
                if isinstance(response, Mapping)
                for row_index in response.get("challenged_fact_row_indices")
                or ()
                if isinstance(row_index, int)
                and not isinstance(row_index, bool)
            ]
        allowed_row_indices = list(dict.fromkeys(allowed_row_indices))
        schema = json.loads(json.dumps(base, ensure_ascii=False))
        challenged_schema = schema["properties"][
            "challenged_fact_row_indices"
        ]
        challenged_schema.pop("uniqueItems", None)
        if allowed_row_indices:
            challenged_schema["items"] = {
                "type": "integer",
                "enum": allowed_row_indices,
            }
        return schema
    if pass_name != "COMPONENT_RESEARCH":
        return base
    schema = json.loads(json.dumps(base, ensure_ascii=False))
    raw_source_coverage = payload.get("source_coverage")
    source_coverage_labels = sorted(
        _coverage_labels(raw_source_coverage)
        if isinstance(raw_source_coverage, Sequence)
        and not isinstance(raw_source_coverage, (str, bytes))
        else ()
    )
    schema["properties"]["source_coverage"] = (
        {
            "type": "array",
            "items": {
                "type": "string",
                "enum": source_coverage_labels,
            },
        }
        if source_coverage_labels
        else {
            "type": "array",
            "items": {"type": "string", "minLength": 1},
            "maxItems": 0,
        }
    )
    structured_metric_rows = payload.get("structured_metric_rows")
    if (
        isinstance(structured_metric_rows, Sequence)
        and not isinstance(structured_metric_rows, (str, bytes))
        and not isinstance(
            payload.get("loss_accounted_fact_chunk"), Mapping
        )
    ):
        structured_metric_row_indices: list[int] = []
        valid_structured_metric_roster = True
        for row in structured_metric_rows:
            row_index = (
                row.get("structured_metric_row_index")
                if isinstance(row, Mapping)
                else None
            )
            if (
                isinstance(row_index, bool)
                or not isinstance(row_index, int)
                or row_index < 0
                or row_index in structured_metric_row_indices
            ):
                valid_structured_metric_roster = False
                break
            structured_metric_row_indices.append(row_index)
        if valid_structured_metric_roster:
            schema["properties"]["structured_metric_row_indices"] = (
                {
                    "type": "array",
                    "prefixItems": [
                        {"type": "integer", "enum": [row_index]}
                        for row_index in structured_metric_row_indices
                    ],
                    "items": {
                        "type": "integer",
                        "enum": structured_metric_row_indices,
                    },
                    "minItems": len(structured_metric_row_indices),
                    "maxItems": len(structured_metric_row_indices),
                }
                if structured_metric_row_indices
                else {
                    "type": "array",
                    "items": {"type": "integer", "minimum": 0},
                    "maxItems": 0,
                }
            )
    retry = payload.get(
        "loss_accounted_fact_chunk_validation_retry_context"
    )
    if not isinstance(retry, Mapping):
        retry = payload.get("component_research_validation_retry_context")
    rows = (
        retry.get("expected_selected_fact_groundings")
        if isinstance(retry, Mapping)
        else None
    )
    if not rows:
        synthesis = payload.get("loss_accounted_fact_chunk_synthesis")
        if isinstance(synthesis, Mapping):
            rows = [
                grounding
                for chunk_response in synthesis.get("chunk_responses") or ()
                if isinstance(chunk_response, Mapping)
                for response in (chunk_response.get("response"),)
                if isinstance(response, Mapping)
                for grounding in response.get("selected_fact_groundings") or ()
                if isinstance(grounding, Mapping)
            ]
    if not rows and isinstance(
        payload.get("loss_accounted_fact_chunk"), Mapping
    ):
        rows = [
            {
                "fact_row_index": row_index,
                **grounding,
            }
            for row_index, grounding in (
                _expected_component_chunk_fact_groundings(payload).items()
            )
        ]
    if (
        not isinstance(rows, Sequence)
        or isinstance(rows, (str, bytes))
        or not rows
    ):
        return schema
    required_fields = (
        "source_predicate",
        "source_value_json",
        "source_period_json",
        "source_economic_mechanism",
    )
    normalized_rows: list[Mapping[str, Any]] = []
    for row in rows:
        if not isinstance(row, Mapping):
            return schema
        row_index = row.get("fact_row_index")
        if (
            isinstance(row_index, bool)
            or not isinstance(row_index, int)
            or row_index < 0
            or any(not str(row.get(field) or "") for field in required_fields)
        ):
            return schema
        normalized_rows.append(
            {
                "fact_row_index": row_index,
                **{field: str(row[field]) for field in required_fields},
            }
        )
    normalized_rows = list(
        {
            int(row["fact_row_index"]): row for row in normalized_rows
        }.values()
    )
    row_indices = [int(row["fact_row_index"]) for row in normalized_rows]
    properties = schema["properties"]
    properties["selected_fact_row_indices"]["items"] = {
        "type": "integer",
        "enum": row_indices,
    }
    grounding_item = properties["selected_fact_groundings"]["items"]
    component_interpretation_schema = grounding_item["properties"][
        "component_interpretation"
    ]
    grounding_variants = [
        {
            "type": "object",
            "additionalProperties": False,
            "required": list(grounding_item["required"]),
            "properties": {
                "fact_row_index": {
                    "type": "integer",
                    "enum": [int(row["fact_row_index"])],
                },
                **{
                    field: (
                        json.loads(
                            json.dumps(
                                grounding_item["properties"][field],
                                ensure_ascii=False,
                            )
                        )
                        if field
                        in {"source_value_json", "source_period_json"}
                        else {
                            "type": "string",
                            "enum": [str(row[field])],
                        }
                    )
                    for field in required_fields
                },
                "component_interpretation": (
                    component_interpretation_schema
                ),
            },
        }
        for row in normalized_rows
    ]
    properties["selected_fact_groundings"]["items"] = {
        "anyOf": grounding_variants
    }
    required_model_selected_indices: list[int] | None = None
    required_model_selected = (
        retry.get("required_model_selected_fact_row_indices")
        if isinstance(retry, Mapping)
        else None
    )
    if required_model_selected is not None:
        if (
            not isinstance(required_model_selected, Sequence)
            or isinstance(required_model_selected, (str, bytes))
            or not required_model_selected
            or any(
                isinstance(row_index, bool)
                or not isinstance(row_index, int)
                or row_index not in row_indices
                for row_index in required_model_selected
            )
            or len(required_model_selected)
            != len(set(required_model_selected))
        ):
            return schema
        required_model_selected_indices = [
            int(row_index) for row_index in required_model_selected
        ]
        grounding_by_index = {
            int(variant["properties"]["fact_row_index"]["enum"][0]): variant
            for variant in grounding_variants
        }
        properties["selected_fact_row_indices"] = {
            "type": "array",
            "prefixItems": [
                {"type": "integer", "enum": [row_index]}
                for row_index in required_model_selected_indices
            ],
            "items": {
                "type": "integer",
                "enum": row_indices,
            },
            "minItems": len(required_model_selected_indices),
            "maxItems": len(required_model_selected_indices),
        }
        properties["selected_fact_groundings"] = {
            "type": "array",
            "prefixItems": [
                grounding_by_index[row_index]
                for row_index in required_model_selected_indices
            ],
            "items": {"anyOf": grounding_variants},
            "minItems": len(required_model_selected_indices),
            "maxItems": len(required_model_selected_indices),
        }
    synthesis = payload.get("loss_accounted_fact_chunk_synthesis")
    chunk = payload.get("loss_accounted_fact_chunk")
    allowed_disposition_indices: list[int] | None = None
    if isinstance(synthesis, Mapping):
        allowed_disposition_indices = list(
            dict.fromkeys(
                int(disposition["fact_row_index"])
                for chunk_response in synthesis.get("chunk_responses") or ()
                if isinstance(chunk_response, Mapping)
                for response in (chunk_response.get("response"),)
                if isinstance(response, Mapping)
                for disposition in response.get("prior_fact_dispositions")
                or ()
                if isinstance(disposition, Mapping)
                and isinstance(disposition.get("fact_row_index"), int)
                and not isinstance(disposition.get("fact_row_index"), bool)
                and int(disposition["fact_row_index"]) >= 0
            )
        )
    elif isinstance(chunk, Mapping):
        prior_context = payload.get("prior_component_memo_context")
        allowed_disposition_indices = list(
            dict.fromkeys(
                int(row["fact_row_index"])
                for row in (
                    prior_context.get("current_fact_rows") or ()
                    if isinstance(prior_context, Mapping)
                    else ()
                )
                if isinstance(row, Mapping)
                and isinstance(row.get("fact_row_index"), int)
                and not isinstance(row.get("fact_row_index"), bool)
                and int(row["fact_row_index"]) >= 0
            )
        )
    if allowed_disposition_indices is not None:
        disposition_schema = properties["prior_fact_dispositions"]
        if allowed_disposition_indices:
            disposition_item = disposition_schema["items"]
            disposition_variants = []
            for row_index in allowed_disposition_indices:
                variant = json.loads(
                    json.dumps(disposition_item, ensure_ascii=False)
                )
                variant["properties"]["fact_row_index"] = {
                    "type": "integer",
                    "enum": [row_index],
                }
                if required_model_selected_indices is not None:
                    variant["properties"]["disposition"] = {
                        "type": "string",
                        "enum": [
                            "RETAIN"
                            if row_index
                            in required_model_selected_indices
                            else "OMIT"
                        ],
                    }
                disposition_variants.append(variant)
            # ``uniqueItems`` is not enforced by every local grammar backend.
            # Position-bind the complete prior roster as well, so duplicate
            # row ids cannot satisfy the exact-once completion contract by
            # merely filling the required array length. RETAIN/OMIT remains
            # unconstrained on the normal path. A semantic retry may bind it
            # to the rejected model's own selected/RETAIN decision so the
            # model cannot express that same decision inconsistently again.
            disposition_schema["prefixItems"] = disposition_variants
            disposition_schema["items"] = {
                "anyOf": disposition_variants,
            }
            disposition_schema["minItems"] = len(
                allowed_disposition_indices
            )
            disposition_schema["maxItems"] = len(
                allowed_disposition_indices
            )
        else:
            disposition_schema["maxItems"] = 0
    if isinstance(synthesis, Mapping):
        # At synthesis time all loss-accounted chunks are already present and
        # deterministic validation requires the model to review every one of
        # them.  ``research_complete`` therefore records review completion,
        # not whether the economic thesis is certain.  Keep uncertainty in
        # ``uncertainties`` instead of letting it reopen a fully reviewed leaf.
        properties["research_complete"] = {
            "type": "boolean",
            "enum": [True],
        }
    anchors = payload.get("historical_component_anchors")
    if (
        isinstance(synthesis, Mapping)
        and isinstance(anchors, Sequence)
        and not isinstance(anchors, (str, bytes))
    ):
        anchor_rows = [row for row in anchors if isinstance(row, Mapping)]
        anchor_ids = list(
            dict.fromkeys(
                str(row.get("anchor_id") or "").strip()
                for row in anchor_rows
                if str(row.get("anchor_id") or "").strip()
            )
        )
        positive_anchor_ids = [
            str(row["anchor_id"])
            for row in anchor_rows
            if str(row.get("anchor_id") or "") in anchor_ids
            and str(row.get("role") or "") == "POSITIVE"
        ]
        counter_anchor_ids = [
            str(row["anchor_id"])
            for row in anchor_rows
            if str(row.get("anchor_id") or "") in anchor_ids
            and str(row.get("role") or "") == "COUNTER"
        ]
        properties["historical_anchor_ids"] = {
            "type": "array",
            "items": (
                {"type": "string", "enum": anchor_ids}
                if anchor_ids
                else {"type": "string"}
            ),
            "minItems": len(anchor_ids),
            "maxItems": len(anchor_ids),
        }
        properties["nearest_positive_anchor_ids"] = {
            "type": "array",
            "items": (
                {"type": "string", "enum": positive_anchor_ids}
                if positive_anchor_ids
                else {"type": "string"}
            ),
            **({} if positive_anchor_ids else {"maxItems": 0}),
        }
        properties["nearest_counter_anchor_ids"] = {
            "type": "array",
            "items": (
                {"type": "string", "enum": counter_anchor_ids}
                if counter_anchor_ids
                else {"type": "string"}
            ),
            **({} if counter_anchor_ids else {"maxItems": 0}),
        }
    return schema


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
_COLLABORATION_RESPONSE_PENDING_RE = re.compile(
    r"^COLLABORATION_RESPONSE_PENDING:"
    r"(COLLABREQ-[0-9a-f]{64})$"
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
            )
        )

    @property
    def memo_fact_prompt_chunk_chars(self) -> int:
        """Keep Codex memo fact chunks comfortably below its prompt gate."""

        return 250_000

    @property
    def prompt_transport_max_chars(self) -> int:
        """Strict upper bound used while materializing Stage fact chunks."""

        return _CODEX_PROMPT_TRANSPORT_MAX_CHARS

    @property
    def candidate_ranking_page_candidate_limit(self) -> int:
        """Match every provider ranking page to the shared output schema."""

        return CANDIDATE_RANKING_PAGE_CANDIDATE_LIMIT

    def _normalize_loss_accounted_response(
        self,
        *,
        pass_name: str,
        response: Mapping[str, Any],
    ) -> Mapping[str, Any]:
        del pass_name
        return response

    def complete(
        self, *, pass_name: str, payload: Mapping[str, Any]
    ) -> Mapping[str, Any]:
        """Review every fact through a shared loss-accounted chunk contract."""

        if pass_name not in _LOSS_ACCOUNTED_FACT_CHUNK_PASSES:
            return self._complete_single_payload(
                pass_name=pass_name,
                payload=payload,
            )
        if (
            "loss_accounted_fact_chunk" in payload
            or "loss_accounted_fact_chunk_synthesis" in payload
        ):
            return self._normalize_loss_accounted_response(
                pass_name=pass_name,
                response=self._complete_single_payload(
                    pass_name=pass_name,
                    payload=payload,
                ),
            )
        chunks = (
            _materialize_stage_gate_fact_chunks(
                payload,
                target_projection_chars=self.memo_fact_prompt_chunk_chars,
                max_prompt_chars=self.prompt_transport_max_chars,
            )
            if pass_name == "STAGE_GATE_FACT_MAPPING"
            else _loss_accounted_fact_chunk_payloads(
                payload,
                pass_name=pass_name,
                target_projection_chars=self.memo_fact_prompt_chunk_chars,
            )
        )
        if len(chunks) <= 1:
            return self._normalize_loss_accounted_response(
                pass_name=pass_name,
                response=self._complete_single_payload(
                    pass_name=pass_name,
                    payload=payload,
                ),
            )

        chunk_responses = []
        collaboration_pending_request_ids: list[str] = []
        for chunk in chunks:
            local_to_global = tuple(
                int(value)
                for value in chunk["loss_accounted_fact_chunk"][
                    "global_fact_row_index_by_chunk_local_index"
                ]
            )
            allowed_indices = {
                int(row["fact_row_index"])
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
            expected_component_groundings = (
                _expected_component_chunk_fact_groundings(chunk)
                if pass_name == "COMPONENT_RESEARCH"
                else {}
            )
            expected_stage_directions = (
                _stage_gate_chunk_fact_directions(chunk)
                if pass_name == "STAGE_GATE_FACT_MAPPING"
                else {}
            )
            allowed_stage_primitives = {
                str(value)
                for value in (
                    (chunk.get("evidence_contract") or {}).get(
                        "allowed_primitive_ids"
                    )
                    or ()
                )
                if str(value).strip()
            }
            attempt_payload = chunk
            validation_retry_used = False
            chunk_collaboration_pending = False
            while True:
                try:
                    response = self._normalize_loss_accounted_response(
                        pass_name=pass_name,
                        response=self._complete_single_payload(
                            pass_name=pass_name,
                            payload=attempt_payload,
                        ),
                    )
                except StructuredProviderUnavailable as exc:
                    pending_request_id = (
                        _collaboration_pending_request_id(exc)
                    )
                    if (
                        pass_name == "STAGE_GATE_FACT_MAPPING"
                        and pending_request_id is not None
                    ):
                        collaboration_pending_request_ids.append(
                            pending_request_id
                        )
                        chunk_collaboration_pending = True
                        break
                    raise
                try:
                    _validate_loss_accounted_chunk_response(
                        pass_name=pass_name,
                        response=response,
                        allowed_fact_row_indices=allowed_indices,
                        prior_fact_row_indices=prior_indices,
                        expected_component_groundings=(
                            expected_component_groundings
                        ),
                        expected_stage_directions=(
                            expected_stage_directions
                        ),
                        allowed_stage_primitives=(
                            allowed_stage_primitives
                        ),
                    )
                    break
                except StructuredProviderRejected as exc:
                    self.invalidate_last_response_cache(str(exc))
                    if validation_retry_used:
                        raise
                    validation_retry_used = True
                    rejected_selected_groundings = (
                        _selected_expected_chunk_grounding_rows(
                            response=response,
                            expected_groundings=(
                                expected_component_groundings
                            ),
                        )
                    )
                    expected_retry_groundings = (
                        _all_expected_chunk_grounding_rows(
                            expected_groundings=(
                                expected_component_groundings
                            ),
                        )
                    )
                    attempt_payload = scrub_blind_research_payload(
                        {
                            **chunk,
                            "loss_accounted_fact_chunk_validation_retry_context": {
                                "validation_error": str(exc),
                                "allowed_fact_row_indices": sorted(
                                    allowed_indices
                                ),
                                "required_prior_fact_row_indices": sorted(
                                    prior_indices
                                ),
                                "expected_selected_fact_groundings": (
                                    expected_retry_groundings
                                ),
                                "rejected_selected_fact_row_indices": (
                                    [
                                        int(row["fact_row_index"])
                                        for row in rejected_selected_groundings
                                    ]
                                ),
                                "instruction": (
                                    (
                                        "Write the complete Stage chunk response "
                                        "again. Use only allowed_fact_row_indices, "
                                        "match SUPPORT to POSITIVE and COUNTER to "
                                        "COUNTER, and return every allowed row "
                                        "exactly once in fact_dispositions as "
                                        "MAPPED, NO_MATCH, or UNRESOLVED. Do not "
                                        "invent evidence, score, or Stage."
                                    )
                                    if pass_name
                                    == "STAGE_GATE_FACT_MAPPING"
                                    else (
                                        "Write the complete chunk response again "
                                        "from the supplied source table, not from "
                                        "the prior rejected answer, which is "
                                        "intentionally omitted to prevent copying "
                                        "its bad row binding. Cite only "
                                        "allowed_fact_row_indices. For a component "
                                        "chunk, return one exact grounding per "
                                        "selected row by copying the immutable "
                                        "fields for that row from the complete "
                                        "expected_selected_fact_groundings table, "
                                        "and dispose every required prior row "
                                        "exactly once. If a selected row does not "
                                        "support the component, omit it instead of "
                                        "attaching another row's semantics. Do not "
                                        "invent evidence, score, or Stage."
                                    )
                                ),
                            },
                        }
                    )
            if chunk_collaboration_pending:
                continue
            response = _restore_loss_accounted_chunk_global_indices(
                pass_name=pass_name,
                response=response,
                local_to_global=local_to_global,
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

        if collaboration_pending_request_ids:
            raise StructuredProviderUnavailable(
                "COLLABORATION_RESPONSE_PENDING:"
                + ":".join(
                    dict.fromkeys(collaboration_pending_request_ids)
                )
            )

        if pass_name == "STAGE_GATE_FACT_MAPPING":
            return _merge_stage_gate_chunk_responses(
                chunks=chunks,
                chunk_responses=chunk_responses,
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
            response = self._normalize_loss_accounted_response(
                pass_name=pass_name,
                response=self._complete_single_payload(
                    pass_name=pass_name,
                    payload=attempt_payload,
                ),
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

    def _complete_single_payload(
        self, *, pass_name: str, payload: Mapping[str, Any]
    ) -> Mapping[str, Any]:
        (
            safe_payload,
            output_schema,
            prompt,
            prompt_hash,
            schema_hash,
        ) = _single_payload_request_material(
            pass_name=pass_name,
            payload=payload,
        )
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
                output_schema=output_schema,
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

    def preview_prompt_hash(
        self,
        *,
        pass_name: str,
        payload: Mapping[str, Any],
    ) -> str:
        """Return the exact single-payload prompt hash without transport I/O."""

        return _single_payload_request_material(
            pass_name=pass_name,
            payload=payload,
        )[3]

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
            if existed:
                quarantine_root = path.parent / "_invalidated"
                quarantine_root.mkdir(parents=True, exist_ok=True)
                quarantine_path = quarantine_root / path.name
                path.replace(quarantine_path)
                reason_path = quarantine_root / (
                    f"{path.stem}.reason.json"
                )
                reason_temporary = reason_path.with_suffix(
                    reason_path.suffix + ".tmp"
                )
                reason_temporary.write_text(
                    json.dumps(
                        {
                            "schema_version": (
                                "e2r_v5_invalidated_provider_response_v1"
                            ),
                            "pass_name": pass_name,
                            "prompt_hash": latest.get("prompt_hash"),
                            "cache_key": cache_key,
                            "reason": clean_reason,
                            "quarantined_response_path": str(
                                quarantine_path
                            ),
                            "production_score_authority": False,
                            "reusable_provider_response": False,
                        },
                        ensure_ascii=False,
                        sort_keys=True,
                        indent=2,
                    )
                    + "\n",
                    encoding="utf-8",
                )
                reason_temporary.replace(reason_path)
                event["quarantined_response_path"] = str(
                    quarantine_path
                )
                event["quarantine_reason_path"] = str(reason_path)
            else:
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
            "invalidated_response_quarantine_is_score_authority": False,
            "invalidated_response_quarantine_is_reusable_cache": False,
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
            "provider_contract": "CODEX_CLI_FIXED",
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


_LOSS_ACCOUNTED_FACT_CHUNK_PASSES = {
    "BUSINESS_MODEL_RESEARCH",
    "COMPONENT_RESEARCH",
    "RED_TEAM_RESEARCH",
    "STAGE_GATE_FACT_MAPPING",
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
        projected_rows, projected, local_to_global = _remap_citable_fact_chunk(
            group,
            fields=fields,
            dictionaries=dictionaries,
            global_projection=projection,
            global_fact_row_indices=row_indices,
        )
        allowed_indices = {int(row[0]) for row in projected_rows}
        global_to_local = {
            global_index: local_index
            for local_index, global_index in enumerate(local_to_global)
        }
        chunk_payload = {
            key: value
            for key, value in dict(payload).items()
            if key not in _FACT_CHUNK_SYNTHESIS_ONLY_KEYS
        }
        # Keep the citation key structurally separate from dictionary-coded
        # fact values.  With a bare numeric row such as ``[0, 12, 3, ...]``, a
        # structured model can copy the whole encoded row into
        # ``fact_row_indices`` even though only the first cell is a citation.
        # Naming that cell removes the ambiguity without sampling, rewriting,
        # or otherwise changing any fact semantics.
        chunk_payload["current_evidence_fact_graph"] = [
            {
                "fact_row_index": int(row[0]),
                "encoded_fact_values": list(row[1:]),
            }
            for row in projected_rows
        ]
        chunk_payload["current_evidence_fact_projection"] = {
            **projected,
            "chunk_fact_row_encoding": {
                "schema_version": "e2r_v5_named_fact_row_encoding_v1",
                "fact_row_index_field": "fact_row_index",
                "encoded_fact_values_field": "encoded_fact_values",
                "encoded_fact_value_fields": list(fields[1:]),
                "citation_cell_is_not_part_of_encoded_fact_values": True,
            },
        }
        _filter_fact_row_context_for_chunk(
            chunk_payload,
            global_to_local=global_to_local,
        )
        chunk_row_indices = sorted(allowed_indices)
        chunk_payload["loss_accounted_fact_chunk"] = {
            "schema_version": "e2r_v5_loss_accounted_fact_chunk_v1",
            "pass_name": pass_name,
            "chunk_index": chunk_index,
            "chunk_count": len(groups),
            "chunk_fact_count": len(group),
            "chunk_fact_row_index_roster_hash": _canonical_json_hash(
                list(local_to_global)
            ),
            "chunk_local_fact_row_index_roster_hash": _canonical_json_hash(
                chunk_row_indices
            ),
            "citation_index_semantics": "CHUNK_LOCAL_FACT_ROW_INDEX",
            "global_fact_row_index_by_chunk_local_index": list(
                local_to_global
            ),
            "global_fact_count": len(normalized_rows),
            "global_fact_row_index_roster_hash": global_index_hash,
            "every_global_fact_assigned_to_exactly_one_chunk": True,
            "fixed_top_n_used": False,
            "prompt_projection_is_research_cap": False,
            "score_authority": False,
            "instruction": (
                "Review every supplied fact row in this chunk. Each row names "
                "its chunk-local citation in fact_row_index; encoded_fact_values "
                "align positionally with encoded_fact_value_fields and are never "
                "citation indices. Cite only the named fact_row_index value; "
                "deterministic transport restores its immutable global index. "
                "Treat research_complete "
                "or review_complete as completion of this chunk only. Return the "
                "normal pass schema and cite only rows in this chunk. Do not infer "
                "global completeness, score, or Stage from one chunk."
            ),
        }
        chunks.append(scrub_blind_research_payload(chunk_payload))

    emitted = [
        int(global_index)
        for chunk in chunks
        for global_index in chunk["loss_accounted_fact_chunk"][
            "global_fact_row_index_by_chunk_local_index"
        ]
    ]
    if emitted != row_indices or len(emitted) != len(set(emitted)):
        raise ValueError("loss-accounted fact chunks changed the global row roster")
    return tuple(chunks)


def _payload_fact_row_indices(
    payload: Mapping[str, Any],
) -> list[int]:
    """Return the exact citable row roster from full or chunk transport."""

    raw_rows = payload.get("current_evidence_fact_graph")
    if not isinstance(raw_rows, Sequence) or isinstance(
        raw_rows, (str, bytes)
    ):
        return []
    result: list[int] = []
    for row in raw_rows:
        value = (
            row.get("fact_row_index")
            if isinstance(row, Mapping)
            else row[0]
            if isinstance(row, Sequence)
            and not isinstance(row, (str, bytes))
            and row
            else None
        )
        if (
            isinstance(value, bool)
            or not isinstance(value, int)
            or value < 0
            or value in result
        ):
            raise ValueError("provider payload fact row roster is invalid")
        result.append(value)
    return result


def _materialize_stage_gate_fact_chunks(
    payload: Mapping[str, Any],
    *,
    target_projection_chars: int,
    max_prompt_chars: int,
) -> tuple[Mapping[str, Any], ...]:
    """Build every exhaustive Stage chunk and verify its actual prompt size.

    The regular fact chunker estimates row transport weight to form useful
    batches. StageCourt additionally validates the fully rendered prompt before
    any provider call. If shared contract or lineage context makes a batch too
    large, the target is reduced and the complete roster is repartitioned. No
    row is sampled, capped, or removed.
    """

    if max_prompt_chars < 10_000:
        raise ValueError("Stage gate prompt budget is too small")
    target = max(10_000, int(target_projection_chars))
    prior_partition: tuple[tuple[int, ...], ...] | None = None
    while True:
        chunks = _loss_accounted_fact_chunk_payloads(
            payload,
            pass_name="STAGE_GATE_FACT_MAPPING",
            target_projection_chars=target,
        )
        prompt_lengths = tuple(
            len(
                _single_payload_request_material(
                    pass_name="STAGE_GATE_FACT_MAPPING",
                    payload=chunk,
                )[2]
            )
            for chunk in chunks
        )
        if all(length < max_prompt_chars for length in prompt_lengths):
            return chunks
        partition = tuple(
            tuple(
                int(value)
                for value in (
                    (
                        chunk.get("loss_accounted_fact_chunk") or {}
                    ).get("global_fact_row_index_by_chunk_local_index")
                    or _payload_fact_row_indices(chunk)
                )
            )
            for chunk in chunks
        )
        if any(
            length >= max_prompt_chars and len(row_indices) <= 1
            for length, row_indices in zip(prompt_lengths, partition)
        ):
            raise StructuredProviderRejected(
                "stage_gate_single_fact_prompt_exceeds_transport_budget"
            )
        next_target = max(10_000, target * 3 // 4)
        if next_target == target or partition == prior_partition:
            next_target = max(10_000, target // 2)
        if next_target == target:
            raise StructuredProviderRejected(
                "stage_gate_fact_prompt_cannot_fit_transport_budget"
            )
        prior_partition = partition
        target = next_target


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
) -> tuple[list[list[Any]], Mapping[str, Any], tuple[int, ...]]:
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
    local_to_global = tuple(int(row[0]) for row in rows)
    for local_index, row in enumerate(rows):
        projected_rows.append(
            [
                local_index,
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
            "global_row_indices_preserved_in_chunk": False,
            "chunk_local_citation_indices_used": True,
            "full_fact_records_persisted_outside_prompt": True,
            "fixed_top_n_used": False,
            "prompt_projection_is_research_cap": False,
            "score_authority": False,
        }
    )
    return projected_rows, projected, local_to_global


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
    payload: dict[str, Any], *, global_to_local: Mapping[int, int]
) -> None:
    counters = payload.get("current_counterfacts")
    if isinstance(counters, Sequence) and not isinstance(counters, (str, bytes)):
        payload["current_counterfacts"] = [
            {
                **dict(row),
                "fact_row_index": global_to_local[int(row["fact_row_index"])],
            }
            for row in counters
            if isinstance(row, Mapping)
            and isinstance(row.get("fact_row_index"), int)
            and int(row["fact_row_index"]) in global_to_local
        ]
    prior = payload.get("prior_component_memo_context")
    if isinstance(prior, Mapping):
        projected = dict(prior)
        rows = [
            {
                **dict(row),
                "fact_row_index": global_to_local[int(row["fact_row_index"])],
            }
            for row in projected.get("current_fact_rows") or ()
            if isinstance(row, Mapping)
            and isinstance(row.get("fact_row_index"), int)
            and int(row["fact_row_index"]) in global_to_local
        ]
        projected["current_fact_rows"] = rows
        projected["current_fact_row_count"] = len(rows)
        projected["available"] = bool(rows)
        projected["prior_fact_dispositions_required"] = bool(rows)
        projected["required_prior_fact_disposition_count"] = len(rows)
        projected["unavailable_prior_facts_are_hash_only_not_dispositions"] = True
        projected["chunk_scoped_current_fact_rows"] = True
        payload["prior_component_memo_context"] = projected


def _restore_loss_accounted_chunk_global_indices(
    *,
    pass_name: str,
    response: Mapping[str, Any],
    local_to_global: Sequence[int],
) -> Mapping[str, Any]:
    """Restore intermediate chunk-local citations before global synthesis."""

    def restore(value: Any) -> int:
        if (
            isinstance(value, bool)
            or not isinstance(value, int)
            or value < 0
            or value >= len(local_to_global)
        ):
            raise StructuredProviderRejected(
                "loss_accounted_fact_chunk_local_index_out_of_range"
            )
        return int(local_to_global[value])

    result = dict(response)
    if pass_name == "STAGE_GATE_FACT_MAPPING":
        result["mappings"] = [
            {
                **dict(row),
                "fact_row_indices": [
                    restore(value)
                    for value in row.get("fact_row_indices") or ()
                ],
            }
            for row in response.get("mappings") or ()
            if isinstance(row, Mapping)
        ]
        result["fact_dispositions"] = [
            {
                **dict(row),
                "fact_row_index": restore(row.get("fact_row_index")),
            }
            for row in response.get("fact_dispositions") or ()
            if isinstance(row, Mapping)
        ]
        return result
    citation_field = {
        "BUSINESS_MODEL_RESEARCH": "fact_row_indices",
        "COMPONENT_RESEARCH": "selected_fact_row_indices",
        "RED_TEAM_RESEARCH": "challenged_fact_row_indices",
    }[pass_name]
    result[citation_field] = [
        restore(value) for value in result.get(citation_field) or ()
    ]
    if pass_name == "COMPONENT_RESEARCH":
        for field in ("selected_fact_groundings", "prior_fact_dispositions"):
            result[field] = [
                {
                    **dict(row),
                    "fact_row_index": restore(row.get("fact_row_index")),
                }
                for row in result.get(field) or ()
                if isinstance(row, Mapping)
            ]
    return result


def _merge_stage_gate_chunk_responses(
    *,
    chunks: Sequence[Mapping[str, Any]],
    chunk_responses: Sequence[Mapping[str, Any]],
) -> Mapping[str, Any]:
    """Deterministically union exhaustive Stage chunk judgments."""

    if len(chunks) != len(chunk_responses) or not chunks:
        raise StructuredProviderRejected(
            "stage_gate_chunk_response_count_mismatch"
        )
    expected_global = [
        int(value)
        for chunk in chunks
        for value in (
            (chunk.get("loss_accounted_fact_chunk") or {}).get(
                "global_fact_row_index_by_chunk_local_index"
            )
            or ()
        )
    ]
    if not expected_global:
        raise StructuredProviderRejected(
            "stage_gate_chunk_global_roster_missing"
        )
    if len(expected_global) != len(set(expected_global)):
        raise StructuredProviderRejected(
            "stage_gate_chunk_global_roster_duplicate"
        )

    mappings: dict[tuple[str, str], dict[str, Any]] = {}
    dispositions: dict[int, Mapping[str, Any]] = {}
    unresolved: set[str] = set()
    complete = True
    for chunk_response in chunk_responses:
        response = chunk_response.get("response")
        if not isinstance(response, Mapping):
            raise StructuredProviderRejected(
                "stage_gate_chunk_response_missing"
            )
        complete = complete and response.get("mapping_complete") is True
        unresolved.update(
            str(value).strip()
            for value in response.get("unresolved_material_questions") or ()
            if str(value).strip()
        )
        for raw in response.get("mappings") or ():
            if not isinstance(raw, Mapping):
                raise StructuredProviderRejected(
                    "stage_gate_chunk_mapping_not_object"
                )
            key = (
                str(raw.get("primitive_id") or ""),
                str(raw.get("direction") or ""),
            )
            state = mappings.setdefault(
                key,
                {
                    "fact_row_indices": set(),
                    "semantic_rationales": set(),
                },
            )
            state["fact_row_indices"].update(
                _stage_gate_mapping_fact_row_indices(raw)
            )
            rationale = str(raw.get("semantic_rationale") or "").strip()
            if rationale:
                state["semantic_rationales"].add(rationale)
        for raw in response.get("fact_dispositions") or ():
            if not isinstance(raw, Mapping):
                raise StructuredProviderRejected(
                    "stage_gate_chunk_disposition_not_object"
                )
            row_index = raw.get("fact_row_index")
            if (
                isinstance(row_index, bool)
                or not isinstance(row_index, int)
                or row_index < 0
                or row_index in dispositions
            ):
                raise StructuredProviderRejected(
                    "stage_gate_chunk_disposition_global_duplicate"
                )
            dispositions[row_index] = dict(raw)

    if set(expected_global) != set(dispositions):
        raise StructuredProviderRejected(
            "stage_gate_chunk_disposition_global_roster_mismatch"
        )
    merged_mappings = [
        {
            "primitive_id": primitive_id,
            "direction": direction,
            "fact_row_indices": sorted(state["fact_row_indices"]),
            "semantic_rationale": " | ".join(
                sorted(state["semantic_rationales"])
            ),
        }
        for (primitive_id, direction), state in sorted(mappings.items())
    ]
    merged_dispositions = [
        dict(dispositions[row_index])
        for row_index in sorted(dispositions)
    ]
    return {
        "mappings": merged_mappings,
        "fact_dispositions": merged_dispositions,
        "unresolved_material_questions": sorted(unresolved),
        "mapping_complete": bool(
            complete
            and not unresolved
            and all(
                row.get("status") != "UNRESOLVED"
                for row in merged_dispositions
            )
        ),
    }


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
    expected_component_groundings: Mapping[int, Mapping[str, Any]],
    expected_stage_directions: Mapping[int, str] | None = None,
    allowed_stage_primitives: set[str] | None = None,
) -> None:
    if pass_name == "STAGE_GATE_FACT_MAPPING":
        _validate_stage_gate_fact_response(
            response=response,
            allowed_fact_row_indices=allowed_fact_row_indices,
            expected_directions=expected_stage_directions or {},
            allowed_primitives=allowed_stage_primitives or set(),
        )
        return
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
    groundings = {
        int(row["fact_row_index"]): row
        for row in response.get("selected_fact_groundings") or ()
        if isinstance(row, Mapping)
        and isinstance(row.get("fact_row_index"), int)
        and not isinstance(row.get("fact_row_index"), bool)
    }
    immutable_fields = (
        "source_predicate",
        "source_value_json",
        "source_period_json",
        "source_economic_mechanism",
    )
    for row_index, grounding in groundings.items():
        expected = expected_component_groundings.get(row_index)
        if expected is None:
            raise StructuredProviderRejected(
                "loss_accounted_fact_chunk_grounding_fact_row_unavailable"
            )
        for field in immutable_fields:
            if str(grounding.get(field)) != str(expected[field]):
                raise StructuredProviderRejected(
                    "loss_accounted_fact_chunk_grounding_"
                    f"{field}_mismatch"
                )
    disposition_indices = _mapping_fact_row_indices(
        response.get("prior_fact_dispositions") or ()
    )
    if disposition_indices != prior_fact_row_indices:
        raise StructuredProviderRejected(
            "loss_accounted_fact_chunk_prior_disposition_roster_mismatch"
        )


def _stage_gate_chunk_fact_directions(
    chunk: Mapping[str, Any],
) -> Mapping[int, str]:
    """Decode the immutable direction attached to every Stage chunk row."""

    decoded = _decode_chunk_fact_rows(chunk)
    result: dict[int, str] = {}
    for row_index, row in decoded.items():
        direction = str(row.get("direction") or "")
        if direction not in {"POSITIVE", "COUNTER"}:
            raise ValueError(
                "Stage gate chunk contains a non-mappable fact direction"
            )
        result[row_index] = direction
    return result


def _validate_stage_gate_fact_response(
    *,
    response: Mapping[str, Any],
    allowed_fact_row_indices: set[int],
    expected_directions: Mapping[int, str],
    allowed_primitives: set[str],
) -> None:
    """Require exactly one terminal disposition for every supplied fact row."""

    if set(expected_directions) != allowed_fact_row_indices:
        raise StructuredProviderRejected(
            "stage_gate_expected_direction_roster_mismatch"
        )
    raw_mappings = response.get("mappings")
    if not isinstance(raw_mappings, Sequence) or isinstance(
        raw_mappings, (str, bytes)
    ):
        raise StructuredProviderRejected("stage_gate_mappings_not_array")
    mapped: set[int] = set()
    mapping_keys: set[tuple[str, str]] = set()
    for raw in raw_mappings:
        if not isinstance(raw, Mapping):
            raise StructuredProviderRejected("stage_gate_mapping_not_object")
        primitive_id = str(raw.get("primitive_id") or "").strip()
        direction = str(raw.get("direction") or "").strip()
        rationale = str(raw.get("semantic_rationale") or "").strip()
        if primitive_id not in allowed_primitives:
            raise StructuredProviderRejected(
                "stage_gate_mapping_unknown_primitive"
            )
        if direction not in {"SUPPORT", "COUNTER"}:
            raise StructuredProviderRejected(
                "stage_gate_mapping_unknown_direction"
            )
        if not rationale:
            raise StructuredProviderRejected(
                "stage_gate_mapping_rationale_missing"
            )
        key = (primitive_id, direction)
        if key in mapping_keys:
            raise StructuredProviderRejected(
                "stage_gate_mapping_duplicate_primitive_direction"
            )
        mapping_keys.add(key)
        indices = _stage_gate_mapping_fact_row_indices(raw)
        if not indices:
            raise StructuredProviderRejected(
                "stage_gate_mapping_fact_rows_empty"
            )
        if not indices.issubset(allowed_fact_row_indices):
            raise StructuredProviderRejected(
                "stage_gate_mapping_fact_row_outside_chunk"
            )
        expected = "POSITIVE" if direction == "SUPPORT" else "COUNTER"
        if any(expected_directions[index] != expected for index in indices):
            raise StructuredProviderRejected(
                "stage_gate_mapping_fact_direction_mismatch"
            )
        mapped.update(indices)

    raw_dispositions = response.get("fact_dispositions")
    if not isinstance(raw_dispositions, Sequence) or isinstance(
        raw_dispositions, (str, bytes)
    ):
        raise StructuredProviderRejected(
            "stage_gate_fact_dispositions_not_array"
        )
    disposition_status: dict[int, str] = {}
    unresolved_disposition = False
    for raw in raw_dispositions:
        if not isinstance(raw, Mapping):
            raise StructuredProviderRejected(
                "stage_gate_fact_disposition_not_object"
            )
        row_index = raw.get("fact_row_index")
        status = str(raw.get("status") or "")
        rationale = str(raw.get("rationale") or "").strip()
        if (
            isinstance(row_index, bool)
            or not isinstance(row_index, int)
            or row_index < 0
            or row_index not in allowed_fact_row_indices
        ):
            raise StructuredProviderRejected(
                "stage_gate_fact_disposition_outside_chunk"
            )
        if row_index in disposition_status:
            raise StructuredProviderRejected(
                "stage_gate_fact_disposition_duplicate"
            )
        if status not in {"MAPPED", "NO_MATCH", "UNRESOLVED"}:
            raise StructuredProviderRejected(
                "stage_gate_fact_disposition_status_invalid"
            )
        if not rationale:
            raise StructuredProviderRejected(
                "stage_gate_fact_disposition_rationale_missing"
            )
        if (status == "MAPPED") != (row_index in mapped):
            raise StructuredProviderRejected(
                "stage_gate_fact_disposition_mapping_mismatch"
            )
        unresolved_disposition = (
            unresolved_disposition or status == "UNRESOLVED"
        )
        disposition_status[row_index] = status
    if set(disposition_status) != allowed_fact_row_indices:
        raise StructuredProviderRejected(
            "stage_gate_fact_disposition_roster_mismatch"
        )

    unresolved_questions = response.get("unresolved_material_questions")
    if not isinstance(unresolved_questions, Sequence) or isinstance(
        unresolved_questions, (str, bytes)
    ) or any(not str(value).strip() for value in unresolved_questions):
        raise StructuredProviderRejected(
            "stage_gate_unresolved_material_questions_invalid"
        )
    if response.get("mapping_complete") is True and (
        unresolved_disposition or unresolved_questions
    ):
        raise StructuredProviderRejected(
            "stage_gate_mapping_complete_contradicts_unresolved"
        )


def _stage_gate_mapping_fact_row_indices(
    row: Mapping[str, Any],
) -> set[int]:
    values = row.get("fact_row_indices")
    if not isinstance(values, Sequence) or isinstance(values, (str, bytes)):
        raise StructuredProviderRejected(
            "stage_gate_mapping_fact_rows_not_array"
        )
    result: set[int] = set()
    for value in values:
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise StructuredProviderRejected(
                "stage_gate_mapping_fact_row_invalid"
            )
        if value in result:
            raise StructuredProviderRejected(
                "stage_gate_mapping_fact_row_duplicate"
            )
        result.add(value)
    return result


def _decode_chunk_fact_rows(
    chunk: Mapping[str, Any],
) -> Mapping[int, Mapping[str, Any]]:
    """Decode every dictionary-coded chunk row without changing semantics."""

    projection = chunk.get("current_evidence_fact_projection")
    rows = chunk.get("current_evidence_fact_graph")
    if (
        not isinstance(projection, Mapping)
        or not isinstance(rows, Sequence)
        or isinstance(rows, (str, bytes))
    ):
        raise ValueError("fact chunk projection is unavailable")
    encoding = projection.get("chunk_fact_row_encoding")
    dictionaries = projection.get("fact_value_dictionaries")
    if not isinstance(encoding, Mapping) or not isinstance(
        dictionaries, Mapping
    ):
        raise ValueError("fact chunk encoding is unavailable")
    fields = tuple(
        str(value)
        for value in encoding.get("encoded_fact_value_fields") or ()
    )
    decoded_by_row: dict[int, Mapping[str, Any]] = {}
    for row in rows:
        if not isinstance(row, Mapping):
            raise ValueError("fact chunk row must be an object")
        row_index = row.get("fact_row_index")
        encoded_values = row.get("encoded_fact_values")
        if (
            isinstance(row_index, bool)
            or not isinstance(row_index, int)
            or row_index < 0
            or not isinstance(encoded_values, Sequence)
            or isinstance(encoded_values, (str, bytes))
            or len(encoded_values) != len(fields)
            or row_index in decoded_by_row
        ):
            raise ValueError("fact chunk row encoding is invalid")
        decoded: dict[str, Any] = {}
        for field, dictionary_index in zip(fields, encoded_values):
            if not field.endswith("_dictionary_index"):
                raise ValueError("fact chunk field is not encoded")
            dictionary_name = field[: -len("_dictionary_index")]
            dictionary = dictionaries.get(dictionary_name)
            if (
                not isinstance(dictionary, Sequence)
                or isinstance(dictionary, (str, bytes))
                or isinstance(dictionary_index, bool)
                or not isinstance(dictionary_index, int)
                or dictionary_index < 0
                or dictionary_index >= len(dictionary)
            ):
                raise ValueError("fact chunk dictionary index is invalid")
            decoded[dictionary_name] = dictionary[dictionary_index]
        decoded_by_row[row_index] = decoded
    return decoded_by_row


def _expected_component_chunk_fact_groundings(
    chunk: Mapping[str, Any],
) -> Mapping[int, Mapping[str, Any]]:
    """Decode immutable grounding fields for each chunk-local fact row."""

    decoded_by_row = _decode_chunk_fact_rows(chunk)
    result: dict[int, Mapping[str, Any]] = {}
    for row_index, decoded in decoded_by_row.items():
        required = {"predicate", "value", "period", "economic_mechanism"}
        if not required.issubset(decoded):
            raise ValueError("component fact chunk grounding fields are missing")
        result[row_index] = {
            "source_predicate": decoded["predicate"],
            "source_value_json": _canonical_fact_field_json(decoded["value"]),
            "source_period_json": _canonical_fact_field_json(decoded["period"]),
            "source_economic_mechanism": decoded["economic_mechanism"],
        }
    return result


def _selected_expected_chunk_grounding_rows(
    *,
    response: Any,
    expected_groundings: Mapping[int, Mapping[str, Any]],
) -> list[Mapping[str, Any]]:
    """Expose exact selected source fields to the bounded chunk rewrite."""

    if not isinstance(response, Mapping):
        return []
    selected = response.get("selected_fact_row_indices")
    if isinstance(selected, (str, bytes)) or not isinstance(selected, Sequence):
        return []
    result = []
    seen: set[int] = set()
    for row_index in selected:
        if (
            isinstance(row_index, bool)
            or not isinstance(row_index, int)
            or row_index < 0
            or row_index in seen
            or row_index not in expected_groundings
        ):
            continue
        seen.add(row_index)
        result.append(
            {
                "fact_row_index": row_index,
                **expected_groundings[row_index],
            }
        )
    return result


def _all_expected_chunk_grounding_rows(
    *,
    expected_groundings: Mapping[int, Mapping[str, Any]],
) -> list[Mapping[str, Any]]:
    """Expose every allowed chunk row's exact immutable grounding once."""

    return [
        {
            "fact_row_index": row_index,
            **expected_groundings[row_index],
        }
        for row_index in sorted(expected_groundings)
    ]


def _business_model_synthesis_chunk_fact_row_sets(
    payload: Mapping[str, Any],
) -> tuple[tuple[int, tuple[int, ...]], ...]:
    """Return each nonempty chunk's own model-selected global fact rows.

    The fact rows were selected independently inside each chunk and restored
    to immutable global indices before synthesis.  This helper preserves that
    complete choice set; it never picks a representative on the model's
    behalf.  The existing chunk-response validator remains the authority for
    malformed or duplicate row indices.
    """

    synthesis = payload.get("loss_accounted_fact_chunk_synthesis")
    if not isinstance(synthesis, Mapping):
        return ()
    raw_chunks = synthesis.get("chunk_responses")
    if (
        not isinstance(raw_chunks, Sequence)
        or isinstance(raw_chunks, (str, bytes))
    ):
        return ()
    result: list[tuple[int, tuple[int, ...]]] = []
    globally_seen: set[int] = set()
    for ordinal, raw_chunk in enumerate(raw_chunks):
        if not isinstance(raw_chunk, Mapping):
            continue
        raw_chunk_index = raw_chunk.get("chunk_index", ordinal)
        chunk_index = (
            int(raw_chunk_index)
            if isinstance(raw_chunk_index, int)
            and not isinstance(raw_chunk_index, bool)
            and raw_chunk_index >= 0
            else ordinal
        )
        response = raw_chunk.get("response")
        if not isinstance(response, Mapping):
            continue
        selected = tuple(
            sorted(
                _response_fact_row_indices(
                    "BUSINESS_MODEL_RESEARCH",
                    response,
                )
            )
        )
        if not selected:
            continue
        # Loss-accounted chunks are disjoint by construction.  Preserve only
        # that invariant here; a duplicated global row cannot be used to make
        # two chunks appear represented by one final citation.
        if globally_seen.intersection(selected):
            raise ValueError(
                "business-model synthesis chunk fact rows must be disjoint"
            )
        globally_seen.update(selected)
        result.append((chunk_index, selected))
    return tuple(result)


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
    if pass_name == "BUSINESS_MODEL_RESEARCH":
        missing_chunk_indices = [
            chunk_index
            for chunk_index, row_indices in (
                _business_model_synthesis_chunk_fact_row_sets(
                    {
                        "loss_accounted_fact_chunk_synthesis": {
                            "chunk_responses": chunk_responses,
                        }
                    }
                )
            )
            if cited.isdisjoint(row_indices)
        ]
        if missing_chunk_indices:
            raise StructuredProviderRejected(
                "loss_accounted_business_model_synthesis_"
                "chunk_coverage_mismatch:"
                + ",".join(
                    str(chunk_index)
                    for chunk_index in missing_chunk_indices
                )
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


def _collaboration_pending_request_id(
    error: Exception,
) -> str | None:
    match = _COLLABORATION_RESPONSE_PENDING_RE.fullmatch(str(error).strip())
    return match.group(1) if match else None


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
                omitted_available_structured_metrics = sorted(
                    (
                        set(plan.structured_metric_requirements)
                        & set(metric_input)
                    )
                    - set(memo.structured_metrics)
                )
                if omitted_available_structured_metrics:
                    raise ValueError(
                        "researcher omitted available required structured "
                        "metrics: "
                        + ",".join(omitted_available_structured_metrics)
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
                disposition_selection_mismatches = (
                    _prior_disposition_selection_mismatches(response)
                )
                expected_retry_groundings = (
                    _expected_selected_fact_grounding_rows(
                        response=response,
                        fact_id_by_row_index=fact_id_by_row_index,
                        facts=fact_by_id,
                        additional_row_indices=(
                            disposition_selection_mismatches[
                                "retained_not_selected_fact_row_indices"
                            ]
                        ),
                    )
                )
                has_disposition_selection_mismatch = any(
                    disposition_selection_mismatches.values()
                )
                rejected_response_context = (
                    {
                        "rejected_response_omitted_to_prevent_"
                        "cross_array_error_copy": True,
                    }
                    if has_disposition_selection_mismatch
                    else {"rejected_response": response}
                )
                retained_not_selected = disposition_selection_mismatches[
                    "retained_not_selected_fact_row_indices"
                ]
                omitted_but_selected = disposition_selection_mismatches[
                    "omitted_but_selected_fact_row_indices"
                ]
                model_selection_consistency_context = (
                    {
                        "required_model_selected_fact_row_indices": [
                            int(row["fact_row_index"])
                            for row in expected_retry_groundings
                        ],
                        "required_model_selection_source": (
                            "REJECTED_LLM_SELECTED_UNION_REJECTED_LLM_RETAIN"
                        ),
                        "deterministic_selection_decision": False,
                    }
                    if retained_not_selected and not omitted_but_selected
                    else {}
                )
                attempt_payload = scrub_blind_research_payload(
                    {
                        **payload,
                        "component_research_validation_retry_context": {
                            "validation_error": (
                                " ".join(str(exc).split())[-500:]
                                or exc.__class__.__name__
                            ),
                            **rejected_response_context,
                            "expected_selected_fact_groundings": (
                                expected_retry_groundings
                            ),
                            **disposition_selection_mismatches,
                            **model_selection_consistency_context,
                            "required_structured_metric_row_indices": [
                                row["structured_metric_row_index"]
                                for row in structured_metric_rows
                            ],
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
                                "a semantic reason and remain unselected. "
                                "Resolve every row named in retained_not_selected_"
                                "fact_row_indices or omitted_but_selected_fact_row_"
                                "indices explicitly. "
                                "When required_model_selected_fact_row_indices is "
                                "present, your rejected response explicitly chose "
                                "RETAIN for the added rows. Return that exact selected "
                                "and grounding roster and keep prior dispositions "
                                "consistent with it; this preserves your own evidence "
                                "decision and only corrects its cross-array expression. "
                                "When that required roster is absent, either keep RETAIN "
                                "and include the row in both selected arrays, or keep it "
                                "unselected and change it to OMIT with your own semantic "
                                "reason. The expected grounding rows expose immutable "
                                "source fields but never decide a score or Stage. "
                                "Positive points require at least one selected current "
                                "POSITIVE fact; neutral context and structured "
                                "metrics with score_authority=false are not positive "
                                "score evidence. If no positive fact qualifies, "
                                "return a zero score range instead of narrating an "
                                "unsupported positive score. Account for every "
                                "supplied structured_metric_rows entry exactly once "
                                "in structured_metric_row_indices. These rows are "
                                "immutable source context required by the research "
                                "plan, but they do not decide a score or Stage. "
                                "Return exactly one "
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
    cited_anchors = tuple(anchors[anchor_id] for anchor_id in historical)
    if not cited_anchors or not any(
        row.get("usable_as_exact_anchor") is True
        or row.get("usable_as_ordinal_anchor") is True
        for row in cited_anchors
    ):
        # A component memo is the input contract for the three independent
        # judges.  Letting an anchorless memo look COMPLETE only postpones the
        # same error until deterministic scoring, where checkpoint reuse can
        # turn it into a non-progressing loop.  Reject it here so the provider
        # receives the normal validation-retry context and rewrites the memo.
        raise ValueError(
            "component research requires a usable historical anchor"
        )
    if any(
        abs(float(row.get("max_points") or 0.0) - plan.component_max_points)
        > 1e-9
        for row in cited_anchors
    ):
        raise ValueError(
            "historical anchor and component point scales differ"
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
        "prior_fact_dispositions_required": False,
        "required_prior_fact_disposition_count": 0,
        "unavailable_prior_facts_are_hash_only_not_dispositions": True,
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
        "available": bool(current_rows),
        "score_authority": False,
        "deterministic_fact_carry_forward": False,
        "prior_fact_dispositions_required": bool(current_rows),
        "required_prior_fact_disposition_count": len(current_rows),
        "unavailable_prior_facts_are_hash_only_not_dispositions": True,
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
    additional_row_indices: Sequence[int] = (),
) -> list[Mapping[str, Any]]:
    """Focus a rejected rewrite on exact source fields without repairing it."""

    if not isinstance(response, Mapping):
        return []
    selected = response.get("selected_fact_row_indices")
    if isinstance(selected, (str, bytes)) or not isinstance(selected, Sequence):
        return []
    result: list[Mapping[str, Any]] = []
    seen: set[int] = set()
    for row_index in (*selected, *additional_row_indices):
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


def _prior_disposition_selection_mismatches(
    response: Any,
) -> Mapping[str, list[int]]:
    """Name cross-array contradictions without choosing their disposition."""

    if not isinstance(response, Mapping):
        return {
            "retained_not_selected_fact_row_indices": [],
            "omitted_but_selected_fact_row_indices": [],
        }
    selected_value = response.get("selected_fact_row_indices")
    selected = {
        int(row_index)
        for row_index in (
            selected_value
            if isinstance(selected_value, Sequence)
            and not isinstance(selected_value, (str, bytes))
            else ()
        )
        if isinstance(row_index, int)
        and not isinstance(row_index, bool)
        and row_index >= 0
    }
    dispositions = response.get("prior_fact_dispositions")
    rows = (
        dispositions
        if isinstance(dispositions, Sequence)
        and not isinstance(dispositions, (str, bytes))
        else ()
    )
    retained = {
        int(row["fact_row_index"])
        for row in rows
        if isinstance(row, Mapping)
        and isinstance(row.get("fact_row_index"), int)
        and not isinstance(row.get("fact_row_index"), bool)
        and int(row["fact_row_index"]) >= 0
        and str(row.get("disposition") or "") == "RETAIN"
    }
    omitted = {
        int(row["fact_row_index"])
        for row in rows
        if isinstance(row, Mapping)
        and isinstance(row.get("fact_row_index"), int)
        and not isinstance(row.get("fact_row_index"), bool)
        and int(row["fact_row_index"]) >= 0
        and str(row.get("disposition") or "") == "OMIT"
    }
    return {
        "retained_not_selected_fact_row_indices": sorted(retained - selected),
        "omitted_but_selected_fact_row_indices": sorted(omitted & selected),
    }


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


def _single_payload_request_material(
    *,
    pass_name: str,
    payload: Mapping[str, Any],
) -> tuple[Mapping[str, Any], Mapping[str, Any], str, str, str]:
    """Build the exact transport request material without performing I/O."""

    if pass_name not in _PROVIDER_SCHEMAS:
        raise ValueError(f"unsupported researcher pass: {pass_name}")
    safe_payload = scrub_blind_research_payload(payload)
    output_schema = _provider_output_schema(
        pass_name=pass_name,
        payload=safe_payload,
    )
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
    schema_hash = _canonical_json_hash(output_schema)
    return safe_payload, output_schema, prompt, prompt_hash, schema_hash


def _pass_instruction(pass_name: str) -> str:
    judge_fact_projection_instruction = (
        "First decode every evidence_fact_projection.facts row positionally with "
        "evidence_fact_projection.fact_fields. Each row preserves one exact fact_id "
        "and its economic meaning. Resolve source_independence_group_index through "
        "source_independence_group_dictionary. The count/hash rosters account only "
        "for repeated lineage; they are not omitted research, a top-N selection, or "
        "permission to skip rows. Review all fact_count rows. "
    )
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
            "Only current_fact_rows require dispositions. When current_fact_rows is "
            "empty or prior_fact_dispositions_required is false, return an empty "
            "prior_fact_dispositions array; unavailable prior facts are hash-only "
            "audit history and must never be assigned a current row index. "
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
        return (
            "Challenge every material thesis independently and distinguish current "
            "counters from resolved or superseded history. review_complete means the "
            "full seven-component counter review was performed; it does not require "
            "pretending that every monitoring uncertainty disappeared. Preserve honest "
            "unresolved challenges and research directions so the independent Supervisor "
            "can decide whether each is still material and has a reasonable public-source "
            "route."
        )
    if pass_name == "SYNTHESIS_REVIEW":
        return "Synthesize cross-component support and tension without calculating total points or Stage."
    if pass_name == "SOURCE_QUERY_GENERATION":
        return (
            "Generate literal target-scoped discovery queries from the current facts, "
            "missing information, source failures, and open objectives. Do not reuse an "
            "executed query and do not supply a deterministic fallback template. A "
            "discovery query does not require a pre-known report id, file name, URL, or "
            "verified document identity: its purpose is to discover that identity from "
            "the evidence-backed gap. When several materially distinct unresolved "
            "directions or eligible source families remain, return a bounded query for "
            "each one rather than selecting only the easiest route; the deterministic "
            "transport budget will enforce the production limit. When "
            "score_gap_context supplies missing_role_resolution_contracts, follow the "
            "accepted evidence roles, allowed source families, and validation conditions "
            "literally. Semantically adjacent evidence from an ineligible source is not "
            "progress; for example, a third-party estimate cannot replace an issuer-only "
            "requirement. The default web discovery backend is token-oriented Naver "
            "search: make each literal query a short natural-language request for one "
            "claim or one source route. Keep cutoff dates, evidence eligibility rules, "
            "long quoted phrases, and multi-claim instructions in the rationale rather "
            "than stuffing them into the literal query; a relevant fiscal period or year "
            "may still be part of the query. Check evidence currentness against the "
            "supplied as_of_date and the latest period/publication already present. The "
            "existence of an older filing, release, transcript, or report does not prove "
            "that the route is current. When a newer eligible source could reasonably "
            "have been published on or before as_of_date and that route has not been "
            "searched, generate a query for the most recent eligible source available by "
            "the cutoff. Never request, infer, or use a publication after as_of_date. "
            "After a zero-result or irrelevant "
            "result, materially change the vocabulary and relax site, path, and exact-quote "
            "constraints instead of repeating the same query. An issuer landing page may "
            "lead to a presentation, transcript, or delegated IR asset, so generate a "
            "route that can discover the landing page as well as the final document. The "
            "same rule applies to independent corroboration. When current source-backed "
            "facts name a counterparty, platform, event, session, product, or speaker and "
            "the open objective needs a source independent of the issuer, use those "
            "already supplied terms to search the counterparty's official catalog, event "
            "page, product page, newsroom, or filing. Do not narrow every "
            "CUSTOMER_OFFICIAL route to procurement terms: an official technical session "
            "or integration page can corroborate a technical relationship without proving "
            "a purchase obligation. Keep those two meanings separate. The "
            "LLM still owns every literal query."
        )
    if pass_name == "SOURCE_CANDIDATE_RANKING":
        return (
            "Assess every discovery candidate for material relevance to the supplied "
            "research objectives. Snippets are discovery metadata only, never evidence. "
            "ranking_complete is local to classifying every candidate in this supplied "
            "transport roster exactly once; it does not mean the documents were fetched "
            "or the broader research is complete. Put fetch or evidence gaps in "
            "unresolved_notes while keeping ranking_complete=true after full roster "
            "accounting. "
            "Use requested_source_families, verified_official_domain_candidate, and "
            "candidate_source_family_hint as discovery provenance. When an objective "
            "requires an issuer source, prioritize an eligible verified issuer-domain "
            "candidate over a third-party retelling even when the issuer snippet is sparse. "
            "Set matched_requested_source_family to exactly one family requested by "
            "that candidate when the URL owner and discovery metadata support that "
            "provenance, even when the document is immaterial or has the wrong "
            "subject. Otherwise set it to NONE. material_relevance=true requires a "
            "matched requested family, but a source-family match alone does not make "
            "an irrelevant candidate material. "
            "A blog, portal repost, or third-party retelling never satisfies an issuer- "
            "or customer-official request merely because it discusses the requested "
            "company or product. "
            "A landing page, redirect page, or document referenced by an already fetched "
            "page may be materially relevant as a route to the full original source; do "
            "not reject it merely because it is not yet evidence. When "
            "reference_transport_context.explicit_text_reference is true and "
            "content_identity_verified is false, the retained parent body cited a "
            "different normalized same-host URL. Do not call that child duplicate "
            "content merely from similar titles, paths, or parent ids. Assess the "
            "distinct URL as a bounded full-fetch route; only a fetched content hash "
            "can later prove content identity."
        )
    if pass_name == "EVIDENCE_FACT_EXTRACTION":
        return (
            "Extract every material economic fact and counterfact from the supplied full "
            "documents. Cite an exact quote that occurs in the cited document, keep issuer, "
            "business segment, product, period, direction, and lifecycle explicit, and account "
            "for every document with one disposition. Tag SEGMENT_CONTRIBUTION, QOQ_GROWTH, "
            "FORWARD_GUIDANCE, EPS_REVISION, OPERATING_PROFIT_REVISION, "
            "LATEST_ACTUAL_DEPRECIATION_AMORTIZATION, "
            "FORWARD_BOOK_VALUE, FORWARD_PB, FORWARD_EV_EBITDA, or "
            "DURABLE_VISIBILITY only when "
            "the exact quote and value explicitly establish that "
            "structured role. For numeric roles, keep value as only the reported numeric "
            "point/range, unit separately, and the time horizon in period. A revision role "
            "additionally requires a dated "
            "full broker PDF whose exact quote identifies the forward metric and shows both "
            "the previous and revised estimates; value is the revised numeric point. Otherwise "
            "return an empty structured_evidence_roles array. "
            "FORWARD_GUIDANCE includes a numeric issuer-owned future operating, capacity, "
            "or capital plan whose period ends after the source became available; it does "
            "not include a broker estimate. "
            "DURABLE_VISIBILITY includes an issuer- or customer-official, target-attributable "
            "future-period statement that explicitly covers demand, committed backlog, "
            "production, capacity, allocation, or binding supply visibility for a specific "
            "business segment or product. It may be qualitative, but must not turn a supply "
            "discussion, aspiration, broker estimate, or silence into a contract, volume, "
            "price, cancellation term, or prepayment. "
            "LATEST_ACTUAL_DEPRECIATION_AMORTIZATION requires "
            "one reported issuer/regulatory numeric point for an already-ended period and "
            "must not be attached to a forecast. "
            "These tags are extraction context only and never assign points. Read prior "
            "fact-extraction retry "
            "context and correct the cited disposition/schema failure: FACTS_EXTRACTED is valid only "
            "when that same document has at least one accepted fact proposal; otherwise use the "
            "accurate non-fact disposition. The five scope_* fields are closed-vocabulary "
            "mechanism coordinates. For each one, copy exactly one token from its corresponding "
            "allowed_* list in deterministic_mechanism_scope_contract. Never put a translated "
            "label, business-unit display name, product generation, narrower synonym, or process "
            "generation in a scope_* field. Preserve that narrower source detail in subject, "
            "product_family, normalized_object, and exact_quote instead. Never "
            "infer absence from silence. Copy exact_quote as a literal contiguous substring of "
            "content_text without paraphrasing, punctuation edits, or whitespace normalization. "
            "An explicit statement inside a bounded disclosure section that no applicable or "
            "material contract exists, or that specified contract terms are not disclosed, is "
            "not silence. It may be extracted as a scoped information-limitation counterfact "
            "only for the issuer, reporting period, section, and contract class actually named "
            "by the source; never generalize it into document-wide or market-wide absence. "
            "An explicit statement that figures are preliminary, unaudited, subject to "
            "review or change, independently unverified, or forward-looking and exposed "
            "to risks is not silence. Extract it as a counterfact when it directly limits "
            "the certainty of an objective-linked result or forecast. Likewise, an "
            "official counterparty catalog or product page that names the target's "
            "technical participation can be an independent-corroboration fact, but it "
            "must not be relabelled as a contract, allocation, or purchase obligation. "
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
            "When fact_extraction_coverage_audit_context is present, perform the requested "
            "independent second reading and return only omitted facts not listed in "
            "previously_accepted_facts. Recheck named relationship and attribution spans "
            "(including events, sessions, speakers, participants, products, platforms, and "
            "counterparties) and source-quality or uncertainty spans (including preliminary "
            "or unaudited status, review or change risk, independent-verification limits, and "
            "forward-looking risk). These are semantic coverage families, not a deterministic "
            "keyword checklist. Do not repeat an accepted quote with the same normalized "
            "economic identity and do not infer a fact or absence from silence. The same "
            "literal quote may support more than one row only "
            "when each row has a materially distinct normalized predicate/object and objective "
            "effect; cosmetic relabeling is still a duplicate. "
            "When fact_extraction_scope_contract.mode is "
            "PRODUCTION_OBJECTIVE_LOCAL, follow objective_coverage_scope. Under "
            "TARGET_WIDE_CURRENT_OPEN_OBJECTIVES, document discovery objective ids "
            "are provenance only: return a fact for any listed current open target "
            "objective whose component is compatible with the literal mechanism, "
            "copy every directly affected id into objective_ids, and classify the "
            "effect as ADVANCE, COUNTER, or SUPERSEDE. Never cite an unknown or "
            "closed objective. NO_OBJECTIVE_LOCAL_FACT means only that the discovery "
            "objective had no fact and is nonterminal; NO_MATERIAL_FACT is allowed "
            "only after target-wide current-objective coverage. Do not turn general "
            "background or adjacent technical history into production facts merely "
            "because it is economically interesting. "
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
            "The mere presence of component uncertainties or red-team unresolved-challenge "
            "text does not make a completed memo insufficient. Decide materiality and route "
            "availability independently: a limitation may remain as a scored counterweight or "
            "monitoring item when verified counter/supersession routes were executed, the "
            "public-source route is exhausted, and no new fact is reasonably likely to change "
            "the component judgment. Keep memo_sufficient false and emit a concrete material "
            "gap/direction whenever such a reasonable route still exists. Do not require a "
            "pre-known document id or URL before declaring a reasonable discovery route: "
            "the query-generation LLM owns discovering the identity. A route is not exhausted "
            "merely because no exact identity is already present in the prompt. Also do not "
            "let one corroborated counterparty, one broker report, or one reporting period "
            "silently exhaust other materially distinct named counterparties, expectation "
            "revisions, or newer eligible periods that remain in the supplied facts or Red "
            "Team directions. Evaluate "
            "currentness explicitly: compare the latest supplied evidence period and "
            "publication date with as_of_date and the normal availability cadence of that "
            "source family. Older evidence is not complete merely because it exists. If a "
            "newer eligible release could reasonably have existed by the cutoff and its "
            "official route was not checked, keep the gap open without naming or using any "
            "post-cutoff publication. For "
            "information-confidence review, issuer facts and issuer-affiliated repetitions "
            "do not establish independent corroboration. If supplied facts name a "
            "counterparty, platform, event, session, product, or speaker and a reasonable "
            "counterparty-official catalog, product, newsroom, filing, or event route has "
            "not been tried, keep that corroboration gap open and direct the query planner "
            "to that route. A technical corroboration route need not disclose procurement "
            "terms, and its absence must not be confused with a missing contract. "
            "When supervisor_validation_retry_context is present, rewrite the entire response "
            "once using its validation error, allowed objective ids, and deterministic current "
            "state as authoritative correction feedback. Do not repeat the rejected semantic "
            "contradiction and do not invent evidence, scores, or stages."
        )
    if pass_name == "SEMANTIC_SATURATION_REVIEW":
        return (
            "Independently decide whether any reasonable material-positive, counter, "
            "supersession, structured-data, or new-source-family route remains. Zero search "
            "results and transport limits are never saturation proof. Evidence age is also "
            "not saturation proof: if the latest supplied period predates a reasonably "
            "available eligible release on or before as_of_date and that route was not "
            "checked, keep the currentness gap open. Never use a post-cutoff source."
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
            "Map only source-backed current/open EvidenceFact row indices to exact configured "
            "Evidence Contract primitive ids. SUPPORT means a current positive mechanism and "
            "COUNTER means a current thesis risk. Return every supplied fact row exactly once "
            "in fact_dispositions: MAPPED only when cited by at least one mapping, NO_MATCH "
            "when fully reviewed without a semantic match, or UNRESOLVED when review cannot "
            "terminate. Primitive names are semantic labels, never score or Stage authority. "
            "Never calculate points, total score, canonical Stage, or an investment action."
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
            judge_fact_projection_instruction
            + "Act as the independent positive analyst for exactly one broad component. "
            "Derive proposed component points and an allowed range from current support facts, "
            "economic strength, duration, and cash conversion. Account for every supplied "
            "positive component fact and compare the case with at least one nearest blind "
            "historical anchor. Explain both why the score is not higher and why it is not lower."
        )
    if pass_name == "COMPONENT_SKEPTIC_JUDGE":
        return (
            judge_fact_projection_instruction
            + "Act as the independent skeptic for exactly one broad component. Review every "
            "supplied counterfact and explicitly reflect business phase, valuation, customer "
            "or supplier concentration, and uncertainty in proposed component points and the "
            "allowed range. Compare with a nearest blind anchor and explain both bounds."
        )
    return (
        judge_fact_projection_instruction
        + "Act as the independent calibration judge for exactly one broad component. Compare "
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
    "STAGE_GATE_FACT_MAPPING_SCHEMA",
    "CLAIM_COMPONENT_IMPACT_MAPPING_SCHEMA",
    "SYNTHESIS_REVIEW_SCHEMA",
    "StructuredResearchProvider",
    "STRUCTURED_PEER_SELECTION_SCHEMA",
    "ValuationResearcher",
    "build_component_researchers",
]
