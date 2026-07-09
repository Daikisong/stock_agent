from __future__ import annotations

import unittest
from pathlib import Path

from e2r.calibration.taxonomy import CANONICAL_ARCHETYPE_IDS
from e2r.research_brain.compiler import compile_research_intelligence
from e2r.research_brain.corpus import parse_historical_research_artifact


REPO_ROOT = Path(__file__).resolve().parents[1]
FIXTURE_ROOT = REPO_ROOT / "tests" / "fixtures" / "e2r_reconstruction" / "corpus"


class ResearchCorpusGoldenTest(unittest.TestCase):
    def test_mandatory_golden_cases_are_preserved_one_for_one(self) -> None:
        path = FIXTURE_ROOT / "golden_mandatory_cases.md"
        parsed = parse_historical_research_artifact(path, repo_root=REPO_ROOT)
        result = compile_research_intelligence([path], repo_root=REPO_ROOT)

        self.assertEqual(len(result.cases), 6)
        self.assertEqual(
            {case.canonical_archetype_id for case in result.cases},
            {
                "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
                "C15_MATERIAL_SPREAD_SUPERCYCLE",
                "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD",
                "C24_BIO_TRIAL_DATA_EVENT_RISK",
                "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
            },
        )
        self.assertNotIn("MUST_NOT_BE_PARSED", {case.case_id for case in result.cases})
        self.assertIsNotNone(parsed.artifact.handoff_line_range)
        self.assertEqual(
            result.manifest["quality"]["handoff_prompt_parsed_as_case_count"],
            0,
        )
        self.assertEqual(
            result.manifest["quality"]["structured_jsonl_row_preservation_rate"],
            1.0,
        )

        by_archetype = {case.canonical_archetype_id: case for case in result.cases}
        for archetype_id in (
            "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
            "C15_MATERIAL_SPREAD_SUPERCYCLE",
        ):
            self.assertTrue(by_archetype[archetype_id].evidence_references)
            self.assertTrue(
                any(reference.url for reference in by_archetype[archetype_id].evidence_references)
            )
        for archetype_id in (
            "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD",
            "C24_BIO_TRIAL_DATA_EVENT_RISK",
            "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
        ):
            self.assertEqual(by_archetype[archetype_id].declared_source_quality, "SOURCE_PROXY_ONLY")
        self.assertFalse(
            any(
                reference.url and "example.invalid" in reference.url
                for case in result.cases
                for reference in case.evidence_references
            )
        )

    def test_registry_golden_has_every_canonical_archetype_exactly_once(self) -> None:
        path = FIXTURE_ROOT / "golden_registry_cases.jsonl"
        result = compile_research_intelligence([path], repo_root=REPO_ROOT)

        self.assertEqual(len(result.cases), len(CANONICAL_ARCHETYPE_IDS))
        self.assertEqual(
            {case.canonical_archetype_id for case in result.cases},
            set(CANONICAL_ARCHETYPE_IDS),
        )
        self.assertEqual(len({case.case_id for case in result.cases}), len(result.cases))
        self.assertEqual(len({case.symbol for case in result.cases}), len(result.cases))
        self.assertEqual(result.manifest["status"], "RESEARCH_CORPUS_SEMANTIC_COMPILER_PASS")
        self.assertEqual(result.manifest["critical_count_sum"], 0)
        self.assertEqual(result.manifest["quality"]["present_company_name_loss_count"], 0)
        self.assertEqual(result.manifest["quality"]["present_trigger_date_loss_count"], 0)
        self.assertEqual(result.manifest["quality"]["first_symbol_collapse_count"], 0)


if __name__ == "__main__":
    unittest.main()
