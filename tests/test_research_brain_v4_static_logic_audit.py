import unittest

from e2r.research_brain.v4_production_orchestrator import run_research_brain_v4_production_shadow
from e2r.research_brain.v4_schemas import ProductionShadowV4Config
from research_brain_v4_test_helpers import RealStubPlannerProviderV4, load_v4_matrix


class ResearchBrainV4StaticLogicAuditTests(unittest.TestCase):
    def test_static_critical_counts_are_zero_for_real_stub_shadow(self):
        result = run_research_brain_v4_production_shadow(
            config=ProductionShadowV4Config(
                as_of_date="2026-06-29",
                planner_provider="real",
                source_acquisition="frozen_real_source_snapshot",
                universe_limit=6,
                planner_success_limit=6,
            ),
            v1_archetype_matrix=load_v4_matrix(),
            planner_provider=RealStubPlannerProviderV4(),
        )
        audit = result["static_audit"]["summary"]
        source = result["source_acquisition_report"]["summary"]
        planner = result["planner_report"]["summary"]
        self.assertEqual(planner["planner_not_attempted_count"], 0)
        self.assertTrue(source["required_official_source_classes_present"])
        self.assertEqual(audit["critical_count_sum"], 0)
        self.assertGreater(audit["real_provider_exercised_count"], 0)


if __name__ == "__main__":
    unittest.main()
