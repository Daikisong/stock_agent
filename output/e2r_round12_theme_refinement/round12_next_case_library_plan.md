# Round-12 Next Case Library Plan

## Add Planned Case Records
- `convenience_store_efficiency_success_candidate` -> `RETAIL_CONVENIENCE_OFFLINE`
- `home_shopping_margin_decline_counterexample` -> `RETAIL_CONVENIENCE_OFFLINE`
- `ecommerce_fresh_logistics_candidate` -> `ECOMMERCE_FRESH_LOGISTICS`
- `china_direct_purchase_margin_pressure_counterexample` -> `ECOMMERCE_FRESH_LOGISTICS`
- `nonlife_insurance_loss_ratio_success_candidate` -> `INSURANCE_UNDERWRITING_CYCLE`
- `life_insurance_csm_candidate` -> `INSURANCE_UNDERWRITING_CYCLE`
- `stablecoin_payment_infra_candidate` -> `PAYMENT_FINTECH_INFRA`
- `sto_platform_candidate` -> `PAYMENT_FINTECH_INFRA`
- `crypto_theme_no_revenue_counterexample` -> `DIGITAL_ASSET_TOKENIZATION`
- `regulation_crackdown_4c` -> `DIGITAL_ASSET_TOKENIZATION`
- `kbeauty_oem_odm_success_candidate` -> `BEAUTY_OEM_ODM_SUPPLYCHAIN`
- `channel_stuffing_receivables_4c` -> `BEAUTY_OEM_ODM_SUPPLYCHAIN`
- `pork_price_cycle_candidate` -> `AGRI_LIVESTOCK_FOOD_COMMODITY`
- `feed_cost_squeeze_counterexample` -> `AGRI_LIVESTOCK_FOOD_COMMODITY`
- `cement_price_hike_candidate` -> `BUILDING_MATERIALS_CYCLE`
- `housing_slowdown_materials_4c` -> `BUILDING_MATERIALS_CYCLE`
- `heatwave_power_demand_candidate` -> `RENEWABLE_ENERGY_POLICY`
- `disaster_rebuild_materials_event` -> `RENEWABLE_ENERGY_POLICY`
- `hydrogen_fuel_cell_plant_candidate` -> `HYDROGEN_FUEL_CELL_INFRA`
- `hydrogen_theme_no_revenue_counterexample` -> `HYDROGEN_FUEL_CELL_INFRA`
- `solar_policy_candidate` -> `SOLAR_TARIFF_SUPPLYCHAIN`
- `solar_tariff_supplychain_4c` -> `SOLAR_TARIFF_SUPPLYCHAIN`
- `tire_spread_success_candidate` -> `TIRE_AUTO_COMPONENT_SPREAD`
- `factory_fire_4c_counterexample` -> `TIRE_AUTO_COMPONENT_SPREAD`
- `infectious_disease_oneoff_counterexample` -> `EVENT_DISEASE_PEST_DEMAND`
- `fine_dust_mask_oneoff_counterexample` -> `EVENT_DISEASE_PEST_DEMAND`
- `speculative_science_theme_counterexample` -> `SPECULATIVE_SCIENCE_THEME`
- `ai_dc_theme_no_order` -> `SPECULATIVE_SCIENCE_THEME`
- `waste_recycling_candidate` -> `WASTE_RECYCLING_ENVIRONMENT`
- `battery_recycling_price_reversal_counterexample` -> `WASTE_RECYCLING_ENVIRONMENT`
- `media_ad_recovery_candidate` -> `MEDIA_AD_CONTENT_CYCLE`
- `new_game_hype_fail` -> `MEDIA_AD_CONTENT_CYCLE`
- `douzone_saas_candidate` -> `CLOUD_AI_SOFTWARE_INFRA`
- `mau_only_platform` -> `CLOUD_AI_SOFTWARE_INFRA`
- `security_identity_candidate` -> `SECURITY_IDENTITY_DEEPFAKE`
- `deepfake_theme_no_revenue_counterexample` -> `SECURITY_IDENTITY_DEEPFAKE`

## What Not To Change
- Do not apply score_weight_profile to production scoring yet.
- Do not use theme tags as evidence.
- Do not make one-off disease, speculative science, or tokenization themes Green without verified recurring revenue and EPS/FCF evidence.
