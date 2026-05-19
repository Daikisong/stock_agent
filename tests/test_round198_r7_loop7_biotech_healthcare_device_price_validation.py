import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round198_r7_loop7_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round198_r7_loop7_biotech_healthcare_device_price_validation import (
    ROUND198_CASE_CANDIDATES,
    ROUND198_GREEN_FORBIDDEN_PATTERNS,
    ROUND198_GREEN_REQUIRED_FIELDS,
    ROUND198_HARD_4C_GATES,
    ROUND198_PRICE_BACKFILL_FIELDS,
    ROUND198_REQUIRED_TARGET_ALIASES,
    render_round198_green_gate_review_markdown,
    render_round198_stage4b_4c_review_markdown,
    round198_audit_payload,
    round198_case_records,
    round198_case_rows,
    round198_price_backfill_field_rows,
    round198_score_adjustment_rows,
    round198_summary,
    write_round198_r7_loop7_reports,
)


class Round198R7Loop7BiotechHealthcareDevicePriceValidationTests(unittest.TestCase):
    def test_round198_targets_are_existing_canonical_archetypes(self):
        self.assertGreaterEqual(len(ROUND198_REQUIRED_TARGET_ALIASES), 18)
        self.assertEqual(
            ROUND198_REQUIRED_TARGET_ALIASES["BIOTECH_ROYALTY_COMMERCIALIZATION"],
            E2RArchetype.BIOTECH_ROYALTY_COMMERCIALIZATION.value,
        )
        self.assertEqual(
            ROUND198_REQUIRED_TARGET_ALIASES["BOTULINUM_US_MARKET_ENTRY"],
            E2RArchetype.BOTULINUM_US_MARKET_ENTRY.value,
        )
        self.assertEqual(
            ROUND198_REQUIRED_TARGET_ALIASES["MANUFACTURING_INSPECTION_CRL_OVERLAY"],
            E2RArchetype.MANUFACTURING_INSPECTION_CRL_OVERLAY.value,
        )
        for canonical in ROUND198_REQUIRED_TARGET_ALIASES.values():
            self.assertIsInstance(E2RArchetype(canonical), E2RArchetype)

    def test_case_records_validate_and_remain_shadow_only(self):
        records = {record.case_id: record for record in round198_case_records()}

        self.assertEqual(len(records), 7)
        self.assertEqual(
            records["yuhan_lazertinib_fda_approval_royalty_commercialization_watch"].case_type,
            "success_candidate",
        )
        self.assertEqual(records["hugel_letybo_us_launch_botulinum_commercialization_watch"].case_type, "success_candidate")
        self.assertEqual(records["samsung_biologics_us_gsk_facility_cdmo_4b_benchmark"].case_type, "4b_watch")
        self.assertEqual(records["r7_hard_4c_reliable_source_gap_watch"].case_type, "failed_rerating")
        for record in records.values():
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("hard_4c_confirmed_false_in_this_pass", record.green_guardrails)
            self.assertEqual(record.price_validation.price_validation_status, "needs_ohlc_backfill")

    def test_yuhan_is_stage2_approval_watch_not_green_or_hard_4c(self):
        rows = {row["case_id"]: row for row in round198_case_rows()}
        yuhan = rows["yuhan_lazertinib_fda_approval_royalty_commercialization_watch"]

        self.assertEqual(yuhan["stage2_date"], "2024-08-20")
        self.assertEqual(yuhan["stage3_date"], "")
        self.assertEqual(yuhan["hard_4c_confirmed"], "false")
        self.assertIn("royalty_recognition_unverified", yuhan["red_flag_fields"])
        self.assertIn("manufacturing_inspection_crl_watch_not_hard_4c", yuhan["red_flag_fields"])

    def test_launch_facility_and_mna_cases_are_stage2_not_forced_green(self):
        rows = {row["case_id"]: row for row in round198_case_rows()}
        hugel = rows["hugel_letybo_us_launch_botulinum_commercialization_watch"]
        celltrion = rows["celltrion_us_facility_biosimilar_tariff_hedge_stage2_watch"]
        sk_bioscience = rows["sk_bioscience_idt_biologika_cmo_transition_event_watch"]

        self.assertEqual(hugel["stage2_date"], "2025-03-01")
        self.assertEqual(hugel["stage3_date"], "")
        self.assertIn("us_sales_absent", hugel["red_flag_fields"])
        self.assertEqual(celltrion["stage2_date"], "2025-09-23")
        self.assertEqual(celltrion["stage3_date"], "")
        self.assertIn("utilization_unverified", celltrion["red_flag_fields"])
        self.assertEqual(sk_bioscience["stage2_date"], "2024-06-27")
        self.assertEqual(sk_bioscience["score_price_alignment"], "price_moved_without_evidence")
        self.assertEqual(sk_bioscience["rerating_result"], "event_premium")

    def test_samsung_bio_lunit_and_source_gap_are_not_new_green(self):
        rows = {row["case_id"]: row for row in round198_case_rows()}
        samsung = rows["samsung_biologics_us_gsk_facility_cdmo_4b_benchmark"]
        lunit = rows["lunit_external_validation_medical_ai_commercialization_gap_watch"]
        source_gap = rows["r7_hard_4c_reliable_source_gap_watch"]

        self.assertEqual(samsung["case_type"], "4b_watch")
        self.assertEqual(samsung["stage2_date"], "2025-12-22")
        self.assertEqual(samsung["stage3_date"], "")
        self.assertEqual(samsung["rerating_result"], "true_rerating")
        self.assertEqual(lunit["stage2_date"], "2025-03-17")
        self.assertEqual(lunit["stage3_date"], "")
        self.assertIn("subgroup_performance_risk", lunit["red_flag_fields"])
        self.assertEqual(source_gap["hard_4c_confirmed"], "false")
        self.assertIn("reliable_source_gap", source_gap["red_flag_fields"])

    def test_green_gate_requires_commercialization_and_blocks_headline_only(self):
        required = set(ROUND198_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND198_GREEN_FORBIDDEN_PATTERNS)
        adjustments = {row["axis"]: row for row in round198_score_adjustment_rows()}
        markdown = render_round198_green_gate_review_markdown()

        self.assertIn("prescription_volume_or_hospital_adoption", required)
        self.assertIn("reimbursement_or_payer_access", required)
        self.assertIn("revenue_recognition", required)
        self.assertIn("royalty_or_gross_margin_confirmed", required)
        self.assertIn("approval_news_only", forbidden)
        self.assertIn("paper_validation_without_revenue", forbidden)
        self.assertIn("mna_announcement_only", forbidden)
        self.assertEqual(adjustments["commercial_revenue"]["points"], "5")
        self.assertEqual(adjustments["approval_news_only"]["points"], "-5")
        self.assertIn("Do not apply these weights to production scoring yet", markdown)

    def test_price_backfill_fields_include_r7_commercial_quality_inputs(self):
        fields = {row["field"] for row in round198_price_backfill_field_rows()}

        self.assertGreaterEqual(len(ROUND198_PRICE_BACKFILL_FIELDS), 50)
        for field in (
            "prescription_volume",
            "reimbursement_status",
            "commercial_revenue",
            "royalty_recognition",
            "capacity_utilization",
            "cash_runway_months",
            "dilution_or_cb_flag",
            "manufacturing_inspection_issue_flag",
            "efficacy_safety_crl_flag",
            "hard_4c_confirmed",
        ):
            self.assertIn(field, fields)

    def test_stage4b_4c_review_separates_crl_types_and_source_gap(self):
        review = render_round198_stage4b_4c_review_markdown()

        self.assertIn("efficacy_or_safety_crl", ROUND198_HARD_4C_GATES)
        self.assertIn("manufacturing_inspection_failure", ROUND198_HARD_4C_GATES)
        self.assertIn("efficacy/safety CRL can be hard 4C", review)
        self.assertIn("manufacturing-inspection CRL is commercialization delay watch", review)
        self.assertIn("r7_hard_4c_reliable_source_gap_watch", review)

    def test_summary_and_audit_payload_are_calibration_only(self):
        summary = round198_summary()
        payload = round198_audit_payload()

        self.assertEqual(summary["case_candidate_count"], len(ROUND198_CASE_CANDIDATES))
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["hard_4c_case_count"], 0)
        self.assertEqual(summary["source_gap_case_count"], 1)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertTrue(summary["shadow_weight_only"])
        self.assertIn("do_not_use_round198_cases_as_candidate_generation_input", payload["what_not_to_change"])
        self.assertIn("do_not_confirm_hard_4c_without_reliable_primary_or_major_source", payload["what_not_to_change"])

    def test_cli_parser_and_writer_outputs(self):
        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])

        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            paths = write_round198_r7_loop7_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)
            records = load_case_library(root / "cases.jsonl")
            self.assertEqual(len(records), 7)
            self.assertIn("Stage 3-Green", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("prescription_volume", paths["score_adjustments"].read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
