"""Canonical schemas for reconstructed E2R research intelligence."""

from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass, field
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
    "LinkageError",
    "NarrativeCaseCandidate",
    "ParsedResearchArtifact",
    "ParsedResearchRow",
    "ParsedRowKind",
    "QuarantineReason",
    "QuarantineRecord",
    "SourceLineRange",
    "UnsupportedEvidenceRecipe",
    "stable_intelligence_id",
]
