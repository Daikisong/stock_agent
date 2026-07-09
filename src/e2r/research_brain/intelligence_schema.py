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
    "INTELLIGENCE_SCHEMA_VERSION",
    "HistoricalEvidenceReference",
    "HistoricalOutcome",
    "HistoricalResearchArtifact",
    "HistoricalResearchCase",
    "HistoricalRuleCandidate",
    "LinkageError",
    "NarrativeCaseCandidate",
    "ParsedResearchArtifact",
    "ParsedResearchRow",
    "ParsedRowKind",
    "QuarantineReason",
    "QuarantineRecord",
    "SourceLineRange",
    "stable_intelligence_id",
]
