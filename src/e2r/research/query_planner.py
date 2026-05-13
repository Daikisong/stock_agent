"""E2R web research query planning."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Mapping, Sequence

from e2r.models import Market


STAGE_DISCOVERY_QUERIES: tuple[str, ...] = (
    "{company} 수주잔고",
    "{company} 장기공급계약",
    "{company} 단일판매 공급계약",
    "{company} 신규시설투자",
    "{company} CAPA 증설",
    "{company} 공급부족",
    "{company} ASP 상승",
    "{company} 판가 상승",
    "{company} 미국향 수주",
    "{company} 데이터센터 수주",
)

STAGE_CONFIRMATION_QUERIES: tuple[str, ...] = (
    "{company} 컨센서스 상회 Review PDF",
    "{company} 영업이익 컨센서스 상회",
    "{company} 목표주가 상향 EPS 상향 PDF",
    "{company} 수주잔고 OPM 수출 비중 PDF",
    "{company} 실적 서프라이즈 목표주가 상향 PDF",
    "{company} 1Q Review 영업이익 컨센서스 PDF",
    "{company} 2Q Review 영업이익 컨센서스 PDF",
    "{company} 3Q Review 영업이익 컨센서스 PDF",
    "{company} 4Q Review 영업이익 컨센서스 PDF",
)

STAGE_MONITORING_QUERIES: tuple[str, ...] = (
    "{company} 수주 둔화",
    "{company} 수주잔고 감소",
    "{company} ASP 하락",
    "{company} 영업이익률 하락",
    "{company} 컨센서스 하향",
    "{company} 계약 취소",
    "{company} 계약 지연",
    "{company} 회계 이슈",
    "{company} 감사의견",
    "{company} 공급과잉",
)

SECTOR_REGIME_QUERIES: tuple[str, ...] = (
    "{sector} 공급 부족",
    "{sector} 리드타임",
    "{sector} 가격 상승",
    "{sector} 장기계약",
    "{sector} 선수금",
    "{sector} CAPA 증설",
)


@dataclass(frozen=True)
class QuerySpec:
    """One planned query and its E2R purpose."""

    group: str
    query: str
    priority: int
    company_name: str
    symbol: str
    sector: str | None
    market: Market
    as_of_date: date


@dataclass(frozen=True)
class QueryPlan:
    """Planned search queries for one company."""

    company_name: str
    symbol: str
    sector: str | None
    market: Market
    as_of_date: date
    queries: tuple[QuerySpec, ...]

    def by_group(self) -> Mapping[str, tuple[QuerySpec, ...]]:
        groups: dict[str, list[QuerySpec]] = {}
        for item in self.queries:
            groups.setdefault(item.group, []).append(item)
        return {key: tuple(value) for key, value in groups.items()}


class QueryPlanner:
    """Build manual-research-style E2R query sets.

    The planner deliberately creates queries only. It does not call a search
    engine, which keeps tests fixture-only and makes later live providers
    swappable.
    """

    def plan(
        self,
        *,
        company_name: str,
        symbol: str,
        sector: str | None,
        market: Market,
        as_of_date: date,
        stage_context: str | None = None,
        groups: Sequence[str] | None = None,
    ) -> QueryPlan:
        selected_groups = tuple(groups or ("discovery", "confirmation", "monitoring", "sector_regime"))
        queries: list[QuerySpec] = []

        def add(group: str, templates: tuple[str, ...], priority: int) -> None:
            if group not in selected_groups:
                return
            for template in templates:
                if "{sector}" in template and not sector:
                    continue
                query = template.format(company=company_name, symbol=symbol, sector=sector or "")
                queries.append(
                    QuerySpec(
                        group=group,
                        query=query,
                        priority=priority,
                        company_name=company_name,
                        symbol=symbol,
                        sector=sector,
                        market=market,
                        as_of_date=as_of_date,
                    )
                )

        add("discovery", STAGE_DISCOVERY_QUERIES, 10)
        add("confirmation", STAGE_CONFIRMATION_QUERIES, 20)
        add("monitoring", STAGE_MONITORING_QUERIES, 30 if stage_context else 40)
        add("sector_regime", SECTOR_REGIME_QUERIES, 50)

        unique: dict[str, QuerySpec] = {}
        for item in sorted(queries, key=lambda query: (query.priority, query.query)):
            unique.setdefault(item.query, item)
        return QueryPlan(
            company_name=company_name,
            symbol=symbol,
            sector=sector,
            market=market,
            as_of_date=as_of_date,
            queries=tuple(unique.values()),
        )


__all__ = [
    "QueryPlan",
    "QueryPlanner",
    "QuerySpec",
    "SECTOR_REGIME_QUERIES",
    "STAGE_CONFIRMATION_QUERIES",
    "STAGE_DISCOVERY_QUERIES",
    "STAGE_MONITORING_QUERIES",
]
