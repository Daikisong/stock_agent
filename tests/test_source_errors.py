from datetime import date
import unittest

from e2r.sources.source_errors import date_value


class SourceErrorsTests(unittest.TestCase):
    def test_date_value_accepts_single_digit_month_and_day(self):
        self.assertEqual(date_value("2025-1-1"), date(2025, 1, 1))
        self.assertEqual(date_value("2025.1.9"), date(2025, 1, 9))

    def test_date_value_keeps_compact_yyyymmdd_support(self):
        self.assertEqual(date_value("20250109"), date(2025, 1, 9))


if __name__ == "__main__":
    unittest.main()
