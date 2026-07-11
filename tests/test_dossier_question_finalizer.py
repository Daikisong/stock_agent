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
            self._jsonl(dossier / "question_source_tasks.jsonl", [{"target_id":"X","question_family_id":"F1","question_to_answer":question}])
            self._jsonl(dossier / "question_closure.jsonl", [{"target_id":"X","question_family_id":"F1","status":"PROVIDER_PENDING","search_exhaustion_proof":[]}])
            self._jsonl(research / "question_source_tasks.jsonl", [{"task_id":"T1","target_id":"X","question_to_answer":question,"budget":{"max_queries":1,"max_candidates":2,"max_fetches":1},"query_intent":{"generator_kind":"REAL_LLM","literal_queries":["X 2026 official fact"]}}])
            self._jsonl(research / "provider_requests.jsonl", [{"provider_request_record_id":"R1","source_task_id":"T1","actual_provider_call":False}])
            self._jsonl(research / "provider_fetch_results.jsonl", [{"source_task_id":"T1","acquisition_class":"SOURCE_EXHAUSTED"}])
            self._jsonl(research / "web_search_tasks.jsonl", [{"web_task_id":"W1","source_task_id":"T1","official_first_attempted":True,"search_call_executed":True,"status":"SEARCH_EXECUTED"}])
            result = finalize_dossier_question_closures(dossier_root=dossier, source_research_roots=(research,))
            self.assertEqual(result["status"], "DOSSIER_QUESTION_CLOSURE_PASS")
            row=json.loads((dossier/"question_closure.jsonl").read_text().splitlines()[0])
            self.assertEqual(row["status"], "EVALUATED_ABSENT")
            self.assertEqual(row["search_exhaustion_proof"],["R1","W1"])

    @staticmethod
    def _jsonl(path: Path, rows) -> None:
        path.write_text("".join(json.dumps(row)+"\n" for row in rows))


if __name__ == "__main__": unittest.main()
