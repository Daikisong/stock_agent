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
import os
from pathlib import Path
import tempfile
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
from .collaboration_envelope_contract import (
    COLLABORATION_PROVIDER_NAME,
    validate_collaboration_request,
    validate_collaboration_response_envelope,
)
from .component_scoring_memos import (
    ComponentScoringMemoRun,
    LLMComponentScoringMemoEngine,
    write_component_scoring_memo_run,
)
from .dossier import CanonicalResearchDossierBuilder, ResearcherModeDossier
from .evidence_fact_extractor import (
    FACT_EXTRACTION_OUTPUT_FILES,
    FACT_EXTRACTION_SEMANTICS_VERSION,
    ResearcherEvidenceFactExtractor,
    ResearcherFactExtractionResult,
    _accepted_claim,
    _coerce_provider_call,
    _coerce_rejection,
    _normalize_transport_fact_proposal,
    fact_extraction_has_exact_checkpoint_recovery_wait,
    normalize_punctuation_only_fact_value,
    production_material_fact_rows,
    rematerialize_claim_source_provenance,
    resolve_current_fact_lineage_recovery_binding,
    write_researcher_fact_extraction_result,
)
from .evidence_fact_compiler import EvidenceFactCompiler
from .fact_lineage_materials import (
    load_authoritative_research_epoch_fact_ledger,
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
    _coerce_checkpoint,
    load_research_epoch_checkpoint,
    write_research_epoch_run,
)
from .research_question_seed_catalog import (
    load_research_question_seed_catalog,
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
from .schemas import (
    CANONICAL_COMPONENT_ORDER,
    ComponentResearchPlan,
    EvidenceDirection,
    scrub_blind_research_payload,
)
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
    OFFICIAL_SOURCE_SUCCESS_DISCOVERY_FALLBACK_REASON,
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
    source_graph_legacy_text_cap_document_ids,
    source_graph_pending_source_repair_ids,
    _supervisor_explicitly_exhausted_source_routes,
    validated_official_first_resolution_query_ids,
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
    fact_documents_per_call: int = 1
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
        if (
            isinstance(self.fact_documents_per_call, bool)
            or not isinstance(self.fact_documents_per_call, int)
            or self.fact_documents_per_call <= 0
        ):
            raise ValueError(
                "fact_documents_per_call must be a positive transport batch"
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


def _initial_component_research_plans(
    *,
    target_id: str,
    archetype_id: str,
    historical_anchors: Sequence[Mapping[str, Any]],
) -> tuple[ComponentResearchPlan, ...]:
    """Build Source Graph plans from the same extensible seed catalog as dossiers.

    Research questions remain semantic hints rather than score gates.  Omitting
    the catalog here made the acquisition LLM see only two generic sentences,
    while the later component researchers received the actual archetype
    questions.  Keeping both stages on one catalog preserves sector expansion
    without introducing target-specific query templates.
    """

    return ComponentResearchPlanner().plan(
        target_id=target_id,
        archetype_id=archetype_id,
        evidence_facts=(),
        historical_anchors=historical_anchors,
        research_seeds=load_research_question_seed_catalog().seeds,
    )


class FactExtractionCheckpointPending(RuntimeError):
    """Stop a target exactly at its persisted fact-response boundary.

    Fact extraction is an upstream material-evidence gate.  Starting peer,
    business-model, scoring, or StageCourt providers while its exact Codex
    collaboration response is still pending creates stale downstream requests
    that cannot be valid for the eventual fact graph.  The CLI catches this
    typed boundary, reports the pending leaf, and resumes only after the exact
    response has been imported.
    """

    def __init__(
        self,
        *,
        target: CurrentResearchTarget,
        output_root: Path,
        source_graph: SourceGraphAcquisitionRun,
        fact_extraction: ResearcherFactExtractionResult,
        audit: Mapping[str, Any],
    ) -> None:
        super().__init__(
            f"{target.target_id} fact extraction checkpoint is pending"
        )
        self.target = target
        self.output_root = output_root
        self.source_graph = source_graph
        self.fact_extraction = fact_extraction
        self.audit = dict(audit)


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
        self._fact_extractor_injected = fact_extractor is not None
        self.fact_extractor = fact_extractor or ResearcherEvidenceFactExtractor(
            provider=effective_provider,
            max_document_chars_per_call=int(
                getattr(
                    effective_provider,
                    "semantic_prompt_chunk_chars",
                    220_000,
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
        fact_extractor = self.fact_extractor
        if (
            fact_extractor.documents_per_call
            != config.fact_documents_per_call
        ):
            if self._fact_extractor_injected:
                raise ValueError(
                    "injected fact extractor transport batch differs from config"
                )
            fact_extractor = ResearcherEvidenceFactExtractor(
                provider=self.provider,
                documents_per_call=config.fact_documents_per_call,
                max_document_chars_per_call=int(
                    getattr(
                        self.provider,
                        "semantic_prompt_chunk_chars",
                        220_000,
                    )
                ),
            )
        anchors = _historical_anchors(
            repo_root=repo_root,
            archetype_id=config.archetype_id,
        )
        initial_plans = _initial_component_research_plans(
            target_id=target.target_id,
            archetype_id=config.archetype_id,
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
        authoritative_fact_context = (
            _load_authoritative_prior_fact_context(
                root,
                target_id=target.target_id,
                as_of_date=config.as_of_date,
                source_checkpoint=prior_source_checkpoint,
            )
        )
        prior_context = _load_prior_research_context(
            root,
            target_id=target.target_id,
            as_of_date=config.as_of_date,
            objectives=objective_rows,
            archetype_id=config.archetype_id,
            authoritative_fact_context=authoritative_fact_context,
        )
        authoritative_fact_lineage_recovery_required = bool(
            prior_context[
                "authoritative_fact_lineage_recovery_required"
            ]
        )
        source_context_requires_acquisition = bool(
            not authoritative_fact_lineage_recovery_required
            and (
                prior_context["source_transport_pending_objective_ids"]
                or prior_context[
                    "source_queries_without_accepted_fact_lineage"
                ]
            )
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
        if (
            source_context_requires_acquisition
            and source_resume_mode == "REUSE_READY_CHECKPOINT"
            and prior_source_checkpoint is not None
            and _source_checkpoint_is_ready_for_readonly_replay(
                prior_source_checkpoint
            )
        ):
            # A completed fact pass may legitimately reopen acquisition, but
            # the ready checkpoint is still the prior input authority.  Verify
            # its graph/audit binding before giving it to a mutating acquirer;
            # otherwise a stale or tampered audit could bypass the readonly
            # replay validation merely because a new semantic gap appeared.
            _hydrate_readonly_source_graph_run(
                root=root,
                checkpoint=prior_source_checkpoint,
                open_objectives=initial_graph.open_objectives,
                config=source_acquisition_config,
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
        source_checkpoint_legacy_text_cap_repair_only = bool(
            prior_source_checkpoint is not None
            and (
                source_graph_legacy_text_cap_document_ids(
                    prior_source_checkpoint
                )
                or source_graph_pending_source_repair_ids(
                    prior_source_checkpoint
                )
            )
        )
        source_checkpoint_migration_only = bool(
            source_checkpoint_navigation_migration_only
            or source_checkpoint_provenance_migration_only
        )
        source_checkpoint_readonly_replayed = bool(
            not authoritative_fact_lineage_recovery_required
            and source_resume_mode == "REUSE_READY_CHECKPOINT"
            and prior_source_checkpoint is not None
            and not source_context_requires_acquisition
            and not source_checkpoint_migration_only
            and not source_checkpoint_legacy_text_cap_repair_only
            and _source_checkpoint_is_ready_for_readonly_replay(
                prior_source_checkpoint
            )
        )
        source_checkpoint_downstream_recovery_replayed = bool(
            not authoritative_fact_lineage_recovery_required
            and source_resume_mode == "REUSE_READY_CHECKPOINT"
            and prior_source_checkpoint is not None
            and not source_context_requires_acquisition
            and not source_checkpoint_readonly_replayed
            and not source_checkpoint_migration_only
            and not source_checkpoint_legacy_text_cap_repair_only
            and _source_checkpoint_needs_downstream_provider_recovery(
                root=root,
                checkpoint=prior_source_checkpoint,
                target_id=target.target_id,
                as_of_date=config.as_of_date,
            )
        )
        source_checkpoint_fact_extraction_recovery_replayed = bool(
            authoritative_fact_lineage_recovery_required
            or (
                source_resume_mode == "REUSE_READY_CHECKPOINT"
                and prior_source_checkpoint is not None
                and not source_context_requires_acquisition
                and not source_checkpoint_readonly_replayed
                and not source_checkpoint_migration_only
                and not source_checkpoint_legacy_text_cap_repair_only
                and not source_checkpoint_downstream_recovery_replayed
                and _source_checkpoint_needs_fact_extraction_recovery(
                    root=root,
                    checkpoint=prior_source_checkpoint,
                    target_id=target.target_id,
                    as_of_date=config.as_of_date,
                )
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
                    and not authoritative_fact_lineage_recovery_required
                ),
                authoritative_fact_lineage_recovery=(
                    authoritative_fact_context
                    if authoritative_fact_lineage_recovery_required
                    else None
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
                    "prior_structured_report_source_candidates": dict(
                        prior_context[
                            "structured_report_candidate_context"
                        ]
                    ),
                    "prior_deterministic_score_gap": dict(
                        prior_context["score_gap_context"]
                    ),
                    "prior_supervisor_gap": dict(
                        prior_context["supervisor_source_gap_context"]
                    ),
                    "prior_queries_without_accepted_fact_lineage": list(
                        prior_context[
                            "source_queries_without_accepted_fact_lineage"
                        ]
                    ),
                    "prior_research_epoch": prior_context["research_epoch"],
                },
                resolved_objective_ids=prior_context["resolved_objective_ids"],
                semantic_resolved_objective_ids=prior_context[
                    "semantic_resolved_objective_ids"
                ],
                prior_checkpoint=prior_source_checkpoint,
                official_domain_allowlist=target.official_domains,
                checkpoint_migration_only=(
                    source_checkpoint_migration_only
                ),
                checkpoint_source_repair_only=(
                    source_checkpoint_legacy_text_cap_repair_only
                ),
            )
            write_source_graph_acquisition_run(source_graph, output_root=root)
        prior_fact = _load_fact_checkpoint(
            root,
            source_graph=source_graph,
            committed_fact_snapshot=(
                authoritative_fact_context.get(
                    "committed_fact_result_snapshot"
                )
                if authoritative_fact_context is not None
                else None
            ),
        )
        fact_score_gap_context = {
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
        }
        authoritative_fact_recovery_kwargs = (
            _authoritative_fact_recovery_extract_kwargs(
                root=root,
                authoritative_fact_context=authoritative_fact_context,
                target=target,
                archetype_id=config.archetype_id,
                as_of_date=config.as_of_date,
                documents=source_graph.evidence_documents,
                open_objectives=objective_rows,
                current_facts=prior_context["facts"],
                score_gap_context=fact_score_gap_context,
                prior_fact=prior_fact,
                extraction_mode=(
                    "PRODUCTION_OBJECTIVE_LOCAL"
                    if config.source_acquisition_mode
                    == SourceGraphAcquisitionMode.PRODUCTION_DAILY.value
                    else "RESEARCH_BACKFILL"
                ),
            )
        )
        fact_extraction = fact_extractor.extract(
            target_id=target.target_id,
            target_name=target.company_name,
            target_aliases=target.aliases,
            archetype_id=config.archetype_id,
            as_of_date=config.as_of_date,
            documents=source_graph.evidence_documents,
            open_objectives=objective_rows,
            current_facts=prior_context["facts"],
            score_gap_context=fact_score_gap_context,
            extraction_mode=(
                "PRODUCTION_OBJECTIVE_LOCAL"
                if config.source_acquisition_mode
                == SourceGraphAcquisitionMode.PRODUCTION_DAILY.value
                else "RESEARCH_BACKFILL"
            ),
            **authoritative_fact_recovery_kwargs,
            **prior_fact,
        )
        write_researcher_fact_extraction_result(fact_extraction, root)
        if fact_extraction.status != "FACT_EXTRACTION_COMPLETE":
            # Upstream facts define every downstream prompt and deterministic
            # input.  A pending exact Codex response is therefore a hard
            # ordering boundary, not permission to open speculative requests.
            source_ready = bool(
                source_graph.status
                in {
                    "EPOCH_COMPLETE_REQUIRES_SUPERVISOR",
                    "STOPPED_ON_RESOLUTION",
                }
                and int(source_graph.audit.get("critical_count_sum") or 0) == 0
            )
            exact_completion_gate = (
                "fact_extraction_complete"
                if (
                    source_ready
                    or fact_extraction_has_exact_checkpoint_recovery_wait(
                        fact_extraction.pending_reasons
                    )
                )
                else "source_graph_checkpoint_ready"
            )
            gate_audit = {
                "schema_version": CURRENT_RESEARCHER_MODE_SCHEMA_VERSION,
                "status": "RESEARCH_CHECKPOINT_PENDING",
                "target_id": target.target_id,
                "as_of_date": config.as_of_date,
                "exact_completion_gate": exact_completion_gate,
                "fact_extraction_status": fact_extraction.status,
                "fact_extraction_pending_reasons": list(
                    fact_extraction.pending_reasons
                ),
                "authoritative_fact_ledger_available": prior_context[
                    "authoritative_fact_ledger_available"
                ],
                "authoritative_fact_lineage_recovery_required": (
                    authoritative_fact_lineage_recovery_required
                ),
                "pending_new_fact_epoch_commit_required": prior_context[
                    "pending_new_fact_epoch_commit_required"
                ],
                "downstream_pipeline_started": False,
                "blocked_downstream_stages": [
                    "structured_peer_materialization",
                    "business_model_research",
                    "component_research",
                    "scoring",
                    "stagecourt",
                ],
                "gold_visibility": False,
                "completion_based_on_fixed_rounds": False,
                "completion_gates": {
                    "source_graph_checkpoint_ready": source_ready,
                    "fact_extraction_complete": False,
                },
                "fact_count": len(fact_extraction.facts),
                "document_count": len(source_graph.evidence_documents),
            }
            write_json(root / "current_researcher_mode_audit.json", gate_audit)
            write_json(
                root / "target_run_manifest.json",
                {
                    **gate_audit,
                    "company_name": target.company_name,
                    "aliases": list(target.aliases),
                    "archetype_id": config.archetype_id,
                    "latest_trading_snapshot_date": (
                        config.latest_trading_snapshot_date
                    ),
                    "output_tree_hash": _tree_hash(root),
                },
            )
            raise FactExtractionCheckpointPending(
                target=target,
                output_root=root,
                source_graph=source_graph,
                fact_extraction=fact_extraction,
                audit=gate_audit,
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
            "authoritative_fact_ledger_available": prior_context[
                "authoritative_fact_ledger_available"
            ],
            "authoritative_fact_lineage_recovery_required": (
                authoritative_fact_lineage_recovery_required
            ),
            "pending_new_fact_epoch_commit_required": prior_context[
                "pending_new_fact_epoch_commit_required"
            ],
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
            "source_checkpoint_legacy_text_cap_repair_only": (
                source_checkpoint_legacy_text_cap_repair_only
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
    *,
    repo_root: str | Path,
    archetype_id: str,
    allow_output_fallback: bool = True,
) -> tuple[Mapping[str, Any], ...]:
    atlas_path = Path(repo_root) / "docs/operational/e2r_v5_component_anchor_atlas.json"
    if atlas_path.is_file():
        payload = _read_json(atlas_path)
    elif not allow_output_fallback:
        raise ValueError(
            "tracked historical anchor atlas is required when output fallback is disabled"
        )
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
    if source_graph_legacy_text_cap_document_ids(checkpoint):
        # A legacy PageFetcher row can look terminal even though the old
        # 200,000-character transport cap was persisted as source content.
        # Force the existing bounded quarantine/refetch migration before any
        # downstream fact leaf is allowed to certify that source as complete.
        return False
    if source_graph_pending_source_repair_ids(checkpoint):
        # A quarantined production source cannot disappear into a resolved
        # objective while its exact same-URL byte replacement is still
        # pending.  Keep the target at Source/Provider Pending.
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
        row.get("execution_status")
        in {"PENDING", "BLOCKED_OFFICIAL_FIRST"}
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

    # Active query, ranking, and fetch states are already committed upstream
    # work.  Drain them before retrying any dossier/scoring leaf; otherwise a
    # stale downstream provider wait can freeze an exact ranking response (or
    # its selected fetch route) against a document graph known to be
    # incomplete.  STOPPED_ON_RESOLUTION may retain suppressed historical
    # pending rows, so use the source state machine status rather than treating
    # every raw legacy marker as active.  Fact extraction has its own narrower
    # immutable-snapshot recovery path and is evaluated separately.
    if (
        str(checkpoint.get("status") or "")
        in {
            "QUERY_GENERATION_PENDING",
            "QUERY_EXECUTION_PENDING",
            "CANDIDATE_RANKING_PENDING",
            "CHECKPOINT_PENDING",
        }
        or any(
            isinstance(row, Mapping)
            and row.get("execution_status") == "PENDING"
            for row in checkpoint.get("generated_queries") or ()
        )
    ):
        return False
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
            "CODEX_CLI_",
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
    authoritative_fact_lineage_recovery: Mapping[str, Any] | None = None,
) -> SourceGraphAcquisitionRun:
    """Hydrate a ready source run without mutating acquisition lineage."""

    authoritative_recovery = bool(
        authoritative_fact_lineage_recovery
        and authoritative_fact_lineage_recovery.get(
            "authoritative_fact_lineage_recovery_required"
        )
        is True
    )
    if (
        not allow_pending_downstream_recovery
        and not allow_pending_fact_extraction_recovery
        and not authoritative_recovery
        and not _source_checkpoint_is_ready_for_readonly_replay(checkpoint)
    ):
        raise ValueError("source checkpoint is not ready for readonly replay")
    if (
        allow_pending_downstream_recovery
        and (allow_pending_fact_extraction_recovery or authoritative_recovery)
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
    if authoritative_recovery:
        assert authoritative_fact_lineage_recovery is not None
        expected_source_id = str(
            authoritative_fact_lineage_recovery.get(
                "source_graph_checkpoint_id"
            )
            or ""
        )
        expected_source_hash = str(
            authoritative_fact_lineage_recovery.get(
                "source_graph_checkpoint_hash"
            )
            or ""
        )
        if (
            str(authoritative_fact_lineage_recovery.get("target_id") or "")
            != str(checkpoint.get("target_id") or "")
            or str(
                authoritative_fact_lineage_recovery.get("as_of_date") or ""
            )
            != str(checkpoint.get("as_of_date") or "")
            or expected_source_id != str(checkpoint.get("checkpoint_id") or "")
            or expected_source_hash
            != str(checkpoint.get("checkpoint_hash") or "")
        ):
            raise ValueError(
                "authoritative fact recovery source checkpoint binding drift"
            )
        # Authoritative fact recovery is a serialization barrier, not an
        # ordinary downstream replay.  Freeze the exact source snapshot even
        # when it still has a ranking/query response to consume; restore the
        # missing fact ledger first and let the next clean resume consume that
        # source response.  For example, a pending delivery inspection must
        # not make the already signed inventory ledger look like identity
        # drift.  Target/date/id/hash above and graph/audit reproduction below
        # remain the fail-closed integrity checks.
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
            or authoritative_recovery
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
        OFFICIAL_SOURCE_SUCCESS_DISCOVERY_FALLBACK_REASON,
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


def _upgrade_current_lineage_objective_reassessment_receipts(
    provider_calls: Sequence[Mapping[str, Any]],
    *,
    document_by_id: Mapping[str, Mapping[str, Any]],
) -> tuple[str, ...]:
    """Upgrade only claim-proven legacy journal calls to typed intent.

    Current-lineage recovery calls written before the typed receipt existed
    still embed the exact accepted claims that official replay validated.  A
    claim objective that is no longer current, but remains in the document's
    explicit historical objective lineage, proves that this recovered
    document needs one current-objective coverage audit.  Ordinary provider
    calls and the global claim roster are intentionally outside this narrow
    migration boundary.
    """

    reassessment_ids: set[str] = set()
    for call in provider_calls:
        if not call.get("current_lineage_request_ids"):
            continue
        _coerce_provider_call(call)
        call_document_ids = {
            str(value) for value in call.get("document_ids") or ()
        }
        if (
            "current_lineage_objective_reassessment_document_ids"
            in call
        ):
            typed_ids = {
                str(value)
                for value in call.get(
                    "current_lineage_objective_reassessment_document_ids"
                )
                or ()
            }
            reassessment_ids.update(typed_ids)
            continue

        claimed_objective_ids_by_document: dict[str, set[str]] = {}
        embedded_claims = call.get("accepted_claims")
        if isinstance(embedded_claims, Sequence) and not isinstance(
            embedded_claims,
            (str, bytes),
        ):
            for claim in embedded_claims:
                if not isinstance(claim, Mapping):
                    raise ValueError(
                        "legacy current-lineage embedded claim is invalid"
                    )
                document_id = str(claim.get("document_id") or "")
                if document_id not in call_document_ids:
                    raise ValueError(
                        "legacy current-lineage claim is outside its call"
                    )
                raw_objective_ids = claim.get("objective_ids") or ()
                if isinstance(raw_objective_ids, (str, bytes)) or not (
                    isinstance(raw_objective_ids, Sequence)
                ):
                    raise ValueError(
                        "legacy current-lineage claim objectives are invalid"
                    )
                objective_ids = {
                    str(value).strip() for value in raw_objective_ids
                }
                if "" in objective_ids:
                    raise ValueError(
                        "legacy current-lineage claim objective is empty"
                    )
                claimed_objective_ids_by_document.setdefault(
                    document_id,
                    set(),
                ).update(objective_ids)

        migrated_ids: list[str] = []
        for document_id, claimed_objective_ids in (
            claimed_objective_ids_by_document.items()
        ):
            document = document_by_id.get(document_id)
            if document is None:
                continue
            current_objective_ids = {
                str(value).strip()
                for value in document.get("objective_ids") or ()
                if str(value).strip()
            }
            historical_objective_ids = {
                str(value).strip()
                for value in document.get("historical_objective_ids") or ()
                if str(value).strip()
            }
            retired_claim_objective_ids = (
                claimed_objective_ids - current_objective_ids
            )
            if not retired_claim_objective_ids:
                continue
            if not retired_claim_objective_ids.issubset(
                historical_objective_ids
            ):
                raise ValueError(
                    "legacy current-lineage objective drift lacks explicit "
                    "historical lineage"
                )
            migrated_ids.append(document_id)
        call[
            "current_lineage_objective_reassessment_document_ids"
        ] = sorted(set(migrated_ids))
        reassessment_ids.update(migrated_ids)
        _coerce_provider_call(call)
    return tuple(sorted(reassessment_ids))


def _completed_current_semantics_coverage_audit_document_ids(
    *,
    provider_calls: Sequence[Mapping[str, Any]],
    document_dispositions: Sequence[Mapping[str, Any]],
) -> frozenset[str]:
    """Return only parents whose complete current-semantics audit is sealed."""

    nonsplit_ids: set[str] = set()
    audited_chunk_ids_by_document: dict[str, set[str]] = {}
    for raw_call in provider_calls:
        if (
            raw_call.get("status") != "COMPLETE"
            or raw_call.get("coverage_audit_performed") is not True
            or str(raw_call.get("extraction_semantics_version") or "")
            != FACT_EXTRACTION_SEMANTICS_VERSION
        ):
            continue
        call = _coerce_provider_call(raw_call)
        if not call.transport_chunk_ids:
            nonsplit_ids.update(call.document_ids)
            continue
        for document_id in call.document_ids:
            audited_chunk_ids_by_document.setdefault(
                document_id,
                set(),
            ).update(call.transport_chunk_ids)
    completed_ids = set(nonsplit_ids)
    for disposition in document_dispositions:
        document_id = str(disposition.get("document_id") or "")
        expected_chunk_ids = {
            str(value)
            for value in disposition.get("transport_chunk_ids") or ()
            if str(value)
        }
        if (
            document_id
            and expected_chunk_ids
            and disposition.get("all_transport_chunks_complete") is True
            and expected_chunk_ids.issubset(
                audited_chunk_ids_by_document.get(document_id, set())
            )
        ):
            completed_ids.add(document_id)
    return frozenset(completed_ids)


def _load_fact_checkpoint(
    root: Path,
    *,
    source_graph: SourceGraphAcquisitionRun,
    committed_fact_snapshot: Mapping[str, Any] | None = None,
) -> Mapping[str, Any]:
    paths = {key: root / value for key, value in FACT_EXTRACTION_OUTPUT_FILES.items()}
    required = (
        paths["accepted_claims"],
        paths["document_dispositions"],
        paths["provider_calls"],
        paths["rejections"],
    )
    if committed_fact_snapshot is None and not all(
        path.is_file() for path in required
    ):
        return {}
    if committed_fact_snapshot is not None and (
        str(committed_fact_snapshot.get("target_id") or "")
        != str(getattr(source_graph, "target_id", ""))
        or str(committed_fact_snapshot.get("as_of_date") or "")
        != str(getattr(source_graph, "as_of_date", ""))
    ):
        raise ValueError("committed fact snapshot target/date mismatch")
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
        for row in (
            tuple(committed_fact_snapshot.get("accepted_claims") or ())
            if committed_fact_snapshot is not None
            else _read_jsonl(paths["accepted_claims"])
        )
    )
    all_calls: list[Mapping[str, Any]] = []
    for raw_call in (
        tuple(committed_fact_snapshot.get("provider_calls") or ())
        if committed_fact_snapshot is not None
        else _read_jsonl(paths["provider_calls"])
    ):
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
    typed_current_lineage_reassessment_receipt_present = any(
        bool(call.get("current_lineage_request_ids"))
        and "current_lineage_objective_reassessment_document_ids"
        in call
        for call in all_calls
    )
    current_lineage_reassessment_receipt_ids = (
        _upgrade_current_lineage_objective_reassessment_receipts(
            all_calls,
            document_by_id=document_by_id,
        )
    )
    carried_coverage_refresh_document_ids: list[str] = []
    carried_current_lineage_objective_reassessment_document_ids: list[
        str
    ] = []
    audit_current_lineage_objective_reassessment_ids: tuple[str, ...] = ()
    prior_semantics_recovery_document_ids: tuple[str, ...] = ()
    prior_semantics_recovery_invalidated_claim_count = 0
    result_path = paths["result"]
    if committed_fact_snapshot is not None:
        prior_result = dict(committed_fact_snapshot.get("result") or {})
    elif result_path.is_file():
        try:
            prior_result = _read_json(result_path)
        except (OSError, UnicodeError, ValueError, json.JSONDecodeError):
            prior_result = {}
    else:
        prior_result = {}
    if prior_result:
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
                if (
                    "current_fact_lineage_objective_reassessment_document_ids"
                    in audit
                ):
                    audit_current_lineage_objective_reassessment_ids = tuple(
                        dict.fromkeys(
                            str(value)
                            for value in audit.get(
                                "current_fact_lineage_objective_reassessment_document_ids"
                            )
                            or ()
                            if str(value) in current_ids
                        )
                    )
                recovery_status = audit.get(
                    "semantics_migration_recovery_status"
                )
                legacy_bootstrap = recovery_status is None
                if legacy_bootstrap:
                    recovery_ids = tuple(
                        str(value)
                        for value in audit.get(
                            "boundary_context_reextraction_document_ids"
                        )
                        or ()
                        if str(value)
                    )
                    invalidated_claim_count = int(
                        audit.get(
                            "boundary_context_invalidated_prior_claim_count"
                        )
                        or 0
                    )
                    completed_reextraction_count = int(
                        audit.get(
                            "boundary_context_reextraction_completed_document_count"
                        )
                        or 0
                    )
                    selected_reextraction_count = int(
                        audit.get(
                            "boundary_context_reextraction_selected_document_count"
                        )
                        or 0
                    )
                elif recovery_status == "INCOMPLETE":
                    recovery_ids = tuple(
                        str(value)
                        for value in audit.get(
                            "pending_semantics_migration_recovery_document_ids"
                        )
                        or ()
                        if str(value)
                    )
                    invalidated_claim_count = int(
                        audit.get(
                            "pending_semantics_migration_recovery_expected_claim_count"
                        )
                        or 0
                    )
                    completed_reextraction_count = 0
                    selected_reextraction_count = len(recovery_ids)
                else:
                    recovery_ids = ()
                    invalidated_claim_count = 0
                    completed_reextraction_count = 0
                    selected_reextraction_count = 0
                if (
                    audit.get("extraction_semantics_version")
                    == FACT_EXTRACTION_SEMANTICS_VERSION
                    and recovery_status in {None, "INCOMPLETE"}
                    and (
                        recovery_status is None
                        or audit.get(
                            "semantics_migration_recovery_requested"
                        )
                        is True
                    )
                    and invalidated_claim_count > 0
                    and completed_reextraction_count == 0
                    and recovery_ids
                    and len(recovery_ids) == len(set(recovery_ids))
                    and selected_reextraction_count == len(recovery_ids)
                    and set(recovery_ids).issubset(current_ids)
                    and all(
                        str(
                            (document_by_id.get(document_id) or {}).get(
                                "source_family"
                            )
                            or ""
                        ).upper()
                        != "PUBLIC_BROKER_PDF"
                        for document_id in recovery_ids
                    )
                ):
                    prior_semantics_recovery_document_ids = recovery_ids
                    prior_semantics_recovery_invalidated_claim_count = (
                        invalidated_claim_count
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
    persisted_dispositions = (
        tuple(committed_fact_snapshot.get("document_dispositions") or ())
        if committed_fact_snapshot is not None
        else _read_jsonl(paths["document_dispositions"])
    )
    completed_current_lineage_reassessment_ids = (
        _completed_current_semantics_coverage_audit_document_ids(
            provider_calls=all_calls,
            document_dispositions=persisted_dispositions,
        )
    )
    if (
        typed_current_lineage_reassessment_receipt_present
        and not set(
            audit_current_lineage_objective_reassessment_ids
        ).issubset(current_lineage_reassessment_receipt_ids)
    ):
        raise ValueError(
            "fact objective reassessment audit is outside its typed receipts"
        )
    outstanding_current_lineage_reassessment_ids = set(
        current_lineage_reassessment_receipt_ids
    )
    if not outstanding_current_lineage_reassessment_ids:
        # Compatibility for the one legacy no-claim edge that cannot be
        # reconstructed from embedded accepted claims.  New recovery writes
        # always carry the typed provider-call receipt above.
        outstanding_current_lineage_reassessment_ids.update(
            audit_current_lineage_objective_reassessment_ids
        )
    outstanding_current_lineage_reassessment_ids.intersection_update(
        current_ids
    )
    outstanding_current_lineage_reassessment_ids.difference_update(
        completed_current_lineage_reassessment_ids
    )
    carried_current_lineage_objective_reassessment_document_ids.extend(
        sorted(outstanding_current_lineage_reassessment_ids)
    )
    carried_coverage_refresh_document_ids.extend(
        sorted(outstanding_current_lineage_reassessment_ids)
    )
    completed_ids = completed_call_ids & {
        str(row.get("document_id") or "")
        for row in persisted_dispositions
        if str(row.get("document_id") or "") in current_ids
    }
    # The writer commits several canonical files before its result audit.  If
    # it is interrupted in that window, a subset of recovered rows may already
    # be visible while the old recovery intent is still authoritative.  Drop
    # the whole intent roster from ordinary resume projection and rebuild it
    # from the immutable journal, preserving all-or-nothing recovery.
    completed_ids.difference_update(
        prior_semantics_recovery_document_ids
    )
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
        and not (
            set(row.get("document_ids") or ())
            & set(prior_semantics_recovery_document_ids)
        )
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
        for row in (
            tuple(committed_fact_snapshot.get("rejections") or ())
            if committed_fact_snapshot is not None
            else _read_jsonl(paths["rejections"])
        )
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
        "prior_current_lineage_objective_reassessment_document_ids": tuple(
            dict.fromkeys(
                carried_current_lineage_objective_reassessment_document_ids
            )
        ),
        "prior_semantics_recovery_document_ids": (
            prior_semantics_recovery_document_ids
        ),
        "prior_semantics_recovery_invalidated_claim_count": (
            prior_semantics_recovery_invalidated_claim_count
        ),
    }


def _authoritative_fact_recovery_extract_kwargs(
    *,
    root: Path,
    authoritative_fact_context: Mapping[str, Any] | None,
    target: CurrentResearchTarget,
    archetype_id: str,
    as_of_date: str,
    documents: Sequence[Mapping[str, Any]],
    open_objectives: Sequence[Mapping[str, Any]],
    current_facts: Sequence[Mapping[str, Any]],
    score_gap_context: Mapping[str, Any],
    prior_fact: Mapping[str, Any],
    extraction_mode: str,
) -> Mapping[str, Any]:
    """Seal an authority-loss replay to its exact validated journal calls."""

    if not (
        authoritative_fact_context
        and authoritative_fact_context.get(
            "authoritative_fact_lineage_recovery_required"
        )
        is True
    ):
        return {}
    ledger = authoritative_fact_context.get("authoritative_fact_ledger")
    expectation = authoritative_fact_context.get(
        "authoritative_recovery_expectation"
    )
    pending_new_fact_ids = tuple(
        authoritative_fact_context.get("pending_new_fact_ids") or ()
    )
    if (
        ledger is None
        or not isinstance(expectation, Mapping)
        or expectation.get("status")
        not in {
            "AUTHORITY_LOSS_RECOVERY_REQUIRED",
            "AUTHORITY_LOSS_RECOVERY_WITH_PENDING_NEW_REQUIRED",
        }
    ):
        raise ValueError("authoritative fact recovery context is inconsistent")
    try:
        binding = resolve_current_fact_lineage_recovery_binding(
            authoritative_fact_ledger=ledger,
            journal_root=root / "collaboration_codex_subagent_provider",
            target_id=target.target_id,
            target_name=target.company_name,
            target_aliases=target.aliases,
            archetype_id=archetype_id,
            as_of_date=as_of_date,
            documents=documents,
            open_objectives=open_objectives,
            current_facts=current_facts,
            score_gap_context=score_gap_context,
            prior_material_claims=tuple(
                prior_fact.get("prior_material_claims") or ()
            ),
            prior_document_dispositions=tuple(
                prior_fact.get("prior_document_dispositions") or ()
            ),
            extraction_mode=extraction_mode,
            pending_new_fact_ids=pending_new_fact_ids,
        )
    except (
        FileNotFoundError,
        OSError,
        KeyError,
        TypeError,
        ValueError,
        RuntimeError,
        json.JSONDecodeError,
    ):
        # The extractor owns the public checkpoint schema.  Handing it the
        # validated ledger without a binding yields a deterministic
        # CURRENT_FACT_LINEAGE_RECOVERY_BINDING_REQUIRED PENDING result and,
        # importantly, keeps its ordinary provider batches closed.
        return {"authoritative_fact_ledger": ledger}
    expected_source_ids = tuple(
        sorted(
            str(value)
            for value in expectation.get(
                "expected_recovered_source_document_ids"
            )
            or ()
        )
    )
    if (
        tuple(sorted(binding.seed_source_document_ids))
        != expected_source_ids
        or tuple(sorted(binding.pending_new_fact_ids))
        != tuple(sorted(pending_new_fact_ids))
    ):
        raise ValueError("authoritative fact journal binding widened its seed")
    return {
        "authoritative_fact_ledger": ledger,
        "current_fact_lineage_recovery_binding": binding,
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

    if (
        SourceGraphAcquisitionMode(config.source_acquisition_mode)
        != SourceGraphAcquisitionMode.PRODUCTION_DAILY
    ):
        raise ValueError(
            "fact recovery is restricted to production daily checkpoints"
        )
    root = Path(config.output_root) / target.symbol
    source_checkpoint_path = root / "source_graph_checkpoint.json"
    if not source_checkpoint_path.is_file():
        raise ValueError("fact recovery requires a source graph checkpoint")
    _configure_provider_response_cache(provider, root)

    anchors = _historical_anchors(
        repo_root=repo_root,
        archetype_id=config.archetype_id,
    )
    initial_plans = _initial_component_research_plans(
        target_id=target.target_id,
        archetype_id=config.archetype_id,
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
    authoritative_fact_context = _load_authoritative_prior_fact_context(
        root,
        target_id=target.target_id,
        as_of_date=config.as_of_date,
        source_checkpoint=checkpoint,
    )
    authoritative_fact_lineage_recovery_required = bool(
        authoritative_fact_context
        and authoritative_fact_context.get(
            "authoritative_fact_lineage_recovery_required"
        )
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
            not authoritative_fact_lineage_recovery_required
            and _source_checkpoint_needs_fact_extraction_recovery(
                root=root,
                checkpoint=checkpoint,
                target_id=target.target_id,
                as_of_date=config.as_of_date,
            )
        ),
        authoritative_fact_lineage_recovery=(
            authoritative_fact_context
            if authoritative_fact_lineage_recovery_required
            else None
        ),
    )
    prior_context = _load_prior_research_context(
        root,
        target_id=target.target_id,
        as_of_date=config.as_of_date,
        objectives=objective_rows,
        archetype_id=config.archetype_id,
        authoritative_fact_context=authoritative_fact_context,
    )
    prior_fact = _load_fact_checkpoint(
        root,
        source_graph=source_graph,
        committed_fact_snapshot=(
            authoritative_fact_context.get("committed_fact_result_snapshot")
            if authoritative_fact_context is not None
            else None
        ),
    )
    extractor = ResearcherEvidenceFactExtractor(
        provider=provider,
        documents_per_call=config.fact_documents_per_call,
        max_document_chars_per_call=int(
            getattr(
                provider,
                "semantic_prompt_chunk_chars",
                220_000,
            )
        ),
    )
    fact_score_gap_context = {
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
    }
    authoritative_fact_recovery_kwargs = (
        _authoritative_fact_recovery_extract_kwargs(
            root=root,
            authoritative_fact_context=authoritative_fact_context,
            target=target,
            archetype_id=config.archetype_id,
            as_of_date=config.as_of_date,
            documents=source_graph.evidence_documents,
            open_objectives=objective_rows,
            current_facts=prior_context["facts"],
            score_gap_context=fact_score_gap_context,
            prior_fact=prior_fact,
            extraction_mode="PRODUCTION_OBJECTIVE_LOCAL",
        )
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
        score_gap_context=fact_score_gap_context,
        extraction_mode="PRODUCTION_OBJECTIVE_LOCAL",
        **authoritative_fact_recovery_kwargs,
        **prior_fact,
    )
    write_researcher_fact_extraction_result(result, root)
    return result


def _fact_extraction_is_complete_for_source_checkpoint(
    *,
    fact_result: Mapping[str, Any],
    source_checkpoint: Mapping[str, Any],
    target_id: str,
    as_of_date: str,
) -> bool:
    """Bind fact completion to the exact current production document roster."""

    if (
        str(source_checkpoint.get("target_id") or "") != target_id
        or str(source_checkpoint.get("as_of_date") or "") != as_of_date
        or str(fact_result.get("target_id") or "") != target_id
        or str(fact_result.get("as_of_date") or "") != as_of_date
        or fact_result.get("status") != "FACT_EXTRACTION_COMPLETE"
    ):
        return False
    audit = fact_result.get("audit") or {}
    if (
        not isinstance(audit, Mapping)
        or int(audit.get("critical_count_sum") or 0) != 0
    ):
        return False
    raw_document_ids = source_checkpoint.get(
        "production_downstream_document_ids"
    )
    if not isinstance(raw_document_ids, (list, tuple)):
        return False
    document_ids = tuple(str(value or "").strip() for value in raw_document_ids)
    if (
        any(not value for value in document_ids)
        or len(document_ids) != len(set(document_ids))
    ):
        return False
    raw_dispositions = fact_result.get("document_dispositions")
    if not isinstance(raw_dispositions, (list, tuple)) or any(
        not isinstance(row, Mapping) for row in raw_dispositions
    ):
        return False
    disposition_ids = tuple(
        str(row.get("document_id") or "").strip()
        for row in raw_dispositions
    )
    return bool(
        not any(not value for value in disposition_ids)
        and len(disposition_ids) == len(set(disposition_ids))
        and set(disposition_ids) == set(document_ids)
        and len(disposition_ids) == len(document_ids)
        and int(audit.get("input_document_count") or 0)
        == len(document_ids)
    )


def _canonical_json_payload(value: Any) -> str:
    """Return one strict RFC-8259-compatible JSON identity."""

    try:
        return json.dumps(
            value,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        )
    except (TypeError, ValueError) as exc:
        raise ValueError("checkpoint payload is not canonical JSON") from exc


def _canonical_fact_payload(row: Mapping[str, Any]) -> str:
    """Return the strict JSON identity used to join fact authority planes."""

    return _canonical_json_payload(dict(row))


def _strict_jsonl_objects(path: Path, *, label: str) -> tuple[Mapping[str, Any], ...]:
    if not path.is_file():
        raise ValueError(f"committed fact checkpoint lacks {label}")
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError) as exc:
        raise ValueError(f"cannot read committed fact {label}") from exc
    if any(not line.strip() for line in lines):
        raise ValueError(f"committed fact {label} has a blank row")
    rows: list[Mapping[str, Any]] = []
    for line in lines:
        try:
            value = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(
                f"committed fact {label} contains invalid JSON"
            ) from exc
        if not isinstance(value, Mapping):
            raise ValueError(f"committed fact {label} contains a non-object")
        _canonical_json_payload(value)
        rows.append(dict(value))
    return tuple(rows)


def _embedded_mapping_rows(
    value: Any,
    *,
    label: str,
) -> tuple[Mapping[str, Any], ...]:
    if isinstance(value, (str, bytes)) or not isinstance(value, Sequence):
        raise ValueError(f"fact result embedded {label} must be an array")
    rows = tuple(dict(row) for row in value if isinstance(row, Mapping))
    if len(rows) != len(value):
        raise ValueError(f"fact result embedded {label} contains a non-object")
    _canonical_json_payload(rows)
    return rows


def _load_committed_fact_result_snapshot(
    root: Path,
    *,
    target_id: str,
    as_of_date: str,
) -> Mapping[str, Any]:
    """Project only the result-last fact generation, never mixed new leaves.

    The writer replaces six JSONL leaves and the standalone audit before it
    replaces ``fact_extraction_result.json``.  A crash can therefore expose,
    for example, a new 499-fact leaf beside the older 457-fact result marker.
    The marker's embedded rows remain the committed generation; mismatching
    leaves are repair work and must not silently become the next input.
    """

    result_path = root / FACT_EXTRACTION_OUTPUT_FILES["result"]
    if not result_path.is_file():
        raise ValueError(
            "authoritative fact ledger requires a result-last fact checkpoint"
        )
    result = _read_json(result_path)
    if (
        str(result.get("target_id") or "") != target_id
        or str(result.get("as_of_date") or "") != as_of_date
    ):
        raise ValueError("fact result commit marker target/date mismatch")
    compilation = result.get("fact_compilation")
    audit = result.get("audit")
    if not isinstance(compilation, Mapping) or not isinstance(audit, Mapping):
        raise ValueError("fact result commit marker is incomplete")
    embedded = {
        "accepted_claims": _embedded_mapping_rows(
            result.get("material_claims"),
            label="material claims",
        ),
        "rejections": _embedded_mapping_rows(
            result.get("rejections"),
            label="rejections",
        ),
        "document_dispositions": _embedded_mapping_rows(
            result.get("document_dispositions"),
            label="document dispositions",
        ),
        "provider_calls": _embedded_mapping_rows(
            result.get("provider_calls"),
            label="provider calls",
        ),
        "facts": _validated_fact_rows(
            compilation.get("facts"),
            target_id=target_id,
            as_of_date=as_of_date,
            label="fact result compiled roster",
        ),
        "claim_fact_links": _embedded_mapping_rows(
            compilation.get("claim_fact_links"),
            label="claim/fact links",
        ),
    }
    for row in embedded["provider_calls"]:
        _coerce_provider_call(row)
    for row in embedded["rejections"]:
        _coerce_rejection(row)
    disposition_ids = tuple(
        str(row.get("document_id") or "").strip()
        for row in embedded["document_dispositions"]
    )
    if (
        any(not value for value in disposition_ids)
        or len(disposition_ids) != len(set(disposition_ids))
    ):
        raise ValueError(
            "fact result embedded document dispositions are not unique"
        )
    recomputed = EvidenceFactCompiler().compile(
        target_id=target_id,
        as_of_date=as_of_date,
        accepted_claims=embedded["accepted_claims"],
    )
    if (
        _canonical_json_payload(
            tuple(row.to_dict() for row in recomputed.facts)
        )
        != _canonical_json_payload(embedded["facts"])
        or _canonical_json_payload(
            tuple(row.to_dict() for row in recomputed.claim_fact_links)
        )
        != _canonical_json_payload(embedded["claim_fact_links"])
    ):
        raise ValueError(
            "fact result embedded compiler projection is inconsistent"
        )

    leaf_mismatches: list[str] = []
    for key in (
        "accepted_claims",
        "rejections",
        "document_dispositions",
        "provider_calls",
        "facts",
        "claim_fact_links",
    ):
        leaf_rows = _strict_jsonl_objects(
            root / FACT_EXTRACTION_OUTPUT_FILES[key],
            label=key,
        )
        if _canonical_json_payload(leaf_rows) != _canonical_json_payload(
            embedded[key]
        ):
            leaf_mismatches.append(key)
    audit_path = root / FACT_EXTRACTION_OUTPUT_FILES["audit"]
    if not audit_path.is_file() or _canonical_json_payload(
        _read_json(audit_path) if audit_path.is_file() else None
    ) != _canonical_json_payload(dict(audit)):
        leaf_mismatches.append("audit")
    counterfacts = tuple(
        row
        for row in embedded["facts"]
        if str(row.get("direction") or "") == EvidenceDirection.COUNTER.value
    )
    counterfact_path = root / "counterfacts.jsonl"
    if (
        not counterfact_path.is_file()
        or _canonical_json_payload(
            _strict_jsonl_objects(counterfact_path, label="counterfacts")
        )
        != _canonical_json_payload(counterfacts)
    ):
        leaf_mismatches.append("counterfacts")
    return {
        "schema_version": "e2r_v5_result_last_fact_snapshot_v1",
        "target_id": target_id,
        "as_of_date": as_of_date,
        "result": dict(result),
        "audit": dict(audit),
        **embedded,
        "leaf_commit_complete": not leaf_mismatches,
        "atomic_snapshot_repair_required": bool(leaf_mismatches),
        "leaf_mismatch_names": tuple(leaf_mismatches),
        "production_score_authority": False,
    }


def _repair_fact_checkpoint_leaves_from_result_snapshot(
    root: Path,
    *,
    snapshot: Mapping[str, Any],
) -> None:
    """Atomically restore every derived leaf from the result-last marker."""

    if snapshot.get("atomic_snapshot_repair_required") is not True:
        return
    result = snapshot.get("result")
    audit = snapshot.get("audit")
    if not isinstance(result, Mapping) or not isinstance(audit, Mapping):
        raise ValueError("fact result repair snapshot is incomplete")
    result_path = root / FACT_EXTRACTION_OUTPUT_FILES["result"]
    if _canonical_json_payload(_read_json(result_path)) != (
        _canonical_json_payload(dict(result))
    ):
        raise ValueError("fact result commit marker changed before leaf repair")
    jsonl_rows = {
        key: tuple(snapshot.get(key) or ())
        for key in (
            "accepted_claims",
            "rejections",
            "document_dispositions",
            "provider_calls",
            "facts",
            "claim_fact_links",
        )
    }
    jsonl_rows["counterfacts"] = tuple(
        row
        for row in jsonl_rows["facts"]
        if str(row.get("direction") or "") == EvidenceDirection.COUNTER.value
    )
    destinations = {
        **{
            key: root / FACT_EXTRACTION_OUTPUT_FILES[key]
            for key in (
                "accepted_claims",
                "rejections",
                "document_dispositions",
                "provider_calls",
                "facts",
                "claim_fact_links",
            )
        },
        "counterfacts": root / "counterfacts.jsonl",
        "audit": root / FACT_EXTRACTION_OUTPUT_FILES["audit"],
    }
    serialized = {
        destinations[key]: "".join(
            json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n"
            for row in rows
        )
        for key, rows in jsonl_rows.items()
    }
    serialized[destinations["audit"]] = (
        json.dumps(dict(audit), ensure_ascii=False, indent=2, sort_keys=True)
        + "\n"
    )
    temporary_paths: dict[Path, Path] = {}
    try:
        for destination, content in serialized.items():
            descriptor, temporary_name = tempfile.mkstemp(
                prefix=f".{destination.name}.",
                suffix=".repair.tmp",
                dir=root,
            )
            temporary_path = Path(temporary_name)
            temporary_paths[destination] = temporary_path
            with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
                handle.write(content)
                handle.flush()
                os.fsync(handle.fileno())
        if _canonical_json_payload(_read_json(result_path)) != (
            _canonical_json_payload(dict(result))
        ):
            raise ValueError("fact result commit marker changed during leaf repair")
        directory_descriptor = os.open(root, os.O_RDONLY)
        try:
            for destination in serialized:
                os.replace(temporary_paths.pop(destination), destination)
            os.fsync(directory_descriptor)
        finally:
            os.close(directory_descriptor)
        if _canonical_json_payload(_read_json(result_path)) != (
            _canonical_json_payload(dict(result))
        ):
            raise ValueError("fact result commit marker changed after leaf repair")
    finally:
        for temporary_path in temporary_paths.values():
            try:
                temporary_path.unlink()
            except FileNotFoundError:
                pass


def _validated_fact_rows(
    values: Sequence[Any],
    *,
    target_id: str,
    as_of_date: str,
    label: str,
) -> tuple[Mapping[str, Any], ...]:
    if isinstance(values, (str, bytes)) or not isinstance(values, Sequence):
        raise ValueError(f"{label} must be a JSON row sequence")
    rows: list[Mapping[str, Any]] = []
    fact_ids: list[str] = []
    for value in values:
        if not isinstance(value, Mapping):
            raise ValueError(f"{label} contains a non-object fact row")
        row = dict(value)
        fact_id = str(row.get("fact_id") or "").strip()
        if (
            not fact_id
            or str(row.get("target_id") or "") != target_id
            or str(row.get("as_of_date") or "") != as_of_date
        ):
            raise ValueError(f"{label} fact identity is invalid")
        _canonical_fact_payload(row)
        rows.append(row)
        fact_ids.append(fact_id)
    if len(fact_ids) != len(set(fact_ids)):
        raise ValueError(f"{label} fact ids are duplicated")
    return tuple(rows)


def _source_checkpoint_downstream_document_ids(
    checkpoint: Mapping[str, Any],
) -> tuple[str, ...]:
    raw = checkpoint.get("production_downstream_document_ids")
    if isinstance(raw, (str, bytes)) or not isinstance(raw, Sequence):
        raise ValueError(
            "authoritative fact recovery requires a downstream source roster"
        )
    result = tuple(str(value or "").strip() for value in raw)
    evidence_ids = {
        str(row.get("document_id") or "").strip()
        for row in checkpoint.get("evidence_documents") or ()
        if isinstance(row, Mapping)
        and str(row.get("document_id") or "").strip()
    }
    if (
        not result
        or any(not value for value in result)
        or len(result) != len(set(result))
        or not set(result).issubset(evidence_ids)
    ):
        raise ValueError(
            "authoritative fact recovery source roster binding is invalid"
        )
    return result


_FACT_COMPILER_ADDITIVE_FIELDS = frozenset(
    {
        "claim_ids",
        "source_ids",
        "quote_ids",
        "corroborating_independence_groups",
        "source_independence_group",
        "confidence",
    }
)


def _fact_lineage_values(
    row: Mapping[str, Any],
    field: str,
    *,
    allow_empty: bool = False,
) -> tuple[str, ...]:
    raw = row.get(field)
    if isinstance(raw, (str, bytes)) or not isinstance(raw, Sequence):
        raise ValueError(f"fact {field} lineage must be an array")
    values = tuple(str(value or "").strip() for value in raw)
    if (
        any(not value for value in values)
        or len(values) != len(set(values))
        or (not allow_empty and not values)
    ):
        raise ValueError(f"fact {field} lineage is invalid")
    return values


def _compiler_claim_quote_ids(row: Mapping[str, Any]) -> frozenset[str]:
    raw = row.get("quote_ids")
    if raw is None and row.get("quote_id"):
        raw = [row.get("quote_id")]
    if raw:
        return frozenset(
            _fact_lineage_values({"quote_ids": raw}, "quote_ids")
        )
    claim_id = str(row.get("claim_id") or "").strip()
    source_ids = _fact_lineage_values(row, "source_ids")
    exact_quote = str(
        row.get("exact_quote") or row.get("quote_text") or ""
    ).strip()
    if not claim_id or not exact_quote:
        raise ValueError("fact addition claim quote lineage is incomplete")
    return frozenset(
        {
            stable_intelligence_id(
                "QUOTE",
                {
                    "claim_id": claim_id,
                    "source_ids": list(source_ids),
                    "quote_text": exact_quote,
                },
            )
        }
    )


def _fact_result_is_bound_to_source_checkpoint(
    *,
    result: Mapping[str, Any],
    source_checkpoint: Mapping[str, Any],
    target_id: str,
    as_of_date: str,
) -> bool:
    status = str(result.get("status") or "")
    if status == "FACT_EXTRACTION_COMPLETE":
        return _fact_extraction_is_complete_for_source_checkpoint(
            fact_result=result,
            source_checkpoint=source_checkpoint,
            target_id=target_id,
            as_of_date=as_of_date,
        )
    if status != "FACT_EXTRACTION_PENDING":
        return False
    downstream_ids = _source_checkpoint_downstream_document_ids(
        source_checkpoint
    )
    audit = result.get("audit") or {}
    return bool(
        fact_extraction_has_exact_checkpoint_recovery_wait(
            result.get("pending_reasons") or ()
        )
        and isinstance(audit, Mapping)
        and int(audit.get("input_document_count") or 0)
        == len(downstream_ids)
    )


def _validated_official_fact_journal_payloads(
    root: Path,
    *,
    required_lineages: Sequence[tuple[str, str]],
) -> Mapping[tuple[str, str], Mapping[str, Any]]:
    """Open only exact current fact request/response receipts.

    Historical journals can contain requests for schemas that are no longer
    accepted by the current bridge.  They are irrelevant here.  We first
    project the stable FACTPROMPT identity and then fully validate only the
    exact prompt/response lineages claimed by the committed fact generation.
    """

    required = frozenset(
        (str(prompt_hash), str(response_hash))
        for prompt_hash, response_hash in required_lineages
    )
    if not required:
        return {}
    if any(
        not prompt_hash.startswith("FACTPROMPT-")
        or not response_hash.startswith("FACTRESP-")
        for prompt_hash, response_hash in required
    ):
        raise ValueError("fact addition journal lineage identity is invalid")
    journal_root = root / "collaboration_codex_subagent_provider"
    request_root = journal_root / "requests"
    response_root = journal_root / "responses"
    if not request_root.is_dir() or not response_root.is_dir():
        raise ValueError("fact additions require the official Collaboration journal")
    required_prompt_hashes = {value[0] for value in required}
    found: dict[tuple[str, str], Mapping[str, Any]] = {}
    for request_path in sorted(request_root.glob("COLLABREQ-*.json")):
        raw_request = _read_json(request_path)
        if raw_request.get("pass_name") != "EVIDENCE_FACT_EXTRACTION":
            continue
        prompt = raw_request.get("prompt")
        if not isinstance(prompt, str) or not prompt:
            continue
        try:
            request_payload = json.loads(prompt.rsplit("\n", 1)[-1])
        except (TypeError, ValueError, json.JSONDecodeError):
            continue
        if not isinstance(request_payload, Mapping):
            continue
        prompt_hash = stable_intelligence_id(
            "FACTPROMPT", request_payload
        )
        if prompt_hash not in required_prompt_hashes:
            continue
        request = validate_collaboration_request(raw_request)
        request_id = str(request["request_id"])
        if request_path.name != f"{request_id}.json":
            raise ValueError("fact addition request filename identity mismatch")
        response_path = response_root / f"{request_id}.json"
        if not response_path.is_file():
            continue
        response = validate_collaboration_response_envelope(
            request=request,
            envelope=_read_json(response_path),
        )
        response_payload = response.get("payload")
        if not isinstance(response_payload, Mapping):
            raise ValueError("fact addition response payload is invalid")
        response_hash = stable_intelligence_id(
            "FACTRESP",
            scrub_blind_research_payload(response_payload),
        )
        lineage = (prompt_hash, response_hash)
        if lineage not in required:
            continue
        quarantine_path = (
            journal_root
            / "quarantine"
            / request_id
            / f"{response['response_id']}.json"
        )
        if quarantine_path.is_file():
            raise ValueError("fact addition response receipt is quarantined")
        if lineage in found:
            raise ValueError("fact addition journal lineage is ambiguous")
        found[lineage] = dict(response_payload)
    if set(found) != set(required):
        raise ValueError("fact addition lacks an exact official imported receipt")
    return found


def _attested_compiler_fact_addition_ids(
    *,
    root: Path,
    target_id: str,
    as_of_date: str,
    source_checkpoint: Mapping[str, Any],
    authority_by_id: Mapping[str, Mapping[str, Any]],
    convenience_rows: Sequence[Mapping[str, Any]],
    enriched_fact_ids: Sequence[str],
    pending_new_fact_ids: Sequence[str],
    committed_snapshot: Mapping[str, Any],
) -> tuple[str, ...]:
    """Attest compiler-owned additive changes without weakening epoch authority.

    An epoch fact may gain corroboration before the next epoch commit, but no
    authority-owned semantic or evidence field may disappear.  Every added
    claim is rebuilt from one validated Collaboration response, checked against
    its exact current source document, and then compiled again with the entire
    committed claim roster.  This makes enrichment monotonic and all-or-none.
    """

    enriched = tuple(sorted(str(value) for value in enriched_fact_ids))
    pending_new = tuple(sorted(str(value) for value in pending_new_fact_ids))
    addition_fact_ids = frozenset((*enriched, *pending_new))
    if not addition_fact_ids:
        return ()
    if committed_snapshot.get("leaf_commit_complete") is not True:
        raise ValueError("fact additions require a fully committed fact snapshot")
    result = committed_snapshot.get("result")
    if (
        not isinstance(result, Mapping)
        or str(result.get("target_id") or "") != target_id
        or str(result.get("as_of_date") or "") != as_of_date
        or not _fact_result_is_bound_to_source_checkpoint(
            result=result,
            source_checkpoint=source_checkpoint,
            target_id=target_id,
            as_of_date=as_of_date,
        )
    ):
        raise ValueError("fact additions are not bound to the current source checkpoint")

    convenience_by_id = {
        str(row["fact_id"]): dict(row) for row in convenience_rows
    }
    snapshot_fact_rows = tuple(committed_snapshot.get("facts") or ())
    snapshot_by_id = {
        str(row.get("fact_id") or ""): dict(row)
        for row in snapshot_fact_rows
        if isinstance(row, Mapping)
    }
    if (
        len(snapshot_by_id) != len(snapshot_fact_rows)
        or set(snapshot_by_id) != set(convenience_by_id)
        or any(
            _canonical_fact_payload(snapshot_by_id[fact_id])
            != _canonical_fact_payload(convenience_by_id[fact_id])
            for fact_id in snapshot_by_id
        )
    ):
        raise ValueError("fact additions do not match the result-last fact roster")

    accepted_claims = tuple(committed_snapshot.get("accepted_claims") or ())
    if any(not isinstance(row, Mapping) for row in accepted_claims):
        raise ValueError("fact addition claim roster is invalid")
    claim_by_id = {
        str(row.get("claim_id") or ""): dict(row)
        for row in accepted_claims
        if isinstance(row, Mapping) and str(row.get("claim_id") or "")
    }
    if len(claim_by_id) != len(accepted_claims):
        raise ValueError("fact addition claim ids are missing or duplicated")
    recomputed = EvidenceFactCompiler().compile(
        target_id=target_id,
        as_of_date=as_of_date,
        accepted_claims=accepted_claims,
    )
    recomputed_fact_rows = tuple(row.to_dict() for row in recomputed.facts)
    recomputed_link_rows = tuple(
        row.to_dict() for row in recomputed.claim_fact_links
    )
    snapshot_links = tuple(committed_snapshot.get("claim_fact_links") or ())
    if (
        recomputed.status != "FACT_COMPILATION_COMPLETE"
        or not recomputed.fact_graph_ready
        or _canonical_json_payload(recomputed_fact_rows)
        != _canonical_json_payload(snapshot_fact_rows)
        or _canonical_json_payload(recomputed_link_rows)
        != _canonical_json_payload(snapshot_links)
    ):
        raise ValueError("fact additions fail exact compiler replay")
    link_by_claim_id = {
        str(row.get("claim_id") or ""): dict(row)
        for row in snapshot_links
        if isinstance(row, Mapping) and str(row.get("claim_id") or "")
    }
    if len(link_by_claim_id) != len(snapshot_links):
        raise ValueError("fact addition claim/fact links are ambiguous")

    added_claim_ids_by_fact: dict[str, frozenset[str]] = {}
    for fact_id in pending_new:
        current = convenience_by_id.get(fact_id)
        if current is None:
            raise ValueError("pending-new fact addition is absent")
        added_claim_ids_by_fact[fact_id] = frozenset(
            _fact_lineage_values(current, "claim_ids")
        )
    for fact_id in enriched:
        old = authority_by_id.get(fact_id)
        current = convenience_by_id.get(fact_id)
        if old is None or current is None:
            raise ValueError("enriched fact is absent from an authority plane")
        old_stable = {
            key: value
            for key, value in old.items()
            if key not in _FACT_COMPILER_ADDITIVE_FIELDS
        }
        current_stable = {
            key: value
            for key, value in current.items()
            if key not in _FACT_COMPILER_ADDITIVE_FIELDS
        }
        if _canonical_json_payload(old_stable) != _canonical_json_payload(
            current_stable
        ):
            raise ValueError("enriched fact changed immutable semantic metadata")
        old_claim_ids = frozenset(
            _fact_lineage_values(old, "claim_ids")
        )
        current_claim_ids = frozenset(
            _fact_lineage_values(current, "claim_ids")
        )
        added_claim_ids = current_claim_ids - old_claim_ids
        if not added_claim_ids or not old_claim_ids.issubset(current_claim_ids):
            raise ValueError("enriched fact did not preserve exact claim lineage")
        added_claim_ids_by_fact[fact_id] = added_claim_ids
        for field in (
            "source_ids",
            "quote_ids",
            "corroborating_independence_groups",
        ):
            old_values = frozenset(_fact_lineage_values(old, field))
            current_values = frozenset(
                _fact_lineage_values(current, field)
            )
            if not old_values.issubset(current_values):
                raise ValueError(f"enriched fact removed authority {field}")
        old_confidence = float(old.get("confidence"))
        current_confidence = float(current.get("confidence"))
        if current_confidence + 1e-12 < old_confidence:
            raise ValueError("enriched fact confidence regressed")

    added_claim_ids = frozenset(
        claim_id
        for values in added_claim_ids_by_fact.values()
        for claim_id in values
    )
    if not added_claim_ids or any(
        claim_id not in claim_by_id or claim_id not in link_by_claim_id
        for claim_id in added_claim_ids
    ):
        raise ValueError("fact addition claim/link coverage is incomplete")

    downstream_ids = frozenset(
        _source_checkpoint_downstream_document_ids(source_checkpoint)
    )
    document_by_id = {
        str(row.get("document_id") or ""): dict(row)
        for row in source_checkpoint.get("evidence_documents") or ()
        if isinstance(row, Mapping) and str(row.get("document_id") or "")
    }
    cutoff = date.fromisoformat(as_of_date)
    provider_calls = tuple(
        _coerce_provider_call(row)
        for row in committed_snapshot.get("provider_calls") or ()
    )
    required_lineages: set[tuple[str, str]] = set()
    for fact_id, fact_claim_ids in added_claim_ids_by_fact.items():
        current = convenience_by_id[fact_id]
        added_claim_rows = tuple(claim_by_id[value] for value in fact_claim_ids)
        added_sources = {
            source_id
            for row in added_claim_rows
            for source_id in _fact_lineage_values(row, "source_ids")
        }
        added_quotes = {
            quote_id
            for row in added_claim_rows
            for quote_id in _compiler_claim_quote_ids(row)
        }
        added_groups = {
            str(row.get("source_independence_group") or "").strip()
            for row in added_claim_rows
            if str(row.get("source_independence_group") or "").strip()
        }
        if not added_sources or not added_sources.issubset(downstream_ids):
            raise ValueError("fact addition source is outside the current roster")
        if fact_id in enriched:
            old = authority_by_id[fact_id]
            old_sources = set(_fact_lineage_values(old, "source_ids"))
            current_sources = set(
                _fact_lineage_values(current, "source_ids")
            )
            if current_sources != old_sources | added_sources:
                raise ValueError("enriched fact source union is not additive")
            old_quotes = set(_fact_lineage_values(old, "quote_ids"))
            current_quotes = set(_fact_lineage_values(current, "quote_ids"))
            if current_quotes != old_quotes | added_quotes:
                raise ValueError("enriched fact quote union is not additive")
            old_groups = set(
                _fact_lineage_values(
                    old, "corroborating_independence_groups"
                )
            )
            current_groups = set(
                _fact_lineage_values(
                    current, "corroborating_independence_groups"
                )
            )
            if current_groups != old_groups | added_groups:
                raise ValueError(
                    "enriched fact independence-group union is not additive"
                )
        for claim in added_claim_rows:
            document_id = str(claim.get("document_id") or "").strip()
            source_ids = frozenset(
                _fact_lineage_values(claim, "source_ids")
            )
            document = document_by_id.get(document_id)
            exact_quote = str(claim.get("exact_quote") or "").strip()
            content = str((document or {}).get("content_text") or "")
            try:
                published = date.fromisoformat(
                    str((document or {}).get("published_at") or "")[:10]
                )
                available = date.fromisoformat(
                    str((document or {}).get("available_at") or "")[:10]
                )
            except ValueError as exc:
                raise ValueError(
                    "fact addition source date is invalid"
                ) from exc
            if (
                document is None
                or source_ids != {document_id}
                or document_id not in downstream_ids
                or str(claim.get("target_id") or "") != target_id
                or str(claim.get("as_of_date") or "") != as_of_date
                or str(document.get("target_id") or "") != target_id
                or str(document.get("as_of_date") or "") != as_of_date
                or not exact_quote
                or exact_quote not in content
                or hashlib.sha256(content.encode("utf-8")).hexdigest()
                != str(document.get("content_hash") or "")
                or str(claim.get("canonical_url") or "")
                != str(document.get("canonical_url") or "")
                or str(claim.get("published_at") or "")
                != str(document.get("published_at") or "")
                or str(claim.get("available_at") or "")
                != str(document.get("available_at") or "")
                or str(claim.get("source_independence_group") or "")
                != str(document.get("source_independence_group") or "")
                or published > cutoff
                or available > cutoff
            ):
                raise ValueError("fact addition claim/source provenance drift")
            prompt_hash = str(claim.get("provider_prompt_hash") or "")
            response_hash = str(claim.get("provider_response_hash") or "")
            required_lineages.add((prompt_hash, response_hash))
            matching_calls = tuple(
                call
                for call in provider_calls
                if claim["claim_id"] in call.accepted_claim_ids
                and call.status == "COMPLETE"
                and call.provider_attempt_count == 1
                and call.provider_name == COLLABORATION_PROVIDER_NAME
                and call.prompt_hash == prompt_hash
                and call.response_hash == response_hash
                and source_ids.issubset(set(call.document_ids))
                and not call.current_lineage_request_ids
                and not call.semantics_migration_request_ids
            )
            if len(matching_calls) != 1:
                raise ValueError("fact addition provider-call receipt is not exact")
            if (
                matching_calls[0].accepted_claims is not None
                and sum(
                    _canonical_json_payload(row)
                    == _canonical_json_payload(claim)
                    for row in matching_calls[0].accepted_claims
                )
                != 1
            ):
                raise ValueError("fact addition embedded claim receipt mismatch")
            link = link_by_claim_id[str(claim["claim_id"])]
            if (
                str(link.get("fact_id") or "") != fact_id
                or str(link.get("source_independence_group") or "")
                != str(claim.get("source_independence_group") or "")
                or frozenset(link.get("source_ids") or ()) != source_ids
                or float(link.get("claim_confidence"))
                != float(claim.get("confidence"))
                or fact_id
                in {
                    *(str(value) for value in link.get("supersedes_fact_ids") or ()),
                    *(str(value) for value in link.get("resolves_fact_ids") or ()),
                }
            ):
                raise ValueError("fact addition claim/fact link drift")

        primary_links = tuple(
            row
            for row in snapshot_links
            if str(row.get("fact_id") or "") == fact_id
            and str(row.get("link_role") or "") == "PRIMARY_FACT_CLAIM"
        )
        if len(primary_links) != 1:
            raise ValueError("fact addition primary claim is ambiguous")
        if fact_id in enriched and (
            str(current.get("source_independence_group") or "")
            != str(authority_by_id[fact_id].get("source_independence_group") or "")
        ):
            primary = primary_links[0]
            old_claim_ids = set(
                _fact_lineage_values(authority_by_id[fact_id], "claim_ids")
            )
            old_claim_rows = [
                claim_by_id[claim_id]
                for claim_id in old_claim_ids
                if claim_id in claim_by_id
            ]
            if len(old_claim_rows) != len(old_claim_ids) or not old_claim_rows:
                raise ValueError(
                    "enriched fact primary authority claim is unavailable"
                )
            old_claim_confidences = [
                float(row.get("confidence")) for row in old_claim_rows
            ]
            primary_claim = claim_by_id.get(
                str(primary.get("claim_id") or "")
            )
            primary_confidence = float(primary.get("claim_confidence"))
            old_max_confidence = max(old_claim_confidences)
            primary_is_stronger = (
                primary_confidence > old_max_confidence + 1e-12
            )
            # Equal-confidence official corroboration is still monotonic.  The
            # compiler uses claim-id ordering as its final deterministic
            # tiebreaker, so adding a second official filing/release can change
            # the representative source even though the old claim, quote and
            # source remain present.  Admit only that narrow case; equal-strength
            # media/general-web replacements remain fail-closed.
            official_tiers = {
                "REGULATORY_OFFICIAL",
                "ISSUER_OFFICIAL",
                "CUSTOMER_OFFICIAL",
            }
            primary_is_equal_official_corroboration = bool(
                primary_claim is not None
                and abs(primary_confidence - old_max_confidence) <= 1e-12
                and str(primary_claim.get("source_tier") or "")
                in official_tiers
                and old_claim_rows
                and all(
                    str(row.get("source_tier") or "") in official_tiers
                    for row in old_claim_rows
                    if abs(float(row.get("confidence")) - old_max_confidence)
                    <= 1e-12
                )
            )
            if (
                str(primary.get("claim_id") or "") not in fact_claim_ids
                or str(primary.get("source_independence_group") or "")
                != str(current.get("source_independence_group") or "")
                or not (
                    primary_is_stronger
                    or primary_is_equal_official_corroboration
                )
            ):
                raise ValueError(
                    "enriched fact primary source changed without stronger current evidence"
                )

    journal_payloads = _validated_official_fact_journal_payloads(
        root,
        required_lineages=tuple(sorted(required_lineages)),
    )
    for claim_id in added_claim_ids:
        claim = claim_by_id[claim_id]
        lineage = (
            str(claim.get("provider_prompt_hash") or ""),
            str(claim.get("provider_response_hash") or ""),
        )
        response_payload = journal_payloads[lineage]
        raw_facts = response_payload.get("facts")
        if isinstance(raw_facts, (str, bytes)) or not isinstance(
            raw_facts, Sequence
        ):
            raise ValueError("fact addition journal fact roster is invalid")
        document_id = str(claim.get("document_id") or "")
        document = document_by_id[document_id]
        reconstructed = []
        for proposal in raw_facts:
            normalized = _normalize_transport_fact_proposal(
                proposal,
                document_by_id={document_id: document},
            )
            if (
                not isinstance(normalized, Mapping)
                or str(normalized.get("document_id") or "") != document_id
            ):
                continue
            try:
                candidate = _accepted_claim(
                    normalized,
                    document=document,
                    target_id=target_id,
                    as_of_date=as_of_date,
                    provider_name=COLLABORATION_PROVIDER_NAME,
                    prompt_hash=lineage[0],
                    response_hash=lineage[1],
                    allowed_component_ids=tuple(
                        claim.get("allowed_component_ids") or ()
                    ),
                )
            except (KeyError, TypeError, ValueError):
                continue
            if _canonical_json_payload(candidate) == _canonical_json_payload(
                claim
            ):
                reconstructed.append(candidate)
        if len(reconstructed) != 1:
            raise ValueError("fact addition claim is not exact in its official response")
    return tuple(sorted(addition_fact_ids))


def _attested_pending_new_fact_ids(
    *,
    root: Path,
    target_id: str,
    as_of_date: str,
    source_checkpoint: Mapping[str, Any],
    convenience_rows: Sequence[Mapping[str, Any]],
    pending_new_fact_ids: Sequence[str],
    committed_snapshot: Mapping[str, Any],
) -> tuple[str, ...]:
    """Bind facts outside the epoch head to one exact result-last snapshot."""

    pending_new = tuple(sorted(str(value) for value in pending_new_fact_ids))
    if not pending_new:
        return ()
    if committed_snapshot.get("leaf_commit_complete") is not True:
        raise ValueError(
            "pending-new facts require a fully committed fact snapshot"
        )
    result = committed_snapshot.get("result")
    if not isinstance(result, Mapping):
        raise ValueError("fact result commit marker is unavailable")
    result_rows = tuple(committed_snapshot.get("facts") or ())
    convenience_by_id = {
        str(row["fact_id"]): _canonical_fact_payload(row)
        for row in convenience_rows
    }
    result_by_id = {
        str(row["fact_id"]): _canonical_fact_payload(row)
        for row in result_rows
    }
    if result_by_id != convenience_by_id:
        raise ValueError(
            "convenience facts do not match the result-last compiled roster"
        )
    source_bound = _fact_result_is_bound_to_source_checkpoint(
        result=result,
        source_checkpoint=source_checkpoint,
        target_id=target_id,
        as_of_date=as_of_date,
    )
    downstream_id_set = set(
        _source_checkpoint_downstream_document_ids(source_checkpoint)
    )
    pending_by_id = {
        str(row["fact_id"]): row
        for row in result_rows
        if str(row["fact_id"]) in set(pending_new)
    }
    pending_sources_are_bound = bool(
        len(pending_by_id) == len(pending_new)
        and all(
            isinstance(row.get("source_ids"), (list, tuple))
            and bool(row.get("source_ids"))
            and {
                str(value or "").strip()
                for value in row.get("source_ids") or ()
            }.issubset(downstream_id_set)
            and all(
                str(value or "").strip()
                for value in row.get("source_ids") or ()
            )
            for row in pending_by_id.values()
        )
    )
    if (
        str(result.get("target_id") or "") != target_id
        or str(result.get("as_of_date") or "") != as_of_date
        or not source_bound
        or not pending_sources_are_bound
    ):
        raise ValueError(
            "facts outside the authoritative ledger lack an exact pending roster"
        )
    return pending_new


def _load_authoritative_prior_fact_context(
    root: Path,
    *,
    target_id: str,
    as_of_date: str,
    source_checkpoint: Mapping[str, Any] | None,
) -> Mapping[str, Any] | None:
    """Union a validated epoch fact head with its convenience snapshot.

    The research-epoch JSONL is append-only authority.  The convenience file is
    only the latest extraction attempt, so a strict subset is a recovery signal,
    not permission to reopen source acquisition.
    """

    ledger_path = root / "research_epochs.jsonl"
    epoch_path = root / "research_epoch_checkpoint.json"
    if not ledger_path.exists() and not epoch_path.exists():
        return None
    if not ledger_path.is_file() or not epoch_path.is_file():
        raise ValueError("authoritative research epoch ledger is incomplete")
    if source_checkpoint is None:
        raise ValueError(
            "authoritative fact ledger requires its bound source checkpoint"
        )
    if (
        str(source_checkpoint.get("target_id") or "") != target_id
        or str(source_checkpoint.get("as_of_date") or "") != as_of_date
        or not str(source_checkpoint.get("checkpoint_id") or "").strip()
        or not str(source_checkpoint.get("checkpoint_hash") or "").strip()
    ):
        raise ValueError("authoritative fact source checkpoint identity is invalid")

    ledger = load_authoritative_research_epoch_fact_ledger(
        root,
        target_id=target_id,
        as_of_date=as_of_date,
    )
    epoch = load_research_epoch_checkpoint(epoch_path)
    epoch_source_checkpoint_id = str(
        epoch.source_graph_checkpoint_id or ""
    )
    current_source_checkpoint_id = str(
        source_checkpoint.get("checkpoint_id") or ""
    )
    current_source_parent_id = str(
        source_checkpoint.get("resumed_from_checkpoint_id") or ""
    )
    authority_rows = _validated_fact_rows(
        ledger.fact_rows,
        target_id=target_id,
        as_of_date=as_of_date,
        label="authoritative fact ledger",
    )
    exact_or_direct_source_bound = bool(
        current_source_checkpoint_id == epoch_source_checkpoint_id
        or current_source_parent_id == epoch_source_checkpoint_id
    )
    multi_epoch_fact_superset_bound = False
    if not exact_or_direct_source_bound:
        authority_source_ids = {
            str(source_id)
            for row in authority_rows
            for source_id in row.get("source_ids") or ()
            if str(source_id).strip()
        }
        current_downstream_document_ids = set(
            _source_checkpoint_downstream_document_ids(source_checkpoint)
        )
        multi_epoch_fact_superset_bound = (
            _validated_multi_epoch_source_fact_binding(
                root=root,
                target_id=target_id,
                as_of_date=as_of_date,
                ledger_checkpoint_id=ledger.checkpoint_id,
                ledger_checkpoint_hash=ledger.checkpoint_hash,
                epoch_source_checkpoint_id=epoch_source_checkpoint_id,
                current_source_checkpoint=source_checkpoint,
            )
            and authority_source_ids.issubset(current_downstream_document_ids)
        )
    source_binding_status = (
        "EXACT_EPOCH_SOURCE_CHECKPOINT"
        if current_source_checkpoint_id == epoch_source_checkpoint_id
        else "DIRECT_DESCENDANT_OF_EPOCH_SOURCE_CHECKPOINT"
        if current_source_parent_id == epoch_source_checkpoint_id
        else "VALIDATED_CURRENT_SOURCE_FACT_SUPERSET"
        if multi_epoch_fact_superset_bound
        else "INVALID"
    )
    if (
        epoch.target_id != target_id
        or epoch.as_of_date != as_of_date
        or epoch.checkpoint_id != ledger.checkpoint_id
        or epoch.checkpoint_hash != ledger.checkpoint_hash
        or source_binding_status == "INVALID"
    ):
        raise ValueError(
            "authoritative fact ledger source checkpoint binding drift"
        )

    authority_by_id = {
        str(row["fact_id"]): row for row in authority_rows
    }
    if set(authority_by_id) != set(ledger.current_fact_ids):
        raise ValueError("authoritative fact ledger current roster mismatch")
    committed_snapshot = _load_committed_fact_result_snapshot(
        root,
        target_id=target_id,
        as_of_date=as_of_date,
    )
    atomic_snapshot_repair_required = bool(
        committed_snapshot["atomic_snapshot_repair_required"]
    )
    atomic_snapshot_leaf_mismatches = tuple(
        committed_snapshot["leaf_mismatch_names"]
    )
    if atomic_snapshot_repair_required:
        _repair_fact_checkpoint_leaves_from_result_snapshot(
            root,
            snapshot=committed_snapshot,
        )
        committed_snapshot = _load_committed_fact_result_snapshot(
            root,
            target_id=target_id,
            as_of_date=as_of_date,
        )
        if committed_snapshot["leaf_commit_complete"] is not True:
            raise ValueError("fact checkpoint leaf repair did not commit")
    convenience_rows = tuple(committed_snapshot["facts"])
    convenience_by_id = {
        str(row["fact_id"]): row for row in convenience_rows
    }
    current_ids = set(ledger.current_fact_ids)
    retired_ids = set(ledger.retired_fact_ids)
    enriched_existing_fact_ids: list[str] = []
    for fact_id in sorted(current_ids.intersection(convenience_by_id)):
        if _canonical_fact_payload(authority_by_id[fact_id]) != (
            _canonical_fact_payload(convenience_by_id[fact_id])
        ):
            enriched_existing_fact_ids.append(fact_id)
    pending_new_fact_ids = tuple(
        sorted(set(convenience_by_id) - current_ids - retired_ids)
    )
    if pending_new_fact_ids:
        _attested_pending_new_fact_ids(
            root=root,
            target_id=target_id,
            as_of_date=as_of_date,
            source_checkpoint=source_checkpoint,
            convenience_rows=convenience_rows,
            pending_new_fact_ids=pending_new_fact_ids,
            committed_snapshot=committed_snapshot,
        )
    if enriched_existing_fact_ids or pending_new_fact_ids:
        try:
            _attested_compiler_fact_addition_ids(
                root=root,
                target_id=target_id,
                as_of_date=as_of_date,
                source_checkpoint=source_checkpoint,
                authority_by_id=authority_by_id,
                convenience_rows=convenience_rows,
                enriched_fact_ids=enriched_existing_fact_ids,
                pending_new_fact_ids=pending_new_fact_ids,
                committed_snapshot=committed_snapshot,
            )
        except (KeyError, TypeError, ValueError) as exc:
            conflict_id = (
                enriched_existing_fact_ids[0]
                if enriched_existing_fact_ids
                else pending_new_fact_ids[0]
            )
            raise ValueError(
                "authoritative and convenience fact payloads conflict:"
                f"{conflict_id}:{exc}"
            ) from exc
    persisted_current_ids = tuple(
        sorted(current_ids.intersection(convenience_by_id))
    )
    expectation = ledger.recovery_expectation(
        persisted_fact_ids=(
            *persisted_current_ids,
            *pending_new_fact_ids,
        ),
        pending_new_fact_ids=pending_new_fact_ids,
    )
    status = str(expectation.get("status") or "")
    authoritative_recovery_required = (
        status
        in {
            "AUTHORITY_LOSS_RECOVERY_REQUIRED",
            "AUTHORITY_LOSS_RECOVERY_WITH_PENDING_NEW_REQUIRED",
        }
    )
    # A semantics upgrade can durably commit one new fact before an older
    # authority gap is restored.  Treating that attested mixed snapshot as a
    # fatal conflict caused the runner to reopen research forever: 42 valid
    # v6 facts could not be restored because one valid v7 fact already
    # existed.  Recovery now restores only the exact old gap, preserves the
    # attested new row, and lets the extractor write one atomic union behind
    # its canonical-refresh barrier.  Unattested extra rows still fail above.
    if authoritative_recovery_required:
        downstream_document_ids = _source_checkpoint_downstream_document_ids(
            source_checkpoint
        )
        if not set(
            expectation.get("expected_recovered_source_document_ids") or ()
        ).issubset(downstream_document_ids):
            raise ValueError(
                "authoritative fact recovery source binding drift"
            )

    union_by_id = dict(authority_by_id)
    union_by_id.update(
        {
            fact_id: convenience_by_id[fact_id]
            for fact_id in (
                *enriched_existing_fact_ids,
                *pending_new_fact_ids,
            )
        }
    )
    return {
        "schema_version": "e2r_v5_authoritative_prior_fact_context_v1",
        "target_id": target_id,
        "as_of_date": as_of_date,
        "facts": tuple(
            union_by_id[fact_id] for fact_id in sorted(union_by_id)
        ),
        "fact_snapshot_available": True,
        "authoritative_fact_ledger_available": True,
        "authoritative_fact_lineage_recovery_required": (
            authoritative_recovery_required
        ),
        "pending_new_fact_epoch_commit_required": (
            status == "PENDING_NEW_FACT_EPOCH_COMMIT_REQUIRED"
        ),
        "authoritative_recovery_expectation": dict(expectation),
        # Kept in-memory only so the exact validated ledger instance can be
        # handed to the extractor.  Audits below project only scalar bindings.
        "authoritative_fact_ledger": ledger,
        "committed_fact_result_snapshot": committed_snapshot,
        "atomic_fact_snapshot_repair_required": (
            atomic_snapshot_repair_required
        ),
        "atomic_fact_snapshot_leaf_mismatches": (
            atomic_snapshot_leaf_mismatches
        ),
        "authoritative_current_fact_count": len(ledger.current_fact_ids),
        "persisted_current_fact_count": len(persisted_current_ids),
        "retired_convenience_fact_count": len(
            set(convenience_by_id).intersection(retired_ids)
        ),
        "enriched_existing_fact_ids": tuple(enriched_existing_fact_ids),
        "enriched_existing_fact_count": len(enriched_existing_fact_ids),
        "pending_new_fact_ids": pending_new_fact_ids,
        "research_epoch_checkpoint_id": ledger.checkpoint_id,
        "research_epoch_checkpoint_hash": ledger.checkpoint_hash,
        "source_graph_checkpoint_id": str(
            source_checkpoint["checkpoint_id"]
        ),
        "source_graph_checkpoint_hash": str(
            source_checkpoint["checkpoint_hash"]
        ),
        "source_graph_checkpoint_binding_status": source_binding_status,
        "research_epoch_source_graph_checkpoint_id": (
            epoch_source_checkpoint_id
        ),
        "production_score_authority": False,
    }


def _validated_multi_epoch_source_fact_binding(
    *,
    root: Path,
    target_id: str,
    as_of_date: str,
    ledger_checkpoint_id: str,
    ledger_checkpoint_hash: str,
    epoch_source_checkpoint_id: str,
    current_source_checkpoint: Mapping[str, Any],
) -> bool:
    """Admit a multi-epoch source head only with a durable bound base.

    Source acquisition checkpoints are cumulative but the current leaf keeps
    only its immediate parent.  A long-running Collaboration wait can advance
    that leaf more than once before the research epoch commits.  The durable
    until-pass receipt preserves the exact research/source base; the caller
    separately proves that every authoritative fact source still belongs to
    the current production document roster.  This is deliberately not named
    an ancestry proof: it is a current-source fact-superset binding.
    """

    progress_path = root / "until_pass_progress.json"
    if progress_path.is_symlink() or not progress_path.is_file():
        return False
    try:
        progress = _read_json(progress_path)
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError):
        return False
    if progress.get("schema_version") == (
        "e2r_v6_current_live_canary_resume_binding_v1"
    ):
        receipt_hash = str(progress.get("resume_binding_hash") or "")
        receipt_payload = {
            key: value
            for key, value in progress.items()
            if key != "resume_binding_hash"
        }
        source_binding = progress.get(
            "phase106_source_checkpoint_binding"
        )
        research_binding = progress.get(
            "research_epoch_checkpoint_binding"
        )
        current_binding = {
            "target_id": str(
                current_source_checkpoint.get("target_id") or ""
            ),
            "as_of_date": str(
                current_source_checkpoint.get("as_of_date") or ""
            ),
            "checkpoint_id": str(
                current_source_checkpoint.get("checkpoint_id") or ""
            ),
            "checkpoint_hash": str(
                current_source_checkpoint.get("checkpoint_hash") or ""
            ),
            "epoch": current_source_checkpoint.get("epoch"),
            "resumed_from_checkpoint_id": str(
                current_source_checkpoint.get(
                    "resumed_from_checkpoint_id"
                )
                or ""
            ),
        }
        return bool(
            receipt_hash == stable_hash(receipt_payload)
            and progress.get("status") == "RESEARCH_CHECKPOINT_PENDING"
            and progress.get("target_id") == target_id
            and progress.get("as_of_date") == as_of_date
            and progress.get(
                "current_source_fact_superset_revalidation_required"
            )
            is True
            and progress.get("production_score_authority") is False
            and progress.get("production_stage_authority") is False
            and isinstance(source_binding, Mapping)
            and dict(source_binding) == current_binding
            and isinstance(research_binding, Mapping)
            and str(research_binding.get("target_id") or "") == target_id
            and str(research_binding.get("as_of_date") or "")
            == as_of_date
            and str(research_binding.get("checkpoint_id") or "")
            == ledger_checkpoint_id
            and str(research_binding.get("checkpoint_hash") or "")
            == ledger_checkpoint_hash
            and str(
                research_binding.get("source_graph_checkpoint_id") or ""
            )
            == epoch_source_checkpoint_id
            and isinstance(current_binding["epoch"], int)
            and not isinstance(current_binding["epoch"], bool)
            and current_binding["epoch"] > 0
            and bool(current_binding["resumed_from_checkpoint_id"])
            and current_binding["checkpoint_id"]
            != epoch_source_checkpoint_id
            and current_binding["resumed_from_checkpoint_id"]
            != current_binding["checkpoint_id"]
        )

    source_binding = progress.get("source_checkpoint_binding")
    research_binding = progress.get("research_epoch_checkpoint_binding")
    if not isinstance(source_binding, Mapping) or not isinstance(
        research_binding, Mapping
    ):
        return False
    current_epoch = current_source_checkpoint.get("epoch")
    base_epoch = source_binding.get("epoch")
    current_parent_id = str(
        current_source_checkpoint.get("resumed_from_checkpoint_id") or ""
    )

    def sha256_text(value: Any) -> bool:
        text = str(value or "")
        return len(text) == 64 and all(
            character in "0123456789abcdef" for character in text
        )

    return bool(
        progress.get("schema_version")
        == "e2r_v5_phase94_until_pass_progress_v1"
        and progress.get("status") == "RESEARCH_CHECKPOINT_PENDING"
        and progress.get("source_transport_chain_valid") is True
        and str(progress.get("target_id") or "") == target_id
        and str(progress.get("as_of_date") or "") == as_of_date
        and str(source_binding.get("target_id") or "") == target_id
        and str(source_binding.get("as_of_date") or "") == as_of_date
        and str(source_binding.get("checkpoint_id") or "")
        == epoch_source_checkpoint_id
        and sha256_text(source_binding.get("checkpoint_hash"))
        and isinstance(base_epoch, int)
        and not isinstance(base_epoch, bool)
        and base_epoch > 0
        and str(research_binding.get("target_id") or "") == target_id
        and str(research_binding.get("as_of_date") or "") == as_of_date
        and str(research_binding.get("checkpoint_id") or "")
        == ledger_checkpoint_id
        and str(research_binding.get("checkpoint_hash") or "")
        == ledger_checkpoint_hash
        and str(research_binding.get("source_graph_checkpoint_id") or "")
        == epoch_source_checkpoint_id
        and isinstance(current_epoch, int)
        and not isinstance(current_epoch, bool)
        and current_epoch >= base_epoch + 2
        and bool(current_parent_id)
        and current_parent_id != epoch_source_checkpoint_id
        and current_parent_id
        != str(current_source_checkpoint.get("checkpoint_id") or "")
    )


def _load_prior_research_context(
    root: Path,
    *,
    target_id: str,
    as_of_date: str,
    objectives: Sequence[Mapping[str, Any]],
    archetype_id: str | None = None,
    authoritative_fact_context: Mapping[str, Any] | None = None,
) -> Mapping[str, Any]:
    if authoritative_fact_context is not None:
        if (
            str(authoritative_fact_context.get("target_id") or "")
            != target_id
            or str(authoritative_fact_context.get("as_of_date") or "")
            != as_of_date
            or authoritative_fact_context.get(
                "authoritative_fact_ledger_available"
            )
            is not True
        ):
            raise ValueError("authoritative prior fact context identity mismatch")
        facts = tuple(
            dict(row)
            for row in authoritative_fact_context.get("facts") or ()
        )
        fact_snapshot_available = True
    else:
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
    fact_extraction_result: Mapping[str, Any] = {}
    fact_extraction_complete = False
    extraction_path = root / "fact_extraction_result.json"
    if extraction_path.is_file():
        extraction = _read_json(extraction_path)
        if (
            str(extraction.get("target_id") or "") == target_id
            and str(extraction.get("as_of_date") or "") == as_of_date
        ):
            fact_extraction_result = extraction
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
    structured_report_candidate_context: Mapping[str, Any] = {}
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
            if materialization and (
                str(materialization.get("target_id") or "") != target_id
                or str(materialization.get("as_of_date") or "")
                != as_of_date
            ):
                raise ValueError(
                    "structured report candidate context target/as_of mismatch"
                )
            raw_report_candidates = materialization.get("report_candidates")
            if isinstance(raw_report_candidates, list) and all(
                isinstance(row, Mapping) for row in raw_report_candidates
            ):
                future_candidate_ids = [
                    str(row.get("candidate_id") or "UNKNOWN")
                    for row in raw_report_candidates
                    if str(row.get("published_at") or "").strip()
                    and date.fromisoformat(
                        str(row.get("published_at"))[:10]
                    )
                    > date.fromisoformat(as_of_date)
                ]
                if future_candidate_ids:
                    raise ValueError(
                        "future structured report candidate context:"
                        + ",".join(future_candidate_ids)
                    )
                structured_report_candidate_context = (
                    _structured_report_source_candidate_context(
                        tuple(raw_report_candidates)
                    )
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
    source_transport_pending_objectives: set[str] = set()
    source_queries_without_accepted_fact_lineage: list[Mapping[str, Any]] = []
    source_query_lineage_gap_objectives: set[str] = set()
    source_checkpoint_path = root / "source_graph_checkpoint.json"
    if source_checkpoint_path.is_file():
        source_checkpoint = _read_json(source_checkpoint_path)
        fact_extraction_complete = (
            _fact_extraction_is_complete_for_source_checkpoint(
                fact_result=fact_extraction_result,
                source_checkpoint=source_checkpoint,
                target_id=target_id,
                as_of_date=as_of_date,
            )
        )
        official_resolution_query_ids = (
            validated_official_first_resolution_query_ids(
                source_checkpoint
            )
        )
        source_transport_pending_objectives.update(
            str(row.get("objective_id") or "")
            for row in source_checkpoint.get("generated_queries") or ()
            if isinstance(row, Mapping)
            and str(row.get("execution_status") or "")
            in {"PENDING", "BLOCKED_OFFICIAL_FIRST"}
            and str(row.get("objective_id") or "")
        )
        compiled_fact_components_by_claim: dict[str, set[str]] = {}
        for fact in facts:
            allowed_components = {
                str(value)
                for value in fact.get("allowed_component_ids") or ()
                if str(value) in CANONICAL_COMPONENT_ORDER
            }
            if not allowed_components:
                continue
            for claim_id in fact.get("claim_ids") or ():
                normalized_claim_id = str(claim_id or "").strip()
                if normalized_claim_id:
                    compiled_fact_components_by_claim.setdefault(
                        normalized_claim_id, set()
                    ).update(allowed_components)
        accepted_claim_objectives_by_document: dict[str, set[str]] = {}
        for claim in _read_jsonl(root / "material_fact_claims.jsonl"):
            if (
                str(claim.get("target_id") or "") != target_id
                or str(claim.get("as_of_date") or "") != as_of_date
                or claim.get("accepted") is not True
                or claim.get("accepted_by_evidence_os") is not True
            ):
                continue
            claim_id = str(claim.get("claim_id") or "").strip()
            document_id = str(claim.get("document_id") or "").strip()
            compiled_components = compiled_fact_components_by_claim.get(
                claim_id, set()
            )
            claim_components = {
                str(value)
                for value in claim.get("allowed_component_ids") or ()
                if str(value) in CANONICAL_COMPONENT_ORDER
            }
            if (
                not claim_id
                or not document_id
                or not compiled_components
                or not claim_components
            ):
                continue
            for objective_id in claim.get("objective_ids") or ():
                normalized_objective_id = str(objective_id or "").strip()
                component_id = objective_component_by_id.get(
                    normalized_objective_id, ""
                )
                if (
                    normalized_objective_id
                    and component_id
                    and component_id in claim_components
                    and component_id in compiled_components
                ):
                    accepted_claim_objectives_by_document.setdefault(
                        document_id, set()
                    ).add(normalized_objective_id)
        query_objective_by_id = {
            str(query.get("query_id") or ""): str(
                query.get("objective_id") or ""
            )
            for query in source_checkpoint.get("generated_queries") or ()
            if isinstance(query, Mapping)
            and str(query.get("query_id") or "")
        }
        accepted_query_ids: set[str] = set()
        for document in source_checkpoint.get("evidence_documents") or ():
            if not isinstance(document, Mapping):
                continue
            document_id = str(document.get("document_id") or "")
            accepted_objective_ids_for_document = (
                accepted_claim_objectives_by_document.get(document_id, set())
            )
            if not accepted_objective_ids_for_document:
                continue
            for query_id in (
                str(value)
                for key in ("query_ids", "materiality_query_ids")
                for value in document.get(key) or ()
                if str(value).strip()
            ):
                objective_id = query_objective_by_id.get(query_id, "")
                if objective_id in accepted_objective_ids_for_document:
                    accepted_query_ids.add(query_id)
        accepted_objective_ids = {
            str(query.get("objective_id") or "")
            for query in source_checkpoint.get("generated_queries") or ()
            if isinstance(query, Mapping)
            and str(query.get("query_id") or "") in accepted_query_ids
            and str(query.get("objective_id") or "")
        }
        # A terminal search without accepted fact lineage is actionable only
        # after the canonical fact pass has completed.  Before that boundary,
        # the document may simply be waiting for extraction/recovery; reopening
        # acquisition here would be equivalent to ordering the same parcel
        # again while it is still waiting in the inspection queue.
        if fact_extraction_complete:
            for query in source_checkpoint.get("generated_queries") or ():
                if not isinstance(query, Mapping):
                    continue
                query_id = str(query.get("query_id") or "")
                objective_id = str(query.get("objective_id") or "")
                execution_status = str(query.get("execution_status") or "")
                if (
                    not query_id
                    or not objective_id
                    or objective_id in accepted_objective_ids
                    or query_id in accepted_query_ids
                    or execution_status
                    in {"", "PENDING", "BLOCKED_OFFICIAL_FIRST"}
                    or (
                        execution_status
                        == "SUPERSEDED_BY_OFFICIAL_RESOLUTION"
                        and query_id in official_resolution_query_ids
                    )
                ):
                    continue
                source_query_lineage_gap_objectives.add(objective_id)
                source_queries_without_accepted_fact_lineage.append(
                    {
                        "query_id": query_id,
                        "objective_id": objective_id,
                        "literal_query": query.get("literal_query"),
                        "source_families": list(
                            query.get("source_families") or ()
                        ),
                        "execution_status": execution_status,
                        "search_result_count": int(
                            query.get("search_result_count") or 0
                        ),
                        "failure_reason": (
                            "QUERY_WITHOUT_ACCEPTED_CLAIM_FACT_LINEAGE"
                        ),
                        "query_generation_owner": (
                            "SOURCE_QUERY_GENERATION_LLM"
                        ),
                        "deterministic_fallback_query_allowed": False,
                    }
                )
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
        supervisor = _source_routing_supervisor_review(
            root=root,
            target_id=target_id,
            as_of_date=as_of_date,
            current_epoch=epoch,
        )
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

            supervisor_routes_exhausted = (
                supervisor.get("reasonable_positive_routes_remaining")
                is False
            )
            if not supervisor_routes_exhausted:
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
                or supervisor_routes_exhausted
            ):
                supervisor_source_gap_context = {
                    "status": supervisor.get("status"),
                    "reasonable_positive_routes_remaining": (
                        supervisor.get(
                            "reasonable_positive_routes_remaining"
                        )
                    ),
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
    if _supervisor_explicitly_exhausted_source_routes(
        {"prior_supervisor_gap": supervisor_source_gap_context}
    ):
        # A terminal query without accepted fact lineage remains auditable in
        # ``source_queries_without_accepted_fact_lineage``.  It no longer owns
        # reopen authority after the canonical Supervisor explicitly exhausts
        # public routes.  This is not a source-absence claim: the component
        # researcher must still rewrite the memo and the three memo-bound
        # judges must run again before saturation or scoring can open.
        source_query_lineage_gap_objectives.clear()
    semantic_resolved_objective_ids = tuple(
        str(row["objective_id"])
        for row in objectives
        if str(row.get("component_id") or "") in complete_components
        and str(row.get("component_id") or "")
        not in structured_missing_components
        and str(row.get("component_id") or "")
        not in supervisor_unresolved_components
        and str(row.get("objective_id") or "")
        not in supervisor_unresolved_objectives
        and str(row.get("objective_id") or "")
        not in source_query_lineage_gap_objectives
    )
    resolved_objective_ids = tuple(
        objective_id
        for objective_id in semantic_resolved_objective_ids
        if objective_id not in source_transport_pending_objectives
    )
    return {
        "facts": facts,
        "fact_snapshot_available": fact_snapshot_available,
        "authoritative_fact_ledger_available": bool(
            authoritative_fact_context
        ),
        "authoritative_fact_lineage_recovery_required": bool(
            authoritative_fact_context
            and authoritative_fact_context.get(
                "authoritative_fact_lineage_recovery_required"
            )
        ),
        "pending_new_fact_epoch_commit_required": bool(
            authoritative_fact_context
            and authoritative_fact_context.get(
                "pending_new_fact_epoch_commit_required"
            )
        ),
        "authoritative_fact_recovery_context": (
            dict(authoritative_fact_context)
            if authoritative_fact_context is not None
            else {}
        ),
        "fact_extraction_complete": fact_extraction_complete,
        "business_model": business_model,
        "research_gap_feedback": feedback,
        "structured_gap_context": structured_gap_context,
        "structured_engine_result": structured_engine_result,
        "structured_report_candidate_context": (
            structured_report_candidate_context
        ),
        "score_gap_context": score_gap_context,
        "supervisor_gap_context": supervisor_gap_context,
        "supervisor_source_gap_context": supervisor_source_gap_context,
        "source_transport_pending_objective_ids": tuple(
            sorted(source_transport_pending_objectives)
        ),
        "source_queries_without_accepted_fact_lineage": tuple(
            source_queries_without_accepted_fact_lineage
        ),
        "semantic_resolved_objective_ids": (
            semantic_resolved_objective_ids
        ),
        "resolved_objective_ids": resolved_objective_ids,
        "research_epoch": epoch_context,
    }


def _source_routing_supervisor_review(
    *,
    root: Path,
    target_id: str,
    as_of_date: str,
    current_epoch: Mapping[str, Any],
) -> Mapping[str, Any]:
    """Keep transport scaffolds from inventing new source authority.

    A component rewrite invalidates the current synthesis for one invocation.
    ``ResearchEpochRunner`` then persists an ``RSUP-PENDING`` scaffold while
    the new memo-bound judges/synthesis are being rebuilt.  That scaffold says
    ``reasonable_positive_routes_remaining=true`` only as a fail-closed
    default; it is not a new Supervisor judgment.  If source planning consumes
    it literally, an earlier completed ``routes=false`` decision is hidden and
    the already exhausted query lane opens again before the new Supervisor can
    review the rewritten memo.

    Use the newest hash-validated, non-scaffold review from the append-only
    epoch chain for *source routing only*.  Readiness, score and Stage continue
    to use the current pending checkpoint.  This is analogous to keeping the
    last signed delivery instruction while a replacement form is awaiting a
    signature: the unsigned placeholder cannot order another shipment.
    """

    current = current_epoch.get("supervisor_review") or {}
    if not isinstance(current, Mapping):
        raise TypeError("research epoch supervisor review must be an object")
    if not _supervisor_review_is_transport_scaffold(current):
        return dict(current)

    history_path = root / "research_epochs.jsonl"
    if not history_path.is_file():
        return dict(current)
    for raw in reversed(_read_jsonl(history_path)):
        if (
            str(raw.get("target_id") or "") != target_id
            or str(raw.get("as_of_date") or "") != as_of_date
            or str(raw.get("checkpoint_id") or "")
            == str(current_epoch.get("checkpoint_id") or "")
        ):
            continue
        # The append-only row is authority only after its complete checkpoint
        # id/hash and nested Supervisor schema round-trip successfully.
        checkpoint = _coerce_checkpoint(raw)
        if checkpoint is None:
            continue
        candidate = checkpoint.supervisor_review
        if _supervisor_review_is_transport_scaffold(candidate):
            continue
        return dict(candidate)
    return dict(current)


def _supervisor_review_is_transport_scaffold(
    review: Mapping[str, Any],
) -> bool:
    """Identify deterministic pending state, never a provider judgment."""

    review_id = str(review.get("review_id") or "")
    rationale = str(review.get("rationale") or "")
    return bool(
        review_id.startswith("RSUP-PENDING-")
        and review.get("status") == "NEXT_RESEARCH_REQUIRED"
        and review.get("ready_for_independent_saturation_review") is False
        and review.get("component_memos_sufficient") is False
        and not (review.get("component_findings") or ())
        and not (review.get("missing_material_facts") or ())
        and not (review.get("new_source_family_directions") or ())
        and not (review.get("query_direction_briefs") or ())
        and (
            rationale.startswith("SUPERVISOR_SYNTHESIS_LINEAGE_PENDING:")
            or rationale.startswith("SUPERVISOR_PROVIDER_OR_OUTPUT_ERROR:")
            or rationale == "SUPERVISOR_PROVIDER_NOT_CONFIGURED"
        )
    )


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


def _structured_report_source_candidate_context(
    structured_report_candidates: Sequence[Mapping[str, Any]],
) -> Mapping[str, Any]:
    """Project metadata-only report hints for both Query LLM and Supervisor.

    These rows can help the LLM name a bounded full-document route, but they
    never become EvidenceFacts or numeric score inputs on their own.
    """

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
    result: dict[str, Any] = {}
    result["structured_report_source_candidates"] = {
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
    result["structured_report_source_candidate_contract"] = {
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
    context.update(
        _structured_report_source_candidate_context(
            structured_report_candidates
        )
    )
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
    "FactExtractionCheckpointPending",
    "load_current_research_target_registry",
    "load_current_research_targets",
    "resume_current_fact_extraction_checkpoint",
    "write_production_lane",
]
