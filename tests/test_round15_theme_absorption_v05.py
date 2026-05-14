import tempfile
from pathlib import Path
import unittest

from e2r.sector.round10_theme_tag_taxonomy import Round10ThemePosture
from e2r.sector.round15_theme_absorption_v05 import (
    ROUND15_THEME_ABSORPTION_TARGETS,
    render_round15_summary_markdown,
    round15_policy_groups,
    round15_target_rows,
    round15_theme_tag_rows,
    target_for,
    write_round15_theme_absorption_reports,
)


class Round15ThemeAbsorptionV05Tests(unittest.TestCase):
    def test_round15_targets_include_missing_theme_families(self):
        labels = {target.sub_archetype for target in ROUND15_THEME_ABSORPTION_TARGETS}

        self.assertIn("WASTE_RECYCLING_ENVIRONMENT", labels)
        self.assertIn("REFINING_OIL_SPREAD", labels)
        self.assertIn("CHEMICAL_SPREAD", labels)
        self.assertIn("INSURANCE_FINANCIAL_VALUEUP", labels)
        self.assertIn("DIAGNOSTICS_INFECTIOUS_EVENT", labels)

    def test_theme_tags_are_search_routing_not_score_inputs(self):
        for row in round15_theme_tag_rows():
            self.assertEqual(row["theme_is_score_input"], "false")

    def test_waste_recycling_requires_volume_utilization_and_fcf(self):
        target = target_for("WASTE_RECYCLING_ENVIRONMENT")

        self.assertIsNotNone(target)
        assert target is not None
        self.assertEqual(target.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertIn("processing_volume", target.must_have_evidence)
        self.assertIn("utilization", target.must_have_evidence)
        self.assertIn("capex_without_fcf", target.red_flags)

    def test_chemical_spread_is_redteam_first_due_to_oversupply(self):
        target = target_for("CHEMICAL_SPREAD")

        self.assertIsNotNone(target)
        assert target is not None
        self.assertEqual(target.posture, Round10ThemePosture.REDTEAM_FIRST)
        self.assertIn("china_oversupply", target.red_flags)
        self.assertIn("petrochemical_oversupply_4c", target.counterexamples)

    def test_insurance_financial_valueup_emphasizes_valuation_and_capital_allocation(self):
        target = target_for("INSURANCE_FINANCIAL_VALUEUP")

        self.assertIsNotNone(target)
        assert target is not None
        weights = target.score_weight.as_dict()
        self.assertEqual(weights["valuation"], 25)
        self.assertEqual(weights["capital_allocation"], 10)
        self.assertIn("roe", target.must_have_evidence)
        self.assertIn("low_pbr_only", target.red_flags)

    def test_infectious_event_allows_eps_but_blocks_green_without_recurring_demand(self):
        target = target_for("DIAGNOSTICS_INFECTIOUS_EVENT")

        self.assertIsNotNone(target)
        assert target is not None
        weights = target.score_weight.as_dict()
        self.assertEqual(weights["eps_fcf"], 20)
        self.assertEqual(weights["structural_visibility"], 5)
        self.assertEqual(target.posture, Round10ThemePosture.REDTEAM_FIRST)
        self.assertIn("one_off_demand", target.red_flags)

    def test_policy_groups_include_green_watch_and_redteam(self):
        groups = round15_policy_groups()

        self.assertIn("INSURANCE_FINANCIAL_VALUEUP", groups[Round10ThemePosture.GREEN_POSSIBLE.value])
        self.assertIn("WASTE_RECYCLING_ENVIRONMENT", groups[Round10ThemePosture.WATCH_YELLOW_FIRST.value])
        self.assertIn("SPECULATIVE_SCIENCE_THEME", groups[Round10ThemePosture.REDTEAM_FIRST.value])

    def test_target_rows_mark_no_production_scoring_change(self):
        for row in round15_target_rows():
            self.assertEqual(row["production_scoring_changed"], "false")

    def test_report_writer_outputs_round15_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round15_theme_absorption_reports(
                output_directory=Path(tmp) / "out",
                score_profile_path=Path(tmp) / "score_weight_profiles_round15.csv",
                theme_map_path=Path(tmp) / "theme_tag_map_round15.csv",
            )

            self.assertTrue(paths["score_profiles"].exists())
            self.assertTrue(paths["theme_map"].exists())
            self.assertTrue(paths["summary"].exists())
            self.assertTrue(paths["target_matrix"].exists())
            self.assertTrue(paths["theme_policy"].exists())
            self.assertTrue(paths["case_candidate_plan"].exists())
            self.assertTrue(paths["next_plan"].exists())
            self.assertIn("production_scoring_changed: false", paths["summary"].read_text(encoding="utf-8"))

    def test_summary_says_evidence_not_theme_names_decide_scores(self):
        markdown = render_round15_summary_markdown()

        self.assertIn("theme_tags_are_score_input: false", markdown)
        self.assertIn("evidence fields", markdown)

    def test_production_scoring_modules_do_not_import_round15_matrix(self):
        paths = [
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ]
        for path in paths:
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round15_theme_absorption_v05", text)


if __name__ == "__main__":
    unittest.main()
