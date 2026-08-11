from __future__ import annotations

import hashlib
import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from e2r.cli.run_e2r_current_operation import main as current_main
from e2r.research_brain.runtime.live_materialization import (
    BaselineBulkSnapshot,
    CurrentBaselineMaterializer,
    CurrentKrxUniverseMaterializer,
    KrxBulkResponse,
    LiveCurrentMaterializationOrchestrator,
    LiveMaterializationPendingError,
)


REPO_ROOT = Path(__file__).resolve().parents[1]
AS_OF = "2026-08-09"
TRADING_DATE = "2026-08-07"


def _digest(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, ensure_ascii=False, sort_keys=True).encode("utf-8")
    ).hexdigest()


def _universe_row(symbol: str, name: str) -> dict[str, str]:
    return {
        "ISU_SRT_CD": symbol,
        "ISU_ABBRV": name,
        "KIND_STKCERT_TP_NM": "보통주",
        "SECUGRP_NM": "주권",
        "SECT_TP_NM": "",
        "LIST_DD": "20200101",
    }


class _UniverseTransport:
    def __init__(self) -> None:
        self.calls: list[tuple[str, str]] = []
        codes = [f"{value:06d}" for value in range(100000, 101002)]
        self.rows = {
            "KOSPI": tuple(
                _universe_row(symbol, f"회사{symbol}") for symbol in codes[:501]
            ),
            "KOSDAQ": tuple(
                _universe_row(symbol, f"회사{symbol}") for symbol in codes[501:]
            ),
        }

    def fetch_market(self, *, market, effective_date, credential, timeout_seconds):
        effective = effective_date.isoformat()
        self.calls.append((market, effective))
        rows = self.rows[market] if effective == TRADING_DATE else ()
        endpoint = "stk_isu_base_info" if market == "KOSPI" else "ksq_isu_base_info"
        return KrxBulkResponse(
            market=market,
            effective_date=effective,
            request_id=f"REQ-{market}-{effective}",
            canonical_url=f"https://data-dbg.krx.co.kr/svc/apis/sto/{endpoint}",
            provider_request_id=f"PROVIDER-{market}-{effective}",
            fetched_at="2026-08-09T00:00:00+00:00",
            content_hash=_digest(rows),
            rows=rows,
        )


def _price_row(symbol: str, *, triggered: bool) -> dict[str, str]:
    return {
        "BAS_DD": "20260807",
        "ISU_CD": symbol,
        "ISU_NM": symbol,
        "SECT_TP_NM": "",
        "TDD_CLSPRC": "10000",
        "CMPPREVDD_PRC": "1200" if triggered else "100",
        "FLUC_RT": "12.00" if triggered else "1.00",
        "ACC_TRDVOL": "100000",
        "ACC_TRDVAL": "2000000000",
        "MKTCAP": "100000000000",
    }


class _BaselineTransport:
    def __init__(self, universe: _UniverseTransport) -> None:
        self.universe = universe
        self.calls: list[tuple[str, str, str]] = []
        self.dart_budget: tuple[int, int] | None = None

    def fetch_krx_price(self, *, market, effective_date, credential, timeout_seconds):
        effective = effective_date.isoformat()
        self.calls.append(("KRX", market, effective))
        rows = tuple(
            _price_row(str(row["ISU_SRT_CD"]), triggered=index == 0 and market == "KOSPI")
            for index, row in enumerate(self.universe.rows[market])
        )
        endpoint = "stk_bydd_trd" if market == "KOSPI" else "ksq_bydd_trd"
        return BaselineBulkSnapshot(
            provider_name="KRX",
            source_class=f"PRICE_{market}",
            effective_date=effective,
            canonical_url=f"https://data-dbg.krx.co.kr/svc/apis/sto/{endpoint}",
            request_id=f"PRICE-{market}-{effective}",
            provider_request_id=f"PRICE-PROVIDER-{market}-{effective}",
            fetched_at="2026-08-09T00:00:00+00:00",
            content_hash=_digest(rows),
            rows=rows,
        )

    def fetch_opendart_index(
        self,
        *,
        start_date,
        end_date,
        credential,
        page_count,
        max_pages,
        timeout_seconds,
    ):
        self.calls.append(("OpenDART", start_date.isoformat(), end_date.isoformat()))
        self.dart_budget = (page_count, max_pages)
        return BaselineBulkSnapshot(
            provider_name="OpenDART",
            source_class="DISCLOSURE_INDEX",
            effective_date=end_date.isoformat(),
            canonical_url="https://opendart.fss.or.kr/api/list.json",
            request_id=f"DART-{start_date.isoformat()}-{end_date.isoformat()}",
            provider_request_id="DART-PROVIDER",
            fetched_at="2026-08-09T00:00:00+00:00",
            content_hash=_digest(()),
            rows=(),
        )


class LivePreDeepOrchestratorTests(unittest.TestCase):
    def _orchestrator(self, *, dart_credential: bool = True):
        universe_transport = _UniverseTransport()
        baseline_transport = _BaselineTransport(universe_transport)
        environment = {"KRX_OPENAPI_KEY": "fixture-krx-key"}
        if dart_credential:
            environment["OPENDART_API_KEY"] = "fixture-dart-key"
        orchestrator = LiveCurrentMaterializationOrchestrator(
            universe_materializer=CurrentKrxUniverseMaterializer(universe_transport),
            baseline_materializer=CurrentBaselineMaterializer(baseline_transport),
            environment=environment,
        )
        return orchestrator, universe_transport, baseline_transport

    def _materialize(self, orchestrator, root: Path):
        return orchestrator.materialize(
            as_of_date=AS_OF,
            live_root=root / "live" / AS_OF,
            current_state_root=root / "state" / AS_OF,
            run_profile=REPO_ROOT / "configs/e2r_production_daily_v1.json",
        )

    def test_missing_chain_materializes_full_pre_deep_then_reports_planner_pending(self):
        orchestrator, universe_transport, baseline_transport = self._orchestrator()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            with self.assertRaises(LiveMaterializationPendingError) as caught:
                self._materialize(orchestrator, root)
            live = root / "live" / AS_OF
            state = root / "state" / AS_OF
            audit = json.loads((live / "current_orchestration_audit.json").read_text())

            self.assertEqual(caught.exception.pending_stage_id, "research_brain")
            self.assertTrue(audit["materializer_called"])
            self.assertEqual(audit["stage_count"], 6)
            self.assertTrue(
                all(
                    row["execution_mode"]
                    == "MISSING_OR_INVALID_CHECKPOINT_MATERIALIZED"
                    for row in audit["stages"]
                )
            )
            self.assertTrue((live / "universe_eligible.jsonl").is_file())
            self.assertTrue((state / "current_state_store.jsonl").is_file())
            self.assertTrue((live / "baseline_lanes.jsonl").is_file())
            self.assertTrue((live / "trigger_signals.jsonl").is_file())
            self.assertTrue((live / "depth_decisions.jsonl").is_file())
            self.assertEqual(len(universe_transport.calls), 6)
            self.assertIn(("OpenDART", TRADING_DATE, AS_OF), baseline_transport.calls)
            self.assertEqual(baseline_transport.dart_budget, (100, 10))

    def test_resume_revalidates_and_reuses_all_pre_deep_checkpoints(self):
        orchestrator, universe_transport, baseline_transport = self._orchestrator()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for _ in range(2):
                with self.assertRaises(LiveMaterializationPendingError):
                    self._materialize(orchestrator, root)
            audit = json.loads(
                (root / "live" / AS_OF / "current_orchestration_audit.json").read_text()
            )

            self.assertEqual(len(universe_transport.calls), 6)
            self.assertEqual(len(baseline_transport.calls), 3)
            self.assertTrue(
                all(
                    row["execution_mode"] == "CHECKPOINT_RESUME_VALIDATED"
                    for row in audit["stages"]
                )
            )

    def test_invalid_baseline_checkpoint_is_regenerated_with_downstream_lineage(self):
        orchestrator, universe_transport, baseline_transport = self._orchestrator()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            with self.assertRaises(LiveMaterializationPendingError):
                self._materialize(orchestrator, root)
            live = root / "live" / AS_OF
            (live / "baseline_lane_audit.json").write_text("{broken", encoding="utf-8")
            with self.assertRaises(LiveMaterializationPendingError):
                self._materialize(orchestrator, root)
            audit = json.loads((live / "current_orchestration_audit.json").read_text())
            modes = {row["stage_id"]: row["execution_mode"] for row in audit["stages"]}

            self.assertEqual(len(universe_transport.calls), 6)
            self.assertEqual(len(baseline_transport.calls), 6)
            self.assertEqual(modes["current_universe"], "CHECKPOINT_RESUME_VALIDATED")
            self.assertEqual(
                modes["baseline_lanes"], "MISSING_OR_INVALID_CHECKPOINT_MATERIALIZED"
            )
            self.assertEqual(
                modes["depth_selection"], "MISSING_OR_INVALID_CHECKPOINT_MATERIALIZED"
            )

    def test_missing_opendart_credential_remains_explicit_provider_pending(self):
        orchestrator, _, baseline_transport = self._orchestrator(dart_credential=False)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            with self.assertRaises(LiveMaterializationPendingError) as caught:
                self._materialize(orchestrator, root)
            audit = json.loads(
                (root / "live" / AS_OF / "current_orchestration_audit.json").read_text()
            )

            self.assertIn("MISSING_CREDENTIAL", caught.exception.blocker_codes)
            self.assertIn("MISSING_CREDENTIAL", audit["blockers"])
            self.assertNotIn(
                "OpenDART", {provider for provider, _, _ in baseline_transport.calls}
            )
            self.assertTrue(audit["materializer_called"])
            self.assertFalse(audit["score_valid"])

    def test_cli_preserves_called_true_and_exact_pending_stage(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            orchestration_audit = root / "current_orchestration_audit.json"
            orchestration_audit.write_text("{}\n", encoding="utf-8")

            class _PendingOrchestrator:
                def materialize(self, **kwargs):
                    raise LiveMaterializationPendingError(
                        blocker_codes=("VALIDATED_DOWNSTREAM_CHECKPOINT_PENDING",),
                        pending_stage_id="research_brain",
                        audit_path=orchestration_audit,
                        detail="planner checkpoint has not been materialized",
                    )

            output_root = root / "command"
            with patch(
                "e2r.cli.run_e2r_current_operation.LiveCurrentMaterializationOrchestrator",
                _PendingOrchestrator,
            ), redirect_stdout(io.StringIO()):
                code = current_main(
                    [
                        "--as-of-date",
                        AS_OF,
                        "--output-root",
                        str(output_root),
                        "--materialize-live-input",
                        "true",
                        "--live-materialization-authorized",
                        "true",
                        "--run-profile",
                        str(REPO_ROOT / "configs/e2r_production_daily_v1.json"),
                    ]
                )
            pending = json.loads(
                (output_root / "live_materialization_internal_pending.json").read_text()
            )

            self.assertEqual(code, 2)
            self.assertTrue(pending["materializer_called"])
            self.assertEqual(
                pending["authorization"]["pending_stage_id"], "research_brain"
            )
            self.assertEqual(
                pending["blockers"], ["VALIDATED_DOWNSTREAM_CHECKPOINT_PENDING"]
            )


if __name__ == "__main__":
    unittest.main()
