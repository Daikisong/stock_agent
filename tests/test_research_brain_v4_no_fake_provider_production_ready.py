import unittest

from e2r.research_brain.v4_production_orchestrator import run_research_brain_v4_production_shadow
from e2r.research_brain.v4_schemas import ProductionShadowV4Config
from research_brain_v4_test_helpers import load_v4_matrix


class ResearchBrainV4NoFakeProviderProductionReadyTests(unittest.TestCase):
    def test_fake_provider_blocks_production_ready_even_when_shadow_runs(self):
        result = run_research_brain_v4_production_shadow(
            config=ProductionShadowV4Config(
                as_of_date="2026-06-29",
                planner_provider="fake",
                source_acquisition="frozen_real_source_snapshot",
                universe_limit=6,
                planner_success_limit=6,
                fake_provider_allowed=True,
            ),
            v1_archetype_matrix=load_v4_matrix(),
        )
        planner = result["planner_report"]["summary"]
        verdict = result["readiness"]["summary"]
        self.assertGreater(planner["fake_provider_used_count"], 0)
        self.assertFalse(verdict["production_ready"])
        self.assertIn("fake planner provider used", verdict["blockers"])


if __name__ == "__main__":
    unittest.main()
