# Round 263 R7 Price Validation Plan

- price_validation_completed: partial_with_reported_price_anchors
- full_ohlc_complete: false
- Do not invent OHLC, stage prices, procedure volume, installed base, consumable attach-rate, provider adoption, reimbursement, FCF, or safety resolution where raw data are unavailable.

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
- transaction_or_market_value_anchor
- procedure_volume_or_exam_count
- installed_base_or_export_channel_anchor
- regulatory_safety_or_policy_gate
- price_validation_status

## Case Anchors

| case | data source | reported anchor | status |
|---|---|---|---|
| r7_loop12_jeisys_medical_ebd_global_buyout | WSJ ArchiMed / Jeisys acquisition anchor | Business quality validated, but public post-event OHLC is unsuitable after delisting | reported_transaction_anchor_delisting_no_full_ohlc |
| r7_loop12_apr_medicube_device_crossover | FT APR / beauty-device anchor | MFE from January 2025 greater than +300%; no full adjusted OHLC in this pass | reported_return_anchor_not_full_ohlc |
| r7_loop12_classys_aesthetic_device_export_platform | public company profile / secondary summary | Business/export anchor confirmed, but reliable event return or full OHLC unavailable | price_data_unavailable_after_deep_search |
| r7_loop12_hugel_letybo_us_toxin_launch | Allure / NY Post U.S. launch and price anchors | Launch Stage 2; Hugel stock OHLC unavailable in this pass | price_data_unavailable_after_deep_search |
| r7_loop12_medytox_innotox_unauthorized_distribution | Guardian / People safety-regulatory anchors | Safety-trust 4C-watch; no reliable Medytox event OHLC in this pass | price_data_unavailable_after_deep_search |
| r7_loop12_lunit_insight_dbt_validation_not_revenue | arXiv external-validation evidence | Medical AI validation, not Green; price path unavailable | price_data_unavailable_after_deep_search |
| r7_loop12_medical_quota_doctors_strike_disruption | Reuters / AP medical-crisis policy anchors | Policy disruption/relief; listed healthcare stock OHLC unavailable | price_data_unavailable_after_deep_search |
| r7_loop12_osstem_zimvie_dental_mna_event | Investors.com / Bloomberg-reported takeover rumor anchor | M&A event premium, not Korean listed Green | reported_target_event_anchor_delisted_buyer_no_ohlc |
