"""Compile leaf-backed mandatory-target full-thesis acceptance reports."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.metadata import write_json, write_text
from e2r.research_brain.scoring.component_assessment import (
    TERMINAL_FULL_SCORE_STATUSES,
)


TARGET_ACCEPTANCE_SCHEMA_VERSION = "e2r_canonical_target_acceptance_v1"
_REQUIRED_LEAVES = (
    "source_timeline.jsonl",
    "accepted_current_claims.jsonl",
    "claim_provenance.jsonl",
    "claim_impacts_validated.jsonl",
    "component_assessments.jsonl",
    "component_score_vector.json",
    "score_interval.json",
    "atomic_stage_decision.json",
    "stagecourt_trace.json",
    "question_closure.jsonl",
)


def compile_target_full_thesis_acceptance(
    *,
    target_id: str,
    company_name: str,
    success_label: str,
    dossier_root: str | Path,
    source_research_roots: Sequence[str | Path],
    output_path: str | Path,
) -> Mapping[str, Any]:
    root = Path(dossier_root)
    missing = tuple(name for name in _REQUIRED_LEAVES if not (root / name).is_file())
    if missing:
        raise ValueError(f"mandatory dossier leaves are missing: {missing}")
    timeline = _read_jsonl(root / "source_timeline.jsonl")
    documents = _read_jsonl(root / "evidence_documents.jsonl")
    claims = _read_jsonl(root / "accepted_current_claims.jsonl")
    provenance = _read_jsonl(root / "claim_provenance.jsonl")
    impacts = _read_jsonl(root / "claim_impacts_validated.jsonl")
    assessments = _read_jsonl(root / "component_assessments.jsonl")
    score = _read_json(root / "component_score_vector.json")
    interval = _read_json(root / "score_interval.json")
    decision = _read_json(root / "atomic_stage_decision.json")
    trace = _read_json(root / "stagecourt_trace.json")
    closures = _read_jsonl(root / "question_closure.jsonl")
    source_roots = tuple(Path(value) for value in source_research_roots)
    research_requests = tuple(
        row
        for source_root in source_roots
        for row in _read_jsonl(source_root / "provider_requests.jsonl")
    )
    research_web = tuple(
        row
        for source_root in source_roots
        for row in _read_jsonl(source_root / "web_search_tasks.jsonl")
    )
    research_documents = tuple(
        row
        for source_root in source_roots
        for row in _read_jsonl(source_root / "evidence_documents.jsonl")
    )
    claim_ids = {str(row.get("claim_id") or "") for row in claims}
    impact_ids = {str(row.get("impact_id") or "") for row in impacts}
    assessment_ids = {str(row.get("assessment_id") or "") for row in assessments}
    mapping_counts: dict[str, int] = {}
    for row in impacts:
        claim_id = str(row.get("claim_id") or "")
        mapping_counts[claim_id] = mapping_counts.get(claim_id, 0) + 1
    closure_by_id = {
        str(row.get("question_family_id") or ""): row for row in closures
    }
    source_classes = {str(row.get("source_class") or "") for row in documents}
    independent_full = any(
        str(row.get("source_class") or "")
        in {"TrustedNews", "GeneralWeb", "CustomerOfficial", "IndustryData"}
        for row in research_documents
    )
    web_investigated = any(
        row.get("search_call_executed") is True
        and row.get("official_first_attempted") is True
        for row in research_web
    )
    companyguide_investigated = any(
        str(row.get("source_class") or "") == "CompanyGuide"
        for row in research_requests
    )
    source_family_coverage = {
        "issuer_official": {
            "status": "SOURCE_BACKED" if "IssuerIR" in source_classes else "MISSING",
            "document_count": sum(
                str(row.get("source_class") or "") == "IssuerIR" for row in documents
            ),
        },
        "official_filing": {
            "status": "SOURCE_BACKED" if "DART" in source_classes else "MISSING",
            "document_count": sum(
                str(row.get("source_class") or "") in {"DART", "KIND"}
                for row in documents
            ),
        },
        "independent_or_customer_industry": {
            "status": (
                "SOURCE_BACKED"
                if independent_full
                else "INVESTIGATED_NO_ACCEPTED_FULL_DOCUMENT"
                if web_investigated
                else "MISSING"
            ),
            "web_task_count": len(research_web),
        },
        "financial_revision": {
            "status": (
                "INVESTIGATED"
                if companyguide_investigated
                and closure_by_id.get("medium_term_revision_consensus")
                else "MISSING"
            ),
            "provider_request_count": sum(
                str(row.get("source_class") or "") == "CompanyGuide"
                for row in research_requests
            ),
        },
    }
    red_team = {
        "qualification_execution": _closure_state(
            closure_by_id, "qualification_pass_lag_reopen"
        ),
        "customer_concentration": _closure_state(
            closure_by_id, "customer_concentration_dependency"
        ),
        "conventional_memory_drag": _closure_state(
            closure_by_id, "conventional_memory_drag"
        ),
        "capacity_expansion_oversupply": _closure_state(
            closure_by_id, "capex_supply_oversupply"
        ),
    }
    nonterminal_components = tuple(
        row.get("component_id")
        for row in assessments
        if row.get("status") not in TERMINAL_FULL_SCORE_STATUSES
    )
    nonterminal_questions = tuple(
        row.get("question_family_id")
        for row in closures
        if row.get("status")
        in {"PROVIDER_PENDING", "SOURCE_PENDING", "BUDGET_PENDING"}
    )
    critical = {
        "organic_claim_missing_count": int(not claims),
        "validated_impact_missing_count": int(not impacts),
        "probe_contamination_count": sum(
            row.get("evidence_origin") != "ORGANIC_LIVE" for row in claims
        ),
        "source_proxy_claim_count": sum(
            row.get("source_proxy_only") is not False for row in claims
        ),
        "target_contamination_count": sum(
            str(row.get("target_id") or row.get("target_entity_id") or "")
            != target_id
            for row in claims
        ),
        "future_source_count": sum(
            row.get("as_of_valid") is not True for row in timeline
        ),
        "provenance_hash_or_quote_mismatch_count": _provenance_mismatch_count(
            provenance
        ),
        "source_family_gap_count": sum(
            row["status"] == "MISSING" for row in source_family_coverage.values()
        ),
        "red_team_gap_count": sum(
            row["status"]
            in {"MISSING", "PROVIDER_PENDING", "SOURCE_PENDING", "BUDGET_PENDING"}
            for row in red_team.values()
        ),
        "nonterminal_component_count": len(nonterminal_components),
        "nonterminal_question_count": len(nonterminal_questions),
        "full_score_invalid_count": int(score.get("full_score_valid") is not True),
        "score_type_mismatch_count": int(score.get("score_type") != "FULL_E2R_100"),
        "score_sum_mismatch_count": int(
            abs(
                sum(float(value) for value in (score.get("component_score_vector") or {}).values())
                - float(score.get("full_e2r_score") or 0.0)
            )
            > 1e-6
        ),
        "decision_claim_lineage_mismatch_count": len(
            claim_ids ^ set(str(value) for value in decision.get("accepted_claim_ids") or ())
        ),
        "decision_impact_lineage_mismatch_count": len(
            impact_ids ^ set(str(value) for value in decision.get("claim_impact_ids") or ())
        ),
        "decision_component_lineage_mismatch_count": len(
            assessment_ids
            ^ set(str(value) for value in decision.get("component_assessment_ids") or ())
        ),
        "stage_trace_mismatch_count": int(
            trace.get("trace_id") != decision.get("trace_id")
            or trace.get("decision_id") != decision.get("decision_id")
        ),
    }
    audit = {
        "schema_version": TARGET_ACCEPTANCE_SCHEMA_VERSION,
        "status": success_label if sum(critical.values()) == 0 else "CANONICAL_FULL_THESIS_NOT_READY",
        "target_id": target_id,
        "company_name": company_name,
        "conversion_funnel": {
            "fetched_documents": len(documents),
            "raw_assertions": len(_read_jsonl(root / "raw_assertions.jsonl")),
            "accepted_current_claims": len(claims),
            "validated_impacts": len(impacts),
            "supported_components": sum(bool(row.get("support_impact_ids")) for row in assessments),
            "evaluated_absent_components": sum(row.get("status") == "VERIFIED_ABSENT_AFTER_SEARCH" for row in assessments),
            "verified_supported_score": score.get("verified_supported_score"),
            "full_score_valid": score.get("full_score_valid"),
            "canonical_stage": decision.get("canonical_stage"),
        },
        "many_to_many_claim_count": sum(value > 1 for value in mapping_counts.values()),
        "source_family_coverage": source_family_coverage,
        "red_team": red_team,
        "score": score,
        "score_interval": interval,
        "decision": decision,
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
        "blockers": [name for name, value in critical.items() if value],
        "investment_recommendation_emitted": False,
    }
    write_json(root / "audit_summary.json", audit)
    write_text(Path(output_path), _markdown(audit))
    return audit


def _closure_state(
    rows: Mapping[str, Mapping[str, Any]], family_id: str
) -> Mapping[str, Any]:
    row = dict(rows.get(family_id) or {})
    return {
        "status": str(row.get("status") or "MISSING"),
        "supporting_claim_ids": list(row.get("supporting_claim_ids") or ()),
        "counter_claim_ids": list(row.get("counter_claim_ids") or ()),
        "search_exhaustion_proof": list(row.get("search_exhaustion_proof") or ()),
    }


def _provenance_mismatch_count(rows: Sequence[Mapping[str, Any]]) -> int:
    mismatch = 0
    for row in rows:
        text = str(row.get("document_text") or "")
        mismatch += hashlib.sha256(text.encode()).hexdigest() != str(
            row.get("content_sha256") or ""
        ) or str(row.get("exact_quote") or "") not in text
    return mismatch


def _markdown(audit: Mapping[str, Any]) -> str:
    funnel = audit["conversion_funnel"]
    lines = [
        f"# {audit['company_name']} C06 Full-Thesis Acceptance",
        "",
        f"- status: {audit['status']}",
        f"- target: {audit['target_id']}",
        f"- source documents: {funnel['fetched_documents']}",
        f"- organic claims: {funnel['accepted_current_claims']}",
        f"- validated impacts: {funnel['validated_impacts']}",
        f"- terminal components: {funnel['supported_components'] + funnel['evaluated_absent_components']}/7",
        f"- FULL_E2R_100: {funnel['verified_supported_score']}",
        f"- deterministic Stage: {funnel['canonical_stage']}",
        f"- many-to-many claims: {audit['many_to_many_claim_count']}",
        f"- critical_count_sum: {audit['critical_count_sum']}",
        "- investment recommendation emitted: false",
        "",
        "## Source family coverage",
        "",
    ]
    lines.extend(
        f"- {name}: {row['status']}"
        for name, row in audit["source_family_coverage"].items()
    )
    lines.extend(("", "## Red-team", ""))
    lines.extend(f"- {name}: {row['status']}" for name, row in audit["red_team"].items())
    lines.extend(("", "## Blockers", "", f"- {audit['blockers']}", ""))
    return "\n".join(lines)


def _read_json(path: Path) -> Mapping[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _read_jsonl(path: Path) -> tuple[Mapping[str, Any], ...]:
    if not path.is_file():
        return ()
    with path.open(encoding="utf-8") as handle:
        return tuple(json.loads(line) for line in handle if line.strip())


__all__ = ["TARGET_ACCEPTANCE_SCHEMA_VERSION", "compile_target_full_thesis_acceptance"]
