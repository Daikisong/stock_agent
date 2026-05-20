# Round 284 R2 Price Validation Plan

- price_validation_completed: partial_with_reported_price_anchors
- full_adjusted_ohlc_complete: false
- Do not invent OHLC, stage prices, full MFE/MAE, HBM shipment, ASP/mix, PO, sell-through, utilization, binding OpenAI terms, or labor-continuity evidence where raw data are unavailable.

## Backfill Fields

- price_data_source
- full_adjusted_ohlc_complete
- reported_event_return_anchor
- reported_price_anchor
- earnings_anchor
- target_price_anchor
- deal_funding_capex_anchor
- market_share_anchor
- strike_export_control_risk_anchor
- stage1_price
- stage2_price
- stage3_price
- stage4b_price
- stage4c_price
- event_mfe_pct
- event_mae_pct
- price_validation_status

## Case Anchors

| case | data source | reported anchor | status |
|---|---|---|---|
| r2_loop14_sk_hynix_hbm_dominance_stage3_4b | WSJ chip-rally anchor + Reuters earnings/market-cap anchors | HBM success is real, but valuation/crowding 4B-watch must trigger after extreme rerating. | reported_event_anchor_not_full_ohlc |
| r2_loop14_samsung_hbm_catchup_labor_4c_watch | Reuters Samsung HBM/export restriction, KOSPI 7000 and strike anchors | Samsung catch-up has Stage 2 evidence, but China, qualification and labor gates remain hard watches. | reported_event_anchor_not_full_ohlc |
| r2_loop14_hanmi_tc_bonder_hbm_equipment_4b | WSJ Hanmi HBM equipment and Micron-rumor event anchors | Actual SK Hynix contract supports Stage 2; Micron rumor is 4B-watch. | reported_event_anchor_not_full_ohlc |
| r2_loop14_lg_innotek_ai_iphone_component_price_failed | MarketWatch/Dow Jones LG Innotek event anchor | Good estimate evidence did not validate price; sell-through and component margin required. | reported_event_anchor_not_full_ohlc |
| r2_loop14_lg_display_oled_restructuring_stage2 | Reuters LCD sale and OLED capex anchors | LCD exit/OLED capex supports Stage 2; utilization and FCF required. | direct_event_return_unavailable_after_deep_search |
| r2_loop14_rebellions_sapeon_korean_ai_chip_stage2 | Reuters Rebellions-Sapeon merger anchors | Korean AI chip merger is Stage 2, but listed EPS bridge is absent. | price_data_unavailable_after_deep_search |
| r2_loop14_samsung_sk_openai_stargate_memory_mou_4b | FT OpenAI Stargate LOI price-reaction anchor | LOI is demand signal, not binding call-off/margin Green. | reported_event_anchor_not_full_ohlc |
| r2_loop14_lg_electronics_component_cost_4c_watch | WSJ LG Electronics earnings anchor | Memory shortage can pressure OEM margins; B2B/cooling optionality is not enough. | price_data_unavailable_after_deep_search |
