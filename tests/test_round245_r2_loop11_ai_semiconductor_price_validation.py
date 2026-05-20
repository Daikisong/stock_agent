from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round245_r2_loop11_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round245_r2_loop11_ai_semiconductor_price_validation import (
    ROUND245_CASE_CANDIDATES,
    ROUND245_GREEN_FORBIDDEN_PATTERNS,
    ROUND245_GREEN_REQUIRED_FIELDS,
    ROUND245_HARD_4C_GATES,
    ROUND245_LARGE_SECTOR,
    ROUND245_PRICE_VALIDATION_FIELDS,
    ROUND245_REQUIRED_TARGET_ALIASES,
    ROUND245_SCORE_ADJUSTMENTS,
    ROUND245_SHADOW_WEIGHT_ROWS,
    ROUND245_STAGE4B_WATCH_TRIGGERS,
    render_round245_green_gate_review_markdown,
    render_round245_stage4b_4c_review_markdown,
    round245_audit_payload,
    round245_case_records,
    round245_case_rows,
    round245_deep_sub_archetype_rows,
    round245_shadow_weight_rows,
    round245_summary,
    write_round245_r2_loop11_reports,
)


class Round245R2Loop11AISemiconductorPriceValidationTests(unittest.TestCase):
    def test_round245_targets_are_explicit_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND245_REQUIRED_TARGET_ALIASES), 12)
        self.assertTrue(set(ROUND245_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND245_REQUIRED_TARGET_ALIASES["MEMORY_HBM_CAPACITY_LEADER"],
            E2RArchetype.MEMORY_HBM_CAPACITY_LEADER.value,
        )
        self.assertEqual(
            ROUND245_REQUIRED_TARGET_ALIASES["HBM_BONDER_EQUIPMENT"],
            E2RArchetype.HBM_BONDER_EQUIPMENT.value,
        )
        self.assertEqual(
            ROUND245_REQUIRED_TARGET_ALIASES["CHINA_CXMT_EQUIPMENT_SUPPLIER_RELIEF"],
            E2RArchetype.CHINA_CXMT_EQUIPMENT_SUPPLIER_RELIEF.value,
        )
        self.assertEqual(
            ROUND245_REQUIRED_TARGET_ALIASES["SEMICONDUCTOR_IP_LEAK_REDTEAM"],
            E2RArchetype.SEMICONDUCTOR_IP_LEAK_REDTEAM.value,
        )

    def test_round245_archetype_definitions_are_available(self) -> None:
        leader = archetype_definition(E2RArchetype.MEMORY_HBM_CAPACITY_LEADER)
        capex = archetype_definition(E2RArchetype.HBM_EUV_ADVANCED_PACKAGING_CAPEX)
        catchup = archetype_definition(E2RArchetype.HBM_CATCHUP_EXECUTION)
        bonder = archetype_definition(E2RArchetype.HBM_BONDER_EQUIPMENT)
        cxmt = archetype_definition(E2RArchetype.CHINA_CXMT_EQUIPMENT_SUPPLIER_RELIEF)
        ip = archetype_definition(E2RArchetype.SEMICONDUCTOR_IP_LEAK_REDTEAM)

        self.assertIn("HBM generation leadership", leader.stage3_high_conviction_signals)
        self.assertIn("capex headline without HBM revenue bridge", capex.false_positive_patterns)
        self.assertIn("labor disruption", catchup.stage4c_thesis_break_signals)
        self.assertIn("media report treated as contract", bonder.false_positive_patterns)
        self.assertIn("authorization loss", cxmt.stage4c_thesis_break_signals)
        self.assertIn("confirmed IP leakage", ip.stage4c_thesis_break_signals)

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round245_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND245_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_ohlc_complete_false", record.green_guardrails)

        summary = round245_summary()
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["structural_success_count"], 1)
        self.assertEqual(summary["success_candidate_count"], 3)
        self.assertEqual(summary["event_premium_count"], 3)
        self.assertEqual(summary["failed_rerating_count"], 1)
        self.assertEqual(summary["hard_4c_case_count"], 0)
        self.assertEqual(summary["stage3_case_count"], 1)
        self.assertEqual(summary["stage4b_watch_count"], 7)
        self.assertEqual(summary["price_moved_without_evidence_count"], 3)
        self.assertEqual(summary["evidence_good_but_price_failed_count"], 2)
        self.assertEqual(summary["target_archetype_count"], 12)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])

    def test_sk_hynix_and_samsung_cases_are_separated(self) -> None:
        by_id = {case.case_id: case for case in ROUND245_CASE_CANDIDATES}
        skh = by_id["r2_loop11_sk_hynix_euv_packaging_4b"]
        samsung = by_id["r2_loop11_samsung_hbm_foundry_strike_export_ip_watch"]

        self.assertEqual(skh.primary_archetype, E2RArchetype.MEMORY_HBM_CAPACITY_LEADER)
        self.assertEqual(skh.stage3_date.isoformat(), "2024-06-25")
        self.assertEqual(skh.stage3_price_anchor, 222000.0)
        self.assertEqual(skh.extra_price_metrics["asml_euv_order_krw_trn"], 11.95)
        self.assertEqual(skh.extra_price_metrics["advanced_packaging_investment_krw_trn"], 19.0)
        self.assertEqual(skh.extra_price_metrics["minimum_compounded_return_from_2025_start_pct"], 1022.0)
        self.assertEqual(skh.stage_failure_type, "green_success")
        self.assertIn("market_cap_milestone_headline", skh.red_flag_fields)

        self.assertEqual(samsung.primary_archetype, E2RArchetype.HBM_CATCHUP_EXECUTION)
        self.assertEqual(samsung.stage2_date.isoformat(), "2025-07-28")
        self.assertIsNone(samsung.stage3_date)
        self.assertEqual(samsung.stage4c_date.isoformat(), "2025-09-01")
        self.assertEqual(samsung.extra_price_metrics["foundry_contract_usd_bn"], 16.5)
        self.assertEqual(samsung.extra_price_metrics["strike_event_mae_pct"], -9.3)
        self.assertEqual(samsung.score_price_alignment, "evidence_good_but_price_failed")
        self.assertIn("ip_leak_watch", samsung.red_flag_fields)

    def test_hanmi_cxmt_gaonchips_and_policy_cases_are_not_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND245_CASE_CANDIDATES}
        hanmi = by_id["r2_loop11_hanmi_hbm_bonder_confirmed_order_rumor_4b"]
        cxmt = by_id["r2_loop11_jusung_mirae_cxmt_supplier_relief"]
        gaon = by_id["r2_loop11_gaonchips_pfn_design_win"]
        db = by_id["r2_loop11_db_hitek_policy_foundry"]

        self.assertEqual(hanmi.primary_archetype, E2RArchetype.HBM_BONDER_EQUIPMENT)
        self.assertEqual(hanmi.stage4b_date.isoformat(), "2024-03-28")
        self.assertEqual(hanmi.stage4b_price_anchor, 139100.0)
        self.assertEqual(hanmi.extra_price_metrics["stage4b_event_mfe_pct"], 22.0)
        self.assertIn("micron_unconfirmed_media_report", hanmi.red_flag_fields)

        self.assertEqual(cxmt.primary_archetype, E2RArchetype.CHINA_CXMT_EQUIPMENT_SUPPLIER_RELIEF)
        self.assertEqual(cxmt.stage2_date.isoformat(), "2024-12-03")
        self.assertEqual(cxmt.extra_price_metrics["mirae_cxmt_revenue_share_1h2024_pct"], 15.0)
        self.assertEqual(cxmt.score_price_alignment, "price_moved_without_evidence")
        self.assertIn("export_control_uncertainty", cxmt.red_flag_fields)

        self.assertEqual(gaon.primary_archetype, E2RArchetype.SYSTEM_SEMI_DESIGN_HOUSE_AI_ORDER)
        self.assertEqual(gaon.stage2_date.isoformat(), "2024-07-09")
        self.assertEqual(gaon.extra_price_metrics["order_size"], "not_disclosed")
        self.assertEqual(gaon.round_stage_failure_label, "stage2_evidence_not_green")

        self.assertEqual(db.primary_archetype, E2RArchetype.POLICY_FOUNDRY_EVENT)
        self.assertEqual(db.stage1_date.isoformat(), "2025-12-10")
        self.assertEqual(db.extra_price_metrics["defense_semiconductor_import_dependency_pct"], 99.0)
        self.assertIn("policy_foundry_without_order", db.red_flag_fields)
        self.assertEqual(db.stage_failure_type, "false_yellow")

    def test_spinoff_and_export_ip_redteam_cases_are_explicit(self) -> None:
        by_id = {case.case_id: case for case in ROUND245_CASE_CANDIDATES}
        spinoff = by_id["r2_loop11_hanwha_precision_hbm_equipment_spinoff"]
        redteam = by_id["r2_loop11_export_control_ip_leak_redteam"]

        self.assertEqual(spinoff.primary_archetype, E2RArchetype.SEMICONDUCTOR_EQUIPMENT_SPINOFF_OPTIONALITY)
        self.assertEqual(spinoff.stage4b_date.isoformat(), "2024-04-05")
        self.assertEqual(spinoff.mfe_1d, 15.0)
        self.assertEqual(spinoff.mae_1d, -8.0)
        self.assertEqual(spinoff.extra_price_metrics["estimated_sum_vs_parent_market_cap_pct"], 9.1)
        self.assertEqual(spinoff.score_price_alignment, "price_moved_without_evidence")

        self.assertEqual(redteam.primary_archetype, E2RArchetype.GEOPOLITICAL_EXPORT_CONTROL_OVERLAY)
        self.assertEqual(redteam.stage4c_date.isoformat(), "2025-09-01")
        self.assertFalse(redteam.hard_4c_confirmed)
        self.assertEqual(redteam.extra_price_metrics["sk_hynix_mae_1d_pct"], -4.4)
        self.assertEqual(redteam.extra_price_metrics["authorization_effective_delay_days"], 120)
        self.assertEqual(redteam.rerating_result, "thesis_break")
        self.assertEqual(redteam.round_stage_failure_label, "4C_watch_not_hard_4C")
        self.assertIn("ip_leakage_china_competitive_catchup", redteam.red_flag_fields)

    def test_green_gate_4b_4c_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND245_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND245_GREEN_FORBIDDEN_PATTERNS)
        review = render_round245_green_gate_review_markdown()
        stage_review = render_round245_stage4b_4c_review_markdown()
        fields = set(ROUND245_PRICE_VALIDATION_FIELDS)
        axes = {item.axis for item in ROUND245_SCORE_ADJUSTMENTS}
        shadow_rows = {row["archetype"]: row for row in round245_shadow_weight_rows()}
        deep_rows = round245_deep_sub_archetype_rows()

        self.assertIn("company_level_customer_evidence", required)
        self.assertIn("eps_fcf_revision", required)
        self.assertIn("unconfirmed_customer_report", forbidden)
        self.assertIn("policy_foundry_without_order", forbidden)
        self.assertIn("market_cap_milestone_headline", ROUND245_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("ip_leakage_china_competitive_catchup", ROUND245_HARD_4C_GATES)
        self.assertIn("market_share_anchor", fields)
        self.assertIn("confirmed_customer_order", axes)
        self.assertIn("Do not apply these weights to production scoring yet.", review)
        self.assertIn("hard 4C needs confirmed production", stage_review)
        self.assertEqual(len(ROUND245_SHADOW_WEIGHT_ROWS), 9)
        self.assertEqual(shadow_rows["MEMORY_HBM_CAPACITY_LEADER"]["confirmed_order"], "+5")
        self.assertEqual(shadow_rows["POLICY_FOUNDRY_EVENT"]["event_penalty"], "-5")
        self.assertEqual(shadow_rows["GEOPOLITICAL_EXPORT_CONTROL_OVERLAY"]["hard_4c_sensitivity"], "+5")
        self.assertTrue(any("SK Hynix" in row["terms"] for row in deep_rows))
        self.assertTrue(any("Hanmi Semiconductor" in row["terms"] for row in deep_rows))
        self.assertTrue(any("CXMT" in row["terms"] for row in deep_rows))

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round245_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_245.md")
        self.assertEqual(audit["round_id"], "round_173")
        self.assertEqual(audit["large_sector"], ROUND245_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_use_round245_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round245_r2_loop11_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round245_case_rows()
            self.assertEqual(len(records), len(ROUND245_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND245_CASE_CANDIDATES))
            self.assertIn("SK Hynix", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("unconfirmed_customer_report", paths["green_gate_review"].read_text(encoding="utf-8"))
            self.assertIn("GEOPOLITICAL_EXPORT_CONTROL_OVERLAY", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("Preferred Networks", paths["deep_sub_archetypes"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[0]["extra_price_metrics"])["market_cap_mfe_minimum_pct"], 842.0)


if __name__ == "__main__":
    unittest.main()
