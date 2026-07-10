from __future__ import annotations

import json
import unittest
from pathlib import Path

from e2r.research_brain.runtime.live_materialization.adaptive_gap_closure import (
    _append_only_entries,
)


class LiveAdaptiveGapClosureTest(unittest.TestCase):
    def test_append_only_ledger_hash_chain_preserves_every_entry(self) -> None:
        entries = _append_only_entries(
            (
                {
                    "entry_type": "MATERIAL_GAP_OPEN",
                    "target_id": "000001",
                    "source_task_id": "TASK-1",
                    "claim_id": None,
                    "status": "SOURCE_PENDING",
                    "reason_code": "GENERIC_CONTEXT_ONLY",
                    "reason_detail": "official document did not resolve the question",
                },
                {
                    "entry_type": "ADAPTIVE_RETRY_PLANNED",
                    "target_id": "000001",
                    "source_task_id": "TASK-1",
                    "claim_id": None,
                    "status": "COMPLETE",
                    "reason_code": "CHANGE_DOCUMENT_SECTION_AND_QUERY",
                    "reason_detail": "a new LLM query",
                },
            )
        )

        self.assertEqual([item.sequence for item in entries], [1, 2])
        self.assertEqual(entries[0].previous_entry_hash, "0" * 64)
        self.assertEqual(entries[1].previous_entry_hash, entries[0].entry_hash)
        self.assertNotEqual(entries[0].entry_hash, entries[1].entry_hash)

    def test_live_operational_audit_keeps_every_material_gap_pending(self) -> None:
        path = (
            Path(__file__).resolve().parents[1]
            / "docs"
            / "operational"
            / "e2r_live_adaptive_gap_audit.json"
        )
        audit = json.loads(path.read_text(encoding="utf-8"))

        self.assertEqual(audit["status"], "PHASE_29_ACCEPTED")
        self.assertEqual(audit["adaptive_attempt_count"], 9)
        self.assertEqual(audit["new_llm_query_count"], 18)
        self.assertEqual(audit["score_valid_true_count"], 0)
        self.assertEqual(sum(audit["critical_counts"].values()), 0)
        self.assertFalse(audit["safety"]["deterministic_fallback_query_used"])
        self.assertFalse(audit["safety"]["same_query_repeated"])


if __name__ == "__main__":
    unittest.main()
