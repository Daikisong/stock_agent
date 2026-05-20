# Round 252 R9 Price Validation Plan

- price_validation_completed: partial_with_reported_price_anchors
- full_adjusted_ohlc_complete: false
- hard_4c_confirmed: true
- Do not invent OHLC, peak, MFE, MAE, stage prices, margin, FCF, yield, load factor, tourist spend, or safety costs.

## Backfill Fields

- price_data_source
- full_adjusted_ohlc_available
- reported_price_anchor
- reported_event_return
- stage1_price
- stage2_price
- stage3_price
- stage4b_price
- stage4c_price
- event_mfe_1d
- event_mae_1d
- event_close_return
- relative_underperformance_pp
- tariff_or_margin_anchor
- logistics_or_supply_chain_anchor
- fleet_yield_load_factor_anchor
- safety_or_factory_risk_anchor
- tourism_spend_or_policy_anchor
- price_validation_status

## Case Anchors

| case | data source | reported anchor | status |
|---|---|---|---|
| r9_loop11_hyundai_hybrid_shareholder_return | Reuters investor-day / event-return anchor | buyback up to 4T won over 2025-2027 and hybrid sales target 1.33M by 2028 | reported_event_anchor_not_full_ohlc |
| r9_loop11_hyundai_kia_us_tariff_margin_shock | Reuters tariff / earnings / trade-deal anchors | Kia Q2 2025 tariff hit 786B won / $570M and OP declined 24% YoY | reported_event_anchor_not_full_ohlc |
| r9_loop11_hyundai_glovis_middle_east_logistics_disruption | Reuters logistics-disruption / event-return anchor | Middle East shipments -49%, some shipments diverted to Sri Lanka | reported_event_anchor_not_full_ohlc |
| r9_loop11_korean_air_asiana_consolidation | Reuters merger / fleet / integration anchors | Korean Air acquired 63.88% Asiana stake for about $1.3B; combined LCC fleet around 58 aircraft | price_data_unavailable_after_deep_search |
| r9_loop11_kumho_tire_gwangju_factory_fire_hard_4c | Reuters fire / production / event-return anchors | Gwangju plant 12M tires/year and nearly 20% of global capacity; production suspended | reported_event_anchor_not_full_ohlc |
| r9_loop11_daejeon_auto_parts_supplier_fire_sector_hard_4c | Reuters workplace-safety / supplier anchor | 14 deaths, 60 injuries, 25 serious injuries; Anjun supplies Hyundai/Kia | sector_hard_4c_direct_listed_mapping_unavailable |
| r9_loop11_pan_ocean_shipping_freight_cycle | WSJ Market Talk / Reuters freight-cycle anchors | target upside +45.2%, OP forecast +39%, but rate normalization can cut freight rates 20-25% | reported_price_anchor_not_full_ohlc |
| r9_loop11_lotte_tour_yellow_balloon_tourism_redirect | Reuters tourism policy / redirect event anchors | China visa-free group tourism and cruise reroute drove basket rally before spend/OPM proof | reported_event_anchor_not_full_ohlc |
