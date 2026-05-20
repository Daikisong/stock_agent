# Round 266 R10 Price Validation Plan

- price_validation_completed: partial_with_reported_price_anchors
- full_adjusted_ohlc_complete: false
- hard_4c_confirmed: true_for_safety_reference
- direct_listed_hard_4c_confirmed: false
- Do not invent OHLC, peak, MFE, MAE, margin, working capital, cash collection, presales, PF, contract award, or legal clearance.

## Backfill Fields

- price_data_source
- full_adjusted_ohlc_available
- reported_price_anchor
- reported_return_anchor
- stage1_price
- stage2_price
- stage3_price
- stage4b_price
- stage4c_price
- event_mfe_1d
- event_mae_1d
- reported_3m_mfe
- project_value_or_capacity_anchor
- safety_or_regulatory_anchor
- policy_or_ltv_anchor
- materials_demand_anchor
- price_validation_status

## Case Anchors

| case | data source | reported anchor | status |
|---|---|---|---|
| r10_loop12_czech_nuclear_preferred_bid_legal_watch | Reuters / AP project and reported equity-return anchors | Two-unit implied project value about $17.3B; later legal context around $18B contract halt | reported_return_anchor_not_full_ohlc |
| r10_loop12_hyundai_ec_bulgaria_kozloduy_talks | Reuters Bulgaria nuclear talks anchor | Two reactors, 2,300MW added capacity, Unit 7 target 2033, Hyundai outbid Bechtel | price_data_unavailable_after_deep_search |
| r10_loop12_hyundai_engineering_anseong_bridge_collapse | Reuters / AP / Washington Post construction-collapse anchors | Reuters at least 3 dead, AP 4 dead, 6 injured, five 50m support structures collapsed sequentially | unlisted_sector_reference |
| r10_loop12_posco_dl_recurring_fatal_accident_regulation | Reuters safety-regulation / company-response anchors | Up to 5% OP fine, license revocation risk, 589 workplace deaths in 2024, about 80 DL executives resigned | price_data_unavailable_after_deep_search |
| r10_loop12_seoul_housing_ltv_supply_policy | Reuters housing-policy anchor | Gangnam/Yongsan LTV 50% to 40%, state-owned land and reconstruction simplification | price_data_unavailable_after_deep_search |
| r10_loop12_sejong_presidential_office_public_infra | Reuters public-infrastructure policy anchor | 350,000 sqm site, 9.8B won preparation cost, 14-month construction period, start target August 2027 | price_data_unavailable_after_deep_search |
| r10_loop12_daewoo_ec_nghi_son_lng_candidate | Reuters Vietnam LNG power project anchor | $2.5B project, 1.5GW capacity, commercial operation target 2030, Daewoo named as possible consortium participant | price_data_unavailable_after_deep_search |
| r10_loop12_hyundai_steel_rebar_construction_demand_break | MarketWatch / Dow Jones Market Talk price and estimate anchor | 2024 net-profit forecast cut 73% to 215B won; rebar price expected -10% | reported_price_anchor_not_full_ohlc |
