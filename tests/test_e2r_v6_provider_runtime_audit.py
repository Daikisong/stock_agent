from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from e2r.cli.compile_e2r_v6_provider_runtime_audit import _write_json_atomic
from e2r.production.v6_provider_runtime_audit import (
    PROVIDER_RUNTIME_AUDIT_FAIL,
    compile_provider_runtime_audit,
)
from e2r.research_brain.researcher_mode.artifact_lifecycle import (
    PROVIDER_RUNTIME_AUDIT_PASS,
    PROVIDER_RUNTIME_AUDIT_SCHEMA,
)


def _call(call_id: str, provider_name: str = "COLLABORATION_CODEX") -> dict[str, object]:
    return {
        "provider_call_id": call_id,
        "provider_name": provider_name,
        "status": "COMPLETED",
        "provider_error_count": 0,
        "score_or_stage_authority": False,
    }


def _fact(fact_id: str, provider_name: str = "COLLABORATION_CODEX") -> dict[str, object]:
    return {
        "fact_id": fact_id,
        "extraction_provider_name": provider_name,
    }


class E2RV6ProviderRuntimeAuditTests(unittest.TestCase):
    def test_exact_receipt_rows_compile_the_provider_pass_leaf(self):
        result = compile_provider_runtime_audit(
            as_of_date="2026-08-09",
            provider_calls=[
                _call("CALL-1"),
                _call(
                    "CALL-2",
                    "COLLABORATION_CODEX_SUBAGENT_STRUCTURED_RESEARCHER_MODE",
                ),
            ],
            scoring_facts=[_fact("FACT-1"), _fact("FACT-2")],
        )

        self.assertEqual(result["schema_version"], PROVIDER_RUNTIME_AUDIT_SCHEMA)
        self.assertEqual(result["status"], PROVIDER_RUNTIME_AUDIT_PASS)
        self.assertEqual(result["provider_call_counts"], {"COLLABORATION_CODEX": 2})
        self.assertEqual(
            result["scored_fact_provider_lineage_counts"],
            {"COLLABORATION_CODEX": 2},
        )
        self.assertEqual(result["critical_count_sum"], 0)
        self.assertFalse(result["production_readiness_authority"])

    def test_prohibited_runtime_or_inherited_lineage_cannot_pass(self):
        result = compile_provider_runtime_audit(
            as_of_date="2026-08-09",
            provider_calls=[_call("CALL-1", "QWEN")],
            scoring_facts=[_fact("FACT-1", "OLLAMA")],
        )

        self.assertEqual(result["status"], PROVIDER_RUNTIME_AUDIT_FAIL)
        self.assertEqual(result["qwen_call_count"], 1)
        self.assertEqual(result["inherited_ollama_scored_fact_count"], 1)
        self.assertGreater(result["critical_count_sum"], 0)

    def test_duplicate_call_or_direct_score_authority_fails_closed(self):
        rows = [_call("CALL-1"), _call("CALL-1")]
        rows[0]["score_or_stage_authority"] = True
        result = compile_provider_runtime_audit(
            as_of_date="2026-08-09",
            provider_calls=rows,
            scoring_facts=[_fact("FACT-1")],
        )

        self.assertEqual(result["status"], PROVIDER_RUNTIME_AUDIT_FAIL)
        self.assertGreaterEqual(result["critical_count_sum"], 2)

    def test_unknown_scored_fact_provider_cannot_hide_behind_clean_calls(self):
        result = compile_provider_runtime_audit(
            as_of_date="2026-08-09",
            provider_calls=[_call("CALL-1")],
            scoring_facts=[_fact("FACT-1", "UNKNOWN_PROVIDER")],
        )

        self.assertEqual(result["status"], PROVIDER_RUNTIME_AUDIT_FAIL)
        self.assertEqual(
            result["scored_fact_provider_lineage_counts"],
            {"UNKNOWN_PROVIDER": 1},
        )
        self.assertGreater(result["critical_count_sum"], 0)

    def test_atomic_writer_does_not_follow_a_parent_symlink(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            victim = root / "victim"
            victim.mkdir()
            alias = root / "alias"
            alias.symlink_to(victim, target_is_directory=True)
            with self.assertRaises(OSError):
                _write_json_atomic(alias / "provider_runtime_audit.json", {"status": "PASS"})
            self.assertFalse((victim / "provider_runtime_audit.json").exists())


if __name__ == "__main__":
    unittest.main()
