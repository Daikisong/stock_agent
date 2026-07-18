"""Phase 94 current Researcher Mode checkpoint orchestration.

This module owns the production lane only.  It never imports or reads the
private Phase 93 Gold corpus.  Post-run Gold comparison is deliberately left
to the CLI after every target production artifact has been closed.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
import hashlib
import json
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.metadata import stable_hash, write_json, write_jsonl
from e2r.research_brain.runtime.scoring_contracts import (
    load_archetype_scoring_contract,
)

from .component_anchor_atlas import compile_component_anchor_atlas_from_files
from .canary_leaf_contract import materialize_canary_checkpoint_leaves
from .component_research_planner import ComponentResearchPlanner
from .component_researcher import CodexResearcherProvider, StructuredResearchProvider
from .component_scoring_memos import (
    ComponentScoringMemoRun,
    LLMComponentScoringMemoEngine,
    write_component_scoring_memo_run,
)
from .dossier import CanonicalResearchDossierBuilder, ResearcherModeDossier
from .evidence_fact_extractor import (
    FACT_EXTRACTION_OUTPUT_FILES,
    ResearcherEvidenceFactExtractor,
    ResearcherFactExtractionResult,
    production_material_fact_rows,
    write_researcher_fact_extraction_result,
)
from .official_source_materializer import (
    OFFICIAL_SOURCE_OUTPUT_FILES,
    CurrentOfficialSourceMaterializer,
    OfficialSourceMaterializationResult,
    write_official_source_materialization,
)
from .current_structured_materializer import (
    FACT_STRUCTURED_ROLE_RESOLUTION_CONTRACTS,
    CurrentStructuredMaterializationResult,
    CurrentStructuredSourceMaterializer,
)
from .research_epoch import (
    ResearchEpochRun,
    ResearchEpochRunner,
    load_research_epoch_checkpoint,
    write_research_epoch_run,
)
from .research_supervisor import ResearchSupervisor
from .saturation import SATURATION_REVIEW_ROLES, SemanticSaturationReviewer
from .schemas import CANONICAL_COMPONENT_ORDER, EvidenceDirection
from .score_aggregator import (
    DeterministicScoreAggregationRun,
    DeterministicScoreAggregator,
    write_deterministic_score_aggregation_run,
)
from .stagecourt import (
    ResearcherStageCourt,
    ResearcherStageCourtRun,
    write_researcher_stagecourt_run,
)
from .source_graph_explorer import (
    ResearcherSourceGraphAcquirer,
    SourceGraphAcquisitionConfig,
    SourceGraphAcquisitionRun,
    SourceGraphExplorer,
    load_source_graph_checkpoint,
    write_source_graph_acquisition_run,
)
from .structured_data_researcher import StructuredMetricRecord
from .structured_financial_engine import (
    PHASE86_COMPONENT_ROLE_COMPATIBILITY,
    PHASE86_REQUIRED_ROLES_BY_COMPONENT,
    StructuredEngineResult,
    StructuredFinancialConsensusValuationEngine,
    StructuredSourcePayload,
    write_structured_financial_outputs,
)
from .structured_source_routes import (
    InMemoryStructuredSourceRoute,
    UnavailableStructuredSourceRoute,
)


CURRENT_RESEARCHER_MODE_SCHEMA_VERSION = "e2r_v5_current_researcher_mode_v1"


@dataclass(frozen=True)
class CurrentResearchTarget:
    symbol: str
    company_name: str
    aliases: tuple[str, ...] = ()
    official_domains: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.symbol.strip() or not self.company_name.strip():
            raise ValueError("current research target identity is incomplete")

    @property
    def target_id(self) -> str:
        return self.symbol


@dataclass(frozen=True)
class CurrentResearcherModeConfig:
    as_of_date: str
    archetype_id: str
    output_root: str | Path
    live_materialization_authorized: bool
    checkpoint_resume: bool
    gold_lane_isolated: bool
    require_researcher_parity: bool
    latest_trading_snapshot_date: str | None = None
    schema_version: str = CURRENT_RESEARCHER_MODE_SCHEMA_VERSION

    def __post_init__(self) -> None:
        cutoff = date.fromisoformat(self.as_of_date)
        if not self.archetype_id.strip():
            raise ValueError("Researcher Mode archetype is required")
        if not self.live_materialization_authorized:
            raise ValueError("Phase 94 requires explicit live materialization authorization")
        if not self.checkpoint_resume:
            raise ValueError("Phase 94 requires checkpoint resume")
        if not self.gold_lane_isolated:
            raise ValueError("Phase 94 production requires Gold lane isolation")
        if not self.require_researcher_parity:
            raise ValueError("Phase 94 requires Researcher parity gates")
        if self.latest_trading_snapshot_date:
            trading_date = date.fromisoformat(self.latest_trading_snapshot_date)
            if trading_date > cutoff:
                raise ValueError("latest trading snapshot cannot be after as_of_date")


@dataclass(frozen=True)
class CurrentResearcherTargetRun:
    target: CurrentResearchTarget
    status: str
    output_root: Path
    official_sources: OfficialSourceMaterializationResult
    source_graph: SourceGraphAcquisitionRun
    fact_extraction: ResearcherFactExtractionResult
    structured_materialization: CurrentStructuredMaterializationResult
    structured_result: StructuredEngineResult
    dossier: ResearcherModeDossier
    scoring_memos: ComponentScoringMemoRun
    score_aggregation: DeterministicScoreAggregationRun
    stagecourt: ResearcherStageCourtRun
    research_epoch: ResearchEpochRun
    component_memo_rows: tuple[Mapping[str, Any], ...]
    production_input_rows: tuple[Mapping[str, Any], ...]
    completion_gates: Mapping[str, Any]
    audit: Mapping[str, Any]


class CurrentResearcherModeTargetRunner:
    """Run one semantic checkpoint for one target without fixed-round completion."""

    def __init__(
        self,
        *,
        provider: StructuredResearchProvider | None = None,
        official_materializer: CurrentOfficialSourceMaterializer | None = None,
        structured_materializer: CurrentStructuredSourceMaterializer | None = None,
        source_acquirer: ResearcherSourceGraphAcquirer | None = None,
        fact_extractor: ResearcherEvidenceFactExtractor | None = None,
    ) -> None:
        effective_provider = provider or CodexResearcherProvider.default(
            working_directory=Path.cwd(), timeout_seconds=300
        )
        self.provider = effective_provider
        self.official_materializer = (
            official_materializer or CurrentOfficialSourceMaterializer()
        )
        self.structured_materializer = (
            structured_materializer
            or CurrentStructuredSourceMaterializer(peer_provider=effective_provider)
        )
        self.source_acquirer = source_acquirer or ResearcherSourceGraphAcquirer(
            query_provider=effective_provider
        )
        self.fact_extractor = fact_extractor or ResearcherEvidenceFactExtractor(
            provider=effective_provider
        )

    def run_checkpoint(
        self,
        *,
        config: CurrentResearcherModeConfig,
        target: CurrentResearchTarget,
        repo_root: str | Path = ".",
    ) -> CurrentResearcherTargetRun:
        root = Path(config.output_root) / target.symbol
        root.mkdir(parents=True, exist_ok=True)
        _configure_provider_response_cache(self.provider, root)
        anchors = _historical_anchors(
            repo_root=repo_root,
            archetype_id=config.archetype_id,
        )
        initial_plans = ComponentResearchPlanner().plan(
            target_id=target.target_id,
            archetype_id=config.archetype_id,
            evidence_facts=(),
            historical_anchors=anchors,
        )
        initial_graph = SourceGraphExplorer().explore(
            target_id=target.target_id,
            as_of_date=config.as_of_date,
            documents=(),
            research_plans=initial_plans,
            source_coverage=(),
        )
        objective_rows = tuple(row.to_dict() for row in initial_graph.open_objectives)
        official = _load_official_checkpoint(root, config=config, target=target)
        if official is None:
            official = self.official_materializer.materialize(
                target_id=target.target_id,
                target_name=target.company_name,
                as_of_date=config.as_of_date,
                objective_ids=tuple(row.objective_id for row in initial_graph.open_objectives),
                live_materialization_authorized=(
                    config.live_materialization_authorized
                ),
                repo_root=repo_root,
            )
            write_official_source_materialization(official, root)
        prior_source_checkpoint = None
        source_checkpoint_path = root / "source_graph_checkpoint.json"
        if config.checkpoint_resume and source_checkpoint_path.is_file():
            prior_source_checkpoint = load_source_graph_checkpoint(
                source_checkpoint_path
            )
        prior_context = _load_prior_research_context(
            root,
            target_id=target.target_id,
            as_of_date=config.as_of_date,
            objectives=objective_rows,
        )
        source_coverage = tuple(
            sorted(
                {
                    str(row.get("source_family") or "")
                    for row in official.evidence_documents
                    if row.get("source_family")
                }
            )
        )
        official_gaps = {
            row.objective_id: tuple(official.pending_reasons)
            or ("official sources fetched; unresolved semantic facts require discovery",)
            for row in initial_graph.open_objectives
        }
        source_graph = self.source_acquirer.acquire(
            config=SourceGraphAcquisitionConfig(
                mode="RESEARCH_BACKFILL",
                max_results_per_query=100,
                max_queries_per_checkpoint=10,
                max_candidates_per_checkpoint=100,
                max_fetches_per_checkpoint=20,
            ),
            target_id=target.target_id,
            target_name=target.company_name,
            target_aliases=target.aliases,
            as_of_date=config.as_of_date,
            open_objectives=initial_graph.open_objectives,
            current_evidence_facts=prior_context["facts"],
            target_business_model=prior_context["business_model"],
            source_coverage=source_coverage,
            official_documents=official.evidence_documents,
            official_gap_reasons_by_objective=official_gaps,
            theme_context={"archetype_hypothesis": config.archetype_id},
            score_gap_context={
                "official_source_status": official.status,
                "official_pending_reasons": list(official.pending_reasons),
                "completion_policy": "semantic saturation, never transport count",
                "verified_official_domain_allowlist": list(
                    target.official_domains
                ),
                "prior_fact_extraction_feedback": list(
                    prior_context["research_gap_feedback"]
                ),
                "prior_structured_source_gap": dict(
                    prior_context["structured_gap_context"]
                ),
                "prior_deterministic_score_gap": dict(
                    prior_context["score_gap_context"]
                ),
                "prior_supervisor_gap": dict(
                    prior_context["supervisor_gap_context"]
                ),
                "prior_research_epoch": prior_context["research_epoch"],
            },
            resolved_objective_ids=prior_context["resolved_objective_ids"],
            prior_checkpoint=prior_source_checkpoint,
            official_domain_allowlist=target.official_domains,
        )
        write_source_graph_acquisition_run(source_graph, output_root=root)
        prior_fact = _load_fact_checkpoint(root, source_graph=source_graph)
        fact_extraction = self.fact_extractor.extract(
            target_id=target.target_id,
            target_name=target.company_name,
            target_aliases=target.aliases,
            archetype_id=config.archetype_id,
            as_of_date=config.as_of_date,
            documents=source_graph.evidence_documents,
            open_objectives=objective_rows,
            current_facts=prior_context["facts"],
            score_gap_context={
                "source_graph_status": source_graph.status,
                "source_graph_pending_reasons": list(
                    source_graph.checkpoint.get("pending_reasons") or ()
                ),
                "prior_fact_extraction_feedback": list(
                    prior_context["research_gap_feedback"]
                ),
                "prior_structured_source_gap": dict(
                    prior_context["structured_gap_context"]
                ),
                "prior_deterministic_score_gap": dict(
                    prior_context["score_gap_context"]
                ),
                "prior_supervisor_gap": dict(
                    prior_context["supervisor_gap_context"]
                ),
            },
            **prior_fact,
        )
        write_researcher_fact_extraction_result(fact_extraction, root)
        write_jsonl(
            root / "counterfacts.jsonl",
            (
                row.to_dict()
                for row in fact_extraction.facts
                if row.direction == EvidenceDirection.COUNTER.value
            ),
        )
        required_structured_roles = {
            plan.component_id: tuple(
                dict.fromkeys(
                    (
                        *PHASE86_REQUIRED_ROLES_BY_COMPONENT.get(
                            plan.component_id, ()
                        ),
                        *plan.structured_metric_requirements,
                    )
                )
            )
            for plan in initial_plans
        }
        structured_materialization = self.structured_materializer.materialize(
            target_id=target.target_id,
            target_name=target.company_name,
            as_of_date=config.as_of_date,
            latest_trading_snapshot_date=(
                config.latest_trading_snapshot_date or config.as_of_date
            ),
            official=official,
            output_root=root,
            checkpoint_resume=config.checkpoint_resume,
            evidence_facts=fact_extraction.facts,
            source_claims=fact_extraction.material_claims,
            source_documents=source_graph.evidence_documents,
            required_roles_by_component=required_structured_roles,
            shared_cache_roots=_same_lane_structured_cache_roots(
                Path(config.output_root),
                target_id=target.target_id,
                as_of_date=config.as_of_date,
            ),
        )
        structured = structured_materialization.engine_result
        write_structured_financial_outputs(structured, root)
        write_json(root / "structured_engine_result.json", structured.to_dict())
        research_source_coverage = tuple(
            sorted(
                {
                    *(
                        str(row.get("source_family") or "")
                        for row in source_graph.evidence_documents
                        if row.get("source_family")
                    ),
                    *(
                        str(row.source_route)
                        for row in structured.records
                        if str(row.source_route).strip()
                    ),
                    *(
                        str(row.route_name)
                        for row in structured.source_attempts
                        if row.accepted_record_count > 0
                    ),
                }
            )
        )
        prior_component_memos = (
            _load_prior_component_memos(
                root=root,
                target_id=target.target_id,
                archetype_id=config.archetype_id,
                as_of_date=config.as_of_date,
            )
            if config.checkpoint_resume
            else {}
        )
        dossier = CanonicalResearchDossierBuilder(provider=self.provider).build(
            target_id=target.target_id,
            archetype_id=config.archetype_id,
            as_of_date=config.as_of_date,
            evidence_facts=fact_extraction.facts,
            historical_anchors=anchors,
            source_claims=fact_extraction.material_claims,
            source_documents=source_graph.evidence_documents,
            source_coverage=research_source_coverage,
            structured_engine_result=structured,
            prior_component_memos_by_component=prior_component_memos,
            prior_supervisor_feedback_by_component=(
                _component_supervisor_feedback_by_component(
                    prior_context["supervisor_gap_context"]
                )
            ),
        )
        _write_dossier(root, dossier)
        scoring_memos = LLMComponentScoringMemoEngine(
            analyst_provider=self.provider
        ).build(
            target_id=target.target_id,
            archetype_id=config.archetype_id,
            as_of_date=config.as_of_date,
            component_results=dossier.component_results,
            evidence_facts=fact_extraction.facts,
            historical_anchors=anchors,
        )
        write_component_scoring_memo_run(scoring_memos, root)
        write_jsonl(
            root / "judge_decisions.jsonl",
            (row.to_dict() for row in scoring_memos.judge_decisions),
        )
        write_jsonl(
            root / "anchor_comparisons.jsonl",
            (
                {
                    "judge_id": row.judge_id,
                    "component_id": row.component_id,
                    "anchor_comparisons": list(row.anchor_comparisons),
                    "nearest_anchor_ids": list(row.nearest_anchor_ids),
                    "prompt_hash": row.prompt_hash,
                    "response_hash": row.response_hash,
                }
                for row in scoring_memos.judge_decisions
            ),
        )
        component_memos = tuple(
            row.memo for row in dossier.component_results if row.memo is not None
        )
        aggregation = DeterministicScoreAggregator().aggregate_run(
            scoring_memo_run=scoring_memos,
            component_research_memos=component_memos,
            evidence_facts=fact_extraction.facts,
            historical_anchors=anchors,
        )
        write_deterministic_score_aggregation_run(aggregation, root)
        write_jsonl(
            root / "component_decisions.jsonl",
            (row.to_dict() for row in aggregation.component_results),
        )
        write_json(root / "total_score.json", aggregation.total_result.to_dict())
        prior_epoch = None
        epoch_path = root / "research_epoch_checkpoint.json"
        if config.checkpoint_resume and epoch_path.is_file():
            prior_epoch = load_research_epoch_checkpoint(epoch_path)
        counter_route_proof = tuple(
            row
            for row in source_graph.checkpoint.get("generated_queries") or ()
            if row.get("counter_or_supersession_search")
            and row.get("execution_status") == "SEARCH_EXECUTED"
        )
        epoch = ResearchEpochRunner(
            supervisor=ResearchSupervisor(provider=self.provider),
            saturation_reviewers=tuple(
                SemanticSaturationReviewer(
                    reviewer_role=role,
                    provider=self.provider,
                )
                for role in SATURATION_REVIEW_ROLES
            ),
        ).run_epoch(
            target_id=target.target_id,
            as_of_date=config.as_of_date,
            component_results=dossier.component_results,
            red_team_result=dossier.red_team_result,
            structured_result=structured,
            evidence_facts=fact_extraction.facts,
            source_graph_checkpoint=source_graph.checkpoint,
            open_objectives=objective_rows,
            # ResearchSupervisor collects every query/provider/document failure
            # from this same Source Graph checkpoint.  Passing query_failures a
            # second time creates duplicate semantic failures with new ids.
            prior_failures=(),
            counter_and_supersession_route_proof=counter_route_proof,
            prior_checkpoint=prior_epoch,
            # Gold is private during production.  One means "not yet verified",
            # not an observed miss.  The post-run evaluator may replace it with
            # the real count only after production has closed.
            gold_critical_fact_miss_count=1,
        )
        write_research_epoch_run(epoch, root)
        provider_cache_audit = _provider_response_cache_audit(self.provider)
        if provider_cache_audit is not None:
            write_json(
                root / "research_provider_response_cache_audit.json",
                provider_cache_audit,
            )
        component_memo_rows = _production_component_memo_rows(
            target=target,
            dossier=dossier,
        )
        input_rows = _production_input_rows(
            target=target,
            source_graph=source_graph,
        )
        research_gates = _completion_gates(
            source_graph=source_graph,
            fact_extraction=fact_extraction,
            dossier=dossier,
            structured=structured,
            aggregation=aggregation,
            epoch=epoch,
        )
        research_complete_for_stagecourt = all(
            bool(value) for value in research_gates.values()
        )
        stagecourt_run = ResearcherStageCourt(provider=self.provider).decide(
            target_id=target.target_id,
            archetype_id=config.archetype_id,
            as_of_date=config.as_of_date,
            score_aggregation=aggregation,
            material_claims=fact_extraction.material_claims,
            claim_fact_links=tuple(
                row.to_dict()
                for row in fact_extraction.fact_compilation.claim_fact_links
            ),
            source_documents=source_graph.evidence_documents,
            structured_records=structured.records,
            research_complete=research_complete_for_stagecourt,
            counter_thesis_complete=bool(
                research_gates["counter_thesis_complete"]
            ),
        )
        write_researcher_stagecourt_run(stagecourt_run, root)
        # Preserve the old handoff filename for readers while the Phase 95
        # atomic decision and trace are now the canonical Stage authority.
        write_json(root / "stagecourt.json", stagecourt_run.decision.to_dict())
        gates = {
            **research_gates,
            "deterministic_stagecourt_final": (
                stagecourt_run.decision.status == "FINAL"
            ),
        }
        production_complete_before_leaf_contract = all(
            bool(value) for value in gates.values()
        )
        leaf_contract = materialize_canary_checkpoint_leaves(
            root,
            target_id=target.target_id,
            as_of_date=config.as_of_date,
            production_research_complete=production_complete_before_leaf_contract,
        )
        gates = {
            **gates,
            "master_canary_leaf_contract": (
                int(leaf_contract["critical_count_sum"]) == 0
            ),
        }
        production_complete = all(bool(value) for value in gates.values())
        status = (
            "PRODUCTION_RESEARCH_COMPLETE_PENDING_POST_RUN_GOLD"
            if production_complete
            else "RESEARCH_CHECKPOINT_PENDING"
        )
        audit = {
            "schema_version": CURRENT_RESEARCHER_MODE_SCHEMA_VERSION,
            "status": status,
            "target_id": target.target_id,
            "as_of_date": config.as_of_date,
            "gold_visibility": False,
            "gold_comparison_timing": "POST_RUN_ONLY",
            "completion_based_on_fixed_rounds": False,
            "zero_search_result_treated_as_completion": False,
            "transport_budget_treated_as_completion": False,
            "component_memo_count": len(component_memos),
            "fact_count": len(fact_extraction.facts),
            "counterfact_count": sum(
                row.direction == EvidenceDirection.COUNTER.value
                for row in fact_extraction.facts
            ),
            "document_count": len(source_graph.evidence_documents),
            "query_count": len(
                source_graph.checkpoint.get("generated_queries") or ()
            ),
            "structured_fetch_attempt_count": len(
                structured_materialization.fetch_attempts
            ),
            "structured_pending_reasons": list(
                structured_materialization.pending_reasons
            ),
            "provider_response_cache": (
                {
                    key: provider_cache_audit.get(key)
                    for key in (
                        "status",
                        "logical_call_count",
                        "successful_call_count",
                        "transport_call_count",
                        "cache_hit_count",
                        "provider_error_count",
                        "provider_usage_limit_detected",
                        "provider_usage_limit_reset_hints",
                        "provider_usage_limit_transport_error_count",
                        "provider_usage_limit_short_circuit_count",
                        "prompt_transport_rejected_count",
                        "cache_invalid_or_unreadable_count",
                        "downstream_semantic_invalidation_count",
                        "downstream_semantic_cache_delete_count",
                        "downstream_semantic_cache_delete_failure_count",
                    )
                }
                if provider_cache_audit is not None
                else {"status": "PROVIDER_CACHE_INTERFACE_UNAVAILABLE"}
            ),
            "canary_leaf_contract": {
                "status": leaf_contract["status"],
                "critical_count_sum": leaf_contract["critical_count_sum"],
                "audit_path": "canary_leaf_contract_audit.json",
            },
            "completion_gates": dict(gates),
            "production_research_complete": production_complete,
        }
        write_json(root / "current_researcher_mode_audit.json", audit)
        write_json(
            root / "target_run_manifest.json",
            {
                **audit,
                "company_name": target.company_name,
                "aliases": list(target.aliases),
                "archetype_id": config.archetype_id,
                "latest_trading_snapshot_date": config.latest_trading_snapshot_date,
                "output_tree_hash": _tree_hash(root),
            },
        )
        return CurrentResearcherTargetRun(
            target=target,
            status=status,
            output_root=root,
            official_sources=official,
            source_graph=source_graph,
            fact_extraction=fact_extraction,
            structured_materialization=structured_materialization,
            structured_result=structured,
            dossier=dossier,
            scoring_memos=scoring_memos,
            score_aggregation=aggregation,
            stagecourt=stagecourt_run,
            research_epoch=epoch,
            component_memo_rows=component_memo_rows,
            production_input_rows=input_rows,
            completion_gates=gates,
            audit=audit,
        )


def write_production_lane(
    *,
    config: CurrentResearcherModeConfig,
    target_runs: Sequence[CurrentResearcherTargetRun],
) -> Mapping[str, Path]:
    root = Path(config.output_root)
    facts = tuple(
        row
        for run in target_runs
        for row in production_material_fact_rows(run.fact_extraction)
    )
    memos = tuple(row for run in target_runs for row in run.component_memo_rows)
    inputs = tuple(row for run in target_runs for row in run.production_input_rows)
    complete = bool(
        target_runs
        and all(
            run.status == "PRODUCTION_RESEARCH_COMPLETE_PENDING_POST_RUN_GOLD"
            for run in target_runs
        )
    )
    lane = {
        "schema_version": "e2r_v5_phase94_production_lane_v1",
        "as_of_date": config.as_of_date,
        "archetype_id": config.archetype_id,
        "target_ids": [run.target.target_id for run in target_runs],
        "gold_visibility": False,
        "gold_query_visibility": False,
        "gold_url_visibility": False,
        "gold_fact_visibility": False,
        "comparison_timing": "POST_RUN_ONLY",
        "production_research_complete": complete,
        "completion_based_on_fixed_rounds": False,
        "latest_trading_snapshot_date": config.latest_trading_snapshot_date,
    }
    paths = {
        "facts": root / "production_material_facts.jsonl",
        "memos": root / "production_component_memos.jsonl",
        "inputs": root / "production_input_manifest.jsonl",
        "lane": root / "production_lane_manifest.json",
    }
    write_jsonl(paths["facts"], facts)
    write_jsonl(paths["memos"], memos)
    write_jsonl(paths["inputs"], inputs)
    write_json(paths["lane"], lane)
    return paths


def load_current_research_targets(
    *,
    symbols: Sequence[str],
    registry_path: str | Path = "configs/e2r_targeted_live_smoke_v1.json",
    as_of_date: str | date | None = None,
    official_domain_registry_path: str | Path = (
        "configs/e2r_issuer_official_domains_v1.json"
    ),
) -> tuple[CurrentResearchTarget, ...]:
    payload = _read_json(Path(registry_path))
    rows = payload.get("mandatory_targets") or payload.get("targets") or ()
    by_symbol = {
        str(row.get("symbol") or row.get("target_id") or ""): row
        for row in rows
        if isinstance(row, Mapping)
    }
    missing = [symbol for symbol in symbols if symbol not in by_symbol]
    if missing:
        raise ValueError(
            "target registry does not contain symbols: " + ",".join(missing)
        )
    cutoff = (
        as_of_date
        if isinstance(as_of_date, date)
        else date.fromisoformat(as_of_date)
        if as_of_date is not None
        else None
    )
    verified_domains = (
        _verified_official_domains_by_symbol(
            path=Path(official_domain_registry_path),
            symbols=symbols,
            as_of_date=cutoff,
        )
        if cutoff is not None
        else {}
    )
    return tuple(
        CurrentResearchTarget(
            symbol=symbol,
            company_name=str(by_symbol[symbol]["company_name"]),
            aliases=tuple(by_symbol[symbol].get("aliases") or ()),
            official_domains=tuple(
                dict.fromkeys(
                    (
                        *by_symbol[symbol].get("official_domains", ()),
                        *verified_domains.get(symbol, ()),
                    )
                )
            ),
        )
        for symbol in symbols
    )


def _verified_official_domains_by_symbol(
    *,
    path: Path,
    symbols: Sequence[str],
    as_of_date: date,
) -> Mapping[str, tuple[str, ...]]:
    """Load only issuer-domain authorities that were valid by the cutoff."""

    if not path.is_file():
        return {}
    payload = _read_json(path)
    entries = payload.get("entries") or ()
    if not isinstance(entries, Sequence) or isinstance(entries, (str, bytes)):
        raise ValueError(f"official domain registry entries must be an array: {path}")
    requested = {str(symbol).zfill(6) for symbol in symbols}
    domains: dict[str, list[str]] = {symbol: [] for symbol in requested}
    for entry in entries:
        if not isinstance(entry, Mapping):
            continue
        symbol = str(entry.get("symbol") or "").zfill(6)
        if symbol not in requested:
            continue
        if str(entry.get("status") or "ACTIVE").strip().upper() != "ACTIVE":
            continue
        valid_from = _registry_date(entry.get("valid_from"))
        verified_as_of = _registry_date(entry.get("verified_as_of"))
        valid_to = _registry_date(entry.get("valid_to"))
        if valid_from is None or verified_as_of is None:
            continue
        if valid_from > as_of_date or verified_as_of > as_of_date:
            continue
        if valid_to is not None and valid_to < as_of_date:
            continue
        host = str(entry.get("host") or "").strip().casefold()
        host = host.removeprefix("https://").removeprefix("http://")
        host = host.split("/", 1)[0].split(":", 1)[0].removeprefix("www.")
        source_url = str(entry.get("source_url") or "").strip()
        source_anchor = str(entry.get("source_anchor_text") or "").strip()
        if not host or not source_url.startswith("https://") or not source_anchor:
            continue
        domains[symbol].append(host)
    return {
        symbol: tuple(dict.fromkeys(values))
        for symbol, values in domains.items()
        if values
    }


def _registry_date(value: Any) -> date | None:
    if value in (None, ""):
        return None
    try:
        return date.fromisoformat(str(value)[:10])
    except ValueError:
        return None


def _historical_anchors(
    *, repo_root: str | Path, archetype_id: str
) -> tuple[Mapping[str, Any], ...]:
    atlas_path = Path(repo_root) / "docs/operational/e2r_v5_component_anchor_atlas.json"
    if atlas_path.is_file():
        payload = _read_json(atlas_path)
    else:
        payload = compile_component_anchor_atlas_from_files(
            atlas_root=Path(repo_root) / "output/researcher_parity/judgment_atlas"
        )
    all_anchors = tuple(payload.get("component_anchors") or ())
    anchors = list(
        row
        for row in all_anchors
        if str(row.get("archetype_id") or "") == archetype_id
        and not row.get("company_name_conditioned")
        and not row.get("target_symbol_conditioned")
    )
    covered = {str(row.get("component_id") or "") for row in anchors}
    missing = set(CANONICAL_COMPONENT_ORDER) - covered
    if missing:
        maxima = load_archetype_scoring_contract(
            archetype_id
        ).component_max_points
        for component_id in CANONICAL_COMPONENT_ORDER:
            if component_id not in missing:
                continue
            candidates = tuple(
                row
                for row in all_anchors
                if str(row.get("component_id") or "") == component_id
                and row.get("usable_as_ordinal_anchor") is True
                and not row.get("company_name_conditioned")
                and not row.get("target_symbol_conditioned")
                and float(row.get("max_points") or 0) > 0
            )
            representatives = []
            for role in ("POSITIVE", "COUNTER"):
                role_rows = sorted(
                    (row for row in candidates if row.get("role") == role),
                    key=lambda row: (
                        float(row["points_mid"]) / float(row["max_points"]),
                        str(row["anchor_id"]),
                    ),
                )
                if not role_rows:
                    continue
                for index in dict.fromkeys(
                    (0, len(role_rows) // 2, len(role_rows) - 1)
                ):
                    representatives.append(role_rows[index])
            target_maximum = float(maxima[component_id])
            anchors.extend(
                _normalized_ordinal_transfer_anchor(
                    row,
                    archetype_id=archetype_id,
                    target_maximum=target_maximum,
                )
                for row in representatives
            )
    final_covered = {str(row.get("component_id") or "") for row in anchors}
    if final_covered != set(CANONICAL_COMPONENT_ORDER):
        raise ValueError("historical anchor atlas lacks seven-component ordinal coverage")
    return tuple(anchors)


def _normalized_ordinal_transfer_anchor(
    row: Mapping[str, Any],
    *,
    archetype_id: str,
    target_maximum: float,
) -> Mapping[str, Any]:
    source_maximum = float(row["max_points"])
    scale = target_maximum / source_maximum
    source_anchor_id = str(row["anchor_id"])
    return {
        "schema_version": "e2r_component_anchor_v1",
        "anchor_id": "ORDTRANSFER-" + stable_hash(
            {
                "source_anchor_id": source_anchor_id,
                "target_archetype_id": archetype_id,
                "target_maximum": target_maximum,
            }
        )[:24],
        "archetype_id": archetype_id,
        "component_id": str(row["component_id"]),
        "economic_fact_patterns": list(row.get("economic_fact_patterns") or ()),
        "role": str(row["role"]),
        "score_band": str(row["score_band"]),
        "points_lower": round(float(row["points_lower"]) * scale, 6),
        "points_mid": round(float(row["points_mid"]) * scale, 6),
        "points_upper": round(float(row["points_upper"]) * scale, 6),
        "max_points": target_maximum,
        "source_backed_case_ids": [],
        "source_proxy_guard_case_ids": list(
            dict.fromkeys(
                (
                    *(row.get("source_backed_case_ids") or ()),
                    *(row.get("source_proxy_guard_case_ids") or ()),
                    source_anchor_id,
                )
            )
        ),
        "source_score_anchor_ids": list(
            dict.fromkeys(row.get("source_score_anchor_ids") or ())
        ),
        "confidence": "LOW",
        "usable_as_exact_anchor": False,
        "usable_as_ordinal_anchor": True,
        "company_name_conditioned": False,
        "target_symbol_conditioned": False,
        "ordinal_transfer_only": True,
        "source_archetype_id": str(row.get("archetype_id") or ""),
        "source_anchor_id": source_anchor_id,
    }


def _structured_result_from_official(
    *,
    target: CurrentResearchTarget,
    as_of_date: str,
    official: OfficialSourceMaterializationResult,
) -> StructuredEngineResult:
    records: list[StructuredMetricRecord] = []
    source_ids: list[str] = []
    for row in official.structured_payloads:
        if str(row.get("provider_name") or "") != "CompanyGuide":
            continue
        payload = row.get("payload") or {}
        if not isinstance(payload, Mapping):
            continue
        observed = str(
            payload.get("CONSENSUS_AS_OF_DATE")
            or row.get("published_at")
            or as_of_date
        ).replace("/", "-")[:10]
        source_id = "SRC-COMPANYGUIDE-" + str(
            row.get("provider_content_hash") or stable_hash(row)
        )[:24]
        source_ids.append(source_id)
        specs = (
            ("forward_eps", payload.get("EPS"), "KRW/share", ("FORWARD_EPS", "CONSENSUS_HISTORY"), "VALUATION"),
            ("forward_pe", payload.get("FORWARD_PER"), "x", ("FORWARD_PE",), "VALUATION"),
            ("consensus_target_price", payload.get("TARGET_PRC"), "KRW/share", ("CONSENSUS_TARGET_PRICE",), "CONSENSUS_REVISION"),
            ("consensus_provider_count", payload.get("CONSENSUS_PROVIDER_COUNT"), "count", ("CONSENSUS_HISTORY",), "CONSENSUS_REVISION"),
        )
        for metric_id, value, unit, roles, dataset in specs:
            if value in (None, ""):
                continue
            records.append(
                StructuredMetricRecord(
                    record_id="STRUCT-" + stable_hash(
                        {
                            "target_id": target.target_id,
                            "metric_id": metric_id,
                            "value": value,
                            "observed": observed,
                            "source_id": source_id,
                        }
                    )[:24],
                    target_id=target.target_id,
                    as_of_date=as_of_date,
                    metric_id=metric_id,
                    value=float(value),
                    unit=unit,
                    period=f"FORWARD_AS_OF_{observed}",
                    evidence_roles=roles,
                    source_ids=(source_id,),
                    source_route="COMPANYGUIDE",
                    observed_at=observed,
                    available_at=observed,
                    record_kind="STRUCTURED_CONSENSUS_SNAPSHOT",
                    confidence=0.9,
                    dataset=dataset,
                    provenance="STRUCTURED_EXTRACTED",
                    metadata={
                        "provider_name": "CompanyGuide",
                        "canonical_url": row.get("canonical_url"),
                        "snippet_only": False,
                    },
                )
            )
    payload = StructuredSourcePayload(
        route_name="COMPANYGUIDE",
        source_ids=tuple(dict.fromkeys(source_ids)) if records else (),
        structured_records=tuple(records),
        diagnostics={"source": "official live CompanyGuide parsed payload"},
    )
    routes = (
        InMemoryStructuredSourceRoute("COMPANYGUIDE", payload),
        UnavailableStructuredSourceRoute("PUBLIC_BROKER_REPORT"),
        UnavailableStructuredSourceRoute("ISSUER_GUIDANCE"),
        UnavailableStructuredSourceRoute("DART_ACTUALS_DETERMINISTIC_SCENARIO"),
        UnavailableStructuredSourceRoute("KRX_PRICE_MARKET_CAP"),
    )
    return StructuredFinancialConsensusValuationEngine().research(
        target_id=target.target_id,
        symbol=target.symbol,
        company_name=target.company_name,
        as_of_date=as_of_date,
        routes=routes,
        deep_researched_canary=True,
    )


def _write_dossier(root: Path, dossier: ResearcherModeDossier) -> None:
    write_json(root / "researcher_mode_dossier.json", dossier.to_dict())
    write_json(
        root / "business_model_memo.json",
        dossier.business_model_result.memo.to_dict()
        if dossier.business_model_result.memo
        else dossier.business_model_result.to_dict(),
    )
    write_jsonl(
        root / "component_research_memos.jsonl",
        (
            row.memo.to_dict()
            if row.memo
            else {
                "component_id": row.component_id,
                "research_status": "RESEARCH_PENDING",
                "pending_reasons": list(row.pending_reasons),
            }
            for row in dossier.component_results
        ),
    )
    write_json(
        root / "red_team_research.json",
        dossier.red_team_result.to_dict()
        if dossier.red_team_result
        else {"status": "PENDING", "reason": "seven component memos incomplete"},
    )


def _production_component_memo_rows(
    *, target: CurrentResearchTarget, dossier: ResearcherModeDossier
) -> tuple[Mapping[str, Any], ...]:
    by_component = {row.component_id: row for row in dossier.component_results}
    rows = []
    for component_id in CANONICAL_COMPONENT_ORDER:
        result = by_component.get(component_id)
        memo = result.memo if result else None
        rows.append(
            {
                "schema_version": "e2r_v5_production_component_memo_v1",
                "target_id": target.target_id,
                "component_id": component_id,
                "research_status": (
                    "RESEARCH_COMPLETE"
                    if result and result.status == "COMPLETE" and memo
                    else "RESEARCH_PENDING"
                ),
                "memo_id": memo.memo_id if memo else None,
                "positive_fact_ids": list(memo.positive_fact_ids) if memo else [],
                "counter_fact_ids": list(memo.counter_fact_ids) if memo else [],
                "why_not_higher": memo.why_not_higher if memo else None,
                "why_not_lower": memo.why_not_lower if memo else None,
                "pending_reasons": list(result.pending_reasons) if result else ["COMPONENT_RESULT_MISSING"],
                "gold_visibility": False,
            }
        )
    return tuple(rows)


def _production_input_rows(
    *, target: CurrentResearchTarget, source_graph: SourceGraphAcquisitionRun
) -> tuple[Mapping[str, Any], ...]:
    rows: list[Mapping[str, Any]] = []
    for query in source_graph.checkpoint.get("generated_queries") or ():
        rows.append(
            {
                "input_id": str(query["query_id"]),
                "target_id": target.target_id,
                "input_type": "QUERY",
                "origin": "PRODUCTION_LLM_QUERY",
                "value": str(query["literal_query"]),
                "path": "",
            }
        )
    for document in source_graph.evidence_documents:
        rows.append(
            {
                "input_id": str(document["document_id"]),
                "target_id": target.target_id,
                "input_type": "DISCOVERED_SOURCE_DOCUMENT",
                "origin": "PRODUCTION_OFFICIAL_OR_LLM_DISCOVERY",
                "value": str(document.get("canonical_url") or ""),
                "path": "",
            }
        )
    return tuple(rows)


def _completion_gates(
    *,
    source_graph: SourceGraphAcquisitionRun,
    fact_extraction: ResearcherFactExtractionResult,
    dossier: ResearcherModeDossier,
    structured: StructuredEngineResult,
    aggregation: DeterministicScoreAggregationRun,
    epoch: ResearchEpochRun,
) -> Mapping[str, bool]:
    complete_results = tuple(
        row
        for row in dossier.component_results
        if row.status == "COMPLETE" and row.memo and row.memo.research_complete
    )
    counter_complete = bool(
        dossier.red_team_result
        and dossier.red_team_result.status == "COMPLETE"
        and dossier.red_team_result.memo
        and not dossier.red_team_result.memo.unresolved_challenges
    )
    no_disagreement = all(
        not row.material_disagreement for row in aggregation.component_results
    )
    return {
        "source_graph_checkpoint_ready": (
            source_graph.status
            in {"EPOCH_COMPLETE_REQUIRES_SUPERVISOR", "STOPPED_ON_RESOLUTION"}
            and int(source_graph.audit.get("critical_count_sum") or 0) == 0
        ),
        "fact_extraction_complete": (
            fact_extraction.status == "FACT_EXTRACTION_COMPLETE"
            and int(fact_extraction.audit.get("critical_count_sum") or 0) == 0
        ),
        "seven_component_research_complete": (
            len(complete_results) == len(CANONICAL_COMPONENT_ORDER)
        ),
        "counter_thesis_complete": counter_complete,
        "structured_valuation_revision_complete": structured.status == "COMPLETE",
        "no_unresolved_material_judge_disagreement": no_disagreement,
        "deterministic_total_score_complete": aggregation.score_valid,
        "production_semantic_supervisor_ready": (
            epoch.supervisor_review.ready_for_independent_saturation_review
        ),
    }


def _load_official_checkpoint(
    root: Path,
    *,
    config: CurrentResearcherModeConfig,
    target: CurrentResearchTarget,
) -> OfficialSourceMaterializationResult | None:
    paths = {key: root / value for key, value in OFFICIAL_SOURCE_OUTPUT_FILES.items()}
    if not config.checkpoint_resume or not all(path.is_file() for path in paths.values()):
        return None
    result = _read_json(paths["result"])
    audit = _read_json(paths["audit"])
    if (
        str(result.get("target_id") or "") != target.target_id
        or str(result.get("as_of_date") or "") != config.as_of_date
        or int(audit.get("critical_count_sum") or 0) != 0
    ):
        return None
    documents = _read_jsonl(paths["documents"])
    for row in documents:
        content = str(row.get("content_text") or "")
        if hashlib.sha256(content.encode("utf-8")).hexdigest() != row.get("content_hash"):
            return None
    return OfficialSourceMaterializationResult(
        target_id=target.target_id,
        as_of_date=config.as_of_date,
        status=str(result["status"]),
        evidence_documents=documents,
        provider_attempts=_read_jsonl(paths["attempts"]),
        structured_payloads=_read_jsonl(paths["structured_payloads"]),
        pending_reasons=tuple(result.get("pending_reasons") or ()),
        audit=audit,
    )


def _same_lane_structured_cache_roots(
    lane_root: Path,
    *,
    target_id: str,
    as_of_date: str,
) -> tuple[Path, ...]:
    """Return only target-bound caches from the same dated production lane."""

    if not lane_root.is_dir():
        return ()
    roots: list[Path] = []
    for child in sorted(lane_root.iterdir()):
        if not child.is_dir() or child.name == target_id:
            continue
        cache_root = child / "structured_source_cache"
        manifest_path = child / "target_run_manifest.json"
        if not manifest_path.is_file():
            continue
        try:
            manifest = _read_json(manifest_path)
        except (OSError, UnicodeError, ValueError, json.JSONDecodeError):
            continue
        if (
            not cache_root.is_dir()
            or str(manifest.get("target_id") or "") != child.name
            or str(manifest.get("as_of_date") or "") != as_of_date
        ):
            continue
        roots.append(cache_root)
    return tuple(roots)


def _load_fact_checkpoint(
    root: Path, *, source_graph: SourceGraphAcquisitionRun
) -> Mapping[str, Any]:
    paths = {key: root / value for key, value in FACT_EXTRACTION_OUTPUT_FILES.items()}
    required = (
        paths["accepted_claims"],
        paths["document_dispositions"],
        paths["provider_calls"],
        paths["rejections"],
    )
    if not all(path.is_file() for path in required):
        return {}
    current_ids = {
        str(row.get("document_id") or "") for row in source_graph.evidence_documents
    }
    all_calls = _read_jsonl(paths["provider_calls"])
    completed_call_ids = {
        str(document_id)
        for row in all_calls
        if row.get("status") == "COMPLETE"
        for document_id in row.get("document_ids") or ()
        if str(document_id) in current_ids
    }
    persisted_dispositions = _read_jsonl(paths["document_dispositions"])
    completed_ids = completed_call_ids & {
        str(row.get("document_id") or "")
        for row in persisted_dispositions
        if str(row.get("document_id") or "") in current_ids
    }
    dispositions = tuple(
        row
        for row in persisted_dispositions
        if str(row.get("document_id") or "") in completed_ids
    )
    claims = tuple(
        row
        for row in _read_jsonl(paths["accepted_claims"])
        if str(row.get("document_id") or "") in completed_ids
    )
    calls = tuple(
        row
        for row in all_calls
        if row.get("status") == "COMPLETE"
        and set(row.get("document_ids") or ()).issubset(completed_ids)
    )
    rejections = tuple(
        row
        for row in _read_jsonl(paths["rejections"])
        if str(row.get("document_id") or "") in completed_ids
    )
    return {
        "prior_material_claims": claims,
        "prior_document_dispositions": dispositions,
        "prior_provider_calls": calls,
        "prior_rejections": rejections,
    }


def _load_prior_research_context(
    root: Path,
    *,
    target_id: str,
    as_of_date: str,
    objectives: Sequence[Mapping[str, Any]],
) -> Mapping[str, Any]:
    facts = tuple(
        row
        for row in _read_jsonl(root / "evidence_facts.jsonl")
        if str(row.get("target_id") or "") == target_id
        and str(row.get("as_of_date") or "") == as_of_date
    )
    business_model = None
    business_path = root / "business_model_memo.json"
    if business_path.is_file():
        candidate = _read_json(business_path)
        if (
            str(candidate.get("target_id") or "") == target_id
            and str(candidate.get("as_of_date") or "") == as_of_date
            and candidate.get("research_complete") is True
        ):
            business_model = candidate
    feedback = ()
    extraction_path = root / "fact_extraction_result.json"
    if extraction_path.is_file():
        extraction = _read_json(extraction_path)
        if (
            str(extraction.get("target_id") or "") == target_id
            and str(extraction.get("as_of_date") or "") == as_of_date
        ):
            feedback = tuple(
                dict.fromkeys(
                    (
                        *(extraction.get("research_gap_feedback") or ()),
                        *(
                            f"FACT_EXTRACTION_RETRY_CONTEXT:{reason}"
                            for reason in extraction.get("pending_reasons") or ()
                        ),
                    )
                )
            )
    complete_components = {
        str(row.get("component_id") or "")
        for row in _read_jsonl(root / "component_research_memos.jsonl")
        if row.get("research_complete") is True
    }
    structured_gap_context: Mapping[str, Any] = {}
    structured_missing_components: set[str] = set()
    structured_path = root / "structured_engine_result.json"
    materialization_path = root / "current_structured_materialization.json"
    materialization_audit_path = (
        root / "current_structured_materialization_audit.json"
    )
    if structured_path.is_file():
        structured = _read_json(structured_path)
        if (
            str(structured.get("target_id") or "") == target_id
            and str(structured.get("as_of_date") or "") == as_of_date
        ):
            missing_by_component = {
                str(component_id): tuple(
                    str(role)
                    for role in roles or ()
                    if str(role).strip()
                )
                for component_id, roles in (
                    structured.get("missing_roles_by_component") or {}
                ).items()
                if isinstance(roles, (list, tuple))
            }
            structured_missing_components = {
                component_id
                for component_id, roles in missing_by_component.items()
                if roles
            }
            materialization = (
                _read_json(materialization_path)
                if materialization_path.is_file()
                else {}
            )
            materialization_audit = (
                _read_json(materialization_audit_path)
                if materialization_audit_path.is_file()
                else {}
            )
            structured_gap_context = {
                "status": structured.get("status"),
                "missing_roles_by_component": {
                    component_id: list(roles)
                    for component_id, roles in missing_by_component.items()
                    if roles
                },
                "missing_role_resolution_contracts": (
                    _structured_gap_resolution_contracts(
                        missing_by_component
                    )
                ),
                "covered_roles_by_component": structured.get(
                    "covered_roles_by_component"
                )
                or {},
                "component_disposition_by_component": structured.get(
                    "component_disposition_by_component"
                )
                or {},
                "pending_reasons": list(
                    materialization.get("pending_reasons") or ()
                ),
                "issuer_fact_materialization": (
                    materialization_audit.get("issuer_fact_materialization")
                    or {}
                ),
                "query_generation_owner": "LLM",
                "deterministic_fallback_query_allowed": False,
            }
    score_gap_context: Mapping[str, Any] = {}
    score_unresolved_components: set[str] = set()
    score_path = root / "deterministic_score_aggregation_run.json"
    if score_path.is_file():
        score = _read_json(score_path)
        if (
            str(score.get("target_id") or "") == target_id
            and str(score.get("as_of_date") or "") == as_of_date
            and score.get("score_valid") is not True
        ):
            # Older checkpoints copied this run-level conjunction into every
            # component.  It is diagnostic, not a component-specific research
            # gap, so only requests with an additional actionable reason reopen
            # that component.
            run_only_reasons = {"COMPONENT_SCORING_MEMO_RUN_NOT_READY"}
            actionable_requests: list[Mapping[str, Any]] = []
            for candidate in score.get("research_requests") or ():
                if not isinstance(candidate, Mapping):
                    continue
                reason_codes = tuple(
                    str(reason)
                    for reason in candidate.get("reason_codes") or ()
                    if str(reason).strip()
                )
                component_id = str(candidate.get("component_id") or "")
                if (
                    component_id in CANONICAL_COMPONENT_ORDER
                    and any(reason not in run_only_reasons for reason in reason_codes)
                ):
                    score_unresolved_components.add(component_id)
                    actionable_requests.append(dict(candidate))
            for candidate in score.get("component_results") or ():
                if not isinstance(candidate, Mapping):
                    continue
                component_id = str(candidate.get("component_id") or "")
                pending_reasons = tuple(
                    str(reason)
                    for reason in candidate.get("pending_reasons") or ()
                    if str(reason).strip()
                )
                if (
                    component_id in CANONICAL_COMPONENT_ORDER
                    and candidate.get("status") != "COMPLETE"
                    and any(
                        reason not in run_only_reasons
                        for reason in pending_reasons
                    )
                ):
                    score_unresolved_components.add(component_id)
            score_gap_context = {
                "status": score.get("status"),
                "score_valid": False,
                "pending_reasons": list(score.get("pending_reasons") or ()),
                "component_research_requests": actionable_requests,
                "unresolved_component_ids": sorted(
                    score_unresolved_components
                ),
                "next_query_generation_authority": "LLM_RESEARCH_SUPERVISOR",
                "deterministic_query_synthesis": False,
            }
    epoch_context = None
    supervisor_gap_context: Mapping[str, Any] = {}
    supervisor_unresolved_components: set[str] = set()
    supervisor_unresolved_objectives: set[str] = set()
    epoch_path = root / "research_epoch_checkpoint.json"
    if epoch_path.is_file():
        epoch = _read_json(epoch_path)
        epoch_context = {
            "checkpoint_id": epoch.get("checkpoint_id"),
            "epoch": epoch.get("epoch"),
            "status": epoch.get("status"),
            "unresolved_material_questions": epoch.get(
                "unresolved_material_questions"
            ),
            "next_actions": epoch.get("next_actions"),
        }
        supervisor = epoch.get("supervisor_review") or {}
        if isinstance(supervisor, Mapping):
            supervisor_gap_context = {
                key: supervisor.get(key)
                for key in (
                    "review_id",
                    "epoch",
                    "status",
                    "component_status",
                    "component_findings",
                    "unresolved_material_questions",
                    "missing_material_facts",
                    "failure_assessments",
                    "new_source_family_directions",
                    "query_direction_briefs",
                    "source_family_gaps",
                    "parser_or_extractor_failures",
                    "next_actions",
                    "counter_and_supersession_checked",
                    "structured_data_complete",
                    "component_memos_sufficient",
                    "reasonable_positive_routes_remaining",
                )
                if key in supervisor
            }
            component_status = supervisor.get("component_status") or {}
            if isinstance(component_status, Mapping):
                supervisor_unresolved_components.update(
                    str(component_id)
                    for component_id, status in component_status.items()
                    if str(component_id) in CANONICAL_COMPONENT_ORDER
                    and str(status) != "COMPLETE"
                )
            for finding in supervisor.get("component_findings") or ():
                if not isinstance(finding, Mapping):
                    continue
                component_id = str(finding.get("component_id") or "")
                if (
                    component_id in CANONICAL_COMPONENT_ORDER
                    and finding.get("memo_sufficient") is False
                ):
                    supervisor_unresolved_components.add(component_id)
            for gap in supervisor.get("missing_material_facts") or ():
                if isinstance(gap, Mapping):
                    component_id = str(gap.get("component_id") or "")
                    if component_id in CANONICAL_COMPONENT_ORDER:
                        supervisor_unresolved_components.add(component_id)
            for key in (
                "new_source_family_directions",
                "query_direction_briefs",
            ):
                for direction in supervisor.get(key) or ():
                    if isinstance(direction, Mapping):
                        objective_id = str(direction.get("objective_id") or "")
                        if objective_id:
                            supervisor_unresolved_objectives.add(objective_id)
    resolved_objective_ids = tuple(
        str(row["objective_id"])
        for row in objectives
        if str(row.get("component_id") or "") in complete_components
        and str(row.get("component_id") or "")
        not in structured_missing_components
        and str(row.get("component_id") or "")
        not in score_unresolved_components
        and str(row.get("component_id") or "")
        not in supervisor_unresolved_components
        and str(row.get("objective_id") or "")
        not in supervisor_unresolved_objectives
    )
    return {
        "facts": facts,
        "business_model": business_model,
        "research_gap_feedback": feedback,
        "structured_gap_context": structured_gap_context,
        "score_gap_context": score_gap_context,
        "supervisor_gap_context": supervisor_gap_context,
        "resolved_objective_ids": resolved_objective_ids,
        "research_epoch": epoch_context,
    }


def _component_supervisor_feedback_by_component(
    context: Mapping[str, Any] | None,
) -> Mapping[str, Mapping[str, Any]]:
    """Route only actionable supervisor feedback to its component rewrite.

    Search/extraction receives the complete supervisor context, but a component
    researcher should see only findings and material-fact gaps assigned to its
    own memo.  This keeps the rewrite prompt bounded and prevents an unrelated
    component's thesis from leaking across the canonical research lanes.
    """

    if not context:
        return {}
    if not isinstance(context, Mapping):
        raise TypeError("supervisor gap context must be an object")
    component_status = context.get("component_status") or {}
    if not isinstance(component_status, Mapping):
        raise TypeError("supervisor component_status must be an object")
    findings_by_component: dict[str, list[Mapping[str, Any]]] = {}
    for finding in context.get("component_findings") or ():
        if not isinstance(finding, Mapping):
            continue
        component_id = str(finding.get("component_id") or "")
        if component_id in CANONICAL_COMPONENT_ORDER:
            findings_by_component.setdefault(component_id, []).append(
                dict(finding)
            )
    gaps_by_component: dict[str, list[Mapping[str, Any]]] = {}
    for gap in context.get("missing_material_facts") or ():
        if not isinstance(gap, Mapping):
            continue
        component_id = str(gap.get("component_id") or "")
        if component_id in CANONICAL_COMPONENT_ORDER:
            gaps_by_component.setdefault(component_id, []).append(dict(gap))

    # ``review_id`` and ``epoch`` are checkpoint lineage, not semantic rewrite
    # instructions.  Including them here forces a fresh provider prompt on
    # every resumed epoch even when the component finding and missing-fact
    # roster are unchanged.  The complete values remain persisted in the
    # supervisor checkpoint; the component provider receives only the stable
    # semantic status so an exact prior response can be reused safely.
    shared: dict[str, Any] = {}
    if "status" in context:
        shared["status"] = context.get("status")
    result: dict[str, Mapping[str, Any]] = {}
    for component_id in CANONICAL_COMPONENT_ORDER:
        status = component_status.get(component_id)
        findings = [
            finding
            for finding in findings_by_component.get(component_id, [])
            if finding.get("memo_sufficient") is False
            or str(status or "COMPLETE") != "COMPLETE"
        ]
        gaps = gaps_by_component.get(component_id, [])
        if str(status or "COMPLETE") == "COMPLETE" and not findings and not gaps:
            continue
        result[component_id] = {
            **shared,
            "component_id": component_id,
            "component_status": status,
            "component_findings": findings,
            "missing_material_facts": gaps,
        }
    return result


def _structured_gap_resolution_contracts(
    missing_roles_by_component: Mapping[str, Sequence[str]],
) -> Mapping[str, Mapping[str, Mapping[str, Any]]]:
    """Project deterministic role eligibility without synthesizing a query."""

    result: dict[str, dict[str, Mapping[str, Any]]] = {}
    for component_id, requirements in missing_roles_by_component.items():
        component_contracts: dict[str, Mapping[str, Any]] = {}
        for requirement in requirements:
            accepted_roles = tuple(
                dict.fromkeys(
                    (
                        str(requirement),
                        *PHASE86_COMPONENT_ROLE_COMPATIBILITY.get(
                            str(requirement), ()
                        ),
                    )
                )
            )
            fact_contracts = {
                role: dict(FACT_STRUCTURED_ROLE_RESOLUTION_CONTRACTS[role])
                for role in accepted_roles
                if role in FACT_STRUCTURED_ROLE_RESOLUTION_CONTRACTS
            }
            component_contracts[str(requirement)] = {
                "accepted_engine_evidence_roles": list(accepted_roles),
                "llm_fact_extractable_roles": list(fact_contracts),
                "fact_materialization_contracts": fact_contracts,
                "semantically_adjacent_ineligible_evidence_closes_gap": False,
                "literal_query_generation_owner": "LLM",
                "deterministic_fallback_query_allowed": False,
            }
        if component_contracts:
            result[str(component_id)] = component_contracts
    return result


def _tree_hash(root: Path) -> str:
    return stable_hash(
        [
            {
                "path": str(path.relative_to(root)),
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            }
            for path in sorted(root.rglob("*"))
            if path.is_file() and path.name != "target_run_manifest.json"
        ]
    )


def _configure_provider_response_cache(
    provider: StructuredResearchProvider,
    root: Path,
) -> None:
    configure = getattr(provider, "configure_response_cache", None)
    if callable(configure):
        configure(root / "research_provider_response_cache")


def _provider_response_cache_audit(
    provider: StructuredResearchProvider,
) -> Mapping[str, Any] | None:
    audit = getattr(provider, "response_cache_audit", None)
    if not callable(audit):
        return None
    value = audit()
    if not isinstance(value, Mapping):
        raise TypeError("provider response cache audit must be an object")
    return dict(value)


def _read_json(path: Path) -> Mapping[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, Mapping):
        raise ValueError(f"JSON object required: {path}")
    return value


def _read_jsonl(path: Path) -> tuple[Mapping[str, Any], ...]:
    if not path.is_file():
        return ()
    return tuple(
        value
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
        for value in (json.loads(line),)
        if isinstance(value, Mapping)
    )


def _load_prior_component_memos(
    *,
    root: Path,
    target_id: str,
    archetype_id: str,
    as_of_date: str,
) -> Mapping[str, Mapping[str, Any]]:
    """Load hash-bound checkpoint memos as non-authoritative continuity context.

    A provider outage may overwrite the convenience JSONL with pending rows.
    The append-only research epoch ledger still contains the prior memo bodies;
    only bodies whose stable hash equals the active checkpoint hash are eligible
    for recovery.
    """

    result: dict[str, Mapping[str, Any]] = {}
    checkpoint_hashes: dict[str, str] = {}
    checkpoint_path = root / "research_epoch_checkpoint.json"
    if checkpoint_path.is_file():
        checkpoint = _read_json(checkpoint_path)
        if (
            str(checkpoint.get("target_id") or "") == target_id
            and str(checkpoint.get("as_of_date") or "") == as_of_date
        ):
            checkpoint_hashes = {
                str(component_id): str(memo_hash)
                for component_id, memo_hash in (
                    checkpoint.get("component_memo_hashes") or {}
                ).items()
                if str(component_id) in CANONICAL_COMPONENT_ORDER
                and len(str(memo_hash)) == 64
            }

    def accept(row: Mapping[str, Any]) -> None:
        component_id = str(row.get("component_id") or "")
        if (
            component_id not in CANONICAL_COMPONENT_ORDER
            or str(row.get("target_id") or "") != target_id
            or str(row.get("archetype_id") or "") != archetype_id
            or not str(row.get("researcher_role") or "").strip()
            or not isinstance(row.get("positive_fact_ids"), list)
            or not isinstance(row.get("counter_fact_ids"), list)
            or not isinstance(row.get("resolution_fact_ids"), list)
            or not isinstance(row.get("context_fact_ids", []), list)
        ):
            return
        expected_hash = checkpoint_hashes.get(component_id)
        if expected_hash and stable_hash(row) != expected_hash:
            return
        result[component_id] = row

    for epoch in _read_jsonl(root / "research_epochs.jsonl"):
        if (
            str(epoch.get("target_id") or "") != target_id
            or str(epoch.get("as_of_date") or "") != as_of_date
        ):
            continue
        changed_memos = epoch.get("changed_component_memos") or ()
        if isinstance(changed_memos, list):
            for row in changed_memos:
                if isinstance(row, Mapping):
                    accept(row)
    for row in _read_jsonl(root / "component_research_memos.jsonl"):
        accept(row)
    return result


__all__ = [
    "CURRENT_RESEARCHER_MODE_SCHEMA_VERSION",
    "CurrentResearchTarget",
    "CurrentResearcherModeConfig",
    "CurrentResearcherModeTargetRunner",
    "CurrentResearcherTargetRun",
    "load_current_research_targets",
    "write_production_lane",
]
