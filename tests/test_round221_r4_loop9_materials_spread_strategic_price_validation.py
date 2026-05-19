from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round221_r4_loop9_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector
from e2r.sector.round221_r4_loop9_materials_spread_strategic_price_validation import (
    ROUND221_CASE_CANDIDATES,
    ROUND221_GREEN_FORBIDDEN_PATTERNS,
    ROUND221_GREEN_REQUIRED_FIELDS,
    ROUND221_HARD_4C_GATES,
    ROUND221_PRICE_VALIDATION_FIELDS,
    ROUND221_REQUIRED_TARGET_ALIASES,
    ROUND221_SHADOW_WEIGHT_ROWS,
    ROUND221_STAGE4B_WATCH_TRIGGERS,
    render_round221_green_gate_review_markdown,
    render_round221_stage4b_4c_review_markdown,
    round221_audit_payload,
    round221_case_rows,
    round221_case_records,
    round221_shadow_weight_rows,
    round221_summary,
    write_round221_r4_loop9_reports,
)


class Round221R4Loop9MaterialsSpreadStrategicPriceValidationTests(unittest.TestCase):
    def test_targets_are_existing_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertGreaterEqual(len(ROUND221_REQUIRED_TARGET_ALIASES), 14)
        self.assertTrue(set(ROUND221_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND221_REQUIRED_TARGET_ALIASES["STEEL_TARIFF_SPREAD_OVERLAY"],
            E2RArchetype.STEEL_TARIFF_EVENT_KOREA.value,
        )
        self.assertEqual(
            ROUND221_REQUIRED_TARGET_ALIASES["CRITICAL_MINERALS_US_SUPPLY_CHAIN"],
            E2RArchetype.RARE_METALS_STRATEGIC_MATERIALS.value,
        )
        self.assertEqual(
            ROUND221_REQUIRED_TARGET_ALIASES["M_AND_A_OPTIONALITY_EVENT"],
            E2RArchetype.EVENT_PREMIUM.value,
        )

    def test_case_records_validate_and_remain_calibration_only(self) -> None:
        records = round221_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, Round10LargeSector.MATERIALS_SPREAD_STRATEGIC.value)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_ohlc_complete_false", record.green_guardrails)

        summary = round221_summary()
        self.assertEqual(summary["case_candidate_count"], 7)
        self.assertEqual(summary["success_candidate_count"], 3)
        self.assertEqual(summary["cyclical_success_count"], 1)
        self.assertEqual(summary["event_premium_count"], 1)
        self.assertEqual(summary["failed_rerating_count"], 2)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["hard_4c_case_count"], 0)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_ohlc_complete"])

    def test_steel_tariff_case_is_4c_watch_not_positive_signal(self) -> None:
        case = _case("r4_loop9_posco_hyundai_steel_tariff_watch")

        self.assertEqual(case.primary_archetype, E2RArchetype.STEEL_TARIFF_EVENT_KOREA)
        self.assertEqual(case.stage4c_date.isoformat(), "2025-02-10")
        self.assertIsNone(case.stage3_date)
        self.assertFalse(case.hard_4c_confirmed)
        self.assertEqual(case.mae_1d, -3.6)
        self.assertEqual(case.mae_1d_secondary, -5.1)
        self.assertEqual(case.stage4c_price_anchor, 230500.0)
        self.assertIn("tariff_export_competitiveness_risk", case.red_flag_fields)
        self.assertEqual(case.extra_price_metrics["posco_relative_underperformance_pp"], -3.1)

    def test_korea_zinc_splits_strategic_resource_from_governance_dilution(self) -> None:
        case = _case("r4_loop9_korea_zinc_strategic_governance")

        self.assertEqual(case.primary_archetype, E2RArchetype.RARE_METALS_STRATEGIC_MATERIALS)
        self.assertIn(E2RArchetype.GOVERNANCE_DILUTION_EVENT, case.secondary_archetypes)
        self.assertEqual(case.stage2_date.isoformat(), "2025-12-15")
        self.assertEqual(case.stage4b_date.isoformat(), "2025-12-15")
        self.assertEqual(case.stage4c_date.isoformat(), "2025-12-16")
        self.assertEqual(case.mfe_1d, 27.0)
        self.assertEqual(case.mae_1d, -13.0)
        self.assertEqual(case.extra_price_metrics["share_issuance_vs_project_value_pct"], 26.2)
        self.assertEqual(case.score_price_alignment, "price_moved_without_evidence")

    def test_petrochemical_restructuring_and_refining_remain_stage2_watch(self) -> None:
        lotte = _case("r4_loop9_lotte_hd_petrochemical_restructuring")
        sk = _case("r4_loop9_sk_innovation_soil_refining_cycle")

        self.assertEqual(lotte.primary_archetype, E2RArchetype.PETROCHEMICAL_RESTRUCTURING_KOREA)
        self.assertEqual(lotte.case_type, "failed_rerating")
        self.assertEqual(lotte.stage2_date.isoformat(), "2026-02-24")
        self.assertIsNone(lotte.stage3_date)
        self.assertEqual(lotte.extra_price_metrics["support_package_krw_trn"], 2.0)
        self.assertEqual(lotte.extra_price_metrics["capital_increase_krw_trn"], 1.2)

        self.assertEqual(sk.primary_archetype, E2RArchetype.REFINING_OIL_SPREAD)
        self.assertEqual(sk.case_type, "cyclical_success")
        self.assertEqual(sk.rerating_result, "cyclical_rerating")
        self.assertEqual(sk.score_price_alignment, "aligned")
        self.assertEqual(sk.extra_price_metrics["beat_vs_lseg_estimate_pct"], 57.1)

    def test_posco_lithium_oci_and_poongsan_do_not_become_green(self) -> None:
        posco = _case("r4_loop9_posco_minres_lithium_jv")
        oci = _case("r4_loop9_oci_non_china_polysilicon")
        poongsan = _case("r4_loop9_poongsan_hanwha_mna_rumor_fade")

        self.assertEqual(posco.primary_archetype, E2RArchetype.LITHIUM_RESOURCE_SECURITY_KOREA)
        self.assertEqual(posco.extra_price_metrics["spodumene_drawdown_peak_to_low_pct"], -89.8)
        self.assertIsNone(posco.stage3_date)

        self.assertEqual(oci.primary_archetype, E2RArchetype.POLYSILICON_NON_CHINA_SUPPLY_OPTION)
        self.assertIn("spacex_contract_unconfirmed_media_report", oci.red_flag_fields)
        self.assertEqual(oci.extra_price_metrics["target_capacity_gw"], 10.0)
        self.assertIsNone(oci.stage3_date)

        self.assertEqual(poongsan.primary_archetype, E2RArchetype.COPPER_PROCESSING_PLUS_DEFENSE)
        self.assertEqual(poongsan.case_type, "event_premium")
        self.assertEqual(poongsan.stage4c_date.isoformat(), "2026-04-09")
        self.assertEqual(poongsan.extra_price_metrics["rumor_duration_days"], 6.0)
        self.assertEqual(poongsan.rerating_result, "event_premium")

    def test_green_gate_and_stage4_rules_are_explicit(self) -> None:
        required = set(ROUND221_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND221_GREEN_FORBIDDEN_PATTERNS)
        green_markdown = render_round221_green_gate_review_markdown()
        stage_review = render_round221_stage4b_4c_review_markdown()

        self.assertIn("actual_product_spread", required)
        self.assertIn("fcf_after_working_capital", required)
        self.assertIn("capex_and_dilution_risk_passed", required)
        self.assertIn("tariff_headline_only", forbidden)
        self.assertIn("mna_rumor_without_transaction", forbidden)
        self.assertIn("tariff_shock_causing_export_margin_damage", ROUND221_HARD_4C_GATES)
        self.assertIn("price_runs_before_spread_and_fcf", ROUND221_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("Do not apply these weights to production scoring yet.", green_markdown)
        self.assertIn("r4_loop9_poongsan_hanwha_mna_rumor_fade", stage_review)

    def test_shadow_weights_cover_round221_materials_targets(self) -> None:
        shadow_text = "\n".join(str(row) for row in round221_shadow_weight_rows())

        self.assertEqual(len(ROUND221_SHADOW_WEIGHT_ROWS), 8)
        self.assertIn("STEEL_TARIFF_EVENT_KOREA", shadow_text)
        self.assertIn("RARE_METALS_STRATEGIC_MATERIALS", shadow_text)
        self.assertIn("PETROCHEMICAL_RESTRUCTURING_KOREA", shadow_text)
        self.assertIn("REFINING_OIL_SPREAD", shadow_text)
        self.assertIn("LITHIUM_RESOURCE_SECURITY_KOREA", shadow_text)
        self.assertIn("POLYSILICON_NON_CHINA_SUPPLY_OPTION", shadow_text)
        self.assertIn("COPPER_PROCESSING_PLUS_DEFENSE", shadow_text)
        self.assertIn("EVENT_PREMIUM", shadow_text)

    def test_price_validation_fields_include_round221_anchor_fields(self) -> None:
        fields = set(ROUND221_PRICE_VALIDATION_FIELDS)

        self.assertIn("relative_underperformance_pp", fields)
        self.assertIn("share_issuance_vs_project_value_pct", fields)
        self.assertIn("rumor_duration_days", fields)
        self.assertIn("commodity_drawdown_pct", fields)
        self.assertIn("full_ohlc_available", fields)

    def test_summary_and_audit_payload_are_calibration_only(self) -> None:
        audit = round221_audit_payload()

        self.assertEqual(audit["source_round"], "docs/round/round_221.md")
        self.assertEqual(audit["large_sector"], Round10LargeSector.MATERIALS_SPREAD_STRATEGIC.value)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_use_round221_cases_as_candidate_generation_input", audit["what_not_to_change"])
        self.assertIn("do_not_lower_stage3_green_thresholds", audit["what_not_to_change"])

    def test_cli_parser_and_writer_outputs(self) -> None:
        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round221_r4_loop9_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round221_case_rows()
            self.assertEqual(len(records), len(ROUND221_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND221_CASE_CANDIDATES))
            self.assertIn("Korea Zinc", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("actual_product_spread", paths["score_adjustments"].read_text(encoding="utf-8"))
            self.assertIn("STEEL_TARIFF_EVENT_KOREA", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("relative_underperformance_pp", paths["price_validation_fields"].read_text(encoding="utf-8"))


def _case(case_id: str) -> object:
    return next(case for case in ROUND221_CASE_CANDIDATES if case.case_id == case_id)


if __name__ == "__main__":
    unittest.main()
