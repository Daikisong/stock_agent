from __future__ import annotations

import unittest

from e2r.research_brain.researcher_mode.evidence_gap import (
    EvidenceGapAuditLineage,
    EvidenceGapAssessment,
    EvidenceGapClass,
    EvidenceGapKey,
    MissingSourceRole,
    accepted_lineage_profile,
    derive_objective_identity,
    source_corpus_profile,
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

    def test_fact_and_source_roster_hashes_ignore_row_order(self) -> None:
        links = [
            {
                "link_id": "L2",
                "claim_id": "C2",
                "fact_id": "F2",
                "current_lifecycle": "CURRENT",
                "source_ids": ["S2"],
            },
            {
                "link_id": "L1",
                "claim_id": "C1",
                "fact_id": "F1",
                "current_lifecycle": "OPEN",
                "source_ids": ["S1"],
            },
        ]
        documents = [
            {"document_id": "D2", "content_hash": "H2"},
            {"document_id": "D1", "content_hash": "H1"},
        ]
        self.assertEqual(
            accepted_lineage_profile(links),
            accepted_lineage_profile(tuple(reversed(links))),
        )
        self.assertEqual(
            source_corpus_profile(documents),
            source_corpus_profile(tuple(reversed(documents))),
        )


class EvidenceGapMaterialityTest(unittest.TestCase):
    def _key(
        self, affected_component_ids: tuple[str, ...]
    ) -> EvidenceGapKey:
        return EvidenceGapKey(
            target_id="TEST_TARGET",
            as_of_date="2026-07-12",
            archetype_id="TEST_ARCHETYPE",
            objective_identity="SGOBJ-stable123",
            affected_component_ids=affected_component_ids,
            required_source_family=(
                "CUSTOMER_OFFICIAL"
                if len(affected_component_ids) == 1
                else "SOURCE_FAMILY_SET[CUSTOMER_OFFICIAL,PUBLIC_BROKER_PDF]"
            ),
            economic_mechanism_id="CUSTOMER_COMMITMENT_VISIBILITY",
            predicate_or_fact_need_id="DIRECT_CONTRACT_TERMS",
            fact_snapshot_hash="a" * 64,
            accepted_lineage_roster_hash="b" * 64,
        )

    def _corroboration_cap(self) -> EvidenceGapAssessment:
        key = self._key(
            ("information_confidence", "earnings_visibility")
        )
        return EvidenceGapAssessment.classify(
            key=key,
            missing_source_role=MissingSourceRole.INDEPENDENT_CORROBORATION,
            source_backed_component_ids=(
                "information_confidence",
                "earnings_visibility",
                "eps_fcf_explosion",
                "market_mispricing",
                "valuation_rerating",
            ),
            component_range_bounded=True,
            could_change_score=True,
            could_change_stage=True,
            could_change_hard_break=False,
            economic_reason=(
                "핵심 actual과 재무 자료는 있으나 독립 고객 확인이 미확인이다."
            ),
            llm_proposed_gap_class="CORROBORATION_CAP",
        )

    def test_corroboration_gap_only_caps_affected_components(self) -> None:
        assessment = self._corroboration_cap()
        self.assertEqual(EvidenceGapClass.CORROBORATION_CAP, assessment.gap_class)
        self.assertEqual(
            ("earnings_visibility", "information_confidence"),
            assessment.capped_component_ids,
        )
        self.assertEqual((), assessment.blocked_component_ids)
        self.assertTrue(assessment.score_valid_if_only_gap)
        self.assertFalse(assessment.global_score_block)

    def test_corroboration_gap_does_not_zero_fcf_revision_valuation(self) -> None:
        assessment = self._corroboration_cap()
        for component_id in (
            "eps_fcf_explosion",
            "market_mispricing",
            "valuation_rerating",
        ):
            self.assertEqual("UNAFFECTED", assessment.component_effect(component_id))
            self.assertTrue(
                assessment.component_completion_allowed(component_id)
            )

    def test_core_score_blocker_keeps_score_invalid(self) -> None:
        key = self._key(("eps_fcf_explosion",))
        assessment = EvidenceGapAssessment.classify(
            key=key,
            missing_source_role=MissingSourceRole.CORE_SCORE_SOURCE,
            source_backed_component_ids=(),
            component_range_bounded=False,
            provider_or_parser_failure=True,
            could_change_score=True,
            could_change_stage=True,
            could_change_hard_break=False,
            economic_reason="핵심 FCF 원문을 읽지 못했다.",
            llm_proposed_gap_class="CORROBORATION_CAP",
        )
        self.assertEqual(EvidenceGapClass.CORE_SCORE_BLOCKER, assessment.gap_class)
        self.assertFalse(assessment.score_valid_if_only_gap)
        self.assertTrue(assessment.global_score_block)
        self.assertEqual("BLOCKED", assessment.component_effect("eps_fcf_explosion"))
        self.assertFalse(
            assessment.to_dict()["llm_proposal_matches_deterministic_class"]
        )

    def test_monitoring_gap_does_not_block_component_completion(self) -> None:
        key = self._key(("information_confidence",))
        assessment = EvidenceGapAssessment.classify(
            key=key,
            missing_source_role=MissingSourceRole.MONITORING_ONLY,
            source_backed_component_ids=("information_confidence",),
            component_range_bounded=True,
            could_change_score=False,
            could_change_stage=False,
            could_change_hard_break=False,
            economic_reason="다음 event refresh에서 다시 확인할 보조 항목이다.",
        )
        self.assertEqual(EvidenceGapClass.MONITORING_GAP, assessment.gap_class)
        self.assertTrue(
            assessment.component_completion_allowed("information_confidence")
        )
        self.assertTrue(assessment.score_valid_if_only_gap)


if __name__ == "__main__":
    unittest.main()
