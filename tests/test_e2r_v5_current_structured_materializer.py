from __future__ import annotations

from datetime import date
from dataclasses import replace
import hashlib
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from e2r.production.source_connectors.companyguide_live_connector import (
    parse_companyguide_live_consensus_payload,
)
from e2r.research_brain.researcher_mode import (
    CurrentStructuredSourceMaterializer,
    EvidenceFact,
    OfficialSourceMaterializationResult,
    StructuredHTTPResponse,
)


class FixtureStructuredTransport:
    def __init__(self, *, future_companyguide: bool = False) -> None:
        self.calls: list[tuple[str, str, dict]] = []
        self.future_companyguide = future_companyguide

    def get_json(self, *, url, params, headers, timeout_seconds):
        del headers, timeout_seconds
        self.calls.append(("json", url, dict(params)))
        if "fnlttSinglAcntAll" in url:
            self.assert_dart_corp_code(params)
            year = int(params["bsns_year"])
            report_code = str(params["reprt_code"])
            payload = _dart_payload(year=year, report_code=report_code)
        elif "c1080001_data" in url:
            payload = _companyguide_reports_payload()
        elif "getstockpriceinfo" in url.casefold():
            payload = _data_go_payload()
        elif "/sto/" in url:
            payload = {"OutBlock_1": [_krx_stock_row()]}
        elif "/idx/" in url:
            payload = {"OutBlock_1": [_krx_index_row(params["basDd"])]}
        else:
            raise AssertionError(f"unexpected fixture URL: {url}")
        raw = json.dumps(payload, ensure_ascii=False, sort_keys=True).encode()
        return StructuredHTTPResponse(
            status_code=200,
            canonical_url=url,
            provider_request_id="FIXTURE-JSON",
            content_hash=hashlib.sha256(raw).hexdigest(),
            payload=payload,
        )

    def get_text(self, *, url, params, headers, timeout_seconds):
        del headers, timeout_seconds
        self.calls.append(("text", url, dict(params)))
        symbol = str(params.get("cmp_cd") or "")
        peer_definition = {
            "111111": ("Peer Alpha", 8.0, 1.4, 4.0),
            "222222": ("Peer Beta", 12.0, 2.2, 6.0),
        }.get(symbol)
        text = _companyguide_html(
            "2026.07.13" if self.future_companyguide else "2026.07.10",
            company_name=(peer_definition or ("Current Corp",))[0],
            forward_per=(peer_definition or (None, 4.94))[1],
            forward_pbr=(peer_definition or (None, None, 1.99))[2],
            forward_ev_ebitda=(peer_definition or (None, None, None, 2.55))[3],
        )
        return StructuredHTTPResponse(
            status_code=200,
            canonical_url=url,
            provider_request_id="FIXTURE-TEXT",
            content_hash=hashlib.sha256(text.encode()).hexdigest(),
            text=text,
        )

    def assert_dart_corp_code(self, params):
        if params.get("corp_code") != "00126380":
            raise AssertionError("DART corp_code was not restored to eight digits")


class FixturePeerProvider:
    provider_name = "FIXTURE_PEER_PROVIDER"

    def __init__(self):
        self.calls = []

    def complete(self, *, pass_name, payload):
        if pass_name != "STRUCTURED_PEER_SELECTION":
            raise AssertionError(pass_name)
        self.calls.append({"pass_name": pass_name, "payload": payload})
        return {
            "peers": [
                {
                    "peer_symbol": "111111",
                    "peer_name": "Peer Alpha",
                    "shared_economic_drivers": ["same capital-intensive revenue model"],
                    "material_differences": ["smaller customer base"],
                    "comparability_rationale": "cash and cycle economics are comparable",
                    "confidence": 0.85,
                },
                {
                    "peer_symbol": "222222",
                    "peer_name": "Peer Beta",
                    "shared_economic_drivers": ["same capacity-led earnings cycle"],
                    "material_differences": ["different product mix"],
                    "comparability_rationale": "forward multiple drivers are comparable",
                    "confidence": 0.8,
                },
            ],
            "selection_complete": True,
            "unresolved_research_notes": [],
            "selection_rationale": "two economic peers cover the valuation comparison",
        }


class IncompleteThenCompletePeerProvider(FixturePeerProvider):
    def __init__(self):
        super().__init__()
        self.attempt_count = 0

    def complete(self, *, pass_name, payload):
        self.attempt_count += 1
        if self.attempt_count == 1:
            self.calls.append({"pass_name": pass_name, "payload": payload})
            return {
                "peers": [],
                "selection_complete": False,
                "unresolved_research_notes": ["first response incomplete"],
                "selection_rationale": "peer selection needs a clean rewrite",
            }
        return super().complete(pass_name=pass_name, payload=payload)


class E2RV5CurrentStructuredMaterializerTests(unittest.TestCase):
    def test_companyguide_forward_fundamentals_keep_units_and_page_date(self):
        payload = parse_companyguide_live_consensus_payload(
            _companyguide_html("2026.07.10"),
            as_of_date=date(2026, 7, 12),
        )
        self.assertEqual(payload["CONSENSUS_AS_OF_DATE"], "2026/07/10")
        self.assertEqual(payload["FORWARD_12M_EPS"], 57_703)
        self.assertEqual(payload["FORWARD_12M_BPS"], 143_386)
        self.assertEqual(payload["FORWARD_12M_EBITDA"], 529_378_530_000_000)
        self.assertEqual(payload["FORWARD_12M_PER"], 4.94)
        self.assertEqual(payload["FORWARD_12M_PBR"], 1.99)
        self.assertEqual(payload["FORWARD_12M_EV_EBITDA"], 2.55)

    def test_live_sources_feed_phase86_and_resume_without_secret_or_refetch(self):
        transport = FixtureStructuredTransport()
        materializer = CurrentStructuredSourceMaterializer(
            transport=transport,
            price_lookback_days=400,
        )
        with tempfile.TemporaryDirectory() as directory, patch.dict(
            os.environ,
            {
                "OPENDART_API_KEY": "DART-SECRET-FIXTURE",
                "KRX_OPENAPI_KEY": "KRX-SECRET-FIXTURE",
                "DATA_GO_KR_SERVICE_KEY": "DATA-SECRET-FIXTURE",
            },
            clear=False,
        ):
            first = materializer.materialize(
                target_id="005930",
                target_name="Current Corp",
                as_of_date="2026-07-12",
                latest_trading_snapshot_date="2026-07-10",
                official=_official(),
                output_root=directory,
                checkpoint_resume=True,
            )
            first_call_count = len(transport.calls)
            second = materializer.materialize(
                target_id="005930",
                target_name="Current Corp",
                as_of_date="2026-07-12",
                latest_trading_snapshot_date="2026-07-10",
                official=_official(),
                output_root=directory,
                checkpoint_resume=True,
            )
            self.assertEqual(len(transport.calls), first_call_count)
            self.assertTrue(all(row.cache_hit for row in second.fetch_attempts))
            roles = {
                role
                for row in first.engine_result.records
                for role in row.evidence_roles
            }
            self.assertTrue(
                {
                    "LATEST_ACTUAL_REVENUE",
                    "LATEST_ACTUAL_OPERATING_PROFIT",
                    "OPERATING_CASH_FLOW",
                    "CAPEX",
                    "FREE_CASH_FLOW",
                    "CURRENT_PRICE",
                    "MARKET_CAP",
                    "FORWARD_EPS",
                    "FORWARD_BOOK_VALUE",
                    "FORWARD_FCF",
                    "FORWARD_FCF_YIELD",
                    "EPS_REVISION",
                    "OPERATING_PROFIT_REVISION",
                }.issubset(roles)
            )
            self.assertTrue(
                all(
                    value != "ZERO"
                    for value in first.engine_result.component_disposition_by_component.values()
                )
            )
            cache_text = "\n".join(
                path.read_text(encoding="utf-8")
                for path in Path(directory).rglob("*.json")
            )
            for secret in (
                "DART-SECRET-FIXTURE",
                "KRX-SECRET-FIXTURE",
                "DATA-SECRET-FIXTURE",
            ):
                self.assertNotIn(secret, cache_text)

    def test_future_companyguide_snapshot_never_becomes_record(self):
        transport = FixtureStructuredTransport(future_companyguide=True)
        with tempfile.TemporaryDirectory() as directory, patch.dict(
            os.environ,
            {
                "OPENDART_API_KEY": "DART-SECRET-FIXTURE",
                "KRX_OPENAPI_KEY": "KRX-SECRET-FIXTURE",
                "DATA_GO_KR_SERVICE_KEY": "DATA-SECRET-FIXTURE",
            },
            clear=False,
        ):
            result = CurrentStructuredSourceMaterializer(
                transport=transport,
                price_lookback_days=400,
            ).materialize(
                target_id="005930",
                target_name="Current Corp",
                as_of_date="2026-07-12",
                latest_trading_snapshot_date="2026-07-10",
                official=_official(),
                output_root=directory,
                checkpoint_resume=True,
            )
            self.assertFalse(
                any(
                    row.metadata.get("source_page_date") == "2026-07-13"
                    for row in result.engine_result.records
                )
            )
            self.assertTrue(
                all(row.observed_at[:10] <= "2026-07-12" for row in result.engine_result.records)
            )

    def test_verified_fact_claims_feed_segment_qoq_and_guidance_roles(self):
        transport = FixtureStructuredTransport()
        facts, claims, documents = _structured_fact_bundle()
        facts = tuple(
            replace(row, current_lifecycle="OPEN")
            if "FORWARD_GUIDANCE" in row.structured_evidence_roles
            else row
            for row in facts
        )
        with tempfile.TemporaryDirectory() as directory, patch.dict(
            os.environ,
            {
                "OPENDART_API_KEY": "DART-SECRET-FIXTURE",
                "KRX_OPENAPI_KEY": "KRX-SECRET-FIXTURE",
                "DATA_GO_KR_SERVICE_KEY": "DATA-SECRET-FIXTURE",
            },
            clear=False,
        ):
            result = CurrentStructuredSourceMaterializer(
                transport=transport,
                price_lookback_days=400,
            ).materialize(
                target_id="005930",
                target_name="Current Corp",
                as_of_date="2026-07-12",
                latest_trading_snapshot_date="2026-07-10",
                official=_official(),
                output_root=directory,
                checkpoint_resume=True,
                evidence_facts=facts,
                source_claims=claims,
                source_documents=documents,
            )
        roles = {
            role
            for row in result.engine_result.records
            for role in row.evidence_roles
        }
        self.assertTrue(
            {"SEGMENT_CONTRIBUTION", "QOQ_GROWTH", "FORWARD_GUIDANCE"}.issubset(
                roles
            )
        )
        fact_audit = result.audit["issuer_fact_materialization"]
        self.assertEqual(fact_audit["accepted_structured_observation_count"], 3)
        self.assertEqual(fact_audit["rejection_counts"], {})
        promoted = [
            row
            for row in result.engine_result.records
            if set(row.evidence_roles)
            & {"SEGMENT_CONTRIBUTION", "QOQ_GROWTH", "FORWARD_GUIDANCE"}
        ]
        self.assertTrue(all(row.metadata["exact_quote_verified"] for row in promoted))
        self.assertTrue(all(row.metadata["llm_role_nomination_only"] for row in promoted))

    def test_nonissuer_guidance_tag_remains_source_pending(self):
        transport = FixtureStructuredTransport()
        facts, claims, documents = _structured_fact_bundle(roles=("FORWARD_GUIDANCE",))
        documents = ({**documents[0], "source_family": "TRUSTED_BUSINESS_MEDIA"},)
        with tempfile.TemporaryDirectory() as directory, patch.dict(
            os.environ,
            {
                "OPENDART_API_KEY": "DART-SECRET-FIXTURE",
                "KRX_OPENAPI_KEY": "KRX-SECRET-FIXTURE",
                "DATA_GO_KR_SERVICE_KEY": "DATA-SECRET-FIXTURE",
            },
            clear=False,
        ):
            result = CurrentStructuredSourceMaterializer(
                transport=transport,
                price_lookback_days=400,
            ).materialize(
                target_id="005930",
                target_name="Current Corp",
                as_of_date="2026-07-12",
                latest_trading_snapshot_date="2026-07-10",
                official=_official(),
                output_root=directory,
                checkpoint_resume=True,
                evidence_facts=facts,
                source_claims=claims,
                source_documents=documents,
            )
        self.assertIn(
            "FORWARD_GUIDANCE",
            result.engine_result.missing_roles_by_component["eps_fcf_explosion"],
        )
        self.assertEqual(
            result.audit["issuer_fact_materialization"]["rejection_counts"],
            {"ROLE_SOURCE_FAMILY_NOT_ALLOWED:FORWARD_GUIDANCE": 1},
        )

    def test_llm_selects_peer_direction_but_structured_pages_supply_values(self):
        transport = FixtureStructuredTransport()
        peer_provider = FixturePeerProvider()
        facts, claims, documents = _structured_fact_bundle()
        with tempfile.TemporaryDirectory() as directory, patch.dict(
            os.environ,
            {
                "OPENDART_API_KEY": "DART-SECRET-FIXTURE",
                "KRX_OPENAPI_KEY": "KRX-SECRET-FIXTURE",
                "DATA_GO_KR_SERVICE_KEY": "DATA-SECRET-FIXTURE",
            },
            clear=False,
        ):
            result = CurrentStructuredSourceMaterializer(
                transport=transport,
                price_lookback_days=400,
                peer_provider=peer_provider,
            ).materialize(
                target_id="005930",
                target_name="Current Corp",
                as_of_date="2026-07-12",
                latest_trading_snapshot_date="2026-07-10",
                official=_official(),
                output_root=directory,
                checkpoint_resume=True,
                evidence_facts=facts,
                source_claims=claims,
                source_documents=documents,
            )
            resumed = CurrentStructuredSourceMaterializer(
                transport=transport,
                price_lookback_days=400,
                peer_provider=peer_provider,
            ).materialize(
                target_id="005930",
                target_name="Current Corp",
                as_of_date="2026-07-12",
                latest_trading_snapshot_date="2026-07-10",
                official=_official(),
                output_root=directory,
                checkpoint_resume=True,
                evidence_facts=facts,
                source_claims=claims,
                source_documents=documents,
            )
        self.assertEqual(len(peer_provider.calls), 1)
        provider_payload = json.dumps(peer_provider.calls[0]["payload"], sort_keys=True)
        self.assertNotIn("suggested_queries", provider_payload)
        self.assertFalse(
            peer_provider.calls[0]["payload"]["selection_constraints"][
                "score_or_stage_authority"
            ]
        )
        self.assertNotIn("current_score", provider_payload.casefold())
        self.assertNotIn("current_stage", provider_payload.casefold())
        peer_audit = result.audit["peer_selection"]
        self.assertEqual(peer_audit["status"], "PEER_SELECTION_COMPLETE")
        self.assertEqual(peer_audit["verified_peer_count"], 2)
        self.assertTrue(resumed.audit["peer_selection"]["provider_cache_hit"])
        self.assertEqual(peer_audit["common_metric_peer_counts"]["forward_pe"], 2)
        peer_inputs = [
            row
            for row in result.engine_result.records
            if "PEER_BAND_INPUT" in row.evidence_roles
        ]
        self.assertEqual(
            {row.value for row in peer_inputs if row.metric_id == "peer_forward_pe"},
            {8.0, 12.0},
        )
        peer_bands = [
            row
            for row in result.engine_result.records
            if "PEER_BAND" in row.evidence_roles
        ]
        self.assertTrue(peer_bands)
        self.assertTrue(all(row.provenance == "DERIVED" for row in peer_bands))
        self.assertTrue(
            all(row.metadata["peer_count"] == 2 for row in peer_bands)
        )

    def test_incomplete_peer_selection_is_reprompted_without_value_invention(self):
        transport = FixtureStructuredTransport()
        peer_provider = IncompleteThenCompletePeerProvider()
        facts, claims, documents = _structured_fact_bundle()
        with tempfile.TemporaryDirectory() as directory, patch.dict(
            os.environ,
            {
                "OPENDART_API_KEY": "DART-SECRET-FIXTURE",
                "KRX_OPENAPI_KEY": "KRX-SECRET-FIXTURE",
                "DATA_GO_KR_SERVICE_KEY": "DATA-SECRET-FIXTURE",
            },
            clear=False,
        ):
            result = CurrentStructuredSourceMaterializer(
                transport=transport,
                price_lookback_days=400,
                peer_provider=peer_provider,
            ).materialize(
                target_id="005930",
                target_name="Current Corp",
                as_of_date="2026-07-12",
                latest_trading_snapshot_date="2026-07-10",
                official=_official(),
                output_root=directory,
                checkpoint_resume=True,
                evidence_facts=facts,
                source_claims=claims,
                source_documents=documents,
            )
        audit = result.audit["peer_selection"]
        self.assertEqual(peer_provider.attempt_count, 2)
        self.assertEqual(audit["status"], "PEER_SELECTION_COMPLETE")
        self.assertEqual(audit["provider_attempt_count"], 2)
        self.assertTrue(audit["validation_retry_used"])
        retry = peer_provider.calls[-1]["payload"][
            "peer_selection_retry_context"
        ]
        self.assertIn("peer selection is incomplete", retry["validation_error"])
        self.assertIn("do not invent", retry["instruction"])


def _official():
    return OfficialSourceMaterializationResult(
        target_id="005930",
        as_of_date="2026-07-12",
        status="OFFICIAL_SOURCE_MATERIALIZED",
        evidence_documents=(),
        provider_attempts=(),
        structured_payloads=(
            {"provider_name": "OpenDART", "payload": {"corp_code": "126380"}},
        ),
        pending_reasons=(),
        audit={},
    )


def _structured_fact_bundle(roles=None):
    selected_roles = tuple(
        roles
        or ("SEGMENT_CONTRIBUTION", "QOQ_GROWTH", "FORWARD_GUIDANCE")
    )
    definitions = {
        "SEGMENT_CONTRIBUTION": {
            "quote": "Memory revenue contribution was 35% in 2026Q1.",
            "value": "35",
            "unit": "%",
            "period": "2026Q1",
            "predicate": "memory_revenue_contribution",
        },
        "QOQ_GROWTH": {
            "quote": "Revenue grew 12.5% quarter over quarter in 2026Q2.",
            "value": "12.5",
            "unit": "percent",
            "period": "2026Q2",
            "predicate": "revenue_growth",
        },
        "FORWARD_GUIDANCE": {
            "quote": "The company guided 2026Q3 revenue to 100~120 billion won.",
            "value": "100~120",
            "unit": "억원",
            "period": "2026Q3",
            "predicate": "revenue_guidance",
        },
    }
    text = " ".join(definitions[role]["quote"] for role in selected_roles)
    document = {
        "document_id": "DOC-ISSUER-STRUCTURED",
        "target_id": "005930",
        "as_of_date": "2026-07-12",
        "canonical_url": "https://issuer.example.com/results",
        "title": "Current Corp official results",
        "source_family": "ISSUER_PRESENTATION",
        "published_at": "2026-07-08",
        "available_at": "2026-07-08",
        "content_hash": hashlib.sha256(text.encode()).hexdigest(),
        "content_text": text,
        "source_independence_group": "ISSUER:issuer.example.com",
        "full_fetch_performed": True,
        "snippet_only": False,
        "evidence_eligible": True,
    }
    facts = []
    claims = []
    for index, role in enumerate(selected_roles, start=1):
        definition = definitions[role]
        claim_id = f"CLAIM-{index}"
        fact_id = f"FACT-{index}"
        claims.append(
            {
                "claim_id": claim_id,
                "target_id": "005930",
                "as_of_date": "2026-07-12",
                "accepted": True,
                "accepted_by_evidence_os": True,
                "material": True,
                "document_id": document["document_id"],
                "exact_quote": definition["quote"],
                "business_segment": "MEMORY",
                "scope_business_segment": "MEMORY",
                "product_family": "HBM",
                "scope_product_family": "HBM",
                "predicate_family": definition["predicate"],
                "normalized_object": definition["predicate"],
                "value": definition["value"],
                "unit": definition["unit"],
                "period": definition["period"],
                "confidence": 0.9,
                "structured_evidence_roles": [role],
            }
        )
        facts.append(
            EvidenceFact(
                fact_id=fact_id,
                target_id="005930",
                as_of_date="2026-07-12",
                subject="Current Corp memory business",
                business_segment="MEMORY",
                product_family="HBM",
                economic_mechanism=definition["predicate"],
                predicate=definition["predicate"],
                value=definition["value"],
                unit=definition["unit"],
                period=definition["period"],
                direction="POSITIVE",
                source_ids=(document["document_id"],),
                claim_ids=(claim_id,),
                quote_ids=(f"QUOTE-{index}",),
                current_lifecycle="CURRENT",
                source_independence_group="ISSUER:issuer.example.com",
                confidence=0.9,
                structured_evidence_roles=(role,),
            )
        )
    return tuple(facts), tuple(claims), (document,)


def _dart_payload(*, year: int, report_code: str):
    multiplier = year - 2020
    quarter_factor = 1 if report_code == "11013" else 4
    return {
        "status": "000",
        "list": [
            _dart_row("IS", "매출액", 10_000 * multiplier * quarter_factor),
            _dart_row("IS", "영업이익", 2_000 * multiplier * quarter_factor),
            _dart_row("IS", "당기순이익", 1_500 * multiplier * quarter_factor),
            _dart_row("CF", "영업활동으로 인한 현금흐름", 1_800 * multiplier * quarter_factor),
            _dart_row("CF", "유형자산의 취득", 600 * multiplier * quarter_factor),
            _dart_row("BS", "현금및현금성자산", 5_000 * multiplier),
            _dart_row("BS", "총차입금", 1_000 * multiplier),
            _dart_row("BS", "자본총계", 20_000 * multiplier),
        ],
    }


def _dart_row(statement, account_name, amount):
    return {
        "fs_div": "CFS",
        "fs_nm": "연결재무제표",
        "sj_div": statement,
        "account_nm": account_name,
        "thstrm_amount": str(amount),
    }


def _companyguide_html(
    page_date: str,
    *,
    company_name: str = "Current Corp",
    forward_per: float = 4.94,
    forward_pbr: float = 1.99,
    forward_ev_ebitda: float = 2.55,
):
    return f"""
    <title>{company_name} - 기업현황 - 기업모니터</title>
    <p>[기준:{page_date}]</p>
    <table id="cTB15"><tbody><tr>
      <td>4.0</td><td>500,000</td><td>46,664</td><td>6.11</td><td>24</td>
    </tr></tbody></table>
    <table summary="기업 펀더멘털 실적, 컨센서스 정보 리스트입니다.">
      <thead><tr><th>주요지표</th><th>2025/12(A)</th><th>2026/12(E)</th><th>Fwd. 12M(E)</th></tr></thead>
      <tbody>
        <tr><th>PER</th><td>43.42</td><td>6.11</td><td>{forward_per}</td></tr>
        <tr><th>PBR</th><td>4.45</td><td>2.61</td><td>{forward_pbr}</td></tr>
        <tr><th>EV/EBITDA</th><td>19.02</td><td>3.51</td><td>{forward_ev_ebitda}</td></tr>
        <tr><th>EPS</th><td>6,564원</td><td>46,664원</td><td>57,703원</td></tr>
        <tr><th>BPS</th><td>63,997원</td><td>109,207원</td><td>143,386원</td></tr>
        <tr><th>EBITDA</th><td>905,276.4억원</td><td>4,341,515.6억원</td><td>5,293,785.3억원</td></tr>
      </tbody>
    </table>
    """


def _companyguide_reports_payload():
    return {
        "lists": [
            {
                "ANL_DT": "26/07/03",
                "BRK_NM_SHORT_KOR": "A증권",
                "RPT_TITLE": "실적 전망치 상향",
                "COMMENT": "2026년 영업이익 전망치를 10조원으로 상향 조정, 컨센서스 상회",
                "EPS": "12000",
                "EPS_ACTION_TYP_NM": "상향",
                "CLOSE_PRC": "120000",
                "TARGET_PRC": "180000",
                "RPT_ID": "R1",
            },
            {
                "ANL_DT": "26/06/03",
                "BRK_NM_SHORT_KOR": "A증권",
                "RPT_TITLE": "기존 전망",
                "COMMENT": "2026년 영업이익 9조원 전망",
                "EPS": "10000",
                "EPS_ACTION_TYP_NM": "유지",
                "CLOSE_PRC": "100000",
                "TARGET_PRC": "160000",
                "RPT_ID": "R0",
            },
        ]
    }


def _data_go_payload():
    return {
        "response": {
            "body": {
                "totalCount": 2,
                "numOfRows": 1000,
                "items": {
                    "item": [
                        {
                            "srtnCd": "005930",
                            "basDt": "20260605",
                            "mkp": "100000",
                            "hipr": "102000",
                            "lopr": "99000",
                            "clpr": "101000",
                            "trqu": "100",
                            "trPrc": "10100000",
                            "mrktTotAmt": "1000000000",
                        },
                        {
                            "srtnCd": "005930",
                            "basDt": "20260709",
                            "mkp": "119000",
                            "hipr": "121000",
                            "lopr": "118000",
                            "clpr": "120000",
                            "trqu": "100",
                            "trPrc": "12000000",
                            "mrktTotAmt": "1200000000",
                        },
                    ]
                },
            }
        }
    }


def _krx_stock_row():
    return {
        "BAS_DD": "20260710",
        "ISU_CD": "005930",
        "ISU_NM": "Current Corp",
        "TDD_CLSPRC": "121000",
        "TDD_OPNPRC": "120000",
        "TDD_HGPRC": "122000",
        "TDD_LWPRC": "119000",
        "ACC_TRDVOL": "100",
        "ACC_TRDVAL": "12100000",
        "MKTCAP": "1210000000",
    }


def _krx_index_row(raw_date):
    return {
        "BAS_DD": raw_date,
        "IDX_NM": "코스피",
        "CLSPRC_IDX": "3000",
        "OPNPRC_IDX": "2990",
        "HGPRC_IDX": "3010",
        "LWPRC_IDX": "2980",
        "ACC_TRDVOL": "1000",
        "ACC_TRDVAL": "3000000",
        "MKTCAP": "3000000000",
    }


if __name__ == "__main__":
    unittest.main()
