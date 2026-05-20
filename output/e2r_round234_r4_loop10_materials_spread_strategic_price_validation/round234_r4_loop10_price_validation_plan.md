# Round 234 R4 Price Validation Plan

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
- share_issue_vs_project_value_pct
- contract_value_drawdown_pct
- rumor_duration_days
- price_validation_status

## Case Anchors

| case | data source | reported anchor | status |
|---|---|---|---|
| r4_loop10_korea_zinc_strategic_minerals_governance | Reuters critical-minerals / governance event anchors | $7.4B project, 540k tons output, 11 critical minerals, 2025 OP 1.2T KRW | reported_event_anchor_not_full_ohlc |
| r4_loop10_lotte_hd_petrochemical_restructuring | Reuters restructuring evidence | Daesan NCC 1.1M tpy shut for 3 years; support >2T KRW; capital increase 1.2T KRW | price_data_unavailable_after_deep_search |
| r4_loop10_sk_innovation_soil_refining_cycle | Reuters refining-cycle financial and price anchors | Q1 2026 OP 2.2T KRW vs 1.4T estimate; but battery drag persists | reported_event_anchor_not_full_ohlc |
| r4_loop10_posco_minres_lithium_jv | Reuters lithium transaction / commodity anchors | $765M transaction, indirect 15% Wodgina/Mt Marion, spodumene still -85%+ vs peak | posco_stock_ohlc_unavailable_after_deep_search |
| r4_loop10_hyundai_steel_policy_capex_rebar_4c | Reuters / MarketWatch capex and weak-demand anchors | $5.8B-$6.0B Louisiana plant, 2.7M tpy capacity, NP forecast -73% | reported_event_anchor_not_full_ohlc |
| r4_loop10_lnf_tesla_cathode_contract_hard_4c | Reuters contract-value collapse anchor | Tesla cathode deal value collapsed by about -99.999745% | reported_contract_anchor_not_full_ohlc |
| r4_loop10_oci_non_china_polysilicon_spacex_watch | FT / Reuters capacity and media-report anchors | $1.2B Texas expansion to 10GW by 2027; SpaceX report unconfirmed | price_data_unavailable_after_deep_search |
| r4_loop10_poongsan_hanwha_mna_rumor_fade | Reuters M&A report / termination anchors | reported 1.5T KRW / $1.1B M&A rumor dropped after 6 calendar days | price_data_unavailable_after_deep_search |
