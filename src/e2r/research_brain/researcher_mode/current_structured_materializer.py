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
    parse_companyguide_live_page_metadata,
)
from e2r.research_brain.planning.provider_transport import (
    StructuredProviderUnavailable,
)
from e2r.sources.company_guide import CompanyGuideConnector
from e2r.sources.opendart import OpenDARTConnector

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
_DART_DISCLOSURE_LIST_URL = "https://opendart.fss.or.kr/api/list.json"
_DART_CORP_CODE_URL = "https://opendart.fss.or.kr/api/corpCode.xml"
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
    "report_candidates": "current_structured_report_candidates.jsonl",
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
    report_candidates: tuple[Mapping[str, Any], ...] = ()
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
            "report_candidates": [dict(row) for row in self.report_candidates],
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


def _invalidate_structured_peer_response_cache(
    provider: StructuredResearchProvider,
    *,
    proposal_failures: Sequence[str],
) -> Mapping[str, Any] | None:
    """Quarantine a schema-valid peer response rejected by source verification."""

    invalidate = getattr(provider, "invalidate_last_response_cache", None)
    if not callable(invalidate):
        return None
    reason = (
        "STRUCTURED_PEER_SOURCE_VERIFICATION_REJECTED:"
        + ",".join(str(value) for value in proposal_failures)
    )[-500:]
    try:
        result = invalidate(reason=reason)
    except (OSError, TypeError, ValueError, RuntimeError):
        return None
    return dict(result) if isinstance(result, Mapping) else None


def _invalidate_peer_validation_response_cache(
    provider: StructuredResearchProvider,
    *,
    rejection_phase: str,
    rejection_error: Exception,
) -> Mapping[str, Any] | None:
    """Quarantine a provider response rejected before source verification."""

    invalidate = getattr(provider, "invalidate_last_response_cache", None)
    if not callable(invalidate):
        return None
    reason = (
        "STRUCTURED_PEER_RESPONSE_VALIDATION_REJECTED:"
        f"{rejection_phase}:"
        + " ".join(str(rejection_error).split())
    )[-500:]
    try:
        result = invalidate(reason=reason)
    except (OSError, TypeError, ValueError, RuntimeError):
        return None
    return dict(result) if isinstance(result, Mapping) else None


def _recover_validated_peer_selection_retry_payload(
    provider: StructuredResearchProvider,
    *,
    primary_payload: Mapping[str, Any],
) -> Mapping[str, Any] | None:
    """Recover a journal-bound retry after a clean-process primary replay."""

    recover = getattr(
        provider,
        "validated_peer_selection_retry_payload",
        None,
    )
    if not callable(recover):
        return None
    try:
        recovered = recover(primary_payload=primary_payload)
    except (OSError, TypeError, ValueError, RuntimeError):
        return None
    if not isinstance(recovered, Mapping):
        return None
    retry_context = recovered.get("peer_selection_retry_context")
    if (
        not isinstance(retry_context, Mapping)
        or set(retry_context) != {"validation_error", "instruction"}
        or not isinstance(retry_context.get("validation_error"), str)
        or not str(retry_context["validation_error"]).strip()
        or retry_context.get("instruction")
        != (
            "Rewrite the complete peer selection under the original "
            "two-to-five peer contract; do not invent any valuation values."
        )
    ):
        return None
    return dict(recovered)


def _delete_peer_selection_route_cache(
    selection_cache_path: Path,
    *,
    reason: str,
) -> Mapping[str, Any]:
    cache_entry_existed = selection_cache_path.is_file()
    try:
        selection_cache_path.unlink(missing_ok=True)
        cache_entry_deleted = cache_entry_existed
    except OSError:
        cache_entry_deleted = False
    return {
        "cache_path": str(selection_cache_path),
        "cache_entry_existed": cache_entry_existed,
        "cache_entry_deleted": cache_entry_deleted,
        "reason": reason,
    }


class CurrentStructuredSourceMaterializer:
    """Collect every canonical structured route and fail closed on gaps."""

    def __init__(
        self,
        *,
        transport: CurrentStructuredHTTPTransport | None = None,
        timeout_seconds: float = 30.0,
        price_lookback_days: int = 1_825,
        companyguide_report_rows: int = 100,
        companyguide_report_max_pages: int = 3,
        companyguide_report_max_candidates: int = 300,
        peer_provider: StructuredResearchProvider | None = None,
        opendart_corp_code_cache_root: str | Path = (
            "data/cache/opendart_corp_code"
        ),
        opendart_corp_code_max_archives: int = 3,
    ) -> None:
        if timeout_seconds <= 0 or timeout_seconds > 120:
            raise ValueError("structured source timeout must be bounded")
        if price_lookback_days < 370:
            raise ValueError("structured price history must cover at least one year")
        if companyguide_report_rows <= 0 or companyguide_report_rows > 100:
            raise ValueError("CompanyGuide report rows exceed provider page maximum")
        if companyguide_report_max_pages <= 0 or companyguide_report_max_pages > 20:
            raise ValueError("CompanyGuide report pagination must be explicitly bounded")
        if (
            companyguide_report_max_candidates <= 0
            or companyguide_report_max_candidates > 2_000
        ):
            raise ValueError("CompanyGuide report candidate budget is invalid")
        if not 1 <= opendart_corp_code_max_archives <= 10:
            raise ValueError("OpenDART corp-code archive scan must be bounded")
        self.transport = transport or RequestsCurrentStructuredHTTPTransport()
        self.timeout_seconds = timeout_seconds
        self.price_lookback_days = price_lookback_days
        self.companyguide_report_rows = companyguide_report_rows
        self.companyguide_report_max_pages = companyguide_report_max_pages
        self.companyguide_report_max_candidates = companyguide_report_max_candidates
        self.peer_provider = peer_provider
        self.opendart_corp_code_cache_root = Path(opendart_corp_code_cache_root)
        self.opendart_corp_code_max_archives = opendart_corp_code_max_archives

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
        report_candidates: list[Mapping[str, Any]] = []
        companyguide_report_audit: dict[str, Any] = {}

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
            report_candidates=report_candidates,
            report_pagination_audit=companyguide_report_audit,
        )
        (
            price_route,
            listing_identity_roster,
            listing_identity_roster_audit,
            peer_price_rows,
        ) = self._price_route(
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
            listing_identity_roster=listing_identity_roster,
            listing_identity_roster_audit=listing_identity_roster_audit,
            listing_snapshot_date=trading_date,
            peer_price_rows=peer_price_rows,
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
            "report_candidate_count": len(report_candidates),
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
            "companyguide_report_history": companyguide_report_audit,
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
            report_candidates=tuple(report_candidates),
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
        report_candidates: list[Mapping[str, Any]],
        report_pagination_audit: dict[str, Any],
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
        report_pages: list[tuple[Mapping[str, Any], str, int]] = []
        selected_candidate_count = 0
        fetched_page_count = 0
        provider_total_pages: int | None = None
        stop_reason = "MAX_PAGES_REACHED"
        for page_number in range(1, self.companyguide_report_max_pages + 1):
            manifest_start = len(manifests)
            reports_payload = self._json(
                target_id=target_id,
                cutoff=cutoff,
                provider_name="CompanyGuide",
                source_role="BROKER_REPORT_HISTORY",
                cache_key=(
                    f"companyguide_reports_{target_id}"
                    if page_number == 1
                    else f"companyguide_reports_{target_id}_page_{page_number}"
                ),
                cache_root=cache_root,
                checkpoint_resume=checkpoint_resume,
                url=_COMPANYGUIDE_REPORTS_URL,
                params={
                    "cmp_cd": target_id,
                    "perPage": self.companyguide_report_rows,
                    "curPage": page_number,
                },
                headers={"User-Agent": "Mozilla/5.0 E2R-ResearcherMode/5.0"},
                attempts=attempts,
                manifests=manifests,
                rows_getter=lambda value: value.get("lists") or (),
            )
            if reports_payload is None:
                stop_reason = "PROVIDER_ERROR"
                break
            fetched_page_count += 1
            raw_rows = tuple(
                row
                for row in reports_payload.get("lists") or ()
                if isinstance(row, Mapping)
            )
            declared_total_pages = _int(reports_payload.get("tp"))
            if declared_total_pages is not None and declared_total_pages > 0:
                provider_total_pages = declared_total_pages
            page_source_id = next(
                (
                    str(row["source_id"])
                    for row in reversed(manifests[manifest_start:])
                    if row.get("provider_name") == "CompanyGuide"
                    and row.get("source_role") == "BROKER_REPORT_HISTORY"
                ),
                "",
            )
            if not raw_rows:
                stop_reason = "PROVIDER_PAGE_EMPTY"
                break
            remaining = (
                self.companyguide_report_max_candidates - selected_candidate_count
            )
            selected_rows = raw_rows[:remaining]
            selected_candidate_count += len(selected_rows)
            if selected_rows and page_source_id:
                report_pages.append(
                    ({"lists": list(selected_rows)}, page_source_id, page_number)
                )
            if len(selected_rows) < len(raw_rows) or (
                selected_candidate_count
                >= self.companyguide_report_max_candidates
            ):
                stop_reason = "MAX_CANDIDATES_REACHED"
                break
            if provider_total_pages is None:
                # Older/fixture payloads do not expose tp.  One page remains a
                # bounded, fail-closed read instead of guessing more pages.
                stop_reason = "PROVIDER_TOTAL_PAGES_UNKNOWN_SINGLE_PAGE"
                break
            if page_number >= provider_total_pages:
                stop_reason = "PROVIDER_TOTAL_PAGES_REACHED"
                break
        provider_archive_exhausted = stop_reason in {
            "PROVIDER_PAGE_EMPTY",
            "PROVIDER_TOTAL_PAGES_REACHED",
        }
        source_ids = tuple(
            dict.fromkeys(
                row["source_id"]
                for row in manifests
                if row["provider_name"] == "CompanyGuide"
            )
        )
        snapshots: list[ConsensusSnapshot] = []
        parsed_report_rows: list[ResearchReport] = []
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
            snapshot_source_id = next(
                (
                    str(row["source_id"])
                    for row in reversed(manifests)
                    if row.get("provider_name") == "CompanyGuide"
                    and row.get("source_role")
                    == "CONSENSUS_VALUATION_SNAPSHOT"
                ),
                "",
            )
            if snapshot_source_id:
                seed_records.extend(
                    _companyguide_trailing_valuation_records(
                        target_id=target_id,
                        cutoff=cutoff,
                        payload=parsed,
                        source_id=snapshot_source_id,
                    )
                )
        for reports_payload, report_source_id, page_number in report_pages:
            try:
                parsed_reports = CompanyGuideConnector.parse_recent_reports_payload(
                    reports_payload,
                    symbol=target_id,
                    as_of_date=cutoff,
                )
            except (TypeError, ValueError, json.JSONDecodeError):
                parsed_reports = ()
            for report in parsed_reports:
                parsed_report_rows.append(
                    _enrich_report(
                        replace(
                            report,
                            parsed_fields={
                                **dict(report.parsed_fields),
                                "structured_page_source_id": report_source_id,
                                "provider_page": page_number,
                            },
                        )
                    )
                )
        reports, duplicate_report_count = _dedupe_companyguide_reports(
            parsed_report_rows
        )
        if reports:
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
                )
            )
            known_candidate_ids = {
                str(row.get("candidate_id") or "") for row in report_candidates
            }
            for report in reports:
                candidate = _companyguide_report_source_candidate(
                    report,
                    target_id=target_id,
                    cutoff=cutoff,
                )
                if candidate is None or candidate["candidate_id"] in known_candidate_ids:
                    continue
                report_candidates.append(candidate)
                known_candidate_ids.add(str(candidate["candidate_id"]))
        report_pagination_audit.update(
            {
                "schema_version": "e2r_v5_companyguide_report_pagination_audit_v1",
                "status": (
                    "REPORT_CANDIDATE_HANDOFF_READY"
                    if report_candidates
                    else "REPORT_CANDIDATE_HANDOFF_EMPTY"
                ),
                "max_pages": self.companyguide_report_max_pages,
                "max_candidates": self.companyguide_report_max_candidates,
                "results_per_page": self.companyguide_report_rows,
                "fetched_page_count": fetched_page_count,
                "selected_candidate_count": selected_candidate_count,
                "eligible_report_count": len(reports),
                "duplicate_report_count": duplicate_report_count,
                "handoff_candidate_count": len(report_candidates),
                "provider_total_pages": provider_total_pages,
                "stop_reason": stop_reason,
                "provider_archive_exhausted": provider_archive_exhausted,
                "bounded_pagination": True,
                "full_document_owner": "LLM_SOURCE_GRAPH",
                "full_document_fetch_performed": False,
                "deterministic_url_or_query_synthesis": False,
            }
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
                "direction_record_count": sum(
                    row.record_kind == "STRUCTURED_BROKER_REPORT_DIRECTION"
                    for row in seed_records
                ),
                "trailing_valuation_record_count": sum(
                    row.record_kind == "PROVIDER_TRAILING_VALUATION_SNAPSHOT"
                    for row in seed_records
                ),
                "report_candidate_count": len(report_candidates),
                "report_pagination_stop_reason": stop_reason,
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
        listing_identity_rows: list[Mapping[str, str]] = []
        peer_price_rows: list[Mapping[str, Any]] = []
        required_listing_markets = tuple(_KRX_STOCK_URLS)
        complete_listing_markets: list[str] = []
        listing_market_details: dict[str, Mapping[str, Any]] = {}
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
                manifest_start = len(manifests)
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
                    listing_market_details[candidate_market] = {
                        "status": "PROVIDER_ERROR",
                        "exact_snapshot_row_count": 0,
                        "identity_count": 0,
                        "source_id": None,
                    }
                    continue
                raw_rows = payload.get("OutBlock_1") or ()
                exact_snapshot_rows = tuple(
                    row
                    for row in raw_rows
                    if isinstance(row, Mapping)
                    and str(row.get("BAS_DD") or "")
                    == trading_date.strftime("%Y%m%d")
                )
                snapshot_accounting = _krx_listing_snapshot_accounting(
                    payload,
                    target_id=target_id,
                    snapshot_date=trading_date,
                )
                market_identities = tuple(
                    dict(row)
                    for row in snapshot_accounting.get("identities") or ()
                )
                market_source_id = next(
                    (
                        str(row["source_id"])
                        for row in manifests[manifest_start:]
                        if row.get("provider_name") == "KRX"
                        and row.get("source_role")
                        == "CURRENT_PRICE_MARKET_CAP"
                        and row.get("canonical_url") == url
                    ),
                    None,
                )
                market_snapshot_complete = (
                    snapshot_accounting.get("complete_identity_plane") is True
                    and market_source_id is not None
                )
                listing_market_details[candidate_market] = {
                    "status": (
                        "COMPLETE"
                        if market_snapshot_complete
                        else "IDENTITY_PLANE_INCOMPLETE"
                    ),
                    **{
                        key: value
                        for key, value in snapshot_accounting.items()
                        if key != "identities"
                    },
                    "source_id": market_source_id,
                }
                if not market_snapshot_complete:
                    continue
                complete_listing_markets.append(candidate_market)
                listing_identity_rows.extend(
                    market_identities
                )
                identity_names = {
                    str(row["peer_symbol"]): str(row["peer_name"])
                    for row in market_identities
                }
                for row in exact_snapshot_rows:
                    symbol = str(
                        row.get("ISU_CD") or row.get("ISU_SRT_CD") or ""
                    )
                    close = _float(row.get("TDD_CLSPRC"))
                    market_cap = _float(row.get("MKTCAP"))
                    if (
                        symbol not in identity_names
                        or close is None
                        or close <= 0
                        or market_cap is None
                        or market_cap <= 0
                    ):
                        continue
                    peer_price_rows.append(
                        {
                            "peer_symbol": symbol,
                            "peer_name": identity_names[symbol],
                            "close": close,
                            "market_cap": market_cap,
                            "observed_at": trading_date.isoformat(),
                            "source_id": market_source_id,
                        }
                    )
                target_row = next(
                    (
                        row
                        for row in exact_snapshot_rows
                        if str(row.get("ISU_CD") or row.get("ISU_SRT_CD") or "")
                        == target_id
                    ),
                    None,
                )
                if target_row is None:
                    continue
                bar = _krx_stock_bar(target_row, target_id=target_id, cutoff=cutoff)
                if bar is not None and market is None:
                    bars.append(bar)
                    market = candidate_market
            listing_identity_roster = _merge_listing_identity_rosters(
                listing_identity_rows
            )
            equity_line_counts: dict[str, int] = {}
            for identity in listing_identity_roster:
                base_name = _krx_equity_issuer_name_key(
                    identity.get("peer_name")
                )
                equity_line_counts[base_name] = (
                    equity_line_counts.get(base_name, 0) + 1
                )
            peer_price_rows = [
                {
                    **dict(row),
                    "listed_equity_line_count": equity_line_counts.get(
                        _krx_equity_issuer_name_key(row.get("peer_name")),
                        0,
                    ),
                }
                for row in peer_price_rows
            ]
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
            listing_identity_roster = ()
            listing_market_details = {
                candidate_market: {
                    "status": "AUTH_FAILED",
                    "exact_snapshot_row_count": 0,
                    "identity_count": 0,
                    "source_id": None,
                }
                for candidate_market in required_listing_markets
            }
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
        complete_listing_market_set = set(complete_listing_markets)
        listing_identity_roster_audit = {
            "schema_version": "e2r_v5_krx_listing_identity_roster_audit_v1",
            "snapshot_date": trading_date.isoformat(),
            "required_markets": list(required_listing_markets),
            "complete_markets": [
                market
                for market in required_listing_markets
                if market in complete_listing_market_set
            ],
            "incomplete_markets": [
                market
                for market in required_listing_markets
                if market not in complete_listing_market_set
            ],
            "market_details": {
                market: dict(listing_market_details[market])
                for market in required_listing_markets
            },
            "all_required_markets_complete": (
                complete_listing_market_set == set(required_listing_markets)
            ),
            "complete_market_snapshot_used_without_top_n": (
                complete_listing_market_set == set(required_listing_markets)
            ),
            "identity_count": len(listing_identity_roster),
            "identity_roster_hash": stable_hash(listing_identity_roster),
            "identity_scope_only_not_score_or_stage_input": True,
        }
        selected = _dedupe_price_bars(bars, target_id=target_id)
        source_ids = tuple(
            dict.fromkeys(
                row["source_id"]
                for row in manifests
                if (
                    row.get("provider_name") == "data.go.kr"
                    and row.get("source_role") == "PRICE_HISTORY"
                )
                or (
                    row.get("provider_name") == "KRX"
                    and market is not None
                    and (
                        (
                            row.get("source_role")
                            == "CURRENT_PRICE_MARKET_CAP"
                            and row.get("canonical_url")
                            == _KRX_STOCK_URLS[market]
                        )
                        or (
                            row.get("source_role") == "BENCHMARK_PRICE"
                            and row.get("canonical_url")
                            == _KRX_INDEX_URLS[market]
                        )
                    )
                )
            )
        )
        if not selected or not source_ids:
            return (
                UnavailableStructuredSourceRoute(
                    "KRX_PRICE_MARKET_CAP",
                    "no point-in-time price history available",
                ),
                listing_identity_roster,
                listing_identity_roster_audit,
                tuple(peer_price_rows),
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
        return (
            InMemoryStructuredSourceRoute("KRX_PRICE_MARKET_CAP", payload),
            listing_identity_roster,
            listing_identity_roster_audit,
            tuple(peer_price_rows),
        )

    def _peer_route(
        self,
        *,
        target_id: str,
        target_name: str,
        cutoff: date,
        evidence_facts: Sequence[EvidenceFact | Mapping[str, Any]],
        source_claims: Sequence[Mapping[str, Any]],
        listing_identity_roster: Sequence[Mapping[str, str]],
        listing_identity_roster_audit: Mapping[str, Any],
        listing_snapshot_date: date,
        peer_price_rows: Sequence[Mapping[str, Any]],
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
            "official_trailing_pb_fallbacks": [],
            "pending_reason": None,
            "listing_identity_roster": dict(listing_identity_roster_audit),
            "provider_response_cache_invalidations": [],
            "selection_route_cache_invalidations": [],
            "llm_selects_direction_only": True,
            "llm_supplies_valuation_values": False,
            "point_in_time_structured_fetch_required": True,
            "production_score_authority": False,
        }
        if listing_identity_roster_audit.get(
            "all_required_markets_complete"
        ) is not True:
            base_audit["pending_reason"] = (
                "AUTHORITATIVE_LISTING_ROSTER_INCOMPLETE"
            )
            return (
                UnavailableStructuredSourceRoute(
                    "PEER_STRUCTURED",
                    "authoritative KRX listing roster is incomplete",
                ),
                base_audit,
            )
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
        point_in_time_peer_roster = _point_in_time_peer_identity_roster(
            listing_identity_roster,
            cutoff=cutoff,
            cache_roots=(cache_root, *shared_cache_roots),
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
            "authoritative_listing_identity_roster": [
                dict(row) for row in listing_identity_roster
            ],
            "point_in_time_structured_peer_identity_roster": [
                dict(row) for row in point_in_time_peer_roster
            ],
            "listing_identity_roster_accounting": {
                "provider_name": "KRX",
                "snapshot_date": listing_snapshot_date.isoformat(),
                "identity_count": len(listing_identity_roster),
                "identity_roster_hash": stable_hash(listing_identity_roster),
                "required_markets": list(
                    listing_identity_roster_audit.get("required_markets") or ()
                ),
                "complete_markets": list(
                    listing_identity_roster_audit.get("complete_markets") or ()
                ),
                "complete_market_snapshot_used_without_top_n": (
                    listing_identity_roster_audit.get(
                        "complete_market_snapshot_used_without_top_n"
                    )
                    is True
                ),
                "identity_scope_only_not_score_or_stage_input": True,
            },
            "point_in_time_peer_roster_accounting": {
                "cutoff_date": cutoff.isoformat(),
                "available_identity_count": len(point_in_time_peer_roster),
                "available_identity_roster_hash": stable_hash(
                    point_in_time_peer_roster
                ),
                "availability_only_no_multiple_or_score_values_exposed": True,
                "availability_hint_only_not_peer_allowlist": True,
                (
                    "cached_snapshot_candidates_should_be_preferred_only_"
                    "when_economically_comparable"
                ): True,
            },
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
                "authoritative_listing_identity_roster_is_allowlist": True,
                (
                    "point_in_time_structured_peer_identity_roster_is_"
                    "availability_hint_only"
                ): True,
                (
                    "peer_symbol_and_name_must_be_copied_exactly_from_"
                    "authoritative_listing_identity_roster"
                ): True,
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
        if response is not None:
            try:
                assert_blind_research_output(response)
                proposals = _validated_peer_proposals(
                    response,
                    target_id=target_id,
                    authoritative_listing_identity_roster=(
                        listing_identity_roster
                    ),
                )
            except (KeyError, TypeError, ValueError) as exc:
                invalidation = _invalidate_peer_validation_response_cache(
                    self.peer_provider,
                    rejection_phase="CACHED_SELECTION_RESPONSE",
                    rejection_error=exc,
                )
                if invalidation is not None:
                    base_audit[
                        "provider_response_cache_invalidations"
                    ].append(invalidation)
                base_audit["selection_route_cache_invalidations"].append(
                    _delete_peer_selection_route_cache(
                        selection_cache_path,
                        reason=(
                            "STRUCTURED_PEER_CACHED_RESPONSE_VALIDATION_REJECTED"
                        ),
                    )
                )
                base_audit["rejected_provider_cache_hit"] = True
                base_audit["provider_cache_hit"] = False
                base_audit["validation_retry_used"] = True
                response = None
                cached_prompt_hash = None
        try:
            if response is None:
                # A route-cache row does not carry an active collaboration
                # request handle across a clean process resume.  Replay the
                # original semantic payload once so the real provider/journal
                # response becomes active; if it is still invalid, the normal
                # fresh-response path below can quarantine that exact response.
                attempt_payload = payload
                for attempt_index in range(2):
                    base_audit["provider_attempt_count"] += 1
                    try:
                        response = self.peer_provider.complete(
                            pass_name="STRUCTURED_PEER_SELECTION",
                            payload=attempt_payload,
                        )
                    except StructuredProviderUnavailable as exc:
                        recovered_retry_payload = (
                            _recover_validated_peer_selection_retry_payload(
                                self.peer_provider,
                                primary_payload=payload,
                            )
                            if (
                                attempt_index == 0
                                and attempt_payload == payload
                                and str(exc).startswith(
                                    "COLLABORATION_RESPONSE_PENDING:"
                                    "COLLABREQ-"
                                )
                            )
                            else None
                        )
                        if recovered_retry_payload is not None:
                            base_audit["validation_retry_used"] = True
                            attempt_payload = recovered_retry_payload
                            continue
                        raise
                    try:
                        assert_blind_research_output(response)
                        proposals = _validated_peer_proposals(
                            response,
                            target_id=target_id,
                            authoritative_listing_identity_roster=(
                                listing_identity_roster
                            ),
                        )
                    except (KeyError, TypeError, ValueError) as exc:
                        invalidation = (
                            _invalidate_peer_validation_response_cache(
                                self.peer_provider,
                                rejection_phase=(
                                    "FRESH_SELECTION_RESPONSE_"
                                    f"ATTEMPT_{attempt_index + 1}"
                                ),
                                rejection_error=exc,
                            )
                        )
                        if invalidation is not None:
                            base_audit[
                                "provider_response_cache_invalidations"
                            ].append(invalidation)
                        base_audit[
                            "selection_route_cache_invalidations"
                        ].append(
                            _delete_peer_selection_route_cache(
                                selection_cache_path,
                                reason=(
                                    "STRUCTURED_PEER_FRESH_RESPONSE_"
                                    "VALIDATION_REJECTED"
                                ),
                            )
                        )
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
            # The exact-date KRX roster already establishes listing identity.
            # CompanyGuide is optional here: a missing/current-only page must
            # not prevent the bounded KRX + DART trailing-value fallback.
            actual_name = str(proposal["peer_name"])
            parsed: Mapping[str, Any] = {}
            snapshot_failure = "SNAPSHOT_FETCH_FAILED"
            if text:
                page_metadata = parse_companyguide_live_page_metadata(text)
                parsed = parse_companyguide_live_consensus_payload(
                    text, as_of_date=cutoff
                )
                page_name = str(
                    page_metadata.get("COMPANY_NAME")
                    or parsed.get("COMPANY_NAME")
                    or ""
                ).strip()
                if not page_name:
                    snapshot_failure = "COMPANY_IDENTITY_UNVERIFIED"
                elif _company_name_key(page_name) != _company_name_key(
                    proposal["peer_name"]
                ):
                    snapshot_failure = "COMPANY_IDENTITY_MISMATCH"
                else:
                    actual_name = page_name
                    snapshot_failure = "CONSENSUS_PAYLOAD_UNAVAILABLE"
            source_id = next(
                (
                    str(row["source_id"])
                    for row in reversed(manifests)
                    if row.get("provider_name") == "CompanyGuide"
                    and row.get("source_role") == role
                ),
                None,
            )
            observed: date | None = None
            if (
                snapshot_failure not in {
                    "COMPANY_IDENTITY_UNVERIFIED",
                    "COMPANY_IDENTITY_MISMATCH",
                }
                and parsed.get("CONSENSUS_DATE_VERIFIED") is True
            ):
                try:
                    observed = date.fromisoformat(
                        str(parsed["CONSENSUS_AS_OF_DATE"])
                        .replace("/", "-")[:10]
                    )
                    snapshot_failure = (
                        "FUTURE_SNAPSHOT_REJECTED"
                        if observed > cutoff
                        else "NO_FORWARD_MULTIPLE"
                    )
                except (KeyError, ValueError):
                    snapshot_failure = "SNAPSHOT_DATE_INVALID"
            metric_count = 0
            if observed is not None and observed <= cutoff and source_id:
                metrics = (
                    ("forward_pe", parsed.get("FORWARD_12M_PER")),
                    ("forward_pb", parsed.get("FORWARD_12M_PBR")),
                    (
                        "forward_ev_ebitda",
                        parsed.get("FORWARD_12M_EV_EBITDA"),
                    ),
                )
                for metric_id, raw_value in metrics:
                    value = _float(raw_value)
                    if value is None or value <= 0:
                        continue
                    observations.append(
                        _peer_valuation_observation(
                            proposal=proposal,
                            peer_name=actual_name,
                            cutoff=cutoff,
                            metric_id=metric_id,
                            value=value,
                            observed_at=observed,
                            source_ids=(source_id,),
                            valuation_source=(
                                "COMPANYGUIDE_POINT_IN_TIME_SNAPSHOT"
                            ),
                        )
                    )
                    metric_count += 1
            if metric_count == 0:
                if snapshot_failure == "COMPANY_IDENTITY_MISMATCH":
                    proposal_failures.append(
                        f"{symbol}:COMPANY_IDENTITY_MISMATCH"
                    )
                    continue
                fallback_observation, fallback_audit = (
                    self._peer_official_trailing_pb_observation(
                        target_id=target_id,
                        cutoff=cutoff,
                        listing_snapshot_date=listing_snapshot_date,
                        proposal=proposal,
                        peer_price_rows=peer_price_rows,
                        cache_root=cache_root,
                        checkpoint_resume=checkpoint_resume,
                        attempts=attempts,
                        manifests=manifests,
                        snapshot_failure=snapshot_failure,
                    )
                )
                base_audit["official_trailing_pb_fallbacks"].append(
                    fallback_audit
                )
                if fallback_observation is None:
                    if snapshot_failure == "FUTURE_SNAPSHOT_REJECTED":
                        _mark_attempt_future_rejected(
                            attempts,
                            source_role=role,
                            effective_date=(
                                observed.isoformat() if observed else ""
                            ),
                        )
                    proposal_failures.append(
                        f"{symbol}:"
                        + str(
                            fallback_audit.get("failure_reason")
                            or snapshot_failure
                        )
                    )
                    continue
                observations.append(fallback_observation)
                observed = date.fromisoformat(
                    fallback_observation.observed_at[:10]
                )
                metric_count = 1
            selected_rows.append(
                {
                    "peer_symbol": symbol,
                    "proposed_peer_name": proposal["peer_name"],
                    "verified_peer_name": actual_name,
                    "observed_at": observed.isoformat(),
                    "structured_metric_count": metric_count,
                    "valuation_source": (
                        observations[-1].metadata.get("valuation_source")
                    ),
                }
            )
            metric_peer_counts = {
                metric_id: len(
                    {
                        row.peer_id
                        for row in observations
                        if row.metric_id == metric_id
                    }
                )
                for metric_id in {row.metric_id for row in observations}
            }
            if any(count >= 2 for count in metric_peer_counts.values()):
                base_audit["structured_fetch_stop_condition"] = (
                    "COMMON_PEER_MULTIPLE_RESOLVED"
                )
                break

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
                    try:
                        assert_blind_research_output(retry_response)
                        _validated_peer_proposals(
                            retry_response,
                            target_id=target_id,
                            authoritative_listing_identity_roster=(
                                listing_identity_roster
                            ),
                        )
                    except (KeyError, TypeError, ValueError) as exc:
                        invalidation = (
                            _invalidate_peer_validation_response_cache(
                                self.peer_provider,
                                rejection_phase=(
                                    "STRUCTURED_SOURCE_VERIFICATION_RETRY_RESPONSE"
                                ),
                                rejection_error=exc,
                            )
                        )
                        if invalidation is not None:
                            base_audit[
                                "provider_response_cache_invalidations"
                            ].append(invalidation)
                        base_audit[
                            "selection_route_cache_invalidations"
                        ].append(
                            _delete_peer_selection_route_cache(
                                selection_cache_path,
                                reason=(
                                    "STRUCTURED_PEER_VERIFICATION_RETRY_"
                                    "RESPONSE_VALIDATION_REJECTED"
                                ),
                            )
                        )
                        raise
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
                    listing_identity_roster=listing_identity_roster,
                    listing_identity_roster_audit=(
                        listing_identity_roster_audit
                    ),
                    listing_snapshot_date=listing_snapshot_date,
                    peer_price_rows=peer_price_rows,
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
            base_audit["provider_response_cache_invalidation"] = (
                _invalidate_structured_peer_response_cache(
                    self.peer_provider,
                    proposal_failures=proposal_failures,
                )
            )
            base_audit["selection_route_cache_invalidation"] = (
                _delete_peer_selection_route_cache(
                    selection_cache_path,
                    reason="STRUCTURED_PEER_SOURCE_VERIFICATION_REJECTED",
                )
            )
            base_audit["selection_route_cache_invalidations"].append(
                base_audit["selection_route_cache_invalidation"]
            )
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

    def _peer_corp_code_from_archived_directory(
        self,
        *,
        target_id: str,
        cutoff: date,
        symbol: str,
        company_name: str,
        cache_root: Path,
        attempts: list[CurrentStructuredFetchAttempt],
        manifests: list[Mapping[str, Any]],
    ) -> tuple[str | None, str | None, Mapping[str, Any]]:
        """Resolve a peer identifier through a non-economic DART locator bridge.

        Legacy cache folder dates are not trusted as fetch timestamps.  The
        directory is therefore never presented as a historical source.  Only a
        mapping whose own DART ``modify_date`` is pre-cutoff and whose name
        matches the exact-date KRX roster may locate the issuer's dated
        financial response.  The selected row and archive hash are persisted
        solely to make that identifier bridge reproducible.
        """

        audit: dict[str, Any] = {
            "status": "PENDING",
            "archive_directory_label": None,
            "archive_content_hash": None,
            "mapping_modify_date": None,
            "failure_reason": None,
            "maximum_archive_candidates": self.opendart_corp_code_max_archives,
            "archive_candidate_count": 0,
            "parsed_archive_count": 0,
            "stop_condition": None,
            "folder_date_used_as_source_availability": False,
            "identifier_bridge_only": True,
            "economic_value_authority": False,
        }
        candidates: list[tuple[date, Path]] = []
        for path in self.opendart_corp_code_cache_root.glob("*/corpCode.zip"):
            try:
                snapshot_date = date.fromisoformat(path.parent.name)
            except ValueError:
                continue
            candidates.append((snapshot_date, path))
        audit["archive_candidate_count"] = len(candidates)
        bounded_candidates = sorted(candidates, reverse=True)[
            : self.opendart_corp_code_max_archives
        ]
        for snapshot_date, path in bounded_candidates:
            try:
                content = path.read_bytes()
                rows = OpenDARTConnector.normalize_company_code_archive(content)
            except (OSError, TypeError, ValueError):
                continue
            audit["parsed_archive_count"] += 1
            row = next((item for item in rows if item.stock_code == symbol), None)
            if row is None:
                continue
            if _company_name_key(row.corp_name) != _company_name_key(company_name):
                audit["failure_reason"] = "CORP_CODE_DIRECTORY_NAME_MISMATCH"
                continue
            if row.modify_date is None:
                audit["failure_reason"] = "CORP_CODE_MAPPING_MODIFY_DATE_MISSING"
                continue
            if row.modify_date > cutoff:
                audit["failure_reason"] = "CORP_CODE_MAPPING_MODIFIED_AFTER_CUTOFF"
                continue
            content_hash = hashlib.sha256(content).hexdigest()
            response = StructuredHTTPResponse(
                status_code=200,
                canonical_url=_DART_CORP_CODE_URL,
                provider_request_id="CACHE-" + content_hash[:20],
                content_hash=content_hash,
            )
            role = f"PEER_CORP_CODE_DIRECTORY:{symbol}"
            attempts.append(
                _attempt(
                    target_id=target_id,
                    cutoff=cutoff,
                    provider_name="OpenDART",
                    source_role=role,
                    canonical_url=_DART_CORP_CODE_URL,
                    status="FETCHED",
                    response=response,
                    row_count=len(rows),
                    effective_date=None,
                    cache_hit=True,
                    error=None,
                )
            )
            manifest = _manifest_row(
                target_id=target_id,
                cutoff=cutoff,
                provider_name="OpenDART",
                source_role=role,
                response=response,
                row_count=len(rows),
                effective_date=None,
            )
            manifests.append(manifest)
            selected_mapping = {
                "schema_version": "e2r_v5_peer_corp_code_mapping_v1",
                "symbol": symbol,
                "company_name": row.corp_name,
                "corp_code": row.corp_code,
                "mapping_modify_date": (
                    row.modify_date.isoformat() if row.modify_date else None
                ),
                "archive_directory_label": snapshot_date.isoformat(),
                "archive_directory_label_is_not_fetch_date": True,
                "archive_content_hash": content_hash,
                "source_id": manifest["source_id"],
                "identity_cross_checked_with_krx_roster": True,
                "production_score_authority": False,
            }
            write_json(
                cache_root / f"dart_peer_corp_code_{symbol}.json",
                selected_mapping,
            )
            audit.update(
                {
                    "status": "RESOLVED",
                    "archive_directory_label": snapshot_date.isoformat(),
                    "archive_content_hash": content_hash,
                    "mapping_modify_date": (
                        row.modify_date.isoformat() if row.modify_date else None
                    ),
                    "failure_reason": None,
                    "stop_condition": "IDENTITY_MAPPING_RESOLVED",
                }
            )
            return row.corp_code.zfill(8), str(manifest["source_id"]), audit
        if audit["failure_reason"] is None:
            audit["failure_reason"] = "USABLE_CORP_CODE_DIRECTORY_MAPPING_MISSING"
        audit["stop_condition"] = "ARCHIVE_CANDIDATE_BUDGET_EXHAUSTED"
        return None, None, audit

    def _peer_official_trailing_pb_observation(
        self,
        *,
        target_id: str,
        cutoff: date,
        listing_snapshot_date: date,
        proposal: Mapping[str, Any],
        peer_price_rows: Sequence[Mapping[str, Any]],
        cache_root: Path,
        checkpoint_resume: bool,
        attempts: list[CurrentStructuredFetchAttempt],
        manifests: list[Mapping[str, Any]],
        snapshot_failure: str,
    ) -> tuple[PeerValuationObservation | None, Mapping[str, Any]]:
        """Derive a cutoff-valid peer P/B from bounded official observations.

        A current-only CompanyGuide page cannot prove a historical forward
        multiple, and a report-list EPS field does not identify its forecast
        horizon.  This fallback therefore uses only an exact-date KRX market
        capitalization and the newest pre-cutoff OpenDART consolidated total
        equity.  It tries at most two explicitly dated statement periods and
        creates neither report downloads nor EvidenceFacts.
        """

        symbol = str(proposal.get("peer_symbol") or "")
        proposed_name = str(proposal.get("peer_name") or "")
        audit: dict[str, Any] = {
            "peer_symbol": symbol,
            "peer_name": proposed_name,
            "snapshot_failure": snapshot_failure,
            "route": "KRX_MARKET_CAP_X_OPENDART_PARENT_EQUITY",
            "maximum_statement_fetches": 2,
            "statement_fetch_count": 0,
            "maximum_filing_metadata_fetches": 2,
            "filing_metadata_fetch_count": 0,
            "report_pdf_fetch_count": 0,
            "evidence_fact_count_added": 0,
            "status": "PENDING",
            "failure_reason": None,
        }
        price_row = next(
            (
                row
                for row in peer_price_rows
                if str(row.get("peer_symbol") or "") == symbol
                and _company_name_key(row.get("peer_name"))
                == _company_name_key(proposed_name)
                and str(row.get("observed_at") or "")[:10]
                == listing_snapshot_date.isoformat()
            ),
            None,
        )
        if price_row is None:
            audit["failure_reason"] = "POINT_IN_TIME_KRX_PRICE_MISSING"
            return None, audit
        if int(price_row.get("listed_equity_line_count") or 0) != 1:
            audit["failure_reason"] = (
                "MULTIPLE_LISTED_EQUITY_LINES_REQUIRE_SCOPE_MATCHING"
            )
            return None, audit

        credential = os.environ.get("OPENDART_API_KEY") or os.environ.get(
            "OPEN_DART_API_KEY"
        )
        if not credential:
            audit["failure_reason"] = "OPENDART_CREDENTIAL_MISSING"
            return None, audit
        corp_code, corp_code_source_id, corp_code_audit = (
            self._peer_corp_code_from_archived_directory(
                target_id=target_id,
                cutoff=cutoff,
                symbol=symbol,
                company_name=proposed_name,
                cache_root=cache_root,
                attempts=attempts,
                manifests=manifests,
            )
        )
        audit["corp_code_resolution"] = dict(corp_code_audit)
        if not corp_code or not corp_code_source_id:
            audit["failure_reason"] = str(
                corp_code_audit.get("failure_reason")
                or "OPENDART_CORP_CODE_IDENTITY_UNVERIFIED"
            )
            return None, audit

        equity_value: float | None = None
        equity_metadata: Mapping[str, Any] = {}
        equity_source_id = ""
        filing_metadata_source_id = ""
        selected_period: Mapping[str, Any] | None = None
        period_attempts: list[Mapping[str, Any]] = []
        terminal_statement_failure: str | None = None
        for period in _latest_balance_sheet_periods(cutoff, maximum=2):
            role = (
                f"PEER_PARENT_EQUITY:{symbol}:"
                f"{period['fiscal_year']}:{period['report_code']}"
            )
            manifest_start = len(manifests)
            payload = self._json(
                target_id=target_id,
                cutoff=cutoff,
                provider_name="OpenDART",
                source_role=role,
                cache_key=(
                    f"dart_peer_equity_{symbol}_{corp_code}_"
                    f"{period['fiscal_year']}_{period['report_code']}_CFS"
                ),
                cache_root=cache_root,
                checkpoint_resume=checkpoint_resume,
                url=_DART_FULL_ACCOUNT_URL,
                params={
                    "crtfc_key": credential,
                    "corp_code": corp_code,
                    "bsns_year": str(period["fiscal_year"]),
                    "reprt_code": str(period["report_code"]),
                    "fs_div": "CFS",
                },
                headers={},
                attempts=attempts,
                manifests=manifests,
                effective_date=period["reported_at"].isoformat(),
                rows_getter=lambda value: value.get("list") or (),
            )
            audit["statement_fetch_count"] += 1
            if payload is None:
                terminal_statement_failure = "PEER_EQUITY_PROVIDER_ERROR"
                period_attempts.append(
                    {
                        "fiscal_year": period["fiscal_year"],
                        "report_code": period["report_code"],
                        "period_end": period["period_end"].isoformat(),
                        "reported_at": period["reported_at"].isoformat(),
                        "status": terminal_statement_failure,
                    }
                )
                break
            dart_status = str(payload.get("status") or "")
            if dart_status == "013":
                period_attempts.append(
                    {
                        "fiscal_year": period["fiscal_year"],
                        "report_code": period["report_code"],
                        "period_end": period["period_end"].isoformat(),
                        "reported_at": period["reported_at"].isoformat(),
                        "status": "DART_NO_RESULT",
                    }
                )
                continue
            if dart_status != "000":
                terminal_statement_failure = (
                    f"PEER_EQUITY_DART_STATUS_ERROR:{dart_status}"
                )
                period_attempts.append(
                    {
                        "fiscal_year": period["fiscal_year"],
                        "report_code": period["report_code"],
                        "period_end": period["period_end"].isoformat(),
                        "reported_at": period["reported_at"].isoformat(),
                        "status": terminal_statement_failure,
                    }
                )
                break
            parsed_equity, parse_audit = _opendart_parent_equity(
                payload or {},
                cutoff=cutoff,
                expected_corp_code=corp_code,
                expected_fiscal_year=int(period["fiscal_year"]),
                expected_report_code=str(period["report_code"]),
            )
            period_attempts.append(
                {
                    "fiscal_year": period["fiscal_year"],
                    "report_code": period["report_code"],
                    "period_end": period["period_end"].isoformat(),
                    "reported_at": period["reported_at"].isoformat(),
                    **dict(parse_audit),
                }
            )
            if parsed_equity is None:
                rejected = set(
                    (parse_audit.get("rejected_reasons") or {}).keys()
                )
                if rejected.intersection(
                    {
                        "CORP_CODE_MISMATCH",
                        "FISCAL_YEAR_MISMATCH",
                        "REPORT_CODE_MISMATCH",
                        "NON_KRW_CURRENCY",
                        "RECEIPT_DATE_INVALID",
                        "FUTURE_RECEIPT_REJECTED",
                        "FILING_PERIOD_END_UNVERIFIED",
                    }
                ):
                    terminal_statement_failure = (
                        "PEER_EQUITY_IDENTITY_OR_DATE_VALIDATION_FAILED"
                    )
                    break
                continue
            receipt_date = date.fromisoformat(str(parse_audit["rcept_date"]))
            filing_role = (
                f"PEER_FILING_PERIOD:{symbol}:"
                f"{period['fiscal_year']}:{period['report_code']}"
            )
            filing_manifest_start = len(manifests)
            filing_payload = self._json(
                target_id=target_id,
                cutoff=cutoff,
                provider_name="OpenDART",
                source_role=filing_role,
                cache_key=(
                    f"dart_peer_filing_period_{symbol}_{corp_code}_"
                    f"{parse_audit['rcept_no']}"
                ),
                cache_root=cache_root,
                checkpoint_resume=checkpoint_resume,
                url=_DART_DISCLOSURE_LIST_URL,
                params={
                    "crtfc_key": credential,
                    "corp_code": corp_code,
                    "bgn_de": receipt_date.strftime("%Y%m%d"),
                    "end_de": receipt_date.strftime("%Y%m%d"),
                    "page_no": "1",
                    "page_count": "100",
                },
                headers={},
                attempts=attempts,
                manifests=manifests,
                effective_date=receipt_date.isoformat(),
                rows_getter=lambda value: value.get("list") or (),
            )
            audit["filing_metadata_fetch_count"] += 1
            if filing_payload is None:
                terminal_statement_failure = (
                    "PEER_FILING_PERIOD_PROVIDER_ERROR"
                )
                period_attempts[-1]["filing_period_status"] = (
                    terminal_statement_failure
                )
                break
            filing_period_end, filing_audit = (
                _opendart_filing_period_end(
                    filing_payload,
                    cutoff=cutoff,
                    expected_corp_code=corp_code,
                    expected_rcept_no=str(parse_audit["rcept_no"]),
                    expected_report_code=str(period["report_code"]),
                    expected_period_end=period["period_end"],
                )
            )
            period_attempts[-1]["filing_period_confirmation"] = dict(
                filing_audit
            )
            if filing_period_end is None:
                terminal_statement_failure = (
                    "PEER_FILING_PERIOD_VALIDATION_FAILED"
                )
                break
            filing_metadata_source_id = next(
                (
                    str(row["source_id"])
                    for row in reversed(
                        manifests[filing_manifest_start:]
                    )
                    if row.get("provider_name") == "OpenDART"
                    and row.get("source_role") == filing_role
                ),
                "",
            )
            if not filing_metadata_source_id:
                terminal_statement_failure = (
                    "PEER_FILING_PERIOD_SOURCE_MANIFEST_MISSING"
                )
                break
            source_id = next(
                (
                    str(row["source_id"])
                    for row in reversed(manifests[manifest_start:])
                    if row.get("provider_name") == "OpenDART"
                    and row.get("source_role") == role
                ),
                "",
            )
            if not source_id:
                continue
            equity_value = parsed_equity
            equity_metadata = {
                **dict(parse_audit),
                "filing_period_confirmation": dict(filing_audit),
            }
            equity_source_id = source_id
            selected_period = period
            break
        audit["statement_period_attempts"] = period_attempts
        if (
            equity_value is None
            or selected_period is None
            or not equity_source_id
            or not filing_metadata_source_id
        ):
            audit["failure_reason"] = terminal_statement_failure or (
                "PRE_CUTOFF_CONSOLIDATED_PARENT_EQUITY_MISSING"
            )
            return None, audit

        market_cap = _float(price_row.get("market_cap"))
        price_source_id = str(price_row.get("source_id") or "")
        if market_cap is None or market_cap <= 0:
            audit["failure_reason"] = "POINT_IN_TIME_KRX_MARKET_CAP_MISSING"
            return None, audit
        if not price_source_id:
            audit["failure_reason"] = "FALLBACK_SOURCE_MANIFEST_MISSING"
            return None, audit

        value = market_cap / equity_value
        equity_received_at = date.fromisoformat(
            str(equity_metadata["rcept_date"])
        )
        value_observed_at = max(listing_snapshot_date, equity_received_at)
        observation = _peer_valuation_observation(
            proposal=proposal,
            peer_name=proposed_name,
            cutoff=cutoff,
            metric_id="trailing_parent_pb",
            value=value,
            observed_at=value_observed_at,
            source_ids=(
                price_source_id,
                equity_source_id,
                corp_code_source_id,
                filing_metadata_source_id,
            ),
            valuation_source="KRX_MARKET_CAP_X_OPENDART_PARENT_EQUITY",
            extra_metadata={
                "krx_market_cap_date": listing_snapshot_date.isoformat(),
                "krx_market_cap_krw": market_cap,
                "dart_parent_equity_krw": equity_value,
                "dart_corp_code": corp_code,
                "dart_fiscal_year": selected_period["fiscal_year"],
                "dart_report_code": selected_period["report_code"],
                "dart_period_end": selected_period["period_end"].isoformat(),
                "dart_available_at": equity_received_at.isoformat(),
                "corp_code_directory_source_id": corp_code_source_id,
                "dart_filing_period_source_id": filing_metadata_source_id,
                "corp_code_identity_cross_checked_with_krx_name": True,
                **dict(equity_metadata),
            },
        )
        audit.update(
            {
                "status": "RESOLVED",
                "failure_reason": None,
                "derived_metric_id": "trailing_parent_pb",
                "derived_value": round(value, 6),
                "source_ids": [
                    price_source_id,
                    equity_source_id,
                    corp_code_source_id,
                    filing_metadata_source_id,
                ],
                "stop_condition": "POINT_IN_TIME_TRAILING_PARENT_PB_RESOLVED",
            }
        )
        return observation, audit


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


def _point_in_time_peer_identity_roster(
    listing_identity_roster: Sequence[Mapping[str, str]],
    *,
    cutoff: date,
    cache_roots: Sequence[Path],
) -> tuple[Mapping[str, str], ...]:
    """Expose only identities with an already cached pre-cutoff source page.

    No multiple or financial value enters the LLM prompt.  This is source
    availability metadata so the open-ended peer selector does not repeatedly
    choose identities whose only reachable CompanyGuide page is from the
    future relative to ``cutoff``.
    """

    available: list[Mapping[str, str]] = []
    for identity in listing_identity_roster:
        symbol = str(identity.get("peer_symbol") or "").strip()
        name = str(identity.get("peer_name") or "").strip()
        if not symbol or not name:
            continue
        request_fingerprint = _structured_request_fingerprint(
            response_kind="text",
            url=_COMPANYGUIDE_SNAPSHOT_URL,
            params={"cmp_cd": symbol, "cn": ""},
        )
        cache_keys = (
            f"companyguide_peer_snapshot_{symbol}",
            f"companyguide_snapshot_{symbol}",
        )
        found = False
        for cache_root in cache_roots:
            for cache_key in cache_keys:
                path = Path(cache_root) / f"{cache_key}.json"
                if not path.is_file():
                    continue
                loaded = _load_structured_cache_response(
                    path,
                    response_kind="text",
                    request_url=_COMPANYGUIDE_SNAPSHOT_URL,
                    request_fingerprint=request_fingerprint,
                    legacy_identity_allowed=True,
                )
                if loaded is None:
                    continue
                response, _ = loaded
                if _companyguide_cached_snapshot_is_point_in_time(
                    response,
                    cutoff=cutoff,
                    expected_company_name=name,
                ):
                    found = True
                    break
            if found:
                break
        if found:
            available.append(
                {
                    "peer_symbol": symbol,
                    "peer_name": name,
                    "point_in_time_snapshot_available": "YES",
                }
            )
    return tuple(available)


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
    response: Mapping[str, Any],
    *,
    target_id: str,
    authoritative_listing_identity_roster: Sequence[Mapping[str, str]],
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
    authoritative_identities = {
        str(row.get("peer_symbol") or "").strip(): str(
            row.get("peer_name") or ""
        ).strip()
        for row in authoritative_listing_identity_roster
        if str(row.get("peer_symbol") or "").strip()
        and str(row.get("peer_name") or "").strip()
    }
    if not authoritative_identities:
        raise ValueError("authoritative listing identity roster is empty")
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
        authoritative_name = authoritative_identities.get(symbol)
        if authoritative_name is None:
            raise ValueError(
                f"peer symbol is absent from authoritative listing roster: {symbol}"
            )
        if _company_name_key(name) != _company_name_key(authoritative_name):
            raise ValueError(
                f"peer symbol/name pair mismatches authoritative listing roster: {symbol}"
            )
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
                "peer_name": authoritative_name,
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


def _krx_equity_issuer_name_key(value: Any) -> str:
    """Collapse only KRX-style preferred-share suffixes for scope detection."""

    normalized = _company_name_key(value)
    return re.sub(r"(?:[0-9]+우b|[0-9]+우|우b|우)$", "", normalized)


def _peer_valuation_observation(
    *,
    proposal: Mapping[str, Any],
    peer_name: str,
    cutoff: date,
    metric_id: str,
    value: float,
    observed_at: date,
    source_ids: Sequence[str],
    valuation_source: str,
    extra_metadata: Mapping[str, Any] | None = None,
) -> PeerValuationObservation:
    """Build one source-backed value after deterministic peer verification."""

    return PeerValuationObservation(
        peer_id=str(proposal["peer_symbol"]),
        as_of_date=cutoff.isoformat(),
        metric_id=metric_id,
        value=float(value),
        unit="MULTIPLE",
        observed_at=observed_at.isoformat(),
        source_ids=tuple(dict.fromkeys(str(value) for value in source_ids)),
        source_route="PEER_STRUCTURED",
        confidence=float(proposal["confidence"]),
        metadata={
            "peer_name": peer_name,
            "symbol_identity_verified": True,
            "comparability_rationale": proposal["comparability_rationale"],
            "shared_economic_drivers": list(
                proposal["shared_economic_drivers"]
            ),
            "material_differences": list(proposal["material_differences"]),
            "structured_source": True,
            "llm_supplied_metric_value": False,
            "valuation_source": valuation_source,
            **dict(extra_metadata or {}),
        },
    )


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
    write_jsonl(paths["report_candidates"], result.report_candidates)
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


def _latest_balance_sheet_periods(
    cutoff: date, *, maximum: int
) -> tuple[Mapping[str, Any], ...]:
    """Return the newest distinct pre-cutoff statement periods, bounded."""

    candidates: list[Mapping[str, Any]] = []
    for fiscal_year in range(cutoff.year, cutoff.year - 4, -1):
        for quarter, month, report_code, available_month, available_day in (
            (1, 3, "11013", 5, 16),
            (2, 6, "11012", 8, 16),
            (3, 9, "11014", 11, 16),
        ):
            reported_at = date(
                fiscal_year, available_month, available_day
            )
            if reported_at <= cutoff:
                candidates.append(
                    {
                        "fiscal_year": fiscal_year,
                        "fiscal_quarter": quarter,
                        "period_end": date(
                            fiscal_year,
                            month,
                            _month_end(fiscal_year, month),
                        ),
                        "report_code": report_code,
                        "reported_at": reported_at,
                    }
                )
        annual_available = date(fiscal_year + 1, 4, 1)
        if annual_available <= cutoff:
            candidates.append(
                {
                    "fiscal_year": fiscal_year,
                    "fiscal_quarter": None,
                    "period_end": date(fiscal_year, 12, 31),
                    "report_code": "11011",
                    "reported_at": annual_available,
                }
            )
    ordered = sorted(
        candidates,
        key=lambda row: (row["reported_at"], row["period_end"]),
        reverse=True,
    )
    selected: list[Mapping[str, Any]] = []
    seen_period_ends: set[date] = set()
    for row in ordered:
        period_end = row["period_end"]
        if period_end in seen_period_ends:
            continue
        seen_period_ends.add(period_end)
        selected.append(row)
        if len(selected) >= maximum:
            break
    return tuple(selected)


def _opendart_parent_equity(
    payload: Mapping[str, Any],
    *,
    cutoff: date,
    expected_corp_code: str,
    expected_fiscal_year: int,
    expected_report_code: str,
) -> tuple[float | None, Mapping[str, Any]]:
    """Extract one identity/date-bound parent-equity BS observation."""

    status = str(payload.get("status") or "")
    if status != "000":
        return None, {"status": "DART_STATUS_ERROR", "dart_status": status}
    rows = payload.get("list") or ()
    if not isinstance(rows, (list, tuple)):
        return None, {"status": "DART_ROWS_INVALID"}
    candidates: list[tuple[float, date, Mapping[str, Any]]] = []
    rejected_reasons: dict[str, int] = {}
    for raw in rows:
        if not isinstance(raw, Mapping):
            continue
        if str(raw.get("sj_div") or "") != "BS":
            continue
        account_id = str(raw.get("account_id") or "").strip().casefold()
        if account_id != "ifrs-full_equityattributabletoownersofparent":
            continue
        corp_code = str(raw.get("corp_code") or "").strip()
        if corp_code.isdigit():
            corp_code = corp_code.zfill(8)
        if corp_code != expected_corp_code:
            rejected_reasons["CORP_CODE_MISMATCH"] = (
                rejected_reasons.get("CORP_CODE_MISMATCH", 0) + 1
            )
            continue
        if str(raw.get("bsns_year") or "") != str(expected_fiscal_year):
            rejected_reasons["FISCAL_YEAR_MISMATCH"] = (
                rejected_reasons.get("FISCAL_YEAR_MISMATCH", 0) + 1
            )
            continue
        if str(raw.get("reprt_code") or "") != expected_report_code:
            rejected_reasons["REPORT_CODE_MISMATCH"] = (
                rejected_reasons.get("REPORT_CODE_MISMATCH", 0) + 1
            )
            continue
        if str(raw.get("currency") or "") != "KRW":
            rejected_reasons["NON_KRW_CURRENCY"] = (
                rejected_reasons.get("NON_KRW_CURRENCY", 0) + 1
            )
            continue
        rcept_no = str(raw.get("rcept_no") or "")
        if not re.fullmatch(r"[0-9]{14}", rcept_no):
            rejected_reasons["RECEIPT_DATE_INVALID"] = (
                rejected_reasons.get("RECEIPT_DATE_INVALID", 0) + 1
            )
            continue
        try:
            received_at = date.fromisoformat(
                f"{rcept_no[:4]}-{rcept_no[4:6]}-{rcept_no[6:8]}"
            )
        except ValueError:
            rejected_reasons["RECEIPT_DATE_INVALID"] = (
                rejected_reasons.get("RECEIPT_DATE_INVALID", 0) + 1
            )
            continue
        if received_at > cutoff:
            rejected_reasons["FUTURE_RECEIPT_REJECTED"] = (
                rejected_reasons.get("FUTURE_RECEIPT_REJECTED", 0) + 1
            )
            continue
        amount = _float(raw.get("thstrm_amount"))
        if amount is None or amount <= 0:
            continue
        candidates.append((amount, received_at, raw))
    if not candidates:
        return None, {
            "status": "PARENT_EQUITY_ROW_MISSING",
            "rejected_reasons": rejected_reasons,
        }
    distinct_amounts = {row[0] for row in candidates}
    if len(distinct_amounts) != 1:
        return None, {
            "status": "PARENT_EQUITY_ROW_AMBIGUOUS",
            "candidate_count": len(candidates),
            "distinct_amount_count": len(distinct_amounts),
            "rejected_reasons": rejected_reasons,
        }
    amount, received_at, selected = min(
        candidates, key=lambda row: stable_hash(row[2])
    )
    return amount, {
        "status": "RESOLVED",
        "candidate_count": len(candidates),
        "account_id": str(selected.get("account_id") or ""),
        "account_name": str(selected.get("account_nm") or ""),
        "currency": "KRW",
        "corp_code": expected_corp_code,
        "fiscal_year": expected_fiscal_year,
        "report_code": expected_report_code,
        "rcept_no": str(selected.get("rcept_no") or ""),
        "rcept_date": received_at.isoformat(),
        "requested_fs_div": "CFS",
        "parent_equity_row_hash": stable_hash(selected),
        "rejected_reasons": rejected_reasons,
    }


def _opendart_filing_period_end(
    payload: Mapping[str, Any],
    *,
    cutoff: date,
    expected_corp_code: str,
    expected_rcept_no: str,
    expected_report_code: str,
    expected_period_end: date,
) -> tuple[date | None, Mapping[str, Any]]:
    """Verify the fiscal period from the dated DART filing title itself.

    Receipt timing is not a fiscal-calendar proof: a non-December issuer can
    file inside the same month as a December issuer.  DART's cutoff-valid
    disclosure list names the actual report period, for example
    ``분기보고서 (2026.03)``.  Only an exact receipt-number match whose named
    year/month equals the requested balance-sheet period is accepted.
    """

    status = str(payload.get("status") or "")
    if status != "000":
        return None, {"status": "DART_STATUS_ERROR", "dart_status": status}
    rows = payload.get("list") or ()
    if not isinstance(rows, (list, tuple)):
        return None, {"status": "DART_ROWS_INVALID"}
    expected_kind = {
        "11013": "분기보고서",
        "11012": "반기보고서",
        "11014": "분기보고서",
        "11011": "사업보고서",
    }.get(expected_report_code)
    candidates: list[tuple[date, Mapping[str, Any]]] = []
    rejected_reasons: dict[str, int] = {}
    for raw in rows:
        if not isinstance(raw, Mapping):
            continue
        if str(raw.get("rcept_no") or "") != expected_rcept_no:
            continue
        corp_code = str(raw.get("corp_code") or "").strip()
        if corp_code.isdigit():
            corp_code = corp_code.zfill(8)
        if corp_code != expected_corp_code:
            rejected_reasons["CORP_CODE_MISMATCH"] = 1
            continue
        receipt_text = str(raw.get("rcept_dt") or "")
        try:
            receipt_date = date.fromisoformat(
                f"{receipt_text[:4]}-{receipt_text[4:6]}-{receipt_text[6:8]}"
            )
        except ValueError:
            rejected_reasons["RECEIPT_DATE_INVALID"] = 1
            continue
        if receipt_text != expected_rcept_no[:8]:
            rejected_reasons["RECEIPT_DATE_MISMATCH"] = 1
            continue
        if receipt_date > cutoff:
            rejected_reasons["FUTURE_RECEIPT_REJECTED"] = 1
            continue
        report_name = str(raw.get("report_nm") or "")
        if expected_kind is None or expected_kind not in report_name:
            rejected_reasons["REPORT_KIND_MISMATCH"] = 1
            continue
        period_tokens = re.findall(r"\((\d{4})[./-](\d{2})\)", report_name)
        if len(set(period_tokens)) != 1:
            rejected_reasons["FILING_PERIOD_TOKEN_UNVERIFIED"] = 1
            continue
        year_text, month_text = period_tokens[0]
        try:
            period_end = date(
                int(year_text),
                int(month_text),
                _month_end(int(year_text), int(month_text)),
            )
        except ValueError:
            rejected_reasons["FILING_PERIOD_TOKEN_INVALID"] = 1
            continue
        if period_end != expected_period_end:
            rejected_reasons["FILING_PERIOD_END_MISMATCH"] = 1
            continue
        candidates.append((period_end, raw))
    if len(candidates) != 1:
        return None, {
            "status": "FILING_PERIOD_END_UNVERIFIED",
            "candidate_count": len(candidates),
            "rejected_reasons": rejected_reasons,
        }
    period_end, selected = candidates[0]
    return period_end, {
        "status": "RESOLVED",
        "rcept_no": expected_rcept_no,
        "report_name": str(selected.get("report_nm") or ""),
        "period_end": period_end.isoformat(),
        "period_end_authority": "OPENDART_DISCLOSURE_REPORT_NAME",
        "filing_row_hash": stable_hash(selected),
        "rejected_reasons": rejected_reasons,
    }


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


def _companyguide_trailing_valuation_records(
    *,
    target_id: str,
    cutoff: date,
    payload: Mapping[str, Any],
    source_id: str,
) -> tuple[StructuredMetricRecord, ...]:
    if payload.get("TRAILING_VALUATION_DATE_VERIFIED") is not True:
        return ()
    raw_date = str(
        payload.get("TRAILING_VALUATION_AS_OF_DATE") or ""
    ).replace("/", "-")[:10]
    try:
        observed = date.fromisoformat(raw_date)
    except ValueError:
        return ()
    if observed > cutoff:
        return ()
    anchors = payload.get("TRAILING_VALUATION_FIELD_ANCHORS") or {}
    if not isinstance(anchors, Mapping):
        anchors = {}
    specs = (
        (
            "trailing_eps",
            "TRAILING_EPS",
            "CURRENCY_PER_SHARE",
            ("TRAILING_EPS", "CURRENT_VALUATION"),
        ),
        (
            "trailing_bps",
            "TRAILING_BPS",
            "CURRENCY_PER_SHARE",
            ("TRAILING_BPS", "CURRENT_VALUATION"),
        ),
        (
            "trailing_pe",
            "TRAILING_PER",
            "MULTIPLE",
            ("TRAILING_PE", "CURRENT_VALUATION"),
        ),
        (
            "trailing_pb",
            "TRAILING_PBR",
            "MULTIPLE",
            ("TRAILING_PB", "CURRENT_VALUATION"),
        ),
        (
            "provider_previous_close",
            "PROVIDER_PREVIOUS_CLOSE",
            "CURRENCY_PER_SHARE",
            ("CURRENT_PRICE", "CURRENT_VALUATION"),
        ),
    )
    records: list[StructuredMetricRecord] = []
    for metric_id, payload_key, unit, roles in specs:
        value = _float(payload.get(payload_key))
        if value is None:
            continue
        records.append(
            StructuredMetricRecord(
                record_id="STRUCT-" + stable_hash(
                    {
                        "target_id": target_id,
                        "metric_namespace": "TRAILING_ACTUAL",
                        "metric_id": metric_id,
                        "value": value,
                        "observed_at": observed.isoformat(),
                        "source_id": source_id,
                    }
                )[:24],
                target_id=target_id,
                as_of_date=cutoff.isoformat(),
                metric_id=metric_id,
                value=value,
                unit=unit,
                period=f"TRAILING_AS_OF_{observed.isoformat()}",
                evidence_roles=roles,
                source_ids=(source_id,),
                source_route="COMPANYGUIDE",
                observed_at=observed.isoformat(),
                available_at=observed.isoformat(),
                record_kind="PROVIDER_TRAILING_VALUATION_SNAPSHOT",
                confidence=0.9,
                dataset="VALUATION",
                provenance="STRUCTURED_EXTRACTED",
                metadata={
                    "structured_source": True,
                    "provider_name": "CompanyGuide",
                    "metric_namespace": "TRAILING_ACTUAL",
                    "provider_field": payload_key,
                    "field_anchor": anchors.get(payload_key),
                    "provider_published_value": True,
                    "forward_value": False,
                    "date_verified": True,
                    "snippet_only": False,
                },
            )
        )
    return tuple(records)


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


def _dedupe_companyguide_reports(
    reports: Sequence[ResearchReport],
) -> tuple[tuple[ResearchReport, ...], int]:
    """Collapse provider page overlap before structured ids are compiled.

    CompanyGuide's archive may advance pages by fewer rows than ``perPage``;
    the same provider report can therefore appear at both page boundaries.
    The provider report id/file name is transport identity, so keeping its
    first occurrence preserves one source lineage without merging unrelated
    reports or hiding the overlap from the pagination audit.
    """

    deduped: dict[tuple[str, ...], ResearchReport] = {}
    duplicate_count = 0
    for report in reports:
        parsed = dict(report.parsed_fields)
        report_id = str(parsed.get("report_id") or "").strip()
        file_name = str(parsed.get("file_name") or "").strip()
        provider_index = str(parsed.get("idx") or "").strip()
        if report_id:
            identity = ("REPORT_ID", report_id)
        elif file_name:
            identity = ("FILE_NAME", file_name.casefold())
        elif provider_index:
            identity = ("PROVIDER_INDEX", provider_index)
        else:
            identity = (
                "SEMANTIC_FALLBACK",
                report.broker.casefold(),
                report.publish_date.isoformat(),
                report.title.casefold(),
            )
        if identity in deduped:
            duplicate_count += 1
            continue
        deduped[identity] = report
    return tuple(deduped.values()), duplicate_count


def _companyguide_report_source_candidate(
    report: ResearchReport,
    *,
    target_id: str,
    cutoff: date,
) -> Mapping[str, Any] | None:
    parsed = dict(report.parsed_fields)
    source_id = str(parsed.get("structured_page_source_id") or "").strip()
    file_name = str(parsed.get("file_name") or "").strip()
    report_id = str(parsed.get("report_id") or "").strip()
    provider_index = str(parsed.get("idx") or "").strip()
    if not source_id or not (file_name or report_id or provider_index):
        return None
    if report.publish_date > cutoff:
        return None
    identity = {
        "target_id": target_id,
        "published_at": report.publish_date.isoformat(),
        "broker": report.broker,
        "title": report.title,
        "report_id": report_id,
        "provider_index": provider_index,
        "file_name": file_name,
        "metadata_source_id": source_id,
    }
    return {
        "schema_version": "e2r_v5_structured_report_source_candidate_v1",
        "candidate_id": "STRUCTCAND-" + stable_hash(identity)[:24],
        "target_id": target_id,
        "as_of_date": cutoff.isoformat(),
        "provider_name": "CompanyGuide",
        "source_family_hint": "PUBLIC_BROKER_PDF",
        "research_route": "PUBLIC_BROKER_REPORT",
        "discovery_origin": "STRUCTURED_PROVIDER_METADATA",
        "published_at": report.publish_date.isoformat(),
        "available_at": report.publish_date.isoformat(),
        "broker": report.broker,
        "title": report.title,
        "provider_report_id": report_id or None,
        "provider_index": provider_index or None,
        "provider_file_name": file_name or None,
        "provider_page": parsed.get("provider_page"),
        "metadata_source_ids": [source_id],
        "provider_summary": str(parsed.get("comment") or report.raw_text or ""),
        "structured_fields": {
            "close_price": report.current_price,
            "target_price": report.target_price,
            "fy1_eps": report.fy1_eps,
            "est_per": report.est_per,
        },
        "canonical_url": None,
        "url_resolution_required": True,
        "full_document_owner": "LLM_SOURCE_GRAPH",
        "full_fetch_performed": False,
        "evidence_eligible": False,
        "snippet_only": True,
        "snippet_used_as_document": False,
        "deterministic_url_synthesis": False,
        "deterministic_query_synthesis": False,
        "production_score_authority": False,
    }


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
    source_id: str | None = None,
) -> tuple[StructuredMetricRecord, ...]:
    records: list[StructuredMetricRecord] = []
    for report in reports:
        report_id = str(
            report.parsed_fields.get("report_id")
            or stable_hash((report.broker, report.publish_date.isoformat(), report.title))[:16]
        )
        effective_source_id = str(
            report.parsed_fields.get("structured_page_source_id")
            or source_id
            or ""
        ).strip()
        if not effective_source_id:
            continue
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
                    source_ids=(effective_source_id,),
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


def _krx_listing_identity_roster(
    payload: Mapping[str, Any],
    *,
    target_id: str,
    snapshot_date: date,
) -> tuple[Mapping[str, str], ...]:
    """Project the complete point-in-time KRX symbol/name identity plane.

    The roster gives the LLM valid identities to choose from; it does not rank
    peers or provide valuation values.  CompanyGuide still verifies every
    selected identity and multiple independently.
    """

    rows = payload.get("OutBlock_1") or ()
    if not isinstance(rows, Sequence) or isinstance(rows, (str, bytes)):
        return ()
    expected_date = snapshot_date.strftime("%Y%m%d")
    identities: dict[str, str] = {}
    ambiguous: set[str] = set()
    for row in rows:
        if not isinstance(row, Mapping):
            continue
        if str(row.get("BAS_DD") or "") != expected_date:
            continue
        symbol = str(row.get("ISU_CD") or row.get("ISU_SRT_CD") or "").strip()
        name = str(row.get("ISU_NM") or "").strip()
        if (
            symbol == target_id
            or len(symbol) != 6
            or not symbol.isdigit()
            or not name
        ):
            continue
        previous = identities.get(symbol)
        if previous is not None and previous != name:
            ambiguous.add(symbol)
            continue
        identities[symbol] = name
    return tuple(
        {"peer_symbol": symbol, "peer_name": identities[symbol]}
        for symbol in sorted(identities)
        if symbol not in ambiguous
    )


def _krx_listing_snapshot_accounting(
    payload: Mapping[str, Any],
    *,
    target_id: str,
    snapshot_date: date,
) -> Mapping[str, Any]:
    """Prove that one KRX market identity plane was consumed without top-N."""

    raw_rows = payload.get("OutBlock_1") or ()
    if isinstance(raw_rows, (str, bytes)) or not isinstance(
        raw_rows, Sequence
    ):
        raw_rows = ()
    expected_date = snapshot_date.strftime("%Y%m%d")
    target_rows: list[Mapping[str, Any]] = []
    eligible_rows_by_symbol: dict[str, list[Mapping[str, Any]]] = {}
    non_peer_eligible_rows: list[Mapping[str, Any]] = []
    malformed_rows: list[Any] = []
    non_snapshot_rows: list[Mapping[str, Any]] = []
    for raw in raw_rows:
        if not isinstance(raw, Mapping):
            malformed_rows.append(raw)
            continue
        if str(raw.get("BAS_DD") or "") != expected_date:
            non_snapshot_rows.append(raw)
            continue
        symbol = str(
            raw.get("ISU_CD") or raw.get("ISU_SRT_CD") or ""
        ).strip()
        name = str(raw.get("ISU_NM") or "").strip()
        if not symbol or not name:
            malformed_rows.append(raw)
        elif symbol == target_id:
            target_rows.append(raw)
        elif len(symbol) == 6 and symbol.isdigit():
            eligible_rows_by_symbol.setdefault(symbol, []).append(raw)
        else:
            # Preferred shares and SPAC identifiers can contain letters.  They
            # are fully accounted source rows but cannot satisfy the provider
            # contract requiring a six-digit numeric common-stock identity.
            non_peer_eligible_rows.append(raw)

    identities: list[Mapping[str, str]] = []
    duplicate_identity_row_count = 0
    ambiguous_identity_row_count = 0
    for symbol, rows in eligible_rows_by_symbol.items():
        names = {
            _company_name_key(str(row.get("ISU_NM") or "").strip())
            for row in rows
        }
        if len(names) != 1:
            ambiguous_identity_row_count += len(rows)
            continue
        if len(rows) != 1:
            duplicate_identity_row_count += len(rows)
            continue
        identities.append(
            {
                "peer_symbol": symbol,
                "peer_name": str(rows[0].get("ISU_NM") or "").strip(),
            }
        )
    identities = sorted(identities, key=lambda row: row["peer_symbol"])
    exact_snapshot_row_count = (
        len(target_rows)
        + sum(len(rows) for rows in eligible_rows_by_symbol.values())
        + len(non_peer_eligible_rows)
        + sum(
            1
            for raw in malformed_rows
            if isinstance(raw, Mapping)
            and str(raw.get("BAS_DD") or "") == expected_date
        )
    )
    accounted_exact_snapshot_row_count = (
        len(target_rows)
        + len(identities)
        + duplicate_identity_row_count
        + ambiguous_identity_row_count
        + len(non_peer_eligible_rows)
        + sum(
            1
            for raw in malformed_rows
            if isinstance(raw, Mapping)
            and str(raw.get("BAS_DD") or "") == expected_date
        )
    )
    unaccounted_exact_snapshot_row_count = (
        exact_snapshot_row_count - accounted_exact_snapshot_row_count
    )
    return {
        "identities": identities,
        "raw_row_count": len(raw_rows),
        "exact_snapshot_row_count": exact_snapshot_row_count,
        "identity_count": len(identities),
        "target_row_count": len(target_rows),
        "non_peer_eligible_security_row_count": len(
            non_peer_eligible_rows
        ),
        "duplicate_identity_row_count": duplicate_identity_row_count,
        "ambiguous_identity_row_count": ambiguous_identity_row_count,
        "malformed_row_count": len(malformed_rows),
        "non_snapshot_row_count": len(non_snapshot_rows),
        "unaccounted_exact_snapshot_row_count": (
            unaccounted_exact_snapshot_row_count
        ),
        "all_rows_accounted": (
            unaccounted_exact_snapshot_row_count == 0
            and not malformed_rows
            and not non_snapshot_rows
        ),
        "complete_identity_plane": (
            bool(identities)
            and len(target_rows) <= 1
            and duplicate_identity_row_count == 0
            and ambiguous_identity_row_count == 0
            and unaccounted_exact_snapshot_row_count == 0
            and not malformed_rows
            and not non_snapshot_rows
        ),
    }


def _merge_listing_identity_rosters(
    rows: Sequence[Mapping[str, str]],
) -> tuple[Mapping[str, str], ...]:
    """Merge bounded KRX market identity planes without choosing peers.

    A symbol whose legal name conflicts across source rows is omitted instead
    of letting market iteration order decide its identity.
    """

    identities: dict[str, str] = {}
    ambiguous: set[str] = set()
    for row in rows:
        symbol = str(row.get("peer_symbol") or "").strip()
        name = str(row.get("peer_name") or "").strip()
        if not symbol or not name:
            continue
        previous = identities.get(symbol)
        if previous is not None and _company_name_key(previous) != _company_name_key(
            name
        ):
            ambiguous.add(symbol)
            continue
        identities[symbol] = name
    return tuple(
        {"peer_symbol": symbol, "peer_name": identities[symbol]}
        for symbol in sorted(identities)
        if symbol not in ambiguous
    )


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
