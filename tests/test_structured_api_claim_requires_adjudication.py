import unittest
from datetime import date

from e2r.production.claim_extraction import (
    RawAssertionRecord,
    adjudicate_entity_temporal_scope,
    map_claim_to_primitive,
)


class StructuredApiClaimRequiresAdjudicationTests(unittest.TestCase):
    def test_wrong_subject_claim_rejected_before_mapping(self):
        assertion = RawAssertionRecord(
            raw_assertion_id="RAW1",
            document_id="DOC1",
            anchor_id="ANCHOR1",
            subject="월덱스",
            predicate="audit_or_accounting_claim",
            object_text="월덱스의 감사의견은 적정이다.",
            polarity_proposal="POSITIVE",
            modality="STATED",
            event_date="2020-03-18",
            exact_quote="월덱스의 감사의견은 적정이다.",
            related_entities=("삼성전자",),
        )
        adjudication = adjudicate_entity_temporal_scope(
            assertion,
            target_aliases=("삼성전자", "005930"),
            as_of_date=date(2026, 6, 30),
        )
        decision = map_claim_to_primitive(
            assertion,
            adjudication,
            allowed_primitives=("accounting_trust_break",),
        )
        self.assertEqual(adjudication.semantic_status, "REJECTED")
        self.assertEqual(decision.mapping_status, "REJECTED")


if __name__ == "__main__":
    unittest.main()
