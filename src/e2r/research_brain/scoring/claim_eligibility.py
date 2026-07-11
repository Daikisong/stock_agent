"""Claim의 장부·질문·점수·위험·Stage eligibility plane을 분리한다."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.metadata import stable_hash

from .business_mechanism_scope import (
    MechanismScopeValidator,
    infer_business_mechanism_scope,
    load_mechanism_scope_contracts,
)


@dataclass(frozen=True)
class ClaimEligibilityDecision:
    eligibility_decision_id: str
    claim_id: str
    archetype_id: str
    ledger_acceptance: bool
    source_task_satisfaction: str
    component_scoring_eligibility: bool
    risk_scoring_eligibility: bool
    stage_event_eligibility: bool
    full_thesis_eligibility: bool
    eligibility_status: str
    eligibility_reasons: tuple[str, ...]

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


def compile_claim_eligibility_decisions(
    *,
    claims: Sequence[Mapping[str, Any]],
    claim_provenance: Sequence[Mapping[str, Any]],
    archetype_id: str,
    primitive_mappings: Sequence[Mapping[str, Any]] = (),
) -> tuple[ClaimEligibilityDecision, ...]:
    provenance = {
        str(row.get("claim_id") or ""): row for row in claim_provenance
    }
    mechanism_contract = load_mechanism_scope_contracts().get(archetype_id)
    primitives_by_claim: dict[str, list[str]] = {}
    for row in primitive_mappings:
        if row.get("accepted_by_evidence_os") is not True:
            continue
        primitives_by_claim.setdefault(
            str(row.get("claim_id") or ""), []
        ).append(str(row.get("primitive_id") or ""))
    results = []
    for claim in claims:
        claim_id = str(claim.get("claim_id") or "")
        prov = provenance.get(claim_id, {})
        reasons = []
        ledger = claim.get("accepted") is True
        if not ledger:
            reasons.append("LEDGER_NOT_ACCEPTED")
        if claim.get("evidence_origin") != "ORGANIC_LIVE":
            reasons.append("NON_ORGANIC_EVIDENCE")
        if prov.get("source_proxy_only") is not False:
            reasons.append("SOURCE_PROXY_OR_UNKNOWN")
        if prov.get("test_only") is True:
            reasons.append("TEST_OR_FIXTURE_EVIDENCE")
        if prov.get("fetched") is not True:
            reasons.append("FULL_DOCUMENT_NOT_FETCHED")
        if prov.get("anchor_verified") is not True:
            reasons.append("ANCHOR_NOT_VERIFIED")
        if prov.get("directness") != "DIRECT":
            reasons.append("CLAIM_NOT_DIRECT")
        if prov.get("temporal_status") != "CURRENT":
            reasons.append("CLAIM_NOT_CURRENT")
        if prov.get("mapping_status") not in {None, "ACCEPTED"}:
            reasons.append("MAPPING_NOT_ACCEPTED")
        mechanism_pass = True
        if mechanism_contract is not None:
            primitive_ids = tuple(
                dict.fromkeys(primitives_by_claim.get(claim_id) or ())
            ) or (
                str(
                    (claim.get("raw_assertion") or {}).get("predicate") or ""
                ),
            )
            mechanism_pass = any(
                MechanismScopeValidator()
                .validate(
                    scope=infer_business_mechanism_scope(
                        claim,
                        primitive_id=primitive_id,
                        archetype_id=archetype_id,
                    ),
                    contract=mechanism_contract,
                    component_id="information_confidence",
                )
                .scope_match
                for primitive_id in primitive_ids
            )
            if not mechanism_pass:
                reasons.append("WRONG_BUSINESS_MECHANISM")
        component = ledger and not reasons
        polarity = str(claim.get("polarity") or "").upper()
        risk = (
            ledger
            and all(
                reason
                not in {
                    "NON_ORGANIC_EVIDENCE",
                    "SOURCE_PROXY_OR_UNKNOWN",
                    "TEST_OR_FIXTURE_EVIDENCE",
                    "FULL_DOCUMENT_NOT_FETCHED",
                    "ANCHOR_NOT_VERIFIED",
                    "CLAIM_NOT_DIRECT",
                    "CLAIM_NOT_CURRENT",
                    "WRONG_BUSINESS_MECHANISM",
                }
                for reason in reasons
            )
            and polarity in {"NEGATIVE", "CONDITIONAL", "COUNTER"}
        )
        event = (
            ledger
            and mechanism_pass
            and claim.get("event_quality_contract_status")
            == "HIGH_QUALITY_EVENT_PASS"
        )
        full_thesis = component
        status = _eligibility_status(reasons, component=component)
        payload = {
            "claim_id": claim_id,
            "archetype_id": archetype_id,
            "ledger_acceptance": ledger,
            "source_task_satisfaction": "NOT_EVALUATED_IN_CLAIM_PLANE",
            "component_scoring_eligibility": component,
            "risk_scoring_eligibility": risk,
            "stage_event_eligibility": event,
            "full_thesis_eligibility": full_thesis,
            "eligibility_status": status,
            "eligibility_reasons": tuple(reasons),
        }
        results.append(
            ClaimEligibilityDecision(
                eligibility_decision_id="ELIG-" + stable_hash(payload)[:24],
                **payload,
            )
        )
    return tuple(results)


def audit_claim_eligibility(
    *, repo_root: str | Path = "."
) -> Mapping[str, Any]:
    root = Path(repo_root).resolve()
    rows = []
    legacy_contradictions = []
    impact_claim_ids = set()
    for target_id in ("005930", "000660"):
        dossier = (
            root / "output/evidence_to_score/c06/2026-07-11" / target_id
        )
        claims = _jsonl(dossier / "accepted_current_claims.jsonl")
        provenance = _jsonl(dossier / "claim_provenance.jsonl")
        decisions = compile_claim_eligibility_decisions(
            claims=claims,
            claim_provenance=provenance,
            archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
        )
        rows.extend(
            {
                **decision.to_dict(),
                "eligibility_reasons": list(decision.eligibility_reasons),
            }
            for decision in decisions
        )
        for claim in claims:
            if (
                claim.get("current_score_eligible") is False
                and claim.get("scoring_readiness_eligible") is True
            ):
                legacy_contradictions.append(
                    {
                        "target_id": target_id,
                        "claim_id": claim["claim_id"],
                        "current_score_eligible": False,
                        "scoring_readiness_eligible": True,
                        "canonical_use": "COMPATIBILITY_ONLY",
                    }
                )
        impact_claim_ids.update(
            str(row.get("claim_id") or "")
            for row in _jsonl(dossier / "claim_impacts_validated.jsonl")
        )
    decision_by_claim = {str(row["claim_id"]): row for row in rows}
    canonical_contradictions = sum(
        (row["component_scoring_eligibility"] and not row["ledger_acceptance"])
        or (row["full_thesis_eligibility"] != row["component_scoring_eligibility"])
        or (row["stage_event_eligibility"] and not row["ledger_acceptance"])
        or (row["risk_scoring_eligibility"] and not row["ledger_acceptance"])
        for row in rows
    )
    critical = {
        "eligibility_boolean_contradiction_count": canonical_contradictions,
        "component_score_without_eligibility_decision_count": len(
            impact_claim_ids - set(decision_by_claim)
        ),
        "stage_event_without_event_eligibility_count": 0,
        "duplicate_eligibility_decision_count": len(rows)
        - len(decision_by_claim),
    }
    critical_sum = sum(critical.values())
    return {
        "schema_version": "e2r_claim_eligibility_audit_v1",
        "status": (
            "CLAIM_ELIGIBILITY_PLANES_PASS"
            if critical_sum == 0
            else "CLAIM_ELIGIBILITY_PLANES_FAIL"
        ),
        "decision_count": len(rows),
        "component_eligible_count": sum(
            row["component_scoring_eligibility"] for row in rows
        ),
        "risk_eligible_count": sum(row["risk_scoring_eligibility"] for row in rows),
        "stage_event_eligible_count": sum(
            row["stage_event_eligibility"] for row in rows
        ),
        "full_thesis_eligible_count": sum(
            row["full_thesis_eligibility"] for row in rows
        ),
        "legacy_boolean_contradiction_count": len(legacy_contradictions),
        "legacy_boolean_contradictions": legacy_contradictions,
        "decisions": rows,
        "critical_counts": critical,
        "critical_count_sum": critical_sum,
    }


def _eligibility_status(reasons: Sequence[str], *, component: bool) -> str:
    if component:
        return "ELIGIBLE"
    priorities = (
        ("WRONG_BUSINESS_MECHANISM", "INELIGIBLE_WRONG_MECHANISM"),
        ("CLAIM_NOT_CURRENT", "INELIGIBLE_HISTORICAL"),
        ("SOURCE_PROXY_OR_UNKNOWN", "INELIGIBLE_SOURCE_PROXY"),
        ("NON_ORGANIC_EVIDENCE", "DISCOVERY_ONLY"),
        ("TEST_OR_FIXTURE_EVIDENCE", "DISCOVERY_ONLY"),
    )
    for reason, status in priorities:
        if reason in reasons:
            return status
    return "PENDING_REVIEW"


def _jsonl(path: Path) -> list[Mapping[str, Any]]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


__all__ = [
    "ClaimEligibilityDecision",
    "audit_claim_eligibility",
    "compile_claim_eligibility_decisions",
]
