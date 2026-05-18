# Round-184 R13 Loop-11 Price Validation Plan

R13 unifies price-path, disclosure-confidence, RedTeam, and cash-flow validation across R1-R12.

## Required Fields

- `ticker`
- `company_name`
- `sector_round`
- `canonical_archetype`
- `case_type`
- `stage1_date`
- `stage2_date`
- `stage3_date`
- `stage4b_date`
- `stage4c_date`
- `stage1_trigger`
- `stage2_trigger`
- `stage3_trigger`
- `stage4b_trigger`
- `stage4c_trigger`
- `price_at_stage1`
- `price_at_stage2`
- `price_at_stage3`
- `price_at_stage4b`
- `price_at_stage4c`
- `return_1d_after_event`
- `return_5d_after_event`
- `return_20d_after_stage2`
- `return_60d_after_stage2`
- `return_120d_after_stage2`
- `return_252d_after_stage2`
- `mfe_20d_after_stage2`
- `mae_20d_after_stage2`
- `mfe_60d_after_stage2`
- `mae_60d_after_stage2`
- `mfe_120d_after_stage2`
- `mae_120d_after_stage2`
- `mfe_252d_after_stage2`
- `mae_252d_after_stage2`
- `relative_strength_vs_kospi`
- `relative_strength_vs_kosdaq`
- `relative_strength_vs_sector_basket`
- `op_revision_before_stage3`
- `op_revision_after_stage3`
- `eps_revision_before_stage3`
- `eps_revision_after_stage3`
- `fcf_signal`
- `roe_or_affo_signal`
- `opm_signal`
- `contract_amount`
- `contract_counterparty`
- `contract_period`
- `customer_name`
- `revenue_recognition_timing`
- `royalty_revenue`
- `arr_or_bookings`
- `noi_or_affo`
- `prescription_volume`
- `repeat_revenue_signal`
- `disclosure_source_type`
- `opendart_list_only_flag`
- `opendart_detail_flag`
- `media_report_only_flag`
- `mou_loi_flag`
- `non_binding_flag`
- `parser_confidence`
- `disclosure_confidence`
- `event_price_only_flag`
- `price_only_event_allowed`
- `stage3_green_allowed`
- `stage4b_watch_flag`
- `stage4c_hard_flag`
- `hard_4c_reason`
- `valuation_at_stage3`
- `valuation_at_stage4b`

## Case Backfill Priorities

- `hanmi_hbm_equipment_stage3_early_capture_case`: contract detail, confirmed customers, OP/EPS revision, MFE/MAE, and 4B crowding.
- `samsung_sds_kkr_cb_stage2_not_green_case`: AI ARR/revenue, CB dilution, OPM/FCF, and one-day event return.
- `kogas_daesung_gas_event_4b_case`: drill-bit result, commerciality, event returns, and price-only unwind risk.
- `jeju_air_fatal_accident_hard_4c_case`: accident date MAE, safety inspections, trust recovery, and demand impact.
- `naver_dunamu_holdco_link_stage2_case`: equity-method income, cash upstream, security incidents, regulation, and listed EPS/FCF linkage.
