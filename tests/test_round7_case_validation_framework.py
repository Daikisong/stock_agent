import tempfile
from pathlib import Path
import unittest

from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import E2RCaseRecord, PriceValidation
from e2r.sector.round7_case_validation_framework import (
    ROUND7_COUNTEREXAMPLE_CRITERIA,
    ROUND7_PRICE_VALIDATION_FIELDS,
    ROUND7_SUCCESS_CRITERIA,
    Round7StagePosture,
    Round7ValidationBucket,
    classify_round7_case,
    render_round7_rules_markdown,
    round7_archetype_validation_rows,
    round7_case_validation_gaps,
    round7_rule_for,
    round7_stage_posture_for,
    write_round7_case_validation_reports,
)


class Round7CaseValidationFrameworkTests(unittest.TestCase):
    def test_round7_success_and_counterexample_criteria_require_score_price_eps_alignment(self):
        self.assertIn("price_rerating_after_signal", ROUND7_SUCCESS_CRITERIA)
        self.assertIn("eps_op_fcf_revision_confirmed", ROUND7_SUCCESS_CRITERIA)
        self.assertIn("price_up_without_eps_fcf", ROUND7_COUNTEREXAMPLE_CRITERIA)
        self.assertIn("score_high_but_price_no_rerating", ROUND7_COUNTEREXAMPLE_CRITERIA)

        markdown = render_round7_rules_markdown()
        self.assertIn("Stage 2/3", markdown)
        self.assertIn("mfe_90d", ROUND7_PRICE_VALIDATION_FIELDS)

    def test_platform_rule_requires_monetization_and_rejects_ai_or_mau_only(self):
        rule = round7_rule_for(E2RArchetype.PLATFORM_SOFTWARE_INTERNET)

        self.assertEqual(rule.posture, Round7StagePosture.WATCH_YELLOW_DEFAULT)
        self.assertIn("arpu_or_take_rate_up", rule.success_requires)
        self.assertIn("ai_cost_not_hurting_fcf", rule.success_requires)
        self.assertIn("mau_or_ai_narrative_without_op_fcf", rule.counterexample_triggers)
        self.assertIn("governance_or_legal_risk", rule.counterexample_triggers)

    def test_cdmo_is_separated_from_pre_revenue_biotech(self):
        cdmo = round7_rule_for(E2RArchetype.CDMO_HEALTHCARE_CONTRACT)
        pre_revenue = round7_stage_posture_for(E2RArchetype.BIOTECH_PRE_REVENUE_REGULATORY)

        self.assertEqual(cdmo.posture, Round7StagePosture.GREEN_ELIGIBLE_AFTER_VALIDATION)
        self.assertIn("long_term_production_contract", cdmo.success_requires)
        self.assertIn("capacity_utilization_ramp", cdmo.success_requires)
        self.assertIn("patent_or_litigation_risk", cdmo.counterexample_triggers)
        self.assertEqual(pre_revenue, Round7StagePosture.REDTEAM_GUARDRAIL)

    def test_travel_and_rare_metals_are_watch_yellow_not_default_green(self):
        travel = round7_rule_for(E2RArchetype.TRAVEL_LEISURE_REOPENING)
        rare = round7_rule_for(E2RArchetype.RARE_METALS_STRATEGIC_MATERIALS)

        self.assertEqual(travel.posture, Round7StagePosture.WATCH_YELLOW_DEFAULT)
        self.assertIn("one_time_reopening", travel.counterexample_triggers)
        self.assertEqual(rare.posture, Round7StagePosture.WATCH_YELLOW_DEFAULT)
        self.assertIn("takeover_premium_only", rare.counterexample_triggers)

    def test_every_archetype_has_round7_posture_and_matrix_row(self):
        rows = round7_archetype_validation_rows()
        by_archetype = {row["archetype"]: row for row in rows}

        self.assertEqual(len(rows), len(tuple(E2RArchetype)))
        self.assertEqual(
            by_archetype[E2RArchetype.CONSTRUCTION_REAL_ESTATE_CREDIT.value]["posture"],
            Round7StagePosture.REDTEAM_GUARDRAIL.value,
        )
        self.assertEqual(
            by_archetype[E2RArchetype.MEMORY_HBM_CAPACITY.value]["posture"],
            Round7StagePosture.GREEN_ELIGIBLE_AFTER_VALIDATION.value,
        )

    def test_classify_round7_case_detects_success_and_counterexamples(self):
        success = _record("success", "aligned", "true_rerating", "success_candidate", "price_filled")
        no_price = _record("needs", "unknown", "unknown", "success_candidate", "needs_price_backfill")
        price_only = _record("price_only", "price_moved_without_evidence", "theme_overheat", "overheat", "price_filled")
        failed = _record("failed", "evidence_good_but_price_failed", "no_rerating", "failed_rerating", "price_filled")
        event = _record("event", "unknown", "event_premium", "event_premium", "price_filled")

        self.assertEqual(classify_round7_case(success), Round7ValidationBucket.SUCCESS_VALIDATION)
        self.assertEqual(classify_round7_case(no_price), Round7ValidationBucket.NEEDS_PRICE_PATH)
        self.assertEqual(classify_round7_case(price_only), Round7ValidationBucket.PRICE_WITHOUT_EPS)
        self.assertEqual(classify_round7_case(failed), Round7ValidationBucket.SCORE_WEIGHT_FAILURE)
        self.assertEqual(classify_round7_case(event), Round7ValidationBucket.EVENT_PREMIUM_ONLY)

    def test_case_gap_report_counts_validation_buckets(self):
        rows = round7_case_validation_gaps(
            (
                _record("success", "aligned", "true_rerating", "success_candidate", "price_filled"),
                _record("failed", "evidence_good_but_price_failed", "no_rerating", "failed_rerating", "price_filled"),
            )
        )
        by_archetype = {row["archetype"]: row for row in rows}
        platform = by_archetype[E2RArchetype.PLATFORM_SOFTWARE_INTERNET.value]

        self.assertEqual(platform["success_validation_count"], 1)
        self.assertEqual(platform["score_weight_failure_count"], 1)
        self.assertEqual(platform["next_action"], "ready_for_shadow_score_review")

    def test_report_writer_outputs_round7_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round7_case_validation_reports(output_directory=tmp)

            self.assertTrue(paths["framework"].exists())
            self.assertTrue(paths["rules"].exists())
            self.assertTrue(paths["matrix"].exists())
            self.assertTrue(paths["gaps"].exists())
            self.assertTrue(paths["next_plan"].exists())
            self.assertIn("Round-7 Case Validation", paths["framework"].read_text(encoding="utf-8"))

    def test_production_scoring_modules_do_not_import_round7_framework(self):
        paths = [
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ]
        for path in paths:
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round7_case_validation_framework", text)


def _record(
    case_id: str,
    alignment: str,
    rerating_result: str,
    case_type: str,
    price_status: str,
) -> E2RCaseRecord:
    return E2RCaseRecord(
        case_id=case_id,
        symbol=f"T{case_id}",
        company_name=f"테스트 {case_id}",
        market="KR",
        sector_raw="플랫폼",
        primary_archetype=E2RArchetype.PLATFORM_SOFTWARE_INTERNET,
        expected_group=case_type,
        case_type=case_type,
        score_price_alignment=alignment,
        rerating_result=rerating_result,
        price_validation=PriceValidation(price_validation_status=price_status),
    )


if __name__ == "__main__":
    unittest.main()
