"""Codex mapping of open-ended Pro fact language into closed scope contracts.

The mapper has no score, Stage, component-credit, or search authority.  It only
projects natural-language dossier scope fields onto enum values already owned
by the selected archetype mechanism contracts.  ``MechanismScopeValidator``
still makes the deterministic component-edge decision afterwards.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
from pathlib import Path
from typing import Any, Mapping, Protocol, Sequence

from e2r.research_brain.planning.provider_transport import (
    CodexStructuredProviderTransport,
)
from e2r.research_brain.scoring.business_mechanism_scope import (
    ArchetypeMechanismScopeContract,
)

from ..ids import canonical_json


_SCOPE_FIELDS = (
    "scope_business_segment",
    "scope_product_family",
    "scope_technology_family",
    "scope_transaction_type",
    "scope_economic_mechanism",
    "scope_confidence",
)


@dataclass(frozen=True)
class MechanismScopeMappingRun:
    mappings_by_fact_id: Mapping[str, Mapping[str, Any]]
    provider_name: str
    prompt_hash: str
    response_hash: str


class MechanismScopeMapper(Protocol):
    provider_name: str

    def map_facts(
        self,
        *,
        facts: Sequence[Mapping[str, Any]],
        contracts: Sequence[ArchetypeMechanismScopeContract],
    ) -> MechanismScopeMappingRun: ...


class CodexMechanismScopeMapper:
    provider_name = "CODEX_STRUCTURED_MECHANISM_SCOPE"

    def __init__(self, transport: CodexStructuredProviderTransport) -> None:
        self.transport = transport

    @classmethod
    def default(
        cls,
        *,
        working_directory: str | Path | None = None,
        timeout_seconds: float = 180.0,
    ) -> "CodexMechanismScopeMapper":
        return cls(
            CodexStructuredProviderTransport(
                working_directory=working_directory or Path.cwd(),
                timeout_seconds=timeout_seconds,
            )
        )

    def map_facts(
        self,
        *,
        facts: Sequence[Mapping[str, Any]],
        contracts: Sequence[ArchetypeMechanismScopeContract],
    ) -> MechanismScopeMappingRun:
        if not facts or not contracts:
            raise ValueError("mechanism scope mapping requires facts and contracts")
        fact_ids = tuple(str(row.get("dossier_fact_id") or "").strip() for row in facts)
        if any(not value for value in fact_ids) or len(set(fact_ids)) != len(fact_ids):
            raise ValueError("mechanism scope mapping requires unique dossier fact ids")
        schema, enum_context = _scope_schema(contracts=contracts, fact_count=len(facts))
        payload = {
            "schema_version": "e2r_pro_mechanism_scope_mapping_input_v1",
            "facts": [
                {
                    "dossier_fact_id": str(row.get("dossier_fact_id") or ""),
                    "statement": str(row.get("statement") or ""),
                    "subject": str(row.get("subject") or ""),
                    "business_segment": str(row.get("business_segment") or ""),
                    "product_family": str(row.get("product_family") or ""),
                    "economic_mechanism": str(row.get("economic_mechanism") or ""),
                    "predicate": str(row.get("predicate") or ""),
                    "candidate_components": list(row.get("candidate_components") or ()),
                    "direction": str(row.get("direction") or ""),
                }
                for row in facts
            ],
            "allowed_scope_enums": enum_context,
            "component_credit_authority": False,
            "score_authority": False,
            "stage_authority": False,
        }
        prompt = "\n".join(
            (
                "You map open-ended E2R Pro fact language into an existing closed business-mechanism scope contract.",
                "Return exactly one mapping for every supplied dossier_fact_id and no others, preserving the input order.",
                "Choose only enum values supplied in allowed_scope_enums. Mixed valid products such as DRAM and NAND should use the broad valid memory enum when available; do not classify the whole fact as a forbidden product merely because one product is named.",
                "This is semantic normalization only. Do not decide component credit, evidence acceptance, score, Stage, investment action, or new research.",
                "Return exactly one JSON object matching the schema.",
                canonical_json(payload),
            )
        )
        response = self.transport.complete(
            prompt=prompt,
            output_schema=schema,
            schema_name="e2r_pro_mechanism_scope_mapping",
        )
        mappings = _decode_scope_mappings(
            response.payload,
            expected_fact_ids=fact_ids,
            enum_context=enum_context,
        )
        return MechanismScopeMappingRun(
            mappings_by_fact_id=mappings,
            provider_name=self.provider_name,
            prompt_hash=hashlib.sha256(prompt.encode("utf-8")).hexdigest(),
            response_hash=hashlib.sha256(
                response.raw_response.encode("utf-8")
            ).hexdigest(),
        )


def _scope_schema(
    *,
    contracts: Sequence[ArchetypeMechanismScopeContract],
    fact_count: int,
) -> tuple[Mapping[str, Any], Mapping[str, tuple[str, ...]]]:
    enum_context = {
        "scope_business_segment": _union(
            *(row.allowed_business_segments for row in contracts),
            *(row.forbidden_business_segments for row in contracts),
            ("CORPORATE_GENERIC",),
        ),
        "scope_product_family": _union(
            *(row.allowed_product_families for row in contracts),
            *(row.forbidden_product_families for row in contracts),
            ("CORPORATE_GENERIC",),
        ),
        "scope_technology_family": _union(
            *(row.allowed_technology_families for row in contracts),
            ("FOUNDRY", "CORPORATE_GENERIC"),
        ),
        "scope_transaction_type": _union(
            *(row.allowed_transaction_types for row in contracts),
            ("GENERIC_INFORMATION",),
        ),
        "scope_economic_mechanism": _union(
            *(row.allowed_economic_mechanisms for row in contracts),
            ("INFORMATION_ONLY",),
        ),
    }
    item_properties: dict[str, Any] = {
        "dossier_fact_id": {"type": "string"},
        **{
            field: {"enum": list(values)}
            for field, values in enum_context.items()
        },
        "scope_confidence": {"type": "number", "minimum": 0, "maximum": 1},
    }
    item_required = ["dossier_fact_id", *_SCOPE_FIELDS]
    return (
        {
            "type": "object",
            "additionalProperties": False,
            "required": ["scope_mappings"],
            "properties": {
                "scope_mappings": {
                    "type": "array",
                    "minItems": fact_count,
                    "maxItems": fact_count,
                    "items": {
                        "type": "object",
                        "additionalProperties": False,
                        "required": item_required,
                        "properties": item_properties,
                    },
                }
            },
        },
        enum_context,
    )


def _decode_scope_mappings(
    raw: Mapping[str, Any],
    *,
    expected_fact_ids: Sequence[str],
    enum_context: Mapping[str, Sequence[str]],
) -> Mapping[str, Mapping[str, Any]]:
    if set(raw) != {"scope_mappings"} or not isinstance(raw.get("scope_mappings"), list):
        raise ValueError("mechanism scope provider returned an invalid root object")
    rows = raw["scope_mappings"]
    actual_ids = tuple(str(row.get("dossier_fact_id") or "") for row in rows if isinstance(row, Mapping))
    if actual_ids != tuple(expected_fact_ids) or len(rows) != len(expected_fact_ids):
        raise ValueError("mechanism scope provider changed the exact fact roster or order")
    expected_keys = {"dossier_fact_id", *_SCOPE_FIELDS}
    decoded: dict[str, Mapping[str, Any]] = {}
    for row in rows:
        if not isinstance(row, Mapping) or set(row) != expected_keys:
            raise ValueError("mechanism scope provider returned invalid mapping keys")
        for field, allowed in enum_context.items():
            if str(row.get(field) or "") not in set(allowed):
                raise ValueError("mechanism scope provider escaped a contract enum")
        confidence = row.get("scope_confidence")
        if isinstance(confidence, bool) or not isinstance(confidence, (int, float)):
            raise ValueError("mechanism scope confidence must be numeric")
        if not 0 <= float(confidence) <= 1:
            raise ValueError("mechanism scope confidence is outside [0, 1]")
        fact_id = str(row["dossier_fact_id"])
        decoded[fact_id] = {
            field: (float(row[field]) if field == "scope_confidence" else str(row[field]))
            for field in _SCOPE_FIELDS
        }
    return decoded


def _union(*values: Sequence[str]) -> tuple[str, ...]:
    return tuple(sorted({str(item).strip() for rows in values for item in rows if str(item).strip()}))


__all__ = [
    "CodexMechanismScopeMapper",
    "MechanismScopeMapper",
    "MechanismScopeMappingRun",
]
