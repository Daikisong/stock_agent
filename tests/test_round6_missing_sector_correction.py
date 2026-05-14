import tempfile
from pathlib import Path
import unittest

from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import PriceValidation, load_case_library
from e2r.sector.round6_missing_sector_correction import (
    ROUND6_PRICE_PATTERN_VALUES,
    ROUND6_PRICE_VALIDATION_FIELDS,
    Round6OverlaySector,
    Round6ValidationPosture,
    render_round6_price_contract_markdown,
    round6_case_coverage,
    round6_definition,
    round6_overlay_rows,
    round6_overlays_for,
    round6_primary_overlay_for,
    write_round6_missing_sector_reports,
)


class Round6MissingSectorCorrectionTests(unittest.TestCase):
    def test_round6_has_six_overlay_sectors(self):
        self.assertEqual(len(tuple(Round6OverlaySector)), 6)
        self.assertEqual(round6_definition(Round6OverlaySector.AI_POWER_INFRA).korean_name, "AI/전력/인프라")

    def test_cross_sector_overlay_covers_ai_policy_and_theme_cases(self):
        self.assertIn(
            Round6OverlaySector.AI_POWER_INFRA,
            round6_overlays_for(E2RArchetype.AI_DATA_CENTER_INFRASTRUCTURE),
        )
        self.assertIn(
            Round6OverlaySector.NATIONAL_STRATEGY_POLICY,
            round6_overlays_for(E2RArchetype.NUCLEAR_SMR_GRID_POLICY),
        )
        self.assertEqual(
            round6_primary_overlay_for(E2RArchetype.ROBOTICS_FACTORY_AUTOMATION),
            Round6OverlaySector.THEME_TECH_EXPECTATION,
        )

    def test_overlay_postures_keep_risky_areas_guardrailed(self):
        self.assertEqual(
            round6_definition(Round6OverlaySector.RECURRING_EXPORT_BRAND).posture,
            Round6ValidationPosture.STRUCTURAL_GREEN_POSSIBLE,
        )
        self.assertEqual(
            round6_definition(Round6OverlaySector.THEME_TECH_EXPECTATION).posture,
            Round6ValidationPosture.REDTEAM_FIRST,
        )
        self.assertEqual(
            round6_definition(Round6OverlaySector.CYCLE_MACRO_CREDIT).posture,
            Round6ValidationPosture.CYCLE_OR_EVENT_CAPPED,
        )

    def test_every_archetype_has_overlay_row(self):
        rows = round6_overlay_rows()
        by_archetype = {row["archetype"]: row for row in rows}

        self.assertEqual(len(rows), len(tuple(E2RArchetype)))
        self.assertIn("price_validation_focus", by_archetype[E2RArchetype.SHIPPING_FREIGHT_CYCLE.value])

    def test_round6_price_contract_includes_mfe_mae_30d_and_2y(self):
        markdown = render_round6_price_contract_markdown()

        self.assertIn("mfe_30d", ROUND6_PRICE_VALIDATION_FIELDS)
        self.assertIn("mfe_2y", ROUND6_PRICE_VALIDATION_FIELDS)
        self.assertIn("mae_30d", ROUND6_PRICE_VALIDATION_FIELDS)
        self.assertIn("mae_2y", ROUND6_PRICE_VALIDATION_FIELDS)
        self.assertIn("cycle_boom_bust", ROUND6_PRICE_PATTERN_VALUES)
        self.assertIn("credit_relief_rally", markdown)

    def test_price_validation_parses_round6_forward_path_fields(self):
        validation = PriceValidation.from_mapping(
            {
                "mfe_30d": 12.5,
                "mfe_2y": 210,
                "mae_30d": -8,
                "mae_2y": -35,
                "price_validation_status": "price_filled",
            }
        )

        self.assertEqual(validation.mfe_30d, 12.5)
        self.assertEqual(validation.mfe_2y, 210)
        self.assertEqual(validation.mae_30d, -8)
        self.assertEqual(validation.mae_2y, -35)

    def test_case_coverage_rolls_up_to_overlays(self):
        records = load_case_library("data/e2r_case_library/cases_v02.jsonl")
        rows = round6_case_coverage(records)
        by_overlay = {row["overlay_sector"]: row for row in rows}

        self.assertGreater(by_overlay["RECURRING_EXPORT_BRAND"]["case_count"], 0)
        self.assertGreater(by_overlay["THEME_TECH_EXPECTATION"]["case_count"], 0)

    def test_report_writer_outputs_round6_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round6_missing_sector_reports(output_directory=tmp)

            self.assertTrue(paths["framework"].exists())
            self.assertTrue(paths["overlay_matrix"].exists())
            self.assertTrue(paths["price_contract"].exists())
            self.assertTrue(paths["coverage"].exists())
            self.assertTrue(paths["next_plan"].exists())
            self.assertIn("Round-6 Missing-Sector", paths["framework"].read_text(encoding="utf-8"))

    def test_production_scoring_modules_do_not_import_round6_framework(self):
        paths = [
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ]
        for path in paths:
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round6_missing_sector_correction", text)


if __name__ == "__main__":
    unittest.main()
