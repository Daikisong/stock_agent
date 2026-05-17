# Round-110 R5 Loop-6 Green Guardrails

| target | posture | Green unlock evidence | Loop-6 penalties |
| --- | --- | --- | --- |
| `EXPORT_RECURRING_CONSUMER` | GREEN_POSSIBLE | export_growth, recurring_demand, channel_sell_through, reorder_signal, opm_improvement, eps_revision | single_product, recall, foreign_inventory, channel_stuffing |
| `K_FOOD_SINGLE_HERO_PRODUCT` | WATCH_YELLOW_FIRST | sku_expansion, multi_country_sell_through, repeat_purchase, opm_improvement | hero_product_dependency, recall, viral_safety, foreign_inventory |
| `K_FOOD_GLOBAL_PORTFOLIO_EXPANSION` | WATCH_YELLOW_FIRST | multi_sku_sales, multi_country_sell_through, repeat_purchase, opm_improvement, inventory_stable | sku_expansion, foreign_inventory, capa, food_safety |
| `K_FOOD_VIRAL_BRAND_CULTURE` | WATCH_YELLOW_FIRST | sell_through, reorder_signal, opm_improvement, repeat_purchase | viral_fade, single_campaign, reorder_unverified, discount |
| `K_BEAUTY_EXPORT_DISTRIBUTION` | GREEN_POSSIBLE | export_growth, offline_channel_sell_through, reorder_signal, opm_roe_improvement, inventory_receivables_stable | tariff, sell_through, inventory, receivables, china_slowdown |
| `K_BEAUTY_OFFLINE_SELL_THROUGH` | WATCH_YELLOW_FIRST | offline_sell_through, reorder_signal, store_expansion, inventory_receivables_stable | sell_through, reorder, inventory, receivables, discount |
| `K_BEAUTY_RETAIL_PLATFORM` | WATCH_YELLOW_FIRST | store_level_sell_through, reorder_signal, inventory_stable, opm_fcf_improvement | store_economics, inventory, brand_churn, channel_conflict, sell_through |
| `K_BEAUTY_TARIFF_IMPORT_REVIEW` | REDTEAM_FIRST | not_applicable | tariff, import_review, price_increase, gross_margin_buffer |
| `BEAUTY_DEVICE_EXPORT` | GREEN_POSSIBLE | device_unit_sales, device_asp, device_margin, repeat_consumables, opm_improvement | 4b_crowding, device_competition, regulation, tariff |
| `BEAUTY_DEVICE_AFFILIATE_COMMERCE` | WATCH_YELLOW_FIRST | affiliate_cac_stable, discount_rate_stable, reorder_signal, opm_improvement | cac, discount, creator_dependency, viral_fade, inventory |
| `BEAUTY_DEVICE_REGULATORY_SAFETY` | REDTEAM_FIRST | not_applicable | device_safety, medical_claim, country_regulation |
| `BEAUTY_OEM_ODM_SUPPLYCHAIN` | GREEN_POSSIBLE | customer_diversification, repeat_orders, capacity_utilization, opm_improvement, receivables_stable | customer_diversification, inventory, receivables, brand_sell_through |
| `BEAUTY_FAST_PRODUCT_CYCLE_RISK` | REDTEAM_FIRST | not_applicable | sku_overexpansion, brand_churn, inventory, receivables |
| `RETAIL_CONVENIENCE_OFFLINE` | WATCH_YELLOW_FIRST | same_store_sales, pb_mix, opm_improvement, fcf_stability | sssg, pb_mix, store_profitability, rent_wage |
| `RETAIL_ECOMMERCE_LOGISTICS` | WATCH_YELLOW_FIRST | repeat_customer_base, logistics_efficiency, fcf_improvement, trust_and_regulation_clean | data_security, supplier_regulation, logistics_cost, fcf, margin_quality |
| `ECOMMERCE_FRESH_LOGISTICS` | WATCH_YELLOW_FIRST | unit_economics, repeat_orders, waste_rate_control, fcf_path | waste_rate, delivery_cost, cash_burn |
| `APPAREL_FAST_FASHION_BRAND_OEM` | WATCH_YELLOW_FIRST | order_visibility, inventory_turnover, discount_rate_control, opm_improvement | inventory, discount, ip_litigation, product_safety, tariff |
| `ULTRA_LOW_COST_CROSSBORDER_PLATFORM` | REDTEAM_FIRST | unit_economics, customs_compliance, product_safety_process, opm_fcf_improvement | unsafe_items, dsa, de_minimis, ip_litigation, tariff |
| `FAST_FASHION_IP_SUPPLIER_LITIGATION` | REDTEAM_FIRST | not_applicable | ip_litigation, supplier_exclusivity, competition_law |
| `FAST_FASHION_PRODUCT_SAFETY_DSA` | REDTEAM_FIRST | not_applicable | unsafe_items, dsa, product_safety, customs |
| `HOME_LIVING_APPLIANCE_RENTAL` | WATCH_YELLOW_FIRST | rental_accounts, churn_stable, recurring_service_revenue, fcf_improvement | churn, overseas_margin, hardware_cycle, quality_recall |
| `HOME_APPLIANCE_HARDWARE_CYCLE` | REDTEAM_FIRST | recurring_service_revenue, low_churn, fcf_improvement | replacement_demand, housing, dividend, guidance, fcf |
| `HOME_CHILD_EDUCATION` | REDTEAM_FIRST | recurring_demand, channel_expansion, opm_improvement | birth_rate, tam, policy, inventory |
| `CONSUMER_REGULATED_PRODUCT` | WATCH_YELLOW_FIRST | legal_revenue, approval, repeat_revenue, margin_visibility | approval, public_health, regulatory_ban |
| `FOOD_SAFETY_RECALL_OVERLAY` | REDTEAM_FIRST | not_applicable | food_safety, recall, country_ban |
| `ECOMMERCE_TRUST_SECURITY` | REDTEAM_FIRST | not_applicable | data_security, privacy, trust_damage, security_cost |
| `CHANNEL_STUFFING_INVENTORY_OVERLAY` | REDTEAM_FIRST | not_applicable | shipment_vs_sell_through, inventory, receivables, reorder |
| `ECOMMERCE_SUPPLIER_MARGIN_QUALITY` | REDTEAM_FIRST | not_applicable | supplier_pressure, payment_delay, margin_quality, regulation |
| `DISCOUNT_PROMOTION_MARGIN_OVERLAY` | REDTEAM_FIRST | not_applicable | discount, affiliate_cac, creator_commission, gross_margin, viral_fade |
| `DISCLOSURE_CONFIDENCE_CAP` | REDTEAM_FIRST | not_applicable | disclosure_detail, parser_confidence, sell_through, margin_detail |

## What Not To Change

- Do not apply R5 Loop-6 v6.0 weights to production scoring yet.
- Do not treat viral demand, channel entry, GMV, user count, store count, or appliance hardware sales as Green evidence by themselves.
- Do not invent export growth, sell-through, reorder, inventory, receivables, churn, tariff rate, FCF, or stage prices.
- Treat food recall, country sales ban, data breach, supplier regulation, payment delay, channel stuffing, IP litigation, product safety, and tariff/import damage as RedTeam fields.
