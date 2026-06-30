import unittest

from e2r.census.census_event import build_census_assessment_event
from tests.census_test_helpers import instrument


class CensusIdempotentRerunTests(unittest.TestCase):
    def test_census_event_id_is_stable(self):
        inst = instrument()
        first = build_census_assessment_event(inst, as_of_date="2026-07-01")
        second = build_census_assessment_event(inst, as_of_date="2026-07-01")
        self.assertEqual(first.assessment_event_id, second.assessment_event_id)


if __name__ == "__main__":
    unittest.main()
