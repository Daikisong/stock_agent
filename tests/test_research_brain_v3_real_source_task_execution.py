import unittest
from datetime import date

from e2r.agentic.evidence_contract_v2 import load_evidence_contracts_v2
from e2r.research_brain.v3_evidence_os_execution_bridge import execute_source_tasks_with_evidence_os_v3
from e2r.research_brain.v3_llm_planner_provider import FixturePlannerProvider, source_tasks_from_planner_output
from e2r.research_brain.v3_raw_event_routing import load_raw_event_routing_fixtures, raw_fixture_to_event
from e2r.research_brain.v3_source_acquisition_runner import SourceAcquisitionRunnerV3
from research_brain_v2_test_helpers import load_v2_cards


class ResearchBrainV3RealSourceTaskExecutionTests(unittest.TestCase):
    def test_source_task_creates_evidence_os_claim(self):
        cards = load_v2_cards()
        cards_by_id = {card.archetype_id: card for card in cards}
        event = raw_fixture_to_event(load_raw_event_routing_fixtures()[0])
        output = FixturePlannerProvider().plan(event, cards)
        primary = output.top_k_archetype_hypotheses[0]["archetype_id"]
        tasks = source_tasks_from_planner_output(event=event, planner_output=output, card_by_id=cards_by_id)
        contract = load_evidence_contracts_v2(require_all_archetypes=True)[primary]
        bundle = execute_source_tasks_with_evidence_os_v3(
            event=event,
            tasks=tasks,
            contract=contract,
            as_of_date=date(2026, 6, 29),
            source_runner=SourceAcquisitionRunnerV3(mode="snapshot"),
        )
        accepted = [claim for execution in bundle.executions for claim in execution.accepted_claim_ids]
        self.assertGreater(len(accepted), 0)
        for claim_id in accepted:
            self.assertIn(claim_id, bundle.ledger.claims)


if __name__ == "__main__":
    unittest.main()
