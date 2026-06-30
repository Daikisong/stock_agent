import unittest

from e2r.production.claim_extraction.anchor_validator import validate_anchor


class CutoverV2QuoteAnchorValidationTests(unittest.TestCase):
    def test_quote_must_exist_in_document_text(self):
        self.assertFalse(
            validate_anchor(
                exact_quote="없는 문장",
                document_text="삼성전자는 공급계약을 공시했다.",
                locator=None,
                anchor_type="TEXT_SPAN",
            ).valid
        )
        self.assertTrue(
            validate_anchor(
                exact_quote=None,
                document_text=None,
                locator="opendart:list:123",
                anchor_type="API_RECORD",
            ).valid
        )


if __name__ == "__main__":
    unittest.main()
