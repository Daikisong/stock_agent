# Round 221 R4 Price Validation Plan

- price_validation_completed: partial_with_reported_price_anchors
- full_ohlc_complete: false
- Do not invent OHLC, stage prices, spreads, offtake, MFE, or MAE where raw adjusted daily prices are unavailable.

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
- mfe_1d
- mae_1d
- mae_1d_secondary
- relative_underperformance_pp
- commodity_drawdown_pct
- commodity_rebound_pct
- share_issuance_vs_project_value_pct
- rumor_duration_days
- price_validation_status

## Case Anchors

| case | data source | reported anchor | status |
|---|---|---|---|
| r4_loop9_posco_hyundai_steel_tariff_watch | Reuters/WSJ reported event-return anchors | POSCO -3.6%; Hyundai Steel -2.9%; later 50% tariff threat: Hyundai Steel -5.1%, POSCO -3.2% | reported_event_anchor_not_full_ohlc |
| r4_loop9_korea_zinc_strategic_governance | FT/Reuters reported event anchors | U.S. smelter +27%; injunction -13%; court rejection +5%; YoungPoong -10.5% | reported_event_anchor_not_full_ohlc |
| r4_loop9_lotte_hd_petrochemical_restructuring | Reuters restructuring evidence | Daesan NCC 1.1M tpy shut for 3 years; support >2T KRW; capital increase 1.2T KRW | price_data_unavailable_after_deep_search |
| r4_loop9_sk_innovation_soil_refining_cycle | Reuters reported financial/event anchors | Q4 OP 295B KRW, forecast miss -16%; Q1 2026 OP 2.2T KRW, +57.1% beat | reported_event_anchor_not_full_ohlc |
| r4_loop9_posco_minres_lithium_jv | Reuters commodity/transaction anchors | MinRes +10.8%; spodumene >$6,000/t to ~$610/t then ~$880/t | posco_stock_ohlc_unavailable_after_deep_search |
| r4_loop9_oci_non_china_polysilicon | FT/Reuters evidence anchors | $1.2B Texas expansion, 10GW by 2027; SpaceX report unconfirmed | price_data_unavailable_after_deep_search |
| r4_loop9_poongsan_hanwha_mna_rumor_fade | Reuters M&A report/termination anchors | reported 1.5T KRW M&A rumor dropped after 6 calendar days | price_data_unavailable_after_deep_search |
