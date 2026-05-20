from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round276_r7_loop13_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round276_r7_loop13_biotech_healthcare_device_price_validation import (
    ROUND276_CASE_CANDIDATES,
    ROUND276_GREEN_FORBIDDEN_PATTERNS,
    ROUND276_GREEN_REQUIRED_FIELDS,
    ROUND276_HARD_4C_GATES,
    ROUND276_LARGE_SECTOR,
    ROUND276_PRICE_VALIDATION_FIELDS,
    ROUND276_REQUIRED_TARGET_ALIASES,
    ROUND276_SHADOW_WEIGHT_ROWS,
    ROUND276_STAGE4B_WATCH_TRIGGERS,
    render_round276_green_gate_review_markdown,
    render_round276_stage4b_4c_review_markdown,
    round276_audit_payload,
    round276_case_records,
    round276_case_rows,
    round276_deep_sub_archetype_rows,
    round276_shadow_weight_rows,
    round276_summary,
    write_round276_r7_loop13_reports,
)


class Round276R7Loop13BiotechHealthcareDevicePriceValidationTests(unittest.TestCase):
    def test_round276_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND276_REQUIRED_TARGET_ALIASES), 8)
        self.assertTrue(set(ROUND276_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND276_REQUIRED_TARGET_ALIASES["KOREAN_ORIGIN_DRUG_GLOBAL_APPROVAL"],
            E2RArchetype.KOREAN_ORIGIN_DRUG_GLOBAL_APPROVAL.value,
        )
        self.assertEqual(
            ROUND276_REQUIRED_TARGET_ALIASES["PLATFORM_TECH_ENZYME_ROYALTY_OPTIONALITY"],
            E2RArchetype.PLATFORM_TECH_ENZYME_ROYALTY_OPTIONALITY.value,
        )
        self.assertEqual(
            ROUND276_REQUIRED_TARGET_ALIASES["VACCINE_DEMAND_COLLAPSE_HARD_REFERENCE"],
            E2RArchetype.VACCINE_DEMAND_COLLAPSE_HARD_REFERENCE.value,
        )

    def test_round276_archetype_definitions_capture_r7_loop13_gates(self) -> None:
        yuhan = archetype_definition(E2RArchetype.KOREAN_ORIGIN_DRUG_GLOBAL_APPROVAL)
        alteogen = archetype_definition(E2RArchetype.PLATFORM_TECH_ENZYME_ROYALTY_OPTIONALITY)
        cdmo = archetype_definition(E2RArchetype.CDMO_US_TARIFF_HEDGE_STAGE2)
        factory = archetype_definition(E2RArchetype.BIOPHARMA_US_FACTORY_TARIFF_HEDGE)
        vaccine_mna = archetype_definition(E2RArchetype.VACCINE_CDMO_M_AND_A_STAGE2)
        aesthetic = archetype_definition(E2RArchetype.AESTHETIC_MEDICAL_DEVICE_PE_TAKEOUT)
        policy = archetype_definition(E2RArchetype.BIOPHARMA_POLICY_RALLY_EVENT_PREMIUM)
        demand = archetype_definition(E2RArchetype.VACCINE_DEMAND_COLLAPSE_HARD_REFERENCE)

        self.assertIn("FDA approval alone treated as Stage 3-Green", yuhan.false_positive_patterns)
        self.assertIn("royalty cashflow", alteogen.stage3_high_conviction_signals)
        self.assertIn("capacity utilization", cdmo.stage3_high_conviction_signals)
        self.assertIn("factory acquisition treated as product transfer", factory.false_positive_patterns)
        self.assertIn("M&A without utilization", vaccine_mna.false_positive_patterns)
        self.assertIn("take-private benchmark used as tradable Stage 3", aesthetic.false_positive_patterns)
        self.assertIn("policy tariff support only", policy.false_positive_patterns)
        self.assertIn("vaccine demand collapse", demand.stage4c_thesis_break_signals)

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round276_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND276_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_use_round276_cases_as_candidate_generation_input", record.green_guardrails)

        summary = round276_summary()
        self.assertEqual(summary["round_id"], "round_204")
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["success_candidate_count"], 6)
        self.assertEqual(summary["event_premium_count"], 3)
        self.assertEqual(summary["failed_rerating_count"], 1)
        self.assertEqual(summary["hard_4c_case_count"], 0)
        self.assertEqual(summary["hard_4c_reference_count"], 1)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 6)
        self.assertEqual(summary["stage4c_watch_count"], 6)
        self.assertEqual(summary["price_moved_without_evidence_count"], 2)
        self.assertEqual(summary["target_archetype_count"], 8)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])
        self.assertFalse(summary["hard_4c_confirmed"])
        self.assertTrue(summary["hard_4c_reference_confirmed"])

    def test_yuhan_alteogen_samsung_and_celltrion_are_guarded(self) -> None:
        by_id = {case.case_id: case for case in ROUND276_CASE_CANDIDATES}
        yuhan = by_id["r7_loop13_yuhan_lazertinib_global_fda_approval"]
        alteogen = by_id["r7_loop13_alteogen_merck_sc_keytruda_platform"]
        samsung = by_id["r7_loop13_samsung_biologics_gsk_rockville_facility"]
        celltrion = by_id["r7_loop13_celltrion_us_factory_tariff_hedge"]

        self.assertEqual(yuhan.primary_archetype, E2RArchetype.KOREAN_ORIGIN_DRUG_GLOBAL_APPROVAL)
        self.assertEqual(yuhan.extra_price_metrics["jnj_expected_rybrevant_peak_sales_usd_bn"], 5.0)
        self.assertEqual(yuhan.extra_price_metrics["trial_patient_count_marketwatch"], 1074)
        self.assertEqual(yuhan.extra_price_metrics["crl_cause"], "pre-approval manufacturing facility inspection observations")
        self.assertIn("FDA_approval_without_sales_bridge", yuhan.red_flag_fields)

        self.assertEqual(alteogen.primary_archetype, E2RArchetype.PLATFORM_TECH_ENZYME_ROYALTY_OPTIONALITY)
        self.assertEqual(alteogen.extra_price_metrics["keytruda_2024_sales_usd_bn"], 30.0)
        self.assertEqual(alteogen.extra_price_metrics["sc_keytruda_expected_adoption_pct"], "30-40")
        self.assertEqual(alteogen.event_mfe_pct, 1.8)
        self.assertIn("patent_or_CRL_overhang", alteogen.red_flag_fields)

        self.assertEqual(samsung.primary_archetype, E2RArchetype.CDMO_US_TARIFF_HEDGE_STAGE2)
        self.assertEqual(samsung.event_mae_pct, -0.4)
        self.assertEqual(samsung.extra_price_metrics["relative_underperformance_pp"], -2.4)
        self.assertFalse(samsung.extra_price_metrics["facility_utilization_confirmed"])
        self.assertEqual(samsung.score_price_alignment, "evidence_good_but_price_failed")

        self.assertEqual(celltrion.primary_archetype, E2RArchetype.BIOPHARMA_US_FACTORY_TARIFF_HEDGE)
        self.assertEqual(celltrion.extra_price_metrics["imclone_acquisition_usd_mn"], 330.0)
        self.assertEqual(celltrion.extra_price_metrics["us_factory_expansion_max_krw_bn"], 700.0)
        self.assertFalse(celltrion.extra_price_metrics["utilization_confirmed"])

    def test_sk_bioscience_jeisys_policy_and_skycovione_cases_are_separated(self) -> None:
        by_id = {case.case_id: case for case in ROUND276_CASE_CANDIDATES}
        sk_idt = by_id["r7_loop13_sk_bioscience_idt_biologika_cdmomna"]
        jeisys = by_id["r7_loop13_jeisys_medical_archimed_aesthetic_device_takeout"]
        policy = by_id["r7_loop13_biopharma_tariff_support_policy_rally"]
        skycovione = by_id["r7_loop13_sk_bioscience_skycovione_demand_collapse_reference"]

        self.assertEqual(sk_idt.primary_archetype, E2RArchetype.VACCINE_CDMO_M_AND_A_STAGE2)
        self.assertEqual(sk_idt.event_mfe_pct, 11.7)
        self.assertEqual(sk_idt.extra_price_metrics["idt_stake_acquired_pct"], 60.0)
        self.assertEqual(sk_idt.score_price_alignment, "price_moved_without_evidence")

        self.assertEqual(jeisys.primary_archetype, E2RArchetype.AESTHETIC_MEDICAL_DEVICE_PE_TAKEOUT)
        self.assertEqual(jeisys.stage2_price_anchor, 12860.0)
        self.assertEqual(jeisys.extra_price_metrics["take_private_value_usd_mn"], 742.0)
        self.assertEqual(jeisys.extra_price_metrics["revenue_cagr_3y_pct"], 44.0)
        self.assertEqual(jeisys.score_price_alignment, "aligned")
        self.assertEqual(jeisys.rerating_result, "event_premium")

        self.assertEqual(policy.primary_archetype, E2RArchetype.BIOPHARMA_POLICY_RALLY_EVENT_PREMIUM)
        self.assertEqual(policy.event_mfe_pct, 3.97)
        self.assertEqual(policy.extra_price_metrics["samsung_biologics_mfe_pct"], 6.23)
        self.assertEqual(policy.extra_price_metrics["implied_us_pharma_exports_2024_usd_bn"], 1.53)
        self.assertEqual(policy.case_type, "event_premium")

        self.assertEqual(skycovione.primary_archetype, E2RArchetype.VACCINE_DEMAND_COLLAPSE_HARD_REFERENCE)
        self.assertEqual(skycovione.case_type, "failed_rerating")
        self.assertFalse(skycovione.hard_4c_confirmed)
        self.assertTrue(skycovione.hard_4c_reference_confirmed)
        self.assertEqual(skycovione.extra_price_metrics["administered_shots"], 3787)
        self.assertEqual(skycovione.extra_price_metrics["administered_share_of_purchased_pct"], 0.038)
        self.assertEqual(skycovione.rerating_result, "no_rerating")

    def test_green_gate_4b_4c_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND276_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND276_GREEN_FORBIDDEN_PATTERNS)
        fields = set(ROUND276_PRICE_VALIDATION_FIELDS)
        shadow_rows = {row["archetype"]: row for row in round276_shadow_weight_rows()}
        deep_rows = round276_deep_sub_archetype_rows()
        green_markdown = render_round276_green_gate_review_markdown()
        stage_markdown = render_round276_stage4b_4c_review_markdown()

        self.assertIn("actual_prescription_ramp_confirmed", required)
        self.assertIn("cdmo_capacity_utilization_confirmed", required)
        self.assertIn("FDA_approval_without_sales_bridge", forbidden)
        self.assertIn("vaccine_procurement_without_demand", forbidden)
        self.assertIn("M&A_announcement_plus_10pct_before_order_book", ROUND276_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("vaccine_demand_collapse", ROUND276_HARD_4C_GATES)
        self.assertIn("demand_or_administered_dose_anchor", fields)
        self.assertIn("Do not apply these weights to production scoring yet.", green_markdown)
        self.assertIn("SkyCovione", stage_markdown)
        self.assertIn("hard reference", stage_markdown)
        self.assertEqual(len(ROUND276_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["BIOPHARMA_POLICY_RALLY_EVENT_PREMIUM"]["event_penalty"], "-5")
        self.assertEqual(shadow_rows["VACCINE_DEMAND_COLLAPSE_HARD_REFERENCE"]["hard_4c_sensitivity"], "+5")
        self.assertTrue(any("Yuhan" in row["terms"] for row in deep_rows))
        self.assertTrue(any("SkyCovione" in row["terms"] for row in deep_rows))

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round276_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_276.md")
        self.assertEqual(audit["round_id"], "round_204")
        self.assertEqual(audit["large_sector"], ROUND276_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertFalse(audit["summary"]["hard_4c_confirmed"])
        self.assertTrue(audit["summary"]["hard_4c_reference_confirmed"])
        self.assertIn("do_not_use_round276_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round276_r7_loop13_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round276_case_rows()
            self.assertEqual(len(records), len(ROUND276_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND276_CASE_CANDIDATES))
            self.assertIn("Yuhan", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("royalty_milestone_cashflow_confirmed", paths["green_gate_review"].read_text(encoding="utf-8"))
            self.assertIn("VACCINE_DEMAND_COLLAPSE_HARD_REFERENCE", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("demand_or_administered_dose_anchor", paths["price_validation_plan"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[0]["extra_price_metrics"])["jnj_expected_rybrevant_peak_sales_usd_bn"], 5.0)


if __name__ == "__main__":
    unittest.main()
