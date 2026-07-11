from __future__ import annotations

import unittest

from e2r.research_brain.runtime.scoring_contracts import load_scoring_policy_v2


class RiskDirectionPolicyTests(unittest.TestCase):
    def test_risk_open_is_counter_only_and_nonzero(self) -> None:
        policy = load_scoring_policy_v2()
        self.assertEqual(
            policy.cap_for(support_type="RISK_OPEN", direction="SUPPORT"),
            0.0,
        )
        self.assertEqual(
            policy.cap_for(support_type="RISK_OPEN", direction="COUNTER"),
            1.0,
        )

    def test_risk_resolved_releases_but_does_not_keep_penalty(self) -> None:
        policy = load_scoring_policy_v2()
        self.assertEqual(
            policy.cap_for(support_type="RISK_RESOLVED", direction="COUNTER"),
            0.0,
        )
        self.assertEqual(
            policy.cap_for(support_type="RISK_RESOLVED", direction="RESOLUTION"),
            1.0,
        )


if __name__ == "__main__":
    unittest.main()
