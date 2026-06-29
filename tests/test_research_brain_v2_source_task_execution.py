import unittest

from e2r.research_brain.v2_candidate_events import candidate_events_v2_from_mapping
from e2r.research_brain.v2_source_task_execution import (
    build_source_task_execution_audit,
    execute_source_tasks_from_local_evidence,
    plan_source_tasks_v2,
)
from research_brain_v2_test_helpers import load_json, load_v2_cards


class ResearchBrainV2SourceTaskExecutionTests(unittest.TestCase):
    def test_source_task_execution_audit_has_no_unbounded_tasks(self):
        audit = load_json("docs/operational/research_brain_v2_source_task_execution_audit.json")
        self.assertEqual(audit["summary"]["unbounded_source_task_count"], 0)
        self.assertEqual(audit["summary"]["planned_but_not_executed_task_count"], 0)
        self.assertEqual(audit["summary"]["source_task_to_score_contribution_count"], 0)
        self.assertEqual(audit["summary"]["DART_solvable_gap_sent_to_web_count"], 0)
        self.assertEqual(audit["summary"]["FCF_gap_sent_to_news_count"], 0)
        self.assertEqual(audit["summary"]["general_search_task_ratio"], 0.0)

    def test_accepted_claim_zero_does_not_create_score_contribution(self):
        card = {card.archetype_id: card for card in load_v2_cards()}["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]
        event = candidate_events_v2_from_mapping(
            {
                "symbol": "000660",
                "company_name": "SK하이닉스",
                "as_of_date": "2026-06-29",
                "reason_codes": ["DISC_SUPPLY_CONTRACT"],
                "evidence_ids": [],
            }
        )[0]
        tasks = plan_source_tasks_v2(event=event, card=card)
        executions = execute_source_tasks_from_local_evidence(event=event, tasks=tasks)
        audit = build_source_task_execution_audit(planned_tasks=tasks, executions=executions, deterministic_stage_output_count=0)
        self.assertEqual(audit["summary"]["accepted_claim_count"], 0)
        self.assertEqual(audit["summary"]["source_task_to_score_contribution_count"], 0)


if __name__ == "__main__":
    unittest.main()
