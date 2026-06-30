import unittest

from e2r.production.cutover_v3 import _completion_labels_v3
from tests.cutover_v3_test_helpers import fake_a2, fake_provider_matrix


class CutoverV3NoReadyWithProviderBlockerTests(unittest.TestCase):
    def test_provider_blocker_prevents_cutover_and_production_ready(self):
        labels = _completion_labels_v3(
            provider_matrix=fake_provider_matrix(status="PROVIDER_COMPLETENESS_NOT_READY", blockers=1),
            multiday={"summary": {"status": "MULTIDAY_SHADOW_PASS"}},
            claim_audit={"summary": {"status": "CLAIM_EXTRACTOR_AUDIT_PASS"}},
            stage_distribution={"summary": {"status": "MEANINGFUL_STAGE_SPLIT_PASS"}},
            trigger_policy={"summary": {"status": "TRIGGER_POLICY_ENFORCED"}},
            operator_digest={"summary": {"status": "OPERATOR_DIGEST_PASS"}},
            sla={"summary": {"status": "SLA_PASS"}},
            static={"summary": {"critical_count_sum": 0, "production_blockers": ["provider completeness blockers remain"]}},
            a2=fake_a2(),
            final_cutover_approved=True,
        )
        self.assertNotIn("CUTOVER_READY", labels)
        self.assertNotIn("PRODUCTION_READY", labels)


if __name__ == "__main__":
    unittest.main()
