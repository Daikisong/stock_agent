"""Blind, source-backed C06 component attribution replay."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Callable, Mapping

from e2r.research_brain.compiler.evidence_impact_rubric_compiler import (
    compile_evidence_impact_rubrics,
)
from e2r.research_brain.scoring import EvidenceImpactAdjudicator
from e2r.research_brain.scoring.business_mechanism_scope import (
    infer_business_mechanism_scope,
)
from e2r.research_brain.scoring.evidence_impact_adjudicator import (
    compile_question_component_subcriteria,
)
from e2r.research_brain.scoring.question_impact_contract import (
    load_question_impact_contracts,
)
from e2r.research_brain.replay.source_backed import (
    UrllibHistoricalSourceTransport,
    extract_source_full_text,
)
from e2r.production.metadata import write_json


def run_c06_component_replay(
    *,
    config_path: str | Path,
    provider: Any,
    source_loader: Callable[[Mapping[str, Any]], Mapping[str, Any]] | None = None,
) -> Mapping[str, Any]:
    config = json.loads(Path(config_path).read_text(encoding="utf-8"))
    if config.get("schema_version") != "e2r_c06_historical_component_replay_v1":
        raise ValueError("C06 component replay config schema mismatch")
    archetype_id = str(config["archetype_id"])
    rubrics = compile_evidence_impact_rubrics(archetype_id)
    all_question_contracts = tuple(
        row
        for row in load_question_impact_contracts().values()
        if row.archetype_id == archetype_id
    )
    allowed_components = (
        "eps_fcf_explosion",
        "earnings_visibility",
        "bottleneck_pricing",
        "market_mispricing",
        "valuation_rerating",
        "capital_allocation",
        "information_confidence",
    )
    rows = []
    effective_source_loader = source_loader or _load_live_source
    strength_fractions = {
        "NONE": 0.0,
        "WEAK": 0.25,
        "MODERATE": 0.5,
        "STRONG": 0.75,
        "VERY_STRONG": 1.0,
    }
    completeness_fractions = {
        "MENTION": 0.2,
        "PARTIAL": 0.5,
        "SUBSTANTIAL": 0.8,
        "COMPLETE_FOR_PRIMITIVE": 1.0,
    }
    for case in config.get("cases") or ():
        case = dict(case)
        source = dict(effective_source_loader(case))
        source_text = str(source.get("text") or "")
        source_verified = _normalize(str(case["exact_quote"])) in _normalize(
            source_text
        )
        if not source_verified:
            rows.append(
                {
                    "case_id": case["case_id"],
                    "target_id": case["target_id"],
                    "as_of_date": case["as_of_date"],
                    "source_url": case["source_url"],
                    "source_verified": False,
                    "source_error": source.get("error"),
                    "source_content_sha256": source.get("content_sha256"),
                    "adjudication_status": "SOURCE_NOT_VERIFIED",
                    "predicted_component_ids": [],
                    "required_component_ids": sorted(case["required_component_ids"]),
                    "allowed_component_ids": sorted(case["allowed_component_ids"]),
                    "forbidden_component_ids": sorted(case["forbidden_component_ids"]),
                    "precision_numerator": 0,
                    "precision_denominator": 0,
                    "required_component_missing_count": len(
                        case["required_component_ids"]
                    ),
                    "forbidden_component_count": 0,
                    "direction_error_count": 0,
                    "hard_break_emitted": False,
                    "provider_call_count": 0,
                    "future_leakage_count": 0,
                    "proposal_rows": [],
                    "attribution_strength": 0.0,
                }
            )
            continue
        claim_id = "HCLM-" + _hash({"case_id": case["case_id"], "quote": case["exact_quote"]})[:24]
        mapping_id = "HMAP-" + _hash({"claim_id": claim_id, "primitive": case["primitive_id"]})[:24]
        claim = {
            "claim_id": claim_id,
            "target_id": case["target_id"],
            "mapping_ids": [mapping_id],
            "accepted": True,
            "primitive_id": case["primitive_id"],
            "temporal_status": "CURRENT",
            "exact_quote": case["exact_quote"],
            "raw_assertion": {
                "predicate": case["primitive_id"],
                "object_text": case["exact_quote"],
            },
        }
        question_contracts = tuple(
            row
            for row in all_question_contracts
            if case["primitive_id"] in row.allowed_primitive_ids
        )
        if not question_contracts:
            raise ValueError(
                "historical replay primitive has no question impact contract"
            )
        mechanism_scope = infer_business_mechanism_scope(
            claim,
            primitive_id=case["primitive_id"],
            archetype_id=archetype_id,
        )
        result = EvidenceImpactAdjudicator(provider).adjudicate(
            target_identity={
                "target_id": case["target_id"],
                "company_name": case["target_name"],
            },
            as_of_date=case["as_of_date"],
            archetype_id=archetype_id,
            accepted_claim=claim,
            exact_quote=case["exact_quote"],
            document_metadata={
                "source_url": case["source_url"],
                "source_verified": True,
                "source_error": source.get("error"),
                "source_content_sha256": source.get("content_sha256"),
                "source_family": case["source_family"],
                "published_date": case["as_of_date"],
                "historical_blind_replay": True,
            },
            current_claim_ledger=(),
            counter_claims=(),
            rubrics=rubrics.rubrics,
            allowed_component_ids=allowed_components,
            business_mechanism_scope=mechanism_scope,
            question_impact_contracts=question_contracts,
            claim_eligibility_decision={
                "eligibility_decision_id": (
                    "REPLAY-ELIG-" + _hash({"claim_id": claim_id})[:20]
                ),
                "claim_id": claim_id,
                "component_scoring_eligibility": True,
                "eligibility_status": "RESEARCH_REPLAY_ELIGIBLE",
            },
            component_subcriteria=compile_question_component_subcriteria(
                question_contracts,
                allowed_component_ids=allowed_components,
            ),
        )
        proposals = tuple(
            proposal
            for proposal in result.proposals
            if proposal.mapping_id == mapping_id
            and proposal.primitive_id == case["primitive_id"]
        )
        predicted = {proposal.component_id for proposal in proposals}
        allowed = set(case["allowed_component_ids"])
        required = set(case["required_component_ids"])
        forbidden = set(case["forbidden_component_ids"])
        direction_errors = sum(
            proposal.direction != case["direction"] for proposal in proposals
        )
        attribution_strength = sum(
            strength_fractions[proposal.strength_band]
            * completeness_fractions[proposal.completeness_band]
            for proposal in proposals
        )
        rows.append(
            {
                "case_id": case["case_id"],
                "target_id": case["target_id"],
                "as_of_date": case["as_of_date"],
                "source_url": case["source_url"],
                "source_verified": True,
                "source_error": source.get("error"),
                "source_content_sha256": source.get("content_sha256"),
                "exact_quote_sha256": hashlib.sha256(
                    case["exact_quote"].encode("utf-8")
                ).hexdigest(),
                "primitive_id": case["primitive_id"],
                "adjudication_status": result.status,
                "predicted_component_ids": sorted(predicted),
                "required_component_ids": sorted(required),
                "allowed_component_ids": sorted(allowed),
                "forbidden_component_ids": sorted(forbidden),
                "precision_numerator": len(predicted & allowed),
                "precision_denominator": len(predicted),
                "required_component_missing_count": len(required - predicted),
                "forbidden_component_count": len(predicted & forbidden),
                "direction_error_count": direction_errors,
                "hard_break_emitted": False,
                "provider_call_count": result.audit["provider_call_count"],
                "future_leakage_count": result.audit["critical_counts"][
                    "future_outcome_leakage_count"
                ],
                "proposal_rows": [proposal.to_dict() for proposal in proposals],
                "attribution_strength": round(attribution_strength, 6),
            }
        )
    precision_numerator = sum(row["precision_numerator"] for row in rows)
    precision_denominator = sum(row["precision_denominator"] for row in rows)
    precision = (
        precision_numerator / precision_denominator if precision_denominator else 0.0
    )
    direction_denominator = sum(len(row["proposal_rows"]) for row in rows)
    direction_errors = sum(row["direction_error_count"] for row in rows)
    direction_accuracy = (
        1.0 - direction_errors / direction_denominator
        if direction_denominator
        else 0.0
    )
    by_id = {row["case_id"]: row for row in rows}
    positive_ids = (
        "C06-SKHYNIX-20240502-SOLDOUT",
        "C06-SKHYNIX-20250123-REVENUE-MIX",
    )
    qualification = by_id["C06-SAMSUNG-20240524-QUALIFICATION-LAG"]
    positive_average_strength = sum(
        float(by_id[case_id]["attribution_strength"])
        for case_id in positive_ids
    ) / len(positive_ids)
    qualification_strength = float(qualification["attribution_strength"])
    critical = {
        "component_assignment_precision_below_95": int(precision < 0.95),
        "direction_accuracy_below_95": int(direction_accuracy < 0.95),
        "required_component_missing_count": sum(
            row["required_component_missing_count"] for row in rows
        ),
        "forbidden_component_count": sum(
            row["forbidden_component_count"] for row in rows
        ),
        "qualification_hard_4c_count": int(qualification["hard_break_emitted"]),
        "positive_not_stronger_than_qualification_count": int(
            positive_average_strength <= qualification_strength
        ),
        "future_leakage_count": sum(row["future_leakage_count"] for row in rows),
        "provider_or_adjudication_failure_count": sum(
            row["adjudication_status"] != "IMPACT_ADJUDICATION_PASS" for row in rows
        ),
        "source_verification_failure_count": sum(
            row.get("source_verified") is not True for row in rows
        ),
    }
    return {
        "schema_version": "e2r_c06_historical_component_replay_v1",
        "status": (
            "C06_HISTORICAL_COMPONENT_REPLAY_PASS"
            if sum(critical.values()) == 0
            else "C06_HISTORICAL_COMPONENT_REPLAY_FAIL"
        ),
        "case_count": len(rows),
        "component_assignment_precision": round(precision, 6),
        "direction_accuracy": round(direction_accuracy, 6),
        "critical_guard_accuracy": 1.0
        if not critical["qualification_hard_4c_count"]
        and not critical["forbidden_component_count"]
        else 0.0,
        "cases": rows,
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
    }


def _hash(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(
            value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
        ).encode("utf-8")
    ).hexdigest()


def _load_live_source(case: Mapping[str, Any]) -> Mapping[str, Any]:
    response = UrllibHistoricalSourceTransport(
        user_agent="E2R-C06-Component-Replay/1.0"
    ).fetch(url=str(case["source_url"]), timeout_seconds=30)
    if response.error or response.status_code != 200 or not response.body:
        return {
            "text": "",
            "error": response.error or f"HTTP_{response.status_code}",
            "content_sha256": (
                hashlib.sha256(response.body).hexdigest() if response.body else None
            ),
        }
    text, _ = extract_source_full_text(
        response.body, content_type=response.content_type
    )
    return {
        "text": text,
        "error": None,
        "content_sha256": hashlib.sha256(response.body).hexdigest(),
    }


def _normalize(value: str) -> str:
    return " ".join(value.casefold().replace("’", "'").split())


def write_c06_component_replay(
    result: Mapping[str, Any], *, output_path: str | Path
) -> Path:
    path = Path(output_path)
    write_json(path, result)
    return path


__all__ = ["run_c06_component_replay", "write_c06_component_replay"]
