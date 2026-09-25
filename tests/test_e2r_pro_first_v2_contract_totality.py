from __future__ import annotations

import json
from pathlib import Path
import unittest

from e2r.pro_first.research_contracts import (
    CROSS_GUARD_IDS,
    compile_contract_totality_audit,
    load_all_research_contracts,
    select_contract_bundle,
)


ROOT = Path(__file__).resolve().parents[1]


class ProFirstV2ContractTotalityTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.contracts = load_all_research_contracts()
        cls.audit = compile_contract_totality_audit(ROOT)

    def test_canonical_roster_is_36(self) -> None:
        canonical = json.loads(
            (ROOT / "configs/e2r_archetype_evidence_contracts_v12.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(canonical["contract_count"], 36)
        self.assertEqual(len(canonical["contracts"]), 36)

    def test_research_contract_roster_is_36(self) -> None:
        self.assertEqual(len(self.contracts), 36)
        self.assertEqual(self.audit["counters"]["missing_contract_count"], 0)
        self.assertEqual(self.audit["counters"]["extra_unknown_contract_count"], 0)

    def test_every_required_primitive_has_question(self) -> None:
        self.assertEqual(
            self.audit["counters"]["required_primitive_unmapped_count"],
            0,
        )

    def test_every_green_gate_has_question(self) -> None:
        self.assertEqual(
            self.audit["counters"]["green_gate_primitive_unmapped_count"],
            0,
        )

    def test_every_guard_has_counter_or_hard_break_question(self) -> None:
        self.assertEqual(
            self.audit["counters"]["guard_primitive_unmapped_count"],
            0,
        )
        for contract in self.contracts:
            counter_primitives = {
                primitive
                for question in contract["question_families"]
                if set(question["question_roles"]).intersection(
                    {"COUNTER_HARD_BREAK", "LIFECYCLE_SUPERSESSION", "GUARD_ONLY"}
                )
                for primitive in question["required_primitives"]
            }
            self.assertFalse(
                set(contract["guard_primitives"]) - counter_primitives,
                contract["archetype_id"],
            )

    def test_every_question_has_source_role(self) -> None:
        self.assertEqual(
            self.audit["counters"]["question_without_source_role_count"],
            0,
        )
        self.assertTrue(
            all(
                question["required_source_roles"]
                for contract in self.contracts
                for question in contract["question_families"]
            )
        )

    def test_no_generic_filler_contract(self) -> None:
        self.assertEqual(self.audit["counters"]["generic_filler_contract_count"], 0)
        primary = [row for row in self.contracts if row["contract_role"] == "PRIMARY"]
        self.assertEqual(len(primary), 32)
        self.assertTrue(all(len(row["question_families"]) >= 5 for row in primary))
        texts = [
            question["question_text"]
            for contract in self.contracts
            for question in contract["question_families"]
        ]
        self.assertEqual(len(texts), 233)
        self.assertEqual(len(set(texts)), 233)

    def test_cross_guard_attached_to_primary_jobs(self) -> None:
        bundle = select_contract_bundle(
            (
                "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD",
                "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
            )
        )
        self.assertEqual(len(bundle.primary_contracts), 3)
        self.assertEqual(
            tuple(row["archetype_id"] for row in bundle.cross_guard_contracts),
            CROSS_GUARD_IDS,
        )
        self.assertEqual(len(bundle.contracts), 7)


if __name__ == "__main__":
    unittest.main()
