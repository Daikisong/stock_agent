"""Goal 전용 25개 evidence-to-score known-bad 회귀 감사."""

from __future__ import annotations

import io
import unittest
from dataclasses import dataclass
from typing import Any, Mapping

from e2r.production.metadata import stable_hash


SCHEMA_VERSION = "e2r_evidence_to_score_known_bad_v1"
PASS_STATUS = "EVIDENCE_TO_SCORE_KNOWN_BAD_PASS"
FAIL_STATUS = "EVIDENCE_TO_SCORE_KNOWN_BAD_FAIL"


@dataclass(frozen=True)
class KnownBadCase:
    case_id: str
    mutation: str
    detector_ids: tuple[str, ...]


CASES = (
    KnownBadCase("KB-01", "SourceTask count로 100점을 균등분배", ("tests.test_canonical_archetype_scoring_contract.CanonicalArchetypeScoringContractTests.test_c06_uses_research_weights_not_source_task_count",)),
    KnownBadCase("KB-02", "모든 primitive를 material/green_required로 강제", ("tests.test_production_no_balanced_points.ProductionNoBalancedPointsTests.test_static_lockout_audit_has_zero_critical_counts",)),
    KnownBadCase("KB-03", "direct task closure만으로 점수 계산", ("tests.test_production_no_balanced_points.ProductionNoBalancedPointsTests.test_static_lockout_audit_has_zero_critical_counts",)),
    KnownBadCase("KB-04", "rerouted valid claim의 score impact를 폐기", ("tests.test_claim_many_to_many_impacts.ClaimManyToManyImpactTests.test_rerouted_impact_survives_without_closing_original_gap",)),
    KnownBadCase("KB-05", "rerouted claim이 original gap까지 닫음", ("tests.test_claim_many_to_many_impacts.ClaimManyToManyImpactTests.test_rerouted_impact_survives_without_closing_original_gap",)),
    KnownBadCase("KB-06", "한 claim의 복수 impact를 금지", ("tests.test_claim_many_to_many_impacts.ClaimManyToManyImpactTests.test_one_claim_can_support_multiple_primitive_and_component_impacts",)),
    KnownBadCase("KB-07", "동일 claim의 mapping ID를 나중 값으로 덮어씀", ("tests.test_claim_mapping_lineage_preserved.ClaimMappingLineagePreservedTests.test_same_claim_provenance_unions_every_mapping_id",)),
    KnownBadCase("KB-08", "동일 claim에 같은 경제적 credit을 중복 부여", ("tests.test_claim_many_to_many_impacts.ClaimManyToManyImpactTests.test_duplicate_economic_credit_is_rejected",)),
    KnownBadCase("KB-09", "claim 전체 credit budget을 초과", ("tests.test_impact_credit_caps.ImpactCreditCapsTests.test_claim_total_credit_budget_scales_many_components",)),
    KnownBadCase("KB-10", "한 component gap이 이미 확인된 component 점수를 삭제", ("tests.test_component_assessment_states.ComponentAssessmentStateTests.test_partial_component_score_is_preserved_while_other_components_unknown",)),
    KnownBadCase("KB-11", "VERIFIED_ABSENT_AFTER_SEARCH를 UNKNOWN으로 붕괴", ("tests.test_component_assessment_states.ComponentAssessmentStateTests.test_evaluated_absent_allows_terminal_full_thesis_assessment",)),
    KnownBadCase("KB-12", "UNKNOWN_UNINVESTIGATED를 0점 final로 확정", ("tests.test_component_assessment_states.ComponentAssessmentStateTests.test_unknown_and_provider_pending_block_finalization",)),
    KnownBadCase("KB-13", "provider pending 상태에서 full score 확정", ("tests.test_atomic_stagecourt_component_trace.AtomicStageCourtComponentTraceTests.test_pending_preserves_verified_score_and_does_not_finalize_stage",)),
    KnownBadCase("KB-14", "acceptance probe를 organic claim으로 계산", ("tests.test_acceptance_probe_not_organic.AcceptanceProbeNotOrganicTests.test_controlled_probe_claim_is_excluded_from_scoring_plane",)),
    KnownBadCase("KB-15", "NO_SCORE probe로 readiness를 PASS", ("tests.test_acceptance_probe_not_organic.AcceptanceProbeNotOrganicTests.test_probe_no_score_decision_cannot_unlock_scoring_readiness",)),
    KnownBadCase("KB-16", "calibrated profile을 사용하지 않고 점수 계산", ("tests.test_research_calibrated_component_scorer.ResearchCalibratedComponentScorerTests.test_component_vector_uses_c06_calibrated_maxima",)),
    KnownBadCase("KB-17", "historical outcome을 planner prompt에 누수", ("tests.test_historical_current_mode_separation.HistoricalCurrentModeSeparationTest.test_historical_prompt_is_blind_and_source_proxy_never_scores",)),
    KnownBadCase("KB-18", "Samsung Q1 ASP/record 실적을 customer allocation으로 과매핑", ("tests.test_samsung_q1_claim_component_impacts.SamsungQ1ClaimComponentImpactTests.test_asp_and_record_revenue_do_not_become_customer_allocation",)),
    KnownBadCase("KB-19", "Samsung Q1 claim의 bounded component impact까지 전부 폐기", ("tests.test_samsung_q1_claim_component_impacts.SamsungQ1ClaimComponentImpactTests.test_asp_and_record_revenue_keep_bounded_economic_impacts",)),
    KnownBadCase("KB-20", "qualification lag를 hard 4C로 강제", ("tests.test_c06_qualification_lag_guard.C06QualificationLagGuardTests.test_qualification_counter_does_not_force_hard_4c",)),
    KnownBadCase("KB-21", "HBM 키워드만으로 sold-out capacity를 생성", ("tests.test_samsung_q1_claim_component_impacts.SamsungQ1ClaimComponentImpactTests.test_hbm_product_keyword_does_not_become_sold_out_capacity",)),
    KnownBadCase("KB-22", "package substrate profile을 target HBM customer allocation으로 과매핑", ("tests.test_samsung_q1_claim_component_impacts.SamsungQ1ClaimComponentImpactTests.test_package_profile_does_not_become_target_hbm_allocation",)),
    KnownBadCase("KB-23", "Stage/score/component trace lineage 불일치 허용", ("tests.test_atomic_stagecourt_component_trace.AtomicStageCourtComponentTraceTests.test_score_impact_lineage_mismatch_is_rejected",)),
    KnownBadCase("KB-24", "organic canary claim이 0인데 READY", ("tests.test_final_readiness_requires_valid_score.FinalReadinessRequiresValidScoreTests.test_missing_dossiers_are_explicit_not_ready",)),
    KnownBadCase("KB-25", "full_score_valid=false인데 meaningful scoring READY", ("tests.test_final_readiness_requires_valid_score.FinalReadinessRequiresValidScoreTests.test_no_score_decision_cannot_pass_even_with_organic_claim",)),
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
    expected_ids = [f"KB-{index:02d}" for index in range(1, 26)]
    critical_counts = {
        "case_count_mismatch": abs(len(rows) - 25),
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
        "required_case_count": 25,
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
