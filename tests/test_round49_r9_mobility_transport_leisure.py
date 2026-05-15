import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round49_r9_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10ThemePosture
from e2r.sector.round49_r9_mobility_transport_leisure import (
    ROUND49_CASE_CANDIDATES,
    ROUND49_SCORE_TARGETS,
    render_round49_cycle_event_cap_markdown,
    render_round49_green_guardrail_markdown,
    render_round49_price_validation_plan_markdown,
    render_round49_summary_markdown,
    round49_case_candidate_rows,
    round49_case_records,
    round49_price_field_rows,
    round49_score_profile_rows,
    round49_stage_date_rows,
    round49_summary,
    target_for,
    write_round49_r9_reports,
)


class Round49R9MobilityTransportLeisureTests(unittest.TestCase):
    def test_round49_targets_cover_r9_archetypes(self):
        labels = {target.target_id for target in ROUND49_SCORE_TARGETS}

        self.assertEqual(len(labels), 14)
        for label in (
            "AUTO_MOBILITY_COMPLETED_VEHICLE",
            "AUTO_MOBILITY_COMPONENTS",
            "TIRE_AUTO_COMPONENT_SPREAD",
            "AIRLINE_TRAVEL_CYCLE",
            "TRAVEL_LEISURE_REOPENING",
            "CASINO_DUTYFREE_TOURISM",
            "SHIPPING_FREIGHT_CYCLE",
            "LOGISTICS_PARCEL_FREIGHT",
            "RENTAL_USED_CAR_MOBILITY",
            "MOBILITY_RENTAL_MICROMOBILITY",
            "AUTO_COMPONENTS_EV_ADAS",
            "URBAN_AIR_DRONE",
            "SPACE_SUPPLYCHAIN",
            "SATELLITE_CONNECTIVITY_INFRA",
        ):
            self.assertIn(label, labels)

    def test_new_r9_canonical_archetypes_exist(self):
        expected = (
            E2RArchetype.TIRE_AUTO_COMPONENT_SPREAD,
            E2RArchetype.AIRLINE_TRAVEL_CYCLE,
            E2RArchetype.CASINO_DUTYFREE_TOURISM,
            E2RArchetype.LOGISTICS_PARCEL_FREIGHT,
            E2RArchetype.RENTAL_USED_CAR_MOBILITY,
            E2RArchetype.MOBILITY_RENTAL_MICROMOBILITY,
            E2RArchetype.AUTO_COMPONENTS_EV_ADAS,
            E2RArchetype.URBAN_AIR_DRONE,
            E2RArchetype.SPACE_SUPPLYCHAIN,
            E2RArchetype.SATELLITE_CONNECTIVITY_INFRA,
        )

        for archetype in expected:
            self.assertIsInstance(archetype.value, str)

    def test_completed_vehicle_and_satellite_are_green_possible_but_guardrailed(self):
        completed = target_for("AUTO_MOBILITY_COMPLETED_VEHICLE")
        satellite = target_for("SATELLITE_CONNECTIVITY_INFRA")

        self.assertIsNotNone(completed)
        self.assertIsNotNone(satellite)
        assert completed is not None
        assert satellite is not None
        self.assertEqual(completed.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertEqual(completed.score_weight.capital_allocation, 10)
        self.assertIn("shareholder_return", completed.green_conditions)
        self.assertIn("tariff", completed.red_flags)
        self.assertEqual(satellite.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("satellite_backlog", satellite.green_conditions)
        self.assertIn("capex_debt", satellite.red_flags)

    def test_airline_shipping_tourism_and_evtol_are_cycle_or_redteam_first(self):
        airline = target_for("AIRLINE_TRAVEL_CYCLE")
        shipping = target_for("SHIPPING_FREIGHT_CYCLE")
        tourism = target_for("CASINO_DUTYFREE_TOURISM")
        evtol = target_for("URBAN_AIR_DRONE")
        cap_text = render_round49_cycle_event_cap_markdown()

        self.assertIsNotNone(airline)
        self.assertIsNotNone(shipping)
        self.assertIsNotNone(tourism)
        self.assertIsNotNone(evtol)
        assert airline is not None
        assert shipping is not None
        assert tourism is not None
        assert evtol is not None
        self.assertEqual(airline.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertEqual(tourism.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertEqual(shipping.posture, Round10ThemePosture.REDTEAM_FIRST)
        self.assertEqual(evtol.posture, Round10ThemePosture.REDTEAM_FIRST)
        self.assertIn("policy is Stage 1", cap_text)
        self.assertIn("Part 135", cap_text)

    def test_required_round49_cases_are_present_with_stage_dates(self):
        rows = {row["case_id"]: row for row in round49_case_candidate_rows()}

        self.assertEqual(len(rows), len(ROUND49_CASE_CANDIDATES))
        self.assertEqual(rows["hyundai_hybrid_valueup_case"]["stage2_date"], "2024-08-28")
        self.assertEqual(rows["korean_air_asiana_integration_case"]["stage2_date"], "2025-02-07")
        self.assertEqual(rows["china_group_visa_tourism_case"]["case_type"], "event_premium")
        self.assertEqual(rows["maersk_overcapacity_rate_collapse_case"]["stage4c_date"], "2026-02-05")
        self.assertEqual(rows["hertz_ev_rental_failure_case"]["stage4c_date"], "2024-01-11")
        self.assertEqual(rows["joby_discounted_offering_case"]["stage4c_date"], "2025-10-08")
        self.assertEqual(rows["ses_airline_connectivity_case"]["stage2_date"], "2026-05-12")

    def test_case_records_validate_and_keep_price_backfill_open(self):
        records = round49_case_records()

        self.assertEqual(len(records), len(ROUND49_CASE_CANDIDATES))
        for record in records:
            record.validate()
            self.assertEqual(record.price_validation.price_validation_status, "needs_price_backfill")
            self.assertFalse(record.data_quality.price_data_available)
            self.assertIn("do_not_use_case_as_candidate_input", record.green_guardrails)
            self.assertIn("theme_label_is_not_score_evidence", record.green_guardrails)
            self.assertIn("demand_recovery_or_policy_headline_is_not_green_evidence_alone", record.green_guardrails)

    def test_score_profile_rows_mark_no_production_change(self):
        rows = round49_score_profile_rows()

        self.assertEqual(len(rows), len(ROUND49_SCORE_TARGETS))
        for row in rows:
            self.assertEqual(row["production_scoring_changed"], "false")
        self.assertEqual({row["target_id"]: row for row in rows}["SHIPPING_FREIGHT_CYCLE"]["posture"], "REDTEAM_FIRST")

    def test_stage_date_and_price_field_plans_are_explicit(self):
        stage_rows = {row["target_id"]: row for row in round49_stage_date_rows()}
        price_fields = {row["field"] for row in round49_price_field_rows()}

        self.assertIn("stage4c", stage_rows["URBAN_AIR_DRONE"])
        self.assertIn("type_certification_flag", price_fields)
        self.assertIn("freight_rate_index", price_fields)
        self.assertIn("casino_drop_amount", price_fields)
        self.assertIn("satellite_backlog", price_fields)

    def test_summary_and_markdown_explain_r9_guardrails(self):
        summary = round49_summary()
        summary_md = render_round49_summary_markdown()
        guardrails = render_round49_green_guardrail_markdown()
        price_plan = render_round49_price_validation_plan_markdown()

        self.assertEqual(summary["target_count"], 14)
        self.assertEqual(summary["case_candidate_count"], 13)
        self.assertEqual(summary["success_candidate_count"], 6)
        self.assertEqual(summary["cyclical_success_count"], 1)
        self.assertEqual(summary["event_premium_count"], 2)
        self.assertEqual(summary["stage4c_case_count"], 4)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertIn("production_scoring_changed: false", summary_md)
        self.assertIn("Do not apply these R9 v1.0 weights", guardrails)
        self.assertIn("unit_economics_failure", price_plan)

    def test_report_writer_outputs_cases_and_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round49_r9_reports(
                output_directory=Path(tmp) / "out",
                cases_path=Path(tmp) / "cases_r9_round49.jsonl",
                score_profile_path=Path(tmp) / "score_weight_profiles_round49_r9_v1.csv",
            )

            self.assertTrue(paths["cases"].exists())
            self.assertTrue(paths["score_profiles"].exists())
            self.assertTrue(paths["summary"].exists())
            self.assertTrue(paths["case_matrix"].exists())
            self.assertTrue(paths["stage_date_plan"].exists())
            self.assertTrue(paths["green_guardrails"].exists())
            self.assertTrue(paths["cycle_event_caps"].exists())
            self.assertTrue(paths["price_validation_plan"].exists())
            self.assertTrue(paths["price_fields"].exists())
            self.assertEqual(len(load_case_library(paths["cases"])), len(ROUND49_CASE_CANDIDATES))

    def test_cli_argument_parser_supports_paths(self):
        args = build_parser().parse_args(
            [
                "--output-directory",
                "out",
                "--cases",
                "cases.jsonl",
                "--score-profiles",
                "scores.csv",
            ]
        )

        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.score_profiles, "scores.csv")

    def test_production_scoring_modules_do_not_import_round49_pack(self):
        for path in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round49_r9_mobility_transport_leisure", text)


if __name__ == "__main__":
    unittest.main()
