# Round 292 R10 Price Validation Plan

- price_validation_completed: partial_with_reported_price_anchors
- full_adjusted_ohlc_complete: false
- Do not invent OHLC, stage prices, PF repayment, presales, construction margins, safety remediation, final contracts, ASP/volume, capex IRR or FCF where raw data are unavailable.

## Backfill Fields

- price_data_source
- full_adjusted_ohlc_complete
- reported_event_return_anchor
- reported_event_price_anchor
- PF_delinquency_anchor
- support_package_anchor
- policy_LTV_anchor
- safety_event_fact_anchor
- order_value_anchor
- legal_challenge_anchor
- building_material_spread_anchor
- capex_funding_anchor
- stage2_price_anchor
- stage3_price
- stage4b_price
- stage4c_price
- event_mfe_pct
- event_mae_pct
- price_validation_status

## Case Anchors

| case | data source | reported anchor | status |
|---|---|---|---|
| r10_loop14_taeyoung_pf_liquidity_hard_watch | Reuters PF liquidity and restructuring anchors | Direct adjusted OHLC unavailable; PF delinquency and support-package anchors used | price_data_unavailable_after_deep_search |
| r10_loop14_seoul_property_policy_stage2_not_green | Reuters Seoul property-curb and BOK housing-risk anchors | Direct construction-stock anchor unavailable; policy and macro anchors used | price_data_unavailable_after_deep_search |
| r10_loop14_hdc_gwangju_construction_safety_hard_4c | Gwangju Hwajeong I-Park collapse public reference; adjusted OHLC unavailable | Direct adjusted OHLC unavailable; safety and quality facts used | price_data_unavailable_after_deep_search |
| r10_loop14_samsung_ena_fadhili_epc_order_4b | WSJ Samsung E&A Fadhili order event anchor | Samsung E&A +8.5% while KOSPI -1.4% | reported_event_anchor_not_full_ohlc |
| r10_loop14_czech_nuclear_construction_export_stage2 | Reuters Czech nuclear preferred-bidder and legal-challenge anchors | Doosan Enerbility +48%, KEPCO Plant S&E +14%, KEPCO E&C +41% over three months | reported_event_anchor_not_full_ohlc |
| r10_loop14_hyundai_steel_rebar_weak_construction_demand | MarketWatch/Dow Jones Hyundai Steel weak-demand anchor | Hyundai Steel -1.2% to 29,000 KRW | reported_event_anchor_not_full_ohlc |
| r10_loop14_hyundai_posco_steel_plate_antidumping_event | Reuters steel-plate anti-dumping event anchor | Hyundai Steel +5.8%, POSCO +3.9%, KOSPI -0.7% | reported_event_anchor_not_full_ohlc |
| r10_loop14_hyundai_steel_us_plant_capex_false_positive | Reuters Hyundai Steel U.S. plant investor backlash anchor | Hyundai Steel shares drop more than 21% after U.S. plant announcement | reported_event_anchor_not_full_ohlc |
