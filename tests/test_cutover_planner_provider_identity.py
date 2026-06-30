import unittest
import json
import subprocess
from pathlib import Path
from unittest.mock import patch

from e2r.production.cutover_shadow import ProductionCutoverConfig, _planner_call_count, build_production_cutover_bundle
from e2r.production.official_live_shadow import _real_codex_planner_runs_for_events


class CutoverPlannerProviderIdentityTests(unittest.TestCase):
    def test_planner_report_counts_model_null_as_blocker_not_ready_claim(self):
        bundle = build_production_cutover_bundle(
            config=ProductionCutoverConfig(as_of_date="2026-06-30"),
            repo_root=".",
            command="unit-test",
        )
        planner = bundle["planner_provider_report"]["summary"]
        self.assertGreaterEqual(planner["real_planner_success_count"], 0)
        self.assertIn("planner_provider_model_null_count", planner)
        self.assertFalse(bundle["shadow_latest"]["production_ready"])

    def test_real_planner_path_records_codex_model_hashes_and_raw_payload(self):
        event = {
            "candidate_event_id": "CE-UNIT-005930-1",
            "symbol": "005930",
            "company_name": "삼성전자",
            "event_date": "2026-06-30",
            "detected_at": "2026-06-30",
            "source_family": "DART",
            "source_id": "https://dart.fss.or.kr/dsaf001/main.do?rcpNo=1",
            "event_type": "단일판매ㆍ공급계약체결",
            "event_title": "단일판매ㆍ공급계약체결",
            "event_summary": "삼성전자 OpenDART disclosure",
            "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
            "industry_code": "264",
            "issuer_directness": "DIRECT",
        }

        def fake_run(command, *, prompt, timeout):
            output_path = Path(command[command.index("-o") + 1])
            output_path.write_text(
                """
                {
                  "plans": [
                    {
                      "candidate_event_id": "CE-UNIT-005930-1",
                      "archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP",
                      "primitive_gap": "contract_quality",
                      "preferred_source_classes": ["DART"],
                      "fallback_source_classes": ["IssuerOfficial"],
                      "forbidden_source_classes": ["unbounded_general_search"],
                      "max_queries": 1,
                      "max_candidates": 2,
                      "max_fetches": 1,
                      "rationale": "official disclosure contract must be verified",
                      "red_team_checks": ["wrong subject"],
                      "planner_self_check": {
                        "score_keys_present": false,
                        "stage_keys_present": false,
                        "future_outcome_used": false
                      }
                    }
                  ]
                }
                """,
                encoding="utf-8",
            )
            return subprocess.CompletedProcess(command, 0, "", "")

        with patch.dict("os.environ", {"E2R_CODEX_PLANNER_MODEL": "gpt-test"}, clear=False), patch(
            "e2r.production.official_live_shadow._run_codex_command",
            side_effect=fake_run,
        ):
            rows = _real_codex_planner_runs_for_events((event,), repo_root=Path("."))
        row = rows["CE-UNIT-005930-1"]
        self.assertTrue(row["real_provider_success"])
        self.assertEqual(row["model"], "gpt-test")
        self.assertEqual(row["schema_validation_status"], "PASS")
        self.assertEqual(row["raw_response_payload"]["primitive_gap"], "contract_quality")
        self.assertTrue(row["prompt_hash"])
        self.assertTrue(row["response_hash"])

    def test_real_planner_batches_large_event_sets(self):
        events = tuple(
            {
                "candidate_event_id": f"CE-UNIT-005930-{idx}",
                "symbol": "005930",
                "company_name": "삼성전자",
                "event_date": "2026-06-30",
                "detected_at": "2026-06-30",
                "source_family": "DART",
                "source_id": f"https://dart.fss.or.kr/dsaf001/main.do?rcpNo={idx}",
                "event_type": "단일판매ㆍ공급계약체결",
                "event_title": "단일판매ㆍ공급계약체결",
                "event_summary": "삼성전자 OpenDART disclosure",
                "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
                "industry_code": "264",
                "issuer_directness": "DIRECT",
            }
            for idx in range(5)
        )
        calls = []

        def fake_run(command, *, prompt, timeout):
            payload = json.loads(prompt.rsplit("\n\n", 1)[-1])
            calls.append(tuple(event["candidate_event_id"] for event in payload["events"]))
            output_path = Path(command[command.index("-o") + 1])
            output_path.write_text(
                json.dumps(
                    {
                        "plans": [
                            {
                                "candidate_event_id": event["candidate_event_id"],
                                "archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP",
                                "primitive_gap": "contract_quality",
                                "preferred_source_classes": ["DART"],
                                "fallback_source_classes": ["IssuerOfficial"],
                                "forbidden_source_classes": ["unbounded_general_search"],
                                "max_queries": 1,
                                "max_candidates": 2,
                                "max_fetches": 1,
                                "rationale": "official disclosure contract must be verified",
                                "red_team_checks": ["wrong subject"],
                                "planner_self_check": {
                                    "score_keys_present": False,
                                    "stage_keys_present": False,
                                    "future_outcome_used": False,
                                },
                            }
                            for event in payload["events"]
                        ]
                    },
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )
            return subprocess.CompletedProcess(command, 0, "", "")

        with patch.dict("os.environ", {"E2R_CODEX_PLANNER_BATCH_SIZE": "2"}, clear=False), patch(
            "e2r.production.official_live_shadow._run_codex_command",
            side_effect=fake_run,
        ):
            rows = _real_codex_planner_runs_for_events(events, repo_root=Path("."))
        self.assertEqual(len(rows), 5)
        self.assertEqual([len(call) for call in calls], [2, 2, 1])
        self.assertTrue(all(row["real_provider_success"] for row in rows.values()))

    def test_sla_planner_call_count_uses_batches_not_event_rows(self):
        planner_rows = [
            {"candidate_event_id": "A", "batch_prompt_hash": "P1", "batch_response_hash": "R1"},
            {"candidate_event_id": "B", "batch_prompt_hash": "P1", "batch_response_hash": "R1"},
            {"candidate_event_id": "C", "batch_prompt_hash": "P2", "batch_response_hash": "R2"},
        ]
        self.assertEqual(_planner_call_count(planner_rows), 2)


if __name__ == "__main__":
    unittest.main()
