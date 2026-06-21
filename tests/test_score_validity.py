from datetime import date, datetime
from types import SimpleNamespace
import unittest

from e2r.models import ScoreSnapshot
from e2r.score_validity import (
    compare_score_state_rows,
    compare_score_states,
    find_score_state_contract_violations,
    is_score_valid,
    normalized_score_alias_value,
    normalized_score_state_mapping_if_present,
    normalized_score_state_payload,
    raw_score_total_before_block,
    research_input_fingerprint,
    score_block_reason,
    score_fingerprint,
    score_state_contract_violations,
    score_state_output_contract_violations,
    score_variability_drivers,
    serialized_score_block_reason,
    serialized_score_valid,
    serialized_visible_score,
    visible_score_total,
)


def _score(diagnostics):
    return ScoreSnapshot(
        symbol="005930",
        as_of_date=date(2026, 6, 12),
        eps_fcf_explosion_score=20,
        earnings_visibility_score=20,
        bottleneck_pricing_score=20,
        market_mispricing_score=15,
        valuation_rerating_score=15,
        capital_allocation_score=5,
        information_confidence_score=5,
        risk_penalty=0,
        total_score=100,
        diagnostic_scores=diagnostics,
    )


class ScoreValidityTests(unittest.TestCase):
    def test_score_block_flag_invalidates_even_when_score_valid_is_missing(self):
        score = _score({"score_blocked_by_score_gap": 100.0, "raw_score_total_before_score_gap_block": 68.9})

        self.assertFalse(is_score_valid(score))
        self.assertIsNone(visible_score_total(score))
        self.assertEqual(score_block_reason(score), "score_gap_unresolved")
        self.assertEqual(raw_score_total_before_block(score), 68.9)

    def test_raw_block_key_invalidates_and_preserves_specific_reason_when_block_flag_is_missing(self):
        score = _score({"raw_score_total_before_theme_route_block": 72.0})

        self.assertFalse(is_score_valid(score))
        self.assertIsNone(visible_score_total(score))
        self.assertEqual(score_block_reason(score), "theme_route_unresolved")
        self.assertEqual(raw_score_total_before_block(score), 72.0)

    def test_score_gap_raw_block_key_preserves_score_gap_reason(self):
        score = _score({"raw_score_total_before_score_gap_block": 83.0})

        self.assertFalse(is_score_valid(score))
        self.assertIsNone(visible_score_total(score))
        self.assertEqual(score_block_reason(score), "score_gap_unresolved")
        self.assertEqual(raw_score_total_before_block(score), 83.0)

    def test_asof_raw_block_key_preserves_asof_reason(self):
        score = _score({"raw_score_total_before_asof_web_block": 66.0})

        self.assertFalse(is_score_valid(score))
        self.assertIsNone(visible_score_total(score))
        self.assertEqual(score_block_reason(score), "asof_web_score_unresolved")
        self.assertEqual(raw_score_total_before_block(score), 66.0)

    def test_explicit_valid_score_remains_visible_without_block_markers(self):
        score = _score({"score_valid": 100.0})

        self.assertTrue(is_score_valid(score))
        self.assertEqual(visible_score_total(score), 100.0)
        self.assertIsNone(score_block_reason(score))
        self.assertIsNone(raw_score_total_before_block(score))

    def test_score_snapshot_without_score_valid_is_not_visible(self):
        score = _score({})

        self.assertFalse(is_score_valid(score))
        self.assertIsNone(visible_score_total(score))
        self.assertEqual(score_block_reason(score), "score_invalid")

    def test_score_fingerprint_is_stable_and_changes_when_evidence_changes(self):
        first = ScoreSnapshot(
            symbol="005930",
            as_of_date=date(2026, 6, 12),
            eps_fcf_explosion_score=20,
            earnings_visibility_score=20,
            bottleneck_pricing_score=20,
            market_mispricing_score=15,
            valuation_rerating_score=15,
            capital_allocation_score=5,
            information_confidence_score=5,
            risk_penalty=0,
            total_score=100,
            diagnostic_scores={"b": 2.0, "a": 1.0},
            evidence_ids=("ev-b", "ev-a"),
        )
        same = ScoreSnapshot(
            symbol="005930",
            as_of_date=date(2026, 6, 12),
            eps_fcf_explosion_score=20,
            earnings_visibility_score=20,
            bottleneck_pricing_score=20,
            market_mispricing_score=15,
            valuation_rerating_score=15,
            capital_allocation_score=5,
            information_confidence_score=5,
            risk_penalty=0,
            total_score=100,
            diagnostic_scores={"a": 1.0, "b": 2.0},
            evidence_ids=("ev-a", "ev-b"),
        )
        changed = ScoreSnapshot(
            symbol="005930",
            as_of_date=date(2026, 6, 12),
            eps_fcf_explosion_score=20,
            earnings_visibility_score=20,
            bottleneck_pricing_score=20,
            market_mispricing_score=15,
            valuation_rerating_score=15,
            capital_allocation_score=5,
            information_confidence_score=5,
            risk_penalty=0,
            total_score=100,
            diagnostic_scores={"a": 1.0, "b": 2.0},
            evidence_ids=("ev-a", "ev-c"),
        )

        self.assertEqual(score_fingerprint(first), score_fingerprint(same))
        self.assertNotEqual(score_fingerprint(first), score_fingerprint(changed))

    def test_score_variability_drivers_explain_invalid_and_missing_inputs(self):
        score = _score(
            {
                "score_blocked_by_score_gap": 100.0,
                "raw_score_total_before_score_gap_block": 68.9,
                "estimate_missing_fcf_source": 100.0,
                "estimate_missing_revision_source": 100.0,
                "estimate_conflict_count_capped": 2.0,
            }
        )

        drivers = score_variability_drivers(
            score,
            input_counts={"research_reports": 0, "consensus": 0, "consensus_revisions": 0, "agent_extracted_fields": 0},
            evidence_count=0,
            expansion_query_count=0,
        )

        self.assertIn("score_invalid:score_gap_unresolved", drivers)
        self.assertIn("raw_score_before_block:68.9", drivers)
        self.assertIn("estimate_source_missing:fcf", drivers)
        self.assertIn("estimate_source_missing:revision", drivers)
        self.assertIn("estimate_quality:estimate_conflict_count_capped=2", drivers)
        self.assertIn("input_missing:research_report", drivers)
        self.assertIn("input_missing:evidence", drivers)
        self.assertIn("llm_expansion_query_count:0", drivers)

    def test_score_variability_drivers_explain_valid_run_state(self):
        score = _score(
            {
                "score_valid": 100.0,
                "claim_backed_claim_count_capped": 6.0,
                "claim_backed_primitive_count_capped": 4.0,
                "score_claim_backed_component_count_capped": 7.0,
                "orphan_score_component_count_capped": 0.0,
                "score_claim_backed_component_ratio": 100.0,
            }
        )

        drivers = score_variability_drivers(
            score,
            route_diagnostics={
                "theme_rebalance_status": "completed",
                "theme_route_status": "transition_detected",
                "theme_evidence_gate_status": "source_backed",
                "large_sector_id": "R2_AI_SEMICONDUCTOR_ELECTRONICS",
                "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            },
            input_counts={
                "price_bars": 120,
                "financial_actuals": 3,
                "research_reports": 2,
                "news_items": 5,
                "consensus": 1,
                "consensus_revisions": 1,
                "agent_extracted_fields": 4,
            },
            evidence_count=9,
            expansion_query_count=6,
            scoring_canonical_archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
        )

        self.assertIn(
            "score_components:eps_fcf=20,visibility=20,bottleneck=20,mispricing=15,valuation=15,capital=5,confidence=5,risk=0,total=100",
            drivers,
        )
        self.assertIn(
            "route_state:rebalance=completed|route=transition_detected|gate=source_backed|sector=R2_AI_SEMICONDUCTOR_ELECTRONICS|route_archetype=C06_HBM_MEMORY_CUSTOMER_CAPACITY|scoring_archetype=C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            drivers,
        )
        self.assertIn("input_count:research_report=2", drivers)
        self.assertIn("input_count:news_item=5", drivers)
        self.assertIn("evidence_count:9", drivers)
        self.assertIn("score_evidence_count:0", drivers)
        self.assertIn("claim_backed_claim_count:6", drivers)
        self.assertIn("claim_backed_primitive_count:4", drivers)
        self.assertIn("score_claim_backed_component_count:7", drivers)
        self.assertIn("orphan_score_component_count:0", drivers)
        self.assertIn("score_claim_backed_component_ratio:100", drivers)
        self.assertIn("llm_expansion_query_count:6", drivers)

    def test_research_input_fingerprint_is_stable_and_changes_with_inputs(self):
        score = _score({"score_valid": 100.0})
        evidence_a = SimpleNamespace(
            evidence_id="ev-a",
            source_type="research_report",
            source_name="broker",
            symbol="005930",
            title="삼성전자 EPS 상향",
            url_or_identifier="https://example.com/a",
            published_at=datetime(2026, 6, 10, 9, 0),
            available_at=datetime(2026, 6, 10, 9, 0),
            excerpt_or_value="EPS +20%",
            parsed_fields={"eps_revision_pct": 20},
        )
        evidence_b = SimpleNamespace(
            evidence_id="ev-b",
            source_type="news",
            source_name="news",
            symbol="005930",
            title="HBM 공급",
            url_or_identifier="https://example.com/b",
            published_at=datetime(2026, 6, 11, 9, 0),
            available_at=datetime(2026, 6, 11, 9, 0),
            excerpt_or_value="HBM 공급 확대",
            parsed_fields={"contract_visibility": "high"},
        )

        first = research_input_fingerprint(
            score=score,
            evidence=(evidence_b, evidence_a),
            queries=("삼성전자 EPS 상향", "삼성전자 HBM 공급"),
            input_counts={"research_reports": 1, "news_items": 1},
        )
        same = research_input_fingerprint(
            score=score,
            evidence=(evidence_a, evidence_b),
            queries=("삼성전자 EPS 상향", "삼성전자 HBM 공급"),
            input_counts={"news_items": 1, "research_reports": 1},
        )
        changed = research_input_fingerprint(
            score=score,
            evidence=(evidence_a, evidence_b),
            queries=("삼성전자 EPS 상향", "삼성전자 HBM 공급 장기계약"),
            input_counts={"news_items": 1, "research_reports": 1},
        )

        self.assertEqual(first, same)
        self.assertNotEqual(first, changed)

    def test_score_variability_drivers_include_input_fingerprint_when_present(self):
        score = _score({"score_valid": 100.0})

        drivers = score_variability_drivers(score, input_fingerprint="abc123")

        self.assertIn("research_input_fingerprint:abc123", drivers)

    def test_compare_score_states_classifies_input_changed_score_move(self):
        comparison = compare_score_states(
            {
                "visible_score": 82,
                "score_valid": True,
                "score_fingerprint": "score-a",
                "research_input_fingerprint": "input-a",
            },
            {
                "visible_score": 65,
                "score_valid": True,
                "score_fingerprint": "score-b",
                "research_input_fingerprint": "input-b",
            },
        )

        self.assertEqual(comparison.status, "input_changed")
        self.assertEqual(comparison.visible_score_delta, -17)
        self.assertIn("visible_score_delta:-17", comparison.drivers)
        self.assertIn("score_fingerprint_changed", comparison.drivers)
        self.assertIn("research_input_fingerprint_changed", comparison.drivers)

    def test_compare_score_states_classifies_same_input_scoring_change(self):
        comparison = compare_score_states(
            {
                "visible_score": 82,
                "score_valid": True,
                "score_fingerprint": "score-a",
                "research_input_fingerprint": "input-a",
            },
            {
                "visible_score": 65,
                "score_valid": True,
                "score_fingerprint": "score-b",
                "research_input_fingerprint": "input-a",
            },
        )

        self.assertEqual(comparison.status, "scoring_changed_same_input")
        self.assertIn("research_input_fingerprint_same", comparison.drivers)
        self.assertIn("score_fingerprint_changed", comparison.drivers)

    def test_compare_score_states_flags_inconsistent_output_when_same_score_fingerprint_moves(self):
        comparison = compare_score_states(
            {
                "visible_score": 82,
                "score_valid": True,
                "score_fingerprint": "score-a",
                "research_input_fingerprint": "input-a",
            },
            {
                "visible_score": 65,
                "score_valid": True,
                "score_fingerprint": "score-a",
                "research_input_fingerprint": "input-a",
            },
        )

        self.assertEqual(comparison.status, "inconsistent_output_same_score_fingerprint")
        self.assertIn("score_fingerprint_same", comparison.drivers)

    def test_compare_score_states_blocks_compat_score_without_visible_score(self):
        comparison = compare_score_states(
            {
                "score": 82,
                "score_valid": True,
                "score_fingerprint": "score-a",
                "research_input_fingerprint": "input-a",
            },
            {
                "visible_score": 82,
                "score_total": 12,
                "score_valid": True,
                "score_fingerprint": "score-a",
                "research_input_fingerprint": "input-a",
            },
        )

        self.assertEqual(comparison.status, "score_became_valid")
        self.assertIsNone(comparison.visible_score_before)
        self.assertEqual(comparison.visible_score_after, 82)
        self.assertIn("before_visible_score_ignored:compat_score_without_visible_score", comparison.drivers)
        self.assertIn("before_score_state_contract:valid_visible_score_missing", comparison.drivers)
        self.assertIn("after_score_state_contract:valid_score_alias_mismatch:score_total", comparison.drivers)
        self.assertNotIn("after_visible_score_alias:score_total", comparison.drivers)

    def test_compare_score_states_blocks_conflicting_compat_aliases_without_visible_score(self):
        comparison = compare_score_states(
            {
                "score": 82,
                "score_total": 90,
                "score_valid": True,
                "score_fingerprint": "legacy-conflict",
                "research_input_fingerprint": "input-a",
            },
            {
                "visible_score": 65,
                "score_valid": True,
                "score_fingerprint": "valid-score",
                "research_input_fingerprint": "input-a",
            },
        )

        self.assertEqual(comparison.status, "score_became_valid")
        self.assertIsNone(comparison.visible_score_before)
        self.assertEqual(comparison.visible_score_after, 65)
        self.assertIsNone(comparison.visible_score_delta)
        self.assertIn("before_visible_score_ignored:score_alias_conflict_without_visible_score", comparison.drivers)
        self.assertIn("score_valid_changed:False->True", comparison.drivers)
        self.assertIn("score_blocked_reason_changed:score_alias_conflict->none", comparison.drivers)
        self.assertIn("before_score_state_contract:score_alias_conflict", comparison.drivers)
        self.assertIn("before_score_state_contract:valid_visible_score_missing", comparison.drivers)

    def test_compare_score_states_blocks_conflicting_visible_aliases_without_visible_score(self):
        comparison = compare_score_states(
            {
                "current_score": 82,
                "merged_score": 65,
                "score_valid": True,
                "score_fingerprint": "legacy-conflict",
                "research_input_fingerprint": "input-a",
            },
            {
                "visible_score": 65,
                "score_valid": True,
                "score_fingerprint": "valid-score",
                "research_input_fingerprint": "input-a",
            },
        )

        self.assertEqual(comparison.status, "score_became_valid")
        self.assertIsNone(comparison.visible_score_before)
        self.assertEqual(comparison.visible_score_after, 65)
        self.assertIn("before_visible_score_ignored:score_alias_conflict_without_visible_score", comparison.drivers)
        self.assertIn("score_valid_changed:False->True", comparison.drivers)
        self.assertIn("score_blocked_reason_changed:score_alias_conflict->none", comparison.drivers)
        self.assertIn("before_score_state_contract:score_alias_conflict", comparison.drivers)
        self.assertIn("before_score_state_contract:valid_score_alias_mismatch:merged_score", comparison.drivers)

    def test_compare_score_states_reports_pending_transition_and_missing_fingerprints(self):
        comparison = compare_score_states(
            {"visible_score": 74, "score_valid": True},
            {"visible_score": None, "score_valid": False, "score_blocked_reason": "score_gap_unresolved"},
        )

        self.assertEqual(comparison.status, "score_became_invalid")
        self.assertIn("score_valid_changed:True->False", comparison.drivers)
        self.assertIn("score_blocked_reason_changed:none->score_gap_unresolved", comparison.drivers)
        self.assertIn("score_fingerprint_missing", comparison.drivers)
        self.assertIn("research_input_fingerprint_missing", comparison.drivers)

    def test_compare_score_states_ignores_compat_score_when_state_is_invalid(self):
        comparison = compare_score_states(
            {
                "score": 82,
                "score_total": 82,
                "score_valid": False,
                "score_blocked_reason": "score_gap_unresolved",
                "raw_score_before_block": 82,
                "score_fingerprint": "raw-blocked-score",
                "research_input_fingerprint": "input-a",
            },
            {
                "visible_score": 65,
                "score_valid": True,
                "score_fingerprint": "valid-score",
                "research_input_fingerprint": "input-b",
            },
        )

        self.assertIsNone(comparison.visible_score_before)
        self.assertEqual(comparison.visible_score_after, 65)
        self.assertIsNone(comparison.visible_score_delta)
        self.assertIn("before_visible_score_ignored:score_valid_false_without_visible_score", comparison.drivers)
        self.assertIn("score_valid_changed:False->True", comparison.drivers)

    def test_compare_score_states_ignores_visible_score_when_state_is_marked_invalid(self):
        comparison = compare_score_states(
            {
                "visible_score": 82,
                "score_valid": False,
                "score_blocked_reason": "score_gap_unresolved",
                "score_fingerprint": "invalid-score",
                "research_input_fingerprint": "input-a",
            },
            {
                "visible_score": None,
                "score_valid": False,
                "score_blocked_reason": "score_gap_unresolved",
                "score_fingerprint": "invalid-score",
                "research_input_fingerprint": "input-a",
            },
        )

        self.assertIsNone(comparison.visible_score_before)
        self.assertIsNone(comparison.visible_score_after)
        self.assertEqual(comparison.status, "same_score_snapshot")
        self.assertIn("before_visible_score_ignored:visible_score_ignored_score_valid_false", comparison.drivers)

    def test_compare_score_states_ignores_compat_score_when_block_reason_marks_invalid(self):
        comparison = compare_score_states(
            {
                "score": 82,
                "score_blocked_reason": "score_gap_unresolved",
                "score_fingerprint": "blocked-score",
                "research_input_fingerprint": "input-a",
            },
            {
                "visible_score": 65,
                "score_valid": True,
                "score_fingerprint": "valid-score",
                "research_input_fingerprint": "input-b",
            },
        )

        self.assertIsNone(comparison.visible_score_before)
        self.assertEqual(comparison.visible_score_after, 65)
        self.assertIsNone(comparison.visible_score_delta)
        self.assertIn("before_visible_score_ignored:score_blocked_reason_without_visible_score", comparison.drivers)

    def test_compare_score_states_ignores_compat_score_when_raw_block_marker_exists(self):
        comparison = compare_score_states(
            {
                "total_score": 82,
                "raw_score_before_block": 82,
                "score_fingerprint": "blocked-score",
                "research_input_fingerprint": "input-a",
            },
            {
                "visible_score": 65,
                "score_valid": True,
                "score_fingerprint": "valid-score",
                "research_input_fingerprint": "input-b",
            },
        )

        self.assertIsNone(comparison.visible_score_before)
        self.assertEqual(comparison.visible_score_after, 65)
        self.assertIsNone(comparison.visible_score_delta)
        self.assertIn("before_visible_score_ignored:raw_score_before_block_without_visible_score", comparison.drivers)

    def test_compare_score_states_treats_score_without_validity_as_pending(self):
        comparison = compare_score_states(
            {
                "score": 82,
                "score_fingerprint": "old-score",
                "research_input_fingerprint": "input-a",
            },
            {
                "visible_score": 65,
                "score_valid": True,
                "score_fingerprint": "new-score",
                "research_input_fingerprint": "input-b",
            },
        )

        self.assertIsNone(comparison.visible_score_before)
        self.assertEqual(comparison.visible_score_after, 65)
        self.assertIsNone(comparison.visible_score_delta)
        self.assertIn("before_visible_score_ignored:score_valid_missing_without_visible_score", comparison.drivers)

    def test_serialized_visible_score_uses_same_invalid_marker_guard(self):
        self.assertIsNone(serialized_visible_score({"score": 82, "score_valid": True}))
        self.assertIsNone(serialized_visible_score({"score": 82, "score_valid": False}))
        self.assertIsNone(serialized_visible_score({"score": 82, "score_blocked_reason": "score_gap_unresolved"}))
        self.assertIsNone(serialized_visible_score({"total_score": 82, "raw_score_before_block": 82}))
        self.assertIsNone(serialized_visible_score({"score": 82}))
        self.assertIsNone(serialized_visible_score({"visible_score": 82}))
        self.assertIsNone(serialized_visible_score({"score": 82, "score_total": 90, "score_valid": True}))
        self.assertIsNone(serialized_visible_score({"current_score": 82, "merged_score": 65, "score_valid": True}))
        self.assertIsNone(serialized_visible_score({"score": "not-a-score", "score_valid": True}))

    def test_serialized_score_valid_and_reason_match_visible_score_contract(self):
        self.assertFalse(serialized_score_valid({"score": 82, "score_valid": True}))
        self.assertEqual(serialized_score_block_reason({"score": 82, "score_valid": True}), "visible_score_missing")
        self.assertFalse(serialized_score_valid({"score": 82, "score_valid": False}))
        self.assertEqual(
            serialized_score_block_reason({"score": 82, "score_valid": False, "score_blocked_reason": "score_gap_unresolved"}),
            "score_gap_unresolved",
        )
        self.assertFalse(serialized_score_valid({"score": 82}))
        self.assertEqual(serialized_score_block_reason({"score": 82}), "score_valid_missing")
        self.assertFalse(serialized_score_valid({"score": 82, "score_total": 90, "score_valid": True}))
        self.assertEqual(
            serialized_score_block_reason({"score": 82, "score_total": 90, "score_valid": True}),
            "score_alias_conflict",
        )
        self.assertFalse(serialized_score_valid({"score": "not-a-score", "score_valid": True}))
        self.assertEqual(
            serialized_score_block_reason({"score": "not-a-score", "score_valid": True}),
            "score_alias_not_numeric",
        )

    def test_serialized_visible_score_parses_score_valid_numbers_strictly(self):
        self.assertEqual(serialized_visible_score({"visible_score": 82, "score_valid": 100.0}), 82)
        self.assertEqual(serialized_visible_score({"visible_score": 82, "score_valid": "100.0"}), 82)
        self.assertIsNone(serialized_visible_score({"score": 82, "score_valid": 0.0}))
        self.assertIsNone(serialized_visible_score({"score": 82, "score_valid": "0.0"}))
        self.assertIsNone(serialized_visible_score({"score": 82, "score_valid": -1}))
        self.assertIsNone(serialized_visible_score({"score": 82, "score_valid": "-1"}))
        self.assertIsNone(serialized_visible_score({"score": 82, "score_valid": "unknown"}))

    def test_score_state_contract_violations_flag_invalid_visible_and_compat_scores(self):
        self.assertEqual(
            score_state_contract_violations(
                {
                    "visible_score": 65,
                    "score": 65,
                    "score_valid": True,
                    "score_fingerprint": "valid-score",
                    "research_input_fingerprint": "input-a",
                }
            ),
            (),
        )
        self.assertEqual(
            score_state_contract_violations(
                {
                    "visible_score": 82,
                    "current_score": 82,
                    "merged_score": 82,
                    "score_total": 82,
                    "score_valid": False,
                    "score_blocked_reason": "score_gap_unresolved",
                    "raw_score_before_block": 82,
                }
            ),
            (
                "invalid_visible_score_present",
                "invalid_visible_score_alias_present:current_score",
                "invalid_visible_score_alias_present:merged_score",
                "invalid_compat_score_present:score_total",
            ),
        )
        self.assertEqual(
            score_state_contract_violations(
                {
                    "score": 82,
                    "score_blocked_reason": "theme_route_unresolved",
                }
            ),
            ("invalid_compat_score_present:score",),
        )
        self.assertEqual(
            score_state_contract_violations({"score": 82}),
            ("invalid_compat_score_present:score",),
        )
        self.assertEqual(
            score_state_contract_violations({"visible_score": 82}),
            ("invalid_visible_score_present",),
        )

    def test_score_state_contract_violations_flag_valid_rows_missing_visible_score(self):
        self.assertEqual(
            score_state_contract_violations(
                {
                    "score": 65,
                    "score_valid": True,
                }
            ),
            ("valid_visible_score_missing",),
        )
        self.assertEqual(
            score_state_contract_violations(
                {
                    "visible_score": 65,
                    "score_valid": True,
                    "raw_score_before_block": 82,
                }
            ),
            ("valid_raw_block_marker_present:raw_score_before_block", "invalid_visible_score_present"),
        )

    def test_score_state_contract_violations_flag_high_confidence_orphan_claim_score(self):
        self.assertIn(
            "valid_high_confidence_claim_backed_gap",
            score_state_contract_violations(
                {
                    "stage": "3-Green",
                    "visible_score": 92.0,
                    "score_valid": True,
                    "evidence_contract_required_primitive_count": 6,
                    "claim_backed_claim_count": 0,
                    "score_claim_backed_component_ratio": 0,
                    "orphan_score_component_count": 7,
                }
            ),
        )
        self.assertIn(
            "valid_high_confidence_claim_backed_gap",
            score_state_contract_violations(
                {
                    "stage": "2",
                    "visible_score": 70.0,
                    "score_valid": True,
                    "source_backed_green_bridge_raw": 90,
                    "claim_backed_claim_count": 3,
                    "score_claim_backed_component_ratio": 80,
                    "orphan_score_component_count": 1,
                }
            ),
        )
        self.assertNotIn(
            "valid_high_confidence_claim_backed_gap",
            score_state_contract_violations(
                {
                    "stage": "1",
                    "visible_score": 12.0,
                    "score_valid": True,
                    "evidence_contract_required_primitive_count": 6,
                    "claim_backed_claim_count": 0,
                    "score_claim_backed_component_ratio": 0,
                    "orphan_score_component_count": 7,
                }
            ),
        )

    def test_score_state_contract_violations_require_component_claim_id_output(self):
        high_confidence_row = {
            "stage": "3-Green",
            "visible_score": 92.0,
            "score_valid": True,
            "evidence_contract_required_primitive_count": 6,
            "claim_backed_claim_count": 4,
            "score_claim_backed_component_ratio": 100,
            "orphan_score_component_count": 0,
            "eps_fcf_explosion_score": 20,
            "earnings_visibility_score": 18,
            "bottleneck_pricing_score": 0,
        }

        self.assertIn(
            "valid_high_confidence_score_contribution_claim_ids_missing",
            score_state_contract_violations(high_confidence_row),
        )
        self.assertIn(
            "valid_high_confidence_score_contribution_claim_ids_missing",
            score_state_contract_violations(
                {
                    **high_confidence_row,
                    "score_contribution_claim_ids": {
                        "eps_fcf_explosion": ["CLM-EPS"],
                    },
                }
            ),
        )
        self.assertNotIn(
            "valid_high_confidence_score_contribution_claim_ids_missing",
            score_state_contract_violations(
                {
                    **high_confidence_row,
                    "score_contribution_claim_ids": {
                        "eps_fcf_explosion": ["CLM-EPS"],
                        "earnings_visibility": ["CLM-VIS"],
                    },
                }
            ),
        )
        self.assertNotIn(
            "valid_high_confidence_score_contribution_claim_ids_missing",
            score_state_contract_violations(
                {
                    **high_confidence_row,
                    "score_contribution_claim_ids": "{\"eps_fcf_explosion\":[\"CLM-EPS\"],\"earnings_visibility\":[\"CLM-VIS\"]}",
                }
            ),
        )

    def test_score_state_contract_violations_require_score_contribution_ledger_output(self):
        high_confidence_row = {
            "stage": "3-Green",
            "visible_score": 92.0,
            "score_valid": True,
            "evidence_contract_required_primitive_count": 6,
            "claim_backed_claim_count": 4,
            "score_claim_backed_component_ratio": 100,
            "orphan_score_component_count": 0,
            "eps_fcf_explosion_score": 20,
            "earnings_visibility_score": 18,
            "score_contribution_claim_ids": {
                "eps_fcf_explosion": ["CLM-EPS"],
                "earnings_visibility": ["CLM-VIS"],
            },
        }

        self.assertIn(
            "valid_high_confidence_score_contribution_ledger_missing",
            score_state_contract_violations(high_confidence_row),
        )
        self.assertIn(
            "valid_high_confidence_score_contribution_ledger_missing",
            score_state_contract_violations(
                {
                    **high_confidence_row,
                    "score_contribution_ledger": [
                        {
                            "component_key": "eps_fcf_explosion",
                            "raw_points": 20,
                            "max_points": 20,
                            "support_claim_ids": ["CLM-EPS"],
                        },
                        {
                            "component_key": "earnings_visibility",
                            "raw_points": 18,
                            "max_points": 20,
                            "support_claim_ids": [],
                        },
                    ],
                }
            ),
        )
        self.assertNotIn(
            "valid_high_confidence_score_contribution_ledger_missing",
            score_state_contract_violations(
                {
                    **high_confidence_row,
                    "score_contribution_ledger": [
                        {
                            "component_key": "eps_fcf_explosion",
                            "raw_points": 20,
                            "max_points": 20,
                            "support_claim_ids": ["CLM-EPS"],
                        },
                        {
                            "component_key": "earnings_visibility",
                            "raw_points": 18,
                            "max_points": 20,
                            "support_claim_ids": ["CLM-VIS"],
                        },
                    ],
                }
            ),
        )
        self.assertNotIn(
            "valid_high_confidence_score_contribution_ledger_missing",
            score_state_contract_violations(
                {
                    **high_confidence_row,
                    "score_contribution_ledger": "[{\"component_key\":\"eps_fcf_explosion\",\"raw_points\":20,\"max_points\":20,\"support_claim_ids\":[\"CLM-EPS\"]},{\"component_key\":\"earnings_visibility\",\"raw_points\":18,\"max_points\":20,\"support_claim_ids\":[\"CLM-VIS\"]}]",
                }
            ),
        )

    def test_score_state_contract_violations_require_contribution_claims_in_claim_ledger(self):
        high_confidence_row = {
            "stage": "3-Green",
            "visible_score": 92.0,
            "score_valid": True,
            "evidence_contract_required_primitive_count": 6,
            "claim_backed_claim_count": 4,
            "score_claim_backed_component_ratio": 100,
            "orphan_score_component_count": 0,
            "eps_fcf_explosion_score": 20,
            "earnings_visibility_score": 18,
            "score_contribution_claim_ids": {
                "eps_fcf_explosion": ["CLM-EPS"],
                "earnings_visibility": ["CLM-VIS"],
            },
            "score_contribution_ledger": [
                {
                    "component_key": "eps_fcf_explosion",
                    "raw_points": 20,
                    "max_points": 20,
                    "support_claim_ids": ["CLM-EPS"],
                },
                {
                    "component_key": "earnings_visibility",
                    "raw_points": 18,
                    "max_points": 20,
                    "support_claim_ids": ["CLM-VIS"],
                },
            ],
        }

        self.assertIn(
            "valid_high_confidence_claim_ledger_ids_missing",
            score_state_contract_violations(high_confidence_row),
        )
        self.assertIn(
            "valid_high_confidence_score_contribution_claim_ids_unknown",
            score_state_contract_violations(
                {
                    **high_confidence_row,
                    "claim_ledger_claim_ids": ["CLM-EPS"],
                }
            ),
        )
        self.assertNotIn(
            "valid_high_confidence_score_contribution_claim_ids_unknown",
            score_state_contract_violations(
                {
                    **high_confidence_row,
                    "claim_ledger_claim_ids": ["CLM-EPS", "CLM-VIS"],
                }
            ),
        )
        self.assertNotIn(
            "valid_high_confidence_score_contribution_claim_ids_unknown",
            score_state_contract_violations(
                {
                    **high_confidence_row,
                    "claim_ledger_claim_ids_by_primitive": "{\"actual_eps_yoy_pct\":[\"CLM-EPS\"],\"revenue_visibility_contract\":[\"CLM-VIS\"]}",
                }
            ),
        )

    def test_score_state_contract_violations_flag_stage3_green_unverified_guard_primitives(self):
        row = {
            "stage": "3-Green",
            "visible_score": 92.0,
            "score_valid": True,
            "evidence_contract_required_primitive_count": 5,
            "evidence_contract_guard_missing_primitive_count": 1,
            "claim_backed_claim_count": 7,
            "score_claim_backed_component_ratio": 100,
            "orphan_score_component_count": 0,
            "claim_ledger_claim_ids": ["CLM-EPS"],
            "eps_fcf_explosion_score": 20,
            "score_contribution_claim_ids": {"eps_fcf_explosion": ["CLM-EPS"]},
            "score_contribution_ledger": [
                {
                    "component_key": "eps_fcf_explosion",
                    "raw_points": 20,
                    "max_points": 20,
                    "support_claim_ids": ["CLM-EPS"],
                }
            ],
        }

        self.assertIn(
            "valid_stage3_green_guard_primitives_unverified",
            score_state_contract_violations(row),
        )

    def test_score_state_contract_violations_flag_stage3_green_present_guard_primitives(self):
        row = {
            "stage": "3-Green",
            "visible_score": 92.0,
            "score_valid": True,
            "evidence_contract_required_primitive_count": 5,
            "evidence_contract_guard_present_primitive_count": 1,
            "evidence_contract_guard_missing_primitive_count": 0,
            "claim_backed_claim_count": 7,
            "score_claim_backed_component_ratio": 100,
            "orphan_score_component_count": 0,
            "claim_ledger_claim_ids": ["CLM-EPS"],
            "eps_fcf_explosion_score": 20,
            "score_contribution_claim_ids": {"eps_fcf_explosion": ["CLM-EPS"]},
            "score_contribution_ledger": [
                {
                    "component_key": "eps_fcf_explosion",
                    "raw_points": 20,
                    "max_points": 20,
                    "support_claim_ids": ["CLM-EPS"],
                }
            ],
        }

        self.assertIn(
            "valid_stage3_green_guard_primitives_present",
            score_state_contract_violations(row),
        )
        self.assertNotIn(
            "valid_stage3_green_guard_primitives_unverified",
            score_state_contract_violations({**row, "stage": "3-Yellow"}),
        )

    def test_normalized_score_state_payload_removes_invalid_visible_and_compat_scores(self):
        payload = normalized_score_state_payload(
            {
                "symbol": "005930",
                "visible_score": 83,
                "current_score": 83,
                "merged_score": 83,
                "score": 83,
                "score_total": 83,
                "total_score": 83,
                "score_valid": False,
                "score_blocked_reason": "score_gap_unresolved",
                "raw_score_before_block": 83,
            }
        )

        self.assertIsNone(payload["visible_score"])
        self.assertIsNone(payload["current_score"])
        self.assertIsNone(payload["merged_score"])
        self.assertIsNone(payload["score"])
        self.assertIsNone(payload["score_total"])
        self.assertIsNone(payload["total_score"])
        self.assertEqual(payload["raw_score_before_block"], 83)
        self.assertEqual(score_state_contract_violations(payload), ())

    def test_normalized_score_state_payload_removes_ambiguous_score_without_validity(self):
        payload = normalized_score_state_payload(
            {
                "symbol": "005930",
                "score": 83,
                "visible_score": 83,
                "current_score": 83,
            }
        )

        self.assertIsNone(payload["score"])
        self.assertIsNone(payload["visible_score"])
        self.assertIsNone(payload["current_score"])
        self.assertEqual(score_state_contract_violations(payload), ())

    def test_normalized_score_state_payload_blocks_compat_score_without_visible_score(self):
        payload = normalized_score_state_payload(
            {
                "symbol": "005930",
                "score": 65,
                "score_valid": True,
            }
        )

        self.assertIsNone(payload["score"])
        self.assertIsNone(payload["visible_score"])
        self.assertFalse(payload["score_valid"])
        self.assertEqual(payload["score_blocked_reason"], "visible_score_missing")
        self.assertEqual(score_state_contract_violations(payload), ())

    def test_normalized_score_state_payload_reconciles_conflicting_valid_aliases(self):
        payload = normalized_score_state_payload(
            {
                "symbol": "005930",
                "visible_score": 65,
                "score": 82,
                "score_total": 90,
                "total_score": 77,
                "current_score": 71,
                "merged_score": 68,
                "score_valid": True,
            }
        )

        self.assertEqual(payload["visible_score"], 65)
        self.assertEqual(payload["score"], 65)
        self.assertEqual(payload["score_total"], 65)
        self.assertEqual(payload["total_score"], 65)
        self.assertEqual(payload["current_score"], 65)
        self.assertEqual(payload["merged_score"], 65)
        self.assertEqual(score_state_contract_violations(payload), ())

    def test_normalized_score_state_payload_blocks_conflicting_compat_aliases_without_visible_score(self):
        payload = normalized_score_state_payload(
            {
                "symbol": "005930",
                "score": 82,
                "score_total": 90,
                "total_score": 82,
                "score_valid": True,
            }
        )

        self.assertFalse(payload["score_valid"])
        self.assertEqual(payload["score_blocked_reason"], "score_alias_conflict")
        self.assertIsNone(payload["visible_score"])
        self.assertIsNone(payload["score"])
        self.assertIsNone(payload["score_total"])
        self.assertIsNone(payload["total_score"])
        self.assertEqual(score_state_contract_violations(payload), ())

    def test_normalized_score_state_payload_blocks_conflicting_visible_aliases_without_visible_score(self):
        payload = normalized_score_state_payload(
            {
                "symbol": "005930",
                "current_score": 82,
                "merged_score": 65,
                "score": 65,
                "score_valid": True,
            }
        )

        self.assertFalse(payload["score_valid"])
        self.assertEqual(payload["score_blocked_reason"], "score_alias_conflict")
        self.assertIsNone(payload["visible_score"])
        self.assertIsNone(payload["current_score"])
        self.assertIsNone(payload["merged_score"])
        self.assertIsNone(payload["score"])
        self.assertEqual(score_state_contract_violations(payload), ())

    def test_normalized_score_state_payload_blocks_nonnumeric_valid_score(self):
        payload = normalized_score_state_payload(
            {
                "symbol": "005930",
                "score": "not-a-score",
                "score_valid": True,
            }
        )

        self.assertFalse(payload["score_valid"])
        self.assertEqual(payload["score_blocked_reason"], "score_alias_not_numeric")
        self.assertIsNone(payload["visible_score"])
        self.assertIsNone(payload["score"])
        self.assertEqual(score_state_contract_violations(payload), ())

    def test_normalized_score_state_payload_keeps_visible_valid_and_reason_consistent_across_alias_cases(self):
        cases = (
            (
                "single_compat_score",
                {"score": 82, "score_valid": True},
                False,
                None,
                "visible_score_missing",
            ),
            (
                "matching_compat_aliases",
                {"score": 82, "score_total": 82, "total_score": 82, "score_valid": True},
                False,
                None,
                "visible_score_missing",
            ),
            (
                "explicit_visible_wins",
                {"visible_score": 65, "score": 82, "score_total": 90, "score_valid": True},
                True,
                65,
                None,
            ),
            (
                "merged_alias_promotes_to_visible",
                {"merged_score": 65, "score_valid": True},
                True,
                65,
                None,
            ),
            (
                "missing_visible_score",
                {"score": None, "score_valid": True},
                False,
                None,
                "visible_score_missing",
            ),
            (
                "score_without_validity",
                {"score": 82},
                False,
                None,
                "score_valid_missing",
            ),
            (
                "explicit_invalid",
                {"score": 82, "score_valid": False, "score_blocked_reason": "score_gap_unresolved"},
                False,
                None,
                "score_gap_unresolved",
            ),
            (
                "compat_alias_conflict",
                {"score": 82, "score_total": 90, "score_valid": True},
                False,
                None,
                "score_alias_conflict",
            ),
            (
                "visible_alias_conflict",
                {"current_score": 82, "merged_score": 65, "score_valid": True},
                False,
                None,
                "score_alias_conflict",
            ),
            (
                "nonnumeric_score",
                {"score": "not-a-score", "score_valid": True},
                False,
                None,
                "score_alias_not_numeric",
            ),
            (
                "raw_block_marker_with_valid_true",
                {"score": 82, "score_valid": True, "raw_score_before_block": 82},
                False,
                None,
                "raw_score_before_block",
            ),
            (
                "score_gap_raw_marker_with_valid_true",
                {"score": 82, "score_valid": True, "raw_score_total_before_score_gap_block": 82},
                False,
                None,
                "score_gap_unresolved",
            ),
        )
        score_aliases = ("visible_score", "current_score", "merged_score", "score", "score_total", "total_score")

        for name, raw, expected_valid, expected_visible, expected_reason in cases:
            with self.subTest(name=name):
                payload = normalized_score_state_payload(raw)

                self.assertEqual(serialized_visible_score(payload), expected_visible)
                self.assertEqual(serialized_score_valid(payload), expected_valid)
                self.assertEqual(serialized_score_block_reason(payload), expected_reason)
                self.assertEqual(score_state_contract_violations(payload), ())
                if expected_valid:
                    self.assertEqual(payload["visible_score"], expected_visible)
                    for key in score_aliases:
                        if key in payload and payload[key] not in (None, ""):
                            self.assertEqual(payload[key], expected_visible)
                else:
                    self.assertIsNone(payload.get("visible_score"))
                    for key in score_aliases:
                        if key in payload:
                            self.assertIsNone(payload[key])

    def test_find_score_state_contract_violations_scans_nested_outputs_without_ranking_score_false_positive(self):
        payload = {
            "search_results": [
                {"title": "ranked result", "score": 0.92},
            ],
            "candidates": [
                {
                    "symbol": "005930",
                    "visible_score": 65,
                    "score_total": 12,
                    "score_valid": True,
                },
                {
                    "symbol": "000660",
                    "score": 82,
                },
            ],
            "diagnostics": {
                "score_valid": True,
            },
        }

        default_findings = find_score_state_contract_violations(payload)
        strict_findings = find_score_state_contract_violations(payload, include_score_only=True)
        strict_output_findings = find_score_state_contract_violations(
            payload,
            include_score_only=True,
            require_visible_score_field=True,
        )

        self.assertEqual(
            [(item.path, item.violation) for item in default_findings],
            [("$.candidates[0]", "valid_score_alias_mismatch:score_total")],
        )
        self.assertEqual(
            [(item.path, item.violation) for item in strict_findings],
            [
                ("$.candidates[0]", "valid_score_alias_mismatch:score_total"),
                ("$.candidates[1]", "invalid_compat_score_present:score"),
            ],
        )
        self.assertEqual(
            [(item.path, item.violation) for item in strict_output_findings],
            [
                ("$.candidates[0]", "valid_score_alias_mismatch:score_total"),
                ("$.candidates[1]", "invalid_compat_score_present:score"),
                ("$.candidates[1]", "visible_score_field_missing"),
            ],
        )

    def test_score_state_output_contract_requires_visible_score_field(self):
        self.assertEqual(
            score_state_output_contract_violations(
                {
                    "symbol": "005930",
                    "stage": "0",
                    "score_valid": False,
                    "score_blocked_reason": "theme_route_provider_error",
                }
            ),
            ("visible_score_field_missing",),
        )
        self.assertEqual(
            score_state_output_contract_violations(
                {
                    "symbol": "005930",
                    "stage": "0",
                    "visible_score": None,
                    "score_valid": False,
                    "score_blocked_reason": "theme_route_provider_error",
                }
            ),
            (),
        )

    def test_normalized_score_state_mapping_if_present_only_normalizes_score_rows(self):
        diagnostic = normalized_score_state_mapping_if_present(
            {
                "score_valid": False,
                "raw_score_total_before_score_gap_block": 82,
            }
        )
        score_row = normalized_score_state_mapping_if_present(
            {
                "score": 82,
                "score_valid": False,
                "score_blocked_reason": "score_gap_unresolved",
            }
        )

        self.assertNotIn("visible_score", diagnostic)
        self.assertIsNone(score_row["score"])
        self.assertIsNone(score_row["visible_score"])

    def test_normalized_score_state_mapping_if_present_normalizes_block_markers_without_score_valid(self):
        blocked_reason_row = normalized_score_state_mapping_if_present(
            {
                "score": 82,
                "score_blocked_reason": "score_gap_unresolved",
            }
        )
        raw_marker_row = normalized_score_state_mapping_if_present(
            {
                "score": 82,
                "raw_score_total_before_score_gap_block": 82,
            }
        )
        generic_score_row = normalized_score_state_mapping_if_present({"score": 82})

        self.assertFalse(blocked_reason_row["score_valid"])
        self.assertIsNone(blocked_reason_row["score"])
        self.assertIsNone(blocked_reason_row["visible_score"])
        self.assertEqual(blocked_reason_row["score_blocked_reason"], "score_gap_unresolved")
        self.assertFalse(raw_marker_row["score_valid"])
        self.assertIsNone(raw_marker_row["score"])
        self.assertIsNone(raw_marker_row["visible_score"])
        self.assertEqual(raw_marker_row["score_blocked_reason"], "score_gap_unresolved")
        self.assertEqual(generic_score_row, {"score": 82})

    def test_score_state_contract_violations_flag_valid_alias_mismatch(self):
        self.assertEqual(
            score_state_contract_violations(
                {
                    "visible_score": 65,
                    "score": 82,
                    "total_score": 65,
                    "score_valid": True,
                }
            ),
            ("valid_score_alias_mismatch:score",),
        )
        self.assertEqual(
            score_state_contract_violations(
                {
                    "visible_score": "not-a-number",
                    "score_valid": True,
                }
            ),
            ("valid_visible_score_not_numeric",),
        )
        self.assertEqual(
            score_state_contract_violations(
                {
                    "score": 82,
                    "score_total": 90,
                    "score_valid": True,
                }
            ),
            ("score_alias_conflict", "valid_visible_score_missing"),
        )

    def test_normalized_score_alias_value_uses_visible_score_contract(self):
        self.assertIsNone(normalized_score_alias_value(77, score_valid=True))
        self.assertIsNone(normalized_score_alias_value(77, score_valid=False))
        self.assertIsNone(normalized_score_alias_value(77, score_valid=None))
        self.assertIsNone(
            normalized_score_alias_value(
                77,
                score_valid=True,
                score_blocked_reason="score_gap_unresolved",
            )
        )

    def test_current_and_merged_score_aliases_count_as_explicit_visible_scores(self):
        self.assertEqual(
            score_state_contract_violations(
                {
                    "current_score": 65,
                    "score_valid": True,
                }
            ),
            (),
        )
        payload = normalized_score_state_payload(
            {
                "merged_score": 65,
                "score_valid": True,
            }
        )

        self.assertEqual(payload["visible_score"], 65)
        self.assertEqual(payload["merged_score"], 65)
        self.assertEqual(score_state_contract_violations(payload), ())

    def test_compare_score_states_reports_component_and_driver_changes(self):
        comparison = compare_score_states(
            {
                "visible_score": 82,
                "score_valid": True,
                "score_fingerprint": "score-a",
                "research_input_fingerprint": "input-a",
                "component_scores": {
                    "eps_fcf_explosion": 20,
                    "earnings_visibility": 18,
                    "bottleneck_pricing": 17,
                },
                "score_variability_drivers": ("input_count:research_report=2",),
            },
            {
                "visible_score": 65,
                "score_valid": True,
                "score_fingerprint": "score-b",
                "research_input_fingerprint": "input-b",
                "score_components": {
                    "eps_fcf_explosion_score": 20,
                    "earnings_visibility_score": 10,
                    "bottleneck_pricing_score": 12,
                },
                "score_variability_drivers": (
                    "input_count:research_report=2",
                    "estimate_source_missing:revision",
                ),
            },
        )

        self.assertEqual(comparison.status, "input_changed")
        self.assertEqual(comparison.component_deltas["earnings_visibility"], -8)
        self.assertEqual(comparison.component_deltas["bottleneck_pricing"], -5)
        self.assertIn("component_delta:earnings_visibility=-8", comparison.drivers)
        self.assertIn("component_delta:bottleneck_pricing=-5", comparison.drivers)
        self.assertIn("variability_driver_added:estimate_source_missing:revision", comparison.drivers)

    def test_compare_score_states_reports_contract_violations_even_when_visible_score_is_available(self):
        comparison = compare_score_states(
            {
                "visible_score": 65,
                "score": 82,
                "score_valid": True,
                "score_fingerprint": "same-score",
                "research_input_fingerprint": "same-input",
            },
            {
                "visible_score": 65,
                "score_valid": True,
                "score_fingerprint": "same-score",
                "research_input_fingerprint": "same-input",
            },
        )

        self.assertEqual(comparison.status, "same_score_snapshot")
        self.assertEqual(comparison.visible_score_before, 65)
        self.assertEqual(comparison.visible_score_after, 65)
        self.assertIn("before_score_state_contract:valid_score_alias_mismatch:score", comparison.drivers)

    def test_compare_score_state_rows_tracks_missing_and_changed_rows(self):
        changes = compare_score_state_rows(
            (
                {
                    "symbol": "005930",
                    "visible_score": 82,
                    "score_valid": True,
                    "score_fingerprint": "score-a",
                    "research_input_fingerprint": "input-a",
                },
                {
                    "symbol": "009999",
                    "visible_score": 71,
                    "score_valid": True,
                    "score_fingerprint": "old-score",
                    "research_input_fingerprint": "old-input",
                },
            ),
            (
                {
                    "symbol": "000111",
                    "visible_score": 69,
                    "score_valid": True,
                    "score_fingerprint": "new-score",
                    "research_input_fingerprint": "new-input",
                },
                {
                    "symbol": "005930",
                    "visible_score": 65,
                    "score_valid": True,
                    "score_fingerprint": "score-b",
                    "research_input_fingerprint": "input-b",
                },
            ),
            key_fields=("symbol",),
        )

        by_key = {change.key: change.comparison for change in changes}
        self.assertEqual(by_key["000111"].status, "missing_before_state")
        self.assertEqual(by_key["005930"].status, "input_changed")
        self.assertEqual(by_key["005930"].visible_score_delta, -17)
        self.assertEqual(by_key["009999"].status, "missing_after_state")

    def test_compare_score_state_rows_keeps_duplicate_keys_visible(self):
        changes = compare_score_state_rows(
            (
                {"symbol": "005930", "visible_score": 82, "score_valid": True},
                {"symbol": "005930", "visible_score": 77, "score_valid": True},
            ),
            (
                {"symbol": "005930", "visible_score": 82, "score_valid": True},
            ),
            key_fields=("symbol",),
        )

        self.assertEqual(tuple(change.key for change in changes), ("005930", "005930#2"))
        self.assertEqual(changes[1].comparison.status, "missing_after_state")


if __name__ == "__main__":
    unittest.main()
