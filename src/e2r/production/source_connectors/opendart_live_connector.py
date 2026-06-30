"""OpenDART live connector for production cutover checks."""

from __future__ import annotations

import hashlib
import io
import json
import os
import time
import zipfile
from datetime import date, datetime
from functools import lru_cache
from pathlib import Path
from typing import Any, Mapping
import xml.etree.ElementTree as ET

import requests

from e2r.env import load_project_env

from .source_provider_registry import LocalSnapshotConnector, SourceFetchResult


_CORP_CODE_URL = "https://opendart.fss.or.kr/api/corpCode.xml"
_COMPANY_URL = "https://opendart.fss.or.kr/api/company.json"


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
            response = requests.get(_COMPANY_URL, params={"crtfc_key": key, "corp_code": corp_row["corp_code"]}, timeout=30)
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
            raw_text = json.dumps(public_payload, ensure_ascii=False, sort_keys=True)
            content_hash = hashlib.sha256(raw_text.encode("utf-8")).hexdigest()
            corp_code = str(corp_row["corp_code"])
            return SourceFetchResult(
                provider_name=self.provider_name,
                source_class=self.source_class,
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
