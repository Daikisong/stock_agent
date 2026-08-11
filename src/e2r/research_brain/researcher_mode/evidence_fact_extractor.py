"""Provider-backed full-document extraction for current Researcher Mode.

The LLM proposes explicit economic facts.  Deterministic code verifies target,
as-of date, full-document eligibility, exact-quote lineage, document accounting,
and source identity before the existing EvidenceFactCompiler is allowed to
create canonical facts.  Search snippets and LLM-only assertions never enter
the fact graph.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, replace
from datetime import date
import hashlib
import json
import math
import os
from pathlib import Path
import re
import tempfile
from typing import Any, Mapping, Sequence

from e2r.research_brain.intelligence_schema import stable_intelligence_id
from e2r.research_brain.planning.provider_transport import (
    StructuredProviderRejected,
    StructuredProviderUnavailable,
)
from e2r.research_brain.scoring.business_mechanism_scope import (
    ArchetypeMechanismScopeContract,
    BusinessMechanismScope,
    MechanismScopeValidator,
    load_mechanism_scope_contracts,
)

from .component_researcher import (
    FACT_EXTRACTION_PAGE_FACT_LIMIT,
    StructuredResearchProvider,
    _single_payload_request_material,
)
from .prompt_projection import (
    project_fact_extraction_evidence_context,
    project_fact_extraction_score_gap_context,
)
from .evidence_fact_compiler import EvidenceFactCompiler, FactCompilationResult
from .fact_lineage_materials import (
    AUTHORITY_RECOVERY_FACT_SEMANTICS_VERSIONS,
    AuthoritativeResearchEpochFactLedger,
    CurrentFactLineageRecoveryBinding,
    validate_current_v5_fact_lineage_materials,
)
from .schemas import (
    CANONICAL_COMPONENT_ORDER,
    EvidenceDirection,
    EvidenceLifecycle,
    assert_blind_research_output,
    scrub_blind_research_payload,
)


FACT_EXTRACTION_OUTPUT_FILES: Mapping[str, str] = {
    "accepted_claims": "material_fact_claims.jsonl",
    "rejections": "fact_extraction_rejections.jsonl",
    "document_dispositions": "fact_document_dispositions.jsonl",
    "provider_calls": "fact_extraction_provider_calls.jsonl",
    "facts": "evidence_facts.jsonl",
    "counterfacts": "counterfacts.jsonl",
    "claim_fact_links": "claim_fact_links.jsonl",
    "result": "fact_extraction_result.json",
    "audit": "fact_extraction_audit.json",
}

PUNCTUATION_ONLY_VALUE_NORMALIZATION = (
    "PUNCTUATION_ONLY_VALUE_REPLACED_WITH_NORMALIZED_OBJECT"
)
TRANSPORT_FRAGMENT_VALUE_NORMALIZATION = (
    "TRANSPORT_FRAGMENT_VALUE_REPLACED_WITH_NORMALIZED_OBJECT"
)
STRUCTURED_JSON_STRING_VALUE_TYPE_RESTORED = (
    "STRUCTURED_JSON_STRING_VALUE_TYPE_RESTORED"
)
NUMERIC_SCALAR_STRING_VALUE_TYPE_RESTORED = (
    "NUMERIC_SCALAR_STRING_VALUE_TYPE_RESTORED"
)
FACT_EXTRACTION_MODES = frozenset(
    {"RESEARCH_BACKFILL", "PRODUCTION_OBJECTIVE_LOCAL"}
)
OBJECTIVE_FACT_RELATIONS = frozenset(
    {"ADVANCE", "COUNTER", "SUPERSEDE"}
)
FACT_EXTRACTION_SEMANTICS_VERSION = (
    "e2r_v5_structured_revision_roles_v6"
)
_PRE_STRUCTURED_REVISION_ROLE_SEMANTICS_VERSION = (
    "e2r_v5_structured_valuation_roles_v5"
)
_PRE_STRUCTURED_VALUATION_ROLE_SEMANTICS_VERSION = (
    "e2r_v5_source_boundary_context_v4"
)
SOURCE_BOUNDARY_CONTEXT_CHARS = 4_000
_TRUSTED_COVERAGE_REFRESH_SOURCE_TIERS = frozenset(
    {
        "REGULATORY_OFFICIAL",
        "ISSUER_OFFICIAL",
        "CUSTOMER_OFFICIAL",
        "TRUSTED_INDEPENDENT",
    }
)

_RFC8259_NUMBER_PATTERN = re.compile(
    r"-?(?:0|[1-9]\d*)(?:\.\d+)?(?:[eE][+-]?\d+)?\Z"
)
_CALENDAR_YEAR_PATTERN = re.compile(r"(?:19|20)\d{2}\Z")
_CALENDAR_YEAR_MONTH_PATTERN = re.compile(
    r"(?:19|20)\d{2}\.(?:0?[1-9]|1[0-2])\Z"
)
_TEMPORAL_IDENTITY_UNITS = frozenset(
    {"date", "year", "years", "날짜", "년", "년도", "연도"}
)
_NONQUANTITATIVE_UNITS = frozenset(
    {
        "n/a",
        "na",
        "none",
        "not applicable",
        "null",
        "qualitative",
        "text",
        "unknown",
        "unspecified",
    }
)
_MAX_SAFE_NUMERIC_SIGNIFICANT_DIGITS = 15


def _is_transport_fragment_only_value(value: str) -> bool:
    """Return true only for a detached JSON-literal serialization fragment."""

    compact = "".join(value.lower().split())
    for literal in ("null", "true", "false"):
        if f":{literal}" not in compact:
            continue
        residue = compact.replace(literal, "")
        if residue and all(character in "{}[],:" for character in residue):
            return True
    return False


def _restorable_numeric_scalar(
    value: str,
    *,
    unit: Any,
) -> int | float | None:
    """Restore only an unambiguous quantitative RFC 8259 number."""

    if not _RFC8259_NUMBER_PATTERN.fullmatch(value):
        return None
    normalized_unit = str(unit or "").strip().casefold()
    if (
        not normalized_unit
        or normalized_unit in _TEMPORAL_IDENTITY_UNITS
        or normalized_unit in _NONQUANTITATIVE_UNITS
        or _CALENDAR_YEAR_PATTERN.fullmatch(value)
        or _CALENDAR_YEAR_MONTH_PATTERN.fullmatch(value)
    ):
        return None
    mantissa = value.lower().split("e", 1)[0].lstrip("-")
    significant_digits = mantissa.replace(".", "").lstrip("0")
    if len(significant_digits or "0") > _MAX_SAFE_NUMERIC_SIGNIFICANT_DIGITS:
        return None
    try:
        parsed = json.loads(value)
    except (TypeError, ValueError, json.JSONDecodeError):
        return None
    if (
        isinstance(parsed, bool)
        or not isinstance(parsed, (int, float))
        or (isinstance(parsed, float) and not math.isfinite(parsed))
    ):
        return None
    return parsed


def normalize_punctuation_only_fact_value(
    claim_or_proposal: Mapping[str, Any],
) -> Mapping[str, Any]:
    """Replace transport-noise-only values with the explicit semantic object.

    ``value`` may arrive as a delimiter accidentally copied from a table even
    though ``normalized_object`` contains the model's complete semantic value.
    A detached JSON serialization fragment such as ``:null},{`` or
    ``:true}],`` is the same transport failure even though its JSON literal
    contains letters.  Only that narrowly recognizable structural form is
    repaired; standalone literals and normal prose containing them are
    preserved exactly.  Complete JSON object/array strings are restored to
    their native type so exact grounding compares an object with an object;
    JSON scalars and actual mapping values are untouched.
    """

    normalized = dict(claim_or_proposal)
    raw_value = normalized.get("value")
    normalizations = [
        str(value).strip()
        for value in normalized.get("deterministic_field_normalizations", ())
        if str(value).strip()
    ]
    if isinstance(raw_value, str):
        try:
            parsed_value = json.loads(raw_value)
        except (TypeError, ValueError, json.JSONDecodeError):
            parsed_value = None
        if isinstance(parsed_value, (dict, list)):
            normalized["value"] = parsed_value
            raw_value = parsed_value
            normalizations.append(
                STRUCTURED_JSON_STRING_VALUE_TYPE_RESTORED
            )
        elif (
            numeric_value := _restorable_numeric_scalar(
                raw_value,
                unit=normalized.get("unit"),
            )
        ) is not None:
            normalized["value"] = numeric_value
            raw_value = numeric_value
            normalizations.append(
                NUMERIC_SCALAR_STRING_VALUE_TYPE_RESTORED
            )
    value_text = str(raw_value).strip() if raw_value is not None else ""
    normalized_object = str(normalized.get("normalized_object") or "").strip()
    punctuation_only = (
        bool(value_text)
        and not any(character.isalnum() for character in value_text)
    )
    transport_fragment_only = _is_transport_fragment_only_value(value_text)
    if (
        not value_text
        or not (punctuation_only or transport_fragment_only)
        or not any(character.isalnum() for character in normalized_object)
    ):
        if normalizations:
            normalized["deterministic_field_normalizations"] = list(
                dict.fromkeys(normalizations)
            )
        return normalized
    normalized["value"] = normalized_object
    normalizations.append(
        (
            TRANSPORT_FRAGMENT_VALUE_NORMALIZATION
            if transport_fragment_only
            else PUNCTUATION_ONLY_VALUE_NORMALIZATION
        )
    )
    normalized["deterministic_field_normalizations"] = list(
        dict.fromkeys(normalizations)
    )
    return normalized


@dataclass(frozen=True)
class FactExtractionRejection:
    batch_id: str
    proposal_index: int
    document_id: str
    reason: str
    material_proposal: bool
    proposed_exact_quote: str | None = None
    extraction_semantics_version: str = FACT_EXTRACTION_SEMANTICS_VERSION
    schema_version: str = "e2r_v5_fact_extraction_rejection_v1"

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class FactExtractionProviderCall:
    batch_id: str
    status: str
    document_ids: tuple[str, ...]
    accepted_claim_ids: tuple[str, ...]
    rejected_proposal_count: int
    document_dispositions: tuple[Mapping[str, Any], ...]
    pending_reasons: tuple[str, ...]
    research_gap_feedback: tuple[str, ...]
    provider_name: str
    prompt_hash: str
    response_hash: str | None
    provider_attempt_count: int = 1
    validation_retry_used: bool = False
    completion_flag_reconciled: bool = False
    transport_chunk_ids: tuple[str, ...] = ()
    accepted_claims: tuple[Mapping[str, Any], ...] | None = None
    coverage_audit_performed: bool = False
    semantics_migration_request_ids: tuple[str, ...] = ()
    semantics_migration_response_ids: tuple[str, ...] = ()
    current_lineage_request_ids: tuple[str, ...] = ()
    current_lineage_response_ids: tuple[str, ...] = ()
    current_lineage_original_batch_document_ids: tuple[str, ...] = ()
    current_lineage_objective_reassessment_document_ids: tuple[str, ...] = ()
    extraction_semantics_version: str = FACT_EXTRACTION_SEMANTICS_VERSION
    schema_version: str = "e2r_v5_fact_extraction_provider_call_v5"

    def __post_init__(self) -> None:
        if self.status not in {"COMPLETE", "PENDING"}:
            raise ValueError("unknown fact extraction provider-call status")
        if self.status == "PENDING" and not self.pending_reasons:
            raise ValueError("pending fact extraction call requires reasons")
        if self.provider_attempt_count < 0 or (
            self.provider_attempt_count == 0
            and not self.current_lineage_request_ids
        ):
            raise ValueError(
                "fact extraction provider attempt count must be positive "
                "outside current-lineage journal replay"
            )
        if self.accepted_claims is not None:
            embedded_claim_ids = tuple(
                str(row.get("claim_id") or "") for row in self.accepted_claims
            )
            if (
                any(not value for value in embedded_claim_ids)
                or len(embedded_claim_ids) != len(set(embedded_claim_ids))
                or set(embedded_claim_ids) != set(self.accepted_claim_ids)
            ):
                raise ValueError(
                    "embedded fact extraction claims must match accepted claim ids"
                )
        if (
            len(self.semantics_migration_request_ids)
            != len(self.semantics_migration_response_ids)
            or any(
                re.fullmatch(r"COLLABREQ-[0-9a-f]{64}", value) is None
                for value in self.semantics_migration_request_ids
            )
            or any(
                re.fullmatch(r"COLLABRESP-[0-9a-f]{64}", value) is None
                for value in self.semantics_migration_response_ids
            )
            or (
                self.semantics_migration_request_ids
                and (
                    self.status != "COMPLETE"
                    or self.extraction_semantics_version
                    != _PRE_STRUCTURED_VALUATION_ROLE_SEMANTICS_VERSION
                    or "COLLABORATION_CODEX_SUBAGENT"
                    not in self.provider_name
                )
            )
        ):
            raise ValueError("fact semantics migration receipts are invalid")
        if (
            len(self.current_lineage_request_ids)
            != len(self.current_lineage_response_ids)
            or len(self.current_lineage_request_ids)
            != len(set(self.current_lineage_request_ids))
            or len(self.current_lineage_response_ids)
            != len(set(self.current_lineage_response_ids))
            or any(
                re.fullmatch(r"COLLABREQ-[0-9a-f]{64}", value) is None
                for value in self.current_lineage_request_ids
            )
            or any(
                re.fullmatch(r"COLLABRESP-[0-9a-f]{64}", value) is None
                for value in self.current_lineage_response_ids
            )
            or len(self.current_lineage_original_batch_document_ids)
            != len(set(self.current_lineage_original_batch_document_ids))
            or any(
                not value
                for value in self.current_lineage_original_batch_document_ids
            )
            or len(
                self.current_lineage_objective_reassessment_document_ids
            )
            != len(
                set(
                    self.current_lineage_objective_reassessment_document_ids
                )
            )
            or any(
                not value
                for value in (
                    self.current_lineage_objective_reassessment_document_ids
                )
            )
            or not set(
                self.current_lineage_objective_reassessment_document_ids
            ).issubset(self.document_ids)
            or (
                self.current_lineage_request_ids
                and (
                    self.status != "COMPLETE"
                    or self.provider_attempt_count != 0
                    or self.extraction_semantics_version
                    != FACT_EXTRACTION_SEMANTICS_VERSION
                    or "COLLABORATION_CODEX_SUBAGENT"
                    not in self.provider_name
                    or not self.current_lineage_original_batch_document_ids
                    or not set(self.document_ids).issubset(
                        self.current_lineage_original_batch_document_ids
                    )
                    or self.semantics_migration_request_ids
                )
            )
            or (
                not self.current_lineage_request_ids
                and (
                    self.current_lineage_original_batch_document_ids
                    or self.current_lineage_objective_reassessment_document_ids
                )
            )
        ):
            raise ValueError("current fact lineage recovery receipts are invalid")

    def to_dict(self) -> Mapping[str, Any]:
        output = {
            **asdict(self),
            "document_dispositions": [dict(row) for row in self.document_dispositions],
        }
        if self.accepted_claims is None:
            output.pop("accepted_claims", None)
        else:
            output["accepted_claims"] = [
                dict(row) for row in self.accepted_claims
            ]
        if not self.semantics_migration_request_ids:
            output.pop("semantics_migration_request_ids", None)
            output.pop("semantics_migration_response_ids", None)
        if not self.current_lineage_request_ids:
            output.pop("current_lineage_request_ids", None)
            output.pop("current_lineage_response_ids", None)
            output.pop("current_lineage_original_batch_document_ids", None)
            output.pop(
                "current_lineage_objective_reassessment_document_ids",
                None,
            )
        return output


@dataclass(frozen=True)
class ResearcherFactExtractionResult:
    target_id: str
    as_of_date: str
    status: str
    material_claims: tuple[Mapping[str, Any], ...]
    fact_compilation: FactCompilationResult
    provider_calls: tuple[FactExtractionProviderCall, ...]
    rejections: tuple[FactExtractionRejection, ...]
    document_dispositions: tuple[Mapping[str, Any], ...]
    pending_reasons: tuple[str, ...]
    research_gap_feedback: tuple[str, ...]
    audit: Mapping[str, Any]
    production_score_authority: bool = False
    schema_version: str = "e2r_v5_researcher_fact_extraction_v1"

    def __post_init__(self) -> None:
        if self.status not in {"FACT_EXTRACTION_COMPLETE", "FACT_EXTRACTION_PENDING"}:
            raise ValueError("unknown Researcher fact extraction status")
        if self.status == "FACT_EXTRACTION_PENDING" and not self.pending_reasons:
            raise ValueError("pending fact extraction requires reasons")
        if self.production_score_authority:
            raise ValueError("fact extraction cannot assign production score")

    @property
    def facts(self):
        return self.fact_compilation.facts

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "schema_version": self.schema_version,
            "target_id": self.target_id,
            "as_of_date": self.as_of_date,
            "status": self.status,
            "material_claims": [dict(row) for row in self.material_claims],
            "fact_compilation": self.fact_compilation.to_dict(),
            "provider_calls": [row.to_dict() for row in self.provider_calls],
            "rejections": [row.to_dict() for row in self.rejections],
            "document_dispositions": [dict(row) for row in self.document_dispositions],
            "pending_reasons": list(self.pending_reasons),
            "research_gap_feedback": list(self.research_gap_feedback),
            "audit": dict(self.audit),
            "production_score_authority": False,
        }


_COLLABORATION_FACT_WAIT_RE = re.compile(
    r"FACT_EXTRACTION_PROVIDER_OR_OUTPUT_ERROR:"
    r"StructuredProviderUnavailable:"
    r"COLLABORATION_RESPONSE_PENDING:"
    r"COLLABREQ-[0-9a-f]{64}"
)
_INCOMPLETE_FACT_TRANSPORT_RE = re.compile(
    r"INCOMPLETE_DOCUMENT_TRANSPORT_CHUNKS:"
    r"SGDOC-[0-9a-f]{24}:[0-9]+/[1-9][0-9]*"
)
_CURRENT_FACT_LINEAGE_REMATERIALIZATION_RE = re.compile(
    r"CURRENT_FACT_LINEAGE_REMATERIALIZATION_REQUIRED:"
    r"SGDOC-[0-9a-f]{24}"
)
_CURRENT_FACT_LINEAGE_OBJECTIVE_REASSESSMENT_RE = re.compile(
    r"CURRENT_FACT_LINEAGE_OBJECTIVE_REASSESSMENT_REQUIRED:"
    r"SGDOC-[0-9a-f]{24}"
)
FACT_EXTRACTION_CANONICAL_STATE_REFRESH_REQUIRED = (
    "FACT_EXTRACTION_CANONICAL_STATE_REFRESH_REQUIRED"
)
_CURRENT_FACT_LINEAGE_AUTHORITY_PROJECTION_MISMATCH = (
    "CURRENT_FACT_LINEAGE_AUTHORITY_PROJECTION_MISMATCH"
)


def fact_extraction_has_exact_collaboration_wait(
    pending_reasons: Sequence[Any],
) -> bool:
    """Recognize only the resumable Codex response wait plus split progress."""

    reasons = tuple(str(value) for value in pending_reasons)
    collaboration_wait_count = sum(
        _COLLABORATION_FACT_WAIT_RE.fullmatch(reason) is not None
        for reason in reasons
    )
    return bool(
        collaboration_wait_count == 1
        and all(
            _COLLABORATION_FACT_WAIT_RE.fullmatch(reason) is not None
            or _INCOMPLETE_FACT_TRANSPORT_RE.fullmatch(reason) is not None
            for reason in reasons
        )
    )


def fact_extraction_has_exact_checkpoint_recovery_wait(
    pending_reasons: Sequence[Any],
) -> bool:
    """Recognize only a bounded fact queue wait that may reuse source state."""

    reasons = tuple(str(value) for value in pending_reasons)
    collaboration_count = sum(
        _COLLABORATION_FACT_WAIT_RE.fullmatch(reason) is not None
        for reason in reasons
    )
    refresh_count = reasons.count(
        FACT_EXTRACTION_CANONICAL_STATE_REFRESH_REQUIRED
    )
    authority_projection_mismatch_count = reasons.count(
        _CURRENT_FACT_LINEAGE_AUTHORITY_PROJECTION_MISMATCH
    )
    rematerialization_reasons = tuple(
        reason
        for reason in reasons
        if _CURRENT_FACT_LINEAGE_REMATERIALIZATION_RE.fullmatch(reason)
        is not None
    )
    rematerialization_count = len(rematerialization_reasons)
    rematerialization_roster_is_unique = (
        rematerialization_count == len(set(rematerialization_reasons))
    )
    objective_reassessment_reasons = tuple(
        reason
        for reason in reasons
        if _CURRENT_FACT_LINEAGE_OBJECTIVE_REASSESSMENT_RE.fullmatch(reason)
        is not None
    )
    objective_reassessment_count = len(objective_reassessment_reasons)
    objective_reassessment_roster_is_unique = (
        objective_reassessment_count
        == len(set(objective_reassessment_reasons))
    )
    incomplete_count = sum(
        _INCOMPLETE_FACT_TRANSPORT_RE.fullmatch(reason) is not None
        for reason in reasons
    )
    return bool(
        reasons
        and rematerialization_roster_is_unique
        and objective_reassessment_roster_is_unique
        and collaboration_count <= 1
        and refresh_count <= 1
        and authority_projection_mismatch_count <= 1
        and not (
            collaboration_count
            and (refresh_count or authority_projection_mismatch_count)
        )
        and not (
            refresh_count and authority_projection_mismatch_count
        )
        and (
            collaboration_count
            + refresh_count
            + authority_projection_mismatch_count
            + rematerialization_count
            + objective_reassessment_count
            + incomplete_count
            == len(reasons)
        )
        and (
            rematerialization_count >= 1
            or objective_reassessment_count >= 1
            or collaboration_count == 1
            or refresh_count == 1
            or authority_projection_mismatch_count == 1
        )
    )


def _project_current_facts_with_accepted_claims(
    *,
    current_facts: Sequence[Mapping[str, Any]],
    accepted_claims: Sequence[Mapping[str, Any]],
    target_id: str,
    as_of_date: str,
) -> Mapping[str, Any]:
    """Project the fact state that a clean resume would load.

    Facts accepted earlier in the same extraction invocation are persisted and
    compiled before a clean resume.  Compile them before every later batch too,
    then replace same-id baseline facts with the compiler-owned row so an
    in-process prompt and its resumed prompt have identical semantic context.
    """

    merged_by_fact_id: dict[str, Mapping[str, Any]] = {}
    rows_without_fact_id: list[Mapping[str, Any]] = []
    for row in current_facts:
        payload = (
            dict(row)
            if isinstance(row, Mapping)
            else dict(row.to_dict())
        )
        fact_id = str(payload.get("fact_id") or "")
        if fact_id:
            merged_by_fact_id[fact_id] = payload
        else:
            rows_without_fact_id.append(payload)
    if accepted_claims:
        compilation = EvidenceFactCompiler().compile(
            target_id=target_id,
            as_of_date=as_of_date,
            accepted_claims=accepted_claims,
        )
        for fact in compilation.facts:
            merged_by_fact_id[fact.fact_id] = fact.to_dict()
    return project_fact_extraction_evidence_context(
        (
            *rows_without_fact_id,
            *(
                merged_by_fact_id[fact_id]
                for fact_id in sorted(merged_by_fact_id)
            ),
        )
    )


def _current_document_ids_for_lineage_row(
    row: Mapping[str, Any],
    *,
    current_document_ids: frozenset[str],
) -> frozenset[str]:
    linked_ids = {
        str(value)
        for value in row.get("source_ids") or ()
        if str(value) in current_document_ids
    }
    document_id = str(row.get("document_id") or "")
    if document_id in current_document_ids:
        linked_ids.add(document_id)
    return frozenset(linked_ids)


def _current_fact_lineage_rematerialization_gaps(
    *,
    current_facts: Sequence[Mapping[str, Any]],
    current_document_ids: frozenset[str],
    compilation: FactCompilationResult,
) -> Mapping[str, tuple[str, ...]]:
    """Find current-roster facts absent from the newly compiled fact graph.

    ``current_facts`` is prompt context, not compiler input.  A document that
    leaves and later re-enters the source roster can therefore expose an old
    fact to the provider even when its durable claim/disposition checkpoint is
    absent.  If the provider avoids re-emitting that apparent duplicate, the
    compiler would otherwise retire the fact silently.

    An old fact is reconciled only when its exact id remains in the new graph,
    or a new claim/fact link explicitly names that id in ``supersedes`` or
    ``resolves`` lineage.  A source outside the current document roster is not
    constrained here; ordinary roster retirement remains allowed.
    """

    compiled_fact_by_id = {
        row.fact_id: row.to_dict() for row in compilation.facts
    }
    explicitly_reconciled_fact_ids = {
        fact_id
        for link in compilation.claim_fact_links
        for fact_id in (*link.supersedes_fact_ids, *link.resolves_fact_ids)
        if fact_id != link.fact_id
    }
    gaps_by_document: dict[str, set[str]] = {}
    for row in current_facts:
        linked_document_ids = _current_document_ids_for_lineage_row(
            row,
            current_document_ids=current_document_ids,
        )
        if not linked_document_ids:
            continue
        fact_id = str(row.get("fact_id") or "").strip()
        if not fact_id:
            raise ValueError(
                "current fact linked to the current source roster lacks fact_id"
            )
        if fact_id in explicitly_reconciled_fact_ids:
            continue
        compiled_row = compiled_fact_by_id.get(fact_id)
        gap_document_ids = set(linked_document_ids)
        if compiled_row is not None:
            old_source_ids = {
                str(value)
                for value in row.get("source_ids") or ()
                if str(value)
            }
            compiled_source_ids = {
                str(value)
                for value in compiled_row.get("source_ids") or ()
                if str(value)
            }
            required_current_source_ids = (
                old_source_ids & set(current_document_ids)
            )
            missing_current_source_ids = (
                required_current_source_ids - compiled_source_ids
            )
            all_old_sources_are_current = bool(old_source_ids) and (
                old_source_ids <= set(current_document_ids)
            )
            old_claim_ids = {
                str(value)
                for value in row.get("claim_ids") or ()
                if str(value)
            }
            compiled_claim_ids = {
                str(value)
                for value in compiled_row.get("claim_ids") or ()
                if str(value)
            }
            old_quote_ids = {
                str(value)
                for value in row.get("quote_ids") or ()
                if str(value)
            }
            compiled_quote_ids = {
                str(value)
                for value in compiled_row.get("quote_ids") or ()
                if str(value)
            }
            lineage_set_fields = (
                "claim_ids",
                "quote_ids",
                "corroborating_independence_groups",
                "question_family_tags",
                "primitive_tags",
                "allowed_component_ids",
                "structured_evidence_roles",
            )
            lineage_set_regressed = all_old_sources_are_current and any(
                {
                    str(value)
                    for value in row.get(field) or ()
                    if str(value)
                }
                - {
                    str(value)
                    for value in compiled_row.get(field) or ()
                    if str(value)
                }
                for field in lineage_set_fields
            )
            confidence_regressed = all_old_sources_are_current and (
                float(compiled_row.get("confidence") or 0.0) + 1e-12
                < float(row.get("confidence") or 0.0)
            )
            exact_lineage_roster_unchanged = bool(
                all_old_sources_are_current
                and old_source_ids == compiled_source_ids
                and old_claim_ids == compiled_claim_ids
                and old_quote_ids == compiled_quote_ids
            )
            primary_lineage_changed_in_place = bool(
                exact_lineage_roster_unchanged
                and (
                    tuple(row.get("claim_ids") or ())
                    != tuple(compiled_row.get("claim_ids") or ())
                    or str(row.get("source_independence_group") or "")
                    != str(
                        compiled_row.get("source_independence_group") or ""
                    )
                )
            )
            # If only part of a corroborated fact's source roster remains
            # current, retired support may legitimately disappear.  The
            # surviving fact must nevertheless retain at least one immutable
            # claim and quote from its current support; otherwise a new claim
            # with the same economic identity could silently replace all old
            # lineage while keeping the same deterministic fact id.
            mixed_source_lineage_replaced = bool(
                required_current_source_ids
                and not all_old_sources_are_current
                and (
                    not (old_claim_ids & compiled_claim_ids)
                    or not (old_quote_ids & compiled_quote_ids)
                )
            )
            if not (
                missing_current_source_ids
                or lineage_set_regressed
                or confidence_regressed
                or mixed_source_lineage_replaced
                or primary_lineage_changed_in_place
            ):
                continue
            # When the missing source is known, rematerialize that exact
            # current document.  A claim/quote/metadata regression cannot be
            # mapped back to one source from an EvidenceFact row alone, so the
            # complete current lineage unit must be reconsidered.
            gap_document_ids = (
                missing_current_source_ids or set(linked_document_ids)
            )
        for document_id in gap_document_ids:
            gaps_by_document.setdefault(document_id, set()).add(fact_id)
    return {
        document_id: tuple(sorted(fact_ids))
        for document_id, fact_ids in sorted(gaps_by_document.items())
    }


def _atomic_fact_lineage_rematerialization_document_ids(
    *,
    initial_document_ids: Sequence[str],
    provider_calls: Sequence[FactExtractionProviderCall],
    current_document_ids: frozenset[str],
) -> tuple[str, ...]:
    """Expand a gap to the complete transitive provider-call unit."""

    affected = {
        str(value)
        for value in initial_document_ids
        if str(value) in current_document_ids
    }
    changed = True
    while changed:
        changed = False
        for call in provider_calls:
            call_document_ids = set(call.document_ids) & set(
                current_document_ids
            )
            if (
                affected & call_document_ids
                and not call_document_ids <= affected
            ):
                affected.update(call_document_ids)
                changed = True
    return tuple(sorted(affected))


def _batch_current_fact_lineage_pending_reasons(
    *,
    current_facts: Sequence[Mapping[str, Any]],
    batch_document_ids: frozenset[str],
    accepted_claims: Sequence[Mapping[str, Any]],
    target_id: str,
    as_of_date: str,
) -> tuple[str, ...]:
    """Fail a terminal batch response that silently drops a current fact.

    This check intentionally runs only after all deterministic response
    validation for one observable parent batch.  Its pending reason enters the
    ordinary validation-retry path, which invalidates a cached Collaboration
    response and gives the rewrite request a distinct identity.  Because
    ``EvidenceFact`` carries parent-document, not exact transport-chunk,
    lineage, the caller invokes this for an unsplit batch or only after the
    final chunk of a split parent.
    """

    if not batch_document_ids:
        return ()
    batch_current_facts = tuple(
        row
        for row in current_facts
        if _current_document_ids_for_lineage_row(
            row,
            current_document_ids=batch_document_ids,
        )
    )
    if not batch_current_facts:
        return ()
    claim_by_id: dict[str, Mapping[str, Any]] = {}
    for claim in accepted_claims:
        claim_id = str(claim.get("claim_id") or "").strip()
        if not claim_id:
            continue
        claim_by_id[claim_id] = claim
    compilation = EvidenceFactCompiler().compile(
        target_id=target_id,
        as_of_date=as_of_date,
        accepted_claims=tuple(claim_by_id.values()),
    )
    gaps = _current_fact_lineage_rematerialization_gaps(
        current_facts=batch_current_facts,
        current_document_ids=batch_document_ids,
        compilation=compilation,
    )
    return tuple(
        "CURRENT_FACT_LINEAGE_REMATERIALIZATION_REQUIRED:" + document_id
        for document_id in gaps
    )


def _canonical_downstream_fact_input_hash(
    *,
    claims: Sequence[Mapping[str, Any]],
    dispositions: Sequence[Mapping[str, Any]],
    pending: Sequence[str],
    split_chunk_ids_by_document: Mapping[str, tuple[str, ...]],
    pending_transport_chunk_ids: set[str],
    target_id: str,
    as_of_date: str,
) -> str:
    """Hash only parent-complete fact inputs consumed downstream."""

    canonical_claims, canonical_dispositions, _ = (
        _reconcile_transport_chunks(
            claims=claims,
            dispositions=dispositions,
            pending=pending,
            split_chunk_ids_by_document=split_chunk_ids_by_document,
            pending_transport_chunk_ids=pending_transport_chunk_ids,
            target_id=target_id,
            as_of_date=as_of_date,
        )
    )

    def canonical_json(row: Mapping[str, Any]) -> str:
        return json.dumps(
            dict(row),
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )

    return stable_intelligence_id(
        "FACTDOWNSTREAM",
        {
            "claims": [
                json.loads(value)
                for value in sorted(
                    canonical_json(row) for row in canonical_claims
                )
            ],
            "dispositions": [
                json.loads(value)
                for value in sorted(
                    canonical_json(row)
                    for row in canonical_dispositions
                )
            ],
        },
    )


class ResearcherEvidenceFactExtractor:
    """Extract and verify facts from every supplied full document.

    ``documents_per_call`` is only a prompt-transport chunk size.  Every input
    document is processed, so it cannot become a research-completion cap.
    """

    def __init__(
        self,
        *,
        provider: StructuredResearchProvider,
        documents_per_call: int = 1,
        max_document_chars_per_call: int = 220_000,
    ) -> None:
        if (
            isinstance(documents_per_call, bool)
            or not isinstance(documents_per_call, int)
            or documents_per_call <= 0
        ):
            raise ValueError("documents_per_call must be a positive transport chunk")
        if (
            isinstance(max_document_chars_per_call, bool)
            or max_document_chars_per_call < 10_000
        ):
            raise ValueError("fact extraction character transport bound is too small")
        self.provider = provider
        self.documents_per_call = documents_per_call
        self.max_document_chars_per_call = max_document_chars_per_call

    def extract(
        self,
        *,
        target_id: str,
        target_name: str,
        target_aliases: Sequence[str],
        archetype_id: str,
        as_of_date: str,
        documents: Sequence[Mapping[str, Any]],
        open_objectives: Sequence[Mapping[str, Any]],
        current_facts: Sequence[Mapping[str, Any]] = (),
        score_gap_context: Mapping[str, Any] | None = None,
        prior_material_claims: Sequence[Mapping[str, Any]] = (),
        prior_document_dispositions: Sequence[Mapping[str, Any]] = (),
        prior_provider_calls: Sequence[
            FactExtractionProviderCall | Mapping[str, Any]
        ] = (),
        prior_rejections: Sequence[
            FactExtractionRejection | Mapping[str, Any]
        ] = (),
        prior_coverage_refresh_document_ids: Sequence[str] = (),
        prior_current_lineage_objective_reassessment_document_ids: (
            Sequence[str]
        ) = (),
        prior_semantics_recovery_document_ids: Sequence[str] = (),
        prior_semantics_recovery_invalidated_claim_count: int = 0,
        authoritative_fact_ledger: (
            AuthoritativeResearchEpochFactLedger | None
        ) = None,
        current_fact_lineage_recovery_binding: (
            CurrentFactLineageRecoveryBinding | None
        ) = None,
        extraction_mode: str = "RESEARCH_BACKFILL",
    ) -> ResearcherFactExtractionResult:
        cutoff = date.fromisoformat(as_of_date)
        if not target_id.strip() or not target_name.strip() or not archetype_id.strip():
            raise ValueError("fact extraction target identity is incomplete")
        if extraction_mode not in FACT_EXTRACTION_MODES:
            raise ValueError("unknown fact extraction mode")
        prepared = _validate_documents(
            documents,
            target_id=target_id,
            as_of_date=as_of_date,
            cutoff=cutoff,
        )
        source_boundary_context_by_document_id = (
            _source_boundary_context_by_document_id(prepared)
        )
        objective_ids = {
            str(row.get("objective_id") or "").strip()
            for row in open_objectives
        }
        if "" in objective_ids or len(objective_ids) != len(open_objectives):
            raise ValueError("fact extraction objectives require unique ids")
        objective_component_by_id = {
            str(row.get("objective_id") or "").strip(): str(
                row.get("component_id") or ""
            ).strip()
            for row in open_objectives
        }
        objective_scope_by_document: Mapping[str, frozenset[str]] | None = None
        if extraction_mode == "PRODUCTION_OBJECTIVE_LOCAL":
            if not objective_ids:
                raise ValueError(
                    "production objective-local extraction requires open objectives"
                )
            invalid_objective_component_ids = sorted(
                objective_id
                for objective_id, component_id
                in objective_component_by_id.items()
                if component_id not in CANONICAL_COMPONENT_ORDER
            )
            if invalid_objective_component_ids:
                raise ValueError(
                    "production objectives require canonical component ids:"
                    + ",".join(invalid_objective_component_ids)
                )
            objective_scope_by_document = {
                str(document["document_id"]): frozenset(
                    str(value).strip()
                    for value in document.get("objective_ids") or ()
                    if str(value).strip() in objective_ids
                )
                for document in prepared
            }
            unlinked = sorted(
                document_id
                for document_id, linked_ids in objective_scope_by_document.items()
                if not linked_ids
            )
            if unlinked:
                raise ValueError(
                    "production evidence documents lack current objective lineage:"
                    + ",".join(unlinked)
                )
        scope_contract = load_mechanism_scope_contracts().get(archetype_id)
        if scope_contract is None:
            raise ValueError("fact extraction archetype lacks mechanism-scope contract")
        document_ids = {str(row["document_id"]) for row in prepared}
        carried_coverage_refresh_document_ids = tuple(
            dict.fromkeys(
                str(value).strip()
                for value in prior_coverage_refresh_document_ids
                if str(value).strip()
            )
        )
        if any(
            document_id not in document_ids
            for document_id in carried_coverage_refresh_document_ids
        ):
            raise ValueError(
                "prior coverage refresh intent is outside current documents"
            )
        carried_current_lineage_objective_reassessment_document_ids = tuple(
            dict.fromkeys(
                str(value).strip()
                for value in (
                    prior_current_lineage_objective_reassessment_document_ids
                )
                if str(value).strip()
            )
        )
        if any(
            document_id not in document_ids
            for document_id in (
                carried_current_lineage_objective_reassessment_document_ids
            )
        ):
            raise ValueError(
                "prior current-lineage objective reassessment intent is "
                "outside current documents"
            )
        coverage_gap_objective_ids = _coverage_gap_objective_ids(
            open_objectives=open_objectives,
            score_gap_context=score_gap_context or {},
        )
        document_by_id = {
            str(row["document_id"]): row for row in prepared
        }
        if (
            current_fact_lineage_recovery_binding is not None
            and authoritative_fact_ledger is None
        ):
            raise ValueError(
                "current fact lineage recovery binding requires its "
                "authoritative research-epoch fact ledger"
            )
        current_lineage_recovery: Mapping[str, Any] | None = None
        if authoritative_fact_ledger is not None:
            try:
                current_lineage_recovery = (
                    _recover_current_fact_lineage_authority_gap(
                        authoritative_fact_ledger=authoritative_fact_ledger,
                        recovery_binding=(
                            current_fact_lineage_recovery_binding
                        ),
                        target_id=target_id,
                        target_name=target_name,
                        target_aliases=target_aliases,
                        archetype_id=archetype_id,
                        as_of_date=as_of_date,
                        documents=prepared,
                        open_objectives=open_objectives,
                        current_facts=current_facts,
                        score_gap_context=score_gap_context or {},
                        prior_material_claims=prior_material_claims,
                        prior_document_dispositions=(
                            prior_document_dispositions
                        ),
                        scope_contract=scope_contract,
                        objective_scope_by_document=(
                            objective_scope_by_document
                        ),
                        objective_component_by_id=objective_component_by_id,
                    )
                )
            except (
                FileNotFoundError,
                OSError,
                KeyError,
                TypeError,
                ValueError,
                RuntimeError,
                json.JSONDecodeError,
            ) as exc:
                current_lineage_recovery = {
                    "status": "PENDING",
                    "pending_reason": (
                        "CURRENT_FACT_LINEAGE_JOURNAL_RECOVERY_INVALID:"
                        f"{type(exc).__name__}:{_clean_error(exc)}"
                    ),
                    "provider_complete_call_count": 0,
                    "recovered_claim_count": 0,
                    "recovered_fact_count": 0,
                    "recovered_document_count": 0,
                    "objective_reassessment_rows": (),
                }
        current_lineage_recovery_succeeded = bool(
            current_lineage_recovery is not None
            and current_lineage_recovery.get("status") == "COMPLETE"
        )
        current_lineage_recovery_phase = bool(
            current_fact_lineage_recovery_binding is not None
            or (
                current_lineage_recovery is not None
                and current_lineage_recovery.get("status")
                not in {"NO_AUTHORITY_LOSS"}
            )
        )
        if current_lineage_recovery_succeeded:
            assert current_lineage_recovery is not None
            prior_material_claims = (
                *prior_material_claims,
                *current_lineage_recovery["material_claims"],
            )
            prior_document_dispositions = (
                *prior_document_dispositions,
                *current_lineage_recovery["document_dispositions"],
            )
            prior_provider_calls = (
                *prior_provider_calls,
                *current_lineage_recovery["provider_calls"],
            )
        semantics_recovery_requested = bool(
            prior_semantics_recovery_document_ids
            or prior_semantics_recovery_invalidated_claim_count
        )
        semantics_recovery: Mapping[str, Any] | None = None
        if semantics_recovery_requested:
            try:
                semantics_recovery = _recover_v4_fact_semantics_checkpoint(
                    self.provider,
                    target_id=target_id,
                    target_name=target_name,
                    target_aliases=target_aliases,
                    archetype_id=archetype_id,
                    as_of_date=as_of_date,
                    documents=prepared,
                    source_boundary_context_by_document_id=(
                        source_boundary_context_by_document_id
                    ),
                    max_document_chars_per_call=(
                        self.max_document_chars_per_call
                    ),
                    open_objectives=open_objectives,
                    scope_contract=scope_contract,
                    objective_scope_by_document=(
                        objective_scope_by_document
                    ),
                    objective_component_by_id=objective_component_by_id,
                    recovery_document_ids=(
                        prior_semantics_recovery_document_ids
                    ),
                    expected_invalidated_claim_count=(
                        prior_semantics_recovery_invalidated_claim_count
                    ),
                    prior_material_claims=prior_material_claims,
                    prior_document_dispositions=(
                        prior_document_dispositions
                    ),
                    prior_provider_calls=prior_provider_calls,
                )
            except (KeyError, OSError, TypeError, ValueError, RuntimeError):
                semantics_recovery = None
        semantics_recovery_succeeded = (
            isinstance(semantics_recovery, Mapping)
            and semantics_recovery.get("status") == "COMPLETE"
        )
        semantics_recovery_absent = (
            isinstance(semantics_recovery, Mapping)
            and semantics_recovery.get("status") == "ABSENT"
        )
        semantics_recovery_failed = (
            semantics_recovery_requested
            and not semantics_recovery_succeeded
            and not semantics_recovery_absent
        )
        if semantics_recovery_succeeded:
            assert semantics_recovery is not None
            prior_material_claims = (
                *prior_material_claims,
                *semantics_recovery["material_claims"],
            )
            prior_document_dispositions = (
                *prior_document_dispositions,
                *semantics_recovery["document_dispositions"],
            )
            prior_provider_calls = (
                *prior_provider_calls,
                *semantics_recovery["provider_calls"],
            )
            prior_rejections = (
                *prior_rejections,
                *semantics_recovery["rejections"],
            )
        stale_semantics_disposition_count = sum(
            _fact_semantics_upgrade_requires_reextraction(
                previous_version=_extraction_semantics_version(row),
                document=document_by_id.get(
                    str(row.get("document_id") or "")
                ),
            )
            for row in prior_document_dispositions
        )
        stale_semantics_provider_call_count = sum(
            any(
                _fact_semantics_upgrade_requires_reextraction(
                    previous_version=_extraction_semantics_version(row),
                    document=document_by_id.get(document_id),
                )
                for document_id in (
                    row.document_ids
                    if isinstance(row, FactExtractionProviderCall)
                    else tuple(row.get("document_ids") or ())
                )
            )
            for row in prior_provider_calls
        )
        all_prior_dispositions = [
            dict(row) for row in prior_document_dispositions
        ]
        all_prior_disposition_ids = [
            str(row.get("document_id") or "")
            for row in all_prior_dispositions
        ]
        stale_semantics_disposition_ids = {
            str(row.get("document_id") or "")
            for row in all_prior_dispositions
            if _fact_semantics_upgrade_requires_reextraction(
                previous_version=_extraction_semantics_version(row),
                document=document_by_id.get(
                    str(row.get("document_id") or "")
                ),
            )
        }
        if (
            any(
                not value or value not in document_ids
                for value in all_prior_disposition_ids
            )
            or len(all_prior_disposition_ids)
            != len(set(all_prior_disposition_ids))
        ):
            raise ValueError("prior fact dispositions are stale or duplicated")
        all_checkpoint_calls = [
            _coerce_provider_call(row) for row in prior_provider_calls
        ]
        if any(row.status != "COMPLETE" for row in all_checkpoint_calls):
            raise ValueError("only completed fact provider calls may be resumed")
        boundary_context_reextraction_document_ids = (
            _boundary_context_reextraction_document_ids(
                documents=prepared,
                source_boundary_context_by_document_id=(
                    source_boundary_context_by_document_id
                ),
                prior_material_claims=prior_material_claims,
                prior_document_dispositions=all_prior_dispositions,
                prior_provider_calls=all_checkpoint_calls,
            )
        )
        effective_current_facts = tuple(
            row
            for row in current_facts
            if not (
                {
                    str(value)
                    for value in row.get("source_ids") or ()
                    if str(value)
                }
                & boundary_context_reextraction_document_ids
            )
            and str(row.get("document_id") or "")
            not in boundary_context_reextraction_document_ids
        )
        raw_coverage_complete_document_ids = {
            document_id
            for call in all_checkpoint_calls
            if call.coverage_audit_performed
            and call.extraction_semantics_version
            == FACT_EXTRACTION_SEMANTICS_VERSION
            for document_id in call.document_ids
        }
        previously_coverage_audited_document_ids = {
            document_id
            for call in all_checkpoint_calls
            if call.coverage_audit_performed
            for document_id in call.document_ids
        }
        stale_semantics_document_ids = (
            stale_semantics_disposition_ids
            | {
                document_id
                for call in all_checkpoint_calls
                for document_id in call.document_ids
                if _fact_semantics_upgrade_requires_reextraction(
                    previous_version=call.extraction_semantics_version,
                    document=document_by_id.get(document_id),
                )
            }
        )
        prior_disposition_by_document_id = {
            str(row.get("document_id") or ""): row
            for row in all_prior_dispositions
        }
        bounded_stale_coverage_refresh_document_ids = (
            _bounded_stale_coverage_refresh_document_ids(
                documents=prepared,
                prior_disposition_by_document_id=(
                    prior_disposition_by_document_id
                ),
                stale_semantics_document_ids=(
                    stale_semantics_document_ids
                ),
                coverage_complete_document_ids=(
                    raw_coverage_complete_document_ids
                    - set(carried_coverage_refresh_document_ids)
                ),
                previously_coverage_audited_document_ids=(
                    previously_coverage_audited_document_ids
                ),
                coverage_gap_objective_ids=(
                    coverage_gap_objective_ids
                ),
            )
            if extraction_mode == "PRODUCTION_OBJECTIVE_LOCAL"
            else frozenset()
        )
        regular_live_gap_document_ids = {
            str(document["document_id"])
            for document in prepared
            if bool(
                set(document.get("objective_ids") or ())
                & coverage_gap_objective_ids
            )
        }
        live_gap_lineage_document_ids = {
            str(document["document_id"])
            for document in prepared
            if bool(
                {
                    str(value).strip()
                    for key in (
                        "objective_ids",
                        "historical_objective_ids",
                    )
                    for value in document.get(key) or ()
                    if str(value).strip()
                }
                & coverage_gap_objective_ids
            )
        }
        current_lineage_objective_reassessment_document_ids = tuple(
            sorted(
                set(
                    carried_current_lineage_objective_reassessment_document_ids
                )
                | {
                    str(row.get("document_id") or "")
                    for row in (
                        current_lineage_recovery.get(
                            "objective_reassessment_rows"
                        )
                        or ()
                        if current_lineage_recovery is not None
                        else ()
                    )
                    if str(row.get("document_id") or "")
                }
            )
        )
        active_carried_coverage_refresh_document_ids = frozenset(
            carried_coverage_refresh_document_ids
            if extraction_mode != "PRODUCTION_OBJECTIVE_LOCAL"
            else (
                (
                    set(carried_coverage_refresh_document_ids)
                    & live_gap_lineage_document_ids
                )
                | set(
                    current_lineage_objective_reassessment_document_ids
                )
            )
        )
        coverage_complete_document_ids = (
            raw_coverage_complete_document_ids
            - active_carried_coverage_refresh_document_ids
        )
        cross_objective_coverage_refresh_document_ids = frozenset(
            set(bounded_stale_coverage_refresh_document_ids)
            | (
                set(active_carried_coverage_refresh_document_ids)
                & stale_semantics_document_ids
            )
        )
        coverage_refresh_document_ids = {
            str(document["document_id"])
            for document in prepared
            if str(document["document_id"])
            in set(all_prior_disposition_ids)
            and str(document["document_id"])
            not in coverage_complete_document_ids
            and (
                str(document["document_id"])
                in bounded_stale_coverage_refresh_document_ids
                or bool(
                    set(document.get("objective_ids") or ())
                    & coverage_gap_objective_ids
                )
            )
        }
        coverage_refresh_document_ids.update(
            active_carried_coverage_refresh_document_ids
        )
        coverage_refresh_document_ids.difference_update(
            boundary_context_reextraction_document_ids
        )
        new_unprocessed_document_ids = {
            str(document["document_id"])
            for document in prepared
            if (
                str(document["document_id"])
                not in set(all_prior_disposition_ids)
                or str(document["document_id"])
                in boundary_context_reextraction_document_ids
            )
            and str(document["document_id"])
            not in coverage_refresh_document_ids
        }
        deferred_coverage_refresh_document_ids = set()
        if new_unprocessed_document_ids:
            # A newly fetched document can change the canonical fact state and
            # therefore the gap that requested a stale coverage re-audit.  Drain
            # the new source first and keep every prior disposition intact for
            # this checkpoint.  The canonical-state barrier then recomputes the
            # gap; if the re-audit is still required, the next clean resume sees
            # the same prior disposition and performs it.  Removing the prior
            # disposition before an unprocessed new document would lose that
            # durable refresh intent when a collaboration response is pending.
            deferred_coverage_refresh_document_ids = set(
                coverage_refresh_document_ids
            )
            coverage_refresh_document_ids = set()
        coverage_refresh_objective_scope_by_document = (
            {
                document_id: (
                    frozenset(
                        set(objective_scope_by_document[document_id])
                        | set(coverage_gap_objective_ids)
                    )
                    if document_id
                    in cross_objective_coverage_refresh_document_ids
                    else objective_scope_by_document[document_id]
                )
                for document in prepared
                if (
                    document_id := str(document["document_id"])
                )
                in coverage_refresh_document_ids
            }
            if objective_scope_by_document is not None
            else {}
        )
        retained_prior_disposition_ids = (
            set(all_prior_disposition_ids)
            - coverage_refresh_document_ids
            - boundary_context_reextraction_document_ids
        )
        dispositions: list[Mapping[str, Any]] = [
            row
            for row in all_prior_dispositions
            if str(row.get("document_id") or "")
            in retained_prior_disposition_ids
        ]
        claims: list[Mapping[str, Any]] = [
            dict(row)
            for row in prior_material_claims
            if str(row.get("document_id") or "")
            not in boundary_context_reextraction_document_ids
        ]
        claim_ids = [str(row.get("claim_id") or "") for row in claims]
        if any(not value for value in claim_ids) or len(claim_ids) != len(set(claim_ids)):
            raise ValueError("prior material claims require unique ids")
        if any(
            str(row.get("document_id") or "")
            not in set(all_prior_disposition_ids)
            or str(row.get("target_id") or "") != target_id
            or str(row.get("as_of_date") or "") != as_of_date
            for row in claims
        ):
            raise ValueError("prior material claims are outside resumed document scope")
        rejections: list[FactExtractionRejection] = [
            _coerce_rejection(row)
            for row in prior_rejections
            if str(
                row.document_id
                if isinstance(row, FactExtractionRejection)
                else row.get("document_id") or ""
            )
            not in boundary_context_reextraction_document_ids
        ]
        pending: list[str] = []
        if current_lineage_recovery is not None and not (
            current_lineage_recovery_succeeded
            or current_lineage_recovery.get("status")
            == "NO_AUTHORITY_LOSS"
        ):
            pending.append(
                str(
                    current_lineage_recovery.get("pending_reason")
                    or "CURRENT_FACT_LINEAGE_JOURNAL_RECOVERY_PENDING"
                )
            )
        pending.extend(
            "CURRENT_FACT_LINEAGE_OBJECTIVE_REASSESSMENT_REQUIRED:"
            + document_id
            for document_id in (
                current_lineage_objective_reassessment_document_ids
            )
        )
        if semantics_recovery_failed:
            pending.append(
                "FACT_SEMANTICS_MIGRATION_RECOVERY_INCOMPLETE"
            )
        provider_name = str(
            getattr(self.provider, "provider_name", type(self.provider).__name__)
        )
        parent_disposition_ids = set(retained_prior_disposition_ids)
        remaining = tuple(
            row
            for row in prepared
            if str(row["document_id"]) not in parent_disposition_ids
        )
        coverage_required_document_ids = {
            str(document["document_id"])
            for document in prepared
            if (
                str(document["document_id"])
                in coverage_refresh_document_ids
                or (
                    (
                        str(document["document_id"])
                        not in set(all_prior_disposition_ids)
                        or str(document["document_id"])
                        in boundary_context_reextraction_document_ids
                    )
                    and bool(
                        set(document.get("objective_ids") or ())
                        & coverage_gap_objective_ids
                    )
                )
            )
        }
        all_transport_documents = tuple(
            chunk
            for document in remaining
            for chunk in _document_transport_chunks(
                document,
                max_chars=self.max_document_chars_per_call,
                source_boundary_context=(
                    source_boundary_context_by_document_id.get(
                        str(document["document_id"])
                    )
                ),
            )
        )
        split_chunk_ids_by_document = _split_chunk_ids_by_document(
            all_transport_documents
        )
        (
            resumed_transport_calls,
            resumed_transport_claims,
            resumed_transport_dispositions,
            resumed_transport_chunk_ids,
        ) = _resume_completed_transport_chunks(
            calls=tuple(
                call
                for call in all_checkpoint_calls
                if not (
                    set(call.document_ids)
                    & boundary_context_reextraction_document_ids
                )
                and (
                    not (
                        set(call.document_ids)
                        & coverage_refresh_document_ids
                    )
                    or (
                        call.coverage_audit_performed
                        and call.extraction_semantics_version
                        == FACT_EXTRACTION_SEMANTICS_VERSION
                    )
                )
            ),
            transport_documents=all_transport_documents,
            target_id=target_id,
            as_of_date=as_of_date,
        )
        calls: list[FactExtractionProviderCall] = [
            row
            for row in all_checkpoint_calls
            if set(row.document_ids).issubset(
                set(all_prior_disposition_ids)
            )
            and not (
                set(row.document_ids)
                & boundary_context_reextraction_document_ids
            )
        ]
        checkpoint_call_object_ids = {id(row) for row in calls}
        calls.extend(
            row
            for row in resumed_transport_calls
            if id(row) not in checkpoint_call_object_ids
        )
        claims.extend(resumed_transport_claims)
        dispositions.extend(resumed_transport_dispositions)
        research_gap_feedback: list[str] = [
            reason for row in calls for reason in row.research_gap_feedback
        ]
        transport_documents = tuple(
            row
            for row in all_transport_documents
            if str(row.get("transport_chunk_id") or "")
            not in resumed_transport_chunk_ids
        )
        pending_transport_chunk_ids: set[str] = set()
        provider_circuit_breaker_open = False
        current_fact_prompt_context = (
            _project_current_facts_with_accepted_claims(
                current_facts=effective_current_facts,
                accepted_claims=claims,
                target_id=target_id,
                as_of_date=as_of_date,
            )
        )
        maximum_current_fact_prompt_count = int(
            current_fact_prompt_context.get("fact_count") or 0
        )
        maximum_current_fact_prompt_context_chars = _json_character_count(
            current_fact_prompt_context
        )
        effective_score_gap_context = dict(score_gap_context or {})
        if current_lineage_objective_reassessment_document_ids:
            raw_prior_feedback = effective_score_gap_context.get(
                "prior_fact_extraction_feedback",
                (),
            )
            if isinstance(raw_prior_feedback, (str, bytes)) or not (
                isinstance(raw_prior_feedback, Sequence)
            ):
                raise ValueError(
                    "current-lineage objective reassessment requires raw "
                    "fact feedback rows"
                )
            effective_score_gap_context[
                "prior_fact_extraction_feedback"
            ] = list(
                dict.fromkeys(
                    (
                        *(str(value) for value in raw_prior_feedback),
                        *(
                            "FACT_EXTRACTION_RETRY_CONTEXT:"
                            "CURRENT_FACT_LINEAGE_OBJECTIVE_"
                            "REASSESSMENT_REQUIRED:"
                            + document_id
                            for document_id in (
                                current_lineage_objective_reassessment_document_ids
                            )
                        ),
                    )
                )
            )
        score_gap_prompt_context = project_fact_extraction_score_gap_context(
            effective_score_gap_context
        )
        score_gap_prompt_context_chars = _json_character_count(
            score_gap_prompt_context
        )
        max_primary_payload_chars = 0
        max_attempt_payload_chars = 0
        max_full_document_chars = max(
            (len(str(row.get("content_text") or "")) for row in prepared),
            default=0,
        )
        max_transport_chunk_chars = 0
        max_contextual_transport_chars = 0
        pagination_continuation_call_count = 0
        maximum_pagination_page_count = 1
        coverage_audit_call_count = 0
        coverage_audit_document_ids: set[str] = set()
        coverage_audit_new_fact_count = 0
        coverage_refresh_transport_documents = tuple(
            row
            for row in transport_documents
            if str(row["document_id"])
            in coverage_refresh_document_ids
        )
        primary_transport_documents = tuple(
            row
            for row in transport_documents
            if str(row["document_id"])
            not in coverage_refresh_document_ids
        )
        document_batches = (
            ()
            if semantics_recovery_failed or current_lineage_recovery_phase
            else (
                *_document_batches(
                    coverage_refresh_transport_documents,
                    max_documents=self.documents_per_call,
                    max_chars=self.max_document_chars_per_call,
                ),
                *_document_batches(
                    primary_transport_documents,
                    max_documents=self.documents_per_call,
                    max_chars=self.max_document_chars_per_call,
                ),
            )
        )
        canonical_state_refresh_barrier_count = 0
        if current_lineage_recovery_succeeded and transport_documents:
            # Journal recovery changes the canonical claim/fact/disposition
            # state.  Persist that atomic recovery before opening requests for
            # documents outside the sealed recovery closure.  Otherwise the
            # deliberately empty batch schedule below can produce a pending
            # result with no machine-readable reason.
            pending.append(
                FACT_EXTRACTION_CANONICAL_STATE_REFRESH_REQUIRED
            )
            canonical_state_refresh_barrier_count += 1
        for batch_index, batch in enumerate(document_batches):
            downstream_input_hash_before_batch = (
                _canonical_downstream_fact_input_hash(
                    claims=claims,
                    dispositions=dispositions,
                    pending=pending,
                    split_chunk_ids_by_document=(
                        split_chunk_ids_by_document
                    ),
                    pending_transport_chunk_ids=(
                        pending_transport_chunk_ids
                    ),
                    target_id=target_id,
                    as_of_date=as_of_date,
                )
            )
            current_fact_prompt_context = (
                _project_current_facts_with_accepted_claims(
                    current_facts=effective_current_facts,
                    accepted_claims=claims,
                    target_id=target_id,
                    as_of_date=as_of_date,
                )
            )
            maximum_current_fact_prompt_count = max(
                maximum_current_fact_prompt_count,
                int(current_fact_prompt_context.get("fact_count") or 0),
            )
            maximum_current_fact_prompt_context_chars = max(
                maximum_current_fact_prompt_context_chars,
                _json_character_count(current_fact_prompt_context),
            )
            batch_identity = {
                "target_id": target_id,
                "as_of_date": as_of_date,
                "extraction_semantics_version": (
                    FACT_EXTRACTION_SEMANTICS_VERSION
                ),
                "document_ids": [str(row["document_id"]) for row in batch],
            }
            batch_document_ids = {
                str(row["document_id"]) for row in batch
            }
            coverage_only_batch = bool(batch_document_ids) and (
                batch_document_ids
                <= coverage_refresh_document_ids
            )
            batch_objective_scope_by_document = (
                {
                    document_id: (
                        coverage_refresh_objective_scope_by_document[
                            document_id
                        ]
                    )
                    for document_id in batch_document_ids
                }
                if coverage_only_batch
                and objective_scope_by_document is not None
                else objective_scope_by_document
            )
            objective_lineage_reassessment_rows = [
                {
                    "document_id": document_id,
                    "prior_current_objective_ids": sorted(
                        objective_scope_by_document[document_id]
                    ),
                    "current_open_objective_candidates": sorted(
                        batch_objective_scope_by_document[document_id]
                    ),
                }
                for document_id in sorted(batch_document_ids)
                if (
                    coverage_only_batch
                    and objective_scope_by_document is not None
                    and batch_objective_scope_by_document is not None
                    and batch_objective_scope_by_document[document_id]
                    != objective_scope_by_document[document_id]
                )
            ]
            batch_transport_chunk_ids = _batch_transport_chunk_ids(batch)
            if any(
                int(row.get("transport_chunk_count") or 1) > 1
                for row in batch
            ):
                batch_identity["transport_chunk_ids"] = list(
                    batch_transport_chunk_ids
                )
            batch_id = stable_intelligence_id("FACTBATCH", batch_identity)
            payload = _fact_extraction_primary_payload(
                target_id=target_id,
                target_name=target_name,
                target_aliases=target_aliases,
                archetype_id=archetype_id,
                as_of_date=as_of_date,
                extraction_semantics_version=(
                    FACT_EXTRACTION_SEMANTICS_VERSION
                ),
                open_objectives=open_objectives,
                current_evidence_facts=current_fact_prompt_context,
                score_gap_context=score_gap_prompt_context,
                scope_contract=scope_contract,
                batch=batch,
                objective_scope_by_document=(
                    batch_objective_scope_by_document
                ),
                objective_component_by_id=objective_component_by_id,
                objective_lineage_reassessment_rows=(
                    objective_lineage_reassessment_rows
                ),
            )
            prompt_documents = tuple(payload.get("full_documents") or ())
            if len(prompt_documents) != len(batch) or any(
                str(prompt_row.get("content_text") or "")
                != str(source_row.get("content_text") or "")
                for source_row, prompt_row in zip(batch, prompt_documents)
            ):
                raise ValueError(
                    "fact extraction prompt must preserve every full document verbatim"
                )
            max_primary_payload_chars = max(
                max_primary_payload_chars,
                _json_character_count(payload),
            )
            max_transport_chunk_chars = max(
                max_transport_chunk_chars,
                *(len(str(row.get("content_text") or "")) for row in batch),
            )
            max_contextual_transport_chars = max(
                max_contextual_transport_chars,
                *(
                    len(str(row.get("content_text") or ""))
                    + len(
                        str(
                            (
                                row.get("_source_boundary_context")
                                or {}
                            ).get("preceding_tail_text")
                            or ""
                        )
                    )
                    for row in batch
                ),
            )
            attempt_base_payload = payload
            attempt_payload = payload
            provider_attempt_count = 0
            validation_retry_used = False
            validation_retry_count = 0
            pagination_page_number = 1
            coverage_audit_performed = False
            carried_rejections: list[FactExtractionRejection] = []
            carried_feedback: list[str] = []
            carried_completion_flag_reconciled = False
            previously_accepted_claims: dict[str, Mapping[str, Any]] = {}
            primary_accepted_claim_ids: set[str] = set()
            previously_rejected_material_quote_failures: dict[
                tuple[str, str], FactExtractionRejection
            ] = {}
            if coverage_only_batch:
                content_by_document_id = {
                    str(row["document_id"]): str(
                        row.get("content_text") or ""
                    )
                    for row in batch
                }
                previously_accepted_claims = {
                    str(claim["claim_id"]): claim
                    for claim in claims
                    if str(claim.get("document_id") or "")
                    in batch_document_ids
                    and str(claim.get("exact_quote") or "")
                    in content_by_document_id.get(
                        str(claim.get("document_id") or ""),
                        "",
                    )
                }
                primary_accepted_claim_ids = set(
                    previously_accepted_claims
                )
                coverage_audit_performed = True
                coverage_audit_call_count += 1
                coverage_audit_document_ids.update(
                    batch_document_ids
                )
                attempt_base_payload = _coverage_audit_attempt_payload(
                    primary_payload=payload,
                    required_document_ids=sorted(
                        batch_document_ids
                    ),
                    primary_document_dispositions=tuple(
                        row
                        for row in all_prior_dispositions
                        if str(row.get("document_id") or "")
                        in batch_document_ids
                    ),
                    previously_accepted_claims=tuple(
                        previously_accepted_claims.values()
                    ),
                )
                attempt_payload = attempt_base_payload
            if (
                not coverage_only_batch
                and "fact_extraction_continuation_context"
                not in attempt_base_payload
                and "fact_extraction_retry_context" not in attempt_base_payload
            ):
                # A clean resume can arrive with a changed downstream
                # ``score_gap_context`` while an earlier pagination chain is
                # still open.  Recover that immutable page-one origin before
                # calling ``complete``.  Calling the current payload first
                # would journal a second base request for the same documents
                # merely because the downstream diagnostic changed.
                recovered_pagination_origin = (
                    _recover_validated_fact_extraction_pagination_origin_payload(
                        self.provider,
                        primary_payload=attempt_base_payload,
                    )
                )
                if recovered_pagination_origin is not None:
                    attempt_base_payload = recovered_pagination_origin
                    attempt_payload = recovered_pagination_origin
                    pagination_page_number = 1
            while True:
                max_attempt_payload_chars = max(
                    max_attempt_payload_chars,
                    _json_character_count(attempt_payload),
                )
                prompt_hash = stable_intelligence_id(
                    "FACTPROMPT", attempt_payload
                )
                provider_attempt_count += 1
                try:
                    response = self.provider.complete(
                        pass_name="EVIDENCE_FACT_EXTRACTION",
                        payload=attempt_payload,
                    )
                    assert_blind_research_output(response)
                except (
                    StructuredProviderUnavailable,
                    StructuredProviderRejected,
                    TimeoutError,
                    OSError,
                    RuntimeError,
                    KeyError,
                    TypeError,
                    ValueError,
                ) as exc:
                    recovered_retry_payload = (
                        _recover_validated_fact_extraction_retry_payload(
                            self.provider,
                            primary_payload=attempt_base_payload,
                            previously_accepted_claims=tuple(
                                previously_accepted_claims.values()
                            ),
                        )
                        if (
                            isinstance(exc, StructuredProviderUnavailable)
                            and str(exc).startswith(
                                "COLLABORATION_RESPONSE_PENDING:"
                                "COLLABREQ-"
                            )
                            and attempt_payload == attempt_base_payload
                            and "fact_extraction_retry_context"
                            not in attempt_payload
                        )
                        else None
                    )
                    if recovered_retry_payload is not None:
                        retry_context = recovered_retry_payload[
                            "fact_extraction_retry_context"
                        ]
                        validation_retry_count = int(
                            retry_context["rewrite_attempt"]
                        )
                        validation_retry_used = True
                        attempt_payload = recovered_retry_payload
                        continue
                    recovered_pagination_origin = (
                        _recover_validated_fact_extraction_pagination_origin_payload(
                            self.provider,
                            primary_payload=attempt_base_payload,
                        )
                        if (
                            isinstance(exc, StructuredProviderUnavailable)
                            and str(exc).startswith(
                                "COLLABORATION_RESPONSE_PENDING:"
                                "COLLABREQ-"
                            )
                            and attempt_payload == attempt_base_payload
                            and "fact_extraction_retry_context"
                            not in attempt_payload
                            and recovered_retry_payload is None
                        )
                        else None
                    )
                    if recovered_pagination_origin is not None:
                        # Replaying page one is intentional.  It reconstructs
                        # the complete accepted-claim objects in memory before
                        # page two and later cached responses are consumed.
                        # Jumping directly to the latest page would preserve
                        # only the compact continuation projection and silently
                        # lose earlier facts.
                        attempt_base_payload = recovered_pagination_origin
                        attempt_payload = recovered_pagination_origin
                        pagination_page_number = 1
                        continue
                    reason = (
                        "FACT_EXTRACTION_PROVIDER_OR_OUTPUT_ERROR:"
                        f"{type(exc).__name__}:{_clean_error(exc)}"
                    )
                    pending.append(reason)
                    pending_transport_chunk_ids.update(
                        batch_transport_chunk_ids
                    )
                    calls.append(
                        FactExtractionProviderCall(
                            batch_id=batch_id,
                            status="PENDING",
                            document_ids=tuple(
                                str(row["document_id"]) for row in batch
                            ),
                            accepted_claim_ids=(),
                            rejected_proposal_count=0,
                            document_dispositions=(),
                            pending_reasons=(reason,),
                            research_gap_feedback=(),
                            provider_name=provider_name,
                            prompt_hash=prompt_hash,
                            response_hash=None,
                            provider_attempt_count=provider_attempt_count,
                            validation_retry_used=validation_retry_used,
                            coverage_audit_performed=(
                                coverage_audit_performed
                            ),
                            transport_chunk_ids=(
                                batch_transport_chunk_ids
                            ),
                        )
                    )
                    # Usage-limit / process-launch failures are transport-wide:
                    # retrying them once per remaining document only burns time
                    # and can make a no-progress checkpoint look active.  A CLI
                    # timeout is different.  It can be caused by one unusually
                    # large document, while the next document may complete
                    # normally.  Preserve that batch as pending, continue the
                    # queue, and let checkpoint/resume retry only the timed-out
                    # document later.
                    provider_circuit_breaker_open = (
                        _is_transport_wide_provider_failure(exc)
                    )
                    break
                response_hash = stable_intelligence_id(
                    "FACTRESP", scrub_blind_research_payload(response)
                )
                (
                    batch_claims,
                    batch_rejections,
                    batch_dispositions,
                    batch_pending,
                    batch_feedback,
                    batch_completion_flag_reconciled,
                ) = _validate_response(
                    response,
                    batch_id=batch_id,
                    documents=batch,
                    target_id=target_id,
                    as_of_date=as_of_date,
                    scope_contract=scope_contract,
                    provider_name=provider_name,
                    prompt_hash=prompt_hash,
                    response_hash=response_hash,
                    previously_accepted_claim_counts={
                        document_id: sum(
                            1
                            for claim in previously_accepted_claims.values()
                            if str(claim.get("document_id") or "")
                            == document_id
                        )
                        for document_id in {
                            str(row["document_id"]) for row in batch
                        }
                    },
                    previously_accepted_semantic_identities={
                        document_id: tuple(
                            dict.fromkeys(
                                _fact_semantic_identity(claim)
                                for claim in previously_accepted_claims.values()
                                if str(claim.get("document_id") or "")
                                == document_id
                            )
                        )
                        for document_id in {
                            str(row["document_id"]) for row in batch
                        }
                    },
                    previously_rejected_material_quote_failure_counts={
                        document_id: sum(
                            1
                            for rejection in (
                                previously_rejected_material_quote_failures.values()
                            )
                            if rejection.document_id == document_id
                        )
                        for document_id in {
                            str(row["document_id"]) for row in batch
                        }
                    },
                    objective_scope_by_document=(
                        batch_objective_scope_by_document
                    ),
                    objective_component_by_id=(
                        objective_component_by_id
                    ),
                )
                page_boundary_reached = (
                    len(tuple(response.get("facts") or ()))
                    >= FACT_EXTRACTION_PAGE_FACT_LIMIT
                )
                unresolved_page_ids = {
                    str(value).strip()
                    for value in response.get("unresolved_document_ids") or ()
                    if str(value).strip()
                }
                required_page_ids = {
                    str(row["document_id"]) for row in batch
                }
                pagination_only_pending = all(
                    reason == "LLM_DECLARED_FACT_EXTRACTION_INCOMPLETE"
                    or (
                        reason.startswith("UNRESOLVED_DOCUMENT:")
                        and reason.split(":", 1)[1] in required_page_ids
                    )
                    for reason in batch_pending
                )
                pagination_requested = (
                    bool(batch_claims)
                    and pagination_only_pending
                    and (
                        page_boundary_reached
                        or (
                            response.get("extraction_complete") is not True
                            and bool(unresolved_page_ids)
                            and unresolved_page_ids.issubset(
                                required_page_ids
                            )
                        )
                    )
                )
                if pagination_requested:
                    for claim in batch_claims:
                        previously_accepted_claims[
                            str(claim["claim_id"])
                        ] = claim
                    pagination_page_number += 1
                    pagination_continuation_call_count += 1
                    maximum_pagination_page_count = max(
                        maximum_pagination_page_count,
                        pagination_page_number,
                    )
                    attempt_payload = scrub_blind_research_payload(
                        {
                            **attempt_base_payload,
                            "fact_extraction_continuation_context": (
                                _fact_extraction_continuation_context(
                                    page_number=pagination_page_number,
                                    required_document_ids=(
                                        required_page_ids
                                    ),
                                    accepted_claims=tuple(
                                        previously_accepted_claims.values()
                                    ),
                                )
                            ),
                        }
                    )
                    continue
                parent_fact_roster_is_observable = (
                    not batch_transport_chunk_ids
                    or all(
                        int(row.get("transport_chunk_index") or 0)
                        == int(row.get("transport_chunk_count") or 1) - 1
                        for row in batch
                    )
                )
                if parent_fact_roster_is_observable:
                    # A current-roster fact may be visible in prompt context
                    # even when the durable claim/disposition checkpoint was
                    # lost during roster churn.  Detect that omission while
                    # this exact response is still the provider's latest cache
                    # entry, so the existing invalidation + rewrite machinery
                    # can request the missing lineage under a fresh identity.
                    # For split parents this becomes safe only on the final
                    # chunk, after claims from every earlier chunk are present.
                    batch_pending.extend(
                        reason
                        for reason in (
                            _batch_current_fact_lineage_pending_reasons(
                                current_facts=effective_current_facts,
                                batch_document_ids=frozenset(
                                    batch_document_ids
                                ),
                                accepted_claims=(
                                    *claims,
                                    *previously_accepted_claims.values(),
                                    *batch_claims,
                                ),
                                target_id=target_id,
                                as_of_date=as_of_date,
                            )
                        )
                        if reason not in batch_pending
                    )
                if (
                    not batch_pending
                    and extraction_mode == "PRODUCTION_OBJECTIVE_LOCAL"
                    and not coverage_audit_performed
                    and bool(
                        required_page_ids
                        & coverage_required_document_ids
                    )
                ):
                    for claim in batch_claims:
                        previously_accepted_claims[
                            str(claim["claim_id"])
                        ] = claim
                    carried_rejections.extend(batch_rejections)
                    carried_feedback.extend(batch_feedback)
                    carried_completion_flag_reconciled = (
                        carried_completion_flag_reconciled
                        or batch_completion_flag_reconciled
                    )
                    coverage_audit_performed = True
                    coverage_audit_call_count += 1
                    coverage_audit_document_ids.update(
                        str(row["document_id"]) for row in batch
                    )
                    primary_accepted_claim_ids = set(
                        previously_accepted_claims
                    )
                    validation_retry_count = 0
                    pagination_page_number = 1
                    attempt_base_payload = _coverage_audit_attempt_payload(
                        primary_payload=payload,
                        required_document_ids=sorted(
                            required_page_ids
                        ),
                        primary_document_dispositions=(
                            batch_dispositions
                        ),
                        previously_accepted_claims=tuple(
                            previously_accepted_claims.values()
                        ),
                    )
                    attempt_payload = attempt_base_payload
                    continue
                if batch_pending:
                    _invalidate_semantically_invalid_provider_response(
                        self.provider,
                        reasons=batch_pending,
                    )
                if batch_pending and validation_retry_count < 2:
                    for claim in batch_claims:
                        previously_accepted_claims[str(claim["claim_id"])] = claim
                    validation_retry_count += 1
                    validation_retry_used = True
                    response_fact_rows = tuple(response.get("facts") or ())
                    scope_rejected_proposals = []
                    for rejection in batch_rejections:
                        if not (
                            rejection.material_proposal
                            and rejection.reason.startswith(
                                "MECHANISM_SCOPE_REJECTED"
                            )
                        ):
                            continue
                        raw_proposal = (
                            response_fact_rows[rejection.proposal_index]
                            if 0 <= rejection.proposal_index < len(response_fact_rows)
                            else {}
                        )
                        proposal = (
                            raw_proposal
                            if isinstance(raw_proposal, Mapping)
                            else {}
                        )
                        scope_rejected_proposals.append(
                            {
                                "proposal_index": rejection.proposal_index,
                                "document_id": rejection.document_id,
                                "reason": rejection.reason,
                                "exact_quote": rejection.proposed_exact_quote,
                                "scope_business_segment": proposal.get(
                                    "scope_business_segment"
                                ),
                                "scope_product_family": proposal.get(
                                    "scope_product_family"
                                ),
                                "scope_technology_family": proposal.get(
                                    "scope_technology_family"
                                ),
                                "scope_transaction_type": proposal.get(
                                    "scope_transaction_type"
                                ),
                                "scope_economic_mechanism": proposal.get(
                                    "scope_economic_mechanism"
                                ),
                                "normalized_object": proposal.get(
                                    "normalized_object"
                                ),
                            }
                        )
                    rejected_material_proposals = [
                        {
                            "proposal_index": row.proposal_index,
                            "document_id": row.document_id,
                            "reason": row.reason,
                            "proposed_exact_quote": row.proposed_exact_quote,
                        }
                        for row in batch_rejections
                        if row.material_proposal
                        and not row.reason.startswith("MECHANISM_SCOPE_REJECTED")
                    ]
                    for rejection in batch_rejections:
                        if (
                            rejection.material_proposal
                            and rejection.reason
                            == "EXACT_QUOTE_NOT_IN_FULL_DOCUMENT"
                            and rejection.proposed_exact_quote
                        ):
                            previously_rejected_material_quote_failures[
                                (
                                    rejection.document_id,
                                    rejection.proposed_exact_quote,
                                )
                            ] = rejection
                    retry_rejected_proposals = {
                        (
                            str(row["document_id"]),
                            str(row["proposed_exact_quote"] or ""),
                            str(row["reason"]),
                        ): row
                        for row in (
                            *rejected_material_proposals,
                            *(
                                {
                                    "proposal_index": row.proposal_index,
                                    "document_id": row.document_id,
                                    "reason": row.reason,
                                    "proposed_exact_quote": (
                                        row.proposed_exact_quote
                                    ),
                                }
                                for row in (
                                    previously_rejected_material_quote_failures.values()
                                )
                            ),
                        )
                    }
                    attempt_payload = scrub_blind_research_payload(
                        {
                            **attempt_base_payload,
                            "fact_extraction_retry_context": {
                                "rewrite_attempt": validation_retry_count,
                                "maximum_rewrite_attempts": 2,
                                "validation_errors": list(batch_pending),
                                "rejected_proposals": list(
                                    retry_rejected_proposals.values()
                                ),
                                "scope_rejected_proposals": (
                                    scope_rejected_proposals
                                ),
                                "must_not_repeat_invalid_scope_encoding": True,
                                "prior_material_quote_failures": [
                                    {
                                        "document_id": row.document_id,
                                        "reason": row.reason,
                                        "proposed_exact_quote": (
                                            row.proposed_exact_quote
                                        ),
                                    }
                                    for row in (
                                        previously_rejected_material_quote_failures.values()
                                    )
                                ],
                                "must_not_repeat_rejected_proposals": True,
                                "previously_accepted_facts": (
                                    _fact_extraction_retry_accepted_facts(
                                        tuple(
                                            previously_accepted_claims.values()
                                        )
                                    )
                                ),
                                "prohibited_exact_quote_reuse": [
                                    {
                                        "document_id": row["document_id"],
                                        "exact_quote": row["proposed_exact_quote"],
                                    }
                                    for row in rejected_material_proposals
                                    if row["reason"]
                                    == "EXACT_QUOTE_NOT_IN_FULL_DOCUMENT"
                                    and row["proposed_exact_quote"]
                                ],
                                "required_document_ids": [
                                    str(row["document_id"]) for row in batch
                                ],
                                "instruction": (
                                    "Rewrite the complete batch. Every listed rejected "
                                    "proposal was deterministically invalid and must not "
                                    "be repeated, paraphrased, whitespace-normalized, or "
                                    "reused. Facts listed in previously_accepted_facts have "
                                    "already passed deterministic validation: do not emit "
                                    "them again and do not downgrade their document to "
                                    "NO_MATERIAL_FACT. Use FACTS_EXTRACTED for every document "
                                    "that has a previously accepted fact. Omit a rejected "
                                    "proposal unless a different literal substring "
                                    "in the same document directly supports the fact. Every material "
                                    "exact_quote must be copied as one literal "
                                    "contiguous substring from that document's "
                                    "content_text. Delete any unsupported proposal; "
                                    "do not paraphrase or repair quotes in code. If the "
                                    "document contains semantically material content but "
                                    "parser fragmentation or noise prevents a literal "
                                    "quote, use UNREADABLE rather than NO_MATERIAL_FACT. "
                                    "A prior material quote failure cannot be closed as "
                                    "NO_MATERIAL_FACT merely because quote copying failed."
                                    " For every scope_rejected_proposal, distinguish a "
                                    "target-direct fact encoded with noncanonical scope "
                                    "tokens from a genuinely wrong target or segment. For "
                                    "a target-direct fact, preserve a literal exact quote "
                                    "and rewrite every scope_* field using exactly one token "
                                    "from its corresponding allowed_* list in "
                                    "deterministic_mechanism_scope_contract; keep narrower "
                                    "product, process, generation, or business-unit wording "
                                    "in the descriptive fields. For a genuinely wrong-target "
                                    "or wrong-segment proposal, omit it and return the accurate "
                                    "terminal disposition. Never relabel a wrong-scope fact "
                                    "merely to force it through the contract."
                                    " extraction_complete is local to this supplied batch, "
                                    "not to the broader thesis or future research. Set it "
                                    "to true when every required_document_id has exactly "
                                    "one valid disposition and unresolved_document_ids is "
                                    "empty, including when every disposition is "
                                    "NO_MATERIAL_FACT. Put broader evidence gaps only in "
                                    "unresolved_research_notes; those gaps alone must not "
                                    "make extraction_complete false."
                                ),
                            },
                        }
                    )
                    continue
                batch_rejections = [
                    *carried_rejections,
                    *batch_rejections,
                ]
                batch_feedback = [
                    *carried_feedback,
                    *batch_feedback,
                ]
                batch_completion_flag_reconciled = (
                    carried_completion_flag_reconciled
                    or batch_completion_flag_reconciled
                )
                combined_batch_claims = {
                    **previously_accepted_claims,
                    **{
                        str(claim["claim_id"]): claim
                        for claim in batch_claims
                    },
                }
                if coverage_audit_performed:
                    coverage_audit_new_fact_count += sum(
                        claim_id
                        not in primary_accepted_claim_ids
                        for claim_id in combined_batch_claims
                    )
                claims.extend(combined_batch_claims.values())
                rejections.extend(batch_rejections)
                if batch_pending:
                    rejections.extend(
                        previously_rejected_material_quote_failures.values()
                    )
                dispositions.extend(batch_dispositions)
                pending.extend(batch_pending)
                if batch_pending:
                    pending_transport_chunk_ids.update(
                        batch_transport_chunk_ids
                    )
                research_gap_feedback.extend(batch_feedback)
                calls.append(
                    FactExtractionProviderCall(
                        batch_id=batch_id,
                        status="PENDING" if batch_pending else "COMPLETE",
                        document_ids=tuple(
                            str(row["document_id"]) for row in batch
                        ),
                        accepted_claim_ids=tuple(
                            combined_batch_claims
                        ),
                        rejected_proposal_count=len(batch_rejections),
                        document_dispositions=tuple(batch_dispositions),
                        pending_reasons=tuple(batch_pending),
                        research_gap_feedback=tuple(batch_feedback),
                        provider_name=provider_name,
                        prompt_hash=prompt_hash,
                        response_hash=response_hash,
                        provider_attempt_count=provider_attempt_count,
                        validation_retry_used=validation_retry_used,
                        completion_flag_reconciled=(
                            batch_completion_flag_reconciled
                        ),
                        coverage_audit_performed=(
                            coverage_audit_performed
                        ),
                        transport_chunk_ids=batch_transport_chunk_ids,
                        accepted_claims=(
                            tuple(combined_batch_claims.values())
                            if batch_transport_chunk_ids
                            and not batch_pending
                            else None
                        ),
                    )
                )
                break
            if provider_circuit_breaker_open:
                break
            successful_call = calls[-1] if calls else None
            successful_batch_changed_downstream_input = bool(
                successful_call is not None
                and successful_call.status == "COMPLETE"
                and downstream_input_hash_before_batch
                != _canonical_downstream_fact_input_hash(
                    claims=claims,
                    dispositions=dispositions,
                    pending=pending,
                    split_chunk_ids_by_document=(
                        split_chunk_ids_by_document
                    ),
                    pending_transport_chunk_ids=(
                        pending_transport_chunk_ids
                    ),
                    target_id=target_id,
                    as_of_date=as_of_date,
                )
            )
            successful_batch_added_feedback = bool(
                successful_call is not None
                and successful_call.status == "COMPLETE"
                and successful_call.research_gap_feedback
            )
            if (
                batch_index + 1 < len(document_batches)
                and (
                    successful_batch_changed_downstream_input
                    or successful_batch_added_feedback
                )
            ):
                # A completed parent disposition feeds the downstream
                # counter-route, structured gaps, Supervisor, and the next
                # checkpoint's fact prompt.  Persist that canonical state
                # before opening another collaboration request.  Intermediate
                # split chunks may continue because their accepted claims are
                # embedded in the call ledger and projected above; only the
                # reconciler proving every split chunk complete closes its
                # parent and therefore yields here.
                pending.append(
                    FACT_EXTRACTION_CANONICAL_STATE_REFRESH_REQUIRED
                )
                canonical_state_refresh_barrier_count += 1
                break
        claims, dispositions, pending = _reconcile_transport_chunks(
            claims=claims,
            dispositions=dispositions,
            pending=pending,
            split_chunk_ids_by_document=split_chunk_ids_by_document,
            pending_transport_chunk_ids=pending_transport_chunk_ids,
            target_id=target_id,
            as_of_date=as_of_date,
        )
        coverage_audited_document_ids = {
            document_id
            for call in calls
            if call.status == "COMPLETE"
            and call.coverage_audit_performed
            and call.extraction_semantics_version
            == FACT_EXTRACTION_SEMANTICS_VERSION
            for document_id in call.document_ids
        }
        coverage_audited_transport_chunk_ids = {
            chunk_id
            for call in calls
            if call.status == "COMPLETE"
            and call.coverage_audit_performed
            and call.extraction_semantics_version
            == FACT_EXTRACTION_SEMANTICS_VERSION
            for chunk_id in call.transport_chunk_ids
        }
        current_semantics_disposition_ids = {
            str(row.get("document_id") or "")
            for row in dispositions
            if _extraction_semantics_version(row)
            == FACT_EXTRACTION_SEMANTICS_VERSION
        }
        completed_boundary_context_reextraction_document_ids = (
            boundary_context_reextraction_document_ids
            & current_semantics_disposition_ids
        )
        completed_coverage_refresh_document_ids = {
            document_id
            for document_id in set(coverage_refresh_document_ids)
            if document_id in current_semantics_disposition_ids
            and (
                (
                    document_id in split_chunk_ids_by_document
                    and set(split_chunk_ids_by_document[document_id])
                    <= coverage_audited_transport_chunk_ids
                )
                or (
                    document_id not in split_chunk_ids_by_document
                    and document_id in coverage_audited_document_ids
                )
            )
        }
        completed_current_lineage_objective_reassessment_document_ids = (
            set(current_lineage_objective_reassessment_document_ids)
            & completed_coverage_refresh_document_ids
        )
        if completed_current_lineage_objective_reassessment_document_ids:
            completed_reassessment_reasons = {
                "CURRENT_FACT_LINEAGE_OBJECTIVE_REASSESSMENT_REQUIRED:"
                + document_id
                for document_id in (
                    completed_current_lineage_objective_reassessment_document_ids
                )
            }
            pending = [
                reason
                for reason in pending
                if reason not in completed_reassessment_reasons
            ]
            current_lineage_objective_reassessment_document_ids = tuple(
                document_id
                for document_id in (
                    current_lineage_objective_reassessment_document_ids
                )
                if document_id
                not in (
                    completed_current_lineage_objective_reassessment_document_ids
                )
            )
        incomplete_coverage_refresh_document_ids = (
            set(coverage_refresh_document_ids)
            | deferred_coverage_refresh_document_ids
        ) - completed_coverage_refresh_document_ids
        if incomplete_coverage_refresh_document_ids:
            # A coverage refresh is an atomic replacement of an already
            # accepted parent document.  Until every transport chunk has a
            # COMPLETE audit response, keep the baseline parent disposition
            # and claims in the durable checkpoint.  The completed chunk
            # calls above remain embedded in the provider-call ledger and are
            # resumed independently; exposing their partial claims or
            # deleting the baseline would make the next clean resume mistake
            # the same document for a first-pass extraction.
            baseline_claims = [
                dict(row)
                for row in prior_material_claims
                if str(row.get("document_id") or "")
                in incomplete_coverage_refresh_document_ids
            ]
            claim_by_id = {
                str(
                    row.get("claim_id")
                    or stable_intelligence_id("CLAIM", row)
                ): row
                for row in (*claims, *baseline_claims)
            }
            claims = list(claim_by_id.values())
            disposition_by_document_id = {
                str(row.get("document_id") or ""): row
                for row in dispositions
                if str(row.get("document_id") or "")
            }
            for row in all_prior_dispositions:
                document_id = str(row.get("document_id") or "")
                if (
                    document_id
                    in incomplete_coverage_refresh_document_ids
                    and document_id not in disposition_by_document_id
                ):
                    dispositions.append(row)
                    disposition_by_document_id[document_id] = row
        if (
            deferred_coverage_refresh_document_ids
            and all(
                reason
                in {
                    "CURRENT_FACT_LINEAGE_OBJECTIVE_REASSESSMENT_REQUIRED:"
                    + document_id
                    for document_id in (
                        current_lineage_objective_reassessment_document_ids
                    )
                }
                for reason in pending
            )
            and new_unprocessed_document_ids.issubset(
                {
                    str(row.get("document_id") or "")
                    for row in dispositions
                }
            )
        ):
            # The deferred baseline dispositions are intentionally still
            # present.  Persist the newly accepted canonical fact state before
            # deciding on the next resume whether those older documents still
            # need their coverage audit.
            pending.append(
                FACT_EXTRACTION_CANONICAL_STATE_REFRESH_REQUIRED
            )
            canonical_state_refresh_barrier_count += 1
        rejections = list(
            {
                (
                    row.batch_id,
                    row.document_id,
                    row.reason,
                    row.proposed_exact_quote,
                ): row
                for row in rejections
            }.values()
        )
        compilation = EvidenceFactCompiler().compile(
            target_id=target_id,
            as_of_date=as_of_date,
            accepted_claims=claims,
        )
        initial_current_fact_lineage_gaps_by_document = (
            _current_fact_lineage_rematerialization_gaps(
                current_facts=effective_current_facts,
                current_document_ids=frozenset(document_ids),
                compilation=compilation,
            )
        )
        initial_lineage_gap_document_ids = tuple(
            initial_current_fact_lineage_gaps_by_document
        )
        initial_lineage_gap_fact_ids = tuple(
            sorted(
                {
                    fact_id
                    for fact_ids in (
                        initial_current_fact_lineage_gaps_by_document.values()
                    )
                    for fact_id in fact_ids
                }
            )
        )
        current_fact_lineage_rematerialization_document_ids = (
            _atomic_fact_lineage_rematerialization_document_ids(
                initial_document_ids=initial_lineage_gap_document_ids,
                provider_calls=calls,
                current_document_ids=frozenset(document_ids),
            )
        )
        current_fact_lineage_rematerialization_by_document = dict(
            initial_current_fact_lineage_gaps_by_document
        )
        rematerialization_document_ids = set(
            current_fact_lineage_rematerialization_document_ids
        )
        if current_fact_lineage_rematerialization_document_ids:
            # A partial or NO_MATERIAL_FACT response is not a safe replacement
            # for compiler-owned claim/fact/link lineage.  Invalidate the whole
            # affected document checkpoint so the next clean resume re-reads
            # it without the stale prompt-only fact snapshot.
            invalidated_calls = tuple(
                call
                for call in calls
                if set(call.document_ids) & rematerialization_document_ids
            )
            retained_calls = [
                call
                for call in calls
                if not (
                    set(call.document_ids)
                    & rematerialization_document_ids
                )
            ]
            invalidated_transport_chunk_ids = {
                chunk_id
                for call in invalidated_calls
                for chunk_id in call.transport_chunk_ids
            }
            invalidated_transport_chunk_ids.update(
                chunk_id
                for document_id in rematerialization_document_ids
                for chunk_id in split_chunk_ids_by_document.get(
                    document_id, ()
                )
            )
            pending_transport_chunk_ids.difference_update(
                invalidated_transport_chunk_ids
            )
            resumed_transport_chunk_ids.difference_update(
                invalidated_transport_chunk_ids
            )
            invalidated_call_pending_reasons = {
                reason
                for call in invalidated_calls
                for reason in call.pending_reasons
            }
            retained_call_pending_reasons = {
                reason
                for call in retained_calls
                for reason in call.pending_reasons
            }
            invalidated_feedback = {
                reason
                for call in invalidated_calls
                for reason in call.research_gap_feedback
            }
            retained_feedback = {
                reason
                for call in retained_calls
                for reason in call.research_gap_feedback
            }
            pending = [
                reason
                for reason in pending
                if not (
                    reason in invalidated_call_pending_reasons
                    and reason not in retained_call_pending_reasons
                    and _COLLABORATION_FACT_WAIT_RE.fullmatch(reason) is None
                )
                and not (
                    set(reason.split(":"))
                    & rematerialization_document_ids
                )
            ]
            research_gap_feedback = [
                reason
                for reason in research_gap_feedback
                if not (
                    reason in invalidated_feedback
                    and reason not in retained_feedback
                )
            ]
            claims = [
                row
                for row in claims
                if not (
                    _current_document_ids_for_lineage_row(
                        row,
                        current_document_ids=frozenset(
                            rematerialization_document_ids
                        ),
                    )
                )
            ]
            dispositions = [
                row
                for row in dispositions
                if str(row.get("document_id") or "")
                not in rematerialization_document_ids
            ]
            calls = retained_calls
            rejections = [
                row
                for row in rejections
                if row.document_id not in rematerialization_document_ids
            ]
            coverage_audited_document_ids.difference_update(
                rematerialization_document_ids
            )
            coverage_audited_transport_chunk_ids.difference_update(
                invalidated_transport_chunk_ids
            )
            current_semantics_disposition_ids.difference_update(
                rematerialization_document_ids
            )
            completed_boundary_context_reextraction_document_ids = (
                completed_boundary_context_reextraction_document_ids
                - rematerialization_document_ids
            )
            completed_coverage_refresh_document_ids.difference_update(
                rematerialization_document_ids
            )
            compilation = EvidenceFactCompiler().compile(
                target_id=target_id,
                as_of_date=as_of_date,
                accepted_claims=claims,
            )
            current_fact_lineage_rematerialization_by_document = dict(
                _current_fact_lineage_rematerialization_gaps(
                    current_facts=effective_current_facts,
                    current_document_ids=frozenset(
                        rematerialization_document_ids
                    ),
                    compilation=compilation,
                )
            )
            pending.extend(
                "CURRENT_FACT_LINEAGE_REMATERIALIZATION_REQUIRED:"
                + document_id
                for document_id in (
                    current_fact_lineage_rematerialization_document_ids
                )
            )
        current_fact_lineage_rematerialization_fact_ids = tuple(
            sorted(
                {
                    fact_id
                    for fact_ids in (
                        current_fact_lineage_rematerialization_by_document.values()
                    )
                    for fact_id in fact_ids
                }
            )
        )
        if compilation.status != "FACT_COMPILATION_COMPLETE":
            pending.append(compilation.status)
        pending = list(dict.fromkeys(pending))
        research_gap_feedback.extend(
            f"FACT_EXTRACTION_RETRY_CONTEXT:{reason}" for reason in pending
        )
        disposition_document_ids = {
            str(row.get("document_id") or "")
            for row in dispositions
            if str(row.get("document_id") or "")
        }
        pending_coverage_refresh_document_ids = sorted(
            (
                set(coverage_refresh_document_ids)
                | deferred_coverage_refresh_document_ids
                | set(
                    current_lineage_objective_reassessment_document_ids
                )
            )
            - completed_coverage_refresh_document_ids
        )
        critical_counts = {
            "snippet_or_non_full_document_input_count": sum(
                bool(row.get("snippet_only"))
                or not bool(row.get("full_fetch_performed"))
                or not bool(row.get("evidence_eligible"))
                for row in prepared
            ),
            "unaccounted_document_count": max(0, len(prepared) - len(dispositions)),
            "duplicate_document_disposition_count": max(
                0,
                len(dispositions)
                - len({str(row.get("document_id") or "") for row in dispositions}),
            ),
            "material_proposal_rejection_count": sum(
                row.material_proposal
                and not row.reason.startswith("MECHANISM_SCOPE_REJECTED")
                for row in rejections
            ),
            "accepted_claim_without_fact_count": (
                compilation.accepted_claim_without_fact_count
            ),
            "provider_or_semantic_pending_count": len(pending),
            "production_document_without_coverage_audit_count": (
                len(
                    (
                        disposition_document_ids
                        & coverage_required_document_ids
                    )
                    - coverage_audited_document_ids
                )
                if extraction_mode == "PRODUCTION_OBJECTIVE_LOCAL"
                else 0
            ),
            "future_source_count": sum(
                date.fromisoformat(str(row["published_at"])[:10]) > cutoff
                for row in prepared
            ),
        }
        critical_sum = sum(critical_counts.values())
        complete = critical_sum == 0 and all(
            row.status == "COMPLETE" for row in calls
        )
        audit = {
            "schema_version": "e2r_v5_fact_extraction_audit_v1",
            "status": "FACT_EXTRACTION_AUDIT_PASS" if complete else "FACT_EXTRACTION_AUDIT_PENDING",
            "target_id": target_id,
            "as_of_date": as_of_date,
            "input_document_count": len(prepared),
            "provider_call_count": len(calls),
            "provider_attempt_count": sum(
                row.provider_attempt_count for row in calls
            ),
            "validation_retry_call_count": sum(
                row.validation_retry_used for row in calls
            ),
            "completion_flag_reconciled_count": (
                sum(row.completion_flag_reconciled for row in calls)
            ),
            "completion_flag_reconciliation_policy": (
                "BATCH_DISPOSITIONS_COMPLETE_AND_NO_UNRESOLVED_DOCUMENT_IDS"
            ),
            "fact_page_limit": FACT_EXTRACTION_PAGE_FACT_LIMIT,
            "fact_page_limit_is_total_fact_cap": False,
            "pagination_continuation_call_count": (
                pagination_continuation_call_count
            ),
            "maximum_pagination_page_count": (
                maximum_pagination_page_count
            ),
            "extraction_mode": extraction_mode,
            "extraction_semantics_version": (
                FACT_EXTRACTION_SEMANTICS_VERSION
            ),
            "current_fact_lineage_recovery_requested": (
                authoritative_fact_ledger is not None
            ),
            "current_fact_lineage_recovery_status": (
                str(current_lineage_recovery.get("status") or "PENDING")
                if current_lineage_recovery is not None
                else "NOT_REQUESTED"
            ),
            "current_fact_lineage_authority_checkpoint_id": (
                authoritative_fact_ledger.checkpoint_id
                if authoritative_fact_ledger is not None
                else None
            ),
            "current_fact_lineage_authority_checkpoint_hash": (
                authoritative_fact_ledger.checkpoint_hash
                if authoritative_fact_ledger is not None
                else None
            ),
            "current_fact_lineage_expectation_status": (
                str(
                    (
                        current_lineage_recovery.get("expectation")
                        or {}
                    ).get("status")
                    or "NOT_REQUESTED"
                )
                if current_lineage_recovery is not None
                else "NOT_REQUESTED"
            ),
            "current_fact_lineage_recovered_claim_count": (
                int(
                    current_lineage_recovery.get(
                        "recovered_claim_count"
                    )
                    or 0
                )
                if current_lineage_recovery is not None
                else 0
            ),
            "current_fact_lineage_recovered_fact_count": (
                int(
                    current_lineage_recovery.get("recovered_fact_count")
                    or 0
                )
                if current_lineage_recovery is not None
                else 0
            ),
            "current_fact_lineage_recovered_document_count": (
                int(
                    current_lineage_recovery.get(
                        "recovered_document_count"
                    )
                    or 0
                )
                if current_lineage_recovery is not None
                else 0
            ),
            "current_fact_lineage_journal_request_count": (
                int(
                    current_lineage_recovery.get("journal_request_count")
                    or 0
                )
                if current_lineage_recovery is not None
                else 0
            ),
            "current_fact_lineage_journal_call_group_count": (
                int(
                    current_lineage_recovery.get(
                        "journal_call_group_count"
                    )
                    or 0
                )
                if current_lineage_recovery is not None
                else 0
            ),
            "current_fact_lineage_provider_complete_call_count": (
                int(
                    current_lineage_recovery.get(
                        "provider_complete_call_count"
                    )
                    or 0
                )
                if current_lineage_recovery is not None
                else 0
            ),
            "current_fact_lineage_recovered_claim_ids": list(
                current_lineage_recovery.get("recovered_claim_ids") or ()
            )
            if current_lineage_recovery is not None
            else [],
            "current_fact_lineage_recovered_fact_ids": list(
                current_lineage_recovery.get("recovered_fact_ids") or ()
            )
            if current_lineage_recovery is not None
            else [],
            "current_fact_lineage_exact_recovery_receipt": (
                dict(current_lineage_recovery.get("receipt") or {})
                if current_lineage_recovery is not None
                else {}
            ),
            "current_fact_lineage_atomic_all_or_nothing": True,
            "current_fact_lineage_objective_reassessment_document_ids": list(
                current_lineage_objective_reassessment_document_ids
            ),
            "current_fact_lineage_objective_reassessment_preserves_facts": (
                True
            ),
            "stale_semantics_disposition_count": (
                stale_semantics_disposition_count
            ),
            "stale_semantics_provider_call_count": (
                stale_semantics_provider_call_count
            ),
            "semantics_migration_recovery_requested": (
                semantics_recovery_requested
            ),
            "semantics_migration_recovery_status": (
                "COMPLETE"
                if semantics_recovery_succeeded
                else (
                    "ABSENT_REEXTRACTION"
                    if semantics_recovery_absent
                    else (
                        "INCOMPLETE"
                        if semantics_recovery_failed
                        else "NOT_REQUIRED"
                    )
                )
            ),
            "semantics_migration_recovery_document_count": (
                int(semantics_recovery.get("document_count") or 0)
                if semantics_recovery_succeeded
                and semantics_recovery is not None
                else 0
            ),
            "semantics_migration_recovery_claim_count": (
                int(semantics_recovery.get("claim_count") or 0)
                if semantics_recovery_succeeded
                and semantics_recovery is not None
                else 0
            ),
            "semantics_migration_recovery_call_count": (
                int(semantics_recovery.get("call_count") or 0)
                if semantics_recovery_succeeded
                and semantics_recovery is not None
                else 0
            ),
            "semantics_migration_recovery_request_count": (
                int(semantics_recovery.get("request_count") or 0)
                if semantics_recovery_succeeded
                and semantics_recovery is not None
                else 0
            ),
            "semantics_migration_recovery_is_atomic": True,
            "pending_semantics_migration_recovery_document_ids": (
                list(prior_semantics_recovery_document_ids)
                if semantics_recovery_failed
                else []
            ),
            "pending_semantics_migration_recovery_expected_claim_count": (
                prior_semantics_recovery_invalidated_claim_count
                if semantics_recovery_failed
                else 0
            ),
            "stale_semantics_checkpoint_reextracted": bool(
                boundary_context_reextraction_document_ids
                and boundary_context_reextraction_document_ids
                <= current_semantics_disposition_ids
            ),
            "stale_semantics_checkpoint_coverage_refreshed": bool(
                coverage_refresh_document_ids
                & stale_semantics_disposition_ids
            ),
            "prior_checkpoint_coverage_refreshed": bool(
                coverage_refresh_document_ids
            ),
            "preserved_prior_claim_count": sum(
                str(row.get("document_id") or "")
                not in boundary_context_reextraction_document_ids
                and str(row.get("document_id") or "")
                not in rematerialization_document_ids
                for row in prior_material_claims
            ),
            "current_fact_lineage_initial_gap_document_ids": list(
                initial_lineage_gap_document_ids
            ),
            "current_fact_lineage_initial_gap_fact_ids": list(
                initial_lineage_gap_fact_ids
            ),
            "current_fact_lineage_initial_gap_by_document": {
                document_id: list(fact_ids)
                for document_id, fact_ids in (
                    initial_current_fact_lineage_gaps_by_document.items()
                )
            },
            "current_fact_lineage_rematerialization_document_ids": list(
                current_fact_lineage_rematerialization_document_ids
            ),
            "current_fact_lineage_rematerialization_fact_ids": list(
                current_fact_lineage_rematerialization_fact_ids
            ),
            "current_fact_lineage_rematerialization_by_document": {
                document_id: list(fact_ids)
                for document_id, fact_ids in (
                    current_fact_lineage_rematerialization_by_document.items()
                )
            },
            "current_fact_lineage_invalidated_prior_claim_count": sum(
                str(row.get("document_id") or "")
                in rematerialization_document_ids
                for row in prior_material_claims
            ),
            "boundary_context_invalidated_prior_claim_count": sum(
                str(row.get("document_id") or "")
                in boundary_context_reextraction_document_ids
                for row in prior_material_claims
            ),
            "prior_claim_source_provenance_rematerialized_count": sum(
                row.get("source_provenance_rematerialized") is True
                for row in prior_material_claims
            ),
            "embedded_claim_source_provenance_rematerialized_count": sum(
                claim.get("source_provenance_rematerialized") is True
                for call in all_checkpoint_calls
                for claim in call.accepted_claims or ()
            ),
            "base_reextraction_document_count": len(
                completed_boundary_context_reextraction_document_ids
            ),
            "boundary_context_reextraction_selected_document_count": len(
                boundary_context_reextraction_document_ids
            ),
            "boundary_context_reextraction_completed_document_count": len(
                completed_boundary_context_reextraction_document_ids
            ),
            "source_boundary_context_document_count": len(
                source_boundary_context_by_document_id
            ),
            "source_boundary_context_total_chars": sum(
                int(row["preceding_tail_chars"])
                for row in source_boundary_context_by_document_id.values()
            ),
            "boundary_context_reextraction_document_ids": sorted(
                boundary_context_reextraction_document_ids
            ),
            "production_objective_local_completion": (
                extraction_mode == "PRODUCTION_OBJECTIVE_LOCAL"
            ),
            "coverage_audit_required_for_production": (
                extraction_mode == "PRODUCTION_OBJECTIVE_LOCAL"
            ),
            "coverage_gap_objective_count": len(
                coverage_gap_objective_ids
            ),
            "coverage_audit_required_document_count": len(
                coverage_required_document_ids
            ),
            "coverage_refresh_prior_document_count": len(
                coverage_refresh_document_ids
            ),
            "coverage_refresh_deferred_for_new_document_count": len(
                deferred_coverage_refresh_document_ids
            ),
            "pending_coverage_refresh_document_ids": (
                pending_coverage_refresh_document_ids
            ),
            "pending_coverage_refresh_document_count": len(
                pending_coverage_refresh_document_ids
            ),
            "new_unprocessed_document_count": len(
                new_unprocessed_document_ids
            ),
            "bounded_stale_coverage_refresh_document_count": len(
                bounded_stale_coverage_refresh_document_ids
            ),
            "coverage_refresh_objective_lineage_reassessment_document_count": sum(
                coverage_refresh_objective_scope_by_document[document_id]
                != objective_scope_by_document[document_id]
                for document_id in coverage_refresh_document_ids
            )
            if objective_scope_by_document is not None
            else 0,
            "coverage_audit_call_count": coverage_audit_call_count,
            "coverage_audit_document_count": len(
                coverage_audit_document_ids
            ),
            "coverage_audit_new_fact_count": (
                coverage_audit_new_fact_count
            ),
            "transport_chunk_size": self.documents_per_call,
            "transport_character_bound": self.max_document_chars_per_call,
            "transport_chunk_is_completion_cap": False,
            "canonical_state_refresh_barrier_count": (
                canonical_state_refresh_barrier_count
            ),
            "canonical_state_refresh_is_completion_cap": False,
            "prompt_transport_accounting": {
                "current_fact_projection_schema_version": (
                    current_fact_prompt_context["schema_version"]
                ),
                "current_fact_count": maximum_current_fact_prompt_count,
                "maximum_current_fact_count": (
                    maximum_current_fact_prompt_count
                ),
                "current_fact_projection_chars": (
                    maximum_current_fact_prompt_context_chars
                ),
                "maximum_current_fact_projection_chars": (
                    maximum_current_fact_prompt_context_chars
                ),
                "score_gap_projection_schema_version": (
                    score_gap_prompt_context[
                        "fact_extraction_score_gap_projection_audit"
                    ]["schema_version"]
                ),
                "score_gap_projection_chars": score_gap_prompt_context_chars,
                "maximum_full_document_chars": max_full_document_chars,
                "maximum_transport_chunk_chars": max_transport_chunk_chars,
                "maximum_contextual_transport_chars": (
                    max_contextual_transport_chars
                ),
                "transport_character_bound_enforced": (
                    max_contextual_transport_chars
                    <= self.max_document_chars_per_call
                ),
                "split_document_count": len(split_chunk_ids_by_document),
                "transport_chunk_count": len(all_transport_documents),
                "resumed_transport_chunk_count": len(
                    resumed_transport_chunk_ids
                ),
                "provider_transport_chunk_count": len(transport_documents),
                "resumed_transport_chunks_skipped_provider": True,
                "every_full_document_covered_by_transport_chunks": True,
                "maximum_primary_payload_chars": max_primary_payload_chars,
                "maximum_attempt_payload_chars": max_attempt_payload_chars,
                "full_document_content_preserved_verbatim": True,
                "full_fact_records_persisted_outside_prompt": True,
                "fixed_top_n_used": False,
                "prompt_projection_is_research_cap": False,
                "score_authority": False,
            },
            "provider_circuit_breaker_open": provider_circuit_breaker_open,
            "accepted_material_claim_count": len(claims),
            "compiled_fact_count": len(compilation.facts),
            "counterfact_count": sum(
                row.direction == EvidenceDirection.COUNTER.value
                for row in compilation.facts
            ),
            "research_gap_feedback_count": len(
                tuple(dict.fromkeys(research_gap_feedback))
            ),
            "wrong_mechanism_terminal_count": sum(
                row.reason.startswith("MECHANISM_SCOPE_REJECTED")
                for row in rejections
            ),
            "snippet_is_evidence": False,
            "llm_score_authority": False,
            "llm_stage_authority": False,
            "critical_counts": critical_counts,
            "critical_count_sum": critical_sum,
        }
        return ResearcherFactExtractionResult(
            target_id=target_id,
            as_of_date=as_of_date,
            status=(
                "FACT_EXTRACTION_COMPLETE"
                if complete
                else "FACT_EXTRACTION_PENDING"
            ),
            material_claims=tuple(claims),
            fact_compilation=compilation,
            provider_calls=tuple(calls),
            rejections=tuple(rejections),
            document_dispositions=tuple(dispositions),
            pending_reasons=tuple(pending),
            research_gap_feedback=tuple(dict.fromkeys(research_gap_feedback)),
            audit=audit,
        )


def resolve_current_fact_lineage_recovery_binding(
    *,
    authoritative_fact_ledger: AuthoritativeResearchEpochFactLedger,
    journal_root: str | Path,
    target_id: str,
    target_name: str,
    target_aliases: Sequence[str],
    archetype_id: str,
    as_of_date: str,
    documents: Sequence[Mapping[str, Any]],
    open_objectives: Sequence[Mapping[str, Any]],
    current_facts: Sequence[Mapping[str, Any]],
    score_gap_context: Mapping[str, Any] | None,
    prior_material_claims: Sequence[Mapping[str, Any]],
    prior_document_dispositions: Sequence[Mapping[str, Any]],
    extraction_mode: str,
    pending_new_fact_ids: Sequence[str] = (),
) -> CurrentFactLineageRecoveryBinding:
    """Resolve the authoritative source seed to one exact journal call cover.

    This resolver is read-only and never calls ``provider.complete``.  It is
    intentionally strict: the missing-fact sources must have one structural
    exact cover.  Redundant partial overlaps are ignored, while a second
    independently complete cover remains ambiguous and fails closed.
    """

    cutoff = date.fromisoformat(as_of_date)
    if extraction_mode not in FACT_EXTRACTION_MODES:
        raise ValueError("unknown fact extraction mode")
    prepared = _validate_documents(
        documents,
        target_id=target_id,
        as_of_date=as_of_date,
        cutoff=cutoff,
    )
    document_by_id = {
        str(row["document_id"]): row for row in prepared
    }
    if (
        authoritative_fact_ledger.target_id != target_id
        or authoritative_fact_ledger.as_of_date != as_of_date
    ):
        raise ValueError("current fact authority target/date mismatch")
    prior_compilation = EvidenceFactCompiler().compile(
        target_id=target_id,
        as_of_date=as_of_date,
        accepted_claims=prior_material_claims,
    )
    if prior_compilation.status != "FACT_COMPILATION_COMPLETE":
        raise ValueError("persisted fact claims do not compile completely")
    persisted_rows = {
        row.fact_id: row.to_dict() for row in prior_compilation.facts
    }
    expectation = authoritative_fact_ledger.recovery_expectation(
        persisted_fact_ids=tuple(persisted_rows),
        pending_new_fact_ids=pending_new_fact_ids,
    )
    if expectation["status"] != "AUTHORITY_LOSS_RECOVERY_REQUIRED":
        raise ValueError(
            "current fact lineage binding requires an exact authority loss"
        )
    authority_rows = _exact_fact_rows_by_id(
        authoritative_fact_ledger.fact_rows,
        label="authoritative research-epoch facts",
    )
    current_projection_rows = _exact_fact_rows_by_id(
        current_facts,
        label="current fact authority projection",
    )
    if set(current_projection_rows) != set(authority_rows):
        raise ValueError("current fact authority projection is not exact")
    for fact_id, row in persisted_rows.items():
        if (
            fact_id in current_projection_rows
            and _canonical_json_value(row)
            != _canonical_json_value(current_projection_rows[fact_id])
        ):
            raise ValueError(
                "persisted fact body differs from current fact projection"
            )
    for fact_id in set(authority_rows) - set(persisted_rows):
        if _canonical_json_value(current_projection_rows[fact_id]) != (
            _canonical_json_value(authority_rows[fact_id])
        ):
            raise ValueError(
                "missing fact body differs from authoritative lineage"
            )
    seed_source_document_ids = tuple(
        str(value)
        for value in expectation["expected_recovered_source_document_ids"]
    )
    if not seed_source_document_ids or not set(
        seed_source_document_ids
    ).issubset(document_by_id):
        raise ValueError("authority-loss source seed is outside current documents")

    objective_ids = {
        str(row.get("objective_id") or "").strip()
        for row in open_objectives
    }
    if "" in objective_ids or len(objective_ids) != len(open_objectives):
        raise ValueError("fact extraction objectives require unique ids")
    objective_component_by_id = {
        str(row.get("objective_id") or "").strip(): str(
            row.get("component_id") or ""
        ).strip()
        for row in open_objectives
    }
    objective_scope_by_document: Mapping[str, frozenset[str]] | None = None
    if extraction_mode == "PRODUCTION_OBJECTIVE_LOCAL":
        if not objective_ids or any(
            value not in CANONICAL_COMPONENT_ORDER
            for value in objective_component_by_id.values()
        ):
            raise ValueError("production objective scope is invalid")
        objective_scope_by_document = {
            str(row["document_id"]): frozenset(
                str(value).strip()
                for value in row.get("objective_ids") or ()
                if str(value).strip() in objective_ids
            )
            for row in prepared
        }
        if any(not values for values in objective_scope_by_document.values()):
            raise ValueError(
                "production evidence documents lack current objective lineage"
            )
    scope_contract = load_mechanism_scope_contracts().get(archetype_id)
    if scope_contract is None:
        raise ValueError("fact extraction archetype lacks mechanism-scope contract")
    prompt_payload = _fact_extraction_primary_payload(
        target_id=target_id,
        target_name=target_name,
        target_aliases=target_aliases,
        archetype_id=archetype_id,
        as_of_date=as_of_date,
        extraction_semantics_version=FACT_EXTRACTION_SEMANTICS_VERSION,
        open_objectives=open_objectives,
        current_evidence_facts=(
            _project_current_facts_with_accepted_claims(
                current_facts=current_facts,
                accepted_claims=prior_material_claims,
                target_id=target_id,
                as_of_date=as_of_date,
            )
        ),
        score_gap_context=project_fact_extraction_score_gap_context(
            score_gap_context or {}
        ),
        scope_contract=scope_contract,
        batch=tuple(
            document_by_id[document_id]
            for document_id in seed_source_document_ids
        ),
        objective_scope_by_document=objective_scope_by_document,
        objective_component_by_id=objective_component_by_id,
    )
    exact_bindings: list[CurrentFactLineageRecoveryBinding] = []
    for semantics_version in AUTHORITY_RECOVERY_FACT_SEMANTICS_VERSIONS:
        materials = validate_current_v5_fact_lineage_materials(
            journal_root=journal_root,
            target_id=target_id,
            as_of_date=as_of_date,
            archetype_id=archetype_id,
            current_documents=prepared,
            current_fact_prompt_payload=prompt_payload,
            recovery_projection_document_ids=seed_source_document_ids,
            fact_extraction_semantics_version=semantics_version,
        )
        if materials.get("status") != "READY_FOR_OFFICIAL_SEMANTIC_REPLAY":
            continue
        try:
            binding = _current_fact_lineage_binding_from_materials(
                journal_root=journal_root,
                seed_source_document_ids=seed_source_document_ids,
                pending_new_fact_ids=pending_new_fact_ids,
                prior_document_dispositions=prior_document_dispositions,
                materials=materials,
                fact_extraction_semantics_version=semantics_version,
            )
            replay = _recover_current_fact_lineage_authority_gap(
                authoritative_fact_ledger=authoritative_fact_ledger,
                recovery_binding=binding,
                target_id=target_id,
                target_name=target_name,
                target_aliases=target_aliases,
                archetype_id=archetype_id,
                as_of_date=as_of_date,
                documents=prepared,
                open_objectives=open_objectives,
                current_facts=current_facts,
                score_gap_context=score_gap_context or {},
                prior_material_claims=prior_material_claims,
                prior_document_dispositions=prior_document_dispositions,
                scope_contract=scope_contract,
                objective_scope_by_document=objective_scope_by_document,
                objective_component_by_id=objective_component_by_id,
            )
        except (KeyError, TypeError, ValueError, RuntimeError):
            continue
        if replay.get("status") == "COMPLETE":
            exact_bindings.append(binding)
    if len(exact_bindings) != 1:
        raise ValueError(
            "current fact journal source-seed cover is ambiguous or does "
            "not reproduce the exact authoritative fact intersection"
        )
    return exact_bindings[0]


def _current_fact_lineage_binding_from_materials(
    *,
    journal_root: str | Path,
    seed_source_document_ids: Sequence[str],
    pending_new_fact_ids: Sequence[str],
    prior_document_dispositions: Sequence[Mapping[str, Any]],
    materials: Mapping[str, Any],
    fact_extraction_semantics_version: str,
) -> CurrentFactLineageRecoveryBinding:
    """Seal one structural cover before exact fact-intersection replay."""

    occurrence_counts = materials.get(
        "current_document_material_occurrence_counts"
    )
    if not isinstance(occurrence_counts, Mapping) or set(
        str(key) for key in occurrence_counts
    ) != set(seed_source_document_ids) or any(
        int(value) <= 0 for value in occurrence_counts.values()
    ):
        raise ValueError("current fact journal source-seed cover is ambiguous")
    material_rows = tuple(
        dict(row) for row in materials.get("materials") or ()
    )
    if not material_rows:
        raise ValueError("current fact journal source-seed cover is empty")
    group_ids = tuple(
        dict.fromkeys(
            str(row.get("lineage_call_group_id") or "")
            for row in material_rows
        )
    )
    if any(not value for value in group_ids):
        raise ValueError("current fact journal call-group identity is missing")
    selected_material_rows = _select_unique_raw_current_lineage_transport_cover(
        material_rows=material_rows,
        document_ids=seed_source_document_ids,
    )
    if selected_material_rows is None:
        raise ValueError("current fact journal source-seed cover is ambiguous")
    material_rows = tuple(dict(row) for row in selected_material_rows)
    group_ids = tuple(
        dict.fromkeys(
            str(row.get("lineage_call_group_id") or "")
            for row in material_rows
        )
    )
    disposition_ids = {
        str(row.get("document_id") or "")
        for row in prior_document_dispositions
    }
    expanded_by_group = {
        group_id: frozenset(
            str(document_id)
            for row in material_rows
            if row.get("lineage_call_group_id") == group_id
            for document_id in (
                row.get("validated_current_document_ids") or ()
            )
            if str(document_id) not in disposition_ids
        )
        for group_id in group_ids
    }
    expanded_ids = tuple(
        sorted(
            {
                document_id
                for values in expanded_by_group.values()
                for document_id in values
            }
        )
    )
    if (
        not set(seed_source_document_ids).issubset(expanded_ids)
        or _validated_raw_current_lineage_transport_cover(
            material_rows=material_rows,
            document_ids=expanded_ids,
        )
        is None
    ):
        raise ValueError("current fact atomic document expansion is ambiguous")
    ordered_material_rows = tuple(
        sorted(
            material_rows,
            key=lambda row: (
                str(row.get("lineage_call_group_id") or ""),
                int(row.get("continuation_page_number") or 0),
            ),
        )
    )
    return CurrentFactLineageRecoveryBinding(
        journal_root=Path(journal_root),
        seed_source_document_ids=tuple(sorted(seed_source_document_ids)),
        journal_request_ids=tuple(
            str(row["request_id"]) for row in ordered_material_rows
        ),
        journal_response_ids=tuple(
            str(row["response_id"]) for row in ordered_material_rows
        ),
        expected_recovery_document_ids=expanded_ids,
        pending_new_fact_ids=tuple(str(value) for value in pending_new_fact_ids),
        fact_extraction_semantics_version=(
            fact_extraction_semantics_version
        ),
    )


def write_researcher_fact_extraction_result(
    result: ResearcherFactExtractionResult,
    output_directory: str | Path,
) -> Mapping[str, Path]:
    root = Path(output_directory)
    root.mkdir(parents=True, exist_ok=True)
    paths = {
        key: root / filename for key, filename in FACT_EXTRACTION_OUTPUT_FILES.items()
    }
    jsonl_rows = {
        "accepted_claims": tuple(result.material_claims),
        "rejections": tuple(row.to_dict() for row in result.rejections),
        "document_dispositions": tuple(result.document_dispositions),
        "provider_calls": tuple(row.to_dict() for row in result.provider_calls),
        "facts": tuple(row.to_dict() for row in result.facts),
        "counterfacts": tuple(
            row.to_dict()
            for row in result.facts
            if row.direction == EvidenceDirection.COUNTER.value
        ),
        "claim_fact_links": tuple(
            row.to_dict() for row in result.fact_compilation.claim_fact_links
        ),
    }
    serialized = {
        paths[key]: "".join(
            json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n"
            for row in rows
        )
        for key, rows in jsonl_rows.items()
    }
    serialized[paths["audit"]] = (
        json.dumps(result.audit, ensure_ascii=False, indent=2, sort_keys=True)
        + "\n"
    )
    serialized[paths["result"]] = (
        json.dumps(result.to_dict(), ensure_ascii=False, indent=2, sort_keys=True)
        + "\n"
    )
    temporary_paths: dict[Path, Path] = {}
    try:
        for destination, content in serialized.items():
            descriptor, temporary_name = tempfile.mkstemp(
                prefix=f".{destination.name}.",
                suffix=".tmp",
                dir=root,
            )
            temporary_path = Path(temporary_name)
            temporary_paths[destination] = temporary_path
            with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
                handle.write(content)
                handle.flush()
                os.fsync(handle.fileno())
        # The embedded result audit is the checkpoint commit marker.  It is
        # replaced only after every canonical leaf and the standalone audit
        # are durable, so an interrupted migration keeps the older recovery
        # intent authoritative on the next resume.
        leaf_commit_order = (
            paths["accepted_claims"],
            paths["rejections"],
            paths["document_dispositions"],
            paths["provider_calls"],
            paths["facts"],
            paths["counterfacts"],
            paths["claim_fact_links"],
            paths["audit"],
        )
        directory_descriptor = os.open(root, os.O_RDONLY)
        try:
            for destination in leaf_commit_order:
                os.replace(temporary_paths.pop(destination), destination)
            os.fsync(directory_descriptor)
            os.replace(
                temporary_paths.pop(paths["result"]),
                paths["result"],
            )
            os.fsync(directory_descriptor)
        finally:
            os.close(directory_descriptor)
    finally:
        for temporary_path in temporary_paths.values():
            try:
                temporary_path.unlink()
            except FileNotFoundError:
                pass
    return paths


def production_material_fact_rows(
    result: ResearcherFactExtractionResult,
) -> tuple[Mapping[str, Any], ...]:
    """Project verified claims into the isolated Phase 93 comparison contract."""

    claim_by_id = {
        str(row["claim_id"]): row for row in result.material_claims
    }
    output = []
    for fact in result.facts:
        primary = claim_by_id[str(fact.claim_ids[0])]
        output.append(
            {
                "schema_version": "e2r_v5_production_material_fact_v1",
                "fact_id": fact.fact_id,
                "target_id": fact.target_id,
                "discovery_origin": "CANONICAL_SOURCE_TASK",
                "question_family_id": primary["question_family_id"],
                "subject_id": primary["subject_id"],
                "predicate_family": primary["predicate_family"],
                "normalized_object": primary["normalized_object"],
                "period": fact.period,
                "mechanism_scope_id": primary["mechanism_scope_id"],
                "source_id": fact.source_ids[0],
                "source_ids": list(fact.source_ids),
                "source_tier": primary["source_tier"],
                "temporal_status": "CURRENT",
                "as_of_date": fact.as_of_date,
                "materiality": primary["materiality"],
                "fact_role": (
                    "SUPERSESSION"
                    if fact.current_lifecycle == EvidenceLifecycle.SUPERSEDED.value
                    else "COUNTER"
                    if fact.direction == EvidenceDirection.COUNTER.value
                    else "SUPPORT"
                ),
                "economic_mechanism": fact.economic_mechanism,
                "predicate": fact.predicate,
                "value": fact.value,
                "confidence": fact.confidence,
                "claim_ids": list(fact.claim_ids),
                "quote_ids": list(fact.quote_ids),
                "gold_visibility": False,
            }
        )
    return tuple(output)


def _document_batches(
    documents: Sequence[Mapping[str, Any]],
    *,
    max_documents: int,
    max_chars: int,
) -> tuple[tuple[Mapping[str, Any], ...], ...]:
    batches: list[tuple[Mapping[str, Any], ...]] = []
    current: list[Mapping[str, Any]] = []
    current_chars = 0
    for document in documents:
        boundary_context = document.get("_source_boundary_context") or {}
        chars = len(str(document.get("content_text") or "")) + len(
            str(boundary_context.get("preceding_tail_text") or "")
        )
        if int(document.get("transport_chunk_count") or 1) > 1:
            if current:
                batches.append(tuple(current))
                current = []
                current_chars = 0
            batches.append((document,))
            continue
        if current and (
            len(current) >= max_documents or current_chars + chars > max_chars
        ):
            batches.append(tuple(current))
            current = []
            current_chars = 0
        current.append(document)
        current_chars += chars
    if current:
        batches.append(tuple(current))
    return tuple(batches)


def _validate_documents(
    documents: Sequence[Mapping[str, Any]],
    *,
    target_id: str,
    as_of_date: str,
    cutoff: date,
) -> tuple[Mapping[str, Any], ...]:
    rows = tuple(dict(row) for row in documents)
    ids = [str(row.get("document_id") or "") for row in rows]
    if not rows:
        return ()
    if any(not value for value in ids) or len(ids) != len(set(ids)):
        raise ValueError("fact extraction documents require unique ids")
    for row in rows:
        if str(row.get("target_id") or "") != target_id:
            raise ValueError("fact extraction received a cross-target document")
        if str(row.get("as_of_date") or "") != as_of_date:
            raise ValueError("fact extraction document as_of_date mismatch")
        if (
            not row.get("full_fetch_performed")
            or row.get("snippet_only")
            or row.get("snippet_used_as_document")
            or not row.get("evidence_eligible")
        ):
            raise ValueError("fact extraction requires full evidence-eligible documents")
        published = date.fromisoformat(str(row.get("published_at") or "")[:10])
        available = date.fromisoformat(str(row.get("available_at") or "")[:10])
        if published > cutoff or available > cutoff:
            raise ValueError("future document cannot enter fact extraction")
        text = str(row.get("content_text") or "")
        if not text.strip() or hashlib.sha256(text.encode("utf-8")).hexdigest() != str(
            row.get("content_hash") or ""
        ):
            raise ValueError("fact extraction document content/hash mismatch")
    return rows


def _document_prompt_row(
    row: Mapping[str, Any],
    *,
    source_boundary_context: Mapping[str, Any] | None = None,
) -> Mapping[str, Any]:
    payload = {
        "document_id": row["document_id"],
        "canonical_url": row["canonical_url"],
        "title": row.get("title"),
        "source_family": row["source_family"],
        "published_at": row["published_at"],
        "available_at": row["available_at"],
        "source_independence_group": row["source_independence_group"],
        "objective_ids": list(row.get("objective_ids") or ()),
        "content_text": row["content_text"],
        "full_fetch_performed": True,
        "snippet_used_as_document": False,
    }
    if source_boundary_context is not None:
        payload["source_boundary_context"] = {
            **dict(source_boundary_context),
            "instruction": (
                "This literal tail belongs to the immediately preceding chunk "
                "of the same fully fetched canonical source. Use it only to "
                "interpret a table heading, period, sentence, or section that "
                "continues into content_text. Never emit a fact whose exact_quote "
                "exists only in this context: every accepted exact_quote must "
                "still be copied from this document's content_text."
            ),
        }
    if int(row.get("transport_chunk_count") or 1) > 1:
        payload["transport_chunk"] = {
            "transport_chunk_id": row["transport_chunk_id"],
            "chunk_index": int(row["transport_chunk_index"]),
            "chunk_count": int(row["transport_chunk_count"]),
            "start_char": int(row["transport_chunk_start"]),
            "end_char": int(row["transport_chunk_end"]),
            "chunk_content_hash": row["transport_chunk_content_hash"],
            "full_document_content_hash": row["content_hash"],
            "full_document_text_chars": int(
                row["full_document_text_chars"]
            ),
            "all_chunks_required_before_document_completion": True,
            "instruction": (
                "Inspect and dispose only this literal transport chunk. "
                "NO_MATERIAL_FACT for one chunk does not prove that the "
                "canonical parent document lacks a fact; deterministic code "
                "aggregates the parent only after every chunk is complete."
            ),
        }
    return payload


def _fact_extraction_primary_payload(
    *,
    target_id: str,
    target_name: str,
    target_aliases: Sequence[str],
    archetype_id: str,
    as_of_date: str,
    extraction_semantics_version: str,
    open_objectives: Sequence[Mapping[str, Any]],
    current_evidence_facts: Mapping[str, Any],
    score_gap_context: Mapping[str, Any],
    scope_contract: ArchetypeMechanismScopeContract,
    batch: Sequence[Mapping[str, Any]],
    objective_scope_by_document: Mapping[str, frozenset[str]] | None,
    objective_component_by_id: Mapping[str, str],
    objective_lineage_reassessment_rows: Sequence[Mapping[str, Any]] = (),
) -> Mapping[str, Any]:
    """Build the immutable fact prompt contract shared with migration replay."""

    batch_document_ids = {
        str(row["document_id"]) for row in batch
    }
    return scrub_blind_research_payload(
        {
            "target_id": target_id,
            "target_name": target_name,
            "target_aliases": list(target_aliases),
            "archetype_hypothesis": archetype_id,
            "as_of_date": as_of_date,
            "fact_extraction_semantics_version": (
                extraction_semantics_version
            ),
            "open_research_objectives": [
                dict(row) for row in open_objectives
            ],
            "current_evidence_facts": dict(current_evidence_facts),
            "score_gap_context": dict(score_gap_context),
            "normalization_contract": {
                "question_family_id": (
                    "stable semantic research-question family, not a query string"
                ),
                "subject_id": (
                    "stable target business/product/mechanism subject"
                ),
                "predicate_family": "stable economic predicate family",
                "normalized_object": "concise normalized economic object or state",
                "value": (
                    "Use a JSON number only for one finite quantitative "
                    "point. Use a JSON string for text, ranges, identifiers, "
                    "and dates. Do not encode arbitrary objects or arrays."
                ),
                "mechanism_scope_id": (
                    "target-direct business mechanism, never industry or "
                    "wrong-segment proxy"
                ),
            },
            "deterministic_mechanism_scope_contract": {
                "allowed_business_segments": list(
                    scope_contract.allowed_business_segments
                ),
                "allowed_product_families": list(
                    scope_contract.allowed_product_families
                ),
                "allowed_technology_families": list(
                    scope_contract.allowed_technology_families
                ),
                "allowed_transaction_types": list(
                    scope_contract.allowed_transaction_types
                ),
                "allowed_economic_mechanisms": list(
                    scope_contract.allowed_economic_mechanisms
                ),
                "generic_company_allowed_components": list(
                    scope_contract.generic_company_allowed_components
                ),
                "forbidden_business_segments": list(
                    scope_contract.forbidden_business_segments
                ),
                "forbidden_product_families": list(
                    scope_contract.forbidden_product_families
                ),
                "issuer_wide_fact_encoding": {
                    "scope_business_segment": "CORPORATE_GENERIC",
                    "scope_product_family": "CORPORATE_GENERIC",
                    "scope_technology_family": "CORPORATE_GENERIC",
                    "scope_transaction_type": "GENERIC_INFORMATION",
                    "scope_economic_mechanism": "INFORMATION_ONLY",
                    "allowed_only_for_components": list(
                        scope_contract.generic_company_allowed_components
                    ),
                    "instruction": (
                        "Use these exact scope tokens for issuer-wide liquidity, "
                        "capital allocation, funding, governance, or information-quality "
                        "facts that are not attributable to the archetype business segment."
                    ),
                },
            },
            "full_documents": [
                _document_prompt_row(
                    row,
                    source_boundary_context=(
                        row.get("_source_boundary_context")
                    ),
                )
                for row in batch
            ],
            **(
                {
                    "fact_extraction_scope_contract": {
                        "mode": "PRODUCTION_OBJECTIVE_LOCAL",
                        "allowed_objective_relations": sorted(
                            OBJECTIVE_FACT_RELATIONS
                        ),
                        "objective_component_rows": [
                            {
                                "objective_id": objective_id,
                                "component_id": (
                                    objective_component_by_id[objective_id]
                                ),
                            }
                            for objective_id in sorted(
                                {
                                    objective_id
                                    for document_id in batch_document_ids
                                    for objective_id in (
                                        objective_scope_by_document[
                                            document_id
                                        ]
                                    )
                                }
                            )
                        ],
                        "document_objective_ids": [
                            {
                                "document_id": str(row["document_id"]),
                                "objective_ids": sorted(
                                    objective_scope_by_document[
                                        str(row["document_id"])
                                    ]
                                ),
                            }
                            for row in batch
                        ],
                        "material_fact_definition": (
                            "A source-backed fact is material in this "
                            "production pass only when it directly "
                            "advances, counters, or supersedes at least "
                            "one document-linked current research "
                            "objective, with the unresolved facts and "
                            "questions in score_gap_context controlling "
                            "the present research focus. General "
                            "background, adjacent technology history, "
                            "and facts that do not affect that focus "
                            "must not be emitted."
                        ),
                        "completion_definition": (
                            "extraction_complete means no further "
                            "distinct objective-linked fact remains in "
                            "the supplied document batch; it never "
                            "means every generally economic sentence "
                            "in the document was exhausted."
                        ),
                        "deterministic_validation_scope": (
                            "objective roster, document lineage, exact "
                            "quote, as_of_date, and closed-vocabulary "
                            "mechanism coordinates plus objective-component "
                            "compatibility only"
                        ),
                        "llm_owns_economic_relevance": True,
                        **(
                            {
                                "objective_lineage_reassessment": {
                                    "enabled": True,
                                    "documents": [
                                        dict(row)
                                        for row in (
                                            objective_lineage_reassessment_rows
                                        )
                                    ],
                                    "instruction": (
                                        "For this stale-semantics full-document "
                                        "coverage refresh, independently reassess which "
                                        "listed current open objectives each literal "
                                        "source fact advances, counters, or supersedes, "
                                        "including an objective outside the document's "
                                        "original discovery lineage. Re-read compound "
                                        "statements as distinct atomic economic legs when "
                                        "each leg has its own literal numeric, temporal, "
                                        "cash-flow, valuation, or market-response meaning "
                                        "needed to reconstruct the source statement. Emit "
                                        "only economically material relations supported by "
                                        "the supplied full text. The proposal's closed-"
                                        "vocabulary mechanism scope must allow the component "
                                        "of every cited objective. The expanded candidate "
                                        "roster is not evidence that a relation exists, and "
                                        "does not make general background material."
                                    ),
                                }
                            }
                            if objective_lineage_reassessment_rows
                            else {}
                        ),
                    }
                }
                if objective_scope_by_document is not None
                else {}
            ),
        }
    )


def _source_boundary_context_by_document_id(
    documents: Sequence[Mapping[str, Any]],
    *,
    context_chars: int = SOURCE_BOUNDARY_CONTEXT_CHARS,
) -> Mapping[str, Mapping[str, Any]]:
    """Bind a chunk start to the literal tail of its canonical predecessor.

    Official source materialization preserves every chunk, but a size boundary
    can fall between a table's period heading and its first value.  The
    predecessor tail is therefore prompt-only context: it does not change the
    canonical document, its content hash, or the exact-quote authority of the
    current chunk.
    """

    if isinstance(context_chars, bool) or not isinstance(context_chars, int):
        raise ValueError("source boundary context size must be a positive integer")
    if context_chars <= 0:
        raise ValueError("source boundary context size must be a positive integer")
    groups: dict[str, dict[int, Mapping[str, Any]]] = {}
    for row in documents:
        full_source_id = str(row.get("full_source_document_id") or "").strip()
        raw_index = row.get("chunk_index")
        raw_count = row.get("chunk_count")
        if not full_source_id:
            continue
        if (
            isinstance(raw_index, bool)
            or not isinstance(raw_index, int)
            or raw_index < 0
            or isinstance(raw_count, bool)
            or not isinstance(raw_count, int)
            or raw_count <= 0
            or raw_index >= raw_count
            or row.get("all_chunks_preserved") is not True
        ):
            raise ValueError("canonical source chunk metadata is malformed")
        group = groups.setdefault(full_source_id, {})
        if raw_index in group:
            raise ValueError("canonical source chunk index is duplicated")
        group[raw_index] = row

    output: dict[str, Mapping[str, Any]] = {}
    for full_source_id, indexed_rows in groups.items():
        counts = {int(row["chunk_count"]) for row in indexed_rows.values()}
        source_hashes = {
            str(row.get("full_source_content_hash") or "")
            for row in indexed_rows.values()
        }
        canonical_urls = {
            str(row.get("canonical_url") or "")
            for row in indexed_rows.values()
        }
        targets = {
            str(row.get("target_id") or "")
            for row in indexed_rows.values()
        }
        if (
            len(counts) != 1
            or len(source_hashes) != 1
            or "" in source_hashes
            or len(canonical_urls) != 1
            or len(targets) != 1
        ):
            raise ValueError("canonical source chunks disagree on source identity")
        chunk_count = next(iter(counts))
        if set(indexed_rows) != set(range(chunk_count)):
            raise ValueError("canonical source chunks are not fully preserved")
        for index in range(1, chunk_count):
            current = indexed_rows[index]
            preceding = indexed_rows[index - 1]
            preceding_text = str(preceding.get("content_text") or "")
            context_text = preceding_text[-context_chars:]
            if not context_text:
                raise ValueError("canonical predecessor chunk is empty")
            output[str(current["document_id"])] = {
                "schema_version": "e2r_v5_source_boundary_context_v1",
                "full_source_document_id": full_source_id,
                "current_chunk_index": index,
                "preceding_chunk_index": index - 1,
                "preceding_document_id": str(preceding["document_id"]),
                "preceding_content_hash": str(preceding["content_hash"]),
                "preceding_tail_chars": len(context_text),
                "preceding_tail_text": context_text,
                "context_only": True,
                "current_document_exact_quote_authority": True,
                "preceding_context_exact_quote_authority": False,
            }
    return output


def _boundary_context_reextraction_document_ids(
    *,
    documents: Sequence[Mapping[str, Any]],
    source_boundary_context_by_document_id: Mapping[
        str, Mapping[str, Any]
    ],
    prior_material_claims: Sequence[Mapping[str, Any]],
    prior_document_dispositions: Sequence[Mapping[str, Any]],
    prior_provider_calls: Sequence[FactExtractionProviderCall],
) -> frozenset[str]:
    """Invalidate an old call atomically when a claim lacked chunk context.

    A provider call is the durable response unit.  If one member contained a
    claim from a non-initial canonical source chunk under the pre-context
    semantics, removing only that claim would leave its call, disposition, and
    compiled fact out of sync.  Expand to every document in the same completed
    call and re-extract that bounded unit from the canonical source instead.
    """

    document_ids = {
        str(row.get("document_id") or "") for row in documents
    }
    document_by_id = {
        str(row.get("document_id") or ""): row for row in documents
    }
    stale_document_ids = {
        str(row.get("document_id") or "")
        for row in prior_document_dispositions
        if _fact_semantics_upgrade_requires_reextraction(
            previous_version=_extraction_semantics_version(row),
            document=document_by_id.get(
                str(row.get("document_id") or "")
            ),
        )
    }
    stale_document_ids.update(
        document_id
        for call in prior_provider_calls
        for document_id in call.document_ids
        if _fact_semantics_upgrade_requires_reextraction(
            previous_version=call.extraction_semantics_version,
            document=document_by_id.get(document_id),
        )
    )
    affected = {
        str(claim.get("document_id") or "")
        for claim in prior_material_claims
        if str(claim.get("document_id") or "")
        in source_boundary_context_by_document_id
        and str(claim.get("document_id") or "") in stale_document_ids
    }
    affected.update(
        document_id
        for document_id in stale_document_ids
        if str(
            (document_by_id.get(document_id) or {}).get("source_family")
            or ""
        ).upper()
        == "PUBLIC_BROKER_PDF"
    )
    if not affected:
        return frozenset()
    changed = True
    while changed:
        changed = False
        for call in prior_provider_calls:
            call_document_ids = set(call.document_ids)
            if affected & call_document_ids and not call_document_ids <= affected:
                affected.update(call_document_ids)
                changed = True
    if not affected <= document_ids:
        raise ValueError(
            "boundary-context re-extraction escaped current document scope"
        )
    return frozenset(affected)


def _document_transport_chunks(
    document: Mapping[str, Any],
    *,
    max_chars: int,
    source_boundary_context: Mapping[str, Any] | None = None,
) -> tuple[Mapping[str, Any], ...]:
    """Split one canonical document into overlapping literal transport chunks."""

    text = str(document.get("content_text") or "")
    boundary_context_chars = len(
        str(
            (source_boundary_context or {}).get(
                "preceding_tail_text"
            )
            or ""
        )
    )
    first_chunk_max_chars = max_chars - boundary_context_chars
    if first_chunk_max_chars <= 0:
        raise ValueError("source boundary context exhausts fact transport bound")
    if len(text) <= first_chunk_max_chars:
        return (
            {
                **dict(document),
                **(
                    {"_source_boundary_context": dict(source_boundary_context)}
                    if source_boundary_context is not None
                    else {}
                ),
            },
        )
    overlap = min(4_000, max(1_000, max_chars // 50))
    ranges: list[tuple[int, int]] = []
    start = 0
    while start < len(text):
        chunk_bound = first_chunk_max_chars if not ranges else max_chars
        hard_end = min(len(text), start + chunk_bound)
        end = hard_end
        if hard_end < len(text):
            minimum_boundary = start + int(chunk_bound * 0.80)
            newline = text.rfind("\n", minimum_boundary, hard_end)
            if newline >= minimum_boundary:
                end = newline + 1
        if end <= start:
            end = hard_end
        ranges.append((start, end))
        if end >= len(text):
            break
        next_start = max(start + 1, end - overlap)
        start = next_start
    chunks: list[Mapping[str, Any]] = []
    count = len(ranges)
    for index, (chunk_start, chunk_end) in enumerate(ranges):
        chunk_text = text[chunk_start:chunk_end]
        chunk_id = stable_intelligence_id(
            "FACTCHUNK",
            {
                "document_id": document["document_id"],
                "content_hash": document["content_hash"],
                "start": chunk_start,
                "end": chunk_end,
            },
        )
        chunks.append(
            {
                **dict(document),
                "content_text": chunk_text,
                **(
                    {"_source_boundary_context": dict(source_boundary_context)}
                    if index == 0 and source_boundary_context is not None
                    else {}
                ),
                "transport_chunk_id": chunk_id,
                "transport_chunk_index": index,
                "transport_chunk_count": count,
                "transport_chunk_start": chunk_start,
                "transport_chunk_end": chunk_end,
                "transport_chunk_content_hash": hashlib.sha256(
                    chunk_text.encode("utf-8")
                ).hexdigest(),
                "full_document_text_chars": len(text),
            }
        )
    if (
        not chunks
        or chunks[0]["transport_chunk_start"] != 0
        or chunks[-1]["transport_chunk_end"] != len(text)
        or any(
            len(str(row["content_text"]))
            + len(
                str(
                    (row.get("_source_boundary_context") or {}).get(
                        "preceding_tail_text"
                    )
                    or ""
                )
            )
            > max_chars
            for row in chunks
        )
        or any(
            int(right["transport_chunk_start"])
            > int(left["transport_chunk_end"])
            for left, right in zip(chunks, chunks[1:])
        )
    ):
        raise ValueError("fact transport chunks do not cover the full document")
    return tuple(chunks)


def _split_chunk_ids_by_document(
    documents: Sequence[Mapping[str, Any]],
) -> Mapping[str, tuple[str, ...]]:
    output: dict[str, list[str]] = {}
    for row in documents:
        if int(row.get("transport_chunk_count") or 1) <= 1:
            continue
        output.setdefault(str(row["document_id"]), []).append(
            str(row["transport_chunk_id"])
        )
    return {key: tuple(values) for key, values in output.items()}


def _batch_transport_chunk_ids(
    batch: Sequence[Mapping[str, Any]],
) -> tuple[str, ...]:
    return tuple(
        str(row["transport_chunk_id"])
        for row in batch
        if row.get("transport_chunk_id")
    )


def _resume_completed_transport_chunks(
    *,
    calls: Sequence[FactExtractionProviderCall],
    transport_documents: Sequence[Mapping[str, Any]],
    target_id: str,
    as_of_date: str,
) -> tuple[
    list[FactExtractionProviderCall],
    list[Mapping[str, Any]],
    list[Mapping[str, Any]],
    set[str],
]:
    """Restore only self-contained COMPLETE chunk checkpoints.

    A split parent has no canonical disposition until every chunk is complete.
    The provider-call ledger therefore embeds the verified claims and per-chunk
    disposition needed for a clean resume.  Legacy calls without that embedded
    state, stale chunk ids, or internally inconsistent rows are ignored so the
    provider safely reprocesses those chunks instead of promoting partial data.
    """

    chunk_by_id = {
        str(row.get("transport_chunk_id") or ""): row
        for row in transport_documents
        if str(row.get("transport_chunk_id") or "")
    }
    structurally_valid: list[
        tuple[
            FactExtractionProviderCall,
            tuple[Mapping[str, Any], ...],
            tuple[Mapping[str, Any], ...],
        ]
    ] = []
    for call in calls:
        chunk_ids = tuple(call.transport_chunk_ids)
        if (
            not chunk_ids
            or call.accepted_claims is None
            or len(chunk_ids) != len(set(chunk_ids))
            or any(chunk_id not in chunk_by_id for chunk_id in chunk_ids)
        ):
            continue
        chunks = tuple(chunk_by_id[chunk_id] for chunk_id in chunk_ids)
        chunk_document_ids = tuple(
            str(row.get("document_id") or "") for row in chunks
        )
        if (
            any(not value for value in chunk_document_ids)
            or len(chunk_document_ids) != len(set(chunk_document_ids))
            or set(chunk_document_ids) != set(call.document_ids)
        ):
            continue
        disposition_by_chunk_id = {
            str(row.get("transport_chunk_id") or ""): row
            for row in call.document_dispositions
            if str(row.get("transport_chunk_id") or "")
        }
        if (
            len(disposition_by_chunk_id) != len(call.document_dispositions)
            or set(disposition_by_chunk_id) != set(chunk_ids)
        ):
            continue
        chunk_by_document_id = {
            str(row["document_id"]): row for row in chunks
        }
        claims = tuple(dict(row) for row in call.accepted_claims)
        claim_ids = tuple(
            str(row.get("claim_id") or "") for row in claims
        )
        if (
            any(not value for value in claim_ids)
            or len(claim_ids) != len(set(claim_ids))
            or set(claim_ids) != set(call.accepted_claim_ids)
        ):
            continue
        claims_by_document: dict[str, list[Mapping[str, Any]]] = {}
        claims_valid = True
        for claim in claims:
            document_id = str(claim.get("document_id") or "")
            document = chunk_by_document_id.get(document_id)
            if (
                document is None
                or str(claim.get("target_id") or "") != target_id
                or str(claim.get("as_of_date") or "") != as_of_date
                or not str(claim.get("exact_quote") or "")
                or str(claim.get("exact_quote") or "")
                not in str(document.get("content_text") or "")
            ):
                claims_valid = False
                break
            claims_by_document.setdefault(document_id, []).append(claim)
        if not claims_valid:
            continue
        dispositions = tuple(
            dict(disposition_by_chunk_id[chunk_id])
            for chunk_id in chunk_ids
        )
        dispositions_valid = True
        for disposition in dispositions:
            chunk_id = str(disposition["transport_chunk_id"])
            document = chunk_by_id[chunk_id]
            document_id = str(disposition.get("document_id") or "")
            accepted_count = len(claims_by_document.get(document_id, ()))
            status = str(disposition.get("status") or "")
            if (
                document_id != str(document.get("document_id") or "")
                or int(disposition.get("accepted_fact_count") or 0)
                != accepted_count
                or (status == "FACTS_EXTRACTED") != bool(accepted_count)
                or status
                not in {
                    "FACTS_EXTRACTED",
                    "NO_MATERIAL_FACT",
                    "WRONG_TARGET_OR_SEGMENT",
                }
            ):
                dispositions_valid = False
                break
        if not dispositions_valid:
            continue
        structurally_valid.append((call, claims, dispositions))

    chunk_occurrence_count: dict[str, int] = {}
    for call, _, _ in structurally_valid:
        for chunk_id in call.transport_chunk_ids:
            chunk_occurrence_count[chunk_id] = (
                chunk_occurrence_count.get(chunk_id, 0) + 1
            )
    resumed_calls: list[FactExtractionProviderCall] = []
    resumed_claims: list[Mapping[str, Any]] = []
    resumed_dispositions: list[Mapping[str, Any]] = []
    resumed_chunk_ids: set[str] = set()
    for call, claims, dispositions in structurally_valid:
        if any(
            chunk_occurrence_count.get(chunk_id) != 1
            for chunk_id in call.transport_chunk_ids
        ):
            continue
        resumed_calls.append(call)
        resumed_claims.extend(claims)
        resumed_dispositions.extend(dispositions)
        resumed_chunk_ids.update(call.transport_chunk_ids)
    return (
        resumed_calls,
        resumed_claims,
        resumed_dispositions,
        resumed_chunk_ids,
    )


def _reconcile_transport_chunks(
    *,
    claims: Sequence[Mapping[str, Any]],
    dispositions: Sequence[Mapping[str, Any]],
    pending: Sequence[str],
    split_chunk_ids_by_document: Mapping[str, tuple[str, ...]],
    pending_transport_chunk_ids: set[str],
    target_id: str,
    as_of_date: str,
) -> tuple[list[Mapping[str, Any]], list[Mapping[str, Any]], list[str]]:
    deduped_claims = list(
        {
            str(row.get("claim_id") or stable_intelligence_id("CLAIM", row)): row
            for row in claims
        }.values()
    )
    if not split_chunk_ids_by_document:
        return deduped_claims, list(dispositions), list(pending)
    by_document: dict[str, list[Mapping[str, Any]]] = {}
    for row in dispositions:
        document_id = str(row.get("document_id") or "")
        if document_id in split_chunk_ids_by_document:
            by_document.setdefault(document_id, []).append(row)
    output_dispositions = [
        row
        for row in dispositions
        if str(row.get("document_id") or "")
        not in split_chunk_ids_by_document
    ]
    output_pending = list(pending)
    incomplete_document_ids: set[str] = set()
    for document_id, expected_chunk_ids in split_chunk_ids_by_document.items():
        rows = by_document.get(document_id, [])
        completed_chunk_ids = {
            str(row.get("transport_chunk_id") or "")
            for row in rows
            if str(row.get("transport_chunk_id") or "")
        }
        expected = set(expected_chunk_ids)
        incomplete = (
            completed_chunk_ids != expected
            or bool(expected & pending_transport_chunk_ids)
        )
        if incomplete:
            incomplete_document_ids.add(document_id)
            output_pending.append(
                "INCOMPLETE_DOCUMENT_TRANSPORT_CHUNKS:"
                f"{document_id}:{len(completed_chunk_ids)}/{len(expected)}"
            )
            continue
        document_claims = [
            row
            for row in deduped_claims
            if str(row.get("document_id") or "") == document_id
        ]
        statuses = [str(row.get("status") or "") for row in rows]
        status = (
            "FACTS_EXTRACTED"
            if document_claims
            else "WRONG_TARGET_OR_SEGMENT"
            if statuses and all(value == "WRONG_TARGET_OR_SEGMENT" for value in statuses)
            else "NO_MATERIAL_FACT"
        )
        rationales = tuple(
            dict.fromkeys(
                str(row.get("rationale") or "").strip()
                for row in rows
                if str(row.get("rationale") or "").strip()
            )
        )
        output_dispositions.append(
            {
                "schema_version": "e2r_v5_fact_document_disposition_v1",
                "extraction_semantics_version": (
                    FACT_EXTRACTION_SEMANTICS_VERSION
                ),
                "batch_id": stable_intelligence_id(
                    "FACTDOCAGG",
                    {
                        "target_id": target_id,
                        "as_of_date": as_of_date,
                        "document_id": document_id,
                        "transport_chunk_ids": list(expected_chunk_ids),
                    },
                ),
                "document_id": document_id,
                "status": status,
                "rationale": " | ".join(rationales),
                "accepted_fact_count": len(document_claims),
                "source_absence_proven": False,
                "production_score_authority": False,
                "transport_chunk_count": len(expected_chunk_ids),
                "completed_transport_chunk_count": len(completed_chunk_ids),
                "transport_chunk_ids": list(expected_chunk_ids),
                "all_transport_chunks_complete": True,
            }
        )
    if incomplete_document_ids:
        deduped_claims = [
            row
            for row in deduped_claims
            if str(row.get("document_id") or "")
            not in incomplete_document_ids
        ]
    return deduped_claims, output_dispositions, output_pending


def _validate_response(
    response: Mapping[str, Any],
    *,
    batch_id: str,
    documents: Sequence[Mapping[str, Any]],
    target_id: str,
    as_of_date: str,
    scope_contract: ArchetypeMechanismScopeContract,
    provider_name: str,
    prompt_hash: str,
    response_hash: str,
    previously_accepted_claim_counts: Mapping[str, int] | None = None,
    previously_accepted_semantic_identities: (
        Mapping[str, Sequence[str]] | None
    ) = None,
    previously_rejected_material_quote_failure_counts: (
        Mapping[str, int] | None
    ) = None,
    objective_scope_by_document: (
        Mapping[str, frozenset[str]] | None
    ) = None,
    objective_component_by_id: Mapping[str, str] | None = None,
    extraction_semantics_version: str = FACT_EXTRACTION_SEMANTICS_VERSION,
) -> tuple[
    list[Mapping[str, Any]],
    list[FactExtractionRejection],
    list[Mapping[str, Any]],
    list[str],
    list[str],
    bool,
]:
    document_by_id = {str(row["document_id"]): row for row in documents}
    raw_facts = response.get("facts")
    raw_dispositions = response.get("document_dispositions")
    unresolved = response.get("unresolved_document_ids")
    notes = response.get("unresolved_research_notes")
    if any(
        isinstance(value, (str, bytes)) or not isinstance(value, Sequence)
        for value in (raw_facts, raw_dispositions, unresolved, notes)
    ):
        raise TypeError("fact extraction arrays are malformed")
    claims: list[Mapping[str, Any]] = []
    rejections: list[FactExtractionRejection] = []
    pending: list[str] = []
    feedback: list[str] = []
    accepted_by_document: dict[str, int] = {
        str(document_id): int(count)
        for document_id, count in (
            previously_accepted_claim_counts or {}
        ).items()
        if str(document_id) in document_by_id and int(count) > 0
    }
    accepted_identities_by_document = {
        str(document_id): frozenset(
            str(value)
            for value in values
            if str(value)
        )
        for document_id, values in (
            previously_accepted_semantic_identities or {}
        ).items()
        if str(document_id) in document_by_id
    }
    for index, raw_proposal in enumerate(raw_facts):
        proposal = _normalize_transport_fact_proposal(
            raw_proposal,
            document_by_id=document_by_id,
        )
        document_id = (
            str(proposal.get("document_id") or "")
            if isinstance(proposal, Mapping)
            else ""
        )
        material = bool(proposal.get("material")) if isinstance(proposal, Mapping) else False
        proposed_exact_quote = (
            str(proposal.get("exact_quote") or "").strip()
            if isinstance(proposal, Mapping)
            else ""
        )
        if (
            material
            and proposed_exact_quote
            and _fact_semantic_identity(proposal)
            in accepted_identities_by_document.get(
                document_id,
                frozenset(),
            )
        ):
            rejections.append(
                FactExtractionRejection(
                    batch_id=batch_id,
                    proposal_index=index,
                    document_id=document_id,
                    reason="PREVIOUSLY_ACCEPTED_EXACT_QUOTE_REPEATED",
                    material_proposal=False,
                    proposed_exact_quote=proposed_exact_quote,
                    extraction_semantics_version=extraction_semantics_version,
                )
            )
            continue
        objective_scope_reason = _objective_scope_rejection_reason(
            proposal,
            objective_scope_by_document=objective_scope_by_document,
            objective_component_by_id=objective_component_by_id,
            target_id=target_id,
            scope_contract=scope_contract,
        )
        if objective_scope_reason:
            rejections.append(
                FactExtractionRejection(
                    batch_id=batch_id,
                    proposal_index=index,
                    document_id=document_id,
                    reason=objective_scope_reason,
                    material_proposal=material,
                    proposed_exact_quote=proposed_exact_quote or None,
                    extraction_semantics_version=extraction_semantics_version,
                )
            )
            if material:
                pending.append(
                    "MATERIAL_FACT_PROPOSAL_REJECTED:"
                    f"{document_id}:{objective_scope_reason}"
                )
            continue
        reason = _proposal_rejection_reason(
            proposal,
            document_by_id=document_by_id,
            target_id=target_id,
            scope_contract=scope_contract,
        )
        if reason:
            rejections.append(
                FactExtractionRejection(
                    batch_id=batch_id,
                    proposal_index=index,
                    document_id=document_id,
                    reason=reason,
                    material_proposal=material,
                    proposed_exact_quote=(
                        str(proposal.get("exact_quote") or "").strip() or None
                        if isinstance(proposal, Mapping)
                        else None
                    ),
                    extraction_semantics_version=extraction_semantics_version,
                )
            )
            if material and not reason.startswith("MECHANISM_SCOPE_REJECTED"):
                pending.append(f"MATERIAL_FACT_PROPOSAL_REJECTED:{document_id}:{reason}")
            continue
        assert isinstance(proposal, Mapping)
        if not material:
            rejections.append(
                FactExtractionRejection(
                    batch_id=batch_id,
                    proposal_index=index,
                    document_id=document_id,
                    reason="IMMATERIAL_PROPOSAL_TERMINAL",
                    material_proposal=False,
                    proposed_exact_quote=(
                        str(proposal.get("exact_quote") or "").strip() or None
                    ),
                    extraction_semantics_version=extraction_semantics_version,
                )
            )
            continue
        document = document_by_id[document_id]
        allowed_component_ids, _ = _allowed_components(
            proposal,
            target_id=target_id,
            scope_contract=scope_contract,
        )
        claim = _accepted_claim(
            proposal,
            document=document,
            target_id=target_id,
            as_of_date=as_of_date,
            provider_name=provider_name,
            prompt_hash=prompt_hash,
            response_hash=response_hash,
            allowed_component_ids=allowed_component_ids,
        )
        claims.append(claim)
        accepted_by_document[document_id] = accepted_by_document.get(document_id, 0) + 1
    dispositions: list[Mapping[str, Any]] = []
    disposition_ids: list[str] = []
    for raw in raw_dispositions:
        if not isinstance(raw, Mapping):
            pending.append("INVALID_DOCUMENT_DISPOSITION_OBJECT")
            continue
        document_id = str(raw.get("document_id") or "")
        status = str(raw.get("status") or "")
        rationale = str(raw.get("rationale") or "").strip()
        if document_id not in document_by_id:
            pending.append(f"UNKNOWN_DOCUMENT_DISPOSITION:{document_id}")
            continue
        document = document_by_id[document_id]
        if status not in {
            "FACTS_EXTRACTED",
            "NO_MATERIAL_FACT",
            "WRONG_TARGET_OR_SEGMENT",
            "UNREADABLE",
        } or not rationale:
            pending.append(f"INVALID_DOCUMENT_DISPOSITION:{document_id}")
            continue
        if status == "FACTS_EXTRACTED" and not accepted_by_document.get(document_id):
            pending.append(f"FACTS_EXTRACTED_WITHOUT_ACCEPTED_FACT:{document_id}")
        if status != "FACTS_EXTRACTED" and accepted_by_document.get(document_id):
            pending.append(f"ACCEPTED_FACT_DISPOSITION_MISMATCH:{document_id}")
        if (
            status == "NO_MATERIAL_FACT"
            and int(
                (previously_rejected_material_quote_failure_counts or {}).get(
                    document_id,
                    0,
                )
            )
            > 0
            and not accepted_by_document.get(document_id)
        ):
            pending.append(
                "NO_MATERIAL_FACT_CANNOT_CLOSE_PRIOR_MATERIAL_"
                f"QUOTE_FAILURE:{document_id}"
            )
        if status == "UNREADABLE":
            pending.append(f"UNREADABLE_FULL_DOCUMENT:{document_id}")
        dispositions.append(
            {
                "schema_version": "e2r_v5_fact_document_disposition_v1",
                "extraction_semantics_version": (
                    extraction_semantics_version
                ),
                "batch_id": batch_id,
                "document_id": document_id,
                "status": status,
                "rationale": rationale,
                "accepted_fact_count": accepted_by_document.get(document_id, 0),
                "source_absence_proven": False,
                "production_score_authority": False,
                **(
                    {
                        "transport_chunk_id": str(
                            document.get("transport_chunk_id")
                        ),
                        "transport_chunk_index": int(
                            document.get("transport_chunk_index") or 0
                        ),
                        "transport_chunk_count": int(
                            document.get("transport_chunk_count") or 1
                        ),
                        "transport_chunk_start": int(
                            document.get("transport_chunk_start") or 0
                        ),
                        "transport_chunk_end": int(
                            document.get("transport_chunk_end") or 0
                        ),
                    }
                    if int(document.get("transport_chunk_count") or 1) > 1
                    else {}
                ),
            }
        )
        disposition_ids.append(document_id)
    expected_ids = set(document_by_id)
    if set(disposition_ids) != expected_ids or len(disposition_ids) != len(expected_ids):
        pending.append("EVERY_DOCUMENT_REQUIRES_EXACTLY_ONE_DISPOSITION")
    unresolved_ids = tuple(str(value).strip() for value in unresolved if str(value).strip())
    if set(unresolved_ids) - expected_ids:
        pending.append("UNRESOLVED_DOCUMENT_ID_OUTSIDE_BATCH")
    if unresolved_ids:
        pending.extend(f"UNRESOLVED_DOCUMENT:{value}" for value in unresolved_ids)
    feedback.extend(
        f"UNRESOLVED_RESEARCH_NOTE:{str(value).strip()}"
        for value in notes
        if str(value).strip()
    )
    batch_document_accounting_complete = (
        set(disposition_ids) == expected_ids
        and len(disposition_ids) == len(expected_ids)
        and not unresolved_ids
    )
    completion_flag_reconciled = (
        response.get("extraction_complete") is not True
        and batch_document_accounting_complete
    )
    if (
        response.get("extraction_complete") is not True
        and not completion_flag_reconciled
    ):
        pending.append("LLM_DECLARED_FACT_EXTRACTION_INCOMPLETE")
    return (
        claims,
        rejections,
        dispositions,
        list(dict.fromkeys(pending)),
        list(dict.fromkeys(feedback)),
        completion_flag_reconciled,
    )


def _literal_quote_whitespace_identity(value: Any) -> str:
    """Identify the same literal quote despite transport/OCR spacing only."""

    return "".join(str(value).split()).casefold()


def _fact_semantic_identity(
    fact: Mapping[str, Any],
) -> str:
    """Identify a duplicate by quote plus normalized economic meaning."""

    return stable_intelligence_id(
        "FACTSEM",
        {
            "document_id": str(fact.get("document_id") or ""),
            "exact_quote": _literal_quote_whitespace_identity(
                fact.get("exact_quote")
            ),
            "question_family_id": str(
                fact.get("question_family_id") or ""
            ),
            "subject_id": str(fact.get("subject_id") or ""),
            "predicate_family": str(
                fact.get("predicate_family") or ""
            ),
            "normalized_object": str(
                fact.get("normalized_object") or ""
            ),
            "period": str(fact.get("period") or ""),
            "direction": str(fact.get("direction") or ""),
            "current_lifecycle": str(
                fact.get("current_lifecycle") or ""
            ),
            "objective_ids": sorted(
                str(value)
                for value in fact.get("objective_ids") or ()
            ),
            "objective_relation": str(
                fact.get("objective_relation") or ""
            ),
        },
    )


def _invalidate_semantically_invalid_provider_response(
    provider: StructuredResearchProvider,
    *,
    reasons: Sequence[str],
) -> None:
    invalidate = getattr(provider, "invalidate_last_response_cache", None)
    if not callable(invalidate):
        return
    try:
        invalidate(
            "FACT_EXTRACTION_SEMANTIC_VALIDATION:"
            + " | ".join(str(reason) for reason in reasons)
        )
    except (OSError, TypeError, ValueError, RuntimeError):
        return


def _fact_extraction_retry_accepted_facts(
    claims: Sequence[Mapping[str, Any]],
) -> list[Mapping[str, str]]:
    return [
        {
            "document_id": str(claim["document_id"]),
            "question_family_id": str(claim["question_family_id"]),
            "subject_id": str(claim["subject_id"]),
            "predicate_family": str(claim["predicate_family"]),
            "normalized_object": str(claim["normalized_object"]),
            "period": str(claim["period"]),
            "direction": str(claim["direction"]),
            "current_lifecycle": str(claim["current_lifecycle"]),
            "exact_quote": str(claim["exact_quote"]),
        }
        for claim in claims
    ]


def _recover_validated_fact_extraction_retry_payload(
    provider: StructuredResearchProvider,
    *,
    primary_payload: Mapping[str, Any],
    previously_accepted_claims: Sequence[Mapping[str, Any]],
) -> Mapping[str, Any] | None:
    recover = getattr(
        provider,
        "validated_fact_extraction_retry_payload",
        None,
    )
    if not callable(recover):
        return None
    try:
        recovered = recover(primary_payload=primary_payload)
    except (OSError, TypeError, ValueError, RuntimeError):
        return None
    if not isinstance(recovered, Mapping):
        return None
    retry_context = recovered.get("fact_extraction_retry_context")
    if not isinstance(retry_context, Mapping):
        return None
    rewrite_attempt = retry_context.get("rewrite_attempt")
    maximum_rewrite_attempts = retry_context.get(
        "maximum_rewrite_attempts"
    )
    validation_errors = retry_context.get("validation_errors")
    if (
        isinstance(rewrite_attempt, bool)
        or rewrite_attempt not in (1, 2)
        or maximum_rewrite_attempts != 2
        or not isinstance(validation_errors, list)
        or not validation_errors
        or any(
            not isinstance(reason, str) or not reason.strip()
            for reason in validation_errors
        )
        or retry_context.get("prior_material_quote_failures") not in (
            [],
            (),
        )
    ):
        return None
    expected_accepted = _fact_extraction_retry_accepted_facts(
        previously_accepted_claims
    )
    recovered_accepted = retry_context.get("previously_accepted_facts")
    if not isinstance(recovered_accepted, list):
        return None
    canonical_recovered = sorted(
        json.dumps(
            dict(row),
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        for row in recovered_accepted
        if isinstance(row, Mapping)
    )
    canonical_expected = sorted(
        json.dumps(
            dict(row),
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        for row in expected_accepted
    )
    if (
        len(canonical_recovered) != len(recovered_accepted)
        or canonical_recovered != canonical_expected
    ):
        return None
    return dict(recovered)


def _recover_validated_fact_extraction_pagination_origin_payload(
    provider: StructuredResearchProvider,
    *,
    primary_payload: Mapping[str, Any],
) -> Mapping[str, Any] | None:
    recover = getattr(
        provider,
        "validated_fact_extraction_pagination_origin_payload",
        None,
    )
    if not callable(recover):
        return None
    try:
        recovered = recover(primary_payload=primary_payload)
    except (OSError, TypeError, ValueError, RuntimeError):
        return None
    if (
        not isinstance(recovered, Mapping)
        or "fact_extraction_continuation_context" in recovered
        or "fact_extraction_retry_context" in recovered
    ):
        return None
    return dict(recovered)


def _fact_continuation_projection(
    claims: Sequence[Mapping[str, Any]],
) -> list[Mapping[str, Any]]:
    return [
        {
            "document_id": str(claim["document_id"]),
            "question_family_id": str(claim["question_family_id"]),
            "subject_id": str(claim["subject_id"]),
            "predicate_family": str(claim["predicate_family"]),
            "normalized_object": str(claim["normalized_object"]),
            "period": str(claim["period"]),
            "direction": str(claim["direction"]),
            "current_lifecycle": str(claim["current_lifecycle"]),
            **(
                {
                    "objective_ids": list(claim["objective_ids"]),
                    "objective_relation": str(claim["objective_relation"]),
                }
                if claim.get("objective_ids")
                else {}
            ),
            "exact_quote": str(claim["exact_quote"]),
        }
        for claim in claims
    ]


def _fact_extraction_continuation_context(
    *,
    page_number: int,
    required_document_ids: Sequence[str] | frozenset[str] | set[str],
    accepted_claims: Sequence[Mapping[str, Any]],
) -> Mapping[str, Any]:
    """Build the exact immutable continuation instruction and prior roster."""

    return {
        "page_number": page_number,
        "page_fact_limit": FACT_EXTRACTION_PAGE_FACT_LIMIT,
        "required_document_ids": sorted(
            str(value) for value in required_document_ids
        ),
        "previously_accepted_facts": _fact_continuation_projection(
            accepted_claims
        ),
        "instruction": (
            "Continue the same supplied batch without repeating any "
            "previously accepted fact or exact quote. Return the next "
            "distinct page of material facts. If more remain after this "
            "page, keep extraction_complete false and list the affected "
            "document ids. If no distinct facts remain, return an empty "
            "facts array, the accurate final disposition (FACTS_EXTRACTED "
            "when prior accepted facts exist), an empty "
            "unresolved_document_ids array, and extraction_complete true."
        ),
    }


def _recover_current_fact_lineage_authority_gap(
    *,
    authoritative_fact_ledger: AuthoritativeResearchEpochFactLedger,
    recovery_binding: CurrentFactLineageRecoveryBinding | None,
    target_id: str,
    target_name: str,
    target_aliases: Sequence[str],
    archetype_id: str,
    as_of_date: str,
    documents: Sequence[Mapping[str, Any]],
    open_objectives: Sequence[Mapping[str, Any]],
    current_facts: Sequence[Mapping[str, Any]],
    score_gap_context: Mapping[str, Any],
    prior_material_claims: Sequence[Mapping[str, Any]],
    prior_document_dispositions: Sequence[Mapping[str, Any]],
    scope_contract: ArchetypeMechanismScopeContract,
    objective_scope_by_document: Mapping[str, frozenset[str]] | None,
    objective_component_by_id: Mapping[str, str],
) -> Mapping[str, Any]:
    """Replay an exact current-fact authority gap without calling a provider."""

    if (
        authoritative_fact_ledger.target_id != target_id
        or authoritative_fact_ledger.as_of_date != as_of_date
    ):
        raise ValueError("current fact authority target/date mismatch")
    prior_compilation = EvidenceFactCompiler().compile(
        target_id=target_id,
        as_of_date=as_of_date,
        accepted_claims=prior_material_claims,
    )
    if prior_compilation.status != "FACT_COMPILATION_COMPLETE":
        return _current_lineage_pending_result(
            "CURRENT_FACT_LINEAGE_PERSISTED_CLAIMS_INVALID",
        )
    persisted_fact_rows = {
        row.fact_id: row.to_dict() for row in prior_compilation.facts
    }
    pending_new_fact_ids = (
        recovery_binding.pending_new_fact_ids
        if recovery_binding is not None
        else ()
    )
    expectation = authoritative_fact_ledger.recovery_expectation(
        persisted_fact_ids=tuple(persisted_fact_rows),
        pending_new_fact_ids=pending_new_fact_ids,
    )
    authority_rows = _exact_fact_rows_by_id(
        authoritative_fact_ledger.fact_rows,
        label="authoritative research-epoch facts",
    )
    current_rows = _exact_fact_rows_by_id(
        current_facts,
        label="current fact authority projection",
    )
    if set(current_rows) != set(authority_rows):
        return _current_lineage_pending_result(
            "CURRENT_FACT_LINEAGE_AUTHORITY_PROJECTION_MISMATCH",
            expectation=expectation,
        )
    for fact_id in set(persisted_fact_rows).intersection(authority_rows):
        if _canonical_json_value(persisted_fact_rows[fact_id]) != (
            _canonical_json_value(current_rows[fact_id])
        ):
            return _current_lineage_pending_result(
                "CURRENT_FACT_LINEAGE_PERSISTED_FACT_BODY_MISMATCH",
                expectation=expectation,
            )
    for fact_id in set(authority_rows) - set(persisted_fact_rows):
        if _canonical_json_value(current_rows[fact_id]) != (
            _canonical_json_value(authority_rows[fact_id])
        ):
            return _current_lineage_pending_result(
                "CURRENT_FACT_LINEAGE_MISSING_FACT_BODY_MISMATCH",
                expectation=expectation,
            )
    expectation_status = str(expectation["status"])
    if expectation_status == "NO_AUTHORITY_LOSS":
        return {
            "status": "NO_AUTHORITY_LOSS",
            "expectation": dict(expectation),
            "provider_complete_call_count": 0,
            "recovered_claim_count": 0,
            "recovered_fact_count": 0,
            "recovered_document_count": 0,
            "objective_reassessment_rows": (),
        }
    if expectation_status != "AUTHORITY_LOSS_RECOVERY_REQUIRED":
        return _current_lineage_pending_result(
            "CURRENT_FACT_LINEAGE_" + expectation_status,
            expectation=expectation,
        )
    if recovery_binding is None:
        return _current_lineage_pending_result(
            "CURRENT_FACT_LINEAGE_RECOVERY_BINDING_REQUIRED",
            expectation=expectation,
        )

    document_by_id = {
        str(row.get("document_id") or ""): dict(row) for row in documents
    }
    seed_source_document_ids = tuple(
        recovery_binding.seed_source_document_ids
    )
    seed_source_document_id_set = frozenset(seed_source_document_ids)
    prior_disposition_ids = {
        str(row.get("document_id") or "")
        for row in prior_document_dispositions
    }
    if (
        not seed_source_document_id_set.issubset(document_by_id)
        or seed_source_document_id_set.intersection(prior_disposition_ids)
    ):
        return _current_lineage_pending_result(
            "CURRENT_FACT_LINEAGE_RECOVERY_DOCUMENT_SCOPE_INVALID",
            expectation=expectation,
        )
    expected_source_ids = frozenset(
        str(value)
        for value in expectation["expected_recovered_source_document_ids"]
    )
    if expected_source_ids != seed_source_document_id_set:
        return _current_lineage_pending_result(
            "CURRENT_FACT_LINEAGE_RECOVERY_SOURCE_COVER_INCOMPLETE",
            expectation=expectation,
        )

    prompt_payload = _fact_extraction_primary_payload(
        target_id=target_id,
        target_name=target_name,
        target_aliases=target_aliases,
        archetype_id=archetype_id,
        as_of_date=as_of_date,
        extraction_semantics_version=FACT_EXTRACTION_SEMANTICS_VERSION,
        open_objectives=open_objectives,
        current_evidence_facts=(
            _project_current_facts_with_accepted_claims(
                current_facts=current_facts,
                accepted_claims=prior_material_claims,
                target_id=target_id,
                as_of_date=as_of_date,
            )
        ),
        score_gap_context=project_fact_extraction_score_gap_context(
            score_gap_context
        ),
        scope_contract=scope_contract,
        batch=tuple(
            document_by_id[document_id]
            for document_id in seed_source_document_ids
        ),
        objective_scope_by_document=objective_scope_by_document,
        objective_component_by_id=objective_component_by_id,
    )
    material_result = validate_current_v5_fact_lineage_materials(
        journal_root=recovery_binding.journal_root,
        target_id=target_id,
        as_of_date=as_of_date,
        archetype_id=archetype_id,
        current_documents=documents,
        current_fact_prompt_payload=prompt_payload,
        recovery_projection_document_ids=seed_source_document_ids,
        fact_extraction_semantics_version=(
            recovery_binding.fact_extraction_semantics_version
        ),
    )
    if material_result.get("status") != (
        "READY_FOR_OFFICIAL_SEMANTIC_REPLAY"
    ):
        return _current_lineage_pending_result(
            "CURRENT_FACT_LINEAGE_JOURNAL_MATERIALS_"
            + str(material_result.get("status") or "INVALID"),
            expectation=expectation,
        )

    material_rows = tuple(
        dict(row) for row in material_result.get("materials") or ()
    )
    material_by_receipt: dict[tuple[str, str], Mapping[str, Any]] = {}
    for material in material_rows:
        pair = (
            str(material.get("request_id") or ""),
            str(material.get("response_id") or ""),
        )
        if pair in material_by_receipt:
            return _current_lineage_pending_result(
                "CURRENT_FACT_LINEAGE_DUPLICATE_JOURNAL_RECEIPT",
                expectation=expectation,
            )
        material_by_receipt[pair] = material
    sealed_pairs = tuple(recovery_binding.journal_receipt_pairs)
    if any(pair not in material_by_receipt for pair in sealed_pairs):
        return _current_lineage_pending_result(
            "CURRENT_FACT_LINEAGE_SEALED_JOURNAL_RECEIPT_MISSING",
            expectation=expectation,
        )
    selected_materials = tuple(
        material_by_receipt[pair] for pair in sealed_pairs
    )
    selected_group_ids = {
        str(row.get("lineage_call_group_id") or "")
        for row in selected_materials
    }
    for group_id in selected_group_ids:
        complete_group_pairs = {
            (
                str(row.get("request_id") or ""),
                str(row.get("response_id") or ""),
            )
            for row in material_rows
            if str(row.get("lineage_call_group_id") or "") == group_id
        }
        if not complete_group_pairs or not complete_group_pairs.issubset(
            sealed_pairs
        ):
            return _current_lineage_pending_result(
                "CURRENT_FACT_LINEAGE_PARTIAL_JOURNAL_CALL_GROUP",
                expectation=expectation,
            )

    grouped: dict[str, list[Mapping[str, Any]]] = {}
    for material in selected_materials:
        group_id = str(material.get("lineage_call_group_id") or "")
        grouped.setdefault(group_id, []).append(material)
    recovery_document_ids = tuple(
        sorted(
            {
                str(document_id)
                for material in selected_materials
                for document_id in (
                    material.get("validated_current_document_ids") or ()
                )
                if str(document_id) not in prior_disposition_ids
            }
        )
    )
    recovery_document_id_set = frozenset(recovery_document_ids)
    if (
        not recovery_document_ids
        or not seed_source_document_id_set.issubset(
            recovery_document_id_set
        )
        or (
            recovery_binding.expected_recovery_document_ids
            and recovery_document_id_set
            != frozenset(
                recovery_binding.expected_recovery_document_ids
            )
        )
    ):
        return _current_lineage_pending_result(
            "CURRENT_FACT_LINEAGE_ATOMIC_DOCUMENT_EXPANSION_INVALID",
            expectation=expectation,
        )
    replayed_groups = []
    try:
        for group_id in sorted(grouped):
            replayed_groups.append(
                _replay_current_fact_lineage_group(
                    group_id=group_id,
                    materials=grouped[group_id],
                    target_id=target_id,
                    as_of_date=as_of_date,
                    scope_contract=scope_contract,
                    provider_name=str(material_result["provider_name"]),
                    recovery_document_ids=recovery_document_id_set,
                )
            )
    except (KeyError, TypeError, ValueError, RuntimeError):
        return _current_lineage_pending_result(
            "CURRENT_FACT_LINEAGE_OFFICIAL_SEMANTIC_REPLAY_INVALID",
            expectation=expectation,
        )
    split_chunk_ids_by_document = (
        _validated_current_lineage_transport_cover(
            replayed_groups=replayed_groups,
            recovery_document_ids=recovery_document_ids,
        )
    )
    if split_chunk_ids_by_document is None:
        return _current_lineage_pending_result(
            "CURRENT_FACT_LINEAGE_UNIQUE_ATOMIC_GROUP_COVER_REQUIRED",
            expectation=expectation,
        )

    recovered_claims = tuple(
        claim
        for row in replayed_groups
        for claim in row["material_claims"]
    )
    raw_recovered_dispositions = tuple(
        disposition
        for row in replayed_groups
        for disposition in row["document_dispositions"]
    )
    (
        reconciled_claims,
        reconciled_dispositions,
        transport_pending,
    ) = _reconcile_transport_chunks(
        claims=recovered_claims,
        dispositions=raw_recovered_dispositions,
        pending=(),
        split_chunk_ids_by_document=split_chunk_ids_by_document,
        pending_transport_chunk_ids=set(),
        target_id=target_id,
        as_of_date=as_of_date,
    )
    if transport_pending or len(reconciled_claims) != len(
        recovered_claims
    ):
        return _current_lineage_pending_result(
            "CURRENT_FACT_LINEAGE_TRANSPORT_RECONCILIATION_INVALID",
            expectation=expectation,
        )
    recovered_claims = tuple(reconciled_claims)
    recovered_dispositions = tuple(reconciled_dispositions)
    if (
        len(recovered_dispositions) != len(recovery_document_ids)
        or {
            str(row.get("document_id") or "")
            for row in recovered_dispositions
        }
        != set(recovery_document_ids)
    ):
        return _current_lineage_pending_result(
            "CURRENT_FACT_LINEAGE_RECOVERED_DISPOSITION_COVER_INVALID",
            expectation=expectation,
        )
    recovered_calls = tuple(
        row["provider_call"] for row in replayed_groups
    )
    recovered_claim_ids = tuple(
        str(row.get("claim_id") or "") for row in recovered_claims
    )
    if (
        any(not value for value in recovered_claim_ids)
        or len(recovered_claim_ids) != len(set(recovered_claim_ids))
        or set(recovered_claim_ids).intersection(
            str(row.get("claim_id") or "")
            for row in prior_material_claims
        )
        or set(recovered_claim_ids)
        != set(expectation["expected_recovered_claim_ids"])
    ):
        return _current_lineage_pending_result(
            "CURRENT_FACT_LINEAGE_RECOVERED_CLAIM_INTERSECTION_INVALID",
            expectation=expectation,
        )
    recovered_compilation = EvidenceFactCompiler().compile(
        target_id=target_id,
        as_of_date=as_of_date,
        accepted_claims=recovered_claims,
    )
    recovered_fact_ids = tuple(
        row.fact_id for row in recovered_compilation.facts
    )
    if (
        recovered_compilation.status != "FACT_COMPILATION_COMPLETE"
        or set(recovered_fact_ids)
        != set(expectation["expected_recovered_fact_ids"])
    ):
        return _current_lineage_pending_result(
            "CURRENT_FACT_LINEAGE_RECOVERED_FACT_INTERSECTION_INVALID",
            expectation=expectation,
        )
    merged_compilation = EvidenceFactCompiler().compile(
        target_id=target_id,
        as_of_date=as_of_date,
        accepted_claims=(*prior_material_claims, *recovered_claims),
    )
    merged_rows = {
        row.fact_id: row.to_dict() for row in merged_compilation.facts
    }
    if (
        merged_compilation.status != "FACT_COMPILATION_COMPLETE"
        or _canonical_json_value(merged_rows)
        != _canonical_json_value(current_rows)
    ):
        return _current_lineage_pending_result(
            "CURRENT_FACT_LINEAGE_MERGED_FACT_ROWS_NOT_AUTHORITATIVE",
            expectation=expectation,
        )
    receipt = authoritative_fact_ledger.exact_recovery_receipt(
        persisted_fact_ids=tuple(persisted_fact_rows),
        recovered_fact_ids=recovered_fact_ids,
        recovered_claim_ids=recovered_claim_ids,
        pending_new_fact_ids=pending_new_fact_ids,
    )
    objective_reassessment_rows = tuple(
        dict(row)
        for row in material_result.get(
            "objective_lineage_reassessment"
        )
        or ()
        if str(row.get("document_id") or "")
        in recovery_document_id_set
    )
    objective_reassessment_document_ids = frozenset(
        str(row["document_id"]) for row in objective_reassessment_rows
    )
    recovered_calls = tuple(
        replace(
            call,
            current_lineage_objective_reassessment_document_ids=tuple(
                sorted(
                    set(call.document_ids)
                    & objective_reassessment_document_ids
                )
            ),
        )
        for call in recovered_calls
    )
    if objective_reassessment_document_ids != frozenset(
        document_id
        for call in recovered_calls
        for document_id in (
            call.current_lineage_objective_reassessment_document_ids
        )
    ):
        return _current_lineage_pending_result(
            "CURRENT_FACT_LINEAGE_OBJECTIVE_REASSESSMENT_RECEIPT_INVALID",
            expectation=expectation,
        )
    return {
        "status": "COMPLETE",
        "expectation": dict(expectation),
        "receipt": dict(receipt),
        "material_claims": recovered_claims,
        "document_dispositions": recovered_dispositions,
        "provider_calls": recovered_calls,
        "seed_source_document_ids": tuple(
            sorted(seed_source_document_ids)
        ),
        "recovery_document_ids": tuple(sorted(recovery_document_ids)),
        "recovered_claim_ids": tuple(sorted(recovered_claim_ids)),
        "recovered_fact_ids": tuple(sorted(recovered_fact_ids)),
        "recovered_claim_count": len(recovered_claims),
        "recovered_fact_count": len(recovered_fact_ids),
        "recovered_document_count": len(recovered_dispositions),
        "journal_request_count": len(selected_materials),
        "journal_call_group_count": len(replayed_groups),
        "provider_complete_call_count": 0,
        "objective_reassessment_rows": objective_reassessment_rows,
        "objective_reassessment_pending_count": len(
            objective_reassessment_rows
        ),
        "atomic_all_or_nothing": True,
    }


def _replay_current_fact_lineage_group(
    *,
    group_id: str,
    materials: Sequence[Mapping[str, Any]],
    target_id: str,
    as_of_date: str,
    scope_contract: ArchetypeMechanismScopeContract,
    provider_name: str,
    recovery_document_ids: frozenset[str],
) -> Mapping[str, Any]:
    """Run one historical base plus every continuation through authority."""

    ordered = tuple(
        sorted(
            (dict(row) for row in materials),
            key=lambda row: int(row.get("continuation_page_number") or 0),
        )
    )
    if not ordered:
        raise ValueError("current fact lineage call group is empty")
    base_payload = dict(ordered[0]["request_payload"])
    if (
        "fact_extraction_continuation_context" in base_payload
        or "fact_extraction_retry_context" in base_payload
        or "fact_extraction_coverage_audit_context" in base_payload
    ):
        raise ValueError("current fact lineage call group lacks a plain base")
    historical_prompt_documents = tuple(
        dict(row) for row in base_payload.get("full_documents") or ()
    )
    historical_documents = tuple(
        _historical_fact_validation_document(row)
        for row in historical_prompt_documents
    )
    original_document_ids = tuple(
        str(row.get("document_id") or "") for row in historical_documents
    )
    if (
        not historical_documents
        or any(not value for value in original_document_ids)
        or len(original_document_ids) != len(set(original_document_ids))
    ):
        raise ValueError("current fact lineage historical batch is invalid")
    projection_document_ids = tuple(
        document_id
        for document_id in original_document_ids
        if document_id in recovery_document_ids
    )
    if not projection_document_ids:
        raise ValueError("current fact lineage group has no recovery projection")
    objective_scope, objective_components = (
        _historical_fact_objective_contract(base_payload)
    )
    historical_transport_chunk_ids = tuple(
        str((row.get("transport_chunk") or {}).get("transport_chunk_id"))
        for row in historical_prompt_documents
        if isinstance(row.get("transport_chunk"), Mapping)
        and str(
            (row.get("transport_chunk") or {}).get("transport_chunk_id")
            or ""
        )
    )
    batch_identity = {
        "target_id": target_id,
        "as_of_date": as_of_date,
        "extraction_semantics_version": FACT_EXTRACTION_SEMANTICS_VERSION,
        "document_ids": list(original_document_ids),
    }
    if historical_transport_chunk_ids:
        batch_identity["transport_chunk_ids"] = list(
            historical_transport_chunk_ids
        )
    batch_id = stable_intelligence_id("FACTBATCH", batch_identity)
    accepted: dict[str, Mapping[str, Any]] = {}
    final_dispositions: list[Mapping[str, Any]] = []
    feedback: list[str] = []
    request_ids: list[str] = []
    response_ids: list[str] = []
    final_prompt_hash = ""
    final_response_hash = ""
    for page_index, material in enumerate(ordered, start=1):
        if int(material.get("continuation_page_number") or 0) != page_index:
            raise ValueError("current fact lineage pages are not contiguous")
        request_payload = dict(material["request_payload"])
        response_payload = dict(material["response_payload"])
        request_core = dict(request_payload)
        continuation = request_core.pop(
            "fact_extraction_continuation_context",
            None,
        )
        if request_core != base_payload:
            raise ValueError("current fact lineage continuation base drifted")
        if page_index == 1:
            if continuation is not None:
                raise ValueError("current fact lineage first page is continuation")
        elif continuation != _fact_extraction_continuation_context(
            page_number=page_index,
            required_document_ids=original_document_ids,
            accepted_claims=tuple(accepted.values()),
        ):
            raise ValueError("current fact lineage continuation context drifted")
        prompt_hash = stable_intelligence_id(
            "FACTPROMPT",
            request_payload,
        )
        (
            _safe_payload,
            _output_schema,
            _transport_prompt,
            transport_prompt_hash,
            transport_schema_hash,
        ) = _single_payload_request_material(
            pass_name="EVIDENCE_FACT_EXTRACTION",
            payload=request_payload,
        )
        if (
            str(material.get("prompt_hash") or "")
            != transport_prompt_hash
            or str(material.get("output_schema_hash") or "")
            != transport_schema_hash
        ):
            raise ValueError("current fact lineage prompt hash drifted")
        response_hash = stable_intelligence_id(
            "FACTRESP",
            scrub_blind_research_payload(response_payload),
        )
        (
            page_claims,
            page_rejections,
            page_dispositions,
            page_pending,
            page_feedback,
            _completion_flag_reconciled,
        ) = _validate_response(
            response_payload,
            batch_id=batch_id,
            documents=historical_documents,
            target_id=target_id,
            as_of_date=as_of_date,
            scope_contract=scope_contract,
            provider_name=provider_name,
            prompt_hash=prompt_hash,
            response_hash=response_hash,
            previously_accepted_claim_counts={
                document_id: sum(
                    str(claim.get("document_id") or "") == document_id
                    for claim in accepted.values()
                )
                for document_id in original_document_ids
            },
            previously_accepted_semantic_identities={
                document_id: tuple(
                    _fact_semantic_identity(claim)
                    for claim in accepted.values()
                    if str(claim.get("document_id") or "") == document_id
                )
                for document_id in original_document_ids
            },
            objective_scope_by_document=objective_scope,
            objective_component_by_id=objective_components,
            extraction_semantics_version=FACT_EXTRACTION_SEMANTICS_VERSION,
        )
        if any(row.material_proposal for row in page_rejections):
            raise ValueError("current fact lineage material proposal rejected")
        for claim in page_claims:
            claim_id = str(claim.get("claim_id") or "")
            if not claim_id or claim_id in accepted:
                raise ValueError("current fact lineage accepted claim duplicated")
            accepted[claim_id] = claim
        feedback.extend(page_feedback)
        request_ids.append(str(material["request_id"]))
        response_ids.append(str(material["response_id"]))
        final_prompt_hash = prompt_hash
        final_response_hash = response_hash
        if page_index < len(ordered):
            if (
                response_payload.get("extraction_complete") is not False
                or not page_pending
                or any(
                    reason != "LLM_DECLARED_FACT_EXTRACTION_INCOMPLETE"
                    and not reason.startswith("UNRESOLVED_DOCUMENT:")
                    for reason in page_pending
                )
            ):
                raise ValueError("current fact lineage continuation did not stay open")
        else:
            if (
                response_payload.get("extraction_complete") is not True
                or page_pending
            ):
                raise ValueError("current fact lineage final page is incomplete")
            final_dispositions = page_dispositions
    if (
        len(final_dispositions) != len(original_document_ids)
        or {
            str(row.get("document_id") or "")
            for row in final_dispositions
        }
        != set(original_document_ids)
    ):
        raise ValueError("current fact lineage final dispositions are incomplete")
    projected_claims = tuple(
        claim
        for claim in accepted.values()
        if str(claim.get("document_id") or "")
        in projection_document_ids
    )
    projected_dispositions = tuple(
        row
        for row in final_dispositions
        if str(row.get("document_id") or "")
        in projection_document_ids
    )
    transport_chunk_ids = tuple(
        str((row.get("transport_chunk") or {}).get("transport_chunk_id"))
        for row in historical_prompt_documents
        if str(row.get("document_id") or "") in projection_document_ids
        and isinstance(row.get("transport_chunk"), Mapping)
        and str(
            (row.get("transport_chunk") or {}).get("transport_chunk_id")
            or ""
        )
    )
    provider_call = FactExtractionProviderCall(
        batch_id=batch_id,
        status="COMPLETE",
        document_ids=projection_document_ids,
        accepted_claim_ids=tuple(
            str(row["claim_id"]) for row in projected_claims
        ),
        rejected_proposal_count=0,
        document_dispositions=projected_dispositions,
        pending_reasons=(),
        research_gap_feedback=tuple(dict.fromkeys(feedback)),
        provider_name=provider_name,
        prompt_hash=final_prompt_hash,
        response_hash=final_response_hash,
        provider_attempt_count=0,
        validation_retry_used=False,
        completion_flag_reconciled=False,
        transport_chunk_ids=transport_chunk_ids,
        accepted_claims=projected_claims,
        coverage_audit_performed=False,
        current_lineage_request_ids=tuple(request_ids),
        current_lineage_response_ids=tuple(response_ids),
        current_lineage_original_batch_document_ids=(
            original_document_ids
        ),
        extraction_semantics_version=FACT_EXTRACTION_SEMANTICS_VERSION,
    )
    return {
        "group_id": group_id,
        "recovery_document_ids": frozenset(projection_document_ids),
        "material_claims": projected_claims,
        "document_dispositions": projected_dispositions,
        "provider_call": provider_call,
        "transport_chunks": tuple(
            {
                "document_id": str(row.get("document_id") or ""),
                "transport_chunk_id": str(
                    (row.get("transport_chunk") or {}).get(
                        "transport_chunk_id"
                    )
                    or ""
                ),
                "chunk_index": int(
                    (row.get("transport_chunk") or {}).get("chunk_index")
                    or 0
                ),
                "chunk_count": int(
                    (row.get("transport_chunk") or {}).get("chunk_count")
                    or 0
                ),
                "full_document_content_hash": str(
                    (row.get("transport_chunk") or {}).get(
                        "full_document_content_hash"
                    )
                    or ""
                ),
            }
            for row in historical_prompt_documents
            if str(row.get("document_id") or "")
            in projection_document_ids
            and isinstance(row.get("transport_chunk"), Mapping)
        ),
    }


def _historical_fact_validation_document(
    prompt_document: Mapping[str, Any],
) -> Mapping[str, Any]:
    """Rebuild the extractor's internal chunk row from its prompt projection."""

    row = dict(prompt_document)
    transport = row.get("transport_chunk")
    if transport is None:
        return row
    if not isinstance(transport, Mapping):
        raise ValueError("historical fact transport chunk is invalid")
    return {
        **row,
        "transport_chunk_id": str(transport["transport_chunk_id"]),
        "transport_chunk_index": int(transport["chunk_index"]),
        "transport_chunk_count": int(transport["chunk_count"]),
        "transport_chunk_start": int(transport["start_char"]),
        "transport_chunk_end": int(transport["end_char"]),
        "transport_chunk_content_hash": str(
            transport["chunk_content_hash"]
        ),
        "content_hash": str(transport["full_document_content_hash"]),
        "full_document_text_chars": int(
            transport["full_document_text_chars"]
        ),
    }


def _historical_fact_objective_contract(
    request_payload: Mapping[str, Any],
) -> tuple[Mapping[str, frozenset[str]] | None, Mapping[str, str] | None]:
    scope = request_payload.get("fact_extraction_scope_contract")
    if scope is None:
        return None, None
    if not isinstance(scope, Mapping):
        raise ValueError("historical fact objective scope is invalid")
    document_rows = scope.get("document_objective_ids")
    component_rows = scope.get("objective_component_rows")
    if not isinstance(document_rows, list) or not isinstance(
        component_rows,
        list,
    ):
        raise ValueError("historical fact objective rows are invalid")
    objective_scope: dict[str, frozenset[str]] = {}
    for row in document_rows:
        if not isinstance(row, Mapping):
            raise ValueError("historical document objective row is invalid")
        document_id = str(row.get("document_id") or "")
        objective_ids = frozenset(
            str(value) for value in row.get("objective_ids") or ()
        )
        if (
            not document_id
            or not objective_ids
            or document_id in objective_scope
        ):
            raise ValueError("historical document objective row is incomplete")
        objective_scope[document_id] = objective_ids
    objective_components: dict[str, str] = {}
    for row in component_rows:
        if not isinstance(row, Mapping):
            raise ValueError("historical objective component row is invalid")
        objective_id = str(row.get("objective_id") or "")
        component_id = str(row.get("component_id") or "")
        if (
            not objective_id
            or component_id not in CANONICAL_COMPONENT_ORDER
            or objective_id in objective_components
        ):
            raise ValueError("historical objective component row is incomplete")
        objective_components[objective_id] = component_id
    if set(objective_components) != {
        objective_id
        for objective_ids in objective_scope.values()
        for objective_id in objective_ids
    }:
        raise ValueError("historical objective/component cover is not exact")
    return objective_scope, objective_components


def _validated_current_lineage_transport_cover(
    *,
    replayed_groups: Sequence[Mapping[str, Any]],
    recovery_document_ids: Sequence[str],
) -> Mapping[str, tuple[str, ...]] | None:
    """Validate one non-split unit or every exact chunk for each document."""

    split_chunks_by_document: dict[str, list[Mapping[str, Any]]] = {}
    for group in replayed_groups:
        for raw in group.get("transport_chunks") or ():
            if not isinstance(raw, Mapping):
                return None
            document_id = str(raw.get("document_id") or "")
            if document_id:
                split_chunks_by_document.setdefault(document_id, []).append(
                    dict(raw)
                )
    result: dict[str, tuple[str, ...]] = {}
    for document_id in recovery_document_ids:
        group_occurrence_count = sum(
            document_id in group["recovery_document_ids"]
            for group in replayed_groups
        )
        chunks = split_chunks_by_document.get(document_id, [])
        if not chunks:
            if group_occurrence_count != 1:
                return None
            continue
        chunk_count_values = {
            int(row.get("chunk_count") or 0) for row in chunks
        }
        full_hash_values = {
            str(row.get("full_document_content_hash") or "")
            for row in chunks
        }
        chunk_ids = tuple(
            str(row.get("transport_chunk_id") or "") for row in chunks
        )
        chunk_indices = tuple(int(row.get("chunk_index") or 0) for row in chunks)
        if (
            len(chunk_count_values) != 1
            or len(full_hash_values) != 1
            or "" in full_hash_values
            or not chunk_ids
            or any(not value for value in chunk_ids)
            or len(chunk_ids) != len(set(chunk_ids))
            or len(chunk_indices) != len(set(chunk_indices))
        ):
            return None
        chunk_count = next(iter(chunk_count_values))
        if (
            chunk_count <= 1
            or len(chunks) != chunk_count
            or set(chunk_indices) != set(range(chunk_count))
            or group_occurrence_count != chunk_count
        ):
            return None
        result[document_id] = tuple(
            str(row["transport_chunk_id"])
            for row in sorted(
                chunks,
                key=lambda row: int(row["chunk_index"]),
            )
        )
    if set(split_chunks_by_document) - set(recovery_document_ids):
        return None
    return result


def _validated_raw_current_lineage_transport_cover(
    *,
    material_rows: Sequence[Mapping[str, Any]],
    document_ids: Sequence[str],
) -> Mapping[str, tuple[str, ...]] | None:
    """Validate structural full/chunk units before official semantic replay."""

    base_by_group: dict[str, Mapping[str, Any]] = {}
    for row in material_rows:
        group_id = str(row.get("lineage_call_group_id") or "")
        if int(row.get("continuation_page_number") or 0) == 1:
            if not group_id or group_id in base_by_group:
                return None
            base_by_group[group_id] = row
    target_ids = frozenset(str(value) for value in document_ids)
    units_by_document: dict[str, list[Mapping[str, Any] | None]] = {
        document_id: [] for document_id in target_ids
    }
    for material in base_by_group.values():
        request_payload = material.get("request_payload")
        if not isinstance(request_payload, Mapping):
            return None
        for raw in request_payload.get("full_documents") or ():
            if not isinstance(raw, Mapping):
                return None
            document_id = str(raw.get("document_id") or "")
            if document_id not in target_ids:
                continue
            transport = raw.get("transport_chunk")
            if transport is not None and not isinstance(transport, Mapping):
                return None
            units_by_document[document_id].append(
                dict(transport) if isinstance(transport, Mapping) else None
            )
    result: dict[str, tuple[str, ...]] = {}
    for document_id, units in units_by_document.items():
        if not units:
            return None
        if all(unit is None for unit in units):
            if len(units) != 1:
                return None
            continue
        if any(unit is None for unit in units):
            return None
        chunks = [dict(unit) for unit in units if unit is not None]
        chunk_ids = tuple(
            str(row.get("transport_chunk_id") or "") for row in chunks
        )
        counts = {int(row.get("chunk_count") or 0) for row in chunks}
        indices = tuple(int(row.get("chunk_index") or 0) for row in chunks)
        full_hashes = {
            str(row.get("full_document_content_hash") or "")
            for row in chunks
        }
        if (
            len(counts) != 1
            or len(full_hashes) != 1
            or "" in full_hashes
            or any(not value for value in chunk_ids)
            or len(chunk_ids) != len(set(chunk_ids))
            or len(indices) != len(set(indices))
        ):
            return None
        count = next(iter(counts))
        if count <= 1 or len(chunks) != count or set(indices) != set(range(count)):
            return None
        result[document_id] = tuple(
            str(row["transport_chunk_id"])
            for row in sorted(chunks, key=lambda row: int(row["chunk_index"]))
        )
    return result


def _select_unique_raw_current_lineage_transport_cover(
    *,
    material_rows: Sequence[Mapping[str, Any]],
    document_ids: Sequence[str],
) -> tuple[Mapping[str, Any], ...] | None:
    """Select the sole structurally exact journal-call cover, if one exists.

    A later valid call may overlap only part of an older atomic call.  Such a
    redundant call must not make the older, complete cover ambiguous.  At the
    same time, two independently complete covers remain ambiguous and fail
    closed.  Split documents are covered only by one complete, hash-consistent
    chunk set.
    """

    target_ids = tuple(sorted({str(value) for value in document_ids}))
    if (
        not target_ids
        or len(target_ids) != len(tuple(document_ids))
        or any(not value for value in target_ids)
    ):
        return None

    rows_by_group: dict[str, list[Mapping[str, Any]]] = {}
    base_by_group: dict[str, Mapping[str, Any]] = {}
    for row in material_rows:
        group_id = str(row.get("lineage_call_group_id") or "")
        if not group_id:
            return None
        rows_by_group.setdefault(group_id, []).append(row)
        if int(row.get("continuation_page_number") or 0) == 1:
            if group_id in base_by_group:
                return None
            base_by_group[group_id] = row
    if set(rows_by_group) != set(base_by_group):
        return None

    units_by_document: dict[
        str, dict[str, Mapping[str, Any] | None]
    ] = {document_id: {} for document_id in target_ids}
    for group_id, material in base_by_group.items():
        request_payload = material.get("request_payload")
        if not isinstance(request_payload, Mapping):
            return None
        for raw in request_payload.get("full_documents") or ():
            if not isinstance(raw, Mapping):
                return None
            document_id = str(raw.get("document_id") or "")
            if document_id not in units_by_document:
                continue
            if group_id in units_by_document[document_id]:
                return None
            transport = raw.get("transport_chunk")
            if transport is not None and not isinstance(transport, Mapping):
                return None
            units_by_document[document_id][group_id] = (
                dict(transport) if isinstance(transport, Mapping) else None
            )

    options_by_document: dict[str, tuple[frozenset[str], ...]] = {}
    touching_by_document: dict[str, frozenset[str]] = {}
    for document_id, units_by_group in units_by_document.items():
        if not units_by_group:
            return None
        touching_by_document[document_id] = frozenset(units_by_group)
        options: set[frozenset[str]] = {
            frozenset((group_id,))
            for group_id, unit in units_by_group.items()
            if unit is None
        }
        chunks_by_identity: dict[
            tuple[int, str], dict[int, list[str]]
        ] = {}
        for group_id, unit in units_by_group.items():
            if unit is None:
                continue
            count = int(unit.get("chunk_count") or 0)
            index = int(unit.get("chunk_index") or 0)
            full_hash = str(unit.get("full_document_content_hash") or "")
            chunk_id = str(unit.get("transport_chunk_id") or "")
            if (
                count <= 1
                or index < 0
                or index >= count
                or not full_hash
                or not chunk_id
            ):
                return None
            chunks_by_identity.setdefault((count, full_hash), {}).setdefault(
                index, []
            ).append(group_id)
        for (count, _full_hash), groups_by_index in chunks_by_identity.items():
            if set(groups_by_index) != set(range(count)):
                continue

            def add_chunk_options(
                index: int,
                selected: frozenset[str],
            ) -> None:
                if index == count:
                    options.add(selected)
                    return
                for group_id in sorted(groups_by_index[index]):
                    if group_id not in selected:
                        add_chunk_options(index + 1, selected | {group_id})

            add_chunk_options(0, frozenset())
        if not options:
            return None
        options_by_document[document_id] = tuple(
            sorted(options, key=lambda value: (len(value), tuple(sorted(value))))
        )

    solutions: set[frozenset[str]] = set()
    visited: set[tuple[tuple[str, ...], frozenset[str], frozenset[str]]] = set()

    def search(
        remaining: tuple[str, ...],
        selected: frozenset[str],
        forbidden: frozenset[str],
    ) -> None:
        if len(solutions) > 1:
            return
        state = (remaining, selected, forbidden)
        if state in visited:
            return
        visited.add(state)
        if not remaining:
            chosen_rows = tuple(
                row
                for row in material_rows
                if str(row.get("lineage_call_group_id") or "") in selected
            )
            if _validated_raw_current_lineage_transport_cover(
                material_rows=chosen_rows,
                document_ids=target_ids,
            ) is not None:
                solutions.add(selected)
            return

        compatible_by_document: dict[str, tuple[frozenset[str], ...]] = {}
        for document_id in remaining:
            touching = touching_by_document[document_id]
            already_selected = selected.intersection(touching)
            compatible = tuple(
                option
                for option in options_by_document[document_id]
                if already_selected.issubset(option)
                and not option.intersection(forbidden)
            )
            if not compatible:
                return
            compatible_by_document[document_id] = compatible
        document_id = min(
            remaining,
            key=lambda value: (len(compatible_by_document[value]), value),
        )
        touching = touching_by_document[document_id]
        next_remaining = tuple(
            value for value in remaining if value != document_id
        )
        for option in compatible_by_document[document_id]:
            next_selected = selected.union(option)
            next_forbidden = forbidden.union(touching - option)
            if next_selected.intersection(next_forbidden):
                continue
            search(next_remaining, next_selected, next_forbidden)

    search(target_ids, frozenset(), frozenset())
    if len(solutions) != 1:
        return None
    selected_group_ids = next(iter(solutions))
    return tuple(
        row
        for row in material_rows
        if str(row.get("lineage_call_group_id") or "")
        in selected_group_ids
    )


def _exact_fact_rows_by_id(
    rows: Sequence[Mapping[str, Any]],
    *,
    label: str,
) -> Mapping[str, Mapping[str, Any]]:
    result: dict[str, Mapping[str, Any]] = {}
    for raw in rows:
        value = raw.to_dict() if hasattr(raw, "to_dict") else dict(raw)
        fact_id = str(value.get("fact_id") or "")
        if not fact_id or fact_id in result:
            raise ValueError(f"{label} require unique fact ids")
        result[fact_id] = _canonical_json_value(value)
    return result


def _canonical_json_value(value: Any) -> Any:
    return json.loads(
        json.dumps(
            value,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        )
    )


def _current_lineage_pending_result(
    reason: str,
    *,
    expectation: Mapping[str, Any] | None = None,
) -> Mapping[str, Any]:
    return {
        "status": "PENDING",
        "pending_reason": reason,
        "expectation": dict(expectation or {}),
        "provider_complete_call_count": 0,
        "recovered_claim_count": 0,
        "recovered_fact_count": 0,
        "recovered_document_count": 0,
        "objective_reassessment_rows": (),
        "atomic_all_or_nothing": True,
    }


def _recover_v4_fact_semantics_checkpoint(
    provider: StructuredResearchProvider,
    *,
    target_id: str,
    target_name: str,
    target_aliases: Sequence[str],
    archetype_id: str,
    as_of_date: str,
    documents: Sequence[Mapping[str, Any]],
    source_boundary_context_by_document_id: Mapping[
        str, Mapping[str, Any]
    ],
    max_document_chars_per_call: int,
    open_objectives: Sequence[Mapping[str, Any]],
    scope_contract: ArchetypeMechanismScopeContract,
    objective_scope_by_document: Mapping[str, frozenset[str]] | None,
    objective_component_by_id: Mapping[str, str],
    recovery_document_ids: Sequence[str],
    expected_invalidated_claim_count: int,
    prior_material_claims: Sequence[Mapping[str, Any]],
    prior_document_dispositions: Sequence[Mapping[str, Any]],
    prior_provider_calls: Sequence[
        FactExtractionProviderCall | Mapping[str, Any]
    ],
) -> Mapping[str, Any] | None:
    """Atomically rebuild one lost v4 checkpoint from official receipts."""

    recovery_ids = tuple(dict.fromkeys(str(value) for value in recovery_document_ids))
    recovery_id_set = frozenset(recovery_ids)
    document_by_id = {
        str(row.get("document_id") or ""): row for row in documents
    }
    if (
        not recovery_ids
        or len(recovery_ids) != len(tuple(recovery_document_ids))
        or expected_invalidated_claim_count <= 0
        or not recovery_id_set.issubset(document_by_id)
        or objective_scope_by_document is None
        or any(
            _fact_semantics_upgrade_requires_reextraction(
                previous_version=(
                    _PRE_STRUCTURED_VALUATION_ROLE_SEMANTICS_VERSION
                ),
                document=document_by_id[document_id],
            )
            for document_id in recovery_ids
        )
    ):
        return None
    prior_disposition_ids = {
        str(row.get("document_id") or "")
        for row in prior_document_dispositions
    }
    prior_claim_document_ids = {
        str(row.get("document_id") or "") for row in prior_material_claims
    }
    prior_call_document_ids = {
        str(document_id)
        for raw_call in prior_provider_calls
        for document_id in (
            raw_call.document_ids
            if isinstance(raw_call, FactExtractionProviderCall)
            else tuple(raw_call.get("document_ids") or ())
        )
    }
    if recovery_id_set & (
        prior_disposition_ids
        | prior_claim_document_ids
        | prior_call_document_ids
    ):
        return None
    transport_by_document_id: dict[str, Mapping[str, Any]] = {}
    for document_id in recovery_ids:
        transport_rows = _document_transport_chunks(
            document_by_id[document_id],
            max_chars=max_document_chars_per_call,
            source_boundary_context=(
                source_boundary_context_by_document_id.get(document_id)
            ),
        )
        if len(transport_rows) != 1:
            return None
        transport_by_document_id[document_id] = transport_rows[0]
    recover = getattr(
        provider,
        "validated_fact_extraction_semantics_migration_materials",
        None,
    )
    if not callable(recover):
        return None
    try:
        recovered = recover(
            target_id=target_id,
            as_of_date=as_of_date,
            archetype_id=archetype_id,
            document_ids=recovery_ids,
        )
    except (OSError, TypeError, ValueError, RuntimeError):
        return None
    if (
        not isinstance(recovered, Mapping)
        or recovered.get("prior_semantics_version")
        != _PRE_STRUCTURED_VALUATION_ROLE_SEMANTICS_VERSION
        or recovered.get("current_semantics_version")
        != FACT_EXTRACTION_SEMANTICS_VERSION
        or recovered.get("target_id") != target_id
        or recovered.get("as_of_date") != as_of_date
        or recovered.get("archetype_id") != archetype_id
        or tuple(recovered.get("document_ids") or ()) != recovery_ids
        or recovered.get("provider_name")
        != "COLLABORATION_CODEX_SUBAGENT_STRUCTURED_RESEARCHER_MODE"
    ):
        return None
    raw_materials = recovered.get("materials")
    recovery_material_status = recovered.get(
        "recovery_material_status"
    )
    if recovery_material_status == "ABSENT" and raw_materials == []:
        return {"status": "ABSENT"}
    if recovery_material_status != "COMPLETE":
        return None
    if (
        isinstance(raw_materials, (str, bytes))
        or not isinstance(raw_materials, Sequence)
        or not raw_materials
        or any(not isinstance(row, Mapping) for row in raw_materials)
    ):
        return None
    request_ids = tuple(
        str(row.get("request_id") or "") for row in raw_materials
    )
    response_ids = tuple(
        str(row.get("response_id") or "") for row in raw_materials
    )
    if (
        any(re.fullmatch(r"COLLABREQ-[0-9a-f]{64}", value) is None for value in request_ids)
        or any(re.fullmatch(r"COLLABRESP-[0-9a-f]{64}", value) is None for value in response_ids)
        or len(request_ids) != len(set(request_ids))
        or len(response_ids) != len(set(response_ids))
    ):
        return None

    base_by_roster: dict[tuple[str, ...], Mapping[str, Any]] = {}
    continuations_by_roster: dict[
        tuple[str, ...], list[tuple[int, Mapping[str, Any]]]
    ] = {}
    for material in raw_materials:
        request_payload = material.get("request_payload")
        response_payload = material.get("response_payload")
        provenance = material.get("provenance")
        if (
            not isinstance(request_payload, Mapping)
            or not isinstance(response_payload, Mapping)
            or not isinstance(provenance, Mapping)
            or provenance.get("agent_model") != "codex-collaboration"
            or request_payload.get("fact_extraction_semantics_version")
            != _PRE_STRUCTURED_VALUATION_ROLE_SEMANTICS_VERSION
            or request_payload.get("target_id") != target_id
            or request_payload.get("target_name") != target_name
            or tuple(request_payload.get("target_aliases") or ())
            != tuple(target_aliases)
            or request_payload.get("archetype_hypothesis") != archetype_id
            or request_payload.get("as_of_date") != as_of_date
            or "fact_extraction_retry_context" in request_payload
        ):
            return None
        request_base_payload = dict(request_payload)
        continuation = request_base_payload.pop(
            "fact_extraction_continuation_context", None
        )
        runtime_evidence_context = request_base_payload.get(
            "current_evidence_facts"
        )
        runtime_score_gap_context = request_base_payload.get(
            "score_gap_context"
        )
        if (
            not isinstance(runtime_evidence_context, Mapping)
            or not isinstance(runtime_score_gap_context, Mapping)
        ):
            return None
        full_documents = request_payload.get("full_documents")
        if (
            not isinstance(full_documents, list)
            or not full_documents
            or any(not isinstance(row, Mapping) for row in full_documents)
        ):
            return None
        batch_document_ids = tuple(
            str(row.get("document_id") or "") for row in full_documents
        )
        if (
            any(not value for value in batch_document_ids)
            or len(batch_document_ids) != len(set(batch_document_ids))
            or not set(batch_document_ids).issubset(recovery_id_set)
            or full_documents
            != [
                _document_prompt_row(
                    transport_by_document_id[document_id],
                    source_boundary_context=(
                        transport_by_document_id[document_id].get(
                            "_source_boundary_context"
                        )
                    ),
                )
                for document_id in batch_document_ids
            ]
        ):
            return None
        expected_base_payload = _fact_extraction_primary_payload(
            target_id=target_id,
            target_name=target_name,
            target_aliases=target_aliases,
            archetype_id=archetype_id,
            as_of_date=as_of_date,
            extraction_semantics_version=(
                _PRE_STRUCTURED_VALUATION_ROLE_SEMANTICS_VERSION
            ),
            open_objectives=open_objectives,
            current_evidence_facts=runtime_evidence_context,
            score_gap_context=runtime_score_gap_context,
            scope_contract=scope_contract,
            batch=[
                transport_by_document_id[document_id]
                for document_id in batch_document_ids
            ],
            objective_scope_by_document=objective_scope_by_document,
            objective_component_by_id=objective_component_by_id,
        )
        if request_base_payload != expected_base_payload:
            return None
        if continuation is None:
            if batch_document_ids in base_by_roster:
                return None
            base_by_roster[batch_document_ids] = material
            continue
        if not isinstance(continuation, Mapping):
            return None
        page_number = continuation.get("page_number")
        if (
            isinstance(page_number, bool)
            or not isinstance(page_number, int)
            or page_number < 2
        ):
            return None
        continuations_by_roster.setdefault(batch_document_ids, []).append(
            (page_number, material)
        )

    recovered_document_ids: set[str] = set()
    recovered_claims: list[Mapping[str, Any]] = []
    recovered_dispositions: list[Mapping[str, Any]] = []
    recovered_calls: list[FactExtractionProviderCall] = []
    for batch_document_ids, base_material in base_by_roster.items():
        if recovered_document_ids & set(batch_document_ids):
            return None
        page_materials = [(1, base_material), *sorted(
            continuations_by_roster.pop(batch_document_ids, []),
            key=lambda row: row[0],
        )]
        if [row[0] for row in page_materials] != list(
            range(1, len(page_materials) + 1)
        ):
            return None
        base_payload = dict(base_material["request_payload"])
        batch_documents = [
            transport_by_document_id[document_id]
            for document_id in batch_document_ids
        ]
        batch_id = stable_intelligence_id(
            "FACTBATCH",
            {
                "target_id": target_id,
                "as_of_date": as_of_date,
                "extraction_semantics_version": (
                    _PRE_STRUCTURED_VALUATION_ROLE_SEMANTICS_VERSION
                ),
                "document_ids": list(batch_document_ids),
            },
        )
        accepted: dict[str, Mapping[str, Any]] = {}
        feedback: list[str] = []
        receipt_request_ids: list[str] = []
        receipt_response_ids: list[str] = []
        final_dispositions: list[Mapping[str, Any]] = []
        final_prompt_hash = ""
        final_response_hash = ""
        for page_index, material in page_materials:
            request_payload = dict(material["request_payload"])
            response_payload = dict(material["response_payload"])
            if page_index > 1:
                continuation = request_payload.get(
                    "fact_extraction_continuation_context"
                )
                continuation_base = dict(request_payload)
                continuation_base.pop(
                    "fact_extraction_continuation_context", None
                )
                if (
                    not isinstance(continuation, Mapping)
                    or continuation_base != base_payload
                    or continuation
                    != _fact_extraction_continuation_context(
                        page_number=page_index,
                        required_document_ids=batch_document_ids,
                        accepted_claims=tuple(accepted.values()),
                    )
                ):
                    return None
            prompt_hash = stable_intelligence_id(
                "FACTPROMPT", request_payload
            )
            response_hash = stable_intelligence_id(
                "FACTRESP",
                scrub_blind_research_payload(response_payload),
            )
            (
                page_claims,
                page_rejections,
                page_dispositions,
                page_pending,
                page_feedback,
                _completion_flag_reconciled,
            ) = _validate_response(
                response_payload,
                batch_id=batch_id,
                documents=batch_documents,
                target_id=target_id,
                as_of_date=as_of_date,
                scope_contract=scope_contract,
                provider_name=str(
                    recovered["provider_name"]
                ),
                prompt_hash=prompt_hash,
                response_hash=response_hash,
                previously_accepted_claim_counts={
                    document_id: sum(
                        1
                        for claim in accepted.values()
                        if str(claim.get("document_id") or "")
                        == document_id
                    )
                    for document_id in batch_document_ids
                },
                previously_accepted_semantic_identities={
                    document_id: tuple(
                        _fact_semantic_identity(claim)
                        for claim in accepted.values()
                        if str(claim.get("document_id") or "")
                        == document_id
                    )
                    for document_id in batch_document_ids
                },
                objective_scope_by_document=objective_scope_by_document,
                objective_component_by_id=objective_component_by_id,
                extraction_semantics_version=(
                    _PRE_STRUCTURED_VALUATION_ROLE_SEMANTICS_VERSION
                ),
            )
            if page_rejections:
                return None
            for claim in page_claims:
                claim_id = str(claim["claim_id"])
                if claim_id in accepted:
                    return None
                accepted[claim_id] = claim
            feedback.extend(page_feedback)
            receipt_request_ids.append(str(material["request_id"]))
            receipt_response_ids.append(str(material["response_id"]))
            final_prompt_hash = prompt_hash
            final_response_hash = response_hash
            if page_index < len(page_materials):
                allowed_pending = all(
                    reason == "LLM_DECLARED_FACT_EXTRACTION_INCOMPLETE"
                    or reason.startswith("UNRESOLVED_DOCUMENT:")
                    for reason in page_pending
                )
                if (
                    response_payload.get("extraction_complete") is not False
                    or not page_pending
                    or not allowed_pending
                ):
                    return None
            else:
                if (
                    response_payload.get("extraction_complete") is not True
                    or page_pending
                ):
                    return None
                final_dispositions = page_dispositions
        if (
            {str(row.get("document_id") or "") for row in final_dispositions}
            != set(batch_document_ids)
            or len(final_dispositions) != len(batch_document_ids)
        ):
            return None
        recovered_document_ids.update(batch_document_ids)
        recovered_claims.extend(accepted.values())
        recovered_dispositions.extend(final_dispositions)
        recovered_calls.append(
            FactExtractionProviderCall(
                batch_id=batch_id,
                status="COMPLETE",
                document_ids=batch_document_ids,
                accepted_claim_ids=tuple(accepted),
                rejected_proposal_count=0,
                document_dispositions=tuple(final_dispositions),
                pending_reasons=(),
                research_gap_feedback=tuple(dict.fromkeys(feedback)),
                provider_name=str(
                    recovered["provider_name"]
                ),
                prompt_hash=final_prompt_hash,
                response_hash=final_response_hash,
                provider_attempt_count=len(page_materials),
                validation_retry_used=False,
                coverage_audit_performed=False,
                semantics_migration_request_ids=tuple(receipt_request_ids),
                semantics_migration_response_ids=tuple(receipt_response_ids),
                extraction_semantics_version=(
                    _PRE_STRUCTURED_VALUATION_ROLE_SEMANTICS_VERSION
                ),
            )
        )
    if continuations_by_roster:
        return None
    recovered_claim_ids = tuple(
        str(row.get("claim_id") or "") for row in recovered_claims
    )
    recovered_disposition_ids = tuple(
        str(row.get("document_id") or "")
        for row in recovered_dispositions
    )
    if (
        recovered_document_ids != set(recovery_ids)
        or len(recovered_claims) != expected_invalidated_claim_count
        or any(not value for value in recovered_claim_ids)
        or len(recovered_claim_ids) != len(set(recovered_claim_ids))
        or len(recovered_disposition_ids) != len(set(recovered_disposition_ids))
        or set(recovered_disposition_ids) != set(recovery_ids)
        or any(
            _fact_semantics_upgrade_requires_reextraction(
                previous_version=call.extraction_semantics_version,
                document=document_by_id[document_id],
            )
            for call in recovered_calls
            for document_id in call.document_ids
        )
    ):
        return None
    return {
        "status": "COMPLETE",
        "material_claims": tuple(recovered_claims),
        "document_dispositions": tuple(recovered_dispositions),
        "provider_calls": tuple(recovered_calls),
        "rejections": (),
        "request_count": len(raw_materials),
        "response_count": len(raw_materials),
        "claim_count": len(recovered_claims),
        "document_count": len(recovered_dispositions),
        "call_count": len(recovered_calls),
    }


def _proposal_rejection_reason(
    proposal: Any,
    *,
    document_by_id: Mapping[str, Mapping[str, Any]],
    target_id: str,
    scope_contract: ArchetypeMechanismScopeContract,
) -> str | None:
    if not isinstance(proposal, Mapping):
        return "FACT_PROPOSAL_NOT_OBJECT"
    document_id = str(proposal.get("document_id") or "")
    if document_id not in document_by_id:
        return "UNKNOWN_DOCUMENT_ID"
    required = (
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
        "economic_mechanism",
        "mechanism_scope_id",
        "predicate",
        "predicate_family",
        "value",
        "normalized_object",
        "period",
        "exact_quote",
        "materiality_rationale",
    )
    missing = [
        key
        for key in required
        if (
            key == "value"
            and (
                proposal.get(key) is None
                or (
                    isinstance(proposal.get(key), str)
                    and not str(proposal.get(key)).strip()
                )
                or (
                    isinstance(proposal.get(key), (Mapping, list, tuple))
                    and not proposal.get(key)
                )
            )
        )
        or (
            key != "value"
            and not str(proposal.get(key) or "").strip()
        )
    ]
    if missing:
        return "EXPLICIT_FACT_FIELDS_MISSING:" + ",".join(missing)
    try:
        EvidenceDirection(str(proposal.get("direction") or ""))
        EvidenceLifecycle(str(proposal.get("current_lifecycle") or ""))
        confidence = float(proposal.get("confidence"))
        if not math.isfinite(confidence) or not 0 <= confidence <= 1:
            raise ValueError("confidence")
        proposal_value = proposal.get("value")
        if isinstance(proposal_value, bool) or (
            isinstance(proposal_value, float)
            and not math.isfinite(proposal_value)
        ):
            raise ValueError("value")
    except (TypeError, ValueError):
        return "INVALID_FACT_ENUM_OR_CONFIDENCE"
    if str(proposal.get("materiality") or "") not in {"CRITICAL", "NONCRITICAL"}:
        return "INVALID_MATERIALITY"
    allowed_component_ids, scope_reasons = _allowed_components(
        proposal,
        target_id=target_id,
        scope_contract=scope_contract,
    )
    if not allowed_component_ids:
        return "MECHANISM_SCOPE_REJECTED:" + ",".join(scope_reasons)
    quote = str(proposal.get("exact_quote") or "").strip()
    if quote not in str(document_by_id[document_id].get("content_text") or ""):
        return "EXACT_QUOTE_NOT_IN_FULL_DOCUMENT"
    return None


def _objective_scope_rejection_reason(
    proposal: Any,
    *,
    objective_scope_by_document: Mapping[str, frozenset[str]] | None,
    objective_component_by_id: Mapping[str, str] | None,
    target_id: str,
    scope_contract: ArchetypeMechanismScopeContract,
) -> str | None:
    if objective_scope_by_document is None:
        return None
    if not isinstance(proposal, Mapping):
        return "FACT_PROPOSAL_NOT_OBJECT"
    document_id = str(proposal.get("document_id") or "")
    allowed_objective_ids = objective_scope_by_document.get(document_id)
    if allowed_objective_ids is None:
        return "UNKNOWN_DOCUMENT_ID"
    raw_objective_ids = proposal.get("objective_ids")
    if isinstance(raw_objective_ids, (str, bytes)) or not isinstance(
        raw_objective_ids, Sequence
    ):
        return "OBJECTIVE_IDS_MISSING_OR_MALFORMED"
    cited_objective_ids = tuple(
        str(value).strip() for value in raw_objective_ids
    )
    if (
        not cited_objective_ids
        or any(not value for value in cited_objective_ids)
        or len(cited_objective_ids) != len(set(cited_objective_ids))
    ):
        return "OBJECTIVE_IDS_MISSING_OR_DUPLICATED"
    if set(cited_objective_ids) - set(allowed_objective_ids):
        return "OBJECTIVE_ID_OUTSIDE_DOCUMENT_LINEAGE"
    if (
        str(proposal.get("objective_relation") or "")
        not in OBJECTIVE_FACT_RELATIONS
    ):
        return "INVALID_OBJECTIVE_FACT_RELATION"
    allowed_component_ids, _ = _allowed_components(
        proposal,
        target_id=target_id,
        scope_contract=scope_contract,
    )
    if allowed_component_ids and objective_component_by_id is not None:
        cited_objective_component_ids = {
            str(objective_component_by_id.get(objective_id) or "")
            for objective_id in cited_objective_ids
        }
        if (
            "" in cited_objective_component_ids
            or cited_objective_component_ids - set(allowed_component_ids)
        ):
            return "OBJECTIVE_COMPONENT_OUTSIDE_MECHANISM_SCOPE"
    return None


def _accepted_claim(
    proposal: Mapping[str, Any],
    *,
    document: Mapping[str, Any],
    target_id: str,
    as_of_date: str,
    provider_name: str,
    prompt_hash: str,
    response_hash: str,
    allowed_component_ids: Sequence[str],
) -> Mapping[str, Any]:
    identity = {
        "target_id": target_id,
        "as_of_date": as_of_date,
        "document_id": document["document_id"],
        "question_family_id": proposal["question_family_id"],
        "subject_id": proposal["subject_id"],
        "predicate_family": proposal["predicate_family"],
        "normalized_object": proposal["normalized_object"],
        "period": proposal["period"],
        "mechanism_scope_id": proposal["mechanism_scope_id"],
        "exact_quote": proposal["exact_quote"],
    }
    claim_id = stable_intelligence_id("RFC", identity)
    source_family = str(document.get("source_family") or "")
    return {
        "schema_version": "e2r_v5_researcher_material_claim_v1",
        "claim_id": claim_id,
        "target_id": target_id,
        "as_of_date": as_of_date,
        "accepted": True,
        "accepted_by_evidence_os": True,
        "material": True,
        "materiality": proposal["materiality"],
        **(
            {
                "objective_ids": list(proposal["objective_ids"]),
                "objective_relation": str(proposal["objective_relation"]),
            }
            if proposal.get("objective_ids")
            else {}
        ),
        "question_family_id": str(proposal["question_family_id"]).strip(),
        "subject_id": str(proposal["subject_id"]).strip(),
        "subject": str(proposal["subject"]).strip(),
        "business_segment": str(proposal["business_segment"]).strip(),
        "product_family": str(proposal["product_family"]).strip(),
        "scope_business_segment": str(proposal["scope_business_segment"]).strip(),
        "scope_product_family": str(proposal["scope_product_family"]).strip(),
        "scope_technology_family": str(proposal["scope_technology_family"]).strip(),
        "scope_transaction_type": str(proposal["scope_transaction_type"]).strip(),
        "scope_economic_mechanism": str(proposal["scope_economic_mechanism"]).strip(),
        "scope_confidence": float(proposal["scope_confidence"]),
        "economic_mechanism": str(proposal["economic_mechanism"]).strip(),
        "mechanism_scope_id": str(proposal["mechanism_scope_id"]).strip(),
        "predicate": str(proposal["predicate"]).strip(),
        "predicate_family": str(proposal["predicate_family"]).strip(),
        "value": (
            proposal["value"]
            if (
                isinstance(proposal["value"], (Mapping, list))
                or (
                    isinstance(proposal["value"], (int, float))
                    and not isinstance(proposal["value"], bool)
                    and (
                        not isinstance(proposal["value"], float)
                        or math.isfinite(proposal["value"])
                    )
                )
            )
            else str(proposal["value"]).strip()
        ),
        "normalized_object": str(proposal["normalized_object"]).strip(),
        "unit": str(proposal.get("unit") or "").strip() or None,
        "period": str(proposal["period"]).strip(),
        "direction": str(proposal["direction"]),
        "current_lifecycle": str(proposal["current_lifecycle"]),
        "source_ids": [str(document["document_id"])],
        "document_id": str(document["document_id"]),
        "canonical_url": str(document["canonical_url"]),
        "published_at": str(document["published_at"]),
        "available_at": str(document["available_at"]),
        "exact_quote": str(proposal["exact_quote"]).strip(),
        "source_independence_group": str(
            document["source_independence_group"]
        ),
        "source_family": source_family,
        "source_tier": _source_tier(source_family),
        "confidence": float(proposal["confidence"]),
        "question_family_tags": list(
            dict.fromkeys(
                (
                    str(proposal["question_family_id"]).strip(),
                    *(str(value).strip() for value in proposal.get("question_family_tags") or ()),
                )
            )
        ),
        "primitive_tags": list(
            dict.fromkeys(
                str(value).strip()
                for value in proposal.get("primitive_tags") or ()
                if str(value).strip()
            )
        ),
        "structured_evidence_roles": list(
            dict.fromkeys(
                str(value).strip()
                for value in proposal.get("structured_evidence_roles") or ()
                if str(value).strip()
            )
        ),
        "allowed_component_ids": list(allowed_component_ids),
        "materiality_rationale": str(proposal["materiality_rationale"]).strip(),
        "deterministic_field_normalizations": list(
            dict.fromkeys(
                str(value).strip()
                for value in proposal.get(
                    "deterministic_field_normalizations", ()
                )
                if str(value).strip()
            )
        ),
        "provider_name": provider_name,
        "provider_prompt_hash": prompt_hash,
        "provider_response_hash": response_hash,
        "llm_score_authority": False,
        "llm_stage_authority": False,
    }


def _normalize_transport_fact_proposal(
    proposal: Any,
    *,
    document_by_id: Mapping[str, Mapping[str, Any]],
) -> Any:
    """Repair only representation noise that can be proven deterministically.

    The model occasionally wraps an otherwise literal source substring in one
    extra pair of quotation marks or emits a probability as a percentage.  We
    accept those forms only when stripping the wrapper produces an exact
    contiguous substring of the cited document, and only when a confidence
    value is within the conventional 0..100 percentage range.  No source text
    or economic assertion is rewritten.
    """

    if not isinstance(proposal, Mapping):
        return proposal
    normalized = dict(normalize_punctuation_only_fact_value(proposal))
    normalizations: list[str] = [
        str(value).strip()
        for value in normalized.get("deterministic_field_normalizations", ())
        if str(value).strip()
    ]
    document_id = str(normalized.get("document_id") or "")
    document = document_by_id.get(document_id)
    quote = str(normalized.get("exact_quote") or "").strip()
    content = str((document or {}).get("content_text") or "")
    if quote and content and quote not in content:
        quote_pairs = {
            '"': '"',
            "'": "'",
            "`": "`",
            "“": "”",
            "‘": "’",
        }
        expected_closer = quote_pairs.get(quote[0])
        if expected_closer is not None and quote.endswith(expected_closer):
            inner = quote[1:-1].strip()
            if inner and inner in content:
                normalized["exact_quote"] = inner
                normalizations.append("EXACT_QUOTE_OUTER_WRAPPER_STRIPPED")
    for field in ("confidence", "scope_confidence"):
        raw_value = normalized.get(field)
        try:
            numeric = float(raw_value)
        except (TypeError, ValueError):
            continue
        if math.isfinite(numeric) and 1 < numeric <= 100:
            normalized[field] = numeric / 100.0
            normalizations.append(f"{field.upper()}_PERCENT_TO_PROBABILITY")
    if normalizations:
        normalized["deterministic_field_normalizations"] = list(
            dict.fromkeys(normalizations)
        )
    return normalized


def _allowed_components(
    proposal: Mapping[str, Any],
    *,
    target_id: str,
    scope_contract: ArchetypeMechanismScopeContract,
) -> tuple[tuple[str, ...], tuple[str, ...]]:
    try:
        scope_confidence = float(proposal.get("scope_confidence"))
        if not math.isfinite(scope_confidence) or not 0 <= scope_confidence <= 1:
            raise ValueError("scope_confidence")
        scope = BusinessMechanismScope(
            issuer_id=target_id,
            business_segment=str(proposal.get("scope_business_segment") or ""),
            product_family=str(proposal.get("scope_product_family") or ""),
            technology_family=str(proposal.get("scope_technology_family") or ""),
            customer_or_counterparty="",
            transaction_type=str(proposal.get("scope_transaction_type") or ""),
            economic_mechanism=str(proposal.get("scope_economic_mechanism") or ""),
            geography="UNSPECIFIED",
            effective_period=str(proposal.get("period") or ""),
            scope_confidence=scope_confidence,
        )
    except (TypeError, ValueError):
        return (), ("INVALID_SCOPE_FIELDS",)
    validator = MechanismScopeValidator()
    validations = tuple(
        validator.validate(
            scope=scope,
            contract=scope_contract,
            component_id=component_id,
        )
        for component_id in CANONICAL_COMPONENT_ORDER
    )
    allowed = tuple(
        component_id
        for component_id, validation in zip(
            CANONICAL_COMPONENT_ORDER, validations
        )
        if validation.scope_match
    )
    reasons = tuple(
        dict.fromkeys(
            validation.reason_code
            for validation in validations
            if validation.reason_code
        )
    )
    return allowed, reasons


def _source_tier(source_family: str) -> str:
    if source_family in {"OPENDART", "KIND_KRX"}:
        return "REGULATORY_OFFICIAL"
    if source_family in {
        "ISSUER_EARNINGS_RELEASE",
        "ISSUER_PRESENTATION",
        "ISSUER_NEWSROOM",
        "FINANCIAL_STATEMENTS",
        "SEGMENT_DATA",
        "CASH_FLOW",
    }:
        return "ISSUER_OFFICIAL"
    if source_family == "CUSTOMER_OFFICIAL":
        return "CUSTOMER_OFFICIAL"
    if source_family in {"CONSENSUS_REVISION", "VALUATION_MULTIPLES"}:
        return "FINANCIAL_REVISION"
    if source_family in {
        "REUTERS",
        "TRUSTED_BUSINESS_MEDIA",
        "PUBLIC_BROKER_PDF",
        "INDUSTRY_REPORT",
    }:
        return "TRUSTED_INDEPENDENT"
    return "GENERAL_WEB"


def rematerialize_claim_source_provenance(
    claim: Mapping[str, Any],
    *,
    document: Mapping[str, Any] | None,
) -> Mapping[str, Any]:
    """Refresh only deterministic provenance derived from a migrated source.

    Claim/economic identities do not include the source-family label.  When a
    checkpoint migration corrects that label, preserve the exact quote and
    claim id while updating the family, tier, and independence group from the
    current canonical document.  Any lineage/content mismatch fails closed.
    """

    row = dict(claim)
    if (
        document is None
        or document.get("source_family_provenance_reclassified") is not True
    ):
        return row
    document_id = str(document.get("document_id") or "")
    source_ids = {
        str(value) for value in row.get("source_ids") or () if str(value)
    }
    content = str(document.get("content_text") or "")
    exact_quote = str(row.get("exact_quote") or "")
    if (
        not document_id
        or str(row.get("document_id") or "") != document_id
        or source_ids != {document_id}
        or str(row.get("target_id") or "")
        != str(document.get("target_id") or "")
        or str(row.get("as_of_date") or "")
        != str(document.get("as_of_date") or "")
        or not exact_quote
        or exact_quote not in content
        or hashlib.sha256(content.encode("utf-8")).hexdigest()
        != str(document.get("content_hash") or "")
        or (
            row.get("canonical_url")
            and str(row.get("canonical_url"))
            != str(document.get("canonical_url") or "")
        )
        or (
            row.get("published_at")
            and str(row.get("published_at"))
            != str(document.get("published_at") or "")
        )
        or (
            row.get("available_at")
            and str(row.get("available_at"))
            != str(document.get("available_at") or "")
        )
    ):
        raise ValueError(
            "claim source provenance migration lineage mismatch"
        )
    source_family = str(document.get("source_family") or "")
    source_independence_group = str(
        document.get("source_independence_group") or ""
    )
    if not source_family or not source_independence_group:
        raise ValueError(
            "migrated source document lacks canonical provenance"
        )
    if (
        str(row.get("source_family") or "") == source_family
        and str(row.get("source_independence_group") or "")
        == source_independence_group
        and str(row.get("source_tier") or "")
        == _source_tier(source_family)
    ):
        return row
    row["source_family"] = source_family
    row["source_tier"] = _source_tier(source_family)
    row["source_independence_group"] = source_independence_group
    row["source_provenance_rematerialized"] = True
    row["source_provenance_semantics_version"] = str(
        document.get("source_family_provenance_semantics_version") or ""
    )
    return row


def _clean_error(error: Exception) -> str:
    return " ".join(str(error).split())[-800:] or type(error).__name__


def _is_transport_wide_provider_failure(error: Exception) -> bool:
    """Return whether later document calls cannot reasonably make progress.

    The shared transport exposes both terminal provider failures and a
    per-request CLI timeout as ``StructuredProviderUnavailable``.  A timeout
    must leave only its own document pending because later, smaller documents
    can still succeed in the same checkpoint.
    """

    if not isinstance(error, StructuredProviderUnavailable):
        return False
    return "codex_cli_timeout" not in _clean_error(error).casefold()


def _json_character_count(value: Any) -> int:
    return len(
        json.dumps(
            value,
            ensure_ascii=False,
            sort_keys=True,
            default=str,
        )
    )


def _bounded_stale_coverage_refresh_document_ids(
    *,
    documents: Sequence[Mapping[str, Any]],
    prior_disposition_by_document_id: Mapping[str, Mapping[str, Any]],
    stale_semantics_document_ids: set[str] | frozenset[str],
    coverage_complete_document_ids: set[str] | frozenset[str],
    previously_coverage_audited_document_ids: set[str] | frozenset[str],
    coverage_gap_objective_ids: frozenset[str],
) -> frozenset[str]:
    """Select stale trusted documents only for a live lineage-scoped gap.

    A semantics-version change is not itself a material research gap. Replaying
    every legacy document merely because the extractor version changed is an
    unbounded migration, not production research. A stale document is eligible
    only when a current Supervisor/score gap names an objective already present
    in its current or historical lineage. The provider still owns economic
    relevance, while deterministic validation checks literal source support and
    objective/mechanism component compatibility.
    """

    if not coverage_gap_objective_ids:
        return frozenset()
    selected: set[str] = set()
    for document in documents:
        document_id = str(document.get("document_id") or "")
        document_objective_lineage = {
            str(value).strip()
            for key in ("objective_ids", "historical_objective_ids")
            for value in document.get(key) or ()
            if str(value).strip()
        }
        if (
            document_id not in stale_semantics_document_ids
            or document_id in coverage_complete_document_ids
            or document_id in previously_coverage_audited_document_ids
            or not (
                document_objective_lineage
                & coverage_gap_objective_ids
            )
            or _source_tier(str(document.get("source_family") or ""))
            not in _TRUSTED_COVERAGE_REFRESH_SOURCE_TIERS
        ):
            continue
        disposition = prior_disposition_by_document_id.get(document_id, {})
        if (
            str(disposition.get("status") or "") != "FACTS_EXTRACTED"
            or int(disposition.get("accepted_fact_count") or 0) <= 0
        ):
            continue
        selected.add(document_id)
    return frozenset(selected)


def _coverage_gap_objective_ids(
    *,
    open_objectives: Sequence[Mapping[str, Any]],
    score_gap_context: Mapping[str, Any],
) -> frozenset[str]:
    """Route coverage audit only to objective lineage with a live gap.

    The router reads structured gap fields, never company names, URLs, source
    prose, or fixed research keywords.  Economic selection remains with the
    provider during the coverage audit itself.
    """

    objective_component_by_id = {
        str(row.get("objective_id") or "").strip(): str(
            row.get("component_id") or ""
        ).strip()
        for row in open_objectives
        if str(row.get("objective_id") or "").strip()
    }
    open_objective_ids = frozenset(objective_component_by_id)
    unresolved_objective_ids: set[str] = set()
    unresolved_component_ids: set[str] = set()
    nonempty_gap_fields = frozenset(
        {
            "missing_fact_needs",
            "missing_material_facts",
            "source_family_gaps",
            "parser_or_extractor_failures",
            "failure_assessments",
            "unresolved_material_questions",
            "unresolved_document_ids",
            "pending_reasons",
            "query_direction_briefs",
            "new_source_family_directions",
        }
    )
    incomplete_boolean_fields = frozenset(
        {
            "memo_sufficient",
            "source_research_sufficient",
            "structured_data_complete",
            "research_complete",
            "extraction_complete",
            "resolved",
        }
    )

    def nonempty(value: Any) -> bool:
        if value is None or value is False:
            return False
        if isinstance(value, (str, bytes)):
            return bool(str(value).strip())
        if isinstance(value, Mapping):
            return bool(value)
        if isinstance(value, Sequence):
            return bool(tuple(value))
        return bool(value)

    def visit(value: Any) -> None:
        if isinstance(value, Mapping):
            status = str(value.get("status") or "").strip().upper()
            declares_gap = (
                any(
                    value.get(key) is False
                    for key in incomplete_boolean_fields
                    if key in value
                )
                or any(
                    nonempty(value.get(key))
                    for key in nonempty_gap_fields
                    if key in value
                )
                or any(
                    token in status
                    for token in (
                        "PENDING",
                        "INCOMPLETE",
                        "FAILED",
                        "NEXT_RESEARCH_REQUIRED",
                    )
                )
                or (
                    value.get("retryable") is True
                    and bool(
                        str(value.get("classification") or "").strip()
                    )
                )
            )
            for key in (
                "unresolved_objective_ids",
                "missing_objective_ids",
                "pending_objective_ids",
            ):
                for objective_id in value.get(key) or ():
                    normalized = str(objective_id).strip()
                    if normalized in open_objective_ids:
                        unresolved_objective_ids.add(normalized)
            for key in (
                "unresolved_component_ids",
                "missing_component_ids",
                "pending_component_ids",
            ):
                for component_id in value.get(key) or ():
                    normalized = str(component_id).strip()
                    if normalized:
                        unresolved_component_ids.add(normalized)
            if declares_gap:
                direct_objective_ids = {
                    str(value.get("objective_id") or "").strip(),
                    *(
                        str(row).strip()
                        for row in value.get("objective_ids") or ()
                    ),
                }
                unresolved_objective_ids.update(
                    direct_objective_ids & open_objective_ids
                )
                component_id = str(
                    value.get("component_id") or ""
                ).strip()
                if component_id:
                    unresolved_component_ids.add(component_id)
            for nested in value.values():
                visit(nested)
            return
        if isinstance(value, Sequence) and not isinstance(
            value,
            (str, bytes),
        ):
            for nested in value:
                visit(nested)

    visit(score_gap_context)
    unresolved_objective_ids.update(
        objective_id
        for objective_id, component_id
        in objective_component_by_id.items()
        if component_id in unresolved_component_ids
    )
    return frozenset(unresolved_objective_ids)


def _coverage_audit_fact_row(
    claim: Mapping[str, Any],
) -> Mapping[str, Any]:
    """Project accepted facts needed to prevent coverage-audit duplication."""

    return {
        "document_id": str(claim["document_id"]),
        "question_family_id": str(claim["question_family_id"]),
        "subject_id": str(claim["subject_id"]),
        "predicate_family": str(claim["predicate_family"]),
        "normalized_object": str(claim["normalized_object"]),
        "period": str(claim["period"]),
        "direction": str(claim["direction"]),
        "current_lifecycle": str(claim["current_lifecycle"]),
        **(
            {
                "objective_ids": list(claim["objective_ids"]),
                "objective_relation": str(claim["objective_relation"]),
            }
            if claim.get("objective_ids")
            else {}
        ),
        "exact_quote": str(claim["exact_quote"]),
    }


def _coverage_audit_attempt_payload(
    *,
    primary_payload: Mapping[str, Any],
    required_document_ids: Sequence[str],
    primary_document_dispositions: Sequence[Mapping[str, Any]],
    previously_accepted_claims: Sequence[Mapping[str, Any]],
) -> Mapping[str, Any]:
    return scrub_blind_research_payload(
        {
            **primary_payload,
            "fact_extraction_coverage_audit_context": {
                "audit_round": 1,
                "required_document_ids": sorted(required_document_ids),
                "primary_document_dispositions": [
                    dict(row) for row in primary_document_dispositions
                ],
                "previously_accepted_facts": [
                    _coverage_audit_fact_row(claim)
                    for claim in previously_accepted_claims
                ],
                "instruction": (
                    "Perform one independent coverage review of the same "
                    "supplied full documents from start to finish. Return "
                    "only distinct objective-linked facts or counterfacts "
                    "omitted from previously_accepted_facts. Re-read compound "
                    "source statements as distinct atomic economic legs when "
                    "each leg has its own literal numeric, temporal, cash-flow, "
                    "valuation, or market-response meaning needed to reconstruct "
                    "the statement. This is a semantic completeness review, not "
                    "a keyword or number checklist. Recheck named "
                    "relationships and attribution spans such as events, "
                    "sessions, speakers, participants, products, platforms, "
                    "and counterparties, and recheck source-quality or "
                    "uncertainty spans such as preliminary or unaudited "
                    "status, review or change risk, independent-verification "
                    "limits, and forward-looking risk. These are semantic "
                    "coverage families, not a keyword checklist. Do not "
                    "infer a fact or source absence from silence, and do not "
                    "repeat an accepted quote with the same normalized "
                    "economic identity. Cite an expanded-lineage objective only "
                    "when the literal fact directly affects it and the fact's "
                    "closed-vocabulary mechanism scope allows that objective's "
                    "component. The expanded roster alone does not make adjacent "
                    "background material. The same literal may be reused only "
                    "when it explicitly supports a materially distinct "
                    "objective-linked predicate or limitation; do not split "
                    "one meaning into cosmetic duplicates. If no "
                    "omitted distinct fact remains, return an empty facts "
                    "array, an empty unresolved_document_ids array, and "
                    "extraction_complete=true. Use FACTS_EXTRACTED only when "
                    "the supplied document or transport chunk has an "
                    "accepted fact in this context; otherwise return its "
                    "accurate disposition."
                ),
            },
        }
    )


def _extraction_semantics_version(
    row: FactExtractionProviderCall
    | FactExtractionRejection
    | Mapping[str, Any],
) -> str:
    if isinstance(row, (FactExtractionProviderCall, FactExtractionRejection)):
        return row.extraction_semantics_version
    return str(row.get("extraction_semantics_version") or "")


def _fact_semantics_upgrade_requires_reextraction(
    *,
    previous_version: str,
    document: Mapping[str, Any] | None,
) -> bool:
    """Re-read only broker PDFs that can supply newly admitted typed roles.

    Easy example: adding a verified operating-profit-revision role must revisit
    the dated broker PDF that contains the old/new estimates, but it must not
    reopen hundreds of unrelated issuer filings.  The document is re-read by
    the LLM; this boundary still does not infer a role from keywords.
    """

    if previous_version == FACT_EXTRACTION_SEMANTICS_VERSION:
        return False
    if previous_version in {
        _PRE_STRUCTURED_VALUATION_ROLE_SEMANTICS_VERSION,
        _PRE_STRUCTURED_REVISION_ROLE_SEMANTICS_VERSION,
    }:
        return bool(
            document is not None
            and str(document.get("source_family") or "").upper()
            == "PUBLIC_BROKER_PDF"
        )
    return True


def _coerce_provider_call(
    row: FactExtractionProviderCall | Mapping[str, Any],
) -> FactExtractionProviderCall:
    if isinstance(row, FactExtractionProviderCall):
        return row
    return FactExtractionProviderCall(
        batch_id=str(row["batch_id"]),
        status=str(row["status"]),
        document_ids=tuple(row.get("document_ids") or ()),
        accepted_claim_ids=tuple(row.get("accepted_claim_ids") or ()),
        rejected_proposal_count=int(row.get("rejected_proposal_count") or 0),
        document_dispositions=tuple(
            dict(value) for value in row.get("document_dispositions") or ()
        ),
        pending_reasons=tuple(row.get("pending_reasons") or ()),
        research_gap_feedback=tuple(row.get("research_gap_feedback") or ()),
        provider_name=str(row["provider_name"]),
        prompt_hash=str(row["prompt_hash"]),
        response_hash=(
            str(row["response_hash"]) if row.get("response_hash") else None
        ),
        provider_attempt_count=int(
            row["provider_attempt_count"]
            if "provider_attempt_count" in row
            else 1
        ),
        validation_retry_used=bool(row.get("validation_retry_used")),
        completion_flag_reconciled=bool(
            row.get("completion_flag_reconciled")
        ),
        transport_chunk_ids=tuple(row.get("transport_chunk_ids") or ()),
        accepted_claims=(
            tuple(dict(value) for value in row.get("accepted_claims") or ())
            if "accepted_claims" in row
            else None
        ),
        coverage_audit_performed=bool(
            row.get("coverage_audit_performed")
        ),
        semantics_migration_request_ids=tuple(
            str(value)
            for value in row.get("semantics_migration_request_ids") or ()
        ),
        semantics_migration_response_ids=tuple(
            str(value)
            for value in row.get("semantics_migration_response_ids") or ()
        ),
        current_lineage_request_ids=tuple(
            str(value)
            for value in row.get("current_lineage_request_ids") or ()
        ),
        current_lineage_response_ids=tuple(
            str(value)
            for value in row.get("current_lineage_response_ids") or ()
        ),
        current_lineage_original_batch_document_ids=tuple(
            str(value)
            for value in row.get(
                "current_lineage_original_batch_document_ids"
            )
            or ()
        ),
        current_lineage_objective_reassessment_document_ids=tuple(
            str(value)
            for value in row.get(
                "current_lineage_objective_reassessment_document_ids"
            )
            or ()
        ),
        extraction_semantics_version=str(
            row.get("extraction_semantics_version") or ""
        ),
        schema_version=str(
            row.get("schema_version")
            or "e2r_v5_fact_extraction_provider_call_v1"
        ),
    )


def _coerce_rejection(
    row: FactExtractionRejection | Mapping[str, Any],
) -> FactExtractionRejection:
    if isinstance(row, FactExtractionRejection):
        return row
    return FactExtractionRejection(
        batch_id=str(row["batch_id"]),
        proposal_index=int(row["proposal_index"]),
        document_id=str(row.get("document_id") or ""),
        reason=str(row["reason"]),
        material_proposal=bool(row.get("material_proposal")),
        proposed_exact_quote=(
            str(row["proposed_exact_quote"])
            if row.get("proposed_exact_quote")
            else None
        ),
        extraction_semantics_version=str(
            row.get("extraction_semantics_version") or ""
        ),
    )


__all__ = [
    "FACT_EXTRACTION_OUTPUT_FILES",
    "FactExtractionProviderCall",
    "FactExtractionRejection",
    "ResearcherEvidenceFactExtractor",
    "ResearcherFactExtractionResult",
    "production_material_fact_rows",
    "resolve_current_fact_lineage_recovery_binding",
    "write_researcher_fact_extraction_result",
]
