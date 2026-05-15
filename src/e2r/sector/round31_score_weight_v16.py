"""Round-31 cases_v13 expansion and score-weight v1.6 hypotheses.

Round 31 strengthens data-center REITs, waste/recycling, dental and medical
devices, regulated consumer products, apparel/fast-fashion, digital assets,
AI data-center infrastructure, and shareholder-return value-up. It is
report-only calibration material. Production feature engineering, scoring,
staging, and RedTeam code must not import this module.
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


ROUND31_SOURCE_ROUND_PATH = "docs/round/round_31.md"
ROUND31_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round31_score_weight_v16"
ROUND31_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_v13_round31.jsonl"
ROUND31_DEFAULT_SCORE_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round31_v16.csv"


@dataclass(frozen=True)
class Round31ScoreWeightDraft:
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
class Round31ScoreTarget:
    target_id: str
    large_sector: Round10LargeSector
    canonical_archetype: E2RArchetype
    posture: Round10ThemePosture
    score_weight: Round31ScoreWeightDraft
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
class Round31CaseCandidate:
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


ROUND31_SCORE_TARGETS: tuple[Round31ScoreTarget, ...] = (
    Round31ScoreTarget(
        "DATA_CENTER_REIT_INFRASTRUCTURE",
        Round10LargeSector.CONSTRUCTION_REAL_ESTATE_MATERIALS,
        E2RArchetype.AI_DATA_CENTER_INFRASTRUCTURE,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round31ScoreWeightDraft(18, 23, 18, 13, 13, 5, 5),
        ("ai_datacenter_reit", "hyperscale_tenant", "liquid_cooling_asset", "idc_asset"),
        ("hyperscale_long_lease", "occupancy_high", "power_cooling_land_secured", "ffo_affo_growth"),
        ("tenant_quality", "funding_cost_controlled", "capex_to_affo_visible"),
        ("hyperscale_long_lease", "occupancy_high", "power_cooling_land_secured", "ffo_affo_growth", "funding_cost_controlled"),
        ("capex_burden", "power_water_constraint", "tenant_concentration", "funding_cost", "ai_theme_only"),
        ("power_water_constraint", "affo_dilution", "funding_cost_spike", "tenant_loss"),
        "Data-center REITs are Green-possible only when lease, occupancy, FFO/AFFO, power/cooling/land, and funding cost are source-backed.",
    ),
    Round31ScoreTarget(
        "WASTE_RECYCLING_ENVIRONMENT",
        Round10LargeSector.BATTERY_EV_GREEN,
        E2RArchetype.UTILITIES_REGULATED_TARIFF,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round31ScoreWeightDraft(18, 22, 15, 13, 12, 3, 5),
        ("waste_platform", "recycling_policy", "battery_recycling_keyword", "waste_to_energy"),
        ("permit_or_license", "facility_utilization", "long_term_processing_contract", "recurring_fcf"),
        ("capacity_rights", "customer_diversification", "capex_burden_low", "volume_visible"),
        ("permit_or_license", "facility_utilization", "long_term_processing_contract", "recurring_fcf", "capex_burden_low"),
        ("utilization", "commodity_price", "capex", "regulation_delay", "volume_missing"),
        ("low_utilization", "capex_burden", "commodity_price_drop", "regulation_delay"),
        "Waste treatment can be Green when permits, facilities, utilization, contracts, and recurring FCF are present.",
    ),
    Round31ScoreTarget(
        "MEDICAL_DEVICE_DENTAL_IMPLANT",
        Round10LargeSector.BIOTECH_HEALTHCARE_DEVICE,
        E2RArchetype.MEDICAL_DEVICE_HEALTHCARE_EXPORT,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round31ScoreWeightDraft(20, 22, 13, 14, 12, 0, 5),
        ("dental_implant_growth", "medical_device_export", "approval_or_channel", "consumable_revenue"),
        ("export_country_expansion", "recurring_procedure_consumable", "opm_roe_improvement", "channel_quality"),
        ("approval_stable", "repeat_consumable_revenue", "pricing_pressure_low"),
        ("export_country_expansion", "recurring_procedure_consumable", "approval_stable", "opm_roe_improvement", "channel_quality"),
        ("approval", "vbp_price_control", "safety", "competition", "channel_quality", "single_device_no_consumable"),
        ("approval_delay", "vbp_price_control", "asp_drop", "safety_issue"),
        "Dental/medical devices can be Green, but price control, approval, safety, and consumable repeatability are gates.",
    ),
    Round31ScoreTarget(
        "CONSUMER_REGULATED_PRODUCT",
        Round10LargeSector.CONSUMER_RETAIL_BRAND,
        E2RArchetype.RETAIL_DOMESTIC_CONSUMER,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round31ScoreWeightDraft(18, 14, 8, 12, 10, 0, 5),
        ("regulated_consumer_product", "e_cigarette", "alcohol_or_cannabis_policy", "brand_distribution"),
        ("regulatory_approval", "repeat_consumption", "distribution_network", "stable_fcf"),
        ("regulation_stable", "brand_lock_in", "legal_social_risk_low"),
        ("regulatory_approval", "repeat_consumption", "distribution_network", "stable_fcf", "legal_social_risk_low"),
        ("regulation", "public_health", "legal", "social_backlash", "approval_uncertain"),
        ("sales_ban", "regulatory_reversal", "public_health_litigation", "social_backlash"),
        "Regulated consumer products are Watch-first because approval or bans can flip the stage.",
    ),
    Round31ScoreTarget(
        "APPAREL_FAST_FASHION_BRAND_OEM",
        Round10LargeSector.CONSUMER_RETAIL_BRAND,
        E2RArchetype.RETAIL_DOMESTIC_CONSUMER,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round31ScoreWeightDraft(18, 16, 8, 14, 12, 0, 5),
        ("fashion_brand_growth", "kfashion_channel", "apparel_oem_order", "fast_fashion_scale"),
        ("overseas_channel_expansion", "inventory_turn_stable", "markdown_control", "opm_fcf_improvement"),
        ("brand_or_customer_diversification", "discount_rate_low", "ip_legal_risk_low"),
        ("overseas_channel_expansion", "inventory_turn_stable", "markdown_control", "opm_fcf_improvement", "ip_legal_risk_low"),
        ("inventory", "markdown", "fashion_cycle", "channel_concentration", "ip_legal_risk", "ultra_low_price_competition"),
        ("inventory_markdown", "ip_litigation", "order_slowdown", "channel_concentration_hit"),
        "Apparel is more conservative than K-food/K-beauty because inventory, markdown, IP, and fast-fashion competition are stronger risks.",
    ),
    Round31ScoreTarget(
        "DIGITAL_ASSET_TOKENIZATION",
        Round10LargeSector.FINANCIAL_CAPITAL_DIGITAL,
        E2RArchetype.FINANCIAL_SPREAD_BALANCE_SHEET,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round31ScoreWeightDraft(16, 18, 8, 16, 12, 3, 5),
        ("stablecoin_keyword", "sto_policy", "tokenization_infra", "nft_or_blockchain_theme"),
        ("regulatory_approval", "issuance_or_transaction_volume", "payment_network_adoption", "fee_or_deposit_revenue"),
        ("repeat_financial_infra_revenue", "security_risk_low", "liquidity_visible"),
        ("regulatory_approval", "issuance_or_transaction_volume", "payment_network_adoption", "fee_or_deposit_revenue", "security_risk_low"),
        ("regulation", "security", "adoption", "liquidity", "no_revenue", "nft_theme_only"),
        ("regulatory_delay", "security_incident", "liquidity_collapse", "no_revenue_model"),
        "Stablecoin/STO infrastructure is not the same as NFT/theme exposure; revenue model and volume are required.",
    ),
    Round31ScoreTarget(
        "AI_DATA_CENTER_INFRASTRUCTURE",
        Round10LargeSector.AI_SEMICONDUCTOR_ELECTRONICS,
        E2RArchetype.AI_DATA_CENTER_INFRASTRUCTURE,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round31ScoreWeightDraft(22, 23, 20, 14, 12, 2, 5),
        ("ai_capex", "power_grid", "cooling_hvac", "ai_server_pcb", "datacenter_reit", "ppa"),
        ("orders_or_leases", "bottleneck_asset", "delivery_schedule", "op_eps_revision", "project_financing_visible"),
        ("multi_axis_infra_bottleneck", "project_delay_risk_low", "revenue_exposure_clear"),
        ("orders_or_leases", "bottleneck_asset", "delivery_schedule", "op_eps_revision", "project_delay_risk_low"),
        ("ai_capex_cut", "project_delay", "grid_constraint", "overbuild", "water_power_constraint", "revenue_exposure_unclear"),
        ("ai_capex_cut", "project_delay", "grid_constraint", "overbuild", "water_power_constraint"),
        "AI infrastructure must be split into power, cooling, real estate, PPA, and PCB axes rather than one broad AI theme.",
    ),
    Round31ScoreTarget(
        "VALUE_UP_SHAREHOLDER_RETURN",
        Round10LargeSector.FINANCIAL_CAPITAL_DIGITAL,
        E2RArchetype.VALUE_UP_SHAREHOLDER_RETURN,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round31ScoreWeightDraft(12, 18, 4, 20, 25, 10, 5),
        ("low_pbr", "nav_discount", "buyback_or_dividend", "valueup_policy"),
        ("actual_cancellation", "repeat_dividend_policy", "roe_improvement", "nav_discount_closure"),
        ("pbr_roe_frame_change", "capital_return_execution", "fcf_support", "governance_improvement"),
        ("actual_cancellation", "repeat_dividend_policy", "roe_improvement", "nav_discount_closure", "fcf_support"),
        ("governance", "execution", "low_roe", "no_cancellation", "credit_cost", "index_inclusion_only"),
        ("return_execution_failure", "roe_deterioration", "governance_discount_persistent", "credit_cost_spike"),
        "Value-up is execution, not policy label: cancellation, dividend, ROE/NAV, governance, and FCF are gates.",
    ),
)


ROUND31_CASE_CANDIDATES: tuple[Round31CaseCandidate, ...] = (
    Round31CaseCandidate("blackstone_digital_infra_reit_candidate", "DATA_CENTER_REIT_INFRASTRUCTURE", "BDIV", "Blackstone Digital Infrastructure REIT", "US", "success_candidate", ("hyperscale_long_lease", "ai_datacenter_reit"), ("funding_cost", "tenant_concentration"), "Data-center REIT candidate needs lease, occupancy, FFO/AFFO, and funding validation."),
    Round31CaseCandidate("equinix_malaysia_ai_liquid_cooling_candidate", "DATA_CENTER_REIT_INFRASTRUCTURE", "EQIX_MY", "Equinix Malaysia AI liquid cooling", "US", "success_candidate", ("liquid_cooling_asset", "power_cooling_land_secured"), ("power_water_constraint", "funding_cost"), "AI-ready IDC candidate is positive only if power/water and economics are controlled."),
    Round31CaseCandidate("data_center_reit_power_water_constraint_4c", "DATA_CENTER_REIT_INFRASTRUCTURE", "DC_POWER_4C", "데이터센터 전력수자원 제약4C", "US", "4c_thesis_break", ("ai_datacenter_reit",), ("power_water_constraint", "project_delay"), "Power/water constraints can break data-center visibility."),
    Round31CaseCandidate("data_center_reit_capex_affo_pressure_counterexample", "DATA_CENTER_REIT_INFRASTRUCTURE", "DC_AFFO_PRESS", "데이터센터REIT AFFO 압박", "US", "failed_rerating", ("idc_asset",), ("capex_burden", "affo_dilution"), "CAPEX growth without AFFO improvement is not Green evidence."),
    Round31CaseCandidate("eqt_kj_environment_waste_platform_candidate", "WASTE_RECYCLING_ENVIRONMENT", "KJ_ENV", "EQT KJ Environment 폐기물 플랫폼", "KR", "success_candidate", ("waste_platform", "permit_or_license", "facility_utilization"), ("capex", "regulation_delay"), "Waste platform can be recurring infrastructure when permits and utilization are visible."),
    Round31CaseCandidate("waste_permit_recurring_fcf_candidate", "WASTE_RECYCLING_ENVIRONMENT", "WASTE_FCF", "폐기물 허가권 반복 FCF 후보", "KR", "success_candidate", ("permit_or_license", "long_term_processing_contract", "recurring_fcf"), ("utilization", "capex"), "Permit and recurring FCF are stronger than ESG labels."),
    Round31CaseCandidate("battery_recycling_no_volume_counterexample", "WASTE_RECYCLING_ENVIRONMENT", "RECY_NOVOL_V13", "폐배터리 회수량 부재", "KR", "failed_rerating", ("battery_recycling_keyword",), ("volume_missing", "commodity_price"), "Battery recycling needs actual collection volume and economics."),
    Round31CaseCandidate("recycling_capex_low_utilization_4c", "WASTE_RECYCLING_ENVIRONMENT", "RECY_UTIL_4C", "재활용CAPEX저가동률4C", "KR", "4c_thesis_break", ("recycling_policy",), ("low_utilization", "capex_burden"), "Low utilization after CAPEX can break recycling FCF."),
    Round31CaseCandidate("straumann_dental_implant_growth_candidate", "MEDICAL_DEVICE_DENTAL_IMPLANT", "STMN", "Straumann dental implant growth", "EU", "success_candidate", ("dental_implant_growth", "export_country_expansion", "opm_roe_improvement"), ("vbp_price_control", "competition"), "Dental implant growth must be paired with price-control risk checks."),
    Round31CaseCandidate("dental_implant_vbp_price_control_counterexample", "MEDICAL_DEVICE_DENTAL_IMPLANT", "DENTAL_VBP", "임플란트 VBP 가격통제", "CN", "failed_rerating", ("dental_implant_growth",), ("vbp_price_control", "asp_drop"), "VBP can cap medical-device pricing power."),
    Round31CaseCandidate("medical_device_approval_delay_4c", "MEDICAL_DEVICE_DENTAL_IMPLANT", "MED_APPROVAL_4C", "의료기기허가지연4C", "KR", "4c_thesis_break", ("medical_device_export",), ("approval_delay", "channel_delay"), "Approval delay can break export medical-device rerating."),
    Round31CaseCandidate("single_device_no_consumable_counterexample", "MEDICAL_DEVICE_DENTAL_IMPLANT", "DEVICE_NOCONS", "단일장비무소모품반례", "KR", "failed_rerating", ("medical_device_export",), ("single_device_no_consumable", "repeat_revenue_missing"), "Single device sale without consumables weakens visibility."),
    Round31CaseCandidate("juul_fda_approval_stage2_candidate", "CONSUMER_REGULATED_PRODUCT", "JUUL_APPROVAL", "Juul FDA 승인 Stage2", "US", "success_candidate", ("regulatory_approval", "repeat_consumption", "distribution_network"), ("public_health", "social_backlash"), "FDA approval can move regulated consumer products to Watch/Stage 2."),
    Round31CaseCandidate("juul_prior_fda_ban_4c", "CONSUMER_REGULATED_PRODUCT", "JUUL_BAN_4C", "Juul FDA 판매금지4C", "US", "4c_thesis_break", ("e_cigarette",), ("sales_ban", "regulatory_reversal"), "Sales ban is hard 4C-style evidence."),
    Round31CaseCandidate("e_cigarette_youth_regulation_risk", "CONSUMER_REGULATED_PRODUCT", "ECIG_YOUTH", "전자담배 청소년 규제 위험", "US", "failed_rerating", ("e_cigarette",), ("public_health", "legal", "social_backlash"), "Public-health regulation can cap repeat-consumption economics."),
    Round31CaseCandidate("cannabis_policy_event_only_counterexample", "CONSUMER_REGULATED_PRODUCT", "CANNABIS_POLICY", "마리화나 정책 이벤트", "US", "event_premium", ("alcohol_or_cannabis_policy",), ("approval_uncertain", "policy_event_only"), "Cannabis policy headline is event premium until approval and FCF exist."),
    Round31CaseCandidate("shein_fast_fashion_scale_candidate", "APPAREL_FAST_FASHION_BRAND_OEM", "SHEIN_SCALE", "Shein fast-fashion scale", "CN", "success_candidate", ("fast_fashion_scale", "overseas_channel_expansion"), ("ip_legal_risk", "ultra_low_price_competition"), "Fast-fashion scale needs inventory, markdown, and legal-risk checks."),
    Round31CaseCandidate("shein_temu_ip_litigation_risk_4c", "APPAREL_FAST_FASHION_BRAND_OEM", "SHEIN_TEMU_4C", "Shein Temu IP litigation", "CN", "4c_thesis_break", ("fast_fashion_scale",), ("ip_litigation", "ultra_low_price_competition"), "IP litigation and price competition can break apparel thesis."),
    Round31CaseCandidate("apparel_inventory_markdown_counterexample", "APPAREL_FAST_FASHION_BRAND_OEM", "APPAREL_MARKDOWN", "의류재고할인반례", "KR", "failed_rerating", ("fashion_brand_growth",), ("inventory_markdown", "fashion_cycle"), "Inventory and markdown can erase apparel OPM."),
    Round31CaseCandidate("kfashion_channel_expansion_candidate", "APPAREL_FAST_FASHION_BRAND_OEM", "KFASHION_CHANNEL", "K패션 채널확장 후보", "KR", "success_candidate", ("kfashion_channel", "overseas_channel_expansion", "opm_fcf_improvement"), ("channel_concentration", "inventory"), "K-fashion can be Watch-to-Green when channel and FCF improve."),
    Round31CaseCandidate("stablecoin_payment_infra_candidate", "DIGITAL_ASSET_TOKENIZATION", "STABLE_PAY", "스테이블코인 결제 인프라 후보", "KR", "success_candidate", ("regulatory_approval", "payment_network_adoption", "fee_or_deposit_revenue"), ("security", "liquidity"), "Stablecoin payment infrastructure needs approval, volume, and fee/deposit revenue."),
    Round31CaseCandidate("sto_regulation_no_revenue_counterexample", "DIGITAL_ASSET_TOKENIZATION", "STO_NOREV_V13", "STO 규제 무매출 반례", "KR", "failed_rerating", ("sto_policy",), ("no_revenue", "adoption"), "STO regulation without revenue remains Watch."),
    Round31CaseCandidate("nft_theme_overheat_counterexample", "DIGITAL_ASSET_TOKENIZATION", "NFT_OVERHEAT_V13", "NFT 테마 과열 반례", "KR", "overheat", ("nft_or_blockchain_theme",), ("nft_theme_only", "liquidity_collapse"), "NFT theme is separate from stablecoin/STO infra."),
    Round31CaseCandidate("crypto_related_stock_no_revenue_counterexample", "DIGITAL_ASSET_TOKENIZATION", "CRYPTO_NOREV_V13", "코인관련주 무매출 반례", "KR", "failed_rerating", ("tokenization_infra",), ("no_revenue", "revenue_exposure_unclear"), "Crypto-related stock label is not score evidence."),
    Round31CaseCandidate("blackstone_ai_datacenter_reit_candidate", "AI_DATA_CENTER_INFRASTRUCTURE", "BDIV_AI", "Blackstone AI datacenter REIT", "US", "success_candidate", ("datacenter_reit", "orders_or_leases"), ("funding_cost", "tenant_concentration"), "AI infra candidate through data-center lease economics."),
    Round31CaseCandidate("equinix_ai_datacenter_liquid_cooling_candidate", "AI_DATA_CENTER_INFRASTRUCTURE", "EQIX_AI", "Equinix AI liquid cooling", "US", "success_candidate", ("cooling_hvac", "bottleneck_asset"), ("water_power_constraint", "project_delay"), "Cooling and liquid cooling are AI infra axes when revenue exposure is clear."),
    Round31CaseCandidate("ai_datacenter_power_water_constraint_4c", "AI_DATA_CENTER_INFRASTRUCTURE", "AI_POWER_4C", "AI 데이터센터 전력수자원4C", "US", "4c_thesis_break", ("ai_capex",), ("water_power_constraint", "grid_constraint"), "Power and water constraints can break AI infrastructure projects."),
    Round31CaseCandidate("ai_capex_overbuild_counterexample", "AI_DATA_CENTER_INFRASTRUCTURE", "AI_OVERBUILD_V13", "AI CAPEX 과잉 반례", "US", "failed_rerating", ("ai_capex",), ("overbuild", "revenue_exposure_unclear"), "AI CAPEX theme without specific revenue exposure is not Green evidence."),
    Round31CaseCandidate("buyback_cancellation_success_candidate", "VALUE_UP_SHAREHOLDER_RETURN", "BUYBACK_CANCEL_V13", "자사주소각 성공 후보", "KR", "success_candidate", ("actual_cancellation", "repeat_dividend_policy", "roe_improvement"), ("execution", "governance"), "Actual cancellation is stronger than buyback announcement."),
    Round31CaseCandidate("low_pbr_low_roe_value_trap", "VALUE_UP_SHAREHOLDER_RETURN", "LOWPBR_LOWROE_V13", "저PBR 저ROE 가치함정", "KR", "failed_rerating", ("low_pbr",), ("low_roe", "weak_fcf"), "Low PBR without ROE/FCF is value trap."),
    Round31CaseCandidate("buyback_no_cancel_counterexample", "VALUE_UP_SHAREHOLDER_RETURN", "BUYBACK_NOCANCEL_V13", "자사주 미소각 반례", "KR", "failed_rerating", ("buyback_or_dividend",), ("no_cancellation", "execution"), "Buyback without cancellation can fail value-up rerating."),
    Round31CaseCandidate("governance_discount_persistent_counterexample", "VALUE_UP_SHAREHOLDER_RETURN", "GOV_DISCOUNT_V13", "지배구조 할인 지속 반례", "KR", "failed_rerating", ("nav_discount",), ("governance_discount_persistent", "execution"), "Governance discount can remain justified without execution."),
)


def target_for(target_id: str) -> Round31ScoreTarget | None:
    for target in ROUND31_SCORE_TARGETS:
        if target.target_id == target_id:
            return target
    return None


def round31_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND31_CASE_CANDIDATES:
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
                f"Round31 v1.6 calibration candidate for {candidate.target_id}; "
                "stage dates, prices, and numeric evidence remain unfilled."
            ),
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=tuple(field for field in candidate.evidence_fields if field in target.green_conditions),
            stage3_evidence=(),
            stage4c_evidence=candidate.red_flag_fields if candidate.case_type == "4c_thesis_break" else (),
            must_have_fields=target.green_conditions,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason="; ".join(candidate.red_flag_fields) if candidate.case_type not in {"success_candidate", "structural_success"} else None,
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


def round31_score_profile_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for target in ROUND31_SCORE_TARGETS:
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


def round31_case_candidate_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND31_CASE_CANDIDATES:
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


def round31_summary() -> dict[str, int | bool]:
    records = round31_case_records()
    positive = sum(1 for record in records if record.case_type in {"success_candidate", "structural_success", "cyclical_success"})
    stage4c = sum(1 for record in records if record.case_type == "4c_thesis_break")
    stage4b = sum(1 for record in records if record.case_type == "4b_watch")
    return {
        "target_count": len(ROUND31_SCORE_TARGETS),
        "case_candidate_count": len(records),
        "success_candidate_count": positive,
        "counterexample_or_risk_count": len(records) - positive,
        "stage4b_case_count": stage4b,
        "stage4c_case_count": stage4c,
        "green_possible_count": sum(1 for target in ROUND31_SCORE_TARGETS if target.posture == Round10ThemePosture.GREEN_POSSIBLE),
        "watch_yellow_first_count": sum(1 for target in ROUND31_SCORE_TARGETS if target.posture == Round10ThemePosture.WATCH_YELLOW_FIRST),
        "redteam_first_count": sum(1 for target in ROUND31_SCORE_TARGETS if target.posture == Round10ThemePosture.REDTEAM_FIRST),
        "production_scoring_changed": False,
        "case_records_are_candidate_generation_input": False,
    }


def write_round31_score_weight_reports(
    *,
    output_directory: str | Path = ROUND31_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND31_DEFAULT_CASES_PATH,
    score_profile_path: str | Path = ROUND31_DEFAULT_SCORE_PROFILE_PATH,
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
        "summary": output / "round31_score_weight_v16_summary.md",
        "case_matrix": output / "round31_case_candidate_matrix.csv",
        "green_guardrails": output / "round31_green_guardrail_review.md",
        "regulated_risk": output / "round31_regulated_risk_review.md",
        "ai_infra_split": output / "round31_ai_infra_split_review.md",
        "price_validation_plan": output / "round31_price_validation_plan.md",
    }
    _write_case_jsonl(round31_case_records(), cases)
    _write_rows(round31_score_profile_rows(), score_profiles)
    _write_rows(round31_case_candidate_rows(), paths["case_matrix"])
    paths["summary"].write_text(render_round31_summary_markdown(), encoding="utf-8")
    paths["green_guardrails"].write_text(render_round31_green_guardrail_markdown(), encoding="utf-8")
    paths["regulated_risk"].write_text(render_round31_regulated_risk_markdown(), encoding="utf-8")
    paths["ai_infra_split"].write_text(render_round31_ai_infra_split_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round31_price_validation_plan_markdown(), encoding="utf-8")
    return paths


def render_round31_summary_markdown() -> str:
    summary = round31_summary()
    lines = [
        "# Round-31 Score-Weight v1.6 Summary",
        "",
        f"- source_round: `{ROUND31_SOURCE_ROUND_PATH}`",
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
        "- Round 31 adds v1.6 calibration cases and target weights only.",
        "- Example: data-center REITs need tenant, occupancy, FFO/AFFO, power/cooling/land, and funding-cost evidence.",
        "- Example: waste treatment can be Green-possible when permits, facilities, utilization, contracts, and recurring FCF are source-backed.",
        "- Example: regulated consumer, apparel, and digital-asset themes stay Watch unless approval, revenue, inventory, legal, and FCF risks are controlled.",
        "- Theme names, case IDs, policy approvals, store/channel labels, and price rallies are not score evidence by themselves.",
    ]
    return "\n".join(lines) + "\n"


def render_round31_green_guardrail_markdown() -> str:
    lines = [
        "# Round-31 Green Guardrail Review",
        "",
        "| target | posture | Green unlock evidence | Red flags |",
        "|---|---|---|---|",
    ]
    for target in ROUND31_SCORE_TARGETS:
        lines.append(
            "| "
            f"{target.target_id} | {target.posture.value} | "
            f"{', '.join(target.green_conditions)} | {', '.join(target.red_flags)} |"
        )
    lines.extend(
        [
            "",
            "## What Not To Change",
            "- Do not apply v1.6 weights to production scoring yet.",
            "- Do not use case IDs or theme labels as candidate-generation input.",
            "- Do not invent stage dates, prices, FFO/AFFO, tenant terms, utilization, VBP impact, approval status, markdown rate, or transaction volume.",
            "- Do not lower Stage 3-Green thresholds to improve recall.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round31_regulated_risk_markdown() -> str:
    return "\n".join(
        [
            "# Round-31 Regulated / Legal Risk Review",
            "",
            "Round 31 makes regulation and legal exposure explicit for products where one approval or one ban can flip the stage.",
            "",
            "## Examples",
            "- Dental implants: VBP or other price-control policy can cap ASP and margin.",
            "- E-cigarettes and cannabis: approval can create Stage 2, but bans or public-health litigation can become 4C.",
            "- Apparel/fast fashion: IP litigation, markdown, inventory, and ultra-low-price competition can erase growth quality.",
            "- Digital assets: stablecoin/STO infrastructure must be separated from NFT or crypto theme exposure.",
            "",
            "## Guardrail",
            "- Regulatory approval can support evidence, but it cannot replace revenue, FCF, and risk controls.",
        ]
    ) + "\n"


def render_round31_ai_infra_split_markdown() -> str:
    return "\n".join(
        [
            "# Round-31 AI Infrastructure Split Review",
            "",
            "AI data-center infrastructure is not one score bucket. It must be split into evidence axes.",
            "",
            "## Green-Possible Axes",
            "- Power equipment, transformers, and cables with orders or leases.",
            "- Cooling, HVAC, or liquid cooling with project and revenue exposure.",
            "- Data-center REIT with hyperscale lease, occupancy, FFO/AFFO, and funding-cost control.",
            "- Long-term power PPA with tariff/economics visible.",
            "- AI server PCB when delivery and OP/EPS revisions are source-backed.",
            "",
            "## Watch / Red Axes",
            "- Smart-grid PoC without paying customer.",
            "- Generic HVAC or IDC theme without tenant economics.",
            "- AI CAPEX label without revenue exposure.",
            "- Project delay, overbuild, or power/water constraint.",
        ]
    ) + "\n"


def render_round31_price_validation_plan_markdown() -> str:
    return "\n".join(
        [
            "# Round-31 Price Validation Plan",
            "",
            "1. Backfill tradable case price paths where symbols exist.",
            "2. Keep synthetic, theme, and reference counterexamples as `needs_price_backfill` or `missing_price_data`.",
            "3. Calculate MFE/MAE, peak, drawdown, and below-entry flags only from source data.",
            "4. Run shadow score-price alignment before any production scoring change.",
            "",
            "## Priority Validation",
            "- Data-center REIT: lease/occupancy/FFO/AFFO versus power/water and funding-cost 4C.",
            "- Waste: permits/utilization/recurring FCF versus low utilization and CAPEX pressure.",
            "- Medical device: export/consumables/OPM versus VBP, approval delay, and ASP pressure.",
            "- Regulated consumer and apparel: approval/channel/brand growth versus bans, IP litigation, markdown, and inventory.",
            "- AI infrastructure/value-up: split evidence axes and prove execution before Green-like interpretation.",
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
    "ROUND31_CASE_CANDIDATES",
    "ROUND31_DEFAULT_CASES_PATH",
    "ROUND31_DEFAULT_OUTPUT_DIRECTORY",
    "ROUND31_DEFAULT_SCORE_PROFILE_PATH",
    "ROUND31_SCORE_TARGETS",
    "ROUND31_SOURCE_ROUND_PATH",
    "Round31CaseCandidate",
    "Round31ScoreTarget",
    "Round31ScoreWeightDraft",
    "render_round31_ai_infra_split_markdown",
    "render_round31_green_guardrail_markdown",
    "render_round31_price_validation_plan_markdown",
    "render_round31_regulated_risk_markdown",
    "render_round31_summary_markdown",
    "round31_case_candidate_rows",
    "round31_case_records",
    "round31_score_profile_rows",
    "round31_summary",
    "target_for",
    "write_round31_score_weight_reports",
]
