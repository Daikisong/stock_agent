from __future__ import annotations

import unittest

from e2r.research_brain.replay.c06_component_replay import (
    run_c06_component_replay,
)


class _BlindFixtureProvider:
    provider_name = "TEST_BLIND_COMPONENT_PROVIDER"

    def complete(self, *, pass_name, payload):
        if pass_name == "IMPACT_SKEPTIC":
            return {"verdict": "APPROVE", "issues": []}
        claim = payload["accepted_claim"]
        primitive = claim["primitive_id"]
        rubric = next(
            row for row in payload["rubrics"] if row["primitive_id"] == primitive
        )
        direction = "COUNTER" if primitive == "qualification_state" else "SUPPORT"
        required_by_primitive = {
            "hbm_capacity_pre_sold": ["bottleneck_pricing", "earnings_visibility"],
            "shipment_or_revenue_mix": ["eps_fcf_explosion", "earnings_visibility"],
            "qualification_state": ["earnings_visibility"],
            "actual_earnings_conversion": ["eps_fcf_explosion"],
            "hbm_product_profile": ["information_confidence"],
            "package_substrate_sympathy": ["information_confidence"],
        }
        return {
            "impacts": [
                {
                    "mapping_id": claim["mapping_ids"][0],
                    "primitive_id": primitive,
                    "component_id": component,
                    "direction": direction,
                    "support_type": "RISK_OPEN" if direction == "COUNTER" else "DIRECT_ACTUAL",
                    "strength_band": "STRONG",
                    "completeness_band": "SUBSTANTIAL",
                    "causal_distance": "DIRECT",
                    "temporal_scope": "CURRENT",
                    "source_family": "ISSUER_OFFICIAL",
                    "evidence_family_id": f"FAM-{primitive}",
                    "confidence": 0.9,
                    "rationale": "The exact historical quote directly supports this bounded component impact.",
                    "unsupported_aspects": ["No other economic effect is established."],
                    "counter_claim_ids": [],
                }
                for component in required_by_primitive[primitive]
                if component in rubric["allowed_component_ids"]
            ],
            "unsupported_aspects": ["No score, Stage, or unquoted effect is inferred."],
            "counter_thesis": [],
            "reasoning_summary": "Blind bounded attribution only.",
        }


class C06HistoricalComponentReplayTests(unittest.TestCase):
    def test_blind_replay_preserves_positive_guard_and_profile_relations(self) -> None:
        result = run_c06_component_replay(
            config_path="configs/e2r_c06_historical_component_replay_v1.json",
            provider=_BlindFixtureProvider(),
            source_loader=_fixture_source_loader,
        )
        self.assertEqual(result["status"], "C06_HISTORICAL_COMPONENT_REPLAY_PASS")
        self.assertEqual(result["component_assignment_precision"], 1.0)
        self.assertEqual(result["direction_accuracy"], 1.0)
        self.assertEqual(result["critical_guard_accuracy"], 1.0)
        self.assertEqual(result["critical_count_sum"], 0)

    def test_provider_prompt_hides_expected_components_and_future_outcomes(self) -> None:
        provider = _RecordingBlindProvider()
        run_c06_component_replay(
            config_path="configs/e2r_c06_historical_component_replay_v1.json",
            provider=provider,
            source_loader=_fixture_source_loader,
        )
        serialized = str(provider.payloads).lower()
        self.assertNotIn("required_component_ids", serialized)
        self.assertNotIn("forbidden_component_ids", serialized)
        self.assertNotIn("mfe", serialized)
        self.assertNotIn("mae", serialized)
        self.assertNotIn("future_outcome", serialized)


class _RecordingBlindProvider(_BlindFixtureProvider):
    def __init__(self):
        self.payloads = []

    def complete(self, *, pass_name, payload):
        self.payloads.append(payload)
        return super().complete(pass_name=pass_name, payload=payload)


def _fixture_source_loader(case):
    text = f"Source header. {case['exact_quote']}. Source footer."
    return {"text": text, "error": None, "content_sha256": "a" * 64}


if __name__ == "__main__":
    unittest.main()
