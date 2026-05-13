"""Licensed-data fallback consensus CSV/JSON connector."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any, Mapping

from e2r.models import ConsensusRevision, ConsensusSnapshot
from e2r.sources.source_errors import date_value, float_or_none, int_or_none, load_fixture_records, text_or_none


@dataclass(frozen=True)
class ConsensusCSVConnector:
    """Load consensus estimates and revisions from local licensed-data exports."""

    fixture_root: str | Path | None = "data/raw/consensus"

    def get_consensus(self, symbol: str, as_of_date: date) -> tuple[ConsensusSnapshot, ...]:
        rows = []
        rows.extend(load_fixture_records(self.fixture_root, "kr_consensus"))
        rows.extend(load_fixture_records(self.fixture_root, "us_consensus"))
        snapshots = tuple(self.normalize_consensus(row) for row in rows)
        return tuple(
            sorted(
                (
                    item
                    for item in snapshots
                    if item.symbol == symbol
                    and item.date <= as_of_date
                    and item.as_of_date <= as_of_date
                ),
                key=lambda item: (item.date, item.fiscal_year),
            )
        )

    def get_consensus_revisions(self, symbol: str, as_of_date: date) -> tuple[ConsensusRevision, ...]:
        rows = []
        rows.extend(load_fixture_records(self.fixture_root, "kr_consensus_revisions"))
        rows.extend(load_fixture_records(self.fixture_root, "us_consensus_revisions"))
        revisions = tuple(self.normalize_revision(row) for row in rows)
        return tuple(
            sorted(
                (
                    item
                    for item in revisions
                    if item.symbol == symbol
                    and item.date <= as_of_date
                    and item.as_of_date <= as_of_date
                ),
                key=lambda item: (item.date, item.fiscal_year),
            )
        )

    @staticmethod
    def normalize_consensus(row: Mapping[str, Any]) -> ConsensusSnapshot:
        return ConsensusSnapshot(
            symbol=str(row["symbol"]),
            date=date_value(row.get("date") or row.get("as_of_date")),
            fiscal_year=int(float(row["fiscal_year"])),
            as_of_date=date_value(row["as_of_date"]),
            source=str(row.get("source") or "consensus-csv"),
            sales_e=float_or_none(row.get("sales_e")),
            op_e=float_or_none(row.get("op_e")),
            net_income_e=float_or_none(row.get("net_income_e")),
            eps_e=float_or_none(row.get("eps_e")),
            fcf_e=float_or_none(row.get("fcf_e")),
            bps_e=float_or_none(row.get("bps_e")),
            roe_e=float_or_none(row.get("roe_e")),
            per_e=float_or_none(row.get("per_e")),
            pbr_e=float_or_none(row.get("pbr_e")),
            analyst_count=int_or_none(row.get("analyst_count")),
            target_price=float_or_none(row.get("target_price")),
            target_multiple_type=text_or_none(row.get("target_multiple_type")),
            target_multiple=float_or_none(row.get("target_multiple")),
        )

    @staticmethod
    def normalize_revision(row: Mapping[str, Any]) -> ConsensusRevision:
        return ConsensusRevision(
            symbol=str(row["symbol"]),
            date=date_value(row.get("date") or row.get("as_of_date")),
            fiscal_year=int(float(row["fiscal_year"])),
            as_of_date=date_value(row["as_of_date"]),
            eps_revision_1w=float_or_none(row.get("eps_revision_1w")),
            eps_revision_1m=float_or_none(row.get("eps_revision_1m")),
            eps_revision_3m=float_or_none(row.get("eps_revision_3m")),
            op_revision_1w=float_or_none(row.get("op_revision_1w")),
            op_revision_1m=float_or_none(row.get("op_revision_1m")),
            op_revision_3m=float_or_none(row.get("op_revision_3m")),
            fcf_revision_1m=float_or_none(row.get("fcf_revision_1m")),
            target_price_revision_1m=float_or_none(row.get("target_price_revision_1m")),
            analyst_count_change=int_or_none(row.get("analyst_count_change")),
            street_high_eps_revision_1m=float_or_none(row.get("street_high_eps_revision_1m")),
            street_low_eps_revision_1m=float_or_none(row.get("street_low_eps_revision_1m")),
        )
