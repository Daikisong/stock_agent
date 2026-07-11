from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.research_brain.runtime.scoring_contracts import (
    ScoringContractIncompleteError,
    audit_scoring_schema_totality,
    load_scoring_contract_catalog,
    load_scoring_policy_v2,
)


class ScoringSchemaTotalityTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]

    def test_all_36_archetypes_inherit_total_source_and_temporal_policy(self) -> None:
        policy = load_scoring_policy_v2()
        catalog = load_scoring_contract_catalog()
        self.assertEqual(len(catalog.contracts), 36)
        expected_source = set(policy.enum_registry["source_families"])
        expected_temporal = set(policy.enum_registry["temporal_scopes"])
        for contract in catalog.contracts.values():
            self.assertEqual(set(contract.source_tier_caps), expected_source)
            self.assertEqual(set(contract.freshness_caps), expected_temporal)

    def test_operational_totality_audit_has_no_critical_count(self) -> None:
        audit = audit_scoring_schema_totality(repo_root=self.ROOT)
        artifact = json.loads(
            (
                self.ROOT
                / "docs/operational/e2r_scoring_schema_totality_audit.json"
            ).read_text()
        )
        self.assertEqual(audit, artifact)
        self.assertEqual(audit["status"], "SCORING_SCHEMA_TOTALITY_PASS")
        self.assertEqual(audit["total_schema_archetype_count"], 36)
        self.assertEqual(audit["critical_count_sum"], 0)

    def test_missing_policy_key_is_hard_contract_error(self) -> None:
        payload = json.loads(
            (self.ROOT / "configs/e2r_scoring_policy_v2.json").read_text()
        )
        del payload["support_type_policies"]["PARTIAL_BRIDGE"]
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "policy.json"
            path.write_text(json.dumps(payload), encoding="utf-8")
            with self.assertRaisesRegex(
                ScoringContractIncompleteError,
                "SCORING_CONTRACT_INCOMPLETE:support_types",
            ):
                load_scoring_policy_v2(path)


if __name__ == "__main__":
    unittest.main()
