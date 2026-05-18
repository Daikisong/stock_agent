# Round-185 R1 Loop-12 Price Validation Plan

R1 Loop 12 must backfill order/contract fields, price-path fields, and capital/governance fields together.

## Required Fields

- `ticker`
- `company_name`
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
- `mfe_60d_after_stage2`
- `mae_60d_after_stage2`
- `mfe_120d_after_stage2`
- `mae_120d_after_stage2`
- `mfe_252d_after_stage2`
- `mae_252d_after_stage2`
- `relative_strength_vs_kospi`
- `relative_strength_vs_kosdaq`
- `relative_strength_vs_industrial_basket`
- `relative_strength_vs_power_equipment_basket`
- `relative_strength_vs_defense_basket`
- `relative_strength_vs_shipbuilding_equipment_basket`
- `contract_amount`
- `contract_counterparty`
- `contract_period`
- `contract_amount_to_prior_sales`
- `product_or_service`
- `backlog`
- `delivery_schedule`
- `government_program_flag`
- `program_budget`
- `recurring_service_flag`
- `op_revision_before_stage3`
- `op_revision_after_stage3`
- `eps_revision_before_stage3`
- `eps_revision_after_stage3`
- `opm`
- `fcf_signal`
- `cash_conversion_signal`
- `capital_raise_flag`
- `cb_bw_flag`
- `dilution_type`
- `fss_revision_request_flag`
- `governance_risk_flag`
- `minority_shareholder_risk_flag`
- `media_report_only_flag`
- `mou_loi_flag`
- `non_binding_flag`
- `disclosure_confidence`
- `valuation_at_stage3`
- `valuation_at_stage4b`

## Backfill Priorities

- `iljin_midcap_transformer_stage3_candidate_case`: customer, amount, period, OPM, OP/EPS, MFE/MAE, and relative strength.
- `hanwha_aerospace_capital_raise_dilution_case`: dilution terms, FSS correction timing, price MAE, and use-of-proceeds confidence.
- `doosan_bobcat_governance_cap_case`: governance event date, minority-shareholder impact, valuation discount, and price path.
- `shipbuilding_equipment_backlog_stage3_candidate_case`: yard backlog link, delivery schedule, OPM, FCF, and own price path.
