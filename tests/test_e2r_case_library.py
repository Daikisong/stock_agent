from pathlib import Path
import tempfile
import unittest

from e2r.cli.mine_e2r_sector_cases import main as mine_cases_main
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import (
    CaseDataQuality,
    E2RCaseRecord,
    PriceValidation,
    coverage_by_archetype,
    load_case_library,
    write_case_coverage_outputs,
)
from e2r.sector.taxonomy import SectorTaxonomyRow, write_sector_taxonomy


class E2RCaseLibraryTests(unittest.TestCase):
    def test_case_library_record_validates_required_fields(self):
        record = E2RCaseRecord.from_mapping(
            {
                "case_id": "test_case",
                "symbol": "000001",
                "company_name": "테스트",
                "market": "KR",
                "sector_raw": "전력기기",
                "primary_archetype": "CONTRACT_BACKLOG_INDUSTRIAL",
                "expected_group": "structural_success",
                "key_evidence_fields": ["backlog"],
                "data_quality": {
                    "official_data_available": True,
                    "report_data_available": False,
                    "price_data_available": True,
                    "stage_dates_confidence": 0.5,
                },
            }
        )

        record.validate()
        self.assertEqual(record.primary_archetype, E2RArchetype.CONTRACT_BACKLOG_INDUSTRIAL)

    def test_case_library_ignores_non_finite_numeric_fields(self):
        quality = CaseDataQuality.from_mapping(
            {
                "official_data_available": True,
                "report_data_available": True,
                "price_data_available": True,
                "stage_dates_confidence": "nan",
            }
        )
        validation = PriceValidation.from_mapping(
            {
                "stage3_price": "nan",
                "peak_return_from_stage3": "inf",
                "time_to_100pct": "nan",
            }
        )

        self.assertEqual(quality.stage_dates_confidence, 0.0)
        self.assertIsNone(validation.stage3_price)
        self.assertIsNone(validation.peak_return_from_stage3)
        self.assertIsNone(validation.time_to_100pct)

    def test_case_coverage_reports_insufficient_when_under_2x2(self):
        records = load_case_library("data/e2r_case_library/cases.jsonl")
        coverage = coverage_by_archetype(records, min_positive_cases=2, min_counterexamples=2)
        statuses = {item.archetype: item.status for item in coverage}

        self.assertEqual(statuses[E2RArchetype.EXPORT_RECURRING_CONSUMER], "insufficient_case_coverage")

        with tempfile.TemporaryDirectory() as tmp:
            paths = write_case_coverage_outputs(records, tmp)
            summary = paths["summary"].read_text(encoding="utf-8")

        self.assertIn("insufficient_case_coverage", summary)

    def test_scoring_modules_do_not_import_case_library(self):
        for path in (
            Path("src/e2r/features.py"),
            Path("src/e2r/staging.py"),
            Path("src/e2r/red_team.py"),
            Path("src/e2r/sector_profiles.py"),
        ):
            self.assertNotIn("case_library", path.read_text(encoding="utf-8"), str(path))

    def test_case_mining_dry_run_writes_planned_searches(self):
        with tempfile.TemporaryDirectory() as tmp:
            taxonomy_path = Path(tmp) / "taxonomy.csv"
            write_sector_taxonomy(
                (
                    SectorTaxonomyRow(
                        symbol="267260",
                        company_name="HD현대일렉트릭",
                        market="KR",
                        exchange="KRX",
                        listed_date=None,
                        sector_raw="전력기기",
                        industry_raw="",
                        sector_custom="전력기기/전선",
                        sector_source="test",
                        sector_confidence=0.9,
                        primary_archetype=E2RArchetype.CONTRACT_BACKLOG_INDUSTRIAL,
                        secondary_archetypes=(),
                        business_keywords=("전력기기",),
                        product_keywords=("변압기",),
                        mapping_reason="test",
                    ),
                ),
                taxonomy_path,
            )
            output = Path(tmp) / "out"
            exit_code = mine_cases_main(
                [
                    "--market",
                    "KR",
                    "--start-date",
                    "2023-01-01",
                    "--end-date",
                    "2026-05-14",
                    "--dry-run",
                    "--taxonomy",
                    str(taxonomy_path),
                    "--case-library",
                    "data/e2r_case_library/cases.jsonl",
                    "--output-directory",
                    str(output),
                ]
            )

            self.assertEqual(exit_code, 0)
            self.assertTrue((output / "planned_searches.json").exists())
            self.assertIn("HD현대일렉트릭", (output / "planned_searches.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
