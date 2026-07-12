"""Compile accepted source-backed claims into deduplicated EvidenceFacts."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Any, Mapping, Sequence

from e2r.research_brain.intelligence_schema import stable_intelligence_id

from .schemas import EvidenceDirection, EvidenceFact, EvidenceLifecycle


@dataclass(frozen=True)
class FactCompilationRejection:
    claim_id: str
    reason: str

    def to_dict(self) -> Mapping[str, str]:
        return {"claim_id": self.claim_id, "reason": self.reason}


@dataclass(frozen=True)
class FactCompilationResult:
    facts: tuple[EvidenceFact, ...]
    rejected_claims: tuple[FactCompilationRejection, ...]
    input_claim_count: int
    accounted_claim_count: int
    duplicate_fact_merge_count: int

    def __post_init__(self) -> None:
        if self.accounted_claim_count != self.input_claim_count:
            raise ValueError("every claim must terminate in a fact or rejection")

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "facts": [row.to_dict() for row in self.facts],
            "rejected_claims": [row.to_dict() for row in self.rejected_claims],
            "input_claim_count": self.input_claim_count,
            "accounted_claim_count": self.accounted_claim_count,
            "duplicate_fact_merge_count": self.duplicate_fact_merge_count,
            "question_family_score_gateway": False,
            "primitive_score_gateway": False,
        }


class EvidenceFactCompiler:
    """Requires explicit economic semantics; it does not infer via keywords."""

    def compile(
        self,
        *,
        target_id: str,
        as_of_date: str,
        accepted_claims: Sequence[Mapping[str, Any]],
    ) -> FactCompilationResult:
        cutoff = date.fromisoformat(as_of_date)
        provisional: dict[str, EvidenceFact] = {}
        rejections = []
        merges = 0
        seen_claim_ids = set()
        for claim in accepted_claims:
            claim_id = str(claim.get("claim_id") or "").strip()
            if not claim_id:
                rejections.append(
                    FactCompilationRejection("MISSING_CLAIM_ID", "CLAIM_ID_REQUIRED")
                )
                continue
            if claim_id in seen_claim_ids:
                rejections.append(
                    FactCompilationRejection(claim_id, "DUPLICATE_CLAIM_ID")
                )
                continue
            seen_claim_ids.add(claim_id)
            if not _accepted(claim):
                rejections.append(
                    FactCompilationRejection(claim_id, "CLAIM_NOT_ACCEPTED")
                )
                continue
            claim_target = str(claim.get("target_id") or target_id).strip()
            if claim_target != target_id:
                rejections.append(
                    FactCompilationRejection(claim_id, "CROSS_TARGET_CLAIM")
                )
                continue
            claim_as_of = str(claim.get("as_of_date") or as_of_date).strip()
            if claim_as_of != as_of_date:
                rejections.append(
                    FactCompilationRejection(claim_id, "CLAIM_AS_OF_DATE_MISMATCH")
                )
                continue
            try:
                publication = _date_field(
                    claim, "published_at", "publication_date", "filed_at"
                )
            except ValueError:
                rejections.append(
                    FactCompilationRejection(claim_id, "INVALID_SOURCE_DATE")
                )
                continue
            if publication and publication > cutoff:
                rejections.append(
                    FactCompilationRejection(claim_id, "FUTURE_SOURCE_LEAKAGE")
                )
                continue
            missing = [
                key
                for key in (
                    "subject",
                    "economic_mechanism",
                    "predicate",
                    "period",
                    "direction",
                    "source_independence_group",
                )
                if not str(claim.get(key) or "").strip()
            ]
            source_ids = _source_ids(claim)
            if not source_ids:
                missing.append("source_ids")
            if missing:
                rejections.append(
                    FactCompilationRejection(
                        claim_id,
                        "EXPLICIT_FACT_FIELDS_MISSING:" + ",".join(sorted(missing)),
                    )
                )
                continue
            try:
                direction = EvidenceDirection(str(claim["direction"]).upper()).value
                lifecycle = EvidenceLifecycle(
                    str(claim.get("current_lifecycle") or "CURRENT").upper()
                ).value
                confidence = float(claim.get("confidence", 0.5))
                if not 0 <= confidence <= 1:
                    raise ValueError("confidence")
            except (TypeError, ValueError):
                rejections.append(
                    FactCompilationRejection(claim_id, "INVALID_FACT_ENUM_OR_CONFIDENCE")
                )
                continue
            identity = {
                "target_id": target_id,
                "as_of_date": as_of_date,
                "subject": str(claim["subject"]).strip(),
                "business_segment": str(claim.get("business_segment") or "").strip(),
                "product_family": str(claim.get("product_family") or "").strip(),
                "economic_mechanism": str(claim["economic_mechanism"]).strip(),
                "predicate": str(claim["predicate"]).strip(),
                "value": claim.get("value"),
                "unit": claim.get("unit"),
                "period": str(claim["period"]).strip(),
                "direction": direction,
                "current_lifecycle": lifecycle,
            }
            fact_id = stable_intelligence_id("EFACT", identity)
            quote_ids = tuple(
                dict.fromkeys(
                    str(value).strip()
                    for value in (
                        claim.get("quote_ids")
                        or ([claim.get("quote_id")] if claim.get("quote_id") else [])
                    )
                    if str(value).strip()
                )
            )
            if not quote_ids:
                quote_ids = (f"QUOTE-{claim_id}",)
            group = str(claim["source_independence_group"]).strip()
            existing = provisional.get(fact_id)
            if existing is None:
                provisional[fact_id] = EvidenceFact(
                    fact_id=fact_id,
                    target_id=target_id,
                    as_of_date=as_of_date,
                    subject=identity["subject"],
                    business_segment=identity["business_segment"],
                    product_family=identity["product_family"],
                    economic_mechanism=identity["economic_mechanism"],
                    predicate=identity["predicate"],
                    value=identity["value"],
                    unit=(str(identity["unit"]) if identity["unit"] is not None else None),
                    period=identity["period"],
                    direction=direction,
                    source_ids=source_ids,
                    claim_ids=(claim_id,),
                    quote_ids=quote_ids,
                    current_lifecycle=lifecycle,
                    source_independence_group=group,
                    confidence=confidence,
                    corroborating_independence_groups=(group,),
                    question_family_tags=_strings(claim.get("question_family_tags")),
                    primitive_tags=_strings(claim.get("primitive_tags")),
                )
            else:
                merges += 1
                groups = tuple(
                    dict.fromkeys((*existing.corroborating_independence_groups, group))
                )
                provisional[fact_id] = EvidenceFact(
                    **{
                        **existing.to_dict(),
                        "source_ids": tuple(
                            dict.fromkeys((*existing.source_ids, *source_ids))
                        ),
                        "claim_ids": tuple(
                            dict.fromkeys((*existing.claim_ids, claim_id))
                        ),
                        "quote_ids": tuple(
                            dict.fromkeys((*existing.quote_ids, *quote_ids))
                        ),
                        "confidence": max(existing.confidence, confidence),
                        "corroborating_independence_groups": groups,
                        "question_family_tags": tuple(
                            dict.fromkeys(
                                (*existing.question_family_tags, *_strings(claim.get("question_family_tags")))
                            )
                        ),
                        "primitive_tags": tuple(
                            dict.fromkeys(
                                (*existing.primitive_tags, *_strings(claim.get("primitive_tags")))
                            )
                        ),
                    }
                )
        return FactCompilationResult(
            facts=tuple(sorted(provisional.values(), key=lambda row: row.fact_id)),
            rejected_claims=tuple(rejections),
            input_claim_count=len(accepted_claims),
            accounted_claim_count=len(accepted_claims),
            duplicate_fact_merge_count=merges,
        )


def _accepted(claim: Mapping[str, Any]) -> bool:
    if claim.get("accepted_by_evidence_os") is True:
        return True
    return str(claim.get("status") or claim.get("claim_status") or "").upper() in {
        "ACCEPTED",
        "CURRENT_ACCEPTED",
        "SOURCE_BACKED_ACCEPTED",
    }


def _source_ids(claim: Mapping[str, Any]) -> tuple[str, ...]:
    values = claim.get("source_ids")
    if values is None:
        single = claim.get("source_id") or claim.get("document_id")
        values = [single] if single else []
    return _strings(values)


def _strings(value: Any) -> tuple[str, ...]:
    if value is None:
        return ()
    if isinstance(value, str):
        values = [value]
    else:
        values = value
    return tuple(
        dict.fromkeys(str(item).strip() for item in values if str(item).strip())
    )


def _date_field(claim: Mapping[str, Any], *keys: str) -> date | None:
    raw = next((str(claim.get(key)) for key in keys if claim.get(key)), "")
    if not raw:
        return None
    try:
        return date.fromisoformat(raw[:10])
    except ValueError as exc:
        raise ValueError(f"invalid source date: {raw}") from exc


__all__ = [
    "EvidenceFactCompiler",
    "FactCompilationRejection",
    "FactCompilationResult",
]
