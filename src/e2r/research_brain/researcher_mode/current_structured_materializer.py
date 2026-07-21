"""Live point-in-time structured sources for current Researcher Mode.

The Phase 86 engine already knows how to derive FCF, growth, market reaction,
valuation multiples, historical bands, and deterministic scenarios.  This
module closes the missing production boundary: it fetches real OpenDART,
CompanyGuide, KRX, and data.go.kr rows, preserves response hashes, and donates
typed source payloads to that engine without assigning points or Stage.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, replace
from datetime import date, datetime, timedelta
import hashlib
import json
import math
import os
from pathlib import Path
import re
from typing import Any, Callable, Mapping, Protocol, Sequence

import requests

from e2r.cheap_scan.korea_sources import DataGoKrFSCConnector
from e2r.env import load_project_env
from e2r.models import ConsensusSnapshot, PriceBar, ResearchReport
from e2r.production.metadata import stable_hash, write_json, write_jsonl
from e2r.production.source_connectors.companyguide_live_connector import (
    parse_companyguide_live_consensus_payload,
)
from e2r.sources.company_guide import CompanyGuideConnector

from .component_researcher import StructuredResearchProvider
from .official_source_materializer import OfficialSourceMaterializationResult
from .prompt_projection import project_peer_selection_context
from .schemas import EvidenceFact, assert_blind_research_output
from .structured_data_researcher import StructuredMetricRecord
from .structured_financial_engine import (
    ForwardGuidanceObservation,
    PeerValuationObservation,
    SegmentFinancialObservation,
    StructuredEngineResult,
    StructuredFinancialConsensusValuationEngine,
    StructuredSourcePayload,
)
from .structured_source_routes import (
    InMemoryStructuredSourceRoute,
    OpenDARTActualsStructuredRoute,
    UnavailableStructuredSourceRoute,
)


_DART_FULL_ACCOUNT_URL = (
    "https://opendart.fss.or.kr/api/fnlttSinglAcntAll.json"
)
_COMPANYGUIDE_SNAPSHOT_URL = (
    "https://comp.wisereport.co.kr/company/c1010001.aspx"
)
_COMPANYGUIDE_REPORTS_URL = (
    "https://comp.wisereport.co.kr/company/ajax/c1080001_data.aspx"
)
_DATA_GO_PRICE_URL = (
    "https://apis.data.go.kr/1160100/service/"
    "GetStockSecuritiesInfoService/getStockPriceInfo"
)
_KRX_STOCK_URLS = {
    "KOSPI": "https://data-dbg.krx.co.kr/svc/apis/sto/stk_bydd_trd",
    "KOSDAQ": "https://data-dbg.krx.co.kr/svc/apis/sto/ksq_bydd_trd",
}
_KRX_INDEX_URLS = {
    "KOSPI": "https://data-dbg.krx.co.kr/svc/apis/idx/kospi_dd_trd",
    "KOSDAQ": "https://data-dbg.krx.co.kr/svc/apis/idx/kosdaq_dd_trd",
}
_INDEX_NAMES = {"KOSPI": "코스피", "KOSDAQ": "코스닥"}

_ISSUER_STRUCTURED_SOURCE_FAMILIES = frozenset(
    {
        "OPENDART",
        "KIND_KRX",
        "ISSUER_EARNINGS_RELEASE",
        "ISSUER_PRESENTATION",
        "ISSUER_NEWSROOM",
        "CUSTOMER_OFFICIAL",
    }
)
_QOQ_STRUCTURED_SOURCE_FAMILIES = frozenset(
    {
        *_ISSUER_STRUCTURED_SOURCE_FAMILIES,
        "FINANCIAL_STATEMENTS",
        "SEGMENT_DATA",
        "CASH_FLOW",
        "PUBLIC_BROKER_PDF",
    }
)
_FACT_STRUCTURED_ROLES = frozenset(
    {"SEGMENT_CONTRIBUTION", "QOQ_GROWTH", "FORWARD_GUIDANCE"}
)

# Public discovery contract: this tells the LLM what kind of source-backed
# observation the deterministic structured engine can actually accept.  It
# deliberately contains no literal query, issuer name, sector name, or points.
FACT_STRUCTURED_ROLE_RESOLUTION_CONTRACTS: Mapping[
    str, Mapping[str, Any]
] = {
    "SEGMENT_CONTRIBUTION": {
        "allowed_source_families": tuple(
            sorted(_ISSUER_STRUCTURED_SOURCE_FAMILIES)
        ),
        "exact_quote_required": True,
        "machine_numeric_value_required": True,
        "specific_business_segment_required": True,
        "point_value_required": True,
        "issuer_source_required": True,
    },
    "QOQ_GROWTH": {
        "allowed_source_families": tuple(
            sorted(_QOQ_STRUCTURED_SOURCE_FAMILIES)
        ),
        "exact_quote_required": True,
        "machine_numeric_value_required": True,
        "point_percent_required": True,
        "current_lifecycle_required": True,
    },
    "FORWARD_GUIDANCE": {
        "allowed_source_families": tuple(
            sorted(_ISSUER_STRUCTURED_SOURCE_FAMILIES)
        ),
        "exact_quote_required": True,
        "machine_numeric_point_or_range_required": True,
        "period_must_be_forward_from_source_availability_date": True,
        "issuer_source_required": True,
        "third_party_estimate_is_not_substitutable": True,
    },
}

CURRENT_STRUCTURED_OUTPUT_FILES: Mapping[str, str] = {
    "fetch_attempts": "current_structured_fetch_attempts.jsonl",
    "payload_manifest": "current_structured_payload_manifest.jsonl",
    "result": "current_structured_materialization.json",
    "audit": "current_structured_materialization_audit.json",
}

_CURRENT_STRUCTURED_CACHE_SCHEMA_VERSION = (
    "e2r_v5_current_structured_cache_v2"
)


@dataclass(frozen=True)
class StructuredHTTPResponse:
    status_code: int
    canonical_url: str
    provider_request_id: str
    content_hash: str
    payload: Mapping[str, Any] | None = None
    text: str | None = None


class CurrentStructuredHTTPTransport(Protocol):
    def get_json(
        self,
        *,
        url: str,
        params: Mapping[str, Any],
        headers: Mapping[str, str],
        timeout_seconds: float,
    ) -> StructuredHTTPResponse:
        ...

    def get_text(
        self,
        *,
        url: str,
        params: Mapping[str, Any],
        headers: Mapping[str, str],
        timeout_seconds: float,
    ) -> StructuredHTTPResponse:
        ...


class RequestsCurrentStructuredHTTPTransport:
    def get_json(
        self,
        *,
        url: str,
        params: Mapping[str, Any],
        headers: Mapping[str, str],
        timeout_seconds: float,
    ) -> StructuredHTTPResponse:
        response = requests.get(
            url,
            params=dict(params),
            headers=dict(headers),
            timeout=(5.0, timeout_seconds),
        )
        response.raise_for_status()
        payload = response.json()
        if not isinstance(payload, Mapping):
            raise ValueError("structured JSON response is not an object")
        return StructuredHTTPResponse(
            status_code=response.status_code,
            canonical_url=response.url.split("?", 1)[0],
            provider_request_id=(
                response.headers.get("X-Request-ID")
                or "HTTP-" + hashlib.sha256(response.content).hexdigest()[:20]
            ),
            content_hash=hashlib.sha256(response.content).hexdigest(),
            payload=dict(payload),
        )

    def get_text(
        self,
        *,
        url: str,
        params: Mapping[str, Any],
        headers: Mapping[str, str],
        timeout_seconds: float,
    ) -> StructuredHTTPResponse:
        response = requests.get(
            url,
            params=dict(params),
            headers=dict(headers),
            timeout=(5.0, timeout_seconds),
        )
        response.raise_for_status()
        return StructuredHTTPResponse(
            status_code=response.status_code,
            canonical_url=response.url.split("?", 1)[0],
            provider_request_id=(
                response.headers.get("X-Request-ID")
                or "HTTP-" + hashlib.sha256(response.content).hexdigest()[:20]
            ),
            content_hash=hashlib.sha256(response.content).hexdigest(),
            text=response.text,
        )


@dataclass(frozen=True)
class CurrentStructuredFetchAttempt:
    attempt_id: str
    target_id: str
    as_of_date: str
    provider_name: str
    source_role: str
    canonical_url: str
    status: str
    provider_request_id: str | None
    content_hash: str | None
    row_count: int
    effective_date: str | None
    cache_hit: bool
    error: str | None = None
    production_score_authority: bool = False
    schema_version: str = "e2r_v5_current_structured_fetch_attempt_v1"

    def __post_init__(self) -> None:
        if self.status not in {
            "FETCHED",
            "NO_RESULT",
            "AUTH_FAILED",
            "PROVIDER_ERROR",
            "FUTURE_REJECTED",
        }:
            raise ValueError("unknown current structured fetch status")
        if self.status == "FETCHED" and not self.content_hash:
            raise ValueError("fetched structured source requires content hash")
        if self.production_score_authority:
            raise ValueError("structured fetch attempts cannot assign score")

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class CurrentStructuredMaterializationResult:
    target_id: str
    as_of_date: str
    latest_trading_snapshot_date: str
    status: str
    engine_result: StructuredEngineResult
    fetch_attempts: tuple[CurrentStructuredFetchAttempt, ...]
    payload_manifest: tuple[Mapping[str, Any], ...]
    pending_reasons: tuple[str, ...]
    audit: Mapping[str, Any]
    production_score_authority: bool = False
    schema_version: str = "e2r_v5_current_structured_materialization_v1"

    def __post_init__(self) -> None:
        if self.status not in {"COMPLETE", "SOURCE_PENDING"}:
            raise ValueError("unknown current structured materialization status")
        if self.production_score_authority:
            raise ValueError("structured materialization cannot assign score")
        if self.status == "COMPLETE" and self.pending_reasons:
            raise ValueError("complete structured materialization has pending reasons")

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "schema_version": self.schema_version,
            "target_id": self.target_id,
            "as_of_date": self.as_of_date,
            "latest_trading_snapshot_date": self.latest_trading_snapshot_date,
            "status": self.status,
            "engine_result": self.engine_result.to_dict(),
            "fetch_attempts": [row.to_dict() for row in self.fetch_attempts],
            "payload_manifest": [dict(row) for row in self.payload_manifest],
            "pending_reasons": list(self.pending_reasons),
            "audit": dict(self.audit),
            "production_score_authority": False,
        }


@dataclass(frozen=True)
class _ParsedReportedNumeric:
    low: float | None
    high: float | None
    midpoint: float
    unit: str


class CurrentStructuredSourceMaterializer:
    """Collect every canonical structured route and fail closed on gaps."""

    def __init__(
        self,
        *,
        transport: CurrentStructuredHTTPTransport | None = None,
        timeout_seconds: float = 30.0,
        price_lookback_days: int = 1_825,
        companyguide_report_rows: int = 100,
        peer_provider: StructuredResearchProvider | None = None,
    ) -> None:
        if timeout_seconds <= 0 or timeout_seconds > 120:
            raise ValueError("structured source timeout must be bounded")
        if price_lookback_days < 370:
            raise ValueError("structured price history must cover at least one year")
        if companyguide_report_rows <= 0 or companyguide_report_rows > 100:
            raise ValueError("CompanyGuide report rows exceed provider page maximum")
        self.transport = transport or RequestsCurrentStructuredHTTPTransport()
        self.timeout_seconds = timeout_seconds
        self.price_lookback_days = price_lookback_days
        self.companyguide_report_rows = companyguide_report_rows
        self.peer_provider = peer_provider

    def materialize(
        self,
        *,
        target_id: str,
        target_name: str,
        as_of_date: str,
        latest_trading_snapshot_date: str,
        official: OfficialSourceMaterializationResult,
        output_root: str | Path,
        checkpoint_resume: bool,
        evidence_facts: Sequence[EvidenceFact | Mapping[str, Any]] = (),
        source_claims: Sequence[Mapping[str, Any]] = (),
        source_documents: Sequence[Mapping[str, Any]] = (),
        required_roles_by_component: Mapping[str, Sequence[str]] | None = None,
        shared_cache_roots: Sequence[str | Path] = (),
    ) -> CurrentStructuredMaterializationResult:
        cutoff = date.fromisoformat(as_of_date)
        trading_date = date.fromisoformat(latest_trading_snapshot_date)
        if trading_date > cutoff:
            raise ValueError("structured trading snapshot leaks future data")
        if official.target_id != target_id or official.as_of_date != as_of_date:
            raise ValueError("official/structured target boundary mismatch")
        load_project_env()
        root = Path(output_root)
        cache_root = root / "structured_source_cache"
        reusable_cache_roots = tuple(
            dict.fromkeys(
                candidate
                for value in shared_cache_roots
                if (candidate := Path(value)) != cache_root
            )
        )
        attempts: list[CurrentStructuredFetchAttempt] = []
        manifests: list[Mapping[str, Any]] = []

        dart_route = self._opendart_route(
            target_id=target_id,
            cutoff=cutoff,
            official=official,
            cache_root=cache_root,
            checkpoint_resume=checkpoint_resume,
            attempts=attempts,
            manifests=manifests,
        )
        companyguide_route = self._companyguide_route(
            target_id=target_id,
            target_name=target_name,
            cutoff=cutoff,
            cache_root=cache_root,
            checkpoint_resume=checkpoint_resume,
            attempts=attempts,
            manifests=manifests,
            shared_cache_roots=reusable_cache_roots,
        )
        price_route = self._price_route(
            target_id=target_id,
            cutoff=cutoff,
            trading_date=trading_date,
            cache_root=cache_root,
            checkpoint_resume=checkpoint_resume,
            attempts=attempts,
            manifests=manifests,
        )
        issuer_route, issuer_fact_audit = _issuer_fact_route(
            target_id=target_id,
            cutoff=cutoff,
            evidence_facts=evidence_facts,
            source_claims=source_claims,
            source_documents=source_documents,
        )
        peer_route, peer_selection_audit = self._peer_route(
            target_id=target_id,
            target_name=target_name,
            cutoff=cutoff,
            evidence_facts=evidence_facts,
            source_claims=source_claims,
            cache_root=cache_root,
            checkpoint_resume=checkpoint_resume,
            attempts=attempts,
            manifests=manifests,
            shared_cache_roots=reusable_cache_roots,
        )
        routes = (
            companyguide_route,
            UnavailableStructuredSourceRoute(
                "PUBLIC_BROKER_REPORT",
                "full public report route remains LLM source-graph owned",
            ),
            issuer_route,
            dart_route,
            price_route,
            peer_route,
        )
        engine = StructuredFinancialConsensusValuationEngine().research(
            target_id=target_id,
            symbol=target_id,
            company_name=target_name,
            as_of_date=cutoff,
            routes=routes,
            required_roles_by_component=required_roles_by_component,
            deep_researched_canary=True,
        )
        pending = tuple(
            dict.fromkeys(
                (
                    *(
                        f"STRUCTURED_FETCH_PENDING:{row.provider_name}:{row.source_role}:{row.status}"
                        for row in attempts
                        if row.status
                        in {"AUTH_FAILED", "PROVIDER_ERROR", "FUTURE_REJECTED"}
                    ),
                    *(
                        f"STRUCTURED_ROLE_MISSING:{component_id}:{role}"
                        for component_id, roles in engine.missing_roles_by_component.items()
                        for role in roles
                    ),
                    *(
                        (
                            "PEER_SELECTION_PENDING:"
                            + str(peer_selection_audit.get("pending_reason") or "UNKNOWN")
                        ,)
                        if peer_selection_audit.get("status")
                        != "PEER_SELECTION_COMPLETE"
                        else ()
                    ),
                )
            )
        )
        complete = engine.status == "COMPLETE" and not pending
        critical_counts = {
            "future_structured_source_count": sum(
                row.status == "FUTURE_REJECTED" for row in attempts
            ),
            "provider_or_auth_failure_count": sum(
                row.status in {"AUTH_FAILED", "PROVIDER_ERROR"}
                for row in attempts
            ),
            "missing_structured_role_count": sum(
                len(value) for value in engine.missing_roles_by_component.values()
            ),
            "peer_selection_pending_count": int(
                peer_selection_audit.get("status") != "PEER_SELECTION_COMPLETE"
            ),
            "deep_canary_valuation_route_not_attempted_count": (
                engine.deep_researched_canary_valuation_route_not_attempted_count
            ),
            "revision_zero_due_connector_gap_count": (
                engine.revision_component_zero_solely_due_connector_gap_count
            ),
            "fcf_zero_due_missing_parser_count": (
                engine.fcf_component_zero_solely_due_missing_parser_count
            ),
        }
        audit = {
            "schema_version": "e2r_v5_current_structured_materialization_audit_v1",
            "status": (
                "CURRENT_STRUCTURED_MATERIALIZATION_PASS"
                if complete
                else "CURRENT_STRUCTURED_MATERIALIZATION_PENDING"
            ),
            "target_id": target_id,
            "as_of_date": as_of_date,
            "latest_trading_snapshot_date": trading_date.isoformat(),
            "fetch_attempt_count": len(attempts),
            "cache_hit_count": sum(row.cache_hit for row in attempts),
            "payload_manifest_count": len(manifests),
            "structured_record_count": len(engine.records),
            "financial_record_count": len(engine.financial_records),
            "consensus_revision_record_count": len(
                engine.consensus_revision_records
            ),
            "valuation_record_count": len(engine.valuation_records),
            "required_roles_by_component": {
                component_id: list(roles)
                for component_id, roles in (
                    required_roles_by_component or {}
                ).items()
            },
            "issuer_fact_materialization": issuer_fact_audit,
            "peer_selection": peer_selection_audit,
            "fixed_transport_count_is_completion": False,
            "provider_failure_is_zero_score": False,
            "future_data_is_rejected": True,
            "llm_structured_tag_direct_score_authority": False,
            "structured_fact_requires_verified_exact_quote": True,
            "critical_counts": critical_counts,
            "critical_count_sum": sum(critical_counts.values()),
        }
        result = CurrentStructuredMaterializationResult(
            target_id=target_id,
            as_of_date=as_of_date,
            latest_trading_snapshot_date=trading_date.isoformat(),
            status="COMPLETE" if complete else "SOURCE_PENDING",
            engine_result=engine,
            fetch_attempts=tuple(attempts),
            payload_manifest=tuple(manifests),
            pending_reasons=pending,
            audit=audit,
        )
        write_current_structured_materialization(result, root)
        return result

    def _opendart_route(
        self,
        *,
        target_id: str,
        cutoff: date,
        official: OfficialSourceMaterializationResult,
        cache_root: Path,
        checkpoint_resume: bool,
        attempts: list[CurrentStructuredFetchAttempt],
        manifests: list[Mapping[str, Any]],
    ):
        credential = os.environ.get("OPENDART_API_KEY") or os.environ.get(
            "OPEN_DART_API_KEY"
        )
        corp_code = _official_corp_code(official)
        if not credential:
            attempts.append(
                _failed_attempt(
                    target_id,
                    cutoff,
                    "OpenDART",
                    "FINANCIAL_ACTUALS",
                    _DART_FULL_ACCOUNT_URL,
                    "AUTH_FAILED",
                    "OPENDART_API_KEY is not configured",
                )
            )
            return UnavailableStructuredSourceRoute(
                "DART_ACTUALS_DETERMINISTIC_SCENARIO", "OpenDART credential missing"
            )
        if not corp_code:
            attempts.append(
                _failed_attempt(
                    target_id,
                    cutoff,
                    "OpenDART",
                    "FINANCIAL_ACTUALS",
                    _DART_FULL_ACCOUNT_URL,
                    "PROVIDER_ERROR",
                    "official OpenDART source did not expose corp_code",
                )
            )
            return UnavailableStructuredSourceRoute(
                "DART_ACTUALS_DETERMINISTIC_SCENARIO", "OpenDART corp_code missing"
            )
        payloads: list[Mapping[str, Any]] = []
        for period in _financial_statement_periods(cutoff):
            key = (
                f"dart_{target_id}_{corp_code}_{period['fiscal_year']}_"
                f"{period['report_code']}_CFS"
            )
            response = self._json(
                target_id=target_id,
                cutoff=cutoff,
                provider_name="OpenDART",
                source_role="FINANCIAL_ACTUALS",
                cache_key=key,
                cache_root=cache_root,
                checkpoint_resume=checkpoint_resume,
                url=_DART_FULL_ACCOUNT_URL,
                params={
                    "crtfc_key": credential,
                    "corp_code": corp_code,
                    "bsns_year": str(period["fiscal_year"]),
                    "reprt_code": period["report_code"],
                    "fs_div": "CFS",
                },
                headers={},
                attempts=attempts,
                manifests=manifests,
                effective_date=period["reported_at"].isoformat(),
                rows_getter=lambda value: value.get("list") or (),
            )
            if response is None:
                continue
            status = str(response.get("status") or "")
            if status != "000" or not isinstance(response.get("list"), list):
                continue
            payloads.append(
                {
                    "payload": response,
                    "fiscal_year": period["fiscal_year"],
                    "fiscal_quarter": period["fiscal_quarter"],
                    "period_end": period["period_end"].isoformat(),
                    "reported_at": period["reported_at"].isoformat(),
                    "report_code": period["report_code"],
                    "corp_code": corp_code,
                }
            )
        if not payloads:
            return UnavailableStructuredSourceRoute(
                "DART_ACTUALS_DETERMINISTIC_SCENARIO",
                "OpenDART returned no usable full-account payload",
            )
        return OpenDARTActualsStructuredRoute(
            connector=_EmptyFinancialActualConnector(),
            single_account_payloads=tuple(payloads),
        )

    def _companyguide_route(
        self,
        *,
        target_id: str,
        target_name: str,
        cutoff: date,
        cache_root: Path,
        checkpoint_resume: bool,
        attempts: list[CurrentStructuredFetchAttempt],
        manifests: list[Mapping[str, Any]],
        shared_cache_roots: Sequence[Path] = (),
    ):
        snapshot = self._text(
            target_id=target_id,
            cutoff=cutoff,
            provider_name="CompanyGuide",
            source_role="CONSENSUS_VALUATION_SNAPSHOT",
            cache_key=f"companyguide_snapshot_{target_id}",
            cache_root=cache_root,
            checkpoint_resume=checkpoint_resume,
            url=_COMPANYGUIDE_SNAPSHOT_URL,
            params={"cmp_cd": target_id, "cn": ""},
            headers={"User-Agent": "Mozilla/5.0 E2R-ResearcherMode/5.0"},
            attempts=attempts,
            manifests=manifests,
            shared_cache_roots=shared_cache_roots,
            shared_cache_keys=(
                f"companyguide_snapshot_{target_id}",
                f"companyguide_peer_snapshot_{target_id}",
            ),
            cached_response_validator=lambda response: (
                _companyguide_cached_snapshot_is_point_in_time(
                    response,
                    cutoff=cutoff,
                    expected_company_name=target_name,
                )
            ),
        )
        reports_payload = self._json(
            target_id=target_id,
            cutoff=cutoff,
            provider_name="CompanyGuide",
            source_role="BROKER_REPORT_HISTORY",
            cache_key=f"companyguide_reports_{target_id}",
            cache_root=cache_root,
            checkpoint_resume=checkpoint_resume,
            url=_COMPANYGUIDE_REPORTS_URL,
            params={
                "cmp_cd": target_id,
                "perPage": self.companyguide_report_rows,
                "curPage": 1,
            },
            headers={"User-Agent": "Mozilla/5.0 E2R-ResearcherMode/5.0"},
            attempts=attempts,
            manifests=manifests,
            rows_getter=lambda value: value.get("lists") or (),
        )
        source_ids = tuple(
            dict.fromkeys(
                row["source_id"]
                for row in manifests
                if row["provider_name"] == "CompanyGuide"
            )
        )
        snapshots: list[ConsensusSnapshot] = []
        reports: tuple[ResearchReport, ...] = ()
        seed_records: list[StructuredMetricRecord] = []
        if snapshot:
            parsed = parse_companyguide_live_consensus_payload(
                snapshot, as_of_date=cutoff
            )
            raw_snapshot_date = str(
                parsed.get("CONSENSUS_AS_OF_DATE") or ""
            ).replace("/", "-")[:10]
            try:
                snapshot_date = date.fromisoformat(raw_snapshot_date)
            except ValueError:
                snapshot_date = None
            if snapshot_date is not None and snapshot_date > cutoff:
                _mark_attempt_future_rejected(
                    attempts,
                    source_role="CONSENSUS_VALUATION_SNAPSHOT",
                    effective_date=snapshot_date.isoformat(),
                )
            consensus = _companyguide_consensus_snapshot(
                target_id=target_id,
                cutoff=cutoff,
                payload=parsed,
            )
            if consensus is not None:
                snapshots.append(consensus)
        if reports_payload:
            try:
                parsed_reports = CompanyGuideConnector.parse_recent_reports_payload(
                    reports_payload,
                    symbol=target_id,
                    as_of_date=cutoff,
                )
            except (TypeError, ValueError, json.JSONDecodeError):
                parsed_reports = ()
            reports = tuple(_enrich_report(row) for row in parsed_reports)
            report_source_id = next(
                (
                    row["source_id"]
                    for row in reversed(manifests)
                    if row["provider_name"] == "CompanyGuide"
                    and row["source_role"] == "BROKER_REPORT_HISTORY"
                ),
                None,
            )
            if report_source_id:
                snapshots.extend(
                    _report_consensus_snapshots(
                        reports,
                        target_id=target_id,
                        cutoff=cutoff,
                    )
                )
                seed_records.extend(
                    _report_direction_records(
                        reports,
                        target_id=target_id,
                        cutoff=cutoff,
                        source_id=report_source_id,
                    )
                )
        has_rows = bool(snapshots or reports or seed_records)
        if not has_rows or not source_ids:
            return UnavailableStructuredSourceRoute(
                "COMPANYGUIDE", "CompanyGuide returned no point-in-time structured rows"
            )
        payload = StructuredSourcePayload(
            route_name="COMPANYGUIDE",
            source_ids=source_ids,
            consensus_snapshots=tuple(snapshots),
            research_reports=reports,
            structured_records=tuple(seed_records),
            diagnostics={
                "snapshot_count": len(snapshots),
                "report_count": len(reports),
                "direction_record_count": len(seed_records),
                "report_page_is_provider_bounded_not_research_completion": True,
            },
        )
        return InMemoryStructuredSourceRoute("COMPANYGUIDE", payload)

    def _price_route(
        self,
        *,
        target_id: str,
        cutoff: date,
        trading_date: date,
        cache_root: Path,
        checkpoint_resume: bool,
        attempts: list[CurrentStructuredFetchAttempt],
        manifests: list[Mapping[str, Any]],
    ):
        bars: list[PriceBar] = []
        data_key = os.environ.get("DATA_GO_KR_SERVICE_KEY")
        if data_key:
            page = 1
            total_pages = 1
            connector = DataGoKrFSCConnector(
                service_key=data_key, fixture_mode=False
            )
            while page <= total_pages:
                payload = self._json(
                    target_id=target_id,
                    cutoff=cutoff,
                    provider_name="data.go.kr",
                    source_role="PRICE_HISTORY",
                    cache_key=f"data_go_price_{target_id}_{page:04d}",
                    cache_root=cache_root,
                    checkpoint_resume=checkpoint_resume,
                    url=_DATA_GO_PRICE_URL,
                    params={
                        "serviceKey": data_key,
                        "resultType": "json",
                        "likeSrtnCd": target_id,
                        "beginBasDt": (
                            cutoff - timedelta(days=self.price_lookback_days)
                        ).strftime("%Y%m%d"),
                        "endBasDt": cutoff.strftime("%Y%m%d"),
                        "pageNo": page,
                        "numOfRows": 1000,
                    },
                    headers={},
                    attempts=attempts,
                    manifests=manifests,
                    rows_getter=_data_go_items,
                )
                if payload is None:
                    break
                rows = _data_go_items(payload)
                for row in rows:
                    try:
                        bar = connector.normalize_price_bar(row)
                    except (TypeError, ValueError):
                        continue
                    if bar.symbol == target_id and bar.date <= cutoff:
                        bars.append(bar)
                total_pages = _data_go_total_pages(payload, rows_per_page=1000)
                page += 1
        else:
            attempts.append(
                _failed_attempt(
                    target_id,
                    cutoff,
                    "data.go.kr",
                    "PRICE_HISTORY",
                    _DATA_GO_PRICE_URL,
                    "AUTH_FAILED",
                    "DATA_GO_KR_SERVICE_KEY is not configured",
                )
            )

        market = None
        krx_key = os.environ.get("KRX_OPENAPI_KEY")
        if krx_key:
            for candidate_market, url in _KRX_STOCK_URLS.items():
                payload = self._json(
                    target_id=target_id,
                    cutoff=cutoff,
                    provider_name="KRX",
                    source_role="CURRENT_PRICE_MARKET_CAP",
                    cache_key=(
                        f"krx_{candidate_market.lower()}_{trading_date:%Y%m%d}"
                    ),
                    cache_root=cache_root,
                    checkpoint_resume=checkpoint_resume,
                    url=url,
                    params={"basDd": trading_date.strftime("%Y%m%d")},
                    headers={"AUTH_KEY": krx_key},
                    attempts=attempts,
                    manifests=manifests,
                    effective_date=trading_date.isoformat(),
                    rows_getter=lambda value: value.get("OutBlock_1") or (),
                )
                if payload is None:
                    continue
                target_row = next(
                    (
                        row
                        for row in payload.get("OutBlock_1") or ()
                        if isinstance(row, Mapping)
                        and str(row.get("ISU_CD") or row.get("ISU_SRT_CD") or "")
                        == target_id
                    ),
                    None,
                )
                if target_row is None:
                    continue
                bar = _krx_stock_bar(target_row, target_id=target_id, cutoff=cutoff)
                if bar is not None:
                    bars.append(bar)
                    market = candidate_market
                    break
            if market:
                for benchmark_date in (
                    trading_date - timedelta(days=35),
                    trading_date,
                ):
                    payload = self._json(
                        target_id=target_id,
                        cutoff=cutoff,
                        provider_name="KRX",
                        source_role="BENCHMARK_PRICE",
                        cache_key=(
                            f"krx_index_{market.lower()}_{benchmark_date:%Y%m%d}"
                        ),
                        cache_root=cache_root,
                        checkpoint_resume=checkpoint_resume,
                        url=_KRX_INDEX_URLS[market],
                        params={"basDd": benchmark_date.strftime("%Y%m%d")},
                        headers={"AUTH_KEY": krx_key},
                        attempts=attempts,
                        manifests=manifests,
                        effective_date=benchmark_date.isoformat(),
                        rows_getter=lambda value: value.get("OutBlock_1") or (),
                    )
                    if payload:
                        index_row = next(
                            (
                                row
                                for row in payload.get("OutBlock_1") or ()
                                if isinstance(row, Mapping)
                                and str(row.get("IDX_NM") or "")
                                == _INDEX_NAMES[market]
                            ),
                            None,
                        )
                        bar = _krx_index_bar(
                            index_row,
                            market=market,
                            cutoff=cutoff,
                        )
                        if bar is not None:
                            bars.append(bar)
        else:
            attempts.append(
                _failed_attempt(
                    target_id,
                    cutoff,
                    "KRX",
                    "CURRENT_PRICE_MARKET_CAP",
                    _KRX_STOCK_URLS["KOSPI"],
                    "AUTH_FAILED",
                    "KRX_OPENAPI_KEY is not configured",
                )
            )
        selected = _dedupe_price_bars(bars, target_id=target_id)
        source_ids = tuple(
            dict.fromkeys(
                row["source_id"]
                for row in manifests
                if row["provider_name"] in {"KRX", "data.go.kr"}
            )
        )
        if not selected or not source_ids:
            return UnavailableStructuredSourceRoute(
                "KRX_PRICE_MARKET_CAP", "no point-in-time price history available"
            )
        payload = StructuredSourcePayload(
            route_name="KRX_PRICE_MARKET_CAP",
            source_ids=source_ids,
            price_bars=selected,
            diagnostics={
                "market": market,
                "price_bar_count": len(selected),
                "current_snapshot_date": trading_date.isoformat(),
                "history_provider": "data.go.kr",
                "current_provider": "KRX",
            },
        )
        return InMemoryStructuredSourceRoute("KRX_PRICE_MARKET_CAP", payload)

    def _peer_route(
        self,
        *,
        target_id: str,
        target_name: str,
        cutoff: date,
        evidence_facts: Sequence[EvidenceFact | Mapping[str, Any]],
        source_claims: Sequence[Mapping[str, Any]],
        cache_root: Path,
        checkpoint_resume: bool,
        attempts: list[CurrentStructuredFetchAttempt],
        manifests: list[Mapping[str, Any]],
        shared_cache_roots: Sequence[Path] = (),
        _structured_verification_retry_used: bool = False,
    ):
        provider_name = (
            str(
                getattr(
                    self.peer_provider,
                    "provider_name",
                    type(self.peer_provider).__name__,
                )
            )
            if self.peer_provider is not None
            else "UNCONFIGURED"
        )
        base_audit: dict[str, Any] = {
            "schema_version": "e2r_v5_structured_peer_selection_audit_v1",
            "status": "PEER_SELECTION_PENDING",
            "target_id": target_id,
            "as_of_date": cutoff.isoformat(),
            "provider_name": provider_name,
            "provider_prompt_hash": None,
            "provider_response_hash": None,
            "provider_cache_hit": False,
            "provider_attempt_count": 0,
            "validation_retry_used": False,
            "structured_verification_retry_used": (
                _structured_verification_retry_used
            ),
            "proposal_count": 0,
            "verified_peer_count": 0,
            "peer_observation_count": 0,
            "common_metric_peer_counts": {},
            "selected_peers": [],
            "pending_reason": None,
            "llm_selects_direction_only": True,
            "llm_supplies_valuation_values": False,
            "point_in_time_structured_fetch_required": True,
            "production_score_authority": False,
        }
        if self.peer_provider is None:
            base_audit["pending_reason"] = "PEER_PROVIDER_NOT_CONFIGURED"
            return (
                UnavailableStructuredSourceRoute(
                    "PEER_STRUCTURED", "peer-selection provider is not configured"
                ),
                base_audit,
            )
        peer_selection_context = project_peer_selection_context(
            tuple(_fact_mapping(row) for row in evidence_facts),
            tuple(dict(row) for row in source_claims),
        )
        payload = {
            "target_id": target_id,
            "target_name": target_name,
            "as_of_date": cutoff.isoformat(),
            "missing_structured_role": "PEER_BAND",
            "current_evidence_facts": peer_selection_context[
                "evidence_business_profile"
            ],
            "source_backed_claim_context": peer_selection_context[
                "source_claim_business_profile"
            ],
            "peer_selection_context_accounting": {
                key: value
                for key, value in peer_selection_context.items()
                if key
                not in {
                    "evidence_business_profile",
                    "source_claim_business_profile",
                }
            },
            "selection_constraints": {
                "listing_market": "KOREA",
                "minimum_peer_count": 2,
                "maximum_peer_count": 5,
                "exact_symbol_format": "SIX_DIGIT_NUMERIC",
                "exclude_target_symbol": True,
                "sector_label_alone_is_insufficient": True,
                "structured_value_invention_forbidden": True,
                "score_or_stage_authority": False,
            },
        }
        selection_input_hash = stable_hash(payload)
        selection_cache_path = cache_root / f"peer_selection_{target_id}.json"
        response: Mapping[str, Any] | None = None
        cached_prompt_hash = None
        if checkpoint_resume and selection_cache_path.is_file():
            try:
                cached = json.loads(selection_cache_path.read_text(encoding="utf-8"))
                candidate = cached.get("response")
                if (
                    cached.get("target_id") == target_id
                    and cached.get("as_of_date") == cutoff.isoformat()
                    and cached.get("selection_input_hash") == selection_input_hash
                    and isinstance(candidate, Mapping)
                    and cached.get("provider_response_hash") == stable_hash(candidate)
                ):
                    response = dict(candidate)
                    cached_prompt_hash = str(
                        cached.get("provider_prompt_hash") or ""
                    ) or None
                    base_audit["provider_cache_hit"] = True
            except (OSError, TypeError, ValueError, json.JSONDecodeError):
                response = None
        try:
            if response is None:
                attempt_payload = payload
                for attempt_index in range(2):
                    base_audit["provider_attempt_count"] += 1
                    response = self.peer_provider.complete(
                        pass_name="STRUCTURED_PEER_SELECTION",
                        payload=attempt_payload,
                    )
                    try:
                        assert_blind_research_output(response)
                        proposals = _validated_peer_proposals(
                            response,
                            target_id=target_id,
                        )
                    except (KeyError, TypeError, ValueError) as exc:
                        if attempt_index == 0:
                            base_audit["validation_retry_used"] = True
                            attempt_payload = {
                                **payload,
                                "peer_selection_retry_context": {
                                    "validation_error": " ".join(
                                        str(exc).split()
                                    )[-500:],
                                    "instruction": (
                                        "Rewrite the complete peer selection under "
                                        "the original two-to-five peer contract; do "
                                        "not invent any valuation values."
                                    ),
                                },
                            }
                            continue
                        raise
                    break
            else:
                assert_blind_research_output(response)
                proposals = _validated_peer_proposals(
                    response,
                    target_id=target_id,
                )
            prompt_hash = cached_prompt_hash or _latest_provider_prompt_hash(
                self.peer_provider, "STRUCTURED_PEER_SELECTION"
            )
            if not base_audit["provider_cache_hit"]:
                write_json(
                    selection_cache_path,
                    {
                        "schema_version": "e2r_v5_peer_selection_cache_v1",
                        "target_id": target_id,
                        "as_of_date": cutoff.isoformat(),
                        "selection_input_hash": selection_input_hash,
                        "provider_name": provider_name,
                        "provider_prompt_hash": prompt_hash,
                        "provider_response_hash": stable_hash(response),
                        "response": dict(response),
                        "production_score_authority": False,
                    },
                )
        except Exception as exc:
            base_audit["provider_prompt_hash"] = _latest_provider_prompt_hash(
                self.peer_provider, "STRUCTURED_PEER_SELECTION"
            )
            base_audit["pending_reason"] = (
                "PEER_SELECTION_PROVIDER_OR_SCHEMA_ERROR:"
                + " ".join(str(exc).split())[-500:]
            )
            return (
                UnavailableStructuredSourceRoute(
                    "PEER_STRUCTURED", "peer selection provider/schema failed"
                ),
                base_audit,
            )

        base_audit["provider_prompt_hash"] = prompt_hash
        base_audit["provider_response_hash"] = stable_hash(response)
        base_audit["proposal_count"] = len(proposals)
        observations: list[PeerValuationObservation] = []
        selected_rows: list[Mapping[str, Any]] = []
        proposal_failures: list[str] = []
        for proposal in proposals:
            symbol = str(proposal["peer_symbol"])
            role = f"PEER_VALUATION_SNAPSHOT:{symbol}"
            text = self._text(
                target_id=target_id,
                cutoff=cutoff,
                provider_name="CompanyGuide",
                source_role=role,
                cache_key=f"companyguide_peer_snapshot_{symbol}",
                cache_root=cache_root,
                checkpoint_resume=checkpoint_resume,
                url=_COMPANYGUIDE_SNAPSHOT_URL,
                params={"cmp_cd": symbol, "cn": ""},
                headers={"User-Agent": "Mozilla/5.0 E2R-ResearcherMode/5.0"},
                attempts=attempts,
                manifests=manifests,
                shared_cache_roots=shared_cache_roots,
                shared_cache_keys=(
                    f"companyguide_peer_snapshot_{symbol}",
                    f"companyguide_snapshot_{symbol}",
                ),
                cached_response_validator=lambda response: (
                    _companyguide_cached_snapshot_is_point_in_time(
                        response,
                        cutoff=cutoff,
                        expected_company_name=str(proposal["peer_name"]),
                    )
                ),
            )
            if not text:
                proposal_failures.append(f"{symbol}:SNAPSHOT_FETCH_FAILED")
                continue
            parsed = parse_companyguide_live_consensus_payload(
                text, as_of_date=cutoff
            )
            actual_name = str(parsed.get("COMPANY_NAME") or "").strip()
            if not actual_name:
                proposal_failures.append(f"{symbol}:COMPANY_IDENTITY_UNVERIFIED")
                continue
            if _company_name_key(actual_name) != _company_name_key(
                proposal["peer_name"]
            ):
                proposal_failures.append(f"{symbol}:COMPANY_IDENTITY_MISMATCH")
                continue
            if parsed.get("CONSENSUS_DATE_VERIFIED") is not True:
                proposal_failures.append(f"{symbol}:SNAPSHOT_DATE_UNVERIFIED")
                continue
            try:
                observed = date.fromisoformat(
                    str(parsed["CONSENSUS_AS_OF_DATE"]).replace("/", "-")[:10]
                )
            except (KeyError, ValueError):
                proposal_failures.append(f"{symbol}:SNAPSHOT_DATE_INVALID")
                continue
            if observed > cutoff:
                _mark_attempt_future_rejected(
                    attempts,
                    source_role=role,
                    effective_date=observed.isoformat(),
                )
                proposal_failures.append(f"{symbol}:FUTURE_SNAPSHOT_REJECTED")
                continue
            source_id = next(
                (
                    str(row["source_id"])
                    for row in reversed(manifests)
                    if row.get("provider_name") == "CompanyGuide"
                    and row.get("source_role") == role
                ),
                None,
            )
            if not source_id:
                proposal_failures.append(f"{symbol}:SOURCE_MANIFEST_MISSING")
                continue
            metrics = (
                ("forward_pe", parsed.get("FORWARD_12M_PER")),
                ("forward_pb", parsed.get("FORWARD_12M_PBR")),
                ("forward_ev_ebitda", parsed.get("FORWARD_12M_EV_EBITDA")),
            )
            metric_count = 0
            for metric_id, raw_value in metrics:
                value = _float(raw_value)
                if value is None or value <= 0:
                    continue
                observations.append(
                    PeerValuationObservation(
                        peer_id=symbol,
                        as_of_date=cutoff.isoformat(),
                        metric_id=metric_id,
                        value=value,
                        unit="MULTIPLE",
                        observed_at=observed.isoformat(),
                        source_ids=(source_id,),
                        source_route="PEER_STRUCTURED",
                        confidence=float(proposal["confidence"]),
                        metadata={
                            "peer_name": actual_name,
                            "symbol_identity_verified_from_page": True,
                            "comparability_rationale": proposal[
                                "comparability_rationale"
                            ],
                            "shared_economic_drivers": list(
                                proposal["shared_economic_drivers"]
                            ),
                            "material_differences": list(
                                proposal["material_differences"]
                            ),
                            "structured_source": True,
                            "llm_supplied_metric_value": False,
                        },
                    )
                )
                metric_count += 1
            if metric_count == 0:
                proposal_failures.append(f"{symbol}:NO_FORWARD_MULTIPLE")
                continue
            selected_rows.append(
                {
                    "peer_symbol": symbol,
                    "proposed_peer_name": proposal["peer_name"],
                    "verified_peer_name": actual_name,
                    "observed_at": observed.isoformat(),
                    "structured_metric_count": metric_count,
                }
            )

        common_counts: dict[str, int] = {}
        for metric_id in sorted({row.metric_id for row in observations}):
            common_counts[metric_id] = len(
                {
                    row.peer_id
                    for row in observations
                    if row.metric_id == metric_id
                }
            )
        resolved = any(value >= 2 for value in common_counts.values())
        base_audit.update(
            {
                "verified_peer_count": len(
                    {row.peer_id for row in observations}
                ),
                "peer_observation_count": len(observations),
                "common_metric_peer_counts": common_counts,
                "selected_peers": selected_rows,
                "proposal_failures": proposal_failures,
            }
        )
        if not resolved:
            if not _structured_verification_retry_used:
                retry_payload = {
                    **payload,
                    "peer_selection_retry_context": {
                        "validation_error": (
                            "Structured source verification rejected the "
                            "proposed peers or found no multiple shared by at "
                            "least two verified peers."
                        ),
                        "proposal_failures": list(proposal_failures),
                        "verified_peers": list(selected_rows),
                        "common_metric_peer_counts": dict(common_counts),
                        "rejected_proposals": [dict(row) for row in proposals],
                        "instruction": (
                            "Select a different complete set of two to five "
                            "real Korean listed peers. Keep each six-digit "
                            "symbol paired with its exact legal company name. "
                            "Do not relabel a company, invent a listing vehicle, "
                            "or supply valuation values; CompanyGuide will "
                            "verify identity, date, and multiples again."
                        ),
                    },
                }
                try:
                    base_audit["provider_attempt_count"] += 1
                    retry_response = self.peer_provider.complete(
                        pass_name="STRUCTURED_PEER_SELECTION",
                        payload=retry_payload,
                    )
                    assert_blind_research_output(retry_response)
                    _validated_peer_proposals(
                        retry_response,
                        target_id=target_id,
                    )
                    retry_prompt_hash = _latest_provider_prompt_hash(
                        self.peer_provider,
                        "STRUCTURED_PEER_SELECTION",
                    )
                    write_json(
                        selection_cache_path,
                        {
                            "schema_version": "e2r_v5_peer_selection_cache_v1",
                            "target_id": target_id,
                            "as_of_date": cutoff.isoformat(),
                            "selection_input_hash": selection_input_hash,
                            "provider_name": provider_name,
                            "provider_prompt_hash": retry_prompt_hash,
                            "provider_response_hash": stable_hash(retry_response),
                            "response": dict(retry_response),
                            "production_score_authority": False,
                        },
                    )
                except Exception as exc:
                    base_audit["validation_retry_used"] = True
                    base_audit["structured_verification_retry_used"] = True
                    base_audit["pending_reason"] = (
                        "PEER_SELECTION_VERIFICATION_RETRY_ERROR:"
                        + " ".join(str(exc).split())[-500:]
                    )
                    return (
                        UnavailableStructuredSourceRoute(
                            "PEER_STRUCTURED",
                            "peer verification feedback retry failed",
                        ),
                        base_audit,
                    )
                route, retry_audit = self._peer_route(
                    target_id=target_id,
                    target_name=target_name,
                    cutoff=cutoff,
                    evidence_facts=evidence_facts,
                    source_claims=source_claims,
                    cache_root=cache_root,
                    checkpoint_resume=True,
                    attempts=attempts,
                    manifests=manifests,
                    shared_cache_roots=shared_cache_roots,
                    _structured_verification_retry_used=True,
                )
                retry_audit = dict(retry_audit)
                retry_audit["provider_attempt_count"] = int(
                    retry_audit.get("provider_attempt_count") or 0
                ) + int(base_audit["provider_attempt_count"])
                retry_audit["provider_cache_hit"] = bool(
                    base_audit["provider_cache_hit"]
                )
                retry_audit["validation_retry_used"] = True
                retry_audit["structured_verification_retry_used"] = True
                retry_audit["initial_proposal_failures"] = list(
                    proposal_failures
                )
                return route, retry_audit
            base_audit["pending_reason"] = "INSUFFICIENT_COMMON_PEER_MULTIPLES"
            return (
                UnavailableStructuredSourceRoute(
                    "PEER_STRUCTURED", "fewer than two verified peers share a multiple"
                ),
                base_audit,
            )
        source_ids = tuple(
            sorted({source_id for row in observations for source_id in row.source_ids})
        )
        base_audit["status"] = "PEER_SELECTION_COMPLETE"
        base_audit["pending_reason"] = None
        route_payload = StructuredSourcePayload(
            route_name="PEER_STRUCTURED",
            source_ids=source_ids,
            peer_valuations=tuple(observations),
            diagnostics=base_audit,
        )
        return InMemoryStructuredSourceRoute("PEER_STRUCTURED", route_payload), base_audit

    def _json(
        self,
        *,
        target_id: str,
        cutoff: date,
        provider_name: str,
        source_role: str,
        cache_key: str,
        cache_root: Path,
        checkpoint_resume: bool,
        url: str,
        params: Mapping[str, Any],
        headers: Mapping[str, str],
        attempts: list[CurrentStructuredFetchAttempt],
        manifests: list[Mapping[str, Any]],
        rows_getter,
        effective_date: str | None = None,
    ) -> Mapping[str, Any] | None:
        response, cache_hit, error = self._response(
            cache_key=cache_key,
            cache_root=cache_root,
            checkpoint_resume=checkpoint_resume,
            response_kind="json",
            request_url=url,
            request_params=params,
            fetch=lambda: self.transport.get_json(
                url=url,
                params=params,
                headers=headers,
                timeout_seconds=self.timeout_seconds,
            ),
        )
        payload = response.payload if response else None
        rows = rows_getter(payload) if payload else ()
        status = "FETCHED" if payload is not None else "PROVIDER_ERROR"
        if payload is not None and not rows:
            status = "NO_RESULT"
        attempts.append(
            _attempt(
                target_id=target_id,
                cutoff=cutoff,
                provider_name=provider_name,
                source_role=source_role,
                canonical_url=url,
                status=status,
                response=response,
                row_count=len(rows),
                effective_date=effective_date,
                cache_hit=cache_hit,
                error=error,
            )
        )
        if response and payload is not None:
            manifests.append(
                _manifest_row(
                    target_id=target_id,
                    cutoff=cutoff,
                    provider_name=provider_name,
                    source_role=source_role,
                    response=response,
                    row_count=len(rows),
                    effective_date=effective_date,
                )
            )
        return payload

    def _text(
        self,
        *,
        target_id: str,
        cutoff: date,
        provider_name: str,
        source_role: str,
        cache_key: str,
        cache_root: Path,
        checkpoint_resume: bool,
        url: str,
        params: Mapping[str, Any],
        headers: Mapping[str, str],
        attempts: list[CurrentStructuredFetchAttempt],
        manifests: list[Mapping[str, Any]],
        shared_cache_roots: Sequence[Path] = (),
        shared_cache_keys: Sequence[str] = (),
        cached_response_validator: Callable[[StructuredHTTPResponse], bool]
        | None = None,
    ) -> str | None:
        response, cache_hit, error = self._response(
            cache_key=cache_key,
            cache_root=cache_root,
            checkpoint_resume=checkpoint_resume,
            response_kind="text",
            request_url=url,
            request_params=params,
            shared_cache_roots=shared_cache_roots,
            shared_cache_keys=shared_cache_keys,
            cached_response_validator=cached_response_validator,
            fetch=lambda: self.transport.get_text(
                url=url,
                params=params,
                headers=headers,
                timeout_seconds=self.timeout_seconds,
            ),
        )
        text = response.text if response else None
        status = "FETCHED" if text else "PROVIDER_ERROR"
        attempts.append(
            _attempt(
                target_id=target_id,
                cutoff=cutoff,
                provider_name=provider_name,
                source_role=source_role,
                canonical_url=url,
                status=status,
                response=response,
                row_count=1 if text else 0,
                effective_date=None,
                cache_hit=cache_hit,
                error=error,
            )
        )
        if response and text:
            manifests.append(
                _manifest_row(
                    target_id=target_id,
                    cutoff=cutoff,
                    provider_name=provider_name,
                    source_role=source_role,
                    response=response,
                    row_count=1,
                    effective_date=None,
                )
            )
        return text

    def _response(
        self,
        *,
        cache_key: str,
        cache_root: Path,
        checkpoint_resume: bool,
        response_kind: str,
        request_url: str,
        request_params: Mapping[str, Any],
        fetch: Callable[[], StructuredHTTPResponse],
        shared_cache_roots: Sequence[Path] = (),
        shared_cache_keys: Sequence[str] = (),
        cached_response_validator: Callable[[StructuredHTTPResponse], bool]
        | None = None,
    ) -> tuple[StructuredHTTPResponse | None, bool, str | None]:
        cache_path = cache_root / f"{cache_key}.json"
        request_fingerprint = _structured_request_fingerprint(
            response_kind=response_kind,
            url=request_url,
            params=request_params,
        )
        if checkpoint_resume:
            candidates: list[Path] = [cache_path]
            reusable_keys = tuple(
                dict.fromkeys((cache_key, *shared_cache_keys))
            )
            for shared_root in shared_cache_roots:
                candidates.extend(
                    Path(shared_root) / f"{key}.json"
                    for key in reusable_keys
                )
            seen_paths: set[Path] = set()
            for candidate in candidates:
                if candidate in seen_paths or not candidate.is_file():
                    continue
                seen_paths.add(candidate)
                loaded = _load_structured_cache_response(
                    candidate,
                    response_kind=response_kind,
                    request_url=request_url,
                    request_fingerprint=request_fingerprint,
                    legacy_identity_allowed=(
                        candidate == cache_path
                        or candidate.stem in reusable_keys
                    ),
                )
                if loaded is None:
                    continue
                value, cached = loaded
                if cached_response_validator is not None:
                    try:
                        if not cached_response_validator(value):
                            continue
                    except (KeyError, TypeError, ValueError):
                        continue
                upgraded_cache = {
                    **cached,
                    "schema_version": (
                        _CURRENT_STRUCTURED_CACHE_SCHEMA_VERSION
                    ),
                    "request_fingerprint": request_fingerprint,
                }
                if candidate != cache_path:
                    upgraded_cache["shared_cache_reuse"] = True
                    upgraded_cache["shared_cache_source_content_hash"] = (
                        value.content_hash
                    )
                write_json(cache_path, upgraded_cache)
                return value, True, None
        try:
            value = fetch()
        except Exception as exc:
            return None, False, f"{type(exc).__name__}: {exc}"
        serialized = (
            json.dumps(value.payload, ensure_ascii=False, sort_keys=True)
            if response_kind == "json"
            else value.text or ""
        )
        write_json(
            cache_path,
            {
                "schema_version": _CURRENT_STRUCTURED_CACHE_SCHEMA_VERSION,
                "status_code": value.status_code,
                "canonical_url": value.canonical_url,
                "provider_request_id": value.provider_request_id,
                "content_hash": value.content_hash,
                "payload": dict(value.payload) if value.payload is not None else None,
                "text": value.text,
                "cache_value_hash": hashlib.sha256(
                    serialized.encode("utf-8")
                ).hexdigest(),
                "request_fingerprint": request_fingerprint,
            },
        )
        return value, False, None


def _structured_request_fingerprint(
    *,
    response_kind: str,
    url: str,
    params: Mapping[str, Any],
) -> str:
    """Hash source semantics without persisting API credentials.

    The fingerprint lets two targets in the same dated production lane reuse
    the exact same public structured snapshot.  Credential values are transport
    details, not data identity, and must never enter the cache artifact.
    """

    safe_params = {
        str(key): (
            "<credential>"
            if _request_parameter_is_credential(str(key))
            else value
        )
        for key, value in sorted(params.items(), key=lambda row: str(row[0]))
    }
    return stable_hash(
        {
            "schema_version": "e2r_v5_structured_request_identity_v1",
            "response_kind": response_kind,
            "url": str(url).split("?", 1)[0].rstrip("/"),
            "params": safe_params,
        }
    )


def _request_parameter_is_credential(key: str) -> bool:
    normalized = re.sub(r"[^a-z0-9]", "", key.casefold())
    return normalized in {
        "authkey",
        "crtfckey",
        "apikey",
        "servicekey",
        "token",
    } or normalized.endswith(("apikey", "authkey", "token"))


def _load_structured_cache_response(
    path: Path,
    *,
    response_kind: str,
    request_url: str,
    request_fingerprint: str,
    legacy_identity_allowed: bool,
) -> tuple[StructuredHTTPResponse, Mapping[str, Any]] | None:
    try:
        cached = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(cached, Mapping):
            return None
        cached_fingerprint = str(cached.get("request_fingerprint") or "")
        if cached_fingerprint:
            if cached_fingerprint != request_fingerprint:
                return None
        elif not legacy_identity_allowed:
            return None
        expected_url = str(request_url).split("?", 1)[0].rstrip("/")
        cached_url = str(cached["canonical_url"]).split("?", 1)[0].rstrip("/")
        if cached_url != expected_url:
            return None
        value = StructuredHTTPResponse(
            status_code=int(cached["status_code"]),
            canonical_url=str(cached["canonical_url"]),
            provider_request_id=str(cached["provider_request_id"]),
            content_hash=str(cached["content_hash"]),
            payload=(
                dict(cached["payload"])
                if isinstance(cached.get("payload"), Mapping)
                else None
            ),
            text=(
                str(cached["text"])
                if cached.get("text") is not None
                else None
            ),
        )
        if response_kind == "json" and value.payload is None:
            return None
        if response_kind == "text" and value.text is None:
            return None
        serialized = (
            json.dumps(value.payload, ensure_ascii=False, sort_keys=True)
            if response_kind == "json"
            else value.text or ""
        )
        if hashlib.sha256(serialized.encode("utf-8")).hexdigest() != str(
            cached.get("cache_value_hash") or ""
        ):
            return None
        return value, dict(cached)
    except (
        KeyError,
        OSError,
        TypeError,
        UnicodeError,
        ValueError,
        json.JSONDecodeError,
    ):
        return None


def _companyguide_cached_snapshot_is_point_in_time(
    response: StructuredHTTPResponse,
    *,
    cutoff: date,
    expected_company_name: str | None = None,
) -> bool:
    if not response.text:
        return False
    try:
        parsed = parse_companyguide_live_consensus_payload(
            response.text,
            as_of_date=cutoff,
        )
        if parsed.get("CONSENSUS_DATE_VERIFIED") is not True:
            return False
        observed = date.fromisoformat(
            str(parsed["CONSENSUS_AS_OF_DATE"]).replace("/", "-")[:10]
        )
    except (KeyError, TypeError, ValueError):
        return False
    if observed > cutoff:
        return False
    if expected_company_name is not None:
        actual_name = str(parsed.get("COMPANY_NAME") or "").strip()
        if not actual_name or _company_name_key(actual_name) != _company_name_key(
            expected_company_name
        ):
            return False
    return True


def _issuer_fact_route(
    *,
    target_id: str,
    cutoff: date,
    evidence_facts: Sequence[EvidenceFact | Mapping[str, Any]],
    source_claims: Sequence[Mapping[str, Any]],
    source_documents: Sequence[Mapping[str, Any]],
):
    """Promote only verified numeric fact claims into typed issuer rows.

    The LLM may nominate a semantic role, but this boundary independently
    verifies claim/fact/document lineage, exact-quote presence, source class,
    numeric shape, period, and point-in-time availability.  It never assigns a
    component score.
    """

    documents = _unique_rows_by_id(source_documents, "document_id")
    claims = _unique_rows_by_id(source_claims, "claim_id")
    segment_rows: list[SegmentFinancialObservation] = []
    guidance_rows: list[ForwardGuidanceObservation] = []
    metric_rows: list[StructuredMetricRecord] = []
    rejection_counts: dict[str, int] = {}
    tagged_claim_count = 0

    def reject(reason: str) -> None:
        rejection_counts[reason] = rejection_counts.get(reason, 0) + 1

    for raw_fact in evidence_facts:
        fact = _fact_mapping(raw_fact)
        fact_roles = {
            str(value).strip()
            for value in fact.get("structured_evidence_roles") or ()
            if str(value).strip() in _FACT_STRUCTURED_ROLES
        }
        if not fact_roles:
            continue
        if str(fact.get("target_id") or "") != target_id:
            reject("CROSS_TARGET_FACT")
            continue
        if str(fact.get("as_of_date") or "") != cutoff.isoformat():
            reject("FACT_AS_OF_MISMATCH")
            continue
        lifecycle = str(fact.get("current_lifecycle") or "")
        if lifecycle not in {"CURRENT", "OPEN"}:
            reject("FACT_NOT_CURRENT_OR_OPEN")
            continue
        fact_id = str(fact.get("fact_id") or "").strip()
        fact_source_ids = {
            str(value).strip()
            for value in fact.get("source_ids") or ()
            if str(value).strip()
        }
        claim_ids = tuple(
            str(value).strip()
            for value in fact.get("claim_ids") or ()
            if str(value).strip()
        )
        if not fact_id or not fact_source_ids or not claim_ids:
            reject("FACT_LINEAGE_INCOMPLETE")
            continue
        for claim_id in claim_ids:
            claim = claims.get(claim_id)
            if claim is None:
                reject("CLAIM_LINEAGE_UNAVAILABLE")
                continue
            roles = tuple(
                dict.fromkeys(
                    str(value).strip()
                    for value in claim.get("structured_evidence_roles") or ()
                    if str(value).strip() in _FACT_STRUCTURED_ROLES
                )
            )
            if not roles:
                continue
            tagged_claim_count += 1
            if not set(roles).issubset(fact_roles):
                reject("CLAIM_FACT_STRUCTURED_ROLE_MISMATCH")
                continue
            document_id = str(claim.get("document_id") or "").strip()
            document = documents.get(document_id)
            common_reason = _structured_claim_rejection(
                claim=claim,
                document=document,
                fact_source_ids=fact_source_ids,
                target_id=target_id,
                cutoff=cutoff,
            )
            if common_reason:
                reject(common_reason)
                continue
            assert document is not None
            source_family = str(document.get("source_family") or "").upper()
            observed_at = str(document.get("published_at") or "")[:10]
            available_at = str(document.get("available_at") or "")[:10]
            period = str(claim.get("period") or "").strip()
            parsed = _parse_reported_numeric(
                claim.get("value"), claim.get("unit")
            )
            confidence = min(
                _probability(fact.get("confidence"), default=0.0),
                _probability(claim.get("confidence"), default=0.0),
            )
            if parsed is None:
                for _ in roles:
                    reject("TAGGED_VALUE_NOT_MACHINE_NUMERIC")
                continue
            for role in roles:
                if role != "FORWARD_GUIDANCE" and lifecycle != "CURRENT":
                    reject(f"ROLE_REQUIRES_CURRENT_LIFECYCLE:{role}")
                    continue
                if role in {"SEGMENT_CONTRIBUTION", "FORWARD_GUIDANCE"}:
                    allowed_families = _ISSUER_STRUCTURED_SOURCE_FAMILIES
                else:
                    allowed_families = _QOQ_STRUCTURED_SOURCE_FAMILIES
                if source_family not in allowed_families:
                    reject(f"ROLE_SOURCE_FAMILY_NOT_ALLOWED:{role}")
                    continue
                if role == "SEGMENT_CONTRIBUTION":
                    segment_id = _meaningful_segment_id(claim)
                    if segment_id is None:
                        reject("SEGMENT_ID_NOT_SPECIFIC")
                        continue
                    if parsed.low is not None or parsed.high is not None:
                        reject("SEGMENT_VALUE_RANGE_AMBIGUOUS")
                        continue
                    segment_rows.append(
                        SegmentFinancialObservation(
                            target_id=target_id,
                            as_of_date=cutoff.isoformat(),
                            segment_id=segment_id,
                            metric_id=_metric_slug(
                                claim.get("predicate_family")
                                or claim.get("normalized_object")
                                or "segment_metric"
                            ),
                            value=parsed.midpoint,
                            unit=parsed.unit,
                            period=period,
                            observed_at=observed_at,
                            available_at=available_at,
                            source_ids=(document_id,),
                            source_route="ISSUER_GUIDANCE",
                            contribution_pct=(
                                parsed.midpoint
                                if parsed.unit == "PERCENT"
                                else None
                            ),
                            confidence=confidence,
                            metadata={
                                "fact_id": fact_id,
                                "claim_id": claim_id,
                                "exact_quote_verified": True,
                                "llm_role_nomination_only": True,
                                "structured_source": True,
                            },
                        )
                    )
                elif role == "QOQ_GROWTH":
                    if parsed.unit != "PERCENT" or parsed.low is not None:
                        reject("QOQ_REQUIRES_POINT_PERCENT")
                        continue
                    metric_rows.append(
                        StructuredMetricRecord(
                            record_id="STRUCT-" + stable_hash(
                                {
                                    "fact_id": fact_id,
                                    "claim_id": claim_id,
                                    "role": role,
                                    "value": parsed.midpoint,
                                }
                            )[:24],
                            target_id=target_id,
                            as_of_date=cutoff.isoformat(),
                            metric_id=_metric_slug(
                                claim.get("predicate_family")
                                or claim.get("normalized_object")
                                or "qoq_growth"
                            )
                            + "_qoq_pct",
                            value=parsed.midpoint,
                            unit="PERCENT",
                            period=period,
                            evidence_roles=("QOQ_GROWTH",),
                            source_ids=(document_id,),
                            source_route="ISSUER_GUIDANCE",
                            observed_at=observed_at,
                            available_at=available_at,
                            record_kind="SOURCE_BACKED_QOQ_GROWTH",
                            confidence=confidence,
                            dataset="FINANCIAL",
                            provenance="STRUCTURED_EXTRACTED",
                            metadata={
                                "fact_id": fact_id,
                                "claim_id": claim_id,
                                "exact_quote_verified": True,
                                "llm_role_nomination_only": True,
                                "structured_source": True,
                            },
                        )
                    )
                elif role == "FORWARD_GUIDANCE":
                    if not _period_is_forward(period, date.fromisoformat(available_at)):
                        reject("GUIDANCE_PERIOD_NOT_FORWARD")
                        continue
                    guidance_rows.append(
                        ForwardGuidanceObservation(
                            target_id=target_id,
                            as_of_date=cutoff.isoformat(),
                            metric_id=_metric_slug(
                                claim.get("predicate_family")
                                or claim.get("normalized_object")
                                or "issuer_outlook"
                            ),
                            unit=parsed.unit,
                            period=period,
                            observed_at=observed_at,
                            available_at=available_at,
                            source_ids=(document_id,),
                            source_route="ISSUER_GUIDANCE",
                            low_value=parsed.low,
                            high_value=parsed.high,
                            midpoint_value=(
                                None
                                if parsed.low is not None and parsed.high is not None
                                else parsed.midpoint
                            ),
                            guidance_status="ISSUER_GUIDANCE",
                            confidence=confidence,
                            metadata={
                                "fact_id": fact_id,
                                "claim_id": claim_id,
                                "exact_quote_verified": True,
                                "llm_role_nomination_only": True,
                                "structured_source": True,
                            },
                        )
                    )

    source_ids = tuple(
        sorted(
            {
                source_id
                for row in (*segment_rows, *guidance_rows, *metric_rows)
                for source_id in row.source_ids
            }
        )
    )
    accepted_count = len(segment_rows) + len(guidance_rows) + len(metric_rows)
    audit = {
        "schema_version": "e2r_v5_issuer_fact_materialization_audit_v1",
        "input_fact_count": len(evidence_facts),
        "input_claim_count": len(source_claims),
        "input_document_count": len(source_documents),
        "tagged_claim_count": tagged_claim_count,
        "segment_observation_count": len(segment_rows),
        "qoq_record_count": len(metric_rows),
        "guidance_observation_count": len(guidance_rows),
        "accepted_structured_observation_count": accepted_count,
        "rejection_counts": dict(sorted(rejection_counts.items())),
        "exact_quote_required": True,
        "numeric_value_required": True,
        "issuer_source_required_for_segment_and_guidance": True,
        "llm_score_authority": False,
    }
    if not accepted_count:
        return (
            UnavailableStructuredSourceRoute(
                "ISSUER_GUIDANCE",
                "no validated numeric issuer fact reached the structured boundary",
            ),
            audit,
        )
    payload = StructuredSourcePayload(
        route_name="ISSUER_GUIDANCE",
        source_ids=source_ids,
        structured_records=tuple(metric_rows),
        segment_observations=tuple(segment_rows),
        guidance_observations=tuple(guidance_rows),
        diagnostics=audit,
    )
    return InMemoryStructuredSourceRoute("ISSUER_GUIDANCE", payload), audit


def _unique_rows_by_id(
    rows: Sequence[Mapping[str, Any]], key: str
) -> Mapping[str, Mapping[str, Any]]:
    output: dict[str, Mapping[str, Any]] = {}
    for raw in rows:
        row = dict(raw)
        identity = str(row.get(key) or "").strip()
        if not identity:
            raise ValueError(f"structured fact input requires {key}")
        if identity in output and dict(output[identity]) != row:
            raise ValueError(f"structured fact input has conflicting {key}")
        output[identity] = row
    return output


def _fact_mapping(
    value: EvidenceFact | Mapping[str, Any],
) -> Mapping[str, Any]:
    if isinstance(value, EvidenceFact):
        return value.to_dict()
    return dict(value)


def _structured_claim_rejection(
    *,
    claim: Mapping[str, Any],
    document: Mapping[str, Any] | None,
    fact_source_ids: set[str],
    target_id: str,
    cutoff: date,
) -> str | None:
    if claim.get("accepted_by_evidence_os") is not True or claim.get("material") is not True:
        return "CLAIM_NOT_ACCEPTED_MATERIAL_EVIDENCE"
    if str(claim.get("target_id") or "") != target_id:
        return "CROSS_TARGET_CLAIM"
    if str(claim.get("as_of_date") or "") != cutoff.isoformat():
        return "CLAIM_AS_OF_MISMATCH"
    document_id = str(claim.get("document_id") or "").strip()
    if not document_id or document_id not in fact_source_ids:
        return "CLAIM_FACT_SOURCE_LINK_MISSING"
    if document is None:
        return "SOURCE_DOCUMENT_UNAVAILABLE"
    if str(document.get("target_id") or "") != target_id:
        return "CROSS_TARGET_SOURCE_DOCUMENT"
    if bool(document.get("snippet_only")) or not bool(
        document.get("full_fetch_performed")
    ):
        return "SOURCE_DOCUMENT_NOT_FULL_TEXT"
    if document.get("evidence_eligible") is not True:
        return "SOURCE_DOCUMENT_NOT_EVIDENCE_ELIGIBLE"
    exact_quote = str(claim.get("exact_quote") or "").strip()
    if not exact_quote or exact_quote not in str(document.get("content_text") or ""):
        return "EXACT_QUOTE_REVERIFICATION_FAILED"
    try:
        published = date.fromisoformat(str(document.get("published_at") or "")[:10])
        available = date.fromisoformat(str(document.get("available_at") or "")[:10])
    except ValueError:
        return "SOURCE_DOCUMENT_DATE_UNVERIFIED"
    if published > cutoff or available > cutoff:
        return "FUTURE_SOURCE_DOCUMENT"
    if available < published:
        return "SOURCE_AVAILABLE_BEFORE_PUBLISHED"
    return None


def _parse_reported_numeric(value: Any, unit: Any) -> _ParsedReportedNumeric | None:
    raw_value = str(value or "").strip()
    raw_unit = str(unit or "").strip()
    if not raw_value:
        return None
    combined = f"{raw_value} {raw_unit}".casefold()
    if any(
        marker in combined
        for marker in ("qualitative", "unknown", "n/a", "not disclosed", "비공개")
    ):
        return None
    normalized_value = re.sub(r"(?<=\d)\s*[-–—]\s*(?=\d)", "~", raw_value)
    tokens = re.findall(r"[-+]?\d[\d,]*(?:\.\d+)?", normalized_value)
    if not tokens or len(tokens) > 2:
        return None
    numbers = [_float(token) for token in tokens]
    if any(number is None for number in numbers):
        return None
    parsed_numbers = [float(number) for number in numbers if number is not None]
    if any(1900 <= abs(number) <= 2100 and number.is_integer() for number in parsed_numbers):
        return None
    if len(parsed_numbers) == 2 and not re.search(
        r"~|\bto\b|에서|부터|범위|range", normalized_value, flags=re.IGNORECASE
    ):
        return None
    multiplier = 1.0
    if "조원" in combined:
        multiplier = 1e12
        normalized_unit = "KRW"
    elif "억원" in combined:
        multiplier = 1e8
        normalized_unit = "KRW"
    elif "백만원" in combined:
        multiplier = 1e6
        normalized_unit = "KRW"
    elif "천원" in combined:
        multiplier = 1e3
        normalized_unit = "KRW"
    elif re.search(r"%|percent|pct|퍼센트", combined):
        normalized_unit = "PERCENT"
    elif re.search(r"\bkrw\b|원(?:\b|$)", combined):
        normalized_unit = "KRW"
    elif re.search(r"\busd\b|달러|\$", combined):
        normalized_unit = "USD"
    elif "배" in combined or "multiple" in combined:
        normalized_unit = "MULTIPLE"
    elif raw_unit:
        normalized_unit = _metric_slug(raw_unit).upper()
    else:
        normalized_unit = "NUMBER"
    scaled = [number * multiplier for number in parsed_numbers]
    if len(scaled) == 1:
        return _ParsedReportedNumeric(
            low=None,
            high=None,
            midpoint=scaled[0],
            unit=normalized_unit,
        )
    low, high = sorted(scaled)
    return _ParsedReportedNumeric(
        low=low,
        high=high,
        midpoint=(low + high) / 2.0,
        unit=normalized_unit,
    )


def _meaningful_segment_id(claim: Mapping[str, Any]) -> str | None:
    candidates = (
        claim.get("business_segment"),
        claim.get("scope_business_segment"),
        claim.get("product_family"),
        claim.get("scope_product_family"),
    )
    generic = {
        "",
        "CORE",
        "TOTAL",
        "COMPANY",
        "CONSOLIDATED",
        "ALL",
        "UNKNOWN",
        "N/A",
        "전체",
        "전사",
        "연결",
    }
    for value in candidates:
        text = str(value or "").strip()
        if text.upper() not in generic:
            return _metric_slug(text)
    return None


def _metric_slug(value: Any) -> str:
    text = re.sub(r"[^0-9A-Za-z가-힣]+", "_", str(value or "").strip())
    text = re.sub(r"_+", "_", text).strip("_").casefold()
    return text[:96] or "metric"


def _period_is_forward(period: str, available: date) -> bool:
    normalized = period.strip()
    if not normalized:
        return False
    if re.search(r"\b(next|forward|future|outlook)\b|향후|차기|다음", normalized, re.I):
        return True
    end = _period_end(normalized)
    return end is not None and end > available


def _period_end(period: str) -> date | None:
    normalized = period.upper().replace(" ", "")
    match = re.search(r"(20\d{2})[-/]?(?:Q([1-4])|([1-4])Q|([1-4])분기)", normalized)
    if match:
        year = int(match.group(1))
        quarter = int(next(value for value in match.groups()[1:] if value))
        month = quarter * 3
        return date(year, month, _month_end(year, month))
    match = re.search(r"(20\d{2})(?:H([12])|([12])H|상반기|하반기)", normalized)
    if match:
        year = int(match.group(1))
        half = (
            int(match.group(2) or match.group(3))
            if match.group(2) or match.group(3)
            else (1 if "상반기" in period else 2)
        )
        return date(year, 6 if half == 1 else 12, 30 if half == 1 else 31)
    match = re.fullmatch(r"(?:FY)?(20\d{2})(?:년)?", normalized)
    if match:
        return date(int(match.group(1)), 12, 31)
    match = re.fullmatch(r"(20\d{2})[-/](\d{1,2})(?:[-/](\d{1,2}))?", normalized)
    if match:
        year, month = int(match.group(1)), int(match.group(2))
        day = int(match.group(3)) if match.group(3) else _month_end(year, month)
        try:
            return date(year, month, day)
        except ValueError:
            return None
    return None


def _validated_peer_proposals(
    response: Mapping[str, Any], *, target_id: str
) -> tuple[Mapping[str, Any], ...]:
    if not isinstance(response, Mapping):
        raise TypeError("peer selection response must be an object")
    allowed_top = {
        "peers",
        "selection_complete",
        "unresolved_research_notes",
        "selection_rationale",
    }
    if set(response) != allowed_top:
        raise ValueError("peer selection response fields do not match contract")
    if response.get("selection_complete") is not True:
        raise ValueError("peer selection is incomplete")
    if not str(response.get("selection_rationale") or "").strip():
        raise ValueError("peer selection rationale is required")
    notes = response.get("unresolved_research_notes")
    if isinstance(notes, (str, bytes)) or not isinstance(notes, Sequence):
        raise TypeError("peer unresolved notes must be an array")
    peers = response.get("peers")
    if isinstance(peers, (str, bytes)) or not isinstance(peers, Sequence):
        raise TypeError("peer proposals must be an array")
    if not 2 <= len(peers) <= 5:
        raise ValueError("peer selection requires two to five proposals")
    required = {
        "peer_symbol",
        "peer_name",
        "shared_economic_drivers",
        "material_differences",
        "comparability_rationale",
        "confidence",
    }
    output: list[Mapping[str, Any]] = []
    seen: set[str] = set()
    for raw in peers:
        if not isinstance(raw, Mapping) or set(raw) != required:
            raise ValueError("peer proposal fields do not match contract")
        symbol = str(raw.get("peer_symbol") or "").strip()
        if not re.fullmatch(r"[0-9]{6}", symbol):
            raise ValueError("peer symbol must contain exactly six digits")
        if symbol == target_id:
            raise ValueError("target cannot be its own valuation peer")
        if symbol in seen:
            raise ValueError("peer symbols must be unique")
        seen.add(symbol)
        name = str(raw.get("peer_name") or "").strip()
        rationale = str(raw.get("comparability_rationale") or "").strip()
        shared = _nonempty_string_sequence(raw.get("shared_economic_drivers"))
        differences = _nonempty_string_sequence(raw.get("material_differences"))
        confidence = _probability(raw.get("confidence"), default=-1.0)
        if not name or not rationale or not shared or not differences:
            raise ValueError("peer proposal lacks economic comparability evidence")
        if confidence < 0.5:
            raise ValueError("peer proposal confidence is below validation threshold")
        output.append(
            {
                "peer_symbol": symbol,
                "peer_name": name,
                "shared_economic_drivers": shared,
                "material_differences": differences,
                "comparability_rationale": rationale,
                "confidence": confidence,
            }
        )
    return tuple(output)


def _nonempty_string_sequence(value: Any) -> tuple[str, ...]:
    if isinstance(value, (str, bytes)) or not isinstance(value, Sequence):
        raise TypeError("peer comparison fields must be arrays")
    rows = tuple(str(item).strip() for item in value)
    if any(not item for item in rows) or len(rows) != len(set(rows)):
        raise ValueError("peer comparison fields require unique nonempty text")
    return rows


def _latest_provider_prompt_hash(
    provider: StructuredResearchProvider, pass_name: str
) -> str | None:
    for row in reversed(tuple(getattr(provider, "calls", ()) or ())):
        if (
            isinstance(row, Mapping)
            and str(row.get("pass_name") or "") == pass_name
            and row.get("prompt_hash")
        ):
            return str(row["prompt_hash"])
    return None


def _company_name_key(value: Any) -> str:
    text = str(value or "").casefold()
    text = re.sub(r"주식회사|㈜|\(주\)|corp(?:oration)?|co\.?[,]?\s*ltd\.?", "", text)
    return re.sub(r"[^0-9a-z가-힣]", "", text)


def _mark_attempt_future_rejected(
    attempts: list[CurrentStructuredFetchAttempt],
    *,
    source_role: str,
    effective_date: str,
) -> None:
    for index in range(len(attempts) - 1, -1, -1):
        row = attempts[index]
        if row.source_role != source_role:
            continue
        attempts[index] = replace(
            row,
            status="FUTURE_REJECTED",
            effective_date=effective_date,
            error="structured snapshot is after as_of_date",
        )
        return


def _probability(value: Any, *, default: float) -> float:
    parsed = _float(value)
    if parsed is None or not 0.0 <= parsed <= 1.0:
        return default
    return parsed


@dataclass(frozen=True)
class _EmptyFinancialActualConnector:
    def get_financial_actuals(
        self, symbol: str, as_of_date: date
    ) -> tuple[Any, ...]:
        del symbol, as_of_date
        return ()


def write_current_structured_materialization(
    result: CurrentStructuredMaterializationResult,
    output_root: str | Path,
) -> Mapping[str, Path]:
    root = Path(output_root)
    paths = {
        key: root / filename for key, filename in CURRENT_STRUCTURED_OUTPUT_FILES.items()
    }
    write_jsonl(paths["fetch_attempts"], (row.to_dict() for row in result.fetch_attempts))
    write_jsonl(paths["payload_manifest"], result.payload_manifest)
    write_json(paths["result"], result.to_dict())
    write_json(paths["audit"], result.audit)
    return paths


def _official_corp_code(result: OfficialSourceMaterializationResult) -> str | None:
    for row in result.structured_payloads:
        if str(row.get("provider_name") or "") != "OpenDART":
            continue
        payload = row.get("payload")
        if isinstance(payload, Mapping) and str(payload.get("corp_code") or "").strip():
            raw = str(payload["corp_code"]).strip()
            return raw.zfill(8) if raw.isdigit() else raw
    return None


def _financial_statement_periods(cutoff: date) -> tuple[Mapping[str, Any], ...]:
    candidates = (
        (cutoff.year, 1, date(cutoff.year, 3, 31), "11013", date(cutoff.year, 5, 16)),
        (cutoff.year, 2, date(cutoff.year, 6, 30), "11012", date(cutoff.year, 8, 16)),
        (cutoff.year, 3, date(cutoff.year, 9, 30), "11014", date(cutoff.year, 11, 16)),
    )
    periods: list[Mapping[str, Any]] = []
    available_quarters = [row for row in candidates if row[4] <= cutoff]
    for fiscal_year, quarter, period_end, report_code, reported_at in available_quarters:
        periods.append(
            {
                "fiscal_year": fiscal_year,
                "fiscal_quarter": quarter,
                "period_end": period_end,
                "report_code": report_code,
                "reported_at": reported_at,
            }
        )
    if available_quarters:
        fiscal_year, quarter, _, report_code, _ = available_quarters[-1]
        prior_year = fiscal_year - 1
        reported_month_day = {1: (5, 16), 2: (8, 16), 3: (11, 16)}[quarter]
        periods.append(
            {
                "fiscal_year": prior_year,
                "fiscal_quarter": quarter,
                "period_end": date(prior_year, quarter * 3, _month_end(prior_year, quarter * 3)),
                "report_code": report_code,
                "reported_at": date(prior_year, *reported_month_day),
            }
        )
    for fiscal_year in (cutoff.year - 1, cutoff.year - 2, cutoff.year - 3):
        reported_at = date(fiscal_year + 1, 4, 1)
        if reported_at <= cutoff:
            periods.append(
                {
                    "fiscal_year": fiscal_year,
                    "fiscal_quarter": None,
                    "period_end": date(fiscal_year, 12, 31),
                    "report_code": "11011",
                    "reported_at": reported_at,
                }
            )
    return tuple(periods)


def _month_end(year: int, month: int) -> int:
    if month == 2:
        return 29 if year % 4 == 0 and (year % 100 or year % 400 == 0) else 28
    return 30 if month in {4, 6, 9, 11} else 31


def _companyguide_consensus_snapshot(
    *, target_id: str, cutoff: date, payload: Mapping[str, Any]
) -> ConsensusSnapshot | None:
    if payload.get("CONSENSUS_DATE_VERIFIED") is not True:
        return None
    raw_date = str(payload.get("CONSENSUS_AS_OF_DATE") or "").replace("/", "-")[:10]
    try:
        observed = date.fromisoformat(raw_date)
    except ValueError:
        return None
    if observed > cutoff:
        return None
    eps = _float(payload.get("FORWARD_12M_EPS") or payload.get("EPS"))
    per = _float(payload.get("FORWARD_12M_PER") or payload.get("FORWARD_PER"))
    bps = _float(payload.get("FORWARD_12M_BPS"))
    pbr = _float(payload.get("FORWARD_12M_PBR"))
    if all(value is None for value in (eps, per, bps, pbr)):
        return None
    return ConsensusSnapshot(
        symbol=target_id,
        date=observed,
        fiscal_year=cutoff.year,
        as_of_date=cutoff,
        source="company_guide_forward_12m",
        eps_e=eps,
        bps_e=bps,
        per_e=per,
        pbr_e=pbr,
        analyst_count=_int(payload.get("CONSENSUS_PROVIDER_COUNT")),
        target_price=_float(payload.get("TARGET_PRC")),
        parsed_fields={
            "structured_consensus_source": True,
            "forward_horizon": "FWD_12M",
            "ebitda_e": _float(payload.get("FORWARD_12M_EBITDA")),
            "ev_ebitda_e": _float(payload.get("FORWARD_12M_EV_EBITDA")),
            "currency_unit": "KRW",
            "source_page_date": observed.isoformat(),
        },
    )


def _enrich_report(row: ResearchReport) -> ResearchReport:
    est_per = row.est_per
    if (
        est_per is None
        and row.current_price is not None
        and row.fy1_eps is not None
        and row.current_price > 0
        and row.fy1_eps > 0
    ):
        est_per = row.current_price / row.fy1_eps
    parsed = dict(row.parsed_fields)
    if est_per is not None and row.est_per is None:
        parsed["est_per_formula"] = "report_close_price / report_fy1_eps"
        parsed["est_per_derived_from_structured_report_fields"] = True
    return replace(row, est_per=est_per, parsed_fields=parsed)


def _report_consensus_snapshots(
    reports: Sequence[ResearchReport], *, target_id: str, cutoff: date
) -> tuple[ConsensusSnapshot, ...]:
    rows: list[ConsensusSnapshot] = []
    for report in reports:
        op_value = _explicit_annual_operating_profit(report.raw_text or "", cutoff.year)
        if report.fy1_eps is None and op_value is None:
            continue
        rows.append(
            ConsensusSnapshot(
                symbol=target_id,
                date=report.publish_date,
                fiscal_year=cutoff.year,
                as_of_date=cutoff,
                source=f"company_guide_report:{report.broker}",
                op_e=op_value,
                eps_e=report.fy1_eps,
                per_e=report.est_per,
                target_price=report.target_price,
                parsed_fields={
                    "structured_consensus_source": True,
                    "structured_consensus_revision_source": True,
                    "fiscal_quarter": "ANNUAL",
                    "report_id": report.parsed_fields.get("report_id"),
                    "broker": report.broker,
                },
            )
        )
    return tuple(rows)


def _report_direction_records(
    reports: Sequence[ResearchReport],
    *,
    target_id: str,
    cutoff: date,
    source_id: str,
) -> tuple[StructuredMetricRecord, ...]:
    records: list[StructuredMetricRecord] = []
    for report in reports:
        report_id = str(
            report.parsed_fields.get("report_id")
            or stable_hash((report.broker, report.publish_date.isoformat(), report.title))[:16]
        )
        directions: list[tuple[str, str, str]] = []
        eps_direction = str(
            report.parsed_fields.get("eps_revision_direction") or ""
        ).upper()
        if eps_direction in {"UP", "DOWN", "UNCHANGED"}:
            directions.append(("eps_revision_direction", eps_direction, "EPS_REVISION"))
        op_direction = _operating_profit_revision_direction(report.raw_text or "")
        if op_direction:
            directions.append(
                (
                    "operating_profit_revision_direction",
                    op_direction,
                    "OPERATING_PROFIT_REVISION",
                )
            )
        surprise = _earnings_surprise_direction(report.raw_text or "")
        if surprise:
            directions.append(
                ("earnings_surprise_direction", surprise, "EARNINGS_SURPRISE")
            )
        for metric_id, value, role in directions:
            records.append(
                StructuredMetricRecord(
                    record_id="STRUCT-" + stable_hash(
                        {
                            "target_id": target_id,
                            "report_id": report_id,
                            "metric_id": metric_id,
                            "value": value,
                        }
                    )[:24],
                    target_id=target_id,
                    as_of_date=cutoff.isoformat(),
                    metric_id=metric_id,
                    value=value,
                    unit="DIRECTION",
                    period=report.publish_date.isoformat(),
                    evidence_roles=(role,),
                    source_ids=(source_id,),
                    source_route="COMPANYGUIDE",
                    observed_at=report.publish_date.isoformat(),
                    available_at=report.publish_date.isoformat(),
                    record_kind="STRUCTURED_BROKER_REPORT_DIRECTION",
                    confidence=0.82,
                    dataset="CONSENSUS_REVISION",
                    provenance="STRUCTURED_EXTRACTED",
                    metadata={
                        "structured_source": True,
                        "report_id": report_id,
                        "broker": report.broker,
                        "title": report.title,
                        "numeric_magnitude_invented": False,
                    },
                )
            )
    return tuple(records)


def _explicit_annual_operating_profit(text: str, fiscal_year: int) -> float | None:
    year = str(fiscal_year)
    patterns = (
        rf"(?:FY\s*{year[-2:]}|{year}년)[^\n]{{0,45}}?영업이익(?:은|을|이)?\s*"
        rf"([0-9][0-9,.]*)\s*(조원|억원|백만원)",
        rf"영업이익(?:은|을|이)?\s*([0-9][0-9,.]*)\s*(조원|억원|백만원)"
        rf"[^\n]{{0,45}}?(?:FY\s*{year[-2:]}|{year}년)",
    )
    for pattern in patterns:
        match = re.search(pattern, text, flags=re.IGNORECASE)
        if not match:
            continue
        value = _float(match.group(1))
        if value is None:
            continue
        return value * {"조원": 1e12, "억원": 1e8, "백만원": 1e6}[match.group(2)]
    return None


def _operating_profit_revision_direction(text: str) -> str | None:
    compact = " ".join(text.split())
    patterns = (
        r"영업이익\s*(?:전망치|추정치)(?:를|은|는)?[^▶\n]{0,120}?(상향|하향|유지)",
        r"영업이익[^▶\n]{0,120}?직전\s*대비\s*(상향|하향|유지)",
    )
    for pattern in patterns:
        match = re.search(pattern, compact, flags=re.IGNORECASE)
        if match:
            return {"상향": "UP", "하향": "DOWN", "유지": "UNCHANGED"}[
                match.group(1)
            ]
    return None


def _earnings_surprise_direction(text: str) -> str | None:
    match = re.search(
        r"(?:컨센서스|시장\s*기대치|기대치)[^。.!?\n]{0,35}?(상회|하회|부합)",
        " ".join(text.split()),
    )
    if not match:
        return None
    return {"상회": "ABOVE", "하회": "BELOW", "부합": "IN_LINE"}[
        match.group(1)
    ]


def _data_go_items(payload: Mapping[str, Any]) -> tuple[Mapping[str, Any], ...]:
    response = payload.get("response", payload)
    body = response.get("body", response) if isinstance(response, Mapping) else {}
    items = body.get("items", ()) if isinstance(body, Mapping) else ()
    rows = items.get("item", ()) if isinstance(items, Mapping) else items
    if isinstance(rows, Mapping):
        rows = (rows,)
    if not isinstance(rows, Sequence) or isinstance(rows, (str, bytes)):
        return ()
    return tuple(row for row in rows if isinstance(row, Mapping))


def _data_go_total_pages(payload: Mapping[str, Any], *, rows_per_page: int) -> int:
    response = payload.get("response", payload)
    body = response.get("body", response) if isinstance(response, Mapping) else {}
    if not isinstance(body, Mapping):
        return 1
    total = _int(body.get("totalCount")) or 0
    per_page = _int(body.get("numOfRows")) or rows_per_page
    return max(1, math.ceil(total / per_page)) if total > 0 and per_page > 0 else 1


def _krx_stock_bar(
    row: Mapping[str, Any], *, target_id: str, cutoff: date
) -> PriceBar | None:
    try:
        observed = datetime.strptime(str(row["BAS_DD"]), "%Y%m%d").date()
        if observed > cutoff:
            return None
        return PriceBar(
            symbol=target_id,
            date=observed,
            open=float(str(row["TDD_OPNPRC"]).replace(",", "")),
            high=float(str(row["TDD_HGPRC"]).replace(",", "")),
            low=float(str(row["TDD_LWPRC"]).replace(",", "")),
            close=float(str(row["TDD_CLSPRC"]).replace(",", "")),
            adj_close=float(str(row["TDD_CLSPRC"]).replace(",", "")),
            volume=int(str(row.get("ACC_TRDVOL") or "0").replace(",", "")),
            trading_value=float(
                str(row.get("ACC_TRDVAL") or "0").replace(",", "")
            ),
            market_cap=float(str(row["MKTCAP"]).replace(",", "")),
            source="KRX OpenAPI daily stock trading",
            as_of_date=cutoff,
        )
    except (KeyError, TypeError, ValueError):
        return None


def _krx_index_bar(
    row: Mapping[str, Any] | None, *, market: str, cutoff: date
) -> PriceBar | None:
    if row is None:
        return None
    try:
        observed = datetime.strptime(str(row["BAS_DD"]), "%Y%m%d").date()
        if observed > cutoff:
            return None
        return PriceBar(
            symbol=f"KRX:{market}",
            date=observed,
            open=float(str(row["OPNPRC_IDX"]).replace(",", "")),
            high=float(str(row["HGPRC_IDX"]).replace(",", "")),
            low=float(str(row["LWPRC_IDX"]).replace(",", "")),
            close=float(str(row["CLSPRC_IDX"]).replace(",", "")),
            adj_close=float(str(row["CLSPRC_IDX"]).replace(",", "")),
            volume=int(str(row.get("ACC_TRDVOL") or "0").replace(",", "")),
            trading_value=float(
                str(row.get("ACC_TRDVAL") or "0").replace(",", "")
            ),
            market_cap=float(str(row.get("MKTCAP") or "0").replace(",", "")),
            source="KRX OpenAPI daily index trading",
            as_of_date=cutoff,
        )
    except (KeyError, TypeError, ValueError):
        return None


def _dedupe_price_bars(
    rows: Sequence[PriceBar], *, target_id: str
) -> tuple[PriceBar, ...]:
    selected: dict[tuple[str, date], PriceBar] = {}
    for row in rows:
        key = (row.symbol, row.date)
        current = selected.get(key)
        if current is None or (
            row.symbol == target_id
            and row.source.startswith("KRX")
            and not current.source.startswith("KRX")
        ):
            selected[key] = row
    return tuple(sorted(selected.values(), key=lambda row: (row.symbol, row.date)))


def _attempt(
    *,
    target_id: str,
    cutoff: date,
    provider_name: str,
    source_role: str,
    canonical_url: str,
    status: str,
    response: StructuredHTTPResponse | None,
    row_count: int,
    effective_date: str | None,
    cache_hit: bool,
    error: str | None,
) -> CurrentStructuredFetchAttempt:
    identity = {
        "target_id": target_id,
        "as_of_date": cutoff.isoformat(),
        "provider_name": provider_name,
        "source_role": source_role,
        "canonical_url": canonical_url,
        "effective_date": effective_date,
        "content_hash": response.content_hash if response else None,
    }
    return CurrentStructuredFetchAttempt(
        attempt_id="STRUCTFETCH-" + stable_hash(identity)[:24],
        target_id=target_id,
        as_of_date=cutoff.isoformat(),
        provider_name=provider_name,
        source_role=source_role,
        canonical_url=canonical_url,
        status=status,
        provider_request_id=response.provider_request_id if response else None,
        content_hash=response.content_hash if response else None,
        row_count=row_count,
        effective_date=effective_date,
        cache_hit=cache_hit,
        error=error,
    )


def _failed_attempt(
    target_id: str,
    cutoff: date,
    provider_name: str,
    source_role: str,
    canonical_url: str,
    status: str,
    error: str,
) -> CurrentStructuredFetchAttempt:
    return _attempt(
        target_id=target_id,
        cutoff=cutoff,
        provider_name=provider_name,
        source_role=source_role,
        canonical_url=canonical_url,
        status=status,
        response=None,
        row_count=0,
        effective_date=None,
        cache_hit=False,
        error=error,
    )


def _manifest_row(
    *,
    target_id: str,
    cutoff: date,
    provider_name: str,
    source_role: str,
    response: StructuredHTTPResponse,
    row_count: int,
    effective_date: str | None,
) -> Mapping[str, Any]:
    source_id = "STRUCTSRC-" + stable_hash(
        {
            "provider_name": provider_name,
            "canonical_url": response.canonical_url,
            "content_hash": response.content_hash,
        }
    )[:24]
    return {
        "schema_version": "e2r_v5_current_structured_payload_manifest_v1",
        "source_id": source_id,
        "target_id": target_id,
        "as_of_date": cutoff.isoformat(),
        "provider_name": provider_name,
        "source_role": source_role,
        "canonical_url": response.canonical_url,
        "provider_request_id": response.provider_request_id,
        "content_hash": response.content_hash,
        "row_count": row_count,
        "effective_date": effective_date,
        "secret_material_persisted": False,
        "production_score_authority": False,
    }


def _float(value: Any) -> float | None:
    if value in (None, ""):
        return None
    try:
        parsed = float(str(value).replace(",", ""))
    except (TypeError, ValueError):
        return None
    return parsed if math.isfinite(parsed) else None


def _int(value: Any) -> int | None:
    parsed = _float(value)
    return int(parsed) if parsed is not None else None


__all__ = [
    "CURRENT_STRUCTURED_OUTPUT_FILES",
    "FACT_STRUCTURED_ROLE_RESOLUTION_CONTRACTS",
    "CurrentStructuredFetchAttempt",
    "CurrentStructuredMaterializationResult",
    "CurrentStructuredSourceMaterializer",
    "RequestsCurrentStructuredHTTPTransport",
    "StructuredHTTPResponse",
    "write_current_structured_materialization",
]
