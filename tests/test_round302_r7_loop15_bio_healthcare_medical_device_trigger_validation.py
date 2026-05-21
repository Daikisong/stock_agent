from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round302_r7_loop15_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round302_r7_loop15_bio_healthcare_medical_device_trigger_validation import (
    ROUND302_CASE_CANDIDATES,
    ROUND302_GREEN_BLOCKERS,
    ROUND302_HARD_4C_GATES,
    ROUND302_LARGE_SECTOR,
    ROUND302_REQUIRED_TARGET_ALIASES,
    ROUND302_SCORE_DOWN_AXES,
    ROUND302_SCORE_UP_AXES,
    ROUND302_SHADOW_WEIGHT_ROWS,
    ROUND302_STAGE2_ACTIONABLE_RULES,
    ROUND302_STAGE3_GREEN_RULES,
    ROUND302_STAGE3_YELLOW_RULES,
    ROUND302_STAGE4B_WATCH_TRIGGERS,
    ROUND302_TRIGGER_RECORDS,
    render_round302_stage_rules_markdown,
    render_round302_stage4b_4c_review_markdown,
    render_round302_trigger_grid_markdown,
    round302_audit_payload,
    round302_case_records,
    round302_case_rows,
    round302_shadow_weight_rows,
    round302_summary,
    round302_trigger_rows,
    write_round302_r7_loop15_reports,
)


class Round302R7Loop15BioHealthcareTriggerValidationTests(unittest.TestCase):
    def test_round302_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND302_REQUIRED_TARGET_ALIASES), 9)
        self.assertTrue(set(ROUND302_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND302_REQUIRED_TARGET_ALIASES["SC_FORMULATION_ROYALTY_STAGE2_TO_GREEN"],
            E2RArchetype.SC_FORMULATION_ROYALTY_STAGE2_TO_GREEN.value,
        )
        self.assertEqual(
            ROUND302_REQUIRED_TARGET_ALIASES["AESTHETIC_TOXIN_US_LAUNCH_STAGE2"],
            E2RArchetype.AESTHETIC_TOXIN_US_LAUNCH_STAGE2.value,
        )
        self.assertEqual(
            ROUND302_REQUIRED_TARGET_ALIASES["BIOSIMILAR_PATENT_LITIGATION_4C_WATCH"],
            E2RArchetype.BIOSIMILAR_PATENT_LITIGATION_4C_WATCH.value,
        )

    def test_archetype_definitions_capture_r7_loop15_rules(self) -> None:
        sc_formulation = archetype_definition(E2RArchetype.SC_FORMULATION_ROYALTY_STAGE2_TO_GREEN)
        patent_watch = archetype_definition(E2RArchetype.SC_FORMULATION_PATENT_4C_WATCH)
        localization = archetype_definition(E2RArchetype.BIOPHARMA_TARIFF_LOCALIZATION_STAGE2)
        cdmo_price_failed = archetype_definition(E2RArchetype.CDMO_LOCALIZATION_EVIDENCE_GOOD_PRICE_FAILED)
        vaccine_ma = archetype_definition(E2RArchetype.VACCINE_CDMO_MA_STAGE2_ACTIONABLE)
        toxin_launch = archetype_definition(E2RArchetype.AESTHETIC_TOXIN_US_LAUNCH_STAGE2)
        device_control = archetype_definition(E2RArchetype.AESTHETIC_DEVICE_MA_CONTROL_PREMIUM)
        biosimilar_litigation = archetype_definition(E2RArchetype.BIOSIMILAR_PATENT_LITIGATION_4C_WATCH)
        private_lo = archetype_definition(E2RArchetype.PRIVATE_BIOTECH_LO_REFERENCE)

        self.assertIn("royalty recognition", " ".join(sc_formulation.stage3_high_conviction_signals))
        self.assertIn("injunction", " ".join(patent_watch.stage4c_thesis_break_signals))
        self.assertIn("facility utilization", " ".join(localization.stage3_high_conviction_signals))
        self.assertIn("market-relative price recovery", " ".join(cdmo_price_failed.stage3_high_conviction_signals))
        self.assertIn("strong event return", " ".join(vaccine_ma.stage2_candidate_signals))
        self.assertIn("clinic adoption", " ".join(toxin_launch.stage3_high_conviction_signals))
        self.assertIn("control premium", " ".join(device_control.false_positive_patterns))
        self.assertIn("patent clearance", " ".join(biosimilar_litigation.false_positive_patterns))
        self.assertIn("upfront", " ".join(private_lo.stage2_candidate_signals))

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round302_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND302_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_use_round302_cases_as_candidate_generation_input", record.green_guardrails)
            self.assertIn("do_not_treat_fda_factory_lo_or_launch_headline_as_green", record.green_guardrails)
            self.assertIn("hard_4c_confirmed_false", record.green_guardrails)

        summary = round302_summary()
        self.assertEqual(summary["round_id"], "round_230")
        self.assertEqual(summary["large_sector"], ROUND302_LARGE_SECTOR)
        self.assertEqual(summary["method"], "trigger_level_backtest_v1")
        self.assertEqual(summary["case_candidate_count"], 9)
        self.assertEqual(summary["trigger_count"], 11)
        self.assertEqual(summary["stage2_actionable_candidate_count"], 3)
        self.assertEqual(summary["stage3_yellow_candidate_count"], 1)
        self.assertEqual(summary["stage3_green_candidate_count"], 1)
        self.assertEqual(summary["stage3_green_confirmed_count"], 0)
        self.assertEqual(summary["hard_4c_case_count"], 0)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])

    def test_case_metrics_separate_approval_capacity_and_commercialization(self) -> None:
        by_id = {case.case_id: case for case in ROUND302_CASE_CANDIDATES}
        alteogen = by_id["r7_loop15_alteogen_keytruda_qlex"]
        patent = by_id["r7_loop15_alteogen_halozyme_patent_watch"]
        samsung = by_id["r7_loop15_samsung_biologics_tariff_localization"]
        celltrion = by_id["r7_loop15_celltrion_us_factory_tariff_hedge"]
        skbio = by_id["r7_loop15_sk_bioscience_idt_biologika"]
        hugel = by_id["r7_loop15_hugel_letybo_us_launch"]
        jeisys = by_id["r7_loop15_jeisys_archimed_aesthetic_device_ma"]
        bioepis = by_id["r7_loop15_samsung_bioepis_amgen_patent_litigation"]
        adel = by_id["r7_loop15_adel_sanofi_private_reference"]

        self.assertEqual(alteogen.primary_archetype, E2RArchetype.SC_FORMULATION_ROYALTY_STAGE2_TO_GREEN)
        self.assertEqual(alteogen.extra_price_metrics["qlex_q1_2026_sales_usd_mn"], 128)
        self.assertIn("commercial_royalty_recognition_missing", alteogen.red_flag_fields)

        self.assertEqual(patent.primary_archetype, E2RArchetype.SC_FORMULATION_PATENT_4C_WATCH)
        self.assertFalse(patent.extra_price_metrics["launch_delay_confirmed"])

        self.assertEqual(samsung.primary_archetype, E2RArchetype.BIOPHARMA_TARIFF_LOCALIZATION_STAGE2)
        self.assertEqual(samsung.event_mae_pct, -0.4)
        self.assertEqual(samsung.score_price_alignment, "evidence_good_but_price_failed")

        self.assertEqual(celltrion.extra_price_metrics["imclone_acquisition_value_usd_mn"], 330)
        self.assertIn("US_facility_utilization_missing", celltrion.red_flag_fields)

        self.assertEqual(skbio.primary_archetype, E2RArchetype.VACCINE_CDMO_MA_STAGE2_ACTIONABLE)
        self.assertEqual(skbio.event_mfe_pct, 11.7)

        self.assertEqual(hugel.primary_archetype, E2RArchetype.AESTHETIC_TOXIN_US_LAUNCH_STAGE2)
        self.assertIn("US_clinic_adoption_missing", hugel.red_flag_fields)

        self.assertEqual(jeisys.primary_archetype, E2RArchetype.AESTHETIC_DEVICE_MA_CONTROL_PREMIUM)
        self.assertTrue(jeisys.extra_price_metrics["delisting_process"])
        self.assertEqual(jeisys.stage_failure_type, "false_yellow")

        self.assertEqual(bioepis.primary_archetype, E2RArchetype.BIOSIMILAR_PATENT_LITIGATION_4C_WATCH)
        self.assertEqual(bioepis.extra_price_metrics["patents_asserted_count"], 34)

        self.assertEqual(adel.primary_archetype, E2RArchetype.PRIVATE_BIOTECH_LO_REFERENCE)
        self.assertEqual(adel.extra_price_metrics["upfront_payment_usd_mn"], 80)
        self.assertEqual(adel.round_case_type, "private_reference")

    def test_trigger_rows_shadow_rules_and_reports_are_explicit(self) -> None:
        trigger_rows = {row["trigger_id"]: row for row in round302_trigger_rows()}
        shadow_rows = {row["archetype"]: row for row in round302_shadow_weight_rows()}
        rules_md = render_round302_stage_rules_markdown()
        trigger_md = render_round302_trigger_grid_markdown()
        stage_md = render_round302_stage4b_4c_review_markdown()

        self.assertEqual(len(ROUND302_TRIGGER_RECORDS), 11)
        self.assertEqual(trigger_rows["r7l15_alteogen_T1"]["promote_to"], "Stage2-Actionable")
        self.assertEqual(trigger_rows["r7l15_alteogen_T3"]["promote_to"], "Stage3-Green_candidate")
        self.assertEqual(trigger_rows["r7l15_samsungbio_T1"]["promote_to"], "Stage2_only")
        self.assertEqual(trigger_rows["r7l15_samsungbioepis_T1"]["promote_to"], "4C-watch")
        self.assertEqual(len(ROUND302_SHADOW_WEIGHT_ROWS), 9)
        self.assertEqual(shadow_rows["SC_FORMULATION_ROYALTY_STAGE2_TO_GREEN"]["royalty_recognition_visibility"], "+5")
        self.assertEqual(shadow_rows["BIOPHARMA_TARIFF_LOCALIZATION_STAGE2"]["cdmo_order_backlog_utilization"], "+5")
        self.assertEqual(shadow_rows["PRIVATE_BIOTECH_LO_REFERENCE"]["total_lo_value_without_upfront_penalty"], "-5")
        self.assertIn("pivotal_or_noninferiority_result_is_public", ROUND302_STAGE2_ACTIONABLE_RULES)
        self.assertIn("approval_launch_and_adoption_guidance_are_visible_but_one_gate_remains", ROUND302_STAGE3_YELLOW_RULES)
        self.assertIn("issuer_royalty_or_revenue_recognition_is_visible", ROUND302_STAGE3_GREEN_RULES)
        self.assertIn("fda_approval_without_launch_or_revenue", ROUND302_GREEN_BLOCKERS)
        self.assertIn("royalty_recognition_visibility", ROUND302_SCORE_UP_AXES)
        self.assertIn("total_lo_value_without_upfront", ROUND302_SCORE_DOWN_AXES)
        self.assertIn("lo_total_value_headline_without_upfront_or_probability", ROUND302_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("biosimilar_litigation_blocks_launch", ROUND302_HARD_4C_GATES)
        self.assertIn("Do not apply these weights to production scoring yet.", rules_md)
        self.assertIn("r7_loop15_alteogen_keytruda_qlex", trigger_md)
        self.assertIn("approval, capacity, LO headline", stage_md)

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round302_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_302.md")
        self.assertEqual(audit["round_id"], "round_230")
        self.assertEqual(audit["large_sector"], ROUND302_LARGE_SECTOR)
        self.assertEqual(audit["method"], "trigger_level_backtest_v1")
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_treat_fda_factory_lo_or_launch_headline_as_green", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(
            [
                "--output-directory",
                "out",
                "--cases",
                "cases.jsonl",
                "--triggers",
                "triggers.jsonl",
                "--audit",
                "audit.json",
                "--weight-profile",
                "weights.csv",
            ]
        )
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.triggers, "triggers.jsonl")
        self.assertEqual(args.audit, "audit.json")
        self.assertEqual(args.weight_profile, "weights.csv")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round302_r7_loop15_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                triggers_path=root / "triggers.jsonl",
                audit_path=root / "audit.json",
                weight_profile_path=root / "weights.csv",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round302_case_rows()
            self.assertEqual(len(records), len(ROUND302_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND302_CASE_CANDIDATES))
            self.assertEqual(len(paths["triggers"].read_text(encoding="utf-8").splitlines()), len(ROUND302_TRIGGER_RECORDS))
            self.assertIn("Alteogen/Qlex", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("Stage3-Green", paths["stage_rules"].read_text(encoding="utf-8"))
            self.assertIn("r7l15_alteogen_T3", paths["trigger_grid_md"].read_text(encoding="utf-8"))
            self.assertIn("SC_FORMULATION_ROYALTY_STAGE2_TO_GREEN", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("BIOPHARMA_TARIFF_LOCALIZATION_STAGE2", paths["weight_profile"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[0]["extra_price_metrics"])["qlex_q1_2026_sales_usd_mn"], 128)


if __name__ == "__main__":
    unittest.main()
