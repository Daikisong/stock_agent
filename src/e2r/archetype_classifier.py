"""Resolve v12 large-sector/canonical archetype before rolling scoring."""

from __future__ import annotations

import re
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
        metadata_haystack=f"{company_name or ''} {sector_context or ''}".lower(),
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
    metadata_haystack: str,
    price_stage_score: float,
    revision_score: float,
) -> str:
    if _has_accounting_trust_risk(haystack, parsed_fields):
        return "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION"
    if price_stage_score >= 90.0 and revision_score < 50.0 and not _has_candidate_route_context(
        sector_profile=sector_profile,
        parsed_fields=parsed_fields,
        haystack=haystack,
        metadata_haystack=metadata_haystack,
    ):
        return "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM"

    bio_route = _classify_bio_healthcare_context(haystack)
    if bio_route and _has_bio_healthcare_metadata(metadata_haystack):
        return bio_route

    if sector_profile == SectorProfile.DEFENSE:
        return "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG"
    if sector_profile == SectorProfile.GENERIC and _has_holding_financial_context(metadata_haystack, haystack):
        return "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN"
    if sector_profile in {SectorProfile.GENERIC, SectorProfile.POWER_EQUIPMENT} and _has_defense_export_evidence(haystack, parsed_fields):
        return "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG"
    if sector_profile == SectorProfile.POWER_EQUIPMENT:
        if _has_defense_export_evidence(haystack, parsed_fields):
            return "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG"
        if _has_power_grid_datacenter_context(haystack):
            return "C02_POWER_GRID_DATACENTER_CAPEX"
        if _has_nuclear_policy_project_context(haystack):
            return "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY"
        if _has_any(haystack, ("epc", "mega contract", "플랜트", "jafurah", "gas pipeline")):
            return "C05_EPC_MEGA_CONTRACT_MARGIN_GAP"
        return "C01_ORDER_BACKLOG_MARGIN_BRIDGE"

    if sector_profile == SectorProfile.AI_INFRA_PLATFORM:
        return _classify_ai_infra_platform(haystack)

    if bio_route and sector_profile == SectorProfile.GENERIC and _has_bio_healthcare_metadata_or_context(metadata_haystack, haystack):
        return bio_route

    mobility_business_context = _has_mobility_business_context(haystack)
    if _has_mobility_context(metadata_haystack) or mobility_business_context:
        return "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE"

    memory_hbm_fallback = (
        sector_profile == SectorProfile.GENERIC
        and _has_semiconductor_memory_context(haystack)
        and not _has_non_semiconductor_metadata_context(metadata_haystack)
    )
    if sector_profile == SectorProfile.MEMORY_HBM or memory_hbm_fallback:
        structured_memory_context = _has_structured_memory_manufacturer_context(parsed_fields)
        equipment_supplier_context = _has_semiconductor_equipment_supplier_context(haystack, parsed_fields)
        memory_manufacturer_context = _has_memory_manufacturer_context(haystack, parsed_fields)
        hbm_customer_capacity_context = _has_hbm_customer_capacity_context(haystack, parsed_fields)
        if memory_manufacturer_context and hbm_customer_capacity_context:
            return "C06_HBM_MEMORY_CUSTOMER_CAPACITY"
        if not structured_memory_context and not hbm_customer_capacity_context and _has_test_socket_context(haystack):
            return "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY"
        if not structured_memory_context and not hbm_customer_capacity_context and equipment_supplier_context:
            return "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH"
        if memory_manufacturer_context and _has_any(haystack, ("recovery", "cycle", "price increase", "가격 상승", "supply discipline", "공급조절")):
            return "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE"
        if memory_manufacturer_context:
            return "C06_HBM_MEMORY_CUSTOMER_CAPACITY"
        if _has_test_socket_context(haystack):
            return "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY"
        if equipment_supplier_context:
            return "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH"
        if _has_any(haystack, ("blowoff", "valuation", "과열", "멀티플")):
            return "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF"
        if _has_any(haystack, ("recovery", "cycle", "price increase", "가격 상승", "supply discipline", "공급조절")):
            return "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE"
        return "C06_HBM_MEMORY_CUSTOMER_CAPACITY"

    battery_fallback = sector_profile == SectorProfile.GENERIC and not mobility_business_context and (
        _has_any(haystack, ("battery", "배터리", "2차전지")) or _has_ev_token(haystack)
    )
    if (sector_profile == SectorProfile.BATTERY_OVERHEAT and not mobility_business_context) or battery_fallback:
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

    if _has_any(haystack, ("insurance", "보험", "reserve", "준비금", "rate cycle")) and not _has_bio_healthcare_metadata_or_context(
        metadata_haystack, haystack
    ):
        return "C22_INSURANCE_RATE_CYCLE_RESERVE"
    if _has_financial_context(haystack, metadata_haystack):
        return "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN"

    if bio_route:
        return bio_route

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
    if _has_governance_control_event(haystack):
        return "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP"
    if _has_any(haystack, ("policy", "subsidy", "legislation", "law", "정책", "보조금", "법안")):
        return "C31_POLICY_SUBSIDY_LEGISLATION_EVENT"

    if _has_operating_evidence(parsed_fields):
        return "C01_ORDER_BACKLOG_MARGIN_BRIDGE"
    return "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW"


def _has_accounting_trust_risk(haystack: str, parsed_fields: Mapping[str, Any]) -> bool:
    if parsed_fields.get("accounting_or_trust_issue"):
        return True
    risk_phrases = (
        "회계 이슈",
        "회계 문제",
        "회계 부정",
        "회계 조작",
        "분식회계",
        "감사의견",
        "감사 의견",
        "의견거절",
        "한정의견",
        "부적정의견",
        "내부회계",
        "내부 회계",
        "감사보고서 미제출",
        "감사보고서 제출 지연",
        "공매도 리포트",
        "공매도 보고서",
        "공매도 공격",
        "숏리포트",
        "short seller report",
        "short-seller report",
        "short report",
        "short attack",
        "accounting issue",
        "accounting irregularity",
        "accounting fraud",
        "audit opinion",
        "qualified opinion",
        "adverse opinion",
        "material weakness",
        "internal control weakness",
        "going concern",
    )
    return _has_any(haystack, risk_phrases)


def _has_defense_export_evidence(haystack: str, parsed_fields: Mapping[str, Any]) -> bool:
    del parsed_fields
    defense_tokens = ("방산", "방위산업", "defense", "defence", "military", "k9", "k2", "천무", "fa-50", "kf-21")
    visibility_tokens = (
        "수출",
        "계약",
        "수주",
        "수주잔고",
        "납품",
        "인도",
        "폴란드",
        "루마니아",
        "정부",
        "방위사업청",
        "export",
        "contract",
        "backlog",
        "delivery",
        "government",
    )
    return _has_nearby_pair(haystack, defense_tokens, visibility_tokens)


def _classify_ai_infra_platform(haystack: str) -> str:
    platform_monetization_tokens = (
        "클라우드 매출",
        "cloud revenue",
        "ai 매출",
        "ai revenue",
        "gpu 매출",
        "gpu revenue",
        "gpu cloud",
        "gpu 클라우드",
        "platform",
        "플랫폼",
        "arpu",
        "광고",
        "advertising",
        "ad revenue",
        "commerce",
        "커머스",
        "search",
        "검색",
        "hyperclova",
        "하이퍼클로바",
        "sovereign ai",
        "소버린 ai",
        "webtoon",
        "웹툰",
        "content ip",
        "콘텐츠",
    )
    physical_datacenter_tokens = (
        "데이터센터",
        "datacenter",
        "data center",
        "capex",
        "전력",
        "power capacity",
        "gpu allocation",
        "gpu 할당",
        "blackwell",
        "b200",
        "gb200",
    )
    if _has_any(haystack, platform_monetization_tokens):
        return "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE"
    if _has_any(haystack, physical_datacenter_tokens):
        return "C02_POWER_GRID_DATACENTER_CAPEX"
    return "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE"


def _has_operating_evidence(parsed_fields: Mapping[str, Any]) -> bool:
    fields = {
        "financial_actuals_present",
        "actual_sales_yoy_pct",
        "actual_op_yoy_pct",
        "actual_eps_yoy_pct",
        "actual_fcf_yoy_pct",
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


def _has_candidate_route_context(
    *,
    sector_profile: SectorProfile,
    parsed_fields: Mapping[str, Any],
    haystack: str,
    metadata_haystack: str,
) -> bool:
    if sector_profile != SectorProfile.GENERIC:
        return True
    if _has_operating_evidence(parsed_fields):
        return True
    if _has_defense_export_evidence(haystack, parsed_fields):
        return True
    if _has_power_grid_datacenter_context(haystack) or _has_nuclear_policy_project_context(haystack):
        return True
    if _has_semiconductor_memory_context(haystack):
        return True
    if _has_financial_context(haystack, metadata_haystack):
        return True
    if _classify_bio_healthcare_context(haystack):
        return True
    route_tokens = (
        "platform",
        "광고",
        "content",
        "콘텐츠",
        "software",
        "보안",
        "battery",
        "배터리",
        "beauty",
        "뷰티",
        "food",
        "식품",
        "chemical",
        "화학",
        "resource",
        "리튬",
        "mobility",
        "자동차",
        "construction",
        "건설",
        "policy",
        "정책",
        "governance",
        "지배구조",
    )
    return _has_any(haystack, route_tokens)


def _has_holding_financial_context(metadata_haystack: str, haystack: str) -> bool:
    return _has_any(metadata_haystack, ("holding", "지주")) or _has_any(
        haystack,
        ("자회사", "지분법", "순자산가치", "할인율"),
    ) or _has_standalone_nav_token(haystack)


def _has_mobility_context(metadata_haystack: str) -> bool:
    return _has_any(metadata_haystack, ("mobility", "auto", "vehicle", "transport", "logistics", "자동차", "운송"))


def _has_mobility_business_context(haystack: str) -> bool:
    if _has_any(
        haystack,
        (
            "완성차",
            "자동차 판매",
            "차량 판매",
            "글로벌 도매",
            "도매 판매",
            "판매대수",
            "제네시스",
            "auto sales",
            "vehicle sales",
            "wholesale volume",
        ),
    ):
        return True
    return _has_nearby_pair(
        haystack,
        ("하이브리드", "suv", "model mix"),
        ("자동차", "차량", "완성차", "판매대수", "도매", "vehicle", "auto"),
        window=80,
    )


def _has_non_semiconductor_metadata_context(haystack: str) -> bool:
    return _has_any(
        haystack,
        (
            "holding",
            "지주",
            "auto",
            "자동차",
            "mobility",
            "모빌리티",
            "auto parts",
            "biotech",
            "bio",
            "바이오",
            "제약",
            "healthcare",
            "power_equipment",
            "전력기기",
        ),
    )


def _has_semiconductor_memory_context(haystack: str) -> bool:
    if _has_any(
        haystack,
        (
            "hbm",
            "high bandwidth memory",
            "고대역폭메모리",
            "고대역폭 메모리",
            "dram",
            "d램",
            "d 램",
            "nand",
            "낸드",
            "lpddr",
            "ddr5",
        ),
    ):
        return True
    if not _has_any(haystack, ("반도체", "semiconductor")):
        return False
    return _has_any(
        haystack,
        (
            "장비",
            "소켓",
            "테스트",
            "웨이퍼",
            "파운드리",
            "공정",
            "기판",
            "후공정",
            "패키징",
            "fab",
            "foundry",
            "wafer",
            "socket",
            "test",
            "equipment",
        ),
    )


def _has_memory_manufacturer_context(haystack: str, parsed_fields: Mapping[str, Any]) -> bool:
    if _has_structured_memory_manufacturer_context(parsed_fields):
        return True
    if _has_any(
        haystack,
        (
            "hbm d램",
            "hbm dram",
            "고대역폭메모리",
            "고대역폭 메모리",
            "메모리 가격",
            "dram 가격",
            "d램 가격",
            "nand 가격",
            "낸드 가격",
            "hbm 공급",
            "hbm 수요",
        ),
    ):
        return True
    return _has_nearby_pair(
        haystack,
        ("hbm", "dram", "d램", "nand", "낸드", "메모리"),
        ("수요", "가격", "공급부족", "공급 부족", "수익성", "실적", "매출", "영업이익"),
    )


def _has_structured_memory_manufacturer_context(parsed_fields: Mapping[str, Any]) -> bool:
    return any(
        parsed_fields.get(key) not in (None, "", False, 0)
        for key in (
            "hbm_demand_mentioned",
            "hbm_context_mentioned",
            "hbm_capacity_constraint",
            "memory_price_increase_mentioned",
            "supply_discipline_mentioned",
        )
    )


def _has_hbm_customer_capacity_context(haystack: str, parsed_fields: Mapping[str, Any]) -> bool:
    if any(
        parsed_fields.get(key) not in (None, "", False, 0)
        for key in (
            "hbm_capacity_constraint",
            "customer_preorder_or_allocation",
            "minimum_revenue_guarantee",
            "minimum_sales_guarantee",
            "revenue_visibility_contract",
        )
    ):
        return True
    if parsed_fields.get("prepayment_exists") not in (None, "", False, 0) and parsed_fields.get("multi_year_contract") not in (
        None,
        "",
        False,
        0,
    ):
        return True
    hbm_terms = (
        "hbm",
        "hbm3",
        "hbm3e",
        "hbm4",
        "high bandwidth memory",
        "고대역폭메모리",
        "고대역폭 메모리",
    )
    customer_capacity_terms = (
        "nvidia",
        "엔비디아",
        "customer allocation",
        "customer preorder",
        "customer pre-order",
        "고객 배정",
        "고객사 배정",
        "선급금",
        "선수금",
        "prepayment",
        "lta",
        "long-term agreement",
        "장기공급계약",
        "장기 공급계약",
        "최소 매출 보장",
        "최소매출 보장",
        "최소 물량 보장",
        "최소 구매 보장",
        "capacity locked",
        "capa locked",
        "생산능력 배정",
    )
    if _has_nearby_pair(haystack, hbm_terms, customer_capacity_terms, window=260):
        return True
    return _has_nearby_pair(
        haystack,
        ("메모리", "memory", "dram", "d램"),
        (
            "lta",
            "long-term agreement",
            "장기공급계약",
            "장기 공급계약",
            "최소 매출 보장",
            "최소매출 보장",
            "선급금",
            "선수금",
        ),
        window=220,
    )


def _has_test_socket_context(haystack: str) -> bool:
    if _has_any(haystack, ("socket", "소켓", "probe", "프로브", "customer quality")):
        return True
    return _has_nearby_pair(
        haystack,
        ("test", "테스트", "qualification", "퀄", "인증"),
        ("socket", "소켓", "probe", "프로브", "검사", "quality", "품질"),
        window=80,
    )


def _has_semiconductor_equipment_supplier_context(haystack: str, parsed_fields: Mapping[str, Any]) -> bool:
    if parsed_fields.get("equipment_order_mentioned") not in (None, "", False, 0):
        return True
    equipment_tokens = (
        "반도체 장비",
        "검사장비",
        "후공정 장비",
        "패키징 장비",
        "bonding equipment",
        "test equipment",
        "inspection equipment",
        "equipment supplier",
        "equipment maker",
        "bonder",
        "tsv-tc",
        "tc bonder",
    )
    if not _has_any(haystack, equipment_tokens):
        return False
    return _has_any(haystack, ("수주", "계약", "공급", "order", "backlog", "customer po", "purchase order"))


def _has_power_grid_datacenter_context(haystack: str) -> bool:
    return _has_any(
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
    )


def _has_nuclear_policy_project_context(haystack: str) -> bool:
    if "smr" in haystack:
        return True
    nuclear_terms = ("원전", "nuclear")
    project_terms = (
        "정책",
        "허가",
        "소송",
        "legal delay",
        "지연",
        "착공",
        "수주",
        "프로젝트",
        "project",
        "license",
        "permit",
        "litigation",
    )
    return _has_nearby_pair(haystack, nuclear_terms, project_terms)


def _has_financial_context(haystack: str, metadata_haystack: str) -> bool:
    if _has_any(metadata_haystack, ("financial", "finance", "금융", "은행", "holding", "지주")):
        return True
    return _has_any(
        haystack,
        (
            "roe",
            "pbr",
            "buyback",
            "dividend",
            "capital return",
            "value-up",
            "자사주",
            "배당",
            "주주환원",
            "지분법",
            "순자산가치",
        ),
    ) or _has_standalone_nav_token(haystack)


def _has_standalone_nav_token(haystack: str) -> bool:
    return re.search(r"(?<![a-z0-9])nav(?![a-z0-9])", haystack) is not None


def _has_governance_control_event(haystack: str) -> bool:
    direct_event_tokens = (
        "tender offer",
        "control premium",
        "hostile takeover",
        "activist",
        "공개매수",
        "경영권 분쟁",
        "경영권 인수",
        "최대주주 변경",
        "지배권",
    )
    if _has_any(haystack, direct_event_tokens):
        return True
    governance_tokens = ("governance", "지배구조")
    event_qualifiers = (
        "reform",
        "takeover",
        "premium",
        "activist",
        "개편",
        "분쟁",
        "공개매수",
        "경영권",
    )
    return _has_any(haystack, governance_tokens) and _has_any(haystack, event_qualifiers)


def _has_bio_healthcare_metadata_or_context(metadata_haystack: str, haystack: str) -> bool:
    return _has_bio_healthcare_metadata(metadata_haystack) or _has_any(
        haystack,
        ("바이오시밀러", "항암제", "치료제", "임상", "품목허가", "식약처", "fda", "clinical", "biosimilar"),
    )


def _has_bio_healthcare_metadata(metadata_haystack: str) -> bool:
    return _has_any(metadata_haystack, ("biotech", "bio", "바이오", "제약", "healthcare", "헬스케어"))


def _classify_bio_healthcare_context(haystack: str) -> str | None:
    if _has_any(haystack, ("approval", "fda", "regulatory", "commercialization", "승인", "허가", "품목허가")):
        return "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION"
    if _has_any(haystack, ("trial", "phase", "임상", "data event", "clinical")):
        return "C24_BIO_TRIAL_DATA_EVENT_RISK"
    if _has_any(haystack, ("medical device", "의료기기", "reimbursement", "procedure", "시술")):
        return "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT"
    return None


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


def _has_ev_token(haystack: str) -> bool:
    return re.search(r"(?<![a-z0-9])ev(?![a-z0-9])", haystack) is not None


def _has_nearby_pair(haystack: str, left_tokens: tuple[str, ...], right_tokens: tuple[str, ...], *, window: int = 180) -> bool:
    for left in left_tokens:
        start = haystack.find(left)
        while start >= 0:
            excerpt = haystack[max(0, start - window) : start + len(left) + window]
            if any(right in excerpt for right in right_tokens):
                return True
            start = haystack.find(left, start + len(left))
    return False


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
