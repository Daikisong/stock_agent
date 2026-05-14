import tempfile
from pathlib import Path
import unittest

from e2r.sector.round10_theme_tag_taxonomy import Round10ThemePosture
from e2r.sector.round12_theme_refinement import (
    ROUND12_REFINEMENTS,
    find_round12_theme_tag,
    render_round12_schema_markdown,
    round12_case_candidate_rows,
    round12_refinement_rows,
    write_round12_theme_refinement_reports,
)


class Round12ThemeRefinementTests(unittest.TestCase):
    def test_round12_confirms_18_refined_sub_archetypes(self):
        self.assertEqual(len(ROUND12_REFINEMENTS), 18)

    def test_round12_maps_key_theme_tags_to_refined_sub_archetypes(self):
        expected = {
            "편의점": "RETAIL_CONVENIENCE_OFFLINE",
            "손해보험": "INSURANCE_UNDERWRITING_CYCLE",
            "스테이블코인": "DIGITAL_ASSET_TOKENIZATION",
            "태양광": "SOLAR_TARIFF_SUPPLYCHAIN",
            "타이어": "TIRE_AUTO_COMPONENT_SPREAD",
            "화장품 OEM": "BEAUTY_OEM_ODM_SUPPLYCHAIN",
            "엠폭스": "EVENT_DISEASE_PEST_DEMAND",
            "초전도체": "SPECULATIVE_SCIENCE_THEME",
            "건자재": "BUILDING_MATERIALS_CYCLE",
        }
        for tag, sub_archetype in expected.items():
            rows = find_round12_theme_tag(tag)
            self.assertTrue(rows, tag)
            self.assertEqual(rows[0]["primary_archetype"], sub_archetype)
            self.assertEqual(rows[0]["theme_is_score_input"], "false")

    def test_redteam_first_tags_are_not_score_inputs(self):
        for tag in ("스테이블코인", "엠폭스", "초전도체"):
            row = find_round12_theme_tag(tag)[0]
            self.assertEqual(row["posture"], Round10ThemePosture.REDTEAM_FIRST.value)
            self.assertEqual(row["theme_is_score_input"], "false")

    def test_schema_contains_round12_required_fields(self):
        markdown = render_round12_schema_markdown()
        rows = round12_refinement_rows()
        first = rows[0]

        for field in (
            "theme_tag",
            "large_sector",
            "primary_archetype",
            "secondary_archetypes",
            "green_policy",
            "stage1_query_terms",
            "must_have_evidence",
            "red_flag_evidence",
            "score_weight_profile",
        ):
            self.assertIn(field, first)
            self.assertIn(field, markdown)

    def test_case_candidate_plan_contains_fintech_and_disease_cases(self):
        rows = round12_case_candidate_rows()
        ids = {row["case_id"] for row in rows}

        self.assertIn("stablecoin_payment_infra_candidate", ids)
        self.assertIn("infectious_disease_oneoff_counterexample", ids)

    def test_report_writer_outputs_round12_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round12_theme_refinement_reports(
                output_directory=Path(tmp) / "out",
                theme_map_path=Path(tmp) / "theme_tag_map_round12.csv",
            )

            self.assertTrue(paths["theme_map"].exists())
            self.assertTrue(paths["summary"].exists())
            self.assertTrue(paths["sub_archetype_refinements"].exists())
            self.assertTrue(paths["case_candidate_plan"].exists())
            self.assertTrue(paths["schema"].exists())
            self.assertTrue(paths["next_plan"].exists())
            self.assertIn("production_scoring_changed: false", paths["summary"].read_text(encoding="utf-8"))

    def test_production_scoring_modules_do_not_import_round12_refinement(self):
        paths = [
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ]
        for path in paths:
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round12_theme_refinement", text)


if __name__ == "__main__":
    unittest.main()
