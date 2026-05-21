# Round 328 R7 Loop 17 Stage Rules

Do not apply these weights to production scoring yet.

## Stage2-Actionable Rules

- `event_return_at_least_5pct_or_clear_relative_outperformance`
- `deal_approval_facility_capacity_or_product_launch_is_explicit`
- `customer_product_facility_or_indication_is_specific`
- `revenue_path_exists_through_CDMO_utilization_royalty_launch_sales_or_reimbursement`
- `patent_litigation_tariff_manufacturing_inspection_or_integration_4B_is_identified`
- `price_reaction_validates_the_evidence_when_available`
- `approval_or_MA_can_move_to_commercial_execution`

## Stage3-Yellow Rules

- `CDMO_utilization_orderbook_or_customer_transfer_confirms`
- `FDA_or_EMA_approval_converts_to_commercial_launch`
- `royalty_product_supply_or_reimbursement_revenue_visibility_exists`
- `patent_litigation_risk_is_contained`
- `payer_physician_or_channel_adoption_is_visible`
- `US_tariff_hedge_converts_to_margin_or_volume_benefit`
- `facility_acquisition_integration_is_on_schedule`

## Stage3-Green Rules

- `approval_or_facility_acquisition_converts_into_recurring_revenue`
- `CDMO_utilization_and_margin_are_visible`
- `platform_royalty_or_supply_economics_are_disclosed_or_inferable`
- `patent_litigation_and_manufacturing_inspection_risks_are_contained`
- `launch_sellthrough_and_reimbursement_are_confirmed`
- `full_window_MFE_MAE_is_available_and_supportive`

## Green Blockers

- `facility_acquisition_without_utilization`
- `policy_support_without_company_specific_contract`
- `FDA_approval_without_sellthrough`
- `platform_link_without_royalty_visibility`
- `MA_reference_without_public_liquidity`
- `biosimilar_opportunity_without_patent_clearance`
- `hard_4C_without_sourced_price_anchor`
- `full_adjusted_ohlc_missing_for_Green_confirmation`

## Score Up Axes

- `manufacturing_asset_MA`
- `biopharma_policy_support`
- `US_localization_tariff_hedge`
- `blockbuster_platform_linkage`
- `FDA_approval_commercial_launch`
- `medical_device_MA_valuation`
- `patent_litigation_risk`
- `utilization_margin_conversion`

## Score Down Axes

- `facility_acquisition_without_price_validation`
- `policy_support_without_company_contract`
- `FDA_approval_without_sellthrough`
- `platform_link_without_royalty_visibility`
- `MA_reference_without_public_liquidity`
- `biosimilar_opportunity_without_patent_clearance`
- `CDMO_capacity_without_utilization`
- `hard_4C_without_sourced_price_anchor`

## Row Separation Rules

- `case_library_row_describes_stage_candidate_and_evidence_quality`
- `trigger_calibration_row_stores_reported_event_return_deal_approval_facility_or_litigation_metrics`
- `ohlc_backfill_row_stores_adjusted_OHLC_MFE_MAE_below_entry_peak_drawdown`
- `do_not_create_MFE_MAE_without_full_adjusted_OHLC`
- `do_not_treat_policy_facility_FDA_or_patent_headline_as_Green_without_revenue_utilization_royalty_sellthrough_or_risk_closure`
