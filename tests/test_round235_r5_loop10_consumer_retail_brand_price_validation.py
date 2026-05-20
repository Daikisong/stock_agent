from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round235_r5_loop10_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector
from e2r.sector.round235_r5_loop10_consumer_retail_brand_price_validation import (
    ROUND235_CASE_CANDIDATES,
    ROUND235_DEEP_SUB_ARCHETYPES,
    ROUND235_GREEN_FORBIDDEN_PATTERNS,
    ROUND235_GREEN_REQUIRED_FIELDS,
    ROUND235_HARD_4C_GATES,
    ROUND235_PRICE_VALIDATION_FIELDS,
    ROUND235_REQUIRED_TARGET_ALIASES,
    ROUND235_SHADOW_WEIGHT_ROWS,
    ROUND235_STAGE4B_WATCH_TRIGGERS,
    render_round235_green_gate_review_markdown,
    render_round235_stage4b_4c_review_markdown,
    round235_audit_payload,
    round235_case_records,
    round235_case_rows,
    round235_deep_sub_archetype_rows,
    round235_shadow_weight_rows,
    round235_summary,
    write_round235_r5_loop10_reports,
)


class Round235R5Loop10ConsumerRetailBrandPriceValidationTests(unittest.TestCase):
    def test_targets_are_existing_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND235_REQUIRED_TARGET_ALIASES), 13)
        self.assertTrue(set(ROUND235_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND235_REQUIRED_TARGET_ALIASES["K_FOOD_EXPORT_RECURRING"],
            E2RArchetype.EXPORT_RECURRING_CONSUMER.value,
        )
        self.assertEqual(
            ROUND235_REQUIRED_TARGET_ALIASES["K_BEAUTY_ODM_DISTRIBUTOR_LEVERAGE"],
            E2RArchetype.K_BEAUTY_EXPORT_DISTRIBUTION_KOREA.value,
        )
        self.assertEqual(
            ROUND235_REQUIRED_TARGET_ALIASES["CHANNEL_SELLTHROUGH_GATE"],
            E2RArchetype.K_BEAUTY_OFFLINE_SELL_THROUGH.value,
        )

    def test_case_records_validate_and_remain_calibration_only(self) -> None:
        records = round235_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, Round10LargeSector.CONSUMER_RETAIL_BRAND.value)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_ohlc_complete_false", record.green_guardrails)

        summary = round235_summary()
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["structural_success_count"], 2)
        self.assertEqual(summary["success_candidate_count"], 2)
        self.assertEqual(summary["overheat_count"], 1)
        self.assertEqual(summary["failed_rerating_count"], 1)
        self.assertEqual(summary["event_premium_count"], 2)
        self.assertEqual(summary["stage3_case_count"], 2)
        self.assertEqual(summary["stage4c_watch_count"], 2)
        self.assertEqual(summary["hard_4c_case_count"], 0)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_ohlc_complete"])

    def test_samyang_is_stage3_candidate_with_regulatory_watch(self) -> None:
        case = _case("r5_loop10_samyang_buldak_export_regulatory_watch")

        self.assertEqual(case.primary_archetype, E2RArchetype.EXPORT_RECURRING_CONSUMER)
        self.assertEqual(case.stage2_date.isoformat(), "2024-06-14")
        self.assertEqual(case.stage3_date.isoformat(), "2024-06-14")
        self.assertEqual(case.stage4c_date.isoformat(), "2024-06-12")
        self.assertFalse(case.hard_4c_confirmed)
        self.assertEqual(case.stage3_price_anchor, 647000.0)
        self.assertEqual(case.mfe_1d, 5.7)
        self.assertEqual(case.extra_price_metrics["target_upside_pct"], 28.3)
        self.assertEqual(case.extra_price_metrics["op_estimate_q2_krw_bn"], 81.2)
        self.assertEqual(case.round_alignment_label, "aligned_partial")
        self.assertIn("food_safety_regulatory_watch", case.red_flag_fields)

    def test_nongshim_and_olive_young_are_stage2_watch_until_sellthrough(self) -> None:
        nongshim = _case("r5_loop10_nongshim_shin_global_staple")
        olive = _case("r5_loop10_cj_olive_young_retail_platform")

        self.assertEqual(nongshim.primary_archetype, E2RArchetype.K_FOOD_GLOBAL_STAPLE_BRAND)
        self.assertEqual(nongshim.stage2_date.isoformat(), "2024-05-27")
        self.assertIsNone(nongshim.stage3_date)
        self.assertEqual(nongshim.extra_price_metrics["target_growth_from_2023_na_sales_pct"], 178.8)
        self.assertNotIn("toomba_first_3_month_sales_mn_units", nongshim.extra_price_metrics)
        self.assertIn("opm_eps_revision_unverified", nongshim.red_flag_fields)

        self.assertEqual(olive.primary_archetype, E2RArchetype.K_BEAUTY_RETAIL_PLATFORM)
        self.assertEqual(olive.case_type, "success_candidate")
        self.assertIsNone(olive.stage3_date)
        self.assertEqual(olive.extra_price_metrics["us_kbeauty_market_growth_pct"], 37.0)
        self.assertIn("private_affiliate_value_without_listed_earnings_bridge", olive.red_flag_fields)

    def test_apr_is_structural_success_with_4b_watch(self) -> None:
        case = _case("r5_loop10_apr_medicube_structural_4b")

        self.assertEqual(case.primary_archetype, E2RArchetype.BEAUTY_DEVICE_EXPORT)
        self.assertEqual(case.stage3_date.isoformat(), "2025-10-01")
        self.assertEqual(case.stage4b_date.isoformat(), "2025-10-01")
        self.assertEqual(case.stage4b_status, "watch")
        self.assertEqual(case.extra_price_metrics["reported_mfe_since_january_pct"], 300.0)
        self.assertEqual(case.extra_price_metrics["medicube_revenue_share_pct"], 91.7)
        self.assertEqual(case.extra_price_metrics["tiktok_shop_revenue_usd_mn"], 102.9)
        self.assertEqual(case.extra_price_metrics["market_value_context_usd_bn"], 6.0)

    def test_kbeauty_tourism_and_fnf_are_event_or_overheat_not_green(self) -> None:
        dalba = _case("r5_loop10_indie_kbeauty_odm_distribution_watch")
        tourism = _case("r5_loop10_tourism_retail_china_visa_event")
        fnf = _case("r5_loop10_fnf_taylormade_mna_optionality")

        self.assertEqual(dalba.case_type, "overheat")
        self.assertEqual(dalba.rerating_result, "theme_overheat")
        self.assertEqual(dalba.stage4b_date.isoformat(), "2025-06-05")
        self.assertEqual(dalba.extra_price_metrics["relative_growth_vs_us_market_multiple"], 3.38)
        self.assertIn(E2RArchetype.K_BEAUTY_OEM_ODM_SUPPLYCHAIN_KOREA, dalba.secondary_archetypes)
        self.assertIn("retail_talks_without_sell_through", dalba.red_flag_fields)

        self.assertEqual(tourism.primary_archetype, E2RArchetype.TOURISM_POLICY_EVENT)
        self.assertEqual(tourism.case_type, "event_premium")
        self.assertEqual(tourism.stage4b_date.isoformat(), "2025-08-06")
        self.assertEqual(tourism.extra_price_metrics["hankook_cosmetics_event_mfe_1d_pct"], 9.9)
        self.assertEqual(tourism.extra_price_metrics["target_growth_vs_2024_pct"], 12.8)
        self.assertEqual(tourism.round_alignment_label, "event_premium_success_candidate")

        self.assertEqual(fnf.rerating_result, "event_premium")
        self.assertEqual(fnf.stage1_date.isoformat(), "2025-07-21")
        self.assertEqual(fnf.extra_price_metrics["ff_investment_vs_possible_value_pct"], 7.4)
        self.assertIn("mna_optionality_without_eps", fnf.red_flag_fields)

    def test_amorepacific_is_legacy_china_exposure_watch_without_price_invention(self) -> None:
        case = _case("r5_loop10_amorepacific_legacy_china_exposure")

        self.assertEqual(case.primary_archetype, E2RArchetype.CHINA_CONSUMER_EXPOSURE_4C)
        self.assertEqual(case.case_type, "failed_rerating")
        self.assertEqual(case.stage4c_date.isoformat(), "2024-10-22")
        self.assertIsNone(case.mae_1d)
        self.assertEqual(case.rerating_result, "thesis_break")
        self.assertEqual(case.stage_failure_type, "should_have_been_red")
        self.assertEqual(case.round_alignment_label, "thesis_break_watch_insufficient_price_data")
        self.assertEqual(case.extra_price_metrics["loreal_north_asia_sales_pct"], -6.5)
        self.assertIn("china_demand_weakness", case.red_flag_fields)

    def test_green_gate_deep_tags_and_stage4_rules_are_explicit(self) -> None:
        required = set(ROUND235_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND235_GREEN_FORBIDDEN_PATTERNS)
        deep_rows = round235_deep_sub_archetype_rows()
        deep_text = "\n".join(row["deep_sub_archetype"] for row in deep_rows)
        green_markdown = render_round235_green_gate_review_markdown()
        stage_review = render_round235_stage4b_4c_review_markdown()

        self.assertIn("repeat_purchase_or_repeat_demand", required)
        self.assertIn("channel_sell_through_confirmed", required)
        self.assertIn("single_sku_or_single_device_risk_managed", required)
        self.assertIn("viral_tiktok_only", forbidden)
        self.assertIn("ipo_or_debut_rally_only", forbidden)
        self.assertIn("tourism_policy_without_spend_or_opm", forbidden)
        self.assertIn("food_safety_recall_expands", ROUND235_HARD_4C_GATES)
        self.assertIn("mna_optionality_prices_before_signed_transaction", ROUND235_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("Do not apply these weights to production scoring yet.", green_markdown)
        self.assertIn("r5_loop10_tourism_retail_china_visa_event", stage_review)
        self.assertIn("Samyang_Buldak_export", deep_text)
        self.assertIn("Olive_Young_US_store", deep_text)
        self.assertGreaterEqual(len(ROUND235_DEEP_SUB_ARCHETYPES), 20)

    def test_shadow_weights_cover_r5_loop10_targets(self) -> None:
        shadow_text = "\n".join(str(row) for row in round235_shadow_weight_rows())

        self.assertEqual(len(ROUND235_SHADOW_WEIGHT_ROWS), 9)
        self.assertIn("EXPORT_RECURRING_CONSUMER", shadow_text)
        self.assertIn("K_FOOD_GLOBAL_STAPLE_BRAND", shadow_text)
        self.assertIn("BEAUTY_DEVICE_EXPORT", shadow_text)
        self.assertIn("K_BEAUTY_BRAND_US_CHANNEL", shadow_text)
        self.assertIn("K_BEAUTY_EXPORT_DISTRIBUTION_KOREA", shadow_text)
        self.assertIn("K_BEAUTY_RETAIL_PLATFORM", shadow_text)
        self.assertIn("CHINA_CONSUMER_EXPOSURE_4C", shadow_text)
        self.assertIn("TOURISM_POLICY_EVENT", shadow_text)
        self.assertIn("APPAREL_FAST_FASHION_BRAND_OEM", shadow_text)

    def test_price_validation_fields_include_round235_anchor_fields(self) -> None:
        fields = set(ROUND235_PRICE_VALIDATION_FIELDS)

        self.assertIn("target_upside_pct", fields)
        self.assertIn("reported_mfe_since_debut_pct", fields)
        self.assertIn("reported_mfe_since_january_pct", fields)
        self.assertIn("relative_growth_vs_us_market_multiple", fields)
        self.assertIn("visitor_target_growth_pct", fields)
        self.assertIn("ff_investment_vs_possible_value_pct", fields)
        self.assertIn("overseas_sales_mix", fields)
        self.assertIn("opm_estimate", fields)

    def test_summary_and_audit_payload_are_calibration_only(self) -> None:
        audit = round235_audit_payload()

        self.assertEqual(audit["source_round"], "docs/round/round_235.md")
        self.assertEqual(audit["large_sector"], Round10LargeSector.CONSUMER_RETAIL_BRAND.value)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_use_round235_cases_as_candidate_generation_input", audit["what_not_to_change"])
        self.assertIn("do_not_lower_stage3_green_thresholds", audit["what_not_to_change"])

    def test_cli_parser_and_writer_outputs(self) -> None:
        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round235_r5_loop10_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round235_case_rows()
            self.assertEqual(len(records), len(ROUND235_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND235_CASE_CANDIDATES))
            self.assertIn("삼양식품", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("channel_sell_through", paths["score_adjustments"].read_text(encoding="utf-8"))
            self.assertIn("K_BEAUTY_EXPORT_DISTRIBUTION_KOREA", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("ff_investment_vs_possible_value_pct", paths["price_validation_fields"].read_text(encoding="utf-8"))
            self.assertIn("Olive_Young_US_store", paths["deep_sub_archetype_review"].read_text(encoding="utf-8"))


def _case(case_id: str):
    return next(case for case in ROUND235_CASE_CANDIDATES if case.case_id == case_id)


if __name__ == "__main__":
    unittest.main()
