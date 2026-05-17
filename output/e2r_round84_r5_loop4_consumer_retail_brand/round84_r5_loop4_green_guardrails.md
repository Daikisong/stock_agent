# Round-84 R5 Loop-4 Green Guardrails

| target | posture | Green unlock evidence | Loop-4 penalties |
| --- | --- | --- | --- |
| `EXPORT_RECURRING_CONSUMER` | GREEN_POSSIBLE | export_growth, recurring_demand, channel_sell_through, reorder_signal, opm_improvement, eps_revision | single_product, recall, foreign_inventory, channel_stuffing |
| `K_FOOD_SINGLE_HERO_PRODUCT` | GREEN_POSSIBLE | sku_expansion, multi_country_sell_through, repeat_purchase, opm_improvement | hero_product_dependency, recall, viral_safety, foreign_inventory |
| `K_FOOD_GLOBAL_PORTFOLIO_EXPANSION` | WATCH_YELLOW_FIRST | multi_sku_sales, multi_country_sell_through, repeat_purchase, opm_improvement, inventory_stable | sku_expansion, foreign_inventory, capa, food_safety |
| `K_BEAUTY_EXPORT_DISTRIBUTION` | GREEN_POSSIBLE | export_growth, offline_channel_sell_through, reorder_signal, opm_roe_improvement, inventory_receivables_stable | tariff, sell_through, inventory, receivables, china_slowdown |
| `K_BEAUTY_OFFLINE_SELL_THROUGH` | WATCH_YELLOW_FIRST | offline_sell_through, reorder_signal, store_expansion, inventory_receivables_stable | sell_through, reorder, inventory, receivables, discount |
| `BEAUTY_DEVICE_EXPORT` | GREEN_POSSIBLE | device_unit_sales, device_asp, device_margin, repeat_consumables, opm_improvement | 4b_crowding, device_competition, regulation, tariff |
| `BEAUTY_DEVICE_AFFILIATE_COMMERCE` | WATCH_YELLOW_FIRST | affiliate_cac_stable, discount_rate_stable, reorder_signal, opm_improvement | cac, discount, creator_dependency, viral_fade, inventory |
| `BEAUTY_OEM_ODM_SUPPLYCHAIN` | GREEN_POSSIBLE | customer_diversification, repeat_orders, capacity_utilization, opm_improvement, receivables_stable | customer_diversification, inventory, receivables, brand_sell_through |
| `RETAIL_CONVENIENCE_OFFLINE` | WATCH_YELLOW_FIRST | same_store_sales, pb_mix, opm_improvement, fcf_stability | sssg, pb_mix, store_profitability, rent_wage |
| `RETAIL_ECOMMERCE_LOGISTICS` | WATCH_YELLOW_FIRST | repeat_customer_base, logistics_efficiency, fcf_improvement, trust_and_regulation_clean | data_security, supplier_regulation, logistics_cost, fcf, margin_quality |
| `ECOMMERCE_FRESH_LOGISTICS` | WATCH_YELLOW_FIRST | unit_economics, repeat_orders, waste_rate_control, fcf_path | waste_rate, delivery_cost, cash_burn |
| `APPAREL_FAST_FASHION_BRAND_OEM` | WATCH_YELLOW_FIRST | order_visibility, inventory_turnover, discount_rate_control, opm_improvement | inventory, discount, ip_litigation, product_safety, tariff |
| `ULTRA_LOW_COST_CROSSBORDER_PLATFORM` | REDTEAM_FIRST | unit_economics, customs_compliance, product_safety_process, opm_fcf_improvement | unsafe_items, dsa, de_minimis, ip_litigation, tariff |
| `HOME_LIVING_APPLIANCE_RENTAL` | WATCH_YELLOW_FIRST | rental_accounts, churn_stable, recurring_service_revenue, fcf_improvement | churn, overseas_margin, hardware_cycle, quality_recall |
| `HOME_APPLIANCE_HARDWARE_CYCLE` | REDTEAM_FIRST | recurring_service_revenue, low_churn, fcf_improvement | replacement_demand, housing, dividend, guidance, fcf |
| `HOME_CHILD_EDUCATION` | REDTEAM_FIRST | recurring_demand, channel_expansion, opm_improvement | birth_rate, tam, policy, inventory |
| `CONSUMER_REGULATED_PRODUCT` | WATCH_YELLOW_FIRST | legal_revenue, approval, repeat_revenue, margin_visibility | approval, public_health, regulatory_ban |
| `FOOD_SAFETY_RECALL_OVERLAY` | REDTEAM_FIRST | not_applicable | food_safety, recall, country_ban |
| `DATA_SECURITY_SUPPLIER_REGULATION_OVERLAY` | REDTEAM_FIRST | not_applicable | data_security, supplier_regulation, payment_delay, margin_quality |
| `CHANNEL_STUFFING_INVENTORY_OVERLAY` | REDTEAM_FIRST | not_applicable | shipment_vs_sell_through, inventory, receivables, reorder |
| `TARIFF_IMPORT_REGULATION_OVERLAY` | REDTEAM_FIRST | not_applicable | tariff, import_review, de_minimis, gross_margin_buffer |
| `DISCOUNT_PROMOTION_MARGIN_OVERLAY` | REDTEAM_FIRST | not_applicable | discount, affiliate_cac, creator_commission, gross_margin, viral_fade |

## What Not To Change

- Do not apply R5 Loop-4 v4.0 weights to production scoring yet.
- Do not treat viral demand, channel entry, GMV, user count, store count, or appliance hardware sales as Green evidence by themselves.
- Do not invent export growth, sell-through, reorder, inventory, receivables, churn, tariff rate, FCF, or stage prices.
- Treat food recall, country sales ban, data breach, supplier regulation, payment delay, channel stuffing, IP litigation, product safety, and tariff/import damage as RedTeam fields.
