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
from e2r.research_brain.intelligence_schema import stable_intelligence_id
from e2r.research_brain.runtime.scoring_contracts import (
    load_archetype_scoring_contract,
)

from .component_anchor_atlas import compile_component_anchor_atlas_from_files
from .canary_leaf_contract import (
    canary_output_tree_hash,
    materialize_canary_checkpoint_leaves,
)
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
    fact_extraction_has_exact_checkpoint_recovery_wait,
    normalize_punctuation_only_fact_value,
    production_material_fact_rows,
    rematerialize_claim_source_provenance,
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
from .research_supervisor import (
    ResearchSupervisor,
    build_counter_and_supersession_route_proof,
)
from .saturation import (
    GOLD_EVALUATION_NOT_RUN_POST_RUN_ONLY,
    SATURATION_REVIEW_ROLES,
    SemanticSaturationReviewer,
)
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
    SourceGraphAcquisitionMode,
    SourceGraphAcquisitionRun,
    SourceGraphExplorer,
    load_source_graph_checkpoint,
    source_graph_ranker_customer_official_reclassification_document_ids,
    source_graph_active_navigation_only_document_ids,
    source_graph_acquisition_safety_critical_counts,
    source_graph_checkpoint_audit_binding,
    validate_source_graph_checkpoint,
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
    source_acquisition_mode: str = SourceGraphAcquisitionMode.PRODUCTION_DAILY.value
    schema_version: str = CURRENT_RESEARCHER_MODE_SCHEMA_VERSION

    def __post_init__(self) -> None:
        cutoff = date.fromisoformat(self.as_of_date)
        source_mode = SourceGraphAcquisitionMode(self.source_acquisition_mode)
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
        if source_mode == SourceGraphAcquisitionMode.RESEARCH_BACKFILL:
            raise ValueError(
                "Phase 94 current Researcher Mode cannot run with backfill source semantics"
            )
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
            provider=effective_provider,
            max_document_chars_per_call=int(
                getattr(
                    effective_provider,
                    "semantic_prompt_chunk_chars",
                    getattr(
                        effective_provider,
                        "fact_document_chunk_chars",
                        220_000,
                    ),
                )
            ),
        )

    def run_checkpoint(
        self,
        *,
        config: CurrentResearcherModeConfig,
        target: CurrentResearchTarget,
        repo_root: str | Path = ".",
        source_resume_mode: str = "ADVANCE",
    ) -> CurrentResearcherTargetRun:
        if source_resume_mode not in {
            "ADVANCE",
            "REUSE_READY_CHECKPOINT",
        }:
            raise ValueError("unknown source resume mode")
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
            prior_source_checkpoint = validate_source_graph_checkpoint(
                load_source_graph_checkpoint(source_checkpoint_path),
                target_id=target.target_id,
                as_of_date=config.as_of_date,
            )
        prior_context = _load_prior_research_context(
            root,
            target_id=target.target_id,
            as_of_date=config.as_of_date,
            objectives=objective_rows,
            archetype_id=config.archetype_id,
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
        effective_official_gap_reasons = _official_gap_reasons(official)
        official_gaps = {
            row.objective_id: effective_official_gap_reasons
            for row in initial_graph.open_objectives
        }
        source_acquisition_config = SourceGraphAcquisitionConfig(
            mode=config.source_acquisition_mode,
            max_results_per_query=100,
            max_queries_per_checkpoint=10,
            max_candidates_per_checkpoint=100,
            max_fetches_per_checkpoint=20,
        )
        source_checkpoint_navigation_migration_only = bool(
            source_resume_mode == "REUSE_READY_CHECKPOINT"
            and prior_source_checkpoint is not None
            and source_graph_active_navigation_only_document_ids(
                prior_source_checkpoint
            )
            and (
                _source_checkpoint_has_terminal_source_work(
                    prior_source_checkpoint
                )
                or _source_checkpoint_needs_downstream_provider_recovery(
                    root=root,
                    checkpoint=prior_source_checkpoint,
                    target_id=target.target_id,
                    as_of_date=config.as_of_date,
                )
            )
        )
        source_checkpoint_provenance_migration_only = bool(
            source_resume_mode == "REUSE_READY_CHECKPOINT"
            and prior_source_checkpoint is not None
            and source_graph_ranker_customer_official_reclassification_document_ids(
                prior_source_checkpoint
            )
        )
        source_checkpoint_migration_only = bool(
            source_checkpoint_navigation_migration_only
            or source_checkpoint_provenance_migration_only
        )
        source_checkpoint_readonly_replayed = bool(
            source_resume_mode == "REUSE_READY_CHECKPOINT"
            and prior_source_checkpoint is not None
            and not source_checkpoint_migration_only
            and _source_checkpoint_is_ready_for_readonly_replay(
                prior_source_checkpoint
            )
        )
        source_checkpoint_downstream_recovery_replayed = bool(
            source_resume_mode == "REUSE_READY_CHECKPOINT"
            and prior_source_checkpoint is not None
            and not source_checkpoint_readonly_replayed
            and not source_checkpoint_migration_only
            and _source_checkpoint_needs_downstream_provider_recovery(
                root=root,
                checkpoint=prior_source_checkpoint,
                target_id=target.target_id,
                as_of_date=config.as_of_date,
            )
        )
        source_checkpoint_fact_extraction_recovery_replayed = bool(
            source_resume_mode == "REUSE_READY_CHECKPOINT"
            and prior_source_checkpoint is not None
            and not source_checkpoint_readonly_replayed
            and not source_checkpoint_migration_only
            and not source_checkpoint_downstream_recovery_replayed
            and _source_checkpoint_needs_fact_extraction_recovery(
                root=root,
                checkpoint=prior_source_checkpoint,
                target_id=target.target_id,
                as_of_date=config.as_of_date,
            )
        )
        if (
            source_checkpoint_readonly_replayed
            or source_checkpoint_downstream_recovery_replayed
            or source_checkpoint_fact_extraction_recovery_replayed
        ):
            source_graph = _hydrate_readonly_source_graph_run(
                root=root,
                checkpoint=prior_source_checkpoint,
                open_objectives=initial_graph.open_objectives,
                config=source_acquisition_config,
                allow_pending_downstream_recovery=(
                    source_checkpoint_downstream_recovery_replayed
                ),
                allow_pending_fact_extraction_recovery=(
                    source_checkpoint_fact_extraction_recovery_replayed
                ),
            )
        else:
            source_graph = self.source_acquirer.acquire(
                config=source_acquisition_config,
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
                        prior_context["supervisor_source_gap_context"]
                    ),
                    "prior_research_epoch": prior_context["research_epoch"],
                },
                resolved_objective_ids=prior_context["resolved_objective_ids"],
                prior_checkpoint=prior_source_checkpoint,
                official_domain_allowlist=target.official_domains,
                checkpoint_migration_only=(
                    source_checkpoint_migration_only
                ),
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
                    prior_context["supervisor_source_gap_context"]
                ),
            },
            extraction_mode=(
                "PRODUCTION_OBJECTIVE_LOCAL"
                if config.source_acquisition_mode
                == SourceGraphAcquisitionMode.PRODUCTION_DAILY.value
                else "RESEARCH_BACKFILL"
            ),
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
        objective_component_by_id = {
            str(row.get("objective_id") or ""): str(
                row.get("component_id") or ""
            )
            for row in objective_rows
            if str(row.get("objective_id") or "")
        }
        supervisor_feedback_by_component = (
            _component_supervisor_feedback_by_component(
                prior_context["supervisor_gap_context"],
                objective_component_by_id=objective_component_by_id,
            )
        )
        reusable_prior_component_memos = _reusable_prior_component_memos(
            prior_component_memos=prior_component_memos,
            actionable_feedback_by_component=(
                supervisor_feedback_by_component
            ),
            prior_facts=prior_context["facts"],
            current_facts=fact_extraction.facts,
            prior_fact_snapshot_available=bool(
                prior_context["fact_snapshot_available"]
            ),
            prior_structured_result=prior_context[
                "structured_engine_result"
            ],
            current_structured_result=structured,
            required_roles_by_component=required_structured_roles,
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
            reusable_prior_component_memos_by_component=(
                reusable_prior_component_memos
            ),
            prior_supervisor_feedback_by_component=(
                supervisor_feedback_by_component
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
        counter_route_proof = build_counter_and_supersession_route_proof(
            source_graph_checkpoint=source_graph.checkpoint,
            document_dispositions=fact_extraction.document_dispositions,
            evidence_facts=fact_extraction.facts,
            required_objective_ids=tuple(
                str(row.get("objective_id") or "")
                for row in objective_rows
                if bool(row.get("counter_or_supersession_required", True))
            ),
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
            synthesis_result=dossier.synthesis_result,
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
            score_gap_context=_score_gap_context_for_supervisor(
                aggregation=aggregation,
                scoring_memos=scoring_memos,
                structured_report_candidates=(
                    structured_materialization.report_candidates
                ),
            ),
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
            evidence_facts=fact_extraction.fact_compilation.facts,
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
            "source_checkpoint_readonly_replayed": (
                source_checkpoint_readonly_replayed
                or source_checkpoint_downstream_recovery_replayed
                or source_checkpoint_fact_extraction_recovery_replayed
            ),
            "source_checkpoint_downstream_recovery_replayed": (
                source_checkpoint_downstream_recovery_replayed
            ),
            "source_checkpoint_fact_extraction_recovery_replayed": (
                source_checkpoint_fact_extraction_recovery_replayed
            ),
            "source_checkpoint_navigation_migration_only": (
                source_checkpoint_navigation_migration_only
            ),
            "source_checkpoint_provenance_migration_only": (
                source_checkpoint_provenance_migration_only
            ),
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
    research_provider: Mapping[str, Any] | None = None,
    production_semantics_seal: Mapping[str, Any] | None = None,
) -> Mapping[str, Path]:
    root = Path(config.output_root)
    facts = tuple(
        row
        for run in target_runs
        for row in (
            *production_material_fact_rows(run.fact_extraction),
            *production_structured_material_fact_rows(
                getattr(run, "structured_result", None)
            ),
        )
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
        "lane_role": "PRODUCTION",
        "as_of_date": config.as_of_date,
        "archetype_id": config.archetype_id,
        "target_ids": [run.target.target_id for run in target_runs],
        "target_statuses": {
            run.target.target_id: run.status for run in target_runs
        },
        "gold_visibility": False,
        "gold_query_visibility": False,
        "gold_url_visibility": False,
        "gold_fact_visibility": False,
        "comparison_timing": "POST_RUN_ONLY",
        "production_research_complete": complete,
        "completion_based_on_fixed_rounds": False,
        "latest_trading_snapshot_date": config.latest_trading_snapshot_date,
    }
    if research_provider is not None:
        lane["research_provider"] = dict(research_provider)
    if production_semantics_seal is not None:
        lane["production_semantics_seal"] = dict(
            production_semantics_seal
        )
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


def production_structured_material_fact_rows(
    result: StructuredEngineResult | None,
) -> tuple[Mapping[str, Any], ...]:
    """Project verified structured observations into the blind fact lane.

    Structured records already pass cutoff, source-lineage, value, and
    availability validation before they reach ``StructuredEngineResult``.
    They previously informed component research but disappeared from the
    post-run Gold comparison because the production lane copied only document
    extraction facts.  This projection preserves the observation as a
    non-scoring fact; it does not infer direction, strength, score, or Stage.
    """

    if result is None:
        return ()
    rows: list[Mapping[str, Any]] = []
    for record in result.records:
        if record.target_id != result.target_id:
            raise ValueError(
                "structured production fact crosses target boundaries"
            )
        if record.as_of_date != result.as_of_date:
            raise ValueError(
                "structured production fact has a mismatched cutoff"
            )
        value_text = json.dumps(
            record.value,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        semantic_payload = {
            "target_id": record.target_id,
            "question_family_id": (
                f"STRUCTURED_{record.dataset}_{record.metric_id}"
            ),
            "subject_id": record.target_id,
            "predicate_family": record.metric_id,
            "normalized_object": (
                f"{record.metric_id}={value_text} {record.unit}"
            ),
            "period": record.period,
            "mechanism_scope_id": (
                f"STRUCTURED|{record.dataset}|{record.record_kind}"
            ).upper(),
        }
        rows.append(
            {
                "schema_version": (
                    "e2r_v5_production_structured_material_fact_v1"
                ),
                "fact_id": "SFACT-"
                + stable_hash(
                    {
                        "record_id": record.record_id,
                        **semantic_payload,
                    }
                )[:24],
                **semantic_payload,
                "discovery_origin": "CANONICAL_SOURCE_TASK",
                "source_id": record.source_ids[0],
                "source_ids": list(record.source_ids),
                "source_tier": _structured_production_source_tier(record),
                "temporal_status": "CURRENT",
                "as_of_date": record.as_of_date,
                "materiality": "NONCRITICAL",
                "fact_role": "SUPPORT",
                "economic_mechanism": (
                    "SOURCE_BACKED_STRUCTURED_OBSERVATION"
                ),
                "predicate": record.metric_id,
                "value": record.value,
                "unit": record.unit,
                "confidence": record.confidence,
                "structured_record_id": record.record_id,
                "input_record_ids": list(record.input_record_ids),
                "claim_ids": [],
                "quote_ids": [],
                "source_route": record.source_route,
                "observed_at": record.observed_at,
                "available_at": record.available_at,
                "provenance": record.provenance,
                "score_authority": False,
                "gold_visibility": False,
            }
        )
    fact_ids = [str(row["fact_id"]) for row in rows]
    if len(fact_ids) != len(set(fact_ids)):
        raise ValueError("structured production facts require unique ids")
    return tuple(rows)


def _structured_production_source_tier(
    record: StructuredMetricRecord,
) -> str:
    route = record.source_route.upper()
    if record.dataset in {"CONSENSUS_REVISION", "VALUATION"} or any(
        token in route
        for token in (
            "COMPANYGUIDE",
            "KRX_",
            "PEER",
            "HISTORICAL_BAND",
            "DETERMINISTIC_FORWARD_SCENARIO",
        )
    ):
        return "FINANCIAL_REVISION"
    if "DART" in route:
        return "REGULATORY_OFFICIAL"
    if "ISSUER" in route:
        return "ISSUER_OFFICIAL"
    if "CUSTOMER" in route:
        return "CUSTOMER_OFFICIAL"
    return "TRUSTED_INDEPENDENT"


def load_current_research_targets(
    *,
    symbols: Sequence[str],
    registry_path: str | Path = "configs/e2r_targeted_live_smoke_v1.json",
    as_of_date: str | date | None = None,
    official_domain_registry_path: str | Path = (
        "configs/e2r_issuer_official_domains_v1.json"
    ),
    registry_rows: Sequence[Mapping[str, Any]] | None = None,
) -> tuple[CurrentResearchTarget, ...]:
    rows = (
        tuple(dict(row) for row in registry_rows)
        if registry_rows is not None
        else load_current_research_target_registry(registry_path)
    )
    by_symbol = {
        str(row.get("symbol") or row.get("target_id") or ""): row
        for row in rows
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


def load_current_research_target_registry(
    registry_path: str | Path = "configs/e2r_targeted_live_smoke_v1.json",
) -> tuple[Mapping[str, Any], ...]:
    """Load the canonical effective roster without duplicating fallback logic."""

    path = Path(registry_path)
    payload = _read_json(path)
    raw_rows = payload.get("mandatory_targets") or payload.get("targets") or ()
    if not isinstance(raw_rows, (list, tuple)) or not raw_rows:
        raise ValueError(
            "target registry mandatory_targets or targets must be a "
            "non-empty array"
        )
    rows = tuple(
        dict(row) if isinstance(row, Mapping) else {}
        for row in raw_rows
    )
    target_ids = tuple(
        str(row.get("symbol") or row.get("target_id") or "").strip()
        for row in rows
    )
    if (
        any(not target_id for target_id in target_ids)
        or len(target_ids) != len(set(target_ids))
    ):
        raise ValueError(
            "target registry roster must contain unique target ids"
        )
    return rows


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
    current_component_memo_ids = {
        row.memo.memo_id for row in complete_results if row.memo is not None
    }
    synthesis_memo = (
        dossier.synthesis_result.memo
        if dossier.synthesis_result
        and dossier.synthesis_result.status == "COMPLETE"
        else None
    )
    current_red_team_memo = (
        dossier.red_team_result.memo
        if dossier.red_team_result
        and dossier.red_team_result.status == "COMPLETE"
        else None
    )
    synthesis_complete = bool(
        synthesis_memo
        and synthesis_memo.synthesis_complete
        and synthesis_memo.target_id == dossier.target_id
        and synthesis_memo.archetype_id == dossier.archetype_id
        and current_red_team_memo
        and synthesis_memo.red_team_memo_id
        == current_red_team_memo.memo_id
        and synthesis_memo.red_team_memo_hash
        == stable_hash(current_red_team_memo.to_dict())
        and len(synthesis_memo.component_memo_ids)
        == len(CANONICAL_COMPONENT_ORDER)
        and len(set(synthesis_memo.component_memo_ids))
        == len(CANONICAL_COMPONENT_ORDER)
        and set(synthesis_memo.component_memo_ids)
        == current_component_memo_ids
        and epoch.supervisor_review.synthesis_memo_id
        == synthesis_memo.memo_id
        and epoch.supervisor_review.synthesis_memo_hash
        == stable_hash(synthesis_memo.to_dict())
    )
    counter_complete = bool(
        dossier.red_team_result
        and dossier.red_team_result.status == "COMPLETE"
        and dossier.red_team_result.memo
        and dossier.red_team_result.memo.review_complete
        and set(dossier.red_team_result.memo.reviewed_component_ids)
        == set(CANONICAL_COMPONENT_ORDER)
        and epoch.supervisor_review.counter_and_supersession_checked
        and synthesis_complete
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
        "production_semantic_saturation_certified": (
            _production_semantic_saturation_certified(epoch)
        ),
    }


def _production_semantic_saturation_certified(
    epoch: ResearchEpochRun,
) -> bool:
    checkpoint = getattr(epoch, "checkpoint", None)
    if checkpoint is None:
        return False
    certificate = checkpoint.saturation_certificate
    if (
        checkpoint.status != "SEMANTIC_SATURATION_CERTIFIED"
        or checkpoint.semantic_saturation_certified is not True
        or checkpoint.gold_evaluation_status
        != GOLD_EVALUATION_NOT_RUN_POST_RUN_ONLY
        or checkpoint.gold_critical_fact_miss_count is not None
        or not isinstance(certificate, Mapping)
        or certificate.get("status") != "CERTIFIED"
        or certificate.get("semantic_saturation_certified") is not True
        or certificate.get("checkpoint_id") != checkpoint.checkpoint_id
        or certificate.get("provider_backed_reviews_required") is not True
        or certificate.get("gold_evaluation_status")
        != GOLD_EVALUATION_NOT_RUN_POST_RUN_ONLY
        or certificate.get("gold_critical_fact_miss_count") is not None
    ):
        return False
    reviewer_results = tuple(checkpoint.saturation_reviews)
    roles = tuple(str(row.get("reviewer_role") or "") for row in reviewer_results)
    review_payloads = tuple(
        row.get("review") if isinstance(row.get("review"), Mapping) else {}
        for row in reviewer_results
    )
    review_ids = tuple(
        str(review.get("review_id") or "") for review in review_payloads
    )
    prompt_hashes = tuple(
        str(review.get("prompt_hash") or "") for review in review_payloads
    )
    return bool(
        len(reviewer_results) == len(SATURATION_REVIEW_ROLES)
        and set(roles) == set(SATURATION_REVIEW_ROLES)
        and all(row.get("status") == "COMPLETE" for row in reviewer_results)
        and all(
            review.get("approve") is True
            and review.get("provider_backed") is True
            and review.get("checkpoint_id") == checkpoint.checkpoint_id
            and review.get("reviewer_role") == roles[index]
            and review.get("gold_evaluation_status")
            == GOLD_EVALUATION_NOT_RUN_POST_RUN_ONLY
            and review.get("gold_critical_fact_miss_count") is None
            for index, review in enumerate(review_payloads)
        )
        and all(review_ids)
        and len(set(review_ids)) == len(SATURATION_REVIEW_ROLES)
        and set(review_ids) == set(certificate.get("review_ids") or ())
        and all(prompt_hashes)
        and len(set(prompt_hashes)) == len(SATURATION_REVIEW_ROLES)
        and set(prompt_hashes)
        == set(certificate.get("provider_prompt_hashes") or ())
    )


def _source_checkpoint_is_ready_for_readonly_replay(
    checkpoint: Mapping[str, Any],
) -> bool:
    """Return whether downstream may replay this exact source snapshot.

    A replay is stricter than ordinary source readiness: every persisted query,
    ranking, and fetch route must already be terminal.  This lets a recovered
    provider or output contract retry downstream research without creating a
    query, reference candidate, fetch, or new source epoch.
    """

    if not _source_checkpoint_has_terminal_source_work(checkpoint):
        return False
    if (
        checkpoint.get("mode")
        == SourceGraphAcquisitionMode.PRODUCTION_DAILY.value
        and "production_downstream_document_ids" not in checkpoint
    ):
        # A legacy production checkpoint may contain backfill-era fetched
        # documents that never passed a current requested-source-family
        # decision.  Force one acquisition migration to persist the exact
        # downstream document roster before readonly replay is allowed.
        return False
    if source_graph_active_navigation_only_document_ids(checkpoint):
        # A ready legacy checkpoint can still contain a fetched search/listing
        # page.  Route it through one bounded migration ADVANCE so source
        # acquisition can preserve lineage and retire derived facts without
        # creating a query, candidate, fetch, or source document.
        return False
    return True


def _source_checkpoint_has_terminal_source_work(
    checkpoint: Mapping[str, Any],
) -> bool:
    """Return whether persisted query/ranking/fetch work is terminal."""

    if str(checkpoint.get("status") or "") not in {
        "EPOCH_COMPLETE_REQUIRES_SUPERVISOR",
        "STOPPED_ON_RESOLUTION",
    }:
        return False
    return _source_checkpoint_has_drained_persisted_work(checkpoint)


def _source_checkpoint_has_drained_persisted_work(
    checkpoint: Mapping[str, Any],
) -> bool:
    """Return whether no persisted query, ranking, or fetch action is pending."""

    if any(
        row.get("execution_status") == "PENDING"
        for row in checkpoint.get("generated_queries") or ()
        if isinstance(row, Mapping)
    ):
        return False
    return not any(
        (
            row.get("ranking_status") == "PENDING"
            or row.get("fetch_status")
            in {"MATERIAL_PENDING_FETCH", "FETCH_RETRY_PENDING"}
        )
        for row in checkpoint.get("search_candidates") or ()
        if isinstance(row, Mapping)
    )


def _source_checkpoint_needs_fact_extraction_recovery(
    *,
    root: Path,
    checkpoint: Mapping[str, Any],
    target_id: str,
    as_of_date: str,
) -> bool:
    """Replay one immutable source snapshot solely to drain pending facts.

    A collaboration wait or canonical-state refresh barrier may be opened
    while unrelated source work is still pending.  The source planner must not
    replace that exact document snapshot before its already-fetched documents
    have drained through fact extraction.  This does not certify Source Graph
    completion: it freezes one exact snapshot solely for the downstream retry.
    """

    if (
        str(checkpoint.get("target_id") or "") != target_id
        or str(checkpoint.get("as_of_date") or "") != as_of_date
        or _source_checkpoint_has_terminal_source_work(checkpoint)
        or not checkpoint.get("evidence_documents")
    ):
        return False
    downstream_document_ids = tuple(
        str(value)
        for value in checkpoint.get("production_downstream_document_ids") or ()
        if str(value).strip()
    )
    downstream_document_id_set = set(downstream_document_ids)
    evidence_document_ids = {
        str(row.get("document_id") or "")
        for row in checkpoint.get("evidence_documents") or ()
        if isinstance(row, Mapping) and str(row.get("document_id") or "")
    }
    if (
        not downstream_document_ids
        or len(downstream_document_ids) != len(downstream_document_id_set)
        or not downstream_document_id_set.issubset(evidence_document_ids)
    ):
        return False
    fact_path = root / "fact_extraction_result.json"
    if not fact_path.is_file():
        return False
    try:
        fact_result = _read_json(fact_path)
    except (OSError, UnicodeError, ValueError, json.JSONDecodeError):
        return False
    audit = fact_result.get("audit") or {}
    return bool(
        str(fact_result.get("target_id") or "") == target_id
        and str(fact_result.get("as_of_date") or "") == as_of_date
        and fact_result.get("status") == "FACT_EXTRACTION_PENDING"
        and fact_extraction_has_exact_checkpoint_recovery_wait(
            fact_result.get("pending_reasons") or ()
        )
        and isinstance(audit, Mapping)
        and int(audit.get("input_document_count") or 0)
        == len(downstream_document_id_set)
    )


def _source_checkpoint_needs_downstream_provider_recovery(
    *,
    root: Path,
    checkpoint: Mapping[str, Any],
    target_id: str,
    as_of_date: str,
) -> bool:
    """Allow one immutable downstream retry before expanding pending sources.

    This does not make a pending Source Graph ready.  It only handles the
    narrower case where the exact current document roster was already fully
    extracted, but a provider/output failure prevented the business model,
    component dossier, or Supervisor from adjudicating whether the remaining
    source candidates are still needed.
    """

    if (
        _source_checkpoint_has_terminal_source_work(checkpoint)
        or not checkpoint.get("evidence_documents")
    ):
        return False
    fact_path = root / "fact_extraction_result.json"
    dossier_path = root / "researcher_mode_dossier.json"
    if not fact_path.is_file() or not dossier_path.is_file():
        return False
    try:
        fact_result = _read_json(fact_path)
        dossier = _read_json(dossier_path)
    except (OSError, UnicodeError, ValueError, json.JSONDecodeError):
        return False
    if (
        str(fact_result.get("target_id") or "") != target_id
        or str(fact_result.get("as_of_date") or "") != as_of_date
        or fact_result.get("status") != "FACT_EXTRACTION_COMPLETE"
        or int((fact_result.get("audit") or {}).get("critical_count_sum") or 0)
        != 0
        or str(dossier.get("target_id") or "") != target_id
        or str(dossier.get("as_of_date") or "") != as_of_date
    ):
        return False
    evidence_document_ids = {
        str(row.get("document_id") or "")
        for row in checkpoint.get("evidence_documents") or ()
        if str(row.get("document_id") or "")
    }
    if "production_downstream_document_ids" in checkpoint:
        document_ids = {
            str(value)
            for value in checkpoint.get("production_downstream_document_ids")
            or ()
            if str(value).strip()
        }
        if (
            not document_ids
            or not document_ids.issubset(evidence_document_ids)
        ):
            return False
    else:
        document_ids = evidence_document_ids
    dispositions = tuple(
        row
        for row in fact_result.get("document_dispositions") or ()
        if isinstance(row, Mapping)
    )
    disposition_ids = {
        str(row.get("document_id") or "")
        for row in dispositions
        if str(row.get("document_id") or "")
    }
    if (
        not evidence_document_ids
        or not document_ids
        or disposition_ids != document_ids
        or any(row.get("status") == "UNREADABLE" for row in dispositions)
        or int((fact_result.get("audit") or {}).get("input_document_count") or 0)
        != len(document_ids)
    ):
        return False
    failure_texts = []
    business = dossier.get("business_model_result") or {}
    if isinstance(business, Mapping):
        failure_texts.extend(business.get("pending_reasons") or ())
    for row in dossier.get("component_results") or ():
        if isinstance(row, Mapping):
            failure_texts.extend(row.get("pending_reasons") or ())
    red_team = dossier.get("red_team_result") or {}
    if isinstance(red_team, Mapping):
        failure_texts.extend(red_team.get("pending_reasons") or ())
    supervisor_path = root / "research_supervisor_review.json"
    if supervisor_path.is_file():
        try:
            supervisor = _read_json(supervisor_path)
        except (OSError, UnicodeError, ValueError, json.JSONDecodeError):
            supervisor = {}
        if isinstance(supervisor, Mapping):
            failure_texts.extend(
                supervisor.get("unresolved_material_questions") or ()
            )
            failure_texts.append(supervisor.get("rationale") or "")
    failure_texts.extend(
        _current_downstream_provider_failure_texts(
            root=root,
            target_id=target_id,
            as_of_date=as_of_date,
            source_checkpoint=checkpoint,
        )
    )
    return any(_is_downstream_provider_or_output_failure(value) for value in failure_texts)


def _current_downstream_provider_failure_texts(
    *,
    root: Path,
    target_id: str,
    as_of_date: str,
    source_checkpoint: Mapping[str, Any],
) -> tuple[str, ...]:
    """Read provider waits from the current scoring, saturation, and Stage leaves."""

    source_binding = {
        "target_id": str(source_checkpoint.get("target_id") or target_id),
        "as_of_date": str(source_checkpoint.get("as_of_date") or as_of_date),
        "checkpoint_id": str(source_checkpoint.get("checkpoint_id") or ""),
        "checkpoint_hash": str(source_checkpoint.get("checkpoint_hash") or ""),
        "epoch": int(source_checkpoint.get("epoch") or 0),
    }
    if (
        source_binding["target_id"] != target_id
        or source_binding["as_of_date"] != as_of_date
        or not source_binding["checkpoint_id"]
        or not source_binding["checkpoint_hash"]
        or source_binding["epoch"] < 1
    ):
        return ()
    progress_path = root / "until_pass_progress.json"
    epoch_path = root / "research_epoch_checkpoint.json"
    if not progress_path.is_file() or not epoch_path.is_file():
        return ()
    try:
        progress = _read_json(progress_path)
        epoch_checkpoint = load_research_epoch_checkpoint(epoch_path)
    except (
        OSError,
        UnicodeError,
        ValueError,
        TypeError,
        json.JSONDecodeError,
    ):
        return ()
    if (
        not isinstance(progress, Mapping)
        or progress.get("source_checkpoint_binding") != source_binding
        or epoch_checkpoint.target_id != target_id
        or epoch_checkpoint.as_of_date != as_of_date
    ):
        return ()
    epoch_binding = {
        "target_id": epoch_checkpoint.target_id,
        "as_of_date": epoch_checkpoint.as_of_date,
        "checkpoint_id": epoch_checkpoint.checkpoint_id,
        "checkpoint_hash": epoch_checkpoint.checkpoint_hash,
        "epoch": epoch_checkpoint.epoch,
        "source_graph_checkpoint_id": str(
            epoch_checkpoint.source_graph_checkpoint_id or ""
        ),
    }
    if progress.get("research_epoch_checkpoint_binding") != epoch_binding:
        # A semantic transport replay may intentionally retain the prior
        # research checkpoint identity after proving that every current
        # provider prompt hash is unchanged.  The until-pass progress leaf is
        # written only after that replay returns, so bind the current source
        # and the exact replayed epoch independently instead of falsely
        # requiring their checkpoint ids to be equal.
        return ()

    def load_current(name: str) -> Mapping[str, Any]:
        path = root / name
        if not path.is_file():
            return {}
        try:
            payload = _read_json(path)
        except (OSError, UnicodeError, ValueError, json.JSONDecodeError):
            return {}
        if (
            not isinstance(payload, Mapping)
            or str(payload.get("target_id") or "") != target_id
            or str(payload.get("as_of_date") or "") != as_of_date
        ):
            return {}
        return payload

    def add_reasons(output: list[str], row: Any) -> None:
        if not isinstance(row, Mapping):
            return
        reasons = row.get("pending_reasons") or ()
        if isinstance(reasons, (list, tuple)):
            output.extend(str(value) for value in reasons)

    def mapping_rows(value: Any) -> tuple[Mapping[str, Any], ...]:
        if not isinstance(value, (list, tuple)):
            return ()
        return tuple(row for row in value if isinstance(row, Mapping))

    output: list[str] = []
    scoring = load_current("component_scoring_memo_run.json")
    for row in mapping_rows(scoring.get("component_memos")):
        add_reasons(output, row)

    aggregation = load_current("deterministic_score_aggregation_run.json")
    add_reasons(output, aggregation)
    add_reasons(output, aggregation.get("total_result"))
    for row in mapping_rows(aggregation.get("component_results")):
        add_reasons(output, row)

    stagecourt = load_current("stagecourt.json")
    add_reasons(output, stagecourt)

    for row in epoch_checkpoint.saturation_reviews:
        add_reasons(output, row)
    return tuple(output)


def _is_downstream_provider_or_output_failure(value: Any) -> bool:
    text = " ".join(str(value).split()).upper()
    return any(
        marker in text
        for marker in (
            "PROVIDER_ERROR",
            "PROVIDER_OR_OUTPUT_ERROR",
            "INVALID_PROVIDER_OUTPUT",
            "STRUCTUREDPROVIDER",
            "OLLAMA_HTTP_ERROR",
            "CODEX_CLI_",
            "CUDA ERROR",
            "CONTEXT_WINDOW",
        )
    )


def _hydrate_readonly_source_graph_run(
    *,
    root: Path,
    checkpoint: Mapping[str, Any],
    open_objectives: Sequence[Any],
    config: SourceGraphAcquisitionConfig,
    allow_pending_downstream_recovery: bool = False,
    allow_pending_fact_extraction_recovery: bool = False,
) -> SourceGraphAcquisitionRun:
    """Hydrate a ready source run without mutating acquisition lineage."""

    if (
        not allow_pending_downstream_recovery
        and not allow_pending_fact_extraction_recovery
        and not _source_checkpoint_is_ready_for_readonly_replay(checkpoint)
    ):
        raise ValueError("source checkpoint is not ready for readonly replay")
    if (
        allow_pending_downstream_recovery
        and allow_pending_fact_extraction_recovery
    ):
        raise ValueError("source checkpoint recovery replay is ambiguous")
    if allow_pending_downstream_recovery and (
        _source_checkpoint_has_terminal_source_work(checkpoint)
        or not checkpoint.get("evidence_documents")
    ):
        raise ValueError("pending downstream recovery requires pending source work")
    if allow_pending_fact_extraction_recovery and (
        not _source_checkpoint_needs_fact_extraction_recovery(
            root=root,
            checkpoint=checkpoint,
            target_id=str(checkpoint.get("target_id") or ""),
            as_of_date=str(checkpoint.get("as_of_date") or ""),
        )
    ):
        raise ValueError(
            "pending fact extraction recovery requires an exact collaboration "
            "or canonical refresh wait over the current source snapshot"
        )
    graph_payload = checkpoint.get("source_graph")
    if not isinstance(graph_payload, Mapping):
        raise ValueError("source checkpoint graph payload is missing")
    checkpoint_documents = tuple(
        checkpoint.get("evidence_documents") or ()
    )
    if (
        checkpoint.get("mode")
        == SourceGraphAcquisitionMode.PRODUCTION_DAILY.value
    ):
        downstream_document_ids = {
            str(value)
            for value in checkpoint.get(
                "production_downstream_document_ids"
            )
            or ()
            if str(value).strip()
        }
        checkpoint_documents = tuple(
            row
            for row in checkpoint_documents
            if str(row.get("document_id") or "")
            in downstream_document_ids
        )
    graph = SourceGraphExplorer().build_graph(
        target_id=str(checkpoint["target_id"]),
        as_of_date=str(checkpoint["as_of_date"]),
        documents=checkpoint_documents,
        open_objectives=open_objectives,
        source_coverage=tuple(
            graph_payload.get("covered_source_families") or ()
        ),
        generated_queries=tuple(checkpoint.get("generated_queries") or ()),
        discovery_candidates=tuple(
            checkpoint.get("search_candidates") or ()
        ),
    )
    if stable_hash(graph.to_dict()) != stable_hash(graph_payload):
        raise ValueError("source checkpoint graph cannot be reproduced")
    audit_path = root / "source_graph_acquisition_audit.json"
    if not audit_path.is_file():
        raise ValueError("source checkpoint audit is missing")
    persisted_audit = _read_json(audit_path)
    if (
        persisted_audit.get("schema_version")
        != "e2r_v5_source_graph_acquisition_run_audit_v1"
    ):
        raise ValueError("source checkpoint audit is not replay-safe")
    expected_binding = source_graph_checkpoint_audit_binding(checkpoint)
    persisted_binding = persisted_audit.get("checkpoint_binding")
    if persisted_binding is not None and (
        not isinstance(persisted_binding, Mapping)
        or dict(persisted_binding) != dict(expected_binding)
    ):
        raise ValueError("source checkpoint audit binding mismatch")
    critical = source_graph_acquisition_safety_critical_counts(
        config=config,
        checkpoint=checkpoint,
    )
    if sum(critical.values()) != 0:
        raise ValueError("source checkpoint recomputed safety audit failed")
    if persisted_binding is not None and (
        dict(persisted_audit.get("critical_counts") or {}) != dict(critical)
    ):
        raise ValueError("source checkpoint bound audit critical counts mismatch")
    pending_candidate_count = sum(
        bool(
            row.get("ranking_status") == "PENDING"
            or row.get("fetch_status")
            in {"MATERIAL_PENDING_FETCH", "FETCH_RETRY_PENDING"}
        )
        for row in checkpoint.get("search_candidates") or ()
        if isinstance(row, Mapping)
    )
    audit = {
        **persisted_audit,
        "status": "V5_SOURCE_GRAPH_ACQUISITION_SAFETY_PASS",
        "critical_counts": dict(critical),
        "critical_count_sum": 0,
        "checkpoint_binding": dict(expected_binding),
        "checkpoint_binding_status": (
            "EXACT_MATCH_RECOMPUTED"
            if persisted_binding is not None
            else "LEGACY_AUDIT_REBOUND_FROM_EXACT_CHECKPOINT_IN_MEMORY"
        ),
        "query_count": len(checkpoint.get("generated_queries") or ()),
        "search_candidate_count": len(
            checkpoint.get("search_candidates") or ()
        ),
        "pending_candidate_count": pending_candidate_count,
        "downstream_provider_recovery_replay": (
            allow_pending_downstream_recovery
        ),
        "fact_extraction_recovery_replay": (
            allow_pending_fact_extraction_recovery
        ),
    }
    return SourceGraphAcquisitionRun(
        status=str(checkpoint["status"]),
        target_id=str(checkpoint["target_id"]),
        as_of_date=str(checkpoint["as_of_date"]),
        query_generation=None,
        ranking_results=(),
        evidence_documents=tuple(
            dict(row) for row in checkpoint_documents
        ),
        source_graph=graph,
        checkpoint=checkpoint,
        audit=audit,
    )


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


def _official_gap_reasons(
    official: OfficialSourceMaterializationResult,
) -> tuple[str, ...]:
    """Preserve issuer-owned provider failures in official-first feedback.

    The materializer may have enough DART evidence to pass its mandatory
    provider audit while the generic issuer-IR discovery route still failed.
    That failure remains an official-source gap; replacing it with a generic
    "official fetched" sentence would incorrectly authorize objective closure.
    """

    reasons = list(official.pending_reasons)
    for attempt in official.provider_attempts:
        source_class = str(attempt.get("source_class") or "").upper()
        if source_class not in {"IR", "ISSUER_IR", "ISSUERIR"}:
            continue
        status = str(attempt.get("status") or "UNKNOWN")
        if (
            status == "FETCHED"
            and attempt.get("counts_as_symbol_evidence") is True
        ):
            continue
        provider_name = str(attempt.get("provider_name") or source_class)
        provider_error = str(
            attempt.get("provider_error") or "no symbol evidence"
        )
        reasons.append(
            "OFFICIAL_PROVIDER_PENDING:"
            + provider_name
            + ":"
            + status
            + ":"
            + provider_error
        )
    return tuple(dict.fromkeys(reasons)) or (
        "official sources fetched; unresolved semantic facts require discovery",
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
    document_by_id = {
        str(row.get("document_id") or ""): row
        for row in source_graph.evidence_documents
        if str(row.get("document_id") or "")
    }
    persisted_claims = tuple(
        rematerialize_claim_source_provenance(
            normalize_punctuation_only_fact_value(row),
            document=document_by_id.get(
                str(row.get("document_id") or "")
            ),
        )
        for row in _read_jsonl(paths["accepted_claims"])
    )
    all_calls: list[Mapping[str, Any]] = []
    for raw_call in _read_jsonl(paths["provider_calls"]):
        call = dict(raw_call)
        if isinstance(call.get("accepted_claims"), list):
            call["accepted_claims"] = [
                rematerialize_claim_source_provenance(
                    claim,
                    document=document_by_id.get(
                        str(claim.get("document_id") or "")
                    ),
                )
                for claim in call["accepted_claims"]
            ]
        all_calls.append(call)
    carried_coverage_refresh_document_ids: list[str] = []
    result_path = paths["result"]
    if result_path.is_file():
        try:
            prior_result = _read_json(result_path)
        except (OSError, UnicodeError, ValueError, json.JSONDecodeError):
            prior_result = {}
        if (
            str(prior_result.get("target_id") or "")
            == str(getattr(source_graph, "target_id", ""))
            and str(prior_result.get("as_of_date") or "")
            == str(getattr(source_graph, "as_of_date", ""))
        ):
            audit = prior_result.get("audit") or {}
            if isinstance(audit, Mapping):
                carried_coverage_refresh_document_ids.extend(
                    str(value)
                    for value in audit.get(
                        "pending_coverage_refresh_document_ids"
                    )
                    or ()
                    if str(value) in current_ids
                )
    # Migration for a checkpoint written before the durable refresh-intent
    # roster existed.  A pending coverage-audit call is not accepted as a
    # completed fact call, but its current document id must keep the audit from
    # silently disappearing on resume.
    carried_coverage_refresh_document_ids.extend(
        str(document_id)
        for row in all_calls
        if row.get("status") == "PENDING"
        and row.get("coverage_audit_performed") is True
        for document_id in row.get("document_ids") or ()
        if str(document_id) in current_ids
    )
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
        for row in persisted_claims
        if str(row.get("document_id") or "") in completed_ids
    )
    calls = tuple(
        row
        for row in all_calls
        if row.get("status") == "COMPLETE"
        and (
            set(row.get("document_ids") or ()).issubset(completed_ids)
            or (
                bool(row.get("transport_chunk_ids"))
                and "accepted_claims" in row
                and bool(row.get("document_ids"))
                and set(row.get("document_ids") or ()).issubset(current_ids)
            )
        )
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
        "prior_coverage_refresh_document_ids": tuple(
            dict.fromkeys(carried_coverage_refresh_document_ids)
        ),
    }


def resume_current_fact_extraction_checkpoint(
    *,
    config: CurrentResearcherModeConfig,
    target: CurrentResearchTarget,
    provider: StructuredResearchProvider,
    repo_root: str | Path = ".",
) -> ResearcherFactExtractionResult:
    """Resume only an exact pending production fact-extraction checkpoint.

    This recovery entry point deliberately reuses the same source checkpoint,
    objective construction, prior-context projection, provider journal, and
    fact writer as :class:`CurrentResearcherModeTargetRunner`.  It does not run
    business-model, component, scoring, StageCourt, or Gold work.  The narrow
    replay is useful when a collaboration response arrives after the full
    target checkpoint has already closed: rebuilding and hashing every later
    artifact cannot change the still-pending fact leaf.
    """

    root = Path(config.output_root) / target.symbol
    source_checkpoint_path = root / "source_graph_checkpoint.json"
    if not source_checkpoint_path.is_file():
        raise ValueError("fact recovery requires a source graph checkpoint")
    _configure_provider_response_cache(provider, root)

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
    objective_rows = tuple(
        row.to_dict() for row in initial_graph.open_objectives
    )
    checkpoint = validate_source_graph_checkpoint(
        load_source_graph_checkpoint(source_checkpoint_path),
        target_id=target.target_id,
        as_of_date=config.as_of_date,
    )
    source_config = SourceGraphAcquisitionConfig(
        mode=config.source_acquisition_mode,
        max_results_per_query=100,
        max_queries_per_checkpoint=10,
        max_candidates_per_checkpoint=100,
        max_fetches_per_checkpoint=20,
    )
    source_graph = _hydrate_readonly_source_graph_run(
        root=root,
        checkpoint=checkpoint,
        open_objectives=initial_graph.open_objectives,
        config=source_config,
        allow_pending_fact_extraction_recovery=(
            _source_checkpoint_needs_fact_extraction_recovery(
                root=root,
                checkpoint=checkpoint,
                target_id=target.target_id,
                as_of_date=config.as_of_date,
            )
        ),
    )
    prior_context = _load_prior_research_context(
        root,
        target_id=target.target_id,
        as_of_date=config.as_of_date,
        objectives=objective_rows,
        archetype_id=config.archetype_id,
    )
    prior_fact = _load_fact_checkpoint(root, source_graph=source_graph)
    extractor = ResearcherEvidenceFactExtractor(
        provider=provider,
        max_document_chars_per_call=int(
            getattr(
                provider,
                "semantic_prompt_chunk_chars",
                getattr(provider, "fact_document_chunk_chars", 220_000),
            )
        ),
    )
    result = extractor.extract(
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
                prior_context["supervisor_source_gap_context"]
            ),
        },
        extraction_mode="PRODUCTION_OBJECTIVE_LOCAL",
        **prior_fact,
    )
    write_researcher_fact_extraction_result(result, root)
    write_jsonl(
        root / "counterfacts.jsonl",
        (
            row.to_dict()
            for row in result.facts
            if row.direction == EvidenceDirection.COUNTER.value
        ),
    )
    return result


def _load_prior_research_context(
    root: Path,
    *,
    target_id: str,
    as_of_date: str,
    objectives: Sequence[Mapping[str, Any]],
    archetype_id: str | None = None,
) -> Mapping[str, Any]:
    fact_snapshot_available = (root / "evidence_facts.jsonl").is_file()
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
    resolved_archetype_id = str(
        archetype_id
        or (
            business_model.get("archetype_id")
            if isinstance(business_model, Mapping)
            else ""
        )
        or ""
    )
    if resolved_archetype_id:
        # The convenience JSONL is the latest attempt, not durable completion
        # authority.  A transport-pending retry may overwrite it with pending
        # rows even though the active epoch still hash-binds a complete memo.
        # Recover that exact memo from the append-only epoch ledger before
        # deciding whether its source objective is open.
        complete_components.update(
            component_id
            for component_id, memo in _load_prior_component_memos(
                root=root,
                target_id=target_id,
                archetype_id=resolved_archetype_id,
                as_of_date=as_of_date,
            ).items()
            if memo.get("research_complete") is True
        )
    structured_gap_context: Mapping[str, Any] = {}
    structured_engine_result: Mapping[str, Any] = {}
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
            structured_engine_result = structured
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
    # Deterministic score disagreements are semantic Supervisor input, not a
    # direct source-query instruction.  Sending them to SOURCE_QUERY_GENERATION
    # made the planner see broad monitoring uncertainties and create more
    # documents even when the actual leaf was only non-intersecting judge
    # ranges.  The current aggregation is passed to ResearchSupervisor later
    # in this same run; only a concrete Supervisor fact gap or query direction
    # may reopen acquisition on the following resume.
    score_gap_context: Mapping[str, Any] = {}
    epoch_context = None
    supervisor_gap_context: Mapping[str, Any] = {}
    supervisor_source_gap_context: Mapping[str, Any] = {}
    supervisor_unresolved_components: set[str] = set()
    supervisor_unresolved_objectives: set[str] = set()
    objective_component_by_id = {
        str(row.get("objective_id") or ""): str(row.get("component_id") or "")
        for row in objectives
        if str(row.get("objective_id") or "")
    }
    source_failure_by_id: dict[str, Mapping[str, Any]] = {}
    source_checkpoint_path = root / "source_graph_checkpoint.json"
    if source_checkpoint_path.is_file():
        source_checkpoint = _read_json(source_checkpoint_path)
        resolved_source_objectives = {
            str(value)
            for value in source_checkpoint.get("resolved_objective_ids") or ()
        }
        for key, kind in (
            ("query_failures", "QUERY_FAILURE"),
            ("provider_failures", "PROVIDER_FAILURE"),
            ("rejected_documents", "DOCUMENT_REJECTION"),
        ):
            for raw in source_checkpoint.get(key) or ():
                if not isinstance(raw, Mapping):
                    continue
                row = dict(raw)
                row.setdefault("failure_kind", kind)
                objective_id = str(row.get("objective_id") or "")
                if (
                    objective_id
                    and objective_id in resolved_source_objectives
                ):
                    row.setdefault("resolved", True)
                    row.setdefault(
                        "resolved_by",
                        "SOURCE_GRAPH_OBJECTIVE_RESOLUTION",
                    )
                row.setdefault("absence_eligible", False)
                reason = str(
                    row.get("failure_reason") or row.get("reason") or ""
                )
                row["zero_result_only"] = bool(
                    row.get("zero_result_only")
                ) or (
                    "NO_RESULT" in reason.upper()
                    or "ZERO_RESULT" in reason.upper()
                )
                failure_id = str(row.get("failure_id") or "").strip()
                if not failure_id:
                    failure_id = stable_intelligence_id("RSFAIL", row)
                    row["failure_id"] = failure_id
                if failure_id:
                    source_failure_by_id[failure_id] = row
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

            def route_source_row(row: Mapping[str, Any]) -> None:
                objective_id = str(row.get("objective_id") or "")
                component_id = str(row.get("component_id") or "")
                if component_id not in CANONICAL_COMPONENT_ORDER:
                    component_id = objective_component_by_id.get(
                        objective_id, ""
                    )
                if component_id in CANONICAL_COMPONENT_ORDER:
                    supervisor_unresolved_components.add(component_id)
                if objective_id in objective_component_by_id:
                    supervisor_unresolved_objectives.add(objective_id)

            for gap in supervisor.get("missing_material_facts") or ():
                if isinstance(gap, Mapping):
                    route_source_row(gap)
            for key in (
                "new_source_family_directions",
                "query_direction_briefs",
                "source_family_gaps",
            ):
                for direction in supervisor.get(key) or ():
                    if isinstance(direction, Mapping):
                        route_source_row(direction)
            source_failures = []
            enriched_failure_assessments = []
            for raw in supervisor.get("failure_assessments") or ():
                if not isinstance(raw, Mapping):
                    continue
                failure = dict(raw)
                source = source_failure_by_id.get(
                    str(failure.get("failure_id") or ""), {}
                )
                for key, value in source.items():
                    failure.setdefault(key, value)
                enriched_failure_assessments.append(failure)
                if (
                    failure.get("retryable") is not True
                    or str(failure.get("classification") or "")
                    not in {"PARSER_EXTRACTOR_FAILURE", "FETCH_FAILURE"}
                ):
                    continue
                route_source_row(failure)
                source_failures.append(failure)
            if enriched_failure_assessments:
                supervisor_gap_context = {
                    **supervisor_gap_context,
                    "failure_assessments": enriched_failure_assessments,
                }
            retryable_parser_failure_ids = {
                str(row.get("failure_id") or "")
                for row in source_failures
                if str(row.get("classification") or "")
                == "PARSER_EXTRACTOR_FAILURE"
                and str(row.get("failure_id") or "")
            }
            parser_failures = list(
                failure_id
                for failure_id in (
                    supervisor.get("parser_or_extractor_failures") or ()
                )
                if str(failure_id) in retryable_parser_failure_ids
            )
            filtered_directions: dict[str, list[Mapping[str, Any]]] = {}
            for key in (
                "new_source_family_directions",
                "query_direction_briefs",
            ):
                filtered_directions[key] = [
                    dict(direction)
                    for direction in supervisor.get(key) or ()
                    if isinstance(direction, Mapping)
                    and str(direction.get("objective_id") or "")
                    in supervisor_unresolved_objectives
                ]
            missing_facts = [
                dict(row)
                for row in supervisor.get("missing_material_facts") or ()
                if isinstance(row, Mapping)
            ]
            source_family_gaps = [
                dict(row) if isinstance(row, Mapping) else str(row)
                for row in supervisor.get("source_family_gaps") or ()
                if (
                    isinstance(row, Mapping)
                    and (
                        str(row.get("component_id") or "")
                        in supervisor_unresolved_components
                        or str(row.get("objective_id") or "")
                        in supervisor_unresolved_objectives
                    )
                )
            ]
            if (
                missing_facts
                or source_failures
                or parser_failures
                or any(filtered_directions.values())
                or source_family_gaps
            ):
                supervisor_source_gap_context = {
                    "status": supervisor.get("status"),
                    "missing_material_facts": missing_facts,
                    "failure_assessments": source_failures,
                    "new_source_family_directions": filtered_directions[
                        "new_source_family_directions"
                    ],
                    "query_direction_briefs": filtered_directions[
                        "query_direction_briefs"
                    ],
                    "source_family_gaps": source_family_gaps,
                    "parser_or_extractor_failures": parser_failures,
                }
    resolved_objective_ids = tuple(
        str(row["objective_id"])
        for row in objectives
        if str(row.get("component_id") or "") in complete_components
        and str(row.get("component_id") or "")
        not in structured_missing_components
        and str(row.get("component_id") or "")
        not in supervisor_unresolved_components
        and str(row.get("objective_id") or "")
        not in supervisor_unresolved_objectives
    )
    return {
        "facts": facts,
        "fact_snapshot_available": fact_snapshot_available,
        "business_model": business_model,
        "research_gap_feedback": feedback,
        "structured_gap_context": structured_gap_context,
        "structured_engine_result": structured_engine_result,
        "score_gap_context": score_gap_context,
        "supervisor_gap_context": supervisor_gap_context,
        "supervisor_source_gap_context": supervisor_source_gap_context,
        "resolved_objective_ids": resolved_objective_ids,
        "research_epoch": epoch_context,
    }


def _component_supervisor_feedback_by_component(
    context: Mapping[str, Any] | None,
    *,
    objective_component_by_id: Mapping[str, str] | None = None,
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
    objective_components = {
        str(objective_id): str(component_id)
        for objective_id, component_id in (
            objective_component_by_id or {}
        ).items()
        if str(objective_id)
        and str(component_id) in CANONICAL_COMPONENT_ORDER
    }

    def component_for(row: Mapping[str, Any]) -> str:
        direct = str(row.get("component_id") or "")
        if direct in CANONICAL_COMPONENT_ORDER:
            return direct
        return objective_components.get(
            str(row.get("objective_id") or ""), ""
        )

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
    routed_rows_by_key: dict[
        str, dict[str, list[Mapping[str, Any]]]
    ] = {
        key: {}
        for key in (
            "new_source_family_directions",
            "query_direction_briefs",
            "source_family_gaps",
            "failure_assessments",
            "parser_or_extractor_failures",
        )
    }
    for key in (
        "new_source_family_directions",
        "query_direction_briefs",
        "source_family_gaps",
    ):
        for row in context.get(key) or ():
            if not isinstance(row, Mapping):
                continue
            component_id = component_for(row)
            if component_id:
                routed_rows_by_key[key].setdefault(
                    component_id, []
                ).append(dict(row))
    retryable_failure_by_id: dict[str, Mapping[str, Any]] = {}
    for row in context.get("failure_assessments") or ():
        if (
            not isinstance(row, Mapping)
            or row.get("retryable") is not True
            or str(row.get("classification") or "")
            not in {"PARSER_EXTRACTOR_FAILURE", "FETCH_FAILURE"}
        ):
            continue
        failure = dict(row)
        failure_id = str(failure.get("failure_id") or "")
        if failure_id:
            retryable_failure_by_id[failure_id] = failure
        component_id = component_for(failure)
        if component_id:
            routed_rows_by_key["failure_assessments"].setdefault(
                component_id, []
            ).append(failure)
    for raw in context.get("parser_or_extractor_failures") or ():
        row = (
            dict(raw)
            if isinstance(raw, Mapping)
            else retryable_failure_by_id.get(str(raw))
        )
        if not isinstance(row, Mapping):
            continue
        component_id = component_for(row)
        if component_id:
            routed_rows_by_key[
                "parser_or_extractor_failures"
            ].setdefault(component_id, []).append(dict(row))

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
        ]
        gaps = gaps_by_component.get(component_id, [])
        routed = {
            key: rows_by_component.get(component_id, [])
            for key, rows_by_component in routed_rows_by_key.items()
        }
        # A provider/transport placeholder marks every component PENDING before
        # the supervisor has produced any semantic finding.  Status alone is
        # therefore not rewrite authority: otherwise a completed memo is
        # reopened merely because the supervisor response is still in flight.
        # Findings and component-scoped material-fact gaps are the actionable
        # feedback planes.
        if not findings and not gaps and not any(routed.values()):
            continue
        result[component_id] = {
            **shared,
            "component_id": component_id,
            "component_status": status,
            "component_findings": findings,
            "missing_material_facts": gaps,
            **{
                key: rows
                for key, rows in routed.items()
                if rows
            },
        }
    return result


def _score_gap_context_for_supervisor(
    *,
    aggregation: DeterministicScoreAggregationRun,
    scoring_memos: ComponentScoringMemoRun,
    structured_report_candidates: Sequence[Mapping[str, Any]] = (),
) -> Mapping[str, Any]:
    """Expose only active score-research leaves to the semantic supervisor.

    The deterministic aggregator already returns a material judge
    disagreement to research, but its compact request intentionally omits the
    judges' prose.  The Supervisor needs the exact allowed ranges and
    rationales to decide whether the component memo needs a semantic rewrite
    or whether a genuinely missing source-backed fact requires another query.
    Transport-only missing judge responses are preserved as diagnostics but
    never become memo-rewrite authority.
    """

    context = dict(aggregation.to_score_gap_context())
    material_components = {
        row.component_id
        for row in aggregation.component_results
        if row.material_disagreement
        and "UNRESOLVED_MATERIAL_JUDGE_DISAGREEMENT"
        in row.pending_reasons
    }
    scoring_by_component = {
        row.component_id: row for row in scoring_memos.component_memos
    }
    judge_reviews = []
    for component_id in CANONICAL_COMPONENT_ORDER:
        if component_id not in material_components:
            continue
        scoring_memo = scoring_by_component.get(component_id)
        if scoring_memo is None:
            continue
        judge_reviews.append(
            {
                "component_id": component_id,
                "judge_reviews": [
                    {
                        "role": decision.role,
                        "proposed_points": decision.proposed_points,
                        "allowed_range": list(decision.allowed_range),
                        "rationale": decision.rationale,
                        "disagreements": list(decision.disagreements),
                        "why_not_higher": decision.why_not_higher,
                        "why_not_lower": decision.why_not_lower,
                    }
                    for decision in scoring_memo.judge_decisions
                ],
            }
        )
    context["material_disagreement_component_ids"] = sorted(
        material_components
    )
    context["material_disagreement_judge_reviews"] = judge_reviews
    # CompanyGuide's public report history is a discovery surface, not a
    # score source.  Preserve every bounded metadata candidate so the semantic
    # Supervisor can decide whether one of those reports is worth resolving
    # through the LLM-owned Source Graph query path.  Numeric preview fields
    # remain explicitly non-evidence until the full report is independently
    # discovered, fetched, parsed, and linked to an EvidenceFact.
    invalid_report_candidate_constants = [
        str(dict(row).get("candidate_id") or "UNKNOWN")
        for row in structured_report_candidates
        if str(dict(row).get("provider_name") or "") != "CompanyGuide"
        or str(dict(row).get("source_family_hint") or "")
        != "PUBLIC_BROKER_PDF"
        or str(dict(row).get("research_route") or "")
        != "PUBLIC_BROKER_REPORT"
    ]
    if invalid_report_candidate_constants:
        raise ValueError(
            "structured report prompt projection has mixed route constants:"
            + ",".join(invalid_report_candidate_constants)
        )
    report_candidate_fields = (
        "candidate_id",
        "published_at",
        "broker",
        "title",
        "provider_report_id",
        "provider_index",
        "provider_file_name",
        "provider_summary",
    )
    context["structured_report_source_candidates"] = {
        "schema_version": (
            "e2r_v5_structured_report_candidate_prompt_projection_v1"
        ),
        "fields": list(report_candidate_fields),
        "rows": [
            [dict(row).get(field) for field in report_candidate_fields]
            for row in structured_report_candidates
        ],
        "candidate_count": len(structured_report_candidates),
        "candidate_roster_hash": stable_hash(
            [
                [dict(row).get(field) for field in report_candidate_fields]
                for row in structured_report_candidates
            ]
        ),
        "candidate_id_roster_hash": stable_hash(
            sorted(
                str(dict(row).get("candidate_id") or "")
                for row in structured_report_candidates
            )
        ),
        "every_candidate_projected": True,
        "fixed_top_n_used": False,
        "metadata_only_not_evidence": True,
        "provider_summary_is_non_evidence_discovery_hint": True,
        "provider_name": "CompanyGuide",
        "source_family_hint": "PUBLIC_BROKER_PDF",
        "research_route": "PUBLIC_BROKER_REPORT",
    }
    context["structured_report_source_candidate_contract"] = {
        "bounded_candidate_count": len(structured_report_candidates),
        "candidate_roster_complete_within_materializer_budget": True,
        "metadata_is_discovery_hint_not_evidence": True,
        "numeric_preview_is_not_fact_authority": True,
        "llm_owns_materiality_and_objective_binding": True,
        "literal_query_generation_owner": "SOURCE_QUERY_GENERATION_LLM",
        "deterministic_url_or_query_synthesis_allowed": False,
        "full_document_required_before_fact_extraction": True,
        "score_or_stage_authority": False,
    }
    context["score_or_stage_authority"] = False
    return context


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
    return canary_output_tree_hash(
        root,
        include_post_run_gold=False,
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


def _reusable_prior_component_memos(
    *,
    prior_component_memos: Mapping[str, Mapping[str, Any]],
    actionable_feedback_by_component: Mapping[str, Mapping[str, Any]],
    prior_facts: Sequence[Mapping[str, Any]],
    current_facts: Sequence[Any],
    prior_fact_snapshot_available: bool,
    prior_structured_result: Mapping[str, Any],
    current_structured_result: StructuredEngineResult,
    required_roles_by_component: Mapping[str, Sequence[str]],
) -> Mapping[str, Mapping[str, Any]]:
    """Reuse a complete memo only when its semantic input plane is unchanged."""

    if (
        not prior_fact_snapshot_available
        or not prior_structured_result
        or _semantic_row_roster_hash(prior_facts, id_key="fact_id")
        != _semantic_row_roster_hash(current_facts, id_key="fact_id")
    ):
        return {}
    current_fact_ids = _semantic_row_ids(current_facts, id_key="fact_id")
    prior_structured_hashes = _component_structured_input_hashes(
        prior_structured_result.get("records") or (),
        required_roles_by_component=required_roles_by_component,
    )
    current_structured_hashes = _component_structured_input_hashes(
        current_structured_result.records,
        required_roles_by_component=required_roles_by_component,
    )
    return {
        component_id: memo
        for component_id, memo in prior_component_memos.items()
        if component_id in CANONICAL_COMPONENT_ORDER
        and memo.get("research_complete") is True
        and component_id not in actionable_feedback_by_component
        and _component_memo_cites_only_current_facts(
            memo,
            current_fact_ids=current_fact_ids,
        )
        and prior_structured_hashes.get(component_id)
        == current_structured_hashes.get(component_id)
    }


def _component_memo_cites_only_current_facts(
    memo: Mapping[str, Any],
    *,
    current_fact_ids: set[str],
) -> bool:
    for field_name in (
        "positive_fact_ids",
        "counter_fact_ids",
        "resolution_fact_ids",
    ):
        values = memo.get(field_name) or ()
        if isinstance(values, (str, bytes)) or not isinstance(values, Sequence):
            return False
        for value in values:
            fact_id = str(value).strip()
            if not fact_id or fact_id not in current_fact_ids:
                return False
    return True


def _semantic_row_ids(rows: Sequence[Any], *, id_key: str) -> set[str]:
    row_ids: set[str] = set()
    for row in rows:
        if isinstance(row, Mapping):
            payload = row
        else:
            to_dict = getattr(row, "to_dict", None)
            if not callable(to_dict):
                raise TypeError("semantic input row must expose to_dict")
            payload = to_dict()
        row_id = str(payload.get(id_key) or "")
        if not row_id or row_id in row_ids:
            raise ValueError(f"semantic input rows require unique {id_key}")
        row_ids.add(row_id)
    return row_ids


def _semantic_row_roster_hash(
    rows: Sequence[Any],
    *,
    id_key: str,
) -> str:
    payloads = []
    seen: set[str] = set()
    for row in rows:
        if isinstance(row, Mapping):
            payload = dict(row)
        else:
            to_dict = getattr(row, "to_dict", None)
            if not callable(to_dict):
                raise TypeError("semantic input row must expose to_dict")
            payload = dict(to_dict())
        row_id = str(payload.get(id_key) or "")
        if not row_id or row_id in seen:
            raise ValueError(
                f"semantic input rows require unique {id_key}"
            )
        seen.add(row_id)
        payloads.append(payload)
    return stable_hash(
        sorted(payloads, key=lambda payload: str(payload[id_key]))
    )


def _component_structured_input_hashes(
    records: Sequence[Any],
    *,
    required_roles_by_component: Mapping[str, Sequence[str]],
) -> Mapping[str, str]:
    payloads = []
    for row in records:
        if isinstance(row, Mapping):
            payload = dict(row)
        else:
            to_dict = getattr(row, "to_dict", None)
            if not callable(to_dict):
                raise TypeError("structured input row must expose to_dict")
            payload = dict(to_dict())
        payloads.append(payload)
    result = {}
    for component_id in CANONICAL_COMPONENT_ORDER:
        required_roles = tuple(
            dict.fromkeys(
                str(role)
                for role in required_roles_by_component.get(
                    component_id, ()
                )
                if str(role)
            )
        )
        compatible_roles = {
            role
            for required_role in required_roles
            for role in (
                required_role,
                *PHASE86_COMPONENT_ROLE_COMPATIBILITY.get(
                    required_role, ()
                ),
            )
        }
        relevant = [
            payload
            for payload in payloads
            if compatible_roles
            & {
                str(role)
                for role in payload.get("evidence_roles") or ()
            }
        ]
        result[component_id] = stable_hash(
            {
                "required_roles": list(required_roles),
                "records": sorted(
                    relevant,
                    key=lambda payload: str(
                        payload.get("record_id") or ""
                    ),
                ),
            }
        )
    return result


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
    "load_current_research_target_registry",
    "load_current_research_targets",
    "write_production_lane",
]
