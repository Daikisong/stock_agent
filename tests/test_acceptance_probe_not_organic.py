from __future__ import annotations

import json
import unittest
from pathlib import Path

from e2r.research_brain.scoring import audit_probe_separation, partition_scoring_evidence


ROOT = Path(__file__).resolve().parents[1]


class AcceptanceProbeNotOrganicTests(unittest.TestCase):
    def test_controlled_probe_claim_is_excluded_from_scoring_plane(self) -> None:
        report = json.loads((ROOT / "docs/operational/e2r_live_acceptance_report.json").read_text())
        claim_id = report["accepted_claim_proof"]["claim_id"]
        current_rows = [json.loads(line) for line in (ROOT / "output/current_operation/live_2026-07-10/accepted_claims.jsonl").read_text().splitlines() if line.strip()]
        partition = partition_scoring_evidence(current_rows, controlled_probe_claim_ids=(claim_id,))
        audit = audit_probe_separation(partition=partition, scoring_decisions=())
        self.assertEqual(len(partition.organic_rows), 0)
        self.assertEqual(partition.origin_counts["CONTROLLED_CLAIM_PROBE"], 1)
        self.assertEqual(audit["status"], "CONTROLLED_CLAIM_PROBE_PASS")
        self.assertEqual(audit["critical_count_sum"], 0)

    def test_probe_no_score_decision_cannot_unlock_scoring_readiness(self) -> None:
        rows=({"claim_id":"PROBE-1","evidence_origin":"CONTROLLED_CLAIM_PROBE"},)
        partition=partition_scoring_evidence(rows,controlled_probe_claim_ids=("PROBE-1",))
        audit=audit_probe_separation(partition=partition,scoring_decisions=({"accepted_claim_ids":["PROBE-1"],"score_type":"NO_SCORE","scoring_readiness_eligible":True},))
        self.assertGreater(audit["critical_counts"]["probe_decision_merged_into_canonical_score_count"],0)
        self.assertGreater(audit["critical_counts"]["no_score_probe_unlocks_readiness_count"],0)

    def test_only_explicit_fetched_non_proxy_live_rows_are_organic(self) -> None:
        rows=({"claim_id":"ORG-1","evidence_origin":"ORGANIC_LIVE","source_proxy_only":False,"fetched":True,"source_url":"https://issuer.test/doc"},)
        partition=partition_scoring_evidence(rows)
        self.assertEqual([row["claim_id"] for row in partition.organic_rows],["ORG-1"])


if __name__=="__main__": unittest.main()
