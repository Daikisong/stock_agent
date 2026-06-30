import unittest

from e2r.census.universe import is_fixture_like_symbol


class CensusNoFixtureSymbolsTests(unittest.TestCase):
    def test_fixture_like_symbols_detected(self):
        self.assertTrue(is_fixture_like_symbol("TEST01"))
        self.assertTrue(is_fixture_like_symbol("123"))
        self.assertFalse(is_fixture_like_symbol("005930"))


if __name__ == "__main__":
    unittest.main()
