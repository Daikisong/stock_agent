from datetime import date
import unittest
from unittest.mock import patch

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


if __name__ == "__main__":
    unittest.main()
