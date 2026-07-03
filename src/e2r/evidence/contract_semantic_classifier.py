"""Semantic classifier for disclosure/event contract language.

This is intentionally conservative. It does not decide score or stage; it only
separates revenue-facing contracts from financial/admin uses of the word
"contract".
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping


COMMERCIAL_SUPPLY_CONTRACT = "commercial_supply_contract"
CUSTOMER_ORDER_OR_BACKLOG = "customer_order_or_backlog"
FINANCIAL_CONTRACT = "financial_contract"
SHAREHOLDER_RETURN_CONTRACT = "shareholder_return_contract"
SHARE_BUYBACK_TRUST_CONTRACT = "share_buyback_trust_contract"
PLEDGE_OR_COLLATERAL_CONTRACT = "pledge_or_collateral_contract"
EQUITY_ISSUANCE_OR_SECURITY_REGISTRATION = "equity_issuance_or_security_registration"
CAPITAL_ALLOCATION_EVENT = "capital_allocation_event"
ADMINISTRATIVE_DISCLOSURE = "administrative_disclosure"
CLARIFICATION_OR_RUMOR_RESPONSE = "clarification_or_rumor_response"
INFORMATION_CONFIDENCE_ONLY = "information_confidence_only"
RISK_OR_LISTING_EVENT = "risk_or_listing_event"
UNRELATED_CONTRACT_OR_WRONG_SUBJECT = "unrelated_contract_or_wrong_subject"


@dataclass(frozen=True)
class ContractSemanticClassification:
    event_class: str
    revenue_facing: bool
    allowed_for_contract_quality: bool
    reasons: tuple[str, ...]

    def to_dict(self) -> dict[str, Any]:
        return {
            "event_class": self.event_class,
            "revenue_facing": self.revenue_facing,
            "allowed_for_contract_quality": self.allowed_for_contract_quality,
            "reasons": list(self.reasons),
        }


def classify_contract_event(row: Mapping[str, Any]) -> ContractSemanticClassification:
    text = _combined_text(row)
    reasons: list[str] = []

    if _has_any(text, ("자기주식취득신탁", "자기주식 취득 신탁", "자기주식취득 신탁")):
        return _blocked(SHARE_BUYBACK_TRUST_CONTRACT, "share buyback trust is capital/shareholder-return, not customer demand")
    if _has_any(text, ("주식담보", "담보제공", "질권", "pledge", "collateral")):
        return _blocked(PLEDGE_OR_COLLATERAL_CONTRACT, "pledge/collateral contract is not customer revenue visibility")
    if _has_any(text, ("유상증자", "무상증자", "증권신고서", "지분증권", "전환사채", "신주인수권", "교환사채")):
        return _blocked(EQUITY_ISSUANCE_OR_SECURITY_REGISTRATION, "equity/security filing is capital allocation, not revenue contract")
    if _has_any(text, ("풍문또는보도에대한해명", "풍문 또는 보도", "해명(미확정)", "해명")):
        return _blocked(CLARIFICATION_OR_RUMOR_RESPONSE, "rumor clarification is information confidence only")
    if _has_any(text, ("거래정지", "관리종목", "상장폐지", "개선기간", "투자주의환기")):
        return _blocked(RISK_OR_LISTING_EVENT, "listing/risk event is risk overlay, not contract quality")

    if _has_any(text, ("단일판매", "공급계약", "판매ㆍ공급계약", "판매·공급계약", "수주", "order", "backlog")):
        reasons.append("supply/order wording present")
        return ContractSemanticClassification(
            event_class=COMMERCIAL_SUPPLY_CONTRACT,
            revenue_facing=True,
            allowed_for_contract_quality=True,
            reasons=tuple(reasons),
        )

    if _has_any(text, ("시설투자", "유형자산취득", "생산능력", "capa", "capacity")):
        return ContractSemanticClassification(
            event_class=CAPITAL_ALLOCATION_EVENT,
            revenue_facing=False,
            allowed_for_contract_quality=False,
            reasons=("capacity/capital event is not customer contract quality by itself",),
        )

    if "계약" in text:
        return _blocked(FINANCIAL_CONTRACT, "contract wording exists but no customer/order/revenue scope was identified")
    if _has_any(text, ("투자판단관련주요경영사항", "주요사항보고서")):
        return _blocked(ADMINISTRATIVE_DISCLOSURE, "administrative disclosure requires a more specific revenue-facing claim")
    return _blocked(INFORMATION_CONFIDENCE_ONLY, "no revenue-facing contract evidence identified")


def _blocked(event_class: str, reason: str) -> ContractSemanticClassification:
    return ContractSemanticClassification(
        event_class=event_class,
        revenue_facing=False,
        allowed_for_contract_quality=False,
        reasons=(reason,),
    )


def _combined_text(row: Mapping[str, Any]) -> str:
    parts: list[str] = []
    for key in ("quote_text", "event_title", "event_summary", "event_type", "report_nm", "title", "summary", "primitive_id"):
        value = row.get(key)
        if value is not None:
            parts.append(str(value))
    mapping = row.get("mapping")
    if isinstance(mapping, Mapping):
        for key in ("primitive_id", "rationale"):
            value = mapping.get(key)
            if value is not None:
                parts.append(str(value))
    return " ".join(parts).lower()


def _has_any(text: str, needles: tuple[str, ...]) -> bool:
    return any(needle.lower() in text for needle in needles)


__all__ = [
    "CAPITAL_ALLOCATION_EVENT",
    "CLARIFICATION_OR_RUMOR_RESPONSE",
    "COMMERCIAL_SUPPLY_CONTRACT",
    "ContractSemanticClassification",
    "EQUITY_ISSUANCE_OR_SECURITY_REGISTRATION",
    "PLEDGE_OR_COLLATERAL_CONTRACT",
    "SHARE_BUYBACK_TRUST_CONTRACT",
    "classify_contract_event",
]
