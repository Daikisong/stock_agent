from __future__ import annotations

from datetime import date, datetime
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from zoneinfo import ZoneInfo

from e2r.cheap_scan.korea_scanner import KoreaCheapScanConfig, KoreaCheapScanResult
from e2r.cheap_scan.models import CheapScanCandidate, RecommendedNextLayer
from e2r.models import Market
from e2r.pro_first.candidate_selector import (
    CandidateObservation,
    ExistingDossierContext,
    ProCandidateSelector,
)
from e2r.pro_first.job_store import ProFirstJobStore
from e2r.pro_first.models import ResearchMode, ScanWindow
from e2r.pro_first.scheduler import KoreaScanToProQueue


KST = ZoneInfo("Asia/Seoul")


def _candidate(
    symbol: str,
    *,
    layer: RecommendedNextLayer = RecommendedNextLayer.DEEP_RESEARCH,
    production: bool = True,
    injected: bool = False,
    reasons: tuple[str, ...] = ("DISC_SUPPLY_CONTRACT",),
    evidence: tuple[str, ...] = ("EV-1",),
    score: float = 55.0,
) -> CheapScanCandidate:
    return CheapScanCandidate(
        symbol=symbol,
        company_name=f"기업-{symbol}",
        market=Market.KR,
        as_of_date=date(2026, 8, 22),
        reason_codes=reasons,
        disclosure_event_score=score,
        cheap_scan_total_score=score,
        evidence_ids=evidence,
        recommended_next_layer=layer,
        candidate_source_path="official_cheap_scan",
        test_injected=injected,
        production_candidate=production,
    )


class ProFirstCandidateSelectorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.selector = ProCandidateSelector(
            archetype_resolver=lambda candidate: (
                ("C06",) if "SUPPLY_CONTRACT" in " ".join(candidate.reason_codes) else ("C17",)
            )
        )

    @staticmethod
    def _result(*candidates: CheapScanCandidate) -> KoreaCheapScanResult:
        return KoreaCheapScanResult(
            as_of_date=date(2026, 8, 22),
            candidates=tuple(candidates),
            instruments_scanned=100,
        )

    def test_only_production_deep_candidates_selected(self) -> None:
        deep = _candidate("100001")
        none = _candidate("100002", layer=RecommendedNextLayer.NONE)
        nonproduction = _candidate("100003", production=False)
        batch = self.selector.select_result(
            self._result(deep, none, nonproduction),
            scan_window=ScanWindow.MORNING,
        )
        self.assertEqual([row.source_candidate.symbol for row in batch.selected], ["100001"])
        self.assertEqual(batch.rejection_counts["NOT_DEEP_RESEARCH"], 1)
        self.assertEqual(batch.rejection_counts["NOT_PRODUCTION_CANDIDATE"], 1)

    def test_test_injected_candidate_rejected(self) -> None:
        injected = _candidate("100004", production=False, injected=True)
        batch = self.selector.select_result(
            self._result(injected), scan_window=ScanWindow.MORNING
        )
        self.assertEqual(batch.selected, ())
        self.assertEqual(batch.rejection_counts, {"TEST_INJECTED": 1})

    def test_event_search_not_directly_promoted(self) -> None:
        event_search = _candidate("100005", layer=RecommendedNextLayer.EVENT_SEARCH)
        batch = self.selector.select_result(
            self._result(event_search), scan_window=ScanWindow.EVENING
        )
        self.assertEqual(batch.selected, ())
        self.assertEqual(
            batch.rejection_counts, {"EVENT_SEARCH_NOT_DIRECTLY_PROMOTED": 1}
        )

    def test_selection_does_not_see_final_score_stage(self) -> None:
        batch = self.selector.select_result(
            self._result(_candidate("100006")), scan_window=ScanWindow.MORNING
        )
        receipt = batch.selected[0].receipt.to_dict()
        self.assertFalse(receipt["final_score_visible_at_selection"])
        self.assertFalse(receipt["final_stage_visible_at_selection"])
        self.assertNotIn("full_e2r_score", receipt)
        self.assertNotIn("final_stage", receipt)
        self.assertEqual(receipt["cheap_scan_total_score"], 55.0)

    def test_morning_evening_trigger_merge(self) -> None:
        morning = _candidate(
            "100007",
            reasons=("DISC_SUPPLY_CONTRACT",),
            evidence=("EV-MORNING",),
        )
        evening = _candidate(
            "100007",
            reasons=("DISC_FACILITY_INVESTMENT",),
            evidence=("EV-EVENING",),
            score=60.0,
        )
        batch = self.selector.select_observations(
            (
                CandidateObservation(morning, ScanWindow.MORNING, "scan-morning"),
                CandidateObservation(evening, ScanWindow.EVENING, "scan-evening"),
            )
        )
        self.assertEqual(len(batch.selected), 1)
        selected = batch.selected[0]
        self.assertEqual(selected.scan_window, ScanWindow.EVENING)
        self.assertEqual(selected.scan_run_id, "scan-evening")
        self.assertEqual(len(selected.receipt.trigger_ids), 2)
        self.assertEqual(
            set(selected.receipt.reason_codes),
            {"DISC_SUPPLY_CONTRACT", "DISC_FACILITY_INVESTMENT"},
        )
        self.assertEqual(
            set(selected.source_candidate.evidence_ids), {"EV-MORNING", "EV-EVENING"}
        )
        reversed_batch = self.selector.select_observations(
            (
                CandidateObservation(evening, ScanWindow.EVENING, "scan-evening"),
                CandidateObservation(morning, ScanWindow.MORNING, "scan-morning"),
            )
        )
        self.assertEqual(
            reversed_batch.selected[0].trigger_fingerprint,
            selected.trigger_fingerprint,
        )

    def test_no_material_delta_creates_no_job_candidate(self) -> None:
        first = self.selector.select_result(
            self._result(_candidate("100008")), scan_window=ScanWindow.MORNING
        ).selected[0]
        context = ExistingDossierContext(
            dossier_id="DOSSIER-1",
            materially_stale=False,
            last_trigger_fingerprint=first.trigger_fingerprint,
        )
        batch = self.selector.select_result(
            self._result(_candidate("100008")),
            scan_window=ScanWindow.EVENING,
            existing_by_symbol={"100008": context},
        )
        self.assertEqual(batch.selected, ())
        self.assertEqual(batch.rejection_counts, {"NO_MATERIAL_DELTA": 1})

    def test_existing_dossier_routes_delta_without_copying_final_authority(self) -> None:
        batch = self.selector.select_result(
            self._result(_candidate("100009")),
            scan_window=ScanWindow.MORNING,
            existing_by_symbol={
                "100009": ExistingDossierContext(
                    dossier_id="DOSSIER-2",
                    current_source_delta_hash="new-delta",
                    last_source_delta_hash="old-delta",
                )
            },
        )
        self.assertEqual(batch.selected[0].research_mode, ResearchMode.DELTA_RESEARCH)
        self.assertEqual(batch.selected[0].receipt.existing_dossier_id, "DOSSIER-2")

    def test_existing_korea_scanner_result_enqueued_idempotently(self) -> None:
        class FakeExistingScanner:
            def run(self, config: KoreaCheapScanConfig) -> KoreaCheapScanResult:
                return ProFirstCandidateSelectorTest._result(_candidate("100010"))

        with TemporaryDirectory() as directory:
            now = lambda: datetime(2026, 8, 22, 5, 30, tzinfo=KST)
            store = ProFirstJobStore(Path(directory) / "queue.sqlite3", now=now)
            scan_run = store.claim_scan_run(
                as_of_date="2026-08-22",
                scan_window=ScanWindow.MORNING,
                scheduled_for="2026-08-22T05:30:00+09:00",
                catchup=False,
            )
            pipeline = KoreaScanToProQueue(
                store=store,
                scanner=FakeExistingScanner(),
                selector=self.selector,
                config_factory=lambda as_of, _window: KoreaCheapScanConfig(as_of_date=as_of),
            )
            receipt = pipeline.run_claimed_window(scan_run)
            self.assertEqual(receipt.pro_job_count, 1)
            self.assertEqual(receipt.scan_run.status, "COMPLETED")

            selected = self.selector.select_result(
                self._result(_candidate("100010")), scan_window=ScanWindow.MORNING
            )
            second = self.selector.enqueue(store, selected)
            self.assertEqual(len(second), 1)
            self.assertFalse(second[0].created)
            self.assertEqual(second[0].job.job_id, store.get_job_by_candidate(second[0].candidate.candidate_id).job_id)


if __name__ == "__main__":
    unittest.main()
