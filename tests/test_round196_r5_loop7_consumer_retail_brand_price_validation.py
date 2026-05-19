import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round196_r5_loop7_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round196_r5_loop7_consumer_retail_brand_price_validation import (
    ROUND196_CASE_CANDIDATES,
    ROUND196_GREEN_FORBIDDEN_PATTERNS,
    ROUND196_GREEN_REQUIRED_FIELDS,
    ROUND196_HARD_4C_GATES,
    ROUND196_PRICE_BACKFILL_FIELDS,
    ROUND196_REQUIRED_TARGET_ALIASES,
    render_round196_green_gate_review_markdown,
    render_round196_stage4b_4c_review_markdown,
    round196_audit_payload,
    round196_case_records,
    round196_case_rows,
    round196_price_backfill_field_rows,
    round196_score_adjustment_rows,
    round196_summary,
    write_round196_r5_loop7_reports,
)


class Round196R5Loop7ConsumerRetailBrandPriceValidationTests(unittest.TestCase):
    def test_round196_targets_are_existing_canonical_archetypes(self):
        self.assertGreaterEqual(len(ROUND196_REQUIRED_TARGET_ALIASES), 15)
        self.assertEqual(
            ROUND196_REQUIRED_TARGET_ALIASES["K_FOOD_GLOBAL_STAPLE_BRAND"],
            E2RArchetype.K_FOOD_GLOBAL_STAPLE_BRAND.value,
        )
        self.assertEqual(
            ROUND196_REQUIRED_TARGET_ALIASES["EVENT_PREMIUM_GOVERNANCE_OVERLAY"],
            E2RArchetype.EVENT_PREMIUM_GOVERNANCE_OVERLAY.value,
        )
        self.assertEqual(
            ROUND196_REQUIRED_TARGET_ALIASES["DISCLOSURE_CONFIDENCE_CAP"],
            E2RArchetype.DISCLOSURE_CONFIDENCE_CAP.value,
        )
        for canonical in ROUND196_REQUIRED_TARGET_ALIASES.values():
            self.assertIsInstance(E2RArchetype(canonical), E2RArchetype)

    def test_case_records_validate_and_remain_shadow_only(self):
        records = {record.case_id: record for record in round196_case_records()}

        self.assertEqual(len(records), 7)
        self.assertEqual(records["nongshim_shin_ramyun_global_staple_stage2_watch"].case_type, "success_candidate")
        self.assertEqual(records["apr_medicube_beauty_device_structural_success_4b_watch"].case_type, "structural_success")
        self.assertEqual(records["dalba_global_us_retail_talks_ipo_overheat_watch"].case_type, "overheat")
        self.assertEqual(records["fnf_taylormade_mna_event_premium_not_brand_rerating"].case_type, "event_premium")
        for record in records.values():
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertEqual(record.price_validation.price_validation_status, "needs_ohlc_backfill")

    def test_kfood_and_apr_are_stage2_or_4b_watch_not_forced_green(self):
        rows = {row["case_id"]: row for row in round196_case_rows()}
        nongshim = rows["nongshim_shin_ramyun_global_staple_stage2_watch"]
        apr = rows["apr_medicube_beauty_device_structural_success_4b_watch"]

        self.assertEqual(nongshim["stage2_date"], "2024-05-27")
        self.assertEqual(nongshim["stage3_date"], "")
        self.assertIn("opm_eps_revision", nongshim["red_flag_fields"])
        self.assertEqual(apr["rerating_result"], "true_rerating")
        self.assertEqual(apr["stage4b_date"], "2025-10-20")
        self.assertEqual(apr["stage4b_status"], "watch")
        self.assertIn("possible_after_q2_2025", apr["stage3_decision"])

    def test_ipo_retail_talks_and_mna_are_not_green_evidence(self):
        rows = {row["case_id"]: row for row in round196_case_rows()}
        dalba = rows["dalba_global_us_retail_talks_ipo_overheat_watch"]
        fnf = rows["fnf_taylormade_mna_event_premium_not_brand_rerating"]

        self.assertEqual(dalba["stage2_date"], "2025-06-05")
        self.assertEqual(dalba["stage3_date"], "")
        self.assertEqual(dalba["score_price_alignment"], "price_moved_without_evidence")
        self.assertEqual(dalba["rerating_result"], "theme_overheat")
        self.assertIn("retail_talks_without_sellthrough", dalba["red_flag_fields"])
        self.assertEqual(fnf["stage1_date"], "2025-07-21")
        self.assertEqual(fnf["stage3_date"], "")
        self.assertEqual(fnf["rerating_result"], "event_premium")
        self.assertIn("mna_event_premium", fnf["red_flag_fields"])

    def test_odm_legacy_brand_and_holdco_caps_are_separated(self):
        rows = {row["case_id"]: row for row in round196_case_rows()}
        odm = rows["cosmax_kolmar_fast_beauty_odm_supply_chain_stage2_watch"]
        amore = rows["amorepacific_legacy_kbeauty_china_to_us_transition_watch"]
        cj = rows["cj_olive_young_private_platform_holdco_cap_stage2_watch"]

        self.assertEqual(odm["stage2_date"], "2025-06-05")
        self.assertIn("customer_diversification", odm["stage3_decision"])
        self.assertEqual(amore["rerating_result"], "no_rerating")
        self.assertIn("china_exports_decline", amore["red_flag_fields"])
        self.assertIn("holdco_discount", cj["red_flag_fields"])
        self.assertEqual(cj["stage4b_status"], "watch")

    def test_green_gate_requires_repeat_sellthrough_opm_and_blocks_event_buzz(self):
        required = set(ROUND196_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND196_GREEN_FORBIDDEN_PATTERNS)
        adjustments = {row["axis"]: row for row in round196_score_adjustment_rows()}
        markdown = render_round196_green_gate_review_markdown()

        self.assertIn("repeat_purchase_evidence", required)
        self.assertIn("channel_sell_through_confirmed", required)
        self.assertIn("inventory_and_receivables_stable", required)
        self.assertIn("tiktok_viral_only", forbidden)
        self.assertIn("ipo_first_month_rally", forbidden)
        self.assertIn("mna_event_only", forbidden)
        self.assertEqual(adjustments["repeat_demand"]["points"], "4")
        self.assertEqual(adjustments["viral_product_only"]["points"], "-5")
        self.assertIn("Do not apply these weights to production scoring yet", markdown)

    def test_price_backfill_fields_include_r5_quality_inputs(self):
        fields = {row["field"] for row in round196_price_backfill_field_rows()}

        self.assertGreaterEqual(len(ROUND196_PRICE_BACKFILL_FIELDS), 45)
        for field in (
            "repeat_purchase_evidence",
            "channel_sell_through",
            "repeat_order",
            "opm_improvement",
            "inventory_days",
            "receivables_days",
            "retail_talks_without_sell_through_flag",
            "ipo_first_month_rally_flag",
            "mna_event_premium_flag",
            "hard_4c_confirmed",
        ):
            self.assertIn(field, fields)

    def test_stage4b_4c_review_contains_consumer_hard_gates(self):
        review = render_round196_stage4b_4c_review_markdown()

        self.assertIn("recall_or_food_safety_issue", ROUND196_HARD_4C_GATES)
        self.assertIn("channel_stuffing", ROUND196_HARD_4C_GATES)
        self.assertIn("mna_event_failure", ROUND196_HARD_4C_GATES)
        self.assertIn("dalba_global_us_retail_talks_ipo_overheat_watch", review)
        self.assertIn("fnf_taylormade_mna_event_premium_not_brand_rerating", review)

    def test_summary_and_audit_payload_are_calibration_only(self):
        summary = round196_summary()
        payload = round196_audit_payload()

        self.assertEqual(summary["case_candidate_count"], len(ROUND196_CASE_CANDIDATES))
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["stage3_possible_candidate_count"], 1)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertTrue(summary["shadow_weight_only"])
        self.assertIn("do_not_use_round196_cases_as_candidate_generation_input", payload["what_not_to_change"])

    def test_cli_parser_and_writer_outputs(self):
        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])

        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            paths = write_round196_r5_loop7_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)
            records = load_case_library(root / "cases.jsonl")
            self.assertEqual(len(records), 7)
            self.assertIn("Stage 3-Green", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("channel_sell_through", paths["score_adjustments"].read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
