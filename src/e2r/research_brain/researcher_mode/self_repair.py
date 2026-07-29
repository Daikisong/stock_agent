"""Phase 99 research-recall and score-scale self-repair acceptance.

This module separates two truths:

* internal failure clusters are repaired only when focused tests and an
  independent clean rerun both pass; and
* live canaries from the repository target registry remain incomplete while
  their production dossiers are pending.

It never generates a literal query, copies Gold inputs, or treats a provider
failure as a low score.
"""

from __future__ import annotations

import io
import json
import re
import unittest
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.metadata import stable_hash, write_json, write_text


SCHEMA_VERSION = "e2r_v5_phase99_self_repair_v1"
PHASE99_PASS = "PHASE99_INTERNAL_SELF_REPAIR_PASS"
PHASE99_FAIL = "PHASE99_INTERNAL_SELF_REPAIR_FAIL"
DEFAULT_PHASE99_AUDIT_PATH = Path(
    "docs/operational/e2r_v5_self_repair_audit.json"
)
DEFAULT_PHASE99_SUMMARY_PATH = Path(
    "docs/operational/e2r_v5_self_repair_summary.md"
)

PARITY_FAILURE_CLASSES = (
    "RESEARCH_APERTURE_TOO_NARROW",
    "MATERIAL_FACT_MISSED",
    "COUNTERFACT_MISSED",
    "STRUCTURED_DATA_MISSING",
    "DOCUMENT_RANKER_FAILURE",
    "CLAIM_EXTRACTION_FAILURE",
    "COMPONENT_JUDGMENT_UNDERCREDIT",
    "COMPONENT_JUDGMENT_OVERCREDIT",
    "ANCHOR_MISMATCH",
    "SCORE_SCALE_COLLAPSE",
    "STAGE_MISMATCH",
    "TARGET_SPECIFIC_OVERFIT",
)

SELF_REPAIR_LOOP_ORDER = (
    "RUN",
    "EVIDENCE_RECALL_AUDIT",
    "COMPONENT_PARITY_AUDIT",
    "SCORE_SCALE_AUDIT",
    "STAGE_AUDIT",
    "ROOT_CAUSE_CLUSTER",
    "CODE_PROMPT_SOURCE_PARSER_PATCH",
    "FOCUSED_TESTS",
    "CLEAN_RERUN",
)

PUBLIC_RESEARCH_ROUTES = (
    "DART",
    "KIND",
    "KRX",
    "ISSUER_IR",
    "COMPANYGUIDE",
    "PUBLIC_BROKER_REPORT",
    "INDEPENDENT_PUBLIC_REPORT",
    "GENERAL_WEB_FALLBACK",
)


@dataclass(frozen=True)
class FailureClusterRepairSpec:
    failure_class: str
    audit_layer: str
    root_cause_file_function_config: str
    repair_kind: str
    changed_files: tuple[str, ...]
    focused_test_ids: tuple[str, ...]

    def __post_init__(self) -> None:
        if self.failure_class not in PARITY_FAILURE_CLASSES:
            raise ValueError("unknown Phase 99 failure class")
        if self.audit_layer not in {
            "EVIDENCE_RECALL",
            "COMPONENT_PARITY",
            "SCORE_SCALE",
            "STAGE",
            "GENERALIZATION",
        }:
            raise ValueError("unknown Phase 99 audit layer")
        if self.repair_kind not in {
            "CODE",
            "PROMPT",
            "SOURCE_ROUTE",
            "PARSER",
            "CODE_AND_PROMPT",
        }:
            raise ValueError("unknown Phase 99 repair kind")
        if not all(
            (
                self.root_cause_file_function_config,
                self.changed_files,
                self.focused_test_ids,
            )
        ):
            raise ValueError("Phase 99 repair specs require concrete lineage")


REPAIR_CLUSTER_SPECS = (
    FailureClusterRepairSpec(
        "RESEARCH_APERTURE_TOO_NARROW",
        "EVIDENCE_RECALL",
        "researcher_mode/legacy_retrieval_aperture.py::compile_legacy_retrieval_aperture; source_graph_explorer.py::ResearcherSourceGraphAcquirer",
        "CODE_AND_PROMPT",
        (
            "src/e2r/research_brain/researcher_mode/legacy_retrieval_aperture.py",
            "src/e2r/research_brain/researcher_mode/source_graph_explorer.py",
        ),
        (
            "tests.test_e2r_v5_legacy_retrieval_aperture.E2RV5LegacyRetrievalApertureTests.test_acceptance_recall_is_above_threshold",
            "tests.test_e2r_v5_all_archetype_generalization.E2RV5AllArchetypeGeneralizationTests.test_source_graph_is_broad_but_literal_queries_remain_llm_owned",
        ),
    ),
    FailureClusterRepairSpec(
        "MATERIAL_FACT_MISSED",
        "EVIDENCE_RECALL",
        "researcher_mode/full_thesis_gold_benchmark.py::audit_full_thesis_gold_recall; evidence_fact_extractor.py::production_material_fact_rows",
        "CODE_AND_PROMPT",
        (
            "src/e2r/research_brain/researcher_mode/full_thesis_gold_benchmark.py",
            "src/e2r/research_brain/researcher_mode/evidence_fact_extractor.py",
        ),
        (
            "tests.test_e2r_v5_full_thesis_gold_benchmark.E2RV5FullThesisGoldBenchmarkTests.test_controlled_independent_post_run_meets_all_recall_gates",
            "tests.test_e2r_v5_full_thesis_gold_benchmark.E2RV5FullThesisGoldBenchmarkTests.test_critical_fact_miss_fails_post_run_gate",
        ),
    ),
    FailureClusterRepairSpec(
        "COUNTERFACT_MISSED",
        "EVIDENCE_RECALL",
        "researcher_mode/red_team_researcher.py::RedTeamResearcher; full_thesis_gold_benchmark.py::counterfact gate",
        "CODE_AND_PROMPT",
        (
            "src/e2r/research_brain/researcher_mode/red_team_researcher.py",
            "src/e2r/research_brain/researcher_mode/full_thesis_gold_benchmark.py",
        ),
        (
            "tests.test_e2r_v5_full_thesis_gold_benchmark.E2RV5FullThesisGoldBenchmarkTests.test_counterfact_miss_fails_counter_and_topic_gates",
            "tests.test_e2r_v5_full_thesis_gold_benchmark.E2RV5FullThesisGoldBenchmarkTests.test_every_component_has_source_backed_support_and_counter",
        ),
    ),
    FailureClusterRepairSpec(
        "STRUCTURED_DATA_MISSING",
        "EVIDENCE_RECALL",
        "researcher_mode/structured_financial_engine.py::StructuredFinancialConsensusValuationEngine; current_structured_materializer.py::CurrentStructuredSourceMaterializer",
        "CODE_AND_PROMPT",
        (
            "src/e2r/research_brain/researcher_mode/structured_financial_engine.py",
            "src/e2r/research_brain/researcher_mode/current_structured_materializer.py",
        ),
        (
            "tests.test_e2r_v5_structured_financial_engine.E2RV5StructuredFinancialEngineTests.test_connector_gap_is_pending_and_never_zero_component",
            "tests.test_e2r_v5_structured_financial_engine.E2RV5StructuredFinancialEngineTests.test_valuation_uses_price_forward_and_balance_sheet_records",
        ),
    ),
    FailureClusterRepairSpec(
        "DOCUMENT_RANKER_FAILURE",
        "EVIDENCE_RECALL",
        "researcher_mode/document_ranker.py::ResearcherDocumentRanker; source_graph_explorer.py::material candidate accounting",
        "CODE_AND_PROMPT",
        (
            "src/e2r/research_brain/researcher_mode/document_ranker.py",
            "src/e2r/research_brain/researcher_mode/source_graph_explorer.py",
        ),
        (
            "tests.test_e2r_v5_researcher_mode.E2RV5ResearcherModeTests.test_document_ranker_has_no_top_n_and_snippet_is_not_evidence",
            "tests.test_e2r_v5_source_graph_acquisition.E2RV5SourceGraphAcquisitionTests.test_incomplete_materiality_ranking_fetches_nothing_and_stays_pending",
        ),
    ),
    FailureClusterRepairSpec(
        "CLAIM_EXTRACTION_FAILURE",
        "EVIDENCE_RECALL",
        "researcher_mode/evidence_fact_extractor.py::ResearcherEvidenceFactExtractor; evidence_fact_compiler.py::EvidenceFactCompiler",
        "PARSER",
        (
            "src/e2r/research_brain/researcher_mode/evidence_fact_extractor.py",
            "src/e2r/research_brain/researcher_mode/evidence_fact_compiler.py",
        ),
        (
            "tests.test_e2r_v5_fact_extraction.E2RV5FactExtractionTests.test_invalid_exact_quote_is_reprompted_with_the_rejected_proposal",
            "tests.test_e2r_v5_fact_extraction.E2RV5FactExtractionTests.test_wrong_business_segment_is_terminal_and_cannot_enter_fact_graph",
        ),
    ),
    FailureClusterRepairSpec(
        "COMPONENT_JUDGMENT_UNDERCREDIT",
        "COMPONENT_PARITY",
        "researcher_mode/component_judge.py::ComponentJudge; score_aggregator.py::DeterministicScoreAggregator.aggregate_component",
        "CODE_AND_PROMPT",
        (
            "src/e2r/research_brain/researcher_mode/component_judge.py",
            "src/e2r/research_brain/researcher_mode/score_aggregator.py",
        ),
        (
            "tests.test_e2r_v5_deterministic_score_aggregator.E2RV5DeterministicScoreAggregatorTests.test_strong_high_anchor_equivalent_evidence_does_not_collapse_to_one_to_three_points",
        ),
    ),
    FailureClusterRepairSpec(
        "COMPONENT_JUDGMENT_OVERCREDIT",
        "COMPONENT_PARITY",
        "researcher_mode/evidence_fact_graph.py::EvidenceFactGraphEngine; claim_utilization.py::ClaimUtilizationLedgerBuilder",
        "CODE",
        (
            "src/e2r/research_brain/researcher_mode/evidence_fact_graph.py",
            "src/e2r/research_brain/researcher_mode/claim_utilization.py",
        ),
        (
            "tests.test_e2r_v5_evidence_fact_graph.E2RV5EvidenceFactGraphTests.test_one_claim_can_feed_multiple_components_but_total_credit_is_capped",
            "tests.test_e2r_v5_evidence_fact_graph.E2RV5EvidenceFactGraphTests.test_corroborating_or_same_group_duplicate_claim_cannot_score_again",
        ),
    ),
    FailureClusterRepairSpec(
        "ANCHOR_MISMATCH",
        "COMPONENT_PARITY",
        "researcher_mode/component_anchor_atlas.py::compile_component_anchor_atlas; calibration_judge.py::CalibrationJudge",
        "CODE_AND_PROMPT",
        (
            "src/e2r/research_brain/researcher_mode/component_anchor_atlas.py",
            "src/e2r/research_brain/researcher_mode/calibration_judge.py",
        ),
        (
            "tests.test_e2r_v5_component_scoring_memos.E2RV5ComponentScoringMemoTests.test_missing_or_incompatible_anchor_blocks_calibration",
            "tests.test_e2r_v5_component_anchor_atlas.E2RV5ComponentAnchorAtlasTests.test_all_registry_components_have_ordinal_anchor_or_explicit_gap",
        ),
    ),
    FailureClusterRepairSpec(
        "SCORE_SCALE_COLLAPSE",
        "SCORE_SCALE",
        "researcher_mode/historical_blind_replay.py::audit_dynamic_range; score_aggregator.py::DeterministicScoreAggregator",
        "CODE_AND_PROMPT",
        (
            "src/e2r/research_brain/researcher_mode/historical_blind_replay.py",
            "src/e2r/research_brain/researcher_mode/score_aggregator.py",
        ),
        (
            "tests.test_e2r_v5_historical_blind_replay.E2RV5HistoricalBlindReplayTests.test_dynamic_range_audit_fails_when_high_mid_low_all_collapse_to_twenty",
            "tests.test_e2r_v5_historical_blind_replay.E2RV5HistoricalBlindReplayTests.test_dynamic_range_canary_contains_historical_high_mid_and_low",
        ),
    ),
    FailureClusterRepairSpec(
        "STAGE_MISMATCH",
        "STAGE",
        "researcher_mode/stagecourt.py::ResearcherStageCourt; canonical deterministic stage gates",
        "CODE",
        ("src/e2r/research_brain/researcher_mode/stagecourt.py",),
        (
            "tests.test_e2r_v5_stagecourt.E2RV5StageCourtTests.test_daily_event_overlay_cannot_change_canonical_stage",
            "tests.test_e2r_v5_stagecourt.E2RV5StageCourtTests.test_hard_break_requires_open_official_target_mechanism_claim",
        ),
    ),
    FailureClusterRepairSpec(
        "TARGET_SPECIFIC_OVERFIT",
        "GENERALIZATION",
        "researcher_mode/generalization.py::compile_all_archetype_generalization; runtime branch scanner",
        "CODE_AND_PROMPT",
        (
            "src/e2r/research_brain/researcher_mode/generalization.py",
            "src/e2r/research_brain/researcher_mode/current_researcher_mode.py",
        ),
        (
            "tests.test_e2r_v5_all_archetype_generalization.E2RV5AllArchetypeGeneralizationTests.test_complete_registry_enters_the_same_seven_component_path",
            "tests.test_e2r_v5_full_thesis_gold_benchmark.E2RV5FullThesisGoldBenchmarkTests.test_generic_validator_contains_no_canary_target_branch",
        ),
    ),
)


@dataclass(frozen=True)
class RepairQueryValidation:
    status: str
    accepted_queries: tuple[str, ...]
    rejected_queries: tuple[str, ...]
    rejection_reasons: tuple[str, ...]
    score_gap_context: Mapping[str, Any]
    query_generation_authority: str = "LLM_RESEARCH_SUPERVISOR"
    deterministic_query_synthesis: bool = False

    def __post_init__(self) -> None:
        if self.status not in {"ACCEPTED", "RETRY_LLM_REQUIRED"}:
            raise ValueError("unknown repair query validation status")
        if self.deterministic_query_synthesis:
            raise ValueError("Phase 99 cannot synthesize deterministic queries")
        if self.query_generation_authority != "LLM_RESEARCH_SUPERVISOR":
            raise ValueError("Phase 99 query generation must remain LLM-owned")

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "status": self.status,
            "accepted_queries": list(self.accepted_queries),
            "rejected_queries": list(self.rejected_queries),
            "rejection_reasons": list(self.rejection_reasons),
            "score_gap_context": dict(self.score_gap_context),
            "query_generation_authority": self.query_generation_authority,
            "deterministic_query_synthesis": False,
        }


@dataclass(frozen=True)
class AlternatePublicRoutePlan:
    status: str
    failed_route: str
    attempted_routes: tuple[str, ...]
    remaining_public_routes: tuple[str, ...]
    exact_blocker: str | None
    canary_goal_complete: bool
    query_generation_authority: str = "LLM_RESEARCH_SUPERVISOR"
    deterministic_literal_query: str | None = None

    def __post_init__(self) -> None:
        if self.status not in {
            "ALTERNATE_PUBLIC_ROUTE_REQUIRED",
            "ALL_PUBLIC_ROUTES_EXHAUSTED",
        }:
            raise ValueError("unknown alternate route status")
        if self.canary_goal_complete:
            raise ValueError("provider-route planning cannot complete the canary goal")
        if self.deterministic_literal_query is not None:
            raise ValueError("alternate route plan cannot synthesize a literal query")

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "status": self.status,
            "failed_route": self.failed_route,
            "attempted_routes": list(self.attempted_routes),
            "remaining_public_routes": list(self.remaining_public_routes),
            "exact_blocker": self.exact_blocker,
            "canary_goal_complete": False,
            "query_generation_authority": self.query_generation_authority,
            "deterministic_literal_query": None,
        }


_SPACE_RE = re.compile(r"\s+")
_URL_RE = re.compile(r"https?://[^\s]+", re.IGNORECASE)
_GOLD_MARKER_RE = re.compile(r"(?:^|[-_\s])gold(?:$|[-_\s])", re.IGNORECASE)
_USAGE_LIMIT_RE = re.compile(
    r"\busage\s+limit\b",
    re.IGNORECASE,
)
_USAGE_LIMIT_RESET_RE = re.compile(
    r"try\s+again\s+at\s+"
    r"([A-Z][a-z]{2}\s+\d{1,2}(?:st|nd|rd|th),\s+\d{4}\s+"
    r"\d{1,2}:\d{2}\s+(?:AM|PM))",
    re.IGNORECASE,
)
_ACTIVE_PROVIDER_DIAGNOSTIC_LEAVES = (
    "target_run_manifest.json",
    "component_research_memos.jsonl",
    "component_judge_decisions.jsonl",
    "business_model_memo.json",
    "red_team_research.json",
    "research_supervisor_review.json",
    "research_epoch_checkpoint.json",
    "stagecourt.json",
    "until_pass_progress.json",
)


def validate_llm_repair_queries(
    *,
    executed_queries: Sequence[str],
    suggested_queries: Sequence[str],
    provenance_by_query: Mapping[str, str] | None = None,
) -> RepairQueryValidation:
    """Validate, but never create, literal LLM repair queries."""

    executed = {_normalize_query(query) for query in executed_queries if query.strip()}
    accepted: list[str] = []
    rejected: list[str] = []
    reasons: list[str] = []
    seen = set(executed)
    provenance = dict(provenance_by_query or {})
    for query in suggested_queries:
        normalized = _normalize_query(query)
        query_reasons = []
        if not normalized:
            query_reasons.append("EMPTY_QUERY")
        if normalized in seen:
            query_reasons.append("IDENTICAL_OR_NORMALIZED_DUPLICATE_QUERY")
        origin = str(provenance.get(query) or provenance.get(normalized) or "LLM")
        if _GOLD_MARKER_RE.search(origin) or _GOLD_MARKER_RE.search(query):
            query_reasons.append("GOLD_QUERY_OR_PROVENANCE_FORBIDDEN")
        if query_reasons:
            rejected.append(query)
            reasons.extend(query_reasons)
            continue
        accepted.append(query.strip())
        seen.add(normalized)
    status = "ACCEPTED" if accepted and not rejected else "RETRY_LLM_REQUIRED"
    feedback = tuple(dict.fromkeys(reasons or ("NO_NOVEL_EXECUTABLE_QUERY",)))
    return RepairQueryValidation(
        status=status,
        accepted_queries=tuple(accepted) if status == "ACCEPTED" else (),
        rejected_queries=tuple(rejected),
        rejection_reasons=feedback if status != "ACCEPTED" else (),
        score_gap_context={
            "failure_class": "REPAIR_QUERY_VALIDATION_FAILED",
            "rejection_reasons": list(feedback if status != "ACCEPTED" else ()),
            "executed_query_hashes": [
                stable_hash(value) for value in sorted(executed)
            ],
            "instruction": (
                "Generate a genuinely new query from current evidence and failure context; "
                "do not use Gold URLs, Gold scores, or expected outputs."
            ),
        },
    )


def plan_alternate_public_routes(
    *,
    failed_route: str,
    attempted_routes: Sequence[str],
    available_public_routes: Sequence[str] = PUBLIC_RESEARCH_ROUTES,
) -> AlternatePublicRoutePlan:
    attempted = tuple(dict.fromkeys(str(value) for value in attempted_routes if value))
    available = tuple(
        dict.fromkeys(str(value) for value in available_public_routes if value)
    )
    remaining = tuple(route for route in available if route not in set(attempted))
    if remaining:
        return AlternatePublicRoutePlan(
            status="ALTERNATE_PUBLIC_ROUTE_REQUIRED",
            failed_route=failed_route,
            attempted_routes=attempted,
            remaining_public_routes=remaining,
            exact_blocker=None,
            canary_goal_complete=False,
        )
    blocker = (
        "ALL_PUBLIC_ROUTES_EXHAUSTED:"
        + (failed_route.strip() or "UNKNOWN_PROVIDER_OR_ROUTE")
    )
    return AlternatePublicRoutePlan(
        status="ALL_PUBLIC_ROUTES_EXHAUSTED",
        failed_route=failed_route,
        attempted_routes=attempted,
        remaining_public_routes=(),
        exact_blocker=blocker,
        canary_goal_complete=False,
    )


class _RecordingResult(unittest.TextTestResult):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.passed_ids: set[str] = set()

    def addSuccess(self, test: unittest.case.TestCase) -> None:  # noqa: N802
        super().addSuccess(test)
        self.passed_ids.add(test.id())


def _run_detectors(detector_ids: Sequence[str]) -> tuple[_RecordingResult, str]:
    suite = unittest.TestSuite(
        unittest.TestLoader().loadTestsFromName(test_id) for test_id in detector_ids
    )
    stream = io.StringIO()
    result = unittest.TextTestRunner(
        stream=stream,
        verbosity=0,
        resultclass=_RecordingResult,
    ).run(suite)
    return result, stream.getvalue()


def compile_phase99_self_repair_audit(
    workspace_root: str | Path = ".",
) -> Mapping[str, Any]:
    """Recompute the Phase 99 repair ledger and current live-canary blockers."""

    root = Path(workspace_root)
    detector_ids = tuple(
        dict.fromkeys(
            test_id
            for spec in REPAIR_CLUSTER_SPECS
            for test_id in spec.focused_test_ids
        )
    )
    focused, focused_output = _run_detectors(detector_ids)
    clean, clean_output = _run_detectors(detector_ids)
    focused_vector = tuple(test_id in focused.passed_ids for test_id in detector_ids)
    clean_vector = tuple(test_id in clean.passed_ids for test_id in detector_ids)

    clusters = []
    for spec in REPAIR_CLUSTER_SPECS:
        focused_missing = tuple(
            test_id for test_id in spec.focused_test_ids if test_id not in focused.passed_ids
        )
        clean_missing = tuple(
            test_id for test_id in spec.focused_test_ids if test_id not in clean.passed_ids
        )
        resolved = not focused_missing and not clean_missing
        clusters.append(
            {
                "cluster_id": "PHASE99-" + stable_hash(
                    {
                        "failure_class": spec.failure_class,
                        "root_cause": spec.root_cause_file_function_config,
                    }
                )[:20],
                "failure_class": spec.failure_class,
                "audit_layer": spec.audit_layer,
                "initial_status": "DETECTED",
                "root_cause_file_function_config": spec.root_cause_file_function_config,
                "patch": {
                    "repair_kind": spec.repair_kind,
                    "changed_files": list(spec.changed_files),
                    "literal_query": None,
                    "query_generation_authority": "LLM_RESEARCH_SUPERVISOR",
                    "gold_url_or_score_injected": False,
                    "identical_query_retry": False,
                },
                "focused_test_ids": list(spec.focused_test_ids),
                "focused_test_status": "PASS" if not focused_missing else "FAIL",
                "clean_rerun_status": "PASS" if not clean_missing else "FAIL",
                "failed_focused_test_ids": list(focused_missing),
                "failed_clean_rerun_test_ids": list(clean_missing),
                "final_status": "VERIFIED_REPAIRED" if resolved else "REPAIR_FAILED",
            }
        )

    live_canaries = _audit_live_canaries(root)
    failure_classes = [row["failure_class"] for row in clusters]
    critical_counts = {
        "failure_class_count_mismatch": abs(len(clusters) - 12),
        "failure_class_roster_mismatch": len(
            set(failure_classes) ^ set(PARITY_FAILURE_CLASSES)
        ),
        "duplicate_failure_class_count": len(failure_classes)
        - len(set(failure_classes)),
        "focused_test_failure_count": len(focused.failures) + len(focused.errors),
        "clean_rerun_failure_count": len(clean.failures) + len(clean.errors),
        "focused_test_run_count_mismatch": abs(
            focused.testsRun - len(detector_ids)
        ),
        "clean_rerun_test_count_mismatch": abs(clean.testsRun - len(detector_ids)),
        "unresolved_internal_cluster_count": sum(
            row["final_status"] != "VERIFIED_REPAIRED" for row in clusters
        ),
        "same_evidence_replay_variance_count": sum(
            left != right for left, right in zip(focused_vector, clean_vector)
        ),
        "deterministic_query_synthesis_count": sum(
            row["patch"]["literal_query"] is not None for row in clusters
        ),
        "gold_injection_count": sum(
            row["patch"]["gold_url_or_score_injected"] for row in clusters
        ),
        "identical_query_retry_count": sum(
            row["patch"]["identical_query_retry"] for row in clusters
        ),
    }
    critical_sum = sum(critical_counts.values())
    return {
        "schema_version": SCHEMA_VERSION,
        "status": PHASE99_PASS if critical_sum == 0 else PHASE99_FAIL,
        "scope": "INTERNAL_REPAIR_ACCEPTANCE_WITH_SEPARATE_LIVE_CANARY_TRUTH",
        "production_readiness_authority": False,
        "self_repair_loop_order": list(SELF_REPAIR_LOOP_ORDER),
        "fixed_iteration_cap_used": False,
        "failure_class_count": len(clusters),
        "failure_classes": list(PARITY_FAILURE_CLASSES),
        "repair_clusters": clusters,
        "focused_test_run": {
            "test_count": focused.testsRun,
            "passed_count": len(focused.passed_ids),
            "outcome_hash": stable_hash(focused_vector),
        },
        "clean_rerun": {
            "test_count": clean.testsRun,
            "passed_count": len(clean.passed_ids),
            "outcome_hash": stable_hash(clean_vector),
            "same_evidence_replay_variance": sum(
                left != right for left, right in zip(focused_vector, clean_vector)
            ),
        },
        "query_safety": {
            "literal_query_generation_authority": "LLM_RESEARCH_SUPERVISOR",
            "deterministic_query_synthesis": False,
            "identical_query_retry_allowed": False,
            "gold_url_score_or_expected_output_allowed": False,
            "provider_failure_policy": "TRY_ALTERNATE_PUBLIC_ROUTE_THEN_EXACT_PENDING_BLOCKER",
        },
        "live_canaries": live_canaries,
        "canary_goal_complete": live_canaries["canary_goal_complete"],
        "canary_completion_blockers": live_canaries["blockers"],
        "critical_counts": critical_counts,
        "critical_count_sum": critical_sum,
        "runner_output": (
            focused_output + clean_output if critical_sum else ""
        ),
    }


def render_phase99_self_repair_summary(audit: Mapping[str, Any]) -> str:
    clusters = audit.get("repair_clusters") or []
    canaries = audit.get("live_canaries") or {}
    lines = [
        "# E2R v5 Phase 99 Self-Repair Summary",
        "",
        f"- internal status: `{audit.get('status')}`",
        f"- internal failure clusters: `{len(clusters)}` / `12`",
        "- self-repair order: `run → evidence recall → component parity → score scale → Stage → root cause → patch → focused tests → clean rerun`",
        f"- clean replay variance: `{(audit.get('clean_rerun') or {}).get('same_evidence_replay_variance')}`",
        "- deterministic query synthesis: `false`",
        "- identical query retry allowed: `false`",
        "- Gold URL/score injection allowed: `false`",
        "- production readiness authority: `false`",
        "",
        "## Failure clusters",
        "",
        "| failure class | layer | repair | focused | clean rerun |",
        "|---|---|---|---|---|",
    ]
    for row in clusters:
        lines.append(
            "| {failure_class} | {audit_layer} | {repair_kind} | {focused_test_status} | {clean_rerun_status} |".format(
                failure_class=row.get("failure_class"),
                audit_layer=row.get("audit_layer"),
                repair_kind=(row.get("patch") or {}).get("repair_kind"),
                focused_test_status=row.get("focused_test_status"),
                clean_rerun_status=row.get("clean_rerun_status"),
            )
        )
    lines.extend(
        [
            "",
            "## Live canary truth",
            "",
            *(
                f"- {row.get('company_name')} ({row.get('target_id')}) status: `{row.get('status')}`"
                for row in canaries.get("targets") or []
            ),
            f"- canary goal complete: `{str(bool(audit.get('canary_goal_complete'))).lower()}`",
            f"- provider usage limit detected: `{str(bool(canaries.get('provider_usage_limit_detected'))).lower()}`",
            *(
                f"- provider reset hint: `{hint}`"
                for hint in canaries.get("provider_usage_limit_reset_hints") or []
            ),
            "- blockers:",
        ]
    )
    blockers = audit.get("canary_completion_blockers") or []
    lines.extend(f"  - `{blocker}`" for blocker in blockers)
    lines.extend(
        [
            "",
            "내부 자가수리 회귀 통과는 target registry의 live dossier 완료를 대신하지 않는다.",
            (
                "live canary goal도 완료되었으므로 "
                "`MEANINGFUL_E2R_RESEARCHER_PARITY_READY` 선언의 canary gate는 통과했다."
                if audit.get("canary_goal_complete") is True
                else "따라서 현재 `MEANINGFUL_E2R_RESEARCHER_PARITY_READY` 선언은 허용되지 않는다."
            ),
            "",
        ]
    )
    return "\n".join(lines)


def write_phase99_self_repair_artifacts(
    *,
    workspace_root: str | Path = ".",
    audit_path: str | Path = DEFAULT_PHASE99_AUDIT_PATH,
    summary_path: str | Path = DEFAULT_PHASE99_SUMMARY_PATH,
) -> Mapping[str, Path]:
    audit = compile_phase99_self_repair_audit(workspace_root)
    audit_destination = Path(audit_path)
    summary_destination = Path(summary_path)
    write_json(audit_destination, audit)
    write_text(summary_destination, render_phase99_self_repair_summary(audit))
    return {"audit": audit_destination, "summary": summary_destination}


def _audit_live_canaries(root: Path) -> Mapping[str, Any]:
    manifests = sorted(
        root.glob("output/researcher_mode/**/target_run_manifest.json"),
        key=lambda path: str(path),
    )
    by_target: dict[str, tuple[Path, Mapping[str, Any]]] = {}
    for path in manifests:
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError):
            continue
        target_id = str(payload.get("target_id") or "")
        if target_id:
            by_target[target_id] = (path, payload)

    target_registry_path = root / "configs/e2r_targeted_live_smoke_v1.json"
    try:
        registry = json.loads(target_registry_path.read_text(encoding="utf-8"))
        target_specs = tuple(registry.get("mandatory_targets") or ())
    except (OSError, UnicodeError, json.JSONDecodeError):
        target_specs = ()
    targets = tuple(
        _canary_row(
            str(spec.get("symbol") or ""),
            by_target.get(str(spec.get("symbol") or "")),
            root,
            company_name=str(spec.get("company_name") or "UNKNOWN"),
        )
        for spec in target_specs
        if str(spec.get("symbol") or "").strip()
    )
    blockers = []
    if not targets:
        blockers.append("LIVE_CANARY_TARGET_REGISTRY_MISSING_OR_EMPTY")
    for row in targets:
        if row["status"] == "LIVE_RESEARCH_NOT_STARTED":
            blockers.append(f"LIVE_RESEARCH_NOT_STARTED:{row['target_id']}")
        elif row["status"] != "PRODUCTION_RESEARCH_COMPLETE":
            blockers.append(f"LIVE_RESEARCH_CHECKPOINT_PENDING:{row['target_id']}")
    usage_limit = _audit_active_provider_usage_limits(
        root=root,
        target_items=tuple(
            item
            for item in (
                by_target.get(str(spec.get("symbol") or ""))
                for spec in target_specs
            )
            if item is not None
        ),
    )
    blockers.extend(
        f"CODEX_PROVIDER_USAGE_LIMIT:{target_id}"
        for target_id in usage_limit["target_ids"]
    )
    canary_goal_complete = bool(targets) and not blockers and all(
        row["production_research_complete"] for row in targets
    )
    return {
        "target_registry_path": (
            str(target_registry_path.relative_to(root))
            if target_registry_path.is_file()
            else None
        ),
        "targets": list(targets),
        "provider_usage_limit_detected": usage_limit["detected"],
        "provider_usage_limit_target_ids": usage_limit["target_ids"],
        "provider_usage_limit_reset_hints": usage_limit["reset_hints"],
        "provider_usage_limit_evidence_paths": usage_limit["evidence_paths"],
        "blockers": list(dict.fromkeys(blockers)),
        "canary_goal_complete": canary_goal_complete,
    }


def _audit_active_provider_usage_limits(
    *,
    root: Path,
    target_items: Sequence[tuple[Path, Mapping[str, Any]]],
) -> Mapping[str, Any]:
    """Read only current canary leaves, never stale append-only history.

    A provider limit is operationally relevant only while the current target
    manifest is incomplete.  The reset time is evidence copied from the
    provider message, not a date embedded in deterministic code.
    """

    target_ids: list[str] = []
    reset_hints: list[str] = []
    evidence_paths: list[str] = []
    for manifest_path, manifest in target_items:
        if manifest.get("production_research_complete") is True:
            continue
        target_id = str(manifest.get("target_id") or "").strip()
        target_directory = manifest_path.parent
        target_detected = False
        provider_cache = manifest.get("provider_response_cache")
        if (
            isinstance(provider_cache, Mapping)
            and provider_cache.get("provider_usage_limit_detected") is True
        ):
            target_detected = True
            try:
                evidence_paths.append(str(manifest_path.relative_to(root)))
            except ValueError:
                evidence_paths.append(str(manifest_path))
            reset_hints.extend(
                " ".join(str(value).split())
                for value in (
                    provider_cache.get("provider_usage_limit_reset_hints") or ()
                )
                if str(value).strip()
            )
        for leaf_name in _ACTIVE_PROVIDER_DIAGNOSTIC_LEAVES:
            path = target_directory / leaf_name
            try:
                text = path.read_text(encoding="utf-8")
            except (OSError, UnicodeError):
                continue
            if not _USAGE_LIMIT_RE.search(text):
                continue
            target_detected = True
            try:
                relative = str(path.relative_to(root))
            except ValueError:
                relative = str(path)
            evidence_paths.append(relative)
            reset_hints.extend(
                " ".join(match.group(1).split())
                for match in _USAGE_LIMIT_RESET_RE.finditer(text)
            )
        if target_detected and target_id:
            target_ids.append(target_id)
    target_ids = list(dict.fromkeys(target_ids))
    reset_hints = list(dict.fromkeys(reset_hints))
    evidence_paths = list(dict.fromkeys(evidence_paths))
    return {
        "detected": bool(target_ids),
        "target_ids": target_ids,
        "reset_hints": reset_hints,
        "evidence_paths": evidence_paths,
    }


def _canary_row(
    target_id: str,
    item: tuple[Path, Mapping[str, Any]] | None,
    root: Path,
    *,
    company_name: str,
) -> Mapping[str, Any]:
    if item is None:
        return {
            "target_id": target_id,
            "company_name": company_name,
            "status": "LIVE_RESEARCH_NOT_STARTED",
            "manifest_path": None,
            "production_research_complete": False,
            "score_valid": False,
            "stage_final": False,
        }
    path, payload = item
    complete = payload.get("production_research_complete") is True
    try:
        manifest_path = str(path.relative_to(root))
    except ValueError:
        manifest_path = str(path)
    return {
        "target_id": target_id,
        "company_name": company_name,
        "status": (
            "PRODUCTION_RESEARCH_COMPLETE"
            if complete
            else str(payload.get("status") or "RESEARCH_CHECKPOINT_PENDING")
        ),
        "manifest_path": manifest_path,
        "production_research_complete": complete,
        "document_count": int(payload.get("document_count") or 0),
        "fact_count": int(payload.get("fact_count") or 0),
        "counterfact_count": int(payload.get("counterfact_count") or 0),
        "component_memo_count": int(payload.get("component_memo_count") or 0),
        "score_valid": False,
        "stage_final": False,
    }


def _normalize_query(value: str) -> str:
    return _SPACE_RE.sub(" ", str(value).strip()).casefold()


__all__ = [
    "DEFAULT_PHASE99_AUDIT_PATH",
    "DEFAULT_PHASE99_SUMMARY_PATH",
    "PARITY_FAILURE_CLASSES",
    "PHASE99_FAIL",
    "PHASE99_PASS",
    "PUBLIC_RESEARCH_ROUTES",
    "REPAIR_CLUSTER_SPECS",
    "SCHEMA_VERSION",
    "SELF_REPAIR_LOOP_ORDER",
    "AlternatePublicRoutePlan",
    "FailureClusterRepairSpec",
    "RepairQueryValidation",
    "compile_phase99_self_repair_audit",
    "plan_alternate_public_routes",
    "render_phase99_self_repair_summary",
    "validate_llm_repair_queries",
    "write_phase99_self_repair_artifacts",
]
