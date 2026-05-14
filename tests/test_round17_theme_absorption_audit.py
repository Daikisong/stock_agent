import tempfile
from pathlib import Path
import unittest

from e2r.cli.audit_round17_theme_coverage import build_parser
from e2r.sector.round17_theme_absorption_audit import (
    parse_round17_theme_expectations,
    render_round17_theme_coverage_report,
    round17_coverage_summary,
    round17_theme_audit_records,
    round17_theme_map_rows,
    round17_unmatched_theme_rows,
    write_round17_theme_absorption_reports,
)


class Round17ThemeAbsorptionAuditTests(unittest.TestCase):
    def test_round17_parses_theme_table_and_maps_all_rows(self):
        expectations = parse_round17_theme_expectations()
        summary = round17_coverage_summary()

        self.assertGreaterEqual(len(expectations), 150)
        self.assertEqual(summary["large_sector_count"], 12)
        self.assertGreaterEqual(summary["archetype_count"], 70)
        self.assertEqual(summary["total_theme_tags"], summary["mapped_theme_tags"])
        self.assertEqual(summary["unmatched_theme_tags"], 0)

    def test_key_round17_theme_tags_have_expected_policy_and_archetype(self):
        rows = {row["theme_tag"]: row for row in round17_theme_map_rows()}

        self.assertEqual(rows["초전도체"]["primary_archetype"], "SPECULATIVE_SCIENCE_THEME")
        self.assertEqual(rows["초전도체"]["green_policy"], "red_flag")
        self.assertEqual(rows["전력설비"]["primary_archetype"], "CONTRACT_BACKLOG_INDUSTRIAL")
        self.assertEqual(rows["전력설비"]["green_policy"], "green_allowed")
        self.assertEqual(rows["스테이블코인"]["primary_archetype"], "DIGITAL_ASSET_TOKENIZATION")
        self.assertEqual(rows["스테이블코인"]["green_policy"], "watch_only")
        self.assertEqual(rows["마켓컬리·오아시스"]["primary_archetype"], "ECOMMERCE_FRESH_LOGISTICS")

    def test_theme_tags_are_routing_not_score_inputs(self):
        for row in round17_theme_map_rows():
            self.assertEqual(row["theme_is_score_input"], "false")
            self.assertEqual(row["production_scoring_changed"], "false")

    def test_supplemental_profiles_cover_cro_and_regulated_consumer(self):
        records = {record.theme_tag: record for record in round17_theme_audit_records()}

        self.assertEqual(records["CRO"].mapped_via, "round17_supplemental")
        self.assertEqual(records["CRO"].canonical_archetype, "CDMO_HEALTHCARE_CONTRACT")
        self.assertEqual(records["전자담배"].mapped_via, "round17_supplemental")
        self.assertEqual(records["전자담배"].canonical_archetype, "RETAIL_DOMESTIC_CONSUMER")

    def test_report_writer_outputs_audit_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round17_theme_absorption_reports(
                output_directory=Path(tmp) / "out",
                theme_map_path=Path(tmp) / "theme_tag_map_v05.csv",
                alias_path=Path(tmp) / "theme_aliases_round17.yml",
            )

            self.assertTrue(paths["theme_map"].exists())
            self.assertTrue(paths["aliases"].exists())
            self.assertTrue(paths["summary_json"].exists())
            self.assertTrue(paths["summary_md"].exists())
            self.assertTrue(paths["coverage_matrix"].exists())
            self.assertTrue(paths["unmatched"].exists())
            self.assertTrue(paths["green_policy_distribution"].exists())
            self.assertIn("unmatched_theme_tags: 0", paths["summary_md"].read_text(encoding="utf-8"))

    def test_summary_says_scoring_is_not_ready_or_changed(self):
        summary = round17_coverage_summary()
        markdown = render_round17_theme_coverage_report()

        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["theme_tags_are_score_input"])
        self.assertFalse(summary["scoring_ready"])
        self.assertIn("Raw theme tags are search/routing tags", markdown)

    def test_unmatched_rows_are_empty_for_round17_table(self):
        self.assertEqual(round17_unmatched_theme_rows(), ())

    def test_cli_argument_parser_supports_output_paths(self):
        args = build_parser().parse_args(
            [
                "--round-doc",
                "docs/round/round_17.md",
                "--output-directory",
                "out",
                "--theme-map",
                "theme.csv",
                "--aliases",
                "aliases.yml",
            ]
        )

        self.assertEqual(args.round_doc, "docs/round/round_17.md")
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.theme_map, "theme.csv")
        self.assertEqual(args.aliases, "aliases.yml")

    def test_production_scoring_modules_do_not_import_round17_audit(self):
        paths = [
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ]
        for path in paths:
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round17_theme_absorption_audit", text)


if __name__ == "__main__":
    unittest.main()
