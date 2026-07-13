from __future__ import annotations

import json
import tempfile
import unittest
from dataclasses import replace
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any, Mapping

from e2r.models import (
    ConsensusRevision,
    ConsensusSnapshot,
    FinancialActual,
    PriceBar,
    ResearchReport,
)
from e2r.research_brain.researcher_mode import (
    CANONICAL_STRUCTURED_SOURCE_ROUTES,
    PHASE86_PASS,
    CanonicalResearchDossierBuilder,
    CompanyGuideStructuredRoute,
    ConsensusConnectorStructuredRoute,
    ForwardGuidanceObservation,
    InMemoryStructuredSourceRoute,
    IssuerGuidanceStructuredRoute,
    KRXPriceMarketCapStructuredRoute,
    OpenDARTActualsStructuredRoute,
    PeerStructuredValuationRoute,
    PeerValuationObservation,
    PublicBrokerReportStructuredRoute,
    SegmentFinancialObservation,
    StructuredFinancialConsensusValuationEngine,
    StructuredMetricRecord,
    StructuredSourcePayload,
    build_structured_source_routes,
    compile_phase86_structured_financial_engine_audit,
    write_structured_financial_outputs,
)


TARGET = "CURRENT_TARGET"
SYMBOL = "TARGET"
AS_OF = date(2026, 6, 29)


def actual(
    fiscal_year: int,
    *,
    quarter: int | None = None,
    reported_at: date | None = None,
    sales: float = 100.0,
    op: float = 20.0,
    net_income: float = 10.0,
    cfo: float = 18.0,
    capex: float = 7.0,
    fcf: float | None = None,
) -> FinancialActual:
    period_end = (
        date(fiscal_year, quarter * 3, 28)
        if quarter is not None
        else date(fiscal_year, 12, 31)
    )
    return FinancialActual(
        symbol=SYMBOL,
        fiscal_year=fiscal_year,
        fiscal_quarter=quarter,
        period_end=period_end,
        reported_at=datetime.combine(
            reported_at or date(fiscal_year + 1, 3, 15), datetime.min.time()
        ),
        as_of_date=AS_OF,
        source="OpenDART single account",
        sales=sales,
        operating_profit=op,
        net_income=net_income,
        cashflow_from_operations=cfo,
        capex=capex,
        fcf=fcf,
    )


def consensus(
    observed: date,
    *,
    fiscal_year: int = 2026,
    eps: float = 10.0,
    op: float = 30.0,
    fcf: float = 20.0,
    bps: float = 40.0,
    per: float = 10.0,
    pbr: float = 2.0,
    parsed_fields: Mapping[str, Any] | None = None,
) -> ConsensusSnapshot:
    return ConsensusSnapshot(
        symbol=SYMBOL,
        date=observed,
        fiscal_year=fiscal_year,
        as_of_date=AS_OF,
        source="CompanyGuide",
        op_e=op,
        eps_e=eps,
        fcf_e=fcf,
        bps_e=bps,
        per_e=per,
        pbr_e=pbr,
        parsed_fields={"ebitda_e": 35.0, **dict(parsed_fields or {})},
    )


def price_bars(*, release_date: date | None = None) -> tuple[PriceBar, ...]:
    start = (release_date or date(2026, 5, 1)) - timedelta(days=20)
    rows: list[PriceBar] = []
    for index in range(70):
        observed = start + timedelta(days=index)
        if observed > AS_OF:
            break
        target_close = 100.0 + index
        benchmark_close = 100.0 + index * 0.2
        rows.extend(
            (
                PriceBar(
                    symbol=SYMBOL,
                    date=observed,
                    open=target_close,
                    high=target_close + 1.0,
                    low=target_close - 1.0,
                    close=target_close,
                    adj_close=target_close,
                    volume=100,
                    trading_value=1_000.0,
                    market_cap=1_000.0 + index * 10,
                    source="KRX",
                    as_of_date=AS_OF,
                ),
                PriceBar(
                    symbol="BENCHMARK",
                    date=observed,
                    open=benchmark_close,
                    high=benchmark_close + 1.0,
                    low=benchmark_close - 1.0,
                    close=benchmark_close,
                    adj_close=benchmark_close,
                    volume=100,
                    trading_value=1_000.0,
                    market_cap=10_000.0,
                    source="KRX",
                    as_of_date=AS_OF,
                ),
            )
        )
    return tuple(rows)


def metric(
    metric_id: str,
    value: float,
    role: str,
    *,
    route: str = "ISSUER_GUIDANCE",
    dataset: str = "FINANCIAL",
    period: str = "FY2025",
    metadata: Mapping[str, Any] | None = None,
) -> StructuredMetricRecord:
    return StructuredMetricRecord(
        record_id=f"REC-{route}-{metric_id}-{period}",
        target_id=TARGET,
        as_of_date=AS_OF.isoformat(),
        metric_id=metric_id,
        value=value,
        unit="MULTIPLE" if "pe" in metric_id else "CURRENCY",
        period=period,
        evidence_roles=(role,),
        source_ids=(f"SRC-{route}",),
        source_route=route,
        observed_at="2026-06-20",
        record_kind="STRUCTURED_INPUT",
        confidence=0.9,
        dataset=dataset,
        provenance="STRUCTURED_EXTRACTED",
        metadata={"structured_source": True, **dict(metadata or {})},
    )


def route(name: str, **kwargs: Any) -> InMemoryStructuredSourceRoute:
    rows_present = any(bool(value) for value in kwargs.values())
    return InMemoryStructuredSourceRoute(
        name,
        StructuredSourcePayload(
            route_name=name,
            source_ids=(f"SRC-{name}",) if rows_present else (),
            **kwargs,
        ),
    )


class FakeFinancialConnector:
    def __init__(self, rows: tuple[FinancialActual, ...] = ()) -> None:
        self.rows = rows
        self.calls: list[tuple[str, date]] = []

    def get_financial_actuals(self, symbol: str, as_of_date: date):
        self.calls.append((symbol, as_of_date))
        return self.rows


class FakeConsensusConnector:
    def __init__(self, snapshots=(), revisions=()) -> None:
        self.snapshots = tuple(snapshots)
        self.revisions = tuple(revisions)
        self.calls: list[str] = []

    def get_consensus(self, symbol: str, as_of_date: date):
        self.calls.append("consensus")
        return self.snapshots

    def get_consensus_revisions(self, symbol: str, as_of_date: date):
        self.calls.append("revision")
        return self.revisions


class FakePriceConnector:
    def __init__(self, rows: tuple[PriceBar, ...]) -> None:
        self.rows = rows
        self.calls: list[str] = []

    def get_price_bars(self, symbol, start, end, as_of_date):
        self.calls.append(symbol)
        return tuple(row for row in self.rows if row.symbol == symbol)


class NeverCalledResearchProvider:
    provider_name = "NEVER_CALLED"

    def __init__(self) -> None:
        self.call_count = 0

    def complete(self, *, pass_name, payload):
        self.call_count += 1
        raise AssertionError("provider must not be called for mismatched structured input")


class E2RV5StructuredFinancialEngineTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]

    def test_phase86_audit_is_reproducible_and_passes(self) -> None:
        actual_audit = compile_phase86_structured_financial_engine_audit(self.ROOT)
        committed = json.loads(
            (
                self.ROOT
                / "docs/operational/e2r_v5_structured_financial_engine_audit.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(actual_audit, committed)
        self.assertEqual(actual_audit["status"], PHASE86_PASS)
        self.assertEqual(actual_audit["critical_count_sum"], 0)

    def test_fcf_is_derived_from_cfo_and_capex_without_direct_parser(self) -> None:
        result = self._run(
            route(
                "DART_ACTUALS_DETERMINISTIC_SCENARIO",
                financial_actuals=(actual(2025, cfo=30.0, capex=11.0, fcf=None),),
            )
        )
        fcf = next(row for row in result.records if row.metric_id == "free_cash_flow")
        self.assertEqual(fcf.value, 19.0)
        self.assertEqual(fcf.provenance, "DERIVED")
        self.assertEqual(len(fcf.input_record_ids), 2)
        self.assertEqual(result.fcf_component_zero_solely_due_missing_parser_count, 0)

    def test_fcf_is_also_derived_from_generic_structured_cashflow_rows(self) -> None:
        result = self._run(
            route(
                "ISSUER_GUIDANCE",
                structured_records=(
                    metric("operating_cash_flow", 50.0, "OPERATING_CASH_FLOW"),
                    metric("capex", 17.0, "CAPEX"),
                ),
            )
        )
        fcf = next(row for row in result.records if row.metric_id == "free_cash_flow")
        self.assertEqual(fcf.value, 33.0)
        self.assertTrue(fcf.metadata["derived_from_generic_structured_records"])
        self.assertEqual(result.fcf_component_zero_solely_due_missing_parser_count, 0)

    def test_provider_failure_continues_to_every_fallback_route(self) -> None:
        failed = InMemoryStructuredSourceRoute(
            "COMPANYGUIDE",
            StructuredSourcePayload(route_name="COMPANYGUIDE"),
            provider_error="provider down",
        )
        result = self._run(
            failed,
            route(
                "DART_ACTUALS_DETERMINISTIC_SCENARIO",
                financial_actuals=(actual(2025),),
            ),
            route("KRX_PRICE_MARKET_CAP", price_bars=price_bars()),
            deep=True,
        )
        attempts = {row.route_name: row for row in result.source_attempts}
        self.assertEqual(attempts["COMPANYGUIDE"].status, "PROVIDER_ERROR")
        self.assertEqual(attempts["KRX_PRICE_MARKET_CAP"].status, "FETCHED")
        self.assertIn("current_price", {row.metric_id for row in result.records})
        self.assertEqual(
            result.deep_researched_canary_valuation_route_not_attempted_count, 0
        )

    def test_connector_gap_is_pending_and_never_zero_component(self) -> None:
        result = self._run()
        self.assertEqual(result.status, "SOURCE_PENDING")
        self.assertTrue(result.missing_roles_by_component["market_mispricing"])
        self.assertNotIn("ZERO", result.component_disposition_by_component.values())
        self.assertEqual(
            result.component_disposition_by_component["market_mispricing"],
            "PROVIDER_SOURCE_PENDING",
        )
        self.assertEqual(
            result.revision_component_zero_solely_due_connector_gap_count, 0
        )

    def test_contract_alias_requires_its_compatible_structured_role(self) -> None:
        requirements = {
            "valuation_rerating": ("DURABLE_VISIBILITY",),
        }
        missing = StructuredFinancialConsensusValuationEngine().research(
            target_id=TARGET,
            symbol=SYMBOL,
            company_name="Current Target Corp",
            as_of_date=AS_OF,
            routes=(),
            required_roles_by_component=requirements,
        )
        self.assertEqual(
            missing.missing_roles_by_component["valuation_rerating"],
            ("DURABLE_VISIBILITY",),
        )

        covered = StructuredFinancialConsensusValuationEngine().research(
            target_id=TARGET,
            symbol=SYMBOL,
            company_name="Current Target Corp",
            as_of_date=AS_OF,
            routes=(
                route(
                    "ISSUER_GUIDANCE",
                    structured_records=(
                        metric(
                            "issuer_forward_guidance",
                            1.0,
                            "FORWARD_GUIDANCE",
                        ),
                    ),
                ),
            ),
            required_roles_by_component=requirements,
        )
        self.assertEqual(covered.status, "COMPLETE")
        self.assertEqual(
            covered.covered_roles_by_component["valuation_rerating"],
            ("DURABLE_VISIBILITY",),
        )
        self.assertIn(
            "DURABLE_VISIBILITY",
            covered.to_component_structured_metrics(requirements)[
                "valuation_rerating"
            ],
        )

    def test_structured_result_feeds_component_researcher_roles_without_points(self) -> None:
        result = self._run(
            route(
                "DART_ACTUALS_DETERMINISTIC_SCENARIO",
                financial_actuals=(actual(2025),),
            ),
            route(
                "COMPANYGUIDE",
                consensus_snapshots=(
                    consensus(date(2026, 1, 1), eps=10.0, op=30.0),
                    consensus(date(2026, 6, 1), eps=12.0, op=36.0),
                ),
            ),
            route("KRX_PRICE_MARKET_CAP", price_bars=price_bars()),
        )
        payloads = result.to_component_structured_metrics(
            {
                "eps_fcf_explosion": ("CASH_CONVERSION",),
                "market_mispricing": ("EARNINGS_REVISION",),
                "valuation_rerating": ("CURRENT_VALUATION",),
            }
        )
        self.assertIn("CASH_CONVERSION", payloads["eps_fcf_explosion"])
        self.assertIn("EARNINGS_REVISION", payloads["market_mispricing"])
        self.assertIn("CURRENT_VALUATION", payloads["valuation_rerating"])
        for component in payloads.values():
            self.assertTrue(
                all(not value["score_authority"] for value in component.values())
            )

    def test_dossier_rejects_mismatched_structured_result_before_llm_call(self) -> None:
        bad_result = replace(self._run(), target_id="OTHER_TARGET")
        provider = NeverCalledResearchProvider()
        builder = CanonicalResearchDossierBuilder(provider=provider)
        with self.assertRaisesRegex(ValueError, "target/as_of mismatch"):
            builder.build(
                target_id=TARGET,
                archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                as_of_date=AS_OF.isoformat(),
                evidence_facts=(),
                historical_anchors=(),
                source_claims=(),
                source_documents=(),
                source_coverage=(),
                structured_engine_result=bad_result,
            )
        self.assertEqual(provider.call_count, 0)

    def test_target_price_revision_is_not_earnings_revision(self) -> None:
        revision = ConsensusRevision(
            symbol=SYMBOL,
            date=date(2026, 6, 20),
            fiscal_year=2026,
            as_of_date=AS_OF,
            target_price_revision_1m=12.0,
            source="CompanyGuide",
        )
        result = self._run(
            route("COMPANYGUIDE", consensus_revisions=(revision,))
        )
        row = next(
            item
            for item in result.records
            if item.metric_id == "target_price_revision_1m_pct"
        )
        self.assertEqual(row.evidence_roles, ("TARGET_PRICE_ONLY",))
        self.assertTrue(row.metadata["target_price_only"])
        self.assertFalse(row.metadata["earnings_revision"])

    def test_consensus_history_derives_eps_and_op_revisions(self) -> None:
        result = self._run(
            route(
                "COMPANYGUIDE",
                consensus_snapshots=(
                    consensus(date(2026, 1, 1), eps=10.0, op=30.0),
                    consensus(date(2026, 6, 1), eps=12.0, op=36.0),
                ),
            )
        )
        rows = {row.metric_id: row for row in result.records}
        self.assertAlmostEqual(rows["eps_revision_history_pct"].value, 20.0)
        self.assertAlmostEqual(
            rows["operating_profit_revision_history_pct"].value, 20.0
        )
        self.assertIn(
            "CONSENSUS_HISTORY", rows["consensus_history_span_days"].evidence_roles
        )

    def test_earnings_surprise_uses_only_consensus_known_before_release(self) -> None:
        released = actual(
            2025,
            reported_at=date(2026, 3, 15),
            op=40.0,
            net_income=20.0,
        )
        result = self._run(
            route(
                "DART_ACTUALS_DETERMINISTIC_SCENARIO",
                financial_actuals=(released,),
            ),
            route(
                "COMPANYGUIDE",
                consensus_snapshots=(
                    consensus(
                        date(2026, 3, 1), fiscal_year=2025, op=32.0, eps=8.0
                    ),
                    consensus(
                        date(2026, 4, 1), fiscal_year=2025, op=100.0, eps=100.0
                    ),
                ),
            ),
        )
        op_surprise = next(
            row
            for row in result.records
            if row.metric_id == "operating_profit_earnings_surprise_pct"
        )
        self.assertAlmostEqual(op_surprise.value, 25.0)
        self.assertEqual(op_surprise.metadata["consensus_date"], "2026-03-01")

    def test_price_reaction_and_relative_performance_are_structured(self) -> None:
        release = date(2026, 5, 20)
        result = self._run(
            route(
                "DART_ACTUALS_DETERMINISTIC_SCENARIO",
                financial_actuals=(actual(2026, quarter=1, reported_at=release),),
            ),
            route("KRX_PRICE_MARKET_CAP", price_bars=price_bars(release_date=release)),
        )
        roles = {role for row in result.records for role in row.evidence_roles}
        self.assertIn("PRICE_REACTION", roles)
        self.assertIn("RELATIVE_PERFORMANCE", roles)
        relative = next(
            row
            for row in result.records
            if row.metric_id == "relative_performance_1m_pctp"
        )
        self.assertEqual(relative.provenance, "DERIVED")
        self.assertEqual(len(relative.input_record_ids), 4)

    def test_valuation_uses_price_forward_and_balance_sheet_records(self) -> None:
        records = (
            metric("cash_and_equivalents", 100.0, "BALANCE_SHEET_CASH"),
            metric("total_debt", 40.0, "BALANCE_SHEET_DEBT"),
        )
        result = self._run(
            route(
                "COMPANYGUIDE",
                consensus_snapshots=(
                    consensus(date(2026, 6, 20), eps=10.0, fcf=50.0, bps=50.0),
                ),
            ),
            route("ISSUER_GUIDANCE", structured_records=records),
            route("KRX_PRICE_MARKET_CAP", price_bars=price_bars()),
        )
        rows = {row.metric_id: row for row in result.records}
        self.assertIn("net_debt", rows)
        self.assertEqual(rows["net_debt"].value, -60.0)
        self.assertIn("forward_pe", rows)
        self.assertIn("forward_pb", rows)
        self.assertIn("forward_fcf_yield_pct", rows)
        self.assertEqual(rows["forward_pe"].dataset, "VALUATION")

    def test_historical_peer_and_scenario_sensitivity_are_derived(self) -> None:
        issuer = tuple(
            metric(
                "historical_forward_pe",
                value,
                "VALUATION_HISTORY",
                period=f"FY{year}",
            )
            for year, value in ((2022, 8.0), (2023, 10.0), (2024, 12.0))
        )
        peers = tuple(
            PeerValuationObservation(
                peer_id=f"P{index}",
                as_of_date=AS_OF.isoformat(),
                metric_id="forward_pe",
                value=value,
                unit="MULTIPLE",
                observed_at="2026-06-20",
                source_ids=(f"SRC-P{index}",),
                source_route="PEER_STRUCTURED",
            )
            for index, value in enumerate((9.0, 11.0, 13.0), start=1)
        )
        result = self._run(
            route(
                "DART_ACTUALS_DETERMINISTIC_SCENARIO",
                financial_actuals=(actual(2024), actual(2025, sales=130.0)),
            ),
            route(
                "COMPANYGUIDE",
                consensus_snapshots=(consensus(date(2026, 6, 20)),),
            ),
            route("ISSUER_GUIDANCE", structured_records=issuer),
            route("KRX_PRICE_MARKET_CAP", price_bars=price_bars()),
            route("PEER_STRUCTURED", peer_valuations=peers),
        )
        roles = {role for row in result.records for role in row.evidence_roles}
        self.assertIn("OWN_HISTORICAL_BAND", roles)
        self.assertIn("PEER_BAND", roles)
        self.assertIn("SCENARIO_SENSITIVITY", roles)
        scenarios = [
            row
            for row in result.records
            if row.provenance == "DETERMINISTIC_SCENARIO"
        ]
        self.assertTrue(scenarios)
        self.assertTrue(all(not row.metadata["observed_fact"] for row in scenarios))

    def test_quarterly_yoy_and_qoq_are_derived_from_matching_periods(self) -> None:
        result = self._run(
            route(
                "DART_ACTUALS_DETERMINISTIC_SCENARIO",
                financial_actuals=(
                    actual(
                        2025,
                        quarter=1,
                        reported_at=date(2025, 5, 15),
                        sales=100.0,
                    ),
                    actual(
                        2025,
                        quarter=4,
                        reported_at=date(2026, 3, 15),
                        sales=120.0,
                    ),
                    actual(
                        2026,
                        quarter=1,
                        reported_at=date(2026, 5, 15),
                        sales=150.0,
                    ),
                ),
            )
        )
        latest = {
            row.metric_id: row
            for row in result.records
            if row.period == "FY2026Q1"
        }
        self.assertAlmostEqual(latest["revenue_yoy_pct"].value, 50.0)
        self.assertAlmostEqual(latest["revenue_qoq_pct"].value, 25.0)
        self.assertIn("YOY_GROWTH", latest["revenue_yoy_pct"].evidence_roles)
        self.assertIn("QOQ_GROWTH", latest["revenue_qoq_pct"].evidence_roles)
        scenario_periods = {
            row.period
            for row in result.records
            if row.provenance == "DETERMINISTIC_SCENARIO"
        }
        self.assertEqual(scenario_periods, {"FY2026Q2E"})

    def test_fcf_yield_normalizes_explicit_consensus_currency_unit(self) -> None:
        snapshot = consensus(
            date(2026, 6, 20),
            fcf=1_000.0,
            parsed_fields={"financial_statement_unit": "KRW_100M"},
        )
        bar = PriceBar(
            symbol=SYMBOL,
            date=date(2026, 6, 20),
            open=100.0,
            high=101.0,
            low=99.0,
            close=100.0,
            adj_close=100.0,
            volume=100,
            trading_value=1_000.0,
            market_cap=1_000_000_000_000.0,
            source="KRX",
            as_of_date=AS_OF,
        )
        result = self._run(
            route("COMPANYGUIDE", consensus_snapshots=(snapshot,)),
            route("KRX_PRICE_MARKET_CAP", price_bars=(bar,)),
        )
        fcf_yield = next(
            row
            for row in result.records
            if row.metric_id == "forward_fcf_yield_pct"
        )
        self.assertAlmostEqual(fcf_yield.value, 10.0)
        forward_fcf = next(
            row for row in result.records if row.metric_id == "forward_fcf"
        )
        self.assertEqual(forward_fcf.unit, "KRW_100M")

    def test_generic_article_claim_cannot_be_valuation_record(self) -> None:
        with self.assertRaisesRegex(ValueError, "generic article"):
            metric(
                "forward_pe",
                10.0,
                "FORWARD_PE",
                route="PUBLIC_BROKER_REPORT",
                dataset="VALUATION",
                metadata={"generic_article_claim": True},
            )

    def test_future_structured_row_is_rejected_without_killing_valid_route(self) -> None:
        valid = metric("issuer_forward_revenue", 100.0, "FORWARD_GUIDANCE")
        future_payload = StructuredMetricRecord(
            record_id="FUTURE",
            target_id=TARGET,
            as_of_date="2026-07-01",
            metric_id="issuer_forward_revenue",
            value=200.0,
            unit="CURRENCY",
            period="FY2026E",
            evidence_roles=("FORWARD_GUIDANCE",),
            source_ids=("SRC-FUTURE",),
            source_route="ISSUER_GUIDANCE",
            observed_at="2026-07-01",
            record_kind="STRUCTURED_INPUT",
            confidence=0.9,
            dataset="FINANCIAL",
        )
        result = self._run(
            route(
                "ISSUER_GUIDANCE",
                structured_records=(valid, future_payload),
            )
        )
        self.assertIn(valid.record_id, {row.record_id for row in result.records})
        self.assertNotIn("FUTURE", {row.record_id for row in result.records})
        self.assertEqual(result.rejections[0].reason, "STRUCTURED_RECORD_AS_OF_MISMATCH")
        attempt = next(
            row for row in result.source_attempts if row.route_name == "ISSUER_GUIDANCE"
        )
        self.assertEqual(attempt.status, "PARTIAL")

    def test_outputs_are_split_into_exact_three_jsonl_files(self) -> None:
        result = self._run(
            route(
                "DART_ACTUALS_DETERMINISTIC_SCENARIO",
                financial_actuals=(actual(2025),),
            ),
            route(
                "COMPANYGUIDE",
                consensus_snapshots=(consensus(date(2026, 6, 20)),),
            ),
            route("KRX_PRICE_MARKET_CAP", price_bars=price_bars()),
        )
        with tempfile.TemporaryDirectory() as directory:
            paths = write_structured_financial_outputs(result, directory)
            self.assertEqual(
                {path.name for path in paths.values()},
                {
                    "structured_financial_records.jsonl",
                    "consensus_revision_records.jsonl",
                    "valuation_records.jsonl",
                },
            )
            for dataset, path in paths.items():
                rows = [
                    json.loads(line)
                    for line in path.read_text(encoding="utf-8").splitlines()
                    if line
                ]
                self.assertTrue(all(row["dataset"] == dataset for row in rows))

    def test_opendart_adapter_parses_single_account_and_derives_fcf(self) -> None:
        connector = FakeFinancialConnector()
        payload = {
            "list": [
                {"account_nm": "매출액", "sj_div": "IS", "thstrm_amount": "100"},
                {"account_nm": "영업이익", "sj_div": "IS", "thstrm_amount": "20"},
                {"account_nm": "당기순이익", "sj_div": "IS", "thstrm_amount": "10"},
                {"account_nm": "영업활동현금흐름", "sj_div": "CF", "thstrm_amount": "30"},
                {"account_nm": "유형자산의 취득", "sj_div": "CF", "thstrm_amount": "12"},
                {"account_nm": "현금및현금성자산", "sj_div": "BS", "fs_div": "CFS", "thstrm_amount": "100"},
                {"account_nm": "단기차입금", "sj_div": "BS", "fs_div": "CFS", "thstrm_amount": "40"},
                {"account_nm": "장기차입금", "sj_div": "BS", "fs_div": "CFS", "thstrm_amount": "20"},
            ]
        }
        adapter = OpenDARTActualsStructuredRoute(
            connector,
            single_account_payloads=(
                {
                    "payload": payload,
                    "fiscal_year": 2025,
                    "reported_at": "2026-03-15",
                    "period_end": "2025-12-31",
                },
            ),
        )
        result = self._run(adapter)
        fcf = next(row for row in result.records if row.metric_id == "free_cash_flow")
        self.assertEqual(fcf.value, 18.0)
        net_debt = next(row for row in result.records if row.metric_id == "net_debt")
        self.assertEqual(net_debt.value, -40.0)
        self.assertIn("NET_CASH_DEBT", net_debt.evidence_roles)
        self.assertEqual(connector.calls, [(SYMBOL, AS_OF)])

    def test_consensus_adapter_calls_history_and_revision_connectors(self) -> None:
        revision = ConsensusRevision(
            symbol=SYMBOL,
            date=date(2026, 6, 20),
            fiscal_year=2026,
            as_of_date=AS_OF,
            eps_revision_1m=5.0,
            source="CSV",
        )
        connector = FakeConsensusConnector(
            snapshots=(consensus(date(2026, 6, 20)),), revisions=(revision,)
        )
        result = self._run(ConsensusConnectorStructuredRoute(connector))
        self.assertEqual(connector.calls, ["consensus", "revision"])
        self.assertIn("eps_revision_1m_pct", {row.metric_id for row in result.records})

    def test_krx_adapter_collects_target_and_benchmark_history(self) -> None:
        connector = FakePriceConnector(price_bars())
        adapter = KRXPriceMarketCapStructuredRoute(
            connector, benchmark_symbols=("BENCHMARK",), lookback_days=90
        )
        result = self._run(adapter)
        self.assertEqual(connector.calls, [SYMBOL, "BENCHMARK"])
        self.assertIn("current_price", {row.metric_id for row in result.records})
        self.assertIn(
            "relative_performance_1m_pctp",
            {row.metric_id for row in result.records},
        )

    def test_companyguide_adapter_keeps_target_revision_separate(self) -> None:
        html = """
        <div>[기준 : 2026.06.20]</div>
        <table id="cTB15"><tr><td>4.0</td><td>150000</td><td>10000</td><td>12</td><td>20</td></tr></table>
        <table id="cTB24">
          <tr><td>제공처</td><td>일자</td><td>목표가</td><td>직전목표가</td><td>변동률</td><td>의견</td><td>직전의견</td></tr>
          <tr><td>Broker</td><td>26/06/20</td><td>150000</td><td>140000</td><td>7.14</td><td>Buy</td><td>Buy</td></tr>
        </table>
        """
        adapter = CompanyGuideStructuredRoute(
            snapshot_loader=lambda symbol, as_of: html
        )
        result = self._run(adapter)
        rows = {row.metric_id: row for row in result.records}
        self.assertIn("consensus_forward_eps", rows)
        self.assertEqual(
            rows["target_price_revision_1m_pct"].evidence_roles,
            ("TARGET_PRICE_ONLY",),
        )

    def test_public_broker_report_requires_full_or_structured_anchor(self) -> None:
        weak = ResearchReport(
            symbol=SYMBOL,
            publish_date=date(2026, 6, 20),
            broker="Broker",
            title="Target update",
            as_of_date=AS_OF,
            target_price=150.0,
        )
        adapter = PublicBrokerReportStructuredRoute(
            reports=(weak,), source_ids=("SRC-REPORT",)
        )
        result = self._run(adapter)
        self.assertFalse(result.records)
        self.assertEqual(
            result.rejections[0].reason,
            "BROKER_REPORT_WITHOUT_FULL_OR_STRUCTURED_ANCHOR",
        )

    def test_public_broker_target_only_does_not_invent_eps_revision(self) -> None:
        report = ResearchReport(
            symbol=SYMBOL,
            publish_date=date(2026, 6, 20),
            broker="Broker",
            title="Target update",
            as_of_date=AS_OF,
            target_price=150.0,
            target_revision_pct=10.0,
            fy1_eps=12.0,
            raw_text="Full public broker report with forward EPS table",
        )
        result = self._run(
            PublicBrokerReportStructuredRoute(
                reports=(report,), source_ids=("SRC-REPORT",)
            )
        )
        target_rows = [
            row for row in result.records if "target_price" in row.metric_id
        ]
        self.assertTrue(target_rows)
        self.assertTrue(
            all("EPS_REVISION" not in row.evidence_roles for row in target_rows)
        )
        self.assertFalse(
            any(row.metric_id == "broker_eps_revision_pct" for row in result.records)
        )

    def test_issuer_and_peer_routes_preserve_structured_lineage(self) -> None:
        guidance = metric(
            "issuer_forward_revenue", 150.0, "FORWARD_GUIDANCE"
        )
        issuer = IssuerGuidanceStructuredRoute(
            records=(guidance,), source_ids=("SRC-ISSUER_GUIDANCE",)
        )
        peer = PeerValuationObservation(
            peer_id="PEER",
            as_of_date=AS_OF.isoformat(),
            metric_id="forward_pe",
            value=10.0,
            unit="MULTIPLE",
            observed_at="2026-06-20",
            source_ids=("SRC-PEER",),
            source_route="PEER_STRUCTURED",
        )
        peer_route = PeerStructuredValuationRoute(
            observations=(peer,), source_ids=("SRC-PEER",)
        )
        result = self._run(issuer, peer_route)
        self.assertIn(guidance.record_id, {row.record_id for row in result.records})
        peer_row = next(
            row for row in result.records if row.metric_id == "peer_forward_pe"
        )
        self.assertEqual(peer_row.metadata["peer_id"], "PEER")

    def test_segment_contribution_and_issuer_guidance_have_canonical_records(self) -> None:
        segment = SegmentFinancialObservation(
            target_id=TARGET,
            as_of_date=AS_OF.isoformat(),
            segment_id="CORE",
            metric_id="revenue",
            value=60.0,
            total_company_value=150.0,
            unit="CURRENCY",
            period="FY2025",
            observed_at="2026-03-15",
            available_at="2026-03-15",
            source_ids=("SRC-ISSUER",),
            source_route="ISSUER_GUIDANCE",
        )
        guidance = ForwardGuidanceObservation(
            target_id=TARGET,
            as_of_date=AS_OF.isoformat(),
            metric_id="revenue",
            unit="CURRENCY",
            period="FY2026E",
            observed_at="2026-06-20",
            available_at="2026-06-20",
            source_ids=("SRC-ISSUER",),
            source_route="ISSUER_GUIDANCE",
            low_value=170.0,
            high_value=190.0,
        )
        result = self._run(
            IssuerGuidanceStructuredRoute(
                source_ids=("SRC-ISSUER",),
                segment_observations=(segment,),
                guidance_observations=(guidance,),
            )
        )
        rows = {row.metric_id: row for row in result.records}
        contribution = rows["segment_CORE_revenue_contribution_pct"]
        self.assertAlmostEqual(contribution.value, 40.0)
        self.assertEqual(contribution.provenance, "DERIVED")
        self.assertTrue(
            set(contribution.input_record_ids).issubset(
                {row.record_id for row in result.records}
            )
        )
        midpoint = rows["issuer_guidance_revenue_midpoint"]
        self.assertEqual(midpoint.value, 180.0)
        self.assertEqual(midpoint.provenance, "DERIVED")
        self.assertIn("FORWARD_GUIDANCE", midpoint.evidence_roles)

    def test_withdrawn_guidance_is_counter_state_not_forward_coverage(self) -> None:
        withdrawn = ForwardGuidanceObservation(
            target_id=TARGET,
            as_of_date=AS_OF.isoformat(),
            metric_id="revenue",
            unit="CURRENCY",
            period="FY2026E",
            observed_at="2026-06-20",
            available_at="2026-06-20",
            source_ids=("SRC-ISSUER",),
            source_route="ISSUER_GUIDANCE",
            midpoint_value=150.0,
            guidance_status="WITHDRAWN_GUIDANCE",
        )
        result = self._run(
            IssuerGuidanceStructuredRoute(
                source_ids=("SRC-ISSUER",),
                guidance_observations=(withdrawn,),
            )
        )
        row = next(
            item
            for item in result.records
            if item.metric_id == "issuer_guidance_revenue_midpoint"
        )
        self.assertEqual(row.evidence_roles, ("GUIDANCE_WITHDRAWN",))
        self.assertIn(
            "FORWARD_GUIDANCE",
            result.missing_roles_by_component["eps_fcf_explosion"],
        )

    def test_issuer_eps_guidance_can_feed_structured_forward_valuation(self) -> None:
        eps_guidance = ForwardGuidanceObservation(
            target_id=TARGET,
            as_of_date=AS_OF.isoformat(),
            metric_id="eps",
            unit="KRW_PER_SHARE",
            period="FY2026E",
            observed_at="2026-06-20",
            available_at="2026-06-20",
            source_ids=("SRC-ISSUER",),
            source_route="ISSUER_GUIDANCE",
            midpoint_value=20.0,
        )
        result = self._run(
            IssuerGuidanceStructuredRoute(
                source_ids=("SRC-ISSUER",),
                guidance_observations=(eps_guidance,),
            ),
            route("KRX_PRICE_MARKET_CAP", price_bars=price_bars()),
        )
        rows = {row.metric_id: row for row in result.records}
        self.assertEqual(rows["forward_eps"].value, 20.0)
        self.assertEqual(rows["forward_eps"].unit, "KRW_PER_SHARE")
        self.assertIn("forward_pe", rows)

    def test_default_route_builder_keeps_all_canonical_fallback_attempts(self) -> None:
        routes = build_structured_source_routes()
        self.assertEqual(
            tuple(route.route_name for route in routes),
            CANONICAL_STRUCTURED_SOURCE_ROUTES,
        )
        result = self._run(*routes, deep=True)
        self.assertEqual(
            tuple(row.route_name for row in result.source_attempts),
            CANONICAL_STRUCTURED_SOURCE_ROUTES,
        )
        self.assertTrue(
            all(row.status == "PROVIDER_ERROR" for row in result.source_attempts)
        )
        self.assertEqual(
            result.deep_researched_canary_valuation_route_not_attempted_count, 0
        )

    def test_legacy_structured_metric_constructor_remains_compatible(self) -> None:
        row = StructuredMetricRecord(
            record_id="LEGACY",
            target_id=TARGET,
            as_of_date=AS_OF.isoformat(),
            metric_id="cash_conversion",
            value=1.0,
            unit="RATIO",
            period="FY2025",
            evidence_roles=("CASH_CONVERSION",),
            source_ids=("SRC",),
            source_route="DART",
            observed_at="2026-03-15",
            record_kind="LEGACY_STRUCTURED",
            confidence=0.8,
        )
        self.assertEqual(row.dataset, "GENERIC")
        self.assertFalse(row.score_authority)
        self.assertEqual(row.available_at, row.observed_at)

    def _run(self, *routes, deep: bool = False):
        return StructuredFinancialConsensusValuationEngine().research(
            target_id=TARGET,
            symbol=SYMBOL,
            company_name="Current Target Corp",
            as_of_date=AS_OF,
            routes=routes,
            deep_researched_canary=deep,
        )


if __name__ == "__main__":
    unittest.main()
