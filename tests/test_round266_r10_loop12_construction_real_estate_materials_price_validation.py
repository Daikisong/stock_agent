from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round266_r10_loop12_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector
from e2r.sector.round266_r10_loop12_construction_real_estate_materials_price_validation import (
    ROUND266_CASE_CANDIDATES,
    ROUND266_DEEP_SUB_ARCHETYPES,
    ROUND266_GREEN_FORBIDDEN_PATTERNS,
    ROUND266_GREEN_REQUIRED_FIELDS,
    ROUND266_HARD_4C_GATES,
    ROUND266_LARGE_SECTOR,
    ROUND266_PRICE_VALIDATION_FIELDS,
    ROUND266_REQUIRED_TARGET_ALIASES,
    ROUND266_SCORE_ADJUSTMENTS,
    ROUND266_SHADOW_WEIGHT_ROWS,
    ROUND266_STAGE4B_WATCH_TRIGGERS,
    render_round266_green_gate_review_markdown,
    render_round266_stage4b_4c_review_markdown,
    round266_audit_payload,
    round266_case_records,
    round266_case_rows,
    round266_deep_sub_archetype_rows,
    round266_shadow_weight_rows,
    round266_summary,
    write_round266_r10_loop12_reports,
)


class Round266R10Loop12ConstructionRealEstateMaterialsPriceValidationTests(unittest.TestCase):
    def test_targets_are_explicit_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND266_REQUIRED_TARGET_ALIASES), 8)
        self.assertTrue(set(ROUND266_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND266_REQUIRED_TARGET_ALIASES["NUCLEAR_EPC_EXPORT_STAGE2"],
            E2RArchetype.NUCLEAR_EPC_EXPORT_STAGE2.value,
        )
        self.assertEqual(
            ROUND266_REQUIRED_TARGET_ALIASES["NUCLEAR_EXPORT_LEGAL_4C_WATCH"],
            E2RArchetype.NUCLEAR_EXPORT_LEGAL_4C_WATCH.value,
        )
        self.assertEqual(
            ROUND266_REQUIRED_TARGET_ALIASES["CONSTRUCTION_SAFETY_HARD_REFERENCE"],
            E2RArchetype.CONSTRUCTION_SAFETY_HARD_REFERENCE.value,
        )
        self.assertEqual(
            ROUND266_REQUIRED_TARGET_ALIASES["LNG_POWER_INFRA_CONSORTIUM_OPTION"],
            E2RArchetype.LNG_POWER_INFRA_CONSORTIUM_OPTION.value,
        )

    def test_archetype_definitions_capture_round266_gates(self) -> None:
        nuclear = archetype_definition(E2RArchetype.NUCLEAR_EPC_EXPORT_STAGE2)
        legal = archetype_definition(E2RArchetype.NUCLEAR_EXPORT_LEGAL_4C_WATCH)
        safety = archetype_definition(E2RArchetype.CONSTRUCTION_SAFETY_HARD_REFERENCE)
        recurring = archetype_definition(E2RArchetype.RECURRING_FATAL_ACCIDENT_REGULATORY_4C)
        housing = archetype_definition(E2RArchetype.HOUSING_SUPPLY_POLICY_EVENT)
        public = archetype_definition(E2RArchetype.PUBLIC_INFRASTRUCTURE_POLICY_EVENT)
        lng = archetype_definition(E2RArchetype.LNG_POWER_INFRA_CONSORTIUM_OPTION)
        materials = archetype_definition(E2RArchetype.BUILDING_MATERIALS_DEMAND_BREAK)

        self.assertIn("final contract signed", nuclear.stage3_high_conviction_signals)
        self.assertIn("legal appeal pending", legal.stage4c_thesis_break_signals)
        self.assertIn("fatal construction collapse", safety.stage4c_thesis_break_signals)
        self.assertIn("license revocation risk", recurring.stage4c_thesis_break_signals)
        self.assertIn("presales and margin confirmed", housing.stage3_high_conviction_signals)
        self.assertIn("listed contractor award", public.stage3_high_conviction_signals)
        self.assertIn("investor selected", lng.stage3_high_conviction_signals)
        self.assertIn("net-profit forecast cut", materials.stage4c_thesis_break_signals)

    def test_case_records_validate_and_keep_calibration_guardrails(self) -> None:
        records = round266_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, Round10LargeSector.CONSTRUCTION_REAL_ESTATE_MATERIALS.value)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("direct_listed_hard_4c_confirmed_false", record.green_guardrails)
            self.assertIn(
                "do_not_treat_preferred_bidder_talks_policy_public_infra_candidate_consortium_or_rebar_target_upside_as_green",
                record.green_guardrails,
            )

        summary = round266_summary()
        self.assertEqual(summary["analyst_round_id"], "round_194")
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["success_candidate_count"], 3)
        self.assertEqual(summary["event_premium_count"], 2)
        self.assertEqual(summary["safety_hard_reference_count"], 1)
        self.assertEqual(summary["hard_4c_case_count"], 1)
        self.assertEqual(summary["direct_listed_hard_4c_case_count"], 0)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 6)
        self.assertEqual(summary["stage4c_watch_count"], 3)
        self.assertEqual(summary["thesis_break_watch_count"], 5)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertTrue(summary["shadow_weight_only"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["hard_4c_confirmed"])
        self.assertFalse(summary["direct_listed_hard_4c_confirmed"])

    def test_nuclear_and_lng_cases_are_stage2_not_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND266_CASE_CANDIDATES}
        czech = by_id["r10_loop12_czech_nuclear_preferred_bid_legal_watch"]
        bulgaria = by_id["r10_loop12_hyundai_ec_bulgaria_kozloduy_talks"]
        lng = by_id["r10_loop12_daewoo_ec_nghi_son_lng_candidate"]

        self.assertEqual(czech.primary_archetype, E2RArchetype.NUCLEAR_EPC_EXPORT_STAGE2)
        self.assertIn(E2RArchetype.NUCLEAR_EXPORT_LEGAL_4C_WATCH, czech.secondary_archetypes)
        self.assertEqual(czech.stage2_date.isoformat(), "2024-07-17")
        self.assertEqual(czech.stage4c_date.isoformat(), "2024-08-27")
        self.assertEqual(czech.extra_price_metrics["doosan_enerbility_3m_mfe_pct"], 48.0)
        self.assertEqual(czech.extra_price_metrics["kepco_ec_3m_mfe_pct"], 41.0)
        self.assertEqual(czech.extra_price_metrics["two_unit_implied_value_usd_bn"], 17.3)
        self.assertIn("legal_appeal_pending", czech.red_flag_fields)

        self.assertEqual(bulgaria.primary_archetype, E2RArchetype.NUCLEAR_EPC_EXPORT_STAGE2)
        self.assertEqual(bulgaria.stage2_date.isoformat(), "2024-02-23")
        self.assertEqual(bulgaria.extra_price_metrics["new_reactors"], 2.0)
        self.assertEqual(bulgaria.extra_price_metrics["additional_capacity_mw"], 2300.0)
        self.assertEqual(bulgaria.extra_price_metrics["average_capacity_per_reactor_mw"], 1150.0)
        self.assertIn("talks_or_MOU_only", bulgaria.red_flag_fields)

        self.assertEqual(lng.primary_archetype, E2RArchetype.LNG_POWER_INFRA_CONSORTIUM_OPTION)
        self.assertEqual(lng.stage2_date.isoformat(), "2024-08-21")
        self.assertEqual(lng.extra_price_metrics["project_value_usd_bn"], 2.5)
        self.assertEqual(lng.extra_price_metrics["capacity_gw"], 1.5)
        self.assertEqual(lng.extra_price_metrics["project_value_per_gw_usd_bn"], 1.67)
        self.assertIn("candidate_consortium_only", lng.red_flag_fields)

    def test_safety_policy_public_infra_and_materials_cases_keep_green_blockers(self) -> None:
        by_id = {case.case_id: case for case in ROUND266_CASE_CANDIDATES}
        collapse = by_id["r10_loop12_hyundai_engineering_anseong_bridge_collapse"]
        recurring = by_id["r10_loop12_posco_dl_recurring_fatal_accident_regulation"]
        housing = by_id["r10_loop12_seoul_housing_ltv_supply_policy"]
        public = by_id["r10_loop12_sejong_presidential_office_public_infra"]
        rebar = by_id["r10_loop12_hyundai_steel_rebar_construction_demand_break"]

        self.assertEqual(collapse.primary_archetype, E2RArchetype.CONSTRUCTION_SAFETY_HARD_REFERENCE)
        self.assertTrue(collapse.hard_4c_confirmed)
        self.assertFalse(collapse.direct_listed_hard_4c_confirmed)
        self.assertEqual(collapse.stage4c_date.isoformat(), "2025-02-25")
        self.assertEqual(collapse.extra_price_metrics["fatalities_ap"], 4.0)
        self.assertEqual(collapse.extra_price_metrics["injured"], 6.0)
        self.assertEqual(collapse.price_validation_status, "unlisted_sector_reference")

        self.assertEqual(recurring.primary_archetype, E2RArchetype.RECURRING_FATAL_ACCIDENT_REGULATORY_4C)
        self.assertFalse(recurring.hard_4c_confirmed)
        self.assertEqual(recurring.extra_price_metrics["proposed_fine_pct_of_operating_profit"], 5.0)
        self.assertEqual(recurring.extra_price_metrics["workplace_deaths_2024"], 589.0)
        self.assertEqual(recurring.extra_price_metrics["dl_executives_resigned"], 80.0)
        self.assertIn("license_revocation_risk", recurring.red_flag_fields)

        self.assertEqual(housing.primary_archetype, E2RArchetype.HOUSING_SUPPLY_POLICY_EVENT)
        self.assertEqual(housing.score_price_alignment, "price_moved_without_evidence")
        self.assertEqual(housing.extra_price_metrics["ltv_before_pct"], 50.0)
        self.assertEqual(housing.extra_price_metrics["ltv_after_pct"], 40.0)
        self.assertEqual(housing.extra_price_metrics["ltv_change_relative_pct"], -20.0)

        self.assertEqual(public.primary_archetype, E2RArchetype.PUBLIC_INFRASTRUCTURE_POLICY_EVENT)
        self.assertEqual(public.extra_price_metrics["site_area_sqm"], 350000.0)
        self.assertEqual(public.extra_price_metrics["site_preparation_cost_krw_bn"], 9.8)
        self.assertEqual(public.extra_price_metrics["site_preparation_cost_per_sqm_krw"], 28000.0)
        self.assertIn("listed_contract_winner_not_disclosed", public.red_flag_fields)

        self.assertEqual(rebar.primary_archetype, E2RArchetype.BUILDING_MATERIALS_DEMAND_BREAK)
        self.assertEqual(rebar.stage4c_price_anchor, 29000.0)
        self.assertEqual(rebar.mae_1d, -1.2)
        self.assertEqual(rebar.extra_price_metrics["net_profit_forecast_cut_pct"], -73.0)
        self.assertEqual(rebar.extra_price_metrics["expected_rebar_price_decline_pct"], -10.0)
        self.assertEqual(rebar.rerating_result, "thesis_break")

    def test_green_gate_4b_4c_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND266_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND266_GREEN_FORBIDDEN_PATTERNS)
        fields = set(ROUND266_PRICE_VALIDATION_FIELDS)
        axes = {item.axis for item in ROUND266_SCORE_ADJUSTMENTS}
        shadow_rows = {row["archetype"]: row for row in round266_shadow_weight_rows()}
        deep_rows = round266_deep_sub_archetype_rows()
        green_markdown = render_round266_green_gate_review_markdown()
        stage_markdown = render_round266_stage4b_4c_review_markdown()

        self.assertIn("final_contract_signed", required)
        self.assertIn("working_capital_and_receivables_stable", required)
        self.assertIn("preferred_bidder_only", forbidden)
        self.assertIn("candidate_consortium_only", forbidden)
        self.assertIn("nuclear_preferred_bidder_rally_before_final_contract", ROUND266_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("fatal_construction_collapse", ROUND266_HARD_4C_GATES)
        self.assertIn("legal_block_on_project_signing", ROUND266_HARD_4C_GATES)
        self.assertIn("reported_3m_mfe", fields)
        self.assertIn("final_contract_signed", axes)
        self.assertIn("legal_appeal_pending", axes)
        self.assertIn("Do not apply these weights to production scoring yet.", green_markdown)
        self.assertIn("preferred bidder", green_markdown)
        self.assertIn("r10_loop12_hyundai_steel_rebar_construction_demand_break", stage_markdown)
        self.assertEqual(len(ROUND266_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["NUCLEAR_EPC_EXPORT_STAGE2"]["final_contract_signed"], "+5")
        self.assertEqual(shadow_rows["HOUSING_SUPPLY_POLICY_EVENT"]["event_penalty"], "-5")
        self.assertEqual(shadow_rows["CONSTRUCTION_SAFETY_HARD_REFERENCE"]["hard_4c_sensitivity"], "+5")
        self.assertTrue(any("Kozloduy" in row["deep_sub_archetype"] for row in deep_rows))
        self.assertIn("Hyundai Steel rebar construction-demand break", ROUND266_DEEP_SUB_ARCHETYPES)

    def test_audit_payload_cli_and_writer_outputs(self) -> None:
        audit = round266_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_266.md")
        self.assertEqual(audit["analyst_round_id"], "round_194")
        self.assertEqual(audit["large_sector"], ROUND266_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertTrue(audit["summary"]["hard_4c_confirmed"])
        self.assertFalse(audit["summary"]["direct_listed_hard_4c_confirmed"])
        self.assertIn("do_not_use_round266_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round266_r10_loop12_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round266_case_rows()
            self.assertEqual(len(records), len(ROUND266_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND266_CASE_CANDIDATES))
            self.assertIn("Czech nuclear is strong Stage 2", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("cash_collection_quality", paths["score_adjustments"].read_text(encoding="utf-8"))
            self.assertIn("NUCLEAR_EPC_EXPORT_STAGE2", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("license_revocation", paths["stage4b_4c_review"].read_text(encoding="utf-8"))
            self.assertEqual(rows[0]["round_score_price_alignment"], "success_candidate_legal_4C_watch")
            self.assertEqual(json.loads(rows[0]["extra_price_metrics"])["doosan_enerbility_3m_mfe_pct"], 48.0)

    def test_production_modules_do_not_import_round266(self) -> None:
        forbidden = "round266_r10_loop12_construction_real_estate_materials_price_validation"
        for rel_path in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = Path(rel_path).read_text(encoding="utf-8")
            self.assertNotIn(forbidden, text)


if __name__ == "__main__":
    unittest.main()
