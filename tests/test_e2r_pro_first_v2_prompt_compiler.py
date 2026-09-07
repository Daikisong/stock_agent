from __future__ import annotations

import json
from pathlib import Path
import unittest

from e2r.pro_first.ids import canonical_hash
from e2r.pro_first.research_contracts import (
    ProResearchPromptCompilerV2,
    load_research_contract,
)


ROOT = Path(__file__).resolve().parents[1]
SNAPSHOTS = ROOT / "docs/operational/e2r_pro_first_v2/prompt_snapshots"
AUDIT = ROOT / "docs/operational/e2r_pro_first_v2/prompt_snapshot_audit.json"


class ProFirstV2PromptCompilerTest(unittest.TestCase):
    def snapshot(self, archetype_id: str) -> str:
        return (SNAPSHOTS / f"{archetype_id}.md").read_text(encoding="utf-8")

    def test_compile_all_36_prompt_snapshots(self) -> None:
        audit = json.loads(AUDIT.read_text(encoding="utf-8"))
        self.assertEqual(audit["status"], "PASS")
        self.assertEqual(audit["critical_count"], 0)
        self.assertEqual(audit["prompt_snapshot_count"], 36)
        self.assertEqual(len(tuple(SNAPSHOTS.glob("*.md"))), 36)
        for row in audit["snapshots"]:
            self.assertEqual(row["failure_codes"], [], row["archetype_id"])

    def test_c06_prompt_contains_hbm_questions(self) -> None:
        prompt = self.snapshot("C06_HBM_MEMORY_CUSTOMER_CAPACITY")
        for phrase in (
            "allocation·booking·commitment·LTA",
            "capacity sold-out·pre-sold",
            "qualification pass",
            "margin·FCF·cash conversion",
        ):
            self.assertIn(phrase, prompt)

    def test_c08_prompt_contains_customer_order_conversion_questions(self) -> None:
        prompt = self.snapshot("C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY")
        self.assertIn("named customer qualification", prompt)
        self.assertIn("repeat order·renewal·shipment·backlog", prompt)
        self.assertIn("issuer 매출·ASP·gross margin·OPM", prompt)

    def test_c15_prompt_contains_passthrough_inventory_phase_questions(self) -> None:
        prompt = self.snapshot("C15_MATERIAL_SPREAD_SUPERCYCLE")
        self.assertIn("ASP/pass-through", prompt)
        self.assertIn("재고평가·계약 가격 lag", prompt)
        self.assertIn("cycle phase·신규 공급·가격 반락", prompt)

    def test_c17_prompt_contains_realized_spread_questions(self) -> None:
        prompt = self.snapshot("C17_CHEMICAL_COMMODITY_MARGIN_SPREAD")
        self.assertIn("realized spread", prompt)
        self.assertIn("spot spread와 issuer 계약가격", prompt)
        self.assertIn("gross margin·OPM·EPS·FCF 전환", prompt)

    def test_c24_prompt_contains_endpoint_regulatory_partner_runway_questions(self) -> None:
        prompt = self.snapshot("C24_BIO_TRIAL_DATA_EVENT_RISK")
        for phrase in (
            "endpoint·control·통계계획",
            "규제기관 피드백·다음 단계·approval path",
            "partner/platform validation",
            "cash runway·추가 임상비",
        ):
            self.assertIn(phrase, prompt)

    def test_c28_prompt_contains_arr_nrr_retention_rpo_questions(self) -> None:
        prompt = self.snapshot("C28_SOFTWARE_SECURITY_CONTRACT_RETENTION")
        self.assertIn("ARR·recurring revenue·RPO/backlog", prompt)
        self.assertIn("GRR/NRR·renewal·churn", prompt)
        self.assertIn("retention bridge", prompt)

    def test_non_c06_prompt_not_polluted_by_hbm_literals(self) -> None:
        prompt = self.snapshot("C17_CHEMICAL_COMMODITY_MARGIN_SPREAD")
        c06 = load_research_contract("C06_HBM_MEMORY_CUSTOMER_CAPACITY")
        self.assertNotIn("C06_HBM_MEMORY_CUSTOMER_CAPACITY_Q", prompt)
        for question in c06["question_families"]:
            self.assertNotIn(question["question_text"], prompt)

    def test_prompt_does_not_force_complete(self) -> None:
        for path in SNAPSHOTS.glob("*.md"):
            prompt = path.read_text(encoding="utf-8")
            self.assertNotIn("research_status`는 `COMPLETE`", prompt, path.name)
            self.assertIn("특정 완료 상태를 형식적으로 강제하지 않는다", prompt, path.name)

    def test_prompt_does_not_expose_score_stage_gold(self) -> None:
        forbidden = (
            "expected_score",
            "expected_stage",
            "gold_score",
            "gold_stage",
            "gold_answer",
            "future_outcome",
            "forward_return",
        )
        for path in SNAPSHOTS.glob("*.md"):
            prompt = path.read_text(encoding="utf-8").casefold()
            for token in forbidden:
                self.assertNotIn(token, prompt, path.name)
            self.assertIn("score_authority: `false`", prompt, path.name)
            self.assertIn("stage_authority: `false`", prompt, path.name)

    def test_all_six_pass_templates_compile(self) -> None:
        compiler = ProResearchPromptCompilerV2()
        packet = {
            "job_id": "PROMPT-PASS-TEST",
            "run_id": "PROMPT-PASS-RUN",
            "target": {"symbol": "TEST", "company_name": "프롬프트검증"},
            "as_of_date": "2026-08-22",
            "candidate_archetypes": ["C28_SOFTWARE_SECURITY_CONTRACT_RETENTION"],
        }
        for pass_name in (
            "INITIAL_FULL_RESEARCH",
            "PUBLIC_GAP_CLOSURE",
            "COUNTER_SUPERSESSION_CLOSURE",
            "VERIFIER_REPAIR",
            "SATURATION_AUDIT",
            "DELTA_RESEARCH",
        ):
            selected_packet = packet
            if pass_name == "DELTA_RESEARCH":
                closure = {"status": "SUPPORTED_SCORING"}
                selected_packet = {
                    **packet,
                    "delta_context": {
                        "question_families_to_revisit": [
                            "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_Q02"
                        ],
                        "prior_question_closure_map": {
                            "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_Q02": {
                                **closure,
                                "closure_hash": canonical_hash(closure),
                            }
                        },
                        "reused_question_family_ids": [],
                    },
                }
            compiled = compiler.compile(
                packet=selected_packet,
                primary_archetype_ids=("C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",),
                pass_name=pass_name,
                conversation_id="CONVERSATION-SAME",
            )
            self.assertEqual(compiled.pass_name, pass_name)
            self.assertIn("CONVERSATION-SAME", compiled.prompt_text)
            self.assertEqual(len(compiled.prompt_hash), 64)

    def test_delta_reopens_only_impacted_questions(self) -> None:
        impacted = "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_Q02"
        reused = "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_Q01"
        impacted_closure = {"status": "SUPPORTED_SCORING"}
        reused_closure = {"status": "COUNTER_SUPPORTED"}
        packet = {
            "job_id": "PROMPT-DELTA-TEST",
            "run_id": "PROMPT-DELTA-RUN",
            "target": {"symbol": "TEST", "company_name": "델타검증"},
            "as_of_date": "2026-08-22",
            "candidate_archetypes": [
                "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION"
            ],
            "delta_context": {
                "question_families_to_revisit": [impacted],
                "prior_question_closure_map": {
                    impacted: {
                        **impacted_closure,
                        "closure_hash": canonical_hash(impacted_closure),
                    },
                    reused: {
                        **reused_closure,
                        "closure_hash": canonical_hash(reused_closure),
                    },
                },
                "reused_question_family_ids": [reused],
                "stale_primitive_ids": ["renewal_retention"],
            },
        }

        compiled = ProResearchPromptCompilerV2().compile(
            packet=packet,
            primary_archetype_ids=(
                "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
            ),
            pass_name="DELTA_RESEARCH",
        )

        self.assertEqual(compiled.mandatory_question_ids, (impacted,))
        self.assertIn(impacted, compiled.prompt_text)
        self.assertNotIn(f"`{reused}` —", compiled.prompt_text)
        self.assertIn('"reused_question_family_ids": [', compiled.prompt_text)

    def test_delta_prompt_rejects_tampered_prior_closure(self) -> None:
        impacted = "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_Q02"
        packet = {
            "job_id": "PROMPT-DELTA-TAMPER",
            "run_id": "PROMPT-DELTA-TAMPER-RUN",
            "target": {"symbol": "TEST", "company_name": "델타검증"},
            "as_of_date": "2026-08-22",
            "candidate_archetypes": [
                "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION"
            ],
            "delta_context": {
                "question_families_to_revisit": [impacted],
                "prior_question_closure_map": {
                    impacted: {
                        "status": "SUPPORTED_SCORING",
                        "closure_hash": "a" * 64,
                    },
                },
                "reused_question_family_ids": [],
            },
        }

        with self.assertRaisesRegex(ValueError, "closure hash mismatch"):
            ProResearchPromptCompilerV2().compile(
                packet=packet,
                primary_archetype_ids=(
                    "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
                ),
                pass_name="DELTA_RESEARCH",
            )


if __name__ == "__main__":
    unittest.main()
