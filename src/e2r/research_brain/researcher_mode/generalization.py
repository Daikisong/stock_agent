"""Audit Researcher Mode generalization across the complete archetype registry.

The audit is deliberately structural.  It proves that every registered
archetype can enter the same seven-component research planner, source graph,
historical-memory isolation, and proxy-safety path.  It does not manufacture a
current score or Stage for archetypes that have not been researched as of a
real target date.
"""

from __future__ import annotations

import ast
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.agentic.evidence_contract_v2 import load_evidence_contracts_v2
from e2r.agentic.evidence_os import EvidenceContractV2
from e2r.calibration.taxonomy import CANONICAL_ARCHETYPE_IDS
from e2r.production.metadata import stable_hash, write_json

from .component_research_planner import ComponentResearchPlanner
from .schemas import CANONICAL_COMPONENT_ORDER
from .source_graph_explorer import SourceGraphExplorer


ALL_ARCHETYPE_GENERALIZATION_SCHEMA_VERSION = (
    "e2r_v5_all_archetype_generalization_v1"
)
ALL_ARCHETYPE_GENERALIZATION_PASS = (
    "V5_PHASE96_ALL_ARCHETYPE_RESEARCHER_GENERALIZATION_PASS"
)
ALL_ARCHETYPE_GENERALIZATION_FAIL = (
    "V5_PHASE96_ALL_ARCHETYPE_RESEARCHER_GENERALIZATION_FAIL"
)

MANDATORY_GENERALIZATION_CANARIES = (
    "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
    "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
    "C15_MATERIAL_SPREAD_SUPERCYCLE",
    "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD",
    "C24_BIO_TRIAL_DATA_EVENT_RISK",
    "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
)

DEFAULT_GENERALIZATION_OUTPUT_PATH = (
    "docs/operational/e2r_v5_all_archetype_generalization.json"
)
DEFAULT_GENERALIZATION_AS_OF_DATE = "2026-07-12"

_DEFAULT_PRODUCTION_SOURCE_PATHS = (
    "src/e2r/research_brain/researcher_mode/component_research_planner.py",
    "src/e2r/research_brain/researcher_mode/source_graph_explorer.py",
    "src/e2r/research_brain/researcher_mode/current_researcher_mode.py",
    "src/e2r/research_brain/researcher_mode/stagecourt.py",
    "src/e2r/research_brain/researcher_mode/generalization.py",
)
_CONDITIONED_IDENTIFIERS = {
    "archetype",
    "archetype_id",
    "canonical_archetype_id",
    "company",
    "company_name",
    "symbol",
    "target",
    "target_id",
    "ticker",
}


def compile_all_archetype_generalization(
    *,
    repo_root: str | Path = ".",
    anchor_atlas_payload: Mapping[str, Any] | None = None,
    blind_replay_payload: Mapping[str, Any] | None = None,
    contracts: Mapping[str, EvidenceContractV2] | None = None,
    registry_ids: Sequence[str] | None = None,
    as_of_date: str = DEFAULT_GENERALIZATION_AS_OF_DATE,
    production_source_paths: Sequence[str] = _DEFAULT_PRODUCTION_SOURCE_PATHS,
) -> Mapping[str, Any]:
    """Compile a reproducible, non-scoring generalization audit."""

    root = Path(repo_root)
    anchor_atlas = (
        _read_json(root / "docs/operational/e2r_v5_component_anchor_atlas.json")
        if anchor_atlas_payload is None
        else anchor_atlas_payload
    )
    blind_replay = (
        _read_json(root / "docs/operational/e2r_v5_historical_blind_replay.json")
        if blind_replay_payload is None
        else blind_replay_payload
    )
    evidence_contracts = (
        load_evidence_contracts_v2(require_all_archetypes=True)
        if contracts is None
        else contracts
    )
    registry = tuple(
        CANONICAL_ARCHETYPE_IDS if registry_ids is None else registry_ids
    )

    anchors = tuple(anchor_atlas.get("component_anchors") or ())
    coverage_rows = tuple(anchor_atlas.get("component_coverage") or ())
    exemplar_rows = tuple(anchor_atlas.get("archetype_role_exemplars") or ())
    blind_coverage_rows = tuple(
        blind_replay.get("registry_archetype_coverage") or ()
    )
    executed_leave_one_out_rows = tuple(
        blind_replay.get("leave_one_out_audits") or ()
    )

    anchors_by_archetype: dict[str, list[Mapping[str, Any]]] = defaultdict(list)
    for row in anchors:
        anchors_by_archetype[str(row.get("archetype_id") or "")].append(row)
    coverage_by_key = {
        (str(row.get("archetype_id") or ""), str(row.get("component_id") or "")): row
        for row in coverage_rows
    }
    exemplars_by_key = {
        (str(row.get("archetype_id") or ""), str(row.get("role") or "")): row
        for row in exemplar_rows
    }
    blind_by_archetype = {
        str(row.get("archetype_id") or ""): row
        for row in blind_coverage_rows
    }
    executed_loo_by_judgment = {
        str(row.get("target_judgment_id") or ""): row
        for row in executed_leave_one_out_rows
        if row.get("target_judgment_id")
    }

    planner = ComponentResearchPlanner()
    explorer = SourceGraphExplorer()
    archetype_results = []
    for archetype_id in registry:
        contract = evidence_contracts.get(archetype_id)
        archetype_anchors = tuple(anchors_by_archetype.get(archetype_id, ()))
        component_anchor_rows = tuple(
            _component_anchor_coverage(
                coverage_by_key.get((archetype_id, component_id)),
                archetype_id=archetype_id,
                component_id=component_id,
            )
            for component_id in CANONICAL_COMPONENT_ORDER
        )
        blind_row = blind_by_archetype.get(archetype_id, {})
        leave_one_out = _compile_leave_one_out_replay(
            archetype_id=archetype_id,
            blind_coverage=blind_row,
            all_anchors=anchors,
            component_coverage=component_anchor_rows,
            executed_audit=executed_loo_by_judgment.get(
                str(blind_row.get("selected_judgment_id") or "")
            ),
        )

        planning_error = None
        plans = ()
        exploration = None
        if contract is None:
            planning_error = "EVIDENCE_CONTRACT_MISSING"
        else:
            try:
                plans = planner.plan(
                    target_id="PHASE96_GENERIC_RESEARCH_TARGET",
                    archetype_id=archetype_id,
                    evidence_facts=(),
                    historical_anchors=archetype_anchors,
                    research_seeds=(),
                )
                exploration = explorer.explore(
                    target_id="PHASE96_GENERIC_RESEARCH_TARGET",
                    as_of_date=as_of_date,
                    documents=(),
                    research_plans=plans,
                    source_coverage=(),
                )
            except (KeyError, TypeError, ValueError) as exc:
                planning_error = f"{type(exc).__name__}:{exc}"

        objectives_by_component = {
            row.component_id: row
            for row in (() if exploration is None else exploration.open_objectives)
        }
        plans_by_component = {row.component_id: row for row in plans}
        component_strategies = tuple(
            _component_strategy(
                component_id=component_id,
                plan=plans_by_component.get(component_id),
                objective=objectives_by_component.get(component_id),
                coverage=coverage_by_key.get((archetype_id, component_id)),
                contract=contract,
            )
            for component_id in CANONICAL_COMPONENT_ORDER
        )
        positive = exemplars_by_key.get((archetype_id, "POSITIVE"))
        counter = exemplars_by_key.get((archetype_id, "COUNTER"))
        row_reasons = _archetype_failure_reasons(
            contract=contract,
            component_strategies=component_strategies,
            positive_exemplar=positive,
            counter_exemplar=counter,
            leave_one_out=leave_one_out,
            planning_error=planning_error,
            archetype_anchors=archetype_anchors,
        )
        archetype_results.append(
            {
                "archetype_id": archetype_id,
                "status": (
                    "ALL_ARCHETYPE_GENERALIZATION_PASS"
                    if not row_reasons
                    else "ALL_ARCHETYPE_GENERALIZATION_FAIL"
                ),
                "failure_reasons": row_reasons,
                "mandatory_canary": archetype_id
                in MANDATORY_GENERALIZATION_CANARIES,
                "evidence_contract": _contract_summary(contract),
                "historical_judgment_anchors": {
                    "anchor_count": len(archetype_anchors),
                    "exact_anchor_count": sum(
                        bool(row.get("usable_as_exact_anchor"))
                        for row in archetype_anchors
                    ),
                    "ordinal_anchor_count": sum(
                        bool(row.get("usable_as_ordinal_anchor"))
                        for row in archetype_anchors
                    ),
                    "source_proxy_guard_anchor_count": sum(
                        bool(row.get("source_proxy_guard_case_ids"))
                        for row in archetype_anchors
                    ),
                    "component_coverage": list(component_anchor_rows),
                },
                "component_research_strategies": list(component_strategies),
                "source_graph": {
                    "objective_count": len(objectives_by_component),
                    "component_ids": list(objectives_by_component),
                    "literal_query_count": sum(
                        row.literal_query is not None
                        for row in objectives_by_component.values()
                    ),
                    "llm_query_generation_required": all(
                        row.query_must_be_generated_by_llm
                        for row in objectives_by_component.values()
                    ),
                    "score_authority": False,
                },
                "positive_example": _exemplar_summary(positive),
                "counter_example": _exemplar_summary(counter),
                "leave_one_out_replay": leave_one_out,
                "current_score_authority": False,
                "current_stage_authority": False,
            }
        )

    branch_scan = _scan_conditioned_branches(
        repo_root=root,
        source_paths=production_source_paths,
    )
    registry_set = set(registry)
    anchor_registry = {
        str(row.get("archetype_id") or "") for row in coverage_rows
    }
    blind_registry = {
        str(row.get("archetype_id") or "") for row in blind_coverage_rows
    }
    contract_registry = set(evidence_contracts)
    expected_component_keys = {
        (archetype_id, component_id)
        for archetype_id in registry
        for component_id in CANONICAL_COMPONENT_ORDER
    }
    observed_component_keys = {
        (str(row.get("archetype_id") or ""), str(row.get("component_id") or ""))
        for row in coverage_rows
    }
    duplicate_component_key_count = len(coverage_rows) - len(observed_component_keys)
    result_by_archetype = {
        row["archetype_id"]: row for row in archetype_results
    }
    canary_results = [
        {
            "archetype_id": archetype_id,
            "status": (
                result_by_archetype.get(archetype_id, {}).get("status")
                or "MISSING"
            ),
        }
        for archetype_id in MANDATORY_GENERALIZATION_CANARIES
    ]
    source_proxy_exact_count = sum(
        bool(row.get("source_proxy_guard_case_ids"))
        and bool(row.get("usable_as_exact_anchor"))
        for row in anchors
    )
    conditioned_anchor_count = sum(
        bool(row.get("company_name_conditioned"))
        or bool(row.get("target_symbol_conditioned"))
        for row in anchors
    )
    critical_counts = {
        "anchor_atlas_input_not_pass_count": int(
            anchor_atlas.get("status") != "COMPONENT_ANCHOR_ATLAS_PASS"
        ),
        "blind_replay_input_not_pass_count": int(
            blind_replay.get("status")
            != "V5_PHASE91_HISTORICAL_BLIND_RESEARCHER_PARITY_PASS"
        ),
        "registry_anchor_coverage_mismatch_count": len(
            registry_set.symmetric_difference(anchor_registry)
        ),
        "registry_blind_coverage_mismatch_count": len(
            registry_set.symmetric_difference(blind_registry)
        ),
        "registry_evidence_contract_mismatch_count": len(
            registry_set.symmetric_difference(contract_registry)
        ),
        "archetype_component_roster_mismatch_count": len(
            expected_component_keys.symmetric_difference(observed_component_keys)
        )
        + max(0, duplicate_component_key_count),
        "archetype_component_strategy_gap_count": sum(
            len(row["component_research_strategies"])
            != len(CANONICAL_COMPONENT_ORDER)
            or any(
                strategy["status"] != "COMPONENT_GENERALIZATION_PASS"
                for strategy in row["component_research_strategies"]
            )
            for row in archetype_results
        ),
        "archetype_source_graph_route_gap_count": sum(
            row["source_graph"]["objective_count"]
            != len(CANONICAL_COMPONENT_ORDER)
            or not row["source_graph"]["llm_query_generation_required"]
            or row["source_graph"]["literal_query_count"] != 0
            for row in archetype_results
        ),
        "archetype_positive_exemplar_gap_count": sum(
            row["positive_example"]["explicit_gap"]
            for row in archetype_results
        ),
        "archetype_counter_exemplar_gap_count": sum(
            row["counter_example"]["explicit_gap"]
            for row in archetype_results
        ),
        "archetype_leave_one_out_failure_count": sum(
            row["leave_one_out_replay"]["status"]
            != "LEAVE_ONE_OUT_REPLAY_PASS"
            for row in archetype_results
        ),
        "leave_one_out_target_leakage_count": sum(
            row["leave_one_out_replay"]["target_reference_count_after_filter"]
            for row in archetype_results
        ),
        "exact_source_gap_without_reason_count": sum(
            row["leave_one_out_replay"]["coverage_status"]
            == "EXACT_SOURCE_GAP"
            and not row["leave_one_out_replay"]["exact_source_gap_reason"]
            for row in archetype_results
        ),
        "source_proxy_exact_current_score_anchor_count": source_proxy_exact_count,
        "company_or_symbol_conditioned_anchor_count": conditioned_anchor_count,
        "mandatory_canary_failure_count": sum(
            row["status"] != "ALL_ARCHETYPE_GENERALIZATION_PASS"
            for row in canary_results
        ),
        "production_conditioned_branch_count": branch_scan["finding_count"],
        "score_or_stage_authority_violation_count": sum(
            bool(row["current_score_authority"])
            or bool(row["current_stage_authority"])
            or bool(row["source_graph"]["score_authority"])
            for row in archetype_results
        ),
    }
    critical_count_sum = sum(critical_counts.values())
    payload: dict[str, Any] = {
        "schema_version": ALL_ARCHETYPE_GENERALIZATION_SCHEMA_VERSION,
        "status": (
            ALL_ARCHETYPE_GENERALIZATION_PASS
            if critical_count_sum == 0
            else ALL_ARCHETYPE_GENERALIZATION_FAIL
        ),
        "phase_scope": "STRUCTURAL_GENERALIZATION_AUDIT_NOT_CURRENT_SCORING",
        "as_of_date": as_of_date,
        "registry_autoloaded": registry_ids is None,
        "registry_archetype_count": len(registry),
        "canonical_component_count": len(CANONICAL_COMPONENT_ORDER),
        "critical_counts": critical_counts,
        "critical_count_sum": critical_count_sum,
        "mandatory_canaries": canary_results,
        "source_proxy_policy": {
            "allowed_uses": ["ORDINAL_GUARD", "QUERY_STRATEGY_CONTEXT"],
            "exact_current_score_anchor_allowed": False,
            "current_stage_authority": False,
        },
        "query_policy": {
            "literal_query_in_generalization_artifact_allowed": False,
            "query_generation_authority": "LLM",
            "deterministic_code_authority": (
                "VALIDATE_SCOPE_AS_OF_DUPLICATE_FUTURE_LEAKAGE_AND_EXECUTE"
            ),
        },
        "production_conditioned_branch_scan": branch_scan,
        "archetypes": archetype_results,
    }
    payload["audit_hash"] = stable_hash(payload)
    return payload


def write_all_archetype_generalization(
    payload: Mapping[str, Any],
    *,
    output_path: str | Path = DEFAULT_GENERALIZATION_OUTPUT_PATH,
) -> Path:
    path = Path(output_path)
    write_json(path, payload)
    return path


def _component_anchor_coverage(
    row: Mapping[str, Any] | None,
    *,
    archetype_id: str,
    component_id: str,
) -> Mapping[str, Any]:
    if row is None:
        return {
            "archetype_id": archetype_id,
            "component_id": component_id,
            "anchor_count": 0,
            "ordinal_anchor_count": 0,
            "exact_anchor_count": 0,
            "positive_anchor_count": 0,
            "counter_anchor_count": 0,
            "explicit_gap": False,
            "gap_reason": "COMPONENT_COVERAGE_ROW_MISSING",
        }
    return {
        key: row.get(key)
        for key in (
            "archetype_id",
            "component_id",
            "anchor_count",
            "ordinal_anchor_count",
            "exact_anchor_count",
            "positive_anchor_count",
            "counter_anchor_count",
            "explicit_gap",
            "gap_reason",
        )
    }


def _component_strategy(
    *,
    component_id: str,
    plan: Any,
    objective: Any,
    coverage: Mapping[str, Any] | None,
    contract: EvidenceContractV2 | None,
) -> Mapping[str, Any]:
    coverage_summary = _component_anchor_coverage(
        coverage,
        archetype_id=str((coverage or {}).get("archetype_id") or "MISSING"),
        component_id=component_id,
    )
    anchor_ready = bool(coverage_summary["ordinal_anchor_count"]) or bool(
        coverage_summary["explicit_gap"]
    )
    route_ready = bool(
        objective is not None
        and objective.preferred_source_families
        and objective.literal_query is None
        and objective.query_must_be_generated_by_llm
    )
    plan_ready = bool(plan is not None and plan.component_id == component_id)
    return {
        "component_id": component_id,
        "status": (
            "COMPONENT_GENERALIZATION_PASS"
            if plan_ready and route_ready and anchor_ready and contract is not None
            else "COMPONENT_GENERALIZATION_FAIL"
        ),
        "researcher_role": None if plan is None else plan.researcher_role,
        "component_max_points": (
            None if plan is None else plan.component_max_points
        ),
        "research_questions": (
            [] if plan is None else list(plan.research_questions)
        ),
        "structured_metric_requirements": (
            [] if plan is None else list(plan.structured_metric_requirements)
        ),
        "historical_anchor_count": (
            0 if plan is None else len(plan.candidate_anchor_ids)
        ),
        "historical_anchor_explicit_gap": bool(
            coverage_summary["explicit_gap"]
        ),
        "historical_anchor_gap_reason": coverage_summary["gap_reason"],
        "contract_primitive_hints": (
            []
            if contract is None
            else list(contract.score_rubric.get(component_id, ()))
        ),
        "contract_primitive_hints_are_non_exhaustive": True,
        "new_economic_mechanism_allowed": True,
        "source_graph_objective_id": (
            None if objective is None else objective.objective_id
        ),
        "preferred_source_families": (
            [] if objective is None else list(objective.preferred_source_families)
        ),
        "positive_counter_supersession_required": bool(
            objective is not None
            and objective.counter_or_supersession_required
        ),
        "stop_condition": None if objective is None else objective.stop_condition,
        "literal_query": None if objective is None else objective.literal_query,
        "query_generation_authority": "LLM",
        "score_authority": False,
        "stage_authority": False,
    }


def _compile_leave_one_out_replay(
    *,
    archetype_id: str,
    blind_coverage: Mapping[str, Any],
    all_anchors: Sequence[Mapping[str, Any]],
    component_coverage: Sequence[Mapping[str, Any]],
    executed_audit: Mapping[str, Any] | None,
) -> Mapping[str, Any]:
    target_case_id = str(
        blind_coverage.get("selected_research_case_id") or ""
    )
    target_judgment_id = str(
        blind_coverage.get("selected_judgment_id") or ""
    )
    coverage_status = str(blind_coverage.get("coverage_status") or "MISSING")
    excluded = tuple(
        row
        for row in all_anchors
        if target_case_id
        and target_case_id
        in {
            *tuple(row.get("source_backed_case_ids") or ()),
            *tuple(row.get("source_proxy_guard_case_ids") or ()),
        }
    )
    excluded_ids = {str(row.get("anchor_id") or "") for row in excluded}
    retained = tuple(
        row
        for row in all_anchors
        if str(row.get("archetype_id") or "") == archetype_id
        and str(row.get("anchor_id") or "") not in excluded_ids
        and bool(row.get("usable_as_ordinal_anchor"))
    )
    retained_by_component = Counter(
        str(row.get("component_id") or "") for row in retained
    )
    target_reference_count_after_filter = sum(
        bool(target_case_id)
        and target_case_id
        in {
            *tuple(row.get("source_backed_case_ids") or ()),
            *tuple(row.get("source_proxy_guard_case_ids") or ()),
        }
        for row in retained
    )
    component_results = []
    for row in component_coverage:
        component_id = str(row.get("component_id") or "")
        retained_count = retained_by_component.get(component_id, 0)
        explicit_gap = bool(row.get("explicit_gap"))
        component_results.append(
            {
                "component_id": component_id,
                "retained_ordinal_anchor_count": retained_count,
                "explicit_historical_gap": explicit_gap,
                "gap_reason": row.get("gap_reason"),
                "memory_ready": bool(retained_count) or explicit_gap,
            }
        )
    source_backed_holdout_ready = bool(
        coverage_status != "SOURCE_BACKED_HOLDOUT"
        or (target_case_id and target_judgment_id and excluded)
    )
    exact_gap_ready = bool(
        coverage_status != "EXACT_SOURCE_GAP"
        or blind_coverage.get("exact_source_gap_reason")
    )
    executed_target_presence = (
        None
        if executed_audit is None
        else sum(
            int(value)
            for value in (
                executed_audit.get("target_presence_after_filter") or {}
            ).values()
        )
    )
    replay_ready = bool(
        coverage_status in {"SOURCE_BACKED_HOLDOUT", "EXACT_SOURCE_GAP"}
        and source_backed_holdout_ready
        and exact_gap_ready
        and target_reference_count_after_filter == 0
        and all(row["memory_ready"] for row in component_results)
        and (executed_target_presence in (None, 0))
    )
    replay_mode = (
        "PHASE91_EXECUTED_BLIND_REPLAY"
        if executed_audit is not None
        else "EXACT_SOURCE_GAP_ORDINAL_ONLY_STRUCTURAL_REPLAY"
        if coverage_status == "EXACT_SOURCE_GAP"
        else "SOURCE_BACKED_STRUCTURAL_MEMORY_ISOLATION_REPLAY"
    )
    return {
        "status": (
            "LEAVE_ONE_OUT_REPLAY_PASS"
            if replay_ready
            else "LEAVE_ONE_OUT_REPLAY_FAIL"
        ),
        "replay_mode": replay_mode,
        "coverage_status": coverage_status,
        "target_research_case_id": target_case_id or None,
        "target_judgment_id": target_judgment_id or None,
        "exact_source_gap_reason": blind_coverage.get(
            "exact_source_gap_reason"
        ),
        "excluded_anchor_ids": sorted(excluded_ids),
        "excluded_anchor_count": len(excluded_ids),
        "retained_ordinal_anchor_count": len(retained),
        "retained_component_memory": component_results,
        "target_reference_count_after_filter": (
            target_reference_count_after_filter
        ),
        "phase91_executed_audit_target_presence_count": (
            executed_target_presence
        ),
        "safe_memory_hash": stable_hash(
            sorted(str(row.get("anchor_id") or "") for row in retained)
        ),
        "source_proxy_exact_current_score_allowed": False,
        "current_score_replay_authority": False,
        "current_stage_replay_authority": False,
    }


def _archetype_failure_reasons(
    *,
    contract: EvidenceContractV2 | None,
    component_strategies: Sequence[Mapping[str, Any]],
    positive_exemplar: Mapping[str, Any] | None,
    counter_exemplar: Mapping[str, Any] | None,
    leave_one_out: Mapping[str, Any],
    planning_error: str | None,
    archetype_anchors: Sequence[Mapping[str, Any]],
) -> list[str]:
    reasons = []
    if contract is None:
        reasons.append("EVIDENCE_CONTRACT_MISSING")
    if planning_error:
        reasons.append(f"PLANNING_ERROR:{planning_error}")
    if len(component_strategies) != len(CANONICAL_COMPONENT_ORDER) or any(
        row["status"] != "COMPONENT_GENERALIZATION_PASS"
        for row in component_strategies
    ):
        reasons.append("SEVEN_COMPONENT_STRATEGY_INCOMPLETE")
    if positive_exemplar is None or positive_exemplar.get("explicit_gap"):
        reasons.append("POSITIVE_EXEMPLAR_MISSING")
    if counter_exemplar is None or counter_exemplar.get("explicit_gap"):
        reasons.append("COUNTER_EXEMPLAR_MISSING")
    if leave_one_out["status"] != "LEAVE_ONE_OUT_REPLAY_PASS":
        reasons.append("LEAVE_ONE_OUT_REPLAY_FAILED")
    if any(
        bool(row.get("source_proxy_guard_case_ids"))
        and bool(row.get("usable_as_exact_anchor"))
        for row in archetype_anchors
    ):
        reasons.append("SOURCE_PROXY_USED_AS_EXACT_ANCHOR")
    if any(
        bool(row.get("company_name_conditioned"))
        or bool(row.get("target_symbol_conditioned"))
        for row in archetype_anchors
    ):
        reasons.append("TARGET_CONDITIONED_ANCHOR")
    return reasons


def _contract_summary(
    contract: EvidenceContractV2 | None,
) -> Mapping[str, Any] | None:
    if contract is None:
        return None
    return {
        "archetype_id": contract.archetype_id,
        "required_primitives": list(contract.required_primitives),
        "green_gate_primitive_ids": list(contract.green_gate.primitive_ids()),
        "route_hints": {
            str(key): list(values)
            for key, values in sorted(contract.route_hints.items())
        },
        "score_rubric_component_ids": list(contract.score_rubric),
        "guard_primitive_ids": list(contract.guard_modes),
        "score_authority": False,
        "stage_authority": False,
    }


def _exemplar_summary(
    row: Mapping[str, Any] | None,
) -> Mapping[str, Any]:
    if row is None:
        return {
            "research_case_id": None,
            "role": None,
            "economic_fact_patterns": [],
            "source_quality": None,
            "explicit_gap": True,
            "gap_reason": "ROLE_EXEMPLAR_ROW_MISSING",
            "score_authority": False,
        }
    return {
        "research_case_id": row.get("research_case_id"),
        "role": row.get("role"),
        "economic_fact_patterns": list(
            row.get("economic_fact_patterns") or ()
        ),
        "source_quality": row.get("source_quality"),
        "reported_stage": row.get("reported_stage"),
        "explicit_gap": bool(row.get("explicit_gap")),
        "gap_reason": row.get("gap_reason"),
        "company_name_conditioned": bool(
            row.get("company_name_conditioned")
        ),
        "target_symbol_conditioned": bool(
            row.get("target_symbol_conditioned")
        ),
        "score_authority": False,
        "current_stage_authority": False,
    }


def _scan_conditioned_branches(
    *,
    repo_root: Path,
    source_paths: Sequence[str],
) -> Mapping[str, Any]:
    findings = []
    scanned = []
    for relative_path in source_paths:
        path = repo_root / relative_path
        scanned.append(relative_path)
        if not path.exists():
            findings.append(
                {
                    "path": relative_path,
                    "line": None,
                    "kind": "SOURCE_FILE_MISSING",
                }
            )
            continue
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=relative_path)
        for node in ast.walk(tree):
            if isinstance(node, ast.Compare):
                operands = (node.left, *node.comparators)
                for left, right in zip(operands, operands[1:]):
                    if (
                        _is_conditioned_operand(left)
                        and _is_literal_operand(right)
                    ) or (
                        _is_conditioned_operand(right)
                        and _is_literal_operand(left)
                    ):
                        findings.append(
                            {
                                "path": relative_path,
                                "line": node.lineno,
                                "kind": "LITERAL_CONDITIONED_COMPARISON",
                            }
                        )
                        break
            if (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and node.func.attr in {"startswith", "endswith"}
                and _is_conditioned_operand(node.func.value)
                and any(_is_literal_operand(arg) for arg in node.args)
            ):
                findings.append(
                    {
                        "path": relative_path,
                        "line": node.lineno,
                        "kind": "LITERAL_CONDITIONED_PREFIX_BRANCH",
                    }
                )
    return {
        "scanner": "PYTHON_AST_CONDITIONED_BRANCH_SCAN_V1",
        "scanned_paths": list(scanned),
        "finding_count": len(findings),
        "findings": findings,
    }


def _is_conditioned_operand(node: ast.AST) -> bool:
    if isinstance(node, ast.Name):
        return node.id.lower() in _CONDITIONED_IDENTIFIERS
    if isinstance(node, ast.Attribute):
        return node.attr.lower() in _CONDITIONED_IDENTIFIERS
    if isinstance(node, ast.Subscript):
        return _literal_text(node.slice) in _CONDITIONED_IDENTIFIERS
    if (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr == "get"
        and node.args
    ):
        return _literal_text(node.args[0]) in _CONDITIONED_IDENTIFIERS
    return False


def _is_literal_operand(node: ast.AST) -> bool:
    if isinstance(node, ast.Constant):
        return isinstance(node.value, str)
    if isinstance(node, (ast.Tuple, ast.List, ast.Set)):
        return bool(node.elts) and all(_is_literal_operand(item) for item in node.elts)
    return False


def _literal_text(node: ast.AST) -> str:
    return (
        str(node.value).lower()
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
        else ""
    )


def _read_json(path: Path) -> Mapping[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


__all__ = [
    "ALL_ARCHETYPE_GENERALIZATION_FAIL",
    "ALL_ARCHETYPE_GENERALIZATION_PASS",
    "ALL_ARCHETYPE_GENERALIZATION_SCHEMA_VERSION",
    "DEFAULT_GENERALIZATION_AS_OF_DATE",
    "DEFAULT_GENERALIZATION_OUTPUT_PATH",
    "MANDATORY_GENERALIZATION_CANARIES",
    "compile_all_archetype_generalization",
    "write_all_archetype_generalization",
]
