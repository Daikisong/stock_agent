# Round-206 R2 Loop-8 Price Validation Plan

## Required Fields

- `price_data_source`
- `full_ohlc_available`
- `reported_price_anchor`
- `reported_return_anchor`
- `stage2_price`
- `stage3_price`
- `stage4b_price`
- `stage4c_price`
- `peak_price`
- `reported_mfe_minimum_pct`
- `reported_market_cap_mfe_minimum_pct`
- `reported_compounded_return_minimum_pct`
- `mfe_1d`
- `mfe_1d_secondary`
- `mae_1d`
- `mae_1d_secondary`
- `price_validation_status`

## Case Anchors

| case | price data source | reported anchor | status |
| --- | --- | --- | --- |
| `r2_loop8_sk_hynix_hbm_aligned_4b` | MarketWatch/Reuters/Tom's Hardware reported anchors | +776.6% from stage3 anchor to reported peak; market cap minimum +842%; 2025 +274% and 2026 >+200% | `reported_price_anchor_not_full_ohlc` |
| `r2_loop8_hanmi_semiconductor_hbm_bonder_4b` | WSJ reported event return and intraday price anchor | +16% on confirmed SK Hynix order day; +22% on unconfirmed Micron report day | `reported_event_anchor_not_full_ohlc` |
| `r2_loop8_samsung_memory_recovery_hbm_watch` | Reuters/WSJ reported event return and close anchors | +3.5% OpenAI event close; Q3 profit event +2.9% intraday then -0.5% close | `stage2_watch_not_stage3` |
| `r2_loop8_gaonchips_pfn_design_win` | Reuters evidence source only | price data unavailable after deep search | `price_data_unavailable_after_deep_search` |
| `r2_loop8_db_hitek_policy_foundry` | Reuters evidence source only | price data unavailable after deep search | `price_data_unavailable_after_deep_search` |
| `r2_loop8_hana_micron_hanmi_export_control_watch` | Reuters reported event returns | export-control shock one-day reported returns | `reported_event_return_not_full_ohlc` |
| `r2_loop8_openai_stargate_memory_4b` | Reuters/FT/WSJ reported return and close price anchors | SK Hynix +12% intraday / about +10% close; Samsung +3.5% close to +4.7% reported | `reported_event_return_not_full_ohlc` |

## Backfill Rule

- Use reported Reuters/WSJ/FT/MarketWatch/Tom's Hardware anchors only for fields they explicitly support.
- Keep full OHLC unavailable until official or adjusted daily price backfill is done.
- Separate Stage 2 design/order evidence, Stage 3 HBM/EPS evidence, 4B crowding, and 4C-watch export-control events.
- Do not create a Stage 3 anchor when the case intentionally has no Stage 3 date.
