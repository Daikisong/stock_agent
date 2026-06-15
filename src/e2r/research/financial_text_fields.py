"""Extract explicit financial-performance signals from fetched text/snippets."""

from __future__ import annotations

import re
from datetime import date
from calendar import monthrange
from typing import Any


def extract_reported_financial_fields(text: str, *, as_of_date: date | None = None) -> dict[str, Any]:
    """Return normalized fields only when financial figures are explicit."""

    fields: dict[str, Any] = {}
    if not text or not _has_financial_performance_context(text):
        return fields

    period = latest_reported_period_end(text)
    future_period = bool(as_of_date is not None and period is not None and period > as_of_date)
    sales = None if future_period else _money_after(text, ("매출액", "매출", "sales", "revenue"))
    operating_profit = None if future_period else _money_after(text, ("영업이익", "영업익", "잠정 영업익", "operating profit", "op"))
    if sales is not None:
        fields["actual_sales"] = sales
    if operating_profit is not None:
        fields["actual_operating_profit"] = operating_profit
    if sales is not None or operating_profit is not None:
        fields["financial_actuals_from_text"] = True
        fields["financial_actuals_present"] = True
    if sales is not None and operating_profit is not None and sales > 0:
        fields["actual_opm"] = operating_profit / sales * 100.0

    if period is not None and (sales is not None or operating_profit is not None):
        fields["reported_fiscal_year"] = period.year
        fields["reported_fiscal_quarter"] = (period.month - 1) // 3 + 1

    sales_yoy = None if future_period else _nearby_yoy_pct(text, ("매출액", "매출", "sales", "revenue"))
    op_yoy = None if future_period else _nearby_yoy_pct(text, ("영업이익", "operating profit", "op"))
    if sales_yoy is not None:
        fields["actual_sales_yoy_pct"] = sales_yoy
        fields["sales_yoy_pct"] = sales_yoy
    if op_yoy is not None:
        fields["actual_op_yoy_pct"] = op_yoy
        fields["op_yoy_pct"] = op_yoy

    lowered = text.lower()
    if (
        "컨센서스 상회" in text
        or "컨센서스를 상회" in text
        or "시장 예상 상회" in text
        or "예상치 상회" in text
        or "어닝 서프라이즈" in text
        or "깜짝 실적" in text
        or "earnings beat" in lowered
        or "beat consensus" in lowered
    ):
        fields["earnings_beat_mentioned"] = True
        fields["consensus_beat_mentioned"] = True
    if (
        "실적 전망치 상향" in text
        or "실적 추정치 상향" in text
        or "영업이익 전망치 상향" in text
        or "영업이익 추정치 상향" in text
        or "전망치 상향" in text
        or "추정치 상향" in text
        or "eps 상향" in lowered
        or "estimate upgrade" in lowered
        or "estimate raised" in lowered
    ):
        fields["estimate_upgrade_mentioned"] = True
    if "목표주가 상향" in text or "목표가 상향" in text or "목표가↑" in text or "target price raised" in lowered or "target price upgrade" in lowered:
        fields["target_price_upgrade_mentioned"] = True
    target_revision = _target_price_revision_pct(text)
    if target_revision is not None:
        fields["target_price_revision_pct"] = target_revision
        fields["target_revision_pct"] = target_revision
        fields["target_price_upgrade_mentioned"] = True

    return fields


def latest_reported_period_end(text: str) -> date | None:
    """Infer the latest fiscal quarter/year explicitly mentioned in text."""

    periods: list[date] = []
    for match in re.finditer(r"(20[0-9]{2})\s*년?\s*([1-4])\s*분기", text):
        periods.append(_quarter_end(int(match.group(1)), int(match.group(2))))
    for match in re.finditer(r"(?<![0-9])([0-9]{2})\s*년\s*([1-4])\s*분기", text):
        periods.append(_quarter_end(_two_digit_year(match.group(1)), int(match.group(2))))
    for match in re.finditer(r"(?<![a-z0-9])([1-4])q\s*'?([0-9]{2,4})(?![0-9])", text, re.IGNORECASE):
        periods.append(_quarter_end(_year_value(match.group(2)), int(match.group(1))))
    for match in re.finditer(r"(?<![a-z0-9])q([1-4])\s*'?([0-9]{2,4})(?![0-9])", text, re.IGNORECASE):
        periods.append(_quarter_end(_year_value(match.group(2)), int(match.group(1))))
    return max(periods) if periods else None


def _has_financial_performance_context(text: str) -> bool:
    lowered = text.lower()
    return (
        ("매출" in text and "영업이익" in text)
        or "실적" in text
        or "잠정실적" in text
        or "컨센서스 상회" in text
        or "어닝 서프라이즈" in text
        or "earnings" in lowered
        or "operating profit" in lowered
    )


def _money_after(text: str, labels: tuple[str, ...]) -> float | None:
    for label in labels:
        pattern = (
            rf"{re.escape(label)}[^0-9\-]{{0,28}}"
            r"(?P<number>-?[0-9][0-9,]*(?:\.[0-9]+)?)\s*"
            r"(?P<unit>조원|조|억원|억|백만원|만원|원|trillion|billion|million)"
            r"(?:\s*(?P<sub_number>[0-9][0-9,]*)\s*(?P<sub_unit>억원|억))?"
        )
        match = re.search(pattern, text, re.IGNORECASE)
        if not match:
            continue
        prefix_context = text[match.start() : match.start("number")]
        suffix_context = text[match.end() : match.end() + 36]
        if _looks_like_forward_estimate(prefix_context) or _looks_like_forward_estimate_after_amount(suffix_context):
            continue
        value = _float(match.group("number"))
        if value is None:
            continue
        unit = (match.group("unit") or "").lower()
        amount = _scale_money(value, unit)
        sub_number = _float(match.group("sub_number"))
        sub_unit = match.group("sub_unit")
        if sub_number is not None and sub_unit in {"억원", "억"}:
            amount += sub_number * 100_000_000.0
        return amount
    return None


def _looks_like_forward_estimate(context: str) -> bool:
    lowered = context.lower()
    return any(
        token in lowered
        for token in (
            "전망",
            "전망치",
            "추정",
            "추정치",
            "예상",
            "가이던스",
            "컨센서스",
            "forecast",
            "estimate",
            "expected",
            "guidance",
        )
    )


def _looks_like_forward_estimate_after_amount(context: str) -> bool:
    lowered = context.lower()
    if re.search(r"(?:예상치|시장\s*예상|컨센서스)[^.\n]{0,16}(?:상회|하회|웃돌|밑돌|beat|above|below)", lowered):
        return False
    return any(
        token in lowered
        for token in (
            "전망",
            "전망치",
            "추정",
            "추정치",
            "예상",
            "가이던스",
            "forecast",
            "estimate",
            "expected",
            "guidance",
        )
    )


def _scale_money(value: float, unit: str) -> float:
    if unit in {"조원", "조", "trillion"}:
        return value * 1_000_000_000_000.0
    if unit in {"억원", "억", "billion"}:
        return value * 100_000_000.0
    if unit in {"백만원", "million"}:
        return value * 1_000_000.0
    if unit == "만원":
        return value * 10_000.0
    return value


def _nearby_yoy_pct(text: str, labels: tuple[str, ...]) -> float | None:
    for label in labels:
        for match in re.finditer(re.escape(label), text, re.IGNORECASE):
            window = text[match.start() : match.start() + 180]
            yoy = _yoy_pct_from_window(window)
            if yoy is not None:
                return yoy
    return None


def _target_price_revision_pct(text: str) -> float | None:
    patterns = (
        r"(?:목표주가|목표가)[^.\n]{0,80}?기존\s*(?P<old>[0-9][0-9,]*(?:\.[0-9]+)?)\s*(?P<old_unit>만원|원)?[^.\n]{0,40}?(?P<new>[0-9][0-9,]*(?:\.[0-9]+)?)\s*(?P<new_unit>만원|원)?(?:으로|로)?\s*상향",
        r"(?:목표주가|목표가)[^.\n]{0,80}?(?P<old>[0-9][0-9,]*(?:\.[0-9]+)?)\s*(?P<old_unit>만원|원)?\s*(?:에서|→|->|to)\s*(?P<new>[0-9][0-9,]*(?:\.[0-9]+)?)\s*(?P<new_unit>만원|원)?",
        r"target price[^.\n]{0,80}?(?:from\s*)?(?:krw\s*)?(?P<old>[0-9][0-9,]*(?:\.[0-9]+)?)\s*(?P<old_unit>만원|원)?\s*(?:to|→|->)\s*(?:krw\s*)?(?P<new>[0-9][0-9,]*(?:\.[0-9]+)?)\s*(?P<new_unit>만원|원)?",
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


def _scale_price(value: float | None, unit: str | None) -> float | None:
    if value is None:
        return None
    if unit == "만원":
        return value * 10_000.0
    return value


def _yoy_pct_from_window(window: str) -> float | None:
    patterns = (
        r"(?:전년\s*(?:동기)?\s*대비|전년대비|yoy|y/y)[^0-9+\-]{0,40}(?P<number>[+\-]?[0-9][0-9,]*(?:\.[0-9]+)?)\s*%?\s*(?P<direction>증가|감소|상승|하락|up|down)?",
        r"(?P<number>[+\-]?[0-9][0-9,]*(?:\.[0-9]+)?)\s*%\s*(?P<direction>증가|감소|상승|하락|up|down)?[^.\n]{0,40}(?:전년\s*(?:동기)?\s*대비|전년대비|yoy|y/y)",
    )
    for pattern in patterns:
        match = re.search(pattern, window, re.IGNORECASE)
        if not match:
            continue
        value = _float(match.group("number"))
        if value is None:
            continue
        direction = (match.groupdict().get("direction") or "").lower()
        if direction in {"감소", "하락", "down"} and value > 0:
            value = -value
        return value
    return None


def _quarter_end(year: int, quarter: int) -> date:
    month = quarter * 3
    return date(year, month, monthrange(year, month)[1])


def _year_value(value: str) -> int:
    return _two_digit_year(value) if len(value) == 2 else int(value)


def _two_digit_year(value: str) -> int:
    year = int(value)
    return 2000 + year if year < 70 else 1900 + year


def _float(value: str | None) -> float | None:
    if value in (None, ""):
        return None
    try:
        return float(str(value).replace(",", ""))
    except ValueError:
        return None


__all__ = ["extract_reported_financial_fields", "latest_reported_period_end"]
