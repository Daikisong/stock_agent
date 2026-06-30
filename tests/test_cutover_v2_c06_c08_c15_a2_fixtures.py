import unittest

from e2r.production import cutover_v2


class CutoverV2C06C08C15A2FixturesTests(unittest.TestCase):
    def test_c06_c08_c15_have_url_backed_candidates(self):
        for archetype_id, minimum in cutover_v2._A2_ARCHETYPE_TARGETS.items():
            rows = cutover_v2._iter_a2_url_candidates(".", archetype_id, limit=minimum)
            self.assertGreaterEqual(len(rows), minimum)


if __name__ == "__main__":
    unittest.main()
