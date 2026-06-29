import unittest
from datetime import date

from e2r.agentic.evidence_contract_v2 import load_evidence_contracts_v2
from e2r.research_brain.v4_evidence_extraction_bridge import execute_source_tasks_with_evidence_os_v4
from e2r.research_brain.v4_source_acquisition_runner import SourceAcquisitionRunnerV4
from research_brain_v4_test_helpers import c06_source_task, sample_v4_event


class ResearchBrainV4NoSnapshotFakeClaimTests(unittest.TestCase):
    def test_fake_source_provider_never_creates_accepted_claim(self):
        contract = load_evidence_contracts_v2(require_all_archetypes=True)["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]
        bundle = execute_source_tasks_with_evidence_os_v4(
            event=sample_v4_event(),
            tasks=(c06_source_task(),),
            contract=contract,
            as_of_date=date(2026, 6, 29),
            source_runner=SourceAcquisitionRunnerV4(mode="test_fake"),
        )
        execution = bundle.executions[0]
        self.assertEqual(execution.status, "PROVIDER_FAILED")
        self.assertFalse(execution.accepted_claim_ids)
        self.assertFalse(bundle.ledger.claims)


if __name__ == "__main__":
    unittest.main()
