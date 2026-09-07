from __future__ import annotations

from datetime import datetime, timezone
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from e2r.pro_first.fresh_session import OldRunFreezeService
from e2r.pro_first.job_store import (
    OldDiagnosticRunFrozen,
    ProFirstJobStore,
)
from e2r.pro_first.models import ResearchMode, ScanWindow
from e2r.pro_first.multi_pass import ProMultiPassResearchOrchestrator
from e2r.pro_first.multi_pass.models import TransportPendingDecision


class ProFirstV21OldRunFreezeTest(unittest.TestCase):
    now = datetime(2026, 8, 25, 4, 30, tzinfo=timezone.utc)

    def setUp(self) -> None:
        self.temporary_directory = TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.root = Path(self.temporary_directory.name)
        self.store = ProFirstJobStore(
            self.root / "pro_first.sqlite3",
            now=lambda: self.now,
        )
        self.job = self._create_job("old")

    def _create_job(self, suffix: str):
        candidate = self.store.create_candidate(
            symbol="000660",
            company_name="SK하이닉스",
            as_of_date="2026-08-23",
            scan_window=ScanWindow.MORNING,
            trigger_fingerprint=f"fresh-session-{suffix}",
            research_mode=ResearchMode.FULL_RESEARCH,
            selection_receipt={"production_candidate": True},
            dedupe_key=f"fresh-session-{suffix}",
        )
        return self.store.create_job(
            candidate.candidate_id,
            archetype_ids=("C06_HBM_MEMORY_CUSTOMER_CAPACITY",),
        )

    def test_freeze_is_idempotent_and_writes_immutable_receipt(self) -> None:
        job_root = self.root / "jobs" / self.job.job_id
        job_root.mkdir(parents=True)
        receipt = OldRunFreezeService(self.store).freeze(
            job_id=self.job.job_id,
            run_id="PRORUN-old",
            job_root=job_root,
        )
        frozen = self.store.get_job(self.job.job_id)
        self.assertEqual(frozen.old_job_frozen_at, "2026-08-25T04:30:00Z")
        self.assertIsNone(frozen.superseded_by_fresh_job_id)
        self.assertEqual(
            receipt["dispositions"],
            [
                "OLD_V2_REPAIR_HEAVY_DIAGNOSTIC_RUN",
                "SUPERSEDED_BY_FRESH_SESSION_EFFICIENCY_VALIDATION",
                "NOT_OPERATIONAL_EFFICIENCY_PROOF",
            ],
        )
        self.assertFalse(receipt["score_authority"])
        self.assertTrue(receipt["publication_withheld"])
        receipt_path = job_root / "fresh_session/old_run_freeze_receipt.json"
        self.assertEqual(json.loads(receipt_path.read_text()), receipt)

        repeated = OldRunFreezeService(self.store).freeze(
            job_id=self.job.job_id,
            run_id="PRORUN-old",
            job_root=job_root,
        )
        self.assertEqual(repeated, receipt)

    def test_frozen_job_blocks_initial_and_followup_planning(self) -> None:
        frozen = self.store.freeze_old_diagnostic_job(
            self.job.job_id,
            expected_version=self.job.state_version,
            actor="test",
            idempotency_key="freeze",
        )
        with self.assertRaisesRegex(OldDiagnosticRunFrozen, "frozen"):
            self.store.claim_submit(
                frozen.job_id,
                expected_version=frozen.state_version,
                actor="test",
                idempotency_key="forbidden-submit",
            )

        decision = ProMultiPassResearchOrchestrator(self.store).plan_followup(
            job_id=frozen.job_id,
            packet={},
            primary_archetype_ids=("C06_HBM_MEMORY_CUSTOMER_CAPACITY",),
            pass_name="VERIFIER_REPAIR",
        )
        self.assertIsInstance(decision, TransportPendingDecision)
        self.assertIn(
            "SUPERSEDED_BY_FRESH_SESSION_EFFICIENCY_VALIDATION",
            decision.reason,
        )

    def test_frozen_job_binds_only_distinct_same_target_fresh_successor(self) -> None:
        frozen = self.store.freeze_old_diagnostic_job(
            self.job.job_id,
            expected_version=self.job.state_version,
            actor="test",
            idempotency_key="freeze",
        )
        fresh = self._create_job("fresh")
        bound = self.store.bind_superseding_fresh_job(
            frozen.job_id,
            fresh.job_id,
            expected_version=frozen.state_version,
            actor="test",
            idempotency_key="bind-fresh",
        )
        self.assertEqual(bound.superseded_by_fresh_job_id, fresh.job_id)
        repeated = self.store.bind_superseding_fresh_job(
            frozen.job_id,
            fresh.job_id,
            expected_version=0,
            actor="test",
            idempotency_key="ignored-after-binding",
        )
        self.assertEqual(repeated.superseded_by_fresh_job_id, fresh.job_id)


if __name__ == "__main__":
    unittest.main()
