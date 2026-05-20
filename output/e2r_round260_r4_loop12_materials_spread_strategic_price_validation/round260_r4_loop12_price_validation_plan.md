# Round 260 R4 Price Validation Plan

- price_validation_completed: partial_with_reported_price_anchors
- full_ohlc_complete: false
- Do not invent OHLC, stage prices, spreads, offtakes, MFE, MAE, margin, or FCF where raw adjusted daily prices are unavailable.

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
- project_or_policy_anchor
- spread_capacity_or_import_anchor
- dilution_or_credit_anchor
- tariff_or_export_control_anchor
- price_validation_status

## Case Anchors

| case | data source | reported anchor | status |
|---|---|---|---|
| r4_loop12_poongsan_defense_metals_mna_rumor | Reuters M&A rumor / denial anchors | Full adjusted OHLC unavailable; rumor-driven optionality only | price_data_unavailable_after_deep_search |
| r4_loop12_korea_zinc_critical_minerals_dilution_watch | Reuters critical-minerals / share-issuance anchors | Full adjusted OHLC unavailable; project quality high but offtake/FCF not closed | price_data_unavailable_after_deep_search |
| r4_loop12_china_rare_earth_end_use_restriction_overlay | Reuters rare-earth export-control report | China reportedly asked Korean firms not to export Chinese rare-earth-containing products to U.S. defense firms | sector_overlay_no_company_ohlc |
| r4_loop12_posco_hyundai_seah_steel_tariff_two_sided | Reuters steel tariff / event-return anchors | Domestic anti-dumping relief and U.S. export tariff risk point in opposite directions | reported_event_anchor_not_full_ohlc |
| r4_loop12_hyundai_steel_us_capex_false_positive | Reuters U.S. steel plant / investor backlash / capital-increase anchors | $5.8B Louisiana plant; later funding clarified as $2.9B equity + $2.9B external borrowing | reported_event_anchor_not_full_ohlc |
| r4_loop12_lgchem_hanwha_dl_yncc_petrochemical_credit_watch | Reuters petrochemical overhaul / restructuring-plan anchors | YNCC debt-to-equity 249%; one or two crackers may shut; No.3 cracker already shut | price_data_unavailable_after_deep_search |
| r4_loop12_lotte_hd_hyundai_chemical_restructuring_relief | Reuters first petrochemical restructuring approval anchors | Support package is relief; spread/OPM/FCF not yet confirmed | price_data_unavailable_after_deep_search |
| r4_loop12_korea_critical_minerals_policy_relief | Reuters critical-minerals policy anchor | Policy relief only; actual supply/offtake/margin not yet visible | policy_anchor_not_full_ohlc |
