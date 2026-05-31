"""Resolve v12 large-sector/canonical archetype before rolling scoring."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping

from e2r.calibration.taxonomy import (
    CANONICAL_ARCHETYPE_IDS,
    LARGE_SECTOR_IDS,
    large_sector_for_archetype,
    normalise_canonical_archetype_id,
    normalise_large_sector_id,
)
from e2r.sector_profiles import SectorProfile


@dataclass(frozen=True)
class ArchetypeClassification:
    """Resolved v12 taxonomy scope used by runtime scoring."""

    large_sector_id: str
    canonical_archetype_id: str
    confidence: float
    reason: str


class ArchetypeResolutionError(ValueError):
    """Raised when evidence cannot be mapped into a valid v12 archetype."""


def classify_v12_archetype(
    *,
    symbol: str,
    sector_profile: SectorProfile,
    parsed_fields: Mapping[str, Any],
    text: str,
    company_name: str | None = None,
    sector_context: str | None = None,
    large_sector_id: str | None = None,
    canonical_archetype_id: str | None = None,
    price_stage_score: float = 0.0,
    revision_score: float = 0.0,
) -> ArchetypeClassification:
    """Classify a candidate into an explicit v12 archetype.

    This is deliberately a classifier, not a weight fallback. Bad or missing
    metadata is not carried into scoring; the available point-in-time context
    from search, reports, filings, news, and parsed fields is routed to a
    specific C/R13 archetype before scoring starts.
    """

    del symbol  # Symbol-specific historical winner lookup is intentionally forbidden.
    normalised_canonical = normalise_canonical_archetype_id(canonical_archetype_id)
    normalised_large = normalise_large_sector_id(large_sector_id)
    resolution_note: str | None = None
    if normalised_canonical:
        if normalised_canonical in CANONICAL_ARCHETYPE_IDS:
            expected_large = large_sector_for_archetype(normalised_canonical)
            if expected_large is None:
                raise ArchetypeResolutionError(f"canonical_archetype_id has no large sector: {normalised_canonical}")
            reason = "explicit_canonical_archetype"
            confidence = 1.0
            if normalised_large and normalised_large != expected_large:
                reason = "explicit_canonical_corrected_large_sector_mismatch"
                confidence = 0.95
            return ArchetypeClassification(
                large_sector_id=expected_large,
                canonical_archetype_id=normalised_canonical,
                confidence=confidence,
                reason=reason,
            )
        resolution_note = "unknown_explicit_canonical_reclassified_by_agent_context"
    if normalised_large and normalised_large not in LARGE_SECTOR_IDS:
        resolution_note = "unknown_explicit_large_sector_reclassified_by_agent_context"

    haystack = _haystack(text=text, company_name=company_name, sector_context=sector_context, parsed_fields=parsed_fields)
    canonical = _classify_from_context(
        sector_profile=sector_profile,
        parsed_fields=parsed_fields,
        haystack=haystack,
        price_stage_score=price_stage_score,
        revision_score=revision_score,
    )
    expected_large = large_sector_for_archetype(canonical)
    if expected_large is None:
        raise ArchetypeResolutionError(f"classifier emitted archetype without large sector: {canonical}")
    if normalised_large and normalised_large != expected_large:
        resolution_note = "provided_large_sector_corrected_by_agent_classification"
    return ArchetypeClassification(
        large_sector_id=expected_large,
        canonical_archetype_id=canonical,
        confidence=_confidence_for(canonical, sector_profile, haystack, parsed_fields, resolution_note),
        reason=_reason_for(canonical, resolution_note),
    )


def _classify_from_context(
    *,
    sector_profile: SectorProfile,
    parsed_fields: Mapping[str, Any],
    haystack: str,
    price_stage_score: float,
    revision_score: float,
) -> str:
    if _has_any(haystack, ("회계", "감사", "accounting", "audit", "trust", "short seller", "공매도")):
        return "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION"
    if price_stage_score >= 90.0 and revision_score < 50.0:
        return "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM"

    if sector_profile == SectorProfile.DEFENSE or _has_any(haystack, ("방산", "defense", "k9", "천무")):
        return "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG"
    if sector_profile == SectorProfile.POWER_EQUIPMENT:
        if _has_any(haystack, ("원전", "nuclear", "smr", "legal delay", "소송", "허가")):
            return "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY"
        if _has_any(haystack, ("epc", "mega contract", "플랜트", "jafurah", "gas pipeline")):
            return "C05_EPC_MEGA_CONTRACT_MARGIN_GAP"
        if _has_any(haystack, ("defense", "방산", "폴란드", "government customer")):
            return "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG"
        if _has_any(
            haystack,
            (
                "datacenter",
                "data center",
                "데이터센터",
                "전력망",
                "grid",
                "transformer",
                "변압기",
                "power_equipment",
                "power equipment",
                "전력기기",
                "중공업",
                "초고압",
            ),
        ):
            return "C02_POWER_GRID_DATACENTER_CAPEX"
        return "C01_ORDER_BACKLOG_MARGIN_BRIDGE"

    if sector_profile == SectorProfile.MEMORY_HBM or _has_any(haystack, ("hbm", "memory", "dram", "nand", "반도체")):
        if _has_any(haystack, ("socket", "test", "테스트", "probe", "qualification", "customer quality")):
            return "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY"
        if _has_any(haystack, ("equipment", "장비", "bonder", "order", "상대강도")):
            return "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH"
        if _has_any(haystack, ("blowoff", "valuation", "과열", "멀티플")):
            return "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF"
        if _has_any(haystack, ("recovery", "cycle", "price increase", "가격 상승", "supply discipline", "공급조절")):
            return "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE"
        return "C06_HBM_MEMORY_CUSTOMER_CAPACITY"

    if sector_profile == SectorProfile.BATTERY_OVERHEAT or _has_any(haystack, ("battery", "배터리", "ev", "2차전지")):
        if _has_any(haystack, ("slowdown", "수요 둔화", "cancellation", "cancel", "4c")):
            return "C14_EV_DEMAND_SLOWDOWN_4B_4C"
        if _has_any(haystack, ("jv", "ampc", "ira", "utilization", "보조금")):
            return "C13_BATTERY_JV_UTILIZATION_AMPC_IRA"
        if _has_any(haystack, ("call-off", "calloff", "customer risk", "고객 리스크")):
            return "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK"
        return "C11_BATTERY_ORDERBOOK_RERATING"

    if sector_profile in {SectorProfile.K_FOOD_EXPORT, SectorProfile.K_BEAUTY_EXPORT}:
        return "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION"
    if _has_any(haystack, ("beauty", "뷰티", "food", "식품", "k-food", "k-beauty", "distribution", "유통")):
        return "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION"
    if _has_any(haystack, ("export channel", "수출 채널", "reorder", "재주문")):
        return "C18_CONSUMER_EXPORT_CHANNEL_REORDER"
    if _has_any(haystack, ("inventory", "재고", "retail", "리테일", "brand margin")):
        return "C19_BRAND_RETAIL_INVENTORY_MARGIN"

    if _has_any(haystack, ("insurance", "보험", "reserve", "준비금", "rate cycle")):
        return "C22_INSURANCE_RATE_CYCLE_RESERVE"
    if _has_any(haystack, ("roe", "pbr", "buyback", "dividend", "capital return", "value-up", "은행", "금융")):
        return "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN"

    if _has_any(haystack, ("approval", "fda", "regulatory", "commercialization", "승인", "허가")):
        return "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION"
    if _has_any(haystack, ("trial", "phase", "임상", "data event")):
        return "C24_BIO_TRIAL_DATA_EVENT_RISK"
    if _has_any(haystack, ("medical device", "의료기기", "reimbursement", "procedure", "시술")):
        return "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT"

    if _has_any(haystack, ("ad revenue", "advertising", "arpu", "platform", "광고")):
        return "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE"
    if _has_any(haystack, ("content", "ip", "game", "콘텐츠", "게임")):
        return "C27_CONTENT_IP_GLOBAL_MONETIZATION"
    if _has_any(haystack, ("software", "security", "arr", "retention", "saas", "보안")):
        return "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION"

    if _has_any(haystack, ("chemical", "화학", "spread", "스프레드")):
        return "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD"
    if _has_any(haystack, ("resource", "rare earth", "lithium", "리튬", "희토류")):
        return "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY"
    if _has_any(haystack, ("materials", "소재", "commodity", "원자재")):
        return "C15_MATERIAL_SPREAD_SUPERCYCLE"

    if _has_any(haystack, ("mobility", "auto", "vehicle", "transport", "logistics", "자동차", "운송")):
        return "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE"
    if _has_any(haystack, ("pf", "construction", "real estate", "housing", "건설", "부동산")):
        return "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK"
    if _has_any(haystack, ("governance", "tender", "control premium", "지배구조", "공개매수")):
        return "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP"
    if _has_any(haystack, ("policy", "subsidy", "legislation", "law", "정책", "보조금", "법안")):
        return "C31_POLICY_SUBSIDY_LEGISLATION_EVENT"

    if _has_operating_evidence(parsed_fields):
        return "C01_ORDER_BACKLOG_MARGIN_BRIDGE"
    return "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW"


def _has_operating_evidence(parsed_fields: Mapping[str, Any]) -> bool:
    fields = {
        "contract_amount_to_prior_sales",
        "contract_duration_months",
        "order_backlog_to_sales",
        "rpo_to_sales",
        "backlog_to_sales",
        "capa_utilization_pct",
        "lead_time_months",
        "asp_yoy_pct",
        "opm_expansion_pctp",
        "fcf_quality_score",
    }
    return any(parsed_fields.get(field) not in (None, "", False, 0) for field in fields)


def _haystack(
    *,
    text: str,
    company_name: str | None,
    sector_context: str | None,
    parsed_fields: Mapping[str, Any],
) -> str:
    field_tokens = " ".join(str(key) for key, value in parsed_fields.items() if value not in (None, "", False, 0))
    return " ".join((company_name or "", sector_context or "", text or "", field_tokens)).lower()


def _has_any(haystack: str, tokens: tuple[str, ...]) -> bool:
    return any(token.lower() in haystack for token in tokens)


def _confidence_for(
    canonical: str,
    sector_profile: SectorProfile,
    haystack: str,
    parsed_fields: Mapping[str, Any],
    resolution_note: str | None = None,
) -> float:
    if canonical.startswith("R13_"):
        confidence = 0.7
    elif sector_profile != SectorProfile.GENERIC:
        confidence = 0.9
    elif _has_operating_evidence(parsed_fields):
        confidence = 0.75
    elif _has_any(haystack, ("policy", "subsidy", "governance", "software", "content", "insurance", "medical")):
        confidence = 0.75
    else:
        confidence = 0.65
    if resolution_note:
        return max(0.55, confidence - 0.1)
    return confidence


def _reason_for(canonical: str, resolution_note: str | None = None) -> str:
    if canonical.startswith("R13_"):
        reason = "cross_archetype_guardrail_classification"
    elif canonical.startswith("C02"):
        reason = "power_grid_or_datacenter_capex_evidence"
    elif canonical.startswith("C03"):
        reason = "defense_export_backlog_evidence"
    elif canonical.startswith("C06") or canonical.startswith("C07") or canonical.startswith("C08") or canonical.startswith("C10"):
        reason = "ai_semiconductor_or_memory_evidence"
    elif canonical.startswith("C20"):
        reason = "consumer_global_distribution_evidence"
    else:
        reason = "evidence_routed_to_canonical_archetype"
    if resolution_note:
        return f"{reason}:{resolution_note}"
    return reason


__all__ = [
    "ArchetypeClassification",
    "ArchetypeResolutionError",
    "classify_v12_archetype",
]
