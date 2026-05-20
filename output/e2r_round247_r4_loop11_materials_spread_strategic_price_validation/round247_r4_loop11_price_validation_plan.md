# Round 247 R4 Price Validation Plan

- price_validation_completed: partial_with_reported_price_anchors
- full_ohlc_complete: false
- Do not invent OHLC, stage prices, spreads, offtake, MFE, or MAE where raw adjusted daily prices are unavailable.

## Backfill Fields

- price_data_source
- full_ohlc_available
- reported_price_anchor
- reported_return_anchor
- stage2_price_anchor
- stage3_price
- stage4b_price
- stage4c_price
- mfe_1d
- mae_1d
- mae_1d_secondary
- project_or_contract_value_anchor
- spread_or_capacity_anchor
- governance_or_tariff_anchor
- price_validation_status

## Case Anchors

| case | data source | reported anchor | status |
|---|---|---|---|
| r4_loop11_korea_zinc_critical_minerals_governance | Reuters critical-minerals / governance / share-issuance anchors | $7.4B project, 540k tons output, 11 critical minerals, 2025 OP 1.2T KRW | reported_event_anchor_not_full_ohlc |
| r4_loop11_lotte_hd_petrochemical_restructuring | Reuters restructuring evidence | Daesan NCC 1.1M tpy shut for 3 years; support >2T KRW; capital increase 1.2T KRW | price_data_unavailable_after_deep_search |
| r4_loop11_yncc_standalone_ncc_credit_watch | Reuters petrochemical overhaul / YNCC credit-risk anchor | debt/equity 249%, one or two cracker shutdown risk, No.3 cracker already shut | price_data_unavailable_after_deep_search |
| r4_loop11_hyundai_posco_steel_tariff_two_sided | Reuters / WSJ tariff-policy and event-return anchors | Korea anti-dumping 27.91%-38.02%; Chinese steel import share 49% | reported_event_anchor_not_full_ohlc |
| r4_loop11_lg_chem_toyota_cathode_derisking | Reuters ownership-structure anchor | Toyota Tsusho 25%; Huayou Cobalt stake 49% -> 24% | price_data_unavailable_after_deep_search |
| r4_loop11_posco_minres_lithium_resource_security | Reuters lithium transaction / commodity anchors | $765M transaction, indirect 15% Wodgina/Mt Marion, spodumene still -85%+ vs peak | posco_stock_ohlc_unavailable_after_deep_search |
| r4_loop11_oci_non_china_polysilicon_spacex_watch | FT / Reuters capacity and media-report anchors | $1.2B Texas expansion to 10GW by 2027; SpaceX report unconfirmed | price_data_unavailable_after_deep_search |
| r4_loop11_lnf_tesla_cathode_contract_hard_4c | Reuters contract-value collapse anchor | Tesla cathode deal value collapsed by about -99.999745% | reported_contract_anchor_not_full_ohlc |
