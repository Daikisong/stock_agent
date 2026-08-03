from __future__ import annotations

from datetime import date
from dataclasses import replace
import hashlib
import io
import json
import os
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch

from e2r.production.source_connectors.companyguide_live_connector import (
    parse_companyguide_live_consensus_payload,
)
from e2r.research_brain.planning.provider_transport import (
    StructuredProviderUnavailable,
)
from e2r.research_brain.researcher_mode import (
    CurrentStructuredSourceMaterializer,
    EvidenceFact,
    OfficialSourceMaterializationResult,
    StructuredHTTPResponse,
)
from e2r.research_brain.researcher_mode import (
    current_structured_materializer as structured_materializer_module,
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
            payload = {
                "OutBlock_1": [
                    _krx_stock_row(),
                    _krx_stock_row(symbol="111111", name="Peer Alpha"),
                    _krx_stock_row(symbol="222222", name="Peer Beta"),
                    _krx_stock_row(
                        symbol="333333", name="Relabelled Company"
                    ),
                    _krx_stock_row(
                        symbol="444444", name="Invented Listing Vehicle"
                    ),
                ]
            }
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


class HistoricalReportFallbackStructuredTransport(FixtureStructuredTransport):
    """Peer snapshots lack consensus, while official equity remains available."""

    def __init__(self, *, peer_dart_status_by_report_code=None):
        super().__init__()
        self.peer_dart_status_by_report_code = dict(
            peer_dart_status_by_report_code or {}
        )

    def get_text(self, *, url, params, headers, timeout_seconds):
        symbol = str(params.get("cmp_cd") or "")
        names = {"111111": "Peer Alpha", "222222": "Peer Beta"}
        if symbol not in names:
            return super().get_text(
                url=url,
                params=params,
                headers=headers,
                timeout_seconds=timeout_seconds,
            )
        del headers, timeout_seconds
        self.calls.append(("text", url, dict(params)))
        text = _companyguide_no_consensus_html(
            "2026.08.03",
            company_name=names[symbol],
        )
        return StructuredHTTPResponse(
            status_code=200,
            canonical_url=url,
            provider_request_id="FIXTURE-NO-CONSENSUS",
            content_hash=hashlib.sha256(text.encode()).hexdigest(),
            text=text,
        )

    def get_json(self, *, url, params, headers, timeout_seconds):
        symbol = str(params.get("cmp_cd") or "")
        names = {"111111": "Peer Alpha", "222222": "Peer Beta"}
        if "list.json" in url and str(params.get("corp_code")) in {
            "00000011",
            "00000022",
        }:
            del headers, timeout_seconds
            self.calls.append(("json", url, dict(params)))
            receipt_date = str(params["bgn_de"])
            if receipt_date == "20260515":
                report_name = "분기보고서 (2026.03)"
                receipt_no = "20260515000001"
            elif receipt_date == "20260331":
                report_name = "사업보고서 (2025.12)"
                receipt_no = "20260331000001"
            else:
                raise AssertionError(
                    f"unexpected peer filing receipt date: {receipt_date}"
                )
            payload = {
                "status": "000",
                "list": [
                    {
                        "corp_code": str(params["corp_code"]),
                        "rcept_no": receipt_no,
                        "rcept_dt": receipt_date,
                        "report_nm": report_name,
                    }
                ],
            }
            raw = json.dumps(
                payload, ensure_ascii=False, sort_keys=True
            ).encode()
            return StructuredHTTPResponse(
                status_code=200,
                canonical_url=url,
                provider_request_id="FIXTURE-PEER-FILING-PERIOD",
                content_hash=hashlib.sha256(raw).hexdigest(),
                payload=payload,
            )
        if "fnlttSinglAcntAll" in url and str(params.get("corp_code")) in {
            "00000011",
            "00000022",
        }:
            del headers, timeout_seconds
            self.calls.append(("json", url, dict(params)))
            report_code = str(params["reprt_code"])
            fixture_status = self.peer_dart_status_by_report_code.get(
                report_code,
                "000",
            )
            if fixture_status == "PROVIDER_ERROR":
                raise OSError("fixture peer DART provider failure")
            if fixture_status != "000":
                payload = {"status": fixture_status, "list": []}
                raw = json.dumps(
                    payload, ensure_ascii=False, sort_keys=True
                ).encode()
                return StructuredHTTPResponse(
                    status_code=200,
                    canonical_url=url,
                    provider_request_id="FIXTURE-PEER-EQUITY-STATUS",
                    content_hash=hashlib.sha256(raw).hexdigest(),
                    payload=payload,
                )
            fiscal_year = int(params["bsns_year"])
            receipt_no = (
                f"{fiscal_year}0515000001"
                if report_code == "11013"
                else f"{fiscal_year + 1}0331000001"
            )
            payload = {
                "status": "000",
                "list": [
                    {
                        **_dart_row(
                            "BS",
                            "지배기업의 소유주에게 귀속되는 자본",
                            1_000_000_000,
                        ),
                        "account_id": (
                            "ifrs-full_EquityAttributableToOwnersOfParent"
                        ),
                        "corp_code": str(params["corp_code"]),
                        "bsns_year": str(params["bsns_year"]),
                        "reprt_code": report_code,
                        "currency": "KRW",
                        "rcept_no": receipt_no,
                    }
                ],
            }
            raw = json.dumps(payload, ensure_ascii=False, sort_keys=True).encode()
            return StructuredHTTPResponse(
                status_code=200,
                canonical_url=url,
                provider_request_id="FIXTURE-PEER-EQUITY",
                content_hash=hashlib.sha256(raw).hexdigest(),
                payload=payload,
            )
        return super().get_json(
            url=url,
            params=params,
            headers=headers,
            timeout_seconds=timeout_seconds,
        )


class MultipleEquityLineStructuredTransport(
    HistoricalReportFallbackStructuredTransport
):
    """The KRX roster contains common and preferred lines for one issuer."""

    def get_json(self, *, url, params, headers, timeout_seconds):
        response = super().get_json(
            url=url,
            params=params,
            headers=headers,
            timeout_seconds=timeout_seconds,
        )
        if "/sto/" not in url:
            return response
        payload = dict(response.payload or {})
        rows = list(payload.get("OutBlock_1") or ())
        rows.append(_krx_stock_row(symbol="111112", name="Peer Alpha우"))
        payload["OutBlock_1"] = rows
        raw = json.dumps(payload, ensure_ascii=False, sort_keys=True).encode()
        return StructuredHTTPResponse(
            status_code=200,
            canonical_url=response.canonical_url,
            provider_request_id="FIXTURE-MULTIPLE-EQUITY-LINES",
            content_hash=hashlib.sha256(raw).hexdigest(),
            payload=payload,
        )


class PaginatedReportStructuredTransport(FixtureStructuredTransport):
    def get_json(self, *, url, params, headers, timeout_seconds):
        if "c1080001_data" not in url:
            return super().get_json(
                url=url,
                params=params,
                headers=headers,
                timeout_seconds=timeout_seconds,
            )
        del headers, timeout_seconds
        self.calls.append(("json", url, dict(params)))
        page = int(params["curPage"])
        rows = _companyguide_reports_payload()["lists"]
        payload = {
            "cp": page,
            "tc": len(rows),
            "tp": len(rows),
            "tr": 1,
            "lists": [rows[page - 1]] if 1 <= page <= len(rows) else [],
        }
        raw = json.dumps(payload, ensure_ascii=False, sort_keys=True).encode()
        return StructuredHTTPResponse(
            status_code=200,
            canonical_url=url,
            provider_request_id=f"FIXTURE-REPORT-PAGE-{page}",
            content_hash=hashlib.sha256(raw).hexdigest(),
            payload=payload,
        )


class OverlappingPaginatedReportStructuredTransport(
    PaginatedReportStructuredTransport
):
    def get_json(self, *, url, params, headers, timeout_seconds):
        if "c1080001_data" not in url:
            return super().get_json(
                url=url,
                params=params,
                headers=headers,
                timeout_seconds=timeout_seconds,
            )
        del headers, timeout_seconds
        self.calls.append(("json", url, dict(params)))
        page = int(params["curPage"])
        row = _companyguide_reports_payload()["lists"][0]
        payload = {
            "cp": page,
            "tc": 2,
            "tp": 2,
            "tr": 1,
            "lists": [row],
        }
        raw = json.dumps(payload, ensure_ascii=False, sort_keys=True).encode()
        return StructuredHTTPResponse(
            status_code=200,
            canonical_url=url,
            provider_request_id=f"FIXTURE-OVERLAP-PAGE-{page}",
            content_hash=hashlib.sha256(raw).hexdigest(),
            payload=payload,
        )


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


class CleanResumePeerRetryProvider(FixturePeerProvider):
    def complete(self, *, pass_name, payload):
        if "peer_selection_retry_context" not in payload:
            self.calls.append({"pass_name": pass_name, "payload": payload})
            raise StructuredProviderUnavailable(
                "COLLABORATION_RESPONSE_PENDING:COLLABREQ-" + "a" * 64
            )
        return super().complete(pass_name=pass_name, payload=payload)

    def validated_peer_selection_retry_payload(self, *, primary_payload):
        return {
            **primary_payload,
            "peer_selection_retry_context": {
                "validation_error": "peer selection is incomplete",
                "instruction": (
                    "Rewrite the complete peer selection under the original "
                    "two-to-five peer contract; do not invent any valuation values."
                ),
            },
        }


class VerificationFailureThenCompletePeerProvider(FixturePeerProvider):
    def __init__(self):
        super().__init__()
        self.attempt_count = 0

    def complete(self, *, pass_name, payload):
        self.attempt_count += 1
        if self.attempt_count == 1:
            self.calls.append({"pass_name": pass_name, "payload": payload})
            return {
                "peers": [
                    {
                        "peer_symbol": symbol,
                        "peer_name": name,
                        "shared_economic_drivers": ["same earnings cycle"],
                        "material_differences": ["different product mix"],
                        "comparability_rationale": "cycle economics overlap",
                        "confidence": 0.8,
                    }
                    for symbol, name in (
                        ("333333", "Relabelled Company"),
                        ("444444", "Invented Listing Vehicle"),
                    )
                ],
                "selection_complete": True,
                "unresolved_research_notes": [],
                "selection_rationale": "unverified first proposal",
            }
        return super().complete(pass_name=pass_name, payload=payload)


class RepeatedVerificationFailurePeerProvider(FixturePeerProvider):
    def __init__(self):
        super().__init__()
        self.attempt_count = 0
        self.invalidations = []

    def complete(self, *, pass_name, payload):
        self.attempt_count += 1
        if self.attempt_count <= 2:
            self.calls.append({"pass_name": pass_name, "payload": payload})
            return {
                "peers": [
                    {
                        "peer_symbol": symbol,
                        "peer_name": name,
                        "shared_economic_drivers": ["same earnings cycle"],
                        "material_differences": ["different product mix"],
                        "comparability_rationale": "cycle economics overlap",
                        "confidence": 0.8,
                    }
                    for symbol, name in (
                        ("333333", "Relabelled Company"),
                        ("444444", "Invented Listing Vehicle"),
                    )
                ],
                "selection_complete": True,
                "unresolved_research_notes": [],
                "selection_rationale": "repeated unverified proposal",
            }
        return super().complete(pass_name=pass_name, payload=payload)

    def invalidate_last_response_cache(self, reason):
        event = {"status": "INVALIDATED", "reason": reason}
        self.invalidations.append(event)
        return event


class ExpansionPeerProvider(FixturePeerProvider):
    def complete(self, *, pass_name, payload):
        if pass_name != "STRUCTURED_PEER_SELECTION":
            raise AssertionError(pass_name)
        legacy_exclusive_roster = bool(
            (
                payload.get("point_in_time_peer_roster_accounting")
                or {}
            ).get(
                "when_two_or_more_available_select_only_from_this_roster"
            )
            or (payload.get("selection_constraints") or {}).get(
                (
                    "when_two_or_more_point_in_time_identities_are_available_"
                    "select_only_from_point_in_time_structured_peer_identity_roster"
                )
            )
        )
        if (
            "peer_selection_retry_context" not in payload
            or legacy_exclusive_roster
        ):
            return super().complete(pass_name=pass_name, payload=payload)
        self.calls.append({"pass_name": pass_name, "payload": payload})
        return {
            "peers": [
                {
                    "peer_symbol": "555555",
                    "peer_name": "Peer Gamma",
                    "shared_economic_drivers": ["same capital cycle"],
                    "material_differences": ["different customer mix"],
                    "comparability_rationale": "capacity economics overlap",
                    "confidence": 0.82,
                },
                {
                    "peer_symbol": "666666",
                    "peer_name": "Peer Delta",
                    "shared_economic_drivers": ["same demand cycle"],
                    "material_differences": ["different product mix"],
                    "comparability_rationale": "forward earnings cycle overlaps",
                    "confidence": 0.8,
                },
            ],
            "selection_complete": True,
            "unresolved_research_notes": [],
            "selection_rationale": "expand beyond cached availability hints",
        }


class ExpansionFixtureStructuredTransport(FixtureStructuredTransport):
    def get_json(self, *, url, params, headers, timeout_seconds):
        if "/sto/" not in url:
            return super().get_json(
                url=url,
                params=params,
                headers=headers,
                timeout_seconds=timeout_seconds,
            )
        del headers, timeout_seconds
        self.calls.append(("json", url, dict(params)))
        payload = {
            "OutBlock_1": [
                _krx_stock_row(),
                _krx_stock_row(symbol="111111", name="Peer Alpha"),
                _krx_stock_row(symbol="222222", name="Peer Beta"),
                _krx_stock_row(symbol="555555", name="Peer Gamma"),
                _krx_stock_row(symbol="666666", name="Peer Delta"),
            ]
        }
        raw = json.dumps(payload, ensure_ascii=False, sort_keys=True).encode()
        return StructuredHTTPResponse(
            status_code=200,
            canonical_url=url,
            provider_request_id="FIXTURE-EXPANSION-JSON",
            content_hash=hashlib.sha256(raw).hexdigest(),
            payload=payload,
        )

    def get_text(self, *, url, params, headers, timeout_seconds):
        symbol = str(params.get("cmp_cd") or "")
        definition = {
            "555555": ("Peer Gamma", 9.0, 1.6, 4.5),
            "666666": ("Peer Delta", 11.0, 2.0, 5.5),
        }.get(symbol)
        if definition is None:
            return super().get_text(
                url=url,
                params=params,
                headers=headers,
                timeout_seconds=timeout_seconds,
            )
        del headers, timeout_seconds
        self.calls.append(("text", url, dict(params)))
        text = _companyguide_html(
            "2026.07.10",
            company_name=definition[0],
            forward_per=definition[1],
            forward_pbr=definition[2],
            forward_ev_ebitda=definition[3],
        )
        return StructuredHTTPResponse(
            status_code=200,
            canonical_url=url,
            provider_request_id="FIXTURE-EXPANSION-TEXT",
            content_hash=hashlib.sha256(text.encode()).hexdigest(),
            text=text,
        )


class MarketCoverageStructuredTransport(FixtureStructuredTransport):
    def __init__(
        self,
        *,
        target_id: str = "005930",
        target_market: str = "KOSPI",
        missing_market: str | None = None,
        target_only_market: str | None = None,
    ) -> None:
        super().__init__()
        self.target_id = target_id
        self.target_market = target_market
        self.missing_market = missing_market
        self.target_only_market = target_only_market

    def get_json(self, *, url, params, headers, timeout_seconds):
        market = (
            "KOSPI"
            if "stk_bydd_trd" in url
            else "KOSDAQ"
            if "ksq_bydd_trd" in url
            else None
        )
        if market is not None:
            del headers, timeout_seconds
            self.calls.append(("json", url, dict(params)))
            if market == self.missing_market:
                payload = {"OutBlock_1": []}
            else:
                rows = [
                    _krx_stock_row(
                        symbol="111111" if market == "KOSPI" else "222222",
                        name=(
                            "Peer Alpha"
                            if market == "KOSPI"
                            else "Peer Beta"
                        ),
                    )
                ]
                if market == self.target_market:
                    rows.insert(
                        0,
                        _krx_stock_row(
                            symbol=self.target_id,
                            name="Current Corp",
                        ),
                    )
                if market == self.target_only_market:
                    rows = [
                        row
                        for row in rows
                        if str(row.get("ISU_CD") or "") == self.target_id
                    ]
                payload = {"OutBlock_1": rows}
            return _json_response(
                url,
                payload,
                request_id=f"FIXTURE-{market}-STOCK",
            )
        if "/idx/" in url:
            del headers, timeout_seconds
            self.calls.append(("json", url, dict(params)))
            market = "KOSDAQ" if "kosdaq" in url else "KOSPI"
            row = {
                **_krx_index_row(params["basDd"]),
                "IDX_NM": "코스닥" if market == "KOSDAQ" else "코스피",
            }
            return _json_response(
                url,
                {"OutBlock_1": [row]},
                request_id=f"FIXTURE-{market}-INDEX",
            )
        return super().get_json(
            url=url,
            params=params,
            headers=headers,
            timeout_seconds=timeout_seconds,
        )


class CacheInvalidationRecordingPeerProvider(FixturePeerProvider):
    def __init__(self):
        super().__init__()
        self.invalidations = []
        self.active_response = False

    def invalidate_last_response_cache(self, reason):
        event = {
            "status": (
                "INVALIDATED"
                if self.active_response
                else "NO_ELIGIBLE_RESPONSE"
            ),
            "reason": reason,
        }
        self.active_response = False
        self.invalidations.append(event)
        return event

    def complete(self, *, pass_name, payload):
        if "peer_selection_retry_context" in payload:
            return super().complete(pass_name=pass_name, payload=payload)
        self.calls.append({"pass_name": pass_name, "payload": payload})
        self.active_response = True
        return {
            "peers": [
                {
                    "peer_symbol": "999999",
                    "peer_name": "Absent Peer",
                    "shared_economic_drivers": ["same earnings cycle"],
                    "material_differences": ["different product mix"],
                    "comparability_rationale": "cycle economics overlap",
                    "confidence": 0.8,
                },
                {
                    "peer_symbol": "222222",
                    "peer_name": "Peer Beta",
                    "shared_economic_drivers": ["same capacity cycle"],
                    "material_differences": ["different customer mix"],
                    "comparability_rationale": "capacity economics overlap",
                    "confidence": 0.8,
                },
            ],
            "selection_complete": True,
            "unresolved_research_notes": [],
            "selection_rationale": "stateful invalid cached proposal",
        }


class InvalidStructuredRetryPeerProvider(FixturePeerProvider):
    def __init__(self):
        super().__init__()
        self.attempt_count = 0
        self.active_response = False
        self.invalidations = []

    def complete(self, *, pass_name, payload):
        self.attempt_count += 1
        self.calls.append({"pass_name": pass_name, "payload": payload})
        self.active_response = True
        pairs = (
            (
                ("333333", "Relabelled Company"),
                ("444444", "Invented Listing Vehicle"),
            )
            if self.attempt_count == 1
            else (
                ("999999", "Absent Peer"),
                ("222222", "Peer Beta"),
            )
        )
        return {
            "peers": [
                {
                    "peer_symbol": symbol,
                    "peer_name": name,
                    "shared_economic_drivers": ["same earnings cycle"],
                    "material_differences": ["different product mix"],
                    "comparability_rationale": "cycle economics overlap",
                    "confidence": 0.8,
                }
                for symbol, name in pairs
            ],
            "selection_complete": True,
            "unresolved_research_notes": [],
            "selection_rationale": "exercise structured retry validation",
        }

    def invalidate_last_response_cache(self, reason):
        event = {
            "status": (
                "INVALIDATED"
                if self.active_response
                else "NO_ELIGIBLE_RESPONSE"
            ),
            "reason": reason,
        }
        self.active_response = False
        self.invalidations.append(event)
        return event


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
        self.assertEqual(payload["INVESTMENT_OPINION_SCORE"], 4)
        self.assertEqual(payload["TARGET_PRC"], 500_000)
        self.assertEqual(payload["EPS"], 46_664)
        self.assertEqual(payload["FORWARD_PER"], 6.11)
        self.assertEqual(payload["CONSENSUS_PROVIDER_COUNT"], 24)
        self.assertEqual(payload["TRAILING_EPS"], 6_564)
        self.assertEqual(payload["TRAILING_BPS"], 63_997)
        self.assertEqual(payload["TRAILING_PER"], 43.42)
        self.assertEqual(payload["TRAILING_PBR"], 4.45)
        self.assertEqual(payload["PROVIDER_PREVIOUS_CLOSE"], 285_000)
        self.assertEqual(
            payload["TRAILING_VALUATION_AS_OF_DATE"], "2026/07/10"
        )
        self.assertTrue(payload["TRAILING_VALUATION_DATE_VERIFIED"])
        self.assertTrue(
            payload["score_anchor_text"].startswith("투자의견 컨센서스")
        )
        self.assertNotIn("og:description", payload["score_anchor_text"])

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
            trailing = {
                row.metric_id: row
                for row in first.engine_result.valuation_records
                if row.record_kind == "PROVIDER_TRAILING_VALUATION_SNAPSHOT"
            }
            self.assertEqual(
                set(trailing),
                {
                    "trailing_eps",
                    "trailing_bps",
                    "trailing_pe",
                    "trailing_pb",
                    "provider_previous_close",
                },
            )
            self.assertEqual(trailing["trailing_pe"].value, 43.42)
            self.assertEqual(trailing["trailing_pb"].value, 4.45)
            self.assertEqual(trailing["provider_previous_close"].value, 285_000)
            self.assertTrue(
                all(
                    row.metadata["metric_namespace"] == "TRAILING_ACTUAL"
                    and row.metadata["forward_value"] is False
                    and row.source_ids
                    for row in trailing.values()
                )
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

    def test_companyguide_report_history_is_bounded_and_hands_off_full_document_candidates(
        self,
    ):
        transport = PaginatedReportStructuredTransport()
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
                companyguide_report_rows=1,
                companyguide_report_max_pages=2,
                companyguide_report_max_candidates=2,
            ).materialize(
                target_id="005930",
                target_name="Current Corp",
                as_of_date="2026-07-12",
                latest_trading_snapshot_date="2026-07-10",
                official=_official(),
                output_root=directory,
                checkpoint_resume=True,
            )

            report_calls = [
                call
                for call in transport.calls
                if "c1080001_data" in call[1]
            ]
            self.assertEqual(
                [call[2]["curPage"] for call in report_calls], [1, 2]
            )
            audit = result.audit["companyguide_report_history"]
            self.assertTrue(audit["bounded_pagination"])
            self.assertEqual(audit["max_pages"], 2)
            self.assertEqual(audit["max_candidates"], 2)
            self.assertEqual(audit["stop_reason"], "MAX_CANDIDATES_REACHED")
            self.assertEqual(audit["fetched_page_count"], 2)
            self.assertEqual(len(result.report_candidates), 2)
            page_two = next(
                row
                for row in result.report_candidates
                if row["provider_page"] == 2
            )
            self.assertEqual(
                page_two["provider_file_name"], "provider_report_page_2.pdf"
            )
            self.assertEqual(page_two["full_document_owner"], "LLM_SOURCE_GRAPH")
            self.assertTrue(page_two["url_resolution_required"])
            self.assertIsNone(page_two["canonical_url"])
            self.assertFalse(page_two["deterministic_url_synthesis"])
            self.assertFalse(page_two["deterministic_query_synthesis"])
            self.assertFalse(page_two["evidence_eligible"])
            handoff_path = (
                Path(directory) / "current_structured_report_candidates.jsonl"
            )
            self.assertTrue(handoff_path.is_file())
            self.assertEqual(
                len(
                    [
                        line
                        for line in handoff_path.read_text(
                            encoding="utf-8"
                        ).splitlines()
                        if line.strip()
                    ]
                ),
                2,
            )

    def test_companyguide_report_page_overlap_is_deduped_before_engine_compile(
        self,
    ):
        transport = OverlappingPaginatedReportStructuredTransport()
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
                companyguide_report_rows=1,
                companyguide_report_max_pages=2,
                companyguide_report_max_candidates=2,
            ).materialize(
                target_id="005930",
                target_name="Current Corp",
                as_of_date="2026-07-12",
                latest_trading_snapshot_date="2026-07-10",
                official=_official(),
                output_root=directory,
                checkpoint_resume=True,
            )

            audit = result.audit["companyguide_report_history"]
            self.assertEqual(audit["selected_candidate_count"], 2)
            self.assertEqual(audit["eligible_report_count"], 1)
            self.assertEqual(audit["duplicate_report_count"], 1)
            self.assertEqual(len(result.report_candidates), 1)
            report_record_ids = [
                row.record_id
                for row in result.engine_result.records
                if row.record_kind == "STRUCTURED_BROKER_REPORT_DIRECTION"
            ]
            self.assertEqual(
                len(report_record_ids), len(set(report_record_ids))
            )

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

    def test_same_lane_cache_prefers_pre_cutoff_companyguide_snapshot(self):
        url = "https://comp.wisereport.co.kr/company/c1010001.aspx"
        with tempfile.TemporaryDirectory() as directory:
            lane = Path(directory)
            source_cache = lane / "SOURCE" / "structured_source_cache"
            target_cache = lane / "TARGET" / "structured_source_cache"
            source_cache.mkdir(parents=True)
            target_cache.mkdir(parents=True)
            pre_cutoff = _companyguide_html("2026.07.10")
            future = _companyguide_html("2026.07.13")
            _write_legacy_text_cache(
                source_cache / "companyguide_snapshot_005930.json",
                url=url,
                text=pre_cutoff,
            )
            _write_legacy_text_cache(
                target_cache / "companyguide_peer_snapshot_005930.json",
                url=url,
                text=future,
            )
            _write_legacy_text_cache(
                target_cache / "companyguide_peer_snapshot_111111.json",
                url=url,
                text=future,
            )
            fetch_calls = []
            response, cache_hit, error = CurrentStructuredSourceMaterializer()._response(
                cache_key="companyguide_peer_snapshot_005930",
                cache_root=target_cache,
                checkpoint_resume=True,
                response_kind="text",
                request_url=url,
                request_params={"cmp_cd": "005930", "cn": ""},
                fetch=lambda: fetch_calls.append("unexpected"),
                shared_cache_roots=(source_cache,),
                shared_cache_keys=(
                    "companyguide_peer_snapshot_005930",
                    "companyguide_snapshot_005930",
                ),
                cached_response_validator=lambda value: (
                    structured_materializer_module._companyguide_cached_snapshot_is_point_in_time(
                        value,
                        cutoff=date(2026, 7, 12),
                    )
                ),
            )
            self.assertTrue(cache_hit)
            self.assertIsNone(error)
            self.assertEqual(fetch_calls, [])
            self.assertEqual(response.text, pre_cutoff)
            self.assertFalse(
                structured_materializer_module._companyguide_cached_snapshot_is_point_in_time(
                    response,
                    cutoff=date(2026, 7, 12),
                    expected_company_name="A Different Company",
                )
            )
            persisted = json.loads(
                (
                    target_cache / "companyguide_peer_snapshot_005930.json"
                ).read_text(encoding="utf-8")
            )
            self.assertEqual(
                persisted["schema_version"],
                "e2r_v5_current_structured_cache_v2",
            )
            self.assertTrue(persisted["shared_cache_reuse"])
            self.assertEqual(
                persisted["shared_cache_source_content_hash"],
                response.content_hash,
            )
            available = (
                structured_materializer_module._point_in_time_peer_identity_roster(
                    (
                        {"peer_symbol": "005930", "peer_name": "Current Corp"},
                        {"peer_symbol": "111111", "peer_name": "Current Corp"},
                    ),
                    cutoff=date(2026, 7, 12),
                    cache_roots=(target_cache, source_cache),
                )
            )
            self.assertEqual(
                available,
                (
                    {
                        "peer_symbol": "005930",
                        "peer_name": "Current Corp",
                        "point_in_time_snapshot_available": "YES",
                    },
                ),
            )

    def test_cached_point_in_time_roster_is_hint_not_exclusive_allowlist(self):
        transport = ExpansionFixtureStructuredTransport()
        peer_provider = ExpansionPeerProvider()
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
            cache = Path(directory) / "structured_source_cache"
            cache.mkdir(parents=True)
            for symbol, name, per, pbr in (
                ("111111", "Peer Alpha", 8.0, "N/A"),
                ("222222", "Peer Beta", "N/A", 2.2),
            ):
                _write_legacy_text_cache(
                    cache / f"companyguide_peer_snapshot_{symbol}.json",
                    url="https://comp.wisereport.co.kr/company/c1010001.aspx",
                    text=_companyguide_html(
                        "2026.07.10",
                        company_name=name,
                        forward_per=per,
                        forward_pbr=pbr,
                        forward_ev_ebitda="N/A",
                    ),
                )
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

        payload = peer_provider.calls[0]["payload"]
        self.assertEqual(
            {
                row["peer_symbol"]
                for row in payload[
                    "point_in_time_structured_peer_identity_roster"
                ]
            },
            {"111111", "222222"},
        )
        self.assertTrue(
            payload["point_in_time_peer_roster_accounting"][
                "availability_hint_only_not_peer_allowlist"
            ]
        )
        self.assertEqual(len(peer_provider.calls), 2)
        retry_payload = peer_provider.calls[1]["payload"]
        self.assertIn("peer_selection_retry_context", retry_payload)
        self.assertEqual(
            {
                row["peer_symbol"]
                for row in retry_payload[
                    "authoritative_listing_identity_roster"
                ]
            },
            {"111111", "222222", "555555", "666666"},
        )
        self.assertTrue(
            result.audit["peer_selection"][
                "structured_verification_retry_used"
            ]
        )
        self.assertEqual(
            {
                row["peer_symbol"]
                for row in result.audit["peer_selection"]["selected_peers"]
            },
            {"555555", "666666"},
        )
        self.assertEqual(
            result.audit["peer_selection"]["status"],
            "PEER_SELECTION_COMPLETE",
        )
        self.assertNotIn(
            "point_in_time_structured_peer_identity_roster_is_allowlist",
            retry_payload["selection_constraints"],
        )
        self.assertNotIn(
            (
                "when_two_or_more_point_in_time_identities_are_available_"
                "select_only_from_point_in_time_structured_peer_identity_roster"
            ),
            retry_payload["selection_constraints"],
        )
        self.assertNotIn(
            "when_two_or_more_available_select_only_from_this_roster",
            retry_payload["point_in_time_peer_roster_accounting"],
        )

    def test_peer_identity_must_match_authoritative_krx_pair(self):
        response = FixturePeerProvider().complete(
            pass_name="STRUCTURED_PEER_SELECTION",
            payload={},
        )
        tampered = json.loads(json.dumps(response))
        tampered["peers"][0]["peer_name"] = "Wrong Legal Name"
        with self.assertRaisesRegex(
            ValueError,
            "mismatches authoritative listing roster",
        ):
            structured_materializer_module._validated_peer_proposals(
                tampered,
                target_id="005930",
                authoritative_listing_identity_roster=(
                    {"peer_symbol": "111111", "peer_name": "Peer Alpha"},
                    {"peer_symbol": "222222", "peer_name": "Peer Beta"},
                ),
            )

    def test_krx_market_identity_rosters_merge_and_drop_conflicts(self):
        merged = structured_materializer_module._merge_listing_identity_rosters(
            (
                {"peer_symbol": "111111", "peer_name": "KOSPI Peer"},
                {"peer_symbol": "222222", "peer_name": "KOSDAQ Peer"},
                {"peer_symbol": "333333", "peer_name": "First Name"},
                {"peer_symbol": "333333", "peer_name": "Conflicting Name"},
            )
        )
        self.assertEqual(
            merged,
            (
                {"peer_symbol": "111111", "peer_name": "KOSPI Peer"},
                {"peer_symbol": "222222", "peer_name": "KOSDAQ Peer"},
            ),
        )

    def test_kospi_and_kosdaq_rosters_are_both_required_and_merged(self):
        transport = MarketCoverageStructuredTransport()
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

        provider_roster = peer_provider.calls[0]["payload"][
            "authoritative_listing_identity_roster"
        ]
        self.assertEqual(
            provider_roster,
            [
                {"peer_symbol": "111111", "peer_name": "Peer Alpha"},
                {"peer_symbol": "222222", "peer_name": "Peer Beta"},
            ],
        )
        roster_audit = result.audit["peer_selection"][
            "listing_identity_roster"
        ]
        self.assertTrue(roster_audit["all_required_markets_complete"])
        self.assertEqual(
            roster_audit["complete_markets"],
            ["KOSPI", "KOSDAQ"],
        )
        self.assertEqual(
            roster_audit["market_details"]["KOSPI"]["identity_count"],
            1,
        )
        self.assertEqual(
            roster_audit["market_details"]["KOSDAQ"]["identity_count"],
            1,
        )

    def test_missing_one_krx_market_fails_closed_before_peer_provider(self):
        transport = MarketCoverageStructuredTransport(
            missing_market="KOSDAQ"
        )
        peer_provider = FixturePeerProvider()
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
            )

        self.assertEqual(peer_provider.calls, [])
        peer_audit = result.audit["peer_selection"]
        self.assertEqual(
            peer_audit["pending_reason"],
            "AUTHORITATIVE_LISTING_ROSTER_INCOMPLETE",
        )
        self.assertFalse(
            peer_audit["listing_identity_roster"][
                "all_required_markets_complete"
            ]
        )
        self.assertEqual(
            peer_audit["listing_identity_roster"]["incomplete_markets"],
            ["KOSDAQ"],
        )
        self.assertIn(
            (
                "PEER_SELECTION_PENDING:"
                "AUTHORITATIVE_LISTING_ROSTER_INCOMPLETE"
            ),
            result.pending_reasons,
        )

    def test_target_only_market_row_is_not_a_complete_identity_plane(self):
        transport = MarketCoverageStructuredTransport(
            target_only_market="KOSPI"
        )
        peer_provider = FixturePeerProvider()
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
            )

        self.assertEqual(peer_provider.calls, [])
        peer_audit = result.audit["peer_selection"]
        self.assertEqual(
            peer_audit["pending_reason"],
            "AUTHORITATIVE_LISTING_ROSTER_INCOMPLETE",
        )
        kospi_audit = peer_audit["listing_identity_roster"][
            "market_details"
        ]["KOSPI"]
        self.assertEqual(kospi_audit["exact_snapshot_row_count"], 1)
        self.assertEqual(kospi_audit["target_row_count"], 1)
        self.assertEqual(kospi_audit["identity_count"], 0)
        self.assertFalse(kospi_audit["complete_identity_plane"])
        self.assertEqual(kospi_audit["status"], "IDENTITY_PLANE_INCOMPLETE")

    def test_kosdaq_target_uses_kosdaq_price_and_benchmark_lineage_only(self):
        transport = MarketCoverageStructuredTransport(
            target_id="000660",
            target_market="KOSDAQ",
        )
        attempts = []
        manifests = []
        with tempfile.TemporaryDirectory() as directory, patch.dict(
            os.environ,
            {
                "KRX_OPENAPI_KEY": "KRX-SECRET-FIXTURE",
                "DATA_GO_KR_SERVICE_KEY": "DATA-SECRET-FIXTURE",
            },
            clear=False,
        ):
            route, _, roster_audit, peer_price_rows = (
                CurrentStructuredSourceMaterializer(
                    transport=transport,
                    price_lookback_days=400,
                )._price_route(
                    target_id="000660",
                    cutoff=date(2026, 7, 12),
                    trading_date=date(2026, 7, 10),
                    cache_root=Path(directory),
                    checkpoint_resume=True,
                    attempts=attempts,
                    manifests=manifests,
                )
            )

        self.assertEqual(route.payload.diagnostics["market"], "KOSDAQ")
        self.assertTrue(roster_audit["all_required_markets_complete"])
        self.assertTrue(peer_price_rows)
        kospi_stock_source = roster_audit["market_details"]["KOSPI"][
            "source_id"
        ]
        kosdaq_stock_source = roster_audit["market_details"]["KOSDAQ"][
            "source_id"
        ]
        self.assertNotIn(kospi_stock_source, route.payload.source_ids)
        self.assertIn(kosdaq_stock_source, route.payload.source_ids)
        kosdaq_index_sources = {
            row["source_id"]
            for row in manifests
            if row["canonical_url"]
            == structured_materializer_module._KRX_INDEX_URLS["KOSDAQ"]
        }
        self.assertTrue(kosdaq_index_sources)
        self.assertTrue(
            kosdaq_index_sources.issubset(set(route.payload.source_ids))
        )
        self.assertFalse(
            {
                row["source_id"]
                for row in manifests
                if row["canonical_url"]
                == structured_materializer_module._KRX_INDEX_URLS["KOSPI"]
            }
            & set(route.payload.source_ids)
        )

    def test_invalid_cached_peer_membership_is_quarantined_then_retried(self):
        transport = FixtureStructuredTransport()
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
            initial_materializer = CurrentStructuredSourceMaterializer(
                transport=transport,
                price_lookback_days=400,
                peer_provider=FixturePeerProvider(),
            )
            for _ in range(2):
                initial_materializer.materialize(
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
            selection_cache_path = (
                Path(directory)
                / "structured_source_cache"
                / "peer_selection_005930.json"
            )
            cached = json.loads(
                selection_cache_path.read_text(encoding="utf-8")
            )
            cached["response"]["peers"][0]["peer_symbol"] = "999999"
            cached["response"]["peers"][0]["peer_name"] = "Absent Peer"
            cached["provider_response_hash"] = (
                structured_materializer_module.stable_hash(
                    cached["response"]
                )
            )
            selection_cache_path.write_text(
                json.dumps(
                    cached,
                    ensure_ascii=False,
                    sort_keys=True,
                )
                + "\n",
                encoding="utf-8",
            )
            peer_provider = CacheInvalidationRecordingPeerProvider()
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
        self.assertEqual(audit["status"], "PEER_SELECTION_COMPLETE")
        self.assertTrue(audit["rejected_provider_cache_hit"])
        self.assertTrue(audit["validation_retry_used"])
        self.assertEqual(len(peer_provider.calls), 2)
        self.assertEqual(len(peer_provider.invalidations), 2)
        self.assertEqual(
            [row["status"] for row in peer_provider.invalidations],
            ["NO_ELIGIBLE_RESPONSE", "INVALIDATED"],
        )
        self.assertIn(
            "absent from authoritative listing roster",
            peer_provider.invalidations[1]["reason"],
        )
        self.assertEqual(
            [
                row["status"]
                for row in audit["provider_response_cache_invalidations"]
            ],
            ["NO_ELIGIBLE_RESPONSE", "INVALIDATED"],
        )
        self.assertTrue(
            audit["selection_route_cache_invalidations"][0][
                "cache_entry_deleted"
            ]
        )

    def test_shared_cache_request_fingerprint_blocks_other_symbol(self):
        url = "https://comp.wisereport.co.kr/company/c1010001.aspx"
        with tempfile.TemporaryDirectory() as directory:
            lane = Path(directory)
            source_cache = lane / "SOURCE" / "structured_source_cache"
            target_cache = lane / "TARGET" / "structured_source_cache"
            source_cache.mkdir(parents=True)
            source_text = _companyguide_html("2026.07.10")
            target_text = _companyguide_html("2026.07.11")
            materializer = CurrentStructuredSourceMaterializer()
            materializer._response(
                cache_key="companyguide_snapshot_005930",
                cache_root=source_cache,
                checkpoint_resume=True,
                response_kind="text",
                request_url=url,
                request_params={
                    "cmp_cd": "005930",
                    "serviceKey": "SHOULD-NOT-BE-PERSISTED",
                },
                fetch=lambda: _text_response(url, source_text),
            )
            fetch_calls = []

            def fetch_target():
                fetch_calls.append("called")
                return _text_response(url, target_text)

            response, cache_hit, error = materializer._response(
                cache_key="companyguide_snapshot_000660",
                cache_root=target_cache,
                checkpoint_resume=True,
                response_kind="text",
                request_url=url,
                request_params={
                    "cmp_cd": "000660",
                    "serviceKey": "A-DIFFERENT-SECRET",
                },
                fetch=fetch_target,
                shared_cache_roots=(source_cache,),
                shared_cache_keys=("companyguide_snapshot_005930",),
            )
            self.assertFalse(cache_hit)
            self.assertIsNone(error)
            self.assertEqual(fetch_calls, ["called"])
            self.assertEqual(response.text, target_text)
            cache_text = "\n".join(
                path.read_text(encoding="utf-8")
                for path in lane.rglob("*.json")
            )
            self.assertNotIn("SHOULD-NOT-BE-PERSISTED", cache_text)
            self.assertNotIn("A-DIFFERENT-SECRET", cache_text)

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
                required_roles_by_component={
                    "eps_fcf_explosion": ("FORWARD_GUIDANCE",),
                    "valuation_rerating": ("DURABLE_VISIBILITY",),
                },
            )
        self.assertIn(
            "FORWARD_GUIDANCE",
            result.engine_result.missing_roles_by_component["eps_fcf_explosion"],
        )
        self.assertIn(
            "DURABLE_VISIBILITY",
            result.engine_result.missing_roles_by_component[
                "valuation_rerating"
            ],
        )
        self.assertEqual(
            result.audit["required_roles_by_component"]["valuation_rerating"],
            ["DURABLE_VISIBILITY"],
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
            stabilized = CurrentStructuredSourceMaterializer(
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
        self.assertEqual(len(peer_provider.calls), 2)
        provider_payload = json.dumps(peer_provider.calls[0]["payload"], sort_keys=True)
        self.assertNotIn("suggested_queries", provider_payload)
        fact_profile = peer_provider.calls[0]["payload"]["current_evidence_facts"]
        claim_profile = peer_provider.calls[0]["payload"][
            "source_backed_claim_context"
        ]
        self.assertEqual(fact_profile["collection_name"], "peer_selection_evidence_facts")
        self.assertEqual(claim_profile["collection_name"], "peer_selection_source_claims")
        self.assertTrue(
            peer_provider.calls[0]["payload"][
                "peer_selection_context_accounting"
            ]["every_fact_and_claim_accounted_by_hash_and_group_count"]
        )
        self.assertFalse(
            peer_provider.calls[0]["payload"][
                "peer_selection_context_accounting"
            ]["fixed_top_n_used"]
        )
        self.assertFalse(
            peer_provider.calls[0]["payload"]["selection_constraints"][
                "score_or_stage_authority"
            ]
        )
        self.assertEqual(
            peer_provider.calls[0]["payload"][
                "authoritative_listing_identity_roster"
            ],
            [
                {"peer_symbol": "111111", "peer_name": "Peer Alpha"},
                {"peer_symbol": "222222", "peer_name": "Peer Beta"},
                {
                    "peer_symbol": "333333",
                    "peer_name": "Relabelled Company",
                },
                {
                    "peer_symbol": "444444",
                    "peer_name": "Invented Listing Vehicle",
                },
            ],
        )
        self.assertTrue(
            peer_provider.calls[0]["payload"][
                "listing_identity_roster_accounting"
            ]["complete_market_snapshot_used_without_top_n"]
        )
        self.assertNotIn("current_score", provider_payload.casefold())
        self.assertNotIn("current_stage", provider_payload.casefold())
        peer_audit = result.audit["peer_selection"]
        self.assertEqual(peer_audit["status"], "PEER_SELECTION_COMPLETE")
        self.assertEqual(peer_audit["verified_peer_count"], 2)
        self.assertFalse(resumed.audit["peer_selection"]["provider_cache_hit"])
        self.assertTrue(stabilized.audit["peer_selection"]["provider_cache_hit"])
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

    def test_official_equity_and_krx_market_cap_close_empty_peer_snapshot(self):
        transport = HistoricalReportFallbackStructuredTransport()
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
            corp_code_root = Path(directory) / "corp_code_archives"
            _write_corp_code_archive(
                corp_code_root / "2099-01-01" / "corpCode.zip",
                (
                    ("00000011", "Peer Alpha", "111111", "20260101"),
                    ("00000022", "Peer Beta", "222222", "20260101"),
                ),
            )
            materializer = CurrentStructuredSourceMaterializer(
                transport=transport,
                price_lookback_days=400,
                peer_provider=peer_provider,
                opendart_corp_code_cache_root=corp_code_root,
            )
            result = materializer.materialize(
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
        self.assertEqual(audit["status"], "PEER_SELECTION_COMPLETE")
        self.assertEqual(
            audit["common_metric_peer_counts"]["trailing_parent_pb"], 2
        )
        self.assertEqual(
            audit["structured_fetch_stop_condition"],
            "COMMON_PEER_MULTIPLE_RESOLVED",
        )
        self.assertEqual(
            {row["status"] for row in audit["official_trailing_pb_fallbacks"]},
            {"RESOLVED"},
        )
        self.assertTrue(
            all(
                row["evidence_fact_count_added"] == 0
                and row["report_pdf_fetch_count"] == 0
                for row in audit["official_trailing_pb_fallbacks"]
            )
        )
        peer_inputs = [
            row
            for row in result.engine_result.records
            if row.metric_id == "peer_trailing_parent_pb"
        ]
        self.assertEqual(len(peer_inputs), 2)
        self.assertEqual({round(float(row.value), 2) for row in peer_inputs}, {1.21})
        self.assertTrue(
            all(
                row.metadata["valuation_source"]
                == "KRX_MARKET_CAP_X_OPENDART_PARENT_EQUITY"
                and row.observed_at == "2026-07-10"
                and row.metadata["dart_report_code"] == "11013"
                and row.metadata["dart_period_end"] == "2026-03-31"
                and row.metadata["rcept_date"] == "2026-05-15"
                and len(row.source_ids) == 4
                and row.metadata["filing_period_confirmation"]["period_end"]
                == "2026-03-31"
                for row in peer_inputs
            )
        )
        self.assertFalse(
            any(
                row.status == "FUTURE_REJECTED"
                for row in result.fetch_attempts
            )
        )
        corp_code_manifests = [
            row
            for row in result.payload_manifest
            if str(row["source_role"]).startswith("PEER_CORP_CODE_DIRECTORY:")
        ]
        self.assertEqual(len(corp_code_manifests), 2)
        self.assertTrue(
            all(
                row["effective_date"] is None
                and row["production_score_authority"] is False
                for row in corp_code_manifests
            )
        )
        self.assertTrue(
            all(
                row["corp_code_resolution"]["archive_directory_label"]
                == "2099-01-01"
                and row["corp_code_resolution"][
                    "folder_date_used_as_source_availability"
                ]
                is False
                for row in audit["official_trailing_pb_fallbacks"]
            )
        )

    def test_corp_code_bridge_fails_closed_on_modify_date_and_archive_budget(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "archives"
            # The newest three archives are the entire configured budget.  A
            # valid fourth archive must not be reached implicitly.
            for folder, modify_date in (
                ("2099-04-01", ""),
                ("2099-03-01", "20260713"),
                ("2099-02-01", ""),
                ("2099-01-01", "20260101"),
            ):
                _write_corp_code_archive(
                    root / folder / "corpCode.zip",
                    (("00000011", "Peer Alpha", "111111", modify_date),),
                )
            attempts = []
            manifests = []
            corp_code, source_id, audit = CurrentStructuredSourceMaterializer(
                transport=HistoricalReportFallbackStructuredTransport(),
                opendart_corp_code_cache_root=root,
                opendart_corp_code_max_archives=3,
            )._peer_corp_code_from_archived_directory(
                target_id="005930",
                cutoff=date(2026, 7, 12),
                symbol="111111",
                company_name="Peer Alpha",
                cache_root=Path(directory) / "target_cache",
                attempts=attempts,
                manifests=manifests,
            )

        self.assertIsNone(corp_code)
        self.assertIsNone(source_id)
        self.assertEqual(audit["archive_candidate_count"], 4)
        self.assertEqual(audit["parsed_archive_count"], 3)
        self.assertEqual(audit["maximum_archive_candidates"], 3)
        self.assertEqual(
            audit["stop_condition"], "ARCHIVE_CANDIDATE_BUDGET_EXHAUSTED"
        )
        self.assertEqual(attempts, [])
        self.assertEqual(manifests, [])

    def test_peer_equity_only_013_falls_back_to_older_statement(self):
        for first_status, older_expected in (
            ("013", True),
            ("999", False),
            ("PROVIDER_ERROR", False),
        ):
            with self.subTest(first_status=first_status):
                transport = HistoricalReportFallbackStructuredTransport(
                    peer_dart_status_by_report_code={"11013": first_status}
                )
                result = self._materialize_official_peer_fallback(
                    transport=transport
                )
                peer_dart_calls = [
                    row[2]
                    for row in transport.calls
                    if row[0] == "json"
                    and "fnlttSinglAcntAll" in row[1]
                    and str(row[2].get("corp_code"))
                    in {"00000011", "00000022"}
                ]
                has_older_call = any(
                    str(row.get("reprt_code")) == "11011"
                    for row in peer_dart_calls
                )
                self.assertEqual(has_older_call, older_expected)
                audit = result.audit["peer_selection"]
                if older_expected:
                    self.assertEqual(audit["status"], "PEER_SELECTION_COMPLETE")
                else:
                    self.assertNotEqual(
                        audit["status"], "PEER_SELECTION_COMPLETE"
                    )

    def test_multiple_listed_equity_lines_block_parent_pb_scope_mismatch(self):
        materializer = CurrentStructuredSourceMaterializer(
            transport=HistoricalReportFallbackStructuredTransport()
        )
        attempts = []
        manifests = []
        with patch.dict(
            os.environ,
            {"OPENDART_API_KEY": "DART-SECRET-FIXTURE"},
            clear=False,
        ), patch.object(
            materializer,
            "_peer_corp_code_from_archived_directory",
        ) as resolver:
            observation, audit = (
                materializer._peer_official_trailing_pb_observation(
                    target_id="005930",
                    cutoff=date(2026, 7, 12),
                    listing_snapshot_date=date(2026, 7, 10),
                    proposal={
                        "peer_symbol": "111111",
                        "peer_name": "Peer Alpha",
                        "confidence": 0.9,
                        "comparability_rationale": ("same business",),
                        "material_differences": (),
                    },
                    peer_price_rows=(
                        {
                            "peer_symbol": "111111",
                            "peer_name": "Peer Alpha",
                            "observed_at": "2026-07-10",
                            "market_cap": 1_210_000_000,
                            "source_id": "KRX-SOURCE",
                            "listed_equity_line_count": 2,
                        },
                    ),
                    cache_root=Path("unused"),
                    checkpoint_resume=True,
                    attempts=attempts,
                    manifests=manifests,
                    snapshot_failure="CONSENSUS_PAYLOAD_UNAVAILABLE",
                )
            )

        self.assertIsNone(observation)
        self.assertEqual(
            audit["failure_reason"],
            "MULTIPLE_LISTED_EQUITY_LINES_REQUIRE_SCOPE_MATCHING",
        )
        resolver.assert_not_called()
        self.assertEqual(attempts, [])
        self.assertEqual(manifests, [])

    def test_krx_common_and_preferred_rows_reach_scope_mismatch_block(self):
        transport = MultipleEquityLineStructuredTransport()
        result = self._materialize_official_peer_fallback(transport=transport)
        audit = result.audit["peer_selection"]
        alpha = next(
            row
            for row in audit["official_trailing_pb_fallbacks"]
            if row["peer_symbol"] == "111111"
        )
        self.assertEqual(
            alpha["failure_reason"],
            "MULTIPLE_LISTED_EQUITY_LINES_REQUIRE_SCOPE_MATCHING",
        )
        self.assertNotEqual(audit["status"], "PEER_SELECTION_COMPLETE")
        alpha_dart_calls = [
            row
            for row in transport.calls
            if row[0] == "json"
            and str(row[2].get("corp_code")) == "00000011"
        ]
        self.assertEqual(alpha_dart_calls, [])

    def _materialize_official_peer_fallback(self, *, transport):
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
            materializer = CurrentStructuredSourceMaterializer(
                transport=transport,
                price_lookback_days=400,
                peer_provider=peer_provider,
            )
            with patch.object(
                materializer,
                "_peer_corp_code_from_archived_directory",
                side_effect=lambda **kwargs: (
                    {
                        "111111": "00000011",
                        "222222": "00000022",
                    }.get(kwargs["symbol"]),
                    f"CORPSRC-{kwargs['symbol']}",
                    {"status": "RESOLVED", "failure_reason": None},
                ),
            ):
                return materializer.materialize(
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

    def test_parent_equity_requires_exact_identity_period_currency_and_cutoff(self):
        base = {
            **_dart_row(
                "BS",
                "지배기업의 소유주에게 귀속되는 자본",
                1_000_000_000,
            ),
            "account_id": "ifrs-full_EquityAttributableToOwnersOfParent",
            "corp_code": "00000011",
            "bsns_year": "2026",
            "reprt_code": "11013",
            "currency": "KRW",
            "rcept_no": "20260515000001",
        }
        value, audit = structured_materializer_module._opendart_parent_equity(
            {"status": "000", "list": [base]},
            cutoff=date(2026, 7, 12),
            expected_corp_code="00000011",
            expected_fiscal_year=2026,
            expected_report_code="11013",
        )
        self.assertEqual(value, 1_000_000_000)
        self.assertEqual(audit["rcept_date"], "2026-05-15")

        for field, invalid in (
            ("corp_code", "99999999"),
            ("bsns_year", "2099"),
            ("reprt_code", "11011"),
            ("currency", "USD"),
            ("rcept_no", "20260713000001"),
        ):
            bad = {**base, field: invalid}
            rejected, rejected_audit = (
                structured_materializer_module._opendart_parent_equity(
                    {"status": "000", "list": [bad]},
                    cutoff=date(2026, 7, 12),
                    expected_corp_code="00000011",
                    expected_fiscal_year=2026,
                    expected_report_code="11013",
                )
            )
            self.assertIsNone(rejected, field)
            self.assertEqual(rejected_audit["status"], "PARENT_EQUITY_ROW_MISSING")

        rejected, rejected_audit = (
            structured_materializer_module._opendart_filing_period_end(
                {
                    "status": "000",
                    "list": [
                        {
                            "corp_code": "00000011",
                            "rcept_no": "20260415000001",
                            "rcept_dt": "20260415",
                            "report_nm": "분기보고서 (2026.02)",
                        }
                    ],
                },
                cutoff=date(2026, 7, 12),
                expected_corp_code="00000011",
                expected_rcept_no="20260415000001",
                expected_report_code="11013",
                expected_period_end=date(2026, 3, 31),
            )
        )
        self.assertIsNone(rejected)
        self.assertEqual(
            rejected_audit["rejected_reasons"],
            {"FILING_PERIOD_END_MISMATCH": 1},
        )

        mismatched_receipt, mismatch_audit = (
            structured_materializer_module._opendart_filing_period_end(
                {
                    "status": "000",
                    "list": [
                        {
                            "corp_code": "00000011",
                            "rcept_no": "20260515000001",
                            "rcept_dt": "20260401",
                            "report_nm": "분기보고서 (2026.03)",
                        }
                    ],
                },
                cutoff=date(2026, 7, 12),
                expected_corp_code="00000011",
                expected_rcept_no="20260515000001",
                expected_report_code="11013",
                expected_period_end=date(2026, 3, 31),
            )
        )
        self.assertIsNone(mismatched_receipt)
        self.assertEqual(
            mismatch_audit["rejected_reasons"],
            {"RECEIPT_DATE_MISMATCH": 1},
        )

    def test_balance_sheet_fallback_calendar_keeps_prior_q3_in_early_year(self):
        periods = structured_materializer_module._latest_balance_sheet_periods(
            date(2026, 1, 15), maximum=2
        )
        self.assertEqual(
            [
                (row["fiscal_year"], row["report_code"])
                for row in periods
            ],
            [(2025, "11014"), (2025, "11012")],
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

    def test_clean_resume_consumes_validated_peer_retry_after_primary_wait(self):
        transport = FixtureStructuredTransport()
        peer_provider = CleanResumePeerRetryProvider()
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
        self.assertEqual(audit["status"], "PEER_SELECTION_COMPLETE")
        self.assertEqual(audit["provider_attempt_count"], 2)
        self.assertTrue(audit["validation_retry_used"])
        self.assertIsNone(audit["pending_reason"])
        self.assertNotIn(
            "peer_selection_retry_context",
            peer_provider.calls[0]["payload"],
        )
        self.assertIn(
            "peer_selection_retry_context",
            peer_provider.calls[1]["payload"],
        )

    def test_peer_page_verification_failures_are_fed_back_and_cache_replaced(self):
        transport = FixtureStructuredTransport()
        peer_provider = VerificationFailureThenCompletePeerProvider()
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

            cache = json.loads(
                (
                    Path(directory)
                    / "structured_source_cache"
                    / "peer_selection_005930.json"
                ).read_text(encoding="utf-8")
            )

        audit = result.audit["peer_selection"]
        self.assertEqual(peer_provider.attempt_count, 2)
        self.assertEqual(audit["status"], "PEER_SELECTION_COMPLETE")
        self.assertEqual(audit["provider_attempt_count"], 2)
        self.assertTrue(audit["structured_verification_retry_used"])
        self.assertIn(
            "333333:COMPANY_IDENTITY_MISMATCH",
            audit["initial_proposal_failures"],
        )
        retry = peer_provider.calls[-1]["payload"][
            "peer_selection_retry_context"
        ]
        self.assertTrue(
            any(
                "COMPANY_IDENTITY_MISMATCH" in reason
                for reason in retry["proposal_failures"]
            )
        )
        self.assertEqual(
            {row["peer_symbol"] for row in cache["response"]["peers"]},
            {"111111", "222222"},
        )

    def test_invalid_structured_retry_response_is_quarantined_and_not_cached(self):
        transport = FixtureStructuredTransport()
        peer_provider = InvalidStructuredRetryPeerProvider()
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
            selection_cache_exists = (
                Path(directory)
                / "structured_source_cache"
                / "peer_selection_005930.json"
            ).exists()

        audit = result.audit["peer_selection"]
        self.assertEqual(audit["status"], "PEER_SELECTION_PENDING")
        self.assertTrue(audit["structured_verification_retry_used"])
        self.assertIn(
            "PEER_SELECTION_VERIFICATION_RETRY_ERROR",
            audit["pending_reason"],
        )
        self.assertEqual(peer_provider.attempt_count, 2)
        self.assertEqual(
            [row["status"] for row in peer_provider.invalidations],
            ["INVALIDATED"],
        )
        self.assertIn(
            "absent from authoritative listing roster",
            peer_provider.invalidations[0]["reason"],
        )
        self.assertFalse(selection_cache_exists)
        self.assertTrue(
            audit["selection_route_cache_invalidations"][0][
                "cache_entry_deleted"
            ]
        )

    def test_repeated_source_invalid_peer_response_is_not_reusable_cache(self):
        transport = FixtureStructuredTransport()
        peer_provider = RepeatedVerificationFailurePeerProvider()
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
            first = CurrentStructuredSourceMaterializer(
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
            selection_cache_path = (
                Path(directory)
                / "structured_source_cache"
                / "peer_selection_005930.json"
            )
            selection_cache_exists_after_first = selection_cache_path.exists()
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

        first_audit = first.audit["peer_selection"]
        self.assertEqual(first_audit["status"], "PEER_SELECTION_PENDING")
        self.assertEqual(
            first_audit["provider_response_cache_invalidation"]["status"],
            "INVALIDATED",
        )
        self.assertIn(
            "COMPANY_IDENTITY_MISMATCH",
            peer_provider.invalidations[0]["reason"],
        )
        self.assertFalse(selection_cache_exists_after_first)
        self.assertTrue(
            first_audit["selection_route_cache_invalidation"][
                "cache_entry_deleted"
            ]
        )
        self.assertEqual(peer_provider.attempt_count, 3)
        self.assertEqual(
            resumed.audit["peer_selection"]["status"],
            "PEER_SELECTION_COMPLETE",
        )


def _text_response(url: str, text: str) -> StructuredHTTPResponse:
    content_hash = hashlib.sha256(text.encode()).hexdigest()
    return StructuredHTTPResponse(
        status_code=200,
        canonical_url=url,
        provider_request_id=f"FIXTURE-{content_hash[:20]}",
        content_hash=content_hash,
        text=text,
    )


def _json_response(
    url: str,
    payload,
    *,
    request_id: str,
) -> StructuredHTTPResponse:
    raw = json.dumps(payload, ensure_ascii=False, sort_keys=True).encode()
    return StructuredHTTPResponse(
        status_code=200,
        canonical_url=url,
        provider_request_id=request_id,
        content_hash=hashlib.sha256(raw).hexdigest(),
        payload=payload,
    )


def _write_legacy_text_cache(path: Path, *, url: str, text: str) -> None:
    response = _text_response(url, text)
    path.write_text(
        json.dumps(
            {
                "schema_version": "e2r_v5_current_structured_cache_v1",
                "status_code": response.status_code,
                "canonical_url": response.canonical_url,
                "provider_request_id": response.provider_request_id,
                "content_hash": response.content_hash,
                "payload": None,
                "text": response.text,
                "cache_value_hash": hashlib.sha256(text.encode()).hexdigest(),
            },
            ensure_ascii=False,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )


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
    <meta property="og:description" content="투자의견 컨센서스 및 재무정보">
    <table id="metadata-noise"><tbody><tr>
      <td>9.9</td><td>999,999</td><td>99,999</td><td>99.9</td><td>99</td>
    </tr></tbody></table>
    <p>[기준:{page_date}]</p>
    <ul class="company-header">
      <li><p>EPS<b>6,564</b></p></li>
      <li><p>BPS<b>63,997</b></p></li>
      <li><p>PER<b>43.42</b></p></li>
      <li><p>업종PER<b>36.34</b></p></li>
      <li><p>PBR<b>4.45</b></p></li>
      <li><p>전일종가<b>285,000</b></p></li>
    </ul>
    <h5>투자의견 컨센서스</h5>
    <p class="disc table">[기준:{page_date}]</p>
    <table class="gHead" id="cTB15">
    <tr><th>투자의견</th><th>목표주가</th><th>EPS</th><th>PER</th><th>추정기관수</th></tr>
    <tr>
      <td>4.0</td><td>500,000</td><td>46,664</td><td>6.11</td><td>24</td>
    </tr></table>
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


def _companyguide_no_consensus_html(
    page_date: str,
    *,
    company_name: str,
):
    return f"""
    <title>{company_name} - 기업현황 - 기업모니터</title>
    <p class="disc table">[기준:{page_date}]</p>
    <h5>투자의견 컨센서스</h5>
    <table class="gHead" id="cTB15">
      <tr><th>투자의견</th><th>목표주가</th><th>EPS</th><th>PER</th><th>추정기관수</th></tr>
      <tr><td colspan="5">최근3개월 이내에 제시된 의견이 없습니다</td></tr>
    </table>
    """


def _write_corp_code_archive(path: Path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    xml = "<result>" + "".join(
        (
            "<list>"
            f"<corp_code>{corp_code}</corp_code>"
            f"<corp_name>{corp_name}</corp_name>"
            f"<stock_code>{stock_code}</stock_code>"
            f"<modify_date>{modify_date}</modify_date>"
            "</list>"
        )
        for corp_code, corp_name, stock_code, modify_date in rows
    ) + "</result>"
    payload = io.BytesIO()
    with zipfile.ZipFile(payload, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("CORPCODE.xml", xml.encode("utf-8"))
    path.write_bytes(payload.getvalue())


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
                "FILE_NM": "provider_report_page_2.pdf",
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


def _krx_stock_row(*, symbol: str = "005930", name: str = "Current Corp"):
    return {
        "BAS_DD": "20260710",
        "ISU_CD": symbol,
        "ISU_NM": name,
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
