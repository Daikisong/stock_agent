from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.research_brain.dossier import finalize_dossier_question_closures


class DossierQuestionFinalizerTests(unittest.TestCase):
    def test_only_bounded_official_first_web_exhaustion_closes_pending(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            dossier, research = root / "dossier", root / "research"
            dossier.mkdir(); research.mkdir()
            question = "Is a current direct fact confirmed?"
            routes = ["OFFICIAL","ISSUER_IR","FINANCIAL_REVISION","INDEPENDENT","COUNTER","SUPERSESSION"]
            self._jsonl(dossier / "question_source_tasks.jsonl", [{"target_id":"X","question_family_id":"F1","question_to_answer":question,"as_of_date":"2026-07-11","required_route_categories":routes}])
            self._jsonl(dossier / "question_closure.jsonl", [{"target_id":"X","question_family_id":"F1","status":"PROVIDER_PENDING","search_exhaustion_proof":[]}])
            self._jsonl(research / "question_source_tasks.jsonl", [{"task_id":"T1","target_id":"X","question_to_answer":question,"budget":{"max_queries":1,"max_candidates":2,"max_fetches":1},"query_intent":{"generator_kind":"REAL_LLM","literal_queries":["X 2026 official fact"]},"adequacy_route_attempts":[{"route_category":route,"status":"ATTEMPTED","proof_id":"R1"} for route in routes]}])
            self._jsonl(research / "provider_requests.jsonl", [{"provider_request_record_id":"R1","source_task_id":"T1","actual_provider_call":False}])
            self._jsonl(research / "provider_fetch_results.jsonl", [{"source_task_id":"T1","acquisition_class":"SOURCE_EXHAUSTED"}])
            self._jsonl(research / "web_search_tasks.jsonl", [{"web_task_id":"W1","source_task_id":"T1","official_first_attempted":True,"search_call_executed":True,"status":"SEARCH_EXECUTED"}])
            result = finalize_dossier_question_closures(dossier_root=dossier, source_research_roots=(research,))
            self.assertEqual(result["status"], "DOSSIER_QUESTION_CLOSURE_PASS")
            row=json.loads((dossier/"question_closure.jsonl").read_text().splitlines()[0])
            self.assertEqual(row["status"], "EVALUATED_ABSENT")
            self.assertEqual(row["search_exhaustion_proof"],["R1","W1"])

    def test_validated_scoring_closure_promotes_pending_question(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            dossier, research = root / "dossier", root / "research"
            dossier.mkdir(); research.mkdir()
            question = "Is current margin conversion visible?"
            routes = ["OFFICIAL", "ISSUER_IR", "INDEPENDENT", "COUNTER", "SUPERSESSION"]
            self._jsonl(dossier / "question_source_tasks.jsonl", [{"target_id":"X","question_family_id":"F1","question_to_answer":question,"as_of_date":"2026-07-11","required_route_categories":routes}])
            self._jsonl(dossier / "question_closure.jsonl", [{"target_id":"X","question_family_id":"F1","status":"PROVIDER_PENDING","search_exhaustion_proof":[]}])
            self._jsonl(dossier / "question_closure_v2.jsonl", [{"target_id":"X","question_family_id":"F1","status":"PARTIALLY_SUPPORTED_SCORING","supporting_claim_ids":["C1"]}])
            self._jsonl(dossier / "accepted_current_claims.jsonl", [{"claim_id":"C1","target_id":"X","accepted":True}])
            self._jsonl(research / "question_source_tasks.jsonl", [{"task_id":"T1","target_id":"X","question_to_answer":question,"budget":{"max_queries":1,"max_candidates":2,"max_fetches":1},"query_intent":{"generator_kind":"REAL_LLM","literal_queries":["X current margin conversion"]},"adequacy_route_attempts":[{"route_category":route,"status":"ATTEMPTED","proof_id":"R1"} for route in routes]}])
            self._jsonl(research / "provider_requests.jsonl", [{"provider_request_record_id":"R1","source_task_id":"T1","actual_provider_call":True,"source_class":"DART"}])
            self._jsonl(research / "provider_fetch_results.jsonl", [{"provider_fetch_result_id":"F1","source_task_id":"T1","source_class":"DART","acquisition_class":"REAL_PROVIDER_FETCH"}])
            self._jsonl(research / "web_search_tasks.jsonl", [])
            self._jsonl(research / "evidence_documents.jsonl", [{"document_id":"D1","source_task_ids":["T1"],"source_class":"DART","published_at":"2026-06-01","content_text":"X current margin conversion evidence"}])

            result = finalize_dossier_question_closures(
                dossier_root=dossier,
                source_research_roots=(research,),
            )

            self.assertEqual(result["status"], "DOSSIER_QUESTION_CLOSURE_PASS")
            row = json.loads((dossier / "question_closure.jsonl").read_text().splitlines()[0])
            self.assertEqual(row["status"], "PARTIALLY_SUPPORTED_SCORING")
            self.assertEqual(row["supporting_claim_ids"], ["C1"])

    @staticmethod
    def _jsonl(path: Path, rows) -> None:
        path.write_text("".join(json.dumps(row)+"\n" for row in rows))


if __name__ == "__main__": unittest.main()
