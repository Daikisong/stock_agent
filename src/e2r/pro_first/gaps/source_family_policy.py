"""Generic Pro source-family role and connector routing policy.

The policy branches on the source authority (issuer, regulator, customer,
peer, and so on), never on a target, sector, archetype, or missing slot.
"""

from __future__ import annotations


_SUPPORTING_AUTHORITY_PREFIXES = (
    "CUSTOMER_",
    "PEER_",
    "PARTNER_",
    "EQUIPMENT_SUPPLIER_",
    "PACKAGING_PARTNER_",
    "PLATFORM_VENDOR_",
    "INDUSTRY_",
    "REUTERS",
    "TRUSTED_BUSINESS_MEDIA",
    "PUBLIC_BROKER_",
    "GENERAL_WEB_",
    "NAVER_",
)
_CORE_AUTHORITY_PREFIXES = (
    "ISSUER_",
    "REGULATORY_",
    "AUDITED_",
    "CONSENSUS_",
    "NORMALIZED_CONSENSUS_",
    "MARKET_",
    "FINANCIAL_",
    "CASH_FLOW",
    "SEGMENT_",
    "VALUATION_",
    "OPENDART",
    "DART",
    "KIND",
    "KRX",
    "GOVERNMENT_",
)


def normalized_source_family(value: str) -> str:
    return str(value or "").strip().upper()


def source_family_evidence_role(value: str) -> str:
    """Return CORE, SUPPORTING, or UNKNOWN from source authority only."""

    family = normalized_source_family(value)
    if any(family.startswith(prefix) for prefix in _SUPPORTING_AUTHORITY_PREFIXES):
        return "SUPPORTING"
    if any(family.startswith(prefix) for prefix in _CORE_AUTHORITY_PREFIXES):
        return "CORE"
    return "UNKNOWN"


def canonical_gap_source_family(value: str) -> str:
    """Project an open-ended Pro family into Gate 1's closed role taxonomy."""

    family = normalized_source_family(value)
    role = source_family_evidence_role(family)
    if role == "SUPPORTING":
        return "CUSTOMER_OFFICIAL"
    if family.startswith(("CONSENSUS_", "NORMALIZED_CONSENSUS_")):
        return "CONSENSUS_REVISION"
    if family.startswith("MARKET_"):
        return "MARKET_CAP_PRICE"
    if family.startswith("VALUATION_"):
        return "VALUATION_MULTIPLES"
    if family.startswith(("SEGMENT_", "ISSUER_SEGMENT_")):
        return "SEGMENT_DATA"
    if family.startswith(("CASH_FLOW", "AUDITED_CASH_FLOW")):
        return "CASH_FLOW"
    if role == "CORE":
        return "FINANCIAL_STATEMENTS"
    return family


def route_source_classes(value: str) -> tuple[str, ...]:
    """Return existing bounded connector classes for one authority family."""

    family = normalized_source_family(value)
    exact = {
        "OPENDART": ("DART",),
        "DART": ("DART",),
        "KIND_KRX": ("KIND", "KRX"),
        "KIND": ("KIND",),
        "KRX": ("KRX",),
        "ISSUER_EARNINGS_RELEASE": ("IssuerIR", "DART"),
        "ISSUER_PRESENTATION": ("IssuerIR",),
        "ISSUER_NEWSROOM": ("IssuerIR",),
        "FINANCIAL_STATEMENTS": ("DART", "CompanyGuide"),
        "SEGMENT_DATA": ("DART", "CompanyGuide"),
        "CASH_FLOW": ("DART", "CompanyGuide"),
        "MARKET_CAP_PRICE": ("KRX", "CompanyGuide"),
        "CONSENSUS_REVISION": ("CompanyGuide",),
        "VALUATION_MULTIPLES": ("CompanyGuide",),
        "GENERAL_WEB_DISCOVERY": ("GeneralWebSearch",),
        "NAVER_DISCOVERY": ("NaverSearch",),
        "TRUSTED_BUSINESS_MEDIA": ("TrustedNews",),
    }
    if family in exact:
        return exact[family]
    role = source_family_evidence_role(family)
    if role == "SUPPORTING" or family.startswith("GOVERNMENT_"):
        return ("GeneralWebSearch",)
    if family.startswith("ISSUER_"):
        return ("IssuerIR", "DART")
    if family.startswith("REGULATORY_"):
        return ("DART", "KIND", "KRX", "IssuerIR")
    if family.startswith("AUDITED_"):
        return ("DART", "CompanyGuide", "IssuerIR")
    if family.startswith(("CONSENSUS_", "NORMALIZED_CONSENSUS_")):
        return ("CompanyGuide",)
    if family.startswith("MARKET_"):
        return ("KRX", "CompanyGuide")
    if family.startswith("VALUATION_"):
        return ("CompanyGuide",)
    return (value,)


def source_family_requires_general_web(value: str) -> bool:
    return any(
        source_class in {"GeneralWebSearch", "NaverSearch", "TrustedNews"}
        for source_class in route_source_classes(value)
    )


__all__ = [
    "canonical_gap_source_family",
    "normalized_source_family",
    "route_source_classes",
    "source_family_evidence_role",
    "source_family_requires_general_web",
]
