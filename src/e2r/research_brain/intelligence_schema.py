"""Canonical schemas for reconstructed E2R research intelligence."""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import asdict, dataclass, field
from datetime import date
from enum import Enum
from typing import Any, Mapping


INTELLIGENCE_SCHEMA_VERSION = "e2r_research_intelligence_v1"


class ParsedRowKind(str, Enum):
    YAML_FRONT_MATTER = "yaml_front_matter"
    FENCED_JSON = "fenced_json"
    FENCED_JSONL = "fenced_jsonl"
    FENCED_CSV = "fenced_csv"
    MARKDOWN_TABLE = "markdown_table"
    JSON = "json"
    JSONL = "jsonl"
    CSV = "csv"
    NARRATIVE = "narrative"


class QuarantineReason(str, Enum):
    MALFORMED_STRUCTURED_ROW = "MALFORMED_STRUCTURED_ROW"
    CONFLICTING_DUPLICATE = "CONFLICTING_DUPLICATE"
    MISSING_SYMBOL = "MISSING_SYMBOL"
    MISSING_COMPANY = "MISSING_COMPANY"
    MISSING_DATE = "MISSING_DATE"
    URL_CASE_ASSOCIATION_AMBIGUOUS = "URL_CASE_ASSOCIATION_AMBIGUOUS"
    INCONSISTENT_ARCHETYPE = "INCONSISTENT_ARCHETYPE"
    OUTCOME_ONLY = "OUTCOME_ONLY"
    HANDOFF_PROMPT_EXCLUDED = "HANDOFF_PROMPT_EXCLUDED"
    NARRATIVE_REQUIRES_LLM = "NARRATIVE_REQUIRES_LLM"
    LLM_DERIVED_UNVERIFIED = "LLM_DERIVED_UNVERIFIED"
    LLM_PROVIDER_ERROR = "LLM_PROVIDER_ERROR"
    UNLINKED_ROW = "UNLINKED_ROW"


class HistoricalSourceState(str, Enum):
    SOURCE_PROXY_ONLY = "SOURCE_PROXY_ONLY"
    EVIDENCE_URL_PENDING = "EVIDENCE_URL_PENDING"
    URL_PRESENT_UNVERIFIED = "URL_PRESENT_UNVERIFIED"
    URL_FETCH_FAILED = "URL_FETCH_FAILED"
    URL_FETCHED_NO_ANCHOR = "URL_FETCHED_NO_ANCHOR"
    URL_FETCHED_WRONG_SUBJECT = "URL_FETCHED_WRONG_SUBJECT"
    URL_FETCHED_DATE_INVALID = "URL_FETCHED_DATE_INVALID"
    URL_FETCHED_ANCHORED = "URL_FETCHED_ANCHORED"
    URL_FETCHED_ANCHORED_CASE_MATCH = "URL_FETCHED_ANCHORED_CASE_MATCH"
    HISTORICAL_REPLAY_READY = "HISTORICAL_REPLAY_READY"


class HistoricalCaseSourceRelationship(str, Enum):
    CASE_MATCH = "CASE_MATCH"
    COUNTER_CASE_MATCH = "COUNTER_CASE_MATCH"
    UNRELATED = "UNRELATED"
    CONTRADICTS_CASE_SUMMARY = "CONTRADICTS_CASE_SUMMARY"


class EvidenceRecipeRole(str, Enum):
    POSITIVE = "POSITIVE"
    GUARD = "GUARD"
    HARD_BREAK = "HARD_BREAK"


class MemoryNodeType(str, Enum):
    CASE = "CASE"
    RECIPE = "RECIPE"
    PRIMITIVE = "PRIMITIVE"
    ARCHETYPE = "ARCHETYPE"
    SOURCE = "SOURCE"
    POSITIVE = "POSITIVE"
    COUNTER = "COUNTER"
    HARD_BREAK = "HARD_BREAK"
    SOURCE_SUCCESS = "SOURCE_SUCCESS"
    SOURCE_FAILURE = "SOURCE_FAILURE"


class MemoryEdgeType(str, Enum):
    SUPPORTS = "SUPPORTS"
    COUNTERS = "COUNTERS"
    CAPS = "CAPS"
    REQUIRES = "REQUIRES"
    BEST_FOUND_IN = "BEST_FOUND_IN"
    FAILED_IN = "FAILED_IN"
    SUPERSEDES = "SUPERSEDES"
    WRONG_SUBJECT_EXAMPLE = "WRONG_SUBJECT_EXAMPLE"
    SAME_MECHANISM = "SAME_MECHANISM"


class BalancedMemoryRole(str, Enum):
    DIRECT_RECIPE = "DIRECT_RECIPE"
    POSITIVE = "POSITIVE"
    COUNTEREXAMPLE_GUARD = "COUNTEREXAMPLE_GUARD"
    SOURCE_SUCCESS = "SOURCE_SUCCESS"
    SOURCE_FAILURE = "SOURCE_FAILURE"
    SEMANTIC_GUARD = "SEMANTIC_GUARD"
    CONTEXT_CASE = "CONTEXT_CASE"


class PlannerPass(str, Enum):
    BLIND_HYPOTHESIS = "BLIND_HYPOTHESIS"
    MEMORY_CRITIQUE = "MEMORY_CRITIQUE"


class PlannerStatus(str, Enum):
    COMPLETE = "COMPLETE"
    PENDING = "PENDING"
    ABSTAINED = "ABSTAINED"


class HypothesisStrength(str, Enum):
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"


def stable_intelligence_id(prefix: str, payload: Mapping[str, Any]) -> str:
    encoded = json.dumps(_json_safe(payload), ensure_ascii=False, sort_keys=True).encode("utf-8")
    return f"{prefix}-{hashlib.sha256(encoded).hexdigest()[:24]}"


@dataclass(frozen=True)
class SourceLineRange:
    start: int
    end: int

    def __post_init__(self) -> None:
        if self.start <= 0 or self.end < self.start:
            raise ValueError("invalid source line range")

    def to_dict(self) -> dict[str, int]:
        return {"start": self.start, "end": self.end}


@dataclass(frozen=True)
class HistoricalEvidenceReference:
    url: str | None = None
    document_id: str | None = None
    summary: str | None = None
    declared_source_quality: str | None = None
    source_row_id: str | None = None
    source_line_range: SourceLineRange | None = None

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class HistoricalResearchArtifact:
    artifact_id: str
    source_file: str
    sha256: str
    artifact_type: str
    line_count: int
    structured_row_count: int
    narrative_row_count: int
    handoff_line_range: SourceLineRange | None = None
    metadata: Mapping[str, Any] = field(default_factory=dict)
    parser_version: str = INTELLIGENCE_SCHEMA_VERSION

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class ParsedResearchRow:
    row_id: str
    artifact_id: str
    source_file: str
    source_line_range: SourceLineRange
    row_kind: str
    precedence: int
    data: Mapping[str, Any]
    raw_text: str
    structured: bool
    handoff_metadata: bool = False

    def __post_init__(self) -> None:
        ParsedRowKind(self.row_kind)

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class ParsedResearchArtifact:
    artifact: HistoricalResearchArtifact
    rows: tuple[ParsedResearchRow, ...]
    quarantine: tuple["QuarantineRecord", ...] = ()


@dataclass(frozen=True)
class HistoricalResearchCase:
    case_id: str
    artifact_id: str
    source_file: str
    source_line_range: SourceLineRange
    symbol: str
    company_name: str
    trigger_type: str | None
    trigger_date: str | None
    entry_date: str | None
    canonical_archetype_id: str
    fine_archetype_id: str | None
    large_sector_id: str | None
    case_role: str
    classification: str
    evidence_families: tuple[str, ...] = ()
    evidence_references: tuple[HistoricalEvidenceReference, ...] = ()
    declared_source_quality: str | None = None
    positive_evidence_fields: tuple[str, ...] = ()
    missing_evidence_fields: tuple[str, ...] = ()
    counter_evidence_fields: tuple[str, ...] = ()
    stage_caps: tuple[str, ...] = ()
    hard_breaks: tuple[str, ...] = ()
    false_positive_patterns: tuple[str, ...] = ()
    price_metrics_ref: str | None = None
    score_simulation_refs: tuple[str, ...] = ()
    shadow_rule_refs: tuple[str, ...] = ()
    transition_refs: tuple[str, ...] = ()
    trigger_refs: tuple[str, ...] = ()
    source_row_ids: tuple[str, ...] = ()
    runtime_score_eligible: bool = False
    compiler_origin: str = "STRUCTURED_ROW"
    uncertainty: tuple[str, ...] = ()
    schema_version: str = INTELLIGENCE_SCHEMA_VERSION

    def __post_init__(self) -> None:
        if self.runtime_score_eligible:
            raise ValueError("historical research cases cannot be runtime score eligible")
        if not self.case_id or not self.artifact_id:
            raise ValueError("case and artifact identity are required")
        if not self.symbol or not self.company_name:
            raise ValueError("case symbol and company name are required")
        if not self.canonical_archetype_id:
            raise ValueError("canonical archetype is required")

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class HistoricalOutcome:
    outcome_id: str
    artifact_id: str
    case_id: str
    trigger_id: str | None
    source_row_id: str
    source_line_range: SourceLineRange
    price_metrics: Mapping[str, Any] = field(default_factory=dict)
    expected_stage_or_label: str | None = None
    current_profile_verdict: str | None = None
    evaluator_only: bool = True
    runtime_prompt_allowed: bool = False
    runtime_score_eligible: bool = False
    schema_version: str = INTELLIGENCE_SCHEMA_VERSION

    def __post_init__(self) -> None:
        if not self.evaluator_only:
            raise ValueError("historical outcomes must remain evaluator-only")
        if self.runtime_prompt_allowed or self.runtime_score_eligible:
            raise ValueError("historical outcomes cannot enter runtime prompts or scores")

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class HistoricalRuleCandidate:
    rule_id: str
    artifact_id: str
    source_row_id: str
    source_line_range: SourceLineRange
    rule_type: str
    canonical_archetype_id: str | None
    case_ids: tuple[str, ...]
    trigger_ids: tuple[str, ...]
    payload: Mapping[str, Any]
    runtime_score_eligible: bool = False
    schema_version: str = INTELLIGENCE_SCHEMA_VERSION

    def __post_init__(self) -> None:
        if self.runtime_score_eligible:
            raise ValueError("historical rule candidates cannot directly score")

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class NarrativeCaseCandidate:
    candidate_id: str
    artifact_id: str
    source_file: str
    source_line_range: SourceLineRange
    payload: Mapping[str, Any]
    uncertainty: tuple[str, ...]
    llm_derived: bool = True
    verified: bool = False
    runtime_score_eligible: bool = False
    schema_version: str = INTELLIGENCE_SCHEMA_VERSION

    def __post_init__(self) -> None:
        if not self.llm_derived or self.verified or self.runtime_score_eligible:
            raise ValueError("narrative candidates must remain unverified and non-scoring")
        if not self.uncertainty:
            raise ValueError("narrative candidates require explicit uncertainty")

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class HistoricalSnapshotAnchor:
    anchor_id: str
    locator: str
    exact_text: str
    anchor_type: str = "TEXT_SPAN"

    def __post_init__(self) -> None:
        if not self.anchor_id or not self.locator or not self.exact_text.strip():
            raise ValueError("historical snapshot anchors require id, locator, and exact text")

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class HistoricalProviderSnapshot:
    snapshot_id: str
    canonical_url: str | None
    official_document_id: str | None
    provider_name: str
    provider_record_id: str
    fetch_status: str
    content_path: str | None
    content_sha256: str | None
    published_date: str | None
    available_date: str | None
    captured_at: str | None
    title: str | None
    source_type: str
    subject_symbols: tuple[str, ...]
    subject_names: tuple[str, ...]
    anchors: tuple[HistoricalSnapshotAnchor, ...]
    valid_provider_snapshot: bool
    replay_only: bool = True
    production_score_evidence_allowed: bool = False
    metadata: Mapping[str, Any] = field(default_factory=dict)
    schema_version: str = INTELLIGENCE_SCHEMA_VERSION

    def __post_init__(self) -> None:
        if not self.snapshot_id or not self.provider_name or not self.provider_record_id:
            raise ValueError("provider snapshot identity is required")
        if not self.canonical_url and not self.official_document_id:
            raise ValueError("provider snapshot requires URL or official document id")
        if self.production_score_evidence_allowed:
            raise ValueError("historical provider snapshots cannot be current score evidence")
        if self.valid_provider_snapshot and self.fetch_status != "FETCHED":
            raise ValueError("valid provider snapshots must be fetched")
        if self.valid_provider_snapshot and (
            not self.content_path
            or not self.content_sha256
            or not self.published_date
            or not self.available_date
            or not self.captured_at
        ):
            raise ValueError("valid provider snapshots require content and temporal provenance")

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class HistoricalCaseSourceLink:
    link_id: str
    case_id: str
    snapshot_id: str
    anchor_ids: tuple[str, ...]
    relationship: str
    target_directness: str
    summary_consistent: bool
    rationale: str
    verifier_origin: str
    verifier_prompt_hash: str
    verifier_response_hash: str
    verified: bool = True
    current_score_evidence_allowed: bool = False
    schema_version: str = INTELLIGENCE_SCHEMA_VERSION

    def __post_init__(self) -> None:
        HistoricalCaseSourceRelationship(self.relationship)
        if not self.case_id or not self.snapshot_id or not self.anchor_ids:
            raise ValueError("case/source link requires case, snapshot, and anchor ids")
        if not self.rationale or not self.verifier_origin:
            raise ValueError("case/source link requires verification provenance")
        if self.current_score_evidence_allowed:
            raise ValueError("historical case/source links cannot enter current score")

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class HistoricalSourceVerification:
    verification_id: str
    case_id: str
    artifact_id: str
    source_state: str
    source_url: str | None
    official_document_id: str | None
    snapshot_id: str | None
    content_sha256: str | None
    published_date: str | None
    historical_as_of_date: str | None
    anchor_ids: tuple[str, ...]
    anchor_locators: tuple[str, ...]
    exact_quotes: tuple[str, ...]
    target_directness: str
    case_relationship: str | None
    summary_consistent: bool | None
    blocker_code: str | None
    blocker_detail: str | None
    checks: Mapping[str, bool]
    state_trace: tuple[str, ...]
    historical_replay_ready: bool
    a2_historical_evidence_eligible: bool
    evaluator_only: bool = True
    current_score_eligible: bool = False
    schema_version: str = INTELLIGENCE_SCHEMA_VERSION

    def __post_init__(self) -> None:
        HistoricalSourceState(self.source_state)
        if self.current_score_eligible or not self.evaluator_only:
            raise ValueError("historical source verification must be evaluator-only")
        if self.historical_replay_ready != (
            self.source_state == HistoricalSourceState.HISTORICAL_REPLAY_READY.value
        ):
            raise ValueError("historical replay readiness must match source state")
        if self.historical_replay_ready:
            if not self.a2_historical_evidence_eligible:
                raise ValueError("replay-ready source must be historical A2 eligible")
            if self.blocker_code:
                raise ValueError("replay-ready source cannot carry a blocker")
            if not self.checks or not all(self.checks.values()):
                raise ValueError("replay-ready source requires every verification check")
        elif self.a2_historical_evidence_eligible:
            raise ValueError("non-ready source cannot be historical A2 eligible")

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class HistoricalSourceRepairTask:
    repair_task_id: str
    case_id: str
    source_state: str
    source_url: str | None
    official_document_id: str | None
    blocker_code: str
    blocker_detail: str
    required_resolution: tuple[str, ...]
    planning_only: bool = True
    current_score_eligible: bool = False
    schema_version: str = INTELLIGENCE_SCHEMA_VERSION

    def __post_init__(self) -> None:
        HistoricalSourceState(self.source_state)
        if not self.blocker_code or not self.required_resolution:
            raise ValueError("source repair task requires an exact blocker and resolution")
        if not self.planning_only or self.current_score_eligible:
            raise ValueError("historical source repair tasks are planning-only")

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class AcceptedClaimPredicate:
    predicate_id: str
    semantic_test: str
    required_subject_relation: str
    required_fields: tuple[str, ...]
    allowed_polarities: tuple[str, ...]
    temporal_test: str
    lifecycle_test: str

    def __post_init__(self) -> None:
        if not all(
            (
                self.predicate_id.strip(),
                self.semantic_test.strip(),
                self.required_subject_relation.strip(),
                self.temporal_test.strip(),
                self.lifecycle_test.strip(),
            )
        ):
            raise ValueError("accepted claim predicate fields must be non-empty")
        if not self.required_fields or not self.allowed_polarities:
            raise ValueError("accepted claim predicate requires fields and polarity")

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class EvidenceRecipe:
    recipe_id: str
    archetype_id: str
    primitive_id: str
    role: str
    economic_mechanism: str
    question_to_answer: str
    accepted_claim_predicates: tuple[AcceptedClaimPredicate, ...]
    required_entities: tuple[str, ...]
    required_values: tuple[str, ...]
    required_units: tuple[str, ...]
    required_time_scope: tuple[str, ...]
    required_target_directness: tuple[str, ...]
    required_current_lifecycle: tuple[str, ...]
    preferred_source_families: tuple[str, ...]
    preferred_document_types: tuple[str, ...]
    preferred_sections: tuple[str, ...]
    discovery_sources: tuple[str, ...]
    forbidden_score_sources: tuple[str, ...]
    positive_examples: tuple[str, ...]
    counterexamples: tuple[str, ...]
    wrong_subject_examples: tuple[str, ...]
    source_success_examples: tuple[str, ...]
    source_failure_examples: tuple[str, ...]
    rejection_conditions: tuple[str, ...]
    counter_questions: tuple[str, ...]
    supersession_questions: tuple[str, ...]
    query_intent_constraints: tuple[str, ...]
    stop_conditions: tuple[str, ...]
    source_exhaustion_conditions: tuple[str, ...]
    supporting_case_ids: tuple[str, ...]
    supporting_source_verification_ids: tuple[str, ...]
    supporting_source_failure_verification_ids: tuple[str, ...]
    planning_only_source_proxy_case_ids: tuple[str, ...]
    freshness_max_age_days: int | None
    freshness_supersession_rule: str | None
    literal_queries: tuple[str, ...] = ()
    executable: bool = True
    runtime_score_eligible: bool = False
    compiler_origin: str = "EXPLICIT_SEMANTIC_DEFINITION"
    schema_version: str = INTELLIGENCE_SCHEMA_VERSION

    def __post_init__(self) -> None:
        EvidenceRecipeRole(self.role)
        required_text = (
            self.recipe_id,
            self.archetype_id,
            self.primitive_id,
            self.economic_mechanism,
            self.question_to_answer,
        )
        if not all(item.strip() for item in required_text):
            raise ValueError("evidence recipe identity and semantic question are required")
        required_collections = {
            "accepted_claim_predicates": self.accepted_claim_predicates,
            "required_entities": self.required_entities,
            "required_values": self.required_values,
            "required_units": self.required_units,
            "required_time_scope": self.required_time_scope,
            "required_target_directness": self.required_target_directness,
            "required_current_lifecycle": self.required_current_lifecycle,
            "preferred_source_families": self.preferred_source_families,
            "preferred_document_types": self.preferred_document_types,
            "preferred_sections": self.preferred_sections,
            "discovery_sources": self.discovery_sources,
            "forbidden_score_sources": self.forbidden_score_sources,
            "positive_examples": self.positive_examples,
            "counterexamples": self.counterexamples,
            "wrong_subject_examples": self.wrong_subject_examples,
            "source_success_examples": self.source_success_examples,
            "source_failure_examples": self.source_failure_examples,
            "rejection_conditions": self.rejection_conditions,
            "counter_questions": self.counter_questions,
            "supersession_questions": self.supersession_questions,
            "query_intent_constraints": self.query_intent_constraints,
            "stop_conditions": self.stop_conditions,
            "source_exhaustion_conditions": self.source_exhaustion_conditions,
            "supporting_case_ids": self.supporting_case_ids,
        }
        missing = [name for name, values in required_collections.items() if not values]
        if missing:
            raise ValueError(f"evidence recipe fields must be non-empty: {missing}")
        if self.literal_queries:
            raise ValueError("evidence recipes must not contain deterministic literal queries")
        if not self.executable or self.runtime_score_eligible:
            raise ValueError("recipes must be executable but cannot directly score")

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class UnsupportedEvidenceRecipe:
    unsupported_id: str
    archetype_id: str
    primitive_id: str
    reason_code: str
    reason_detail: str
    required_next_input: tuple[str, ...]
    planning_only: bool = True
    runtime_route_available: bool = False
    schema_version: str = INTELLIGENCE_SCHEMA_VERSION

    def __post_init__(self) -> None:
        if not all(
            item.strip()
            for item in (
                self.unsupported_id,
                self.archetype_id,
                self.primitive_id,
                self.reason_code,
                self.reason_detail,
            )
        ):
            raise ValueError("unsupported recipe requires exact identity and reason")
        if not self.required_next_input:
            raise ValueError("unsupported recipe requires next input")
        if not self.planning_only or self.runtime_route_available:
            raise ValueError("unsupported recipe cannot become a runtime route")

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class MemoryNode:
    node_id: str
    node_type: str
    label: str
    search_text: str
    archetype_id: str | None = None
    primitive_id: str | None = None
    case_id: str | None = None
    recipe_id: str | None = None
    source_verification_id: str | None = None
    role_slot: str | None = None
    available_from_date: str | None = None
    planner_payload: Mapping[str, Any] = field(default_factory=dict)
    planner_visible: bool = True
    planning_only: bool = True
    runtime_score_eligible: bool = False
    schema_version: str = INTELLIGENCE_SCHEMA_VERSION

    def __post_init__(self) -> None:
        MemoryNodeType(self.node_type)
        if not self.node_id.strip() or not self.label.strip():
            raise ValueError("memory node identity and label are required")
        if self.role_slot is not None:
            BalancedMemoryRole(self.role_slot)
        if self.available_from_date is not None:
            try:
                date.fromisoformat(self.available_from_date)
            except ValueError as exc:
                raise ValueError("memory node available_from_date must be ISO date") from exc
        if not self.planning_only or self.runtime_score_eligible:
            raise ValueError("research memory nodes are planning-only and non-scoring")
        if self.planner_visible:
            _assert_planner_memory_safe(
                {
                    "node_id": self.node_id,
                    "node_type": self.node_type,
                    "label": self.label,
                    "search_text": self.search_text,
                    "archetype_id": self.archetype_id,
                    "primitive_id": self.primitive_id,
                    "case_id": self.case_id,
                    "recipe_id": self.recipe_id,
                    "source_verification_id": self.source_verification_id,
                    "role_slot": self.role_slot,
                    "planner_payload": self.planner_payload,
                },
                context=f"planner-visible memory node {self.node_id}",
            )

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class MemoryEdge:
    edge_id: str
    edge_type: str
    source_node_id: str
    target_node_id: str
    rationale: str
    planner_visible: bool = True
    planning_only: bool = True
    runtime_score_eligible: bool = False
    metadata: Mapping[str, Any] = field(default_factory=dict)
    schema_version: str = INTELLIGENCE_SCHEMA_VERSION

    def __post_init__(self) -> None:
        MemoryEdgeType(self.edge_type)
        if not all(
            value.strip()
            for value in (
                self.edge_id,
                self.source_node_id,
                self.target_node_id,
                self.rationale,
            )
        ):
            raise ValueError("memory edge identity, endpoints, and rationale are required")
        if not self.planning_only or self.runtime_score_eligible:
            raise ValueError("research memory edges are planning-only and non-scoring")
        if self.planner_visible:
            _assert_planner_memory_safe(
                {
                    "edge_id": self.edge_id,
                    "edge_type": self.edge_type,
                    "rationale": self.rationale,
                    "metadata": self.metadata,
                },
                context=f"planner-visible memory edge {self.edge_id}",
            )

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class ResearchMemoryGraph:
    graph_id: str
    nodes: tuple[MemoryNode, ...]
    edges: tuple[MemoryEdge, ...]
    schema_version: str = INTELLIGENCE_SCHEMA_VERSION

    def __post_init__(self) -> None:
        if not self.graph_id.strip() or not self.nodes:
            raise ValueError("research memory graph requires identity and nodes")
        node_ids = [node.node_id for node in self.nodes]
        if len(node_ids) != len(set(node_ids)):
            raise ValueError("research memory graph contains duplicate node ids")
        edge_ids = [edge.edge_id for edge in self.edges]
        if len(edge_ids) != len(set(edge_ids)):
            raise ValueError("research memory graph contains duplicate edge ids")
        known_nodes = set(node_ids)
        dangling = [
            edge.edge_id
            for edge in self.edges
            if edge.source_node_id not in known_nodes or edge.target_node_id not in known_nodes
        ]
        if dangling:
            raise ValueError(f"research memory graph contains dangling edges: {dangling[:5]}")

    def to_dict(self) -> dict[str, Any]:
        return {
            "graph_id": self.graph_id,
            "schema_version": self.schema_version,
            "nodes": [node.to_dict() for node in self.nodes],
            "edges": [edge.to_dict() for edge in self.edges],
        }


@dataclass(frozen=True)
class SemanticMemoryIndexEntry:
    node_id: str
    node_type: str
    archetype_id: str | None
    primitive_id: str | None
    recipe_id: str | None
    role_slot: str | None
    concepts: tuple[str, ...]
    available_from_date: str | None
    planner_visible: bool
    search_text_sha256: str
    schema_version: str = INTELLIGENCE_SCHEMA_VERSION

    def __post_init__(self) -> None:
        MemoryNodeType(self.node_type)
        if self.role_slot is not None:
            BalancedMemoryRole(self.role_slot)
        if not self.node_id.strip() or not self.search_text_sha256.strip():
            raise ValueError("semantic memory index entry requires node and text hash")
        if self.planner_visible:
            _assert_planner_memory_safe(
                {
                    "node_id": self.node_id,
                    "archetype_id": self.archetype_id,
                    "primitive_id": self.primitive_id,
                    "recipe_id": self.recipe_id,
                    "concepts": self.concepts,
                },
                context=f"semantic memory index entry {self.node_id}",
            )

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class BalancedRetrievalRequest:
    request_id: str
    current_evidence_text: str
    as_of_date: str
    candidate_archetype_ids: tuple[str, ...] = ()
    required_primitive_ids: tuple[str, ...] = ()
    excluded_case_ids: tuple[str, ...] = ()
    top_k_archetypes: int = 3
    max_recipe_hits: int = 3

    def __post_init__(self) -> None:
        if not self.request_id.strip() or not self.current_evidence_text.strip():
            raise ValueError("balanced retrieval request requires id and current evidence")
        if not self.as_of_date.strip():
            raise ValueError("balanced retrieval request requires as_of_date")
        try:
            date.fromisoformat(self.as_of_date)
        except ValueError as exc:
            raise ValueError("balanced retrieval request as_of_date must be ISO date") from exc
        if self.top_k_archetypes <= 0 or self.max_recipe_hits <= 0:
            raise ValueError("balanced retrieval limits must be positive")
        _assert_planner_memory_safe(
            {
                "request_id": self.request_id,
                "current_evidence_text": self.current_evidence_text,
                "candidate_archetype_ids": self.candidate_archetype_ids,
                "required_primitive_ids": self.required_primitive_ids,
            },
            context=f"balanced retrieval request {self.request_id}",
        )

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class ArchetypeRetrievalHit:
    archetype_id: str
    semantic_score: float
    matched_concepts: tuple[str, ...]
    supporting_node_ids: tuple[str, ...]

    def __post_init__(self) -> None:
        if not self.archetype_id.strip() or self.semantic_score < 0.0:
            raise ValueError("archetype retrieval hit requires id and non-negative score")

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class BalancedRetrievalItem:
    node_id: str
    node_type: str
    role_slot: str
    archetype_id: str
    primitive_id: str | None
    recipe_id: str | None
    semantic_score: float
    matched_concepts: tuple[str, ...]
    planner_payload: Mapping[str, Any]
    available_from_date: str | None = None

    def __post_init__(self) -> None:
        MemoryNodeType(self.node_type)
        BalancedMemoryRole(self.role_slot)
        if not self.node_id.strip() or not self.archetype_id.strip():
            raise ValueError("balanced retrieval item requires node and archetype")
        if self.semantic_score < 0.0:
            raise ValueError("balanced retrieval item score cannot be negative")
        _assert_planner_memory_safe(
            {
                "node_id": self.node_id,
                "node_type": self.node_type,
                "role_slot": self.role_slot,
                "archetype_id": self.archetype_id,
                "primitive_id": self.primitive_id,
                "recipe_id": self.recipe_id,
                "matched_concepts": self.matched_concepts,
                "planner_payload": self.planner_payload,
            },
            context=f"balanced retrieval item {self.node_id}",
        )

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class BalancedRetrievalResult:
    request_id: str
    archetype_hits: tuple[ArchetypeRetrievalHit, ...]
    items: tuple[BalancedRetrievalItem, ...]
    covered_roles: tuple[str, ...]
    missing_roles: tuple[str, ...]
    direct_recipe_ids: tuple[str, ...]
    first_n_only: bool
    popularity_weight_used: bool
    future_leakage_count: int

    def __post_init__(self) -> None:
        if not self.request_id.strip() or not self.archetype_hits:
            raise ValueError("balanced retrieval result requires request and archetype hits")
        for role in (*self.covered_roles, *self.missing_roles):
            BalancedMemoryRole(role)
        if self.first_n_only or self.popularity_weight_used:
            raise ValueError("balanced retrieval cannot use first-N or popularity weight")
        if self.future_leakage_count:
            raise ValueError("balanced retrieval result contains future leakage")

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class CurrentEvidenceFact:
    fact_id: str
    text: str
    observed_date: str
    target_relation: str
    current_status: str

    def __post_init__(self) -> None:
        if not all(
            value.strip()
            for value in (
                self.fact_id,
                self.text,
                self.observed_date,
                self.target_relation,
                self.current_status,
            )
        ):
            raise ValueError("current evidence fact fields must be non-empty")
        try:
            date.fromisoformat(self.observed_date)
        except ValueError as exc:
            raise ValueError("current evidence fact observed_date must be ISO date") from exc
        _assert_planner_memory_safe(
            {"fact_id": self.fact_id, "text": self.text},
            context=f"current evidence fact {self.fact_id}",
        )

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class BlindHypothesisInput:
    input_id: str
    target_id: str
    target_name: str
    target_aliases: tuple[str, ...]
    as_of_date: str
    current_facts: tuple[CurrentEvidenceFact, ...]
    sector_context: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not all(
            value.strip()
            for value in (
                self.input_id,
                self.target_id,
                self.target_name,
                self.as_of_date,
            )
        ):
            raise ValueError("blind hypothesis input identity is required")
        try:
            as_of = date.fromisoformat(self.as_of_date)
        except ValueError as exc:
            raise ValueError("blind hypothesis as_of_date must be ISO date") from exc
        if not self.current_facts:
            raise ValueError("blind hypothesis input requires current evidence facts")
        if len({fact.fact_id for fact in self.current_facts}) != len(self.current_facts):
            raise ValueError("blind hypothesis input contains duplicate fact ids")
        if any(date.fromisoformat(fact.observed_date) > as_of for fact in self.current_facts):
            raise ValueError("blind hypothesis input contains future evidence")
        _assert_blind_pass_payload_safe(self.to_dict(), context=self.input_id)

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class BlindMechanismHypothesis:
    hypothesis_id: str
    rank: int
    mechanism_summary: str
    strength: str
    supporting_fact_ids: tuple[str, ...]
    contradicting_fact_ids: tuple[str, ...]
    must_verify_questions: tuple[str, ...]

    def __post_init__(self) -> None:
        HypothesisStrength(self.strength)
        if self.rank <= 0 or not self.hypothesis_id.strip() or not self.mechanism_summary.strip():
            raise ValueError("blind mechanism hypothesis requires identity, rank, and summary")
        if not self.supporting_fact_ids or not self.must_verify_questions:
            raise ValueError("blind mechanism hypothesis requires facts and questions")
        _assert_blind_pass_payload_safe(self.to_dict(), context=self.hypothesis_id)

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class BlindHypothesisOutput:
    input_id: str
    hypotheses: tuple[BlindMechanismHypothesis, ...]
    ambiguity_reasons: tuple[str, ...]
    abstain: bool
    abstention_reason: str | None

    def __post_init__(self) -> None:
        if not self.input_id.strip():
            raise ValueError("blind hypothesis output requires input id")
        if self.abstain and not str(self.abstention_reason or "").strip():
            raise ValueError("blind abstention requires a reason")
        if not self.abstain and not self.hypotheses:
            raise ValueError("non-abstaining blind output requires hypotheses")
        ranks = [item.rank for item in self.hypotheses]
        if ranks != list(range(1, len(ranks) + 1)):
            raise ValueError("blind hypotheses must use contiguous rank order")
        if len({item.hypothesis_id for item in self.hypotheses}) != len(self.hypotheses):
            raise ValueError("blind hypotheses require unique IDs")
        _assert_blind_pass_payload_safe(self.to_dict(), context=self.input_id)

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class MemoryCritiqueInput:
    input_id: str
    blind_input_id: str
    as_of_date: str
    current_facts: tuple[CurrentEvidenceFact, ...]
    blind_hypotheses: tuple[BlindMechanismHypothesis, ...]
    balanced_memory: Mapping[str, Any]
    available_recipe_ids: tuple[str, ...]

    def __post_init__(self) -> None:
        if not all(
            value.strip() for value in (self.input_id, self.blind_input_id, self.as_of_date)
        ):
            raise ValueError("memory critique input identity is required")
        try:
            date.fromisoformat(self.as_of_date)
        except ValueError as exc:
            raise ValueError("memory critique as_of_date must be ISO date") from exc
        if not self.current_facts or not self.blind_hypotheses:
            raise ValueError("memory critique requires current facts and blind hypotheses")
        if not self.balanced_memory:
            raise ValueError("memory critique requires balanced memory")
        as_of = date.fromisoformat(self.as_of_date)
        if any(date.fromisoformat(fact.observed_date) > as_of for fact in self.current_facts):
            raise ValueError("memory critique input contains future evidence")
        if len({fact.fact_id for fact in self.current_facts}) != len(self.current_facts):
            raise ValueError("memory critique input contains duplicate fact IDs")
        fact_ids = {fact.fact_id for fact in self.current_facts}
        referenced_fact_ids = {
            fact_id
            for hypothesis in self.blind_hypotheses
            for fact_id in (
                *hypothesis.supporting_fact_ids,
                *hypothesis.contradicting_fact_ids,
            )
        }
        if not referenced_fact_ids <= fact_ids:
            raise ValueError("memory critique hypothesis references an unknown current fact")
        if len(set(self.available_recipe_ids)) != len(self.available_recipe_ids):
            raise ValueError("memory critique input contains duplicate recipe IDs")
        _assert_two_pass_output_safe(self.to_dict(), context=self.input_id)

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class ArchetypeHypothesis:
    archetype_id: str
    rank: int
    reason: str
    supporting_fact_ids: tuple[str, ...]
    contradicting_fact_ids: tuple[str, ...]
    recipe_ids: tuple[str, ...]

    def __post_init__(self) -> None:
        if self.rank <= 0 or not self.archetype_id.strip() or not self.reason.strip():
            raise ValueError("archetype hypothesis requires identity, rank, and reason")
        if not self.supporting_fact_ids:
            raise ValueError("archetype hypothesis requires supporting current facts")
        _assert_two_pass_output_safe(self.to_dict(), context=self.archetype_id)

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class PlannerSourceTaskDraft:
    draft_id: str
    recipe_id: str
    question_to_answer: str
    why_material: str
    query_intent: str
    preferred_source_families: tuple[str, ...]
    fallback_source_families: tuple[str, ...]
    max_queries: int
    max_candidates: int
    max_fetches: int
    stop_condition: str

    def __post_init__(self) -> None:
        required = (
            self.draft_id,
            self.recipe_id,
            self.question_to_answer,
            self.why_material,
            self.query_intent,
            self.stop_condition,
        )
        if not all(value.strip() for value in required):
            raise ValueError("planner source-task draft fields must be non-empty")
        if not self.preferred_source_families:
            raise ValueError("planner source-task draft requires preferred sources")
        if min(self.max_queries, self.max_candidates, self.max_fetches) <= 0:
            raise ValueError("planner source-task draft budgets must be bounded and positive")
        _assert_two_pass_output_safe(self.to_dict(), context=self.draft_id)

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class MemoryCritiqueOutput:
    input_id: str
    top_k_archetypes: tuple[ArchetypeHypothesis, ...]
    supporting_current_fact_ids: tuple[str, ...]
    contradicting_current_fact_ids: tuple[str, ...]
    positive_thesis: str
    counter_thesis: str
    must_verify_questions: tuple[str, ...]
    red_team_questions: tuple[str, ...]
    source_task_drafts: tuple[PlannerSourceTaskDraft, ...]
    do_not_promote_reasons: tuple[str, ...]
    ambiguity_reasons: tuple[str, ...]
    abstain: bool
    abstention_reason: str | None

    def __post_init__(self) -> None:
        if not self.input_id.strip():
            raise ValueError("memory critique output requires input id")
        if self.abstain and not str(self.abstention_reason or "").strip():
            raise ValueError("memory critique abstention requires a reason")
        if not self.abstain:
            required = (
                self.top_k_archetypes,
                self.supporting_current_fact_ids,
                self.positive_thesis,
                self.counter_thesis,
                self.must_verify_questions,
                self.red_team_questions,
                self.do_not_promote_reasons,
            )
            if not all(required):
                raise ValueError("non-abstaining critique output is incomplete")
        ranks = [item.rank for item in self.top_k_archetypes]
        if ranks != list(range(1, len(ranks) + 1)):
            raise ValueError("archetype hypotheses must use contiguous rank order")
        if len({item.archetype_id for item in self.top_k_archetypes}) != len(
            self.top_k_archetypes
        ):
            raise ValueError("archetype hypotheses require unique IDs")
        _assert_two_pass_output_safe(self.to_dict(), context=self.input_id)

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class ProviderCallTrace:
    planner_pass: str
    provider_name: str
    real_provider: bool
    fake_provider: bool
    prompt_hash: str
    response_hash: str

    def __post_init__(self) -> None:
        PlannerPass(self.planner_pass)
        if not all(
            value.strip()
            for value in (
                self.provider_name,
                self.prompt_hash,
                self.response_hash,
            )
        ):
            raise ValueError("provider call trace requires provider and hashes")
        if self.real_provider and self.fake_provider:
            raise ValueError("provider cannot be both real and fake")
        if not _is_sha256(self.prompt_hash) or not _is_sha256(self.response_hash):
            raise ValueError("provider call trace hashes must be SHA-256 hex")

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class PlannerPending:
    input_id: str
    failed_pass: str
    reason_code: str
    reason_detail: str
    provider_name: str
    prompt_hash: str
    response_hash: str

    def __post_init__(self) -> None:
        PlannerPass(self.failed_pass)
        if not all(
            value.strip()
            for value in (
                self.input_id,
                self.reason_code,
                self.reason_detail,
                self.provider_name,
                self.prompt_hash,
                self.response_hash,
            )
        ):
            raise ValueError("planner pending requires exact provider failure provenance")
        if not _is_sha256(self.prompt_hash) or not _is_sha256(self.response_hash):
            raise ValueError("planner pending hashes must be SHA-256 hex")

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class TwoPassPlan:
    plan_id: str
    blind_input_id: str
    status: str
    blind_output: BlindHypothesisOutput | None
    critique_output: MemoryCritiqueOutput | None
    pending: PlannerPending | None
    provider_traces: tuple[ProviderCallTrace, ...]
    deterministic_stage_or_score_mutation: bool = False

    def __post_init__(self) -> None:
        PlannerStatus(self.status)
        if not self.plan_id.strip() or not self.blind_input_id.strip():
            raise ValueError("two-pass plan identity is required")
        if self.deterministic_stage_or_score_mutation:
            raise ValueError("Research Brain cannot mutate deterministic score or stage")
        if self.blind_output is not None and self.blind_output.input_id != self.blind_input_id:
            raise ValueError("two-pass plan blind output identity mismatch")
        if self.pending is not None and self.pending.input_id != self.blind_input_id:
            raise ValueError("two-pass plan pending identity mismatch")
        if self.status == PlannerStatus.PENDING.value:
            if self.pending is None or self.critique_output is not None:
                raise ValueError("pending plan requires pending detail and no critique output")
        elif self.status == PlannerStatus.COMPLETE.value:
            if self.pending is not None or self.blind_output is None or self.critique_output is None:
                raise ValueError("complete plan requires both pass outputs")
            if self.critique_output.abstain:
                raise ValueError("complete plan cannot carry critique abstention")
        else:
            if self.pending is not None or self.blind_output is None:
                raise ValueError("abstained plan requires blind output and no pending state")
            if self.critique_output is not None and not self.critique_output.abstain:
                raise ValueError("abstained plan critique must also abstain")
        _assert_two_pass_output_safe(
            {
                "blind_output": self.blind_output.to_dict() if self.blind_output else None,
                "critique_output": (
                    self.critique_output.to_dict() if self.critique_output else None
                ),
                "deterministic_stage_or_score_mutation": (
                    self.deterministic_stage_or_score_mutation
                ),
            },
            context=self.plan_id,
        )

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class QuarantineRecord:
    quarantine_id: str
    artifact_id: str
    source_file: str
    source_line_range: SourceLineRange
    reason: str
    row_id: str | None = None
    details: Mapping[str, Any] = field(default_factory=dict)
    raw_text: str = ""

    def __post_init__(self) -> None:
        QuarantineReason(self.reason)

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class LinkageError:
    linkage_error_id: str
    artifact_id: str
    source_file: str
    source_row_id: str
    source_line_range: SourceLineRange
    relation: str
    missing_or_conflicting_id: str
    details: Mapping[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


_FORBIDDEN_PLANNER_MEMORY_PATTERN = re.compile(
    r"(?:^|[^a-z0-9])(?:"
    r"mfe(?:[_-]?[0-9]+[a-z]*)?|"
    r"mae(?:[_-]?[0-9]+[a-z]*)?|"
    r"future[_ -]?return|"
    r"future[_ -]?outcome|"
    r"outcome[_ -]?label|"
    r"expected[_ -]?stage|"
    r"price[_ -]?metrics|"
    r"current[_ -]?profile[_ -]?verdict"
    r")(?:$|[^a-z0-9])",
    re.IGNORECASE,
)
_CANONICAL_ARCHETYPE_TOKEN_PATTERN = re.compile(
    r"(?:^|[^A-Za-z0-9])(?:C[0-9]{2}|R13)_[A-Z0-9_]+(?:$|[^A-Za-z0-9])",
    re.IGNORECASE,
)
_FORBIDDEN_STAGE_SCORE_TEXT_PATTERN = re.compile(
    r"(?:target[_ -]?score|expected[_ -]?stage|"
    r"(?:e2r|final|planner|target)\s+score\s*(?:[:=]|is|was)?\s*[0-9]|"
    r"score\s*(?:[:=]|is\s|was\s|of\s)\s*[0-9]|"
    r"(?:canonical|e2r|expected|target)\s+stage|"
    r"stage\s*[:=]\s*(?:0|1|2|3|4[abc]?|5|3-(?:green|yellow|red))|"
    r"stage\s+(?:3-(?:green|yellow|red)|4[abc])|"
    r"stage[0-9]+-(?:green|yellow|red)|source[_ -]?primary)",
    re.IGNORECASE,
)
_FORBIDDEN_TWO_PASS_KEYS = frozenset(
    {
        "score",
        "stage",
        "target_score",
        "target_stage",
        "expected_stage",
        "current_score_eligible",
        "feature_input",
        "score_contribution",
        "verified_score",
        "provisional_score",
        "base_stage",
        "source_primary",
        "expected_archetype_id",
        "expected_primitive_id",
        "outcome_label",
        "price_metrics",
        "current_profile_verdict",
    }
)
_ALLOWED_TWO_PASS_AUDIT_KEYS = frozenset(
    {"deterministic_stage_or_score_mutation", "forbidden_score_sources"}
)


def _is_sha256(value: str) -> bool:
    return re.fullmatch(r"[0-9a-f]{64}", value) is not None


def _assert_planner_memory_safe(value: Any, *, context: str) -> None:
    serialized = json.dumps(_json_safe(value), ensure_ascii=False, sort_keys=True)
    match = _FORBIDDEN_PLANNER_MEMORY_PATTERN.search(serialized)
    if match:
        raise ValueError(f"{context} contains forbidden historical outcome token: {match.group(0)!r}")


def _assert_blind_pass_payload_safe(value: Any, *, context: str) -> None:
    _assert_two_pass_output_safe(value, context=context)
    serialized = json.dumps(_json_safe(value), ensure_ascii=False, sort_keys=True)
    if _CANONICAL_ARCHETYPE_TOKEN_PATTERN.search(serialized):
        raise ValueError(f"blind pass {context} contains an archetype label")
    for key in _iter_mapping_keys(value):
        normalized = str(key).strip().lower()
        if "archetype" in normalized or normalized == "source_primary":
            raise ValueError(f"blind pass {context} contains forbidden key {key!r}")


def _assert_two_pass_output_safe(value: Any, *, context: str) -> None:
    for key, item in _iter_mapping_items(value):
        normalized = str(key).strip().lower()
        if normalized in _ALLOWED_TWO_PASS_AUDIT_KEYS:
            if normalized == "deterministic_stage_or_score_mutation" and bool(item):
                raise ValueError(f"two-pass payload {context} mutates score/stage")
            continue
        if (
            normalized in _FORBIDDEN_TWO_PASS_KEYS
            or normalized.endswith("_score")
            or normalized.endswith("_stage")
            or normalized.startswith("score_")
            or normalized.startswith("stage_")
        ):
            raise ValueError(f"two-pass payload {context} contains forbidden key {key!r}")
    serialized = json.dumps(_json_safe(value), ensure_ascii=False, sort_keys=True)
    match = _FORBIDDEN_PLANNER_MEMORY_PATTERN.search(serialized)
    if match:
        raise ValueError(
            f"two-pass payload {context} contains historical outcome token: {match.group(0)!r}"
        )
    stage_score_scan_text = _CANONICAL_ARCHETYPE_TOKEN_PATTERN.sub(" ", serialized)
    if _FORBIDDEN_STAGE_SCORE_TEXT_PATTERN.search(stage_score_scan_text):
        raise ValueError(f"two-pass payload {context} contains score/stage target text")


def _iter_mapping_keys(value: Any):
    if isinstance(value, Mapping):
        for key, item in value.items():
            yield key
            yield from _iter_mapping_keys(item)
    elif isinstance(value, (tuple, list)):
        for item in value:
            yield from _iter_mapping_keys(item)


def _iter_mapping_items(value: Any):
    if isinstance(value, Mapping):
        for key, item in value.items():
            yield key, item
            yield from _iter_mapping_items(item)
    elif isinstance(value, (tuple, list)):
        for item in value:
            yield from _iter_mapping_items(item)


def _json_safe(value: Any) -> Any:
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, Mapping):
        return {str(key): _json_safe(item) for key, item in value.items()}
    if isinstance(value, (tuple, list, set, frozenset)):
        return [_json_safe(item) for item in value]
    if hasattr(value, "__dataclass_fields__"):
        return _json_safe(asdict(value))
    return value


__all__ = [
    "AcceptedClaimPredicate",
    "ArchetypeRetrievalHit",
    "BalancedMemoryRole",
    "BalancedRetrievalItem",
    "BalancedRetrievalRequest",
    "BalancedRetrievalResult",
    "BlindHypothesisInput",
    "BlindHypothesisOutput",
    "BlindMechanismHypothesis",
    "CurrentEvidenceFact",
    "EvidenceRecipe",
    "EvidenceRecipeRole",
    "INTELLIGENCE_SCHEMA_VERSION",
    "HistoricalEvidenceReference",
    "HistoricalCaseSourceLink",
    "HistoricalCaseSourceRelationship",
    "HistoricalOutcome",
    "HistoricalProviderSnapshot",
    "HistoricalResearchArtifact",
    "HistoricalResearchCase",
    "HistoricalRuleCandidate",
    "HistoricalSnapshotAnchor",
    "HistoricalSourceRepairTask",
    "HistoricalSourceState",
    "HistoricalSourceVerification",
    "HypothesisStrength",
    "LinkageError",
    "MemoryEdge",
    "MemoryEdgeType",
    "MemoryNode",
    "MemoryNodeType",
    "MemoryCritiqueInput",
    "MemoryCritiqueOutput",
    "NarrativeCaseCandidate",
    "ParsedResearchArtifact",
    "ParsedResearchRow",
    "ParsedRowKind",
    "PlannerPass",
    "PlannerPending",
    "PlannerSourceTaskDraft",
    "PlannerStatus",
    "ProviderCallTrace",
    "QuarantineReason",
    "QuarantineRecord",
    "ResearchMemoryGraph",
    "SemanticMemoryIndexEntry",
    "SourceLineRange",
    "TwoPassPlan",
    "UnsupportedEvidenceRecipe",
    "ArchetypeHypothesis",
    "stable_intelligence_id",
]
