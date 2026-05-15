# Round-33 Green Guardrail Review

| target | posture | Green unlock evidence | Red flags |
|---|---|---|---|
| MEDIA_AD_CONTENT_CYCLE | WATCH_YELLOW_FIRST | repeat_ad_inventory, ad_arpu_growth, owned_ad_platform, opm_improvement | ad_cycle, platform_shift, client_budget_cut, privacy_regulation, traditional_media_decline |
| PAPER_PACKAGING_CYCLE | REDTEAM_FIRST | packaging_price_hike, raw_material_cost_stable, customer_contract, fcf_improvement | pulp_price, overcapacity, mature_growth, pricing_pressure, ma_expectation_only |
| SMART_FARM_AGRI_TECH | WATCH_YELLOW_FIRST | smart_farm_order, operation_contract, recurring_service, adoption_economics_visible | commodity_cycle, disease_event, subsidy, weather, feed_cost, technical_barrier |
| CONSUMER_REGULATED_PRODUCT | WATCH_YELLOW_FIRST | regulatory_approval, legal_sales_permission, repeat_consumption, distribution_network | regulation, legal_conflict, public_health, social_backlash, approval_uncertain |
| APPAREL_FAST_FASHION | WATCH_YELLOW_FIRST | fast_inventory_turn, low_markdown, overseas_channel_expansion, opm_fcf_improvement | inventory, markdown, ip_legal, product_safety, regulatory_crackdown, supply_chain_labor |
| AI_SOFTWARE_APPLICATION | GREEN_POSSIBLE | recurring_subscription_or_api, customer_lock_in, compute_cost_controlled, opm_improvement | compute_cost, copyright, licensing, data_privacy, model_dependency, feature_only_ai |
| METAVERSE_NFT_THEME | REDTEAM_FIRST | real_platform_fee, repeat_transaction_volume, fcf_conversion | extreme_theme, no_revenue, liquidity_collapse, regulatory, price_only_rally |
| FOOD_AGRI_LIVESTOCK_CYCLE | REDTEAM_FIRST | price_pass_through, raw_material_cost_stable, repeat_demand, recurring_non_event_demand | disease_event, feed_cost, weather, price_normalization, one_off_supply_shock |

## What Not To Change
- Do not apply v1.8 weights to production scoring yet.
- Do not use case IDs or theme labels as candidate-generation input.
- Do not invent stage dates, prices, ad ARPU, packaging price hikes, smart-farm contracts, cannabis approvals, inventory turnover, AI subscription revenue, license status, NFT transaction volume, or livestock disease normalization.
- Do not lower Stage 3-Green thresholds to improve recall.
