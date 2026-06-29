import unittest
from datetime import date

from e2r.agentic.evidence_contract_v2 import load_evidence_contracts_v2
from e2r.research_brain.v4_evidence_extraction_bridge import execute_source_tasks_with_evidence_os_v4
from e2r.research_brain.v4_source_acquisition_runner import SourceAcquisitionRunnerV4
from research_brain_v4_test_helpers import c06_source_task, sample_v4_event


class ResearchBrainV4NoSyntheticAssertionTests(unittest.TestCase):
    def test_extraction_audit_has_no_synthetic_or_forced_fields(self):
        contract = load_evidence_contracts_v2(require_all_archetypes=True)["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]
        bundle = execute_source_tasks_with_evidence_os_v4(
            event=sample_v4_event(),
            tasks=(c06_source_task(),),
            contract=contract,
            as_of_date=date(2026, 6, 29),
            source_runner=SourceAcquisitionRunnerV4(mode="frozen_real_source_snapshot"),
        )
        audit = bundle.extraction_audit
        self.assertEqual(audit["synthetic_assertion_count"], 0)
        self.assertEqual(audit["forced_positive_polarity_count"], 0)
        self.assertEqual(audit["forced_current_temporal_count"], 0)
        self.assertEqual(audit["forced_target_subject_count"], 0)
        self.assertEqual(audit["event_summary_used_as_exact_quote_count"], 0)


if __name__ == "__main__":
    unittest.main()
