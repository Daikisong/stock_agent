from __future__ import annotations

import json
import unittest
from pathlib import Path

from e2r.research_brain.researcher_mode import (
    C06_MANDATORY_ANCHOR_FAMILIES,
    COMPONENT_ANCHOR_PASS,
)


class E2RV5ComponentAnchorAtlasTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]

    @classmethod
    def setUpClass(cls) -> None:
        cls.path = cls.ROOT / "docs/operational/e2r_v5_component_anchor_atlas.json"
        cls.atlas = json.loads(cls.path.read_text(encoding="utf-8"))

    def test_all_registry_components_have_ordinal_anchor_or_explicit_gap(self) -> None:
        self.assertEqual(self.atlas["status"], COMPONENT_ANCHOR_PASS)
        self.assertEqual(self.atlas["critical_count_sum"], 0)
        self.assertEqual(self.atlas["registry_archetype_count"], 36)
        self.assertEqual(self.atlas["component_count"], 7)
        self.assertEqual(len(self.atlas["component_coverage"]), 36 * 7)
        for row in self.atlas["component_coverage"]:
            self.assertTrue(row["ordinal_anchor_count"] or row["explicit_gap"])
            if row["explicit_gap"]:
                self.assertTrue(row["gap_reason"])

    def test_exact_anchors_are_source_backed_and_proxy_rows_are_guard_only(self) -> None:
        exact = 0
        proxy = 0
        for row in self.atlas["component_anchors"]:
            if row["usable_as_exact_anchor"]:
                exact += 1
                self.assertEqual(row["confidence"], "HIGH")
                self.assertTrue(row["source_backed_case_ids"])
                self.assertFalse(row["source_proxy_guard_case_ids"])
            if row["source_proxy_guard_case_ids"]:
                proxy += 1
                self.assertFalse(row["usable_as_exact_anchor"])
        self.assertGreater(exact, 0)
        self.assertGreater(proxy, 0)

    def test_every_archetype_has_positive_and_counter_exemplar(self) -> None:
        rows = self.atlas["archetype_role_exemplars"]
        self.assertEqual(len(rows), 36 * 2)
        self.assertEqual(
            {(row["archetype_id"], row["role"]) for row in rows},
            {
                (archetype_id, role)
                for archetype_id in {row["archetype_id"] for row in rows}
                for role in ("POSITIVE", "COUNTER")
            },
        )
        self.assertFalse(any(row["explicit_gap"] for row in rows))

    def test_c06_six_mandatory_economic_anchor_families_are_present(self) -> None:
        rows = self.atlas["c06_mandatory_anchors"]
        self.assertEqual(
            {row["anchor_family_id"] for row in rows},
            set(C06_MANDATORY_ANCHOR_FAMILIES),
        )
        for row in rows:
            self.assertTrue(row["matched_case_ids"], row["anchor_family_id"])
            self.assertTrue(row["usable_as_ordinal_anchor"])
            self.assertFalse(row["company_name_conditioned"])
            self.assertFalse(row["target_symbol_conditioned"])

    def test_conflicting_score_rows_are_quarantined_not_exact(self) -> None:
        conflict = self.atlas["conflict_quarantine"]
        self.assertEqual(
            conflict["conflicting_case_count"],
            conflict["quarantined_conflicting_case_count"],
        )
        self.assertEqual(
            self.atlas["critical_counts"]["anchor_conflict_not_quarantined_count"],
            0,
        )


if __name__ == "__main__":
    unittest.main()
