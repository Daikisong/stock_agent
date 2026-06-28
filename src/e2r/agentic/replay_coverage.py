"""Coverage helpers for source-backed replay planning.

The functions in this module do not score anything. They only separate rows
that can be investigated as source-backed replay candidates from rows that
must remain ontology/gap references because they are proxy-only, URL-pending,
or otherwise unverified research summaries.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import date
import hashlib
import json
from pathlib import Path
import re
from typing import Any, Iterable, Mapping, Sequence
from urllib import parse

from e2r.calibration.taxonomy import normalise_canonical_archetype_id
from e2r.agentic.evidence_os import (
    AdjudicatedClaim,
    AnchorType,
    Directness,
    EvidenceContractV2,
    EvidenceAnchor,
    EvidenceDocument,
    InvestigationStatus,
    Polarity,
    PrimitiveStateV2,
    PrimitiveStatus,
    RelationToTarget,
    ScoreContributionV2,
    ScoreInterval,
    SemanticStatus,
    SourceType,
    TargetScopeStatus,
    TemporalStatus,
    VerificationStatus,
)
from e2r.agentic.evidence_workflow import (
    ADJUDICATION_OUTPUT_FIELDS,
    PRIMITIVE_MAPPING_ROW_FIELDS,
    decode_adjudication_proposal,
    decode_claim_extraction_output,
    decode_primitive_mapping_output,
)
from e2r.agentic.stage_court import StageCourtInput, decide_stage_court


class ReplaySourceStatus:
    SOURCE_BACKED_CANDIDATE = "source_backed_candidate"
    SOURCE_PROXY_OR_PENDING = "source_proxy_or_pending"
    UNVERIFIED_RESEARCH_ROW = "unverified_research_row"


COVERAGE_AVAILABLE = "source_backed_candidate_available"
COVERAGE_GAP_WITH_ROWS = "source_gap_only_proxy_or_unverified_rows"
COVERAGE_GAP_NO_ROWS = "source_gap_no_rows_observed"

_ARCHETYPE_KEYS = (
    "canonical_archetype_id",
    "archetype_id",
    "primary_archetype",
    "source_canonical_archetype_id",
    "source_archetype_id",
)
_SOURCE_TEXT_KEYS = (
    "evidence_source",
    "evidence_url",
    "source_url",
    "url",
    "source_ref",
    "evidence_ref",
    "source",
    "source_name",
)
_SOURCE_ANCHOR_PREFIXES = (
    "http://",
    "https://",
    "fixture://",
    "dart://",
    "kind://",
    "xbrl://",
    "api://",
)
_PROXY_MARKERS = (
    "source_proxy",
    "proxy_only",
    "manual_verification_required",
    "evidence_url_pending",
)


@dataclass(frozen=True)
class ReplaySourceClassification:
    archetype_id: str | None
    status: str
    reasons: tuple[str, ...]
    source_path: str | None = None
    source_line: int | None = None


@dataclass(frozen=True)
class ReplayCoverageRow:
    archetype_id: str
    total_rows: int
    source_backed_candidate_count: int
    source_proxy_or_pending_count: int
    unverified_research_row_count: int
    coverage_status: str
    example_source_backed_rows: tuple[str, ...] = ()
    example_source_proxy_or_pending_rows: tuple[str, ...] = ()
    example_unverified_rows: tuple[str, ...] = ()


@dataclass(frozen=True)
class SourceBackedReplayCandidate:
    archetype_id: str
    candidate_id: str
    row_fingerprint: str
    source_anchors: tuple[str, ...]
    source_path: str | None = None
    source_line: int | None = None
    case_id: str | None = None
    trigger_id: str | None = None
    symbol: str | None = None
    company_name: str | None = None
    fine_archetype_id: str | None = None
    trigger_date: str | None = None
    entry_date: str | None = None
    stage_label_before: str | None = None
    stage_label_after: str | None = None
    replay_role: str = "source_document_fixture_candidate"
    production_score_fixture: bool = False
    selection_reasons: tuple[str, ...] = ()


@dataclass(frozen=True)
class SourceBackedReplayFixtureSeed:
    archetype_id: str
    candidate_id: str
    fixture_seed_id: str
    source_anchor: str
    as_of_date: str | None
    snapshot_status: str
    snapshot_request_ready: bool
    evidence_document_fixture_ready: bool = False
    production_score_fixture: bool = False
    source_path: str | None = None
    source_line: int | None = None
    case_id: str | None = None
    trigger_id: str | None = None
    symbol: str | None = None
    company_name: str | None = None
    trigger_date: str | None = None
    entry_date: str | None = None


@dataclass(frozen=True)
class SourceBackedSnapshotAvailability:
    fixture_seed_id: str
    candidate_id: str
    archetype_id: str
    source_anchor: str
    as_of_date: str | None
    snapshot_status: str
    snapshot_url: str | None = None
    snapshot_as_of_date: str | None = None
    snapshot_source_type: str | None = None
    snapshot_title: str | None = None
    extracted_text_path: str | None = None
    extracted_text_hash: str | None = None
    evidence_document_fixture_ready: bool = False
    production_score_fixture: bool = False
    reasons: tuple[str, ...] = ()


@dataclass(frozen=True)
class SourceBackedCurrentFetchStatus:
    fixture_seed_id: str
    candidate_id: str
    archetype_id: str
    source_anchor: str
    as_of_date: str | None
    current_fetch_status: str
    fetched_at: str | None = None
    content_type: str | None = None
    current_text_path: str | None = None
    current_text_hash: str | None = None
    current_text_chars: int = 0
    reason: str | None = None
    asof_snapshot_verified: bool = False
    evidence_document_fixture_ready: bool = False
    production_score_fixture: bool = False
    reasons: tuple[str, ...] = ()


@dataclass(frozen=True)
class SourceBackedSnapshotRemediationTask:
    task_id: str
    fixture_seed_id: str
    candidate_id: str
    archetype_id: str
    source_anchor: str
    as_of_date: str | None
    input_status: str
    remediation_type: str
    priority: int
    target_state: str
    score_blocked_until_resolved: bool = True
    suggested_actions: tuple[str, ...] = ()
    reasons: tuple[str, ...] = ()


@dataclass(frozen=True)
class SourceBackedCurrentTextAsofPrecheck:
    fixture_seed_id: str
    candidate_id: str
    archetype_id: str
    source_anchor: str
    as_of_date: str | None
    current_text_path: str | None
    precheck_status: str
    date_hints: tuple[str, ...] = ()
    asof_precheck_candidate: bool = False
    asof_snapshot_verified: bool = False
    evidence_document_fixture_ready: bool = False
    production_score_fixture: bool = False
    reasons: tuple[str, ...] = ()


@dataclass(frozen=True)
class SourceBackedEvidenceDocumentFixture:
    fixture_seed_id: str
    candidate_id: str
    archetype_id: str
    source_anchor: str
    as_of_date: str | None
    fixture_status: str
    document_id: str | None = None
    anchor_id: str | None = None
    canonical_url: str | None = None
    source_type: str | None = None
    source_name: str | None = None
    source_lineage_id: str | None = None
    content_hash: str | None = None
    snapshot_as_of_date: str | None = None
    extracted_text_path: str | None = None
    anchor_locator: str | None = None
    anchor_verified: bool = False
    evidence_document_fixture_ready: bool = False
    claim_replay_ready: bool = False
    production_score_fixture: bool = False
    score_block_reasons: tuple[str, ...] = ()
    reasons: tuple[str, ...] = ()


@dataclass(frozen=True)
class SourceBackedAsofSnapshotAcquisitionTask:
    task_id: str
    fixture_seed_id: str
    candidate_id: str
    archetype_id: str
    source_anchor: str
    as_of_date: str | None
    task_type: str
    priority: int
    date_window_start: str | None
    date_window_end: str | None
    max_archive_lookups: int
    max_browser_fetches: int
    max_alternative_source_candidates: int
    max_total_fetches: int
    stop_condition: str
    llm_followup_required: bool
    score_blocked_until_verified: bool = True
    production_score_fixture: bool = False
    reasons: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.task_id.strip():
            raise ValueError("task_id must be non-empty")
        if not self.fixture_seed_id.strip():
            raise ValueError("fixture_seed_id must be non-empty")
        if not self.source_anchor.strip():
            raise ValueError("source_anchor must be non-empty")
        for field_name in (
            "max_archive_lookups",
            "max_browser_fetches",
            "max_alternative_source_candidates",
            "max_total_fetches",
        ):
            value = getattr(self, field_name)
            if value is None or value < 0:
                raise ValueError(f"{field_name} must be a bounded non-negative integer")
        if self.max_total_fetches <= 0:
            raise ValueError("max_total_fetches must be positive")
        if not self.stop_condition.strip():
            raise ValueError("stop_condition must be non-empty")


@dataclass(frozen=True)
class SourceBackedAsofSnapshotVerificationResult:
    task_id: str
    fixture_seed_id: str
    candidate_id: str
    archetype_id: str
    source_anchor: str
    as_of_date: str | None
    verification_status: str
    snapshot_url: str | None = None
    snapshot_as_of_date: str | None = None
    snapshot_source_type: str | None = None
    snapshot_title: str | None = None
    extracted_text_path: str | None = None
    extracted_text_hash: str | None = None
    source_replacement_verified: bool = False
    evidence_document_fixture_ready: bool = False
    production_score_fixture: bool = False
    reasons: tuple[str, ...] = ()


@dataclass(frozen=True)
class SourceBackedAsofSnapshotVerifierTask:
    verifier_task_id: str
    acquisition_task_id: str
    fixture_seed_id: str
    candidate_id: str
    archetype_id: str
    source_anchor: str
    as_of_date: str | None
    input_task_type: str
    verifier_task_status: str
    required_output: str
    snapshot_url: str | None = None
    snapshot_source_type: str | None = None
    extracted_text_path: str | None = None
    extracted_text_hash: str | None = None
    extracted_text_chars: int = 0
    date_hints: tuple[str, ...] = ()
    score_blocked_until_verified: bool = True
    source_replacement_verified: bool = False
    asof_snapshot_verified: bool = False
    evidence_document_fixture_ready: bool = False
    production_score_fixture: bool = False
    forbidden_context: tuple[str, ...] = (
        "evidence_contract",
        "missing_primitive",
        "score_gap",
        "current_score",
        "stage_gate",
        "green_gate",
    )
    reasons: tuple[str, ...] = ()


@dataclass(frozen=True)
class SourceBackedAsofSnapshotVerifierResult:
    result_id: str
    verifier_task_id: str
    acquisition_task_id: str
    fixture_seed_id: str
    candidate_id: str
    archetype_id: str
    source_anchor: str
    as_of_date: str | None
    snapshot_url: str | None
    snapshot_source_type: str | None
    extracted_text_path: str | None
    extracted_text_hash: str | None
    extracted_text_chars: int
    result_status: str
    source_identity_decision: str | None = None
    snapshot_as_of_date: str | None = None
    snapshot_title: str | None = None
    forbidden_output_fields: tuple[str, ...] = ()
    source_replacement_verified: bool = False
    asof_snapshot_verified: bool = False
    evidence_document_fixture_ready: bool = False
    production_score_fixture: bool = False
    accepted_attempt_row: Mapping[str, Any] | None = None
    reasons: tuple[str, ...] = ()


@dataclass(frozen=True)
class SourceBackedReplacementSourceRequest:
    request_id: str
    task_id: str
    fixture_seed_id: str
    candidate_id: str
    archetype_id: str
    source_anchor: str
    as_of_date: str | None
    task_type: str
    request_status: str
    llm_followup_required: bool
    deterministic_queries_generated: bool = False
    suggested_queries: tuple[str, ...] = ()
    required_output: str = "same_event_candidate_sources"
    asof_constraint: str = "candidate_source_available_on_or_before_as_of_date"
    acceptance_criteria: tuple[str, ...] = (
        "same_underlying_event_as_source_anchor",
        "source_anchor_or_replacement_identity_verified",
        "snapshot_as_of_date_on_or_before_seed_as_of_date",
        "text_snapshot_available",
        "claim_replay_required_before_score",
    )
    production_score_fixture: bool = False
    reasons: tuple[str, ...] = ()


@dataclass(frozen=True)
class SourceBackedReplacementSourceCandidate:
    request_id: str
    fixture_seed_id: str
    candidate_id: str
    archetype_id: str
    original_source_anchor: str
    as_of_date: str | None
    replacement_candidate_id: str
    candidate_url: str | None
    candidate_title: str | None
    candidate_status: str
    candidate_available_date: str | None = None
    llm_rationale: str | None = None
    source_replacement_verified: bool = False
    asof_snapshot_verified: bool = False
    evidence_document_fixture_ready: bool = False
    production_score_fixture: bool = False
    reasons: tuple[str, ...] = ()


@dataclass(frozen=True)
class SourceBackedReplacementCandidateAcquisitionTask:
    task_id: str
    replacement_candidate_id: str
    request_id: str
    fixture_seed_id: str
    candidate_id: str
    archetype_id: str
    original_source_anchor: str
    candidate_url: str
    as_of_date: str | None
    task_type: str
    priority: int
    date_window_start: str | None
    date_window_end: str | None
    max_archive_lookups: int
    max_browser_fetches: int
    max_total_fetches: int
    stop_condition: str
    score_blocked_until_verified: bool = True
    source_replacement_verified: bool = False
    asof_snapshot_verified: bool = False
    evidence_document_fixture_ready: bool = False
    production_score_fixture: bool = False
    reasons: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.task_id.strip():
            raise ValueError("task_id must be non-empty")
        if not self.replacement_candidate_id.strip():
            raise ValueError("replacement_candidate_id must be non-empty")
        if not self.candidate_url.strip():
            raise ValueError("candidate_url must be non-empty")
        for field_name in ("max_archive_lookups", "max_browser_fetches", "max_total_fetches"):
            value = getattr(self, field_name)
            if value is None or value < 0:
                raise ValueError(f"{field_name} must be a bounded non-negative integer")
        if self.max_total_fetches <= 0:
            raise ValueError("max_total_fetches must be positive")
        if not self.stop_condition.strip():
            raise ValueError("stop_condition must be non-empty")


@dataclass(frozen=True)
class SourceBackedReplacementCandidateFetchStatus:
    task_id: str
    replacement_candidate_id: str
    request_id: str
    fixture_seed_id: str
    candidate_id: str
    archetype_id: str
    original_source_anchor: str
    candidate_url: str
    as_of_date: str | None
    fetch_status: str
    fetched_at: str | None = None
    content_type: str | None = None
    current_text_path: str | None = None
    current_text_hash: str | None = None
    current_text_chars: int = 0
    reason: str | None = None
    source_replacement_verified: bool = False
    asof_snapshot_verified: bool = False
    evidence_document_fixture_ready: bool = False
    production_score_fixture: bool = False
    reasons: tuple[str, ...] = ()


@dataclass(frozen=True)
class SourceBackedReplacementSnapshotVerificationResult:
    task_id: str
    replacement_candidate_id: str
    request_id: str
    fixture_seed_id: str
    candidate_id: str
    archetype_id: str
    original_source_anchor: str
    candidate_url: str
    as_of_date: str | None
    verification_status: str
    snapshot_url: str | None = None
    snapshot_as_of_date: str | None = None
    snapshot_source_type: str | None = None
    snapshot_title: str | None = None
    extracted_text_path: str | None = None
    extracted_text_hash: str | None = None
    extracted_text_chars: int = 0
    source_replacement_verified: bool = False
    asof_snapshot_verified: bool = False
    evidence_document_fixture_ready: bool = False
    production_score_fixture: bool = False
    reasons: tuple[str, ...] = ()


@dataclass(frozen=True)
class SourceBackedReplacementSnapshotRequest:
    request_id: str
    task_id: str
    replacement_candidate_id: str
    fixture_seed_id: str
    candidate_id: str
    archetype_id: str
    original_source_anchor: str
    candidate_url: str
    as_of_date: str | None
    input_verification_status: str
    request_status: str
    required_output: str
    snapshot_url: str | None = None
    snapshot_source_type: str | None = None
    extracted_text_path: str | None = None
    extracted_text_hash: str | None = None
    extracted_text_chars: int = 0
    score_blocked_until_resolved: bool = True
    source_replacement_verified: bool = False
    asof_snapshot_verified: bool = False
    evidence_document_fixture_ready: bool = False
    production_score_fixture: bool = False
    acceptance_criteria: tuple[str, ...] = (
        "candidate_source_text_snapshot_available",
        "same_underlying_event_as_original_source_anchor",
        "snapshot_as_of_date_on_or_before_seed_as_of_date",
        "content_hash_recorded",
        "claim_replay_required_before_score",
    )
    reasons: tuple[str, ...] = ()


@dataclass(frozen=True)
class SourceBackedReplacementSnapshotVerifierTask:
    task_id: str
    request_id: str
    replacement_candidate_id: str
    fixture_seed_id: str
    candidate_id: str
    archetype_id: str
    original_source_anchor: str
    candidate_url: str
    as_of_date: str | None
    input_request_status: str
    verifier_task_status: str
    required_output: str
    snapshot_url: str | None = None
    snapshot_source_type: str | None = None
    extracted_text_path: str | None = None
    extracted_text_hash: str | None = None
    extracted_text_chars: int = 0
    score_blocked_until_verified: bool = True
    source_replacement_verified: bool = False
    asof_snapshot_verified: bool = False
    evidence_document_fixture_ready: bool = False
    production_score_fixture: bool = False
    forbidden_context: tuple[str, ...] = (
        "evidence_contract",
        "missing_primitive",
        "score_gap",
        "current_score",
        "stage_gate",
    )
    acceptance_criteria: tuple[str, ...] = (
        "same_underlying_event_as_original_source_anchor",
        "snapshot_as_of_date_on_or_before_seed_as_of_date",
        "content_hash_matches_extracted_text",
        "no_score_or_stage_output",
    )
    reasons: tuple[str, ...] = ()


@dataclass(frozen=True)
class SourceBackedReplacementSnapshotVerifierResult:
    result_id: str
    verifier_task_id: str
    request_id: str
    replacement_candidate_id: str
    fixture_seed_id: str
    candidate_id: str
    archetype_id: str
    original_source_anchor: str
    candidate_url: str
    as_of_date: str | None
    result_status: str
    same_event_decision: str | None = None
    snapshot_url: str | None = None
    snapshot_as_of_date: str | None = None
    snapshot_source_type: str | None = None
    snapshot_title: str | None = None
    extracted_text_path: str | None = None
    extracted_text_hash: str | None = None
    extracted_text_chars: int = 0
    source_replacement_verified: bool = False
    asof_snapshot_verified: bool = False
    evidence_document_fixture_ready: bool = False
    production_score_fixture: bool = False
    forbidden_output_fields: tuple[str, ...] = ()
    accepted_verification_row: Mapping[str, Any] | None = None
    reasons: tuple[str, ...] = ()


@dataclass(frozen=True)
class SourceBackedReplacementEvidenceDocumentFixture:
    task_id: str
    replacement_candidate_id: str
    request_id: str
    fixture_seed_id: str
    candidate_id: str
    archetype_id: str
    original_source_anchor: str
    candidate_url: str
    as_of_date: str | None
    fixture_status: str
    document_id: str | None = None
    anchor_id: str | None = None
    canonical_url: str | None = None
    source_type: str | None = None
    source_name: str | None = None
    source_lineage_id: str | None = None
    content_hash: str | None = None
    snapshot_as_of_date: str | None = None
    extracted_text_path: str | None = None
    anchor_locator: str | None = None
    anchor_verified: bool = False
    evidence_document_fixture_ready: bool = False
    claim_replay_ready: bool = False
    production_score_fixture: bool = False
    score_block_reasons: tuple[str, ...] = ()
    reasons: tuple[str, ...] = ()


@dataclass(frozen=True)
class SourceBackedClaimReplayTask:
    task_id: str
    fixture_kind: str
    fixture_seed_id: str
    candidate_id: str
    archetype_id: str
    target_entity_id: str
    target_names: tuple[str, ...]
    as_of_date: str | None
    document_id: str
    anchor_id: str
    canonical_url: str | None
    source_type: str | None
    source_name: str | None
    source_lineage_id: str | None
    content_hash: str
    extracted_text_path: str
    anchor_locator: str | None
    document_published_at: str | None = None
    contract_blind_extraction: bool = True
    score_blocked_until_claim_replay: bool = True
    production_score_fixture: bool = False
    replacement_candidate_id: str | None = None
    original_source_anchor: str | None = None
    candidate_url: str | None = None
    forbidden_context_excluded: tuple[str, ...] = (
        "score_gap_context",
        "missing_primitives",
        "evidence_contract",
        "existing_claim_ledger",
        "current_primitive_state",
        "score_contribution_ledger",
        "stage_court_result",
        "current_score",
        "stage_gate_target",
    )
    reasons: tuple[str, ...] = ("evidence_document_fixture_ready_for_contract_blind_claim_extraction",)


@dataclass(frozen=True)
class SourceBackedClaimReplayResult:
    task_id: str
    fixture_kind: str
    fixture_seed_id: str
    candidate_id: str
    archetype_id: str
    target_entity_id: str
    target_names: tuple[str, ...]
    as_of_date: str | None
    document_id: str
    anchor_id: str
    replay_status: str
    canonical_url: str | None = None
    source_type: str | None = None
    source_name: str | None = None
    source_lineage_id: str | None = None
    content_hash: str | None = None
    extracted_text_path: str | None = None
    anchor_locator: str | None = None
    document_published_at: str | None = None
    raw_assertion_count: int = 0
    raw_assertion_ids: tuple[str, ...] = ()
    raw_assertions: tuple[Mapping[str, Any], ...] = ()
    blocked_reason: str | None = None
    extraction_status: str | None = None
    contract_blind_extraction: bool = True
    adjudication_ready: bool = False
    score_blocked_until_adjudication: bool = True
    production_score_fixture: bool = False
    replacement_candidate_id: str | None = None
    original_source_anchor: str | None = None
    candidate_url: str | None = None
    reasons: tuple[str, ...] = ()


@dataclass(frozen=True)
class SourceBackedAdjudicationTask:
    task_id: str
    claim_replay_task_id: str
    raw_assertion_id: str
    fixture_kind: str
    fixture_seed_id: str
    candidate_id: str
    archetype_id: str
    target_entity_id: str
    target_names: tuple[str, ...]
    as_of_date: str | None
    document_id: str
    anchor_id: str
    subject_text: str
    predicate: str
    exact_quote: str
    canonical_url: str | None = None
    source_type: str | None = None
    source_name: str | None = None
    source_lineage_id: str | None = None
    content_hash: str | None = None
    extracted_text_path: str | None = None
    anchor_locator: str | None = None
    document_published_at: str | None = None
    replacement_candidate_id: str | None = None
    original_source_anchor: str | None = None
    candidate_url: str | None = None
    raw_assertion: Mapping[str, Any] | None = None
    score_blocked_until_adjudication: bool = True
    production_score_fixture: bool = False
    reasons: tuple[str, ...] = ("raw_assertion_ready_for_target_temporal_adjudication",)


@dataclass(frozen=True)
class SourceBackedAdjudicationResult:
    task_id: str
    claim_replay_task_id: str
    raw_assertion_id: str
    fixture_kind: str
    fixture_seed_id: str
    candidate_id: str
    archetype_id: str
    target_entity_id: str
    target_names: tuple[str, ...]
    as_of_date: str | None
    document_id: str
    anchor_id: str
    adjudication_status: str
    subject_entity_id: str | None = None
    relation_to_target: str | None = None
    directness: str | None = None
    target_scope_status: str | None = None
    polarity: str | None = None
    temporal_status: str | None = None
    semantic_status: str | None = None
    investigation_status: str | None = None
    event_date: str | None = None
    effective_start: str | None = None
    effective_end: str | None = None
    rationale: str = ""
    canonical_url: str | None = None
    source_type: str | None = None
    source_name: str | None = None
    source_lineage_id: str | None = None
    content_hash: str | None = None
    extracted_text_path: str | None = None
    anchor_locator: str | None = None
    document_published_at: str | None = None
    raw_assertion: Mapping[str, Any] | None = None
    mapping_ready: bool = False
    score_blocked_until_mapping: bool = True
    production_score_fixture: bool = False
    replacement_candidate_id: str | None = None
    original_source_anchor: str | None = None
    candidate_url: str | None = None
    blocked_reason: str | None = None
    reasons: tuple[str, ...] = ()


@dataclass(frozen=True)
class SourceBackedPrimitiveMappingTask:
    task_id: str
    claim_id: str
    adjudication_task_id: str
    claim_replay_task_id: str
    raw_assertion_id: str
    fixture_kind: str
    fixture_seed_id: str
    candidate_id: str
    archetype_id: str
    target_entity_id: str
    target_names: tuple[str, ...]
    subject_entity_id: str
    as_of_date: str | None
    document_id: str
    anchor_id: str
    relation_to_target: str
    directness: str
    target_scope_status: str
    polarity: str
    temporal_status: str
    semantic_status: str
    investigation_status: str
    event_date: str | None = None
    effective_start: str | None = None
    effective_end: str | None = None
    canonical_url: str | None = None
    source_type: str | None = None
    source_name: str | None = None
    source_lineage_id: str | None = None
    content_hash: str | None = None
    extracted_text_path: str | None = None
    anchor_locator: str | None = None
    document_published_at: str | None = None
    raw_assertion: Mapping[str, Any] | None = None
    replacement_candidate_id: str | None = None
    original_source_anchor: str | None = None
    candidate_url: str | None = None
    score_blocked_until_mapping: bool = True
    production_score_fixture: bool = False
    reasons: tuple[str, ...] = ("adjudicated_claim_ready_for_primitive_mapping",)


@dataclass(frozen=True)
class SourceBackedPrimitiveMappingResult:
    task_id: str
    primitive_mapping_task_id: str
    claim_id: str
    adjudication_task_id: str
    raw_assertion_id: str
    fixture_seed_id: str
    candidate_id: str
    archetype_id: str
    target_entity_id: str
    subject_entity_id: str
    as_of_date: str | None
    document_id: str
    anchor_id: str
    result_status: str
    relation_to_target: str = ""
    directness: str = ""
    target_scope_status: str = ""
    polarity: str = ""
    temporal_status: str = ""
    semantic_status: str = ""
    investigation_status: str = ""
    event_date: str | None = None
    effective_start: str | None = None
    effective_end: str | None = None
    canonical_url: str | None = None
    source_type: str | None = None
    source_name: str | None = None
    source_lineage_id: str | None = None
    content_hash: str | None = None
    extracted_text_path: str | None = None
    anchor_locator: str | None = None
    document_published_at: str | None = None
    raw_assertion: Mapping[str, Any] | None = None
    replacement_candidate_id: str | None = None
    original_source_anchor: str | None = None
    candidate_url: str | None = None
    primitive_id: str | None = None
    support_direction: str | None = None
    mapping_status: str | None = None
    contract_rule_id: str | None = None
    rationale: str = ""
    eligibility_ready: bool = False
    score_blocked_until_eligibility: bool = True
    production_score_fixture: bool = False
    blocked_reason: str | None = None
    reasons: tuple[str, ...] = ()


@dataclass(frozen=True)
class SourceBackedEligibilityTask:
    task_id: str
    primitive_mapping_result_id: str
    primitive_mapping_task_id: str
    claim_id: str
    adjudication_task_id: str
    raw_assertion_id: str
    fixture_seed_id: str
    candidate_id: str
    archetype_id: str
    target_entity_id: str
    subject_entity_id: str
    as_of_date: str | None
    document_id: str
    anchor_id: str
    primitive_id: str
    support_direction: str
    mapping_status: str
    relation_to_target: str = ""
    directness: str = ""
    target_scope_status: str = ""
    polarity: str = ""
    temporal_status: str = ""
    semantic_status: str = ""
    investigation_status: str = ""
    event_date: str | None = None
    effective_start: str | None = None
    effective_end: str | None = None
    canonical_url: str | None = None
    source_type: str | None = None
    source_name: str | None = None
    source_lineage_id: str | None = None
    content_hash: str | None = None
    extracted_text_path: str | None = None
    anchor_locator: str | None = None
    document_published_at: str | None = None
    contract_rule_id: str | None = None
    mapping_rationale: str = ""
    raw_assertion: Mapping[str, Any] | None = None
    replacement_candidate_id: str | None = None
    original_source_anchor: str | None = None
    candidate_url: str | None = None
    score_blocked_until_eligibility: bool = True
    production_score_fixture: bool = False
    reasons: tuple[str, ...] = ("primitive_mapping_ready_for_eligibility_checks",)


@dataclass(frozen=True)
class SourceBackedEligibilityResult:
    task_id: str
    eligibility_task_id: str
    primitive_mapping_result_id: str
    primitive_mapping_task_id: str
    claim_id: str
    raw_assertion_id: str
    fixture_seed_id: str
    candidate_id: str
    archetype_id: str
    target_entity_id: str
    subject_entity_id: str
    as_of_date: str | None
    source_lineage_id: str | None
    document_id: str
    anchor_id: str
    primitive_id: str
    support_direction: str
    result_status: str
    eligibility_source: str | None = None
    eligibility_ready: bool = False
    source_anchor_verified: bool = False
    future_leakage: bool = False
    source_proxy_only: bool = False
    snippet_only: bool = False
    unresolved_contradiction: bool = False
    score_blocked_until_score_contribution: bool = True
    production_score_fixture: bool = False
    blocked_reason: str | None = None
    reasons: tuple[str, ...] = ()


@dataclass(frozen=True)
class SourceBackedScoreContributionTask:
    task_id: str
    eligibility_result_id: str
    eligibility_task_id: str
    primitive_mapping_result_id: str
    raw_assertion_id: str
    fixture_seed_id: str
    candidate_id: str
    archetype_id: str
    target_entity_id: str
    subject_entity_id: str
    document_id: str
    anchor_id: str
    primitive_id: str
    support_direction: str
    score_blocked_until_score_contribution: bool = True
    production_score_fixture: bool = False
    reasons: tuple[str, ...] = ("eligible_mapping_ready_for_score_contribution_builder",)


@dataclass(frozen=True)
class SourceBackedScoreContributionResult:
    task_id: str
    score_contribution_task_id: str
    eligibility_result_id: str
    raw_assertion_id: str
    fixture_seed_id: str
    candidate_id: str
    archetype_id: str
    target_entity_id: str
    subject_entity_id: str
    document_id: str
    anchor_id: str
    primitive_id: str
    support_direction: str
    result_status: str
    component_key: str | None = None
    criterion_id: str | None = None
    raw_points: float = 0.0
    max_points: float = 0.0
    contribution_id: str | None = None
    support_claim_ids: tuple[str, ...] = ()
    counter_claim_ids: tuple[str, ...] = ()
    mapping_ids: tuple[str, ...] = ()
    source_family_ids: tuple[str, ...] = ()
    cap_reason: str | None = None
    rationale: str = ""
    score_contribution_ready: bool = False
    production_score_fixture: bool = False
    blocked_reason: str | None = None
    reasons: tuple[str, ...] = ()


@dataclass(frozen=True)
class SourceBackedScoreSnapshotTask:
    task_id: str
    fixture_seed_id: str
    candidate_id: str
    archetype_id: str
    target_entity_id: str
    contribution_ids: tuple[str, ...]
    score_contribution_result_ids: tuple[str, ...]
    component_keys: tuple[str, ...]
    support_claim_ids: tuple[str, ...]
    mapping_ids: tuple[str, ...] = ()
    source_family_ids: tuple[str, ...] = ()
    score_blocked_until_stage_court: bool = True
    production_score_fixture: bool = False
    reasons: tuple[str, ...] = ("score_contributions_ready_for_score_snapshot_builder",)


@dataclass(frozen=True)
class SourceBackedScoreSnapshotResult:
    task_id: str
    score_snapshot_task_id: str
    fixture_seed_id: str
    candidate_id: str
    archetype_id: str
    target_entity_id: str
    result_status: str
    verified_score: float = 0.0
    potential_score_upper_bound: float = 0.0
    unresolved_material_gap_points: float = 0.0
    unresolved_hard_break_candidate: bool = False
    provider_failed: bool = False
    invalid_evidence: bool = False
    contribution_ids: tuple[str, ...] = ()
    component_keys: tuple[str, ...] = ()
    support_claim_ids: tuple[str, ...] = ()
    mapping_ids: tuple[str, ...] = ()
    source_family_ids: tuple[str, ...] = ()
    score_interval_ready: bool = False
    score_blocked_until_stage_court: bool = True
    production_score_fixture: bool = False
    blocked_reason: str | None = None
    reasons: tuple[str, ...] = ()


@dataclass(frozen=True)
class SourceBackedStageCourtTask:
    task_id: str
    score_snapshot_result_id: str
    score_snapshot_task_id: str
    fixture_seed_id: str
    candidate_id: str
    archetype_id: str
    target_entity_id: str
    verified_score: float
    potential_score_upper_bound: float
    unresolved_hard_break_candidate: bool = False
    provider_failed: bool = False
    invalid_evidence: bool = False
    contribution_ids: tuple[str, ...] = ()
    primitive_ids: tuple[str, ...] = ()
    present_primitive_ids: tuple[str, ...] = ()
    support_claim_ids: tuple[str, ...] = ()
    component_keys: tuple[str, ...] = ()
    score_blocked_until_stage_court_result: bool = True
    production_score_fixture: bool = False
    production_stage_fixture: bool = False
    reasons: tuple[str, ...] = ("score_interval_ready_for_stage_court",)


@dataclass(frozen=True)
class SourceBackedStageCourtResult:
    task_id: str
    stage_court_task_id: str
    score_snapshot_result_id: str
    fixture_seed_id: str
    candidate_id: str
    archetype_id: str
    target_entity_id: str
    result_status: str
    verified_score: float = 0.0
    potential_score_upper_bound: float = 0.0
    score_status: str | None = None
    base_stage: str | None = None
    canonical_stage: str | None = None
    investigation_status: str | None = None
    transition_overlay: str | None = None
    present_green_primitives: tuple[str, ...] = ()
    missing_green_primitives: tuple[str, ...] = ()
    stage_court_ready: bool = False
    production_score_fixture: bool = False
    production_stage_fixture: bool = False
    blocked_reason: str | None = None
    reasons: tuple[str, ...] = ()


@dataclass(frozen=True)
class SourceBackedReplayChainAudit:
    audit_id: str
    chain_status: str
    evidence_os_chain_ready: bool
    production_cutover_ready: bool
    first_blocking_stage: str
    first_blocking_reason: str
    claim_replay_ready_count: int
    adjudication_mapping_ready_count: int
    primitive_mapping_eligibility_ready_count: int
    eligibility_score_contribution_ready_count: int
    score_contribution_ready_count: int
    score_interval_ready_count: int
    stage_court_ready_count: int
    production_score_fixture_total: int
    production_stage_fixture_total: int
    blocked_reason: str | None = None
    reasons: tuple[str, ...] = ()


@dataclass(frozen=True)
class SourceBackedClaimReplayReadinessAudit:
    audit_id: str
    readiness_status: str
    claim_replay_task_count: int
    fixture_not_ready_count: int
    replacement_fixture_row_count: int = 0
    replacement_fixture_ready_count: int = 0
    replacement_snapshot_not_verified_count: int = 0
    replacement_snapshot_verification_row_count: int = 0
    replacement_fetch_not_ready_count: int = 0
    replacement_snapshot_verified_count: int = 0
    replacement_candidate_fetch_task_count: int = 0
    replacement_candidate_fetch_failed_count: int = 0
    replacement_candidate_fetch_not_attempted_count: int = 0
    replacement_candidate_current_text_available_count: int = 0
    replacement_snapshot_request_count: int = 0
    replacement_fetch_snapshot_required_count: int = 0
    replacement_same_event_verification_required_count: int = 0
    replacement_score_blocked_request_count: int = 0
    first_upstream_blocking_stage: str | None = None
    first_upstream_blocking_reason: str | None = None
    production_score_fixture_total: int = 0
    reasons: tuple[str, ...] = ()


@dataclass(frozen=True)
class SourceBackedReplacementFetchRemediationTask:
    task_id: str
    replacement_candidate_id: str
    request_id: str
    fixture_seed_id: str
    candidate_id: str
    archetype_id: str
    original_source_anchor: str
    candidate_url: str
    as_of_date: str | None
    fetch_status: str
    remediation_status: str
    remediation_action: str
    priority: int
    max_total_fetches: int
    stop_condition: str
    reason: str | None = None
    score_blocked_until_resolved: bool = True
    source_replacement_verified: bool = False
    asof_snapshot_verified: bool = False
    evidence_document_fixture_ready: bool = False
    production_score_fixture: bool = False
    reasons: tuple[str, ...] = ()


@dataclass(frozen=True)
class SourceBackedReplacementFetchFailureAudit:
    audit_id: str
    remediation_status: str
    fetch_row_count: int
    remediation_task_count: int
    fetch_failed_count: int
    fetch_not_attempted_count: int
    current_text_available_count: int
    text_snapshot_required_count: int
    bounded_fetch_required_count: int
    snapshot_verification_required_count: int
    production_score_fixture_total: int = 0
    first_blocking_reason: str | None = None
    reasons: tuple[str, ...] = ()


@dataclass(frozen=True)
class SourceBackedReplacementPlannerRun:
    run_id: str
    request_id: str
    fixture_seed_id: str
    candidate_id: str
    archetype_id: str
    source_anchor: str
    as_of_date: str | None
    planner_status: str
    llm_called: bool
    candidate_source_count: int = 0
    provider_error: str | None = None
    production_score_fixture: bool = False
    reasons: tuple[str, ...] = ()


def classify_replay_source_status(
    row: Mapping[str, Any],
    *,
    contract_ids: Iterable[str] | None = None,
) -> ReplaySourceClassification:
    """Classify a research/calibration row for replay planning.

    Easy example:
    - `source_proxy_only=true` stays proxy/gap material even if the row has a
      tempting score label.
    - `evidence_url_pending=true` also stays gap material.
    - A non-proxy row with a concrete URL/API/fixture anchor is only a replay
      candidate. It still has to pass document -> claim -> primitive replay.
    """

    archetype_id = _row_archetype_id(row, contract_ids=contract_ids)
    source_path = _optional_text(row.get("_source_path"))
    source_line = _optional_int(row.get("_source_line"))
    reasons: list[str] = []

    source_proxy_only = _optional_bool(row.get("source_proxy_only"))
    evidence_url_pending = _optional_bool(row.get("evidence_url_pending"))
    if source_proxy_only is True:
        reasons.append("source_proxy_only_true")
    if evidence_url_pending is True:
        reasons.append("evidence_url_pending_true")
    if _has_proxy_marker(row):
        reasons.append("source_proxy_or_manual_verification_marker")
    if reasons:
        return ReplaySourceClassification(
            archetype_id=archetype_id,
            status=ReplaySourceStatus.SOURCE_PROXY_OR_PENDING,
            reasons=tuple(dict.fromkeys(reasons)),
            source_path=source_path,
            source_line=source_line,
        )

    has_concrete_anchor = _has_concrete_source_anchor(row)
    explicit_non_proxy = source_proxy_only is False and evidence_url_pending is False
    if has_concrete_anchor or explicit_non_proxy:
        candidate_reasons = []
        if has_concrete_anchor:
            candidate_reasons.append("concrete_source_anchor")
        if explicit_non_proxy:
            candidate_reasons.append("explicit_non_proxy_non_pending_flags")
        return ReplaySourceClassification(
            archetype_id=archetype_id,
            status=ReplaySourceStatus.SOURCE_BACKED_CANDIDATE,
            reasons=tuple(candidate_reasons),
            source_path=source_path,
            source_line=source_line,
        )

    return ReplaySourceClassification(
        archetype_id=archetype_id,
        status=ReplaySourceStatus.UNVERIFIED_RESEARCH_ROW,
        reasons=("no_concrete_source_anchor_or_non_proxy_flags",),
        source_path=source_path,
        source_line=source_line,
    )


def build_source_backed_replay_coverage(
    *,
    contract_ids: Sequence[str],
    rows: Iterable[Mapping[str, Any]],
    example_limit: int = 3,
) -> tuple[ReplayCoverageRow, ...]:
    contract_set = {normalise_canonical_archetype_id(item) for item in contract_ids}
    contract_set.discard(None)
    buckets: dict[str, list[ReplaySourceClassification]] = {str(item): [] for item in sorted(contract_set)}

    for row in rows:
        classification = classify_replay_source_status(row, contract_ids=contract_set)
        if classification.archetype_id in buckets:
            buckets[classification.archetype_id].append(classification)

    coverage_rows: list[ReplayCoverageRow] = []
    for archetype_id in sorted(buckets):
        classifications = buckets[archetype_id]
        source_backed = [item for item in classifications if item.status == ReplaySourceStatus.SOURCE_BACKED_CANDIDATE]
        proxy_or_pending = [item for item in classifications if item.status == ReplaySourceStatus.SOURCE_PROXY_OR_PENDING]
        unverified = [item for item in classifications if item.status == ReplaySourceStatus.UNVERIFIED_RESEARCH_ROW]
        if source_backed:
            coverage_status = COVERAGE_AVAILABLE
        elif classifications:
            coverage_status = COVERAGE_GAP_WITH_ROWS
        else:
            coverage_status = COVERAGE_GAP_NO_ROWS
        coverage_rows.append(
            ReplayCoverageRow(
                archetype_id=archetype_id,
                total_rows=len(classifications),
                source_backed_candidate_count=len(source_backed),
                source_proxy_or_pending_count=len(proxy_or_pending),
                unverified_research_row_count=len(unverified),
                coverage_status=coverage_status,
                example_source_backed_rows=_examples(source_backed, limit=example_limit),
                example_source_proxy_or_pending_rows=_examples(proxy_or_pending, limit=example_limit),
                example_unverified_rows=_examples(unverified, limit=example_limit),
            )
        )
    return tuple(coverage_rows)


def build_source_backed_replay_manifest(
    *,
    contract_ids: Sequence[str],
    rows: Iterable[Mapping[str, Any]],
    per_archetype_limit: int = 3,
) -> Mapping[str, Any]:
    if per_archetype_limit <= 0:
        raise ValueError("per_archetype_limit must be positive")

    contract_set = {normalise_canonical_archetype_id(item) for item in contract_ids}
    contract_set.discard(None)
    buckets: dict[str, list[tuple[tuple[Any, ...], SourceBackedReplayCandidate]]] = {
        str(item): [] for item in sorted(contract_set)
    }
    source_backed_without_concrete_anchor = {str(item): 0 for item in sorted(contract_set)}

    for row in rows:
        classification = classify_replay_source_status(row, contract_ids=contract_set)
        if classification.archetype_id not in buckets:
            continue
        if classification.status != ReplaySourceStatus.SOURCE_BACKED_CANDIDATE:
            continue
        anchors = _source_anchors(row)
        if not anchors:
            source_backed_without_concrete_anchor[classification.archetype_id] += 1
            continue
        candidate = _replay_candidate_from_row(
            row,
            archetype_id=classification.archetype_id,
            anchors=anchors,
            classification_reasons=classification.reasons,
        )
        buckets[classification.archetype_id].append((_candidate_sort_key(row, candidate), candidate))

    archetype_rows: list[dict[str, Any]] = []
    selected_candidates: list[SourceBackedReplayCandidate] = []
    for archetype_id in sorted(buckets):
        candidates = [candidate for _, candidate in sorted(buckets[archetype_id], key=lambda item: item[0])]
        unique_candidates = _dedupe_replay_candidates(candidates)
        selected = unique_candidates[:per_archetype_limit]
        selected_candidates.extend(selected)
        archetype_rows.append(
            {
                "archetype_id": archetype_id,
                "fixture_ready_candidate_count": len(candidates),
                "unique_fixture_ready_candidate_count": len(unique_candidates),
                "selected_candidate_count": len(selected),
                "source_backed_without_concrete_anchor_count": source_backed_without_concrete_anchor[archetype_id],
                "selected_candidate_ids": [candidate.candidate_id for candidate in selected],
            }
        )

    return {
        "schema_version": "e2r_source_backed_replay_manifest_v1",
        "contract_count": len(contract_set),
        "per_archetype_limit": per_archetype_limit,
        "summary": {
            "archetype_count": len(archetype_rows),
            "archetype_with_selected_candidate_count": sum(
                1 for row in archetype_rows if row["selected_candidate_count"] > 0
            ),
            "fixture_ready_candidate_count": sum(row["fixture_ready_candidate_count"] for row in archetype_rows),
            "unique_fixture_ready_candidate_count": sum(
                row["unique_fixture_ready_candidate_count"] for row in archetype_rows
            ),
            "selected_candidate_count": len(selected_candidates),
            "source_backed_without_concrete_anchor_count": sum(
                row["source_backed_without_concrete_anchor_count"] for row in archetype_rows
            ),
            "production_score_fixture_count": sum(1 for candidate in selected_candidates if candidate.production_score_fixture),
        },
        "archetype_rows": archetype_rows,
        "candidates": [asdict(candidate) for candidate in selected_candidates],
    }


def build_source_backed_fixture_seed_manifest(
    *,
    replay_manifest: Mapping[str, Any],
) -> Mapping[str, Any]:
    seeds: list[SourceBackedReplayFixtureSeed] = []
    for candidate in replay_manifest.get("candidates") or ():
        if not isinstance(candidate, Mapping):
            continue
        seeds.extend(_fixture_seeds_from_candidate(candidate))

    return {
        "schema_version": "e2r_source_backed_fixture_seed_manifest_v1",
        "source_manifest_schema_version": replay_manifest.get("schema_version"),
        "summary": {
            "candidate_count": len(replay_manifest.get("candidates") or ()),
            "fixture_seed_count": len(seeds),
            "snapshot_request_ready_count": sum(1 for seed in seeds if seed.snapshot_request_ready),
            "pending_source_snapshot_count": sum(
                1 for seed in seeds if seed.snapshot_status == "pending_source_snapshot"
            ),
            "missing_as_of_date_count": sum(1 for seed in seeds if seed.snapshot_status == "missing_as_of_date"),
            "evidence_document_fixture_ready_count": sum(1 for seed in seeds if seed.evidence_document_fixture_ready),
            "production_score_fixture_count": sum(1 for seed in seeds if seed.production_score_fixture),
        },
        "seeds": [asdict(seed) for seed in seeds],
    }


def build_source_snapshot_availability_manifest(
    *,
    fixture_seed_manifest: Mapping[str, Any],
    snapshot_rows: Iterable[Mapping[str, Any]],
) -> Mapping[str, Any]:
    snapshots_by_url = _snapshot_rows_by_url(snapshot_rows)
    rows: list[SourceBackedSnapshotAvailability] = []
    for seed in fixture_seed_manifest.get("seeds") or ():
        if not isinstance(seed, Mapping):
            continue
        rows.append(_snapshot_availability_for_seed(seed, snapshots_by_url=snapshots_by_url))

    return {
        "schema_version": "e2r_source_snapshot_availability_manifest_v1",
        "source_fixture_seed_schema_version": fixture_seed_manifest.get("schema_version"),
        "summary": {
            "fixture_seed_count": len(rows),
            "local_text_snapshot_ready_count": sum(
                1 for row in rows if row.snapshot_status == "local_text_snapshot_ready"
            ),
            "no_local_snapshot_count": sum(1 for row in rows if row.snapshot_status == "no_local_snapshot"),
            "future_snapshot_not_allowed_count": sum(
                1 for row in rows if row.snapshot_status == "future_snapshot_not_allowed"
            ),
            "local_snapshot_text_missing_count": sum(
                1 for row in rows if row.snapshot_status == "local_snapshot_text_missing"
            ),
            "not_snapshot_request_ready_count": sum(
                1 for row in rows if row.snapshot_status == "not_snapshot_request_ready"
            ),
            "evidence_document_fixture_ready_count": sum(1 for row in rows if row.evidence_document_fixture_ready),
            "production_score_fixture_count": sum(1 for row in rows if row.production_score_fixture),
        },
        "rows": [asdict(row) for row in rows],
    }


def build_current_fetch_status_manifest(
    *,
    fixture_seed_manifest: Mapping[str, Any],
    fetch_rows: Iterable[Mapping[str, Any]],
) -> Mapping[str, Any]:
    fetch_by_seed = {
        str(row.get("fixture_seed_id")): row
        for row in fetch_rows
        if isinstance(row, Mapping) and row.get("fixture_seed_id")
    }
    rows: list[SourceBackedCurrentFetchStatus] = []
    for seed in fixture_seed_manifest.get("seeds") or ():
        if not isinstance(seed, Mapping):
            continue
        rows.append(_current_fetch_status_for_seed(seed, fetch_by_seed=fetch_by_seed))

    return {
        "schema_version": "e2r_current_fetch_status_manifest_v1",
        "source_fixture_seed_schema_version": fixture_seed_manifest.get("schema_version"),
        "summary": {
            "fixture_seed_count": len(rows),
            "current_fetch_text_available_count": sum(
                1 for row in rows if row.current_fetch_status == "current_fetch_text_available_asof_unverified"
            ),
            "current_fetch_failed_count": sum(1 for row in rows if row.current_fetch_status == "current_fetch_failed"),
            "current_fetch_not_attempted_count": sum(
                1 for row in rows if row.current_fetch_status == "current_fetch_not_attempted"
            ),
            "not_snapshot_request_ready_count": sum(
                1 for row in rows if row.current_fetch_status == "not_snapshot_request_ready"
            ),
            "asof_snapshot_verified_count": sum(1 for row in rows if row.asof_snapshot_verified),
            "evidence_document_fixture_ready_count": sum(1 for row in rows if row.evidence_document_fixture_ready),
            "production_score_fixture_count": sum(1 for row in rows if row.production_score_fixture),
        },
        "rows": [asdict(row) for row in rows],
    }


def build_snapshot_remediation_plan(
    *,
    current_fetch_status_manifest: Mapping[str, Any],
) -> Mapping[str, Any]:
    tasks: list[SourceBackedSnapshotRemediationTask] = []
    for row in current_fetch_status_manifest.get("rows") or ():
        if not isinstance(row, Mapping):
            continue
        tasks.append(_remediation_task_for_current_fetch_row(row))
    by_type: dict[str, int] = {}
    for task in tasks:
        by_type[task.remediation_type] = by_type.get(task.remediation_type, 0) + 1
    return {
        "schema_version": "e2r_source_snapshot_remediation_plan_v1",
        "source_current_fetch_schema_version": current_fetch_status_manifest.get("schema_version"),
        "summary": {
            "task_count": len(tasks),
            "score_blocked_task_count": sum(1 for task in tasks if task.score_blocked_until_resolved),
            "asof_verify_current_text_count": by_type.get("verify_current_text_asof_identity", 0),
            "archive_or_alternative_source_count": by_type.get("archive_or_alternative_source", 0),
            "pdf_parser_repair_count": by_type.get("pdf_parser_repair", 0),
            "retry_current_fetch_count": by_type.get("retry_current_fetch_with_browser_or_tls_repair", 0),
            "dead_url_replacement_count": by_type.get("dead_url_replacement", 0),
            "fetch_not_attempted_count": by_type.get("fetch_current_text", 0),
            "seed_metadata_repair_count": by_type.get("seed_metadata_repair", 0),
        },
        "remediation_type_counts": dict(sorted(by_type.items())),
        "tasks": [asdict(task) for task in sorted(tasks, key=lambda item: (item.priority, item.archetype_id, item.task_id))],
    }


def build_current_text_asof_precheck_manifest(
    *,
    current_fetch_status_manifest: Mapping[str, Any],
    max_text_chars: int = 20_000,
) -> Mapping[str, Any]:
    rows: list[SourceBackedCurrentTextAsofPrecheck] = []
    for row in current_fetch_status_manifest.get("rows") or ():
        if not isinstance(row, Mapping):
            continue
        rows.append(_current_text_asof_precheck_for_row(row, max_text_chars=max_text_chars))
    return {
        "schema_version": "e2r_current_text_asof_precheck_manifest_v1",
        "source_current_fetch_schema_version": current_fetch_status_manifest.get("schema_version"),
        "summary": {
            "row_count": len(rows),
            "asof_precheck_candidate_count": sum(1 for row in rows if row.asof_precheck_candidate),
            "date_hint_on_or_before_asof_count": sum(
                1 for row in rows if row.precheck_status == "date_hint_on_or_before_asof"
            ),
            "future_date_hint_blocks_count": sum(
                1 for row in rows if row.precheck_status == "future_date_hint_blocks"
            ),
            "no_date_hint_count": sum(1 for row in rows if row.precheck_status == "no_date_hint"),
            "current_text_unavailable_count": sum(
                1 for row in rows if row.precheck_status == "current_text_unavailable"
            ),
            "current_text_file_missing_count": sum(
                1 for row in rows if row.precheck_status == "current_text_file_missing"
            ),
            "asof_snapshot_verified_count": sum(1 for row in rows if row.asof_snapshot_verified),
            "evidence_document_fixture_ready_count": sum(1 for row in rows if row.evidence_document_fixture_ready),
            "production_score_fixture_count": sum(1 for row in rows if row.production_score_fixture),
        },
        "rows": [asdict(row) for row in rows],
    }


def build_evidence_document_fixture_manifest(
    *,
    snapshot_availability_manifest: Mapping[str, Any],
    anchor_max_chars: int = 800,
) -> Mapping[str, Any]:
    rows: list[SourceBackedEvidenceDocumentFixture] = []
    for row in snapshot_availability_manifest.get("rows") or ():
        if not isinstance(row, Mapping):
            continue
        rows.append(_evidence_document_fixture_for_snapshot_row(row, anchor_max_chars=anchor_max_chars))

    return {
        "schema_version": "e2r_evidence_document_fixture_manifest_v1",
        "source_snapshot_availability_schema_version": snapshot_availability_manifest.get("schema_version"),
        "summary": {
            "row_count": len(rows),
            "evidence_document_fixture_ready_count": sum(
                1 for row in rows if row.evidence_document_fixture_ready
            ),
            "anchor_verified_count": sum(1 for row in rows if row.anchor_verified),
            "source_snapshot_not_ready_count": sum(
                1 for row in rows if row.fixture_status == "source_snapshot_not_ready"
            ),
            "snapshot_text_missing_count": sum(1 for row in rows if row.fixture_status == "snapshot_text_missing"),
            "invalid_snapshot_date_count": sum(1 for row in rows if row.fixture_status == "invalid_snapshot_date"),
            "empty_snapshot_text_count": sum(1 for row in rows if row.fixture_status == "empty_snapshot_text"),
            "content_hash_mismatch_count": sum(1 for row in rows if row.fixture_status == "content_hash_mismatch"),
            "anchor_verification_failed_count": sum(
                1 for row in rows if row.fixture_status == "anchor_verification_failed"
            ),
            "claim_replay_ready_count": sum(1 for row in rows if row.claim_replay_ready),
            "production_score_fixture_count": sum(1 for row in rows if row.production_score_fixture),
        },
        "rows": [asdict(row) for row in rows],
    }


def build_asof_snapshot_acquisition_queue(
    *,
    current_text_asof_precheck_manifest: Mapping[str, Any],
    snapshot_remediation_plan: Mapping[str, Any],
    evidence_document_fixture_manifest: Mapping[str, Any] | None = None,
) -> Mapping[str, Any]:
    precheck_by_seed = {
        str(row.get("fixture_seed_id")): row
        for row in current_text_asof_precheck_manifest.get("rows") or ()
        if isinstance(row, Mapping) and row.get("fixture_seed_id")
    }
    ready_seed_ids = {
        str(row.get("fixture_seed_id"))
        for row in (evidence_document_fixture_manifest or {}).get("rows", ())
        if isinstance(row, Mapping) and _optional_bool(row.get("evidence_document_fixture_ready"))
    }
    tasks: list[SourceBackedAsofSnapshotAcquisitionTask] = []
    for row in snapshot_remediation_plan.get("tasks") or ():
        if not isinstance(row, Mapping):
            continue
        fixture_seed_id = _optional_text(row.get("fixture_seed_id")) or ""
        if fixture_seed_id in ready_seed_ids:
            continue
        tasks.append(
            _asof_snapshot_acquisition_task_for_row(
                row,
                precheck_row=precheck_by_seed.get(fixture_seed_id),
            )
        )
    by_type: dict[str, int] = {}
    for task in tasks:
        by_type[task.task_type] = by_type.get(task.task_type, 0) + 1
    return {
        "schema_version": "e2r_asof_snapshot_acquisition_queue_v1",
        "source_precheck_schema_version": current_text_asof_precheck_manifest.get("schema_version"),
        "source_remediation_schema_version": snapshot_remediation_plan.get("schema_version"),
        "source_evidence_document_fixture_schema_version": (evidence_document_fixture_manifest or {}).get(
            "schema_version"
        ),
        "summary": {
            "task_count": len(tasks),
            "score_blocked_task_count": sum(1 for task in tasks if task.score_blocked_until_verified),
            "llm_followup_required_count": sum(1 for task in tasks if task.llm_followup_required),
            "archive_identity_verify_candidate_count": by_type.get("archive_identity_verify_candidate", 0),
            "archive_or_metadata_disambiguation_count": by_type.get("archive_or_metadata_disambiguation", 0),
            "metadata_archive_date_lookup_count": by_type.get("metadata_archive_date_lookup", 0),
            "pdf_binary_snapshot_repair_count": by_type.get("pdf_binary_snapshot_repair", 0),
            "dead_url_archive_or_replacement_count": by_type.get("dead_url_archive_or_replacement", 0),
            "archive_or_alternative_source_count": by_type.get("archive_or_alternative_source", 0),
            "bounded_retry_then_archive_count": by_type.get("bounded_retry_then_archive", 0),
            "generic_source_snapshot_repair_count": by_type.get("generic_source_snapshot_repair", 0),
            "production_score_fixture_count": sum(1 for task in tasks if task.production_score_fixture),
        },
        "task_type_counts": dict(sorted(by_type.items())),
        "tasks": [asdict(task) for task in sorted(tasks, key=lambda item: (item.priority, item.archetype_id, item.task_id))],
    }


def build_asof_snapshot_verification_manifest(
    *,
    acquisition_queue: Mapping[str, Any],
    attempt_rows: Iterable[Mapping[str, Any]],
) -> Mapping[str, Any]:
    attempts_by_task_id: dict[str, Mapping[str, Any]] = {}
    attempts_by_seed_id: dict[str, Mapping[str, Any]] = {}
    for row in attempt_rows:
        if not isinstance(row, Mapping):
            continue
        task_id = _optional_text(row.get("task_id"))
        fixture_seed_id = _optional_text(row.get("fixture_seed_id"))
        if task_id:
            attempts_by_task_id[task_id] = row
        if fixture_seed_id:
            attempts_by_seed_id[fixture_seed_id] = row

    rows: list[SourceBackedAsofSnapshotVerificationResult] = []
    for task in acquisition_queue.get("tasks") or ():
        if not isinstance(task, Mapping):
            continue
        attempt = attempts_by_task_id.get(_optional_text(task.get("task_id")) or "")
        if attempt is None:
            attempt = attempts_by_seed_id.get(_optional_text(task.get("fixture_seed_id")) or "")
        rows.append(_verify_asof_snapshot_attempt(task, attempt))

    by_status: dict[str, int] = {}
    for row in rows:
        by_status[row.verification_status] = by_status.get(row.verification_status, 0) + 1
    return {
        "schema_version": "e2r_asof_snapshot_verification_manifest_v1",
        "source_acquisition_queue_schema_version": acquisition_queue.get("schema_version"),
        "summary": {
            "row_count": len(rows),
            "asof_text_snapshot_verified_count": by_status.get("asof_text_snapshot_verified", 0),
            "no_attempt_result_count": by_status.get("no_attempt_result", 0),
            "attempt_failed_count": by_status.get("attempt_failed", 0),
            "source_anchor_mismatch_count": by_status.get("source_anchor_mismatch", 0),
            "invalid_snapshot_date_count": by_status.get("invalid_snapshot_date", 0),
            "future_snapshot_not_allowed_count": by_status.get("future_snapshot_not_allowed", 0),
            "snapshot_text_missing_count": by_status.get("snapshot_text_missing", 0),
            "empty_snapshot_text_count": by_status.get("empty_snapshot_text", 0),
            "content_hash_mismatch_count": by_status.get("content_hash_mismatch", 0),
            "evidence_document_fixture_ready_count": sum(
                1 for row in rows if row.evidence_document_fixture_ready
            ),
            "production_score_fixture_count": sum(1 for row in rows if row.production_score_fixture),
        },
        "verification_status_counts": dict(sorted(by_status.items())),
        "rows": [asdict(row) for row in rows],
    }


def build_asof_snapshot_verifier_task_manifest(
    *,
    acquisition_queue: Mapping[str, Any],
    current_fetch_status_manifest: Mapping[str, Any],
    current_text_asof_precheck_manifest: Mapping[str, Any],
) -> Mapping[str, Any]:
    fetch_by_seed = {
        str(row.get("fixture_seed_id")): row
        for row in current_fetch_status_manifest.get("rows") or ()
        if isinstance(row, Mapping) and row.get("fixture_seed_id")
    }
    precheck_by_seed = {
        str(row.get("fixture_seed_id")): row
        for row in current_text_asof_precheck_manifest.get("rows") or ()
        if isinstance(row, Mapping) and row.get("fixture_seed_id")
    }
    tasks = [
        _asof_snapshot_verifier_task_for_acquisition_task(
            task,
            fetch_row=fetch_by_seed.get(_optional_text(task.get("fixture_seed_id")) or ""),
            precheck_row=precheck_by_seed.get(_optional_text(task.get("fixture_seed_id")) or ""),
        )
        for task in acquisition_queue.get("tasks") or ()
        if isinstance(task, Mapping)
    ]
    by_status: dict[str, int] = {}
    for task in tasks:
        by_status[task.verifier_task_status] = by_status.get(task.verifier_task_status, 0) + 1
    return {
        "schema_version": "e2r_asof_snapshot_verifier_task_manifest_v1",
        "source_acquisition_queue_schema_version": acquisition_queue.get("schema_version"),
        "source_current_fetch_status_schema_version": current_fetch_status_manifest.get("schema_version"),
        "source_current_text_asof_precheck_schema_version": current_text_asof_precheck_manifest.get(
            "schema_version"
        ),
        "summary": {
            "task_count": len(tasks),
            "ready_for_source_identity_asof_verifier_count": by_status.get(
                "ready_for_source_identity_asof_verifier",
                0,
            ),
            "ready_for_source_metadata_asof_verifier_count": by_status.get(
                "ready_for_source_metadata_asof_verifier",
                0,
            ),
            "blocked_non_identity_verify_task_count": by_status.get(
                "blocked_non_identity_verify_task",
                0,
            ),
            "blocked_until_current_text_snapshot_count": by_status.get(
                "blocked_until_current_text_snapshot",
                0,
            ),
            "blocked_until_asof_precheck_candidate_count": by_status.get(
                "blocked_until_asof_precheck_candidate",
                0,
            ),
            "score_blocked_task_count": sum(1 for task in tasks if task.score_blocked_until_verified),
            "source_replacement_verified_count": sum(1 for task in tasks if task.source_replacement_verified),
            "asof_snapshot_verified_count": sum(1 for task in tasks if task.asof_snapshot_verified),
            "evidence_document_fixture_ready_count": sum(
                1 for task in tasks if task.evidence_document_fixture_ready
            ),
            "production_score_fixture_count": sum(1 for task in tasks if task.production_score_fixture),
        },
        "verifier_task_status_counts": dict(sorted(by_status.items())),
        "tasks": [
            asdict(task)
            for task in sorted(
                tasks,
                key=lambda item: (item.verifier_task_status, item.archetype_id, item.verifier_task_id),
            )
        ],
    }


def build_asof_snapshot_verifier_result_manifest(
    *,
    verifier_task_manifest: Mapping[str, Any],
    verifier_rows: Iterable[Mapping[str, Any]],
) -> Mapping[str, Any]:
    rows_by_verifier_task_id: dict[str, Mapping[str, Any]] = {}
    rows_by_acquisition_task_id: dict[str, Mapping[str, Any]] = {}
    rows_by_seed_id: dict[str, Mapping[str, Any]] = {}
    for row in verifier_rows:
        if not isinstance(row, Mapping):
            continue
        verifier_task_id = _optional_text(row.get("verifier_task_id") or row.get("task_id"))
        acquisition_task_id = _optional_text(row.get("acquisition_task_id"))
        fixture_seed_id = _optional_text(row.get("fixture_seed_id"))
        if verifier_task_id:
            rows_by_verifier_task_id[verifier_task_id] = row
        if acquisition_task_id:
            rows_by_acquisition_task_id[acquisition_task_id] = row
        if fixture_seed_id:
            rows_by_seed_id[fixture_seed_id] = row

    results: list[SourceBackedAsofSnapshotVerifierResult] = []
    for task in verifier_task_manifest.get("tasks") or ():
        if not isinstance(task, Mapping):
            continue
        row = rows_by_verifier_task_id.get(_optional_text(task.get("verifier_task_id")) or "")
        if row is None:
            row = rows_by_acquisition_task_id.get(_optional_text(task.get("acquisition_task_id")) or "")
        if row is None:
            row = rows_by_seed_id.get(_optional_text(task.get("fixture_seed_id")) or "")
        results.append(_asof_snapshot_verifier_result_for_task(task, row))

    by_status: dict[str, int] = {}
    for result in results:
        by_status[result.result_status] = by_status.get(result.result_status, 0) + 1
    accepted_rows = [
        dict(result.accepted_attempt_row)
        for result in results
        if result.accepted_attempt_row is not None
    ]
    return {
        "schema_version": "e2r_asof_snapshot_verifier_result_manifest_v1",
        "source_verifier_task_schema_version": verifier_task_manifest.get("schema_version"),
        "summary": {
            "result_count": len(results),
            "source_identity_asof_verified_count": by_status.get("source_identity_asof_verified", 0),
            "blocked_task_not_ready_count": by_status.get("blocked_task_not_ready", 0),
            "no_verifier_result_count": by_status.get("no_verifier_result", 0),
            "forbidden_output_field_count": by_status.get("forbidden_output_field", 0),
            "source_identity_unverified_count": by_status.get("source_identity_unverified", 0),
            "attempt_failed_count": by_status.get("attempt_failed", 0),
            "snapshot_url_mismatch_count": by_status.get("snapshot_url_mismatch", 0),
            "invalid_snapshot_date_count": by_status.get("invalid_snapshot_date", 0),
            "future_snapshot_not_allowed_count": by_status.get("future_snapshot_not_allowed", 0),
            "snapshot_text_missing_count": by_status.get("snapshot_text_missing", 0),
            "empty_snapshot_text_count": by_status.get("empty_snapshot_text", 0),
            "content_hash_mismatch_count": by_status.get("content_hash_mismatch", 0),
            "accepted_attempt_row_count": len(accepted_rows),
            "source_replacement_verified_count": sum(1 for result in results if result.source_replacement_verified),
            "asof_snapshot_verified_count": sum(1 for result in results if result.asof_snapshot_verified),
            "evidence_document_fixture_ready_count": sum(
                1 for result in results if result.evidence_document_fixture_ready
            ),
            "production_score_fixture_count": sum(1 for result in results if result.production_score_fixture),
        },
        "result_status_counts": dict(sorted(by_status.items())),
        "accepted_attempt_rows": accepted_rows,
        "results": [
            asdict(result)
            for result in sorted(results, key=lambda item: (item.result_status, item.archetype_id, item.result_id))
        ],
    }


def build_same_event_source_replacement_request_manifest(
    *,
    acquisition_queue: Mapping[str, Any],
    verification_manifest: Mapping[str, Any] | None = None,
) -> Mapping[str, Any]:
    verified_seed_ids = {
        str(row.get("fixture_seed_id"))
        for row in (verification_manifest or {}).get("rows", ())
        if isinstance(row, Mapping) and row.get("verification_status") == "asof_text_snapshot_verified"
    }
    requests: list[SourceBackedReplacementSourceRequest] = []
    for task in acquisition_queue.get("tasks") or ():
        if not isinstance(task, Mapping):
            continue
        fixture_seed_id = _optional_text(task.get("fixture_seed_id")) or ""
        if fixture_seed_id in verified_seed_ids:
            continue
        if _optional_bool(task.get("llm_followup_required")) is not True:
            continue
        requests.append(_replacement_source_request_for_task(task))

    return {
        "schema_version": "e2r_same_event_source_replacement_request_manifest_v1",
        "source_acquisition_queue_schema_version": acquisition_queue.get("schema_version"),
        "source_verification_schema_version": (verification_manifest or {}).get("schema_version"),
        "summary": {
            "request_count": len(requests),
            "llm_followup_required_count": sum(1 for request in requests if request.llm_followup_required),
            "deterministic_query_count": sum(len(request.suggested_queries) for request in requests),
            "ready_for_llm_planning_count": sum(
                1 for request in requests if request.request_status == "ready_for_llm_same_event_source_planning"
            ),
            "production_score_fixture_count": sum(1 for request in requests if request.production_score_fixture),
        },
        "requests": [asdict(request) for request in sorted(requests, key=lambda item: (item.archetype_id, item.request_id))],
    }


def build_same_event_replacement_planner_run_manifest(
    *,
    request_manifest: Mapping[str, Any],
    provider: Any | None = None,
) -> Mapping[str, Any]:
    runs: list[SourceBackedReplacementPlannerRun] = []
    planner_rows: list[Mapping[str, Any]] = []
    for request in request_manifest.get("requests") or ():
        if not isinstance(request, Mapping):
            continue
        run, rows = _same_event_planner_run_for_request(request, provider=provider)
        runs.append(run)
        planner_rows.extend(rows)
    by_status: dict[str, int] = {}
    for run in runs:
        by_status[run.planner_status] = by_status.get(run.planner_status, 0) + 1
    return {
        "schema_version": "e2r_same_event_replacement_planner_run_manifest_v1",
        "source_replacement_request_schema_version": request_manifest.get("schema_version"),
        "summary": {
            "request_count": len(runs),
            "llm_called_count": sum(1 for run in runs if run.llm_called),
            "planner_output_count": len(planner_rows),
            "provider_not_configured_count": by_status.get("provider_not_configured", 0),
            "provider_error_count": by_status.get("provider_error", 0),
            "planner_success_count": by_status.get("planner_success", 0),
            "planner_empty_output_count": by_status.get("planner_empty_output", 0),
            "production_score_fixture_count": sum(1 for run in runs if run.production_score_fixture),
        },
        "planner_status_counts": dict(sorted(by_status.items())),
        "runs": [asdict(run) for run in runs],
        "planner_rows": planner_rows,
    }


def build_same_event_source_replacement_candidate_manifest(
    *,
    request_manifest: Mapping[str, Any],
    planner_rows: Iterable[Mapping[str, Any]],
) -> Mapping[str, Any]:
    planner_by_request_id: dict[str, list[Mapping[str, Any]]] = {}
    planner_by_seed_id: dict[str, list[Mapping[str, Any]]] = {}
    for row in planner_rows:
        if not isinstance(row, Mapping):
            continue
        request_id = _optional_text(row.get("request_id"))
        fixture_seed_id = _optional_text(row.get("fixture_seed_id"))
        if request_id:
            planner_by_request_id.setdefault(request_id, []).append(row)
        if fixture_seed_id:
            planner_by_seed_id.setdefault(fixture_seed_id, []).append(row)

    candidates: list[SourceBackedReplacementSourceCandidate] = []
    for request in request_manifest.get("requests") or ():
        if not isinstance(request, Mapping):
            continue
        rows = planner_by_request_id.get(_optional_text(request.get("request_id")) or "")
        if rows is None:
            rows = planner_by_seed_id.get(_optional_text(request.get("fixture_seed_id")) or "", [])
        if not rows:
            candidates.append(_replacement_candidate_missing_output(request))
            continue
        for row in rows:
            expanded = _replacement_candidate_rows_from_planner_row(row)
            if not expanded:
                candidates.append(_replacement_candidate_from_planner_source(request, {}))
                continue
            for source in expanded:
                candidates.append(_replacement_candidate_from_planner_source(request, source))

    by_status: dict[str, int] = {}
    for candidate in candidates:
        by_status[candidate.candidate_status] = by_status.get(candidate.candidate_status, 0) + 1
    return {
        "schema_version": "e2r_same_event_source_replacement_candidate_manifest_v1",
        "source_replacement_request_schema_version": request_manifest.get("schema_version"),
        "summary": {
            "candidate_row_count": len(candidates),
            "replacement_candidate_unverified_count": by_status.get("replacement_candidate_unverified", 0),
            "no_llm_candidate_output_count": by_status.get("no_llm_candidate_output", 0),
            "invalid_candidate_missing_url_count": by_status.get("invalid_candidate_missing_url", 0),
            "invalid_candidate_same_as_blocked_source_count": by_status.get(
                "invalid_candidate_same_as_blocked_source",
                0,
            ),
            "candidate_after_asof_blocked_count": by_status.get("candidate_after_asof_blocked", 0),
            "source_replacement_verified_count": sum(1 for candidate in candidates if candidate.source_replacement_verified),
            "asof_snapshot_verified_count": sum(1 for candidate in candidates if candidate.asof_snapshot_verified),
            "evidence_document_fixture_ready_count": sum(
                1 for candidate in candidates if candidate.evidence_document_fixture_ready
            ),
            "production_score_fixture_count": sum(1 for candidate in candidates if candidate.production_score_fixture),
        },
        "candidate_status_counts": dict(sorted(by_status.items())),
        "candidates": [
            asdict(candidate)
            for candidate in sorted(candidates, key=lambda item: (item.archetype_id, item.fixture_seed_id, item.replacement_candidate_id))
        ],
    }


def build_replacement_candidate_acquisition_queue(
    *,
    replacement_candidate_manifest: Mapping[str, Any],
) -> Mapping[str, Any]:
    tasks: list[SourceBackedReplacementCandidateAcquisitionTask] = []
    skipped: list[Mapping[str, Any]] = []
    seen_fetch_keys: dict[tuple[str, str | None], str] = {}
    for candidate in replacement_candidate_manifest.get("candidates") or ():
        if not isinstance(candidate, Mapping):
            continue
        if candidate.get("candidate_status") != "replacement_candidate_unverified":
            skipped.append(
                {
                    "replacement_candidate_id": _optional_text(candidate.get("replacement_candidate_id")),
                    "fixture_seed_id": _optional_text(candidate.get("fixture_seed_id")),
                    "candidate_status": _optional_text(candidate.get("candidate_status")),
                    "skip_reason": "candidate_not_unverified_fetch_candidate",
                }
            )
            continue
        candidate_url = _optional_text(candidate.get("candidate_url"))
        if not candidate_url:
            skipped.append(
                {
                    "replacement_candidate_id": _optional_text(candidate.get("replacement_candidate_id")),
                    "fixture_seed_id": _optional_text(candidate.get("fixture_seed_id")),
                    "candidate_status": _optional_text(candidate.get("candidate_status")),
                    "skip_reason": "candidate_url_missing",
                }
            )
            continue
        fetch_key = (_replacement_candidate_fetch_key(candidate_url, _optional_text(candidate.get("as_of_date"))))
        existing_task_id = seen_fetch_keys.get(fetch_key)
        if existing_task_id is not None:
            skipped.append(
                {
                    "replacement_candidate_id": _optional_text(candidate.get("replacement_candidate_id")),
                    "fixture_seed_id": _optional_text(candidate.get("fixture_seed_id")),
                    "candidate_status": _optional_text(candidate.get("candidate_status")),
                    "candidate_url": candidate_url,
                    "duplicate_of_task_id": existing_task_id,
                    "skip_reason": "duplicate_replacement_candidate_fetch_task",
                }
            )
            continue
        task = _replacement_candidate_acquisition_task(candidate, candidate_url=candidate_url)
        seen_fetch_keys[fetch_key] = task.task_id
        tasks.append(task)

    return {
        "schema_version": "e2r_replacement_candidate_acquisition_queue_v1",
        "source_replacement_candidate_schema_version": replacement_candidate_manifest.get("schema_version"),
        "summary": {
            "task_count": len(tasks),
            "skipped_candidate_count": len(skipped),
            "duplicate_fetch_task_skipped_count": sum(
                1 for row in skipped if row.get("skip_reason") == "duplicate_replacement_candidate_fetch_task"
            ),
            "score_blocked_task_count": sum(1 for task in tasks if task.score_blocked_until_verified),
            "source_replacement_verified_count": sum(1 for task in tasks if task.source_replacement_verified),
            "asof_snapshot_verified_count": sum(1 for task in tasks if task.asof_snapshot_verified),
            "evidence_document_fixture_ready_count": sum(1 for task in tasks if task.evidence_document_fixture_ready),
            "production_score_fixture_count": sum(1 for task in tasks if task.production_score_fixture),
        },
        "tasks": [asdict(task) for task in sorted(tasks, key=lambda item: (item.archetype_id, item.task_id))],
        "skipped_candidates": skipped,
    }


def build_replacement_candidate_fetch_status_manifest(
    *,
    acquisition_queue: Mapping[str, Any],
    fetch_rows: Iterable[Mapping[str, Any]],
) -> Mapping[str, Any]:
    fetch_by_task_id: dict[str, Mapping[str, Any]] = {}
    fetch_by_candidate_id: dict[str, Mapping[str, Any]] = {}
    for row in fetch_rows:
        if not isinstance(row, Mapping):
            continue
        task_id = _optional_text(row.get("task_id"))
        replacement_candidate_id = _optional_text(row.get("replacement_candidate_id"))
        if task_id:
            fetch_by_task_id[task_id] = row
        if replacement_candidate_id:
            fetch_by_candidate_id[replacement_candidate_id] = row

    rows: list[SourceBackedReplacementCandidateFetchStatus] = []
    for task in acquisition_queue.get("tasks") or ():
        if not isinstance(task, Mapping):
            continue
        fetch = fetch_by_task_id.get(_optional_text(task.get("task_id")) or "")
        if fetch is None:
            fetch = fetch_by_candidate_id.get(_optional_text(task.get("replacement_candidate_id")) or "")
        rows.append(_replacement_candidate_fetch_status_for_task(task, fetch))

    by_status: dict[str, int] = {}
    for row in rows:
        by_status[row.fetch_status] = by_status.get(row.fetch_status, 0) + 1
    return {
        "schema_version": "e2r_replacement_candidate_fetch_status_manifest_v1",
        "source_acquisition_queue_schema_version": acquisition_queue.get("schema_version"),
        "summary": {
            "task_count": len(rows),
            "replacement_candidate_current_text_available_count": by_status.get(
                "replacement_candidate_current_text_available_replacement_unverified",
                0,
            ),
            "replacement_candidate_fetch_failed_count": by_status.get("replacement_candidate_fetch_failed", 0),
            "replacement_candidate_fetch_not_attempted_count": by_status.get(
                "replacement_candidate_fetch_not_attempted",
                0,
            ),
            "source_replacement_verified_count": sum(1 for row in rows if row.source_replacement_verified),
            "asof_snapshot_verified_count": sum(1 for row in rows if row.asof_snapshot_verified),
            "evidence_document_fixture_ready_count": sum(
                1 for row in rows if row.evidence_document_fixture_ready
            ),
            "production_score_fixture_count": sum(1 for row in rows if row.production_score_fixture),
        },
        "fetch_status_counts": dict(sorted(by_status.items())),
        "rows": [
            asdict(row)
            for row in sorted(
                rows,
                key=lambda item: (item.archetype_id, item.fixture_seed_id, item.replacement_candidate_id),
            )
        ],
    }


def build_replacement_snapshot_verification_manifest(
    *,
    fetch_status_manifest: Mapping[str, Any],
    verification_rows: Iterable[Mapping[str, Any]],
) -> Mapping[str, Any]:
    verification_by_task_id: dict[str, Mapping[str, Any]] = {}
    verification_by_candidate_id: dict[str, Mapping[str, Any]] = {}
    for row in verification_rows:
        if not isinstance(row, Mapping):
            continue
        task_id = _optional_text(row.get("task_id"))
        replacement_candidate_id = _optional_text(row.get("replacement_candidate_id"))
        if task_id:
            verification_by_task_id[task_id] = row
        if replacement_candidate_id:
            verification_by_candidate_id[replacement_candidate_id] = row

    rows: list[SourceBackedReplacementSnapshotVerificationResult] = []
    for fetch_row in fetch_status_manifest.get("rows") or ():
        if not isinstance(fetch_row, Mapping):
            continue
        verification = verification_by_task_id.get(_optional_text(fetch_row.get("task_id")) or "")
        if verification is None:
            verification = verification_by_candidate_id.get(_optional_text(fetch_row.get("replacement_candidate_id")) or "")
        rows.append(_replacement_snapshot_verification_for_fetch_row(fetch_row, verification))

    by_status: dict[str, int] = {}
    for row in rows:
        by_status[row.verification_status] = by_status.get(row.verification_status, 0) + 1
    return {
        "schema_version": "e2r_replacement_snapshot_verification_manifest_v1",
        "source_fetch_status_schema_version": fetch_status_manifest.get("schema_version"),
        "summary": {
            "row_count": len(rows),
            "replacement_snapshot_verified_count": by_status.get("replacement_snapshot_verified", 0),
            "fetch_not_ready_count": by_status.get("fetch_not_ready", 0),
            "same_event_verification_missing_count": by_status.get("same_event_verification_missing", 0),
            "source_replacement_unverified_count": by_status.get("source_replacement_unverified", 0),
            "attempt_failed_count": by_status.get("attempt_failed", 0),
            "snapshot_url_mismatch_count": by_status.get("snapshot_url_mismatch", 0),
            "invalid_snapshot_date_count": by_status.get("invalid_snapshot_date", 0),
            "future_snapshot_not_allowed_count": by_status.get("future_snapshot_not_allowed", 0),
            "snapshot_text_missing_count": by_status.get("snapshot_text_missing", 0),
            "empty_snapshot_text_count": by_status.get("empty_snapshot_text", 0),
            "content_hash_mismatch_count": by_status.get("content_hash_mismatch", 0),
            "source_replacement_verified_count": sum(1 for row in rows if row.source_replacement_verified),
            "asof_snapshot_verified_count": sum(1 for row in rows if row.asof_snapshot_verified),
            "evidence_document_fixture_ready_count": sum(
                1 for row in rows if row.evidence_document_fixture_ready
            ),
            "production_score_fixture_count": sum(1 for row in rows if row.production_score_fixture),
        },
        "verification_status_counts": dict(sorted(by_status.items())),
        "rows": [
            asdict(row)
            for row in sorted(
                rows,
                key=lambda item: (item.archetype_id, item.fixture_seed_id, item.replacement_candidate_id),
            )
        ],
    }


def build_replacement_snapshot_request_manifest(
    *,
    snapshot_verification_manifest: Mapping[str, Any],
) -> Mapping[str, Any]:
    requests: list[SourceBackedReplacementSnapshotRequest] = []
    for row in snapshot_verification_manifest.get("rows") or ():
        if not isinstance(row, Mapping):
            continue
        request = _replacement_snapshot_request_for_verification_row(row)
        if request is not None:
            requests.append(request)
    by_status: dict[str, int] = {}
    for request in requests:
        by_status[request.request_status] = by_status.get(request.request_status, 0) + 1
    return {
        "schema_version": "e2r_replacement_snapshot_request_manifest_v1",
        "source_snapshot_verification_schema_version": snapshot_verification_manifest.get("schema_version"),
        "summary": {
            "request_count": len(requests),
            "fetch_snapshot_required_count": by_status.get("fetch_candidate_snapshot_required", 0),
            "same_event_verification_required_count": by_status.get("same_event_verification_required", 0),
            "asof_date_repair_required_count": by_status.get("asof_date_repair_required", 0),
            "text_snapshot_repair_required_count": by_status.get("text_snapshot_repair_required", 0),
            "hash_repair_required_count": by_status.get("hash_repair_required", 0),
            "score_blocked_request_count": sum(1 for request in requests if request.score_blocked_until_resolved),
            "source_replacement_verified_count": sum(1 for request in requests if request.source_replacement_verified),
            "asof_snapshot_verified_count": sum(1 for request in requests if request.asof_snapshot_verified),
            "evidence_document_fixture_ready_count": sum(
                1 for request in requests if request.evidence_document_fixture_ready
            ),
            "production_score_fixture_count": sum(1 for request in requests if request.production_score_fixture),
        },
        "request_status_counts": dict(sorted(by_status.items())),
        "requests": [
            asdict(request)
            for request in sorted(
                requests,
                key=lambda item: (item.archetype_id, item.fixture_seed_id, item.replacement_candidate_id),
            )
        ],
    }


def build_replacement_snapshot_verifier_task_manifest(
    *,
    snapshot_request_manifest: Mapping[str, Any],
) -> Mapping[str, Any]:
    tasks = [
        _replacement_snapshot_verifier_task_for_request(request)
        for request in snapshot_request_manifest.get("requests") or ()
        if isinstance(request, Mapping)
    ]
    by_status: dict[str, int] = {}
    for task in tasks:
        by_status[task.verifier_task_status] = by_status.get(task.verifier_task_status, 0) + 1
    return {
        "schema_version": "e2r_replacement_snapshot_verifier_task_manifest_v1",
        "source_snapshot_request_schema_version": snapshot_request_manifest.get("schema_version"),
        "summary": {
            "task_count": len(tasks),
            "ready_for_same_event_asof_verifier_count": by_status.get(
                "ready_for_same_event_asof_verifier",
                0,
            ),
            "blocked_until_candidate_text_snapshot_count": by_status.get(
                "blocked_until_candidate_text_snapshot",
                0,
            ),
            "ready_for_asof_date_repair_verifier_count": by_status.get(
                "ready_for_asof_date_repair_verifier",
                0,
            ),
            "blocked_until_text_snapshot_repair_count": by_status.get(
                "blocked_until_text_snapshot_repair",
                0,
            ),
            "score_blocked_task_count": sum(1 for task in tasks if task.score_blocked_until_verified),
            "production_score_fixture_count": sum(1 for task in tasks if task.production_score_fixture),
        },
        "verifier_task_status_counts": dict(sorted(by_status.items())),
        "tasks": [
            asdict(task)
            for task in sorted(tasks, key=lambda item: (item.verifier_task_status, item.archetype_id, item.task_id))
        ],
    }


def build_replacement_snapshot_verifier_result_manifest(
    *,
    verifier_task_manifest: Mapping[str, Any],
    verifier_rows: Iterable[Mapping[str, Any]],
) -> Mapping[str, Any]:
    rows_by_task_id: dict[str, Mapping[str, Any]] = {}
    rows_by_candidate_id: dict[str, Mapping[str, Any]] = {}
    for row in verifier_rows:
        if not isinstance(row, Mapping):
            continue
        task_id = _optional_text(row.get("task_id") or row.get("verifier_task_id"))
        replacement_candidate_id = _optional_text(row.get("replacement_candidate_id"))
        if task_id:
            rows_by_task_id[task_id] = row
        if replacement_candidate_id:
            rows_by_candidate_id[replacement_candidate_id] = row

    results: list[SourceBackedReplacementSnapshotVerifierResult] = []
    for task in verifier_task_manifest.get("tasks") or ():
        if not isinstance(task, Mapping):
            continue
        row = rows_by_task_id.get(_optional_text(task.get("task_id")) or "")
        if row is None:
            row = rows_by_candidate_id.get(_optional_text(task.get("replacement_candidate_id")) or "")
        results.append(_replacement_snapshot_verifier_result_for_task(task, row))

    by_status: dict[str, int] = {}
    for result in results:
        by_status[result.result_status] = by_status.get(result.result_status, 0) + 1
    accepted_rows = [
        dict(result.accepted_verification_row)
        for result in results
        if result.accepted_verification_row is not None
    ]
    return {
        "schema_version": "e2r_replacement_snapshot_verifier_result_manifest_v1",
        "source_verifier_task_schema_version": verifier_task_manifest.get("schema_version"),
        "summary": {
            "result_count": len(results),
            "same_event_asof_verified_count": by_status.get("same_event_asof_verified", 0),
            "blocked_task_not_ready_count": by_status.get("blocked_task_not_ready", 0),
            "no_verifier_result_count": by_status.get("no_verifier_result", 0),
            "forbidden_output_field_count": by_status.get("forbidden_output_field", 0),
            "same_event_unverified_count": by_status.get("same_event_unverified", 0),
            "invalid_snapshot_date_count": by_status.get("invalid_snapshot_date", 0),
            "future_snapshot_not_allowed_count": by_status.get("future_snapshot_not_allowed", 0),
            "snapshot_url_mismatch_count": by_status.get("snapshot_url_mismatch", 0),
            "snapshot_text_missing_count": by_status.get("snapshot_text_missing", 0),
            "content_hash_mismatch_count": by_status.get("content_hash_mismatch", 0),
            "accepted_verification_row_count": len(accepted_rows),
            "production_score_fixture_count": sum(1 for result in results if result.production_score_fixture),
        },
        "result_status_counts": dict(sorted(by_status.items())),
        "accepted_verification_rows": accepted_rows,
        "results": [
            asdict(result)
            for result in sorted(results, key=lambda item: (item.result_status, item.archetype_id, item.result_id))
        ],
    }


def build_replacement_evidence_document_fixture_manifest(
    *,
    snapshot_verification_manifest: Mapping[str, Any],
    anchor_max_chars: int = 800,
) -> Mapping[str, Any]:
    rows: list[SourceBackedReplacementEvidenceDocumentFixture] = []
    for row in snapshot_verification_manifest.get("rows") or ():
        if not isinstance(row, Mapping):
            continue
        rows.append(_replacement_evidence_document_fixture_for_snapshot_row(row, anchor_max_chars=anchor_max_chars))

    return {
        "schema_version": "e2r_replacement_evidence_document_fixture_manifest_v1",
        "source_snapshot_verification_schema_version": snapshot_verification_manifest.get("schema_version"),
        "summary": {
            "row_count": len(rows),
            "evidence_document_fixture_ready_count": sum(
                1 for row in rows if row.evidence_document_fixture_ready
            ),
            "anchor_verified_count": sum(1 for row in rows if row.anchor_verified),
            "replacement_snapshot_not_verified_count": sum(
                1 for row in rows if row.fixture_status == "replacement_snapshot_not_verified"
            ),
            "snapshot_text_missing_count": sum(1 for row in rows if row.fixture_status == "snapshot_text_missing"),
            "invalid_snapshot_date_count": sum(1 for row in rows if row.fixture_status == "invalid_snapshot_date"),
            "empty_snapshot_text_count": sum(1 for row in rows if row.fixture_status == "empty_snapshot_text"),
            "content_hash_mismatch_count": sum(1 for row in rows if row.fixture_status == "content_hash_mismatch"),
            "anchor_verification_failed_count": sum(
                1 for row in rows if row.fixture_status == "anchor_verification_failed"
            ),
            "claim_replay_ready_count": sum(1 for row in rows if row.claim_replay_ready),
            "production_score_fixture_count": sum(1 for row in rows if row.production_score_fixture),
        },
        "rows": [
            asdict(row)
            for row in sorted(
                rows,
                key=lambda item: (item.archetype_id, item.fixture_seed_id, item.replacement_candidate_id),
            )
        ],
    }


def build_claim_replay_task_manifest(
    *,
    evidence_document_fixture_manifest: Mapping[str, Any] | None = None,
    replacement_evidence_document_fixture_manifest: Mapping[str, Any] | None = None,
    target_identity_by_candidate_id: Mapping[str, Mapping[str, Any]] | None = None,
    target_identity_by_fixture_seed_id: Mapping[str, Mapping[str, Any]] | None = None,
    max_tasks: int | None = None,
) -> Mapping[str, Any]:
    if max_tasks is not None and max_tasks < 1:
        raise ValueError("max_tasks must be positive when provided")
    inputs = (
        ("source_snapshot_fixture", evidence_document_fixture_manifest),
        ("replacement_snapshot_fixture", replacement_evidence_document_fixture_manifest),
    )
    tasks: list[SourceBackedClaimReplayTask] = []
    skipped: list[Mapping[str, Any]] = []
    seen_keys: set[tuple[str, str, str, str]] = set()
    for fixture_kind, manifest in inputs:
        if not manifest:
            continue
        for row in manifest.get("rows") or ():
            if not isinstance(row, Mapping):
                continue
            task, skip = _claim_replay_task_for_fixture_row(
                row,
                fixture_kind=fixture_kind,
                target_identity_by_candidate_id=target_identity_by_candidate_id or {},
                target_identity_by_fixture_seed_id=target_identity_by_fixture_seed_id or {},
            )
            if task is None:
                skipped.append(skip)
                continue
            key = (task.archetype_id, task.target_entity_id, task.document_id, task.anchor_id)
            if key in seen_keys:
                skipped.append(
                    _claim_replay_skip_row(
                        row,
                        fixture_kind=fixture_kind,
                        skip_reason="duplicate_claim_replay_task",
                        duplicate_task_id=next(
                            existing.task_id
                            for existing in tasks
                            if (
                                existing.archetype_id,
                                existing.target_entity_id,
                                existing.document_id,
                                existing.anchor_id,
                            )
                            == key
                        ),
                    )
                )
                continue
            seen_keys.add(key)
            tasks.append(task)
    selected_tasks = tasks[:max_tasks] if max_tasks is not None else tasks
    if max_tasks is not None and len(tasks) > len(selected_tasks):
        selected_ids = {task.task_id for task in selected_tasks}
        for task in tasks:
            if task.task_id not in selected_ids:
                skipped.append(
                    {
                        "fixture_kind": task.fixture_kind,
                        "fixture_seed_id": task.fixture_seed_id,
                        "candidate_id": task.candidate_id,
                        "archetype_id": task.archetype_id,
                        "document_id": task.document_id,
                        "anchor_id": task.anchor_id,
                        "skip_reason": "claim_replay_task_over_max_tasks",
                    }
                )

    return {
        "schema_version": "e2r_claim_replay_task_manifest_v1",
        "source_evidence_document_fixture_schema_version": (evidence_document_fixture_manifest or {}).get("schema_version"),
        "replacement_evidence_document_fixture_schema_version": (
            replacement_evidence_document_fixture_manifest or {}
        ).get("schema_version"),
        "summary": {
            "task_count": len(selected_tasks),
            "skipped_fixture_count": len(skipped),
            "contract_blind_task_count": sum(1 for task in selected_tasks if task.contract_blind_extraction),
            "score_blocked_task_count": sum(
                1 for task in selected_tasks if task.score_blocked_until_claim_replay
            ),
            "source_snapshot_task_count": sum(
                1 for task in selected_tasks if task.fixture_kind == "source_snapshot_fixture"
            ),
            "replacement_snapshot_task_count": sum(
                1 for task in selected_tasks if task.fixture_kind == "replacement_snapshot_fixture"
            ),
            "production_score_fixture_count": sum(1 for task in selected_tasks if task.production_score_fixture),
            "fixture_not_ready_count": sum(
                1 for item in skipped if item.get("skip_reason") == "evidence_document_fixture_not_ready"
            ),
            "fixture_text_missing_count": sum(
                1 for item in skipped if item.get("skip_reason") == "fixture_text_missing"
            ),
            "fixture_text_hash_mismatch_count": sum(
                1 for item in skipped if item.get("skip_reason") == "fixture_text_hash_mismatch"
            ),
            "target_identity_missing_count": sum(
                1 for item in skipped if item.get("skip_reason") == "target_identity_missing"
            ),
            "duplicate_task_skipped_count": sum(
                1 for item in skipped if item.get("skip_reason") == "duplicate_claim_replay_task"
            ),
        },
        "tasks": [asdict(task) for task in selected_tasks],
        "skipped_fixtures": list(skipped),
    }


def build_claim_replay_result_manifest(
    *,
    claim_replay_task_manifest: Mapping[str, Any],
    extraction_rows: Iterable[Mapping[str, Any]] = (),
) -> Mapping[str, Any]:
    extraction_by_task_id: dict[str, Mapping[str, Any]] = {}
    for row in extraction_rows:
        if not isinstance(row, Mapping):
            continue
        task_id = _optional_text(row.get("task_id"))
        if task_id:
            extraction_by_task_id[task_id] = row

    results: list[SourceBackedClaimReplayResult] = []
    for task in claim_replay_task_manifest.get("tasks") or ():
        if not isinstance(task, Mapping):
            continue
        extraction_row = extraction_by_task_id.get(_optional_text(task.get("task_id")) or "")
        results.append(_claim_replay_result_for_task(task, extraction_row))

    by_status: dict[str, int] = {}
    for result in results:
        by_status[result.replay_status] = by_status.get(result.replay_status, 0) + 1
    return {
        "schema_version": "e2r_claim_replay_result_manifest_v1",
        "source_claim_replay_task_schema_version": claim_replay_task_manifest.get("schema_version"),
        "summary": {
            "task_count": len(results),
            "raw_assertions_extracted_count": by_status.get("raw_assertions_extracted", 0),
            "no_raw_assertions_count": by_status.get("no_raw_assertions", 0),
            "claim_replay_not_attempted_count": by_status.get("claim_replay_not_attempted", 0),
            "provider_error_count": by_status.get("provider_error", 0),
            "invalid_provider_output_count": by_status.get("invalid_provider_output", 0),
            "raw_assertion_anchor_mismatch_count": by_status.get("raw_assertion_anchor_mismatch", 0),
            "adjudication_ready_count": sum(1 for result in results if result.adjudication_ready),
            "score_blocked_result_count": sum(1 for result in results if result.score_blocked_until_adjudication),
            "production_score_fixture_count": sum(1 for result in results if result.production_score_fixture),
            "raw_assertion_count": sum(result.raw_assertion_count for result in results),
        },
        "replay_status_counts": dict(sorted(by_status.items())),
        "results": [asdict(result) for result in results],
    }


def build_adjudication_task_manifest(
    *,
    claim_replay_result_manifest: Mapping[str, Any],
) -> Mapping[str, Any]:
    tasks: list[SourceBackedAdjudicationTask] = []
    skipped: list[Mapping[str, Any]] = []
    for result in claim_replay_result_manifest.get("results") or ():
        if not isinstance(result, Mapping):
            continue
        if result.get("replay_status") != "raw_assertions_extracted" or not _optional_bool(
            result.get("adjudication_ready")
        ):
            skipped.append(_adjudication_skip_row(result, skip_reason="claim_replay_not_ready"))
            continue
        raw_assertions = result.get("raw_assertions")
        if not isinstance(raw_assertions, Sequence) or isinstance(raw_assertions, (str, bytes, bytearray)):
            skipped.append(_adjudication_skip_row(result, skip_reason="raw_assertion_payload_missing"))
            continue
        for raw in raw_assertions:
            if not isinstance(raw, Mapping):
                skipped.append(_adjudication_skip_row(result, skip_reason="raw_assertion_payload_invalid"))
                continue
            task = _adjudication_task_for_raw_assertion(result, raw)
            if task is None:
                skipped.append(_adjudication_skip_row(result, skip_reason="raw_assertion_anchor_mismatch"))
                continue
            tasks.append(task)

    return {
        "schema_version": "e2r_adjudication_task_manifest_v1",
        "source_claim_replay_result_schema_version": claim_replay_result_manifest.get("schema_version"),
        "summary": {
            "task_count": len(tasks),
            "skipped_result_count": len(skipped),
            "score_blocked_task_count": sum(1 for task in tasks if task.score_blocked_until_adjudication),
            "production_score_fixture_count": sum(1 for task in tasks if task.production_score_fixture),
            "claim_replay_not_ready_count": sum(
                1 for item in skipped if item.get("skip_reason") == "claim_replay_not_ready"
            ),
            "raw_assertion_payload_missing_count": sum(
                1 for item in skipped if item.get("skip_reason") == "raw_assertion_payload_missing"
            ),
            "raw_assertion_anchor_mismatch_count": sum(
                1 for item in skipped if item.get("skip_reason") == "raw_assertion_anchor_mismatch"
            ),
        },
        "tasks": [asdict(task) for task in tasks],
        "skipped_results": skipped,
    }


def build_adjudication_result_manifest(
    *,
    adjudication_task_manifest: Mapping[str, Any],
    adjudication_rows: Iterable[Mapping[str, Any]] = (),
) -> Mapping[str, Any]:
    adjudication_by_task_id: dict[str, Mapping[str, Any]] = {}
    for row in adjudication_rows:
        if not isinstance(row, Mapping):
            continue
        task_id = _optional_text(row.get("task_id"))
        if task_id:
            adjudication_by_task_id[task_id] = row

    results: list[SourceBackedAdjudicationResult] = []
    for task in adjudication_task_manifest.get("tasks") or ():
        if not isinstance(task, Mapping):
            continue
        row = adjudication_by_task_id.get(_optional_text(task.get("task_id")) or "")
        results.append(_adjudication_result_for_task(task, row))

    by_status: dict[str, int] = {}
    for result in results:
        by_status[result.adjudication_status] = by_status.get(result.adjudication_status, 0) + 1
    return {
        "schema_version": "e2r_adjudication_result_manifest_v1",
        "source_adjudication_task_schema_version": adjudication_task_manifest.get("schema_version"),
        "summary": {
            "task_count": len(results),
            "mapping_ready_count": sum(1 for result in results if result.mapping_ready),
            "adjudication_not_attempted_count": by_status.get("adjudication_not_attempted", 0),
            "provider_error_count": by_status.get("provider_error", 0),
            "invalid_provider_output_count": by_status.get("invalid_provider_output", 0),
            "target_scope_blocked_count": by_status.get("target_scope_blocked", 0),
            "temporal_blocked_count": by_status.get("temporal_blocked", 0),
            "semantic_blocked_count": by_status.get("semantic_blocked", 0),
            "investigation_blocked_count": by_status.get("investigation_blocked", 0),
            "score_blocked_result_count": sum(1 for result in results if result.score_blocked_until_mapping),
            "production_score_fixture_count": sum(1 for result in results if result.production_score_fixture),
        },
        "adjudication_status_counts": dict(sorted(by_status.items())),
        "results": [asdict(result) for result in results],
    }


def build_primitive_mapping_task_manifest(
    *,
    adjudication_result_manifest: Mapping[str, Any],
) -> Mapping[str, Any]:
    tasks: list[SourceBackedPrimitiveMappingTask] = []
    skipped: list[Mapping[str, Any]] = []
    for result in adjudication_result_manifest.get("results") or ():
        if not isinstance(result, Mapping):
            continue
        task = _primitive_mapping_task_for_adjudication_result(result)
        if task is None:
            skipped.append(_primitive_mapping_skip_row(result, skip_reason="adjudication_not_mapping_ready"))
            continue
        tasks.append(task)

    return {
        "schema_version": "e2r_primitive_mapping_task_manifest_v1",
        "source_adjudication_result_schema_version": adjudication_result_manifest.get("schema_version"),
        "summary": {
            "task_count": len(tasks),
            "skipped_result_count": len(skipped),
            "score_blocked_task_count": sum(1 for task in tasks if task.score_blocked_until_mapping),
            "production_score_fixture_count": sum(1 for task in tasks if task.production_score_fixture),
            "adjudication_not_mapping_ready_count": sum(
                1 for item in skipped if item.get("skip_reason") == "adjudication_not_mapping_ready"
            ),
        },
        "tasks": [asdict(task) for task in tasks],
        "skipped_results": skipped,
    }


def build_primitive_mapping_result_manifest(
    *,
    primitive_mapping_task_manifest: Mapping[str, Any],
    mapping_rows: Iterable[Mapping[str, Any]] = (),
    canonical_primitive_ids_by_archetype: Mapping[str, Sequence[str]] | None = None,
) -> Mapping[str, Any]:
    rows_by_task_id: dict[str, list[Mapping[str, Any]]] = {}
    for row in mapping_rows:
        if not isinstance(row, Mapping):
            continue
        task_id = _optional_text(row.get("task_id"))
        if task_id:
            rows_by_task_id.setdefault(task_id, []).append(row)

    results: list[SourceBackedPrimitiveMappingResult] = []
    for task in primitive_mapping_task_manifest.get("tasks") or ():
        if not isinstance(task, Mapping):
            continue
        task_rows = rows_by_task_id.get(_optional_text(task.get("task_id")) or "", [])
        if not task_rows:
            results.append(_primitive_mapping_result_for_missing_task(task))
            continue
        for row in task_rows:
            results.extend(
                _primitive_mapping_results_for_task_row(
                    task,
                    row,
                    canonical_primitive_ids_by_archetype=canonical_primitive_ids_by_archetype or {},
                )
            )

    by_status: dict[str, int] = {}
    for result in results:
        by_status[result.result_status] = by_status.get(result.result_status, 0) + 1
    return {
        "schema_version": "e2r_primitive_mapping_result_manifest_v1",
        "source_primitive_mapping_task_schema_version": primitive_mapping_task_manifest.get("schema_version"),
        "summary": {
            "result_count": len(results),
            "eligibility_ready_count": sum(1 for result in results if result.eligibility_ready),
            "mapping_not_attempted_count": by_status.get("mapping_not_attempted", 0),
            "provider_error_count": by_status.get("provider_error", 0),
            "invalid_provider_output_count": by_status.get("invalid_provider_output", 0),
            "claim_id_mismatch_count": by_status.get("claim_id_mismatch", 0),
            "primitive_registry_missing_count": by_status.get("primitive_registry_missing", 0),
            "invented_primitive_blocked_count": by_status.get("invented_primitive_blocked", 0),
            "mapping_rejected_count": by_status.get("mapping_rejected", 0),
            "score_blocked_result_count": sum(1 for result in results if result.score_blocked_until_eligibility),
            "production_score_fixture_count": sum(1 for result in results if result.production_score_fixture),
        },
        "result_status_counts": dict(sorted(by_status.items())),
        "results": [asdict(result) for result in results],
    }


def build_eligibility_task_manifest(
    *,
    primitive_mapping_result_manifest: Mapping[str, Any],
) -> Mapping[str, Any]:
    tasks: list[SourceBackedEligibilityTask] = []
    skipped: list[Mapping[str, Any]] = []
    for result in primitive_mapping_result_manifest.get("results") or ():
        if not isinstance(result, Mapping):
            continue
        task = _eligibility_task_for_mapping_result(result)
        if task is None:
            skipped.append(_eligibility_skip_row(result, skip_reason="primitive_mapping_not_eligibility_ready"))
            continue
        tasks.append(task)
    return {
        "schema_version": "e2r_eligibility_task_manifest_v1",
        "source_primitive_mapping_result_schema_version": primitive_mapping_result_manifest.get("schema_version"),
        "summary": {
            "task_count": len(tasks),
            "skipped_result_count": len(skipped),
            "score_blocked_task_count": sum(1 for task in tasks if task.score_blocked_until_eligibility),
            "production_score_fixture_count": sum(1 for task in tasks if task.production_score_fixture),
            "primitive_mapping_not_ready_count": sum(
                1 for item in skipped if item.get("skip_reason") == "primitive_mapping_not_eligibility_ready"
            ),
        },
        "tasks": [asdict(task) for task in tasks],
        "skipped_results": skipped,
    }


def build_eligibility_result_manifest(
    *,
    eligibility_task_manifest: Mapping[str, Any],
    eligibility_rows: Iterable[Mapping[str, Any]] = (),
) -> Mapping[str, Any]:
    rows_by_task_id: dict[str, Mapping[str, Any]] = {}
    for row in eligibility_rows:
        if not isinstance(row, Mapping):
            continue
        task_id = _optional_text(row.get("task_id"))
        if task_id:
            rows_by_task_id[task_id] = row

    results: list[SourceBackedEligibilityResult] = []
    for task in eligibility_task_manifest.get("tasks") or ():
        if not isinstance(task, Mapping):
            continue
        row = rows_by_task_id.get(_optional_text(task.get("task_id")) or "")
        results.append(_eligibility_result_for_task(task, row))

    by_status: dict[str, int] = {}
    for result in results:
        by_status[result.result_status] = by_status.get(result.result_status, 0) + 1
    return {
        "schema_version": "e2r_eligibility_result_manifest_v1",
        "source_eligibility_task_schema_version": eligibility_task_manifest.get("schema_version"),
        "summary": {
            "task_count": len(results),
            "score_contribution_ready_count": sum(1 for result in results if result.eligibility_ready),
            "eligibility_not_attempted_count": by_status.get("eligibility_not_attempted", 0),
            "invalid_eligibility_output_count": by_status.get("invalid_eligibility_output", 0),
            "non_deterministic_eligibility_blocked_count": by_status.get("non_deterministic_eligibility_blocked", 0),
            "source_anchor_unverified_count": by_status.get("source_anchor_unverified", 0),
            "future_leakage_blocked_count": by_status.get("future_leakage_blocked", 0),
            "source_proxy_blocked_count": by_status.get("source_proxy_blocked", 0),
            "snippet_only_blocked_count": by_status.get("snippet_only_blocked", 0),
            "contradiction_blocked_count": by_status.get("contradiction_blocked", 0),
            "eligibility_rejected_count": by_status.get("eligibility_rejected", 0),
            "score_blocked_result_count": sum(
                1 for result in results if result.score_blocked_until_score_contribution
            ),
            "production_score_fixture_count": sum(1 for result in results if result.production_score_fixture),
        },
        "result_status_counts": dict(sorted(by_status.items())),
        "results": [asdict(result) for result in results],
    }


def build_score_contribution_task_manifest(
    *,
    eligibility_result_manifest: Mapping[str, Any],
) -> Mapping[str, Any]:
    tasks: list[SourceBackedScoreContributionTask] = []
    skipped: list[Mapping[str, Any]] = []
    for result in eligibility_result_manifest.get("results") or ():
        if not isinstance(result, Mapping):
            continue
        task = _score_contribution_task_for_eligibility_result(result)
        if task is None:
            skipped.append(_score_contribution_skip_row(result, skip_reason="eligibility_not_ready"))
            continue
        tasks.append(task)
    return {
        "schema_version": "e2r_score_contribution_task_manifest_v1",
        "source_eligibility_result_schema_version": eligibility_result_manifest.get("schema_version"),
        "summary": {
            "task_count": len(tasks),
            "skipped_result_count": len(skipped),
            "score_blocked_task_count": sum(1 for task in tasks if task.score_blocked_until_score_contribution),
            "production_score_fixture_count": sum(1 for task in tasks if task.production_score_fixture),
            "eligibility_not_ready_count": sum(
                1 for item in skipped if item.get("skip_reason") == "eligibility_not_ready"
            ),
        },
        "tasks": [asdict(task) for task in tasks],
        "skipped_results": skipped,
    }


def build_score_contribution_result_manifest(
    *,
    score_contribution_task_manifest: Mapping[str, Any],
    contribution_rows: Iterable[Mapping[str, Any]] = (),
) -> Mapping[str, Any]:
    rows_by_task_id: dict[str, Mapping[str, Any]] = {}
    for row in contribution_rows:
        if not isinstance(row, Mapping):
            continue
        task_id = _optional_text(row.get("task_id"))
        if task_id:
            rows_by_task_id[task_id] = row

    results: list[SourceBackedScoreContributionResult] = []
    for task in score_contribution_task_manifest.get("tasks") or ():
        if not isinstance(task, Mapping):
            continue
        row = rows_by_task_id.get(_optional_text(task.get("task_id")) or "")
        results.append(_score_contribution_result_for_task(task, row))

    by_status: dict[str, int] = {}
    for result in results:
        by_status[result.result_status] = by_status.get(result.result_status, 0) + 1
    return {
        "schema_version": "e2r_score_contribution_result_manifest_v1",
        "source_score_contribution_task_schema_version": score_contribution_task_manifest.get("schema_version"),
        "summary": {
            "task_count": len(results),
            "score_contribution_ready_count": sum(1 for result in results if result.score_contribution_ready),
            "score_contribution_not_attempted_count": by_status.get("score_contribution_not_attempted", 0),
            "invalid_score_contribution_output_count": by_status.get("invalid_score_contribution_output", 0),
            "non_deterministic_score_contribution_blocked_count": by_status.get(
                "non_deterministic_score_contribution_blocked", 0
            ),
            "component_missing_count": by_status.get("component_missing", 0),
            "criterion_missing_count": by_status.get("criterion_missing", 0),
            "negative_points_blocked_count": by_status.get("negative_points_blocked", 0),
            "over_max_points_blocked_count": by_status.get("over_max_points_blocked", 0),
            "orphan_score_blocked_count": by_status.get("orphan_score_blocked", 0),
            "production_score_fixture_count": sum(1 for result in results if result.production_score_fixture),
        },
        "result_status_counts": dict(sorted(by_status.items())),
        "results": [asdict(result) for result in results],
    }


def build_score_snapshot_task_manifest(
    *,
    score_contribution_result_manifest: Mapping[str, Any],
) -> Mapping[str, Any]:
    groups: dict[tuple[str, str, str, str], list[Mapping[str, Any]]] = {}
    for result in score_contribution_result_manifest.get("results") or ():
        if not isinstance(result, Mapping):
            continue
        key = (
            _optional_text(result.get("fixture_seed_id")) or "",
            _optional_text(result.get("candidate_id")) or "",
            _optional_text(result.get("archetype_id")) or "",
            _optional_text(result.get("target_entity_id")) or "",
        )
        groups.setdefault(key, []).append(result)

    tasks: list[SourceBackedScoreSnapshotTask] = []
    skipped: list[Mapping[str, Any]] = []
    for key, rows in sorted(groups.items()):
        task = _score_snapshot_task_for_group(key, rows)
        if task is None:
            skipped.append(_score_snapshot_skip_row(key, rows))
            continue
        tasks.append(task)

    return {
        "schema_version": "e2r_score_snapshot_task_manifest_v1",
        "source_score_contribution_result_schema_version": score_contribution_result_manifest.get(
            "schema_version"
        ),
        "summary": {
            "task_count": len(tasks),
            "skipped_candidate_count": len(skipped),
            "score_blocked_task_count": sum(1 for task in tasks if task.score_blocked_until_stage_court),
            "production_score_fixture_count": sum(1 for task in tasks if task.production_score_fixture),
            "ready_contribution_count": sum(len(task.contribution_ids) for task in tasks),
            "blocked_candidate_count": sum(
                1 for item in skipped if item.get("skip_reason") == "score_contribution_results_not_all_ready"
            ),
        },
        "tasks": [asdict(task) for task in tasks],
        "skipped_candidates": skipped,
    }


def build_score_snapshot_result_manifest(
    *,
    score_snapshot_task_manifest: Mapping[str, Any],
    score_contribution_result_manifest: Mapping[str, Any],
    snapshot_rows: Iterable[Mapping[str, Any]] = (),
) -> Mapping[str, Any]:
    rows_by_task_id: dict[str, Mapping[str, Any]] = {}
    for row in snapshot_rows:
        if not isinstance(row, Mapping):
            continue
        task_id = _optional_text(row.get("task_id"))
        if task_id:
            rows_by_task_id[task_id] = row

    contribution_results_by_id = {
        _optional_text(row.get("contribution_id")) or "": row
        for row in score_contribution_result_manifest.get("results") or ()
        if isinstance(row, Mapping) and _optional_text(row.get("contribution_id"))
    }
    results: list[SourceBackedScoreSnapshotResult] = []
    for task in score_snapshot_task_manifest.get("tasks") or ():
        if not isinstance(task, Mapping):
            continue
        row = rows_by_task_id.get(_optional_text(task.get("task_id")) or "")
        results.append(_score_snapshot_result_for_task(task, row, contribution_results_by_id))

    by_status: dict[str, int] = {}
    for result in results:
        by_status[result.result_status] = by_status.get(result.result_status, 0) + 1
    return {
        "schema_version": "e2r_score_snapshot_result_manifest_v1",
        "source_score_snapshot_task_schema_version": score_snapshot_task_manifest.get("schema_version"),
        "source_score_contribution_result_schema_version": score_contribution_result_manifest.get(
            "schema_version"
        ),
        "summary": {
            "task_count": len(results),
            "score_interval_ready_count": sum(1 for result in results if result.score_interval_ready),
            "score_snapshot_not_attempted_count": by_status.get("score_snapshot_not_attempted", 0),
            "invalid_score_snapshot_output_count": by_status.get("invalid_score_snapshot_output", 0),
            "non_deterministic_score_snapshot_blocked_count": by_status.get(
                "non_deterministic_score_snapshot_blocked", 0
            ),
            "contribution_set_mismatch_count": by_status.get("contribution_set_mismatch", 0),
            "score_snapshot_sum_mismatch_count": by_status.get("score_snapshot_sum_mismatch", 0),
            "negative_material_gap_blocked_count": by_status.get("negative_material_gap_blocked", 0),
            "score_blocked_task_count": sum(1 for result in results if result.score_blocked_until_stage_court),
            "production_score_fixture_count": sum(1 for result in results if result.production_score_fixture),
        },
        "result_status_counts": dict(sorted(by_status.items())),
        "results": [asdict(result) for result in results],
    }


def build_stage_court_task_manifest(
    *,
    score_snapshot_result_manifest: Mapping[str, Any],
    score_contribution_result_manifest: Mapping[str, Any],
    contracts_by_archetype: Mapping[str, EvidenceContractV2],
) -> Mapping[str, Any]:
    contribution_results_by_id = _contribution_results_by_contribution_id(score_contribution_result_manifest)
    tasks: list[SourceBackedStageCourtTask] = []
    skipped: list[Mapping[str, Any]] = []
    for result in score_snapshot_result_manifest.get("results") or ():
        if not isinstance(result, Mapping):
            continue
        task = _stage_court_task_for_score_snapshot_result(
            result,
            contribution_results_by_id=contribution_results_by_id,
            contracts_by_archetype=contracts_by_archetype,
        )
        if task is None:
            skipped.append(_stage_court_task_skip_row(result, contracts_by_archetype=contracts_by_archetype))
            continue
        tasks.append(task)
    return {
        "schema_version": "e2r_stage_court_task_manifest_v1",
        "source_score_snapshot_result_schema_version": score_snapshot_result_manifest.get("schema_version"),
        "summary": {
            "task_count": len(tasks),
            "skipped_result_count": len(skipped),
            "score_interval_not_ready_count": sum(
                1 for row in skipped if row.get("skip_reason") == "score_interval_not_ready"
            ),
            "evidence_contract_missing_count": sum(
                1 for row in skipped if row.get("skip_reason") == "evidence_contract_missing"
            ),
            "primitive_state_missing_count": sum(
                1 for row in skipped if row.get("skip_reason") == "primitive_state_missing"
            ),
            "score_blocked_task_count": sum(1 for task in tasks if task.score_blocked_until_stage_court_result),
            "production_score_fixture_count": sum(1 for task in tasks if task.production_score_fixture),
            "production_stage_fixture_count": sum(1 for task in tasks if task.production_stage_fixture),
        },
        "tasks": [asdict(task) for task in tasks],
        "skipped_results": skipped,
    }


def build_stage_court_result_manifest(
    *,
    stage_court_task_manifest: Mapping[str, Any],
    score_contribution_result_manifest: Mapping[str, Any],
    contracts_by_archetype: Mapping[str, EvidenceContractV2],
) -> Mapping[str, Any]:
    contribution_results_by_id = _contribution_results_by_contribution_id(score_contribution_result_manifest)
    results: list[SourceBackedStageCourtResult] = []
    for task in stage_court_task_manifest.get("tasks") or ():
        if not isinstance(task, Mapping):
            continue
        results.append(
            _stage_court_result_for_task(
                task,
                contribution_results_by_id=contribution_results_by_id,
                contracts_by_archetype=contracts_by_archetype,
            )
        )
    by_status: dict[str, int] = {}
    for result in results:
        by_status[result.result_status] = by_status.get(result.result_status, 0) + 1
    return {
        "schema_version": "e2r_stage_court_result_manifest_v1",
        "source_stage_court_task_schema_version": stage_court_task_manifest.get("schema_version"),
        "summary": {
            "task_count": len(results),
            "stage_court_ready_count": sum(1 for result in results if result.stage_court_ready),
            "stage_court_failed_count": by_status.get("stage_court_failed", 0),
            "evidence_contract_missing_count": by_status.get("evidence_contract_missing", 0),
            "production_score_fixture_count": sum(1 for result in results if result.production_score_fixture),
            "production_stage_fixture_count": sum(1 for result in results if result.production_stage_fixture),
        },
        "result_status_counts": dict(sorted(by_status.items())),
        "results": [asdict(result) for result in results],
    }


def build_claim_replay_chain_audit_manifest(
    *,
    claim_replay_result_manifest: Mapping[str, Any],
    adjudication_result_manifest: Mapping[str, Any],
    primitive_mapping_result_manifest: Mapping[str, Any],
    eligibility_result_manifest: Mapping[str, Any],
    score_contribution_result_manifest: Mapping[str, Any],
    score_snapshot_result_manifest: Mapping[str, Any],
    stage_court_result_manifest: Mapping[str, Any],
) -> Mapping[str, Any]:
    manifests = (
        claim_replay_result_manifest,
        adjudication_result_manifest,
        primitive_mapping_result_manifest,
        eligibility_result_manifest,
        score_contribution_result_manifest,
        score_snapshot_result_manifest,
        stage_court_result_manifest,
    )
    production_score_total = sum(_summary_int(manifest, "production_score_fixture_count") for manifest in manifests)
    production_stage_total = sum(_summary_int(manifest, "production_stage_fixture_count") for manifest in manifests)
    stage_court_ready_count = _summary_int(stage_court_result_manifest, "stage_court_ready_count")
    score_interval_ready_count = _summary_int(score_snapshot_result_manifest, "score_interval_ready_count")
    first_blocking_stage, first_blocking_reason = _claim_replay_chain_first_blocker(
        claim_replay_result_manifest=claim_replay_result_manifest,
        adjudication_result_manifest=adjudication_result_manifest,
        primitive_mapping_result_manifest=primitive_mapping_result_manifest,
        eligibility_result_manifest=eligibility_result_manifest,
        score_contribution_result_manifest=score_contribution_result_manifest,
        score_snapshot_result_manifest=score_snapshot_result_manifest,
        stage_court_result_manifest=stage_court_result_manifest,
        production_score_total=production_score_total,
        production_stage_total=production_stage_total,
    )
    evidence_os_chain_ready = (
        production_score_total == 0
        and production_stage_total == 0
        and stage_court_ready_count > 0
        and score_interval_ready_count > 0
    )
    if production_score_total or production_stage_total:
        chain_status = "invalid_production_fixture_present"
        blocked_reason = "production_fixture_present_before_cutover"
        reasons = ("production_fixture_present_before_cutover",)
    elif stage_court_ready_count <= 0:
        chain_status = "blocked_no_stage_court_ready_results"
        blocked_reason = "no_stage_court_ready_results"
        reasons = ("no_stage_court_ready_results",)
    else:
        chain_status = "stage_preview_ready_not_production_cutover"
        blocked_reason = "production_cutover_requires_full_replay_acceptance"
        reasons = ("stage_court_preview_ready_but_production_cutover_not_enabled",)

    audit = SourceBackedReplayChainAudit(
        audit_id=_claim_replay_chain_audit_id(
            stage_court_ready_count=stage_court_ready_count,
            production_score_total=production_score_total,
            production_stage_total=production_stage_total,
        ),
        chain_status=chain_status,
        evidence_os_chain_ready=evidence_os_chain_ready,
        production_cutover_ready=False,
        first_blocking_stage=first_blocking_stage,
        first_blocking_reason=first_blocking_reason,
        claim_replay_ready_count=_summary_int(claim_replay_result_manifest, "adjudication_ready_count"),
        adjudication_mapping_ready_count=_summary_int(adjudication_result_manifest, "mapping_ready_count"),
        primitive_mapping_eligibility_ready_count=_summary_int(
            primitive_mapping_result_manifest,
            "eligibility_ready_count",
        ),
        eligibility_score_contribution_ready_count=_summary_int(
            eligibility_result_manifest,
            "score_contribution_ready_count",
        ),
        score_contribution_ready_count=_summary_int(
            score_contribution_result_manifest,
            "score_contribution_ready_count",
        ),
        score_interval_ready_count=score_interval_ready_count,
        stage_court_ready_count=stage_court_ready_count,
        production_score_fixture_total=production_score_total,
        production_stage_fixture_total=production_stage_total,
        blocked_reason=blocked_reason,
        reasons=reasons,
    )
    return {
        "schema_version": "e2r_claim_replay_chain_audit_manifest_v1",
        "input_schema_versions": {
            "claim_replay_results": claim_replay_result_manifest.get("schema_version"),
            "adjudication_results": adjudication_result_manifest.get("schema_version"),
            "primitive_mapping_results": primitive_mapping_result_manifest.get("schema_version"),
            "eligibility_results": eligibility_result_manifest.get("schema_version"),
            "score_contribution_results": score_contribution_result_manifest.get("schema_version"),
            "score_snapshot_results": score_snapshot_result_manifest.get("schema_version"),
            "stage_court_results": stage_court_result_manifest.get("schema_version"),
        },
        "summary": {
            "chain_status": audit.chain_status,
            "evidence_os_chain_ready": audit.evidence_os_chain_ready,
            "production_cutover_ready": audit.production_cutover_ready,
            "stage_court_ready_count": audit.stage_court_ready_count,
            "score_interval_ready_count": audit.score_interval_ready_count,
            "score_contribution_ready_count": audit.score_contribution_ready_count,
            "production_score_fixture_total": audit.production_score_fixture_total,
            "production_stage_fixture_total": audit.production_stage_fixture_total,
            "first_blocking_stage": audit.first_blocking_stage,
            "first_blocking_reason": audit.first_blocking_reason,
            "blocked_reason": audit.blocked_reason,
        },
        "audit": asdict(audit),
    }


def build_claim_replay_readiness_audit_manifest(
    *,
    claim_replay_task_manifest: Mapping[str, Any],
    replacement_evidence_document_fixture_manifest: Mapping[str, Any] | None = None,
    replacement_snapshot_verification_manifest: Mapping[str, Any] | None = None,
    replacement_candidate_fetch_status_manifest: Mapping[str, Any] | None = None,
    replacement_snapshot_request_manifest: Mapping[str, Any] | None = None,
) -> Mapping[str, Any]:
    replacement_fixture_manifest = replacement_evidence_document_fixture_manifest or {}
    verification_manifest = replacement_snapshot_verification_manifest or {}
    fetch_manifest = replacement_candidate_fetch_status_manifest or {}
    snapshot_request_manifest = replacement_snapshot_request_manifest or {}

    claim_replay_task_count = _summary_count(claim_replay_task_manifest, "task_count", "tasks")
    fixture_not_ready_count = _summary_int(claim_replay_task_manifest, "fixture_not_ready_count")
    replacement_fixture_row_count = _summary_count(replacement_fixture_manifest, "row_count", "rows")
    replacement_fixture_ready_count = _summary_int(
        replacement_fixture_manifest,
        "evidence_document_fixture_ready_count",
    )
    replacement_snapshot_not_verified_count = _summary_int(
        replacement_fixture_manifest,
        "replacement_snapshot_not_verified_count",
    )
    verification_row_count = _summary_count(verification_manifest, "row_count", "rows")
    fetch_not_ready_count = _summary_int(verification_manifest, "fetch_not_ready_count")
    snapshot_verified_count = _summary_int(verification_manifest, "replacement_snapshot_verified_count")
    fetch_task_count = _summary_count(fetch_manifest, "task_count", "rows")
    fetch_failed_count = _summary_int(fetch_manifest, "replacement_candidate_fetch_failed_count")
    fetch_not_attempted_count = _summary_int(fetch_manifest, "replacement_candidate_fetch_not_attempted_count")
    current_text_available_count = _summary_int(
        fetch_manifest,
        "replacement_candidate_current_text_available_count",
    )
    snapshot_request_count = _summary_count(snapshot_request_manifest, "request_count", "requests")
    fetch_snapshot_required_count = _summary_int(snapshot_request_manifest, "fetch_snapshot_required_count")
    same_event_verification_required_count = _summary_int(
        snapshot_request_manifest,
        "same_event_verification_required_count",
    )
    score_blocked_request_count = _summary_int(snapshot_request_manifest, "score_blocked_request_count")
    first_stage, first_reason = _claim_replay_readiness_first_blocker(
        claim_replay_task_count=claim_replay_task_count,
        fixture_not_ready_count=fixture_not_ready_count,
        replacement_fixture_row_count=replacement_fixture_row_count,
        replacement_fixture_ready_count=replacement_fixture_ready_count,
        replacement_snapshot_not_verified_count=replacement_snapshot_not_verified_count,
        verification_row_count=verification_row_count,
        fetch_not_ready_count=fetch_not_ready_count,
        snapshot_verified_count=snapshot_verified_count,
        fetch_task_count=fetch_task_count,
        fetch_failed_count=fetch_failed_count,
        fetch_not_attempted_count=fetch_not_attempted_count,
        current_text_available_count=current_text_available_count,
    )
    readiness_status = "claim_replay_tasks_ready" if claim_replay_task_count > 0 else "claim_replay_blocked"
    if first_stage == "replacement_candidate_fetch" and first_reason == "replacement_candidate_fetch_failed":
        readiness_status = "blocked_replacement_candidate_fetch_failed"
    elif first_stage == "replacement_candidate_fetch" and first_reason == "replacement_candidate_fetch_not_attempted":
        readiness_status = "blocked_replacement_candidate_fetch_not_attempted"
    elif first_stage == "replacement_snapshot_verification":
        readiness_status = "blocked_replacement_snapshot_verification"
    elif first_stage == "replacement_evidence_document_fixture":
        readiness_status = "blocked_replacement_evidence_document_fixture"
    production_score_total = sum(
        _summary_int(manifest, "production_score_fixture_count")
        for manifest in (
            claim_replay_task_manifest,
            replacement_fixture_manifest,
            verification_manifest,
            fetch_manifest,
            snapshot_request_manifest,
        )
    )
    audit = SourceBackedClaimReplayReadinessAudit(
        audit_id=_claim_replay_readiness_audit_id(
            readiness_status=readiness_status,
            first_stage=first_stage,
            first_reason=first_reason,
        ),
        readiness_status=readiness_status,
        claim_replay_task_count=claim_replay_task_count,
        fixture_not_ready_count=fixture_not_ready_count,
        replacement_fixture_row_count=replacement_fixture_row_count,
        replacement_fixture_ready_count=replacement_fixture_ready_count,
        replacement_snapshot_not_verified_count=replacement_snapshot_not_verified_count,
        replacement_snapshot_verification_row_count=verification_row_count,
        replacement_fetch_not_ready_count=fetch_not_ready_count,
        replacement_snapshot_verified_count=snapshot_verified_count,
        replacement_candidate_fetch_task_count=fetch_task_count,
        replacement_candidate_fetch_failed_count=fetch_failed_count,
        replacement_candidate_fetch_not_attempted_count=fetch_not_attempted_count,
        replacement_candidate_current_text_available_count=current_text_available_count,
        replacement_snapshot_request_count=snapshot_request_count,
        replacement_fetch_snapshot_required_count=fetch_snapshot_required_count,
        replacement_same_event_verification_required_count=same_event_verification_required_count,
        replacement_score_blocked_request_count=score_blocked_request_count,
        first_upstream_blocking_stage=first_stage,
        first_upstream_blocking_reason=first_reason,
        production_score_fixture_total=production_score_total,
        reasons=tuple(reason for reason in (first_reason,) if reason),
    )
    return {
        "schema_version": "e2r_claim_replay_readiness_audit_manifest_v1",
        "input_schema_versions": {
            "claim_replay_tasks": claim_replay_task_manifest.get("schema_version"),
            "replacement_evidence_document_fixtures": replacement_fixture_manifest.get("schema_version"),
            "replacement_snapshot_verification": verification_manifest.get("schema_version"),
            "replacement_candidate_fetch_status": fetch_manifest.get("schema_version"),
            "replacement_snapshot_requests": snapshot_request_manifest.get("schema_version"),
        },
        "summary": {
            "readiness_status": audit.readiness_status,
            "claim_replay_task_count": audit.claim_replay_task_count,
            "fixture_not_ready_count": audit.fixture_not_ready_count,
            "replacement_fixture_row_count": audit.replacement_fixture_row_count,
            "replacement_fixture_ready_count": audit.replacement_fixture_ready_count,
            "replacement_snapshot_not_verified_count": audit.replacement_snapshot_not_verified_count,
            "replacement_candidate_fetch_failed_count": audit.replacement_candidate_fetch_failed_count,
            "replacement_candidate_fetch_not_attempted_count": audit.replacement_candidate_fetch_not_attempted_count,
            "replacement_candidate_current_text_available_count": (
                audit.replacement_candidate_current_text_available_count
            ),
            "replacement_snapshot_request_count": audit.replacement_snapshot_request_count,
            "replacement_fetch_snapshot_required_count": audit.replacement_fetch_snapshot_required_count,
            "replacement_same_event_verification_required_count": (
                audit.replacement_same_event_verification_required_count
            ),
            "replacement_score_blocked_request_count": audit.replacement_score_blocked_request_count,
            "first_upstream_blocking_stage": audit.first_upstream_blocking_stage,
            "first_upstream_blocking_reason": audit.first_upstream_blocking_reason,
            "production_score_fixture_total": audit.production_score_fixture_total,
        },
        "audit": asdict(audit),
    }


def build_replacement_fetch_failure_audit_manifest(
    *,
    replacement_candidate_fetch_status_manifest: Mapping[str, Any] | None = None,
) -> Mapping[str, Any]:
    fetch_manifest = replacement_candidate_fetch_status_manifest or {}
    rows = [row for row in fetch_manifest.get("rows") or () if isinstance(row, Mapping)]
    tasks = [
        task
        for task in (
            _replacement_fetch_remediation_task_for_fetch_row(row)
            for row in rows
        )
        if task is not None
    ]
    reason_groups = _replacement_fetch_reason_groups(rows)
    first_reason = tasks[0].reason if tasks else None
    fetch_failed_count = sum(1 for row in rows if row.get("fetch_status") == "replacement_candidate_fetch_failed")
    fetch_not_attempted_count = sum(
        1 for row in rows if row.get("fetch_status") == "replacement_candidate_fetch_not_attempted"
    )
    current_text_available_count = sum(
        1
        for row in rows
        if row.get("fetch_status") == "replacement_candidate_current_text_available_replacement_unverified"
    )
    text_snapshot_required_count = sum(
        1 for task in tasks if task.remediation_status == "text_snapshot_required"
    )
    bounded_fetch_required_count = sum(
        1 for task in tasks if task.remediation_status == "bounded_fetch_required"
    )
    snapshot_verification_required_count = sum(
        1 for task in tasks if task.remediation_status == "snapshot_verification_required"
    )
    production_score_total = _summary_int(fetch_manifest, "production_score_fixture_count") + sum(
        1 for row in rows if _optional_bool(row.get("production_score_fixture")) is True
    )
    if tasks:
        remediation_status = "replacement_fetch_remediation_required"
    elif rows:
        remediation_status = "replacement_fetch_remediation_not_required"
    else:
        remediation_status = "replacement_fetch_status_missing"
    audit = SourceBackedReplacementFetchFailureAudit(
        audit_id=_replacement_fetch_failure_audit_id(
            remediation_status=remediation_status,
            first_reason=first_reason,
            task_count=len(tasks),
        ),
        remediation_status=remediation_status,
        fetch_row_count=len(rows),
        remediation_task_count=len(tasks),
        fetch_failed_count=fetch_failed_count,
        fetch_not_attempted_count=fetch_not_attempted_count,
        current_text_available_count=current_text_available_count,
        text_snapshot_required_count=text_snapshot_required_count,
        bounded_fetch_required_count=bounded_fetch_required_count,
        snapshot_verification_required_count=snapshot_verification_required_count,
        production_score_fixture_total=production_score_total,
        first_blocking_reason=first_reason,
        reasons=tuple(reason for reason in (first_reason,) if reason),
    )
    return {
        "schema_version": "e2r_replacement_fetch_failure_audit_manifest_v1",
        "input_schema_versions": {
            "replacement_candidate_fetch_status": fetch_manifest.get("schema_version"),
        },
        "summary": {
            "remediation_status": audit.remediation_status,
            "fetch_row_count": audit.fetch_row_count,
            "remediation_task_count": audit.remediation_task_count,
            "fetch_failed_count": audit.fetch_failed_count,
            "fetch_not_attempted_count": audit.fetch_not_attempted_count,
            "current_text_available_count": audit.current_text_available_count,
            "text_snapshot_required_count": audit.text_snapshot_required_count,
            "bounded_fetch_required_count": audit.bounded_fetch_required_count,
            "snapshot_verification_required_count": audit.snapshot_verification_required_count,
            "production_score_fixture_total": audit.production_score_fixture_total,
            "first_blocking_reason": audit.first_blocking_reason,
        },
        "reason_groups": reason_groups,
        "tasks": [asdict(task) for task in sorted(tasks, key=lambda item: (item.priority, item.archetype_id, item.task_id))],
        "audit": asdict(audit),
    }


def replay_coverage_summary(coverage_rows: Sequence[ReplayCoverageRow]) -> Mapping[str, Any]:
    rows = list(coverage_rows)
    return {
        "contract_count": len(rows),
        "source_backed_candidate_archetype_count": sum(
            1 for row in rows if row.coverage_status == COVERAGE_AVAILABLE
        ),
        "source_gap_with_rows_archetype_count": sum(
            1 for row in rows if row.coverage_status == COVERAGE_GAP_WITH_ROWS
        ),
        "source_gap_no_rows_archetype_count": sum(
            1 for row in rows if row.coverage_status == COVERAGE_GAP_NO_ROWS
        ),
        "source_backed_candidate_row_count": sum(row.source_backed_candidate_count for row in rows),
        "source_proxy_or_pending_row_count": sum(row.source_proxy_or_pending_count for row in rows),
        "unverified_research_row_count": sum(row.unverified_research_row_count for row in rows),
    }


def replay_coverage_to_dict(coverage_rows: Sequence[ReplayCoverageRow]) -> Mapping[str, Any]:
    return {
        "summary": dict(replay_coverage_summary(coverage_rows)),
        "rows": [asdict(row) for row in coverage_rows],
    }


def iter_json_research_rows(paths: Iterable[str | Path]) -> Iterable[Mapping[str, Any]]:
    for raw_path in paths:
        path = Path(raw_path)
        if not path.exists() or path.is_dir():
            continue
        if path.suffix.lower() == ".jsonl":
            yield from _iter_jsonl_rows(path)
        elif path.suffix.lower() == ".json":
            yield from _iter_json_file_rows(path)
        elif path.suffix.lower() == ".md":
            yield from _iter_json_objects_from_markdown(path)


def _iter_jsonl_rows(path: Path) -> Iterable[Mapping[str, Any]]:
    with path.open(encoding="utf-8") as fh:
        for line_no, line in enumerate(fh, start=1):
            text = line.strip()
            if not text or not text.startswith("{"):
                continue
            try:
                row = json.loads(text)
            except json.JSONDecodeError:
                continue
            if isinstance(row, Mapping):
                yield _with_source_location(row, path=path, line_no=line_no)


def _iter_json_file_rows(path: Path) -> Iterable[Mapping[str, Any]]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return
    rows: Iterable[Any]
    if isinstance(payload, list):
        rows = payload
    elif isinstance(payload, Mapping):
        raw_rows = payload.get("rows") or payload.get("cases") or payload.get("records") or payload.get("data")
        rows = raw_rows if isinstance(raw_rows, list) else (payload,)
    else:
        rows = ()
    for row in rows:
        if isinstance(row, Mapping):
            yield _with_source_location(row, path=path, line_no=None)


def _iter_json_objects_from_markdown(path: Path) -> Iterable[Mapping[str, Any]]:
    with path.open(encoding="utf-8", errors="ignore") as fh:
        for line_no, line in enumerate(fh, start=1):
            text = line.strip()
            if not (text.startswith("{") and text.endswith("}")):
                continue
            try:
                row = json.loads(text)
            except json.JSONDecodeError:
                continue
            if isinstance(row, Mapping):
                yield _with_source_location(row, path=path, line_no=line_no)


def _with_source_location(row: Mapping[str, Any], *, path: Path, line_no: int | None) -> Mapping[str, Any]:
    result = dict(row)
    result.setdefault("_source_path", str(path))
    if line_no is not None:
        result.setdefault("_source_line", line_no)
    return result


def _row_archetype_id(
    row: Mapping[str, Any],
    *,
    contract_ids: Iterable[str] | None,
) -> str | None:
    contract_set = {normalise_canonical_archetype_id(item) for item in (contract_ids or ())}
    contract_set.discard(None)
    first_normalised: str | None = None
    for key in _ARCHETYPE_KEYS:
        canonical = normalise_canonical_archetype_id(row.get(key))
        if not canonical:
            continue
        if first_normalised is None:
            first_normalised = canonical
        if not contract_set or canonical in contract_set:
            return canonical
    return first_normalised


def _has_proxy_marker(row: Mapping[str, Any]) -> bool:
    for key in _SOURCE_TEXT_KEYS:
        for text in _iter_text_values(row.get(key)):
            lowered = text.lower()
            if any(marker in lowered for marker in _PROXY_MARKERS):
                return True
    return False


def _has_concrete_source_anchor(row: Mapping[str, Any]) -> bool:
    return bool(_source_anchors(row))


def _source_anchors(row: Mapping[str, Any]) -> tuple[str, ...]:
    anchors: list[str] = []
    for key in _SOURCE_TEXT_KEYS:
        for text in _iter_text_values(row.get(key)):
            anchors.extend(_extract_source_anchors(text))
    return tuple(dict.fromkeys(anchors))


def _extract_source_anchors(text: str) -> tuple[str, ...]:
    result: list[str] = []
    for match in re.finditer(r"(?:https?://|fixture://|dart://|kind://|xbrl://|api://)[^\s,;\)\]\}]+", text):
        clean = match.group(0).strip().strip(".,;")
        lowered = clean.lower()
        if any(lowered.startswith(prefix) for prefix in _SOURCE_ANCHOR_PREFIXES):
            result.append(clean)
    return tuple(dict.fromkeys(result))


def _replay_candidate_from_row(
    row: Mapping[str, Any],
    *,
    archetype_id: str,
    anchors: tuple[str, ...],
    classification_reasons: Sequence[str],
) -> SourceBackedReplayCandidate:
    fingerprint = _row_fingerprint(row)
    digest = hashlib.sha256(
        "\n".join((archetype_id, fingerprint, "\n".join(anchors))).encode("utf-8")
    ).hexdigest()[:20]
    return SourceBackedReplayCandidate(
        archetype_id=archetype_id,
        candidate_id=f"RPLAY-{digest}",
        row_fingerprint=fingerprint,
        source_anchors=anchors,
        source_path=_optional_text(row.get("_source_path")),
        source_line=_optional_int(row.get("_source_line")),
        case_id=_optional_text(row.get("case_id") or row.get("source_case_id")),
        trigger_id=_optional_text(row.get("trigger_id") or row.get("source_trigger_id")),
        symbol=_optional_text(row.get("symbol")),
        company_name=_optional_text(row.get("company_name")),
        fine_archetype_id=_optional_text(row.get("fine_archetype_id") or row.get("source_fine_archetype_id")),
        trigger_date=_optional_text(row.get("trigger_date")),
        entry_date=_optional_text(row.get("entry_date")),
        stage_label_before=_optional_text(row.get("stage_label_before") or row.get("source_trigger_type")),
        stage_label_after=_optional_text(row.get("stage_label_after")),
        selection_reasons=tuple(dict.fromkeys(("concrete_source_anchor", *classification_reasons))),
    )


def _candidate_sort_key(row: Mapping[str, Any], candidate: SourceBackedReplayCandidate) -> tuple[Any, ...]:
    representative = (
        _optional_bool(row.get("is_aggregate_representative")) is True
        or str(row.get("aggregate_group_role") or "").strip().lower() == "representative"
    )
    has_case_id = bool(candidate.case_id)
    has_company = bool(candidate.company_name or candidate.symbol)
    return (
        0 if representative else 1,
        0 if has_case_id else 1,
        0 if has_company else 1,
        candidate.trigger_date or candidate.entry_date or "",
        candidate.source_path or "",
        candidate.source_line or 0,
        candidate.candidate_id,
    )


def _dedupe_replay_candidates(candidates: Sequence[SourceBackedReplayCandidate]) -> tuple[SourceBackedReplayCandidate, ...]:
    selected: list[SourceBackedReplayCandidate] = []
    seen: set[tuple[str, str, tuple[str, ...]]] = set()
    for candidate in candidates:
        source_identity = candidate.case_id or candidate.trigger_id or candidate.row_fingerprint
        key = (candidate.archetype_id, source_identity, candidate.source_anchors)
        if key in seen:
            continue
        seen.add(key)
        selected.append(candidate)
    return tuple(selected)


def _fixture_seeds_from_candidate(candidate: Mapping[str, Any]) -> tuple[SourceBackedReplayFixtureSeed, ...]:
    candidate_id = _optional_text(candidate.get("candidate_id"))
    archetype_id = _optional_text(candidate.get("archetype_id"))
    if not candidate_id or not archetype_id:
        return ()
    source_anchors = tuple(_iter_text_values(candidate.get("source_anchors")))
    as_of_date = _candidate_as_of_date(candidate)
    snapshot_status = "pending_source_snapshot" if as_of_date else "missing_as_of_date"
    result: list[SourceBackedReplayFixtureSeed] = []
    for source_anchor in source_anchors:
        digest = hashlib.sha256(
            "\n".join((archetype_id, candidate_id, source_anchor, as_of_date or "")).encode("utf-8")
        ).hexdigest()[:20]
        result.append(
            SourceBackedReplayFixtureSeed(
                archetype_id=archetype_id,
                candidate_id=candidate_id,
                fixture_seed_id=f"FSEED-{digest}",
                source_anchor=source_anchor,
                as_of_date=as_of_date,
                snapshot_status=snapshot_status,
                snapshot_request_ready=bool(as_of_date),
                source_path=_optional_text(candidate.get("source_path")),
                source_line=_optional_int(candidate.get("source_line")),
                case_id=_optional_text(candidate.get("case_id")),
                trigger_id=_optional_text(candidate.get("trigger_id")),
                symbol=_optional_text(candidate.get("symbol")),
                company_name=_optional_text(candidate.get("company_name")),
                trigger_date=_optional_text(candidate.get("trigger_date")),
                entry_date=_optional_text(candidate.get("entry_date")),
            )
        )
    return tuple(result)


def _candidate_as_of_date(candidate: Mapping[str, Any]) -> str | None:
    for key in ("trigger_date", "entry_date"):
        text = _optional_text(candidate.get(key))
        if text and re.fullmatch(r"\d{4}-\d{2}-\d{2}", text):
            return text
    return None


def _snapshot_rows_by_url(snapshot_rows: Iterable[Mapping[str, Any]]) -> Mapping[str, tuple[Mapping[str, Any], ...]]:
    result: dict[str, list[Mapping[str, Any]]] = {}
    for row in snapshot_rows:
        url = _normalise_url(_optional_text(row.get("url")))
        if not url:
            continue
        result.setdefault(url, []).append(dict(row))
    return {url: tuple(rows) for url, rows in result.items()}


def _snapshot_availability_for_seed(
    seed: Mapping[str, Any],
    *,
    snapshots_by_url: Mapping[str, tuple[Mapping[str, Any], ...]],
) -> SourceBackedSnapshotAvailability:
    fixture_seed_id = _optional_text(seed.get("fixture_seed_id")) or ""
    candidate_id = _optional_text(seed.get("candidate_id")) or ""
    archetype_id = _optional_text(seed.get("archetype_id")) or ""
    source_anchor = _optional_text(seed.get("source_anchor")) or ""
    seed_as_of_date = _optional_text(seed.get("as_of_date"))

    if not _optional_bool(seed.get("snapshot_request_ready")):
        return SourceBackedSnapshotAvailability(
            fixture_seed_id=fixture_seed_id,
            candidate_id=candidate_id,
            archetype_id=archetype_id,
            source_anchor=source_anchor,
            as_of_date=seed_as_of_date,
            snapshot_status="not_snapshot_request_ready",
            reasons=("seed_snapshot_request_not_ready",),
        )

    candidates = snapshots_by_url.get(_normalise_url(source_anchor) or "", ())
    if not candidates:
        return SourceBackedSnapshotAvailability(
            fixture_seed_id=fixture_seed_id,
            candidate_id=candidate_id,
            archetype_id=archetype_id,
            source_anchor=source_anchor,
            as_of_date=seed_as_of_date,
            snapshot_status="no_local_snapshot",
            reasons=("no_exact_url_snapshot_in_local_store",),
        )

    ordered = sorted(candidates, key=lambda item: str(item.get("as_of_date") or "9999-99-99"))
    for snapshot in ordered:
        snapshot_as_of = _optional_text(snapshot.get("as_of_date"))
        if seed_as_of_date and snapshot_as_of and snapshot_as_of > seed_as_of_date:
            continue
        text_path = _optional_text(snapshot.get("extracted_text_path"))
        if not text_path:
            return _availability_from_snapshot(
                seed,
                snapshot,
                status="local_snapshot_text_missing",
                reasons=("snapshot_has_no_extracted_text_path",),
            )
        if not Path(text_path).is_absolute():
            text_path = str(Path("data/report_snapshots") / text_path)
        if not Path(text_path).exists():
            return _availability_from_snapshot(
                seed,
                snapshot,
                status="local_snapshot_text_missing",
                reasons=("snapshot_text_path_missing",),
                extracted_text_path=text_path,
            )
        return _availability_from_snapshot(
            seed,
            snapshot,
            status="local_text_snapshot_ready",
            reasons=("exact_url_snapshot_text_available",),
            extracted_text_path=text_path,
            evidence_document_fixture_ready=True,
        )

    return _availability_from_snapshot(
        seed,
        ordered[0],
        status="future_snapshot_not_allowed",
        reasons=("snapshot_as_of_date_after_seed_as_of_date",),
    )


def _availability_from_snapshot(
    seed: Mapping[str, Any],
    snapshot: Mapping[str, Any],
    *,
    status: str,
    reasons: Sequence[str],
    extracted_text_path: str | None = None,
    evidence_document_fixture_ready: bool = False,
) -> SourceBackedSnapshotAvailability:
    return SourceBackedSnapshotAvailability(
        fixture_seed_id=_optional_text(seed.get("fixture_seed_id")) or "",
        candidate_id=_optional_text(seed.get("candidate_id")) or "",
        archetype_id=_optional_text(seed.get("archetype_id")) or "",
        source_anchor=_optional_text(seed.get("source_anchor")) or "",
        as_of_date=_optional_text(seed.get("as_of_date")),
        snapshot_status=status,
        snapshot_url=_optional_text(snapshot.get("url")),
        snapshot_as_of_date=_optional_text(snapshot.get("as_of_date")),
        snapshot_source_type=_optional_text(snapshot.get("source_type")),
        snapshot_title=_optional_text(snapshot.get("title")),
        extracted_text_path=extracted_text_path or _optional_text(snapshot.get("extracted_text_path")),
        extracted_text_hash=_optional_text(snapshot.get("extracted_text_hash")),
        evidence_document_fixture_ready=evidence_document_fixture_ready,
        production_score_fixture=False,
        reasons=tuple(dict.fromkeys(reasons)),
    )


def _normalise_url(url: str | None) -> str | None:
    if not url:
        return None
    parts = parse.urlsplit(url.strip())
    if not parts.scheme or not parts.netloc:
        return url.strip()
    scheme = parts.scheme.lower()
    netloc = parts.netloc.lower()
    path = parts.path or "/"
    query = parts.query
    return parse.urlunsplit((scheme, netloc, path, query, ""))


def _current_fetch_status_for_seed(
    seed: Mapping[str, Any],
    *,
    fetch_by_seed: Mapping[str, Mapping[str, Any]],
) -> SourceBackedCurrentFetchStatus:
    fixture_seed_id = _optional_text(seed.get("fixture_seed_id")) or ""
    candidate_id = _optional_text(seed.get("candidate_id")) or ""
    archetype_id = _optional_text(seed.get("archetype_id")) or ""
    source_anchor = _optional_text(seed.get("source_anchor")) or ""
    seed_as_of_date = _optional_text(seed.get("as_of_date"))
    if not _optional_bool(seed.get("snapshot_request_ready")):
        return SourceBackedCurrentFetchStatus(
            fixture_seed_id=fixture_seed_id,
            candidate_id=candidate_id,
            archetype_id=archetype_id,
            source_anchor=source_anchor,
            as_of_date=seed_as_of_date,
            current_fetch_status="not_snapshot_request_ready",
            reason="seed_snapshot_request_not_ready",
            reasons=("seed_snapshot_request_not_ready",),
        )

    fetch_row = fetch_by_seed.get(fixture_seed_id)
    if not fetch_row:
        return SourceBackedCurrentFetchStatus(
            fixture_seed_id=fixture_seed_id,
            candidate_id=candidate_id,
            archetype_id=archetype_id,
            source_anchor=source_anchor,
            as_of_date=seed_as_of_date,
            current_fetch_status="current_fetch_not_attempted",
            reasons=("no_current_fetch_attempt_for_seed",),
        )

    ok = _optional_bool(fetch_row.get("ok"))
    text_path = _optional_text(fetch_row.get("current_text_path") or fetch_row.get("text_path"))
    text_hash = _optional_text(fetch_row.get("current_text_hash") or fetch_row.get("text_hash"))
    text_chars = _optional_int(fetch_row.get("current_text_chars") or fetch_row.get("text_chars")) or 0
    if ok is True and text_path and text_hash and text_chars > 0:
        return SourceBackedCurrentFetchStatus(
            fixture_seed_id=fixture_seed_id,
            candidate_id=candidate_id,
            archetype_id=archetype_id,
            source_anchor=source_anchor,
            as_of_date=seed_as_of_date,
            current_fetch_status="current_fetch_text_available_asof_unverified",
            fetched_at=_optional_text(fetch_row.get("fetched_at")),
            content_type=_optional_text(fetch_row.get("content_type")),
            current_text_path=text_path,
            current_text_hash=text_hash,
            current_text_chars=text_chars,
            asof_snapshot_verified=False,
            evidence_document_fixture_ready=False,
            production_score_fixture=False,
            reasons=("current_fetch_is_not_asof_verified",),
        )

    return SourceBackedCurrentFetchStatus(
        fixture_seed_id=fixture_seed_id,
        candidate_id=candidate_id,
        archetype_id=archetype_id,
        source_anchor=source_anchor,
        as_of_date=seed_as_of_date,
        current_fetch_status="current_fetch_failed",
        fetched_at=_optional_text(fetch_row.get("fetched_at")),
        content_type=_optional_text(fetch_row.get("content_type")),
        reason=_optional_text(fetch_row.get("reason")) or "current_fetch_failed",
        reasons=("current_fetch_failed",),
    )


def _remediation_task_for_current_fetch_row(row: Mapping[str, Any]) -> SourceBackedSnapshotRemediationTask:
    fixture_seed_id = _optional_text(row.get("fixture_seed_id")) or ""
    archetype_id = _optional_text(row.get("archetype_id")) or ""
    source_anchor = _optional_text(row.get("source_anchor")) or ""
    input_status = _optional_text(row.get("current_fetch_status")) or "unknown_current_fetch_status"
    remediation_type, priority, actions, reasons = _remediation_classification(row)
    digest = hashlib.sha256(
        "\n".join((fixture_seed_id, input_status, remediation_type, source_anchor)).encode("utf-8")
    ).hexdigest()[:20]
    return SourceBackedSnapshotRemediationTask(
        task_id=f"SREMED-{digest}",
        fixture_seed_id=fixture_seed_id,
        candidate_id=_optional_text(row.get("candidate_id")) or "",
        archetype_id=archetype_id,
        source_anchor=source_anchor,
        as_of_date=_optional_text(row.get("as_of_date")),
        input_status=input_status,
        remediation_type=remediation_type,
        priority=priority,
        target_state="asof_text_snapshot_verified",
        score_blocked_until_resolved=True,
        suggested_actions=actions,
        reasons=reasons,
    )


def _remediation_classification(row: Mapping[str, Any]) -> tuple[str, int, tuple[str, ...], tuple[str, ...]]:
    status = _optional_text(row.get("current_fetch_status")) or ""
    reason = (_optional_text(row.get("reason")) or "").lower()
    source_anchor = (_optional_text(row.get("source_anchor")) or "").lower()
    if status == "current_fetch_text_available_asof_unverified":
        return (
            "verify_current_text_asof_identity",
            10,
            (
                "verify_published_or_available_date_against_seed_as_of_date",
                "verify_current_text_matches_source_identity_and_target_article",
                "promote_to_asof_snapshot_only_after_source_date_or_archive_verification",
            ),
            ("current_text_available_but_asof_unverified",),
        )
    if status == "current_fetch_not_attempted":
        return (
            "fetch_current_text",
            20,
            ("attempt_bounded_current_fetch",),
            ("fetch_not_attempted",),
        )
    if status == "not_snapshot_request_ready":
        return (
            "seed_metadata_repair",
            5,
            ("repair_seed_as_of_date_or_source_anchor",),
            ("seed_snapshot_request_not_ready",),
        )
    if "pdf_text_extraction_failed" in reason or "pdf text extraction" in reason:
        return (
            "pdf_parser_repair",
            25,
            (
                "retry_pdf_extraction_with_alternative_parser",
                "download_pdf_binary_snapshot_before_text_extraction",
                "use_manual_text_fixture_only_if_source_hash_is_recorded",
            ),
            ("current_fetch_pdf_text_extraction_failed",),
        )
    if "404" in reason or "not found" in reason:
        return (
            "dead_url_replacement",
            30,
            (
                "look_up_archived_copy_or_original_source",
                "find_same_event_official_or_tier1_source_before_seed_as_of_date",
            ),
            ("current_fetch_dead_url",),
        )
    if "401" in reason or "403" in reason or "forbidden" in reason or "reuters.com" in source_anchor:
        return (
            "archive_or_alternative_source",
            30,
            (
                "look_up_archive_or_licensed_snapshot",
                "replace_with_official_or_independent_source_for_same_event",
                "do_not_use_current_error_page_as_evidence",
            ),
            ("current_fetch_access_blocked_or_paywalled",),
        )
    if any(marker in reason for marker in ("timeout", "remote end closed", "connection reset", "certificate_verify_failed", "ssl")):
        return (
            "retry_current_fetch_with_browser_or_tls_repair",
            35,
            (
                "retry_with_browser_fetch_or_tls_repair_with_same_bounded_budget",
                "if_retry_fails_find_archive_or_alternative_source",
            ),
            ("current_fetch_transport_failure",),
        )
    return (
        "archive_or_alternative_source",
        40,
        (
            "inspect_fetch_failure_reason",
            "find_archive_or_alternative_source_for_same_event",
        ),
        ("current_fetch_failed_unknown_reason",),
    )


def _current_text_asof_precheck_for_row(
    row: Mapping[str, Any],
    *,
    max_text_chars: int,
) -> SourceBackedCurrentTextAsofPrecheck:
    fixture_seed_id = _optional_text(row.get("fixture_seed_id")) or ""
    candidate_id = _optional_text(row.get("candidate_id")) or ""
    archetype_id = _optional_text(row.get("archetype_id")) or ""
    source_anchor = _optional_text(row.get("source_anchor")) or ""
    as_of_text = _optional_text(row.get("as_of_date"))
    current_text_path = _optional_text(row.get("current_text_path"))
    if row.get("current_fetch_status") != "current_fetch_text_available_asof_unverified":
        return SourceBackedCurrentTextAsofPrecheck(
            fixture_seed_id=fixture_seed_id,
            candidate_id=candidate_id,
            archetype_id=archetype_id,
            source_anchor=source_anchor,
            as_of_date=as_of_text,
            current_text_path=current_text_path,
            precheck_status="current_text_unavailable",
            reasons=("current_fetch_text_not_available",),
        )
    if not current_text_path or not Path(current_text_path).exists():
        return SourceBackedCurrentTextAsofPrecheck(
            fixture_seed_id=fixture_seed_id,
            candidate_id=candidate_id,
            archetype_id=archetype_id,
            source_anchor=source_anchor,
            as_of_date=as_of_text,
            current_text_path=current_text_path,
            precheck_status="current_text_file_missing",
            reasons=("current_text_path_missing",),
        )
    try:
        as_of = date.fromisoformat(as_of_text or "")
    except ValueError:
        return SourceBackedCurrentTextAsofPrecheck(
            fixture_seed_id=fixture_seed_id,
            candidate_id=candidate_id,
            archetype_id=archetype_id,
            source_anchor=source_anchor,
            as_of_date=as_of_text,
            current_text_path=current_text_path,
            precheck_status="current_text_unavailable",
            reasons=("invalid_as_of_date",),
        )
    text = Path(current_text_path).read_text(encoding="utf-8", errors="ignore")[:max(0, max_text_chars)]
    date_hints = _date_hints_from_text_and_url(text=text, source_anchor=source_anchor)
    parsed_hints = tuple(date.fromisoformat(item) for item in date_hints)
    if not parsed_hints:
        return SourceBackedCurrentTextAsofPrecheck(
            fixture_seed_id=fixture_seed_id,
            candidate_id=candidate_id,
            archetype_id=archetype_id,
            source_anchor=source_anchor,
            as_of_date=as_of_text,
            current_text_path=current_text_path,
            precheck_status="no_date_hint",
            date_hints=date_hints,
            reasons=("no_parseable_date_hint_in_url_or_current_text",),
        )
    if any(item > as_of for item in parsed_hints):
        return SourceBackedCurrentTextAsofPrecheck(
            fixture_seed_id=fixture_seed_id,
            candidate_id=candidate_id,
            archetype_id=archetype_id,
            source_anchor=source_anchor,
            as_of_date=as_of_text,
            current_text_path=current_text_path,
            precheck_status="future_date_hint_blocks",
            date_hints=date_hints,
            reasons=("date_hint_after_seed_as_of_date",),
        )
    return SourceBackedCurrentTextAsofPrecheck(
        fixture_seed_id=fixture_seed_id,
        candidate_id=candidate_id,
        archetype_id=archetype_id,
        source_anchor=source_anchor,
        as_of_date=as_of_text,
        current_text_path=current_text_path,
        precheck_status="date_hint_on_or_before_asof",
        date_hints=date_hints,
        asof_precheck_candidate=True,
        reasons=("date_hint_on_or_before_asof_but_archive_unverified",),
    )


def _evidence_document_fixture_for_snapshot_row(
    row: Mapping[str, Any],
    *,
    anchor_max_chars: int,
) -> SourceBackedEvidenceDocumentFixture:
    base_kwargs = {
        "fixture_seed_id": _optional_text(row.get("fixture_seed_id")) or "",
        "candidate_id": _optional_text(row.get("candidate_id")) or "",
        "archetype_id": _optional_text(row.get("archetype_id")) or "",
        "source_anchor": _optional_text(row.get("source_anchor")) or "",
        "as_of_date": _optional_text(row.get("as_of_date")),
        "snapshot_as_of_date": _optional_text(row.get("snapshot_as_of_date")),
        "extracted_text_path": _optional_text(row.get("extracted_text_path")),
    }
    snapshot_ready = row.get("snapshot_status") == "local_text_snapshot_ready" or row.get(
        "verification_status"
    ) == "asof_text_snapshot_verified"
    if not snapshot_ready or not _optional_bool(row.get("evidence_document_fixture_ready")):
        return SourceBackedEvidenceDocumentFixture(
            **base_kwargs,
            fixture_status="source_snapshot_not_ready",
            reasons=("local_text_snapshot_not_ready",),
        )

    text_path = _optional_text(row.get("extracted_text_path"))
    if not text_path or not Path(text_path).exists():
        return SourceBackedEvidenceDocumentFixture(
            **base_kwargs,
            fixture_status="snapshot_text_missing",
            reasons=("snapshot_text_path_missing",),
        )
    snapshot_date_text = _optional_text(row.get("snapshot_as_of_date")) or _optional_text(row.get("as_of_date"))
    snapshot_date = _parse_iso_date(snapshot_date_text)
    if snapshot_date is None:
        return SourceBackedEvidenceDocumentFixture(
            **base_kwargs,
            fixture_status="invalid_snapshot_date",
            reasons=("snapshot_as_of_date_required",),
        )
    text = Path(text_path).read_text(encoding="utf-8", errors="ignore")
    anchor_text = _fixture_anchor_text(text, max_chars=anchor_max_chars)
    if not anchor_text:
        return SourceBackedEvidenceDocumentFixture(
            **base_kwargs,
            fixture_status="empty_snapshot_text",
            reasons=("snapshot_text_empty",),
        )

    expected_hash = _optional_text(row.get("extracted_text_hash"))
    actual_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
    if _looks_like_sha256(expected_hash) and expected_hash != actual_hash:
        return SourceBackedEvidenceDocumentFixture(
            **base_kwargs,
            fixture_status="content_hash_mismatch",
            content_hash=actual_hash,
            reasons=("snapshot_text_hash_mismatch",),
        )

    canonical_url = _optional_text(row.get("snapshot_url")) or _optional_text(row.get("source_anchor"))
    document = EvidenceDocument.from_text(
        text=text,
        canonical_url=canonical_url,
        source_type=_source_type_from_snapshot_row(row),
        source_name=_source_name_from_snapshot_row(row),
        published_at=snapshot_date,
        available_at=snapshot_date,
        revision_id=_snapshot_revision_id(row),
        parser_version="source_snapshot_fixture_v1",
        source_lineage_id=_source_lineage_id(canonical_url),
        source_proxy_only=False,
        score_block_reasons=("claim_replay_pending",),
    )
    anchor = EvidenceAnchor.text_span(document=document, document_text=text, exact_text=anchor_text)
    if not anchor.anchor_verified:
        return SourceBackedEvidenceDocumentFixture(
            **base_kwargs,
            fixture_status="anchor_verification_failed",
            document_id=document.document_id,
            content_hash=document.content_hash,
            reasons=("fixture_anchor_not_verified_against_document_text",),
        )

    reasons = ["local_text_snapshot_promoted_to_evidence_document_fixture"]
    if expected_hash and not _looks_like_sha256(expected_hash):
        reasons.append("snapshot_hash_label_replaced_by_computed_content_hash")
    return SourceBackedEvidenceDocumentFixture(
        **base_kwargs,
        fixture_status="evidence_document_fixture_ready_score_blocked_claim_replay_pending",
        document_id=document.document_id,
        anchor_id=anchor.anchor_id,
        canonical_url=document.canonical_url,
        source_type=document.source_type.value,
        source_name=document.source_name,
        source_lineage_id=document.source_lineage_id,
        content_hash=document.content_hash,
        anchor_locator=anchor.locator,
        anchor_verified=anchor.anchor_verified,
        evidence_document_fixture_ready=True,
        claim_replay_ready=False,
        production_score_fixture=False,
        score_block_reasons=document.score_block_reasons,
        reasons=tuple(reasons),
    )


def _replacement_evidence_document_fixture_for_snapshot_row(
    row: Mapping[str, Any],
    *,
    anchor_max_chars: int,
) -> SourceBackedReplacementEvidenceDocumentFixture:
    base_kwargs = {
        "task_id": _optional_text(row.get("task_id")) or "",
        "replacement_candidate_id": _optional_text(row.get("replacement_candidate_id")) or "",
        "request_id": _optional_text(row.get("request_id")) or "",
        "fixture_seed_id": _optional_text(row.get("fixture_seed_id")) or "",
        "candidate_id": _optional_text(row.get("candidate_id")) or "",
        "archetype_id": _optional_text(row.get("archetype_id")) or "",
        "original_source_anchor": _optional_text(row.get("original_source_anchor")) or "",
        "candidate_url": _optional_text(row.get("candidate_url")) or "",
        "as_of_date": _optional_text(row.get("as_of_date")),
        "snapshot_as_of_date": _optional_text(row.get("snapshot_as_of_date")),
        "extracted_text_path": _optional_text(row.get("extracted_text_path")),
    }
    if row.get("verification_status") != "replacement_snapshot_verified" or not _optional_bool(
        row.get("evidence_document_fixture_ready")
    ):
        reasons = tuple(str(item) for item in (row.get("reasons") or ()) if str(item).strip())
        return SourceBackedReplacementEvidenceDocumentFixture(
            **base_kwargs,
            fixture_status="replacement_snapshot_not_verified",
            reasons=reasons or ("replacement_snapshot_not_verified",),
        )

    text_path = _optional_text(row.get("extracted_text_path"))
    if not text_path or not Path(text_path).exists():
        return SourceBackedReplacementEvidenceDocumentFixture(
            **base_kwargs,
            fixture_status="snapshot_text_missing",
            reasons=("replacement_snapshot_text_path_missing",),
        )
    snapshot_date = _parse_iso_date(_optional_text(row.get("snapshot_as_of_date")) or _optional_text(row.get("as_of_date")))
    if snapshot_date is None:
        return SourceBackedReplacementEvidenceDocumentFixture(
            **base_kwargs,
            fixture_status="invalid_snapshot_date",
            reasons=("snapshot_as_of_date_required",),
        )
    text = Path(text_path).read_text(encoding="utf-8", errors="ignore")
    anchor_text = _fixture_anchor_text(text, max_chars=anchor_max_chars)
    if not anchor_text:
        return SourceBackedReplacementEvidenceDocumentFixture(
            **base_kwargs,
            fixture_status="empty_snapshot_text",
            reasons=("replacement_snapshot_text_empty",),
        )

    expected_hash = _optional_text(row.get("extracted_text_hash"))
    actual_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
    if _looks_like_sha256(expected_hash) and expected_hash != actual_hash:
        return SourceBackedReplacementEvidenceDocumentFixture(
            **base_kwargs,
            fixture_status="content_hash_mismatch",
            content_hash=actual_hash,
            reasons=("replacement_snapshot_text_hash_mismatch",),
        )

    canonical_url = _optional_text(row.get("snapshot_url")) or _optional_text(row.get("candidate_url"))
    document = EvidenceDocument.from_text(
        text=text,
        canonical_url=canonical_url,
        source_type=_source_type_from_snapshot_row(row),
        source_name=_source_name_from_snapshot_row(row),
        published_at=snapshot_date,
        available_at=snapshot_date,
        revision_id=_snapshot_revision_id(row),
        parser_version="replacement_source_snapshot_fixture_v1",
        source_lineage_id=_source_lineage_id(canonical_url),
        source_proxy_only=False,
        score_block_reasons=("claim_replay_pending",),
    )
    anchor = EvidenceAnchor.text_span(document=document, document_text=text, exact_text=anchor_text)
    if not anchor.anchor_verified:
        return SourceBackedReplacementEvidenceDocumentFixture(
            **base_kwargs,
            fixture_status="anchor_verification_failed",
            document_id=document.document_id,
            content_hash=document.content_hash,
            reasons=("replacement_fixture_anchor_not_verified_against_document_text",),
        )

    reasons = ["replacement_snapshot_promoted_to_evidence_document_fixture"]
    if expected_hash and not _looks_like_sha256(expected_hash):
        reasons.append("replacement_snapshot_hash_label_replaced_by_computed_content_hash")
    return SourceBackedReplacementEvidenceDocumentFixture(
        **base_kwargs,
        fixture_status="evidence_document_fixture_ready_score_blocked_claim_replay_pending",
        document_id=document.document_id,
        anchor_id=anchor.anchor_id,
        canonical_url=document.canonical_url,
        source_type=document.source_type.value,
        source_name=document.source_name,
        content_hash=document.content_hash,
        anchor_locator=anchor.locator,
        anchor_verified=anchor.anchor_verified,
        evidence_document_fixture_ready=True,
        claim_replay_ready=False,
        production_score_fixture=False,
        score_block_reasons=document.score_block_reasons,
        reasons=tuple(reasons),
    )


def _claim_replay_task_for_fixture_row(
    row: Mapping[str, Any],
    *,
    fixture_kind: str,
    target_identity_by_candidate_id: Mapping[str, Mapping[str, Any]],
    target_identity_by_fixture_seed_id: Mapping[str, Mapping[str, Any]],
) -> tuple[SourceBackedClaimReplayTask | None, Mapping[str, Any]]:
    if not _optional_bool(row.get("evidence_document_fixture_ready")) or not _optional_bool(row.get("anchor_verified")):
        return None, _claim_replay_skip_row(
            row,
            fixture_kind=fixture_kind,
            skip_reason="evidence_document_fixture_not_ready",
        )

    text_path = _optional_text(row.get("extracted_text_path"))
    if not text_path or not Path(text_path).exists():
        return None, _claim_replay_skip_row(row, fixture_kind=fixture_kind, skip_reason="fixture_text_missing")
    text = Path(text_path).read_text(encoding="utf-8", errors="ignore")
    actual_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
    content_hash = _optional_text(row.get("content_hash"))
    if _looks_like_sha256(content_hash) and content_hash != actual_hash:
        return None, _claim_replay_skip_row(
            row,
            fixture_kind=fixture_kind,
            skip_reason="fixture_text_hash_mismatch",
        )
    document_id = _optional_text(row.get("document_id"))
    anchor_id = _optional_text(row.get("anchor_id"))
    if not document_id or not anchor_id or not content_hash:
        return None, _claim_replay_skip_row(
            row,
            fixture_kind=fixture_kind,
            skip_reason="fixture_document_anchor_missing",
        )
    identity = _target_identity_for_fixture_row(
        row,
        target_identity_by_candidate_id=target_identity_by_candidate_id,
        target_identity_by_fixture_seed_id=target_identity_by_fixture_seed_id,
    )
    if identity is None:
        return None, _claim_replay_skip_row(row, fixture_kind=fixture_kind, skip_reason="target_identity_missing")

    archetype_id = _optional_text(row.get("archetype_id")) or ""
    fixture_seed_id = _optional_text(row.get("fixture_seed_id")) or ""
    task_id = "CLREPLAY-" + hashlib.sha1(
        "|".join((fixture_kind, archetype_id, fixture_seed_id, document_id, anchor_id, content_hash)).encode(
            "utf-8"
        )
    ).hexdigest()[:20]
    return SourceBackedClaimReplayTask(
        task_id=task_id,
        fixture_kind=fixture_kind,
        fixture_seed_id=fixture_seed_id,
        candidate_id=_optional_text(row.get("candidate_id")) or "",
        archetype_id=archetype_id,
        target_entity_id=identity[0],
        target_names=identity[1],
        as_of_date=_optional_text(row.get("as_of_date")),
        document_id=document_id,
        anchor_id=anchor_id,
        canonical_url=_optional_text(row.get("canonical_url")),
        source_type=_optional_text(row.get("source_type")),
        source_name=_optional_text(row.get("source_name")),
        source_lineage_id=_optional_text(row.get("source_lineage_id")),
        content_hash=content_hash,
        extracted_text_path=text_path,
        anchor_locator=_optional_text(row.get("anchor_locator")),
        document_published_at=_optional_text(row.get("snapshot_as_of_date") or row.get("published_at")),
        replacement_candidate_id=_optional_text(row.get("replacement_candidate_id")),
        original_source_anchor=_optional_text(row.get("original_source_anchor")),
        candidate_url=_optional_text(row.get("candidate_url")),
    ), {}


def _claim_replay_skip_row(
    row: Mapping[str, Any],
    *,
    fixture_kind: str,
    skip_reason: str,
    duplicate_task_id: str | None = None,
) -> Mapping[str, Any]:
    result: dict[str, Any] = {
        "fixture_kind": fixture_kind,
        "fixture_seed_id": _optional_text(row.get("fixture_seed_id")) or "",
        "candidate_id": _optional_text(row.get("candidate_id")) or "",
        "archetype_id": _optional_text(row.get("archetype_id")) or "",
        "document_id": _optional_text(row.get("document_id")),
        "anchor_id": _optional_text(row.get("anchor_id")),
        "fixture_status": _optional_text(row.get("fixture_status")),
        "skip_reason": skip_reason,
        "production_score_fixture": False,
    }
    replacement_candidate_id = _optional_text(row.get("replacement_candidate_id"))
    if replacement_candidate_id:
        result["replacement_candidate_id"] = replacement_candidate_id
    if duplicate_task_id:
        result["duplicate_task_id"] = duplicate_task_id
    return result


def _target_identity_for_fixture_row(
    row: Mapping[str, Any],
    *,
    target_identity_by_candidate_id: Mapping[str, Mapping[str, Any]],
    target_identity_by_fixture_seed_id: Mapping[str, Mapping[str, Any]],
) -> tuple[str, tuple[str, ...]] | None:
    identity_sources = (
        row,
        target_identity_by_candidate_id.get(_optional_text(row.get("candidate_id")) or "") or {},
        target_identity_by_fixture_seed_id.get(_optional_text(row.get("fixture_seed_id")) or "") or {},
    )
    for identity in identity_sources:
        target_entity_id = _optional_text(
            identity.get("target_entity_id")
            or identity.get("entity_id")
            or identity.get("corp_code")
            or identity.get("symbol")
        )
        target_names = _target_names_from_identity(identity)
        if target_entity_id and target_names:
            return target_entity_id, target_names
    return None


def _target_names_from_identity(identity: Mapping[str, Any]) -> tuple[str, ...]:
    raw_names = identity.get("target_names")
    names: list[str] = []
    if isinstance(raw_names, str):
        names.extend(part.strip() for part in re.split(r"[,|]", raw_names) if part.strip())
    elif isinstance(raw_names, Sequence) and not isinstance(raw_names, (bytes, bytearray)):
        names.extend(str(item).strip() for item in raw_names if str(item).strip())
    for key in ("company_name", "target_company_name", "issuer_name", "symbol"):
        value = _optional_text(identity.get(key))
        if value:
            names.append(value)
    return tuple(dict.fromkeys(names))


def _claim_replay_result_for_task(
    task: Mapping[str, Any],
    extraction_row: Mapping[str, Any] | None,
) -> SourceBackedClaimReplayResult:
    base = _claim_replay_result_base(task)
    if extraction_row is None:
        return SourceBackedClaimReplayResult(
            **base,
            replay_status="claim_replay_not_attempted",
            blocked_reason="extraction_result_missing",
            reasons=("claim_replay_extraction_result_missing",),
        )
    if _optional_bool(extraction_row.get("ok")) is False:
        reason = _optional_text(extraction_row.get("reason")) or "claim_replay_provider_error"
        return SourceBackedClaimReplayResult(
            **base,
            replay_status="provider_error",
            blocked_reason=reason,
            extraction_status="provider_error",
            reasons=(reason,),
        )
    payload = extraction_row.get("output")
    if not isinstance(payload, Mapping):
        payload = _claim_extraction_payload_from_flat_row(extraction_row)
    try:
        output = decode_claim_extraction_output(payload)
    except Exception as exc:
        return SourceBackedClaimReplayResult(
            **base,
            replay_status="invalid_provider_output",
            blocked_reason=str(exc)[:180],
            extraction_status="invalid_provider_output",
            reasons=("claim_replay_output_decode_failed",),
        )
    if output.status in {"provider_error", "invalid_provider_output"}:
        return SourceBackedClaimReplayResult(
            **base,
            replay_status=output.status,
            blocked_reason=output.blocked_reason or output.status,
            extraction_status=output.status,
            reasons=(output.blocked_reason or output.status,),
        )
    expected_anchor_id = _optional_text(task.get("anchor_id")) or ""
    mismatched = tuple(raw.raw_assertion_id for raw in output.raw_assertions if raw.anchor_id != expected_anchor_id)
    if mismatched:
        return SourceBackedClaimReplayResult(
            **base,
            replay_status="raw_assertion_anchor_mismatch",
            raw_assertion_count=len(output.raw_assertions),
            raw_assertion_ids=tuple(raw.raw_assertion_id for raw in output.raw_assertions),
            blocked_reason="raw_assertion_references_unavailable_anchor",
            extraction_status=output.status,
            reasons=("raw_assertion_anchor_id_not_in_task_anchor",),
        )
    if not output.raw_assertions:
        return SourceBackedClaimReplayResult(
            **base,
            replay_status="no_raw_assertions",
            blocked_reason=output.blocked_reason or "no_explicit_assertions_extracted",
            extraction_status=output.status,
            reasons=("claim_replay_completed_without_raw_assertions",),
        )
    return SourceBackedClaimReplayResult(
        **base,
        replay_status="raw_assertions_extracted",
        raw_assertion_count=len(output.raw_assertions),
        raw_assertion_ids=tuple(raw.raw_assertion_id for raw in output.raw_assertions),
        raw_assertions=tuple(_raw_assertion_manifest_payload(raw) for raw in output.raw_assertions),
        extraction_status=output.status,
        adjudication_ready=True,
        score_blocked_until_adjudication=True,
        production_score_fixture=False,
        reasons=("claim_replay_raw_assertions_ready_for_adjudication",),
    )


def _claim_replay_result_base(task: Mapping[str, Any]) -> Mapping[str, Any]:
    return {
        "task_id": _optional_text(task.get("task_id")) or "",
        "fixture_kind": _optional_text(task.get("fixture_kind")) or "",
        "fixture_seed_id": _optional_text(task.get("fixture_seed_id")) or "",
        "candidate_id": _optional_text(task.get("candidate_id")) or "",
        "archetype_id": _optional_text(task.get("archetype_id")) or "",
        "target_entity_id": _optional_text(task.get("target_entity_id")) or "",
        "target_names": tuple(str(item).strip() for item in (task.get("target_names") or ()) if str(item).strip()),
        "as_of_date": _optional_text(task.get("as_of_date")),
        "document_id": _optional_text(task.get("document_id")) or "",
        "anchor_id": _optional_text(task.get("anchor_id")) or "",
        "canonical_url": _optional_text(task.get("canonical_url")),
        "source_type": _optional_text(task.get("source_type")),
        "source_name": _optional_text(task.get("source_name")),
        "source_lineage_id": _optional_text(task.get("source_lineage_id")),
        "content_hash": _optional_text(task.get("content_hash")),
        "extracted_text_path": _optional_text(task.get("extracted_text_path")),
        "anchor_locator": _optional_text(task.get("anchor_locator")),
        "document_published_at": _optional_text(task.get("document_published_at")),
        "replacement_candidate_id": _optional_text(task.get("replacement_candidate_id")),
        "original_source_anchor": _optional_text(task.get("original_source_anchor")),
        "candidate_url": _optional_text(task.get("candidate_url")),
    }


def _raw_assertion_manifest_payload(raw: Any) -> Mapping[str, Any]:
    return {
        "raw_assertion_id": raw.raw_assertion_id,
        "anchor_id": raw.anchor_id,
        "subject_text": raw.subject_text,
        "predicate": raw.predicate,
        "object_text": raw.object_text,
        "value": raw.value,
        "unit": raw.unit,
        "polarity_proposal": raw.polarity_proposal.value,
        "modality": raw.modality,
        "certainty": raw.certainty,
        "event_date_text": raw.event_date_text,
        "effective_period_text": raw.effective_period_text,
        "exact_quote": raw.exact_quote,
        "span": raw.span,
        "related_entity_texts": tuple(raw.related_entity_texts),
        "extractor_model": raw.extractor_model,
        "extractor_prompt_hash": raw.extractor_prompt_hash,
    }


def _adjudication_task_for_raw_assertion(
    result: Mapping[str, Any],
    raw: Mapping[str, Any],
) -> SourceBackedAdjudicationTask | None:
    expected_anchor_id = _optional_text(result.get("anchor_id")) or ""
    raw_anchor_id = _optional_text(raw.get("anchor_id")) or ""
    raw_assertion_id = _optional_text(raw.get("raw_assertion_id")) or ""
    if not raw_assertion_id or raw_anchor_id != expected_anchor_id:
        return None
    claim_replay_task_id = _optional_text(result.get("task_id")) or ""
    task_id = "ADJ-" + hashlib.sha1(
        "|".join(
            (
                claim_replay_task_id,
                raw_assertion_id,
                _optional_text(result.get("document_id")) or "",
                expected_anchor_id,
            )
        ).encode("utf-8")
    ).hexdigest()[:20]
    return SourceBackedAdjudicationTask(
        task_id=task_id,
        claim_replay_task_id=claim_replay_task_id,
        raw_assertion_id=raw_assertion_id,
        fixture_kind=_optional_text(result.get("fixture_kind")) or "",
        fixture_seed_id=_optional_text(result.get("fixture_seed_id")) or "",
        candidate_id=_optional_text(result.get("candidate_id")) or "",
        archetype_id=_optional_text(result.get("archetype_id")) or "",
        target_entity_id=_optional_text(result.get("target_entity_id")) or "",
        target_names=tuple(str(item).strip() for item in (result.get("target_names") or ()) if str(item).strip()),
        as_of_date=_optional_text(result.get("as_of_date")),
        document_id=_optional_text(result.get("document_id")) or "",
        anchor_id=expected_anchor_id,
        subject_text=_optional_text(raw.get("subject_text")) or "",
        predicate=_optional_text(raw.get("predicate")) or "",
        exact_quote=_optional_text(raw.get("exact_quote")) or "",
        canonical_url=_optional_text(result.get("canonical_url")),
        source_type=_optional_text(result.get("source_type")),
        source_name=_optional_text(result.get("source_name")),
        source_lineage_id=_optional_text(result.get("source_lineage_id")),
        content_hash=_optional_text(result.get("content_hash")),
        extracted_text_path=_optional_text(result.get("extracted_text_path")),
        anchor_locator=_optional_text(result.get("anchor_locator")),
        document_published_at=_optional_text(result.get("document_published_at")),
        replacement_candidate_id=_optional_text(result.get("replacement_candidate_id")),
        original_source_anchor=_optional_text(result.get("original_source_anchor")),
        candidate_url=_optional_text(result.get("candidate_url")),
        raw_assertion=raw,
    )


def _adjudication_skip_row(result: Mapping[str, Any], *, skip_reason: str) -> Mapping[str, Any]:
    return {
        "claim_replay_task_id": _optional_text(result.get("task_id")) or "",
        "fixture_kind": _optional_text(result.get("fixture_kind")),
        "fixture_seed_id": _optional_text(result.get("fixture_seed_id")),
        "candidate_id": _optional_text(result.get("candidate_id")),
        "archetype_id": _optional_text(result.get("archetype_id")),
        "document_id": _optional_text(result.get("document_id")),
        "anchor_id": _optional_text(result.get("anchor_id")),
        "replay_status": _optional_text(result.get("replay_status")),
        "skip_reason": skip_reason,
        "production_score_fixture": False,
    }


def _adjudication_result_for_task(
    task: Mapping[str, Any],
    adjudication_row: Mapping[str, Any] | None,
) -> SourceBackedAdjudicationResult:
    base = _adjudication_result_base(task)
    if adjudication_row is None:
        return SourceBackedAdjudicationResult(
            **base,
            adjudication_status="adjudication_not_attempted",
            blocked_reason="adjudication_result_missing",
            reasons=("adjudication_result_missing",),
        )
    if _optional_bool(adjudication_row.get("ok")) is False:
        reason = _optional_text(adjudication_row.get("reason")) or "adjudication_provider_error"
        return SourceBackedAdjudicationResult(
            **base,
            adjudication_status="provider_error",
            blocked_reason=reason,
            reasons=(reason,),
        )
    payload = adjudication_row.get("output")
    if not isinstance(payload, Mapping):
        payload = _adjudication_payload_from_flat_row(adjudication_row)
    try:
        proposal = decode_adjudication_proposal(payload)
    except Exception as exc:
        return SourceBackedAdjudicationResult(
            **base,
            adjudication_status="invalid_provider_output",
            blocked_reason=str(exc)[:180],
            reasons=("adjudication_output_decode_failed",),
        )
    status, reasons = _adjudication_status_and_reasons(
        proposal,
        target_entity_id=_optional_text(task.get("target_entity_id")) or "",
    )
    mapping_ready = status == "mapping_ready"
    return SourceBackedAdjudicationResult(
        **base,
        adjudication_status=status,
        subject_entity_id=proposal.subject_entity_id,
        relation_to_target=proposal.relation_to_target.value,
        directness=proposal.directness.value,
        target_scope_status=proposal.target_scope_status.value,
        polarity=proposal.polarity.value,
        temporal_status=proposal.temporal_status.value,
        semantic_status=proposal.semantic_status.value,
        investigation_status=proposal.investigation_status.value,
        event_date=proposal.event_date.isoformat() if proposal.event_date else None,
        effective_start=proposal.effective_start.isoformat() if proposal.effective_start else None,
        effective_end=proposal.effective_end.isoformat() if proposal.effective_end else None,
        rationale=proposal.rationale,
        mapping_ready=mapping_ready,
        score_blocked_until_mapping=True,
        production_score_fixture=False,
        blocked_reason=None if mapping_ready else ",".join(reasons),
        reasons=reasons,
    )


def _claim_extraction_payload_from_flat_row(row: Mapping[str, Any]) -> Mapping[str, Any]:
    return {
        "status": str(row.get("status") or "ok"),
        "blocked_reason": row.get("blocked_reason"),
        "raw_assertions": row.get("raw_assertions", ()),
    }


def _adjudication_payload_from_flat_row(row: Mapping[str, Any]) -> Mapping[str, Any]:
    return {key: row.get(key) for key in ADJUDICATION_OUTPUT_FIELDS if key in row}


def _adjudication_result_base(task: Mapping[str, Any]) -> Mapping[str, Any]:
    return {
        "task_id": _optional_text(task.get("task_id")) or "",
        "claim_replay_task_id": _optional_text(task.get("claim_replay_task_id")) or "",
        "raw_assertion_id": _optional_text(task.get("raw_assertion_id")) or "",
        "fixture_kind": _optional_text(task.get("fixture_kind")) or "",
        "fixture_seed_id": _optional_text(task.get("fixture_seed_id")) or "",
        "candidate_id": _optional_text(task.get("candidate_id")) or "",
        "archetype_id": _optional_text(task.get("archetype_id")) or "",
        "target_entity_id": _optional_text(task.get("target_entity_id")) or "",
        "target_names": tuple(str(item).strip() for item in (task.get("target_names") or ()) if str(item).strip()),
        "as_of_date": _optional_text(task.get("as_of_date")),
        "document_id": _optional_text(task.get("document_id")) or "",
        "anchor_id": _optional_text(task.get("anchor_id")) or "",
        "canonical_url": _optional_text(task.get("canonical_url")),
        "source_type": _optional_text(task.get("source_type")),
        "source_name": _optional_text(task.get("source_name")),
        "source_lineage_id": _optional_text(task.get("source_lineage_id")),
        "content_hash": _optional_text(task.get("content_hash")),
        "extracted_text_path": _optional_text(task.get("extracted_text_path")),
        "anchor_locator": _optional_text(task.get("anchor_locator")),
        "document_published_at": _optional_text(task.get("document_published_at")),
        "replacement_candidate_id": _optional_text(task.get("replacement_candidate_id")),
        "original_source_anchor": _optional_text(task.get("original_source_anchor")),
        "candidate_url": _optional_text(task.get("candidate_url")),
        "raw_assertion": task.get("raw_assertion") if isinstance(task.get("raw_assertion"), Mapping) else None,
    }


def _adjudication_status_and_reasons(proposal: Any, *, target_entity_id: str) -> tuple[str, tuple[str, ...]]:
    reasons: list[str] = []
    subject_entity_id = _optional_text(getattr(proposal, "subject_entity_id", None)) or ""
    relation_to_target = getattr(proposal, "relation_to_target", RelationToTarget.UNKNOWN)
    target_scope_status = getattr(proposal, "target_scope_status", TargetScopeStatus.UNKNOWN)
    directness = getattr(proposal, "directness", Directness.UNKNOWN)
    if (
        relation_to_target == RelationToTarget.SELF
        and _looks_like_entity_id(subject_entity_id)
        and subject_entity_id != target_entity_id
    ):
        reasons.append("self_relation_subject_entity_mismatch")
        return "target_scope_blocked", tuple(reasons)
    if relation_to_target == RelationToTarget.UNRELATED:
        reasons.append("relation_to_target:UNRELATED")
        return "target_scope_blocked", tuple(reasons)
    if relation_to_target == RelationToTarget.INDUSTRY and target_scope_status == TargetScopeStatus.DIRECT:
        reasons.append("industry_relation_cannot_be_direct_target_scope")
        return "target_scope_blocked", tuple(reasons)
    related_entity_mapping_allowed = (
        relation_to_target in {RelationToTarget.SUBSIDIARY, RelationToTarget.PARENT}
        and target_scope_status
        in {
            TargetScopeStatus.SUBSIDIARY,
            TargetScopeStatus.PARENT,
        }
        and directness in {Directness.DIRECT, Directness.INDIRECT}
    )
    partner_direct_mapping_allowed = (
        relation_to_target == RelationToTarget.PARTNER
        and target_scope_status == TargetScopeStatus.PARTNER
        and directness == Directness.DIRECT
    )
    if directness != Directness.DIRECT and not related_entity_mapping_allowed:
        reasons.append("target_not_direct")
        return "target_scope_blocked", tuple(reasons)
    if relation_to_target not in {RelationToTarget.SELF, RelationToTarget.SUBSIDIARY, RelationToTarget.PARENT}:
        if partner_direct_mapping_allowed:
            pass
        else:
            reasons.append(f"relation_to_target:{relation_to_target.value}")
            return "target_scope_blocked", tuple(reasons)
    if proposal.temporal_status != TemporalStatus.CURRENT:
        reasons.append(f"temporal_status:{proposal.temporal_status.value}")
        return "temporal_blocked", tuple(reasons)
    if proposal.semantic_status != SemanticStatus.PASS_:
        reasons.append(f"semantic_status:{proposal.semantic_status.value}")
        return "semantic_blocked", tuple(reasons)
    if proposal.investigation_status != InvestigationStatus.COMPLETE:
        reasons.append(f"investigation_status:{proposal.investigation_status.value}")
        return "investigation_blocked", tuple(reasons)
    return "mapping_ready", ("adjudication_passed_target_temporal_semantic_gate",)


def _looks_like_entity_id(value: str) -> bool:
    return bool(re.match(r"^(KRX|CORP|DART|CIK|NYSE|NASDAQ|TSE|HKEX|LSE)[:_]", value))


def _primitive_mapping_task_for_adjudication_result(
    result: Mapping[str, Any],
) -> SourceBackedPrimitiveMappingTask | None:
    if result.get("adjudication_status") != "mapping_ready" or not _optional_bool(result.get("mapping_ready")):
        return None
    claim_id = _claim_id_for_source_backed_adjudication_result(result)
    if not claim_id:
        return None
    task_id = "PMAP-" + hashlib.sha1(
        "|".join(
            (
                _optional_text(result.get("task_id")) or "",
                _optional_text(result.get("raw_assertion_id")) or "",
                _optional_text(result.get("archetype_id")) or "",
                _optional_text(result.get("subject_entity_id")) or "",
            )
        ).encode("utf-8")
    ).hexdigest()[:20]
    return SourceBackedPrimitiveMappingTask(
        task_id=task_id,
        claim_id=claim_id,
        adjudication_task_id=_optional_text(result.get("task_id")) or "",
        claim_replay_task_id=_optional_text(result.get("claim_replay_task_id")) or "",
        raw_assertion_id=_optional_text(result.get("raw_assertion_id")) or "",
        fixture_kind=_optional_text(result.get("fixture_kind")) or "",
        fixture_seed_id=_optional_text(result.get("fixture_seed_id")) or "",
        candidate_id=_optional_text(result.get("candidate_id")) or "",
        archetype_id=_optional_text(result.get("archetype_id")) or "",
        target_entity_id=_optional_text(result.get("target_entity_id")) or "",
        target_names=tuple(str(item).strip() for item in (result.get("target_names") or ()) if str(item).strip()),
        subject_entity_id=_optional_text(result.get("subject_entity_id")) or "",
        as_of_date=_optional_text(result.get("as_of_date")),
        document_id=_optional_text(result.get("document_id")) or "",
        anchor_id=_optional_text(result.get("anchor_id")) or "",
        relation_to_target=_optional_text(result.get("relation_to_target")) or "",
        directness=_optional_text(result.get("directness")) or "",
        target_scope_status=_optional_text(result.get("target_scope_status")) or "",
        polarity=_optional_text(result.get("polarity")) or "",
        temporal_status=_optional_text(result.get("temporal_status")) or "",
        semantic_status=_optional_text(result.get("semantic_status")) or "",
        investigation_status=_optional_text(result.get("investigation_status")) or "",
        event_date=_optional_text(result.get("event_date")),
        effective_start=_optional_text(result.get("effective_start")),
        effective_end=_optional_text(result.get("effective_end")),
        canonical_url=_optional_text(result.get("canonical_url")),
        source_type=_optional_text(result.get("source_type")),
        source_name=_optional_text(result.get("source_name")),
        source_lineage_id=_optional_text(result.get("source_lineage_id")),
        content_hash=_optional_text(result.get("content_hash")),
        extracted_text_path=_optional_text(result.get("extracted_text_path")),
        anchor_locator=_optional_text(result.get("anchor_locator")),
        document_published_at=_optional_text(result.get("document_published_at")),
        replacement_candidate_id=_optional_text(result.get("replacement_candidate_id")),
        original_source_anchor=_optional_text(result.get("original_source_anchor")),
        candidate_url=_optional_text(result.get("candidate_url")),
        raw_assertion=result.get("raw_assertion") if isinstance(result.get("raw_assertion"), Mapping) else None,
    )


def _claim_id_for_source_backed_adjudication_result(result: Mapping[str, Any]) -> str | None:
    raw_payload = result.get("raw_assertion")
    if not isinstance(raw_payload, Mapping):
        return None
    try:
        raw = decode_claim_extraction_output(
            {"status": "ok", "blocked_reason": None, "raw_assertions": [raw_payload]}
        ).raw_assertions[0]
    except Exception:
        return None
    document_id = _optional_text(result.get("document_id")) or _stable_short_id(
        "DOC",
        _optional_text(result.get("fixture_seed_id")) or "",
        _optional_text(result.get("candidate_id")) or "",
        raw.anchor_id,
    )
    content_hash = _optional_text(result.get("content_hash")) or hashlib.sha256(document_id.encode("utf-8")).hexdigest()
    published_at = _parse_iso_date(_optional_text(result.get("document_published_at")))
    source_type = _source_type_from_text(result.get("source_type"))
    document = EvidenceDocument(
        document_id=document_id,
        canonical_url=_optional_text(result.get("canonical_url")),
        source_type=source_type,
        source_name=_optional_text(result.get("source_name")) or source_type.value,
        content_hash=content_hash,
        published_at=published_at,
        available_at=published_at,
        parser_version="source_backed_replay_claim_id_v1",
        source_proxy_only=False,
        score_block_reasons=("primitive_mapping_pending",),
    )
    exact_text = _optional_text(raw.exact_quote) or _optional_text(raw.object_text) or ""
    anchor = EvidenceAnchor(
        anchor_id=_optional_text(result.get("anchor_id")) or raw.anchor_id,
        document_id=document.document_id,
        anchor_type=AnchorType.TEXT_SPAN,
        locator=_optional_text(result.get("anchor_locator")) or raw.anchor_id,
        exact_text=exact_text,
        content_hash=hashlib.sha256(exact_text.encode("utf-8")).hexdigest() if exact_text else None,
        anchor_verified=bool(exact_text),
    )
    claim = AdjudicatedClaim.from_raw(
        raw=raw,
        document=document,
        anchor=anchor,
        subject_entity_id=_optional_text(result.get("subject_entity_id")) or "",
        target_entity_id=_optional_text(result.get("target_entity_id")) or "",
        relation_to_target=_enum_from_text(
            RelationToTarget,
            result.get("relation_to_target"),
            RelationToTarget.UNKNOWN,
        ),
        directness=_enum_from_text(Directness, result.get("directness"), Directness.UNKNOWN),
        verification_status=VerificationStatus.SEMANTIC_VERIFIED,
        target_scope_status=_enum_from_text(
            TargetScopeStatus,
            result.get("target_scope_status"),
            TargetScopeStatus.UNKNOWN,
        ),
        polarity=_enum_from_text(Polarity, result.get("polarity"), Polarity.CONDITIONAL),
        temporal_status=_enum_from_text(TemporalStatus, result.get("temporal_status"), TemporalStatus.UNKNOWN),
        semantic_status=_enum_from_text(SemanticStatus, result.get("semantic_status"), SemanticStatus.UNVERIFIED),
        investigation_status=_enum_from_text(
            InvestigationStatus,
            result.get("investigation_status"),
            InvestigationStatus.FOLLOWUP_REQUIRED,
        ),
        event_date=_parse_iso_date(_optional_text(result.get("event_date"))),
        effective_start=_parse_iso_date(_optional_text(result.get("effective_start"))),
        effective_end=_parse_iso_date(_optional_text(result.get("effective_end"))),
        adjudication_rationale=_optional_text(result.get("rationale")) or "",
    )
    return claim.claim_id


def _primitive_mapping_skip_row(result: Mapping[str, Any], *, skip_reason: str) -> Mapping[str, Any]:
    return {
        "adjudication_task_id": _optional_text(result.get("task_id")) or "",
        "claim_replay_task_id": _optional_text(result.get("claim_replay_task_id")),
        "raw_assertion_id": _optional_text(result.get("raw_assertion_id")),
        "fixture_seed_id": _optional_text(result.get("fixture_seed_id")),
        "candidate_id": _optional_text(result.get("candidate_id")),
        "archetype_id": _optional_text(result.get("archetype_id")),
        "document_id": _optional_text(result.get("document_id")),
        "anchor_id": _optional_text(result.get("anchor_id")),
        "adjudication_status": _optional_text(result.get("adjudication_status")),
        "skip_reason": skip_reason,
        "production_score_fixture": False,
    }


def _primitive_mapping_result_for_missing_task(task: Mapping[str, Any]) -> SourceBackedPrimitiveMappingResult:
    return SourceBackedPrimitiveMappingResult(
        **_primitive_mapping_result_base(task),
        task_id=_primitive_mapping_result_id(task, primitive_id="missing", support_direction=""),
        result_status="mapping_not_attempted",
        blocked_reason="primitive_mapping_result_missing",
        reasons=("primitive_mapping_result_missing",),
    )


def _primitive_mapping_results_for_task_row(
    task: Mapping[str, Any],
    row: Mapping[str, Any],
    *,
    canonical_primitive_ids_by_archetype: Mapping[str, Sequence[str]],
) -> tuple[SourceBackedPrimitiveMappingResult, ...]:
    base = _primitive_mapping_result_base(task)
    if _optional_bool(row.get("ok")) is False:
        reason = _optional_text(row.get("reason")) or "primitive_mapping_provider_error"
        return (
            SourceBackedPrimitiveMappingResult(
                **base,
                task_id=_primitive_mapping_result_id(task, primitive_id="provider_error", support_direction=""),
                result_status="provider_error",
                blocked_reason=reason,
                reasons=(reason,),
            ),
        )
    raw_mappings = row.get("mappings")
    if raw_mappings is None:
        raw_mappings = row.get("output", {}).get("mappings") if isinstance(row.get("output"), Mapping) else None
    if raw_mappings is None:
        raw_mappings = (row,)
    if not isinstance(raw_mappings, Sequence) or isinstance(raw_mappings, (str, bytes, bytearray)):
        return (
            SourceBackedPrimitiveMappingResult(
                **base,
                task_id=_primitive_mapping_result_id(task, primitive_id="invalid", support_direction=""),
                result_status="invalid_provider_output",
                blocked_reason="primitive_mapping_output_not_sequence",
                reasons=("primitive_mapping_output_not_sequence",),
            ),
        )
    results: list[SourceBackedPrimitiveMappingResult] = []
    for mapping in raw_mappings:
        if not isinstance(mapping, Mapping):
            results.append(
                SourceBackedPrimitiveMappingResult(
                    **base,
                    task_id=_primitive_mapping_result_id(task, primitive_id="invalid", support_direction=""),
                    result_status="invalid_provider_output",
                    blocked_reason="primitive_mapping_item_not_mapping",
                    reasons=("primitive_mapping_item_not_mapping",),
                )
            )
            continue
        try:
            decoded_mapping = decode_primitive_mapping_output({"mappings": [mapping]}).mappings[0]
            mapping = _primitive_mapping_payload_from_proposal(decoded_mapping)
        except Exception as exc:
            results.append(
                SourceBackedPrimitiveMappingResult(
                    **base,
                    task_id=_primitive_mapping_result_id(task, primitive_id="invalid", support_direction=""),
                    result_status="invalid_provider_output",
                    blocked_reason=str(exc)[:180],
                    reasons=("primitive_mapping_output_decode_failed",),
                )
            )
            continue
        results.append(
            _primitive_mapping_result_for_mapping(
                task,
                mapping,
                canonical_primitive_ids_by_archetype=canonical_primitive_ids_by_archetype,
            )
    )
    return tuple(results)


def _primitive_mapping_payload_from_proposal(proposal: Any) -> Mapping[str, Any]:
    payload = asdict(proposal)
    for key in ("support_direction", "mapping_status"):
        value = payload.get(key)
        if hasattr(value, "value"):
            payload[key] = value.value
    return {key: payload.get(key) for key in PRIMITIVE_MAPPING_ROW_FIELDS if key in payload}


def _primitive_mapping_result_for_mapping(
    task: Mapping[str, Any],
    mapping: Mapping[str, Any],
    *,
    canonical_primitive_ids_by_archetype: Mapping[str, Sequence[str]],
) -> SourceBackedPrimitiveMappingResult:
    base = _primitive_mapping_result_base(task)
    expected_claim_id = _optional_text(task.get("claim_id")) or ""
    mapped_claim_id = _optional_text(mapping.get("claim_id")) or ""
    if expected_claim_id and mapped_claim_id != expected_claim_id:
        return SourceBackedPrimitiveMappingResult(
            **base,
            task_id=_primitive_mapping_result_id(task, primitive_id="claim_mismatch", support_direction=""),
            result_status="claim_id_mismatch",
            blocked_reason="primitive_mapping_claim_id_mismatch",
            reasons=("primitive_mapping_claim_id_mismatch",),
        )
    primitive_id = _optional_text(mapping.get("primitive_id"))
    support_direction = _optional_text(mapping.get("support_direction")) or "SUPPORT"
    mapping_status = _optional_text(mapping.get("mapping_status")) or "PROPOSED"
    if not primitive_id:
        return SourceBackedPrimitiveMappingResult(
            **base,
            task_id=_primitive_mapping_result_id(task, primitive_id="missing", support_direction=support_direction),
            result_status="invalid_provider_output",
            blocked_reason="primitive_id_missing",
            reasons=("primitive_id_missing",),
        )
    canonical_ids = tuple(
        str(item).strip()
        for item in canonical_primitive_ids_by_archetype.get(_optional_text(task.get("archetype_id")) or "", ())
        if str(item).strip()
    )
    if not canonical_ids:
        return SourceBackedPrimitiveMappingResult(
            **base,
            task_id=_primitive_mapping_result_id(task, primitive_id=primitive_id, support_direction=support_direction),
            result_status="primitive_registry_missing",
            primitive_id=primitive_id,
            support_direction=support_direction,
            mapping_status=mapping_status,
            blocked_reason="canonical_primitive_registry_missing_for_archetype",
            reasons=("canonical_primitive_registry_missing_for_archetype",),
        )
    if primitive_id not in canonical_ids:
        return SourceBackedPrimitiveMappingResult(
            **base,
            task_id=_primitive_mapping_result_id(task, primitive_id=primitive_id, support_direction=support_direction),
            result_status="invented_primitive_blocked",
            primitive_id=primitive_id,
            support_direction=support_direction,
            mapping_status=mapping_status,
            blocked_reason="primitive_id_not_in_canonical_registry",
            reasons=("primitive_id_not_in_canonical_registry",),
        )
    if mapping_status not in {"PROPOSED", "ACCEPTED"} or support_direction == "NEUTRAL":
        return SourceBackedPrimitiveMappingResult(
            **base,
            task_id=_primitive_mapping_result_id(task, primitive_id=primitive_id, support_direction=support_direction),
            result_status="mapping_rejected",
            primitive_id=primitive_id,
            support_direction=support_direction,
            mapping_status=mapping_status,
            contract_rule_id=_optional_text(mapping.get("contract_rule_id")),
            rationale=_optional_text(mapping.get("rationale")) or "",
            blocked_reason=f"mapping_status:{mapping_status}",
            reasons=(f"mapping_status:{mapping_status}",),
        )
    return SourceBackedPrimitiveMappingResult(
        **base,
        task_id=_primitive_mapping_result_id(task, primitive_id=primitive_id, support_direction=support_direction),
        result_status="mapping_ready_for_eligibility",
        primitive_id=primitive_id,
        support_direction=support_direction,
        mapping_status=mapping_status,
        contract_rule_id=_optional_text(mapping.get("contract_rule_id")),
        rationale=_optional_text(mapping.get("rationale")) or "",
        eligibility_ready=True,
        score_blocked_until_eligibility=True,
        production_score_fixture=False,
        reasons=("primitive_mapping_ready_for_eligibility_checks",),
    )


def _primitive_mapping_result_base(task: Mapping[str, Any]) -> Mapping[str, Any]:
    return {
        "primitive_mapping_task_id": _optional_text(task.get("task_id")) or "",
        "claim_id": _optional_text(task.get("claim_id")) or "",
        "adjudication_task_id": _optional_text(task.get("adjudication_task_id")) or "",
        "raw_assertion_id": _optional_text(task.get("raw_assertion_id")) or "",
        "fixture_seed_id": _optional_text(task.get("fixture_seed_id")) or "",
        "candidate_id": _optional_text(task.get("candidate_id")) or "",
        "archetype_id": _optional_text(task.get("archetype_id")) or "",
        "target_entity_id": _optional_text(task.get("target_entity_id")) or "",
        "subject_entity_id": _optional_text(task.get("subject_entity_id")) or "",
        "as_of_date": _optional_text(task.get("as_of_date")),
        "document_id": _optional_text(task.get("document_id")) or "",
        "anchor_id": _optional_text(task.get("anchor_id")) or "",
        "relation_to_target": _optional_text(task.get("relation_to_target")) or "",
        "directness": _optional_text(task.get("directness")) or "",
        "target_scope_status": _optional_text(task.get("target_scope_status")) or "",
        "polarity": _optional_text(task.get("polarity")) or "",
        "temporal_status": _optional_text(task.get("temporal_status")) or "",
        "semantic_status": _optional_text(task.get("semantic_status")) or "",
        "investigation_status": _optional_text(task.get("investigation_status")) or "",
        "event_date": _optional_text(task.get("event_date")),
        "effective_start": _optional_text(task.get("effective_start")),
        "effective_end": _optional_text(task.get("effective_end")),
        "canonical_url": _optional_text(task.get("canonical_url")),
        "source_type": _optional_text(task.get("source_type")),
        "source_name": _optional_text(task.get("source_name")),
        "source_lineage_id": _optional_text(task.get("source_lineage_id")),
        "content_hash": _optional_text(task.get("content_hash")),
        "extracted_text_path": _optional_text(task.get("extracted_text_path")),
        "anchor_locator": _optional_text(task.get("anchor_locator")),
        "document_published_at": _optional_text(task.get("document_published_at")),
        "replacement_candidate_id": _optional_text(task.get("replacement_candidate_id")),
        "original_source_anchor": _optional_text(task.get("original_source_anchor")),
        "candidate_url": _optional_text(task.get("candidate_url")),
        "raw_assertion": task.get("raw_assertion") if isinstance(task.get("raw_assertion"), Mapping) else None,
    }


def _primitive_mapping_result_id(task: Mapping[str, Any], *, primitive_id: str, support_direction: str) -> str:
    return "PMRES-" + hashlib.sha1(
        "|".join(
            (
                _optional_text(task.get("task_id")) or "",
                _optional_text(task.get("raw_assertion_id")) or "",
                primitive_id,
                support_direction,
            )
        ).encode("utf-8")
    ).hexdigest()[:20]


def _eligibility_task_for_mapping_result(result: Mapping[str, Any]) -> SourceBackedEligibilityTask | None:
    if result.get("result_status") != "mapping_ready_for_eligibility" or not _optional_bool(
        result.get("eligibility_ready")
    ):
        return None
    task_id = "ELIG-" + hashlib.sha1(
        "|".join(
            (
                _optional_text(result.get("task_id")) or "",
                _optional_text(result.get("primitive_id")) or "",
                _optional_text(result.get("support_direction")) or "",
            )
        ).encode("utf-8")
    ).hexdigest()[:20]
    return SourceBackedEligibilityTask(
        task_id=task_id,
        primitive_mapping_result_id=_optional_text(result.get("task_id")) or "",
        primitive_mapping_task_id=_optional_text(result.get("primitive_mapping_task_id")) or "",
        claim_id=_optional_text(result.get("claim_id")) or "",
        adjudication_task_id=_optional_text(result.get("adjudication_task_id")) or "",
        raw_assertion_id=_optional_text(result.get("raw_assertion_id")) or "",
        fixture_seed_id=_optional_text(result.get("fixture_seed_id")) or "",
        candidate_id=_optional_text(result.get("candidate_id")) or "",
        archetype_id=_optional_text(result.get("archetype_id")) or "",
        target_entity_id=_optional_text(result.get("target_entity_id")) or "",
        subject_entity_id=_optional_text(result.get("subject_entity_id")) or "",
        as_of_date=_optional_text(result.get("as_of_date")),
        document_id=_optional_text(result.get("document_id")) or "",
        anchor_id=_optional_text(result.get("anchor_id")) or "",
        primitive_id=_optional_text(result.get("primitive_id")) or "",
        support_direction=_optional_text(result.get("support_direction")) or "",
        mapping_status=_optional_text(result.get("mapping_status")) or "",
        relation_to_target=_optional_text(result.get("relation_to_target")) or "",
        directness=_optional_text(result.get("directness")) or "",
        target_scope_status=_optional_text(result.get("target_scope_status")) or "",
        polarity=_optional_text(result.get("polarity")) or "",
        temporal_status=_optional_text(result.get("temporal_status")) or "",
        semantic_status=_optional_text(result.get("semantic_status")) or "",
        investigation_status=_optional_text(result.get("investigation_status")) or "",
        event_date=_optional_text(result.get("event_date")),
        effective_start=_optional_text(result.get("effective_start")),
        effective_end=_optional_text(result.get("effective_end")),
        canonical_url=_optional_text(result.get("canonical_url")),
        source_type=_optional_text(result.get("source_type")),
        source_name=_optional_text(result.get("source_name")),
        source_lineage_id=_optional_text(result.get("source_lineage_id")),
        content_hash=_optional_text(result.get("content_hash")),
        extracted_text_path=_optional_text(result.get("extracted_text_path")),
        anchor_locator=_optional_text(result.get("anchor_locator")),
        document_published_at=_optional_text(result.get("document_published_at")),
        replacement_candidate_id=_optional_text(result.get("replacement_candidate_id")),
        original_source_anchor=_optional_text(result.get("original_source_anchor")),
        candidate_url=_optional_text(result.get("candidate_url")),
        contract_rule_id=_optional_text(result.get("contract_rule_id")),
        mapping_rationale=_optional_text(result.get("rationale")) or "",
        raw_assertion=result.get("raw_assertion") if isinstance(result.get("raw_assertion"), Mapping) else None,
    )


def _eligibility_skip_row(result: Mapping[str, Any], *, skip_reason: str) -> Mapping[str, Any]:
    return {
        "primitive_mapping_result_id": _optional_text(result.get("task_id")) or "",
        "primitive_mapping_task_id": _optional_text(result.get("primitive_mapping_task_id")),
        "raw_assertion_id": _optional_text(result.get("raw_assertion_id")),
        "archetype_id": _optional_text(result.get("archetype_id")),
        "primitive_id": _optional_text(result.get("primitive_id")),
        "result_status": _optional_text(result.get("result_status")),
        "skip_reason": skip_reason,
        "production_score_fixture": False,
    }


def _eligibility_result_for_task(
    task: Mapping[str, Any],
    row: Mapping[str, Any] | None,
) -> SourceBackedEligibilityResult:
    base = _eligibility_result_base(task)
    if row is None:
        return SourceBackedEligibilityResult(
            **base,
            task_id=_eligibility_result_id(task),
            result_status="eligibility_not_attempted",
            blocked_reason="eligibility_result_missing",
            reasons=("eligibility_result_missing",),
        )
    if _optional_bool(row.get("ok")) is False:
        reason = _optional_text(row.get("reason")) or "eligibility_provider_error"
        return SourceBackedEligibilityResult(
            **base,
            task_id=_eligibility_result_id(task),
            result_status="invalid_eligibility_output",
            blocked_reason=reason,
            reasons=(reason,),
        )
    eligibility_source = _optional_text(row.get("eligibility_source"))
    source_anchor_verified = _optional_bool(row.get("source_anchor_verified")) is True
    future_leakage = _optional_bool(row.get("future_leakage")) is True
    source_proxy_only = _optional_bool(row.get("source_proxy_only")) is True
    snippet_only = _optional_bool(row.get("snippet_only")) is True
    unresolved_contradiction = _optional_bool(row.get("unresolved_contradiction")) is True
    eligible = _optional_bool(row.get("eligible")) is True
    status = _eligibility_result_status(
        eligibility_source=eligibility_source,
        source_anchor_verified=source_anchor_verified,
        future_leakage=future_leakage,
        source_proxy_only=source_proxy_only,
        snippet_only=snippet_only,
        unresolved_contradiction=unresolved_contradiction,
        eligible=eligible,
    )
    reasons = tuple(str(item).strip() for item in (row.get("reasons") or ()) if str(item).strip())
    if not reasons:
        reasons = (status,)
    return SourceBackedEligibilityResult(
        **base,
        task_id=_eligibility_result_id(task),
        result_status=status,
        eligibility_source=eligibility_source,
        eligibility_ready=status == "score_contribution_ready",
        source_anchor_verified=source_anchor_verified,
        future_leakage=future_leakage,
        source_proxy_only=source_proxy_only,
        snippet_only=snippet_only,
        unresolved_contradiction=unresolved_contradiction,
        score_blocked_until_score_contribution=True,
        production_score_fixture=False,
        blocked_reason=None if status == "score_contribution_ready" else ",".join(reasons),
        reasons=reasons,
    )


def _eligibility_result_status(
    *,
    eligibility_source: str | None,
    source_anchor_verified: bool,
    future_leakage: bool,
    source_proxy_only: bool,
    snippet_only: bool,
    unresolved_contradiction: bool,
    eligible: bool,
) -> str:
    if eligibility_source != "deterministic":
        return "non_deterministic_eligibility_blocked"
    if not source_anchor_verified:
        return "source_anchor_unverified"
    if future_leakage:
        return "future_leakage_blocked"
    if source_proxy_only:
        return "source_proxy_blocked"
    if snippet_only:
        return "snippet_only_blocked"
    if unresolved_contradiction:
        return "contradiction_blocked"
    if not eligible:
        return "eligibility_rejected"
    return "score_contribution_ready"


def _eligibility_result_base(task: Mapping[str, Any]) -> Mapping[str, Any]:
    return {
        "eligibility_task_id": _optional_text(task.get("task_id")) or "",
        "primitive_mapping_result_id": _optional_text(task.get("primitive_mapping_result_id")) or "",
        "primitive_mapping_task_id": _optional_text(task.get("primitive_mapping_task_id")) or "",
        "claim_id": _optional_text(task.get("claim_id")) or "",
        "raw_assertion_id": _optional_text(task.get("raw_assertion_id")) or "",
        "fixture_seed_id": _optional_text(task.get("fixture_seed_id")) or "",
        "candidate_id": _optional_text(task.get("candidate_id")) or "",
        "archetype_id": _optional_text(task.get("archetype_id")) or "",
        "target_entity_id": _optional_text(task.get("target_entity_id")) or "",
        "subject_entity_id": _optional_text(task.get("subject_entity_id")) or "",
        "as_of_date": _optional_text(task.get("as_of_date")),
        "source_lineage_id": _optional_text(task.get("source_lineage_id")),
        "document_id": _optional_text(task.get("document_id")) or "",
        "anchor_id": _optional_text(task.get("anchor_id")) or "",
        "primitive_id": _optional_text(task.get("primitive_id")) or "",
        "support_direction": _optional_text(task.get("support_direction")) or "",
    }


def _eligibility_result_id(task: Mapping[str, Any]) -> str:
    return "ELRES-" + hashlib.sha1(
        "|".join(
            (
                _optional_text(task.get("task_id")) or "",
                _optional_text(task.get("primitive_mapping_result_id")) or "",
                _optional_text(task.get("primitive_id")) or "",
            )
        ).encode("utf-8")
    ).hexdigest()[:20]


def _score_contribution_task_for_eligibility_result(
    result: Mapping[str, Any],
) -> SourceBackedScoreContributionTask | None:
    if result.get("result_status") != "score_contribution_ready" or not _optional_bool(
        result.get("eligibility_ready")
    ):
        return None
    task_id = "SCTASK-" + hashlib.sha1(
        "|".join(
            (
                _optional_text(result.get("task_id")) or "",
                _optional_text(result.get("primitive_id")) or "",
                _optional_text(result.get("support_direction")) or "",
            )
        ).encode("utf-8")
    ).hexdigest()[:20]
    return SourceBackedScoreContributionTask(
        task_id=task_id,
        eligibility_result_id=_optional_text(result.get("task_id")) or "",
        eligibility_task_id=_optional_text(result.get("eligibility_task_id")) or "",
        primitive_mapping_result_id=_optional_text(result.get("primitive_mapping_result_id")) or "",
        raw_assertion_id=_optional_text(result.get("raw_assertion_id")) or "",
        fixture_seed_id=_optional_text(result.get("fixture_seed_id")) or "",
        candidate_id=_optional_text(result.get("candidate_id")) or "",
        archetype_id=_optional_text(result.get("archetype_id")) or "",
        target_entity_id=_optional_text(result.get("target_entity_id")) or "",
        subject_entity_id=_optional_text(result.get("subject_entity_id")) or "",
        document_id=_optional_text(result.get("document_id")) or "",
        anchor_id=_optional_text(result.get("anchor_id")) or "",
        primitive_id=_optional_text(result.get("primitive_id")) or "",
        support_direction=_optional_text(result.get("support_direction")) or "",
    )


def _score_contribution_skip_row(result: Mapping[str, Any], *, skip_reason: str) -> Mapping[str, Any]:
    return {
        "eligibility_result_id": _optional_text(result.get("task_id")) or "",
        "eligibility_task_id": _optional_text(result.get("eligibility_task_id")),
        "primitive_mapping_result_id": _optional_text(result.get("primitive_mapping_result_id")),
        "archetype_id": _optional_text(result.get("archetype_id")),
        "primitive_id": _optional_text(result.get("primitive_id")),
        "result_status": _optional_text(result.get("result_status")),
        "skip_reason": skip_reason,
        "production_score_fixture": False,
    }


def _score_contribution_result_for_task(
    task: Mapping[str, Any],
    row: Mapping[str, Any] | None,
) -> SourceBackedScoreContributionResult:
    base = _score_contribution_result_base(task)
    if row is None:
        return SourceBackedScoreContributionResult(
            **base,
            task_id=_score_contribution_result_id(task),
            result_status="score_contribution_not_attempted",
            blocked_reason="score_contribution_result_missing",
            reasons=("score_contribution_result_missing",),
        )
    if _optional_bool(row.get("ok")) is False:
        reason = _optional_text(row.get("reason")) or "score_contribution_provider_error"
        return SourceBackedScoreContributionResult(
            **base,
            task_id=_score_contribution_result_id(task),
            result_status="invalid_score_contribution_output",
            blocked_reason=reason,
            reasons=(reason,),
        )
    source = _optional_text(row.get("contribution_source"))
    if source != "deterministic":
        return SourceBackedScoreContributionResult(
            **base,
            task_id=_score_contribution_result_id(task),
            result_status="non_deterministic_score_contribution_blocked",
            blocked_reason="contribution_source_not_deterministic",
            reasons=("contribution_source_not_deterministic",),
        )
    component_key = _optional_text(row.get("component_key"))
    criterion_id = _optional_text(row.get("criterion_id"))
    if not component_key:
        return SourceBackedScoreContributionResult(
            **base,
            task_id=_score_contribution_result_id(task),
            result_status="component_missing",
            blocked_reason="component_key_missing",
            reasons=("component_key_missing",),
        )
    if not criterion_id:
        return SourceBackedScoreContributionResult(
            **base,
            task_id=_score_contribution_result_id(task),
            result_status="criterion_missing",
            component_key=component_key,
            blocked_reason="criterion_id_missing",
            reasons=("criterion_id_missing",),
        )
    raw_points = _optional_float(row.get("raw_points"))
    max_points = _optional_float(row.get("max_points"))
    if raw_points is None or max_points is None:
        return SourceBackedScoreContributionResult(
            **base,
            task_id=_score_contribution_result_id(task),
            result_status="invalid_score_contribution_output",
            component_key=component_key,
            criterion_id=criterion_id,
            blocked_reason="raw_points_or_max_points_missing",
            reasons=("raw_points_or_max_points_missing",),
        )
    if raw_points < 0.0 or max_points < 0.0:
        return SourceBackedScoreContributionResult(
            **base,
            task_id=_score_contribution_result_id(task),
            result_status="negative_points_blocked",
            component_key=component_key,
            criterion_id=criterion_id,
            raw_points=raw_points,
            max_points=max_points,
            blocked_reason="negative_points_not_allowed",
            reasons=("negative_points_not_allowed",),
        )
    if raw_points > max_points:
        return SourceBackedScoreContributionResult(
            **base,
            task_id=_score_contribution_result_id(task),
            result_status="over_max_points_blocked",
            component_key=component_key,
            criterion_id=criterion_id,
            raw_points=raw_points,
            max_points=max_points,
            blocked_reason="raw_points_exceed_max_points",
            reasons=("raw_points_exceed_max_points",),
        )
    support_claim_ids = _text_tuple_from_value(row.get("support_claim_ids"))
    counter_claim_ids = _text_tuple_from_value(row.get("counter_claim_ids"))
    mapping_ids = _text_tuple_from_value(row.get("mapping_ids"))
    source_family_ids = _text_tuple_from_value(row.get("source_family_ids"))
    if raw_points > 0.0 and not support_claim_ids:
        return SourceBackedScoreContributionResult(
            **base,
            task_id=_score_contribution_result_id(task),
            result_status="orphan_score_blocked",
            component_key=component_key,
            criterion_id=criterion_id,
            raw_points=raw_points,
            max_points=max_points,
            blocked_reason="nonzero_score_without_support_claim_ids",
            reasons=("nonzero_score_without_support_claim_ids",),
        )
    try:
        contribution = ScoreContributionV2.build(
            component_key=component_key,
            criterion_id=criterion_id,
            raw_points=raw_points,
            max_points=max_points,
            support_claim_ids=support_claim_ids,
            counter_claim_ids=counter_claim_ids,
            mapping_ids=mapping_ids,
            source_family_ids=source_family_ids,
            cap_reason=_optional_text(row.get("cap_reason")),
            rationale=_optional_text(row.get("rationale")) or "",
        )
    except Exception as exc:
        return SourceBackedScoreContributionResult(
            **base,
            task_id=_score_contribution_result_id(task),
            result_status="invalid_score_contribution_output",
            component_key=component_key,
            criterion_id=criterion_id,
            raw_points=raw_points,
            max_points=max_points,
            blocked_reason=str(exc)[:180],
            reasons=("score_contribution_build_failed",),
        )
    return SourceBackedScoreContributionResult(
        **base,
        task_id=_score_contribution_result_id(task),
        result_status="score_contribution_ready",
        component_key=component_key,
        criterion_id=criterion_id,
        raw_points=raw_points,
        max_points=max_points,
        contribution_id=contribution.contribution_id,
        support_claim_ids=contribution.support_claim_ids,
        counter_claim_ids=contribution.counter_claim_ids,
        mapping_ids=contribution.mapping_ids,
        source_family_ids=contribution.source_family_ids,
        cap_reason=contribution.cap_reason,
        rationale=contribution.rationale,
        score_contribution_ready=True,
        production_score_fixture=False,
        reasons=("score_contribution_v2_built_but_not_production_stage_input",),
    )


def _score_contribution_result_base(task: Mapping[str, Any]) -> Mapping[str, Any]:
    return {
        "score_contribution_task_id": _optional_text(task.get("task_id")) or "",
        "eligibility_result_id": _optional_text(task.get("eligibility_result_id")) or "",
        "raw_assertion_id": _optional_text(task.get("raw_assertion_id")) or "",
        "fixture_seed_id": _optional_text(task.get("fixture_seed_id")) or "",
        "candidate_id": _optional_text(task.get("candidate_id")) or "",
        "archetype_id": _optional_text(task.get("archetype_id")) or "",
        "target_entity_id": _optional_text(task.get("target_entity_id")) or "",
        "subject_entity_id": _optional_text(task.get("subject_entity_id")) or "",
        "document_id": _optional_text(task.get("document_id")) or "",
        "anchor_id": _optional_text(task.get("anchor_id")) or "",
        "primitive_id": _optional_text(task.get("primitive_id")) or "",
        "support_direction": _optional_text(task.get("support_direction")) or "",
    }


def _score_contribution_result_id(task: Mapping[str, Any]) -> str:
    return "SCRES-" + hashlib.sha1(
        "|".join(
            (
                _optional_text(task.get("task_id")) or "",
                _optional_text(task.get("eligibility_result_id")) or "",
                _optional_text(task.get("primitive_id")) or "",
            )
        ).encode("utf-8")
    ).hexdigest()[:20]


def _score_snapshot_task_for_group(
    key: tuple[str, str, str, str],
    rows: Sequence[Mapping[str, Any]],
) -> SourceBackedScoreSnapshotTask | None:
    ready_rows = [
        row
        for row in rows
        if _optional_text(row.get("result_status")) == "score_contribution_ready"
        and _optional_bool(row.get("score_contribution_ready")) is True
    ]
    if not ready_rows or len(ready_rows) != len(rows):
        return None
    fixture_seed_id, candidate_id, archetype_id, target_entity_id = key
    contribution_ids = tuple(
        sorted(
            {
                _optional_text(row.get("contribution_id")) or ""
                for row in ready_rows
                if _optional_text(row.get("contribution_id"))
            }
        )
    )
    if not contribution_ids:
        return None
    result_ids = tuple(sorted(_optional_text(row.get("task_id")) or "" for row in ready_rows))
    component_keys = tuple(
        sorted(
            {
                _optional_text(row.get("component_key")) or ""
                for row in ready_rows
                if _optional_text(row.get("component_key"))
            }
        )
    )
    support_claim_ids = tuple(
        sorted(
            {
                claim_id
                for row in ready_rows
                for claim_id in _text_tuple_from_value(row.get("support_claim_ids"))
            }
        )
    )
    mapping_ids = tuple(
        sorted({mapping_id for row in ready_rows for mapping_id in _text_tuple_from_value(row.get("mapping_ids"))})
    )
    source_family_ids = tuple(
        sorted(
            {
                source_family_id
                for row in ready_rows
                for source_family_id in _text_tuple_from_value(row.get("source_family_ids"))
            }
        )
    )
    return SourceBackedScoreSnapshotTask(
        task_id=_score_snapshot_task_id(
            candidate_id=candidate_id,
            archetype_id=archetype_id,
            contribution_ids=contribution_ids,
        ),
        fixture_seed_id=fixture_seed_id,
        candidate_id=candidate_id,
        archetype_id=archetype_id,
        target_entity_id=target_entity_id,
        contribution_ids=contribution_ids,
        score_contribution_result_ids=result_ids,
        component_keys=component_keys,
        support_claim_ids=support_claim_ids,
        mapping_ids=mapping_ids,
        source_family_ids=source_family_ids,
    )


def _score_snapshot_skip_row(
    key: tuple[str, str, str, str],
    rows: Sequence[Mapping[str, Any]],
) -> Mapping[str, Any]:
    fixture_seed_id, candidate_id, archetype_id, target_entity_id = key
    statuses = tuple(
        sorted(
            {
                _optional_text(row.get("result_status")) or "unknown"
                for row in rows
            }
        )
    )
    return {
        "fixture_seed_id": fixture_seed_id,
        "candidate_id": candidate_id,
        "archetype_id": archetype_id,
        "target_entity_id": target_entity_id,
        "ready_count": sum(
            1
            for row in rows
            if _optional_text(row.get("result_status")) == "score_contribution_ready"
            and _optional_bool(row.get("score_contribution_ready")) is True
        ),
        "result_count": len(rows),
        "result_statuses": statuses,
        "skip_reason": "score_contribution_results_not_all_ready",
        "production_score_fixture": False,
    }


def _score_snapshot_task_id(
    *,
    candidate_id: str,
    archetype_id: str,
    contribution_ids: Sequence[str],
) -> str:
    return "SSNAP-" + hashlib.sha1(
        "|".join((candidate_id, archetype_id, ",".join(contribution_ids))).encode("utf-8")
    ).hexdigest()[:20]


def _score_snapshot_result_for_task(
    task: Mapping[str, Any],
    row: Mapping[str, Any] | None,
    contribution_results_by_id: Mapping[str, Mapping[str, Any]],
) -> SourceBackedScoreSnapshotResult:
    base = _score_snapshot_result_base(task)
    if row is None:
        return SourceBackedScoreSnapshotResult(
            **base,
            task_id=_score_snapshot_result_id(task),
            result_status="score_snapshot_not_attempted",
            blocked_reason="score_snapshot_result_missing",
            reasons=("score_snapshot_result_missing",),
        )
    if _optional_bool(row.get("ok")) is False:
        reason = _optional_text(row.get("reason")) or "score_snapshot_provider_error"
        return SourceBackedScoreSnapshotResult(
            **base,
            task_id=_score_snapshot_result_id(task),
            result_status="invalid_score_snapshot_output",
            blocked_reason=reason,
            reasons=(reason,),
        )
    source = _optional_text(row.get("snapshot_source"))
    if source != "deterministic":
        return SourceBackedScoreSnapshotResult(
            **base,
            task_id=_score_snapshot_result_id(task),
            result_status="non_deterministic_score_snapshot_blocked",
            blocked_reason="snapshot_source_not_deterministic",
            reasons=("snapshot_source_not_deterministic",),
        )

    expected_contribution_ids = _text_tuple_from_value(task.get("contribution_ids"))
    row_contribution_ids = _text_tuple_from_value(row.get("contribution_ids"))
    if tuple(sorted(row_contribution_ids)) != tuple(sorted(expected_contribution_ids)):
        return SourceBackedScoreSnapshotResult(
            **base,
            task_id=_score_snapshot_result_id(task),
            result_status="contribution_set_mismatch",
            blocked_reason="score_snapshot_contribution_ids_do_not_match_task",
            reasons=("score_snapshot_contribution_ids_do_not_match_task",),
        )
    contribution_rows = [contribution_results_by_id.get(contribution_id) for contribution_id in expected_contribution_ids]
    if any(item is None for item in contribution_rows):
        return SourceBackedScoreSnapshotResult(
            **base,
            task_id=_score_snapshot_result_id(task),
            result_status="contribution_set_mismatch",
            blocked_reason="score_snapshot_references_missing_contribution_result",
            reasons=("score_snapshot_references_missing_contribution_result",),
        )
    computed_verified_score = sum(_optional_float(item.get("raw_points")) or 0.0 for item in contribution_rows if item)
    verified_score = _optional_float(row.get("verified_score"))
    if verified_score is None:
        return SourceBackedScoreSnapshotResult(
            **base,
            task_id=_score_snapshot_result_id(task),
            result_status="invalid_score_snapshot_output",
            blocked_reason="verified_score_missing",
            reasons=("verified_score_missing",),
        )
    if abs(verified_score - computed_verified_score) > 1e-9:
        return SourceBackedScoreSnapshotResult(
            **base,
            task_id=_score_snapshot_result_id(task),
            result_status="score_snapshot_sum_mismatch",
            verified_score=verified_score,
            potential_score_upper_bound=verified_score,
            blocked_reason="verified_score_does_not_equal_contribution_raw_sum",
            reasons=("verified_score_does_not_equal_contribution_raw_sum",),
        )

    unresolved_material_gap_points = _optional_float(row.get("unresolved_material_gap_points"))
    if unresolved_material_gap_points is None:
        unresolved_material_gap_points = 0.0
    if unresolved_material_gap_points < 0.0:
        return SourceBackedScoreSnapshotResult(
            **base,
            task_id=_score_snapshot_result_id(task),
            result_status="negative_material_gap_blocked",
            verified_score=verified_score,
            potential_score_upper_bound=verified_score,
            unresolved_material_gap_points=unresolved_material_gap_points,
            blocked_reason="unresolved_material_gap_points_negative",
            reasons=("unresolved_material_gap_points_negative",),
        )
    potential_score_upper_bound = verified_score + unresolved_material_gap_points
    return SourceBackedScoreSnapshotResult(
        **base,
        task_id=_score_snapshot_result_id(task),
        result_status="score_snapshot_ready",
        verified_score=verified_score,
        potential_score_upper_bound=potential_score_upper_bound,
        unresolved_material_gap_points=unresolved_material_gap_points,
        unresolved_hard_break_candidate=_optional_bool(row.get("unresolved_hard_break_candidate")) is True,
        provider_failed=_optional_bool(row.get("provider_failed")) is True,
        invalid_evidence=_optional_bool(row.get("invalid_evidence")) is True,
        score_interval_ready=True,
        score_blocked_until_stage_court=True,
        production_score_fixture=False,
        reasons=("score_interval_built_but_not_stage_court_input",),
    )


def _score_snapshot_result_base(task: Mapping[str, Any]) -> Mapping[str, Any]:
    return {
        "score_snapshot_task_id": _optional_text(task.get("task_id")) or "",
        "fixture_seed_id": _optional_text(task.get("fixture_seed_id")) or "",
        "candidate_id": _optional_text(task.get("candidate_id")) or "",
        "archetype_id": _optional_text(task.get("archetype_id")) or "",
        "target_entity_id": _optional_text(task.get("target_entity_id")) or "",
        "contribution_ids": _text_tuple_from_value(task.get("contribution_ids")),
        "component_keys": _text_tuple_from_value(task.get("component_keys")),
        "support_claim_ids": _text_tuple_from_value(task.get("support_claim_ids")),
        "mapping_ids": _text_tuple_from_value(task.get("mapping_ids")),
        "source_family_ids": _text_tuple_from_value(task.get("source_family_ids")),
    }


def _score_snapshot_result_id(task: Mapping[str, Any]) -> str:
    return "SSRES-" + hashlib.sha1(
        "|".join(
            (
                _optional_text(task.get("task_id")) or "",
                _optional_text(task.get("candidate_id")) or "",
                ",".join(_text_tuple_from_value(task.get("contribution_ids"))),
            )
        ).encode("utf-8")
    ).hexdigest()[:20]


def _contribution_results_by_contribution_id(
    score_contribution_result_manifest: Mapping[str, Any],
) -> Mapping[str, Mapping[str, Any]]:
    return {
        _optional_text(row.get("contribution_id")) or "": row
        for row in score_contribution_result_manifest.get("results") or ()
        if isinstance(row, Mapping) and _optional_text(row.get("contribution_id"))
    }


def _stage_court_task_for_score_snapshot_result(
    result: Mapping[str, Any],
    *,
    contribution_results_by_id: Mapping[str, Mapping[str, Any]],
    contracts_by_archetype: Mapping[str, EvidenceContractV2],
) -> SourceBackedStageCourtTask | None:
    if _optional_text(result.get("result_status")) != "score_snapshot_ready" or not _optional_bool(
        result.get("score_interval_ready")
    ):
        return None
    archetype_id = _optional_text(result.get("archetype_id")) or ""
    if archetype_id not in contracts_by_archetype:
        return None
    contribution_ids = _text_tuple_from_value(result.get("contribution_ids"))
    primitive_ids, present_primitive_ids = _primitive_ids_from_contribution_results(
        contribution_ids,
        contribution_results_by_id=contribution_results_by_id,
    )
    if not primitive_ids:
        return None
    verified_score = _optional_float(result.get("verified_score")) or 0.0
    potential_score_upper_bound = _optional_float(result.get("potential_score_upper_bound"))
    if potential_score_upper_bound is None:
        potential_score_upper_bound = verified_score
    return SourceBackedStageCourtTask(
        task_id=_stage_court_task_id(result),
        score_snapshot_result_id=_optional_text(result.get("task_id")) or "",
        score_snapshot_task_id=_optional_text(result.get("score_snapshot_task_id")) or "",
        fixture_seed_id=_optional_text(result.get("fixture_seed_id")) or "",
        candidate_id=_optional_text(result.get("candidate_id")) or "",
        archetype_id=archetype_id,
        target_entity_id=_optional_text(result.get("target_entity_id")) or "",
        verified_score=verified_score,
        potential_score_upper_bound=potential_score_upper_bound,
        unresolved_hard_break_candidate=_optional_bool(result.get("unresolved_hard_break_candidate")) is True,
        provider_failed=_optional_bool(result.get("provider_failed")) is True,
        invalid_evidence=_optional_bool(result.get("invalid_evidence")) is True,
        contribution_ids=contribution_ids,
        primitive_ids=primitive_ids,
        present_primitive_ids=present_primitive_ids,
        support_claim_ids=_text_tuple_from_value(result.get("support_claim_ids")),
        component_keys=_text_tuple_from_value(result.get("component_keys")),
    )


def _stage_court_task_skip_row(
    result: Mapping[str, Any],
    *,
    contracts_by_archetype: Mapping[str, EvidenceContractV2],
) -> Mapping[str, Any]:
    archetype_id = _optional_text(result.get("archetype_id")) or ""
    if _optional_text(result.get("result_status")) != "score_snapshot_ready" or not _optional_bool(
        result.get("score_interval_ready")
    ):
        skip_reason = "score_interval_not_ready"
    elif archetype_id not in contracts_by_archetype:
        skip_reason = "evidence_contract_missing"
    else:
        skip_reason = "primitive_state_missing"
    return {
        "score_snapshot_result_id": _optional_text(result.get("task_id")) or "",
        "score_snapshot_task_id": _optional_text(result.get("score_snapshot_task_id")) or "",
        "candidate_id": _optional_text(result.get("candidate_id")) or "",
        "archetype_id": archetype_id,
        "result_status": _optional_text(result.get("result_status")) or "",
        "skip_reason": skip_reason,
        "production_score_fixture": False,
        "production_stage_fixture": False,
    }


def _stage_court_result_for_task(
    task: Mapping[str, Any],
    *,
    contribution_results_by_id: Mapping[str, Mapping[str, Any]],
    contracts_by_archetype: Mapping[str, EvidenceContractV2],
) -> SourceBackedStageCourtResult:
    base = _stage_court_result_base(task)
    archetype_id = _optional_text(task.get("archetype_id")) or ""
    contract = contracts_by_archetype.get(archetype_id)
    if contract is None:
        return SourceBackedStageCourtResult(
            **base,
            task_id=_stage_court_result_id(task),
            result_status="evidence_contract_missing",
            blocked_reason="evidence_contract_missing",
            reasons=("evidence_contract_missing",),
        )
    contribution_ids = _text_tuple_from_value(task.get("contribution_ids"))
    primitive_states = _primitive_states_from_contribution_results(
        contribution_ids,
        contribution_results_by_id=contribution_results_by_id,
        contract=contract,
    )
    try:
        output = decide_stage_court(
            StageCourtInput(
                score_interval=ScoreInterval(
                    verified_score=_optional_float(task.get("verified_score")) or 0.0,
                    potential_score_upper_bound=_optional_float(task.get("potential_score_upper_bound")) or 0.0,
                    unresolved_hard_break_candidate=_optional_bool(
                        task.get("unresolved_hard_break_candidate")
                    ) is True,
                    provider_failed=_optional_bool(task.get("provider_failed")) is True,
                    invalid_evidence=_optional_bool(task.get("invalid_evidence")) is True,
                ),
                primitive_states=primitive_states,
                contract=contract,
            )
        )
    except Exception as exc:
        return SourceBackedStageCourtResult(
            **base,
            task_id=_stage_court_result_id(task),
            result_status="stage_court_failed",
            blocked_reason=str(exc)[:180],
            reasons=("stage_court_failed",),
        )
    return SourceBackedStageCourtResult(
        **base,
        task_id=_stage_court_result_id(task),
        result_status="stage_court_ready",
        score_status=output.score_status.value,
        base_stage=output.decision.base_stage.value,
        canonical_stage=output.decision.canonical_stage(),
        investigation_status=output.decision.investigation_status.value,
        transition_overlay=output.decision.transition_overlay.value,
        present_green_primitives=output.present_green_primitives,
        missing_green_primitives=output.missing_green_primitives,
        stage_court_ready=True,
        production_score_fixture=False,
        production_stage_fixture=False,
        reasons=output.reasons,
    )


def _stage_court_result_base(task: Mapping[str, Any]) -> Mapping[str, Any]:
    return {
        "stage_court_task_id": _optional_text(task.get("task_id")) or "",
        "score_snapshot_result_id": _optional_text(task.get("score_snapshot_result_id")) or "",
        "fixture_seed_id": _optional_text(task.get("fixture_seed_id")) or "",
        "candidate_id": _optional_text(task.get("candidate_id")) or "",
        "archetype_id": _optional_text(task.get("archetype_id")) or "",
        "target_entity_id": _optional_text(task.get("target_entity_id")) or "",
        "verified_score": _optional_float(task.get("verified_score")) or 0.0,
        "potential_score_upper_bound": _optional_float(task.get("potential_score_upper_bound")) or 0.0,
    }


def _primitive_ids_from_contribution_results(
    contribution_ids: Sequence[str],
    *,
    contribution_results_by_id: Mapping[str, Mapping[str, Any]],
) -> tuple[tuple[str, ...], tuple[str, ...]]:
    primitive_ids: set[str] = set()
    present_primitive_ids: set[str] = set()
    for contribution_id in contribution_ids:
        row = contribution_results_by_id.get(contribution_id)
        if row is None:
            continue
        primitive_ids_from_row = _primitive_ids_from_contribution_row(row)
        if not primitive_ids_from_row:
            continue
        primitive_ids.update(primitive_ids_from_row)
        raw_points = _optional_float(row.get("raw_points")) or 0.0
        present_from_row = _text_tuple_from_value(row.get("present_primitive_ids"))
        if present_from_row:
            present_primitive_ids.update(item for item in present_from_row if item in primitive_ids_from_row)
        elif raw_points > 0.0 and _text_tuple_from_value(row.get("support_claim_ids")):
            present_primitive_ids.update(primitive_ids_from_row)
    return tuple(sorted(primitive_ids)), tuple(sorted(present_primitive_ids))


def _primitive_states_from_contribution_results(
    contribution_ids: Sequence[str],
    *,
    contribution_results_by_id: Mapping[str, Mapping[str, Any]],
    contract: EvidenceContractV2,
) -> Mapping[str, PrimitiveStateV2]:
    rows_by_primitive: dict[str, list[Mapping[str, Any]]] = {}
    for contribution_id in contribution_ids:
        row = contribution_results_by_id.get(contribution_id)
        if row is None:
            continue
        embedded_states = row.get("primitive_states")
        if isinstance(embedded_states, Sequence) and not isinstance(embedded_states, (str, bytes, bytearray)):
            for state_row in embedded_states:
                if not isinstance(state_row, Mapping):
                    continue
                primitive_id = _optional_text(state_row.get("primitive_id"))
                if primitive_id:
                    rows_by_primitive.setdefault(primitive_id, []).append(state_row)
            continue
        for primitive_id in _primitive_ids_from_contribution_row(row):
            rows_by_primitive.setdefault(primitive_id, []).append(row)
    states: dict[str, PrimitiveStateV2] = {}
    for primitive_id in set(contract.required_primitives) | set(rows_by_primitive):
        rows = rows_by_primitive.get(primitive_id, [])
        support_claim_ids = tuple(
            sorted({claim_id for row in rows for claim_id in _text_tuple_from_value(row.get("support_claim_ids"))})
        )
        counter_claim_ids = tuple(
            sorted({claim_id for row in rows for claim_id in _text_tuple_from_value(row.get("counter_claim_ids"))})
        )
        source_family_ids = tuple(
            sorted(
                {
                    source_family_id
                    for row in rows
                    for source_family_id in (
                        _text_tuple_from_value(row.get("source_family_ids"))
                        or _text_tuple_from_value(row.get("support_source_family_ids"))
                    )
                }
            )
        )
        mapping_ids = tuple(
            sorted(
                {
                    mapping_id
                    for row in rows
                    for mapping_id in (
                        _text_tuple_from_value(row.get("mapping_ids"))
                        or _text_tuple_from_value(row.get("support_mapping_ids"))
                    )
                }
            )
        )
        positive_points = sum(_optional_float(row.get("raw_points")) or 0.0 for row in rows)
        state_statuses = {_optional_text(row.get("status")) for row in rows if _optional_text(row.get("status"))}
        if support_claim_ids and counter_claim_ids:
            status = PrimitiveStatus.CONTRADICTED
        elif support_claim_ids and (
            positive_points > 0.0 or PrimitiveStatus.PRESENT_CURRENT.value in state_statuses
        ):
            status = PrimitiveStatus.PRESENT_CURRENT
        elif counter_claim_ids and PrimitiveStatus.ABSENT_EXPLICITLY_CONFIRMED.value in state_statuses:
            status = PrimitiveStatus.ABSENT_EXPLICITLY_CONFIRMED
        else:
            status = PrimitiveStatus.UNKNOWN
        states[primitive_id] = PrimitiveStateV2(
            primitive_id=primitive_id,
            status=status,
            support_claim_ids=support_claim_ids,
            counter_claim_ids=counter_claim_ids,
            support_source_family_ids=source_family_ids,
            support_mapping_ids=mapping_ids,
        )
    return states


def _primitive_ids_from_contribution_row(row: Mapping[str, Any]) -> tuple[str, ...]:
    primitive_ids = _text_tuple_from_value(row.get("primitive_ids"))
    if primitive_ids:
        return primitive_ids
    primitive_id = _optional_text(row.get("primitive_id"))
    return (primitive_id,) if primitive_id else ()


def _stage_court_task_id(result: Mapping[str, Any]) -> str:
    return "SCT-" + hashlib.sha1(
        "|".join(
            (
                _optional_text(result.get("task_id")) or "",
                _optional_text(result.get("candidate_id")) or "",
                _optional_text(result.get("archetype_id")) or "",
            )
        ).encode("utf-8")
    ).hexdigest()[:20]


def _stage_court_result_id(task: Mapping[str, Any]) -> str:
    return "SCRESLT-" + hashlib.sha1(
        "|".join(
            (
                _optional_text(task.get("task_id")) or "",
                _optional_text(task.get("candidate_id")) or "",
                _optional_text(task.get("archetype_id")) or "",
            )
        ).encode("utf-8")
    ).hexdigest()[:20]


def _summary_int(manifest: Mapping[str, Any], key: str) -> int:
    summary = manifest.get("summary")
    if not isinstance(summary, Mapping):
        return 0
    return int(summary.get(key) or 0)


def _summary_count(manifest: Mapping[str, Any], summary_key: str, collection_key: str) -> int:
    value = _summary_int(manifest, summary_key)
    if value:
        return value
    collection = manifest.get(collection_key)
    if isinstance(collection, Sequence) and not isinstance(collection, (str, bytes, bytearray)):
        return len(collection)
    return 0


def _claim_replay_chain_first_blocker(
    *,
    claim_replay_result_manifest: Mapping[str, Any],
    adjudication_result_manifest: Mapping[str, Any],
    primitive_mapping_result_manifest: Mapping[str, Any],
    eligibility_result_manifest: Mapping[str, Any],
    score_contribution_result_manifest: Mapping[str, Any],
    score_snapshot_result_manifest: Mapping[str, Any],
    stage_court_result_manifest: Mapping[str, Any],
    production_score_total: int,
    production_stage_total: int,
) -> tuple[str, str]:
    if production_score_total or production_stage_total:
        return "production_cutover_guard", "production_fixture_present_before_cutover"
    stages = (
        (
            "claim_replay",
            claim_replay_result_manifest,
            "task_count",
            "adjudication_ready_count",
            "no_claim_replay_tasks",
            "no_claim_replay_ready_results",
        ),
        (
            "adjudication",
            adjudication_result_manifest,
            "task_count",
            "mapping_ready_count",
            "no_adjudication_tasks",
            "no_mapping_ready_adjudications",
        ),
        (
            "primitive_mapping",
            primitive_mapping_result_manifest,
            "result_count",
            "eligibility_ready_count",
            "no_primitive_mapping_results",
            "no_eligibility_ready_mappings",
        ),
        (
            "eligibility",
            eligibility_result_manifest,
            "task_count",
            "score_contribution_ready_count",
            "no_eligibility_tasks",
            "no_score_contribution_ready_eligibility_results",
        ),
        (
            "score_contribution",
            score_contribution_result_manifest,
            "task_count",
            "score_contribution_ready_count",
            "no_score_contribution_tasks",
            "no_score_contribution_ready_results",
        ),
        (
            "score_snapshot",
            score_snapshot_result_manifest,
            "task_count",
            "score_interval_ready_count",
            "no_score_snapshot_tasks",
            "no_score_interval_ready_results",
        ),
        (
            "stage_court",
            stage_court_result_manifest,
            "task_count",
            "stage_court_ready_count",
            "no_stage_court_tasks",
            "no_stage_court_ready_results",
        ),
    )
    for stage_name, manifest, total_key, ready_key, no_total_reason, no_ready_reason in stages:
        if _summary_int(manifest, total_key) <= 0:
            return stage_name, no_total_reason
        if _summary_int(manifest, ready_key) <= 0:
            return stage_name, no_ready_reason
    return "production_cutover_acceptance", "production_cutover_requires_full_replay_acceptance"


def _claim_replay_readiness_first_blocker(
    *,
    claim_replay_task_count: int,
    fixture_not_ready_count: int,
    replacement_fixture_row_count: int,
    replacement_fixture_ready_count: int,
    replacement_snapshot_not_verified_count: int,
    verification_row_count: int,
    fetch_not_ready_count: int,
    snapshot_verified_count: int,
    fetch_task_count: int,
    fetch_failed_count: int,
    fetch_not_attempted_count: int,
    current_text_available_count: int,
) -> tuple[str | None, str | None]:
    if claim_replay_task_count > 0:
        return "claim_replay", "claim_replay_tasks_ready"
    if fetch_failed_count > 0:
        return "replacement_candidate_fetch", "replacement_candidate_fetch_failed"
    if fetch_not_attempted_count > 0:
        return "replacement_candidate_fetch", "replacement_candidate_fetch_not_attempted"
    if fetch_task_count > 0 and current_text_available_count <= 0:
        return "replacement_candidate_fetch", "replacement_candidate_current_text_missing"
    if verification_row_count > 0 and fetch_not_ready_count > 0:
        return "replacement_snapshot_verification", "replacement_snapshot_fetch_not_ready"
    if verification_row_count > 0 and snapshot_verified_count <= 0:
        return "replacement_snapshot_verification", "replacement_snapshot_not_verified"
    if replacement_fixture_row_count > 0 and replacement_fixture_ready_count <= 0:
        if replacement_snapshot_not_verified_count > 0:
            return "replacement_evidence_document_fixture", "replacement_snapshot_not_verified"
        return "replacement_evidence_document_fixture", "evidence_document_fixture_not_ready"
    if fixture_not_ready_count > 0:
        return "evidence_document_fixture", "evidence_document_fixture_not_ready"
    return "claim_replay", "no_claim_replay_tasks"


def _claim_replay_chain_audit_id(
    *,
    stage_court_ready_count: int,
    production_score_total: int,
    production_stage_total: int,
) -> str:
    return "CRAUD-" + hashlib.sha1(
        "|".join(
            (
                str(stage_court_ready_count),
                str(production_score_total),
                str(production_stage_total),
            )
        ).encode("utf-8")
    ).hexdigest()[:20]


def _claim_replay_readiness_audit_id(
    *,
    readiness_status: str,
    first_stage: str | None,
    first_reason: str | None,
) -> str:
    return "CRREADY-" + hashlib.sha1(
        "|".join((readiness_status, first_stage or "", first_reason or "")).encode("utf-8")
    ).hexdigest()[:20]


def _replacement_fetch_failure_audit_id(
    *,
    remediation_status: str,
    first_reason: str | None,
    task_count: int,
) -> str:
    return "RFAUD-" + hashlib.sha1(
        "|".join((remediation_status, first_reason or "", str(task_count))).encode("utf-8")
    ).hexdigest()[:20]


def _replacement_fetch_remediation_task_id(row: Mapping[str, Any], remediation_status: str) -> str:
    parts = (
        _optional_text(row.get("task_id")) or "",
        _optional_text(row.get("replacement_candidate_id")) or "",
        _optional_text(row.get("candidate_url")) or "",
        remediation_status,
    )
    return "RFREM-" + hashlib.sha1("|".join(parts).encode("utf-8")).hexdigest()[:20]


def _replacement_fetch_reason_groups(rows: Sequence[Mapping[str, Any]]) -> list[Mapping[str, Any]]:
    counts: dict[tuple[str, str], int] = {}
    for row in rows:
        status = _optional_text(row.get("fetch_status")) or "unknown_fetch_status"
        reason = _optional_text(row.get("reason")) or ""
        key = (status, reason)
        counts[key] = counts.get(key, 0) + 1
    return [
        {"fetch_status": status, "reason": reason or None, "count": count}
        for (status, reason), count in sorted(counts.items(), key=lambda item: (-item[1], item[0][0], item[0][1]))
    ]


def _replacement_fetch_remediation_task_for_fetch_row(
    row: Mapping[str, Any],
) -> SourceBackedReplacementFetchRemediationTask | None:
    fetch_status = _optional_text(row.get("fetch_status")) or ""
    reason = _optional_text(row.get("reason"))
    text_path = _optional_text(row.get("current_text_path"))
    text_hash = _optional_text(row.get("current_text_hash"))
    text_chars = _optional_int(row.get("current_text_chars")) or 0

    if fetch_status == "replacement_candidate_current_text_available_replacement_unverified":
        remediation_status = "snapshot_verification_required"
        remediation_action = "run_same_event_and_asof_snapshot_verification"
        priority = 30
        reasons = (
            "candidate_current_text_available_but_same_event_unverified",
            "candidate_current_text_available_but_asof_unverified",
        )
    elif fetch_status == "replacement_candidate_fetch_not_attempted":
        remediation_status = "bounded_fetch_required"
        remediation_action = "run_bounded_replacement_candidate_fetch"
        priority = 20
        reasons = ("replacement_candidate_fetch_not_attempted",)
    elif fetch_status == "replacement_candidate_fetch_failed":
        if text_path and text_hash and text_chars > 0:
            remediation_status = "snapshot_verification_required"
            remediation_action = "run_same_event_and_asof_snapshot_verification"
            priority = 30
            reasons = ("candidate_current_text_available_despite_failed_status",)
        else:
            remediation_status = "text_snapshot_required"
            remediation_action = "attach_fixture_text_or_run_bounded_replacement_fetch"
            priority = 10
            reasons = ("replacement_candidate_text_snapshot_required",)
    else:
        return None

    return SourceBackedReplacementFetchRemediationTask(
        task_id=_replacement_fetch_remediation_task_id(row, remediation_status),
        replacement_candidate_id=_optional_text(row.get("replacement_candidate_id")) or "",
        request_id=_optional_text(row.get("request_id")) or "",
        fixture_seed_id=_optional_text(row.get("fixture_seed_id")) or "",
        candidate_id=_optional_text(row.get("candidate_id")) or "",
        archetype_id=_optional_text(row.get("archetype_id")) or "",
        original_source_anchor=_optional_text(row.get("original_source_anchor")) or "",
        candidate_url=_optional_text(row.get("candidate_url")) or "",
        as_of_date=_optional_text(row.get("as_of_date")),
        fetch_status=fetch_status,
        remediation_status=remediation_status,
        remediation_action=remediation_action,
        priority=priority,
        max_total_fetches=3,
        stop_condition="source_text_snapshot_available_or_candidate_rejected",
        reason=reason,
        score_blocked_until_resolved=True,
        source_replacement_verified=False,
        asof_snapshot_verified=False,
        evidence_document_fixture_ready=False,
        production_score_fixture=False,
        reasons=reasons,
    )


def _asof_snapshot_acquisition_task_for_row(
    row: Mapping[str, Any],
    *,
    precheck_row: Mapping[str, Any] | None,
) -> SourceBackedAsofSnapshotAcquisitionTask:
    fixture_seed_id = _optional_text(row.get("fixture_seed_id")) or ""
    source_anchor = _optional_text(row.get("source_anchor")) or ""
    as_of_date = _optional_text(row.get("as_of_date"))
    task_type, priority, budgets, llm_required, reasons = _snapshot_acquisition_classification(
        remediation_type=_optional_text(row.get("remediation_type")),
        precheck_status=_optional_text((precheck_row or {}).get("precheck_status")),
    )
    task_id = "SACQ-" + hashlib.sha1(
        "|".join((fixture_seed_id, task_type, source_anchor, as_of_date or "")).encode("utf-8")
    ).hexdigest()[:20]
    return SourceBackedAsofSnapshotAcquisitionTask(
        task_id=task_id,
        fixture_seed_id=fixture_seed_id,
        candidate_id=_optional_text(row.get("candidate_id")) or "",
        archetype_id=_optional_text(row.get("archetype_id")) or "",
        source_anchor=source_anchor,
        as_of_date=as_of_date,
        task_type=task_type,
        priority=priority,
        date_window_start=None,
        date_window_end=as_of_date,
        max_archive_lookups=budgets["max_archive_lookups"],
        max_browser_fetches=budgets["max_browser_fetches"],
        max_alternative_source_candidates=budgets["max_alternative_source_candidates"],
        max_total_fetches=budgets["max_total_fetches"],
        stop_condition="asof_text_snapshot_verified_or_source_replaced",
        llm_followup_required=llm_required,
        score_blocked_until_verified=True,
        production_score_fixture=False,
        reasons=reasons,
    )


def _snapshot_acquisition_classification(
    *,
    remediation_type: str | None,
    precheck_status: str | None,
) -> tuple[str, int, Mapping[str, int], bool, tuple[str, ...]]:
    bounded_small = {
        "max_archive_lookups": 2,
        "max_browser_fetches": 1,
        "max_alternative_source_candidates": 1,
        "max_total_fetches": 3,
    }
    bounded_repair = {
        "max_archive_lookups": 2,
        "max_browser_fetches": 2,
        "max_alternative_source_candidates": 2,
        "max_total_fetches": 4,
    }
    if precheck_status == "date_hint_on_or_before_asof":
        return (
            "archive_identity_verify_candidate",
            10,
            bounded_small,
            False,
            ("date_hint_candidate_requires_archive_or_source_identity_verification",),
        )
    if precheck_status == "future_date_hint_blocks":
        return (
            "archive_or_metadata_disambiguation",
            20,
            bounded_small,
            False,
            ("future_date_hint_requires_archive_or_metadata_disambiguation",),
        )
    if precheck_status == "no_date_hint":
        return (
            "metadata_archive_date_lookup",
            25,
            bounded_small,
            False,
            ("no_date_hint_requires_metadata_or_archive_date_lookup",),
        )
    if remediation_type == "pdf_parser_repair":
        return (
            "pdf_binary_snapshot_repair",
            30,
            bounded_repair,
            False,
            ("pdf_source_requires_binary_snapshot_and_text_extraction_repair",),
        )
    if remediation_type == "dead_url_replacement":
        return (
            "dead_url_archive_or_replacement",
            35,
            bounded_repair,
            True,
            ("dead_url_requires_archive_or_llm_planned_replacement_source",),
        )
    if remediation_type == "archive_or_alternative_source":
        return (
            "archive_or_alternative_source",
            35,
            bounded_repair,
            True,
            ("access_blocked_or_unknown_failure_requires_archive_or_llm_planned_alternative",),
        )
    if remediation_type == "retry_current_fetch_with_browser_or_tls_repair":
        return (
            "bounded_retry_then_archive",
            40,
            bounded_repair,
            False,
            ("transport_failure_allows_bounded_retry_then_archive_lookup",),
        )
    return (
        "generic_source_snapshot_repair",
        50,
        bounded_repair,
        True,
        ("source_snapshot_repair_requires_manual_or_llm_followup_context",),
    )


def _verify_asof_snapshot_attempt(
    task: Mapping[str, Any],
    attempt: Mapping[str, Any] | None,
) -> SourceBackedAsofSnapshotVerificationResult:
    base_kwargs = {
        "task_id": _optional_text(task.get("task_id")) or "",
        "fixture_seed_id": _optional_text(task.get("fixture_seed_id")) or "",
        "candidate_id": _optional_text(task.get("candidate_id")) or "",
        "archetype_id": _optional_text(task.get("archetype_id")) or "",
        "source_anchor": _optional_text(task.get("source_anchor")) or "",
        "as_of_date": _optional_text(task.get("as_of_date")),
    }
    if attempt is None:
        return SourceBackedAsofSnapshotVerificationResult(
            **base_kwargs,
            verification_status="no_attempt_result",
            reasons=("no_snapshot_attempt_result_for_task",),
        )
    snapshot_url = _optional_text(attempt.get("snapshot_url") or attempt.get("canonical_url") or attempt.get("source_anchor"))
    snapshot_as_of_date = _optional_text(attempt.get("snapshot_as_of_date") or attempt.get("as_of_date"))
    text_path = _optional_text(attempt.get("extracted_text_path") or attempt.get("text_path"))
    text_hash = _optional_text(attempt.get("extracted_text_hash") or attempt.get("text_hash"))
    source_replacement_verified = _optional_bool(attempt.get("source_replacement_verified")) is True
    common = {
        **base_kwargs,
        "snapshot_url": snapshot_url,
        "snapshot_as_of_date": snapshot_as_of_date,
        "snapshot_source_type": _optional_text(attempt.get("snapshot_source_type") or attempt.get("source_type")),
        "snapshot_title": _optional_text(attempt.get("snapshot_title") or attempt.get("title")),
        "extracted_text_path": text_path,
        "extracted_text_hash": text_hash,
        "source_replacement_verified": source_replacement_verified,
    }
    if _optional_bool(attempt.get("ok")) is False:
        return SourceBackedAsofSnapshotVerificationResult(
            **common,
            verification_status="attempt_failed",
            reasons=(_optional_text(attempt.get("reason")) or "snapshot_attempt_failed",),
        )
    task_source_anchor = _optional_text(task.get("source_anchor")) or ""
    if not snapshot_url:
        return SourceBackedAsofSnapshotVerificationResult(
            **common,
            verification_status="source_anchor_mismatch",
            reasons=("snapshot_url_missing",),
        )
    if _normalise_url(snapshot_url) != _normalise_url(task_source_anchor) and not source_replacement_verified:
        return SourceBackedAsofSnapshotVerificationResult(
            **common,
            verification_status="source_anchor_mismatch",
            reasons=("snapshot_url_does_not_match_source_anchor_and_replacement_unverified",),
        )
    snapshot_date = _parse_iso_date(snapshot_as_of_date)
    as_of = _parse_iso_date(_optional_text(task.get("as_of_date")))
    if snapshot_date is None:
        return SourceBackedAsofSnapshotVerificationResult(
            **common,
            verification_status="invalid_snapshot_date",
            reasons=("snapshot_as_of_date_required",),
        )
    if as_of is not None and snapshot_date > as_of:
        return SourceBackedAsofSnapshotVerificationResult(
            **common,
            verification_status="future_snapshot_not_allowed",
            reasons=("snapshot_as_of_date_after_seed_as_of_date",),
        )
    if not text_path or not Path(text_path).exists():
        return SourceBackedAsofSnapshotVerificationResult(
            **common,
            verification_status="snapshot_text_missing",
            reasons=("snapshot_text_path_missing",),
        )
    text = Path(text_path).read_text(encoding="utf-8", errors="ignore")
    if not text.strip():
        return SourceBackedAsofSnapshotVerificationResult(
            **common,
            verification_status="empty_snapshot_text",
            reasons=("snapshot_text_empty",),
        )
    actual_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
    if _looks_like_sha256(text_hash) and text_hash != actual_hash:
        return SourceBackedAsofSnapshotVerificationResult(
            **common,
            verification_status="content_hash_mismatch",
            reasons=("snapshot_text_hash_mismatch",),
        )
    reasons = ["snapshot_attempt_verified_asof_text"]
    if source_replacement_verified:
        reasons.append("source_replacement_verified")
    if text_hash and not _looks_like_sha256(text_hash):
        reasons.append("snapshot_hash_label_replaced_by_computed_content_hash")
    verified_common = dict(common)
    verified_common["extracted_text_hash"] = actual_hash
    return SourceBackedAsofSnapshotVerificationResult(
        **verified_common,
        verification_status="asof_text_snapshot_verified",
        evidence_document_fixture_ready=True,
        production_score_fixture=False,
        reasons=tuple(reasons),
    )


def _asof_snapshot_verifier_task_for_acquisition_task(
    task: Mapping[str, Any],
    *,
    fetch_row: Mapping[str, Any] | None,
    precheck_row: Mapping[str, Any] | None,
) -> SourceBackedAsofSnapshotVerifierTask:
    acquisition_task_id = _optional_text(task.get("task_id")) or ""
    fixture_seed_id = _optional_text(task.get("fixture_seed_id")) or ""
    source_anchor = _optional_text(task.get("source_anchor")) or ""
    input_task_type = _optional_text(task.get("task_type")) or ""
    verifier_status, required_output, reasons = _asof_snapshot_verifier_task_classification(
        input_task_type=input_task_type,
        fetch_status=_optional_text((fetch_row or {}).get("current_fetch_status")),
        precheck_status=_optional_text((precheck_row or {}).get("precheck_status")),
        text_path=_optional_text((fetch_row or {}).get("current_text_path")),
        text_hash=_optional_text((fetch_row or {}).get("current_text_hash")),
        text_chars=_optional_int((fetch_row or {}).get("current_text_chars")) or 0,
    )
    verifier_task_id = "ASVFY-" + hashlib.sha1(
        "|".join((acquisition_task_id, fixture_seed_id, input_task_type, verifier_status)).encode("utf-8")
    ).hexdigest()[:20]
    return SourceBackedAsofSnapshotVerifierTask(
        verifier_task_id=verifier_task_id,
        acquisition_task_id=acquisition_task_id,
        fixture_seed_id=fixture_seed_id,
        candidate_id=_optional_text(task.get("candidate_id")) or "",
        archetype_id=_optional_text(task.get("archetype_id")) or "",
        source_anchor=source_anchor,
        as_of_date=_optional_text(task.get("as_of_date")),
        input_task_type=input_task_type,
        verifier_task_status=verifier_status,
        required_output=required_output,
        snapshot_url=source_anchor,
        snapshot_source_type=_optional_text((fetch_row or {}).get("content_type")),
        extracted_text_path=_optional_text((fetch_row or {}).get("current_text_path")),
        extracted_text_hash=_optional_text((fetch_row or {}).get("current_text_hash")),
        extracted_text_chars=_optional_int((fetch_row or {}).get("current_text_chars")) or 0,
        date_hints=_text_tuple_from_value((precheck_row or {}).get("date_hints")),
        score_blocked_until_verified=True,
        source_replacement_verified=False,
        asof_snapshot_verified=False,
        evidence_document_fixture_ready=False,
        production_score_fixture=False,
        reasons=reasons,
    )


def _asof_snapshot_verifier_task_classification(
    *,
    input_task_type: str | None,
    fetch_status: str | None,
    precheck_status: str | None,
    text_path: str | None,
    text_hash: str | None,
    text_chars: int,
) -> tuple[str, str, tuple[str, ...]]:
    has_text_anchor = bool(
        fetch_status == "current_fetch_text_available_asof_unverified"
        and text_path
        and text_hash
        and text_chars > 0
    )
    if input_task_type == "metadata_archive_date_lookup" and precheck_status == "no_date_hint":
        if not has_text_anchor:
            return (
                "blocked_until_current_text_snapshot",
                "current_source_text_snapshot_required",
                ("metadata_date_lookup_requires_current_text_anchor",),
            )
        return (
            "ready_for_source_metadata_asof_verifier",
            "source_identity_and_metadata_asof_date_observation",
            ("current_text_without_date_hint_requires_metadata_asof_verifier_without_score_context",),
        )
    if input_task_type == "archive_or_metadata_disambiguation" and precheck_status == "future_date_hint_blocks":
        if not has_text_anchor:
            return (
                "blocked_until_current_text_snapshot",
                "current_source_text_snapshot_required",
                ("metadata_disambiguation_requires_current_text_anchor",),
            )
        return (
            "ready_for_source_metadata_asof_verifier",
            "source_identity_and_metadata_asof_date_observation",
            ("future_date_hint_requires_metadata_asof_verifier_without_score_context",),
        )
    if input_task_type != "archive_identity_verify_candidate":
        return (
            "blocked_non_identity_verify_task",
            "source_snapshot_repair_or_replacement",
            ("only_archive_identity_verify_candidate_is_safe_for_current_text_verifier",),
        )
    if precheck_status != "date_hint_on_or_before_asof":
        return (
            "blocked_until_asof_precheck_candidate",
            "archive_or_metadata_date_disambiguation",
            ("current_text_date_hint_not_prechecked_on_or_before_asof",),
        )
    if not has_text_anchor:
        return (
            "blocked_until_current_text_snapshot",
            "current_source_text_snapshot_required",
            ("current_text_snapshot_missing_or_hash_unavailable",),
        )
    return (
        "ready_for_source_identity_asof_verifier",
        "source_identity_and_asof_date_observation",
        ("current_text_requires_source_identity_and_asof_verifier_without_score_context",),
    )


_FORBIDDEN_ASOF_SNAPSHOT_VERIFIER_RESULT_FIELDS = frozenset(
    {
        "verified",
        "current_score_eligible",
        "score_eligible",
        "source_replacement_verified",
        "asof_snapshot_verified",
        "evidence_document_fixture_ready",
        "production_score_fixture",
        "source_tier",
        "primitive_id",
        "candidate_primitive_id",
        "score",
        "stage",
        "evidence_contract",
        "missing_primitive",
        "score_gap",
        "current_score",
        "stage_gate",
        "green_gate",
    }
)


def _asof_snapshot_verifier_result_for_task(
    task: Mapping[str, Any],
    row: Mapping[str, Any] | None,
) -> SourceBackedAsofSnapshotVerifierResult:
    base = {
        "verifier_task_id": _optional_text(task.get("verifier_task_id") or task.get("task_id")) or "",
        "acquisition_task_id": _optional_text(task.get("acquisition_task_id")) or "",
        "fixture_seed_id": _optional_text(task.get("fixture_seed_id")) or "",
        "candidate_id": _optional_text(task.get("candidate_id")) or "",
        "archetype_id": _optional_text(task.get("archetype_id")) or "",
        "source_anchor": _optional_text(task.get("source_anchor")) or "",
        "as_of_date": _optional_text(task.get("as_of_date")),
        "snapshot_url": _optional_text(task.get("snapshot_url") or task.get("source_anchor")),
        "snapshot_source_type": _optional_text(task.get("snapshot_source_type")),
        "extracted_text_path": _optional_text(task.get("extracted_text_path")),
        "extracted_text_hash": _optional_text(task.get("extracted_text_hash")),
        "extracted_text_chars": _optional_int(task.get("extracted_text_chars")) or 0,
    }
    status = _optional_text(task.get("verifier_task_status")) or ""
    if status not in {"ready_for_source_identity_asof_verifier", "ready_for_source_metadata_asof_verifier"}:
        return SourceBackedAsofSnapshotVerifierResult(
            result_id=_asof_snapshot_verifier_result_id(task, "blocked_task_not_ready"),
            **base,
            result_status="blocked_task_not_ready",
            reasons=("asof_snapshot_verifier_task_not_ready",),
        )
    if row is None:
        return SourceBackedAsofSnapshotVerifierResult(
            result_id=_asof_snapshot_verifier_result_id(task, "no_verifier_result"),
            **base,
            result_status="no_verifier_result",
            reasons=("no_source_identity_asof_verifier_result",),
        )

    forbidden = tuple(sorted(_FORBIDDEN_ASOF_SNAPSHOT_VERIFIER_RESULT_FIELDS.intersection(row)))
    if forbidden:
        return SourceBackedAsofSnapshotVerifierResult(
            result_id=_asof_snapshot_verifier_result_id(task, "forbidden_output_field"),
            **base,
            result_status="forbidden_output_field",
            forbidden_output_fields=forbidden,
            reasons=("source_identity_asof_verifier_returned_forbidden_score_or_stage_field",),
        )

    if _optional_bool(row.get("ok")) is False:
        return SourceBackedAsofSnapshotVerifierResult(
            result_id=_asof_snapshot_verifier_result_id(task, "attempt_failed"),
            **base,
            result_status="attempt_failed",
            source_identity_decision=_optional_text(row.get("source_identity_decision")),
            reasons=(_optional_text(row.get("reason")) or "source_identity_asof_verifier_failed",),
        )

    source_identity_decision = _normalise_source_identity_decision(
        row.get("source_identity_decision")
        or row.get("same_source_decision")
        or row.get("source_match")
    )
    if source_identity_decision != "same_source":
        return SourceBackedAsofSnapshotVerifierResult(
            result_id=_asof_snapshot_verifier_result_id(task, "source_identity_unverified"),
            **base,
            result_status="source_identity_unverified",
            source_identity_decision=source_identity_decision,
            reasons=("source_identity_not_verified_for_original_anchor",),
        )

    snapshot_url = _optional_text(row.get("snapshot_url") or row.get("source_anchor")) or base["snapshot_url"]
    if _normalise_url(snapshot_url or "") != _normalise_url(base["source_anchor"] or ""):
        mismatch_base = {**base, "snapshot_url": snapshot_url}
        return SourceBackedAsofSnapshotVerifierResult(
            result_id=_asof_snapshot_verifier_result_id(task, "snapshot_url_mismatch"),
            **mismatch_base,
            result_status="snapshot_url_mismatch",
            source_identity_decision=source_identity_decision,
            reasons=("verifier_snapshot_url_does_not_match_source_anchor",),
        )

    snapshot_as_of_date = _optional_text(row.get("snapshot_as_of_date") or row.get("available_at"))
    snapshot_date = _parse_iso_date(snapshot_as_of_date)
    as_of = _parse_iso_date(base["as_of_date"])
    if snapshot_date is None:
        invalid_date_base = {**base, "snapshot_url": snapshot_url}
        return SourceBackedAsofSnapshotVerifierResult(
            result_id=_asof_snapshot_verifier_result_id(task, "invalid_snapshot_date"),
            **invalid_date_base,
            result_status="invalid_snapshot_date",
            source_identity_decision=source_identity_decision,
            snapshot_as_of_date=snapshot_as_of_date,
            reasons=("snapshot_as_of_date_required",),
        )
    if as_of is not None and snapshot_date > as_of:
        future_base = {**base, "snapshot_url": snapshot_url}
        return SourceBackedAsofSnapshotVerifierResult(
            result_id=_asof_snapshot_verifier_result_id(task, "future_snapshot_not_allowed"),
            **future_base,
            result_status="future_snapshot_not_allowed",
            source_identity_decision=source_identity_decision,
            snapshot_as_of_date=snapshot_as_of_date,
            reasons=("snapshot_as_of_date_after_seed_as_of_date",),
        )

    text_path = base["extracted_text_path"]
    if not text_path or not Path(text_path).exists():
        text_missing_base = {**base, "snapshot_url": snapshot_url}
        return SourceBackedAsofSnapshotVerifierResult(
            result_id=_asof_snapshot_verifier_result_id(task, "snapshot_text_missing"),
            **text_missing_base,
            result_status="snapshot_text_missing",
            source_identity_decision=source_identity_decision,
            snapshot_as_of_date=snapshot_as_of_date,
            reasons=("source_snapshot_text_path_missing",),
        )
    text = Path(text_path).read_text(encoding="utf-8", errors="ignore")
    if not text.strip():
        empty_base = {**base, "snapshot_url": snapshot_url}
        return SourceBackedAsofSnapshotVerifierResult(
            result_id=_asof_snapshot_verifier_result_id(task, "empty_snapshot_text"),
            **empty_base,
            result_status="empty_snapshot_text",
            source_identity_decision=source_identity_decision,
            snapshot_as_of_date=snapshot_as_of_date,
            reasons=("source_snapshot_text_empty",),
        )
    actual_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
    text_hash = base["extracted_text_hash"]
    if _looks_like_sha256(text_hash) and text_hash != actual_hash:
        mismatch_base = {**base, "snapshot_url": snapshot_url, "extracted_text_hash": actual_hash}
        return SourceBackedAsofSnapshotVerifierResult(
            result_id=_asof_snapshot_verifier_result_id(task, "content_hash_mismatch"),
            **mismatch_base,
            result_status="content_hash_mismatch",
            source_identity_decision=source_identity_decision,
            snapshot_as_of_date=snapshot_as_of_date,
            reasons=("source_snapshot_text_hash_mismatch",),
        )

    accepted_row = {
        "task_id": base["acquisition_task_id"],
        "verifier_task_id": base["verifier_task_id"],
        "fixture_seed_id": base["fixture_seed_id"],
        "ok": True,
        "source_identity_verified": True,
        "snapshot_url": snapshot_url,
        "snapshot_as_of_date": snapshot_as_of_date,
        "snapshot_source_type": _optional_text(row.get("snapshot_source_type") or row.get("source_type"))
        or base["snapshot_source_type"],
        "snapshot_title": _optional_text(row.get("snapshot_title") or row.get("title")),
        "extracted_text_path": text_path,
        "extracted_text_hash": actual_hash,
        "verifier_result_id": _asof_snapshot_verifier_result_id(task, "source_identity_asof_verified"),
    }
    verified_base = {
        **base,
        "snapshot_url": snapshot_url,
        "snapshot_source_type": accepted_row["snapshot_source_type"],
        "extracted_text_hash": actual_hash,
    }
    return SourceBackedAsofSnapshotVerifierResult(
        result_id=accepted_row["verifier_result_id"],
        **verified_base,
        result_status="source_identity_asof_verified",
        source_identity_decision=source_identity_decision,
        snapshot_as_of_date=snapshot_as_of_date,
        snapshot_title=accepted_row["snapshot_title"],
        source_replacement_verified=False,
        asof_snapshot_verified=True,
        evidence_document_fixture_ready=False,
        production_score_fixture=False,
        accepted_attempt_row=accepted_row,
        reasons=("source_identity_asof_verifier_result_passed_gate",),
    )


def _asof_snapshot_verifier_result_id(task: Mapping[str, Any], status: str) -> str:
    digest = hashlib.sha1(
        "|".join(
            (
                _optional_text(task.get("verifier_task_id") or task.get("task_id")) or "",
                _optional_text(task.get("fixture_seed_id")) or "",
                status,
            )
        ).encode("utf-8")
    ).hexdigest()[:20]
    return f"ASVRES-{digest}"


def _normalise_source_identity_decision(value: Any) -> str:
    text = str(value or "").strip().lower().replace("-", "_").replace(" ", "_")
    if text in {"same_source", "same", "source_match", "match", "matched", "true", "yes"}:
        return "same_source"
    if text in {"different_source", "not_same_source", "mismatch", "false", "no"}:
        return "different_source"
    return "unknown"


def _replacement_source_request_for_task(task: Mapping[str, Any]) -> SourceBackedReplacementSourceRequest:
    task_id = _optional_text(task.get("task_id")) or ""
    fixture_seed_id = _optional_text(task.get("fixture_seed_id")) or ""
    task_type = _optional_text(task.get("task_type")) or ""
    source_anchor = _optional_text(task.get("source_anchor")) or ""
    digest = hashlib.sha1("|".join((task_id, fixture_seed_id, task_type, source_anchor)).encode("utf-8")).hexdigest()[:20]
    return SourceBackedReplacementSourceRequest(
        request_id=f"SREPL-{digest}",
        task_id=task_id,
        fixture_seed_id=fixture_seed_id,
        candidate_id=_optional_text(task.get("candidate_id")) or "",
        archetype_id=_optional_text(task.get("archetype_id")) or "",
        source_anchor=source_anchor,
        as_of_date=_optional_text(task.get("as_of_date")),
        task_type=task_type,
        request_status="ready_for_llm_same_event_source_planning",
        llm_followup_required=True,
        deterministic_queries_generated=False,
        suggested_queries=(),
        production_score_fixture=False,
        reasons=("llm_must_plan_same_event_alternative_source_without_deterministic_query_template",),
    )


def _same_event_planner_run_for_request(
    request: Mapping[str, Any],
    *,
    provider: Any | None,
) -> tuple[SourceBackedReplacementPlannerRun, tuple[Mapping[str, Any], ...]]:
    base = _replacement_planner_run_base(request)
    if provider is None:
        return (
            SourceBackedReplacementPlannerRun(
                **base,
                planner_status="provider_not_configured",
                llm_called=False,
                reasons=("same_event_replacement_planner_provider_not_configured",),
            ),
            (),
        )
    try:
        output = provider.plan_same_event_replacement_sources((request,))
    except Exception as exc:  # pragma: no cover - defensive boundary around provider plugins
        return (
            SourceBackedReplacementPlannerRun(
                **base,
                planner_status="provider_error",
                llm_called=True,
                provider_error=f"{type(exc).__name__}:{str(exc)[:240]}",
                reasons=("same_event_replacement_planner_provider_exception",),
            ),
            (),
        )
    if not isinstance(output, Mapping):
        return (
            SourceBackedReplacementPlannerRun(
                **base,
                planner_status="provider_error",
                llm_called=True,
                provider_error="provider_returned_non_mapping_output",
                reasons=("same_event_replacement_planner_invalid_output",),
            ),
            (),
        )
    rows = tuple(_planner_output_rows_for_request(request, output))
    status = str(output.get("status") or "ok")
    if status == "provider_error":
        provider_error = (
            _optional_text(output.get("provider_error"))
            or _optional_text(output.get("blocked_reason"))
            or "provider_error_status"
        )
        return (
            SourceBackedReplacementPlannerRun(
                **base,
                planner_status="provider_error",
                llm_called=True,
                provider_error=provider_error,
                reasons=("same_event_replacement_planner_provider_error_status",),
            ),
            (),
        )
    if not rows:
        return (
            SourceBackedReplacementPlannerRun(
                **base,
                planner_status="planner_empty_output",
                llm_called=True,
                reasons=("same_event_replacement_planner_returned_no_candidate_sources",),
            ),
            (),
        )
    return (
        SourceBackedReplacementPlannerRun(
            **base,
            planner_status="planner_success",
            llm_called=True,
            candidate_source_count=len(rows),
            reasons=("same_event_replacement_planner_returned_candidate_sources",),
        ),
        rows,
    )


def _replacement_planner_run_base(request: Mapping[str, Any]) -> Mapping[str, Any]:
    request_id = _optional_text(request.get("request_id")) or ""
    fixture_seed_id = _optional_text(request.get("fixture_seed_id")) or ""
    source_anchor = _optional_text(request.get("source_anchor")) or ""
    digest = hashlib.sha1("|".join((request_id, fixture_seed_id, source_anchor)).encode("utf-8")).hexdigest()[:20]
    return {
        "run_id": f"SRUN-{digest}",
        "request_id": request_id,
        "fixture_seed_id": fixture_seed_id,
        "candidate_id": _optional_text(request.get("candidate_id")) or "",
        "archetype_id": _optional_text(request.get("archetype_id")) or "",
        "source_anchor": source_anchor,
        "as_of_date": _optional_text(request.get("as_of_date")),
        "production_score_fixture": False,
    }


def _planner_output_rows_for_request(
    request: Mapping[str, Any],
    output: Mapping[str, Any],
) -> Iterable[Mapping[str, Any]]:
    raw_sources = output.get("candidate_sources") or ()
    if not isinstance(raw_sources, Sequence) or isinstance(raw_sources, (str, bytes, bytearray)):
        return ()
    rows: list[Mapping[str, Any]] = []
    request_id = _optional_text(request.get("request_id")) or ""
    fixture_seed_id = _optional_text(request.get("fixture_seed_id")) or ""
    for item in raw_sources:
        if not isinstance(item, Mapping):
            continue
        rows.append(
            {
                "request_id": _optional_text(item.get("request_id")) or request_id,
                "fixture_seed_id": _optional_text(item.get("fixture_seed_id")) or fixture_seed_id,
                "candidate_url": _optional_text(item.get("candidate_url")),
                "candidate_title": _optional_text(item.get("candidate_title")),
                "candidate_available_date": _optional_text(item.get("candidate_available_date")),
                "source_type": _optional_text(item.get("source_type")),
                "rationale": _optional_text(item.get("rationale")) or "",
            }
        )
    return tuple(rows)


def _replacement_candidate_missing_output(request: Mapping[str, Any]) -> SourceBackedReplacementSourceCandidate:
    return _replacement_candidate_base(
        request,
        candidate_url=None,
        candidate_title=None,
        candidate_available_date=None,
        llm_rationale=None,
        candidate_status="no_llm_candidate_output",
        reasons=("no_llm_candidate_output_for_replacement_request",),
    )


def _replacement_candidate_from_planner_source(
    request: Mapping[str, Any],
    source: Mapping[str, Any],
) -> SourceBackedReplacementSourceCandidate:
    candidate_url = _optional_text(
        source.get("candidate_url")
        or source.get("source_url")
        or source.get("url")
        or source.get("canonical_url")
    )
    candidate_title = _optional_text(source.get("candidate_title") or source.get("title"))
    candidate_available_date = _optional_text(
        source.get("candidate_available_date")
        or source.get("available_at")
        or source.get("published_at")
        or source.get("as_of_date")
    )
    llm_rationale = _optional_text(source.get("rationale") or source.get("llm_rationale"))
    if not candidate_url:
        return _replacement_candidate_base(
            request,
            candidate_url=None,
            candidate_title=candidate_title,
            candidate_available_date=candidate_available_date,
            llm_rationale=llm_rationale,
            candidate_status="invalid_candidate_missing_url",
            reasons=("llm_candidate_missing_url",),
        )
    if _normalise_url(candidate_url) == _normalise_url(_optional_text(request.get("source_anchor")) or ""):
        return _replacement_candidate_base(
            request,
            candidate_url=candidate_url,
            candidate_title=candidate_title,
            candidate_available_date=candidate_available_date,
            llm_rationale=llm_rationale,
            candidate_status="invalid_candidate_same_as_blocked_source",
            reasons=("llm_candidate_repeated_blocked_source_anchor",),
        )
    as_of = _parse_iso_date(_optional_text(request.get("as_of_date")))
    candidate_date = _parse_iso_date(candidate_available_date)
    if as_of is not None and candidate_date is not None and candidate_date > as_of:
        return _replacement_candidate_base(
            request,
            candidate_url=candidate_url,
            candidate_title=candidate_title,
            candidate_available_date=candidate_available_date,
            llm_rationale=llm_rationale,
            candidate_status="candidate_after_asof_blocked",
            reasons=("llm_candidate_available_date_after_seed_as_of_date",),
        )
    return _replacement_candidate_base(
        request,
        candidate_url=candidate_url,
        candidate_title=candidate_title,
        candidate_available_date=candidate_available_date,
        llm_rationale=llm_rationale,
        candidate_status="replacement_candidate_unverified",
        reasons=("llm_candidate_requires_bounded_fetch_and_asof_verification",),
    )


def _replacement_candidate_base(
    request: Mapping[str, Any],
    *,
    candidate_url: str | None,
    candidate_title: str | None,
    candidate_available_date: str | None,
    llm_rationale: str | None,
    candidate_status: str,
    reasons: Sequence[str],
) -> SourceBackedReplacementSourceCandidate:
    request_id = _optional_text(request.get("request_id")) or ""
    fixture_seed_id = _optional_text(request.get("fixture_seed_id")) or ""
    source_anchor = _optional_text(request.get("source_anchor")) or ""
    digest = hashlib.sha1(
        "|".join((request_id, fixture_seed_id, candidate_url or candidate_status, candidate_available_date or "")).encode(
            "utf-8"
        )
    ).hexdigest()[:20]
    return SourceBackedReplacementSourceCandidate(
        request_id=request_id,
        fixture_seed_id=fixture_seed_id,
        candidate_id=_optional_text(request.get("candidate_id")) or "",
        archetype_id=_optional_text(request.get("archetype_id")) or "",
        original_source_anchor=source_anchor,
        as_of_date=_optional_text(request.get("as_of_date")),
        replacement_candidate_id=f"SRCAND-{digest}",
        candidate_url=candidate_url,
        candidate_title=candidate_title,
        candidate_available_date=candidate_available_date,
        llm_rationale=llm_rationale,
        candidate_status=candidate_status,
        source_replacement_verified=False,
        asof_snapshot_verified=False,
        evidence_document_fixture_ready=False,
        production_score_fixture=False,
        reasons=tuple(dict.fromkeys(str(item).strip() for item in reasons if str(item).strip())),
    )


def _replacement_candidate_rows_from_planner_row(row: Mapping[str, Any]) -> tuple[Mapping[str, Any], ...]:
    raw_sources = row.get("candidate_sources")
    if isinstance(raw_sources, Sequence) and not isinstance(raw_sources, (str, bytes, bytearray)):
        sources = tuple(source for source in raw_sources if isinstance(source, Mapping))
        if sources:
            return sources
    return (row,)


def _replacement_candidate_fetch_key(candidate_url: str, as_of_date: str | None) -> tuple[str | None, str | None]:
    normalised = _normalise_url(candidate_url)
    if normalised:
        parts = parse.urlsplit(normalised)
        if parts.scheme and parts.netloc:
            path = parts.path.rstrip("/") or "/"
            normalised = parse.urlunsplit((parts.scheme, parts.netloc, path, parts.query, ""))
    return normalised, as_of_date


def _replacement_candidate_acquisition_task(
    candidate: Mapping[str, Any],
    *,
    candidate_url: str,
) -> SourceBackedReplacementCandidateAcquisitionTask:
    replacement_candidate_id = _optional_text(candidate.get("replacement_candidate_id")) or ""
    fixture_seed_id = _optional_text(candidate.get("fixture_seed_id")) or ""
    as_of_date = _optional_text(candidate.get("as_of_date"))
    digest = hashlib.sha1(
        "|".join((replacement_candidate_id, fixture_seed_id, candidate_url, as_of_date or "")).encode("utf-8")
    ).hexdigest()[:20]
    return SourceBackedReplacementCandidateAcquisitionTask(
        task_id=f"RCACQ-{digest}",
        replacement_candidate_id=replacement_candidate_id,
        request_id=_optional_text(candidate.get("request_id")) or "",
        fixture_seed_id=fixture_seed_id,
        candidate_id=_optional_text(candidate.get("candidate_id")) or "",
        archetype_id=_optional_text(candidate.get("archetype_id")) or "",
        original_source_anchor=_optional_text(candidate.get("original_source_anchor")) or "",
        candidate_url=candidate_url,
        as_of_date=as_of_date,
        task_type="replacement_candidate_bounded_fetch_and_archive",
        priority=20,
        date_window_start=None,
        date_window_end=as_of_date,
        max_archive_lookups=2,
        max_browser_fetches=1,
        max_total_fetches=3,
        stop_condition="candidate_source_text_snapshot_verified_or_candidate_rejected",
        score_blocked_until_verified=True,
        source_replacement_verified=False,
        asof_snapshot_verified=False,
        evidence_document_fixture_ready=False,
        production_score_fixture=False,
        reasons=("replacement_candidate_requires_bounded_acquisition_and_asof_verification",),
    )


def _replacement_candidate_fetch_status_for_task(
    task: Mapping[str, Any],
    fetch: Mapping[str, Any] | None,
) -> SourceBackedReplacementCandidateFetchStatus:
    base = {
        "task_id": _optional_text(task.get("task_id")) or "",
        "replacement_candidate_id": _optional_text(task.get("replacement_candidate_id")) or "",
        "request_id": _optional_text(task.get("request_id")) or "",
        "fixture_seed_id": _optional_text(task.get("fixture_seed_id")) or "",
        "candidate_id": _optional_text(task.get("candidate_id")) or "",
        "archetype_id": _optional_text(task.get("archetype_id")) or "",
        "original_source_anchor": _optional_text(task.get("original_source_anchor")) or "",
        "candidate_url": _optional_text(task.get("candidate_url")) or "",
        "as_of_date": _optional_text(task.get("as_of_date")),
    }
    if fetch is None:
        return SourceBackedReplacementCandidateFetchStatus(
            **base,
            fetch_status="replacement_candidate_fetch_not_attempted",
            reasons=("no_replacement_candidate_fetch_attempt_result",),
        )

    text_path = _optional_text(fetch.get("current_text_path") or fetch.get("text_path") or fetch.get("extracted_text_path"))
    text_hash = _optional_text(fetch.get("current_text_hash") or fetch.get("text_hash") or fetch.get("extracted_text_hash"))
    text_chars = _optional_int(fetch.get("current_text_chars") or fetch.get("text_chars")) or 0
    common = {
        **base,
        "fetched_at": _optional_text(fetch.get("fetched_at")),
        "content_type": _optional_text(fetch.get("content_type")),
        "current_text_path": text_path,
        "current_text_hash": text_hash,
        "current_text_chars": text_chars,
    }
    if _optional_bool(fetch.get("ok")) is False:
        return SourceBackedReplacementCandidateFetchStatus(
            **common,
            fetch_status="replacement_candidate_fetch_failed",
            reason=_optional_text(fetch.get("reason")) or "replacement_candidate_fetch_failed",
            reasons=("replacement_candidate_fetch_failed",),
        )
    if _optional_bool(fetch.get("ok")) is True and text_path and text_hash and text_chars > 0:
        return SourceBackedReplacementCandidateFetchStatus(
            **common,
            fetch_status="replacement_candidate_current_text_available_replacement_unverified",
            source_replacement_verified=False,
            asof_snapshot_verified=False,
            evidence_document_fixture_ready=False,
            production_score_fixture=False,
            reasons=(
                "candidate_current_text_available_but_same_event_unverified",
                "candidate_current_text_available_but_asof_unverified",
            ),
        )
    return SourceBackedReplacementCandidateFetchStatus(
        **common,
        fetch_status="replacement_candidate_fetch_failed",
        reason=_optional_text(fetch.get("reason")) or "replacement_candidate_fetch_result_missing_text_snapshot",
        reasons=("replacement_candidate_fetch_result_missing_text_snapshot",),
    )


def _replacement_snapshot_verification_for_fetch_row(
    fetch_row: Mapping[str, Any],
    verification: Mapping[str, Any] | None,
) -> SourceBackedReplacementSnapshotVerificationResult:
    base = {
        "task_id": _optional_text(fetch_row.get("task_id")) or "",
        "replacement_candidate_id": _optional_text(fetch_row.get("replacement_candidate_id")) or "",
        "request_id": _optional_text(fetch_row.get("request_id")) or "",
        "fixture_seed_id": _optional_text(fetch_row.get("fixture_seed_id")) or "",
        "candidate_id": _optional_text(fetch_row.get("candidate_id")) or "",
        "archetype_id": _optional_text(fetch_row.get("archetype_id")) or "",
        "original_source_anchor": _optional_text(fetch_row.get("original_source_anchor")) or "",
        "candidate_url": _optional_text(fetch_row.get("candidate_url")) or "",
        "as_of_date": _optional_text(fetch_row.get("as_of_date")),
    }
    if fetch_row.get("fetch_status") != "replacement_candidate_current_text_available_replacement_unverified":
        return SourceBackedReplacementSnapshotVerificationResult(
            **base,
            verification_status="fetch_not_ready",
            reasons=("replacement_candidate_current_text_not_available",),
        )

    text_path = _optional_text(fetch_row.get("current_text_path"))
    text_hash = _optional_text(fetch_row.get("current_text_hash"))
    text_chars = _optional_int(fetch_row.get("current_text_chars")) or 0
    common = {
        **base,
        "snapshot_url": _optional_text(fetch_row.get("candidate_url")),
        "snapshot_source_type": _optional_text(fetch_row.get("content_type")),
        "extracted_text_path": text_path,
        "extracted_text_hash": text_hash,
        "extracted_text_chars": text_chars,
    }
    if verification is None:
        return SourceBackedReplacementSnapshotVerificationResult(
            **common,
            verification_status="same_event_verification_missing",
            reasons=("source_replacement_verification_row_missing",),
        )
    if _optional_bool(verification.get("ok")) is False:
        return SourceBackedReplacementSnapshotVerificationResult(
            **common,
            verification_status="attempt_failed",
            reasons=(_optional_text(verification.get("reason")) or "replacement_snapshot_verification_failed",),
        )

    snapshot_url = _optional_text(verification.get("snapshot_url") or verification.get("candidate_url")) or common["snapshot_url"]
    source_replacement_verified = _optional_bool(
        verification.get("source_replacement_verified") or verification.get("same_event_verified")
    ) is True
    snapshot_as_of_date = _optional_text(
        verification.get("snapshot_as_of_date")
        or verification.get("candidate_available_date")
        or verification.get("available_at")
    )
    verified_common = dict(common)
    verified_common.update(
        {
            "snapshot_url": snapshot_url,
            "snapshot_as_of_date": snapshot_as_of_date,
            "snapshot_source_type": _optional_text(verification.get("snapshot_source_type") or verification.get("source_type"))
            or common["snapshot_source_type"],
            "snapshot_title": _optional_text(verification.get("snapshot_title") or verification.get("title")),
            "source_replacement_verified": source_replacement_verified,
        }
    )
    if not source_replacement_verified:
        return SourceBackedReplacementSnapshotVerificationResult(
            **verified_common,
            verification_status="source_replacement_unverified",
            reasons=("same_event_source_replacement_not_verified",),
        )
    if _normalise_url(snapshot_url) != _normalise_url(_optional_text(fetch_row.get("candidate_url"))):
        return SourceBackedReplacementSnapshotVerificationResult(
            **verified_common,
            verification_status="snapshot_url_mismatch",
            reasons=("verified_snapshot_url_does_not_match_candidate_url",),
        )
    snapshot_date = _parse_iso_date(snapshot_as_of_date)
    as_of = _parse_iso_date(_optional_text(fetch_row.get("as_of_date")))
    if snapshot_date is None:
        return SourceBackedReplacementSnapshotVerificationResult(
            **verified_common,
            verification_status="invalid_snapshot_date",
            reasons=("snapshot_as_of_date_required",),
        )
    if as_of is not None and snapshot_date > as_of:
        return SourceBackedReplacementSnapshotVerificationResult(
            **verified_common,
            verification_status="future_snapshot_not_allowed",
            reasons=("snapshot_as_of_date_after_seed_as_of_date",),
        )
    if not text_path or not Path(text_path).exists():
        return SourceBackedReplacementSnapshotVerificationResult(
            **verified_common,
            verification_status="snapshot_text_missing",
            reasons=("replacement_snapshot_text_path_missing",),
        )
    text = Path(text_path).read_text(encoding="utf-8", errors="ignore")
    if not text.strip():
        return SourceBackedReplacementSnapshotVerificationResult(
            **verified_common,
            verification_status="empty_snapshot_text",
            reasons=("replacement_snapshot_text_empty",),
        )
    actual_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
    if _looks_like_sha256(text_hash) and text_hash != actual_hash:
        return SourceBackedReplacementSnapshotVerificationResult(
            **verified_common,
            verification_status="content_hash_mismatch",
            reasons=("replacement_snapshot_text_hash_mismatch",),
        )
    verified_common["extracted_text_hash"] = actual_hash
    return SourceBackedReplacementSnapshotVerificationResult(
        **verified_common,
        verification_status="replacement_snapshot_verified",
        asof_snapshot_verified=True,
        evidence_document_fixture_ready=True,
        production_score_fixture=False,
        reasons=("replacement_source_same_event_and_asof_snapshot_verified",),
    )


def _replacement_snapshot_request_for_verification_row(
    row: Mapping[str, Any],
) -> SourceBackedReplacementSnapshotRequest | None:
    status = _optional_text(row.get("verification_status")) or ""
    if status == "replacement_snapshot_verified":
        return None
    request_status, required_output, reasons = _replacement_snapshot_request_classification(status)
    return SourceBackedReplacementSnapshotRequest(
        request_id=_optional_text(row.get("request_id")) or "",
        task_id=_optional_text(row.get("task_id")) or "",
        replacement_candidate_id=_optional_text(row.get("replacement_candidate_id")) or "",
        fixture_seed_id=_optional_text(row.get("fixture_seed_id")) or "",
        candidate_id=_optional_text(row.get("candidate_id")) or "",
        archetype_id=_optional_text(row.get("archetype_id")) or "",
        original_source_anchor=_optional_text(row.get("original_source_anchor")) or "",
        candidate_url=_optional_text(row.get("candidate_url") or row.get("snapshot_url")) or "",
        as_of_date=_optional_text(row.get("as_of_date")),
        input_verification_status=status,
        request_status=request_status,
        required_output=required_output,
        snapshot_url=_optional_text(row.get("snapshot_url") or row.get("candidate_url")),
        snapshot_source_type=_optional_text(row.get("snapshot_source_type")),
        extracted_text_path=_optional_text(row.get("extracted_text_path")),
        extracted_text_hash=_optional_text(row.get("extracted_text_hash")),
        extracted_text_chars=_optional_int(row.get("extracted_text_chars")) or 0,
        score_blocked_until_resolved=True,
        source_replacement_verified=_optional_bool(row.get("source_replacement_verified")) is True,
        asof_snapshot_verified=_optional_bool(row.get("asof_snapshot_verified")) is True,
        evidence_document_fixture_ready=_optional_bool(row.get("evidence_document_fixture_ready")) is True,
        production_score_fixture=False,
        reasons=reasons,
    )


def _replacement_snapshot_verifier_task_for_request(
    request: Mapping[str, Any],
) -> SourceBackedReplacementSnapshotVerifierTask:
    request_status = _optional_text(request.get("request_status")) or ""
    verifier_status, required_output, reasons = _replacement_snapshot_verifier_task_classification(
        request_status=request_status,
        extracted_text_path=_optional_text(request.get("extracted_text_path")),
        extracted_text_hash=_optional_text(request.get("extracted_text_hash")),
        extracted_text_chars=_optional_int(request.get("extracted_text_chars")) or 0,
    )
    task_id = "RSVFY-" + hashlib.sha1(
        "|".join(
            (
                _optional_text(request.get("task_id")) or "",
                _optional_text(request.get("replacement_candidate_id")) or "",
                verifier_status,
            )
        ).encode("utf-8")
    ).hexdigest()[:20]
    return SourceBackedReplacementSnapshotVerifierTask(
        task_id=task_id,
        request_id=_optional_text(request.get("request_id")) or "",
        replacement_candidate_id=_optional_text(request.get("replacement_candidate_id")) or "",
        fixture_seed_id=_optional_text(request.get("fixture_seed_id")) or "",
        candidate_id=_optional_text(request.get("candidate_id")) or "",
        archetype_id=_optional_text(request.get("archetype_id")) or "",
        original_source_anchor=_optional_text(request.get("original_source_anchor")) or "",
        candidate_url=_optional_text(request.get("candidate_url")) or "",
        as_of_date=_optional_text(request.get("as_of_date")),
        input_request_status=request_status,
        verifier_task_status=verifier_status,
        required_output=required_output,
        snapshot_url=_optional_text(request.get("snapshot_url")),
        snapshot_source_type=_optional_text(request.get("snapshot_source_type")),
        extracted_text_path=_optional_text(request.get("extracted_text_path")),
        extracted_text_hash=_optional_text(request.get("extracted_text_hash")),
        extracted_text_chars=_optional_int(request.get("extracted_text_chars")) or 0,
        score_blocked_until_verified=True,
        source_replacement_verified=False,
        asof_snapshot_verified=False,
        evidence_document_fixture_ready=False,
        production_score_fixture=False,
        reasons=reasons,
    )


def _replacement_snapshot_verifier_task_classification(
    *,
    request_status: str,
    extracted_text_path: str | None,
    extracted_text_hash: str | None,
    extracted_text_chars: int,
) -> tuple[str, str, tuple[str, ...]]:
    has_text_anchor = bool(extracted_text_path and extracted_text_hash and extracted_text_chars > 0)
    if request_status == "same_event_verification_required" and has_text_anchor:
        return (
            "ready_for_same_event_asof_verifier",
            "source_replacement_same_event_and_asof_decision",
            ("same_event_asof_verifier_requires_text_anchor_only_no_score_context",),
        )
    if request_status == "same_event_verification_required":
        return (
            "blocked_until_text_snapshot_repair",
            "candidate_text_snapshot_repair",
            ("same_event_verification_missing_text_anchor",),
        )
    if request_status == "fetch_candidate_snapshot_required":
        return (
            "blocked_until_candidate_text_snapshot",
            "candidate_source_text_snapshot",
            ("candidate_text_snapshot_required_before_verifier",),
        )
    if request_status == "asof_date_repair_required" and has_text_anchor:
        return (
            "ready_for_asof_date_repair_verifier",
            "asof_safe_snapshot_date_verification",
            ("asof_date_repair_verifier_requires_text_anchor_only_no_score_context",),
        )
    if request_status == "text_snapshot_repair_required":
        return (
            "blocked_until_text_snapshot_repair",
            "candidate_text_snapshot_repair",
            ("candidate_text_snapshot_repair_required_before_verifier",),
        )
    return (
        "blocked_unknown_snapshot_request",
        "snapshot_request_triage",
        ("unknown_replacement_snapshot_request_status",),
    )


_FORBIDDEN_REPLACEMENT_SNAPSHOT_VERIFIER_RESULT_FIELDS = frozenset(
    {
        "verified",
        "current_score_eligible",
        "score_eligible",
        "source_tier",
        "primitive_id",
        "candidate_primitive_id",
        "score",
        "stage",
        "evidence_contract",
        "missing_primitive",
        "score_gap",
        "current_score",
        "stage_gate",
        "green_gate",
        "production_score_fixture",
    }
)


def _replacement_snapshot_verifier_result_for_task(
    task: Mapping[str, Any],
    row: Mapping[str, Any] | None,
) -> SourceBackedReplacementSnapshotVerifierResult:
    base = {
        "verifier_task_id": _optional_text(task.get("task_id")) or "",
        "request_id": _optional_text(task.get("request_id")) or "",
        "replacement_candidate_id": _optional_text(task.get("replacement_candidate_id")) or "",
        "fixture_seed_id": _optional_text(task.get("fixture_seed_id")) or "",
        "candidate_id": _optional_text(task.get("candidate_id")) or "",
        "archetype_id": _optional_text(task.get("archetype_id")) or "",
        "original_source_anchor": _optional_text(task.get("original_source_anchor")) or "",
        "candidate_url": _optional_text(task.get("candidate_url")) or "",
        "as_of_date": _optional_text(task.get("as_of_date")),
        "snapshot_url": _optional_text(task.get("snapshot_url") or task.get("candidate_url")),
        "snapshot_source_type": _optional_text(task.get("snapshot_source_type")),
        "extracted_text_path": _optional_text(task.get("extracted_text_path")),
        "extracted_text_hash": _optional_text(task.get("extracted_text_hash")),
        "extracted_text_chars": _optional_int(task.get("extracted_text_chars")) or 0,
    }
    status = _optional_text(task.get("verifier_task_status")) or ""
    if status not in {"ready_for_same_event_asof_verifier", "ready_for_asof_date_repair_verifier"}:
        return SourceBackedReplacementSnapshotVerifierResult(
            result_id=_replacement_snapshot_verifier_result_id(task, "blocked_task_not_ready"),
            **base,
            result_status="blocked_task_not_ready",
            reasons=("replacement_snapshot_verifier_task_not_ready",),
        )
    if row is None:
        return SourceBackedReplacementSnapshotVerifierResult(
            result_id=_replacement_snapshot_verifier_result_id(task, "no_verifier_result"),
            **base,
            result_status="no_verifier_result",
            reasons=("no_same_event_asof_verifier_result",),
        )

    forbidden = tuple(sorted(_FORBIDDEN_REPLACEMENT_SNAPSHOT_VERIFIER_RESULT_FIELDS.intersection(row)))
    if forbidden:
        return SourceBackedReplacementSnapshotVerifierResult(
            result_id=_replacement_snapshot_verifier_result_id(task, "forbidden_output_field"),
            **base,
            result_status="forbidden_output_field",
            forbidden_output_fields=forbidden,
            reasons=("same_event_asof_verifier_returned_forbidden_score_or_stage_field",),
        )

    if _optional_bool(row.get("ok")) is False:
        return SourceBackedReplacementSnapshotVerifierResult(
            result_id=_replacement_snapshot_verifier_result_id(task, "attempt_failed"),
            **base,
            result_status="attempt_failed",
            same_event_decision=_optional_text(row.get("same_event_decision")),
            reasons=(_optional_text(row.get("reason")) or "same_event_asof_verifier_failed",),
        )

    same_event_decision = _normalise_same_event_decision(
        row.get("same_event_decision")
        or row.get("same_underlying_event")
        or row.get("event_match")
    )
    if same_event_decision != "same_event":
        return SourceBackedReplacementSnapshotVerifierResult(
            result_id=_replacement_snapshot_verifier_result_id(task, "same_event_unverified"),
            **base,
            result_status="same_event_unverified",
            same_event_decision=same_event_decision,
            reasons=("same_underlying_event_not_verified",),
        )

    snapshot_url = _optional_text(row.get("snapshot_url") or row.get("candidate_url")) or base["snapshot_url"]
    if _normalise_url(snapshot_url or "") != _normalise_url(base["snapshot_url"] or ""):
        url_mismatch_base = {**base, "snapshot_url": snapshot_url}
        return SourceBackedReplacementSnapshotVerifierResult(
            result_id=_replacement_snapshot_verifier_result_id(task, "snapshot_url_mismatch"),
            **url_mismatch_base,
            result_status="snapshot_url_mismatch",
            same_event_decision=same_event_decision,
            reasons=("verifier_snapshot_url_does_not_match_task_snapshot_url",),
        )

    snapshot_as_of_date = _optional_text(
        row.get("snapshot_as_of_date")
        or row.get("candidate_available_date")
        or row.get("available_at")
    )
    snapshot_date = _parse_iso_date(snapshot_as_of_date)
    as_of = _parse_iso_date(base["as_of_date"])
    if snapshot_date is None:
        invalid_date_base = {**base, "snapshot_url": snapshot_url}
        return SourceBackedReplacementSnapshotVerifierResult(
            result_id=_replacement_snapshot_verifier_result_id(task, "invalid_snapshot_date"),
            **invalid_date_base,
            result_status="invalid_snapshot_date",
            same_event_decision=same_event_decision,
            snapshot_as_of_date=snapshot_as_of_date,
            reasons=("snapshot_as_of_date_required",),
        )
    if as_of is not None and snapshot_date > as_of:
        future_date_base = {**base, "snapshot_url": snapshot_url}
        return SourceBackedReplacementSnapshotVerifierResult(
            result_id=_replacement_snapshot_verifier_result_id(task, "future_snapshot_not_allowed"),
            **future_date_base,
            result_status="future_snapshot_not_allowed",
            same_event_decision=same_event_decision,
            snapshot_as_of_date=snapshot_as_of_date,
            reasons=("snapshot_as_of_date_after_seed_as_of_date",),
        )

    text_path = base["extracted_text_path"]
    if not text_path or not Path(text_path).exists():
        text_missing_base = {**base, "snapshot_url": snapshot_url}
        return SourceBackedReplacementSnapshotVerifierResult(
            result_id=_replacement_snapshot_verifier_result_id(task, "snapshot_text_missing"),
            **text_missing_base,
            result_status="snapshot_text_missing",
            same_event_decision=same_event_decision,
            snapshot_as_of_date=snapshot_as_of_date,
            reasons=("replacement_snapshot_text_path_missing",),
        )
    text = Path(text_path).read_text(encoding="utf-8", errors="ignore")
    if not text.strip():
        empty_text_base = {**base, "snapshot_url": snapshot_url}
        return SourceBackedReplacementSnapshotVerifierResult(
            result_id=_replacement_snapshot_verifier_result_id(task, "empty_snapshot_text"),
            **empty_text_base,
            result_status="empty_snapshot_text",
            same_event_decision=same_event_decision,
            snapshot_as_of_date=snapshot_as_of_date,
            reasons=("replacement_snapshot_text_empty",),
        )
    actual_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
    text_hash = base["extracted_text_hash"]
    if _looks_like_sha256(text_hash) and text_hash != actual_hash:
        mismatch_base = {**base, "snapshot_url": snapshot_url, "extracted_text_hash": actual_hash}
        return SourceBackedReplacementSnapshotVerifierResult(
            result_id=_replacement_snapshot_verifier_result_id(task, "content_hash_mismatch"),
            **mismatch_base,
            result_status="content_hash_mismatch",
            same_event_decision=same_event_decision,
            snapshot_as_of_date=snapshot_as_of_date,
            reasons=("replacement_snapshot_text_hash_mismatch",),
        )

    accepted_row = {
        "task_id": base["verifier_task_id"],
        "replacement_candidate_id": base["replacement_candidate_id"],
        "ok": True,
        "same_event_verified": True,
        "snapshot_url": snapshot_url,
        "snapshot_as_of_date": snapshot_as_of_date,
        "snapshot_source_type": _optional_text(row.get("snapshot_source_type") or row.get("source_type"))
        or base["snapshot_source_type"],
        "snapshot_title": _optional_text(row.get("snapshot_title") or row.get("title")),
        "verifier_result_id": _replacement_snapshot_verifier_result_id(task, "same_event_asof_verified"),
    }
    verified_base = {
        **base,
        "snapshot_url": snapshot_url,
        "snapshot_source_type": accepted_row["snapshot_source_type"],
        "extracted_text_hash": actual_hash,
    }
    return SourceBackedReplacementSnapshotVerifierResult(
        result_id=accepted_row["verifier_result_id"],
        **verified_base,
        result_status="same_event_asof_verified",
        same_event_decision=same_event_decision,
        snapshot_as_of_date=snapshot_as_of_date,
        snapshot_title=accepted_row["snapshot_title"],
        source_replacement_verified=True,
        asof_snapshot_verified=True,
        evidence_document_fixture_ready=False,
        production_score_fixture=False,
        accepted_verification_row=accepted_row,
        reasons=("same_event_asof_verifier_result_passed_gate",),
    )


def _replacement_snapshot_verifier_result_id(task: Mapping[str, Any], status: str) -> str:
    digest = hashlib.sha1(
        "|".join(
            (
                _optional_text(task.get("task_id")) or "",
                _optional_text(task.get("replacement_candidate_id")) or "",
                status,
            )
        ).encode("utf-8")
    ).hexdigest()[:20]
    return f"RSVRES-{digest}"


def _normalise_same_event_decision(value: Any) -> str:
    text = str(value or "").strip().lower().replace("-", "_").replace(" ", "_")
    if text in {"same_event", "same_underlying_event", "match", "matched", "true", "yes"}:
        return "same_event"
    if text in {"different_event", "not_same_event", "mismatch", "false", "no"}:
        return "different_event"
    return "unknown"


def _replacement_snapshot_request_classification(status: str) -> tuple[str, str, tuple[str, ...]]:
    if status == "fetch_not_ready":
        return (
            "fetch_candidate_snapshot_required",
            "candidate_source_text_snapshot",
            ("replacement_candidate_fetch_not_ready",),
        )
    if status in {"same_event_verification_missing", "source_replacement_unverified", "snapshot_url_mismatch"}:
        return (
            "same_event_verification_required",
            "same_event_source_replacement_verification",
            ("same_event_or_source_replacement_verification_required",),
        )
    if status in {"invalid_snapshot_date", "future_snapshot_not_allowed"}:
        return (
            "asof_date_repair_required",
            "asof_safe_snapshot_date_verification",
            ("snapshot_asof_date_repair_required",),
        )
    if status in {"snapshot_text_missing", "empty_snapshot_text", "attempt_failed"}:
        return (
            "text_snapshot_repair_required",
            "candidate_text_snapshot_repair",
            ("candidate_text_snapshot_repair_required",),
        )
    if status == "content_hash_mismatch":
        return (
            "hash_repair_required",
            "candidate_text_hash_repair",
            ("candidate_text_hash_repair_required",),
        )
    return (
        "text_snapshot_repair_required",
        "replacement_snapshot_manual_review",
        ("replacement_snapshot_status_requires_manual_review",),
    )


def _date_hints_from_text_and_url(*, text: str, source_anchor: str) -> tuple[str, ...]:
    hints: list[str] = []
    haystacks = (source_anchor, text)
    for haystack in haystacks:
        for year, month, day in re.findall(r"\b(20\d{2})[-./](0[1-9]|1[0-2])[-./]([0-2]\d|3[01])\b", haystack):
            _append_valid_date_hint(hints, year, month, day)
        for year, month, day in re.findall(r"\b(20\d{2})(0[1-9]|1[0-2])([0-2]\d|3[01])\b", haystack):
            _append_valid_date_hint(hints, year, month, day)
        for year, month, day in re.findall(r"AKR(20\d{2})(0[1-9]|1[0-2])([0-2]\d|3[01])", haystack):
            _append_valid_date_hint(hints, year, month, day)
    return tuple(dict.fromkeys(hints))


def _append_valid_date_hint(hints: list[str], year: str, month: str, day: str) -> None:
    value = f"{year}-{month}-{day}"
    try:
        date.fromisoformat(value)
    except ValueError:
        return
    hints.append(value)


def _fixture_anchor_text(text: str, *, max_chars: int) -> str:
    clean = text.strip()
    if not clean:
        return ""
    return clean[: max(1, max_chars)].strip()


def _parse_iso_date(value: str | None) -> date | None:
    if not value:
        return None
    try:
        return date.fromisoformat(value[:10])
    except ValueError:
        return None


def _looks_like_sha256(value: str | None) -> bool:
    return bool(value and re.fullmatch(r"[0-9a-fA-F]{64}", value.strip()))


def _source_type_from_snapshot_row(row: Mapping[str, Any]) -> SourceType:
    raw = (_optional_text(row.get("snapshot_source_type")) or "").lower()
    if any(marker in raw for marker in ("broker", "research", "report", "pdf")):
        return SourceType.RESEARCH_REPORT
    if any(marker in raw for marker in ("news", "article", "press")):
        return SourceType.NEWS
    if any(marker in raw for marker in ("dart", "filing", "disclosure", "kind")):
        return SourceType.FILING
    if "ir" in raw or "presentation" in raw:
        return SourceType.IR
    if "xbrl" in raw:
        return SourceType.XBRL
    if "api" in raw:
        return SourceType.API
    return SourceType.OTHER


def _source_type_from_text(value: Any) -> SourceType:
    text = str(value or "").strip()
    if text:
        try:
            return SourceType(text)
        except ValueError:
            pass
    lowered = text.lower()
    if "news" in lowered or "article" in lowered:
        return SourceType.NEWS
    if "filing" in lowered or "dart" in lowered or "kind" in lowered:
        return SourceType.FILING
    if "ir" in lowered:
        return SourceType.IR
    if "research" in lowered or "report" in lowered:
        return SourceType.RESEARCH_REPORT
    return SourceType.OTHER


def _source_name_from_snapshot_row(row: Mapping[str, Any]) -> str:
    title = _optional_text(row.get("snapshot_title"))
    if title:
        return title[:120]
    url = _optional_text(row.get("snapshot_url")) or _optional_text(row.get("source_anchor"))
    if url:
        netloc = parse.urlsplit(url).netloc
        if netloc:
            return netloc.lower()
    return "source_snapshot"


def _snapshot_revision_id(row: Mapping[str, Any]) -> str:
    parts = (
        _optional_text(row.get("fixture_seed_id")) or "",
        _optional_text(row.get("snapshot_as_of_date")) or "",
        _optional_text(row.get("extracted_text_hash")) or "",
    )
    return "SREV-" + hashlib.sha1("|".join(parts).encode("utf-8")).hexdigest()[:20]


def _source_lineage_id(canonical_url: str | None) -> str | None:
    if not canonical_url:
        return None
    return "SLIN-" + hashlib.sha1((_normalise_url(canonical_url) or canonical_url).encode("utf-8")).hexdigest()[:20]


def _row_fingerprint(row: Mapping[str, Any]) -> str:
    stable_row = {
        key: value
        for key, value in row.items()
        if key not in {"raw_source_snippet"}
    }
    payload = json.dumps(stable_row, ensure_ascii=False, sort_keys=True, default=str)
    return "RROW-" + hashlib.sha256(payload.encode("utf-8")).hexdigest()[:20]


def _stable_short_id(prefix: str, *parts: object) -> str:
    payload = "|".join(str(part) for part in parts)
    return f"{prefix}-{hashlib.sha1(payload.encode('utf-8')).hexdigest()[:20]}"


def _enum_from_text(enum_cls: Any, value: Any, default: Any) -> Any:
    try:
        return enum_cls(str(value or "").strip())
    except ValueError:
        return default


def _iter_text_values(value: Any) -> Iterable[str]:
    if value is None:
        return
    if isinstance(value, (list, tuple, set)):
        for item in value:
            yield from _iter_text_values(item)
        return
    if isinstance(value, Mapping):
        for item in value.values():
            yield from _iter_text_values(item)
        return
    text = str(value).strip()
    if text:
        yield text


def _optional_bool(value: Any) -> bool | None:
    if isinstance(value, bool):
        return value
    if value is None:
        return None
    text = str(value).strip().lower()
    if text in {"true", "1", "yes", "y"}:
        return True
    if text in {"false", "0", "no", "n"}:
        return False
    return None


def _optional_int(value: Any) -> int | None:
    if value in (None, ""):
        return None
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def _optional_float(value: Any) -> float | None:
    if value in (None, ""):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _text_tuple_from_value(value: Any) -> tuple[str, ...]:
    if value is None:
        return ()
    if isinstance(value, str):
        parts = re.split(r"[,|]", value)
        return tuple(dict.fromkeys(part.strip() for part in parts if part.strip()))
    if isinstance(value, Sequence) and not isinstance(value, (bytes, bytearray)):
        return tuple(dict.fromkeys(str(item).strip() for item in value if str(item).strip()))
    text = str(value).strip()
    return (text,) if text else ()


def _optional_text(value: Any) -> str | None:
    text = str(value or "").strip()
    return text or None


def _examples(classifications: Sequence[ReplaySourceClassification], *, limit: int) -> tuple[str, ...]:
    result: list[str] = []
    for item in classifications[:limit]:
        if item.source_path and item.source_line:
            result.append(f"{item.source_path}:{item.source_line}")
        elif item.source_path:
            result.append(item.source_path)
        else:
            result.append(",".join(item.reasons))
    return tuple(result)


__all__ = [
    "COVERAGE_AVAILABLE",
    "COVERAGE_GAP_NO_ROWS",
    "COVERAGE_GAP_WITH_ROWS",
    "ReplayCoverageRow",
    "ReplaySourceClassification",
    "ReplaySourceStatus",
    "SourceBackedReplayCandidate",
    "SourceBackedReplayFixtureSeed",
    "SourceBackedSnapshotAvailability",
    "SourceBackedCurrentFetchStatus",
    "SourceBackedSnapshotRemediationTask",
    "SourceBackedCurrentTextAsofPrecheck",
    "SourceBackedEvidenceDocumentFixture",
    "SourceBackedAsofSnapshotAcquisitionTask",
    "SourceBackedAsofSnapshotVerificationResult",
    "SourceBackedAsofSnapshotVerifierTask",
    "SourceBackedAsofSnapshotVerifierResult",
    "SourceBackedReplacementSourceRequest",
    "SourceBackedReplacementSourceCandidate",
    "SourceBackedReplacementCandidateAcquisitionTask",
    "SourceBackedReplacementCandidateFetchStatus",
    "SourceBackedReplacementSnapshotVerificationResult",
    "SourceBackedReplacementSnapshotRequest",
    "SourceBackedReplacementSnapshotVerifierTask",
    "SourceBackedReplacementSnapshotVerifierResult",
    "SourceBackedReplacementEvidenceDocumentFixture",
    "SourceBackedClaimReplayTask",
    "SourceBackedClaimReplayResult",
    "SourceBackedAdjudicationTask",
    "SourceBackedAdjudicationResult",
    "SourceBackedPrimitiveMappingTask",
    "SourceBackedPrimitiveMappingResult",
    "SourceBackedEligibilityTask",
    "SourceBackedEligibilityResult",
    "SourceBackedScoreContributionTask",
    "SourceBackedScoreContributionResult",
    "SourceBackedScoreSnapshotTask",
    "SourceBackedScoreSnapshotResult",
    "SourceBackedStageCourtTask",
    "SourceBackedStageCourtResult",
    "SourceBackedReplayChainAudit",
    "SourceBackedClaimReplayReadinessAudit",
    "SourceBackedReplacementFetchRemediationTask",
    "SourceBackedReplacementFetchFailureAudit",
    "SourceBackedReplacementPlannerRun",
    "build_source_backed_fixture_seed_manifest",
    "build_source_backed_replay_coverage",
    "build_source_backed_replay_manifest",
    "build_current_fetch_status_manifest",
    "build_snapshot_remediation_plan",
    "build_current_text_asof_precheck_manifest",
    "build_evidence_document_fixture_manifest",
    "build_asof_snapshot_acquisition_queue",
    "build_asof_snapshot_verification_manifest",
    "build_asof_snapshot_verifier_task_manifest",
    "build_asof_snapshot_verifier_result_manifest",
    "build_same_event_source_replacement_request_manifest",
    "build_same_event_replacement_planner_run_manifest",
    "build_same_event_source_replacement_candidate_manifest",
    "build_replacement_candidate_acquisition_queue",
    "build_replacement_candidate_fetch_status_manifest",
    "build_replacement_snapshot_verification_manifest",
    "build_replacement_snapshot_request_manifest",
    "build_replacement_snapshot_verifier_task_manifest",
    "build_replacement_snapshot_verifier_result_manifest",
    "build_replacement_evidence_document_fixture_manifest",
    "build_claim_replay_task_manifest",
    "build_claim_replay_result_manifest",
    "build_adjudication_task_manifest",
    "build_adjudication_result_manifest",
    "build_primitive_mapping_task_manifest",
    "build_primitive_mapping_result_manifest",
    "build_eligibility_task_manifest",
    "build_eligibility_result_manifest",
    "build_score_contribution_task_manifest",
    "build_score_contribution_result_manifest",
    "build_score_snapshot_task_manifest",
    "build_score_snapshot_result_manifest",
    "build_stage_court_task_manifest",
    "build_stage_court_result_manifest",
    "build_claim_replay_chain_audit_manifest",
    "build_claim_replay_readiness_audit_manifest",
    "build_replacement_fetch_failure_audit_manifest",
    "build_source_snapshot_availability_manifest",
    "classify_replay_source_status",
    "iter_json_research_rows",
    "replay_coverage_summary",
    "replay_coverage_to_dict",
]
