# Evidence URL Pending Report

v12 잔차 장부입니다. 검증 통과 항목은 rolling calibration에 들어가고, 제약은 guardrail로 남깁니다.
source proxy 또는 evidence URL 한계는 positive patch를 막거나 scope 제한을 강화합니다.

- residual_rows: `3906`

| trigger_id | symbol | archetype | verdict | source_proxy_only | evidence_url_pending |
|---|---|---|---|---|---|
| YUHAN_000100_2024_01_29_STAGE2A_REGULATORY_COMMERCIALIZATION | 000100 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_4B_too_late | False | True |
| C23_R7_L209_T03 | 000100 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_too_late | False | True |
| None | 000100 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | None | True | True |
| V12_COMPACT_000100_2024-07-01_APPROVAL_TO_COMMERCIAL_ROYALTY_BRIDGE | 000100 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive | True | True |
| C24-R7-L99-TRG-04-000100 | 000100 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_too_late | True | True |
| C24-R7-L100-TRIG-01-000100 | 000100 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_correct | True | True |
| R9L85_C29_000120_20240119_STAGE2_LOGISTICS_VOLUME_MARGIN_BRIDGE | 000120 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_correct_if_volume_margin_bridge_required | True | True |
| TRG_R9L82-C29-000120-CJ-LOGISTICS-PARCEL-VOLUME-MARGIN-FADE | 000120 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should not treat logistics/parcel volume beta as durable Stage2 unless parcel volume, freight-rate/pass-through, contract mix, automation productivity, revenue conversion and margin bridge are visible. CJ Logistics had early MFE and then persistent high-MAE fade, so it is a local-4B boundary until operating-leverage proof is repaired. | True | True |
| R13L85_REVIEW_R9_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_000120_2024-01-19 | 000120 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_correct | True | True |
| C32_000150_20241029_LOCAL_4B_WATCH | 000150 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive_or_overpromotion_risk | True | True |
| TRG_R12L73-C32-000150-DOOSAN-HOLDCO-DELAYED-CONTROL-PREMIUM | 000150 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should not blindly block the holding company if control-premium option value later becomes visible, but the entry cannot be pure event chase because early MAE was severe. Doosan is a delayed positive with early local 4B risk and later lifecycle drawdown. | False | True |
| C32_000150_DOOSAN_20240712_S2A | 000150 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive_high_mae | True | True |
| TRG_R12L73-C32-000150-DOOSAN-HOLDCO-DELAYED-CONTROL-PREMIUM | 000150 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should not blindly block the holding company if control-premium option value later becomes visible, but the entry cannot be pure event chase because early MAE was severe. Doosan is a delayed positive with early local 4B risk and later lifecycle drawdown. | False | True |
| TRG_R11L82-C32-000150-DOOSAN-HOLDCO-RESTRUCTURING-CONTROL-DISCOUNT-LIFECYCLE | 000150 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should protect governance/restructuring positives only when event mechanics, board/shareholder process, asset/NAV bridge, control-premium logic, timing and downside cap are visible. Doosan produced very large MFE with shallow entry-basis MAE, but the row still needs source repair and event-mechanics validation before runtime promotion. | True | True |
| R12L88_C32_000240_20240129_STAGE2_CONTROL_PREMIUM_HOLDCO | 000240 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_correct_if_control_premium_capital_return_bridge_required | True | True |
| C32_000240_HANKOOK_20231206_FAILED_TENDER_S2 | 000240 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | None | True | True |
| R12L94_C32_HANKOOKANDCOMPANY_2024_STAGE4B_CONTROL_PREMIUM_EVENT_CAP | 000240 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_4B_too_late_if_control_premium_tender_aftermath_event_premium_not_capped | True | True |
| R13L88_REVIEW_R12_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_000240_2024-01-29 | 000240 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_correct | True | True |
| T_R13_STAGE2FP_L6_000240_Stage2Actionable_2023-12-06 | 000240 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_stage2_false_positive_or_overpromotion_risk | True | True |
| R13L94_REVIEW_R12_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_000240_2024_02_02_TRIGGER | 000240 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_4B_too_late_if_control_premium_tender_aftermath_event_premium_not_capped | True | True |
| TRG_R7L81-C23-000250-SCD-BIOSIMILAR-APPROVAL-PARTNER-COMMERCIALIZATION | 000250 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | C23 should protect regulatory/commercialization positives only when approval, partner/license economics, supply agreement, launch timing, revenue conversion and margin bridge are visible. Samchundang Pharm produced very large MFE with shallow early MAE, but post-peak drawdown requires lifecycle 4B if commercialization evidence fades. | True | True |
| R7L89_C23_SCDPHARM_2024_STAGE2_ACTIONABLE_BIOSIMILAR_COMMERCIALIZATION | 000250 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R7L88_C23_000250_20240325_STAGE2_BIOSIMILAR_APPROVAL_COMMERCIAL | 000250 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_correct_if_approval_partner_revenue_bridge_required | True | True |
| R7L95_C23_SCD_2024_STAGE2_ACTIONABLE_BIOSIMILAR_GLOBAL_COMMERCIALIZATION_PARTNER_BRIDGE | 000250 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| None | 000250 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | False | True |
| None | 000250 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | None | False | True |
| R13L88_REVIEW_R7_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_000250_2024-03-25 | 000250 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_correct | True | True |
| T_R9L10_000270_STAGE2 | 000270 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_correct | False | True |
| T_C29_R9L105_000270_Stage2Actionable_20240125 | 000270 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| TRG_C29_R9L100_000270_STAGE2A_20240125 | 000270 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_correct | False | True |
| T_C29_R9L106_000270_20240614_17_Stage3-Green | 000270 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_correct | True | True |
| T_C29_R9L106_000270_20240202_02_Stage3-Yellow | 000270 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_correct | True | True |
| T_R9L10_000270_4B | 000270 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_correct | False | True |
| T_C21_R6L104_000370_STAGE2_20240201 | 000370 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | True | True |
| None | 000370 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | True | True |
| None | 000370 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | False | True |
| TRG_R6L80-C22-000370-HANWHA-GENERAL-INSURANCE-RATE-CYCLE | 000370 | C22_INSURANCE_RATE_CYCLE_RESERVE | C22 should allow non-life insurance positives when loss ratio, reserve adequacy, rate cycle, capital buffer and shareholder-return bridge are visible. Hanwha General Insurance had strong early MFE with bounded entry-basis MAE, then a lifecycle drawdown. | True | True |
| TRG_R6L76-C22-000370-HANWHA-GENERAL-INSURANCE-LOSS-RATIO-CAPITAL-RETURN | 000370 | C22_INSURANCE_RATE_CYCLE_RESERVE | C22 should allow non-life insurers when value-up and rate-cycle attention connects to loss-ratio improvement, CSM/IFRS17 reserve quality, K-ICS capital buffer, dividend/buyback or capital-return bridge. Hanwha General Insurance produced high MFE with controlled entry-basis MAE, but later drawdown requires lifecycle local 4B if reserve/capital-return evidence fades. | True | True |
| TRG_R6L74-C22-000370-HANWHA-GI-RESERVE-CAPITAL-RETURN | 000370 | C22_INSURANCE_RATE_CYCLE_RESERVE | C22 should allow Stage2 when non-top P&C insurers show CSM, reserve release, loss-ratio improvement, K-ICS/capital return or shareholder-return bridge. Hanwha General Insurance produced high MFE with controlled entry-basis MAE, but later local 4B-watch is needed if the reserve/capital-return evidence stops refreshing. | True | True |
| None | 000370 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | True | True |
| TRG_R6L76-C22-000370-HANWHA-GENERAL-INSURANCE-LOSS-RATIO-CAPITAL-RETURN | 000370 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_correct | True | True |
| TRG_R6L74-C22-000370-HANWHA-GI-RESERVE-CAPITAL-RETURN | 000370 | C22_INSURANCE_RATE_CYCLE_RESERVE | C22 should allow Stage2 when non-top P&C insurers show CSM, reserve release, loss-ratio improvement, K-ICS/capital return or shareholder-return bridge. Hanwha General Insurance produced high MFE with controlled entry-basis MAE, but later local 4B-watch is needed if the reserve/capital-return evidence stops refreshing. | True | True |
| R13_CROSS_000370_2024-02-01_Stage2-Actionable-InsuranceValueupCSM | 000370 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive | True | True |
| None | 000370 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | True | True |
| C22-R6-L101-02-T1 | 000370 | C22_INSURANCE_RATE_CYCLE_RESERVE | partly_correct_but_should_attach_high_MAE_reserve_volatility_guard | True | True |
| TRG_C22_R6L104_07 | 000370 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive | True | True |
| None | 000370 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | True | True |
| None | 000370 | C22_INSURANCE_RATE_CYCLE_RESERVE | Canonical Stage4B is acceptable only as local/watch; full 4B or Stage3 promotion needs non-price reserve/capital bridge. | True | True |
| C31_R11L106_TRG_18 | 000370 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | None | True | True |
| None | 000370 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | None | True | True |
| V12_COMPACT_000370_2024-02-29_policy_valueup_insurance_csm_reserve_capital_return_cash_bridge | 000370 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | True | True |
| R6L90_C22_000400_20240213_STAGE2_FALSE_POSITIVE_NONLIFE_MNA_THEME | 000400 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive_if_MNA_theme_counted_as_C22_rate_cycle | True | True |
| R6L86_C22_000400_20240423_STAGE2_FALSE_POSITIVE_SMALLCAP_INSURANCE_MNA_BETA | 000400 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive_if_MNA_beta_overcredited | True | True |
| None | 000400 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | True | True |
| R6L97_C22_LOTTEINS_2024_STAGE4B_INSURANCE_SALE_RESERVE_EVENT_CAP | 000400 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_4B_too_late_if_insurance_sale_reserve_event_premium_not_capped | True | True |
| R6L91_C22_LOTTEINS_2024_STAGE4B_INSURANCE_MA_CONTROL_PREMIUM_CAP | 000400 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_4B_too_late_if_insurance_MA_control_premium_event_not_capped | True | True |
| R12L88_C32_LOTTEINS_2024_STAGE2_ACTIONABLE_INSURANCE_SALE_PREMIUM | 000400 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R13L86_REVIEW_R6_C22_INSURANCE_RATE_CYCLE_RESERVE_000400_2024-04-23 | 000400 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R13L91_REVIEW_R6_C22_INSURANCE_RATE_CYCLE_RESERVE_000400_2024_06_26_TRIGGER | 000400 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_4B_too_late_if_insurance_MA_control_premium_event_not_capped | True | True |
| TRG_R1L76-C02-000500-GAON-CABLE-GRID-CAPEX-LIFECYCLE | 000500 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_correct | True | True |
| TRG_R1L76-C02-000500-GAON-CABLE-GRID-CAPEX-LIFECYCLE | 000500 | C02_POWER_GRID_DATACENTER_CAPEX | C02 should include cable suppliers only when grid capex, export order, copper pass-through and margin bridge are visible. Gaon Cable produced high MFE with controlled early MAE, but post-peak drawdown and a later 2024 corporate-action candidate require lifecycle and validation controls. | True | True |
| TRG_R1L78-C02-000500-GAON-CABLE-DATACENTER-GRID-CABLE-BACKLOG | 000500 | C02_POWER_GRID_DATACENTER_CAPEX | C02 should include cable names only when grid/datacenter capex maps to customer orderbook, cable shipment, ASP/copper pass-through and margin bridge. Gaon Cable produced high MFE with controlled entry-basis MAE, but the later drawdown requires lifecycle local 4B if orderbook/margin evidence fades. | True | True |
| T_C15_R4L104_000500_Stage2_Actionable_20240125 | 000500 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_may_under_control_early_MAE_if_later_MFE_dominates | True | True |
| None | 000500 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| None | 000500 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| R13_CROSS_000500_2024-06-12_Stage4B | 000500 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| None | 000540 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | True | True |
| R6L91_C22_HEUNGKUKFIRE_2024_STAGE2_FALSE_POSITIVE_FIRE_INSURANCE_VALUEUP | 000540 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive_if_fire_insurance_valueup_theme_counts_without_reserve_loss_ratio_capital_bridge | True | True |
| C22-R6-L101-03-T1 | 000540 | C22_INSURANCE_RATE_CYCLE_RESERVE | false_positive_valueup_rate_label_without_reserve_quality_bridge | True | True |
| R6L99_C22_HEUNGKUKFIRE_2024_STAGE4B_SMALLCAP_INSURANCE_VALUEUP_EVENT_CAP | 000540 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_4B_too_late_if_smallcap_insurance_valueup_event_premium_not_capped | True | True |
| TRG_C22_R6L104_08 | 000540 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_4C_too_late | True | True |
| V12_COMPACT_000540_2024-02-01_policy_valueup_insurance_csm_reserve_capital_return_cash_bridge | 000540 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | True | True |
| TRIG_C31_R11L100_006_000540 | 000540 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_4B_too_late | True | True |
| R13L91_REVIEW_R6_C22_INSURANCE_RATE_CYCLE_RESERVE_000540_2024_02_14_TRIGGER | 000540 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive_if_fire_insurance_valueup_theme_counts_without_reserve_loss_ratio_capital_bridge | True | True |
| C06-127-T001 | 000660 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_correct_but_green_should_wait_for_mass_production | False | True |
| R2L98_C06_SKHYNIX_2024_STAGE2_ACTIONABLE_HBM_MEMORY_CUSTOMER_CAPACITY_MIX_BRIDGE | 000660 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| SKHYNIX_000660_2024_02_22_STAGE2A_HBM_CUSTOMER_CAPACITY_MIX | 000660 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_4B_too_late | False | True |
| R2L91_C06_SKHYNIX_2024_STAGE2_ACTIONABLE_HBM_CUSTOMER_CAPACITY_BRIDGE | 000660 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| C06-127-T002 | 000660 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_correct_green_with_drawdown_aware_hold | False | True |
| C06-127-T003 | 000660 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_partly_too_permissive_if_late_valuation_not_penalized | False | True |
| None | 000660 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | None | True | True |
| None | 000660 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | None | True | True |
| C31_L101_T001_000660 | 000660 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_partially_correct_but_high_MAE_guard_needed | True | True |
| None | 000660 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | None | False | True |
| C32_000670_20240913_STAGE2_ACTIONABLE | 000670 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive_or_overpromotion_risk | True | True |
| R12L92_C32_000670_20240913_STAGE2_FALSE_POSITIVE_SPILLOVER_CONTROL_BATTLE | 000670 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive_if_spillover_MFE_counted_as_direct_C32_tender_evidence | True | True |
| T_C01_R1L111_000720_20240126_Stage2 | 000720 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | low-MAE rebound was tradable but construction/PF balance-sheet thesis belongs to C30/C05, not generic C01 backlog | True | True |
| T_C05_R1L108_000720_20240126_MARGIN_BACKLOG_REPAIR | 000720 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | True | True |
| None | 000720 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | True | True |
| R1L84_C05_000720_20250122_STAGE2_EPC_BACKLOG_MARGIN_BRIDGE_POSITIVE | 000720 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | current_profile_may_undercredit_if_C05_too_guarded | True | True |
| R1L86_C05_000720_20240429_STAGE2_FALSE_POSITIVE_CONTRACT_THEME | 000720 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | current_profile_false_positive_if_contract_theme_overcredited | True | True |
| T_C05_R1L109_000720_20240202_BACKLOG_DELIVERY_MARGIN_BRIDGE | 000720 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | True | True |
| R10L90_C30_HYUNDAICONST_2024_STAGE2_ACTIONABLE_PF_DISCOUNT_REPAIR | 000720 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| C30_R10L105_000720_20240126_Stage2_Actionable | 000720 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_error_if_C30_overcredits_price_or_low_PBR_without_balance_sheet_bridge | True | True |
| R10L87_C30_HDEC_2025_STAGE2_ACTIONABLE_BALANCE_REPAIR | 000720 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_missed_structural_if_large_builder_repair_excluded_by_C30_red_watch | True | True |
| R10L86_C30_000720_20240429_STAGE2_FALSE_POSITIVE_LARGECAP_CONSTRUCTION | 000720 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive_if_largecap_construction_theme_overcredited | True | True |
| None | 000720 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | True | True |
| R13L86_REVIEW_R1_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_000720_2024-04-29 | 000720 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R13L86_REVIEW_R10_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_000720_2024-04-29 | 000720 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| None | 000810 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | True | True |
| None | 000810 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | True | True |
| R6L99_C22_SAMSUNGFIRE_2024_STAGE2_ACTIONABLE_PNC_RATE_RESERVE_CAPITAL_RETURN_BRIDGE | 000810 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R6L41_C22_000810_T1_STAGE2A | 000810 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_correct | True | True |
| None | 000810 | C22_INSURANCE_RATE_CYCLE_RESERVE | Stage3-Green allowed only when reserve quality, CSM durability, solvency capital, and payout execution are all explicit. | True | True |
| R6L41_C22_000810_T2_GREEN_COMPARE | 000810 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_too_late | True | True |
| None | 000810 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | True | True |
| TRG_C22_R6L104_02 | 000810 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_too_late | True | True |
| None | 000810 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | True | True |
| None | 000810 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | True | True |
| None | 000810 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | True | True |
| None | 000810 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | True | True |
| R6L41_C22_000810_T3_4B_LOCAL | 000810 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_4B_too_early | True | True |
| TRIG_C31_R11L100_004_000810 | 000810 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_correct | True | True |
| C31_R11L106_TRG_15 | 000810 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | None | True | True |
| None | 000810 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | None | True | True |
| V12_COMPACT_000810_2024-06-28_policy_valueup_insurance_csm_reserve_capital_return_cash_bridge | 000810 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_correct | True | True |
| None | 000810 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | None | False | True |
| None | 000810 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| None | 000810 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| None | 000810 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| None | 000810 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| None | 000810 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | None | True | True |
| None | 000860 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | True | True |
| T_C15_R4L105_000880_20240605_09_Stage2-Actionable | 000880 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive | True | True |
| None | 000880 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | True | True |
| R12L84_C32_000880_20240201_STAGE2_FALSE_POSITIVE_HOLDCO_DEFENSE_THEME | 000880 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive_if_conglomerate_theme_overcredited | True | True |
| TR_C16_UNION_S2_20230217 | 000910 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_false_positive | True | True |
| TRG_R4L75-C16-000910-UNION-RARE-EARTH-POLICY-PROXY-FADE | 000910 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_false_positive | True | True |
| None | 000910 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| R4L98_C16_UNION_2024_STAGE2_FALSE_POSITIVE_RAREEARTH_POLICY_SUPPLY_WATCH | 000910 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_false_positive_if_rareearth_policy_watch_counts_without_resource_exposure_order_volume_pass_through_margin_revision_bridge | True | True |
| TRG_R4L75-C16-000910-UNION-RARE-EARTH-POLICY-PROXY-FADE | 000910 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | C16 should not treat rare-earth or resource policy proxy beta as durable Stage2 unless direct resource supply, processing capacity, customer contract or margin bridge is visible. Union had only modest MFE and later deep MAE/drawdown. | True | True |
| TRG_R4L78-C16-000910-UNION-RAREEARTH-RESOURCE-THEME-FADE | 000910 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | C16 should not treat rare-earth/resource-security theme beta as durable Stage2 unless direct supply exposure, customer demand, pricing, inventory and margin bridge are visible. Union had a small early MFE and then opened a deep MAE drawdown path. | True | True |
| R4L92_C16_000910_20240110_STAGE2_FALSE_POSITIVE_RARE_EARTH_POLICY | 000910 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_false_positive_if_rare_earth_policy_vocabulary_overcredited | True | True |
| C16-102-06-000910-T1 | 000910 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_false_positive | True | True |
| DBHITEK_000990_2024_06_20_STAGE2_FALSE_POSITIVE_MEMORY_BETA_NO_HBM_BRIDGE | 000990 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_false_positive | False | True |
| R2L85_C06_000990_20240620_STAGE2_FALSE_POSITIVE_FOUNDRY_MEMORY_BETA | 000990 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_false_positive_if_memory_beta_overcredited | True | True |
| R13_CROSS_R13L4_C32_000990_20240304_TENDER_CASH_PATH_TRUST_000990_2024-03-04_Stage4B | 000990 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | True | True |
| R13L85_REVIEW_R2_C06_HBM_MEMORY_CUSTOMER_CAPACITY_000990_2024-06-20 | 000990 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| T_C32_R12L106_001040_20240307_Local-4B-Watch | 001040 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | Local-4B-Watch is allowed but full4B should wait for payout, asset sale, or tender cash bridge | True | True |
| C32_001040_20240207_STAGE2_ACTIONABLE | 001040 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive_or_overpromotion_risk | True | True |
| R12L86_C32_001040_20240329_STAGE2_FALSE_POSITIVE_HOLDCO_VALUEUP | 001040 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive_if_holdco_theme_overcredited | True | True |
| R12L92_C32_CJ_2024_STAGE4B_HOLDCO_CONTROL_PREMIUM_EVENT_CAP | 001040 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_4B_too_late_if_holdco_control_premium_event_premium_not_capped | True | True |
| R13L86_REVIEW_R12_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_001040_2024-03-29 | 001040 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R13L92_REVIEW_R12_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_001040_2024_05_10_TRIGGER | 001040 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_4B_too_late_if_holdco_control_premium_event_premium_not_capped | True | True |
| R4L92_C16_001120_20240129_STAGE2_RESOURCE_TRADING_CASH | 001120 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_correct_if_resource_channel_margin_cash_bridge_required_but_Green_strict | True | True |
| C16-102-03-001120-T1 | 001120 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_missed_structural | True | True |
| None | 001120 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| R4L101_C16_LXINTL_2024_STAGE2_FALSE_POSITIVE_RESOURCE_TRADING_POLICY_WATCH | 001120 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_false_positive_if_resource_trading_policy_watch_counts_without_offtake_volume_inventory_margin_revision_bridge | True | True |
| None | 001120 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| None | 001120 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| None | 001120 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| None | 001120 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| None | 001120 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| None | 001120 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| None | 001120 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | True | True |
| R6L89_C21_001200_20240222_STAGE2_FALSE_POSITIVE_BROKERAGE_PRICE_BLOWOFF | 001200 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive_if_brokerage_price_blowoff_counted_as_capital_return | True | True |
| R12L88_C32_001230_20240202_STAGE2_FALSE_POSITIVE_HOLDCO_SPLIT_THEME | 001230 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive_if_split_theme_spike_overcredited | True | True |
| R13L88_REVIEW_R12_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_001230_2024-02-02 | 001230 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R10L91_C30_NAMKWANG_2024_STAGE2_FALSE_POSITIVE_REGIONAL_CONSTRUCTION_PF_WATCH | 001260 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive_if_regional_construction_recovery_counts_without_PF_cashflow_balance_bridge | True | True |
| R10L87_C30_001260_20240102_STAGE2_FALSE_POSITIVE_POLICY_THEME | 001260 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive_if_policy_theme_overcredited | True | True |
| R13L87_REVIEW_R10_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_001260_2024-01-02 | 001260 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R13L91_REVIEW_R10_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_001260_2024_02_14_TRIGGER | 001260 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive_if_regional_construction_recovery_counts_without_PF_cashflow_balance_bridge | True | True |
| R6L91_C21_001290_20240215_STAGE2_FALSE_POSITIVE_TURNAROUND_BROKERAGE | 001290 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive_if_turnaround_brokerage_vocabulary_overcredited | True | True |
| R4L97_C17_PKC_2024_STAGE2_ACTIONABLE_CHLORALKALI_SEMICON_CHEMICAL_MARGIN_BRIDGE | 001340 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R4L89_C17_001340_20240522_STAGE2_CHLOR_ALKALI_SPREAD | 001340 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_correct_if_spread_ASP_margin_cash_bridge_required | True | True |
| None | 001340 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | True | True |
| C15-FERT-002_TRIGGER | 001390 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive | True | True |
| None | 001390 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| None | 001390 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| R1L93B_C01_001440_20240520_STAGE2_FALSE_POSITIVE_CABLE_PRICE_MFE | 001440 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_false_positive_if_cable_theme_price_MFE_overcredited_without_margin_cash_and_CA_repair | True | True |
| TRG_R1L80-C02-001440-DAEHAN-CABLE-POST-CA-GRID-CAPEX-BACKLOG | 001440 | C02_POWER_GRID_DATACENTER_CAPEX | C02 should allow power-cable positives when grid/datacenter capex maps to cable order backlog, export/customer quality, delivery schedule, revenue recognition and margin bridge. Daehan Cable produced a very large post-CA MFE, but runtime promotion requires post-CA continuity and source repair. | True | True |
| None | 001440 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| None | 001440 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| R13_CROSS_001440_2024-06-13_Stage4B | 001440 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| None | 001450 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | True | True |
| None | 001450 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | True | True |
| None | 001450 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | True | True |
| R6L86_C22_001450_20240124_STAGE2_PANDC_RESERVE_CAPITAL_RETURN | 001450 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_correct_if_reserve_capital_return_bridge_required | True | True |
| R6L92_C22_001450_20240129_STAGE2_PC_INSURANCE_RESERVE | 001450 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_correct_if_loss_ratio_reserve_capital_payout_bridge_required_but_Green_strict | True | True |
| None | 001450 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | True | True |
| R6L89_C22_HYUNDAIMARINE_2024_STAGE2_FALSE_POSITIVE_NONLIFE_RATE_RESERVE | 001450 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive_if_nonlife_rate_theme_counts_without_loss_ratio_reserve_capital_bridge | True | True |
| R6L93_C22_HYUNDAIMARINE_2024_STAGE2_FALSE_POSITIVE_NONLIFE_RESERVE_CYCLE_WATCH | 001450 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive_if_nonlife_reserve_cycle_watch_counts_without_loss_ratio_capital_return_revision_bridge | True | True |
| None | 001450 | C22_INSURANCE_RATE_CYCLE_RESERVE | Rate-cycle label alone should remain Stage2/watch; high MAE says actionable bonus is unsafe without explicit reserve/capital bridge. | True | True |
| R6L84_C22_001450_20240205_STAGE2_FALSE_POSITIVE_NONLIFE_VALUEUP_RESERVE_UNVERIFIED | 001450 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive_if_valueup_beta_overcredited | True | True |
| None | 001450 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | True | True |
| None | 001450 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | True | True |
| TRG_C22_R6L104_05 | 001450 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive | True | True |
| C22-R6-L101-06-T1 | 001450 | C22_INSURANCE_RATE_CYCLE_RESERVE | hard_4c_should_activate_after_reserve_loss_ratio_break_not_merely_late_price_weakness | True | True |
| None | 001450 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | False | True |
| None | 001450 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | None | True | True |
| C31_R11L106_TRG_17 | 001450 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | None | True | True |
| V12_COMPACT_001450_2024-08-20_policy_valueup_insurance_csm_reserve_capital_return_cash_bridge | 001450 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | True | True |
| R13L86_REVIEW_R6_C22_INSURANCE_RATE_CYCLE_RESERVE_001450_2024-01-24 | 001450 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_correct | True | True |
| R13L93_REVIEW_R6_C22_INSURANCE_RATE_CYCLE_RESERVE_001450_2024_02_05_TRIGGER | 001450 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_nonlife_reserve_cycle_watch_counts_without_loss_ratio_capital_return_revision_bridge | True | True |
| T_C05_R1L109_001470_20240201_POLITICAL_CONSTRUCTION_THEME_CONTAMINANT | 001470 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | True | True |
| None | 001470 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | True | True |
| R10L84_C30_001470_20240315_STAGE2_FALSE_POSITIVE_PF_THEME_BREAK | 001470 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive_if_theme_spike_overcredited | True | True |
| TRG_R10L82-C30-001470-SAMBU-SMALL-BUILDER-HIGHMAE-SHARECOUNT-STATUS | 001470 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should escalate small-builder/PF risk to local 4B when the price path shows severe MAE and persistent drawdown, but hard 4C still requires non-price refinancing failure, default, impairment, covenant, auditor/control or solvency evidence. Sambu also requires share-count and status continuity validation. | True | True |
| TRG_R10L76-C30-001470-SAMBU-CONSTRUCTION-FINANCING-RISK-LOCAL4B | 001470 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should flag local 4B when a builder/financing-risk row produces a high-MFE but then opens severe MAE and post-peak drawdown. Sambu Construction had a tradable spike but later collapsed; however hard 4C still requires non-price default, refinancing, auditor/control, impairment, covenant or solvency evidence. | True | True |
| TRG_R10L76-C30-001470-SAMBU-CONSTRUCTION-FINANCING-RISK-LOCAL4B | 001470 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive | True | True |
| R10L89_C30_SAMBU_2024_STAGE4B_POLITICAL_CONSTRUCTION_EVENT_CAP | 001470 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_4B_too_late_if_political_construction_event_premium_not_capped | True | True |
| None | 001470 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | True | True |
| R13_CROSS_001470_2024-01-05_Stage4C-HardBalanceSheetBreak | 001470 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive | True | True |
| R13L89_REVIEW_C30_SAMBU_2024_STAGE4B_POLITICAL_CONSTRUCTION_EVENT_CAP | 001470 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_4B_too_late_if_political_construction_event_premium_not_capped | True | True |
| None | 001500 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | True | True |
| R6L90_C21_SKSEC_2024_STAGE2_FALSE_POSITIVE_SMALL_BROKERAGE_VALUEUP | 001510 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive_if_small_brokerage_valueup_theme_counts_without_ROE_capital_return_revision_bridge | True | True |
| TRG_R6L81-C21-001510-SK-SECURITIES-SMALL-BROKERAGE-THEME-FADE | 001510 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | C21 should not treat small brokerage value-up theme beta as durable Stage2 unless ROE improvement, payout policy, trading-volume sensitivity, capital buffer and earnings bridge are visible. SK Securities had a small early MFE and then a persistent MAE path. | True | True |
| R6L89_C21_001510_20240201_STAGE2_FALSE_POSITIVE_SMALL_BROKERAGE_REBOUND | 001510 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive_if_small_brokerage_rebound_overcredited | True | True |
| R13L90_REVIEW_R6_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_001510_2024_02_01_TRIGGER | 001510 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive_if_small_brokerage_valueup_theme_counts_without_ROE_capital_return_revision_bridge | True | True |
| C15-FERT-003_TRIGGER | 001550 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive | True | True |
| R4L92_C16_001550_20240102_STAGE2_FALSE_POSITIVE_FERTILIZER_POLICY | 001550 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_false_positive_if_fertilizer_policy_vocabulary_overcredited | True | True |
| T_C13_R3L104_001570_STAGE2_20240226 | 001570 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | True | True |
| T_C13_R3L103_001570_STAGE4B_20240226 | 001570 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_false_positive_if_resource_battery_story_promoted_to_C13 | True | True |
| T_C13_R3L105_001570_STAGE4C_20240226 | 001570 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | True | True |
| T_C14_R3L108_001570_STAGE4B_20240226 | 001570 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_false_positive | True | True |
| TR_C16_GEUMYANG_S2_20230221 | 001570 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_4B_too_late | True | True |
| TRG_R4L81-C16-001570-KUMYANG-LITHIUM-RESOURCE-POLICY-THEME-FADE | 001570 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | C16 should not treat lithium/resource policy beta as durable Stage2 unless mine/supply availability, customer offtake, financing, permitting, revenue conversion and margin bridge are visible. Kumyang had a strong early spike, then a severe high-MAE fade. | True | True |
| C16-102-07-001570-T1 | 001570 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_4B_too_late | True | True |
| None | 001570 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| V12_COMPACT_R13L11-4B4C-009_001570_2024-02-26_cross_archetype_4b_4c_boundary_retest | 001570 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| V12_COMPACT_R13L12_ACCT_PRICE_06_C13_001570_20240226_001570_2024-02-26_Stage2 | 001570 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | True | True |
| V12_COMPACT_R13L12_ACCT_PRICE_05_C14_001570_20240226_001570_2024-02-26_Stage4B | 001570 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | True | True |
| V12_COMPACT_R13L2_C13_001570_20240226_STAGE2_001570_2024-02-26_cross_archetype_high_MAE_guardrail_review | 001570 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| R13_CROSS_001570_2024-02-26_Stage4B | 001570 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| T_R13_STAGE2FP_L5_001570_Stage2_2024-02-26 | 001570 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_stage2_false_positive_or_overpromotion_risk | True | True |
| R13_CROSS_001570_2024-02-26_Stage2 | 001570 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive | True | True |
| C20_R5L115_001680_20240201_INGREDIENT_FOOD_EXPORT_MIX_MARGIN_BRIDGE_Stage2_Actionable | 001680 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_undercredits_bridge_but_needs_high_MAE_guard | False | True |
| R13_L106_T17_001680 | 001680 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive | True | True |
| None | 001720 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | True | True |
| C31_R11L106_TRG_14 | 001720 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | None | True | True |
| C32_001740_20240215_STAGE2_ACTIONABLE | 001740 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive_or_overpromotion_risk | True | True |
| R6L90_C21_HANYANGSEC_2024_STAGE4B_BROKERAGE_CONTROL_PREMIUM_CAP | 001750 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_4B_too_late_if_brokerage_control_or_sale_event_premium_not_capped | True | True |
| TRG_R12L75-C32-001750-HANYANG-SECURITIES-CONTROL-SALE-PREMIUM-FADE | 001750 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive | True | True |
| R12L96_C32_HANYANGSEC_2024_STAGE2_ACTIONABLE_SECURITIES_SALE_CONTROL_PREMIUM_BRIDGE | 001750 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| TRG_R12L72-C32-001750-HANYANG-SECURITIES-SALE-PROCESS-CAP | 001750 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should support a sale-process Stage2 only when control-stake sale, buyer certainty and closing path are verified. The stock-web path had strong MFE but later reverted toward pre-event levels, so tender/sale-process cap logic is required. | True | True |
| TRG_R12L72-C32-001750-HANYANG-SECURITIES-SALE-PROCESS-CAP | 001750 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should support a sale-process Stage2 only when control-stake sale, buyer certainty and closing path are verified. The stock-web path had strong MFE but later reverted toward pre-event levels, so tender/sale-process cap logic is required. | True | True |
| TRG_R12L75-C32-001750-HANYANG-SECURITIES-CONTROL-SALE-PREMIUM-FADE | 001750 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should not treat a control-sale or preferred-bidder headline as durable Stage2 unless minority economics, tender floor, closing certainty or listed-shareholder beneficiary bridge is explicit. Hanyang Securities had a tradable MFE but then faded into local 4B risk. | True | True |
| R13L90_REVIEW_R6_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_001750_2024_08_05_TRIGGER | 001750 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_4B_too_late_if_brokerage_control_or_sale_event_premium_not_capped | True | True |
| R3L100-C14-007-T1 | 001780 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_missed_structural_if_EV_slowdown_blocks_lightweighting_component_recovery | True | True |
| TRG_R4L74-C15-001780-ALUKO-ALUMINUM-PRICE-BETA-LOCAL4B | 001780 | C15_MATERIAL_SPREAD_SUPERCYCLE | C15 should not treat aluminum or battery-material profile beta as Green unless product mix, customer order, spread and margin bridge are explicit. Aluko produced only small MFE and then severe late-2024 MAE, making it local 4B-watch rather than durable Stage2. | True | True |
| TRG_R4L74-C15-001780-ALUKO-ALUMINUM-PRICE-BETA-LOCAL4B | 001780 | C15_MATERIAL_SPREAD_SUPERCYCLE | C15 should not treat aluminum or battery-material profile beta as Green unless product mix, customer order, spread and margin bridge are explicit. Aluko produced only small MFE and then severe late-2024 MAE, making it local 4B-watch rather than durable Stage2. | True | True |
| R4L83_C15_001780_20240314_STAGE2_FALSE_POSITIVE_ALUMINUM_PRICE_SPIKE_ROUNDTRIP | 001780 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive | True | True |
| R10L93_C30_EWHACONST_2024_STAGE2_FALSE_POSITIVE_SMALL_BUILDER_PF_WATCH | 001840 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive_if_small_builder_PF_watch_counts_without_cashflow_order_quality_balance_bridge | True | True |
| R10L85_C30_001840_20240111_STAGE2_FALSE_POSITIVE_SMALLCAP_CONSTRUCTION_THEME | 001840 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive_if_construction_theme_overcredited | True | True |
| R13L93_REVIEW_R10_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_001840_2024_01_24_TRIGGER | 001840 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_small_builder_PF_watch_counts_without_cashflow_order_quality_balance_bridge | True | True |
| R13L85_REVIEW_R10_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_001840_2024-01-11 | 001840 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| R10L91_C30_002290_20240102_STAGE2_FALSE_POSITIVE_SMALL_CONSTRUCTION_POLICY | 002290 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive_if_small_construction_policy_vocabulary_overcredited | True | True |
| R10L94_C30_SAMIL_2024_STAGE4B_REGIONAL_BUILDER_POLICY_EVENT_CAP | 002290 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_4B_too_late_if_regional_builder_policy_event_premium_not_capped | True | True |
| R13L94_REVIEW_R10_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_002290_2024_01_24_TRIGGER | 002290 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_4B_too_late_if_regional_builder_policy_event_premium_not_capped | True | True |
| None | 002350 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | False | True |
| T_C29_R9L106_002350_20240223_11_Stage2 | 002350 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| T_C29_R9L104_002350_STAGE2_20240411 | 002350 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | True | True |
| R9L87_C29_NEXEN_2023_STAGE2_FALSE_POSITIVE_HIGH_MAE | 002350 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive_if_stage2_bonus_ignores_post_spike_mae | True | True |
| C29_R9L88_TRG_002350_S2 | 002350 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_correct_with_watch | True | True |
| R9L83_C29_002350_20240411_STAGE2_FALSE_POSITIVE_TIRE_MARGIN_ROUNDTRIP | 002350 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| R13L87_REVIEW_C29_NEXEN_2023_STAGE2_FALSE_POSITIVE_HIGH_MAE | 002350 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive_if_stage2_bonus_ignores_post_spike_mae | True | True |
| None | 002360 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | True | True |
| R13_CROSS_002360_2024-05-02_Stage2 | 002360 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive | True | True |
| R4L94_C17_KCC_2024_STAGE2_ACTIONABLE_SILICONE_PAINT_MATERIAL_MARGIN_BRIDGE | 002380 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R4L84_C17_002380_20240419_STAGE2_SILICONE_PAINT_MARGIN_BRIDGE | 002380 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_correct_if_margin_bridge_required | True | True |
| None | 002380 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | True | True |
| T_C05_R1L109_002410_20240715_THIN_BUILDER_PRICE_SPIKE | 002410 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | True | True |
| None | 002410 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | True | True |
| R10L85_C30_002410_20240102_STAGE2_FALSE_POSITIVE_PF_RELIEF_THEME | 002410 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive_if_PF_relief_theme_overcredited | True | True |
| R10L92_C30_BUMYANG_2024_STAGE4B_SMALL_BUILDER_PF_EVENT_CAP | 002410 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_4B_too_late_if_small_builder_PF_event_premium_not_capped | True | True |
| TRG_R10L74-C30-002410-BUMYANG-PF-LIQUIDITY-LOCAL4B-SEVERE | 002410 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should catch severe small-builder PF/liquidity/local 4B risk when MAE and drawdown become large, but hard 4C still needs non-price proof. Bumyang Construction shows the price-path severity that should raise local 4B-watch, not a price-only hard 4C. | True | True |
| TRG_R10L77-C30-002410-BEOMYANG-BUILDER-FINANCING-HIGH-MAE-LOCAL4B | 002410 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should flag local 4B when a small-builder/PF-financing row opens severe MAE and persistent drawdown, but hard 4C still requires non-price default, refinancing failure, court rehabilitation, impairment, covenant or solvency evidence. Beomyang Construction produced minimal MFE and then a deep drawdown path. | True | True |
| TRG_R10L80-C30-002410-BEOMYANG-E&C-PF-HIGHMAE-LOCAL4B | 002410 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should flag local 4B when small-builder/PF fear aligns with persistent high MAE and weak recovery, but hard 4C still requires non-price refinancing failure, default, covenant, impairment, auditor/control or solvency evidence. | True | True |
| TRG_R10L77-C30-002410-BEOMYANG-BUILDER-FINANCING-HIGH-MAE-LOCAL4B | 002410 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive | True | True |
| TRG_R10L74-C30-002410-BUMYANG-PF-LIQUIDITY-LOCAL4B-SEVERE | 002410 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should catch severe small-builder PF/liquidity/local 4B risk when MAE and drawdown become large, but hard 4C still needs non-price proof. Bumyang Construction shows the price-path severity that should raise local 4B-watch, not a price-only hard 4C. | True | True |
| R13L85_REVIEW_R10_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_002410_2024-01-02 | 002410 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| R13L92_REVIEW_R10_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_002410_2024_01_02_TRIGGER | 002410 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_4B_too_late_if_small_builder_PF_event_premium_not_capped | True | True |
| T_C05_R1L109_002460_20240522_REGIONAL_BUILDER_CASH_BRIDGE_PARTIAL | 002460 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | True | True |
| None | 002460 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | True | True |
| R10L90_C30_HSWHASUNG_2024_STAGE2_FALSE_POSITIVE_REGIONAL_CONSTRUCTION | 002460 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive_if_regional_construction_beta_counts_without_PF_cashflow_balance_bridge | True | True |
| R10L88_C30_002460_20240205_STAGE2_FALSE_POSITIVE_REGIONAL_CONSTRUCTION | 002460 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive_if_regional_construction_rebound_overcredited | True | True |
| R13L88_REVIEW_R10_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_002460_2024-02-05 | 002460 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R13L90_REVIEW_R10_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_002460_2024_02_01_TRIGGER | 002460 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive_if_regional_construction_beta_counts_without_PF_cashflow_balance_bridge | True | True |
| T_C11_R3L107_002710_STAGE2_20240206 | 002710 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_needs_high_MAE_guard_before_green | True | True |
| TRG_R3L77-C11-002710-TCCSTEEL-BATTERY-CAN-MATERIAL-ORDERBOOK-LIFECYCLE | 002710 | C11_BATTERY_ORDERBOOK_RERATING | C11 can include battery-can/component material names when customer orderbook, capacity ramp, quality approval and margin bridge are visible. TCC Steel produced very large early MFE, but the later high-MAE collapse says C11 must lifecycle-manage the signal and activate local 4B when orderbook/margin evidence fades. | True | True |
| TRG_R3L77-C11-002710-TCCSTEEL-BATTERY-CAN-MATERIAL-ORDERBOOK-LIFECYCLE | 002710 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_correct | True | True |
| R3L90_C12_TCCSTEEL_2024_STAGE2_ACTIONABLE_BATTERY_CAN_CUSTOMER_CONTRACT_BRIDGE | 002710 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| T_C13_R3L103_002710_STAGE2_20240206 | 002710 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_needs_local_4b_cap_for_battery_can_metal_spike | True | True |
| C13_R3L102_02_002710_20240130_T1 | 002710 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_data_insufficient | True | True |
| T_C13_R3L105_002710_STAGE3YELLOW_20240206 | 002710 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | True | True |
| T_C13_R3L104_002710_STAGE4B_20240206 | 002710 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | True | True |
| T_C14_R3L108_002710_STAGE3YELLOW_20240206 | 002710 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_false_positive | True | True |
| T_C05_R1L109_002780_20240314_SMALL_BUILDER_BALANCE_SHEET_LABEL | 002780 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | True | True |
| None | 002780 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | True | True |
| R10L92_C30_CHINHUNG_2024_STAGE2_FALSE_POSITIVE_REGIONAL_BUILDER_PF_WATCH | 002780 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive_if_regional_builder_PF_watch_counts_without_cashflow_order_quality_balance_bridge | True | True |
| R10L84_C30_002780_20240409_STAGE2_FALSE_POSITIVE_RELIEF_SPIKE | 002780 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive_if_relief_rally_overcredited | True | True |
| TRG_R10L81-C30-002780-JINHEUNG-SMALL-BUILDER-HIGHMAE-LOCAL4B | 002780 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should escalate small-builder/PF risk to local 4B when the path has little durable MFE and large 180D MAE, but hard 4C still needs non-price refinancing failure, default, impairment, covenant, auditor/control or solvency evidence. | True | True |
| R13L92_REVIEW_R10_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_002780_2024_02_26_TRIGGER | 002780 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive_if_regional_builder_PF_watch_counts_without_cashflow_order_quality_balance_bridge | True | True |
| R5L95_C20_AMOREG_2024_STAGE2_ACTIONABLE_KBEAUTY_HOLDCO_CHANNEL_MARGIN_BRIDGE | 002790 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| C32_002790_20240517_STAGE2_ACTIONABLE | 002790 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive_or_overpromotion_risk | True | True |
| T_C05_R1L109_002990_20240403_BUILDER_LABEL_HIGH_MAE | 002990 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | True | True |
| None | 002990 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | True | True |
| TRG_C30_R10L100_002990_STAGE2_FALSE_20240125 | 002990 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive | False | True |
| TRG_R10L74-C30-002990-KUMHO-PF-LIQUIDITY-ORDERBOOK-LOCAL4B | 002990 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 local 4B-watch should fire when mid-builder PF/orderbook/liquidity risk produces weak MFE and persistent MAE, but hard 4C still requires explicit non-price default, refinancing failure, court rehabilitation, auditor/control or solvency break. | True | True |
| TRG_R10L78-C30-002990-KUMHO-E&C-SMALLBUILDER-HIGH-MAE-LOCAL4B | 002990 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should flag local 4B when construction/PF fear aligns with persistent MAE and drawdown, but hard 4C still requires non-price refinancing failure, default, covenant, impairment, auditor/control or solvency evidence. Kumho E&C produced almost no MFE and then a deep drawdown path. | True | True |
| TRG_R10L74-C30-002990-KUMHO-PF-LIQUIDITY-ORDERBOOK-LOCAL4B | 002990 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 local 4B-watch should fire when mid-builder PF/orderbook/liquidity risk produces weak MFE and persistent MAE, but hard 4C still requires explicit non-price default, refinancing failure, court rehabilitation, auditor/control or solvency break. | True | True |
| R4L93_C15_SEAHSTEELHOLDINGS_2024_STAGE2_ACTIONABLE_STEEL_PIPE_EXPORT_SPREAD_MARGIN | 003030 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| C32_003030_20240207_STAGE2_ACTIONABLE | 003030 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive_or_overpromotion_risk | True | True |
| R12L90_C32_003030_20240102_STAGE2_FALSE_POSITIVE_STEEL_HOLDCO_NAV | 003030 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive_if_NAV_discount_vocabulary_overcredited | True | True |
| T_C05_R1L109_003070_20240612_POST_PEAK_HIGH_MAE_BUILDER_SPIKE | 003070 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | True | True |
| TRG_R10L77-C30-003070-KOLON-GLOBAL-PF-RISKWATCH-RECOVERY-NO-HARD4C | 003070 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should not over-convert builder/PF fear into hard 4C when price produces a recovery spike and MAE remains bounded. Kolon Global still needs PF/orderbook/liquidity monitoring, but the price path is a RiskWatch/no-hard-4C boundary unless non-price refinancing or solvency evidence breaks. | True | True |
| TRG_R10L79-C30-003070-KOLON-GLOBAL-PF-RECOVERY-SPIKE-NO-HARD4C | 003070 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should not over-convert builder/PF fear into hard 4C when the path produces a strong recovery spike. Kolon Global needs PF/orderbook/liquidity monitoring, but price action alone is not confirmed balance-sheet break evidence. | True | True |
| TRG_R10L77-C30-003070-KOLON-GLOBAL-PF-RISKWATCH-RECOVERY-NO-HARD4C | 003070 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive | True | True |
| None | 003070 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | True | True |
| R10L91_C30_KOLONGLOBAL_2024_STAGE2_ACTIONABLE_MID_BUILDER_PF_ORDER_RECOVERY | 003070 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R10L86_C30_003070_20240620_STAGE2_FALSE_POSITIVE_POLICY_SPIKE | 003070 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive_if_policy_spike_overcredited | True | True |
| R13L86_REVIEW_R10_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_003070_2024-06-20 | 003070 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| TRG_R2L80-C07-003160-DI-HBM-TEST-EQUIPMENT-RS-ORDER-BRIDGE | 003160 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | C07 should protect HBM/test-equipment positives when relative strength maps to equipment order, customer capacity, delivery schedule, revenue recognition and margin bridge. DI produced a very large MFE with controlled entry-basis MAE, but the post-peak drawdown means source-repaired lifecycle 4B is still needed. | True | True |
| R2L98_C07_DI_2024_STAGE2_ACTIONABLE_HBM_TEST_EQUIPMENT_ORDER_RS_BRIDGE | 003160 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R2L93_C10_DI_2024_STAGE2_ACTIONABLE_MEMORY_TESTER_EQUIPMENT_RECOVERY | 003160 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R5L94_C18_SAMYANGFOODS_2024_STAGE2_ACTIONABLE_KFOOD_EXPORT_REORDER_CHANNEL_MARGIN | 003230 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R5L99_C18_SAMYANGFOODS_2024_STAGE2_ACTIONABLE_K_FOOD_EXPORT_REORDER_MARGIN_BRIDGE | 003230 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R5L86_C18_003230_20240216_STAGE2_KFOOD_EXPORT_REORDER_BRIDGE | 003230 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_correct_if_export_reorder_bridge_required | True | True |
| None | 003230 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | True | True |
| R5L88_C20_SAMYANG_2024_STAGE2_ACTIONABLE_KFOOD_EXPORT_REORDER | 003230 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R5L83_C20_003230_20240409_STAGE2_KFOOD_REPEAT_EXPORT | 003230 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_correct | True | True |
| None | 003230 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | None | False | True |
| R5L88_C20_KFOOD_GLOBAL_REORDER_001 | 003230 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | None | False | True |
| C20_R5L116_003230_20240417_Stage3_Yellow | 003230 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_too_late | True | True |
| C20_R5_L102_T03_003230 | 003230 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_too_late | True | True |
| R13L86_REVIEW_R5_C18_CONSUMER_EXPORT_CHANNEL_REORDER_003230_2024-02-16 | 003230 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_correct | True | True |
| None | 003230 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| None | 003230 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| None | 003230 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| None | 003230 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| None | 003230 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| R13L83_HIGHMAE_REVIEW_003230_2024-04-09 | 003230 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_correct | True | True |
| None | 003230 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | None | True | True |
| None | 003240 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | True | True |
| R12L90_C32_TAEKWANG_2024_STAGE2_ACTIONABLE_GOVERNANCE_CAPITAL_ALLOCATION_BRIDGE | 003240 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R5L91_C20_003350_20240415_STAGE2_KBEAUTY_EXPORT_MANUFACTURING | 003350 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_correct_if_export_channel_reorder_margin_cash_bridge_required | True | True |
| R5L95_C20_HANKOOKCOSMETICSMFG_2024_STAGE4B_COSMETICS_ODM_EXPORT_EVENT_CAP | 003350 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_4B_too_late_if_cosmetics_ODM_export_event_premium_not_capped | True | True |
| R13L95_REVIEW_R5_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_003350_2024_09_03_TRIGGER | 003350 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late_if_cosmetics_ODM_export_event_premium_not_capped | True | True |
| TRG_R12L76-C32-003410-SSANGYONGCNE-VOLUNTARY-DELISTING-TENDER-FLOOR | 003410 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive | True | True |
| TRG_R12L76-C32-003410-SSANGYONGCNE-VOLUNTARY-DELISTING-TENDER-FLOOR | 003410 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should allow tender-floor lifecycle candidates when minority shareholders have explicit tender mechanics, floor price, closing path and direct economic beneficiary mapping. Ssangyong C&E produced a low-MAE tender-floor move and then price pinning, but this is not an operating Green; it is a governance-event floor trade that ends when tender mechanics complete. | True | True |
| R6L92_C21_YUANTA_2024_STAGE2_FALSE_POSITIVE_BROKERAGE_VALUEUP_THEME | 003470 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive_if_brokerage_valueup_theme_counts_without_ROE_capital_return_revision_bridge | True | True |
| R13L92_REVIEW_R6_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_003470_2024_02_19_TRIGGER | 003470 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive_if_brokerage_valueup_theme_counts_without_ROE_capital_return_revision_bridge | True | True |
| T_C03_R1L108_003490_20240306_STAGE2 | 003490 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current profile can over-promote defense beta unless sovereign funded backlog, delivery schedule and margin/cash bridge are verified | True | True |
| T_C03_R1L107_003490_20240306_STAGE2 | 003490 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | defense_MRO_or_aircraft_label_is_parent_airline_contaminant_unless_contract_backlog_margin_bridge_dominates | True | True |
| T_C32_R12L106_003490_20240126_Stage2 | 003490 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | regulatory closing may help the business, but it is not a C32 control premium cash event for minority holders | True | True |
| R6L98_C21_HANWHAINVEST_2024_STAGE4B_BROKERAGE_DIGITAL_ASSET_EVENT_CAP | 003530 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_4B_too_late_if_brokerage_digital_asset_event_premium_not_capped | True | True |
| R6L88_C21_HANWHAINV_2024_STAGE4B_DIGITAL_BROKERAGE_THEME_CAP | 003530 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive_if_digital_finance_theme_spike_counts_as_capital_return_rerating | True | True |
| None | 003540 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | True | True |
| None | 003540 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | False | True |
| C31_R11L106_TRG_13 | 003540 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | None | True | True |
| TRG_R11L82-C32-003550-LG-HOLDCO-VALUEUP-BOUNDED-NO-FORCED4B | 003550 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should not force bounded holding-company value-up rows into 4B when no non-price event break is confirmed, but it also should not call durable Stage2 without explicit event mechanics, NAV bridge, shareholder process and downside cap. LG is a bounded RiskWatch/no-forced-4B row. | True | True |
| C32_003550_LG_20240207_S2A | 003550 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_stage3_too_early_without_capital_return_bridge | True | True |
| C32_003550_20240814_STAGE2_ACTIONABLE | 003550 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive_or_overpromotion_risk | True | True |
| R11L83_C32_003550_20240201_STAGE2_VALUEUP_HOLDCO_NO_DURABLE_BRIDGE | 003550 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive | True | True |
| TRG_R11L77-C03-003570-SNT-DYNAMICS-DEFENSE-DRIVETRAIN-EXPORT-BACKLOG | 003570 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | C03 should allow defense component suppliers when export framework demand maps to drivetrain/transmission backlog, delivery schedule and margin bridge. SNT Dynamics produced large MFE with almost no entry-basis MAE, but lifecycle local 4B is still required if export/backlog/margin evidence fades. | True | True |
| TRG_R1L74-C03-003570-SNT-DYNAMICS-POWERTRAIN-EXPORT-BACKLOG | 003570 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | C03 should include defense powertrain and transmission suppliers when export programs convert into backlog and margin. SNT Dynamics produced a strong 180D MFE with very controlled entry MAE, but later drawdown after the October peak requires lifecycle local 4B if backlog/margin evidence fades. | True | True |
| TRG_R11L77-C03-003570-SNT-DYNAMICS-DEFENSE-DRIVETRAIN-EXPORT-BACKLOG | 003570 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_correct | True | True |
| TRG_R1L74-C03-003570-SNT-DYNAMICS-POWERTRAIN-EXPORT-BACKLOG | 003570 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | C03 should include defense powertrain and transmission suppliers when export programs convert into backlog and margin. SNT Dynamics produced a strong 180D MFE with very controlled entry MAE, but later drawdown after the October peak requires lifecycle local 4B if backlog/margin evidence fades. | True | True |
| T_C03_R1L108_003570_20240522_STAGE2_ACTIONABLE | 003570 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current profile can over-promote defense beta unless sovereign funded backlog, delivery schedule and margin/cash bridge are verified | True | True |
| None | 003570 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | None | False | True |
| R9L88_C29_KGMOBILITY_2024_STAGE2_FALSE_POSITIVE_OEM_REBOUND | 003620 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive_if_OEM_rebound_counts_without_volume_mix_margin_cashflow_bridge | True | True |
| R9L85_C29_003620_20240423_STAGE2_FALSE_POSITIVE_OEM_TURNAROUND | 003620 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive_if_OEM_turnaround_theme_overcredited | True | True |
| T_C29_R9L106_003620_20240319_14_Stage4C | 003620 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| R13L88_REVIEW_C29_KGMOBILITY_2024_STAGE2_FALSE_POSITIVE_OEM_REBOUND | 003620 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_OEM_rebound_counts_without_volume_mix_margin_cashflow_bridge | True | True |
| R13L85_REVIEW_R9_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_003620_2024-04-23 | 003620 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| None | 003650 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | True | True |
| TRG-C11-003670-20250203-STAGE4B | 003670 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_error_if_hard_4c_without_orderbook_cancellation | False | True |
| V12_COMPACT_C12_R3L105_003670_20240503_05_003670_2024-05-03_Stage2-Actionable | 003670 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_false_positive | True | True |
| R3L83_C12_003670_20240322_STAGE2_FALSE_POSITIVE_ORDERBOOK_CALLOFF | 003670 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_false_positive | True | True |
| None | 003670 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | True | True |
| R13_CROSS_003670_2024-04-25_Stage4B-Local-CathodeCustomerCallOffRisk | 003670 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_false_positive | True | True |
| None | 003670 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | True | True |
| R3L93_C13_003670_20240125_STAGE2_CATHODE_JV_UTILIZATION_IRA | 003670 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_correct_if_JV_utilization_IRA_margin_FCF_bridge_required_but_Green_strict | True | True |
| V12_COMPACT_C13-102-04_003670_2024-02-15_Stage3-Yellow | 003670 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_false_positive | True | True |
| None | 003670 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | True | True |
| R3L98_C14_POSCOFUTUREM_2024_STAGE4B_CATHODE_DEMAND_SLOWDOWN_EVENT_CAP | 003670 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_4B_too_late_if_cathode_demand_recovery_event_premium_not_capped | True | True |
| R3L100-C14-001-T1 | 003670 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_too_late_if_cathode_orderbook_memory_blocks_demand_reset_4C | True | True |
| None | 003670 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| C31_L101_T005_003670 | 003670 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | True | True |
| None | 003690 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | True | True |
| None | 003690 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | True | True |
| TRG_R6L76-C22-003690-KOREANRE-REINSURANCE-RESERVE-CAPITAL-RETURN | 003690 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive | True | True |
| None | 003690 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | True | True |
| TRG_R6L74-C22-003690-KOREANRE-REINSURANCE-CYCLE-CAPITAL-BUFFER | 003690 | C22_INSURANCE_RATE_CYCLE_RESERVE | C22 should include reinsurers when pricing cycle, reserve adequacy and capital buffer translate into low-MAE rerating. Korean Re produced slow but durable MFE; however a late-2024 share-count change in the shard requires validation before runtime promotion. | True | True |
| None | 003690 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | True | True |
| R13_CROSS_003690_2024-02-01_Stage2-Actionable-ReinsuranceRateCycle | 003690 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive | True | True |
| TRG_R6L74-C22-003690-KOREANRE-REINSURANCE-CYCLE-CAPITAL-BUFFER | 003690 | C22_INSURANCE_RATE_CYCLE_RESERVE | C22 should include reinsurers when pricing cycle, reserve adequacy and capital buffer translate into low-MAE rerating. Korean Re produced slow but durable MFE; however a late-2024 share-count change in the shard requires validation before runtime promotion. | True | True |
| None | 003690 | C22_INSURANCE_RATE_CYCLE_RESERVE | Stable low-MAE profile can support watch/actionable, but weak MFE says not enough for Yellow unless ROE and capital-return bridge improves. | True | True |
| R6L99_C22_KOREANRE_2024_STAGE2_FALSE_POSITIVE_REINSURANCE_RATE_RESERVE_WATCH | 003690 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive_if_reinsurance_rate_reserve_watch_counts_without_reserve_quality_combined_ratio_capital_return_revision_bridge | True | True |
| C22-R6-L101-01-T1 | 003690 | C22_INSURANCE_RATE_CYCLE_RESERVE | residual_missed_structural_underweighted_reinsurance_rate_reserve_bridge | True | True |
| TRG_R6L76-C22-003690-KOREANRE-REINSURANCE-RESERVE-CAPITAL-RETURN | 003690 | C22_INSURANCE_RATE_CYCLE_RESERVE | C22 should preserve reinsurance reserve/capital-return rows when underwriting cycle, reinsurance rate hardening, reserve adequacy, K-ICS buffer and shareholder-return bridge are visible. Korean Re produced slow low-MAE rerating, not explosive beta; the model should not overblock these compounding C22 rows. | True | True |
| TRG_R6L82-C22-003690-KOREAN-RE-REINSURANCE-RATE-CYCLE-CAPITAL-RETURN | 003690 | C22_INSURANCE_RATE_CYCLE_RESERVE | C22 should allow reinsurance positives when rate-cycle pricing, reserve adequacy, loss ratio, capital buffer, shareholder return and ROE/PBR bridge are visible. Korean Re had controlled entry-basis MAE and steady later MFE, so it is a protected positive after source repair. | True | True |
| None | 003690 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | True | True |
| TRG_C22_R6L104_03 | 003690 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_missed_structural | True | True |
| None | 003690 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | True | True |
| V12_COMPACT_003690_2024-04-26_policy_valueup_insurance_csm_reserve_capital_return_cash_bridge | 003690 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | True | True |
| R7L92_C23_BORYUNG_2024_STAGE2_FALSE_POSITIVE_PHARMA_COMMERCIALIZATION_CHANNEL | 003850 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive_if_pharma_commercialization_channel_counts_without_approval_reimbursement_revision_bridge | True | True |
| R13L92_REVIEW_R7_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_003850_2024_03_20_TRIGGER | 003850 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive_if_pharma_commercialization_channel_counts_without_approval_reimbursement_revision_bridge | True | True |
| None | 003920 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | True | True |
| TRG_R12L74-C32-003920-NAMYANG-CONTROL-TRANSFER-PREMIUM-CAP | 003920 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should not treat legal/control-transfer resolution as durable Green unless minority economics, tender floor, capital policy, operational turnaround or closing economics bridge is visible. Namyang had small MFE and persistent MAE before the later share-split/corporate-action area, so it is a control-transfer premium-cap counterexample. | True | True |
| TRG_R12L74-C32-003920-NAMYANG-CONTROL-TRANSFER-PREMIUM-CAP | 003920 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should not treat legal/control-transfer resolution as durable Green unless minority economics, tender floor, capital policy, operational turnaround or closing economics bridge is visible. Namyang had small MFE and persistent MAE before the later share-split/corporate-action area, so it is a control-transfer premium-cap counterexample. | True | True |
| None | 003920 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | None | True | True |
| R12L87_C32_NAMYANG_2021_STAGE4B_CONTROL_SALE_EVENT_CAP | 003920 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_4B_too_late_if_control_premium_cap_not_detected | True | True |
| R13L87_REVIEW_C32_NAMYANG_2021_STAGE4B_CONTROL_SALE_EVENT_CAP | 003920 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_4B_too_late_if_control_premium_cap_not_detected | True | True |
| R5_L122_C18_018 | 003960 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | True | True |
| C19_R5L119_14_003960_4B_Local_Watch_2024-06-17 | 003960 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | True | True |
| C20_R5L115_003960_20240201_SEAFOOD_PROCESSED_FOOD_MIX_EXPORT_BRIDGE_Stage2_Actionable | 003960 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_undercredits_mix_bridge_but_needs_peak_guard | False | True |
| C20_R5L119_003960_20240617_09_Stage4B_Local_Watch | 003960 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | None | True | True |
| C20_R5L118_003960_20240617_Stage4B | 003960 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_error | True | True |
| T_C15_R4L105_004000_20240516_10_Stage2-Actionable | 004000 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive | True | True |
| TRG_R4L82-C17-004000-LOTTE-FINE-CHEM-CHLOR-ALKALI-BOUNDED-RISKWATCH | 004000 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | C17 should not force bounded chemical spread rows into 4B when no non-price margin break is confirmed, but it also should not call durable Stage2 without spread recovery, volume, pricing and margin bridge. Lotte Fine Chemical is a bounded RiskWatch row. | True | True |
| None | 004000 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | True | True |
| R4L93_C17_004000_20240102_STAGE2_FALSE_POSITIVE_CHLORALKALI_AMMONIA | 004000 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive_if_chloralkali_ammonia_spread_vocabulary_overcredited | True | True |
| TRG_R4L80-C15-004020-HYUNDAI-STEEL-SPREAD-MARGIN-FADE | 004020 | C15_MATERIAL_SPREAD_SUPERCYCLE | C15 should not treat steel spread beta as durable Stage2 unless HRC/rebar/auto steel volume, utilization, raw-material spread, price pass-through and margin bridge are visible. Hyundai Steel produced modest MFE and then a high-MAE downtrend. | True | True |
| C15_R4L89_HYUNDAISTEEL_20240207 | 004020 | C15_MATERIAL_SPREAD_SUPERCYCLE | None | False | True |
| C15_R4L89_HYUNDAISTEEL_20240207 | 004020 | C15_MATERIAL_SPREAD_SUPERCYCLE | None | False | True |
| R12L85_C31_004020_20240129_STAGE2_FALSE_POSITIVE_CYCLICAL_VALUEUP_THEME | 004020 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive_if_policy_lowPBR_theme_overcredited | True | True |
| R13L85_REVIEW_R12_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_004020_2024-01-29 | 004020 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| T_R13_STAGE2FP_L6_004020_Stage2_2024-02-07 | 004020 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_stage2_false_positive_or_overpromotion_risk | True | True |
| TRG_R4L78-C16-004090-KOREA-PETROLEUM-OIL-SUPPLY-SECURITY-LIFECYCLE | 004090 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | C16 can allow oil/resource-security rows when geopolitical supply shock maps to product pricing, inventory, demand and margin bridge. Korea Petroleum produced a very large MFE with controlled entry-basis MAE, but later post-peak drawdown requires lifecycle local 4B if supply/inventory/margin evidence fades. | True | True |
| R4L94_C17_KOREAPETROLEUM_2024_STAGE4B_OIL_PRODUCT_SPREAD_EVENT_CAP | 004090 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_4B_too_late_if_oil_product_spread_event_premium_not_capped | True | True |
| TRG_R11L74-C31-004090-KOREA-PETROLEUM-POLICY-THEME-BETA-FADE | 004090 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should not treat oil/gas policy attention as a durable Stage2 signal for an oil-product proxy without direct concession, supply, infrastructure, procurement or earnings bridge. Korea Petroleum produced strong event MFE but later opened high MAE and a large post-peak drawdown. | True | True |
| TRG_R11L74-C31-004090-KOREA-PETROLEUM-POLICY-THEME-BETA-FADE | 004090 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should not treat oil/gas policy attention as a durable Stage2 signal for an oil-product proxy without direct concession, supply, infrastructure, procurement or earnings bridge. Korea Petroleum produced strong event MFE but later opened high MAE and a large post-peak drawdown. | True | True |
| R12L87_C31_004090_20240604_STAGE2_FALSE_POSITIVE_OIL_POLICY_BLOWOFF | 004090 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive_if_policy_theme_blowoff_overcredited | True | True |
| R13L87_REVIEW_R12_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_004090_2024-06-04 | 004090 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R13L94_REVIEW_R4_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_004090_2024_04_09_TRIGGER | 004090 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_4B_too_late_if_oil_product_spread_event_premium_not_capped | True | True |
| TRG_R5L74-C19-004170-SHINSEGAE-DS-MARGIN-RISKWATCH | 004170 | C19_BRAND_RETAIL_INVENTORY_MARGIN | C19 should distinguish stable department-store value-up from durable inventory/margin rerating. Shinsegae had early MFE but later MAE opened and the return path was not strong enough to qualify as durable Green without stronger traffic/duty-free/margin evidence. | True | True |
| SHINSEGAE_004170_2024_01_29_STAGE2A_RETAIL_MARGIN_STABLE | 004170 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_correct | False | True |
| R5L93_C19_004170_20240208_STAGE2_FALSE_POSITIVE_DEPARTMENT_STORE | 004170 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_false_positive_if_department_store_brand_inventory_vocabulary_overcredited | True | True |
| TRG_R5L74-C19-004170-SHINSEGAE-DS-MARGIN-RISKWATCH | 004170 | C19_BRAND_RETAIL_INVENTORY_MARGIN | C19 should distinguish stable department-store value-up from durable inventory/margin rerating. Shinsegae had early MFE but later MAE opened and the return path was not strong enough to qualify as durable Green without stronger traffic/duty-free/margin evidence. | True | True |
| TRG_C19_004170_20240219_DEPARTMENT_STORE_DUTYFREE_PRICE_ONLY_4B | 004170 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_4B_too_late | True | True |
| R5L92_C18_NONGSHIM_2024_STAGE2_ACTIONABLE_RAMEN_EXPORT_CHANNEL_REORDER | 004370 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| C18_R5L113_004370_20240528_Stage2_Actionable_2024-05-28 | 004370 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_too_late | False | True |
| Stage2-Actionable | 004370 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_too_late | False | True |
| C20_R5L115_004370_20240201_RAMEN_GLOBAL_REORDER_MARGIN_BRIDGE_Stage2_Actionable | 004370 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_too_late | False | True |
| C20_R5L118_004370_20240528_Stage2_Actionable | 004370 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_error | True | True |
| R5L91_C20_004370_20240614_STAGE2_FALSE_POSITIVE_FOOD_GLOBAL_POSTMOVE | 004370 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive_if_food_global_distribution_postmove_overcredited | True | True |
| R5L83_C20_004370_20240528_LOCAL4B_MATURE_BRAND_ROUNDTRIP | 004370 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_4B_too_late | True | True |
| T_C15_R4L105_004430_20240429_05_Stage2-Actionable | 004430 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive | True | True |
| T_C15_R4L105_004430_20240517_11_Stage2-Actionable | 004430 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive | True | True |
| R4L88_C15_004430_20240102_STAGE2_FALSE_POSITIVE_CHEM_SPREAD | 004430 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive_if_chemical_spread_rebound_overcredited | True | True |
| TRG_R4L76-C17-004430-SONGWON-INDUSTRIAL-ADDITIVE-SPREAD-FADE | 004430 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive | True | True |
| T_C17_R4L105_03_004430_Stage2Actionable_20240429 | 004430 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive | True | True |
| None | 004430 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | True | True |
| TRG_R4L82-C17-004430-SONGWON-INDUSTRIAL-ADDITIVE-MARGIN-FADE | 004430 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | C17 should not treat chemical additive or commodity spread theme beta as durable Stage2 unless customer volume, pricing power, input-cost pass-through, revenue and margin bridge are visible. Songwon Industrial had tiny early MFE and then high MAE before a late theme bounce. | True | True |
| TRG_R4L76-C17-004430-SONGWON-INDUSTRIAL-ADDITIVE-SPREAD-FADE | 004430 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | C17 should not treat specialty additive or commodity-spread beta as durable Stage2 unless order, inventory restocking, price-cost spread and margin evidence refreshes. Songwon Industrial had weak MFE and then opened a high-MAE drawdown path. | True | True |
| R13L88_REVIEW_R4_C15_MATERIAL_SPREAD_SUPERCYCLE_004430_2024-01-02 | 004430 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R9L89_C13_SEBANG_2024_STAGE2_ACTIONABLE_BATTERY_VOLUME_MARGIN_BRIDGE | 004490 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R9L87_C29_004490_20240202_STAGE2_AUTO_BATTERY_VOLUME_MARGIN | 004490 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_correct_if_volume_margin_bridge_required | True | True |
| R13L87_REVIEW_R9_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_004490_2024-02-02 | 004490 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_correct | True | True |
| R12L88_C32_004800_20240201_STAGE2_FALSE_POSITIVE_HOLDCO_RESTRUCTURING | 004800 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive_if_holdco_restructuring_theme_overcredited | True | True |
| R13L88_REVIEW_R12_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_004800_2024-02-01 | 004800 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| None | 004960 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | True | True |
| T_C05_R1L109_004960_20240328_SMALL_BUILDER_WORKING_CAPITAL_GUARD | 004960 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | True | True |
| T_C05_R1L108_004960_20240429_SMALL_BUILDER_COUNTER | 004960 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | True | True |
| TRG_R10L82-C30-004960-HANSHIN-BUILDER-BOUNDED-PF-RISKWATCH | 004960 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should not force bounded builder/PF watch rows into 4B when no refinancing, liquidity or solvency break is confirmed, but it also should not call durable Stage2 without orderbook, PF and margin recovery bridge. Hanshin Construction is a bounded RiskWatch row. | True | True |
| TRG_R10L78-C30-004960-HANSHIN-E&C-PF-RISKWATCH-BOUNDED-NO-HARD4C | 004960 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should keep PF/orderbook watch active for mid-builders, but bounded MAE and a non-collapsing price path should not become hard 4C without explicit refinancing, impairment, covenant, auditor/control or solvency break evidence. | True | True |
| TRG_R10L75-C30-004960-HANSHIN-BUILDER-RISKWATCH-NO-HARD4C | 004960 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive | True | True |
| None | 004960 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | True | True |
| C30_R10L104_004960_20240429_Stage2 | 004960 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive_if_stage2_actionable_bonus_overcredits_low_PBR | True | True |
| TRG_R10L75-C30-004960-HANSHIN-BUILDER-RISKWATCH-NO-HARD4C | 004960 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should keep PF/orderbook RiskWatch active for builders, but bounded MAE and recovery rows should not be escalated into hard 4C. Hanshin Construction shows PF fear but also rebound behavior; full 4B or hard 4C requires non-price break evidence. | True | True |
| TRG_R10L73-C30-004960-HANSHIN-PF-ORDERBOOK-LOCAL4B | 004960 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 local 4B-watch should fire when PF/orderbook/margin risk prevents a durable MFE path, even if the stock does not show a hard 4C collapse. 한신공영 is a local-risk boundary row: MAE opens and MFE is small, but full 4B/4C still needs explicit non-price deterioration. | True | True |
| TRG_R10L73-C30-004960-HANSHIN-PF-ORDERBOOK-LOCAL4B | 004960 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 local 4B-watch should fire when PF/orderbook/margin risk prevents a durable MFE path, even if the stock does not show a hard 4C collapse. 한신공영 is a local-risk boundary row: MAE opens and MFE is small, but full 4B/4C still needs explicit non-price deterioration. | True | True |
| R10L89_C30_004980_20240201_STAGE2_CEMENT_MARGIN_CASH | 004980 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_correct_if_materials_margin_cash_bridge_required | True | True |
| C32_004990_20240207_STAGE2_ACTIONABLE | 004990 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_correct_if_local4b_or_yellow_capped | True | True |
| R12L92_C32_LOTTEHOLDINGS_2024_STAGE2_FALSE_POSITIVE_HOLDCO_VALUEUP_THEME | 004990 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive_if_holdco_valueup_theme_counts_without_control_premium_capital_return_bridge | True | True |
| R12L86_C32_004990_20240201_STAGE2_FALSE_POSITIVE_HOLDCO_GOVERNANCE_REBOUND | 004990 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive_if_governance_rebound_overcredited | True | True |
| R12L84_C32_004990_20240201_STAGE2_FALSE_POSITIVE_HOLDCO_VALUEUP_THEME | 004990 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive_if_valueup_theme_overcredited | True | True |
| R13L86_REVIEW_R12_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_004990_2024-02-01 | 004990 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R13L92_REVIEW_R12_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_004990_2024_02_07_TRIGGER | 004990 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive_if_holdco_valueup_theme_counts_without_control_premium_capital_return_bridge | True | True |
| T_C11_R3L107_005070_STAGE4B_20240216 | 005070 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive_if_orderbook_label_is_overcredited | True | True |
| R3L93_C12_005070_20240220_STAGE2_FALSE_POSITIVE_CATHODE_CONTRACT_SPIKE | 005070 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_false_positive_if_cathode_customer_contract_vocabulary_overcredited | True | True |
| None | 005070 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | True | True |
| None | 005070 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_correct_if_hard_4c_requires_customer_pull_margin_break | True | True |
| None | 005070 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | True | True |
| COSMO_005070_2024_02_02_STAGE2A_CATHODE_CAPA_UTILIZATION | 005070 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_4B_too_late | False | True |
| T_C13_R3L103_005070_STAGE2ACTIONABLE_20240216 | 005070 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_too_late_if_mixed_asp_utilization_margin_bridge_visible | True | True |
| T_C13_R3L104_005070_STAGE3GREEN_20240216 | 005070 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | True | True |
| T_C13_R3L105_005070_STAGE4B_20240216 | 005070 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | True | True |
| COSMO_005070_2024_02_21_4C_EV_DEMAND_SLOWDOWN | 005070 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_4C_too_late | False | True |
| R5L96_C18_BINGGRAE_2024_STAGE2_ACTIONABLE_DAIRY_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE | 005180 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R5L89_C18_005180_20240415_STAGE2_KFOOD_EXPORT_REORDER | 005180 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_correct_if_export_reorder_sellthrough_margin_bridge_required | True | True |
| R5L84_C18_005180_20240415_STAGE2_KFOOD_EXPORT_REORDER_BRIDGE | 005180 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_correct_if_reorder_bridge_required | True | True |
| C18_R5L113_005180_20240517_Stage2_Actionable_2024-05-17 | 005180 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_too_late | False | True |
| Stage2-Actionable | 005180 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_too_late | False | True |
| None | 005180 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | True | True |
| C18_R5L113_005180_20240517_Stage4B_2024-06-11 | 005180 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_4B_too_late | False | True |
| C19_R5L120_01_005180_Stage3_Yellow_2024-04-17 | 005180 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | True | True |
| C20_R5L116_005180_20240517_Stage2_Actionable | 005180 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_undercredits_bridge_but_needs_high_MAE_guard | True | True |
| R5L88_C20_KFOOD_GLOBAL_REORDER_002 | 005180 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | None | False | True |
| C20_R5L119_005180_20240417_01_Stage3_Yellow | 005180 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | None | True | True |
| C20_R5_L102_T06_005180 | 005180 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_4B_too_late | True | True |
| C20_R5L116_005180_20240611_Stage4B | 005180 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive_if_price_only_4B_promoted | True | True |
| R5L88_C20_BINGGRAE_2024_STAGE4B_KFOOD_EXPORT_THEME_CAP | 005180 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_4B_too_late_if_export_theme_premium_not_capped | True | True |
| None | 005180 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| R2L85_C06_005290_20240321_STAGE2_FALSE_POSITIVE_SEMI_MATERIAL_BETA | 005290 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_false_positive_if_material_beta_overcredited | True | True |
| TRG-C06-L110-005290-Stage3Yellow-2024-03-22 | 005290 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_false_positive | True | True |
| DONGJIN_005290_2024_03_06_STAGE2_FALSE_POSITIVE_MEMORY_MATERIAL_BETA | 005290 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_false_positive | False | True |
| R13L85_REVIEW_R2_C06_HBM_MEMORY_CUSTOMER_CAPACITY_005290_2024-03-21 | 005290 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| T_R9L10_005380_STAGE2 | 005380 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_correct | False | True |
| T_C29_R9L105_005380_Stage2Actionable_20240125 | 005380 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| TRG_C29_R9L100_005380_STAGE2A_20240125 | 005380 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_too_late | False | True |
| T_C29_R9L106_005380_20240614_16_Stage3-Green | 005380 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_correct | True | True |
| T_C29_R9L106_005380_20240202_01_Stage3-Yellow | 005380 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_correct | True | True |
| None | 005380 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| None | 005380 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| None | 005380 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| R5_L122_C18_004 | 005390 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | True | True |
| None | 005390 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | True | True |
| None | 005390 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | False | True |
| C19_R5L119_04_005390_Stage2_Actionable_2024-02-02 | 005390 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | True | True |
| V12_COMPACT_C20_R5L120_005390_20240202_10_005390_2024-02-02_Stage2-Actionable | 005390 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | True | True |
| C14-R3L97-02-005420-Stage4C-2024-04-30 | 005420 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_correct | True | True |
| T_C15_R4L105_005420_20240226_12_4C | 005420 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive | True | True |
| TRG_R4L81-C16-005420-COSMO-CHEMICAL-COBALT-LITHIUM-RECOVERY-LIFECYCLE | 005420 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | C16 should allow strategic-resource recovery positives only when cobalt/lithium/nickel or recycling supply maps to customer volume, utilization, policy support, revenue and margin bridge. Cosmo Chemical produced a large early MFE, but the later high-MAE path requires lifecycle 4B if the bridge fades. | True | True |
| None | 005420 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| None | 005420 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | True | True |
| None | 005420 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | None | True | True |
| V12_COMPACT_C15-101-03_005490_2024-02-01_Stage2_FalsePositive | 005490 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive | True | True |
| T_C15_R4L103_005490_Stage2_20240201 | 005490 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive_or_wrong_archetype_if_material_label_overweighted | True | True |
| R4L100_C15_POSCOHOLDINGS_2024_STAGE2_FALSE_POSITIVE_LITHIUM_STEEL_SUPERCYCLE_WATCH | 005490 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive_if_lithium_steel_supercycle_watch_counts_without_realized_spread_volume_inventory_margin_revision_bridge | True | True |
| TRG_R4L80-C15-005490-POSCO-HOLDINGS-STEEL-LITHIUM-SPREAD-FADE | 005490 | C15_MATERIAL_SPREAD_SUPERCYCLE | C15 should not treat steel/lithium/resource beta as durable Stage2 unless steel spread, lithium resource economics, inventory, volume, pricing and margin bridge refreshes. POSCO Holdings had a tradable bounce but then opened a high-MAE drawdown path. | True | True |
| None | 005490 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| None | 005490 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| TR_C16_POSCO_S2A_20230410 | 005490 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_correct | True | True |
| None | 005490 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| None | 005490 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| T_C32_R12L106_005490_20240215_Stage2 | 005490 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | holdco/resource theme belongs to C15/C16 unless concrete minority-return bridge exists | True | True |
| None | 005490 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| None | 005490 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| R5_L122_C18_017 | 005610 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | True | True |
| None | 005610 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | True | True |
| R5L84_C18_005610_20240614_STAGE2_FALSE_POSITIVE_DOMESTIC_CHANNEL_SPIKE | 005610 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive_if_channel_spike_overcredited | True | True |
| R5L86_C18_005610_20240614_STAGE2_FALSE_POSITIVE_DOMESTIC_FOOD_REBOUND | 005610 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive_if_food_rebound_overcredited | True | True |
| R5L92_C18_SPCSAMLIP_2024_STAGE4B_BAKERY_CHANNEL_EVENT_CAP | 005610 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_4B_too_late_if_bakery_food_channel_event_premium_not_capped | True | True |
| C19_R5L119_13_005610_Stage2_2024-05-17 | 005610 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | True | True |
| C20_R5L118_005610_20240517_Stage2 | 005610 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_error | True | True |
| C20_R5L115_005610_20240517_BRAND_CHANNEL_BUZZ_LOCAL4B_CAP_Stage4B | 005610 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive_if_brand_buzz_promoted | False | True |
| C20_R5L119_005610_20240517_06_Stage4B_Local_Watch | 005610 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | None | True | True |
| R13L86_REVIEW_R5_C18_CONSUMER_EXPORT_CHANNEL_REORDER_005610_2024-06-14 | 005610 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R13L92_REVIEW_R5_C18_CONSUMER_EXPORT_CHANNEL_REORDER_005610_2024_06_14_TRIGGER | 005610 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_4B_too_late_if_bakery_food_channel_event_premium_not_capped | True | True |
| R9L92_C29_005710_20240129_STAGE2_FALSE_POSITIVE_SEAT_PARTS | 005710 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive_if_seat_parts_vocabulary_overcredited | True | True |
| R4L91_C15_005810_20240411_STAGE2_FALSE_POSITIVE_COPPER_HOLDCO | 005810 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive_if_copper_holdco_vocabulary_overcredited | True | True |
| T_C21_R6L104_005830_STAGE2ACTIONABLE_20240201 | 005830 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | True | True |
| None | 005830 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | True | True |
| None | 005830 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | True | True |
| TRG_C22_R6L104_01 | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_too_late | True | True |
| None | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | True | True |
| R6L41_C22_005830_T1_STAGE2A | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_correct | True | True |
| None | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | True | True |
| C22-R6-L101-04-T1 | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | too_optimistic_without_drawdown_guard_despite_later_recovery | True | True |
| None | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | False | True |
| R6L41_C22_005830_T2_GREEN_COMPARE | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_too_late | True | True |
| None | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | Yellow/watch is defensible, but Green needs fresh CSM/reserve/payout bridge rather than earlier value-up beta. | True | True |
| None | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | True | True |
| None | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | True | True |
| None | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | True | True |
| R6L41_C22_005830_T3_4B_FULL | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_correct | True | True |
| TRIG_C31_R11L100_003_005830 | 005830 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_correct | True | True |
| None | 005830 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | None | True | True |
| C31_R11L106_TRG_16 | 005830 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | None | True | True |
| V12_COMPACT_005830_2024-08-22_policy_valueup_insurance_csm_reserve_capital_return_cash_bridge | 005830 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_correct | True | True |
| None | 005850 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | False | True |
| C29_R9L87_TRG_005850_S2 | 005850 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_4B_too_late | True | True |
| TRG_R9L74-C29-005850-SL-AUTO-LIGHTING-ADAS-MARGIN | 005850 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should include lighting/ADAS suppliers when OEM mix, order cadence and margin conversion drive rerating. SL had strong MFE, but post-peak drawdown says lifecycle local 4B should fire if OEM mix or margin evidence fades. | True | True |
| TRG_R9L76-C29-005850-SL-LAMP-MODULE-OEM-MIX-MARGIN-BRIDGE | 005850 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should allow mobility supplier Stage2 when OEM program volume, lamp/module mix, pricing and margin bridge are visible. SL produced a large mid-year MFE with bounded entry-basis MAE, but the later drawdown requires lifecycle local 4B if volume/mix/margin evidence fades. | True | True |
| TRG_R9L76-C29-005850-SL-LAMP-MODULE-OEM-MIX-MARGIN-BRIDGE | 005850 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_correct | True | True |
| TRG_R9L79-C29-005850-SL-AUTO-LAMP-MIX-MARGIN-BRIDGE | 005850 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should allow auto lamp/electronics suppliers when customer program volume, product mix, pricing, utilization and margin bridge are visible. SL produced a large MFE with bounded MAE, but the post-peak drawdown requires lifecycle local 4B if volume/mix/margin evidence fades. | True | True |
| TRG_R9L74-C29-005850-SL-AUTO-LIGHTING-ADAS-MARGIN | 005850 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should include lighting/ADAS suppliers when OEM mix, order cadence and margin conversion drive rerating. SL had strong MFE, but post-peak drawdown says lifecycle local 4B should fire if OEM mix or margin evidence fades. | True | True |
| T_C29_R9L104_005850_STAGE3Y_20240429 | 005850 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | True | True |
| T_C29_R9L106_005850_20240612_10_Stage3-Yellow | 005850 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_correct | True | True |
| None | 005850 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | False | True |
| T_C29_R9L106_005850_20240717_20_Stage4B | 005850 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| TRG_R12L81-C31-005860-HANIL-FEED-FOOD-SECURITY-LIFECYCLE | 005860 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should allow food-security/feed policy positives only when policy or grain-price attention maps to direct feed demand, purchase cost pass-through, customer volume, revenue conversion and margin bridge. Hanil Feed produced tradable MFE but later drawdown requires lifecycle 4B if direct-economics evidence fades. | True | True |
| T_C03_R1L108_005870_20240429_STAGE2 | 005870 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current profile can over-promote defense beta unless sovereign funded backlog, delivery schedule and margin/cash bridge are verified | True | True |
| R1L102_C03_HUNEED_2024_STAGE2_FALSE_POSITIVE_DEFENSE_COMMUNICATION_EXPORT_FRAMEWORK_WATCH | 005870 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_false_positive_if_defense_communication_export_watch_counts_without_signed_order_delivery_customer_acceptance_margin_revision_bridge | True | True |
| None | 005870 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | None | False | True |
| SAMSUNG_005930_2024_03_20_STAGE2_FALSE_POSITIVE_HBM_CATCHUP_CAPACITY_LAG | 005930 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_false_positive | False | True |
| C06-127-T004 | 005930 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_too_permissive_if_generic_hbm_demand_offsets_customer_delay | False | True |
| C06-127-T005 | 005930 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_needs_hard_4c_confirmation_before_price_validation | False | True |
| None | 005930 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | None | True | True |
| None | 005930 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | None | True | True |
| None | 005930 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | None | False | True |
| R6L91_C21_005940_20240129_STAGE2_BROKERAGE_CAPITAL_RETURN | 005940 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_correct_if_ROE_payout_buyback_capital_buffer_bridge_required | True | True |
| TRG_R6L81-C21-005940-NH-INVESTMENT-BROKERAGE-CAPITAL-RETURN-BRIDGE | 005940 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | C21 should protect securities/brokerage value-up positives when PBR/ROE rerating is backed by dividend or buyback policy, trading volume, retail brokerage, IB earnings and capital buffer. NH Investment had strong MFE with almost no entry-basis MAE. | True | True |
| None | 005940 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | True | True |
| None | 005940 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | False | True |
| C31_R11L106_TRG_11 | 005940 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | None | True | True |
| T_C15_R4L105_005950_20240508_13_Stage2-Actionable | 005950 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive | True | True |
| None | 005950 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | True | True |
| T_C05_R1L109_005960_20240226_POST_SPIKE_LOCAL4B_HIGH_MAE | 005960 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | True | True |
| None | 005960 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | True | True |
| R10L89_C30_DONGBU_2024_STAGE2_FALSE_POSITIVE_CONSTRUCTION_BETA | 005960 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive_if_construction_beta_counts_without_PF_cashflow_balance_bridge | True | True |
| R10L83_C30_005960_20240425_STAGE2_FALSE_POSITIVE_LOW_LIQUIDITY_NO_REPAIR | 005960 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive | True | True |
| R10L87-C30-005960-T1 | 005960 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | residual_false_positive_if_macro_support_overweighted_without_company_repair_bridge | True | True |
| TRG_R10L79-C30-005960-DONGBU-E&C-PF-HIGHMAE-LOCAL4B | 005960 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should flag local 4B when builder/PF fear aligns with persistent MAE and liquidity/orderbook risk, but hard 4C still requires non-price refinancing failure, default, covenant, impairment, auditor/control or solvency evidence. Dongbu E&C leaked into a high-MAE path with very limited MFE. | True | True |
| TRG_R10L75-C30-005960-DONGBU-PF-LIQUIDITY-LOCAL4B | 005960 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should flag local 4B when mid-builder PF/orderbook/liquidity risk produces weak MFE and widening MAE. Dongbu Construction had almost no upside and a later -25% MAE path, but hard 4C still requires explicit non-price refinancing, default, impairment, auditor/control or solvency break. | True | True |
| None | 005960 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | True | True |
| TRG_R10L75-C30-005960-DONGBU-PF-LIQUIDITY-LOCAL4B | 005960 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive | True | True |
| R13_CROSS_005960_2024-02-01_Stage4B-Local-PFRisk | 005960 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive | True | True |
| R13L89_REVIEW_C30_DONGBU_2024_STAGE2_FALSE_POSITIVE_CONSTRUCTION_BETA | 005960 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive_if_construction_beta_counts_without_PF_cashflow_balance_bridge | True | True |
| R5_L122_C18_011 | 006040 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | True | True |
| C19_R5L119_07_006040_Stage2_Actionable_2024-02-01 | 006040 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | True | True |
| C20_R5L117_006040_20240201_Stage2_Actionable | 006040 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_error_or_stress_case | True | True |
| R12L88_C32_DONGWON_2024_STAGE2_FALSE_POSITIVE_CAPITAL_STRUCTURE_EVENT | 006040 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive_if_capital_structure_event_counts_without_control_premium_or_cashflow_bridge | True | True |
| R13L88_REVIEW_C32_DONGWON_2024_STAGE2_FALSE_POSITIVE_CAPITAL_STRUCTURE_EVENT | 006040 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_capital_structure_event_counts_without_control_premium_or_cashflow_bridge | True | True |
| TRG_R3L77-C11-006110-SAMA-ALUMINUM-FOIL-ORDERBOOK-THEME-FADE | 006110 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive | True | True |
| R3L96_C11_SAMAALUMINUM_2024_STAGE2_ACTIONABLE_BATTERY_FOIL_ORDERBOOK_MARGIN_BRIDGE | 006110 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| TRG_R3L77-C11-006110-SAMA-ALUMINUM-FOIL-ORDERBOOK-THEME-FADE | 006110 | C11_BATTERY_ORDERBOOK_RERATING | C11 should not treat battery aluminum-foil or component-material beta as durable Stage2 unless customer call-off, contracted volume, utilization, price pass-through and margin evidence refreshes. Sama Aluminum had a strong MFE but later opened a very large MAE path, making it local 4B rather than durable Green. | True | True |
| TRG_R3L75-C12-006110-SAMA-ALUMINIUM-ALFOIL-CONTRACT-BETA-FADE | 006110 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_false_positive | True | True |
| TRG_R3L75-C12-006110-SAMA-ALUMINIUM-ALFOIL-CONTRACT-BETA-FADE | 006110 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | C12 should not treat aluminum-foil contract beta as durable Stage2 unless customer order, call-off cadence, utilization and margin bridge remain visible. Sama Aluminium had a strong early MFE but later collapsed, showing call-off and utilization risk. | True | True |
| R3L92_C14_006110_20240102_STAGE2_4B_EV_FOIL_SLOWDOWN | 006110 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_correct_if_demand_slowdown_calloff_margin_cash_drag_routes_to_4B | True | True |
| C14-R3L97-01-006110-Stage4C-2024-10-31 | 006110 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_correct | True | True |
| R4L88_C15_006110_20240220_STAGE2_FALSE_POSITIVE_ALUMINUM_REBOUND | 006110 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive_if_aluminum_material_rebound_overcredited | True | True |
| R4L83_C15_006110_20240214_STAGE2_FALSE_POSITIVE_ALUMINUM_FOIL_HIGH_MAE | 006110 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive | True | True |
| R4L90_C15_SAMAALUMINUM_2024_STAGE4B_ALUMINUM_FOIL_EVENT_CAP | 006110 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_4B_too_late_if_aluminum_foil_theme_premium_not_capped | True | True |
| TRG_R4L81-C16-006110-SAMA-ALUMINUM-FOIL-STRATEGIC-SUPPLY-FADE | 006110 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | C16 should not treat aluminum/battery-foil supply theme beta as durable Stage2 unless customer volume, utilization, orderbook, pricing and margin bridge are visible. Sam-A Aluminum had an early MFE, then a severe drawdown. | True | True |
| R13L88_REVIEW_R4_C15_MATERIAL_SPREAD_SUPERCYCLE_006110_2024-02-20 | 006110 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R13L90_REVIEW_R4_C15_MATERIAL_SPREAD_SUPERCYCLE_006110_2024_06_11_TRIGGER | 006110 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_4B_too_late_if_aluminum_foil_theme_premium_not_capped | True | True |
| LS_006260_2024_03_14_STAGE2A_GRID_CABLE_DATACENTER_CAPEX | 006260 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_4B_too_late | False | True |
| C15_R4L89_LS_20240412 | 006260 | C15_MATERIAL_SPREAD_SUPERCYCLE | None | False | True |
| C15_R4L89_LS_20240412 | 006260 | C15_MATERIAL_SPREAD_SUPERCYCLE | None | False | True |
| R4L92_C16_LS_2024_STAGE2_ACTIONABLE_COPPER_RESOURCE_SUPPLY_CHAIN | 006260 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R4L87_C16_006260_20240314_STAGE2_COPPER_GRID_SUPPLY | 006260 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_correct_if_supply_customer_margin_bridge_required | True | True |
| R4L85_C16_006260_20240411_STAGE2_COPPER_ELECTRIFICATION_SUPPLY_BRIDGE | 006260 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_correct_if_supply_bridge_required | True | True |
| None | 006260 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| None | 006260 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| C32_006260_20240411_STAGE3_YELLOW | 006260 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive_or_overpromotion_risk | True | True |
| R13L87_REVIEW_R4_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_006260_2024-03-14 | 006260 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_correct | True | True |
| R13L85_REVIEW_R4_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_006260_2024-04-11 | 006260 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_correct | True | True |
| None | 006280 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | None | True | True |
| C23_006280_20240709_STAGE2A_TRIGGER | 006280 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | None | True | True |
| None | 006280 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | None | True | True |
| V12_COMPACT_006280_2024-06-12_POST_LAUNCH_COMMERCIALIZATION_BLOWOFF_GUARD | 006280 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive | True | True |
| None | 006280 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | False | True |
| None | 006280 | C24_BIO_TRIAL_DATA_EVENT_RISK | C24 must require fresh binary/data endpoint quality; reroute commercialization, device, reimbursement, or price-only events to C23/C25/local_4B as appropriate. | True | True |
| R1L93B_C01_006340_20240513_STAGE2_FALSE_POSITIVE_WIRE_CABLE_BLOWOFF | 006340 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_false_positive_if_wire_cable_theme_blowoff_counted_as_orderbacklog_margin_bridge | True | True |
| TRG_R1L76-C02-006340-DAEWON-CABLE-COPPER-GRID-THEME-FADE | 006340 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_false_positive | True | True |
| DAEWONCABLE_006340_2024_04_05_STAGE2A_GRID_CABLE_SMALLCAP_BETA | 006340 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_4B_too_late | False | True |
| TRG_R1L76-C02-006340-DAEWON-CABLE-COPPER-GRID-THEME-FADE | 006340 | C02_POWER_GRID_DATACENTER_CAPEX | C02 should not treat copper/cable/grid theme spikes as durable Stage2 unless customer order, backlog, delivery and margin bridge are explicit. Daewon Cable had huge tradable MFE but then a deep post-peak drawdown, making it a theme-spike lifecycle local 4B row rather than durable Green. | True | True |
| R4L91_C15_006340_20240314_STAGE2_COPPER_WIRE_SPREAD | 006340 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_correct_if_inventory_spread_ASP_margin_cash_bridge_required | True | True |
| None | 006340 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| T_C01_R1L111_006360_20240430_Stage2-Actionable | 006360 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | delayed repair worked, but it is a C30/C05 balance-sheet/cost-repair bridge; C01 should only keep it as a reroute stress row | True | True |
| None | 006360 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | False | True |
| T_C05_R1L109_006360_20240201_COST_PROVISION_REPAIR_MARGIN_WATCH | 006360 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | True | True |
| T_C05_R1L108_006360_20240430_COST_PROVISION_RECOVERY | 006360 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | True | True |
| R1L84_C05_006360_20240403_STAGE2_REPAIR_CONTROL_MARGIN_BRIDGE | 006360 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | current_profile_correct_watch_yellow_not_green | True | True |
| TRG_C05_006360_20230629_STAGE4C | 006360 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | current_profile_4C_should_route_fast_when_quality_cost_break_confirms_margin_gap | True | True |
| None | 006360 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | True | True |
| V12_COMPACT_006360_2024-04-29_post_pf_risk_repair_backlog_margin_recovery | 006360 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive | False | True |
| C30_R10L105_006360_20240430_Stage2_Actionable | 006360 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_error_if_C30_overcredits_price_or_low_PBR_without_balance_sheet_bridge | True | True |
| None | 006360 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| None | 006360 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| None | 006360 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | True | True |
| R10L91_C30_006390_20240531_STAGE2_CEMENT_ASP_MARGIN | 006390 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_correct_if_ASP_input_cost_margin_cash_bridge_required_and_data_quality_repaired | True | True |
| TRG-C11-006400-20240828-STAGE2 | 006400 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive_if_actionable | False | True |
| R3L98_C11_SAMSUNGSDI_2024_STAGE2_FALSE_POSITIVE_CELLMAKER_ORDERBOOK_CALLOFF_WATCH | 006400 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive_if_cellmaker_orderbook_watch_counts_without_calloff_utilization_margin_revision_bridge | True | True |
| V12_COMPACT_C12_R3L105_006400_20240129_02_006400_2024-01-29_Stage2 | 006400 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_false_positive | True | True |
| R3L93_C12_006400_20240312_STAGE2_FALSE_POSITIVE_PREMIUM_CELL_CALLOFF | 006400 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_false_positive_if_premium_cell_contract_vocabulary_overcredited | True | True |
| None | 006400 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | True | True |
| R3L92_C13_SAMSDI_2024_STAGE2_ACTIONABLE_CELL_JV_UTILIZATION_AMPC_BRIDGE | 006400 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| V12_COMPACT_C13-102-02_006400_2024-03-12_Stage3-Yellow | 006400 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_false_positive | True | True |
| None | 006400 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | True | True |
| None | 006400 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | None | False | True |
| None | 006400 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| R13_CROSS_006400_2024-03-12_Stage3-Yellow | 006400 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| T_C15_R4L105_006650_20240415_14_Stage2 | 006650 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive | True | True |
| None | 006650 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | True | True |
| R13_4B4C_L101_T005_006650 | 006650 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| None | 006650 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | None | True | True |
| TRG_R6L73-C21-006800-MIRAESEC-BROKERAGE-VALUEUP-BETA-FADE | 006800 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | C21 should not treat brokerage/value-up beta as durable Green unless recurring ROE, capital return, treasury-stock cancellation or distribution bridge is verified. Mirae generated MFE but later faded and needs local 4B/RiskWatch rather than durable Stage2. | True | True |
| R6L87_C21_006800_20240125_STAGE2_BROKERAGE_ROE_CAPITAL_RETURN | 006800 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_correct_if_ROE_capital_return_bridge_required | True | True |
| R6L94_C21_MIRAESEC_2024_STAGE2_FALSE_POSITIVE_BROKERAGE_PBR_VALUEUP_WATCH | 006800 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive_if_brokerage_PBR_valueup_watch_counts_without_capital_return_ROE_revision_bridge | True | True |
| None | 006800 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | True | True |
| TRG_R6L73-C21-006800-MIRAESEC-BROKERAGE-VALUEUP-BETA-FADE | 006800 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | C21 should not treat brokerage/value-up beta as durable Green unless recurring ROE, capital return, treasury-stock cancellation or distribution bridge is verified. Mirae generated MFE but later faded and needs local 4B/RiskWatch rather than durable Stage2. | True | True |
| R6L83_C21_006800_20240202_STAGE2_BROKERAGE_BETA_NO_ROE_BRIDGE | 006800 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | True | True |
| C31_R11L106_TRG_10 | 006800 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | None | True | True |
| R13L87_REVIEW_R6_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_006800_2024-01-25 | 006800 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_correct | True | True |
| R13L94_REVIEW_R6_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_006800_2024_02_23_TRIGGER | 006800 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive_if_brokerage_PBR_valueup_watch_counts_without_capital_return_ROE_revision_bridge | True | True |
| R12L90_C32_006840_20240102_STAGE2_FALSE_POSITIVE_HOLDCO_DISCOUNT | 006840 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive_if_holdco_discount_rebound_overcredited | True | True |
| R4L97_C17_TAEKYUNGCHEM_2024_STAGE4B_INDUSTRIAL_GAS_DRYICE_SPREAD_EVENT_CAP | 006890 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_4B_too_late_if_industrial_gas_spread_event_premium_not_capped | True | True |
| R11L89_C02_006910_20240222_STAGE2_FALSE_POSITIVE_POWER_POLICY | 006910 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_false_positive_if_power_policy_rebound_counted_as_C02_bridge | True | True |
| TRG_R11L78-C04-006910-BOSEONG-POWERTEC-NUCLEAR-POLICY-EQUIPMENT-LIFECYCLE | 006910 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | C04 should allow nuclear-policy/project equipment rows only when policy headline maps to named project, equipment order, delivery schedule, revenue recognition and margin bridge. Boseong Powertec produced a meaningful MFE, then a post-peak drawdown, so it should be lifecycle-managed rather than permanent Green. | True | True |
| R11L92_C04_BOSUNGPOWER_2024_STAGE4B_NUCLEAR_POWER_EQUIPMENT_EVENT_CAP | 006910 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_4B_too_late_if_nuclear_power_equipment_event_premium_not_capped | True | True |
| C04_P1_TO50_TRG_17 | 006910 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive | True | True |
| R13L92_REVIEW_R11_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_006910_2024_05_27_TRIGGER | 006910 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_4B_too_late_if_nuclear_power_equipment_event_premium_not_capped | True | True |
| R10L89_C30_006920_20240223_STAGE2_FALSE_POSITIVE_READY_MIX_BLOWOFF | 006920 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive_if_ready_mix_policy_blowoff_counted_as_C30_bridge | True | True |
| R5L93_C19_007070_20240102_STAGE2_FALSE_POSITIVE_RETAIL_OPM_CASH | 007070 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_false_positive_if_retail_platform_vocabulary_overcredited | True | True |
| C32_007070_20240207_STAGE2_ACTIONABLE | 007070 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive_or_overpromotion_risk | True | True |
| R10L89_C30_007110_20240112_STAGE2_FALSE_POSITIVE_STONE_POLICY | 007110 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive_if_policy_theme_spike_overcredited | True | True |
| None | 007310 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | True | True |
| R5L92_C18_OTTOGI_2024_STAGE2_FALSE_POSITIVE_DOMESTIC_FOOD_CHANNEL_CATCHUP | 007310 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive_if_domestic_food_channel_catchup_counts_without_export_reorder_margin_bridge | True | True |
| R5L86_C18_007310_20240617_STAGE2_FALSE_POSITIVE_LARGECAP_FOOD_CHANNEL | 007310 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive_if_channel_theme_overcredited | True | True |
| R5_L122_C18_019 | 007310 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | True | True |
| C19_R5L119_15_007310_Stage3_Yellow_2024-07-15 | 007310 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | True | True |
| C20_R5L115_007310_20240202_FOOD_EXPORT_LABEL_OPM_BRIDGE_FALSE_POSITIVE_Stage3_Yellow | 007310 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | False | True |
| C20_R5L118_007310_20240715_Stage3_Yellow | 007310 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_error | True | True |
| R13L86_REVIEW_R5_C18_CONSUMER_EXPORT_CHANNEL_REORDER_007310_2024-06-17 | 007310 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R13L92_REVIEW_R5_C18_CONSUMER_EXPORT_CHANNEL_REORDER_007310_2024_06_13_TRIGGER | 007310 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive_if_domestic_food_channel_catchup_counts_without_export_reorder_margin_bridge | True | True |
| R6L96_C21_PUREUNSB_2024_STAGE2_FALSE_POSITIVE_SAVINGS_BANK_RATE_VALUEUP_WATCH | 007330 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive_if_savings_bank_rate_valueup_watch_counts_without_ROE_credit_cost_capital_return_revision_bridge | True | True |
| R13L96_REVIEW_R6_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_007330_2024_04_16_TRIGGER | 007330 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_savings_bank_rate_valueup_watch_counts_without_ROE_credit_cost_capital_return_revision_bridge | True | True |
| None | 007540 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | True | True |
| TRG_R2L75-C06-007660-ISU-PETASYS-AI-SERVER-MEMORY-SUBSTRATE-CAPACITY | 007660 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | C06 should not be limited to Samsung/SK Hynix memory makers. It should include AI server/HBM-adjacent memory-network substrate suppliers when customer capacity, order visibility and margin bridge are explicit. Isu Petasys produced strong MFE but later severe drawdown, so lifecycle local 4B is required if bridge evidence fades. | True | True |
| TRG_R2L75-C06-007660-ISU-PETASYS-AI-SERVER-MEMORY-SUBSTRATE-CAPACITY | 007660 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_correct | True | True |
| ISUPETASYS_007660_2024_03_05_STAGE2A_AI_SERVER_HBM_PCB_CUSTOMER_CAPA | 007660 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_4B_too_late | False | True |
| T_C15_R4L105_007690_20240402_15_Stage2 | 007690 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive | True | True |
| None | 007690 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | True | True |
| R4L91_C17_KUKDO_2024_STAGE2_FALSE_POSITIVE_EPOXY_SPREAD_RECOVERY | 007690 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive_if_epoxy_chemical_spread_watch_counts_without_margin_revision_bridge | True | True |
| R13L91_REVIEW_R4_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_007690_2024_02_20_TRIGGER | 007690 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive_if_epoxy_chemical_spread_watch_counts_without_margin_revision_bridge | True | True |
| R9L92_C29_007860_20240129_STAGE2_AUTO_INTERIOR_VOLUME_MIX | 007860 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_correct_if_OEM_volume_program_mix_margin_cash_bridge_required | True | True |
| R5_L122_C18_005 | 007980 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | True | True |
| None | 007980 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | False | True |
| C19_R5L119_05_007980_Stage2_Actionable_2024-02-13 | 007980 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | True | True |
| R4L91_C15_008350_20240213_STAGE2_FALSE_POSITIVE_ALUMINUM_EXTRUSION | 008350 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive_if_aluminum_theme_rebound_overcredited | True | True |
| R4L96_C15_NAMSEONALUMINUM_2024_STAGE4B_ALUMINUM_POLICY_SPREAD_EVENT_CAP | 008350 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_4B_too_late_if_aluminum_policy_spread_event_premium_not_capped | True | True |
| R13L96_REVIEW_R4_C15_MATERIAL_SPREAD_SUPERCYCLE_008350_2024_01_02_TRIGGER | 008350 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late_if_aluminum_policy_spread_event_premium_not_capped | True | True |
| R3L93_C11_YULCHONCHEM_2024_STAGE4B_POUCH_FILM_ORDERBOOK_EVENT_CAP | 008730 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_4B_too_late_if_pouch_film_orderbook_event_premium_not_capped | True | True |
| R13L93_REVIEW_R3_C11_BATTERY_ORDERBOOK_RERATING_008730_2024_02_16_TRIGGER | 008730 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late_if_pouch_film_orderbook_event_premium_not_capped | True | True |
| R5L87_C19_008770_20240401_STAGE2_FALSE_POSITIVE_DUTYFREE_RETAIL | 008770 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_false_positive_if_dutyfree_rebound_overcredited | True | True |
| R5L97_C19_HOTELSHILLA_2024_STAGE4B_DUTY_FREE_RETAIL_INVENTORY_EVENT_CAP | 008770 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_4B_too_late_if_duty_free_retail_event_premium_not_capped | True | True |
| R13L87_REVIEW_R5_C19_BRAND_RETAIL_INVENTORY_MARGIN_008770_2024-04-01 | 008770 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| None | 008930 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | True | True |
| T_C24_R7L105_008930_20240130_STAGE4B | 008930 | C24_BIO_TRIAL_DATA_EVENT_RISK | bio_holdco_event_spike_must_not_unlock_C24_positive_credit_without_direct_asset_endpoint_or_cash_flow | True | True |
| TRG_R12L75-C32-008930-HANMI-SCIENCE-CONTROL-DISPUTE-BENEFICIARY-FADE | 008930 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive | True | True |
| R12L90_C32_008930_20240112_STAGE2_CONTROL_PREMIUM_EVENT | 008930 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_correct_if_control_premium_ownership_event_bridge_required | True | True |
| R12L90_C32_HANMISCIENCE_2024_STAGE2_FALSE_POSITIVE_FAMILY_DISPUTE_CONTROL_PREMIUM | 008930 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive_if_family_dispute_control_premium_counts_without_durable_transaction_or_capital_allocation_bridge | True | True |
| C32_008930_20240326_STAGE2_ACTIONABLE | 008930 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive_or_overpromotion_risk | True | True |
| TRG_R12L75-C32-008930-HANMI-SCIENCE-CONTROL-DISPUTE-BENEFICIARY-FADE | 008930 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should not treat control dispute or group-combination headlines as durable Stage2 unless listed-shareholder beneficiary, transaction mechanics, closing certainty, capital policy or operating bridge is explicit. Hanmi Science produced an event spike but later opened severe MAE and requires share-count validation. | True | True |
| TRG_R11L80-C32-008930-HANMI-SCIENCE-GOVERNANCE-MERGER-PROXY-SPIKE-FADE | 008930 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should not treat governance/proxy-fight spike beta as durable Stage2 unless a clear tender/control-price anchor, completion probability, legal timetable, shareholder vote mechanics and downside cap are visible. Hanmi Science produced a sharp spike then a severe drawdown. | True | True |
| TRG_R12L72-C32-008930-HANMI-SCIENCE-OCI-CONTROL-CONTEST-BLOWOFF | 008930 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should not treat a control-contest / group-integration headline as durable Stage2 unless closing path, tender price, board/shareholder approval and execution certainty are visible. The price path had fast MFE but later MAE opened materially. | True | True |
| TRG_R12L72-C32-008930-HANMI-SCIENCE-OCI-CONTROL-CONTEST-BLOWOFF | 008930 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should not treat a control-contest / group-integration headline as durable Stage2 unless closing path, tender price, board/shareholder approval and execution certainty are visible. The price path had fast MFE but later MAE opened materially. | True | True |
| R12L96_C32_HANMISCIENCE_2024_STAGE4B_BIO_HOLDCO_MERGER_CONTROL_EVENT_CAP | 008930 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_4B_too_late_if_bio_holdco_merger_control_event_premium_not_capped | True | True |
| R13L96_REVIEW_R12_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_008930_2024_01_16_TRIGGER | 008930 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late_if_bio_holdco_merger_control_event_premium_not_capped | True | True |
| R13L90_REVIEW_R12_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_008930_2024_01_16_TRIGGER | 008930 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive_if_family_dispute_control_premium_counts_without_durable_transaction_or_capital_allocation_bridge | True | True |
| TRG_R11L76-C31-008970-DONGYANG-STEEL-PIPE-EASTSEA-GAS-POLICY-PIPE-BETA-FADE | 008970 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | True | True |
| TRG_R11L74-C31-008970-DONGYANG-PIPELINE-POLICY-PROXY-FADE | 008970 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should not convert a pipeline/steel-pipe policy proxy into durable Stage2 unless project ownership, procurement scope, actual order, EPC participation or revenue timing is visible. KBI Dongyang Steel Pipe had a large initial MFE but then deep MAE and post-peak drawdown. | True | True |
| TRG_R11L76-C31-008970-DONGYANG-STEEL-PIPE-EASTSEA-GAS-POLICY-PIPE-BETA-FADE | 008970 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should not treat gas-field / pipeline policy beta as durable Stage2 unless direct beneficiary mapping, confirmed order, project schedule, revenue and margin bridge are visible. Dongyang Steel Pipe had a tradable MFE but then high MAE and repeated share-count movement, making it local 4B rather than Green. | True | True |
| TRG_R11L74-C31-008970-DONGYANG-PIPELINE-POLICY-PROXY-FADE | 008970 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should not convert a pipeline/steel-pipe policy proxy into durable Stage2 unless project ownership, procurement scope, actual order, EPC participation or revenue timing is visible. KBI Dongyang Steel Pipe had a large initial MFE but then deep MAE and post-peak drawdown. | True | True |
| C06-127-T006 | 009150 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | stage2_ok_but_green_cap_until_direct_memory_customer_capacity_bridge | False | True |
| None | 009150 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | None | True | True |
| None | 009150 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | None | True | True |
| R12L87_C32_HANSSEM_2021_STAGE4B_PE_CONTROL_PREMIUM_FADE | 009240 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive_if_control_premium_spike_counts_as_structural_green | True | True |
| R13L87_REVIEW_C32_HANSSEM_2021_STAGE4B_PE_CONTROL_PREMIUM_FADE | 009240 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive_if_control_premium_spike_counts_as_structural_green | True | True |
| T_C05_R1L109_009410_20240103_WORKOUT_RECAPITALIZATION_HARD_BREAK | 009410 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | True | True |
| R10L92_C30_009410_20240103_STAGE2_4C_PF_WORKOUT_HARD_BREAK | 009410 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_correct_if_PF_workout_liquidity_hard_break_routes_to_4C_not_bargain_rebound | True | True |
| R10L88_C30_TAEYOUNG_2025_STAGE4B_WORKOUT_EVENT_CAP | 009410 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_4B_too_late_if_workout_event_premium_not_capped | True | True |
| None | 009410 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | True | True |
| None | 009410 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | None | False | True |
| None | 009410 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| R13L88_REVIEW_C30_TAEYOUNG_2025_STAGE4B_WORKOUT_EVENT_CAP | 009410 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late_if_workout_event_premium_not_capped | True | True |
| None | 009410 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| R13_CROSS_R13L4_C30_009410_20240103_ACCOUNTING_TRUST_BLOCK_009410_2024-01-03_Stage4C | 009410 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | True | True |
| None | 009410 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | True | True |
| R7L93_C23_009420_20240516_STAGE2_FALSE_POSITIVE_PIPELINE_LATE_REBOUND | 009420 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive_if_late_rebound_validates_original_pipeline_commercialization_entry | True | True |
| None | 009440 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | True | True |
| R4L100_C15_POSCOMTECH_2024_STAGE4B_LITHIUM_MATERIAL_EVENT_CAP | 009520 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_4B_too_late_if_lithium_material_supercycle_event_premium_not_capped | True | True |
| R4L89_C16_POSCOMTECH_2023_STAGE2_ACTIONABLE_LITHIUM_RESOURCE_SUPPLY_BRIDGE | 009520 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| None | 009520 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| R4L90_C16_009520_20240611_STAGE2_FALSE_POSITIVE_LITHIUM_THEME | 009520 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_false_positive_if_lithium_materials_theme_overcredited | True | True |
| T_C15_R4L105_009830_20240220_16_4C | 009830 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive | True | True |
| None | 009830 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| None | 009830 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | True | True |
| R4L86_C17_009830_20240110_STAGE2_FALSE_POSITIVE_SOLAR_CHEMICAL_BETA | 009830 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive_if_solar_chemical_beta_overcredited | True | True |
| R4L84_C17_009830_20240401_STAGE2_FALSE_POSITIVE_SOLAR_CHEMICAL_SPREAD | 009830 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive_if_policy_spread_rebound_overcredited | True | True |
| R12L83_C31_009830_20240401_STAGE2_FALSE_POSITIVE_SOLAR_IRA_REBOUND | 009830 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_too_early | True | True |
| R11L87_C31_HSOL_2023_STAGE4B_SOLAR_POLICY_CAPEX_EVENT_CAP | 009830 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_4B_too_late_if_policy_capex_premium_not_capped | True | True |
| R13L86_REVIEW_R4_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_009830_2024-01-10 | 009830 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R13L83_HIGHMAE_REVIEW_009830_2024-04-01 | 009830 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_too_early | True | True |
| R13_CROSS_009830_2024-02-20_Stage2 | 009830 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive | True | True |
| None | 009830 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | None | True | True |
| R9L94_C29_MYOUNGSHIN_2024_STAGE2_FALSE_POSITIVE_EV_BODY_PARTS_VOLUME_WATCH | 009900 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive_if_EV_body_parts_volume_watch_counts_without_OEM_volume_utilization_margin_revision_bridge | True | True |
| TRG_R9L79-C29-009900-MYOUNGSHIN-EV-BODY-PARTS-THEME-FADE | 009900 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should not treat EV body/parts beta as durable Stage2 unless customer program, volume, utilization, pricing and margin bridge are visible. Myoung Shin Industrial had a small early MFE and then a severe MAE drawdown path. | True | True |
| C29_R9L88_TRG_009900_FP | 009900 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| R9L87_C29_009900_20240202_STAGE2_FALSE_POSITIVE_EV_BODY_PARTS | 009900 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive_if_EV_body_parts_theme_overcredited | True | True |
| R13L87_REVIEW_R9_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_009900_2024-02-02 | 009900 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R13L94_REVIEW_R9_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_009900_2024_01_24_TRIGGER | 009900 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive_if_EV_body_parts_volume_watch_counts_without_OEM_volume_utilization_margin_revision_bridge | True | True |
| C15_R4L89_OCI_20240110 | 010060 | C15_MATERIAL_SPREAD_SUPERCYCLE | None | False | True |
| C15_R4L89_OCI_20240110 | 010060 | C15_MATERIAL_SPREAD_SUPERCYCLE | None | False | True |
| R4L91_C17_OCI_2024_STAGE2_ACTIONABLE_POLYSILICON_CHEMICAL_SPREAD_RECOVERY | 010060 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R4L97_C17_OCIHOLDINGS_2024_STAGE2_FALSE_POSITIVE_POLYSILICON_SPREAD_WATCH | 010060 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive_if_polysilicon_spread_watch_counts_without_realized_spread_inventory_cost_curve_margin_revision_bridge | True | True |
| R4L86_C17_010060_20240110_STAGE2_FALSE_POSITIVE_POLYSILICON_REBOUND | 010060 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive_if_commodity_rebound_overcredited | True | True |
| R13L86_REVIEW_R4_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_010060_2024-01-10 | 010060 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| TRG_R9L77-C29-010100-KOREA-MOVENEX-AUTO-PARTS-VOLUME-MARGIN-FADE | 010100 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| TRG_R9L77-C29-010100-KOREA-MOVENEX-AUTO-PARTS-VOLUME-MARGIN-FADE | 010100 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should not treat auto-parts or drivetrain component beta as durable Stage2 unless named customer program, volume, mix, pricing and margin bridge are visible. Korea Movenex produced an early spike, then leaked into a high-MAE drawdown. | True | True |
| R1L93B_C01_010120_20240227_STAGE2_POWER_EQUIPMENT_BACKLOG | 010120 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_correct_if_order_quality_delivery_margin_cash_bridge_required_but_Green_strict | True | True |
| R1L10_C02_010120_STAGE2A_2024_01_03 | 010120 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_too_late | False | True |
| R1L98_C02_LSELECTRIC_2024_STAGE2_ACTIONABLE_GRID_AUTOMATION_DATACENTER_CAPEX_DELIVERY_BRIDGE | 010120 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R11L85_C02_010120_20240716_STAGE2_FALSE_POSITIVE_GRID_PRICE_EXTENSION | 010120 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_false_positive_if_price_extension_overcredited | True | True |
| R1L10_C02_010120_4B_WATCH_2024_04_12 | 010120 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_correct | False | True |
| R1L91_C02_LSELECTRIC_2024_STAGE4B_LOCAL_SWITCHGEAR_CAPEX_CAP | 010120 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_local_4B_too_early_if_full_window_order_revision_bridge_continues | True | True |
| C04_STATIC_TO50_TRG_12 | 010120 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive | True | True |
| None | 010120 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| None | 010120 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| V12_COMPACT_R13L12_ACCT_PRICE_15_C02_010120_20240704_010120_2024-07-04_4B | 010120 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | True | True |
| R13L85_REVIEW_R11_C02_POWER_GRID_DATACENTER_CAPEX_010120_2024-07-16 | 010120 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| R13L91_REVIEW_R1_C02_POWER_GRID_DATACENTER_CAPEX_010120_2024_07_24_TRIGGER | 010120 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_local_4B_too_early_if_full_window_order_revision_bridge_continues | True | True |
| R13_CROSS_010120_2024-07-04_Stage2-Actionable | 010120 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive | True | True |
| V12_COMPACT_C15-101-02_010130_2024-09-13_Stage3_Yellow_Local4BWatch | 010130 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive | True | True |
| TRG_R4L80-C15-010130-KOREA-ZINC-NONFERROUS-SPREAD-EVENT-LIFECYCLE | 010130 | C15_MATERIAL_SPREAD_SUPERCYCLE | C15 should allow nonferrous smelter positives only when zinc/copper/precious-metal spread, TC/RC, inventory, utilization and margin bridge are visible. Korea Zinc produced enormous MFE, but a late governance/tender-event component must be separated from commodity-spread economics before runtime promotion. | True | True |
| T_C15_R4L103_010130_Stage4B_20240913 | 010130 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive_or_wrong_archetype_if_material_label_overweighted | True | True |
| None | 010130 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | None | False | True |
| C32_010130_20240913_LOCAL_4B_WATCH | 010130 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_correct_if_local4b_or_yellow_capped | True | True |
| R12L92_C32_010130_20240913_STAGE2_CONTROL_PREMIUM_TENDER_CASH_PATH | 010130 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_correct_if_tender_terms_minority_eligibility_financing_settlement_floor_required | True | True |
| None | 010130 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| None | 010130 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| None | 010130 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| None | 010130 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| None | 010130 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| None | 010130 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | True | True |
| None | 010130 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | None | True | True |
| TRG_C01_R1L100_010140_20240726 | 010140 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_false_positive | False | True |
| TRG_R1L77-C01-010140-SAMSUNG-HI-SHIPBUILDING-BACKLOG-MARGIN | 010140 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | C01 should allow shipbuilding orderbook Stage2 when backlog, LNG/offshore mix, pricing discipline, delivery schedule and margin bridge are visible. Samsung Heavy produced a large MFE with controlled entry-basis MAE, but post-peak drawdown requires lifecycle local 4B if backlog/margin evidence fades. | True | True |
| TRG_R1L77-C01-010140-SAMSUNG-HI-SHIPBUILDING-BACKLOG-MARGIN | 010140 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_correct | True | True |
| C01_R1L100_010620_midsize_ship_backlog_margin_bridge_T1 | 010620 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_correct_but_green_late_risk | False | True |
| HDMIPO_010620_2024_04_18_STAGE2A_SHIPBUILDING_BACKLOG_MARGIN_BRIDGE | 010620 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_4B_too_late | False | True |
| TRG_R1L73-C01-010620-HDMIPO-MIDSHIP_PRODUCT_MIX_MARGIN_BRIDGE | 010620 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | C01 should capture mid-size vessel backlog recovery when product mix and margin conversion are visible. But after the 2025 peak, a later local 4B-watch is needed if the margin bridge stops refreshing or drawdown opens. | True | True |
| TRG_R1L73-C01-010620-HDMIPO-MIDSHIP_PRODUCT_MIX_MARGIN_BRIDGE | 010620 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | C01 should capture mid-size vessel backlog recovery when product mix and margin conversion are visible. But after the 2025 peak, a later local 4B-watch is needed if the margin bridge stops refreshing or drawdown opens. | True | True |
| R1L93_C01_010620_20240314_STAGE2_FALSE_OVERBLOCK_ORDERBOOK_MARGIN_RESET | 010620 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_false_positive_if_margin_gap_guard_blocks_reset_plus_orderbook_margin_recovery | True | True |
| None | 010690 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | True | True |
| T_C29_R9L105_010690_Stage2Actionable_20240617 | 010690 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| T_C29_R9L106_010690_20240617_08_Stage4B | 010690 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| V12_COMPACT_R13L11-4B4C-011_010690_2024-06-17_cross_archetype_4b_4c_boundary_retest | 010690 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R13_CROSS_R13L4_C29_010690_20240617_MARGIN_FCF_TRUST_010690_2024-06-17_Stage4B-Local-Watch | 010690 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | True | True |
| V12_COMPACT_R13L2_C29_010690_20240617_STAGE2ACTIONABLE_010690_2024-06-17_cross_archetype_high_MAE_guardrail_review | 010690 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| R13_CROSS_010690_2024-06-17_Stage2-Actionable | 010690 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| T_R13_STAGE2FP_L6_010690_Stage2Actionable_2024-06-17 | 010690 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_stage2_false_positive_or_overpromotion_risk | True | True |
| T_C05_R1L109_010780_20240207_MATERIALS_CONSTRUCTION_CASH_BRIDGE | 010780 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | True | True |
| TRG_R10L82-C30-010780-ISDONGSEO-PF-HOUSING-RECOVERY-SHARECOUNT | 010780 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should allow builder recovery rows only when housing project quality, orderbook, PF exposure, refinancing access, liquidity and margin bridge are visible. IS Dongseo produced tradable MFE but later post-peak drawdown and stock-web share-count movement require lifecycle 4B discipline and validation. | True | True |
| TRG_R10L78-C30-010780-ISDONGSEO-PF-RECOVERY-SPIKE-NO-HARD4C | 010780 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should not over-convert builder/developer PF fear into hard 4C when the path produces recovery MFE and entry-basis MAE remains bounded. IS Dongseo needs PF/liquidity/orderbook monitoring, but price alone is not confirmed balance-sheet break evidence. | True | True |
| R10L89_C30_ISDONGSEO_2024_STAGE2_ACTIONABLE_HOUSING_PF_REPAIR | 010780 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R10L87_C30_010780_20240125_STAGE2_MIDCAP_REPAIR | 010780 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_correct_if_PF_liquidity_backlog_bridge_required | True | True |
| R10L87-C30-010780-T1 | 010780 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | residual_false_positive_if_macro_support_or_low_PBR_overlay_is_allowed_without_company_repair_bridge | True | True |
| None | 010780 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | True | True |
| R13L87_REVIEW_R10_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_010780_2024-01-25 | 010780 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_correct | True | True |
| R13_L106_T08_010780 | 010780 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive | True | True |
| None | 010820 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | None | False | True |
| TRG_R1L74-C03-010820-FIRSTEC-DEFENSE-ELECTRONICS-PRICE-BETA | 010820 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | C03 should not treat defense electronics or drone-theme price beta as durable Stage2 unless named export order, customer framework, backlog conversion or margin bridge is visible. Firstec had a same-day spike but later MAE and drawdown opened, so it is a local 4B-watch / false Stage2 row. | True | True |
| TRG_R11L77-C03-010820-FIRSTEC-DEFENSE-UNMANNED-THEME-BETA-FADE | 010820 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_false_positive | True | True |
| R11L89_C03_FIRSTEC_2024_STAGE2_FALSE_POSITIVE_DRONE_DEFENSE_THEME | 010820 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_false_positive_if_drone_defense_theme_counts_without_export_backlog_margin_bridge | True | True |
| TRG_R1L82-C03-010820-FIRSTEC-DEFENSE-COMPONENT-THEME-WHIPSAW | 010820 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | C03 should not treat defense component/drone/robot theme beta as durable Stage2 unless contract backlog, customer program, delivery schedule, revenue conversion and margin bridge are visible. Firstec had a late theme spike but also a deep interim MAE, so it is a whipsaw/local-4B boundary rather than durable Green. | True | True |
| TRG_R11L79-C03-010820-FIRSTEC-DEFENSE-DRONE-THEME-BACKLOG-GAP | 010820 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | C03 should not treat drone/defense component theme beta as durable Stage2 unless named export framework, order backlog, delivery schedule, revenue recognition and margin bridge are visible. Firstec had limited early MFE, then high MAE, and a late theme spike; without backlog/margin proof it should be local 4B-watch rather than durable Green. | True | True |
| TRG_R1L74-C03-010820-FIRSTEC-DEFENSE-ELECTRONICS-PRICE-BETA | 010820 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | C03 should not treat defense electronics or drone-theme price beta as durable Stage2 unless named export order, customer framework, backlog conversion or margin bridge is visible. Firstec had a same-day spike but later MAE and drawdown opened, so it is a local 4B-watch / false Stage2 row. | True | True |
| TRG_R11L77-C03-010820-FIRSTEC-DEFENSE-UNMANNED-THEME-BETA-FADE | 010820 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | C03 should not treat defense/unmanned-system theme beta as durable Stage2 unless named defense program, contract backlog, delivery schedule, revenue recognition and margin bridge are visible. Firstec had tradable MFE but spent much of the window in drawdown and only later spiked, making it a local 4B-watch boundary rather than durable Green. | True | True |
| R11L86_C03_010820_20240117_STAGE2_FALSE_POSITIVE_DEFENSE_ROBOT_THEME | 010820 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_false_positive_if_defense_robot_theme_overcredited | True | True |
| T_C03_R1L108_010820_20240617_STAGE4B | 010820 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current profile can over-promote defense beta unless sovereign funded backlog, delivery schedule and margin/cash bridge are verified | True | True |
| R13L86_REVIEW_R11_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_010820_2024-01-17 | 010820 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R13L89_REVIEW_C03_FIRSTEC_2024_STAGE2_FALSE_POSITIVE_DRONE_DEFENSE_THEME | 010820 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive_if_drone_defense_theme_counts_without_export_backlog_margin_bridge | True | True |
| T_C15_R4L105_010950_20240213_01_Stage2 | 010950 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive | True | True |
| T_C15_R4L103_010950_Stage2_20240405 | 010950 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive_or_wrong_archetype_if_material_label_overweighted | True | True |
| T_C15_R4L105_010950_20240405_17_4B-Local-Watch | 010950 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive | True | True |
| None | 010950 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| None | 010950 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| None | 010950 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| TRG_R4L73-C17-010950-SOIL-REFINING-SPREAD-BETA-LOCAL4B | 010950 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | C17 should not treat refinery spread beta as Green unless crack spread, inventory, utilization, and earnings revision bridge are visible. S-Oil produced almost no MFE and later severe 180D MAE, so local 4B-watch is more appropriate. | True | True |
| None | 010950 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | True | True |
| TRG_R4L73-C17-010950-SOIL-REFINING-SPREAD-BETA-LOCAL4B | 010950 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | C17 should not treat refinery spread beta as Green unless crack spread, inventory, utilization, and earnings revision bridge are visible. S-Oil produced almost no MFE and later severe 180D MAE, so local 4B-watch is more appropriate. | True | True |
| None | 010950 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | None | True | True |
| R1L93_C05_SAMHODEV_2024_STAGE2_FALSE_POSITIVE_CIVIL_EPC_ORDER_CATCHUP | 010960 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | current_profile_false_positive_if_civil_EPC_order_catchup_counts_without_contract_backlog_margin_revision_bridge | True | True |
| R10L96_C30_SAMHODEV_2024_STAGE2_ACTIONABLE_CIVIL_ENGINEERING_ORDER_CASHFLOW_BRIDGE | 010960 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R13L93_REVIEW_R1_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_010960_2024_02_01_TRIGGER | 010960 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_civil_EPC_order_catchup_counts_without_contract_backlog_margin_revision_bridge | True | True |
| TRG_R5L75-C18-011150-CJ-SEAFOOD-KFOOD-THEME-SPIKE-FADE | 011150 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | True | True |
| TRG_R5L75-C18-011150-CJ-SEAFOOD-KFOOD-THEME-SPIKE-FADE | 011150 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | C18 should not treat K-food or seafood export theme spikes as durable Stage2 unless sell-through, reorder cadence, customer/channel expansion and margin bridge are visible. CJ Seafood had an enormous tradable MFE but then a sharp post-peak drawdown, so it is a theme-spike local 4B row rather than durable Green. | True | True |
| R5L84_C18_011150_20240614_STAGE2_FALSE_POSITIVE_SEAFOOD_EXPORT_THEME | 011150 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive_if_theme_spike_overcredited | True | True |
| R5L94_C18_CJSEAFOOD_2024_STAGE4B_SEAFOOD_KFOOD_EXPORT_EVENT_CAP | 011150 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_4B_too_late_if_seafood_Kfood_export_event_premium_not_capped | True | True |
| R5L99_C18_CJSEAFOOD_2024_STAGE4B_SEAFOOD_K_FOOD_EXPORT_EVENT_CAP | 011150 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_4B_too_late_if_K_food_export_event_premium_not_capped | True | True |
| None | 011150 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | True | True |
| R5L88_C20_CJSEAFOOD_2024_STAGE4B_KFOOD_THEME_EVENT_CAP | 011150 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive_if_Kfood_theme_spike_counts_as_distribution_rerating | True | True |
| R13L94_REVIEW_R5_C18_CONSUMER_EXPORT_CHANNEL_REORDER_011150_2024_01_25_TRIGGER | 011150 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_4B_too_late_if_seafood_Kfood_export_event_premium_not_capped | True | True |
| T_C15_R4L103_011170_Stage2_20240429 | 011170 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive_or_wrong_archetype_if_material_label_overweighted | True | True |
| T_C15_R4L105_011170_20240429_18_4B-Local-Watch | 011170 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive | True | True |
| None | 011170 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| None | 011170 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | True | True |
| R4L10_C17_011170_T1 | 011170 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive | False | True |
| R4L98_C17_LOTTECHEM_2024_STAGE2_FALSE_POSITIVE_BASE_CHEMICAL_SPREAD_RECOVERY_WATCH | 011170 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive_if_base_chemical_recovery_watch_counts_without_realized_spread_volume_inventory_margin_revision_bridge | True | True |
| R4L94_C17_LOTTECHEM_2024_STAGE2_FALSE_POSITIVE_PETROCHEM_SPREAD_WATCH | 011170 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive_if_petrochem_spread_watch_counts_without_utilization_margin_revision_bridge | True | True |
| R4L84_C17_011170_20240216_STAGE2_FALSE_POSITIVE_PETROCHEM_SPREAD | 011170 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive_if_spread_rebound_overcredited | True | True |
| R13_CROSS_R13L4_C17_011170_20240202_INVENTORY_SPREAD_TRUST_011170_2024-02-02_Stage2 | 011170 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | True | True |
| None | 011170 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | True | True |
| T_R13_STAGE2FP_L5_011170_Stage2_2024-04-29 | 011170 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_stage2_false_positive_or_overpromotion_risk | True | True |
| None | 011170 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | None | True | True |
| None | 011170 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | None | True | True |
| R13L94_REVIEW_R4_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_011170_2024_02_01_TRIGGER | 011170 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive_if_petrochem_spread_watch_counts_without_utilization_margin_revision_bridge | True | True |
| C32_011200_HMM_20231219_STRATEGIC_SALE_S2 | 011200 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | None | True | True |
| None | 011210 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | False | True |
| T_C29_R9L106_011210_20240125_04_Stage2 | 011210 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| T_C29_R9L104_011210_STAGE2_20240202 | 011210 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | True | True |
| R9L92_C29_UNICK_2024_STAGE2_FALSE_POSITIVE_EV_VALVE_MOBILITY_THEME | 011320 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive_if_EV_valve_mobility_theme_counts_without_volume_margin_revision_bridge | True | True |
| R13L92_REVIEW_R9_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_011320_2024_02_06_TRIGGER | 011320 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive_if_EV_valve_mobility_theme_counts_without_volume_margin_revision_bridge | True | True |
| TRG_C11_R3L105_007 | 011500 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive | True | True |
| R3L98_C13_HANNONG_2024_STAGE4B_SOLID_STATE_ELECTROLYTE_JV_EVENT_CAP | 011500 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_4B_too_late_if_solid_state_electrolyte_JV_event_premium_not_capped | True | True |
| R3L99-C14-004-T1 | 011500 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_missed_structural_if_all_battery_materials_are_hard_4C_by_label | True | True |
| T_C15_R4L105_011500_20240328_19_Stage2-Actionable | 011500 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive | True | True |
| None | 011500 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | True | True |
| None | 011500 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | None | True | True |
| C04_P1_TO50_TRG_09 | 011700 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive | True | True |
| T_C04_R1L107_011700_20240528_Stage2 | 011700 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | stage2_cap_required_without_order_bridge_or_cash_conversion | True | True |
| None | 011700 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | None | False | True |
| None | 011700 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | None | True | True |
| R13_CROSS_011700_2024-05-28_Stage2 | 011700 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive | True | True |
| T_R13_STAGE2FP_L5_011700_Stage2_2024-05-28 | 011700 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_stage2_false_positive_or_overpromotion_risk | True | True |
| T_C15_R4L105_011780_20240429_20_Stage2-Actionable | 011780 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive | True | True |
| T_C15_R4L104_011780_Stage3_Yellow_20240429 | 011780 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_can_capture_local_MFE_but_overstay_without_spread_to_FCF_bridge | True | True |
| None | 011780 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| R4L10_C17_011780_T1 | 011780 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_correct | False | True |
| R4L98_C17_KUMHOPETRO_2024_STAGE2_ACTIONABLE_SYNTHETIC_RUBBER_SPREAD_MARGIN_BRIDGE | 011780 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| KUMHOPETRO_011780_2024_01_29_STAGE2A_SYNTHETIC_RUBBER_SPREAD | 011780 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_4B_too_late | False | True |
| None | 011780 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | True | True |
| None | 011780 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| None | 011780 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| None | 011780 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| None | 011780 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| None | 011780 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | None | True | True |
| SKC_011790_2024_03_05_STAGE2A_COPPER_FOIL_ORDERBOOK_RERATING | 011790 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_4B_too_late | False | True |
| None | 011790 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_too_conservative_if_prior_drawdown_blocks_all_C11_repair_but_Green_should_be_high_MAE_guarded | True | True |
| T_C11_R3L107_011790_STAGE2ACTIONABLE_20240405 | 011790 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_needs_high_MAE_guard_before_green | True | True |
| V12_COMPACT_C12_R3L105_011790_20240618_07_011790_2024-06-18_Local-4B-Watch | 011790 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_false_positive | True | True |
| R3L97_C12_SKC_2024_STAGE2_ACTIONABLE_COPPER_FOIL_CUSTOMER_CONTRACT_BRIDGE | 011790 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| None | 011790 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | True | True |
| None | 011790 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_false_positive_if_copper_foil_label_remains_Actionable_after_customer_pull_and_margin_pressure | True | True |
| T_C13_R3L103_011790_STAGE2_20240207 | 011790 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_false_positive_without_copperfoil_utilization_cash_bridge | True | True |
| T_C13_R3L105_011790_STAGE2ACTIONABLE_20240405 | 011790 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | True | True |
| R3L87_C13_011790_20240614_STAGE2_FALSE_POSITIVE_COPPERFOIL_JV_AMPC | 011790 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_false_positive_if_AMPC_JV_theme_overcredited | True | True |
| TRG_R3L81-C13-011790-SKC-COPPERFOIL-AMPC-IRA-EVENT-SEPARATION | 011790 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | C13 should not blindly credit a whole SKC rally to battery JV/AMPC economics. A valid positive needs copper-foil customer/JV visibility, US capacity, utilization, IRA/AMPC economics, revenue and margin bridge; non-battery event/theme components must be separated. | True | True |
| T_C13_R3L104_011790_STAGE4B_20240207 | 011790 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | True | True |
| C14-R3L97-07-011790-Stage4B-2025-03-31 | 011790 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_false_positive_if_hard_4c_without_recovery_band | True | True |
| R3L88_C14_SKC_2024_STAGE4C_FALSE_BREAK_COPPERFOIL_GLASS_SUBSTRATE_RECOVERY | 011790 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_4C_too_hard_if_price_break_without_durable_non_price_thesis_break | True | True |
| T_C15_R4L104_011790_Stage2_Actionable_20240314 | 011790 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_too_permissive_if_price_only_material_blowoff_extends_Green | True | True |
| T_C15_R4L105_011790_20240314_02_Stage3-Yellow | 011790 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_correct | True | True |
| None | 011790 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | True | True |
| R13L87_REVIEW_R3_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_011790_2024-06-14 | 011790 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R13_4B4C_L101_T003_011790 | 011790 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_too_conservative_after_spread_recovery | True | True |
| V12_COMPACT_R13L2_C14_011790_20240507_STAGE4C_011790_2024-05-07_cross_archetype_high_MAE_guardrail_review | 011790 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| TRG_R4L75-C16-011810-STX-RESOURCE-TRADING-POLICY-BETA-FADE | 011810 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_false_positive | True | True |
| R4L89_C16_STX_2024_STAGE2_FALSE_POSITIVE_RESOURCE_TRADING | 011810 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_false_positive_if_resource_trading_theme_counts_without_contract_offtake_margin_bridge | True | True |
| None | 011810 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| None | 011810 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| None | 011810 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| TRG_R4L75-C16-011810-STX-RESOURCE-TRADING-POLICY-BETA-FADE | 011810 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | C16 should not treat resource trading or offtake-policy beta as durable Stage2 unless named supply/offtake, inventory, customer and margin bridge is visible. STX had a short spike but then opened a long high-MAE drawdown path. | True | True |
| R4L95_C16_STX_2024_STAGE4B_LITHIUM_NICKEL_TRADING_RESOURCE_EVENT_CAP | 011810 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_4B_too_late_if_lithium_nickel_resource_trading_event_premium_not_capped | True | True |
| V12_COMPACT_R13L11-4B4C-018_011810_2024-02-16_cross_archetype_4b_4c_boundary_retest | 011810 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R13L95_REVIEW_R4_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_011810_2024_02_16_TRIGGER | 011810 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late_if_lithium_nickel_resource_trading_event_premium_not_capped | True | True |
| V12_COMPACT_R13L12_ACCT_PRICE_18_C16_011810_20240216_011810_2024-02-16_Stage2-Actionable | 011810 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | True | True |
| None | 011810 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | True | True |
| V12_COMPACT_R13L2_C16_011810_20240216_STAGE2ACTIONABLE_011810_2024-02-16_cross_archetype_high_MAE_guardrail_review | 011810 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| T_R13_STAGE2FP_L6_011810_Stage2Actionable_2024-02-16 | 011810 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_stage2_false_positive_or_overpromotion_risk | True | True |
| R13_CROSS_011810_2024-02-16_Stage2-Actionable | 011810 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive | True | True |
| R11L92_C05_011930_20240129_STAGE2_CLEANROOM_EPC_ORDER_MARGIN | 011930 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | current_profile_correct_if_signed_order_delivery_cost_pass_through_margin_cash_bridge_required_but_Green_strict | True | True |
| None | 011930 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | True | True |
| R9L91_C29_012280_20240111_STAGE2_FALSE_POSITIVE_CASTING_AUTOPARTS | 012280 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive_if_casting_autoparts_rebound_overcredited | True | True |
| TR_C16_KDINV_S2_20221020 | 012320 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_4B_too_late | True | True |
| TRG_R9L76-C29-012330-HYUNDAI-MOBIS-MODULE-AS-MIX-CAPITAL-RETURN | 012330 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| None | 012330 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | True | True |
| TRG_R9L74-C29-012330-HYUNDAI-MOBIS-MODULE-ELECTRIFICATION-MARGIN | 012330 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should allow Stage2 for non-OEM auto modules when value-up attention connects to A/S parts, electrification module mix, capital return and margin bridge. Hyundai Mobis produced controlled MAE and a clean MFE path, but shard share-count changes need validation. | True | True |
| TRG_R9L74-C29-012330-HYUNDAI-MOBIS-MODULE-ELECTRIFICATION-MARGIN | 012330 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should allow Stage2 for non-OEM auto modules when value-up attention connects to A/S parts, electrification module mix, capital return and margin bridge. Hyundai Mobis produced controlled MAE and a clean MFE path, but shard share-count changes need validation. | True | True |
| R13_CROSS_012330_2024-02-01_Stage2-Actionable-AutoPartsMarginBridge | 012330 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| R9L83_C29_012330_20240201_STAGE2_VALUEUP_MIX_MARGIN_BRIDGE_POSITIVE | 012330 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_correct | True | True |
| T_C29_R9L105_012330_Stage2Actionable_20240219 | 012330 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| None | 012330 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | False | True |
| TRG_R9L78-C29-012330-HYUNDAI-MOBIS-MODULE-AS-MARGIN-BRIDGE | 012330 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should preserve large auto-module and AS-parts suppliers when customer volume, module mix, AS parts profitability, electrification exposure and margin bridge are visible. Hyundai Mobis produced a slow MFE with controlled MAE; it should not be overblocked, but lifecycle local 4B is needed if mix/margin evidence fades. | True | True |
| TRG_R9L76-C29-012330-HYUNDAI-MOBIS-MODULE-AS-MIX-CAPITAL-RETURN | 012330 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should preserve large-cap mobility supplier positives when module/A/S mix, electrification exposure, customer program stability, capital return and margin bridge are visible. Hyundai Mobis had a slow low-MAE rerating path rather than a theme spike. | True | True |
| T_C29_R9L106_012330_20240219_03_Stage3-Yellow | 012330 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| T_C29_R9L106_012330_20240618_18_Stage4B | 012330 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| None | 012450 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | True | True |
| T_C01_R1L111_012450_20240214_Stage3-Yellow | 012450 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | C01 can recognize backlog compounding, but this should score primarily through C03 unless non-defense orderbook margin bridge is isolated | True | True |
| R11L91_C03_HANWHA_AERO_2024_STAGE2_ACTIONABLE_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 012450 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R11L86_C03_012450_20240214_STAGE2_DEFENSE_EXPORT_FRAMEWORK | 012450 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_correct_if_export_framework_backlog_bridge_required | True | True |
| R11L84_C03_012450_20240226_STAGE2_DEFENSE_PRIME_EXPORT_BACKLOG | 012450 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_correct_if_export_framework_backlog_bridge_required | True | True |
| T_012450_20240214_STAGE3G_REPAIR | 012450 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_too_late_if_delivery_margin_bridge_is_over-gated | False | True |
| T_012450_20240227_STAGE3G_REPAIR | 012450 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_should_allow_green_if_delivery_margin_bridge_verified | False | True |
| T_C03_R1L107_012450_20240426_STAGE3GREEN | 012450 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | allow_green_only_when_export_backlog_delivery_margin_bridge_is_verified | True | True |
| T_C03_R1L108_012450_20240510_STAGE3_GREEN | 012450 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current profile can over-promote defense beta unless sovereign funded backlog, delivery schedule and margin/cash bridge are verified | True | True |
| V12_COMPACT_C03-R1L105-01_012450_2024-02-27_Stage3-Yellow | 012450 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_false_positive | True | True |
| None | 012450 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | None | False | True |
| T_C03_R1L107_012450_20241112_STAGE4B | 012450 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | post_peak_leader_chase_requires_fresh_order_delivery_margin_refresh_or_remains_4b_watch | True | True |
| T_C03_R1L108_012450_20241112_STAGE4B | 012450 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current profile can over-promote defense beta unless sovereign funded backlog, delivery schedule and margin/cash bridge are verified | True | True |
| None | 012450 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | None | False | True |
| None | 012450 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| R13L86_REVIEW_R11_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_012450_2024-02-14 | 012450 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_correct | True | True |
| None | 012450 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| None | 012450 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| None | 012450 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | True | True |
| None | 012510 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | None | False | True |
| R8L92_C28_012510_20240108_STAGE2_ERP_CLOUD_CONTRACT_RETENTION | 012510 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_correct_if_contract_renewal_ARR_margin_cash_bridge_required | True | True |
| DOUZONE_012510_2024_01_18_STAGE2A_ERP_SAAS_RETENTION | 012510 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_4B_too_late | False | True |
| V12_COMPACT_C28_R8L104_012510_20240708_012510_2024-07-09_Stage2-Actionable | 012510 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive | True | True |
| None | 012510 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| None | 012510 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| R10L93_C30_HDC_2024_STAGE2_ACTIONABLE_HOLDCO_HOUSING_BALANCE_REPAIR | 012630 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R10L86_C30_012630_20240125_STAGE2_HOLDCO_REPAIR | 012630 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_correct_if_balance_sheet_repair_bridge_required | True | True |
| R13L86_REVIEW_R10_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_012630_2024-01-25 | 012630 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_correct | True | True |
| TRG_R4L77-C15-012800-DAECHANG-COPPER-BRASS-SPREAD-THEME-FADE | 012800 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive | True | True |
| TRG_R4L74-C15-012800-DAECHANG-COPPER-BRASS-PRICE-BETA-FADE | 012800 | C15_MATERIAL_SPREAD_SUPERCYCLE | C15 should not treat copper/brass price beta as durable Stage2 unless spread-to-margin and inventory/export bridge refreshes. Daechang produced a large MFE but quickly fell into high MAE and post-peak drawdown, so it is a false Stage2 / local 4B-watch row. | True | True |
| TRG_R4L74-C15-012800-DAECHANG-COPPER-BRASS-PRICE-BETA-FADE | 012800 | C15_MATERIAL_SPREAD_SUPERCYCLE | C15 should not treat copper/brass price beta as durable Stage2 unless spread-to-margin and inventory/export bridge refreshes. Daechang produced a large MFE but quickly fell into high MAE and post-peak drawdown, so it is a false Stage2 / local 4B-watch row. | True | True |
| TRG_R4L77-C15-012800-DAECHANG-COPPER-BRASS-SPREAD-THEME-FADE | 012800 | C15_MATERIAL_SPREAD_SUPERCYCLE | C15 should not treat copper/brass price beta as durable Stage2 unless spread, inventory, volume, price pass-through and margin evidence refreshes. Daechang produced large tradable MFE, then opened high MAE and deep post-peak drawdown. | True | True |
| R4L92_C16_DAECHANG_2024_STAGE2_FALSE_POSITIVE_COPPER_THEME | 012800 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_false_positive_if_copper_theme_counts_without_supply_margin_revision_bridge | True | True |
| R4L101_C16_DAECHANG_2024_STAGE4B_COPPER_STRATEGIC_METAL_EVENT_CAP | 012800 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_4B_too_late_if_copper_strategic_metal_event_premium_not_capped | True | True |
| R13L92_REVIEW_R4_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_012800_2024_02_15_TRIGGER | 012800 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive_if_copper_theme_counts_without_supply_margin_revision_bridge | True | True |
| R9L89_C29_012860_20240205_STAGE2_FALSE_POSITIVE_AUTO_ELECTRONICS_SPIKE | 012860 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive_if_auto_electronics_price_spike_overcredited | True | True |
| C29_R9L88_TRG_012860_FP | 012860 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| R1L117-C01-005 | 013030 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_false_positive | False | True |
| T_C05_R1L109_013360_20240411_HOUSING_THEME_PRICE_ONLY | 013360 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | True | True |
| TRG_R10L80-C30-013360-ILSEONG-E&C-RECOVERY-SPIKE-NO-HARD4C | 013360 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should not convert small-builder/PF fear into hard 4C when the path still produces a recovery spike and MAE remains below severe threshold. Price action alone is not balance-sheet-break evidence. | True | True |
| None | 013360 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | True | True |
| R10L87_C30_013360_20240102_STAGE2_FALSE_POSITIVE_POLICY_LATE_REBOUND | 013360 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive_if_late_rebound_retroactively_validates_weak_entry | True | True |
| R10L90_C30_ILSUNGCONST_2024_STAGE4B_POLITICAL_CONSTRUCTION_EVENT_CAP | 013360 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_4B_too_late_if_political_construction_event_premium_not_capped | True | True |
| R13L87_REVIEW_R10_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_013360_2024-01-02 | 013360 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R13L90_REVIEW_R10_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_013360_2024_07_23_TRIGGER | 013360 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_4B_too_late_if_political_construction_event_premium_not_capped | True | True |
| None | 013580 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | True | True |
| T_C05_R1L108_013580_20240429_REGIONAL_EPC_STAGE2_CAP | 013580 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | True | True |
| T_C05_R1L109_013580_20240516_REGIONAL_BUILDER_PARTIAL_CASH_BRIDGE | 013580 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | True | True |
| TRG_R10L80-C30-013580-KYERYONG-E&C-BOUNDED-RISKWATCH-NO-FORCED4B | 013580 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should keep PF/orderbook monitoring active for bounded builders, but should not force local 4B or hard 4C when MAE is contained and no non-price refinancing or solvency break is confirmed. | True | True |
| TRG_R10L75-C30-013580-KYERYONG-BUFFERED-BUILDER-NO-HARD4C | 013580 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive | True | True |
| R13_CROSS_013580_2024-02-01_Stage2-RiskWatch_/_NoFull4B | 013580 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive | True | True |
| C30_R10L104_013580_20240429_Stage2_Actionable | 013580 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_too_positive_if_green_too_late_if_blocks_stage2 | True | True |
| None | 013580 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | True | True |
| TRG_R10L75-C30-013580-KYERYONG-BUFFERED-BUILDER-NO-HARD4C | 013580 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should not convert every regional-builder PF fear into full 4B or hard 4C when MAE is bounded and the stock shows recovery/sideways behavior. Kyeryong Construction is a buffered RiskWatch row: PF/orderbook watch is allowed, but hard balance-sheet break is not price-only. | True | True |
| None | 013580 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | True | True |
| R10L94_C30_CAMUSENC_2024_STAGE2_FALSE_POSITIVE_SMALL_BUILDER_PF_NORMALIZATION_WATCH | 013700 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive_if_small_builder_PF_normalization_watch_counts_without_cashflow_order_funding_margin_bridge | True | True |
| R13L94_REVIEW_R10_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_013700_2024_01_24_TRIGGER | 013700 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive_if_small_builder_PF_normalization_watch_counts_without_cashflow_order_funding_margin_bridge | True | True |
| R11L86_C03_013810_20240118_STAGE2_FALSE_POSITIVE_GEOPOLITICAL_DEFENSE_SPIKE | 013810 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_false_positive_if_geopolitical_theme_overcredited | True | True |
| R11L91_C03_SPEC0_2024_STAGE4B_DEFENSE_THEME_EVENT_CAP | 013810 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_4B_too_late_if_defense_theme_event_premium_not_capped | True | True |
| R13L86_REVIEW_R11_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_013810_2024-01-18 | 013810 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R13L91_REVIEW_R11_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_013810_2024_01_18_TRIGGER | 013810 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_4B_too_late_if_defense_theme_event_premium_not_capped | True | True |
| R9L90_C29_013870_20240102_STAGE2_FALSE_POSITIVE_THERMAL_PUMP | 013870 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive_if_pump_autoparts_rebound_overcredited | True | True |
| TRG_R11L81-C31-013990-AGABANG-LOWBIRTH-CHILDCARE-POLICY-LIFECYCLE | 013990 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should allow low-birth/childcare policy positives only when policy attention maps to direct beneficiary demand, baby-product sales, channel sell-through, revenue conversion and margin bridge. Agabang Company produced tradable MFE but later high MAE, so it is lifecycle-managed rather than durable Green. | True | True |
| TRG_R12L77-C31-013990-AGABANG-LOW-BIRTH-CHILDCARE-POLICY-LIFECYCLE | 013990 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_correct | True | True |
| TRG_R12L77-C31-013990-AGABANG-LOW-BIRTH-CHILDCARE-POLICY-LIFECYCLE | 013990 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 can allow a policy-event lifecycle candidate when low-birth or childcare policy maps to direct beneficiary demand, sell-through, inventory normalization and margin bridge. Agabang produced a large MFE, but later drawdown means it cannot remain Green unless direct-demand and margin evidence refreshes. | True | True |
| R13_CROSS_013990_2024-01-10_Stage2 | 013990 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | True | True |
| R13_CROSS_013990_2024-01-10_Stage2 | 013990 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| T_R13_STAGE2FP_L6_013990_Stage2_2024-01-10 | 013990 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_stage2_false_positive_or_overpromotion_risk | True | True |
| R13_CROSS_013990_2024-01-10_Stage2 | 013990 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive | True | True |
| R10L90_C30_014280_20240213_STAGE2_FALSE_POSITIVE_FORMWORK_REBOUND | 014280 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive_if_formwork_material_rebound_overcredited | True | True |
| C16-102-04-014580-T1 | 014580 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_missed_structural | True | True |
| R1L117-C01-004 | 014620 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_missed_structural | False | True |
| R1L117-C01-004 | 014620 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_missed_structural | True | True |
| HANSOLCHEM_014680_2024_03_06_STAGE2_FALSE_POSITIVE_MEMORY_CHEMICAL_BETA | 014680 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_false_positive | False | True |
| HANSOLCHEM_014680_2024_03_06_STAGE2_FALSE_POSITIVE_MEMORY_MATERIALS_RECOVERY | 014680 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_false_positive | False | True |
| R4L93_C17_014680_20240227_STAGE2_SPECIALTY_CHEM_SPREAD_RESET | 014680 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_correct_if_spread_cost_margin_FCF_bridge_required_but_Green_strict | True | True |
| None | 014680 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | True | True |
| R5_L122_C18_015 | 014710 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | True | True |
| C19_R5L119_11_014710_4B_Local_Watch_2024-06-13 | 014710 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | True | True |
| C20_R5L119_014710_20240613_08_Stage4B_Local_Watch | 014710 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | None | True | True |
| C20_R5L118_014710_20240613_Stage4B | 014710 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_error | True | True |
| T_C05_R1L109_014790_20240429_REPAIR_BOUNCE_WITHOUT_FCF | 014790 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | True | True |
| TRG_R10L81-C30-014790-HL-DNI-MID-BUILDER-ORDERBOOK-RECOVERY | 014790 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should allow builder recovery rows only when orderbook, housing project quality, PF exposure, refinancing access, liquidity and margin bridge are visible. HL D&I produced large MFE with controlled entry-basis MAE, but it cannot become durable recovery without PF/orderbook source repair. | True | True |
| None | 014790 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | True | True |
| R10L92_C30_HLDNI_2024_STAGE2_ACTIONABLE_MID_BUILDER_PF_ORDER_BALANCE_REPAIR | 014790 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R10L83_C30_014790_20240604_STAGE2_PF_REPAIR_BRIDGE_POSITIVE | 014790 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_correct | True | True |
| R3L95_C13_DONGWONSYSTEMS_2024_STAGE2_ACTIONABLE_BATTERY_PACKAGING_CAN_JV_UTILIZATION_MARGIN | 014820 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R3L91_C13_014820_20240321_STAGE2_FALSE_POSITIVE_PACKAGING_CAN_MATERIALS | 014820 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_false_positive_if_packaging_can_materials_vocabulary_overcredited | True | True |
| TRG_R4L76-C17-014830-UNID-KOH-CAUSTIC-POTASH-SPREAD-BRIDGE | 014830 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | C17 should allow chemical commodity Stage2 when the commodity price/spread move connects to inventory, export demand, utilization and margin bridge. Unid produced large MFE with controlled entry-basis MAE, but the later post-peak drawdown requires lifecycle local 4B if KOH/spread/margin evidence fades. | True | True |
| TRG_R4L76-C17-014830-UNID-KOH-CAUSTIC-POTASH-SPREAD-BRIDGE | 014830 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_correct | True | True |
| UNID_014830_2024_01_25_STAGE2A_CAUSTIC_POTASH_SPREAD | 014830 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_4B_too_late | False | True |
| TRG_R4L79-C17-014830-UNID-KOH-SPREAD-MARGIN-LIFECYCLE | 014830 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | C17 should allow chemical spread positives only when commodity price/cost spread, export demand, inventory, utilization and margin bridge refreshes. Unid produced meaningful MFE and then a drawdown; it is Stage2 only after source repair and lifecycle-managed if spread/margin evidence fades. | True | True |
| TRG_R4L73-C17-014830-UNID-CAUSTIC-POTASH-SPREAD-MARGIN-BRIDGE | 014830 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | C17 should allow Stage2 only when a commodity/spread move connects to product-specific spread, export price, cost pass-through, and margin conversion. 유니드 produced a real MFE path, but later collapse means local 4B-watch should activate if spread evidence stops refreshing. | True | True |
| TRG_R4L73-C17-014830-UNID-CAUSTIC-POTASH-SPREAD-MARGIN-BRIDGE | 014830 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | C17 should allow Stage2 only when a commodity/spread move connects to product-specific spread, export price, cost pass-through, and margin conversion. 유니드 produced a real MFE path, but later collapse means local 4B-watch should activate if spread evidence stops refreshing. | True | True |
| None | 014830 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | True | True |
| None | 015710 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | None | False | True |
| R9L94_C29_SUNGWOOHITEC_2024_STAGE2_ACTIONABLE_AUTO_PARTS_GLOBAL_VOLUME_MARGIN_BRIDGE | 015750 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| None | 015750 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | True | True |
| V12_COMPACT_R13L11-4B4C-017_015750_2024-02-26_cross_archetype_4b_4c_boundary_retest | 015750 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R13_CROSS_015750_2024-02-26_Stage3-Yellow | 015750 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| TRG_R12L79-C31-015760-KEPCO-TARIFF-NORMALIZATION-DEBT-RECOVERY | 015760 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 can allow public-utility policy rows when tariff normalization maps to direct beneficiary economics, fuel-cost pass-through, debt recovery, earnings bridge and regulatory visibility. KEPCO produced meaningful MFE with bounded entry-basis MAE, but later drawdown means tariff/debt/earnings evidence must refresh. | True | True |
| None | 016250 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | True | True |
| T_C05_R1L108_016250_20240130_HEAVY_CIVIL_COUNTER | 016250 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | True | True |
| R10L97_C30_SGCEC_2024_STAGE2_FALSE_POSITIVE_MIDCAP_EPC_PF_RECOVERY_WATCH | 016250 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive_if_midcap_EPC_PF_watch_counts_without_cashflow_funding_order_quality_margin_revision_bridge | True | True |
| R13_L106_T20_016250 | 016250 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive | True | True |
| None | 016360 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | True | True |
| None | 016360 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | False | True |
| None | 016360 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | True | True |
| C31_R11L106_TRG_12 | 016360 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | None | True | True |
| C32_016360_20240207_STAGE2_ACTIONABLE | 016360 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive_or_overpromotion_risk | True | True |
| R4L93_C15_KGSTEEL_2024_STAGE2_FALSE_POSITIVE_STEEL_COIL_SPREAD_WATCH | 016380 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive_if_steel_spread_theme_counts_without_ASP_margin_revision_bridge | True | True |
| R13L93_REVIEW_R4_C15_MATERIAL_SPREAD_SUPERCYCLE_016380_2024_02_05_TRIGGER | 016380 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_steel_spread_theme_counts_without_ASP_margin_revision_bridge | True | True |
| R6L92_C21_DBSEC_2024_STAGE4B_BROKERAGE_CAPITAL_RETURN_EVENT_CAP | 016610 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_4B_too_late_if_brokerage_capital_return_event_premium_not_capped | True | True |
| R13L92_REVIEW_R6_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_016610_2024_02_23_TRIGGER | 016610 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_4B_too_late_if_brokerage_capital_return_event_premium_not_capped | True | True |
| R10L96_C30_SHINWONDEV_2024_STAGE2_FALSE_POSITIVE_SMALL_BUILDER_PF_RECOVERY_WATCH | 017000 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive_if_small_builder_PF_recovery_watch_counts_without_cashflow_funding_order_margin_bridge | True | True |
| R13L96_REVIEW_R10_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_017000_2024_01_02_TRIGGER | 017000 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_small_builder_PF_recovery_watch_counts_without_cashflow_funding_order_margin_bridge | True | True |
| KWANGMYUNG_017040_2024_05_07_STAGE2_FALSE_POSITIVE_SWITCHGEAR_EVENT_PREMIUM | 017040 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_false_positive | False | True |
| TRG_R1L78-C02-017040-KWANGMYUNG-ELECTRIC-SWITCHGEAR-THEME-FADE | 017040 | C02_POWER_GRID_DATACENTER_CAPEX | C02 should not treat switchgear/electrical-equipment theme beta as durable Stage2 unless customer order, backlog conversion, delivery schedule, ASP and margin bridge are visible. Kwangmyung Electric produced a strong theme MFE, then opened a high-MAE drawdown path, making it local 4B-watch rather than durable Green. | True | True |
| V12_COMPACT_R13L11-4B4C-004_017040_2024-05-07_cross_archetype_4b_4c_boundary_retest | 017040 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| V12_COMPACT_R13L2_C02_017040_20240507_STAGE2ACTIONABLE_017040_2024-05-07_cross_archetype_high_MAE_guardrail_review | 017040 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| T_R13_STAGE2FP_L6_017040_Stage2Actionable_2024-05-07 | 017040 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_stage2_false_positive_or_overpromotion_risk | True | True |
| SEMYUNG_017510_2024_04_05_STAGE2A_GRID_COMPONENT_ORDER_BETA | 017510 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_4B_too_late | False | True |
| R1L95_C02_SEMYOUNGELECTRIC_2024_STAGE4B_TRANSMISSION_FITTING_GRID_EVENT_CAP | 017510 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_4B_too_late_if_transmission_fitting_grid_event_premium_not_capped | True | True |
| R13L95_REVIEW_R1_C02_POWER_GRID_DATACENTER_CAPEX_017510_2024_07_10_TRIGGER | 017510 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late_if_transmission_fitting_grid_event_premium_not_capped | True | True |
| R13_L106_T14_017510 | 017510 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_4B_too_late | True | True |
| TRG_R5L79-C18-017810-PULMUONE-GLOBAL-FOOD-CHANNEL-REORDER | 017810 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | C18 should preserve food-channel positives when overseas/online channel reorder, product mix, volume, revenue conversion and margin bridge are visible. Pulmuone produced high MFE with very bounded entry-basis MAE, but post-peak drawdown requires lifecycle management. | True | True |
| TRG_R5L75-C18-017810-PULMUONE-TOFU-HMR-US-CHANNEL-REORDER | 017810 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | C18 should include food names when overseas refrigerated channel reorder, utilization, logistics and margin conversion are visible. Pulmuone produced a clean multi-month MFE path, but later drawdown says the model needs lifecycle decay if reorder/margin evidence stalls. | True | True |
| TRG_R5L75-C18-017810-PULMUONE-TOFU-HMR-US-CHANNEL-REORDER | 017810 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_correct | True | True |
| TRG_R5L73-C18-018250-AEKYUNG-EXPORT-CHANNEL-ONE-CANDLE-FADE | 018250 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | C18 should not treat a short export/channel rally as durable Green when reorder, sell-through or margin evidence fails to refresh. Aekyung generated MFE but later opened deep MAE and drawdown. | True | True |
| None | 018250 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | True | True |
| TRG_R5L73-C18-018250-AEKYUNG-EXPORT-CHANNEL-ONE-CANDLE-FADE | 018250 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | C18 should not treat a short export/channel rally as durable Green when reorder, sell-through or margin evidence fails to refresh. Aekyung generated MFE but later opened deep MAE and drawdown. | True | True |
| R5L100_C20_AEKYUNGIND_2024_STAGE2_FALSE_POSITIVE_LEGACY_BEAUTY_CHANNEL_WATCH | 018250 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive_if_legacy_beauty_channel_watch_counts_without_sellthrough_reorder_inventory_OPM_revision_bridge | True | True |
| R5L88_C20_018250_20240531_STAGE2_FALSE_POSITIVE_MASS_BEAUTY_EXTENSION | 018250 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive_if_mass_beauty_extension_overcredited | True | True |
| R13L88_REVIEW_R5_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_018250_2024-05-31 | 018250 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| None | 018250 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | None | True | True |
| R5L89_C18_VT_2024_STAGE2_ACTIONABLE_KBEAUTY_EXPORT_REORDER | 018290 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R5L85_C20_018290_20240321_STAGE2_KBEAUTY_GLOBAL_SELLTHROUGH_BRIDGE | 018290 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_correct_if_sellthrough_distribution_bridge_required | True | True |
| C20_R5_L102_T02_018290 | 018290 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_correct | True | True |
| R13L85_REVIEW_R5_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_018290_2024-03-21 | 018290 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_correct | True | True |
| R3L100-C14-006-T1 | 018470 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_too_conservative_if_all_battery_input_materials_route_to_4C | True | True |
| R4L90_C15_CHOILALUMINUM_2024_STAGE2_FALSE_POSITIVE_ALUMINUM_THEME | 018470 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive_if_aluminum_theme_counts_without_spread_margin_bridge | True | True |
| R4L90_C16_018470_20240220_STAGE2_FALSE_POSITIVE_ALUMINUM_SHEET | 018470 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_false_positive_if_aluminum_sheet_rebound_overcredited | True | True |
| R13L90_REVIEW_R4_C15_MATERIAL_SPREAD_SUPERCYCLE_018470_2024_04_18_TRIGGER | 018470 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive_if_aluminum_theme_counts_without_spread_margin_bridge | True | True |
| TRG_R9L76-C29-018880-HANON-SYSTEMS-EV-THERMAL-UTILIZATION-FADE | 018880 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| TRG_R9L73-C29-018880-HANON-THERMAL-EV-BETA-LOCAL4B | 018880 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should not treat EV thermal-management or auto-parts theme beta as durable Stage2 when customer volume, pricing and margin conversion are weak. Hanon generated only small MFE and later severe MAE, making it a local 4B-watch / false Stage2 row. | True | True |
| T_C29_R9L105_018880_Stage2_20240503 | 018880 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| TRG_R9L76-C29-018880-HANON-SYSTEMS-EV-THERMAL-UTILIZATION-FADE | 018880 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should not treat EV thermal-management beta as durable Stage2 unless customer volume, platform program, utilization, pricing/mix and margin bridge are visible. Hanon Systems had limited MFE and then opened a high-MAE drawdown path. | True | True |
| TRG_R9L73-C29-018880-HANON-THERMAL-EV-BETA-LOCAL4B | 018880 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should not treat EV thermal-management or auto-parts theme beta as durable Stage2 when customer volume, pricing and margin conversion are weak. Hanon generated only small MFE and later severe MAE, making it a local 4B-watch / false Stage2 row. | True | True |
| TRG_R9L78-C29-018880-HANON-THERMAL-EV-PARTS-THEME-FADE | 018880 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should not treat thermal-management or EV-parts beta as durable Stage2 unless customer program, volume, pricing, utilization and margin bridge are visible. Hanon Systems had only small MFE and then a severe MAE drawdown path. | True | True |
| None | 018880 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | False | True |
| T_C29_R9L106_018880_20240503_06_Stage4C | 018880 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| R7L88_C23_019170_20240325_STAGE2_FALSE_POSITIVE_CLINICAL_THEME | 019170 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive_if_clinical_regulatory_theme_overcredited | True | True |
| R13L88_REVIEW_R7_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_019170_2024-03-25 | 019170 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| C04_P1_TO50_TRG_19 | 019990 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive | True | True |
| C04_R1_L112_019990_2024_07_17_CZECH_PREFERRED_BIDDER_ACTUATOR_THEME_FALSE_POSITIVE_TRIGGER | 019990 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive | True | True |
| C04_STATIC_TO50_TRG_10 | 019990 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive | True | True |
| R1L90_C04_019990_20240222_STAGE2_FALSE_POSITIVE_ACTUATOR_POLICY_REBOUND | 019990 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive_if_actuator_policy_rebound_overcredited | True | True |
| R11L96_C04_ENERTORK_2024_STAGE4B_NUCLEAR_ACTUATOR_POLICY_EVENT_CAP | 019990 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_4B_too_late_if_nuclear_actuator_policy_event_premium_not_capped | True | True |
| R13L96_REVIEW_R11_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_019990_2024_01_15_TRIGGER | 019990 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late_if_nuclear_actuator_policy_event_premium_not_capped | True | True |
| R5_L122_C18_009 | 020000 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | True | True |
| None | 020000 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | True | True |
| TRG_R5L76-C19-020000-HANDSOME-APPAREL-RETAIL-INVENTORY-BETA-FADE | 020000 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_false_positive | True | True |
| C19_R5L120_09_020000_Stage2_2024-02-07 | 020000 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | True | True |
| R5L93_C19_HANDSOME_2024_STAGE2_FALSE_POSITIVE_FASHION_RETAIL_INVENTORY_WATCH | 020000 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_false_positive_if_fashion_retail_inventory_watch_counts_without_sellthrough_margin_revision_bridge | True | True |
| 020000_2024-11-15_Stage2_Actionable_C19_INVENTORY_CLEAN_LOW_MAE_VALUE_RERATING_POSITIVE | 020000 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_correct | False | True |
| TRG_R5L76-C19-020000-HANDSOME-APPAREL-RETAIL-INVENTORY-BETA-FADE | 020000 | C19_BRAND_RETAIL_INVENTORY_MARGIN | C19 should not treat apparel retail or inventory-normalization beta as durable Stage2 unless sell-through, markdown control, channel productivity and margin bridge are visible. Handsome had a brief MFE but later faded into a lower range; share-count movement inside the window requires validation. | True | True |
| R5L90_C19_020000_20240207_STAGE2_FALSE_POSITIVE_PREMIUM_APPAREL | 020000 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_false_positive_if_premium_apparel_rebound_overcredited | True | True |
| None | 020000 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | True | True |
| R13_CROSS_020000_2024-04-11_Stage4B-Local-DomesticFashionInventoryMargin | 020000 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_false_positive | True | True |
| V12_COMPACT_C20_R5L120_020000_20240207_04_020000_2024-02-07_Stage2 | 020000 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | True | True |
| R13L93_REVIEW_R5_C19_BRAND_RETAIL_INVENTORY_MARGIN_020000_2024_02_07_TRIGGER | 020000 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_fashion_retail_inventory_watch_counts_without_sellthrough_margin_revision_bridge | True | True |
| T_C11_R3L107_020150_STAGE2ACTIONABLE_20240321 | 020150 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_needs_high_MAE_guard_before_green | True | True |
| R3L93_C11_020150_20240102_STAGE2_FALSE_POSITIVE_COPPER_FOIL_ORDERBOOK | 020150 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive_if_copper_foil_orderbook_vocabulary_overcredited | True | True |
| None | 020150 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive_if_old_orderbook_memory_keeps_Yellow_without_margin_bridge | True | True |
| TRG_R3L75-C12-020150-LOTTE-ENERGY-MATERIALS-COPPER-FOIL-CONTRACT-BRIDGE | 020150 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | C12 should allow Stage2 when copper-foil customer contracts, delivery schedule, capacity utilization and margin bridge are explicit. Lotte Energy Materials produced high MFE with low entry-basis MAE, but later drawdown shows lifecycle local 4B is needed if customer call-off or margin evidence fades. | True | True |
| TRG_R3L75-C12-020150-LOTTE-ENERGY-MATERIALS-COPPER-FOIL-CONTRACT-BRIDGE | 020150 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_correct | True | True |
| V12_COMPACT_C12_R3L105_020150_20240607_10_020150_2024-06-07_Stage2-Actionable | 020150 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_false_positive | True | True |
| R3L98_C12_LOTTEEM_2024_STAGE2_FALSE_POSITIVE_COPPERFOIL_CUSTOMER_CALLOFF_WATCH | 020150 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_false_positive_if_copperfoil_customer_contract_watch_counts_without_calloff_volume_inventory_margin_revision_bridge | True | True |
| None | 020150 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | True | True |
| None | 020150 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | True | True |
| T_C13_R3L105_020150_STAGE2ACTIONABLE_20240321 | 020150 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | True | True |
| None | 020150 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | False | True |
| None | 020150 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | True | True |
| TRG_R3L81-C13-020150-LOTTE-ENERGY-MATERIALS-COPPERFOIL-UTILIZATION-RECOVERY | 020150 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | C13 can preserve copper-foil recovery positives when customer volume, utilization, IRA/AMPC economics and margin bridge are visible. Lotte Energy Materials had tradable MFE with bounded entry-basis MAE, but post-peak drawdown means bridge refresh is required. | True | True |
| T_C13_R3L105_020150_STAGE3YELLOW_20240321 | 020150 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | True | True |
| T_C14_R3L108_020150_STAGE3YELLOW_20240321 | 020150 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_false_positive | True | True |
| T_R13_STAGE2FP_L6_020150_Stage2_2024-06-12 | 020150 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_stage2_false_positive_or_overpromotion_risk | True | True |
| TRG_R9L81-C29-020560-ASIANA-AIRLINE-MERGER-TRANSPORT-MARGIN-FADE | 020560 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should not treat airline merger/transport beta as durable volume-margin operating leverage unless passenger volume, yield, fuel-cost pass-through, integration path, revenue and margin bridge are visible. Asiana had early MFE, then a persistent high-MAE drawdown. The profile has a 2024-12-30 corporate-action candidate outside the selected 180D window, so extended-window ingestion needs validation. | True | True |
| TRG_R4L77-C15-021050-SEOWON-COPPER-ALLOY-SPREAD-THEME-FADE | 021050 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive | True | True |
| TRG_R4L77-C15-021050-SEOWON-COPPER-ALLOY-SPREAD-THEME-FADE | 021050 | C15_MATERIAL_SPREAD_SUPERCYCLE | C15 should not treat copper alloy or nonferrous theme spikes as durable Stage2 unless order, volume, inventory and margin bridge are visible. Seowon produced high MFE but then leaked back into a broad range, making it a local 4B-watch row rather than durable Green. | True | True |
| R4L85_C16_021050_20240520_STAGE2_FALSE_POSITIVE_COPPER_THEME_SPIKE | 021050 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_false_positive_if_policy_supply_theme_overcredited | True | True |
| C16-102-08-021050-T1 | 021050 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_false_positive | True | True |
| R13L85_REVIEW_R4_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_021050_2024-05-20 | 021050 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| TRG_R10L79-C30-021320-KCC-E&C-PF-BOUNDED-RISKWATCH-NO-FORCED4B | 021320 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should keep PF/orderbook monitoring active for bounded builders, but should not force local 4B or hard 4C when MAE is contained and no non-price refinancing or solvency break is confirmed. KCC E&C is a boundary row. | True | True |
| TRG_R10L74-C30-021320-KCC-CONSTRUCTION-RISKWATCH-NO-HARD4C | 021320 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should not convert every regional-builder PF fear into full 4B or hard 4C when the price path has moderate MAE, tradable MFE and no confirmed non-price break. KCC Construction is a RiskWatch/no-hard-4C boundary row. | True | True |
| R10L85_C30_021320_20240123_STAGE2_REGIONAL_CONTRACTOR_REPAIR_CONTROL | 021320 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_correct_if_balance_sheet_repair_bridge_required | True | True |
| TRG_R10L74-C30-021320-KCC-CONSTRUCTION-RISKWATCH-NO-HARD4C | 021320 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should not convert every regional-builder PF fear into full 4B or hard 4C when the price path has moderate MAE, tradable MFE and no confirmed non-price break. KCC Construction is a RiskWatch/no-hard-4C boundary row. | True | True |
| R10L91_C30_KCCCONST_2024_STAGE4B_CONSTRUCTION_PF_EVENT_CAP | 021320 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_4B_too_late_if_construction_PF_event_premium_not_capped | True | True |
| R13L85_REVIEW_R10_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_021320_2024-01-23 | 021320 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_correct | True | True |
| R13L91_REVIEW_R10_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_021320_2024_04_08_TRIGGER | 021320 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_4B_too_late_if_construction_PF_event_premium_not_capped | True | True |
| R11L92_C05_023350_20240110_STAGE2_FALSE_POSITIVE_ENGINEERING_POLICY_PROJECT | 023350 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | current_profile_false_positive_if_engineering_policy_project_vocabulary_overcredited | True | True |
| R10L90_C30_023410_20240223_STAGE2_FALSE_POSITIVE_READY_MIX_POLICY | 023410 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive_if_ready_mix_policy_MFE_overcredited | True | True |
| TRG_C19_023530_20240208_RETAIL_VALUEUP_NO_INVENTORY_MARGIN_BRIDGE | 023530 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_false_positive | True | True |
| R5L97_C19_LOTTESHOPPING_2024_STAGE2_ACTIONABLE_DEPARTMENT_STORE_RETAIL_INVENTORY_MARGIN_BRIDGE | 023530 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| TRG_R5L81-C19-023530-LOTTE-SHOPPING-RETAIL-MARGIN-VALUEUP-LIFECYCLE | 023530 | C19_BRAND_RETAIL_INVENTORY_MARGIN | C19 should allow department-store/retail positives only when value-up or channel recovery maps to inventory turnover, cost control, revenue mix and margin bridge. Lotte Shopping had a tradable early MFE but later high MAE, so it is lifecycle-managed rather than durable Green. | True | True |
| TRG_R5L78-C19-023530-LOTTE-SHOPPING-RETAIL-INVENTORY-MARGIN-LIFECYCLE | 023530 | C19_BRAND_RETAIL_INVENTORY_MARGIN | C19 should allow large-cap retail inventory-normalization positives when channel productivity, inventory turnover, markdown discipline, cost control and margin bridge are visible. Lotte Shopping produced a meaningful MFE from a low-risk entry, but the later post-peak drawdown requires lifecycle local 4B if inventory/margin evidence fades. | True | True |
| TRG_R9L75-C29-023800-INZI-CONTROLS-THERMAL-MANAGEMENT-BETA-FADE | 023800 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| TRG_R9L75-C29-023800-INZI-CONTROLS-THERMAL-MANAGEMENT-BETA-FADE | 023800 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should not treat thermal-management or cooling-system theme beta as durable Stage2 unless customer volume, OEM program, pricing/mix and margin bridge refreshes. Inzi Controls had a sharp tradable spike but later opened large MAE and drawdown. | True | True |
| R9L90_C29_INFAC_2024_STAGE4B_EV_WIREHARNESS_MOBILITY_THEME_CAP | 023810 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_4B_too_late_if_EV_wireharness_mobility_theme_premium_not_capped | True | True |
| R13L90_REVIEW_R9_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_023810_2024_03_20_TRIGGER | 023810 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_4B_too_late_if_EV_wireharness_mobility_theme_premium_not_capped | True | True |
| R11L92_C05_023960_20240129_STAGE2_FALSE_POSITIVE_SMALL_EPC_LATE_SPIKE | 023960 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | current_profile_false_positive_if_late_spike_validates_original_small_EPC_vocabulary_entry | True | True |
| R4L93_C15_HEUNGGOO_2024_STAGE4B_OIL_RESOURCE_SPREAD_EVENT_CAP | 024060 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_4B_too_late_if_oil_resource_event_premium_not_capped | True | True |
| R12L87_C31_024060_20240604_STAGE2_FALSE_POSITIVE_DISTRIBUTOR_THEME | 024060 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive_if_oil_distributor_theme_overcredited | True | True |
| R13L87_REVIEW_R12_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_024060_2024-06-04 | 024060 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R13L93_REVIEW_R4_C15_MATERIAL_SPREAD_SUPERCYCLE_024060_2024_06_04_TRIGGER | 024060 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late_if_oil_resource_event_premium_not_capped | True | True |
| None | 024070 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | True | True |
| V12_COMPACT_C21-IBK-20240314_024110_2024-03-14_Stage3_Yellow_LowPBR_Dividend_Label_LateChase | 024110 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | False | True |
| R6L89_C21_024110_20240124_STAGE2_BANK_VALUEUP_CAPITAL_RETURN | 024110 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_correct_if_ROE_PBR_capital_return_bridge_required | True | True |
| R6L100_C21_IBK_2024_STAGE2_ACTIONABLE_BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN_BRIDGE | 024110 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| TRG_R6L73-C21-024110-IBK-HIGH-DIVIDEND-PBR-ROE-BRIDGE | 024110 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | C21 should include slower high-dividend/value-up bank paths when dividend yield, low PBR, capital discipline and stable ROE support the rerating. IBK produced strong MFE with essentially no entry-basis MAE. | True | True |
| TRG_R6L73-C21-024110-IBK-HIGH-DIVIDEND-PBR-ROE-BRIDGE | 024110 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | C21 should include slower high-dividend/value-up bank paths when dividend yield, low PBR, capital discipline and stable ROE support the rerating. IBK produced strong MFE with essentially no entry-basis MAE. | True | True |
| None | 024110 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | True | True |
| None | 024110 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | False | True |
| R6L88_C21_IBK_2024_STAGE4B_POLICY_BANK_VALUEUP_CAP | 024110 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_4B_too_late_if_policy_bank_valueup_premium_not_capped | True | True |
| V12_COMPACT_024110_2024-04-26_policy_valueup_bank_brokerage_ROE_PBR_capital_return_execution_bridge | 024110 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | True | True |
| C31_R11L106_TRG_08 | 024110 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | None | True | True |
| R11L97_C03_HANILFORGING_2024_STAGE4B_MUNITION_ARTILLERY_EXPORT_EVENT_CAP | 024740 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_4B_too_late_if_munition_artillery_export_event_premium_not_capped | True | True |
| R1L94_C03_HANILFORGING_2024_STAGE4B_MUNITION_FORGING_DEFENSE_EVENT_CAP | 024740 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_4B_too_late_if_munition_forging_defense_event_premium_not_capped | True | True |
| R13L94_REVIEW_R1_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_024740_2024_01_17_TRIGGER | 024740 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_4B_too_late_if_munition_forging_defense_event_premium_not_capped | True | True |
| R1L98_C02_KBIMETAL_2024_STAGE4B_CABLE_COPPER_GRID_EVENT_CAP | 024840 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_4B_too_late_if_cable_copper_grid_event_premium_not_capped | True | True |
| R4L90_C15_KBIMETAL_2024_STAGE2_ACTIONABLE_COPPER_SPREAD_MARGIN_BRIDGE | 024840 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R4L88_C15_024840_20240412_STAGE2_COPPER_METAL_SPREAD | 024840 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_correct_if_inventory_ASP_margin_bridge_required | True | True |
| R4L101_C16_KBIMETAL_2024_STAGE2_ACTIONABLE_COPPER_CABLE_OFFTAKE_SUPPLY_EXECUTION | 024840 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| None | 024840 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| R13L88_REVIEW_R4_C15_MATERIAL_SPREAD_SUPERCYCLE_024840_2024-04-12 | 024840 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_correct | True | True |
| None | 024890 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| R4L98_C16_DAEWONCHEM_2024_STAGE4B_LITHIUM_MATERIAL_SUPPLY_EVENT_CAP | 024890 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_4B_too_late_if_lithium_material_supply_event_premium_not_capped | True | True |
| TRG_R9L75-C29-024900-DY-DEOKYANG-BODY-BATTERY-HOUSING-BETA-FADE | 024900 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| TRG_R9L75-C29-024900-DY-DEOKYANG-BODY-BATTERY-HOUSING-BETA-FADE | 024900 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should not treat body-module, interior or battery-housing beta as durable Stage2 unless OEM volume, product mix, program award, pricing and margin bridge are visible. Deokyang Industrial produced a strong early MFE but then opened high MAE and a deep drawdown. | True | True |
| R9L87_C29_024900_20240202_STAGE2_FALSE_POSITIVE_AUTOPARTS_VOLUME_THEME | 024900 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive_if_autoparts_theme_promoted_without_operating_leverage | True | True |
| R9L92_C29_DUCKYANG_2024_STAGE4B_INTERIOR_MODULE_MOBILITY_EVENT_CAP | 024900 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_4B_too_late_if_interior_module_mobility_event_premium_not_capped | True | True |
| R13L87_REVIEW_R9_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_024900_2024-02-02 | 024900 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R13L92_REVIEW_R9_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_024900_2024_02_05_TRIGGER | 024900 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_4B_too_late_if_interior_module_mobility_event_premium_not_capped | True | True |
| TRG_R4L79-C17-025000-KPX-CHEMICAL-POLYOL-SPREAD-DEFENSIVE-NO-STAGE2 | 025000 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | C17 should not force local 4B when a chemical name has bounded MAE and defensive cashflow, but it also should not mark Stage2 unless spread expansion, volume, utilization and margin bridge are visible. KPX Chemical is a low-volatility boundary row. | True | True |
| TRG_R4L82-C17-025000-KPX-CHEMICAL-POLYOL-SPREAD-BOUNDED | 025000 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | C17 should allow chemical spread recovery candidates only when input-cost pass-through, customer volume, utilization, pricing and margin bridge are visible. KPX Chemical had bounded MAE and mild MFE, so it is a RiskWatch/Stage2-Yellow candidate after source repair, not a forced 4B row. | True | True |
| None | 025000 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | True | True |
| TRG_R9L80-C29-025540-KET-AUTO-CONNECTOR-THEME-LOCAL4B | 025540 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should not treat auto connector/electronics theme beta as durable Stage2 unless customer program volume, connector content growth, utilization, pricing and margin bridge are visible. Korea Electric Terminal had modest MFE and later high MAE. | True | True |
| R10L91_C30_025750_20240110_STAGE2_FALSE_POSITIVE_HOME_MATERIALS | 025750 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive_if_home_materials_rebound_overcredited | True | True |
| TRG_R4L74-C15-025820-IGU-COPPER-FABRICATOR-SPREAD-BRIDGE | 025820 | C15_MATERIAL_SPREAD_SUPERCYCLE | C15 should allow Stage2 when copper rally is tied to product-specific spread, inventory effect, export price and margin bridge. Igu Industry produced a strong copper-cycle MFE, but the late-2024 collapse requires local 4B-watch if spread/margin evidence stops refreshing. | True | True |
| TRG_R4L77-C15-025820-IGOO-COPPER-SPREAD-INVENTORY-MARGIN-LIFECYCLE | 025820 | C15_MATERIAL_SPREAD_SUPERCYCLE | C15 should allow nonferrous/copper processors when copper price/spread, inventory revaluation, volume and margin bridge are visible. Igoo Industry produced large MFE with controlled entry-basis MAE, but later drawdown requires lifecycle local 4B if spread/margin evidence fades. | True | True |
| TRG_R4L77-C15-025820-IGOO-COPPER-SPREAD-INVENTORY-MARGIN-LIFECYCLE | 025820 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_correct | True | True |
| TRG_R4L74-C15-025820-IGU-COPPER-FABRICATOR-SPREAD-BRIDGE | 025820 | C15_MATERIAL_SPREAD_SUPERCYCLE | C15 should allow Stage2 when copper rally is tied to product-specific spread, inventory effect, export price and margin bridge. Igu Industry produced a strong copper-cycle MFE, but the late-2024 collapse requires local 4B-watch if spread/margin evidence stops refreshing. | True | True |
| R4L85_C16_025820_20240520_STAGE2_FALSE_POSITIVE_SMALLCAP_COPPER_THEME | 025820 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_false_positive_if_copper_theme_overcredited | True | True |
| R4L92_C16_EGU_2024_STAGE4B_COPPER_RESOURCE_EVENT_CAP | 025820 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_4B_too_late_if_copper_resource_event_premium_not_capped | True | True |
| R13L85_REVIEW_R4_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_025820_2024-05-20 | 025820 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| R13L92_REVIEW_R4_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_025820_2024_04_05_TRIGGER | 025820 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_4B_too_late_if_copper_resource_event_premium_not_capped | True | True |
| C15-FERT-001_TRIGGER | 025860 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_correct | True | True |
| None | 025860 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| None | 025860 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| None | 025860 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | True | True |
| R9L95_C14_DONGWHA_2024_STAGE4B_ELECTROLYTE_POST_CA_EV_DEMAND_EVENT_CAP | 025900 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_4B_too_late_if_electrolyte_post_CA_EV_demand_event_premium_not_capped | True | True |
| R13L95_REVIEW_R9_C14_EV_DEMAND_SLOWDOWN_4B_4C_025900_2024_06_10_TRIGGER | 025900 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late_if_electrolyte_post_CA_EV_demand_event_premium_not_capped | True | True |
| R10L93_C30_DONGSHIN_2024_STAGE4B_REGIONAL_POLICY_BUILDER_EVENT_CAP | 025950 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_4B_too_late_if_regional_builder_policy_event_premium_not_capped | True | True |
| R13L93_REVIEW_R10_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_025950_2024_03_25_TRIGGER | 025950 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late_if_regional_builder_policy_event_premium_not_capped | True | True |
| R11L88_C05_026150_20240130_STAGE2_FALSE_POSITIVE_CIVIL_WORKS_THEME | 026150 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | current_profile_false_positive_if_civil_works_theme_promoted_without_contract_margin_bridge | True | True |
| R13L88_REVIEW_R11_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_026150_2024-01-30 | 026150 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R5L95_C20_COREANA_2024_STAGE2_FALSE_POSITIVE_MASS_BEAUTY_EXPORT_SYMPATHY | 027050 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive_if_mass_beauty_export_sympathy_counts_without_channel_reorder_margin_revision_bridge | True | True |
| R13L95_REVIEW_R5_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_027050_2024_05_24_TRIGGER | 027050 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_mass_beauty_export_sympathy_counts_without_channel_reorder_margin_revision_bridge | True | True |
| TRG_R12L81-C31-027710-FARMSTORY-FEED-FOOD-SECURITY-THEME-FADE | 027710 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should not treat feed/food-security policy beta as durable Stage2 unless direct feed/meat demand, input cost pass-through, customer volume, revenue and margin bridge are visible. FarmStory had almost no post-entry MFE and then a persistent MAE path. | True | True |
| T_C01_R1L111_028050_20240228_Stage2-Actionable | 028050 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | EPC/plant order headline belongs to C05 unless margin gap and working-capital bridge are confirmed; C01 generic backlog would over-score it | True | True |
| R1L88_C05_SAMSUNGEA_2023_STAGE2_ACTIONABLE_EPC_MARGIN_BRIDGE | 028050 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| TRG_C05_028050_20230131_STAGE2_ACTIONABLE | 028050 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | current_profile_missed_structural_if_C05_has_no_runtime_weight | True | True |
| None | 028050 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | True | True |
| R11L90_C05_SAMSUNGEA_2024_STAGE2_FALSE_POSITIVE_PLANT_EPC_MARGIN_GAP | 028050 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | current_profile_false_positive_if_EPC_order_label_counts_without_margin_execution_revision_bridge | True | True |
| T_C05_R1L108_028050_20240228_PLANT_ORDER_MARGIN_GAP | 028050 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | True | True |
| R1L97_C05_SAMSUNGEA_2024_STAGE2_FALSE_POSITIVE_GLOBAL_EPC_MARGIN_GAP_WATCH | 028050 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | current_profile_false_positive_if_global_EPC_contract_watch_counts_without_cost_to_complete_change_order_margin_revision_bridge | True | True |
| T_C05_R1L109_028050_20240424_EPC_PROJECT_MARGIN_BRIDGE | 028050 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | True | True |
| R1L86_C05_028050_20240611_STAGE2_EPC_MARGIN_RECOVERY | 028050 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | current_profile_correct_if_margin_recovery_bridge_required | True | True |
| R1L91_C05_028050_20240422_STAGE2_FALSE_POSITIVE_EPC_REBRAND | 028050 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | current_profile_false_positive_if_large_EPC_vocabulary_overcredited | True | True |
| R1L84_C05_028050_20240311_STAGE2_FALSE_POSITIVE_MARGIN_GAP | 028050 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | current_profile_false_positive_if_headline_overcredited | True | True |
| None | 028050 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | False | True |
| T_C05_R1L108_028050_20240626_POST_PEAK_LOCAL4B | 028050 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | True | True |
| R10L88_C30_028050_20240201_STAGE2_ENGINEERING_BACKLOG_CASH | 028050 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_correct_if_backlog_margin_cash_bridge_required | True | True |
| C30_R10L105_028050_20240228_Stage2_Actionable | 028050 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_error_if_C30_overcredits_price_or_low_PBR_without_balance_sheet_bridge | True | True |
| None | 028050 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | True | True |
| None | 028050 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | None | False | True |
| R13L88_REVIEW_R10_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_028050_2024-02-01 | 028050 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_correct | True | True |
| R13L86_REVIEW_R1_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_028050_2024-06-11 | 028050 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_correct | True | True |
| None | 028050 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| R13_CROSS_R13L4_C05_028050_20240617_UNBILLED_RECEIVABLES_GUARD_028050_2024-06-17_Stage2-Actionable | 028050 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | True | True |
| R13L90_REVIEW_R11_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_028050_2024_02_28_TRIGGER | 028050 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive_if_EPC_order_label_counts_without_margin_execution_revision_bridge | True | True |
| V12_COMPACT_R13L2_C30_028050_20240228_STAGE2ACTIONABLE_028050_2024-02-28_cross_archetype_high_MAE_guardrail_review | 028050 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| T_R13_STAGE2FP_L5_028050_Stage2Actionable_2024-02-28 | 028050 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_stage2_false_positive_or_overpromotion_risk | True | True |
| R11L88_C05_028100_20240130_STAGE2_FALSE_POSITIVE_GEOTECH_CIVIL_WORKS | 028100 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | current_profile_false_positive_if_geotechnical_theme_overcredited_without_contract_economics | True | True |
| R10L88_C30_DONGAH_2024_STAGE2_FALSE_POSITIVE_CONTRACT_BETA | 028100 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive_if_contract_or_infra_beta_counts_without_cashflow_balance_bridge | True | True |
| R13L88_REVIEW_R11_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_028100_2024-01-30 | 028100 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R13L88_REVIEW_C30_DONGAH_2024_STAGE2_FALSE_POSITIVE_CONTRACT_BETA | 028100 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_contract_or_infra_beta_counts_without_cashflow_balance_bridge | True | True |
| R12L92_C32_SAMSUNGCNT_2024_STAGE2_ACTIONABLE_HOLDCO_GOVERNANCE_CAPITAL_RETURN_BRIDGE | 028260 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R12L86_C32_028260_20240129_STAGE2_GOVERNANCE_CAPITAL_RETURN | 028260 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_correct_if_governance_capital_return_bridge_required | True | True |
| R12L84_C32_028260_20240129_STAGE2_HOLDCO_NAV_RETURN_BRIDGE | 028260 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_correct_if_governance_bridge_required | True | True |
| C32_028260_20240207_STAGE3_YELLOW | 028260 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive_or_overpromotion_risk | True | True |
| R13L86_REVIEW_R12_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_028260_2024-01-29 | 028260 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_correct | True | True |
| C23_R7_L209_T05 | 028300 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_correct | False | True |
| None | 028300 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | None | True | True |
| None | 028300 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | False | True |
| R7L93_C24_028300_20240516_STAGE2_4C_REGULATORY_CRL | 028300 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_correct_if_CRL_or_regulatory_refusal_routes_to_hard_4C_not_4B_rebound | True | True |
| HLB_028300_2024_05_16_4C_FDA_BINARY_EVENT_RISK | 028300 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_4C_too_late | False | True |
| R7L98_C24_HLB_2024_STAGE4C_FDA_CRL_TRIAL_REGULATORY_EVENT_PROTECTION | 028300 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_kept_but_hard_4C_should_block_positive_stage | True | True |
| C24_R7L98_TRIG_06_028300 | 028300 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_4C_too_late | True | True |
| None | 028300 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | True | True |
| None | 028300 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| None | 028300 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| V12_COMPACT_R13L11-4B4C-006_028300_2024-04-25_cross_archetype_4b_4c_boundary_retest | 028300 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| None | 028300 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| None | 028300 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| None | 028300 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| R13_CROSS_R13L4_C24_028300_20240425_PRICE_ROW_AND_ENDPOINT_BREAK_028300_2024-04-25_Stage4C | 028300 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | True | True |
| None | 028300 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | True | True |
| V12_COMPACT_R13L2_C24_028300_20240425_STAGE3YELLOW_028300_2024-04-25_cross_archetype_high_MAE_guardrail_review | 028300 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| R6L96_C21_SAMSUNGCARD_2024_STAGE2_ACTIONABLE_CARD_DIVIDEND_VALUEUP_ROE_BRIDGE | 029780 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| TRG_R8L81-C26-030000-CHEIL-WORLDWIDE-AD-AGENCY-BOUNDED-RISKWATCH | 030000 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | C26 should not force stable large ad-agency rows into 4B when MAE is bounded and no client-budget or margin break is confirmed, but it also should not call durable Stage2 without verified ad spend recovery, client budget, operating leverage and margin bridge. | True | True |
| V12_COMPACT_030000_2024-02-01_platform_ad_budget_retention_opm_bridge_cleanup | 030000 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| None | 030000 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | None | False | True |
| T_C26_030000_STAGE2_20240401 | 030000 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | None | False | True |
| T_C26_R8L106_05_030000_STAGE2ACTIONABLE_Stage2Actionable_2024-04-25 | 030000 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_too_late_low_beta | True | True |
| C32_030200_20240207_STAGE2_ACTIONABLE | 030200 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive_or_overpromotion_risk | True | True |
| TRG_R6L77-C21-030210-DAOL-SECURITIES-BROKERAGE-VALUEUP-BETA-FADE | 030210 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | True | True |
| TRG_R6L77-C21-030210-DAOL-SECURITIES-BROKERAGE-VALUEUP-BETA-FADE | 030210 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | C21 should not treat brokerage/value-up beta as durable Stage2 unless ROE recovery, capital buffer, shareholder return, balance-sheet risk reduction and earnings bridge are visible. Daol Investment had only a small MFE, then drifted into a prolonged drawdown, making it a local 4B-watch boundary rather than a capital-return Green. | True | True |
| V12_COMPACT_030520_2024-07-08_platform_ad_budget_retention_opm_bridge_cleanup | 030520 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| None | 030520 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | None | False | True |
| R8L88_C28_HAANSOFT_2024_STAGE2_ACTIONABLE_AI_OFFICE_SOFTWARE | 030520 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R8L94_C28_HANCOM_2024_STAGE2_ACTIONABLE_AI_OFFICE_SOFTWARE_CONTRACT_RETENTION_BRIDGE | 030520 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R8L86_C28_030520_20240110_STAGE2_SOFTWARE_AI_CONTRACT_RETENTION | 030520 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_correct_if_contract_retention_bridge_required | True | True |
| R8L84_C28_030520_20240418_STAGE2_OFFICE_AI_SW_RETENTION_BRIDGE | 030520 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_correct_if_contract_retention_bridge_required | True | True |
| V12_COMPACT_C28_R8L104_030520_20240715_030520_2024-07-16_4B-Local-Watch | 030520 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive | True | True |
| R13L86_REVIEW_R8_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_030520_2024-01-10 | 030520 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_correct | True | True |
| R13_4B4C_L12_12_030520_20240119_4B_Local_Watch | 030520 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_source_proxy_row_promotes_to_green_or_full_4B | True | True |
| V12_COMPACT_R13L11-4B4C-012_030520_2024-02-07_cross_archetype_4b_4c_boundary_retest | 030520 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| None | 030520 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| V12_COMPACT_R13L12_ACCT_PRICE_09_C28_030520_20240119_030520_2024-01-19_Stage4B | 030520 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | True | True |
| R6L91_C21_030610_20240219_STAGE2_FALSE_POSITIVE_SMALL_BROKERAGE_VALUEUP | 030610 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive_if_small_brokerage_PBR_vocabulary_overcredited | True | True |
| R6L100_C21_KYOBOSECU_2024_STAGE4B_SMALLCAP_BROKERAGE_VALUEUP_EVENT_CAP | 030610 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_4B_too_late_if_smallcap_brokerage_valueup_event_premium_not_capped | True | True |
| None | 031430 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | True | True |
| R5_L122_C18_002 | 031430 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | True | True |
| None | 031430 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | False | True |
| 031430_2024-05-16_Stage2_C19_BRAND_PORTFOLIO_INVENTORY_DISCOUNT_FALSE_POSITIVE | 031430 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_false_positive | False | True |
| R5L90_C19_SI_2024_STAGE2_FALSE_POSITIVE_LUXURY_RETAIL_INVENTORY | 031430 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_false_positive_if_brand_retail_recovery_counts_without_inventory_margin_revision_bridge | True | True |
| R5L87_C19_031430_20240401_STAGE2_FALSE_POSITIVE_FASHION_BRAND | 031430 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_false_positive_if_brand_inventory_rebound_overcredited | True | True |
| C19_R5L119_02_031430_Stage3_Yellow_2024-03-27 | 031430 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | True | True |
| V12_COMPACT_C20_R5L120_031430_20240327_09_031430_2024-03-27_Stage3-Yellow | 031430 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | True | True |
| R13L87_REVIEW_R5_C19_BRAND_RETAIL_INVENTORY_MARGIN_031430_2024-04-01 | 031430 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R13L90_REVIEW_R5_C19_BRAND_RETAIL_INVENTORY_MARGIN_031430_2024_03_27_TRIGGER | 031430 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive_if_brand_retail_recovery_counts_without_inventory_margin_revision_bridge | True | True |
| T_C06_R2L103_031980_20240201_Stage2Actionable_CROSS_C07 | 031980 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_needs_C06_vs_C07_C08_C09_reroute_guard | True | True |
| R2L97_C06_PSKHOLDINGS_2024_STAGE2_ACTIONABLE_HBM_PACKAGING_CAPACITY_CUSTOMER_BRIDGE | 031980 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| V12_COMPACT_031980_2024-02-01_Stage2-Actionable | 031980 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_false_positive | True | True |
| R2L93_C07_031980_20240222_STAGE2_HBM_BACKEND_ORDER_REVISION | 031980 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_correct_if_order_delivery_revision_margin_cash_bridge_required_but_Green_strict | True | True |
| TRG-C09-L115-01-031980-Stage2Actionable-2024-02-15 | 031980 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_missed_structural_if_capped_as_generic_price_blowoff | True | True |
| PSKHOLDINGS_031980_2024_03_06_STAGE2A_ADVANCED_PACKAGING_EQUIPMENT | 031980 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_4B_too_late | False | True |
| T_C09_R2L111_03_031980_20240201 | 031980 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_false_positive | True | True |
| TRG_C10_R2_L110_031980_20240201_BACKEND_MEMORY_PACKAGING_RECOVERY | 031980 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_missed_structural_if_direct_order_bridge_required_too_late | True | True |
| TRG_R2L76-C10-031980-PSK-HOLDINGS-ADVANCED-PACKAGING-EQUIPMENT-CYCLE | 031980 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | C10 should allow equipment-cycle Stage2 when memory/advanced-package equipment demand connects to actual order, customer capacity, delivery and margin bridge. PSK Holdings produced high MFE with controlled entry-basis MAE; post-peak drawdown requires lifecycle local 4B if order/margin evidence fades. | True | True |
| TRG_R2L76-C10-031980-PSK-HOLDINGS-ADVANCED-PACKAGING-EQUIPMENT-CYCLE | 031980 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_correct | True | True |
| R2L93_C10_PSKHOLDINGS_2024_STAGE4B_ADVANCED_PACKAGING_EQUIPMENT_EVENT_CAP | 031980 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_4B_too_late_if_advanced_packaging_equipment_event_premium_not_capped | True | True |
| R13L93_REVIEW_R2_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_031980_2024_06_19_TRIGGER | 031980 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late_if_advanced_packaging_equipment_event_premium_not_capped | True | True |
| R13_L106_T01_031980 | 031980 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_4B_too_late | True | True |
| TRG_R12L82-C31-032350-LOTTE-TOURISM-RESORT-VISA-VOLUME-MARGIN | 032350 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should allow tourism policy positives only when visa/reopening policy maps to inbound volume, casino drop, hotel occupancy, ADR, revenue conversion and margin bridge. Lotte Tour Development had moderate MFE with bounded MAE, but share-count validation is needed before runtime promotion. | True | True |
| R4L96_C15_HWANGGEUMST_2024_STAGE2_FALSE_POSITIVE_STAINLESS_NICKEL_SPREAD_WATCH | 032560 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive_if_stainless_nickel_spread_watch_counts_without_shipment_inventory_margin_revision_bridge | True | True |
| R13L96_REVIEW_R4_C15_MATERIAL_SPREAD_SUPERCYCLE_032560_2024_01_31_TRIGGER | 032560 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_stainless_nickel_spread_watch_counts_without_shipment_inventory_margin_revision_bridge | True | True |
| TRG_R12L78-C31-032620-UBCARE-TELEMEDICINE-POLICY-DIRECT-DEMAND | 032620 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 can allow telemedicine/digital-health policy rows when policy relaxation maps to direct clinic/EMR platform usage, claim/workflow demand, paid usage, revenue conversion and margin bridge. UBCare produced a large MFE, but later drawdown means it cannot remain Green unless direct-demand and margin evidence refreshes. | True | True |
| V12_COMPACT_R13L11-4B4C-015_032620_2024-02-23_cross_archetype_4b_4c_boundary_retest | 032620 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R13_4B4C_L12_11_032620_20240223_4B_Local_Watch | 032620 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_source_proxy_row_promotes_to_green_or_full_4B | True | True |
| R13_CROSS_032620_2024-02-23_Stage4B | 032620 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | True | True |
| None | 032620 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | True | True |
| V12_COMPACT_R13L2_C31_032620_20240223_STAGE4B_032620_2024-02-23_cross_archetype_high_MAE_guardrail_review | 032620 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| TRG_R1L81-C04-032820-WOORITECH-NUCLEAR-CONTROL-SYSTEM-RS-SHARECOUNT | 032820 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | C04 should protect nuclear control-system positives when project/order evidence, customer quality, delivery schedule, revenue conversion and margin bridge are visible. Woori Technology produced very large MFE with nearly no early MAE, but share-count validation is required before runtime promotion. | True | True |
| TRG_R11L78-C04-032820-WOORI-TECH-NUCLEAR-IANDC-PROJECT-LIFECYCLE | 032820 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | C04 should protect nuclear control/I&C positives when project-policy demand maps to control-system order, customer/project visibility, delivery/revenue bridge and margin conversion. Woori Technology produced a strong MFE with almost no entry-basis MAE, but share-count movement requires validation. | True | True |
| TRG_R1L75-C04-032820-WOORI-TECH-NUCLEAR-CONTROL-SYSTEM-BRIDGE | 032820 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | C04 should include nuclear control/I&C suppliers when policy/project attention converts into project scope, order or customer validation. Woori Technology produced very high MFE and no entry-basis negative MAE, but share-count changes and later drawdown require validation and lifecycle local 4B. | True | True |
| TRG_R1L75-C04-032820-WOORI-TECH-NUCLEAR-CONTROL-SYSTEM-BRIDGE | 032820 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_correct | True | True |
| R11L87_C04_032820_20240718_STAGE2_FALSE_POSITIVE_NUCLEAR_CONTROL_BLOWOFF | 032820 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive_if_price_only_nuclear_theme_overcredited | True | True |
| C04_P1_TO50_TRG_16 | 032820 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive | True | True |
| C04_STATIC_TO50_TRG_07 | 032820 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive | True | True |
| None | 032820 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | None | True | True |
| R12L91_C31_WOORITECH_2024_STAGE2_FALSE_POSITIVE_NUCLEAR_POLICY_THEME | 032820 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive_if_nuclear_policy_theme_counts_without_procurement_contract_backlog_bridge | True | True |
| R13L87_REVIEW_R11_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_032820_2024-07-18 | 032820 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R13L91_REVIEW_R12_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_032820_2024_07_15_TRIGGER | 032820 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive_if_nuclear_policy_theme_counts_without_procurement_contract_backlog_bridge | True | True |
| T_C21_R6L104_032830_STAGE2ACTIONABLE_20240201 | 032830 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | True | True |
| None | 032830 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | True | True |
| None | 032830 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | True | True |
| R6L93_C22_SAMLIFE_2024_STAGE2_ACTIONABLE_LIFE_INSURANCE_CAPITAL_SURPLUS_RATE_CYCLE | 032830 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R6L90_C22_032830_20240124_STAGE2_LIFE_RATE_RESERVE_CAPITAL | 032830 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_correct_if_reserve_capital_buffer_payout_bridge_required | True | True |
| R6L97_C22_SAMSUNGLIFE_2024_STAGE2_ACTIONABLE_LIFE_CSM_RESERVE_VALUEUP_BRIDGE | 032830 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R6L84_C22_032830_20240129_STAGE2_LIFE_CSM_CAPITAL_RETURN_BRIDGE | 032830 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_correct_if_CSM_and_capital_return_bridge_required | True | True |
| TRG_R6L78-C22-032830-SAMSUNG-LIFE-RATE-RESERVE-CAPITAL-RETURN | 032830 | C22_INSURANCE_RATE_CYCLE_RESERVE | C22 should allow life-insurance positives when rate cycle, CSM/reserve quality, capital buffer, dividend/buyback and shareholder-return bridge are visible. Samsung Life produced large MFE with almost no entry-basis MAE, but later drawdown requires lifecycle local 4B if reserve/capital-return evidence fades. | True | True |
| TRG_R6L80-C22-032830-SAMSUNG-LIFE-RATE-CYCLE-CAPITAL-RETURN | 032830 | C22_INSURANCE_RATE_CYCLE_RESERVE | C22 should preserve life-insurance positives when rate cycle, CSM/reserve quality, capital buffer, dividend/buyback policy and earnings durability are visible. Samsung Life produced large MFE with almost no entry-basis MAE, but later drawdown requires lifecycle monitoring. | True | True |
| None | 032830 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | False | True |
| None | 032830 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | True | True |
| None | 032830 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | True | True |
| None | 032830 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | True | True |
| C22-R6-L101-05-T1 | 032830 | C22_INSURANCE_RATE_CYCLE_RESERVE | residual_missed_structural_life_insurer_rate_capital_return_bridge_after_initial_valueup_phase | True | True |
| R6L89_C22_SAMSUNGLIFE_2024_STAGE4B_LIFE_VALUEUP_PREMIUM_CAP | 032830 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_4B_too_late_if_life_insurance_valueup_premium_not_capped | True | True |
| None | 032830 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | True | True |
| None | 032830 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | False | True |
| None | 032830 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | None | True | True |
| V12_COMPACT_032830_2024-02-29_policy_valueup_insurance_csm_reserve_capital_return_cash_bridge | 032830 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | True | True |
| R13_CROSS_R13L4_C22_032830_20240229_CSM_RESERVE_TRUST_032830_2024-02-29_Stage3-Yellow | 032830 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | True | True |
| R12L97_C31_BITCOMPUTER_2024_STAGE2_FALSE_POSITIVE_TELEMEDICINE_POLICY_WATCH | 032850 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive_if_telemedicine_policy_watch_counts_without_implementation_reimbursement_adoption_revenue_revision_bridge | True | True |
| TRG_R12L78-C31-032850-BITCOMPUTER-TELEMEDICINE-IT-POLICY-THEME-FADE | 032850 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should not treat telemedicine or healthcare-IT policy beta as durable Stage2 unless policy event maps to direct installed-base demand, contract conversion, usage/revenue and margin evidence. BitComputer had an immediate MFE spike and then a long drawdown, making it local 4B rather than Green. | True | True |
| None | 033100 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | True | True |
| TRG_R1L76-C02-033100-JERYONG-TRANSFORMER-GRID-CAPEX-BACKLOG | 033100 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_correct | True | True |
| TRG_R1L76-C02-033100-JERYONG-TRANSFORMER-GRID-CAPEX-BACKLOG | 033100 | C02_POWER_GRID_DATACENTER_CAPEX | C02 should allow transformer suppliers when grid/datacenter capex converts into export order backlog, delivery slot, ASP and margin bridge. Jeryong Electric had extreme MFE and no entry-basis MAE, but later drawdown requires lifecycle local 4B if backlog/order evidence fades. | True | True |
| JERYONG_033100_2024_03_06_STAGE2A_TRANSFORMER_DATACENTER_EXPORT | 033100 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_4B_too_late | False | True |
| V12_COMPACT_R13L11-4B4C-013_033100_2024-05-02_cross_archetype_4b_4c_boundary_retest | 033100 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| V12_COMPACT_R13L12_ACCT_PRICE_04_C01_033100_20240502_033100_2024-05-02_4B-LocalWatch | 033100 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | True | True |
| TRG-C06-L111-033160-Stage2Actionable-2025-01-02 | 033160 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_ok_actionable | True | True |
| R2L90_C06_033170_20240222_STAGE2_FALSE_POSITIVE_OSAT_PACKAGING_THEME | 033170 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_false_positive_if_OSAT_packaging_theme_overcredited | True | True |
| SIGNETICS_033170_2024_03_06_STAGE2_FALSE_POSITIVE_OSAT_PACKAGE_EVENT | 033170 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_false_positive | False | True |
| R9L91_C29_033250_20240102_STAGE2_FALSE_POSITIVE_CHASSIS_PARTS | 033250 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive_if_chassis_parts_vocabulary_overcredited | True | True |
| TRG_R9L74-C29-033530-SJG-SEJONG-HYDROGEN-EXHAUST-PARTS-BETA-FADE | 033530 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should not treat hydrogen/exhaust/auto-parts theme beta as durable Stage2 unless customer volume, OEM program, pricing or margin bridge is visible. SJG Sejong had a tradable spike but later MAE and post-peak drawdown opened. | True | True |
| TRG_R9L74-C29-033530-SJG-SEJONG-HYDROGEN-EXHAUST-PARTS-BETA-FADE | 033530 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should not treat hydrogen/exhaust/auto-parts theme beta as durable Stage2 unless customer volume, OEM program, pricing or margin bridge is visible. SJG Sejong had a tradable spike but later MAE and post-peak drawdown opened. | True | True |
| R9L92_C29_033530_20240102_STAGE2_FALSE_POSITIVE_EXHAUST_LEGACY_AUTOPARTS | 033530 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive_if_exhaust_legacy_autoparts_vocabulary_overcredited | True | True |
| R9L91_C29_SJGSEJONG_2024_STAGE4B_EXHAUST_MOBILITY_PARTS_EVENT_CAP | 033530 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_4B_too_late_if_exhaust_mobility_parts_event_premium_not_capped | True | True |
| R13L91_REVIEW_R9_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_033530_2024_02_14_TRIGGER | 033530 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_4B_too_late_if_exhaust_mobility_parts_event_premium_not_capped | True | True |
| None | 033640 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | False | True |
| None | 033640 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | None | True | True |
| C32_033780_20240207_STAGE2_ACTIONABLE | 033780 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive_or_overpromotion_risk | True | True |
| R1L117-C01-002 | 034020 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_correct_but_scope_ambiguous_between_C01_and_C04 | False | True |
| R1L117-C01-002 | 034020 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_correct_but_scope_ambiguous_between_C01_and_C04 | True | True |
| C04_P1_TO50_TRG_01 | 034020 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive | True | True |
| C04_STATIC_TO50_TRG_01 | 034020 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive | True | True |
| None | 034020 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | None | True | True |
| C04_P1_TO50_TRG_02 | 034020 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive | True | True |
| None | 034020 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | True | True |
| C31_L101_T003_034020 | 034020 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_missed_policy_to_project_bridge | True | True |
| R11L94_C31_DOOSANENERBILITY_2024_STAGE2_ACTIONABLE_NUCLEAR_POWER_POLICY_ORDER_BRIDGE | 034020 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R12L83_C31_034020_20240311_STAGE2_NUCLEAR_POLICY_PROJECT_BRIDGE | 034020 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_data_insufficient | True | True |
| None | 034020 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| None | 034020 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| R13_4B4C_L101_T001_034020 | 034020 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_correct_or_too_conservative | True | True |
| None | 034020 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| None | 034020 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | True | True |
| V12_COMPACT_034120_2024-06-18_platform_ad_budget_retention_opm_bridge_cleanup | 034120 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| R12L93_C32_SBS_2024_STAGE4B_BROADCAST_CONTROL_PREMIUM_EVENT_CAP | 034120 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_4B_too_late_if_broadcast_control_premium_sale_event_premium_not_capped | True | True |
| R13L93_REVIEW_R12_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_034120_2024_01_04_TRIGGER | 034120 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late_if_broadcast_control_premium_sale_event_premium_not_capped | True | True |
| R12L95_C31_PARADISE_2024_STAGE2_ACTIONABLE_CASINO_TOURISM_POLICY_CHANNEL_BRIDGE | 034230 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R12L91_C31_034230_20240401_STAGE2_FALSE_POSITIVE_CASINO_TOURISM_POLICY | 034230 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive_if_tourism_casino_policy_vocabulary_overcredited | True | True |
| None | 034230 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | None | True | True |
| TRG_R10L76-C30-034300-SHINSEGAE-CONSTRUCTION-POST-CA-SUPPORT-NO-HARD4C | 034300 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should not convert every PF fear or construction liquidity story into hard 4C when post-CA price action recovers and stabilizes. Shinsegae Construction requires post-corporate-action validation, but the post-CA window is a no-hard-4C boundary unless non-price solvency/refinancing break is confirmed. | True | True |
| TRG_R10L76-C30-034300-SHINSEGAE-CONSTRUCTION-POST-CA-SUPPORT-NO-HARD4C | 034300 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive | True | True |
| TRG_R10L73-C30-034300-SHINSEGAE-CONSTRUCTION-PF-RECAP-BUFFER | 034300 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should not convert every PF-liquidity headline into hard 4C when parent recapitalization, tender/de-listing path, or capital buffer changes the equity path. The stock-web path had large MFE after the recapitalization candidate, so this is a no-hard-4C buffer row, not a hard break row. | True | True |
| R10L87-C30-034300-T1 | 034300 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_would_allow_watch_stage2; positive_path_observed_but_no_new_delta_due_source_proxy | True | True |
| R10L92_C30_034300_20240118_STAGE2_FALSE_POSITIVE_LATE_PRICE_NONVALIDATION | 034300 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive_if_late_corporate_action_price_behavior_validates_original_weak_entry | True | True |
| TRG_R10L73-C30-034300-SHINSEGAE-CONSTRUCTION-PF-RECAP-BUFFER | 034300 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should not convert every PF-liquidity headline into hard 4C when parent recapitalization, tender/de-listing path, or capital buffer changes the equity path. The stock-web path had large MFE after the recapitalization candidate, so this is a no-hard-4C buffer row, not a hard break row. | True | True |
| R10L87_C30_SSG_2024_STAGE4B_PARENT_SUPPORT_EVENT_CAP | 034300 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_4B_too_late_if_parent_support_event_cap_not_detected | True | True |
| R10L87-C30-034300-T2 | 034300 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | existing full_4b_requires_non_price_evidence kept | True | True |
| R10L95_C30_SHINSEGAEEC_2024_STAGE4B_RETAIL_BUILDER_POST_CA_RESCUE_EVENT_CAP | 034300 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_4B_too_late_if_retail_builder_PF_rescue_event_premium_not_capped | True | True |
| R11L93_C31_SHINSEGAECONST_2024_STAGE4B_RESTRUCTURING_POLICY_EVENT_CAP | 034300 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_4B_too_late_if_restructuring_policy_support_event_premium_not_capped | True | True |
| R13L93_REVIEW_R11_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_034300_2024_05_29_TRIGGER | 034300 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late_if_restructuring_policy_support_event_premium_not_capped | True | True |
| R13L95_REVIEW_R10_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_034300_2024_05_29_TRIGGER | 034300 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late_if_retail_builder_PF_rescue_event_premium_not_capped | True | True |
| R12L85_C31_034730_20240219_STAGE2_FALSE_POSITIVE_HOLDCO_VALUEUP_THEME | 034730 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive_if_valueup_theme_overcredited | True | True |
| R12L94_C32_SK_2024_STAGE2_FALSE_POSITIVE_HOLDCO_VALUEUP_WATCH | 034730 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive_if_holdco_valueup_watch_counts_without_NAV_capital_return_execution_revision_bridge | True | True |
| C32_034730_SK_20240207_S2A | 034730 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive | True | True |
| C32_034730_20240814_STAGE2_ACTIONABLE | 034730 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive_or_overpromotion_risk | True | True |
| TRG_R11L82-C32-034730-SK-HOLDCO-VALUEUP-SHARECOUNT-WHIPSAW | 034730 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should not treat holding-company value-up or control-discount beta as durable Stage2 unless event mechanics, asset/NAV bridge, capital allocation, shareholder process, timing and downside cap are visible. SK had early MFE but then a deep MAE path and stock-web share-count movement, so validation is mandatory. | True | True |
| R11L83_C32_034730_20240531_STAGE2_EVENT_PREMIUM_ROUNDTRIP | 034730 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive | True | True |
| R13L85_REVIEW_R12_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_034730_2024-02-19 | 034730 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| R13L94_REVIEW_R12_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_034730_2024_02_01_TRIGGER | 034730 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive_if_holdco_valueup_watch_counts_without_NAV_capital_return_execution_revision_bridge | True | True |
| TR_C26_L105_035000_Stage2Actionable_20240930 | 035000 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_correct | True | True |
| R12L89_C31_035250_20240206_STAGE2_FALSE_POSITIVE_CASINO_POLICY | 035250 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive_if_casino_policy_theme_overcredited | True | True |
| R8L99_C26_NAVER_2024_STAGE2_FALSE_POSITIVE_SEARCH_PORTAL_AD_RECOVERY_WATCH | 035420 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive_if_search_portal_ad_recovery_watch_counts_without_ad_revenue_operating_leverage_revision_bridge | True | True |
| V12_COMPACT_035420_2024-02-02_platform_ad_budget_retention_opm_bridge_cleanup | 035420 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_correct | True | True |
| None | 035420 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | None | False | True |
| C27-R8L105-002|Stage2-Actionable|2024-02-07 | 035420 | C27_CONTENT_IP_GLOBAL_MONETIZATION | residual_error_needs_C27_specific_bridge_or_guard | True | True |
| None | 035420 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | None | False | True |
| C32_035420_20240712_STAGE2_ACTIONABLE | 035420 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive_or_overpromotion_risk | True | True |
| None | 035420 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| None | 035420 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| None | 035420 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| R13_CROSS_R13L4_C26_035420_20240401_SEGMENT_MARGIN_TRUST_035420_2024-04-01_Stage3-Yellow | 035420 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | True | True |
| T_C26_R8L106_04_035720_STAGE2_Stage2_2024-02-02 | 035720 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| T_C26_035720_STAGE2_20240111 | 035720 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | None | False | True |
| V12_COMPACT_035720_2024-01-26_platform_ad_budget_retention_opm_bridge_cleanup | 035720 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| None | 035720 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | None | False | True |
| C27-R8L105-001|Stage2-Actionable|2024-02-06 | 035720 | C27_CONTENT_IP_GLOBAL_MONETIZATION | residual_error_needs_C27_specific_bridge_or_guard | True | True |
| C31_L101_T008_035720 | 035720 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | True | True |
| None | 035720 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | None | False | True |
| T_C32_R12L106_035720_20240202_Stage2-Actionable | 035720 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | governance repair narrative lacked cash bridge and produced deep MAE; Stage2 watch only | True | True |
| None | 035760 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | None | False | True |
| V12_COMPACT_035760_2024-06-12_platform_ad_budget_retention_opm_bridge_cleanup | 035760 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| T_C26_035760_STAGE2A_20240123 | 035760 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | None | False | True |
| T_C26_035760_STAGE4B_20240527 | 035760 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | None | False | True |
| R8L90_C27_035760_20240122_STAGE2_MEDIA_COMMERCE_IP | 035760 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_correct_if_distribution_IP_margin_cash_bridge_required | True | True |
| R8L93_C27_CJENM_2024_STAGE2_FALSE_POSITIVE_CONTENT_PLATFORM_VALUEUP_WATCH | 035760 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_false_positive_if_content_platform_valueup_counts_without_IP_export_royalty_margin_revision_bridge | True | True |
| R13L93_REVIEW_R8_C27_CONTENT_IP_GLOBAL_MONETIZATION_035760_2024_02_08_TRIGGER | 035760 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_content_platform_valueup_counts_without_IP_export_royalty_margin_revision_bridge | True | True |
| T_C05_R1L109_035890_20240321_REGIONAL_PRE_SALE_CASH_BRIDGE | 035890 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | True | True |
| TRG_R10L76-C30-035890-SEOHEE-CONSTRUCTION-ORDERBOOK-BUFFER-NO-HARD4C | 035890 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should keep PF/orderbook RiskWatch active for builders, but bounded MAE and recovery rows should not be escalated into hard 4C. Seohee Construction showed a low-MAE recovery path; without non-price PF/refinancing or solvency break it should remain RiskWatch/no-hard-4C. | True | True |
| TRG_R10L76-C30-035890-SEOHEE-CONSTRUCTION-ORDERBOOK-BUFFER-NO-HARD4C | 035890 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive | True | True |
| None | 035890 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | True | True |
| R10L88_C30_SEOHEE_2024_STAGE2_ACTIONABLE_PF_REPAIR | 035890 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R10L84_C30_035890_20240924_STAGE2_REGIONAL_HOUSING_REPAIR | 035890 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_correct_if_balance_sheet_repair_bridge_required | True | True |
| None | 035900 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | None | False | True |
| None | 035900 | C27_CONTENT_IP_GLOBAL_MONETIZATION | None | True | True |
| R8L87_C27_035900_20240102_STAGE2_FALSE_POSITIVE_ARTIST_IP_THEME | 035900 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_false_positive_if_artist_IP_theme_overcredited | True | True |
| C27-R8L105-003|Stage3-Yellow|2024-02-16 | 035900 | C27_CONTENT_IP_GLOBAL_MONETIZATION | residual_error_needs_C27_specific_bridge_or_guard | True | True |
| R13L87_REVIEW_R8_C27_CONTENT_IP_GLOBAL_MONETIZATION_035900_2024-01-02 | 035900 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R11L91_C04_036190_20240102_STAGE2_FALSE_POSITIVE_LEGACY_PLANT_MAINTENANCE | 036190 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive_if_maintenance_vocabulary_overcredited_as_nuclear_project | True | True |
| R2L90_C07_UNISEM_2024_STAGE2_FALSE_POSITIVE_SCRUBBER_EQUIPMENT_THEME | 036200 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_false_positive_if_equipment_theme_counts_without_HBM_customer_order_revision_bridge | True | True |
| UNISEM_036200_2024_03_06_STAGE2A_ADVANCED_PROCESS_SUPPORT_EQUIPMENT | 036200 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_4B_too_late | False | True |
| R2L98_C10_UNISEM_2024_STAGE2_FALSE_POSITIVE_SCRUBBER_CHILLER_MEMORY_RECOVERY_WATCH | 036200 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_false_positive_if_scrubber_chiller_memory_recovery_watch_counts_without_customer_order_utilization_margin_revision_bridge | True | True |
| R2L93_C10_036200_20240529_STAGE2_FALSE_POSITIVE_CHILLER_SCRUBBER_SPIKE | 036200 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_false_positive_if_chiller_scrubber_spike_overcredited | True | True |
| TRG_C10_R2_L110_036200_20240502_CHILLER_SCRUBBER_LATE_CYCLE_FALSE_YELLOW | 036200 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_false_positive_late_yellow_without_order_bridge | True | True |
| R13L90_REVIEW_R2_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_036200_2024_06_28_TRIGGER | 036200 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive_if_equipment_theme_counts_without_HBM_customer_order_revision_bridge | True | True |
| C27-R8L105-012|Stage2|2024-02-26 | 036420 | C27_CONTENT_IP_GLOBAL_MONETIZATION | residual_error_needs_C27_specific_bridge_or_guard | True | True |
| R11L88_C31_KOGAS_2024_STAGE2_ACTIONABLE_TARIFF_RECEIVABLE_REPAIR | 036460 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R12L87_C31_036460_20240604_STAGE2_GAS_POLICY_ASSET | 036460 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_correct_if_direct_policy_asset_bridge_required | True | True |
| C32_036460_20240603_STAGE2_ACTIONABLE | 036460 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive_or_overpromotion_risk | True | True |
| R13L87_REVIEW_R12_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_036460_2024-06-04 | 036460 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_correct | True | True |
| R2L90_C06_036540_20240118_STAGE2_MEMORY_BACKEND_CAPACITY | 036540 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_correct_if_customer_capacity_ramp_margin_bridge_required | True | True |
| R2L97_C06_SFASEMI_2024_STAGE2_FALSE_POSITIVE_MEMORY_OSAT_CAPACITY_WATCH | 036540 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_false_positive_if_memory_OSAT_capacity_watch_counts_without_customer_capacity_order_utilization_margin_revision_bridge | True | True |
| TRG-C06-L111-036540-Stage2Actionable-2024-04-01 | 036540 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_false_positive | True | True |
| SFASEMICON_036540_2024_03_06_STAGE2_FALSE_POSITIVE_OSAT_PACKAGE_TEST | 036540 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_false_positive | False | True |
| None | 036540 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | False | True |
| None | 036540 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | None | True | True |
| R2L93_C10_SFASEMI_2024_STAGE2_FALSE_POSITIVE_OSAT_MEMORY_RECOVERY_THEME | 036540 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_false_positive_if_OSAT_memory_recovery_theme_counts_without_order_utilization_margin_revision_bridge | True | True |
| R13L93_REVIEW_R2_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_036540_2024_01_24_TRIGGER | 036540 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_OSAT_memory_recovery_theme_counts_without_order_utilization_margin_revision_bridge | True | True |
| C32_036560_YP_PRECISION_20240913_TENDER_BATTLE_4B | 036560 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | None | True | True |
| TRG_R12L75-C32-036560-YP-PRECISION-TENDER-CONTROL-PREMIUM-LIFECYCLE | 036560 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_correct | True | True |
| TRG_R12L72-C32-036560-YOUNGPOONG-PRECISION-TENDER-BATTLE-CAP | 036560 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 can allow Stage2 when a tender/control battle has explicit tender price and strategic control context, but extreme post-peak drawdown after the tender window requires local 4B-watch. Runtime must separate tender-cap math from open-ended governance rerating. | True | True |
| TRG_R12L72-C32-036560-YOUNGPOONG-PRECISION-TENDER-BATTLE-CAP | 036560 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 can allow Stage2 when a tender/control battle has explicit tender price and strategic control context, but extreme post-peak drawdown after the tender window requires local 4B-watch. Runtime must separate tender-cap math from open-ended governance rerating. | True | True |
| TRG_R11L80-C32-036560-YOUNGPOONG-PRECISION-TENDER-BATTLE-CAP | 036560 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should allow tender-battle positives only when tender price, acceptance window, ownership structure, free-float and event-end mechanics are explicit. Young Poong Precision/KZ Precision produced enormous event MFE, then the post-event path required local 4B discipline. | True | True |
| TRG_R12L75-C32-036560-YP-PRECISION-TENDER-CONTROL-PREMIUM-LIFECYCLE | 036560 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should allow a tender/control-premium lifecycle candidate when the listed company is a direct economic beneficiary of tender terms, control dispute or stake economics. Young Poong Precision/KZ Precision produced very large MFE, but post-tender drawdown means lifecycle local 4B is mandatory once tender/control-premium evidence fades. | True | True |
| R5_L121_C18_001 | 036620 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | True | True |
| None | 036620 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | True | True |
| None | 036620 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | False | True |
| TRG_C19_036620_20240214_OUTDOOR_BRAND_MARGIN_RESTOCK_SUCCESS | 036620 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_correct_but_4B_watch_needed | True | True |
| GAMSUNG_036620_2024_02_21_STAGE2A_BRAND_SELLTHROUGH_MARGIN | 036620 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_4B_too_late | False | True |
| R5L98_C19_GAMSUNG_2024_STAGE2_ACTIONABLE_APPAREL_BRAND_SELLTHROUGH_REORDER_MARGIN_BRIDGE | 036620 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R5L90_C19_GAMSUNG_2024_STAGE2_ACTIONABLE_OUTDOOR_BRAND_REORDER_MARGIN | 036620 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| C19_R5L119_17_036620_Stage2_Actionable_2024-02-22 | 036620 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | True | True |
| V12_COMPACT_C20_R5L120_036620_20240222_07_036620_2024-02-22_Stage2-Actionable | 036620 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | True | True |
| T_C06_R2L103_036810_20240318_Stage2_CROSS_C07 | 036810 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_needs_C06_vs_C07_C08_C09_reroute_guard | True | True |
| V12_COMPACT_036810_2024-03-18_Stage2 | 036810 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_false_positive | True | True |
| TRG_R2L74-C07-036810-FST-EUV-CHILLER-ANCILLARY-EQUIPMENT-RS | 036810 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | C07 can include ancillary equipment when relative strength is tied to customer adoption, capex timing and margin conversion. FST had strong early MFE, but the later collapse shows that price strength must decay into local 4B if order/customer bridge evidence fails to refresh. | True | True |
| TRG_R2L74-C07-036810-FST-EUV-CHILLER-ANCILLARY-EQUIPMENT-RS | 036810 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | C07 can include ancillary equipment when relative strength is tied to customer adoption, capex timing and margin conversion. FST had strong early MFE, but the later collapse shows that price strength must decay into local 4B if order/customer bridge evidence fails to refresh. | True | True |
| None | 036810 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | False | True |
| R2L93B_C09_036810_20240409_STAGE2_FALSE_POSITIVE_EUV_PRICE_MFE | 036810 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_false_positive_if_EUV_price_MFE_overcredited | True | True |
| T_C09_R2L111_08_036810_20240318 | 036810 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_false_positive | True | True |
| TRG-C09-L115-05-036810-Stage4B-2024-06-17 | 036810 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_4B_too_late_if_yellow_allowed | True | True |
| None | 036810 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | None | True | True |
| T_R13_STAGE2FP_L6_036810_Stage2_2024-03-18 | 036810 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_stage2_false_positive_or_overpromotion_risk | True | True |
| None | 036830 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | False | True |
| R3L94_C12_SOULBRAINHOLDINGS_2024_STAGE2_ACTIONABLE_ELECTROLYTE_CUSTOMER_CALLOFF_CAPACITY_MARGIN | 036830 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R3L91_C13_036830_20240129_STAGE2_ELECTROLYTE_JV_UTILIZATION_AMPC | 036830 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_correct_if_JV_utilization_AMPC_margin_cash_bridge_required | True | True |
| R3L98_C13_SOLBRAINHOLDINGS_2024_STAGE2_ACTIONABLE_ELECTROLYTE_HOLDCO_JV_UTILIZATION_AMPC_BRIDGE | 036830 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| T_C06_R2L103_036930_20240201_Stage2_CROSS_C07 | 036930 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_needs_C06_vs_C07_C08_C09_reroute_guard | True | True |
| V12_COMPACT_036930_2024-02-01_Stage2 | 036930 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_false_positive | True | True |
| R2L86_C07_036930_20240226_STAGE2_HBM_ALD_ORDER_BRIDGE | 036930 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_correct_if_order_bridge_required | True | True |
| R2_L110_C07 | 036930 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | None | True | True |
| None | 036930 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | False | True |
| R2L93_C09_036930_20240228_STAGE2_4B_ALD_VALUATION_BLOWOFF | 036930 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_correct_if_valuation_blowoff_without_order_delivery_margin_routes_to_4B | True | True |
| TRG_R2L82-C09-036930-JUSUNG-ALD-EQUIPMENT-VALUATION-BLOWOFF-SHARECOUNT | 036930 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | C09 should not treat ALD/deposition equipment theme beta as durable Stage2 unless named customer order, delivery schedule, backlog conversion, revenue and margin bridge are visible. Jusung produced a fast spike and then deep MAE; the 2024 shard also shows share-count change, so validation is required. | True | True |
| TRG_R2L79-C09-036930-JUSUNG-ADVANCED-EQUIPMENT-THEME-BLOWOFF-FADE | 036930 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | C09 should not treat advanced deposition/equipment theme beta as durable Stage2 unless customer order, backlog conversion, delivery, customer capacity and margin bridge refreshes. Jusung Engineering had a tradable MFE, then opened a high-MAE drawdown path. | True | True |
| TRG_R2L76-C10-036930-JUSUNG-EQUIPMENT-CYCLE-BETA-FADE | 036930 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_false_positive | True | True |
| R13_CROSS_036930_2024-02-28_Stage2-FalsePositive_/_Stage4B-Local-PriceOnly | 036930 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_false_positive | True | True |
| R2L89_C10_JUSUNG_2024_STAGE2_ACTIONABLE_MEMORY_EQUIPMENT_REORDER | 036930 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| TRG_R2L76-C10-036930-JUSUNG-EQUIPMENT-CYCLE-BETA-FADE | 036930 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | C10 should not treat generic equipment-cycle or memory recovery beta as durable Stage2 unless customer order, delivery, capex conversion and margin evidence refreshes. Jusung Engineering produced only limited MFE and then high MAE; share-count movement inside the window requires validation. | True | True |
| None | 036930 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | None | True | True |
| R13L86_REVIEW_R2_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_036930_2024-02-26 | 036930 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_correct | True | True |
| R1L98_C02_POWERNET_2024_STAGE2_FALSE_POSITIVE_POWER_SUPPLY_DATACENTER_CAPEX_WATCH | 037030 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_false_positive_if_power_supply_capex_watch_counts_without_customer_order_delivery_capacity_margin_revision_bridge | True | True |
| R1L92_C02_037030_20240102_STAGE2_FALSE_POSITIVE_POWER_SUPPLY | 037030 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_false_positive_if_power_supply_vocabulary_overcredited | True | True |
| R1L91_C05_037350_20241010_STAGE2_FALSE_POSITIVE_CLEANROOM_ENGINEERING_SPIKE | 037350 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | current_profile_false_positive_if_cleanroom_engineering_spike_overcredited | True | True |
| R4L89_C16_EG_2024_STAGE4B_RARE_EARTH_POLICY_THEME_CAP | 037370 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_4B_too_late_if_rare_earth_policy_theme_premium_not_capped | True | True |
| R9L91_C29_ECOPLASTIC_2024_STAGE2_FALSE_POSITIVE_LIGHTWEIGHT_EV_PARTS | 038110 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive_if_lightweight_EV_parts_theme_counts_without_volume_margin_revision_bridge | True | True |
| R13L91_REVIEW_R9_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_038110_2024_02_02_TRIGGER | 038110 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive_if_lightweight_EV_parts_theme_counts_without_volume_margin_revision_bridge | True | True |
| T_C06_R2L103_039030_20240223_Stage2Actionable_CROSS_C07 | 039030 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_needs_C06_vs_C07_C08_C09_reroute_guard | True | True |
| R2L85_C06_039030_20240228_STAGE2_HBM_CUSTOMER_CAPACITY_BRIDGE | 039030 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_correct_if_customer_capacity_bridge_required | True | True |
| V12_COMPACT_039030_2024-02-23_Stage2-Actionable | 039030 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_false_positive | True | True |
| None | 039030 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | False | True |
| R2L88_C09_EOTECH_2024_STAGE2_ACTIONABLE_ADVANCED_EQUIPMENT_RERATING | 039030 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| T_C09_R2L111_05_039030_20240223 | 039030 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_false_positive | True | True |
| R2L88_C09_039030_20240228_STAGE2_ADVANCED_LASER_ORDER_MARGIN | 039030 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_correct_if_customer_order_margin_bridge_required | True | True |
| R13L88_REVIEW_R2_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_039030_2024-02-28 | 039030 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_correct | True | True |
| R13L85_REVIEW_R2_C06_HBM_MEMORY_CUSTOMER_CAPACITY_039030_2024-02-28 | 039030 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_correct | True | True |
| TRG_R12L82-C31-039130-HANATOUR-TRAVEL-VISA-THEME-FADE | 039130 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should not treat tourism/visa reopening beta as durable Stage2 unless package bookings, air-seat supply, ASP, commission take-rate, revenue and margin bridge are visible. Hanatour had modest early MFE and then high-MAE fade. | True | True |
| R12L89_C31_039130_20240131_STAGE2_FALSE_POSITIVE_TRAVEL_POLICY | 039130 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive_if_travel_policy_rebound_overcredited | True | True |
| C24_R7L98_TRIG_02_039200 | 039200 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_too_late | True | True |
| None | 039200 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | True | True |
| T_C24_R7L105_039200_20240226_STAGE2 | 039200 | C24_BIO_TRIAL_DATA_EVENT_RISK | Stage2_can_exist_but_Stage3_must_be_blocked_until_endpoint_and_commercial_path_are_validated | True | True |
| R7L93_C24_OSCOTEC_2024_STAGE2_ACTIONABLE_KINASE_PIPELINE_TRIAL_DATA_DURABILITY | 039200 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| None | 039200 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | True | True |
| T_R13_STAGE2FP_L5_039200_Stage2_2024-02-26 | 039200 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_stage2_false_positive_or_overpromotion_risk | True | True |
| R2L90_C07_STI_2024_STAGE4B_HBM_REFLOW_THEME_CAP | 039440 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_4B_too_late_if_HBM_reflow_equipment_theme_premium_not_capped | True | True |
| None | 039440 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | False | True |
| R2L93C_C09_039440_20240213_STAGE2_FALSE_POSITIVE_CCSS_SPIKE | 039440 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_false_positive_if_CCSS_equipment_price_spike_overcredited | True | True |
| TRG-C09-L115-04-039440-Stage3Yellow-2024-03-15 | 039440 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_false_positive_if_theme_label_promoted_to_yellow | True | True |
| STI_039440_2024_03_06_STAGE2_FALSE_POSITIVE_MEMORY_INFRA_RECOVERY | 039440 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_false_positive | False | True |
| STI_039440_2024_03_06_STAGE2_FALSE_POSITIVE_MEMORY_INFRA_RECOVERY_BETA | 039440 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_false_positive | False | True |
| R13L90_REVIEW_R2_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_039440_2024_03_13_TRIGGER | 039440 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_4B_too_late_if_HBM_reflow_equipment_theme_premium_not_capped | True | True |
| TRG_R6L81-C21-039490-KIWOOM-BROKERAGE-TRADING-VOLUME-CAPITAL-RETURN | 039490 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | C21 should allow brokerage platform positives when market turnover, customer asset quality, retail brokerage, credit balance, capital return and earnings bridge are visible. Kiwoom produced a very large MFE with controlled entry-basis MAE, but stock-web share count changes need validation. | True | True |
| None | 039490 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | False | True |
| None | 039490 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | False | True |
| R6L87_C21_039490_20240711_STAGE2_FALSE_POSITIVE_LATE_BROKERAGE_EXTENSION | 039490 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive_if_late_brokerage_extension_overcredited | True | True |
| R6L83_C21_039490_20240314_STAGE2_RETAIL_BROKERAGE_LATE_ENTRY | 039490 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_early | True | True |
| None | 039490 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | True | True |
| None | 039490 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | True | True |
| None | 039490 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | True | True |
| TRIG_C31_R11L100_008_039490 | 039490 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | True | True |
| None | 039490 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | None | True | True |
| V12_COMPACT_039490_2024-05-08_policy_valueup_bank_brokerage_ROE_PBR_capital_return_execution_bridge | 039490 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_correct | True | True |
| R13L87_REVIEW_R6_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_039490_2024-07-11 | 039490 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| None | 039490 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| TRG_R11L76-C31-039610-HWASEONG-VALVE-EASTSEA-GAS-POLICY-LIFECYCLE | 039610 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_correct | True | True |
| TRG_R11L74-C31-039610-HWASUNG-VALVE-GAS-POLICY-CONTRACT-BRIDGE | 039610 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 can allow a policy-event lifecycle candidate when a valve or pipeline-infra name later connects to named procurement, order, EPC, utility or offshore infrastructure bridge. Hwasung Valve had a large MFE and later secondary peak, but still needs source repair and lifecycle local 4B after the peak. | True | True |
| TRG_R11L74-C31-039610-HWASUNG-VALVE-GAS-POLICY-CONTRACT-BRIDGE | 039610 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 can allow a policy-event lifecycle candidate when a valve or pipeline-infra name later connects to named procurement, order, EPC, utility or offshore infrastructure bridge. Hwasung Valve had a large MFE and later secondary peak, but still needs source repair and lifecycle local 4B after the peak. | True | True |
| TRG_R11L76-C31-039610-HWASEONG-VALVE-EASTSEA-GAS-POLICY-LIFECYCLE | 039610 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 can allow a policy-event lifecycle candidate when a gas-field/resource-development policy shock maps to a direct valve/pipeline beneficiary and then to actual order, project schedule, revenue and margin bridge. Hwaseong Valve produced large MFE, but post-peak drawdown requires lifecycle local 4B if the policy-to-order bridge fades. | True | True |
| None | 039840 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | True | True |
| None | 039840 | C24_BIO_TRIAL_DATA_EVENT_RISK | C24 must require fresh binary/data endpoint quality; reroute commercialization, device, reimbursement, or price-only events to C23/C25/local_4B as appropriate. | True | True |
| None | 039840 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | None | True | True |
| V12_COMPACT_C25_R7L107_039840_20240527_Stage2_Actionable_039840_2024-05-27_Stage2-Actionable | 039840 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive | True | True |
| None | 039840 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | None | True | True |
| TRG_R12L74-C32-040300-YTN-PRIVATIZATION-CONTROL-SALE-FADE | 040300 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should not treat privatization or control-sale approval as durable Stage2 unless minority tender economics, closing certainty, capital policy or earnings bridge is explicit. YTN had a short control-sale pop but then suffered high MAE and post-peak drawdown. | True | True |
| R12L96_C32_YTN_2024_STAGE2_FALSE_POSITIVE_MEDIA_PRIVATIZATION_CONTROL_WATCH | 040300 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive_if_media_privatization_control_watch_counts_without_binding_transaction_regulatory_closing_tender_price_floor_bridge | True | True |
| C32_040300_YTN_20231024_CONTROL_TRANSFER_S2 | 040300 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | None | True | True |
| TRG_R12L74-C32-040300-YTN-PRIVATIZATION-CONTROL-SALE-FADE | 040300 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should not treat privatization or control-sale approval as durable Stage2 unless minority tender economics, closing certainty, capital policy or earnings bridge is explicit. YTN had a short control-sale pop but then suffered high MAE and post-peak drawdown. | True | True |
| R12L88_C32_YTN_2023_STAGE4B_BROADCAST_CONTROL_SALE_CAP | 040300 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_4B_too_late_if_control_sale_premium_cap_not_detected | True | True |
| R13L96_REVIEW_R12_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_040300_2024_02_05_TRIGGER | 040300 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_media_privatization_control_watch_counts_without_binding_transaction_regulatory_closing_tender_price_floor_bridge | True | True |
| R13L88_REVIEW_C32_YTN_2023_STAGE4B_BROADCAST_CONTROL_SALE_CAP | 040300 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late_if_control_sale_premium_cap_not_detected | True | True |
| R8L98_C28_POLARISOFFICE_2024_STAGE2_ACTIONABLE_AI_OFFICE_SW_RETENTION_BRIDGE | 041020 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R8L84_C28_041020_20240509_STAGE2_FALSE_POSITIVE_AI_OFFICE_THEME | 041020 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive_if_AI_office_theme_overcredited | True | True |
| R6L94_C21_WOORITECHINVEST_2024_STAGE4B_DIGITAL_ASSET_EVENT_CAP | 041190 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_4B_too_late_if_digital_asset_financial_event_premium_not_capped | True | True |
| R13L94_REVIEW_R6_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_041190_2024_03_05_TRIGGER | 041190 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_4B_too_late_if_digital_asset_financial_event_premium_not_capped | True | True |
| C28_R8L103_06_041460_Stage2_2024-10-02 | 041460 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_4B_too_late | True | True |
| C27-R8L105-004|Stage2|2024-03-05 | 041510 | C27_CONTENT_IP_GLOBAL_MONETIZATION | residual_error_needs_C27_specific_bridge_or_guard | True | True |
| R8L97_C27_SM_2024_STAGE2_ACTIONABLE_ARTIST_IP_GLOBAL_TOUR_FANDOM_MONETIZATION_BRIDGE | 041510 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R8L93_C27_041510_20240527_STAGE2_FALSE_POSITIVE_KPOP_LABEL_SPIKE | 041510 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_false_positive_if_Kpop_global_content_vocabulary_overcredited | True | True |
| None | 041830 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | True | True |
| None | 041830 | C24_BIO_TRIAL_DATA_EVENT_RISK | C24 must require fresh binary/data endpoint quality; reroute commercialization, device, reimbursement, or price-only events to C23/C25/local_4B as appropriate. | True | True |
| TRG_R7L82-C25-041830-INBODY-DIAGNOSTIC-DEVICE-EXPORT-BOUNDED | 041830 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | C25 should allow bounded diagnostic-device export positives only when export channel, hospital/fitness/clinic reorder, reimbursement or distributor channel quality, revenue conversion and margin bridge are visible. InBody had moderate MFE with bounded MAE, so it should be RiskWatch/Stage2-Yellow after source repair, not forced 4B. | True | True |
| V12_COMPACT_C25_R7L107_041830_20240429_Stage2_041830_2024-04-29_Stage2 | 041830 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive | True | True |
| None | 041830 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | None | True | True |
| R8L92_C26_CAFE24_2024_STAGE2_ACTIONABLE_COMMERCE_PLATFORM_AD_REVENUE_LEVERAGE | 042000 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R8L99_C26_CAFE24_2024_STAGE2_ACTIONABLE_COMMERCE_PLATFORM_GMV_AD_TAKE_RATE_OPERATING_LEVERAGE | 042000 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| TR_C26_L105_042000_Stage2Actionable_20240516 | 042000 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_missed_structural | True | True |
| C04_P1_TO50_TRG_20 | 042370 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive | True | True |
| C04_STATIC_TO50_TRG_11 | 042370 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive | True | True |
| None | 042510 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | None | False | True |
| RAONSECURE_042510_2024_01_23_STAGE2_FALSE_POSITIVE_IDENTITY_SECURITY_EVENT | 042510 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive | False | True |
| R8L92_C28_042510_20240126_STAGE2_FALSE_POSITIVE_DIGITAL_ID_AUTH | 042510 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive_if_digital_ID_authentication_theme_overcredited | True | True |
| V12_COMPACT_C28_R8L104_042510_20240604_042510_2024-06-05_4B-Local-Watch | 042510 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive | True | True |
| None | 042510 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| None | 042510 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | True | True |
| None | 042520 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | None | True | True |
| R1L116-C01-001 | 042660 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_correct_when_backlog_is_entity_level_and_margin_bridge_is_visible | True | True |
| C03_R1L111_002_TRIGGER | 042660 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_missed_structural | True | True |
| T_C03_R1L107_042660_20240618_STAGE4B | 042660 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | naval_defense_and_shipbuilding_capacity_contaminant_should_route_to_C01_C05_unless_export_backlog_cash_bridge_is_explicit | True | True |
| T_C03_R1L108_042660_20240821_STAGE4B | 042660 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current profile can over-promote defense beta unless sovereign funded backlog, delivery schedule and margin/cash bridge are verified | True | True |
| HDI_042670_2024_02_02_STAGE2_FALSE_POSITIVE_ORDER_CYCLE_MARGIN_BRIDGE | 042670 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_false_positive | False | True |
| C01_R1L100_042670_machinery_beta_no_backlog_margin_bridge_T1 | 042670 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_false_positive_if_stage2_bonus_uses_equipment_beta_only | False | True |
| R1L116-C01-007 | 042670 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_false_positive_if_machinery_recovery_proxy_replaces_order_margin_bridge | True | True |
| HANMI_042700_2024_02_08_STAGE2A_HBM_CUSTOMER_CAPACITY | 042700 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_4B_too_late | False | True |
| TRG_C06_R2_L109_042700_20240322_TCBONDER_CUSTOMER_CAPACITY_PROXY | 042700 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_too_late | True | True |
| T_C06_R2L103_042700_20240201_Stage3Yellow_CROSS_C07 | 042700 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_needs_C06_vs_C07_C08_C09_reroute_guard | True | True |
| V12_COMPACT_042700_2024-03-26_C07_TCBONDER_ORDER_RELATIVE_STRENGTH_CONFIRMATION | 042700 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_false_positive | False | True |
| V12_COMPACT_042700_2024-06-13_C07_LEADER_LATE_EXTENSION_AFTER_REPRICING | 042700 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_false_positive | False | True |
| HANMI_042700_2024_02_08_STAGE2A_HBM_TCB_BONDER_ORDER_RS | 042700 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_4B_too_late | False | True |
| C07_R2L90_042700_20240208_STAGE2A | 042700 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_too_late | True | True |
| V12_COMPACT_042700_2024-02-01_Stage3-Yellow | 042700 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_false_positive | True | True |
| C07_R2L90_042700_20240614_STAGE4B_OVERLAY | 042700 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_4B_too_late | True | True |
| TRG-C09-L116-01-042700-Stage2Actionable-2024-02-15 | 042700 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_missed_structural_if_all_C09_is_treated_as_price_only_blowoff | True | True |
| T_C09_R2L111_01_042700_20240201 | 042700 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_false_positive | True | True |
| C31_L101_T002_042700 | 042700 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_too_permissive_without_high_MAE_4B_overlay | True | True |
| C32_042700_20240326_STAGE2_ACTIONABLE | 042700 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive_or_overpromotion_risk | True | True |
| None | 043150 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | None | False | True |
| TRG_R7L77-C25-043150-VATECH-DENTAL-IMAGING-EXPORT-BETA-FADE | 043150 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive | True | True |
| None | 043150 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | None | True | True |
| R7L91_C25_VATECH_2024_STAGE2_FALSE_POSITIVE_DENTAL_IMAGING_EXPORT_RECOVERY | 043150 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive_if_dental_imaging_export_recovery_counts_without_order_reimbursement_margin_bridge | True | True |
| V12_COMPACT_C25_R7L107_043150_20240712_Stage2_Actionable_043150_2024-07-12_Stage2-Actionable | 043150 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive | True | True |
| TRG_R7L82-C25-043150-VATECH-DENTAL-IMAGING-EXPORT-FADE | 043150 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | C25 should not treat dental-imaging device export/reimbursement theme beta as durable Stage2 unless distributor channel order, dental clinic demand, reimbursement or capex cycle, revenue conversion and margin bridge are visible. Vatech had almost no forward MFE and a persistent MAE path. | True | True |
| TRG_R7L77-C25-043150-VATECH-DENTAL-IMAGING-EXPORT-BETA-FADE | 043150 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | C25 should not treat dental imaging/export-device beta as durable Stage2 unless export channel reorder, installed-base utilization, distributor inventory and margin bridge are visible. Vatech failed to generate meaningful MFE and then drifted lower, so it is a no-durable-Green/local-4B boundary. | True | True |
| None | 043150 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | None | True | True |
| R13_CROSS_043150_2024-02-01_Stage4B-Local-DentalImagingExportWeakness | 043150 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive | True | True |
| R13L91_REVIEW_R7_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_043150_2024_04_01_TRIGGER | 043150 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive_if_dental_imaging_export_recovery_counts_without_order_reimbursement_margin_bridge | True | True |
| R1L87_C01_044450_20240117_STAGE2_FALSE_POSITIVE_SHIPPING_BACKLOG_THEME | 044450 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_false_positive_if_shipping_backlog_theme_promoted_without_fresh_bridge | True | True |
| R13L87_REVIEW_R1_C01_ORDER_BACKLOG_MARGIN_BRIDGE_044450_2024-01-17 | 044450 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R1L88_C05_HANYANGENG_2023_STAGE4B_CLEANROOM_EPC_EVENT_CAP | 045100 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | current_profile_false_positive_if_cleanroom_EPC_spike_counts_as_structural_green | True | True |
| R1L97_C05_HANYANGENG_2024_STAGE4B_SEMICON_FACILITY_EPC_EVENT_CAP | 045100 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | current_profile_4B_too_late_if_semicon_facility_EPC_event_premium_not_capped | True | True |
| C04_P1_TO50_TRG_15 | 046120 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive | True | True |
| C04_R1_L112_046120_2024_07_17_CZECH_PREFERRED_BIDDER_INSPECTION_THEME_FALSE_POSITIVE_TRIGGER | 046120 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive | True | True |
| C04_STATIC_TO50_TRG_09 | 046120 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive | True | True |
| R11L92_C04_ORBITECH_2024_STAGE2_FALSE_POSITIVE_NUCLEAR_INSPECTION_THEME | 046120 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive_if_nuclear_inspection_theme_counts_without_project_service_margin_bridge | True | True |
| TRG_R1L81-C04-046120-ORBITECH-NUCLEAR-INSPECTION-THEME-FADE | 046120 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | C04 should not treat nuclear inspection/radiation-safety theme beta as durable Stage2 unless inspection backlog, project order, customer quality, revenue and margin bridge are visible. Orbitech had only small MFE and then a deep MAE path. | True | True |
| TRG_R11L78-C04-046120-ORBITEC-NUCLEAR-INSPECTION-THEME-DELAY-FADE | 046120 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | C04 should not treat nuclear-inspection/radiation policy beta as durable Stage2 unless inspection work, named project, regulatory path, order backlog and margin bridge are visible. Orbitec had limited MFE and then a deep drawdown, making it local 4B-watch rather than durable Green. | True | True |
| R13L92_REVIEW_R11_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_046120_2024_05_27_TRIGGER | 046120 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive_if_nuclear_inspection_theme_counts_without_project_service_margin_bridge | True | True |
| R10L97_C30_WOOWONDEV_2024_STAGE4B_LOCAL_CIVIL_INFRA_EVENT_CAP | 046940 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_4B_too_late_if_local_civil_infra_event_premium_not_capped | True | True |
| None | 047040 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | True | True |
| TRG_C05_047040_20230131_STAGE2_FALSE_POSITIVE | 047040 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | current_profile_false_positive_if_order_headline_scored_without_margin_bridge | True | True |
| T_C05_R1L109_047040_20240110_LARGE_BUILDER_ORDERBOOK_STAGE2_WATCH | 047040 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | True | True |
| T_C05_R1L108_047040_20240403_ORDERBOOK_LABEL_COUNTER | 047040 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | True | True |
| R11L90_C05_DAEWOOE_C_2024_STAGE2_ACTIONABLE_OVERSEAS_EPC_POLICY_CONTRACT_MARGIN_BRIDGE | 047040 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| None | 047040 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | False | True |
| None | 047040 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | True | True |
| R1L86_C05_047040_20240715_STAGE2_FALSE_POSITIVE_MEGA_CONTRACT_THEME | 047040 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | current_profile_false_positive_if_backlog_theme_overcredited | True | True |
| T_C05_R1L108_047040_20240717_POST_PEAK_LOCAL4B | 047040 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | True | True |
| TRG_R10L81-C30-047040-DAEWOO-E&C-BOUNDED-BUILDER-NO-FORCED4B | 047040 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should keep PF/orderbook monitoring active for bounded large builders, but should not force local 4B or hard 4C when MAE is contained and no non-price refinancing, liquidity or solvency break is confirmed. | True | True |
| TRG_R10L77-C30-047040-DAEWOO-E&C-LARGECAP-PF-RISKWATCH-NO-HARD4C | 047040 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should keep PF/orderbook RiskWatch active for large builders, but bounded MAE and recovery/sideways price action should not become hard 4C without refinancing, impairment, covenant, auditor/control or solvency break evidence. Daewoo E&C is a no-hard-4C boundary row. | True | True |
| None | 047040 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | True | True |
| TRG_R10L77-C30-047040-DAEWOO-E&C-LARGECAP-PF-RISKWATCH-NO-HARD4C | 047040 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive | True | True |
| TRG_R10L73-C30-047040-DAEWOO-LARGE-BUILDER-BUFFER-NOFULL4B | 047040 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should distinguish large-builder PF fear from a balance-sheet break. 대우건설 had bounded MAE and later tradable MFE, so it should remain RiskWatch/no-full-4B unless explicit impairment/refinancing/default evidence appears. | True | True |
| C30_R10L105_047040_20240403_Stage2 | 047040 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_error_if_C30_overcredits_price_or_low_PBR_without_balance_sheet_bridge | True | True |
| V12_COMPACT_047040_2024-07-15_construction_beta_event_spike_without_clean_cash_bridge | 047040 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive | False | True |
| R10L87_C30_DAEWOO_2024_STAGE2_FALSE_POSITIVE_SECTOR_BETA | 047040 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive_if_order_or_sector_beta_counts_without_cashflow_bridge | True | True |
| R10L94_C30_DAEWOOE_C_2024_STAGE2_ACTIONABLE_MAJOR_BUILDER_ORDER_BACKLOG_FUNDING_BRIDGE | 047040 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| TRG_C30_R10L100_047040_STAGE2A_20240125 | 047040 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_too_late | False | True |
| R10L83_C30_047040_20240715_STAGE2_FALSE_POSITIVE_PF_RELIEF_SPIKE | 047040 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive | True | True |
| TRG_R10L73-C30-047040-DAEWOO-LARGE-BUILDER-BUFFER-NOFULL4B | 047040 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should distinguish large-builder PF fear from a balance-sheet break. 대우건설 had bounded MAE and later tradable MFE, so it should remain RiskWatch/no-full-4B unless explicit impairment/refinancing/default evidence appears. | True | True |
| C30_R10L104_047040_20240717_4B_Local_Watch | 047040 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive_if_promoted_beyond_local_4B | True | True |
| TRG_C30_R10L100_047040_STAGE4B_OVERLAY_20240718 | 047040 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_4B_too_late | False | True |
| R13L86_REVIEW_R1_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_047040_2024-07-15 | 047040 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R13L87_REVIEW_C30_DAEWOO_2024_STAGE2_FALSE_POSITIVE_SECTOR_BETA | 047040 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive_if_order_or_sector_beta_counts_without_cashflow_bridge | True | True |
| None | 047050 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| R4L99_C16_POSCOINTL_2024_STAGE2_FALSE_POSITIVE_ENERGY_TRADING_RESOURCE_WATCH | 047050 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_false_positive_if_energy_resource_watch_counts_without_offtake_volume_inventory_margin_revision_bridge | True | True |
| None | 047050 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| None | 047050 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| None | 047050 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| T_C15_R4L104_047400_Stage2_20240118 | 047400 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive_if_strategic_material_keyword_gets_actionable_bonus | True | True |
| None | 047400 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| None | 047400 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| C16-102-05-047400-T1 | 047400 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_false_positive | True | True |
| V12_COMPACT_R13L12_ACCT_PRICE_17_C16_047400_20240118_047400_2024-01-18_Stage2 | 047400 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | True | True |
| TRG_R8L75-C28-047560-ESTSOFT-AI-AVATAR-SOFTWARE-THEME-SPIKE-FADE | 047560 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive | True | True |
| R8L97_C28_ESTSOFT_2024_STAGE2_ACTIONABLE_AI_SOFTWARE_LICENSE_CONTRACT_RETENTION_BRIDGE | 047560 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| TRG_R8L75-C28-047560-ESTSOFT-AI-AVATAR-SOFTWARE-THEME-SPIKE-FADE | 047560 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | C28 should not treat AI software/avatar headline MFE as durable Stage2 unless enterprise contract retention, paid seat expansion, ARR/license revenue or margin bridge is visible. ESTsoft produced an enormous MFE, but later drawdown shows that theme-spike winners need lifecycle local 4B when bridge evidence fades. | True | True |
| R8L84_C28_047560_20240126_STAGE2_FALSE_POSITIVE_AI_AVATAR_SW_THEME | 047560 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive_if_AI_theme_overcredited | True | True |
| V12_COMPACT_C28_R8L104_047560_20240717_047560_2024-07-18_4B-Local-Watch | 047560 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive | True | True |
| R13_4B4C_L12_09_047560_20240612_4B_Local_Watch | 047560 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_source_proxy_row_promotes_to_green_or_full_4B | True | True |
| R13_CROSS_047560_2024-06-12_Stage4B | 047560 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | True | True |
| None | 047560 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | True | True |
| T_C01_R1L111_047810_20240306_Stage2-Actionable | 047810 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | platform backlog label alone was too weak; C01 Stage2 should be capped without fresh order margin or delivery-margin refresh | True | True |
| T_C03_R1L108_047810_20240614_STAGE2 | 047810 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current profile can over-promote defense beta unless sovereign funded backlog, delivery schedule and margin/cash bridge are verified | True | True |
| T_C03_R1L107_047810_20240718_STAGE2 | 047810 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | aerospace_export_label_repeated_without_incremental_order_margin_bridge_is_false_positive | True | True |
| R1L99_C03_KAI_2024_STAGE2_FALSE_POSITIVE_AIRCRAFT_EXPORT_FRAMEWORK_WATCH | 047810 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_false_positive_if_aircraft_export_framework_watch_counts_without_final_contract_delivery_backlog_margin_revision_bridge | True | True |
| T_C03_R1L107_047810_20240223_STAGE2ACTIONABLE | 047810 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | aerospace_export_label_needs_delivery_and_margin_refresh_before_stage3 | True | True |
| None | 047810 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | None | False | True |
| T_C03_R1L108_047810_20240919_STAGE4C | 047810 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current profile can over-promote defense beta unless sovereign funded backlog, delivery schedule and margin/cash bridge are verified | True | True |
| None | 047810 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | None | False | True |
| V12_COMPACT_R13L2_C03_047810_20240701_STAGE2_047810_2024-07-01_cross_archetype_high_MAE_guardrail_review | 047810 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| R8L96_C27_DAEWONMEDIA_2024_STAGE2_FALSE_POSITIVE_LEGACY_ANIMATION_IP_WATCH | 048910 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_false_positive_if_legacy_animation_IP_watch_counts_without_distribution_slate_licensing_margin_revision_bridge | True | True |
| R13L96_REVIEW_R8_C27_CONTENT_IP_GLOBAL_MONETIZATION_048910_2024_01_24_TRIGGER | 048910 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_legacy_animation_IP_watch_counts_without_distribution_slate_licensing_margin_revision_bridge | True | True |
| TRG-C09-L116-06-049080-Stage2-2024-03-15 | 049080 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_false_positive_if_RF_component_theme_accepted_as_advanced_equipment | True | True |
| R2L112-C10-003-T1 | 049080 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_false_positive_if_memory_beta_relative_strength_overrides_missing_order_bridge | True | True |
| None | 049180 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | None | True | True |
| C28_R8L103_02_049480_Stage2_Actionable_2024-10-02 | 049480 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_correct | True | True |
| R8L86_C28_049480_20240401_STAGE2_FALSE_POSITIVE_SECURITY_AI_THEME | 049480 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive_if_AI_security_theme_overcredited | True | True |
| R13L86_REVIEW_R8_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_049480_2024-04-01 | 049480 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R5_L122_C18_010 | 049770 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | True | True |
| None | 049770 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | True | True |
| C19_R5L119_06_049770_Stage2_Actionable_2024-02-01 | 049770 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | True | True |
| C20_R5L117_049770_20240201_Stage2_Actionable | 049770 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_error_or_stress_case | True | True |
| R11L92_C04_KEPCOKPS_2024_STAGE2_ACTIONABLE_NUCLEAR_O_AND_M_POLICY_PROJECT_BRIDGE | 051600 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| C04_P1_TO50_TRG_06 | 051600 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive | True | True |
| R11L87_C04_051600_20240712_STAGE2_NUCLEAR_OM_PROJECT | 051600 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_correct_if_project_service_backlog_bridge_required | True | True |
| None | 051600 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | None | True | True |
| None | 051600 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | None | False | True |
| T_C04_R1L107_051600_20240718_Stage3-Yellow | 051600 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | yellow_allowed_when_service_revenue_bridge_visible_but_green_needs_revision_margin_confirmation | True | True |
| C04_P1_TO50_TRG_05 | 051600 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive | True | True |
| C04_STATIC_TO50_TRG_03 | 051600 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive | True | True |
| TRG_R11L73-C31-051600-KEPCO-KPS-CZECH-NUCLEAR-SERVICE-PROXY-RISKWATCH | 051600 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should flag nuclear service proxies as RiskWatch unless service scope, O&M participation, or backlog bridge is verified. KEPCO KPS had bounded MAE and later recovery, so it should not become full 4B or hard 4C from the policy headline alone. | False | True |
| TRG_R11L73-C31-051600-KEPCO-KPS-CZECH-NUCLEAR-SERVICE-PROXY-RISKWATCH | 051600 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should flag nuclear service proxies as RiskWatch unless service scope, O&M participation, or backlog bridge is verified. KEPCO KPS had bounded MAE and later recovery, so it should not become full 4B or hard 4C from the policy headline alone. | False | True |
| R13L87_REVIEW_R11_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_051600_2024-07-12 | 051600 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_correct | True | True |
| TRG_R5L80-C20-051900-LG-HH-CHINA-BRAND-RECOVERY-BOUNDARY | 051900 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | C20 should not force bounded large-cap China beauty recovery rows into 4B when MAE is controlled, but it also should not mark durable Stage2 without sell-through, channel inventory, brand mix, revenue and margin bridge. LG H&H is a bounded no-forced-4B boundary. | True | True |
| R5L91_C20_LGHNH_2024_STAGE2_FALSE_POSITIVE_LUXURY_CHINA_RECOVERY | 051900 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive_if_luxury_china_channel_recovery_counts_without_reorder_margin_revision_bridge | True | True |
| R5L85_C20_051900_20240510_STAGE2_FALSE_POSITIVE_BEAUTY_REOPENING_REBOUND | 051900 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive_if_reopening_beta_overcredited | True | True |
| R5L91_C20_051900_20240430_STAGE2_FALSE_POSITIVE_LEGACY_BEAUTY_CHANNEL | 051900 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive_if_legacy_beauty_channel_vocabulary_overcredited | True | True |
| R13L85_REVIEW_R5_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_051900_2024-05-10 | 051900 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| R13L91_REVIEW_R5_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_051900_2024_05_10_TRIGGER | 051900 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive_if_luxury_china_channel_recovery_counts_without_reorder_margin_revision_bridge | True | True |
| TRG-C11-051910-20240208-STAGE2 | 051910 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive_if_green_or_actionable | False | True |
| T_C11_R3L107_051910_STAGE4B_20240216 | 051910 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive_if_orderbook_label_is_overcredited | True | True |
| None | 051910 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | True | True |
| None | 051910 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | True | True |
| T_C13_R3L103_051910_STAGE2ACTIONABLE_20240201 | 051910 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_mixed_parent_battery_chemical_balance_sheet_contamination | True | True |
| TRG_R3L81-C13-051910-LG-CHEM-CATHODE-AMPC-IRA-THEME-FADE | 051910 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | C13 should not treat cathode/IRA/AMPC policy beta as durable Stage2 unless JV utilization, customer volume, subsidy economics, revenue conversion and margin bridge are visible. LG Chem had an early MFE but then a severe high-MAE drawdown path. | True | True |
| R3L87_C13_051910_20240216_STAGE2_FALSE_POSITIVE_BATTERY_CHEM_AMPC | 051910 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_false_positive_if_policy_credit_theme_overcredited | True | True |
| R3L84_C13_051910_20240216_STAGE2_FALSE_POSITIVE_HOLDCO_AMPC_JV_DISCOUNT | 051910 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_false_positive_if_policy_optionalities_overcredited | True | True |
| T_C13_R3L104_051910_STAGE3YELLOW_20240201 | 051910 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | True | True |
| T_C13_R3L105_051910_STAGE4B_20240216 | 051910 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | True | True |
| TRG_R3L73-C14-051910-LGCHEM-INTEGRATED-MATERIALS-DEMAND-RISK-NO-HARD4C | 051910 | C14_EV_DEMAND_SLOWDOWN_4B_4C | C14 should flag EV/material demand slowdown risk, but not convert diversified integrated chemical/cathode exposure into hard 4C when later rebound and business-buffer evidence can exist. The correct label is RiskWatch/local 4B boundary, not hard thesis break without non-price evidence. | True | True |
| TRG_R3L73-C14-051910-LGCHEM-INTEGRATED-MATERIALS-DEMAND-RISK-NO-HARD4C | 051910 | C14_EV_DEMAND_SLOWDOWN_4B_4C | C14 should flag EV/material demand slowdown risk, but not convert diversified integrated chemical/cathode exposure into hard 4C when later rebound and business-buffer evidence can exist. The correct label is RiskWatch/local 4B boundary, not hard thesis break without non-price evidence. | True | True |
| R3L88_C14_LGCHEM_2023_STAGE4B_EV_MATERIALS_DEMAND_SLOWDOWN | 051910 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_4B_too_late_if_EV_materials_price_volume_margin_break_not_capped | True | True |
| T_C14_R3L108_051910_STAGE4B_20240216 | 051910 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_false_positive | True | True |
| LGCHEM_051910_2024_02_21_4C_EV_DEMAND_SLOWDOWN | 051910 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_4C_too_late | False | True |
| T_C15_R4L104_051910_Stage2_20240216 | 051910 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive_if_material_label_receives_stage2_actionable_bonus | True | True |
| T_C15_R4L105_051910_20240216_03_4C | 051910 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive | True | True |
| None | 051910 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | True | True |
| C31_L101_T006_051910 | 051910 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | True | True |
| R13L87_REVIEW_R3_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_051910_2024-02-16 | 051910 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R13_4B4C_L12_15_051910_20240216_4B_Local_Watch | 051910 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_source_proxy_row_promotes_to_green_or_full_4B | True | True |
| V12_COMPACT_R13L2_C17_051910_20240216_STAGE2_051910_2024-02-16_cross_archetype_high_MAE_guardrail_review | 051910 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| R13_CROSS_051910_2024-02-16_Stage4B | 051910 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| T_R13_STAGE2FP_L5_051910_Stage2_2024-02-16 | 051910 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_stage2_false_positive_or_overpromotion_risk | True | True |
| R13_CROSS_051910_2024-02-16_Stage2 | 051910 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive | True | True |
| None | 051910 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | None | True | True |
| C04_P1_TO50_TRG_03 | 052690 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive | True | True |
| R11L96_C04_KEPCOE_C_2024_STAGE2_ACTIONABLE_NUCLEAR_ENGINEERING_POLICY_PROJECT_BRIDGE | 052690 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R1L85_C04_052690_20240429_STAGE2_NUCLEAR_ENGINEERING_PROJECT_BRIDGE | 052690 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_correct_if_project_bridge_required | True | True |
| C04_STATIC_TO50_TRG_02 | 052690 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive | True | True |
| None | 052690 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | None | True | True |
| None | 052690 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | None | False | True |
| T_C04_R1L107_052690_20240718_Stage4B | 052690 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | must_remain_stage4b_or_4c_watch_unless_final_contract_cash_bridge_appears | True | True |
| C04_P1_TO50_TRG_04 | 052690 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive | True | True |
| R11L88_C05_052690_20240422_STAGE2_NUCLEAR_EPC_SCOPE | 052690 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | current_profile_correct_if_project_scope_margin_cash_bridge_required | True | True |
| R11L90_C05_KEPCOE_C_2024_STAGE4B_NUCLEAR_ENGINEERING_EPC_POLICY_CAP | 052690 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | current_profile_4B_too_late_if_nuclear_engineering_EPC_policy_premium_not_capped | True | True |
| TRG_R11L73-C31-052690-KEPCO-ENC-CZECH-NUCLEAR-EPC-PROXY-CHASE | 052690 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should not treat the nuclear preferred-bidder headline as durable Stage2 for EPC/engineering proxies unless named scope, contract allocation, revenue timing, or backlog bridge is visible. KEPCO E&C gapped into the event but then opened severe MAE and drawdown. | False | True |
| TRG_R11L73-C31-052690-KEPCO-ENC-CZECH-NUCLEAR-EPC-PROXY-CHASE | 052690 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should not treat the nuclear preferred-bidder headline as durable Stage2 for EPC/engineering proxies unless named scope, contract allocation, revenue timing, or backlog bridge is visible. KEPCO E&C gapped into the event but then opened severe MAE and drawdown. | False | True |
| R13L88_REVIEW_R11_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_052690_2024-04-22 | 052690 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_correct | True | True |
| R13_4B4C_L12_17_052690_20240718_4B_Local_Watch | 052690 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_source_proxy_row_promotes_to_green_or_full_4B | True | True |
| R13L85_REVIEW_R1_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_052690_2024-04-29 | 052690 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_correct | True | True |
| R13L90_REVIEW_R11_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_052690_2024_03_11_TRIGGER | 052690 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_4B_too_late_if_nuclear_engineering_EPC_policy_premium_not_capped | True | True |
| None | 052860 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | False | True |
| TRG_R11L75-C31-053290-NE-NEUNGYULE-MEDQUOTA-EDU-PROXY-FADE | 053290 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | True | True |
| R11L88_C31_NEE_2024_STAGE2_FALSE_POSITIVE_EDUCATION_POLICY_THEME | 053290 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive_if_education_policy_theme_counts_without_revenue_contract_bridge | True | True |
| TRG_R11L75-C31-053290-NE-NEUNGYULE-MEDQUOTA-EDU-PROXY-FADE | 053290 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should not treat broad education-policy beta as durable Stage2 unless the policy connects to direct product demand, paid course enrollment, channel expansion or margin bridge. NE Neungyule had only tiny MFE and then severe drawdown before later theme rebounds. | True | True |
| R13L88_REVIEW_C31_NEE_2024_STAGE2_FALSE_POSITIVE_EDUCATION_POLICY_THEME | 053290 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_education_policy_theme_counts_without_revenue_contract_bridge | True | True |
| C28_R8L103_07_053300_Stage2_2024-09-02 | 053300 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_correct | True | True |
| None | 053450 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | False | True |
| TRG_R8L82-C28-053580-WEBCASH-FINTECH-SOFTWARE-RETENTION-FADE | 053580 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | C28 should not treat B2B fintech software retention theme beta as durable Stage2 unless customer retention, paid conversion, renewal, usage, revenue and margin bridge are visible. WebCash had modest MFE and then high-MAE fade. | True | True |
| None | 053610 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | False | True |
| TRG-C09-L116-03-053610-Stage3Yellow-2024-02-15 | 053610 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_false_positive_if_short_lived_packaging_theme_promoted | True | True |
| R2L112-C10-001-T1 | 053610 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_missed_structural_if_2024_memory_drawdown_blocks_2025_recovery_band | True | True |
| None | 053690 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | True | True |
| R1L88_C05_HANMIGLOBAL_2022_STAGE4B_NEOM_PM_EVENT_CAP | 053690 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | current_profile_4B_too_late_if_project_PM_theme_not_capped | True | True |
| R10L95_C30_HANMIGLOBAL_2024_STAGE2_ACTIONABLE_CM_ORDER_CASHFLOW_BRIDGE | 053690 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| V12_COMPACT_053800_2024-07-01_platform_ad_budget_retention_opm_bridge_cleanup | 053800 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| None | 053800 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | None | False | True |
| R8L88_C28_AHNLAB_2024_STAGE2_FALSE_POSITIVE_SECURITY_QUALITY | 053800 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive_if_security_quality_counts_without_contract_retention_revision_bridge | True | True |
| R8L94_C28_AHNLAB_2024_STAGE2_FALSE_POSITIVE_CYBERSECURITY_RETENTION_WATCH | 053800 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive_if_cybersecurity_retention_watch_counts_without_enterprise_renewal_ARR_margin_revision_bridge | True | True |
| R8L86_C28_053800_20240125_STAGE2_FALSE_POSITIVE_SECURITY_THEME_BETA | 053800 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive_if_security_beta_overcredited | True | True |
| R13L86_REVIEW_R8_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_053800_2024-01-25 | 053800 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R13L94_REVIEW_R8_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_053800_2024_01_24_TRIGGER | 053800 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive_if_cybersecurity_retention_watch_counts_without_enterprise_renewal_ARR_margin_revision_bridge | True | True |
| TRG_R12L81-C31-054050-NONGWOO-BIO-SEED-AGRI-POLICY-BOUNDED | 054050 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should keep seed/agri policy monitoring active, but should not force local 4B when MAE is bounded and no non-price demand or margin break is confirmed. Nongwoo Bio is a RiskWatch/no durable Stage2/no forced 4B boundary. | True | True |
| R10L95_C30_YOOSHIN_2024_STAGE2_FALSE_POSITIVE_ENGINEERING_PF_NORMALIZATION_WATCH | 054930 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive_if_engineering_PF_normalization_watch_counts_without_order_fee_cashflow_margin_bridge | True | True |
| R13L95_REVIEW_R10_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_054930_2024_02_13_TRIGGER | 054930 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_engineering_PF_normalization_watch_counts_without_order_fee_cashflow_margin_bridge | True | True |
| V12_COMPACT_C21-SHINHAN-20240201_055550_2024-02-01_Stage2_Actionable_CapitalReturn_ValueUp_Bridge | 055550 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | False | True |
| R6L94_C21_SHINHAN_2024_STAGE2_ACTIONABLE_BANK_VALUEUP_CAPITAL_RETURN_ROE_PBR_BRIDGE | 055550 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| TRG_R6L79-C21-055550-SHINHAN-BANK-HOLDCO-CAPITAL-RETURN | 055550 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | C21 should protect bank-holding positives when ROE/PBR rerating maps to capital buffer, dividend, buyback, treasury cancellation and earnings-quality bridge. Shinhan produced large MFE with bounded entry-basis MAE, but raw share-count changes inside the window require validation before runtime promotion. | True | True |
| R6L83_C21_055550_20240202_STAGE2_BANK_VALUEUP_CAPITAL_RETURN | 055550 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_correct | True | True |
| None | 055550 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | False | True |
| None | 055550 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | True | True |
| None | 055550 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | True | True |
| None | 055550 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | False | True |
| R12L85_C31_055550_20240129_STAGE2_VALUEUP_POLICY_CAPITAL_RETURN | 055550 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_correct_if_policy_to_capital_return_bridge_required | True | True |
| V12_COMPACT_055550_2024-03-07_policy_valueup_bank_capital_return_cash_bridge | 055550 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | True | True |
| V12_COMPACT_055550_2024-04-26_policy_valueup_bank_brokerage_ROE_PBR_capital_return_execution_bridge | 055550 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_correct | True | True |
| C31_R11L106_TRG_03 | 055550 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | None | True | True |
| None | 055550 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | None | False | True |
| None | 055550 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| R13L85_REVIEW_R12_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_055550_2024-01-29 | 055550 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_correct | True | True |
| TRG_R12L80-C31-057030-YBMNET-ONLINE-EDUCATION-POLICY-FADE | 057030 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should not treat online education or language-learning policy beta as durable Stage2 unless paid conversion, institutional demand, subscription revenue and margin bridge are visible. YBM Net produced a tradable MFE but then a high-MAE fade. | True | True |
| R11L88_C31_YBMNET_2024_STAGE4B_DIGITAL_EDU_POLICY_THEME_CAP | 057030 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_4B_too_late_if_digital_education_policy_theme_premium_not_capped | True | True |
| R13L88_REVIEW_C31_YBMNET_2024_STAGE4B_DIGITAL_EDU_POLICY_THEME_CAP | 057030 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late_if_digital_education_policy_theme_premium_not_capped | True | True |
| V12_COMPACT_C25_R7L107_058110_20240416_Stage2_FalsePositive_058110_2024-04-16_Stage2-FalsePositive | 058110 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive | True | True |
| R4L96_C15_POSCOSTEELION_2024_STAGE2_ACTIONABLE_COATED_STEEL_SPREAD_MARGIN_BRIDGE | 058430 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R2L93_C08_058470_20240213_STAGE2_IC_TEST_SOCKET_REPEAT | 058470 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_correct_if_customer_qualification_repeat_demand_margin_cash_bridge_required_but_Green_strict | True | True |
| C08_R2_L112_004_058470_Stage2_Actionable | 058470 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_too_late | True | True |
| R2L92_C08_LEENO_2024_STAGE2_ACTIONABLE_TEST_SOCKET_CUSTOMER_QUALITY_MARGIN | 058470 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| None | 058470 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | False | True |
| None | 058470 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | False | True |
| None | 058470 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| TRG_R8L75-C28-058970-EMRO-PROCUREMENT-SAAS-CONTRACT-RETENTION-BRIDGE | 058970 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_correct | True | True |
| R8L93_C28_058970_20240227_STAGE2_SCM_SAAS_RETENTION | 058970 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_correct_if_contract_retention_ARR_margin_cash_bridge_required_but_Green_strict | True | True |
| TRG_R8L75-C28-058970-EMRO-PROCUREMENT-SAAS-CONTRACT-RETENTION-BRIDGE | 058970 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | C28 should allow a delayed Stage2 when procurement SaaS / supply-chain AI demand connects to actual enterprise contract retention, customer expansion, recurring license or margin bridge. EMRO produced controlled-MAE follow-through after the August reset, but the price shard shows share-count changes, so runtime promotion needs validation. | True | True |
| None | 059210 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | None | True | True |
| TR_C26_L105_060250_Stage2_20240930 | 060250 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_missed_structural | True | True |
| None | 060280 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | True | True |
| None | 060280 | C24_BIO_TRIAL_DATA_EVENT_RISK | C24 must require fresh binary/data endpoint quality; reroute commercialization, device, reimbursement, or price-only events to C23/C25/local_4B as appropriate. | True | True |
| None | 060280 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | None | True | True |
| R1L89_C02_LSMARINE_2024_STAGE4B_SUBSEA_CABLE_EVENT_CAP | 060370 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_4B_too_late_if_subsea_cable_event_premium_not_capped | True | True |
| None | 060370 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| None | 060370 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| TR_C26_L105_060570_Stage4B_20240516 | 060570 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| V12_COMPACT_C28-R8-L102-05_060850_2024-04-01_Stage2 | 060850 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive | True | True |
| V12_COMPACT_C28_R8L104_060850_20240812_060850_2024-08-13_Stage2 | 060850 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive | True | True |
| R8L89_C28_060850_20240102_STAGE2_ERP_SAAS_RETENTION | 060850 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_correct_if_contract_retention_margin_cash_bridge_required | True | True |
| TRG_R8L82-C28-060850-YOUNGLIMWON-ERP-CONTRACT-RETENTION-FADE | 060850 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | C28 should not treat ERP/cloud software theme beta as durable Stage2 unless ARR/subscription, renewal, churn control, implementation backlog, revenue conversion and margin bridge are visible. YoungLimWon had a theme spike and then high MAE, so it is local-4B unless retention economics are source-repaired. | True | True |
| V12_COMPACT_R13_STAGE2FP_L8_13_060850_2024-08-13_STAGE2_060850_2024-08-13_stage2_source_proxy_deep_MAE_false_positive_review | 060850 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive | True | True |
| LBSEMI_061970_2024_03_06_STAGE2_FALSE_POSITIVE_OSAT_TEST_PACKAGE | 061970 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_false_positive | False | True |
| C27-R8L105-015|Stage2|2024-03-07 | 063080 | C27_CONTENT_IP_GLOBAL_MONETIZATION | residual_error_needs_C27_specific_bridge_or_guard | True | True |
| R13_CROSS_063080_2024-03-07_Stage2 | 063080 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive | True | True |
| INTEK_064290_2024_02_20_STAGE2_FALSE_POSITIVE_INSPECTION_EQUIP_BETA | 064290 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_false_positive | False | True |
| R2L93C_C08_064290_20240220_STAGE2_FALSE_POSITIVE_INSPECTION_DECAY | 064290 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_false_positive_if_inspection_customer_quality_vocabulary_overcredited | True | True |
| INTEKPLUS_064290_2024_03_06_STAGE2_FALSE_POSITIVE_ADVANCED_INSPECTION | 064290 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_false_positive | False | True |
| T_C01_R1L111_064350_20240222_Stage2-Actionable | 064350 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | backlog path was eventually large but interim drawdown and mixed rail/defense exposure require a bridge before Green | True | True |
| R1L117-C01-001 | 064350 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_missed_structural | False | True |
| None | 064350 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | True | True |
| R11L89_C03_HYUNDAIROTEM_2024_STAGE2_ACTIONABLE_DEFENSE_EXPORT_BACKLOG | 064350 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| TRG_R11L79-C03-064350-HYUNDAI-ROTEM-GROUND-SYSTEM-EXPORT-BACKLOG | 064350 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | C03 should allow ground-system positives when export framework or follow-on contract maps to named customer/project, backlog, delivery schedule, revenue recognition and margin bridge. Hyundai Rotem produced very large MFE with controlled entry-basis MAE, but lifecycle 4B is needed if delivery/margin evidence fades. | True | True |
| TRG_R1L74-C03-064350-HYUNDAI-ROTEM-K2-GROUND-SYSTEMS-BACKLOG | 064350 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | C03 should allow Stage2 when defense-export attention is tied to a named ground-systems framework, backlog visibility, production cadence and margin bridge. Hyundai Rotem's stock-web path had large MFE and limited entry-basis MAE; after the late-2024 peak, a local 4B lifecycle guard is still needed if export/backlog evidence stops refreshing. | True | True |
| TRG_R1L74-C03-064350-HYUNDAI-ROTEM-K2-GROUND-SYSTEMS-BACKLOG | 064350 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | C03 should allow Stage2 when defense-export attention is tied to a named ground-systems framework, backlog visibility, production cadence and margin bridge. Hyundai Rotem's stock-web path had large MFE and limited entry-basis MAE; after the late-2024 peak, a local 4B lifecycle guard is still needed if export/backlog evidence stops refreshing. | True | True |
| R1L89_C03_064350_20240222_STAGE2_DEFENSE_EXPORT_BACKLOG | 064350 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_correct_if_export_framework_backlog_margin_bridge_required | True | True |
| V12_COMPACT_C03-R1L105-03_064350_2024-02-22_Stage2-Actionable | 064350 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_false_positive | True | True |
| T_C03_R1L108_064350_20240605_STAGE2_ACTIONABLE | 064350 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current profile can over-promote defense beta unless sovereign funded backlog, delivery schedule and margin/cash bridge are verified | True | True |
| T_064350_20240222_STAGE3Y_REPAIR | 064350 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_should_not_green_without_margin_refresh | False | True |
| T_064350_20240329_STAGE3Y_REPAIR | 064350 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_needs_mixed_exposure_bridge_not_generic_defense_beta | False | True |
| T_C03_R1L107_064350_20240513_STAGE3YELLOW | 064350 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | delivery_schedule_visibility_can_convert_stage2_to_yellow_but_margin_bridge_required_for_green | True | True |
| None | 064350 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | None | False | True |
| T_C03_R1L108_064350_20241018_STAGE4B | 064350 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current profile can over-promote defense beta unless sovereign funded backlog, delivery schedule and margin/cash bridge are verified | True | True |
| T_C03_R1L107_064350_20241018_STAGE4B | 064350 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | trend_continues_but_high_MAE_and_known_backlog_timing_make_stage4b_watch_preferable | True | True |
| TRG_R9L77-C29-064350-HYUNDAI-ROTEM-RAIL-MOBILITY-ORDERBOOK-MARGIN | 064350 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should allow rail/mobility equipment positives when orderbook, delivery slots, export/customer cadence, utilization and margin bridge are visible. Hyundai Rotem produced very large MFE with controlled entry-basis MAE, but the move must be lifecycle-managed if orderbook/margin evidence fades. | True | True |
| TRG_R9L77-C29-064350-HYUNDAI-ROTEM-RAIL-MOBILITY-ORDERBOOK-MARGIN | 064350 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_correct | True | True |
| C31_L101_T004_064350 | 064350 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_missed_direct_bridge_strength | True | True |
| TCK_064760_2024_03_22_STAGE2A_MEMORY_CUSTOMER_CAPACITY_PARTS | 064760 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_4B_too_late | False | True |
| R2_L110_C07 | 064760 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | None | True | True |
| TRG_R2L73-C08-064760-TCK-SIC-CONSUMABLE-CUSTOMER-QUALITY-LOCAL4B | 064760 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | C08 should not treat high-quality semi consumables as Green when near-term customer utilization or margin bridge is absent. TCK had an initial MFE but later opened large MAE and drawdown, requiring local 4B-watch rather than durable Stage2. | True | True |
| None | 064760 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | False | True |
| TRG_R2L73-C08-064760-TCK-SIC-CONSUMABLE-CUSTOMER-QUALITY-LOCAL4B | 064760 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | C08 should not treat high-quality semi consumables as Green when near-term customer utilization or margin bridge is absent. TCK had an initial MFE but later opened large MAE and drawdown, requiring local 4B-watch rather than durable Stage2. | True | True |
| TCK_064760_2024_03_06_STAGE2A_MEMORY_CONSUMABLE_RECOVERY | 064760 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_4B_too_late | False | True |
| R1L96_C01_CAPE_2024_STAGE2_FALSE_POSITIVE_SHIP_PARTS_ORDER_BACKLOG_WATCH | 064820 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_false_positive_if_ship_parts_backlog_watch_counts_without_order_quality_delivery_margin_revision_bridge | True | True |
| R13L96_REVIEW_R1_C01_ORDER_BACKLOG_MARGIN_BRIDGE_064820_2024_04_24_TRIGGER | 064820 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_ship_parts_backlog_watch_counts_without_order_quality_delivery_margin_revision_bridge | True | True |
| R12L90_C32_FNGUIDE_2024_STAGE4B_PROXY_CONTROL_PREMIUM_CAP | 064850 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_4B_too_late_if_proxy_control_premium_not_capped | True | True |
| R13L90_REVIEW_R12_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_064850_2024_09_24_TRIGGER | 064850 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_4B_too_late_if_proxy_control_premium_not_capped | True | True |
| None | 064960 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | None | False | True |
| TRG_R9L80-C29-064960-SNT-MOTIV-MOTOR-DRIVETRAIN-BOUNDED-RISKWATCH | 064960 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should not force bounded motor/drivetrain supplier rows into 4B when MAE is contained, but it also should not mark durable Stage2 without customer volume, mix, drivetrain content and margin bridge. SNT Motiv is a bounded RiskWatch row. | True | True |
| TRG_R9L75-C29-064960-SNT-MOTIVE-MOTOR-DEFENSE-AUTO-MIX-MARGIN | 064960 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| C29_R9L87_TRG_064960_S2 | 064960 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_correct | True | True |
| R9L89_C29_064960_20240129_STAGE2_AUTOMOTOR_VOLUME_MIX_CASH | 064960 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_correct_if_volume_mix_margin_cash_bridge_required | True | True |
| R9L97_C29_SNTMOTIVE_2024_STAGE2_ACTIONABLE_EV_POWERTRAIN_AUTO_PARTS_MARGIN_BRIDGE | 064960 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| None | 064960 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | True | True |
| T_C29_R9L106_064960_20240306_07_Stage2-Actionable | 064960 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| T_C29_R9L105_064960_Stage2Actionable_20240306 | 064960 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| TRG_R9L75-C29-064960-SNT-MOTIVE-MOTOR-DEFENSE-AUTO-MIX-MARGIN | 064960 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should include slow mobility suppliers when motor/module mix, electrification component exposure, customer program stability and margin bridge are visible. SNT Motive is not an explosive beta row; it is a low-volatility supplier rerating candidate that should not be overblocked but still needs non-price mix/margin evidence. | True | True |
| None | 065130 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | True | True |
| V12_COMPACT_C28-R8-L102-06_065370_2024-02-22_Stage4B | 065370 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive | True | True |
| None | 065450 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | None | False | True |
| R1L102_C03_VICTEK_2024_STAGE4B_ELECTRONIC_WARFARE_GEOPOLITICAL_EVENT_CAP | 065450 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_4B_too_late_if_electronic_warfare_defense_event_premium_not_capped | True | True |
| T_C03_R1L108_065450_20240422_STAGE4B | 065450 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current profile can over-promote defense beta unless sovereign funded backlog, delivery schedule and margin/cash bridge are verified | True | True |
| R13_4B4C_L12_04_065450_20240422_Stage4C_Watch | 065450 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_source_proxy_row_promotes_to_green_or_full_4B | True | True |
| R13_CROSS_065450_2024-04-22_Stage4B | 065450 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | True | True |
| None | 065450 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | True | True |
| None | 065510 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | True | True |
| V12_COMPACT_C25_R7L107_065510_20240701_Stage2_065510_2024-07-01_Stage2 | 065510 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive | True | True |
| R7L97_C25_HUVITZ_2024_STAGE2_FALSE_POSITIVE_OPHTHALMIC_DEVICE_EXPORT_WATCH | 065510 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive_if_ophthalmic_device_export_watch_counts_without_distributor_sellthrough_regulatory_margin_revision_bridge | True | True |
| None | 065510 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | None | True | True |
| TRG_R7L82-C25-065510-HUVITZ-OPHTHALMIC-DEVICE-SHARECOUNT-FADE | 065510 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | C25 should not treat ophthalmic/optical device export theme beta as durable Stage2 unless customer order, distributor channel, reimbursement/capex cycle, revenue conversion and margin bridge are visible. Huvitz had an early spike, a severe high-MAE fade, and 2024 shard share-count changes that require validation. | True | True |
| R7L86_C25_065510_20240215_STAGE2_FALSE_POSITIVE_OPHTHALMIC_DEVICE_REBOUND | 065510 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive_if_device_rebound_overcredited | True | True |
| R13L86_REVIEW_R7_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_065510_2024-02-15 | 065510 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| None | 065680 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | False | True |
| T_C11_R3L107_066970_STAGE2ACTIONABLE_20240322 | 066970 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive_if_orderbook_label_is_overcredited | True | True |
| TRG-C11-066970-20240325-STAGE4C | 066970 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive_if_orderbook_overcredited | False | True |
| V12_COMPACT_C12_R3L105_066970_20240216_04_066970_2024-02-16_Stage2 | 066970 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_false_positive | True | True |
| None | 066970 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | True | True |
| R3L83_C12_066970_20240322_STAGE2_FALSE_POSITIVE_CATHODE_CALLOFF | 066970 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_false_positive | True | True |
| R3L86_C12_066970_20240325_STAGE2_FALSE_POSITIVE_CATHODE_CALLOFF_RISK | 066970 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_false_positive_if_contract_headline_overcredited | True | True |
| LNF_066970_2024_02_14_STAGE2A_CATHODE_JV_UTILIZATION_IRA | 066970 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_4B_too_late | False | True |
| R3L98_C13_LF_2024_STAGE2_FALSE_POSITIVE_CATHODE_IRA_AMPC_UTILIZATION_WATCH | 066970 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_false_positive_if_cathode_IRA_AMPC_watch_counts_without_customer_calloff_JV_utilization_margin_revision_bridge | True | True |
| T_C13_R3L105_066970_STAGE2ACTIONABLE_20240322 | 066970 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | True | True |
| T_C13_R3L103_066970_STAGE3YELLOW_20240214 | 066970 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_too_fast_if_customer_calloff_absent | True | True |
| None | 066970 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | True | True |
| T_C13_R3L104_066970_STAGE4B_20240214 | 066970 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | True | True |
| T_C13_R3L105_066970_STAGE4C_20240322 | 066970 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | True | True |
| None | 066970 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | False | True |
| T_C14_R3L108_066970_STAGE4C_20240322 | 066970 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_false_positive | True | True |
| R3L91_C14_LENF_2024_STAGE4C_EV_DEMAND_SLOWDOWN_MARGIN_THESIS_BREAK | 066970 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_kept_and_hard_4C_protection_should_block_EV_cathode_positive_stage | True | True |
| V12_COMPACT_R13L11-4B4C-008_066970_2024-03-22_cross_archetype_4b_4c_boundary_retest | 066970 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R13L86_REVIEW_R3_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_066970_2024-03-25 | 066970 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R13_4B4C_L12_07_066970_20240322_Stage4C_Watch | 066970 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_source_proxy_row_promotes_to_green_or_full_4B | True | True |
| R13_CROSS_066970_2024-03-22_Stage4C | 066970 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | True | True |
| R13L83_HIGHMAE_REVIEW_066970_2024-03-22 | 066970 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| None | 066970 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | True | True |
| R13_CROSS_066970_2024-03-22_Stage4C | 066970 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| R13L91_REVIEW_R3_C14_EV_DEMAND_SLOWDOWN_4B_4C_066970_2024_03_25_TRIGGER | 066970 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_kept_and_hard_4C_protection_should_block_EV_cathode_positive_stage | True | True |
| T_R13_STAGE2FP_L5_066970_Stage2Actionable_2024-03-22 | 066970 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_stage2_false_positive_or_overpromotion_risk | True | True |
| R13_CROSS_066970_2024-03-22_Stage2-Actionable | 066970 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive | True | True |
| R8L83_C26_067160_20240108_STAGE2_LIVESTREAM_TRAFFIC_MIGRATION_POSITIVE | 067160 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_correct | True | True |
| R8L85_C26_067160_20240108_STAGE2_LIVE_PLATFORM_OPERATING_LEVERAGE | 067160 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_correct_if_monetization_bridge_required | True | True |
| R8L89_C26_SOOP_2024_STAGE2_ACTIONABLE_PLATFORM_REVENUE_BRIDGE | 067160 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| T_C26_R8L106_01_067160_STAGE2ACTIONABLE_Stage2Actionable_2024-02-01 | 067160 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_too_late_or_data_insufficient | True | True |
| V12_COMPACT_067160_2024-04-01_platform_ad_budget_retention_opm_bridge_cleanup | 067160 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_correct | True | True |
| None | 067160 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | None | False | True |
| C27-R8L105-007|Stage3-Yellow|2024-02-01 | 067160 | C27_CONTENT_IP_GLOBAL_MONETIZATION | residual_error_needs_C27_specific_bridge_or_guard | True | True |
| R13L85_REVIEW_R8_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_067160_2024-01-08 | 067160 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_correct | True | True |
| T_C06_R2L103_067310_20240222_Stage2Actionable_CROSS_C07 | 067310 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_needs_C06_vs_C07_C08_C09_reroute_guard | True | True |
| R2L98_C06_HANAMICRON_2024_STAGE2_FALSE_POSITIVE_OSAT_HBM_CAPA_WATCH | 067310 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_false_positive_if_OSAT_HBM_capacity_watch_counts_without_customer_calloff_utilization_mix_margin_revision_bridge | True | True |
| TRG-C06-L111-067310-Stage3Yellow-2024-04-01 | 067310 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_false_positive | True | True |
| V12_COMPACT_067310_2024-02-22_Stage2-Actionable | 067310 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_false_positive | True | True |
| R2L93_C07_067310_20240327_STAGE2_FALSE_POSITIVE_PACKAGING_CROSSLABEL | 067310 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_false_positive_if_packaging_capacity_price_MFE_counted_as_C07_equipment_order_evidence | True | True |
| TRG_R2L73-C08-067310-HANAMICRON-OSAT-HBM-BETA-WEAK-UTILIZATION | 067310 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | C08 must not allow OSAT/HBM packaging beta to become durable Stage2 without utilization, customer quality, margin, or package mix evidence. Hana Micron generated only small MFE and then severe MAE. | True | True |
| None | 067310 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | False | True |
| TRG_R2L73-C08-067310-HANAMICRON-OSAT-HBM-BETA-WEAK-UTILIZATION | 067310 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | C08 must not allow OSAT/HBM packaging beta to become durable Stage2 without utilization, customer quality, margin, or package mix evidence. Hana Micron generated only small MFE and then severe MAE. | True | True |
| None | 067310 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | False | True |
| HANAMICRON_067310_2024_03_06_STAGE2_FALSE_POSITIVE_OSAT_MEMORY_RECOVERY | 067310 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_false_positive | False | True |
| R9L89_C29_067570_20240206_STAGE2_FALSE_POSITIVE_NVH_REBOUND | 067570 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive_if_NVH_interior_rebound_overcredited | True | True |
| R7L91_C23_067630_20240422_STAGE2_FALSE_POSITIVE_APPROVAL_EXPECTATION_CRL | 067630 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive_if_approval_expectation_overcredited_without_CRL_protection | True | True |
| R7L98_C23_HLBLIFESCI_2024_STAGE4B_ONCOLOGY_APPROVAL_COMMERCIALIZATION_EVENT_CAP | 067630 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_4B_too_late_if_approval_commercialization_event_premium_not_capped | True | True |
| R7L90_C24_HLBBIO_2024_STAGE4B_REGULATORY_TRIAL_EVENT_CAP | 067630 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_4B_too_late_if_regulatory_trial_event_premium_not_capped | True | True |
| C24-R7-L99-TRG-01-067630 | 067630 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_4C_too_early | True | True |
| None | 067630 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| R13L90_REVIEW_R7_C24_BIO_TRIAL_DATA_EVENT_RISK_067630_2024_03_25_TRIGGER | 067630 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_4B_too_late_if_regulatory_trial_event_premium_not_capped | True | True |
| TRG_R8L75-C28-067920-IGLOO-CYBERSECURITY-CONTRACT-RETENTION-BETA-FADE | 067920 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive | True | True |
| V12_COMPACT_C28_R8L104_067920_20240522_067920_2024-05-23_Stage2-Actionable | 067920 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive | True | True |
| TRG_R8L75-C28-067920-IGLOO-CYBERSECURITY-CONTRACT-RETENTION-BETA-FADE | 067920 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | C28 should not treat cybersecurity/SIEM/SOC theme spikes as durable Stage2 unless recurring contract retention, renewal rate, managed security service backlog or margin bridge is visible. IGLOO had a strong early MFE but then faded into high MAE and post-peak drawdown. | True | True |
| R8L89_C28_067920_20240119_STAGE2_FALSE_POSITIVE_SECURITY_THEME | 067920 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive_if_security_theme_spike_overcredited | True | True |
| C27-R8L105-014|Stage2|2024-03-12 | 068050 | C27_CONTENT_IP_GLOBAL_MONETIZATION | residual_error_needs_C27_specific_bridge_or_guard | True | True |
| V12_COMPACT_068270_2024-02-02_BIOSIMILAR_APPROVAL_WITHOUT_INCREMENTAL_REVISION_GUARD | 068270 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive | True | True |
| None | 068270 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | None | True | True |
| C23_R7_L209_T02 | 068270 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_correct | False | True |
| R7L98_C23_CELLTRION_2024_STAGE2_FALSE_POSITIVE_BIOSIMILAR_COMMERCIALIZATION_WATCH | 068270 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive_if_biosimilar_approval_watch_counts_without_sales_channel_pricing_margin_revision_bridge | True | True |
| TRG_R7L73-C23-068270-CELLTRION-ZYMFENTRA-COMMERCIALIZATION-BRIDGE | 068270 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | C23 should reward regulatory approval only when it becomes commercialization evidence: launch, reimbursement access, channel uptake, direct sales or margin bridge. Celltrion has a slower but cleaner large-cap commercialization path with controlled MAE. | True | True |
| TRG_R7L73-C23-068270-CELLTRION-ZYMFENTRA-COMMERCIALIZATION-BRIDGE | 068270 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | C23 should reward regulatory approval only when it becomes commercialization evidence: launch, reimbursement access, channel uptake, direct sales or margin bridge. Celltrion has a slower but cleaner large-cap commercialization path with controlled MAE. | True | True |
| TRG_R7L81-C23-068270-CELLTRION-BIOSIMILAR-COMMERCIALIZATION-POSTCA | 068270 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | C23 should not overblock large-cap biosimilar commercialization rows when MAE is controlled and commercialization/export revenue bridge may be visible. Celltrion requires post-CA and share-count continuity validation because the profile flags a 2024-01-12 corporate-action candidate and the 2024 shard shows share-count changes. | True | True |
| None | 068270 | C24_BIO_TRIAL_DATA_EVENT_RISK | C24 must require fresh binary/data endpoint quality; reroute commercialization, device, reimbursement, or price-only events to C23/C25/local_4B as appropriate. | True | True |
| None | 068270 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | False | True |
| None | 068270 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | None | False | True |
| None | 068270 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| R12L91_C31_068290_20240110_STAGE2_FALSE_POSITIVE_LOWBIRTH_CHILDCARE_POLICY | 068290 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive_if_low_birth_policy_price_MFE_overcredited | True | True |
| C32_068400_SKRENTACAR_20240801_S2A | 068400 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive_if_completion_uncertain | True | True |
| T_R13_STAGE2FP_L5_068400_Stage2Actionable_2024-08-01 | 068400 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_stage2_false_positive_or_overpromotion_risk | True | True |
| R7L89_C23_CELLTRIONPHARM_2024_STAGE4B_BIOSIMILAR_APPROVAL_PREMIUM_CAP | 068760 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_4B_too_late_if_biosimilar_approval_event_premium_not_capped | True | True |
| None | 068760 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | False | True |
| R4L88_C17_TKGHUCHEMS_2024_STAGE2_FALSE_POSITIVE_LOW_BETA_SPREAD | 069260 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive_if_spread_watch_counts_without_margin_revision_bridge | True | True |
| None | 069260 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | True | True |
| TRG_R4L79-C17-069260-TKG-HUCHEMS-NITRIC-ACID-SPREAD-FADE | 069260 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | C17 should not treat nitric-acid/TDI/MNB spread exposure as durable Stage2 unless volume, contract price, utilization, raw-material spread and margin bridge refreshes. TKG Huchems produced tiny MFE and then a persistent drawdown path. | True | True |
| V12_COMPACT_069620_2024-02-02_EXPORT_APPROVAL_WITHOUT_REVISION_GUARD | 069620 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive | True | True |
| None | 069620 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | None | False | True |
| None | 069620 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | None | True | True |
| None | 069620 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | True | True |
| None | 069620 | C24_BIO_TRIAL_DATA_EVENT_RISK | C24 must require fresh binary/data endpoint quality; reroute commercialization, device, reimbursement, or price-only events to C23/C25/local_4B as appropriate. | True | True |
| R5_L122_C18_007 | 069960 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | True | True |
| R5L87_C19_069960_20240129_STAGE2_RETAIL_INVENTORY_MARGIN | 069960 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_correct_if_inventory_margin_bridge_required | True | True |
| C19_R5L120_08_069960_Stage2_Actionable_2024-01-29 | 069960 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | True | True |
| TRG_R5L74-C19-069960-HYUNDAI-DS-VALUEUP-TRAFFIC-MARGIN | 069960 | C19_BRAND_RETAIL_INVENTORY_MARGIN | C19 should allow Stage2 only when low-PBR/value-up retail attention connects to traffic, inventory discipline, duty-free recovery or margin conversion. Hyundai Department Store produced a controlled-MAE positive path, but later drawdown still needs local 4B-watch if the margin bridge stops refreshing. | True | True |
| TRG_R5L74-C19-069960-HYUNDAI-DS-VALUEUP-TRAFFIC-MARGIN | 069960 | C19_BRAND_RETAIL_INVENTORY_MARGIN | C19 should allow Stage2 only when low-PBR/value-up retail attention connects to traffic, inventory discipline, duty-free recovery or margin conversion. Hyundai Department Store produced a controlled-MAE positive path, but later drawdown still needs local 4B-watch if the margin bridge stops refreshing. | True | True |
| V12_COMPACT_C20_R5L120_069960_20240129_02_069960_2024-01-29_Stage2-Actionable | 069960 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | True | True |
| R13L87_REVIEW_R5_C19_BRAND_RETAIL_INVENTORY_MARGIN_069960_2024-01-29 | 069960 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_correct | True | True |
| None | 071050 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | True | True |
| None | 071050 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | True | True |
| V12_COMPACT_071050_2024-05-08_policy_valueup_bank_brokerage_ROE_PBR_capital_return_execution_bridge | 071050 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_correct | True | True |
| C31_R11L106_TRG_09 | 071050 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | None | True | True |
| TRG_R11L76-C31-071090-HISTEEL-EASTSEA-GAS-POLICY-PIPE-BETA-FADE | 071090 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | True | True |
| TRG_R11L76-C31-071090-HISTEEL-EASTSEA-GAS-POLICY-PIPE-BETA-FADE | 071090 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should not treat steel-pipe/resource-policy beta as durable Stage2 unless actual project order, customer, delivery schedule and margin bridge is visible. Hi Steel produced a small MFE and then a large MAE drawdown, making it a policy-proxy local 4B row. | True | True |
| R12L89_C31_DISTRICTHEATING_2024_STAGE2_ACTIONABLE_TARIFF_CASHFLOW_BRIDGE | 071320 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R12L89_C31_071320_20240126_STAGE2_UTILITY_TARIFF_VALUEUP | 071320 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_correct_if_tariff_cost_recovery_capital_return_bridge_required | True | True |
| TRG_R12L79-C31-071320-DISTRICT-HEATING-TARIFF-RECOVERY-BRIDGE | 071320 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should preserve utility tariff normalization positives when policy adjustment maps to cost pass-through, direct earnings recovery, dividend/capital policy and regulatory visibility. Korea District Heating produced very large MFE with controlled entry-basis MAE, but the post-peak drawdown needs lifecycle management. | True | True |
| C01_R1L100_071970_ship_engine_backlog_high_mae_success_T1 | 071970 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_correct_with_high_mae_guardrail_needed | False | True |
| TRG_C01_R1L100_071970_20240424 | 071970 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_correct | False | True |
| None | 073240 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | False | True |
| R9L87_C29_KUMHO_2023_STAGE2_ACTIONABLE_MARGIN_BRIDGE | 073240 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R9L92_C29_KUMHOTIRE_2024_STAGE2_ACTIONABLE_TIRE_VOLUME_MARGIN_BRIDGE | 073240 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R9L86_C29_073240_20240125_STAGE2_TIRE_VOLUME_MARGIN | 073240 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_correct_if_volume_margin_bridge_required | True | True |
| TRG_R9L78-C29-073240-KUMHO-TIRE-OE-REPLACEMENT-MIX-MARGIN | 073240 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should allow tire names when OE/replacement volume, product mix, utilization, raw-material spread and margin bridge are visible. Kumho Tire produced large MFE, but later high MAE and post-peak drawdown require lifecycle local 4B if mix/margin evidence fades. | True | True |
| T_C29_R9L104_073240_STAGE2A_20240411 | 073240 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | True | True |
| T_C29_R9L106_073240_20240430_12_Stage2-Actionable | 073240 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| R13L86_REVIEW_R9_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_073240_2024-01-25 | 073240 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_correct | True | True |
| R13_L106_T11_073240 | 073240 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive_or_4B_too_late | True | True |
| R4L87_C16_073570_20240329_STAGE2_FALSE_POSITIVE_LITHIUM_POLICY | 073570 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_false_positive_if_lithium_policy_theme_overcredited | True | True |
| R13L87_REVIEW_R4_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_073570_2024-03-29 | 073570 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R2L97_C08_WONIKQNC_2024_STAGE2_ACTIONABLE_QUARTZ_CONSUMABLE_CUSTOMER_QUALITY_BRIDGE | 074600 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R2L89_C10_074600_20240607_STAGE2_FALSE_POSITIVE_QUARTZ_MATERIALS_SPIKE | 074600 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_false_positive_if_quartz_materials_spike_overcredited | True | True |
| C28_R8L103_01_075130_Stage2_Actionable_2024-08-01 | 075130 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_missed_structural | True | True |
| R1L116-C01-002 | 075580 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_missed_structural_supplier_bridge_if_supplier_order_conversion_visible | True | True |
| R1L92_C01_SEJINHEAVY_2024_STAGE4B_SHIP_BLOCK_BACKLOG_EVENT_CAP | 075580 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_4B_too_late_if_ship_block_equipment_event_premium_not_capped | True | True |
| R13L92_REVIEW_R1_C01_ORDER_BACKLOG_MARGIN_BRIDGE_075580_2024_07_17_TRIGGER | 075580 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_4B_too_late_if_ship_block_equipment_event_premium_not_capped | True | True |
| R4L95_C16_DONGKUKRNS_2024_STAGE2_FALSE_POSITIVE_RARE_EARTH_POLICY_SUPPLY_WATCH | 075970 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_false_positive_if_rare_earth_policy_watch_counts_without_supply_order_margin_revision_bridge | True | True |
| TRG_R4L78-C16-075970-DONGKUK-RNS-RAREEARTH-REFRACTORY-THEME-FADE | 075970 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | C16 should not treat rare-earth/refractory theme spikes as durable Stage2 unless policy shock maps to direct order, volume, pricing and margin bridge. Dongkuk R&S produced only modest MFE and then a persistent drawdown, making it local 4B-watch rather than durable Green. | True | True |
| R13L95_REVIEW_R4_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_075970_2024_01_23_TRIGGER | 075970 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_rare_earth_policy_watch_counts_without_supply_order_margin_revision_bridge | True | True |
| TRG_R1L83-C01-077970-STX-ENGINE-MARINE-ENGINE-BACKLOG-MARGIN | 077970 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | C01 should protect industrial orderbacklog positives only when customer/program backlog, delivery schedule, revenue recognition and margin bridge are visible. STX Engine produced very large MFE with effectively no entry-basis MAE, but post-peak drawdown still requires lifecycle 4B if order/delivery/margin evidence fades. | True | True |
| TRG_R1L79-C01-077970-STX-ENGINE-ORDER-BACKLOG-DELIVERY-MARGIN | 077970 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | C01 should preserve ship/defense engine suppliers when order backlog, delivery schedule, customer quality, revenue recognition and margin bridge are visible. STX Engine produced high MFE with essentially no entry-basis MAE, but lifecycle local 4B is needed if backlog or margin evidence fades. | True | True |
| TRG_C01_R1L100_077970_20240424 | 077970 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_correct | False | True |
| R1L116-C01-003 | 077970 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_correct_for_engine_supplier_bridge_but_green_requires_margin_revision | True | True |
| T_C03_R1L108_077970_20240612_STAGE2 | 077970 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current profile can over-promote defense beta unless sovereign funded backlog, delivery schedule and margin/cash bridge are verified | True | True |
| R1L94_C03_STXENGINE_2024_STAGE2_ACTIONABLE_NAVAL_ENGINE_EXPORT_BACKLOG_BRIDGE | 077970 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R11L97_C03_STXENGINE_2024_STAGE2_ACTIONABLE_NAVAL_ENGINE_DEFENSE_EXPORT_BACKLOG_DELIVERY_BRIDGE | 077970 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R1L102_C03_STXENGINE_2024_STAGE2_ACTIONABLE_NAVAL_ENGINE_EXPORT_DELIVERY_MARGIN_BRIDGE | 077970 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| None | 077970 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | None | False | True |
| C27-R8L105-008|Stage2|2024-02-15 | 078340 | C27_CONTENT_IP_GLOBAL_MONETIZATION | residual_error_needs_C27_specific_bridge_or_guard | True | True |
| R5L89_C18_ABLECNC_2024_STAGE2_FALSE_POSITIVE_BEAUTY_EXPORT_THEME | 078520 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive_if_beauty_export_theme_counts_without_reorder_margin_revision_bridge | True | True |
| TRG_R3L77-C11-078600-DAEJOO-SILICON-ANODE-ORDERBOOK-MARGIN | 078600 | C11_BATTERY_ORDERBOOK_RERATING | C11 should allow battery-material orderbook Stage2 when a silicon-anode customer ramp, call-off/orderbook, capacity absorption and margin bridge are visible. Daejoo Electronic Materials produced high MFE with almost no entry-basis MAE; post-peak drawdown still requires lifecycle local 4B if orderbook/margin evidence fades. | True | True |
| TRG_R3L77-C11-078600-DAEJOO-SILICON-ANODE-ORDERBOOK-MARGIN | 078600 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_correct | True | True |
| R3L89_C11_DAEJOO_2024_STAGE2_ACTIONABLE_ORDER_REVISION_BRIDGE | 078600 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| T_C11_R3L107_078600_STAGE2ACTIONABLE_20240321 | 078600 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_too_late_if_orderbook_to_margin_bridge_is_confirmed | True | True |
| R3L85_C11_078600_20240321_STAGE2_SILICON_ANODE_ORDERBOOK_BRIDGE | 078600 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_correct_if_customer_capacity_bridge_required | True | True |
| R3L94_C12_DAEJOO_2024_STAGE4B_SILICON_ANODE_CALLOFF_EVENT_CAP | 078600 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_4B_too_late_if_silicon_anode_calloff_event_premium_not_capped | True | True |
| None | 078600 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | True | True |
| T_C13_R3L103_078600_STAGE2ACTIONABLE_20240321 | 078600 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_too_late_when_customer_qualification_to_revenue_bridge_visible | True | True |
| T_C13_R3L104_078600_STAGE3GREEN_20240321 | 078600 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | True | True |
| None | 078600 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | True | True |
| T_C14_R3L108_078600_STAGE3GREEN_20240321 | 078600 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_false_positive | True | True |
| C14-R3L97-06-078600-Stage4B-2024-04-30 | 078600 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_false_positive_if_hard_4c_without_recovery_band | True | True |
| R13L85_REVIEW_R3_C11_BATTERY_ORDERBOOK_RERATING_078600_2024-03-21 | 078600 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_correct | True | True |
| R13_L106_T03_078600 | 078600 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive | True | True |
| R13L94_REVIEW_R3_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_078600_2024_06_12_TRIGGER | 078600 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_4B_too_late_if_silicon_anode_calloff_event_premium_not_capped | True | True |
| T_C06_R2L103_079370_20240201_Stage2_CROSS_C07 | 079370 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_needs_C06_vs_C07_C08_C09_reroute_guard | True | True |
| V12_COMPACT_079370_2024-02-01_Stage2 | 079370 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_false_positive | True | True |
| T_C09_R2L111_09_079370_20240201 | 079370 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_false_positive | True | True |
| R2L93C_C09_079370_20240222_STAGE2_FALSE_POSITIVE_WETCLEAN_CA | 079370 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_false_positive_if_wet_clean_robot_equipment_vocabulary_overcredited | True | True |
| TRG-C09-L115-07-079370-Stage4B-2024-03-15 | 079370 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_false_positive_or_4B_too_late | True | True |
| None | 079370 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | None | True | True |
| T_C01_R1L111_079550_20240214_Stage3-Yellow | 079550 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | strong backlog path, but C01 should defer to C03 when sovereign defense customer quality is the thesis driver | True | True |
| None | 079550 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | True | True |
| R1L99_C03_LIGNEX1_2024_STAGE2_ACTIONABLE_MISSILE_EXPORT_BACKLOG_DELIVERY_MARGIN_BRIDGE | 079550 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| T_079550_20240214_STAGE3G_REPAIR | 079550 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_too_late_if_sovereign_customer_quality_is_not_scored | False | True |
| V12_COMPACT_C03-R1L105-02_079550_2024-03-06_Stage3-Yellow | 079550 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_false_positive | True | True |
| T_C03_R1L107_079550_20240430_STAGE3YELLOW | 079550 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | yellow_valid_but_green_requires_sovereign_customer_funding_and_margin_visibility | True | True |
| T_C03_R1L108_079550_20240517_STAGE3_YELLOW | 079550 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current profile can over-promote defense beta unless sovereign funded backlog, delivery schedule and margin/cash bridge are verified | True | True |
| None | 079550 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | None | False | True |
| T_079550_20240306_STAGE4B_REPAIR | 079550 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_needs_local_4b_vs_green_split | False | True |
| T_C03_R1L107_079550_20241108_STAGE4B | 079550 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | late_leader_chase_should_not_be_green_without_new_contract_or_margin_surprise | True | True |
| T_C03_R1L108_079550_20241108_STAGE4B | 079550 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current profile can over-promote defense beta unless sovereign funded backlog, delivery schedule and margin/cash bridge are verified | True | True |
| None | 079810 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive_if_equipment_orderbook_proxy_promotes_Yellow | True | True |
| R3L96_C11_DENT_2024_STAGE2_FALSE_POSITIVE_BATTERY_EQUIPMENT_ORDERBOOK_WATCH | 079810 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive_if_battery_equipment_orderbook_watch_counts_without_customer_calloff_delivery_margin_revision_bridge | True | True |
| None | 079810 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_4B_too_late_if_orderbook_memory_ignores_local_peak | True | True |
| None | 079810 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_4B_too_late_if_laser_notching_orderbook_memory_ignores_local_peak_and_delivery_acceptance_gap | True | True |
| C13_R3L102_06_079810_20240315_T1 | 079810 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_false_positive | True | True |
| R13L96_REVIEW_R3_C11_BATTERY_ORDERBOOK_RERATING_079810_2024_02_21_TRIGGER | 079810 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_battery_equipment_orderbook_watch_counts_without_customer_calloff_delivery_margin_revision_bridge | True | True |
| R13_CROSS_079940_2024-02-22_Stage2-FalsePositive_/_CloudAIBetaLocal4B | 079940 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive | True | True |
| None | 079940 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | None | True | True |
| TRG_R12L82-C31-080160-MODETOUR-TRAVEL-VISA-REOPENING-FADE | 080160 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should not treat travel-agency reopening theme beta as durable Stage2 unless booking volume, package margin, channel mix, air-seat cost, revenue conversion and margin bridge are visible. Modetour had almost no forward MFE and then severe MAE. | True | True |
| R2L91_C06_JEJUSEMI_2024_STAGE2_FALSE_POSITIVE_ONDEVICE_AI_MEMORY_THEME | 080220 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_false_positive_if_AI_memory_theme_counts_without_HBM_customer_capacity_revision_bridge | True | True |
| R2L97_C06_JEJUSEMI_2024_STAGE4B_EDGE_AI_MEMORY_EVENT_CAP | 080220 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_4B_too_late_if_edge_AI_memory_event_premium_not_capped | True | True |
| R13L91_REVIEW_R2_C06_HBM_MEMORY_CUSTOMER_CAPACITY_080220_2024_01_24_TRIGGER | 080220 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive_if_AI_memory_theme_counts_without_HBM_customer_capacity_revision_bridge | True | True |
| TRG-C06-L111-080580-Stage4B-2024-06-03 | 080580 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_false_positive | True | True |
| None | 080580 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | False | True |
| TRG_R2L81-C08-080580-OKINS-ELECTRONICS-SOCKET-THEME-FADE | 080580 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | C08 should not treat socket/probe/interface theme beta as durable Stage2 unless named customer quality, reorder, utilization, delivery and margin bridge are visible. Okins Electronics had a tradable early MFE, then a severe high-MAE fade. | True | True |
| TRG_R2L78-C08-080580-OKINS-TEST-SOCKET-THEME-FADE | 080580 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | C08 should not treat socket/connector/HBM theme beta as durable Stage2 unless customer qualification, socket reorder, shipment, ASP and margin bridge are visible. Okins Electronics had an early MFE but then opened a severe MAE drawdown path. | True | True |
| R2L92_C08_080580_20240122_STAGE2_FALSE_POSITIVE_TEST_SOCKET_VOLATILITY | 080580 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_false_positive_if_test_socket_theme_volatility_overcredited | True | True |
| R2L96_C08_OKINS_2024_STAGE4B_MEMORY_SOCKET_EVENT_CAP | 080580 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_4B_too_late_if_memory_socket_event_premium_not_capped | True | True |
| R2L92_C08_OKINS_2024_STAGE4B_TEST_SOCKET_EVENT_CAP | 080580 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_4B_too_late_if_test_socket_event_premium_not_capped | True | True |
| None | 080580 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| R13L96_REVIEW_R2_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_080580_2024_01_23_TRIGGER | 080580 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late_if_memory_socket_event_premium_not_capped | True | True |
| None | 080580 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | True | True |
| None | 080580 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | None | True | True |
| R13L92_REVIEW_R2_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_080580_2024_01_23_TRIGGER | 080580 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_4B_too_late_if_test_socket_event_premium_not_capped | True | True |
| TRG_R4L75-C16-081150-TFLEX-RARE-METAL-PROCESSING-SUPPLY-BRIDGE | 081150 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | C16 should allow Stage2 when strategic-resource policy heat connects to real rare-metal processing, customer demand, inventory/supply and margin bridge. T-Flex produced controlled-MAE follow-through and later 2025 highs, but runtime promotion still requires non-proxy customer/supply evidence. | True | True |
| TRG_R4L75-C16-081150-TFLEX-RARE-METAL-PROCESSING-SUPPLY-BRIDGE | 081150 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_correct | True | True |
| R5_L122_C18_006 | 081660 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | True | True |
| None | 081660 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | True | True |
| R5_L122_C18_003 | 081660 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | True | True |
| None | 081660 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | False | True |
| TRG_R5L76-C19-081660-FILA-HOLDINGS-GLOBAL-BRAND-INVENTORY-MARGIN | 081660 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_false_positive | True | True |
| None | 081660 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | True | True |
| R13_CROSS_081660_2024-04-11_Stage2-Actionable-InventoryCleanup | 081660 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_false_positive | True | True |
| TRG_R5L76-C19-081660-FILA-HOLDINGS-GLOBAL-BRAND-INVENTORY-MARGIN | 081660 | C19_BRAND_RETAIL_INVENTORY_MARGIN | C19 should preserve low-MAE global brand rerating candidates when inventory destocking, channel mix, royalty/brand margin and capital return evidence are visible. FILA Holdings had modest MFE but a controlled risk profile; it still needs lifecycle monitoring if inventory/margin evidence fades. | True | True |
| C19_R5L119_03_081660_4B_Local_Watch_2024-02-13 | 081660 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | True | True |
| V12_COMPACT_C20_R5L120_081660_20240401_01_081660_2024-04-01_Stage2-Actionable | 081660 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | True | True |
| TRG_R6L78-C22-082640-TONGYANG-LIFE-HIGHBETA-RESERVE-CAPITAL-RETURN | 082640 | C22_INSURANCE_RATE_CYCLE_RESERVE | C22 can allow high-beta life-insurance positives when reserve quality, rate-cycle leverage, capital buffer and shareholder-return bridge are explicit. Tong Yang Life produced very large MFE with low entry-basis MAE, but the post-peak drawdown shows high beta must be lifecycle-managed. | True | True |
| TRG_R6L82-C22-082640-TONGLIFE-LIFE-INSURANCE-RATE-CYCLE-EVENT-WHIPSAW | 082640 | C22_INSURANCE_RATE_CYCLE_RESERVE | C22 can protect life-insurance positives when CSM/reserve quality, rate-cycle sensitivity, capital return and payout bridge are visible. Tongyang Life had very large MFE but also a violent post-peak whipsaw, so event mechanics and bridge refresh are required. | True | True |
| TRG_C22_R6L104_04 | 082640 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_missed_structural | True | True |
| None | 082640 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | True | True |
| C31_R11L106_TRG_20 | 082640 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | None | True | True |
| TRG_R1L79-C01-082740-HANWHA-ENGINE-SHIP-ENGINE-BACKLOG-MARGIN | 082740 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | C01 should allow industrial ship-engine positives when shipbuilding orderbook maps to engine order backlog, delivery slots, pricing, revenue recognition and margin conversion. Hanwha Engine produced a large MFE, but raw share-count movement inside the window requires validation before runtime promotion. | True | True |
| R1L87_C01_082740_20240314_STAGE2_SHIP_ENGINE_BACKLOG_MARGIN | 082740 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_correct_if_order_backlog_margin_bridge_required | True | True |
| R1L92_C01_HANWHAENGINE_2024_STAGE2_ACTIONABLE_SHIP_ENGINE_ORDER_BACKLOG_MARGIN | 082740 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R1L96_C01_HANWHAENGINE_2024_STAGE2_ACTIONABLE_SHIP_ENGINE_ORDER_BACKLOG_MARGIN_BRIDGE | 082740 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| TRG_R1L83-C01-082740-HANWHA-ENGINE-MARINE-ENGINE-BACKLOG-NAME-SHARECOUNT | 082740 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | C01 can protect marine-engine positives when shipbuilding customer orderbook, delivery schedule, revenue conversion and margin bridge are visible. Hanwha Engine had large MFE and controlled early MAE, but 2024 name/share-count continuity must be validated before runtime promotion. | True | True |
| R13L87_REVIEW_R1_C01_ORDER_BACKLOG_MARGIN_BRIDGE_082740_2024-03-14 | 082740 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_correct | True | True |
| LOTVAC_083310_2024_02_22_STAGE2_FALSE_POSITIVE_VACUUM_EQUIP_SPIKE | 083310 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_false_positive | False | True |
| TRG-C09-L116-04-083310-Stage2-2024-03-15 | 083310 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_false_positive_if_memory_capex_proxy_is_stage2 | True | True |
| LOTVACUUM_083310_2024_02_22_STAGE2_FALSE_POSITIVE_MEMORY_EQUIPMENT_RECOVERY | 083310 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_false_positive | False | True |
| LOTVACUUM_083310_2024_03_06_STAGE2_FALSE_POSITIVE_VACUUM_EQUIPMENT_BETA | 083310 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_false_positive | False | True |
| R2L112-C10-004-T1 | 083310 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_false_positive_if_equipment_label_stays_actionable_after_MAE_break | True | True |
| FNSTECH_083500_2024_03_06_STAGE2A_ADVANCED_CLEAN_PROCESS_EQUIPMENT | 083500 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_4B_too_late | False | True |
| C04_P1_TO50_TRG_11 | 083650 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive | True | True |
| None | 083650 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | None | True | True |
| C04_STATIC_TO50_TRG_04 | 083650 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive | True | True |
| C04_P1_TO50_TRG_12 | 083650 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive | True | True |
| TRG_R11L73-C31-083650-BHI-CZECH-NUCLEAR-EQUIPMENT-DELAYED-BRIDGE | 083650 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should not overblock true nuclear equipment/backlog beneficiaries, but the entry should not be a blind policy-headline chase. BHI had severe early MAE before later rerating; Stage2 requires non-proxy equipment order/backlog evidence and a lifecycle local 4B after peak. | False | True |
| TRG_R11L73-C31-083650-BHI-CZECH-NUCLEAR-EQUIPMENT-DELAYED-BRIDGE | 083650 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should not overblock true nuclear equipment/backlog beneficiaries, but the entry should not be a blind policy-headline chase. BHI had severe early MAE before later rerating; Stage2 requires non-proxy equipment order/backlog evidence and a lifecycle local 4B after peak. | False | True |
| V12_COMPACT_C15-101-04_084010_2024-02-05_Stage2_FalsePositive | 084010 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive | True | True |
| T_C15_R4L103_084010_Stage2_20240205 | 084010 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive_or_wrong_archetype_if_material_label_overweighted | True | True |
| T_C06_R2L103_084370_20240201_Stage2_CROSS_C07 | 084370 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_needs_C06_vs_C07_C08_C09_reroute_guard | True | True |
| V12_COMPACT_084370_2024-02-01_Stage2 | 084370 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_false_positive | True | True |
| TRG_R2L77-C07-084370-EUGENE-TECH-DEPOSITION-EQUIPMENT-RS | 084370 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | C07 should preserve equipment relative-strength rows when customer capex, deposition equipment orders, delivery schedule and margin bridge are visible. Eugene Technology had a controlled-MAE rerating path; later drawdown should be lifecycle-managed, not treated as hard 4C without order or margin break. | True | True |
| TRG_R2L77-C07-084370-EUGENE-TECH-DEPOSITION-EQUIPMENT-RS | 084370 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_correct | True | True |
| R2L91_C07_084370_20240222_STAGE2_HBM_DEPOSITION_EQUIPMENT_ORDER_RAMP | 084370 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_correct_if_HBM_customer_order_delivery_margin_bridge_required | True | True |
| TRG_R2L74-C07-084370-EUGENE-TECH-DEPOSITION-EQUIPMENT-RS | 084370 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | C07 should allow Stage2 when front-end deposition equipment relative strength connects to HBM/DRAM capex, customer order visibility and margin bridge. Eugene Tech produced high MFE with limited entry MAE, but later post-peak drawdown means a lifecycle local 4B guard is needed if order/margin evidence stops refreshing. | True | True |
| TRG_R2L74-C07-084370-EUGENE-TECH-DEPOSITION-EQUIPMENT-RS | 084370 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | C07 should allow Stage2 when front-end deposition equipment relative strength connects to HBM/DRAM capex, customer order visibility and margin bridge. Eugene Tech produced high MFE with limited entry MAE, but later post-peak drawdown means a lifecycle local 4B guard is needed if order/margin evidence stops refreshing. | True | True |
| R2L86_C07_084370_20240528_STAGE2_FALSE_POSITIVE_LATE_EQUIPMENT_EXTENSION | 084370 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_false_positive_if_late_equipment_extension_overcredited | True | True |
| R2_L110_C07 | 084370 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | None | True | True |
| None | 084370 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | False | True |
| None | 084370 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | None | True | True |
| R13_CROSS_084370_2024-02-20_Stage2-Actionable | 084370 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_false_positive | True | True |
| EUGENETECH_084370_2024_03_06_STAGE2A_MEMORY_ALD_RECOVERY | 084370 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_4B_too_late | False | True |
| R2L89_C10_EUGENETECH_2024_STAGE4B_MEMORY_EQUIPMENT_EVENT_CAP | 084370 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_4B_too_late_if_memory_equipment_event_premium_not_capped | True | True |
| R13L86_REVIEW_R2_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_084370_2024-05-28 | 084370 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| V12_COMPACT_084990_2024-02-26_PIPELINE_SURVIVAL_BOUNCE_NOT_COMMERCIALIZATION | 084990 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive | True | True |
| C23_084990_20240202_STAGE2_TRIGGER | 084990 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | None | True | True |
| None | 084990 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | None | True | True |
| None | 084990 | C24_BIO_TRIAL_DATA_EVENT_RISK | C24 must require fresh binary/data endpoint quality; reroute commercialization, device, reimbursement, or price-only events to C23/C25/local_4B as appropriate. | True | True |
| None | 084990 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | False | True |
| C24-R7-L100-TRIG-03-084990 | 084990 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_correct | True | True |
| C24-R7-L99-TRG-02-084990 | 084990 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_false_positive | True | True |
| None | 084990 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | True | True |
| T_C24_R7L105_084990_20240202_STAGE4B | 084990 | C24_BIO_TRIAL_DATA_EVENT_RISK | local_MFE_is_real_but_must_be_capped_to_4B_watch_until_endpoint_and_financing_path_are_validated | True | True |
| R7L96_C24_HELIXMITH_2024_STAGE4B_GENE_THERAPY_TRIAL_EVENT_CAP | 084990 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_4B_too_late_if_gene_therapy_trial_event_premium_not_capped | True | True |
| C24-R7-L100-TRIG-05-084990 | 084990 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_4B_too_late | True | True |
| R13L96_REVIEW_R7_C24_BIO_TRIAL_DATA_EVENT_RISK_084990_2024_02_06_TRIGGER | 084990 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late_if_gene_therapy_trial_event_premium_not_capped | True | True |
| R13_CROSS_084990_2024-02-26_Stage2 | 084990 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | True | True |
| None | 084990 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | True | True |
| R13_CROSS_084990_2024-02-26_Stage2 | 084990 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive | True | True |
| TRG_R6L76-C22-085620-MIRAE-ASSET-LIFE-VALUEUP-BETA-RESERVE-FADE | 085620 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive | True | True |
| None | 085620 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | True | True |
| TRG_R6L74-C22-085620-MIRAE-LIFE-BETA-BRIDGE-FADE | 085620 | C22_INSURANCE_RATE_CYCLE_RESERVE | C22 should not treat life-insurance/value-up beta as durable Stage2 unless CSM quality, reserve sensitivity, K-ICS and capital-return evidence refreshes. Mirae Asset Life had an early MFE but quickly opened 90D MAE and never produced a strong rerating path. | True | True |
| R13_CROSS_085620_2024-02-01_Stage2-FalsePositive_/_LifeInsurerPriceOnlyValueupBeta | 085620 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive | True | True |
| None | 085620 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | True | True |
| R6L91_C22_MIRAEASSETLIFE_2024_STAGE2_ACTIONABLE_RATE_RESERVE_VALUEUP_BRIDGE | 085620 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| TRG_R6L74-C22-085620-MIRAE-LIFE-BETA-BRIDGE-FADE | 085620 | C22_INSURANCE_RATE_CYCLE_RESERVE | C22 should not treat life-insurance/value-up beta as durable Stage2 unless CSM quality, reserve sensitivity, K-ICS and capital-return evidence refreshes. Mirae Asset Life had an early MFE but quickly opened 90D MAE and never produced a strong rerating path. | True | True |
| TRG_R6L78-C22-085620-MIRAEASSET-LIFE-INSURANCE-BETA-FADE | 085620 | C22_INSURANCE_RATE_CYCLE_RESERVE | C22 should not treat life-insurance rate/value-up beta as durable Stage2 unless reserve quality, capital buffer, shareholder return and earnings bridge are visible. Mirae Asset Life had a tradable early MFE, then opened a high-MAE drawdown path. | True | True |
| TRG_R6L82-C22-085620-MIRAE-ASSET-LIFE-RATE-CYCLE-FADE | 085620 | C22_INSURANCE_RATE_CYCLE_RESERVE | C22 should not treat life-insurance value-up/rate-cycle beta as durable Stage2 unless CSM quality, reserve adequacy, payout policy, solvency ratio and ROE bridge are visible. Mirae Asset Life had an early spike and then persistent MAE, so it is a local-4B fade candidate. | True | True |
| TRG_R6L80-C22-085620-MIRAE-ASSET-LIFE-THEME-FADE | 085620 | C22_INSURANCE_RATE_CYCLE_RESERVE | C22 should not treat life-insurance value-up/rate-cycle beta as durable Stage2 unless CSM, reserve quality, capital return, investment spread and earnings bridge are visible. Mirae Asset Life had an initial spike, then a high-MAE fade. | True | True |
| TRG_R6L76-C22-085620-MIRAE-ASSET-LIFE-VALUEUP-BETA-RESERVE-FADE | 085620 | C22_INSURANCE_RATE_CYCLE_RESERVE | C22 should not treat life-insurance value-up beta as durable Stage2 unless CSM/IFRS17 reserve quality, K-ICS buffer, new-business margin, capital return and shareholder-return evidence refreshes. Mirae Asset Life had a tradable spike but then opened high MAE, making it a local 4B row. | True | True |
| None | 085620 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | True | True |
| R6L92_C22_085620_20240205_STAGE2_FALSE_POSITIVE_LIFE_INSURANCE_SPIKE | 085620 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive_if_life_insurance_spike_overcredited | True | True |
| R6L86_C22_085620_20240213_STAGE2_FALSE_POSITIVE_LIFE_INSURANCE_RATE_BETA | 085620 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive_if_rate_beta_overcredited | True | True |
| V12_COMPACT_085620_2024-02-01_policy_valueup_insurance_csm_reserve_capital_return_cash_bridge | 085620 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | True | True |
| R13L86_REVIEW_R6_C22_INSURANCE_RATE_CYCLE_RESERVE_085620_2024-02-13 | 085620 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R7L95_C23_CHABIO_2024_STAGE2_FALSE_POSITIVE_CELL_THERAPY_COMMERCIALIZATION_WATCH | 085660 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive_if_cell_therapy_commercialization_watch_counts_without_regulatory_partner_revenue_margin_revision_bridge | True | True |
| R7L93_C23_085660_20240307_STAGE2_FALSE_POSITIVE_CELL_THERAPY_COMMERCIALIZATION | 085660 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive_if_cell_therapy_commercialization_vocabulary_overcredited | True | True |
| R13L95_REVIEW_R7_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_085660_2024_03_07_TRIGGER | 085660 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_cell_therapy_commercialization_watch_counts_without_regulatory_partner_revenue_margin_revision_bridge | True | True |
| T_C29_R9L106_086280_20240618_15_Stage2 | 086280 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| R9L84_C29_086280_20240819_STAGE2_MOBILITY_LOGISTICS_VOLUME_MIX_BRIDGE | 086280 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_correct_if_volume_mix_bridge_required | True | True |
| TRG_R9L73-C29-086280-GLOVIS-PCC-LOGISTICS-MARGIN-POST-CA | 086280 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should include logistics/PCC/CKD operating leverage when freight rate, capacity and capital-return bridge are visible. Because Hyundai Glovis had 2024 corporate-action candidates, the entry is placed after the 2024-08-02 candidate; the post-CA path is strong but needs source repair. | True | True |
| TRG_R9L73-C29-086280-GLOVIS-PCC-LOGISTICS-MARGIN-POST-CA | 086280 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should include logistics/PCC/CKD operating leverage when freight rate, capacity and capital-return bridge are visible. Because Hyundai Glovis had 2024 corporate-action candidates, the entry is placed after the 2024-08-02 candidate; the post-CA path is strong but needs source repair. | True | True |
| R2L91_C07_086390_20240308_STAGE2_FALSE_POSITIVE_MEMORY_TESTER_THEME | 086390 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_false_positive_if_memory_tester_MFE_overcredited | True | True |
| UNITEST_086390_2024_03_06_STAGE2A_ADVANCED_MEMORY_TEST_EQUIPMENT | 086390 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_4B_too_late | False | True |
| T_C11_R3L107_086520_STAGE4B_20240202 | 086520 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_needs_high_MAE_guard_before_green | True | True |
| R3L93_C13_086520_20240426_STAGE2_FALSE_POSITIVE_AMPC_HOLDCO | 086520 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_false_positive_if_AMPC_holdco_or_cathode_cycle_vocabulary_overcredited | True | True |
| T_C13_R3L104_086520_STAGE3YELLOW_20240202 | 086520 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | True | True |
| T_C13_R3L103_086520_STAGE4B_20240202 | 086520 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_false_positive_if_parent_holdco_AMPC_label_scores_like_direct_cash | True | True |
| T_C14_R3L108_086520_STAGE4B_20240202 | 086520 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_false_positive | True | True |
| R9L93_C14_ECOPRO_2024_STAGE4B_PARENT_EV_DEMAND_SLOWDOWN_EVENT_CAP | 086520 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_4B_too_late_if_parent_battery_EV_demand_slowdown_rebound_premium_not_capped | True | True |
| R13L93_REVIEW_R9_C14_EV_DEMAND_SLOWDOWN_4B_4C_086520_2024_07_08_TRIGGER | 086520 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late_if_parent_battery_EV_demand_slowdown_rebound_premium_not_capped | True | True |
| R1L117-C01-007 | 086670 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_false_positive | False | True |
| V12_COMPACT_C21-HANA-20240201_086790_2024-02-01_Stage2_Actionable_CapitalReturn_ValueUp_Bridge | 086790 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | False | True |
| R6L88_C21_HANAFG_2024_STAGE2_ACTIONABLE_VALUEUP_CAPITAL_RETURN | 086790 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R6L85_C21_086790_20240129_STAGE2_BANK_CAPITAL_RETURN_BRIDGE | 086790 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_correct_if_capital_return_bridge_required | True | True |
| R6L98_C21_HANAFIN_2024_STAGE2_ACTIONABLE_BANK_ROE_PBR_CAPITAL_RETURN_BRIDGE | 086790 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| None | 086790 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | True | True |
| None | 086790 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | False | True |
| None | 086790 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | True | True |
| R12L91_C31_086790_20240129_STAGE2_VALUEUP_POLICY_CAPITAL_RETURN | 086790 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_correct_if_policy_timetable_payout_capital_return_cash_bridge_required | True | True |
| TRIG_C31_R11L100_002_086790 | 086790 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_correct | True | True |
| V12_COMPACT_086790_2024-02-29_policy_valueup_bank_capital_return_cash_bridge | 086790 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_correct | True | True |
| V12_COMPACT_086790_2024-04-26_policy_valueup_bank_brokerage_ROE_PBR_capital_return_execution_bridge | 086790 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_correct | True | True |
| C31_R11L106_TRG_02 | 086790 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | None | True | True |
| None | 086790 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | None | False | True |
| T_C32_R12L106_086790_20240226_Stage3-Yellow | 086790 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | cash return bridge is real, but C21 should own the scoring; C32 only tags governance/value-up contamination | True | True |
| None | 086790 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| None | 086790 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| None | 086790 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| None | 086790 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| None | 086790 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| R13L85_REVIEW_R6_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_086790_2024-01-29 | 086790 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_correct | True | True |
| None | 086790 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | None | True | True |
| R7L89_C23_MEDITOX_2024_STAGE2_FALSE_POSITIVE_REGULATORY_COMMERCIALIZATION | 086900 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive_if_regulatory_or_litigation_theme_counts_without_commercialization_bridge | True | True |
| V12_COMPACT_086900_2024-03-21_REGULATORY_CLEARANCE_EXPORT_REORDER_BRIDGE | 086900 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive | True | True |
| R7L85_C23_086900_20240627_STAGE2_FALSE_POSITIVE_REGULATORY_LEGAL_THEME | 086900 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive_if_regulatory_legal_theme_overcredited | True | True |
| None | 086900 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | False | True |
| R13L85_REVIEW_R7_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_086900_2024-06-27 | 086900 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| T_C21_R6L104_088350_STAGE2_20240201 | 088350 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | True | True |
| None | 088350 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | True | True |
| None | 088350 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | True | True |
| None | 088350 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | True | True |
| R6L41_C22_088350_T1_STAGE2_POLICY_ONLY | 088350 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive | True | True |
| C22-R6-L101-07-T1 | 088350 | C22_INSURANCE_RATE_CYCLE_RESERVE | false_positive_life_rate_beta_without_csm_or_capital_return_bridge | True | True |
| None | 088350 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | False | True |
| R6L89_C22_HANWHALIFE_2024_STAGE2_ACTIONABLE_RATE_VALUEUP_BRIDGE | 088350 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R6L97_C22_HANWHALIFE_2024_STAGE2_FALSE_POSITIVE_LIFE_RATE_SENSITIVITY_RESERVE_WATCH | 088350 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive_if_life_insurer_rate_sensitivity_watch_counts_without_CSM_reserve_capital_return_revision_bridge | True | True |
| None | 088350 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | True | True |
| R6L84_C22_088350_20240205_STAGE2_FALSE_POSITIVE_LIFE_BETA_SPIKE_NO_CSM_RETURN | 088350 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive_if_life_beta_spike_overcredited | True | True |
| R6L90_C22_088350_20240213_STAGE2_FALSE_POSITIVE_LIFE_PRICE_SPIKE | 088350 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive_if_life_insurance_spike_overcredited | True | True |
| None | 088350 | C22_INSURANCE_RATE_CYCLE_RESERVE | Generic life-insurance beta should not become Yellow unless CSM, reserve adequacy, solvency capital, and payout execution are visible. | True | True |
| None | 088350 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | True | True |
| R6L93_C22_HANWHALIFE_2024_STAGE4B_LIFE_INSURANCE_RATE_CYCLE_EVENT_CAP | 088350 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_4B_too_late_if_life_insurance_rate_cycle_event_premium_not_capped | True | True |
| TRG_C22_R6L104_06 | 088350 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive | True | True |
| R6L41_C22_088350_T2_4C_WATCH | 088350 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_4C_too_late | True | True |
| None | 088350 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | False | True |
| V12_COMPACT_088350_2024-02-29_policy_valueup_insurance_csm_reserve_capital_return_cash_bridge | 088350 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | True | True |
| C31_R11L106_TRG_19 | 088350 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | None | True | True |
| TRIG_C31_R11L100_007_088350 | 088350 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | True | True |
| R13L93_REVIEW_R6_C22_INSURANCE_RATE_CYCLE_RESERVE_088350_2024_02_05_TRIGGER | 088350 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late_if_life_insurance_rate_cycle_event_premium_not_capped | True | True |
| TECHWING_089030_2024_03_05_STAGE2A_HBM_TEST_HANDLER_CAPACITY | 089030 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_4B_too_late | False | True |
| TRG_C06_R2_L109_089030_20240322_HBM_TESTER_CAPACITY_PROXY | 089030 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_missed_structural | True | True |
| T_C06_R2L103_089030_20240201_Stage3Yellow_CROSS_C07 | 089030 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_needs_C06_vs_C07_C08_C09_reroute_guard | True | True |
| V12_COMPACT_089030_2024-05-20_C07_HBM_TEST_HANDLER_ORDER_RAMP_RELATIVE_STRENGTH | 089030 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_false_positive | False | True |
| R2L94_C07_TECHWING_2024_STAGE2_ACTIONABLE_HBM_TEST_HANDLER_ORDER_CAPACITY_BRIDGE | 089030 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| TECHWING_089030_2024_02_22_STAGE2A_HBM_TEST_HANDLER_ORDER_RS | 089030 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_4B_too_late | False | True |
| C07_R2L90_089030_20240222_STAGE2A | 089030 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_4B_too_late | True | True |
| V12_COMPACT_089030_2024-02-01_Stage3-Yellow | 089030 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_false_positive | True | True |
| C07_R2L90_089030_20240711_STAGE4B_OVERLAY | 089030 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_4B_too_late | True | True |
| TECHWING_089030_2024_03_06_STAGE2A_MEMORY_TEST_HANDLER_CUSTOMER_QUALITY | 089030 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_4B_too_late | False | True |
| None | 089030 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | False | True |
| R2L93B_C09_089030_20240222_STAGE2_HBM_HANDLER_ORDER | 089030 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_correct_if_order_delivery_revision_margin_cash_bridge_required_but_Green_strict | True | True |
| TRG-C09-L115-02-089030-Stage2Actionable-2024-03-15 | 089030 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_missed_structural_if_forced_into_price_only_blowoff_bucket | True | True |
| T_C09_R2L111_02_089030_20240201 | 089030 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_false_positive | True | True |
| R2L98_C10_TECHWING_2024_STAGE2_ACTIONABLE_HBM_TEST_HANDLER_MEMORY_RECOVERY_BRIDGE | 089030 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| None | 089030 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | None | True | True |
| TRG_R9L81-C29-089590-JEJU-AIR-LCC-PASSENGER-YIELD-FADE | 089590 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should not treat LCC passenger recovery beta as durable Stage2 unless passenger volume, load factor, yield, fuel cost and operating margin bridge are visible. Jeju Air had almost no forward MFE after entry and then a persistent high-MAE path. | True | True |
| None | 089590 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | True | True |
| R13_CROSS_089590_2024-01-05_Stage4B-Local-AirlinePassengerBeta | 089590 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| T_C26_R8L106_02_089600_STAGE2_Stage2_2024-02-15 | 089600 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| R8L92_C26_NASMEDIA_2024_STAGE2_FALSE_POSITIVE_DIGITAL_AD_REP_RECOVERY | 089600 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive_if_digital_ad_recovery_counts_without_traffic_budget_margin_revision_bridge | True | True |
| V12_COMPACT_089600_2024-03-21_platform_ad_budget_retention_opm_bridge_cleanup | 089600 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| None | 089600 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | None | False | True |
| R8L83_C26_089600_20240411_STAGE2_FALSE_POSITIVE_ADTECH_RECOVERY | 089600 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| R8L85_C26_089600_20240124_STAGE2_FALSE_POSITIVE_DIGITAL_AD_BETA | 089600 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive_if_ad_beta_overcredited | True | True |
| R13L83_HIGHMAE_REVIEW_089600_2024-04-11 | 089600 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| R13L85_REVIEW_R8_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_089600_2024-01-24 | 089600 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| R13L92_REVIEW_R8_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_089600_2024_01_24_TRIGGER | 089600 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive_if_digital_ad_recovery_counts_without_traffic_budget_margin_revision_bridge | True | True |
| R2L84_C07_089790_20240328_STAGE2_FALSE_POSITIVE_TEST_HANDLER_NO_ORDER_BRIDGE | 089790 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_false_positive_if_order_bridge_missing | True | True |
| R2L98_C07_JT_2024_STAGE4B_TEST_HANDLER_HBM_EQUIPMENT_EVENT_CAP | 089790 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_4B_too_late_if_test_handler_HBM_equipment_event_premium_not_capped | True | True |
| None | 089790 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | False | True |
| R2L97_C08_JT_2024_STAGE4B_TEST_HANDLER_EVENT_CAP | 089790 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_4B_too_late_if_test_handler_event_premium_not_capped | True | True |
| JT_089790_2024_03_06_STAGE2_FALSE_POSITIVE_ADVANCED_HANDLER_TEST_EQUIPMENT | 089790 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_false_positive | False | True |
| None | 089790 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| None | 089790 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | None | True | True |
| TRG_R9L82-C29-089860-LOTTE-RENTAL-FLEET-UTILIZATION-MARGIN | 089860 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should allow rental/mobility positives only when fleet utilization, used-car residual value, pricing, rental demand, revenue conversion and margin bridge are visible. Lotte Rental produced bounded MAE and later MFE, so it is a protected RiskWatch/Stage2-Yellow candidate after source repair rather than forced 4B. | True | True |
| None | 089860 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | True | True |
| R13_CROSS_089860_2024-02-23_Stage2-Actionable-FleetUtilizationMarginBridge | 089860 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| V12_COMPACT_089890_2024-06-12_C07_LASER_EQUIPMENT_EVENT_SPIKE_NO_ORDER_BRIDGE | 089890 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_false_positive | False | True |
| KOSES_089890_2024_01_24_STAGE2A_ADVANCED_PACKAGING_LASER_EQUIPMENT | 089890 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_4B_too_late | False | True |
| TRG-C09-L116-02-089890-Stage4B-2024-03-15 | 089890 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_4B_too_late_if_equipment_theme_promoted_to_yellow | True | True |
| None | 089890 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | None | True | True |
| None | 089970 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | False | True |
| VM_089970_2024_06_11_STAGE2_FALSE_POSITIVE_ADV_EQUIP_BLOWOFF | 089970 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_false_positive | False | True |
| VM_APTC_089970_2024_03_06_STAGE2A_ADVANCED_ETCH_EQUIPMENT | 089970 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_4B_too_late | False | True |
| None | 089980 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_correct_for_Actionable_but_Yellow_requires_margin_bridge | True | True |
| R3L89_C11_089980_20240522_STAGE2_FALSE_POSITIVE_SEPARATOR_MATERIALS | 089980 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive_if_separator_materials_rebound_overcredited | True | True |
| V12_COMPACT_C12_R3L105_089980_20240430_14_089980_2024-04-30_Stage2 | 089980 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_false_positive | True | True |
| None | 089980 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_broadly_correct_for_Actionable_but_Yellow_requires_customer_conversion_margin_bridge | True | True |
| C13_R3L102_01_089980_20240315_T1 | 089980 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_correct | True | True |
| R3L100-C14-005-T1 | 089980 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_missed_structural_if_generic_EV_slowdown_blocks_verified_recovery_band | True | True |
| R3L91_C14_SANGAFRONTEC_2024_FALSE_4C_EV_MEMBRANE_RECOVERY_RECHECK | 089980 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_false_4C_risk_if_EV_component_slowdown_watch_is_treated_as_thesis_break_without_margin_bridge_failure | True | True |
| R13L91_REVIEW_R3_C14_EV_DEMAND_SLOWDOWN_4B_4C_089980_2024_02_23_TRIGGER | 089980 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_4C_risk_if_EV_component_slowdown_watch_is_treated_as_thesis_break_without_margin_bridge_failure | True | True |
| R9L86_C29_090080_20240202_STAGE2_FALSE_POSITIVE_HYDROGEN_AUTOPARTS | 090080 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive_if_hydrogen_autoparts_theme_overcredited | True | True |
| R13L86_REVIEW_R9_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_090080_2024-02-02 | 090080 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| C19_R5L120_06_090430_Stage2_2024-05-31 | 090430 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | True | True |
| R5L90_C19_090430_20240412_STAGE2_BEAUTY_CHANNEL_MARGIN | 090430 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_correct_if_channel_inventory_sellthrough_margin_bridge_required | True | True |
| None | 090430 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | None | False | True |
| C20_R5L119_090430_20240531_07_Stage2 | 090430 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | None | True | True |
| R5L91_C20_AMOREPACIFIC_2024_STAGE2_ACTIONABLE_KBEAUTY_GLOBAL_CHANNEL_REORDER | 090430 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| None | 090430 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | None | False | True |
| R5L85_C20_090430_20240531_STAGE2_FALSE_POSITIVE_BEAUTY_CHANNEL_SPIKE | 090430 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive_if_channel_spike_overcredited | True | True |
| R5L83_C20_090430_20240531_STAGE2_KBEAUTY_CHINA_REBOUND_FALSE_POSITIVE | 090430 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | True | True |
| R13L85_REVIEW_R5_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_090430_2024-05-31 | 090430 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| T_R13_STAGE2FP_L6_090430_Stage2FalsePositive_2024-05-31 | 090430 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_stage2_false_positive_or_overpromotion_risk | True | True |
| R3L93_C14_091580_20240307_STAGE2_FALSE_POSITIVE_BATTERYCAN_PARTS | 091580 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_false_positive_if_battery_parts_capacity_vocabulary_overcredited_under_EV_slowdown | True | True |
| R3L100-C14-003-T1 | 091580 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_too_late_if_customer_component_label_delays_4C | True | True |
| R10L88_C30_091590_20240102_STAGE2_FALSE_POSITIVE_SMALLCAP_POLICY | 091590 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive_if_smallcap_policy_theme_overcredited | True | True |
| R10L96_C30_NAMHWA_2024_STAGE4B_LOCAL_BUILDER_PF_EVENT_CAP | 091590 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_4B_too_late_if_local_builder_PF_event_premium_not_capped | True | True |
| R13L88_REVIEW_R10_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_091590_2024-01-02 | 091590 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R13L96_REVIEW_R10_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_091590_2024_01_02_TRIGGER | 091590 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late_if_local_builder_PF_event_premium_not_capped | True | True |
| None | 091700 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | False | True |
| TRG_R9L81-C29-091810-TWAY-LCC-ROUTE-YIELD-SHARECOUNT-LIFECYCLE | 091810 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 can allow airline/LCC positives only when passenger volume, route expansion, load factor, yield, fuel-cost sensitivity and margin bridge are visible. T'way produced later MFE but had large interim MAE and stock-web share-count changes, so source repair and share-count validation are mandatory. | True | True |
| TRG_R12L74-C32-091810-TWAY-AIR-CONTROL-PREMIUM-DISPUTE-LIFECYCLE | 091810 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should allow a delayed control-premium dispute candidate when stake accumulation, management-rights pressure and strategic airline-route economics become credible. T'way produced a large MFE into early 2025, but the later collapse requires lifecycle local 4B if control-premium or route/capacity execution evidence fades. | True | True |
| TRG_R12L74-C32-091810-TWAY-AIR-CONTROL-PREMIUM-DISPUTE-LIFECYCLE | 091810 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should allow a delayed control-premium dispute candidate when stake accumulation, management-rights pressure and strategic airline-route economics become credible. T'way produced a large MFE into early 2025, but the later collapse requires lifecycle local 4B if control-premium or route/capacity execution evidence fades. | True | True |
| None | 092070 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | None | True | True |
| R9L97_C29_DIC_2024_STAGE2_FALSE_POSITIVE_EV_REDUCER_EXPORT_VOLUME_WATCH | 092200 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive_if_EV_reducer_export_watch_counts_without_OEM_calloff_mix_utilization_margin_revision_bridge | True | True |
| R9L90_C29_DIC_2024_STAGE2_FALSE_POSITIVE_EV_REDUCER_PARTS_THEME | 092200 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive_if_EV_reducer_parts_theme_counts_without_volume_margin_revision_bridge | True | True |
| R9L88_C29_092200_20240626_STAGE2_FALSE_POSITIVE_EV_DRIVETRAIN_SPIKE | 092200 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive_if_late_EV_drivetrain_spike_overcredited | True | True |
| R13L88_REVIEW_R9_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_092200_2024-06-26 | 092200 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R13L90_REVIEW_R9_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_092200_2024_06_26_TRIGGER | 092200 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive_if_EV_reducer_parts_theme_counts_without_volume_margin_revision_bridge | True | True |
| R9L90_C29_092780_20240422_STAGE2_POWERTRAIN_PISTON_VOLUME | 092780 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_correct_if_OEM_volume_mix_margin_cash_bridge_required | True | True |
| R2L98_C07_EXICON_2024_STAGE2_FALSE_POSITIVE_HBM_TESTER_POST_CA_RS_WATCH | 092870 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_false_positive_if_HBM_tester_RS_watch_counts_without_customer_order_qualification_utilization_margin_revision_bridge | True | True |
| R2L84_C07_092870_20240926_STAGE2_FALSE_POSITIVE_HBM_TESTER_REBOUND | 092870 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_false_positive_if_relative_strength_overcredited | True | True |
| C08_R2_L112_003_092870_Stage2_Actionable | 092870 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_missed_structural | True | True |
| R2L92_C08_092870_20240228_STAGE2_MEMORY_TESTER_CUSTOMER_QUALITY | 092870 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_correct_if_customer_qualification_order_delivery_margin_cash_bridge_required_and_data_quality_repaired | True | True |
| TRG_R2L73-C08-092870-EXICON-HBM-TESTER-POST-CA-ADOPTION-BRIDGE | 092870 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | C08 can permit Stage2 when tester demand is tied to verified customer adoption/reorder and the entry window is after corporate-action contamination. Exicon's post-CA path had strong MFE with controlled MAE, but source repair is required before runtime promotion. | True | True |
| TRG_R2L73-C08-092870-EXICON-HBM-TESTER-POST-CA-ADOPTION-BRIDGE | 092870 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | C08 can permit Stage2 when tester demand is tied to verified customer adoption/reorder and the entry window is after corporate-action contamination. Exicon's post-CA path had strong MFE with controlled MAE, but source repair is required before runtime promotion. | True | True |
| None | 092870 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | False | True |
| None | 092870 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | False | True |
| None | 092870 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | None | True | True |
| None | 093050 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | True | True |
| R5_L122_C18_001 | 093050 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | True | True |
| None | 093050 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | False | True |
| TRG_R5L76-C19-093050-LF-APPAREL-BRAND-INVENTORY-MARGIN-RECOVERY | 093050 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_false_positive | True | True |
| LF_093050_2024_03_07_STAGE2A_APPAREL_INVENTORY_MARGIN_STABLE | 093050 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_correct | False | True |
| C19_R5L119_01_093050_Stage2_Actionable_2024-03-27 | 093050 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | True | True |
| 093050_2024-11-15_Stage2_Actionable_C19_RETAIL_BRAND_INVENTORY_CLEAN_VALUE_POSITIVE | 093050 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_correct | False | True |
| TRG_R5L76-C19-093050-LF-APPAREL-BRAND-INVENTORY-MARGIN-RECOVERY | 093050 | C19_BRAND_RETAIL_INVENTORY_MARGIN | C19 should allow slow brand/retail positives when inventory normalization, DTC/channel mix, markdown control and margin bridge are visible. LF produced a moderate MFE with controlled MAE; not explosive, but useful to avoid overfitting C19 only to high-beta consumer names. | True | True |
| V12_COMPACT_C20_R5L120_093050_20240327_08_093050_2024-03-27_Stage2-Actionable | 093050 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | True | True |
| R3L95_C13_FOOSUNG_2024_STAGE2_FALSE_POSITIVE_ELECTROLYTE_FLUOROCHEM_AMPC_WATCH | 093370 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_false_positive_if_electrolyte_fluorochem_AMPC_watch_counts_without_utilization_margin_revision_bridge | True | True |
| R3L88_C14_093370_20240126_4B_ELECTROLYTE_DEMAND_SLOWDOWN | 093370 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_correct_if_C14_blocks_Yellow_Green_under_demand_slowdown | True | True |
| T_C15_R4L105_093370_20240321_06_Stage2 | 093370 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive | True | True |
| FOOSUNG_093370_2024_02_15_STAGE2_FALSE_POSITIVE_FLUOROCHEMICAL_SPREAD | 093370 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive | False | True |
| T_C17_R4L105_02_093370_Stage2_20240321 | 093370 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive | True | True |
| None | 093370 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | True | True |
| R13L88_REVIEW_R3_C14_EV_DEMAND_SLOWDOWN_4B_4C_093370_2024-01-26 | 093370 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_correct | True | True |
| R13L95_REVIEW_R3_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_093370_2024_02_13_TRIGGER | 093370 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_electrolyte_fluorochem_AMPC_watch_counts_without_utilization_margin_revision_bridge | True | True |
| T_R13_STAGE2FP_L6_093370_Stage2_2024-03-21 | 093370 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_stage2_false_positive_or_overpromotion_risk | True | True |
| None | 093370 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | None | True | True |
| TRG_R8L82-C28-094280-HYOSUNG-ITX-ITOUTSOURCING-CONTRACT-RETENTION-BOUNDED | 094280 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | C28 should allow software/IT service positives only when recurring contract retention, renewal, managed-service orderbook, revenue conversion and margin bridge are visible. Hyosung ITX had bounded MAE and later MFE, so it is a RiskWatch/Stage2-Yellow candidate after source repair rather than a forced 4B row. | True | True |
| R12L97_C31_GALAXIAMONEYTREE_2024_STAGE4B_STO_DIGITAL_ASSET_LEGISLATION_EVENT_CAP | 094480 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_4B_too_late_if_STO_digital_asset_legislation_event_premium_not_capped | True | True |
| C04_P1_TO50_TRG_13 | 094820 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive | True | True |
| C04_STATIC_TO50_TRG_06 | 094820 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive | True | True |
| C04_P1_TO50_TRG_14 | 094820 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive | True | True |
| R11L87_C04_094820_20240318_STAGE2_FALSE_POSITIVE_NUCLEAR_MAINTENANCE_THEME | 094820 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive_if_maintenance_theme_promoted_without_confirmed_project_scope | True | True |
| R1L85_C04_094820_20240405_STAGE2_FALSE_POSITIVE_NUCLEAR_MAINTENANCE_THEME | 094820 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive_if_service_theme_overcredited | True | True |
| R1L90_C04_ILJINPOWER_2024_STAGE4B_NUCLEAR_MAINTENANCE_THEME_CAP | 094820 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_4B_too_late_if_nuclear_maintenance_theme_premium_not_capped | True | True |
| None | 094820 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | None | True | True |
| R1L93_C05_ILJINPOWER_2024_STAGE4B_POWER_PLANT_SERVICE_EPC_EVENT_CAP | 094820 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | current_profile_4B_too_late_if_power_plant_service_EPC_event_premium_not_capped | True | True |
| R13L87_REVIEW_R11_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_094820_2024-03-18 | 094820 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R13L93_REVIEW_R1_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_094820_2024_05_27_TRIGGER | 094820 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late_if_power_plant_service_EPC_event_premium_not_capped | True | True |
| R13L85_REVIEW_R1_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_094820_2024-04-05 | 094820 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| R13L90_REVIEW_R1_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_094820_2024_04_05_TRIGGER | 094820 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_4B_too_late_if_nuclear_maintenance_theme_premium_not_capped | True | True |
| None | 095190 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | None | False | True |
| R11L90_C03_095190_20240215_STAGE2_FALSE_POSITIVE_DUALUSE_MACHINING | 095190 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_false_positive_if_dualuse_machining_MFE_overcredited | True | True |
| ISC_095340_2024_03_08_STAGE2_FALSE_POSITIVE_HBM_SOCKET_CAPACITY | 095340 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_false_positive | False | True |
| TRG-C06-L110-095340-Stage3Yellow-2024-04-01 | 095340 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_false_positive | True | True |
| C08_R2L97_095340_STAGE2A_20240215_CUSTOMER_QUALITY_SOCKET_BRIDGE | 095340 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_too_late | True | True |
| ISC_095340_2024_02_22_STAGE2A_SOCKET_QUALIFICATION | 095340 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_4B_too_late | False | True |
| ISC_095340_2024_03_06_STAGE2A_TEST_SOCKET_CUSTOMER_QUALITY | 095340 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_4B_too_late | False | True |
| C08_R2_L112_002_095340_Stage2_Actionable | 095340 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_too_late | True | True |
| None | 095340 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | False | True |
| R2L93_C08_095340_20240308_STAGE2_FALSE_POSITIVE_SOCKET_MFE_DECAY | 095340 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_false_positive_if_test_socket_price_MFE_overcredited | True | True |
| None | 095340 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | False | True |
| C08_095340_2024_03_28_TEST_SOCKET_BLOWOFF_4B_GUARD_Stage4B | 095340 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_4B_too_late | False | True |
| TRG_C09_R2L98_ISC_20240328_4B_BLOWOFF_GUARD | 095340 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_correct | False | True |
| None | 095340 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| None | 095340 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| None | 095340 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | True | True |
| None | 095340 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | None | True | True |
| None | 095340 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | None | True | True |
| TRG_C11_R3L105_003 | 095500 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive | True | True |
| R3L91_C13_095500_20240229_STAGE2_FALSE_POSITIVE_LITHIUM_IRA_VOCABULARY | 095500 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_false_positive_if_lithium_IRA_vocabulary_overcredited | True | True |
| R3L98-C14-002-T1 | 095500 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_too_conservative_if_generic_EV_slowdown_blocks_recovery_band_exception | True | True |
| T_C06_R2L103_095610_20240215_Stage2_CROSS_C07 | 095610 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_needs_C06_vs_C07_C08_C09_reroute_guard | True | True |
| V12_COMPACT_095610_2024-02-15_Stage2 | 095610 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_false_positive | True | True |
| TRG_R2L74-C07-095610-TES-HBM-EQUIPMENT-BETA-BRIDGE-FADE | 095610 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | C07 should not treat a one-month equipment beta spike as durable Stage2 unless named customer order, HBM-related capex, backlog or margin bridge refreshes. TES had strong initial MFE but later opened severe MAE and drawdown, making it a local 4B-watch / false Stage2 row. | True | True |
| R2_L110_C07 | 095610 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | None | True | True |
| TRG_R2L74-C07-095610-TES-HBM-EQUIPMENT-BETA-BRIDGE-FADE | 095610 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | C07 should not treat a one-month equipment beta spike as durable Stage2 unless named customer order, HBM-related capex, backlog or margin bridge refreshes. TES had strong initial MFE but later opened severe MAE and drawdown, making it a local 4B-watch / false Stage2 row. | True | True |
| T_C09_R2L111_10_095610_20240215 | 095610 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_false_positive | True | True |
| TES_095610_2024_03_06_STAGE2A_MEMORY_EQUIPMENT_RECOVERY | 095610 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_4B_too_late | False | True |
| R2L89_C10_TES_2024_STAGE2_FALSE_POSITIVE_DEPOSITION_THEME | 095610 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_false_positive_if_deposition_equipment_theme_counts_without_customer_order_revision_bridge | True | True |
| R2L98_C10_TES_2024_STAGE4B_CVD_MEMORY_RECOVERY_EQUIPMENT_EVENT_CAP | 095610 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_4B_too_late_if_CVD_memory_recovery_equipment_event_premium_not_capped | True | True |
| V12_COMPACT_C27-R8-L101-003_095660_2024-02-02_single_title_global_console_ip_label_without_new_monetization_bridge | 095660 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_false_positive | True | True |
| TRG_R8L78-C27-095660-NEOWIZ-GAME-IP-THEME-FADE | 095660 | C27_CONTENT_IP_GLOBAL_MONETIZATION | C27 should not treat game-IP or PC/console title beta as durable Stage2 unless user retention, live-ops, revenue rank, content pipeline and margin bridge are visible. Neowiz had a brief MFE and then a large drawdown, making it a local 4B-watch boundary rather than durable Green. | True | True |
| R7L88_C23_095700_20240318_STAGE2_FALSE_POSITIVE_PLATFORM_THEME | 095700 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive_if_platform_clinical_theme_overcredited | True | True |
| R7L84_C24_095700_20240318_STAGE2_FALSE_POSITIVE_TRIAL_REBOUND_NO_DATA_BRIDGE | 095700 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_false_positive_if_trial_theme_overcredited | True | True |
| C24-R7-L99-TRG-03-095700 | 095700 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_false_positive | True | True |
| R13L88_REVIEW_R7_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_095700_2024-03-18 | 095700 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| TRG_R12L80-C31-095720-WOONGJIN-THINKBIG-EDTECH-POLICY-FADE | 095720 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should not treat education/AI textbook policy beta as durable Stage2 unless direct beneficiary mapping, procurement timing, paid user conversion, revenue and margin bridge are visible. Woongjin Thinkbig had a small policy MFE and then a deep MAE path. | True | True |
| R1L92_C01_DAECHANGSOL_2024_STAGE2_FALSE_POSITIVE_LNG_EQUIPMENT_THEME | 096350 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_false_positive_if_LNG_ship_equipment_theme_counts_without_order_backlog_margin_bridge | True | True |
| R13L92_REVIEW_R1_C01_ORDER_BACKLOG_MARGIN_BRIDGE_096350_2024_02_23_TRIGGER | 096350 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive_if_LNG_ship_equipment_theme_counts_without_order_backlog_margin_bridge | True | True |
| T_C11_R3L107_096770_STAGE2ACTIONABLE_20240129 | 096770 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive_if_orderbook_label_is_overcredited | True | True |
| None | 096770 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | True | True |
| R3L87_C13_096770_20240122_STAGE2_JV_AMPC_UTILIZATION | 096770 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_correct_if_JV_AMPC_utilization_bridge_required | True | True |
| T_C13_R3L105_096770_STAGE2ACTIONABLE_20240129 | 096770 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | True | True |
| V12_COMPACT_C13-102-03_096770_2024-01-31_Stage2-Actionable | 096770 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_false_positive | True | True |
| None | 096770 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | True | True |
| R9L93_C14_SKINNOVATION_2024_STAGE2_ACTIONABLE_INTEGRATED_BATTERY_REFINING_FUNDING_BRIDGE | 096770 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R3L100-C14-002-T1 | 096770 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_false_positive_if_integrated_refining_cashflow_masks_battery_demand_reset | True | True |
| C14-R3L97-04-096770-Stage4C-2025-01-31 | 096770 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_correct_but_requires_post_corporate_action_entry | True | True |
| R13L87_REVIEW_R3_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_096770_2024-01-22 | 096770 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_correct | True | True |
| R13L93_REVIEW_R9_C14_EV_DEMAND_SLOWDOWN_4B_4C_096770_2024_01_24_TRIGGER | 096770 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| TRG_R1L73-C01-097230-HJSC-ORDER_BETA_WEAK_MARGIN_CONVERSION | 097230 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | C01 should not treat shipbuilding/construction order beta as Stage2 unless backlog quality and margin conversion are explicit. HJ Heavy produced a short MFE but later opened drawdown, making it a false Stage2 / local 4B-watch candidate. | True | True |
| TRG_R1L73-C01-097230-HJSC-ORDER_BETA_WEAK_MARGIN_CONVERSION | 097230 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | C01 should not treat shipbuilding/construction order beta as Stage2 unless backlog quality and margin conversion are explicit. HJ Heavy produced a short MFE but later opened drawdown, making it a false Stage2 / local 4B-watch candidate. | True | True |
| R1L87_C01_097230_20240207_STAGE2_FALSE_POSITIVE_SHIPBUILDING_BACKLOG | 097230 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_false_positive_if_backlog_theme_overcredited | True | True |
| R1L93_C01_097230_20240102_STAGE2_FALSE_POSITIVE_WEAK_BACKLOG_LATE_SPIKE | 097230 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_false_positive_if_late_spike_validates_original_weak_backlog_entry | True | True |
| R1L116-C01-004 | 097230 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_correct_but_position_size_high_MFE_outlier_guard_needed | True | True |
| R10L97_C30_HJSC_2024_STAGE2_ACTIONABLE_HEAVY_CIVIL_INFRA_ORDER_CASHFLOW_BRIDGE | 097230 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R13L87_REVIEW_R1_C01_ORDER_BACKLOG_MARGIN_BRIDGE_097230_2024-02-07 | 097230 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| TRG_R5L77-C18-097950-CJ-CHEILJEDANG-KFOOD-CHANNEL-MARGIN-LIFECYCLE | 097950 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | True | True |
| None | 097950 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | True | True |
| TRG_R5L79-C18-097950-CJ-CHEILJEDANG-KFOOD-GLOBAL-CHANNEL-REORDER | 097950 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | C18 should allow K-food/global food positives when overseas channel reorder, distribution expansion, volume growth, price/mix and margin bridge are visible. CJ CheilJedang produced strong MFE with bounded entry-basis MAE, but later drawdown means channel/revenue/margin evidence must refresh. | True | True |
| TRG_R5L77-C18-097950-CJ-CHEILJEDANG-KFOOD-CHANNEL-MARGIN-LIFECYCLE | 097950 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | C18 should preserve large-cap food export/channel positives when global channel reorder, product mix, price-cost spread and margin bridge are visible. CJ CheilJedang produced moderate MFE with controlled MAE, then faded; it should be lifecycle-managed rather than treated as permanent Green. | True | True |
| R5L91_C20_CJFOOD_2024_STAGE4B_GLOBAL_FOOD_MARGIN_DISTRIBUTION_CAP | 097950 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_4B_too_late_if_global_food_margin_distribution_premium_not_capped | True | True |
| R13L91_REVIEW_R5_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_097950_2024_06_26_TRIGGER | 097950 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_4B_too_late_if_global_food_margin_distribution_premium_not_capped | True | True |
| R2L92_C08_MICROCONTACT_2024_STAGE2_FALSE_POSITIVE_SOCKET_THEME | 098120 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_false_positive_if_socket_theme_counts_without_customer_quality_margin_revision_bridge | True | True |
| R2L96_C08_MICONSO_2024_STAGE2_FALSE_POSITIVE_TEST_SOCKET_CHANNEL_WATCH | 098120 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_false_positive_if_test_socket_channel_watch_counts_without_customer_order_ASP_margin_revision_bridge | True | True |
| None | 098120 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | False | True |
| TRG_R2L78-C08-098120-MICROCONTACTSOL-IC-SOCKET-CUSTOMER-QUALITY-FADE | 098120 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | C08 should not treat IC-socket/test-parts exposure as durable Stage2 unless customer quality, socket demand, order visibility and margin bridge refreshes. Micro Contact Solution had limited MFE and then a large MAE drawdown. | True | True |
| TRG_R2L81-C08-098120-MICROCONTACTSOL-TEST-SOCKET-THEME-FADE | 098120 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | C08 should not treat IC/test-socket theme beta as durable Stage2 unless customer quality, reorder cadence, delivery/revenue and margin bridge are visible. Micro Contact Solution had only small early MFE and then severe MAE. | True | True |
| R2L87_C08_098120_20240429_STAGE2_FALSE_POSITIVE_SOCKET_THEME_REBOUND | 098120 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_false_positive_if_socket_theme_rebound_overcredited | True | True |
| R13L87_REVIEW_R2_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_098120_2024-04-29 | 098120 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R13L96_REVIEW_R2_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_098120_2024_04_24_TRIGGER | 098120 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_test_socket_channel_watch_counts_without_customer_order_ASP_margin_revision_bridge | True | True |
| R13L92_REVIEW_R2_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_098120_2024_03_08_TRIGGER | 098120 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive_if_socket_theme_counts_without_customer_quality_margin_revision_bridge | True | True |
| TRG-C09-L116-05-098460-Stage2Actionable-2024-06-17 | 098460 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_too_conservative_if_inspection_recovery_is_forced_to_4B_after_drawdown | True | True |
| R2L112-C10-002-T1 | 098460 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_correct_on_stage2_but_green_requires_memory_order_bridge_filter | True | True |
| None | 099190 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | True | True |
| None | 099190 | C24_BIO_TRIAL_DATA_EVENT_RISK | C24 must require fresh binary/data endpoint quality; reroute commercialization, device, reimbursement, or price-only events to C23/C25/local_4B as appropriate. | True | True |
| TRG_R7L75-C25-099190-ISENS-CGM-REIMBURSEMENT-ADOPTION-BETA-FADE | 099190 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive | True | True |
| TRG_R7L77-C25-099190-ISENS-CGM-REIMBURSEMENT-EXPORT-BETA-FADE | 099190 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive | True | True |
| R13_CROSS_099190_2024-02-01_Stage2-FalsePositive_/_CGMReimbursementLaunchBeta | 099190 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive | True | True |
| V12_COMPACT_C25_R7L107_099190_20240517_Stage2_Actionable_099190_2024-05-17_Stage2-Actionable | 099190 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive | True | True |
| None | 099190 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | None | True | True |
| TRG_R7L75-C25-099190-ISENS-CGM-REIMBURSEMENT-ADOPTION-BETA-FADE | 099190 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | C25 should not treat CGM/reimbursement or launch attention as durable Stage2 unless adoption, prescription refill, reimbursement coverage, utilization and margin evidence refreshes. i-SENS had only small initial MFE and then severe MAE/drawdown. | True | True |
| TRG_R7L77-C25-099190-ISENS-CGM-REIMBURSEMENT-EXPORT-BETA-FADE | 099190 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | C25 should not treat CGM/reimbursement or diabetes-device theme beta as durable Stage2 unless adoption, reimbursement coverage, distributor sell-through, export reorder and margin bridge are visible. i-SENS had only a small early MFE and then a high-MAE drawdown path. | True | True |
| TRG_R7L79-C25-099190-ISENS-CGM-REIMBURSEMENT-EXPORT-THEME-FADE | 099190 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | C25 should not treat CGM reimbursement/export theme beta as durable Stage2 unless reimbursement coverage, prescription/adoption, distributor revenue, recurring consumables and margin bridge are visible. i-SENS produced only small early MFE and then a deep MAE path. | True | True |
| None | 099190 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | None | True | True |
| R7L83_C25_099190_20240110_STAGE2_FALSE_POSITIVE_CGM_REIMBURSEMENT | 099190 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive | True | True |
| R7L92_C25_099190_20240111_STAGE2_FALSE_POSITIVE_CGM_REIMBURSEMENT | 099190 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive_if_CGM_reimbursement_vocabulary_overcredited | True | True |
| R13_L106_T19_099190 | 099190 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive | True | True |
| T_C03_R1L107_099320_20240312_STAGE2 | 099320 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | space_defense_label_has_optional_value_but_sovereign_order_bridge_missing | True | True |
| T_C03_R1L108_099320_20240411_STAGE2 | 099320 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current profile can over-promote defense beta unless sovereign funded backlog, delivery schedule and margin/cash bridge are verified | True | True |
| None | 099320 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | None | False | True |
| R1L89_C03_099320_20240424_STAGE2_FALSE_POSITIVE_SPACE_DEFENSE_THEME | 099320 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_false_positive_if_space_defense_theme_overcredited | True | True |
| R11L84_C03_099320_20240701_STAGE2_FALSE_POSITIVE_SPACE_DEFENSE_THEME | 099320 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_false_positive_if_space_defense_theme_overcredited | True | True |
| R11L89_C03_SATRECINITIATIVE_2024_STAGE4B_SPACE_DEFENSE_THEME_CAP | 099320 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_4B_too_late_if_space_defense_theme_premium_not_capped | True | True |
| R13L89_REVIEW_C03_SATREC_2024_STAGE4B_SPACE_DEFENSE_THEME_CAP | 099320 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_4B_too_late_if_space_defense_theme_premium_not_capped | True | True |
| V12_COMPACT_C28_R8L104_099390_20240612_099390_2024-06-13_Stage2-Actionable | 099390 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive | True | True |
| V12_COMPACT_R13_STAGE2FP_L8_17_099390_2024-06-13_STAGE2ACTIONABLE_099390_2024-06-13_stage2_source_proxy_deep_MAE_false_positive_review | 099390 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive | True | True |
| TRG_R1L77-C01-100090-SK-OCEANPLANT-OFFSHORE-ORDERBOOK-BETA-FADE | 100090 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_false_positive | True | True |
| TRG_R1L77-C01-100090-SK-OCEANPLANT-OFFSHORE-ORDERBOOK-BETA-FADE | 100090 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | C01 should not treat offshore plant / orderbook beta as durable Stage2 unless project award, backlog conversion, delivery schedule, utilization and margin bridge are visible. SK Oceanplant had only small MFE and then a large MAE drawdown, making it local 4B-watch rather than a backlog Green. | True | True |
| None | 100120 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | True | True |
| None | 100120 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | None | True | True |
| V12_COMPACT_C25_R7L107_100120_20240826_Stage3_Yellow_100120_2024-08-26_Stage3-Yellow | 100120 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive | True | True |
| R12L89_C31_VISANG_2024_STAGE2_FALSE_POSITIVE_EDUCATION_POLICY_THEME | 100220 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive_if_education_policy_theme_counts_without_revenue_contract_or_subsidy_bridge | True | True |
| R13L89_REVIEW_C31_VISANG_2024_STAGE2_FALSE_POSITIVE_EDUCATION_POLICY_THEME | 100220 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive_if_education_policy_theme_counts_without_revenue_contract_or_subsidy_bridge | True | True |
| R1L117-C01-003 | 100840 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_missed_structural | False | True |
| R1L117-C01-003 | 100840 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_missed_structural | True | True |
| R1L91_C05_100840_20240603_STAGE2_ENERGY_EQUIPMENT_BACKLOG_MARGIN | 100840 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | current_profile_correct_if_order_backlog_delivery_margin_cash_bridge_required | True | True |
| R1L97_C05_SNTENERGY_2024_STAGE2_ACTIONABLE_HEAT_EXCHANGER_PLANT_EPC_ORDER_MARGIN_BRIDGE | 100840 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R1L93_C05_SNTENERGY_2024_STAGE2_ACTIONABLE_PLANT_EPC_EXPORT_ORDER_MARGIN_BRIDGE | 100840 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R2L97_C08_WORLDEX_2024_STAGE2_FALSE_POSITIVE_SILICON_PARTS_CUSTOMER_QUALITY_WATCH | 101160 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_false_positive_if_silicon_parts_quality_watch_counts_without_customer_qualification_reorder_utilization_margin_revision_bridge | True | True |
| R2L93_C10_101160_20240102_STAGE2_FALSE_POSITIVE_PARTS_RECOVERY_DECAY | 101160 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_false_positive_if_parts_recovery_vocabulary_overcredited | True | True |
| R1L96_C01_WOORIMPTS_2024_STAGE4B_INDUSTRIAL_GEAR_ORDER_EVENT_CAP | 101170 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_4B_too_late_if_industrial_gear_order_event_premium_not_capped | True | True |
| R13L96_REVIEW_R1_C01_ORDER_BACKLOG_MARGIN_BRIDGE_101170_2024_06_07_TRIGGER | 101170 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late_if_industrial_gear_order_event_premium_not_capped | True | True |
| R3L99-C14-003-T1 | 101360 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_too_conservative_if_generic_EV_slowdown_blocks_verified_recovery_band | True | True |
| R3L92_C14_101360_20240111_STAGE2_FALSE_OVERBLOCK_PRECURSOR_RAMP | 101360 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_false_positive_if_EV_slowdown_guard_ignores_customer_capacity_ramp_bridge | True | True |
| T_C06_R2L103_101490_20240306_Stage4B_CROSS_C07 | 101490 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_needs_C06_vs_C07_C08_C09_reroute_guard | True | True |
| V12_COMPACT_101490_2024-03-06_Stage4B | 101490 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_false_positive | True | True |
| None | 101490 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | False | True |
| SNSTECH_101490_2024_03_06_STAGE2_FALSE_POSITIVE_ADVANCED_MASK_PREMIUM | 101490 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_false_positive | False | True |
| TRG-C09-L115-06-101490-Stage2-2024-03-15 | 101490 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_false_positive_if_technology_scarcity_promoted | True | True |
| R2L93B_C09_101490_20240228_STAGE2_FALSE_POSITIVE_MASKBLANK_DECAY | 101490 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_false_positive_if_maskblank_EUV_vocabulary_overcredited | True | True |
| T_C09_R2L111_07_101490_20240306 | 101490 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_false_positive | True | True |
| R2L88_C09_SNSTECH_2024_STAGE4B_EUV_MASK_VALUATION_EVENT_CAP | 101490 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_4B_too_late_if_EUV_mask_premium_not_capped | True | True |
| R5L94_C18_HAITAI_2024_STAGE2_FALSE_POSITIVE_SNACK_RETAIL_EXPORT_THEME | 101530 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive_if_snack_retail_export_theme_counts_without_reorder_channel_margin_revision_bridge | True | True |
| R5L89_C18_101530_20240614_STAGE2_FALSE_POSITIVE_SNACK_LATE_THEME | 101530 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive_if_snack_theme_spike_overcredited | True | True |
| R13L94_REVIEW_R5_C18_CONSUMER_EXPORT_CHANNEL_REORDER_101530_2024_02_01_TRIGGER | 101530 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive_if_snack_retail_export_theme_counts_without_reorder_channel_margin_revision_bridge | True | True |
| None | 102120 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | False | True |
| None | 102260 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | True | True |
| C03_R1L111_003_TRIGGER | 103140 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_false_positive | True | True |
| None | 103140 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | None | False | True |
| TRG_R1L82-C03-103140-POONGSAN-AMMO-EXPORT-BACKLOG-MARGIN | 103140 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | C03 should protect defense/ammunition positives only when export backlog, customer country/program, delivery schedule, metal spread, revenue recognition and margin bridge are visible. Poongsan produced a very large MFE with shallow entry-basis MAE, but post-peak drawdown requires lifecycle 4B if backlog/margin evidence fades. | True | True |
| TRG_R11L79-C03-103140-POONGSAN-AMMO-EXPORT-DEMAND-BACKLOG | 103140 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | C03 should preserve ammo/munitions positives when defense export demand, backlog visibility, order/shipment cadence, raw-material spread and margin bridge are visible. Poongsan produced a very large MFE with bounded entry-basis MAE, but post-peak drawdown requires lifecycle management. | True | True |
| T_C03_R1L107_103140_20240214_STAGE2ACTIONABLE | 103140 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | ammunition_export_bridge_positive_but_material_spread_contaminant_must_be_split_from_C16_C17 | True | True |
| T_C03_R1L108_103140_20240321_STAGE2_ACTIONABLE | 103140 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current profile can over-promote defense beta unless sovereign funded backlog, delivery schedule and margin/cash bridge are verified | True | True |
| R1L99_C03_POONGSAN_2024_STAGE4B_AMMUNITION_EXPORT_EVENT_CAP | 103140 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_4B_too_late_if_ammunition_export_event_premium_not_capped | True | True |
| V12_COMPACT_C15-101-01_103140_2024-03-07_Stage2_Actionable | 103140 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive | True | True |
| R4L83_C15_103140_20240222_STAGE2_COPPER_DEFENSE_POSITIVE_CONTROL | 103140 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_correct | True | True |
| R4L100_C15_POONGSAN_2024_STAGE2_ACTIONABLE_COPPER_SPREAD_VOLUME_MARGIN_BRIDGE | 103140 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| T_C15_R4L103_103140_Stage2Actionable_20240307 | 103140 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_too_late_or_underexplains_positive_without_company_bridge | True | True |
| R4L95_C16_POONGSAN_2024_STAGE2_ACTIONABLE_COPPER_DEFENSE_MATERIAL_SUPPLY_MARGIN_BRIDGE | 103140 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R1L89_C02_ILJIN_2024_STAGE2_ACTIONABLE_GRID_ORDER_MARGIN_BRIDGE | 103590 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| TRG_R1L78-C02-103590-ILJIN-ELECTRIC-POWER-CABLE-TRANSFORMER-POST-CA | 103590 | C02_POWER_GRID_DATACENTER_CAPEX | C02 should allow power cable/transformer names when datacenter/grid capex maps to order backlog, delivery slots, ASP/copper pass-through and margin bridge. Iljin Electric produced very large MFE after the 2024-02-13 corporate-action candidate; runtime promotion requires post-CA continuity validation and source repair. | True | True |
| R11L85_C02_103590_20240715_STAGE2_FALSE_POSITIVE_WIRE_TRANSFORMER_BETA | 103590 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_false_positive_if_wire_transformer_beta_overcredited | True | True |
| None | 103590 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| None | 103590 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| R13L85_REVIEW_R11_C02_POWER_GRID_DATACENTER_CAPEX_103590_2024-07-15 | 103590 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| R5L96_C18_WOOYANG_2024_STAGE4B_HMR_KFOOD_EXPORT_EVENT_CAP | 103840 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_4B_too_late_if_HMR_Kfood_export_event_premium_not_capped | True | True |
| R13L96_REVIEW_R5_C18_CONSUMER_EXPORT_CHANNEL_REORDER_103840_2024_06_13_TRIGGER | 103840 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late_if_HMR_Kfood_export_event_premium_not_capped | True | True |
| R8L91_C26_104200_20240119_STAGE2_FALSE_POSITIVE_MUSIC_PLATFORM | 104200 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive_if_music_platform_content_theme_overcredited | True | True |
| None | 104540 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | True | True |
| V12_COMPACT_C25_R7L107_104540_20240816_Stage2_FalsePositive_104540_2024-08-16_Stage2-FalsePositive | 104540 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive | True | True |
| None | 104540 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | None | True | True |
| None | 104830 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | True | True |
| V12_COMPACT_C21-KB-20240201_105560_2024-02-01_Stage2_Actionable_CapitalReturn_ValueUp_Bridge | 105560 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | False | True |
| None | 105560 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | False | True |
| None | 105560 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | True | True |
| None | 105560 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | False | True |
| None | 105560 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | True | True |
| TRIG_C31_R11L100_001_105560 | 105560 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_correct | True | True |
| V12_COMPACT_105560_2024-04-26_policy_valueup_bank_brokerage_ROE_PBR_capital_return_execution_bridge | 105560 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_correct | True | True |
| C31_R11L106_TRG_01 | 105560 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | None | True | True |
| V12_COMPACT_105560_2024-02-26_policy_valueup_bank_capital_return_cash_bridge | 105560 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_correct | True | True |
| None | 105560 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | None | False | True |
| None | 105560 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| R13_CROSS_R13L4_C21_105560_20240202_CAPITAL_RETURN_EXECUTION_105560_2024-02-02_Stage3-Yellow | 105560 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | True | True |
| None | 105560 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| R5_L121_C18_003 | 105630 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | True | True |
| None | 105630 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | True | True |
| None | 105630 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | False | True |
| 105630_2023-05-16_Stage2_Actionable_C19_OEM_RESTOCKING_MARGIN_BRIDGE_POSITIVE | 105630 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_correct | False | True |
| C19_R5L119_19_105630_Stage2_Actionable_2024-02-14 | 105630 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | True | True |
| V12_COMPACT_C20_R5L120_105630_20240214_06_105630_2024-02-14_Stage2-Actionable | 105630 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | True | True |
| R1L117-C01-006 | 105740 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_false_positive | False | True |
| C04_P1_TO50_TRG_07 | 105840 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive | True | True |
| TRG_R1L75-C04-105840-WOOJIN-INSTRUMENTATION-POLICY-PROXY-FADE | 105840 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive | True | True |
| C04_STATIC_TO50_TRG_05 | 105840 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive | True | True |
| R11L96_C04_WOOJIN_2024_STAGE2_FALSE_POSITIVE_NUCLEAR_INSTRUMENTATION_POLICY_WATCH | 105840 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive_if_nuclear_instrumentation_policy_watch_counts_without_project_order_delivery_permit_margin_revision_bridge | True | True |
| R1L90_C04_WOOJIN_2024_STAGE2_FALSE_POSITIVE_NUCLEAR_INSTRUMENT_THEME | 105840 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive_if_nuclear_instrument_theme_counts_without_project_order_margin_bridge | True | True |
| TRG_R1L75-C04-105840-WOOJIN-INSTRUMENTATION-POLICY-PROXY-FADE | 105840 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | C04 should not treat nuclear instrumentation or policy proxy beta as durable Stage2 unless project scope, order, customer, safety instrumentation, replacement cycle or margin bridge is verified. Woojin produced an early pop but later opened severe MAE and post-peak drawdown. | True | True |
| R1L85_C04_105840_20240115_STAGE2_FALSE_POSITIVE_NUCLEAR_INSTRUMENT_THEME | 105840 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive_if_policy_theme_overcredited | True | True |
| R1L90_C04_105840_20240522_STAGE2_FALSE_POSITIVE_INSTRUMENTATION_THEME | 105840 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive_if_instrumentation_theme_MFE_overcredited | True | True |
| C04_P1_TO50_TRG_08 | 105840 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive | True | True |
| None | 105840 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | None | True | True |
| R11L93_C31_WOOJIN_2024_STAGE2_FALSE_POSITIVE_NUCLEAR_POLICY_HEADLINE | 105840 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive_if_nuclear_policy_headline_counts_without_order_budget_margin_revision_bridge | True | True |
| R13L96_REVIEW_R11_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_105840_2024_01_15_TRIGGER | 105840 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_nuclear_instrumentation_policy_watch_counts_without_project_order_delivery_permit_margin_revision_bridge | True | True |
| R13L93_REVIEW_R11_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_105840_2024_01_24_TRIGGER | 105840 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_nuclear_policy_headline_counts_without_order_budget_margin_revision_bridge | True | True |
| R13L85_REVIEW_R1_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_105840_2024-01-15 | 105840 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| R13L90_REVIEW_R1_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_105840_2024_01_24_TRIGGER | 105840 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive_if_nuclear_instrument_theme_counts_without_project_order_margin_bridge | True | True |
| TRG_C11_R3L105_004 | 107600 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_missed_structural | True | True |
| None | 108380 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | None | False | True |
| R2L93_C07_110990_20240214_STAGE2_FALSE_POSITIVE_HBM_LASER_WEAK_BRIDGE | 110990 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_false_positive_if_HBM_laser_equipment_vocabulary_overcredited | True | True |
| R2L98_C09_DIT_2024_STAGE2_ACTIONABLE_HBM_LASER_ANNEALING_ADVANCED_EQUIPMENT_BRIDGE | 110990 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R5_L122_C18_008 | 111770 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | True | True |
| R5_L121_C18_002 | 111770 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | True | True |
| None | 111770 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | True | True |
| None | 111770 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | False | True |
| R13_CROSS_111770_2024-02-01_Stage2-FalsePositive_/_InventoryDestockingWatch | 111770 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_false_positive | True | True |
| TRG_R5L78-C19-111770-YOUNGONE-APPAREL-OEM-INVENTORY-MARGIN-FADE | 111770 | C19_BRAND_RETAIL_INVENTORY_MARGIN | C19 should not treat apparel OEM or restocking exposure as durable Stage2 unless customer reorder, inventory normalization, shipment cadence, FX/cost spread and margin bridge refreshes. Youngone had a tradable early MFE, then a large drawdown into the spring/summer window. | True | True |
| None | 111770 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | True | True |
| 111770_2023-05-16_Stage3_Yellow_C19_EXPORT_OEM_INVENTORY_MARGIN_BRIDGE_POSITIVE | 111770 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_correct | False | True |
| C19_R5L119_18_111770_Stage3_Yellow_2024-01-31 | 111770 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | True | True |
| V12_COMPACT_C20_R5L120_111770_20240129_03_111770_2024-01-29_Stage2 | 111770 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | True | True |
| WEMADE_112040_2024_03_11_STAGE2A_GAME_BLOCKCHAIN_IP_MONETIZATION | 112040 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_4B_too_late | False | True |
| V12_COMPACT_C27-R8-L101-001_112040_2024-03-11_game_ip_global_launch_web3_liveops_spike_then_4b | 112040 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_false_positive | True | True |
| C27-R8L105-017|Stage4B|2024-04-01 | 112040 | C27_CONTENT_IP_GLOBAL_MONETIZATION | residual_error_needs_C27_specific_bridge_or_guard | True | True |
| R13_4B4C_L12_08_112040_20240401_4B_Local_Watch | 112040 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_source_proxy_row_promotes_to_green_or_full_4B | True | True |
| V12_COMPACT_R13L12_ACCT_PRICE_10_C27_112040_20240311_112040_2024-03-11_Stage2-Actionable | 112040 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | True | True |
| R13_CROSS_112040_2024-04-01_Stage4B | 112040 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | True | True |
| V12_COMPACT_R13L2_C27_112040_20240311_STAGE2ACTIONABLE_112040_2024-03-11_cross_archetype_high_MAE_guardrail_review | 112040 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| None | 112040 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | True | True |
| T_R13_STAGE2FP_L6_112040_Stage2Actionable_2024-03-11 | 112040 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_stage2_false_positive_or_overpromotion_risk | True | True |
| R1L116-C01-005 | 112610 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_false_positive_if_backlog_without_margin_and_working_capital_bridge_is_promoted | True | True |
| R11L87_C31_CSWIND_2022_STAGE2_ACTIONABLE_IRA_ORDER_CASHFLOW | 112610 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| TRG_R3L82-C11-114190-KANGWON-ENERGY-BATTERY-MATERIAL-EQUIPMENT-THEME-FADE | 114190 | C11_BATTERY_ORDERBOOK_RERATING | C11 should not treat battery material/equipment theme beta as durable orderbook rerating unless direct customer order, material supply volume, delivery, revenue and margin bridge are visible. Kangwon Energy had strong early MFE but then high MAE and post-peak drawdown. | True | True |
| R3L90_C12_114190_20240126_STAGE2_BATTERY_EQUIPMENT_CALLOFF | 114190 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_correct_if_customer_calloff_shipment_margin_bridge_required | True | True |
| R3L99-C14-002-T1 | 114190 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_too_late_if_2023_orderbook_memory_delays_hard_4C | True | True |
| R5L98_C20_IFAMILYSC_2024_STAGE2_ACTIONABLE_K_BEAUTY_EXPORT_DTC_REORDER_BRIDGE | 114840 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| QRI_115180_2024_03_06_STAGE2_FALSE_POSITIVE_CLINICAL_DATA_EVENT | 115180 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_false_positive | False | True |
| C32_115390_LOCKLOCK_20240215_LOCAL4B | 115390 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | would_overpromote_without_tender_cap_guard | True | True |
| TRG_R12L76-C32-115390-LOCKNLOCK-VOLUNTARY-DELISTING-TENDER-FLOOR | 115390 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_correct | True | True |
| TRG_R11L80-C32-115390-LOCKNLOCK-TENDER-PRICE-CAP-DELISTING | 115390 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should distinguish tender-offer price-cap trades from open-ended governance rerating. LocknLock was anchored by a tender/de-listing style price cap and later became inactive_or_delisted_like, so runtime ingestion requires status validation. | True | True |
| TRG_R12L76-C32-115390-LOCKNLOCK-VOLUNTARY-DELISTING-TENDER-FLOOR | 115390 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should preserve tender-floor minority-economics positives when the listed minority shareholder is the direct beneficiary of a tender/voluntary-delisting floor. Lock&Lock showed a controlled-MAE tender rerating and then price pinning near the offer floor; C32 should treat this as event-floor lifecycle, not perpetual operating Stage2. | True | True |
| R12L97_C31_KCS_2024_STAGE2_ACTIONABLE_CBDC_DIGITAL_INFRA_POLICY_LEGISLATION_BRIDGE | 115500 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| TRG_R12L79-C31-117580-DAESUNG-ENERGY-GAS-POLICY-THEME-BETA | 117580 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should not treat city-gas or energy policy/geopolitical beta as durable Stage2 unless tariff formula, direct beneficiary mapping, volume, cost pass-through, earnings and margin bridge are visible. Daesung Energy produced tradable MFE but also a drawdown path; without direct-economics proof it should be local 4B-watch rather than Green. | True | True |
| R9L96_C29_MOTREX_2024_STAGE2_FALSE_POSITIVE_MOBILITY_INFOTAINMENT_VOLUME_WATCH | 118990 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive_if_mobility_infotainment_watch_counts_without_OEM_volume_mix_margin_revision_bridge | True | True |
| R9L86_C29_118990_20240430_STAGE2_FALSE_POSITIVE_AUTONOMOUS_EV_PARTS | 118990 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive_if_EV_parts_theme_overcredited | True | True |
| R13L86_REVIEW_R9_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_118990_2024-04-30 | 118990 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R13L96_REVIEW_R9_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_118990_2024_01_02_TRIGGER | 118990 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_mobility_infotainment_watch_counts_without_OEM_volume_mix_margin_revision_bridge | True | True |
| V12_COMPACT_C25_R7L107_119610_20240610_Stage2_Actionable_119610_2024-06-10_Stage2-Actionable | 119610 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive | True | True |
| R7L89_C25_119610_20240131_STAGE2_FALSE_POSITIVE_CONTACT_LENS_WEAK_BRIDGE | 119610 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive_if_contact_lens_export_theme_overcredited | True | True |
| R1L91_C02_GNCENERGY_2024_STAGE2_FALSE_POSITIVE_BACKUP_POWER_THEME | 119850 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_false_positive_if_backup_power_theme_counts_without_order_margin_delivery_bridge | True | True |
| R11L94_C31_GNCENERGY_2024_STAGE4B_DATACENTER_POWER_POLICY_EVENT_CAP | 119850 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_4B_too_late_if_datacenter_power_policy_event_premium_not_capped | True | True |
| R13L91_REVIEW_R1_C02_POWER_GRID_DATACENTER_CAPEX_119850_2024_05_16_TRIGGER | 119850 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive_if_backup_power_theme_counts_without_order_margin_delivery_bridge | True | True |
| R13L94_REVIEW_R11_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_119850_2024_05_16_TRIGGER | 119850 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_4B_too_late_if_datacenter_power_policy_event_premium_not_capped | True | True |
| C32_119860_CONNECTWAVE_20240517_LOCAL4B | 119860 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_green_risk_if_uncapped | True | True |
| TRG_R12L76-C32-119860-CONNECTWAVE-TENDER-CAP-NO-FURTHER-GREEN | 119860 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive | True | True |
| TRG_R12L76-C32-119860-CONNECTWAVE-TENDER-CAP-NO-FURTHER-GREEN | 119860 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should distinguish tender-floor tradability from ongoing rerating. Connectwave produced a large controlled-MAE move into the tender/floor region and then pinned near the floor, so it is a good counterexample against treating tender-floor MFE as permanent Green. | True | True |
| TRG_R4L76-C17-120110-KOLON-INDUSTRIES-CHEMICAL-MATERIAL-SPREAD-FADE | 120110 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive | True | True |
| TRG_R4L73-C17-120110-KOLONIND-INDUSTRIAL-MATERIAL-SPREAD-FADE | 120110 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | C17 industrial materials should require spread-to-margin refresh. 코오롱인더 produced an initial MFE on industrial-material optimism, but later MAE and drawdown widened; this supports local 4B-watch unless aramid/tire-cord/film margin evidence refreshes. | True | True |
| R4L86_C17_120110_20240423_STAGE2_CHEM_MARGIN_SPREAD_BRIDGE | 120110 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_correct_if_margin_spread_bridge_required | True | True |
| R4L88_C17_KOLONIND_2025_STAGE2_ACTIONABLE_SPREAD_MARGIN_BRIDGE | 120110 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| None | 120110 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | True | True |
| TRG_R4L76-C17-120110-KOLON-INDUSTRIES-CHEMICAL-MATERIAL-SPREAD-FADE | 120110 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | C17 should not treat industrial chemical/material spread beta as durable Stage2 unless volume, product mix, price-cost spread and margin bridge are visible. Kolon Industries had very limited MFE and then a persistent drawdown, so it is a local 4B-watch row rather than a spread-cycle Green. | True | True |
| TRG_R4L73-C17-120110-KOLONIND-INDUSTRIAL-MATERIAL-SPREAD-FADE | 120110 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | C17 industrial materials should require spread-to-margin refresh. 코오롱인더 produced an initial MFE on industrial-material optimism, but later MAE and drawdown widened; this supports local 4B-watch unless aramid/tire-cord/film margin evidence refreshes. | True | True |
| R4L93_C17_120110_20240102_STAGE2_FALSE_POSITIVE_INDUSTRIAL_MATERIALS | 120110 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive_if_industrial_materials_spread_vocabulary_overcredited | True | True |
| R13L86_REVIEW_R4_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_120110_2024-04-23 | 120110 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_correct | True | True |
| TRG_R3L74-C11-121600-NANO-CNT-MATERIAL-ORDERBOOK-BRIDGE | 121600 | C11_BATTERY_ORDERBOOK_RERATING | C11 should include battery material orderbook rerating when CNT additive capacity, customer qualification, order visibility and margin bridge are visible. Nano New Materials had a strong event-window MFE, but the later 2024 collapse shows lifecycle local 4B is necessary if customer/order evidence stops refreshing. | True | True |
| TRG_R3L74-C11-121600-NANO-CNT-MATERIAL-ORDERBOOK-BRIDGE | 121600 | C11_BATTERY_ORDERBOOK_RERATING | C11 should include battery material orderbook rerating when CNT additive capacity, customer qualification, order visibility and margin bridge are visible. Nano New Materials had a strong event-window MFE, but the later 2024 collapse shows lifecycle local 4B is necessary if customer/order evidence stops refreshing. | True | True |
| T_C11_R3L107_121600_STAGE2ACTIONABLE_20240221 | 121600 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_needs_high_MAE_guard_before_green | True | True |
| R3L93_C11_121600_20240312_STAGE2_FALSE_POSITIVE_CNT_SPIKE_NO_FCF | 121600 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive_if_CNT_orderbook_spike_overcredited | True | True |
| None | 121600 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive_if_capacity_label_promotes_Yellow_after_local_blowoff | True | True |
| R3L98_C11_NANOCHEM_2024_STAGE4B_CNT_MATERIAL_ORDERBOOK_EVENT_CAP | 121600 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_4B_too_late_if_CNT_material_orderbook_event_premium_not_capped | True | True |
| NANOMATERIALS_121600_2024_02_21_STAGE2_FALSE_POSITIVE_CUSTOMER_RAMP | 121600 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_false_positive | False | True |
| TRG_R3L78-C12-121600-NANO-CNT-CUSTOMER-CALLOFF-LIFECYCLE | 121600 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | C12 should allow battery-material positives when customer contract visibility maps to call-off volume, capacity absorption, shipment cadence and margin bridge. Nano New Material produced large MFE with controlled early MAE, but the later post-peak drawdown requires lifecycle local 4B if customer call-off or margin evidence fades. | True | True |
| V12_COMPACT_C12_R3L105_121600_20240315_11_121600_2024-03-15_Stage2-Actionable | 121600 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_false_positive | True | True |
| None | 121600 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | True | True |
| None | 121600 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_false_negative_if_generic_battery_calloff_guard_forces_hard_4C_on_CNT_growth_exception | True | True |
| TRG_R3L76-C13-121600-NANOSIN-CNT-CONDUCTIVE-ADDITIVE-US-UTILIZATION | 121600 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_correct | True | True |
| TRG_R3L76-C13-121600-NANOSIN-CNT-CONDUCTIVE-ADDITIVE-US-UTILIZATION | 121600 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | C13 should include CNT/conductive additive suppliers only when US/local supply, customer ramp, utilization and margin bridge is visible. Nano New Material produced strong early MFE, but the later utilization/demand drawdown means the signal must be lifecycle-managed and share-count validated. | True | True |
| T_C13_R3L105_121600_STAGE2ACTIONABLE_20240221 | 121600 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | True | True |
| T_C13_R3L105_121600_STAGE3YELLOW_20240221 | 121600 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | True | True |
| T_C13_R3L103_121600_STAGE3YELLOW_20240314 | 121600 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_too_fast_without_repeat_material_order_bridge | True | True |
| T_C13_R3L104_121600_STAGE4B_20240314 | 121600 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | True | True |
| None | 121600 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | True | True |
| T_C14_R3L108_121600_STAGE3YELLOW_20240221 | 121600 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_false_positive | True | True |
| YG_122870_2024_03_11_STAGE2_FALSE_POSITIVE_FANDOM_IP_LINEUP | 122870 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_false_positive | False | True |
| C27-R8L105-005|Stage2|2024-03-14 | 122870 | C27_CONTENT_IP_GLOBAL_MONETIZATION | residual_error_needs_C27_specific_bridge_or_guard | True | True |
| R9L88_C29_123040_20240926_STAGE2_FALSE_POSITIVE_BODY_PARTS_LATE_EXTENSION | 123040 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive_if_body_parts_late_extension_overcredited | True | True |
| R13L88_REVIEW_R9_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_123040_2024-09-26 | 123040 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| None | 123100 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | False | True |
| R9L91_C29_123410_20240122_STAGE2_HYBRID_VOLUME_MIX | 123410 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_correct_if_OEM_volume_program_mix_margin_cash_bridge_required | True | True |
| R9L90_C29_KOREAFT_2024_STAGE2_ACTIONABLE_HYBRID_VOLUME_MARGIN_BRIDGE | 123410 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R9L94_C29_KOREAFT_2024_STAGE4B_HYBRID_PARTS_MOBILITY_EVENT_CAP | 123410 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_4B_too_late_if_hybrid_parts_mobility_event_premium_not_capped | True | True |
| R13L94_REVIEW_R9_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_123410_2024_04_26_TRIGGER | 123410 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_4B_too_late_if_hybrid_parts_mobility_event_premium_not_capped | True | True |
| V12_COMPACT_123570_2024-05-20_platform_ad_budget_retention_opm_bridge_cleanup | 123570 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| None | 123570 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | None | False | True |
| R8L85_C26_123570_20240306_STAGE2_FALSE_POSITIVE_SMALLCAP_AD_THEME | 123570 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive_if_smallcap_ad_theme_overcredited | True | True |
| R8L92_C26_EMNET_2024_STAGE4B_DIGITAL_AD_AGENCY_EVENT_CAP | 123570 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_4B_too_late_if_digital_ad_agency_event_premium_not_capped | True | True |
| R13L85_REVIEW_R8_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_123570_2024-03-06 | 123570 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| R13L92_REVIEW_R8_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_123570_2024_03_06_TRIGGER | 123570 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_4B_too_late_if_digital_ad_agency_event_premium_not_capped | True | True |
| R5L89_C18_HANKOOKCOS_2024_STAGE4B_KBEAUTY_THEME_CAP | 123690 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_4B_too_late_if_Kbeauty_theme_premium_not_capped | True | True |
| R9L90_C29_126640_20240102_STAGE2_FALSE_POSITIVE_SMALL_CHASSIS | 126640 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive_if_small_chassis_rebound_overcredited | True | True |
| R11L91_C04_126720_20240122_STAGE2_NUCLEAR_OM_PROJECT | 126720 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_correct_if_project_approval_OM_contract_margin_cash_bridge_required | True | True |
| C04_P1_TO50_TRG_18 | 126720 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive | True | True |
| C04_R1_L112_126720_2025_04_24_CZECH_LEGAL_CLEARANCE_SERVICE_SCOPE_POSITIVE_WATCH_TRIGGER | 126720 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_missed_structural | True | True |
| TRG_R1L81-C04-126720-SUSAN-INDUSTRIES-NUCLEAR-OM-PROJECT-BRIDGE | 126720 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | C04 should allow nuclear O&M/maintenance positives when policy attention maps to maintenance project orderbook, outage/regular-maintenance demand, revenue recognition and margin bridge. Susan Industries had controlled entry-basis MAE and moderate MFE, so it should not be overblocked after source repair. | True | True |
| R11L94_C31_JNKGLOBAL_2024_STAGE2_FALSE_POSITIVE_HYDROGEN_POLICY_SUBSIDY_WATCH | 126880 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive_if_hydrogen_policy_subsidy_watch_counts_without_budget_order_margin_revision_bridge | True | True |
| R13L94_REVIEW_R11_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_126880_2024_01_24_TRIGGER | 126880 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive_if_hydrogen_policy_subsidy_watch_counts_without_budget_order_margin_revision_bridge | True | True |
| R4L90_C16_128660_20240412_STAGE2_ALUMINUM_SUPPLY | 128660 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_correct_if_supply_policy_spread_margin_bridge_required | True | True |
| R4L99_C16_PJMETAL_2024_STAGE4B_ALUMINUM_STRATEGIC_METAL_EVENT_CAP | 128660 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_4B_too_late_if_aluminum_strategic_metal_event_premium_not_capped | True | True |
| None | 128940 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | None | False | True |
| None | 128940 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | None | True | True |
| C23_R7_L209_T04 | 128940 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive | False | True |
| V12_COMPACT_128940_2024-02-01_PARTNER_MILESTONE_TO_ROYALTY_BRIDGE | 128940 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive | True | True |
| None | 128940 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | True | True |
| T_C24_R7L105_128940_20240115_STAGE2 | 128940 | C24_BIO_TRIAL_DATA_EVENT_RISK | named_pipeline_visibility_score_too_high_without_fresh_binary_event_or_sales_bridge | True | True |
| None | 128940 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | True | True |
| None | 128940 | C24_BIO_TRIAL_DATA_EVENT_RISK | C24 must require fresh binary/data endpoint quality; reroute commercialization, device, reimbursement, or price-only events to C23/C25/local_4B as appropriate. | True | True |
| R1L90_C04_130660_20240422_STAGE2_NUCLEAR_OM_SERVICE_POLICY | 130660 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_correct_if_project_policy_service_margin_bridge_required | True | True |
| TRG_R1L75-C04-130660-KEPCO-INDUSTRIAL-NUCLEAR-SERVICE-PROJECT-BRIDGE | 130660 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | C04 should allow Stage2 when nuclear policy attention is tied to actual service/O&M/project scope, operating contract visibility and margin bridge. KEPCO Industrial produced very high MFE with controlled entry-basis MAE, but post-peak drawdown requires lifecycle local 4B if project-scope evidence fades. | True | True |
| TRG_R1L75-C04-130660-KEPCO-INDUSTRIAL-NUCLEAR-SERVICE-PROJECT-BRIDGE | 130660 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_correct | True | True |
| R1L90_C04_KEPCOIND_2024_STAGE2_ACTIONABLE_NUCLEAR_OM_POLICY_PROJECT_BRIDGE | 130660 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| None | 130660 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | None | False | True |
| C04_P1_TO50_TRG_10 | 130660 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive | True | True |
| T_C04_R1L107_130660_20240611_Stage4B | 130660 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | local_4b_watch_ok_but_full_stage3_green_requires_margin_or_cash_bridge | True | True |
| C04_STATIC_TO50_TRG_08 | 130660 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive | True | True |
| R11L93_C31_KEPCOINDUSTRIAL_2024_STAGE2_ACTIONABLE_POWER_POLICY_O_AND_M_TARIFF_BRIDGE | 130660 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| V12_COMPACT_C28_R8L104_131090_20240516_131090_2024-05-17_Stage2 | 131090 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive | True | True |
| V12_COMPACT_R13_STAGE2FP_L8_04_131090_2024-05-17_STAGE2_131090_2024-05-17_stage2_source_proxy_deep_MAE_false_positive_review | 131090 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive | True | True |
| TRG-C06-L110-131290-Stage2Actionable-2024-03-22 | 131290 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_too_late | True | True |
| TSE_131290_2024_03_06_STAGE2_FALSE_POSITIVE_TEST_INTERFACE | 131290 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_false_positive | False | True |
| C08_131290_2024_02_01_PROBE_CARD_QUALIFICATION_REORDER_POSITIVE_Stage2-Actionable | 131290 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_missed_structural | False | True |
| TSE_131290_2024_02_13_STAGE2A_PROBE_TEST_REACCELERATION | 131290 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_4B_too_late | False | True |
| C08_R2L97_131290_STAGE2A_20240222_PROBE_CARD_TEST_INTERFACE_BRIDGE | 131290 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_correct_but_risk_overlay_too_late | True | True |
| R2L93_C08_131290_20240426_STAGE2_FALSE_POSITIVE_PROBE_POST_SPIKE | 131290 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_false_positive_if_probe_testinterface_post_spike_vocabulary_overcredited | True | True |
| C08_R2_L112_006_131290_Stage4B | 131290 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_4B_too_late | True | True |
| TRG_C09_R2L98_TSE_20240426_ADV_EQUIP_LATE_CHASE | 131290 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_false_positive | False | True |
| TSE_131290_2024_03_06_STAGE2_FALSE_POSITIVE_MEMORY_TEST_INTERFACE | 131290 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_false_positive | False | True |
| V12_COMPACT_C28-R8-L102-04_131370_2024-07-09_Stage4B | 131370 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive | True | True |
| R4L87_C16_131400_20240124_STAGE2_FALSE_POSITIVE_EV_LITHIUM_RESOURCE | 131400 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_false_positive_if_EV_resource_theme_overcredited | True | True |
| R13L87_REVIEW_R4_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_131400_2024-01-24 | 131400 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| T_C06_R2L103_131970_20240304_Stage2_CROSS_C07 | 131970 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_needs_C06_vs_C07_C08_C09_reroute_guard | True | True |
| TRG-C06-L111-131970-Stage2Actionable-2025-01-02 | 131970 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_missed_structural | True | True |
| V12_COMPACT_131970_2024-03-04_Stage2 | 131970 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_false_positive | True | True |
| DOOSANTESNA_131970_2024_03_06_STAGE2_FALSE_POSITIVE_TEST_SERVICE | 131970 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_false_positive | False | True |
| None | 131970 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | False | True |
| None | 131970 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | False | True |
| TRG_R11L75-C31-133750-MEGA-MD-MEDQUOTA-POLICY-PROXY-FADE | 133750 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | True | True |
| TRG_R11L75-C31-133750-MEGA-MD-MEDQUOTA-POLICY-PROXY-FADE | 133750 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should not treat medical-school quota policy education-proxy spikes as durable Stage2 unless paid enrollment, course demand, retention or margin bridge is visible. MegaMD had a small MFE and then a deep MAE/drawdown. | True | True |
| R5_L122_C18_014 | 136480 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | True | True |
| C19_R5L119_10_136480_Stage3_Yellow_2024-02-02 | 136480 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | True | True |
| C20_R5L117_136480_20240202_Stage3_Yellow | 136480 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_error_or_stress_case | True | True |
| None | 136540 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | None | True | True |
| R13_CROSS_136540_2024-04-11_Stage2-Actionable-SecurityMaintenanceRetention | 136540 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive | True | True |
| V12_COMPACT_C28_R8L104_136540_20240529_136540_2024-05-30_Stage2-Actionable | 136540 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive | True | True |
| R8L91_C28_WINS_2024_STAGE2_FALSE_POSITIVE_SECURITY_RETENTION_SPIKE | 136540 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive_if_security_retention_theme_counts_without_contract_margin_revision_bridge | True | True |
| TRG_R8L79-C28-136540-WINS-SECURITY-CONTRACT-RETENTION-DEFENSIVE | 136540 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | C28 should allow defensive security software positives when maintenance renewal, public/enterprise customer retention, recurring revenue and margin bridge are visible. Wins had bounded entry-basis MAE and later recovery MFE; it is Stage2-Yellow only after source repair, not a security theme blowoff. | True | True |
| R13L91_REVIEW_R8_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_136540_2024_06_25_TRIGGER | 136540 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive_if_security_retention_theme_counts_without_contract_margin_revision_bridge | True | True |
| None | 137400 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_too_conservative_if_battery_equipment_orderbook_bridge_is_capped_below_Yellow | True | True |
| TRG_R3L74-C11-137400-PNT-BATTERY-EQUIPMENT-ORDERBOOK-BRIDGE | 137400 | C11_BATTERY_ORDERBOOK_RERATING | C11 should allow Stage2 when equipment orderbook and delivery-slot visibility convert into margin/revision bridge. PNT produced very high MFE after the trigger, but later post-peak drawdown and an in-window share-count change require lifecycle local 4B and coding-agent validation. | True | True |
| TRG_R3L74-C11-137400-PNT-BATTERY-EQUIPMENT-ORDERBOOK-BRIDGE | 137400 | C11_BATTERY_ORDERBOOK_RERATING | C11 should allow Stage2 when equipment orderbook and delivery-slot visibility convert into margin/revision bridge. PNT produced very high MFE after the trigger, but later post-peak drawdown and an in-window share-count change require lifecycle local 4B and coding-agent validation. | True | True |
| R3L98_C11_PNT_2024_STAGE2_ACTIONABLE_BATTERY_EQUIPMENT_ORDERBOOK_MARGIN_BRIDGE | 137400 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| PNT_137400_2024_03_05_STAGE2A_BATTERY_EQUIPMENT_ORDERBOOK | 137400 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_4B_too_late | False | True |
| TRG_R3L82-C11-137400-PNT-BATTERY-EQUIPMENT-ORDERBOOK-LIFECYCLE | 137400 | C11_BATTERY_ORDERBOOK_RERATING | C11 should protect battery equipment orderbook positives only when customer orderbook, delivery schedule, capacity utilization, revenue recognition and margin bridge are visible. PNT produced very large MFE with shallow entry-basis MAE, but stock-web shard shows share-count movement and post-peak drawdown requires lifecycle 4B discipline. | True | True |
| None | 137400 | C11_BATTERY_ORDERBOOK_RERATING | None | True | True |
| None | 137400 | C11_BATTERY_ORDERBOOK_RERATING | None | True | True |
| None | 137400 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_false_positive_if_battery_equipment_backlog_is_treated_as_completed_customer_pull | True | True |
| V12_COMPACT_C12_R3L105_137400_20240613_13_137400_2024-06-13_Stage3-Yellow | 137400 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_false_positive | True | True |
| None | 137400 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | True | True |
| R3L93_C14_137400_20240213_STAGE2_FALSE_OVERBLOCK_PNT_BACKLOG | 137400 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_false_positive_if_broad_EV_slowdown_guard_blocks_backlog_order_margin_bridge_after_reset | True | True |
| PNT_137400_2024_03_05_FALSE_4C_BROAD_EV_SLOWDOWN | 137400 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_overprotective_4C | False | True |
| R6L95_C22_MERITZFINANCIAL_2024_STAGE2_ACTIONABLE_INSURANCE_RATE_RESERVE_CAPITAL_RETURN_BRIDGE | 138040 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R6L88_C22_138040_20240131_STAGE2_INSURANCE_HOLDCO_CAPITAL_RETURN | 138040 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_correct_if_reserve_capital_return_bridge_required | True | True |
| None | 138040 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | True | True |
| V12_COMPACT_138040_2024-02-01_policy_valueup_insurance_csm_reserve_capital_return_cash_bridge | 138040 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_correct | True | True |
| R13L88_REVIEW_R6_C22_INSURANCE_RATE_CYCLE_RESERVE_138040_2024-01-31 | 138040 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_correct | True | True |
| V12_COMPACT_C28_R8L104_138580_20240312_138580_2024-03-13_Stage2-Actionable | 138580 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive | True | True |
| TRG_R6L79-C21-138930-BNK-REGIONAL-BANK-VALUEUP-BOUNDARY | 138930 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | C21 should avoid forcing regional-bank value-up rows into 4B when entry-basis MAE is bounded and recovery MFE is meaningful. BNK needs ROE, credit-cost, capital buffer and shareholder-return source repair before Stage2, but price action alone does not support hard local 4B. | True | True |
| TRG_R6L77-C21-138930-BNK-FINANCIAL-ROE-PBR-CAPITAL-RETURN | 138930 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | True | True |
| None | 138930 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | True | True |
| TRG_R6L75-C21-138930-BNK-FINANCIAL-REGIONAL-BANK-CAPITAL-RETURN | 138930 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | C21 should keep slower regional-bank capital return winners when ROE stability, dividend path, treasury cancellation and CET1/capital buffer support the rerating. BNK had modest early MFE but a durable low-MAE rerating path; share-count validation remains required. | True | True |
| TRG_R6L75-C21-138930-BNK-FINANCIAL-REGIONAL-BANK-CAPITAL-RETURN | 138930 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | True | True |
| T-BNK-S2A-20250113 | 138930 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_late | True | True |
| None | 138930 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | False | True |
| TRG_R6L77-C21-138930-BNK-FINANCIAL-ROE-PBR-CAPITAL-RETURN | 138930 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | C21 should preserve slow regional-financial rerating rows when sustainable ROE, PBR discount, CET1/capital buffer, dividend policy and capital-return bridge are visible. BNK produced slow controlled-MAE MFE and share-count movement that likely relates to capital policy, but runtime promotion requires share-count validation. | True | True |
| R6L92_C22_138930_20240129_STAGE2_FALSE_POSITIVE_BANK_RATE_CROSSLABEL | 138930 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive_if_bank_rate_PBR_MFE_counted_as_C22_insurance_evidence | True | True |
| V12_COMPACT_138930_2024-04-26_policy_valueup_bank_brokerage_ROE_PBR_capital_return_execution_bridge | 138930 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | True | True |
| C31_R11L106_TRG_05 | 138930 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | None | True | True |
| V12_COMPACT_138930_2024-05-09_policy_valueup_regional_bank_capital_return_cash_bridge | 138930 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | True | True |
| None | 139130 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | False | True |
| None | 139130 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | True | True |
| V12_COMPACT_139130_2024-04-26_policy_valueup_bank_brokerage_ROE_PBR_capital_return_execution_bridge | 139130 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | True | True |
| C31_R11L106_TRG_07 | 139130 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | None | True | True |
| TRIG_C31_R11L100_005_139130 | 139130 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | True | True |
| None | 139130 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| EMART_139480_2024_01_29_STAGE2_FALSE_POSITIVE_RETAIL_TURNAROUND | 139480 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_false_positive | False | True |
| TRG_R5L74-C19-139480-EMART-GROCERY-TURNAROUND-PRICE-BETA | 139480 | C19_BRAND_RETAIL_INVENTORY_MARGIN | C19 should not treat grocery retail/value-up price beta as durable Stage2 unless inventory turns, SSG/online losses, store traffic and margin bridge improve. E-Mart had early MFE but then opened deep MAE and a large post-peak drawdown, so the first signal should be local 4B-watch rather than Green. | True | True |
| TRG_R5L74-C19-139480-EMART-GROCERY-TURNAROUND-PRICE-BETA | 139480 | C19_BRAND_RETAIL_INVENTORY_MARGIN | C19 should not treat grocery retail/value-up price beta as durable Stage2 unless inventory turns, SSG/online losses, store traffic and margin bridge improve. E-Mart had early MFE but then opened deep MAE and a large post-peak drawdown, so the first signal should be local 4B-watch rather than Green. | True | True |
| TRG_R5L81-C19-139480-EMART-MART-INVENTORY-MARGIN-FADE | 139480 | C19_BRAND_RETAIL_INVENTORY_MARGIN | C19 should not treat mart/value-up or retail restructuring beta as durable Stage2 unless inventory cleanup, online/offline mix, cost control, revenue recovery and margin bridge are visible. E-Mart had a sharp early MFE and then a high-MAE fade. | True | True |
| None | 140410 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | False | True |
| None | 140860 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | False | True |
| R2L88_C09_PARKSYSTEMS_2024_STAGE2_FALSE_POSITIVE_VALUATION_PREMIUM | 140860 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_false_positive_if_quality_premium_counts_without_order_revision_bridge | True | True |
| R2L83_C09_140860_20240514_STAGE2_ADVANCED_AFM_REVENUE_BRIDGE_POSITIVE | 140860 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_correct | True | True |
| R2L93_C09_140860_20240423_STAGE2_FALSE_OVERBLOCK_AFM_METROLOGY_ORDER | 140860 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_false_positive_if_C09_guard_blocks_reset_plus_customer_order_bridge | True | True |
| None | 140860 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | None | True | True |
| V12_COMPACT_141080_2024-02-02_PIPELINE_LICENSE_BLOWOFF_HIGH_MAE_GUARD | 141080 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive | True | True |
| TRG_R7L74-C24-141080-LCB-ADC-PLATFORM-DATA-DERISKING | 141080 | C24_BIO_TRIAL_DATA_EVENT_RISK | C24 should not treat a biotech data/platform event as instant Green at the first gap, but it should allow delayed Stage2 when clinical/platform derisking and partner validation become real. LigaChem Bio required post-CA validation and later lifecycle 4B after the November peak. | True | True |
| C24-R7-L99-TRG-07-141080 | 141080 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_missed_structural | True | True |
| C24_R7L98_TRIG_03_141080 | 141080 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_missed_structural | True | True |
| None | 141080 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | True | True |
| T_C24_R7L105_141080_20240129_STAGE2ACTIONABLE | 141080 | C24_BIO_TRIAL_DATA_EVENT_RISK | underweighted_when_data_license_event_is_real_but_green_needs_royalty_or_endpoint_confirmation | True | True |
| TRG_R7L78-C24-141080-LIGACHEM-ADC-DATA-PARTNERING-POST-CA | 141080 | C24_BIO_TRIAL_DATA_EVENT_RISK | C24 should allow ADC/platform positives only when trial-data quality, partner validation, named program visibility, milestone economics and cash runway bridge are visible. LigaChem Bio produced very large MFE after the 2024-04-23 corporate-action/share-count discontinuity; runtime promotion requires post-CA and share-count validation. | True | True |
| TRG_R7L80-C24-141080-LIGACHEM-ADC-POSTCA-DATA-LICENSE-MILESTONE | 141080 | C24_BIO_TRIAL_DATA_EVENT_RISK | C24 should allow ADC platform positives when post-CA continuity, trial data, license economics, milestone runway, partner quality and commercialization bridge are visible. LigaChem Bio produced a large post-CA MFE, but runtime ingestion requires post-CA/name-change validation. | True | True |
| TRG_R7L76-C24-141080-LIGACHEM-ADC-TRIAL-DATA-POST-CA-LIFECYCLE | 141080 | C24_BIO_TRIAL_DATA_EVENT_RISK | C24 should allow ADC-platform trial-data / partner-validation positives only after corporate-action windows are handled. LigaChem Bio had a 2024-04-23 corporate-action candidate, so the post-CA entry is deliberately 2024-04-24; the post-entry path produced very large MFE, but requires source repair and CA validation before runtime promotion. | True | True |
| TRG_R7L76-C24-141080-LIGACHEM-ADC-TRIAL-DATA-POST-CA-LIFECYCLE | 141080 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_correct | True | True |
| TRG_R7L74-C24-141080-LCB-ADC-PLATFORM-DATA-DERISKING | 141080 | C24_BIO_TRIAL_DATA_EVENT_RISK | C24 should not treat a biotech data/platform event as instant Green at the first gap, but it should allow delayed Stage2 when clinical/platform derisking and partner validation become real. LigaChem Bio required post-CA validation and later lifecycle 4B after the November peak. | True | True |
| R7L93_C24_141080_20240222_STAGE2_FALSE_OVERBLOCK_ADC_PLATFORM_LICENSE | 141080 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_false_positive_if_C24_guard_blocks_platform_license_data_bridge_after_reset | True | True |
| None | 141080 | C24_BIO_TRIAL_DATA_EVENT_RISK | C24 must require fresh binary/data endpoint quality; reroute commercialization, device, reimbursement, or price-only events to C23/C25/local_4B as appropriate. | True | True |
| None | 141080 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | False | True |
| None | 141080 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | True | True |
| R13_CROSS_141080_2024-02-02_Stage2 | 141080 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | True | True |
| None | 141080 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | True | True |
| R13_CROSS_141080_2024-02-02_Stage2 | 141080 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive | True | True |
| NPP_144960_2024_03_06_STAGE2A_PLASMA_POWER_MEMORY_EQUIPMENT_RECOVERY | 144960 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_4B_too_late | False | True |
| R7L98_C23_HUGEL_2024_STAGE2_ACTIONABLE_BOTULINUM_TOXIN_FDA_APPROVAL_COMMERCIALIZATION_BRIDGE | 145020 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R7L85_C23_145020_20240304_STAGE2_APPROVAL_COMMERCIAL_BRIDGE | 145020 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_correct_if_commercialization_bridge_required | True | True |
| C23_R7_L209_T01 | 145020 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_correct | False | True |
| None | 145020 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | None | True | True |
| V12_COMPACT_145020_2024-03-21_REGULATORY_APPROVAL_EXPORT_COMMERCIALIZATION | 145020 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive | True | True |
| None | 145020 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | None | True | True |
| R13L85_REVIEW_R7_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_145020_2024-03-04 | 145020 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_correct | True | True |
| None | 145720 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | None | False | True |
| R7L92_C25_145720_20240229_STAGE2_FALSE_POSITIVE_DENTAL_IMPLANT_EXPORT_SPIKE | 145720 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive_if_dental_export_spike_overcredited | True | True |
| V12_COMPACT_C25_R7L107_145720_20240503_Stage3_Yellow_145720_2024-05-03_Stage3-Yellow | 145720 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive | True | True |
| V12_COMPACT_R13L11-4B4C-002_145720_2024-02-29_cross_archetype_4b_4c_boundary_retest | 145720 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| None | 145720 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| None | 145720 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| R5_L122_C18_016 | 145990 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | True | True |
| R5_L122_C18_020 | 145990 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | True | True |
| C19_R5L119_12_145990_Stage2_Actionable_2024-02-01 | 145990 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | True | True |
| C19_R5L119_16_145990_Stage2_Actionable_2024-05-22 | 145990 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | True | True |
| C20_R5L118_145990_20240201_Stage2_Actionable | 145990 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_error | True | True |
| C20_R5L116_145990_20240522_Stage2_Actionable | 145990 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_undercredits_bridge_but_needs_ASP_mix_guard | True | True |
| None | 147760 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | False | True |
| R1L88_C02_147830_20240926_STAGE2_FALSE_POSITIVE_LATE_GRID_EXTENSION | 147830 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_false_positive_if_late_grid_equipment_extension_overcredited | True | True |
| R13L88_REVIEW_R1_C02_POWER_GRID_DATACENTER_CAPEX_147830_2024-09-26 | 147830 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R3L99-C14-006-T1 | 148930 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_false_positive_if_equipment_order_label_stays_actionable_without_delivery_bridge | True | True |
| None | 149980 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | True | True |
| V12_COMPACT_C25_R7L107_149980_20240507_Stage2_Actionable_149980_2024-05-07_Stage2-Actionable | 149980 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive | True | True |
| None | 149980 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | None | True | True |
| R8L92_C28_150900_20240102_STAGE2_FALSE_POSITIVE_DATA_SECURITY | 150900 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive_if_data_security_vocabulary_overcredited | True | True |
| C28-R8-L101-03-Stage4B-2024-03-27 | 150900 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive | True | True |
| TRG-C09-L116-07-159010-Stage4B-2024-03-15 | 159010 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_4B_too_late_if_component_scarcity_label_promoted | True | True |
| R2L112-C10-005-T1 | 159010 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_false_positive_if_component_capex_beta_promotes_without_customer_order_conversion | True | True |
| TRG_R12L77-C31-159580-ZEROTOSEVEN-LOW-BIRTH-POLICY-THEME-FADE | 159580 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | True | True |
| R12L95_C31_ZEROSEVEN_2024_STAGE2_FALSE_POSITIVE_LOW_BIRTH_POLICY_WATCH | 159580 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive_if_low_birth_policy_watch_counts_without_subsidy_to_sales_channel_margin_revision_bridge | True | True |
| TRG_R11L81-C31-159580-ZERO2SEVEN-CHILDCARE-POLICY-THEME-FADE | 159580 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should not treat childcare/low-birth-rate policy beta as durable Stage2 unless direct beneficiary mapping, channel demand, paid conversion, product sell-through, revenue and margin bridge are visible. Zero to Seven had small policy MFE and then a severe MAE path. | True | True |
| TRG_R12L77-C31-159580-ZEROTOSEVEN-LOW-BIRTH-POLICY-THEME-FADE | 159580 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should not treat childcare/low-birth policy beta as durable Stage2 unless direct demand, channel reorder, sell-through and margin evidence refreshes. Zero to Seven had a tradable MFE, but then high MAE and post-peak fade, making it local 4B rather than Green. | True | True |
| R13L95_REVIEW_R12_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_159580_2024_01_03_TRIGGER | 159580 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_low_birth_policy_watch_counts_without_subsidy_to_sales_channel_margin_revision_bridge | True | True |
| R8L93_C27_NEW_2024_STAGE4B_FILM_STUDIO_CONTENT_EVENT_CAP | 160550 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_4B_too_late_if_film_studio_content_event_premium_not_capped | True | True |
| R13L93_REVIEW_R8_C27_CONTENT_IP_GLOBAL_MONETIZATION_160550_2024_02_26_TRIGGER | 160550 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late_if_film_studio_content_event_premium_not_capped | True | True |
| CYMECHS_160980_2024_03_06_STAGE2_FALSE_POSITIVE_WAFER_TRANSFER_AUTOMATION | 160980 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_false_positive | False | True |
| None | 160980 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | None | True | True |
| C13_R3L102_03_161000_20240130_T1 | 161000 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_data_insufficient | True | True |
| T_C15_R4L105_161000_20240201_07_Stage2-Actionable | 161000 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive | True | True |
| None | 161000 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| T_C17_R4L105_01_161000_Stage2Actionable_20240201 | 161000 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive | True | True |
| None | 161000 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | True | True |
| None | 161000 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | True | True |
| R4L89_C17_161000_20240102_STAGE2_FALSE_POSITIVE_BATTERY_CHEM_REBOUND | 161000 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive_if_battery_chemical_rebound_overcredited | True | True |
| R4L88_C17_AEKYUNGCHEM_2023_STAGE4B_CHEMICAL_BATTERY_THEME_CAP | 161000 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_4B_too_late_if_chemical_battery_theme_premium_not_capped | True | True |
| R4L98_C17_AEKYUNGCHEM_2024_STAGE4B_BATTERY_CHEMICAL_SPREAD_EVENT_CAP | 161000 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_4B_too_late_if_battery_chemical_event_premium_not_capped | True | True |
| C19_R5L120_07_161000_Stage2_Actionable_2024-02-01 | 161000 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | True | True |
| C20_R5L119_161000_20240201_10_Stage2_Actionable | 161000 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | None | True | True |
| None | 161390 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | False | True |
| TRG_R9L77-C29-161390-HANKOOK-TIRE-OE-REPLACEMENT-MIX-MARGIN-FADE | 161390 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| R9L88_C29_HANKOOKTIRE_2024_STAGE2_ACTIONABLE_TIRE_MARGIN_BRIDGE | 161390 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| TRG_R9L73-C29-161390-HANKOOKTIRE-PRICE-MIX-MARGIN-LEVERAGE | 161390 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should include tire price/mix and replacement-demand margin leverage, not only OEM vehicle volume. 한국타이어 produced a strong MFE with controlled early MAE, but later post-peak drawdown means local 4B-watch is needed if margin/mix evidence stops refreshing. | True | True |
| TRG_R9L73-C29-161390-HANKOOKTIRE-PRICE-MIX-MARGIN-LEVERAGE | 161390 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should include tire price/mix and replacement-demand margin leverage, not only OEM vehicle volume. 한국타이어 produced a strong MFE with controlled early MAE, but later post-peak drawdown means local 4B-watch is needed if margin/mix evidence stops refreshing. | True | True |
| T_C29_R9L106_161390_20240430_13_Stage2-Actionable | 161390 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| TRG_R9L77-C29-161390-HANKOOK-TIRE-OE-REPLACEMENT-MIX-MARGIN-FADE | 161390 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should not treat tire/OE/replacement-cycle beta as durable Stage2 unless OE/replacement volume, product mix, raw-material cost spread and margin bridge refreshes. Hankook Tire had a tradable MFE, then opened a high-MAE drawdown path. | True | True |
| R9L84_C29_161390_20240411_STAGE2_FALSE_POSITIVE_TIRE_MARGIN_PEAK | 161390 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive_if_tire_margin_peak_overcredited | True | True |
| TRG_R9L79-C29-161390-HANKOOK-TIRE-MIX-MARGIN-LIFECYCLE | 161390 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 can preserve tire volume/mix positives when OE/replacement demand, product mix, raw-material cost spread, pricing and margin bridge are visible. Hankook Tire produced meaningful MFE, but later high MAE after the peak means the signal must be lifecycle-managed instead of permanent Green. | True | True |
| None | 161390 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | False | True |
| T_C29_R9L104_161390_STAGE4B_20240125 | 161390 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | True | True |
| PHILOPTICS_161580_2024_03_06_STAGE2A_GLASS_SUBSTRATE_EQUIPMENT | 161580 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_4B_too_late | False | True |
| None | 161890 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | True | True |
| C19_R5L120_04_161890_Stage2_Actionable_2024-05-08 | 161890 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | True | True |
| C20_R5L119_161890_20240508_04_Stage2_Actionable | 161890 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | None | True | True |
| C20_R5_L102_T04_161890 | 161890 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_correct | True | True |
| None | 161890 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | None | False | True |
| None | 161890 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | None | False | True |
| T_C06_R2L103_166090_20240226_Stage2_CROSS_C07 | 166090 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_needs_C06_vs_C07_C08_C09_reroute_guard | True | True |
| V12_COMPACT_166090_2024-02-26_Stage2 | 166090 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_false_positive | True | True |
| R2_L110_C07 | 166090 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | None | True | True |
| None | 166090 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | False | True |
| HANAMATERIALS_166090_2024_03_06_STAGE2A_MEMORY_PARTS_RECOVERY | 166090 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_4B_too_late | False | True |
| HANAMATERIALS_166090_2024_03_22_STAGE2A_MEMORY_PROCESS_PARTS_RECOVERY | 166090 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_4B_too_late | False | True |
| R2L89_C10_166090_20240626_STAGE2_FALSE_POSITIVE_PARTS_LATE_CYCLE | 166090 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_false_positive_if_parts_late_cycle_extension_overcredited | True | True |
| C07-R2-L111-168360-Stage2Actionable-2024-12-03 | 168360 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_too_strict_if_HBM_inspection_tool_qualification_has_non_price_customer_signal | True | True |
| R8L91_C28_PIOLINK_2024_STAGE2_ACTIONABLE_NETWORK_SECURITY_ADC_CONTRACT_BRIDGE | 170790 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| C23_170900_20240229_STAGE2_TRIGGER | 170900 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | None | True | True |
| None | 170900 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | None | True | True |
| V12_COMPACT_170900_2024-03-14_COMMERCIAL_PRODUCT_EXPORT_REORDER_BRIDGE | 170900 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive | True | True |
| None | 170900 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | None | True | True |
| None | 170900 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | False | True |
| R7L93_C24_ABCLON_2024_STAGE4B_CART_TRIAL_DATA_EVENT_CAP | 174900 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_4B_too_late_if_CART_trial_data_event_premium_not_capped | True | True |
| R13L93_REVIEW_R7_C24_BIO_TRIAL_DATA_EVENT_RISK_174900_2024_03_05_TRIGGER | 174900 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late_if_CART_trial_data_event_premium_not_capped | True | True |
| R6L92_C21_JBFG_2024_STAGE2_ACTIONABLE_REGIONAL_BANK_ROE_CAPITAL_RETURN | 175330 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| TRG_R6L77-C21-175330-JB-FINANCIAL-ROE-PBR-CAPITAL-RETURN | 175330 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | C21 should allow regional-bank value-up positives when PBR discount, sustainable ROE, CET1/capital buffer, dividend/buyback and shareholder-return bridge are visible. JB Financial produced high MFE with essentially no entry-basis MAE; it should be protected after source repair while still requiring lifecycle monitoring if capital-return evidence fades. | True | True |
| TRG_R6L75-C21-175330-JB-FINANCIAL-ROE-CAPITAL-RETURN-BRIDGE | 175330 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | C21 should allow Stage2 when low-PBR/value-up attention connects to durable ROE, payout, treasury cancellation or capital-return bridge. JB Financial produced high MFE with controlled entry-basis MAE; share-count movement should be validated before runtime promotion. | True | True |
| TRG_R6L77-C21-175330-JB-FINANCIAL-ROE-PBR-CAPITAL-RETURN | 175330 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_correct | True | True |
| TRG_R6L75-C21-175330-JB-FINANCIAL-ROE-CAPITAL-RETURN-BRIDGE | 175330 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_correct | True | True |
| None | 175330 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | True | True |
| None | 175330 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | False | True |
| None | 175330 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | True | True |
| V12_COMPACT_175330_2024-04-26_policy_valueup_bank_brokerage_ROE_PBR_capital_return_execution_bridge | 175330 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_correct | True | True |
| C31_R11L106_TRG_06 | 175330 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | None | True | True |
| R12L87_C32_HANJINKAL_2020_STAGE2_ACTIONABLE_CONTROL_PREMIUM | 180640 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_kept_but_4B_overlay_needed_after_fast_event_run | True | True |
| T_C32_R12L106_180640_20240129_Stage2-Actionable | 180640 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | Stage2-Actionable watch is acceptable, but Stage3-Green/full4B should be blocked without direct minority cash path | True | True |
| R12L93_C32_HANJINKAL_2024_STAGE2_FALSE_POSITIVE_AIRLINE_HOLDCO_CONTROL_PREMIUM_WATCH | 180640 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive_if_airline_holdco_control_premium_watch_counts_without_tender_control_premium_execution_bridge | True | True |
| R12L92_C32_180640_20240129_STAGE2_FALSE_POSITIVE_HISTORICAL_CONTROL_PREMIUM | 180640 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive_if_historical_control_premium_vocabulary_overcredited | True | True |
| None | 180640 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | None | True | True |
| R13L93_REVIEW_R12_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_180640_2024_02_08_TRIGGER | 180640 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_airline_holdco_control_premium_watch_counts_without_tender_control_premium_execution_bridge | True | True |
| TR_C26_L105_181710_Stage2_20240930 | 181710 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_missed_structural | True | True |
| R8L91_C26_181710_20240129_STAGE2_PLATFORM_OPERATING_LEVERAGE | 181710 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_correct_if_ARPU_mix_cost_margin_cash_bridge_required | True | True |
| V12_COMPACT_181710_2024-02-05_platform_ad_budget_retention_opm_bridge_cleanup | 181710 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| None | 181710 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | None | False | True |
| R10L92_C30_183190_20240129_STAGE2_CEMENT_MARGIN_CASH | 183190 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_correct_if_ASP_input_cost_margin_cash_bridge_required_but_Green_strict | True | True |
| None | 183300 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | False | True |
| R13_CROSS_184230_2024-07-01_Stage2 | 184230 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| V12_COMPACT_185750_2024-02-15_PRESCRIPTION_VOLUME_REIMBURSEMENT_CONFIRMATION | 185750 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive | True | True |
| C23_185750_20240710_STAGE2_TRIGGER | 185750 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | None | True | True |
| None | 185750 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | None | True | True |
| None | 185750 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | False | True |
| DEVICEENG_187870_2024_03_06_STAGE2_FALSE_POSITIVE_ADVANCED_CLEANING_EQUIPMENT | 187870 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_false_positive | False | True |
| V12_COMPACT_C28_R8L104_189690_20240531_189690_2024-06-03_Stage2 | 189690 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive | True | True |
| V12_COMPACT_R13_STAGE2FP_L8_14_189690_2024-06-03_STAGE2_189690_2024-06-03_stage2_source_proxy_deep_MAE_false_positive_review | 189690 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive | True | True |
| SEOJUN_189860_2024_07_09_STAGE2_FALSE_POSITIVE_SWITCHGEAR_LATE_BETA | 189860 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_false_positive | False | True |
| TRG_R1L80-C02-189860-SEOJEON-ELECTRIC-SWITCHGEAR-THEME-BACKLOG-GAP | 189860 | C02_POWER_GRID_DATACENTER_CAPEX | C02 should not treat switchgear/grid/nuclear theme beta as durable Stage2 unless named customer, order backlog, delivery schedule, revenue recognition and margin bridge are visible. Seojeon Electric produced tradable MFE, then a post-peak drawdown, making it local 4B-watch rather than durable Green. | True | True |
| V12_COMPACT_R13L11-4B4C-016_189860_2024-05-28_cross_archetype_4b_4c_boundary_retest | 189860 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R13_CROSS_189860_2024-05-28_Stage2 | 189860 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| T_R13_STAGE2FP_L6_189860_Stage2_2024-04-12 | 189860 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_stage2_false_positive_or_overpromotion_risk | True | True |
| C27-R8L105-009|Stage2-Actionable|2024-01-30 | 192080 | C27_CONTENT_IP_GLOBAL_MONETIZATION | residual_error_needs_C27_specific_bridge_or_guard | True | True |
| V12_COMPACT_C28_R8L104_192250_20240513_192250_2024-05-14_Stage2 | 192250 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive | True | True |
| TRG_R8L79-C28-192250-KSIGN-SECURITY-THEME-LOCAL4B-CA-CAVEAT | 192250 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | C28 should not treat security/encryption/authentication theme MFE as durable Stage2 unless contract retention, renewal rate, recurring revenue, public/enterprise customer quality and margin bridge are visible. KSign produced a sharp MFE and then high MAE; 2024-11-01 corporate-action candidate is outside the selected 180D interpretation but must be validated before any extended ingestion. | True | True |
| R8L93_C28_192250_20240326_STAGE2_FALSE_POSITIVE_CERT_SECURITY_CA | 192250 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive_if_certificate_security_theme_or_post_CA_price_counted_as_retention_evidence | True | True |
| V12_COMPACT_R13_STAGE2FP_L8_06_192250_2024-05-14_STAGE2_192250_2024-05-14_stage2_source_proxy_deep_MAE_false_positive_review | 192250 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive | True | True |
| TRG_R5L73-C18-192820-COSMAX-ODM-GLOBAL-CUSTOMER-REORDER | 192820 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | C18 should reward ODM/customer reorder only when global customer demand and margin conversion are visible. Cosmax shows a strong MFE path with manageable entry-basis MAE, but source repair is required before promotion. | True | True |
| TRG_R5L73-C18-192820-COSMAX-ODM-GLOBAL-CUSTOMER-REORDER | 192820 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | C18 should reward ODM/customer reorder only when global customer demand and margin conversion are visible. Cosmax shows a strong MFE path with manageable entry-basis MAE, but source repair is required before promotion. | True | True |
| TRG_R5L82-C18-192820-COSMAX-ODM-GLOBAL-CHANNEL-REORDER | 192820 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | C18 should allow global ODM/channel positives when customer mix, export channel sell-through, reorder cadence, capacity utilization, revenue conversion and margin bridge are visible. Cosmax had strong MFE but not without MAE, so source repair is required before Stage2 promotion. | True | True |
| None | 192820 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | True | True |
| C19_R5L120_03_192820_Stage2_Actionable_2024-04-30 | 192820 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | True | True |
| TRG_R5L80-C20-192820-COSMAX-BEAUTY-ODM-GLOBAL-REORDER-MARGIN | 192820 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | C20 should protect beauty ODM/OEM positives when global channel reorder, customer quality, US/China volume, revenue conversion and margin bridge are visible. Cosmax produced a large MFE but later drawdown means lifecycle 4B is needed if channel/revenue/margin evidence fades. | True | True |
| R5L100_C20_COSMAX_2024_STAGE2_ACTIONABLE_K_BEAUTY_ODM_GLOBAL_CHANNEL_MARGIN_BRIDGE | 192820 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| C20_R5L119_192820_20240430_03_Stage2_Actionable | 192820 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | None | True | True |
| None | 192820 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | None | False | True |
| C20_R5_L102_T08_192820 | 192820 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_4B_too_late | True | True |
| None | 192820 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| None | 192820 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| TRG_R8L78-C27-194480-DEVSISTERS-GAME-IP-GLOBAL-MONETIZATION | 194480 | C27_CONTENT_IP_GLOBAL_MONETIZATION | C27 should preserve game-IP monetization positives only when launch/update traction, DAU retention, revenue rank, overseas channel and margin bridge are visible. Devsisters produced very large MFE with controlled entry-basis MAE, but later drawdown requires lifecycle 4B if IP monetization evidence fades. Share-count movement inside the raw shard requires validation. | True | True |
| R8L93_C27_DEVSISTERS_2024_STAGE2_ACTIONABLE_GAME_IP_GLOBAL_LIVEOPS_MONETIZATION | 194480 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| TRG_R8L76-C27-194480-DEVSISTERS-GAME-IP-GLOBAL-LAUNCH-MONETIZATION | 194480 | C27_CONTENT_IP_GLOBAL_MONETIZATION | C27 should allow game-IP positives when global launch, DAU/MAU, IAP revenue, platform monetization, royalty/licensing and margin bridge are visible. Devsisters produced large MFE but later post-peak drawdown and share-count movement require lifecycle local 4B and validation. | True | True |
| TRG_R8L76-C27-194480-DEVSISTERS-GAME-IP-GLOBAL-LAUNCH-MONETIZATION | 194480 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_correct | True | True |
| V12_COMPACT_C27-R8-L101-002_194480_2024-03-07_cookie_run_new_title_global_ip_monetization_reacceleration | 194480 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_false_positive | True | True |
| TRG_R8L80-C27-194480-DEVSISTERS-COOKIE-IP-GLOBAL-LAUNCH-MARGIN | 194480 | C27_CONTENT_IP_GLOBAL_MONETIZATION | C27 should allow game-IP launch/live-ops positives when global launch cadence, user acquisition, sales ranking, revenue conversion and margin bridge are visible. Devsisters produced large MFE, but later drawdown makes lifecycle 4B necessary if post-launch metrics fade. | True | True |
| C27-R8L105-018|Stage3-Yellow|2024-05-27 | 194480 | C27_CONTENT_IP_GLOBAL_MONETIZATION | residual_error_needs_C27_specific_bridge_or_guard | True | True |
| R2L93_C06_195870_20240102_STAGE2_FALSE_POSITIVE_SUBSTRATE_DECAY | 195870 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_false_positive_if_memory_substrate_vocabulary_overcredited | True | True |
| None | 195870 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | None | True | True |
| HKINNON_195940_2024_01_03_STAGE2_FALSE_POSITIVE_COMMERCIALIZATION_PREMIUM | 195940 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive | False | True |
| V12_COMPACT_195940_2024-02-02_COMMERCIAL_DRUG_REIMBURSEMENT_VOLUME_BRIDGE | 195940 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive | True | True |
| TRG_R7L73-C23-195940-HKINNO-KCAB-GLOBAL-COMMERCIALIZATION-RAMP | 195940 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | C23 should distinguish real prescription/export commercialization ramp from pure regulatory excitement. HK inno.N produced an attractive path, but later post-peak drawdown requires local 4B-watch if prescription/partner revenue evidence stops refreshing. | True | True |
| TRG_R7L73-C23-195940-HKINNO-KCAB-GLOBAL-COMMERCIALIZATION-RAMP | 195940 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | C23 should distinguish real prescription/export commercialization ramp from pure regulatory excitement. HK inno.N produced an attractive path, but later post-peak drawdown requires local 4B-watch if prescription/partner revenue evidence stops refreshing. | True | True |
| R7L93_C23_195940_20240617_STAGE2_DRUG_COMMERCIAL_BRIDGE | 195940 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_correct_if_approval_launch_reimbursement_royalty_cash_bridge_required_but_Green_strict | True | True |
| None | 195940 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | None | True | True |
| None | 195940 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| None | 195940 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| None | 195940 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| V12_COMPACT_196170_2024-02-02_ROYALTY_COMMERCIALIZATION_BRIDGE_REVERIFY | 196170 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive | True | True |
| R7L92_C23_ALTEOGEN_2024_STAGE2_ACTIONABLE_PLATFORM_LICENSE_REGULATORY_COMMERCIALIZATION | 196170 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| None | 196170 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | None | False | True |
| None | 196170 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | None | True | True |
| None | 196170 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | True | True |
| R7L84_C24_196170_20240222_STAGE2_PLATFORM_EVENT_VALIDATION_BRIDGE | 196170 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_correct_if_partner_validation_bridge_required | True | True |
| C24_R7L98_TRIG_01_196170 | 196170 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_missed_structural | True | True |
| R7L87_C24_196170_20240223_STAGE2_PLATFORM_LICENSE_EVENT | 196170 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_correct_if_partnered_platform_data_bridge_required | True | True |
| None | 196170 | C24_BIO_TRIAL_DATA_EVENT_RISK | C24 must require fresh binary/data endpoint quality; reroute commercialization, device, reimbursement, or price-only events to C23/C25/local_4B as appropriate. | True | True |
| None | 196170 | C24_BIO_TRIAL_DATA_EVENT_RISK | C24 must require fresh binary/data endpoint quality; reroute commercialization, device, reimbursement, or price-only events to C23/C25/local_4B as appropriate. | True | True |
| None | 196170 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | False | True |
| R13L87_REVIEW_R7_C24_BIO_TRIAL_DATA_EVENT_RISK_196170_2024-02-23 | 196170 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_correct | True | True |
| R13_CROSS_R13L4_C23_196170_20240221_ROYALTY_REVENUE_TRUST_196170_2024-02-21_Stage2-Actionable | 196170 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | True | True |
| R1L89_C02_JEIL_2024_STAGE2_FALSE_POSITIVE_BREAKER_THEME_HIGH_MAE | 199820 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_false_positive_if_breaker_theme_counts_without_order_margin_bridge | True | True |
| TRG_R1L80-C02-199820-CHEIL-ELECTRIC-POST-CA-SWITCHGEAR-FADE | 199820 | C02_POWER_GRID_DATACENTER_CAPEX | C02 should not treat post-CA switchgear/datacenter theme beta as durable Stage2 unless order backlog, customer quality, delivery schedule, revenue recognition and margin bridge survive the corporate-action reset. Cheil Electric's post-CA path had small MFE and high MAE. | True | True |
| R11L89_C02_199820_20240920_STAGE2_FALSE_POSITIVE_SWITCHGEAR_THEME | 199820 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_false_positive_if_switchgear_theme_overcredited | True | True |
| None | 200350 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | None | False | True |
| C27-R8L105-013|Stage4B|2024-02-29 | 200350 | C27_CONTENT_IP_GLOBAL_MONETIZATION | residual_error_needs_C27_specific_bridge_or_guard | True | True |
| None | 200350 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| R13_4B4C_L12_05_200350_20240229_Stage4C_Watch | 200350 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_source_proxy_row_promotes_to_green_or_full_4B | True | True |
| None | 200350 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| R13_CROSS_200350_2024-02-29_Stage4B | 200350 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | True | True |
| None | 200350 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | True | True |
| None | 200350 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | True | True |
| AFACT_200470_2024_03_06_STAGE2A_TEST_SERVICE_RERATING | 200470 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_4B_too_late | False | True |
| None | 200470 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | None | True | True |
| R2L95_C10_AFACT_2024_STAGE4B_TEST_OUTSOURCING_MEMORY_EVENT_CAP | 200470 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_4B_too_late_if_memory_test_outsourcing_event_premium_not_capped | True | True |
| R13L95_REVIEW_R2_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_200470_2024_06_04_TRIGGER | 200470 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late_if_memory_test_outsourcing_event_premium_not_capped | True | True |
| V12_COMPACT_200670_2024-02-02_AESTHETIC_DEVICE_PHARMA_OVERLAP_REROUTE | 200670 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive | True | True |
| R7L89_C25_200670_20240325_STAGE2_AESTHETIC_EXPORT_MARGIN | 200670 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_correct_if_export_reimbursement_margin_bridge_required | True | True |
| R9L91_C29_SEOYONEHWA_2024_STAGE2_ACTIONABLE_AUTO_INTERIOR_VOLUME_MARGIN | 200880 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R9L88_C29_200880_20240201_STAGE2_GLOBAL_AUTOPARTS_VOLUME_MARGIN | 200880 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_correct_if_volume_mix_margin_bridge_required | True | True |
| TRG_R9L80-C29-200880-SEOYON-EHWA-AUTO-INTERIOR-VOLUME-MIX-LIFECYCLE | 200880 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should preserve auto interior/module positives when customer program volume, product mix, utilization, pricing and margin bridge are visible. Seoyon E-Hwa produced a very large early MFE but later high MAE requires lifecycle local 4B if volume/mix/margin evidence fades. | True | True |
| None | 200880 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | True | True |
| T_C29_R9L105_200880_Stage3Yellow_20240617 | 200880 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| T_C29_R9L106_200880_20240617_09_Stage4B | 200880 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| R13L88_REVIEW_R9_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_200880_2024-02-01 | 200880 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_correct | True | True |
| R7L96_C24_ABION_2024_STAGE2_FALSE_POSITIVE_CLINICAL_DATA_EVENT_WATCH | 203400 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_false_positive_if_clinical_data_event_watch_counts_without_endpoint_partner_funding_regulatory_revision_bridge | True | True |
| R13L96_REVIEW_R7_C24_BIO_TRIAL_DATA_EVENT_RISK_203400_2024_06_10_TRIGGER | 203400 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_clinical_data_event_watch_counts_without_endpoint_partner_funding_regulatory_revision_bridge | True | True |
| DREAMSECURITY_203650_2024_02_15_STAGE2_FALSE_POSITIVE_SECURITY_AUTH_THEME | 203650 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive | False | True |
| V12_COMPACT_C28_R8L104_203650_20240701_203650_2024-07-02_Stage2 | 203650 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive | True | True |
| V12_COMPACT_C28-R8-L102-03_203650_2024-06-17_Stage4B | 203650 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive | True | True |
| V12_COMPACT_R13_STAGE2FP_L8_08_203650_2024-07-02_STAGE2_203650_2024-07-02_stage2_source_proxy_deep_MAE_false_positive_review | 203650 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive | True | True |
| T_R9L10_204320_STAGE2 | 204320 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | False | True |
| R9L96_C29_HLMANDO_2024_STAGE2_ACTIONABLE_ADAS_AUTO_PARTS_VOLUME_MARGIN_BRIDGE | 204320 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| TRG_C29_R9L100_204320_STAGE2_FALSE_20240605 | 204320 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | False | True |
| R9L83_C29_204320_20240605_STAGE2_FALSE_POSITIVE_ADAS_EV_SPIKE_HIGH_MAE | 204320 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| C29_R9L87_TRG_204320_S2 | 204320 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| T_C29_R9L106_204320_20240605_05_Stage4B | 204320 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| T_C29_R9L105_204320_Stage4B_20240605 | 204320 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| TRG_C29_R9L100_204320_STAGE4B_OVERLAY_20240607 | 204320 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_4B_too_late | False | True |
| R9L88_C29_HLMANDO_2024_STAGE4B_AUTO_PARTS_EVENT_CAP | 204320 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_4B_too_late_if_auto_parts_mobility_premium_not_capped | True | True |
| T_C29_R9L106_204320_20241112_19_Stage4C | 204320 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| R13L88_REVIEW_C29_HLMANDO_2024_STAGE4B_AUTO_PARTS_EVENT_CAP | 204320 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late_if_auto_parts_mobility_premium_not_capped | True | True |
| R13L83_HIGHMAE_REVIEW_204320_2024-06-05 | 204320 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| TRG_R8L76-C27-206560-DEXTER-VFX-CONTENT-PRODUCTION-PIPELINE | 206560 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_false_positive | True | True |
| TRG_R8L76-C27-206560-DEXTER-VFX-CONTENT-PRODUCTION-PIPELINE | 206560 | C27_CONTENT_IP_GLOBAL_MONETIZATION | C27 should not only include idol/label/game names; VFX/content production pipelines can be C27 when order backlog, production schedule, global IP service revenue and margin bridge are visible. Dexter produced controlled-MAE follow-through, but needs non-price order/pipeline evidence before runtime promotion. | True | True |
| R8L90_C27_206560_20240109_STAGE2_FALSE_POSITIVE_VFX_THEME | 206560 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_false_positive_if_VFX_content_theme_overcredited | True | True |
| None | 206640 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | None | True | True |
| TRG_R7L75-C25-206640-BODITECH-IVD-EXPORT-CHANNEL-MARGIN-BRIDGE | 206640 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | C25 should allow Stage2 when IVD device export/channel reorder converts into installed base, reagent pull-through, utilization and margin bridge. Boditech Med produced high MFE with controlled entry-basis MAE, but later drawdown requires lifecycle local 4B if export/reagent bridge fades. | True | True |
| TRG_R7L75-C25-206640-BODITECH-IVD-EXPORT-CHANNEL-MARGIN-BRIDGE | 206640 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_correct | True | True |
| R7L91_C25_BODITECH_2024_STAGE2_ACTIONABLE_DIAGNOSTIC_DEVICE_EXPORT_REIMBURSEMENT | 206640 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R7L87_C24_206650_20240215_STAGE2_FALSE_POSITIVE_VACCINE_EVENT | 206650 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_false_positive_if_vaccine_event_theme_promoted_without_partner_revenue_bridge | True | True |
| R7L84_C24_206650_20240415_STAGE2_FALSE_POSITIVE_VACCINE_THEME_SPIKE | 206650 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_false_positive_if_vaccine_theme_spike_overcredited | True | True |
| R13L87_REVIEW_R7_C24_BIO_TRIAL_DATA_EVENT_RISK_206650_2024-02-15 | 206650 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| TRG_R8L76-C27-207760-MRBLUE-WEBTOON-IP-THEME-SPIKE-FADE | 207760 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_false_positive | True | True |
| TRG_R8L76-C27-207760-MRBLUE-WEBTOON-IP-THEME-SPIKE-FADE | 207760 | C27_CONTENT_IP_GLOBAL_MONETIZATION | C27 should not treat webtoon/IP/platform theme spikes as durable Stage2 unless paid-content revenue, subscriber/traffic conversion, global distribution, licensing and margin bridge are visible. Mr. Blue produced large MFE but later collapsed into a high-MAE local 4B path; share-count movement requires validation. | True | True |
| V12_COMPACT_207940_2024-02-02_CDMO_REGULATORY_LABEL_WITHOUT_INCREMENTAL_ORDER | 207940 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive | True | True |
| SAMBIO_207940_2024_01_29_STAGE2A_CDMO_COMMERCIALIZATION | 207940 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_correct | False | True |
| C24-R7-L99-TRG-05-208340 | 208340 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_4C_too_late | True | True |
| None | 208370 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | None | True | True |
| R13_4B4C_L12_13_208370_20240229_4B_Local_Watch | 208370 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_source_proxy_row_promotes_to_green_or_full_4B | True | True |
| R13_CROSS_208370_2024-02-29_Stage4B | 208370 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | True | True |
| R13_CROSS_208370_2024-02-29_Stage4B | 208370 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| R6L88_C22_211050_20241115_STAGE2_FALSE_POSITIVE_GA_DISTRIBUTION_SPIKE | 211050 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive_if_GA_distribution_beta_promoted_as_C22 | True | True |
| R6L95_C22_INCARFINANCIAL_2024_STAGE4B_INSURANCE_BROKER_COMMISSION_EVENT_CAP | 211050 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_4B_too_late_if_insurance_broker_commission_event_premium_not_capped | True | True |
| R13L88_REVIEW_R6_C22_INSURANCE_RATE_CYCLE_RESERVE_211050_2024-11-15 | 211050 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R13L95_REVIEW_R6_C22_INSURANCE_RATE_CYCLE_RESERVE_211050_2024_05_08_TRIGGER | 211050 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late_if_insurance_broker_commission_event_premium_not_capped | True | True |
| None | 211270 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | None | False | True |
| R11L95_C03_APSAT_2024_STAGE2_FALSE_POSITIVE_SMALLSAT_POLICY_EXPORT_WATCH | 211270 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_false_positive_if_smallsat_policy_watch_counts_without_customer_order_backlog_delivery_margin_revision_bridge | True | True |
| R13L95_REVIEW_R11_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_211270_2024_01_03_TRIGGER | 211270 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_smallsat_policy_watch_counts_without_customer_order_backlog_delivery_margin_revision_bridge | True | True |
| None | 214150 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | None | False | True |
| R7L92_C25_214150_20240214_STAGE2_AESTHETIC_DEVICE_CONSUMABLE_EXPORT | 214150 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_correct_if_procedure_volume_consumable_reorder_margin_cash_bridge_required_but_data_quality_repair_needed | True | True |
| V12_COMPACT_C25_R7L107_214150_20240605_Stage3_Yellow_214150_2024-06-05_Stage3-Yellow | 214150 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive | True | True |
| None | 214150 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| None | 214150 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| None | 214270 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | None | False | True |
| TRG_R8L73-C26-214270-FSN-DIGITAL-ADTECH-PRICE-BETA-LOCAL4B | 214270 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | C26 should not treat digital-adtech or platform theme MFE as durable Stage2 unless recurring ad revenue, take-rate, client retention and margin conversion are visible. FSN had a sharp MFE but later severe MAE and post-peak drawdown. | True | True |
| TRG_R8L73-C26-214270-FSN-DIGITAL-ADTECH-PRICE-BETA-LOCAL4B | 214270 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | C26 should not treat digital-adtech or platform theme MFE as durable Stage2 unless recurring ad revenue, take-rate, client retention and margin conversion are visible. FSN had a sharp MFE but later severe MAE and post-peak drawdown. | True | True |
| TR_C26_L105_214270_Stage4B_20240215 | 214270 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_4B_too_late | True | True |
| V12_COMPACT_214270_2024-05-22_platform_ad_budget_retention_opm_bridge_cleanup | 214270 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| None | 214270 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| None | 214270 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| None | 214270 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | True | True |
| TRG_R8L73-C26-214320-INNOCEAN-AD-AGENCY-OPERATING-LEVERAGE-WEAK | 214320 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | C26 should distinguish ad-agency campaign stability from true platform operating leverage. Innocean had limited MFE and later MAE; without client-budget, digital mix or margin revision evidence it should remain RiskWatch / no durable Green rather than Stage2. | True | True |
| V12_COMPACT_214320_2024-02-07_platform_ad_budget_retention_opm_bridge_cleanup | 214320 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| TR_C26_L105_214320_Stage2_20240530 | 214320 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| R8L95_C26_INNOCEAN_2024_STAGE2_ACTIONABLE_AD_AGENCY_PLATFORM_OPERATING_LEVERAGE_BRIDGE | 214320 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| T_C26_214320_STAGE2A_20240125 | 214320 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | None | False | True |
| None | 214320 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | None | False | True |
| TRG_R8L73-C26-214320-INNOCEAN-AD-AGENCY-OPERATING-LEVERAGE-WEAK | 214320 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | C26 should distinguish ad-agency campaign stability from true platform operating leverage. Innocean had limited MFE and later MAE; without client-budget, digital mix or margin revision evidence it should remain RiskWatch / no durable Green rather than Stage2. | True | True |
| T_C26_R8L106_06_214320_STAGE3YELLOW_Stage3Yellow_2024-05-17 | 214320 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_too_late_or_green_strictness_watch | True | True |
| TRG_R5L73-C18-214420-TONYMOLY-KBEAUTY-EXPORT-CHANNEL-REORDER | 214420 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | C18 should allow Stage2 when small-brand export/channel reorder connects to operating leverage, but should add local 4B-watch after a blowoff if reorder evidence stops refreshing. | True | True |
| TRG_R5L73-C18-214420-TONYMOLY-KBEAUTY-EXPORT-CHANNEL-REORDER | 214420 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | C18 should allow Stage2 when small-brand export/channel reorder connects to operating leverage, but should add local 4B-watch after a blowoff if reorder evidence stops refreshing. | True | True |
| TRG_R5L82-C18-214420-TONYMOLY-KBEAUTY-BRAND-THEME-SPIKE-FADE | 214420 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | C18 should not treat K-beauty brand/channel theme spikes as durable Stage2 unless export sell-through, channel restocking, repeat order cadence, revenue and margin bridge are visible. TonyMoly had large MFE but also sharp post-peak fade, so it is a theme-spike/local-4B boundary until direct channel proof is repaired. | True | True |
| None | 214420 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | True | True |
| C19_R5L120_05_214420_4B_Local_Watch_2024-05-10 | 214420 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | True | True |
| TRG_R5L80-C20-214420-TONYMOLY-BEAUTY-BRAND-GLOBAL-CHANNEL-LIFECYCLE | 214420 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | C20 should allow beauty-brand positives when global channel reorder, offline/online sell-through, product mix, revenue and margin bridge are visible. TonyMoly produced a very large MFE, but its post-peak drawdown requires lifecycle local 4B if sell-through or margin proof fades. | True | True |
| C20_R5L119_214420_20240510_05_Stage4B_Local_Watch | 214420 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | None | True | True |
| C20_R5_L102_T05_214420 | 214420 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | True | True |
| R5L100_C20_TONYMOLY_2024_STAGE4B_K_BEAUTY_GLOBAL_DISTRIBUTION_EVENT_CAP | 214420 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_4B_too_late_if_K_beauty_global_distribution_event_premium_not_capped | True | True |
| None | 214420 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| None | 214420 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| None | 214420 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | True | True |
| None | 214420 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | None | True | True |
| T_C03_R1L107_214430_20240305_STAGE2 | 214430 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | component_supplier_can_follow_export_theme_but_order_book_bridge_is_thin | True | True |
| T_C03_R1L108_214430_20240403_STAGE2 | 214430 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current profile can over-promote defense beta unless sovereign funded backlog, delivery schedule and margin/cash bridge are verified | True | True |
| R11L91_C03_I3SYSTEM_2024_STAGE2_FALSE_POSITIVE_IR_SENSOR_DEFENSE_THEME | 214430 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_false_positive_if_IR_sensor_defense_theme_counts_without_export_framework_backlog_bridge | True | True |
| R1L89_C03_214430_20240325_STAGE2_FALSE_POSITIVE_DEFENSE_SENSOR_THEME | 214430 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_false_positive_if_sensor_theme_spike_overcredited | True | True |
| None | 214430 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | None | False | True |
| R13L91_REVIEW_R11_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_214430_2024_03_25_TRIGGER | 214430 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive_if_IR_sensor_defense_theme_counts_without_export_framework_backlog_bridge | True | True |
| V12_COMPACT_214450_2024-02-02_MEDICAL_PRODUCT_REVENUE_REROUTE_CHECK | 214450 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive | True | True |
| None | 214450 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | False | True |
| R7L94_C25_PHARMARESEARCH_2024_STAGE2_ACTIONABLE_MEDICAL_AESTHETIC_EXPORT_MARGIN_BRIDGE | 214450 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R7L88_C25_PHARMARESEARCH_2024_STAGE2_ACTIONABLE_AESTHETIC_EXPORT_REORDER | 214450 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| TRG_R7L77-C25-214450-PHARMARESEARCH-AESTHETIC-MEDDEVICE-EXPORT-MARGIN | 214450 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | C25 should allow aesthetic/regenerative medical-device positives when export channel reorder, approval/registration visibility, pricing and margin bridge are visible. PharmaResearch produced very large MFE with almost no entry-basis MAE, but later price pinning and post-peak drawdown require lifecycle local 4B if export/margin evidence fades. | True | True |
| TRG_R7L77-C25-214450-PHARMARESEARCH-AESTHETIC-MEDDEVICE-EXPORT-MARGIN | 214450 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_correct | True | True |
| R7L83_C25_214450_20240401_STAGE2_AESTHETIC_EXPORT_BRIDGE | 214450 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_correct | True | True |
| V12_COMPACT_C25_R7L107_214450_20240603_Stage3_Yellow_214450_2024-06-03_Stage3-Yellow | 214450 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive | True | True |
| None | 214450 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | None | False | True |
| None | 214680 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | True | True |
| None | 214680 | C24_BIO_TRIAL_DATA_EVENT_RISK | C24 must require fresh binary/data endpoint quality; reroute commercialization, device, reimbursement, or price-only events to C23/C25/local_4B as appropriate. | True | True |
| TRG_R7L75-C25-214680-DRTECH-XRAY-DETECTOR-EXPORT-ORDER-BETA-FADE | 214680 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive | True | True |
| V12_COMPACT_C25_R7L107_214680_20240624_Local_4B_Watch_214680_2024-06-24_Local-4B-Watch | 214680 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive | True | True |
| TRG_R7L75-C25-214680-DRTECH-XRAY-DETECTOR-EXPORT-ORDER-BETA-FADE | 214680 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | C25 should not treat X-ray detector/export/OEM order beta as durable Stage2 unless named export orders, OEM channel expansion, reimbursement or margin bridge is visible. DRTech had tradable MFE but later drawdown opened enough to require local 4B-watch. | True | True |
| R7L94_C25_DRTECH_2024_STAGE4B_DIAGNOSTIC_IMAGING_DEVICE_EVENT_CAP | 214680 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_4B_too_late_if_diagnostic_imaging_device_event_premium_not_capped | True | True |
| None | 214680 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | None | True | True |
| R13_4B4C_L12_16_214680_20240226_4B_Local_Watch | 214680 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_source_proxy_row_promotes_to_green_or_full_4B | True | True |
| V12_COMPACT_R13L12_ACCT_PRICE_02_C25_214680_20240226_214680_2024-02-26_Stage4B | 214680 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | True | True |
| R13L94_REVIEW_R7_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_214680_2024_01_09_TRIGGER | 214680 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_4B_too_late_if_diagnostic_imaging_device_event_premium_not_capped | True | True |
| T_C03_R1L108_215090_20240226_STAGE4C | 215090 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current profile can over-promote defense beta unless sovereign funded backlog, delivery schedule and margin/cash bridge are verified | True | True |
| R13_4B4C_L12_01_215090_20240226_Stage4C_Watch | 215090 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_source_proxy_row_promotes_to_green_or_full_4B | True | True |
| R13_CROSS_215090_2024-02-26_Stage4C | 215090 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | True | True |
| None | 215090 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | True | True |
| R9L85_C29_215360_20240401_STAGE2_FALSE_POSITIVE_EV_THERMAL_THEME | 215360 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive_if_EV_parts_theme_overcredited | True | True |
| R13L85_REVIEW_R9_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_215360_2024-04-01 | 215360 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| TRG_R7L76-C24-215600-SILLAJEN-ONCOLOGY-TRIAL-DATA-POST-CA-BETA-FADE | 215600 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_false_positive | True | True |
| None | 215600 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | False | True |
| TRG_R7L76-C24-215600-SILLAJEN-ONCOLOGY-TRIAL-DATA-POST-CA-BETA-FADE | 215600 | C24_BIO_TRIAL_DATA_EVENT_RISK | C24 should not treat oncology-trial or financing/post-CA bio beta as durable Stage2 unless endpoint quality, safety, regulatory path, financing runway and commercialization bridge are visible. SillaJen had only a small MFE after the post-CA entry and then opened a high-MAE decline. | True | True |
| C24_R7L98_TRIG_08_215600 | 215600 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_false_positive | True | True |
| R7L98_C24_SILLAJEN_2024_STAGE4B_ONCOLYTIC_VIRUS_TRIAL_EVENT_CAP | 215600 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_4B_too_late_if_oncology_trial_event_premium_not_capped | True | True |
| V12_COMPACT_216050_2024-03-22_platform_ad_budget_retention_opm_bridge_cleanup | 216050 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| None | 216050 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | None | False | True |
| R8L89_C26_INCROSS_2024_STAGE2_FALSE_POSITIVE_ADTECH_RECOVERY | 216050 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive_if_adtech_theme_counts_without_revenue_margin_bridge | True | True |
| T_C26_R8L106_03_216050_STAGE2ACTIONABLE_Stage2Actionable_2024-03-14 | 216050 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_data_insufficient | True | True |
| R8L88_C26_216050_20240111_STAGE2_FALSE_POSITIVE_LEGACY_AD_PLATFORM | 216050 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive_if_legacy_ad_platform_rebound_overcredited | True | True |
| R13L88_REVIEW_R8_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_216050_2024-01-11 | 216050 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| V12_COMPACT_R13L2_C26_216050_20240109_STAGE2_216050_2024-01-09_cross_archetype_high_MAE_guardrail_review | 216050 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| T_R13_STAGE2FP_L6_216050_Stage2_2024-01-09 | 216050 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_stage2_false_positive_or_overpromotion_risk | True | True |
| R13_CROSS_216050_2024-01-09_Stage2 | 216050 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive | True | True |
| TRG_C06_R2_L109_217190_20240322_EMI_SHIELD_HBM_LABEL_FALSE_YELLOW | 217190 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_false_positive | True | True |
| R2L91_C07_217190_20240124_STAGE2_FALSE_POSITIVE_BACKEND_HBM_POSTPROCESS | 217190 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_false_positive_if_backend_equipment_rebound_overcredited | True | True |
| None | 217190 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | False | True |
| TRG_C11_R3L105_001 | 217820 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_missed_structural | True | True |
| R3L98-C14-001-T1 | 217820 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_false_positive_if_equipment_label_spike_overrides_EV_demand_reset | True | True |
| R13HMG_L104_T006_217820 | 217820 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive_or_late_4B_4C_under_high_MAE | True | True |
| R11L90_C03_218410_20240122_STAGE2_FALSE_POSITIVE_RF_DEFENSE_THEME | 218410 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_false_positive_if_RF_defense_theme_overcredited | True | True |
| TIGERELEC_219130_2024_03_06_STAGE2_FALSE_POSITIVE_TEST_PCB_SOCKET | 219130 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_false_positive | False | True |
| R2L93C_C08_219130_20240213_STAGE2_TESTBOARD_REPEAT | 219130 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_correct_if_customer_qualification_repeat_demand_margin_cash_bridge_required_but_Green_strict | True | True |
| R13_L106_T04_219130 | 219130 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_4B_too_late | True | True |
| TRG_R7L78-C24-220100-FUTURECHEM-RADIOPHARMA-TRIAL-DATA | 220100 | C24_BIO_TRIAL_DATA_EVENT_RISK | C24 should preserve radiopharma positives when clinical-data quality, regulatory path, patient enrollment, partner/commercial route and financing bridge are visible. FutureChem produced very large MFE with controlled entry-basis MAE, but post-peak volatility still requires lifecycle local 4B if data/commercial bridge decays. | True | True |
| None | 220260 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_4B_too_late_if_early_MFE_fade_ignored | True | True |
| None | 220260 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_4B_too_late_if_customer_registration_proxy_keeps_Actionable_after_fade | True | True |
| R5L96_C18_COSMAXNBT_2024_STAGE2_FALSE_POSITIVE_HEALTH_FUNCTIONAL_EXPORT_CHANNEL_WATCH | 222040 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive_if_health_functional_export_channel_watch_counts_without_reorder_sellthrough_margin_revision_bridge | True | True |
| R13L96_REVIEW_R5_C18_CONSUMER_EXPORT_CHANNEL_REORDER_222040_2024_01_09_TRIGGER | 222040 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_health_functional_export_channel_watch_counts_without_reorder_sellthrough_margin_revision_bridge | True | True |
| TRG_R3L74-C11-222080-CIS-EQUIPMENT-CAPEX-BETA-FADE | 222080 | C11_BATTERY_ORDERBOOK_RERATING | C11 should not treat battery equipment or solid-state capex beta as durable Stage2 unless orderbook, delivery, customer or margin evidence refreshes. CIS generated a sharp MFE but later gave it back and opened large MAE, making it a false Stage2 / local 4B-watch row. | True | True |
| CIS_222080_2024_03_05_STAGE2_FALSE_POSITIVE_ORDERBOOK_SPIKE | 222080 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive | False | True |
| None | 222080 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_missed_actionable_if_equipment_orderbook_is_zeroed_but_correct_to_block_Green_without_margin_bridge | True | True |
| R3L89_C11_222080_20240215_STAGE2_BATTERY_EQUIPMENT_ORDERBOOK | 222080 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_correct_if_orderbook_customer_ramp_margin_bridge_required | True | True |
| TRG_R3L74-C11-222080-CIS-EQUIPMENT-CAPEX-BETA-FADE | 222080 | C11_BATTERY_ORDERBOOK_RERATING | C11 should not treat battery equipment or solid-state capex beta as durable Stage2 unless orderbook, delivery, customer or margin evidence refreshes. CIS generated a sharp MFE but later gave it back and opened large MAE, making it a false Stage2 / local 4B-watch row. | True | True |
| T_C11_R3L107_222080_STAGE4B_20240312 | 222080 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive_if_orderbook_label_is_overcredited | True | True |
| None | 222080 | C11_BATTERY_ORDERBOOK_RERATING | None | True | True |
| None | 222080 | C11_BATTERY_ORDERBOOK_RERATING | None | True | True |
| V12_COMPACT_C12_R3L105_222080_20240416_12_222080_2024-04-16_Local-4B-Watch | 222080 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_false_positive | True | True |
| None | 222080 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | True | True |
| None | 222080 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | True | True |
| T_C13_R3L105_222080_STAGE4B_20240312 | 222080 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | True | True |
| R9L93_C14_CIS_2024_STAGE2_FALSE_POSITIVE_BATTERY_EQUIPMENT_CAPEX_REBOUND | 222080 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_false_positive_if_battery_equipment_capex_rebound_counts_without_customer_delivery_margin_bridge | True | True |
| R13L93_REVIEW_R9_C14_EV_DEMAND_SLOWDOWN_4B_4C_222080_2024_03_05_TRIGGER | 222080 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_battery_equipment_capex_rebound_counts_without_customer_delivery_margin_bridge | True | True |
| TRG_R2L75-C06-222800-SIMMTECH-DDR5-HBM-SUBSTRATE-CYCLE-FADE | 222800 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_false_positive | True | True |
| TRG-C06-L110-222800-Stage2Actionable-2024-03-22 | 222800 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_missed_structural | True | True |
| TRG_R2L75-C06-222800-SIMMTECH-DDR5-HBM-SUBSTRATE-CYCLE-FADE | 222800 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | C06 should not reward memory substrate restocking beta unless customer order, utilization, ASP or margin bridge is visible. Simmtech produced only moderate MFE and then a deep late-2024 drawdown, so it belongs in false Stage2/local 4B-watch until bridge evidence is repaired. | True | True |
| R2L93_C06_222800_20240102_STAGE2_FALSE_POSITIVE_PCB_SUBSTRATE_CAPACITY | 222800 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_false_positive_if_PCB_substrate_capacity_vocabulary_counted_as_C06_memory_capacity_bridge | True | True |
| None | 222800 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | False | True |
| TRG_R8L78-C27-225570-NEXON-GAMES-GLOBAL-LAUNCH-LIVEOPS | 225570 | C27_CONTENT_IP_GLOBAL_MONETIZATION | C27 should allow game-IP launch positives when global launch, user traction, live-ops retention, monetization and operating-leverage bridge are visible. Nexon Games produced large MFE, but the later post-peak drawdown means user/revenue/retention evidence must refresh. Share-count changes inside the window need validation. | True | True |
| TRG_R8L74-C27-225570-NEXONGAMES-GLOBAL-LAUNCH-RETENTION-LIFECYCLE | 225570 | C27_CONTENT_IP_GLOBAL_MONETIZATION | C27 should allow a global launch name only if launch traction converts into retention, paying-user monetization, live-ops cadence and revenue bridge. Nexon Games produced a huge launch-window MFE, but later drawdown makes lifecycle local 4B mandatory unless retention/monetization evidence refreshes. | True | True |
| TRG_R8L74-C27-225570-NEXONGAMES-GLOBAL-LAUNCH-RETENTION-LIFECYCLE | 225570 | C27_CONTENT_IP_GLOBAL_MONETIZATION | C27 should allow a global launch name only if launch traction converts into retention, paying-user monetization, live-ops cadence and revenue bridge. Nexon Games produced a huge launch-window MFE, but later drawdown makes lifecycle local 4B mandatory unless retention/monetization evidence refreshes. | True | True |
| C27-R8L105-019|Stage4B|2024-07-05 | 225570 | C27_CONTENT_IP_GLOBAL_MONETIZATION | residual_error_needs_C27_specific_bridge_or_guard | True | True |
| V12_COMPACT_R13L12_ACCT_PRICE_16_C27_225570_20240703_225570_2024-07-03_Stage4B | 225570 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | True | True |
| R13_CROSS_225570_2024-07-03_Stage4B | 225570 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| None | 226400 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | None | True | True |
| R13_CROSS_226400_2024-07-01_Stage2-Actionable-OrthopedicExportBridge | 226400 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive | True | True |
| None | 228670 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | None | False | True |
| R7L88_C25_RAY_2024_STAGE2_FALSE_POSITIVE_DENTAL_EXPORT_REBOUND | 228670 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive_if_dental_device_export_rebound_counts_without_order_reimbursement_margin_bridge | True | True |
| R7L94_C25_RAY_2024_STAGE2_FALSE_POSITIVE_DENTAL_DEVICE_EXPORT_RECOVERY | 228670 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive_if_dental_device_export_recovery_counts_without_channel_margin_revision_bridge | True | True |
| R7L83_C25_228670_20240401_STAGE2_FALSE_POSITIVE_DENTAL_DEVICE | 228670 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive | True | True |
| R7L86_C25_228670_20240108_STAGE2_FALSE_POSITIVE_DENTAL_EXPORT_THEME | 228670 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive_if_device_export_theme_overcredited | True | True |
| R13L86_REVIEW_R7_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_228670_2024-01-08 | 228670 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| V12_COMPACT_R13L11-4B4C-001_228670_2024-01-02_cross_archetype_4b_4c_boundary_retest | 228670 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R13L83_HIGHMAE_REVIEW_228670_2024-04-01 | 228670 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| V12_COMPACT_R13L2_C25_228670_20240102_STAGE2_228670_2024-01-02_cross_archetype_high_MAE_guardrail_review | 228670 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| R13_CROSS_228670_2024-01-02_Stage2 | 228670 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| R13L94_REVIEW_R7_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_228670_2024_01_24_TRIGGER | 228670 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive_if_dental_device_export_recovery_counts_without_channel_margin_revision_bridge | True | True |
| T_R13_STAGE2FP_L6_228670_Stage2FalsePositive_2024-01-02 | 228670 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_stage2_false_positive_or_overpromotion_risk | True | True |
| V12_COMPACT_C25_R7L107_228850_20240722_Stage2_228850_2024-07-22_Stage2 | 228850 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive | True | True |
| R7L91_C23_229000_20240102_STAGE2_FALSE_POSITIVE_DIAGNOSTIC_COMMERCIALIZATION | 229000 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive_if_diagnostic_commercialization_vocabulary_overcredited | True | True |
| R11L89_C02_229640_20240422_STAGE2_POWER_CABLE_EXPORT_GRID | 229640 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_correct_if_orderbook_export_margin_cash_bridge_required | True | True |
| R4L99_C16_LSECOENERGY_2024_STAGE2_ACTIONABLE_CRITICAL_MINERAL_CABLE_SUPPLY_CHAIN_EXECUTION | 229640 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R8L88_C26_230360_20240314_STAGE2_PERFORMANCE_MARKETING_LEVERAGE | 230360 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_correct_if_revenue_margin_retention_bridge_required | True | True |
| V12_COMPACT_230360_2024-06-10_platform_ad_budget_retention_opm_bridge_cleanup | 230360 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| R8L83_C26_230360_20240411_STAGE2_FALSE_POSITIVE_PERFORMANCE_MARKETING_RECOVERY | 230360 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| None | 230360 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | None | False | True |
| R13_4B4C_L101_T004_230360 | 230360 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_missed_structural | True | True |
| R13L88_REVIEW_R8_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_230360_2024-03-14 | 230360 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_correct | True | True |
| T_C06_R2L103_232140_20240415_Stage2Actionable_CROSS_C07 | 232140 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_needs_C06_vs_C07_C08_C09_reroute_guard | True | True |
| TRG_C06_R2_L109_232140_20240610_LATE_TESTER_HBM_CAPACITY_LABEL_4B | 232140 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_4B_too_late | True | True |
| TRG_R2L80-C07-232140-YC-HBM-TEST-EQUIPMENT-CUSTOMER-ORDER-RS | 232140 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | C07 should preserve memory-test equipment positives when relative strength is backed by customer order quality, HBM capacity expansion, delivery cadence, revenue conversion and margin bridge. YC produced explosive MFE but later drawdown requires lifecycle treatment and source repair. | True | True |
| R2L90_C07_YC_2024_STAGE2_ACTIONABLE_HBM_TEST_EQUIPMENT_ORDER_RS | 232140 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| V12_COMPACT_232140_2024-04-15_Stage2-Actionable | 232140 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_false_positive | True | True |
| TRG_R2L77-C07-232140-YC-HBM-TESTER-ORDER-RS-LIFECYCLE | 232140 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | C07 should allow HBM/AI tester equipment winners when relative strength connects to customer capex, tester order, delivery backlog and margin bridge. YC/YIK produced extreme MFE with controlled entry-basis MAE, but the post-peak drawdown requires lifecycle local 4B if order/backlog/margin evidence fades. | True | True |
| TRG_R2L77-C07-232140-YC-HBM-TESTER-ORDER-RS-LIFECYCLE | 232140 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_correct | True | True |
| R2L84_C07_232140_20240417_STAGE2_HBM_TESTER_ORDER_BRIDGE | 232140 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_correct_if_non_price_bridge_required | True | True |
| R2L87_C08_232140_20240228_STAGE2_MEMORY_TESTER_CUSTOMER_QUALITY | 232140 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_correct_if_customer_quality_shipment_bridge_required | True | True |
| YC_232140_2024_03_06_STAGE2A_MEMORY_TESTER_CUSTOMER_QUALITY | 232140 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_4B_too_late | False | True |
| None | 232140 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | False | True |
| C08_R2_L112_001_232140_Stage3_Yellow | 232140 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_missed_structural | True | True |
| None | 232140 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | False | True |
| T_C09_R2L111_04_232140_20240415 | 232140 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_false_positive | True | True |
| R2L95_C10_YC_2024_STAGE2_ACTIONABLE_MEMORY_TESTER_ORDER_CYCLE_BRIDGE | 232140 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R13L87_REVIEW_R2_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_232140_2024-02-28 | 232140 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_correct | True | True |
| V12_COMPACT_C28_R8L104_234300_20240620_234300_2024-06-21_Stage2 | 234300 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive | True | True |
| V12_COMPACT_R13_STAGE2FP_L8_10_234300_2024-06-21_STAGE2_234300_2024-06-21_stage2_source_proxy_deep_MAE_false_positive_review | 234300 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive | True | True |
| C24_R7L98_TRIG_07_235980 | 235980 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_false_positive | True | True |
| C24-R7-L100-TRIG-06-235980 | 235980 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_4C_too_late | True | True |
| R13_4B4C_L101_T007_235980 | 235980 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R8L95_C26_NBT_2024_STAGE2_FALSE_POSITIVE_REWARD_AD_PLATFORM_WATCH | 236810 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive_if_reward_ad_platform_watch_counts_without_ad_budget_retention_margin_revision_bridge | True | True |
| None | 236810 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | None | False | True |
| TRG_R8L81-C26-236810-NBT-REWARD-AD-PLATFORM-THEME-FADE | 236810 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | C26 should not treat reward-ad or mobile-ad platform theme beta as durable Stage2 unless advertiser budget, DAU/MAU or conversion metrics, retention, revenue conversion and margin bridge are visible. NBT had a small/medium MFE and then a severe high-MAE fade. | True | True |
| R8L91_C26_236810_20240103_STAGE2_FALSE_POSITIVE_REWARD_ADTECH | 236810 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive_if_reward_adtech_spike_overcredited | True | True |
| V12_COMPACT_236810_2024-05-02_platform_ad_budget_retention_opm_bridge_cleanup | 236810 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| R13L95_REVIEW_R8_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_236810_2024_01_08_TRIGGER | 236810 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_reward_ad_platform_watch_counts_without_ad_budget_retention_margin_revision_bridge | True | True |
| V12_COMPACT_237690_2024-02-05_RNA_CDMO_APPROVAL_CONTAMINANT_REROUTE | 237690 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive | True | True |
| R7L90_C24_237690_20240223_STAGE2_RNA_PLATFORM_BRIDGE | 237690 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_correct_if_endpoint_partner_manufacturing_cash_bridge_required | True | True |
| None | 237690 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | False | True |
| R1L95_C02_PNCTECH_2024_STAGE2_FALSE_POSITIVE_GRID_AUTOMATION_CAPEX_WATCH | 237750 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_false_positive_if_grid_automation_capex_watch_counts_without_customer_order_delivery_margin_revision_bridge | True | True |
| R1L92_C02_237750_20240102_STAGE2_FALSE_POSITIVE_DIGITAL_GRID_RELAY | 237750 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_false_positive_if_digital_grid_price_MFE_overcredited | True | True |
| R2L92_C08_237750_20240102_STAGE2_FALSE_POSITIVE_CROSSLABEL_GRID_MFE | 237750 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_false_positive_if_cross_label_price_MFE_overcredited | True | True |
| R13L95_REVIEW_R1_C02_POWER_GRID_DATACENTER_CAPEX_237750_2024_05_08_TRIGGER | 237750 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_grid_automation_capex_watch_counts_without_customer_order_delivery_margin_revision_bridge | True | True |
| None | 237820 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | None | False | True |
| TRG_R8L77-C26-237820-PLAYD-ADTECH-ROAS-BUDGET-OPERATING-LEVERAGE | 237820 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | C26 should allow adtech/platform positives only when advertiser budget recovery, ROAS/performance evidence, media-buying platform revenue and operating leverage bridge are visible. PlayD produced very large MFE with controlled entry-basis MAE, but the later post-peak drawdown requires lifecycle local 4B if ad-budget/ROAS/margin evidence fades. | True | True |
| TRG_R8L77-C26-237820-PLAYD-ADTECH-ROAS-BUDGET-OPERATING-LEVERAGE | 237820 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_correct | True | True |
| TRG_R8L81-C26-237820-PLAYD-PERFORMANCE-AD-AI-MARKETING-LIFECYCLE | 237820 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | C26 should allow adtech/performance-marketing positives only when AI/digital ad attention maps to client budget, conversion metrics, recurring advertiser spend, revenue conversion and margin bridge. PlayD produced a very large MFE but later post-peak drawdown demands lifecycle 4B if the bridge fades. | True | True |
| R8L99_C26_PLAYD_2024_STAGE4B_DIGITAL_ADTECH_EVENT_CAP | 237820 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_4B_too_late_if_digital_adtech_event_premium_not_capped | True | True |
| V12_COMPACT_237820_2024-04-11_platform_ad_budget_retention_opm_bridge_cleanup | 237820 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| R5L98_C20_CLIO_2024_STAGE2_FALSE_POSITIVE_MASS_COSMETIC_CHANNEL_MARGIN_WATCH | 237880 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive_if_cosmetic_channel_watch_counts_without_sellthrough_reorder_inventory_margin_revision_bridge | True | True |
| R5L88_C20_237880_20240613_STAGE2_FALSE_POSITIVE_LATE_BRAND_EXTENSION | 237880 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive_if_late_brand_extension_overcredited | True | True |
| R13L88_REVIEW_R5_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_237880_2024-06-13 | 237880 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| V12_COMPACT_240810_2024-02-01_Stage2 | 240810 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_false_positive | True | True |
| R2L86_C07_240810_20240704_STAGE2_FALSE_POSITIVE_MEMORY_EQUIPMENT_BETA | 240810 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_false_positive_if_memory_equipment_beta_overcredited | True | True |
| R2_L110_C07 | 240810 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | None | True | True |
| None | 240810 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | False | True |
| TRG_R2L79-C09-240810-WONIKIPS-ADVANCED-EQUIPMENT-ORDER-QUALITY-POSITIVE | 240810 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | C09 should not block advanced-equipment positives when customer quality, tool order/backlog, delivery schedule, utilization/customer capacity and margin bridge are visible. Wonik IPS produced a meaningful MFE with bounded MAE, so it is a protected candidate after source repair rather than a pure blowoff. | True | True |
| R2L93C_C09_240810_20240229_STAGE2_FRONTEND_ORDER | 240810 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_correct_if_order_delivery_revision_margin_cash_bridge_required_but_Green_strict | True | True |
| R2L83_C09_240810_20240229_STAGE2_ACTIONABLE_THEN_4B_WATCH | 240810 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_4B_too_late | True | True |
| TRG_R2L82-C09-240810-WONIK-IPS-SEMICAP-ORDER-BRIDGE-LIFECYCLE | 240810 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | C09 should not mechanically reject all advanced-equipment MFE. Wonik IPS had a credible semicap/order-cycle price path, but promotion requires memory capex, customer order, delivery/revenue and margin evidence; later drawdown requires lifecycle 4B if bridge fades. | True | True |
| TRG_R2L76-C10-240810-WONIK-IPS-MEMORY-PROCESS-EQUIPMENT-CYCLE | 240810 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | C10 should preserve process-equipment recovery winners when memory capex/order recovery, customer schedule and margin bridge are visible. Wonik IPS produced a strong early MFE with moderate MAE, then faded, so C10 needs lifecycle local 4B after bridge decay. | True | True |
| None | 240810 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | None | True | True |
| TRG_R2L76-C10-240810-WONIK-IPS-MEMORY-PROCESS-EQUIPMENT-CYCLE | 240810 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_correct | True | True |
| R13_CROSS_240810_2024-02-29_Stage2-Actionable | 240810 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_false_positive | True | True |
| WONIKIPS_240810_2024_03_06_STAGE2A_MEMORY_WFE_RECOVERY | 240810 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_4B_too_late | False | True |
| R13L86_REVIEW_R2_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_240810_2024-07-04 | 240810 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| None | 240810 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| None | 240810 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | None | True | True |
| TRG_R1L83-C01-241560-DOOSAN-BOBCAT-EQUIPMENT-CYCLE-FADE | 241560 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | C01 should not treat construction-equipment backlog/cycle beta as durable Stage2 unless dealer channel inventory, rental demand, production scheduling, revenue conversion and margin bridge are visible. Doosan Bobcat had modest MFE and then high MAE, so it is local 4B-watch unless the bridge is repaired. | True | True |
| TRG_R1L79-C01-241560-DOOSAN-BOBCAT-CONSTRUCTION-EQUIPMENT-BACKLOG-FADE | 241560 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | C01 should not treat construction-equipment backlog/channel beta as durable Stage2 unless dealer inventory, order intake, utilization, pricing and margin bridge refreshes. Doosan Bobcat had a modest MFE and then a high-MAE drawdown, making it a local 4B-watch row. | True | True |
| R1L116-C01-006 | 241560 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_false_positive_if_legacy_backlog_ignores_cycle_slowdown | True | True |
| TRG_R12L73-C32-241560-DOOSANBOBCAT-MERGER-RATIO-MINORITY-RISK | 241560 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should not treat a chaebol restructuring headline as positive control-premium evidence for the operating subsidiary when merger-ratio and minority-shareholder dilution risk dominate. Bobcat showed a brief squeeze but then opened deep MAE. | False | True |
| TRG_R12L73-C32-241560-DOOSANBOBCAT-MERGER-RATIO-MINORITY-RISK | 241560 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should not treat a chaebol restructuring headline as positive control-premium evidence for the operating subsidiary when merger-ratio and minority-shareholder dilution risk dominate. Bobcat showed a brief squeeze but then opened deep MAE. | False | True |
| R5L93_C19_HWASEUNGENTERPRISE_2024_STAGE2_ACTIONABLE_FOOTWEAR_OEM_INVENTORY_RESTOCKING_MARGIN | 241590 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| TRG_R5L82-C18-241710-COSMECCA-KOREA-ODM-EXPORT-REORDER | 241710 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | C18 should protect ODM/export positives only when export channel sell-through, customer quality, reorder cadence, revenue conversion and margin bridge are visible. Cosmecca Korea produced very large MFE with moderate interim MAE, but later drawdown requires lifecycle 4B if channel/reorder proof fades. | True | True |
| None | 241770 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | False | True |
| None | 241840 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | None | False | True |
| R8L90_C27_241840_20240102_STAGE2_FALSE_POSITIVE_DRAMA_IP | 241840 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_false_positive_if_drama_IP_rebound_overcredited | True | True |
| R3L97_C12_SHINHEUNGSEC_2024_STAGE2_FALSE_POSITIVE_BATTERY_CAP_CALLOFF_WATCH_POST_CA | 243840 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_false_positive_if_battery_cap_calloff_watch_counts_without_customer_calloff_delivery_utilization_margin_revision_bridge | True | True |
| T_C13_R3L103_243840_STAGE2ACTIONABLE_20240522 | 243840 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_too_late_if_safety_component_volume_margin_bridge_exists | True | True |
| R9L89_C13_SHINHEUNG_2024_STAGE2_FALSE_POSITIVE_BATTERY_PARTS_UTILIZATION | 243840 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_false_positive_if_battery_parts_utilization_theme_counts_without_customer_margin_bridge | True | True |
| R13L89_REVIEW_C13_SHINHEUNG_2024_STAGE2_FALSE_POSITIVE_BATTERY_PARTS_UTILIZATION | 243840 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive_if_battery_parts_utilization_theme_counts_without_customer_margin_bridge | True | True |
| R6L95_C22_APLUSASSET_2024_STAGE2_FALSE_POSITIVE_INSURANCE_AGENCY_COMMISSION_WATCH | 244920 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive_if_insurance_agency_commission_watch_counts_without_persistency_margin_capital_return_revision_bridge | True | True |
| R6L88_C22_244920_20240520_STAGE2_FALSE_POSITIVE_INSURANCE_DISTRIBUTION | 244920 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive_if_distribution_theme_overcredited | True | True |
| R13L88_REVIEW_R6_C22_INSURANCE_RATE_CYCLE_RESERVE_244920_2024-05-20 | 244920 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R13L95_REVIEW_R6_C22_INSURANCE_RATE_CYCLE_RESERVE_244920_2024_05_17_TRIGGER | 244920 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_insurance_agency_commission_watch_counts_without_persistency_margin_capital_return_revision_bridge | True | True |
| R7L91_C25_TNRBIOFAB_2024_STAGE4B_BIOPRINTING_REGENERATIVE_DEVICE_CAP | 246710 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_4B_too_late_if_bioprinting_regenerative_device_event_premium_not_capped | True | True |
| R13L91_REVIEW_R7_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_246710_2024_03_11_TRIGGER | 246710 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_4B_too_late_if_bioprinting_regenerative_device_event_premium_not_capped | True | True |
| R3L85_C11_247540_20240325_STAGE2_FALSE_POSITIVE_CATHODE_ORDERBOOK | 247540 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive_if_orderbook_headline_overcredited | True | True |
| T_C11_R3L107_247540_STAGE4C_20240122 | 247540 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive_if_orderbook_label_is_overcredited | True | True |
| V12_COMPACT_C12_R3L105_247540_20240409_03_247540_2024-04-09_Stage4C | 247540 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_false_positive | True | True |
| None | 247540 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | False | True |
| None | 247540 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | True | True |
| T_C13_R3L105_247540_STAGE4C_20240122 | 247540 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | True | True |
| None | 247540 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | False | True |
| R3L98_C14_ECOPROBM_2024_STAGE4C_CATHODE_DEMAND_SLOWDOWN_CALL_OFF_PROTECTION | 247540 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_kept_but_hard_4C_watch_should_block_positive_stage | True | True |
| R3L98-C14-007-T1 | 247540 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_false_positive_if_contract_size_memory_blocks_late_cycle_4C | True | True |
| None | 247540 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| V12_COMPACT_R13L12_ACCT_PRICE_08_C31_247540_20240122_247540_2024-01-22_Stage2 | 247540 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | True | True |
| R13_CROSS_247540_2024-01-22_Stage2 | 247540 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| R13L85_REVIEW_R3_C11_BATTERY_ORDERBOOK_RERATING_247540_2024-03-25 | 247540 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| None | 247540 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | True | True |
| T_R13_STAGE2FP_L6_247540_Stage2_2024-01-22 | 247540 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_stage2_false_positive_or_overpromotion_risk | True | True |
| None | 248170 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | True | True |
| R5L89_C18_248170_20240620_STAGE2_FALSE_POSITIVE_SAUCE_EXPORT_THEME | 248170 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive_if_sauce_export_theme_overcredited | True | True |
| R5_L122_C18_012 | 248170 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | True | True |
| C19_R5L119_08_248170_4B_Local_Watch_2024-03-21 | 248170 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | True | True |
| C20_R5L117_248170_20240321_Stage4B | 248170 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_error_or_stress_case | True | True |
| R8L87_C27_251270_20240429_STAGE2_GAME_IP_GLOBAL_MONETIZATION | 251270 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_correct_if_IP_launch_monetization_bridge_required | True | True |
| None | 251270 | C27_CONTENT_IP_GLOBAL_MONETIZATION | None | True | True |
| R13L87_REVIEW_R8_C27_CONTENT_IP_GLOBAL_MONETIZATION_251270_2024-04-29 | 251270 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_correct | True | True |
| R3L98-C14-004-T1 | 251630 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_missed_structural_if_all_battery_equipment_is_blocked_by_generic_EV_slowdown | True | True |
| SEMCNS_252990_2024_01_23_STAGE2A_PROBE_CARD_CERAMIC_STF | 252990 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_correct | False | True |
| SEMCNS_252990_2024_03_06_STAGE2A_PROBE_CARD_CUSTOMER_QUALITY | 252990 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_4B_too_late | False | True |
| C08_R2_L112_007_252990_Stage4C | 252990 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_4C_too_late | True | True |
| None | 253450 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | None | False | True |
| R8L93_C27_253450_20240102_STAGE2_FALSE_POSITIVE_STUDIO_PIPELINE | 253450 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_false_positive_if_studio_content_pipeline_vocabulary_overcredited | True | True |
| None | 253450 | C27_CONTENT_IP_GLOBAL_MONETIZATION | None | True | True |
| R2L91_C06_NEOSEM_2024_STAGE4B_CXL_SSD_MEMORY_THEME_CAP | 253590 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_4B_too_late_if_CXL_SSD_memory_theme_premium_not_capped | True | True |
| R2L94_C07_NEOSEM_2024_STAGE2_FALSE_POSITIVE_MEMORY_TESTER_HEADLINE | 253590 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_false_positive_if_memory_tester_headline_counts_without_customer_order_delivery_margin_bridge | True | True |
| NEOSEM_253590_2024_03_06_STAGE2_FALSE_POSITIVE_SSD_TESTER_EVENT | 253590 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_false_positive | False | True |
| R2L88_C09_253590_20240704_STAGE2_FALSE_POSITIVE_LATE_TESTER_EXTENSION | 253590 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_false_positive_if_late_tester_extension_overcredited | True | True |
| R13L88_REVIEW_R2_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_253590_2024-07-04 | 253590 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| None | 253590 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| R13L91_REVIEW_R2_C06_HBM_MEMORY_CUSTOMER_CAPACITY_253590_2024_07_04_TRIGGER | 253590 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_4B_too_late_if_CXL_SSD_memory_theme_premium_not_capped | True | True |
| R13L94_REVIEW_R2_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_253590_2024_03_20_TRIGGER | 253590 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive_if_memory_tester_headline_counts_without_customer_order_delivery_margin_bridge | True | True |
| None | 253840 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | True | True |
| None | 253840 | C24_BIO_TRIAL_DATA_EVENT_RISK | C24 must require fresh binary/data endpoint quality; reroute commercialization, device, reimbursement, or price-only events to C23/C25/local_4B as appropriate. | True | True |
| None | 253840 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | None | True | True |
| V12_COMPACT_R13L11-4B4C-010_253840_2024-01-25_cross_archetype_4b_4c_boundary_retest | 253840 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R13_4B4C_L12_10_253840_20240125_4B_Local_Watch | 253840 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_source_proxy_row_promotes_to_green_or_full_4B | True | True |
| None | 253840 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| V12_COMPACT_R13L12_ACCT_PRICE_03_C25_253840_20240125_253840_2024-01-25_Stage4B | 253840 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | True | True |
| R13_CROSS_253840_2024-01-25_Stage4B-Local | 253840 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | True | True |
| None | 253840 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | True | True |
| R2L98_C06_MIRAESCM_2024_STAGE4B_MEMORY_DISTRIBUTION_HBM_EVENT_CAP | 254490 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_4B_too_late_if_memory_distribution_HBM_event_premium_not_capped | True | True |
| R7L90_C24_256840_20240320_STAGE2_FALSE_POSITIVE_THERAPEUTIC_EVENT | 256840 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_false_positive_if_therapeutic_event_momentum_overcredited | True | True |
| None | 257720 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | None | False | True |
| C20_R5_L102_T01_257720 | 257720 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_4B_too_late | True | True |
| None | 257720 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | None | False | True |
| None | 257720 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | None | False | True |
| R13_4B4C_L101_T002_257720 | 257720 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late_after_blowoff_not_false_positive_upfront | True | True |
| R13_4B4C_L12_14_257720_20240612_4B_Local_Watch | 257720 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_source_proxy_row_promotes_to_green_or_full_4B | True | True |
| None | 257720 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| R13_CROSS_R13L4_C20_257720_20240612_INVENTORY_AR_TRUST_GUARD_257720_2024-06-12_Stage4B | 257720 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | True | True |
| None | 257720 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | True | True |
| V12_COMPACT_R13L2_C20_257720_20240612_STAGE4B_257720_2024-06-12_cross_archetype_high_MAE_guardrail_review | 257720 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| V12_COMPACT_C28_R8L104_258790_20240226_258790_2024-02-27_Stage2 | 258790 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive | True | True |
| V12_COMPACT_R13_STAGE2FP_L8_03_258790_2024-02-27_STAGE2_258790_2024-02-27_stage2_source_proxy_deep_MAE_false_positive_review | 258790 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive | True | True |
| TRG_R8L80-C27-259960-KRAFTON-GAME-IP-GLOBAL-LIVEOPS-MONETIZATION | 259960 | C27_CONTENT_IP_GLOBAL_MONETIZATION | C27 should protect game-IP positives only when global live-ops, user metrics, monetization, publishing cadence, revenue conversion and margin bridge are visible. Krafton produced strong MFE with almost no entry-basis MAE, so it should not be overblocked after source repair. | True | True |
| TRG_R8L74-C27-259960-KRAFTON-PUBG-GLOBAL-MONETIZATION | 259960 | C27_CONTENT_IP_GLOBAL_MONETIZATION | C27 should allow Stage2 when global game IP monetization is tied to live-ops, regional monetization, MAU/ARPU and margin bridge. Krafton produced a large, low-MAE rerating path; this is a positive anchor that should not be overblocked by generic content-beta guards. | True | True |
| TRG_R8L74-C27-259960-KRAFTON-PUBG-GLOBAL-MONETIZATION | 259960 | C27_CONTENT_IP_GLOBAL_MONETIZATION | C27 should allow Stage2 when global game IP monetization is tied to live-ops, regional monetization, MAU/ARPU and margin bridge. Krafton produced a large, low-MAE rerating path; this is a positive anchor that should not be overblocked by generic content-beta guards. | True | True |
| KRAFTON_259960_2024_02_13_STAGE2A_GAME_IP_GLOBAL_MONETIZATION | 259960 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_4B_too_late | False | True |
| None | 259960 | C27_CONTENT_IP_GLOBAL_MONETIZATION | None | True | True |
| None | 259960 | C27_CONTENT_IP_GLOBAL_MONETIZATION | None | True | True |
| V12_COMPACT_C25_R7L107_261200_20240529_Stage2_261200_2024-05-29_Stage2 | 261200 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive | True | True |
| None | 263690 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | None | True | True |
| TRG_R12L78-C31-263700-CARELabs-DIGITAL-HEALTH-PLATFORM-POLICY-FADE | 263700 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should not treat digital-health platform policy beta as durable Stage2 unless policy maps to appointment/transaction volume, hospital/clinic adoption, revenue conversion and margin bridge. CareLabs produced a sharp MFE, but then a severe drawdown path, so the row is useful as local 4B boundary. | True | True |
| None | 263720 | C27_CONTENT_IP_GLOBAL_MONETIZATION | None | True | True |
| R13_4B4C_L101_T008_263720 | 263720 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| TRG_R8L74-C27-263750-PEARLABYSS-TRAILER-ANTICIPATION-BETA-FADE | 263750 | C27_CONTENT_IP_GLOBAL_MONETIZATION | C27 should not treat trailer/release-expectation beta as durable Stage2 unless release date, preorder/wishlist conversion, monetization model and revenue timing are visible. Pearl Abyss had limited MFE and then large MAE, so this is a false Stage2/local 4B row. | True | True |
| PEARLABYSS_263750_2024_07_09_STAGE2_FALSE_POSITIVE_GAME_IP_EVENT | 263750 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_false_positive | False | True |
| TRG_R8L74-C27-263750-PEARLABYSS-TRAILER-ANTICIPATION-BETA-FADE | 263750 | C27_CONTENT_IP_GLOBAL_MONETIZATION | C27 should not treat trailer/release-expectation beta as durable Stage2 unless release date, preorder/wishlist conversion, monetization model and revenue timing are visible. Pearl Abyss had limited MFE and then large MAE, so this is a false Stage2/local 4B row. | True | True |
| C27-R8L105-010|Stage4B|2024-03-21 | 263750 | C27_CONTENT_IP_GLOBAL_MONETIZATION | residual_error_needs_C27_specific_bridge_or_guard | True | True |
| None | 263750 | C27_CONTENT_IP_GLOBAL_MONETIZATION | None | True | True |
| R8L88_C28_DATASOLUTION_2024_STAGE4B_DATA_AI_THEME_CAP | 263800 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_4B_too_late_if_data_AI_theme_premium_not_capped | True | True |
| R8L97_C28_GENIANS_2024_STAGE2_FALSE_POSITIVE_ENDPOINT_SECURITY_CONTRACT_WATCH | 263860 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive_if_endpoint_security_watch_counts_without_contract_renewal_ARR_retention_margin_revision_bridge | True | True |
| V12_COMPACT_C28_R8L104_263860_20240530_263860_2024-05-31_Stage2-Actionable | 263860 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive | True | True |
| R8L93_C28_263860_20240124_STAGE2_FALSE_POSITIVE_ENDPOINT_SECURITY | 263860 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive_if_endpoint_security_vocabulary_overcredited | True | True |
| R5_L122_C18_013 | 264900 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | True | True |
| C19_R5L119_09_264900_Stage3_Yellow_2024-02-26 | 264900 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | True | True |
| C20_R5L117_264900_20240226_Stage3_Yellow | 264900 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_error_or_stress_case | True | True |
| R12L94_C32_HDHYUNDAI_2024_STAGE2_ACTIONABLE_HOLDCO_NAV_CAPITAL_RETURN_BRIDGE | 267250 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R1L10_C02_267260_STAGE2A_2024_01_03 | 267260 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_too_late | False | True |
| R1L95_C02_HDHYUNDAIELECTRIC_2024_STAGE2_ACTIONABLE_TRANSFORMER_GRID_BACKLOG_DATACENTER_CAPEX | 267260 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R1L92_C02_267260_20240129_STAGE2_TRANSFORMER_DATACENTER_BACKLOG | 267260 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_correct_if_customer_order_delivery_margin_cash_bridge_required | True | True |
| R11L85_C02_267260_20240129_STAGE2_TRANSFORMER_DATACENTER_CAPEX | 267260 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_correct_if_order_capacity_margin_bridge_required | True | True |
| None | 267260 | C02_POWER_GRID_DATACENTER_CAPEX | None | True | True |
| R13_CROSS_267260_2024-04-23_Stage2-Actionable | 267260 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_false_positive | True | True |
| None | 267260 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| None | 267260 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| None | 267260 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | None | False | True |
| None | 267260 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| None | 267260 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| R13L85_REVIEW_R11_C02_POWER_GRID_DATACENTER_CAPEX_267260_2024-01-29 | 267260 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_correct | True | True |
| None | 267260 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | True | True |
| TRG_R5L79-C18-271560-ORION-CHINA-CHANNEL-REORDER-RESET-BOUNDARY | 271560 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | C18 should not treat all confectionery or China-channel reorder resets as durable Stage2. Orion produced bounded MAE and a modest recovery MFE, so it should not be forced into 4B, but the price path did not validate a high-conviction export/channel rerating either. | True | True |
| C18_R5L113_271560_20240116_Stage2_2024-01-16 | 271560 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | False | True |
| TRG_R5L77-C18-271560-ORION-GLOBAL-DISTRIBUTION-BETA-FADE | 271560 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | True | True |
| None | 271560 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | True | True |
| TRG_R5L77-C18-271560-ORION-GLOBAL-DISTRIBUTION-BETA-FADE | 271560 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | C18 should not treat global snack distribution beta as durable Stage2 unless overseas reorder, sell-through, distributor inventory, pricing and margin bridge are visible. Orion had only limited MFE and a weak range-bound path, so it is a counterexample against generic global-distribution Green. | True | True |
| C19_R5L120_02_271560_Stage2_Actionable_2024-04-11 | 271560 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | True | True |
| C20_R5L116_271560_20240116_Stage2 | 271560 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | True | True |
| C20_R5_L102_T07_271560 | 271560 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | True | True |
| C20_R5L119_271560_20240411_02_Stage2_Actionable | 271560 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | None | True | True |
| R5L88_C20_KFOOD_GLOBAL_REORDER_003 | 271560 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | None | False | True |
| R9L84_C29_271940_20240522_STAGE2_FALSE_POSITIVE_HYDROGEN_OPTIONALITY | 271940 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive_if_hydrogen_optionality_overcredited | True | True |
| None | 272210 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | True | True |
| T_272210_20240618_STAGE2_REPAIR | 272210 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_false_positive_if_defense_system_label_promotes_to_stage3 | False | True |
| TRG_R1L82-C03-272210-HANWHA-SYSTEMS-DEFENSE-ELECTRONICS-BACKLOG | 272210 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | C03 should allow defense electronics positives when radar/C4I/sensor program backlog, export customer, delivery milestones, revenue conversion and margin bridge are visible. Hanwha Systems produced strong MFE with controlled entry-basis MAE, but bridge refresh is required after post-peak drawdown. | True | True |
| TRG_R11L77-C03-272210-HANWHA-SYSTEMS-DEFENSE-ELECTRONICS-BACKLOG | 272210 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | C03 should include defense electronics / radar / C4I names only when policy-defense demand maps to backlog, customer program, delivery schedule and margin bridge. Hanwha Systems produced solid MFE with controlled MAE, but later drawdown says C03 must lifecycle-manage the signal. | True | True |
| TRG_R11L77-C03-272210-HANWHA-SYSTEMS-DEFENSE-ELECTRONICS-BACKLOG | 272210 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_correct | True | True |
| T_272210_20240306_STAGE2A_REPAIR | 272210 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_false_positive_if_stage2_actionable_without_export_backlog_cash_bridge | False | True |
| R11L90_C03_272210_20240422_STAGE2_DEFENSE_ELECTRONICS_EXPORT_BACKLOG | 272210 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_correct_if_export_framework_backlog_delivery_margin_bridge_required | True | True |
| R11L95_C03_HANWHASYSTEMS_2024_STAGE2_ACTIONABLE_DEFENSE_SPACE_EXPORT_BACKLOG_BRIDGE | 272210 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| None | 272210 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | None | False | True |
| V12_COMPACT_C03-R1L105-04_272210_2024-03-06_4B-Watch | 272210 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_false_positive | True | True |
| T_C03_R1L108_272210_20240711_STAGE4B | 272210 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current profile can over-promote defense beta unless sovereign funded backlog, delivery schedule and margin/cash bridge are verified | True | True |
| T_C03_R1L107_272210_20240912_STAGE4B | 272210 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | local_4b_real_but_full_green_needs_export_backlog_or_recurring_margin_bridge | True | True |
| R12L91_C31_HANWHASYSTEMS_2024_STAGE2_ACTIONABLE_SPACE_DEFENSE_POLICY_CONTRACT_BRIDGE | 272210 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| TRG-C06-L111-272290-Stage3Yellow-2024-02-01 | 272290 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_needs_4B_watch_despite_positive_MFE | True | True |
| None | 272290 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | False | True |
| TRG_R8L77-C26-273060-WISEBIRDS-AD-PLATFORM-THEME-FADE | 273060 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| None | 273060 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | None | False | True |
| TRG_R8L77-C26-273060-WISEBIRDS-AD-PLATFORM-THEME-FADE | 273060 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | C26 should not treat digital-ad or AI-ad platform beta as durable Stage2 unless advertiser budget, ROAS, media buying efficiency, repeat spend and margin bridge refreshes. Wisebirds had a tradable MFE but then a deep post-peak fade, making it a local 4B-watch row rather than durable Green. | True | True |
| R8L88_C26_273060_20240220_STAGE2_FALSE_POSITIVE_ADTECH_THEME_BLOWOFF | 273060 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive_if_adtech_theme_blowoff_overcredited | True | True |
| R8L89_C26_WISEBIRDS_2024_STAGE4B_ADTECH_AI_THEME_CAP | 273060 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_4B_too_late_if_adtech_AI_theme_premium_not_capped | True | True |
| TR_C26_L105_273060_Stage4B_20240516 | 273060 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| V12_COMPACT_273060_2024-06-03_platform_ad_budget_retention_opm_bridge_cleanup | 273060 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| R13L88_REVIEW_R8_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_273060_2024-02-20 | 273060 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| None | 274090 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | None | False | True |
| R11L84_C03_274090_20240118_STAGE2_FALSE_POSITIVE_AEROSPACE_THEME | 274090 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_false_positive_if_aerospace_theme_overcredited | True | True |
| R13_L106_T07_277880 | 277880 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive | True | True |
| T_C11_R3L107_278280_STAGE4B_20240221 | 278280 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive_if_orderbook_label_is_overcredited | True | True |
| V12_COMPACT_C12_R3L105_278280_20240503_08_278280_2024-05-03_Stage2 | 278280 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_false_positive | True | True |
| CHUNBO_278280_2024_02_21_4C_ELECTROLYTE_CALL_OFF_RISK | 278280 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_4C_too_late | False | True |
| None | 278280 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_correct_if_hard_4c_requires_customer_pull_margin_break | True | True |
| TRG_R3L76-C13-278280-CHUNBO-ELECTROLYTE-ADDITIVE-UTILIZATION-FADE | 278280 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_false_positive | True | True |
| None | 278280 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | False | True |
| TRG_R3L76-C13-278280-CHUNBO-ELECTROLYTE-ADDITIVE-UTILIZATION-FADE | 278280 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | C13 should not treat electrolyte/additive or IRA supply-chain beta as durable Stage2 unless customer utilization, local supply, call-off and margin evidence refreshes. Chunbo had limited MFE and then a high-MAE utilization fade. | True | True |
| R3L93_C13_278280_20240208_STAGE2_FALSE_POSITIVE_ELECTROLYTE_CAPACITY | 278280 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_false_positive_if_electrolyte_capacity_JV_vocabulary_overcredited | True | True |
| T_C13_R3L105_278280_STAGE4B_20240221 | 278280 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | True | True |
| T_C13_R3L105_278280_STAGE4C_20240221 | 278280 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | True | True |
| T_C14_R3L108_278280_STAGE4C_20240221 | 278280 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_false_positive | True | True |
| None | 278280 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| V12_COMPACT_R13L11-4B4C-005_278280_2024-02-21_cross_archetype_4b_4c_boundary_retest | 278280 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R13_4B4C_L12_03_278280_20240221_Stage4C_Watch | 278280 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_source_proxy_row_promotes_to_green_or_full_4B | True | True |
| R13_CROSS_278280_2024-02-21_Stage4B | 278280 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | True | True |
| None | 278280 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | True | True |
| R13_CROSS_278280_2024-02-21_Stage4C | 278280 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| R13_CROSS_278280_2024-05-03_Stage2 | 278280 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive | True | True |
| TRG_R5L75-C18-280360-LOTTE-WELLFOOD-KFOOD-EXPORT-CHANNEL-MARGIN | 280360 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | C18 should allow Stage2 when K-food/export attention is tied to channel reorder, overseas sell-through, product mix and margin bridge. Lotte Wellfood produced large MFE with controlled early MAE, but post-peak drawdown requires lifecycle local 4B if channel reorder evidence fades. | True | True |
| TRG_R5L75-C18-280360-LOTTE-WELLFOOD-KFOOD-EXPORT-CHANNEL-MARGIN | 280360 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_correct | True | True |
| TRG_R5L77-C18-280360-LOTTE-WELLFOOD-GLOBAL-SNACK-CHANNEL-REORDER | 280360 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | C18 should allow packaged-food/snack exporters when overseas channel reorder, category mix, pricing and margin bridge are visible. Lotte Wellfood produced high MFE with controlled MAE, but the later post-peak drawdown requires lifecycle local 4B if global channel/margin evidence fades. | True | True |
| TRG_R5L77-C18-280360-LOTTE-WELLFOOD-GLOBAL-SNACK-CHANNEL-REORDER | 280360 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_correct | True | True |
| None | 280360 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | True | True |
| None | 281740 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | None | True | True |
| None | 281820 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | False | True |
| KCTECH_281820_2024_03_06_STAGE2_FALSE_POSITIVE_CMP_PROCESS_EQUIPMENT | 281820 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_false_positive | False | True |
| KCTECH_281820_2024_02_27_STAGE2A_ADV_EQUIP_RERATING | 281820 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_4B_too_late | False | True |
| R2L93_C10_281820_20240214_STAGE2_CMP_WETCLEAN_MEMORY_RECOVERY | 281820 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_correct_if_memory_recovery_order_delivery_margin_cash_bridge_required_but_Green_strict | True | True |
| TRG_R5L81-C19-282330-BGF-RETAIL-CONVENIENCE-MARGIN-BOUNDED-RECOVERY | 282330 | C19_BRAND_RETAIL_INVENTORY_MARGIN | C19 should not call bounded convenience-store recovery hard 4C when no non-price margin or demand break is confirmed, but it also should not mark durable Stage2 without same-store sales, mix, cost control and margin bridge. BGF Retail is a RiskWatch/no-hard-4C boundary. | True | True |
| BGFRETAIL_282330_2024_01_29_STAGE2_FALSE_POSITIVE_CVS_MARGIN_SLOWDOWN | 282330 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_false_positive | False | True |
| R5L98_C19_BGFRETAIL_2024_STAGE2_FALSE_POSITIVE_CONVENIENCE_RETAIL_INVENTORY_MARGIN_WATCH | 282330 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_false_positive_if_defensive_retail_watch_counts_without_SSS_inventory_turn_OPM_revision_bridge | True | True |
| R5L93_C19_282330_20240705_STAGE2_CONVENIENCE_INVENTORY_MARGIN | 282330 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_correct_if_sellthrough_inventory_margin_cash_bridge_required_but_Green_strict | True | True |
| None | 282880 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive_if_automation_orderbook_proxy_promotes_Yellow | True | True |
| None | 282880 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_false_positive_if_factory_automation_orderbook_proxy_promotes_Yellow_without_delivery_acceptance_margin_bridge | True | True |
| C13_R3L102_05_282880_20240329_T1 | 282880 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_false_positive | True | True |
| R3L92_C14_282880_20240102_STAGE2_4B_EQUIPMENT_CAPEX_DELAY | 282880 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_correct_if_capex_delay_backlog_margin_cash_drag_routes_to_4B | True | True |
| T_C15_R4L105_285130_20240226_08_Stage2 | 285130 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive | True | True |
| T_C17_R4L105_04_285130_Stage2_20240226 | 285130 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive | True | True |
| None | 285130 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | True | True |
| TRG_R7L79-C25-287410-JEISYS-MEDICAL-AESTHETIC-DEVICE-STRATEGIC-EVENT | 287410 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | C25 should protect aesthetic-device export/commercialization positives when export channel, installed-base, consumables, distributor reorder, revenue and margin bridge are visible. Jeisys Medical produced strong MFE and later a stabilized strategic-event price path, but status/delisting-like caveat requires validation. | True | True |
| C32_287410_JEISYS_20240610_LOCAL4B | 287410 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_correct_if_local_4b_not_green | True | True |
| C24-R7-L99-TRG-06-288330 | 288330 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_false_positive | True | True |
| TRG_R12L80-C31-289010-ICECREAM-EDU-AI-DIGITAL-TEXTBOOK-LIFECYCLE | 289010 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should allow under-covered education-policy rows only when AI digital textbook policy maps to direct school/customer adoption, paid conversion, subscription revenue and margin bridge. Icecream Edu produced tradable MFE but later high MAE, so it is a lifecycle candidate only after source repair. | True | True |
| R8L96_C27_GIANTSTEP_2024_STAGE4B_VIRTUAL_PRODUCTION_AI_CONTENT_EVENT_CAP | 289220 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_4B_too_late_if_virtual_production_AI_content_event_premium_not_capped | True | True |
| R13L96_REVIEW_R8_C27_CONTENT_IP_GLOBAL_MONETIZATION_289220_2024_01_09_TRIGGER | 289220 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late_if_virtual_production_AI_content_event_premium_not_capped | True | True |
| None | 290270 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | None | False | True |
| V12_COMPACT_C28_R8L104_290270_20240321_290270_2024-03-22_Stage2 | 290270 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive | True | True |
| V12_COMPACT_R13L11-4B4C-014_290270_2024-03-26_cross_archetype_4b_4c_boundary_retest | 290270 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R13_CROSS_290270_2024-03-26_Stage2 | 290270 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | True | True |
| None | 290270 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | True | True |
| V12_COMPACT_R13L2_C28_290270_20240326_STAGE2_290270_2024-03-26_cross_archetype_high_MAE_guardrail_review | 290270 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| V12_COMPACT_R13_STAGE2FP_L8_01_290270_2024-03-22_STAGE2_290270_2024-03-22_stage2_source_proxy_deep_MAE_false_positive_review | 290270 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive | True | True |
| T_R13_STAGE2FP_L6_290270_Stage2_2024-03-26 | 290270 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_stage2_false_positive_or_overpromotion_risk | True | True |
| R13_CROSS_290270_2024-03-26_Stage2 | 290270 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive | True | True |
| V12_COMPACT_C25_R7L107_290650_20240513_Stage2_Actionable_290650_2024-05-13_Stage2-Actionable | 290650 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive | True | True |
| R7L89_C25_290650_20240102_STAGE2_FALSE_POSITIVE_BIOMATERIAL_REBOUND | 290650 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive_if_biomaterial_rebound_overcredited | True | True |
| None | 290670 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive_if_equipment_order_cycle_promotes_Yellow | True | True |
| R3L89_C11_290670_20240221_STAGE2_FALSE_POSITIVE_MAGNETIC_EQUIPMENT | 290670 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive_if_equipment_rebound_overcredited | True | True |
| None | 290670 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_false_positive_if_equipment_order_cycle_proxy_promotes_Actionable_or_Yellow_without_customer_pull_and_margin_bridge | True | True |
| R3L90_C12_DAEBOMAGNETIC_2024_STAGE2_FALSE_POSITIVE_CALLOFF_RISK | 290670 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_false_positive_if_battery_process_equipment_theme_counts_without_customer_contract_reorder_bridge | True | True |
| C13_R3L102_07_290670_20240315_T1 | 290670 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_false_positive | True | True |
| R3L98-C14-005-T1 | 290670 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_too_late_if_equipment_orderbook_memory_blocks_hard_4C | True | True |
| R13L90_REVIEW_R3_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_290670_2024_02_21_TRIGGER | 290670 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive_if_battery_process_equipment_theme_counts_without_customer_contract_reorder_bridge | True | True |
| KAKAOGAMES_293490_2024_01_11_STAGE2_FALSE_POSITIVE_GAME_IP_LINEUP | 293490 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_false_positive | False | True |
| V12_COMPACT_C27-R8-L101-004_293490_2024-03-11_portfolio_game_pipeline_label_without_hit_revenue_conversion | 293490 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_false_positive | True | True |
| C27-R8L105-016|Stage2-Actionable|2024-05-27 | 293490 | C27_CONTENT_IP_GLOBAL_MONETIZATION | residual_error_needs_C27_specific_bridge_or_guard | True | True |
| TRG_R8L80-C27-293490-KAKAOGAMES-GAME-PORTFOLIO-THEME-FADE | 293490 | C27_CONTENT_IP_GLOBAL_MONETIZATION | C27 should not treat game portfolio or new-title theme beta as durable Stage2 unless global IP traction, launch metrics, user retention, revenue conversion and margin bridge are visible. Kakao Games had small MFE and then a persistent MAE/downtrend path. | True | True |
| R7L95_C23_APTABIO_2024_STAGE4B_NOX_INHIBITOR_REGULATORY_EVENT_CAP | 293780 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_4B_too_late_if_NOX_inhibitor_regulatory_event_premium_not_capped | True | True |
| R13L95_REVIEW_R7_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_293780_2024_07_11_TRIGGER | 293780 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late_if_NOX_inhibitor_regulatory_event_premium_not_capped | True | True |
| R7L97_C25_EOFLOW_2024_STAGE4B_WEARABLE_INSULIN_DEVICE_EVENT_CAP | 294090 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_4B_too_late_if_wearable_insulin_device_event_premium_not_capped | True | True |
| R13_CROSS_294570_2024-02-01_Stage2-FalsePositive_/_DataAPIContractRetentionWeak | 294570 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive | True | True |
| None | 294570 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | None | True | True |
| None | 294870 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | True | True |
| T_C05_R1L108_294870_20240126_HOUSING_PF_CONTAMINANT | 294870 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | True | True |
| T_C05_R1L109_294870_20240126_PF_BALANCE_SHEET_REPAIR_CONTAMINANT | 294870 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | True | True |
| T_C05_R1L108_294870_20240826_HDC_POST_SPIKE_WATCH | 294870 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | True | True |
| V12_COMPACT_294870_2024-01-26_PF_balance_sheet_repair_rebound_with_orderbook_visibility | 294870 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive | False | True |
| C30_R10L104_294870_20240424_Stage2_Actionable | 294870 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_may_be_too_late_if_it_waits_for_full_4B | True | True |
| None | 294870 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | True | True |
| C30_R10L105_294870_20240826_4B_Local_Watch | 294870 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_error_if_C30_overcredits_price_or_low_PBR_without_balance_sheet_bridge | True | True |
| None | 294870 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| None | 294870 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| None | 294870 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| R4L89_C17_298000_20240102_STAGE2_FALSE_POSITIVE_PETROCHEM_REBOUND | 298000 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive_if_petrochemical_rebound_overcredited | True | True |
| R4L91_C17_HYOSUNGCHEM_2024_STAGE4C_PP_CHEMICAL_MARGIN_BREAK | 298000 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_4C_needed_if_chemical_commodity_margin_break_has_deep_MAE_and_no_revision_bridge | True | True |
| R13L91_REVIEW_R4_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_298000_2024_01_24_TRIGGER | 298000 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_4C_needed_if_chemical_commodity_margin_break_has_deep_MAE_and_no_revision_bridge | True | True |
| T_C15_R4L105_298020_20240329_04_Stage2-Actionable | 298020 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive | True | True |
| T_C15_R4L104_298020_Stage3_Yellow_20240417 | 298020 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_too_permissive_if_spread_label_scores_without_margin_FCF_durability | True | True |
| None | 298020 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| None | 298020 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| R4L10_C17_298020_T1 | 298020 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_correct | False | True |
| None | 298020 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | True | True |
| R4L10_C17_298020_T4B | 298020 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_correct | False | True |
| None | 298040 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | True | True |
| R1L10_C02_298040_STAGE2A_2024_01_03 | 298040 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_too_late | False | True |
| R1L91_C02_HYOSUNGHEAVY_2024_STAGE2_ACTIONABLE_TRANSFORMER_DATACENTER_CAPEX | 298040 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R1L88_C02_298040_20240304_STAGE2_TRANSFORMER_CAPEX | 298040 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_correct_if_order_customer_margin_bridge_required | True | True |
| None | 298040 | C02_POWER_GRID_DATACENTER_CAPEX | None | True | True |
| R13_CROSS_298040_2024-04-29_Stage2-Actionable | 298040 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_false_positive | True | True |
| None | 298040 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| None | 298040 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | None | True | True |
| None | 298040 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | None | False | True |
| R13L88_REVIEW_R1_C02_POWER_GRID_DATACENTER_CAPEX_298040_2024-03-04 | 298040 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_correct | True | True |
| V12_COMPACT_R13L12_ACCT_PRICE_14_C02_298040_20240717_298040_2024-07-17_4B | 298040 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | True | True |
| None | 298040 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | None | True | True |
| V12_COMPACT_298380_2024-02-02_LICENSE_OUT_MILESTONE_NOT_COMMERCIALIZATION_GUARD | 298380 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive | True | True |
| TRG_R7L74-C24-298380-ABL-BISPECIFIC-PLATFORM-DATA-RERATING | 298380 | C24_BIO_TRIAL_DATA_EVENT_RISK | C24 should distinguish platform-data derisking from simple biotech beta. ABL Bio had an early tradable MFE, then later re-accelerated into a larger 180D MFE; however later drawdown and share-count change require lifecycle and validation controls. | True | True |
| TRG_R7L80-C24-298380-ABL-BIO-BIOPLATFORM-DATA-LICENSE-MILESTONE | 298380 | C24_BIO_TRIAL_DATA_EVENT_RISK | C24 should protect platform-biotech positives only when trial data, partner/license economics, milestone runway, cash runway and commercialization path are visible. ABL Bio produced a strong MFE but still needs lifecycle 4B if the data/license bridge fades. | True | True |
| R7L93_C24_298380_20240222_STAGE2_BISPECIFIC_ADC_DATA | 298380 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_correct_if_data_quality_partner_validation_cash_bridge_required_but_Green_strict | True | True |
| TRG_R7L76-C24-298380-ABL-BIO-BISPECIFIC-ADC-TRIAL-DATA-BRIDGE | 298380 | C24_BIO_TRIAL_DATA_EVENT_RISK | C24 should allow a trial-data/platform-event Stage2 when clinical data, partner validation, differentiated modality and downstream commercialization bridge are visible. ABL Bio produced high MFE with almost no entry-basis MAE, but later post-peak fading still requires lifecycle local 4B if clinical/partner bridge evidence goes stale. | True | True |
| TRG_R7L76-C24-298380-ABL-BIO-BISPECIFIC-ADC-TRIAL-DATA-BRIDGE | 298380 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_correct | True | True |
| ABL_298380_2024_03_06_STAGE2A_BISPECIFIC_DATA_PLATFORM | 298380 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_correct | False | True |
| None | 298380 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | False | True |
| TRG_R7L74-C24-298380-ABL-BISPECIFIC-PLATFORM-DATA-RERATING | 298380 | C24_BIO_TRIAL_DATA_EVENT_RISK | C24 should distinguish platform-data derisking from simple biotech beta. ABL Bio had an early tradable MFE, then later re-accelerated into a larger 180D MFE; however later drawdown and share-count change require lifecycle and validation controls. | True | True |
| C24_R7L98_TRIG_05_298380 | 298380 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_false_positive | True | True |
| None | 298540 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | True | True |
| 298540_2023-11-15_Stage2_C19_SINGLE_BRAND_INVENTORY_OVERHANG_FALSE_POSITIVE | 298540 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_false_positive | False | True |
| NATURE_298540_2024_04_01_STAGE2_FALSE_POSITIVE_INVENTORY_MARGIN_FAIL | 298540 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_false_positive | False | True |
| R5L93_C19_NATUREHOLDINGS_2024_STAGE4B_OUTDOOR_BRAND_INVENTORY_EVENT_CAP | 298540 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_4B_too_late_if_outdoor_brand_inventory_event_premium_not_capped | True | True |
| R13L93_REVIEW_R5_C19_BRAND_RETAIL_INVENTORY_MARGIN_298540_2024_02_02_TRIGGER | 298540 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late_if_outdoor_brand_inventory_event_premium_not_capped | True | True |
| HANATECH_299030_2024_03_06_STAGE2_FALSE_POSITIVE_EQUIPMENT_ORDERBOOK | 299030 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive | False | True |
| None | 299030 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive_if_turnkey_orderbook_proxy_promotes_Yellow | True | True |
| TRG_R3L82-C11-299030-HANA-TECH-BATTERY-EQUIPMENT-ORDERBOOK-FADE | 299030 | C11_BATTERY_ORDERBOOK_RERATING | C11 should not treat battery equipment orderbook theme beta as durable Stage2 unless customer order, delivery schedule, backlog conversion, revenue and margin bridge are visible. Hana Technology had a sharp early MFE, then severe high-MAE fade and share-count changes. | True | True |
| T_C11_R3L107_299030_STAGE4B_20240308 | 299030 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive_if_orderbook_label_is_overcredited | True | True |
| None | 299030 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_4B_too_late_if_orderbook_memory_ignores_local_peak | True | True |
| None | 299030 | C11_BATTERY_ORDERBOOK_RERATING | None | True | True |
| None | 299030 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | True | True |
| T_C13_R3L105_299030_STAGE4B_20240308 | 299030 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | True | True |
| C13_R3L102_04_299030_20240315_T1 | 299030 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_false_positive | True | True |
| T_C13_R3L105_299030_STAGE4C_20240308 | 299030 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | True | True |
| T_C14_R3L108_299030_STAGE4C_20240308 | 299030 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_false_positive | True | True |
| R3L98-C14-006-T1 | 299030 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_too_late_if_orderbook_memory_delays_hard_4C | True | True |
| V12_COMPACT_R13L11-4B4C-007_299030_2024-03-08_cross_archetype_4b_4c_boundary_retest | 299030 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R13_4B4C_L12_06_299030_20240308_Stage4C_Watch | 299030 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_source_proxy_row_promotes_to_green_or_full_4B | True | True |
| R13_CROSS_299030_2024-03-08_Stage4C | 299030 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | True | True |
| None | 299030 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | True | True |
| R13_CROSS_299030_2024-03-08_Stage4C | 299030 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| C27-R8L105-011|Stage2|2024-03-18 | 299900 | C27_CONTENT_IP_GLOBAL_MONETIZATION | residual_error_needs_C27_specific_bridge_or_guard | True | True |
| R8L97_C27_WYSIWYG_2024_STAGE4B_VIRTUAL_PRODUCTION_AI_CONTENT_EVENT_CAP | 299900 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_4B_too_late_if_virtual_production_AI_content_event_premium_not_capped | True | True |
| R13_CROSS_299900_2024-03-18_Stage2 | 299900 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive | True | True |
| R10L90_C30_300720_20240129_STAGE2_CEMENT_MARGIN_CASH | 300720 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_correct_if_materials_margin_cash_bridge_required | True | True |
| C23_R7_L209_T06 | 302440 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive | False | True |
| V12_COMPACT_302440_2024-02-02_VACCINE_PLATFORM_LABEL_WITHOUT_REVENUE_BRIDGE | 302440 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive | True | True |
| TRG_R7L81-C23-302440-SK-BIOSCIENCE-VACCINE-COMMERCIALIZATION-THEME-FADE | 302440 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | C23 should not treat vaccine platform or regulatory commercialization theme beta as durable Stage2 unless product approval, procurement/order visibility, manufacturing utilization, revenue conversion and margin bridge are visible. SK Bioscience had tiny MFE and then a high-MAE fade. | True | True |
| R7L85_C23_302440_20240321_STAGE2_FALSE_POSITIVE_VACCINE_COMMERCIAL_THEME | 302440 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive_if_approval_commercial_theme_overcredited | True | True |
| R13L85_REVIEW_R7_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_302440_2024-03-21 | 302440 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| None | 302550 | C24_BIO_TRIAL_DATA_EVENT_RISK | C24 must require fresh binary/data endpoint quality; reroute commercialization, device, reimbursement, or price-only events to C23/C25/local_4B as appropriate. | True | True |
| V12_COMPACT_C25_R7L107_302550_20240904_Stage2_FalsePositive_302550_2024-09-04_Stage2-FalsePositive | 302550 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive | True | True |
| None | 302550 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | None | True | True |
| T_R13_STAGE2FP_L6_302550_Stage2_2024-03-21 | 302550 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_stage2_false_positive_or_overpromotion_risk | True | True |
| R8L89_C28_304100_20240105_STAGE2_FALSE_POSITIVE_AI_SOFTWARE_BLOWOFF | 304100 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive_if_AI_software_blowoff_counted_as_contract_retention | True | True |
| TRG_R5L78-C19-306040-SJ-GROUP-BRAND-INVENTORY-TURNAROUND-FADE | 306040 | C19_BRAND_RETAIL_INVENTORY_MARGIN | C19 should not treat fashion-brand inventory-turnaround beta as durable Stage2 unless sell-through, channel productivity, inventory clearance, reorder and margin bridge are visible. SJ Group produced only small MFE, then persistent MAE and post-peak fade. | True | True |
| R8L98_C28_HYUNDAIAUTOEVER_2024_STAGE2_FALSE_POSITIVE_AUTO_ENTERPRISE_SW_RETENTION_WATCH | 307950 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive_if_auto_enterprise_SW_watch_counts_without_retention_backlog_margin_revision_bridge | True | True |
| V12_COMPACT_C28-R8-L102-07_307950_2024-01-29_Stage2-Actionable | 307950 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive | True | True |
| V12_COMPACT_C28_R8L104_307950_20240805_307950_2024-08-06_Stage2-Actionable | 307950 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive | True | True |
| TRG_R8L79-C28-307950-HYUNDAI-AUTOEVER-AUTO-SW-CONTRACT-RETENTION | 307950 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | C28 should preserve software/SI positives when contract retention, captive/customer quality, recurring maintenance, project backlog, revenue recognition and margin bridge are visible. Hyundai AutoEver produced a slow MFE with moderate MAE; it should not be overblocked after source repair, but lifecycle 4B is needed if contract/revenue/margin evidence fades. | True | True |
| None | 307950 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| R7L96_C24_VORONOI_2024_STAGE2_ACTIONABLE_TARGETED_ONCOLOGY_PIPELINE_DATA_BRIDGE | 310210 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R7L98_C24_VORONOI_2024_STAGE2_ACTIONABLE_ONCOLOGY_TARGET_TRIAL_DATA_PARTNERING_BRIDGE | 310210 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| C24_R7L98_TRIG_04_310210 | 310210 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_missed_structural | True | True |
| None | 316140 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | False | True |
| R6L90_C21_WOORI_2024_STAGE2_ACTIONABLE_BANK_VALUEUP_ROE_CAPITAL_RETURN | 316140 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| TRG_R6L73-C21-316140-WOORI-VALUEUP-CAPITAL-RETURN-BRIDGE | 316140 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | C21 should allow Stage2 when low-PBR bank rerating is backed by shareholder-return, buyback/cancellation, dividend and ROE bridge. Woori produced controlled MAE and later MFE, but share-count change inside the window needs coding-agent validation. | True | True |
| TRG_R6L79-C21-316140-WOORI-BANK-HOLDCO-CAPITAL-RETURN | 316140 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | C21 should preserve bank-holdco capital-return rows when PBR discount, capital ratio, shareholder-return policy, earnings durability and buyback/cancellation evidence are visible. Woori Financial produced a controlled-MAE MFE path, but share-count changes inside the raw shard require validation. | True | True |
| TRG_R6L73-C21-316140-WOORI-VALUEUP-CAPITAL-RETURN-BRIDGE | 316140 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | C21 should allow Stage2 when low-PBR bank rerating is backed by shareholder-return, buyback/cancellation, dividend and ROE bridge. Woori produced controlled MAE and later MFE, but share-count change inside the window needs coding-agent validation. | True | True |
| None | 316140 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | True | True |
| T-WOORI-S2A-20250210 | 316140 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_late | True | True |
| None | 316140 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | True | True |
| None | 316140 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | False | True |
| R6L87_C21_316140_20240726_STAGE2_FALSE_POSITIVE_LATE_BANK_VALUEUP | 316140 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive_if_late_bank_valueup_extension_overcredited | True | True |
| V12_COMPACT_316140_2024-04-02_policy_valueup_bank_capital_return_cash_bridge | 316140 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | True | True |
| V12_COMPACT_316140_2024-04-26_policy_valueup_bank_brokerage_ROE_PBR_capital_return_execution_bridge | 316140 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | True | True |
| C31_R11L106_TRG_04 | 316140 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | None | True | True |
| R13L87_REVIEW_R6_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_316140_2024-07-26 | 316140 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R9L96_C29_RANIX_2024_STAGE4B_AUTONOMOUS_DRIVING_CHIP_EVENT_CAP | 317120 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_4B_too_late_if_autonomous_driving_chip_event_premium_not_capped | True | True |
| R13L96_REVIEW_R9_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_317120_2024_01_11_TRIGGER | 317120 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late_if_autonomous_driving_chip_event_premium_not_capped | True | True |
| R3L93_C11_DUKSAN_2024_STAGE2_ACTIONABLE_ELECTROLYTE_ADDITIVE_ORDERBOOK_BRIDGE | 317330 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R3L86_C12_317330_20240214_STAGE2_BATTERY_MATERIAL_CALLOFF_BRIDGE | 317330 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_correct_if_calloff_capacity_bridge_required | True | True |
| R3L99-C14-005-T1 | 317330 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_too_conservative_if_proxy_material_recovery_MFE_is_ignored | True | True |
| R13L86_REVIEW_R3_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_317330_2024-02-14 | 317330 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_correct | True | True |
| C07_R2L90_319660_20240711_STAGE2_FALSE_POSITIVE | 319660 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_false_positive | True | True |
| R2_L110_C07 | 319660 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | None | True | True |
| None | 319660 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | False | True |
| TRG-C09-L115-03-319660-Stage2Actionable-2024-02-15 | 319660 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_correct_if_actionable_not_green | True | True |
| PSK_319660_2024_03_06_STAGE2A_MEMORY_DRY_STRIP_RECOVERY | 319660 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_4B_too_late | False | True |
| PSK_319660_2024_03_06_STAGE2A_MEMORY_DRY_STRIP_EQUIPMENT_RECOVERY | 319660 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_4B_too_late | False | True |
| None | 319660 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | None | True | True |
| T_C06_R2L103_322310_20240201_Stage2Actionable_CROSS_C07 | 322310 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_needs_C06_vs_C07_C08_C09_reroute_guard | True | True |
| TRG_R2L77-C07-322310-AUROS-METROLOGY-EQUIPMENT-THEME-FADE | 322310 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_false_positive | True | True |
| V12_COMPACT_322310_2024-02-01_Stage2-Actionable | 322310 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_false_positive | True | True |
| TRG_R2L77-C07-322310-AUROS-METROLOGY-EQUIPMENT-THEME-FADE | 322310 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | C07 should not treat metrology/overlay equipment beta as durable Stage2 unless customer order, delivery, tool adoption and margin bridge are visible. Auros Technology had a tradable early MFE, but then opened a high-MAE drawdown path, making it local 4B-watch rather than durable Green. | True | True |
| None | 322310 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | False | True |
| None | 322310 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | False | True |
| AURAS_322310_2024_03_06_STAGE2_FALSE_POSITIVE_ADVANCED_OVERLAY_METROLOGY | 322310 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_false_positive | False | True |
| TRG_R2L82-C09-322310-AUROS-METROLOGY-VALUATION-BLOWOFF | 322310 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | C09 should cap overlay metrology/inspection equipment MFE when it is mostly valuation/theme beta. Without customer order, delivery, revenue conversion and margin bridge, Oros' early spike should be treated as local 4B/fade rather than durable Stage2. | True | True |
| R2L93_C09_322310_20240227_STAGE2_FALSE_POSITIVE_OVERLAY_METROLOGY_MFE | 322310 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_false_positive_if_overlay_metrology_price_MFE_overcredited | True | True |
| None | 322310 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | None | True | True |
| None | 322310 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| T-KAKAOBANK-S2-20250210 | 323410 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | True | True |
| R6L100_C21_KAKAOBANK_2024_STAGE2_FALSE_POSITIVE_DIGITAL_BANK_ROE_PBR_WATCH | 323410 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive_if_digital_bank_PBR_watch_counts_without_ROE_credit_cost_capital_return_revision_bridge | True | True |
| R6L98_C21_KAKAOBANK_2024_STAGE2_FALSE_POSITIVE_DIGITAL_BANK_VALUEUP_WATCH | 323410 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive_if_digital_bank_valueup_watch_counts_without_ROE_capital_return_NIM_risk_cost_revision_bridge | True | True |
| R6L85_C21_323410_20240115_STAGE2_FALSE_POSITIVE_DIGITAL_BANK_BETA | 323410 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive_if_digital_bank_beta_overcredited | True | True |
| T-KAKAOBANK-4B-20250624 | 323410 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_4B_too_late | True | True |
| C31_L101_T007_323410 | 323410 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | True | True |
| R13L85_REVIEW_R6_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_323410_2024-01-15 | 323410 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| None | 323990 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | False | True |
| TRG_R7L80-C24-323990-VAXCELL-TRIAL-THEME-FADE | 323990 | C24_BIO_TRIAL_DATA_EVENT_RISK | C24 should not treat cell-therapy trial theme beta as durable Stage2 unless trial data quality, regulatory path, partner/commercial economics and cash runway are visible. VaxCell had a tradable MFE but then a high-MAE fade. | True | True |
| C24-R7-L100-TRIG-04-323990 | 323990 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_4B_too_late | True | True |
| C24-R7-L100-TRIG-07-323990 | 323990 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_4C_too_late | True | True |
| None | 326030 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | None | False | True |
| R7L91_C23_326030_20240705_STAGE2_CNS_COMMERCIALIZATION_REVENUE | 326030 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_correct_if_launch_revenue_margin_cash_bridge_required | True | True |
| None | 326030 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | None | True | True |
| None | 326030 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | None | True | True |
| V12_COMPACT_326030_2024-02-05_APPROVED_DRUG_SALES_OPM_REVISION_BRIDGE | 326030 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_correct | True | True |
| None | 326030 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | True | True |
| T_C24_R7L105_326030_20240229_STAGE2 | 326030 | C24_BIO_TRIAL_DATA_EVENT_RISK | if_trigger_is_commercial_sales_not_binary_data_it_should_route_to_C23_or_remain_Stage2_not_C24_Green | True | True |
| None | 326030 | C24_BIO_TRIAL_DATA_EVENT_RISK | C24 must require fresh binary/data endpoint quality; reroute commercialization, device, reimbursement, or price-only events to C23/C25/local_4B as appropriate. | True | True |
| T_R13_STAGE2FP_L5_326030_Stage2_2024-02-29 | 326030 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_stage2_false_positive_or_overpromotion_risk | True | True |
| TRG_R1L77-C01-329180-HD-HYUNDAI-HI-SHIPBUILDING-ORDERBOOK-MARGIN | 329180 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | C01 should preserve large shipbuilding orderbook winners when customer quality, delivery slots, naval/LNG mix, ASP and margin bridge are visible. HD Hyundai Heavy produced high MFE with controlled MAE; later drawdown should be lifecycle-managed, not treated as a hard 4C without order/margin break. | True | True |
| TRG_R1L77-C01-329180-HD-HYUNDAI-HI-SHIPBUILDING-ORDERBOOK-MARGIN | 329180 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_correct | True | True |
| C01_R1L100_329180_shipbuilding_backlog_margin_bridge_T1 | 329180 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_correct | False | True |
| HHI_329180_2024_04_18_STAGE2A_SHIPBUILDING_BACKLOG_MARGIN_BRIDGE | 329180 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_4B_too_late | False | True |
| R1L93_C01_329180_20240418_STAGE2_SHIPBUILDING_BACKLOG_MARGIN | 329180 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_correct_if_orderbacklog_delivery_margin_cash_bridge_required_but_Green_strict | True | True |
| TRG_R1L73-C01-329180-HDHHI-LNG-NAVAL-BACKLOG-MARGIN-BRIDGE | 329180 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | C01 should allow Stage2 when shipbuilding backlog is not just order volume but connects to LNG/naval mix, rising newbuild prices and margin conversion. The stock-web path shows structural MFE with controlled early MAE, but source repair is needed before runtime weight promotion. | True | True |
| TRG_R1L73-C01-329180-HDHHI-LNG-NAVAL-BACKLOG-MARGIN-BRIDGE | 329180 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | C01 should allow Stage2 when shipbuilding backlog is not just order volume but connects to LNG/naval mix, rising newbuild prices and margin conversion. The stock-web path shows structural MFE with controlled early MAE, but source repair is needed before runtime weight promotion. | True | True |
| C03_R1L111_001_TRIGGER | 329180 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_correct | True | True |
| NEPESARK_330860_2024_03_06_STAGE2_FALSE_POSITIVE_TEST_SERVICE_PREMIUM | 330860 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_false_positive | False | True |
| R2L95_C10_NEPESARK_2024_STAGE2_FALSE_POSITIVE_OSAT_TEST_RECOVERY_WATCH | 330860 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_false_positive_if_OSAT_test_recovery_watch_counts_without_customer_order_utilization_margin_revision_bridge | True | True |
| R13L95_REVIEW_R2_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_330860_2024_02_22_TRIGGER | 330860 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_OSAT_test_recovery_watch_counts_without_customer_order_utilization_margin_revision_bridge | True | True |
| None | 335810 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | None | True | True |
| R7L86_C25_335890_20240216_STAGE2_AESTHETIC_DEVICE_EXPORT_BRIDGE | 335890 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_correct_if_export_channel_margin_bridge_required | True | True |
| V12_COMPACT_C25_R7L107_335890_20240408_Stage2_Actionable_335890_2024-04-08_Stage2-Actionable | 335890 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive | True | True |
| R7L97_C25_VIOL_2024_STAGE2_ACTIONABLE_AESTHETIC_DEVICE_EXPORT_CONSUMABLE_MARGIN_BRIDGE | 335890 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R7L88_C25_VIOL_2024_STAGE4B_AESTHETIC_DEVICE_EVENT_CAP | 335890 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_4B_too_late_if_aesthetic_device_theme_premium_not_capped | True | True |
| R13L86_REVIEW_R7_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_335890_2024-02-16 | 335890 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_correct | True | True |
| R11L87_C31_DSFUEL_2022_STAGE2_FALSE_POSITIVE_HYDROGEN_POLICY | 336260 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive_if_policy_score_counts_without_order_revenue_bridge | True | True |
| R12L83_C31_336260_20240522_STAGE2_FALSE_POSITIVE_HYDROGEN_POLICY_SPIKE | 336260 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | True | True |
| R13L87_REVIEW_C31_DSFUEL_2022_STAGE2_FALSE_POSITIVE_HYDROGEN_POLICY | 336260 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive_if_policy_score_counts_without_order_revenue_bridge | True | True |
| SOLUS_336370_2024_03_27_STAGE2A_COPPER_FOIL_ORDERBOOK_RELIEF | 336370 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_4B_too_late | False | True |
| TRG_R3L80-C12-336370-SOLUS-COPPERFOIL-POSTCA-CALLOFF-LIFECYCLE | 336370 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | C12 should not overblock post-CA copperfoil/material names when recovery MFE and bounded entry MAE are visible, but it still requires customer volume, utilization and margin evidence before Stage2 promotion. | True | True |
| R3L88_C14_336370_20240701_STAGE2_FALSE_POSITIVE_COPPERFOIL_BLOWOFF | 336370 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_false_positive_if_copperfoil_rebound_overcredited | True | True |
| R3L91_C14_SOLUS_2024_STAGE4B_COPPER_FOIL_EV_DEMAND_EVENT_CAP | 336370 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_4B_too_late_if_copper_foil_EV_demand_recovery_premium_not_capped | True | True |
| R3L100-C14-004-T1 | 336370 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_false_positive_if_copper_foil_capacity_label_overrides_customer_pull_break | True | True |
| C14-R3L97-03-336370-Stage4C-2024-07-31 | 336370 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_correct | True | True |
| R4L98_C16_SOLUS_2024_STAGE2_ACTIONABLE_COPPERFOIL_CRITICAL_MATERIAL_SUPPLY_BRIDGE | 336370 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R13L88_REVIEW_R3_C14_EV_DEMAND_SLOWDOWN_4B_4C_336370_2024-07-01 | 336370 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R13L91_REVIEW_R3_C14_EV_DEMAND_SLOWDOWN_4B_4C_336370_2024_04_11_TRIGGER | 336370 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_4B_too_late_if_copper_foil_EV_demand_recovery_premium_not_capped | True | True |
| V12_COMPACT_C25_R7L107_336570_20240617_Stage2_336570_2024-06-17_Stage2 | 336570 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive | True | True |
| TRG_R7L79-C25-336570-WONTECH-AESTHETIC-DEVICE-EXPORT-MARGIN-LIFECYCLE | 336570 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | C25 should allow medical-aesthetic device positives when export demand, distributor reorder, installed-base utilization, consumables/service revenue and margin bridge are visible. Wontech produced large MFE, then a high post-peak drawdown, so it needs lifecycle 4B if export/reorder/margin evidence fades. | True | True |
| None | 336570 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | None | True | True |
| R13_CROSS_336570_2024-06-17_Stage2 | 336570 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive | True | True |
| R13_CROSS_337930_2024-08-14_Stage4B | 337930 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | True | True |
| None | 337930 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | True | True |
| T_R13_STAGE2FP_L6_337930_Stage2Actionable_2024-05-20 | 337930 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_stage2_false_positive_or_overpromotion_risk | True | True |
| TRG_R11L75-C31-339950-IVY-KIMYOUNG-MEDQUOTA-ADMISSION-DEMAND-LIFECYCLE | 339950 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_correct | True | True |
| TRG_R11L75-C31-339950-IVY-KIMYOUNG-MEDQUOTA-ADMISSION-DEMAND-LIFECYCLE | 339950 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 can allow a policy-event lifecycle candidate when a medical-school quota policy shock connects to transfer/admission-course demand, paid enrollment, retention and margin bridge. Ivy Kimyoung produced large MFE, but the post-peak drawdown says lifecycle local 4B is mandatory if the policy-demand bridge fades. | True | True |
| R12L89_C31_IBKIMYOUNG_2024_STAGE4B_DIGITAL_EDU_POLICY_THEME_CAP | 339950 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_4B_too_late_if_digital_education_policy_theme_premium_not_capped | True | True |
| R13L89_REVIEW_C31_IBKIMYOUNG_2024_STAGE4B_DIGITAL_EDU_POLICY_THEME_CAP | 339950 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_4B_too_late_if_digital_education_policy_theme_premium_not_capped | True | True |
| TRG_C11_R3L105_006 | 340930 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive | True | True |
| V12_COMPACT_348210_2024-05-22_C07_INSPECTION_EQUIPMENT_RELATIVE_STRENGTH_WEAK_BRIDGE | 348210 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_false_positive | False | True |
| TRG_R2L80-C07-348210-NEXTIN-INSPECTION-METROLOGY-THEME-FADE | 348210 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | C07 should not treat semiconductor inspection/metrology theme beta as durable Stage2 unless HBM/customer order, capacity expansion, delivery, recurring service and margin bridge are visible. Nextin had small early MFE and then a deep MAE path, making it a local 4B boundary rather than Green. | True | True |
| None | 348210 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | False | True |
| NEXTEEN_348210_2024_03_06_STAGE2_FALSE_POSITIVE_ADVANCED_INSPECTION | 348210 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_false_positive | False | True |
| None | 348210 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | None | True | True |
| None | 348370 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_too_late_if_all_electrolyte_capacity_proxy_is_discarded_but_too_loose_if_Green_after_blowoff | True | True |
| T_C11_R3L107_348370_STAGE2ACTIONABLE_20240115 | 348370 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_too_late_if_orderbook_to_margin_bridge_is_confirmed | True | True |
| R3L93_C11_348370_20240129_STAGE2_ELECTROLYTE_ORDERBOOK_FCF | 348370 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_correct_if_customer_allocation_capacity_margin_FCF_bridge_required_but_data_quality_and_Green_strict | True | True |
| R3L83_C12_348370_20240112_STAGE2_ELECTROLYTE_CONTRACT_BRIDGE | 348370 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_correct | True | True |
| R3L98_C12_ENCHEM_2024_STAGE2_ACTIONABLE_ELECTROLYTE_CUSTOMER_CONTRACT_CAPA_BRIDGE | 348370 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| None | 348370 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_false_positive_if_broad_calloff_guard_routes_growth_exception_to_hard_4c | True | True |
| TRG_R3L76-C13-348370-ENCHEM-US-ELECTROLYTE-IRA-LOCAL-SUPPLY-LIFECYCLE | 348370 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_correct | True | True |
| TRG_R3L76-C13-348370-ENCHEM-US-ELECTROLYTE-IRA-LOCAL-SUPPLY-LIFECYCLE | 348370 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | C13 should allow Stage2 when US/IRA battery supply-chain attention connects to actual electrolyte local supply, customer qualification, utilization, AMPC or margin bridge. Enchem produced extreme MFE with controlled entry-basis MAE, but the post-peak drawdown and share-count changes require lifecycle local 4B and validation. | True | True |
| None | 348370 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | False | True |
| None | 348370 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | True | True |
| R5L88_C20_352480_20240305_STAGE2_BEAUTY_ODM_GLOBAL_ORDER | 352480 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_correct_if_global_order_margin_bridge_required | True | True |
| R13L88_REVIEW_R5_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_352480_2024-03-05 | 352480 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_correct | True | True |
| HYBE_352820_2024_03_25_STAGE2_FALSE_POSITIVE_FANDOM_IP_PLATFORM_RISK | 352820 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_false_positive | False | True |
| R8L97_C27_HYBE_2024_STAGE2_FALSE_POSITIVE_LABEL_PLATFORM_IP_RISK_WATCH | 352820 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_false_positive_if_label_platform_IP_watch_counts_without_release_pipeline_governance_margin_revision_bridge | True | True |
| None | 352820 | C27_CONTENT_IP_GLOBAL_MONETIZATION | None | True | True |
| R8L87_C27_352820_20240401_STAGE2_FALSE_POSITIVE_PLATFORM_IP_THEME | 352820 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_false_positive_if_platform_IP_theme_overcredited | True | True |
| C27-R8L105-020|Stage4C|2024-04-22 | 352820 | C27_CONTENT_IP_GLOBAL_MONETIZATION | residual_error_needs_C27_specific_bridge_or_guard | True | True |
| None | 352820 | C27_CONTENT_IP_GLOBAL_MONETIZATION | None | True | True |
| R13L87_REVIEW_R8_C27_CONTENT_IP_GLOBAL_MONETIZATION_352820_2024-04-01 | 352820 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| None | 352820 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| None | 352820 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| None | 352820 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| TRG_R2L75-C06-353200-DAEDUCK-FCBGA-MEMORY-PACKAGE-SUBSTRATE-BETA-FADE | 353200 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_false_positive | True | True |
| TRG_R2L75-C06-353200-DAEDUCK-FCBGA-MEMORY-PACKAGE-SUBSTRATE-BETA-FADE | 353200 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | C06 should not treat package substrate or AI memory-adjacent beta as durable Stage2 unless customer capacity, utilization, order or margin bridge refreshes. Daeduck Electronics produced limited MFE and then a severe 180D MAE path, making it a false Stage2/local 4B row. | True | True |
| None | 356680 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | None | False | True |
| C28_R8L103_04_356680_Stage2_Actionable_2024-09-02 | 356680 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_missed_structural | True | True |
| R8L97_C28_XGATE_2024_STAGE4B_NETWORK_SECURITY_GATEWAY_EVENT_CAP | 356680 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_4B_too_late_if_network_security_gateway_event_premium_not_capped | True | True |
| V12_COMPACT_C28_R8L104_356680_20240417_356680_2024-04-18_4B-Local-Watch | 356680 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive | True | True |
| V12_COMPACT_R13L12_ACCT_PRICE_13_C28_356680_20240821_356680_2024-08-21_Stage4B | 356680 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | True | True |
| R13_CROSS_356680_2024-01-26_Stage2 | 356680 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| R13_CROSS_356680_2024-01-26_Stage2 | 356680 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive | True | True |
| TLB_356860_2024_03_06_STAGE2_FALSE_POSITIVE_HBM_PCB_CAPA_PREMIUM | 356860 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_false_positive | False | True |
| R8L91_C28_CYBERONE_2024_STAGE4B_MSS_SECURITY_THEME_EVENT_CAP | 356890 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_4B_too_late_if_MSS_security_theme_premium_not_capped | True | True |
| R13L91_REVIEW_R8_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_356890_2024_06_04_TRIGGER | 356890 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_4B_too_late_if_MSS_security_theme_premium_not_capped | True | True |
| T_C06_R2L103_357780_20240401_Stage2Actionable_CROSS_C07 | 357780 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_needs_C06_vs_C07_C08_C09_reroute_guard | True | True |
| TRG-C06-L111-357780-Stage2Actionable-2025-01-02 | 357780 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_missed_structural | True | True |
| V12_COMPACT_357780_2024-04-01_Stage2-Actionable | 357780 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_false_positive | True | True |
| None | 357780 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | False | True |
| None | 357780 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | None | True | True |
| None | 357780 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | True | True |
| None | 358570 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | True | True |
| TRG_C11_R3L105_005 | 360070 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_too_late | True | True |
| R11L97_C03_GENOHCO_2024_STAGE2_FALSE_POSITIVE_SPACE_DEFENSE_COMPONENT_WATCH | 361390 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_false_positive_if_space_defense_component_watch_counts_without_prime_contract_export_backlog_delivery_margin_revision_bridge | True | True |
| R1L94_C03_XENOCO_2024_STAGE2_FALSE_POSITIVE_SPACE_DEFENSE_COMPONENT_HEADLINE | 361390 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_false_positive_if_space_defense_component_headline_counts_without_export_order_margin_bridge | True | True |
| None | 361390 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | None | False | True |
| R13L94_REVIEW_R1_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_361390_2024_01_24_TRIGGER | 361390 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive_if_space_defense_component_headline_counts_without_export_order_margin_bridge | True | True |
| TRG-C11-361610-20250227-STAGE2A | 361610 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_too_early_if_green | False | True |
| None | 361610 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_4B_too_late_if_separator_orderbook_label_is_treated_as_durable_C11 | True | True |
| T_C11_R3L107_361610_STAGE4C_20240115 | 361610 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive_if_orderbook_label_is_overcredited | True | True |
| TRG_R3L75-C12-361610-SK-IET-SEPARATOR-CUSTOMER-CALLOFF-RISK | 361610 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_false_positive | True | True |
| TRG_R3L75-C12-361610-SK-IET-SEPARATOR-CUSTOMER-CALLOFF-RISK | 361610 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | C12 should not treat separator beta as durable Stage2 unless customer call-off schedule, utilization, pricing and margin evidence refreshes. SK IET had a brief rebound but then opened severe MAE as EV demand and separator utilization risk dominated. | True | True |
| TRG_R3L78-C12-361610-SKIET-SEPARATOR-CALLOFF-LOCAL4B | 361610 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | C12 should not treat separator customer-contract exposure as durable Stage2 unless call-off volume, utilization, pricing and margin bridge refreshes. SK IE Technology had only a small early MFE and then a severe high-MAE drawdown path. | True | True |
| R3L86_C12_361610_20240325_STAGE2_FALSE_POSITIVE_SEPARATOR_UTILIZATION_RISK | 361610 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_false_positive_if_separator_contract_theme_overcredited | True | True |
| TRG_R3L80-C12-361610-SKIET-SEPARATOR-CALLOFF-UTILIZATION-LOCAL4B | 361610 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | C12 should flag separator/customer-calloff risk when customer volume, utilization, pricing and margin bridge weaken. SK IET produced only a small early MFE and then a deep high-MAE path. | True | True |
| None | 361610 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_correct_if_hard_4c_requires_utilization_calloff_margin_break | True | True |
| V12_COMPACT_C12_R3L105_361610_20240412_06_361610_2024-04-12_Stage4C | 361610 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_false_positive | True | True |
| T_C13_R3L103_361610_STAGE2_20240131 | 361610 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_false_positive_if_separator_beta_scores_like_AMPC_direct_capture | True | True |
| R3L84_C13_361610_20240319_STAGE2_FALSE_POSITIVE_SEPARATOR_UTILIZATION | 361610 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_false_positive_if_EV_JV_optionality_overcredited | True | True |
| T_C13_R3L105_361610_STAGE4C_20240115 | 361610 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | True | True |
| None | 361610 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | True | True |
| None | 361610 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | False | True |
| TRG_R3L73-C14-361610-SKIET-SEPARATOR-DEMAND-SLOWDOWN-LOCAL4B | 361610 | C14_EV_DEMAND_SLOWDOWN_4B_4C | C14 should fire local 4B-watch when EV demand slowdown translates into separator utilization pressure and the stock path opens severe MAE. Hard 4C still requires non-price evidence such as plant impairment, contract cancellation, insolvency, or structural customer loss. | True | True |
| TRG_R3L73-C14-361610-SKIET-SEPARATOR-DEMAND-SLOWDOWN-LOCAL4B | 361610 | C14_EV_DEMAND_SLOWDOWN_4B_4C | C14 should fire local 4B-watch when EV demand slowdown translates into separator utilization pressure and the stock path opens severe MAE. Hard 4C still requires non-price evidence such as plant impairment, contract cancellation, insolvency, or structural customer loss. | True | True |
| R3L88_C14_SKIET_2024_STAGE4C_SEPARATOR_UTILIZATION_BREAK | 361610 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_kept_true_4C_when_utilization_customer_calloff_and_margin_break_are_confirmed | True | True |
| T_C14_R3L108_361610_STAGE4C_20240115 | 361610 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_false_positive | True | True |
| R9L95_C14_SKIET_2024_STAGE4C_SEPARATOR_DEMAND_SLOWDOWN_THESIS_BREAK_GUARD | 361610 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_kept_but_C14_needs_earlier_4C_when_separator_utilization_and_customer_volume_bridge_breaks | True | True |
| R13L86_REVIEW_R3_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_361610_2024-03-25 | 361610 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| V12_COMPACT_R13L11-4B4C-003_361610_2024-01-15_cross_archetype_4b_4c_boundary_retest | 361610 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R13_4B4C_L12_02_361610_20240115_Stage4C_Watch | 361610 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_source_proxy_row_promotes_to_green_or_full_4B | True | True |
| R13L95_REVIEW_R9_C14_EV_DEMAND_SLOWDOWN_4B_4C_361610_2024_01_24_TRIGGER | 361610 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_kept_but_C14_needs_earlier_4C_when_separator_utilization_and_customer_volume_bridge_breaks | True | True |
| None | 361610 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| R13_CROSS_361610_2024-01-15_Stage4C | 361610 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | True | True |
| None | 361610 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | True | True |
| V12_COMPACT_R13L2_C12_361610_20240115_STAGE4C_361610_2024-01-15_cross_archetype_high_MAE_guardrail_review | 361610 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| TRG_R8L77-C26-363260-MOBIDAYS-POST-CA-ADTECH-THEME-FADE | 363260 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| None | 363260 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | None | False | True |
| TRG_R8L77-C26-363260-MOBIDAYS-POST-CA-ADTECH-THEME-FADE | 363260 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | C26 should not treat post-corporate-action adtech theme spikes as durable Stage2 unless advertiser budget, campaign ROAS, platform revenue retention and operating leverage bridge are verified. Mobidays was measured only after the 2024-05-24 corporate-action candidate; the post-entry path showed weak MFE and high MAE, so it is a post-CA local 4B boundary. | True | True |
| V12_COMPACT_363260_2024-04-18_platform_ad_budget_retention_opm_bridge_cleanup | 363260 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| R7L90_C24_CURACLE_2024_STAGE2_FALSE_POSITIVE_TRIAL_DATA_EVENT | 365270 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_false_positive_if_trial_data_event_counts_without_endpoint_partner_runway_bridge | True | True |
| R7L90_C24_365270_20240320_STAGE2_FALSE_POSITIVE_VASCULAR_EVENT | 365270 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_false_positive_if_trial_event_spike_overcredited | True | True |
| R13L90_REVIEW_R7_C24_BIO_TRIAL_DATA_EVENT_RISK_365270_2024_03_20_TRIGGER | 365270 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive_if_trial_data_event_counts_without_endpoint_partner_runway_bridge | True | True |
| R3L93_C14_365340_20240221_STAGE2_4B_RECYCLING_DEMAND_DECAY | 365340 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_correct_if_recycling_capacity_vocabulary_routes_to_4B_when_EV_demand_and_cash_bridge_missing | True | True |
| R5L90_C19_09WOMEN_2024_STAGE4B_SIZE_APPAREL_RETAIL_THEME_CAP | 366030 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_4B_too_late_if_size_apparel_retail_theme_premium_not_capped | True | True |
| R5L98_C19_GONGGUWOMEN_2024_STAGE4B_SMALL_CAP_APPAREL_BRAND_EVENT_CAP | 366030 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_4B_too_late_if_small_cap_apparel_brand_event_premium_not_capped | True | True |
| R13_4B4C_L101_T006_366030 | 366030 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | false_positive_if_brand_spike_lacks_reorder_margin_bridge | True | True |
| R13_CROSS_366030_2024-10-14_Stage4B | 366030 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | True | True |
| R13L90_REVIEW_R5_C19_BRAND_RETAIL_INVENTORY_MARGIN_366030_2024_01_31_TRIGGER | 366030 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_4B_too_late_if_size_apparel_retail_theme_premium_not_capped | True | True |
| None | 366030 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | True | True |
| R9L97_C29_FUTURENURI_2024_STAGE4B_AUTONOMOUS_CAMERA_MODULE_EVENT_CAP | 370090 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_4B_too_late_if_autonomous_camera_module_event_premium_not_capped | True | True |
| T_C11_R3L107_373220_STAGE2ACTIONABLE_20240312 | 373220 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive_if_orderbook_label_is_overcredited | True | True |
| TRG-C11-373220-20240725-STAGE2A | 373220 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_correct_with_green_delay_risk | False | True |
| R3L93_C12_373220_20240910_STAGE2_LARGE_CELL_CALLOFF_STABILIZATION | 373220 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_correct_if_contract_visibility_calloff_ASP_margin_cash_bridge_required_but_Green_strict | True | True |
| V12_COMPACT_C12_R3L105_373220_20241010_01_373220_2024-10-10_Stage2-Actionable | 373220 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_false_positive | True | True |
| None | 373220 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | True | True |
| None | 373220 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | True | True |
| R3L92_C13_LGES_2024_STAGE2_FALSE_POSITIVE_CELL_AMPC_UTILIZATION_REBOUND | 373220 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_false_positive_if_cell_AMPC_utilization_rebound_counts_without_customer_volume_margin_bridge | True | True |
| T_C13_R3L105_373220_STAGE2ACTIONABLE_20240312 | 373220 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | True | True |
| V12_COMPACT_C13-102-01_373220_2024-08-21_Stage2-Actionable | 373220 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_false_positive | True | True |
| R3L84_C13_373220_20240821_STAGE2_AMPC_JV_UTILIZATION_BRIDGE | 373220 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_correct_if_utilization_bridge_required | True | True |
| None | 373220 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | True | True |
| None | 373220 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | False | True |
| R3L98_C14_LGES_2024_STAGE2_FALSE_POSITIVE_CELLMAKER_UTILIZATION_REBOUND_WATCH | 373220 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_false_positive_if_cellmaker_rebound_watch_counts_without_calloff_utilization_margin_revision_bridge | True | True |
| None | 373220 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | None | False | True |
| None | 373220 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| R13_CROSS_R13L4_C11_373220_20240201_ORDERBOOK_ACCEPTANCE_PAYMENT_373220_2024-02-01_Stage2 | 373220 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | True | True |
| None | 373220 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | None | True | True |
| None | 373220 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | True | True |
| R13_L106_T15_373220 | 373220 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive | True | True |
| R13L92_REVIEW_R3_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_373220_2024_02_16_TRIGGER | 373220 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive_if_cell_AMPC_utilization_rebound_counts_without_customer_volume_margin_bridge | True | True |
| T_R13_STAGE2FP_L5_373220_Stage2Actionable_2024-03-12 | 373220 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_stage2_false_positive_or_overpromotion_risk | True | True |
| T_C05_R1L109_375500_20240205_LOW_PBR_BUILDER_WITHOUT_PROJECT_MARGIN | 375500 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | True | True |
| T_C05_R1L108_375500_20240429_LOW_PBR_EPC_REBOUND | 375500 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | True | True |
| None | 375500 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | False | True |
| T_C05_R1L108_375500_20240613_EPC_LOCAL4B_DECAY | 375500 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | True | True |
| V12_COMPACT_375500_2024-04-29_low_pbr_balance_sheet_label_without_revision_followthrough | 375500 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive | False | True |
| None | 375500 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | True | True |
| C30_R10L105_375500_20240429_Stage2_Actionable | 375500 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_error_if_C30_overcredits_price_or_low_PBR_without_balance_sheet_bridge | True | True |
| C30_R10L104_375500_20240613_4B_Local_Watch | 375500 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive_if_full_4B | True | True |
| None | 375500 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| T_R13_STAGE2FP_L5_375500_Stage2Actionable_2024-04-29 | 375500 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_stage2_false_positive_or_overpromotion_risk | True | True |
| TRG_R8L73-C26-376300-DEARU-SUBSCRIPTION-PLATFORM-OPERATING-LEVERAGE | 376300 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | C26 should allow Stage2 when a platform has subscription/user or ARPU expansion that can convert into operating leverage. DearU produced very high MFE with almost no entry-basis MAE, but later local 4B-watch is still needed if subscriber/artist expansion evidence stops refreshing after the peak. | True | True |
| TRG_R8L73-C26-376300-DEARU-SUBSCRIPTION-PLATFORM-OPERATING-LEVERAGE | 376300 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | C26 should allow Stage2 when a platform has subscription/user or ARPU expansion that can convert into operating leverage. DearU produced very high MFE with almost no entry-basis MAE, but later local 4B-watch is still needed if subscriber/artist expansion evidence stops refreshing after the peak. | True | True |
| R8L93_C27_376300_20241010_STAGE2_FAN_PLATFORM_SUBSCRIPTION | 376300 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_correct_if_subscription_retention_artist_lineup_margin_cash_bridge_required_but_Green_strict | True | True |
| C27-R8L105-006|Stage3-Yellow|2024-02-22 | 376300 | C27_CONTENT_IP_GLOBAL_MONETIZATION | residual_error_needs_C27_specific_bridge_or_guard | True | True |
| TRG_R6L75-C21-377300-KAKAOPAY-DIGITAL-FINANCE-PBR-BETA-FADE | 377300 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | True | True |
| TRG_R6L75-C21-377300-KAKAOPAY-DIGITAL-FINANCE-PBR-BETA-FADE | 377300 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | C21 should not treat digital-finance/value-up beta as durable Stage2 unless ROE inflection, capital return, profitability and shareholder-return bridge are visible. KakaoPay produced an event spike but then entered a long high-MAE decline, making it a false Stage2/local 4B row. | True | True |
| R6L85_C21_377300_20240115_STAGE2_FALSE_POSITIVE_FINTECH_PAYMENT_BETA | 377300 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive_if_fintech_beta_overcredited | True | True |
| R6L96_C21_KAKAOPAY_2024_STAGE4B_FINTECH_VALUEUP_PROFITABILITY_EVENT_CAP | 377300 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_4B_too_late_if_fintech_valueup_profitability_event_premium_not_capped | True | True |
| R13L96_REVIEW_R6_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_377300_2024_01_11_TRIGGER | 377300 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late_if_fintech_valueup_profitability_event_premium_not_capped | True | True |
| R13L85_REVIEW_R6_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_377300_2024-01-15 | 377300 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| GITECH_382480_2024_03_12_STAGE2_FALSE_POSITIVE_SMALLCAP_ORDERBOOK | 382480 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive | False | True |
| TRG_C11_R3L105_002 | 382480 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive | True | True |
| R3L98-C14-003-T1 | 382480 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_false_positive_if_battery_equipment_theme_stays_actionable_without_delivery_bridge | True | True |
| R13_L106_T05_382480 | 382480 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive | True | True |
| R3L89_C11_ONEJOON_2024_STAGE2_FALSE_POSITIVE_EQUIPMENT_ORDERBOOK_THEME | 382840 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive_if_equipment_orderbook_theme_counts_without_order_margin_revision_bridge | True | True |
| None | 382840 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive_if_equipment_orderbook_proxy_promotes_Yellow | True | True |
| R3L93_C11_WONJUN_2024_STAGE2_FALSE_POSITIVE_BATTERY_EQUIPMENT_ORDERBOOK_WATCH | 382840 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive_if_battery_equipment_orderbook_watch_counts_without_customer_delivery_margin_bridge | True | True |
| R3L88_C14_382840_20240312_STAGE2_FALSE_POSITIVE_BATTERY_EQUIPMENT_REBOUND | 382840 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_false_positive_if_battery_equipment_rebound_overcredited | True | True |
| R3L99-C14-001-T1 | 382840 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_false_positive_if_equipment_backlog_memory_overrides_demand_reset | True | True |
| R13L88_REVIEW_R3_C14_EV_DEMAND_SLOWDOWN_4B_4C_382840_2024-03-12 | 382840 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R13L93_REVIEW_R3_C11_BATTERY_ORDERBOOK_RERATING_382840_2024_02_21_TRIGGER | 382840 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_battery_equipment_orderbook_watch_counts_without_customer_delivery_margin_bridge | True | True |
| R5L99_C18_FNF_2024_STAGE2_FALSE_POSITIVE_APPAREL_EXPORT_CHANNEL_INVENTORY_WATCH | 383220 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive_if_apparel_export_channel_watch_counts_without_sellthrough_reorder_inventory_OPM_revision_bridge | True | True |
| None | 383220 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | True | True |
| R5_L121_C18_004 | 383220 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | True | True |
| None | 383220 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | False | True |
| 383220_2023-05-16_Stage2_C19_PREMIUM_BRAND_INVENTORY_MARGIN_FALSE_POSITIVE | 383220 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_false_positive | False | True |
| R5L97_C19_FNF_2024_STAGE2_FALSE_POSITIVE_APPAREL_CHINA_INVENTORY_WATCH | 383220 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_false_positive_if_apparel_inventory_watch_counts_without_sellthrough_markdown_inventory_margin_revision_bridge | True | True |
| R5L90_C19_383220_20240401_STAGE2_FALSE_POSITIVE_APPAREL_INVENTORY | 383220 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_false_positive_if_apparel_brand_rebound_overcredited | True | True |
| C19_R5L119_20_383220_4B_Local_Watch_2024-07-17 | 383220 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | True | True |
| V12_COMPACT_C20_R5L120_383220_20240717_05_383220_2024-07-17_Local-4B-Watch | 383220 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | True | True |
| None | 383220 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | True | True |
| None | 383220 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | None | True | True |
| R1L88_C02_388050_20240529_STAGE2_FALSE_POSITIVE_SMALLCAP_GRID_THEME | 388050 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_false_positive_if_smallcap_grid_theme_overcredited | True | True |
| R13L88_REVIEW_R1_C02_POWER_GRID_DATACENTER_CAPEX_388050_2024-05-29 | 388050 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R2L98_C09_ZARAM_2024_STAGE4B_AI_SEMICONDUCTOR_IP_EVENT_CAP | 389020 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_4B_too_late_if_AI_semiconductor_IP_event_premium_not_capped | True | True |
| TRG-C06-L110-389260-Stage4B-2024-04-18 | 389260 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_4B_too_late | True | True |
| R3L85_C11_393890_20240221_STAGE2_FALSE_POSITIVE_SEPARATOR_ORDERBOOK_THEME | 393890 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive_if_separator_orderbook_theme_overcredited | True | True |
| T_C11_R3L107_393890_STAGE4C_20240213 | 393890 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive_if_orderbook_label_is_overcredited | True | True |
| None | 393890 | C11_BATTERY_ORDERBOOK_RERATING | None | True | True |
| V12_COMPACT_C12_R3L105_393890_20240322_09_393890_2024-03-22_Stage2-False-Positive | 393890 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_false_positive | True | True |
| TRG_R3L78-C12-393890-WCP-SEPARATOR-CUSTOMER-CALLOFF-FADE | 393890 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | C12 should not treat separator customer-calloff exposure as durable Stage2 unless customer order, utilization, shipment and margin bridge are visible. WCP had tradable MFE but then a deep post-peak drawdown, making it local 4B-watch rather than durable Green. | True | True |
| WCP_393890_2024_02_21_4C_SEPARATOR_CALL_OFF_RISK | 393890 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_4C_too_late | False | True |
| T_C13_R3L103_393890_STAGE2_20240213 | 393890 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_false_positive_if_separator_contract_label_lacks_calloff | True | True |
| R3L92_C13_WCP_2024_STAGE4B_SEPARATOR_AMPC_EVENT_CAP | 393890 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_4B_too_late_if_separator_AMPC_event_premium_not_capped | True | True |
| R9L89_C13_WCP_2024_STAGE4B_SEPARATOR_UTILIZATION_CAP | 393890 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_4B_too_late_if_separator_utilization_event_premium_not_capped | True | True |
| T_C13_R3L104_393890_STAGE4C_20240213 | 393890 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | True | True |
| None | 393890 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | True | True |
| R9L95_C14_WCP_2024_STAGE2_FALSE_POSITIVE_SEPARATOR_CAPACITY_RECOVERY_WATCH | 393890 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_false_positive_if_separator_capacity_recovery_watch_counts_without_customer_calloff_utilization_margin_revision_bridge | True | True |
| TRG_R3L73-C14-393890-WCP-SEPARATOR-CUSTOMER-DEMAND-LOCAL4B | 393890 | C14_EV_DEMAND_SLOWDOWN_4B_4C | Separator suppliers need stricter C14 treatment than diversified cell or chemical names. WCP produced initial MFE, but the later 180D MAE and post-peak drawdown show customer demand/utilization risk converting into local 4B-watch. | True | True |
| TRG_R3L73-C14-393890-WCP-SEPARATOR-CUSTOMER-DEMAND-LOCAL4B | 393890 | C14_EV_DEMAND_SLOWDOWN_4B_4C | Separator suppliers need stricter C14 treatment than diversified cell or chemical names. WCP produced initial MFE, but the later 180D MAE and post-peak drawdown show customer demand/utilization risk converting into local 4B-watch. | True | True |
| R13_4B4C_L12_18_393890_20240213_Stage2_Actionable | 393890 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_source_proxy_row_promotes_to_green_or_full_4B | True | True |
| R13L95_REVIEW_R9_C14_EV_DEMAND_SLOWDOWN_4B_4C_393890_2024_02_22_TRIGGER | 393890 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_separator_capacity_recovery_watch_counts_without_customer_calloff_utilization_margin_revision_bridge | True | True |
| R13L85_REVIEW_R3_C11_BATTERY_ORDERBOOK_RERATING_393890_2024-02-21 | 393890 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | True | True |
| R13L89_REVIEW_C13_WCP_2024_STAGE4B_SEPARATOR_UTILIZATION_CAP | 393890 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_4B_too_late_if_separator_utilization_event_premium_not_capped | True | True |
| T_R13_STAGE2FP_L5_393890_Stage2_2024-02-13 | 393890 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_stage2_false_positive_or_overpromotion_risk | True | True |
| R13L92_REVIEW_R3_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_393890_2024_02_22_TRIGGER | 393890 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_4B_too_late_if_separator_AMPC_event_premium_not_capped | True | True |
| R2L90_C06_394280_20240222_STAGE2_FALSE_POSITIVE_AI_IP_BLOWOFF | 394280 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_false_positive_if_AI_IP_blowoff_counted_as_HBM_capacity | True | True |
| R3L90_C12_SEAMECHANICS_2024_STAGE4B_EV_PARTS_CUSTOMER_PROGRAM_CAP | 396300 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_4B_too_late_if_EV_parts_customer_program_premium_not_capped | True | True |
| R13L90_REVIEW_R3_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_396300_2024_03_08_TRIGGER | 396300 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_4B_too_late_if_EV_parts_customer_program_premium_not_capped | True | True |
| R13_L106_T09_396470 | 396470 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_4B_too_late | True | True |
| R7L90_C24_APRILBIO_2024_STAGE2_ACTIONABLE_TRIAL_DATA_LICENSING_BRIDGE | 397030 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| V12_COMPACT_C28_R8L104_402030_20240419_402030_2024-04-22_4B-Local-Watch | 402030 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive | True | True |
| R2L93_C06_402340_20240201_STAGE2_HBM_MEMORY_LOOKTHROUGH | 402340 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_correct_if_HBM_mix_capacity_FCF_bridge_and_holdco_discount_repair_required_but_Green_strict | True | True |
| R12L93_C32_SKSQUARE_2024_STAGE2_ACTIONABLE_HOLDCO_NAV_CAPITAL_RETURN_BRIDGE | 402340 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R11L83_C32_402340_20240202_STAGE2_HOLDCO_NAV_RETURN_BRIDGE_POSITIVE | 402340 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_correct | True | True |
| R13L83_HIGHMAE_REVIEW_402340_2024-02-02 | 402340 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_correct | True | True |
| TRG_R9L82-C29-403550-SOCAR-CARSHARING-UTILIZATION-MARGIN | 403550 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 can protect car-sharing/platform mobility positives only when fleet utilization, active user demand, pricing, unit economics, revenue conversion and margin bridge are visible. Socar had controlled entry-basis MAE and strong MFE, but stock-web share count changes require validation before runtime promotion. | True | True |
| T_C06_R2L103_403870_20240304_Stage4BLocal_CROSS_C07 | 403870 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_needs_C06_vs_C07_C08_C09_reroute_guard | True | True |
| V12_COMPACT_403870_2024-03-04_Stage4B-Local | 403870 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_false_positive | True | True |
| R2L83_C09_403870_20240213_STAGE2_FALSE_POSITIVE_HIGH_MAE | 403870 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_false_positive | True | True |
| TRG_R2L79-C09-403870-HPSP-ADVANCED-EQUIPMENT-VALUATION-BLOWOFF | 403870 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | C09 should detect advanced-equipment valuation blowoff when a large MFE arrives before refreshed tool order, customer capacity and margin evidence. HPSP produced a huge early MFE and then a deep MAE/post-peak drawdown; runtime ingestion also needs share-count validation. | True | True |
| T_C09_R2L111_06_403870_20240304 | 403870 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_false_positive | True | True |
| R2L89_C10_403870_20240118_STAGE2_HBM_EQUIPMENT_RAMP | 403870 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_correct_if_customer_ramp_shipment_margin_bridge_required | True | True |
| QRT_405100_2024_01_18_STAGE2A_RELIABILITY_TEST_CUSTOMER_QUALITY | 405100 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_4B_too_late | False | True |
| C08_R2_L112_005_405100_Stage4B | 405100 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_false_positive | True | True |
| R2L98_C09_QRT_2024_STAGE2_FALSE_POSITIVE_TEST_RELIABILITY_EQUIPMENT_WATCH | 405100 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_false_positive_if_test_reliability_equipment_watch_counts_without_customer_order_utilization_margin_revision_bridge | True | True |
| None | 406820 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | True | True |
| R5L98_C20_BEAUTYSKIN_2024_STAGE4B_SMALL_CAP_K_BEAUTY_EVENT_CAP | 406820 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_4B_too_late_if_small_cap_K_beauty_event_premium_not_capped | True | True |
| TRG_R12L77-C31-407400-GGUMBI-LOW-BIRTH-BABYPRODUCT-THEME-FADE | 407400 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | True | True |
| TRG_R12L77-C31-407400-GGUMBI-LOW-BIRTH-BABYPRODUCT-THEME-FADE | 407400 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should not treat baby-product / low-birth policy theme spikes as durable Stage2 unless policy support maps to direct demand, channel sell-through, replenishment and margin bridge. Ggumbi produced an early MFE and then a severe drawdown path. | True | True |
| TRG_R11L81-C31-407400-GGUMBI-CHILDCARE-POLICY-THEME-FADE | 407400 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should not treat babycare/childcare policy beta as durable Stage2 unless direct beneficiary policy, customer demand, channel sell-through, product revenue and margin bridge are visible. Ggumbi produced a modest MFE but then a high-MAE drawdown. | True | True |
| R12L95_C31_GGUMBI_2024_STAGE4B_INFANT_CARE_POLICY_EVENT_CAP | 407400 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_4B_too_late_if_infant_care_policy_event_premium_not_capped | True | True |
| R13L95_REVIEW_R12_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_407400_2024_01_03_TRIGGER | 407400 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late_if_infant_care_policy_event_premium_not_capped | True | True |
| R8L90_C27_STUDIOMIR_2024_STAGE2_FALSE_POSITIVE_OUTSOURCE_ANIMATION | 408900 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_false_positive_if_content_production_theme_counts_without_owned_IP_or_recurring_monetization_bridge | True | True |
| R13L90_REVIEW_R8_C27_CONTENT_IP_GLOBAL_MONETIZATION_408900_2024_06_26_TRIGGER | 408900 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive_if_content_production_theme_counts_without_owned_IP_or_recurring_monetization_bridge | True | True |
| C28_R8L103_05_411080_Stage3_Yellow_2024-04-01 | 411080 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_4B_too_late | True | True |
| R8L98_C28_SANDSLAB_2024_STAGE4B_CYBERSECURITY_AI_EVENT_CAP | 411080 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_4B_too_late_if_cybersecurity_AI_event_premium_not_capped | True | True |
| R13HMG_L104_T003_411080 | 411080 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_needs_high_MAE_overlay_or_green_block | True | True |
| V12_COMPACT_412350_2024-04-23_C07_LASER_BONDING_EVENT_CAP_FALSE_STAGE2 | 412350 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_false_positive | False | True |
| R2L88_C09_412350_20240502_STAGE2_FALSE_POSITIVE_LASER_THEME | 412350 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_false_positive_if_laser_theme_overcredited | True | True |
| R13L88_REVIEW_R2_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_412350_2024-05-02 | 412350 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R3L96_C11_NANOTIM_2024_STAGE4B_THERMAL_MANAGEMENT_BATTERY_ORDER_EVENT_CAP | 417010 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_4B_too_late_if_thermal_management_battery_order_event_premium_not_capped | True | True |
| R13L96_REVIEW_R3_C11_BATTERY_ORDERBOOK_RERATING_417010_2024_03_26_TRIGGER | 417010 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late_if_thermal_management_battery_order_event_premium_not_capped | True | True |
| R8L90_C27_FINGERSTORY_2024_STAGE4B_WEBTOON_PLATFORM_THEME_CAP | 417180 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_4B_too_late_if_webtoon_platform_theme_premium_not_capped | True | True |
| R13L90_REVIEW_R8_C27_CONTENT_IP_GLOBAL_MONETIZATION_417180_2024_01_24_TRIGGER | 417180 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_4B_too_late_if_webtoon_platform_theme_premium_not_capped | True | True |
| R3L90_C12_417200_20240102_STAGE2_FALSE_POSITIVE_SUPERCAP_IPO_THEME | 417200 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_false_positive_if_supercapacitor_EV_theme_overcredited | True | True |
| C14-R3L97-05-417200-Stage4B-2025-03-31 | 417200 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_false_positive_if_hard_4c_without_recovery_band | True | True |
| R8L95_C26_OBZEN_2024_STAGE4B_AI_MARKETING_SAAS_EVENT_CAP | 417860 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_4B_too_late_if_AI_marketing_SaaS_event_premium_not_capped | True | True |
| R13L95_REVIEW_R8_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_417860_2024_01_09_TRIGGER | 417860 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late_if_AI_marketing_SaaS_event_premium_not_capped | True | True |
| R3L89_C11_JEO_2024_STAGE4B_CNT_CONDUCTIVE_ADDITIVE_CAP | 418550 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_4B_too_late_if_CNT_material_event_premium_not_capped | True | True |
| R3L94_C12_JEO_2024_STAGE2_FALSE_POSITIVE_CNT_MATERIAL_CALLOFF_WATCH | 418550 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_false_positive_if_CNT_material_calloff_watch_counts_without_customer_ramp_margin_revision_bridge | True | True |
| R13L94_REVIEW_R3_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_418550_2024_02_21_TRIGGER | 418550 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive_if_CNT_material_calloff_watch_counts_without_customer_ramp_margin_revision_bridge | True | True |
| R3L97_C12_SAMGIEV_2024_STAGE4B_BATTERY_CASE_CUSTOMER_CONTRACT_EVENT_CAP | 419050 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_4B_too_late_if_battery_case_contract_event_premium_not_capped | True | True |
| R8L90_C27_SAMG_2024_STAGE2_ACTIONABLE_KIDS_IP_MERCH_MONETIZATION | 419530 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| R2L93C_C08_420770_20240404_STAGE2_FALSE_POSITIVE_PACKAGE_INSPECTION_SPIKE | 420770 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_false_positive_if_package_inspection_theme_spike_overcredited | True | True |
| MICRO2NANO_424980_2024_03_06_STAGE2_FALSE_POSITIVE_PROBE_CARD_EVENT | 424980 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_false_positive | False | True |
| M2N_424980_2024_04_02_STAGE2_FALSE_POSITIVE_MEMS_PROBE_CARD | 424980 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_false_positive | False | True |
| R2L96_C08_MICRO2NANO_2024_STAGE2_ACTIONABLE_MEMS_PROBE_CARD_CUSTOMER_QUALITY_BRIDGE | 424980 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| C08_R2L97_424980_STAGE4B_20240423_MEMS_PROBE_CARD_PRICE_SPIKE | 424980 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_4B_too_late | True | True |
| TRG_C09_R2L98_M2N_20240423_MEMS_PROBE_BLOWOFF | 424980 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_too_early | False | True |
| R2L94_C07_TFE_2024_STAGE4B_HBM_SOCKET_PACKAGE_EVENT_CAP | 425420 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_4B_too_late_if_HBM_socket_package_event_premium_not_capped | True | True |
| TFE_425420_2024_03_06_STAGE2_FALSE_POSITIVE_SOCKET_PROBE_PREMIUM | 425420 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_false_positive | False | True |
| C08_R2L97_425420_STAGE2_20240308_TEST_SOCKET_CHANNEL_FALSE_STAGE2 | 425420 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_false_positive | True | True |
| TFE_425420_2024_03_08_STAGE2_FALSE_POSITIVE_SOCKET_THEME | 425420 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_false_positive | False | True |
| None | 425420 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | False | True |
| TRG_R2L78-C08-425420-TFE-TEST-SOCKET-CUSTOMER-QUALITY-LIFECYCLE | 425420 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | C08 should allow test-socket / probe-pin positives only when customer quality, HBM or advanced package qualification, reorder cadence and margin bridge are visible. TFE had strong early MFE, but the later drawdown means the signal must be lifecycle-managed if quality/reorder/margin evidence fades. | True | True |
| R2L87_C08_425420_20240320_STAGE2_FALSE_POSITIVE_SOCKET_BLOWOFF | 425420 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_false_positive_if_socket_beta_overcredited | True | True |
| TRG_R2L81-C08-425420-TFE-TEST-SOCKET-CUSTOMER-QUALITY-LIFECYCLE | 425420 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | C08 should preserve test-socket/interface-board positives when customer quality, reorder visibility, capacity utilization, delivery cadence and margin bridge are visible. TFE produced a large MFE, but the later high-MAE drawdown forces lifecycle local 4B if reorder/margin evidence fades. | True | True |
| C08_425420_2024_03_20_TEST_INTERFACE_PRICE_ONLY_BETA_DECAY_Stage4B | 425420 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_correct | False | True |
| TRG_C09_R2L98_TFE_20240320_TEST_HANDLER_BLOWOFF_FAIL | 425420 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_false_positive | False | True |
| R13L87_REVIEW_R2_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_425420_2024-03-20 | 425420 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R13L94_REVIEW_R2_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_425420_2024_03_20_TRIGGER | 425420 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_4B_too_late_if_HBM_socket_package_event_premium_not_capped | True | True |
| R8L96_C27_YLAB_2024_STAGE2_ACTIONABLE_WEBTOON_IP_GLOBAL_OPTIONALITY_BRIDGE | 432430 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_kept_but_source_proxy_blocks_positive_delta | True | True |
| C28_R8L103_03_434480_Stage3_Yellow_2024-05-02 | 434480 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive | True | True |
| R8L94_C28_MONITORLAB_2024_STAGE4B_WAF_CLOUD_SECURITY_EVENT_CAP | 434480 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_4B_too_late_if_WAF_cloud_security_event_premium_not_capped | True | True |
| R13L94_REVIEW_R8_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_434480_2024_04_03_TRIGGER | 434480 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_4B_too_late_if_WAF_cloud_security_event_premium_not_capped | True | True |
| T_C26_R8L106_07_443250_STAGE2_Stage2_2024-02-26 | 443250 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_4b_too_early_high_mae | True | True |
| V12_COMPACT_443250_2024-05-13_platform_ad_budget_retention_opm_bridge_cleanup | 443250 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | True | True |
| None | 443250 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | None | False | True |
| None | 443250 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | None | True | True |
| V12_COMPACT_R13L12_ACCT_PRICE_01_C26_443250_20240226_443250_2024-02-26_Stage2 | 443250 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | True | True |
| None | 448710 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | None | False | True |
| TRG_R3L80-C12-450080-ECOPRO-MATERIALS-PRECURSOR-CALLOFF-FADE | 450080 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | C12 should not treat precursor/material contract beta as durable Stage2 unless customer call-off, volume visibility, utilization, pricing and margin bridge remain visible. Ecopro Materials had an early MFE but then opened a severe high-MAE drawdown path. | True | True |
| R3L90_C12_450080_20240213_STAGE2_FALSE_POSITIVE_PRECURSOR_REBOUND | 450080 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_false_positive_if_precursor_rebound_overcredited | True | True |
| R3L98_C12_ECOPROMATERIALS_2024_STAGE4B_PRECURSOR_MATERIAL_CALLOFF_EVENT_CAP | 450080 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_4B_too_late_if_precursor_material_contract_event_premium_not_capped | True | True |
| ECOPROMAT_450080_2024_02_13_STAGE2_FALSE_POSITIVE_PRECURSOR_CAPA_IRA | 450080 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_false_positive | False | True |
| R3L95_C13_ECOPROMATERIALS_2024_STAGE4B_PRECURSOR_IRA_EVENT_CAP | 450080 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_4B_too_late_if_precursor_IRA_JV_utilization_event_premium_not_capped | True | True |
| R3L99-C14-007-T1 | 450080 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_false_positive_if_contract_size_memory_blocks_late_cycle_4C | True | True |
| R13L95_REVIEW_R3_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_450080_2024_06_10_TRIGGER | 450080 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late_if_precursor_IRA_JV_utilization_event_premium_not_capped | True | True |
| R11L95_C03_CONTEC_2024_STAGE4B_SATELLITE_GROUND_STATION_EVENT_CAP | 451760 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_4B_too_late_if_satellite_ground_station_space_event_premium_not_capped | True | True |
| R13L95_REVIEW_R11_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_451760_2024_01_11_TRIGGER | 451760 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late_if_satellite_ground_station_space_event_premium_not_capped | True | True |
| TRG_R12L73-C32-454910-DOOSANROBOTICS-VALUATION-BETA-LOCAL4B | 454910 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should cap the acquirer/beneficiary valuation beta when the proposed restructuring implies control benefit but no earnings or closing bridge. Doosan Robotics had a large first-day MFE and then severe MAE, so price-only governance beta should be local 4B-watch. | False | True |
| TRG_R12L73-C32-454910-DOOSANROBOTICS-VALUATION-BETA-LOCAL4B | 454910 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should cap the acquirer/beneficiary valuation beta when the proposed restructuring implies control benefit but no earnings or closing bridge. Doosan Robotics had a large first-day MFE and then severe MAE, so price-only governance beta should be local 4B-watch. | False | True |
| R11L91_C04_457550_20240126_STAGE2_FALSE_POSITIVE_RECENT_LISTING_NUCLEAR_SPIKE | 457550 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive_if_recent_listing_nuclear_spike_overcredited | True | True |
| R12L91_C31_WOOJINENTEC_2024_STAGE4B_NUCLEAR_POLICY_IPO_EVENT_CAP | 457550 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_4B_too_late_if_nuclear_policy_IPO_event_premium_not_capped | True | True |
| R13L91_REVIEW_R12_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_457550_2024_04_05_TRIGGER | 457550 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_4B_too_late_if_nuclear_policy_IPO_event_premium_not_capped | True | True |
| None | 950130 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | None | True | True |
| R7L92_C23_KOLONTISSUEGENE_2024_STAGE4B_GENE_THERAPY_REGULATORY_EVENT_CAP | 950160 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_4B_too_late_if_gene_therapy_regulatory_event_premium_not_capped | True | True |
| None | 950160 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | True | True |
| R13L92_REVIEW_R7_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_950160_2024_07_15_TRIGGER | 950160 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_4B_too_late_if_gene_therapy_regulatory_event_premium_not_capped | True | True |
| TRG_R7L73-C23-950210-PRESTIGE-BIOSIMILAR-APPROVAL-HEADLINE-CHASE | 950210 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | C23 should not convert a late approval/regulatory headline chase into durable Stage2 unless reimbursement, launch timing, partner orders and sales bridge are visible. The stock showed same-day MFE but later MAE and drawdown widened. | True | True |
| TRG_R7L73-C23-950210-PRESTIGE-BIOSIMILAR-APPROVAL-HEADLINE-CHASE | 950210 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | C23 should not convert a late approval/regulatory headline chase into durable Stage2 unless reimbursement, launch timing, partner orders and sales bridge are visible. The stock showed same-day MFE but later MAE and drawdown widened. | True | True |
| TRG_R7L74-C24-950220-NEOIMMUNETECH-IMMUNOTHERAPY-TRIAL-HEADLINE-FADE | 950220 | C24_BIO_TRIAL_DATA_EVENT_RISK | C24 should not treat immunotherapy trial/headline spikes as durable Stage2 unless data quality, endpoint durability, partner path or commercialization bridge is visible. NeoImmuneTech had large MFE but later collapsed into high MAE and post-peak drawdown. | True | True |
| R7L93_C24_NEOIMMUNETECH_2024_STAGE2_FALSE_POSITIVE_IMMUNO_ONCOLOGY_TRIAL_WATCH | 950220 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_false_positive_if_trial_watch_counts_without_endpoint_quality_partner_regulatory_revision_bridge | True | True |
| C24-R7-L100-TRIG-02-950220 | 950220 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_false_positive | True | True |
| TRG_R7L78-C24-950220-NEOIMMUNETECH-IMMUNO-ONCOLOGY-DATA-FADE | 950220 | C24_BIO_TRIAL_DATA_EVENT_RISK | C24 should not treat immuno-oncology trial-data theme beta as durable Stage2 unless efficacy/safety, endpoint quality, regulatory path, financing runway and commercialization bridge are visible. NeoImmuneTech had a tradable spike but no durable rerating and then a broad drawdown path. | True | True |
| TRG_R7L74-C24-950220-NEOIMMUNETECH-IMMUNOTHERAPY-TRIAL-HEADLINE-FADE | 950220 | C24_BIO_TRIAL_DATA_EVENT_RISK | C24 should not treat immunotherapy trial/headline spikes as durable Stage2 unless data quality, endpoint durability, partner path or commercialization bridge is visible. NeoImmuneTech had large MFE but later collapsed into high MAE and post-peak drawdown. | True | True |
| R7L87_C24_950220_20240322_STAGE2_FALSE_POSITIVE_IMMUNO_ONCOLOGY_DATA | 950220 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_false_positive_if_data_theme_overcredited | True | True |
| R13L87_REVIEW_R7_C24_BIO_TRIAL_DATA_EVENT_RISK_950220_2024-03-22 | 950220 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | True | True |
| R13L93_REVIEW_R7_C24_BIO_TRIAL_DATA_EVENT_RISK_950220_2024_02_26_TRIGGER | 950220 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive_if_trial_watch_counts_without_endpoint_quality_partner_regulatory_revision_bridge | True | True |
| T-KAKAOBANK-S2-20250210 | None | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | False | True |
| T-BNK-S2A-20250113 | None | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_late | False | True |
| T-WOORI-S2A-20250210 | None | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_late | False | True |
