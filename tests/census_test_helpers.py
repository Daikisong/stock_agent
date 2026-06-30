from __future__ import annotations

import csv
from pathlib import Path
from tempfile import TemporaryDirectory

from e2r.census.schemas import UniverseInstrument


def instrument(symbol: str = "005930", name: str = "삼성전자", sector: str | None = "반도체") -> UniverseInstrument:
    return UniverseInstrument(symbol=symbol, company_name=name, market="KOSPI", large_sector_id=sector)


def write_universe_csv(path: Path, count: int = 5) -> Path:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["symbol", "company_name", "market", "instrument_type", "listing_status"])
        writer.writeheader()
        for idx in range(1, count + 1):
            writer.writerow(
                {
                    "symbol": f"{idx:06d}",
                    "company_name": f"테스트회사{idx:04d}",
                    "market": "KOSPI" if idx % 2 else "KOSDAQ",
                    "instrument_type": "COMMON",
                    "listing_status": "ACTIVE",
                }
            )
    return path
