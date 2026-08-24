from __future__ import annotations

import json
from pathlib import Path
import unittest

from e2r.pro_first.research_contracts import (
    CROSS_GUARD_IDS,
    ProResearchPromptCompilerV3,
    load_research_contract,
)
from e2r.pro_first.research_contracts.prompt_compiler_v3 import (
    MAX_INITIAL_PROMPT_CHARS,
    VERIFIER_PREFLIGHT_FALSE_FIELDS,
    VERIFIER_PREFLIGHT_TRUE_FIELDS,
)
from e2r.pro_first.research_contracts.snapshot_audit_v3 import (
    ATOMIC_EVIDENCE_REQUIREMENT_MARKERS,
)


ROOT = Path(__file__).resolve().parents[1]
SNAPSHOTS = (
    ROOT / "docs/operational/e2r_pro_first_v2_1/prompt_snapshots_v3"
)
AUDIT = (
    ROOT
    / "docs/operational/e2r_pro_first_v2_1/initial_prompt_v3_snapshot_audit.json"
)


class ProFirstV21InitialPromptV3Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.audit = json.loads(AUDIT.read_text(encoding="utf-8"))

    def snapshot(self, archetype_id: str) -> str:
        return (SNAPSHOTS / f"{archetype_id}.md").read_text(encoding="utf-8")

    def test_all_36_canonical_contract_snapshots_pass(self) -> None:
        self.assertEqual(self.audit["status"], "PASS")
        self.assertEqual(self.audit["critical_count"], 0)
        self.assertEqual(self.audit["canonical_contract_count"], 36)
        self.assertEqual(self.audit["prompt_snapshot_count"], 36)
        self.assertEqual(self.audit["primary_prompt_snapshot_count"], 32)
        self.assertEqual(self.audit["cross_guard_prompt_snapshot_count"], 4)
        self.assertEqual(len(tuple(SNAPSHOTS.glob("*.md"))), 36)
        self.assertTrue(
            all(not row["failure_codes"] for row in self.audit["snapshots"])
        )
        self.assertTrue(all(value == 0 for value in self.audit["counters"].values()))

    def test_atomic_evidence_contract_is_common_to_all_snapshots(self) -> None:
        for path in SNAPSHOTS.glob("*.md"):
            prompt = path.read_text(encoding="utf-8")
            for marker in ATOMIC_EVIDENCE_REQUIREMENT_MARKERS:
                self.assertIn(marker, prompt, f"{path.name}: {marker}")

    def test_all_preflight_fields_and_derived_separation_are_explicit(self) -> None:
        fields = (*VERIFIER_PREFLIGHT_TRUE_FIELDS, *VERIFIER_PREFLIGHT_FALSE_FIELDS)
        for path in SNAPSHOTS.glob("*.md"):
            prompt = path.read_text(encoding="utf-8")
            for field in fields:
                self.assertIn(f'"{field}"', prompt, path.name)
                self.assertIn(f"`{field}`", prompt, path.name)
            self.assertIn("DerivedMetricV3", prompt, path.name)
            self.assertIn("`input_fact_ids`", prompt, path.name)
            self.assertIn("quoted atomic fact에 계산 결과를 섞지 않는다", prompt)

    def test_exact_v3_output_schema_and_authority_boundary_are_embedded(self) -> None:
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
            prompt = path.read_text(encoding="utf-8")
            lowered = prompt.casefold()
            self.assertIn('"const": "e2r_pro_research_dossier_v3"', prompt)
            self.assertIn('"source_documents"', prompt)
            self.assertIn('"derived_metrics"', prompt)
            self.assertIn("score_authority: `false`", prompt)
            self.assertIn("stage_authority: `false`", prompt)
            self.assertNotIn('"score_authority": true', lowered)
            self.assertNotIn('"stage_authority": true', lowered)
            for token in forbidden:
                self.assertNotIn(token, lowered, path.name)

    def test_primary_snapshot_has_only_its_questions_plus_cross_guards(self) -> None:
        c06_prompt = self.snapshot("C06_HBM_MEMORY_CUSTOMER_CAPACITY")
        c06 = load_research_contract("C06_HBM_MEMORY_CUSTOMER_CAPACITY")
        c17 = load_research_contract("C17_CHEMICAL_COMMODITY_MARGIN_SPREAD")
        for question in c06["question_families"]:
            self.assertIn(f"`{question['question_family_id']}`", c06_prompt)
        for guard_id in CROSS_GUARD_IDS:
            guard = load_research_contract(guard_id)
            for question in guard["question_families"]:
                self.assertIn(f"`{question['question_family_id']}`", c06_prompt)
        for question in c17["question_families"]:
            self.assertNotIn(f"`{question['question_family_id']}`", c06_prompt)

    def test_compiler_supports_three_selected_primary_contracts(self) -> None:
        selected = (
            "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD",
            "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
        )
        compiled = ProResearchPromptCompilerV3().compile(
            packet=_packet(selected),
            primary_archetype_ids=selected,
            conversation_id="FRESH-CONVERSATION",
            research_pass_id="PROPASS-FRESH-INITIAL",
        )
        self.assertEqual(compiled.primary_archetype_ids, selected)
        self.assertEqual(compiled.contract_ids, (*selected, *CROSS_GUARD_IDS))
        self.assertLessEqual(len(compiled.prompt_text), MAX_INITIAL_PROMPT_CHARS)
        self.assertIn("FRESH-CONVERSATION", compiled.prompt_text)
        self.assertEqual(compiled.to_receipt()["atomic_evidence_contract"], True)
        self.assertIs(compiled.to_receipt()["score_authority"], False)
        self.assertIs(compiled.to_receipt()["stage_authority"], False)

    def test_template_and_compiler_have_no_c06_specific_hardcoding(self) -> None:
        template = (
            ROOT / "configs/prompts/e2r_pro_v3_initial_full_research.md"
        ).read_text(encoding="utf-8")
        compiler_source = (
            ROOT
            / "src/e2r/pro_first/research_contracts/prompt_compiler_v3.py"
        ).read_text(encoding="utf-8")
        for text in (template, compiler_source):
            self.assertNotIn("C06_HBM_MEMORY_CUSTOMER_CAPACITY", text)
            self.assertNotIn("HBM 장기공급계약", text)

    def test_forbidden_answer_fields_are_rejected_before_compile(self) -> None:
        packet = dict(_packet(("C17_CHEMICAL_COMMODITY_MARGIN_SPREAD",)))
        packet["gold_stage"] = "3-Green"
        with self.assertRaisesRegex(ValueError, "forbidden answer field"):
            ProResearchPromptCompilerV3().compile(
                packet=packet,
                primary_archetype_ids=(
                    "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD",
                ),
            )

    def test_v2_packet_cannot_silently_enter_v3_prompt(self) -> None:
        packet = dict(_packet(("C17_CHEMICAL_COMMODITY_MARGIN_SPREAD",)))
        packet["schema_version"] = "e2r_pro_research_packet_v2"
        with self.assertRaisesRegex(ValueError, "requires ResearchPacketV3"):
            ProResearchPromptCompilerV3().compile(
                packet=packet,
                primary_archetype_ids=(
                    "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD",
                ),
            )

    def test_selected_contract_cannot_be_silently_omitted(self) -> None:
        selected = (
            "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD",
        )
        with self.assertRaisesRegex(ValueError, "exactly match"):
            ProResearchPromptCompilerV3().compile(
                packet=_packet(selected),
                primary_archetype_ids=(selected[0],),
            )


def _packet(archetypes: tuple[str, ...]) -> dict[str, object]:
    return {
        "schema_version": "e2r_pro_research_packet_v3",
        "job_id": "PROJOB-PROMPT-V3-TEST",
        "run_id": "PRORUN-PROMPT-V3-TEST",
        "target": {
            "target_id": "BLIND-TEST",
            "symbol": "BLIND-TEST",
            "company_name": "블라인드 테스트 대상",
            "aliases": [],
        },
        "as_of_date": "2026-08-22",
        "research_mode": "FULL_RESEARCH",
        "candidate_archetypes": list(archetypes),
        "selected_archetypes": list(archetypes),
        "trigger_summary": [],
        "business_snapshot": {},
        "structured_financial_snapshot": {},
        "revision_valuation_snapshot": {},
        "known_positive_facts": [],
        "known_counterfacts": [],
        "score_authority": False,
        "stage_authority": False,
    }


if __name__ == "__main__":
    unittest.main()
