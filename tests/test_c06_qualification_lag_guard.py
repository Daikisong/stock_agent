from __future__ import annotations

import json
import unittest
from pathlib import Path


class C06QualificationLagGuardTests(unittest.TestCase):
    def test_qualification_counter_does_not_force_hard_4c(self) -> None:
        audit = json.loads(
            Path("docs/operational/e2r_c06_historical_component_replay.json").read_text()
        )
        row = next(
            item
            for item in audit["cases"]
            if item["case_id"] == "C06-SAMSUNG-20240524-QUALIFICATION-LAG"
        )
        self.assertEqual(row["adjudication_status"], "IMPACT_ADJUDICATION_PASS")
        self.assertFalse(row["hard_break_emitted"])
        self.assertEqual(row["forbidden_component_count"], 0)


if __name__ == "__main__": unittest.main()
