import unittest

from e2r.research_brain.v4_evidence_extraction_bridge import _structured_field_polarity


class CutoverNoDefaultPositiveCurrentTargetTests(unittest.TestCase):
    def test_structured_field_presence_is_not_positive(self):
        polarity, source = _structured_field_polarity("TARGET_PRC", "90000")
        self.assertEqual(polarity.value, "NORMAL")
        self.assertEqual(source, "structured_field_presence_only_not_score_positive")


if __name__ == "__main__":
    unittest.main()
