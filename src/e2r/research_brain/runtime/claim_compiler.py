"""Contract-blind claim compilation over Phase 8 acquired documents."""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import asdict, dataclass, replace
from datetime import date, datetime
from enum import Enum
from typing import Any, Callable, Mapping, Protocol, Sequence

from e2r.agentic.evidence_os import (
    AdjudicatedClaim,
    AppendOnlyEvidenceLedger,
    AnchorType,
    Directness,
    EvidenceAnchor,
    EvidenceDocument,
    EntityRegistry,
    InvestigationStatus,
    MappingStatus,
    Polarity,
    PrimitiveMappingProposal,
    RawAssertion,
    RelationToTarget,
    SemanticStatus,
    SourceType,
    SupportDirection,
    TargetScopeStatus,
    TemporalStatus,
    VerificationStatus,
)
from e2r.production.claim_extraction import (
    ExtractionInput,
    ExtractorProviderResult,
    LLMContractBlindRawAssertionExtractor,
    RawAssertionRecord,
)
from e2r.research_brain.intelligence_schema import EvidenceRecipe
from e2r.research_brain.planning.source_task import QuestionSourceTask
from e2r.research_brain.runtime.source_acquisition import (
    AcquiredDocument,
    AcquisitionMode,
    AcquisitionResult,
    AcquisitionStatus,
)


CLAIM_COMPILER_SCHEMA_VERSION = "e2r_contract_blind_claim_compiler_v1"
CLAIM_LEDGER_EVENT_SCHEMA_VERSION = "e2r_claim_ledger_event_v1"
MAX_CANONICAL_RAW_ASSERTIONS_PER_DOCUMENT = 20

_FORBIDDEN_BLIND_INPUT_KEYS = frozenset(
    {
        "archetype_id",
        "desired_archetype",
        "expected_archetype",
        "primitive_id",
        "primitive_gap",
        "missing_primitive",
        "recipe_id",
        "score",
        "score_gap_context",
        "stage",
        "historical_outcome",
        "outcome_label",
        "mfe",
        "mae",
    }
)
_FORBIDDEN_SCORE_PROVIDER_KINDS = frozenset(
    {"LEGACY_RULE_FALLBACK", "PARSER_SIGNAL"}
)
_TASK_SATISFACTION_VALUES = frozenset(
    {
        "DIRECT_TASK_SATISFIED",
        "REROUTED_CLAIM_ACCEPTED_ORIGINAL_GAP_OPEN",
        "BASELINE_CLAIM_REUSED",
        "LIFECYCLE_REFRESH_ONLY",
        "COUNTER_CLAIM_FOUND",
        "NO_RELEVANT_CLAIM",
        "WRONG_SUBJECT",
        "STALE_ONLY",
        "PROVIDER_FAILED",
        "SOURCE_EXHAUSTED",
    }
)


class ClaimProviderKind(str, Enum):
    REAL_LLM = "REAL_LLM"
    TEST_FIXTURE_LLM = "TEST_FIXTURE_LLM"
    LEGACY_RULE_FALLBACK = "LEGACY_RULE_FALLBACK"
    PARSER_SIGNAL = "PARSER_SIGNAL"


class ClaimCompilationStatus(str, Enum):
    COMPLETE = "COMPLETE"
    PARTIAL = "PARTIAL"
    NO_RELEVANT_CLAIM = "NO_RELEVANT_CLAIM"
    PROVIDER_FAILED = "PROVIDER_FAILED"
    SOURCE_EXHAUSTED = "SOURCE_EXHAUSTED"
    REJECTED_BY_POLICY = "REJECTED_BY_POLICY"


class ClaimLifecycleKind(str, Enum):
    NEW_ASSERTION = "NEW_ASSERTION"
    BASELINE_REUSE = "BASELINE_REUSE"
    LIFECYCLE_REFRESH = "LIFECYCLE_REFRESH"


class ClaimRejectionStage(str, Enum):
    EXTRACTION = "EXTRACTION"
    ANCHOR = "ANCHOR"
    ENTITY = "ENTITY"
    TEMPORAL = "TEMPORAL"
    LIFECYCLE = "LIFECYCLE"
    MAPPING = "MAPPING"
    ELIGIBILITY = "ELIGIBILITY"
    PROVIDER = "PROVIDER"


@dataclass(frozen=True)
class BlindExtractionAnchor:
    anchor_id: str
    document_id: str
    locator: str
    exact_text: str
    content_hash: str

    def __post_init__(self) -> None:
        required = (
            self.anchor_id,
            self.document_id,
            self.locator,
            self.exact_text,
            self.content_hash,
        )
        if not all(item.strip() for item in required):
            raise ValueError("blind extraction anchor provenance is required")
        if _sha256(self.exact_text) != self.content_hash:
            raise ValueError("blind extraction anchor hash mismatch")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class BlindClaimExtractionInput:
    target_entity_id: str
    target_name: str
    symbol: str
    target_aliases: tuple[str, ...]
    as_of_date: str
    document_id: str
    source_family: str
    document_type: str
    canonical_url: str
    published_at: str
    available_at: str
    content_hash: str
    document_text: str
    anchors: tuple[BlindExtractionAnchor, ...]

    def __post_init__(self) -> None:
        required = (
            self.target_entity_id,
            self.target_name,
            self.as_of_date,
            self.document_id,
            self.source_family,
            self.document_type,
            self.canonical_url,
            self.published_at,
            self.available_at,
            self.content_hash,
            self.document_text,
        )
        if not all(item.strip() for item in required):
            raise ValueError("contract-blind extraction input is incomplete")
        as_of = _parse_date(self.as_of_date)
        if _parse_date(self.published_at) > as_of or _parse_date(self.available_at) > as_of:
            raise ValueError("contract-blind extraction input contains future source")
        if _sha256(self.document_text) != self.content_hash:
            raise ValueError("contract-blind extraction document hash mismatch")
        if not self.anchors:
            raise ValueError("contract-blind extraction requires verified anchors")
        if any(anchor.document_id != self.document_id for anchor in self.anchors):
            raise ValueError("blind extraction anchor/document mismatch")
        if len({anchor.anchor_id for anchor in self.anchors}) != len(self.anchors):
            raise ValueError("blind extraction input contains duplicate anchors")

    def to_dict(self) -> dict[str, Any]:
        payload = _json_safe(asdict(self))
        overlap = _forbidden_key_overlap(payload)
        if overlap:
            raise ValueError(
                "contract-blind provider payload leaked forbidden fields: "
                + ",".join(sorted(overlap))
            )
        return payload


@dataclass(frozen=True)
class RawExtractionBatch:
    provider_name: str
    provider_kind: str
    raw_assertions: tuple[RawAssertion, ...]
    input_hash: str
    response_hash: str
    provider_error: str | None = None

    def __post_init__(self) -> None:
        ClaimProviderKind(self.provider_kind)
        if not self.provider_name.strip():
            raise ValueError("raw extraction provider name is required")
        if not _is_sha256(self.input_hash) or not _is_sha256(self.response_hash):
            raise ValueError("raw extraction input/response hashes must be SHA-256")
        if self.provider_error and self.raw_assertions:
            raise ValueError("failed raw extraction batch cannot carry assertions")
        if len({item.raw_assertion_id for item in self.raw_assertions}) != len(
            self.raw_assertions
        ):
            raise ValueError("raw extraction batch contains duplicate assertion IDs")

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


class BlindClaimExtractorProvider(Protocol):
    provider_name: str
    provider_kind: str

    def extract(self, inputs: BlindClaimExtractionInput) -> RawExtractionBatch:
        ...


@dataclass
class FixtureBlindClaimExtractorProvider:
    callback: Callable[[BlindClaimExtractionInput], Sequence[RawAssertion]]
    provider_name: str = "fixture_contract_blind_claim_extractor"
    provider_kind: str = ClaimProviderKind.TEST_FIXTURE_LLM.value

    def extract(self, inputs: BlindClaimExtractionInput) -> RawExtractionBatch:
        assertions = tuple(self.callback(inputs))
        input_hash = _sha256(_stable_json(inputs.to_dict()))
        response_hash = _sha256(
            _stable_json(
                {"raw_assertions": [_json_safe(asdict(item)) for item in assertions]}
            )
        )
        return RawExtractionBatch(
            provider_name=self.provider_name,
            provider_kind=self.provider_kind,
            raw_assertions=assertions,
            input_hash=input_hash,
            response_hash=response_hash,
        )


@dataclass
class ProductionLLMRawExtractorAdapter:
    """Adapt the existing LLM extractor while refusing its rule fallback."""

    extractor: LLMContractBlindRawAssertionExtractor
    provider_name: str = "production_llm_contract_blind_extractor_adapter"
    provider_kind: str = ClaimProviderKind.REAL_LLM.value

    def extract(self, inputs: BlindClaimExtractionInput) -> RawExtractionBatch:
        assertions: list[RawAssertion] = []
        results: list[ExtractorProviderResult] = []
        for anchor in inputs.anchors:
            request = ExtractionInput(
                target_entity_id=inputs.target_entity_id,
                target_aliases=tuple(
                    dict.fromkeys(
                        (
                            inputs.target_name,
                            inputs.symbol,
                            *inputs.target_aliases,
                        )
                    )
                ),
                as_of_date=inputs.as_of_date,
                document_id=inputs.document_id,
                anchor_id=anchor.anchor_id,
                source_text=anchor.exact_text,
                source_metadata={
                    "canonical_url": inputs.canonical_url,
                    "source_family": inputs.source_family,
                    "document_type": inputs.document_type,
                    "published_at": inputs.published_at,
                    "available_at": inputs.available_at,
                    "content_hash": inputs.content_hash,
                },
                extra_context={},
            )
            result = self.extractor.extract_with_metadata(request)
            results.append(result)
            if result.provider_error:
                continue
            assertions.extend(
                _raw_assertion_from_record(record, expected_document_id=inputs.document_id)
                for record in result.raw_assertions
            )
        provider_modes = {str(result.provider_mode) for result in results}
        kind = (
            ClaimProviderKind.REAL_LLM
            if provider_modes == {"llm"}
            else ClaimProviderKind.LEGACY_RULE_FALLBACK
        )
        errors = tuple(
            str(result.provider_error)
            for result in results
            if str(result.provider_error or "").strip()
        )
        input_hash = _sha256(_stable_json(inputs.to_dict()))
        response_hash = _sha256(
            _stable_json(
                {
                    "provider_modes": sorted(provider_modes),
                    "response_hashes": [result.response_hash for result in results],
                    "raw_assertions": [_json_safe(asdict(item)) for item in assertions],
                    "errors": list(errors),
                }
            )
        )
        return RawExtractionBatch(
            provider_name="+".join(
                dict.fromkeys(result.provider_name for result in results)
            )
            or self.provider_name,
            provider_kind=kind.value,
            raw_assertions=() if errors else tuple(assertions),
            input_hash=input_hash,
            response_hash=response_hash,
            provider_error=";".join(errors) if errors else None,
        )


@dataclass(frozen=True)
class CanonicalAdjudicationProposal:
    raw_assertion_id: str
    subject_entity_id: str
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
    lifecycle_kind: str = ClaimLifecycleKind.NEW_ASSERTION.value
    supersedes_claim_ids: tuple[str, ...] = ()
    superseded_by_claim_ids: tuple[str, ...] = ()
    contradicted_claim_ids: tuple[str, ...] = ()
    contradiction_group_id: str | None = None
    contradiction_resolved: bool = True
    rationale: str = ""

    def __post_init__(self) -> None:
        RelationToTarget(self.relation_to_target)
        Directness(self.directness)
        TargetScopeStatus(self.target_scope_status)
        Polarity(self.polarity)
        TemporalStatus(self.temporal_status)
        SemanticStatus(self.semantic_status)
        InvestigationStatus(self.investigation_status)
        ClaimLifecycleKind(self.lifecycle_kind)
        if not self.raw_assertion_id.strip() or not self.subject_entity_id.strip():
            raise ValueError("claim adjudication identity is required")
        for value in (self.event_date, self.effective_start, self.effective_end):
            if value is not None:
                _parse_date(value)
        for values in (
            self.supersedes_claim_ids,
            self.superseded_by_claim_ids,
            self.contradicted_claim_ids,
        ):
            _require_unique_strings(values)


class CanonicalClaimAdjudicator(Protocol):
    def adjudicate(
        self,
        *,
        raw_assertion: RawAssertion,
        document: EvidenceDocument,
        anchor: EvidenceAnchor,
        target_entity_id: str,
        entity_registry: EntityRegistry,
        as_of_date: date,
    ) -> CanonicalAdjudicationProposal:
        ...


@dataclass(frozen=True)
class StrictEntityTemporalAdjudicator:
    """Resolve identity and time without recipe, score, or Stage context."""

    def adjudicate(
        self,
        *,
        raw_assertion: RawAssertion,
        document: EvidenceDocument,
        anchor: EvidenceAnchor,
        target_entity_id: str,
        entity_registry: EntityRegistry,
        as_of_date: date,
    ) -> CanonicalAdjudicationProposal:
        del anchor
        subject = _resolve_entity(raw_assertion.subject_text, entity_registry)
        subject_id = subject.entity_id if subject is not None else "UNRESOLVED_SUBJECT"
        relation = entity_registry.relation(
            subject_entity_id=subject_id,
            target_entity_id=target_entity_id,
        )
        target_scope = _target_scope_for_relation(relation.relation_to_target)
        event_date = _optional_date(raw_assertion.event_date_text)
        effective_start, effective_end = _effective_period_dates(
            raw_assertion.effective_period_text
        )
        source_date = document.published_date()
        temporal = TemporalStatus.CURRENT
        reasons: list[str] = []
        if event_date is not None and event_date > as_of_date:
            temporal = TemporalStatus.UNKNOWN
            reasons.append("future_event_date")
        elif source_date is None or source_date > as_of_date:
            temporal = TemporalStatus.UNKNOWN
            reasons.append("source_date_missing_or_future")
        elif effective_end is not None and effective_end < as_of_date:
            temporal = TemporalStatus.EXPIRED
            reasons.append("effective_period_expired")
        semantic = (
            SemanticStatus.PASS_
            if subject is not None
            else SemanticStatus.REJECTED
        )
        if subject is None:
            reasons.append("subject_unresolved")
        return CanonicalAdjudicationProposal(
            raw_assertion_id=raw_assertion.raw_assertion_id,
            subject_entity_id=subject_id,
            relation_to_target=relation.relation_to_target.value,
            directness=relation.directness.value,
            target_scope_status=target_scope.value,
            polarity=raw_assertion.polarity_proposal.value,
            temporal_status=temporal.value,
            semantic_status=semantic.value,
            investigation_status=(
                InvestigationStatus.COMPLETE.value
                if semantic == SemanticStatus.PASS_
                else InvestigationStatus.FOLLOWUP_REQUIRED.value
            ),
            event_date=event_date.isoformat() if event_date else None,
            effective_start=effective_start.isoformat() if effective_start else None,
            effective_end=effective_end.isoformat() if effective_end else None,
            rationale=";".join(reasons) or "identity_and_time_resolved",
        )


@dataclass
class FixtureCanonicalClaimAdjudicator:
    callback: Callable[
        [RawAssertion, EvidenceDocument, EvidenceAnchor, str, EntityRegistry, date],
        CanonicalAdjudicationProposal,
    ]

    def adjudicate(
        self,
        *,
        raw_assertion: RawAssertion,
        document: EvidenceDocument,
        anchor: EvidenceAnchor,
        target_entity_id: str,
        entity_registry: EntityRegistry,
        as_of_date: date,
    ) -> CanonicalAdjudicationProposal:
        return self.callback(
            raw_assertion,
            document,
            anchor,
            target_entity_id,
            entity_registry,
            as_of_date,
        )


@dataclass(frozen=True)
class RecipeMappingInput:
    claim: AdjudicatedClaim
    raw_assertion: RawAssertion
    anchor_id: str
    anchor_text: str
    source_document_id: str
    source_published_at: str
    source_available_at: str
    candidate_recipes: tuple[EvidenceRecipe, ...]

    def __post_init__(self) -> None:
        if self.claim.raw_assertion_id != self.raw_assertion.raw_assertion_id:
            raise ValueError("recipe mapping claim/raw assertion mismatch")
        if self.claim.source_anchor_id != self.anchor_id:
            raise ValueError("recipe mapping claim/anchor mismatch")
        if self.claim.source_document_id != self.source_document_id:
            raise ValueError("recipe mapping claim/document mismatch")
        if not self.anchor_text.strip() or not self.candidate_recipes:
            raise ValueError("recipe mapping input requires anchor and recipe catalog")
        if len({item.recipe_id for item in self.candidate_recipes}) != len(
            self.candidate_recipes
        ):
            raise ValueError("recipe mapping input contains duplicate recipes")

    def to_dict(self) -> dict[str, Any]:
        return {
            "claim": _json_safe(asdict(self.claim)),
            "raw_assertion": _json_safe(asdict(self.raw_assertion)),
            "anchor_id": self.anchor_id,
            "anchor_text": self.anchor_text,
            "source_document_id": self.source_document_id,
            "source_published_at": self.source_published_at,
            "source_available_at": self.source_available_at,
            "candidate_recipes": [item.to_dict() for item in self.candidate_recipes],
        }


@dataclass(frozen=True)
class RecipeClaimMappingProposal:
    mapping_id: str
    claim_id: str
    recipe_id: str
    archetype_id: str
    primitive_id: str
    accepted_predicate_id: str
    support_direction: str
    mapping_status: str
    satisfied_required_fields: tuple[str, ...]
    rationale: str

    def __post_init__(self) -> None:
        SupportDirection(self.support_direction)
        MappingStatus(self.mapping_status)
        required = (
            self.mapping_id,
            self.claim_id,
            self.recipe_id,
            self.archetype_id,
            self.primitive_id,
            self.accepted_predicate_id,
            self.rationale,
        )
        if not all(item.strip() for item in required):
            raise ValueError("recipe claim mapping identity is required")
        _require_unique_strings(self.satisfied_required_fields)

    @classmethod
    def build(
        cls,
        *,
        claim_id: str,
        recipe: EvidenceRecipe,
        accepted_predicate_id: str,
        support_direction: SupportDirection | str,
        mapping_status: MappingStatus | str,
        satisfied_required_fields: Sequence[str],
        rationale: str,
    ) -> "RecipeClaimMappingProposal":
        direction = SupportDirection(support_direction)
        status = MappingStatus(mapping_status)
        mapping_id = _stable_id(
            "RCMAP",
            {
                "claim_id": claim_id,
                "recipe_id": recipe.recipe_id,
                "predicate_id": accepted_predicate_id,
                "direction": direction.value,
                "status": status.value,
            },
        )
        return cls(
            mapping_id=mapping_id,
            claim_id=claim_id,
            recipe_id=recipe.recipe_id,
            archetype_id=recipe.archetype_id,
            primitive_id=recipe.primitive_id,
            accepted_predicate_id=accepted_predicate_id,
            support_direction=direction.value,
            mapping_status=status.value,
            satisfied_required_fields=tuple(dict.fromkeys(satisfied_required_fields)),
            rationale=rationale,
        )


@dataclass(frozen=True)
class RecipeMappingBatch:
    provider_name: str
    provider_kind: str
    mappings: tuple[RecipeClaimMappingProposal, ...]
    input_hash: str
    response_hash: str
    provider_error: str | None = None

    def __post_init__(self) -> None:
        ClaimProviderKind(self.provider_kind)
        if not self.provider_name.strip():
            raise ValueError("recipe mapper provider name is required")
        if not _is_sha256(self.input_hash) or not _is_sha256(self.response_hash):
            raise ValueError("recipe mapper input/response hashes must be SHA-256")
        if self.provider_error and self.mappings:
            raise ValueError("failed recipe mapping batch cannot carry mappings")
        if len({item.mapping_id for item in self.mappings}) != len(self.mappings):
            raise ValueError("recipe mapping batch contains duplicate mapping IDs")


class RecipeClaimMapperProvider(Protocol):
    provider_name: str
    provider_kind: str

    def map_claim(self, inputs: RecipeMappingInput) -> RecipeMappingBatch:
        ...


@dataclass
class FixtureRecipeClaimMapperProvider:
    callback: Callable[
        [RecipeMappingInput], Sequence[RecipeClaimMappingProposal]
    ]
    provider_name: str = "fixture_recipe_claim_mapper"
    provider_kind: str = ClaimProviderKind.TEST_FIXTURE_LLM.value

    def map_claim(self, inputs: RecipeMappingInput) -> RecipeMappingBatch:
        mappings = tuple(self.callback(inputs))
        input_hash = _sha256(_stable_json(inputs.to_dict()))
        response_hash = _sha256(
            _stable_json({"mappings": [_json_safe(asdict(item)) for item in mappings]})
        )
        return RecipeMappingBatch(
            provider_name=self.provider_name,
            provider_kind=self.provider_kind,
            mappings=mappings,
            input_hash=input_hash,
            response_hash=response_hash,
        )


@dataclass(frozen=True)
class ClaimProviderTrace:
    trace_id: str
    stage: str
    provider_name: str
    provider_kind: str
    input_hash: str
    response_hash: str
    provider_error: str | None = None

    def __post_init__(self) -> None:
        ClaimProviderKind(self.provider_kind)
        if not all(
            item.strip()
            for item in (self.trace_id, self.stage, self.provider_name)
        ):
            raise ValueError("claim provider trace identity is required")
        if not _is_sha256(self.input_hash) or not _is_sha256(self.response_hash):
            raise ValueError("claim provider trace hashes must be SHA-256")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class ClaimCompilationRejection:
    rejection_id: str
    stage: str
    reason: str
    detail: str
    document_id: str
    anchor_id: str | None = None
    raw_assertion_id: str | None = None
    claim_id: str | None = None
    mapping_id: str | None = None

    def __post_init__(self) -> None:
        ClaimRejectionStage(self.stage)
        if not all(
            item.strip()
            for item in (
                self.rejection_id,
                self.reason,
                self.detail,
                self.document_id,
            )
        ):
            raise ValueError("claim compilation rejection provenance is required")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class ClaimLedgerEvent:
    event_id: str
    task_id: str
    original_recipe_id: str
    original_primitive_id: str
    claim_id: str
    raw_assertion_id: str
    source_document_id: str
    source_anchor_id: str
    source_family: str
    source_url: str
    source_published_at: str
    source_available_at: str
    subject_entity_id: str
    target_entity_id: str
    relation_to_target: str
    directness: str
    target_scope_status: str
    polarity: str
    temporal_status: str
    semantic_status: str
    verification_status: str
    lifecycle_kind: str
    extraction_provider_kind: str
    mapping_provider_kind: str | None
    mapping_id: str | None
    mapped_recipe_id: str | None
    mapped_archetype_id: str | None
    mapped_primitive_id: str | None
    accepted_predicate_id: str | None
    support_direction: str | None
    mapping_status: str | None
    claim_accepted: bool
    score_eligible: bool
    production_score_eligible: bool
    eligibility_reasons: tuple[str, ...]
    supersedes_claim_ids: tuple[str, ...] = ()
    superseded_by_claim_ids: tuple[str, ...] = ()
    contradicted_claim_ids: tuple[str, ...] = ()
    contradiction_group_id: str | None = None
    contradiction_resolved: bool = True
    source_proxy_only: bool = False
    parser_mention_direct_score: bool = False
    unstructured_rule_fallback_score: bool = False
    satisfaction_status: str | None = None
    closes_original_gap: bool = False
    baseline: bool = False
    schema_version: str = CLAIM_LEDGER_EVENT_SCHEMA_VERSION

    def __post_init__(self) -> None:
        RelationToTarget(self.relation_to_target)
        Directness(self.directness)
        TargetScopeStatus(self.target_scope_status)
        Polarity(self.polarity)
        TemporalStatus(self.temporal_status)
        SemanticStatus(self.semantic_status)
        VerificationStatus(self.verification_status)
        ClaimLifecycleKind(self.lifecycle_kind)
        ClaimProviderKind(self.extraction_provider_kind)
        if self.mapping_provider_kind is not None:
            ClaimProviderKind(self.mapping_provider_kind)
        if self.support_direction is not None:
            SupportDirection(self.support_direction)
        if self.mapping_status is not None:
            MappingStatus(self.mapping_status)
        if self.satisfaction_status is not None and (
            self.satisfaction_status not in _TASK_SATISFACTION_VALUES
        ):
            raise ValueError("unknown task satisfaction status on claim ledger event")
        required = (
            self.event_id,
            self.task_id,
            self.original_recipe_id,
            self.original_primitive_id,
            self.claim_id,
            self.raw_assertion_id,
            self.source_document_id,
            self.source_anchor_id,
            self.source_family,
            self.source_url,
            self.source_published_at,
            self.source_available_at,
            self.subject_entity_id,
            self.target_entity_id,
        )
        if not all(item.strip() for item in required):
            raise ValueError("claim ledger event is missing source/claim identity")
        _parse_date(self.source_published_at)
        _parse_date(self.source_available_at)
        mapping_fields = (
            self.mapping_id,
            self.mapped_recipe_id,
            self.mapped_archetype_id,
            self.mapped_primitive_id,
            self.accepted_predicate_id,
            self.support_direction,
            self.mapping_status,
            self.mapping_provider_kind,
        )
        if any(item is not None for item in mapping_fields) and not all(
            str(item or "").strip() for item in mapping_fields
        ):
            raise ValueError("claim ledger mapping provenance is partially missing")
        if self.score_eligible:
            if not self.claim_accepted or not all(mapping_fields):
                raise ValueError("score-eligible claim requires accepted claim and mapping")
            if self.mapping_status != MappingStatus.ACCEPTED.value:
                raise ValueError("score-eligible claim requires accepted mapping")
            if self.directness != Directness.DIRECT.value:
                raise ValueError("wrong-subject claim cannot become score eligible")
            if self.temporal_status != TemporalStatus.CURRENT.value:
                raise ValueError("old/unknown claim cannot become score eligible")
            if self.source_proxy_only:
                raise ValueError("source proxy cannot become score eligible")
            if self.extraction_provider_kind in _FORBIDDEN_SCORE_PROVIDER_KINDS:
                raise ValueError("legacy parser/rule output cannot become score eligible")
            if self.mapping_provider_kind in _FORBIDDEN_SCORE_PROVIDER_KINDS:
                raise ValueError("legacy mapping output cannot become score eligible")
        if self.production_score_eligible and not self.score_eligible:
            raise ValueError("production eligibility requires canonical score eligibility")
        if self.production_score_eligible and (
            self.extraction_provider_kind != ClaimProviderKind.REAL_LLM.value
            or self.mapping_provider_kind != ClaimProviderKind.REAL_LLM.value
        ):
            raise ValueError("production eligibility requires real LLM providers")
        if self.closes_original_gap:
            if self.satisfaction_status != "DIRECT_TASK_SATISFIED":
                raise ValueError("only direct task satisfaction can close original gap")
            if (
                self.mapped_recipe_id != self.original_recipe_id
                or self.mapped_primitive_id != self.original_primitive_id
                or not self.score_eligible
            ):
                raise ValueError("original gap closure requires exact eligible recipe mapping")

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class ClaimCompilationInput:
    task: QuestionSourceTask
    recipe: EvidenceRecipe
    acquisition: AcquisitionResult
    target_aliases: tuple[str, ...]
    entity_registry: EntityRegistry
    mapping_recipes: tuple[EvidenceRecipe, ...]
    baseline_events: tuple[ClaimLedgerEvent, ...] = ()

    def __post_init__(self) -> None:
        if self.task.recipe_id != self.recipe.recipe_id:
            raise ValueError("claim compilation task/recipe mismatch")
        if self.task.primitive_id != self.recipe.primitive_id:
            raise ValueError("claim compilation task primitive differs from recipe")
        if (
            self.acquisition.task_id != self.task.task_id
            or self.acquisition.recipe_id != self.recipe.recipe_id
        ):
            raise ValueError("claim compilation acquisition identity mismatch")
        if not self.target_aliases:
            raise ValueError("claim compilation requires target aliases")
        if self.entity_registry.entity(self.task.target_id) is None:
            raise ValueError("claim compilation target is absent from entity registry")
        if self.recipe.recipe_id not in {item.recipe_id for item in self.mapping_recipes}:
            raise ValueError("mapping recipe catalog omits the task recipe")
        if len({item.recipe_id for item in self.mapping_recipes}) != len(
            self.mapping_recipes
        ):
            raise ValueError("claim compilation mapping recipes are duplicated")
        if any(
            document.task_id != self.task.task_id
            or document.recipe_id != self.recipe.recipe_id
            for document in self.acquisition.documents
        ):
            raise ValueError("acquired document is not linked to claim task/recipe")


@dataclass(frozen=True)
class ClaimCompilationResult:
    compilation_id: str
    task_id: str
    recipe_id: str
    status: str
    evidence_ledger: AppendOnlyEvidenceLedger
    raw_assertions: tuple[RawAssertion, ...]
    adjudicated_claims: tuple[AdjudicatedClaim, ...]
    recipe_mappings: tuple[RecipeClaimMappingProposal, ...]
    ledger_events: tuple[ClaimLedgerEvent, ...]
    rejections: tuple[ClaimCompilationRejection, ...]
    provider_traces: tuple[ClaimProviderTrace, ...]
    provider_errors: tuple[str, ...]
    satisfaction: Any
    production_runtime_ready: bool = False
    schema_version: str = CLAIM_COMPILER_SCHEMA_VERSION

    def __post_init__(self) -> None:
        ClaimCompilationStatus(self.status)
        if not all(
            item.strip() for item in (self.compilation_id, self.task_id, self.recipe_id)
        ):
            raise ValueError("claim compilation result identity is required")
        if self.provider_errors and self.status not in {
            ClaimCompilationStatus.PROVIDER_FAILED.value,
            ClaimCompilationStatus.PARTIAL.value,
        }:
            raise ValueError("claim provider failure cannot be masked")
        if self.production_runtime_ready:
            raise ValueError("Phase 9 result cannot declare production runtime ready")
        if any(event.task_id != self.task_id for event in self.ledger_events):
            raise ValueError("claim ledger event task mismatch")

    def to_dict(self) -> dict[str, Any]:
        return {
            "compilation_id": self.compilation_id,
            "task_id": self.task_id,
            "recipe_id": self.recipe_id,
            "status": self.status,
            "raw_assertions": [_json_safe(asdict(item)) for item in self.raw_assertions],
            "adjudicated_claims": [
                _json_safe(asdict(item)) for item in self.adjudicated_claims
            ],
            "recipe_mappings": [
                _json_safe(asdict(item)) for item in self.recipe_mappings
            ],
            "ledger_events": [item.to_dict() for item in self.ledger_events],
            "rejections": [item.to_dict() for item in self.rejections],
            "provider_traces": [item.to_dict() for item in self.provider_traces],
            "provider_errors": list(self.provider_errors),
            "satisfaction": self.satisfaction.to_dict(),
            "production_runtime_ready": self.production_runtime_ready,
            "schema_version": self.schema_version,
        }


@dataclass(frozen=True)
class LegacyClaimSideBySideResult:
    status: str
    raw_assertion_ids: tuple[str, ...]
    adjudicated_claim_ids: tuple[str, ...]
    mapping_ids: tuple[str, ...]
    canonical_score_credit_count: int = 0
    canonical_task_closure_count: int = 0
    canonical_execution_allowed: bool = False

    def __post_init__(self) -> None:
        if self.status != "LEGACY_CLAIM_DIAGNOSTIC_ONLY":
            raise ValueError("legacy claim adapter status is diagnostic-only")
        if (
            self.canonical_score_credit_count
            or self.canonical_task_closure_count
            or self.canonical_execution_allowed
        ):
            raise ValueError("legacy claim adapter cannot grant canonical credit")

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass
class ContractBlindClaimCompiler:
    extractor: BlindClaimExtractorProvider
    mapper: RecipeClaimMapperProvider
    adjudicator: CanonicalClaimAdjudicator = StrictEntityTemporalAdjudicator()
    test_mode: bool = False
    max_raw_assertions_per_document: int = MAX_CANONICAL_RAW_ASSERTIONS_PER_DOCUMENT

    def __post_init__(self) -> None:
        if (
            isinstance(self.max_raw_assertions_per_document, bool)
            or not isinstance(self.max_raw_assertions_per_document, int)
            or self.max_raw_assertions_per_document <= 0
            or self.max_raw_assertions_per_document
            > MAX_CANONICAL_RAW_ASSERTIONS_PER_DOCUMENT
        ):
            raise ValueError("claim compiler raw assertion budget is invalid")

    def compile(self, inputs: ClaimCompilationInput) -> ClaimCompilationResult:
        from e2r.research_brain.runtime.task_satisfaction import (
            evaluate_task_satisfaction,
            tag_claim_events_with_satisfaction,
        )

        provider_errors: list[str] = list(inputs.acquisition.provider_errors)
        traces: list[ClaimProviderTrace] = []
        rejections: list[ClaimCompilationRejection] = []
        raw_assertions: list[RawAssertion] = []
        claims: list[AdjudicatedClaim] = []
        mappings: list[RecipeClaimMappingProposal] = []
        events: list[ClaimLedgerEvent] = []
        ledger = AppendOnlyEvidenceLedger()

        acquisition_status = AcquisitionStatus(inputs.acquisition.status)
        if not inputs.acquisition.documents:
            source_exhausted = acquisition_status in {
                AcquisitionStatus.SOURCE_EXHAUSTED,
                AcquisitionStatus.NO_EVIDENCE,
            }
            provider_failed = acquisition_status == AcquisitionStatus.PROVIDER_FAILED
            if provider_failed and not provider_errors:
                provider_errors.append("acquisition_provider_failed_without_detail")
            policy_rejected = (
                acquisition_status == AcquisitionStatus.REJECTED_BY_POLICY
            )
            satisfaction = evaluate_task_satisfaction(
                task=inputs.task,
                events=(),
                baseline_events=(
                    () if policy_rejected else _eligible_baseline_events(inputs)
                ),
                provider_failed=provider_failed,
                source_exhausted=source_exhausted,
            )
            if satisfaction.original_gap_closed and provider_errors:
                status = ClaimCompilationStatus.PARTIAL
            elif satisfaction.original_gap_closed:
                status = ClaimCompilationStatus.COMPLETE
            elif provider_errors:
                status = ClaimCompilationStatus.PROVIDER_FAILED
            elif source_exhausted:
                status = ClaimCompilationStatus.SOURCE_EXHAUSTED
            else:
                status = ClaimCompilationStatus.REJECTED_BY_POLICY
            return _claim_result(
                inputs=inputs,
                status=status,
                ledger=ledger,
                raw_assertions=raw_assertions,
                claims=claims,
                mappings=mappings,
                events=events,
                rejections=rejections,
                traces=traces,
                provider_errors=provider_errors,
                satisfaction=satisfaction,
            )

        known_claim_ids = {
            event.claim_id for event in inputs.baseline_events
        }
        seen_raw_ids: set[str] = set()
        seen_claim_ids: set[str] = set()
        for acquired in inputs.acquisition.documents:
            document, anchors = adapt_acquired_document_to_evidence_os(acquired)
            anchors_by_id = {anchor.anchor_id: anchor for anchor in anchors}
            blind_input = _blind_input(inputs=inputs, document=acquired, anchors=anchors)
            try:
                extraction = self.extractor.extract(blind_input)
            except Exception as exc:
                error = f"extractor:{type(exc).__name__}:{exc}"
                provider_errors.append(error)
                rejections.append(
                    _rejection(
                        stage=ClaimRejectionStage.PROVIDER,
                        reason="CLAIM_EXTRACTOR_PROVIDER_FAILED",
                        detail=error,
                        document_id=acquired.document_id,
                    )
                )
                continue
            traces.append(
                _trace(
                    stage="RAW_EXTRACTION",
                    provider_name=extraction.provider_name,
                    provider_kind=extraction.provider_kind,
                    input_hash=extraction.input_hash,
                    response_hash=extraction.response_hash,
                    provider_error=extraction.provider_error,
                )
            )
            extraction_policy_error = _provider_policy_error(
                provider_kind=extraction.provider_kind,
                mode=AcquisitionMode(inputs.acquisition.mode),
                test_mode=self.test_mode,
                stage="extractor",
            )
            expected_extraction_input_hash = _sha256(
                _stable_json(blind_input.to_dict())
            )
            if extraction.input_hash != expected_extraction_input_hash:
                extraction_policy_error = "extractor_input_hash_mismatch"
            if extraction.provider_error or extraction_policy_error:
                error = extraction.provider_error or str(extraction_policy_error)
                provider_errors.append(f"extractor:{error}")
                rejections.append(
                    _rejection(
                        stage=ClaimRejectionStage.PROVIDER,
                        reason="CLAIM_EXTRACTOR_NOT_CANONICAL",
                        detail=str(error),
                        document_id=acquired.document_id,
                    )
                )
                continue
            selected_raw_assertions = extraction.raw_assertions[
                : self.max_raw_assertions_per_document
            ]
            for overflow in extraction.raw_assertions[
                self.max_raw_assertions_per_document :
            ]:
                rejections.append(
                    _rejection(
                        stage=ClaimRejectionStage.EXTRACTION,
                        reason="RAW_ASSERTION_BUDGET_EXCEEDED",
                        detail="raw assertion exceeded the bounded document budget",
                        document_id=acquired.document_id,
                        anchor_id=overflow.anchor_id,
                        raw_assertion_id=overflow.raw_assertion_id,
                    )
                )
            for raw in selected_raw_assertions:
                if raw.raw_assertion_id in seen_raw_ids:
                    rejections.append(
                        _rejection(
                            stage=ClaimRejectionStage.EXTRACTION,
                            reason="DUPLICATE_RAW_ASSERTION_ID",
                            detail="raw assertion ID already appeared in this compilation",
                            document_id=acquired.document_id,
                            raw_assertion_id=raw.raw_assertion_id,
                        )
                    )
                    continue
                seen_raw_ids.add(raw.raw_assertion_id)
                raw_assertions.append(raw)
                anchor = anchors_by_id.get(raw.anchor_id)
                anchor_error = _raw_anchor_error(raw=raw, anchor=anchor)
                if anchor_error:
                    rejections.append(
                        _rejection(
                            stage=ClaimRejectionStage.ANCHOR,
                            reason="RAW_ASSERTION_ANCHOR_REJECTED",
                            detail=anchor_error,
                            document_id=acquired.document_id,
                            anchor_id=raw.anchor_id,
                            raw_assertion_id=raw.raw_assertion_id,
                        )
                    )
                    continue
                assert anchor is not None
                try:
                    proposal = self.adjudicator.adjudicate(
                        raw_assertion=raw,
                        document=document,
                        anchor=anchor,
                        target_entity_id=inputs.task.target_id,
                        entity_registry=inputs.entity_registry,
                        as_of_date=date.fromisoformat(inputs.task.as_of_date),
                    )
                except Exception as exc:
                    rejections.append(
                        _rejection(
                            stage=ClaimRejectionStage.ENTITY,
                            reason="CLAIM_ADJUDICATION_FAILED",
                            detail=f"{type(exc).__name__}:{exc}",
                            document_id=acquired.document_id,
                            anchor_id=anchor.anchor_id,
                            raw_assertion_id=raw.raw_assertion_id,
                        )
                    )
                    continue
                claim, adjudication_reasons = _claim_from_adjudication(
                    raw=raw,
                    document=document,
                    anchor=anchor,
                    proposal=proposal,
                    inputs=inputs,
                    known_claim_ids=known_claim_ids | seen_claim_ids,
                )
                ledger.append_claim(claim)
                claims.append(claim)
                seen_claim_ids.add(claim.claim_id)
                known_claim_ids.add(claim.claim_id)
                mapping_input = RecipeMappingInput(
                    claim=claim,
                    raw_assertion=raw,
                    anchor_id=anchor.anchor_id,
                    anchor_text=anchor.exact_text,
                    source_document_id=acquired.document_id,
                    source_published_at=acquired.published_at,
                    source_available_at=acquired.available_at,
                    candidate_recipes=inputs.mapping_recipes,
                )
                try:
                    mapping_batch = self.mapper.map_claim(mapping_input)
                except Exception as exc:
                    error = f"mapper:{type(exc).__name__}:{exc}"
                    provider_errors.append(error)
                    rejections.append(
                        _rejection(
                            stage=ClaimRejectionStage.PROVIDER,
                            reason="RECIPE_MAPPER_PROVIDER_FAILED",
                            detail=error,
                            document_id=acquired.document_id,
                            anchor_id=anchor.anchor_id,
                            raw_assertion_id=raw.raw_assertion_id,
                            claim_id=claim.claim_id,
                        )
                    )
                    events.append(
                        _ledger_event(
                            inputs=inputs,
                            acquired=acquired,
                            claim=claim,
                            proposal=proposal,
                            extraction_kind=extraction.provider_kind,
                            mapping_kind=None,
                            mapping=None,
                            claim_reasons=(*adjudication_reasons, "mapping_provider_failed"),
                        )
                    )
                    continue
                traces.append(
                    _trace(
                        stage="RECIPE_MAPPING",
                        provider_name=mapping_batch.provider_name,
                        provider_kind=mapping_batch.provider_kind,
                        input_hash=mapping_batch.input_hash,
                        response_hash=mapping_batch.response_hash,
                        provider_error=mapping_batch.provider_error,
                    )
                )
                mapping_policy_error = _provider_policy_error(
                    provider_kind=mapping_batch.provider_kind,
                    mode=AcquisitionMode(inputs.acquisition.mode),
                    test_mode=self.test_mode,
                    stage="mapper",
                )
                expected_mapping_input_hash = _sha256(
                    _stable_json(mapping_input.to_dict())
                )
                if mapping_batch.input_hash != expected_mapping_input_hash:
                    mapping_policy_error = "mapper_input_hash_mismatch"
                if len(mapping_batch.mappings) > len(inputs.mapping_recipes):
                    mapping_policy_error = "mapper_output_exceeds_recipe_catalog"
                if mapping_batch.provider_error or mapping_policy_error:
                    error = mapping_batch.provider_error or str(mapping_policy_error)
                    provider_errors.append(f"mapper:{error}")
                    rejections.append(
                        _rejection(
                            stage=ClaimRejectionStage.PROVIDER,
                            reason="RECIPE_MAPPER_NOT_CANONICAL",
                            detail=str(error),
                            document_id=acquired.document_id,
                            anchor_id=anchor.anchor_id,
                            raw_assertion_id=raw.raw_assertion_id,
                            claim_id=claim.claim_id,
                        )
                    )
                    events.append(
                        _ledger_event(
                            inputs=inputs,
                            acquired=acquired,
                            claim=claim,
                            proposal=proposal,
                            extraction_kind=extraction.provider_kind,
                            mapping_kind=mapping_batch.provider_kind,
                            mapping=None,
                            claim_reasons=(*adjudication_reasons, "mapping_provider_rejected"),
                        )
                    )
                    continue
                if not mapping_batch.mappings:
                    events.append(
                        _ledger_event(
                            inputs=inputs,
                            acquired=acquired,
                            claim=claim,
                            proposal=proposal,
                            extraction_kind=extraction.provider_kind,
                            mapping_kind=mapping_batch.provider_kind,
                            mapping=None,
                            claim_reasons=(*adjudication_reasons, "no_recipe_mapping"),
                        )
                    )
                    continue
                for mapping in mapping_batch.mappings:
                    mapping_reasons, compatible_mapping = _mapping_reasons(
                        mapping=mapping,
                        claim=claim,
                        recipes=inputs.mapping_recipes,
                    )
                    mappings.append(mapping)
                    if compatible_mapping is not None:
                        ledger.append_mapping(compatible_mapping)
                    if mapping_reasons:
                        rejections.append(
                            _rejection(
                                stage=ClaimRejectionStage.MAPPING,
                                reason="RECIPE_MAPPING_REJECTED",
                                detail=";".join(mapping_reasons),
                                document_id=acquired.document_id,
                                anchor_id=anchor.anchor_id,
                                raw_assertion_id=raw.raw_assertion_id,
                                claim_id=claim.claim_id,
                                mapping_id=mapping.mapping_id,
                            )
                        )
                    events.append(
                        _ledger_event(
                            inputs=inputs,
                            acquired=acquired,
                            claim=claim,
                            proposal=proposal,
                            extraction_kind=extraction.provider_kind,
                            mapping_kind=mapping_batch.provider_kind,
                            mapping=mapping,
                            claim_reasons=(*adjudication_reasons, *mapping_reasons),
                        )
                    )

        provider_errors = list(dict.fromkeys(provider_errors))
        satisfaction = evaluate_task_satisfaction(
            task=inputs.task,
            events=tuple(events),
            baseline_events=_eligible_baseline_events(inputs),
            provider_failed=bool(provider_errors),
            source_exhausted=False,
        )
        tagged_events = tag_claim_events_with_satisfaction(
            events=tuple(events),
            satisfaction=satisfaction,
        )
        if provider_errors and tagged_events:
            status = ClaimCompilationStatus.PARTIAL
        elif provider_errors:
            status = ClaimCompilationStatus.PROVIDER_FAILED
        elif not raw_assertions:
            status = ClaimCompilationStatus.NO_RELEVANT_CLAIM
        else:
            status = ClaimCompilationStatus.COMPLETE
        return _claim_result(
            inputs=inputs,
            status=status,
            ledger=ledger,
            raw_assertions=raw_assertions,
            claims=claims,
            mappings=mappings,
            events=tagged_events,
            rejections=rejections,
            traces=traces,
            provider_errors=provider_errors,
            satisfaction=satisfaction,
        )


def adapt_acquired_document_to_evidence_os(
    document: AcquiredDocument,
) -> tuple[EvidenceDocument, tuple[EvidenceAnchor, ...]]:
    evidence_document = EvidenceDocument(
        document_id=document.document_id,
        canonical_url=document.original_source_url,
        source_type=_source_type(document.document_type),
        source_name=document.provider_name,
        content_hash=document.content_hash,
        published_at=date.fromisoformat(document.published_at),
        available_at=date.fromisoformat(document.available_at),
        fetched_at=(
            date.fromisoformat(document.fetched_at) if document.fetched_at else None
        ),
        parser_version=CLAIM_COMPILER_SCHEMA_VERSION,
        source_lineage_id=document.source_lineage_id,
        source_proxy_only=False,
    )
    anchors: list[EvidenceAnchor] = []
    seen_anchor_hashes: set[str] = set()
    for section in document.selected_sections:
        start = document.full_text.find(section.text)
        anchor_text = _anchor_context(
            document.full_text,
            section_text=section.text,
            section_start=start,
        )
        anchor_hash = _sha256(anchor_text) if anchor_text else section.content_hash
        if anchor_hash in seen_anchor_hashes:
            continue
        seen_anchor_hashes.add(anchor_hash)
        anchors.append(
            EvidenceAnchor(
                anchor_id=_stable_id(
                    "CANCH",
                    {
                        "document_id": document.document_id,
                        "section_id": section.section_id,
                        "section_hash": section.content_hash,
                        "anchor_hash": anchor_hash,
                    },
                ),
                document_id=document.document_id,
                anchor_type=AnchorType.TEXT_SPAN,
                locator=(
                    f"char:{start}:{start + len(section.text)}"
                    if start >= 0
                    else f"section:{section.section_id}:not-found"
                ),
                exact_text=anchor_text,
                content_hash=anchor_hash,
                anchor_verified=(
                    start >= 0
                    and bool(anchor_text)
                    and section.text in anchor_text
                    and _sha256(section.text) == section.content_hash
                    and _sha256(document.full_text) == document.content_hash
                ),
            )
        )
    return evidence_document, tuple(anchors)


def adapt_legacy_claim_bundle_for_diagnostics(bundle: Any) -> LegacyClaimSideBySideResult:
    raw = getattr(bundle, "raw_assertions", {}) or {}
    ledger = getattr(bundle, "ledger", None)
    claims = getattr(ledger, "claims", {}) if ledger is not None else {}
    mappings = getattr(ledger, "mappings", {}) if ledger is not None else {}
    return LegacyClaimSideBySideResult(
        status="LEGACY_CLAIM_DIAGNOSTIC_ONLY",
        raw_assertion_ids=tuple(sorted(str(item) for item in raw)),
        adjudicated_claim_ids=tuple(sorted(str(item) for item in claims)),
        mapping_ids=tuple(sorted(str(item) for item in mappings)),
    )


def audit_claim_compilation_results(
    results: Sequence[ClaimCompilationResult],
) -> Mapping[str, Any]:
    events = [event for result in results for event in result.ledger_events]
    accepted = [event for event in events if event.score_eligible]
    critical = {
        "accepted_claim_missing_anchor_source_date_subject_target": sum(
            not all(
                (
                    event.source_anchor_id,
                    event.source_document_id,
                    event.source_published_at,
                    event.source_available_at,
                    event.subject_entity_id,
                    event.target_entity_id,
                )
            )
            for event in accepted
        ),
        "source_proxy_current_claim": sum(
            event.score_eligible and event.source_proxy_only for event in events
        ),
        "wrong_subject_score": sum(
            event.score_eligible and event.directness != Directness.DIRECT.value
            for event in events
        ),
        "old_unknown_risk_penalty": sum(
            event.score_eligible
            and event.temporal_status != TemporalStatus.CURRENT.value
            and (
                event.polarity == Polarity.NEGATIVE.value
                or event.support_direction == SupportDirection.COUNTER.value
            )
            for event in events
        ),
        "rerouted_original_gap_closure": sum(
            event.closes_original_gap
            and (
                event.mapped_recipe_id != event.original_recipe_id
                or event.mapped_primitive_id != event.original_primitive_id
            )
            for event in events
        ),
        "unstructured_rule_fallback_score": sum(
            event.score_eligible and event.unstructured_rule_fallback_score
            for event in events
        ),
        "recipe_mapping_missing_score": sum(
            event.score_eligible and not event.mapping_id for event in events
        ),
        "parser_mention_direct_score": sum(
            event.score_eligible and event.parser_mention_direct_score
            for event in events
        ),
        "provider_failure_masked": sum(
            bool(result.provider_errors)
            and result.status
            not in {
                ClaimCompilationStatus.PROVIDER_FAILED.value,
                ClaimCompilationStatus.PARTIAL.value,
            }
            for result in results
        ),
    }
    return {
        "schema_version": "e2r_claim_compiler_audit_v1",
        "status": (
            "CONTRACT_BLIND_CLAIM_COMPILER_PASS"
            if results and sum(critical.values()) == 0
            else "CONTRACT_BLIND_CLAIM_COMPILER_FAIL"
        ),
        "result_count": len(results),
        "raw_assertion_count": sum(len(item.raw_assertions) for item in results),
        "adjudicated_claim_count": sum(
            len(item.adjudicated_claims) for item in results
        ),
        "ledger_event_count": len(events),
        "score_eligible_claim_event_count": len(accepted),
        "direct_original_gap_closure_count": sum(
            event.closes_original_gap for event in events
        ),
        "rerouted_claim_event_count": sum(
            event.satisfaction_status
            == "REROUTED_CLAIM_ACCEPTED_ORIGINAL_GAP_OPEN"
            for event in events
        ),
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
        "result_hash": _sha256(
            _stable_json({"results": [item.to_dict() for item in results]})
        ),
        "production_runtime_ready": False,
    }


def _blind_input(
    *,
    inputs: ClaimCompilationInput,
    document: AcquiredDocument,
    anchors: Sequence[EvidenceAnchor],
) -> BlindClaimExtractionInput:
    aliases = tuple(
        dict.fromkeys((inputs.task.company_name, inputs.task.symbol, *inputs.target_aliases))
    )
    return BlindClaimExtractionInput(
        target_entity_id=inputs.task.target_id,
        target_name=inputs.task.company_name,
        symbol=inputs.task.symbol,
        target_aliases=aliases,
        as_of_date=inputs.task.as_of_date,
        document_id=document.document_id,
        source_family=document.source_family,
        document_type=document.document_type,
        canonical_url=document.original_source_url,
        published_at=document.published_at,
        available_at=document.available_at,
        content_hash=document.content_hash,
        document_text=document.full_text,
        anchors=tuple(
            BlindExtractionAnchor(
                anchor_id=anchor.anchor_id,
                document_id=anchor.document_id,
                locator=anchor.locator,
                exact_text=anchor.exact_text,
                content_hash=str(anchor.content_hash),
            )
            for anchor in anchors
        ),
    )


def _eligible_baseline_events(
    inputs: ClaimCompilationInput,
) -> tuple[ClaimLedgerEvent, ...]:
    if inputs.acquisition.mode != AcquisitionMode.PRODUCTION_BOUNDED.value:
        return inputs.baseline_events
    return tuple(
        event for event in inputs.baseline_events if event.production_score_eligible
    )


def _claim_from_adjudication(
    *,
    raw: RawAssertion,
    document: EvidenceDocument,
    anchor: EvidenceAnchor,
    proposal: CanonicalAdjudicationProposal,
    inputs: ClaimCompilationInput,
    known_claim_ids: set[str],
) -> tuple[AdjudicatedClaim, tuple[str, ...]]:
    reasons: list[str] = []
    if proposal.raw_assertion_id != raw.raw_assertion_id:
        reasons.append("adjudication_raw_assertion_mismatch")
    if raw.event_date_text and not _date_text_is_anchored(
        raw.event_date_text,
        raw.exact_quote,
    ):
        reasons.append("event_date_not_anchored_in_quote")
    for effective_date_text in re.findall(
        r"20[0-9]{2}-[01][0-9]-[0-3][0-9]",
        str(raw.effective_period_text or ""),
    ):
        if not _date_text_is_anchored(effective_date_text, raw.exact_quote):
            reasons.append("effective_period_not_anchored_in_quote")
            break
    subject = inputs.entity_registry.entity(proposal.subject_entity_id)
    if subject is None:
        reasons.append("subject_entity_not_in_registry")
    elif not any(
        _normalize_entity_name(name) in _normalize_entity_name(raw.exact_quote)
        for name in _entity_identity_names(subject)
        if _normalize_entity_name(name)
    ):
        reasons.append("subject_entity_not_anchored_in_quote")
    actual_relation = inputs.entity_registry.relation(
        subject_entity_id=proposal.subject_entity_id,
        target_entity_id=inputs.task.target_id,
    )
    if (
        actual_relation.relation_to_target.value != proposal.relation_to_target
        or actual_relation.directness.value != proposal.directness
    ):
        reasons.append("adjudication_relation_mismatch")
    expected_scope = _target_scope_for_relation(actual_relation.relation_to_target)
    if expected_scope.value != proposal.target_scope_status:
        reasons.append("adjudication_target_scope_mismatch")
    as_of = date.fromisoformat(inputs.task.as_of_date)
    dates = tuple(
        _optional_date(value)
        for value in (proposal.event_date, proposal.effective_start, proposal.effective_end)
    )
    if dates[0] is not None and dates[0] > as_of:
        reasons.append("future_event_date")
    relationship_ids = {
        *proposal.supersedes_claim_ids,
        *proposal.superseded_by_claim_ids,
        *proposal.contradicted_claim_ids,
    }
    unknown_relationships = sorted(relationship_ids - known_claim_ids)
    if unknown_relationships:
        reasons.append(
            "unknown_claim_relationship:" + ",".join(unknown_relationships)
        )
    semantic_status = SemanticStatus(proposal.semantic_status)
    temporal_status = TemporalStatus(proposal.temporal_status)
    if proposal.superseded_by_claim_ids:
        temporal_status = TemporalStatus.SUPERSEDED
    quote_verified = anchor.anchor_verified and _quote_in_anchor(
        raw.exact_quote,
        anchor_text=anchor.exact_text,
    )
    if not quote_verified:
        reasons.append("exact_quote_not_verified_by_anchor")
    verification = (
        VerificationStatus.SEMANTIC_VERIFIED
        if quote_verified and semantic_status == SemanticStatus.PASS_ and not reasons
        else VerificationStatus.REJECTED
    )
    claim = AdjudicatedClaim.from_raw(
        raw=raw,
        document=document,
        anchor=anchor,
        subject_entity_id=proposal.subject_entity_id,
        target_entity_id=inputs.task.target_id,
        relation_to_target=RelationToTarget(proposal.relation_to_target),
        directness=Directness(proposal.directness),
        verification_status=verification,
        target_scope_status=TargetScopeStatus(proposal.target_scope_status),
        polarity=Polarity(proposal.polarity),
        temporal_status=temporal_status,
        semantic_status=semantic_status,
        investigation_status=InvestigationStatus(proposal.investigation_status),
        event_date=dates[0],
        effective_start=dates[1],
        effective_end=dates[2],
        superseded_by_claim_ids=proposal.superseded_by_claim_ids,
        contradiction_group_id=proposal.contradiction_group_id,
        adjudication_rationale=proposal.rationale,
        extraction_schema_version=CLAIM_COMPILER_SCHEMA_VERSION,
    )
    return claim, tuple(dict.fromkeys(reasons))


def _mapping_reasons(
    *,
    mapping: RecipeClaimMappingProposal,
    claim: AdjudicatedClaim,
    recipes: Sequence[EvidenceRecipe],
) -> tuple[tuple[str, ...], PrimitiveMappingProposal | None]:
    reasons: list[str] = []
    recipes_by_id = {item.recipe_id: item for item in recipes}
    recipe = recipes_by_id.get(mapping.recipe_id)
    expected_mapping_id = _stable_id(
        "RCMAP",
        {
            "claim_id": mapping.claim_id,
            "recipe_id": mapping.recipe_id,
            "predicate_id": mapping.accepted_predicate_id,
            "direction": mapping.support_direction,
            "status": mapping.mapping_status,
        },
    )
    if mapping.mapping_id != expected_mapping_id:
        reasons.append("mapping_id_not_canonical")
    if mapping.claim_id != claim.claim_id:
        reasons.append("mapping_claim_mismatch")
    if recipe is None:
        reasons.append("mapping_recipe_unknown")
    elif (
        mapping.archetype_id != recipe.archetype_id
        or mapping.primitive_id != recipe.primitive_id
    ):
        reasons.append("mapping_recipe_identity_mismatch")
    predicate = None
    if recipe is not None:
        predicate = next(
            (
                item
                for item in recipe.accepted_claim_predicates
                if item.predicate_id == mapping.accepted_predicate_id
            ),
            None,
        )
        if predicate is None:
            reasons.append("accepted_predicate_unknown")
    if predicate is not None:
        missing_fields = set(predicate.required_fields) - set(
            mapping.satisfied_required_fields
        )
        if missing_fields:
            reasons.append(
                "accepted_predicate_required_fields_missing:"
                + ",".join(sorted(missing_fields))
            )
        if claim.polarity.value not in set(predicate.allowed_polarities):
            reasons.append("claim_polarity_not_allowed_by_predicate")
    if mapping.mapping_status != MappingStatus.ACCEPTED.value:
        reasons.append("mapping_not_accepted")
    if reasons:
        return tuple(dict.fromkeys(reasons)), None
    primitive_mapping = PrimitiveMappingProposal(
        mapping_id=mapping.mapping_id,
        claim_id=mapping.claim_id,
        archetype_id=mapping.archetype_id,
        primitive_id=mapping.primitive_id,
        support_direction=SupportDirection(mapping.support_direction),
        mapping_status=MappingStatus(mapping.mapping_status),
        rationale=mapping.rationale,
        contract_rule_id=mapping.accepted_predicate_id,
    )
    return (), primitive_mapping


def _ledger_event(
    *,
    inputs: ClaimCompilationInput,
    acquired: AcquiredDocument,
    claim: AdjudicatedClaim,
    proposal: CanonicalAdjudicationProposal,
    extraction_kind: str,
    mapping_kind: str | None,
    mapping: RecipeClaimMappingProposal | None,
    claim_reasons: Sequence[str],
) -> ClaimLedgerEvent:
    reasons = list(dict.fromkeys(str(item) for item in claim_reasons if str(item)))
    if claim.verification_status != VerificationStatus.SEMANTIC_VERIFIED:
        reasons.append("claim_not_semantically_verified")
    if claim.semantic_status != SemanticStatus.PASS_:
        reasons.append("claim_semantic_status_not_pass")
    if claim.directness != Directness.DIRECT:
        reasons.append("wrong_or_indirect_subject")
    if claim.target_scope_status in {
        TargetScopeStatus.UNRELATED,
        TargetScopeStatus.UNKNOWN,
        TargetScopeStatus.INDUSTRY,
    }:
        reasons.append("target_scope_not_eligible")
    if claim.temporal_status != TemporalStatus.CURRENT:
        reasons.append(f"temporal_not_current:{claim.temporal_status.value}")
    if proposal.lifecycle_kind == ClaimLifecycleKind.LIFECYCLE_REFRESH.value:
        reasons.append("lifecycle_refresh_only")
    if proposal.contradicted_claim_ids and not proposal.contradiction_resolved:
        reasons.append("contradiction_open")
    if mapping is None:
        reasons.append("recipe_mapping_missing")
    else:
        mapping_reasons, _ = _mapping_reasons(
            mapping=mapping,
            claim=claim,
            recipes=inputs.mapping_recipes,
        )
        reasons.extend(mapping_reasons)
        if mapping.support_direction == SupportDirection.NEUTRAL.value:
            reasons.append("neutral_mapping_not_score_eligible")
    if extraction_kind in _FORBIDDEN_SCORE_PROVIDER_KINDS:
        reasons.append("legacy_extraction_provider_forbidden")
    if mapping_kind in _FORBIDDEN_SCORE_PROVIDER_KINDS:
        reasons.append("legacy_mapping_provider_forbidden")
    reasons = list(dict.fromkeys(reasons))
    claim_accepted = (
        claim.verification_status == VerificationStatus.SEMANTIC_VERIFIED
        and claim.semantic_status == SemanticStatus.PASS_
        and claim.directness == Directness.DIRECT
        and claim.target_scope_status
        not in {
            TargetScopeStatus.UNRELATED,
            TargetScopeStatus.UNKNOWN,
            TargetScopeStatus.INDUSTRY,
        }
        and bool(claim.source_document_id)
        and bool(claim.source_anchor_id)
        and bool(acquired.published_at)
        and bool(acquired.available_at)
    )
    score_eligible = claim_accepted and not reasons
    production_score_eligible = (
        score_eligible
        and inputs.acquisition.mode == AcquisitionMode.PRODUCTION_BOUNDED.value
        and extraction_kind == ClaimProviderKind.REAL_LLM.value
        and mapping_kind == ClaimProviderKind.REAL_LLM.value
        and not inputs.acquisition.provider_errors
    )
    event_payload = {
        "task_id": inputs.task.task_id,
        "claim_id": claim.claim_id,
        "mapping_id": mapping.mapping_id if mapping else None,
        "document_id": acquired.document_id,
        "anchor_id": claim.source_anchor_id,
    }
    return ClaimLedgerEvent(
        event_id=_stable_id("CLEVT", event_payload),
        task_id=inputs.task.task_id,
        original_recipe_id=inputs.recipe.recipe_id,
        original_primitive_id=inputs.recipe.primitive_id,
        claim_id=claim.claim_id,
        raw_assertion_id=claim.raw_assertion_id,
        source_document_id=acquired.document_id,
        source_anchor_id=claim.source_anchor_id,
        source_family=acquired.source_family,
        source_url=acquired.original_source_url,
        source_published_at=acquired.published_at,
        source_available_at=acquired.available_at,
        subject_entity_id=claim.subject_entity_id,
        target_entity_id=claim.target_entity_id,
        relation_to_target=claim.relation_to_target.value,
        directness=claim.directness.value,
        target_scope_status=claim.target_scope_status.value,
        polarity=claim.polarity.value,
        temporal_status=claim.temporal_status.value,
        semantic_status=claim.semantic_status.value,
        verification_status=claim.verification_status.value,
        lifecycle_kind=proposal.lifecycle_kind,
        extraction_provider_kind=extraction_kind,
        mapping_provider_kind=mapping_kind if mapping else None,
        mapping_id=mapping.mapping_id if mapping else None,
        mapped_recipe_id=mapping.recipe_id if mapping else None,
        mapped_archetype_id=mapping.archetype_id if mapping else None,
        mapped_primitive_id=mapping.primitive_id if mapping else None,
        accepted_predicate_id=(mapping.accepted_predicate_id if mapping else None),
        support_direction=mapping.support_direction if mapping else None,
        mapping_status=mapping.mapping_status if mapping else None,
        claim_accepted=claim_accepted,
        score_eligible=score_eligible,
        production_score_eligible=production_score_eligible,
        eligibility_reasons=tuple(reasons),
        supersedes_claim_ids=proposal.supersedes_claim_ids,
        superseded_by_claim_ids=proposal.superseded_by_claim_ids,
        contradicted_claim_ids=proposal.contradicted_claim_ids,
        contradiction_group_id=proposal.contradiction_group_id,
        contradiction_resolved=proposal.contradiction_resolved,
        source_proxy_only=False,
        parser_mention_direct_score=(
            score_eligible and extraction_kind == ClaimProviderKind.PARSER_SIGNAL.value
        ),
        unstructured_rule_fallback_score=(
            score_eligible
            and extraction_kind == ClaimProviderKind.LEGACY_RULE_FALLBACK.value
        ),
    )


def _claim_result(
    *,
    inputs: ClaimCompilationInput,
    status: ClaimCompilationStatus,
    ledger: AppendOnlyEvidenceLedger,
    raw_assertions: Sequence[RawAssertion],
    claims: Sequence[AdjudicatedClaim],
    mappings: Sequence[RecipeClaimMappingProposal],
    events: Sequence[ClaimLedgerEvent],
    rejections: Sequence[ClaimCompilationRejection],
    traces: Sequence[ClaimProviderTrace],
    provider_errors: Sequence[str],
    satisfaction: Any,
) -> ClaimCompilationResult:
    compilation_id = _stable_id(
        "CCOMP",
        {
            "task_id": inputs.task.task_id,
            "acquisition_id": inputs.acquisition.acquisition_id,
            "event_ids": [item.event_id for item in events],
            "rejection_ids": [item.rejection_id for item in rejections],
            "provider_errors": list(provider_errors),
            "satisfaction": satisfaction.status,
        },
    )
    return ClaimCompilationResult(
        compilation_id=compilation_id,
        task_id=inputs.task.task_id,
        recipe_id=inputs.recipe.recipe_id,
        status=status.value,
        evidence_ledger=ledger,
        raw_assertions=tuple(raw_assertions),
        adjudicated_claims=tuple(claims),
        recipe_mappings=tuple(mappings),
        ledger_events=tuple(events),
        rejections=tuple(rejections),
        provider_traces=tuple(traces),
        provider_errors=tuple(dict.fromkeys(provider_errors)),
        satisfaction=satisfaction,
    )


def _trace(
    *,
    stage: str,
    provider_name: str,
    provider_kind: str,
    input_hash: str,
    response_hash: str,
    provider_error: str | None,
) -> ClaimProviderTrace:
    return ClaimProviderTrace(
        trace_id=_stable_id(
            "CPTRACE",
            {
                "stage": stage,
                "provider": provider_name,
                "kind": provider_kind,
                "input_hash": input_hash,
                "response_hash": response_hash,
            },
        ),
        stage=stage,
        provider_name=provider_name,
        provider_kind=provider_kind,
        input_hash=input_hash,
        response_hash=response_hash,
        provider_error=provider_error,
    )


def _rejection(
    *,
    stage: ClaimRejectionStage,
    reason: str,
    detail: str,
    document_id: str,
    anchor_id: str | None = None,
    raw_assertion_id: str | None = None,
    claim_id: str | None = None,
    mapping_id: str | None = None,
) -> ClaimCompilationRejection:
    return ClaimCompilationRejection(
        rejection_id=_stable_id(
            "CCREJ",
            {
                "stage": stage.value,
                "reason": reason,
                "document_id": document_id,
                "anchor_id": anchor_id,
                "raw_assertion_id": raw_assertion_id,
                "claim_id": claim_id,
                "mapping_id": mapping_id,
            },
        ),
        stage=stage.value,
        reason=reason,
        detail=detail,
        document_id=document_id,
        anchor_id=anchor_id,
        raw_assertion_id=raw_assertion_id,
        claim_id=claim_id,
        mapping_id=mapping_id,
    )


def _provider_policy_error(
    *,
    provider_kind: str,
    mode: AcquisitionMode,
    test_mode: bool,
    stage: str,
) -> str | None:
    kind = ClaimProviderKind(provider_kind)
    if kind in {
        ClaimProviderKind.LEGACY_RULE_FALLBACK,
        ClaimProviderKind.PARSER_SIGNAL,
    }:
        return f"{stage}_legacy_rule_or_parser_provider_forbidden"
    if kind == ClaimProviderKind.TEST_FIXTURE_LLM and not test_mode:
        return f"{stage}_fixture_provider_outside_test_mode"
    if mode == AcquisitionMode.PRODUCTION_BOUNDED and (
        kind != ClaimProviderKind.REAL_LLM
    ):
        return f"{stage}_production_requires_real_llm_provider"
    return None


def _raw_anchor_error(
    *, raw: RawAssertion, anchor: EvidenceAnchor | None
) -> str | None:
    if anchor is None:
        return "raw assertion references unknown anchor"
    if not anchor.anchor_verified:
        return "raw assertion anchor is not verified"
    if not raw.exact_quote.strip():
        return "raw assertion exact quote is empty"
    if not _quote_in_anchor(raw.exact_quote, anchor_text=anchor.exact_text):
        return "raw assertion exact quote is absent from anchor"
    return None


def _raw_assertion_from_record(
    record: RawAssertionRecord, *, expected_document_id: str
) -> RawAssertion:
    if record.document_id != expected_document_id:
        raise ValueError("LLM raw assertion document identity mismatch")
    try:
        polarity = Polarity(str(record.polarity_proposal))
    except ValueError:
        polarity = Polarity.CONDITIONAL
    return RawAssertion(
        raw_assertion_id=record.raw_assertion_id,
        anchor_id=record.anchor_id,
        subject_text=record.subject,
        predicate=record.predicate,
        object_text=record.object_text,
        polarity_proposal=polarity,
        modality=record.modality,
        event_date_text=record.event_date,
        exact_quote=record.exact_quote,
        related_entity_texts=record.related_entities,
        extractor_model="production_llm_adapter",
    )


def _source_type(document_type: str) -> SourceType:
    mapping = {
        "filing": SourceType.FILING,
        "earnings_release": SourceType.IR,
        "investor_presentation": SourceType.IR,
        "earnings_call_transcript": SourceType.IR,
        "transcript": SourceType.IR,
        "full_article": SourceType.NEWS,
        "press_release": SourceType.NEWS,
        "research_report": SourceType.RESEARCH_REPORT,
        "financial_statement": SourceType.XBRL,
        "structured_record": SourceType.API,
        "registry_record": SourceType.API,
        "industry_dataset": SourceType.API,
    }
    return mapping.get(document_type, SourceType.OTHER)


def _anchor_context(
    document_text: str,
    *,
    section_text: str,
    section_start: int,
    radius: int = 900,
) -> str:
    if section_start < 0:
        return ""
    start = max(0, section_start - radius)
    end = min(len(document_text), section_start + len(section_text) + radius)
    return document_text[start:end].strip()


def _target_scope_for_relation(relation: RelationToTarget) -> TargetScopeStatus:
    mapping = {
        RelationToTarget.SELF: TargetScopeStatus.DIRECT,
        RelationToTarget.SUBSIDIARY: TargetScopeStatus.SUBSIDIARY,
        RelationToTarget.PARENT: TargetScopeStatus.PARENT,
        RelationToTarget.CUSTOMER: TargetScopeStatus.CUSTOMER,
        RelationToTarget.SUPPLIER: TargetScopeStatus.SUPPLIER,
        RelationToTarget.PARTNER: TargetScopeStatus.PARTNER,
        RelationToTarget.INDUSTRY: TargetScopeStatus.INDUSTRY,
        RelationToTarget.UNRELATED: TargetScopeStatus.UNRELATED,
        RelationToTarget.COMPETITOR: TargetScopeStatus.UNRELATED,
        RelationToTarget.UNKNOWN: TargetScopeStatus.UNKNOWN,
    }
    return mapping[relation]


def _resolve_entity(value: str, registry: EntityRegistry) -> Any | None:
    resolved = registry.resolve_text(value)
    if resolved is not None:
        return resolved
    needle = _normalize_entity_name(value)
    if not needle:
        return None
    for entity in registry.entities.values():
        identities = _entity_identity_names(entity)
        if any(
            _normalize_entity_name(str(identity or "")) == needle
            for identity in identities
        ):
            return entity
    return None


def _entity_identity_names(entity: Any) -> tuple[str, ...]:
    return tuple(
        str(item)
        for item in (
            *entity.names(),
            entity.ticker,
            entity.dart_corp_code,
            entity.cik,
        )
        if str(item or "").strip()
    )


def _effective_period_dates(value: str | None) -> tuple[date | None, date | None]:
    if not value:
        return None, None
    matches = re.findall(r"20[0-9]{2}-[01][0-9]-[0-3][0-9]", value)
    parsed = tuple(_optional_date(item) for item in matches[:2])
    if not parsed:
        return None, None
    if len(parsed) == 1:
        return parsed[0], None
    return parsed[0], parsed[1]


def _quote_in_anchor(quote: str, *, anchor_text: str) -> bool:
    clean_quote = _normalize_text(quote)
    if not clean_quote:
        return False
    if not anchor_text:
        return True
    return clean_quote in _normalize_text(anchor_text)


def _normalize_text(value: str) -> str:
    return re.sub(r"\s+", " ", str(value).casefold()).strip()


def _normalize_entity_name(value: str) -> str:
    return re.sub(r"[^0-9a-z가-힣]", "", str(value).casefold())


def _date_text_is_anchored(value: str, quote: str) -> bool:
    clean = str(value).strip()[:10]
    variants = {clean, clean.replace("-", "."), clean.replace("-", "/")}
    parsed = _optional_date(clean)
    if parsed is not None:
        variants.update(
            {
                f"{parsed.year}{parsed.month:02d}{parsed.day:02d}",
                f"{parsed.year}.{parsed.month}.{parsed.day}",
                f"{parsed.year}/{parsed.month}/{parsed.day}",
                f"{parsed.year}년 {parsed.month}월 {parsed.day}일",
                f"{parsed.year}년{parsed.month}월{parsed.day}일",
            }
        )
    return any(item and item in str(quote) for item in variants)


def _forbidden_key_overlap(value: Any) -> set[str]:
    overlap: set[str] = set()
    if isinstance(value, Mapping):
        for key, item in value.items():
            normalized = str(key).casefold()
            if normalized in _FORBIDDEN_BLIND_INPUT_KEYS:
                overlap.add(normalized)
            overlap.update(_forbidden_key_overlap(item))
    elif isinstance(value, (tuple, list)):
        for item in value:
            overlap.update(_forbidden_key_overlap(item))
    return overlap


def _require_unique_strings(values: Sequence[str]) -> None:
    if any(not isinstance(item, str) or not item.strip() for item in values):
        raise ValueError("claim compiler string tuple contains empty values")
    if len(set(values)) != len(values):
        raise ValueError("claim compiler string tuple contains duplicates")


def _optional_date(value: str | None) -> date | None:
    if value is None or not str(value).strip():
        return None
    try:
        return _parse_date(str(value))
    except ValueError:
        return None


def _parse_date(value: str) -> date:
    try:
        return date.fromisoformat(str(value)[:10])
    except ValueError as exc:
        raise ValueError(f"invalid ISO date: {value}") from exc


def _stable_id(prefix: str, payload: Mapping[str, Any]) -> str:
    return f"{prefix}-{_sha256(_stable_json(payload))[:24]}"


def _stable_json(value: Any) -> str:
    return json.dumps(
        _json_safe(value),
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )


def _sha256(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _is_sha256(value: str) -> bool:
    return re.fullmatch(r"[0-9a-f]{64}", str(value)) is not None


def _json_safe(value: Any) -> Any:
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, Mapping):
        return {str(key): _json_safe(item) for key, item in value.items()}
    if isinstance(value, (tuple, list, set, frozenset)):
        return [_json_safe(item) for item in value]
    if hasattr(value, "__dataclass_fields__"):
        return _json_safe(asdict(value))
    return value


__all__ = [
    "CLAIM_COMPILER_SCHEMA_VERSION",
    "CLAIM_LEDGER_EVENT_SCHEMA_VERSION",
    "MAX_CANONICAL_RAW_ASSERTIONS_PER_DOCUMENT",
    "BlindClaimExtractionInput",
    "BlindClaimExtractorProvider",
    "CanonicalAdjudicationProposal",
    "ClaimCompilationInput",
    "ClaimCompilationRejection",
    "ClaimCompilationResult",
    "ClaimCompilationStatus",
    "ClaimLedgerEvent",
    "ClaimLifecycleKind",
    "ClaimProviderKind",
    "ClaimProviderTrace",
    "ContractBlindClaimCompiler",
    "FixtureBlindClaimExtractorProvider",
    "FixtureCanonicalClaimAdjudicator",
    "FixtureRecipeClaimMapperProvider",
    "LegacyClaimSideBySideResult",
    "ProductionLLMRawExtractorAdapter",
    "RawExtractionBatch",
    "RecipeClaimMappingProposal",
    "RecipeMappingBatch",
    "RecipeMappingInput",
    "StrictEntityTemporalAdjudicator",
    "adapt_acquired_document_to_evidence_os",
    "adapt_legacy_claim_bundle_for_diagnostics",
    "audit_claim_compilation_results",
]
