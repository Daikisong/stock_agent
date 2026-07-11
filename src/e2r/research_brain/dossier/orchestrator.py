"""Build bounded, target-generic full-thesis research dossiers."""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any, Mapping, Sequence


DOSSIER_ORCHESTRATOR_SCHEMA_VERSION = "e2r_full_thesis_dossier_orchestrator_v1"
TERMINAL_QUESTION_STATUSES = {
    "SUPPORTED",
    "PARTIALLY_SUPPORTED",
    "EVALUATED_ABSENT",
    "COUNTERED",
    "SOURCE_EXHAUSTED",
    "PROVIDER_PENDING",
}


@dataclass(frozen=True)
class DossierTarget:
    target_id: str
    company_name: str

    def __post_init__(self) -> None:
        if not self.target_id.strip() or not self.company_name.strip():
            raise ValueError("dossier target id and company name are required")


@dataclass(frozen=True)
class DossierRunConfig:
    as_of_date: str
    canonical_archetype: str
    output_root: str | Path
    max_research_iterations: int = 12
    max_code_repair_iterations: int = 10
    materialize_live_input: bool = False
    live_materialization_authorized: bool = False
    require_organic_claim: bool = True
    require_calibrated_component_score: bool = True
    require_full_score_valid: bool = True

    def __post_init__(self) -> None:
        date.fromisoformat(self.as_of_date)
        if not 1 <= self.max_research_iterations <= 50:
            raise ValueError("research iterations must be bounded between 1 and 50")
        if not 0 <= self.max_code_repair_iterations <= 25:
            raise ValueError("code repair iterations must be bounded between 0 and 25")
        if self.materialize_live_input and not self.live_materialization_authorized:
            raise ValueError("live input materialization requires explicit authorization")
        if self.live_materialization_authorized and not self.materialize_live_input:
            raise ValueError("live authorization is invalid when materialization is disabled")


@dataclass(frozen=True)
class DossierInitializationResult:
    status: str
    target_results: tuple[Mapping[str, Any], ...]
    audit: Mapping[str, Any]


def load_question_family_catalog(path: str | Path) -> Mapping[str, Any]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(payload, Mapping):
        raise ValueError("question family catalog must be a JSON object")
    if payload.get("schema_version") != "e2r_full_thesis_question_families_v1":
        raise ValueError("question family catalog schema mismatch")
    _validate_question_family_catalog(payload)
    return payload


class FullThesisDossierOrchestrator:
    def __init__(self, *, question_family_catalog: Mapping[str, Any]) -> None:
        _validate_question_family_catalog(question_family_catalog)
        self.catalog = question_family_catalog

    def initialize(
        self, config: DossierRunConfig, *, targets: Sequence[DossierTarget]
    ) -> DossierInitializationResult:
        if not targets:
            raise ValueError("at least one dossier target is required")
        target_ids = [target.target_id for target in targets]
        if len(target_ids) != len(set(target_ids)):
            raise ValueError("dossier targets must be unique")
        archetypes = dict(self.catalog.get("archetypes") or {})
        archetype = archetypes.get(config.canonical_archetype)
        if not isinstance(archetype, Mapping):
            raise ValueError(
                f"question family recipe is missing: {config.canonical_archetype}"
            )
        families = tuple(archetype.get("question_families") or ())
        results = tuple(
            self._initialize_target(config=config, target=target, families=families)
            for target in targets
        )
        critical = {
            "target_output_missing_count": sum(
                not Path(str(row["output_root"])).is_dir() for row in results
            ),
            "question_family_coverage_gap_count": sum(
                int(row["question_family_count"]) != len(families) for row in results
            ),
            "unbounded_task_count": sum(
                int(row["unbounded_task_count"]) for row in results
            ),
            "literal_query_in_recipe_count": _literal_query_count(self.catalog),
            "nonterminal_missing_status_count": sum(
                int(row["nonterminal_missing_status_count"]) for row in results
            ),
            "target_specific_branch_count": 0,
        }
        return DossierInitializationResult(
            status=(
                "DOSSIER_ORCHESTRATOR_INITIALIZED"
                if sum(critical.values()) == 0
                else "DOSSIER_ORCHESTRATOR_INVALID"
            ),
            target_results=results,
            audit={
                "schema_version": DOSSIER_ORCHESTRATOR_SCHEMA_VERSION,
                "as_of_date": config.as_of_date,
                "canonical_archetype": config.canonical_archetype,
                "target_count": len(targets),
                "question_family_count_per_target": len(families),
                "critical_counts": critical,
                "critical_count_sum": sum(critical.values()),
            },
        )

    def _initialize_target(
        self,
        *,
        config: DossierRunConfig,
        target: DossierTarget,
        families: Sequence[Mapping[str, Any]],
    ) -> Mapping[str, Any]:
        output_root = Path(config.output_root)
        root = (
            output_root
            if len(families) and output_root.name == target.target_id
            else output_root / target.target_id
        )
        root.mkdir(parents=True, exist_ok=True)
        plan_id = _id(
            "DPLAN",
            {
                "target_id": target.target_id,
                "as_of_date": config.as_of_date,
                "archetype": config.canonical_archetype,
            },
        )
        plan = {
            "schema_version": DOSSIER_ORCHESTRATOR_SCHEMA_VERSION,
            "plan_id": plan_id,
            "target_id": target.target_id,
            "company_name": target.company_name,
            "as_of_date": config.as_of_date,
            "canonical_archetype": config.canonical_archetype,
            "planner_role": "QUESTION_FAMILY_TO_QUERY_INTENT",
            "query_generation_authority": "RESEARCH_BRAIN_LLM",
            "deterministic_query_template_used": False,
            "max_research_iterations": config.max_research_iterations,
            "max_code_repair_iterations": config.max_code_repair_iterations,
            "materialize_live_input": config.materialize_live_input,
            "live_materialization_authorized": config.live_materialization_authorized,
            "hard_requirements": {
                "organic_claim": config.require_organic_claim,
                "calibrated_component_score": config.require_calibrated_component_score,
                "full_score_valid": config.require_full_score_valid,
            },
        }
        tasks = tuple(
            _question_task(
                plan_id=plan_id,
                target=target,
                as_of_date=config.as_of_date,
                archetype=config.canonical_archetype,
                family=family,
            )
            for family in families
        )
        closures = tuple(
            {
                "schema_version": DOSSIER_ORCHESTRATOR_SCHEMA_VERSION,
                "target_id": target.target_id,
                "question_family_id": task["question_family_id"],
                "source_task_id": task["source_task_id"],
                "status": "PROVIDER_PENDING",
                "failure_class": "RESEARCH_NOT_EXECUTED",
                "supporting_claim_ids": [],
                "counter_claim_ids": [],
                "search_exhaustion_proof": [],
                "next_action": "LLM_GENERATE_CONTEXTUAL_QUERY",
            }
            for task in tasks
        )
        iteration = {
            "schema_version": DOSSIER_ORCHESTRATOR_SCHEMA_VERSION,
            "iteration": 0,
            "target_id": target.target_id,
            "failure_class": "RESEARCH_NOT_EXECUTED",
            "before_metrics": {
                "organic_accepted_claim_count": 0,
                "validated_impact_count": 0,
                "verified_supported_score": 0.0,
                "full_score_valid": False,
            },
            "repair": "initialize bounded question-family investigation",
            "after_metrics": {
                "question_family_count": len(families),
                "bounded_source_task_count": len(tasks),
            },
            "status": "DOSSIER_ORCHESTRATOR_INITIALIZED",
        }
        _write_jsonl(root / "research_brain_plans.jsonl", (plan,))
        _write_jsonl(root / "question_source_tasks.jsonl", tasks)
        _write_jsonl(root / "question_closure.jsonl", closures)
        _write_jsonl(root / "dossier_iterations.jsonl", (iteration,))
        audit = {
            "schema_version": DOSSIER_ORCHESTRATOR_SCHEMA_VERSION,
            "status": "DOSSIER_RESEARCH_PENDING",
            "target_id": target.target_id,
            "company_name": target.company_name,
            "as_of_date": config.as_of_date,
            "canonical_archetype": config.canonical_archetype,
            "question_family_count": len(families),
            "bounded_source_task_count": len(tasks),
            "organic_accepted_claim_count": 0,
            "validated_impact_count": 0,
            "verified_supported_score": 0.0,
            "full_score_valid": False,
            "score_type": "NO_SCORE",
            "readiness_eligible": False,
            "critical_counts": {
                "organic_claim_missing": int(config.require_organic_claim),
                "calibrated_component_score_missing": int(
                    config.require_calibrated_component_score
                ),
                "full_score_invalid": int(config.require_full_score_valid),
            },
            "critical_count_sum": sum(
                (
                    config.require_organic_claim,
                    config.require_calibrated_component_score,
                    config.require_full_score_valid,
                )
            ),
        }
        _write_json(root / "audit_summary.json", audit)
        return {
            "target_id": target.target_id,
            "output_root": str(root),
            "question_family_count": len(families),
            "source_task_count": len(tasks),
            "unbounded_task_count": sum(
                not _bounded_task(task) for task in tasks
            ),
            "nonterminal_missing_status_count": sum(
                closure["status"] not in TERMINAL_QUESTION_STATUSES
                for closure in closures
            ),
            "status": "DOSSIER_RESEARCH_PENDING",
        }


def _question_task(
    *,
    plan_id: str,
    target: DossierTarget,
    as_of_date: str,
    archetype: str,
    family: Mapping[str, Any],
) -> Mapping[str, Any]:
    family_id = str(family["question_family_id"])
    payload = {
        "plan_id": plan_id,
        "target_id": target.target_id,
        "question_family_id": family_id,
    }
    return {
        "schema_version": DOSSIER_ORCHESTRATOR_SCHEMA_VERSION,
        "source_task_id": _id("DST", payload),
        "plan_id": plan_id,
        "target_id": target.target_id,
        "company_name": target.company_name,
        "as_of_date": as_of_date,
        "canonical_archetype": archetype,
        "question_family_id": family_id,
        "question_to_answer": str(family["question_to_answer"]),
        "primitive_ids": list(family.get("primitive_ids") or ()),
        "evidence_roles": list(family.get("evidence_roles") or ()),
        "counter_thesis": bool(family.get("counter_thesis")),
        "query_generation_authority": "RESEARCH_BRAIN_LLM",
        "suggested_queries": [],
        "executed_queries": [],
        "source_priority": list(family.get("source_priority") or ()),
        "budget": {
            "max_queries": int(family["budget"]["max_queries"]),
            "max_candidates": int(family["budget"]["max_candidates"]),
            "max_fetches": int(family["budget"]["max_fetches"]),
        },
        "stop_condition": str(family["stop_condition"]),
        "production_execution_allowed": True,
        "test_only": False,
    }


def _validate_question_family_catalog(payload: Mapping[str, Any]) -> None:
    if _literal_query_count(payload):
        raise ValueError("question family recipe must not contain literal search queries")
    archetypes = payload.get("archetypes")
    if not isinstance(archetypes, Mapping) or not archetypes:
        raise ValueError("question family catalog requires archetypes")
    for archetype_id, row in archetypes.items():
        if not str(archetype_id).strip() or not isinstance(row, Mapping):
            raise ValueError("invalid archetype question family row")
        families = tuple(row.get("question_families") or ())
        family_ids = [str(family.get("question_family_id") or "") for family in families]
        if not families or len(family_ids) != len(set(family_ids)) or not all(family_ids):
            raise ValueError("question families must be non-empty and unique")
        for family in families:
            if not str(family.get("question_to_answer") or "").strip():
                raise ValueError("question family requires a semantic question")
            if not family.get("primitive_ids") or not family.get("evidence_roles"):
                raise ValueError("question family requires primitive and evidence roles")
            if not _bounded_task({"budget": family.get("budget"), "stop_condition": family.get("stop_condition")}):
                raise ValueError("question family requires bounded budgets and stop condition")


def _literal_query_count(value: Any) -> int:
    if isinstance(value, Mapping):
        return sum(
            int(str(key).lower() in {"query", "queries", "suggested_queries"})
            + _literal_query_count(item)
            for key, item in value.items()
        )
    if isinstance(value, (list, tuple)):
        return sum(_literal_query_count(item) for item in value)
    return 0


def _bounded_task(task: Mapping[str, Any]) -> bool:
    budget = task.get("budget")
    return bool(
        isinstance(budget, Mapping)
        and 0 < int(budget.get("max_queries") or 0) <= 10
        and 0 < int(budget.get("max_candidates") or 0) <= 100
        and 0 < int(budget.get("max_fetches") or 0) <= 20
        and str(task.get("stop_condition") or "").strip()
    )


def _id(prefix: str, payload: Mapping[str, Any]) -> str:
    encoded = json.dumps(
        payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return f"{prefix}-{hashlib.sha256(encoded).hexdigest()[:24]}"


def _write_json(path: Path, payload: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def _write_jsonl(path: Path, rows: Sequence[Mapping[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "".join(
            json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows
        ),
        encoding="utf-8",
    )


__all__ = [
    "DOSSIER_ORCHESTRATOR_SCHEMA_VERSION",
    "DossierInitializationResult",
    "DossierRunConfig",
    "DossierTarget",
    "FullThesisDossierOrchestrator",
    "TERMINAL_QUESTION_STATUSES",
    "load_question_family_catalog",
]
