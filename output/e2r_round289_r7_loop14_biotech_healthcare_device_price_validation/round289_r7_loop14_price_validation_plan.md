# Round 289 R7 Price Validation Plan

- price_validation_completed: partial_with_reported_price_anchors
- full_adjusted_ohlc_complete: false
- Do not invent OHLC, stage prices, utilization, inspection quality, reimbursement, royalty conversion, physician adoption, or Phase 2/3 data where raw data are unavailable.

## Backfill Fields

- price_data_source
- full_adjusted_ohlc_complete
- reported_event_return_anchor
- reported_event_price_anchor
- deal_value_anchor
- facility_capacity_anchor
- fda_approval_anchor
- adoption_target_anchor
- clinical_failure_drawdown_anchor
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
| r7_loop14_samsung_biologics_gsk_us_facility | Reuters Samsung Biologics-GSK facility event anchor | -0.4% vs KOSPI +2.0% | partial_reported_anchor |
| r7_loop14_celltrion_us_factory_tariff_hedge | Reuters Celltrion U.S. factory acquisition and expansion anchors | price_data_unavailable_after_deep_search | price_data_unavailable_after_deep_search |
| r7_loop14_sk_bioscience_idt_biologika_ma | Reuters SK Bioscience-IDT Biologika M&A anchor | +11.7% | partial_reported_anchor |
| r7_loop14_alteogen_keytruda_qlex_sc_formulation | Reuters Keytruda SC trial/launch/approval anchors + WSJ patent-dispute anchor | price_data_unavailable_after_deep_search | price_data_unavailable_after_deep_search |
| r7_loop14_yuhan_lazertinib_jnj_rybrevant_approval | Reuters FDA approval and later CRL anchors | price_data_unavailable_after_deep_search | price_data_unavailable_after_deep_search |
| r7_loop14_hugel_letybo_us_aesthetic_launch | Allure Letybo U.S. launch context + AP FDA counterfeit Botox warning | price_data_unavailable_after_deep_search | price_data_unavailable_after_deep_search |
| r7_loop14_adel_sanofi_alzheimers_tech_export_reference | Reuters ADEL-Sanofi deal anchor | unlisted_reference_no_ohlc | unlisted_reference_no_ohlc |
| r7_loop14_global_clinical_fda_failure_hard_reference | Reuters/Barron's clinical trial failure and FDA rejection/hold anchors | HilleVax -87.6%, Corcept -50.8%, PepGen -25%+ | partial_reported_anchor |
