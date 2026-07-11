from __future__ import annotations

import unittest
from types import SimpleNamespace

from e2r.agentic import MappingStatus, Polarity, PrimitiveMappingProposal, RawAssertion, SupportDirection
from e2r.agentic.evidence_workflow import (
    _mapping_is_pricing_power_without_realized_target_pricing,
)


class KoreanRealizedPricingGuardTests(unittest.TestCase):
    def test_current_korean_average_selling_price_increase_is_not_rejected(self) -> None:
        raw = RawAssertion(
            raw_assertion_id="RA-KO-ASP",
            anchor_id="ANCH-KO-ASP",
            subject_text="임의회사",
            predicate="메모리 평균 판매가격 변동",
            object_text="메모리 평균 판매가격은 전년 대비 146% 상승했다",
            polarity_proposal=Polarity.POSITIVE,
            effective_period_text="2026년 1분기",
            exact_quote="메모리 평균 판매가격은 전년 연간 평균 대비 약 146% 상승하였으며",
        )
        mapping = PrimitiveMappingProposal.build(
            claim_id="CLM-KO-ASP",
            archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            primitive_id="memory_price_increase_mentioned",
            support_direction=SupportDirection.SUPPORT,
            mapping_status=MappingStatus.ACCEPTED,
            rationale="현재 실현된 평균 판매가격 상승",
        )
        self.assertFalse(
            _mapping_is_pricing_power_without_realized_target_pricing(
                SimpleNamespace(raw_assertion=raw), mapping
            )
        )


if __name__ == "__main__":
    unittest.main()
