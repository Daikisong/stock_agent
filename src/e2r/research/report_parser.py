"""Regex-based broker research report parser.

The parser consumes already extracted PDF text or local ``.txt`` fixtures. It
does not download PDFs and it never fills fields that are not present in text or
metadata.
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Any, Mapping

from e2r.models import Evidence, Market, ResearchReport, SourceTier
from e2r.research.one_off_context import has_one_off_shortage_context
from e2r.sources.source_errors import date_value, float_or_none, market_value, text_or_none, tuple_value


@dataclass(frozen=True)
class ReportParseResult:
    """Parsed report object, evidence object, and normalized field map."""

    report: ResearchReport
    evidence: Evidence
    parsed_fields: Mapping[str, Any]


def parse_research_report_file(
    path: str | Path,
    *,
    symbol: str,
    market: Market = Market.KR,
    metadata: Mapping[str, Any] | None = None,
) -> ReportParseResult:
    text = Path(path).read_text(encoding="utf-8")
    return parse_research_report_text(symbol=symbol, market=market, text=text, metadata=metadata)


def parse_research_report_text(
    *,
    symbol: str,
    market: Market = Market.KR,
    text: str,
    metadata: Mapping[str, Any] | None = None,
) -> ReportParseResult:
    metadata = dict(metadata or {})
    report_date = _report_date(text, metadata)
    as_of_date = date_value(metadata.get("as_of_date") or report_date)
    broker = str(metadata.get("broker") or _line_value(text, ("증권사", "Broker", "발행처")) or "UnknownBroker")
    analyst = text_or_none(metadata.get("analyst") or _line_value(text, ("애널리스트", "Analyst")))
    title = str(metadata.get("title") or _line_value(text, ("제목", "Title")) or _first_heading(text) or "Research report")

    parse_context = _parse_context_text(text=text, metadata=metadata, title=title)
    parsed = _extract_fields(parse_context)
    for key in (
        "current_price",
        "target_price",
        "target_revision_pct",
        "upside_pct",
        "fifty_two_week_high",
        "fifty_two_week_low",
        "one_month_return",
        "three_month_return",
        "twelve_month_return",
        "fy1_sales",
        "fy1_op",
        "fy1_eps",
        "fy2_sales",
        "fy2_op",
        "fy2_eps",
        "fy3_sales",
        "fy3_op",
        "fy3_eps",
        "est_per",
        "est_pbr",
        "roe",
        "opm",
        "backlog",
        "new_orders",
        "order_backlog_to_sales",
        "capa_increase_pct",
        "export_ratio",
        "us_revenue_ratio",
        "target_multiple_before",
        "target_multiple_after",
    ):
        if metadata.get(key) not in (None, ""):
            parsed.setdefault(key, float_or_none(metadata.get(key)))
    for key in ("asp_increase_mentioned", "lead_time_mentioned", "shortage_mentioned"):
        if metadata.get(key) not in (None, ""):
            parsed.setdefault(key, bool(metadata[key]))
    _drop_invalid_non_negative_fields(parsed)

    investment_points = tuple_value(metadata.get("investment_points")) or _points_after(parse_context, ("투자포인트", "투자 포인트", "Investment points"))
    risk_points = tuple_value(metadata.get("risk_points")) or _points_after(parse_context, ("리스크", "Risk"))
    parsed["parser_confidence"] = _confidence(parsed, parse_context)

    report = ResearchReport(
        symbol=symbol,
        publish_date=report_date,
        broker=broker,
        title=title,
        as_of_date=as_of_date,
        analyst=analyst,
        current_price=parsed.get("current_price"),
        target_price=parsed.get("target_price"),
        rating=text_or_none(metadata.get("rating") or _line_value(text, ("투자의견", "Rating"))),
        target_revision_pct=parsed.get("target_revision_pct"),
        target_multiple_before=parsed.get("target_multiple_before"),
        target_multiple_after=parsed.get("target_multiple_after"),
        fy1_sales=parsed.get("fy1_sales"),
        fy1_op=parsed.get("fy1_op"),
        fy1_eps=parsed.get("fy1_eps"),
        fy2_sales=parsed.get("fy2_sales"),
        fy2_op=parsed.get("fy2_op"),
        fy2_eps=parsed.get("fy2_eps"),
        fy3_sales=parsed.get("fy3_sales"),
        fy3_op=parsed.get("fy3_op"),
        fy3_eps=parsed.get("fy3_eps"),
        est_per=parsed.get("est_per"),
        est_pbr=parsed.get("est_pbr"),
        upside_pct=parsed.get("upside_pct"),
        fifty_two_week_high=parsed.get("fifty_two_week_high"),
        fifty_two_week_low=parsed.get("fifty_two_week_low"),
        one_month_return=parsed.get("one_month_return"),
        three_month_return=parsed.get("three_month_return"),
        twelve_month_return=parsed.get("twelve_month_return"),
        roe=parsed.get("roe"),
        opm=parsed.get("opm"),
        backlog=parsed.get("backlog"),
        new_orders=parsed.get("new_orders"),
        order_backlog_to_sales=parsed.get("order_backlog_to_sales"),
        capa_increase_pct=parsed.get("capa_increase_pct"),
        export_ratio=parsed.get("export_ratio"),
        us_revenue_ratio=parsed.get("us_revenue_ratio"),
        asp_increase_mentioned=bool(parsed.get("asp_increase_mentioned")),
        lead_time_mentioned=bool(parsed.get("lead_time_mentioned")),
        shortage_mentioned=bool(parsed.get("shortage_mentioned")),
        investment_points=investment_points,
        risk_points=risk_points,
        raw_text=text,
        parsed_fields=parsed,
    )
    published_at = datetime(report_date.year, report_date.month, report_date.day, 8, 0)
    evidence = Evidence(
        evidence_id=f"research:{symbol}:{report_date.isoformat()}:{_stable_id(title)}",
        source_type="research_report",
        source_name=broker,
        source_tier=SourceTier.TIER_1,
        published_at=published_at,
        observed_at=published_at,
        available_at=published_at,
        as_of_date=as_of_date,
        market=market_value(metadata.get("market"), market),
        symbol=symbol,
        title=title,
        url_or_identifier=text_or_none(metadata.get("url")),
        excerpt_or_value=parse_context[:240],
        parsed_fields=parsed,
        confidence=parsed["parser_confidence"],
    )
    return ReportParseResult(report=report, evidence=evidence, parsed_fields=parsed)


def _extract_fields(text: str) -> dict[str, Any]:
    fields: dict[str, Any] = {}
    aliases = {
        "current_price": ("현재가", "현재주가", "Current price"),
        "target_price": ("목표주가", "Target price"),
        "target_revision_pct": ("목표주가 상향", "Target revision"),
        "upside_pct": ("상승여력", "Upside"),
        "fifty_two_week_high": ("52주 최고", "52-week high"),
        "fifty_two_week_low": ("52주 최저", "52-week low"),
        "one_month_return": ("1개월 수익률", "1M return"),
        "three_month_return": ("3개월 수익률", "3M return"),
        "twelve_month_return": ("12개월 수익률", "12M return"),
        "est_per": ("PER", "Est PER"),
        "est_pbr": ("PBR", "Est PBR"),
        "roe": ("ROE",),
        "opm": ("OPM", "영업이익률"),
        "backlog": ("수주잔고", "Backlog"),
        "new_orders": ("신규수주", "New orders"),
        "order_backlog_to_sales": ("수주잔고/매출", "order backlog to sales"),
        "contract_amount_to_prior_sales": ("계약금액/매출", "계약 매출액 대비", "장기계약 매출액 대비", "매출액 대비"),
        "contract_duration_months": ("계약기간", "계약 기간", "duration months"),
        "capa_increase_pct": ("CAPA 증가율", "CAPA 증설", "생산능력 증가"),
        "export_ratio": ("수출 비중", "Export ratio"),
        "export_growth_pct": ("수출 증가율", "수출 성장률", "Export growth"),
        "us_revenue_ratio": ("미국향 매출 비중", "북미 매출 비중", "US revenue ratio"),
        "asp_yoy_pct": ("ASP 상승률", "판가 상승률", "가격 상승률"),
        "lead_time_months": ("리드타임", "lead time"),
        "opm_expansion_pctp": ("OPM 개선폭", "마진 개선폭"),
        "arr_growth_pct": ("ARR 성장률", "ARR growth"),
        "nrr": ("NRR", "net revenue retention"),
        "k_ics_ratio": ("K-ICS", "KICS", "지급여력비율"),
        "target_multiple_before": ("기존 멀티플", "target multiple before"),
        "target_multiple_after": ("상향 멀티플", "target multiple after"),
    }
    percent_fields = {
        "target_revision_pct",
        "upside_pct",
        "one_month_return",
        "three_month_return",
        "twelve_month_return",
        "roe",
        "opm",
        "order_backlog_to_sales",
        "contract_amount_to_prior_sales",
        "capa_increase_pct",
        "export_ratio",
        "export_growth_pct",
        "us_revenue_ratio",
        "asp_yoy_pct",
        "opm_expansion_pctp",
        "arr_growth_pct",
        "nrr",
        "k_ics_ratio",
    }
    for key, labels in aliases.items():
        value = _number_after(text, labels, percent=key in percent_fields)
        if value is not None:
            if key == "contract_amount_to_prior_sales" and value > 2:
                value /= 100.0
            fields[key] = value

    for index, year_key in enumerate(("fy1", "fy2", "fy3"), start=1):
        year_match = re.search(
            rf"FY{index}|20[0-9]{{2}}E",
            text,
            re.IGNORECASE,
        )
        if not year_match and index > 1:
            continue
        for output, labels in (
            (f"{year_key}_sales", ("매출액", "Sales")),
            (f"{year_key}_op", ("영업이익", "OP")),
            (f"{year_key}_eps", ("EPS",)),
        ):
            value = _number_in_year_line(text, index, labels)
            if value is not None:
                fields[output] = value

    _add_forward_estimate_fields(text, fields)
    _add_target_price_fields(text, fields)

    if "ASP" in text or "판가" in text:
        fields["asp_increase_mentioned"] = any(token in text for token in ("ASP 상승", "판가 상승", "가격 상승", "ASP 개선"))
    if any(token in text for token in ("ASP 상승", "판가 상승", "가격 상승", "ASP 개선", "판가 개선")):
        fields["pricing_power_confirmed"] = True
        fields["pricing_power_mentioned"] = True
    if "리드타임" in text or "lead time" in text.lower():
        fields["lead_time_mentioned"] = True
    if any(token in text for token in ("리드타임 장기화", "CAPA 부족", "생산능력 부족", "공급부족")):
        fields["capacity_constraint"] = True
    if "리드타임 장기화" in text:
        fields["lead_time_extended"] = True
    if "공급부족" in text or "공급 부족" in text or "shortage" in text.lower():
        fields["shortage_mentioned"] = True
        fields["supply_shortage_mentioned"] = True
    if "구조적 공급부족" in text or "structural shortage" in text.lower():
        fields["shortage_type"] = "structural"
        fields["structural_shortage_mentioned"] = True
    lowered = text.lower()
    if has_one_off_shortage_context(text):
        fields["shortage_type"] = "one_off"
        fields["one_off_shortage"] = True
        fields["pandemic_demand_spike"] = True
        fields["temporary_shortage"] = True
        fields["one_off_shortage_risk"] = 90.0
    if "사상 최대 수주잔고" in text or ("수주잔고" in text and "사상 최대" in text):
        fields["record_backlog"] = True
        fields["backlog_record_high"] = True
    _add_qualitative_e2r_fields(text, fields)
    return fields


_NON_NEGATIVE_REPORT_FIELDS = frozenset(
    (
        "current_price",
        "target_price",
        "target_multiple_before",
        "target_multiple_after",
        "fy1_sales",
        "fy2_sales",
        "fy3_sales",
        "est_per",
        "est_pbr",
        "fifty_two_week_high",
        "fifty_two_week_low",
        "backlog",
        "new_orders",
        "order_backlog_to_sales",
    )
)


def _drop_invalid_non_negative_fields(fields: dict[str, Any]) -> None:
    dropped: list[str] = []
    for key in _NON_NEGATIVE_REPORT_FIELDS:
        value = fields.get(key)
        if isinstance(value, (int, float)) and value < 0:
            fields.pop(key, None)
            dropped.append(key)
    if dropped:
        fields["invalid_non_negative_fields"] = tuple(sorted(dropped))


def _parse_context_text(*, text: str, metadata: Mapping[str, Any], title: str) -> str:
    parts = (
        title,
        text_or_none(metadata.get("snippet")),
        text_or_none(metadata.get("description")),
        text,
    )
    deduped: list[str] = []
    seen: set[str] = set()
    for part in parts:
        cleaned = str(part or "").strip()
        if not cleaned or cleaned in seen:
            continue
        seen.add(cleaned)
        deduped.append(cleaned)
    return "\n".join(deduped)


def _add_forward_estimate_fields(text: str, fields: dict[str, Any]) -> None:
    lowered = text.lower()
    if not any(
        token in lowered
        for token in (
            "예상",
            "전망",
            "전망치",
            "추정",
            "추정치",
            "가이던스",
            "forecast",
            "estimate",
            "expected",
            "guidance",
        )
    ):
        return

    forward_found = False
    if _estimate_upgrade_mentioned(text):
        fields["estimate_upgrade_mentioned"] = True
    if _has_forward_estimate_amount(text, ("영업이익", "영업익", "OP", "operating profit")):
        forward_found = True
        fields["forward_estimate_present"] = True
        value = _forward_money_after(text, ("영업이익", "영업익", "OP", "operating profit"))
        if value is not None:
            fields.setdefault("fy1_op", value)
            fields.setdefault("forward_op_estimate", value)
    if _has_forward_estimate_amount(text, ("매출액", "매출", "Sales", "Revenue")):
        forward_found = True
        fields["forward_estimate_present"] = True
        value = _forward_money_after(text, ("매출액", "매출", "Sales", "Revenue"))
        if value is not None:
            fields.setdefault("fy1_sales", value)
            fields.setdefault("forward_sales_estimate", value)
    eps = _forward_eps_after(text)
    if eps is not None:
        forward_found = True
        fields["forward_estimate_present"] = True
        fields.setdefault("fy1_eps", eps)
        fields.setdefault("forward_eps_estimate", eps)
    fiscal_year = _forward_fiscal_year(text) if forward_found else None
    if fiscal_year is not None:
        fields.setdefault("fy1_fiscal_year", fiscal_year)


def _add_target_price_fields(text: str, fields: dict[str, Any]) -> None:
    target_price = _target_price_value(text)
    if target_price is not None:
        fields.setdefault("target_price", target_price)
    revision_pct = _target_price_revision_pct(text)
    if revision_pct is not None:
        fields.setdefault("target_revision_pct", revision_pct)
        fields.setdefault("target_price_revision_pct", revision_pct)
        fields["target_price_upgrade_mentioned"] = True
    elif _target_price_upgrade_mentioned(text):
        fields["target_price_upgrade_mentioned"] = True


def _add_qualitative_e2r_fields(text: str, fields: dict[str, Any]) -> None:
    lowered = text.lower()
    hbm_context = "hbm" in lowered or "고대역폭메모리" in text
    if hbm_context:
        fields["hbm_context_mentioned"] = True
    if any(token in text for token in ("수출 비중 확대", "수출 확대", "수출 증가", "해외 매출 확대")):
        fields["export_channel_expansion"] = True
        fields["export_growth_mentioned"] = True
    if any(token in text for token in ("해외 채널 확대", "해외 채널 확장", "북미 채널", "미국 채널")):
        fields["overseas_channel_expansion"] = True
        fields["channel_expansion"] = True
        fields["brand_channel_expansion"] = True
    if any(
        token in text
        for token in (
            "글로벌 유통망 확대",
            "글로벌 유통 확대",
            "플랫폼 유통 확대",
            "대형 유통 채널",
            "대형 리테일 채널",
            "입점 확대",
        )
    ) or any(
        token in lowered
        for token in (
            "global distribution",
            "distribution scale",
            "platform distribution",
            "retail channel expansion",
            "major retail channel",
        )
    ):
        fields["platform_distribution_scale"] = True
        fields["brand_channel_expansion"] = True
        fields["channel_expansion"] = True
    if any(token in text for token in ("브랜드 고객", "주요 고객 다변화", "고객 다변화", "앵커 고객")) or any(
        token in lowered for token in ("brand customer", "customer diversification", "anchor customer", "named customer")
    ):
        fields["brand_customer_diversification"] = True
        fields["named_customer_quality"] = True
    if any(token in text for token in ("반복 수요", "재구매", "리오더", "recurring demand", "repeat purchase")):
        fields["recurring_consumer_demand"] = True
    if any(token in text for token in ("재주문", "리오더", "repeat order", "reorder")):
        fields["repeat_order_confirmed"] = True
        fields["channel_reorder_confirmed"] = True
        fields["recurring_consumer_demand"] = True
    if any(token in text for token in ("셀스루", "sell-through", "sell through", "판매 회전", "재고 소진")):
        fields["sell_through_confirmed"] = True
        fields["recurring_consumer_demand"] = True
    if any(token in text for token in ("재고 부담", "재고 과잉", "inventory overhang", "inventory spike")):
        fields["inventory_overhang"] = True
        fields["receivables_inventory_spike"] = True
    if "불닭" in text and any(token in text for token in ("수출", "채널", "미국", "해외")):
        fields["recurring_consumer_demand"] = True
        fields["export_channel_expansion"] = True
    if any(token in text for token in ("고마진 믹스", "믹스 개선", "수익성 높은", "OPM 개선", "마진 개선")):
        fields["high_margin_mix_improvement"] = True
    if hbm_context and (
        any(token in text for token in ("수요 증가", "수요 확대", "수요 강세", "수요 폭증", "수요 우위", "주문 확대", "고객 수요"))
        or any(token in lowered for token in ("demand growth", "strong demand", "customer demand"))
    ):
        fields["hbm_demand_mentioned"] = True
    if any(token in text for token in ("메모리 가격 상승", "DRAM 가격 상승", "D램 가격 상승", "NAND 가격 상승", "낸드 가격 상승")):
        fields["memory_price_increase_mentioned"] = True
        fields["pricing_power_mentioned"] = True
    if hbm_context and (
        any(token in text for token in ("HBM 가격 상승", "HBM 가격 인상", "가격 인상", "가격 상승", "ASP 상승", "평균판매가격"))
        or any(token in lowered for token in ("hbm price", "asp"))
    ):
        fields["memory_price_increase_mentioned"] = True
        fields["pricing_power_mentioned"] = True
        fields["asp_increase_mentioned"] = True
    if any(token in text for token in ("공급조절", "감산", "공급 discipline", "supply discipline")):
        fields["supply_discipline_mentioned"] = True
    semiconductor_cycle_context = hbm_context or any(
        token in lowered for token in ("memory", "dram", "nand", "semiconductor", "advanced packaging")
    ) or any(token in text for token in ("메모리", "반도체", "D램", "디램", "낸드", "패키징"))
    demand_cycle_visible = any(
        token in text
        for token in (
            "수요 증가",
            "수요 확대",
            "수요 강세",
            "수요 회복",
            "업황 개선",
            "주문 회복",
        )
    ) or any(token in lowered for token in ("demand growth", "strong demand", "demand recovery", "cycle recovery"))
    price_cycle_visible = bool(fields.get("memory_price_increase_mentioned") or fields.get("pricing_power_mentioned"))
    supply_cycle_visible = bool(fields.get("supply_discipline_mentioned")) or any(
        token in lowered for token in ("supply discipline", "capacity constraint", "bottleneck")
    )
    if semiconductor_cycle_context and demand_cycle_visible and (price_cycle_visible or supply_cycle_visible):
        fields["cycle_demand_visibility"] = True
        fields["end_market_demand_visibility"] = True
    if semiconductor_cycle_context and demand_cycle_visible and price_cycle_visible and supply_cycle_visible:
        fields["supply_demand_tightness"] = True
    if fields.get("cycle_demand_visibility") and any(
        token in text for token in ("추정치 상향", "목표주가 상향", "EPS 상향", "영업이익 상향")
    ):
        fields["cycle_to_revenue_bridge"] = True
    if any(token in text for token in ("선주문", "preorder", "allocation", "우선 배정")):
        fields["customer_preorder_or_allocation"] = True
    if any(token in text for token in ("고객사 확정", "확정 고객", "주요 고객", "고객사 배정", "확정 물량")) or any(
        token in lowered for token in ("confirmed customer", "named customer", "anchor customer", "customer allocation")
    ):
        fields["named_customer_quality"] = True
        fields["customer_preorder_or_allocation"] = True
    if any(token in text for token in ("공급계약", "납품계약", "프레임워크 계약", "마스터 공급계약")) or any(
        token in lowered
        for token in ("supply agreement", "supply contract", "customer contract", "framework agreement", "master supply agreement")
    ):
        fields["customer_contract_visible"] = True
        fields["supply_agreement_visible"] = True
    if any(token in text for token in ("선수금", "선급금")) or any(
        token in lowered for token in ("advance payment", "prepayment", "customer prepayment")
    ):
        fields["prepayment_exists"] = True
        fields["customer_prepayment"] = True
    if any(token in text for token in ("취소불가", "취소 불가", "해지 불가", "해지불가")) or any(
        token in lowered for token in ("non-cancellable", "non cancellable", "noncancelable")
    ):
        fields["non_cancellable"] = True
    if any(token in text for token in ("최소 구매 보장", "최소 물량 보장", "의무 구매")) or any(
        token in lowered for token in ("take-or-pay", "take or pay", "minimum purchase commitment")
    ):
        fields["take_or_pay"] = True
        fields["customer_preorder_or_allocation"] = True
    if any(token in text for token in ("최소 매출 보장", "최소매출 보장", "최소 판매 보장")) or any(
        token in lowered for token in ("minimum revenue guarantee", "minimum sales guarantee")
    ):
        fields["minimum_revenue_guarantee"] = True
        fields["minimum_sales_guarantee"] = True
        fields["revenue_visibility_contract"] = True
    if any(token in text for token in ("생산능력 배정", "생산 슬롯 확정", "생산 슬롯 예약", "물량 예약")) or any(
        token in lowered for token in ("capacity allocation", "capacity booked", "booked out", "slot reservation")
    ):
        fields["capacity_precommitted"] = True
        fields["booked_out_capacity"] = True
        fields["order_slot_locked"] = True
    if hbm_context and (
        any(
            token in text
            for token in (
                "완판",
                "전량 판매",
                "전량판매",
                "물량 확보",
                "물량 선점",
                "물량 배정",
                "고객 수요 대비 공급",
                "공급 충족률",
                "공급 부족",
                "공급부족",
                "중장기 물량 확보",
                "장기 물량 확보",
            )
        )
        or any(token in lowered for token in ("sold out", "pre-sold", "sold-out", "capacity allocation", "supply allocation"))
    ):
        fields["customer_preorder_or_allocation"] = True
        fields["capacity_precommitted"] = True
        fields["hbm_capacity_pre_sold"] = True
    if hbm_context and (
        any(
            token in text
            for token in (
                "공급 부족",
                "공급부족",
                "공급이 제한",
                "공급 확대가 제한",
                "공급 충족률",
                "수요 대비 공급",
                "타이트",
                "신규 팹 증설에 시간",
                "단기간 내 공급 확대",
                "생산능력 부족",
            )
        )
        or any(token in lowered for token in ("supply shortage", "tight supply", "capacity constraint"))
    ):
        fields["supply_shortage_mentioned"] = True
        fields["capacity_constraint"] = True
        fields["capa_shortage"] = True
        fields["hbm_capacity_constraint"] = True
    if hbm_context and (
        any(token in text for token in ("CAPA 제약", "CAPA 병목", "패키징 병목", "첨단 패키징 병목"))
        or any(token in lowered for token in ("advanced packaging bottleneck", "packaging bottleneck"))
    ):
        fields["capacity_constraint"] = True
        fields["hbm_capacity_constraint"] = True
        fields["advanced_packaging_bottleneck"] = True
        fields["supply_demand_tightness"] = True
    if any(token in text for token in ("정부 고객", "정부향", "폴란드", "방산")):
        fields["government_customer"] = True
    if any(token in text for token in ("장기계약", "장기 공급계약", "장기공급계약", "다년 계약", "multi-year")):
        fields["multi_year_contract"] = True
        if hbm_context and fields.get("customer_preorder_or_allocation"):
            fields["revenue_visibility_contract"] = True
    if fields.get("multi_year_contract") and any(
        fields.get(key)
        for key in (
            "customer_contract_visible",
            "prepayment_exists",
            "non_cancellable",
            "take_or_pay",
            "minimum_revenue_guarantee",
            "customer_preorder_or_allocation",
        )
    ):
        fields["revenue_visibility_contract"] = True
    if any(token in text for token in ("사상 최대 수주잔고", "최대 수주잔고", "수주잔고 사상 최대")):
        fields["backlog_record_high"] = True
        fields["record_backlog"] = True
    if any(token in text for token in ("납기 일정", "인도 일정", "출하 일정")) or "delivery schedule" in lowered:
        fields["delivery_schedule"] = True
    if any(token in text for token in ("수주잔고 매출 전환", "수주 매출 전환", "매출 전환 경로", "출하 매출 전환")) or any(
        token in lowered for token in ("order-to-revenue", "order to revenue", "revenue recognition path", "call-off")
    ):
        fields["order_to_revenue_bridge"] = True
    if any(token in lowered for token in ("book-to-bill", "book to bill")):
        fields["book_to_bill_visible"] = True
    if any(token in text for token in ("장비 수주 회복", "장비 주문 회복", "수주 회복")) or "equipment order recovery" in lowered:
        fields["equipment_order_recovery"] = True
        fields["order_to_revenue_bridge"] = True
    if any(token in text for token in ("재고 정상화", "재고 사이클 회복")) or any(
        token in lowered for token in ("inventory normalization", "inventory cycle repair")
    ):
        fields["inventory_cycle_repair"] = True
    if any(token in text for token in ("마진 가시성", "마진 전환", "원가 전가")) or any(
        token in lowered for token in ("margin bridge", "margin visibility", "operating leverage")
    ):
        fields["margin_bridge_visible"] = True
        if "operating leverage" in lowered:
            fields["operating_leverage_visible"] = True
    if any(token in text for token in ("고객 인증 지연", "퀄 지연", "인증 지연")) or any(
        token in lowered for token in ("qualification lag", "qualification delay")
    ):
        fields["qualification_lag_risk"] = True
    if any(token in text for token in ("주가만 상승", "가격만 상승", "테마만 부각")) or any(
        token in lowered for token in ("price-only", "price only", "theme hype")
    ):
        fields["price_only_blowoff"] = True
    if any(token in text for token in ("매출 연결 없음", "매출로 연결되지", "현금흐름 연결 없음")) or any(
        token in lowered for token in ("without revenue", "no revenue bridge", "missing cashflow bridge")
    ):
        fields["missing_cashflow_bridge"] = True
        fields["theme_hype_without_revenue"] = True
    if any(token in text for token in ("출처 불일치", "근거 상충", "자료 신뢰도 낮음")) or any(
        token in lowered for token in ("source conflict", "source quality conflict", "low source quality")
    ):
        fields["source_quality_conflict"] = True
        fields["evidence_source_quality_issue"] = True
    if any(token in text for token in ("자사주 소각", "자기주식 소각", "treasury share cancellation", "share cancellation")):
        fields["treasury_share_cancellation"] = True
        fields["buyback_executed"] = True
        fields["capital_return_execution"] = True
    if any(token in text for token in ("자사주 매입", "자사주 취득", "buyback")):
        fields["buyback_announced"] = True
    if any(token in text for token in ("배당 확대", "배당성향 확대", "주주환원 확대", "shareholder return", "dividend growth")):
        fields["dividend_visibility"] = True
        fields["shareholder_return_execution"] = True
    if any(token in text for token in ("신용비용 안정", "credit cost 안정", "NPL 안정", "부실채권 안정")):
        fields["credit_cost_quality"] = True
    if any(token in text for token in ("밸류업 기대", "value-up 기대", "value up 기대")) and not fields.get("capital_return_execution"):
        fields["capital_return_unconfirmed"] = True
    if any(token in text for token in ("CSM 증가", "CSM 성장", "계약서비스마진 증가", "계약서비스마진 성장")):
        fields["csm_growth_visible"] = True
    if any(token in text for token in ("준비금 안정", "준비금 충분", "reserve quality", "reserve adequacy")):
        fields["reserve_quality_visible"] = True
    if any(token in text for token in ("손해율 개선", "손해율 안정", "loss ratio improvement", "loss ratio stable")):
        fields["loss_ratio_quality"] = True
    if any(token in text for token in ("보험료율 인상 기대", "rate cycle 기대")) and not any(
        fields.get(key) for key in ("csm_growth_visible", "reserve_quality_visible", "loss_ratio_quality")
    ):
        fields["insurance_rate_cycle_beta_only"] = True
        fields["reserve_quality_unconfirmed"] = True
    if any(token in text for token in ("FDA 승인", "품목허가", "허가 승인", "regulatory approval", "approved by FDA")):
        fields["regulatory_approval_confirmed"] = True
    if any(token in text for token in ("상업화", "출시", "매출 전환", "approval-to-revenue", "approval to revenue")) and fields.get(
        "regulatory_approval_confirmed"
    ):
        fields["approval_to_revenue_bridge"] = True
    if any(token in text for token in ("로열티", "royalty", "마일스톤", "milestone payment")):
        fields["royalty_route"] = True
        fields["partner_economics_visible"] = True
    if any(token in text for token in ("보험급여", "급여 등재", "reimbursement")):
        fields["reimbursement_confirmed"] = True
    if any(token in text for token in ("PDUFA 예정", "승인 기대", "결과 대기", "approval pending", "binary event")):
        fields["binary_event_unresolved"] = True
        fields["approval_not_confirmed"] = True
    if any(token in text for token in ("ARR 증가", "ARR 성장", "ARR growth", "recurring revenue growth")):
        fields["arr_growth_visible"] = True
    if any(token in text for token in ("갱신율", "renewal", "retention", "NRR", "churn low", "churn 감소")):
        fields["retention_or_renewal"] = True
        fields["contract_renewal_visible"] = True
    if any(token in text for token in ("seat expansion", "좌석 확장", "사용자 확장")):
        fields["seat_expansion_visible"] = True
    if any(token in text for token in ("반복 매출 마진", "SaaS 마진", "cloud margin", "recurring margin")):
        fields["recurring_margin_leverage"] = True
    if any(token in text for token in ("정치 테마", "대선 테마", "political theme")):
        fields["political_theme_risk"] = True
    if any(token in text for token in ("정책 수혜", "보조금 수혜", "policy beneficiary", "subsidy capture")):
        fields["policy_to_company_cash_route"] = True
    if any(token in text for token in ("정책 기대감", "policy headline")) and not fields.get("policy_to_company_cash_route"):
        fields["policy_headline_only"] = True
    if any(token in text for token in ("정책 승인", "규제 승인", "인허가 확인", "정부 승인")) or any(
        token in lowered for token in ("policy confirmed", "regulatory confirmed", "regulatory approval confirmed")
    ):
        fields["policy_or_regulatory_confirmed"] = True
    if any(token in text for token in ("프로젝트 수주", "프로젝트 선정", "사업자 선정", "낙찰")) or any(
        token in lowered for token in ("project award", "project awarded", "selected bidder")
    ):
        fields["project_award_confirmed"] = True
    if any(token in text for token in ("허가 지연", "인허가 지연", "법적 지연", "소송 지연")) or any(
        token in lowered for token in ("permit delay", "legal delay", "permitting delay")
    ):
        fields["permit_or_legal_delay"] = True
    if any(token in text for token in ("회사 현금흐름 연결", "현금흐름 연결", "직접 매출 연결")) or any(
        token in lowered for token in ("direct company cash route", "company cash route", "direct revenue route")
    ):
        fields["direct_company_cash_route"] = True
        fields["policy_to_company_cash_route"] = True
    if any(token in text for token in ("스프레드 확대", "마진 스프레드 확대")) or "spread expansion" in lowered:
        fields["spread_expansion"] = True
        fields["margin_bridge_visible"] = True
    if any(token in text for token in ("ex-credit 마진", "세액공제 제외 마진")) or "ex-credit margin" in lowered:
        fields["ex_credit_margin"] = True
        fields["margin_bridge_visible"] = True
    if any(token in text for token in ("원재료 비용 리스크", "원재료 가격 부담")) or any(
        token in lowered for token in ("raw material cost risk", "raw material price risk")
    ):
        fields["raw_material_cost_risk"] = True
    if any(token in text for token in ("가동률 상승", "가동률 개선", "utilization rate")):
        fields["utilization_rate"] = True
    if any(token in text for token in ("재고 사이클", "inventory cycle")):
        fields["inventory_cycle"] = True
    if any(token in text for token in ("재고 급증", "재고 증가", "inventory spike")):
        fields["inventory_spike"] = True
        fields["receivables_inventory_spike"] = True
    if any(token in text for token in ("데이터센터 고객", "datacenter customer", "data center customer")):
        fields["datacenter_customer"] = True
        fields["data_center_contract"] = True
    if any(token in text for token in ("HBM 고객 주문", "HBM 고객 수주", "hbm customer order")):
        fields["hbm_customer_order"] = True
        fields["customer_preorder_or_allocation"] = True
    if any(token in text for token in ("상대강도", "relative strength")):
        fields["relative_strength_score"] = True
    if any(token in text for token in ("고객 인증 완료", "퀄 통과", "qualification confirmed")):
        fields["qualification_confirmed"] = True
    if any(token in text for token in ("테스트 소켓 수요", "socket demand", "test socket demand")):
        fields["socket_or_test_demand_visible"] = True
    if any(token in text for token in ("고객 품질 확인", "우량 고객", "customer quality visible")):
        fields["customer_quality_visible"] = True
    if any(token in text for token in ("물량 가시성", "volume visibility")):
        fields["volume_visibility"] = True
    if any(token in text for token in ("판매량 증가", "출하량 증가", "volume growth")):
        fields["volume_growth_visible"] = True
    if any(token in text for token in ("JV 가동률", "합작공장 가동률", "jv utilization")):
        fields["jv_utilization"] = True
    if any(token in text for token in ("밸류에이션 과열", "valuation overheat")):
        fields["valuation_overheat"] = True
    if any(token in text for token in ("논리 훼손 확인", "투자논리 훼손", "thesis break")):
        fields["thesis_break_confirmed"] = True
    if any(token in text for token in ("감사 리스크", "회계 신뢰 리스크", "accounting trust risk")):
        fields["accounting_trust_risk"] = True
        fields["auditor_or_disclosure_risk"] = True
    if any(token in text for token in ("재무제표 재작성", "정정 리스크", "restatement risk")):
        fields["restatement_risk"] = True
    if any(token in text for token in ("주식수 증가", "희석 리스크", "share count drift")):
        fields["share_count_drift"] = True
    if any(token in text for token in ("고 MAE", "high mae")):
        fields["high_mae_history"] = True
    if any(token in text for token in ("유동성 리스크", "초소형주 리스크", "liquidity risk", "microcap risk")) and not _risk_mitigated_context(
        text,
        lowered,
    ):
        fields["liquidity_or_microcap_risk"] = True
    if any(token in text for token in ("실행 리스크", "execution risk")):
        fields["execution_risk_score"] = True
    if any(token in text for token in ("포지셔닝 반전", "positioning reversal")):
        fields["positioning_reversal_risk"] = True
    if any(token in text for token in ("EV 수요 둔화", "전기차 수요 둔화", "ev demand slowdown")):
        fields["ev_demand_slowdown"] = True
    if any(token in text for token in ("가격 인하 리스크", "price cut risk")):
        fields["price_cut_risk"] = True
    if any(token in text for token in ("정책 후퇴", "policy reversal")):
        fields["policy_reversal_risk"] = True
    if any(token in text for token in ("규제 리스크", "regulatory risk")):
        fields["regulatory_risk"] = True
    if any(token in text for token in ("테마 토큰 리스크", "token hype risk", "theme hype risk")):
        fields["token_or_theme_hype_risk"] = True
    if any(token in text for token in ("자금조달 비용 리스크", "funding cost risk")):
        fields["funding_cost_risk"] = True
    if any(token in text for token in ("증거 품질", "출처 품질", "evidence source quality")):
        fields["evidence_source_quality"] = True
    if any(token in text for token in ("오프테이크 계약", "offtake contract")):
        fields["offtake_contract"] = True
        fields["customer_contract_visible"] = True
    if any(token in text for token in ("공급부족", "공급 부족", "supply shortage")):
        fields["supply_shortage"] = True
    if any(token in text for token in ("정책 공급 지원", "policy supply support")):
        fields["policy_supply_support"] = True
    if any(token in text for token in ("허가 상태", "permit status")):
        fields["permit_status"] = True
    if any(token in text for token in ("AMPC", "세액공제 수혜", "subsidy capture")):
        fields["ampc_or_subsidy_capture"] = True
        fields["subsidy_capture_visible"] = True
    if any(token in text for token in ("이행 일정", "실행 일정", "implementation timeline")):
        fields["implementation_timeline"] = True
    if any(token in text for token in ("공개매수 확정", "tender offer confirmed")):
        fields["tender_offer_confirmed"] = True
    if any(token in text for token in ("소수주주 현금화 경로", "minority cash path")):
        fields["minority_cash_path"] = True
    if any(token in text for token in ("경영권 프리미엄 하단", "control premium floor")):
        fields["control_premium_floor"] = True
    if any(token in text for token in ("이벤트 스프레드 리스크", "event spread risk")):
        fields["event_spread_risk"] = True
    if any(token in text for token in ("PF 익스포저 축소", "pf exposure reduced")):
        fields["pf_exposure_reduced"] = True
    if any(token in text for token in ("재무구조 개선", "balance sheet repair")):
        fields["balance_sheet_repair"] = True
    if any(token in text for token in ("현금 회수 가시성", "cash collection visible")):
        fields["cash_collection_visible"] = True
    if any(token in text for token in ("분양률 가시성", "입주율 가시성", "occupancy visible", "presale visible")):
        fields["occupancy_or_presale_visible"] = True
    if any(token in text for token in ("ARPU 성장", "arpu growth")):
        fields["arpu_growth_pct"] = fields.get("arpu_growth_pct", 1.0)
    if any(token in text for token in ("광고 매출 성장", "ad revenue growth")):
        fields["ad_revenue_growth_pct"] = fields.get("ad_revenue_growth_pct", 1.0)

    if any(token in text for token in ("take rate 개선", "take-rate improvement", "take rate improvement")):
        fields["take_rate_improvement"] = True
    if any(token in text for token in ("IP 수익화", "ip monetization")):
        fields["ip_monetization_visible"] = True
    if any(token in text for token in ("글로벌 출시 전환", "global launch conversion")):
        fields["global_launch_conversion"] = True
    if any(token in text for token in ("반복 매출", "repeat revenue")):
        fields["repeat_revenue"] = True
    if any(token in text for token in ("사용자 유지", "user retention")):
        fields["user_retention"] = True
    if any(token in text for token in ("임상 질", "trial quality")):
        fields["trial_quality_visible"] = True
    if any(token in text for token in ("안전성 신호", "safety signal")):
        fields["safety_signal"] = True
    if any(token in text for token in ("현금 런웨이 리스크", "cash runway risk")):
        fields["cash_runway_risk"] = True
    if any(token in text for token in ("시술 건수 증가", "procedure volume growth")):
        fields["procedure_volume_growth"] = True
    if any(token in text for token in ("소모품 반복 매출", "consumable repeat revenue")):
        fields["consumable_repeat_revenue"] = True
    if any(token in text for token in ("매출총이익률 브릿지", "gross margin bridge")):
        fields["gross_margin_bridge"] = True
        fields["margin_bridge_visible"] = True


def _risk_mitigated_context(text: str, lowered: str) -> bool:
    return any(
        token in text
        for token in (
            "리스크 상대 우위",
            "리스크 관리",
            "리스크 완화",
            "리스크 축소",
            "리스크 해소",
            "상대 우위",
            "재무구조 개선",
            "현금 회수 가시성",
            "PF 익스포저 축소",
        )
    ) or any(
        token in lowered
        for token in (
            "risk monitored",
            "risk managed",
            "risk mitigated",
            "risk reduced",
            "risk resolved",
            "relative advantage",
            "balance sheet repair",
            "cash collection visible",
            "pf exposure reduced",
        )
    )


def _report_date(text: str, metadata: Mapping[str, Any]) -> date:
    if metadata.get("report_date") or metadata.get("publish_date"):
        return date_value(metadata.get("report_date") or metadata.get("publish_date"))
    match = re.search(r"(20[0-9]{2})[.\-/년]\s*([0-9]{1,2})[.\-/월]\s*([0-9]{1,2})", text)
    if match:
        return date(int(match.group(1)), int(match.group(2)), int(match.group(3)))
    return date.today()


def _line_value(text: str, labels: tuple[str, ...]) -> str | None:
    for label in labels:
        match = re.search(rf"{re.escape(label)}\s*[:：]?\s*(?P<value>[^\n]+)", text, re.IGNORECASE)
        if match:
            value = match.group("value").strip(" -\t")
            return value[:160] if value else None
    return None


def _first_heading(text: str) -> str | None:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped and len(stripped) <= 120:
            return stripped.strip("# ")
    return None


def _number_after(text: str, labels: tuple[str, ...], *, percent: bool = False) -> float | None:
    for label in labels:
        pattern = rf"{re.escape(label)}[^\n0-9\-]*(?P<number>-?[0-9][0-9,]*(?:\.[0-9]+)?)\s*(?P<unit>%|조원|조|억원|억|만원|원|배|x)?"
        match = re.search(pattern, text, re.IGNORECASE)
        if not match:
            continue
        value = float(match.group("number").replace(",", ""))
        unit = match.group("unit")
        if unit in {"조원", "조"}:
            value *= 1_000_000_000_000.0
        if unit in {"억원", "억"}:
            value *= 100_000_000.0
        if unit == "만원":
            value *= 10_000.0
        return value if percent or unit != "%" else value
    return None


def _number_in_year_line(text: str, fy_index: int, labels: tuple[str, ...]) -> float | None:
    year_markers = (f"FY{fy_index}", f"FY{fy_index}E")
    lines = [line for line in text.splitlines() if any(marker in line.upper() for marker in year_markers)]
    if not lines:
        years = re.findall(r"20[0-9]{2}E[^\n]+", text)
        if len(years) >= fy_index:
            lines = [years[fy_index - 1]]
    for line in lines:
        for label in labels:
            match = re.search(rf"{re.escape(label)}[^0-9\-]*(?P<number>-?[0-9][0-9,]*(?:\.[0-9]+)?)", line, re.IGNORECASE)
            if match:
                return float(match.group("number").replace(",", ""))
    return None


def _forward_fiscal_year(text: str) -> int | None:
    patterns = (
        r"(?<![a-z0-9])(?:[1-4]\s*q|q\s*[1-4])\s*'?(?P<year>[0-9]{2,4})(?![0-9])",
        r"(?<![a-z0-9])(?P<year>[0-9]{2,4})\s*(?:년|e)\s*(?:[1-4]\s*분기)?[^.\n]{0,40}(?:예상|전망|전망치|추정|추정치|가이던스)",
        r"(?:예상|전망|전망치|추정|추정치|가이던스)[^.\n]{0,40}(?P<year>20[0-9]{2}|[0-9]{2})\s*(?:년|e)?",
    )
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if not match:
            continue
        year = _year_value(match.group("year"))
        if 1990 <= year <= 2100:
            return year
    return None


def _has_forward_estimate_amount(text: str, labels: tuple[str, ...]) -> bool:
    return _forward_money_after(text, labels) is not None


def _forward_money_after(text: str, labels: tuple[str, ...]) -> float | None:
    for label in labels:
        label_pattern = re.escape(label)
        patterns = (
            rf"{label_pattern}[^.\n]{{0,48}}?(?P<number>-?[0-9][0-9,]*(?:\.[0-9]+)?)\s*(?P<unit>조원|조|억원|억|백만원|만원|원|trillion|billion|million)\s*(?:으로|로)?[^.\n]{{0,36}}?(?:예상|전망|전망치|추정|추정치|가이던스|상향|forecast|estimate|expected|guidance|raised)",
            rf"(?:예상|전망|전망치|추정|추정치|가이던스|상향|forecast|estimate|expected|guidance|raised)[^.\n]{{0,48}}?{label_pattern}[^.\n]{{0,48}}?(?P<number>-?[0-9][0-9,]*(?:\.[0-9]+)?)\s*(?P<unit>조원|조|억원|억|백만원|만원|원|trillion|billion|million)",
            rf"(?:FY[1-3]|20[0-9]{{2}}E|[1-4]\s*Q\s*'?[0-9]{{2,4}}|Q\s*[1-4]\s*'?[0-9]{{2,4}})[^.\n]{{0,80}}?{label_pattern}[^.\n]{{0,48}}?(?P<number>-?[0-9][0-9,]*(?:\.[0-9]+)?)\s*(?P<unit>조원|조|억원|억|백만원|만원|원|trillion|billion|million)",
        )
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if not match:
                continue
            value = _float(match.group("number"))
            if value is None:
                continue
            return _scale_amount(value, match.group("unit"))
    return None


def _forward_eps_after(text: str) -> float | None:
    if not re.search(r"(?:EPS|주당순이익)", text, re.IGNORECASE):
        return None
    if not re.search(r"(?:예상|전망|전망치|추정|추정치|컨센서스|가이던스|forecast|estimate|expected|guidance)", text, re.IGNORECASE):
        return None
    return _number_after(text, ("EPS", "주당순이익"))


def _target_price_value(text: str) -> float | None:
    upgrade_patterns = (
        r"(?:목표주가|목표가)[^.\n]{0,80}?기존\s*(?P<old>[0-9][0-9,]*(?:\.[0-9]+)?)\s*(?P<old_unit>만원|원)?[^.\n]{0,40}?(?P<new>[0-9][0-9,]*(?:\.[0-9]+)?)\s*(?P<new_unit>만원|원)?(?:으로|로)?\s*상향",
        r"(?:목표주가|목표가)[^.\n]{0,80}?(?P<old>[0-9][0-9,]*(?:\.[0-9]+)?)\s*(?P<old_unit>만원|원)?\s*(?:에서|→|->|to)\s*(?P<new>[0-9][0-9,]*(?:\.[0-9]+)?)\s*(?P<new_unit>만원|원)?",
        r"target price[^.\n]{0,80}?(?:from\s*)?(?P<old>[0-9][0-9,]*(?:\.[0-9]+)?)\s*(?P<old_unit>만원|원)?\s*(?:to|→|->)\s*(?P<new>[0-9][0-9,]*(?:\.[0-9]+)?)\s*(?P<new_unit>만원|원)?",
    )
    for pattern in upgrade_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if not match:
            continue
        new = _scale_price(_float(match.group("new")), match.groupdict().get("new_unit"))
        if new is not None:
            return new
    patterns = (
        r"(?:목표주가|목표가)[^\n0-9\-]{0,36}(?P<number>[0-9][0-9,]*(?:\.[0-9]+)?)\s*(?P<unit>만원|원)?",
        r"target price[^\n0-9\-]{0,36}(?:KRW|₩)?\s*(?P<number>[0-9][0-9,]*(?:\.[0-9]+)?)\s*(?P<unit>만원|원)?",
    )
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if not match:
            continue
        value = _float(match.group("number"))
        if value is None:
            continue
        unit = match.group("unit") or ""
        if unit == "만원":
            value *= 10_000.0
        return value
    return None


def _target_price_revision_pct(text: str) -> float | None:
    patterns = (
        r"(?:목표주가|목표가)[^.\n]{0,80}?기존\s*(?P<old>[0-9][0-9,]*(?:\.[0-9]+)?)\s*(?P<old_unit>만원|원)?[^.\n]{0,40}?(?P<new>[0-9][0-9,]*(?:\.[0-9]+)?)\s*(?P<new_unit>만원|원)?(?:으로|로)?\s*상향",
        r"(?:목표주가|목표가)[^.\n]{0,80}?(?P<old>[0-9][0-9,]*(?:\.[0-9]+)?)\s*(?P<old_unit>만원|원)?\s*(?:에서|→|->|to)\s*(?P<new>[0-9][0-9,]*(?:\.[0-9]+)?)\s*(?P<new_unit>만원|원)?",
        r"target price[^.\n]{0,80}?(?:from\s*)?(?P<old>[0-9][0-9,]*(?:\.[0-9]+)?)\s*(?P<old_unit>만원|원)?\s*(?:to|→|->)\s*(?P<new>[0-9][0-9,]*(?:\.[0-9]+)?)\s*(?P<new_unit>만원|원)?",
    )
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if not match:
            continue
        old = _scale_price(_float(match.group("old")), match.groupdict().get("old_unit"))
        new = _scale_price(_float(match.group("new")), match.groupdict().get("new_unit"))
        if old is None or new is None or old <= 0 or new <= old:
            continue
        return (new / old - 1.0) * 100.0
    return None


def _target_price_upgrade_mentioned(text: str) -> bool:
    lowered = text.lower()
    return (
        "목표주가 상향" in text
        or "목표가 상향" in text
        or "목표가↑" in text
        or re.search(r"(?:목표주가|목표가)[^.\n]{0,40}(?:상향|올려|인상)", text) is not None
        or "target price raised" in lowered
        or "target price upgrade" in lowered
    )


def _estimate_upgrade_mentioned(text: str) -> bool:
    lowered = text.lower()
    return (
        "실적 전망치 상향" in text
        or "실적 추정치 상향" in text
        or "영업이익 전망치 상향" in text
        or "영업이익 추정치 상향" in text
        or "전망치 상향" in text
        or "추정치 상향" in text
        or "eps 상향" in lowered
        or "estimate upgrade" in lowered
        or "estimate raised" in lowered
    )


def _scale_amount(value: float, unit: str | None) -> float:
    normalized = (unit or "").lower()
    if normalized in {"조원", "조", "trillion"}:
        return value * 1_000_000_000_000.0
    if normalized in {"억원", "억", "billion"}:
        return value * 100_000_000.0
    if normalized in {"백만원", "million"}:
        return value * 1_000_000.0
    if normalized == "만원":
        return value * 10_000.0
    return value


def _scale_price(value: float | None, unit: str | None) -> float | None:
    if value is None:
        return None
    if unit == "만원":
        return value * 10_000.0
    return value


def _year_value(value: str) -> int:
    year = int(value)
    if year < 100:
        return 2000 + year if year < 70 else 1900 + year
    return year


def _float(value: str | None) -> float | None:
    if value in (None, ""):
        return None
    try:
        return float(str(value).replace(",", ""))
    except ValueError:
        return None


def _points_after(text: str, labels: tuple[str, ...]) -> tuple[str, ...]:
    for label in labels:
        match = re.search(rf"{re.escape(label)}\s*[:：]\s*(?P<value>[^\n]+)", text, re.IGNORECASE)
        if match:
            return tuple(item.strip(" -\t") for item in re.split(r"[|;·]", match.group("value")) if item.strip())
    return ()


def _confidence(fields: Mapping[str, Any], text: str) -> float:
    numeric_count = sum(1 for value in fields.values() if isinstance(value, (int, float)))
    keyword_bonus = sum(1 for token in ("수주잔고", "CAPA", "ASP", "리드타임", "공급부족") if token in text) * 0.03
    return min(1.0, 0.35 + numeric_count * 0.035 + keyword_bonus)


def _stable_id(text: str) -> str:
    return hashlib.sha1(text.encode("utf-8")).hexdigest()[:10]
