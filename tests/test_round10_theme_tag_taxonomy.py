import tempfile
from pathlib import Path
import unittest

from e2r.sector.round10_theme_tag_taxonomy import (
    ROUND10_CASE_CANDIDATE_GROUPS,
    ROUND10_LARGE_SECTORS,
    ROUND10_THEME_ARCHETYPES,
    Round10ThemePosture,
    find_round10_theme_tag,
    render_round10_summary_markdown,
    round10_posture_counts,
    round10_theme_tag_rows,
    write_round10_theme_taxonomy_reports,
)


class Round10ThemeTagTaxonomyTests(unittest.TestCase):
    def test_round10_has_12_large_sectors_and_55_to_65_sub_archetypes(self):
        self.assertEqual(len(ROUND10_LARGE_SECTORS), 12)
        self.assertGreaterEqual(len(ROUND10_THEME_ARCHETYPES), 55)
        self.assertLessEqual(len(ROUND10_THEME_ARCHETYPES), 65)

    def test_theme_tags_cover_examples_from_round10(self):
        examples = {
            "편의점": "RETAIL_CONVENIENCE_OFFLINE",
            "손해보험": "FINANCIAL_SPREAD_BALANCE_SHEET",
            "라면": "EXPORT_RECURRING_CONSUMER",
            "HBM": "MEMORY_HBM_CAPACITY",
            "전선-케이블": "CONTRACT_BACKLOG_INDUSTRIAL",
            "초전도체": "ADVANCED_MATERIAL_THEMES",
            "엠폭스": "DIAGNOSTICS_INFECTIOUS_DISEASE",
            "스테이블코인": "DIGITAL_ASSET_TOKENIZATION",
            "야놀자 관련주": "AIRLINE_TRAVEL_CYCLE",
        }
        for tag, expected_sub_archetype in examples.items():
            rows = find_round10_theme_tag(tag)
            self.assertTrue(rows, tag)
            self.assertEqual(rows[0]["sub_archetype"], expected_sub_archetype)
            self.assertEqual(rows[0]["theme_is_score_input"], "false")

    def test_theme_tags_are_never_direct_score_inputs(self):
        for row in round10_theme_tag_rows():
            self.assertEqual(row["theme_is_score_input"], "false")

    def test_redteam_tags_stay_redteam_first(self):
        redteam_examples = {
            "초전도체": "THEME_VALUATION_OVERHEAT",
            "스테이블코인": "THEME_VALUATION_OVERHEAT",
            "엠폭스": "ONE_OFF_EVENT_DEMAND",
        }
        for tag, expected_canonical in redteam_examples.items():
            rows = find_round10_theme_tag(tag)
            self.assertEqual(rows[0]["posture"], Round10ThemePosture.REDTEAM_FIRST.value)
            self.assertEqual(rows[0]["canonical_archetype"], expected_canonical)

    def test_posture_counts_include_green_watch_and_redteam(self):
        counts = round10_posture_counts()

        self.assertGreater(counts[Round10ThemePosture.GREEN_POSSIBLE.value], 0)
        self.assertGreater(counts[Round10ThemePosture.WATCH_YELLOW_FIRST.value], 0)
        self.assertGreater(counts[Round10ThemePosture.REDTEAM_FIRST.value], 0)

    def test_case_candidate_groups_include_round10_priorities(self):
        self.assertIn("Retail/E-commerce", ROUND10_CASE_CANDIDATE_GROUPS)
        self.assertIn("Digital Finance", ROUND10_CASE_CANDIDATE_GROUPS)
        self.assertIn("stablecoin_payment_infra_candidate", ROUND10_CASE_CANDIDATE_GROUPS["Digital Finance"])

    def test_report_writer_outputs_round10_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round10_theme_taxonomy_reports(
                output_directory=Path(tmp) / "out",
                theme_map_path=Path(tmp) / "theme_tag_map.csv",
            )

            self.assertTrue(paths["theme_tag_map"].exists())
            self.assertTrue(paths["output_theme_tag_map"].exists())
            self.assertTrue(paths["summary"].exists())
            self.assertTrue(paths["large_sector_map"].exists())
            self.assertTrue(paths["sub_archetype_map"].exists())
            self.assertTrue(paths["posture_report"].exists())
            self.assertTrue(paths["case_candidate_plan"].exists())
            self.assertIn("theme_tags_are_score_input: false", paths["summary"].read_text(encoding="utf-8"))

    def test_summary_explains_theme_tag_vs_score_owner(self):
        markdown = render_round10_summary_markdown()

        self.assertIn("Theme tags are search/routing labels", markdown)
        self.assertIn("THEME_VALUATION_OVERHEAT", markdown)

    def test_production_scoring_modules_do_not_import_round10_taxonomy(self):
        paths = [
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ]
        for path in paths:
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round10_theme_tag_taxonomy", text)


if __name__ == "__main__":
    unittest.main()
