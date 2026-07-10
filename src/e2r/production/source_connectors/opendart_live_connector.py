"""OpenDART live connector for production cutover checks."""

from __future__ import annotations

import hashlib
import io
import json
import os
import time
import zipfile
from datetime import date, datetime, timedelta
from functools import lru_cache
from pathlib import Path
from typing import Any, Mapping
import xml.etree.ElementTree as ET

import requests

from e2r.env import load_project_env
from e2r.sources.opendart import OpenDARTConnector, normalize_disclosure_detail

from .source_provider_registry import LocalSnapshotConnector, SourceFetchResult


_CORP_CODE_URL = "https://opendart.fss.or.kr/api/corpCode.xml"
_COMPANY_URL = "https://opendart.fss.or.kr/api/company.json"
_LIST_URL = "https://opendart.fss.or.kr/api/list.json"
_DETAIL_URL = "https://opendart.fss.or.kr/api/document.xml"
_DART_VIEWER_URL = "https://dart.fss.or.kr/dsaf001/main.do"
_DISCLOSURE_LOOKBACK_DAYS = 540


class OpenDARTLiveConnector:
    provider_name = "OpenDART"
    source_class = "DART"

    def __init__(self, *, repo_root: str | Path = ".") -> None:
        self.repo_root = Path(repo_root)
        self._snapshot = LocalSnapshotConnector(
            provider_name=self.provider_name,
            source_class=self.source_class,
            repo_root=self.repo_root,
            path_patterns=("data/raw/opendart/disclosures/*.csv", "data/raw/korea_cheap_scan/opendart/disclosures/*.csv"),
        )

    def fetch(self, *, symbol: str, company_name: str, as_of_date: date, mode: str) -> SourceFetchResult:
        if mode != "live":
            return self._snapshot.fetch(symbol=symbol, company_name=company_name, as_of_date=as_of_date, mode=mode)
        request_id = _stable_id("SRCREQ-OPENDART", symbol, company_name, as_of_date.isoformat())
        started = time.monotonic()
        load_project_env()
        key = os.environ.get("OPENDART_API_KEY") or os.environ.get("OPEN_DART_API_KEY")
        if not key:
            return _failed(
                request_id=request_id,
                status="AUTH_FAILED",
                error="OPENDART_API_KEY is not configured",
                symbol=symbol,
                company_name=company_name,
                started=started,
            )
        try:
            corp_row = _corp_row_for_symbol(key, symbol)
            if corp_row is None:
                return SourceFetchResult(
                    provider_name=self.provider_name,
                    source_class=self.source_class,
                    mode="live",
                    request_id=request_id,
                    request_params={"symbol": symbol, "company_name": company_name},
                    status="NO_RESULT",
                    fetched_at=_utc_now(),
                    provider_request_id=request_id,
                    freshness_seconds=round(time.monotonic() - started, 4),
                    provider_error="symbol_not_found_in_opendart_corp_code",
            )
            corp_code = str(corp_row["corp_code"])
            try:
                disclosure_result = _fetch_latest_disclosure_result(
                    api_key=key,
                    corp_code=corp_code,
                    symbol=symbol,
                    company_name=company_name,
                    as_of_date=as_of_date,
                    request_id=request_id,
                    started=started,
                )
            except Exception:
                disclosure_result = None
            if disclosure_result is not None:
                return disclosure_result
            return _fetch_company_profile_result(
                api_key=key,
                corp_code=corp_code,
                symbol=symbol,
                company_name=company_name,
                as_of_date=as_of_date,
                request_id=request_id,
                started=started,
            )
        except Exception as exc:  # pragma: no cover - exercised by live environment variance
            return _failed(
                request_id=request_id,
                status="PROVIDER_FAILED",
                error=f"{type(exc).__name__}: {exc}",
                symbol=symbol,
                company_name=company_name,
                started=started,
            )


@lru_cache(maxsize=2)
def _corp_rows(api_key: str) -> tuple[Mapping[str, str], ...]:
    response = requests.get(_CORP_CODE_URL, params={"crtfc_key": api_key}, timeout=30)
    response.raise_for_status()
    if response.content[:2] != b"PK":
        raise RuntimeError("OpenDART corpCode did not return a zip payload")
    archive = zipfile.ZipFile(io.BytesIO(response.content))
    root = ET.fromstring(archive.read(archive.namelist()[0]))
    rows: list[Mapping[str, str]] = []
    for item in root.findall("list"):
        stock_code = (item.findtext("stock_code") or "").strip()
        if not stock_code:
            continue
        rows.append(
            {
                "symbol": stock_code,
                "company_name": (item.findtext("corp_name") or "").strip(),
                "corp_code": (item.findtext("corp_code") or "").strip(),
            }
        )
    return tuple(rows)


def _corp_row_for_symbol(api_key: str, symbol: str) -> Mapping[str, str] | None:
    clean = str(symbol).zfill(6)
    for row in _corp_rows(api_key):
        if row.get("symbol") == clean:
            return row
    return None


def _fetch_latest_disclosure_result(
    *,
    api_key: str,
    corp_code: str,
    symbol: str,
    company_name: str,
    as_of_date: date,
    request_id: str,
    started: float,
) -> SourceFetchResult | None:
    start = as_of_date - timedelta(days=_DISCLOSURE_LOOKBACK_DAYS)
    response = requests.get(
        _LIST_URL,
        params={
            "crtfc_key": api_key,
            "corp_code": corp_code,
            "bgn_de": start.strftime("%Y%m%d"),
            "end_de": as_of_date.strftime("%Y%m%d"),
            "page_no": 1,
            "page_count": 100,
        },
        timeout=30,
    )
    response.raise_for_status()
    payload = response.json()
    status = str(payload.get("status") or "")
    if status == "013":
        return None
    if status and status != "000":
        raise RuntimeError(f"OpenDART list.json failed: {status} {payload.get('message')}")
    for row in _watch_disclosure_rows(payload, symbol=symbol, company_name=company_name):
        base_event = OpenDARTConnector.normalize_disclosure(row)
        if not base_event.rcept_no:
            continue
        try:
            raw_detail = _fetch_detail_text(api_key=api_key, rcept_no=base_event.rcept_no)
        except Exception:
            raw_detail = ""
        if raw_detail:
            detail_event = normalize_disclosure_detail(base_event, raw_detail, as_of_date=as_of_date)
            return _disclosure_fetch_result(
                event=detail_event,
                symbol=symbol,
                company_name=company_name,
                request_id=request_id,
                started=started,
                row_source="opendart_detail",
                raw_document=raw_detail,
                score_usage=None,
            )
        return _disclosure_fetch_result(
            event=base_event,
            symbol=symbol,
            company_name=company_name,
            request_id=request_id,
            started=started,
            row_source="opendart_list",
            raw_document=json.dumps(row, ensure_ascii=False, sort_keys=True),
            score_usage="opendart_list_only_detail_not_fetched",
        )
    return None


def _watch_disclosure_rows(payload: Mapping[str, Any], *, symbol: str, company_name: str) -> tuple[Mapping[str, Any], ...]:
    rows = payload.get("list") or ()
    if not isinstance(rows, (list, tuple)):
        return ()
    selected: list[Mapping[str, Any]] = []
    for row in rows:
        if not isinstance(row, Mapping):
            continue
        report_name = str(row.get("report_nm") or row.get("report_name") or row.get("title") or "")
        if not _is_watch_report(report_name):
            continue
        normalized = dict(row)
        normalized.setdefault("symbol", symbol)
        normalized.setdefault("stock_code", symbol)
        normalized.setdefault("corp_name", company_name)
        normalized.setdefault("source", "OpenDART")
        selected.append(normalized)
    return tuple(selected)


def _is_watch_report(report_name: str) -> bool:
    return any(
        token in report_name
        for token in (
            "단일판매",
            "공급계약",
            "신규시설투자",
            "잠정실적",
            "영업실적",
            "사업보고서",
            "반기보고서",
            "분기보고서",
            "유상증자",
            "전환사채",
            "신주인수권부사채",
            "감사의견",
            "거래정지",
            "상장폐지",
            "관리종목",
            "소송",
            "계약 해지",
            "계약 취소",
            "계약 정정",
        )
    )


def _fetch_detail_text(*, api_key: str, rcept_no: str) -> str:
    response = requests.get(_DETAIL_URL, params={"crtfc_key": api_key, "rcept_no": rcept_no}, timeout=30)
    response.raise_for_status()
    text = _decode_detail_payload(
        response.content or response.text.encode("utf-8", errors="replace")
    )
    if len(text.strip()) < 80 or "파일이 존재하지 않습니다" in text:
        return ""
    return text


def _decode_detail_payload(payload: bytes) -> str:
    if not payload:
        return ""
    if zipfile.is_zipfile(io.BytesIO(payload)):
        with zipfile.ZipFile(io.BytesIO(payload)) as archive:
            names = [name for name in archive.namelist() if not name.endswith("/")]
            xml_names = [name for name in names if name.lower().endswith(".xml")]
            targets = xml_names or names[:1]
            return "\n".join(_decode_detail_bytes(archive.read(name)) for name in targets).strip()
    return _decode_detail_bytes(payload)


def _decode_detail_bytes(payload: bytes) -> str:
    for encoding in ("utf-8-sig", "utf-8", "cp949", "euc-kr"):
        try:
            return payload.decode(encoding)
        except UnicodeDecodeError:
            continue
    return payload.decode("utf-8", errors="replace")


def _disclosure_fetch_result(
    *,
    event: Any,
    symbol: str,
    company_name: str,
    request_id: str,
    started: float,
    row_source: str,
    raw_document: str,
    score_usage: str | None,
) -> SourceFetchResult:
    parsed_fields = dict(getattr(event, "parsed_fields", {}) or {})
    rcept_no = str(getattr(event, "rcept_no", "") or "")
    published_at_value = getattr(event, "published_at", None)
    available_at_value = getattr(event, "available_at", None)
    structured_payload: dict[str, Any] = {
        "symbol": symbol,
        "company_name": company_name,
        "provider": "OpenDART",
        "row_source": row_source,
        "report_type": getattr(event, "report_type", None),
        "title": getattr(event, "title", None),
        "rcept_no": rcept_no,
        "published_at": published_at_value.isoformat() if hasattr(published_at_value, "isoformat") else None,
        "available_at": available_at_value.isoformat() if hasattr(available_at_value, "isoformat") else None,
        **parsed_fields,
    }
    if score_usage:
        structured_payload["score_usage"] = score_usage
    raw_text = str(getattr(event, "raw_text", "") or raw_document or json.dumps(structured_payload, ensure_ascii=False, sort_keys=True))
    content_hash = hashlib.sha256(raw_text.encode("utf-8")).hexdigest()
    published_date = published_at_value.date() if hasattr(published_at_value, "date") else None
    available_date = available_at_value.date() if hasattr(available_at_value, "date") else None
    return SourceFetchResult(
        provider_name=OpenDARTLiveConnector.provider_name,
        source_class=OpenDARTLiveConnector.source_class,
        mode="live",
        request_id=request_id,
        request_params={"symbol": symbol, "company_name": company_name, "rcept_no": rcept_no},
        status="FETCHED",
        canonical_url=f"{_DART_VIEWER_URL}?rcpNo={rcept_no}" if rcept_no else _LIST_URL,
        official_document_id=f"opendart:disclosure:{rcept_no}" if rcept_no else f"opendart:disclosure:{content_hash[:12]}",
        published_at=published_date.isoformat() if published_date else None,
        available_at=available_date.isoformat() if available_date else None,
        fetched_at=_utc_now(),
        content_hash=content_hash,
        raw_text=raw_text,
        structured_payload=structured_payload,
        provider_request_id=request_id,
        freshness_seconds=round(time.monotonic() - started, 4),
    )


def _fetch_company_profile_result(
    *,
    api_key: str,
    corp_code: str,
    symbol: str,
    company_name: str,
    as_of_date: date,
    request_id: str,
    started: float,
) -> SourceFetchResult:
    response = requests.get(_COMPANY_URL, params={"crtfc_key": api_key, "corp_code": corp_code}, timeout=30)
    response.raise_for_status()
    payload = response.json()
    if payload.get("status") != "000":
        return _failed(
            request_id=request_id,
            status="PROVIDER_FAILED",
            error=f"OpenDART company.json failed: {payload.get('status')} {payload.get('message')}",
            symbol=symbol,
            company_name=company_name,
            started=started,
        )
    public_payload = {key: value for key, value in payload.items() if key != "status"}
    public_payload.setdefault("score_usage", "company_profile_not_score_evidence")
    raw_text = json.dumps(public_payload, ensure_ascii=False, sort_keys=True)
    content_hash = hashlib.sha256(raw_text.encode("utf-8")).hexdigest()
    return SourceFetchResult(
        provider_name=OpenDARTLiveConnector.provider_name,
        source_class=OpenDARTLiveConnector.source_class,
        mode="live",
        request_id=request_id,
        request_params={"symbol": symbol, "company_name": company_name, "corp_code": corp_code},
        status="FETCHED",
        canonical_url=f"{_COMPANY_URL}?corp_code={corp_code}",
        official_document_id=f"opendart:company:{corp_code}",
        published_at=as_of_date.isoformat(),
        available_at=as_of_date.isoformat(),
        fetched_at=_utc_now(),
        content_hash=content_hash,
        raw_text=raw_text,
        structured_payload=public_payload,
        provider_request_id=request_id,
        freshness_seconds=round(time.monotonic() - started, 4),
    )


def _failed(
    *,
    request_id: str,
    status: str,
    error: str,
    symbol: str,
    company_name: str,
    started: float,
) -> SourceFetchResult:
    return SourceFetchResult(
        provider_name=OpenDARTLiveConnector.provider_name,
        source_class=OpenDARTLiveConnector.source_class,
        mode="live",
        request_id=request_id,
        request_params={"symbol": symbol, "company_name": company_name},
        status=status,
        fetched_at=_utc_now(),
        provider_error=error,
        provider_request_id=request_id,
        freshness_seconds=round(time.monotonic() - started, 4),
    )


def _utc_now() -> str:
    return datetime.utcnow().isoformat(timespec="seconds") + "Z"


def _stable_id(prefix: str, *parts: object) -> str:
    digest = hashlib.sha256("|".join(str(part) for part in parts).encode("utf-8")).hexdigest()[:20]
    return f"{prefix}-{digest}"


__all__ = ["OpenDARTLiveConnector"]
