"""Provider-backed semantic claim→component impact mapping before deterministic caps."""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.metadata import write_json
from e2r.research_brain.intelligence_schema import stable_intelligence_id
from e2r.research_brain.planning.provider_transport import (
    StructuredProviderRejected,
    StructuredProviderUnavailable,
)

from .claim_utilization import (
    COMPONENT_MECHANISM_IDS_BY_COMPONENT,
    ClaimComponentImpactProposal,
    ClaimTerminalDisposition,
)
from .component_researcher import ComponentResearchResult, StructuredResearchProvider
from .evidence_fact_compiler import FactCompilationResult
from .schemas import (
    CANONICAL_COMPONENT_ORDER,
    assert_blind_research_output,
    scrub_blind_research_payload,
)


CLAIM_IMPACT_MAPPING_OUTPUT_FILE = "claim_impact_mapping.json"


@dataclass(frozen=True)
class ClaimImpactMappingResult:
    status: str
    impact_proposals: tuple[ClaimComponentImpactProposal, ...]
    explicit_dispositions: tuple[ClaimTerminalDisposition, ...]
    unresolved_claim_ids: tuple[str, ...]
    pending_reasons: tuple[str, ...]
    provider_name: str
    prompt_hash: str | None
    mapping_complete: bool
    production_score_authority: bool = False
    schema_version: str = "e2r_claim_impact_mapping_result_v1"

    def __post_init__(self) -> None:
        if self.status not in {"COMPLETE", "PENDING"}:
            raise ValueError("unknown claim impact mapping status")
        if self.mapping_complete != (self.status == "COMPLETE"):
            raise ValueError("claim impact mapping status and complete flag disagree")
        if self.status == "PENDING" and not self.pending_reasons:
            raise ValueError("pending claim impact mapping requires reasons")
        if self.status == "COMPLETE" and (
            self.unresolved_claim_ids or self.pending_reasons
        ):
            raise ValueError("complete claim impact mapping cannot have gaps")
        if self.production_score_authority:
            raise ValueError("claim impact mapping cannot assign production score")

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "schema_version": self.schema_version,
            "status": self.status,
            "impact_proposals": [row.to_dict() for row in self.impact_proposals],
            "explicit_dispositions": [
                row.to_dict() for row in self.explicit_dispositions
            ],
            "unresolved_claim_ids": list(self.unresolved_claim_ids),
            "pending_reasons": list(self.pending_reasons),
            "provider_name": self.provider_name,
            "prompt_hash": self.prompt_hash,
            "mapping_complete": self.mapping_complete,
            "production_score_authority": False,
        }

    def to_score_gap_context(self) -> Mapping[str, Any]:
        return {
            "claim_impact_mapping_status": self.status,
            "unresolved_claim_ids": list(self.unresolved_claim_ids),
            "pending_reasons": list(self.pending_reasons),
            "provider_name": self.provider_name,
            "prompt_hash": self.prompt_hash,
        }


class ClaimComponentImpactMapper:
    """Ask the LLM for semantic mappings; deterministic code validates all edges."""

    def __init__(self, *, provider: StructuredResearchProvider | None) -> None:
        self.provider = provider

    def map(
        self,
        *,
        fact_compilation: FactCompilationResult,
        component_results: Sequence[ComponentResearchResult],
    ) -> ClaimImpactMappingResult:
        provider_name = (
            str(getattr(self.provider, "provider_name", type(self.provider).__name__))
            if self.provider is not None
            else "UNCONFIGURED"
        )
        if not fact_compilation.fact_graph_ready:
            return _pending(
                provider_name=provider_name,
                reason="FACT_COMPILATION_NOT_READY",
                unresolved_claim_ids=tuple(
                    sorted(
                        row.claim_id
                        for row in fact_compilation.rejected_claims
                        if row.accepted_claim
                    )
                ),
            )
        component_ids = [row.component_id for row in component_results]
        complete_components = bool(
            len(component_ids) == len(CANONICAL_COMPONENT_ORDER)
            and set(component_ids) == set(CANONICAL_COMPONENT_ORDER)
            and len(component_ids) == len(set(component_ids))
            and all(row.status == "COMPLETE" and row.memo for row in component_results)
        )
        if any(
            row.memo
            and row.memo.target_id != fact_compilation.target_id
            for row in component_results
        ):
            raise ValueError("claim impact mapper target mismatch")
        primary_claim_ids = _primary_material_current_claim_ids(fact_compilation)
        if not complete_components:
            return _pending(
                provider_name=provider_name,
                reason="SEVEN_COMPONENT_MEMOS_INCOMPLETE",
                unresolved_claim_ids=primary_claim_ids,
            )
        if not primary_claim_ids:
            return ClaimImpactMappingResult(
                status="COMPLETE",
                impact_proposals=(),
                explicit_dispositions=(),
                unresolved_claim_ids=(),
                pending_reasons=(),
                provider_name="NO_SEMANTIC_MAPPING_REQUIRED",
                prompt_hash=None,
                mapping_complete=True,
            )
        if self.provider is None:
            return _pending(
                provider_name=provider_name,
                reason="CLAIM_IMPACT_MAPPING_PROVIDER_NOT_CONFIGURED",
                unresolved_claim_ids=primary_claim_ids,
            )
        payload = scrub_blind_research_payload(
            {
                "evidence_facts": [
                    row.to_dict() for row in fact_compilation.facts
                ],
                "claim_fact_links": [
                    row.to_dict() for row in fact_compilation.claim_fact_links
                ],
                "component_research_memos": [
                    row.memo.to_dict() for row in component_results if row.memo
                ],
                "component_mechanism_contract": {
                    key: list(value)
                    for key, value in COMPONENT_MECHANISM_IDS_BY_COMPONENT.items()
                },
                "primary_material_current_claim_ids": list(primary_claim_ids),
                "question_family_score_gateway": False,
                "primitive_score_gateway": False,
            }
        )
        prompt_hash = _payload_hash(payload)
        try:
            response = self.provider.complete(
                pass_name="CLAIM_COMPONENT_IMPACT_MAPPING",
                payload=payload,
            )
            assert_blind_research_output(response)
            prompt_hash = _provider_prompt_hash(self.provider, payload)
            return _decode_mapping_response(
                response=response,
                fact_compilation=fact_compilation,
                component_results=component_results,
                provider_name=provider_name,
                prompt_hash=prompt_hash,
            )
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
            return _pending(
                provider_name=provider_name,
                reason=(
                    f"CLAIM_IMPACT_PROVIDER_OR_OUTPUT_ERROR:"
                    f"{type(exc).__name__}:{exc}"
                ),
                unresolved_claim_ids=primary_claim_ids,
                prompt_hash=prompt_hash,
            )


def write_claim_impact_mapping_result(
    result: ClaimImpactMappingResult,
    output_directory: str | Path,
) -> Path:
    destination = Path(output_directory) / CLAIM_IMPACT_MAPPING_OUTPUT_FILE
    write_json(destination, result.to_dict())
    return destination


def _decode_mapping_response(
    *,
    response: Mapping[str, Any],
    fact_compilation: FactCompilationResult,
    component_results: Sequence[ComponentResearchResult],
    provider_name: str,
    prompt_hash: str,
) -> ClaimImpactMappingResult:
    expected_keys = {
        "impact_proposals",
        "non_scoring_dispositions",
        "mapping_complete",
        "unresolved_claim_ids",
        "rationale",
    }
    if set(response) != expected_keys:
        raise ValueError("claim impact mapper response keys do not match schema")
    mapping_complete = _required_bool(response, "mapping_complete")
    _required_text(response, "rationale")
    links = {row.claim_id: row for row in fact_compilation.claim_fact_links}
    facts = {row.fact_id: row for row in fact_compilation.facts}
    memo_by_component = {
        row.component_id: row.memo
        for row in component_results
        if row.memo is not None
    }
    proposals = []
    proposal_keys = set()
    for row in _mapping_rows(response, "impact_proposals"):
        if set(row) != {
            "claim_id",
            "fact_id",
            "component_id",
            "direction",
            "component_mechanism_id",
            "fact_economic_mechanism",
            "proposed_credit_units",
            "rationale",
        }:
            raise ValueError("claim impact proposal keys do not match schema")
        claim_id = _required_text(row, "claim_id")
        fact_id = _required_text(row, "fact_id")
        component_id = _required_text(row, "component_id")
        direction = _required_text(row, "direction")
        link = links.get(claim_id)
        fact = facts.get(fact_id)
        memo = memo_by_component.get(component_id)
        if link is None or link.link_role != "PRIMARY_FACT_CLAIM":
            raise ValueError("impact mapper cited a non-primary or unknown claim")
        if link.fact_id != fact_id or fact is None:
            raise ValueError("impact mapper claim/fact lineage mismatch")
        if memo is None:
            raise ValueError("impact mapper cited a component without a memo")
        expected_fact_ids = (
            memo.positive_fact_ids if direction == "SUPPORT" else memo.counter_fact_ids
        )
        if fact_id not in expected_fact_ids:
            raise ValueError("impact direction is not supported by the component memo")
        component_mechanism_id = _required_text(row, "component_mechanism_id")
        if component_mechanism_id not in set(
            COMPONENT_MECHANISM_IDS_BY_COMPONENT.get(component_id, ())
        ):
            raise ValueError("impact mapper used an invalid component mechanism")
        fact_economic_mechanism = _required_text(
            row, "fact_economic_mechanism"
        )
        if _normalize_text(fact_economic_mechanism) != _normalize_text(
            fact.economic_mechanism
        ):
            raise ValueError("impact mapper changed the fact economic mechanism")
        proposed_credit_units = row["proposed_credit_units"]
        if isinstance(proposed_credit_units, bool) or not isinstance(
            proposed_credit_units, (int, float)
        ):
            raise TypeError("proposed_credit_units must be numeric")
        key = (claim_id, fact_id, component_id, direction, component_mechanism_id)
        if key in proposal_keys:
            raise ValueError("impact mapper repeated one economic credit edge")
        proposal_keys.add(key)
        proposals.append(
            ClaimComponentImpactProposal(
                impact_id=stable_intelligence_id(
                    "CMAPIMPACT",
                    {
                        "claim_id": claim_id,
                        "fact_id": fact_id,
                        "component_id": component_id,
                        "direction": direction,
                        "component_mechanism_id": component_mechanism_id,
                        "prompt_hash": prompt_hash,
                    },
                ),
                claim_id=claim_id,
                fact_id=fact_id,
                component_id=component_id,
                direction=direction,
                component_mechanism_id=component_mechanism_id,
                fact_economic_mechanism=fact_economic_mechanism,
                proposed_credit_units=float(proposed_credit_units),
                rationale=_required_text(row, "rationale"),
            )
        )
    dispositions = []
    disposition_claim_ids = set()
    for row in _mapping_rows(response, "non_scoring_dispositions"):
        if set(row) != {
            "claim_id",
            "fact_id",
            "status",
            "rationale",
            "component_ids",
        }:
            raise ValueError("claim disposition keys do not match schema")
        claim_id = _required_text(row, "claim_id")
        fact_id = _required_text(row, "fact_id")
        link = links.get(claim_id)
        if link is None or link.link_role != "PRIMARY_FACT_CLAIM":
            raise ValueError("mapper disposition cited a non-primary claim")
        if link.fact_id != fact_id or fact_id not in facts:
            raise ValueError("mapper disposition claim/fact lineage mismatch")
        if claim_id in disposition_claim_ids:
            raise ValueError("mapper returned duplicate claim dispositions")
        disposition_claim_ids.add(claim_id)
        dispositions.append(
            ClaimTerminalDisposition(
                disposition_id=stable_intelligence_id(
                    "CMAPDISP",
                    {
                        "claim_id": claim_id,
                        "fact_id": fact_id,
                        "status": row["status"],
                        "prompt_hash": prompt_hash,
                    },
                ),
                claim_id=claim_id,
                fact_id=fact_id,
                status=_required_text(row, "status"),
                rationale=_required_text(row, "rationale"),
                component_ids=_string_tuple(row.get("component_ids")),
            )
        )
    proposed_claim_ids = {row.claim_id for row in proposals}
    if proposed_claim_ids & disposition_claim_ids:
        raise ValueError("one claim cannot be both scored and non-scoring")
    expected_claim_ids = set(_primary_material_current_claim_ids(fact_compilation))
    covered = proposed_claim_ids | disposition_claim_ids
    missing = expected_claim_ids - covered
    unresolved = set(_string_tuple(response.get("unresolved_claim_ids")))
    if unresolved != missing:
        raise ValueError("mapper unresolved claims do not match uncovered primary claims")
    actual_complete = not missing
    if mapping_complete != actual_complete:
        raise ValueError("mapper complete flag contradicts claim coverage")
    return ClaimImpactMappingResult(
        status="COMPLETE" if actual_complete else "PENDING",
        impact_proposals=tuple(sorted(proposals, key=lambda row: row.impact_id)),
        explicit_dispositions=tuple(
            sorted(dispositions, key=lambda row: row.disposition_id)
        ),
        unresolved_claim_ids=tuple(sorted(missing)),
        pending_reasons=(
            ()
            if actual_complete
            else ("PRIMARY_MATERIAL_CLAIMS_REQUIRE_MAPPING",)
        ),
        provider_name=provider_name,
        prompt_hash=prompt_hash,
        mapping_complete=actual_complete,
    )


def _primary_material_current_claim_ids(
    compilation: FactCompilationResult,
) -> tuple[str, ...]:
    facts = {row.fact_id: row for row in compilation.facts}
    return tuple(
        sorted(
            row.claim_id
            for row in compilation.claim_fact_links
            if row.link_role == "PRIMARY_FACT_CLAIM"
            and row.material_claim
            and facts[row.fact_id].current_lifecycle not in {"RESOLVED", "SUPERSEDED"}
        )
    )


def _mapping_rows(
    response: Mapping[str, Any], key: str
) -> tuple[Mapping[str, Any], ...]:
    value = response.get(key)
    if not isinstance(value, (list, tuple)) or any(
        not isinstance(row, Mapping) for row in value
    ):
        raise TypeError(f"{key} must be an array of objects")
    return tuple(value)


def _string_tuple(value: Any) -> tuple[str, ...]:
    if not isinstance(value, (list, tuple)):
        raise TypeError("expected an array of strings")
    if any(not isinstance(row, str) for row in value):
        raise TypeError("expected an array of strings")
    result = tuple(row.strip() for row in value)
    if any(not row for row in result) or len(result) != len(set(result)):
        raise ValueError("string array must contain unique non-empty values")
    return result


def _required_bool(row: Mapping[str, Any], key: str) -> bool:
    value = row[key]
    if type(value) is not bool:
        raise TypeError(f"{key} must be a boolean")
    return value


def _required_text(row: Mapping[str, Any], key: str) -> str:
    value = row[key]
    if not isinstance(value, str) or not value.strip():
        raise TypeError(f"{key} must be a non-empty string")
    return value.strip()


def _pending(
    *,
    provider_name: str,
    reason: str,
    unresolved_claim_ids: Sequence[str],
    prompt_hash: str | None = None,
) -> ClaimImpactMappingResult:
    return ClaimImpactMappingResult(
        status="PENDING",
        impact_proposals=(),
        explicit_dispositions=(),
        unresolved_claim_ids=tuple(sorted(set(unresolved_claim_ids))),
        pending_reasons=(reason,),
        provider_name=provider_name,
        prompt_hash=prompt_hash,
        mapping_complete=False,
    )


def _provider_prompt_hash(
    provider: StructuredResearchProvider,
    payload: Mapping[str, Any],
) -> str:
    calls = getattr(provider, "calls", None)
    if isinstance(calls, list) and calls:
        value = calls[-1].get("prompt_hash")
        if value:
            return str(value)
    encoded = json.dumps(payload, ensure_ascii=False, sort_keys=True, default=str)
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def _payload_hash(payload: Mapping[str, Any]) -> str:
    encoded = json.dumps(payload, ensure_ascii=False, sort_keys=True, default=str)
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def _normalize_text(value: Any) -> str:
    return " ".join(str(value or "").casefold().split())


__all__ = [
    "CLAIM_IMPACT_MAPPING_OUTPUT_FILE",
    "ClaimComponentImpactMapper",
    "ClaimImpactMappingResult",
    "write_claim_impact_mapping_result",
]
