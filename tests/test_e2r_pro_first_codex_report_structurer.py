from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
import unittest

from e2r.pro_first.dossier import CodexProReportDossierStructurer


ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class _Response:
    payload: dict
    raw_response: str = "provider-raw-response"


class _Transport:
    def __init__(self, dossier: dict) -> None:
        self.dossier = dossier
        self.calls: list[dict] = []

    def complete(self, *, prompt, output_schema, schema_name):
        self.calls.append(
            {
                "prompt": prompt,
                "output_schema": output_schema,
                "schema_name": schema_name,
            }
        )
        return _Response(
            payload={
                "dossier_json": json.dumps(
                    self.dossier,
                    ensure_ascii=False,
                    sort_keys=True,
                )
            }
        )


class CodexProReportDossierStructurerTest(unittest.TestCase):
    def test_structures_only_report_bound_dossier_without_score_authority(self) -> None:
        transport = _Transport(self._dossier())
        result = self._structurer(transport).structure(**self._inputs())

        self.assertEqual(result.dossier["material_facts"], [])
        self.assertEqual(result.receipt["material_fact_count"], 0)
        self.assertEqual(result.receipt["mandatory_question_count"], 2)
        self.assertTrue(result.receipt["browser_result_hash_bound"])
        self.assertFalse(result.receipt["new_research_allowed"])
        self.assertFalse(result.receipt["score_authority"])
        self.assertFalse(result.receipt["stage_authority"])
        prompt = transport.calls[0]["prompt"]
        self.assertIn("Do not browse, fetch, call tools", prompt)
        self.assertIn("keep it out of facts", prompt)
        self.assertIn("COMPLETED_PRO_REPORT", prompt)
        self.assertEqual(
            set(transport.calls[0]["output_schema"]["properties"]),
            {"dossier_json"},
        )

    def test_changed_transport_identity_is_rejected(self) -> None:
        dossier = self._dossier()
        dossier["conversation_id"] = "different-conversation"

        with self.assertRaisesRegex(ValueError, "changed identity field"):
            self._structurer(_Transport(dossier)).structure(**self._inputs())

    def test_missing_mandatory_question_is_rejected(self) -> None:
        dossier = self._dossier()
        dossier["question_family_results"] = dossier["question_family_results"][:1]

        with self.assertRaisesRegex(ValueError, "omitted mandatory question"):
            self._structurer(_Transport(dossier)).structure(**self._inputs())

    @staticmethod
    def _structurer(transport: _Transport) -> CodexProReportDossierStructurer:
        return CodexProReportDossierStructurer(
            transport,
            schema_path=ROOT / "configs/e2r_pro_research_dossier_v3.schema.json",
        )

    @staticmethod
    def _inputs() -> dict:
        return {
            "report_text": (
                "[[E2R_PRO_JOB_ID:PROJOB-STRUCTURE]]\n"
                "[[E2R_PRO_RUN_ID:PRORUN-STRUCTURE]]\n"
                "Readable report with one visible citation URL."
            ),
            "packet": {
                "job_id": "PROJOB-STRUCTURE",
                "run_id": "PRORUN-STRUCTURE",
                "target": {
                    "target_id": "BLIND-TARGET",
                    "symbol": "BLIND-TARGET",
                    "company_name": "블라인드 대상",
                    "aliases": [],
                },
                "as_of_date": "2026-08-23",
                "candidate_archetypes": ["C01_ORDER_BACKLOG_MARGIN_BRIDGE"],
            },
            "conversation_id": "fresh-conversation",
            "research_pass_id": "PROPASS-FRESH-INITIAL",
            "prompt_hash": "a" * 64,
            "response_hash": "b" * 64,
            "mandatory_question_ids": ("Q01", "Q02"),
        }

    @staticmethod
    def _dossier() -> dict:
        return {
            "schema_version": "e2r_pro_research_dossier_v3",
            "job_id": "PROJOB-STRUCTURE",
            "run_id": "PRORUN-STRUCTURE",
            "conversation_id": "fresh-conversation",
            "research_pass_id": "PROPASS-FRESH-INITIAL",
            "parent_pass_id": None,
            "as_of_date": "2026-08-23",
            "source_documents": [],
            "material_facts": [],
            "counterfacts": [],
            "resolution_facts": [],
            "question_family_results": [
                {"question_family_id": "Q01", "status": "VERIFIER_REPAIR_REQUIRED"},
                {"question_family_id": "Q02", "status": "VERIFIER_REPAIR_REQUIRED"},
            ],
            "score_authority": False,
            "stage_authority": False,
        }


if __name__ == "__main__":
    unittest.main()
