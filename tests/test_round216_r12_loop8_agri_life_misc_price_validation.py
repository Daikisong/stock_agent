from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round216_r12_loop8_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round216_r12_loop8_agri_life_misc_price_validation import (
    ROUND216_CASE_CANDIDATES,
    ROUND216_DEFAULT_STAGE3_BIAS,
    ROUND216_GREEN_FORBIDDEN_PATTERNS,
    ROUND216_GREEN_REQUIRED_FIELDS,
    ROUND216_HARD_4C_GATES,
    ROUND216_PRICE_VALIDATION_FIELDS,
    ROUND216_REQUIRED_TARGET_ALIASES,
    ROUND216_SCORE_ADJUSTMENTS,
    ROUND216_SHADOW_WEIGHT_ROWS,
    ROUND216_STAGE4B_WATCH_TRIGGERS,
    render_round216_green_gate_review_markdown,
    render_round216_stage4b_4c_review_markdown,
    round216_audit_payload,
    round216_case_records,
    round216_deep_sub_archetype_rows,
    round216_shadow_weight_rows,
    round216_summary,
    write_round216_r12_loop8_reports,
)


class Round216R12Loop8AgriLifeMiscPriceValidationTests(unittest.TestCase):
    def test_targets_are_existing_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertGreaterEqual(len(ROUND216_REQUIRED_TARGET_ALIASES), 15)
        self.assertTrue(set(ROUND216_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND216_REQUIRED_TARGET_ALIASES["EDUCATION_POLICY_EVENT"],
            E2RArchetype.EDUCATION_POLICY_EVENT.value,
        )
        self.assertEqual(
            ROUND216_REQUIRED_TARGET_ALIASES["FOOD_SERVICE_EVENT_PREMIUM"],
            E2RArchetype.FOOD_SERVICE_EVENT_PREMIUM.value,
        )
        self.assertEqual(
            ROUND216_REQUIRED_TARGET_ALIASES["HOME_LIVING_APPLIANCE_RENTAL"],
            E2RArchetype.HOME_LIVING_APPLIANCE_RENTAL.value,
        )

    def test_case_records_validate_and_keep_calibration_only_bias(self) -> None:
        records = round216_case_records()
        for record in records:
            record.validate()
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("r12_default_stage3_bias_conservative_except_recurring_service", record.green_guardrails)
            self.assertIsNone(record.stage3_date)

        summary = round216_summary()
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["success_candidate_count"], 3)
        self.assertEqual(summary["event_premium_count"], 3)
        self.assertEqual(summary["overheat_count"], 1)
        self.assertEqual(summary["watch_count"], 1)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["r12_default_stage3_bias"], ROUND216_DEFAULT_STAGE3_BIAS)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])

    def test_coway_is_structural_service_candidate_but_not_green(self) -> None:
        coway = next(
            case
            for case in ROUND216_CASE_CANDIDATES
            if case.case_id == "r12_loop8_coway_recurring_rental_service_candidate"
        )

        self.assertEqual(coway.symbol, "021240")
        self.assertEqual(coway.primary_archetype, E2RArchetype.HOME_LIVING_APPLIANCE_RENTAL)
        self.assertEqual(coway.case_type, "success_candidate")
        self.assertIn("recurring_account_base", coway.evidence_fields)
        self.assertIn("churn_unverified", coway.red_flag_fields)
        self.assertIn("arpu_unverified", coway.red_flag_fields)
        self.assertIn("fcf_conversion_unverified", coway.red_flag_fields)
        self.assertIsNone(coway.stage3_date)

    def test_agri_machinery_and_smart_farm_require_unit_economics(self) -> None:
        by_id = {case.case_id: case for case in ROUND216_CASE_CANDIDATES}
        agri = by_id["r12_loop8_daedong_tym_agri_machinery_export_watch"]
        smart_farm = by_id["r12_loop8_smart_farm_unit_economics_watch"]

        self.assertEqual(agri.primary_archetype, E2RArchetype.AGRI_MACHINERY_DEMAND_CYCLE)
        self.assertIn(E2RArchetype.AGRI_MACHINERY_SOFTWARE_LOCKIN, agri.secondary_archetypes)
        self.assertIn("dealer_inventory_unknown", agri.red_flag_fields)
        self.assertIsNone(agri.stage3_date)

        self.assertEqual(smart_farm.primary_archetype, E2RArchetype.SMART_FARM_AGRI_TECH)
        self.assertIn("smart_farm_theme_only", smart_farm.red_flag_fields)
        self.assertIn("unit_economics_unverified", smart_farm.red_flag_fields)
        self.assertEqual(smart_farm.extra_price_metrics["uav_greenhouse_counting_accuracy_pct"], 94.4)
        self.assertEqual(smart_farm.extra_price_metrics["uav_weight_estimation_accuracy_pct"], 87.5)

    def test_education_policy_cases_are_routing_not_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND216_CASE_CANDIDATES}
        megastudy = by_id["r12_loop8_megastudy_medical_quota_policy_event"]
        edtech = by_id["r12_loop8_edtech_phone_ban_policy_watch"]

        self.assertEqual(megastudy.primary_archetype, E2RArchetype.EDUCATION_SPECIALTY_SERVICES)
        self.assertIn(E2RArchetype.EDUCATION_POLICY_EVENT, megastudy.secondary_archetypes)
        self.assertEqual(megastudy.stage2_date.isoformat(), "2025-03-07")
        self.assertEqual(megastudy.extra_price_metrics["original_quota"], 3058.0)
        self.assertEqual(megastudy.extra_price_metrics["quota_increase_2027_pct"], 16.0)
        self.assertEqual(megastudy.extra_price_metrics["quota_increase_2030_pct"], 26.6)
        self.assertIn("education_policy_expectation_only", megastudy.red_flag_fields)

        self.assertEqual(edtech.stage1_date.isoformat(), "2025-08-27")
        self.assertEqual(edtech.extra_price_metrics["law_effective_date"], "2026-03")
        self.assertEqual(edtech.extra_price_metrics["students_social_media_daily_life_impact_pct"], 37.0)
        self.assertEqual(edtech.extra_price_metrics["students_anxious_without_social_media_pct"], 22.0)
        self.assertIsNone(edtech.stage3_date)

    def test_poultry_and_kyochon_are_event_premium_not_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND216_CASE_CANDIDATES}
        poultry = by_id["r12_loop8_poultry_brazil_bird_flu_import_ban_event"]
        kyochon = by_id["r12_loop8_kyochon_chicken_celebrity_food_event"]

        self.assertEqual(poultry.case_type, "event_premium")
        self.assertEqual(poultry.stage4c_date.isoformat(), "2025-06-23")
        self.assertEqual(poultry.extra_price_metrics["event_duration_days"], 35.0)
        self.assertIn("disease_event_only", poultry.red_flag_fields)
        self.assertIn("import_ban_reversal", poultry.red_flag_fields)

        self.assertEqual(kyochon.primary_archetype, E2RArchetype.FOOD_SERVICE_EVENT_PREMIUM)
        self.assertEqual(kyochon.case_type, "overheat")
        self.assertEqual(kyochon.stage4b_date.isoformat(), "2025-10-31")
        self.assertEqual(kyochon.mfe_1d, 25.0)
        self.assertEqual(kyochon.score_price_alignment, "price_moved_without_evidence")
        self.assertIn("celebrity_food_event_only", kyochon.red_flag_fields)

    def test_green_gate_and_4c_rules_are_explicit(self) -> None:
        required = set(ROUND216_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND216_GREEN_FORBIDDEN_PATTERNS)
        green_markdown = render_round216_green_gate_review_markdown()
        review_markdown = render_round216_stage4b_4c_review_markdown()

        self.assertIn("recurring_revenue_or_repeat_purchase_confirmed", required)
        self.assertIn("unit_economics_positive", required)
        self.assertIn("cash_conversion_confirmed", required)
        self.assertIn("price_path_after_evidence", required)
        self.assertIn("celebrity_food_event_only", forbidden)
        self.assertIn("disease_event_only", forbidden)
        self.assertIn("smart_farm_theme_only", forbidden)
        self.assertIn("Do not apply these weights to production scoring yet.", green_markdown)
        self.assertIn("celebrity_or_viral_food_event_basket_rally", ROUND216_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("churn_spike", ROUND216_HARD_4C_GATES)
        self.assertIn("subsidy_withdrawal", ROUND216_HARD_4C_GATES)
        self.assertIn("r12_loop8_kyochon_chicken_celebrity_food_event", review_markdown)

    def test_shadow_weights_and_deep_sub_archetypes_capture_round216_terms(self) -> None:
        shadow_text = "\n".join(str(row) for row in round216_shadow_weight_rows())
        deep_text = "\n".join(str(row) for row in round216_deep_sub_archetype_rows())

        self.assertEqual(len(ROUND216_SHADOW_WEIGHT_ROWS), 8)
        self.assertGreaterEqual(len(ROUND216_SCORE_ADJUSTMENTS), 20)
        self.assertIn("FOOD_SERVICE_EVENT_PREMIUM", shadow_text)
        self.assertIn("HOME_LIVING_APPLIANCE_RENTAL", shadow_text)
        self.assertIn("Coway", deep_text)
        self.assertIn("Kyochon", deep_text)
        self.assertIn("Brazil bird flu", deep_text)

    def test_price_validation_fields_cover_reported_event_and_policy_anchors(self) -> None:
        fields = set(ROUND216_PRICE_VALIDATION_FIELDS)

        self.assertIn("reported_event_mfe_1d_range", fields)
        self.assertIn("reported_event_mfe_1d_midpoint", fields)
        self.assertIn("quota_original", fields)
        self.assertIn("quota_2027", fields)
        self.assertIn("quota_2030", fields)
        self.assertIn("uav_counting_accuracy", fields)
        self.assertIn("price_validation_status", fields)

    def test_summary_and_audit_payload_are_calibration_only(self) -> None:
        audit = round216_audit_payload()

        self.assertEqual(audit["source_round"], "docs/round/round_216.md")
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_use_round216_cases_as_candidate_generation_input", audit["what_not_to_change"])
        self.assertIn("do_not_apply_shadow_weights_to_production_scoring_yet", audit["what_not_to_change"])

    def test_cli_parser_and_writer_outputs(self) -> None:
        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round216_r12_loop8_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            self.assertEqual(len(records), len(ROUND216_CASE_CANDIDATES))
            self.assertIn("코웨이", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("recurring_revenue", paths["score_adjustments"].read_text(encoding="utf-8"))
            self.assertIn("FOOD_SERVICE_EVENT_PREMIUM", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("Kyochon", paths["deep_sub_archetypes"].read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
