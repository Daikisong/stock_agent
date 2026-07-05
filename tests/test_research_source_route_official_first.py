import json
import unittest
from pathlib import Path


class ResearchSourceRouteOfficialFirstTests(unittest.TestCase):
    def test_each_primitive_has_primary_or_secondary_official_route_before_web_discovery(self) -> None:
        matrix = json.loads(Path("docs/operational/research_source_route_recovery_matrix.json").read_text(encoding="utf-8"))
        grouped = {}
        for pattern in matrix["patterns"]:
            key = (pattern["archetype_id"], pattern["primitive_id"])
            grouped.setdefault(key, []).append(pattern)
        for key, patterns in grouped.items():
            official = [
                pattern
                for pattern in patterns
                if pattern["route_role"] in {"PRIMARY", "SECONDARY"} and pattern["official_first_required"]
            ]
            self.assertGreater(len(official), 0, key)


if __name__ == "__main__":
    unittest.main()
