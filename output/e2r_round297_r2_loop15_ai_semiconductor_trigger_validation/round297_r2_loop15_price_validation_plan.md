# Round 297 R2 Price Validation Plan

- price_validation_completed: partial_with_reported_event_price_anchors
- full_adjusted_ohlc_complete: false
- Stage candidates are not downgraded merely because full OHLC is missing.
- Do not invent 30D/90D/180D/1Y MFE/MAE, customer allocation, sell-through, margin, or labor settlement data.

## Case Anchors

| case | data source | reported anchor | status |
|---|---|---|---|
| r2_loop15_sk_hynix_hbm_first_mover | WSJ/Reuters reported event returns and price anchors; no full adjusted OHLC window | T0 +4.3% vs KOSPI +0.7%; T2 +9% vs KOSPI +1.7%; 2025 +274%, 2026 +200%+ | reported_event_anchor_not_full_ohlc |
| r2_loop15_hanmi_semiconductor_hbm_equipment | WSJ reported event return and contract anchors | +16% vs KOSPI +0.7%, relative +15.3pp | reported_event_anchor_not_full_ohlc |
| r2_loop15_samsung_electronics_hbm_catchup_labor_watch | Reuters OpenAI/Nvidia/Samsung labor anchors | Samsung +4.7% while SK Hynix +12%; later Samsung +4%+ | reported_event_anchor_not_full_ohlc |
| r2_loop15_sk_hynix_openai_asml_4b | Reuters OpenAI, hyperscaler capex, ASML order and listing anchors | OpenAI +12%; hyperscaler capex +13% vs KOSPI +5.1%; ASML order +5.7% | reported_event_anchor_not_full_ohlc |
| r2_loop15_memory_china_equipment_export_control | Reuters export-control event anchor | Samsung -2.6%, SK Hynix -5% | reported_event_anchor_not_full_ohlc |
| r2_loop15_lg_innotek_apple_ai_upgrade | WSJ and MarketWatch LG Innotek event/estimate anchors | +19% vs KOSPI +0.4%; later estimate day -0.4% | reported_event_anchor_not_full_ohlc |
| r2_loop15_lg_display_apple_oled_recovery | Reuters LG Display result anchor; no event price anchor | loss beat and revenue +42%, but price unavailable | reported_event_anchor_not_full_ohlc |
| r2_loop15_samsung_labor_supply_chain_4c | Reuters Samsung labor strike risk anchor | strike risk without confirmed supply disruption | reported_event_anchor_not_full_ohlc |
