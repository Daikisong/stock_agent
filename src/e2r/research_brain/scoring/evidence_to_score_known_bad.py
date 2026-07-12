"""Goal Phase 77 전용 semantic scoring known-bad 35종 회귀 감사."""

from __future__ import annotations

import io
import unittest
from dataclasses import dataclass
from typing import Any, Mapping

from e2r.production.metadata import stable_hash


SCHEMA_VERSION = "e2r_semantic_scoring_known_bad_v2"
PASS_STATUS = "SEMANTIC_SCORING_KNOWN_BAD_PASS"
FAIL_STATUS = "SEMANTIC_SCORING_KNOWN_BAD_FAIL"


@dataclass(frozen=True)
class KnownBadCase:
    case_id: str
    mutation: str
    detector_ids: tuple[str, ...]


CASES = (
    KnownBadCase("KB-01", "PARTIAL_BRIDGE cap 누락이 조용히 0점", ("tests.test_partial_bridge_nonzero_policy.PartialBridgeNonzeroPolicyTests.test_partial_bridge_has_research_backed_nonzero_cap",)),
    KnownBadCase("KB-02", "RISK_OPEN cap 누락이 조용히 0점", ("tests.test_risk_direction_policy.RiskDirectionPolicyTests.test_risk_open_is_counter_only_and_nonzero",)),
    KnownBadCase("KB-03", "RISK_RESOLVED cap 누락이 조용히 0점", ("tests.test_risk_direction_policy.RiskDirectionPolicyTests.test_risk_resolved_releases_but_does_not_keep_penalty",)),
    KnownBadCase("KB-04", "source family cap 누락이 조용히 0점", ("tests.test_no_silent_zero_cap.NoSilentZeroCapTests.test_unknown_source_family_is_hard_error_not_zero_credit",)),
    KnownBadCase("KB-05", "temporal cap 누락이 조용히 0점", ("tests.test_no_silent_zero_cap.NoSilentZeroCapTests.test_unknown_temporal_scope_is_hard_error_not_zero_credit",)),
    KnownBadCase("KB-06", "SUPPORTED 질문이 zero-credit", ("tests.test_semantic_closure_reconciler.SemanticClosureReconcilerTests.test_supported_scoring_without_credit_is_pipeline_error",)),
    KnownBadCase("KB-07", "PARTIALLY_SUPPORTED 질문이 zero-credit", ("tests.test_semantic_closure_reconciler.SemanticClosureReconcilerTests.test_partially_supported_scoring_without_credit_is_pipeline_error",)),
    KnownBadCase("KB-08", "SUPPORTED 질문이 VERIFIED_ABSENT", ("tests.test_semantic_closure_reconciler.SemanticClosureReconcilerTests.test_supported_question_cannot_be_reconciled_as_verified_absent",)),
    KnownBadCase("KB-09", "positive claim이 VERIFIED_ABSENT", ("tests.test_semantic_closure_reconciler.SemanticClosureReconcilerTests.test_positive_claim_cannot_be_reconciled_as_verified_absent",)),
    KnownBadCase("KB-10", "internal rejection이 absence로 위장", ("tests.test_semantic_closure_reconciler.SemanticClosureReconcilerTests.test_internal_rejection_cannot_be_relabelled_as_absence",)),
    KnownBadCase("KB-11", "provider failure가 absence", ("tests.test_semantic_closure_reconciler.SemanticClosureReconcilerTests.test_absence_never_masks_provider_or_search_failure",)),
    KnownBadCase("KB-12", "budget exhaustion이 absence", ("tests.test_absence_requires_adequate_search.AbsenceRequiresAdequateSearchTests.test_budget_exhaustion_is_pending_never_absence",)),
    KnownBadCase("KB-13", "Foundry Tesla claim이 HBM allocation 지원", ("tests.test_foundry_not_hbm_allocation.FoundryNotHBMAllocationTests.test_tesla_foundry_claim_stays_global_but_c06_impact_is_rerouted",)),
    KnownBadCase("KB-14", "same issuer wrong segment score", ("tests.test_business_mechanism_scope.BusinessMechanismScopeTests.test_same_issuer_wrong_segment_is_rejected_and_rerouted",)),
    KnownBadCase("KB-15", "adjacent substrate가 target HBM capacity", ("tests.test_business_mechanism_scope.BusinessMechanismScopeTests.test_adjacent_substrate_cannot_be_target_hbm_capacity",)),
    KnownBadCase("KB-16", "accepted claim eligibility boolean 모순", ("tests.test_claim_eligibility_decision.ClaimEligibilityDecisionTests.test_operational_eligibility_audit_ignores_legacy_boolean_for_scoring",)),
    KnownBadCase("KB-17", "component score without eligibility decision", ("tests.test_claim_many_to_many_impacts.ClaimManyToManyImpactTests.test_component_score_requires_explicit_eligibility_decision",)),
    KnownBadCase("KB-18", "support+counter인데 counter 무시", ("tests.test_counter_component_math.CounterComponentMathTests.test_open_counter_blocks_finalization_and_preserves_both_planes",)),
    KnownBadCase("KB-19", "capacity expansion counter가 bottleneck에 0", ("tests.test_counter_component_math.CounterComponentMathTests.test_capacity_counter_in_another_subcriterion_caps_same_component",)),
    KnownBadCase("KB-20", "risk resolved가 계속 감점", ("tests.test_counter_component_math.CounterComponentMathTests.test_linked_resolution_releases_penalty_without_erasing_history",)),
    KnownBadCase("KB-21", "같은 fact 여러 claim 중복 credit", ("tests.test_fact_cluster_dedupe.FactClusterDedupeTests.test_same_economic_fact_across_claims_and_documents_gets_one_credit",)),
    KnownBadCase("KB-22", "같은 document 여러 claim 정보신뢰도 중복", ("tests.test_document_cluster_credit_cap.DocumentClusterCreditCapTests.test_same_document_claim_fragments_do_not_stack_information_confidence",)),
    KnownBadCase("KB-23", "repost 여러 문서 중복 credit", ("tests.test_agentic_evidence_os.AgenticEvidenceOSTests.test_twenty_reuters_reposts_count_as_one_source_family",)),
    KnownBadCase("KB-24", "claim 수만으로 company_event_score 60", ("tests.test_stagecourt_event_separation.StageCourtEventSeparationTests.test_claim_count_and_event_overlay_never_change_full_thesis_stage",)),
    KnownBadCase("KB-25", "any claim이 high_quality_company_event", ("tests.test_atomic_stagecourt_component_trace.AtomicStageCourtComponentTraceTests.test_accepted_claim_is_not_implicitly_a_high_quality_event",)),
    KnownBadCase("KB-26", "full-thesis Stage에 daily event overlay 주입", ("tests.test_stagecourt_event_separation.StageCourtEventSeparationTests.test_explicit_quality_contract_creates_overlay_only",)),
    KnownBadCase("KB-27", "gold URL production seed 주입", ("tests.test_gold_research_blindness.GoldResearchBlindnessTests.test_same_source_may_be_rediscovered_but_cannot_be_a_seed",)),
    KnownBadCase("KB-28", "gold fact production prompt 누수", ("tests.test_gold_research_blindness.GoldResearchBlindnessTests.test_isolated_lanes_pass_without_gold_input_leakage",)),
    KnownBadCase("KB-29", "critical gold material fact miss인데 PASS", ("tests.test_gold_research_blindness.GoldResearchBlindnessTests.test_critical_gold_miss_cannot_pass_on_raw_source_count",)),
    KnownBadCase("KB-30", "frozen corpus bug를 새 문서로 가림", ("tests.test_frozen_52f09f3_repair.Frozen52f09f3RepairTests.test_same_documents_claims_and_provenance_are_byte_identical",)),
    KnownBadCase("KB-31", "source proxy score", ("tests.test_claim_eligibility_decision.ClaimEligibilityDecisionTests.test_source_proxy_can_stay_ledgered_but_not_score",)),
    KnownBadCase("KB-32", "historical outcome prompt leak", ("tests.test_historical_current_mode_separation.HistoricalCurrentModeSeparationTest.test_historical_prompt_is_blind_and_source_proxy_never_scores",)),
    KnownBadCase("KB-33", "Stage/score/impact/component trace mismatch", ("tests.test_atomic_stagecourt_component_trace.AtomicStageCourtComponentTraceTests.test_score_impact_lineage_mismatch_is_rejected",)),
    KnownBadCase("KB-34", "full_score_valid인데 semantic reconciliation fail", ("tests.test_full_score_validity_v2.FullScoreValidityV2Tests.test_invalid_semantics_preserve_verified_score_and_interval",)),
    KnownBadCase("KB-35", "report-only readiness 승격", ("tests.test_meaningful_scoring_readiness_v3.MeaningfulScoringReadinessV3Tests.test_each_required_semantic_counter_blocks_report_only_pass",)),
)


class _RecordingResult(unittest.TextTestResult):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.passed_ids: set[str] = set()

    def addSuccess(self, test: unittest.case.TestCase) -> None:  # noqa: N802
        super().addSuccess(test)
        self.passed_ids.add(test.id())


def compile_evidence_to_score_known_bad_audit() -> Mapping[str, Any]:
    detector_ids = tuple(dict.fromkeys(detector for case in CASES for detector in case.detector_ids))
    loader = unittest.TestLoader()
    suite = unittest.TestSuite(loader.loadTestsFromName(detector) for detector in detector_ids)
    stream = io.StringIO()
    result = unittest.TextTestRunner(stream=stream, verbosity=0, resultclass=_RecordingResult).run(suite)
    rows = []
    for case in CASES:
        missing = tuple(detector for detector in case.detector_ids if detector not in result.passed_ids)
        rows.append(
            {
                "case_id": case.case_id,
                "mutation": case.mutation,
                "detector_ids": list(case.detector_ids),
                "status": "PASS" if not missing else "FAIL",
                "failed_detector_ids": list(missing),
            }
        )
    observed_ids = [row["case_id"] for row in rows]
    expected_ids = [f"KB-{index:02d}" for index in range(1, 36)]
    critical_counts = {
        "case_count_mismatch": abs(len(rows) - 35),
        "case_id_roster_mismatch": len(set(observed_ids) ^ set(expected_ids)),
        "duplicate_case_id_count": len(observed_ids) - len(set(observed_ids)),
        "failed_case_count": sum(row["status"] != "PASS" for row in rows),
        "unittest_error_count": len(result.errors),
        "unittest_failure_count": len(result.failures),
        "unittest_run_count_mismatch": abs(result.testsRun - len(detector_ids)),
    }
    critical_sum = sum(critical_counts.values())
    lineage = {
        "case_registry_hash": stable_hash([case.__dict__ for case in CASES]),
        "unique_detector_count": len(detector_ids),
        "executed_detector_count": result.testsRun,
        "passed_detector_count": len(result.passed_ids),
    }
    return {
        "schema_version": SCHEMA_VERSION,
        "status": PASS_STATUS if critical_sum == 0 else FAIL_STATUS,
        "required_case_count": 35,
        "case_count": len(rows),
        "cases": rows,
        "detector_lineage": lineage,
        "critical_counts": critical_counts,
        "critical_count_sum": critical_sum,
        "runner_output": stream.getvalue() if critical_sum else "",
    }


__all__ = [
    "CASES",
    "FAIL_STATUS",
    "PASS_STATUS",
    "SCHEMA_VERSION",
    "compile_evidence_to_score_known_bad_audit",
]
