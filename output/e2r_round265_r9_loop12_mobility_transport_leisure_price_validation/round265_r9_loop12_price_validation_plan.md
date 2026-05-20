# Round 265 R9 Price Validation Plan

- price_validation_completed: partial_with_reported_price_anchors
- full_adjusted_ohlc_complete: false
- hard_4c_confirmed: true
- Do not invent OHLC, peak, MFE, MAE, stage prices, route yield, load factor, tourism spend, margin, FCF, security costs, or compensation liabilities.

## Backfill Fields

- price_data_source
- full_adjusted_ohlc_available
- reported_price_anchor
- reported_event_return
- stage1_price
- stage2_price
- stage3_price
- stage4b_price
- stage4c_price
- event_mfe_1d
- event_mae_1d
- event_close_return
- relative_underperformance_pp
- safety_or_investigation_anchor
- route_yield_load_factor_anchor
- component_asp_or_transaction_anchor
- shipping_security_or_freight_anchor
- tourism_spend_or_redirect_anchor
- price_validation_status

## Case Anchors

| case | data source | reported anchor | status |
|---|---|---|---|
| r9_loop12_jeju_air_muan_crash_hard_4c | Reuters crash / event-return / probe anchors | AK Holdings -12%, HanaTour -7%, Very Good Tour -11%; later independent probe bill | reported_event_anchor_not_full_ohlc |
| r9_loop12_air_busan_plane_fire_4c_watch | Reuters aircraft-fire event-return anchor | T'way +9%, Jeju Air -0.8%, Korean Air and Asiana flat in same context | reported_event_anchor_not_full_ohlc |
| r9_loop12_tway_eu_route_remedy | Reuters route-remedy operational anchor | Four European routes, 5 A330-200, 100 pilots, management +30-40% growth expectation | price_data_unavailable_after_deep_search |
| r9_loop12_hl_mando_hybrid_erev_component_asp | WSJ / MarketWatch Market Talk price and component-ASP anchor | IDB ASP +70%, SDC ASP +50%, target upside +16.9% from event price | reported_event_anchor_not_full_ohlc |
| r9_loop12_hyundai_mobis_lighting_divestiture | Reuters OPmobility / Hyundai Mobis lighting transaction anchors | Mobis lighting business estimated >1B EUR annual revenue; OPmobility 2025 margin 4.8% vs 4.2% | hyundai_mobis_price_data_unavailable_after_deep_search |
| r9_loop12_hmm_namu_hormuz_shipping_security | Reuters HMM Namu attack / Hormuz policy-response anchors | HMM-operated cargo ship attacked near Hormuz; engine-room fire and Dubai forensic inspection | price_data_unavailable_after_deep_search |
| r9_loop12_hmm_panocean_freight_normalization_watch | Reuters Maersk/Hapag global shipping-cycle anchors | Maersk 2026 EBITDA guide $4.5B-$7B vs $9.53B in 2025; Hapag EBIT -60.7% | korean_shipping_ohlc_unavailable_after_deep_search |
| r9_loop12_lotte_yellowballoon_tourism_redirect | Reuters tourism visa-free / China-Japan dispute / cruise rerouting anchors | Adora Magic City Jeju stay extended to 31-57 hours vs usual 9 hours before spend conversion proof | reported_event_anchor_not_full_ohlc |
