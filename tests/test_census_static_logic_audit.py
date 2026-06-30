import unittest

from e2r.census.census_audit import audit_census_mode


class CensusStaticLogicAuditTests(unittest.TestCase):
    def test_clean_stage_map_has_zero_critical_counts(self):
        rows = [
            {
                "symbol": "005930",
                "census_status": "SCANNED",
                "base_stage": "Stage0",
                "score_valid_status": "NO_CURRENT_EVENT",
                "stage_confidence": "LOW",
                "verified_score": None,
                "accepted_claim_count": 0,
                "market_anomaly_count": 0,
            }
        ]
        audit = audit_census_mode(eligible_symbols=["005930"], stage_status_rows=rows, checkpoints=[{"source_corpus_hash": "a", "config_hash": "b"}])
        self.assertEqual(audit["summary"]["critical_count_sum"], 0)
        self.assertEqual(audit["summary"]["status"], "CENSUS_STATIC_AUDIT_PASS")


if __name__ == "__main__":
    unittest.main()
