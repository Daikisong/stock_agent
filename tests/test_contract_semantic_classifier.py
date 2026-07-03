import unittest

from e2r.evidence.contract_semantic_classifier import classify_contract_event
from e2r.evidence.primitive_semantic_guard import guard_score_contribution


class ContractSemanticClassifierTests(unittest.TestCase):
    def test_supply_contract_is_revenue_facing(self):
        result = classify_contract_event({"quote_text": "단일판매ㆍ공급계약체결 계약금액 기간 거래상대방"})
        self.assertTrue(result.allowed_for_contract_quality)
        self.assertEqual(result.event_class, "commercial_supply_contract")

    def test_share_buyback_trust_is_not_customer_contract(self):
        result = classify_contract_event({"quote_text": "자기주식취득신탁계약체결결정"})
        self.assertFalse(result.allowed_for_contract_quality)
        self.assertEqual(result.event_class, "share_buyback_trust_contract")

    def test_pledge_contract_is_not_customer_contract(self):
        result = classify_contract_event({"quote_text": "주식담보제공계약체결"})
        self.assertFalse(result.allowed_for_contract_quality)
        self.assertEqual(result.event_class, "pledge_or_collateral_contract")

    def test_equity_issuance_is_not_earnings_visibility(self):
        result = classify_contract_event({"quote_text": "주요사항보고서(유상증자결정) 증권신고서(지분증권)"})
        self.assertFalse(result.allowed_for_contract_quality)
        self.assertEqual(result.event_class, "equity_issuance_or_security_registration")

    def test_rumor_clarification_is_information_only(self):
        result = classify_contract_event({"quote_text": "풍문또는보도에대한해명(미확정)"})
        self.assertFalse(result.allowed_for_contract_quality)
        self.assertEqual(result.event_class, "clarification_or_rumor_response")

    def test_facility_investment_correction_cannot_support_capacity_score(self):
        result = guard_score_contribution(
            contribution={
                "component_key": "bottleneck_pricing",
                "criterion_id": "production_cutover_capacity_expansion",
            },
            support_claims=[
                {
                    "primitive_id": "capacity_expansion",
                    "quote_text": "대웅(003090) [기재정정]신규시설투자등 정정사유 종료일 연장 정정전 2026-06-30 정정후 2027-05-31",
                }
            ],
        )
        self.assertFalse(result["score_allowed"])
        self.assertEqual(result["semantic_guard_status"], "BLOCKED")
        self.assertEqual(result["semantic_guard_class"], "facility_investment_correction_followup_required")

    def test_facility_investment_correction_guard_is_not_symbol_specific(self):
        result = guard_score_contribution(
            contribution={
                "component_key": "bottleneck_pricing",
                "criterion_id": "production_cutover_capacity_expansion",
            },
            support_claims=[
                {
                    "primitive_id": "capacity_expansion",
                    "quote_text": "테스트기업(123456) [기재정정]신규시설투자등 정정사유 종료일 연장 정정전 2026-06-30 정정후 2027-05-31",
                }
            ],
        )
        self.assertFalse(result["score_allowed"])
        self.assertEqual(result["semantic_guard_status"], "BLOCKED")
        self.assertEqual(result["semantic_guard_class"], "facility_investment_correction_followup_required")


if __name__ == "__main__":
    unittest.main()
