import unittest
from datetime import date

from e2r.research_brain.schemas import SourceTask, SourceTaskType
from e2r.research_brain.v4_source_acquisition_runner import SourceAcquisitionRunnerV4
from research_brain_v4_test_helpers import sample_v4_event


class ResearchBrainV4NoUnboundedProductionFetchTests(unittest.TestCase):
    def test_source_task_without_unbounded_general_search_guard_is_rejected(self):
        event = sample_v4_event()
        task = SourceTask(
            task_id="bad-task",
            candidate_event_id=event.candidate_event_id,
            symbol=event.symbol,
            company_name=event.company_name,
            archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            primitive_gap="medium_term_revision_visibility",
            task_type=SourceTaskType.POSITIVE_VERIFY.value,
            preferred_source_classes=("CompanyGuide",),
            fallback_source_classes=(),
            forbidden_source_classes=(),
            max_queries=1,
            max_candidates=10,
            max_fetches=3,
            general_search_allowed=False,
        )
        result = SourceAcquisitionRunnerV4(mode="frozen_real_source_snapshot").acquire(
            event=event,
            task=task,
            as_of_date=date(2026, 6, 29),
        )
        self.assertEqual(result.status, "REJECTED_BY_POLICY")
        self.assertIn("missing_unbounded_general_search_guard", result.provider_errors)


if __name__ == "__main__":
    unittest.main()
