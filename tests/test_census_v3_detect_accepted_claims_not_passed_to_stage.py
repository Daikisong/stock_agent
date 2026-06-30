import unittest

from census_v3_test_helpers import read_jsonl, temp_census_v3_copy, write_jsonl
from e2r.census.leaf_artifact_auditor import audit_leaf_artifacts


class CensusV3DetectAcceptedClaimsNotPassedToStageTests(unittest.TestCase):
    def test_scored_rows_without_stage_claim_ids_fail(self):
        tmp, root = temp_census_v3_copy()
        self.addCleanup(tmp.cleanup)
        rows = read_jsonl(root / "census_stage_status.jsonl")
        for row in rows:
            if row.get("verified_score") is not None:
                row["accepted_claim_ids"] = []
        write_jsonl(root / "census_stage_status.jsonl", rows)
        audit = audit_leaf_artifacts(root)
        self.assertGreater(audit["critical_counts"]["claim_to_stage_unlinked_count"], 0)
        self.assertGreater(audit["critical_counts"]["accepted_claim_unused_in_stage_count"], 0)


if __name__ == "__main__":
    unittest.main()
