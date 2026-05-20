# Round 250 R7 Price Validation Plan

- price_validation_completed: partial_with_reported_price_anchors
- full_ohlc_complete: false
- hard_4c_confirmed: false
- Do not invent OHLC, peak, MFE, MAE, stage prices, prescription volume, utilization, margin, FCF, or royalty values.

## Backfill Fields

- price_data_source
- full_ohlc_available
- reported_price_anchor
- reported_event_return
- stage2_price
- stage3_price
- stage4b_price
- stage4c_price
- mfe_1d
- mae_1d
- relative_underperformance_pp
- sales_base_or_peak_sales_expectation
- adoption_or_exam_count
- transaction_value_or_capacity
- trial_or_crl_status
- commercialization_gate_status
- price_validation_status

## Case Anchors

| case | data source | reported anchor | status |
|---|---|---|---|
| r7_loop11_alteogen_keytruda_sc_platform_royalty | Reuters / WSJ clinical-launch-patent anchors | Keytruda $30B product base and 30-40% SC adoption target, but no stage3 stock path | price_data_unavailable_after_deep_search |
| r7_loop11_yuhan_lazertinib_global_approval | Reuters approval and CRL anchors | FDA approval validates molecule, while SC Rybrevant CRL creates manufacturing-inspection watch | price_data_unavailable_after_deep_search |
| r7_loop11_samsung_biologics_gsk_facility_price_failed | Reuters policy, facility-acquisition and event-return anchors | Policy support day +6.23%; GSK facility event relative underperformance -2.4pp | reported_event_anchor_not_full_ohlc |
| r7_loop11_celltrion_us_tariff_hedge_factory | Reuters acquisition and expansion anchors | ImClone $330M acquisition plus expansion up to 700B won, but no stage3 price path | price_data_unavailable_after_deep_search |
| r7_loop11_sk_bioscience_idt_cmo_mna | Reuters acquisition and event-return anchor | Announcement rally before utilization/backlog confirmation | reported_event_anchor_not_full_ohlc |
| r7_loop11_hanall_immunovant_batoclimab_ted_failure | Reuters partner trial-failure anchor | Immunovant -4.8% after batoclimab failed two late-stage thyroid eye disease trials | hanall_stock_price_data_unavailable_after_deep_search |
| r7_loop11_lunit_medical_ai_external_validation | arXiv external validation evidence | AUC 0.91 with subgroup weakness, but no reimbursement/adoption revenue anchor | price_data_unavailable_after_deep_search |
| r7_loop11_biopharma_tariff_policy_relief_basket | Reuters policy and sector-return anchor | Policy-support sector rally before company-level earnings bridge | reported_sector_anchor_not_full_ohlc |
