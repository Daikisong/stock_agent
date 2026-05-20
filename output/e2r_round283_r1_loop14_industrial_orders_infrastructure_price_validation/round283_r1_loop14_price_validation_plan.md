# Round 283 R1 Price Validation Plan

- price_validation_completed: partial_with_reported_price_anchors
- full_adjusted_ohlc_complete: false
- Do not invent OHLC, stage prices, full MFE/MAE, order margin, local production execution, financing, shipment, IPO aftermarket demand, or backlog conversion where raw data are unavailable.

## Backfill Fields

- price_data_source
- full_adjusted_ohlc_complete
- reported_event_return_anchor
- contract_value_anchor
- cancellation_value_anchor
- dilution_amount_anchor
- IPO_price_anchor
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
| r1_loop14_hyundai_rotem_k2_poland_delivery_stage3_candidate | WSJ event price anchor; Reuters Poland second-contract anchor | Delivery/revenue/OP estimate and price reaction align, but local production and financing remain gates. | reported_event_anchor_not_full_ohlc |
| r1_loop14_ls_electric_us_grid_growth_price_failed | MarketWatch / Dow Jones event anchor | Good US growth evidence did not validate Green in price; backlog and margin required. | reported_event_anchor_not_full_ohlc |
| r1_loop14_hyosung_heavy_hico_transformer_capacity | Reuters Events industry-capacity anchor | Transformer shortage and capacity expansion are strong Stage 2 evidence, not Green alone. | price_data_unavailable_after_deep_search |
| r1_loop14_hd_hhi_mipo_merger_masga_4b | Reuters merger event anchor | Merger/MASGA event premium moved before actual US order and integration synergy. | reported_event_anchor_not_full_ohlc |
| r1_loop14_samsung_heavy_zvezda_cancellation_hard_4c | Reuters contract-cancellation anchor | Large backlog was cancelled; execution risk breaks the thesis. | contract_cancellation_value_anchor_not_full_ohlc |
| r1_loop14_hanwha_aerospace_share_sale_dilution | FT / Reuters share-sale and FSS revision anchors | Defense export cycle was capped by dilution and filing-quality gates. | reported_event_anchor_not_full_ohlc |
| r1_loop14_rainbow_robotics_samsung_stake_event | Reuters strategic-stake anchor | Samsung stake is strategic Stage 2, not shipment/margin Green. | price_data_unavailable_after_deep_search |
| r1_loop14_hd_hyundai_marine_ipo_overheat | WSJ / Reuters IPO debut anchors | Strong service business, but first-day doubling is 4B-watch until durability clears. | reported_ipo_anchor_not_full_ohlc |
