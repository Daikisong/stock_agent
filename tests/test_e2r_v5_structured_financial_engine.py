from __future__ import annotations

import hashlib
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
from e2r.research_brain.researcher_mode import (
    structured_financial_engine as structured_engine_module,
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

        directly_covered = StructuredFinancialConsensusValuationEngine().research(
            target_id=TARGET,
            symbol=SYMBOL,
            company_name="Current Target Corp",
            as_of_date=AS_OF,
            routes=(
                route(
                    "ISSUER_GUIDANCE",
                    structured_records=(
                        metric(
                            "issuer_durable_visibility",
                            "full customer demand for FY2027 production",
                            "DURABLE_VISIBILITY",
                        ),
                    ),
                ),
            ),
            required_roles_by_component=requirements,
        )
        self.assertEqual(directly_covered.status, "COMPLETE")
        self.assertEqual(
            directly_covered.covered_roles_by_component["valuation_rerating"],
            ("DURABLE_VISIBILITY",),
        )

    def test_issuer_seed_cannot_bypass_broker_valuation_contract(self) -> None:
        forged = StructuredMetricRecord(
            record_id="REC-FORGED-ISSUER-PB",
            target_id=TARGET,
            as_of_date=AS_OF.isoformat(),
            metric_id="broker_forward_pb",
            value=3.1,
            unit="KRW",
            period="historical 2024",
            evidence_roles=("FORWARD_PB",),
            source_ids=("SRC-FORGED",),
            source_route="ISSUER_GUIDANCE",
            observed_at="2026-06-20",
            record_kind="STRUCTURED_INPUT",
            confidence=0.9,
            dataset="VALUATION",
            provenance="STRUCTURED_EXTRACTED",
            metadata={"structured_source": True},
        )
        result = StructuredFinancialConsensusValuationEngine().research(
            target_id=TARGET,
            symbol=SYMBOL,
            company_name="Current Target Corp",
            as_of_date=AS_OF,
            routes=(route("ISSUER_GUIDANCE", structured_records=(forged,)),),
            required_roles_by_component={
                "valuation_rerating": ("FORWARD_PB",)
            },
        )

        self.assertEqual(result.status, "SOURCE_PENDING")
        self.assertEqual(
            result.missing_roles_by_component["valuation_rerating"],
            ("FORWARD_PB",),
        )
        self.assertEqual(
            [row.reason for row in result.rejections],
            ["BROKER_VALUATION_METRIC_REQUIRES_PUBLIC_BROKER_ROUTE"],
        )

        forged_public = replace(
            forged,
            record_id="REC-FORGED-PUBLIC-BROKER-PB",
            source_route="PUBLIC_BROKER_REPORT",
            record_kind="SOURCE_BACKED_BROKER_VALUATION",
            unit="MULTIPLE",
            period="FY2026E",
            metadata={
                "structured_source": True,
                "source_family": "PUBLIC_BROKER_PDF",
                "exact_quote_verified": True,
            },
        )
        public_result = StructuredFinancialConsensusValuationEngine().research(
            target_id=TARGET,
            symbol=SYMBOL,
            company_name="Current Target Corp",
            as_of_date=AS_OF,
            routes=(
                route(
                    "PUBLIC_BROKER_REPORT",
                    structured_records=(forged_public,),
                ),
            ),
            required_roles_by_component={
                "valuation_rerating": ("FORWARD_PB",)
            },
        )
        self.assertEqual(public_result.status, "SOURCE_PENDING")
        self.assertEqual(
            [row.reason for row in public_result.rejections],
            ["BROKER_VALUATION_VERIFIED_INGRESS_REQUIRED"],
        )

    def test_self_attested_broker_seed_requires_canonical_fact_graph(self) -> None:
        quote = "The broker estimates 2026E PBR at 99x."
        forged = StructuredMetricRecord(
            record_id="REC-SELF-ATTESTED-PUBLIC-BROKER-PB",
            target_id=TARGET,
            as_of_date=AS_OF.isoformat(),
            metric_id="broker_forward_pb",
            value=99.0,
            unit="MULTIPLE",
            period="FY2026E",
            evidence_roles=("FORWARD_PB",),
            source_ids=("DOC-FORGED",),
            source_route="PUBLIC_BROKER_REPORT",
            observed_at="2026-06-20",
            available_at="2026-06-20",
            record_kind="SOURCE_BACKED_BROKER_VALUATION",
            confidence=0.9,
            dataset="VALUATION",
            provenance="STRUCTURED_EXTRACTED",
            metadata={
                "structured_source": True,
                "source_family": "PUBLIC_BROKER_PDF",
                "exact_quote_verified": True,
                "fact_boundary_validation_version": (
                    "e2r_broker_valuation_fact_boundary_v1"
                ),
                "fact_id": "FACT-FORGED",
                "claim_id": "CLAIM-FORGED",
                "document_id": "DOC-FORGED",
                "exact_quote": quote,
                "exact_quote_hash": hashlib.sha256(
                    quote.encode("utf-8")
                ).hexdigest(),
                "document_content_hash": "0" * 64,
            },
        )

        result = StructuredFinancialConsensusValuationEngine().research(
            target_id=TARGET,
            symbol=SYMBOL,
            company_name="Current Target Corp",
            as_of_date=AS_OF,
            routes=(
                route(
                    "PUBLIC_BROKER_REPORT",
                    structured_records=(forged,),
                ),
            ),
            required_roles_by_component={
                "valuation_rerating": ("FORWARD_PB",)
            },
        )

        self.assertEqual(result.status, "SOURCE_PENDING")
        self.assertEqual(
            [row.reason for row in result.rejections],
            ["BROKER_VALUATION_VERIFIED_INGRESS_REQUIRED"],
        )

    def test_public_broker_metric_alias_cannot_recreate_role_without_seal(
        self,
    ) -> None:
        alias_seed = StructuredMetricRecord(
            record_id="REC-UNSEALED-BROKER-BOOK-VALUE-ALIAS",
            target_id=TARGET,
            as_of_date=AS_OF.isoformat(),
            metric_id="broker_forward_book_value",
            value=1.0,
            unit="KRW_PER_SHARE",
            period="FY2026E",
            evidence_roles=("UNRELATED_INPUT",),
            source_ids=("DOC-UNSEALED",),
            source_route="PUBLIC_BROKER_REPORT",
            observed_at="2026-06-20",
            available_at="2026-06-20",
            record_kind="GENERIC_STRUCTURED_INPUT",
            confidence=0.9,
            dataset="VALUATION",
            provenance="STRUCTURED_EXTRACTED",
            metadata={"structured_source": True},
        )
        result = StructuredFinancialConsensusValuationEngine().research(
            target_id=TARGET,
            symbol=SYMBOL,
            company_name="Current Target Corp",
            as_of_date=AS_OF,
            routes=(
                route(
                    "PUBLIC_BROKER_REPORT",
                    structured_records=(alias_seed,),
                ),
            ),
            required_roles_by_component={
                "valuation_rerating": ("FORWARD_BOOK_VALUE",)
            },
        )
        self.assertEqual(result.status, "SOURCE_PENDING")
        self.assertEqual(
            [row.reason for row in result.rejections],
            ["BROKER_VALUATION_METRIC_REQUIRES_VERIFIED_RECORD_KIND"],
        )
        self.assertFalse(
            any(
                "FORWARD_BOOK_VALUE" in row.evidence_roles
                for row in result.records
            )
        )

    def test_broker_metric_alias_cannot_masquerade_as_another_route(self) -> None:
        for source_route in ("ISSUER_GUIDANCE", "UNTRUSTED_ALIAS_ROUTE"):
            with self.subTest(source_route=source_route):
                alias_seed = StructuredMetricRecord(
                    record_id=f"REC-{source_route}-BROKER-BOOK-VALUE-ALIAS",
                    target_id=TARGET,
                    as_of_date=AS_OF.isoformat(),
                    metric_id="broker_forward_book_value",
                    value=1.0,
                    unit="KRW_PER_SHARE",
                    period="FY2026E",
                    evidence_roles=("UNRELATED_INPUT",),
                    source_ids=(f"DOC-{source_route}",),
                    source_route=source_route,
                    observed_at="2026-06-20",
                    available_at="2026-06-20",
                    record_kind="GENERIC_STRUCTURED_INPUT",
                    confidence=0.9,
                    dataset="GENERIC",
                    provenance="STRUCTURED_EXTRACTED",
                    metadata={"structured_source": True},
                )
                result = StructuredFinancialConsensusValuationEngine().research(
                    target_id=TARGET,
                    symbol=SYMBOL,
                    company_name="Current Target Corp",
                    as_of_date=AS_OF,
                    routes=(
                        route(
                            source_route,
                            structured_records=(alias_seed,),
                        ),
                    ),
                    required_roles_by_component={
                        "valuation_rerating": ("FORWARD_BOOK_VALUE",)
                    },
                )
                self.assertEqual(result.status, "SOURCE_PENDING")
                self.assertEqual(
                    [row.reason for row in result.rejections],
                    ["BROKER_VALUATION_METRIC_REQUIRES_PUBLIC_BROKER_ROUTE"],
                )

        generic_alias = replace(
            alias_seed,
            record_id="REC-GENERIC-FORWARD-BOOK-VALUE-ALIAS",
            metric_id="forward_book_value",
        )
        generic_result = StructuredFinancialConsensusValuationEngine().research(
            target_id=TARGET,
            symbol=SYMBOL,
            company_name="Current Target Corp",
            as_of_date=AS_OF,
            routes=(
                route(
                    "UNTRUSTED_ALIAS_ROUTE",
                    structured_records=(generic_alias,),
                ),
            ),
            required_roles_by_component={
                "valuation_rerating": ("FORWARD_BOOK_VALUE",)
            },
        )
        self.assertEqual(generic_result.status, "SOURCE_PENDING")
        self.assertFalse(
            any(
                "FORWARD_BOOK_VALUE" in row.evidence_roles
                for row in generic_result.records
            )
        )

    def test_issuer_guidance_alias_requires_typed_observation(self) -> None:
        for record_kind, expected_rejections in (
            ("GENERIC_STRUCTURED_INPUT", ()),
            (
                "ISSUER_FORWARD_GUIDANCE",
                ("ISSUER_FORWARD_GUIDANCE_REQUIRES_TYPED_OBSERVATION",),
            ),
        ):
            with self.subTest(record_kind=record_kind):
                alias_seed = StructuredMetricRecord(
                    record_id=f"REC-{record_kind}-ISSUER-BOOK-VALUE",
                    target_id=TARGET,
                    as_of_date=AS_OF.isoformat(),
                    metric_id="issuer_guidance_book_value_midpoint",
                    value=1.0,
                    unit="KRW_PER_SHARE",
                    period="FY2026E",
                    evidence_roles=("FORWARD_GUIDANCE",),
                    source_ids=("DOC-SELF-ATTESTED-ISSUER",),
                    source_route="ISSUER_GUIDANCE",
                    observed_at="2026-06-20",
                    available_at="2026-06-20",
                    record_kind=record_kind,
                    confidence=0.9,
                    dataset="GENERIC",
                    provenance="STRUCTURED_EXTRACTED",
                    metadata={"structured_source": True},
                )
                result = StructuredFinancialConsensusValuationEngine().research(
                    target_id=TARGET,
                    symbol=SYMBOL,
                    company_name="Current Target Corp",
                    as_of_date=AS_OF,
                    routes=(
                        route(
                            "ISSUER_GUIDANCE",
                            structured_records=(alias_seed,),
                        ),
                    ),
                    required_roles_by_component={
                        "valuation_rerating": ("FORWARD_BOOK_VALUE",)
                    },
                )
                self.assertEqual(result.status, "SOURCE_PENDING")
                self.assertEqual(
                    tuple(row.reason for row in result.rejections),
                    expected_rejections,
                )
                self.assertFalse(
                    any(
                        "FORWARD_BOOK_VALUE" in row.evidence_roles
                        for row in result.records
                    )
                )

    def test_broker_fact_ingress_is_bound_to_roster_and_scope(self) -> None:
        quote = "The broker estimates 2026E PBR at 3.1x."
        valid = StructuredMetricRecord(
            record_id="REC-SEALED-PUBLIC-BROKER-PB",
            target_id=TARGET,
            as_of_date=AS_OF.isoformat(),
            metric_id="broker_forward_pb",
            value=3.1,
            unit="MULTIPLE",
            period="FY2026E",
            evidence_roles=("FORWARD_PB",),
            source_ids=("DOC-SEALED",),
            source_route="PUBLIC_BROKER_REPORT",
            observed_at="2026-06-20",
            available_at="2026-06-20",
            record_kind="SOURCE_BACKED_BROKER_VALUATION",
            confidence=0.9,
            dataset="VALUATION",
            provenance="STRUCTURED_EXTRACTED",
            metadata={
                "structured_source": True,
                "source_family": "PUBLIC_BROKER_PDF",
                "exact_quote_verified": True,
                "fact_boundary_validation_version": (
                    "e2r_broker_valuation_fact_boundary_v1"
                ),
                "fact_id": "FACT-SEALED",
                "claim_id": "CLAIM-SEALED",
                "document_id": "DOC-SEALED",
                "exact_quote": quote,
                "exact_quote_hash": hashlib.sha256(
                    quote.encode("utf-8")
                ).hexdigest(),
                "document_content_hash": "1" * 64,
            },
        )
        ingress = structured_engine_module._issue_verified_broker_fact_ingress(
            target_id=TARGET,
            as_of_date=AS_OF.isoformat(),
            route_name="PUBLIC_BROKER_REPORT",
            records=(valid,),
        )

        tampered = replace(valid, value=99.0)
        tampered_result = StructuredFinancialConsensusValuationEngine().research(
            target_id=TARGET,
            symbol=SYMBOL,
            company_name="Current Target Corp",
            as_of_date=AS_OF,
            routes=(
                route(
                    "PUBLIC_BROKER_REPORT",
                    structured_records=(tampered,),
                    verified_seed_ingress=ingress,
                ),
            ),
            required_roles_by_component={
                "valuation_rerating": ("FORWARD_PB",)
            },
        )
        self.assertEqual(
            [row.reason for row in tampered_result.rejections],
            ["BROKER_VALUATION_VERIFIED_INGRESS_ROSTER_MISMATCH"],
        )
        for changed in (
            replace(valid, period="FY2027E"),
            replace(
                valid,
                metric_id="broker_forward_ev_ebitda",
                evidence_roles=("FORWARD_EV_EBITDA",),
            ),
        ):
            with self.subTest(changed=changed.record_id + changed.period):
                changed_result = (
                    StructuredFinancialConsensusValuationEngine().research(
                        target_id=TARGET,
                        symbol=SYMBOL,
                        company_name="Current Target Corp",
                        as_of_date=AS_OF,
                        routes=(
                            route(
                                "PUBLIC_BROKER_REPORT",
                                structured_records=(changed,),
                                verified_seed_ingress=ingress,
                            ),
                        ),
                        required_roles_by_component={
                            "valuation_rerating": ("FORWARD_PB",)
                        },
                    )
                )
                self.assertEqual(
                    [row.reason for row in changed_result.rejections],
                    ["BROKER_VALUATION_VERIFIED_INGRESS_ROSTER_MISMATCH"],
                )

        extra = replace(valid, record_id="REC-SEALED-EXTRA")
        expanded_result = StructuredFinancialConsensusValuationEngine().research(
            target_id=TARGET,
            symbol=SYMBOL,
            company_name="Current Target Corp",
            as_of_date=AS_OF,
            routes=(
                route(
                    "PUBLIC_BROKER_REPORT",
                    structured_records=(valid, extra),
                    verified_seed_ingress=ingress,
                ),
            ),
            required_roles_by_component={
                "valuation_rerating": ("FORWARD_PB",)
            },
        )
        self.assertEqual(
            [row.reason for row in expanded_result.rejections],
            [
                "BROKER_VALUATION_VERIFIED_INGRESS_ROSTER_MISMATCH",
                "BROKER_VALUATION_VERIFIED_INGRESS_ROSTER_MISMATCH",
            ],
        )

        other_target = replace(valid, target_id="OTHER_TARGET")
        scoped_result = StructuredFinancialConsensusValuationEngine().research(
            target_id="OTHER_TARGET",
            symbol="OTHER",
            company_name="Other Target Corp",
            as_of_date=AS_OF,
            routes=(
                route(
                    "PUBLIC_BROKER_REPORT",
                    structured_records=(other_target,),
                    verified_seed_ingress=ingress,
                ),
            ),
            required_roles_by_component={
                "valuation_rerating": ("FORWARD_PB",)
            },
        )
        self.assertEqual(
            [row.reason for row in scoped_result.rejections],
            ["BROKER_VALUATION_VERIFIED_INGRESS_SCOPE_MISMATCH"],
        )

        other_as_of = date(2026, 6, 28)
        other_date_record = replace(
            valid,
            as_of_date=other_as_of.isoformat(),
        )
        date_scoped_result = (
            StructuredFinancialConsensusValuationEngine().research(
                target_id=TARGET,
                symbol=SYMBOL,
                company_name="Current Target Corp",
                as_of_date=other_as_of,
                routes=(
                    route(
                        "PUBLIC_BROKER_REPORT",
                        structured_records=(other_date_record,),
                        verified_seed_ingress=ingress,
                    ),
                ),
                required_roles_by_component={
                    "valuation_rerating": ("FORWARD_PB",)
                },
            )
        )
        self.assertEqual(
            [row.reason for row in date_scoped_result.rejections],
            ["BROKER_VALUATION_VERIFIED_INGRESS_SCOPE_MISMATCH"],
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

    def test_actual_equity_and_scenario_income_derive_forward_book_and_pb(self) -> None:
        result = self._run(
            route(
                "DART_ACTUALS_DETERMINISTIC_SCENARIO",
                financial_actuals=(actual(2025),),
            ),
            route(
                "ISSUER_GUIDANCE",
                structured_records=(
                    metric("equity", 200.0, "ACTUAL_EQUITY"),
                    metric(
                        "depreciation_and_amortization",
                        5.0,
                        "LATEST_ACTUAL_DEPRECIATION_AMORTIZATION",
                    ),
                    metric("cash_and_equivalents", 100.0, "BALANCE_SHEET_CASH"),
                    metric("total_debt", 40.0, "BALANCE_SHEET_DEBT"),
                ),
            ),
            route("KRX_PRICE_MARKET_CAP", price_bars=price_bars()),
        )
        rows = {row.metric_id: row for row in result.records}
        self.assertIn("scenario_base_book_value_per_share", rows)
        self.assertIn("forward_book_value", rows)
        self.assertIn("forward_pb", rows)
        self.assertIn("scenario_base_ebitda", rows)
        self.assertIn("forward_ev_ebitda", rows)
        scenario_book = rows["scenario_base_book_value_per_share"]
        self.assertEqual(scenario_book.provenance, "DETERMINISTIC_SCENARIO")
        self.assertFalse(scenario_book.metadata["observed_fact"])
        self.assertEqual(
            scenario_book.metadata["book_value_formula"],
            "latest_reported_equity + projected_net_income; "
            "dividends_and_oci_held_zero",
        )

    def test_report_eps_and_krx_history_create_daily_own_forward_pe_band(self) -> None:
        def report(
            observed: date,
            *,
            broker: str,
            eps: float,
            provider_close: float,
            provider_per: float,
            report_suffix: str = "",
        ) -> ResearchReport:
            return ResearchReport(
                symbol=SYMBOL,
                publish_date=observed,
                broker=broker,
                title=f"{broker} forward estimate",
                as_of_date=AS_OF,
                current_price=provider_close,
                fy1_eps=eps,
                est_per=provider_per,
                parsed_fields={
                    "structured_consensus_source": True,
                    "report_id": (
                        f"{broker}-{observed.isoformat()}{report_suffix}"
                    ),
                },
            )

        reports = (
            report(
                date(2026, 5, 1),
                broker="A",
                eps=10.0,
                provider_close=999.0,
                provider_per=99.9,
            ),
            report(
                date(2026, 5, 1),
                broker="A",
                eps=20.0,
                provider_close=999.0,
                provider_per=49.95,
                report_suffix="-SECOND",
            ),
            report(
                date(2026, 5, 1),
                broker="B",
                eps=10.0,
                provider_close=999.0,
                provider_per=99.9,
            ),
            report(
                date(2026, 5, 15),
                broker="B",
                eps=12.0,
                provider_close=999.0,
                provider_per=83.25,
            ),
            report(
                date(2026, 6, 1),
                broker="C",
                eps=15.0,
                provider_close=999.0,
                provider_per=66.6,
            ),
        )
        prices = tuple(
            PriceBar(
                symbol=SYMBOL,
                date=observed,
                open=close,
                high=close,
                low=close,
                close=close,
                adj_close=close,
                volume=100,
                trading_value=1_000.0,
                market_cap=10_000.0,
                source="KRX",
                as_of_date=AS_OF,
            )
            for observed, close in (
                (date(2026, 5, 1), 100.0),
                (date(2026, 5, 15), 120.0),
                (date(2026, 6, 1), 150.0),
            )
        )

        def run(rows: tuple[ResearchReport, ...]):
            return self._run(
                route(
                    "COMPANYGUIDE",
                    research_reports=rows,
                    consensus_snapshots=(
                        consensus(date(2026, 6, 1), eps=15.0),
                    ),
                ),
                route("KRX_PRICE_MARKET_CAP", price_bars=prices),
            )

        first = run(reports)
        changed_provider_values = tuple(
            replace(row, current_price=1.0, est_per=0.1)
            for row in reversed(reports)
        )
        second = run(changed_provider_values)
        first_history = tuple(
            row.to_dict()
            for row in first.records
            if row.record_kind == "VALUATION_HISTORY_OBSERVATION"
        )
        second_history = tuple(
            row.to_dict()
            for row in second.records
            if row.record_kind == "VALUATION_HISTORY_OBSERVATION"
        )
        self.assertEqual(first_history, second_history)
        self.assertEqual(
            [row["value"] for row in first_history], [8.75, 10.0, 10.0]
        )
        self.assertEqual(first_history[0]["metadata"]["broker_count"], 2)
        self.assertEqual(
            first_history[0]["metadata"]["report_eps_observation_count"], 3
        )
        self.assertTrue(
            all(row["metadata"]["provider_close_price_ignored"] for row in first_history)
        )
        band_rows = tuple(
            row
            for row in first.records
            if "OWN_HISTORICAL_BAND" in row.evidence_roles
        )
        self.assertEqual(len(band_rows), 4)
        self.assertEqual(
            {row.metadata["history_observation_count"] for row in band_rows},
            {3},
        )

    def test_forward_pe_history_requires_three_dates_and_no_future_price(self) -> None:
        reports = tuple(
            ResearchReport(
                symbol=SYMBOL,
                publish_date=observed,
                broker=f"Broker-{index}",
                title="Forward EPS",
                as_of_date=AS_OF,
                fy1_eps=10.0,
                parsed_fields={
                    "structured_consensus_source": True,
                    "report_id": f"REPORT-{index}",
                },
            )
            for index, observed in enumerate(
                (date(2026, 6, 10), date(2026, 6, 20)), start=1
            )
        )
        future_only_price = PriceBar(
            symbol=SYMBOL,
            date=date(2026, 6, 21),
            open=100.0,
            high=100.0,
            low=100.0,
            close=100.0,
            adj_close=100.0,
            volume=100,
            trading_value=1_000.0,
            market_cap=10_000.0,
            source="KRX",
            as_of_date=AS_OF,
        )
        result = self._run(
            route("COMPANYGUIDE", research_reports=reports),
            route("KRX_PRICE_MARKET_CAP", price_bars=(future_only_price,)),
        )
        self.assertFalse(
            any(
                row.record_kind == "VALUATION_HISTORY_OBSERVATION"
                for row in result.records
            )
        )
        self.assertFalse(
            any("OWN_HISTORICAL_BAND" in row.evidence_roles for row in result.records)
        )

    def test_conflicting_latest_krx_close_cannot_choose_current_band_input(self) -> None:
        reports = tuple(
            ResearchReport(
                symbol=SYMBOL,
                publish_date=observed,
                broker=f"Broker-{index}",
                title="Forward EPS",
                as_of_date=AS_OF,
                fy1_eps=eps,
                parsed_fields={
                    "structured_consensus_source": True,
                    "report_id": f"REPORT-{index}",
                },
            )
            for index, (observed, eps) in enumerate(
                (
                    (date(2026, 5, 1), 10.0),
                    (date(2026, 5, 15), 12.0),
                    (date(2026, 6, 1), 15.0),
                ),
                start=1,
            )
        )

        def bar(observed: date, close: float) -> PriceBar:
            return PriceBar(
                symbol=SYMBOL,
                date=observed,
                open=close,
                high=close,
                low=close,
                close=close,
                adj_close=close,
                volume=100,
                trading_value=1_000.0,
                market_cap=close * 100.0,
                source="KRX",
                as_of_date=AS_OF,
            )

        prices = (
            bar(date(2026, 5, 1), 100.0),
            bar(date(2026, 5, 15), 120.0),
            bar(date(2026, 6, 1), 150.0),
            bar(date(2026, 6, 20), 200.0),
            bar(date(2026, 6, 20), 300.0),
        )

        def run(rows: tuple[PriceBar, ...]):
            return self._run(
                route(
                    "COMPANYGUIDE",
                    research_reports=reports,
                    consensus_snapshots=(
                        ConsensusSnapshot(
                            symbol=SYMBOL,
                            date=date(2026, 6, 20),
                            fiscal_year=2026,
                            as_of_date=AS_OF,
                            source="CompanyGuide",
                            eps_e=10.0,
                        ),
                    ),
                ),
                route("KRX_PRICE_MARKET_CAP", price_bars=rows),
            )

        first = run(prices)
        second = run(tuple(reversed(prices)))
        for result in (first, second):
            self.assertFalse(
                any(row.metric_id == "current_price" for row in result.records)
            )
            self.assertEqual(
                len(
                    [
                        row
                        for row in result.records
                        if row.record_kind == "VALUATION_HISTORY_OBSERVATION"
                    ]
                ),
                3,
            )
            self.assertFalse(
                any(
                    "OWN_HISTORICAL_BAND" in row.evidence_roles
                    for row in result.records
                )
            )
        first_projection = tuple(row.to_dict() for row in first.records)
        second_projection = tuple(row.to_dict() for row in second.records)
        self.assertEqual(first_projection, second_projection)

    def test_untrusted_report_route_cannot_create_own_forward_pe_history(self) -> None:
        report = ResearchReport(
            symbol=SYMBOL,
            publish_date=date(2026, 6, 1),
            broker="Broker",
            title="Forward EPS",
            as_of_date=AS_OF,
            fy1_eps=10.0,
            parsed_fields={
                "structured_consensus_source": True,
                "report_id": "REPORT-1",
            },
        )
        result = self._run(
            route("UNTRUSTED_REPORT_ROUTE", research_reports=(report,)),
            route("KRX_PRICE_MARKET_CAP", price_bars=price_bars()),
        )
        self.assertFalse(
            any(
                row.record_kind == "VALUATION_HISTORY_OBSERVATION"
                for row in result.records
            )
        )

    def test_report_cannot_preserve_unbound_page_source_metadata(self) -> None:
        report = ResearchReport(
            symbol=SYMBOL,
            publish_date=date(2026, 6, 1),
            broker="Broker",
            title="Forward EPS",
            as_of_date=AS_OF,
            fy1_eps=10.0,
            parsed_fields={
                "structured_consensus_source": True,
                "report_id": "REPORT-UNBOUND-SOURCE",
                "structured_page_source_id": "NOT-IN-PAYLOAD",
            },
        )
        result = self._run(route("COMPANYGUIDE", research_reports=(report,)))
        eps = next(
            row for row in result.records if row.metric_id == "broker_forward_eps"
        )
        self.assertEqual(eps.source_ids, ("SRC-COMPANYGUIDE",))
        self.assertIsNone(eps.metadata["structured_page_source_id"])

    def test_self_attested_companyguide_seed_cannot_create_history_or_band(self) -> None:
        forged = tuple(
            StructuredMetricRecord(
                record_id=f"FORGED-COMPANYGUIDE-EPS-{index}",
                target_id=TARGET,
                as_of_date=AS_OF.isoformat(),
                metric_id="broker_forward_eps",
                value=value,
                unit="CURRENCY_PER_SHARE",
                period="FY2026E",
                evidence_roles=(
                    "FORWARD_EPS",
                    "PUBLIC_BROKER_FORWARD_ESTIMATE",
                ),
                source_ids=(f"FORGED-SOURCE-{index}",),
                source_route="COMPANYGUIDE",
                observed_at=observed.isoformat(),
                available_at=observed.isoformat(),
                record_kind="PUBLIC_BROKER_STRUCTURED_ESTIMATE",
                confidence=0.99,
                dataset="CONSENSUS_REVISION",
                provenance="STRUCTURED_EXTRACTED",
                metadata={
                    "broker": f"Forged-{index}",
                    "structured_source": True,
                    "forward_index": 1,
                },
            )
            for index, (observed, value) in enumerate(
                (
                    (date(2026, 5, 1), 10.0),
                    (date(2026, 5, 15), 12.0),
                    (date(2026, 6, 1), 15.0),
                ),
                start=1,
            )
        )
        result = self._run(
            route("COMPANYGUIDE", structured_records=forged),
            route("KRX_PRICE_MARKET_CAP", price_bars=price_bars()),
        )
        self.assertEqual(result.rejections, ())
        self.assertFalse(
            any(
                row.record_kind == "VALUATION_HISTORY_OBSERVATION"
                for row in result.records
            )
        )
        self.assertFalse(
            any("OWN_HISTORICAL_BAND" in row.evidence_roles for row in result.records)
        )

    def test_historical_rows_without_current_multiple_do_not_create_band(self) -> None:
        history = tuple(
            metric(
                "historical_forward_pe",
                value,
                "VALUATION_HISTORY",
                period=f"FY{year}",
            )
            for year, value in ((2022, 8.0), (2023, 10.0), (2024, 12.0))
        )
        result = self._run(route("ISSUER_GUIDANCE", structured_records=history))
        self.assertFalse(
            any("OWN_HISTORICAL_BAND" in row.evidence_roles for row in result.records)
        )

    def test_history_observation_cannot_masquerade_as_current_multiple(self) -> None:
        history = tuple(
            metric(
                "historical_forward_pe",
                value,
                "VALUATION_HISTORY",
                period=f"FY{year}",
            )
            for year, value in ((2022, 8.0), (2023, 10.0), (2024, 12.0))
        )
        forged_current = StructuredMetricRecord(
            record_id="FORGED-HISTORY-AS-CURRENT",
            target_id=TARGET,
            as_of_date=AS_OF.isoformat(),
            metric_id="historical_forward_pe",
            value=99.0,
            unit="MULTIPLE",
            period="FWD_1Y_AS_OF_2026-06-20",
            evidence_roles=("FORWARD_PE",),
            source_ids=("FORGED-HISTORY-SOURCE",),
            source_route="COMPANYGUIDE",
            observed_at="2026-06-20",
            available_at="2026-06-20",
            record_kind="VALUATION_HISTORY_OBSERVATION",
            confidence=0.99,
            dataset="CONSENSUS_REVISION",
            provenance="STRUCTURED_EXTRACTED",
            metadata={"structured_source": True},
        )
        result = self._run(
            route(
                "COMPANYGUIDE",
                structured_records=(forged_current,),
            ),
            route("ISSUER_GUIDANCE", structured_records=history),
        )
        self.assertEqual(result.rejections, ())
        self.assertFalse(
            any("OWN_HISTORICAL_BAND" in row.evidence_roles for row in result.records)
        )

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

    def test_public_broker_valuation_fields_cannot_bypass_verified_fact_ingress(
        self,
    ) -> None:
        report = ResearchReport(
            symbol=SYMBOL,
            publish_date=date(2026, 6, 20),
            broker="Broker",
            title="Unbound valuation fields",
            as_of_date=AS_OF,
            est_per=88.0,
            est_pbr=99.0,
            raw_text="Full report says nothing that binds a valuation or period.",
        )
        report_result = StructuredFinancialConsensusValuationEngine().research(
            target_id=TARGET,
            symbol=SYMBOL,
            company_name="Current Target Corp",
            as_of_date=AS_OF,
            routes=(
                PublicBrokerReportStructuredRoute(
                    reports=(report,),
                    source_ids=("SRC-REPORT",),
                ),
            ),
            required_roles_by_component={
                "valuation_rerating": ("FORWARD_PE", "FORWARD_PB")
            },
        )
        self.assertEqual(report_result.status, "SOURCE_PENDING")
        self.assertEqual(
            report_result.missing_roles_by_component["valuation_rerating"],
            ("FORWARD_PB", "FORWARD_PE"),
        )
        self.assertFalse(
            any(
                row.record_kind == "PUBLIC_BROKER_STRUCTURED_VALUATION"
                for row in report_result.records
            )
        )

        snapshot_result = StructuredFinancialConsensusValuationEngine().research(
            target_id=TARGET,
            symbol=SYMBOL,
            company_name="Current Target Corp",
            as_of_date=AS_OF,
            routes=(
                route(
                    "PUBLIC_BROKER_REPORT",
                    consensus_snapshots=(
                        consensus(date(2026, 6, 20), pbr=99.0),
                    ),
                ),
            ),
            required_roles_by_component={
                "valuation_rerating": ("FORWARD_PB",)
            },
        )
        self.assertEqual(snapshot_result.status, "SOURCE_PENDING")
        self.assertEqual(
            [row.reason for row in snapshot_result.rejections],
            ["PUBLIC_BROKER_CONSENSUS_REQUIRES_VERIFIED_FACT_INGRESS"],
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
