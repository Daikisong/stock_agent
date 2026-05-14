from datetime import date, datetime
import unittest

from e2r.audit import audit_parser_outputs
from e2r.models import Evidence, Market, SourceTier


AS_OF = date(2024, 5, 21)


class ParserAuditTests(unittest.TestCase):
    def test_parser_audit_catches_impossible_contract_ratio(self):
        evidence = _evidence(
            parsed_fields={
                "contract_amount_to_prior_sales": 6.0,
                "parser_confidence": 0.9,
            }
        )

        findings = audit_parser_outputs(evidence=(evidence,))

        self.assertTrue(any(item.code == "contract_ratio_too_high" for item in findings))
        finding = next(item for item in findings if item.code == "contract_ratio_too_high")
        self.assertEqual(finding.severity, "hard")
        self.assertEqual(finding.suggested_action, "block_green")

    def test_parser_audit_catches_low_parser_confidence(self):
        evidence = _evidence(parsed_fields={"parser_confidence": 0.3})

        findings = audit_parser_outputs(evidence=(evidence,))

        self.assertTrue(any(item.code == "low_parser_confidence" for item in findings))
        finding = next(item for item in findings if item.code == "low_parser_confidence")
        self.assertEqual(finding.severity, "warning")
        self.assertEqual(finding.suggested_action, "manual_review")

    def test_routine_opendart_list_evidence_does_not_flood_low_confidence_audit(self):
        evidence = _evidence(
            source_type="disclosure",
            source_name="OpenDART",
            parsed_fields={"parser_confidence": 0.3, "signal_class": "routine"},
        )

        findings = audit_parser_outputs(evidence=(evidence,))

        self.assertFalse(any(item.code == "low_parser_confidence" for item in findings))


def _evidence(parsed_fields, source_type="research_report", source_name="FixtureBroker"):
    timestamp = datetime(2024, 5, 21, 8)
    return Evidence(
        evidence_id="test:evidence",
        source_type=source_type,
        source_name=source_name,
        source_tier=SourceTier.TIER_1,
        published_at=timestamp,
        observed_at=timestamp,
        available_at=timestamp,
        as_of_date=AS_OF,
        market=Market.KR,
        symbol="999999",
        title="감사 테스트",
        parsed_fields=parsed_fields,
        confidence=float(parsed_fields.get("parser_confidence", 0.5)),
    )


if __name__ == "__main__":
    unittest.main()
