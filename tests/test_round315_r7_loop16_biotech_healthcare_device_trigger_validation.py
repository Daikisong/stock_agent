from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round315_r7_loop16_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round315_r7_loop16_biotech_healthcare_device_trigger_validation import (
    ROUND315_4C_WATCH_GATES,
    ROUND315_CASE_CANDIDATES,
    ROUND315_GREEN_BLOCKERS,
    ROUND315_LARGE_SECTOR,
    ROUND315_REQUIRED_TARGET_ALIASES,
    ROUND315_ROW_SEPARATION_RULES,
    ROUND315_SCORE_DOWN_AXES,
    ROUND315_SCORE_UP_AXES,
    ROUND315_SHADOW_WEIGHT_ROWS,
    ROUND315_STAGE2_ACTIONABLE_RULES,
    ROUND315_STAGE3_GREEN_RULES,
    ROUND315_STAGE3_YELLOW_RULES,
    ROUND315_STAGE4B_WATCH_TRIGGERS,
    ROUND315_TRIGGER_RECORDS,
    render_round315_stage4b_4c_review_markdown,
    render_round315_stage_rules_markdown,
    render_round315_trigger_grid_markdown,
    round315_audit_payload,
    round315_case_records,
    round315_case_rows,
    round315_shadow_weight_rows,
    round315_summary,
    round315_trigger_rows,
    write_round315_r7_loop16_reports,
)


class Round315R7Loop16BiotechHealthcareDeviceTests(unittest.TestCase):
    def test_round315_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND315_REQUIRED_TARGET_ALIASES), 9)
        self.assertTrue(set(ROUND315_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND315_REQUIRED_TARGET_ALIASES["SC_FORMULATION_PLATFORM_STAGE3_YELLOW"],
            E2RArchetype.SC_FORMULATION_PLATFORM_STAGE3_YELLOW.value,
        )
        self.assertEqual(
            ROUND315_REQUIRED_TARGET_ALIASES["VACCINE_CDMO_MA_STAGE2_ACTIONABLE"],
            E2RArchetype.VACCINE_CDMO_MA_STAGE2_ACTIONABLE.value,
        )
        self.assertEqual(
            ROUND315_REQUIRED_TARGET_ALIASES["BIOSIMILAR_PATENT_LITIGATION_4C_WATCH"],
            E2RArchetype.BIOSIMILAR_PATENT_LITIGATION_4C_WATCH.value,
        )
        self.assertEqual(
            ROUND315_REQUIRED_TARGET_ALIASES["PHARMA_TARIFF_4B_4C_WATCH"],
            E2RArchetype.PHARMA_TARIFF_4B_4C_WATCH.value,
        )

    def test_archetype_definitions_capture_round315_healthcare_rules(self) -> None:
        sc_platform = archetype_definition(E2RArchetype.SC_FORMULATION_PLATFORM_STAGE3_YELLOW)
        policy = archetype_definition(E2RArchetype.BIOPHARMA_TARIFF_POLICY_SUPPORT_STAGE2)
        cdmo = archetype_definition(E2RArchetype.CDMO_US_FACILITY_EXPANSION_STAGE2_PRICE_MUTED)
        vaccine = archetype_definition(E2RArchetype.VACCINE_CDMO_MA_STAGE2_ACTIONABLE)
        localization = archetype_definition(E2RArchetype.BIOPHARMA_US_LOCALIZATION_STAGE2_WITH_CAPEX_GATE)
        oncology = archetype_definition(E2RArchetype.ONCOLOGY_APPROVAL_STAGE2_WITH_MANUFACTURING_4B)
        biosimilar = archetype_definition(E2RArchetype.BIOSIMILAR_PATENT_LITIGATION_4C_WATCH)
        aesthetic = archetype_definition(E2RArchetype.AESTHETIC_MEDICAL_DEVICE_PE_BUYOUT_STAGE2)
        tariff = archetype_definition(E2RArchetype.PHARMA_TARIFF_4B_4C_WATCH)

        self.assertIn("royalty", " ".join(sc_platform.stage3_high_conviction_signals))
        self.assertIn("policy support without backlog", " ".join(policy.false_positive_patterns))
        self.assertIn("facility acquisition without utilization", " ".join(cdmo.false_positive_patterns))
        self.assertIn("facility utilization", " ".join(vaccine.stage3_high_conviction_signals))
        self.assertIn("capex ROIC", " ".join(localization.stage3_high_conviction_signals))
        self.assertIn("manufacturing inspection CRL", " ".join(oncology.stage4c_thesis_break_signals))
        self.assertIn("injunction", " ".join(biosimilar.stage4c_thesis_break_signals))
        self.assertIn("control premium", " ".join(aesthetic.false_positive_patterns))
        self.assertIn("margin compression", " ".join(tariff.stage4c_thesis_break_signals))

    def test_case_records_validate_and_remain_calibration_only(self) -> None:
        records = round315_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND315_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_use_round315_cases_as_candidate_generation_input", record.green_guardrails)
            self.assertIn(
                "do_not_treat_approval_facility_MA_filing_buyout_or_tariff_headline_as_Green_without_royalty_sales_utilization_patent_clearance_or_margin",
                record.green_guardrails,
            )

        summary = round315_summary()
        self.assertEqual(summary["round_id"], "round_243")
        self.assertEqual(summary["large_sector"], ROUND315_LARGE_SECTOR)
        self.assertEqual(summary["case_candidate_count"], 9)
        self.assertEqual(summary["trigger_count"], 9)
        self.assertEqual(summary["target_archetype_count"], 9)
        self.assertEqual(summary["stage2_actionable_candidate_count"], 3)
        self.assertEqual(summary["stage2_policy_or_localization_candidate_count"], 4)
        self.assertEqual(summary["stage3_yellow_candidate_count"], 1)
        self.assertEqual(summary["stage3_green_confirmed_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 6)
        self.assertEqual(summary["stage4c_watch_count"], 3)
        self.assertEqual(summary["hard_4c_case_count"], 0)
        self.assertEqual(summary["evidence_good_but_price_failed_or_muted_count"], 3)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertTrue(summary["shadow_weight_only"])

    def test_case_metrics_separate_approval_facility_ma_litigation_and_tariff(self) -> None:
        by_id = {case.case_id: case for case in ROUND315_CASE_CANDIDATES}
        alteogen = by_id["r7_loop16_alteogen_keytruda_sc"]
        policy = by_id["r7_loop16_samsung_biologics_policy_support"]
        gsk = by_id["r7_loop16_samsung_biologics_gsk_us_facility"]
        skbio = by_id["r7_loop16_sk_bioscience_idt_biologika"]
        celltrion = by_id["r7_loop16_celltrion_us_factory_localization"]
        yuhan = by_id["r7_loop16_yuhan_lazertinib_jnj_rybrevant"]
        bioepis = by_id["r7_loop16_samsung_bioepis_amgen_litigation"]
        jeisys = by_id["r7_loop16_jeisys_archimed_medical_device_buyout"]
        tariff = by_id["r7_loop16_pharma_tariff_localization"]

        self.assertEqual(alteogen.extra_price_metrics["qlex_q1_2026_sales_usd_mn"], 128)
        self.assertEqual(alteogen.stage_failure_type, "yellow_success")

        self.assertEqual(policy.extra_price_metrics["samsung_biologics_event_return_pct"], 6.23)

        self.assertEqual(gsk.extra_price_metrics["facility_capacity_liters"], 60000)
        self.assertEqual(gsk.score_price_alignment, "evidence_good_but_price_failed")

        self.assertEqual(skbio.extra_price_metrics["deal_value_krw_bn"], 339)
        self.assertEqual(skbio.event_mfe_pct, 11.7)

        self.assertEqual(celltrion.extra_price_metrics["imclone_acquisition_value_usd_mn"], 330)

        self.assertEqual(yuhan.extra_price_metrics["sc_crl_date"], "2024-12-16")
        self.assertIn("manufacturing_inspection_CRL_4B", yuhan.red_flag_fields)

        self.assertEqual(bioepis.extra_price_metrics["alleged_patents"], 34)
        self.assertFalse(bioepis.hard_4c_confirmed)

        self.assertEqual(jeisys.extra_price_metrics["reported_share_close_krw"], 12860)

        self.assertEqual(tariff.extra_price_metrics["tariff_rate_context_pct"], 100)

    def test_trigger_rows_shadow_rules_and_reports_are_explicit(self) -> None:
        trigger_rows = {row["trigger_id"]: row for row in round315_trigger_rows()}
        shadow_rows = {row["archetype"]: row for row in round315_shadow_weight_rows()}
        rules_md = render_round315_stage_rules_markdown()
        trigger_md = render_round315_trigger_grid_markdown()
        stage_md = render_round315_stage4b_4c_review_markdown()

        self.assertEqual(len(ROUND315_TRIGGER_RECORDS), 9)
        self.assertEqual(trigger_rows["r7l16_alteogen_keytruda_T2"]["promote_to"], "Stage3-Yellow_candidate")
        self.assertEqual(trigger_rows["r7l16_skbioscience_idt_T0"]["promote_to"], "Stage2-Actionable")
        self.assertEqual(trigger_rows["r7l16_samsung_bioepis_amgen_T1"]["promote_to"], "4C-watch")
        self.assertEqual(len(ROUND315_SHADOW_WEIGHT_ROWS), 9)
        self.assertEqual(shadow_rows["SC_FORMULATION_PLATFORM_STAGE3_YELLOW"]["regulatory_approval_to_sales_bridge"], "+5")
        self.assertEqual(shadow_rows["VACCINE_CDMO_MA_STAGE2_ACTIONABLE"]["MA_price_reaction"], "+5")
        self.assertEqual(shadow_rows["PHARMA_TARIFF_4B_4C_WATCH"]["US_localization_tariff_hedge"], "+5")
        self.assertIn("event_return_at_least_5pct", ROUND315_STAGE2_ACTIONABLE_RULES)
        self.assertIn("reported_price_anchor_supports_trigger_but_full_adjusted_OHLC_is_missing", ROUND315_STAGE3_YELLOW_RULES)
        self.assertIn("tariff_hedge_translates_into_protected_gross_margin", ROUND315_STAGE3_GREEN_RULES)
        self.assertIn("approval_without_economics", ROUND315_GREEN_BLOCKERS)
        self.assertIn("royalty_milestone_visibility", ROUND315_SCORE_UP_AXES)
        self.assertIn("biosimilar_filing_without_patent_clearance", ROUND315_SCORE_DOWN_AXES)
        self.assertIn("FDA_CRL_appears_due_manufacturing_or_inspection_issue", ROUND315_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("patent_lawsuit_blocks_biosimilar_launch", ROUND315_4C_WATCH_GATES)
        self.assertIn("trigger_calibration_row_stores_event_anchor_approval_sales_facility_MA_litigation_or_tariff_metrics", ROUND315_ROW_SEPARATION_RULES)
        self.assertIn("Do not apply these weights to production scoring yet.", rules_md)
        self.assertIn("r7_loop16_alteogen_keytruda_sc", trigger_md)
        self.assertIn("r7_loop16_samsung_bioepis_amgen_litigation", stage_md)

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round315_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_315.md")
        self.assertEqual(audit["round_id"], "round_243")
        self.assertEqual(audit["large_sector"], ROUND315_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_change_production_scoring", audit["what_not_to_change"])

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
            paths = write_round315_r7_loop16_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                triggers_path=root / "triggers.jsonl",
                audit_path=root / "audit.json",
                weight_profile_path=root / "weights.csv",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round315_case_rows()
            self.assertEqual(len(records), len(ROUND315_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND315_CASE_CANDIDATES))
            self.assertEqual(len(paths["triggers"].read_text(encoding="utf-8").splitlines()), len(ROUND315_TRIGGER_RECORDS))
            self.assertIn("Alteogen", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("Stage2-Actionable", paths["stage_rules"].read_text(encoding="utf-8"))
            self.assertIn("r7l16_samsung_bioepis_amgen_T1", paths["trigger_grid_md"].read_text(encoding="utf-8"))
            self.assertIn("PHARMA_TARIFF_4B_4C_WATCH", paths["weight_profiles"].read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
