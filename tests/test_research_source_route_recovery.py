import json
import unittest
from pathlib import Path


class ResearchSourceRouteRecoveryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.matrix = json.loads(Path("docs/operational/research_source_route_recovery_matrix.json").read_text(encoding="utf-8"))
        cls.patterns = cls.matrix["patterns"]

    def test_source_route_patterns_exist_for_mandatory_required_primitives(self) -> None:
        self.assertEqual(self.matrix["schema_version"], "e2r_research_source_route_recovery_matrix_v1")
        self.assertEqual(self.matrix["archetype_count"], 36)
        self.assertGreater(self.matrix["pattern_count"], 100)
        by_arch = {}
        for pattern in self.patterns:
            by_arch.setdefault(pattern["archetype_id"].split("_", 1)[0], set()).add(pattern["primitive_id"])
        for prefix in ("C06", "C08", "C15", "C17", "C24", "C28"):
            self.assertGreater(len(by_arch[prefix]), 0, prefix)

    def test_research_memory_is_discovery_only(self) -> None:
        for pattern in self.patterns:
            if pattern["source_family"] == "ResearchMemory":
                self.assertEqual(pattern["route_role"], "DISCOVERY_ONLY")


if __name__ == "__main__":
    unittest.main()
