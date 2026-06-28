from datetime import date
import unittest
from unittest.mock import patch

from e2r.calibration.taxonomy import large_sector_for_archetype
from e2r.agentic import ScoreContributionV2
from e2r.models import ScoreSnapshot
from e2r.scoring import CANONICAL_SCORE_COMPONENTS, DeterministicScorer, ScoringPayload


def complete_components(**overrides):
    components = {component.key: component.max_points for component in CANONICAL_SCORE_COMPONENTS}
    components.update(overrides)
    return components


class ScoringPayloadTests(unittest.TestCase):
    def test_payload_requires_all_canonical_components(self):
        components = complete_components()
        del components["market_mispricing"]

        with self.assertRaisesRegex(ValueError, "missing score components"):
            ScoringPayload(
                symbol="TEST",
                as_of_date=date(2026, 5, 13),
                components=components,
            )

    def test_payload_rejects_component_above_max_points(self):
        with self.assertRaisesRegex(ValueError, "eps_fcf_explosion must be between 0 and 20.0"):
            ScoringPayload(
                symbol="TEST",
                as_of_date=date(2026, 5, 13),
                components=complete_components(eps_fcf_explosion=21.0),
            )

    def test_payload_coerces_numeric_diagnostic_strings(self):
        payload = ScoringPayload(
            symbol="TEST",
            as_of_date=date(2026, 5, 13),
            components=complete_components(),
            diagnostic_scores={"revision_score": "72.5"},
        )

        self.assertEqual(payload.diagnostic_scores["revision_score"], 72.5)

    def test_payload_coerces_numeric_component_strings(self):
        payload = ScoringPayload(
            symbol="TEST",
            as_of_date=date(2026, 5, 13),
            components=complete_components(eps_fcf_explosion="17.5"),
        )

        self.assertEqual(payload.components["eps_fcf_explosion"], 17.5)

    def test_payload_rejects_non_numeric_diagnostic_scores(self):
        with self.assertRaisesRegex(ValueError, "diagnostic score revision_score must be numeric"):
            ScoringPayload(
                symbol="TEST",
                as_of_date=date(2026, 5, 13),
                components=complete_components(),
                diagnostic_scores={"revision_score": "unknown"},
            )

    def test_payload_allows_signed_total_adjustment_diagnostic(self):
        payload = ScoringPayload(
            symbol="TEST",
            as_of_date=date(2026, 5, 13),
            components=complete_components(),
            diagnostic_scores={"calibration_total_adjustment": -2.0},
        )

        self.assertEqual(payload.diagnostic_scores["calibration_total_adjustment"], -2.0)

    def test_payload_validates_score_contribution_claim_components(self):
        with self.assertRaisesRegex(ValueError, "unknown score contribution component"):
            ScoringPayload(
                symbol="TEST",
                as_of_date=date(2026, 5, 13),
                components=complete_components(),
                score_contribution_claim_ids={"not_a_component": ("CLM-1",)},
            )

    def test_scorer_preserves_score_contribution_claim_ids_on_snapshot(self):
        claim_ids = {
            "eps_fcf_explosion": ("CLM-EPS", "CLM-EPS"),
            "bottleneck_pricing": ("CLM-HBM",),
        }

        score = DeterministicScorer().score(
            ScoringPayload(
                symbol="TEST",
                as_of_date=date(2026, 5, 13),
                components=complete_components(),
                score_contribution_claim_ids=claim_ids,
                large_sector_id=large_sector_for_archetype("C06_HBM_MEMORY_CUSTOMER_CAPACITY"),
                canonical_archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            )
        )

        self.assertEqual(score.score_contribution_claim_ids["eps_fcf_explosion"], ("CLM-EPS",))
        self.assertEqual(score.score_contribution_claim_ids["bottleneck_pricing"], ("CLM-HBM",))
        ledger = {item.component_key: item for item in score.score_contribution_ledger}
        self.assertEqual(ledger["eps_fcf_explosion"].raw_points, 20.0)
        self.assertEqual(ledger["eps_fcf_explosion"].max_points, 20.0)
        self.assertEqual(ledger["eps_fcf_explosion"].support_claim_ids, ("CLM-EPS",))
        self.assertEqual(ledger["bottleneck_pricing"].support_claim_ids, ("CLM-HBM",))
        self.assertEqual(ledger["earnings_visibility"].cap_reason, "missing_support_claim_ids")

    def test_scorer_does_not_emit_claim_ids_for_zero_point_components(self):
        score = DeterministicScorer().score(
            ScoringPayload(
                symbol="TEST",
                as_of_date=date(2026, 5, 13),
                components=complete_components(
                    eps_fcf_explosion=0.0,
                    earnings_visibility=0.0,
                    bottleneck_pricing=0.0,
                    market_mispricing=0.0,
                    valuation_rerating=0.0,
                    capital_allocation=0.0,
                    information_confidence=0.0,
                ),
                score_contribution_claim_ids={
                    "eps_fcf_explosion": ("CLM-ZERO-EPS",),
                    "information_confidence": ("CLM-ZERO-CONFIDENCE",),
                },
                large_sector_id=large_sector_for_archetype("C06_HBM_MEMORY_CUSTOMER_CAPACITY"),
                canonical_archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            )
        )

        ledger = {item.component_key: item for item in score.score_contribution_ledger}
        self.assertEqual(score.total_score, 0.0)
        self.assertEqual(score.score_contribution_claim_ids, {})
        self.assertEqual(ledger["eps_fcf_explosion"].support_claim_ids, ())
        self.assertEqual(ledger["information_confidence"].support_claim_ids, ())

    def test_scorer_uses_score_contribution_v2_as_primary_ledger_input(self):
        v2_contributions = (
            ScoreContributionV2.build(
                component_key="eps_fcf_explosion",
                criterion_id="actual_eps_claim",
                raw_points=12.0,
                max_points=20.0,
                support_claim_ids=("CLM-V2-EPS",),
                rationale="v2 claim-backed actual EPS",
            ),
            ScoreContributionV2.build(
                component_key="earnings_visibility",
                criterion_id="missing_contract_bridge",
                raw_points=0.0,
                max_points=20.0,
                support_claim_ids=(),
                cap_reason="primitive_status:UNKNOWN",
                rationale="v2 missing contract primitive",
            ),
        )

        score = DeterministicScorer().score(
            ScoringPayload(
                symbol="TEST",
                as_of_date=date(2026, 5, 13),
                components=complete_components(eps_fcf_explosion=20.0),
                score_contribution_claim_ids={"eps_fcf_explosion": ("CLM-V1-IGNORED",)},
                score_contributions_v2=v2_contributions,
                large_sector_id=large_sector_for_archetype("C06_HBM_MEMORY_CUSTOMER_CAPACITY"),
                canonical_archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            )
        )

        ledger = {item.component_key: item for item in score.score_contribution_ledger}
        self.assertEqual(score.eps_fcf_explosion_score, 12.0)
        self.assertEqual(score.earnings_visibility_score, 0.0)
        self.assertEqual(score.bottleneck_pricing_score, 0.0)
        self.assertEqual(score.diagnostic_scores["score_contribution_v2_component_input_used"], 100.0)
        self.assertEqual(score.score_contribution_claim_ids["eps_fcf_explosion"], ("CLM-V2-EPS",))
        self.assertEqual(ledger["eps_fcf_explosion"].support_claim_ids, ("CLM-V2-EPS",))
        self.assertEqual(ledger["eps_fcf_explosion"].rationale, "component score has v2 claim-backed support")
        self.assertEqual(ledger["earnings_visibility"].cap_reason, "primitive_status:UNKNOWN")
        self.assertEqual(score.diagnostic_scores["score_contribution_v2_used"], 100.0)
        self.assertEqual(score.diagnostic_scores["score_contribution_v2_input_count_capped"], 2.0)

    def test_scorer_requires_v2_contributions_when_cutover_flag_is_set(self):
        score = DeterministicScorer().score(
            ScoringPayload(
                symbol="TEST",
                as_of_date=date(2026, 5, 13),
                components=complete_components(
                    eps_fcf_explosion=12.0,
                    earnings_visibility=0.0,
                    bottleneck_pricing=0.0,
                    market_mispricing=0.0,
                    valuation_rerating=0.0,
                    capital_allocation=0.0,
                    information_confidence=0.0,
                ),
                diagnostic_scores={"require_v2_score_contributions": 100.0},
                score_contribution_claim_ids={"eps_fcf_explosion": ("CLM-V1-PARSER",)},
                large_sector_id=large_sector_for_archetype("C06_HBM_MEMORY_CUSTOMER_CAPACITY"),
                canonical_archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            )
        )

        self.assertEqual(score.total_score, 0.0)
        self.assertEqual(score.eps_fcf_explosion_score, 0.0)
        self.assertEqual(score.risk_penalty, 0.0)
        self.assertEqual(score.diagnostic_scores["score_valid"], 0.0)
        self.assertEqual(score.diagnostic_scores["score_contribution_v2_required"], 100.0)
        self.assertEqual(score.diagnostic_scores["score_contribution_v2_used"], 0.0)
        self.assertEqual(score.diagnostic_scores["score_blocked_by_orphan_score_contribution"], 100.0)
        self.assertEqual(score.score_contribution_claim_ids, {})

    def test_scorer_quarantines_legacy_risk_penalty_when_v2_components_are_primary(self):
        v2_contributions = (
            ScoreContributionV2.build(
                component_key="earnings_visibility",
                criterion_id="current_revision_claim",
                raw_points=4.0,
                max_points=20.0,
                support_claim_ids=("CLM-V2-REVISION",),
                rationale="v2 claim-backed revision visibility",
            ),
        )

        score = DeterministicScorer().score(
            ScoringPayload(
                symbol="TEST",
                as_of_date=date(2026, 5, 13),
                components=complete_components(earnings_visibility=0.0),
                risk_penalty=15.0,
                score_contributions_v2=v2_contributions,
                large_sector_id=large_sector_for_archetype("C06_HBM_MEMORY_CUSTOMER_CAPACITY"),
                canonical_archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            )
        )

        self.assertEqual(score.earnings_visibility_score, 4.0)
        self.assertEqual(score.risk_penalty, 0.0)
        self.assertGreater(score.total_score, 0.0)
        self.assertEqual(score.diagnostic_scores["score_contribution_v2_component_input_used"], 100.0)
        self.assertEqual(score.diagnostic_scores["score_contribution_v2_legacy_risk_penalty_quarantined"], 100.0)
        self.assertEqual(score.diagnostic_scores["raw_legacy_risk_penalty_before_v2_quarantine"], 15.0)

    def test_payload_rejects_non_finite_component_and_diagnostic_values(self):
        with self.assertRaisesRegex(ValueError, "eps_fcf_explosion must be between 0 and 20.0"):
            ScoringPayload(
                symbol="TEST",
                as_of_date=date(2026, 5, 13),
                components=complete_components(eps_fcf_explosion=float("nan")),
            )
        with self.assertRaisesRegex(ValueError, "diagnostic score revision_score must be finite"):
            ScoringPayload(
                symbol="TEST",
                as_of_date=date(2026, 5, 13),
                components=complete_components(),
                diagnostic_scores={"revision_score": float("inf")},
            )

    def test_score_snapshot_rejects_non_finite_diagnostics(self):
        with self.assertRaisesRegex(ValueError, "diagnostic score revision_score must be finite"):
            ScoreSnapshot(
                symbol="TEST",
                as_of_date=date(2026, 5, 13),
                eps_fcf_explosion_score=20.0,
                earnings_visibility_score=20.0,
                bottleneck_pricing_score=20.0,
                market_mispricing_score=15.0,
                valuation_rerating_score=15.0,
                capital_allocation_score=5.0,
                information_confidence_score=5.0,
                risk_penalty=0.0,
                total_score=100.0,
                diagnostic_scores={"revision_score": float("nan")},
            )


class DeterministicScorerTests(unittest.TestCase):
    def test_score_snapshot_shape_and_total(self):
        payload = ScoringPayload(
            symbol="103590",
            as_of_date=date(2024, 3, 27),
            components={
                "eps_fcf_explosion": 16.0,
                "earnings_visibility": 15.0,
                "bottleneck_pricing": 14.0,
                "market_mispricing": 10.0,
                "valuation_rerating": 9.0,
                "capital_allocation": 3.0,
                "information_confidence": 4.0,
            },
            risk_penalty=6.0,
            diagnostic_scores={"revision_score": 72.0, "price_stage_score": 55.0},
            evidence_ids=("ev-1", "ev-2"),
        )

        with patch.dict("os.environ", {"E2R_SCORING_PROFILE": "calibrated"}):
            snapshot = DeterministicScorer().score(payload)

        self.assertEqual(snapshot.symbol, "103590")
        self.assertEqual(snapshot.as_of_date, date(2024, 3, 27))
        self.assertEqual(snapshot.total_score, 65.0)
        self.assertEqual(snapshot.eps_fcf_explosion_score, 16.0)
        self.assertEqual(snapshot.diagnostic_scores["score_valid"], 100.0)
        self.assertEqual(snapshot.diagnostic_scores["revision_score"], 72.0)
        self.assertEqual(snapshot.evidence_ids, ("ev-1", "ev-2"))

    def test_score_total_is_floored_at_zero(self):
        payload = ScoringPayload(
            symbol="LOW",
            as_of_date=date(2026, 5, 13),
            components=complete_components(
                eps_fcf_explosion=1.0,
                earnings_visibility=1.0,
                bottleneck_pricing=1.0,
                market_mispricing=1.0,
                valuation_rerating=1.0,
                capital_allocation=1.0,
                information_confidence=1.0,
            ),
            risk_penalty=99.0,
        )

        with patch.dict("os.environ", {"E2R_SCORING_PROFILE": "calibrated"}):
            self.assertEqual(DeterministicScorer().score(payload).total_score, 0.0)

    def test_source_backed_deep_research_unlock_allows_rich_single_family_claim_ledger(self):
        components = complete_components()
        claim_ids = {key: (f"CLM-{key}",) for key in components}
        diagnostics = {
            "source_backed_green_bridge_raw": 95.0,
            "claim_backed_claim_count_capped": 80.0,
            "cross_evidence_family_count": 4.0,
            "report_date_confidence": 100.0,
            "date_unverified_snippet_news_count_capped": 0.0,
            "date_unverified_document_count_capped": 0.0,
            "actual_profit_conversion_score": 85.0,
            "medium_term_revision_visibility": 90.0,
            "structural_visibility_quality": 95.0,
            "domain_specific_evidence_score": 35.0,
            "research_axis_bridge_present_count_capped": 6.0,
        }

        with patch.dict("os.environ", {"E2R_SCORING_PROFILE": "calibrated"}):
            unlocked = DeterministicScorer().score(
                ScoringPayload(
                    symbol="SRC",
                    as_of_date=date(2026, 5, 13),
                    components=components,
                    diagnostic_scores=diagnostics,
                    score_contribution_claim_ids=claim_ids,
                )
            )
            rich_single_family = DeterministicScorer().score(
                ScoringPayload(
                    symbol="SRC",
                    as_of_date=date(2026, 5, 13),
                    components=components,
                    diagnostic_scores={**diagnostics, "cross_evidence_family_count": 1.0},
                    score_contribution_claim_ids=claim_ids,
                )
            )
            weak_single_family = DeterministicScorer().score(
                ScoringPayload(
                    symbol="SRC",
                    as_of_date=date(2026, 5, 13),
                    components=components,
                    diagnostic_scores={
                        **diagnostics,
                        "claim_backed_claim_count_capped": 18.0,
                        "cross_evidence_family_count": 1.0,
                    },
                    score_contribution_claim_ids=claim_ids,
                )
            )

        self.assertEqual(unlocked.diagnostic_scores["source_backed_deep_research_completed"], 100.0)
        self.assertEqual(unlocked.diagnostic_scores["green_unlock_evidence_score"], 95.0)
        self.assertEqual(rich_single_family.diagnostic_scores["source_backed_deep_research_completed"], 100.0)
        self.assertNotIn("source_backed_deep_research_completed", weak_single_family.diagnostic_scores)

    def test_calibration_risk_penalties_reduce_score_without_crashing(self):
        payload = ScoringPayload(
            symbol="RISK",
            as_of_date=date(2026, 5, 13),
            components={component.key: component.max_points * 0.7 for component in CANONICAL_SCORE_COMPONENTS},
            diagnostic_scores={
                "high_mae_risk": 100.0,
                "stage2_actionable_volatility_risk": 100.0,
            },
        )

        with patch.dict("os.environ", {"E2R_SCORING_PROFILE": "calibrated"}):
            score = DeterministicScorer().score(payload)

        self.assertEqual(score.total_score, 66.0)
        self.assertEqual(score.diagnostic_scores["calibration_total_adjustment"], -4.0)

    def test_score_contribution_claim_diagnostics_and_enforcement(self):
        components = complete_components(
            eps_fcf_explosion=10.0,
            earnings_visibility=0.0,
            bottleneck_pricing=0.0,
            market_mispricing=0.0,
            valuation_rerating=0.0,
            capital_allocation=0.0,
            information_confidence=0.0,
        )
        claim_backed = ScoringPayload(
            symbol="TEST",
            as_of_date=date(2026, 5, 13),
            components=components,
            score_contribution_claim_ids={"eps_fcf_explosion": ("CLM-1",)},
        )
        unbacked_required = ScoringPayload(
            symbol="TEST",
            as_of_date=date(2026, 5, 13),
            components=components,
            diagnostic_scores={"require_claim_backed_score_contributions": 100.0},
        )

        with patch.dict("os.environ", {"E2R_SCORING_PROFILE": "calibrated"}):
            backed_score = DeterministicScorer().score(claim_backed)
            blocked_score = DeterministicScorer().score(unbacked_required)

        self.assertEqual(backed_score.diagnostic_scores["orphan_score_component_count_capped"], 0.0)
        self.assertEqual(backed_score.diagnostic_scores["score_claim_backed_component_ratio"], 100.0)
        self.assertEqual(blocked_score.total_score, 0.0)
        self.assertEqual(blocked_score.diagnostic_scores["score_valid"], 0.0)
        self.assertEqual(blocked_score.diagnostic_scores["score_blocked_by_orphan_score_contribution"], 100.0)

    def test_source_backed_green_total_floor_requires_tight_clean_bridge(self):
        components = {
            "eps_fcf_explosion": 17.0,
            "earnings_visibility": 17.0,
            "bottleneck_pricing": 17.0,
            "market_mispricing": 12.0,
            "valuation_rerating": 12.0,
            "capital_allocation": 5.0,
            "information_confidence": 5.0,
        }
        diagnostics = {
            "source_backed_green_bridge_raw": 95.0,
            "research_axis_bridge_guard_risk": 0.0,
            "research_axis_bridge_guard_risk_penalty_points": 0.0,
            "research_axis_bridge_present_count_capped": 5.0,
            "claim_backed_claim_count_capped": 80.0,
            "report_date_confidence": 100.0,
            "actual_profit_conversion_score": 55.0,
            "medium_term_revision_visibility": 55.0,
            "structural_visibility_quality": 55.0,
            "domain_specific_evidence_score": 0.0,
        }
        claim_ids = {key: (f"CLM-{key}",) for key in components}

        with patch.dict("os.environ", {"E2R_SCORING_PROFILE": "calibrated"}):
            clean = DeterministicScorer().score(
                ScoringPayload(
                    symbol="SOURCE",
                    as_of_date=date(2026, 5, 13),
                    components=components,
                    diagnostic_scores=diagnostics,
                    score_contribution_claim_ids=claim_ids,
                )
            )
            weak_source = DeterministicScorer().score(
                ScoringPayload(
                    symbol="SOURCE",
                    as_of_date=date(2026, 5, 13),
                    components=components,
                    diagnostic_scores={**diagnostics, "source_backed_green_bridge_raw": 94.9},
                    score_contribution_claim_ids=claim_ids,
                )
            )
            guard_risk = DeterministicScorer().score(
                ScoringPayload(
                    symbol="SOURCE",
                    as_of_date=date(2026, 5, 13),
                    components=components,
                    diagnostic_scores={**diagnostics, "research_axis_bridge_guard_risk": 1.0},
                    score_contribution_claim_ids=claim_ids,
                )
            )
            too_far_below_green = DeterministicScorer().score(
                ScoringPayload(
                    symbol="SOURCE",
                    as_of_date=date(2026, 5, 13),
                    components={**components, "information_confidence": 2.0},
                    diagnostic_scores={**diagnostics, "source_backed_green_bridge_raw": 80.0},
                    score_contribution_claim_ids=claim_ids,
                )
            )
            rich_source_backed_far_below_green = DeterministicScorer().score(
                ScoringPayload(
                    symbol="SOURCE",
                    as_of_date=date(2026, 5, 13),
                    components={**components, "information_confidence": 2.0},
                    diagnostic_scores=diagnostics,
                    score_contribution_claim_ids=claim_ids,
                )
            )
            already_green_below_rich_floor = DeterministicScorer().score(
                ScoringPayload(
                    symbol="SOURCE",
                    as_of_date=date(2026, 5, 13),
                    components={**components, "eps_fcf_explosion": 20.0},
                    diagnostic_scores=diagnostics,
                    score_contribution_claim_ids=claim_ids,
                )
            )
            already_above_rich_floor = DeterministicScorer().score(
                ScoringPayload(
                    symbol="SOURCE",
                    as_of_date=date(2026, 5, 13),
                    components={
                        "eps_fcf_explosion": 20.0,
                        "earnings_visibility": 20.0,
                        "bottleneck_pricing": 20.0,
                        "market_mispricing": 15.0,
                        "valuation_rerating": 15.0,
                        "capital_allocation": 5.0,
                        "information_confidence": 5.0,
                    },
                    diagnostic_scores=diagnostics,
                    score_contribution_claim_ids=claim_ids,
                )
            )

        self.assertEqual(clean.total_score, 92.25)
        self.assertEqual(clean.diagnostic_scores["source_backed_green_total_floor_applied"], 1.0)
        self.assertEqual(weak_source.total_score, 85.0)
        self.assertNotIn("source_backed_green_total_floor_applied", weak_source.diagnostic_scores)
        self.assertEqual(guard_risk.total_score, 85.0)
        self.assertNotIn("source_backed_green_total_floor_applied", guard_risk.diagnostic_scores)
        self.assertEqual(too_far_below_green.total_score, 82.0)
        self.assertNotIn("source_backed_green_total_floor_applied", too_far_below_green.diagnostic_scores)
        self.assertEqual(rich_source_backed_far_below_green.total_score, 92.25)
        self.assertEqual(rich_source_backed_far_below_green.diagnostic_scores["source_backed_deep_research_completed"], 100.0)
        self.assertEqual(already_green_below_rich_floor.total_score, 92.25)
        self.assertEqual(already_green_below_rich_floor.diagnostic_scores["source_backed_green_total_floor_applied"], 1.0)
        self.assertEqual(already_above_rich_floor.total_score, 100.0)
        self.assertNotIn("source_backed_green_total_floor_applied", already_above_rich_floor.diagnostic_scores)

    def test_source_backed_green_context_blocks_orphan_score_contributions(self):
        components = complete_components(
            eps_fcf_explosion=17.0,
            earnings_visibility=17.0,
            bottleneck_pricing=17.0,
            market_mispricing=12.0,
            valuation_rerating=12.0,
            capital_allocation=5.0,
            information_confidence=5.0,
        )

        with patch.dict("os.environ", {"E2R_SCORING_PROFILE": "calibrated"}):
            score = DeterministicScorer().score(
                ScoringPayload(
                    symbol="SOURCE",
                    as_of_date=date(2026, 5, 13),
                    components=components,
                    diagnostic_scores={
                        "source_backed_green_bridge_raw": 95.0,
                        "claim_backed_claim_count_capped": 80.0,
                    },
                )
            )

        self.assertEqual(score.total_score, 0.0)
        self.assertEqual(score.diagnostic_scores["score_valid"], 0.0)
        self.assertEqual(score.diagnostic_scores["score_blocked_by_orphan_score_contribution"], 100.0)
        self.assertEqual(score.diagnostic_scores["score_claim_backed_required"], 100.0)

    def test_source_backed_floor_allows_low_raw_bio_commercialization_with_full_claims(self):
        components = complete_components(
            eps_fcf_explosion=15.0,
            earnings_visibility=14.0,
            bottleneck_pricing=14.0,
            market_mispricing=10.0,
            valuation_rerating=10.0,
            capital_allocation=4.0,
            information_confidence=3.0,
        )
        claim_ids = {key: (f"CLM-{key}",) for key in components}
        diagnostics = {
            "source_backed_green_bridge_raw": 95.0,
            "research_axis_bridge_guard_risk": 0.0,
            "research_axis_bridge_guard_risk_penalty_points": 0.0,
            "research_axis_bridge_present_count_capped": 9.0,
            "research_axis_bridge_bio_commercialization": 100.0,
            "claim_backed_claim_count_capped": 100.0,
            "report_date_confidence": 100.0,
            "actual_profit_conversion_score": 71.0,
            "medium_term_revision_visibility": 100.0,
            "structural_visibility_quality": 95.0,
            "domain_specific_evidence_score": 100.0,
            "cross_evidence_family_count": 1.0,
            "date_unverified_document_count_capped": 0.0,
            "date_unverified_snippet_news_count_capped": 0.0,
        }

        with patch.dict("os.environ", {"E2R_SCORING_PROFILE": "calibrated"}):
            source_backed = DeterministicScorer().score(
                ScoringPayload(
                    symbol="BIO",
                    as_of_date=date(2026, 5, 13),
                    components=components,
                    diagnostic_scores=diagnostics,
                    score_contribution_claim_ids=claim_ids,
                )
            )
            below_source_backed_floor = DeterministicScorer().score(
                ScoringPayload(
                    symbol="BIO",
                    as_of_date=date(2026, 5, 13),
                    components={**components, "information_confidence": 2.5},
                    diagnostic_scores=diagnostics,
                    score_contribution_claim_ids=claim_ids,
                )
            )

        self.assertEqual(source_backed.total_score, 92.25)
        self.assertEqual(source_backed.diagnostic_scores["source_backed_green_total_floor_applied"], 1.0)
        self.assertEqual(below_source_backed_floor.total_score, 69.5)
        self.assertNotIn("source_backed_green_total_floor_applied", below_source_backed_floor.diagnostic_scores)

    def test_event_only_red_watch_override_requires_bio_commercialization_bridge(self):
        archetype = "C24_BIO_TRIAL_DATA_EVENT_RISK"
        components = complete_components(
            eps_fcf_explosion=17.0,
            earnings_visibility=17.0,
            bottleneck_pricing=17.0,
            market_mispricing=12.0,
            valuation_rerating=12.0,
            capital_allocation=5.0,
            information_confidence=5.0,
        )
        diagnostics = {
            "source_backed_green_bridge_raw": 95.0,
            "research_axis_bridge_guard_risk": 0.0,
            "research_axis_bridge_guard_risk_penalty_points": 0.0,
            "research_axis_bridge_present_count_capped": 5.0,
            "actual_profit_conversion_score": 55.0,
            "medium_term_revision_visibility": 55.0,
            "structural_visibility_quality": 55.0,
            "domain_specific_evidence_score": 55.0,
            "revision_score": 55.0,
            "contract_quality": 55.0,
            "green_unlock_evidence_score": 0.0,
        }

        with patch.dict("os.environ", {"E2R_SCORING_PROFILE": "rolling"}):
            missing_bio_bridge = DeterministicScorer().score(
                ScoringPayload(
                    symbol="BIO",
                    as_of_date=date(2026, 5, 13),
                    components=components,
                    diagnostic_scores={**diagnostics, "research_axis_bridge_bio_commercialization": 0.0},
                    large_sector_id=large_sector_for_archetype(archetype),
                    canonical_archetype_id=archetype,
                )
            )
            with_bio_bridge = DeterministicScorer().score(
                ScoringPayload(
                    symbol="BIO",
                    as_of_date=date(2026, 5, 13),
                    components=components,
                    diagnostic_scores={**diagnostics, "research_axis_bridge_bio_commercialization": 80.0},
                    large_sector_id=large_sector_for_archetype(archetype),
                    canonical_archetype_id=archetype,
                )
            )

        self.assertEqual(missing_bio_bridge.diagnostic_scores["archetype_green_policy_source_backed_override"], 0.0)
        self.assertEqual(missing_bio_bridge.diagnostic_scores["archetype_green_restricted_by_profile"], 1.0)
        self.assertEqual(with_bio_bridge.diagnostic_scores["archetype_green_policy_source_backed_override"], 1.0)
        self.assertEqual(with_bio_bridge.diagnostic_scores["archetype_green_restricted_by_profile"], 0.0)


if __name__ == "__main__":
    unittest.main()
