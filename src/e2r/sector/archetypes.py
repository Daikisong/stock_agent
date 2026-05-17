"""E2R archetype definitions.

Archetypes describe business-model patterns, not individual stocks. They are
used for taxonomy, case-library coverage, and later score-weight design.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Mapping


class E2RArchetype(str, Enum):
    """Canonical E2R sector/business archetypes."""

    CONTRACT_BACKLOG_INDUSTRIAL = "CONTRACT_BACKLOG_INDUSTRIAL"
    GRID_TRANSFORMER_SHORTAGE = "GRID_TRANSFORMER_SHORTAGE"
    GRID_MEDIUM_VOLTAGE_EXPANSION = "GRID_MEDIUM_VOLTAGE_EXPANSION"
    AI_DATA_CENTER_POWER_EQUIPMENT = "AI_DATA_CENTER_POWER_EQUIPMENT"
    DEFENSE_GOVERNMENT_BACKLOG = "DEFENSE_GOVERNMENT_BACKLOG"
    DEFENSE_LOCAL_PRODUCTION_PLATFORM = "DEFENSE_LOCAL_PRODUCTION_PLATFORM"
    DEFENSE_CAPITAL_ALLOCATION_SHOCK = "DEFENSE_CAPITAL_ALLOCATION_SHOCK"
    DEFENSE_UNMANNED_NAVAL_SYSTEMS = "DEFENSE_UNMANNED_NAVAL_SYSTEMS"
    DEFENSE_TECH_AUTONOMOUS_SYSTEMS = "DEFENSE_TECH_AUTONOMOUS_SYSTEMS"
    DEFENSE_DRONE_COUNTER_UAS = "DEFENSE_DRONE_COUNTER_UAS"
    DEFENSE_AI_SOFTWARE_INTELLIGENCE = "DEFENSE_AI_SOFTWARE_INTELLIGENCE"
    SHIPBUILDING_OFFSHORE_BACKLOG = "SHIPBUILDING_OFFSHORE_BACKLOG"
    SHIPBUILDING_NAVAL_MRO = "SHIPBUILDING_NAVAL_MRO"
    RAIL_INFRASTRUCTURE = "RAIL_INFRASTRUCTURE"
    NUCLEAR_EXISTING_PPA = "NUCLEAR_EXISTING_PPA"
    NUCLEAR_EXISTING_PPA_RESTART = "NUCLEAR_EXISTING_PPA_RESTART"
    PROJECT_DELAY_CAPEX_OVERLAY = "PROJECT_DELAY_CAPEX_OVERLAY"
    DATA_CENTER_GRID_PERMITTING_OVERLAY = "DATA_CENTER_GRID_PERMITTING_OVERLAY"
    CAPITAL_ALLOCATION_DILUTION_OVERLAY = "CAPITAL_ALLOCATION_DILUTION_OVERLAY"
    SMART_FACTORY_AUTOMATION = "SMART_FACTORY_AUTOMATION"
    EXPORT_RECURRING_CONSUMER = "EXPORT_RECURRING_CONSUMER"
    K_BEAUTY_EXPORT_DISTRIBUTION = "K_BEAUTY_EXPORT_DISTRIBUTION"
    MEMORY_HBM_CAPACITY = "MEMORY_HBM_CAPACITY"
    HBM_CATCHUP_EXECUTION = "HBM_CATCHUP_EXECUTION"
    AI_STORAGE_NAND_SHORTAGE = "AI_STORAGE_NAND_SHORTAGE"
    COMMODITY_MEMORY_GENERAL_SEMI = "COMMODITY_MEMORY_GENERAL_SEMI"
    SEMI_EQUIPMENT_CAPEX = "SEMI_EQUIPMENT_CAPEX"
    SEMI_EQUIPMENT_AI_CAPEX = "SEMI_EQUIPMENT_AI_CAPEX"
    SEMI_MATERIALS_PROCESS = "SEMI_MATERIALS_PROCESS"
    ADVANCED_PACKAGING_PCB = "ADVANCED_PACKAGING_PCB"
    ADVANCED_PACKAGING_COWOS_EMIB = "ADVANCED_PACKAGING_COWOS_EMIB"
    DISPLAY_OLED_SUPPLYCHAIN = "DISPLAY_OLED_SUPPLYCHAIN"
    ELECTRONIC_COMPONENTS_MLCC_SENSOR = "ELECTRONIC_COMPONENTS_MLCC_SENSOR"
    AI_CHIP_FABRIC_INFRA = "AI_CHIP_FABRIC_INFRA"
    AI_ACCELERATOR_CHIP_PUREPLAY = "AI_ACCELERATOR_CHIP_PUREPLAY"
    AI_SERVER_ODM_EMS_SUPPLY_CHAIN = "AI_SERVER_ODM_EMS_SUPPLY_CHAIN"
    NEOCLOUD_GPU_RENTAL = "NEOCLOUD_GPU_RENTAL"
    OPTICAL_NETWORKING_AI_DATACENTER = "OPTICAL_NETWORKING_AI_DATACENTER"
    INDUSTRIAL_GASES_SEMICONDUCTOR_INFRA = "INDUSTRIAL_GASES_SEMICONDUCTOR_INFRA"
    AI_DATA_CENTER_COOLING = "AI_DATA_CENTER_COOLING"
    AI_GRID_FLEXIBILITY_SOFTWARE = "AI_GRID_FLEXIBILITY_SOFTWARE"
    BATTERY_MATERIALS_CAPEX_OVERHEAT = "BATTERY_MATERIALS_CAPEX_OVERHEAT"
    BATTERY_EQUIPMENT_PARTS = "BATTERY_EQUIPMENT_PARTS"
    BATTERY_RECYCLING_ESS_SHIFT = "BATTERY_RECYCLING_ESS_SHIFT"
    ESS_LFP_GRID_STORAGE = "ESS_LFP_GRID_STORAGE"
    ESS_AI_DATA_CENTER_STORAGE = "ESS_AI_DATA_CENTER_STORAGE"
    EV_TO_ESS_CAPACITY_REDEPLOYMENT = "EV_TO_ESS_CAPACITY_REDEPLOYMENT"
    BATTERY_CONTRACT_DISCLOSURE_CONFIDENCE = "BATTERY_CONTRACT_DISCLOSURE_CONFIDENCE"
    EV_INFRASTRUCTURE = "EV_INFRASTRUCTURE"
    HYDROGEN_FUEL_CELL_INFRA = "HYDROGEN_FUEL_CELL_INFRA"
    SOLAR_TARIFF_SUPPLYCHAIN = "SOLAR_TARIFF_SUPPLYCHAIN"
    RENEWABLE_ENERGY_POLICY = "RENEWABLE_ENERGY_POLICY"
    RENEWABLE_ENERGY_PROJECT_ECONOMICS = "RENEWABLE_ENERGY_PROJECT_ECONOMICS"
    ENERGY_DISTRIBUTION_FUEL = "ENERGY_DISTRIBUTION_FUEL"
    WASTE_RECYCLING_ENVIRONMENT = "WASTE_RECYCLING_ENVIRONMENT"
    CARBON_CREDIT_CBAM_COMPLIANCE = "CARBON_CREDIT_CBAM_COMPLIANCE"
    DATA_CENTER_WATER_REUSE_INFRA = "DATA_CENTER_WATER_REUSE_INFRA"
    EV_FIRE_RISK_OVERLAY = "EV_FIRE_RISK_OVERLAY"
    EV_FIRE_BESS_SAFETY_OVERLAY = "EV_FIRE_BESS_SAFETY_OVERLAY"
    BATTERY_HEALTH_TRANSPARENCY_OVERLAY = "BATTERY_HEALTH_TRANSPARENCY_OVERLAY"
    BATTERY_SOH_SECOND_LIFE_TRANSPARENCY = "BATTERY_SOH_SECOND_LIFE_TRANSPARENCY"
    LITHIUM_CYCLE_OVERLAY = "LITHIUM_CYCLE_OVERLAY"
    LITHIUM_ESS_DEMAND_CYCLE = "LITHIUM_ESS_DEMAND_CYCLE"
    SPECULATIVE_BATTERY_TECH = "SPECULATIVE_BATTERY_TECH"
    COMMODITY_SPREAD = "COMMODITY_SPREAD"
    REFINING_OIL_SPREAD = "REFINING_OIL_SPREAD"
    LUBRICANTS_HIGH_MARGIN_MIX = "LUBRICANTS_HIGH_MARGIN_MIX"
    CHEMICAL_SPREAD = "CHEMICAL_SPREAD"
    STEEL_METAL_SPREAD = "STEEL_METAL_SPREAD"
    NONFERROUS_STRATEGIC_METALS = "NONFERROUS_STRATEGIC_METALS"
    COPPER_AI_GRID_STRUCTURAL_DEMAND = "COPPER_AI_GRID_STRUCTURAL_DEMAND"
    LITHIUM_BATTERY_RAW_MATERIAL = "LITHIUM_BATTERY_RAW_MATERIAL"
    PRECIOUS_METALS_SAFE_HAVEN_MINERS = "PRECIOUS_METALS_SAFE_HAVEN_MINERS"
    PAPER_PACKAGING_CYCLE = "PAPER_PACKAGING_CYCLE"
    AGRI_COMMODITY_INPUTS = "AGRI_COMMODITY_INPUTS"
    LNG_ENERGY_TRADING_DISTRIBUTION = "LNG_ENERGY_TRADING_DISTRIBUTION"
    GENERAL_TRADING_RESOURCE_INFRA = "GENERAL_TRADING_RESOURCE_INFRA"
    ENERGY_UTILITY_LNG_GAS = "ENERGY_UTILITY_LNG_GAS"
    EVENT_PREMIUM_GOVERNANCE_OVERLAY = "EVENT_PREMIUM_GOVERNANCE_OVERLAY"
    COMMODITY_PRICE_4C_OVERLAY = "COMMODITY_PRICE_4C_OVERLAY"
    RARE_METALS_PRICE_FLOOR_OFFTAKE = "RARE_METALS_PRICE_FLOOR_OFFTAKE"
    RARE_METALS_EXPORT_CONTROL_EVENT = "RARE_METALS_EXPORT_CONTROL_EVENT"
    SHIPPING_FREIGHT_CYCLE = "SHIPPING_FREIGHT_CYCLE"
    AUTO_MOBILITY_COMPONENTS = "AUTO_MOBILITY_COMPONENTS"
    AUTO_MOBILITY_COMPLETED_VEHICLE = "AUTO_MOBILITY_COMPLETED_VEHICLE"
    AUTO_HYBRID_VALUEUP = "AUTO_HYBRID_VALUEUP"
    HYBRID_COMPONENT_BOTTLENECK = "HYBRID_COMPONENT_BOTTLENECK"
    TIRE_AUTO_COMPONENT_SPREAD = "TIRE_AUTO_COMPONENT_SPREAD"
    AIRLINE_TRAVEL_CYCLE = "AIRLINE_TRAVEL_CYCLE"
    CASINO_DUTYFREE_TOURISM = "CASINO_DUTYFREE_TOURISM"
    LOGISTICS_PARCEL_FREIGHT = "LOGISTICS_PARCEL_FREIGHT"
    RENTAL_USED_CAR_MOBILITY = "RENTAL_USED_CAR_MOBILITY"
    MOBILITY_RENTAL_MICROMOBILITY = "MOBILITY_RENTAL_MICROMOBILITY"
    AUTO_COMPONENTS_EV_ADAS = "AUTO_COMPONENTS_EV_ADAS"
    AUTONOMOUS_ROBOTAXI_DEPLOYMENT = "AUTONOMOUS_ROBOTAXI_DEPLOYMENT"
    URBAN_AIR_DRONE = "URBAN_AIR_DRONE"
    SPACE_SUPPLYCHAIN = "SPACE_SUPPLYCHAIN"
    SATELLITE_CONNECTIVITY_INFRA = "SATELLITE_CONNECTIVITY_INFRA"
    TRANSPORT_SAFETY_REGULATORY_OVERLAY = "TRANSPORT_SAFETY_REGULATORY_OVERLAY"
    FLEET_UNIT_ECONOMICS_OVERLAY = "FLEET_UNIT_ECONOMICS_OVERLAY"
    ROBOTICS_FACTORY_AUTOMATION = "ROBOTICS_FACTORY_AUTOMATION"
    AI_DATA_CENTER_INFRASTRUCTURE = "AI_DATA_CENTER_INFRASTRUCTURE"
    NUCLEAR_SMR_GRID_POLICY = "NUCLEAR_SMR_GRID_POLICY"
    TRAVEL_LEISURE_REOPENING = "TRAVEL_LEISURE_REOPENING"
    EDUCATION_SPECIALTY_SERVICES = "EDUCATION_SPECIALTY_SERVICES"
    RARE_METALS_STRATEGIC_MATERIALS = "RARE_METALS_STRATEGIC_MATERIALS"
    VALUE_UP_SHAREHOLDER_RETURN = "VALUE_UP_SHAREHOLDER_RETURN"
    PLATFORM_SOFTWARE_INTERNET = "PLATFORM_SOFTWARE_INTERNET"
    B2B_SAAS_ERP_WORKFLOW = "B2B_SAAS_ERP_WORKFLOW"
    CLOUD_AI_SOFTWARE_INFRA = "CLOUD_AI_SOFTWARE_INFRA"
    AI_SOFTWARE_APPLICATION = "AI_SOFTWARE_APPLICATION"
    OBSERVABILITY_AI_OPERATIONS = "OBSERVABILITY_AI_OPERATIONS"
    GENERATIVE_AI_IP_RISK = "GENERATIVE_AI_IP_RISK"
    CONTACT_CENTER_AI_AUTOMATION = "CONTACT_CENTER_AI_AUTOMATION"
    SERVICE_KIOSK_SELF_CHECKOUT = "SERVICE_KIOSK_SELF_CHECKOUT"
    GAME_CONTENT_IP = "GAME_CONTENT_IP"
    UGC_GAME_PLATFORM_SAFETY = "UGC_GAME_PLATFORM_SAFETY"
    MEDIA_AD_CONTENT_CYCLE = "MEDIA_AD_CONTENT_CYCLE"
    ADTECH_PLATFORM_PREMIUM = "ADTECH_PLATFORM_PREMIUM"
    STREAMING_AD_PLATFORM = "STREAMING_AD_PLATFORM"
    SECURITY_IDENTITY_DEEPFAKE = "SECURITY_IDENTITY_DEEPFAKE"
    SECURITY_OPERATIONAL_TRUST_OVERLAY = "SECURITY_OPERATIONAL_TRUST_OVERLAY"
    METAVERSE_NFT_THEME = "METAVERSE_NFT_THEME"
    PLATFORM_GOVERNANCE_LEGAL_RISK = "PLATFORM_GOVERNANCE_LEGAL_RISK"
    PLATFORM_AD_TRUST_OVERLAY = "PLATFORM_AD_TRUST_OVERLAY"
    FINANCIAL_SPREAD_BALANCE_SHEET = "FINANCIAL_SPREAD_BALANCE_SHEET"
    INSURANCE_UNDERWRITING_CYCLE = "INSURANCE_UNDERWRITING_CYCLE"
    SECURITIES_BROKERAGE_CYCLE = "SECURITIES_BROKERAGE_CYCLE"
    TREASURY_SHARE_CANCEL_EXECUTION = "TREASURY_SHARE_CANCEL_EXECUTION"
    PAYMENT_FINTECH_INFRA = "PAYMENT_FINTECH_INFRA"
    FINTECH_SUPERAPP_IPO_OPTION = "FINTECH_SUPERAPP_IPO_OPTION"
    DIGITAL_ASSET_TOKENIZATION = "DIGITAL_ASSET_TOKENIZATION"
    CREDIT_DATA_INFRA = "CREDIT_DATA_INFRA"
    VC_EXIT_MARKET_CYCLE = "VC_EXIT_MARKET_CYCLE"
    EVENT_PREMIUM_GOVERNANCE_BATTLE = "EVENT_PREMIUM_GOVERNANCE_BATTLE"
    REGULATED_STABLECOIN_INFRA = "REGULATED_STABLECOIN_INFRA"
    ALGORITHMIC_STABLECOIN_FAILURE = "ALGORITHMIC_STABLECOIN_FAILURE"
    DIGITAL_ASSET_EXCHANGE_CONSOLIDATION = "DIGITAL_ASSET_EXCHANGE_CONSOLIDATION"
    BANK_DIGITAL_ASSET_EQUITY_STAKE = "BANK_DIGITAL_ASSET_EQUITY_STAKE"
    DIGITAL_ASSET_THEME_OVERHEAT = "DIGITAL_ASSET_THEME_OVERHEAT"
    GOVERNANCE_EXECUTION_FAILURE_OVERLAY = "GOVERNANCE_EXECUTION_FAILURE_OVERLAY"
    TAX_POLICY_MARKET_SHOCK_OVERLAY = "TAX_POLICY_MARKET_SHOCK_OVERLAY"
    STABLECOIN_CONVERTIBILITY_OVERLAY = "STABLECOIN_CONVERTIBILITY_OVERLAY"
    BIOTECH_REGULATORY = "BIOTECH_REGULATORY"
    BIOTECH_PRE_REVENUE_REGULATORY = "BIOTECH_PRE_REVENUE_REGULATORY"
    BIOTECH_ROYALTY_COMMERCIALIZATION = "BIOTECH_ROYALTY_COMMERCIALIZATION"
    CDMO_HEALTHCARE_CONTRACT = "CDMO_HEALTHCARE_CONTRACT"
    CDMO_US_TARIFF_HEDGE_CAPACITY = "CDMO_US_TARIFF_HEDGE_CAPACITY"
    CRO_CLINICAL_SERVICE = "CRO_CLINICAL_SERVICE"
    BIOSIMILAR_COMMERCIALIZATION = "BIOSIMILAR_COMMERCIALIZATION"
    BIOSIMILAR_ORIGINATOR_DEFENSE = "BIOSIMILAR_ORIGINATOR_DEFENSE"
    BIOSIMILAR_PATENT_LITIGATION = "BIOSIMILAR_PATENT_LITIGATION"
    OBESITY_GLP1_COMMERCIALIZATION = "OBESITY_GLP1_COMMERCIALIZATION"
    ORAL_GLP1_MAINTENANCE_THERAPY = "ORAL_GLP1_MAINTENANCE_THERAPY"
    GLP1_TELEHEALTH_CHANNEL = "GLP1_TELEHEALTH_CHANNEL"
    COMPOUNDED_GLP1_REGULATORY_RISK = "COMPOUNDED_GLP1_REGULATORY_RISK"
    GENE_THERAPY_RARE_DISEASE = "GENE_THERAPY_RARE_DISEASE"
    AI_DRUG_DISCOVERY_PLATFORM = "AI_DRUG_DISCOVERY_PLATFORM"
    DIGITAL_HEALTHCARE_AI = "DIGITAL_HEALTHCARE_AI"
    MEDICAL_AI_EXTERNAL_VALIDATION = "MEDICAL_AI_EXTERNAL_VALIDATION"
    DIGITAL_HEALTHCARE_REMOTE_MEDICINE = "DIGITAL_HEALTHCARE_REMOTE_MEDICINE"
    TELEHEALTH_BEHAVIORAL_HEALTH = "TELEHEALTH_BEHAVIORAL_HEALTH"
    PHARMA_CHANNEL_AND_PRIVACY_RISK = "PHARMA_CHANNEL_AND_PRIVACY_RISK"
    MEDICAL_DEVICE_HEALTHCARE_EXPORT = "MEDICAL_DEVICE_HEALTHCARE_EXPORT"
    MEDICAL_DEVICE_DENTAL_IMPLANT = "MEDICAL_DEVICE_DENTAL_IMPLANT"
    SURGICAL_ROBOT_INSTALLED_BASE = "SURGICAL_ROBOT_INSTALLED_BASE"
    BOTULINUM_AESTHETIC_REGULATED = "BOTULINUM_AESTHETIC_REGULATED"
    DIAGNOSTICS_INFECTIOUS_DISEASE = "DIAGNOSTICS_INFECTIOUS_DISEASE"
    COMMERCIALIZATION_FAILURE_OVERLAY = "COMMERCIALIZATION_FAILURE_OVERLAY"
    REIMBURSEMENT_ACCESS_OVERLAY = "REIMBURSEMENT_ACCESS_OVERLAY"
    DEVICE_SAFETY_COUNTERFEIT_OVERLAY = "DEVICE_SAFETY_COUNTERFEIT_OVERLAY"
    ANIMAL_HEALTH_BIOSECURITY = "ANIMAL_HEALTH_BIOSECURITY"
    RETAIL_DOMESTIC_CONSUMER = "RETAIL_DOMESTIC_CONSUMER"
    FOOD_AGRI_LIVESTOCK_CYCLE = "FOOD_AGRI_LIVESTOCK_CYCLE"
    RETAIL_CONVENIENCE_OFFLINE = "RETAIL_CONVENIENCE_OFFLINE"
    RETAIL_ECOMMERCE_LOGISTICS = "RETAIL_ECOMMERCE_LOGISTICS"
    ECOMMERCE_FRESH_LOGISTICS = "ECOMMERCE_FRESH_LOGISTICS"
    BEAUTY_OEM_ODM_SUPPLYCHAIN = "BEAUTY_OEM_ODM_SUPPLYCHAIN"
    APPAREL_FAST_FASHION_BRAND_OEM = "APPAREL_FAST_FASHION_BRAND_OEM"
    HOME_LIVING_APPLIANCE_RENTAL = "HOME_LIVING_APPLIANCE_RENTAL"
    K_FOOD_GLOBAL_PORTFOLIO_EXPANSION = "K_FOOD_GLOBAL_PORTFOLIO_EXPANSION"
    K_BEAUTY_OFFLINE_SELL_THROUGH = "K_BEAUTY_OFFLINE_SELL_THROUGH"
    BEAUTY_DEVICE_AFFILIATE_COMMERCE = "BEAUTY_DEVICE_AFFILIATE_COMMERCE"
    ULTRA_LOW_COST_CROSSBORDER_PLATFORM = "ULTRA_LOW_COST_CROSSBORDER_PLATFORM"
    HOME_APPLIANCE_HARDWARE_CYCLE = "HOME_APPLIANCE_HARDWARE_CYCLE"
    DISCOUNT_PROMOTION_MARGIN_OVERLAY = "DISCOUNT_PROMOTION_MARGIN_OVERLAY"
    HOME_CHILD_EDUCATION = "HOME_CHILD_EDUCATION"
    CONSUMER_REGULATED_PRODUCT = "CONSUMER_REGULATED_PRODUCT"
    BEAUTY_DEVICE_EXPORT = "BEAUTY_DEVICE_EXPORT"
    FOOD_SAFETY_RECALL_OVERLAY = "FOOD_SAFETY_RECALL_OVERLAY"
    DATA_SECURITY_SUPPLIER_REGULATION_OVERLAY = "DATA_SECURITY_SUPPLIER_REGULATION_OVERLAY"
    SMART_FARM_AGRI_TECH = "SMART_FARM_AGRI_TECH"
    VERTICAL_FARMING_UNIT_ECONOMICS = "VERTICAL_FARMING_UNIT_ECONOMICS"
    AGRI_MACHINERY_PRECISION_CYCLE = "AGRI_MACHINERY_PRECISION_CYCLE"
    AGRI_MACHINERY_SOFTWARE_LOCKIN = "AGRI_MACHINERY_SOFTWARE_LOCKIN"
    AGRI_LIVESTOCK_FOOD_COMMODITY = "AGRI_LIVESTOCK_FOOD_COMMODITY"
    FOOD_INPUT_REGULATED_CYCLE = "FOOD_INPUT_REGULATED_CYCLE"
    EDTECH_AI_DISRUPTION = "EDTECH_AI_DISRUPTION"
    ONLINE_EDUCATION_OPM_DISTRESS = "ONLINE_EDUCATION_OPM_DISTRESS"
    NICOTINE_ALTERNATIVE_REGULATED = "NICOTINE_ALTERNATIVE_REGULATED"
    CANNABIS_REGULATED_PRODUCT = "CANNABIS_REGULATED_PRODUCT"
    POLICY_LOCAL_SERVICE_THEME = "POLICY_LOCAL_SERVICE_THEME"
    AGRI_DISEASE_EVENT_OVERLAY = "AGRI_DISEASE_EVENT_OVERLAY"
    AI_EDUCATION_DISRUPTION_OVERLAY = "AI_EDUCATION_DISRUPTION_OVERLAY"
    REGULATED_CONSUMER_APPROVAL_OVERLAY = "REGULATED_CONSUMER_APPROVAL_OVERLAY"
    CONSTRUCTION_REAL_ESTATE_CREDIT = "CONSTRUCTION_REAL_ESTATE_CREDIT"
    PF_RESTRUCTURING_RELIEF = "PF_RESTRUCTURING_RELIEF"
    REIT_DEVELOPMENT_TRUST = "REIT_DEVELOPMENT_TRUST"
    BUILDING_MATERIALS_CYCLE = "BUILDING_MATERIALS_CYCLE"
    BUILDING_MATERIALS_PRICE_COST = "BUILDING_MATERIALS_PRICE_COST"
    BUILDING_MATERIALS_VOLUME_FAILURE = "BUILDING_MATERIALS_VOLUME_FAILURE"
    DATA_CENTER_REIT_INFRASTRUCTURE = "DATA_CENTER_REIT_INFRASTRUCTURE"
    DATA_CENTER_POWER_WATER_PERMITTING = "DATA_CENTER_POWER_WATER_PERMITTING"
    COLD_CHAIN_REIT_LOGISTICS = "COLD_CHAIN_REIT_LOGISTICS"
    INFRA_RECONSTRUCTION_POLICY = "INFRA_RECONSTRUCTION_POLICY"
    POLICY_LOCAL_REAL_ESTATE_THEME = "POLICY_LOCAL_REAL_ESTATE_THEME"
    PF_CREDIT_REDTEAM_OVERLAY = "PF_CREDIT_REDTEAM_OVERLAY"
    REIT_AFFO_INTEGRITY_OVERLAY = "REIT_AFFO_INTEGRITY_OVERLAY"
    AI_INFRA_REAL_ASSET_THEME_OVERLAY = "AI_INFRA_REAL_ASSET_THEME_OVERLAY"
    DISASTER_REBUILD_EVENT = "DISASTER_REBUILD_EVENT"
    NORTH_KOREA_POLICY_EVENT = "NORTH_KOREA_POLICY_EVENT"
    GEOPOLITICAL_RECONSTRUCTION = "GEOPOLITICAL_RECONSTRUCTION"
    CLIMATE_DISASTER_EVENT = "CLIMATE_DISASTER_EVENT"
    EVENT_DISEASE_PEST_DEMAND = "EVENT_DISEASE_PEST_DEMAND"
    DIAGNOSTICS_INFECTIOUS_EVENT = "DIAGNOSTICS_INFECTIOUS_EVENT"
    SPECULATIVE_SCIENCE_THEME = "SPECULATIVE_SCIENCE_THEME"
    ADVANCED_MATERIAL_SPECULATIVE_THEME = "ADVANCED_MATERIAL_SPECULATIVE_THEME"
    POLICY_LOCAL_THEME = "POLICY_LOCAL_THEME"
    POLICY_MARKET_SHOCK_EVENT = "POLICY_MARKET_SHOCK_EVENT"
    COMMERCIAL_REAL_ESTATE_CREDIT = "COMMERCIAL_REAL_ESTATE_CREDIT"
    RESIDENTIAL_HOUSING_CYCLE = "RESIDENTIAL_HOUSING_CYCLE"
    AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT = "AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT"
    UTILITIES_REGULATED_TARIFF = "UTILITIES_REGULATED_TARIFF"
    HOLDING_RESTRUCTURING_GOVERNANCE = "HOLDING_RESTRUCTURING_GOVERNANCE"
    TURNAROUND_COST_RESTRUCTURING = "TURNAROUND_COST_RESTRUCTURING"
    ONE_OFF_EVENT_DEMAND = "ONE_OFF_EVENT_DEMAND"
    THEME_VALUATION_OVERHEAT = "THEME_VALUATION_OVERHEAT"
    K_FOOD_SINGLE_HERO_PRODUCT = "K_FOOD_SINGLE_HERO_PRODUCT"
    REDTEAM_ACCOUNTING_TRUST_OVERLAY = "REDTEAM_ACCOUNTING_TRUST_OVERLAY"
    AI_CAPEX_CROWDING_OVERLAY = "AI_CAPEX_CROWDING_OVERLAY"
    FINANCIAL_REPORTING_INTEGRITY_RISK = "FINANCIAL_REPORTING_INTEGRITY_RISK"
    CHANNEL_STUFFING_INVENTORY_OVERLAY = "CHANNEL_STUFFING_INVENTORY_OVERLAY"
    TARIFF_IMPORT_REGULATION_OVERLAY = "TARIFF_IMPORT_REGULATION_OVERLAY"
    PRICE_ONLY_RALLY = "PRICE_ONLY_RALLY"
    EVENT_PREMIUM = "EVENT_PREMIUM"
    EVENT_TO_CONTRACT_ESCALATION = "EVENT_TO_CONTRACT_ESCALATION"
    CYCLICAL_SUCCESS = "CYCLICAL_SUCCESS"
    STRUCTURAL_SUCCESS_ALIGNED = "STRUCTURAL_SUCCESS_ALIGNED"
    SECTOR_SUCCESS_BUT_4B_WATCH = "SECTOR_SUCCESS_BUT_4B_WATCH"
    EVIDENCE_GOOD_BUT_PRICE_FAILED = "EVIDENCE_GOOD_BUT_PRICE_FAILED"
    FALSE_POSITIVE_SCORE = "FALSE_POSITIVE_SCORE"
    CROWDED_RERATING_4B_WATCH = "CROWDED_RERATING_4B_WATCH"
    THESIS_BREAK_4C = "THESIS_BREAK_4C"
    LEGAL_REGULATORY_REDTEAM = "LEGAL_REGULATORY_REDTEAM"
    OPERATIONAL_TRUST_BREAK = "OPERATIONAL_TRUST_BREAK"
    LEVERAGE_FCF_BREAKDOWN = "LEVERAGE_FCF_BREAKDOWN"
    COMMERCIALIZATION_FAILURE = "COMMERCIALIZATION_FAILURE"
    AFFO_CASHFLOW_INTEGRITY_RISK = "AFFO_CASHFLOW_INTEGRITY_RISK"
    STABLECOIN_CONVERTIBILITY_RISK = "STABLECOIN_CONVERTIBILITY_RISK"
    UNKNOWN_INSUFFICIENT_EVIDENCE = "UNKNOWN_INSUFFICIENT_EVIDENCE"
    GENERIC_UNCLASSIFIED = "GENERIC_UNCLASSIFIED"


@dataclass(frozen=True)
class ArchetypeDefinition:
    """Lifecycle signals and future score-weight guidance for one archetype."""

    archetype: E2RArchetype
    stage1_radar_signals: tuple[str, ...]
    stage2_candidate_signals: tuple[str, ...]
    stage3_high_conviction_signals: tuple[str, ...]
    stage4a_ongoing_signals: tuple[str, ...]
    stage4b_graduation_overheat_signals: tuple[str, ...]
    stage4c_thesis_break_signals: tuple[str, ...]
    key_evidence_families: tuple[str, ...]
    false_positive_patterns: tuple[str, ...]
    preferred_score_weights: Mapping[str, float]


def _weights(
    *,
    eps_fcf: float,
    visibility: float,
    bottleneck: float,
    mispricing: float,
    valuation: float,
    confidence: float = 5.0,
) -> Mapping[str, float]:
    return {
        "eps_fcf_explosion": eps_fcf,
        "earnings_visibility": visibility,
        "bottleneck_pricing": bottleneck,
        "market_mispricing": mispricing,
        "valuation_rerating": valuation,
        "information_confidence": confidence,
    }


def _generic_definition(archetype: E2RArchetype) -> ArchetypeDefinition:
    return ArchetypeDefinition(
        archetype=archetype,
        stage1_radar_signals=("price/trading value breakout", "sector keyword appears", "company event disclosure"),
        stage2_candidate_signals=("reported OP/EPS acceleration", "research report confirmation", "valuation frame change"),
        stage3_high_conviction_signals=("multi-source evidence", "EPS/FCF bodyweight change", "old-frame mispricing"),
        stage4a_ongoing_signals=("evidence remains intact", "revision path remains positive"),
        stage4b_graduation_overheat_signals=("large rerating return", "crowded positive reports", "revision slowdown"),
        stage4c_thesis_break_signals=("estimate cuts", "margin reversal", "hard disclosure risk"),
        key_evidence_families=("price", "financial_actual", "research_report", "news"),
        false_positive_patterns=("single-source story", "theme-only runup", "no revision support"),
        preferred_score_weights=_weights(eps_fcf=20, visibility=20, bottleneck=15, mispricing=15, valuation=15),
    )


ARCHETYPE_DEFINITIONS: dict[E2RArchetype, ArchetypeDefinition] = {
    archetype: _generic_definition(archetype) for archetype in E2RArchetype
}

ARCHETYPE_DEFINITIONS.update(
    {
        E2RArchetype.CONTRACT_BACKLOG_INDUSTRIAL: ArchetypeDefinition(
            archetype=E2RArchetype.CONTRACT_BACKLOG_INDUSTRIAL,
            stage1_radar_signals=("supply contract disclosure", "backlog keyword", "price/trading value breakout"),
            stage2_candidate_signals=("contract_amount_to_prior_sales", "contract_duration_months", "backlog_to_sales", "OP/EPS revision"),
            stage3_high_conviction_signals=("multi-year order visibility", "capacity constraint", "ASP/pricing power", "EPS/FCF bodyweight change"),
            stage4a_ongoing_signals=("backlog remains high", "delivery/margin path intact", "revision path remains positive"),
            stage4b_graduation_overheat_signals=("multiple expansion", "revision slowdown", "universally bullish reports"),
            stage4c_thesis_break_signals=("contract cancellation", "backlog decline", "margin/ASP drop"),
            key_evidence_families=("disclosure", "research_report", "consensus_revision", "price"),
            false_positive_patterns=("small one-time contract", "low margin backlog", "valuation already saturated"),
            preferred_score_weights=_weights(eps_fcf=20, visibility=24, bottleneck=22, mispricing=13, valuation=12),
        ),
        E2RArchetype.DEFENSE_GOVERNMENT_BACKLOG: ArchetypeDefinition(
            archetype=E2RArchetype.DEFENSE_GOVERNMENT_BACKLOG,
            stage1_radar_signals=("export defense contract", "government customer disclosure", "backlog keyword"),
            stage2_candidate_signals=("multi-year delivery schedule", "order backlog", "margin recovery", "target/EPS revision"),
            stage3_high_conviction_signals=("government-backed backlog", "export mix improvement", "delivery visibility", "EPS bodyweight change"),
            stage4a_ongoing_signals=("delivery schedule on track", "new orders continue", "margin path intact"),
            stage4b_graduation_overheat_signals=("crowded defense reports", "price outruns revision", "delivery risk ignored"),
            stage4c_thesis_break_signals=("delivery delay", "contract change", "cost overrun", "export approval issue"),
            key_evidence_families=("disclosure", "research_report", "financial_actual", "news"),
            false_positive_patterns=("headline contract without margin", "political delay", "single export customer risk"),
            preferred_score_weights=_weights(eps_fcf=20, visibility=24, bottleneck=17, mispricing=14, valuation=12),
        ),
        E2RArchetype.EXPORT_RECURRING_CONSUMER: ArchetypeDefinition(
            archetype=E2RArchetype.EXPORT_RECURRING_CONSUMER,
            stage1_radar_signals=("export growth", "OPM surprise", "channel expansion"),
            stage2_candidate_signals=("FY1/FY2 EPS/OP revision", "export mix increase", "repeated overseas demand"),
            stage3_high_conviction_signals=("recurring demand", "channel expansion", "OPM leverage", "valuation below new frame"),
            stage4a_ongoing_signals=("sell-through remains strong", "new channels add revenue", "margin remains high"),
            stage4b_graduation_overheat_signals=("peak margin", "crowded reports", "decelerating sell-through"),
            stage4c_thesis_break_signals=("export slowdown", "channel inventory issue", "ASP/margin reversal"),
            key_evidence_families=("research_report", "financial_actual", "consensus_revision", "news"),
            false_positive_patterns=("short-lived product fad", "inventory stuffing", "FX-only margin lift"),
            preferred_score_weights=_weights(eps_fcf=22, visibility=23, bottleneck=14, mispricing=16, valuation=14),
        ),
        E2RArchetype.K_BEAUTY_EXPORT_DISTRIBUTION: ArchetypeDefinition(
            archetype=E2RArchetype.K_BEAUTY_EXPORT_DISTRIBUTION,
            stage1_radar_signals=("export growth", "platform/distribution expansion", "OPM/ROE improvement"),
            stage2_candidate_signals=("brand/customer diversification", "FY1/FY2 OP/EPS revision", "repeat orders"),
            stage3_high_conviction_signals=("recurring export channel", "platform scale", "margin leverage", "new valuation frame"),
            stage4a_ongoing_signals=("channel expansion continues", "brand breadth improves", "cash conversion remains healthy"),
            stage4b_graduation_overheat_signals=("single-platform crowding", "margin peak", "inventory risk ignored"),
            stage4c_thesis_break_signals=("export channel slowdown", "inventory spike", "platform fee/margin reversal"),
            key_evidence_families=("research_report", "financial_actual", "news", "consensus_revision"),
            false_positive_patterns=("single brand fad", "channel stuffing", "low-quality receivables growth"),
            preferred_score_weights=_weights(eps_fcf=22, visibility=23, bottleneck=13, mispricing=16, valuation=14),
        ),
        E2RArchetype.MEMORY_HBM_CAPACITY: ArchetypeDefinition(
            archetype=E2RArchetype.MEMORY_HBM_CAPACITY,
            stage1_radar_signals=("HBM demand", "memory price increase", "earnings turnaround"),
            stage2_candidate_signals=("consensus revision", "DRAM/NAND/HBM pricing", "supply discipline"),
            stage3_high_conviction_signals=("multi-year EPS path", "HBM/capacity bottleneck", "old cyclical discount removal"),
            stage4a_ongoing_signals=("prices and revisions remain positive", "capacity allocation holds", "customer demand intact"),
            stage4b_graduation_overheat_signals=("full rerating", "revision slowdown", "capex overbuild signs"),
            stage4c_thesis_break_signals=("customer capex collapse", "supply glut", "memory price decline"),
            key_evidence_families=("financial_actual", "research_report", "consensus_revision", "news"),
            false_positive_patterns=("pure cyclical bounce", "price-only memory rally", "capex overbuild ignored"),
            preferred_score_weights=_weights(eps_fcf=24, visibility=21, bottleneck=19, mispricing=15, valuation=12),
        ),
        E2RArchetype.AUTO_MOBILITY_COMPLETED_VEHICLE: ArchetypeDefinition(
            archetype=E2RArchetype.AUTO_MOBILITY_COMPLETED_VEHICLE,
            stage1_radar_signals=("hybrid mix improvement", "shareholder return", "export mix", "EV slowdown response"),
            stage2_candidate_signals=("OP/FCF stability", "ROE/PBR rerating", "buyback or dividend execution"),
            stage3_high_conviction_signals=("FCF supports recurring return", "high-margin mix persists", "old auto discount removed"),
            stage4a_ongoing_signals=("mix and FCF remain strong", "return policy continues"),
            stage4b_graduation_overheat_signals=("value-up narrative crowded", "peak margin ignored", "tariff risk ignored"),
            stage4c_thesis_break_signals=("tariff hit", "recall cost", "demand slowdown", "peak margin reversal"),
            key_evidence_families=("financial_actual", "research_report", "news", "price"),
            false_positive_patterns=("buyback headline without FCF", "one-quarter sales mix", "policy headline only"),
            preferred_score_weights=_weights(eps_fcf=20, visibility=18, bottleneck=10, mispricing=15, valuation=17),
        ),
        E2RArchetype.AUTO_MOBILITY_COMPONENTS: ArchetypeDefinition(
            archetype=E2RArchetype.AUTO_MOBILITY_COMPONENTS,
            stage1_radar_signals=("auto parts order", "ADAS or EV component", "high-value lighting or electronics"),
            stage2_candidate_signals=("customer diversification", "cost pass-through", "OP/EPS revision", "raw-material stability"),
            stage3_high_conviction_signals=("repeat program visibility", "margin stable", "quality cost low"),
            stage4a_ongoing_signals=("customer mix broadens", "margin and quality costs remain controlled"),
            stage4b_graduation_overheat_signals=("component group rerating crowded", "single customer risk ignored"),
            stage4c_thesis_break_signals=("customer program cut", "quality recall", "raw-material squeeze", "OEM pressure"),
            key_evidence_families=("financial_actual", "research_report", "news", "price"),
            false_positive_patterns=("single OEM order treated as structural", "component theme without margin proof"),
            preferred_score_weights=_weights(eps_fcf=20, visibility=17, bottleneck=10, mispricing=14, valuation=14),
        ),
        E2RArchetype.TIRE_AUTO_COMPONENT_SPREAD: ArchetypeDefinition(
            archetype=E2RArchetype.TIRE_AUTO_COMPONENT_SPREAD,
            stage1_radar_signals=("tire demand recovery", "raw-material spread", "replacement tire demand"),
            stage2_candidate_signals=("OE/RE mix improves", "OP/EPS revision", "North America demand stable"),
            stage3_high_conviction_signals=("spread and FCF persist", "China competition controlled"),
            stage4a_ongoing_signals=("replacement demand and margin remain healthy",),
            stage4b_graduation_overheat_signals=("spread peak ignored", "auto cycle fully priced"),
            stage4c_thesis_break_signals=("North America demand slowdown", "raw-material spike", "tariff hit", "vehicle sales slowdown"),
            key_evidence_families=("financial_actual", "research_report", "news"),
            false_positive_patterns=("auto sales recovery treated as tire margin proof", "raw-material spread is one-off"),
            preferred_score_weights=_weights(eps_fcf=18, visibility=13, bottleneck=12, mispricing=11, valuation=10),
        ),
        E2RArchetype.AIRLINE_TRAVEL_CYCLE: ArchetypeDefinition(
            archetype=E2RArchetype.AIRLINE_TRAVEL_CYCLE,
            stage1_radar_signals=("passenger recovery", "cargo rate", "airline merger", "reopening news"),
            stage2_candidate_signals=("revenue/OP improvement", "integration synergy", "passenger cargo mix"),
            stage3_high_conviction_signals=("FCF and cost stability verified", "fuel/FX risk controlled"),
            stage4a_ongoing_signals=("load factor and yield remain strong", "fuel/FX manageable"),
            stage4b_graduation_overheat_signals=("reopening or integration synergy crowded", "oil/FX risk ignored"),
            stage4c_thesis_break_signals=("fuel shock", "FX loss", "integration cost", "cargo/passenger slowdown"),
            key_evidence_families=("financial_actual", "research_report", "news", "price"),
            false_positive_patterns=("traffic recovery without margin", "policy or merger headline only"),
            preferred_score_weights=_weights(eps_fcf=18, visibility=14, bottleneck=5, mispricing=12, valuation=10),
        ),
        E2RArchetype.CASINO_DUTYFREE_TOURISM: ArchetypeDefinition(
            archetype=E2RArchetype.CASINO_DUTYFREE_TOURISM,
            stage1_radar_signals=("visa policy", "tourist arrival recovery", "casino/duty-free policy news"),
            stage2_candidate_signals=("tourist spend", "drop amount", "duty-free sales", "hotel occupancy", "OP leverage"),
            stage3_high_conviction_signals=("visitor mix improves", "China dependence lower", "cash flow and margin visible"),
            stage4a_ongoing_signals=("tourist spend and OPM remain strong",),
            stage4b_graduation_overheat_signals=("tourism policy rally crowded", "policy event priced before spend"),
            stage4c_thesis_break_signals=("visitor mix weak", "duty-free ASP weak", "casino drop slowdown", "CAPEX burden"),
            key_evidence_families=("financial_actual", "research_report", "news"),
            false_positive_patterns=("visa news treated as spend proof", "tourist count without margin"),
            preferred_score_weights=_weights(eps_fcf=18, visibility=13, bottleneck=5, mispricing=12, valuation=10),
        ),
        E2RArchetype.SHIPPING_FREIGHT_CYCLE: ArchetypeDefinition(
            archetype=E2RArchetype.SHIPPING_FREIGHT_CYCLE,
            stage1_radar_signals=("freight rate spike", "Red Sea disruption", "vessel capacity adjustment"),
            stage2_candidate_signals=("rate index improves", "EBITDA improves", "dividend or cash flow rises"),
            stage3_high_conviction_signals=("structural Green is restricted unless multi-year supply discipline is proven",),
            stage4a_ongoing_signals=("rates and cash flow remain above cycle floor",),
            stage4b_graduation_overheat_signals=("freight peak", "shipping stocks crowded", "supply risk ignored"),
            stage4c_thesis_break_signals=("freight rate collapse", "overcapacity", "new ship delivery", "route normalization", "earnings collapse"),
            key_evidence_families=("price", "financial_actual", "research_report", "news"),
            false_positive_patterns=("spot freight spike annualized", "temporary disruption treated as structural"),
            preferred_score_weights=_weights(eps_fcf=20, visibility=8, bottleneck=18, mispricing=8, valuation=8),
        ),
        E2RArchetype.MOBILITY_RENTAL_MICROMOBILITY: ArchetypeDefinition(
            archetype=E2RArchetype.MOBILITY_RENTAL_MICROMOBILITY,
            stage1_radar_signals=("IPO filing", "city expansion", "ridership growth", "fleet expansion"),
            stage2_candidate_signals=("revenue growth", "FCF positive", "unit economics", "utilization rate"),
            stage3_high_conviction_signals=("recurring usage", "FCF and debt stability", "regulatory risk controlled"),
            stage4a_ongoing_signals=("utilization and FCF remain positive",),
            stage4b_graduation_overheat_signals=("IPO valuation crowded", "growth priced before profitability"),
            stage4c_thesis_break_signals=("debt maturity", "regulatory restriction", "seasonality loss", "repair cost spike"),
            key_evidence_families=("financial_actual", "research_report", "news"),
            false_positive_patterns=("user growth without unit economics", "fleet growth with cash burn"),
            preferred_score_weights=_weights(eps_fcf=17, visibility=14, bottleneck=6, mispricing=12, valuation=10),
        ),
        E2RArchetype.URBAN_AIR_DRONE: ArchetypeDefinition(
            archetype=E2RArchetype.URBAN_AIR_DRONE,
            stage1_radar_signals=("Part 135", "strategic investment", "eVTOL policy", "air-taxi partnership"),
            stage2_candidate_signals=("type certification", "production certification", "commercial operation", "customer contract"),
            stage3_high_conviction_signals=("commercial revenue", "unit economics", "cash runway secure"),
            stage4a_ongoing_signals=("certification and production remain on schedule",),
            stage4b_graduation_overheat_signals=("pre-revenue valuation crowded", "certification risk ignored"),
            stage4c_thesis_break_signals=("certification delay", "cash burn", "discounted offering", "production delay"),
            key_evidence_families=("news", "financial_actual", "research_report"),
            false_positive_patterns=("certification step treated as full commercialization", "theme rally before revenue"),
            preferred_score_weights=_weights(eps_fcf=10, visibility=10, bottleneck=6, mispricing=12, valuation=7),
        ),
        E2RArchetype.SATELLITE_CONNECTIVITY_INFRA: ArchetypeDefinition(
            archetype=E2RArchetype.SATELLITE_CONNECTIVITY_INFRA,
            stage1_radar_signals=("airline connectivity contract", "secure communications", "satellite backlog"),
            stage2_candidate_signals=("connectivity revenue growth", "airline contract count", "EBITDA improvement", "backlog"),
            stage3_high_conviction_signals=("recurring connectivity revenue", "gross backlog", "debt/capex manageable"),
            stage4a_ongoing_signals=("contracts convert to revenue", "backlog remains visible"),
            stage4b_graduation_overheat_signals=("satellite connectivity narrative crowded", "debt/capex ignored"),
            stage4c_thesis_break_signals=("launch delay", "contract cancellation", "capex/debt stress", "competitor constellation pressure"),
            key_evidence_families=("financial_actual", "research_report", "news"),
            false_positive_patterns=("space theme without contract", "backlog without cash conversion"),
            preferred_score_weights=_weights(eps_fcf=18, visibility=20, bottleneck=10, mispricing=13, valuation=11),
        ),
        E2RArchetype.ONE_OFF_EVENT_DEMAND: ArchetypeDefinition(
            archetype=E2RArchetype.ONE_OFF_EVENT_DEMAND,
            stage1_radar_signals=("explosive temporary demand", "one-time supply shock", "pandemic/event keyword"),
            stage2_candidate_signals=("short-term EPS spike", "news volume spike", "price breakout"),
            stage3_high_conviction_signals=("normally not Green unless recurrence is proven",),
            stage4a_ongoing_signals=("temporary demand persists longer than expected",),
            stage4b_graduation_overheat_signals=("peak margins", "consensus extrapolates one-off demand"),
            stage4c_thesis_break_signals=("normalization", "ASP collapse", "demand cliff"),
            key_evidence_families=("news", "financial_actual", "research_report"),
            false_positive_patterns=("one-off demand treated as structural", "temporary margin annualized"),
            preferred_score_weights=_weights(eps_fcf=20, visibility=8, bottleneck=8, mispricing=8, valuation=8),
        ),
        E2RArchetype.THEME_VALUATION_OVERHEAT: ArchetypeDefinition(
            archetype=E2RArchetype.THEME_VALUATION_OVERHEAT,
            stage1_radar_signals=("theme keyword spike", "price-only breakout", "retail/crowding signal"),
            stage2_candidate_signals=("requires real estimates or official evidence; otherwise remains watch"),
            stage3_high_conviction_signals=("normally blocked without evidence-backed EPS/FCF path",),
            stage4a_ongoing_signals=("theme evidence remains but valuation is watched"),
            stage4b_graduation_overheat_signals=("return multiple excessive", "reports universally bullish", "valuation saturated"),
            stage4c_thesis_break_signals=("funding/dilution", "estimate cuts", "theme unwind"),
            key_evidence_families=("price", "news", "research_report"),
            false_positive_patterns=("story-only rerating", "no cash flow", "dilution ignored"),
            preferred_score_weights=_weights(eps_fcf=18, visibility=8, bottleneck=8, mispricing=7, valuation=5),
        ),
        E2RArchetype.AI_DATA_CENTER_INFRASTRUCTURE: ArchetypeDefinition(
            archetype=E2RArchetype.AI_DATA_CENTER_INFRASTRUCTURE,
            stage1_radar_signals=("AI data center power demand", "grid bottleneck", "server/rack order keyword"),
            stage2_candidate_signals=("confirmed orders", "capacity constraint", "OP/EPS revision"),
            stage3_high_conviction_signals=("multi-source data-center demand", "power/cooling bottleneck", "EPS/FCF bodyweight change"),
            stage4a_ongoing_signals=("orders convert to revenue", "capacity remains scarce", "revision path intact"),
            stage4b_graduation_overheat_signals=("AI infrastructure narrative crowded", "price outruns orders", "capex slowdown hints"),
            stage4c_thesis_break_signals=("customer capex cut", "order cancellation", "margin pressure"),
            key_evidence_families=("disclosure", "research_report", "news", "consensus_revision"),
            false_positive_patterns=("AI keyword only", "no confirmed order", "power theme without revenue"),
            preferred_score_weights=_weights(eps_fcf=22, visibility=22, bottleneck=21, mispricing=13, valuation=12),
        ),
        E2RArchetype.NUCLEAR_SMR_GRID_POLICY: ArchetypeDefinition(
            archetype=E2RArchetype.NUCLEAR_SMR_GRID_POLICY,
            stage1_radar_signals=("nuclear policy event", "SMR/grid contract keyword", "export project news"),
            stage2_candidate_signals=("contract award", "permitted project timeline", "supplier revenue visibility"),
            stage3_high_conviction_signals=("binding project economics", "multi-year backlog", "EPS/FCF path confirmed"),
            stage4a_ongoing_signals=("project schedule intact", "policy support intact"),
            stage4b_graduation_overheat_signals=("policy premium crowds valuation", "legal delay ignored"),
            stage4c_thesis_break_signals=("legal delay", "project cancellation", "cost overrun"),
            key_evidence_families=("disclosure", "news", "research_report"),
            false_positive_patterns=("policy headline without contract", "legal appeal ignored"),
            preferred_score_weights=_weights(eps_fcf=18, visibility=24, bottleneck=14, mispricing=15, valuation=12),
        ),
        E2RArchetype.VALUE_UP_SHAREHOLDER_RETURN: ArchetypeDefinition(
            archetype=E2RArchetype.VALUE_UP_SHAREHOLDER_RETURN,
            stage1_radar_signals=("buyback/cancellation", "dividend policy", "value-up disclosure"),
            stage2_candidate_signals=("ROE improvement", "capital return durability", "NAV discount narrowing catalyst"),
            stage3_high_conviction_signals=("repeatable cash return", "governance improvement", "earnings/NAV support"),
            stage4a_ongoing_signals=("capital return continues", "balance sheet remains healthy"),
            stage4b_graduation_overheat_signals=("event premium fully priced", "return policy no longer incremental"),
            stage4c_thesis_break_signals=("buyback without cancellation", "governance dispute", "credit deterioration"),
            key_evidence_families=("disclosure", "financial_actual", "news", "research_report"),
            false_positive_patterns=("announcement-only premium", "no FCF/NAV improvement", "one-off event"),
            preferred_score_weights=_weights(eps_fcf=16, visibility=19, bottleneck=8, mispricing=24, valuation=20),
        ),
        E2RArchetype.CLOUD_AI_SOFTWARE_INFRA: ArchetypeDefinition(
            archetype=E2RArchetype.CLOUD_AI_SOFTWARE_INFRA,
            stage1_radar_signals=("cloud ERP transition", "B2B SaaS expansion", "AI workflow feature"),
            stage2_candidate_signals=("ARR growth", "recurring revenue", "customer retention", "OPM improvement"),
            stage3_high_conviction_signals=("customer lock-in", "FCF conversion", "net retention", "old software-frame rerating"),
            stage4a_ongoing_signals=("ARR and retention remain strong", "FCF conversion continues"),
            stage4b_graduation_overheat_signals=("AI SaaS narrative crowded", "valuation saturation"),
            stage4c_thesis_break_signals=("churn spike", "AI compute cost surge", "OPM decline", "services revenue reversion"),
            key_evidence_families=("financial_actual", "research_report", "news"),
            false_positive_patterns=("AI feature only", "SI-like revenue mistaken for SaaS", "retention not verified"),
            preferred_score_weights=_weights(eps_fcf=20, visibility=23, bottleneck=8, mispricing=16, valuation=14),
        ),
        E2RArchetype.AI_SOFTWARE_APPLICATION: ArchetypeDefinition(
            archetype=E2RArchetype.AI_SOFTWARE_APPLICATION,
            stage1_radar_signals=("AI application launch", "enterprise adoption headline", "API usage growth"),
            stage2_candidate_signals=("paid customer growth", "API revenue", "workflow integration", "gross margin visibility"),
            stage3_high_conviction_signals=("repeat paid usage", "FCF conversion", "compute cost controlled"),
            stage4a_ongoing_signals=("paid usage expands", "unit economics remain healthy"),
            stage4b_graduation_overheat_signals=("AI app narrative crowded", "valuation before margin proof"),
            stage4c_thesis_break_signals=("compute cost spike", "model dependency", "copyright or data lawsuit"),
            key_evidence_families=("financial_actual", "research_report", "news"),
            false_positive_patterns=("AI label without paid usage", "free user growth mistaken for revenue"),
            preferred_score_weights=_weights(eps_fcf=19, visibility=18, bottleneck=9, mispricing=15, valuation=13),
        ),
        E2RArchetype.GAME_CONTENT_IP: ArchetypeDefinition(
            archetype=E2RArchetype.GAME_CONTENT_IP,
            stage1_radar_signals=("new title announcement", "IP expansion", "platform user growth"),
            stage2_candidate_signals=("bookings growth", "sell-through", "live-service monetization", "OP/EPS revision"),
            stage3_high_conviction_signals=("repeat IP portfolio", "global monetization", "low single-title risk"),
            stage4a_ongoing_signals=("bookings and live service remain strong", "pipeline executes"),
            stage4b_graduation_overheat_signals=("single IP valuation crowded", "launch expectations saturated"),
            stage4c_thesis_break_signals=("title delay", "bookings guide cut", "child safety regulation", "user growth slowdown"),
            key_evidence_families=("financial_actual", "research_report", "news"),
            false_positive_patterns=("pre-release hype", "single-title dependency", "user growth without monetization"),
            preferred_score_weights=_weights(eps_fcf=20, visibility=18, bottleneck=6, mispricing=14, valuation=12),
        ),
        E2RArchetype.MEDIA_AD_CONTENT_CYCLE: ArchetypeDefinition(
            archetype=E2RArchetype.MEDIA_AD_CONTENT_CYCLE,
            stage1_radar_signals=("ad market recovery", "CTV growth", "digital ad rebound"),
            stage2_candidate_signals=("ad revenue growth", "ARPU improvement", "OPM improvement"),
            stage3_high_conviction_signals=("repeat platform ad revenue", "hybrid subscription/ad model", "budget resilience"),
            stage4a_ongoing_signals=("ad revenue and ARPU remain strong",),
            stage4b_graduation_overheat_signals=("ad-tech valuation crowded", "growth expectations saturated"),
            stage4c_thesis_break_signals=("client budget cut", "revenue miss", "privacy lawsuit", "scam ad regulation"),
            key_evidence_families=("financial_actual", "research_report", "news"),
            false_positive_patterns=("cyclical ad rebound treated as structural", "privacy risk ignored"),
            preferred_score_weights=_weights(eps_fcf=18, visibility=16, bottleneck=6, mispricing=14, valuation=12),
        ),
        E2RArchetype.SECURITY_IDENTITY_DEEPFAKE: ArchetypeDefinition(
            archetype=E2RArchetype.SECURITY_IDENTITY_DEEPFAKE,
            stage1_radar_signals=("cybersecurity demand", "identity threat", "deepfake regulation"),
            stage2_candidate_signals=("ARR growth", "customer diversification", "low churn", "OPM improvement"),
            stage3_high_conviction_signals=("security platform lock-in", "renewal strength", "operational trust intact"),
            stage4a_ongoing_signals=("renewals and trust remain strong",),
            stage4b_graduation_overheat_signals=("security valuation crowded", "incident risk ignored"),
            stage4c_thesis_break_signals=("global outage", "customer lawsuit", "renewal risk", "trust damage"),
            key_evidence_families=("financial_actual", "research_report", "news"),
            false_positive_patterns=("threat narrative without revenue", "operational trust risk ignored"),
            preferred_score_weights=_weights(eps_fcf=20, visibility=20, bottleneck=10, mispricing=14, valuation=13),
        ),
        E2RArchetype.BIOTECH_ROYALTY_COMMERCIALIZATION: ArchetypeDefinition(
            archetype=E2RArchetype.BIOTECH_ROYALTY_COMMERCIALIZATION,
            stage1_radar_signals=("royalty deal", "commercial launch", "milestone payment"),
            stage2_candidate_signals=("royalty economics", "partner launch progress", "cash runway"),
            stage3_high_conviction_signals=("commercial royalty visibility", "repeatable milestone/royalty path", "dilution risk controlled"),
            stage4a_ongoing_signals=("launch curve intact", "partner execution intact"),
            stage4b_graduation_overheat_signals=("royalty curve fully priced", "trial/news crowding"),
            stage4c_thesis_break_signals=("trial failure", "label/commercial setback", "CB/dilution pressure"),
            key_evidence_families=("disclosure", "news", "research_report"),
            false_positive_patterns=("pre-revenue story treated as cash flow", "dilution ignored"),
            preferred_score_weights=_weights(eps_fcf=15, visibility=23, bottleneck=9, mispricing=18, valuation=12),
        ),
        E2RArchetype.CDMO_HEALTHCARE_CONTRACT: ArchetypeDefinition(
            archetype=E2RArchetype.CDMO_HEALTHCARE_CONTRACT,
            stage1_radar_signals=("CDMO contract", "capacity utilization", "new plant validation"),
            stage2_candidate_signals=("multi-year manufacturing order", "utilization ramp", "margin path"),
            stage3_high_conviction_signals=("contracted capacity", "utilization leverage", "FCF path"),
            stage4a_ongoing_signals=("utilization and order intake remain strong",),
            stage4b_graduation_overheat_signals=("capacity priced before utilization", "customer concentration ignored"),
            stage4c_thesis_break_signals=("underutilization", "contract delay", "quality issue"),
            key_evidence_families=("disclosure", "financial_actual", "research_report"),
            false_positive_patterns=("capacity exists but demand absent", "validation delay"),
            preferred_score_weights=_weights(eps_fcf=20, visibility=24, bottleneck=16, mispricing=14, valuation=12),
        ),
        E2RArchetype.CRO_CLINICAL_SERVICE: ArchetypeDefinition(
            archetype=E2RArchetype.CRO_CLINICAL_SERVICE,
            stage1_radar_signals=("clinical service backlog", "pharma R&D budget", "trial volume growth"),
            stage2_candidate_signals=("repeat clinical-service revenue", "customer diversification", "OP/EPS improvement"),
            stage3_high_conviction_signals=("multi-year service backlog", "funding cycle stable", "high FCF conversion"),
            stage4a_ongoing_signals=("backlog converts to revenue", "customer funding remains healthy"),
            stage4b_graduation_overheat_signals=("CRO recovery priced before backlog", "valuation multiple crowded"),
            stage4c_thesis_break_signals=("biotech funding crunch", "customer R&D budget cut", "forecast cut"),
            key_evidence_families=("financial_actual", "research_report", "news"),
            false_positive_patterns=("R&D cycle headline without orders", "low-margin backlog", "customer budget cliff"),
            preferred_score_weights=_weights(eps_fcf=18, visibility=20, bottleneck=8, mispricing=12, valuation=12),
        ),
        E2RArchetype.BIOSIMILAR_COMMERCIALIZATION: ArchetypeDefinition(
            archetype=E2RArchetype.BIOSIMILAR_COMMERCIALIZATION,
            stage1_radar_signals=("biosimilar approval", "patent expiry", "commercial launch news"),
            stage2_candidate_signals=("PBM or reimbursement listing", "prescription conversion", "launch revenue"),
            stage3_high_conviction_signals=("prescription growth", "margin defense", "multi-market launch"),
            stage4a_ongoing_signals=("launch curve intact", "pricing remains disciplined"),
            stage4b_graduation_overheat_signals=("approval headline fully priced", "biosimilar launch crowded"),
            stage4c_thesis_break_signals=("price competition", "prescription conversion delay", "margin collapse"),
            key_evidence_families=("news", "financial_actual", "research_report"),
            false_positive_patterns=("approval treated as revenue", "PBM access missing", "price erosion ignored"),
            preferred_score_weights=_weights(eps_fcf=18, visibility=20, bottleneck=6, mispricing=13, valuation=11),
        ),
        E2RArchetype.OBESITY_GLP1_COMMERCIALIZATION: ArchetypeDefinition(
            archetype=E2RArchetype.OBESITY_GLP1_COMMERCIALIZATION,
            stage1_radar_signals=("GLP-1 approval", "obesity drug prescription growth", "oral GLP-1 trial result"),
            stage2_candidate_signals=("weekly prescriptions", "insurance coverage", "supply capacity", "sales ramp"),
            stage3_high_conviction_signals=("durable prescription growth", "price defense", "OP/EPS revision"),
            stage4a_ongoing_signals=("prescriptions and supply remain strong", "coverage expands"),
            stage4b_graduation_overheat_signals=("obesity market narrative crowded", "valuation runs ahead of scripts"),
            stage4c_thesis_break_signals=("price cut", "compounded alternative", "coverage denial", "prescription slowdown"),
            key_evidence_families=("financial_actual", "research_report", "news"),
            false_positive_patterns=("market size story without uptake", "competition ignored", "coverage assumed"),
            preferred_score_weights=_weights(eps_fcf=22, visibility=20, bottleneck=12, mispricing=13, valuation=12),
        ),
        E2RArchetype.GENE_THERAPY_RARE_DISEASE: ArchetypeDefinition(
            archetype=E2RArchetype.GENE_THERAPY_RARE_DISEASE,
            stage1_radar_signals=("gene therapy approval", "rare disease unmet need", "patient recruitment"),
            stage2_candidate_signals=("treated patients", "reimbursement", "commercial sales"),
            stage3_high_conviction_signals=("repeat commercial uptake", "cash runway", "dilution risk controlled"),
            stage4a_ongoing_signals=("uptake and reimbursement remain intact",),
            stage4b_graduation_overheat_signals=("approval news priced as full commercialization",),
            stage4c_thesis_break_signals=("slow uptake", "cash crunch", "going concern", "dilutive financing"),
            key_evidence_families=("news", "financial_actual", "research_report"),
            false_positive_patterns=("approval without commercialization", "patient access friction", "cash burn ignored"),
            preferred_score_weights=_weights(eps_fcf=8, visibility=12, bottleneck=8, mispricing=10, valuation=6),
        ),
        E2RArchetype.AI_DRUG_DISCOVERY_PLATFORM: ArchetypeDefinition(
            archetype=E2RArchetype.AI_DRUG_DISCOVERY_PLATFORM,
            stage1_radar_signals=("AI drug discovery partnership", "candidate molecule", "platform milestone"),
            stage2_candidate_signals=("big pharma milestone", "clinical entry", "cash runway"),
            stage3_high_conviction_signals=("commercial or royalty path", "validated pipeline", "cash burn controlled"),
            stage4a_ongoing_signals=("pipeline advances with partner funding",),
            stage4b_graduation_overheat_signals=("AI platform label crowded", "valuation before clinical proof"),
            stage4c_thesis_break_signals=("clinical failure", "cash burn", "platform hype unwind"),
            key_evidence_families=("news", "research_report", "disclosure"),
            false_positive_patterns=("PoC treated as drug approval", "AI label without economics"),
            preferred_score_weights=_weights(eps_fcf=6, visibility=10, bottleneck=7, mispricing=12, valuation=6),
        ),
        E2RArchetype.DIGITAL_HEALTHCARE_AI: ArchetypeDefinition(
            archetype=E2RArchetype.DIGITAL_HEALTHCARE_AI,
            stage1_radar_signals=("clinical AI paper", "regulatory clearance", "hospital pilot"),
            stage2_candidate_signals=("hospital adoption", "reimbursement", "paid workflow", "recurring revenue"),
            stage3_high_conviction_signals=("workflow embedded", "recurring revenue", "OP improvement", "liability risk low"),
            stage4a_ongoing_signals=("hospital usage expands", "reimbursement remains intact"),
            stage4b_graduation_overheat_signals=("AI healthcare narrative crowded", "paper-only valuation premium"),
            stage4c_thesis_break_signals=("subgroup performance issue", "reimbursement denial", "liability event"),
            key_evidence_families=("research_report", "news", "financial_actual"),
            false_positive_patterns=("AUC headline without adoption", "pilot without revenue", "bias risk ignored"),
            preferred_score_weights=_weights(eps_fcf=18, visibility=17, bottleneck=8, mispricing=13, valuation=12),
        ),
        E2RArchetype.MEDICAL_DEVICE_HEALTHCARE_EXPORT: ArchetypeDefinition(
            archetype=E2RArchetype.MEDICAL_DEVICE_HEALTHCARE_EXPORT,
            stage1_radar_signals=("medical device export growth", "new approval", "procedure growth"),
            stage2_candidate_signals=("repeat consumable revenue", "export channel", "OPM/ROE improvement"),
            stage3_high_conviction_signals=("recurring procedure demand", "ASP stable", "FCF improvement"),
            stage4a_ongoing_signals=("export channel and procedures remain strong",),
            stage4b_graduation_overheat_signals=("medical-device premium crowded", "target multiples saturated"),
            stage4c_thesis_break_signals=("approval delay", "safety issue", "price control", "channel failure"),
            key_evidence_families=("financial_actual", "research_report", "news"),
            false_positive_patterns=("one-time device sale", "approval without channel", "safety risk ignored"),
            preferred_score_weights=_weights(eps_fcf=20, visibility=22, bottleneck=13, mispricing=14, valuation=12),
        ),
    }
)


def archetype_definition(archetype: E2RArchetype | str) -> ArchetypeDefinition:
    """Return the definition for an archetype."""

    if not isinstance(archetype, E2RArchetype):
        archetype = E2RArchetype(str(archetype))
    return ARCHETYPE_DEFINITIONS[archetype]


def all_archetype_definitions() -> tuple[ArchetypeDefinition, ...]:
    """Return definitions for all archetypes."""

    return tuple(ARCHETYPE_DEFINITIONS[item] for item in E2RArchetype)


POSITIVE_GROUPS = frozenset({"structural_success", "success_candidate", "cyclical_success"})
COUNTEREXAMPLE_GROUPS = frozenset(
    {"one_off", "boom_bust", "overheat", "failed_rerating", "event_premium", "4b_watch", "4c_thesis_break"}
)


__all__ = [
    "ARCHETYPE_DEFINITIONS",
    "COUNTEREXAMPLE_GROUPS",
    "POSITIVE_GROUPS",
    "ArchetypeDefinition",
    "E2RArchetype",
    "all_archetype_definitions",
    "archetype_definition",
]
