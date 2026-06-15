"""Sector-aware structural evidence profiles for E2R scoring.

The profiles keep Stage 3 discipline while avoiding one universal contract
gate for every business model. For example, transformer cases usually need
contracts/backlog, while K-food export cases can have visibility from export
channels and repeat consumer demand.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, Mapping, Sequence


class SectorProfile(str, Enum):
    """Domain profiles used for structural visibility scoring."""

    POWER_EQUIPMENT = "POWER_EQUIPMENT"
    DEFENSE = "DEFENSE"
    K_FOOD_EXPORT = "K_FOOD_EXPORT"
    K_BEAUTY_EXPORT = "K_BEAUTY_EXPORT"
    MEMORY_HBM = "MEMORY_HBM"
    CYCLICAL_SHIPPING = "CYCLICAL_SHIPPING"
    BATTERY_OVERHEAT = "BATTERY_OVERHEAT"
    AI_INFRA_PLATFORM = "AI_INFRA_PLATFORM"
    GENERIC = "GENERIC"


_PROFILE_IDS: dict[SectorProfile, int] = {
    SectorProfile.GENERIC: 0,
    SectorProfile.POWER_EQUIPMENT: 1,
    SectorProfile.DEFENSE: 2,
    SectorProfile.K_FOOD_EXPORT: 3,
    SectorProfile.K_BEAUTY_EXPORT: 4,
    SectorProfile.MEMORY_HBM: 5,
    SectorProfile.CYCLICAL_SHIPPING: 6,
    SectorProfile.BATTERY_OVERHEAT: 7,
    SectorProfile.AI_INFRA_PLATFORM: 8,
}
_ID_PROFILES = {value: key for key, value in _PROFILE_IDS.items()}


@dataclass(frozen=True)
class SectorProfileDefinition:
    """Evidence preferences for one sector profile."""

    profile: SectorProfile
    preferred_visibility_fields: tuple[str, ...]
    preferred_bottleneck_fields: tuple[str, ...]
    preferred_pricing_fields: tuple[str, ...]
    stage3_green_required_evidence_families: tuple[str, ...]
    red_team_risk_fields: tuple[str, ...]
    contract_required_for_green: bool = False


PROFILE_DEFINITIONS: Mapping[SectorProfile, SectorProfileDefinition] = {
    SectorProfile.POWER_EQUIPMENT: SectorProfileDefinition(
        profile=SectorProfile.POWER_EQUIPMENT,
        preferred_visibility_fields=(
            "contract_amount_to_prior_sales",
            "contract_duration_months",
            "order_backlog_to_sales",
            "record_backlog",
            "lead_time_extended",
            "capa_constraint",
        ),
        preferred_bottleneck_fields=(
            "lead_time_months",
            "capacity_constraint",
            "capa_shortage",
            "transformer_supply_shortage",
        ),
        preferred_pricing_fields=("asp_yoy_pct", "pricing_power_mentioned", "pricing_power_confirmed"),
        stage3_green_required_evidence_families=("disclosure", "research_report", "consensus_revision"),
        red_team_risk_fields=("contract_cancelled_or_delayed", "backlog_or_rpo_decline", "asp_decline"),
        contract_required_for_green=True,
    ),
    SectorProfile.DEFENSE: SectorProfileDefinition(
        profile=SectorProfile.DEFENSE,
        preferred_visibility_fields=(
            "order_backlog_to_sales",
            "multi_year_contract",
            "government_customer",
            "export_contract",
            "delivery_schedule",
        ),
        preferred_bottleneck_fields=("capacity_constraint", "delivery_schedule", "capa_constraint"),
        preferred_pricing_fields=("opm_expansion_pctp", "high_margin_mix_improvement"),
        stage3_green_required_evidence_families=("disclosure", "research_report", "consensus_revision"),
        red_team_risk_fields=("delivery_delay", "contract_cancelled_or_delayed", "cost_overrun"),
        contract_required_for_green=True,
    ),
    SectorProfile.K_FOOD_EXPORT: SectorProfileDefinition(
        profile=SectorProfile.K_FOOD_EXPORT,
        preferred_visibility_fields=(
            "export_ratio",
            "export_growth_pct",
            "export_channel_expansion",
            "overseas_channel_expansion",
            "recurring_consumer_demand",
            "opm_expansion_pctp",
        ),
        preferred_bottleneck_fields=("high_margin_mix_improvement", "brand_channel_expansion"),
        preferred_pricing_fields=("asp_yoy_pct", "price_increase_pct", "pricing_power_mentioned"),
        stage3_green_required_evidence_families=("research_report", "consensus_revision", "financial_actual"),
        red_team_risk_fields=("single_product_risk", "trend_fade_risk", "raw_material_cost_risk"),
        contract_required_for_green=False,
    ),
    SectorProfile.K_BEAUTY_EXPORT: SectorProfileDefinition(
        profile=SectorProfile.K_BEAUTY_EXPORT,
        preferred_visibility_fields=(
            "export_growth_pct",
            "platform_distribution_scale",
            "brand_customer_diversification",
            "export_channel_expansion",
            "overseas_channel_expansion",
            "recurring_consumer_demand",
        ),
        preferred_bottleneck_fields=("platform_distribution_scale", "brand_channel_expansion"),
        preferred_pricing_fields=("high_margin_mix_improvement", "pricing_power_mentioned"),
        stage3_green_required_evidence_families=("research_report", "consensus_revision", "financial_actual"),
        red_team_risk_fields=("single_channel_risk", "platform_fee_risk", "inventory_spike"),
        contract_required_for_green=False,
    ),
    SectorProfile.MEMORY_HBM: SectorProfileDefinition(
        profile=SectorProfile.MEMORY_HBM,
        preferred_visibility_fields=(
            "hbm_demand_mentioned",
            "memory_price_increase_mentioned",
            "supply_discipline_mentioned",
            "medium_term_revision_visibility",
            "customer_preorder_or_allocation",
        ),
        preferred_bottleneck_fields=("hbm_capacity_constraint", "advanced_packaging_bottleneck", "capa_constraint"),
        preferred_pricing_fields=("memory_price_increase_mentioned", "pricing_power_mentioned", "asp_yoy_pct"),
        stage3_green_required_evidence_families=("research_report", "consensus_revision", "financial_actual"),
        red_team_risk_fields=("memory_price_decline", "customer_capex_decline", "supply_glut"),
        contract_required_for_green=False,
    ),
    SectorProfile.CYCLICAL_SHIPPING: SectorProfileDefinition(
        profile=SectorProfile.CYCLICAL_SHIPPING,
        preferred_visibility_fields=("freight_rate_increase", "contract_rate", "capacity_discipline"),
        preferred_bottleneck_fields=("vessel_shortage", "port_congestion"),
        preferred_pricing_fields=("freight_rate_increase",),
        stage3_green_required_evidence_families=("research_report", "financial_actual", "news"),
        red_team_risk_fields=("freight_rate_decline", "capacity_addition", "one_off_shortage"),
        contract_required_for_green=False,
    ),
    SectorProfile.BATTERY_OVERHEAT: SectorProfileDefinition(
        profile=SectorProfile.BATTERY_OVERHEAT,
        preferred_visibility_fields=("contract_amount_to_prior_sales", "order_backlog_to_sales"),
        preferred_bottleneck_fields=("raw_material_bottleneck",),
        preferred_pricing_fields=("asp_yoy_pct",),
        stage3_green_required_evidence_families=("disclosure", "research_report", "consensus_revision"),
        red_team_risk_fields=("theme_overheat_score", "valuation_overheat", "customer_capex_decline"),
        contract_required_for_green=True,
    ),
    SectorProfile.AI_INFRA_PLATFORM: SectorProfileDefinition(
        profile=SectorProfile.AI_INFRA_PLATFORM,
        preferred_visibility_fields=(
            "gpu_cloud_revenue_visible",
            "cloud_revenue_growth_pct",
            "ai_infra_backlog_or_rpo",
            "hyperscaler_customer",
            "data_center_contract",
            "theme_business_link_mentioned",
            "rpo_to_sales",
        ),
        preferred_bottleneck_fields=(
            "gpu_allocation_mentioned",
            "ai_infra_capacity_or_gpu_mentioned",
            "datacenter_capacity_constraint",
            "power_capacity_constraint",
        ),
        preferred_pricing_fields=("gpu_cloud_margin_visible", "cloud_arpu_improvement", "opm_expansion_pctp"),
        stage3_green_required_evidence_families=("research_report", "financial_actual", "disclosure"),
        red_team_risk_fields=("capex_burden_risk", "ai_theme_hype_without_revenue", "gpu_supply_dependency"),
        contract_required_for_green=False,
    ),
    SectorProfile.GENERIC: SectorProfileDefinition(
        profile=SectorProfile.GENERIC,
        preferred_visibility_fields=("contract_quality", "backlog_rpo_visibility", "medium_term_revision_visibility"),
        preferred_bottleneck_fields=("capa_constraint", "asp_pricing_power", "structural_shortage"),
        preferred_pricing_fields=("asp_yoy_pct", "pricing_power_mentioned"),
        stage3_green_required_evidence_families=("research_report", "consensus_revision", "disclosure"),
        red_team_risk_fields=("one_off_shortage", "valuation_overheat", "contract_cancelled_or_delayed"),
        contract_required_for_green=False,
    ),
}


def profile_id(profile: SectorProfile) -> float:
    """Return numeric ID safe for ``ScoreSnapshot.diagnostic_scores``."""

    return float(_PROFILE_IDS[profile])


def profile_from_id(value: float | int | None) -> SectorProfile:
    """Decode numeric profile ID stored in diagnostics."""

    if value is None:
        return SectorProfile.GENERIC
    return _ID_PROFILES.get(int(value), SectorProfile.GENERIC)


def infer_sector_profile(
    *,
    symbol: str | None = None,
    company_name: str | None = None,
    sector_custom: str | None = None,
    text: str | None = None,
    parsed_fields: Mapping[str, Any] | None = None,
) -> SectorProfile:
    """Infer sector profile from metadata and explicit evidence text.

    This function uses only company/source context available to the pipeline.
    Benchmark labels are intentionally not imported or consulted.
    """

    del symbol  # symbol-specific benchmark lookups are deliberately avoided.
    parsed_fields = parsed_fields or {}
    if (
        any(key in parsed_fields for key in ("lead_time_months", "lead_time_extended", "capa_utilization_pct"))
        and any(key in parsed_fields for key in ("order_backlog_to_sales", "rpo_to_sales", "backlog_to_sales"))
    ):
        return SectorProfile.POWER_EQUIPMENT
    haystack = " ".join(
        str(part or "")
        for part in (
            company_name,
            sector_custom,
            text,
            " ".join(str(key) for key, value in parsed_fields.items() if bool(value)),
        )
    ).lower()
    metadata_haystack = f"{company_name or ''} {sector_custom or ''}".lower()

    platform_context = _has_ai_platform_context(haystack, parsed_fields, metadata_haystack=metadata_haystack)
    memory_context = _has_structured_memory_context(parsed_fields) or _has_memory_hbm_context(haystack)
    power_context = _has_power_equipment_context(haystack)
    defense_context = _has_defense_context(haystack, parsed_fields)
    metadata_prefers_holding = _metadata_prefers_holding_profile(metadata_haystack)
    metadata_prefers_memory = _metadata_prefers_memory_profile(metadata_haystack)
    metadata_prefers_power = _metadata_prefers_power_profile(metadata_haystack)
    metadata_blocks_ai_infra = _metadata_blocks_ai_infra_profile(metadata_haystack)
    mobility_business_context = _has_mobility_business_context(haystack)

    if metadata_prefers_holding:
        return SectorProfile.GENERIC
    if _metadata_prefers_ai_platform_profile(metadata_haystack) and platform_context:
        return SectorProfile.AI_INFRA_PLATFORM
    if metadata_prefers_memory and memory_context:
        return SectorProfile.MEMORY_HBM
    if metadata_prefers_power and power_context:
        return SectorProfile.POWER_EQUIPMENT
    if (
        memory_context
        and platform_context
        and _structured_memory_context_outweighs_platform_noise(parsed_fields, haystack, metadata_haystack)
        and not _metadata_blocks_memory_profile(metadata_haystack)
    ):
        return SectorProfile.MEMORY_HBM
    if platform_context and not metadata_blocks_ai_infra:
        return SectorProfile.AI_INFRA_PLATFORM
    if defense_context and not _metadata_blocks_defense_profile(metadata_haystack):
        return SectorProfile.DEFENSE
    if memory_context and not _metadata_blocks_memory_profile(metadata_haystack):
        return SectorProfile.MEMORY_HBM
    if power_context and not _metadata_blocks_power_profile(metadata_haystack):
        return SectorProfile.POWER_EQUIPMENT
    if any(token in haystack for token in ("불닭", "라면", "k-food", "k푸드", "k-푸드")) and not _metadata_blocks_consumer_profile(
        metadata_haystack
    ):
        return SectorProfile.K_FOOD_EXPORT
    if any(token in haystack for token in ("화장품", "뷰티", "k-beauty", "k뷰티", "k-뷰티", "beauty")) and not _metadata_blocks_consumer_profile(
        metadata_haystack
    ):
        return SectorProfile.K_BEAUTY_EXPORT
    if any(token in haystack for token in ("해운", "운임", "scfi", "shipping")):
        return SectorProfile.CYCLICAL_SHIPPING
    if (
        any(token in haystack for token in ("2차전지", "배터리", "양극재", "battery"))
        and not _metadata_blocks_battery_profile(metadata_haystack)
        and not mobility_business_context
    ):
        return SectorProfile.BATTERY_OVERHEAT
    if _has_ai_infra_context(haystack) and not _metadata_blocks_ai_infra_profile(metadata_haystack):
        return SectorProfile.AI_INFRA_PLATFORM
    return SectorProfile.GENERIC


def _has_ai_platform_context(haystack: str, parsed_fields: Mapping[str, Any], *, metadata_haystack: str) -> bool:
    platform_tokens = (
        "ad revenue",
        "advertising",
        "하이퍼클로바",
        "hyperclova",
        "소버린 ai",
        "sovereign ai",
        "gpu cloud",
        "gpu 클라우드",
        "클라우드 매출",
        "cloud revenue",
        "ai 매출",
        "ai revenue",
        "cloud_revenue_growth_pct",
        "gpu_cloud_revenue_visible",
        "cloud_arpu_improvement",
    )
    if any(token in haystack for token in platform_tokens):
        return True
    metadata_platform = any(
        token in metadata_haystack
        for token in ("platform", "플랫폼", "internet", "인터넷", "portal", "포털")
    )
    if metadata_platform and any(
        token in haystack
        for token in (
            "검색",
            "광고",
            "커머스",
            "commerce",
            "webtoon",
            "웹툰",
            "클라우드 매출",
            "cloud revenue",
            "gpu cloud",
            "gpu 클라우드",
            "하이퍼클로바",
            "hyperclova",
            "소버린 ai",
            "sovereign ai",
        )
    ):
        return True
    return any(
        parsed_fields.get(key) not in (None, "", False, 0)
        for key in (
            "gpu_cloud_revenue_visible",
            "cloud_revenue_growth_pct",
            "cloud_revenue_growth_visible",
            "cloud_arpu_improvement",
        )
    )


def _metadata_prefers_ai_platform_profile(metadata_haystack: str) -> bool:
    return any(
        token in metadata_haystack
        for token in (
            "platform",
            "플랫폼",
            "internet",
            "인터넷",
            "portal",
            "포털",
            "software",
            "소프트웨어",
            "content",
            "콘텐츠",
            "검색",
            "광고",
            "커머스",
        )
    )


def _structured_memory_context_outweighs_platform_noise(
    parsed_fields: Mapping[str, Any],
    haystack: str,
    metadata_haystack: str,
) -> bool:
    if _metadata_prefers_ai_platform_profile(metadata_haystack):
        return False
    structured_memory_keys = (
        "hbm_demand_mentioned",
        "hbm_capacity_constraint",
        "memory_price_increase_mentioned",
        "supply_discipline_mentioned",
        "customer_preorder_or_allocation",
    )
    structured_hits = sum(1 for key in structured_memory_keys if parsed_fields.get(key) not in (None, "", False, 0))
    if structured_hits >= 2:
        return True
    direct_memory_tokens = (
        "hbm",
        "high bandwidth memory",
        "고대역폭메모리",
        "고대역폭 메모리",
        "dram",
        "d램",
        "nand",
        "낸드",
        "메모리 가격",
        "memory price",
    )
    direct_hits = sum(1 for token in direct_memory_tokens if token in haystack)
    return structured_hits >= 1 and direct_hits >= 2


def _has_ai_infra_context(haystack: str) -> bool:
    return any(
        token in haystack
        for token in (
            "ai 인프라",
            "ai infra",
            "ai 데이터센터",
            "ai datacenter",
            "ai data center",
            "data_center_contract",
            "gpu cloud",
            "gpu 클라우드",
            "하이퍼클로바",
            "hyperclova",
            "소버린 ai",
            "sovereign ai",
        )
    )


def _has_memory_hbm_context(haystack: str) -> bool:
    if any(
        token in haystack
        for token in (
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
            "advanced packaging",
            "패키징",
            "후공정",
            "반도체 기판",
            "fc-bga",
            "fcbga",
            "mlcc",
            "커패시터",
            "실리콘 커패시터",
        )
    ):
        return True
    return _has_semiconductor_industry_context(haystack)


def _has_structured_memory_context(parsed_fields: Mapping[str, Any]) -> bool:
    return any(
        parsed_fields.get(key) not in (None, "", False, 0)
        for key in (
            "hbm_demand_mentioned",
            "hbm_capacity_constraint",
            "memory_price_increase_mentioned",
            "supply_discipline_mentioned",
            "customer_preorder_or_allocation",
        )
    )


def _has_power_equipment_context(haystack: str) -> bool:
    return any(
        token in haystack
        for token in (
            "변압기",
            "전력기기",
            "초고압",
            "전선",
            "케이블",
            "전력망",
            "grid",
            "transformer",
            "power equipment",
            "power_equipment",
            "중공업",
        )
    )


def _has_defense_context(haystack: str, parsed_fields: Mapping[str, Any]) -> bool:
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


def _metadata_blocks_ai_infra_profile(metadata_haystack: str) -> bool:
    return any(
        token in metadata_haystack
        for token in (
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
            "semiconductor",
            "반도체",
            "electronics",
            "전기전자",
            "holding",
            "지주",
        )
    )


def _metadata_prefers_power_profile(metadata_haystack: str) -> bool:
    return any(
        token in metadata_haystack
        for token in ("power_equipment", "전력기기", "전력", "원전", "nuclear", "smr", "electric", "일렉트릭", "전기")
    )


def _metadata_prefers_holding_profile(metadata_haystack: str) -> bool:
    return any(token in metadata_haystack for token in ("holding", "지주", "investment", "투자회사", "투자 회사"))


def _metadata_prefers_memory_profile(metadata_haystack: str) -> bool:
    return any(token in metadata_haystack for token in ("semiconductor", "반도체", "electronics", "전기전자"))


def _metadata_blocks_memory_profile(metadata_haystack: str) -> bool:
    return any(
        token in metadata_haystack
        for token in (
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
            "holding",
            "지주",
        )
    )


def _has_semiconductor_industry_context(haystack: str) -> bool:
    if "반도체" not in haystack and "semiconductor" not in haystack:
        return False
    industry_terms = (
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
    )
    return _has_nearby_pair(haystack, ("반도체", "semiconductor"), industry_terms)


def _has_mobility_business_context(haystack: str) -> bool:
    return any(
        token in haystack
        for token in (
            "완성차",
            "자동차 판매",
            "차량 판매",
            "글로벌 도매",
            "도매 판매",
            "판매대수",
            "제네시스",
            "하이브리드",
            "suv",
            "auto sales",
            "vehicle sales",
            "wholesale volume",
            "model mix",
        )
    )


def _metadata_blocks_power_profile(metadata_haystack: str) -> bool:
    return any(
        token in metadata_haystack
        for token in (
            "semiconductor",
            "반도체",
            "electronics",
            "전기전자",
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
            "holding",
            "지주",
        )
    )


def _metadata_blocks_battery_profile(metadata_haystack: str) -> bool:
    return any(
        token in metadata_haystack
        for token in (
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
            "holding",
            "지주",
        )
    )


def _metadata_blocks_defense_profile(metadata_haystack: str) -> bool:
    return any(
        token in metadata_haystack
        for token in (
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
            "semiconductor",
            "반도체",
            "electronics",
            "전기전자",
            "holding",
            "지주",
        )
    )


def _metadata_blocks_consumer_profile(metadata_haystack: str) -> bool:
    return any(
        token in metadata_haystack
        for token in (
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
            "semiconductor",
            "반도체",
            "electronics",
            "전기전자",
            "power_equipment",
            "전력기기",
            "holding",
            "지주",
        )
    )


def _has_nearby_pair(haystack: str, left_tokens: tuple[str, ...], right_tokens: tuple[str, ...], *, window: int = 180) -> bool:
    for left in left_tokens:
        start = haystack.find(left)
        while start >= 0:
            excerpt = haystack[max(0, start - window) : start + len(left) + window]
            if any(right in excerpt for right in right_tokens):
                return True
            start = haystack.find(left, start + len(left))
    return False


def definition_for(profile: SectorProfile) -> SectorProfileDefinition:
    """Return profile definition."""

    return PROFILE_DEFINITIONS[profile]


def profile_name_from_diagnostic(value: float | int | None) -> str:
    """Return a stable profile name from a numeric diagnostic value."""

    return profile_from_id(value).value


def field_presence_score(parsed_fields: Mapping[str, Any], fields: Sequence[str], *, points_each: float = 20.0) -> float:
    """Score bounded qualitative field presence."""

    score = 0.0
    for key in fields:
        value = parsed_fields.get(key)
        if value not in (None, "", False, 0):
            score += points_each
    return min(100.0, score)


__all__ = [
    "PROFILE_DEFINITIONS",
    "SectorProfile",
    "SectorProfileDefinition",
    "definition_for",
    "field_presence_score",
    "infer_sector_profile",
    "profile_from_id",
    "profile_id",
    "profile_name_from_diagnostic",
]
