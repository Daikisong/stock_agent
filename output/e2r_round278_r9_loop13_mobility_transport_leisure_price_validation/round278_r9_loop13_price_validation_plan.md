# Round 278 R9 Price Validation Plan

- price_validation_completed: partial_with_reported_price_anchors
- full_adjusted_ohlc_complete: false
- Do not invent OHLC, stage prices, margin, booking, freight durability, safety remediation, ROI or FCF where raw data are unavailable.

## Backfill Fields

- price_data_source
- full_adjusted_ohlc_complete
- reported_event_return_anchor
- deal_or_policy_value_anchor
- stage2_price_anchor
- stage3_price
- stage4b_price
- stage4c_price
- event_mfe_pct
- event_mae_pct
- tariff_margin_anchor
- safety_trust_anchor
- freight_or_booking_anchor
- price_validation_status

## Case Anchors

| case | data source | reported anchor | status |
|---|---|---|---|
| r9_loop13_hyundai_motor_hybrid_shareholder_return_tariff_watch | Reuters Hyundai investor-day / domestic investment / Q1 tariff anchors | Hybrid/shareholder-return event worked, but tariff margin remains open | reported_event_anchor_not_full_ohlc |
| r9_loop13_kia_us_tariff_margin_break | Reuters Kia Q2 tariff anchor | US sales +5% failed to offset tariff margin hit | reported_event_anchor_not_full_ohlc |
| r9_loop13_hyundai_motor_india_ipo_capital_recycling | Reuters Hyundai India IPO and debut anchors | India IPO was capital recycling, but failed debut blocks parent Green | reported_ipo_anchor_not_full_ohlc |
| r9_loop13_korean_air_asiana_consolidation_fleet_capex_watch | Reuters Korean Air-Asiana acquisition / branding / Boeing order anchors | Consolidation is Stage 2; fleet capex ROI and integration remain gates | price_data_unavailable_after_deep_search |
| r9_loop13_jeju_air_fatal_crash_aviation_safety_hard_4c | Reuters Jeju Air crash and event-price anchor | Fatal crash and emergency safety inspection confirm hard 4C | reported_event_anchor_not_full_ohlc |
| r9_loop13_hyundai_mobis_lighting_portfolio_recycling | Reuters OPmobility / Hyundai Mobis lighting business anchor | Deal value and proceeds use are not disclosed | reported_event_anchor_not_full_ohlc |
| r9_loop13_hmm_pan_ocean_red_sea_freight_cycle_watch | MarketWatch Korean shipping event anchors + Reuters Red Sea/Suez reopening risk anchors | Freight rally is cyclical until contract durability is proven | reported_event_anchor_not_full_ohlc |
| r9_loop13_china_tourism_leisure_event_premium | Reuters China visa-free and China-Japan tourism rerouting anchors | Policy/reroute event premium; booking, occupancy, ADR and margin are required | reported_event_anchor_not_full_ohlc |
