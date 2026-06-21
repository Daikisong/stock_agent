"""Claim-level evidence models for source-backed primitive compilation."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
import hashlib
import math
from typing import Any, Mapping, Sequence


CLAIM_LEDGER_VERSION = "e2r-claim-ledger-v1"


@dataclass(frozen=True)
class EvidenceClaim:
    """Smallest source-backed claim that can support one primitive."""

    claim_id: str
    evidence_id: str
    symbol: str
    archetype_id: str | None
    primitive_id: str
    subject: str
    predicate: str
    value: Any
    as_of_date: date
    quote_text: str
    source_url: str | None = None
    source_tier: int | None = None
    unit: str | None = None
    polarity: str = "positive"
    certainty: str = "confirmed"
    period_start: date | None = None
    period_end: date | None = None
    issuer_scoped: bool = True
    confidence: float = 1.0
    verified: bool = True
    contradiction_group: str | None = None

    def __post_init__(self) -> None:
        if not self.claim_id.strip():
            raise ValueError("claim_id must be non-empty")
        if not self.evidence_id.strip():
            raise ValueError("evidence_id must be non-empty")
        if not self.symbol.strip():
            raise ValueError("symbol must be non-empty")
        if not self.primitive_id.strip():
            raise ValueError("primitive_id must be non-empty")
        if self.polarity not in {"positive", "negative", "conditional"}:
            raise ValueError("polarity must be positive, negative, or conditional")
        if self.certainty not in {"confirmed", "guided", "expected", "rumored"}:
            raise ValueError("certainty must be confirmed, guided, expected, or rumored")
        if self.confidence < 0.0 or self.confidence > 1.0:
            raise ValueError("confidence must be between 0 and 1")


@dataclass(frozen=True)
class PrimitiveState:
    """Aggregated state for one primitive after claim compilation."""

    primitive_id: str
    status: str
    normalized_value: Any | None
    support_claim_ids: tuple[str, ...]
    counter_claim_ids: tuple[str, ...]
    confidence: float
    freshness_days: int

    def __post_init__(self) -> None:
        if not self.primitive_id.strip():
            raise ValueError("primitive_id must be non-empty")
        if self.status not in {"PRESENT", "ABSENT", "UNKNOWN", "CONTRADICTED"}:
            raise ValueError("status must be PRESENT, ABSENT, UNKNOWN, or CONTRADICTED")
        if self.confidence < 0.0 or self.confidence > 1.0:
            raise ValueError("confidence must be between 0 and 1")


def compile_claims_from_primitives(
    *,
    evidence_id: str,
    symbol: str,
    as_of_date: date,
    primitive_ids: Sequence[str],
    archetype_id: str | None = None,
    subject: str | None = None,
    quote_text: str = "",
    source_url: str | None = None,
    source_tier: int | None = None,
    issuer_scoped: bool = True,
    confidence: float = 1.0,
    verified: bool = True,
    polarity: str = "positive",
    certainty: str = "confirmed",
) -> tuple[EvidenceClaim, ...]:
    """Compile already source-backed primitive ids into stable claims.

    This does not infer primitives. It only turns primitives that an upstream
    parser or verifier has already accepted into auditable claim records.
    """

    clean_primitives = tuple(dict.fromkeys(_clean_primitive_id(item) for item in primitive_ids if _clean_primitive_id(item)))
    return tuple(
        EvidenceClaim(
            claim_id=_stable_claim_id(
                evidence_id=evidence_id,
                symbol=symbol,
                archetype_id=archetype_id,
                primitive_id=primitive_id,
                polarity=polarity,
            ),
            evidence_id=evidence_id,
            symbol=symbol,
            archetype_id=archetype_id,
            primitive_id=primitive_id,
            subject=(subject or symbol).strip(),
            predicate=primitive_id,
            value=True,
            as_of_date=as_of_date,
            quote_text=quote_text.strip(),
            source_url=source_url,
            source_tier=source_tier,
            polarity=polarity,
            certainty=certainty,
            issuer_scoped=issuer_scoped,
            confidence=confidence,
            verified=verified,
        )
        for primitive_id in clean_primitives
    )


def compile_claims_from_parsed_fields(
    *,
    evidence_id: str,
    symbol: str,
    as_of_date: date,
    parsed_fields: Mapping[str, Any],
    archetype_id: str | None = None,
    subject: str | None = None,
    quote_text: str = "",
    source_url: str | None = None,
    source_tier: int | None = None,
    confidence: float = 1.0,
    max_claims: int = 80,
) -> tuple[EvidenceClaim, ...]:
    """Compile claim-worthy parsed fields into evidence claims."""

    claims: list[EvidenceClaim] = []
    for key in sorted(parsed_fields):
        if len(claims) >= max_claims:
            break
        primitive_id = _clean_primitive_id(key)
        if not _is_claim_primitive_key(primitive_id):
            continue
        value = parsed_fields.get(key)
        if not _is_claim_value(value):
            continue
        claims.append(
            EvidenceClaim(
                claim_id=_stable_claim_id(
                    evidence_id=evidence_id,
                    symbol=symbol,
                    archetype_id=archetype_id,
                    primitive_id=primitive_id,
                    polarity="positive",
                ),
                evidence_id=evidence_id,
                symbol=symbol,
                archetype_id=archetype_id,
                primitive_id=primitive_id,
                subject=(subject or symbol).strip(),
                predicate=primitive_id,
                value=value,
                as_of_date=as_of_date,
                quote_text=quote_text.strip(),
                source_url=source_url,
                source_tier=source_tier,
                confidence=max(0.0, min(1.0, confidence)),
                verified=True,
            )
        )
    return tuple(claims)


def claim_backed_parsed_fields(
    *,
    evidence_id: str,
    symbol: str,
    as_of_date: date,
    parsed_fields: Mapping[str, Any],
    archetype_id: str | None = None,
    subject: str | None = None,
    quote_text: str = "",
    source_url: str | None = None,
    source_tier: int | None = None,
    confidence: float = 1.0,
) -> Mapping[str, Any]:
    """Return parsed_fields with claim ledger metadata attached."""

    fields = dict(parsed_fields)
    if fields.get("claim_ledger_version"):
        return fields
    claims = compile_claims_from_parsed_fields(
        evidence_id=evidence_id,
        symbol=symbol,
        as_of_date=as_of_date,
        parsed_fields=fields,
        archetype_id=archetype_id,
        subject=subject,
        quote_text=quote_text,
        source_url=source_url,
        source_tier=source_tier,
        confidence=confidence,
    )
    if claims:
        fields.update(claim_metadata_from_claims(claims, as_of_date=as_of_date))
    return fields


def primitive_states_from_claims(
    claims: Sequence[EvidenceClaim],
    *,
    as_of_date: date,
) -> tuple[PrimitiveState, ...]:
    grouped: dict[str, list[EvidenceClaim]] = {}
    for claim in claims:
        grouped.setdefault(claim.primitive_id, []).append(claim)
    states: list[PrimitiveState] = []
    for primitive_id, primitive_claims in sorted(grouped.items()):
        support = tuple(claim.claim_id for claim in primitive_claims if claim.polarity in {"positive", "conditional"})
        counter = tuple(claim.claim_id for claim in primitive_claims if claim.polarity == "negative")
        if support and counter:
            status = "CONTRADICTED"
        elif support or counter:
            status = "PRESENT"
        else:
            status = "UNKNOWN"
        confidence = max((claim.confidence for claim in primitive_claims if claim.verified), default=0.0)
        freshness_days = min(max((as_of_date - claim.as_of_date).days, 0) for claim in primitive_claims)
        states.append(
            PrimitiveState(
                primitive_id=primitive_id,
                status=status,
                normalized_value=True if status == "PRESENT" else None,
                support_claim_ids=support,
                counter_claim_ids=counter,
                confidence=confidence,
                freshness_days=freshness_days,
            )
        )
    return tuple(states)


def claim_metadata_from_claims(
    claims: Sequence[EvidenceClaim],
    *,
    as_of_date: date,
) -> Mapping[str, Any]:
    """Return JSON-friendly parsed_fields metadata for compiled claims."""

    claim_tuple = tuple(claims)
    states = primitive_states_from_claims(claim_tuple, as_of_date=as_of_date)
    ids_by_primitive = {
        primitive_id: [claim.claim_id for claim in claim_tuple if claim.primitive_id == primitive_id]
        for primitive_id in sorted({claim.primitive_id for claim in claim_tuple})
    }
    return {
        "claim_ledger_version": CLAIM_LEDGER_VERSION,
        "compiled_claim_count": len(claim_tuple),
        "compiled_claim_ids": [claim.claim_id for claim in claim_tuple],
        "compiled_claim_ids_by_primitive": ids_by_primitive,
        "compiled_claims": [_claim_to_mapping(claim) for claim in claim_tuple],
        "compiled_primitive_states": {
            state.primitive_id: {
                "status": state.status,
                "normalized_value": state.normalized_value,
                "support_claim_ids": list(state.support_claim_ids),
                "counter_claim_ids": list(state.counter_claim_ids),
                "confidence": state.confidence,
                "freshness_days": state.freshness_days,
            }
            for state in states
        },
    }


def _claim_to_mapping(claim: EvidenceClaim) -> dict[str, Any]:
    return {
        "claim_id": claim.claim_id,
        "evidence_id": claim.evidence_id,
        "symbol": claim.symbol,
        "archetype_id": claim.archetype_id,
        "primitive_id": claim.primitive_id,
        "subject": claim.subject,
        "predicate": claim.predicate,
        "value": claim.value,
        "unit": claim.unit,
        "polarity": claim.polarity,
        "certainty": claim.certainty,
        "as_of_date": claim.as_of_date.isoformat(),
        "quote_text": claim.quote_text,
        "source_url": claim.source_url,
        "source_tier": claim.source_tier,
        "issuer_scoped": claim.issuer_scoped,
        "confidence": claim.confidence,
        "verified": claim.verified,
        "contradiction_group": claim.contradiction_group,
    }


def _stable_claim_id(
    *,
    evidence_id: str,
    symbol: str,
    archetype_id: str | None,
    primitive_id: str,
    polarity: str,
) -> str:
    payload = "|".join((evidence_id, symbol, archetype_id or "", primitive_id, polarity))
    digest = hashlib.sha1(payload.encode("utf-8")).hexdigest()[:16]
    return f"CLM-{digest}"


def _clean_primitive_id(value: str) -> str:
    return str(value or "").strip()


_CLAIM_KEY_PREFIX_EXCLUDES = (
    "compiled_",
    "claim_",
    "evidence_contract_",
    "runtime_fixture_",
    "source_",
    "raw_",
    "invalid_",
)

_CLAIM_KEY_EXCLUDES = {
    "analyst",
    "as_of_date",
    "broker",
    "canonical_archetype_id",
    "confidence",
    "date_verified",
    "document_type",
    "document_type_inferred_from_fetched_text",
    "evidence_id",
    "evidence_source_quality",
    "green_allowed_by_date",
    "large_sector_id",
    "parser_confidence",
    "published_at",
    "report_type",
    "search_snippet_date_unverified",
    "search_snippet_only",
    "title",
    "url",
}


def _is_claim_primitive_key(key: str) -> bool:
    if not key:
        return False
    if key in _CLAIM_KEY_EXCLUDES:
        return False
    if any(key.startswith(prefix) for prefix in _CLAIM_KEY_PREFIX_EXCLUDES):
        return False
    return True


def _is_claim_value(value: Any) -> bool:
    if value in (None, "", False):
        return False
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return math.isfinite(float(value)) and float(value) != 0.0
    if isinstance(value, str):
        return bool(value.strip()) and len(value.strip()) <= 300
    return False
