from __future__ import annotations

import unittest

from e2r.research_brain.researcher_mode.evidence_gap import (
    EvidenceGapAuditLineage,
    EvidenceGapKey,
    derive_objective_identity,
)


class EvidenceGapIdentityTest(unittest.TestCase):
    def _key(self, **overrides: object) -> EvidenceGapKey:
        values: dict[str, object] = {
            "target_id": "TEST_TARGET",
            "as_of_date": "2026-07-12",
            "archetype_id": "TEST_ARCHETYPE",
            "objective_identity": "SGOBJ-stable123",
            "affected_component_ids": (
                "information_confidence",
                "earnings_visibility",
            ),
            "required_source_family": "CUSTOMER_OFFICIAL",
            "economic_mechanism_id": "CUSTOMER_COMMITMENT_VISIBILITY",
            "predicate_or_fact_need_id": "DIRECT_CONTRACT_TERMS",
            "fact_snapshot_hash": "a" * 64,
            "accepted_lineage_roster_hash": "b" * 64,
        }
        values.update(overrides)
        return EvidenceGapKey(**values)  # type: ignore[arg-type]

    def test_evidence_gap_key_is_paraphrase_invariant(self) -> None:
        paraphrases = (
            "고객 공식 계약 corroboration이 부족함",
            "named customer direct confirmation이 확인되지 않음",
            "고객사 직접 물량·가격·기간 근거가 없음",
        )
        keys = []
        for prose in paraphrases:
            key = self._key()
            lineage = EvidenceGapAuditLineage(supervisor_text=prose)
            self.assertNotIn("supervisor_text", key.identity_payload())
            self.assertEqual(prose, lineage.to_dict()["supervisor_text"])
            keys.append(key.gap_key)
        self.assertEqual(1, len(set(keys)))
        self.assertTrue(
            set(EvidenceGapKey.identity_field_names()).isdisjoint(
                EvidenceGapKey.prohibited_prose_or_call_lineage_fields()
            )
        )

    def test_different_core_fact_need_does_not_collide(self) -> None:
        contract_gap = self._key(
            predicate_or_fact_need_id="DIRECT_CONTRACT_TERMS"
        )
        fcf_gap = self._key(
            predicate_or_fact_need_id="FCF_PRIMARY_SOURCE",
            economic_mechanism_id="CASH_CONVERSION",
        )
        self.assertNotEqual(contract_gap.gap_key, fcf_gap.gap_key)
        self.assertNotEqual(contract_gap.semantic_gap_id, fcf_gap.semantic_gap_id)

    def test_prompt_hash_does_not_define_gap_identity(self) -> None:
        key = self._key()
        first = EvidenceGapAuditLineage(prompt_hash="QUERYPROMPT-first")
        second = EvidenceGapAuditLineage(prompt_hash="QUERYPROMPT-second")
        self.assertNotEqual(first.to_dict(), second.to_dict())
        self.assertNotIn("prompt_hash", key.identity_payload())
        self.assertEqual(key.gap_key, self._key().gap_key)

    def test_fallback_objective_identity_uses_only_stable_structure(self) -> None:
        first = derive_objective_identity(
            stable_objective_id=None,
            affected_component_ids=(
                "information_confidence",
                "earnings_visibility",
            ),
            required_source_family=(
                "PUBLIC_BROKER_PDF",
                "CUSTOMER_OFFICIAL",
            ),
            economic_mechanism_id="CUSTOMER_COMMITMENT_VISIBILITY",
            predicate_or_fact_need_id="DIRECT_CONTRACT_TERMS",
        )
        second = derive_objective_identity(
            stable_objective_id=None,
            affected_component_ids=(
                "earnings_visibility",
                "information_confidence",
            ),
            required_source_family=(
                "CUSTOMER_OFFICIAL",
                "PUBLIC_BROKER_PDF",
            ),
            economic_mechanism_id="CUSTOMER_COMMITMENT_VISIBILITY",
            predicate_or_fact_need_id="DIRECT_CONTRACT_TERMS",
        )
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
