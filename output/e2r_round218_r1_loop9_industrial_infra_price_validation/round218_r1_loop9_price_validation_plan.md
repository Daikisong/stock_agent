# Round 218 R1 Price Validation Plan

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
- target_price
- target_upside_pct
- reported_mfe_pct
- mfe_1d
- mae_1d
- event_mae_pct
- relative_outperformance_pp
- contract_value_usd_bn
- policy_contract_value
- ipo_first_day_return_pct
- price_validation_status

## Case Anchors

| case | data source | reported anchor | status |
|---|---|---|---|
| r1_loop9_ls_electric_us_grid_watch | MarketWatch reported price and target anchors | event price -5.4%; target upside +34.3%; target raise +86.7% | reported_price_anchor_not_full_ohlc |
| r1_loop9_k_transformer_bottleneck_basket | Reuters sector evidence and public company profile anchors | GSU demand +274%; substation demand +116%; transformer prices +80%; lead time up to 4 years | price_data_unavailable_after_deep_search |
| r1_loop9_samsung_ea_fadhili_epc | WSJ/Reuters reported contract and price anchors | +8.5% event move; KOSPI relative outperformance +9.9pp; KB target 35,000 KRW | reported_price_anchor_not_full_ohlc |
| r1_loop9_doosan_czech_nuclear_policy_to_contract | Reuters/AP reported policy, contract, and return anchors | reported 3M +48%; signed 407B koruna / $18.7B contract | reported_return_anchor_not_full_ohlc |
| r1_loop9_hd_hyundai_heavy_mipo_masga_event | Reuters reported event return anchors | HD Hyundai Heavy +11.3%; HD Hyundai Mipo +14.6%; record highs | reported_event_return_not_full_ohlc |
| r1_loop9_hanwha_ocean_china_sanction_watch | Reuters/AP reported sanction and price anchors | China sanctions five U.S.-linked subsidiaries; Philly Shipyard $100M; U.S. investment $5B | reported_event_return_not_full_ohlc |
| r1_loop9_hd_hyundai_marine_solution_ipo_premium | WSJ/Reuters Breakingviews IPO anchors | +96.5% first-day close; market cap +98.5% | reported_price_anchor_not_stage3 |
