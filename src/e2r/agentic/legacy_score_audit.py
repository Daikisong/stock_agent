"""Audit helpers for legacy parser fields that still feed score/risk paths."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, Sequence


V2_SCORE_ELIGIBLE_CLAIMS_KEY = "evidence_os_v2_score_eligible_claim_ids_by_primitive"
V2_HARD_BREAK_SOURCE_QUORUM_KEY = "evidence_os_v2_hard_break_source_quorum_by_primitive"

LEGACY_DIRECT_RISK_FIELDS = frozenset(
    {
        "accounting_or_trust_issue",
        "accounting_trust_risk",
        "auditor_or_disclosure_risk",
        "restatement_risk",
        "contract_cancelled_or_delayed",
        "customer_capex_decline",
        "qualification_lag_risk",
        "call_off_risk",
        "source_quality_conflict",
        "evidence_source_quality_issue",
        "receivables_inventory_spike",
        "cash_runway_risk",
        "regulatory_risk",
        "safety_signal",
        "ev_demand_slowdown",
    }
)

LEGACY_PARSER_SCORE_SOURCE_PREFIXES = (
    "disclosure:",
    "legacy-parser:",
    "news:",
    "parser-output:",
    "research:",
)

STRUCTURED_CONNECTOR_SCORE_SOURCE_PREFIXES = (
    "actual:",
    "consensus:",
    "revision:",
)

_LEGACY_SCORE_PRIMITIVE_KEYWORDS = frozenset(
    {
        "actual",
        "allocation",
        "approval",
        "arpu",
        "arr",
        "asp",
        "backlog",
        "balance_sheet",
        "booked",
        "bottleneck",
        "buyback",
        "call_off",
        "cancellation",
        "capacity",
        "capa",
        "capex",
        "capital",
        "cash",
        "cashflow",
        "cash_flow",
        "channel",
        "constraint",
        "contract",
        "csm",
        "customer",
        "delivery",
        "demand",
        "dividend",
        "earnings",
        "eps",
        "estimate",
        "export",
        "fcf",
        "financial",
        "hbm",
        "implementation",
        "insurance",
        "inventory",
        "lead_time",
        "margin",
        "mispricing",
        "multiple",
        "net_income",
        "occupancy",
        "op_",
        "operating_leverage",
        "operating_profit",
        "opm",
        "order",
        "payout",
        "pbr",
        "per",
        "platform",
        "policy",
        "preorder",
        "pre_sold",
        "pricing",
        "profit",
        "project",
        "recurring",
        "regulatory",
        "reimbursement",
        "retention",
        "revenue",
        "revision",
        "risk",
        "roe",
        "royalty",
        "rpo",
        "sales",
        "shareholder",
        "shipment",
        "shortage",
        "software",
        "spread",
        "structural",
        "subsidy",
        "supply",
        "target",
        "tightness",
        "trial",
        "upside",
        "valuation",
        "visibility",
        "volume",
    }
)


@dataclass(frozen=True)
class LegacyDirectFieldFinding:
    mapping_index: int
    field_name: str
    reason: str
    value: Any


def audit_legacy_direct_score_fields(
    mappings: Sequence[Mapping[str, Any]],
    *,
    watched_fields: set[str] | frozenset[str] = LEGACY_DIRECT_RISK_FIELDS,
) -> tuple[LegacyDirectFieldFinding, ...]:
    """Return legacy risk fields that lack v2 score-eligible claim backing.

    Legacy v1 claim metadata is not sufficient here.  The v2 goal requires
    target/temporal adjudication, source anchor validation, and primitive
    mapping before a parser field can affect score or hard-break logic.
    """

    findings: list[LegacyDirectFieldFinding] = []
    for index, mapping in enumerate(mappings):
        v2_claims = _v2_claims_by_primitive(mapping)
        for field_name in sorted(watched_fields):
            value = mapping.get(field_name)
            if value in (None, "", False, 0):
                continue
            if _has_v2_claim(v2_claims, field_name):
                continue
            findings.append(
                LegacyDirectFieldFinding(
                    mapping_index=index,
                    field_name=field_name,
                    reason="legacy_direct_score_field_without_v2_claim",
                    value=value,
                )
            )
    return tuple(findings)


def audit_legacy_parser_score_claim_fields(
    mappings: Sequence[Mapping[str, Any]],
) -> tuple[LegacyDirectFieldFinding, ...]:
    """Return v1 parser claim fields that would look score-backed without v2.

    The old claim compiler can attach ``compiled_claim_ids_by_primitive`` to
    parser output.  That is useful for diagnostics, but it is not a v2
    score-admissible claim because it skipped the Evidence OS target,
    temporal, lifecycle, mapping, and source-quorum gates.

    Structured connector rows such as actuals/consensus/revisions are excluded
    here; they are not keyword parser fields.  Document parser sources like
    research/news/disclosure must pass through v2 before they can be used as
    production score support.
    """

    findings: list[LegacyDirectFieldFinding] = []
    for index, mapping in enumerate(mappings):
        v2_claims = _v2_claims_by_primitive(mapping)
        for primitive_id in _legacy_parser_primitive_ids(mapping):
            if not _legacy_parser_score_relevant_primitive(primitive_id):
                continue
            if _has_v2_claim(v2_claims, primitive_id):
                continue
            findings.append(
                LegacyDirectFieldFinding(
                    mapping_index=index,
                    field_name=primitive_id,
                    reason="legacy_parser_score_claim_without_v2_eligibility",
                    value=True,
                )
            )
    return tuple(findings)


def _v2_claims_by_primitive(mapping: Mapping[str, Any]) -> Mapping[str, tuple[str, ...]]:
    raw = mapping.get(V2_SCORE_ELIGIBLE_CLAIMS_KEY)
    if not isinstance(raw, Mapping):
        return {}
    result: dict[str, tuple[str, ...]] = {}
    for primitive, claim_ids in raw.items():
        primitive_id = str(primitive).strip()
        if not primitive_id:
            continue
        values = claim_ids if isinstance(claim_ids, (list, tuple)) else (claim_ids,)
        clean = tuple(str(item).strip() for item in values if str(item).strip())
        if clean:
            result[primitive_id] = clean
    return result


def _has_v2_claim(v2_claims: Mapping[str, tuple[str, ...]], field_name: str) -> bool:
    return bool(v2_claims.get(field_name))


def _legacy_parser_primitive_ids(mapping: Mapping[str, Any]) -> tuple[str, ...]:
    raw = mapping.get("compiled_claims")
    if isinstance(raw, Sequence) and not isinstance(raw, (str, bytes, bytearray)):
        primitive_ids: list[str] = []
        for row in raw:
            if not isinstance(row, Mapping):
                continue
            evidence_id = str(row.get("evidence_id") or "").strip()
            if not _legacy_parser_source(evidence_id):
                continue
            primitive_id = str(row.get("primitive_id") or "").strip()
            if primitive_id:
                primitive_ids.append(primitive_id)
        return tuple(dict.fromkeys(primitive_ids))

    raw_by_primitive = mapping.get("compiled_claim_ids_by_primitive")
    if not isinstance(raw_by_primitive, Mapping):
        return ()
    evidence_id = str(mapping.get("evidence_id") or "").strip()
    if evidence_id and not _legacy_parser_source(evidence_id):
        return ()
    return tuple(str(primitive).strip() for primitive in raw_by_primitive if str(primitive).strip())


def _legacy_parser_source(evidence_id: str) -> bool:
    if not evidence_id:
        return False
    if evidence_id.startswith(STRUCTURED_CONNECTOR_SCORE_SOURCE_PREFIXES):
        return False
    return evidence_id.startswith(LEGACY_PARSER_SCORE_SOURCE_PREFIXES)


def _legacy_parser_score_relevant_primitive(primitive_id: str) -> bool:
    normalized = primitive_id.strip().casefold()
    if not normalized:
        return False
    if normalized in LEGACY_DIRECT_RISK_FIELDS:
        return True
    return any(keyword in normalized for keyword in _LEGACY_SCORE_PRIMITIVE_KEYWORDS)


__all__ = [
    "LEGACY_DIRECT_RISK_FIELDS",
    "LEGACY_PARSER_SCORE_SOURCE_PREFIXES",
    "LegacyDirectFieldFinding",
    "STRUCTURED_CONNECTOR_SCORE_SOURCE_PREFIXES",
    "V2_HARD_BREAK_SOURCE_QUORUM_KEY",
    "V2_SCORE_ELIGIBLE_CLAIMS_KEY",
    "audit_legacy_direct_score_fields",
    "audit_legacy_parser_score_claim_fields",
]
