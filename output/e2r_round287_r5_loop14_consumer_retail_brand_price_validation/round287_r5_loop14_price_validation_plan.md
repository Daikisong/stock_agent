# Round 287 R5 Price Validation Plan

- price_validation_completed: partial_with_reported_price_anchors
- full_adjusted_ohlc_complete: false
- Do not invent OHLC, full MFE/MAE, sell-through, tariff absorption, take-rate, unit economics, data trust, spend conversion, or stage dates where raw data are unavailable.

## Backfill Fields

- price_data_source
- full_adjusted_ohlc_complete
- reported_event_return_anchor
- reported_event_price_anchor
- target_price_anchor
- op_estimate_anchor
- sales_export_anchor
- user_spend_anchor
- policy_period_anchor
- data_trust_anchor
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
| r5_loop14_samyang_buldak_export_stage3_candidate | MarketWatch/Dow Jones event anchor + AP Denmark recall anchor | OP estimate +84% YoY, target price +26%, target upside 28.3% | reported_event_anchor_not_full_ohlc |
| r5_loop14_nongshim_shin_ramyun_global_expansion | FT brand/export anchor | Shin Ramyun sales 1.2T KRW; overseas share nearly 60%; U.S. sales target 1.5B USD by 2030 | price_data_unavailable_after_deep_search |
| r5_loop14_apr_medicube_beauty_device_brand_4b | FT reported valuation and stock-pop anchors | Stock +75% since IPO in July context and more than 4x since January context | reported_valuation_anchor_not_full_ohlc |
| r5_loop14_kbeauty_us_expansion_basket | Reuters/AP K-beauty export and tariff anchors | Top-five Korean U.S. e-commerce growth 71% over two years; U.S. market 21%; French top-five 15% | reported_growth_anchor_not_full_ohlc |
| r5_loop14_china_tourism_retail_event_premium | reported tourism policy basket event-return anchors | Visitor-count and visa headline moved basket, but spend/conversion/margin were not confirmed | reported_event_anchor_not_full_ohlc |
| r5_loop14_shinsegae_emart_alibaba_gmarket_jv_data_gate | reported JV, KFTC and cross-border market anchors | Expected cross-border market share 41%; data sharing restricted for three years | reported_JV_anchor_not_full_ohlc |
| r5_loop14_coupang_data_breach_retail_trust_hard_reference | reported breach, spending and competitor read-through anchors | Naver users +23% and CJ Logistics volume +120% are read-through, not automatic Green | reported_breach_anchor_not_full_ohlc |
| r5_loop14_cj_logistics_shinsegae_fulfillment_unit_economics | reported target-price and event-price anchors | Annual revenue uplift 300B KRW, but event return -0.2% | reported_event_anchor_not_full_ohlc |
| r5_loop14_domestic_retail_sales_shock_4c_watch | reported macro and retail-sales anchors | Dec retail sales -0.6% MoM; cars/home appliances -4.1%; entertainment -0.6%; Q4 GDP 0.1% | macro_anchor_not_stock_ohlc |
