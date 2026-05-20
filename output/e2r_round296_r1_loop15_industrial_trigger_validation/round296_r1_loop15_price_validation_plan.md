# Round 296 R1 Price Validation Plan

- price_validation_completed: partial_with_reported_event_price_anchors
- full_adjusted_ohlc_complete: false
- Stage candidates are not downgraded merely because full OHLC is missing.
- Do not invent 30D/90D/180D/1Y MFE/MAE, delivery margin, cash collection, legal clearance, or final contract data.

## Case Anchors

| case | data source | reported anchor | status |
|---|---|---|---|
| r1_loop15_hyundai_rotem_k2_poland | WSJ Hyundai Rotem event price and estimate anchor; Reuters Poland second contract confirmation | +9.3% vs KOSPI -0.3%, relative +9.6pp | reported_event_anchor_not_full_ohlc |
| r1_loop15_lig_nex1_msam | MarketWatch downgrade anchor, Reuters Iraq order anchor, FT combat-validation anchor | Iraq order +3.6% vs KOSPI +0.9%; earlier 4B -11% | reported_event_anchor_not_full_ohlc |
| r1_loop15_hanwha_aerospace_k9_backlog_dilution | Reuters Romania order/backlog anchor and FT share-sale dilution anchor | Romania order +5%; later share-sale event -13% | reported_event_anchor_not_full_ohlc |
| r1_loop15_shipbuilding_order_price_basket | WSJ shipbuilding order/share-price/newbuilding price anchor and Reuters HD HHI/Mipo merger anchor | Samsung Heavy +16%, Hanwha Ocean +13%, HD HHI +11%; later HD HHI +11.3%, HD Mipo +14.6% | reported_event_anchor_not_full_ohlc |
| r1_loop15_ls_electric_us_grid | MarketWatch LS Electric target/revenue mix anchor and Reuters U.S. transformer shortage anchor | target +87% but same-day price -5.4% | reported_event_anchor_not_full_ohlc |
| r1_loop15_samsung_ena_fadhili | WSJ Samsung E&A Fadhili order event price anchor | +8.5% vs KOSPI -1.4%, relative +9.9pp | reported_event_anchor_not_full_ohlc |
| r1_loop15_czech_nuclear_doosan | Reuters Czech nuclear preferred-bidder and legal challenge anchors | pre-priced preferred bidder event; at least $18B contract signing later blocked by court | reported_event_anchor_not_full_ohlc |
