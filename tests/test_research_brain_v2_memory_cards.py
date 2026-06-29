import unittest

from research_brain_v2_test_helpers import load_json, load_v2_cards


class ResearchBrainV2MemoryCardTests(unittest.TestCase):
    def test_cards_exist_for_c01_c36_and_are_compressed(self):
        cards = load_v2_cards()
        self.assertEqual(len(cards), 36)
        for card in cards:
            self.assertLessEqual(len(card.required_primitives), 40)
            self.assertTrue(card.canonical_mechanism)
            self.assertTrue(card.quality_breakdown)

    def test_c06_and_c28_cards_capture_required_operating_boundaries(self):
        cards = {card.archetype_id: card for card in load_v2_cards()}
        c06 = cards["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]
        c28 = cards["C28_SOFTWARE_SECURITY_CONTRACT_RETENTION"]
        self.assertIn("capacity sold-out", c06.stage2_unlocks)
        self.assertIn("cashflow bridge", c06.green_blockers)
        self.assertIn("security theme spike", c28.false_positive_patterns)
        self.assertIn("recurring revenue durability", c28.green_blockers)

    def test_memory_card_matrix_report_has_card_count(self):
        matrix = load_json("docs/operational/research_brain_v2_memory_card_matrix.json")
        self.assertEqual(matrix["summary"]["card_count"], 36)


if __name__ == "__main__":
    unittest.main()
