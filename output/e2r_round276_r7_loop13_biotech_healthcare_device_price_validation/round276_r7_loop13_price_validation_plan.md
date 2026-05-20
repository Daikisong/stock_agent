# Round 276 R7 Price Validation Plan

- price_validation_completed: partial_with_reported_price_anchors
- full_adjusted_ohlc_complete: false
- Do not invent OHLC, stage prices, prescription ramp, royalty cashflow, utilization, reimbursement, patent clearance, administered demand, margin or FCF where raw data are unavailable.

## Backfill Fields

- price_data_source
- full_adjusted_ohlc_complete
- reported_price_anchor
- reported_return_anchor
- stage2_price_anchor
- stage3_price
- stage4b_price
- stage4c_price
- event_mfe_pct
- event_mae_pct
- commercialization_or_utilization_anchor
- regulatory_quality_or_patent_gate
- demand_or_administered_dose_anchor
- price_validation_status

## Case Anchors

| case | data source | reported anchor | status |
|---|---|---|---|
| r7_loop13_yuhan_lazertinib_global_fda_approval | Reuters / MarketWatch FDA approval and CRL anchors | Yuhan full OHLC unavailable; subcutaneous Rybrevant CRL was manufacturing-inspection related | yuhan_stock_ohlc_unavailable_after_deep_search |
| r7_loop13_alteogen_merck_sc_keytruda_platform | Reuters / WSJ SC Keytruda trial, launch and patent anchors | Merck premarket +1.8% on non-inferiority; Alteogen full OHLC unavailable | alteogen_stock_ohlc_unavailable_after_deep_search |
| r7_loop13_samsung_biologics_gsk_rockville_facility | Reuters GSK facility acquisition and sector-support anchors | Samsung Biologics -0.4% while KOSPI +2.0%; relative -2.4pp | reported_event_anchor_not_full_ohlc |
| r7_loop13_celltrion_us_factory_tariff_hedge | Reuters Celltrion U.S. factory acquisition and expansion anchors | Product transfer, utilization and margin are not confirmed | price_data_unavailable_after_deep_search |
| r7_loop13_sk_bioscience_idt_biologika_cdmomna | Reuters SK Bioscience / IDT Biologika deal anchor | SK Bioscience shares +11.7% in morning trading | reported_event_anchor_not_full_ohlc |
| r7_loop13_jeisys_medical_archimed_aesthetic_device_takeout | WSJ Jeisys / ArchiMed take-private anchor | Revenue CAGR 44%, adjusted pretax earnings CAGR 45%; tradable Stage 3 unavailable | reported_takeout_anchor_not_full_ohlc |
| r7_loop13_biopharma_tariff_support_policy_rally | Reuters Korea market / policy-support anchors | Policy relief, not company-level Green evidence | reported_event_anchor_not_full_ohlc |
| r7_loop13_sk_bioscience_skycovione_demand_collapse_reference | public vaccine-demand-collapse reference | Approval/procurement failed to become demand; stock OHLC unavailable | stock_ohlc_unavailable_after_deep_search |
