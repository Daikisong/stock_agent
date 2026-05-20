from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round265_r9_loop12_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector
from e2r.sector.round265_r9_loop12_mobility_transport_leisure_price_validation import (
    ROUND265_CASE_CANDIDATES,
    ROUND265_DEEP_SUB_ARCHETYPES,
    ROUND265_GREEN_FORBIDDEN_PATTERNS,
    ROUND265_GREEN_REQUIRED_FIELDS,
    ROUND265_HARD_4C_GATES,
    ROUND265_LARGE_SECTOR,
    ROUND265_PRICE_VALIDATION_FIELDS,
    ROUND265_REQUIRED_TARGET_ALIASES,
    ROUND265_SCORE_ADJUSTMENTS,
    ROUND265_SHADOW_WEIGHT_ROWS,
    ROUND265_STAGE4B_WATCH_TRIGGERS,
    render_round265_green_gate_review_markdown,
    render_round265_stage4b_4c_review_markdown,
    round265_audit_payload,
    round265_case_records,
    round265_case_rows,
    round265_deep_sub_archetype_rows,
    round265_shadow_weight_rows,
    round265_summary,
    write_round265_r9_loop12_reports,
)


class Round265R9Loop12MobilityTransportLeisurePriceValidationTests(unittest.TestCase):
    def test_targets_are_explicit_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND265_REQUIRED_TARGET_ALIASES), 8)
        self.assertTrue(set(ROUND265_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND265_REQUIRED_TARGET_ALIASES["AVIATION_SAFETY_HARD_4C"],
            E2RArchetype.AVIATION_SAFETY_HARD_4C.value,
        )
        self.assertEqual(
            ROUND265_REQUIRED_TARGET_ALIASES["LCC_ROUTE_REMEDY_LONG_HAUL_OPTION"],
            E2RArchetype.LCC_ROUTE_REMEDY_LONG_HAUL_OPTION.value,
        )
        self.assertEqual(
            ROUND265_REQUIRED_TARGET_ALIASES["AUTO_COMPONENT_HYBRID_EREV_ASP"],
            E2RArchetype.AUTO_COMPONENT_HYBRID_EREV_ASP.value,
        )
        self.assertEqual(
            ROUND265_REQUIRED_TARGET_ALIASES["SHIPPING_FREIGHT_NORMALIZATION_4C"],
            E2RArchetype.SHIPPING_FREIGHT_NORMALIZATION_4C.value,
        )
        self.assertEqual(
            ROUND265_REQUIRED_TARGET_ALIASES["TRAVEL_CASINO_DEMAND_CONVERSION"],
            E2RArchetype.TRAVEL_CASINO_DEMAND_CONVERSION.value,
        )

    def test_archetype_definitions_capture_round265_gates(self) -> None:
        aviation = archetype_definition(E2RArchetype.AVIATION_SAFETY_HARD_4C)
        lcc = archetype_definition(E2RArchetype.LCC_ROUTE_REMEDY_LONG_HAUL_OPTION)
        component = archetype_definition(E2RArchetype.AUTO_COMPONENT_HYBRID_EREV_ASP)
        restructure = archetype_definition(E2RArchetype.AUTO_PARTS_PORTFOLIO_RESTRUCTURING)
        shipping_security = archetype_definition(E2RArchetype.SHIPPING_GEOPOLITICAL_SECURITY_4C)
        freight_norm = archetype_definition(E2RArchetype.SHIPPING_FREIGHT_NORMALIZATION_4C)
        casino = archetype_definition(E2RArchetype.TRAVEL_CASINO_DEMAND_CONVERSION)

        self.assertIn("fatal aviation accident", aviation.stage4c_thesis_break_signals)
        self.assertIn("route yield", lcc.stage3_high_conviction_signals)
        self.assertIn("component take-rate", component.stage3_high_conviction_signals)
        self.assertIn("transaction value", restructure.stage3_high_conviction_signals)
        self.assertIn("shipping vessel attack", shipping_security.stage4c_thesis_break_signals)
        self.assertIn("EBITDA guidance collapse", freight_norm.stage4c_thesis_break_signals)
        self.assertIn("tourism spend conversion", casino.stage3_high_conviction_signals)

    def test_case_records_validate_and_keep_calibration_guardrails(self) -> None:
        records = round265_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, Round10LargeSector.MOBILITY_TRANSPORT_LEISURE.value)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn(
                "do_not_treat_route_rights_tourist_arrivals_freight_spike_divestiture_or_component_asp_as_green",
                record.green_guardrails,
            )

        summary = round265_summary()
        self.assertEqual(summary["analyst_round_id"], "round_193")
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["success_candidate_count"], 3)
        self.assertEqual(summary["cyclical_success_count"], 1)
        self.assertEqual(summary["event_premium_count"], 1)
        self.assertEqual(summary["hard_4c_case_count"], 1)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 5)
        self.assertEqual(summary["stage4c_watch_count"], 3)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertTrue(summary["shadow_weight_only"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["hard_4c_confirmed"])

    def test_aviation_and_shipping_cases_feed_4c_redteam(self) -> None:
        by_id = {case.case_id: case for case in ROUND265_CASE_CANDIDATES}
        jeju = by_id["r9_loop12_jeju_air_muan_crash_hard_4c"]
        air_busan = by_id["r9_loop12_air_busan_plane_fire_4c_watch"]
        hmm_security = by_id["r9_loop12_hmm_namu_hormuz_shipping_security"]
        shipping_cycle = by_id["r9_loop12_hmm_panocean_freight_normalization_watch"]

        self.assertEqual(jeju.primary_archetype, E2RArchetype.AVIATION_SAFETY_HARD_4C)
        self.assertTrue(jeju.hard_4c_confirmed)
        self.assertEqual(jeju.stage4c_date.isoformat(), "2024-12-30")
        self.assertEqual(jeju.mae_1d, -15.7)
        self.assertEqual(jeju.extra_price_metrics["event_low_price_krw"], 6920.0)
        self.assertEqual(jeju.extra_price_metrics["fatalities"], 179.0)
        self.assertEqual(jeju.rerating_result, "thesis_break")

        self.assertEqual(air_busan.primary_archetype, E2RArchetype.AVIATION_SAFETY_HARD_4C)
        self.assertFalse(air_busan.hard_4c_confirmed)
        self.assertEqual(air_busan.stage4c_date.isoformat(), "2025-01-31")
        self.assertEqual(air_busan.mae_1d, -6.1)
        self.assertEqual(air_busan.extra_price_metrics["tway_same_context_pct"], 9.0)
        self.assertIn("fatality_not_confirmed_so_not_hard_4c", air_busan.red_flag_fields)

        self.assertEqual(hmm_security.primary_archetype, E2RArchetype.SHIPPING_GEOPOLITICAL_SECURITY_4C)
        self.assertEqual(hmm_security.round_score_price_alignment, "thesis_break_watch")
        self.assertIn("shipping_vessel_attack", hmm_security.red_flag_fields)
        self.assertEqual(hmm_security.price_validation_status, "price_data_unavailable_after_deep_search")

        self.assertEqual(shipping_cycle.primary_archetype, E2RArchetype.SHIPPING_FREIGHT_NORMALIZATION_4C)
        self.assertEqual(shipping_cycle.case_type, "cyclical_success")
        self.assertEqual(shipping_cycle.mae_1d, -5.5)
        self.assertEqual(shipping_cycle.extra_price_metrics["maersk_2026_ebitda_decline_low_end_pct"], -52.8)
        self.assertEqual(shipping_cycle.extra_price_metrics["hapag_ebit_decline_pct"], -60.7)

    def test_route_component_restructuring_and_tourism_cases_are_stage2_or_event_not_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND265_CASE_CANDIDATES}
        tway = by_id["r9_loop12_tway_eu_route_remedy"]
        mando = by_id["r9_loop12_hl_mando_hybrid_erev_component_asp"]
        mobis = by_id["r9_loop12_hyundai_mobis_lighting_divestiture"]
        tourism = by_id["r9_loop12_lotte_yellowballoon_tourism_redirect"]

        self.assertEqual(tway.primary_archetype, E2RArchetype.LCC_ROUTE_REMEDY_LONG_HAUL_OPTION)
        self.assertEqual(tway.stage2_date.isoformat(), "2024-03-07")
        self.assertEqual(tway.extra_price_metrics["aircraft_support_a330_200"], 5.0)
        self.assertEqual(tway.extra_price_metrics["pilot_support"], 100.0)
        self.assertIn("load_factor_unverified", tway.red_flag_fields)

        self.assertEqual(mando.primary_archetype, E2RArchetype.AUTO_COMPONENT_HYBRID_EREV_ASP)
        self.assertEqual(mando.stage2_price_anchor, 49600.0)
        self.assertEqual(mando.mfe_1d, 11.0)
        self.assertEqual(mando.extra_price_metrics["idb_asp_premium_pct"], 70.0)
        self.assertEqual(mando.extra_price_metrics["target_upside_from_event_price_pct"], 16.9)
        self.assertEqual(mando.score_price_alignment, "aligned")

        self.assertEqual(mobis.primary_archetype, E2RArchetype.AUTO_PARTS_PORTFOLIO_RESTRUCTURING)
        self.assertEqual(mobis.stage2_date.isoformat(), "2026-01-27")
        self.assertEqual(mobis.extra_price_metrics["hyundai_mobis_lighting_revenue_estimate_eur_bn"], 1.0)
        self.assertEqual(mobis.extra_price_metrics["opmobility_margin_improvement_pp"], 0.6)
        self.assertIn("transaction_value_unverified", mobis.red_flag_fields)

        self.assertEqual(tourism.primary_archetype, E2RArchetype.TOURISM_REDIRECT_EVENT_PREMIUM)
        self.assertIn(E2RArchetype.TRAVEL_CASINO_DEMAND_CONVERSION, tourism.secondary_archetypes)
        self.assertEqual(tourism.mfe_1d, 24.0)
        self.assertEqual(tourism.extra_price_metrics["jeju_stay_extension_high_pct"], 533.3)
        self.assertEqual(tourism.score_price_alignment, "price_moved_without_evidence")

    def test_green_gate_4b_4c_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND265_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND265_GREEN_FORBIDDEN_PATTERNS)
        fields = set(ROUND265_PRICE_VALIDATION_FIELDS)
        axes = {item.axis for item in ROUND265_SCORE_ADJUSTMENTS}
        shadow_rows = {row["archetype"]: row for row in round265_shadow_weight_rows()}
        deep_rows = round265_deep_sub_archetype_rows()
        green_markdown = render_round265_green_gate_review_markdown()
        stage_markdown = render_round265_stage4b_4c_review_markdown()

        self.assertIn("route_yield_confirmed", required)
        self.assertIn("tourism_spend_hotel_occupancy_casino_drop_adr_confirmed", required)
        self.assertIn("route_rights_only", forbidden)
        self.assertIn("freight_spike_only", forbidden)
        self.assertIn("route_remedy_headline_lcc_spike", ROUND265_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("fatal_aviation_accident", ROUND265_HARD_4C_GATES)
        self.assertIn("shipping_vessel_attack", ROUND265_HARD_4C_GATES)
        self.assertIn("component_asp_or_transaction_anchor", fields)
        self.assertIn("safety_trust", axes)
        self.assertIn("shipping_security_event", axes)
        self.assertIn("Do not apply these weights to production scoring yet.", green_markdown)
        self.assertIn("route rights", green_markdown)
        self.assertIn("r9_loop12_jeju_air_muan_crash_hard_4c", stage_markdown)
        self.assertEqual(len(ROUND265_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["AVIATION_SAFETY_HARD_4C"]["hard_4c_sensitivity"], "+5")
        self.assertEqual(shadow_rows["LCC_ROUTE_REMEDY_LONG_HAUL_OPTION"]["route_yield"], "+5")
        self.assertEqual(shadow_rows["TOURISM_REDIRECT_EVENT_PREMIUM"]["event_penalty"], "-5")
        self.assertTrue(any("T'way" in row["deep_sub_archetype"] for row in deep_rows))
        self.assertIn("Jeju Air Muan crash / aviation safety trust hard 4C", ROUND265_DEEP_SUB_ARCHETYPES)

    def test_audit_payload_cli_and_writer_outputs(self) -> None:
        audit = round265_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_265.md")
        self.assertEqual(audit["analyst_round_id"], "round_193")
        self.assertEqual(audit["large_sector"], ROUND265_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertTrue(audit["summary"]["hard_4c_confirmed"])
        self.assertIn("do_not_use_round265_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round265_r9_loop12_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round265_case_rows()
            self.assertEqual(len(records), len(ROUND265_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND265_CASE_CANDIDATES))
            self.assertIn("Jeju Air is direct hard 4C", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("route_yield", paths["score_adjustments"].read_text(encoding="utf-8"))
            self.assertIn("AVIATION_SAFETY_HARD_4C", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("fatal_aviation_accident", paths["stage4b_4c_review"].read_text(encoding="utf-8"))
            self.assertEqual(rows[0]["round_case_type"], "hard_4c_aviation_safety_trust_break")
            self.assertEqual(json.loads(rows[3]["extra_price_metrics"])["event_price_krw"], 49600.0)

    def test_production_modules_do_not_import_round265(self) -> None:
        forbidden = "round265_r9_loop12_mobility_transport_leisure_price_validation"
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
