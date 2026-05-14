import tempfile
from pathlib import Path
import unittest

from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.research_framework import (
    E2RArchetypeBlock,
    EXTENSION_TO_ROUND1_CORE,
    ROUND1_CORE_ARCHETYPES,
    ROUND1_SCORE_WEIGHT_DRAFT,
    round1_block,
    round1_core_for,
    summarize_round1_case_mapping,
    write_round1_framework_reports,
)


class ResearchFrameworkTests(unittest.TestCase):
    def test_round1_core_has_25_archetypes_and_extensions_are_separate(self):
        self.assertEqual(len(ROUND1_CORE_ARCHETYPES), 25)
        self.assertEqual(len(set(ROUND1_CORE_ARCHETYPES)), 25)
        self.assertIn(E2RArchetype.GENERIC_UNCLASSIFIED, ROUND1_CORE_ARCHETYPES)
        self.assertNotIn(E2RArchetype.AI_DATA_CENTER_INFRASTRUCTURE, ROUND1_CORE_ARCHETYPES)
        self.assertGreaterEqual(len(EXTENSION_TO_ROUND1_CORE), 10)

    def test_three_block_mapping_examples(self):
        self.assertEqual(round1_block(E2RArchetype.CONTRACT_BACKLOG_INDUSTRIAL), E2RArchetypeBlock.STRUCTURAL_E2R)
        self.assertEqual(round1_block(E2RArchetype.SHIPPING_FREIGHT_CYCLE), E2RArchetypeBlock.CYCLICAL_SPREAD_GUARDRAILED)
        self.assertEqual(round1_block(E2RArchetype.ONE_OFF_EVENT_DEMAND), E2RArchetypeBlock.RED_YELLOW_GUARDRAIL)
        self.assertEqual(round1_block(E2RArchetype.AI_DATA_CENTER_INFRASTRUCTURE), E2RArchetypeBlock.EXTENSION_REFINEMENT)

    def test_extension_maps_to_round1_core_bucket(self):
        self.assertEqual(round1_core_for(E2RArchetype.VALUE_UP_SHAREHOLDER_RETURN), E2RArchetype.FINANCIAL_SPREAD_BALANCE_SHEET)
        self.assertEqual(round1_core_for(E2RArchetype.BIOTECH_ROYALTY_COMMERCIALIZATION), E2RArchetype.BIOTECH_REGULATORY)
        self.assertEqual(round1_core_for(E2RArchetype.AUTO_MOBILITY_COMPLETED_VEHICLE), E2RArchetype.AUTO_MOBILITY_COMPONENTS)

    def test_case_pack_summary_uses_round1_mapping(self):
        records = load_case_library("data/e2r_case_library/cases_v02.jsonl")
        summary = summarize_round1_case_mapping(records)

        self.assertEqual(summary["round1_core_archetype_count"], 25)
        self.assertEqual(summary["current_archetype_enum_count"], len(tuple(E2RArchetype)))
        self.assertGreater(summary["cases_using_extension_archetypes"], 0)
        self.assertIn(E2RArchetypeBlock.STRUCTURAL_E2R.value, summary["block_counts"])

    def test_weight_draft_is_report_only_for_known_round1_archetypes(self):
        self.assertIn(E2RArchetype.CONTRACT_BACKLOG_INDUSTRIAL, ROUND1_SCORE_WEIGHT_DRAFT)
        self.assertEqual(ROUND1_SCORE_WEIGHT_DRAFT[E2RArchetype.MEMORY_HBM_CAPACITY]["eps_fcf_explosion"], 24)

    def test_report_writer_outputs_round1_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round1_framework_reports(output_directory=tmp)

            self.assertTrue(paths["summary"].exists())
            self.assertIn("round1_core_archetype_count: 25", paths["summary"].read_text(encoding="utf-8"))
            self.assertTrue(paths["archetype_blocks"].exists())
            self.assertTrue(paths["case_mapping"].exists())
            self.assertTrue(paths["score_weight_draft"].exists())


if __name__ == "__main__":
    unittest.main()
