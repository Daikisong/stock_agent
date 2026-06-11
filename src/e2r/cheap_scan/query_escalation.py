"""Map cheap-scan reason codes into targeted web-research queries."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from e2r.cheap_scan.models import CheapScanCandidate, RecommendedNextLayer
from e2r.models import Market
from e2r.research.query_planner import QueryPlan, QuerySpec


REASON_CODE_QUERY_TEMPLATES: dict[str, tuple[str, ...]] = {
    "DISC_SUPPLY_CONTRACT": (
        "{company} 장기공급계약 매출액 대비",
        "{company} 단일판매 공급계약 계약기간",
        "{company} 수주잔고",
        "{company} 미국향 수주",
        "{company} 장기공급계약 PDF",
    ),
    "DISC_LONG_TERM_CONTRACT": (
        "{company} 장기공급계약 계약기간",
        "{company} 수주잔고",
        "{company} 장기공급계약 PDF",
    ),
    "DISC_CONTRACT_TO_SALES_10P": (
        "{company} 장기공급계약 매출액 대비",
        "{company} 단일판매 공급계약 계약기간",
        "{company} 수주잔고",
    ),
    "DISC_FACILITY_INVESTMENT": (
        "{company} 신규시설투자 CAPA 증설",
        "{company} 생산능력 증가",
        "{company} CAPA 증설 PDF",
        "{company} 수요 증가 대응 신규 공장",
    ),
    "DISC_FACILITY_TO_MARKET_CAP_5P": (
        "{company} 신규시설투자 CAPA 증설",
        "{company} CAPA 증설 PDF",
    ),
    "DISC_CAPA_INCREASE": (
        "{company} CAPA 증설 PDF",
        "{company} 생산능력 증가",
        "{company} 리드타임",
    ),
    "DISC_EARNINGS_PREANNOUNCE": (
        "{company} 실적 서프라이즈",
        "{company} 영업이익 컨센서스 상회",
        "{company} 목표주가 상향 EPS 상향 PDF",
        "{company} Review PDF",
    ),
    "DISC_OP_YOY_100P": (
        "{company} 실적 서프라이즈",
        "{company} 영업이익 컨센서스 상회",
        "{company} Review PDF",
    ),
    "PRICE_VOLUME_SPIKE": (
        "{company} 수주잔고",
        "{company} 공급부족",
        "{company} 목표주가 상향",
        "{company} 컨센서스 상회",
    ),
    "PRICE_NEAR_52W_HIGH": (
        "{company} 목표주가 상향",
        "{company} 컨센서스 상회",
    ),
    "PRICE_60D_TOP_PERCENTILE": (
        "{company} 목표주가 상향",
        "{company} 수주잔고",
    ),
    "FIN_OP_TURNAROUND": (
        "{company} 실적 턴어라운드",
        "{company} 영업이익 컨센서스 상회",
        "{company} Review PDF",
    ),
    "FIN_OPM_EXPANSION_5P": (
        "{company} OPM 개선",
        "{company} 마진 개선 목표주가 상향 PDF",
    ),
    "REPORT_RADAR_MATCH": (
        "{company} 컨센서스 상회 Review PDF",
        "{company} 실적 서프라이즈 목표주가 상향 PDF",
    ),
    "REPORT_RADAR_REPORT": (
        "{company} 목표주가 상향 EPS 상향 PDF",
        "{company} 수주잔고 OPM 수출 비중 PDF",
    ),
    "REPORT_RADAR_CONTRACT": (
        "{company} 장기공급계약 매출액 대비 PDF",
        "{company} 수주잔고 OPM 수출 비중 PDF",
    ),
    "REPORT_RADAR_CAPA": (
        "{company} 신규시설투자 CAPA 증설 PDF",
        "{company} CAPA 증설 PDF",
    ),
    "REPORT_RADAR_PRICING": (
        "{company} ASP 상승 판가 상승 리드타임 PDF",
        "{company} 북미 미국향 데이터센터 수주 PDF",
    ),
    "TARGETED_SMOKE": (
        "{company} 수주잔고",
        "{company} 최근 뉴스 실적 전망",
        "{company} 영업이익 컨센서스 상회",
        "{company} 목표주가 상향 EPS 상향",
        "{company} 매출 성장 마진 OPM",
        "{company} AI 데이터센터 HBM 반도체 클라우드",
    ),
    "TOP_TRADING_VALUE_PROBE": (
        "{company} 최근 뉴스 실적 전망",
        "{company} 공시 계약 수주 투자",
        "{company} 목표주가 상향 컨센서스 상회",
        "{company} 매출 성장 마진 OPM",
        "{company} AI 데이터센터 클라우드 반도체 배터리 정책",
    ),
}

NEGATIVE_REASON_QUERY_TEMPLATES: dict[str, tuple[str, ...]] = {
    "DISC_RIGHTS_OFFERING": (
        "{company} 유상증자",
        "{company} 희석 리스크",
        "{company} 보호예수 해제",
        "{company} 오버행",
    ),
    "DISC_CONVERTIBLE_BOND": (
        "{company} 전환사채",
        "{company} CB 발행",
        "{company} CB 리픽싱",
        "{company} 오버행",
    ),
    "DISC_BOND_WITH_WARRANT": (
        "{company} 신주인수권부사채",
        "{company} BW 발행",
        "{company} 보호예수 해제",
        "{company} 오버행",
    ),
    "DISC_AUDIT_OPINION_ISSUE": ("{company} 감사의견", "{company} 회계 이슈"),
    "DISC_TRADING_HALT": ("{company} 거래정지",),
    "RISK_MANAGED_ISSUE": ("{company} 관리종목",),
    "RISK_TRADING_HALT": ("{company} 거래정지",),
    "RISK_DELISTING": ("{company} 상장폐지 위험",),
}


@dataclass(frozen=True)
class EscalationQuerySet:
    """Targeted web research queries for one cheap-scan candidate."""

    symbol: str
    company_name: str
    as_of_date: date
    recommended_next_layer: RecommendedNextLayer
    queries: tuple[str, ...]


def queries_for_reason_codes(company_name: str, reason_codes: tuple[str, ...]) -> tuple[str, ...]:
    queries: list[str] = []
    for code in reason_codes:
        templates = REASON_CODE_QUERY_TEMPLATES.get(code) or NEGATIVE_REASON_QUERY_TEMPLATES.get(code) or ()
        queries.extend(template.format(company=company_name) for template in templates)
    return tuple(dict.fromkeys(queries))


def queries_for_candidate(candidate: CheapScanCandidate) -> EscalationQuerySet:
    return EscalationQuerySet(
        symbol=candidate.symbol,
        company_name=candidate.company_name,
        as_of_date=candidate.as_of_date,
        recommended_next_layer=candidate.recommended_next_layer,
        queries=queries_for_reason_codes(candidate.company_name, candidate.reason_codes),
    )


class EscalationQueryPlanner:
    """QueryPlanner-compatible adapter for FreeWebResearchRunner."""

    def __init__(self, candidate: CheapScanCandidate, sector: str | None = None) -> None:
        self._candidate = candidate
        self._sector = sector

    def plan(self, **kwargs) -> QueryPlan:
        queries = queries_for_candidate(self._candidate).queries
        specs = tuple(
            QuerySpec(
                group="deep_research" if self._candidate.recommended_next_layer == RecommendedNextLayer.DEEP_RESEARCH else "event_search",
                query=query,
                priority=10 + index,
                company_name=self._candidate.company_name,
                symbol=self._candidate.symbol,
                sector=self._sector,
                market=Market.KR,
                as_of_date=self._candidate.as_of_date,
            )
            for index, query in enumerate(queries)
        )
        return QueryPlan(
            company_name=self._candidate.company_name,
            symbol=self._candidate.symbol,
            sector=self._sector,
            market=Market.KR,
            as_of_date=self._candidate.as_of_date,
            queries=specs,
        )


__all__ = [
    "EscalationQueryPlanner",
    "EscalationQuerySet",
    "NEGATIVE_REASON_QUERY_TEMPLATES",
    "REASON_CODE_QUERY_TEMPLATES",
    "queries_for_candidate",
    "queries_for_reason_codes",
]
