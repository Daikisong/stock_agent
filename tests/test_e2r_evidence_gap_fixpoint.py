from __future__ import annotations

import unittest

from e2r.research_brain.researcher_mode.evidence_gap import (
    EvidenceGapAuditLineage,
    EvidenceGapAssessment,
    EvidenceGapClass,
    EvidenceGapDisposition,
    EvidenceGapKey,
    MissingSourceRole,
    NoNewRouteConfirmation,
    RepeatedExhaustedGapReopenedError,
    SemanticNoNewRouteFixpoint,
    accepted_lineage_profile,
    canonical_current_pending_request_ids,
    derive_objective_identity,
    guard_source_query_generation,
    latest_evidence_gap_dispositions,
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


class EvidenceGapDispositionTest(unittest.TestCase):
    def _assessment(
        self,
        *,
        fact_hash: str = "a" * 64,
        lineage_hash: str = "b" * 64,
        supervisor_prose: str = "ignored",
    ) -> EvidenceGapAssessment:
        del supervisor_prose
        key = EvidenceGapKey(
            target_id="TEST_TARGET",
            as_of_date="2026-07-12",
            archetype_id="TEST_ARCHETYPE",
            objective_identity="SGOBJ-stable123",
            affected_component_ids=(
                "information_confidence",
                "earnings_visibility",
            ),
            required_source_family=(
                "SOURCE_FAMILY_SET[CUSTOMER_OFFICIAL,PUBLIC_BROKER_PDF]"
            ),
            economic_mechanism_id="CUSTOMER_COMMITMENT_VISIBILITY",
            predicate_or_fact_need_id="DIRECT_CONTRACT_TERMS",
            fact_snapshot_hash=fact_hash,
            accepted_lineage_roster_hash=lineage_hash,
        )
        return EvidenceGapAssessment.classify(
            key=key,
            missing_source_role=MissingSourceRole.INDEPENDENT_CORROBORATION,
            source_backed_component_ids=(
                "information_confidence",
                "earnings_visibility",
            ),
            component_range_bounded=True,
            could_change_score=True,
            could_change_stage=True,
            could_change_hard_break=False,
            economic_reason="독립 corroboration 미확인",
        )

    def _disposition(self) -> EvidenceGapDisposition:
        return EvidenceGapDisposition.unresolved(
            assessment=self._assessment(),
            attempted_route_signatures=("ROUTE-A", "ROUTE-B"),
            no_new_route_confirmation_ids=("CONFIRM-1", "CONFIRM-2"),
        )

    def test_fixpoint_creates_unresolved_gap_disposition(self) -> None:
        disposition = self._disposition()
        row = disposition.to_dict()
        self.assertEqual("UNRESOLVED_EVIDENCE_GAP", row["status"])
        self.assertEqual("CORROBORATION_CAP", row["gap_class"])
        self.assertTrue(row["query_lane_exhausted"])
        self.assertFalse(row["source_absence_proven"])
        self.assertEqual(
            "COMPONENT_MEMO_WITH_CONFIDENCE_PENALTY",
            row["downstream_action"],
        )
        restored = EvidenceGapDisposition.from_dict(row)
        self.assertEqual(disposition.disposition_id, restored.disposition_id)

    def test_disposition_reopens_only_on_real_state_change(self) -> None:
        disposition = self._disposition()
        same = self._assessment()
        self.assertIsNone(
            disposition.reopen_reason_for(candidate_key=same.key)
        )
        with self.assertRaisesRegex(ValueError, "real state change"):
            disposition.superseding_reopen(assessment=same)

        changed = self._assessment(lineage_hash="c" * 64)
        reopened = disposition.superseding_reopen(assessment=changed)
        self.assertEqual(
            "ACCEPTED_LINEAGE_ROSTER_CHANGED", reopened.reopen_reason
        )
        self.assertFalse(reopened.query_lane_exhausted)
        self.assertEqual(
            disposition.disposition_id,
            reopened.supersedes_disposition_id,
        )
        current = latest_evidence_gap_dispositions((disposition, reopened))
        self.assertEqual(
            reopened.disposition_id,
            current[reopened.key.semantic_gap_id].disposition_id,
        )

    def test_supervisor_paraphrase_does_not_reopen_disposition(self) -> None:
        disposition = self._disposition()
        first = self._assessment(
            supervisor_prose="고객 공식 계약 corroboration이 부족함"
        )
        second = self._assessment(
            supervisor_prose="named customer direct confirmation이 확인되지 않음"
        )
        self.assertEqual(first.key.gap_key, second.key.gap_key)
        self.assertIsNone(
            disposition.reopen_reason_for(candidate_key=second.key)
        )

    def test_quarantined_request_not_counted_as_current_pending(self) -> None:
        current = "COLLABREQ-" + "a" * 64
        residue = "COLLABREQ-" + "b" * 64
        result = canonical_current_pending_request_ids(
            pending_reasons=(
                "QUERY_PROVIDER_ERROR:COLLABORATION_RESPONSE_PENDING:" + current,
            ),
            request_ids=(current, residue),
            response_ids=(),
            quarantined_request_ids=(residue,),
        )
        self.assertEqual((current,), result)


class SemanticNoNewRouteFixpointTest(unittest.TestCase):
    def _assessment(self) -> EvidenceGapAssessment:
        key = EvidenceGapKey(
            target_id="TEST_TARGET",
            as_of_date="2026-07-12",
            archetype_id="TEST_ARCHETYPE",
            objective_identity="SGOBJ-stable123",
            affected_component_ids=(
                "information_confidence",
                "earnings_visibility",
            ),
            required_source_family=(
                "SOURCE_FAMILY_SET[CUSTOMER_OFFICIAL,PUBLIC_BROKER_PDF]"
            ),
            economic_mechanism_id="CUSTOMER_COMMITMENT_VISIBILITY",
            predicate_or_fact_need_id="DIRECT_CONTRACT_TERMS",
            fact_snapshot_hash="a" * 64,
            accepted_lineage_roster_hash="b" * 64,
        )
        return EvidenceGapAssessment.classify(
            key=key,
            missing_source_role=MissingSourceRole.INDEPENDENT_CORROBORATION,
            source_backed_component_ids=(
                "information_confidence",
                "earnings_visibility",
            ),
            component_range_bounded=True,
            could_change_score=True,
            could_change_stage=True,
            could_change_hard_break=False,
            economic_reason="독립 corroboration 미확인",
        )

    def _confirmation(
        self,
        ordinal: int,
        **overrides: object,
    ) -> NoNewRouteConfirmation:
        values: dict[str, object] = {
            "key": self._assessment().key,
            "prompt_hash": f"QUERYPROMPT-{ordinal}",
            "response_hash": f"QUERYRESP-{ordinal}",
            "request_id": "COLLABREQ-" + str(ordinal) * 64,
            "suggested_queries": (),
            "new_source_directions": (),
            "unresolved_research_notes": ("미확인 공백은 유지된다.",),
        }
        values.update(overrides)
        return NoNewRouteConfirmation(**values)  # type: ignore[arg-type]

    def test_two_independent_empty_confirmations_close_same_gap(self) -> None:
        assessment = self._assessment()
        fixpoint = SemanticNoNewRouteFixpoint(
            key=assessment.key,
            confirmations=(self._confirmation(1), self._confirmation(2)),
        )
        self.assertTrue(fixpoint.reached)
        self.assertEqual(2, fixpoint.valid_confirmation_count)
        disposition = fixpoint.create_disposition(
            assessment=assessment,
            attempted_route_signatures=("ROUTE-A", "ROUTE-B"),
        )
        self.assertTrue(disposition.query_lane_exhausted)
        self.assertEqual(2, len(disposition.no_new_route_confirmation_ids))

    def test_new_source_direction_prevents_fixpoint(self) -> None:
        fixpoint = SemanticNoNewRouteFixpoint(
            key=self._assessment().key,
            confirmations=(
                self._confirmation(1),
                self._confirmation(
                    2,
                    new_source_directions=("새 partner official filing 경로",),
                    concrete_untried_source_route_signatures=("ROUTE-C",),
                ),
            ),
        )
        self.assertFalse(fixpoint.reached)
        self.assertEqual(0, fixpoint.valid_confirmation_count)

    def test_provider_error_does_not_count_as_no_route(self) -> None:
        fixpoint = SemanticNoNewRouteFixpoint(
            key=self._assessment().key,
            confirmations=(
                self._confirmation(1),
                self._confirmation(2, provider_error=True),
            ),
        )
        self.assertFalse(fixpoint.reached)
        self.assertEqual(1, fixpoint.valid_confirmation_count)

    def test_parser_failure_does_not_count_as_no_route(self) -> None:
        fixpoint = SemanticNoNewRouteFixpoint(
            key=self._assessment().key,
            confirmations=(
                self._confirmation(1),
                self._confirmation(2, parser_or_fetch_repair_pending=True),
            ),
        )
        self.assertFalse(fixpoint.reached)
        self.assertEqual(1, fixpoint.valid_confirmation_count)

    def test_fixpoint_does_not_create_source_absence_fact(self) -> None:
        assessment = self._assessment()
        fixpoint = SemanticNoNewRouteFixpoint(
            key=assessment.key,
            confirmations=(self._confirmation(1), self._confirmation(2)),
        )
        disposition = fixpoint.create_disposition(
            assessment=assessment,
            attempted_route_signatures=("ROUTE-A",),
        )
        self.assertFalse(fixpoint.to_dict()["source_absence_proven"])
        self.assertFalse(disposition.to_dict()["source_absence_proven"])
        self.assertNotIn("facts", disposition.to_dict())

    def test_third_same_gap_query_is_hard_failure(self) -> None:
        assessment = self._assessment()
        fixpoint = SemanticNoNewRouteFixpoint(
            key=assessment.key,
            confirmations=(self._confirmation(1), self._confirmation(2)),
        )
        disposition = fixpoint.create_disposition(
            assessment=assessment,
            attempted_route_signatures=("ROUTE-A", "ROUTE-B"),
        )
        with self.assertRaisesRegex(
            RepeatedExhaustedGapReopenedError,
            "REPEATED_EXHAUSTED_GAP_REOPENED",
        ):
            guard_source_query_generation(
                disposition=disposition,
                candidate_key=assessment.key,
            )


if __name__ == "__main__":
    unittest.main()
