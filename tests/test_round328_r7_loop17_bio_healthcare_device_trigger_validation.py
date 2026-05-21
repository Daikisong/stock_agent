from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round328_r7_loop17_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round328_r7_loop17_bio_healthcare_device_trigger_validation import (
    ROUND328_CASE_CANDIDATES,
    ROUND328_GREEN_BLOCKERS,
    ROUND328_HARD_4C_GATES,
    ROUND328_LARGE_SECTOR,
    ROUND328_REQUIRED_TARGET_ALIASES,
    ROUND328_ROW_SEPARATION_RULES,
    ROUND328_SCORE_DOWN_AXES,
    ROUND328_SCORE_UP_AXES,
    ROUND328_SHADOW_WEIGHT_ROWS,
    ROUND328_STAGE2_ACTIONABLE_RULES,
    ROUND328_STAGE3_GREEN_RULES,
    ROUND328_STAGE3_YELLOW_RULES,
    ROUND328_STAGE4B_WATCH_TRIGGERS,
    ROUND328_TRIGGER_RECORDS,
    render_round328_stage4b_4c_review_markdown,
    render_round328_stage_rules_markdown,
    render_round328_trigger_grid_markdown,
    round328_audit_payload,
    round328_case_records,
    round328_case_rows,
    round328_shadow_weight_rows,
    round328_summary,
    round328_trigger_rows,
    write_round328_r7_loop17_reports,
)


class Round328R7Loop17BioHealthcareDeviceTests(unittest.TestCase):
    def test_round328_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND328_REQUIRED_TARGET_ALIASES), 8)
        self.assertTrue(set(ROUND328_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND328_REQUIRED_TARGET_ALIASES["VACCINE_CDMO_CROSS_BORDER_MA_STAGE2_ACTIONABLE"],
            E2RArchetype.VACCINE_CDMO_CROSS_BORDER_MA_STAGE2_ACTIONABLE.value,
        )
        self.assertEqual(
            ROUND328_REQUIRED_TARGET_ALIASES["PLATFORM_ENZYME_BLOCKBUSTER_STAGE3_YELLOW"],
            E2RArchetype.PLATFORM_ENZYME_BLOCKBUSTER_STAGE3_YELLOW.value,
        )
        self.assertEqual(
            ROUND328_REQUIRED_TARGET_ALIASES["BIOSIMILAR_PATENT_LITIGATION_4B"],
            E2RArchetype.BIOSIMILAR_PATENT_LITIGATION_4B.value,
        )

    def test_archetype_definitions_capture_round328_bio_rules(self) -> None:
        policy = archetype_definition(E2RArchetype.BIOPHARMA_POLICY_SUPPORT_STAGE2_ACTIONABLE)
        facility = archetype_definition(E2RArchetype.CDMO_US_FACILITY_TARIFF_HEDGE_STAGE2_PRICE_FAILED)
        vaccine_ma = archetype_definition(E2RArchetype.VACCINE_CDMO_CROSS_BORDER_MA_STAGE2_ACTIONABLE)
        biosimilar_local = archetype_definition(E2RArchetype.BIOSIMILAR_US_LOCALIZATION_STAGE2_NO_PRICE)
        platform = archetype_definition(E2RArchetype.PLATFORM_ENZYME_BLOCKBUSTER_STAGE3_YELLOW)
        toxin = archetype_definition(E2RArchetype.AESTHETIC_TOXIN_US_FDA_STAGE2)
        device_ma = archetype_definition(E2RArchetype.MEDICAL_AESTHETIC_DEVICE_MA_STAGE2)
        patent = archetype_definition(E2RArchetype.BIOSIMILAR_PATENT_LITIGATION_4B)

        self.assertIn("company-specific contract", " ".join(policy.stage3_high_conviction_signals))
        self.assertIn("facility utilization", " ".join(facility.stage3_high_conviction_signals))
        self.assertIn("orderbook", " ".join(vaccine_ma.stage3_high_conviction_signals))
        self.assertIn("product transfer", " ".join(biosimilar_local.stage3_high_conviction_signals))
        self.assertIn("royalty or supply economics", " ".join(platform.stage3_high_conviction_signals))
        self.assertIn("sell-through", " ".join(toxin.stage3_high_conviction_signals))
        self.assertIn("delisting", " ".join(device_ma.stage4b_graduation_overheat_signals))
        self.assertIn("patent clearance", " ".join(patent.stage3_high_conviction_signals))

    def test_case_records_validate_and_remain_calibration_only(self) -> None:
        records = round328_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND328_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_use_round328_cases_as_candidate_generation_input", record.green_guardrails)
            self.assertEqual(record.price_validation.price_validation_status, "price_data_unavailable_after_deep_search")

        summary = round328_summary()
        self.assertEqual(summary["source_round"], "docs/round/round_328.md")
        self.assertEqual(summary["round_id"], "round_256")
        self.assertEqual(summary["large_sector"], ROUND328_LARGE_SECTOR)
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["trigger_count"], 8)
        self.assertEqual(summary["target_archetype_count"], 8)
        self.assertEqual(summary["stage2_actionable_candidate_count"], 2)
        self.assertEqual(summary["stage3_yellow_candidate_count"], 1)
        self.assertEqual(summary["stage3_green_confirmed_count"], 0)
        self.assertEqual(summary["hard_4c_case_count"], 0)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])

    def test_case_metrics_separate_policy_facility_launch_ma_and_litigation(self) -> None:
        by_id = {case.case_id: case for case in ROUND328_CASE_CANDIDATES}
        sk_bio = by_id["r7_loop17_sk_bioscience_idt_biologika"]
        samsung_policy = by_id["r7_loop17_samsung_biologics_policy_support"]
        samsung_gsk = by_id["r7_loop17_samsung_biologics_gsk_us_facility"]
        celltrion = by_id["r7_loop17_celltrion_us_factory_localization"]
        alteogen = by_id["r7_loop17_alteogen_keytruda_sc"]
        hugel = by_id["r7_loop17_hugel_letybo_us_fda"]
        jeisys = by_id["r7_loop17_jeisys_archimed_medical_aesthetic_ma"]
        patent = by_id["r7_loop17_samsung_bioepis_amgen_patent_litigation"]

        self.assertEqual(sk_bio.extra_price_metrics["event_return_pct"], 11.7)
        self.assertIn("utilization_4B", sk_bio.red_flag_fields)

        self.assertEqual(samsung_policy.extra_price_metrics["market_relative_outperformance_pp"], 5.24)
        self.assertIn("company_specific_contract_not_confirmed_4B", samsung_policy.red_flag_fields)

        self.assertEqual(samsung_gsk.score_price_alignment, "evidence_good_but_price_failed")
        self.assertEqual(samsung_gsk.extra_price_metrics["capacity_liters"], 60000)

        self.assertIsNone(celltrion.extra_price_metrics["direct_price_anchor"])
        self.assertIn("rebate_pressure_4B", celltrion.red_flag_fields)

        self.assertEqual(alteogen.stage_candidate, "Stage3-Yellow candidate")
        self.assertEqual(alteogen.extra_price_metrics["expected_peak_adoption_pct"], "30-40")

        self.assertIn("US_FDA_approval_glabellar_lines", hugel.evidence_fields)
        self.assertIn("physician_adoption_4B", hugel.red_flag_fields)

        self.assertEqual(jeisys.case_type, "event_premium")
        self.assertEqual(jeisys.extra_price_metrics["reported_close_price_krw"], 12860)

        self.assertEqual(patent.stage_candidate, "4B-watch")
        self.assertFalse(patent.hard_4c_confirmed)
        self.assertEqual(patent.extra_price_metrics["asserted_patents"], 34)

    def test_trigger_rows_shadow_rules_and_reports_are_explicit(self) -> None:
        trigger_rows = {row["trigger_id"]: row for row in round328_trigger_rows()}
        shadow_rows = {row["archetype"]: row for row in round328_shadow_weight_rows()}
        rules_md = render_round328_stage_rules_markdown()
        trigger_md = render_round328_trigger_grid_markdown()
        stage_md = render_round328_stage4b_4c_review_markdown()

        self.assertEqual(len(ROUND328_TRIGGER_RECORDS), 8)
        self.assertEqual(trigger_rows["r7l17_sk_bioscience_idt_T2"]["promote_to"], "Stage2-Actionable")
        self.assertEqual(trigger_rows["r7l17_alteogen_keytruda_T3"]["promote_to"], "Stage3-Yellow")
        self.assertEqual(trigger_rows["r7l17_bioepis_patent_T1"]["promote_to"], "4B-watch")
        self.assertEqual(len(ROUND328_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["VACCINE_CDMO_CROSS_BORDER_MA_STAGE2_ACTIONABLE"]["manufacturing_asset_MA"], "+5")
        self.assertEqual(shadow_rows["PLATFORM_ENZYME_BLOCKBUSTER_STAGE3_YELLOW"]["blockbuster_platform_linkage"], "+5")
        self.assertEqual(shadow_rows["BIOSIMILAR_PATENT_LITIGATION_4B"]["patent_litigation_risk"], "+5")
        self.assertIn("event_return_at_least_5pct_or_clear_relative_outperformance", ROUND328_STAGE2_ACTIONABLE_RULES)
        self.assertIn("royalty_product_supply_or_reimbursement_revenue_visibility_exists", ROUND328_STAGE3_YELLOW_RULES)
        self.assertIn("CDMO_utilization_and_margin_are_visible", ROUND328_STAGE3_GREEN_RULES)
        self.assertIn("FDA_approval_without_sellthrough", ROUND328_GREEN_BLOCKERS)
        self.assertIn("blockbuster_platform_linkage", ROUND328_SCORE_UP_AXES)
        self.assertIn("hard_4C_without_sourced_price_anchor", ROUND328_SCORE_DOWN_AXES)
        self.assertIn("platform_link_without_royalty_economics", ROUND328_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("pivotal_trial_failure", ROUND328_HARD_4C_GATES)
        self.assertIn("do_not_create_MFE_MAE_without_full_adjusted_OHLC", ROUND328_ROW_SEPARATION_RULES)
        self.assertIn("Do not apply these weights to production scoring yet.", rules_md)
        self.assertIn("r7_loop17_alteogen_keytruda_sc", trigger_md)
        self.assertIn("r7_loop17_samsung_bioepis_amgen_patent_litigation", stage_md)

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round328_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_328.md")
        self.assertEqual(audit["round_id"], "round_256")
        self.assertEqual(audit["large_sector"], ROUND328_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_use_round328_cases_as_candidate_generation_input", audit["what_not_to_change"])

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
            paths = write_round328_r7_loop17_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                triggers_path=root / "triggers.jsonl",
                audit_path=root / "audit.json",
                weight_profile_path=root / "weights.csv",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)
            records = load_case_library(paths["cases"])
            self.assertEqual(len(records), len(ROUND328_CASE_CANDIDATES))
            self.assertEqual(len(round328_case_rows()), len(ROUND328_CASE_CANDIDATES))
            self.assertIn("Stage3-Green confirmed: `0`", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("Full adjusted OHLC", paths["price_validation_plan"].read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
