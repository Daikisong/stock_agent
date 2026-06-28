"""Leakage and hardcoding audits for Research Brain."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Mapping, Sequence

from e2r.research_brain.schemas import ResearchBrainPlan, ResearchMemoryRecord


_FORBIDDEN_PROMPT_TOKENS = ("mfe", "mae", "future_outcome", "outcome_label", "post_peak_drawdown")
_HARDCODE_PATTERNS = {
    "symbol_exception": re.compile(r"^\s*if\s+.*symbol\s*==", re.MULTILINE),
    "company_exception": re.compile(r"^\s*if\s+.*company_name\s*==", re.MULTILINE),
    "archetype_fixed_query": re.compile(r"^\s*if\s+.*archetype.*==.*C\d{2}.*:\s*\n\s*query\s*=", re.MULTILINE),
    "missing_primitive_fixed_query": re.compile(
        r"^\s*if\s+.*missing_primitive.*==.*:\s*\n\s*query\s*=",
        re.MULTILINE,
    ),
    "audit_keyword_score": re.compile(r"^\s*if\s+.*(?:감사의견|accounting).*(?:score|risk)", re.MULTILINE),
    "source_proxy_auto_promotion": re.compile(
        r"^\s*if\s+.*source_proxy_only.*:\s*\n\s*.*(?:production_ready_evidence|fixture_usable|runtime_score_eligible)\s*=\s*True",
        re.IGNORECASE | re.MULTILINE,
    ),
}


def audit_memory_leakage(
    *,
    records: Sequence[ResearchMemoryRecord],
    planner_prompts: Sequence[str] = (),
    extraction_prompts: Sequence[str] = (),
    plans: Sequence[ResearchBrainPlan] = (),
) -> Mapping[str, object]:
    extraction_text = "\n".join(extraction_prompts).lower()
    planner_text = "\n".join(planner_prompts).lower()
    forbidden_future_in_extraction = sum(extraction_text.count(token) for token in _FORBIDDEN_PROMPT_TOKENS)
    forbidden_future_in_runtime = 0
    for record in records:
        if record.leakage_controls.contains_future_price_outcome and record.leakage_controls.may_be_seen_by_extractor_llm:
            forbidden_future_in_runtime += 1
    source_proxy_to_score = sum(
        1
        for record in records
        if (record.source_proxy_only or record.evidence_url_pending)
        and (record.fixture_usable or record.runtime_score_eligible or record.usage_policy.allowed_for_score_contribution)
    )
    missing_policy = sum(1 for record in records if record.usage_policy is None)
    forbidden_plan_keys = 0
    for plan in plans:
        payload = plan.to_dict()
        forbidden_plan_keys += sum(1 for key in ("score", "stage", "current_score_eligible", "hard_break_final") if key in payload)
    return {
        "schema_version": "research_brain_leakage_audit_v1",
        "summary": {
            "future_outcome_in_extraction_prompt_count": forbidden_future_in_extraction,
            "source_proxy_to_score_count": source_proxy_to_score,
            "memory_record_without_usage_policy_count": missing_policy,
            "runtime_llm_seen_forbidden_future_field_count": forbidden_future_in_runtime,
            "planner_prompt_future_pattern_summary_only": all(
                token not in planner_text for token in ("mfe_30d_pct", "mae_30d_pct", "outcome_label")
            ),
            "research_brain_score_output_keys_count": forbidden_plan_keys,
            "leakage_audit_pass": forbidden_future_in_extraction == 0
            and source_proxy_to_score == 0
            and missing_policy == 0
            and forbidden_future_in_runtime == 0
            and forbidden_plan_keys == 0,
        },
    }


def audit_research_brain_hardcoding(paths: Sequence[str | Path]) -> Mapping[str, object]:
    findings = []
    for path_value in paths:
        path = Path(path_value)
        if not path.exists() or path.suffix != ".py":
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for finding_type, pattern in _HARDCODE_PATTERNS.items():
            if pattern.search(text):
                findings.append({"path": str(path), "finding_type": finding_type})
    return {
        "schema_version": "research_brain_hardcoding_audit_v1",
        "summary": {
            "hardcoding_finding_count": len(findings),
            "symbol_exception_count": sum(1 for row in findings if row["finding_type"] == "symbol_exception"),
            "company_exception_count": sum(1 for row in findings if row["finding_type"] == "company_exception"),
            "archetype_fixed_query_count": sum(1 for row in findings if row["finding_type"] == "archetype_fixed_query"),
            "missing_primitive_fixed_query_count": sum(
                1 for row in findings if row["finding_type"] == "missing_primitive_fixed_query"
            ),
            "source_proxy_auto_promotion_count": sum(
                1 for row in findings if row["finding_type"] == "source_proxy_auto_promotion"
            ),
            "hardcoding_audit_pass": len(findings) == 0,
        },
        "findings": findings,
    }


__all__ = ["audit_memory_leakage", "audit_research_brain_hardcoding"]
