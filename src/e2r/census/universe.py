"""Universe builder for Census Mode."""

from __future__ import annotations

import csv
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping
from urllib.parse import urljoin

from e2r.production.metadata import write_json

from .schemas import InstrumentType, UniverseInstrument


PREFERRED_RE = re.compile(r"(우$|우B$|우C$|[123]우$|우선주)")
SPAC_RE = re.compile(r"(스팩|SPAC)", re.IGNORECASE)
REIT_RE = re.compile(r"(리츠|REIT)", re.IGNORECASE)
ETF_RE = re.compile(r"(ETF|상장지수)", re.IGNORECASE)
ETN_RE = re.compile(r"(ETN|상장지수증권)", re.IGNORECASE)
VALID_SYMBOL_RE = re.compile(r"^\d{6}$")


@dataclass(frozen=True)
class UniverseBuildResult:
    instruments: tuple[UniverseInstrument, ...]
    coverage: dict[str, Any]


def load_sector_map(path: str | Path = "data/sector_taxonomy/korea_sector_map.csv") -> dict[str, dict[str, str]]:
    p = Path(path)
    if not p.exists():
        return {}
    with p.open(encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return {str(row.get("symbol", "")).zfill(6): dict(row) for row in reader if row.get("symbol")}


def build_universe(
    *,
    as_of_date: str,
    universe_file: str | Path | None = None,
    max_symbols: int = 0,
    sector_map_path: str | Path = "data/sector_taxonomy/korea_sector_map.csv",
    allow_naver_fallback: bool = True,
) -> UniverseBuildResult:
    sector_map = load_sector_map(sector_map_path)
    rows = _load_rows(universe_file=universe_file, allow_naver_fallback=allow_naver_fallback)
    instruments = tuple(_instrument_from_row(row, sector_map=sector_map) for row in rows)
    instruments = tuple(sorted(_dedupe_by_symbol(instruments), key=lambda item: item.symbol))
    if max_symbols and max_symbols > 0:
        instruments = instruments[:max_symbols]
    coverage = universe_coverage(instruments, as_of_date=as_of_date)
    return UniverseBuildResult(instruments=instruments, coverage=coverage)


def write_universe_coverage(path: str | Path, coverage: Mapping[str, Any]) -> None:
    write_json(Path(path), dict(coverage))


def universe_coverage(instruments: Iterable[UniverseInstrument], *, as_of_date: str) -> dict[str, Any]:
    rows = tuple(instruments)
    eligible = tuple(item for item in rows if item.eligible_for_census)
    excluded = tuple(item for item in rows if not item.eligible_for_census)
    by_reason: dict[str, int] = {}
    market_breakdown: dict[str, int] = {}
    sector_breakdown: dict[str, int] = {}
    for item in rows:
        market_breakdown[item.market] = market_breakdown.get(item.market, 0) + 1
        sector_key = item.large_sector_id or "unknown"
        sector_breakdown[sector_key] = sector_breakdown.get(sector_key, 0) + 1
        if item.exclusion_reason:
            by_reason[item.exclusion_reason] = by_reason.get(item.exclusion_reason, 0) + 1
    return {
        "schema_version": "e2r_census_universe_coverage_v1",
        "as_of_date": as_of_date,
        "raw_universe_count": len(rows),
        "eligible_common_stock_count": len(eligible),
        "excluded_total_count": len(excluded),
        "excluded_etf_count": by_reason.get("ETF", 0),
        "excluded_etn_count": by_reason.get("ETN", 0),
        "excluded_spac_count": by_reason.get("SPAC", 0),
        "excluded_reit_count": by_reason.get("REIT", 0),
        "excluded_preferred_count": by_reason.get("PREFERRED", 0),
        "excluded_inactive_count": by_reason.get("INACTIVE", 0),
        "excluded_invalid_symbol_count": by_reason.get("INVALID_SYMBOL", 0),
        "fixture_like_symbol_count": sum(1 for item in rows if is_fixture_like_symbol(item.symbol)),
        "missing_company_name_count": sum(1 for item in rows if not item.company_name),
        "missing_sector_count": sum(1 for item in eligible if not item.large_sector_id),
        "active_market_breakdown": market_breakdown,
        "sector_coverage_breakdown": sector_breakdown,
    }


def eligible_instruments(instruments: Iterable[UniverseInstrument]) -> tuple[UniverseInstrument, ...]:
    return tuple(item for item in instruments if item.eligible_for_census)


def is_fixture_like_symbol(symbol: str) -> bool:
    value = str(symbol).strip().upper()
    return value.startswith(("TEST", "SAMPLE", "FIXTURE")) or not VALID_SYMBOL_RE.match(value)


def _load_rows(*, universe_file: str | Path | None, allow_naver_fallback: bool) -> tuple[dict[str, Any], ...]:
    if universe_file:
        return tuple(_read_csv_rows(Path(universe_file)))
    default_file = Path("data/krx/universe_latest.csv")
    if default_file.exists():
        return tuple(_read_csv_rows(default_file))
    fixture_file = Path("data/historical_official/universe/universe.csv")
    if fixture_file.exists() and not allow_naver_fallback:
        return tuple(_read_csv_rows(fixture_file))
    if allow_naver_fallback:
        return fetch_naver_market_sum_universe()
    if fixture_file.exists():
        return tuple(_read_csv_rows(fixture_file))
    return ()


def _read_csv_rows(path: Path) -> list[dict[str, Any]]:
    if path.suffix.lower() == ".jsonl":
        rows: list[dict[str, Any]] = []
        with path.open(encoding="utf-8") as handle:
            for line in handle:
                text = line.strip()
                if text:
                    rows.append(json.loads(text))
        return rows
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def fetch_naver_market_sum_universe() -> tuple[dict[str, Any], ...]:
    """Fetch KRX-listed common board rows from Naver Finance pages.

    This is a structured fallback for environments without KRX OpenAPI keys.
    The rows still represent KRX-listed KOSPI/KOSDAQ instruments, but reports
    keep the source visible so the official-provider gap is not hidden.
    """

    try:
        import requests
    except Exception:
        return ()
    rows: list[dict[str, Any]] = []
    for sosok, market in ((0, "KOSPI"), (1, "KOSDAQ")):
        for page in range(1, 80):
            url = f"https://finance.naver.com/sise/sise_market_sum.naver?sosok={sosok}&page={page}"
            response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
            if response.status_code != 200:
                break
            text = response.text
            matches = re.findall(r"code=(\d{6})\"[^>]*>([^<]+)</a>", text)
            if not matches:
                break
            for symbol, name in matches:
                rows.append(
                    {
                        "symbol": symbol,
                        "company_name": name.strip(),
                        "name": name.strip(),
                        "market": market,
                        "listing_status": "ACTIVE",
                        "universe_source_url": urljoin(url, f"/item/main.naver?code={symbol}"),
                    }
                )
    return tuple(rows)


def _dedupe_by_symbol(instruments: Iterable[UniverseInstrument]) -> tuple[UniverseInstrument, ...]:
    seen: dict[str, UniverseInstrument] = {}
    for item in instruments:
        if item.symbol not in seen:
            seen[item.symbol] = item
    return tuple(seen.values())


def _instrument_from_row(row: Mapping[str, Any], *, sector_map: Mapping[str, Mapping[str, str]]) -> UniverseInstrument:
    symbol = str(row.get("symbol") or row.get("code") or "").strip().zfill(6)
    company_name = str(row.get("company_name") or row.get("name") or row.get("isuAbbrv") or row.get("ISU_ABBRV") or "").strip()
    market = _normalize_market(row.get("market") or row.get("mktNm") or row.get("MKT_NM") or row.get("exchange") or "KOSPI")
    status = str(row.get("listing_status") or row.get("instrument_status") or "ACTIVE").strip() or "ACTIVE"
    active = status.upper() not in {"DELISTED", "INACTIVE"}
    instrument_type = _detect_instrument_type(symbol=symbol, company_name=company_name, row=row)
    exclusion_reason: str | None = None
    if is_fixture_like_symbol(symbol):
        exclusion_reason = "INVALID_SYMBOL"
    elif not company_name:
        exclusion_reason = "MISSING_COMPANY_NAME"
    elif instrument_type != InstrumentType.COMMON:
        exclusion_reason = instrument_type.value
    elif not active:
        exclusion_reason = "INACTIVE"
    sector = sector_map.get(symbol, {})
    return UniverseInstrument(
        symbol=symbol,
        company_name=company_name,
        market=market,
        instrument_type=instrument_type,
        is_active=active,
        listing_status=status,
        large_sector_id=str(sector.get("sector_custom") or row.get("large_sector_id") or "").strip() or None,
        sector_source=str(sector.get("sector_source") or row.get("sector_source") or "unknown"),
        eligible_for_census=exclusion_reason is None,
        exclusion_reason=exclusion_reason,
    )


def _normalize_market(value: Any) -> str:
    text = str(value or "").upper()
    if "KOSDAQ" in text or "KSQ" in text:
        return "KOSDAQ"
    if "KONEX" in text:
        return "KONEX"
    if "KOSPI" in text or "STK" in text or text in {"KR", "KRX"}:
        return "KOSPI"
    return text or "OTHER"


def _detect_instrument_type(*, symbol: str, company_name: str, row: Mapping[str, Any]) -> InstrumentType:
    name = company_name.upper()
    if ETF_RE.search(name):
        return InstrumentType.ETF
    if ETN_RE.search(name):
        return InstrumentType.ETN
    if SPAC_RE.search(name):
        return InstrumentType.SPAC
    if REIT_RE.search(name):
        return InstrumentType.REIT
    if PREFERRED_RE.search(company_name) or symbol.endswith(("5", "7", "9")) and company_name.endswith("우"):
        return InstrumentType.PREFERRED
    explicit = str(row.get("instrument_type") or row.get("type") or "").strip().upper()
    if explicit:
        try:
            return InstrumentType(explicit)
        except ValueError:
            pass
    return InstrumentType.COMMON


__all__ = [
    "UniverseBuildResult",
    "build_universe",
    "eligible_instruments",
    "fetch_naver_market_sum_universe",
    "is_fixture_like_symbol",
    "load_sector_map",
    "universe_coverage",
    "write_universe_coverage",
]
