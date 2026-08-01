"""Provider-backed full-document extraction for current Researcher Mode.

The LLM proposes explicit economic facts.  Deterministic code verifies target,
as-of date, full-document eligibility, exact-quote lineage, document accounting,
and source identity before the existing EvidenceFactCompiler is allowed to
create canonical facts.  Search snippets and LLM-only assertions never enter
the fact graph.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import date
import hashlib
import json
import math
from pathlib import Path
import re
from typing import Any, Mapping, Sequence

from e2r.production.metadata import write_json, write_jsonl
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
)
from .prompt_projection import (
    project_fact_extraction_evidence_context,
    project_fact_extraction_score_gap_context,
)
from .evidence_fact_compiler import EvidenceFactCompiler, FactCompilationResult
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
    "e2r_v5_objective_local_coverage_audit_v1"
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
    extraction_semantics_version: str = FACT_EXTRACTION_SEMANTICS_VERSION
    schema_version: str = "e2r_v5_fact_extraction_provider_call_v3"

    def __post_init__(self) -> None:
        if self.status not in {"COMPLETE", "PENDING"}:
            raise ValueError("unknown fact extraction provider-call status")
        if self.status == "PENDING" and not self.pending_reasons:
            raise ValueError("pending fact extraction call requires reasons")
        if self.provider_attempt_count <= 0:
            raise ValueError("fact extraction provider attempt count must be positive")
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
FACT_EXTRACTION_CANONICAL_STATE_REFRESH_REQUIRED = (
    "FACT_EXTRACTION_CANONICAL_STATE_REFRESH_REQUIRED"
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
    if fact_extraction_has_exact_collaboration_wait(reasons):
        return True
    refresh_count = reasons.count(
        FACT_EXTRACTION_CANONICAL_STATE_REFRESH_REQUIRED
    )
    return bool(
        refresh_count == 1
        and all(
            reason == FACT_EXTRACTION_CANONICAL_STATE_REFRESH_REQUIRED
            or _INCOMPLETE_FACT_TRANSPORT_RE.fullmatch(reason) is not None
            for reason in reasons
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
        if isinstance(documents_per_call, bool) or documents_per_call <= 0:
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
        objective_ids = {
            str(row.get("objective_id") or "").strip()
            for row in open_objectives
        }
        if "" in objective_ids or len(objective_ids) != len(open_objectives):
            raise ValueError("fact extraction objectives require unique ids")
        objective_scope_by_document: Mapping[str, frozenset[str]] | None = None
        if extraction_mode == "PRODUCTION_OBJECTIVE_LOCAL":
            if not objective_ids:
                raise ValueError(
                    "production objective-local extraction requires open objectives"
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
        coverage_gap_objective_ids = _coverage_gap_objective_ids(
            open_objectives=open_objectives,
            score_gap_context=score_gap_context or {},
        )
        stale_semantics_disposition_count = sum(
            _extraction_semantics_version(row)
            != FACT_EXTRACTION_SEMANTICS_VERSION
            for row in prior_document_dispositions
        )
        stale_semantics_provider_call_count = sum(
            _extraction_semantics_version(row)
            != FACT_EXTRACTION_SEMANTICS_VERSION
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
            if _extraction_semantics_version(row)
            != FACT_EXTRACTION_SEMANTICS_VERSION
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
        coverage_complete_document_ids = {
            document_id
            for call in all_checkpoint_calls
            if call.coverage_audit_performed
            and call.extraction_semantics_version
            == FACT_EXTRACTION_SEMANTICS_VERSION
            for document_id in call.document_ids
        }
        coverage_refresh_document_ids = {
            str(document["document_id"])
            for document in prepared
            if str(document["document_id"])
            in set(all_prior_disposition_ids)
            and str(document["document_id"])
            not in coverage_complete_document_ids
            and bool(
                set(document.get("objective_ids") or ())
                & coverage_gap_objective_ids
            )
        }
        retained_prior_disposition_ids = (
            set(all_prior_disposition_ids)
            - coverage_refresh_document_ids
        )
        dispositions: list[Mapping[str, Any]] = [
            row
            for row in all_prior_dispositions
            if str(row.get("document_id") or "")
            in retained_prior_disposition_ids
        ]
        claims: list[Mapping[str, Any]] = [
            dict(row) for row in prior_material_claims
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
        ]
        pending: list[str] = []
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
                or str(document["document_id"])
                not in set(all_prior_disposition_ids)
            )
            and bool(
                set(document.get("objective_ids") or ())
                & coverage_gap_objective_ids
            )
        }
        all_transport_documents = tuple(
            chunk
            for document in remaining
            for chunk in _document_transport_chunks(
                document,
                max_chars=self.max_document_chars_per_call,
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
                    & coverage_refresh_document_ids
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
        ]
        calls.extend(resumed_transport_calls)
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
                current_facts=current_facts,
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
        score_gap_prompt_context = project_fact_extraction_score_gap_context(
            score_gap_context or {}
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
        canonical_state_refresh_barrier_count = 0
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
                    current_facts=current_facts,
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
                "document_ids": [str(row["document_id"]) for row in batch],
            }
            batch_document_ids = {
                str(row["document_id"]) for row in batch
            }
            coverage_only_batch = bool(batch_document_ids) and (
                batch_document_ids
                <= coverage_refresh_document_ids
            )
            batch_transport_chunk_ids = _batch_transport_chunk_ids(batch)
            if any(
                int(row.get("transport_chunk_count") or 1) > 1
                for row in batch
            ):
                batch_identity["transport_chunk_ids"] = list(
                    batch_transport_chunk_ids
                )
            batch_id = stable_intelligence_id("FACTBATCH", batch_identity)
            payload = scrub_blind_research_payload(
                {
                    "target_id": target_id,
                    "target_name": target_name,
                    "target_aliases": list(target_aliases),
                    "archetype_hypothesis": archetype_id,
                    "as_of_date": as_of_date,
                    "open_research_objectives": [dict(row) for row in open_objectives],
                    "current_evidence_facts": current_fact_prompt_context,
                    "score_gap_context": score_gap_prompt_context,
                    "normalization_contract": {
                        "question_family_id": "stable semantic research-question family, not a query string",
                        "subject_id": "stable target business/product/mechanism subject",
                        "predicate_family": "stable economic predicate family",
                        "normalized_object": "concise normalized economic object or state",
                        "value": (
                            "Use a JSON number only for one finite quantitative "
                            "point. Use a JSON string for text, ranges, identifiers, "
                            "and dates. Do not encode arbitrary objects or arrays."
                        ),
                        "mechanism_scope_id": "target-direct business mechanism, never industry or wrong-segment proxy",
                    },
                    "deterministic_mechanism_scope_contract": {
                        "allowed_business_segments": list(scope_contract.allowed_business_segments),
                        "allowed_product_families": list(scope_contract.allowed_product_families),
                        "allowed_technology_families": list(scope_contract.allowed_technology_families),
                        "allowed_transaction_types": list(scope_contract.allowed_transaction_types),
                        "allowed_economic_mechanisms": list(scope_contract.allowed_economic_mechanisms),
                        "generic_company_allowed_components": list(scope_contract.generic_company_allowed_components),
                        "forbidden_business_segments": list(scope_contract.forbidden_business_segments),
                        "forbidden_product_families": list(scope_contract.forbidden_product_families),
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
                    "full_documents": [_document_prompt_row(row) for row in batch],
                    **(
                        {
                            "fact_extraction_scope_contract": {
                                "mode": "PRODUCTION_OBJECTIVE_LOCAL",
                                "allowed_objective_relations": sorted(
                                    OBJECTIVE_FACT_RELATIONS
                                ),
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
                                    "mechanism coordinates only"
                                ),
                                "llm_owns_economic_relevance": True,
                            }
                        }
                        if objective_scope_by_document is not None
                        else {}
                    ),
                }
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
                    objective_scope_by_document=objective_scope_by_document,
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
                            "fact_extraction_continuation_context": {
                                "page_number": pagination_page_number,
                                "page_fact_limit": (
                                    FACT_EXTRACTION_PAGE_FACT_LIMIT
                                ),
                                "required_document_ids": sorted(
                                    required_page_ids
                                ),
                                "previously_accepted_facts": [
                                    {
                                        "document_id": str(
                                            claim["document_id"]
                                        ),
                                        "question_family_id": str(
                                            claim["question_family_id"]
                                        ),
                                        "subject_id": str(
                                            claim["subject_id"]
                                        ),
                                        "predicate_family": str(
                                            claim["predicate_family"]
                                        ),
                                        "normalized_object": str(
                                            claim["normalized_object"]
                                        ),
                                        "period": str(claim["period"]),
                                        "direction": str(
                                            claim["direction"]
                                        ),
                                        "current_lifecycle": str(
                                            claim["current_lifecycle"]
                                        ),
                                        **(
                                            {
                                                "objective_ids": list(
                                                    claim["objective_ids"]
                                                ),
                                                "objective_relation": str(
                                                    claim[
                                                        "objective_relation"
                                                    ]
                                                ),
                                            }
                                            if claim.get("objective_ids")
                                            else {}
                                        ),
                                        "exact_quote": str(
                                            claim["exact_quote"]
                                        ),
                                    }
                                    for claim in (
                                        previously_accepted_claims.values()
                                    )
                                ],
                                "instruction": (
                                    "Continue the same supplied batch without "
                                    "repeating any previously accepted fact or "
                                    "exact quote. Return the next distinct page "
                                    "of material facts. If more remain after "
                                    "this page, keep extraction_complete false "
                                    "and list the affected document ids. If no "
                                    "distinct facts remain, return an empty facts "
                                    "array, the accurate final disposition "
                                    "(FACTS_EXTRACTED when prior accepted facts "
                                    "exist), an empty unresolved_document_ids "
                                    "array, and extraction_complete true."
                                ),
                            },
                        }
                    )
                    continue
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
                                "previously_accepted_facts": [
                                    {
                                        "document_id": str(
                                            claim["document_id"]
                                        ),
                                        "question_family_id": str(
                                            claim["question_family_id"]
                                        ),
                                        "subject_id": str(claim["subject_id"]),
                                        "predicate_family": str(
                                            claim["predicate_family"]
                                        ),
                                        "normalized_object": str(
                                            claim["normalized_object"]
                                        ),
                                        "period": str(claim["period"]),
                                        "direction": str(claim["direction"]),
                                        "current_lifecycle": str(
                                            claim["current_lifecycle"]
                                        ),
                                        "exact_quote": str(
                                            claim["exact_quote"]
                                        ),
                                    }
                                    for claim in previously_accepted_claims.values()
                                ],
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
        if compilation.status != "FACT_COMPILATION_COMPLETE":
            pending.append(compilation.status)
        pending = list(dict.fromkeys(pending))
        research_gap_feedback.extend(
            f"FACT_EXTRACTION_RETRY_CONTEXT:{reason}" for reason in pending
        )
        coverage_audited_document_ids = {
            document_id
            for call in calls
            if call.status == "COMPLETE"
            and call.coverage_audit_performed
            for document_id in call.document_ids
        }
        disposition_document_ids = {
            str(row.get("document_id") or "")
            for row in dispositions
            if str(row.get("document_id") or "")
        }
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
            "stale_semantics_disposition_count": (
                stale_semantics_disposition_count
            ),
            "stale_semantics_provider_call_count": (
                stale_semantics_provider_call_count
            ),
            "stale_semantics_checkpoint_reextracted": False,
            "stale_semantics_checkpoint_coverage_refreshed": bool(
                coverage_refresh_document_ids
                & stale_semantics_disposition_ids
            ),
            "prior_checkpoint_coverage_refreshed": bool(
                coverage_refresh_document_ids
            ),
            "preserved_prior_claim_count": len(
                prior_material_claims
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
            "base_reextraction_document_count": 0,
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
                "transport_character_bound_enforced": (
                    max_transport_chunk_chars
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


def write_researcher_fact_extraction_result(
    result: ResearcherFactExtractionResult,
    output_directory: str | Path,
) -> Mapping[str, Path]:
    root = Path(output_directory)
    paths = {
        key: root / filename for key, filename in FACT_EXTRACTION_OUTPUT_FILES.items()
    }
    write_jsonl(paths["accepted_claims"], result.material_claims)
    write_jsonl(paths["rejections"], (row.to_dict() for row in result.rejections))
    write_jsonl(paths["document_dispositions"], result.document_dispositions)
    write_jsonl(paths["provider_calls"], (row.to_dict() for row in result.provider_calls))
    write_jsonl(paths["facts"], (row.to_dict() for row in result.facts))
    write_jsonl(
        paths["claim_fact_links"],
        (row.to_dict() for row in result.fact_compilation.claim_fact_links),
    )
    write_json(paths["result"], result.to_dict())
    write_json(paths["audit"], result.audit)
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
        chars = len(str(document.get("content_text") or ""))
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


def _document_prompt_row(row: Mapping[str, Any]) -> Mapping[str, Any]:
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


def _document_transport_chunks(
    document: Mapping[str, Any],
    *,
    max_chars: int,
) -> tuple[Mapping[str, Any], ...]:
    """Split one canonical document into overlapping literal transport chunks."""

    text = str(document.get("content_text") or "")
    if len(text) <= max_chars:
        return (document,)
    overlap = min(4_000, max(1_000, max_chars // 50))
    ranges: list[tuple[int, int]] = []
    start = 0
    while start < len(text):
        hard_end = min(len(text), start + max_chars)
        end = hard_end
        if hard_end < len(text):
            minimum_boundary = start + int(max_chars * 0.80)
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
        or any(len(str(row["content_text"])) > max_chars for row in chunks)
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
                )
            )
            continue
        objective_scope_reason = _objective_scope_rejection_reason(
            proposal,
            objective_scope_by_document=objective_scope_by_document,
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
                    FACT_EXTRACTION_SEMANTICS_VERSION
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
    if str(proposal.get("objective_relation") or "") not in OBJECTIVE_FACT_RELATIONS:
        return "INVALID_OBJECTIVE_FACT_RELATION"
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
                    "omitted from previously_accepted_facts. Recheck named "
                    "relationships and attribution spans such as events, "
                    "sessions, speakers, participants, products, platforms, "
                    "and counterparties, and recheck source-quality or "
                    "uncertainty spans such as preliminary or unaudited "
                    "status, review or change risk, independent-verification "
                    "limits, and forward-looking risk. These are semantic "
                    "coverage families, not a keyword checklist. Do not "
                    "infer a fact or source absence from silence, and do not "
                    "repeat an accepted quote with the same normalized "
                    "economic identity. The same literal may be reused only "
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
        provider_attempt_count=int(row.get("provider_attempt_count") or 1),
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
    "write_researcher_fact_extraction_result",
]
