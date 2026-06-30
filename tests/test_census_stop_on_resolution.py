import unittest

from e2r.census.deep_dossier_scheduler import execute_source_tasks
from e2r.census.schemas import DepthLevel, SourceTask


class CensusStopOnResolutionTests(unittest.TestCase):
    def test_accepted_claim_stops_task(self):
        task = SourceTask(task_id="T1", symbol="005930", depth_level=DepthLevel.L3_RESEARCH_BRAIN_TRIAGE, task_class="official", source_class="DART", budget={"max_fetches": 1})
        execution = execute_source_tasks([task], accepted_claims_by_task={"T1": ["CLM-1"]})[0]
        self.assertEqual(execution.status.value, "EVIDENCE_OS_ACCEPTED")
        self.assertEqual(execution.stop_reason, "resolved_by_accepted_claim")


if __name__ == "__main__":
    unittest.main()
