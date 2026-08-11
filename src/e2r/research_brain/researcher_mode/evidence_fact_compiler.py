"""Compile every material claim into a deduplicated, source-backed EvidenceFact."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import date
import json
import math
import re
from typing import Any, Mapping, Sequence

from e2r.research_brain.intelligence_schema import stable_intelligence_id

from .schemas import EvidenceDirection, EvidenceFact, EvidenceLifecycle


CLAIM_FACT_LINK_ROLES = (
    "PRIMARY_FACT_CLAIM",
    "INDEPENDENT_CORROBORATION",
    "SAME_GROUP_DUPLICATE",
)


@dataclass(frozen=True)
class FactCompilationRejection:
    claim_id: str
    reason: str
    accepted_claim: bool = False
    material_claim: bool = True
    input_index: int = 0
    utilization_status: str = "REJECTED_WITH_REASON"

    def __post_init__(self) -> None:
        if not self.claim_id.strip() or not self.reason.strip():
            raise ValueError("fact compilation rejection requires identity and reason")
        if self.utilization_status != "REJECTED_WITH_REASON":
            raise ValueError("fact compilation rejection has invalid utilization status")

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class ClaimFactLink:
    link_id: str
    claim_id: str
    fact_id: str
    economic_fact_key: str
    link_role: str
    source_ids: tuple[str, ...]
    source_independence_group: str
    claim_confidence: float
    material_claim: bool
    current_lifecycle: str
    supersedes_fact_ids: tuple[str, ...] = ()
    resolves_fact_ids: tuple[str, ...] = ()
    input_index: int = 0
    production_score_authority: bool = False
    schema_version: str = "e2r_claim_fact_link_v1"

    def __post_init__(self) -> None:
        if self.link_role not in CLAIM_FACT_LINK_ROLES:
            raise ValueError("unknown claim/fact link role")
        if not all(
            value.strip()
            for value in (
                self.link_id,
                self.claim_id,
                self.fact_id,
                self.economic_fact_key,
                self.source_independence_group,
            )
        ):
            raise ValueError("claim/fact link identity is incomplete")
        if not 0 <= self.claim_confidence <= 1:
            raise ValueError("claim/fact link confidence is invalid")
        if not self.source_ids or len(self.source_ids) != len(set(self.source_ids)):
            raise ValueError("claim/fact link requires unique source ids")
        if len(self.supersedes_fact_ids) != len(set(self.supersedes_fact_ids)):
            raise ValueError("superseded fact ids must be unique")
        if len(self.resolves_fact_ids) != len(set(self.resolves_fact_ids)):
            raise ValueError("resolved fact ids must be unique")
        if self.production_score_authority:
            raise ValueError("claim/fact links cannot assign production score")

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class FactCompilationResult:
    target_id: str
    as_of_date: str
    facts: tuple[EvidenceFact, ...]
    claim_fact_links: tuple[ClaimFactLink, ...]
    rejected_claims: tuple[FactCompilationRejection, ...]
    input_claim_count: int
    accounted_claim_count: int
    accepted_claim_count: int
    accepted_claim_without_fact_count: int
    material_claim_without_terminal_count: int
    duplicate_fact_merge_count: int
    independent_corroboration_count: int
    status: str
    fact_graph_ready: bool
    production_score_authority: bool = False
    schema_version: str = "e2r_fact_compilation_result_v2"

    def __post_init__(self) -> None:
        if not self.target_id.strip():
            raise ValueError("fact compilation target id is required")
        date.fromisoformat(self.as_of_date)
        if self.status not in {
            "FACT_COMPILATION_COMPLETE",
            "FACT_COMPILATION_INVALID_ACCEPTED_CLAIM",
        }:
            raise ValueError("unknown fact compilation status")
        if self.accounted_claim_count != self.input_claim_count:
            raise ValueError("every claim must terminate in a fact link or rejection")
        if self.accounted_claim_count != len(self.claim_fact_links) + len(
            self.rejected_claims
        ):
            raise ValueError("claim accounting leaves do not reconcile")
        if self.accepted_claim_count != len(self.claim_fact_links) + sum(
            row.accepted_claim for row in self.rejected_claims
        ):
            raise ValueError("accepted claim count does not reconcile")
        if self.accepted_claim_without_fact_count != sum(
            row.accepted_claim for row in self.rejected_claims
        ):
            raise ValueError("accepted-claim fact gap count does not reconcile")
        if self.material_claim_without_terminal_count:
            raise ValueError("material claims cannot disappear without a terminal row")
        if self.fact_graph_ready != (
            self.status == "FACT_COMPILATION_COMPLETE"
            and self.accepted_claim_without_fact_count == 0
        ):
            raise ValueError("fact compilation ready flag disagrees with critical gaps")
        if self.production_score_authority:
            raise ValueError("fact compiler cannot assign production score")
        fact_by_id = {row.fact_id: row for row in self.facts}
        if len(fact_by_id) != len(self.facts):
            raise ValueError("EvidenceFact ids must be unique")
        link_claim_ids = [row.claim_id for row in self.claim_fact_links]
        if len(link_claim_ids) != len(set(link_claim_ids)):
            raise ValueError("one accepted claim must link to exactly one EvidenceFact")
        if any(row.fact_id not in fact_by_id for row in self.claim_fact_links):
            raise ValueError("claim/fact link references an unknown fact")
        if any(
            row.target_id != self.target_id or row.as_of_date != self.as_of_date
            for row in self.facts
        ):
            raise ValueError("compiled facts cross the result target or cutoff")
        for fact in self.facts:
            linked = {
                row.claim_id
                for row in self.claim_fact_links
                if row.fact_id == fact.fact_id
            }
            if linked != set(fact.claim_ids):
                raise ValueError("EvidenceFact claim lineage does not match links")

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "schema_version": self.schema_version,
            "status": self.status,
            "target_id": self.target_id,
            "as_of_date": self.as_of_date,
            "facts": [row.to_dict() for row in self.facts],
            "claim_fact_links": [row.to_dict() for row in self.claim_fact_links],
            "rejected_claims": [row.to_dict() for row in self.rejected_claims],
            "input_claim_count": self.input_claim_count,
            "accounted_claim_count": self.accounted_claim_count,
            "accepted_claim_count": self.accepted_claim_count,
            "accepted_claim_without_fact_count": (
                self.accepted_claim_without_fact_count
            ),
            "material_claim_without_terminal_count": (
                self.material_claim_without_terminal_count
            ),
            "duplicate_fact_merge_count": self.duplicate_fact_merge_count,
            "independent_corroboration_count": (
                self.independent_corroboration_count
            ),
            "fact_graph_ready": self.fact_graph_ready,
            "production_score_authority": False,
            "question_family_score_gateway": False,
            "primitive_score_gateway": False,
        }


@dataclass(frozen=True)
class _PreparedClaim:
    input_index: int
    claim_id: str
    fact_id: str
    economic_fact_key: str
    target_id: str
    as_of_date: str
    subject: str
    business_segment: str
    product_family: str
    economic_mechanism: str
    predicate: str
    value: Any
    unit: str | None
    period: str
    direction: str
    current_lifecycle: str
    source_ids: tuple[str, ...]
    quote_ids: tuple[str, ...]
    source_independence_group: str
    confidence: float
    question_family_tags: tuple[str, ...]
    primitive_tags: tuple[str, ...]
    allowed_component_ids: tuple[str, ...]
    structured_evidence_roles: tuple[str, ...]
    supersedes_fact_ids: tuple[str, ...]
    resolves_fact_ids: tuple[str, ...]
    material_claim: bool


class EvidenceFactCompiler:
    """Compile explicit economic semantics; tags never decide score eligibility."""

    def compile(
        self,
        *,
        target_id: str,
        as_of_date: str,
        accepted_claims: Sequence[Mapping[str, Any]],
    ) -> FactCompilationResult:
        cutoff = date.fromisoformat(as_of_date)
        if not target_id.strip():
            raise ValueError("fact compilation target id is required")
        prepared: list[_PreparedClaim] = []
        rejections: list[FactCompilationRejection] = []
        seen_claim_ids: set[str] = set()
        accepted_count = 0
        for input_index, claim in enumerate(accepted_claims):
            material = _material_claim(claim)
            accepted = _accepted(claim)
            accepted_count += int(accepted)
            claim_id = str(claim.get("claim_id") or "").strip()
            if not claim_id:
                rejections.append(
                    FactCompilationRejection(
                        claim_id=f"MISSING_CLAIM_ID:{input_index}",
                        reason="CLAIM_ID_REQUIRED",
                        accepted_claim=accepted,
                        material_claim=material,
                        input_index=input_index,
                    )
                )
                continue
            if claim_id in seen_claim_ids:
                rejections.append(
                    FactCompilationRejection(
                        claim_id=claim_id,
                        reason="DUPLICATE_CLAIM_ID",
                        accepted_claim=accepted,
                        material_claim=material,
                        input_index=input_index,
                    )
                )
                continue
            seen_claim_ids.add(claim_id)
            rejection = _prepare_claim(
                claim,
                input_index=input_index,
                claim_id=claim_id,
                target_id=target_id,
                as_of_date=as_of_date,
                cutoff=cutoff,
                accepted=accepted,
                material=material,
            )
            if isinstance(rejection, FactCompilationRejection):
                rejections.append(rejection)
            else:
                prepared.append(rejection)

        cyclic_fact_ids = _cyclic_fact_lineage_ids(prepared)
        if cyclic_fact_ids:
            noncyclic: list[_PreparedClaim] = []
            for row in prepared:
                if row.fact_id in cyclic_fact_ids:
                    rejections.append(
                        FactCompilationRejection(
                            claim_id=row.claim_id,
                            reason="CYCLIC_FACT_LINEAGE",
                            accepted_claim=True,
                            material_claim=row.material_claim,
                            input_index=row.input_index,
                        )
                    )
                else:
                    noncyclic.append(row)
            prepared = noncyclic

        grouped: dict[str, list[_PreparedClaim]] = {}
        for claim in prepared:
            grouped.setdefault(claim.fact_id, []).append(claim)
        facts: list[EvidenceFact] = []
        links: list[ClaimFactLink] = []
        merge_count = 0
        independent_count = 0
        canonical_index_by_claim = {
            claim_id: index
            for index, claim_id in enumerate(
                sorted(row.claim_id for row in prepared)
            )
        }
        for fact_id in sorted(grouped):
            claims = sorted(
                grouped[fact_id],
                key=lambda row: (-row.confidence, row.claim_id, row.input_index),
            )
            primary = claims[0]
            independence_cluster_by_claim = _independence_clusters(claims)
            confidence_by_group: dict[str, float] = {}
            for claim in claims:
                cluster_id = independence_cluster_by_claim[claim.claim_id]
                confidence_by_group[cluster_id] = max(
                    confidence_by_group.get(cluster_id, 0.0),
                    claim.confidence,
                )
            combined_confidence = 1.0
            for confidence in confidence_by_group.values():
                combined_confidence *= 1.0 - confidence
            combined_confidence = round(1.0 - combined_confidence, 12)
            representative_group_by_cluster: dict[str, str] = {}
            for claim in claims:
                representative_group_by_cluster.setdefault(
                    independence_cluster_by_claim[claim.claim_id],
                    claim.source_independence_group,
                )
            groups = tuple(sorted(representative_group_by_cluster.values()))
            fact = EvidenceFact(
                fact_id=fact_id,
                target_id=primary.target_id,
                as_of_date=primary.as_of_date,
                subject=primary.subject,
                business_segment=primary.business_segment,
                product_family=primary.product_family,
                economic_mechanism=primary.economic_mechanism,
                predicate=primary.predicate,
                value=primary.value,
                unit=primary.unit,
                period=primary.period,
                direction=primary.direction,
                source_ids=tuple(
                    sorted({value for row in claims for value in row.source_ids})
                ),
                claim_ids=tuple(row.claim_id for row in claims),
                quote_ids=tuple(
                    sorted({value for row in claims for value in row.quote_ids})
                ),
                current_lifecycle=primary.current_lifecycle,
                source_independence_group=primary.source_independence_group,
                confidence=combined_confidence,
                corroborating_independence_groups=groups,
                question_family_tags=tuple(
                    sorted(
                        {
                            value
                            for row in claims
                            for value in row.question_family_tags
                        }
                    )
                ),
                primitive_tags=tuple(
                    sorted(
                        {value for row in claims for value in row.primitive_tags}
                    )
                ),
                allowed_component_ids=primary.allowed_component_ids,
                structured_evidence_roles=tuple(
                    sorted(
                        {
                            value
                            for row in claims
                            for value in row.structured_evidence_roles
                        }
                    )
                ),
            )
            facts.append(fact)
            seen_groups: set[str] = set()
            for index, claim in enumerate(claims):
                cluster_id = independence_cluster_by_claim[claim.claim_id]
                if index == 0:
                    role = "PRIMARY_FACT_CLAIM"
                elif cluster_id not in seen_groups:
                    role = "INDEPENDENT_CORROBORATION"
                    independent_count += 1
                else:
                    role = "SAME_GROUP_DUPLICATE"
                seen_groups.add(cluster_id)
                links.append(
                    ClaimFactLink(
                        link_id=stable_intelligence_id(
                            "CFLINK",
                            {
                                "claim_id": claim.claim_id,
                                "fact_id": fact_id,
                                "role": role,
                            },
                        ),
                        claim_id=claim.claim_id,
                        fact_id=fact_id,
                        economic_fact_key=claim.economic_fact_key,
                        link_role=role,
                        source_ids=claim.source_ids,
                        source_independence_group=(
                            claim.source_independence_group
                        ),
                        claim_confidence=claim.confidence,
                        material_claim=claim.material_claim,
                        current_lifecycle=claim.current_lifecycle,
                        supersedes_fact_ids=claim.supersedes_fact_ids,
                        resolves_fact_ids=claim.resolves_fact_ids,
                        input_index=canonical_index_by_claim[claim.claim_id],
                    )
                )
            merge_count += len(claims) - 1

        accepted_without_fact = sum(row.accepted_claim for row in rejections)
        status = (
            "FACT_COMPILATION_COMPLETE"
            if accepted_without_fact == 0
            else "FACT_COMPILATION_INVALID_ACCEPTED_CLAIM"
        )
        return FactCompilationResult(
            target_id=target_id,
            as_of_date=as_of_date,
            facts=tuple(facts),
            claim_fact_links=tuple(
                sorted(links, key=lambda row: (row.fact_id, row.claim_id))
            ),
            rejected_claims=tuple(
                sorted(rejections, key=lambda row: (row.input_index, row.claim_id))
            ),
            input_claim_count=len(accepted_claims),
            accounted_claim_count=len(links) + len(rejections),
            accepted_claim_count=accepted_count,
            accepted_claim_without_fact_count=accepted_without_fact,
            material_claim_without_terminal_count=0,
            duplicate_fact_merge_count=merge_count,
            independent_corroboration_count=independent_count,
            status=status,
            fact_graph_ready=status == "FACT_COMPILATION_COMPLETE",
        )


def _prepare_claim(
    claim: Mapping[str, Any],
    *,
    input_index: int,
    claim_id: str,
    target_id: str,
    as_of_date: str,
    cutoff: date,
    accepted: bool,
    material: bool,
) -> _PreparedClaim | FactCompilationRejection:
    def reject(reason: str) -> FactCompilationRejection:
        return FactCompilationRejection(
            claim_id=claim_id,
            reason=reason,
            accepted_claim=accepted,
            material_claim=material,
            input_index=input_index,
        )

    if not accepted:
        return reject("CLAIM_NOT_ACCEPTED")
    claim_target = str(claim.get("target_id") or target_id).strip()
    if claim_target != target_id:
        return reject("CROSS_TARGET_CLAIM")
    claim_as_of = str(claim.get("as_of_date") or as_of_date).strip()
    if claim_as_of != as_of_date:
        return reject("CLAIM_AS_OF_DATE_MISMATCH")
    try:
        publication = _date_field(
            claim,
            "published_at",
            "publication_date",
            "filed_at",
            "observed_at",
        )
    except ValueError:
        return reject("INVALID_SOURCE_DATE")
    if publication and publication > cutoff:
        return reject("FUTURE_SOURCE_LEAKAGE")
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
        return reject("EXPLICIT_FACT_FIELDS_MISSING:" + ",".join(sorted(missing)))
    try:
        direction = EvidenceDirection(str(claim["direction"]).upper()).value
        lifecycle = EvidenceLifecycle(
            str(claim.get("current_lifecycle") or "CURRENT").upper()
        ).value
        confidence_value = claim.get("confidence", 0.5)
        if isinstance(confidence_value, bool):
            raise ValueError("confidence")
        confidence = float(confidence_value)
        if not math.isfinite(confidence) or not 0 <= confidence <= 1:
            raise ValueError("confidence")
        _validate_finite_value(claim.get("value"))
    except (TypeError, ValueError):
        return reject("INVALID_FACT_ENUM_VALUE_OR_CONFIDENCE")
    identity = {
        "target_id": target_id,
        "as_of_date": as_of_date,
        "subject": _normalize_text(claim["subject"]),
        "business_segment": _normalize_text(claim.get("business_segment")),
        "product_family": _normalize_text(claim.get("product_family")),
        "economic_mechanism": _normalize_text(claim["economic_mechanism"]),
        "predicate": _normalize_text(claim["predicate"]),
        "value": _canonical_value(claim.get("value")),
        "unit": _normalize_text(claim.get("unit")),
        "period": _normalize_text(claim["period"]),
        "direction": direction,
        "current_lifecycle": lifecycle,
    }
    fact_id = stable_intelligence_id("EFACT", identity)
    quote_ids = _quote_ids(claim, claim_id=claim_id, source_ids=source_ids)
    supersedes_fact_ids = _strings(claim.get("supersedes_fact_ids"))
    resolves_fact_ids = _strings(claim.get("resolves_fact_ids"))
    if fact_id in {*supersedes_fact_ids, *resolves_fact_ids}:
        return reject("SELF_REFERENTIAL_FACT_LINEAGE")
    return _PreparedClaim(
        input_index=input_index,
        claim_id=claim_id,
        fact_id=fact_id,
        economic_fact_key=stable_intelligence_id("EKEY", identity),
        target_id=target_id,
        as_of_date=as_of_date,
        subject=str(claim["subject"]).strip(),
        business_segment=str(claim.get("business_segment") or "").strip(),
        product_family=str(claim.get("product_family") or "").strip(),
        economic_mechanism=str(claim["economic_mechanism"]).strip(),
        predicate=str(claim["predicate"]).strip(),
        value=claim.get("value"),
        unit=(str(claim["unit"]).strip() if claim.get("unit") is not None else None),
        period=str(claim["period"]).strip(),
        direction=direction,
        current_lifecycle=lifecycle,
        source_ids=source_ids,
        quote_ids=quote_ids,
        source_independence_group=str(
            claim["source_independence_group"]
        ).strip(),
        confidence=confidence,
        question_family_tags=_strings(claim.get("question_family_tags")),
        primitive_tags=_strings(claim.get("primitive_tags")),
        allowed_component_ids=_strings(claim.get("allowed_component_ids")),
        structured_evidence_roles=_strings(
            claim.get("structured_evidence_roles")
        ),
        supersedes_fact_ids=supersedes_fact_ids,
        resolves_fact_ids=resolves_fact_ids,
        material_claim=material,
    )


def _cyclic_fact_lineage_ids(
    claims: Sequence[_PreparedClaim],
) -> frozenset[str]:
    """Return compiled fact ids participating in a replacement cycle."""

    fact_ids = {row.fact_id for row in claims}
    edges: dict[str, set[str]] = {fact_id: set() for fact_id in fact_ids}
    for row in claims:
        edges[row.fact_id].update(
            fact_id
            for fact_id in (
                *row.supersedes_fact_ids,
                *row.resolves_fact_ids,
            )
            if fact_id in fact_ids
        )
    visiting: list[str] = []
    visiting_index: dict[str, int] = {}
    visited: set[str] = set()
    cyclic: set[str] = set()

    def visit(fact_id: str) -> None:
        if fact_id in visited:
            return
        if fact_id in visiting_index:
            cyclic.update(visiting[visiting_index[fact_id] :])
            return
        visiting_index[fact_id] = len(visiting)
        visiting.append(fact_id)
        for related_fact_id in sorted(edges[fact_id]):
            visit(related_fact_id)
        visiting.pop()
        visiting_index.pop(fact_id, None)
        visited.add(fact_id)

    for fact_id in sorted(fact_ids):
        visit(fact_id)
    return frozenset(cyclic)


def _accepted(claim: Mapping[str, Any]) -> bool:
    if claim.get("accepted_by_evidence_os") is True or claim.get("accepted") is True:
        return True
    return str(claim.get("status") or claim.get("claim_status") or "").upper() in {
        "ACCEPTED",
        "CURRENT_ACCEPTED",
        "SOURCE_BACKED_ACCEPTED",
    }


def _material_claim(claim: Mapping[str, Any]) -> bool:
    if claim.get("material") is not None:
        return claim.get("material") is True
    return str(claim.get("materiality") or "MATERIAL").upper() != "IMMATERIAL"


def _source_ids(claim: Mapping[str, Any]) -> tuple[str, ...]:
    values = claim.get("source_ids")
    if values is None:
        single = claim.get("source_id") or claim.get("document_id")
        values = [single] if single else []
    return _strings(values)


def _quote_ids(
    claim: Mapping[str, Any], *, claim_id: str, source_ids: Sequence[str]
) -> tuple[str, ...]:
    values = claim.get("quote_ids") or (
        [claim.get("quote_id")] if claim.get("quote_id") else []
    )
    result = _strings(values)
    if result:
        return result
    quote_text = str(claim.get("exact_quote") or claim.get("quote_text") or "").strip()
    return (
        stable_intelligence_id(
            "QUOTE",
            {
                "claim_id": claim_id,
                "source_ids": list(source_ids),
                "quote_text": quote_text,
            },
        ),
    )


def _strings(value: Any) -> tuple[str, ...]:
    if value is None:
        return ()
    if isinstance(value, str):
        values = [value]
    elif isinstance(value, (list, tuple, set)):
        values = value
    else:
        return ()
    result = tuple(str(item).strip() for item in values if str(item).strip())
    return tuple(dict.fromkeys(result))


def _date_field(claim: Mapping[str, Any], *keys: str) -> date | None:
    raw = next((str(claim.get(key)) for key in keys if claim.get(key)), "")
    if not raw:
        return None
    try:
        return date.fromisoformat(raw[:10])
    except ValueError as exc:
        raise ValueError(f"invalid source date: {raw}") from exc


def _normalize_text(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "").strip()).casefold()


def _canonical_value(value: Any) -> Any:
    return json.loads(json.dumps(value, ensure_ascii=False, sort_keys=True, default=str))


def _validate_finite_value(value: Any) -> None:
    if isinstance(value, float) and not math.isfinite(value):
        raise ValueError("non-finite fact value")
    if isinstance(value, Mapping):
        for nested in value.values():
            _validate_finite_value(nested)
    elif isinstance(value, (list, tuple)):
        for nested in value:
            _validate_finite_value(nested)


def _independence_clusters(
    claims: Sequence[_PreparedClaim],
) -> Mapping[str, str]:
    parents = list(range(len(claims)))

    def find(index: int) -> int:
        while parents[index] != index:
            parents[index] = parents[parents[index]]
            index = parents[index]
        return index

    def union(left: int, right: int) -> None:
        left_root = find(left)
        right_root = find(right)
        if left_root != right_root:
            parents[max(left_root, right_root)] = min(left_root, right_root)

    for left, left_claim in enumerate(claims):
        for right in range(left + 1, len(claims)):
            right_claim = claims[right]
            if (
                _normalize_text(left_claim.source_independence_group)
                == _normalize_text(right_claim.source_independence_group)
                or set(left_claim.source_ids) & set(right_claim.source_ids)
            ):
                union(left, right)
    members: dict[int, list[str]] = {}
    for index, claim in enumerate(claims):
        members.setdefault(find(index), []).append(claim.claim_id)
    cluster_id_by_root = {
        root: stable_intelligence_id("INDGROUP", sorted(claim_ids))
        for root, claim_ids in members.items()
    }
    return {
        claim.claim_id: cluster_id_by_root[find(index)]
        for index, claim in enumerate(claims)
    }


__all__ = [
    "CLAIM_FACT_LINK_ROLES",
    "ClaimFactLink",
    "EvidenceFactCompiler",
    "FactCompilationRejection",
    "FactCompilationResult",
]
