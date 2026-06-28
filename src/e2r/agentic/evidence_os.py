"""Agentic Evidence OS v2 primitives.

This module is intentionally separate from the legacy ``evidence_claim``
compatibility layer.  The v2 path keeps extraction, adjudication, primitive
mapping, eligibility, and score contribution as distinct steps.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from enum import Enum
import hashlib
from typing import Any, Iterable, Mapping, Sequence


EVIDENCE_OS_SCHEMA_VERSION = "e2r-agentic-evidence-os-v2"
FORBIDDEN_EXTRACTOR_FIELDS = frozenset(
    {
        "verified",
        "current_score_eligible",
        "source_tier",
        "issuer_scoped",
        "candidate_primitive_id",
        "primitive_id",
        "score",
        "stage",
        "hard_break",
    }
)


class SourceType(str, Enum):
    FILING = "FILING"
    IR = "IR"
    NEWS = "NEWS"
    RESEARCH_REPORT = "RESEARCH_REPORT"
    XBRL = "XBRL"
    API = "API"
    OTHER = "OTHER"


class AnchorType(str, Enum):
    TEXT_SPAN = "TEXT_SPAN"
    TABLE_CELL = "TABLE_CELL"
    XBRL_FACT = "XBRL_FACT"
    API_RECORD = "API_RECORD"
    PDF_PAGE_REGION = "PDF_PAGE_REGION"


class VerificationStatus(str, Enum):
    UNVERIFIED = "UNVERIFIED"
    ANCHOR_VERIFIED = "ANCHOR_VERIFIED"
    SEMANTIC_VERIFIED = "SEMANTIC_VERIFIED"
    REJECTED = "REJECTED"


class TargetScopeStatus(str, Enum):
    DIRECT = "DIRECT"
    SUBSIDIARY = "SUBSIDIARY"
    PARENT = "PARENT"
    CUSTOMER = "CUSTOMER"
    SUPPLIER = "SUPPLIER"
    PARTNER = "PARTNER"
    INDUSTRY = "INDUSTRY"
    UNRELATED = "UNRELATED"
    UNKNOWN = "UNKNOWN"


class RelationToTarget(str, Enum):
    SELF = "SELF"
    SUBSIDIARY = "SUBSIDIARY"
    PARENT = "PARENT"
    CUSTOMER = "CUSTOMER"
    SUPPLIER = "SUPPLIER"
    PARTNER = "PARTNER"
    COMPETITOR = "COMPETITOR"
    INDUSTRY = "INDUSTRY"
    UNRELATED = "UNRELATED"
    UNKNOWN = "UNKNOWN"


class Directness(str, Enum):
    DIRECT = "DIRECT"
    INDIRECT = "INDIRECT"
    NOT_TARGET_SCOPED = "NOT_TARGET_SCOPED"
    UNKNOWN = "UNKNOWN"


class Polarity(str, Enum):
    POSITIVE = "POSITIVE"
    NEGATIVE = "NEGATIVE"
    NORMAL = "NORMAL"
    MIXED = "MIXED"
    CONDITIONAL = "CONDITIONAL"


class TemporalStatus(str, Enum):
    CURRENT = "CURRENT"
    EXPIRED = "EXPIRED"
    RESOLVED = "RESOLVED"
    SUPERSEDED = "SUPERSEDED"
    HISTORICAL = "HISTORICAL"
    UNKNOWN = "UNKNOWN"


class SemanticStatus(str, Enum):
    UNVERIFIED = "UNVERIFIED"
    PASS_ = "PASS"
    REJECTED = "REJECTED"
    CONTRADICTED = "CONTRADICTED"


class InvestigationStatus(str, Enum):
    COMPLETE = "COMPLETE"
    FOLLOWUP_REQUIRED = "FOLLOWUP_REQUIRED"
    EXHAUSTED = "EXHAUSTED"
    PROVIDER_FAILED = "PROVIDER_FAILED"


class MappingStatus(str, Enum):
    UNMAPPED = "UNMAPPED"
    PROPOSED = "PROPOSED"
    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"
    CONTRADICTED = "CONTRADICTED"


class SupportDirection(str, Enum):
    SUPPORT = "SUPPORT"
    COUNTER = "COUNTER"
    NEUTRAL = "NEUTRAL"


class LedgerEventType(str, Enum):
    CLAIM_CREATED = "CLAIM_CREATED"
    CLAIM_INVALIDATED = "CLAIM_INVALIDATED"
    MAPPING_ACCEPTED = "MAPPING_ACCEPTED"
    MAPPING_REJECTED = "MAPPING_REJECTED"
    CONFIRMS = "CONFIRMS"
    UPDATES = "UPDATES"
    SUPERSEDES = "SUPERSEDES"
    RESOLVES = "RESOLVES"
    CONTRADICTS = "CONTRADICTS"
    DUPLICATES = "DUPLICATES"
    REFERS_TO = "REFERS_TO"


class PrimitiveStatus(str, Enum):
    PRESENT_CURRENT = "PRESENT_CURRENT"
    ABSENT_EXPLICITLY_CONFIRMED = "ABSENT_EXPLICITLY_CONFIRMED"
    NOT_OBSERVED = "NOT_OBSERVED"
    UNKNOWN = "UNKNOWN"
    CONTRADICTED = "CONTRADICTED"
    HISTORICAL = "HISTORICAL"
    RESOLVED = "RESOLVED"


class ScoreStatus(str, Enum):
    FINAL = "FINAL"
    FINAL_WITH_NONMATERIAL_GAPS = "FINAL_WITH_NONMATERIAL_GAPS"
    PENDING_MATERIAL_GAPS = "PENDING_MATERIAL_GAPS"
    INVALID_EVIDENCE = "INVALID_EVIDENCE"
    PROVIDER_FAILURE = "PROVIDER_FAILURE"


class GateOperator(str, Enum):
    PRIMITIVE = "PRIMITIVE"
    ANY = "ANY"
    ALL = "ALL"
    K_OF_N = "K_OF_N"


class BaseStage(str, Enum):
    STAGE_0 = "0"
    STAGE_1 = "1"
    STAGE_2 = "2"
    STAGE_2_ACTIONABLE = "2-Actionable"
    YELLOW = "3-Yellow"
    GREEN = "3-Green"
    RED = "3-Red"


class StageInvestigationStatus(str, Enum):
    COMPLETE = "COMPLETE"
    PENDING = "PENDING"
    EXHAUSTED = "EXHAUSTED"
    CONTRADICTED = "CONTRADICTED"
    FAILED = "FAILED"


class TransitionOverlay(str, Enum):
    NONE = "NONE"
    STAGE_4A = "4A"
    STAGE_4B = "4B"
    STAGE_4C = "4C"


class RunComparisonClass(str, Enum):
    EXACT_REPLAY = "EXACT_REPLAY"
    EVIDENCE_UPDATE = "EVIDENCE_UPDATE"
    EXTRACTION_UPDATE = "EXTRACTION_UPDATE"
    SCORING_UPDATE = "SCORING_UPDATE"
    NON_COMPARABLE = "NON_COMPARABLE"


@dataclass(frozen=True)
class EvidenceDocument:
    document_id: str
    canonical_url: str | None
    source_type: SourceType
    source_name: str
    content_hash: str
    published_at: date | datetime | None
    available_at: date | datetime | None = None
    fetched_at: date | datetime | None = None
    revision_id: str | None = None
    parser_version: str | None = None
    source_lineage_id: str | None = None
    source_proxy_only: bool = False
    score_block_reasons: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.document_id.strip():
            raise ValueError("document_id must be non-empty")
        if not self.source_name.strip():
            raise ValueError("source_name must be non-empty")
        if not self.content_hash.strip():
            raise ValueError("content_hash must be non-empty")
        object.__setattr__(
            self,
            "score_block_reasons",
            tuple(dict.fromkeys(str(item).strip() for item in self.score_block_reasons if str(item).strip())),
        )

    @classmethod
    def from_text(
        cls,
        *,
        text: str,
        canonical_url: str | None,
        source_type: SourceType | str,
        source_name: str,
        published_at: date | datetime | None,
        available_at: date | datetime | None = None,
        fetched_at: date | datetime | None = None,
        revision_id: str | None = None,
        parser_version: str | None = None,
        source_lineage_id: str | None = None,
        source_proxy_only: bool = False,
        score_block_reasons: Sequence[str] = (),
    ) -> "EvidenceDocument":
        content_hash = _hash_text(text)
        document_id = f"DOC-{content_hash[:20]}"
        return cls(
            document_id=document_id,
            canonical_url=canonical_url,
            source_type=SourceType(source_type),
            source_name=source_name,
            content_hash=content_hash,
            published_at=published_at,
            available_at=available_at,
            fetched_at=fetched_at,
            revision_id=revision_id,
            parser_version=parser_version,
            source_lineage_id=source_lineage_id,
            source_proxy_only=source_proxy_only,
            score_block_reasons=tuple(score_block_reasons),
        )

    def published_date(self) -> date | None:
        return _as_date(self.published_at)

    def available_date(self) -> date | None:
        return _as_date(self.available_at)


@dataclass(frozen=True)
class EvidenceAnchor:
    anchor_id: str
    document_id: str
    anchor_type: AnchorType
    locator: str
    exact_text: str = ""
    normalized_value: Any | None = None
    content_hash: str | None = None
    anchor_verified: bool = False

    def __post_init__(self) -> None:
        if not self.anchor_id.strip():
            raise ValueError("anchor_id must be non-empty")
        if not self.document_id.strip():
            raise ValueError("document_id must be non-empty")
        if not self.locator.strip():
            raise ValueError("locator must be non-empty")

    @classmethod
    def text_span(
        cls,
        *,
        document: EvidenceDocument,
        document_text: str,
        exact_text: str,
        locator: str | None = None,
    ) -> "EvidenceAnchor":
        clean_quote = exact_text.strip()
        if not clean_quote:
            raise ValueError("exact_text must be non-empty for TEXT_SPAN anchors")
        start = document_text.find(clean_quote)
        verified = start >= 0 and _hash_text(document_text) == document.content_hash
        span_locator = locator or (f"char:{start}:{start + len(clean_quote)}" if start >= 0 else "char:not-found")
        anchor_id = _stable_id("ANCH", document.document_id, AnchorType.TEXT_SPAN.value, span_locator, clean_quote)
        return cls(
            anchor_id=anchor_id,
            document_id=document.document_id,
            anchor_type=AnchorType.TEXT_SPAN,
            locator=span_locator,
            exact_text=clean_quote,
            content_hash=_hash_text(clean_quote),
            anchor_verified=verified,
        )

    @classmethod
    def structured(
        cls,
        *,
        document: EvidenceDocument,
        anchor_type: AnchorType | str,
        locator: str,
        normalized_value: Any,
        exact_text: str = "",
        anchor_verified: bool = True,
    ) -> "EvidenceAnchor":
        normalized_text = _normalise_value(normalized_value)
        anchor_type_value = AnchorType(anchor_type)
        anchor_id = _stable_id("ANCH", document.document_id, anchor_type_value.value, locator, normalized_text)
        return cls(
            anchor_id=anchor_id,
            document_id=document.document_id,
            anchor_type=anchor_type_value,
            locator=locator,
            exact_text=exact_text.strip(),
            normalized_value=normalized_value,
            content_hash=_hash_text(normalized_text),
            anchor_verified=anchor_verified,
        )


@dataclass(frozen=True)
class EntityRecord:
    entity_id: str
    legal_name: str
    aliases: tuple[str, ...] = ()
    ticker: str | None = None
    exchange: str | None = None
    dart_corp_code: str | None = None
    cik: str | None = None
    parent_entity_id: str | None = None
    subsidiary_entity_ids: tuple[str, ...] = ()
    historical_names: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.entity_id.strip():
            raise ValueError("entity_id must be non-empty")
        if not self.legal_name.strip():
            raise ValueError("legal_name must be non-empty")

    def names(self) -> tuple[str, ...]:
        return tuple(dict.fromkeys((self.legal_name, *self.aliases, *self.historical_names)))


@dataclass(frozen=True)
class EntityRelation:
    subject_entity_id: str
    target_entity_id: str
    relation_to_target: RelationToTarget
    directness: Directness
    object_entity_ids: tuple[str, ...] = ()
    segment_scope: str | None = None
    product_scope: str | None = None


@dataclass(frozen=True)
class EntityRegistry:
    entities: Mapping[str, EntityRecord] = field(default_factory=dict)

    def entity(self, entity_id: str) -> EntityRecord | None:
        return self.entities.get(entity_id)

    def resolve_text(self, text: str) -> EntityRecord | None:
        needle = _norm_text(text)
        if not needle:
            return None
        for entity in self.entities.values():
            for name in entity.names():
                if _norm_text(name) == needle:
                    return entity
        return None

    def relation(
        self,
        *,
        subject_entity_id: str,
        target_entity_id: str,
        fallback: RelationToTarget = RelationToTarget.UNKNOWN,
    ) -> EntityRelation:
        if subject_entity_id == target_entity_id:
            return EntityRelation(
                subject_entity_id=subject_entity_id,
                target_entity_id=target_entity_id,
                relation_to_target=RelationToTarget.SELF,
                directness=Directness.DIRECT,
            )
        subject = self.entity(subject_entity_id)
        target = self.entity(target_entity_id)
        if subject and subject.parent_entity_id == target_entity_id:
            return EntityRelation(subject_entity_id, target_entity_id, RelationToTarget.SUBSIDIARY, Directness.DIRECT)
        if target and target.parent_entity_id == subject_entity_id:
            return EntityRelation(subject_entity_id, target_entity_id, RelationToTarget.PARENT, Directness.DIRECT)
        if subject and target_entity_id in subject.subsidiary_entity_ids:
            return EntityRelation(subject_entity_id, target_entity_id, RelationToTarget.PARENT, Directness.DIRECT)
        if target and subject_entity_id in target.subsidiary_entity_ids:
            return EntityRelation(subject_entity_id, target_entity_id, RelationToTarget.SUBSIDIARY, Directness.DIRECT)
        return EntityRelation(
            subject_entity_id=subject_entity_id,
            target_entity_id=target_entity_id,
            relation_to_target=fallback,
            directness=Directness.UNKNOWN if fallback == RelationToTarget.UNKNOWN else Directness.INDIRECT,
        )


@dataclass(frozen=True)
class RawAssertion:
    raw_assertion_id: str
    anchor_id: str
    subject_text: str
    predicate: str
    object_text: str = ""
    value: Any | None = None
    unit: str | None = None
    polarity_proposal: Polarity = Polarity.CONDITIONAL
    modality: str | None = None
    certainty: str | None = None
    event_date_text: str | None = None
    effective_period_text: str | None = None
    exact_quote: str = ""
    span: tuple[int, int] | None = None
    related_entity_texts: tuple[str, ...] = ()
    extractor_model: str | None = None
    extractor_prompt_hash: str | None = None

    def __post_init__(self) -> None:
        if not self.raw_assertion_id.strip():
            raise ValueError("raw_assertion_id must be non-empty")
        if not self.anchor_id.strip():
            raise ValueError("anchor_id must be non-empty")
        if not self.subject_text.strip():
            raise ValueError("subject_text must be non-empty")
        if not self.predicate.strip():
            raise ValueError("predicate must be non-empty")


@dataclass(frozen=True)
class AdjudicatedClaim:
    claim_id: str
    raw_assertion_id: str
    subject_entity_id: str
    target_entity_id: str
    relation_to_target: RelationToTarget
    directness: Directness
    verification_status: VerificationStatus
    target_scope_status: TargetScopeStatus
    polarity: Polarity
    temporal_status: TemporalStatus
    semantic_status: SemanticStatus
    investigation_status: InvestigationStatus
    event_date: date | None = None
    effective_start: date | None = None
    effective_end: date | None = None
    superseded_by_claim_ids: tuple[str, ...] = ()
    contradiction_group_id: str | None = None
    adjudication_rationale: str = ""
    source_document_id: str = ""
    source_anchor_id: str = ""
    source_assertion_id: str = ""

    def __post_init__(self) -> None:
        if not self.claim_id.strip():
            raise ValueError("claim_id must be non-empty")
        if not self.raw_assertion_id.strip():
            raise ValueError("raw_assertion_id must be non-empty")
        if not self.subject_entity_id.strip():
            raise ValueError("subject_entity_id must be non-empty")
        if not self.target_entity_id.strip():
            raise ValueError("target_entity_id must be non-empty")

    @classmethod
    def from_raw(
        cls,
        *,
        raw: RawAssertion,
        document: EvidenceDocument,
        anchor: EvidenceAnchor,
        subject_entity_id: str,
        target_entity_id: str,
        relation_to_target: RelationToTarget,
        directness: Directness,
        verification_status: VerificationStatus,
        target_scope_status: TargetScopeStatus,
        polarity: Polarity,
        temporal_status: TemporalStatus,
        semantic_status: SemanticStatus,
        investigation_status: InvestigationStatus,
        event_date: date | None = None,
        effective_start: date | None = None,
        effective_end: date | None = None,
        superseded_by_claim_ids: Sequence[str] = (),
        contradiction_group_id: str | None = None,
        adjudication_rationale: str = "",
        extraction_schema_version: str = EVIDENCE_OS_SCHEMA_VERSION,
    ) -> "AdjudicatedClaim":
        assertion_fingerprint = _raw_assertion_fingerprint(raw, anchor=anchor)
        claim_id = stable_claim_id(
            document_hash=document.content_hash,
            anchor_locator=anchor.locator,
            subject_entity_id=subject_entity_id,
            predicate=raw.predicate,
            value=raw.value if raw.value is not None else raw.object_text,
            assertion_fingerprint=assertion_fingerprint,
            extraction_schema_version=extraction_schema_version,
        )
        source_assertion_id = stable_source_assertion_id(
            source_anchor_id=anchor.anchor_id,
            subject_entity_id=subject_entity_id,
            target_entity_id=target_entity_id,
            assertion_fingerprint=assertion_fingerprint,
        )
        return cls(
            claim_id=claim_id,
            raw_assertion_id=raw.raw_assertion_id,
            subject_entity_id=subject_entity_id,
            target_entity_id=target_entity_id,
            relation_to_target=relation_to_target,
            directness=directness,
            verification_status=verification_status,
            target_scope_status=target_scope_status,
            polarity=polarity,
            temporal_status=temporal_status,
            semantic_status=semantic_status,
            investigation_status=investigation_status,
            event_date=event_date,
            effective_start=effective_start,
            effective_end=effective_end,
            superseded_by_claim_ids=tuple(superseded_by_claim_ids),
            contradiction_group_id=contradiction_group_id,
            adjudication_rationale=adjudication_rationale,
            source_document_id=document.document_id,
            source_anchor_id=anchor.anchor_id,
            source_assertion_id=source_assertion_id,
        )


@dataclass(frozen=True)
class PrimitiveMappingProposal:
    mapping_id: str
    claim_id: str
    archetype_id: str
    primitive_id: str
    support_direction: SupportDirection
    mapping_status: MappingStatus
    rationale: str
    contract_rule_id: str | None = None
    counter_primitive_ids: tuple[str, ...] = ()

    @classmethod
    def build(
        cls,
        *,
        claim_id: str,
        archetype_id: str,
        primitive_id: str,
        support_direction: SupportDirection,
        mapping_status: MappingStatus,
        rationale: str,
        contract_rule_id: str | None = None,
        counter_primitive_ids: Sequence[str] = (),
    ) -> "PrimitiveMappingProposal":
        mapping_id = _stable_id(
            "MAP",
            claim_id,
            archetype_id,
            primitive_id,
            support_direction.value,
        )
        return cls(
            mapping_id=mapping_id,
            claim_id=claim_id,
            archetype_id=archetype_id,
            primitive_id=primitive_id,
            support_direction=support_direction,
            mapping_status=mapping_status,
            rationale=rationale,
            contract_rule_id=contract_rule_id,
            counter_primitive_ids=tuple(counter_primitive_ids),
        )


@dataclass(frozen=True)
class LedgerEvent:
    event_id: str
    event_type: LedgerEventType
    from_id: str
    to_id: str | None = None
    reason: str = ""
    created_at: datetime | None = None

    @classmethod
    def build(
        cls,
        *,
        event_type: LedgerEventType,
        from_id: str,
        to_id: str | None = None,
        reason: str = "",
        created_at: datetime | None = None,
    ) -> "LedgerEvent":
        event_id = _stable_id("LEDGER", event_type.value, from_id, to_id or "", reason)
        return cls(
            event_id=event_id,
            event_type=event_type,
            from_id=from_id,
            to_id=to_id,
            reason=reason,
            created_at=created_at,
        )


@dataclass
class AppendOnlyEvidenceLedger:
    claims: dict[str, AdjudicatedClaim] = field(default_factory=dict)
    mappings: dict[str, PrimitiveMappingProposal] = field(default_factory=dict)
    events: list[LedgerEvent] = field(default_factory=list)

    def append_claim(self, claim: AdjudicatedClaim) -> None:
        existing = self.claims.get(claim.claim_id)
        if existing is not None:
            if _claim_material_identity(existing) != _claim_material_identity(claim):
                raise ValueError(f"claim_id collision with different claim: {claim.claim_id}")
            return
        self.claims[claim.claim_id] = claim
        event = LedgerEvent.build(event_type=LedgerEventType.CLAIM_CREATED, from_id=claim.claim_id)
        if event.event_id not in {item.event_id for item in self.events}:
            self.events.append(event)

    def append_mapping(self, mapping: PrimitiveMappingProposal) -> None:
        if mapping.claim_id not in self.claims:
            raise ValueError(f"mapping references unknown claim: {mapping.claim_id}")
        existing = self.mappings.get(mapping.mapping_id)
        if existing is not None:
            if _mapping_material_identity(existing) != _mapping_material_identity(mapping):
                raise ValueError(f"mapping_id collision with different mapping: {mapping.mapping_id}")
            return
        self.mappings[mapping.mapping_id] = mapping
        event_type = (
            LedgerEventType.MAPPING_ACCEPTED
            if mapping.mapping_status == MappingStatus.ACCEPTED
            else LedgerEventType.MAPPING_REJECTED
        )
        event = LedgerEvent.build(event_type=event_type, from_id=mapping.claim_id, to_id=mapping.mapping_id)
        if event.event_id not in {item.event_id for item in self.events}:
            self.events.append(event)

    def append_event(self, event: LedgerEvent) -> None:
        if event.event_id not in {item.event_id for item in self.events}:
            self.events.append(event)

    def invalidate_claim(self, claim_id: str, *, reason: str) -> None:
        if claim_id not in self.claims:
            raise ValueError(f"unknown claim: {claim_id}")
        self.append_event(
            LedgerEvent.build(
                event_type=LedgerEventType.CLAIM_INVALIDATED,
                from_id=claim_id,
                reason=reason,
            )
        )

    def claim_is_invalidated(self, claim_id: str) -> bool:
        return any(
            event.event_type == LedgerEventType.CLAIM_INVALIDATED and event.from_id == claim_id
            for event in self.events
        )


@dataclass(frozen=True)
class PrimitiveStateV2:
    primitive_id: str
    status: PrimitiveStatus
    normalized_value: Any | None = None
    support_claim_ids: tuple[str, ...] = ()
    counter_claim_ids: tuple[str, ...] = ()
    support_source_family_ids: tuple[str, ...] = ()
    counter_source_family_ids: tuple[str, ...] = ()
    confidence_for_review: float = 0.0
    freshness_days: int | None = None
    materiality_remaining_points: float = 0.0
    support_mapping_ids: tuple[str, ...] = ()
    counter_mapping_ids: tuple[str, ...] = ()


@dataclass(frozen=True)
class ScoreContributionV2:
    contribution_id: str
    component_key: str
    criterion_id: str
    raw_points: float
    max_points: float
    support_claim_ids: tuple[str, ...]
    counter_claim_ids: tuple[str, ...] = ()
    mapping_ids: tuple[str, ...] = ()
    source_family_ids: tuple[str, ...] = ()
    cap_reason: str | None = None
    rationale: str = ""

    def __post_init__(self) -> None:
        if self.raw_points != 0 and not self.support_claim_ids:
            raise ValueError("nonzero ScoreContributionV2 requires support_claim_ids")

    @classmethod
    def build(
        cls,
        *,
        component_key: str,
        criterion_id: str,
        raw_points: float,
        max_points: float,
        support_claim_ids: Sequence[str],
        counter_claim_ids: Sequence[str] = (),
        mapping_ids: Sequence[str] = (),
        source_family_ids: Sequence[str] = (),
        cap_reason: str | None = None,
        rationale: str = "",
    ) -> "ScoreContributionV2":
        contribution_id = _stable_id(
            "SCON",
            component_key,
            criterion_id,
            _normalise_value(raw_points),
            ",".join(support_claim_ids),
            ",".join(mapping_ids),
        )
        return cls(
            contribution_id=contribution_id,
            component_key=component_key,
            criterion_id=criterion_id,
            raw_points=raw_points,
            max_points=max_points,
            support_claim_ids=tuple(support_claim_ids),
            counter_claim_ids=tuple(counter_claim_ids),
            mapping_ids=tuple(mapping_ids),
            source_family_ids=tuple(source_family_ids),
            cap_reason=cap_reason,
            rationale=rationale,
        )


@dataclass(frozen=True)
class ScoreEligibilityResult:
    eligible: bool
    reasons: tuple[str, ...] = ()


def derive_score_eligibility(
    *,
    document: EvidenceDocument,
    anchor: EvidenceAnchor,
    claim: AdjudicatedClaim,
    mapping: PrimitiveMappingProposal,
    as_of_date: date,
    allowed_target_scopes: Sequence[TargetScopeStatus] = (TargetScopeStatus.DIRECT,),
    allowed_directness: Sequence[Directness] = (Directness.DIRECT,),
    allowed_temporal_statuses: Sequence[TemporalStatus] = (TemporalStatus.CURRENT,),
    require_source_quorum: bool = False,
    source_quorum_satisfied: bool = True,
    contradiction_resolved: bool = True,
) -> ScoreEligibilityResult:
    reasons: list[str] = []
    if not anchor.anchor_verified:
        reasons.append("anchor_not_verified")
    if document.source_proxy_only:
        reasons.append("source_proxy_only_not_score_eligible")
    for reason in document.score_block_reasons:
        reasons.append(f"document_score_block:{reason}")
    published = document.published_date()
    if published is None:
        reasons.append("source_date_missing")
    elif published > as_of_date:
        reasons.append("future_source")
    available = document.available_date()
    if available is not None and available > as_of_date:
        reasons.append("future_available_at")
    if claim.event_date is not None and claim.event_date > as_of_date:
        reasons.append("future_event")
    if claim.verification_status != VerificationStatus.SEMANTIC_VERIFIED:
        reasons.append("semantic_not_verified")
    if claim.semantic_status != SemanticStatus.PASS_:
        reasons.append("semantic_rejected")
    if claim.target_scope_status not in tuple(allowed_target_scopes):
        reasons.append(f"target_scope_not_allowed:{claim.target_scope_status.value}")
    if claim.directness not in tuple(allowed_directness):
        reasons.append(f"target_not_direct:{claim.directness.value}")
    if claim.temporal_status not in tuple(allowed_temporal_statuses):
        reasons.append(f"temporal_not_allowed:{claim.temporal_status.value}")
    if mapping.mapping_status != MappingStatus.ACCEPTED:
        reasons.append(f"mapping_not_accepted:{mapping.mapping_status.value}")
    if mapping.claim_id != claim.claim_id:
        reasons.append("mapping_claim_mismatch")
    if require_source_quorum and not source_quorum_satisfied:
        reasons.append("source_quorum_not_satisfied")
    if not contradiction_resolved:
        reasons.append("contradiction_unresolved")
    return ScoreEligibilityResult(eligible=not reasons, reasons=tuple(reasons))


@dataclass(frozen=True)
class ScoreInterval:
    verified_score: float
    potential_score_upper_bound: float
    unresolved_hard_break_candidate: bool = False
    provider_failed: bool = False
    invalid_evidence: bool = False

    def status_for_thresholds(self, *, material_stage_boundary: float) -> ScoreStatus:
        if self.invalid_evidence:
            return ScoreStatus.INVALID_EVIDENCE
        if self.provider_failed:
            return ScoreStatus.PROVIDER_FAILURE
        if self.unresolved_hard_break_candidate:
            return ScoreStatus.PENDING_MATERIAL_GAPS
        crosses_boundary = self.verified_score < material_stage_boundary <= self.potential_score_upper_bound
        if crosses_boundary:
            return ScoreStatus.PENDING_MATERIAL_GAPS
        if self.potential_score_upper_bound > self.verified_score:
            return ScoreStatus.FINAL_WITH_NONMATERIAL_GAPS
        return ScoreStatus.FINAL


@dataclass(frozen=True)
class RunFingerprint:
    commit_sha: str
    config_hash: str
    as_of_date: date
    source_corpus_hash: str
    query_set_hash: str
    cache_snapshot_id: str
    llm_model: str
    llm_prompt_hash: str
    llm_schema_version: str
    scoring_schema_version: str
    stage_schema_version: str


def classify_run_comparison(before: RunFingerprint, after: RunFingerprint) -> RunComparisonClass:
    code_same = before.commit_sha == after.commit_sha and before.config_hash == after.config_hash
    corpus_same = before.source_corpus_hash == after.source_corpus_hash and before.query_set_hash == after.query_set_hash
    extraction_same = before.llm_model == after.llm_model and before.llm_prompt_hash == after.llm_prompt_hash and before.llm_schema_version == after.llm_schema_version
    scoring_same = (
        before.scoring_schema_version == after.scoring_schema_version
        and before.stage_schema_version == after.stage_schema_version
    )
    if code_same and corpus_same and extraction_same and scoring_same:
        return RunComparisonClass.EXACT_REPLAY
    if code_same and extraction_same and scoring_same and not corpus_same:
        return RunComparisonClass.EVIDENCE_UPDATE
    if code_same and corpus_same and not extraction_same and scoring_same:
        return RunComparisonClass.EXTRACTION_UPDATE
    if code_same and corpus_same and extraction_same and not scoring_same:
        return RunComparisonClass.SCORING_UPDATE
    return RunComparisonClass.NON_COMPARABLE


@dataclass(frozen=True)
class SourceAcquisitionTask:
    task_id: str
    target_entity_id: str
    primitive_gap: str
    preferred_source_classes: tuple[str, ...]
    date_window: tuple[date | None, date | None] | None
    required_source_tier: str | None
    max_queries: int
    max_candidates: int
    max_fetches: int
    stop_condition: str
    fallback_policy: str
    source_quorum_rule_id: str | None = None
    source_quorum_min_official: int = 0
    source_quorum_min_independent_tier2: int = 0
    target_aliases: tuple[str, ...] = field(default_factory=tuple)
    primitive_aliases: tuple[str, ...] = field(default_factory=tuple)

    def __post_init__(self) -> None:
        if not self.task_id.strip():
            raise ValueError("task_id must be non-empty")
        if not self.target_entity_id.strip():
            raise ValueError("target_entity_id must be non-empty")
        if not self.primitive_gap.strip():
            raise ValueError("primitive_gap must be non-empty")
        object.__setattr__(
            self,
            "target_aliases",
            tuple(dict.fromkeys(str(item).strip() for item in self.target_aliases if str(item).strip())),
        )
        object.__setattr__(
            self,
            "primitive_aliases",
            tuple(dict.fromkeys(str(item).strip() for item in self.primitive_aliases if str(item).strip())),
        )
        for field_name in ("max_queries", "max_candidates", "max_fetches"):
            value = getattr(self, field_name)
            if value is None or value <= 0:
                raise ValueError(f"{field_name} must be a positive bounded integer")
        if not self.stop_condition.strip():
            raise ValueError("stop_condition must be non-empty")
        if not self.fallback_policy.strip():
            raise ValueError("fallback_policy must be non-empty")
        if self.source_quorum_min_official < 0:
            raise ValueError("source_quorum_min_official must be non-negative")
        if self.source_quorum_min_independent_tier2 < 0:
            raise ValueError("source_quorum_min_independent_tier2 must be non-negative")
        if self.source_quorum_rule_id is not None:
            object.__setattr__(self, "source_quorum_rule_id", self.source_quorum_rule_id.strip() or None)


def validate_operational_search_bounds(
    *,
    top_results: int | None,
    retry_max: int | None,
    max_fetches: int | None = None,
) -> None:
    if retry_max is None:
        raise ValueError("operational retry_max must be bounded")
    if top_results is None and max_fetches is None:
        raise ValueError("operational max_fetches must be bounded when top_results is unbounded")
    if top_results is not None and top_results <= 0:
        raise ValueError("operational top_results must be positive")
    if retry_max <= 0:
        raise ValueError("operational retry_max must be positive")
    if max_fetches is not None and max_fetches <= 0:
        raise ValueError("operational max_fetches must be positive")


@dataclass(frozen=True)
class GateExpression:
    operator: GateOperator
    primitive_id: str | None = None
    children: tuple["GateExpression", ...] = ()
    k: int | None = None

    @classmethod
    def primitive(cls, primitive_id: str) -> "GateExpression":
        if not primitive_id.strip():
            raise ValueError("primitive_id must be non-empty")
        return cls(operator=GateOperator.PRIMITIVE, primitive_id=primitive_id.strip())

    @classmethod
    def any(cls, children: Sequence["GateExpression"]) -> "GateExpression":
        return cls(operator=GateOperator.ANY, children=_clean_children(children))

    @classmethod
    def all(cls, children: Sequence["GateExpression"]) -> "GateExpression":
        return cls(operator=GateOperator.ALL, children=_clean_children(children))

    @classmethod
    def k_of_n(cls, *, k: int, children: Sequence["GateExpression"]) -> "GateExpression":
        if k <= 0:
            raise ValueError("k must be positive")
        clean = _clean_children(children)
        if k > len(clean):
            raise ValueError("k cannot exceed child count")
        return cls(operator=GateOperator.K_OF_N, children=clean, k=k)

    def evaluate(self, present_primitives: Iterable[str]) -> bool:
        present = {str(item).strip() for item in present_primitives if str(item).strip()}
        if self.operator == GateOperator.PRIMITIVE:
            return bool(self.primitive_id and self.primitive_id in present)
        child_results = [child.evaluate(present) for child in self.children]
        if self.operator == GateOperator.ANY:
            return any(child_results)
        if self.operator == GateOperator.ALL:
            return all(child_results)
        if self.operator == GateOperator.K_OF_N:
            return sum(1 for result in child_results if result) >= (self.k or 0)
        raise ValueError(f"unsupported gate operator: {self.operator}")

    def primitive_ids(self) -> tuple[str, ...]:
        if self.operator == GateOperator.PRIMITIVE:
            return (self.primitive_id,) if self.primitive_id else ()
        ids: list[str] = []
        for child in self.children:
            ids.extend(child.primitive_ids())
        return tuple(dict.fromkeys(ids))


@dataclass(frozen=True)
class SourceFamilyEvidence:
    source_family_id: str
    document_id: str
    source_type: SourceType
    tier: int
    official: bool = False
    independent: bool = True
    underlying_event_id: str | None = None

    def __post_init__(self) -> None:
        if not self.source_family_id.strip():
            raise ValueError("source_family_id must be non-empty")
        if not self.document_id.strip():
            raise ValueError("document_id must be non-empty")
        if self.tier <= 0:
            raise ValueError("tier must be positive")


@dataclass(frozen=True)
class SourceQuorumRule:
    min_official: int = 0
    min_independent_tier2: int = 0

    def satisfied(self, families: Sequence[SourceFamilyEvidence]) -> bool:
        deduped = dedupe_source_family_evidence(families)
        official_count = sum(1 for family in deduped if family.official)
        independent_tier2_count = sum(1 for family in deduped if family.independent and family.tier <= 2)
        return official_count >= self.min_official and independent_tier2_count >= self.min_independent_tier2


@dataclass(frozen=True)
class FreshnessPolicy:
    primitive_id: str
    max_age_days: int | None = None
    supersession_rule: str | None = None
    closure_conditions: tuple[str, ...] = ()
    authoritative_followup_sources: tuple[SourceType, ...] = ()


@dataclass(frozen=True)
class EvidenceContractV2:
    archetype_id: str
    required_primitives: tuple[str, ...]
    green_gate: GateExpression
    allowed_target_scopes: tuple[TargetScopeStatus, ...] = (TargetScopeStatus.DIRECT,)
    allowed_directness: tuple[Directness, ...] = (Directness.DIRECT,)
    alternative_primitives: Mapping[str, tuple[str, ...]] = field(default_factory=dict)
    primitive_aliases: Mapping[str, tuple[str, ...]] = field(default_factory=dict)
    route_hints: Mapping[str, tuple[str, ...]] = field(default_factory=dict)
    score_rubric: Mapping[str, tuple[str, ...]] = field(default_factory=dict)
    source_quorum: Mapping[str, SourceQuorumRule] = field(default_factory=dict)
    freshness: Mapping[str, FreshnessPolicy] = field(default_factory=dict)
    guard_modes: Mapping[str, str] = field(default_factory=dict)
    aggregation_rules: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.archetype_id.strip():
            raise ValueError("archetype_id must be non-empty")
        if not self.required_primitives:
            raise ValueError("required_primitives must be non-empty")
        if not self.allowed_target_scopes:
            raise ValueError("allowed_target_scopes must be non-empty")
        if not self.allowed_directness:
            raise ValueError("allowed_directness must be non-empty")
        object.__setattr__(self, "allowed_target_scopes", tuple(dict.fromkeys(self.allowed_target_scopes)))
        object.__setattr__(self, "allowed_directness", tuple(dict.fromkeys(self.allowed_directness)))
        unknown_gate_primitives = set(self.green_gate.primitive_ids()) - set(self.required_primitives)
        alternative_values = {item for values in self.alternative_primitives.values() for item in values}
        if unknown_gate_primitives - alternative_values:
            raise ValueError(f"green_gate references unknown primitives: {sorted(unknown_gate_primitives)}")
        allowed_primitives = set(self.required_primitives) | set(self.alternative_primitives) | alternative_values
        unknown_score_primitives = {
            primitive
            for primitives in self.score_rubric.values()
            for primitive in primitives
            if primitive not in allowed_primitives
        }
        if unknown_score_primitives:
            raise ValueError(f"score_rubric references unknown primitives: {sorted(unknown_score_primitives)}")
        unknown_alias_primitives = set(self.primitive_aliases) - allowed_primitives
        if unknown_alias_primitives:
            raise ValueError(f"primitive_aliases references unknown primitives: {sorted(unknown_alias_primitives)}")
        allowed_guard_modes = {
            "block_if_current",
            "block_green_if_current",
            "hard_break_if_current_and_quorum",
        }
        unknown_guard_modes = {
            mode
            for mode in self.guard_modes.values()
            if str(mode).strip() not in allowed_guard_modes
        }
        if unknown_guard_modes:
            raise ValueError(f"guard_modes contains unknown modes: {sorted(unknown_guard_modes)}")
        allowed_contract_primitives = allowed_primitives | set(self.guard_modes)
        unknown_freshness_primitives = set(self.freshness) - allowed_contract_primitives
        if unknown_freshness_primitives:
            raise ValueError(f"freshness references unknown primitives: {sorted(unknown_freshness_primitives)}")
        allowed_quorum_scopes = {"hard_break", "score_contribution", "green_gate"}
        unknown_quorum_keys = set(self.source_quorum) - allowed_contract_primitives - allowed_quorum_scopes
        if unknown_quorum_keys:
            raise ValueError(f"source_quorum references unknown primitives or scopes: {sorted(unknown_quorum_keys)}")

    def green_gate_satisfied(self, present_primitives: Iterable[str]) -> bool:
        expanded = set(str(item).strip() for item in present_primitives if str(item).strip())
        for canonical, alternatives in self.alternative_primitives.items():
            if canonical in expanded:
                continue
            if any(alternative in expanded for alternative in alternatives):
                expanded.add(canonical)
        return self.green_gate.evaluate(expanded)


@dataclass(frozen=True)
class StageDecisionV2:
    base_stage: BaseStage
    investigation_status: StageInvestigationStatus
    transition_overlay: TransitionOverlay = TransitionOverlay.NONE
    has_prior_live_thesis: bool = False

    def __post_init__(self) -> None:
        if self.transition_overlay == TransitionOverlay.STAGE_4C and not self.has_prior_live_thesis:
            object.__setattr__(self, "base_stage", BaseStage.RED)
            object.__setattr__(self, "transition_overlay", TransitionOverlay.NONE)

    def canonical_stage(self) -> str:
        if self.transition_overlay == TransitionOverlay.NONE:
            return self.base_stage.value
        if not self.has_prior_live_thesis and self.transition_overlay == TransitionOverlay.STAGE_4C:
            return BaseStage.RED.value
        return self.transition_overlay.value


def source_family_id_for_document(document: EvidenceDocument) -> str:
    return document.source_lineage_id or document.document_id


def source_family_from_document(
    document: EvidenceDocument,
    *,
    tier: int,
    official: bool = False,
    independent: bool = True,
    underlying_event_id: str | None = None,
) -> SourceFamilyEvidence:
    return SourceFamilyEvidence(
        source_family_id=source_family_id_for_document(document),
        document_id=document.document_id,
        source_type=document.source_type,
        tier=tier,
        official=official,
        independent=independent,
        underlying_event_id=underlying_event_id,
    )


def dedupe_source_family_evidence(families: Sequence[SourceFamilyEvidence]) -> tuple[SourceFamilyEvidence, ...]:
    best_by_family: dict[str, SourceFamilyEvidence] = {}
    for family in families:
        existing = best_by_family.get(family.source_family_id)
        if existing is None or _family_rank(family) < _family_rank(existing):
            best_by_family[family.source_family_id] = family
    return tuple(best_by_family[key] for key in sorted(best_by_family))


PROMPT_INJECTION_MARKERS = (
    "ignore previous instructions",
    "disregard previous instructions",
    "system prompt",
    "developer message",
    "tool call",
    "call this url",
    "open this url",
    "이전 지시를 무시",
    "시스템 프롬프트",
    "도구 호출",
)


def prompt_injection_markers(text: str) -> tuple[str, ...]:
    lowered = str(text or "").lower()
    return tuple(marker for marker in PROMPT_INJECTION_MARKERS if marker.lower() in lowered)


def stable_claim_id(
    *,
    document_hash: str,
    anchor_locator: str,
    subject_entity_id: str,
    predicate: str,
    value: Any,
    assertion_fingerprint: str = "",
    extraction_schema_version: str = EVIDENCE_OS_SCHEMA_VERSION,
) -> str:
    return _stable_id(
        "CLM",
        document_hash,
        anchor_locator,
        assertion_fingerprint,
        _norm_text(subject_entity_id),
        _norm_text(predicate),
        _normalise_value(value),
        extraction_schema_version,
    )


def stable_source_evidence_id(
    *,
    archetype_id: str,
    primitive_id: str,
    support_direction: SupportDirection | str,
    subject_entity_id: str,
    target_entity_id: str,
    source_anchor_id: str,
) -> str:
    direction = support_direction.value if isinstance(support_direction, SupportDirection) else str(support_direction)
    return _stable_id(
        "SRC",
        _norm_text(archetype_id),
        _norm_text(primitive_id),
        _norm_text(direction),
        _norm_text(subject_entity_id),
        _norm_text(target_entity_id),
        _norm_text(source_anchor_id),
    )


def stable_source_assertion_id(
    *,
    source_anchor_id: str,
    subject_entity_id: str,
    target_entity_id: str,
    assertion_fingerprint: str,
) -> str:
    return _stable_id(
        "SASSERT",
        _norm_text(source_anchor_id),
        _norm_text(subject_entity_id),
        _norm_text(target_entity_id),
        _norm_text(assertion_fingerprint),
    )


def _raw_assertion_fingerprint(raw: RawAssertion, *, anchor: EvidenceAnchor | None = None) -> str:
    sentence = _canonical_anchor_sentence(anchor.exact_text if anchor else "", raw.exact_quote)
    if sentence:
        return _stable_id("RAWFP", raw.anchor_id, sentence)
    span = ",".join(str(item) for item in raw.span) if raw.span else ""
    quote = _canonical_claim_quote(raw.exact_quote)
    if not span and not quote:
        quote = _normalise_value(raw.value if raw.value is not None else raw.object_text)
    return _stable_id(
        "RAWFP",
        raw.anchor_id,
        span,
        quote,
    )


def forbidden_extractor_field_overlap(fields: Iterable[str]) -> tuple[str, ...]:
    return tuple(sorted(FORBIDDEN_EXTRACTOR_FIELDS & {str(field) for field in fields}))


def _claim_material_identity(claim: AdjudicatedClaim) -> tuple[object, ...]:
    return (
        claim.claim_id,
        claim.subject_entity_id,
        claim.target_entity_id,
        claim.relation_to_target,
        claim.directness,
        claim.verification_status,
        claim.target_scope_status,
        claim.polarity,
        claim.temporal_status,
        claim.semantic_status,
        claim.investigation_status,
        claim.event_date,
        claim.effective_start,
        claim.effective_end,
        claim.superseded_by_claim_ids,
        claim.contradiction_group_id,
        claim.source_document_id,
        claim.source_anchor_id,
        claim.source_assertion_id,
    )


def _mapping_material_identity(mapping: PrimitiveMappingProposal) -> tuple[object, ...]:
    return (
        mapping.mapping_id,
        mapping.claim_id,
        mapping.archetype_id,
        mapping.primitive_id,
        mapping.support_direction,
        mapping.mapping_status,
    )


def _canonical_claim_quote(value: str) -> str:
    quote = _norm_text(value)
    return quote.strip(" .。．!！?？\"'“”‘’")


def _canonical_anchor_sentence(anchor_text: str, quote_text: str) -> str:
    anchor = str(anchor_text or "").strip()
    quote = _canonical_claim_quote(quote_text)
    if not anchor or not quote:
        return ""
    for sentence in _split_source_sentences(anchor):
        canonical = _canonical_claim_quote(sentence)
        if canonical and (quote in canonical or canonical in quote):
            return canonical
    canonical_anchor = _canonical_claim_quote(anchor)
    return canonical_anchor if quote in canonical_anchor else ""


def _split_source_sentences(text: str) -> tuple[str, ...]:
    sentences: list[str] = []
    start = 0
    for index, char in enumerate(text):
        if char in ".。．!！?？\n":
            segment = text[start : index + 1].strip()
            if segment:
                sentences.append(segment)
            start = index + 1
    tail = text[start:].strip()
    if tail:
        sentences.append(tail)
    return tuple(sentences)


def _stable_id(prefix: str, *parts: str) -> str:
    payload = "|".join(str(part) for part in parts)
    digest = hashlib.sha1(payload.encode("utf-8")).hexdigest()[:20]
    return f"{prefix}-{digest}"


def _hash_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _as_date(value: date | datetime | None) -> date | None:
    if value is None:
        return None
    if isinstance(value, datetime):
        return value.date()
    return value


def _norm_text(value: Any) -> str:
    return " ".join(str(value or "").strip().lower().split())


def _normalise_value(value: Any) -> str:
    if isinstance(value, float):
        return f"{value:.10g}"
    if isinstance(value, (list, tuple)):
        return "[" + ",".join(_normalise_value(item) for item in value) + "]"
    if isinstance(value, Mapping):
        items = sorted((str(key), _normalise_value(raw)) for key, raw in value.items())
        return "{" + ",".join(f"{key}:{raw}" for key, raw in items) + "}"
    return _norm_text(value)


def _clean_children(children: Sequence[GateExpression]) -> tuple[GateExpression, ...]:
    clean = tuple(children)
    if not clean:
        raise ValueError("gate children must be non-empty")
    return clean


def _family_rank(family: SourceFamilyEvidence) -> tuple[int, int, str]:
    official_rank = 0 if family.official else 1
    return (official_rank, family.tier, family.document_id)


__all__ = [
    "AdjudicatedClaim",
    "AnchorType",
    "AppendOnlyEvidenceLedger",
    "BaseStage",
    "Directness",
    "EVIDENCE_OS_SCHEMA_VERSION",
    "EntityRecord",
    "EntityRegistry",
    "EntityRelation",
    "EvidenceAnchor",
    "EvidenceContractV2",
    "EvidenceDocument",
    "FORBIDDEN_EXTRACTOR_FIELDS",
    "FreshnessPolicy",
    "GateExpression",
    "GateOperator",
    "InvestigationStatus",
    "LedgerEvent",
    "LedgerEventType",
    "MappingStatus",
    "Polarity",
    "PrimitiveMappingProposal",
    "PrimitiveStateV2",
    "PrimitiveStatus",
    "PROMPT_INJECTION_MARKERS",
    "RawAssertion",
    "RelationToTarget",
    "RunComparisonClass",
    "RunFingerprint",
    "ScoreContributionV2",
    "ScoreEligibilityResult",
    "ScoreInterval",
    "ScoreStatus",
    "SemanticStatus",
    "SourceFamilyEvidence",
    "SourceQuorumRule",
    "SourceAcquisitionTask",
    "SourceType",
    "StageDecisionV2",
    "StageInvestigationStatus",
    "SupportDirection",
    "TargetScopeStatus",
    "TemporalStatus",
    "TransitionOverlay",
    "VerificationStatus",
    "classify_run_comparison",
    "dedupe_source_family_evidence",
    "derive_score_eligibility",
    "forbidden_extractor_field_overlap",
    "prompt_injection_markers",
    "source_family_from_document",
    "source_family_id_for_document",
    "stable_claim_id",
    "stable_source_assertion_id",
    "stable_source_evidence_id",
    "validate_operational_search_bounds",
]
