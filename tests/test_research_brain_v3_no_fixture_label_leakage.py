import unittest

from e2r.research_brain.v3_raw_event_routing import load_raw_event_routing_fixtures


class ResearchBrainV3NoFixtureLabelLeakageTests(unittest.TestCase):
    def test_expected_archetype_not_in_event_text(self):
        for row in load_raw_event_routing_fixtures():
            expected = row["expected_archetype"]
            text = " ".join(
                [
                    row.get("event_summary", ""),
                    row.get("event_title", ""),
                    " ".join(row.get("raw_reason_codes", ())),
                ]
            )
            self.assertNotIn(expected, text)


if __name__ == "__main__":
    unittest.main()
