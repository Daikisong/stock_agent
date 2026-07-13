"""Phase 98 researcher capability and semantic known-bad regression registry.

The registry intentionally points at executable tests instead of declaring a
static checklist PASS.  Phase 98 is a test-mode acceptance layer: production
scores still come only from source-backed facts, component judges, the
deterministic aggregator, and StageCourt.
"""

from __future__ import annotations

import io
import unittest
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping

from e2r.production.metadata import stable_hash, write_json


SCHEMA_VERSION = "e2r_v5_phase98_capability_regression_v1"
PHASE98_PASS = "PHASE98_CAPABILITY_AND_KNOWN_BAD_PASS"
PHASE98_FAIL = "PHASE98_CAPABILITY_AND_KNOWN_BAD_FAIL"
DEFAULT_PHASE98_OUTPUT_PATH = Path(
    "docs/operational/e2r_v5_capability_known_bad_audit.json"
)


@dataclass(frozen=True)
class CapabilityRegressionCase:
    case_id: str
    case_type: str
    requirement: str
    detector_ids: tuple[str, ...]

    def __post_init__(self) -> None:
        if self.case_type not in {"POSITIVE_CAPABILITY", "SEMANTIC_KNOWN_BAD"}:
            raise ValueError("unknown Phase 98 case type")
        if not self.case_id or not self.requirement or not self.detector_ids:
            raise ValueError("Phase 98 cases require identity, requirement, and detectors")


_PHASE98_TEST = (
    "tests.test_e2r_v5_phase98_capability_regression."
    "E2RV5Phase98PositiveCapabilityTests"
)


POSITIVE_CAPABILITY_CASES = (
    CapabilityRegressionCase(
        "POS-01",
        "POSITIVE_CAPABILITY",
        "HBM sold-out, revenue mix, and record profit produce material visibility, bottleneck, and EPS points",
        (f"{_PHASE98_TEST}.test_hbm_sold_out_mix_and_record_profit_score_three_material_components",),
    ),
    CapabilityRegressionCase(
        "POS-02",
        "POSITIVE_CAPABILITY",
        "official ASP and actual profit produce pricing and EPS points",
        (f"{_PHASE98_TEST}.test_official_asp_and_actual_profit_score_pricing_and_eps",),
    ),
    CapabilityRegressionCase(
        "POS-03",
        "POSITIVE_CAPABILITY",
        "named-customer order produces visibility and customer-quality confidence points",
        (f"{_PHASE98_TEST}.test_named_customer_order_scores_visibility_and_information_quality",),
    ),
    CapabilityRegressionCase(
        "POS-04",
        "POSITIVE_CAPABILITY",
        "public valuation and forward EPS produce nonzero valuation points",
        (f"{_PHASE98_TEST}.test_public_valuation_and_forward_eps_score_valuation",),
    ),
    CapabilityRegressionCase(
        "POS-05",
        "POSITIVE_CAPABILITY",
        "upward consensus revision produces mispricing and visibility points",
        (f"{_PHASE98_TEST}.test_upward_consensus_revision_scores_mispricing_and_visibility",),
    ),
    CapabilityRegressionCase(
        "POS-06",
        "POSITIVE_CAPABILITY",
        "counter capacity expansion can reduce the net bottleneck score",
        (f"{_PHASE98_TEST}.test_capacity_expansion_counter_reduces_net_bottleneck_score",),
    ),
    CapabilityRegressionCase(
        "POS-07",
        "POSITIVE_CAPABILITY",
        "independent corroboration raises confidence without duplicating economic points",
        (f"{_PHASE98_TEST}.test_independent_corroboration_raises_confidence_not_points",),
    ),
)


KNOWN_BAD_CASES = (
    CapabilityRegressionCase(
        "BAD-01",
        "SEMANTIC_KNOWN_BAD",
        "keyword-only text is promoted to support",
        (
            "tests.test_census_v4_all_archetype_replay_matrix.CensusV4AllArchetypeReplayMatrixTests."
            "test_c28_source_backed_semantic_replay_passes_security_keyword_guard",
        ),
    ),
    CapabilityRegressionCase(
        "BAD-02",
        "SEMANTIC_KNOWN_BAD",
        "no extracted claim is relabelled as verified absence",
        (
            "tests.test_absence_requires_adequate_search.AbsenceRequiresAdequateSearchTests."
            "test_absence_provider_pending_and_evidence_found_are_distinct",
        ),
    ),
    CapabilityRegressionCase(
        "BAD-03",
        "SEMANTIC_KNOWN_BAD",
        "provider failure becomes a zero score",
        (
            "tests.test_e2r_v5_researcher_mode.E2RV5ResearcherModeTests."
            "test_provider_outage_is_research_pending_without_score_or_stage",
        ),
    ),
    CapabilityRegressionCase(
        "BAD-04",
        "SEMANTIC_KNOWN_BAD",
        "missing an exact primitive zeros the entire component",
        (
            "tests.test_e2r_v5_researcher_mode.E2RV5ResearcherModeTests."
            "test_component_research_accepts_material_fact_without_exact_primitive",
        ),
    ),
    CapabilityRegressionCase(
        "BAD-05",
        "SEMANTIC_KNOWN_BAD",
        "a source proxy is used as the current exact score",
        (
            "tests.test_e2r_v5_all_archetype_generalization.E2RV5AllArchetypeGeneralizationTests."
            "test_source_proxy_is_never_an_exact_current_score_anchor",
        ),
    ),
    CapabilityRegressionCase(
        "BAD-06",
        "SEMANTIC_KNOWN_BAD",
        "a Foundry fact is credited as HBM evidence",
        (
            "tests.test_foundry_not_hbm_allocation.FoundryNotHBMAllocationTests."
            "test_tesla_foundry_claim_stays_global_but_c06_impact_is_rerouted",
        ),
    ),
    CapabilityRegressionCase(
        "BAD-07",
        "SEMANTIC_KNOWN_BAD",
        "same issuer but wrong segment receives target-segment credit",
        (
            "tests.test_business_mechanism_scope.BusinessMechanismScopeTests."
            "test_same_issuer_wrong_segment_is_rejected_and_rerouted",
        ),
    ),
    CapabilityRegressionCase(
        "BAD-08",
        "SEMANTIC_KNOWN_BAD",
        "industry-wide demand is promoted to an issuer-specific order",
        (
            "tests.test_unified_known_bad_suite.UnifiedKnownBadSuiteTest."
            "test_semantic_and_claim_mutations_are_detected",
        ),
    ),
    CapabilityRegressionCase(
        "BAD-09",
        "SEMANTIC_KNOWN_BAD",
        "customer capacity is promoted to target-company capacity",
        (
            "tests.test_unified_known_bad_suite.UnifiedKnownBadSuiteTest."
            "test_semantic_and_claim_mutations_are_detected",
        ),
    ),
    CapabilityRegressionCase(
        "BAD-10",
        "SEMANTIC_KNOWN_BAD",
        "an old resolved risk remains a current penalty",
        (
            "tests.test_census_v4_known_bad_regression.CensusV4KnownBadRegressionTests."
            "test_old_risk_resolved_case_is_required_known_bad",
        ),
    ),
    CapabilityRegressionCase(
        "BAD-11",
        "SEMANTIC_KNOWN_BAD",
        "qualification lag alone forces hard Stage 4C",
        (
            "tests.test_c06_qualification_lag_guard.C06QualificationLagGuardTests."
            "test_qualification_counter_does_not_force_hard_4c",
        ),
    ),
    CapabilityRegressionCase(
        "BAD-12",
        "SEMANTIC_KNOWN_BAD",
        "duplicate claims for one economic fact stack points",
        (
            "tests.test_e2r_v5_evidence_fact_graph.E2RV5EvidenceFactGraphTests."
            "test_same_economic_fact_gets_one_fact_and_independent_confidence_gain",
        ),
    ),
    CapabilityRegressionCase(
        "BAD-13",
        "SEMANTIC_KNOWN_BAD",
        "claim count or event overlay boosts canonical Stage",
        (
            "tests.test_stagecourt_event_separation.StageCourtEventSeparationTests."
            "test_claim_count_and_event_overlay_never_change_full_thesis_stage",
        ),
    ),
    CapabilityRegressionCase(
        "BAD-14",
        "SEMANTIC_KNOWN_BAD",
        "future outcome leaks into historical replay research",
        (
            "tests.test_e2r_v5_historical_blind_replay.E2RV5HistoricalBlindReplayTests."
            "test_provider_receives_no_historical_score_stage_or_outcome",
        ),
    ),
    CapabilityRegressionCase(
        "BAD-15",
        "SEMANTIC_KNOWN_BAD",
        "historical total or partial vector is copied into the current score",
        (
            "tests.test_e2r_v5_historical_blind_replay.E2RV5HistoricalBlindReplayTests."
            "test_partial_historical_vector_is_not_used_as_total_proxy",
        ),
    ),
    CapabilityRegressionCase(
        "BAD-16",
        "SEMANTIC_KNOWN_BAD",
        "a low fixed cap is treated as semantic saturation",
        (
            "tests.test_e2r_v5_semantic_research_saturation.E2RV5SemanticResearchSaturationTests."
            "test_fixed_round_zero_result_and_transport_flags_are_rejected",
        ),
    ),
    CapabilityRegressionCase(
        "BAD-17",
        "SEMANTIC_KNOWN_BAD",
        "Gold benchmark URLs are injected into production discovery",
        (
            "tests.test_e2r_v5_full_thesis_gold_benchmark.E2RV5FullThesisGoldBenchmarkTests."
            "test_gold_seed_url_injection_fails_post_run_gate",
        ),
    ),
    CapabilityRegressionCase(
        "BAD-18",
        "SEMANTIC_KNOWN_BAD",
        "high, middle, and low historical cases all collapse below 30",
        (
            "tests.test_e2r_v5_historical_blind_replay.E2RV5HistoricalBlindReplayTests."
            "test_dynamic_range_audit_fails_when_high_mid_low_all_collapse_to_twenty",
        ),
    ),
    CapabilityRegressionCase(
        "BAD-19",
        "SEMANTIC_KNOWN_BAD",
        "strong anchor-equivalent evidence is undercredited to one-to-three points",
        (
            "tests.test_e2r_v5_deterministic_score_aggregator.E2RV5DeterministicScoreAggregatorTests."
            "test_strong_high_anchor_equivalent_evidence_does_not_collapse_to_one_to_three_points",
        ),
    ),
    CapabilityRegressionCase(
        "BAD-20",
        "SEMANTIC_KNOWN_BAD",
        "a current score changes without fact and judge lineage",
        (
            "tests.test_atomic_stagecourt_component_trace.AtomicStageCourtComponentTraceTests."
            "test_score_impact_lineage_mismatch_is_rejected",
            "tests.test_e2r_v5_daily_census_integration.E2RV5DailyCensusIntegrationTests."
            "test_l5_materializer_rejects_transport_completion_and_vector_tamper",
        ),
    ),
)


PHASE98_CASES = (*POSITIVE_CAPABILITY_CASES, *KNOWN_BAD_CASES)


class _RecordingResult(unittest.TextTestResult):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.passed_ids: set[str] = set()

    def addSuccess(self, test: unittest.case.TestCase) -> None:  # noqa: N802
        super().addSuccess(test)
        self.passed_ids.add(test.id())


def compile_phase98_capability_regression_audit() -> Mapping[str, Any]:
    """Execute every registered detector and compile an exact Phase 98 leaf."""

    detector_ids = tuple(
        dict.fromkeys(
            detector_id
            for case in PHASE98_CASES
            for detector_id in case.detector_ids
        )
    )
    suite = unittest.TestSuite(
        unittest.TestLoader().loadTestsFromName(detector_id)
        for detector_id in detector_ids
    )
    stream = io.StringIO()
    result = unittest.TextTestRunner(
        stream=stream,
        verbosity=0,
        resultclass=_RecordingResult,
    ).run(suite)
    rows = []
    for case in PHASE98_CASES:
        failed = tuple(
            detector_id
            for detector_id in case.detector_ids
            if detector_id not in result.passed_ids
        )
        rows.append(
            {
                "case_id": case.case_id,
                "case_type": case.case_type,
                "requirement": case.requirement,
                "detector_ids": list(case.detector_ids),
                "status": "PASS" if not failed else "FAIL",
                "failed_detector_ids": list(failed),
            }
        )

    expected_ids = [
        *(f"POS-{index:02d}" for index in range(1, 8)),
        *(f"BAD-{index:02d}" for index in range(1, 21)),
    ]
    actual_ids = [row["case_id"] for row in rows]
    critical_counts = {
        "positive_case_count_mismatch": abs(len(POSITIVE_CAPABILITY_CASES) - 7),
        "known_bad_case_count_mismatch": abs(len(KNOWN_BAD_CASES) - 20),
        "case_id_roster_mismatch": len(set(actual_ids) ^ set(expected_ids)),
        "duplicate_case_id_count": len(actual_ids) - len(set(actual_ids)),
        "failed_case_count": sum(row["status"] != "PASS" for row in rows),
        "unittest_error_count": len(result.errors),
        "unittest_failure_count": len(result.failures),
        "unittest_run_count_mismatch": abs(result.testsRun - len(detector_ids)),
    }
    critical_sum = sum(critical_counts.values())
    return {
        "schema_version": SCHEMA_VERSION,
        "status": PHASE98_PASS if critical_sum == 0 else PHASE98_FAIL,
        "test_mode_only": True,
        "production_readiness_authority": False,
        "required_positive_case_count": 7,
        "required_known_bad_case_count": 20,
        "positive_case_count": len(POSITIVE_CAPABILITY_CASES),
        "known_bad_case_count": len(KNOWN_BAD_CASES),
        "case_count": len(rows),
        "cases": rows,
        "detector_lineage": {
            "registry_hash": stable_hash(
                [
                    {
                        "case_id": case.case_id,
                        "case_type": case.case_type,
                        "requirement": case.requirement,
                        "detector_ids": list(case.detector_ids),
                    }
                    for case in PHASE98_CASES
                ]
            ),
            "unique_detector_count": len(detector_ids),
            "executed_detector_count": result.testsRun,
            "passed_detector_count": len(result.passed_ids),
        },
        "critical_counts": critical_counts,
        "critical_count_sum": critical_sum,
        "runner_output": stream.getvalue() if critical_sum else "",
    }


def write_phase98_capability_regression_audit(
    output_path: str | Path = DEFAULT_PHASE98_OUTPUT_PATH,
) -> Path:
    destination = Path(output_path)
    write_json(destination, compile_phase98_capability_regression_audit())
    return destination


__all__ = [
    "DEFAULT_PHASE98_OUTPUT_PATH",
    "KNOWN_BAD_CASES",
    "PHASE98_CASES",
    "PHASE98_FAIL",
    "PHASE98_PASS",
    "POSITIVE_CAPABILITY_CASES",
    "SCHEMA_VERSION",
    "CapabilityRegressionCase",
    "compile_phase98_capability_regression_audit",
    "write_phase98_capability_regression_audit",
]
