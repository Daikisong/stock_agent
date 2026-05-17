"""Round-10 theme tag taxonomy.

Round 10 separates raw market themes from production scoring. Theme tags help
search, routing, and coverage reports, while canonical archetypes remain the
score owners. This module is calibration/report material only.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Iterable, Mapping

from e2r.sector.archetypes import E2RArchetype


ROUND10_SOURCE_ROUND_PATH = "docs/round/round_10.md"


class Round10LargeSector(str, Enum):
    """Twelve top-level buckets from Round 10."""

    INDUSTRIAL_ORDERS_INFRA = "INDUSTRIAL_ORDERS_INFRA"
    AI_SEMICONDUCTOR_ELECTRONICS = "AI_SEMICONDUCTOR_ELECTRONICS"
    BATTERY_EV_GREEN = "BATTERY_EV_GREEN"
    MATERIALS_SPREAD_STRATEGIC = "MATERIALS_SPREAD_STRATEGIC"
    CONSUMER_RETAIL_BRAND = "CONSUMER_RETAIL_BRAND"
    FINANCIAL_CAPITAL_DIGITAL = "FINANCIAL_CAPITAL_DIGITAL"
    BIOTECH_HEALTHCARE_DEVICE = "BIOTECH_HEALTHCARE_DEVICE"
    PLATFORM_CONTENT_SW_SECURITY = "PLATFORM_CONTENT_SW_SECURITY"
    MOBILITY_TRANSPORT_LEISURE = "MOBILITY_TRANSPORT_LEISURE"
    CONSTRUCTION_REAL_ESTATE_MATERIALS = "CONSTRUCTION_REAL_ESTATE_MATERIALS"
    POLICY_GEOPOLITICAL_EVENT = "POLICY_GEOPOLITICAL_EVENT"
    EDUCATION_LIFE_AGRI_MISC = "EDUCATION_LIFE_AGRI_MISC"


class Round10ThemePosture(str, Enum):
    """How a sub-archetype may be treated in future scoring design."""

    GREEN_POSSIBLE = "GREEN_POSSIBLE"
    WATCH_YELLOW_FIRST = "WATCH_YELLOW_FIRST"
    REDTEAM_FIRST = "REDTEAM_FIRST"


@dataclass(frozen=True)
class Round10LargeSectorDefinition:
    large_sector: Round10LargeSector
    korean_name: str
    description: str


@dataclass(frozen=True)
class Round10ThemeArchetype:
    """Theme-level sub-archetype mapped to one canonical score owner."""

    label: str
    large_sector: Round10LargeSector
    canonical_archetype: E2RArchetype
    theme_tags: tuple[str, ...]
    posture: Round10ThemePosture
    must_have_evidence: tuple[str, ...]
    green_policy: str

    @property
    def theme_is_score_input(self) -> bool:
        return False


ROUND10_LARGE_SECTORS: Mapping[Round10LargeSector, Round10LargeSectorDefinition] = {
    Round10LargeSector.INDUSTRIAL_ORDERS_INFRA: Round10LargeSectorDefinition(
        Round10LargeSector.INDUSTRIAL_ORDERS_INFRA,
        "산업재·수주·인프라",
        "전력설비, 전선, 방산, 조선, 건설기계, 피팅밸브, 원전, 철도",
    ),
    Round10LargeSector.AI_SEMICONDUCTOR_ELECTRONICS: Round10LargeSectorDefinition(
        Round10LargeSector.AI_SEMICONDUCTOR_ELECTRONICS,
        "AI·반도체·전자부품",
        "HBM, CXL, 시스템반도체, PCB, OLED, MLCC, 유리기판, 클린룸, 스마트폰 부품",
    ),
    Round10LargeSector.BATTERY_EV_GREEN: Round10LargeSectorDefinition(
        Round10LargeSector.BATTERY_EV_GREEN,
        "2차전지·전기차·친환경",
        "2차전지 소재/부품/장비, 전고체, 폐배터리, 전기차 인프라, 수소, 태양광, 풍력",
    ),
    Round10LargeSector.MATERIALS_SPREAD_STRATEGIC: Round10LargeSectorDefinition(
        Round10LargeSector.MATERIALS_SPREAD_STRATEGIC,
        "소재·스프레드·전략자원",
        "화학, 정유, 철강, 비철금속, 리튬, 희토류, 구리, 금은, 페라이트",
    ),
    Round10LargeSector.CONSUMER_RETAIL_BRAND: Round10LargeSectorDefinition(
        Round10LargeSector.CONSUMER_RETAIL_BRAND,
        "소비재·유통·브랜드",
        "편의점, 홈쇼핑, 라면, K푸드, 음식료, 화장품, 의류, 건강기능식품",
    ),
    Round10LargeSector.FINANCIAL_CAPITAL_DIGITAL: Round10LargeSectorDefinition(
        Round10LargeSector.FINANCIAL_CAPITAL_DIGITAL,
        "금융·자본배분·디지털금융",
        "은행, 보험, 증권, 금융지주, 고배당, 밸류업, 결제, STO, 스테이블코인",
    ),
    Round10LargeSector.BIOTECH_HEALTHCARE_DEVICE: Round10LargeSectorDefinition(
        Round10LargeSector.BIOTECH_HEALTHCARE_DEVICE,
        "바이오·헬스케어·의료기기",
        "CMO, CRO, 바이오시밀러, 임상, 의료AI, 미용기기, 보톡스, 임플란트, 진단",
    ),
    Round10LargeSector.PLATFORM_CONTENT_SW_SECURITY: Round10LargeSectorDefinition(
        Round10LargeSector.PLATFORM_CONTENT_SW_SECURITY,
        "플랫폼·콘텐츠·SW·보안",
        "게임, 엔터, 미디어, 클라우드, AI, IT보안, 딥페이크, 메타버스, NFT",
    ),
    Round10LargeSector.MOBILITY_TRANSPORT_LEISURE: Round10LargeSectorDefinition(
        Round10LargeSector.MOBILITY_TRANSPORT_LEISURE,
        "모빌리티·운송·레저",
        "항공, 해운, 택배, 렌터카, 중고차, 여행, 카지노, 면세, 골프",
    ),
    Round10LargeSector.CONSTRUCTION_REAL_ESTATE_MATERIALS: Round10LargeSectorDefinition(
        Round10LargeSector.CONSTRUCTION_REAL_ESTATE_MATERIALS,
        "건설·부동산·건자재",
        "대형/중소형 건설, 리츠, 개발신탁, 건자재, 시멘트, 철근, 가구",
    ),
    Round10LargeSector.POLICY_GEOPOLITICAL_EVENT: Round10LargeSectorDefinition(
        Round10LargeSector.POLICY_GEOPOLITICAL_EVENT,
        "정책·지정학·재난·이벤트",
        "남북경협, 우크라 재건, 네옴시티, 세종시, 지진, 폭염, 황사, 전염병",
    ),
    Round10LargeSector.EDUCATION_LIFE_AGRI_MISC: Round10LargeSectorDefinition(
        Round10LargeSector.EDUCATION_LIFE_AGRI_MISC,
        "교육·생활서비스·농수축산",
        "교육, 취업, 키즈, 유아용품, 스마트팜, 농기계, 양돈, 육계, 배합사료, 참치",
    ),
}


def _theme(
    label: str,
    large_sector: Round10LargeSector,
    canonical: E2RArchetype,
    tags: tuple[str, ...],
    posture: Round10ThemePosture,
    evidence: tuple[str, ...],
    policy: str,
) -> Round10ThemeArchetype:
    return Round10ThemeArchetype(
        label=label,
        large_sector=large_sector,
        canonical_archetype=canonical,
        theme_tags=tags,
        posture=posture,
        must_have_evidence=evidence,
        green_policy=policy,
    )


ROUND10_THEME_ARCHETYPES: tuple[Round10ThemeArchetype, ...] = (
    _theme("CONTRACT_BACKLOG_INDUSTRIAL", Round10LargeSector.INDUSTRIAL_ORDERS_INFRA, E2RArchetype.CONTRACT_BACKLOG_INDUSTRIAL, ("전력설비", "전선-케이블", "강관", "피팅 밸브", "건설기계", "조선 기자재", "LNG선 기자재"), Round10ThemePosture.GREEN_POSSIBLE, ("contract_or_order", "backlog", "op_eps_revision", "margin_visibility"), "Green only with contract quality, backlog, margin path, and low cancellation risk."),
    _theme("AI_DATA_CENTER_INFRASTRUCTURE", Round10LargeSector.INDUSTRIAL_ORDERS_INFRA, E2RArchetype.AI_DATA_CENTER_INFRASTRUCTURE, ("전력설비", "전선", "광섬유", "광케이블", "광통신", "냉각시스템", "클린룸", "AI 데이터센터"), Round10ThemePosture.GREEN_POSSIBLE, ("confirmed_order", "data_center_capex", "capacity_bottleneck", "op_eps_revision"), "AI tag alone is not evidence; orders and revision support are required."),
    _theme("DEFENSE_GOVERNMENT_BACKLOG", Round10LargeSector.INDUSTRIAL_ORDERS_INFRA, E2RArchetype.DEFENSE_GOVERNMENT_BACKLOG, ("방위산업", "항공우주", "드론", "플라잉카", "스페이스X 관련주"), Round10ThemePosture.GREEN_POSSIBLE, ("government_customer", "multi_year_contract", "delivery_schedule", "op_eps_revision"), "Government backlog can support Green only when delivery and margin visibility are real."),
    _theme("SHIPBUILDING_OFFSHORE_BACKLOG", Round10LargeSector.INDUSTRIAL_ORDERS_INFRA, E2RArchetype.SHIPBUILDING_OFFSHORE_BACKLOG, ("조선", "조선 기자재", "LNG선 기자재", "엔진", "피팅밸브"), Round10ThemePosture.GREEN_POSSIBLE, ("orderbook_quality", "newbuild_price", "low_margin_backlog_clearance", "op_revision"), "Shipbuilding needs order quality and margin conversion, not backlog headline only."),
    _theme("NUCLEAR_SMR_GRID_POLICY", Round10LargeSector.INDUSTRIAL_ORDERS_INFRA, E2RArchetype.NUCLEAR_SMR_GRID_POLICY, ("원자력", "원전", "SMR", "스마트그리드", "전력망"), Round10ThemePosture.WATCH_YELLOW_FIRST, ("binding_contract", "permitted_project_timeline", "supplier_revenue_visibility"), "Policy headlines stay Watch/Yellow until contract economics are binding."),
    _theme("RAIL_INFRASTRUCTURE", Round10LargeSector.INDUSTRIAL_ORDERS_INFRA, E2RArchetype.CONTRACT_BACKLOG_INDUSTRIAL, ("철도", "우크라 재건", "네옴시티", "대형 인프라"), Round10ThemePosture.WATCH_YELLOW_FIRST, ("funded_project", "confirmed_order", "margin_visibility"), "Infrastructure themes need funded projects and supplier revenue evidence."),
    _theme("SMART_FACTORY_AUTOMATION", Round10LargeSector.INDUSTRIAL_ORDERS_INFRA, E2RArchetype.ROBOTICS_FACTORY_AUTOMATION, ("제조용 로봇", "스마트팩토리", "컨택센터", "키오스크"), Round10ThemePosture.WATCH_YELLOW_FIRST, ("customer_adoption", "revenue_conversion", "opm_improvement"), "Automation themes need revenue conversion before high-conviction scoring."),
    _theme("MEMORY_HBM_CAPACITY", Round10LargeSector.AI_SEMICONDUCTOR_ELECTRONICS, E2RArchetype.MEMORY_HBM_CAPACITY, ("HBM", "반도체-HBM", "종합반도체", "CXL", "뉴로모픽 반도체"), Round10ThemePosture.GREEN_POSSIBLE, ("memory_price", "hbm_demand", "supply_discipline", "medium_term_revision"), "HBM/memory Green needs EPS path and capacity or price evidence."),
    _theme("SEMI_EQUIPMENT_CAPEX", Round10LargeSector.AI_SEMICONDUCTOR_ELECTRONICS, E2RArchetype.SEMI_EQUIPMENT_CAPEX, ("반도체 전공정 장비", "반도체 후공정 장비", "2차전지 공정장비"), Round10ThemePosture.GREEN_POSSIBLE, ("customer_capex", "orders", "revenue_conversion", "customer_diversification"), "Equipment themes need customer capex and order conversion."),
    _theme("SEMI_MATERIALS_PROCESS", Round10LargeSector.AI_SEMICONDUCTOR_ELECTRONICS, E2RArchetype.SEMI_EQUIPMENT_CAPEX, ("반도체 전공정 소재", "반도체 후공정 소재", "클린룸", "OLED 소재부품"), Round10ThemePosture.WATCH_YELLOW_FIRST, ("customer_qualification", "volume_ramp", "margin_visibility"), "Process materials need qualification and volume ramp evidence."),
    _theme("ADVANCED_PACKAGING_PCB", Round10LargeSector.AI_SEMICONDUCTOR_ELECTRONICS, E2RArchetype.SEMI_EQUIPMENT_CAPEX, ("PCB", "인쇄회로기판", "CXL", "유리기판", "후공정", "AI 서버 PCB"), Round10ThemePosture.GREEN_POSSIBLE, ("ai_server_demand", "order_visibility", "capacity_constraint", "op_eps_revision"), "PCB/packaging can be Green-eligible with AI server demand and order conversion."),
    _theme("DISPLAY_OLED_EQUIPMENT", Round10LargeSector.AI_SEMICONDUCTOR_ELECTRONICS, E2RArchetype.SEMI_EQUIPMENT_CAPEX, ("OLED 장비", "OLED 소재부품", "디스플레이 이송장비"), Round10ThemePosture.WATCH_YELLOW_FIRST, ("panel_capex", "orders", "margin_visibility"), "Display capex is cyclical; Green needs durable orders and margin support."),
    _theme("ELECTRONIC_COMPONENTS", Round10LargeSector.AI_SEMICONDUCTOR_ELECTRONICS, E2RArchetype.AUTO_MOBILITY_COMPONENTS, ("MLCC", "카메라", "스마트폰 부품", "무선충전", "LED"), Round10ThemePosture.WATCH_YELLOW_FIRST, ("customer_diversification", "content_growth", "margin_improvement"), "Component tags need content growth and margin proof."),
    _theme("AI_CHIP_FABRIC_INFRA", Round10LargeSector.AI_SEMICONDUCTOR_ELECTRONICS, E2RArchetype.AI_DATA_CENTER_INFRASTRUCTURE, ("퓨리오사AI 관련주", "인공지능 AI", "시스템반도체", "뉴로모픽 반도체"), Round10ThemePosture.REDTEAM_FIRST, ("direct_exposure", "orders_or_revenue", "revision_support"), "AI-chip association without exposure is theme risk, not scoring evidence."),
    _theme("CYBER_AI_SECURITY", Round10LargeSector.AI_SEMICONDUCTOR_ELECTRONICS, E2RArchetype.PLATFORM_SOFTWARE_INTERNET, ("IT보안", "딥페이크", "생체인식", "CCTV"), Round10ThemePosture.WATCH_YELLOW_FIRST, ("recurring_revenue", "security_demand", "opm_leverage"), "Security themes need recurring revenue and monetization evidence."),
    _theme("BATTERY_MATERIALS_CAPEX_OVERHEAT", Round10LargeSector.BATTERY_EV_GREEN, E2RArchetype.BATTERY_MATERIALS_CAPEX_OVERHEAT, ("2차전지 소재", "2차전지 생산·판매", "전고체 배터리", "리튬", "폐배터리"), Round10ThemePosture.REDTEAM_FIRST, ("contract_quality", "price_pass_through", "demand_visibility", "fcf_after_capex"), "Battery materials are Green-restricted until contract, margin, and demand risks are controlled."),
    _theme("BATTERY_EQUIPMENT_PARTS", Round10LargeSector.BATTERY_EV_GREEN, E2RArchetype.BATTERY_MATERIALS_CAPEX_OVERHEAT, ("2차전지 공정장비", "2차전지 부품", "전기차 부품"), Round10ThemePosture.WATCH_YELLOW_FIRST, ("customer_orders", "capex_visibility", "margin_visibility"), "Battery equipment depends on customer capex; order delays are 4C risks."),
    _theme("EV_INFRASTRUCTURE", Round10LargeSector.BATTERY_EV_GREEN, E2RArchetype.AUTO_MOBILITY_COMPONENTS, ("전기차 인프라", "전기차 화재", "무선충전", "충전소"), Round10ThemePosture.WATCH_YELLOW_FIRST, ("utilization", "policy_support", "recurring_revenue"), "EV infrastructure needs utilization and revenue, not installation headline only."),
    _theme("HYDROGEN_FUEL_CELL", Round10LargeSector.BATTERY_EV_GREEN, E2RArchetype.THEME_VALUATION_OVERHEAT, ("수소차 연료전지", "수소차 기타부품", "수소차 인프라"), Round10ThemePosture.REDTEAM_FIRST, ("commercial_revenue", "cost_curve", "policy_support"), "Hydrogen stays RedTeam-first until commercial economics are visible."),
    _theme("RENEWABLE_ENERGY_POLICY", Round10LargeSector.BATTERY_EV_GREEN, E2RArchetype.UTILITIES_REGULATED_TARIFF, ("태양광", "풍력", "탄소배출권", "탈 플라스틱"), Round10ThemePosture.WATCH_YELLOW_FIRST, ("tariff_or_policy", "project_backlog", "margin_visibility"), "Renewable policy needs project economics and margin support."),
    _theme("ENERGY_DISTRIBUTION_FUEL", Round10LargeSector.BATTERY_EV_GREEN, E2RArchetype.COMMODITY_SPREAD, ("LNG 발전유통", "LPG", "유가 상승 수혜", "유류도소매", "윤활유"), Round10ThemePosture.WATCH_YELLOW_FIRST, ("spread", "inventory_status", "demand_visibility"), "Fuel distribution is spread/cycle driven and needs cyclicality caps."),
    _theme("CHEMICAL_SPREAD", Round10LargeSector.MATERIALS_SPREAD_STRATEGIC, E2RArchetype.COMMODITY_SPREAD, ("화학", "페인트", "탈 플라스틱", "주정"), Round10ThemePosture.REDTEAM_FIRST, ("product_spread", "inventory_status", "capacity_discipline"), "Chemical spread alone cannot create structural Green."),
    _theme("REFINING_OIL_SPREAD", Round10LargeSector.MATERIALS_SPREAD_STRATEGIC, E2RArchetype.COMMODITY_SPREAD, ("정유", "화학-정유", "윤활유", "LPG"), Round10ThemePosture.WATCH_YELLOW_FIRST, ("refining_margin", "inventory_status", "demand_visibility"), "Refining is cyclical; Green needs structural supply discipline."),
    _theme("STEEL_METAL_SPREAD", Round10LargeSector.MATERIALS_SPREAD_STRATEGIC, E2RArchetype.COMMODITY_SPREAD, ("철강 주요업체", "철강 중소형업체", "강관", "건자재 철근"), Round10ThemePosture.REDTEAM_FIRST, ("steel_spread", "china_supply", "inventory_status"), "Steel needs spread and supply discipline; China supply risk caps Green."),
    _theme("NONFERROUS_STRATEGIC_METALS", Round10LargeSector.MATERIALS_SPREAD_STRATEGIC, E2RArchetype.RARE_METALS_STRATEGIC_MATERIALS, ("비철금속", "구리", "리튬", "희토류", "금은", "페라이트"), Round10ThemePosture.WATCH_YELLOW_FIRST, ("metal_price", "cost_curve", "supply_constraint"), "Strategic metals need cost curve or supply evidence, not price spike only."),
    _theme("ADVANCED_MATERIAL_THEMES", Round10LargeSector.MATERIALS_SPREAD_STRATEGIC, E2RArchetype.THEME_VALUATION_OVERHEAT, ("그래핀", "맥신", "초전도체", "양자 기술", "페라이트"), Round10ThemePosture.REDTEAM_FIRST, ("commercial_revenue", "contract_or_order", "technical_validation"), "Speculative science tags are Green-blocked without commercialization evidence."),
    _theme("PAPER_PACKAGING", Round10LargeSector.MATERIALS_SPREAD_STRATEGIC, E2RArchetype.COMMODITY_SPREAD, ("제지", "골판지", "탈 플라스틱 포장재"), Round10ThemePosture.WATCH_YELLOW_FIRST, ("paper_spread", "demand_visibility", "cost_pass_through"), "Packaging is spread and demand driven; structural Green requires durable pricing power."),
    _theme("AGRI_COMMODITY_INPUTS", Round10LargeSector.MATERIALS_SPREAD_STRATEGIC, E2RArchetype.COMMODITY_SPREAD, ("대두", "배합사료", "농업 종자", "비료", "농약"), Round10ThemePosture.REDTEAM_FIRST, ("commodity_cost", "price_pass_through", "inventory_status"), "Agri inputs are cycle/event heavy and need RedTeam caps."),
    _theme("EXPORT_RECURRING_CONSUMER", Round10LargeSector.CONSUMER_RETAIL_BRAND, E2RArchetype.EXPORT_RECURRING_CONSUMER, ("라면", "K푸드", "음식료", "건강기능식품", "음식료 유통"), Round10ThemePosture.GREEN_POSSIBLE, ("export_growth", "channel_expansion", "recurring_demand", "fy1_fy2_revision"), "K-food Green does not require contracts but does require repeat demand and revision support."),
    _theme("FOOD_AGRI_LIVESTOCK_CYCLE", Round10LargeSector.CONSUMER_RETAIL_BRAND, E2RArchetype.COMMODITY_SPREAD, ("양돈주", "육계주", "참치 원양어업", "대두", "배합사료"), Round10ThemePosture.REDTEAM_FIRST, ("commodity_cycle", "feed_cost", "inventory_status"), "Food commodity cycles are capped; avoid structural extrapolation."),
    _theme("RETAIL_CONVENIENCE_OFFLINE", Round10LargeSector.CONSUMER_RETAIL_BRAND, E2RArchetype.RETAIL_DOMESTIC_CONSUMER, ("편의점", "홈쇼핑", "음식료 유통"), Round10ThemePosture.WATCH_YELLOW_FIRST, ("same_store_sales", "opm_improvement", "inventory_turnover"), "Offline retail needs store efficiency and margin evidence."),
    _theme("ECOMMERCE_FRESH_LOGISTICS", Round10LargeSector.CONSUMER_RETAIL_BRAND, E2RArchetype.PLATFORM_SOFTWARE_INTERNET, ("마켓컬리", "오아시스", "콜드체인", "택배", "종합물류"), Round10ThemePosture.WATCH_YELLOW_FIRST, ("unit_economics", "repeat_orders", "logistics_margin"), "Fresh e-commerce needs unit economics, not GMV headline only."),
    _theme("K_BEAUTY_EXPORT_DISTRIBUTION", Round10LargeSector.CONSUMER_RETAIL_BRAND, E2RArchetype.K_BEAUTY_EXPORT_DISTRIBUTION, ("화장품 브랜드", "K뷰티", "화장품 유통"), Round10ThemePosture.GREEN_POSSIBLE, ("export_growth", "channel_diversification", "repeat_orders", "opm_roe_improvement"), "K-beauty Green needs repeat export channel and inventory discipline."),
    _theme("BEAUTY_OEM_ODM_SUPPLYCHAIN", Round10LargeSector.CONSUMER_RETAIL_BRAND, E2RArchetype.K_BEAUTY_EXPORT_DISTRIBUTION, ("화장품 OEM", "화장품 ODM", "화장품 원재료", "화장품 부자재"), Round10ThemePosture.GREEN_POSSIBLE, ("customer_diversification", "capacity_utilization", "margin_visibility"), "Beauty supply chain needs customer and utilization evidence."),
    _theme("APPAREL_BRAND_OEM", Round10LargeSector.CONSUMER_RETAIL_BRAND, E2RArchetype.EXPORT_RECURRING_CONSUMER, ("의류 브랜드", "의류 OEM", "의류 ODM", "의류 소재"), Round10ThemePosture.WATCH_YELLOW_FIRST, ("order_visibility", "brand_momentum", "inventory_status"), "Apparel needs order and inventory evidence due fashion cycle risk."),
    _theme("HOME_LIVING_APPLIANCE", Round10LargeSector.CONSUMER_RETAIL_BRAND, E2RArchetype.RETAIL_DOMESTIC_CONSUMER, ("밥솥", "스마트홈", "유아용품", "키즈"), Round10ThemePosture.WATCH_YELLOW_FIRST, ("repeat_demand", "channel_expansion", "margin_visibility"), "Home/living tags need recurring demand and margin support."),
    _theme("FINANCIAL_SPREAD_BALANCE_SHEET", Round10LargeSector.FINANCIAL_CAPITAL_DIGITAL, E2RArchetype.FINANCIAL_SPREAD_BALANCE_SHEET, ("은행", "금융지주회사", "생명보험", "손해보험"), Round10ThemePosture.GREEN_POSSIBLE, ("roe", "pbr", "capital_ratio", "credit_cost"), "Financial Green needs ROE/PBR and balance-sheet quality."),
    _theme("INSURANCE_UNDERWRITING_CYCLE", Round10LargeSector.FINANCIAL_CAPITAL_DIGITAL, E2RArchetype.FINANCIAL_SPREAD_BALANCE_SHEET, ("손해보험", "생명보험", "화재", "고배당주"), Round10ThemePosture.GREEN_POSSIBLE, ("loss_ratio", "csm_or_capital", "shareholder_return", "credit_risk"), "Insurance needs underwriting and capital evidence."),
    _theme("SECURITIES_BROKERAGE_CYCLE", Round10LargeSector.FINANCIAL_CAPITAL_DIGITAL, E2RArchetype.FINANCIAL_SPREAD_BALANCE_SHEET, ("증권사", "벤처캐피탈", "VC"), Round10ThemePosture.WATCH_YELLOW_FIRST, ("brokerage_cycle", "ib_pipeline", "capital_risk"), "Brokerage cycles need market-cycle caps."),
    _theme("VALUE_UP_SHAREHOLDER_RETURN", Round10LargeSector.FINANCIAL_CAPITAL_DIGITAL, E2RArchetype.VALUE_UP_SHAREHOLDER_RETURN, ("밸류업", "밸류업 지수", "고배당주", "부동산 자산 보유"), Round10ThemePosture.GREEN_POSSIBLE, ("roe", "shareholder_return_execution", "capital_strength"), "Value-up tag alone is not evidence; execution matters."),
    _theme("PAYMENT_FINTECH_INFRA", Round10LargeSector.FINANCIAL_CAPITAL_DIGITAL, E2RArchetype.PLATFORM_SOFTWARE_INTERNET, ("결제서비스", "토스 관련주", "지역화폐", "신용정보"), Round10ThemePosture.WATCH_YELLOW_FIRST, ("transaction_volume", "take_rate", "regulatory_risk"), "Fintech needs transaction economics and regulation checks."),
    _theme("DIGITAL_ASSET_TOKENIZATION", Round10LargeSector.FINANCIAL_CAPITAL_DIGITAL, E2RArchetype.THEME_VALUATION_OVERHEAT, ("스테이블코인", "STO", "디지털자산", "블록체인", "NFT"), Round10ThemePosture.REDTEAM_FIRST, ("regulated_revenue", "license_or_partner", "cash_flow"), "Tokenization themes are Green-blocked without regulated revenue."),
    _theme("BIOTECH_PRE_REVENUE_REGULATORY", Round10LargeSector.BIOTECH_HEALTHCARE_DEVICE, E2RArchetype.BIOTECH_PRE_REVENUE_REGULATORY, ("치매치료", "희귀질환 치료제", "면역세포치료제", "줄기세포치료제", "이중항체"), Round10ThemePosture.REDTEAM_FIRST, ("clinical_milestone", "cash_runway", "dilution_risk"), "Pre-revenue biotech is not Green before revenue or royalty conversion."),
    _theme("BIOTECH_ROYALTY_COMMERCIALIZATION", Round10LargeSector.BIOTECH_HEALTHCARE_DEVICE, E2RArchetype.BIOTECH_ROYALTY_COMMERCIALIZATION, ("AI 신약개발", "비만 치료제", "탈모치료", "난임", "치매치료"), Round10ThemePosture.WATCH_YELLOW_FIRST, ("approval", "partner_launch", "royalty_or_revenue"), "Biotech can improve after commercialization evidence, not clinical headline alone."),
    _theme("CDMO_HEALTHCARE_CONTRACT", Round10LargeSector.BIOTECH_HEALTHCARE_DEVICE, E2RArchetype.CDMO_HEALTHCARE_CONTRACT, ("CMO", "원료의약품", "바이오시밀러", "CRO", "임상시험수탁"), Round10ThemePosture.GREEN_POSSIBLE, ("long_term_contract", "capacity_utilization", "customer_diversification", "fcf_conversion"), "CDMO is contract/utilization driven and separated from trial-stage biotech."),
    _theme("DIAGNOSTICS_INFECTIOUS_DISEASE", Round10LargeSector.BIOTECH_HEALTHCARE_DEVICE, E2RArchetype.ONE_OFF_EVENT_DEMAND, ("전염병 진단", "코로나19 제약", "엠폭스", "동물백신", "방역"), Round10ThemePosture.REDTEAM_FIRST, ("recurring_non_event_demand", "revenue_after_event", "margin_normalization"), "Infectious disease demand is one-off until recurring demand is proven."),
    _theme("MEDICAL_DEVICE_HEALTHCARE_EXPORT", Round10LargeSector.BIOTECH_HEALTHCARE_DEVICE, E2RArchetype.MEDICAL_DEVICE_HEALTHCARE_EXPORT, ("미용기기", "치아", "임플란트", "보툴리눔 톡신", "수술용 로봇"), Round10ThemePosture.GREEN_POSSIBLE, ("export_growth", "consumable_repeat_revenue", "regulatory_approval", "opm_roe_improvement"), "Medical device Green needs repeat revenue and export/channel support."),
    _theme("DIGITAL_HEALTHCARE_AI", Round10LargeSector.BIOTECH_HEALTHCARE_DEVICE, E2RArchetype.PLATFORM_SOFTWARE_INTERNET, ("의료 AI", "원격의료", "유전체검사", "마이크로바이옴"), Round10ThemePosture.WATCH_YELLOW_FIRST, ("reimbursement_or_contract", "recurring_revenue", "regulatory_clearance"), "Digital healthcare needs monetization and regulation evidence."),
    _theme("CANNABIS_REGULATED_HEALTH", Round10LargeSector.BIOTECH_HEALTHCARE_DEVICE, E2RArchetype.THEME_VALUATION_OVERHEAT, ("마리화나", "대마초", "규제형 바이오 이벤트"), Round10ThemePosture.REDTEAM_FIRST, ("legal_revenue", "regulatory_approval", "cash_flow"), "Cannabis themes remain RedTeam-first without legal revenue."),
    _theme("PLATFORM_SOFTWARE_INTERNET", Round10LargeSector.PLATFORM_CONTENT_SW_SECURITY, E2RArchetype.PLATFORM_SOFTWARE_INTERNET, ("클라우드 컴퓨팅", "원격근무", "컨택센터", "광고"), Round10ThemePosture.WATCH_YELLOW_FIRST, ("arpu", "recurring_revenue", "opm_leverage"), "Platform needs monetization and margin leverage."),
    _theme("GAME_CONTENT_IP", Round10LargeSector.PLATFORM_CONTENT_SW_SECURITY, E2RArchetype.GAME_CONTENT_IP, ("게임", "엔터", "미디어 콘텐츠", "음원서비스", "방송·언론"), Round10ThemePosture.WATCH_YELLOW_FIRST, ("ip_repeatability", "global_revenue", "op_eps_revision"), "Content/IP needs repeat monetization, not launch hype only."),
    _theme("METAVERSE_NFT_THEME", Round10LargeSector.PLATFORM_CONTENT_SW_SECURITY, E2RArchetype.THEME_VALUATION_OVERHEAT, ("메타버스", "NFT", "디지털자산", "STO"), Round10ThemePosture.REDTEAM_FIRST, ("revenue_conversion", "user_monetization", "regulatory_risk"), "Metaverse/NFT stays theme-risk until monetization is proven."),
    _theme("AI_SOFTWARE_APPLICATION", Round10LargeSector.PLATFORM_CONTENT_SW_SECURITY, E2RArchetype.PLATFORM_SOFTWARE_INTERNET, ("인공지능 AI", "AI 신약개발", "의료AI", "딥페이크"), Round10ThemePosture.WATCH_YELLOW_FIRST, ("paid_usage", "cost_efficiency", "opm_leverage"), "AI software needs paid usage and cost/margin proof."),
    _theme("SECURITY_IDENTITY_INFRA", Round10LargeSector.PLATFORM_CONTENT_SW_SECURITY, E2RArchetype.PLATFORM_SOFTWARE_INTERNET, ("IT보안", "생체인식", "CCTV", "딥페이크"), Round10ThemePosture.WATCH_YELLOW_FIRST, ("recurring_contract", "security_demand", "op_eps_revision"), "Security infra needs recurring contract evidence."),
    _theme("EDUCATION_SPECIALTY_SERVICES", Round10LargeSector.PLATFORM_CONTENT_SW_SECURITY, E2RArchetype.EDUCATION_SPECIALTY_SERVICES, ("교육", "취업일자리", "키즈", "유아용품"), Round10ThemePosture.WATCH_YELLOW_FIRST, ("enrollment_or_user_growth", "opm_leverage", "policy_risk"), "Education services need recurring revenue and policy risk checks."),
    _theme("AIRLINE_TRAVEL_CYCLE", Round10LargeSector.MOBILITY_TRANSPORT_LEISURE, E2RArchetype.TRAVEL_LEISURE_REOPENING, ("항공사", "여행·레저", "야놀자 관련주"), Round10ThemePosture.WATCH_YELLOW_FIRST, ("traffic_recovery", "yield_or_margin", "cost_risk"), "Travel tags need traffic, yield, and margin evidence."),
    _theme("CASINO_DUTYFREE_TOURISM", Round10LargeSector.MOBILITY_TRANSPORT_LEISURE, E2RArchetype.TRAVEL_LEISURE_REOPENING, ("카지노", "면세점", "금강산 관광"), Round10ThemePosture.WATCH_YELLOW_FIRST, ("visitor_mix", "drop_or_sales", "opm_leverage"), "Tourism needs visitor mix and margin evidence; policy events stay capped."),
    _theme("SHIPPING_FREIGHT_CYCLE", Round10LargeSector.MOBILITY_TRANSPORT_LEISURE, E2RArchetype.SHIPPING_FREIGHT_CYCLE, ("해운", "택배", "종합물류"), Round10ThemePosture.REDTEAM_FIRST, ("freight_rate", "contract_vs_spot", "vessel_supply"), "Shipping is cycle-heavy; Green is very restricted."),
    _theme("AUTO_COMPLETED_VEHICLE", Round10LargeSector.MOBILITY_TRANSPORT_LEISURE, E2RArchetype.AUTO_MOBILITY_COMPLETED_VEHICLE, ("현대차", "기아", "자동차 연비개선", "경량화"), Round10ThemePosture.WATCH_YELLOW_FIRST, ("mix_improvement", "roe_fcf", "shareholder_return"), "Completed vehicle needs ROE/FCF and capital allocation proof."),
    _theme("AUTO_COMPONENTS_EV_ADAS", Round10LargeSector.MOBILITY_TRANSPORT_LEISURE, E2RArchetype.AUTO_MOBILITY_COMPONENTS, ("자율주행", "전기차 부품", "카메라", "스마트폰 부품"), Round10ThemePosture.WATCH_YELLOW_FIRST, ("customer_diversification", "content_per_vehicle", "opm_improvement"), "Auto components need customer diversification and margin proof."),
    _theme("RENTAL_USED_CAR_MOBILITY", Round10LargeSector.MOBILITY_TRANSPORT_LEISURE, E2RArchetype.RETAIL_DOMESTIC_CONSUMER, ("렌터카", "중고차", "자전거"), Round10ThemePosture.WATCH_YELLOW_FIRST, ("fleet_margin", "residual_value", "demand_visibility"), "Mobility services need margin and asset value checks."),
    _theme("URBAN_AIR_DRONE", Round10LargeSector.MOBILITY_TRANSPORT_LEISURE, E2RArchetype.DEFENSE_GOVERNMENT_BACKLOG, ("드론", "플라잉카", "항공우주", "스페이스X"), Round10ThemePosture.REDTEAM_FIRST, ("government_or_commercial_order", "revenue_conversion", "regulatory_approval"), "Drone/UAM themes need order or revenue conversion."),
    _theme("CONSTRUCTION_REAL_ESTATE_CREDIT", Round10LargeSector.CONSTRUCTION_REAL_ESTATE_MATERIALS, E2RArchetype.CONSTRUCTION_REAL_ESTATE_CREDIT, ("대형 건설사", "중소형 건설사", "부동산 자산 보유"), Round10ThemePosture.REDTEAM_FIRST, ("pf_exposure", "cash_flow", "credit_risk"), "Construction remains credit-risk first."),
    _theme("REIT_DEVELOPMENT_TRUST", Round10LargeSector.CONSTRUCTION_REAL_ESTATE_MATERIALS, E2RArchetype.REIT_DEVELOPMENT_TRUST, ("부동산 개발신탁리츠", "리츠", "부동산 자산 보유"), Round10ThemePosture.WATCH_YELLOW_FIRST, ("nav_discount", "cash_yield", "debt_cost"), "REITs need NAV, yield, and debt-cost evidence."),
    _theme("BUILDING_MATERIALS_CYCLE", Round10LargeSector.CONSTRUCTION_REAL_ESTATE_MATERIALS, E2RArchetype.BUILDING_MATERIALS_CYCLE, ("건자재", "시멘트", "레미콘", "콘크리트", "철근", "거푸집", "가구"), Round10ThemePosture.WATCH_YELLOW_FIRST, ("price_hike", "volume", "cost_spread", "housing_cycle"), "Building materials are cycle/spread sensitive."),
    _theme("INFRA_RECONSTRUCTION_POLICY", Round10LargeSector.CONSTRUCTION_REAL_ESTATE_MATERIALS, E2RArchetype.INFRA_RECONSTRUCTION_POLICY, ("우크라 재건", "네옴시티", "세종시", "철도"), Round10ThemePosture.REDTEAM_FIRST, ("funded_order", "contract_economics", "delivery_schedule"), "Reconstruction policy themes need confirmed orders."),
    _theme("DISASTER_REBUILD_EVENT", Round10LargeSector.CONSTRUCTION_REAL_ESTATE_MATERIALS, E2RArchetype.ONE_OFF_EVENT_DEMAND, ("지진", "폭염", "재난복구", "건자재 이벤트"), Round10ThemePosture.REDTEAM_FIRST, ("actual_order", "repeat_demand", "margin_visibility"), "Disaster rebuild is event demand unless repeat orders exist."),
    _theme("NORTH_KOREA_POLICY_EVENT", Round10LargeSector.POLICY_GEOPOLITICAL_EVENT, E2RArchetype.THEME_VALUATION_OVERHEAT, ("남북경협", "DMZ", "개성공단", "금강산 관광", "광물자원개발"), Round10ThemePosture.REDTEAM_FIRST, ("binding_policy", "funded_project", "revenue_visibility"), "North Korea policy events are Green-blocked without binding revenue."),
    _theme("GEOPOLITICAL_RECONSTRUCTION", Round10LargeSector.POLICY_GEOPOLITICAL_EVENT, E2RArchetype.CONTRACT_BACKLOG_INDUSTRIAL, ("우크라 재건", "네옴시티", "원전 수출", "철도"), Round10ThemePosture.REDTEAM_FIRST, ("contract_award", "funding", "supplier_margin"), "Geopolitical reconstruction needs funded contract evidence."),
    _theme("CLIMATE_DISASTER_EVENT", Round10LargeSector.POLICY_GEOPOLITICAL_EVENT, E2RArchetype.ONE_OFF_EVENT_DEMAND, ("폭염", "황사", "미세먼지", "공기정화", "마스크", "지진"), Round10ThemePosture.REDTEAM_FIRST, ("repeat_demand", "sell_through", "margin_visibility"), "Climate/disaster demand is event-driven unless recurrence is proven."),
    _theme("INFECTIOUS_DISEASE_EVENT", Round10LargeSector.POLICY_GEOPOLITICAL_EVENT, E2RArchetype.ONE_OFF_EVENT_DEMAND, ("엠폭스", "코로나19", "전염병 진단", "빈대퇴치"), Round10ThemePosture.REDTEAM_FIRST, ("recurring_non_event_demand", "post_event_revenue", "margin_normalization"), "Disease/pest themes are one-off until proven recurring."),
    _theme("SPECULATIVE_SCIENCE_THEME", Round10LargeSector.POLICY_GEOPOLITICAL_EVENT, E2RArchetype.THEME_VALUATION_OVERHEAT, ("초전도체", "맥신", "그래핀", "양자 기술"), Round10ThemePosture.REDTEAM_FIRST, ("commercial_revenue", "contract_or_order", "technical_validation"), "Speculative science is a RedTeam-first tag."),
    _theme("POLICY_LOCAL_THEME", Round10LargeSector.POLICY_GEOPOLITICAL_EVENT, E2RArchetype.THEME_VALUATION_OVERHEAT, ("세종시", "지역화폐", "취업일자리"), Round10ThemePosture.REDTEAM_FIRST, ("policy_execution", "revenue_visibility", "funding"), "Local policy themes need execution and revenue evidence."),
    _theme("SMART_FARM_AGRI_TECH", Round10LargeSector.EDUCATION_LIFE_AGRI_MISC, E2RArchetype.ROBOTICS_FACTORY_AUTOMATION, ("스마트팜", "농업 종자", "비료", "농약", "농기계"), Round10ThemePosture.WATCH_YELLOW_FIRST, ("order_or_adoption", "revenue_conversion", "margin_visibility"), "Smart farm needs adoption and revenue conversion."),
    _theme("LIVESTOCK_FISHERY_CYCLE", Round10LargeSector.EDUCATION_LIFE_AGRI_MISC, E2RArchetype.COMMODITY_SPREAD, ("양돈주", "육계주", "참치 원양어업", "배합사료"), Round10ThemePosture.REDTEAM_FIRST, ("commodity_cycle", "feed_cost", "price_pass_through"), "Livestock/fishery is cycle-heavy."),
    _theme("HOME_CHILD_EDUCATION", Round10LargeSector.EDUCATION_LIFE_AGRI_MISC, E2RArchetype.EDUCATION_SPECIALTY_SERVICES, ("키즈", "유아용품", "교육", "밥솥"), Round10ThemePosture.WATCH_YELLOW_FIRST, ("recurring_demand", "channel_expansion", "margin_visibility"), "Home/child/education needs recurring demand."),
    _theme("WASTE_RECYCLING_ENVIRONMENT", Round10LargeSector.EDUCATION_LIFE_AGRI_MISC, E2RArchetype.UTILITIES_REGULATED_TARIFF, ("폐기물처리", "폐배터리", "탈 플라스틱"), Round10ThemePosture.WATCH_YELLOW_FIRST, ("regulated_demand", "capacity_utilization", "margin_visibility"), "Environmental services need regulated demand and utilization evidence."),
    _theme("SERVICE_KIOSK_AUTOMATION", Round10LargeSector.EDUCATION_LIFE_AGRI_MISC, E2RArchetype.ROBOTICS_FACTORY_AUTOMATION, ("키오스크", "컨택센터", "스마트홈"), Round10ThemePosture.WATCH_YELLOW_FIRST, ("customer_adoption", "recurring_revenue", "opm_leverage"), "Service automation needs adoption and margin leverage."),
)


_ROUND10_THEME_ARCHETYPE_EXCLUSIONS = {
    "RAIL_INFRASTRUCTURE",
    "SMART_FACTORY_AUTOMATION",
    "SEMI_MATERIALS_PROCESS",
    "DISPLAY_OLED_EQUIPMENT",
    "ELECTRONIC_COMPONENTS",
    "CYBER_AI_SECURITY",
    "BATTERY_EQUIPMENT_PARTS",
    "EV_INFRASTRUCTURE",
    "HYDROGEN_FUEL_CELL",
    "PAPER_PACKAGING",
    "AGRI_COMMODITY_INPUTS",
    "APPAREL_BRAND_OEM",
    "HOME_LIVING_APPLIANCE",
}


ROUND10_THEME_ARCHETYPES_RAW = ROUND10_THEME_ARCHETYPES
ROUND10_THEME_ARCHETYPES = tuple(
    item for item in ROUND10_THEME_ARCHETYPES_RAW if item.label not in _ROUND10_THEME_ARCHETYPE_EXCLUSIONS
)


ROUND10_CASE_CANDIDATE_GROUPS: Mapping[str, tuple[str, ...]] = {
    "Retail/E-commerce": (
        "convenience_store_efficiency_success_candidate",
        "ecommerce_fresh_logistics_candidate",
        "home_shopping_margin_decline_counterexample",
        "china_direct_purchase_margin_pressure_counterexample",
    ),
    "Insurance/Financial": (
        "nonlife_insurance_loss_ratio_success_candidate",
        "life_insurance_csm_candidate",
        "low_pbr_no_roe_value_trap",
        "pf_credit_cost_financial_4c",
    ),
    "Beauty Supply Chain": (
        "kbeauty_oem_odm_success_candidate",
        "cosmetic_raw_material_supplier_candidate",
        "china_dependency_counterexample",
        "channel_stuffing_receivables_4c",
    ),
    "Agri/Livestock/Food Commodity": (
        "pork_price_cycle_candidate",
        "poultry_disease_event_candidate",
        "feed_cost_squeeze_counterexample",
        "soybean_cost_pressure_counterexample",
    ),
    "Construction Materials": (
        "cement_price_hike_candidate",
        "rebar_spread_candidate",
        "housing_slowdown_materials_4c",
        "construction_pf_credit_4c",
    ),
    "Digital Finance": (
        "stablecoin_payment_infra_candidate",
        "sto_platform_candidate",
        "crypto_theme_no_revenue_counterexample",
        "regulation_crackdown_4c",
    ),
    "Healthcare": (
        "botox_export_success_candidate",
        "dental_implant_export_candidate",
        "cro_cmo_contract_candidate",
        "clinical_biotech_dilution_4c",
        "infectious_disease_oneoff_counterexample",
    ),
    "Policy/Event": (
        "north_korea_policy_event_counterexample",
        "ukraine_reconstruction_order_confirmed_candidate",
        "neom_city_theme_no_order_counterexample",
        "speculative_science_theme_counterexample",
    ),
    "Climate/Event": (
        "heatwave_power_demand_candidate",
        "fine_dust_mask_oneoff_counterexample",
        "disaster_rebuild_materials_event",
        "bedbug_event_oneoff",
    ),
}


def round10_theme_tag_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for archetype in ROUND10_THEME_ARCHETYPES:
        large_sector = ROUND10_LARGE_SECTORS[archetype.large_sector]
        for tag in archetype.theme_tags:
            rows.append(
                {
                    "theme_tag": tag,
                    "sub_archetype": archetype.label,
                    "large_sector": archetype.large_sector.value,
                    "large_sector_korean": large_sector.korean_name,
                    "canonical_archetype": archetype.canonical_archetype.value,
                    "posture": archetype.posture.value,
                    "theme_is_score_input": str(archetype.theme_is_score_input).lower(),
                    "must_have_evidence": "|".join(archetype.must_have_evidence),
                    "green_policy": archetype.green_policy,
                }
            )
    return tuple(rows)


def find_round10_theme_tag(tag: str) -> tuple[dict[str, str], ...]:
    needle = tag.lower()
    return tuple(row for row in round10_theme_tag_rows() if row["theme_tag"].lower() == needle)


def round10_posture_counts() -> dict[str, int]:
    counts = {posture.value: 0 for posture in Round10ThemePosture}
    for archetype in ROUND10_THEME_ARCHETYPES:
        counts[archetype.posture.value] += 1
    return counts


def write_round10_theme_taxonomy_reports(
    *,
    output_directory: str | Path = "output/e2r_round10_theme_tag_taxonomy",
    theme_map_path: str | Path = "data/sector_taxonomy/theme_tag_map.csv",
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    theme_map = Path(theme_map_path)
    theme_map.parent.mkdir(parents=True, exist_ok=True)
    paths = {
        "theme_tag_map": theme_map,
        "output_theme_tag_map": output / "theme_tag_map.csv",
        "summary": output / "round10_theme_taxonomy_summary.md",
        "large_sector_map": output / "round10_large_sector_map.csv",
        "sub_archetype_map": output / "round10_sub_archetype_map.csv",
        "posture_report": output / "round10_posture_report.md",
        "case_candidate_plan": output / "round10_case_record_candidate_plan.md",
    }
    _write_theme_tag_map(paths["theme_tag_map"])
    _write_theme_tag_map(paths["output_theme_tag_map"])
    _write_large_sector_map(paths["large_sector_map"])
    _write_sub_archetype_map(paths["sub_archetype_map"])
    paths["summary"].write_text(render_round10_summary_markdown(), encoding="utf-8")
    paths["posture_report"].write_text(render_round10_posture_report_markdown(), encoding="utf-8")
    paths["case_candidate_plan"].write_text(render_round10_case_candidate_plan_markdown(), encoding="utf-8")
    return paths


def render_round10_summary_markdown() -> str:
    rows = round10_theme_tag_rows()
    lines = [
        "# Round-10 Theme Tag Taxonomy Summary",
        "",
        f"- source_round: `{ROUND10_SOURCE_ROUND_PATH}`",
        f"- large_sector_count: {len(ROUND10_LARGE_SECTORS)}",
        f"- sub_archetype_count: {len(ROUND10_THEME_ARCHETYPES)}",
        f"- theme_tag_count: {len(rows)}",
        "- production_scoring_changed: false",
        "- theme_tags_are_score_input: false",
        "",
        "## Interpretation",
        "- Theme tags are search/routing labels, not score evidence.",
        "- Scoring remains owned by canonical E2R archetypes and evidence fields.",
        "- Example: `초전도체` maps to `SPECULATIVE_SCIENCE_THEME`, which maps to `THEME_VALUATION_OVERHEAT`; it does not get Green from the tag itself.",
    ]
    return "\n".join(lines) + "\n"


def render_round10_posture_report_markdown() -> str:
    counts = round10_posture_counts()
    lines = [
        "# Round-10 Posture Report",
        "",
        "## Counts",
    ]
    for posture in Round10ThemePosture:
        lines.append(f"- {posture.value}: {counts[posture.value]}")
    lines.extend(
        [
            "",
            "## Guardrail",
            "- Green-possible means future scoring may consider Green after evidence validation.",
            "- Watch/Yellow-first means the tag needs stronger proof before high-conviction treatment.",
            "- RedTeam-first means false-positive prevention is the main purpose.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round10_case_candidate_plan_markdown() -> str:
    lines = [
        "# Round-10 Case Record Candidate Plan",
        "",
        "These are planned case records for future v0.3/v0.4 packs. They are not candidate-generation input.",
        "",
    ]
    for group, cases in ROUND10_CASE_CANDIDATE_GROUPS.items():
        lines.append(f"## {group}")
        for case_id in cases:
            lines.append(f"- `{case_id}`")
        lines.append("")
    lines.extend(
        [
            "## What Not To Change",
            "- Do not apply theme tags directly to score.",
            "- Do not lower Stage 3-Green thresholds.",
            "- Do not fabricate stage dates or price paths.",
        ]
    )
    return "\n".join(lines) + "\n"


def _write_theme_tag_map(path: Path) -> Path:
    with path.open("w", encoding="utf-8", newline="") as handle:
        fieldnames = (
            "theme_tag",
            "sub_archetype",
            "large_sector",
            "large_sector_korean",
            "canonical_archetype",
            "posture",
            "theme_is_score_input",
            "must_have_evidence",
            "green_policy",
        )
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in round10_theme_tag_rows():
            writer.writerow(row)
    return path


def _write_large_sector_map(path: Path) -> Path:
    with path.open("w", encoding="utf-8", newline="") as handle:
        fieldnames = ("large_sector", "korean_name", "description")
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for key, definition in ROUND10_LARGE_SECTORS.items():
            writer.writerow(
                {
                    "large_sector": key.value,
                    "korean_name": definition.korean_name,
                    "description": definition.description,
                }
            )
    return path


def _write_sub_archetype_map(path: Path) -> Path:
    with path.open("w", encoding="utf-8", newline="") as handle:
        fieldnames = (
            "sub_archetype",
            "large_sector",
            "canonical_archetype",
            "posture",
            "theme_count",
            "theme_tags",
            "must_have_evidence",
            "green_policy",
        )
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for item in ROUND10_THEME_ARCHETYPES:
            writer.writerow(
                {
                    "sub_archetype": item.label,
                    "large_sector": item.large_sector.value,
                    "canonical_archetype": item.canonical_archetype.value,
                    "posture": item.posture.value,
                    "theme_count": len(item.theme_tags),
                    "theme_tags": "|".join(item.theme_tags),
                    "must_have_evidence": "|".join(item.must_have_evidence),
                    "green_policy": item.green_policy,
                }
            )
    return path


__all__ = [
    "ROUND10_CASE_CANDIDATE_GROUPS",
    "ROUND10_LARGE_SECTORS",
    "ROUND10_SOURCE_ROUND_PATH",
    "ROUND10_THEME_ARCHETYPES",
    "Round10LargeSector",
    "Round10LargeSectorDefinition",
    "Round10ThemeArchetype",
    "Round10ThemePosture",
    "find_round10_theme_tag",
    "render_round10_case_candidate_plan_markdown",
    "render_round10_posture_report_markdown",
    "render_round10_summary_markdown",
    "round10_posture_counts",
    "round10_theme_tag_rows",
    "write_round10_theme_taxonomy_reports",
]
