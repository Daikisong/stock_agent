from __future__ import annotations

import json
import unittest
from pathlib import Path

from e2r.research_brain.scoring.evidence_to_score_known_bad import (
    CASES,
    PASS_STATUS,
    compile_evidence_to_score_known_bad_audit,
)


EXPECTED_MUTATIONS = (
    "PARTIAL_BRIDGE cap 누락이 조용히 0점",
    "RISK_OPEN cap 누락이 조용히 0점",
    "RISK_RESOLVED cap 누락이 조용히 0점",
    "source family cap 누락이 조용히 0점",
    "temporal cap 누락이 조용히 0점",
    "SUPPORTED 질문이 zero-credit",
    "PARTIALLY_SUPPORTED 질문이 zero-credit",
    "SUPPORTED 질문이 VERIFIED_ABSENT",
    "positive claim이 VERIFIED_ABSENT",
    "internal rejection이 absence로 위장",
    "provider failure가 absence",
    "budget exhaustion이 absence",
    "Foundry Tesla claim이 HBM allocation 지원",
    "same issuer wrong segment score",
    "adjacent substrate가 target HBM capacity",
    "accepted claim eligibility boolean 모순",
    "component score without eligibility decision",
    "support+counter인데 counter 무시",
    "capacity expansion counter가 bottleneck에 0",
    "risk resolved가 계속 감점",
    "같은 fact 여러 claim 중복 credit",
    "같은 document 여러 claim 정보신뢰도 중복",
    "repost 여러 문서 중복 credit",
    "claim 수만으로 company_event_score 60",
    "any claim이 high_quality_company_event",
    "full-thesis Stage에 daily event overlay 주입",
    "gold URL production seed 주입",
    "gold fact production prompt 누수",
    "critical gold material fact miss인데 PASS",
    "frozen corpus bug를 새 문서로 가림",
    "source proxy score",
    "historical outcome prompt leak",
    "Stage/score/impact/component trace mismatch",
    "full_score_valid인데 semantic reconciliation fail",
    "report-only readiness 승격",
)


class SemanticScoringKnownBadTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]

    def test_goal_mutation_roster_is_exact_and_all_detectors_pass(self) -> None:
        audit = compile_evidence_to_score_known_bad_audit()
        self.assertEqual(tuple(case.mutation for case in CASES), EXPECTED_MUTATIONS)
        self.assertEqual(
            tuple(case.case_id for case in CASES),
            tuple(f"KB-{index:02d}" for index in range(1, 36)),
        )
        self.assertTrue(all(case.detector_ids for case in CASES))
        self.assertEqual(audit["status"], PASS_STATUS)
        self.assertEqual(audit["required_case_count"], 35)
        self.assertEqual(audit["case_count"], 35)
        self.assertEqual(audit["critical_count_sum"], 0)

    def test_committed_operational_audit_is_recompiled(self) -> None:
        expected = compile_evidence_to_score_known_bad_audit()
        actual = json.loads(
            (
                self.ROOT
                / "docs/operational/e2r_semantic_scoring_known_bad_audit.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
