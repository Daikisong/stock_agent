"""Official-only issuer/business profiles for Phase-105 forced canaries.

The ordinary current planner may abstain when a weak trigger says only that a
filing exists.  This module does not turn that abstention into a score or a
Stage.  It builds a separate, pre-deep compatibility receipt from:

* current eligible KRX listing rows, with a separately receipted full-universe
  forced discovery lane;
* the OpenDART corp-code and company-profile identities;
* the latest periodic report available by the as-of date; and
* bounded Codex Collaboration classifications that account for the exact five
  Phase-105 archetypes, supported by literal quotations from the full report.

No company-name or symbol allowlist is used.  Deterministic code validates
identity, dates, hashes, taxonomy, quotation membership, uniqueness, budgets,
and authority; it never invents a business mechanism.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from datetime import date, timedelta
from functools import lru_cache
import hashlib
import io
import json
import re
from typing import Any, Protocol
import xml.etree.ElementTree as ET
import zipfile

import requests

from e2r.calibration.taxonomy import large_sector_for_archetype
from e2r.production.metadata import stable_hash


PROFILE_SCHEMA_VERSION = "e2r_v6_issuer_business_profile_v1"
PROFILE_RESULT_SCHEMA_VERSION = "e2r_v6_issuer_business_profile_result_v2"
COMPATIBILITY_RECEIPT_SCHEMA_VERSION = (
    "e2r_v6_issuer_business_compatibility_receipt_v1"
)
PROFILE_SELECTION_RECEIPT_SCHEMA_VERSION = (
    "e2r_v6_issuer_business_profile_selection_receipt_v1"
)
CANDIDATE_EXPANSION_RECEIPT_SCHEMA_VERSION = (
    "e2r_v6_issuer_business_candidate_expansion_receipt_v2"
)
INDUSTRY_DISCOVERY_SCHEMA_VERSION = "e2r_v6_opendart_industry_discovery_v1"
PROFILE_PASS = "COMPLETE"
PROFILE_PENDING = "PENDING"
PROFILE_ABSTAINED = "ABSTAINED"
PROFILE_TEST_ONLY = "TEST_ONLY"
CANONICAL_COMPATIBILITY_PROVIDER = (
    "codex_collaboration_issuer_business_profile"
)

_DISCOVERY_CANDIDATE_INELIGIBLE_DETAILS = frozenset(
    {
        "OpenDART discovery corp-code identity does not match KRX",
        "OpenDART discovery company identity or industry code is invalid",
    }
)

REQUIRED_ARCHETYPES = (
    "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
    "C15_MATERIAL_SPREAD_SUPERCYCLE",
    "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD",
    "C24_BIO_TRIAL_DATA_EVENT_RISK",
    "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
)

_CORP_CODE_URL = "https://opendart.fss.or.kr/api/corpCode.xml"
_COMPANY_URL = "https://opendart.fss.or.kr/api/company.json"
_LIST_URL = "https://opendart.fss.or.kr/api/list.json"
_DOCUMENT_URL = "https://opendart.fss.or.kr/api/document.xml"
_DART_VIEWER_URL = "https://dart.fss.or.kr/dsaf001/main.do"
_KRX_BASE = "https://data-dbg.krx.co.kr/svc/apis/sto"
_KRX_ENDPOINTS = {"KOSPI": "stk_isu_base_info", "KOSDAQ": "ksq_isu_base_info"}
_PERIODIC_REPORT_TOKENS = ("사업보고서", "반기보고서", "분기보고서")
_TARGET_RE = re.compile(r"^[0-9A-Z]{6}$")
_HEX64_RE = re.compile(r"^[0-9a-f]{64}$")
_FORBIDDEN_KEY_RE = re.compile(r"(?:score|stage|gold)", re.IGNORECASE)


def large_sector_for_industry_code(industry_code: object) -> str | None:
    """Map an official KSIC/OpenDART code without using issuer names.

    The first two digits ``21`` mean pharmaceutical manufacturing in KSIC.
    The older shadow-only mapper incorrectly grouped them with materials.
    """

    code = "".join(character for character in str(industry_code or "") if character.isdigit())
    if not code:
        return None
    first2 = code[:2]
    first3 = code[:3]
    first4 = code[:4]
    if first2 in {"64", "65", "66"} or first3 == "715":
        return "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL"
    if first2 in {"58", "59", "60", "61", "62", "63"}:
        return "L8_PLATFORM_CONTENT_SW_SECURITY"
    if first2 == "26" or first3 in {"281", "282"}:
        return "L2_AI_SEMICONDUCTOR_ELECTRONICS"
    if first2 == "21" or first3 == "701" or first2 in {"27", "86", "87"}:
        return "L7_BIO_HEALTHCARE_MEDICAL"
    if first2 in {"17", "19", "20", "22", "24", "25"}:
        return "L4_MATERIALS_SPREAD_RESOURCE"
    if first2 in {"10", "11", "12", "13", "14", "15", "46", "47", "32", "90", "91"}:
        return "L5_CONSUMER_BRAND_DISTRIBUTION"
    if first2 in {"28", "29", "33", "35", "36", "37", "38", "39", "42"} or first3 == "721":
        return "L1_INDUSTRIALS_INFRA_DEFENSE_GRID"
    if first2 in {"23", "41", "68"}:
        return "L9_CONSTRUCTION_REALESTATE_HOUSING"
    if first2 in {"30", "31", "45", "49", "50", "51", "52", "76"}:
        return "L3_BATTERY_EV_GREEN_MOBILITY"
    if first2 in {"73", "84"} or first4 == "8411":
        return "L10_POLICY_EVENT_CROSS_REDTEAM_MISC"
    return None


@dataclass(frozen=True)
class IssuerBusinessProfileConfig:
    as_of_date: str
    max_profile_fetches: int
    max_list_pages: int = 3
    request_timeout_seconds: float = 30.0
    max_compatibility_prompt_chars: int = 2_000_000
    max_discovery_fetches: int = 3_000
    max_forced_candidates_per_required_slot: int = 10
    test_mode: bool = False

    def __post_init__(self) -> None:
        date.fromisoformat(self.as_of_date)
        if isinstance(self.max_profile_fetches, bool) or not isinstance(
            self.max_profile_fetches, int
        ) or not 1 <= self.max_profile_fetches <= 100:
            raise ValueError("max_profile_fetches must be bounded by 100")
        if isinstance(self.max_list_pages, bool) or not isinstance(
            self.max_list_pages, int
        ) or not 1 <= self.max_list_pages <= 10:
            raise ValueError("OpenDART list pages must be bounded by ten")
        if isinstance(self.request_timeout_seconds, bool) or not isinstance(
            self.request_timeout_seconds, (int, float)
        ) or not 0 < self.request_timeout_seconds <= 120:
            raise ValueError("profile request timeout must be bounded by 120 seconds")
        if isinstance(self.max_compatibility_prompt_chars, bool) or not isinstance(
            self.max_compatibility_prompt_chars, int
        ) or not 10_000 <= self.max_compatibility_prompt_chars <= 5_000_000:
            raise ValueError("compatibility prompt must have a finite bounded size")
        if isinstance(self.max_discovery_fetches, bool) or not isinstance(
            self.max_discovery_fetches, int
        ) or not 1 <= self.max_discovery_fetches <= 5_000:
            raise ValueError("OpenDART industry discovery must be bounded by 5,000")
        if isinstance(
            self.max_forced_candidates_per_required_slot, bool
        ) or not isinstance(self.max_forced_candidates_per_required_slot, int) or not 1 <= (
            self.max_forced_candidates_per_required_slot
        ) <= 10:
            raise ValueError("forced candidates per required slot must be bounded by ten")
        if not isinstance(self.test_mode, bool):
            raise ValueError("test_mode must be a boolean")


@dataclass(frozen=True)
class CompatibilityProviderCompletion:
    payload: Mapping[str, Any]
    raw_response: str


class IssuerBusinessProfileFetcher(Protocol):
    """Injectable official network boundary used by the materializer."""

    provider_name: str

    def discover_industry(
        self,
        *,
        target_id: str,
        company_name: str,
        as_of_date: date,
        credential: str,
        timeout_seconds: float,
    ) -> Mapping[str, Any]:
        ...

    def fetch(
        self,
        *,
        target_id: str,
        company_name: str,
        as_of_date: date,
        credential: str,
        max_list_pages: int,
        timeout_seconds: float,
    ) -> Mapping[str, Any]:
        ...


class IssuerBusinessCompatibilityProvider(Protocol):
    provider_name: str
    real_provider: bool
    fake_provider: bool

    def complete(
        self,
        *,
        prompt: str,
        output_schema: Mapping[str, Any],
    ) -> CompatibilityProviderCompletion:
        ...


class RequestsOpenDartIssuerBusinessProfileFetcher:
    """Fetch the exact official OpenDART identity/report bundle."""

    provider_name = "OpenDART"

    def __init__(self) -> None:
        self._corp_code_text: str | None = None

    def discover_industry(
        self,
        *,
        target_id: str,
        company_name: str,
        as_of_date: date,
        credential: str,
        timeout_seconds: float,
    ) -> Mapping[str, Any]:
        """Fetch only official identity and industry code before full reports."""

        request_count = 0
        try:
            if self._corp_code_text is None:
                response = requests.get(
                    _CORP_CODE_URL,
                    params={"crtfc_key": credential},
                    timeout=(5.0, timeout_seconds),
                )
                request_count += 1
                response.raise_for_status()
                self._corp_code_text = _decode_corp_code_payload(response.content)
            corp_text = self._corp_code_text
            corp_row = _corp_row(corp_text, target_id=target_id)
            if corp_row is None:
                return _pending_discovery(
                    target_id=target_id,
                    company_name=company_name,
                    error_category="OPENDART_SYMBOL_NOT_FOUND",
                    request_count=request_count,
                )
            corp_code = str(corp_row["corp_code"])
            company_response = requests.get(
                _COMPANY_URL,
                params={"crtfc_key": credential, "corp_code": corp_code},
                timeout=(5.0, timeout_seconds),
            )
            request_count += 1
            company_response.raise_for_status()
            company_text = company_response.text
            return {
                "status": "DISCOVERED",
                "provider_name": self.provider_name,
                "target_id": target_id,
                "company_name": company_name,
                "request_count": request_count,
                "corp_code_receipt": _source_receipt(
                    role="CORP_CODE_IDENTITY",
                    target_id=target_id,
                    as_of_date=as_of_date,
                    canonical_url=_CORP_CODE_URL,
                    request_params={},
                    response_text=corp_text,
                ),
                "company_receipt": _source_receipt(
                    role="COMPANY_IDENTITY",
                    target_id=target_id,
                    as_of_date=as_of_date,
                    canonical_url=_COMPANY_URL,
                    request_params={"corp_code": corp_code},
                    response_text=company_text,
                ),
                "error_category": None,
            }
        except (
            requests.RequestException,
            RuntimeError,
            TypeError,
            ValueError,
            json.JSONDecodeError,
            ET.ParseError,
        ) as exc:
            return _pending_discovery(
                target_id=target_id,
                company_name=company_name,
                error_category=f"OPENDART_PROVIDER_FAILURE:{type(exc).__name__}",
                request_count=request_count,
            )

    def fetch(
        self,
        *,
        target_id: str,
        company_name: str,
        as_of_date: date,
        credential: str,
        max_list_pages: int,
        timeout_seconds: float,
    ) -> Mapping[str, Any]:
        request_count = 0
        try:
            if self._corp_code_text is None:
                response = requests.get(
                    _CORP_CODE_URL,
                    params={"crtfc_key": credential},
                    timeout=(5.0, timeout_seconds),
                )
                request_count += 1
                response.raise_for_status()
                self._corp_code_text = _decode_corp_code_payload(response.content)
            corp_text = self._corp_code_text
            corp_row = _corp_row(corp_text, target_id=target_id)
            if corp_row is None:
                return _pending_fetch(
                    target_id=target_id,
                    company_name=company_name,
                    error_category="OPENDART_SYMBOL_NOT_FOUND",
                    request_count=request_count,
                )
            corp_code = corp_row["corp_code"]
            company_response = requests.get(
                _COMPANY_URL,
                params={"crtfc_key": credential, "corp_code": corp_code},
                timeout=(5.0, timeout_seconds),
            )
            request_count += 1
            company_response.raise_for_status()
            company_text = company_response.text
            list_texts: list[str] = []
            total_pages = 1
            for page_number in range(1, max_list_pages + 1):
                list_response = requests.get(
                    _LIST_URL,
                    params={
                        "crtfc_key": credential,
                        "corp_code": corp_code,
                        "bgn_de": (as_of_date - timedelta(days=540)).strftime("%Y%m%d"),
                        "end_de": as_of_date.strftime("%Y%m%d"),
                        "page_no": page_number,
                        "page_count": 100,
                    },
                    timeout=(5.0, timeout_seconds),
                )
                request_count += 1
                list_response.raise_for_status()
                list_texts.append(list_response.text)
                list_payload = json.loads(list_response.text)
                status = str(list_payload.get("status") or "")
                if status not in {"000", "013"}:
                    raise RuntimeError(
                        "OpenDART list failure: "
                        + status
                        + " "
                        + str(list_payload.get("message") or "")
                    )
                total_pages = int(list_payload.get("total_page") or 1)
                if status == "013" or page_number >= total_pages:
                    break
            if total_pages > len(list_texts):
                return _pending_fetch(
                    target_id=target_id,
                    company_name=company_name,
                    error_category="OPENDART_LIST_PAGE_BUDGET_EXHAUSTED",
                    request_count=request_count,
                )
            latest = _latest_periodic_row(
                list_texts,
                corp_code=corp_code,
                as_of_date=as_of_date,
            )
            if latest is None:
                return _pending_fetch(
                    target_id=target_id,
                    company_name=company_name,
                    error_category="OPENDART_PERIODIC_REPORT_NOT_FOUND",
                    request_count=request_count,
                )
            rcept_no = str(latest["rcept_no"])
            document_response = requests.get(
                _DOCUMENT_URL,
                params={"crtfc_key": credential, "rcept_no": rcept_no},
                timeout=(5.0, timeout_seconds),
            )
            request_count += 1
            document_response.raise_for_status()
            document_text = _decode_document_payload(document_response.content)
            return {
                "status": "FETCHED",
                "provider_name": self.provider_name,
                "target_id": target_id,
                "company_name": company_name,
                "request_count": request_count,
                "corp_code_receipt": _source_receipt(
                    role="CORP_CODE_IDENTITY",
                    target_id=target_id,
                    as_of_date=as_of_date,
                    canonical_url=_CORP_CODE_URL,
                    request_params={},
                    response_text=corp_text,
                ),
                "company_receipt": _source_receipt(
                    role="COMPANY_IDENTITY",
                    target_id=target_id,
                    as_of_date=as_of_date,
                    canonical_url=_COMPANY_URL,
                    request_params={"corp_code": corp_code},
                    response_text=company_text,
                ),
                "list_receipts": [
                    _source_receipt(
                        role="PERIODIC_REPORT_LIST",
                        target_id=target_id,
                        as_of_date=as_of_date,
                        canonical_url=_LIST_URL,
                        request_params={
                            "corp_code": corp_code,
                            "bgn_de": (as_of_date - timedelta(days=540)).strftime("%Y%m%d"),
                            "end_de": as_of_date.strftime("%Y%m%d"),
                            "page_no": page_number,
                            "page_count": 100,
                        },
                        response_text=text,
                    )
                    for page_number, text in enumerate(list_texts, start=1)
                ],
                "document_receipt": {
                    **_source_receipt(
                        role="PERIODIC_REPORT_DOCUMENT",
                        target_id=target_id,
                        as_of_date=as_of_date,
                        canonical_url=_DOCUMENT_URL,
                        request_params={"rcept_no": rcept_no},
                        response_text=document_text,
                    ),
                    "official_document_id": f"opendart:disclosure:{rcept_no}",
                    "viewer_url": f"{_DART_VIEWER_URL}?rcpNo={rcept_no}",
                    "rcept_no": rcept_no,
                    "available_date": _yyyymmdd_to_iso(latest["rcept_dt"]),
                },
                "error_category": None,
            }
        except (requests.RequestException, RuntimeError, TypeError, ValueError, json.JSONDecodeError, ET.ParseError) as exc:
            return _pending_fetch(
                target_id=target_id,
                company_name=company_name,
                error_category=f"OPENDART_PROVIDER_FAILURE:{type(exc).__name__}",
                request_count=request_count,
            )


class V6IssuerBusinessProfileMaterializer:
    """Build forced-canary compatibility receipts without score authority."""

    def materialize(
        self,
        config: IssuerBusinessProfileConfig,
        *,
        universe_rows: Sequence[Mapping[str, Any]],
        discovery_universe_rows: Sequence[Mapping[str, Any]] = (),
        credential: str | None,
        fetcher: IssuerBusinessProfileFetcher,
        compatibility_provider: IssuerBusinessCompatibilityProvider,
    ) -> Mapping[str, Any]:
        if fetcher.provider_name != "OpenDART":
            raise ValueError("issuer profile fetcher must be official-only OpenDART")
        if not credential:
            expansion_pending = (
                ({"code": "FORCED_DISCOVERY_CREDENTIAL_PENDING"},)
                if discovery_universe_rows
                else ()
            )
            expansion_receipt = (
                _candidate_expansion_receipt(
                    config=config,
                    natural_candidates=(),
                    full_krx_candidate_count=len(discovery_universe_rows),
                    discovery_pool_count=len(discovery_universe_rows),
                    discovery_fetch_count=0,
                    expanded_candidates=(),
                    pending=expansion_pending,
                    status="PENDING",
                    stop_reason="CREDENTIAL_PENDING",
                )
                if discovery_universe_rows
                else _not_requested_candidate_expansion_receipt(config)
            )
            return validate_forced_validation_profile_manifest(_result(
                config=config,
                profiles=(),
                selections=(),
                receipts=(),
                pending=({"code": "OPENDART_CREDENTIAL_MISSING"},),
                fetch_count=0,
                stopped_on_five=False,
                provider_status="NOT_CALLED",
                candidate_expansion_receipt=expansion_receipt,
            ))
        candidates: list[Mapping[str, Any]] = []
        invalid_inputs: list[Mapping[str, Any]] = []
        seen_targets: set[str] = set()
        for index, row in enumerate(universe_rows):
            try:
                candidate = _validate_krx_row(row, as_of_date=config.as_of_date)
                target = str(candidate["symbol"])
                if target in seen_targets:
                    raise ValueError("duplicate KRX target")
                seen_targets.add(target)
                candidates.append(candidate)
            except (TypeError, ValueError) as exc:
                invalid_inputs.append(
                    {"code": "INVALID_KRX_CANDIDATE", "index": index, "detail": str(exc)}
                )
        expansion_receipt = _not_requested_candidate_expansion_receipt(config)
        if discovery_universe_rows:
            expanded_candidates, expansion_receipt = _expand_forced_candidates(
                config=config,
                natural_candidates=candidates,
                discovery_universe_rows=discovery_universe_rows,
                credential=credential,
                fetcher=fetcher,
            )
            for candidate in expanded_candidates:
                target = str(candidate["symbol"])
                if target in seen_targets:
                    raise ValueError("forced discovery duplicated a natural candidate")
                seen_targets.add(target)
            # Discovery candidates are already official-sector filtered.  Give
            # them the bounded full-profile budget first while preserving the
            # original KRX order within both the forced and natural lanes.
            candidates = [*expanded_candidates, *candidates]
        profiles: list[Mapping[str, Any]] = []
        receipts: list[Mapping[str, Any]] = []
        selections: tuple[Mapping[str, Any], ...] = ()
        pending: list[Mapping[str, Any]] = list(invalid_inputs)
        if expansion_receipt["status"] == "PENDING":
            pending.append(
                {
                    "code": "FORCED_DISCOVERY_PENDING",
                    "receipt_id": expansion_receipt["receipt_id"],
                }
            )
            return validate_forced_validation_profile_manifest(
                _result(
                    config=config,
                    profiles=(),
                    selections=(),
                    receipts=(),
                    pending=tuple(_deduplicated_rows(pending)),
                    fetch_count=0,
                    stopped_on_five=False,
                    provider_status="NOT_CALLED",
                    candidate_expansion_receipt=expansion_receipt,
                )
            )
        provider_status = "NOT_CALLED"
        stopped_on_five = False
        fetch_count = 0
        compatibility_call_counter = [0]
        for candidate in candidates:
            if fetch_count >= config.max_profile_fetches:
                break
            fetch_count += 1
            bundle = fetcher.fetch(
                target_id=str(candidate["symbol"]),
                company_name=str(candidate["company_name"]),
                as_of_date=date.fromisoformat(config.as_of_date),
                credential=credential,
                max_list_pages=config.max_list_pages,
                timeout_seconds=config.request_timeout_seconds,
            )
            try:
                profile, full_document = validate_issuer_business_profile(
                    krx_row=candidate,
                    opendart_bundle=bundle,
                    as_of_date=config.as_of_date,
                )
            except (TypeError, ValueError, json.JSONDecodeError, ET.ParseError) as exc:
                pending.append(
                    {
                        "code": "OFFICIAL_PROFILE_PENDING",
                        "target_id": candidate["symbol"],
                        "detail": str(exc),
                    }
                )
                continue
            profiles.append({**profile, "_full_document": full_document})
            if not _sector_quota_available(profiles):
                continue
            try:
                selected, classification_receipts = _classify_profiles_bounded(
                    as_of_date=config.as_of_date,
                    profiles=profiles,
                    provider=compatibility_provider,
                    test_mode=config.test_mode,
                    max_prompt_chars=config.max_compatibility_prompt_chars,
                    max_calls=config.max_profile_fetches,
                    call_counter=compatibility_call_counter,
                )
            except (TypeError, ValueError, RuntimeError, json.JSONDecodeError) as exc:
                provider_status = "PENDING"
                pending.append(
                    {"code": "COMPATIBILITY_PROVIDER_OR_OUTPUT_PENDING", "detail": str(exc)}
                )
                break
            known_response_ids = {
                str(row.get("response_id") or "") for row in receipts
            }
            for receipt in classification_receipts:
                response_id = str(receipt.get("response_id") or "")
                if response_id not in known_response_ids:
                    receipts.append(receipt)
                    known_response_ids.add(response_id)
            provider_status = "COMPLETED"
            if len(selected) == len(REQUIRED_ARCHETYPES):
                selections = selected
                stopped_on_five = True
                break
            statuses = {
                str(row.get("status") or "")
                for receipt in classification_receipts
                for row in receipt["decisions"]
            }
            if "PENDING" in statuses:
                pending.append({"code": "COMPATIBILITY_DECISION_PENDING"})
                break
            # ABSTAIN means the currently fetched profiles are insufficient.
            # Continue fetching another generic KRX candidate while budget remains.
        if not selections and fetch_count >= config.max_profile_fetches:
            pending.append({"code": "PROFILE_FETCH_BUDGET_EXHAUSTED"})
        public_profiles = tuple(
            {key: value for key, value in profile.items() if key != "_full_document"}
            for profile in profiles
        )
        full_documents_by_id = {
            str(profile["periodic_report_document_id"]): str(profile["_full_document"])
            for profile in profiles
        }
        result = _result(
            config=config,
            profiles=public_profiles,
            selections=selections,
            receipts=tuple(receipts),
            pending=tuple(_deduplicated_rows(pending)),
            fetch_count=fetch_count,
            stopped_on_five=stopped_on_five,
            provider_status=provider_status,
            candidate_expansion_receipt=expansion_receipt,
        )
        return validate_forced_validation_profile_manifest(
            result,
            full_documents_by_id=full_documents_by_id,
        )


def _validate_krx_row(
    raw: Mapping[str, Any], *, as_of_date: str
) -> Mapping[str, Any]:
    row = dict(raw)
    target = str(row.get("symbol") or "")
    company = str(row.get("company_name") or "").strip()
    market = str(row.get("market") or "")
    effective = date.fromisoformat(str(row.get("source_effective_date") or ""))
    cutoff = date.fromisoformat(as_of_date)
    endpoint = _KRX_ENDPOINTS.get(market)
    expected_url = (
        f"{_KRX_BASE}/{endpoint}"
        f"?basDd={effective.strftime('%Y%m%d')}"
    )
    expected_request = "KRXREQ-" + stable_hash(
        {"market": market, "effective_date": effective.isoformat(), "endpoint": endpoint}
    )[:24]
    raw_fields = row.get("raw_fields")
    if (
        _TARGET_RE.fullmatch(target) is None
        or not company
        or endpoint is None
        or row.get("eligible") is not True
        or row.get("exclusion_reason") is not None
        or row.get("listing_status") != "LISTED"
        or row.get("source_mode") != "LIVE"
        or effective > cutoff
        or effective < cutoff - timedelta(days=7)
        or row.get("source_url") != expected_url
        or row.get("source_request_id") != expected_request
        or _HEX64_RE.fullmatch(str(row.get("source_content_hash") or "")) is None
        or not isinstance(raw_fields, Mapping)
        or str(raw_fields.get("ISU_SRT_CD") or "") != target
    ):
        raise ValueError("KRX issuer identity is not current and canonical")
    return row


def validate_issuer_industry_discovery(
    *,
    krx_row: Mapping[str, Any],
    opendart_bundle: Mapping[str, Any],
    as_of_date: str,
) -> Mapping[str, Any]:
    """Validate one official OpenDART identity/industry light-discovery row."""

    candidate = _validate_krx_row(krx_row, as_of_date=as_of_date)
    bundle = opendart_bundle
    target = str(candidate["symbol"])
    company = str(candidate["company_name"])
    if (
        not isinstance(bundle, Mapping)
        or bundle.get("status") != "DISCOVERED"
        or bundle.get("provider_name") != "OpenDART"
        or str(bundle.get("target_id") or "") != target
        or str(bundle.get("company_name") or "") != company
        or isinstance(bundle.get("request_count"), bool)
        or not isinstance(bundle.get("request_count"), int)
        or int(bundle.get("request_count") or 0) <= 0
        or bundle.get("error_category") is not None
    ):
        raise ValueError(
            "OpenDART industry discovery is pending: "
            + str(bundle.get("error_category") or "invalid bundle")
        )
    corp_receipt = _validate_source_receipt(
        bundle.get("corp_code_receipt"),
        role="CORP_CODE_IDENTITY",
        canonical_url=_CORP_CODE_URL,
        target_id=target,
        as_of_date=as_of_date,
    )
    corp_row = _corp_row(corp_receipt["response_text"], target_id=target)
    if corp_row is None or not _same_company_name(corp_row["corp_name"], company):
        raise ValueError("OpenDART discovery corp-code identity does not match KRX")
    corp_code = str(corp_row["corp_code"])
    company_receipt = _validate_source_receipt(
        bundle.get("company_receipt"),
        role="COMPANY_IDENTITY",
        canonical_url=_COMPANY_URL,
        target_id=target,
        as_of_date=as_of_date,
    )
    if company_receipt["request_params"] != {"corp_code": corp_code}:
        raise ValueError("OpenDART discovery company request scope mismatch")
    company_payload = json.loads(company_receipt["response_text"])
    industry_code = str(company_payload.get("induty_code") or "").strip()
    company_stock_code = str(company_payload.get("stock_code") or "").strip()
    if (
        company_payload.get("status") != "000"
        or str(company_payload.get("corp_code") or "") != corp_code
        or not company_stock_code
        or company_stock_code.zfill(6) != target
        or not _same_company_name(company_payload.get("corp_name"), company)
        or re.fullmatch(r"[0-9]{2,6}", industry_code) is None
    ):
        raise ValueError("OpenDART discovery company identity or industry code is invalid")
    discovery_core = {
        "schema_version": INDUSTRY_DISCOVERY_SCHEMA_VERSION,
        "status": "COMPLETE",
        "target_id": target,
        "company_name": company,
        "as_of_date": as_of_date,
        "krx_row": dict(candidate),
        "krx_row_hash": stable_hash(dict(candidate)),
        "corp_code": corp_code,
        "corp_code_request_id": corp_receipt["request_id"],
        "corp_code_response_hash": corp_receipt["response_hash"],
        "company_profile_request_id": company_receipt["request_id"],
        "company_profile_hash": company_receipt["response_hash"],
        "industry_code": industry_code,
        "large_sector_id": large_sector_for_industry_code(industry_code) or "",
        "official_only": True,
        "forced_validation_authority": False,
        "score_or_stage_authority": False,
        "gold_authority": False,
    }
    return {
        **discovery_core,
        "discovery_id": "PROFILEDISC-" + stable_hash(discovery_core)[:24],
    }


def _required_sector_quotas(
    max_candidates_per_required_slot: int,
) -> tuple[Mapping[str, Any], ...]:
    counts: dict[str, int] = {}
    order: list[str] = []
    for archetype in REQUIRED_ARCHETYPES:
        sector = str(large_sector_for_archetype(archetype) or "")
        if not sector:
            raise ValueError("required archetype lacks a canonical large sector")
        if sector not in counts:
            order.append(sector)
            counts[sector] = 0
        counts[sector] += 1
    return tuple(
        {
            "large_sector_id": sector,
            "required_archetype_count": counts[sector],
            "candidate_quota": counts[sector] * max_candidates_per_required_slot,
        }
        for sector in order
    )


def _candidate_expansion_receipt(
    *,
    config: IssuerBusinessProfileConfig,
    natural_candidates: Sequence[Mapping[str, Any]],
    full_krx_candidate_count: int,
    discovery_pool_count: int,
    discovery_fetch_count: int,
    expanded_candidates: Sequence[Mapping[str, Any]],
    pending: Sequence[Mapping[str, Any]],
    status: str,
    stop_reason: str,
    diagnostics: Sequence[Mapping[str, Any]] = (),
) -> Mapping[str, Any]:
    natural_roster = [str(row["symbol"]) for row in natural_candidates]
    expanded = [dict(row) for row in expanded_candidates]
    quotas = list(
        _required_sector_quotas(config.max_forced_candidates_per_required_slot)
    )
    expanded_counts = {
        row["large_sector_id"]: sum(
            1
            for candidate in expanded
            if candidate["large_sector_id"] == row["large_sector_id"]
        )
        for row in quotas
    }
    unfilled = [
        {
            "large_sector_id": row["large_sector_id"],
            "missing_candidate_count": row["candidate_quota"]
            - expanded_counts[row["large_sector_id"]],
        }
        for row in quotas
        if expanded_counts[row["large_sector_id"]] < row["candidate_quota"]
    ]
    core = {
        "schema_version": CANDIDATE_EXPANSION_RECEIPT_SCHEMA_VERSION,
        "status": status,
        "selection_mode": "FORCED_VALIDATION_CANARY",
        "as_of_date": config.as_of_date,
        "provider_name": "OpenDART",
        "required_archetypes": list(REQUIRED_ARCHETYPES),
        "required_sector_quotas": quotas,
        "natural_candidate_roster": natural_roster,
        "natural_candidate_roster_hash": stable_hash(natural_roster),
        "full_krx_candidate_count": full_krx_candidate_count,
        "discovery_pool_count": discovery_pool_count,
        "discovery_fetch_count": discovery_fetch_count,
        "max_discovery_fetches": config.max_discovery_fetches,
        "max_forced_candidates_per_required_slot": (
            config.max_forced_candidates_per_required_slot
        ),
        "expanded_candidates": expanded,
        "expanded_candidate_roster_hash": stable_hash(
            [row["discovery_id"] for row in expanded]
        ),
        "unfilled_sector_quotas": unfilled,
        "pending": [dict(row) for row in pending],
        "diagnostics": [dict(row) for row in diagnostics],
        "stop_reason": stop_reason,
        "official_only": True,
        "bounded": True,
        "forced_validation_authority": False,
        "score_or_stage_authority": False,
        "gold_authority": False,
    }
    return {
        **core,
        "receipt_id": "PROFILEEXPAND-" + stable_hash(core)[:24],
    }


def _not_requested_candidate_expansion_receipt(
    config: IssuerBusinessProfileConfig,
) -> Mapping[str, Any]:
    return _candidate_expansion_receipt(
        config=config,
        natural_candidates=(),
        full_krx_candidate_count=0,
        discovery_pool_count=0,
        discovery_fetch_count=0,
        expanded_candidates=(),
        pending=(),
        status="NOT_REQUESTED",
        stop_reason="NOT_REQUESTED",
    )


def _expand_forced_candidates(
    *,
    config: IssuerBusinessProfileConfig,
    natural_candidates: Sequence[Mapping[str, Any]],
    discovery_universe_rows: Sequence[Mapping[str, Any]],
    credential: str,
    fetcher: IssuerBusinessProfileFetcher,
) -> tuple[tuple[Mapping[str, Any], ...], Mapping[str, Any]]:
    natural_targets = {str(row["symbol"]) for row in natural_candidates}
    full_candidates: list[Mapping[str, Any]] = []
    invalid: list[Mapping[str, Any]] = []
    seen: set[str] = set()
    for index, row in enumerate(discovery_universe_rows):
        try:
            candidate = _validate_krx_row(row, as_of_date=config.as_of_date)
            target = str(candidate["symbol"])
            if target in seen:
                raise ValueError("duplicate full-KRX discovery target")
            seen.add(target)
            full_candidates.append(candidate)
        except (TypeError, ValueError) as exc:
            invalid.append(
                {
                    "code": "FORCED_DISCOVERY_INPUT_PENDING",
                    "index": index,
                    "detail": str(exc),
                }
            )
    pool = tuple(
        candidate
        for candidate in full_candidates
        if str(candidate["symbol"]) not in natural_targets
    )
    raw_full_count = len(discovery_universe_rows)
    raw_pool_count = max(0, raw_full_count - len(natural_candidates))
    discover = getattr(fetcher, "discover_industry", None)
    if not callable(discover):
        pending = [
            *invalid,
            {
                "code": "FORCED_DISCOVERY_PROVIDER_PENDING",
                "detail": "OpenDART fetcher lacks industry discovery",
            },
        ]
        return (), _candidate_expansion_receipt(
            config=config,
            natural_candidates=natural_candidates,
            full_krx_candidate_count=raw_full_count,
            discovery_pool_count=raw_pool_count,
            discovery_fetch_count=0,
            expanded_candidates=(),
            pending=pending,
            status="PENDING",
            stop_reason="PROVIDER_PENDING",
        )
    quota_rows = _required_sector_quotas(
        config.max_forced_candidates_per_required_slot
    )
    quotas = {
        str(row["large_sector_id"]): int(row["candidate_quota"])
        for row in quota_rows
    }
    counts = {sector: 0 for sector in quotas}
    expanded_rows: list[Mapping[str, Any]] = []
    expanded_krx_rows: list[Mapping[str, Any]] = []
    pending = list(invalid)
    diagnostics: list[Mapping[str, Any]] = []
    fetch_count = 0
    quotas_filled = False
    for candidate in pool:
        if all(counts[sector] >= quota for sector, quota in quotas.items()):
            quotas_filled = True
            break
        if fetch_count >= config.max_discovery_fetches:
            break
        fetch_count += 1
        bundle = discover(
            target_id=str(candidate["symbol"]),
            company_name=str(candidate["company_name"]),
            as_of_date=date.fromisoformat(config.as_of_date),
            credential=credential,
            timeout_seconds=config.request_timeout_seconds,
        )
        try:
            discovered = validate_issuer_industry_discovery(
                krx_row=candidate,
                opendart_bundle=bundle,
                as_of_date=config.as_of_date,
            )
        except (TypeError, ValueError, json.JSONDecodeError, ET.ParseError) as exc:
            detail = str(exc)
            failure = {
                "target_id": candidate["symbol"],
                "detail": detail,
            }
            if detail in _DISCOVERY_CANDIDATE_INELIGIBLE_DETAILS:
                diagnostics.append(
                    {
                        "code": "FORCED_DISCOVERY_CANDIDATE_INELIGIBLE",
                        **failure,
                    }
                )
            else:
                pending.append(
                    {
                        "code": "FORCED_DISCOVERY_PROVIDER_PENDING",
                        **failure,
                    }
                )
            continue
        sector = str(discovered["large_sector_id"])
        if sector in quotas and counts[sector] < quotas[sector]:
            expanded_rows.append(discovered)
            expanded_krx_rows.append(candidate)
            counts[sector] += 1
    if all(counts[sector] >= quota for sector, quota in quotas.items()):
        quotas_filled = True
    budget_exhausted = (
        not quotas_filled
        and fetch_count >= config.max_discovery_fetches
        and fetch_count < len(pool)
    )
    provider_pending = bool(pending)
    if budget_exhausted:
        pending.append(
            {
                "code": "FORCED_DISCOVERY_BUDGET_PENDING",
                "discovery_fetch_count": fetch_count,
                "discovery_pool_count": len(pool),
            }
        )
    status = "PENDING" if pending or budget_exhausted else "COMPLETE"
    if provider_pending:
        stop_reason = "PROVIDER_PENDING"
    elif budget_exhausted:
        stop_reason = "BUDGET_EXHAUSTED"
    elif quotas_filled:
        stop_reason = "QUOTAS_FILLED"
    else:
        stop_reason = "FULL_KRX_EXHAUSTED"
    receipt = _candidate_expansion_receipt(
        config=config,
        natural_candidates=natural_candidates,
        full_krx_candidate_count=raw_full_count,
        discovery_pool_count=raw_pool_count,
        discovery_fetch_count=fetch_count,
        expanded_candidates=expanded_rows,
        pending=pending,
        status=status,
        stop_reason=stop_reason,
        diagnostics=diagnostics,
    )
    return tuple(expanded_krx_rows), receipt


def validate_issuer_business_profile(
    *,
    krx_row: Mapping[str, Any],
    opendart_bundle: Mapping[str, Any],
    as_of_date: str,
) -> tuple[Mapping[str, Any], str]:
    """Validate one KRX/OpenDART lineage and return its public profile + full text.

    The full text is returned separately so a caller can hand it to the
    Collaboration classifier without persisting it in the compact manifest.
    Every source request/response hash is recomputed before this function
    returns.
    """

    candidate = _validate_krx_row(krx_row, as_of_date=as_of_date)
    bundle = opendart_bundle
    target = str(candidate["symbol"])
    company = str(candidate["company_name"])
    if (
        not isinstance(bundle, Mapping)
        or bundle.get("status") != "FETCHED"
        or bundle.get("provider_name") != "OpenDART"
        or str(bundle.get("target_id") or "") != target
        or str(bundle.get("company_name") or "") != company
        or isinstance(bundle.get("request_count"), bool)
        or not isinstance(bundle.get("request_count"), int)
        or int(bundle.get("request_count") or 0) <= 0
        or bundle.get("error_category") is not None
    ):
        raise ValueError(
            "OpenDART bundle is pending: " + str(bundle.get("error_category") or "invalid bundle")
        )
    corp_receipt = _validate_source_receipt(
        bundle.get("corp_code_receipt"),
        role="CORP_CODE_IDENTITY",
        canonical_url=_CORP_CODE_URL,
        target_id=target,
        as_of_date=as_of_date,
    )
    corp_row = _corp_row(corp_receipt["response_text"], target_id=target)
    if corp_row is None or not _same_company_name(corp_row["corp_name"], company):
        raise ValueError("OpenDART corp-code identity does not match KRX")
    corp_code = str(corp_row["corp_code"])
    company_receipt = _validate_source_receipt(
        bundle.get("company_receipt"),
        role="COMPANY_IDENTITY",
        canonical_url=_COMPANY_URL,
        target_id=target,
        as_of_date=as_of_date,
    )
    if company_receipt["request_params"] != {"corp_code": corp_code}:
        raise ValueError("OpenDART company request scope mismatch")
    company_payload = json.loads(company_receipt["response_text"])
    industry_code = str(company_payload.get("induty_code") or "").strip()
    large_sector = large_sector_for_industry_code(industry_code)
    company_stock_code = str(company_payload.get("stock_code") or "").strip()
    if (
        company_payload.get("status") != "000"
        or str(company_payload.get("corp_code") or "") != corp_code
        or not company_stock_code
        or company_stock_code.zfill(6) != target
        or not _same_company_name(company_payload.get("corp_name"), company)
        or re.fullmatch(r"[0-9]{2,6}", industry_code) is None
        or large_sector is None
    ):
        raise ValueError("OpenDART company identity or industry code is invalid")
    raw_list_receipts = bundle.get("list_receipts")
    if (
        isinstance(raw_list_receipts, (str, bytes))
        or not isinstance(raw_list_receipts, Sequence)
        or not raw_list_receipts
    ):
        raise ValueError("OpenDART periodic report list receipts are missing")
    list_receipts = []
    for page_number, raw_receipt in enumerate(raw_list_receipts, start=1):
        receipt = _validate_source_receipt(
            raw_receipt,
            role="PERIODIC_REPORT_LIST",
            canonical_url=_LIST_URL,
            target_id=target,
            as_of_date=as_of_date,
        )
        expected_params = {
            "corp_code": corp_code,
            "bgn_de": (date.fromisoformat(as_of_date) - timedelta(days=540)).strftime("%Y%m%d"),
            "end_de": date.fromisoformat(as_of_date).strftime("%Y%m%d"),
            "page_no": page_number,
            "page_count": 100,
        }
        if receipt["request_params"] != expected_params:
            raise ValueError("OpenDART list request scope mismatch")
        payload = json.loads(receipt["response_text"])
        if str(payload.get("status") or "") not in {"000", "013"}:
            raise ValueError("OpenDART list receipt is not successful")
        list_receipts.append(receipt)
    first_list_payload = json.loads(list_receipts[0]["response_text"])
    total_pages = int(first_list_payload.get("total_page") or 1)
    if len(list_receipts) != total_pages:
        raise ValueError("OpenDART periodic list page roster is incomplete")
    latest = _latest_periodic_row(
        [row["response_text"] for row in list_receipts],
        corp_code=corp_code,
        as_of_date=date.fromisoformat(as_of_date),
    )
    if latest is None:
        raise ValueError("OpenDART latest periodic report is unavailable")
    document = _validate_source_receipt(
        bundle.get("document_receipt"),
        role="PERIODIC_REPORT_DOCUMENT",
        canonical_url=_DOCUMENT_URL,
        target_id=target,
        as_of_date=as_of_date,
    )
    rcept_no = str(latest.get("rcept_no") or "")
    available_date = _yyyymmdd_to_iso(latest.get("rcept_dt"))
    if (
        document["request_params"] != {"rcept_no": rcept_no}
        or str(document.get("rcept_no") or "") != rcept_no
        or str(document.get("official_document_id") or "")
        != f"opendart:disclosure:{rcept_no}"
        or str(document.get("viewer_url") or "")
        != f"{_DART_VIEWER_URL}?rcpNo={rcept_no}"
        or str(document.get("available_date") or "") != available_date
        or date.fromisoformat(available_date) > date.fromisoformat(as_of_date)
        or len(str(document["response_text"]).strip()) < 80
    ):
        raise ValueError("OpenDART document identity/date/full text is invalid")
    source_hashes = {
        "corp_code_response_hash": corp_receipt["response_hash"],
        "company_response_hash": company_receipt["response_hash"],
        "periodic_list_roster_hash": stable_hash(
            [row["response_hash"] for row in list_receipts]
        ),
        "document_full_text_hash": document["response_hash"],
    }
    profile_core = {
        "schema_version": PROFILE_SCHEMA_VERSION,
        "status": "COMPLETE",
        "target_id": target,
        "company_name": company,
        "as_of_date": as_of_date,
        "krx_row": dict(candidate),
        "krx_row_hash": stable_hash(dict(candidate)),
        "krx_effective_date": candidate["source_effective_date"],
        "krx_request_id": candidate["source_request_id"],
        "krx_content_hash": candidate["source_content_hash"],
        "corp_code": corp_code,
        "corp_code_request_id": corp_receipt["request_id"],
        "corp_code_roster_hash": corp_receipt["response_hash"],
        "industry_code": industry_code,
        "large_sector_id": large_sector,
        "company_profile_request_id": company_receipt["request_id"],
        "company_profile_hash": company_receipt["response_hash"],
        "periodic_list_request_ids": [row["request_id"] for row in list_receipts],
        "periodic_report_request_id": document["request_id"],
        "periodic_report_document_id": document["official_document_id"],
        "periodic_report_rcept_no": rcept_no,
        "periodic_report_available_date": available_date,
        "source_hashes": source_hashes,
        "forced_validation_authority": False,
        "score_or_stage_authority": False,
        "gold_authority": False,
    }
    return {
        **profile_core,
        "profile_id": "ISSUERPROFILE-" + stable_hash(profile_core)[:24],
    }, str(document["response_text"])


def _validate_source_receipt(
    raw: object,
    *,
    role: str,
    canonical_url: str,
    target_id: str,
    as_of_date: str,
) -> Mapping[str, Any]:
    if not isinstance(raw, Mapping):
        raise ValueError(f"{role} receipt is missing")
    receipt = dict(raw)
    response_text = receipt.get("response_text")
    request_params = receipt.get("request_params")
    if not isinstance(response_text, str) or not isinstance(request_params, Mapping):
        raise ValueError(f"{role} receipt body or params are invalid")
    expected_response_hash = _sha256_text(response_text)
    expected_request = _official_request_id(
        role=role,
        target_id=target_id,
        as_of_date=as_of_date,
        request_params=request_params,
    )
    if (
        receipt.get("role") != role
        or receipt.get("provider_name") != "OpenDART"
        or receipt.get("canonical_url") != canonical_url
        or receipt.get("request_id") != expected_request
        or receipt.get("response_hash") != expected_response_hash
    ):
        raise ValueError(f"{role} source/request/response hash mismatch")
    return receipt


def _classify_profiles(
    *,
    as_of_date: str,
    profiles: Sequence[Mapping[str, Any]],
    provider: IssuerBusinessCompatibilityProvider,
    test_mode: bool,
    max_prompt_chars: int,
    required_archetypes: Sequence[str] = REQUIRED_ARCHETYPES,
    prompt_text_by_profile_id: Mapping[str, str] | None = None,
    max_calls: int | None = None,
    call_counter: list[int] | None = None,
) -> tuple[tuple[Mapping[str, Any], ...], Mapping[str, Any]]:
    if not test_mode and (
        provider.provider_name != CANONICAL_COMPATIBILITY_PROVIDER
        or provider.real_provider is not True
        or provider.fake_provider is not False
    ):
        raise ValueError("production profile classification requires Codex Collaboration")
    requested_archetypes = _validated_requested_archetypes(required_archetypes)
    text_overrides = dict(prompt_text_by_profile_id or {})
    profile_ids = {str(row.get("profile_id") or "") for row in profiles}
    if set(text_overrides) - profile_ids:
        raise ValueError("compatibility prompt text override is orphaned")
    prompt_profiles = [
        {
            **{key: value for key, value in row.items() if key != "_full_document"},
            "periodic_report_full_text": text_overrides.get(
                str(row["profile_id"]), str(row["_full_document"])
            ),
        }
        for row in profiles
    ]
    prompt_payload = {
        "as_of_date": as_of_date,
        "required_archetypes": list(requested_archetypes),
        "profiles": prompt_profiles,
        "instructions": (
            "Classify the requested archetype roster exactly. Select only a "
            "mechanism-compatible profile using a literal full-report quote; otherwise "
            "ABSTAIN or PENDING. Do not output a score, Stage, Gold, or recommendation."
        ),
    }
    prompt = json.dumps(prompt_payload, ensure_ascii=False, sort_keys=True)
    if len(prompt) > max_prompt_chars:
        raise ValueError("compatibility prompt exceeds configured bounded size")
    prompt_hash = _sha256_text(prompt)
    request_id = "PROFILECLASSREQ-" + stable_hash(
        {"provider_name": provider.provider_name, "prompt_hash": prompt_hash}
    )[:24]
    if call_counter is not None:
        if (
            len(call_counter) != 1
            or isinstance(call_counter[0], bool)
            or not isinstance(call_counter[0], int)
            or call_counter[0] < 0
        ):
            raise ValueError("compatibility call counter is invalid")
        if max_calls is None or call_counter[0] >= max_calls:
            raise RuntimeError("compatibility call budget exhausted")
        call_counter[0] += 1
    completion = provider.complete(
        prompt=prompt,
        output_schema=_compatibility_schema(requested_archetypes),
    )
    if not isinstance(completion, CompatibilityProviderCompletion):
        raise TypeError("compatibility provider completion type is invalid")
    raw_response = completion.raw_response
    response_hash = _sha256_text(raw_response)
    try:
        decoded = json.loads(raw_response)
    except json.JSONDecodeError as exc:
        raise ValueError("compatibility response is not exact JSON") from exc
    payload = dict(completion.payload)
    if decoded != payload:
        raise ValueError("compatibility raw response and payload differ")
    _assert_no_forbidden_output_keys(payload)
    decisions = payload.get("decisions")
    if (
        not isinstance(decisions, list)
        or len(decisions) != len(requested_archetypes)
        or tuple(str(row.get("archetype_id") or "") for row in decisions if isinstance(row, Mapping))
        != requested_archetypes
        or payload.get("classification_complete") is not True
        or not isinstance(payload.get("unresolved_notes"), list)
        or set(payload) != {"decisions", "classification_complete", "unresolved_notes"}
    ):
        raise ValueError("compatibility response does not account for exact archetype roster")
    profile_by_id = {str(row["profile_id"]): row for row in profiles}
    selected: list[Mapping[str, Any]] = []
    selected_targets: set[str] = set()
    validated_decisions: list[Mapping[str, Any]] = []
    for expected_archetype, raw_decision in zip(requested_archetypes, decisions):
        if not isinstance(raw_decision, Mapping):
            raise ValueError("compatibility decision must be an object")
        decision = dict(raw_decision)
        if set(decision) != {
            "archetype_id",
            "status",
            "target_id",
            "company_name",
            "profile_id",
            "large_sector_id",
            "periodic_report_document_id",
            "exact_quote",
            "mechanism_rationale",
            "confidence",
        }:
            raise ValueError("compatibility decision keys are not exact")
        status = str(decision.get("status") or "")
        if status not in {"SELECTED", "ABSTAIN", "PENDING"}:
            raise ValueError("compatibility decision status is invalid")
        confidence = decision.get("confidence")
        if (
            isinstance(confidence, bool)
            or not isinstance(confidence, (int, float))
            or not 0.0 <= float(confidence) <= 1.0
        ):
            raise ValueError("compatibility confidence must be within zero and one")
        if status != "SELECTED":
            if any(
                str(decision.get(key) or "")
                for key in (
                    "target_id",
                    "company_name",
                    "profile_id",
                    "large_sector_id",
                    "periodic_report_document_id",
                    "exact_quote",
                )
            ) or not str(decision.get("mechanism_rationale") or "").strip() or float(confidence) != 0.0:
                raise ValueError("abstain/pending decision must be empty and explained")
            validated_decisions.append(decision)
            continue
        profile = profile_by_id.get(str(decision.get("profile_id") or ""))
        expected_sector = large_sector_for_archetype(expected_archetype)
        quote = str(decision.get("exact_quote") or "")
        target = str(decision.get("target_id") or "")
        prompt_document = text_overrides.get(
            str(decision.get("profile_id") or ""),
            str(profile.get("_full_document") or "") if profile is not None else "",
        )
        if (
            profile is None
            or target in selected_targets
            or target != str(profile["target_id"])
            or str(decision.get("company_name") or "") != str(profile["company_name"])
            or str(decision.get("large_sector_id") or "") != expected_sector
            or str(profile["large_sector_id"]) != expected_sector
            or str(decision.get("periodic_report_document_id") or "")
            != str(profile["periodic_report_document_id"])
            or len(quote.strip()) < 12
            or quote not in str(profile["_full_document"])
            or quote not in prompt_document
            or not str(decision.get("mechanism_rationale") or "").strip()
        ):
            raise ValueError("selected compatibility lacks unique taxonomy/quote lineage")
        selected_targets.add(target)
        selection_core = {
            "archetype_id": expected_archetype,
            "large_sector_id": expected_sector,
            "target_id": target,
            "company_name": profile["company_name"],
            "profile_id": profile["profile_id"],
            "periodic_report_document_id": profile["periodic_report_document_id"],
            "periodic_report_full_text_hash": profile["source_hashes"][
                "document_full_text_hash"
            ],
            "exact_quote": quote,
            "exact_quote_hash": _sha256_text(quote),
            "mechanism_rationale": decision["mechanism_rationale"],
            "confidence": float(confidence),
            "selection_mode": "FORCED_VALIDATION_CANARY",
            "production_daily_candidate": False,
            "forced_validation_authority": False,
            "score_or_stage_authority": False,
            "gold_authority": False,
            "_profile": profile,
        }
        selected.append(selection_core)
        validated_decisions.append(decision)
    request_envelope = {
        "as_of_date": as_of_date,
        "required_archetypes": list(requested_archetypes),
        "profiles": [
            {
                "profile_id": row["profile_id"],
                "target_id": row["target_id"],
                "company_name": row["company_name"],
                "large_sector_id": row["large_sector_id"],
                "periodic_report_document_id": row["periodic_report_document_id"],
                "periodic_report_full_text_hash": row["source_hashes"][
                    "document_full_text_hash"
                ],
            }
            for row in profiles
        ],
    }
    receipt_core = {
        "schema_version": COMPATIBILITY_RECEIPT_SCHEMA_VERSION,
        "status": (
            "PENDING"
            if any(row["status"] == "PENDING" for row in validated_decisions)
            else "ABSTAINED"
            if any(row["status"] == "ABSTAIN" for row in validated_decisions)
            else "COMPLETE"
        ),
        "as_of_date": as_of_date,
        "provider_name": provider.provider_name,
        "provider_real": bool(provider.real_provider),
        "provider_fake": bool(provider.fake_provider),
        "request_id": request_id,
        "request_envelope": request_envelope,
        "request_envelope_hash": stable_hash(request_envelope),
        "request_input_hash": stable_hash(prompt_payload),
        "prompt_hash": prompt_hash,
        "raw_response": raw_response,
        "response_hash": response_hash,
        "decisions": validated_decisions,
        "classification_complete": True,
        "forced_validation_authority": False,
        "score_or_stage_authority": False,
        "gold_authority": False,
    }
    receipt = {
        **receipt_core,
        "response_id": "PROFILECLASSRESP-" + stable_hash(receipt_core)[:24],
    }
    enriched: list[Mapping[str, Any]] = []
    for selection in selected:
        profile = selection["_profile"]
        selection_core = {
            "schema_version": PROFILE_SELECTION_RECEIPT_SCHEMA_VERSION,
            "status": "COMPLETE",
            "target_id": selection["target_id"],
            "company_name": selection["company_name"],
            "as_of_date": as_of_date,
            "krx_row": profile["krx_row"],
            "krx_row_hash": profile["krx_row_hash"],
            "krx_request_id": profile["krx_request_id"],
            "krx_content_hash": profile["krx_content_hash"],
            "corp_code": profile["corp_code"],
            "corp_code_request_id": profile["corp_code_request_id"],
            "corp_code_roster_hash": profile["corp_code_roster_hash"],
            "company_profile_request_id": profile["company_profile_request_id"],
            "company_profile_hash": profile["company_profile_hash"],
            "periodic_report_request_id": profile["periodic_report_request_id"],
            "periodic_report_document_id": profile["periodic_report_document_id"],
            "periodic_report_rcept_no": profile["periodic_report_rcept_no"],
            "periodic_report_available_date": profile["periodic_report_available_date"],
            "periodic_report_full_text_hash": selection[
                "periodic_report_full_text_hash"
            ],
            "exact_quote": selection["exact_quote"],
            "exact_quote_hash": selection["exact_quote_hash"],
            "large_sector_id": selection["large_sector_id"],
            "archetype_id": selection["archetype_id"],
            "confidence": selection["confidence"],
            "mechanism_rationale": selection["mechanism_rationale"],
            "profile_id": selection["profile_id"],
            "compatibility_request_id": receipt["request_id"],
            "compatibility_response_id": receipt["response_id"],
            "compatibility_response_envelope_hash": receipt["response_hash"],
            "selection_mode": selection["selection_mode"],
            "production_daily_candidate": False,
            "forced_validation_authority": False,
            "score_or_stage_authority": False,
            "gold_authority": False,
        }
        enriched.append(
            {
                **selection_core,
                "selection_id": "PROFILESEL-" + stable_hash(selection_core)[:24],
            }
        )
    return tuple(enriched), receipt


def _validated_requested_archetypes(values: Sequence[str]) -> tuple[str, ...]:
    requested = tuple(str(value) for value in values)
    requested_set = set(requested)
    if (
        not requested
        or len(requested_set) != len(requested)
        or tuple(
            archetype for archetype in REQUIRED_ARCHETYPES if archetype in requested_set
        )
        != requested
    ):
        raise ValueError("compatibility requested archetype roster is invalid")
    return requested


def _compatibility_prompt_payload(
    *,
    as_of_date: str,
    profiles: Sequence[Mapping[str, Any]],
    required_archetypes: Sequence[str],
    prompt_text_by_profile_id: Mapping[str, str] | None = None,
) -> Mapping[str, Any]:
    requested = _validated_requested_archetypes(required_archetypes)
    text_overrides = dict(prompt_text_by_profile_id or {})
    return {
        "as_of_date": as_of_date,
        "required_archetypes": list(requested),
        "profiles": [
            {
                **{key: value for key, value in row.items() if key != "_full_document"},
                "periodic_report_full_text": text_overrides.get(
                    str(row["profile_id"]), str(row["_full_document"])
                ),
            }
            for row in profiles
        ],
        "instructions": (
            "Classify the requested archetype roster exactly. Select only a "
            "mechanism-compatible profile using a literal full-report quote; otherwise "
            "ABSTAIN or PENDING. Do not output a score, Stage, Gold, or recommendation."
        ),
    }


def _bounded_profile_fragments(
    *,
    as_of_date: str,
    profile: Mapping[str, Any],
    archetype: str,
    max_prompt_chars: int,
) -> tuple[str, ...]:
    """Split one full report without dropping any byte-range from review.

    A deterministic overlap keeps quotations near a raw chunk boundary visible
    in at least one prompt.  The final selector still validates every quote
    against the complete OpenDART document and its original hash.
    """

    text = str(profile.get("_full_document") or "")
    if not text:
        raise ValueError("compatibility profile full document is empty")
    fragments: list[str] = []
    start = 0
    while start < len(text):
        remaining = len(text) - start
        low = 0
        high = min(remaining, max_prompt_chars)
        while low < high:
            middle = (low + high + 1) // 2
            fragment = text[start : start + middle]
            payload = _compatibility_prompt_payload(
                as_of_date=as_of_date,
                profiles=(profile,),
                required_archetypes=(archetype,),
                prompt_text_by_profile_id={str(profile["profile_id"]): fragment},
            )
            encoded = json.dumps(payload, ensure_ascii=False, sort_keys=True)
            if len(encoded) <= max_prompt_chars:
                low = middle
            else:
                high = middle - 1
        if low <= 0:
            raise ValueError("compatibility prompt metadata alone exceeds bounded size")
        end = start + low
        if end < len(text):
            search_floor = start + max(1, low * 9 // 10)
            newline = text.rfind("\n", search_floor, end)
            if newline > start:
                end = newline + 1
        fragments.append(text[start:end])
        if end >= len(text):
            break
        overlap = min(4096, max(0, (end - start) // 8))
        next_start = end - overlap
        if next_start <= start:
            next_start = end
        start = next_start
    return tuple(fragments)


def _classify_profiles_bounded(
    *,
    as_of_date: str,
    profiles: Sequence[Mapping[str, Any]],
    provider: IssuerBusinessCompatibilityProvider,
    test_mode: bool,
    max_prompt_chars: int,
    max_calls: int,
    call_counter: list[int],
) -> tuple[tuple[Mapping[str, Any], ...], tuple[Mapping[str, Any], ...]]:
    full_payload = _compatibility_prompt_payload(
        as_of_date=as_of_date,
        profiles=profiles,
        required_archetypes=REQUIRED_ARCHETYPES,
    )
    full_prompt = json.dumps(full_payload, ensure_ascii=False, sort_keys=True)
    if len(full_prompt) <= max_prompt_chars:
        selected, receipt = _classify_profiles(
            as_of_date=as_of_date,
            profiles=profiles,
            provider=provider,
            test_mode=test_mode,
            max_prompt_chars=max_prompt_chars,
            max_calls=max_calls,
            call_counter=call_counter,
        )
        return selected, (receipt,)

    selected: list[Mapping[str, Any]] = []
    receipts: list[Mapping[str, Any]] = []
    selected_targets: set[str] = set()
    for archetype in REQUIRED_ARCHETYPES:
        expected_sector = large_sector_for_archetype(archetype)
        matched = False
        candidates = tuple(
            profile
            for profile in profiles
            if str(profile.get("large_sector_id") or "") == expected_sector
            and str(profile.get("target_id") or "") not in selected_targets
        )
        for profile in candidates:
            for fragment in _bounded_profile_fragments(
                as_of_date=as_of_date,
                profile=profile,
                archetype=archetype,
                max_prompt_chars=max_prompt_chars,
            ):
                partial, receipt = _classify_profiles(
                    as_of_date=as_of_date,
                    profiles=(profile,),
                    provider=provider,
                    test_mode=test_mode,
                    max_prompt_chars=max_prompt_chars,
                    required_archetypes=(archetype,),
                    prompt_text_by_profile_id={str(profile["profile_id"]): fragment},
                    max_calls=max_calls,
                    call_counter=call_counter,
                )
                receipts.append(receipt)
                if any(
                    str(row.get("status") or "") == "PENDING"
                    for row in receipt["decisions"]
                ):
                    return (), tuple(receipts)
                if partial:
                    selection = partial[0]
                    target = str(selection["target_id"])
                    if target in selected_targets:
                        raise ValueError("bounded compatibility selected a duplicate target")
                    selected.append(selection)
                    selected_targets.add(target)
                    matched = True
                    break
            if matched:
                break
        if not matched:
            return (), tuple(receipts)
    if tuple(row["archetype_id"] for row in selected) != REQUIRED_ARCHETYPES:
        raise ValueError("bounded compatibility selection roster is not exact")
    return tuple(selected), tuple(receipts)


def _compatibility_schema(
    required_archetypes: Sequence[str] = REQUIRED_ARCHETYPES,
) -> Mapping[str, Any]:
    requested = _validated_requested_archetypes(required_archetypes)
    return {
        "type": "object",
        "additionalProperties": False,
        "required": ["decisions", "classification_complete", "unresolved_notes"],
        "properties": {
            "decisions": {
                "type": "array",
                "minItems": len(requested),
                "maxItems": len(requested),
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": [
                        "archetype_id",
                        "status",
                        "target_id",
                        "company_name",
                        "profile_id",
                        "large_sector_id",
                        "periodic_report_document_id",
                        "exact_quote",
                        "mechanism_rationale",
                        "confidence",
                    ],
                    "properties": {
                        "archetype_id": {"type": "string", "enum": list(requested)},
                        "status": {"type": "string", "enum": ["SELECTED", "ABSTAIN", "PENDING"]},
                        "target_id": {"type": "string"},
                        "company_name": {"type": "string"},
                        "profile_id": {"type": "string"},
                        "large_sector_id": {"type": "string"},
                        "periodic_report_document_id": {"type": "string"},
                        "exact_quote": {"type": "string"},
                        "mechanism_rationale": {"type": "string", "minLength": 1},
                        "confidence": {"type": "number", "minimum": 0, "maximum": 1},
                    },
                },
            },
            "classification_complete": {"type": "boolean"},
            "unresolved_notes": {"type": "array", "items": {"type": "string"}},
        },
    }


def validate_issuer_business_profile_receipt(
    raw: Mapping[str, Any],
    *,
    profile: Mapping[str, Any],
    compatibility_receipt: Mapping[str, Any],
    full_document_text: str | None = None,
) -> Mapping[str, Any]:
    """Fail closed on one selected-target receipt.

    Supplying ``full_document_text`` additionally rechecks the literal quote
    and the complete document hash.  The materializer always performs that
    stronger check before constructing this compact receipt.
    """

    receipt = dict(raw)
    expected_keys = {
        "schema_version",
        "status",
        "target_id",
        "company_name",
        "as_of_date",
        "krx_row",
        "krx_row_hash",
        "krx_request_id",
        "krx_content_hash",
        "corp_code",
        "corp_code_request_id",
        "corp_code_roster_hash",
        "company_profile_request_id",
        "company_profile_hash",
        "periodic_report_request_id",
        "periodic_report_document_id",
        "periodic_report_rcept_no",
        "periodic_report_available_date",
        "periodic_report_full_text_hash",
        "exact_quote",
        "exact_quote_hash",
        "large_sector_id",
        "archetype_id",
        "confidence",
        "mechanism_rationale",
        "profile_id",
        "compatibility_request_id",
        "compatibility_response_id",
        "compatibility_response_envelope_hash",
        "selection_mode",
        "production_daily_candidate",
        "forced_validation_authority",
        "score_or_stage_authority",
        "gold_authority",
        "selection_id",
    }
    if set(receipt) != expected_keys:
        raise ValueError("profile selection receipt keys are not exact")
    if (
        receipt.get("schema_version") != PROFILE_SELECTION_RECEIPT_SCHEMA_VERSION
        or receipt.get("status") != "COMPLETE"
        or receipt.get("selection_mode") != "FORCED_VALIDATION_CANARY"
        or receipt.get("production_daily_candidate") is not False
        or any(
            receipt.get(key) is not False
            for key in (
                "forced_validation_authority",
                "score_or_stage_authority",
                "gold_authority",
            )
        )
    ):
        raise ValueError("profile selection receipt status/authority is invalid")
    normalized_profile = _validate_public_profile(profile)
    exact_quote = str(receipt.get("exact_quote") or "")
    confidence = receipt.get("confidence")
    expected_sector = large_sector_for_archetype(receipt.get("archetype_id"))
    if (
        len(exact_quote.strip()) < 12
        or receipt.get("exact_quote_hash") != _sha256_text(exact_quote)
        or isinstance(confidence, bool)
        or not isinstance(confidence, (int, float))
        or not 0.0 <= float(confidence) <= 1.0
        or receipt.get("large_sector_id") != expected_sector
        or normalized_profile.get("large_sector_id") != expected_sector
    ):
        raise ValueError("profile selection quote/confidence/taxonomy is invalid")
    profile_links = {
        "target_id": "target_id",
        "company_name": "company_name",
        "as_of_date": "as_of_date",
        "krx_row": "krx_row",
        "krx_row_hash": "krx_row_hash",
        "krx_request_id": "krx_request_id",
        "krx_content_hash": "krx_content_hash",
        "corp_code": "corp_code",
        "corp_code_request_id": "corp_code_request_id",
        "corp_code_roster_hash": "corp_code_roster_hash",
        "company_profile_request_id": "company_profile_request_id",
        "company_profile_hash": "company_profile_hash",
        "periodic_report_request_id": "periodic_report_request_id",
        "periodic_report_document_id": "periodic_report_document_id",
        "periodic_report_rcept_no": "periodic_report_rcept_no",
        "periodic_report_available_date": "periodic_report_available_date",
        "periodic_report_full_text_hash": "document_full_text_hash",
        "profile_id": "profile_id",
    }
    for receipt_key, profile_key in profile_links.items():
        expected = (
            normalized_profile["source_hashes"][profile_key]
            if profile_key == "document_full_text_hash"
            else normalized_profile[profile_key]
        )
        if receipt[receipt_key] != expected:
            raise ValueError(f"profile selection orphan/tamper: {receipt_key}")
    validated_compatibility = _validate_compatibility_receipt(compatibility_receipt)
    if (
        receipt["compatibility_request_id"] != validated_compatibility["request_id"]
        or receipt["compatibility_response_id"]
        != validated_compatibility["response_id"]
        or receipt["compatibility_response_envelope_hash"]
        != validated_compatibility["response_hash"]
    ):
        raise ValueError("profile selection compatibility envelope is orphaned")
    decisions = [
        row
        for row in validated_compatibility["decisions"]
        if row["archetype_id"] == receipt["archetype_id"]
    ]
    if len(decisions) != 1:
        raise ValueError("profile selection decision lineage is not unique")
    decision = decisions[0]
    if (
        decision["status"] != "SELECTED"
        or decision["target_id"] != receipt["target_id"]
        or decision["company_name"] != receipt["company_name"]
        or decision["profile_id"] != receipt["profile_id"]
        or decision["large_sector_id"] != receipt["large_sector_id"]
        or decision["periodic_report_document_id"]
        != receipt["periodic_report_document_id"]
        or decision["exact_quote"] != exact_quote
        or float(decision["confidence"]) != float(confidence)
        or decision["mechanism_rationale"] != receipt["mechanism_rationale"]
    ):
        raise ValueError("profile selection differs from provider response envelope")
    if full_document_text is not None and (
        _sha256_text(full_document_text) != receipt["periodic_report_full_text_hash"]
        or exact_quote not in full_document_text
    ):
        raise ValueError("profile selection quote is not literal in the full document")
    selection_core = {key: value for key, value in receipt.items() if key != "selection_id"}
    if receipt["selection_id"] != "PROFILESEL-" + stable_hash(selection_core)[:24]:
        raise ValueError("profile selection id hash mismatch")
    return receipt


def _validate_industry_discovery_record(raw: object) -> Mapping[str, Any]:
    if not isinstance(raw, Mapping):
        raise ValueError("industry discovery record is not an object")
    row = dict(raw)
    if set(row) != {
        "schema_version",
        "status",
        "target_id",
        "company_name",
        "as_of_date",
        "krx_row",
        "krx_row_hash",
        "corp_code",
        "corp_code_request_id",
        "corp_code_response_hash",
        "company_profile_request_id",
        "company_profile_hash",
        "industry_code",
        "large_sector_id",
        "official_only",
        "forced_validation_authority",
        "score_or_stage_authority",
        "gold_authority",
        "discovery_id",
    }:
        raise ValueError("industry discovery record keys are not exact")
    if (
        row["schema_version"] != INDUSTRY_DISCOVERY_SCHEMA_VERSION
        or row["status"] != "COMPLETE"
        or row["official_only"] is not True
        or any(
            row[key] is not False
            for key in (
                "forced_validation_authority",
                "score_or_stage_authority",
                "gold_authority",
            )
        )
    ):
        raise ValueError("industry discovery status/authority is invalid")
    candidate = _validate_krx_row(row["krx_row"], as_of_date=row["as_of_date"])
    industry_code = str(row["industry_code"])
    corp_code = str(row["corp_code"])
    if (
        row["target_id"] != candidate["symbol"]
        or row["company_name"] != candidate["company_name"]
        or row["krx_row_hash"] != stable_hash(dict(candidate))
        or re.fullmatch(r"[0-9]{8}", corp_code) is None
        or re.fullmatch(r"[0-9]{2,6}", industry_code) is None
        or row["large_sector_id"]
        != (large_sector_for_industry_code(industry_code) or "")
        or row["corp_code_request_id"]
        != _official_request_id(
            role="CORP_CODE_IDENTITY",
            target_id=row["target_id"],
            as_of_date=row["as_of_date"],
            request_params={},
        )
        or row["company_profile_request_id"]
        != _official_request_id(
            role="COMPANY_IDENTITY",
            target_id=row["target_id"],
            as_of_date=row["as_of_date"],
            request_params={"corp_code": corp_code},
        )
        or any(
            _HEX64_RE.fullmatch(str(row[key])) is None
            for key in ("corp_code_response_hash", "company_profile_hash")
        )
    ):
        raise ValueError("industry discovery identity/hash/taxonomy is invalid")
    core = {key: value for key, value in row.items() if key != "discovery_id"}
    if row["discovery_id"] != "PROFILEDISC-" + stable_hash(core)[:24]:
        raise ValueError("industry discovery id hash mismatch")
    return row


def validate_candidate_expansion_receipt(raw: object) -> Mapping[str, Any]:
    if not isinstance(raw, Mapping):
        raise ValueError("candidate expansion receipt is not an object")
    receipt = dict(raw)
    if set(receipt) != {
        "schema_version",
        "status",
        "selection_mode",
        "as_of_date",
        "provider_name",
        "required_archetypes",
        "required_sector_quotas",
        "natural_candidate_roster",
        "natural_candidate_roster_hash",
        "full_krx_candidate_count",
        "discovery_pool_count",
        "discovery_fetch_count",
        "max_discovery_fetches",
        "max_forced_candidates_per_required_slot",
        "expanded_candidates",
        "expanded_candidate_roster_hash",
        "unfilled_sector_quotas",
        "pending",
        "diagnostics",
        "stop_reason",
        "official_only",
        "bounded",
        "forced_validation_authority",
        "score_or_stage_authority",
        "gold_authority",
        "receipt_id",
    }:
        raise ValueError("candidate expansion receipt keys are not exact")
    status = receipt["status"]
    max_discovery = receipt["max_discovery_fetches"]
    per_slot = receipt["max_forced_candidates_per_required_slot"]
    count_fields = (
        receipt["full_krx_candidate_count"],
        receipt["discovery_pool_count"],
        receipt["discovery_fetch_count"],
    )
    if (
        receipt["schema_version"] != CANDIDATE_EXPANSION_RECEIPT_SCHEMA_VERSION
        or status not in {"NOT_REQUESTED", "COMPLETE", "PENDING"}
        or receipt["selection_mode"] != "FORCED_VALIDATION_CANARY"
        or receipt["provider_name"] != "OpenDART"
        or tuple(receipt["required_archetypes"] or ()) != REQUIRED_ARCHETYPES
        or receipt["official_only"] is not True
        or receipt["bounded"] is not True
        or any(
            receipt[key] is not False
            for key in (
                "forced_validation_authority",
                "score_or_stage_authority",
                "gold_authority",
            )
        )
        or any(
            isinstance(value, bool) or not isinstance(value, int) or value < 0
            for value in count_fields
        )
        or isinstance(max_discovery, bool)
        or not isinstance(max_discovery, int)
        or not 1 <= max_discovery <= 5_000
        or isinstance(per_slot, bool)
        or not isinstance(per_slot, int)
        or not 1 <= per_slot <= 10
        or receipt["discovery_fetch_count"] > max_discovery
        or receipt["discovery_fetch_count"] > receipt["discovery_pool_count"]
    ):
        raise ValueError("candidate expansion scope/budget/authority is invalid")
    date.fromisoformat(str(receipt["as_of_date"]))
    natural = receipt["natural_candidate_roster"]
    if (
        isinstance(natural, (str, bytes))
        or not isinstance(natural, Sequence)
        or any(_TARGET_RE.fullmatch(str(target)) is None for target in natural)
        or len(set(natural)) != len(natural)
        or receipt["natural_candidate_roster_hash"] != stable_hash(list(natural))
        or receipt["full_krx_candidate_count"]
        != receipt["discovery_pool_count"] + len(natural)
    ):
        raise ValueError("candidate expansion natural/full KRX roster is invalid")
    expected_quotas = list(_required_sector_quotas(per_slot))
    if receipt["required_sector_quotas"] != expected_quotas:
        raise ValueError("candidate expansion sector quotas are not taxonomy-derived")
    expanded_raw = receipt["expanded_candidates"]
    pending = receipt["pending"]
    diagnostics = receipt["diagnostics"]
    unfilled = receipt["unfilled_sector_quotas"]
    if any(
        isinstance(value, (str, bytes)) or not isinstance(value, Sequence)
        for value in (expanded_raw, pending, diagnostics, unfilled)
    ) or any(
        not isinstance(row, Mapping) for row in (*pending, *diagnostics)
    ):
        raise ValueError("candidate expansion collections are invalid")
    expanded = [_validate_industry_discovery_record(row) for row in expanded_raw]
    expanded_targets = [str(row["target_id"]) for row in expanded]
    quota_by_sector = {
        str(row["large_sector_id"]): int(row["candidate_quota"])
        for row in expected_quotas
    }
    if (
        any(row["as_of_date"] != receipt["as_of_date"] for row in expanded)
        or len(set(expanded_targets)) != len(expanded_targets)
        or set(expanded_targets).intersection(str(target) for target in natural)
        or any(row["large_sector_id"] not in quota_by_sector for row in expanded)
        or any(
            sum(1 for row in expanded if row["large_sector_id"] == sector) > quota
            for sector, quota in quota_by_sector.items()
        )
        or len(expanded) > receipt["discovery_fetch_count"]
        or receipt["expanded_candidate_roster_hash"]
        != stable_hash([row["discovery_id"] for row in expanded])
    ):
        raise ValueError("candidate expansion discovered roster is invalid")
    expected_unfilled = [
        {
            "large_sector_id": sector,
            "missing_candidate_count": quota
            - sum(1 for row in expanded if row["large_sector_id"] == sector),
        }
        for sector, quota in quota_by_sector.items()
        if sum(1 for row in expanded if row["large_sector_id"] == sector) < quota
    ]
    if list(unfilled) != expected_unfilled:
        raise ValueError("candidate expansion unfilled sector quota audit is invalid")
    diagnostic_targets = []
    for diagnostic in diagnostics:
        if set(diagnostic) != {"code", "target_id", "detail"} or (
            diagnostic.get("code")
            != "FORCED_DISCOVERY_CANDIDATE_INELIGIBLE"
            or _TARGET_RE.fullmatch(str(diagnostic.get("target_id") or "")) is None
            or diagnostic.get("detail")
            not in _DISCOVERY_CANDIDATE_INELIGIBLE_DETAILS
        ):
            raise ValueError("candidate expansion diagnostic is invalid")
        diagnostic_targets.append(str(diagnostic["target_id"]))
    if (
        len(set(diagnostic_targets)) != len(diagnostic_targets)
        or set(diagnostic_targets).intersection(expanded_targets)
        or len(diagnostics) + len(expanded) > receipt["discovery_fetch_count"]
    ):
        raise ValueError("candidate expansion diagnostic roster is invalid")
    stop_reason = receipt["stop_reason"]
    if status == "NOT_REQUESTED" and (
        any(count_fields)
        or expanded
        or pending
        or diagnostics
        or stop_reason != "NOT_REQUESTED"
    ):
        raise ValueError("not-requested candidate expansion carries live authority")
    if status == "COMPLETE" and (
        pending
        or stop_reason not in {"QUOTAS_FILLED", "FULL_KRX_EXHAUSTED"}
        or (stop_reason == "QUOTAS_FILLED" and unfilled)
        or (
            stop_reason == "FULL_KRX_EXHAUSTED"
            and receipt["discovery_fetch_count"] != receipt["discovery_pool_count"]
        )
    ):
        raise ValueError("complete candidate expansion stop state is invalid")
    if status == "PENDING" and (
        not pending
        or stop_reason
        not in {"CREDENTIAL_PENDING", "PROVIDER_PENDING", "BUDGET_EXHAUSTED"}
    ):
        raise ValueError("pending candidate expansion lacks a bounded failure")
    core = {key: value for key, value in receipt.items() if key != "receipt_id"}
    if receipt["receipt_id"] != "PROFILEEXPAND-" + stable_hash(core)[:24]:
        raise ValueError("candidate expansion receipt id hash mismatch")
    return receipt


def validate_issuer_business_profile_result(
    raw: Mapping[str, Any],
    *,
    full_documents_by_id: Mapping[str, str] | None = None,
) -> Mapping[str, Any]:
    """Validate the exact-five manifest used by the selector integration."""

    result = dict(raw)
    if set(result) != {
        "schema_version",
        "status",
        "as_of_date",
        "required_archetypes",
        "profiles",
        "selections",
        "compatibility_receipts",
        "candidate_expansion_receipt",
        "pending",
        "audit",
        "forced_validation_authority",
        "score_or_stage_authority",
        "gold_authority",
    }:
        raise ValueError("issuer business profile result keys are not exact")
    if (
        result.get("schema_version") != PROFILE_RESULT_SCHEMA_VERSION
        or result.get("status")
        not in {PROFILE_PASS, PROFILE_PENDING, PROFILE_ABSTAINED, PROFILE_TEST_ONLY}
        or tuple(result.get("required_archetypes") or ()) != REQUIRED_ARCHETYPES
        or any(
            result.get(key) is not False
            for key in (
                "forced_validation_authority",
                "score_or_stage_authority",
                "gold_authority",
            )
        )
    ):
        raise ValueError("issuer business profile result status/authority is invalid")
    date.fromisoformat(str(result.get("as_of_date") or ""))
    profiles_raw = result.get("profiles")
    selections_raw = result.get("selections")
    compatibility_raw = result.get("compatibility_receipts")
    if any(
        isinstance(value, (str, bytes)) or not isinstance(value, Sequence)
        for value in (profiles_raw, selections_raw, compatibility_raw, result.get("pending"))
    ) or not isinstance(result.get("audit"), Mapping):
        raise ValueError("issuer business profile result collections are invalid")
    profiles = [_validate_public_profile(row) for row in profiles_raw]
    if any(row["as_of_date"] != result["as_of_date"] for row in profiles):
        raise ValueError("issuer profile belongs to a different as-of scope")
    if len({row["profile_id"] for row in profiles}) != len(profiles):
        raise ValueError("issuer profile ids are not unique")
    profile_by_id = {row["profile_id"]: row for row in profiles}
    compatibility = [_validate_compatibility_receipt(row) for row in compatibility_raw]
    expansion = validate_candidate_expansion_receipt(
        result.get("candidate_expansion_receipt")
    )
    if expansion["as_of_date"] != result["as_of_date"]:
        raise ValueError("candidate expansion belongs to a different as-of scope")
    if expansion["status"] != "NOT_REQUESTED":
        candidate_targets = {
            str(target) for target in expansion["natural_candidate_roster"]
        }
        candidate_targets.update(
            str(row["target_id"]) for row in expansion["expanded_candidates"]
        )
        if any(str(profile["target_id"]) not in candidate_targets for profile in profiles):
            raise ValueError("issuer profile escaped natural/forced candidate lineage")
        expanded_by_target = {
            str(row["target_id"]): row for row in expansion["expanded_candidates"]
        }
        for profile in profiles:
            discovered = expanded_by_target.get(str(profile["target_id"]))
            if discovered is not None and any(
                profile[key] != discovered[key]
                for key in (
                    "company_name",
                    "krx_row_hash",
                    "corp_code",
                    "corp_code_request_id",
                    "company_profile_request_id",
                    "company_profile_hash",
                    "industry_code",
                    "large_sector_id",
                )
            ):
                raise ValueError("full issuer profile drifted from forced discovery")
    if len({row["response_id"] for row in compatibility}) != len(compatibility):
        raise ValueError("compatibility response ids are not unique")
    compatibility_by_id = {row["response_id"]: row for row in compatibility}
    if result["status"] != PROFILE_TEST_ONLY and any(
        row["provider_name"] != CANONICAL_COMPATIBILITY_PROVIDER
        or row["provider_real"] is not True
        or row["provider_fake"] is not False
        for row in compatibility
    ):
        raise ValueError("production compatibility receipt is not Codex Collaboration")
    for receipt in compatibility:
        envelope_profiles = receipt["request_envelope"]["profiles"]
        for envelope_profile in envelope_profiles:
            profile = profile_by_id.get(envelope_profile["profile_id"])
            if profile is None or envelope_profile != {
                "profile_id": profile["profile_id"],
                "target_id": profile["target_id"],
                "company_name": profile["company_name"],
                "large_sector_id": profile["large_sector_id"],
                "periodic_report_document_id": profile["periodic_report_document_id"],
                "periodic_report_full_text_hash": profile["source_hashes"][
                    "document_full_text_hash"
                ],
            }:
                raise ValueError("compatibility request envelope has an orphan profile")
    selections: list[Mapping[str, Any]] = []
    for selection in selections_raw:
        if not isinstance(selection, Mapping):
            raise ValueError("profile selection receipt is not an object")
        profile = profile_by_id.get(str(selection.get("profile_id") or ""))
        compatibility_receipt = compatibility_by_id.get(
            str(selection.get("compatibility_response_id") or "")
        )
        if profile is None or compatibility_receipt is None:
            raise ValueError("profile selection receipt is orphaned")
        document_id = str(selection.get("periodic_report_document_id") or "")
        full_text = (
            full_documents_by_id.get(document_id)
            if full_documents_by_id is not None
            else None
        )
        if full_documents_by_id is not None and full_text is None:
            raise ValueError("selected profile full document is missing")
        selections.append(
            validate_issuer_business_profile_receipt(
                selection,
                profile=profile,
                compatibility_receipt=compatibility_receipt,
                full_document_text=full_text,
            )
        )
    archetypes = tuple(row["archetype_id"] for row in selections)
    targets = {row["target_id"] for row in selections}
    audit = dict(result["audit"])
    if set(audit) != {
        "required_archetype_count",
        "selected_archetype_count",
        "unique_selected_target_count",
        "profile_fetch_count",
        "max_profile_fetches",
        "max_compatibility_prompt_chars",
        "profile_count",
        "compatibility_receipt_count",
        "provider_status",
        "stopped_on_five",
        "official_only",
        "production_acceptance_pass",
        "diagnostic_count",
        "forced_validation_authority",
        "score_or_stage_authority",
        "gold_authority",
    }:
        raise ValueError("issuer business profile audit keys are not exact")
    expected_audit = {
        "required_archetype_count": len(REQUIRED_ARCHETYPES),
        "selected_archetype_count": len(selections),
        "unique_selected_target_count": len(targets),
        "profile_count": len(profiles),
        "compatibility_receipt_count": len(compatibility),
        "diagnostic_count": len(result["pending"]),
        "production_acceptance_pass": result["status"] == PROFILE_PASS,
        "forced_validation_authority": False,
        "score_or_stage_authority": False,
        "gold_authority": False,
    }
    if any(audit.get(key) != value for key, value in expected_audit.items()):
        raise ValueError("issuer business profile audit counts/authority mismatch")
    if (
        isinstance(audit.get("profile_fetch_count"), bool)
        or not isinstance(audit.get("profile_fetch_count"), int)
        or isinstance(audit.get("max_profile_fetches"), bool)
        or not isinstance(audit.get("max_profile_fetches"), int)
        or isinstance(audit.get("max_compatibility_prompt_chars"), bool)
        or not isinstance(audit.get("max_compatibility_prompt_chars"), int)
        or not 0 <= audit["profile_fetch_count"] <= audit["max_profile_fetches"]
        or not 10_000 <= audit["max_compatibility_prompt_chars"] <= 5_000_000
        or len(profiles) > audit["profile_fetch_count"]
        or audit.get("official_only") is not True
        or audit.get("provider_status") not in {"NOT_CALLED", "COMPLETED", "PENDING"}
        or any(not isinstance(row, Mapping) for row in result["pending"])
    ):
        raise ValueError("issuer business profile audit budget/provider state is invalid")
    if result["status"] == PROFILE_PASS and (
        archetypes != REQUIRED_ARCHETYPES
        or len(targets) != len(REQUIRED_ARCHETYPES)
        or audit.get("stopped_on_five") is not True
        or any(
            compatibility_by_id[row["compatibility_response_id"]]["status"]
            != "COMPLETE"
            for row in selections
        )
        or sum(
            1
            for receipt in compatibility
            for decision in receipt["decisions"]
            if decision["status"] == "SELECTED"
        )
        != len(selections)
    ):
        raise ValueError("production COMPLETE requires the exact-five unique manifest")
    if result["status"] in {PROFILE_PENDING, PROFILE_ABSTAINED} and selections:
        raise ValueError("pending/abstained result may not masquerade as selected")
    if result["status"] == PROFILE_PASS and expansion["status"] == "PENDING":
        raise ValueError("pending forced candidate expansion may not become COMPLETE")
    if result["status"] == PROFILE_TEST_ONLY and audit.get("production_acceptance_pass"):
        raise ValueError("test mode may not become a production acceptance PASS")
    return result


def validate_forced_validation_profile_manifest(
    raw: Mapping[str, Any],
    *,
    full_documents_by_id: Mapping[str, str] | None = None,
) -> Mapping[str, Any]:
    """Named alias for the Phase-105 exact-five manifest contract."""

    return validate_issuer_business_profile_result(
        raw,
        full_documents_by_id=full_documents_by_id,
    )


def _validate_public_profile(raw: object) -> Mapping[str, Any]:
    if not isinstance(raw, Mapping):
        raise ValueError("issuer profile is not an object")
    profile = dict(raw)
    if set(profile) != {
        "schema_version",
        "status",
        "target_id",
        "company_name",
        "as_of_date",
        "krx_row",
        "krx_row_hash",
        "krx_effective_date",
        "krx_request_id",
        "krx_content_hash",
        "corp_code",
        "corp_code_request_id",
        "corp_code_roster_hash",
        "industry_code",
        "large_sector_id",
        "company_profile_request_id",
        "company_profile_hash",
        "periodic_list_request_ids",
        "periodic_report_request_id",
        "periodic_report_document_id",
        "periodic_report_rcept_no",
        "periodic_report_available_date",
        "source_hashes",
        "forced_validation_authority",
        "score_or_stage_authority",
        "gold_authority",
        "profile_id",
    }:
        raise ValueError("issuer profile keys are not exact")
    if (
        profile["schema_version"] != PROFILE_SCHEMA_VERSION
        or profile["status"] != "COMPLETE"
        or any(
            profile.get(key) is not False
            for key in (
                "forced_validation_authority",
                "score_or_stage_authority",
                "gold_authority",
            )
        )
    ):
        raise ValueError("issuer profile status/authority is invalid")
    krx_row = _validate_krx_row(profile["krx_row"], as_of_date=profile["as_of_date"])
    source_hashes = profile.get("source_hashes")
    hash_values = (
        profile.get("krx_content_hash"),
        profile.get("corp_code_roster_hash"),
        profile.get("company_profile_hash"),
        profile.get("krx_row_hash"),
    )
    if (
        not isinstance(source_hashes, Mapping)
        or set(source_hashes)
        != {
            "corp_code_response_hash",
            "company_response_hash",
            "periodic_list_roster_hash",
            "document_full_text_hash",
        }
        or any(_HEX64_RE.fullmatch(str(value or "")) is None for value in hash_values)
        or any(
            _HEX64_RE.fullmatch(str(value or "")) is None
            for value in source_hashes.values()
        )
        or profile["krx_row_hash"] != stable_hash(dict(krx_row))
        or profile["krx_request_id"] != krx_row["source_request_id"]
        or profile["krx_content_hash"] != krx_row["source_content_hash"]
        or profile["corp_code_roster_hash"]
        != source_hashes["corp_code_response_hash"]
        or profile["company_profile_hash"] != source_hashes["company_response_hash"]
        or profile["target_id"] != krx_row["symbol"]
        or profile["company_name"] != krx_row["company_name"]
        or profile["krx_effective_date"] != krx_row["source_effective_date"]
        or profile["large_sector_id"]
        != large_sector_for_industry_code(profile["industry_code"])
        or profile["periodic_report_document_id"]
        != "opendart:disclosure:" + str(profile["periodic_report_rcept_no"])
        or date.fromisoformat(profile["periodic_report_available_date"])
        > date.fromisoformat(profile["as_of_date"])
    ):
        raise ValueError("issuer profile lineage/hash/taxonomy is invalid")
    list_ids = profile.get("periodic_list_request_ids")
    if (
        isinstance(list_ids, (str, bytes))
        or not isinstance(list_ids, Sequence)
        or not list_ids
        or len(set(list_ids)) != len(list_ids)
    ):
        raise ValueError("issuer profile periodic-list request roster is invalid")
    profile_core = {key: value for key, value in profile.items() if key != "profile_id"}
    if profile["profile_id"] != "ISSUERPROFILE-" + stable_hash(profile_core)[:24]:
        raise ValueError("issuer profile id hash mismatch")
    return profile


def _validate_compatibility_receipt(raw: object) -> Mapping[str, Any]:
    if not isinstance(raw, Mapping):
        raise ValueError("compatibility receipt is not an object")
    receipt = dict(raw)
    if set(receipt) != {
        "schema_version",
        "status",
        "as_of_date",
        "provider_name",
        "provider_real",
        "provider_fake",
        "request_id",
        "request_envelope",
        "request_envelope_hash",
        "request_input_hash",
        "prompt_hash",
        "raw_response",
        "response_hash",
        "decisions",
        "classification_complete",
        "forced_validation_authority",
        "score_or_stage_authority",
        "gold_authority",
        "response_id",
    }:
        raise ValueError("compatibility receipt keys are not exact")
    raw_response = receipt.get("raw_response")
    request_envelope = receipt.get("request_envelope")
    if not isinstance(raw_response, str) or not isinstance(request_envelope, Mapping):
        raise ValueError("compatibility request/response envelope is invalid")
    requested_archetypes = _validated_requested_archetypes(
        tuple(request_envelope.get("required_archetypes") or ())
    )
    decoded = json.loads(raw_response)
    decisions = receipt.get("decisions")
    if (
        receipt["schema_version"] != COMPATIBILITY_RECEIPT_SCHEMA_VERSION
        or receipt["status"] not in {"COMPLETE", "ABSTAINED", "PENDING"}
        or receipt["classification_complete"] is not True
        or any(
            receipt.get(key) is not False
            for key in (
                "forced_validation_authority",
                "score_or_stage_authority",
                "gold_authority",
            )
        )
        or receipt["request_envelope_hash"] != stable_hash(dict(request_envelope))
        or _HEX64_RE.fullmatch(str(receipt.get("request_input_hash") or "")) is None
        or _HEX64_RE.fullmatch(str(receipt.get("prompt_hash") or "")) is None
        or receipt["response_hash"] != _sha256_text(raw_response)
        or not isinstance(decoded, Mapping)
        or set(decoded) != {"decisions", "classification_complete", "unresolved_notes"}
        or decoded.get("decisions") != receipt["decisions"]
        or decoded.get("classification_complete") is not True
        or not isinstance(decoded.get("unresolved_notes"), list)
        or not str(receipt.get("provider_name") or "")
        or not isinstance(receipt.get("provider_real"), bool)
        or not isinstance(receipt.get("provider_fake"), bool)
    ):
        raise ValueError("compatibility receipt envelope/hash/authority is invalid")
    if (
        not isinstance(decisions, list)
        or any(not isinstance(row, Mapping) for row in decisions)
        or tuple(row.get("archetype_id") for row in decisions)
        != requested_archetypes
    ):
        raise ValueError("compatibility decision roster is not exact")
    for decision in decisions:
        if not isinstance(decision, Mapping) or set(decision) != {
            "archetype_id",
            "status",
            "target_id",
            "company_name",
            "profile_id",
            "large_sector_id",
            "periodic_report_document_id",
            "exact_quote",
            "mechanism_rationale",
            "confidence",
        }:
            raise ValueError("compatibility decision keys are not exact")
        status = decision.get("status")
        confidence = decision.get("confidence")
        if (
            status not in {"SELECTED", "ABSTAIN", "PENDING"}
            or isinstance(confidence, bool)
            or not isinstance(confidence, (int, float))
            or not 0.0 <= float(confidence) <= 1.0
            or not str(decision.get("mechanism_rationale") or "").strip()
        ):
            raise ValueError("compatibility decision status/confidence is invalid")
        identity_values = [
            str(decision.get(key) or "")
            for key in (
                "target_id",
                "company_name",
                "profile_id",
                "large_sector_id",
                "periodic_report_document_id",
                "exact_quote",
            )
        ]
        if status == "SELECTED" and (
            any(not value for value in identity_values)
            or len(str(decision["exact_quote"]).strip()) < 12
        ):
            raise ValueError("selected compatibility decision lacks lineage")
        if status != "SELECTED" and (any(identity_values) or float(confidence) != 0.0):
            raise ValueError("abstained/pending compatibility decision invents lineage")
    request_profiles = request_envelope.get("profiles")
    if (
        set(request_envelope) != {"as_of_date", "required_archetypes", "profiles"}
        or request_envelope.get("as_of_date") != receipt.get("as_of_date")
        or tuple(request_envelope.get("required_archetypes") or ())
        != requested_archetypes
        or isinstance(request_profiles, (str, bytes))
        or not isinstance(request_profiles, Sequence)
        or not request_profiles
        or any(
            not isinstance(row, Mapping)
            or set(row)
            != {
                "profile_id",
                "target_id",
                "company_name",
                "large_sector_id",
                "periodic_report_document_id",
                "periodic_report_full_text_hash",
            }
            for row in request_profiles
        )
        or len({row.get("profile_id") for row in request_profiles})
        != len(request_profiles)
    ):
        raise ValueError("compatibility request envelope roster is invalid")
    envelope_by_profile_id = {
        str(row["profile_id"]): row for row in request_profiles
    }
    selected_targets: set[str] = set()
    for decision in decisions:
        if decision["status"] != "SELECTED":
            continue
        envelope_profile = envelope_by_profile_id.get(str(decision["profile_id"]))
        target = str(decision["target_id"])
        if (
            envelope_profile is None
            or target in selected_targets
            or decision["company_name"] != envelope_profile["company_name"]
            or target != envelope_profile["target_id"]
            or decision["large_sector_id"]
            != large_sector_for_archetype(decision["archetype_id"])
            or decision["large_sector_id"] != envelope_profile["large_sector_id"]
            or decision["periodic_report_document_id"]
            != envelope_profile["periodic_report_document_id"]
            or _HEX64_RE.fullmatch(
                str(envelope_profile["periodic_report_full_text_hash"] or "")
            )
            is None
        ):
            raise ValueError("compatibility selected decision is orphaned or cross-sector")
        selected_targets.add(target)
    derived_status = (
        "PENDING"
        if any(row.get("status") == "PENDING" for row in decisions)
        else "ABSTAINED"
        if any(row.get("status") == "ABSTAIN" for row in decisions)
        else "COMPLETE"
    )
    if receipt["status"] != derived_status:
        raise ValueError("compatibility receipt status projection is invalid")
    expected_request = "PROFILECLASSREQ-" + stable_hash(
        {
            "provider_name": receipt["provider_name"],
            "prompt_hash": receipt["prompt_hash"],
        }
    )[:24]
    receipt_core = {key: value for key, value in receipt.items() if key != "response_id"}
    if (
        receipt["request_id"] != expected_request
        or receipt["response_id"]
        != "PROFILECLASSRESP-" + stable_hash(receipt_core)[:24]
    ):
        raise ValueError("compatibility request/response id hash mismatch")
    return receipt


def _result(
    *,
    config: IssuerBusinessProfileConfig,
    profiles: Sequence[Mapping[str, Any]],
    selections: Sequence[Mapping[str, Any]],
    receipts: Sequence[Mapping[str, Any]],
    pending: Sequence[Mapping[str, Any]],
    fetch_count: int,
    stopped_on_five: bool,
    provider_status: str,
    candidate_expansion_receipt: Mapping[str, Any],
) -> Mapping[str, Any]:
    selected_complete = (
        tuple(str(row.get("archetype_id") or "") for row in selections)
        == REQUIRED_ARCHETYPES
        and len({str(row.get("target_id") or "") for row in selections})
        == len(REQUIRED_ARCHETYPES)
    )
    latest_decisions = tuple(receipts[-1].get("decisions") or ()) if receipts else ()
    has_abstain = any(row.get("status") == "ABSTAIN" for row in latest_decisions)
    forced_discovery_pending = (
        candidate_expansion_receipt.get("status") == "PENDING"
    )
    if config.test_mode:
        status = PROFILE_TEST_ONLY
    elif selected_complete and not forced_discovery_pending:
        status = PROFILE_PASS
    elif has_abstain and not any("PENDING" in str(row.get("code") or "") for row in pending):
        status = PROFILE_ABSTAINED
    else:
        status = PROFILE_PENDING
    audit = {
        "required_archetype_count": len(REQUIRED_ARCHETYPES),
        "selected_archetype_count": len(selections),
        "unique_selected_target_count": len(
            {str(row.get("target_id") or "") for row in selections}
        ),
        "profile_fetch_count": fetch_count,
        "max_profile_fetches": config.max_profile_fetches,
        "max_compatibility_prompt_chars": config.max_compatibility_prompt_chars,
        "profile_count": len(profiles),
        "compatibility_receipt_count": len(receipts),
        "provider_status": provider_status,
        "stopped_on_five": stopped_on_five,
        "official_only": True,
        "production_acceptance_pass": status == PROFILE_PASS,
        "diagnostic_count": len(pending),
        "forced_validation_authority": False,
        "score_or_stage_authority": False,
        "gold_authority": False,
    }
    return {
        "schema_version": PROFILE_RESULT_SCHEMA_VERSION,
        "status": status,
        "as_of_date": config.as_of_date,
        "required_archetypes": list(REQUIRED_ARCHETYPES),
        "profiles": list(profiles),
        "selections": list(selections),
        "compatibility_receipts": list(receipts),
        "candidate_expansion_receipt": dict(candidate_expansion_receipt),
        "pending": list(pending),
        "audit": audit,
        "forced_validation_authority": False,
        "score_or_stage_authority": False,
        "gold_authority": False,
    }


def _source_receipt(
    *,
    role: str,
    target_id: str,
    as_of_date: date,
    canonical_url: str,
    request_params: Mapping[str, Any],
    response_text: str,
) -> Mapping[str, Any]:
    params = dict(request_params)
    return {
        "role": role,
        "provider_name": "OpenDART",
        "canonical_url": canonical_url,
        "request_params": params,
        "request_id": _official_request_id(
            role=role,
            target_id=target_id,
            as_of_date=as_of_date.isoformat(),
            request_params=params,
        ),
        "response_text": response_text,
        "response_hash": _sha256_text(response_text),
    }


def _official_request_id(
    *,
    role: str,
    target_id: str,
    as_of_date: str,
    request_params: Mapping[str, Any],
) -> str:
    return "PROFILEFETCH-" + stable_hash(
        {
            "provider_name": "OpenDART",
            "role": role,
            "target_id": target_id,
            "as_of_date": as_of_date,
            "request_params": dict(request_params),
        }
    )[:24]


def _pending_fetch(
    *, target_id: str, company_name: str, error_category: str, request_count: int
) -> Mapping[str, Any]:
    return {
        "status": "PENDING",
        "provider_name": "OpenDART",
        "target_id": target_id,
        "company_name": company_name,
        "request_count": request_count,
        "error_category": error_category,
    }


def _pending_discovery(
    *, target_id: str, company_name: str, error_category: str, request_count: int
) -> Mapping[str, Any]:
    return {
        "status": "PENDING",
        "provider_name": "OpenDART",
        "target_id": target_id,
        "company_name": company_name,
        "request_count": request_count,
        "error_category": error_category,
    }


@lru_cache(maxsize=4)
def _corp_row_index(text: str) -> Mapping[str, tuple[str, str]]:
    """Parse one immutable OpenDART corp-code document only once.

    Phase-105 discovery looks up many KRX symbols in the same large official
    XML response.  Caching the document-level index preserves the exact
    uniqueness and completeness checks while avoiding a full XML parse for
    every candidate.
    """

    root = ET.fromstring(text)
    matches: dict[str, list[tuple[str, str]]] = {}
    for item in root.findall("list"):
        raw_stock_code = str(item.findtext("stock_code") or "").strip()
        if not raw_stock_code:
            continue
        stock_code = raw_stock_code.zfill(6)
        matches.setdefault(stock_code, []).append(
            (
                str(item.findtext("corp_code") or "").strip(),
                str(item.findtext("corp_name") or "").strip(),
            )
        )
    return {
        stock_code: rows[0]
        for stock_code, rows in matches.items()
        if len(rows) == 1 and all(rows[0])
    }


def _corp_row(text: str, *, target_id: str) -> Mapping[str, str] | None:
    row = _corp_row_index(text).get(target_id)
    if row is None:
        return None
    corp_code, corp_name = row
    return {
        "stock_code": target_id,
        "corp_code": corp_code,
        "corp_name": corp_name,
    }


def _latest_periodic_row(
    list_texts: Sequence[str], *, corp_code: str, as_of_date: date
) -> Mapping[str, Any] | None:
    rows: list[Mapping[str, Any]] = []
    for text in list_texts:
        payload = json.loads(text)
        for raw in payload.get("list") or ():
            if not isinstance(raw, Mapping):
                continue
            report_name = str(raw.get("report_nm") or "")
            rcept_date = str(raw.get("rcept_dt") or "")
            if (
                str(raw.get("corp_code") or corp_code) == corp_code
                and any(token in report_name for token in _PERIODIC_REPORT_TOKENS)
                and re.fullmatch(r"[0-9]{8}", rcept_date)
                and _yyyymmdd_to_date(rcept_date) <= as_of_date
                and str(raw.get("rcept_no") or "")
            ):
                rows.append(dict(raw))
    return max(rows, key=lambda row: (str(row["rcept_dt"]), str(row["rcept_no"]))) if rows else None


def _sector_quota_available(profiles: Sequence[Mapping[str, Any]]) -> bool:
    sectors = [str(row.get("large_sector_id") or "") for row in profiles]
    required = [large_sector_for_archetype(archetype) for archetype in REQUIRED_ARCHETYPES]
    return all(sectors.count(sector) >= required.count(sector) for sector in set(required))


def _same_company_name(left: object, right: object) -> bool:
    def normalize(value: object) -> str:
        text = re.sub(r"\s+", "", str(value or ""))
        for marker in ("주식회사", "(주)", "㈜"):
            text = text.replace(marker, "")
        return text.casefold()

    return bool(normalize(left)) and normalize(left) == normalize(right)


def _decode_corp_code_payload(payload: bytes) -> str:
    if not zipfile.is_zipfile(io.BytesIO(payload)):
        raise ValueError("OpenDART corpCode response is not a zip archive")
    with zipfile.ZipFile(io.BytesIO(payload)) as archive:
        names = [name for name in archive.namelist() if not name.endswith("/")]
        if len(names) != 1:
            raise ValueError("OpenDART corpCode archive file roster is invalid")
        return _decode_bytes(archive.read(names[0]))


def _decode_document_payload(payload: bytes) -> str:
    if zipfile.is_zipfile(io.BytesIO(payload)):
        with zipfile.ZipFile(io.BytesIO(payload)) as archive:
            names = [name for name in archive.namelist() if not name.endswith("/")]
            xml_names = [name for name in names if name.lower().endswith(".xml")]
            selected = xml_names or names
            return "\n".join(_decode_bytes(archive.read(name)) for name in selected).strip()
    return _decode_bytes(payload).strip()


def _decode_bytes(payload: bytes) -> str:
    for encoding in ("utf-8-sig", "utf-8", "cp949", "euc-kr"):
        try:
            return payload.decode(encoding)
        except UnicodeDecodeError:
            continue
    return payload.decode("utf-8", errors="replace")


def _assert_no_forbidden_output_keys(value: Any) -> None:
    if isinstance(value, Mapping):
        for key, child in value.items():
            if _FORBIDDEN_KEY_RE.search(str(key)):
                raise ValueError("compatibility response contains score, Stage, or Gold")
            _assert_no_forbidden_output_keys(child)
    elif isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        for child in value:
            _assert_no_forbidden_output_keys(child)


def _deduplicated_rows(rows: Sequence[Mapping[str, Any]]) -> tuple[Mapping[str, Any], ...]:
    unique: dict[str, Mapping[str, Any]] = {}
    for row in rows:
        unique.setdefault(stable_hash(dict(row)), dict(row))
    return tuple(unique.values())


def _sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _yyyymmdd_to_date(value: object) -> date:
    text = str(value or "")
    if re.fullmatch(r"[0-9]{8}", text) is None:
        raise ValueError("OpenDART receipt date is invalid")
    return date(int(text[:4]), int(text[4:6]), int(text[6:8]))


def _yyyymmdd_to_iso(value: object) -> str:
    return _yyyymmdd_to_date(value).isoformat()


__all__ = [
    "CANDIDATE_EXPANSION_RECEIPT_SCHEMA_VERSION",
    "CANONICAL_COMPATIBILITY_PROVIDER",
    "CompatibilityProviderCompletion",
    "IssuerBusinessCompatibilityProvider",
    "IssuerBusinessProfileConfig",
    "IssuerBusinessProfileFetcher",
    "INDUSTRY_DISCOVERY_SCHEMA_VERSION",
    "PROFILE_ABSTAINED",
    "PROFILE_PASS",
    "PROFILE_PENDING",
    "PROFILE_SCHEMA_VERSION",
    "PROFILE_RESULT_SCHEMA_VERSION",
    "PROFILE_SELECTION_RECEIPT_SCHEMA_VERSION",
    "PROFILE_TEST_ONLY",
    "REQUIRED_ARCHETYPES",
    "RequestsOpenDartIssuerBusinessProfileFetcher",
    "V6IssuerBusinessProfileMaterializer",
    "large_sector_for_industry_code",
    "validate_candidate_expansion_receipt",
    "validate_forced_validation_profile_manifest",
    "validate_issuer_industry_discovery",
    "validate_issuer_business_profile",
    "validate_issuer_business_profile_receipt",
    "validate_issuer_business_profile_result",
]
