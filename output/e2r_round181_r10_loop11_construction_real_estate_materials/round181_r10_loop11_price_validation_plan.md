# Round-181 R10 Loop-11 Price Validation Plan

R10 needs event-date price-path validation because contracts, PF events, tenant evidence, safety events, and cement pricing can move prices before fundamentals confirm.

## Required Fields

- `ticker`
- `company_name`
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
- `relative_strength_vs_construction_basket`
- `relative_strength_vs_reit_basket`
- `relative_strength_vs_building_materials_basket`
- `contract_amount`
- `contract_counterparty`
- `contract_period`
- `project_completion_date`
- `contract_amount_to_prior_sales`
- `backlog`
- `cost_ratio`
- `op_revision_before_stage3`
- `op_revision_after_stage3`
- `eps_revision_before_stage3`
- `eps_revision_after_stage3`
- `cash_conversion_signal`
- `pf_exposure`
- `pf_refinancing_success_flag`
- `bridge_loan_exposure`
- `unsold_units_signal`
- `workout_flag`
- `debt_rescheduling_flag`
- `tenant_lease_flag`
- `occupancy`
- `noi`
- `affo`
- `affo_per_share`
- `dividend_coverage`
- `ltv`
- `refinancing_rate`
- `safety_accident_flag`
- `fatal_accident_flag`
- `government_investigation_flag`
- `quality_cost_flag`
- `business_suspension_flag`
- `building_material_volume`
- `price_pass_through_signal`
- `energy_cost_signal`
- `regulatory_collusion_flag`
- `disclosure_confidence`
- `valuation_at_stage3`
- `valuation_at_stage4b`

## Case Backfill Priorities

- `samsung_ea_fadhili_epc_stage2_strong_case`: cost ratio, cash conversion, OP/EPS revision, and Fadhili event price path.
- `gs_construction_fadhili_epc_pf_quality_cap_case`: individual contract amount, EPC margin, PF exposure, and quality cost.
- `samsung_ct_ai_data_center_option_no_contract_cap_case`: EPC contract, tenant lease, power/water/permitting, NOI/AFFO, and price-path reaction.
- `k_reit_dividend_coverage_ltv_refinancing_case`: occupancy, NOI, AFFO/share, dividend coverage, LTV, and refinancing rate.
- `taeyoung_construction_pf_workout_hard_4c_case`: workout/debt-rescheduling event date and price reaction.
- `hdc_hyundai_development_gwangju_collapse_hard_4c_case`: safety accident date, quality cost, investigation, and brand impact.
