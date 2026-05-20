from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round286_r4_loop14_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round286_r4_loop14_materials_spreads_strategic_resources_price_validation import (
    ROUND286_CASE_CANDIDATES,
    ROUND286_GREEN_FORBIDDEN_PATTERNS,
    ROUND286_GREEN_REQUIRED_FIELDS,
    ROUND286_HARD_4C_GATES,
    ROUND286_LARGE_SECTOR,
    ROUND286_PRICE_VALIDATION_FIELDS,
    ROUND286_REQUIRED_TARGET_ALIASES,
    ROUND286_SHADOW_WEIGHT_ROWS,
    ROUND286_STAGE4B_WATCH_TRIGGERS,
    render_round286_green_gate_review_markdown,
    render_round286_stage4b_4c_review_markdown,
    round286_audit_payload,
    round286_case_records,
    round286_case_rows,
    round286_deep_sub_archetype_rows,
    round286_shadow_weight_rows,
    round286_summary,
    write_round286_r4_loop14_reports,
)


class Round286R4Loop14MaterialsSpreadsStrategicResourcesTests(unittest.TestCase):
    def test_round286_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND286_REQUIRED_TARGET_ALIASES), 9)
        self.assertTrue(set(ROUND286_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND286_REQUIRED_TARGET_ALIASES["PETROCHEMICAL_SPREAD_COLLAPSE_4C"],
            E2RArchetype.PETROCHEMICAL_SPREAD_COLLAPSE_4C.value,
        )
        self.assertEqual(
            ROUND286_REQUIRED_TARGET_ALIASES["LITHIUM_PRICE_SQUEEZE_EVENT_PREMIUM"],
            E2RArchetype.LITHIUM_PRICE_SQUEEZE_EVENT_PREMIUM.value,
        )
        self.assertEqual(
            ROUND286_REQUIRED_TARGET_ALIASES["RARE_EARTH_EXPORT_CONTROL_SUPPLY_CHAIN_4C"],
            E2RArchetype.RARE_EARTH_EXPORT_CONTROL_SUPPLY_CHAIN_4C.value,
        )

    def test_round286_archetype_definitions_capture_loop14_gates(self) -> None:
        petchem = archetype_definition(E2RArchetype.PETROCHEMICAL_SPREAD_COLLAPSE_4C)
        restructuring = archetype_definition(E2RArchetype.PETROCHEMICAL_RESTRUCTURING_STAGE2_NOT_GREEN)
        steel = archetype_definition(E2RArchetype.STEEL_ANTI_DUMPING_EVENT_PREMIUM)
        zinc = archetype_definition(E2RArchetype.STRATEGIC_METAL_CONTROL_PREMIUM_4B)
        lithium = archetype_definition(E2RArchetype.LITHIUM_RESOURCE_INTEGRATION_STAGE2)
        squeeze = archetype_definition(E2RArchetype.LITHIUM_PRICE_SQUEEZE_EVENT_PREMIUM)
        contract = archetype_definition(E2RArchetype.BATTERY_MATERIAL_CONTRACT_COLLAPSE_HARD_4C)
        cathode = archetype_definition(E2RArchetype.CATHODE_SUPPLY_CHAIN_REBALANCING_STAGE2)

        self.assertIn("deep operating loss", petchem.stage4c_thesis_break_signals)
        self.assertIn("capacity restructuring policy only", restructuring.false_positive_patterns)
        self.assertIn("anti-dumping event treated as demand", steel.false_positive_patterns)
        self.assertIn("control premium only", zinc.false_positive_patterns)
        self.assertIn("mine stake without processing margin", lithium.false_positive_patterns)
        self.assertIn("CATL license suspension sentiment", squeeze.false_positive_patterns)
        self.assertIn("contract value collapses", contract.stage4c_thesis_break_signals)
        self.assertIn("nonbinding supply agreement", cathode.false_positive_patterns)

    def test_case_records_validate_and_remain_calibration_only(self) -> None:
        records = round286_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND286_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("round286_hard_4c_confirmed_true", record.green_guardrails)
            self.assertIn("do_not_use_round286_cases_as_candidate_generation_input", record.green_guardrails)

        summary = round286_summary()
        self.assertEqual(summary["round_id"], "round_214")
        self.assertEqual(summary["large_sector"], "MATERIALS_SPREADS_STRATEGIC_RESOURCES")
        self.assertEqual(summary["case_candidate_count"], 9)
        self.assertEqual(summary["structural_success_count"], 0)
        self.assertEqual(summary["success_candidate_count"], 3)
        self.assertEqual(summary["event_premium_count"], 2)
        self.assertEqual(summary["event_premium_or_result_count"], 3)
        self.assertEqual(summary["failed_rerating_count"], 1)
        self.assertEqual(summary["hard_4c_case_count"], 1)
        self.assertEqual(summary["hard_4c_watch_case_count"], 3)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 5)
        self.assertEqual(summary["stage4c_watch_count"], 4)
        self.assertEqual(summary["price_moved_without_evidence_count"], 2)
        self.assertEqual(summary["evidence_good_but_price_failed_count"], 1)
        self.assertEqual(summary["false_positive_score_count"], 3)
        self.assertEqual(summary["unknown_alignment_count"], 3)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])
        self.assertTrue(summary["hard_4c_confirmed"])
        self.assertTrue(summary["hard_4c_watch_confirmed"])

    def test_round286_cases_separate_event_premium_from_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND286_CASE_CANDIDATES}
        petro = by_id["r4_loop14_lotte_lgchem_petrochemical_spread_collapse"]
        restructuring = by_id["r4_loop14_lotte_hdhyundai_petrochemical_restructuring"]
        steel = by_id["r4_loop14_hyundai_posco_steel_spread_antidumping"]
        zinc = by_id["r4_loop14_korea_zinc_strategic_metal_control_premium"]
        lithium = by_id["r4_loop14_posco_minres_lithium_resource_integration"]
        squeeze = by_id["r4_loop14_posco_future_m_lnf_lithium_squeeze_rally"]
        lnf = by_id["r4_loop14_lnf_tesla_4680_cathode_contract_collapse"]
        rare = by_id["r4_loop14_rare_earth_export_control_supply_chain"]
        cathode = by_id["r4_loop14_lg_chem_cathode_supply_chain_rebalancing"]

        self.assertEqual(petro.primary_archetype, E2RArchetype.PETROCHEMICAL_SPREAD_COLLAPSE_4C)
        self.assertEqual(petro.extra_price_metrics["lotte_2024_op_loss_krw_bn"], 895)
        self.assertTrue(petro.hard_4c_watch_confirmed)
        self.assertEqual(petro.score_price_alignment, "false_positive_score")

        self.assertEqual(restructuring.primary_archetype, E2RArchetype.PETROCHEMICAL_RESTRUCTURING_STAGE2_NOT_GREEN)
        self.assertEqual(restructuring.extra_price_metrics["policy_support_krw_trn"], 2.0)
        self.assertEqual(restructuring.extra_price_metrics["shutdown_years"], 3)
        self.assertEqual(restructuring.stage_failure_type, "stage2_watch_success")

        self.assertEqual(steel.primary_archetype, E2RArchetype.STEEL_ANTI_DUMPING_EVENT_PREMIUM)
        self.assertEqual(steel.event_mfe_pct, 5.8)
        self.assertEqual(steel.score_price_alignment, "evidence_good_but_price_failed")

        self.assertEqual(zinc.primary_archetype, E2RArchetype.STRATEGIC_METAL_CONTROL_PREMIUM_4B)
        self.assertEqual(zinc.extra_price_metrics["offer_price_krw"], 660000)
        self.assertEqual(zinc.extra_price_metrics["korea_zinc_event_mfe_pct"], 19.8)
        self.assertEqual(zinc.score_price_alignment, "price_moved_without_evidence")

        self.assertEqual(lithium.primary_archetype, E2RArchetype.LITHIUM_RESOURCE_INTEGRATION_STAGE2)
        self.assertEqual(lithium.extra_price_metrics["deal_value_usd_mn"], 765)
        self.assertFalse(lithium.extra_price_metrics["processing_utilization_confirmed"])

        self.assertEqual(squeeze.primary_archetype, E2RArchetype.LITHIUM_PRICE_SQUEEZE_EVENT_PREMIUM)
        self.assertEqual(squeeze.extra_price_metrics["lnf_event_mfe_pct"], 10)
        self.assertEqual(squeeze.rerating_result, "event_premium")

        self.assertEqual(lnf.primary_archetype, E2RArchetype.BATTERY_MATERIAL_CONTRACT_COLLAPSE_HARD_4C)
        self.assertTrue(lnf.hard_4c_confirmed)
        self.assertEqual(lnf.extra_price_metrics["contract_value_collapse_pct"], -99.9997)

        self.assertEqual(rare.primary_archetype, E2RArchetype.RARE_EARTH_EXPORT_CONTROL_SUPPLY_CHAIN_4C)
        self.assertEqual(rare.extra_price_metrics["processed_rare_earth_share_pct"], 90)
        self.assertFalse(rare.extra_price_metrics["actual_exports_recovered"])

        self.assertEqual(cathode.primary_archetype, E2RArchetype.CATHODE_SUPPLY_CHAIN_REBALANCING_STAGE2)
        self.assertEqual(cathode.extra_price_metrics["huayou_stake_decline_pp"], -25)
        self.assertFalse(cathode.extra_price_metrics["binding_contract"])

    def test_green_gate_4b_4c_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND286_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND286_GREEN_FORBIDDEN_PATTERNS)
        fields = set(ROUND286_PRICE_VALIDATION_FIELDS)
        shadow_rows = {row["archetype"]: row for row in round286_shadow_weight_rows()}
        deep_rows = round286_deep_sub_archetype_rows()
        green_markdown = render_round286_green_gate_review_markdown()
        stage_markdown = render_round286_stage4b_4c_review_markdown()

        self.assertIn("spread_margin_realization_confirmed", required)
        self.assertIn("export_license_continuity_confirmed", required)
        self.assertIn("customer_calloff_visibility_confirmed", required)
        self.assertIn("CATL_license_suspension_sentiment", forbidden)
        self.assertIn("signed_contract_without_calloff", forbidden)
        self.assertIn("rare_earth_truce_without_actual_exports", forbidden)
        self.assertIn("CATL_lithium_license_headline_8pct_plus", ROUND286_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("signed_contract_value_collapse", ROUND286_HARD_4C_GATES)
        self.assertIn("export_control_anchor", fields)
        self.assertIn("Do not apply these weights to production scoring yet.", green_markdown)
        self.assertIn("Hard 4C Gates", stage_markdown)
        self.assertEqual(len(ROUND286_SHADOW_WEIGHT_ROWS), 9)
        self.assertEqual(shadow_rows["BATTERY_MATERIAL_CONTRACT_COLLAPSE_HARD_4C"]["hard_4c_sensitivity"], "+5")
        self.assertEqual(shadow_rows["LITHIUM_PRICE_SQUEEZE_EVENT_PREMIUM"]["event_penalty"], "-5")
        self.assertEqual(shadow_rows["RARE_EARTH_EXPORT_CONTROL_SUPPLY_CHAIN_4C"]["export_license_continuity"], "+5")
        self.assertTrue(any("Korea Zinc" in row["terms"] for row in deep_rows))
        self.assertTrue(any("CATL Yichun" in row["terms"] for row in deep_rows))
        self.assertTrue(any("Exxon" in row["terms"] for row in deep_rows))

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round286_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_286.md")
        self.assertEqual(audit["round_id"], "round_214")
        self.assertEqual(audit["large_sector"], ROUND286_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertTrue(audit["summary"]["hard_4c_confirmed"])
        self.assertTrue(audit["summary"]["hard_4c_watch_confirmed"])
        self.assertIn("do_not_use_round286_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round286_r4_loop14_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round286_case_rows()
            self.assertEqual(len(records), len(ROUND286_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND286_CASE_CANDIDATES))
            self.assertIn("Lotte Chemical", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("rare-earth export controls", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("spread_margin_realization", paths["score_adjustments"].read_text(encoding="utf-8"))
            self.assertIn("RARE_EARTH_EXPORT_CONTROL_SUPPLY_CHAIN_4C", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("Toyota Tsusho", paths["deep_sub_archetypes"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[0]["extra_price_metrics"])["lotte_2024_op_loss_krw_bn"], 895)


if __name__ == "__main__":
    unittest.main()
