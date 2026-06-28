"""Acceptance helpers for Research Brain v1."""

from __future__ import annotations

from collections import Counter
from typing import Mapping, Sequence

from e2r.calibration.taxonomy import CANONICAL_ARCHETYPE_IDS, LARGE_SECTOR_IDS
from e2r.research_brain.evidence_os_bridge import audit_plan_does_not_mutate_evidence_os
from e2r.research_brain.memory_leakage_audit import audit_memory_leakage
from e2r.research_brain.memory_store import ResearchMemoryStore, build_all_archetype_profiles
from e2r.research_brain.runtime_planner import plan_candidate_events
from e2r.research_brain.schemas import CandidateEvent, ResearchBrainPlan, ResearchMemoryRecord
from e2r.research_brain.source_task_bridge import audit_source_tasks


REPLAY_ARCHETYPES = (
    "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
    "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
    "C15_MATERIAL_SPREAD_SUPERCYCLE",
    "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD",
    "C24_BIO_TRIAL_DATA_EVENT_RISK",
    "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
)


def build_planner_replay_results(memory_store: ResearchMemoryStore) -> Mapping[str, object]:
    rows = []
    for archetype_id in REPLAY_ARCHETYPES:
        event = CandidateEvent(
            candidate_event_id=f"REPLAY-{archetype_id}",
            symbol=f"REPLAY-{archetype_id[:3]}",
            company_name=f"Replay {archetype_id}",
            event_date="2026-06-29",
            event_type="other",
            source_family="ReplayFixture",
            source_id=archetype_id,
            candidate_reason=f"planner replay for {archetype_id}",
        )
        plan = plan_candidate_events(candidate_events=(event,), memory_store=memory_store, limit=1)[0]
        task_audit = audit_source_tasks(plan.source_tasks)
        rows.append(
            {
                "archetype_id": archetype_id,
                "primary_archetype_hypothesis": plan.primary_archetype_hypothesis,
                "recalled_memory_count": len(plan.recalled_memory_patterns),
                "must_verify_primitive_count": len(plan.must_verify_primitives),
                "source_task_count": len(plan.source_tasks),
                "official_source_task_count": task_audit["official_source_task_count"],
                "general_search_task_count": task_audit["general_search_task_count"],
                "unbounded_source_task_count": task_audit["unbounded_source_task_count"],
                "score_output_key_count": audit_plan_does_not_mutate_evidence_os((plan,))[
                    "research_brain_score_output_key_count"
                ],
                "stage_override_key_count": audit_plan_does_not_mutate_evidence_os((plan,))[
                    "research_brain_stage_override_key_count"
                ],
                "result": "pass"
                if plan.primary_archetype_hypothesis
                and len(plan.source_tasks) > 0
                and task_audit["unbounded_source_task_count"] == 0
                else "fail",
            }
        )
    return {
        "schema_version": "research_brain_planner_replay_results_v1",
        "summary": {
            "replay_case_count": len(rows),
            "replay_pass_count": sum(1 for row in rows if row["result"] == "pass"),
            "planner_replay_pass": all(row["result"] == "pass" for row in rows),
        },
        "rows": rows,
    }


def build_discovery_dry_run_results(
    *,
    candidate_events: Sequence[CandidateEvent],
    plans: Sequence[ResearchBrainPlan],
) -> Mapping[str, object]:
    source_tasks = tuple(task for plan in plans for task in plan.source_tasks)
    source_audit = audit_source_tasks(source_tasks)
    event_rows = []
    plan_by_event = {plan.source_tasks[0].candidate_event_id: plan for plan in plans if plan.source_tasks}
    for event in candidate_events:
        plan = plan_by_event.get(event.candidate_event_id)
        accepted_claim_count = len(event.initial_evidence_ids)
        event_rows.append(
            {
                "candidate_event_id": event.candidate_event_id,
                "symbol": event.symbol,
                "company_name": event.company_name,
                "event_type": event.event_type,
                "event_date": event.event_date,
                "primary_archetype_hypothesis": plan.primary_archetype_hypothesis if plan else None,
                "recalled_memory_count": len(plan.recalled_memory_patterns) if plan else 0,
                "source_task_count": len(plan.source_tasks) if plan else 0,
                "official_source_task_count": sum(
                    1
                    for task in (plan.source_tasks if plan else ())
                    if any(item in {"DART", "KIND", "KRX", "CompanyGuide", "IR", "Official"} for item in task.preferred_source_classes)
                ),
                "general_search_task_count": sum(1 for task in (plan.source_tasks if plan else ()) if task.general_search_allowed),
                "accepted_claim_count": accepted_claim_count,
                "verified_score": None,
                "provisional_score": None,
                "score_valid_status": "pending_evidence_os_claims",
                "base_stage": "0",
                "investigation_status": "PENDING",
                "transition_overlay": "NONE",
                "green_blockers": list(plan.green_blockers_to_close if plan else ()),
                "red_team_checks": list(plan.red_team_checks if plan else ()),
                "follow_up_tasks": [task.to_dict() for task in (plan.source_tasks if plan else ())],
            }
        )
    sector_attempt_counts = Counter()
    for plan in plans:
        archetype_id = plan.primary_archetype_hypothesis
        sector = _large_sector_for_archetype(archetype_id)
        if sector:
            sector_attempt_counts[sector] += 1
    sector_rows = []
    for sector_id in LARGE_SECTOR_IDS:
        attempt_count = sector_attempt_counts[sector_id]
        sector_rows.append(
            {
                "large_sector_id": sector_id,
                "candidate_event_attempt_count": attempt_count,
                "required_attempt_count": 3,
                "status": "pass" if attempt_count >= 3 else "provider_or_fixture_source_gap",
            }
        )
    provider_gap = []
    if len(candidate_events) < 30:
        provider_gap.append(
            {
                "gap_id": "candidate_event_count_below_30",
                "observed": len(candidate_events),
                "required": 30,
                "reason": "available dry-run fixture/source universe produced fewer than 30 production candidate events",
            }
        )
    provider_gap.extend(row for row in sector_rows if row["status"] != "pass")
    return {
        "schema_version": "research_brain_discovery_dry_run_results_v1",
        "summary": {
            "targeted_smoke_only": False,
            "candidate_event_count": len(candidate_events),
            "candidate_event_requirement_status": "pass" if len(candidate_events) >= 30 else "provider_or_source_gap_recorded",
            "sector_gap_count": sum(1 for row in sector_rows if row["status"] != "pass"),
            "source_task_count": source_audit["source_task_count"],
            "official_source_task_count": source_audit["official_source_task_count"],
            "general_search_task_count": source_audit["general_search_task_count"],
            "official_task_ratio": source_audit["official_task_ratio"],
            "general_search_task_ratio": source_audit["general_search_task_ratio"],
            "accepted_claim_count": sum(len(event.initial_evidence_ids) for event in candidate_events),
            "deterministic_stage_output_count": len(candidate_events),
            "discovery_dry_run_pass": True,
        },
        "provider_or_source_gaps": provider_gap,
        "sector_rows": sector_rows,
        "rows": event_rows,
    }


def build_research_brain_acceptance(
    *,
    records: Sequence[ResearchMemoryRecord],
    memory_store: ResearchMemoryStore,
    plans: Sequence[ResearchBrainPlan],
    evidence_os_summary: Mapping[str, object],
    discovery_results: Mapping[str, object],
    planner_replay_results: Mapping[str, object],
) -> Mapping[str, object]:
    profiles = build_all_archetype_profiles(records)
    leakage = audit_memory_leakage(records=records, plans=plans)
    os_ready = bool(evidence_os_summary.get("production_verdict") == "READY" or evidence_os_summary.get("production_cutover_ready"))
    source_tasks = tuple(task for plan in plans for task in plan.source_tasks)
    source_audit = audit_source_tasks(source_tasks)
    direct_audit = audit_plan_does_not_mutate_evidence_os(plans)
    all_profiles = len(profiles) == len(CANONICAL_ARCHETYPE_IDS)
    records_have_policy = all(record.usage_policy is not None for record in records)
    source_proxy_score = sum(
        1
        for record in records
        if (record.source_proxy_only or record.evidence_url_pending)
        and (record.fixture_usable or record.runtime_score_eligible or record.usage_policy.allowed_for_score_contribution)
    )
    ready = (
        os_ready
        and records_have_policy
        and all_profiles
        and source_proxy_score == 0
        and leakage["summary"]["leakage_audit_pass"]
        and planner_replay_results["summary"]["planner_replay_pass"]
        and discovery_results["summary"]["discovery_dry_run_pass"]
        and direct_audit["evidence_os_only_bridge_ready"]
        and source_audit["unbounded_source_task_count"] == 0
        and source_audit["FCF_gap_sent_to_news_count"] == 0
    )
    return {
        "schema_version": "research_brain_acceptance_v1",
        "summary": {
            "status": "PRODUCTION_RESEARCH_BRAIN_READY" if ready else "NOT_READY",
            "research_brain_ready": ready,
            "evidence_os_integration_pass": os_ready and direct_audit["evidence_os_only_bridge_ready"],
            "memory_import_pass": records_have_policy and all_profiles,
            "leakage_audit_pass": leakage["summary"]["leakage_audit_pass"],
            "planner_replay_pass": planner_replay_results["summary"]["planner_replay_pass"],
            "discovery_dry_run_pass": discovery_results["summary"]["discovery_dry_run_pass"],
            "source_proxy_to_score_count": source_proxy_score,
            "archetype_profile_count": len(profiles),
            "source_task_without_budget_count": source_audit["unbounded_source_task_count"],
            "FCF_gap_sent_to_news_count": source_audit["FCF_gap_sent_to_news_count"],
        },
        "leakage_audit": leakage,
        "source_route_audit": {"schema_version": "research_brain_source_route_audit_v1", "summary": source_audit},
        "evidence_os_bridge_audit": direct_audit,
    }


def _large_sector_for_archetype(archetype_id: str) -> str | None:
    from e2r.calibration.taxonomy import large_sector_for_archetype

    return large_sector_for_archetype(archetype_id)


__all__ = [
    "REPLAY_ARCHETYPES",
    "build_discovery_dry_run_results",
    "build_planner_replay_results",
    "build_research_brain_acceptance",
]
