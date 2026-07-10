from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from datetime import date
from pathlib import Path

from e2r.research_brain.runtime.live_materialization import (
    CurrentKrxUniverseMaterializer,
    KrxBulkResponse,
    UniverseMaterializerConfig,
    write_universe_materialization,
)


class _FixtureKrxTransport:
    def __init__(self, rows_by_date_market):
        self.rows_by_date_market = rows_by_date_market
        self.calls = []

    def fetch_market(self, *, market, effective_date, credential, timeout_seconds):
        self.calls.append((market, effective_date.isoformat()))
        rows = tuple(self.rows_by_date_market.get((effective_date.isoformat(), market), ()))
        payload = repr(rows).encode("utf-8")
        return KrxBulkResponse(
            market=market,
            effective_date=effective_date.isoformat(),
            request_id=f"REQ-{market}-{effective_date.isoformat()}",
            canonical_url=(
                "https://data-dbg.krx.co.kr/svc/apis/sto/"
                + ("stk_isu_base_info" if market == "KOSPI" else "ksq_isu_base_info")
            ),
            provider_request_id=f"PROVIDER-{market}-{effective_date.isoformat()}",
            fetched_at="2026-07-11T00:00:00+00:00",
            content_hash=hashlib.sha256(payload).hexdigest(),
            rows=rows,
        )


def _row(symbol, name, *, certificate="보통주", group="주권", sector=""):
    return {
        "ISU_SRT_CD": symbol,
        "ISU_ABBRV": name,
        "KIND_STKCERT_TP_NM": certificate,
        "SECUGRP_NM": group,
        "SECT_TP_NM": sector,
        "LIST_DD": "20200101",
    }


class LiveCurrentUniverseMaterializerTests(unittest.TestCase):
    def test_live_operational_audit_records_full_universe_hard_acceptance(self):
        audit = json.loads(
            (
                Path(__file__).resolve().parents[1]
                / "docs/operational/e2r_live_universe_audit.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(audit["status"], "CURRENT_UNIVERSE_MATERIALIZATION_PASS")
        self.assertGreater(audit["raw_universe_count"], 1000)
        self.assertGreater(audit["eligible_universe_count"], 1000)
        self.assertEqual(audit["missing_symbol_count"], 0)
        self.assertEqual(audit["missing_company_name_count"], 0)
        self.assertEqual(audit["duplicate_eligible_symbol_count"], 0)
        self.assertEqual(audit["fixture_symbol_count"], 0)
        self.assertEqual(audit["generic_portal_counted_as_universe_count"], 0)
        self.assertEqual(audit["future_universe_data_count"], 0)
        self.assertEqual(audit["critical_count_sum"], 0)
        self.assertTrue(audit["hard_acceptance_pass"])

    def test_bulk_snapshot_is_normalized_and_exclusion_reasons_are_explicit(self):
        rows = {
            ("2026-07-10", "KOSPI"): (
                _row("005930", "삼성전자"),
                _row("005935", "삼성전자우", certificate="구형우선주"),
                _row("330590", "롯데리츠", group="부동산투자회사"),
            ),
            ("2026-07-10", "KOSDAQ"): (
                _row("000660", "SK하이닉스"),
                _row("0015G0", "그린광학"),
                _row("123456", "테스트스팩", sector="SPAC(소속부없음)"),
            ),
        }
        transport = _FixtureKrxTransport(rows)
        result = CurrentKrxUniverseMaterializer(transport).materialize(
            UniverseMaterializerConfig(as_of_date="2026-07-10", test_mode=True),
            credential="fixture-key",
        )

        self.assertEqual(len(transport.calls), 2)
        self.assertEqual(
            {row.symbol for row in result.eligible_rows},
            {"005930", "000660", "0015G0"},
        )
        self.assertEqual(
            {row.exclusion_reason for row in result.excluded_rows},
            {"PREFERRED_OR_CLASS_SHARE", "REIT", "SPAC"},
        )
        self.assertEqual(result.audit["generic_portal_counted_as_universe_count"], 0)
        self.assertEqual(result.audit["future_universe_data_count"], 0)
        self.assertFalse(result.audit["hard_acceptance_pass"])
        self.assertEqual(result.audit["fixture_symbol_count"], 6)

    def test_empty_as_of_day_falls_back_only_to_prior_available_day(self):
        rows = {
            ("2026-07-09", "KOSPI"): (_row("005930", "삼성전자"),),
            ("2026-07-09", "KOSDAQ"): (_row("000660", "SK하이닉스"),),
        }
        transport = _FixtureKrxTransport(rows)
        result = CurrentKrxUniverseMaterializer(transport).materialize(
            UniverseMaterializerConfig(
                as_of_date="2026-07-10",
                max_trading_day_lookback=2,
                test_mode=True,
            ),
            credential="fixture-key",
        )

        self.assertEqual(result.source_effective_date, "2026-07-09")
        self.assertEqual(len(transport.calls), 4)
        self.assertTrue(all(row.source_effective_date <= "2026-07-10" for row in result.raw_rows))

    def test_missing_identity_and_duplicate_symbol_are_quarantined_from_eligible(self):
        rows = {
            ("2026-07-10", "KOSPI"): (
                _row("005930", "삼성전자"),
                _row("", "코드없음"),
            ),
            ("2026-07-10", "KOSDAQ"): (
                _row("005930", "중복삼성"),
                _row("000660", ""),
            ),
        }
        result = CurrentKrxUniverseMaterializer(_FixtureKrxTransport(rows)).materialize(
            UniverseMaterializerConfig(as_of_date="2026-07-10", test_mode=True),
            credential="fixture-key",
        )

        self.assertFalse(result.eligible_rows)
        self.assertEqual(len(result.excluded_rows), 4)
        self.assertEqual(
            [row.exclusion_reason for row in result.excluded_rows].count("DUPLICATE_SYMBOL"),
            2,
        )

    def test_same_snapshot_and_config_have_deterministic_normalized_rows(self):
        rows = {
            ("2026-07-10", "KOSPI"): (_row("005930", "삼성전자"),),
            ("2026-07-10", "KOSDAQ"): (_row("000660", "SK하이닉스"),),
        }
        config = UniverseMaterializerConfig(as_of_date="2026-07-10", test_mode=True)
        first = CurrentKrxUniverseMaterializer(_FixtureKrxTransport(rows)).materialize(
            config, credential="fixture-key"
        )
        second = CurrentKrxUniverseMaterializer(_FixtureKrxTransport(rows)).materialize(
            config, credential="fixture-key"
        )

        self.assertEqual(
            [row.to_dict() for row in first.raw_rows],
            [row.to_dict() for row in second.raw_rows],
        )

    def test_missing_credential_is_provider_pending_not_empty_success(self):
        result = CurrentKrxUniverseMaterializer(_FixtureKrxTransport({})).materialize(
            UniverseMaterializerConfig(as_of_date="2026-07-10", test_mode=True),
            credential=None,
            env_file=None,
        )
        self.assertEqual(result.status, "PROVIDER_PENDING")
        self.assertEqual(result.audit["hard_acceptance_pass"], False)
        self.assertIn("MISSING_CREDENTIAL:KRX_OPENAPI_KEY", result.blockers)

    def test_writer_emits_required_leaf_files(self):
        rows = {
            ("2026-07-10", "KOSPI"): (_row("005930", "삼성전자"),),
            ("2026-07-10", "KOSDAQ"): (_row("000660", "SK하이닉스"),),
        }
        result = CurrentKrxUniverseMaterializer(_FixtureKrxTransport(rows)).materialize(
            UniverseMaterializerConfig(as_of_date="2026-07-10", test_mode=True),
            credential="fixture-key",
        )
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_universe_materialization(result, output_root=tmp)
            self.assertEqual(
                {path.name for path in paths.values()},
                {
                    "universe_raw.jsonl",
                    "universe_eligible.jsonl",
                    "universe_excluded.jsonl",
                    "universe_provenance.json",
                    "universe_audit.json",
                },
            )
            self.assertTrue(all(Path(path).is_file() for path in paths.values()))


if __name__ == "__main__":
    unittest.main()
