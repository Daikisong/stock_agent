from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round234_r4_loop10_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector
from e2r.sector.round234_r4_loop10_materials_spread_strategic_price_validation import (
    ROUND234_CASE_CANDIDATES,
    ROUND234_GREEN_FORBIDDEN_PATTERNS,
    ROUND234_GREEN_REQUIRED_FIELDS,
    ROUND234_HARD_4C_GATES,
    ROUND234_PRICE_VALIDATION_FIELDS,
    ROUND234_REQUIRED_TARGET_ALIASES,
    ROUND234_SCORE_ADJUSTMENTS,
    ROUND234_SHADOW_WEIGHT_ROWS,
    ROUND234_STAGE4B_WATCH_TRIGGERS,
    render_round234_green_gate_review_markdown,
    render_round234_stage4b_4c_review_markdown,
    round234_audit_payload,
    round234_case_records,
    round234_case_rows,
    round234_deep_sub_archetype_rows,
    round234_shadow_weight_rows,
    round234_summary,
    write_round234_r4_loop10_reports,
)


class Round234R4Loop10MaterialsSpreadStrategicPriceValidationTests(unittest.TestCase):
    def test_targets_map_to_existing_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND234_REQUIRED_TARGET_ALIASES), 15)
        self.assertTrue(set(ROUND234_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND234_REQUIRED_TARGET_ALIASES["STRATEGIC_MINERALS_SUPPLY_CHAIN"],
            E2RArchetype.RARE_METALS_STRATEGIC_MATERIALS.value,
        )
        self.assertEqual(
            ROUND234_REQUIRED_TARGET_ALIASES["BATTERY_MATERIAL_CONTRACT_QUALITY_BREAK"],
            E2RArchetype.CONTRACT_QUALITY_BREAK.value,
        )
        self.assertEqual(
            ROUND234_REQUIRED_TARGET_ALIASES["STEEL_POLICY_CAPEX_TARIFF_HEDGE"],
            E2RArchetype.SPECIALTY_STEEL_US_LOCALIZATION_OPTION.value,
        )

    def test_case_records_validate_and_remain_calibration_only(self) -> None:
        records = round234_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, Round10LargeSector.MATERIALS_SPREAD_STRATEGIC.value)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_ohlc_complete_false", record.green_guardrails)

        summary = round234_summary()
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["success_candidate_count"], 3)
        self.assertEqual(summary["cyclical_success_count"], 1)
        self.assertEqual(summary["event_premium_count"], 1)
        self.assertEqual(summary["failed_rerating_count"], 2)
        self.assertEqual(summary["hard_4c_case_count"], 1)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_ohlc_complete"])

    def test_korea_zinc_splits_strategic_resource_from_governance_dilution(self) -> None:
        case = _case("r4_loop10_korea_zinc_strategic_minerals_governance")

        self.assertEqual(case.primary_archetype, E2RArchetype.RARE_METALS_STRATEGIC_MATERIALS)
        self.assertIn(E2RArchetype.GOVERNANCE_DILUTION_EVENT, case.secondary_archetypes)
        self.assertEqual(case.stage2_date.isoformat(), "2026-03-12")
        self.assertEqual(case.stage4c_date.isoformat(), "2025-12-16")
        self.assertEqual(case.mae_1d, -13.0)
        self.assertEqual(case.extra_price_metrics["us_smelter_project_value_usd_bn"], 7.4)
        self.assertEqual(case.extra_price_metrics["planned_output_tons"], 540000.0)
        self.assertEqual(case.extra_price_metrics["share_issue_vs_project_value_pct"], 25.7)
        self.assertEqual(case.round_alignment_label, "success_candidate_governance_watch")

    def test_petrochemical_restructuring_and_refining_are_not_green(self) -> None:
        lotte = _case("r4_loop10_lotte_hd_petrochemical_restructuring")
        sk = _case("r4_loop10_sk_innovation_soil_refining_cycle")

        self.assertEqual(lotte.primary_archetype, E2RArchetype.PETROCHEMICAL_RESTRUCTURING_KOREA)
        self.assertEqual(lotte.case_type, "failed_rerating")
        self.assertEqual(lotte.extra_price_metrics["target_capacity_cut_national_mn_tpy"], 3.7)
        self.assertEqual(lotte.extra_price_metrics["industry_capacity_cut_goal_pct"], 25.0)
        self.assertIsNone(lotte.stage3_date)

        self.assertEqual(sk.primary_archetype, E2RArchetype.REFINING_OIL_SPREAD)
        self.assertEqual(sk.case_type, "cyclical_success")
        self.assertEqual(sk.extra_price_metrics["q1_beat_vs_estimate_pct"], 57.1)
        self.assertEqual(sk.extra_price_metrics["sk_on_loss_worsening_pct"], 252.8)
        self.assertEqual(sk.rerating_result, "cyclical_rerating")
        self.assertIsNone(sk.stage3_date)

    def test_posco_hyundai_steel_and_lnf_capture_cycle_false_positive_and_hard_4c(self) -> None:
        posco = _case("r4_loop10_posco_minres_lithium_jv")
        steel = _case("r4_loop10_hyundai_steel_policy_capex_rebar_4c")
        lnf = _case("r4_loop10_lnf_tesla_cathode_contract_hard_4c")

        self.assertEqual(posco.primary_archetype, E2RArchetype.LITHIUM_RESOURCE_SECURITY_KOREA)
        self.assertEqual(posco.extra_price_metrics["spodumene_drawdown_peak_to_low_pct"], -89.8)
        self.assertIsNone(posco.stage3_date)

        self.assertEqual(steel.primary_archetype, E2RArchetype.SPECIALTY_STEEL_US_LOCALIZATION_OPTION)
        self.assertEqual(steel.mae_1d_secondary, -21.2)
        self.assertEqual(steel.extra_price_metrics["relative_underperformance_vs_benchmark_pp"], -15.7)
        self.assertEqual(steel.stage_failure_type, "should_have_been_red")

        self.assertEqual(lnf.primary_archetype, E2RArchetype.CONTRACT_QUALITY_BREAK)
        self.assertTrue(lnf.hard_4c_confirmed)
        self.assertEqual(lnf.stage4c_date.isoformat(), "2025-12-29")
        self.assertEqual(lnf.extra_price_metrics["contract_value_drawdown_pct"], -99.999745)
        self.assertEqual(lnf.rerating_result, "thesis_break")

    def test_oci_and_poongsan_are_event_premium_not_green(self) -> None:
        oci = _case("r4_loop10_oci_non_china_polysilicon_spacex_watch")
        poongsan = _case("r4_loop10_poongsan_hanwha_mna_rumor_fade")

        self.assertEqual(oci.primary_archetype, E2RArchetype.POLYSILICON_NON_CHINA_SUPPLY_OPTION)
        self.assertEqual(oci.extra_price_metrics["target_capacity_gw"], 10.0)
        self.assertIn("spacex_supply_talk_unconfirmed_media_report", oci.red_flag_fields)
        self.assertIsNone(oci.stage3_date)

        self.assertEqual(poongsan.primary_archetype, E2RArchetype.COPPER_PROCESSING_PLUS_DEFENSE)
        self.assertEqual(poongsan.case_type, "event_premium")
        self.assertEqual(poongsan.stage4c_date.isoformat(), "2026-04-09")
        self.assertEqual(poongsan.extra_price_metrics["rumor_duration_days"], 6.0)
        self.assertEqual(poongsan.score_price_alignment, "price_moved_without_evidence")

    def test_green_gate_and_stage4_rules_are_explicit(self) -> None:
        required = set(ROUND234_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND234_GREEN_FORBIDDEN_PATTERNS)
        axes = {item.axis for item in ROUND234_SCORE_ADJUSTMENTS}
        green_markdown = render_round234_green_gate_review_markdown()
        stage_review = render_round234_stage4b_4c_review_markdown()

        self.assertIn("actual_product_spread", required)
        self.assertIn("fcf_after_working_capital", required)
        self.assertIn("capex_and_dilution_risk_passed", required)
        self.assertIn("strategic_material_headline_only", forbidden)
        self.assertIn("customer_name_contract_headline_without_calloff", forbidden)
        self.assertIn("contract_value_collapse", ROUND234_HARD_4C_GATES)
        self.assertIn("strategic_minerals_headline_prices_before_offtake_fcf", ROUND234_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("policy_capex_without_funding", axes)
        self.assertIn("contract_headline_without_calloff", axes)
        self.assertIn("Do not apply these weights to production scoring yet.", green_markdown)
        self.assertIn("Tesla customer name", green_markdown)
        self.assertIn("r4_loop10_lnf_tesla_cathode_contract_hard_4c", stage_review)

    def test_shadow_weights_deep_rows_and_price_fields_cover_round234(self) -> None:
        fields = set(ROUND234_PRICE_VALIDATION_FIELDS)
        shadow_text = "\n".join(str(row) for row in round234_shadow_weight_rows())
        deep_rows = round234_deep_sub_archetype_rows()

        self.assertEqual(len(ROUND234_SHADOW_WEIGHT_ROWS), 9)
        self.assertIn("contract_value_drawdown_pct", fields)
        self.assertIn("share_issue_vs_project_value_pct", fields)
        self.assertIn("rumor_duration_days", fields)
        self.assertIn("RARE_METALS_STRATEGIC_MATERIALS", shadow_text)
        self.assertIn("CONTRACT_QUALITY_BREAK", shadow_text)
        self.assertIn("SPECIALTY_STEEL_US_LOCALIZATION_OPTION", shadow_text)
        self.assertTrue(any("Korea Zinc" in row["terms"] for row in deep_rows))
        self.assertTrue(any("L&F" in row["terms"] for row in deep_rows))

    def test_summary_and_audit_payload_are_calibration_only(self) -> None:
        audit = round234_audit_payload()

        self.assertEqual(audit["source_round"], "docs/round/round_234.md")
        self.assertEqual(audit["large_sector"], Round10LargeSector.MATERIALS_SPREAD_STRATEGIC.value)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_use_round234_cases_as_candidate_generation_input", audit["what_not_to_change"])
        self.assertIn("do_not_lower_stage3_green_thresholds", audit["what_not_to_change"])

    def test_cli_parser_and_writer_outputs(self) -> None:
        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round234_r4_loop10_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round234_case_rows()
            self.assertEqual(len(records), len(ROUND234_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND234_CASE_CANDIDATES))
            self.assertIn("Korea Zinc", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("contract_value_collapse", paths["stage4b_4c_review"].read_text(encoding="utf-8"))
            self.assertIn("CONTRACT_QUALITY_BREAK", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("contract_value_drawdown_pct", paths["price_validation_fields"].read_text(encoding="utf-8"))


def _case(case_id: str) -> object:
    return next(case for case in ROUND234_CASE_CANDIDATES if case.case_id == case_id)


if __name__ == "__main__":
    unittest.main()
