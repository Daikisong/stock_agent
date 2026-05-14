"""Round-12 theme refinement overlay.

Round 12 adds a finer theme-tag overlay on top of the Round-10 map. It is
still calibration/report material only: theme labels route research and case
mining, while production scoring remains evidence-driven.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping

from e2r.sector.archetypes import E2RArchetype
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector, Round10ThemePosture


ROUND12_SOURCE_ROUND_PATH = "docs/round/round_12.md"


@dataclass(frozen=True)
class Round12ThemeRefinement:
    sub_archetype: str
    large_sector: Round10LargeSector
    canonical_archetype: E2RArchetype
    posture: Round10ThemePosture
    theme_tags: tuple[str, ...]
    stage1_query_terms: tuple[str, ...]
    must_have_evidence: tuple[str, ...]
    red_flag_evidence: tuple[str, ...]
    score_weight_profile: str
    green_policy: str
    case_candidates: tuple[str, ...]

    @property
    def theme_is_score_input(self) -> bool:
        return False


ROUND12_REFINEMENTS: tuple[Round12ThemeRefinement, ...] = (
    Round12ThemeRefinement(
        "RETAIL_CONVENIENCE_OFFLINE",
        Round10LargeSector.CONSUMER_RETAIL_BRAND,
        E2RArchetype.RETAIL_DOMESTIC_CONSUMER,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        ("편의점", "홈쇼핑", "음식료-유통", "PB상품"),
        ("same-store sales", "PB mix", "점포효율", "OPM 개선"),
        ("same_store_sales", "opm_improvement", "pb_mix", "fcf_improvement"),
        ("rent_wage_pressure", "traffic_only", "inventory_build", "online_competition"),
        "retail_operating_leverage",
        "Green only if store efficiency, margin, and FCF improve beyond simple traffic recovery.",
        ("convenience_store_efficiency_success_candidate", "home_shopping_margin_decline_counterexample"),
    ),
    Round12ThemeRefinement(
        "ECOMMERCE_FRESH_LOGISTICS",
        Round10LargeSector.CONSUMER_RETAIL_BRAND,
        E2RArchetype.PLATFORM_SOFTWARE_INTERNET,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        ("마켓컬리", "오아시스", "콜드체인", "새벽배송"),
        ("unit economics", "repeat orders", "cold-chain margin", "상장 이벤트"),
        ("unit_economics", "repeat_orders", "logistics_margin", "revenue_conversion"),
        ("event_premium_only", "traffic_without_profit", "delivery_cost_pressure"),
        "fresh_ecommerce_unit_economics",
        "Listing or stake events are event-premium until logistics margin and repeat orders are visible.",
        ("ecommerce_fresh_logistics_candidate", "china_direct_purchase_margin_pressure_counterexample"),
    ),
    Round12ThemeRefinement(
        "INSURANCE_UNDERWRITING_CYCLE",
        Round10LargeSector.FINANCIAL_CAPITAL_DIGITAL,
        E2RArchetype.FINANCIAL_SPREAD_BALANCE_SHEET,
        Round10ThemePosture.GREEN_POSSIBLE,
        ("손해보험", "생명보험", "화재", "고배당주"),
        ("손해율 개선", "CSM", "K-ICS", "자사주/배당"),
        ("loss_ratio", "csm_growth", "capital_ratio", "shareholder_return_execution"),
        ("loss_ratio_worsening", "capital_ratio_weak", "credit_cost", "return_policy_retreat"),
        "insurance_underwriting_valueup",
        "Insurance Green requires underwriting improvement, capital strength, and executed return.",
        ("nonlife_insurance_loss_ratio_success_candidate", "life_insurance_csm_candidate"),
    ),
    Round12ThemeRefinement(
        "PAYMENT_FINTECH_INFRA",
        Round10LargeSector.FINANCIAL_CAPITAL_DIGITAL,
        E2RArchetype.PLATFORM_SOFTWARE_INTERNET,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        ("결제서비스", "토스 관련주", "지역화폐", "신용정보"),
        ("거래액", "take rate", "금융기관 채택", "수수료 모델"),
        ("transaction_volume", "take_rate", "institutional_adoption", "fee_model"),
        ("law_delay", "security_issue", "no_revenue", "take_rate_pressure"),
        "payment_infra_monetization",
        "Payment themes need transaction economics and regulated adoption before higher conviction.",
        ("stablecoin_payment_infra_candidate", "sto_platform_candidate"),
    ),
    Round12ThemeRefinement(
        "DIGITAL_ASSET_TOKENIZATION",
        Round10LargeSector.FINANCIAL_CAPITAL_DIGITAL,
        E2RArchetype.THEME_VALUATION_OVERHEAT,
        Round10ThemePosture.REDTEAM_FIRST,
        ("스테이블코인", "STO", "디지털자산", "블록체인", "NFT"),
        ("규제 승인", "발행 실적", "거래량", "수탁/정산 수수료"),
        ("regulation_approval", "issued_volume", "fee_model", "institutional_adoption"),
        ("law_delay", "security_issue", "no_revenue", "theme_only_tokenization"),
        "digital_asset_regulated_revenue",
        "Tokenization stays RedTeam-first until regulated revenue and adoption are proven.",
        ("crypto_theme_no_revenue_counterexample", "regulation_crackdown_4c"),
    ),
    Round12ThemeRefinement(
        "BEAUTY_OEM_ODM_SUPPLYCHAIN",
        Round10LargeSector.CONSUMER_RETAIL_BRAND,
        E2RArchetype.K_BEAUTY_EXPORT_DISTRIBUTION,
        Round10ThemePosture.GREEN_POSSIBLE,
        ("화장품 OEM", "화장품 ODM", "화장품 원재료", "화장품 부자재"),
        ("ODM 주문", "고객사 다변화", "미국/일본 수출", "OPM 개선"),
        ("customer_diversification", "repeat_orders", "capacity_utilization", "opm_roe_improvement"),
        ("china_dependency", "channel_stuffing", "receivables_spike", "tariff_regulation"),
        "beauty_supply_chain_export",
        "Beauty supply-chain Green requires repeat orders, diversified customers, and clean working capital.",
        ("kbeauty_oem_odm_success_candidate", "channel_stuffing_receivables_4c"),
    ),
    Round12ThemeRefinement(
        "AGRI_LIVESTOCK_FOOD_COMMODITY",
        Round10LargeSector.EDUCATION_LIFE_AGRI_MISC,
        E2RArchetype.COMMODITY_SPREAD,
        Round10ThemePosture.REDTEAM_FIRST,
        ("양돈주", "육계주", "배합사료", "대두", "참치 원양어업"),
        ("곡물가격", "사료비", "판가 전가", "질병/날씨 이벤트"),
        ("price_pass_through", "feed_cost", "inventory_status", "op_eps_revision"),
        ("disease_event_only", "feed_cost_squeeze", "commodity_reversal", "weather_theme"),
        "food_commodity_cycle_cap",
        "Agri/livestock moves are cycle-capped unless pricing power and repeat demand are visible.",
        ("pork_price_cycle_candidate", "feed_cost_squeeze_counterexample"),
    ),
    Round12ThemeRefinement(
        "BUILDING_MATERIALS_CYCLE",
        Round10LargeSector.CONSTRUCTION_REAL_ESTATE_MATERIALS,
        E2RArchetype.COMMODITY_SPREAD,
        Round10ThemePosture.REDTEAM_FIRST,
        ("건자재", "시멘트", "레미콘", "콘크리트", "철근", "가구", "거푸집"),
        ("가격 인상", "출하량", "착공", "PF 리스크"),
        ("price_hike", "shipment_volume", "cost_spread", "housing_cycle"),
        ("pf_stress", "housing_slowdown", "cost_inflation", "price_hike_failure"),
        "building_materials_credit_cycle",
        "Building materials need price and volume support; PF/real-estate risk caps Green.",
        ("cement_price_hike_candidate", "housing_slowdown_materials_4c"),
    ),
    Round12ThemeRefinement(
        "RENEWABLE_ENERGY_POLICY",
        Round10LargeSector.BATTERY_EV_GREEN,
        E2RArchetype.UTILITIES_REGULATED_TARIFF,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        ("풍력", "탄소배출권", "신재생에너지", "전력망", "스마트그리드"),
        ("정책/보조금", "프로젝트 수주", "가동률", "OP 전환"),
        ("project_backlog", "policy_support", "utilization", "margin_visibility"),
        ("subsidy_cut", "project_delay", "tariff_issue", "utilization_down"),
        "renewable_policy_project_economics",
        "Renewable policy needs project economics and margin support before high conviction.",
        ("heatwave_power_demand_candidate", "disaster_rebuild_materials_event"),
    ),
    Round12ThemeRefinement(
        "HYDROGEN_FUEL_CELL_INFRA",
        Round10LargeSector.BATTERY_EV_GREEN,
        E2RArchetype.THEME_VALUATION_OVERHEAT,
        Round10ThemePosture.REDTEAM_FIRST,
        ("수소차 연료전지", "수소차 인프라", "수소차 기타부품"),
        ("공장 착공", "생산능력", "고객/수요", "원가 경쟁력"),
        ("commercial_revenue", "production_capacity", "customer_demand", "cost_curve"),
        ("policy_dependency", "no_revenue", "utilization_down", "project_delay"),
        "hydrogen_commercial_economics",
        "Hydrogen is policy/theme-heavy until commercial revenue and utilization are visible.",
        ("hydrogen_fuel_cell_plant_candidate", "hydrogen_theme_no_revenue_counterexample"),
    ),
    Round12ThemeRefinement(
        "SOLAR_TARIFF_SUPPLYCHAIN",
        Round10LargeSector.BATTERY_EV_GREEN,
        E2RArchetype.UTILITIES_REGULATED_TARIFF,
        Round10ThemePosture.REDTEAM_FIRST,
        ("태양광", "태양광 모듈", "태양광 공급망"),
        ("관세", "통관", "보조금", "공장 가동률"),
        ("tariff_visibility", "supply_chain_clearance", "subsidy_support", "utilization"),
        ("tariff_delay", "customs_hold", "subsidy_cut", "supply_chain_disruption"),
        "solar_tariff_supply_chain_risk",
        "Solar is Green-restricted when tariff/customs and subsidy risk dominate economics.",
        ("solar_policy_candidate", "solar_tariff_supplychain_4c"),
    ),
    Round12ThemeRefinement(
        "TIRE_AUTO_COMPONENT_SPREAD",
        Round10LargeSector.MOBILITY_TRANSPORT_LEISURE,
        E2RArchetype.AUTO_MOBILITY_COMPONENTS,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        ("타이어", "자동차 연비개선", "경량화", "현대-기아차 부품주"),
        ("OE/RE mix", "ASP", "원재료 spread", "고객 다변화"),
        ("oe_re_mix", "asp", "raw_material_spread", "customer_diversification"),
        ("raw_material_inflation", "factory_disruption", "customer_concentration", "auto_demand_slowdown"),
        "tire_component_spread",
        "Tire/component scoring needs spread and customer evidence, not auto theme alone.",
        ("tire_spread_success_candidate", "factory_fire_4c_counterexample"),
    ),
    Round12ThemeRefinement(
        "EVENT_DISEASE_PEST_DEMAND",
        Round10LargeSector.POLICY_GEOPOLITICAL_EVENT,
        E2RArchetype.ONE_OFF_EVENT_DEMAND,
        Round10ThemePosture.REDTEAM_FIRST,
        ("엠폭스", "코로나19", "전염병 진단", "빈대퇴치", "황사마스크", "공기정화"),
        ("감염병 뉴스", "진단/방역 수요", "단기 공급부족", "재고 정상화"),
        ("recurring_non_event_demand", "post_event_revenue", "margin_normalization"),
        ("one_off_demand", "inventory_build", "guidance_down", "demand_cliff"),
        "event_demand_redteam_cap",
        "Event disease/pest demand is one-off until recurring platform demand is proven.",
        ("infectious_disease_oneoff_counterexample", "fine_dust_mask_oneoff_counterexample"),
    ),
    Round12ThemeRefinement(
        "SPECULATIVE_SCIENCE_THEME",
        Round10LargeSector.POLICY_GEOPOLITICAL_EVENT,
        E2RArchetype.THEME_VALUATION_OVERHEAT,
        Round10ThemePosture.REDTEAM_FIRST,
        ("초전도체", "맥신", "그래핀", "양자 기술", "스페이스X", "페라이트"),
        ("논문/테마 뉴스", "거래대금 급증", "상용화 검증", "실제 계약"),
        ("commercial_contract", "revenue_conversion", "verified_product"),
        ("paper_only", "relatedness_unclear", "price_only_rally", "commercialization_failure"),
        "speculative_science_theme_guardrail",
        "Speculative science tags are Green-blocked without commercialization and revenue evidence.",
        ("speculative_science_theme_counterexample", "ai_dc_theme_no_order"),
    ),
    Round12ThemeRefinement(
        "WASTE_RECYCLING_ENVIRONMENT",
        Round10LargeSector.EDUCATION_LIFE_AGRI_MISC,
        E2RArchetype.UTILITIES_REGULATED_TARIFF,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        ("폐기물처리", "폐배터리", "재활용", "탈 플라스틱"),
        ("규제 수요", "처리량", "가동률", "마진"),
        ("regulated_demand", "processing_volume", "utilization", "margin_visibility"),
        ("policy_delay", "utilization_down", "commodity_price_reversal", "capex_burden"),
        "regulated_environment_utilization",
        "Environmental services need regulated demand and utilization; commodity-linked recycling is capped.",
        ("waste_recycling_candidate", "battery_recycling_price_reversal_counterexample"),
    ),
    Round12ThemeRefinement(
        "MEDIA_AD_CONTENT_CYCLE",
        Round10LargeSector.PLATFORM_CONTENT_SW_SECURITY,
        E2RArchetype.GAME_CONTENT_IP,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        ("광고", "미디어 콘텐츠", "방송·언론", "음원서비스", "엔터"),
        ("광고 경기", "IP 반복성", "글로벌 매출", "OPM"),
        ("ad_recovery", "ip_repeatability", "global_revenue", "opm_leverage"),
        ("hit_driven_miss", "single_ip_dependence", "ad_cycle_down", "contract_scandal"),
        "media_ad_ip_cycle",
        "Media/content needs repeat monetization and OPM support, not single-launch hype.",
        ("media_ad_recovery_candidate", "new_game_hype_fail"),
    ),
    Round12ThemeRefinement(
        "CLOUD_AI_SOFTWARE_INFRA",
        Round10LargeSector.PLATFORM_CONTENT_SW_SECURITY,
        E2RArchetype.PLATFORM_SOFTWARE_INTERNET,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        ("클라우드 컴퓨팅", "인공지능 AI", "AI 소프트웨어", "원격근무"),
        ("유료 사용량", "ARR", "ARPU", "OPM 레버리지"),
        ("recurring_revenue", "paid_usage", "arpu", "opm_leverage"),
        ("mau_without_monetization", "ai_cost_overrun", "regulatory_risk", "churn"),
        "cloud_ai_software_monetization",
        "Cloud/AI software needs monetization and margin leverage before high-conviction treatment.",
        ("douzone_saas_candidate", "mau_only_platform"),
    ),
    Round12ThemeRefinement(
        "SECURITY_IDENTITY_DEEPFAKE",
        Round10LargeSector.PLATFORM_CONTENT_SW_SECURITY,
        E2RArchetype.PLATFORM_SOFTWARE_INTERNET,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        ("IT보안", "딥페이크", "생체인식", "CCTV"),
        ("보안 수요", "반복 계약", "규제 수요", "OP/EPS 상향"),
        ("recurring_contract", "security_demand", "regulatory_demand", "op_eps_revision"),
        ("theme_only_security", "budget_cut", "churn", "no_recurring_revenue"),
        "security_identity_recurring_contract",
        "Security/identity tags need recurring contracts and revenue conversion.",
        ("security_identity_candidate", "deepfake_theme_no_revenue_counterexample"),
    ),
)


def round12_refinement_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for item in ROUND12_REFINEMENTS:
        for tag in item.theme_tags:
            rows.append(
                {
                    "theme_tag": tag,
                    "large_sector": item.large_sector.value,
                    "primary_archetype": item.sub_archetype,
                    "canonical_archetype": item.canonical_archetype.value,
                    "secondary_archetypes": "",
                    "green_policy": item.green_policy,
                    "posture": item.posture.value,
                    "theme_is_score_input": str(item.theme_is_score_input).lower(),
                    "stage1_query_terms": "|".join(item.stage1_query_terms),
                    "must_have_evidence": "|".join(item.must_have_evidence),
                    "red_flag_evidence": "|".join(item.red_flag_evidence),
                    "score_weight_profile": item.score_weight_profile,
                }
            )
    return tuple(rows)


def find_round12_theme_tag(tag: str) -> tuple[dict[str, str], ...]:
    needle = tag.lower()
    return tuple(row for row in round12_refinement_rows() if row["theme_tag"].lower() == needle)


def round12_case_candidate_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for item in ROUND12_REFINEMENTS:
        for case_id in item.case_candidates:
            rows.append(
                {
                    "case_id": case_id,
                    "sub_archetype": item.sub_archetype,
                    "canonical_archetype": item.canonical_archetype.value,
                    "posture": item.posture.value,
                    "status": "planned_case_record",
                }
            )
    return tuple(rows)


def write_round12_theme_refinement_reports(
    *,
    output_directory: str | Path = "output/e2r_round12_theme_refinement",
    theme_map_path: str | Path = "data/sector_taxonomy/theme_tag_map_round12.csv",
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    theme_map = Path(theme_map_path)
    theme_map.parent.mkdir(parents=True, exist_ok=True)
    paths = {
        "theme_map": theme_map,
        "summary": output / "round12_theme_refinement_summary.md",
        "sub_archetype_refinements": output / "round12_sub_archetype_refinements.csv",
        "case_candidate_plan": output / "round12_case_candidate_plan.csv",
        "schema": output / "round12_theme_tag_map_schema.md",
        "next_plan": output / "round12_next_case_library_plan.md",
    }
    _write_rows(round12_refinement_rows(), paths["theme_map"])
    _write_rows(_sub_archetype_rows(), paths["sub_archetype_refinements"])
    _write_rows(round12_case_candidate_rows(), paths["case_candidate_plan"])
    paths["summary"].write_text(render_round12_summary_markdown(), encoding="utf-8")
    paths["schema"].write_text(render_round12_schema_markdown(), encoding="utf-8")
    paths["next_plan"].write_text(render_round12_next_plan_markdown(), encoding="utf-8")
    return paths


def render_round12_summary_markdown() -> str:
    redteam_count = sum(1 for item in ROUND12_REFINEMENTS if item.posture == Round10ThemePosture.REDTEAM_FIRST)
    green_possible = sum(1 for item in ROUND12_REFINEMENTS if item.posture == Round10ThemePosture.GREEN_POSSIBLE)
    lines = [
        "# Round-12 Theme Refinement Summary",
        "",
        f"- source_round: `{ROUND12_SOURCE_ROUND_PATH}`",
        f"- refined_sub_archetype_count: {len(ROUND12_REFINEMENTS)}",
        f"- refined_theme_tag_count: {len(round12_refinement_rows())}",
        f"- green_possible_refinements: {green_possible}",
        f"- redteam_first_refinements: {redteam_count}",
        "- production_scoring_changed: false",
        "- theme_tags_are_score_input: false",
        "",
        "## Interpretation",
        "- Round 12 refines high-impact theme families such as insurance, stablecoins, solar, tires, disease events, and speculative science.",
        "- Theme names still do not create score. Evidence fields do.",
        "- Example: `손해보험` needs loss ratio, CSM/capital, ROE, and shareholder return; low PBR alone is not enough.",
    ]
    return "\n".join(lines) + "\n"


def render_round12_schema_markdown() -> str:
    fields = (
        "theme_tag",
        "large_sector",
        "primary_archetype",
        "secondary_archetypes",
        "green_policy",
        "stage1_query_terms",
        "must_have_evidence",
        "red_flag_evidence",
        "score_weight_profile",
    )
    lines = [
        "# Round-12 Theme Tag Map Schema",
        "",
        "Round 12 defines the schema expected for future theme maps.",
        "",
        "## Fields",
    ]
    for field in fields:
        lines.append(f"- `{field}`")
    lines.extend(
        [
            "",
            "## Guardrail",
            "- `theme_tag` is for search and routing.",
            "- `primary_archetype` is a sub-archetype label for research structure.",
            "- Final score must still come from evidence and canonical E2R rules.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round12_next_plan_markdown() -> str:
    lines = [
        "# Round-12 Next Case Library Plan",
        "",
        "## Add Planned Case Records",
    ]
    for row in round12_case_candidate_rows():
        lines.append(f"- `{row['case_id']}` -> `{row['sub_archetype']}`")
    lines.extend(
        [
            "",
            "## What Not To Change",
            "- Do not apply score_weight_profile to production scoring yet.",
            "- Do not use theme tags as evidence.",
            "- Do not make one-off disease, speculative science, or tokenization themes Green without verified recurring revenue and EPS/FCF evidence.",
        ]
    )
    return "\n".join(lines) + "\n"


def _sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {
            "sub_archetype": item.sub_archetype,
            "large_sector": item.large_sector.value,
            "canonical_archetype": item.canonical_archetype.value,
            "posture": item.posture.value,
            "theme_tags": "|".join(item.theme_tags),
            "must_have_evidence": "|".join(item.must_have_evidence),
            "red_flag_evidence": "|".join(item.red_flag_evidence),
            "score_weight_profile": item.score_weight_profile,
            "case_candidates": "|".join(item.case_candidates),
        }
        for item in ROUND12_REFINEMENTS
    )


def _write_rows(rows: Iterable[Mapping[str, str]], path: Path) -> Path:
    row_tuple = tuple(rows)
    if not row_tuple:
        path.write_text("", encoding="utf-8")
        return path
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=tuple(row_tuple[0].keys()))
        writer.writeheader()
        for row in row_tuple:
            writer.writerow(row)
    return path


__all__ = [
    "ROUND12_REFINEMENTS",
    "ROUND12_SOURCE_ROUND_PATH",
    "Round12ThemeRefinement",
    "find_round12_theme_tag",
    "render_round12_next_plan_markdown",
    "render_round12_schema_markdown",
    "render_round12_summary_markdown",
    "round12_case_candidate_rows",
    "round12_refinement_rows",
    "write_round12_theme_refinement_reports",
]
