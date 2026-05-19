# Round 219 R2 Price Validation Plan

- price_validation_completed: partial_with_reported_price_anchors
- full_ohlc_complete: false
- Do not invent OHLC, stage prices, MFE, or MAE where raw adjusted daily prices are unavailable.

## Backfill Fields

- price_data_source
- full_ohlc_available
- reported_price_anchor
- reported_return_anchor
- stage2_price
- stage3_price
- stage4b_price
- stage4c_price
- peak_price
- reported_mfe_pct
- reported_market_cap_mfe_minimum_pct
- reported_compounded_return_minimum_pct
- hbm4_event_mfe_intraday_pct
- relative_outperformance_pp
- mfe_1d
- mfe_1d_secondary
- mae_1d
- mae_1d_secondary
- contract_value_krw_bn
- project_size_krw_trn
- price_validation_status

## Case Anchors

| case | data source | reported anchor | status |
|---|---|---|---|
| r2_loop9_sk_hynix_hbm4_stage3_4b | MarketWatch/Reuters reported price and return anchors | +551.8% from Stage 3 anchor to record close; 2025 +274%; 2026 >+200%; market cap <$100B to about $942B | reported_price_anchor_not_full_ohlc |
| r2_loop9_samsung_hbm_catchup_labor_watch | Reuters/AP reported event anchors | OpenAI +4.7%; Q3 OP 12.2T KRW; AI rally +14.4% vs KOSPI +6.45%; strike event -9.3% | reported_event_anchor_not_full_ohlc |
| r2_loop9_hanmi_hbm_bonder_confirmed_vs_rumor | WSJ reported price and contract anchors | +22% on unconfirmed Micron report; KOSPI -0.3%; relative +22.3pp | reported_event_anchor_not_full_ohlc |
| r2_loop9_gaonchips_pfn_design_win | Reuters evidence source only | price data unavailable after deep search | price_data_unavailable_after_deep_search |
| r2_loop9_db_hitek_policy_foundry | Reuters policy evidence source | price data unavailable after deep search | price_data_unavailable_after_deep_search |
| r2_loop9_openai_stargate_memory_4b | Reuters/Tom's Hardware reported anchors | OpenAI/Stargate event: SK Hynix +12%, Samsung +4.7%, KOSPI >+3%, DRAM wafer demand up to 900k/month | reported_event_anchor_not_full_ohlc |
| r2_loop9_export_control_china_fab_watch | Reuters reported event returns | export-control shock one-day reported returns; KOSPI -0.7% | reported_event_anchor_not_full_ohlc |
