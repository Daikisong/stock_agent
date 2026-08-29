"""Stable evidence-gap identity and audit lineage for Researcher Mode.

An evidence gap is an economic state, not a prompt.  Supervisor prose and
provider request hashes remain useful audit lineage, but changing that prose
must never create a fresh source-query lane for the same structured need.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from enum import Enum
import hashlib
import json
import math
import re
from typing import Any, Mapping, Sequence

from e2r.research_brain.intelligence_schema import stable_intelligence_id
from e2r.research_brain.researcher_mode.schemas import (
    CANONICAL_COMPONENT_ORDER,
)


EVIDENCE_GAP_KEY_SCHEMA_VERSION = "e2r_evidence_gap_key_v1"
EVIDENCE_GAP_AUDIT_LINEAGE_SCHEMA_VERSION = (
    "e2r_evidence_gap_audit_lineage_v1"
)
EVIDENCE_GAP_ASSESSMENT_SCHEMA_VERSION = "e2r_evidence_gap_assessment_v1"
GAP_SCORE_MATERIALITY_ASSESSMENT_SCHEMA_VERSION = (
    "e2r_gap_score_materiality_assessment_v1"
)
EVIDENCE_GAP_DISPOSITION_SCHEMA_VERSION = "e2r_evidence_gap_disposition_v1"
NO_NEW_ROUTE_CONFIRMATION_SCHEMA_VERSION = (
    "e2r_no_new_route_confirmation_v1"
)
SEMANTIC_NO_NEW_ROUTE_FIXPOINT_SCHEMA_VERSION = (
    "e2r_semantic_no_new_route_fixpoint_v1"
)

_SHA256 = re.compile(r"[0-9a-f]{64}")
_STABLE_TOKEN = re.compile(r"[A-Za-z0-9_.:/,+\-\[\]]+")
_IDENTITY_FIELDS = (
    "target_id",
    "as_of_date",
    "archetype_id",
    "objective_identity",
    "affected_component_ids",
    "required_source_family",
    "economic_mechanism_id",
    "predicate_or_fact_need_id",
    "fact_snapshot_hash",
    "accepted_lineage_roster_hash",
)
_PROSE_OR_CALL_LINEAGE_FIELDS = frozenset(
    {
        "supervisor_text",
        "rationale",
        "query_text",
        "prompt_hash",
        "response_hash",
        "retry_count",
        "request_id",
    }
)
_ACCEPTED_LINEAGE_FIELDS = (
    "link_id",
    "claim_id",
    "fact_id",
    "economic_fact_key",
    "link_role",
    "material_claim",
    "claim_confidence",
    "current_lifecycle",
    "source_ids",
    "source_independence_group",
    "resolves_fact_ids",
    "supersedes_fact_ids",
    "production_score_authority",
)
_SOURCE_CORPUS_FIELDS = (
    "document_id",
    "full_source_document_id",
    "target_id",
    "as_of_date",
    "canonical_url",
    "content_hash",
    "full_source_content_hash",
    "published_at",
    "available_at",
    "source_family",
    "source_independence_group",
    "evidence_eligible",
    "evidence_os_ingest_eligible",
    "full_fetch_performed",
    "full_source_fetch_performed",
    "snippet_only",
)

# Source-family policy is intentionally economic-role based.  It does not
# synthesize a query and it never branches on a target, sector, archetype, or
# missing-slot name.  A missing primary filing/financial lane is always a
# core gap.  A supporting/independent lane may be a corroboration cap only
# after every affected component already has source-backed evidence for a
# material economic role.
CORE_REQUIRED_SOURCE_FAMILIES = frozenset(
    {
        "OPENDART",
        "KIND_KRX",
        "ISSUER_EARNINGS_RELEASE",
        "ISSUER_PRESENTATION",
        "FINANCIAL_STATEMENTS",
        "SEGMENT_DATA",
        "CASH_FLOW",
        "MARKET_CAP_PRICE",
        "CONSENSUS_REVISION",
        "VALUATION_MULTIPLES",
    }
)
SUPPORTING_CORROBORATION_SOURCE_FAMILIES = frozenset(
    {
        "ISSUER_NEWSROOM",
        "CUSTOMER_OFFICIAL",
        "REUTERS",
        "TRUSTED_BUSINESS_MEDIA",
        "PUBLIC_BROKER_PDF",
        "INDUSTRY_REPORT",
        "NAVER_DISCOVERY",
        "GENERAL_WEB_DISCOVERY",
    }
)
CORE_EVIDENCE_SOURCE_FAMILIES = frozenset(
    {*CORE_REQUIRED_SOURCE_FAMILIES, "ISSUER_NEWSROOM"}
)

_COMMON_CORE_ECONOMIC_ROLE_MARKERS = frozenset(
    {
        "ACTUAL",
        "ISSUER_OFFICIAL",
        "SEGMENT_CONTRIBUTION",
        "QOQ_GROWTH",
        "FORWARD_GUIDANCE",
        "EPS_REVISION",
        "OPERATING_PROFIT_REVISION",
        "DURABLE_VISIBILITY",
        "CONSOLIDATED_REVENUE",
        "CONSOLIDATED_NET_INCOME",
        "OPERATING_PROFIT",
        "BASIC_EARNINGS_PER_SHARE",
        "BASIC_EPS",
        "CASH_FLOW",
        "CASH_BALANCE",
        "CAPEX",
        "CAPACITY_UTILIZATION",
        "CONTRACT_LIABILITY",
        "CUSTOMER_COMMITMENT",
    }
)
_CORE_ECONOMIC_ROLE_MARKERS_BY_COMPONENT = {
    "eps_fcf_explosion": frozenset(
        {
            "EARNINGS",
            "EPS",
            "FCF",
            "FREE_CASH_FLOW",
            "NET_INCOME",
            "REVENUE",
            "MARGIN",
            "PROFIT",
            "CASH_OUTFLOW",
        }
    ),
    "earnings_visibility": frozenset(
        {
            "BACKLOG",
            "RPO",
            "CONTRACT",
            "ORDER",
            "GUIDANCE",
            "REVISION",
            "DEMAND_VISIBILITY",
            "CAPACITY",
            "SUPPLY_RESPONSE",
            "CUSTOMER_COMMITMENT",
        }
    ),
    "bottleneck_pricing": frozenset(
        {
            "ASP",
            "PRICE",
            "PRICING",
            "CAPACITY",
            "UTILIZATION",
            "SHORTAGE",
            "SUPPLY_RESPONSE",
            "CUSTOMER_COMMITMENT",
        }
    ),
    "market_mispricing": frozenset(
        {
            "CONSENSUS",
            "REVISION",
            "VALUATION",
            "FORWARD_PB",
            "FORWARD_EV_EBITDA",
            "MARKET_CAP",
        }
    ),
    "valuation_rerating": frozenset(
        {
            "VALUATION",
            "FORWARD_PB",
            "FORWARD_BOOK_VALUE",
            "FORWARD_EV_EBITDA",
            "MARKET_CAP",
        }
    ),
    "capital_allocation": frozenset(
        {
            "CAPEX",
            "INVESTMENT",
            "DIVIDEND",
            "BUYBACK",
            "TREASURY_SHARE",
            "BORROWINGS",
            "CASH_BALANCE",
        }
    ),
    "information_confidence": frozenset(
        {
            "REGULATORY",
            "FILED",
            "ISSUER_OFFICIAL",
            "REPORTS",
            "SOURCE_LINEAGE",
            "INFORMATION_CONFIDENCE",
        }
    ),
}


def _canonical_hash(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(
            value,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            default=str,
        ).encode("utf-8")
    ).hexdigest()


def _required_text(value: Any, label: str) -> str:
    text = str(value or "").strip()
    if not text:
        raise ValueError(f"{label} is required")
    return text


def _stable_token(value: Any, label: str) -> str:
    text = _required_text(value, label)
    if _STABLE_TOKEN.fullmatch(text) is None:
        raise ValueError(f"{label} must be a stable symbolic id, not prose")
    return text


def _sha256(value: Any, label: str) -> str:
    text = _required_text(value, label).lower()
    if _SHA256.fullmatch(text) is None:
        raise ValueError(f"{label} must be a sha256 digest")
    return text


def _mapping(row: Mapping[str, Any] | Any) -> Mapping[str, Any]:
    if isinstance(row, Mapping):
        return row
    to_dict = getattr(row, "to_dict", None)
    if callable(to_dict):
        value = to_dict()
        if isinstance(value, Mapping):
            return value
    raise TypeError("evidence gap state rows must be mappings or expose to_dict")


def fact_has_core_economic_role(
    row: Mapping[str, Any],
    *,
    component_id: str,
) -> bool:
    """Return whether one fact covers a material role for a component.

    Only structured role/tag fields and symbolic predicates participate.
    Free-form mechanism prose is deliberately excluded, so a sentence such
    as ``company profile`` cannot become core evidence merely because a model
    wrote persuasive prose around it.
    """

    roles = {
        str(value).strip().upper()
        for field in (
            "structured_evidence_roles",
            "primitive_tags",
            "question_family_tags",
        )
        for value in row.get(field) or ()
        if str(value).strip()
    }
    predicate = str(row.get("predicate") or "").strip()
    if predicate and _STABLE_TOKEN.fullmatch(predicate) is not None:
        roles.add(predicate.upper())
    allowed = (
        _COMMON_CORE_ECONOMIC_ROLE_MARKERS
        | _CORE_ECONOMIC_ROLE_MARKERS_BY_COMPONENT.get(
            component_id, frozenset()
        )
    )
    return any(
        role == marker
        or role.startswith(marker + "_")
        or role.endswith("_" + marker)
        or (len(marker) >= 5 and marker in role)
        for role in roles
        for marker in allowed
    )


def classify_missing_source_role(
    *,
    required_source_families: Sequence[str],
    affected_component_ids: Sequence[str],
    core_economic_role_fact_count_by_component: Mapping[str, Any],
) -> MissingSourceRole:
    """Classify a source gap without using raw fact count as authority.

    Missing primary filings/financial lanes are core even when a component
    happens to contain a weak profile fact. Supporting source families are
    corroboration only when every affected component already has at least one
    primary, economic-role-matched fact. Unknown families fail closed.
    """

    families = {
        str(value).strip().upper()
        for value in required_source_families
        if str(value).strip()
    }
    affected = {
        str(value).strip()
        for value in affected_component_ids
        if str(value).strip()
    }
    if (
        not families
        or not affected
        or families & CORE_REQUIRED_SOURCE_FAMILIES
        or not families.issubset(
            SUPPORTING_CORROBORATION_SOURCE_FAMILIES
        )
    ):
        return MissingSourceRole.CORE_SCORE_SOURCE
    if all(
        int(core_economic_role_fact_count_by_component.get(component_id) or 0)
        > 0
        for component_id in affected
    ):
        return MissingSourceRole.INDEPENDENT_CORROBORATION
    return MissingSourceRole.CORE_SCORE_SOURCE


def accepted_lineage_profile(
    claim_fact_links: Sequence[Mapping[str, Any] | Any],
    *,
    active_fact_ids: Sequence[str] | None = None,
) -> Mapping[str, Any]:
    """Hash accepted claim/fact/source lineage without prompt or row order."""

    active = (
        {str(value) for value in active_fact_ids}
        if active_fact_ids is not None
        else None
    )
    rows = []
    for raw in claim_fact_links:
        row = _mapping(raw)
        fact_id = str(row.get("fact_id") or "")
        if active is not None and fact_id not in active:
            continue
        if str(row.get("current_lifecycle") or "") in {
            "RESOLVED",
            "SUPERSEDED",
        }:
            continue
        projected = {field: row.get(field) for field in _ACCEPTED_LINEAGE_FIELDS}
        for field in ("source_ids", "resolves_fact_ids", "supersedes_fact_ids"):
            projected[field] = sorted(
                {str(value) for value in projected.get(field) or () if str(value)}
            )
        rows.append(projected)
    ordered = sorted(
        rows,
        key=lambda row: (
            str(row.get("fact_id") or ""),
            str(row.get("claim_id") or ""),
            str(row.get("link_id") or ""),
        ),
    )
    return {
        "schema_version": "e2r_accepted_lineage_profile_v1",
        "accepted_lineage_count": len(ordered),
        "accepted_lineage_roster_hash": _canonical_hash(ordered),
        "row_order_affects_hash": False,
        "prompt_or_supervisor_prose_in_hash": False,
    }


def source_corpus_profile(
    documents: Sequence[Mapping[str, Any] | Any],
) -> Mapping[str, Any]:
    """Hash source identity/content state, excluding discovery prompt prose."""

    rows = [
        {field: _mapping(raw).get(field) for field in _SOURCE_CORPUS_FIELDS}
        for raw in documents
    ]
    ordered = sorted(
        rows,
        key=lambda row: (
            str(row.get("document_id") or ""),
            str(row.get("full_source_content_hash") or ""),
            str(row.get("content_hash") or ""),
        ),
    )
    return {
        "schema_version": "e2r_source_corpus_profile_v1",
        "source_document_count": len(ordered),
        "source_corpus_hash": _canonical_hash(ordered),
        "row_order_affects_hash": False,
        "query_or_prompt_prose_in_hash": False,
    }


def canonical_source_family_requirement(
    source_families: str | Sequence[str],
) -> str:
    """Return one deterministic source-family requirement token.

    A gap can require one source family or a corroboration set.  The latter is
    represented as one sorted symbolic token so input order cannot split the
    identity.
    """

    raw_values = (
        (source_families,)
        if isinstance(source_families, str)
        else tuple(source_families)
    )
    values = tuple(
        sorted(
            {
                _stable_token(value, "required source family").upper()
                for value in raw_values
            }
        )
    )
    if not values:
        raise ValueError("at least one required source family is required")
    if len(values) == 1:
        return values[0]
    return "SOURCE_FAMILY_SET[" + ",".join(values) + "]"


def derive_objective_identity(
    *,
    stable_objective_id: str | None,
    affected_component_ids: Sequence[str],
    required_source_family: str | Sequence[str],
    economic_mechanism_id: str,
    predicate_or_fact_need_id: str,
) -> str:
    """Prefer a registry objective id, otherwise hash only stable structure."""

    if stable_objective_id is not None and str(stable_objective_id).strip():
        return _stable_token(stable_objective_id, "stable objective id")
    components = tuple(
        sorted(
            {
                _stable_token(value, "affected component id")
                for value in affected_component_ids
            }
        )
    )
    if not components:
        raise ValueError("affected component ids are required")
    payload = {
        "affected_component_ids": components,
        "required_source_family": canonical_source_family_requirement(
            required_source_family
        ),
        "economic_mechanism_id": _stable_token(
            economic_mechanism_id, "economic mechanism id"
        ),
        "predicate_or_fact_need_id": _stable_token(
            predicate_or_fact_need_id, "predicate or fact need id"
        ),
    }
    return stable_intelligence_id("EGAPOBJ", payload)


@dataclass(frozen=True)
class EvidenceGapKey:
    """Canonical identity for one evidence gap at one factual snapshot."""

    target_id: str
    as_of_date: str
    archetype_id: str
    objective_identity: str
    affected_component_ids: tuple[str, ...]
    required_source_family: str
    economic_mechanism_id: str
    predicate_or_fact_need_id: str
    fact_snapshot_hash: str
    accepted_lineage_roster_hash: str
    schema_version: str = EVIDENCE_GAP_KEY_SCHEMA_VERSION

    def __post_init__(self) -> None:
        if self.schema_version != EVIDENCE_GAP_KEY_SCHEMA_VERSION:
            raise ValueError("evidence gap key schema mismatch")
        object.__setattr__(self, "target_id", _stable_token(self.target_id, "target id"))
        try:
            date.fromisoformat(_required_text(self.as_of_date, "as_of_date"))
        except ValueError as error:
            raise ValueError("as_of_date must be ISO-8601") from error
        object.__setattr__(
            self, "archetype_id", _stable_token(self.archetype_id, "archetype id")
        )
        object.__setattr__(
            self,
            "objective_identity",
            _stable_token(self.objective_identity, "objective identity"),
        )
        components = tuple(
            sorted(
                {
                    _stable_token(value, "affected component id")
                    for value in self.affected_component_ids
                }
            )
        )
        # V3 cross-guard questions can leave a monitoring-only audit gap that
        # intentionally owns no scoring component.  Material score gaps still
        # fail closed later because an empty affected roster cannot satisfy a
        # CORE_SCORE_SOURCE assessment; the empty roster is only meaningful
        # with a deterministic MONITORING_ONLY context.
        object.__setattr__(self, "affected_component_ids", components)
        object.__setattr__(
            self,
            "required_source_family",
            canonical_source_family_requirement(self.required_source_family),
        )
        object.__setattr__(
            self,
            "economic_mechanism_id",
            _stable_token(self.economic_mechanism_id, "economic mechanism id"),
        )
        object.__setattr__(
            self,
            "predicate_or_fact_need_id",
            _stable_token(
                self.predicate_or_fact_need_id,
                "predicate or fact need id",
            ),
        )
        object.__setattr__(
            self,
            "fact_snapshot_hash",
            _sha256(self.fact_snapshot_hash, "fact snapshot hash"),
        )
        object.__setattr__(
            self,
            "accepted_lineage_roster_hash",
            _sha256(
                self.accepted_lineage_roster_hash,
                "accepted lineage roster hash",
            ),
        )

    @classmethod
    def identity_field_names(cls) -> tuple[str, ...]:
        return _IDENTITY_FIELDS

    @classmethod
    def from_dict(cls, row: Mapping[str, Any]) -> "EvidenceGapKey":
        return cls(
            target_id=str(row.get("target_id") or ""),
            as_of_date=str(row.get("as_of_date") or ""),
            archetype_id=str(row.get("archetype_id") or ""),
            objective_identity=str(row.get("objective_identity") or ""),
            affected_component_ids=tuple(
                str(value) for value in row.get("affected_component_ids") or ()
            ),
            required_source_family=str(
                row.get("required_source_family") or ""
            ),
            economic_mechanism_id=str(
                row.get("economic_mechanism_id") or ""
            ),
            predicate_or_fact_need_id=str(
                row.get("predicate_or_fact_need_id") or ""
            ),
            fact_snapshot_hash=str(row.get("fact_snapshot_hash") or ""),
            accepted_lineage_roster_hash=str(
                row.get("accepted_lineage_roster_hash") or ""
            ),
            schema_version=str(
                row.get("schema_version") or EVIDENCE_GAP_KEY_SCHEMA_VERSION
            ),
        )

    @classmethod
    def prohibited_prose_or_call_lineage_fields(cls) -> frozenset[str]:
        return _PROSE_OR_CALL_LINEAGE_FIELDS

    @property
    def semantic_gap_id(self) -> str:
        """Gap family identity excluding factual-state version hashes."""

        return stable_intelligence_id(
            "EGAPSEM",
            {
                key: value
                for key, value in self.identity_payload().items()
                if key
                not in {"fact_snapshot_hash", "accepted_lineage_roster_hash"}
            },
        )

    @property
    def gap_key(self) -> str:
        return stable_intelligence_id("EGAP", self.identity_payload())

    def identity_payload(self) -> Mapping[str, Any]:
        return {
            "target_id": self.target_id,
            "as_of_date": self.as_of_date,
            "archetype_id": self.archetype_id,
            "objective_identity": self.objective_identity,
            "affected_component_ids": list(self.affected_component_ids),
            "required_source_family": self.required_source_family,
            "economic_mechanism_id": self.economic_mechanism_id,
            "predicate_or_fact_need_id": self.predicate_or_fact_need_id,
            "fact_snapshot_hash": self.fact_snapshot_hash,
            "accepted_lineage_roster_hash": self.accepted_lineage_roster_hash,
        }

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "schema_version": self.schema_version,
            "gap_key": self.gap_key,
            "semantic_gap_id": self.semantic_gap_id,
            **self.identity_payload(),
            "identity_payload_hash": _canonical_hash(self.identity_payload()),
            "prose_or_call_lineage_in_identity": False,
        }


@dataclass(frozen=True)
class EvidenceGapAuditLineage:
    """Non-authoritative prose and provider lineage kept outside the key."""

    request_id: str | None = None
    prompt_hash: str | None = None
    response_hash: str | None = None
    supervisor_text: str | None = None
    rationale: str | None = None
    schema_version: str = EVIDENCE_GAP_AUDIT_LINEAGE_SCHEMA_VERSION

    def __post_init__(self) -> None:
        if self.schema_version != EVIDENCE_GAP_AUDIT_LINEAGE_SCHEMA_VERSION:
            raise ValueError("evidence gap audit lineage schema mismatch")
        for field_name in ("request_id", "prompt_hash", "response_hash"):
            raw = getattr(self, field_name)
            if raw is not None and not str(raw).strip():
                raise ValueError(f"{field_name} cannot be blank")

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "schema_version": self.schema_version,
            "request_id": self.request_id,
            "prompt_hash": self.prompt_hash,
            "response_hash": self.response_hash,
            "supervisor_text": self.supervisor_text,
            "rationale": self.rationale,
            "production_score_authority": False,
            "production_stage_authority": False,
        }


class EvidenceGapClass(str, Enum):
    CORE_SCORE_BLOCKER = "CORE_SCORE_BLOCKER"
    CORROBORATION_CAP = "CORROBORATION_CAP"
    MONITORING_GAP = "MONITORING_GAP"


class MissingSourceRole(str, Enum):
    CORE_SCORE_SOURCE = "CORE_SCORE_SOURCE"
    INDEPENDENT_CORROBORATION = "INDEPENDENT_CORROBORATION"
    MONITORING_ONLY = "MONITORING_ONLY"


@dataclass(frozen=True)
class EvidenceGapAssessment:
    """Deterministic materiality decision for a structured evidence gap.

    The LLM may propose a class and economic rationale.  The class that owns
    downstream behavior is derived from source-backed component sufficiency,
    range boundedness, and hard-break/Red-Team relevance.
    """

    key: EvidenceGapKey
    gap_class: EvidenceGapClass
    missing_source_role: MissingSourceRole
    source_backed_component_ids: tuple[str, ...]
    component_range_bounded: bool
    provider_or_parser_failure: bool
    direct_contradiction_or_hard_break_unresolved: bool
    required_red_team_evidence_missing: bool
    could_change_score: bool
    could_change_stage: bool
    could_change_hard_break: bool
    economic_reason: str
    llm_proposed_gap_class: str | None = None
    schema_version: str = EVIDENCE_GAP_ASSESSMENT_SCHEMA_VERSION

    def __post_init__(self) -> None:
        if self.schema_version != EVIDENCE_GAP_ASSESSMENT_SCHEMA_VERSION:
            raise ValueError("evidence gap assessment schema mismatch")
        known = frozenset(CANONICAL_COMPONENT_ORDER)
        source_backed = tuple(sorted(set(self.source_backed_component_ids)))
        if not set(self.key.affected_component_ids).issubset(known):
            raise ValueError("evidence gap affects an unknown component")
        if not set(source_backed).issubset(known):
            raise ValueError("source-backed roster contains an unknown component")
        object.__setattr__(self, "source_backed_component_ids", source_backed)
        if not str(self.economic_reason or "").strip():
            raise ValueError("evidence gap assessment requires an economic reason")
        expected = self._deterministic_class(
            missing_source_role=self.missing_source_role,
            affected_component_ids=self.key.affected_component_ids,
            source_backed_component_ids=source_backed,
            component_range_bounded=self.component_range_bounded,
            provider_or_parser_failure=self.provider_or_parser_failure,
            direct_contradiction_or_hard_break_unresolved=(
                self.direct_contradiction_or_hard_break_unresolved
            ),
            required_red_team_evidence_missing=(
                self.required_red_team_evidence_missing
            ),
        )
        if self.gap_class != expected:
            raise ValueError(
                "gap class disagrees with deterministic component sufficiency"
            )

    @classmethod
    def classify(
        cls,
        *,
        key: EvidenceGapKey,
        missing_source_role: MissingSourceRole,
        source_backed_component_ids: Sequence[str],
        component_range_bounded: bool,
        provider_or_parser_failure: bool = False,
        direct_contradiction_or_hard_break_unresolved: bool = False,
        required_red_team_evidence_missing: bool = False,
        could_change_score: bool,
        could_change_stage: bool,
        could_change_hard_break: bool,
        economic_reason: str,
        llm_proposed_gap_class: str | None = None,
    ) -> "EvidenceGapAssessment":
        source_backed = tuple(sorted(set(source_backed_component_ids)))
        deterministic_class = cls._deterministic_class(
            missing_source_role=missing_source_role,
            affected_component_ids=key.affected_component_ids,
            source_backed_component_ids=source_backed,
            component_range_bounded=component_range_bounded,
            provider_or_parser_failure=provider_or_parser_failure,
            direct_contradiction_or_hard_break_unresolved=(
                direct_contradiction_or_hard_break_unresolved
            ),
            required_red_team_evidence_missing=(
                required_red_team_evidence_missing
            ),
        )
        return cls(
            key=key,
            gap_class=deterministic_class,
            missing_source_role=missing_source_role,
            source_backed_component_ids=source_backed,
            component_range_bounded=component_range_bounded,
            provider_or_parser_failure=provider_or_parser_failure,
            direct_contradiction_or_hard_break_unresolved=(
                direct_contradiction_or_hard_break_unresolved
            ),
            required_red_team_evidence_missing=(
                required_red_team_evidence_missing
            ),
            could_change_score=could_change_score,
            could_change_stage=could_change_stage,
            could_change_hard_break=could_change_hard_break,
            economic_reason=economic_reason,
            llm_proposed_gap_class=llm_proposed_gap_class,
        )

    @classmethod
    def from_dict(
        cls,
        row: Mapping[str, Any],
        *,
        key: EvidenceGapKey | None = None,
    ) -> "EvidenceGapAssessment":
        raw_key = key
        if raw_key is None:
            key_payload = row.get("key")
            if not isinstance(key_payload, Mapping):
                raise ValueError("persisted assessment lacks its gap key")
            raw_key = EvidenceGapKey.from_dict(key_payload)
        return cls(
            key=raw_key,
            gap_class=EvidenceGapClass(str(row.get("gap_class") or "")),
            missing_source_role=MissingSourceRole(
                str(row.get("missing_source_role") or "")
            ),
            source_backed_component_ids=tuple(
                str(value)
                for value in row.get("source_backed_component_ids") or ()
            ),
            component_range_bounded=(
                row.get("component_range_bounded") is True
            ),
            provider_or_parser_failure=(
                row.get("provider_or_parser_failure") is True
            ),
            direct_contradiction_or_hard_break_unresolved=(
                row.get("direct_contradiction_or_hard_break_unresolved")
                is True
            ),
            required_red_team_evidence_missing=(
                row.get("required_red_team_evidence_missing") is True
            ),
            could_change_score=row.get("could_change_score") is True,
            could_change_stage=row.get("could_change_stage") is True,
            could_change_hard_break=(
                row.get("could_change_hard_break") is True
            ),
            economic_reason=str(row.get("economic_reason") or ""),
            llm_proposed_gap_class=(
                str(row["llm_proposed_gap_class"])
                if row.get("llm_proposed_gap_class") is not None
                else None
            ),
            schema_version=str(
                row.get("schema_version")
                or EVIDENCE_GAP_ASSESSMENT_SCHEMA_VERSION
            ),
        )

    @staticmethod
    def _deterministic_class(
        *,
        missing_source_role: MissingSourceRole,
        affected_component_ids: Sequence[str],
        source_backed_component_ids: Sequence[str],
        component_range_bounded: bool,
        provider_or_parser_failure: bool,
        direct_contradiction_or_hard_break_unresolved: bool,
        required_red_team_evidence_missing: bool,
    ) -> EvidenceGapClass:
        affected = set(affected_component_ids)
        source_backed = set(source_backed_component_ids)
        core_blocking = bool(
            direct_contradiction_or_hard_break_unresolved
            or required_red_team_evidence_missing
            or not component_range_bounded
            or not affected.issubset(source_backed)
            or (
                provider_or_parser_failure
                and missing_source_role == MissingSourceRole.CORE_SCORE_SOURCE
            )
            or missing_source_role == MissingSourceRole.CORE_SCORE_SOURCE
        )
        if core_blocking:
            return EvidenceGapClass.CORE_SCORE_BLOCKER
        if missing_source_role == MissingSourceRole.INDEPENDENT_CORROBORATION:
            return EvidenceGapClass.CORROBORATION_CAP
        return EvidenceGapClass.MONITORING_GAP

    @property
    def affected_component_ids(self) -> tuple[str, ...]:
        return self.key.affected_component_ids

    @property
    def blocked_component_ids(self) -> tuple[str, ...]:
        if self.gap_class == EvidenceGapClass.CORE_SCORE_BLOCKER:
            return self.affected_component_ids
        return ()

    @property
    def capped_component_ids(self) -> tuple[str, ...]:
        if self.gap_class == EvidenceGapClass.CORROBORATION_CAP:
            return self.affected_component_ids
        return ()

    @property
    def score_valid_if_only_gap(self) -> bool:
        return self.gap_class != EvidenceGapClass.CORE_SCORE_BLOCKER

    @property
    def global_score_block(self) -> bool:
        return self.gap_class == EvidenceGapClass.CORE_SCORE_BLOCKER

    def component_effect(self, component_id: str) -> str:
        component = _stable_token(component_id, "component id")
        if component not in set(CANONICAL_COMPONENT_ORDER):
            raise ValueError("unknown component id")
        if component not in set(self.affected_component_ids):
            return "UNAFFECTED"
        if self.gap_class == EvidenceGapClass.CORE_SCORE_BLOCKER:
            return "BLOCKED"
        if self.gap_class == EvidenceGapClass.CORROBORATION_CAP:
            return "CAPPED"
        return "MONITORING"

    def component_completion_allowed(self, component_id: str) -> bool:
        return self.component_effect(component_id) != "BLOCKED"

    def to_dict(self) -> Mapping[str, Any]:
        proposed = (
            str(self.llm_proposed_gap_class)
            if self.llm_proposed_gap_class is not None
            else None
        )
        return {
            "schema_version": self.schema_version,
            "key": self.key.to_dict(),
            "gap_key": self.key.gap_key,
            "semantic_gap_id": self.key.semantic_gap_id,
            "gap_class": self.gap_class.value,
            "affected_component_ids": list(self.affected_component_ids),
            "blocked_component_ids": list(self.blocked_component_ids),
            "capped_component_ids": list(self.capped_component_ids),
            "unaffected_component_ids": [
                component_id
                for component_id in CANONICAL_COMPONENT_ORDER
                if component_id not in set(self.affected_component_ids)
            ],
            "missing_source_role": self.missing_source_role.value,
            "source_backed_component_ids": list(
                self.source_backed_component_ids
            ),
            "component_range_bounded": self.component_range_bounded,
            "provider_or_parser_failure": self.provider_or_parser_failure,
            "direct_contradiction_or_hard_break_unresolved": (
                self.direct_contradiction_or_hard_break_unresolved
            ),
            "required_red_team_evidence_missing": (
                self.required_red_team_evidence_missing
            ),
            "could_change_score": self.could_change_score,
            "could_change_stage": self.could_change_stage,
            "could_change_hard_break": self.could_change_hard_break,
            "economic_reason": self.economic_reason,
            "llm_proposed_gap_class": proposed,
            "llm_proposal_matches_deterministic_class": (
                proposed is None or proposed == self.gap_class.value
            ),
            "score_valid_if_only_gap": self.score_valid_if_only_gap,
            "global_score_block": self.global_score_block,
            "production_score_authority": False,
            "production_stage_authority": False,
        }


@dataclass(frozen=True)
class GapScoreMaterialityAssessment:
    """Bound one unresolved gap without inventing score weights or Stage rules.

    ``deterministic_lower_stage`` and ``deterministic_upper_stage`` are outputs
    of the existing deterministic scorer/Stage classifier for the two bounded
    component vectors.  This record may decide whether another source-query
    lane is warranted, but it cannot calculate or overwrite a production
    score or Stage itself.
    """

    assessment: EvidenceGapAssessment
    component_lower_delta: Mapping[str, float]
    component_upper_delta: Mapping[str, float]
    total_score_lower_delta: float
    total_score_upper_delta: float
    could_change_score_valid: bool
    could_cross_stage_boundary: bool
    could_change_hard_break: bool
    search_required: bool
    stage_cap_if_unconfirmed: str | None
    rationale: str
    deterministic_lower_stage: str | None
    deterministic_upper_stage: str | None
    executable_new_source_route_exists: bool
    stage_cap_reason: str | None = None
    schema_version: str = GAP_SCORE_MATERIALITY_ASSESSMENT_SCHEMA_VERSION

    def __post_init__(self) -> None:
        if self.schema_version != GAP_SCORE_MATERIALITY_ASSESSMENT_SCHEMA_VERSION:
            raise ValueError("gap score materiality assessment schema mismatch")
        affected = tuple(self.assessment.affected_component_ids)
        lower = self._validated_delta_mapping(
            self.component_lower_delta,
            affected_component_ids=affected,
            label="component lower delta",
        )
        upper = self._validated_delta_mapping(
            self.component_upper_delta,
            affected_component_ids=affected,
            label="component upper delta",
        )
        for component_id in affected:
            if lower[component_id] > upper[component_id]:
                raise ValueError("component lower delta cannot exceed upper delta")
        object.__setattr__(self, "component_lower_delta", lower)
        object.__setattr__(self, "component_upper_delta", upper)
        lower_total = self._finite_number(
            self.total_score_lower_delta,
            "total score lower delta",
        )
        upper_total = self._finite_number(
            self.total_score_upper_delta,
            "total score upper delta",
        )
        if lower_total > upper_total:
            raise ValueError("total score lower delta cannot exceed upper delta")
        if not math.isclose(lower_total, sum(lower.values()), abs_tol=1e-9):
            raise ValueError("total score lower delta must equal component sum")
        if not math.isclose(upper_total, sum(upper.values()), abs_tol=1e-9):
            raise ValueError("total score upper delta must equal component sum")
        object.__setattr__(self, "total_score_lower_delta", lower_total)
        object.__setattr__(self, "total_score_upper_delta", upper_total)
        if not str(self.rationale or "").strip():
            raise ValueError("gap score materiality rationale is required")

        for stage, label in (
            (self.deterministic_lower_stage, "deterministic lower stage"),
            (self.deterministic_upper_stage, "deterministic upper stage"),
            (self.stage_cap_if_unconfirmed, "stage cap"),
        ):
            if stage is not None:
                self._canonical_stage(stage, label)
        crosses = bool(
            self.deterministic_lower_stage is not None
            and self.deterministic_upper_stage is not None
            and self.deterministic_lower_stage
            != self.deterministic_upper_stage
        )
        if self.could_cross_stage_boundary != crosses:
            raise ValueError(
                "stage-boundary flag must come from deterministic lower/upper stages"
            )
        expected_score_valid_change = bool(
            self.assessment.global_score_block
            or not self.assessment.component_range_bounded
        )
        if self.could_change_score_valid != expected_score_valid_change:
            raise ValueError(
                "score-validity materiality disagrees with core source sufficiency"
            )
        if self.could_change_hard_break != self.assessment.could_change_hard_break:
            raise ValueError(
                "hard-break materiality disagrees with evidence-gap assessment"
            )
        expected_search = bool(
            self.assessment.gap_class == EvidenceGapClass.CORE_SCORE_BLOCKER
            or not self.assessment.component_range_bounded
            or self.could_change_hard_break
            or (crosses and self.executable_new_source_route_exists)
        )
        if self.search_required != expected_search:
            raise ValueError("search policy disagrees with deterministic materiality")

        expected_cap = None
        if (
            crosses
            and not expected_search
            and self.assessment.gap_class
            in {
                EvidenceGapClass.CORROBORATION_CAP,
                EvidenceGapClass.MONITORING_GAP,
            }
        ):
            expected_cap = self.deterministic_lower_stage
        if self.stage_cap_if_unconfirmed != expected_cap:
            raise ValueError(
                "unconfirmed gap must use the deterministic lower Stage as its cap"
            )
        if expected_cap is not None and not str(self.stage_cap_reason or "").strip():
            raise ValueError("a conservative Stage cap requires stage_cap_reason")
        if expected_cap is None and self.stage_cap_reason is not None:
            raise ValueError("stage_cap_reason is only allowed when a cap exists")

    @staticmethod
    def _finite_number(value: Any, label: str) -> float:
        if isinstance(value, bool):
            raise ValueError(f"{label} must be finite")
        try:
            number = float(value)
        except (TypeError, ValueError) as error:
            raise ValueError(f"{label} must be finite") from error
        if not math.isfinite(number):
            raise ValueError(f"{label} must be finite")
        return number

    @classmethod
    def _validated_delta_mapping(
        cls,
        values: Mapping[str, float],
        *,
        affected_component_ids: Sequence[str],
        label: str,
    ) -> Mapping[str, float]:
        if not isinstance(values, Mapping):
            raise ValueError(f"{label} must be a mapping")
        expected = set(affected_component_ids)
        if set(values) != expected:
            raise ValueError(f"{label} must cover exactly the affected components")
        return {
            component_id: cls._finite_number(values[component_id], label)
            for component_id in affected_component_ids
        }

    @staticmethod
    def _canonical_stage(value: str, label: str) -> str:
        canonical = {
            "0",
            "1",
            "2",
            "3-Green",
            "3-Yellow",
            "3-Red",
            "4A",
            "4B",
            "4C",
            "5",
        }
        stage = str(value)
        if stage not in canonical:
            raise ValueError(f"{label} must use the canonical Stage enum")
        return stage

    @classmethod
    def assess(
        cls,
        *,
        assessment: EvidenceGapAssessment,
        component_lower_delta: Mapping[str, float],
        component_upper_delta: Mapping[str, float],
        deterministic_lower_stage: str | None,
        deterministic_upper_stage: str | None,
        executable_new_source_route_exists: bool,
        rationale: str,
        stage_cap_reason: str | None = None,
    ) -> "GapScoreMaterialityAssessment":
        lower = {
            component_id: float(component_lower_delta[component_id])
            for component_id in assessment.affected_component_ids
        }
        upper = {
            component_id: float(component_upper_delta[component_id])
            for component_id in assessment.affected_component_ids
        }
        crosses = bool(
            deterministic_lower_stage is not None
            and deterministic_upper_stage is not None
            and deterministic_lower_stage != deterministic_upper_stage
        )
        score_valid_change = bool(
            assessment.global_score_block
            or not assessment.component_range_bounded
        )
        search_required = bool(
            assessment.gap_class == EvidenceGapClass.CORE_SCORE_BLOCKER
            or not assessment.component_range_bounded
            or assessment.could_change_hard_break
            or (crosses and executable_new_source_route_exists)
        )
        stage_cap = (
            deterministic_lower_stage
            if crosses
            and not search_required
            and assessment.gap_class
            in {
                EvidenceGapClass.CORROBORATION_CAP,
                EvidenceGapClass.MONITORING_GAP,
            }
            else None
        )
        return cls(
            assessment=assessment,
            component_lower_delta=lower,
            component_upper_delta=upper,
            total_score_lower_delta=sum(lower.values()),
            total_score_upper_delta=sum(upper.values()),
            could_change_score_valid=score_valid_change,
            could_cross_stage_boundary=crosses,
            could_change_hard_break=assessment.could_change_hard_break,
            search_required=search_required,
            stage_cap_if_unconfirmed=stage_cap,
            rationale=rationale,
            deterministic_lower_stage=deterministic_lower_stage,
            deterministic_upper_stage=deterministic_upper_stage,
            executable_new_source_route_exists=(
                executable_new_source_route_exists
            ),
            stage_cap_reason=stage_cap_reason,
        )

    @property
    def gap_key(self) -> str:
        return self.assessment.key.gap_key

    @property
    def affected_component_ids(self) -> tuple[str, ...]:
        return self.assessment.affected_component_ids

    @property
    def score_valid_if_only_gap(self) -> bool:
        return not self.could_change_score_valid

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "schema_version": self.schema_version,
            "gap_key": self.gap_key,
            "affected_component_ids": list(self.affected_component_ids),
            "component_lower_delta": dict(self.component_lower_delta),
            "component_upper_delta": dict(self.component_upper_delta),
            "total_score_lower_delta": self.total_score_lower_delta,
            "total_score_upper_delta": self.total_score_upper_delta,
            "could_change_score_valid": self.could_change_score_valid,
            "could_cross_stage_boundary": self.could_cross_stage_boundary,
            "could_change_hard_break": self.could_change_hard_break,
            "search_required": self.search_required,
            "stage_cap_if_unconfirmed": self.stage_cap_if_unconfirmed,
            "stage_cap_reason": self.stage_cap_reason,
            "rationale": self.rationale,
            "deterministic_lower_stage": self.deterministic_lower_stage,
            "deterministic_upper_stage": self.deterministic_upper_stage,
            "executable_new_source_route_exists": (
                self.executable_new_source_route_exists
            ),
            "score_valid_if_only_gap": self.score_valid_if_only_gap,
            "new_score_weight_created": False,
            "new_stage_threshold_created": False,
            "production_score_authority": False,
            "production_stage_authority": False,
        }


class EvidenceGapDispositionStatus(str, Enum):
    UNRESOLVED_EVIDENCE_GAP = "UNRESOLVED_EVIDENCE_GAP"


_REOPEN_CONDITIONS = (
    "FACT_SNAPSHOT_CHANGED",
    "ACCEPTED_LINEAGE_ROSTER_CHANGED",
    "GENUINELY_NEW_SOURCE_ROUTE",
    "PROVIDER_OR_PARSER_RECOVERED",
    "NEW_CURRENT_EVENT",
)


@dataclass(frozen=True)
class EvidenceGapDisposition:
    """Append-only handoff from an exhausted query lane to analysis."""

    assessment: EvidenceGapAssessment
    attempted_route_signatures: tuple[str, ...]
    no_new_route_confirmation_ids: tuple[str, ...]
    query_lane_exhausted: bool
    downstream_action: str
    supersedes_disposition_id: str | None = None
    reopen_reason: str | None = None
    status: EvidenceGapDispositionStatus = (
        EvidenceGapDispositionStatus.UNRESOLVED_EVIDENCE_GAP
    )
    schema_version: str = EVIDENCE_GAP_DISPOSITION_SCHEMA_VERSION

    def __post_init__(self) -> None:
        if self.schema_version != EVIDENCE_GAP_DISPOSITION_SCHEMA_VERSION:
            raise ValueError("evidence gap disposition schema mismatch")
        routes = tuple(
            sorted(
                {
                    _required_text(value, "attempted route signature")
                    for value in self.attempted_route_signatures
                }
            )
        )
        confirmations = tuple(
            dict.fromkeys(
                _required_text(value, "no-new-route confirmation id")
                for value in self.no_new_route_confirmation_ids
            )
        )
        object.__setattr__(self, "attempted_route_signatures", routes)
        object.__setattr__(
            self, "no_new_route_confirmation_ids", confirmations
        )
        action = _stable_token(self.downstream_action, "downstream action")
        object.__setattr__(self, "downstream_action", action)
        expected_actions = {
            EvidenceGapClass.CORE_SCORE_BLOCKER: {
                "RESEARCH_PENDING_CORE_SOURCE",
                "REOPEN_SOURCE_QUERY_LANE",
            },
            EvidenceGapClass.CORROBORATION_CAP: {
                "COMPONENT_MEMO_WITH_CONFIDENCE_PENALTY",
                "REOPEN_SOURCE_QUERY_LANE",
            },
            EvidenceGapClass.MONITORING_GAP: {
                "MONITORING_LEDGER",
                "REOPEN_SOURCE_QUERY_LANE",
            },
        }
        if action not in expected_actions[self.assessment.gap_class]:
            raise ValueError("downstream action disagrees with gap class")
        if self.query_lane_exhausted and action == "REOPEN_SOURCE_QUERY_LANE":
            raise ValueError("an exhausted query lane cannot be marked reopened")
        if not self.query_lane_exhausted and action != "REOPEN_SOURCE_QUERY_LANE":
            raise ValueError("a reopened query lane requires the reopen action")
        if self.supersedes_disposition_id is not None:
            _stable_token(
                self.supersedes_disposition_id,
                "superseded disposition id",
            )
            if self.reopen_reason not in _REOPEN_CONDITIONS:
                raise ValueError("superseding disposition requires a real state change")
        elif self.reopen_reason is not None:
            raise ValueError("initial disposition cannot have a reopen reason")

    @classmethod
    def unresolved(
        cls,
        *,
        assessment: EvidenceGapAssessment,
        attempted_route_signatures: Sequence[str],
        no_new_route_confirmation_ids: Sequence[str],
    ) -> "EvidenceGapDisposition":
        action = {
            EvidenceGapClass.CORE_SCORE_BLOCKER: "RESEARCH_PENDING_CORE_SOURCE",
            EvidenceGapClass.CORROBORATION_CAP: (
                "COMPONENT_MEMO_WITH_CONFIDENCE_PENALTY"
            ),
            EvidenceGapClass.MONITORING_GAP: "MONITORING_LEDGER",
        }[assessment.gap_class]
        return cls(
            assessment=assessment,
            attempted_route_signatures=tuple(attempted_route_signatures),
            no_new_route_confirmation_ids=tuple(
                no_new_route_confirmation_ids
            ),
            query_lane_exhausted=True,
            downstream_action=action,
        )

    @classmethod
    def from_dict(cls, row: Mapping[str, Any]) -> "EvidenceGapDisposition":
        assessment_payload = row.get("assessment")
        if not isinstance(assessment_payload, Mapping):
            raise ValueError("persisted disposition lacks assessment")
        assessment = EvidenceGapAssessment.from_dict(assessment_payload)
        disposition = cls(
            assessment=assessment,
            attempted_route_signatures=tuple(
                str(value)
                for value in row.get("attempted_route_signatures") or ()
            ),
            no_new_route_confirmation_ids=tuple(
                str(value)
                for value in row.get("no_new_route_confirmation_ids") or ()
            ),
            query_lane_exhausted=row.get("query_lane_exhausted") is True,
            downstream_action=str(row.get("downstream_action") or ""),
            supersedes_disposition_id=(
                str(row["supersedes_disposition_id"])
                if row.get("supersedes_disposition_id") is not None
                else None
            ),
            reopen_reason=(
                str(row["reopen_reason"])
                if row.get("reopen_reason") is not None
                else None
            ),
            status=EvidenceGapDispositionStatus(
                str(row.get("status") or "")
            ),
            schema_version=str(
                row.get("schema_version")
                or EVIDENCE_GAP_DISPOSITION_SCHEMA_VERSION
            ),
        )
        if row.get("disposition_id") not in {
            None,
            disposition.disposition_id,
        }:
            raise ValueError("persisted disposition id mismatch")
        if row.get("source_absence_proven") not in {None, False}:
            raise ValueError("disposition cannot prove source absence")
        return disposition

    @property
    def key(self) -> EvidenceGapKey:
        return self.assessment.key

    @property
    def disposition_id(self) -> str:
        return stable_intelligence_id(
            "EGAPDISP",
            {
                "gap_key": self.key.gap_key,
                "gap_class": self.assessment.gap_class.value,
                "status": self.status.value,
                "query_lane_exhausted": self.query_lane_exhausted,
                "attempted_route_signatures": self.attempted_route_signatures,
                "no_new_route_confirmation_ids": (
                    self.no_new_route_confirmation_ids
                ),
                "downstream_action": self.downstream_action,
                "supersedes_disposition_id": self.supersedes_disposition_id,
                "reopen_reason": self.reopen_reason,
            },
        )

    def reopen_reason_for(
        self,
        *,
        candidate_key: EvidenceGapKey,
        candidate_route_signatures: Sequence[str] = (),
        provider_or_parser_recovered: bool = False,
        new_current_event: bool = False,
    ) -> str | None:
        if candidate_key.semantic_gap_id != self.key.semantic_gap_id:
            raise ValueError("cannot reopen a disposition for a different gap")
        if candidate_key.fact_snapshot_hash != self.key.fact_snapshot_hash:
            return "FACT_SNAPSHOT_CHANGED"
        if (
            candidate_key.accepted_lineage_roster_hash
            != self.key.accepted_lineage_roster_hash
        ):
            return "ACCEPTED_LINEAGE_ROSTER_CHANGED"
        attempted = set(self.attempted_route_signatures)
        if any(
            _required_text(value, "candidate route signature") not in attempted
            for value in candidate_route_signatures
        ):
            return "GENUINELY_NEW_SOURCE_ROUTE"
        if provider_or_parser_recovered:
            return "PROVIDER_OR_PARSER_RECOVERED"
        if new_current_event:
            return "NEW_CURRENT_EVENT"
        return None

    def superseding_reopen(
        self,
        *,
        assessment: EvidenceGapAssessment,
        candidate_route_signatures: Sequence[str] = (),
        provider_or_parser_recovered: bool = False,
        new_current_event: bool = False,
    ) -> "EvidenceGapDisposition":
        reason = self.reopen_reason_for(
            candidate_key=assessment.key,
            candidate_route_signatures=candidate_route_signatures,
            provider_or_parser_recovered=provider_or_parser_recovered,
            new_current_event=new_current_event,
        )
        if reason is None:
            raise ValueError("disposition cannot reopen without a real state change")
        return EvidenceGapDisposition(
            assessment=assessment,
            attempted_route_signatures=tuple(
                sorted(
                    set(self.attempted_route_signatures)
                    | {
                        _required_text(value, "candidate route signature")
                        for value in candidate_route_signatures
                    }
                )
            ),
            no_new_route_confirmation_ids=(),
            query_lane_exhausted=False,
            downstream_action="REOPEN_SOURCE_QUERY_LANE",
            supersedes_disposition_id=self.disposition_id,
            reopen_reason=reason,
        )

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "schema_version": self.schema_version,
            "disposition_id": self.disposition_id,
            "assessment": self.assessment.to_dict(),
            "gap_key": self.key.gap_key,
            "semantic_gap_id": self.key.semantic_gap_id,
            "status": self.status.value,
            "gap_class": self.assessment.gap_class.value,
            "source_absence_proven": False,
            "query_lane_exhausted": self.query_lane_exhausted,
            "fact_snapshot_hash": self.key.fact_snapshot_hash,
            "accepted_lineage_roster_hash": (
                self.key.accepted_lineage_roster_hash
            ),
            "attempted_route_signatures": list(
                self.attempted_route_signatures
            ),
            "no_new_route_confirmation_ids": list(
                self.no_new_route_confirmation_ids
            ),
            "affected_component_ids": list(self.key.affected_component_ids),
            "downstream_action": self.downstream_action,
            "reopen_conditions": list(_REOPEN_CONDITIONS),
            "supersedes_disposition_id": self.supersedes_disposition_id,
            "reopen_reason": self.reopen_reason,
            "production_score_authority": False,
            "production_stage_authority": False,
        }


def latest_evidence_gap_dispositions(
    rows: Sequence[EvidenceGapDisposition],
) -> Mapping[str, EvidenceGapDisposition]:
    """Index append-only rows without mutating superseded history."""

    by_id: dict[str, EvidenceGapDisposition] = {}
    superseded_ids: set[str] = set()
    for row in rows:
        if row.disposition_id in by_id:
            raise ValueError("duplicate evidence gap disposition id")
        if (
            row.supersedes_disposition_id is not None
            and row.supersedes_disposition_id not in by_id
        ):
            raise ValueError("evidence gap disposition supersedes an unknown row")
        by_id[row.disposition_id] = row
        if row.supersedes_disposition_id is not None:
            superseded_ids.add(row.supersedes_disposition_id)
    current: dict[str, EvidenceGapDisposition] = {}
    for disposition_id, row in by_id.items():
        if disposition_id in superseded_ids:
            continue
        semantic_id = row.key.semantic_gap_id
        if semantic_id in current:
            raise ValueError("multiple current dispositions exist for one gap")
        current[semantic_id] = row
    return current


def canonical_current_pending_request_ids(
    *,
    pending_reasons: Sequence[str],
    request_ids: Sequence[str],
    response_ids: Sequence[str],
    quarantined_request_ids: Sequence[str] = (),
) -> tuple[str, ...]:
    """Return only unanswered requests referenced by canonical state."""

    requested = set(request_ids)
    answered = set(response_ids)
    quarantined = set(quarantined_request_ids)
    referenced: set[str] = set()
    for reason in pending_reasons:
        referenced.update(
            re.findall(r"COLLABREQ-[0-9a-f]{64}", str(reason or ""))
        )
    return tuple(
        sorted((referenced & requested) - answered - quarantined)
    )


@dataclass(frozen=True)
class NoNewRouteConfirmation:
    """One consumed LLM call assessed for no-new-route convergence."""

    key: EvidenceGapKey
    prompt_hash: str
    response_hash: str
    request_id: str | None
    suggested_queries: tuple[Mapping[str, Any], ...]
    new_source_directions: tuple[str, ...]
    unresolved_research_notes: tuple[str, ...]
    provider_error: bool = False
    parser_or_fetch_repair_pending: bool = False
    deterministic_fallback_query_used: bool = False
    concrete_untried_source_route_signatures: tuple[str, ...] = ()
    accepted_fact_delta: int = 0
    accepted_lineage_delta: int = 0
    schema_version: str = NO_NEW_ROUTE_CONFIRMATION_SCHEMA_VERSION

    def __post_init__(self) -> None:
        if self.schema_version != NO_NEW_ROUTE_CONFIRMATION_SCHEMA_VERSION:
            raise ValueError("no-new-route confirmation schema mismatch")
        if not str(self.prompt_hash or "").startswith("QUERYPROMPT-"):
            raise ValueError("confirmation requires query prompt lineage")
        if not str(self.response_hash or "").startswith("QUERYRESP-"):
            raise ValueError("confirmation requires consumed query response lineage")
        if self.request_id is not None and not str(self.request_id).startswith(
            "COLLABREQ-"
        ):
            raise ValueError("confirmation request id is invalid")
        if self.accepted_fact_delta < 0 or self.accepted_lineage_delta < 0:
            raise ValueError("accepted state deltas cannot be negative")
        directions = tuple(
            _required_text(value, "new source direction")
            for value in self.new_source_directions
        )
        notes = tuple(
            _required_text(value, "unresolved research note")
            for value in self.unresolved_research_notes
        )
        routes = tuple(
            sorted(
                {
                    _stable_token(value, "untried source route signature")
                    for value in self.concrete_untried_source_route_signatures
                }
            )
        )
        object.__setattr__(self, "new_source_directions", directions)
        object.__setattr__(self, "unresolved_research_notes", notes)
        object.__setattr__(
            self, "concrete_untried_source_route_signatures", routes
        )

    @property
    def confirmation_id(self) -> str:
        return stable_intelligence_id(
            "EGAPCONF",
            {
                "gap_key": self.key.gap_key,
                "prompt_hash": self.prompt_hash,
                "response_hash": self.response_hash,
                "request_id": self.request_id,
            },
        )

    @property
    def valid_no_new_route_confirmation(self) -> bool:
        return bool(
            not self.suggested_queries
            and not self.new_source_directions
            and not self.provider_error
            and not self.parser_or_fetch_repair_pending
            and not self.deterministic_fallback_query_used
            and not self.concrete_untried_source_route_signatures
            and self.accepted_fact_delta == 0
            and self.accepted_lineage_delta == 0
        )

    @property
    def resets_confirmation_chain(self) -> bool:
        return bool(
            self.suggested_queries
            or self.new_source_directions
            or self.concrete_untried_source_route_signatures
            or self.accepted_fact_delta
            or self.accepted_lineage_delta
        )

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "schema_version": self.schema_version,
            "confirmation_id": self.confirmation_id,
            "gap_key": self.key.gap_key,
            "prompt_hash": self.prompt_hash,
            "response_hash": self.response_hash,
            "request_id": self.request_id,
            "suggested_query_count": len(self.suggested_queries),
            "new_source_direction_count": len(self.new_source_directions),
            "unresolved_research_notes": list(
                self.unresolved_research_notes
            ),
            "provider_error": self.provider_error,
            "parser_or_fetch_repair_pending": (
                self.parser_or_fetch_repair_pending
            ),
            "deterministic_fallback_query_used": (
                self.deterministic_fallback_query_used
            ),
            "concrete_untried_source_route_signatures": list(
                self.concrete_untried_source_route_signatures
            ),
            "accepted_fact_delta": self.accepted_fact_delta,
            "accepted_lineage_delta": self.accepted_lineage_delta,
            "valid_no_new_route_confirmation": (
                self.valid_no_new_route_confirmation
            ),
            "source_absence_proven": False,
            "production_score_authority": False,
            "production_stage_authority": False,
        }


@dataclass(frozen=True)
class SemanticNoNewRouteFixpoint:
    """State convergence for one stable gap; never a source-absence proof."""

    key: EvidenceGapKey
    confirmations: tuple[NoNewRouteConfirmation, ...]
    schema_version: str = SEMANTIC_NO_NEW_ROUTE_FIXPOINT_SCHEMA_VERSION

    def __post_init__(self) -> None:
        if self.schema_version != SEMANTIC_NO_NEW_ROUTE_FIXPOINT_SCHEMA_VERSION:
            raise ValueError("semantic no-new-route fixpoint schema mismatch")
        if any(row.key.gap_key != self.key.gap_key for row in self.confirmations):
            raise ValueError("fixpoint confirmation belongs to another gap state")

    @property
    def confirmation_chain(self) -> tuple[NoNewRouteConfirmation, ...]:
        chain: list[NoNewRouteConfirmation] = []
        for row in self.confirmations:
            if row.resets_confirmation_chain:
                chain.clear()
                continue
            if row.valid_no_new_route_confirmation:
                chain.append(row)
        return tuple(chain)

    @property
    def valid_confirmation_count(self) -> int:
        return len(self.confirmation_chain)

    @property
    def reached(self) -> bool:
        chain = self.confirmation_chain
        if len(chain) < 2:
            return False
        latest = chain[-2:]
        if len({row.prompt_hash for row in latest}) != 2:
            return False
        request_ids = [row.request_id for row in latest if row.request_id]
        if request_ids and len(set(request_ids)) != len(request_ids):
            return False
        return True

    @property
    def fixpoint_id(self) -> str | None:
        if not self.reached:
            return None
        return stable_intelligence_id(
            "EGAPFIX",
            {
                "gap_key": self.key.gap_key,
                "confirmation_ids": [
                    row.confirmation_id for row in self.confirmation_chain[-2:]
                ],
            },
        )

    def create_disposition(
        self,
        *,
        assessment: EvidenceGapAssessment,
        attempted_route_signatures: Sequence[str],
    ) -> EvidenceGapDisposition:
        if assessment.key.gap_key != self.key.gap_key:
            raise ValueError("fixpoint assessment belongs to another gap")
        if not self.reached:
            raise ValueError("semantic no-new-route fixpoint is not reached")
        return EvidenceGapDisposition.unresolved(
            assessment=assessment,
            attempted_route_signatures=attempted_route_signatures,
            no_new_route_confirmation_ids=tuple(
                row.confirmation_id for row in self.confirmation_chain[-2:]
            ),
        )

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "schema_version": self.schema_version,
            "fixpoint_id": self.fixpoint_id,
            "gap_key": self.key.gap_key,
            "semantic_gap_id": self.key.semantic_gap_id,
            "status": (
                "SEMANTIC_NO_NEW_ROUTE_FIXPOINT"
                if self.reached
                else "NO_NEW_ROUTE_FIXPOINT_PENDING"
            ),
            "fact_snapshot_hash": self.key.fact_snapshot_hash,
            "accepted_lineage_roster_hash": (
                self.key.accepted_lineage_roster_hash
            ),
            "confirmation_count": len(self.confirmations),
            "valid_no_new_route_confirmation_count": (
                self.valid_confirmation_count
            ),
            "independent_prompt_count": len(
                {row.prompt_hash for row in self.confirmation_chain[-2:]}
            ),
            "confirmation_ids": [
                row.confirmation_id for row in self.confirmation_chain
            ],
            "accepted_fact_delta": sum(
                row.accepted_fact_delta for row in self.confirmation_chain[-2:]
            ),
            "accepted_lineage_delta": sum(
                row.accepted_lineage_delta
                for row in self.confirmation_chain[-2:]
            ),
            "source_absence_proven": False,
            "deterministic_fallback_query_used": False,
            "production_score_authority": False,
            "production_stage_authority": False,
        }


class RepeatedExhaustedGapReopenedError(RuntimeError):
    failure_code = "REPEATED_EXHAUSTED_GAP_REOPENED"


def guard_source_query_generation(
    *,
    disposition: EvidenceGapDisposition,
    candidate_key: EvidenceGapKey,
    candidate_route_signatures: Sequence[str] = (),
    provider_or_parser_recovered: bool = False,
    new_current_event: bool = False,
) -> str | None:
    """Hard-fail a third query for an unchanged exhausted gap.

    A real state change returns its explicit reopen reason.  The caller must
    append a superseding disposition before opening the query lane.
    """

    reason = disposition.reopen_reason_for(
        candidate_key=candidate_key,
        candidate_route_signatures=candidate_route_signatures,
        provider_or_parser_recovered=provider_or_parser_recovered,
        new_current_event=new_current_event,
    )
    if reason is not None:
        return reason
    if disposition.query_lane_exhausted:
        raise RepeatedExhaustedGapReopenedError(
            RepeatedExhaustedGapReopenedError.failure_code
            + ":"
            + candidate_key.gap_key
        )
    return None
