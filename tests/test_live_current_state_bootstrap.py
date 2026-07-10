from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.research_brain.runtime.live_materialization import (
    BootstrapCompleteness,
    CurrentStateBootstrapper,
    CurrentStateEvent,
    CurrentStateSourceAttempt,
    EventLifecycleStatus,
    LiveUniverseRow,
    SourceAttemptStatus,
    ThesisStatus,
    write_current_state_bootstrap,
)


def _universe_row(symbol: str, name: str) -> LiveUniverseRow:
    return LiveUniverseRow(
        symbol=symbol,
        company_name=name,
        market="KOSPI",
        security_group="주권",
        stock_certificate_type="보통주",
        sector_type="",
        listing_date="2020-01-01",
        listing_status="LISTED",
        source_effective_date="2026-07-10",
        source_url="https://data-dbg.krx.co.kr/svc/apis/sto/stk_isu_base_info",
        source_document_id=f"KRX-UNIVERSE-{symbol}",
        source_content_hash="a" * 64,
        source_request_id="KRX-REQUEST-20260710",
        source_mode="LIVE_OFFICIAL_API",
        eligible=True,
        exclusion_reason=None,
        raw_fields={},
    )


def _event(
    event_id: str,
    *,
    target_id: str = "005930",
    event_type: str = "SUPPLY_CONTRACT",
    effective_date: str = "2024-01-01",
    end_date: str | None = None,
    resolved_date: str | None = None,
) -> CurrentStateEvent:
    return CurrentStateEvent(
        event_id=event_id,
        target_id=target_id,
        event_type=event_type,
        effective_date=effective_date,
        lifecycle_status=EventLifecycleStatus.OPEN.value,
        source_ids=(f"SOURCE-{event_id}",),
        end_date=end_date,
        resolved_date=resolved_date,
        score_eligible=True,
    )


class LiveCurrentStateBootstrapTests(unittest.TestCase):
    def test_every_eligible_symbol_gets_timeline_thesis_and_source_attempts(self):
        universe = (
            _universe_row("005930", "삼성전자"),
            _universe_row("000660", "SK하이닉스"),
        )

        result = CurrentStateBootstrapper().bootstrap(
            as_of_date="2026-07-10",
            universe=universe,
        )

        self.assertEqual(len(result.records), 2)
        self.assertEqual(len(result.source_timelines), 2)
        self.assertEqual(len(result.last_effective_theses), 2)
        self.assertTrue(all(len(record.source_attempts) >= 2 for record in result.records))
        self.assertTrue(
            all(
                record.bootstrap_completeness
                == BootstrapCompleteness.PARTIAL_HISTORY_PENDING.value
                for record in result.records
            )
        )
        self.assertTrue(
            all(
                record.last_effective_thesis_status
                == ThesisStatus.PARTIAL_HISTORY_PENDING.value
                for record in result.records
            )
        )
        self.assertTrue(result.audit["hard_acceptance_pass"])

    def test_old_open_contract_is_preserved_until_its_real_end_date(self):
        result = CurrentStateBootstrapper().bootstrap(
            as_of_date="2026-07-10",
            universe=(_universe_row("005930", "삼성전자"),),
            discovered_events=(
                _event("OLD-ACTIVE-CONTRACT", end_date="2027-12-31"),
            ),
        )

        event = result.records[0].material_events[0]
        self.assertEqual(event.lifecycle_status, EventLifecycleStatus.OPEN.value)
        self.assertTrue(event.score_eligible)
        self.assertEqual(result.audit["old_active_contract_dropped_count"], 0)
        self.assertEqual(
            result.records[0].last_effective_thesis_status,
            ThesisStatus.ACTIVE_THESIS.value,
        )

    def test_expired_contract_and_resolved_risk_are_not_score_eligible(self):
        result = CurrentStateBootstrapper().bootstrap(
            as_of_date="2026-07-10",
            universe=(_universe_row("005930", "삼성전자"),),
            discovered_events=(
                _event("EXPIRED-CONTRACT", end_date="2025-12-31"),
                _event(
                    "RESOLVED-RISK",
                    event_type="RISK",
                    effective_date="2023-01-01",
                    resolved_date="2025-01-15",
                ),
            ),
            history_complete_target_ids=("005930",),
        )

        self.assertTrue(
            all(
                event.lifecycle_status == EventLifecycleStatus.RESOLVED.value
                and not event.score_eligible
                for event in result.records[0].material_events
            )
        )
        self.assertEqual(result.audit["old_resolved_risk_scored_count"], 0)
        self.assertEqual(
            result.records[0].last_effective_thesis_status,
            ThesisStatus.NO_CURRENT_THESIS.value,
        )

    def test_provider_failure_stays_pending_instead_of_becoming_no_thesis(self):
        failure = CurrentStateSourceAttempt(
            attempt_id="ATTEMPT-DART-005930",
            target_id="005930",
            provider_name="OpenDART",
            source_class="OFFICIAL",
            status=SourceAttemptStatus.PROVIDER_FAILED.value,
            observed_date="2026-07-10",
            provider_error_category="PROVIDER_NETWORK_FAILURE",
        )

        result = CurrentStateBootstrapper().bootstrap(
            as_of_date="2026-07-10",
            universe=(_universe_row("005930", "삼성전자"),),
            provider_attempts_by_target={"005930": (failure,)},
            history_complete_target_ids=("005930",),
        )

        record = result.records[0]
        self.assertEqual(
            record.bootstrap_completeness,
            BootstrapCompleteness.PROVIDER_PENDING.value,
        )
        self.assertEqual(record.last_effective_thesis_status, ThesisStatus.PROVIDER_PENDING.value)
        self.assertEqual(result.audit["provider_failure_mapped_no_thesis_count"], 0)

    def test_latest_regular_report_supersedes_the_previous_report(self):
        result = CurrentStateBootstrapper().bootstrap(
            as_of_date="2026-07-10",
            universe=(_universe_row("005930", "삼성전자"),),
            discovered_events=(
                _event(
                    "REPORT-2025",
                    event_type="REGULAR_REPORT",
                    effective_date="2025-03-01",
                ),
                _event(
                    "REPORT-2026",
                    event_type="REGULAR_REPORT",
                    effective_date="2026-03-01",
                ),
            ),
        )

        events = {event.event_id: event for event in result.records[0].material_events}
        self.assertEqual(
            events["REPORT-2025"].lifecycle_status,
            EventLifecycleStatus.SUPERSEDED.value,
        )
        self.assertEqual(events["REPORT-2025"].superseded_by_event_id, "REPORT-2026")
        self.assertFalse(events["REPORT-2025"].score_eligible)
        self.assertEqual(events["REPORT-2026"].lifecycle_status, EventLifecycleStatus.OPEN.value)

    def test_writer_emits_versioned_store_timeline_thesis_and_completeness(self):
        result = CurrentStateBootstrapper().bootstrap(
            as_of_date="2026-07-10",
            universe=(_universe_row("005930", "삼성전자"),),
        )

        with tempfile.TemporaryDirectory() as tmp:
            paths = write_current_state_bootstrap(result, output_root=tmp)
            self.assertEqual(
                {path.name for path in paths.values()},
                {
                    "current_state_store.jsonl",
                    "source_timelines.jsonl",
                    "last_effective_thesis.jsonl",
                    "bootstrap_completeness.json",
                },
            )
            self.assertTrue(all(Path(path).is_file() for path in paths.values()))
            completeness = json.loads(paths["completeness"].read_text(encoding="utf-8"))
            self.assertEqual(completeness["status"], "CURRENT_STATE_BOOTSTRAP_PASS")


if __name__ == "__main__":
    unittest.main()
