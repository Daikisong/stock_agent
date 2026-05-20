# Round 280 R11 Price Validation Plan

- price_validation_completed: partial_with_reported_price_anchors
- full_adjusted_ohlc_complete: false
- Do not invent OHLC, stage prices, policy execution, tariff margin, licences, labor continuity, disaster losses, or FX stabilization where raw data are unavailable.

## Backfill Fields

- price_data_source
- full_adjusted_ohlc_complete
- reported_event_return_anchor
- index_anchor
- fx_anchor
- policy_amount_anchor
- supply_chain_license_anchor
- labor_anchor
- disaster_loss_anchor
- stage2_price_anchor
- stage3_price
- stage4b_price
- stage4c_price
- event_mfe_pct
- event_mae_pct
- price_validation_status

## Case Anchors

| case | data source | reported anchor | status |
|---|---|---|---|
| r11_loop13_martial_law_korea_discount_political_shock | Reuters martial-law political-shock anchors | Political shock immediately repriced KOSPI/won risk premium | reported_index_fx_anchor_not_full_ohlc |
| r11_loop13_iran_middle_east_energy_fx_macro_hard_4c | Reuters Iran conflict macro-market anchors | Samsung -11.7%, SK Hynix -9.6%, Hyundai -15.8%, Korean Air -7.9% | reported_event_anchor_not_full_ohlc |
| r11_loop13_ai_bonus_fiscal_redistribution_event | FT / Barron's / MarketWatch AI bonus policy-reaction anchors | Policy comment moved market before legislation or direct corporate-profit seizure proof | reported_event_anchor_not_full_ohlc |
| r11_loop13_samsung_strike_emergency_arbitration_supply_chain | Reuters Samsung strike / government intervention anchors | One-day semiconductor halt risk up to 1T KRW direct loss; wider damage up to 100T KRW | reported_event_anchor_not_full_ohlc |
| r11_loop13_china_rare_earth_export_control_supply_chain | Reuters rare-earth export-control and Korea trade-envoy anchors | Defence users denied licences; advanced semiconductor applications reviewed case-by-case | supply_chain_policy_anchor_not_full_ohlc |
| r11_loop13_us_korea_tariff_auto_semis_pharma_policy | Reuters U.S.-Korea tariff trade-deal anchors | 15% lower than 25%, but FTA advantage versus Japan was removed | reported_event_anchor_not_full_ohlc |
| r11_loop13_samsung_sk_china_fab_tool_license_relief | Reuters U.S. approval for Samsung/SK Hynix China tool shipments | Annual licence is relief after waiver revocation, not durable Green | price_data_unavailable_after_deep_search |
| r11_loop13_2025_south_korea_wildfires_disaster_reference | Reuters climate-attribution wildfire report + AP early disaster anchor | Disaster cost reference; listed stock price anchor unavailable | disaster_reference_not_full_ohlc |
