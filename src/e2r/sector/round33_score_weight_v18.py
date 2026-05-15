"""Round-33 cases_v15 expansion and score-weight v1.8 hypotheses.

Round 33 separates growth-looking themes with repeat FCF from structures that
can collapse through one-off demand, policy reversal, regulation, legal risk,
inventory, or cost pressure. It is report-only calibration material.
Production feature engineering, scoring, staging, and RedTeam code must not
import this module.
"""

from __future__ import annotations

import csv
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping

from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import CaseDataQuality, E2RCaseRecord, PriceValidation
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector, Round10ThemePosture


ROUND33_SOURCE_ROUND_PATH = "docs/round/round_33.md"
ROUND33_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round33_score_weight_v18"
ROUND33_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_v15_round33.jsonl"
ROUND33_DEFAULT_SCORE_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round33_v18.csv"


@dataclass(frozen=True)
class Round33ScoreWeightDraft:
    eps_fcf: int
    structural_visibility: int
    bottleneck_pricing: int
    market_mispricing: int
    valuation: int
    capital_allocation: int = 0
    information_confidence: int = 5

    def as_dict(self) -> dict[str, int]:
        return {
            "eps_fcf": self.eps_fcf,
            "structural_visibility": self.structural_visibility,
            "bottleneck_pricing": self.bottleneck_pricing,
            "market_mispricing": self.market_mispricing,
            "valuation": self.valuation,
            "capital_allocation": self.capital_allocation,
            "information_confidence": self.information_confidence,
        }


@dataclass(frozen=True)
class Round33ScoreTarget:
    target_id: str
    large_sector: Round10LargeSector
    canonical_archetype: E2RArchetype
    posture: Round10ThemePosture
    score_weight: Round33ScoreWeightDraft
    stage1_signals: tuple[str, ...]
    stage2_signals: tuple[str, ...]
    stage3_conditions: tuple[str, ...]
    green_conditions: tuple[str, ...]
    red_flags: tuple[str, ...]
    stage4c_conditions: tuple[str, ...]
    normalization_point: str

    @property
    def production_scoring_changed(self) -> bool:
        return False


@dataclass(frozen=True)
class Round33CaseCandidate:
    case_id: str
    target_id: str
    symbol: str
    company_name: str
    market: str
    case_type: str
    evidence_fields: tuple[str, ...]
    red_flag_fields: tuple[str, ...]
    notes: str

    @property
    def expected_group(self) -> str:
        return self.case_type


ROUND33_SCORE_TARGETS: tuple[Round33ScoreTarget, ...] = (
    Round33ScoreTarget(
        "MEDIA_AD_CONTENT_CYCLE",
        Round10LargeSector.PLATFORM_CONTENT_SW_SECURITY,
        E2RArchetype.PLATFORM_SOFTWARE_INTERNET,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round33ScoreWeightDraft(18, 16, 6, 14, 12, 0, 5),
        ("ad_cycle_recovery", "streaming_ad_tier", "media_inventory", "digital_ad_platform"),
        ("repeat_ad_inventory", "ad_arpu_growth", "owned_ad_platform", "opm_improvement"),
        ("subscription_ad_hybrid", "data_based_monetization", "client_budget_risk_controlled"),
        ("repeat_ad_inventory", "ad_arpu_growth", "owned_ad_platform", "opm_improvement"),
        ("ad_cycle", "platform_shift", "client_budget_cut", "privacy_regulation", "traditional_media_decline"),
        ("client_budget_cut", "privacy_regulation_hit", "ad_inventory_price_decline", "traditional_media_decline"),
        "Media/ad content is Watch-first: streaming ad platforms can work, but traditional ad cycles and client budgets cap Green.",
    ),
    Round33ScoreTarget(
        "PAPER_PACKAGING_CYCLE",
        Round10LargeSector.MATERIALS_SPREAD_STRATEGIC,
        E2RArchetype.COMMODITY_SPREAD,
        Round10ThemePosture.REDTEAM_FIRST,
        Round33ScoreWeightDraft(17, 13, 12, 10, 9, 3, 5),
        ("paper_packaging", "ecommerce_packaging", "plastic_substitution", "box_price_hike"),
        ("packaging_price_hike", "raw_material_cost_stable", "customer_contract", "fcf_improvement"),
        ("durable_pricing_power", "capacity_discipline", "capital_allocation_controlled"),
        ("packaging_price_hike", "raw_material_cost_stable", "customer_contract", "fcf_improvement"),
        ("pulp_price", "overcapacity", "mature_growth", "pricing_pressure", "ma_expectation_only"),
        ("pulp_cost_spike", "overcapacity", "price_competition", "fcf_deterioration"),
        "Paper and packaging are mature cycle industries; Green is restricted unless pricing, costs, contracts, and FCF are proven.",
    ),
    Round33ScoreTarget(
        "SMART_FARM_AGRI_TECH",
        Round10LargeSector.EDUCATION_LIFE_AGRI_MISC,
        E2RArchetype.ROBOTICS_FACTORY_AUTOMATION,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round33ScoreWeightDraft(18, 14, 12, 9, 9, 0, 5),
        ("smart_farm", "agri_automation", "food_security", "farm_labor_shortage"),
        ("smart_farm_order", "operation_contract", "recurring_service", "price_pass_through"),
        ("adoption_economics_visible", "technical_barrier_controlled", "subsidy_dependency_low"),
        ("smart_farm_order", "operation_contract", "recurring_service", "adoption_economics_visible"),
        ("commodity_cycle", "disease_event", "subsidy", "weather", "feed_cost", "technical_barrier"),
        ("subsidy_cut", "adoption_failure", "weather_event_reversal", "disease_event_normalization"),
        "Smart farm can become Watch-to-Green with orders and recurring service, while livestock/feed events remain cycle-capped.",
    ),
    Round33ScoreTarget(
        "CONSUMER_REGULATED_PRODUCT",
        Round10LargeSector.CONSUMER_RETAIL_BRAND,
        E2RArchetype.RETAIL_DOMESTIC_CONSUMER,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round33ScoreWeightDraft(18, 14, 8, 12, 10, 0, 5),
        ("regulated_consumer", "cannabis_rescheduling", "e_cigarette_approval", "regulated_distribution"),
        ("regulatory_approval", "legal_sales_permission", "repeat_consumption", "distribution_network"),
        ("tax_cost_structure_visible", "legal_conflict_low", "public_health_risk_controlled"),
        ("regulatory_approval", "legal_sales_permission", "repeat_consumption", "distribution_network"),
        ("regulation", "legal_conflict", "public_health", "social_backlash", "approval_uncertain"),
        ("regulatory_crackdown", "sales_ban", "legal_conflict", "public_health_litigation"),
        "Regulated consumer products are Watch-first: approval can open Stage 1/2, but actual sales, margin, and legal stability are required.",
    ),
    Round33ScoreTarget(
        "APPAREL_FAST_FASHION",
        Round10LargeSector.CONSUMER_RETAIL_BRAND,
        E2RArchetype.RETAIL_DOMESTIC_CONSUMER,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round33ScoreWeightDraft(18, 16, 8, 14, 12, 0, 5),
        ("fast_fashion", "cross_border_ecommerce", "apparel_oem", "inventory_turn"),
        ("fast_inventory_turn", "low_markdown", "overseas_channel_expansion", "opm_fcf_improvement"),
        ("ip_legal_risk_low", "product_safety_controlled", "regulatory_compliance_visible"),
        ("fast_inventory_turn", "low_markdown", "overseas_channel_expansion", "opm_fcf_improvement"),
        ("inventory", "markdown", "ip_legal", "product_safety", "regulatory_crackdown", "supply_chain_labor"),
        ("ip_litigation", "product_safety_crackdown", "inventory_markdown", "regulatory_crackdown"),
        "Apparel and cross-border fast fashion stay Watch-first because inventory, markdown, IP, product safety, and regulation can flip the thesis.",
    ),
    Round33ScoreTarget(
        "AI_SOFTWARE_APPLICATION",
        Round10LargeSector.PLATFORM_CONTENT_SW_SECURITY,
        E2RArchetype.PLATFORM_SOFTWARE_INTERNET,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round33ScoreWeightDraft(19, 18, 9, 15, 13, 0, 5),
        ("ai_software", "generative_ai_app", "workflow_ai", "api_usage"),
        ("recurring_subscription_or_api", "customer_lock_in", "compute_cost_controlled", "opm_improvement"),
        ("b2b_workflow_integration", "copyright_risk_controlled", "model_dependency_controlled"),
        ("recurring_subscription_or_api", "customer_lock_in", "compute_cost_controlled", "opm_improvement"),
        ("compute_cost", "copyright", "licensing", "data_privacy", "model_dependency", "feature_only_ai"),
        ("copyright_litigation", "license_integrity_failure", "compute_cost_margin_pressure", "data_privacy_incident"),
        "AI software is Green-possible only with recurring revenue and margin evidence; copyright, licensing, and compute cost are hard gates.",
    ),
    Round33ScoreTarget(
        "METAVERSE_NFT_THEME",
        Round10LargeSector.PLATFORM_CONTENT_SW_SECURITY,
        E2RArchetype.THEME_VALUATION_OVERHEAT,
        Round10ThemePosture.REDTEAM_FIRST,
        Round33ScoreWeightDraft(5, 5, 5, 6, 5, 0, 3),
        ("metaverse", "nft_theme", "virtual_asset_narrative", "price_volume_spike"),
        ("real_platform_fee", "repeat_transaction_volume", "low_regulatory_risk", "fcf_conversion"),
        ("customer_lock_in", "recurring_revenue_above_theme", "liquidity_risk_low"),
        ("real_platform_fee", "repeat_transaction_volume", "fcf_conversion"),
        ("extreme_theme", "no_revenue", "liquidity_collapse", "regulatory", "price_only_rally"),
        ("liquidity_collapse", "regulatory_crackdown", "no_revenue_model", "theme_unwind"),
        "Metaverse/NFT is Green-blocked by default; distinguish it from regulated stablecoin/STO infrastructure.",
    ),
    Round33ScoreTarget(
        "FOOD_AGRI_LIVESTOCK_CYCLE",
        Round10LargeSector.CONSUMER_RETAIL_BRAND,
        E2RArchetype.COMMODITY_SPREAD,
        Round10ThemePosture.REDTEAM_FIRST,
        Round33ScoreWeightDraft(18, 10, 14, 8, 8, 0, 5),
        ("egg_price_spike", "livestock_disease", "feed_cost", "weather_event"),
        ("price_pass_through", "raw_material_cost_stable", "repeat_demand", "smart_farm_service"),
        ("event_normalization_risk_low", "cost_control_visible", "recurring_non_event_demand"),
        ("price_pass_through", "raw_material_cost_stable", "repeat_demand", "recurring_non_event_demand"),
        ("disease_event", "feed_cost", "weather", "price_normalization", "one_off_supply_shock"),
        ("disease_normalization", "feed_cost_spike", "weather_reversal", "price_normalization"),
        "Food/agri/livestock price spikes are mostly event/cycle; Green is restricted unless recurring, non-event demand and cost control are visible.",
    ),
)


ROUND33_CASE_CANDIDATES: tuple[Round33CaseCandidate, ...] = (
    Round33CaseCandidate("netflix_ad_tier_growth_candidate", "MEDIA_AD_CONTENT_CYCLE", "NFLX_AD", "Netflix 광고요금제 성장 후보", "US", "success_candidate", ("streaming_ad_tier", "repeat_ad_inventory", "ad_arpu_growth"), ("privacy_regulation", "ad_cycle"), "Streaming ad tier can be a platform transition candidate if ARPU and OPM are visible."),
    Round33CaseCandidate("wpp_ad_cycle_slowdown_counterexample", "MEDIA_AD_CONTENT_CYCLE", "WPP_CYCLE", "WPP 광고 경기둔화 반례", "EU", "failed_rerating", ("ad_cycle_recovery",), ("client_budget_cut", "ad_cycle"), "Client budget cuts show that advertising market size is not the same as EPS rerating."),
    Round33CaseCandidate("streaming_ad_platform_candidate", "MEDIA_AD_CONTENT_CYCLE", "STREAM_AD", "스트리밍 자체광고 플랫폼 후보", "US", "success_candidate", ("owned_ad_platform", "subscription_ad_hybrid"), ("privacy_regulation", "platform_shift"), "Owned ad platform with hybrid subscription can move beyond traditional ad cycle."),
    Round33CaseCandidate("traditional_broadcast_ad_decline_counterexample", "MEDIA_AD_CONTENT_CYCLE", "BCAST_DECLINE", "전통 방송광고 감소 반례", "GLOBAL", "failed_rerating", ("media_inventory",), ("traditional_media_decline", "client_budget_cut"), "Traditional broadcast ad weakness stays cycle/decline risk."),
    Round33CaseCandidate("packaging_price_hike_candidate", "PAPER_PACKAGING_CYCLE", "PKG_PRICE", "포장재 가격인상 후보", "KR", "success_candidate", ("packaging_price_hike", "raw_material_cost_stable"), ("pulp_price", "pricing_pressure"), "Packaging can reach Stage 2 when price hikes and cost stability improve FCF."),
    Round33CaseCandidate("ecommerce_packaging_demand_candidate", "PAPER_PACKAGING_CYCLE", "ECOM_PKG", "전자상거래 포장수요 후보", "GLOBAL", "success_candidate", ("ecommerce_packaging", "customer_contract"), ("overcapacity", "mature_growth"), "E-commerce demand needs contracts and pricing power, not volume theme only."),
    Round33CaseCandidate("ds_smith_ip_mature_competition_counterexample", "PAPER_PACKAGING_CYCLE", "DSS_IP", "DS Smith IP 성숙경쟁 반례", "EU", "failed_rerating", ("paper_packaging",), ("mature_growth", "ma_expectation_only"), "Mature cardboard consolidation can still fail if capital allocation and growth are weak."),
    Round33CaseCandidate("pulp_cost_margin_4c", "PAPER_PACKAGING_CYCLE", "PULP_4C", "펄프원가 마진훼손 4C", "GLOBAL", "4c_thesis_break", ("box_price_hike",), ("pulp_cost_spike", "fcf_deterioration"), "Pulp cost spike can break packaging margin."),
    Round33CaseCandidate("smart_farm_adoption_policy_candidate", "SMART_FARM_AGRI_TECH", "SMARTFARM_ADOPT", "스마트팜 도입 후보", "KR", "success_candidate", ("smart_farm", "adoption_economics_visible"), ("subsidy", "technical_barrier"), "Smart-farm adoption needs economics and real orders."),
    Round33CaseCandidate("smart_farm_financial_technical_barrier_counterexample", "SMART_FARM_AGRI_TECH", "SMARTFARM_BARRIER", "스마트팜 재무기술 장벽 반례", "KR", "failed_rerating", ("smart_farm",), ("technical_barrier", "subsidy_dependency"), "Adoption barriers cap policy-only smart-farm stories."),
    Round33CaseCandidate("agri_machinery_export_order_candidate", "SMART_FARM_AGRI_TECH", "AGRI_MACH_ORDER", "농기계 수출수주 후보", "KR", "success_candidate", ("agri_automation", "smart_farm_order"), ("weather", "commodity_cycle"), "Agri machinery needs export orders and revenue conversion."),
    Round33CaseCandidate("weather_event_agri_theme_counterexample", "SMART_FARM_AGRI_TECH", "WEATHER_AGRI", "날씨 이벤트 농업테마 반례", "GLOBAL", "failed_rerating", ("food_security",), ("weather_event_reversal", "commodity_cycle"), "Weather-driven price moves are event/cycle, not structural evidence."),
    Round33CaseCandidate("cannabis_rescheduling_stage1_candidate", "CONSUMER_REGULATED_PRODUCT", "CANNABIS_S3", "Cannabis rescheduling Stage1 후보", "US", "event_premium", ("cannabis_rescheduling", "regulatory_approval"), ("legal_conflict", "approval_uncertain"), "Rescheduling can open Stage 1/2 but is not federal legalization or Green evidence."),
    Round33CaseCandidate("cannabis_no_federal_legalization_counterexample", "CONSUMER_REGULATED_PRODUCT", "CANNABIS_NOLEGAL", "Cannabis 연방합법화 부재 반례", "US", "failed_rerating", ("regulated_consumer",), ("legal_conflict", "approval_uncertain"), "Legal conflict can cap cannabis-related rerating."),
    Round33CaseCandidate("e_cigarette_regulatory_approval_candidate", "CONSUMER_REGULATED_PRODUCT", "ECIG_APPROVAL", "전자담배 규제승인 후보", "US", "success_candidate", ("e_cigarette_approval", "repeat_consumption"), ("public_health", "social_backlash"), "Approval can support Watch/Stage 2 if distribution and margin exist."),
    Round33CaseCandidate("regulated_product_crackdown_4c", "CONSUMER_REGULATED_PRODUCT", "REG_CRACK_4C", "규제형 소비재 단속 4C", "GLOBAL", "4c_thesis_break", ("regulated_distribution",), ("regulatory_crackdown", "sales_ban"), "Crackdown or ban is hard thesis-break evidence."),
    Round33CaseCandidate("shein_temu_fast_fashion_scale_candidate", "APPAREL_FAST_FASHION", "SHEIN_TEMU_SCALE", "Shein Temu fast fashion scale 후보", "CN", "success_candidate", ("fast_fashion", "fast_inventory_turn"), ("ip_legal", "product_safety"), "Scale helps only when inventory turn, markdown, compliance, and FCF are visible."),
    Round33CaseCandidate("shein_temu_ip_litigation_4c", "APPAREL_FAST_FASHION", "SHEIN_TEMU_IP_4C", "Shein Temu IP 소송 4C", "CN", "4c_thesis_break", ("cross_border_ecommerce",), ("ip_litigation", "regulatory_crackdown"), "IP litigation can break fast-fashion thesis."),
    Round33CaseCandidate("product_safety_regulation_4c", "APPAREL_FAST_FASHION", "PRODUCT_SAFE_4C", "제품안전 규제 4C", "EU", "4c_thesis_break", ("cross_border_ecommerce",), ("product_safety_crackdown", "regulatory_crackdown"), "Product-safety crackdowns can become 4C for cross-border platforms."),
    Round33CaseCandidate("apparel_inventory_markdown_counterexample_v15", "APPAREL_FAST_FASHION", "APPAREL_MARKDOWN_V15", "의류재고할인 반례 v15", "KR", "failed_rerating", ("apparel_oem",), ("inventory_markdown", "markdown"), "Inventory and markdown erase apparel operating leverage."),
    Round33CaseCandidate("b2b_ai_subscription_candidate", "AI_SOFTWARE_APPLICATION", "B2B_AI_SUB", "B2B AI 구독 후보", "GLOBAL", "success_candidate", ("recurring_subscription_or_api", "b2b_workflow_integration"), ("compute_cost", "copyright"), "AI software can be Green-possible when subscription/API revenue and margin are explicit."),
    Round33CaseCandidate("open_ai_supply_chain_license_risk_counterexample", "AI_SOFTWARE_APPLICATION", "AI_LICENSE_RISK", "오픈AI 공급망 라이선스 리스크 반례", "GLOBAL", "failed_rerating", ("ai_software",), ("license_integrity_failure", "licensing"), "Open AI supply-chain license gaps are a RedTeam risk."),
    Round33CaseCandidate("generative_ai_copyright_risk_4c", "AI_SOFTWARE_APPLICATION", "GENAI_COPY_4C", "생성AI 저작권 4C", "GLOBAL", "4c_thesis_break", ("generative_ai_app",), ("copyright_litigation", "copyright"), "Copyright litigation can break AI app economics."),
    Round33CaseCandidate("compute_cost_margin_pressure_counterexample", "AI_SOFTWARE_APPLICATION", "AI_COMPUTE_PRESS", "AI compute cost 마진압박 반례", "GLOBAL", "failed_rerating", ("api_usage",), ("compute_cost_margin_pressure", "model_dependency"), "Usage growth without compute-cost control is weak evidence."),
    Round33CaseCandidate("nft_theme_rally_no_revenue_counterexample", "METAVERSE_NFT_THEME", "NFT_NOREV", "NFT 테마 무매출 반례", "GLOBAL", "overheat", ("nft_theme", "price_volume_spike"), ("no_revenue", "price_only_rally"), "NFT price rally without platform fees remains overheat."),
    Round33CaseCandidate("metaverse_platform_no_fcf_counterexample", "METAVERSE_NFT_THEME", "META_NOFCF", "메타버스 플랫폼 FCF 부재 반례", "GLOBAL", "failed_rerating", ("metaverse",), ("no_revenue", "fcf_absent"), "Metaverse platform narrative needs FCF conversion."),
    Round33CaseCandidate("digital_asset_infra_vs_nft_split_case", "METAVERSE_NFT_THEME", "INFRA_VS_NFT", "디지털자산 인프라 NFT 분리 사례", "GLOBAL", "event_premium", ("virtual_asset_narrative",), ("extreme_theme", "regulatory"), "Stablecoin/STO infrastructure must be separated from NFT narrative."),
    Round33CaseCandidate("nft_liquidity_collapse_4c", "METAVERSE_NFT_THEME", "NFT_LIQ_4C", "NFT 유동성 붕괴 4C", "GLOBAL", "4c_thesis_break", ("nft_theme",), ("liquidity_collapse", "theme_unwind"), "Liquidity collapse is thesis-break evidence for NFT themes."),
    Round33CaseCandidate("egg_price_spike_event_case", "FOOD_AGRI_LIVESTOCK_CYCLE", "EGG_SPIKE", "계란가격 급등 이벤트", "GLOBAL", "one_off", ("egg_price_spike", "price_pass_through"), ("price_normalization", "disease_event"), "Egg price spikes are event/cycle unless recurring demand and cost control are proven."),
    Round33CaseCandidate("avian_flu_livestock_event_counterexample", "FOOD_AGRI_LIVESTOCK_CYCLE", "AVIAN_FLU", "조류독감 축산 이벤트 반례", "GLOBAL", "failed_rerating", ("livestock_disease",), ("disease_normalization", "one_off_supply_shock"), "Disease events should not become structural Green."),
    Round33CaseCandidate("feed_cost_pressure_counterexample", "FOOD_AGRI_LIVESTOCK_CYCLE", "FEED_COST", "사료비 압박 반례", "KR", "failed_rerating", ("feed_cost",), ("feed_cost_spike", "cost_control_missing"), "Feed-cost pressure can erase livestock pricing benefit."),
    Round33CaseCandidate("smart_farm_recurring_service_candidate", "FOOD_AGRI_LIVESTOCK_CYCLE", "SMARTFARM_SERVICE", "스마트팜 반복서비스 후보", "KR", "success_candidate", ("smart_farm_service", "recurring_non_event_demand"), ("subsidy", "technical_barrier"), "Recurring smart-farm service is stronger than livestock price-event evidence."),
)


def target_for(target_id: str) -> Round33ScoreTarget | None:
    for target in ROUND33_SCORE_TARGETS:
        if target.target_id == target_id:
            return target
    return None


def round33_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND33_CASE_CANDIDATES:
        target = target_for(candidate.target_id)
        if target is None:
            raise ValueError(f"unknown target_id: {candidate.target_id}")
        weights = target.score_weight.as_dict()
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market=candidate.market,
            sector_raw=candidate.target_id,
            primary_archetype=target.canonical_archetype,
            expected_group=candidate.expected_group,
            large_sector=target.large_sector.value,
            case_type=candidate.case_type,
            evidence_summary=(
                f"Round33 v1.8 calibration candidate for {candidate.target_id}; "
                "stage dates, prices, and numeric evidence remain unfilled."
            ),
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=tuple(field for field in candidate.evidence_fields if field in target.green_conditions),
            stage3_evidence=(),
            stage4c_evidence=candidate.red_flag_fields if candidate.case_type == "4c_thesis_break" else (),
            must_have_fields=target.green_conditions,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason="; ".join(candidate.red_flag_fields) if candidate.case_type not in {"success_candidate", "structural_success", "cyclical_success"} else None,
            score_price_alignment="unknown",
            rerating_result="event_premium" if candidate.case_type == "event_premium" else "unknown",
            price_pattern="unknown",
            score_weight_hint={
                "eps_fcf": float(weights["eps_fcf"]),
                "visibility": float(weights["structural_visibility"]),
                "bottleneck": float(weights["bottleneck_pricing"]),
                "mispricing": float(weights["market_mispricing"]),
                "valuation": float(weights["valuation"]),
                "capital_allocation": float(weights["capital_allocation"]),
                "information_confidence": float(weights["information_confidence"]),
            },
            green_guardrails=(
                "do_not_use_case_as_candidate_input",
                "do_not_change_production_scoring",
                "require_price_path_validation",
                "require_cross_evidence_for_green",
                "theme_label_is_not_score_evidence",
                *target.red_flags,
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(price_validation_status="needs_price_backfill"),
            data_quality=CaseDataQuality(False, False, False, 0.0),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round33_score_profile_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for target in ROUND33_SCORE_TARGETS:
        weights = target.score_weight.as_dict()
        rows.append(
            {
                "target_id": target.target_id,
                "large_sector": target.large_sector.value,
                "canonical_archetype": target.canonical_archetype.value,
                "posture": target.posture.value,
                "eps_fcf": str(weights["eps_fcf"]),
                "structural_visibility": str(weights["structural_visibility"]),
                "bottleneck_pricing": str(weights["bottleneck_pricing"]),
                "market_mispricing": str(weights["market_mispricing"]),
                "valuation": str(weights["valuation"]),
                "capital_allocation": str(weights["capital_allocation"]),
                "information_confidence": str(weights["information_confidence"]),
                "stage1_signals": "|".join(target.stage1_signals),
                "stage2_signals": "|".join(target.stage2_signals),
                "stage3_conditions": "|".join(target.stage3_conditions),
                "green_conditions": "|".join(target.green_conditions),
                "red_flags": "|".join(target.red_flags),
                "stage4c_conditions": "|".join(target.stage4c_conditions),
                "production_scoring_changed": str(target.production_scoring_changed).lower(),
                "normalization_point": target.normalization_point,
            }
        )
    return tuple(rows)


def round33_case_candidate_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND33_CASE_CANDIDATES:
        target = target_for(candidate.target_id)
        assert target is not None
        rows.append(
            {
                "case_id": candidate.case_id,
                "target_id": candidate.target_id,
                "symbol": candidate.symbol,
                "company_name": candidate.company_name,
                "market": candidate.market,
                "case_type": candidate.case_type,
                "canonical_archetype": target.canonical_archetype.value,
                "posture": target.posture.value,
                "evidence_fields": "|".join(candidate.evidence_fields),
                "red_flag_fields": "|".join(candidate.red_flag_fields),
                "price_validation_status": "needs_price_backfill",
                "production_input": "false",
                "notes": candidate.notes,
            }
        )
    return tuple(rows)


def round33_summary() -> dict[str, int | bool]:
    records = round33_case_records()
    positive = sum(1 for record in records if record.case_type in {"success_candidate", "structural_success", "cyclical_success"})
    stage4c = sum(1 for record in records if record.case_type == "4c_thesis_break")
    stage4b = sum(1 for record in records if record.case_type == "4b_watch")
    return {
        "target_count": len(ROUND33_SCORE_TARGETS),
        "case_candidate_count": len(records),
        "success_candidate_count": positive,
        "counterexample_or_risk_count": len(records) - positive,
        "stage4b_case_count": stage4b,
        "stage4c_case_count": stage4c,
        "green_possible_count": sum(1 for target in ROUND33_SCORE_TARGETS if target.posture == Round10ThemePosture.GREEN_POSSIBLE),
        "watch_yellow_first_count": sum(1 for target in ROUND33_SCORE_TARGETS if target.posture == Round10ThemePosture.WATCH_YELLOW_FIRST),
        "redteam_first_count": sum(1 for target in ROUND33_SCORE_TARGETS if target.posture == Round10ThemePosture.REDTEAM_FIRST),
        "production_scoring_changed": False,
        "case_records_are_candidate_generation_input": False,
    }


def write_round33_score_weight_reports(
    *,
    output_directory: str | Path = ROUND33_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND33_DEFAULT_CASES_PATH,
    score_profile_path: str | Path = ROUND33_DEFAULT_SCORE_PROFILE_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    cases = Path(cases_path)
    score_profiles = Path(score_profile_path)
    cases.parent.mkdir(parents=True, exist_ok=True)
    score_profiles.parent.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": cases,
        "score_profiles": score_profiles,
        "summary": output / "round33_score_weight_v18_summary.md",
        "case_matrix": output / "round33_case_candidate_matrix.csv",
        "green_guardrails": output / "round33_green_guardrail_review.md",
        "media_cycle": output / "round33_media_ad_cycle_review.md",
        "ai_ip_risk": output / "round33_ai_software_ip_risk_review.md",
        "event_cycle": output / "round33_event_cycle_guardrail_review.md",
        "price_validation_plan": output / "round33_price_validation_plan.md",
    }
    _write_case_jsonl(round33_case_records(), cases)
    _write_rows(round33_score_profile_rows(), score_profiles)
    _write_rows(round33_case_candidate_rows(), paths["case_matrix"])
    paths["summary"].write_text(render_round33_summary_markdown(), encoding="utf-8")
    paths["green_guardrails"].write_text(render_round33_green_guardrail_markdown(), encoding="utf-8")
    paths["media_cycle"].write_text(render_round33_media_cycle_markdown(), encoding="utf-8")
    paths["ai_ip_risk"].write_text(render_round33_ai_ip_risk_markdown(), encoding="utf-8")
    paths["event_cycle"].write_text(render_round33_event_cycle_guardrail_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round33_price_validation_plan_markdown(), encoding="utf-8")
    return paths


def render_round33_summary_markdown() -> str:
    summary = round33_summary()
    lines = [
        "# Round-33 Score-Weight v1.8 Summary",
        "",
        f"- source_round: `{ROUND33_SOURCE_ROUND_PATH}`",
        f"- target_count: {summary['target_count']}",
        f"- case_candidate_count: {summary['case_candidate_count']}",
        f"- success_candidate_count: {summary['success_candidate_count']}",
        f"- counterexample_or_risk_count: {summary['counterexample_or_risk_count']}",
        f"- stage4b_case_count: {summary['stage4b_case_count']}",
        f"- stage4c_case_count: {summary['stage4c_case_count']}",
        f"- green_possible_count: {summary['green_possible_count']}",
        f"- watch_yellow_first_count: {summary['watch_yellow_first_count']}",
        f"- redteam_first_count: {summary['redteam_first_count']}",
        "- production_scoring_changed: false",
        "- case_records_are_candidate_generation_input: false",
        "",
        "## Interpretation",
        "- Round 33 adds v1.8 calibration cases and target weights only.",
        "- Example: streaming ad platforms can be candidates when ad ARPU, owned ad platform, inventory, and OPM are visible; traditional media ad cycles remain capped.",
        "- Example: AI software can be Green-possible with recurring subscription/API revenue, but copyright, licensing, data privacy, and compute cost are hard gates.",
        "- Example: NFT/metaverse and livestock disease/price events stay RedTeam-first because price or volume spikes are usually not recurring FCF.",
        "- Theme names, case IDs, regulation headlines, app features, and price rallies are not score evidence by themselves.",
    ]
    return "\n".join(lines) + "\n"


def render_round33_green_guardrail_markdown() -> str:
    lines = [
        "# Round-33 Green Guardrail Review",
        "",
        "| target | posture | Green unlock evidence | Red flags |",
        "|---|---|---|---|",
    ]
    for target in ROUND33_SCORE_TARGETS:
        lines.append(
            "| "
            f"{target.target_id} | {target.posture.value} | "
            f"{', '.join(target.green_conditions)} | {', '.join(target.red_flags)} |"
        )
    lines.extend(
        [
            "",
            "## What Not To Change",
            "- Do not apply v1.8 weights to production scoring yet.",
            "- Do not use case IDs or theme labels as candidate-generation input.",
            "- Do not invent stage dates, prices, ad ARPU, packaging price hikes, smart-farm contracts, cannabis approvals, inventory turnover, AI subscription revenue, license status, NFT transaction volume, or livestock disease normalization.",
            "- Do not lower Stage 3-Green thresholds to improve recall.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round33_media_cycle_markdown() -> str:
    return "\n".join(
        [
            "# Round-33 Media / Ad Cycle Review",
            "",
            "Advertising must be split between platform monetization and traditional ad-cycle exposure.",
            "",
            "## Candidate Evidence",
            "- Subscription plus advertising hybrid model.",
            "- Owned ad platform and repeat ad inventory.",
            "- Ad ARPU and OPM improvement.",
            "",
            "## Cycle / Decline Risks",
            "- Client budget cuts.",
            "- Traditional broadcast or newspaper ad decline.",
            "- Privacy regulation or platform shift that weakens monetization.",
        ]
    ) + "\n"


def render_round33_ai_ip_risk_markdown() -> str:
    return "\n".join(
        [
            "# Round-33 AI Software IP / Cost Risk Review",
            "",
            "AI software is not scored because it has an AI feature. It needs repeat revenue and margin evidence.",
            "",
            "## Green-Possible Evidence",
            "- Recurring subscription or API revenue.",
            "- Customer lock-in and B2B workflow integration.",
            "- Compute cost control and OPM improvement.",
            "",
            "## RedTeam Gates",
            "- Copyright litigation or license integrity failure.",
            "- Treat copyright, licensing, and compute cost as linked Green gates.",
            "- Data privacy risk.",
            "- Model-provider dependency.",
            "- Compute cost rising faster than revenue.",
        ]
    ) + "\n"


def render_round33_event_cycle_guardrail_markdown() -> str:
    return "\n".join(
        [
            "# Round-33 Event / Cycle Guardrail Review",
            "",
            "Round 33 keeps event-heavy areas from masquerading as structural E2R.",
            "",
            "## Green-Restricted Areas",
            "- NFT/metaverse rally without real platform fees or FCF.",
            "- Cannabis or e-cigarette headlines without legal sales, distribution, and margin evidence.",
            "- Livestock, egg, feed, disease, or weather events without recurring non-event demand.",
            "- Paper/packaging volume or M&A stories without pricing power and FCF.",
            "",
            "## Simple Example",
            "- If egg prices rise because of disease-related supply shock, that can be Stage 1 event evidence.",
            "- It should not become Stage 3-Green unless separate recurring demand, cost control, and non-event FCF evidence exist.",
        ]
    ) + "\n"


def render_round33_price_validation_plan_markdown() -> str:
    return "\n".join(
        [
            "# Round-33 Price Validation Plan",
            "",
            "1. Backfill tradable case price paths where symbols exist.",
            "2. Keep synthetic, global reference, event, and theme cases as `needs_price_backfill` or `missing_price_data`.",
            "3. Calculate MFE/MAE, peak, drawdown, and below-entry flags only from source data.",
            "4. Run shadow score-price alignment before any production scoring change.",
            "",
            "## Priority Validation",
            "- Media/ad: platform monetization versus client budget and traditional ad decline.",
            "- Packaging/agri/livestock: pricing and FCF versus cost, disease, weather, and mature-cycle risks.",
            "- Regulated consumer/apparel: approval and channel evidence versus legal, IP, product safety, inventory, and markdown.",
            "- AI software/NFT: recurring revenue and compute/IP control versus theme-only liquidity or no-revenue rallies.",
        ]
    ) + "\n"


def _write_case_jsonl(records: Iterable[E2RCaseRecord], path: Path) -> Path:
    lines = []
    for record in records:
        record.validate()
        lines.append(json.dumps(record.as_dict(), ensure_ascii=False, sort_keys=True))
    path.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")
    return path


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
    "ROUND33_CASE_CANDIDATES",
    "ROUND33_DEFAULT_CASES_PATH",
    "ROUND33_DEFAULT_OUTPUT_DIRECTORY",
    "ROUND33_DEFAULT_SCORE_PROFILE_PATH",
    "ROUND33_SCORE_TARGETS",
    "ROUND33_SOURCE_ROUND_PATH",
    "Round33CaseCandidate",
    "Round33ScoreTarget",
    "Round33ScoreWeightDraft",
    "render_round33_ai_ip_risk_markdown",
    "render_round33_event_cycle_guardrail_markdown",
    "render_round33_green_guardrail_markdown",
    "render_round33_media_cycle_markdown",
    "render_round33_price_validation_plan_markdown",
    "render_round33_summary_markdown",
    "round33_case_candidate_rows",
    "round33_case_records",
    "round33_score_profile_rows",
    "round33_summary",
    "target_for",
    "write_round33_score_weight_reports",
]
