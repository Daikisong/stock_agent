import json
import unittest
from pathlib import Path


class ResearchRuntimeMemoryCardsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cards = json.loads(Path("docs/operational/research_runtime_memory_cards_v2.json").read_text(encoding="utf-8"))
        cls.matrix = json.loads(
            Path("docs/operational/research_runtime_memory_card_matrix_v2.json").read_text(encoding="utf-8")
        )
        cls.by_prefix = {card["archetype_id"].split("_", 1)[0]: card for card in cls.cards["cards"]}

    def test_cards_cover_all_archetypes(self) -> None:
        self.assertEqual(self.cards["schema_version"], "e2r_research_runtime_memory_cards_v2")
        self.assertEqual(self.cards["card_count"], 36)
        self.assertEqual(len(self.cards["runtime_planner_payloads"]), 36)
        self.assertEqual(self.matrix["card_count"], 36)

    def test_mandatory_cards_separate_url_backed_and_proxy_cases(self) -> None:
        for prefix in ("C06", "C08", "C15", "C17", "C24", "C28"):
            card = self.by_prefix[prefix]
            self.assertEqual(card["runtime_usage_policy"], "READY_FOR_ROUTING", prefix)
            self.assertGreater(len(card["url_backed_replay_cases"]), 0, prefix)
            self.assertGreater(len(card["source_proxy_only_cases"]), 0, prefix)
            self.assertGreater(len(card["source_route_priority_by_primitive"]), 0, prefix)

    def test_each_required_primitive_has_source_route_priority(self) -> None:
        for card in self.cards["cards"]:
            for primitive in card["required_positive_primitives"]:
                self.assertIn(primitive, card["source_route_priority_by_primitive"])
                self.assertGreater(len(card["source_route_priority_by_primitive"][primitive]), 0)


if __name__ == "__main__":
    unittest.main()
