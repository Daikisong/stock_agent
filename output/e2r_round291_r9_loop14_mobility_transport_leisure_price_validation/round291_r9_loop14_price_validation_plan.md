# Round 291 R9 Price Validation Plan

- price_validation_completed: partial_with_reported_price_anchors
- full_adjusted_ohlc_complete: false
- Do not invent OHLC, stage prices, tariff pass-through, margin, route recovery, yield, safety trust, spend conversion, freight durability, OP/FCF or ROIC where raw data are unavailable.

## Backfill Fields

- price_data_source
- full_adjusted_ohlc_complete
- reported_event_return_anchor
- reported_event_price_anchor
- operating_profit_anchor
- tariff_cost_anchor
- deal_value_anchor
- passenger_freight_capacity_anchor
- visitor_data_anchor
- market_cap_wipeout_anchor
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
| r9_loop14_hyundai_kia_us_tariff_hybrid_mix | Reuters auto-tariff deal and Hyundai Q3 earnings anchors | Hyundai -4.5%, Kia -6.6% on tariff deal; later Hyundai +2.7% on Q3 relief/mix | reported_event_anchor_not_full_ohlc |
| r9_loop14_hyundai_glovis_middle_east_logistics_4c_watch | Reuters Hyundai export disruption and Q1 earnings anchors | Hyundai -1.2%, Hyundai Glovis -0.7% while KOSPI +2.7%; Q1 OP -31% | reported_event_anchor_not_full_ohlc |
| r9_loop14_korean_air_asiana_integration_stage2 | Reuters Korean Air-Asiana completion and 2024 annual earnings anchors | Direct event return unavailable; integration and 2024 earnings anchors used | price_data_unavailable_after_deep_search |
| r9_loop14_tway_air_incheon_airline_remedy_stage2 | Reuters T'way Europe-route remedy and Air Incheon cargo-sale anchors | Direct event return unavailable; route/cargo remedy assets used as Stage 2 anchors | price_data_unavailable_after_deep_search |
| r9_loop14_jeju_air_safety_hard_4c | Reuters Jeju Air crash event-price anchor | Jeju Air -15.7% intraday; -8.5% mid-session; AK Holdings -12% | reported_event_anchor_not_full_ohlc |
| r9_loop14_hyundai_india_ipo_failed_rerating | Reuters Hyundai Motor India IPO debut and Q2 earnings anchors | Debut down as much as -6%; Q2 profit -16.5%, domestic sales -6%, exports -17% | reported_ipo_anchor_not_full_ohlc |
| r9_loop14_china_tourism_leisure_basket | Reuters China group-tourist visa-free and leisure-stock reaction anchors | Hyundai Department Store +7.1%, Hotel Shilla +4.8%, Paradise +2.9%, Hankook Cosmetics +9.9% | reported_event_anchor_not_full_ohlc |
| r9_loop14_hmm_red_sea_freight_rate_event_premium | Reuters Hapag-Lloyd / Maersk Red Sea freight-rate cycle anchors | Freightos spot index +40% in six weeks; Maersk -2% on Suez/Red Sea normalization expectations | reported_event_anchor_not_full_ohlc |
| r9_loop14_korea_used_car_export_logistics_shock | Reuters used-car export logistics shock anchor | Listed direct price unavailable; route/destination logistics reference used | price_data_unavailable_after_deep_search |
