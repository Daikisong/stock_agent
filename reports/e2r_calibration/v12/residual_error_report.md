# V12 Residual Error Report

v12 잔차 장부입니다. 검증 통과 항목은 rolling calibration에 들어가고, 제약은 guardrail로 남깁니다.
source proxy 또는 evidence URL 한계는 positive patch를 막거나 scope 제한을 강화합니다.

- residual_rows: `2383`

| trigger_id | symbol | archetype | verdict | source_proxy_only | evidence_url_pending |
|---|---|---|---|---|---|
| R7L26-T001 | 000100 유한양행 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_too_late | False | False |
| R7L26-T002 | 000100 유한양행 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_too_late | False | False |
| R7L12_C23_YUHAN_STAGE2_APPROVAL_2024-08-20 | 000100 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_too_late | False | False |
| TRG_R7L10_YUHAN_2024-08-21_APPROVAL_COMMERCIALIZATION | 000100 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_too_late | False | False |
| R7L11-C23-000100-T1-stage2-actionable-fda-approval | 000100 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_too_late | False | False |
| T-C23-YUHAN-STAGE2A-20240821 | 000100 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_too_late | False | False |
| T_YUHAN_20240821_STAGE2_APPROVAL | 000100 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_too_late | False | False |
| T48_000100_20240821_STAGE2_APPROVAL | 000100 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_too_late | False | False |
| TR_R7L10_000100_2024-08-20_FDA_APPROVAL | 000100 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_missed_structural | False | False |
| R7L11_T01_YUHAN_20240820_STAGE3_GREEN_FDA_APPROVAL_DIRECT_ECONOMICS | 000100 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_too_late | False | False |
| R7L14-C23-000100-FDA-APPROVAL-20240820 | 000100 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_too_late | False | False |
| YUHAN_STAGE3_GREEN_2024_08_28 | 000100 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_too_late | False | False |
| T48_000100_20240828_STAGE3_GREEN_LATE | 000100 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_too_late | False | False |
| R7L26-T002 | 000100 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_too_late | False | False |
| R7L12_C23_YUHAN_STAGE3_GREEN_2024-09-24 | 000100 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_too_late | False | False |
| T-C23-YUHAN-STAGE3G-20240924 | 000100 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_too_late | False | False |
| T_YUHAN_20240924_GREEN_LABEL_COMPARISON | 000100 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_too_late | False | False |
| R7L11_T01B_YUHAN_20240829_PRICE_ONLY_LOCAL_4B_TOO_EARLY | 000100 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_4B_too_early | False | False |
| R7L14-C23-000100-RYBREVANT-SC-CRL-20241217 | 000100 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_4C_too_late | False | False |
| C24-YUHAN-20231004-S2A | 000100 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_too_early | False | False |
| R7L12-C24-000100-T1-MARIPOSA-STAGE2A-20231023 | 000100 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_too_early | False | False |
| R7L27-T001 | 000100 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_too_late | False | False |
| R7L27-T001 | 000100 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_too_late | False | False |
| TRG_R7L71_C24_000100_LAZERTINIB_MARIPOSA_APPROVAL_BRIDGE | 000100 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_too_late | False | False |
| TRG_R7L11_000100_STAGE2_20240821 | 000100 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_too_late | False | False |
| TRG_R7L71_C24_000100_LAZERTINIB_MARIPOSA_APPROVAL_BRIDGE | 000100 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_too_late | False | False |
| TRG_R7L11_000100_STAGE3GREEN_20240920 | 000100 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_too_late | False | False |
| R13L12_REDTEAM__R7L12_C23_YUHAN_STAGE2_APPROVAL_2024-08-20 | 000100 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_too_late | False | False |
| R13L15_X_TRIG_T-C23-YUHAN-STAGE2A-20240821 | 000100 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_too_late | False | False |
| R13L11_REDTEAM__R7L11_T01_YUHAN_20240820_STAGE3_GREEN_FDA_APPROVAL_DIRECT_ECONOMICS | 000100 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_too_late | False | False |
| R13L14_X_TRIG_R7L14-C23-000100-FDA-APPROVAL-20240820 | 000100 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_too_late | False | False |
| R13L15_X_TRIG_T-C23-YUHAN-STAGE3G-20240924 | 000100 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_too_late | False | False |
| R13L11_REDTEAM__R7L11_T01B_YUHAN_20240829_PRICE_ONLY_LOCAL_4B_TOO_EARLY | 000100 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_early | False | False |
| R13L14_X_TRIG_R7L14-C23-000100-RYBREVANT-SC-CRL-20241217 | 000100 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4C_too_late | False | False |
| TRG_R9L82-C29-000120-CJ-LOGISTICS-PARCEL-VOLUME-MARGIN-FADE | 000120 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should not treat logistics/parcel volume beta as durable Stage2 unless parcel volume, freight-rate/pass-through, contract mix, automation productivity, revenue conversion and margin bridge are visible. CJ Logistics had early MFE and then persistent high-MAE fade, so it is a local-4B boundary until operating-leverage proof is repaired. | True | True |
| T_R9L13_000120_4B_20240202 | 000120 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_4B_too_late | False | False |
| R13L13_X_T_R9L13_000120_4B_20240202 | 000120 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late | False | False |
| T_R9L13_000120_4B_20240202 | 000120 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late | False | False |
| TRG_R12L73-C32-000150-DOOSAN-HOLDCO-DELAYED-CONTROL-PREMIUM | 000150 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should not blindly block the holding company if control-premium option value later becomes visible, but the entry cannot be pure event chase because early MAE was severe. Doosan is a delayed positive with early local 4B risk and later lifecycle drawdown. | False | True |
| TRG_R12L73-C32-000150-DOOSAN-HOLDCO-DELAYED-CONTROL-PREMIUM | 000150 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should not blindly block the holding company if control-premium option value later becomes visible, but the entry cannot be pure event chase because early MAE was severe. Doosan is a delayed positive with early local 4B risk and later lifecycle drawdown. | False | True |
| TRG_R11L82-C32-000150-DOOSAN-HOLDCO-RESTRUCTURING-CONTROL-DISCOUNT-LIFECYCLE | 000150 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should protect governance/restructuring positives only when event mechanics, board/shareholder process, asset/NAV bridge, control-premium logic, timing and downside cap are visible. Doosan produced very large MFE with shallow entry-basis MAE, but the row still needs source repair and event-mechanics validation before runtime promotion. | True | True |
| TR_C32_000240_4C_2023-12-15 | 000240 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_4C_too_late | False | False |
| R13_C32_HANKOOK_2023_T1 | 000240 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive | False | False |
| TR_C32_000240_STAGE2_2023-12-05 | 000240 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive | False | False |
| R12L10C32_HANKOOK_T1_STAGE2_EVENT_2023_12_05 | 000240 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive | False | False |
| R13_C32_HANKOOK_2023_T1_OVERLAY | 000240 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive | False | False |
| TRG_R7L81-C23-000250-SCD-BIOSIMILAR-APPROVAL-PARTNER-COMMERCIALIZATION | 000250 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | C23 should protect regulatory/commercialization positives only when approval, partner/license economics, supply agreement, launch timing, revenue conversion and margin bridge are visible. Samchundang Pharm produced very large MFE with shallow early MAE, but post-peak drawdown requires lifecycle 4B if commercialization evidence fades. | True | True |
| R9L15_T003 | 000270 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_too_late | False | False |
| R9L14_C29_000270_T1_STAGE2_ACTIONABLE_20230126 | 000270 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_too_late | False | False |
| R9L33-T001-KIA-STAGE2-FY22 | 000270 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_too_late | False | False |
| T_R9L10_000270_STAGE2 | 000270 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_correct | False | True |
| R9L15_T004 | 000270 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| T-C29-KIA-20210120-GREEN | 000270 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_too_late | False | False |
| TR_R9L10_000270_GREEN_20230425 | 000270 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_too_late | False | False |
| R9L33-T002-KIA-STAGE3-GREEN-Q1CONFIRM | 000270 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_too_late | False | False |
| R9L10-C29-KIA-GREEN-20240229 | 000270 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_too_late | False | False |
| T_R9L10_000270_4B | 000270 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_correct | False | True |
| R9L13_C29_KIA_2024_STAGE4B_OVERLAY | 000270 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_4B_too_late | False | False |
| R9L15_T005 | 000270 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_4C_too_late | False | False |
| R13L14_X_TRIG_R9L14_C29_000270_T1_STAGE2_ACTIONABLE_20230126 | 000270 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_too_late | False | False |
| R13L15_R9L15_T004 | 000270 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L15_R9L15_T005 | 000270 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4C_too_late | False | False |
| R6L11-C22-000370-T1 | 000370 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive | False | False |
| TRG_R6L80-C22-000370-HANWHA-GENERAL-INSURANCE-RATE-CYCLE | 000370 | C22_INSURANCE_RATE_CYCLE_RESERVE | C22 should allow non-life insurance positives when loss ratio, reserve adequacy, rate cycle, capital buffer and shareholder-return bridge are visible. Hanwha General Insurance had strong early MFE with bounded entry-basis MAE, then a lifecycle drawdown. | True | True |
| TRG_R6L76-C22-000370-HANWHA-GENERAL-INSURANCE-LOSS-RATIO-CAPITAL-RETURN | 000370 | C22_INSURANCE_RATE_CYCLE_RESERVE | C22 should allow non-life insurers when value-up and rate-cycle attention connects to loss-ratio improvement, CSM/IFRS17 reserve quality, K-ICS capital buffer, dividend/buyback or capital-return bridge. Hanwha General Insurance produced high MFE with controlled entry-basis MAE, but later drawdown requires lifecycle local 4B if reserve/capital-return evidence fades. | True | True |
| TRG_R6L74-C22-000370-HANWHA-GI-RESERVE-CAPITAL-RETURN | 000370 | C22_INSURANCE_RATE_CYCLE_RESERVE | C22 should allow Stage2 when non-top P&C insurers show CSM, reserve release, loss-ratio improvement, K-ICS/capital return or shareholder-return bridge. Hanwha General Insurance produced high MFE with controlled entry-basis MAE, but later local 4B-watch is needed if the reserve/capital-return evidence stops refreshing. | True | True |
| None | 000370 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | True | True |
| TRG_R6L74-C22-000370-HANWHA-GI-RESERVE-CAPITAL-RETURN | 000370 | C22_INSURANCE_RATE_CYCLE_RESERVE | C22 should allow Stage2 when non-top P&C insurers show CSM, reserve release, loss-ratio improvement, K-ICS/capital return or shareholder-return bridge. Hanwha General Insurance produced high MFE with controlled entry-basis MAE, but later local 4B-watch is needed if the reserve/capital-return evidence stops refreshing. | True | True |
| R13_CROSS_000370_2024-02-01_Stage2-Actionable-InsuranceValueupCSM | 000370 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | True | True |
| R6L11_C22_000400_T3_4C_EVENT_BREAK_20240628 | 000400 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_4C_too_late | False | False |
| R6L11_C22_000400_T1_EVENT_PREMIUM_20240213 | 000400 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive | False | False |
| TR-000400-20240227-S2A | 000400 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive | False | False |
| TR-000400-20240227-S2A | 000400 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive | False | False |
| R6L10_C22_LOTTEINS_T2_REJECT_20240423 | 000400 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive | False | False |
| TR-000400-20240626-4B | 000400 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive | False | False |
| TR-000400-20240626-4B | 000400 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive | False | False |
| R13L10_X05_000400_Stage2-candidate-rejected | 000400 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| TRG_R1L76-C02-000500-GAON-CABLE-GRID-CAPEX-LIFECYCLE | 000500 | C02_POWER_GRID_DATACENTER_CAPEX | C02 should include cable suppliers only when grid capex, export order, copper pass-through and margin bridge are visible. Gaon Cable produced high MFE with controlled early MAE, but post-peak drawdown and a later 2024 corporate-action candidate require lifecycle and validation controls. | True | True |
| TRG_R1L78-C02-000500-GAON-CABLE-DATACENTER-GRID-CABLE-BACKLOG | 000500 | C02_POWER_GRID_DATACENTER_CAPEX | C02 should include cable names only when grid/datacenter capex maps to customer orderbook, cable shipment, ASP/copper pass-through and margin bridge. Gaon Cable produced high MFE with controlled entry-basis MAE, but the later drawdown requires lifecycle local 4B if orderbook/margin evidence fades. | True | True |
| TR-000540-20240227-S2A | 000540 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive | False | False |
| TR-000540-20240227-S2A | 000540 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive | False | False |
| C06_SKH_202310_Q3_HBM_CUSTOMER_TRACTION_STAGE2A | 000660 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_missed_structural | False | False |
| TRG_R2L12_C06_SKHYNIX_20240613 | 000660 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_too_late | False | False |
| R2L15_C06_000660_4B_PRICE_ONLY_2024-07-11 | 000660 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_4B_too_late | False | False |
| C06_SKH_202407_PRICE_ONLY_LOCAL_4B_OVERLAY | 000660 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_4B_too_early | False | False |
| R13L15_X_TRIG_R2L15_C06_000660_4B_PRICE_ONLY_2024-07-11 | 000660 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late | False | False |
| T000720_STAGE2_20240717_CZ_PREFERRED_BIDDER | 000720 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive | False | False |
| R1L15_C05_HDEC_STAGE2_MEGA_ORDER_MARGIN_GAP_20230626 | 000720 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | current_profile_too_early | False | False |
| R1L11_C05_000720_STAGE2A_20240125 | 000720 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | current_profile_too_early | False | False |
| R10L15_T001 | 000720 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_too_late | False | False |
| TRG_HDEC_2023_OVERSEAS_BACKLOG_BALANCE_SHEET_STAGE2_ACTIONABLE_2023_04_11 | 000720 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_too_late | False | False |
| TR-C30-000720-S2-20230626 | 000720 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_too_early | False | False |
| R10L13-C30-HDEC-STAGE2-20230626 | 000720 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive | False | False |
| R10L15_T001G | 000720 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_too_late | False | False |
| TRG_HDEC_2023_POST_ORDER_PRICE_ONLY_4B_WATCH_2023_06_26 | 000720 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_4B_too_early | False | False |
| HYUNDAI_EC_2022_LEGOLAND_PF_SECTOR_SHOCK_COUNTER | 000720 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive | False | False |
| R13L13_X_R10L13-C30-HDEC-STAGE2-20230626 | 000720 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L15_X_TRIG_R1L15_C05_HDEC_STAGE2_MEGA_ORDER_MARGIN_GAP_20230626 | 000720 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_too_early | False | False |
| R10L13-C30-HDEC-STAGE2-20230626 | 000720 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L14_X_TRIG_HYUNDAI_EC_2022_LEGOLAND_PF_SECTOR_SHOCK_COUNTER | 000720 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| C21-SAM-S2A-20240201 | 000810 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_late | False | False |
| C21-SAM-S3G-20240516 | 000810 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_late | False | False |
| R13L17_C22_000810_SFM_RATE_RESERVE_2023Q1_T1 | 000810 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_too_late | False | False |
| R6L33-C22-000810-S2 | 000810 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_too_late | False | False |
| R6L12_T01_SAMSUNGFIRE_20240202_STAGE2_ACTIONABLE_CSM_KICS_CAPITALRETURN | 000810 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_too_late | False | False |
| R6L12_T01_SAMSUNGFIRE_20240202_STAGE2_ACTIONABLE_CSM_KICS_CAPITALRETURN | 000810 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_too_late | False | False |
| R6L41_C22_000810_T1_STAGE2A | 000810 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_correct | True | True |
| R13L20_C22_000810_S2A_20240222 | 000810 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_too_late | False | False |
| R13L20_C22_000810_S2A_20240222 | 000810 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_too_late | False | False |
| R6L45_C22_000810_T1_STAGE2_ACTIONABLE_2024-02-23 | 000810 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_too_late | False | False |
| R6L45_C22_000810_T1_STAGE2_ACTIONABLE_2024-02-23 | 000810 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_too_late | False | False |
| R6L41_C22_000810_T2_GREEN_COMPARE | 000810 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_too_late | True | True |
| R6L33-C22-000810-G | 000810 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_too_late | False | False |
| R6L11_C22_000810_T2_STAGE3_GREEN_20240516 | 000810 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_too_late | False | False |
| R6L45_C22_000810_T2_STAGE3_GREEN_COMPARISON_2024-05-16 | 000810 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_too_late | False | False |
| R6L45_C22_000810_T2_STAGE3_GREEN_COMPARISON_2024-05-16 | 000810 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_too_late | False | False |
| R6L11-C22-000810-T2 | 000810 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_4B_too_early | False | False |
| R13L20_C22_000810_4B_LOCAL_20240321 | 000810 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_4B_too_early | False | False |
| R13L20_C22_000810_4B_LOCAL_20240321 | 000810 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_4B_too_early | False | False |
| R6L41_C22_000810_T3_4B_LOCAL | 000810 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_4B_too_early | True | True |
| R6L19_T005 | 000810 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_4B_too_early | False | False |
| TR_C16_UNION_S2_20230217 | 000910 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_false_positive | True | True |
| TR_R4L71_C16_000910_FALSE_S2_20230704 | 000910 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_false_positive | False | False |
| R4L15_C16_T003 | 000910 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_4C_too_late | False | False |
| TRG_R4L75-C16-000910-UNION-RARE-EARTH-POLICY-PROXY-FADE | 000910 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | C16 should not treat rare-earth or resource policy proxy beta as durable Stage2 unless direct resource supply, processing capacity, customer contract or margin bridge is visible. Union had only modest MFE and later deep MAE/drawdown. | True | True |
| TRG_R4L78-C16-000910-UNION-RAREEARTH-RESOURCE-THEME-FADE | 000910 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | C16 should not treat rare-earth/resource-security theme beta as durable Stage2 unless direct supply exposure, customer demand, pricing, inventory and margin bridge are visible. Union had a small early MFE and then opened a deep MAE drawdown path. | True | True |
| R13L15_X_TRIG_R4L15_C16_T003 | 000910 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4C_too_late | False | False |
| R13_C32_DBHITEK_2023_T1_OVERLAY | 000990 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive | False | False |
| R13_C32_DBHITEK_2023_T1 | 000990 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive | False | False |
| TR_C32_000990_STAGE2_2023-03-08 | 000990 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_missed_structural | False | False |
| R13L14_X_TRIG_R12L14C32_000990_T_STAGE2_20230331 | 000990 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R10L13_C30_001260_T_STAGE2_20240327 | 001260 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_4B_too_late | False | False |
| R13L14_G02_07_001390_R12L14_C31_KGCHEM_STAGE2_20211101 | 001390 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | False | False |
| R4L16_C15_001430_T1 | 001430 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive | False | False |
| R4L16_C15_001430_T1 | 001430 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive | False | False |
| TRG_C01_001440_20240513_COUNTER | 001440 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_false_positive_risk_if_price_theme_treated_as_bridge | True | False |
| TRG_R1L80-C02-001440-DAEHAN-CABLE-POST-CA-GRID-CAPEX-BACKLOG | 001440 | C02_POWER_GRID_DATACENTER_CAPEX | C02 should allow power-cable positives when grid/datacenter capex maps to cable order backlog, export/customer quality, delivery schedule, revenue recognition and margin bridge. Daehan Cable produced a very large post-CA MFE, but runtime promotion requires post-CA continuity and source repair. | True | True |
| C02_001440_20240513_PRICE_ONLY_CABLE_THEME_COUNTEREXAMPLE | 001440 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_false_positive_risk_if_cable_theme_treated_as_C02_green | True | False |
| C21-HYUN-S2A-20240201 | 001450 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | False | False |
| R6L46-T007 | 001450 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_4C_too_late | False | False |
| R6L11-C22-001450-T1 | 001450 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive | False | False |
| R13L17_C22_001450_HYUNDAI_RESERVE_GAP_2023Q1_T1 | 001450 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive | False | False |
| R6L33-C22-001450-S2 | 001450 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive_if_promoted | False | False |
| R6L12_T03_HYUNDAIMARINE_20240202_FALSE_STAGE2_RATE_BETA_RESERVE_GUARD | 001450 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive | False | False |
| R6L12_T03_HYUNDAIMARINE_20240202_FALSE_STAGE2_RATE_BETA_RESERVE_GUARD | 001450 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive | False | False |
| R6L13_C22_HYUNDAIMARINE_20240222_POLICY_BETA_RESERVE_GAP_T1 | 001450 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_too_early | False | False |
| R13L20_C22_001450_S2A_20240222 | 001450 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive | False | False |
| R13L20_C22_001450_S2A_20240222 | 001450 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive | False | False |
| R6L19_T003 | 001450 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive | False | False |
| R6L11_C22_HMF_STAGE2A_20240226 | 001450 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive_risk | False | False |
| T_R13L21_001450_STAGE2_20250214 | 001450 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive | False | False |
| R6L10_C22_HYUNDAI_T2_20240514 | 001450 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive | False | False |
| R6L11_C22_001450_T1_STAGE2_OR_YELLOW_STRESS_20240216 | 001450 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive | False | False |
| R6L33-C22-001450-G | 001450 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive | False | False |
| R6L46-T005 | 001450 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive | False | False |
| R13L12_REDTEAM__R6L12_T03_HYUNDAIMARINE_20240202_FALSE_STAGE2_RATE_BETA_RESERVE_GUARD | 001450 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| TRG_R10L82-C30-001470-SAMBU-SMALL-BUILDER-HIGHMAE-SHARECOUNT-STATUS | 001470 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should escalate small-builder/PF risk to local 4B when the price path shows severe MAE and persistent drawdown, but hard 4C still requires non-price refinancing failure, default, impairment, covenant, auditor/control or solvency evidence. Sambu also requires share-count and status continuity validation. | True | True |
| TRG_R10L76-C30-001470-SAMBU-CONSTRUCTION-FINANCING-RISK-LOCAL4B | 001470 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should flag local 4B when a builder/financing-risk row produces a high-MFE but then opens severe MAE and post-peak drawdown. Sambu Construction had a tradable spike but later collapsed; however hard 4C still requires non-price default, refinancing, auditor/control, impairment, covenant or solvency evidence. | True | True |
| None | 001470 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | True | True |
| R10L12-C30-SAMBU-20240327-4C | 001470 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_4C_too_late | False | False |
| R13_CROSS_001470_2024-01-05_Stage4C-HardBalanceSheetBreak | 001470 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | True | True |
| T001470-S2-20230522 | 001470 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| TRG_R6L81-C21-001510-SK-SECURITIES-SMALL-BROKERAGE-THEME-FADE | 001510 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | C21 should not treat small brokerage value-up theme beta as durable Stage2 unless ROE improvement, payout policy, trading-volume sensitivity, capital buffer and earnings bridge are visible. SK Securities had a small early MFE and then a persistent MAE path. | True | True |
| TR_C16_GEUMYANG_S2_20230221 | 001570 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_4B_too_late | True | True |
| R4L14_C16_T02_KUMYANG_20230726_FALSE_GREEN | 001570 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_false_positive | False | False |
| TRG_R4L81-C16-001570-KUMYANG-LITHIUM-RESOURCE-POLICY-THEME-FADE | 001570 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | C16 should not treat lithium/resource policy beta as durable Stage2 unless mine/supply availability, customer offtake, financing, permitting, revenue conversion and margin bridge are visible. Kumyang had a strong early spike, then a severe high-MAE fade. | True | True |
| R13L14_G02_04_001570_R4L14_C16_T02_KUMYANG_20230726_FALSE_GREEN | 001570 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | False | False |
| TRG_R12L72-C32-001750-HANYANG-SECURITIES-SALE-PROCESS-CAP | 001750 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should support a sale-process Stage2 only when control-stake sale, buyer certainty and closing path are verified. The stock-web path had strong MFE but later reverted toward pre-event levels, so tender/sale-process cap logic is required. | True | True |
| TRG_R12L72-C32-001750-HANYANG-SECURITIES-SALE-PROCESS-CAP | 001750 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should support a sale-process Stage2 only when control-stake sale, buyer certainty and closing path are verified. The stock-web path had strong MFE but later reverted toward pre-event levels, so tender/sale-process cap logic is required. | True | True |
| TRG_R12L75-C32-001750-HANYANG-SECURITIES-CONTROL-SALE-PREMIUM-FADE | 001750 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should not treat a control-sale or preferred-bidder headline as durable Stage2 unless minority economics, tender floor, closing certainty or listed-shareholder beneficiary bridge is explicit. Hanyang Securities had a tradable MFE but then faded into local 4B risk. | True | True |
| TRG_R4L74-C15-001780-ALUKO-ALUMINUM-PRICE-BETA-LOCAL4B | 001780 | C15_MATERIAL_SPREAD_SUPERCYCLE | C15 should not treat aluminum or battery-material profile beta as Green unless product mix, customer order, spread and margin bridge are explicit. Aluko produced only small MFE and then severe late-2024 MAE, making it local 4B-watch rather than durable Stage2. | True | True |
| TRG_R4L74-C15-001780-ALUKO-ALUMINUM-PRICE-BETA-LOCAL4B | 001780 | C15_MATERIAL_SPREAD_SUPERCYCLE | C15 should not treat aluminum or battery-material profile beta as Green unless product mix, customer order, spread and margin bridge are explicit. Aluko produced only small MFE and then severe late-2024 MAE, making it local 4B-watch rather than durable Stage2. | True | True |
| R10L13_C30_002410_T_STAGE2_20240327 | 002410 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_4B_too_late | False | False |
| TRG_R10L74-C30-002410-BUMYANG-PF-LIQUIDITY-LOCAL4B-SEVERE | 002410 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should catch severe small-builder PF/liquidity/local 4B risk when MAE and drawdown become large, but hard 4C still needs non-price proof. Bumyang Construction shows the price-path severity that should raise local 4B-watch, not a price-only hard 4C. | True | True |
| TRG_R10L77-C30-002410-BEOMYANG-BUILDER-FINANCING-HIGH-MAE-LOCAL4B | 002410 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should flag local 4B when a small-builder/PF-financing row opens severe MAE and persistent drawdown, but hard 4C still requires non-price default, refinancing failure, court rehabilitation, impairment, covenant or solvency evidence. Beomyang Construction produced minimal MFE and then a deep drawdown path. | True | True |
| TRG_R10L80-C30-002410-BEOMYANG-E&C-PF-HIGHMAE-LOCAL4B | 002410 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should flag local 4B when small-builder/PF fear aligns with persistent high MAE and weak recovery, but hard 4C still requires non-price refinancing failure, default, covenant, impairment, auditor/control or solvency evidence. | True | True |
| TRG_R10L74-C30-002410-BUMYANG-PF-LIQUIDITY-LOCAL4B-SEVERE | 002410 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should catch severe small-builder PF/liquidity/local 4B risk when MAE and drawdown become large, but hard 4C still needs non-price proof. Bumyang Construction shows the price-path severity that should raise local 4B-watch, not a price-only hard 4C. | True | True |
| R10L12-C30-HS-20240327-T1 | 002460 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive | False | False |
| TRG_R3L77-C11-002710-TCCSTEEL-BATTERY-CAN-MATERIAL-ORDERBOOK-LIFECYCLE | 002710 | C11_BATTERY_ORDERBOOK_RERATING | C11 can include battery-can/component material names when customer orderbook, capacity ramp, quality approval and margin bridge are visible. TCC Steel produced very large early MFE, but the later high-MAE collapse says C11 must lifecycle-manage the signal and activate local 4B when orderbook/margin evidence fades. | True | True |
| R10L13_C30_002780_T_STAGE2_20240327 | 002780 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive | False | False |
| TRG_R10L81-C30-002780-JINHEUNG-SMALL-BUILDER-HIGHMAE-LOCAL4B | 002780 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should escalate small-builder/PF risk to local 4B when the path has little durable MFE and large 180D MAE, but hard 4C still needs non-price refinancing failure, default, impairment, covenant, auditor/control or solvency evidence. | True | True |
| TR-C30-002990-S2RISK | 002990 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_too_late | False | False |
| R10L11-C30-KUMHO-STAGE2-20240125 | 002990 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive | False | False |
| R10L15_T03_KUMHO_STAGE2_POLICY_BETA_FALSE_POSITIVE | 002990 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive | False | False |
| TRG_R10L74-C30-002990-KUMHO-PF-LIQUIDITY-ORDERBOOK-LOCAL4B | 002990 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 local 4B-watch should fire when mid-builder PF/orderbook/liquidity risk produces weak MFE and persistent MAE, but hard 4C still requires explicit non-price default, refinancing failure, court rehabilitation, auditor/control or solvency break. | True | True |
| TRG_R10L78-C30-002990-KUMHO-E&C-SMALLBUILDER-HIGH-MAE-LOCAL4B | 002990 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should flag local 4B when construction/PF fear aligns with persistent MAE and drawdown, but hard 4C still requires non-price refinancing failure, default, covenant, impairment, auditor/control or solvency evidence. Kumho E&C produced almost no MFE and then a deep drawdown path. | True | True |
| TRG_R10L74-C30-002990-KUMHO-PF-LIQUIDITY-ORDERBOOK-LOCAL4B | 002990 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 local 4B-watch should fire when mid-builder PF/orderbook/liquidity risk produces weak MFE and persistent MAE, but hard 4C still requires explicit non-price default, refinancing failure, court rehabilitation, auditor/control or solvency break. | True | True |
| R13L15_X_TRIG_R10L15_T03_KUMHO_STAGE2_POLICY_BETA_FALSE_POSITIVE | 002990 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| TRG_R10L77-C30-003070-KOLON-GLOBAL-PF-RISKWATCH-RECOVERY-NO-HARD4C | 003070 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should not over-convert builder/PF fear into hard 4C when price produces a recovery spike and MAE remains bounded. Kolon Global still needs PF/orderbook/liquidity monitoring, but the price path is a RiskWatch/no-hard-4C boundary unless non-price refinancing or solvency evidence breaks. | True | True |
| TRG_R10L79-C30-003070-KOLON-GLOBAL-PF-RECOVERY-SPIKE-NO-HARD4C | 003070 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should not over-convert builder/PF fear into hard 4C when the path produces a strong recovery spike. Kolon Global needs PF/orderbook/liquidity monitoring, but price action alone is not confirmed balance-sheet break evidence. | True | True |
| R10L11-C30-KOLON-STAGE2-20240125 | 003070 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_4B_too_late | False | False |
| R10L15_T04_KOLON_4B_PRICE_ONLY_PROPERTY_THEME_BLOWOFF | 003070 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive | False | False |
| R10L11-C30-KOLON-4B-20240620 | 003070 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_4B_too_late | False | False |
| R13L15_X_TRIG_R10L15_T04_KOLON_4B_PRICE_ONLY_PROPERTY_THEME_BLOWOFF | 003070 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L11_HIGHMAE_X08_003070_STAGE2A_20240125 | 003070 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_4B_too_late | False | False |
| TRG_R2L80-C07-003160-DI-HBM-TEST-EQUIPMENT-RS-ORDER-BRIDGE | 003160 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | C07 should protect HBM/test-equipment positives when relative strength maps to equipment order, customer capacity, delivery schedule, revenue recognition and margin bridge. DI produced a very large MFE with controlled entry-basis MAE, but the post-peak drawdown means source-repaired lifecycle 4B is still needed. | True | True |
| R2L12_T04_DI_STAGE3_FALSE_GREEN_TESTER_THEME | 003160 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_false_positive | False | False |
| R2L14_C09_003160_DI_TESTER_THEME_FALSE_GREEN | 003160 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_false_positive | False | False |
| R13L14_X_TRIG_R2L14_C09_003160_DI_TESTER_THEME_FALSE_GREEN | 003160 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L12_REDTEAM__R2L12_T04_DI_STAGE3_FALSE_GREEN_TESTER_THEME | 003160 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L41_C18_SAMYANG_4B_2024_06_18 | 003230 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_4B_too_early | False | False |
| TRG_SAMYANG_2023_Q3_EXPORT_REORDER_STAGE2_ACTIONABLE_2023_11_15 | 003230 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_missed_structural | False | False |
| R5L16-C18-003230-T1 | 003230 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_missed_structural | False | False |
| R13L41_C18_SAMYANG_STAGE2_2023_11_16 | 003230 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_too_late | False | False |
| R13L11_T001_003230_STAGE2 | 003230 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_missed_structural | False | False |
| R13L41_C18_SAMYANG_GREEN_2024_05_17 | 003230 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_too_late | False | False |
| TRG_SAMYANG_2024_CONFIRMED_REVISION_LATE_GREEN_2024_05_17 | 003230 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_too_late | False | False |
| R13L11_T002_003230_GREEN_LATE | 003230 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_too_late | False | False |
| R5L13_003230_T2_STAGE3_GREEN_2024-06-17 | 003230 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_too_late | False | False |
| R5L16-C18-003230-T4B | 003230 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_4B_too_late | False | False |
| R13L11_T003_003230_4B | 003230 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_4B_too_late | False | False |
| R5L39_C18_003230_4BLOCAL_20240619 | 003230 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_4B_too_early | False | False |
| R5L15-C18-003230-T2 | 003230 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_4B_too_early | False | False |
| R5L15-C18-003230-T2 | 003230 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_4B_too_early | False | False |
| SYF_STAGE2_EXPORT_REVISION_2024_03_04 | 003230 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_too_late | False | False |
| R13L55_003230_GREEN_20240517 | 003230 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_too_late | False | False |
| R13L55_003230_GREEN_20240517 | 003230 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_too_late | False | False |
| SYF_STAGE3_GREEN_Q1_EXPORT_CONFIRM_2024_05_20 | 003230 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_too_late | False | False |
| R13L55_003230_4B_20240618 | 003230 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_4B_too_early | False | False |
| R5L10_T02_SAMYANG_4B_LOCAL | 003230 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_4B_too_early | False | False |
| R13L55_003230_4B_20240618 | 003230 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_4B_too_early | False | False |
| R13L10_T06_SAMYANG_PRICE_ONLY_4B_TOO_EARLY | 003230 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_early | False | False |
| R13L14_G05_12_003310_R12L14_C31_DAEJOO_4B_20220520 | 003310 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_4B_too_late | False | False |
| R5L10_T07_HANKOOK_COSMETICS_LOCAL_4B_TOO_EARLY_20240614 | 003350 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_4B_too_early | False | False |
| TRG_R12L76-C32-003410-SSANGYONGCNE-VOLUNTARY-DELISTING-TENDER-FLOOR | 003410 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should allow tender-floor lifecycle candidates when minority shareholders have explicit tender mechanics, floor price, closing path and direct economic beneficiary mapping. Ssangyong C&E produced a low-MAE tender-floor move and then price pinning, but this is not an operating Green; it is a governance-event floor trade that ends when tender mechanics complete. | True | True |
| TR_R9L31_C29_003490_REOPENING_FALSE_20211108 | 003490 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| R9L13_C29_KAL_2023_REOPENING_VOLUME_COUNTER | 003490 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| T_R9L13_003490_STAGE2_20240130 | 003490 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| R13L13_X_T_R9L13_003490_STAGE2_20240130 | 003490 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| T_R9L13_003490_STAGE2_20240130 | 003490 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| TRG_R11L82-C32-003550-LG-HOLDCO-VALUEUP-BOUNDED-NO-FORCED4B | 003550 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should not force bounded holding-company value-up rows into 4B when no non-price event break is confirmed, but it also should not call durable Stage2 without explicit event mechanics, NAV bridge, shareholder process and downside cap. LG is a bounded RiskWatch/no-forced-4B row. | True | True |
| TRG_R11L77-C03-003570-SNT-DYNAMICS-DEFENSE-DRIVETRAIN-EXPORT-BACKLOG | 003570 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | C03 should allow defense component suppliers when export framework demand maps to drivetrain/transmission backlog, delivery schedule and margin bridge. SNT Dynamics produced large MFE with almost no entry-basis MAE, but lifecycle local 4B is still required if export/backlog/margin evidence fades. | True | True |
| TRG_R1L74-C03-003570-SNT-DYNAMICS-POWERTRAIN-EXPORT-BACKLOG | 003570 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | C03 should include defense powertrain and transmission suppliers when export programs convert into backlog and margin. SNT Dynamics produced a strong 180D MFE with very controlled entry MAE, but later drawdown after the October peak requires lifecycle local 4B if backlog/margin evidence fades. | True | True |
| TRG_R1L74-C03-003570-SNT-DYNAMICS-POWERTRAIN-EXPORT-BACKLOG | 003570 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | C03 should include defense powertrain and transmission suppliers when export programs convert into backlog and margin. SNT Dynamics produced a strong 180D MFE with very controlled entry MAE, but later drawdown after the October peak requires lifecycle local 4B if backlog/margin evidence fades. | True | True |
| TR_R3L66_003670_20230131_S2A | 003670 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_missed_structural | False | False |
| T_C11_POSCOFUTUREM_STAGE2A_2023_01_30 | 003670 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_too_late | False | False |
| R3L12_T_POSCO_4B_20230726 | 003670 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_4B_too_late | False | False |
| None | 003670 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | True | True |
| R13_CROSS_003670_2024-04-25_Stage4B-Local-CathodeCustomerCallOffRisk | 003670 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | True | True |
| TR_R3L15_C14_PFM_20230726_4B_OVERLAY | 003670 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_4B_too_late | False | False |
| R3L11_T02B_POSCOFUTUREM_20230726_PRICE_ONLY_BLOWOFF_OVERLAY | 003670 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_4B_too_early | False | False |
| T_R3L16_POSCOFM_20230726_4B_PRICE_OVERLAY | 003670 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_4B_too_late | False | False |
| R13L55_C14_003670_4C_LATE_20230726 | 003670 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_4C_too_late | False | False |
| TR_C14_POSCOFM_20240725_STAGE4C | 003670 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_4C_too_late | False | False |
| T_R11L14_C31_003670_LOCAL_4B_2023-04-19 | 003670 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_4B_too_early_if_price_only_overlay_promoted | False | False |
| R13L14_X_TRIG_T_R11L14_C31_003670_LOCAL_4B_2023-04-19 | 003670 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_too_early | False | False |
| TRG_R6L74-C22-003690-KOREANRE-REINSURANCE-CYCLE-CAPITAL-BUFFER | 003690 | C22_INSURANCE_RATE_CYCLE_RESERVE | C22 should include reinsurers when pricing cycle, reserve adequacy and capital buffer translate into low-MAE rerating. Korean Re produced slow but durable MFE; however a late-2024 share-count change in the shard requires validation before runtime promotion. | True | True |
| None | 003690 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | True | True |
| TRG_R6L74-C22-003690-KOREANRE-REINSURANCE-CYCLE-CAPITAL-BUFFER | 003690 | C22_INSURANCE_RATE_CYCLE_RESERVE | C22 should include reinsurers when pricing cycle, reserve adequacy and capital buffer translate into low-MAE rerating. Korean Re produced slow but durable MFE; however a late-2024 share-count change in the shard requires validation before runtime promotion. | True | True |
| R13_CROSS_003690_2024-02-01_Stage2-Actionable-ReinsuranceRateCycle | 003690 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | True | True |
| TRG_R6L76-C22-003690-KOREANRE-REINSURANCE-RESERVE-CAPITAL-RETURN | 003690 | C22_INSURANCE_RATE_CYCLE_RESERVE | C22 should preserve reinsurance reserve/capital-return rows when underwriting cycle, reinsurance rate hardening, reserve adequacy, K-ICS buffer and shareholder-return bridge are visible. Korean Re produced slow low-MAE rerating, not explosive beta; the model should not overblock these compounding C22 rows. | True | True |
| TRG_R6L82-C22-003690-KOREAN-RE-REINSURANCE-RATE-CYCLE-CAPITAL-RETURN | 003690 | C22_INSURANCE_RATE_CYCLE_RESERVE | C22 should allow reinsurance positives when rate-cycle pricing, reserve adequacy, loss ratio, capital buffer, shareholder return and ROE/PBR bridge are visible. Korean Re had controlled entry-basis MAE and steady later MFE, so it is a protected positive after source repair. | True | True |
| R12L15_TR_NAMYANG_STAGE2_20210528 | 003920 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive | False | False |
| TRG-C32-NAMYANG-20240104-STAGE2A | 003920 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive | False | False |
| TRG_R12L74-C32-003920-NAMYANG-CONTROL-TRANSFER-PREMIUM-CAP | 003920 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should not treat legal/control-transfer resolution as durable Green unless minority economics, tender floor, capital policy, operational turnaround or closing economics bridge is visible. Namyang had small MFE and persistent MAE before the later share-split/corporate-action area, so it is a control-transfer premium-cap counterexample. | True | True |
| TRG_R12L74-C32-003920-NAMYANG-CONTROL-TRANSFER-PREMIUM-CAP | 003920 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should not treat legal/control-transfer resolution as durable Green unless minority economics, tender floor, capital policy, operational turnaround or closing economics bridge is visible. Namyang had small MFE and persistent MAE before the later share-split/corporate-action area, so it is a control-transfer premium-cap counterexample. | True | True |
| None | 003920 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | None | True | True |
| R13_CROSS_R12L71-C32-003920-NAMYANG-HAHNCONTROL-EXECUTION-LITIGATION-CAP_003920_2021-05-28_Stage4B-GovernanceExecutionRisk | 003920 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | None | True | True |
| R13L15_X_TRIG_R12L15_TR_NAMYANG_STAGE2_20210528 | 003920 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| TRG_R4L82-C17-004000-LOTTE-FINE-CHEM-CHLOR-ALKALI-BOUNDED-RISKWATCH | 004000 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | C17 should not force bounded chemical spread rows into 4B when no non-price margin break is confirmed, but it also should not call durable Stage2 without spread recovery, volume, pricing and margin bridge. Lotte Fine Chemical is a bounded RiskWatch row. | True | True |
| TR-R4L71-C15-004020-STAGE2A-20250221 | 004020 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_too_late | False | False |
| TRG_R4L80-C15-004020-HYUNDAI-STEEL-SPREAD-MARGIN-FADE | 004020 | C15_MATERIAL_SPREAD_SUPERCYCLE | C15 should not treat steel spread beta as durable Stage2 unless HRC/rebar/auto steel volume, utilization, raw-material spread, price pass-through and margin bridge are visible. Hyundai Steel produced modest MFE and then a high-MAE downtrend. | True | True |
| TRG_R4L78-C16-004090-KOREA-PETROLEUM-OIL-SUPPLY-SECURITY-LIFECYCLE | 004090 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | C16 can allow oil/resource-security rows when geopolitical supply shock maps to product pricing, inventory, demand and margin bridge. Korea Petroleum produced a very large MFE with controlled entry-basis MAE, but later post-peak drawdown requires lifecycle local 4B if supply/inventory/margin evidence fades. | True | True |
| TR_R11L11_KOREAOIL_STAGE2_2024_06_03 | 004090 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| R11L11_T_004090_20240603_Stage2_Event_Watch | 004090 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| TRG_R11L74-C31-004090-KOREA-PETROLEUM-POLICY-THEME-BETA-FADE | 004090 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should not treat oil/gas policy attention as a durable Stage2 signal for an oil-product proxy without direct concession, supply, infrastructure, procurement or earnings bridge. Korea Petroleum produced strong event MFE but later opened high MAE and a large post-peak drawdown. | True | True |
| TRG_R11L74-C31-004090-KOREA-PETROLEUM-POLICY-THEME-BETA-FADE | 004090 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should not treat oil/gas policy attention as a durable Stage2 signal for an oil-product proxy without direct concession, supply, infrastructure, procurement or earnings bridge. Korea Petroleum produced strong event MFE but later opened high MAE and a large post-peak drawdown. | True | True |
| TRG_R5L74-C19-004170-SHINSEGAE-DS-MARGIN-RISKWATCH | 004170 | C19_BRAND_RETAIL_INVENTORY_MARGIN | C19 should distinguish stable department-store value-up from durable inventory/margin rerating. Shinsegae had early MFE but later MAE opened and the return path was not strong enough to qualify as durable Green without stronger traffic/duty-free/margin evidence. | True | True |
| TRG_R5L74-C19-004170-SHINSEGAE-DS-MARGIN-RISKWATCH | 004170 | C19_BRAND_RETAIL_INVENTORY_MARGIN | C19 should distinguish stable department-store value-up from durable inventory/margin rerating. Shinsegae had early MFE but later MAE opened and the return path was not strong enough to qualify as durable Green without stronger traffic/duty-free/margin evidence. | True | True |
| R5L13_004370_T2_4C_LATE_2024-11-15 | 004370 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_4C_too_late | False | False |
| R5L16-C18-004370-T1 | 004370 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_too_late | False | False |
| R5L12_C18_NONGSHIM_T2A_20230516 | 004370 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_too_late | False | False |
| R13L41_C18_NONGSHIM_STAGE2_2023_08_11 | 004370 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | False | False |
| R5L11-C18-003-S2A-2024-05-17 | 004370 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive_if_promoted_green | False | False |
| R5L13_004370_T1_STAGE2_WATCH_2024-05-28 | 004370 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | False | False |
| R5L12_C18_NONGSHIM_GREEN_20231113 | 004370 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_too_late | False | False |
| TRG_NONGSHIM_2023_LATE_GREEN_DOMESTIC_PRICE_COST_TAILWIND_2023_05_16 | 004370 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | False | False |
| R13L41_C18_NONGSHIM_4C_WATCH_2024_02_29 | 004370 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_data_insufficient | False | False |
| NONGSHIM_STAGE2_OVERSEAS_RAMEN_2024_05_13 | 004370 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | False | False |
| NONGSHIM_GREEN_TOO_LATE_2024_06_13 | 004370 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | False | False |
| R12L13_C31_004370_DOWNSTREAM_COST_PRESSURE_T_STAGE2_20220224 | 004370 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| R13L13_X_R12L13_C31_004370_DOWNSTREAM_COST_PRESSURE_T_STAGE2_20220224 | 004370 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R12L13_C31_004370_DOWNSTREAM_COST_PRESSURE_T_STAGE2_20220224 | 004370 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| TRG_R4L82-C17-004430-SONGWON-INDUSTRIAL-ADDITIVE-MARGIN-FADE | 004430 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | C17 should not treat chemical additive or commodity spread theme beta as durable Stage2 unless customer volume, pricing power, input-cost pass-through, revenue and margin bridge are visible. Songwon Industrial had tiny early MFE and then high MAE before a late theme bounce. | True | True |
| TRG_R4L76-C17-004430-SONGWON-INDUSTRIAL-ADDITIVE-SPREAD-FADE | 004430 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | C17 should not treat specialty additive or commodity-spread beta as durable Stage2 unless order, inventory restocking, price-cost spread and margin evidence refreshes. Songwon Industrial had weak MFE and then opened a high-MAE drawdown path. | True | True |
| TRG_R10L82-C30-004960-HANSHIN-BUILDER-BOUNDED-PF-RISKWATCH | 004960 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should not force bounded builder/PF watch rows into 4B when no refinancing, liquidity or solvency break is confirmed, but it also should not call durable Stage2 without orderbook, PF and margin recovery bridge. Hanshin Construction is a bounded RiskWatch row. | True | True |
| TRG_R10L78-C30-004960-HANSHIN-E&C-PF-RISKWATCH-BOUNDED-NO-HARD4C | 004960 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should keep PF/orderbook watch active for mid-builders, but bounded MAE and a non-collapsing price path should not become hard 4C without explicit refinancing, impairment, covenant, auditor/control or solvency break evidence. | True | True |
| R10L12-C30-HANSHIN-20240327-T1 | 004960 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_too_late | False | False |
| R10L15_T02_HANSHIN_STAGE2_PUBLIC_WORKS_BALANCE_SURVIVOR | 004960 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_too_early | False | False |
| TRG_R10L75-C30-004960-HANSHIN-BUILDER-RISKWATCH-NO-HARD4C | 004960 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should keep PF/orderbook RiskWatch active for builders, but bounded MAE and recovery rows should not be escalated into hard 4C. Hanshin Construction shows PF fear but also rebound behavior; full 4B or hard 4C requires non-price break evidence. | True | True |
| TRG_R10L73-C30-004960-HANSHIN-PF-ORDERBOOK-LOCAL4B | 004960 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 local 4B-watch should fire when PF/orderbook/margin risk prevents a durable MFE path, even if the stock does not show a hard 4C collapse. 한신공영 is a local-risk boundary row: MAE opens and MFE is small, but full 4B/4C still needs explicit non-price deterioration. | True | True |
| TRG_R10L73-C30-004960-HANSHIN-PF-ORDERBOOK-LOCAL4B | 004960 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 local 4B-watch should fire when PF/orderbook/margin risk prevents a durable MFE path, even if the stock does not show a hard 4C collapse. 한신공영 is a local-risk boundary row: MAE opens and MFE is small, but full 4B/4C still needs explicit non-price deterioration. | True | True |
| R13L15_X_TRIG_R10L15_T02_HANSHIN_STAGE2_PUBLIC_WORKS_BALANCE_SURVIVOR | 004960 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_too_early | False | False |
| R13L41_C18_BINGGRAE_4B_2024_06_10 | 005180 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_4B_too_late | False | False |
| TRG_BINGGRAE_2024_CHANNEL_REORDER_STAGE2_ACTIONABLE_2024_04_01 | 005180 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_too_late | False | False |
| R13L11_T004_005180_STAGE2 | 005180 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_too_late | False | False |
| R5L13_005180_T1_STAGE2_ACTIONABLE_2024-05-16 | 005180 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_too_early | False | False |
| R5L11-C18-002-S2A-2024-05-17 | 005180 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_too_early_if_green | False | False |
| R5L13_005180_T2_STAGE3_GREEN_LOCAL_2024-06-10 | 005180 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | False | False |
| TRG_BINGGRAE_2024_PRICE_SPIKE_4B_WATCH_2024_05_17 | 005180 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_4B_too_early | False | False |
| R13L11_T005_005180_4B | 005180 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_4B_too_late | False | False |
| R13L27_C16_005290_4B1 | 005290 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_4B_too_early | False | False |
| R9L15_T001 | 005380 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_too_late | False | False |
| R9L14_C29_005380_T1_STAGE2_ACTIONABLE_20230126 | 005380 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_too_late | False | False |
| T_R9L10_005380_STAGE2 | 005380 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_correct | False | True |
| TR_R9L10_005380_GREEN_20230425 | 005380 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_too_late | False | False |
| R9L13_C29_HMC_2024_STAGE4B_OVERLAY | 005380 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_4B_too_late | False | False |
| R9L10-C29-HYUNDAI-4B-20240628 | 005380 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_4B_too_early_if_price_only | False | False |
| TR_R11L13_HYUNDAI_VALUEUP_STAGE2A_20240226 | 005380 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_too_late | False | False |
| R11L11_T_005380_20240226_Stage2_Actionable | 005380 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_too_late | False | False |
| TR_R11L12_HYUNDAI_VALUEUP_STAGE2_20240226 | 005380 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_missed_structural | False | False |
| T_R11L14_C31_005380_IRA_SIGNED_HEADWIND | 005380 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| R13L14_X_TRIG_R9L14_C29_005380_T1_STAGE2_ACTIONABLE_20230126 | 005380 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_too_late | False | False |
| R13L14_X_TRIG_T_R11L14_C31_005380_IRA_SIGNED_HEADWIND | 005380 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| TRG_R4L81-C16-005420-COSMO-CHEMICAL-COBALT-LITHIUM-RECOVERY-LIFECYCLE | 005420 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | C16 should allow strategic-resource recovery positives only when cobalt/lithium/nickel or recycling supply maps to customer volume, utilization, policy support, revenue and margin bridge. Cosmo Chemical produced a large early MFE, but the later high-MAE path requires lifecycle 4B if the bridge fades. | True | True |
| TR-R4L71-C15-005490-STAGE2A-20250221 | 005490 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive | False | False |
| TR-R4L71-C15-005490-STAGE2A-20250221 | 005490 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive | False | False |
| TRG_R4L80-C15-005490-POSCO-HOLDINGS-STEEL-LITHIUM-SPREAD-FADE | 005490 | C15_MATERIAL_SPREAD_SUPERCYCLE | C15 should not treat steel/lithium/resource beta as durable Stage2 unless steel spread, lithium resource economics, inventory, volume, pricing and margin bridge refreshes. POSCO Holdings had a tradable bounce but then opened a high-MAE drawdown path. | True | True |
| TR_C16_POSCO_S2A_20230410 | 005490 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_correct | True | True |
| TR_R11L12_POSCO_VALUEUP_FALSEPOS_20240226 | 005490 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| C21-DB-S2A-20240201 | 005830 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_late | False | False |
| C21-DB-S3G-20240516 | 005830 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_late | False | False |
| R6L19_T001 | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_too_late | False | False |
| R6L11-C22-005830-T1 | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_too_late | False | False |
| R13L17_C22_005830_DBI_RATE_RESERVE_2023Q1_T1 | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_too_late | False | False |
| R6L33-C22-005830-S2 | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_too_late | False | False |
| R6L12_T02_DBINSURANCE_20240202_STAGE2_ACTIONABLE_CSM_CAPITALRETURN | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_too_late | False | False |
| R6L12_T02_DBINSURANCE_20240202_STAGE2_ACTIONABLE_CSM_CAPITALRETURN | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_too_late | False | False |
| R6L41_C22_005830_T1_STAGE2A | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_correct | True | True |
| R13L20_C22_005830_S2A_20240222 | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_too_late | False | False |
| R13L20_C22_005830_S2A_20240222 | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_too_late | False | False |
| R6L45_C22_005830_T1_STAGE2_ACTIONABLE_2024-02-23 | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_too_late | False | False |
| R6L45_C22_005830_T1_STAGE2_ACTIONABLE_2024-02-23 | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_too_late | False | False |
| T_R13L21_005830_STAGE2_20250515 | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_too_late | False | False |
| R6L11-C22-005830-T2 | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_too_late | False | False |
| R6L46-T004 | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_too_late | False | False |
| R6L41_C22_005830_T2_GREEN_COMPARE | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_too_late | True | True |
| R6L33-C22-005830-G | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_too_late | False | False |
| R6L45_C22_005830_T2_STAGE3_GREEN_COMPARISON_2024-05-16 | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_too_late | False | False |
| R6L45_C22_005830_T2_STAGE3_GREEN_COMPARISON_2024-05-16 | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_too_late | False | False |
| R13L20_C22_005830_4B_LOCAL_20240314 | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_4B_too_early | False | False |
| R13L20_C22_005830_4B_LOCAL_20240314 | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_4B_too_early | False | False |
| R6L41_C22_005830_T3_4B_FULL | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_correct | True | True |
| TRG_R9L74-C29-005850-SL-AUTO-LIGHTING-ADAS-MARGIN | 005850 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should include lighting/ADAS suppliers when OEM mix, order cadence and margin conversion drive rerating. SL had strong MFE, but post-peak drawdown says lifecycle local 4B should fire if OEM mix or margin evidence fades. | True | True |
| TRG_R9L76-C29-005850-SL-LAMP-MODULE-OEM-MIX-MARGIN-BRIDGE | 005850 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should allow mobility supplier Stage2 when OEM program volume, lamp/module mix, pricing and margin bridge are visible. SL produced a large mid-year MFE with bounded entry-basis MAE, but the later drawdown requires lifecycle local 4B if volume/mix/margin evidence fades. | True | True |
| TRG_R9L79-C29-005850-SL-AUTO-LAMP-MIX-MARGIN-BRIDGE | 005850 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should allow auto lamp/electronics suppliers when customer program volume, product mix, pricing, utilization and margin bridge are visible. SL produced a large MFE with bounded MAE, but the post-peak drawdown requires lifecycle local 4B if volume/mix/margin evidence fades. | True | True |
| TRG_R9L74-C29-005850-SL-AUTO-LIGHTING-ADAS-MARGIN | 005850 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should include lighting/ADAS suppliers when OEM mix, order cadence and margin conversion drive rerating. SL had strong MFE, but post-peak drawdown says lifecycle local 4B should fire if OEM mix or margin evidence fades. | True | True |
| TRG_R12L81-C31-005860-HANIL-FEED-FOOD-SECURITY-LIFECYCLE | 005860 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should allow food-security/feed policy positives only when policy or grain-price attention maps to direct feed demand, purchase cost pass-through, customer volume, revenue conversion and margin bridge. Hanil Feed produced tradable MFE but later drawdown requires lifecycle 4B if direct-economics evidence fades. | True | True |
| R12_C31_005860_STAGE2A_20220224 | 005860 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_missed_structural | False | False |
| R12L10C31_005860_T1 | 005860 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_4B_too_late | False | False |
| R12L13_C31_005860_GRAIN_FEED_DIRECT_T_4B_20220422 | 005860 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_4B_too_late | False | False |
| R12L10C31_005860_T2 | 005860 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_4B_too_late | False | False |
| R13L10_T11_HANILFEED_EVENT_4B_TOO_LATE | 005860 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late | False | False |
| R13L13_X_R12L13_C31_005860_GRAIN_FEED_DIRECT_T_4B_20220422 | 005860 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late | False | False |
| R12L13_C31_005860_GRAIN_FEED_DIRECT_T_4B_20220422 | 005860 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late | False | False |
| C06_SEC_202407_Q2_MEMORY_RECOVERY_NO_HBM_QUAL_FALSE_POSITIVE | 005930 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_false_positive | False | False |
| R2L15_C06_005930_COUNTER_2024-01-02 | 005930 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_false_positive | False | False |
| R2L10_C06_005930_20240320_STAGE2WATCH | 005930 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_false_positive | False | False |
| TRG_R2L12_C06_SAMSUNG_20240320 | 005930 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_false_positive | False | False |
| TRG_R2L12_C06_SAMSUNG_20240524 | 005930 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_4C_too_late | False | False |
| C06_SEC_202410_HBM3E_DELAY_HARD4C_PROTECTION | 005930 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_4C_too_late | False | False |
| R13L15_X_TRIG_R2L15_C06_005930_COUNTER_2024-01-02 | 005930 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L12_FP_X05_005930_Stage3-Yellow_Weak-Green_2024-03-20 | 005930 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive | False | False |
| TRG_R6L81-C21-005940-NH-INVESTMENT-BROKERAGE-CAPITAL-RETURN-BRIDGE | 005940 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | C21 should protect securities/brokerage value-up positives when PBR/ROE rerating is backed by dividend or buyback policy, trading volume, retail brokerage, IB earnings and capital buffer. NH Investment had strong MFE with almost no entry-basis MAE. | True | True |
| C21-BROKER-NH-S2A-20240201 | 005940 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_late | False | False |
| R10L11-C30-DONGBU-STAGE2-20240125 | 005960 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive | False | False |
| R10L11_T05_DONGBU_POLICY_BETA_CAP | 005960 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive | False | False |
| TRG_R10L79-C30-005960-DONGBU-E&C-PF-HIGHMAE-LOCAL4B | 005960 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should flag local 4B when builder/PF fear aligns with persistent MAE and liquidity/orderbook risk, but hard 4C still requires non-price refinancing failure, default, covenant, impairment, auditor/control or solvency evidence. Dongbu E&C leaked into a high-MAE path with very limited MFE. | True | True |
| TRG_R10L75-C30-005960-DONGBU-PF-LIQUIDITY-LOCAL4B | 005960 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should flag local 4B when mid-builder PF/orderbook/liquidity risk produces weak MFE and widening MAE. Dongbu Construction had almost no upside and a later -25% MAE path, but hard 4C still requires explicit non-price refinancing, default, impairment, auditor/control or solvency break. | True | True |
| None | 005960 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | True | True |
| R13_CROSS_005960_2024-02-01_Stage4B-Local-PFRisk | 005960 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | True | True |
| TRG_R3L77-C11-006110-SAMA-ALUMINUM-FOIL-ORDERBOOK-THEME-FADE | 006110 | C11_BATTERY_ORDERBOOK_RERATING | C11 should not treat battery aluminum-foil or component-material beta as durable Stage2 unless customer call-off, contracted volume, utilization, price pass-through and margin evidence refreshes. Sama Aluminum had a strong MFE but later opened a very large MAE path, making it local 4B rather than durable Green. | True | True |
| TRG_R3L75-C12-006110-SAMA-ALUMINIUM-ALFOIL-CONTRACT-BETA-FADE | 006110 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | C12 should not treat aluminum-foil contract beta as durable Stage2 unless customer order, call-off cadence, utilization and margin bridge remain visible. Sama Aluminium had a strong early MFE but later collapsed, showing call-off and utilization risk. | True | True |
| TRG_R4L81-C16-006110-SAMA-ALUMINUM-FOIL-STRATEGIC-SUPPLY-FADE | 006110 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | C16 should not treat aluminum/battery-foil supply theme beta as durable Stage2 unless customer volume, utilization, orderbook, pricing and margin bridge are visible. Sam-A Aluminum had an early MFE, then a severe drawdown. | True | True |
| R6L10_C21_006220_STAGE2_20240226 | 006220 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | False | False |
| R6L32-C21-JEJU-PRICEONLY-2024-02-19 | 006220 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | False | False |
| R6L32-C21-JEJU-4B-2024-02-19 | 006220 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_4B_too_early_if_treated_as_full_exit | False | False |
| R6L10_C21_006220_4B_PRICE_ONLY_20240419 | 006220 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_4B_too_late | False | False |
| R13L26_C15_002_T1_STAGE2_ACTIONABLE | 006260 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_too_early | False | False |
| R13L26_C15_002_T2_STAGE4B_WATCH | 006260 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_4B_too_early | False | False |
| TRG_R1L76-C02-006340-DAEWON-CABLE-COPPER-GRID-THEME-FADE | 006340 | C02_POWER_GRID_DATACENTER_CAPEX | C02 should not treat copper/cable/grid theme spikes as durable Stage2 unless customer order, backlog, delivery and margin bridge are explicit. Daewon Cable had huge tradable MFE but then a deep post-peak drawdown, making it a theme-spike lifecycle local 4B row rather than durable Green. | True | True |
| R1L15_C02_DAEWON_20240513_FALSE_GREEN | 006340 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_false_positive | False | False |
| R1L16_C02_DAEWONWIRE_20240510_T1 | 006340 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_false_positive | False | False |
| R13L15_R1L15_C02_DAEWON_20240513_FALSE_GREEN | 006340 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| TRG_C05_006360_20230629_STAGE4C | 006360 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | current_profile_4C_should_route_fast_when_quality_cost_break_confirms_margin_gap | True | True |
| R1L15_C05_GS_4C_REMEDIATION_COST_MARGIN_BREAK_20230706 | 006360 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | current_profile_4C_too_late | False | False |
| R1L11_C05_006360_4C_20230706 | 006360 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | current_profile_4C_too_late | False | False |
| R10L15_T002 | 006360 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_4C_too_late | False | False |
| TRG_GS_EC_2023_HARD_4C_DEFECT_LOSS_2023_07_06 | 006360 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_4C_too_late | False | False |
| GS_2023_GEOMDAN_STAGE2_WATCH | 006360 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_too_early | False | False |
| R10L10_T03_GS_2023_QUALITY_INCIDENT_STAGE2_CAP | 006360 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive | False | False |
| TRG_GS_EC_2023_FALSE_GREEN_PRE_DEFECT_STAGE3_2023_04_21 | 006360 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive | False | False |
| R10L13-C30-GS-4B-20230706 | 006360 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_4C_too_early | False | False |
| TRG_R10L12_006360_20230706_4B_QUALITY_LEGAL_OVERLAY | 006360 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_4C_too_early | False | False |
| TRG_R10L12_006360_20230706_4B_QUALITY_LEGAL_OVERLAY | 006360 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_4C_too_early | False | False |
| TR-C30-006360-4C-20230706 | 006360 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_4C_too_late | False | False |
| R10L10-C30-GS-4C-20230706 | 006360 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_4C_too_late | False | False |
| R13L15_R10L15_T002 | 006360 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4C_too_late | False | False |
| R13L14_X_TRIG_GS_2023_GEOMDAN_STAGE2_WATCH | 006360 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_too_early | False | False |
| R13L13_X_R10L13-C30-GS-4B-20230706 | 006360 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4C_too_early | False | False |
| R10L13-C30-GS-4B-20230706 | 006360 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4C_too_early | False | False |
| R13L10_X07_006360_Stage4C | 006360 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4C_too_late | False | False |
| R13L15_X_TRIG_R1L15_C05_GS_4C_REMEDIATION_COST_MARGIN_BREAK_20230706 | 006360 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4C_too_late | False | False |
| TRG-R3L13-C11-006400-SAMSUNGSDI-FUTURE-JV-ORDER-HEADLINE-20231012 | 006400 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive | False | False |
| C12-R3L65-006400-T1 | 006400 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_too_late | False | False |
| R3L67_T04_SDI_2024_GM_JV_4B_OVERLAY | 006400 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_4B_too_late | False | False |
| R3L67_T04_SDI_2024_GM_JV_4B_OVERLAY | 006400 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_4B_too_late | False | False |
| R3L70_C13_006400_T2_STAGE2_ACTIONABLE_SECOND_KOKOMO_COUNTEREXAMPLE | 006400 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_too_early | False | False |
| R3L67_T03_SDI_2024_GM_JV_STAGE2A | 006400 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_false_positive | False | False |
| R3L67_T03_SDI_2024_GM_JV_STAGE2A | 006400 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_false_positive | False | False |
| TR-C13-SDI-20241203-STARPLUS-DOE-CONDITIONAL-LOAN | 006400 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_false_positive | False | False |
| R3L10-C13-006400-T1 | 006400 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_false_positive | False | False |
| R3L10-C13-006400-T1 | 006400 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_false_positive | False | False |
| TRG_R3L14_C13_SDI_20230425_STAGE2_JV_CAPPED | 006400 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_false_positive | False | False |
| R3L10-C13-006400-T1-4B-OVERLAY | 006400 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_4B_too_early | False | False |
| TRG-R3L14-C14-006400-FUTURE-JV-SLOWDOWN-20231012 | 006400 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_false_positive | False | False |
| TR_C14_006400_20240731_STAGE4B_TOO_EARLY | 006400 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_false_positive | False | False |
| R13L10_T04_SDI_PRICE_ONLY_4B_TOO_EARLY | 006400 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_early | False | False |
| R13L14_X_TRIG_TRG-R3L14-C14-006400-FUTURE-JV-SLOWDOWN-20231012 | 006400 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L13_X_TRG-R3L13-C11-006400-SAMSUNGSDI-FUTURE-JV-ORDER-HEADLINE-20231012 | 006400 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| TRG-R3L13-C11-006400-SAMSUNGSDI-FUTURE-JV-ORDER-HEADLINE-20231012 | 006400 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R4L13_C17_006650_T_STAGE2_20210208 | 006650 대한유화 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive | False | False |
| R4L13_C17_006650_T_4C_20210623 | 006650 대한유화 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_4C_too_late | False | False |
| R4L13_C15_T05 | 006650 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive | False | False |
| R13L26_C15_003_T1_STAGE2_WATCH | 006650 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive | False | False |
| R4L18-C17-KPIC-S2-2023-02-14 | 006650 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive | False | False |
| R4L13_C17_006650_T_STAGE2_20210208 | 006650 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive | False | False |
| R4L14_C17_T003 | 006650 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive | False | False |
| R4L12-C17-KPIC-S2-20230302 | 006650 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive | False | False |
| R13L26_C17_004_T1_STAGE2_YELLOW | 006650 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive | False | False |
| R4L16_C17_006650_T1_LATE_GREEN | 006650 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive | False | False |
| R4L11_C17_DAEHAN_20210216_GREEN_FALSE_POSITIVE | 006650 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive | False | False |
| R4L14_C17_T003_4C | 006650 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_4C_too_late | False | False |
| R4L13_C17_006650_T_4C_20210623 | 006650 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_4C_too_late | False | False |
| R13L13_X_R4L13_C17_006650_T_STAGE2_20210208 | 006650 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L14_X_TRIG_R4L14_C17_T003 | 006650 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R4L13_C17_006650_T_STAGE2_20210208 | 006650 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L14_X_TRIG_R4L14_C17_T003_4C | 006650 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4C_too_late | False | False |
| R13L13_X_R4L13_C17_006650_T_4C_20210623 | 006650 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4C_too_late | False | False |
| R4L13_C17_006650_T_4C_20210623 | 006650 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4C_too_late | False | False |
| R13L11_HIGHMAE_X05_006650_FALSEGREEN_20210216 | 006650 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | False | False |
| C21-BROKER-MIRAE-S2A-20240201 | 006800 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | False | False |
| TRG_R6L73-C21-006800-MIRAESEC-BROKERAGE-VALUEUP-BETA-FADE | 006800 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | C21 should not treat brokerage/value-up beta as durable Green unless recurring ROE, capital return, treasury-stock cancellation or distribution bridge is verified. Mirae generated MFE but later faded and needs local 4B/RiskWatch rather than durable Stage2. | True | True |
| TRG_R6L73-C21-006800-MIRAESEC-BROKERAGE-VALUEUP-BETA-FADE | 006800 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | C21 should not treat brokerage/value-up beta as durable Green unless recurring ROE, capital return, treasury-stock cancellation or distribution bridge is verified. Mirae generated MFE but later faded and needs local 4B/RiskWatch rather than durable Stage2. | True | True |
| TRG_R11L78-C04-006910-BOSEONG-POWERTEC-NUCLEAR-POLICY-EQUIPMENT-LIFECYCLE | 006910 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | C04 should allow nuclear-policy/project equipment rows only when policy headline maps to named project, equipment order, delivery schedule, revenue recognition and margin bridge. Boseong Powertec produced a meaningful MFE, then a post-peak drawdown, so it should be lifecycle-managed rather than permanent Green. | True | True |
| TRG_R2L75-C06-007660-ISU-PETASYS-AI-SERVER-MEMORY-SUBSTRATE-CAPACITY | 007660 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | C06 should not be limited to Samsung/SK Hynix memory makers. It should include AI server/HBM-adjacent memory-network substrate suppliers when customer capacity, order visibility and margin bridge are explicit. Isu Petasys produced strong MFE but later severe drawdown, so lifecycle local 4B is required if bridge evidence fades. | True | True |
| R12L11_C31_008040_GREEN_20220418 | 008040 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_too_late | False | False |
| R12_C31_TOUR_003_T1 | 008770 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| R13_C32_HANMI_2024_T1_OVERLAY | 008930 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive | False | False |
| R12L11C32_008930_T2_PROXY_REVERSAL_4C | 008930 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_4C_too_late | False | False |
| R11L12_C32_HANMI_2024_T1 | 008930 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive | False | False |
| R12L11C32_008930_HANMI_SCIENCE_OCI_INTEGRATION_PROXY_REVERSAL_T1_STAGE2_ACTIONABLE | 008930 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive | False | False |
| TR_R11L14_HANMI_OCI_STAGE2A_20240115 | 008930 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive | False | False |
| R13_C32_HANMI_2024_T1 | 008930 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive | False | False |
| TR_C32_008930_STAGE2_2024-01-15 | 008930 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive | False | False |
| TRG_R12L75-C32-008930-HANMI-SCIENCE-CONTROL-DISPUTE-BENEFICIARY-FADE | 008930 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should not treat control dispute or group-combination headlines as durable Stage2 unless listed-shareholder beneficiary, transaction mechanics, closing certainty, capital policy or operating bridge is explicit. Hanmi Science produced an event spike but later opened severe MAE and requires share-count validation. | True | True |
| TRG_R11L80-C32-008930-HANMI-SCIENCE-GOVERNANCE-MERGER-PROXY-SPIKE-FADE | 008930 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should not treat governance/proxy-fight spike beta as durable Stage2 unless a clear tender/control-price anchor, completion probability, legal timetable, shareholder vote mechanics and downside cap are visible. Hanmi Science produced a sharp spike then a severe drawdown. | True | True |
| C32_HANMI_2024_T1 | 008930 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive | False | False |
| TRG_R12L72-C32-008930-HANMI-SCIENCE-OCI-CONTROL-CONTEST-BLOWOFF | 008930 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should not treat a control-contest / group-integration headline as durable Stage2 unless closing path, tender price, board/shareholder approval and execution certainty are visible. The price path had fast MFE but later MAE opened materially. | True | True |
| TRG_R12L72-C32-008930-HANMI-SCIENCE-OCI-CONTROL-CONTEST-BLOWOFF | 008930 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should not treat a control-contest / group-integration headline as durable Stage2 unless closing path, tender price, board/shareholder approval and execution certainty are visible. The price path had fast MFE but later MAE opened materially. | True | True |
| TR_R11L14_HANMI_SHAREHOLDER_VOTE_4C_20240328 | 008930 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_4C_too_late | False | False |
| R13L14_G06_15_008930_TR_R11L14_HANMI_SHAREHOLDER_VOTE_4C_20240328 | 008930 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_4C_too_late | False | False |
| TR_R11L13_DONGYANG_POLICY_STAGE2A_20240603 | 008970 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| TR_R11L11_DONGYANG_STAGE2_2024_06_03 | 008970 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| TRG_R11L76-C31-008970-DONGYANG-STEEL-PIPE-EASTSEA-GAS-POLICY-PIPE-BETA-FADE | 008970 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should not treat gas-field / pipeline policy beta as durable Stage2 unless direct beneficiary mapping, confirmed order, project schedule, revenue and margin bridge are visible. Dongyang Steel Pipe had a tradable MFE but then high MAE and repeated share-count movement, making it local 4B rather than Green. | True | True |
| TRG_R11L74-C31-008970-DONGYANG-PIPELINE-POLICY-PROXY-FADE | 008970 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should not convert a pipeline/steel-pipe policy proxy into durable Stage2 unless project ownership, procurement scope, actual order, EPC participation or revenue timing is visible. KBI Dongyang Steel Pipe had a large initial MFE but then deep MAE and post-peak drawdown. | True | True |
| TRG_R11L74-C31-008970-DONGYANG-PIPELINE-POLICY-PROXY-FADE | 008970 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should not convert a pipeline/steel-pipe policy proxy into durable Stage2 unless project ownership, procurement scope, actual order, EPC participation or revenue timing is visible. KBI Dongyang Steel Pipe had a large initial MFE but then deep MAE and post-peak drawdown. | True | True |
| TR_R11L13_DONGYANG_4B_PRICE_20240607 | 008970 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_4B_too_late | False | False |
| R12L15_TR_HANSSEM_STAGE2_20210714 | 009240 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive | False | False |
| R13L15_X_TRIG_R12L15_TR_HANSSEM_STAGE2_20210714 | 009240 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R7L15-C24-009420-T1-IMVT1402-PH1-STAGE2A-20230927 | 009420 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_too_early | False | False |
| R7L15-C24-009420-T1-IMVT1402-PH1-STAGE2A-20230927 | 009420 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_too_early | False | False |
| TRG_R13L32_009420_STAGE2_20230927 | 009420 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_correct | True | False |
| TRG_R13L32_009420_STAGE3GREEN_20231227 | 009420 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_correct | True | False |
| R4L14_C16_T03_POSCOMTECH_20230726_FALSE_GREEN | 009520 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_false_positive | False | False |
| R13L14_G02_05_009520_R4L14_C16_T03_POSCOMTECH_20230726_FALSE_GREEN | 009520 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | False | False |
| TRIG_R1L14_C01_KSOE_STAGE2_20230104 | 009540 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_too_late | False | False |
| R13L14_X_TRIG_TRIG_R1L14_C01_KSOE_STAGE2_20230104 | 009540 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_too_late | False | False |
| R13L28_C17_003_T1_STAGE2_HEADLINE | 009830 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive | False | False |
| T_R9L15_009900_STAGE2_20230811 | 009900 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| TRG_R9L79-C29-009900-MYOUNGSHIN-EV-BODY-PARTS-THEME-FADE | 009900 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should not treat EV body/parts beta as durable Stage2 unless customer program, volume, utilization, pricing and margin bridge are visible. Myoung Shin Industrial had a small early MFE and then a severe MAE drawdown path. | True | True |
| T_R9L15_009900_4C_20240117 | 009900 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_4C_too_late | False | False |
| R13L15_X_TRIG_T_R9L15_009900_STAGE2_20230811 | 009900 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L15_X_TRIG_T_R9L15_009900_4C_20240117 | 009900 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4C_too_late | False | False |
| R4L13_C15_T03 | 010060 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_4B_too_early | False | False |
| R13L28_C17_001_T1_STAGE2_ACTIONABLE | 010060 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_missed_structural | False | False |
| R4L10-C17-OCI-S2A-20210215 | 010060 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_too_early | False | False |
| R13L28_C17_001_T2_STAGE3_GREEN_LATE | 010060 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_too_late | False | False |
| TRG_R9L77-C29-010100-KOREA-MOVENEX-AUTO-PARTS-VOLUME-MARGIN-FADE | 010100 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should not treat auto-parts or drivetrain component beta as durable Stage2 unless named customer program, volume, mix, pricing and margin bridge are visible. Korea Movenex produced an early spike, then leaked into a high-MAE drawdown. | True | True |
| TRG_C01_010120_20240405_STAGE2A | 010120 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_missed_structural_if_C01_bridge_not_available | True | False |
| R1L15_C02_LSE_20240717_4B_OVERLAY | 010120 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_4B_too_early | False | False |
| R1L10_C02_010120_STAGE2A_2024_01_03 | 010120 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_too_late | False | True |
| TRIG_R1L13_C02_LSE_STAGE2_20240103 | 010120 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_missed_structural | False | False |
| R1L12_C02_LSE_STAGE2A_20240305 | 010120 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_too_late | False | False |
| C02_010120_20240305_STAGE2_GRID_DC_ORDER_VISIBILITY | 010120 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_missed_structural_scope_C02_absent_or_underweighted | True | False |
| R1L10_C02_LS_HIGH_MAE_20240429 | 010120 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_too_early | False | False |
| TR_LSE_20240701_S2A | 010120 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_too_early | False | False |
| R1L15_C02_LSE_20240524_LATE_GREEN | 010120 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_false_positive | False | False |
| R1L10_C02_010120_4B_WATCH_2024_04_12 | 010120 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_correct | False | True |
| R1L12_C02_LSE_STAGE4B_20240529 | 010120 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_4B_too_late | False | False |
| TR_LSE_20240723_4B | 010120 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_4B_too_early | False | False |
| C02_010120_20240724_STAGE4B_FULL_WINDOW_PEAK_CAPTURE | 010120 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_correct_if_non_price_4B_overlay_allowed_for_C02 | True | False |
| R13L13_X_TRIG_R1L13_C02_LSE_STAGE2_20240103 | 010120 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_missed_structural | False | False |
| R13L10_X01_010120_Stage2-Actionable | 010120 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_too_early | False | False |
| TRIG_R1L13_C02_LSE_STAGE2_20240103 | 010120 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_missed_structural | False | False |
| R13L15_R1L15_C02_LSE_20240524_LATE_GREEN | 010120 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L12_FP_X12_010120_Stage4B_2024-05-29 | 010120 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_4B_too_late | False | False |
| R4L12_C15_010130_T1 | 010130 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive | False | False |
| TRG_R4L80-C15-010130-KOREA-ZINC-NONFERROUS-SPREAD-EVENT-LIFECYCLE | 010130 | C15_MATERIAL_SPREAD_SUPERCYCLE | C15 should allow nonferrous smelter positives only when zinc/copper/precious-metal spread, TC/RC, inventory, utilization and margin bridge are visible. Korea Zinc produced enormous MFE, but a late governance/tender-event component must be separated from commodity-spread economics before runtime promotion. | True | True |
| R4L14_C16_T04_KOREAZINC_20220915_STAGE2_FALSE_START | 010130 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_too_early | False | False |
| T_C32_010130_20241029_4B_OVERLAY | 010130 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_4B_too_late | False | False |
| R12L11C32_010130_T2_SHARE_ISSUE_FSS_4B | 010130 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_4B_too_late | False | False |
| TR_C32_010130_4B_2024-12-05 | 010130 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_4B_too_late | False | False |
| TRG_KZ_20240913_MBK_YP_TENDER_STAGE2 | 010130 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_missed_structural | False | False |
| R11L12_C32_KZINC_2024_T1 | 010130 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_missed_structural | False | False |
| R12L13_C32_KZ_STAGE2_2024_09_13 | 010130 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_too_late | False | False |
| R12L11C32_010130_KOREA_ZINC_HOSTILE_TENDER_CONTROL_PREMIUM_T1_STAGE2_ACTIONABLE | 010130 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_4B_too_late | False | False |
| R12L15_TR_KZ_STAGE2_20240913 | 010130 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_4B_too_late | False | False |
| R11L10-C32-KZ-Stage2-20240913 | 010130 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_4B_too_late | False | False |
| R13_C32_KZ_2024_T1 | 010130 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_4B_too_late | False | False |
| TR_C32_010130_STAGE2_2024-09-13 | 010130 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_too_early | False | False |
| R13L20-C32-KZ-STAGE2-20240913 | 010130 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_4B_too_early | False | False |
| TRG-C32-KZ-20240913-STAGE2A | 010130 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_missed_structural | False | False |
| R12L10C32_KZINC_T1_STAGE2_EVENT_2024_09_13 | 010130 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive | False | False |
| TR_R11L14_KOREAZINC_TENDER_STAGE2A_20240913 | 010130 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_4B_too_early | False | False |
| T_C32_010130_20240913_STAGE2_ACTIONABLE | 010130 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_too_late | False | False |
| R13_C32_KZ_2024_T1_OVERLAY | 010130 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_4B_too_late | False | False |
| R11L15_C32_KZ_010130_T2_COURT_BUYBACK_4B_TOO_EARLY | 010130 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_4B_too_early | False | False |
| TRG_KZ_20241031_SHARE_ISSUE_4B_GOV_RISK | 010130 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_4B_too_early | False | False |
| TR_R11L14_KOREAZINC_SHARE_ISSUE_4B_20241031 | 010130 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_4B_too_early | False | False |
| R12L13_C32_KZ_4B_2024_10_31 | 010130 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_4B_too_early | False | False |
| TRG-C32-KZ-20241031-4B-WATCH | 010130 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_4B_too_early | False | False |
| TR_R13L44_KZ_4B_CAPITAL_RAISE_FSS_20241031 | 010130 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_4B_too_early | False | False |
| R13L20-C32-KZ-4B-20241205 | 010130 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_4B_too_late | False | False |
| R11L10-C32-KZ-4B-20241206 | 010130 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_4B_too_late | False | False |
| R13L11_REDTEAM__R12L11C32_010130_T2_SHARE_ISSUE_FSS_4B | 010130 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late | False | False |
| R13L10_T10_KOREAZINC_FULL_WINDOW_4B | 010130 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late | False | False |
| R13L11_REDTEAM__R12L11C32_010130_KOREA_ZINC_HOSTILE_TENDER_CONTROL_PREMIUM_T1_STAGE2_ACTIONABLE | 010130 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late | False | False |
| R13L15_X_TRIG_R12L15_TR_KZ_STAGE2_20240913 | 010130 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late | False | False |
| TRIG_R1L14_C01_SHI_STAGE2_20230131 | 010140 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_missed_structural | False | False |
| TRG_R1L77-C01-010140-SAMSUNG-HI-SHIPBUILDING-BACKLOG-MARGIN | 010140 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | C01 should allow shipbuilding orderbook Stage2 when backlog, LNG/offshore mix, pricing discipline, delivery schedule and margin bridge are visible. Samsung Heavy produced a large MFE with controlled entry-basis MAE, but post-peak drawdown requires lifecycle local 4B if backlog/margin evidence fades. | True | True |
| R13L14_X_TRIG_TRIG_R1L14_C01_SHI_STAGE2_20230131 | 010140 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_missed_structural | False | False |
| TRIG_R1L14_C01_MIPO_STAGE2_20240213 | 010620 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_missed_structural | False | False |
| TRG_R1L73-C01-010620-HDMIPO-MIDSHIP_PRODUCT_MIX_MARGIN_BRIDGE | 010620 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | C01 should capture mid-size vessel backlog recovery when product mix and margin conversion are visible. But after the 2025 peak, a later local 4B-watch is needed if the margin bridge stops refreshing or drawdown opens. | True | True |
| TRG_R1L73-C01-010620-HDMIPO-MIDSHIP_PRODUCT_MIX_MARGIN_BRIDGE | 010620 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | C01 should capture mid-size vessel backlog recovery when product mix and margin conversion are visible. But after the 2025 peak, a later local 4B-watch is needed if the margin bridge stops refreshing or drawdown opens. | True | True |
| R13L14_X_TRIG_TRIG_R1L14_C01_MIPO_STAGE2_20240213 | 010620 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_missed_structural | False | False |
| T_R9L15_010690_STAGE2_20230309 | 010690 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_too_late | False | False |
| R13L15_X_TRIG_T_R9L15_010690_STAGE2_20230309 | 010690 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_too_late | False | False |
| TRG_R10L82-C30-010780-ISDONGSEO-PF-HOUSING-RECOVERY-SHARECOUNT | 010780 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should allow builder recovery rows only when housing project quality, orderbook, PF exposure, refinancing access, liquidity and margin bridge are visible. IS Dongseo produced tradable MFE but later post-peak drawdown and stock-web share-count movement require lifecycle 4B discipline and validation. | True | True |
| TRG_R10L78-C30-010780-ISDONGSEO-PF-RECOVERY-SPIKE-NO-HARD4C | 010780 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should not over-convert builder/developer PF fear into hard 4C when the path produces recovery MFE and entry-basis MAE remains bounded. IS Dongseo needs PF/liquidity/orderbook monitoring, but price alone is not confirmed balance-sheet break evidence. | True | True |
| R10L13_C30_010780_T_STAGE2_20240327 | 010780 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive | False | False |
| R13L13_ACC_X10_010780_20240327 | 010780 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | False | False |
| R1L13_C03_010820_STAGE2WATCH_20220224 | 010820 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_false_positive | False | False |
| TRG_R1L82-C03-010820-FIRSTEC-DEFENSE-COMPONENT-THEME-WHIPSAW | 010820 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | C03 should not treat defense component/drone/robot theme beta as durable Stage2 unless contract backlog, customer program, delivery schedule, revenue conversion and margin bridge are visible. Firstec had a late theme spike but also a deep interim MAE, so it is a whipsaw/local-4B boundary rather than durable Green. | True | True |
| TRG_R11L79-C03-010820-FIRSTEC-DEFENSE-DRONE-THEME-BACKLOG-GAP | 010820 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | C03 should not treat drone/defense component theme beta as durable Stage2 unless named export framework, order backlog, delivery schedule, revenue recognition and margin bridge are visible. Firstec had limited early MFE, then high MAE, and a late theme spike; without backlog/margin proof it should be local 4B-watch rather than durable Green. | True | True |
| TRG_R1L74-C03-010820-FIRSTEC-DEFENSE-ELECTRONICS-PRICE-BETA | 010820 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | C03 should not treat defense electronics or drone-theme price beta as durable Stage2 unless named export order, customer framework, backlog conversion or margin bridge is visible. Firstec had a same-day spike but later MAE and drawdown opened, so it is a local 4B-watch / false Stage2 row. | True | True |
| TRG_R1L74-C03-010820-FIRSTEC-DEFENSE-ELECTRONICS-PRICE-BETA | 010820 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | C03 should not treat defense electronics or drone-theme price beta as durable Stage2 unless named export order, customer framework, backlog conversion or margin bridge is visible. Firstec had a same-day spike but later MAE and drawdown opened, so it is a local 4B-watch / false Stage2 row. | True | True |
| TRG_R11L77-C03-010820-FIRSTEC-DEFENSE-UNMANNED-THEME-BETA-FADE | 010820 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | C03 should not treat defense/unmanned-system theme beta as durable Stage2 unless named defense program, contract backlog, delivery schedule, revenue recognition and margin bridge are visible. Firstec had tradable MFE but spent much of the window in drawdown and only later spiked, making it a local 4B-watch boundary rather than durable Green. | True | True |
| R13L14_X_TRIG_R11L14_C31_010820_20220224_T1 | 010820 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L14_X_TRIG_R11L14_C31_010820_20220608_4B | 010820 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late | False | False |
| TRG_R4L73-C17-010950-SOIL-REFINING-SPREAD-BETA-LOCAL4B | 010950 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | C17 should not treat refinery spread beta as Green unless crack spread, inventory, utilization, and earnings revision bridge are visible. S-Oil produced almost no MFE and later severe 180D MAE, so local 4B-watch is more appropriate. | True | True |
| TRG_R4L73-C17-010950-SOIL-REFINING-SPREAD-BETA-LOCAL4B | 010950 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | C17 should not treat refinery spread beta as Green unless crack spread, inventory, utilization, and earnings revision bridge are visible. S-Oil produced almost no MFE and later severe 180D MAE, so local 4B-watch is more appropriate. | True | True |
| TRG_R5L75-C18-011150-CJ-SEAFOOD-KFOOD-THEME-SPIKE-FADE | 011150 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | C18 should not treat K-food or seafood export theme spikes as durable Stage2 unless sell-through, reorder cadence, customer/channel expansion and margin bridge are visible. CJ Seafood had an enormous tradable MFE but then a sharp post-peak drawdown, so it is a theme-spike local 4B row rather than durable Green. | True | True |
| R12L12C31_011150_T1_RELEASE_ANNOUNCEMENT | 011150 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| R12_C31_011150_STAGE2WATCH_20230822 | 011150 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| R13L12_REDTEAM__R12L12C31_011150_T1_RELEASE_ANNOUNCEMENT | 011150 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R4L13_C17_011170_T_STAGE2_20210205 | 011170 롯데케미칼 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive | False | False |
| R4L13_C15_T04 | 011170 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive | False | False |
| R4L9_C15_011170_T1 | 011170 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive | False | False |
| R4L18-C17-LOTTECHEM-S2-2023-02-14 | 011170 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive | False | False |
| R4L13_C17_011170_T_STAGE2_20210205 | 011170 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive | False | False |
| R4L10-C17-LOTTECHEM-S2A-20210223 | 011170 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive | False | False |
| R4L10_C17_011170_T1 | 011170 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive | False | True |
| R4L12-C17-LOTTE-S2-20230302 | 011170 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive | False | False |
| R4L11-C17-011170-S2A-20240124 | 011170 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive | False | False |
| R13L26_C17_003_T1_STAGE2_YELLOW | 011170 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive | False | False |
| R4L11_T03_LOTTECHEM_20210223_FALSE_GREEN_SPREAD_BETA | 011170 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive | False | False |
| R4L11_C17_LOTTE_20210223_GREEN_FALSE_POSITIVE | 011170 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive | False | False |
| R4L16_C17_011170_T1_FALSE_GREEN | 011170 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive | False | False |
| R13L10_T05_LOTTECHEM_SPREAD_4C_LATE | 011170 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L13_X_R4L13_C17_011170_T_STAGE2_20210205 | 011170 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R4L13_C17_011170_T_STAGE2_20210205 | 011170 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L11_REDTEAM__R4L11_T03_LOTTECHEM_20210223_FALSE_GREEN_SPREAD_BETA | 011170 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L12_FP_X07_011170_Stage2-Actionable_2023-03-02 | 011170 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive | False | False |
| R12L13_C32_HMM_4C_2024_02_07 | 011200 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_4C_too_late | False | False |
| R12L11C32_011200_T2_SALE_COLLAPSE_4C | 011200 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_4C_too_late | False | False |
| R11L12_C32_HMM_2023_T1 | 011200 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive | False | False |
| R12L13_C32_HMM_STAGE2_2023_12_18 | 011200 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive | False | False |
| R12L11C32_011200_HMM_PREFERRED_BIDDER_FINANCING_OVERHANG_T1_STAGE2_ACTIONABLE | 011200 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive | False | False |
| R11L10-C32-HMM-Stage2-20231218 | 011200 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive | False | False |
| TR_R11L14_HMM_PRIVATIZATION_STAGE2A_20231219 | 011200 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive | False | False |
| TRG-C32-HMM-20231219-STAGE2A | 011200 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive | False | False |
| TR_HMM_HARIM_20231220_STAGE2A | 011200 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive | False | False |
| C32_HMM_2023_T1 | 011200 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive | False | False |
| TRG-C32-HMM-20240208-4C | 011200 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_4C_too_late | False | False |
| R13L12_REDTEAM__R11L12_C32_HMM_2023_T1 | 011200 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L13_ACC_X12_011200_20231218 | 011200 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | False | False |
| T-C29-HYUNDAIWIA-20210108-S2A | 011210 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_too_early | False | False |
| TR_R9L10_011210_S2_20230411 | 011210 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_too_early | False | False |
| TR-C29-WIA-S2A-20230627 | 011210 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| R9L33-T005-HYWIA-STAGE2-THERMAL | 011210 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| T_R9L11_011210_STAGE2 | 011210 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| T-C29-HYUNDAIWIA-20210121-4BLOCAL | 011210 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_4B_too_early | False | False |
| R9L33-T006-HYWIA-4C-PRICECONFIRM | 011210 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_4C_too_late | False | False |
| R4L13_C17_011780_T_GREEN_20210121 | 011780 금호석유화학 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_too_late | False | False |
| R4L9_C15_011780_T1 | 011780 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_too_late | False | False |
| R4L10_C17_011780_T1 | 011780 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_correct | False | True |
| R4L14_C17_T002 | 011780 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_missed_structural | False | False |
| R4L16_C17_011780_T1_STAGE2 | 011780 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_4B_too_late | False | False |
| R4L13_C17_011780_T_GREEN_20210121 | 011780 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_too_late | False | False |
| R4L11_C17_KUMHO_20210128_GREEN_COMPARE | 011780 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_too_late | False | False |
| R13L26_C17_002_T2_STAGE3_GREEN_LATE | 011780 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_too_late | False | False |
| R4L11_T01B_KUMHO_20210506_4B_SPREAD_PEAK_OVERLAY | 011780 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_4B_too_late | False | False |
| R13L14_X_TRIG_R4L14_C17_T002 | 011780 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_missed_structural | False | False |
| R13L13_X_R4L13_C17_011780_T_GREEN_20210121 | 011780 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_too_late | False | False |
| R4L13_C17_011780_T_GREEN_20210121 | 011780 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_too_late | False | False |
| TRG_R3L13_C12_SKC_20230726_STAGE2_CAPPED | 011790 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_false_positive | False | False |
| TRG_R3L13_C12_SKC_20230726_STAGE2_CAPPED | 011790 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_false_positive | False | False |
| TRG_R3L81-C13-011790-SKC-COPPERFOIL-AMPC-IRA-EVENT-SEPARATION | 011790 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | C13 should not blindly credit a whole SKC rally to battery JV/AMPC economics. A valid positive needs copper-foil customer/JV visibility, US capacity, utilization, IRA/AMPC economics, revenue and margin bridge; non-battery event/theme components must be separated. | True | True |
| TRG-R3L15-C14-011790-STAGE2-WATCH-20240425 | 011790 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_4C_too_early | False | False |
| R13L28_C17_004_T1_STAGE3_LATE_OR_4B | 011790 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_4B_too_late | False | False |
| R13L15_X_TRIG_TRG-R3L15-C14-011790-STAGE2-WATCH-20240425 | 011790 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4C_too_early | False | False |
| R13L13_ACC_X09_011790_20230726 | 011790 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | False | False |
| TRG_R4L75-C16-011810-STX-RESOURCE-TRADING-POLICY-BETA-FADE | 011810 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | C16 should not treat resource trading or offtake-policy beta as durable Stage2 unless named supply/offtake, inventory, customer and margin bridge is visible. STX had a short spike but then opened a long high-MAE drawdown path. | True | True |
| TR_C16_KDINV_S2_20221020 | 012320 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_4B_too_late | True | True |
| R9L13_C29_MOBIS_2023_VOLUME_READTHROUGH | 012330 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| None | 012330 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | True | True |
| TRG_R9L74-C29-012330-HYUNDAI-MOBIS-MODULE-ELECTRIFICATION-MARGIN | 012330 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should allow Stage2 for non-OEM auto modules when value-up attention connects to A/S parts, electrification module mix, capital return and margin bridge. Hyundai Mobis produced controlled MAE and a clean MFE path, but shard share-count changes need validation. | True | True |
| TRG_R9L74-C29-012330-HYUNDAI-MOBIS-MODULE-ELECTRIFICATION-MARGIN | 012330 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should allow Stage2 for non-OEM auto modules when value-up attention connects to A/S parts, electrification module mix, capital return and margin bridge. Hyundai Mobis produced controlled MAE and a clean MFE path, but shard share-count changes need validation. | True | True |
| R13_CROSS_012330_2024-02-01_Stage2-Actionable-AutoPartsMarginBridge | 012330 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | True | True |
| TRG_R9L78-C29-012330-HYUNDAI-MOBIS-MODULE-AS-MARGIN-BRIDGE | 012330 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should preserve large auto-module and AS-parts suppliers when customer volume, module mix, AS parts profitability, electrification exposure and margin bridge are visible. Hyundai Mobis produced a slow MFE with controlled MAE; it should not be overblocked, but lifecycle local 4B is needed if mix/margin evidence fades. | True | True |
| TRG_R9L76-C29-012330-HYUNDAI-MOBIS-MODULE-AS-MIX-CAPITAL-RETURN | 012330 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should preserve large-cap mobility supplier positives when module/A/S mix, electrification exposure, customer program stability, capital return and margin bridge are visible. Hyundai Mobis had a slow low-MAE rerating path rather than a theme spike. | True | True |
| R1L13_C03_012450_STAGE2A_20220302 | 012450 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_too_late | False | False |
| R1L14-C03-HANWHA-20220829-STAGE2A | 012450 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_too_early | False | False |
| R1L13-HANWHA-20240425-S2A | 012450 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_too_late | False | False |
| R1L11_T01B_HANWHA_4B_FULL_WINDOW_CHECK | 012450 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_4B_too_late | False | False |
| R13L59-T002 | 012450 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_4B_too_early | False | False |
| R13L14_X_TRIG_R11L14_C31_012450_20220728_T1 | 012450 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_too_late | False | False |
| R13L14_G01_01_012450_R1L14-C03-HANWHA-20220829-STAGE2A | 012450 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_too_early | False | False |
| R13L39_C28_012510_STAGE2_20190527 | 012510 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_too_late | False | False |
| R8L12_C28_T001 | 012510 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_too_late | False | False |
| C28_DOUZONE_2020_STAGE2A_2020-04-29 | 012510 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_too_late | False | False |
| R8L12_C28_DOUZONE_T1_STAGE2_ACTIONABLE_2023-11-03 | 012510 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_missed_structural | False | False |
| R8L12_C28_DOUZONE_T1_STAGE2_ACTIONABLE_2023-11-03 | 012510 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_missed_structural | False | False |
| R13L39_C28_012510_GREEN_20200416 | 012510 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_too_late | False | False |
| C28_DOUZONE_2020_GREEN_2020-09-04 | 012510 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_too_late | False | False |
| R8L12_C28_T002 | 012510 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_too_late | False | False |
| R8L12_C28_DUZON_GREEN_20240404 | 012510 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_too_late | False | False |
| R8L12_C28_DOUZONE_T2_STAGE3_GREEN_2024-04-09 | 012510 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_too_late | False | False |
| R8L21_C28_012510_T2_4B_OVERLAY | 012510 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_4B_too_late | False | False |
| R8L21_C28_012510_T2_4B_OVERLAY | 012510 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_4B_too_late | False | False |
| R12L14_C31_012690_STAGE2WATCH_20200120 | 012690 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| TRG_R4L74-C15-012800-DAECHANG-COPPER-BRASS-PRICE-BETA-FADE | 012800 | C15_MATERIAL_SPREAD_SUPERCYCLE | C15 should not treat copper/brass price beta as durable Stage2 unless spread-to-margin and inventory/export bridge refreshes. Daechang produced a large MFE but quickly fell into high MAE and post-peak drawdown, so it is a false Stage2 / local 4B-watch row. | True | True |
| TRG_R4L74-C15-012800-DAECHANG-COPPER-BRASS-PRICE-BETA-FADE | 012800 | C15_MATERIAL_SPREAD_SUPERCYCLE | C15 should not treat copper/brass price beta as durable Stage2 unless spread-to-margin and inventory/export bridge refreshes. Daechang produced a large MFE but quickly fell into high MAE and post-peak drawdown, so it is a false Stage2 / local 4B-watch row. | True | True |
| TRG_R4L77-C15-012800-DAECHANG-COPPER-BRASS-SPREAD-THEME-FADE | 012800 | C15_MATERIAL_SPREAD_SUPERCYCLE | C15 should not treat copper/brass price beta as durable Stage2 unless spread, inventory, volume, price pass-through and margin evidence refreshes. Daechang produced large tradable MFE, then opened high MAE and deep post-peak drawdown. | True | True |
| R4L16_C15_012800_T1 | 012800 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive | False | False |
| R4L16_C15_012800_T1 | 012800 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive | False | False |
| TRG_R10L80-C30-013360-ILSEONG-E&C-RECOVERY-SPIKE-NO-HARD4C | 013360 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should not convert small-builder/PF fear into hard 4C when the path still produces a recovery spike and MAE remains below severe threshold. Price action alone is not balance-sheet-break evidence. | True | True |
| R10L13_C30_013360_T_STAGE2_20240327 | 013360 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_4B_too_late | False | False |
| TRG_R10L80-C30-013580-KYERYONG-E&C-BOUNDED-RISKWATCH-NO-FORCED4B | 013580 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should keep PF/orderbook monitoring active for bounded builders, but should not force local 4B or hard 4C when MAE is contained and no non-price refinancing or solvency break is confirmed. | True | True |
| R10L11_T04_KYERYONG_POLICY_BETA_CAP | 013580 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_too_early | False | False |
| TRG_R10L75-C30-013580-KYERYONG-BUFFERED-BUILDER-NO-HARD4C | 013580 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should not convert every regional-builder PF fear into full 4B or hard 4C when MAE is bounded and the stock shows recovery/sideways behavior. Kyeryong Construction is a buffered RiskWatch row: PF/orderbook watch is allowed, but hard balance-sheet break is not price-only. | True | True |
| None | 013580 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | True | True |
| R13_CROSS_013580_2024-02-01_Stage2-RiskWatch_/_NoFull4B | 013580 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | True | True |
| TRG_R11L81-C31-013990-AGABANG-LOWBIRTH-CHILDCARE-POLICY-LIFECYCLE | 013990 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should allow low-birth/childcare policy positives only when policy attention maps to direct beneficiary demand, baby-product sales, channel sell-through, revenue conversion and margin bridge. Agabang Company produced tradable MFE but later high MAE, so it is lifecycle-managed rather than durable Green. | True | True |
| TRG_R12L77-C31-013990-AGABANG-LOW-BIRTH-CHILDCARE-POLICY-LIFECYCLE | 013990 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 can allow a policy-event lifecycle candidate when low-birth or childcare policy maps to direct beneficiary demand, sell-through, inventory normalization and margin bridge. Agabang produced a large MFE, but later drawdown means it cannot remain Green unless direct-demand and margin evidence refreshes. | True | True |
| R12L12C31_014710_T1_RELEASE_ANNOUNCEMENT | 014710 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| TRG_R10L81-C30-014790-HL-DNI-MID-BUILDER-ORDERBOOK-RECOVERY | 014790 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should allow builder recovery rows only when orderbook, housing project quality, PF exposure, refinancing access, liquidity and margin bridge are visible. HL D&I produced large MFE with controlled entry-basis MAE, but it cannot become durable recovery without PF/orderbook source repair. | True | True |
| TR-C30-014790-S2WATCH | 014790 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive | False | False |
| TRG_R4L76-C17-014830-UNID-KOH-CAUSTIC-POTASH-SPREAD-BRIDGE | 014830 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | C17 should allow chemical commodity Stage2 when the commodity price/spread move connects to inventory, export demand, utilization and margin bridge. Unid produced large MFE with controlled entry-basis MAE, but the later post-peak drawdown requires lifecycle local 4B if KOH/spread/margin evidence fades. | True | True |
| TRG_R4L79-C17-014830-UNID-KOH-SPREAD-MARGIN-LIFECYCLE | 014830 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | C17 should allow chemical spread positives only when commodity price/cost spread, export demand, inventory, utilization and margin bridge refreshes. Unid produced meaningful MFE and then a drawdown; it is Stage2 only after source repair and lifecycle-managed if spread/margin evidence fades. | True | True |
| TRG_R4L73-C17-014830-UNID-CAUSTIC-POTASH-SPREAD-MARGIN-BRIDGE | 014830 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | C17 should allow Stage2 only when a commodity/spread move connects to product-specific spread, export price, cost pass-through, and margin conversion. 유니드 produced a real MFE path, but later collapse means local 4B-watch should activate if spread evidence stops refreshing. | True | True |
| TRG_R4L73-C17-014830-UNID-CAUSTIC-POTASH-SPREAD-MARGIN-BRIDGE | 014830 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | C17 should allow Stage2 only when a commodity/spread move connects to product-specific spread, export price, cost pass-through, and margin conversion. 유니드 produced a real MFE path, but later collapse means local 4B-watch should activate if spread evidence stops refreshing. | True | True |
| TR-C29-SUNGWOO-S2A-20230216 | 015750 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_missed_structural | False | False |
| T_R9L15_015750_STAGE2_20230216 | 015750 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_too_late | False | False |
| R13L15_X_TRIG_T_R9L15_015750_STAGE2_20230216 | 015750 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_too_late | False | False |
| R11L13_C31_KVU_KEPCO_015760_STAGE2A_FALSE_20240226 | 015760 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| TRG_R12L79-C31-015760-KEPCO-TARIFF-NORMALIZATION-DEBT-RECOVERY | 015760 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 can allow public-utility policy rows when tariff normalization maps to direct beneficiary economics, fuel-cost pass-through, debt recovery, earnings bridge and regulatory visibility. KEPCO produced meaningful MFE with bounded entry-basis MAE, but later drawdown means tariff/debt/earnings evidence must refresh. | True | True |
| TR_R11L12_KEPCO_VALUEUP_FALSEPOS_20240226 | 015760 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| C21-BROKER-SAMSUNG-S2A-20240201 | 016360 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_late | False | False |
| TRG_R1L78-C02-017040-KWANGMYUNG-ELECTRIC-SWITCHGEAR-THEME-FADE | 017040 | C02_POWER_GRID_DATACENTER_CAPEX | C02 should not treat switchgear/electrical-equipment theme beta as durable Stage2 unless customer order, backlog conversion, delivery schedule, ASP and margin bridge are visible. Kwangmyung Electric produced a strong theme MFE, then opened a high-MAE drawdown path, making it local 4B-watch rather than durable Green. | True | True |
| R1L16_C02_KWANGMYUNG_20240405_T1 | 017040 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_false_positive | False | False |
| TRG_R5L79-C18-017810-PULMUONE-GLOBAL-FOOD-CHANNEL-REORDER | 017810 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | C18 should preserve food-channel positives when overseas/online channel reorder, product mix, volume, revenue conversion and margin bridge are visible. Pulmuone produced high MFE with very bounded entry-basis MAE, but post-peak drawdown requires lifecycle management. | True | True |
| TRG_R5L75-C18-017810-PULMUONE-TOFU-HMR-US-CHANNEL-REORDER | 017810 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | C18 should include food names when overseas refrigerated channel reorder, utilization, logistics and margin conversion are visible. Pulmuone produced a clean multi-month MFE path, but later drawdown says the model needs lifecycle decay if reorder/margin evidence stalls. | True | True |
| R11L13_C31_UNISON_20220729_STAGE2A | 018000 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| TRG_R5L73-C18-018250-AEKYUNG-EXPORT-CHANNEL-ONE-CANDLE-FADE | 018250 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | C18 should not treat a short export/channel rally as durable Green when reorder, sell-through or margin evidence fails to refresh. Aekyung generated MFE but later opened deep MAE and drawdown. | True | True |
| TRG_R5L73-C18-018250-AEKYUNG-EXPORT-CHANNEL-ONE-CANDLE-FADE | 018250 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | C18 should not treat a short export/channel rally as durable Green when reorder, sell-through or margin evidence fails to refresh. Aekyung generated MFE but later opened deep MAE and drawdown. | True | True |
| R13L24_C20_004_T1_STAGE2_YELLOW | 018250 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | False | False |
| T_C20_VT_2023_08_14_STAGE2A | 018290 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_too_late | False | False |
| R5L17_T02_VT_STAGE2 | 018290 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_too_early | False | False |
| T_C20_VT_2023_09_19_GREEN | 018290 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_too_late | False | False |
| R13L24_C20_002_T2_STAGE3_GREEN_LATE | 018290 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_too_late | False | False |
| TR-R5L42-018290-GREEN-20240613 | 018290 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_too_late | False | False |
| T_VT_20240920_STAGE3_GREEN_LATE | 018290 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_too_late | False | False |
| T_C20_VT_2024_06_13_4B | 018290 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_4B_too_late | False | False |
| R13L13_X_T_VT_20240920_STAGE3_GREEN_LATE | 018290 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_too_late | False | False |
| T_VT_20240920_STAGE3_GREEN_LATE | 018290 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_too_late | False | False |
| R4L16_C15_018470_T1 | 018470 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_4B_too_late | False | False |
| R4L16_C15_018470_T1 | 018470 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_4B_too_late | False | False |
| R4L16_C15_018470_4B_OVERLAY_20210908 | 018470 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_4B_too_late | False | False |
| R4L16_C15_018470_4B_OVERLAY_20210908 | 018470 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_4B_too_late | False | False |
| TR-C29-HANON-S2-20230125 | 018880 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| TR_R9L10_018880_S2_20230412 | 018880 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| T_R9L11_018880_STAGE2 | 018880 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| TRG_R9L76-C29-018880-HANON-SYSTEMS-EV-THERMAL-UTILIZATION-FADE | 018880 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should not treat EV thermal-management beta as durable Stage2 unless customer volume, platform program, utilization, pricing/mix and margin bridge are visible. Hanon Systems had limited MFE and then opened a high-MAE drawdown path. | True | True |
| TRG_R9L73-C29-018880-HANON-THERMAL-EV-BETA-LOCAL4B | 018880 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should not treat EV thermal-management or auto-parts theme beta as durable Stage2 when customer volume, pricing and margin conversion are weak. Hanon generated only small MFE and later severe MAE, making it a local 4B-watch / false Stage2 row. | True | True |
| TRG_R9L73-C29-018880-HANON-THERMAL-EV-BETA-LOCAL4B | 018880 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should not treat EV thermal-management or auto-parts theme beta as durable Stage2 when customer volume, pricing and margin conversion are weak. Hanon generated only small MFE and later severe MAE, making it a local 4B-watch / false Stage2 row. | True | True |
| TRG_R9L78-C29-018880-HANON-THERMAL-EV-PARTS-THEME-FADE | 018880 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should not treat thermal-management or EV-parts beta as durable Stage2 unless customer program, volume, pricing, utilization and margin bridge are visible. Hanon Systems had only small MFE and then a severe MAE drawdown path. | True | True |
| T_R9L11_018880_4C | 018880 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_4C_too_late | False | False |
| R13L11_REDTEAM__T_R9L11_018880_STAGE2 | 018880 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L11_REDTEAM__T_R9L11_018880_4C | 018880 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4C_too_late | False | False |
| C24-SHINPOONG-20210705-S2_FALSE | 019170 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_false_positive | False | False |
| R7L12-C24-019170-T1-PRE-READOUT-FALSE-STAGE2-20210625 | 019170 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_false_positive | False | False |
| R7L12-C24-019170-T2-HARD-4C-DATA-FAILURE-20210706 | 019170 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_4C_too_late | False | False |
| R13L12_FP_X11_019170_Stage4C_2021-07-06 | 019170 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_4C_too_late | False | False |
| R5L71-C19-003-S2 | 020000 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_false_positive | True | False |
| TRG_R5L76-C19-020000-HANDSOME-APPAREL-RETAIL-INVENTORY-BETA-FADE | 020000 | C19_BRAND_RETAIL_INVENTORY_MARGIN | C19 should not treat apparel retail or inventory-normalization beta as durable Stage2 unless sell-through, markdown control, channel productivity and margin bridge are visible. Handsome had a brief MFE but later faded into a lower range; share-count movement inside the window requires validation. | True | True |
| None | 020000 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | True | True |
| R13_CROSS_020000_2024-04-11_Stage4B-Local-DomesticFashionInventoryMargin | 020000 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | True | True |
| TRG_R3L75-C12-020150-LOTTE-ENERGY-MATERIALS-COPPER-FOIL-CONTRACT-BRIDGE | 020150 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | C12 should allow Stage2 when copper-foil customer contracts, delivery schedule, capacity utilization and margin bridge are explicit. Lotte Energy Materials produced high MFE with low entry-basis MAE, but later drawdown shows lifecycle local 4B is needed if customer call-off or margin evidence fades. | True | True |
| TRG_R3L81-C13-020150-LOTTE-ENERGY-MATERIALS-COPPERFOIL-UTILIZATION-RECOVERY | 020150 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | C13 can preserve copper-foil recovery positives when customer volume, utilization, IRA/AMPC economics and margin bridge are visible. Lotte Energy Materials had tradable MFE with bounded entry-basis MAE, but post-peak drawdown means bridge refresh is required. | True | True |
| TRG_R3L14_C13_LOTTEEM_20230726_STAGE2_CAPEX_CAPPED | 020150 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_false_positive | False | False |
| TRG-R3L15-C14-020150-STAGE2-WATCH-20240425 | 020150 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_4C_too_early | False | False |
| R13L15_X_TRIG_TRG-R3L15-C14-020150-STAGE2-WATCH-20240425 | 020150 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4C_too_early | False | False |
| TRG_R9L81-C29-020560-ASIANA-AIRLINE-MERGER-TRANSPORT-MARGIN-FADE | 020560 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should not treat airline merger/transport beta as durable volume-margin operating leverage unless passenger volume, yield, fuel-cost pass-through, integration path, revenue and margin bridge are visible. Asiana had early MFE, then a persistent high-MAE drawdown. The profile has a 2024-12-30 corporate-action candidate outside the selected 180D window, so extended-window ingestion needs validation. | True | True |
| TRG_R4L77-C15-021050-SEOWON-COPPER-ALLOY-SPREAD-THEME-FADE | 021050 | C15_MATERIAL_SPREAD_SUPERCYCLE | C15 should not treat copper alloy or nonferrous theme spikes as durable Stage2 unless order, volume, inventory and margin bridge are visible. Seowon produced high MFE but then leaked back into a broad range, making it a local 4B-watch row rather than durable Green. | True | True |
| TRG_R10L79-C30-021320-KCC-E&C-PF-BOUNDED-RISKWATCH-NO-FORCED4B | 021320 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should keep PF/orderbook monitoring active for bounded builders, but should not force local 4B or hard 4C when MAE is contained and no non-price refinancing or solvency break is confirmed. KCC E&C is a boundary row. | True | True |
| R10L12-C30-KCCCON-20240327-T1 | 021320 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive | False | False |
| TRG_R10L74-C30-021320-KCC-CONSTRUCTION-RISKWATCH-NO-HARD4C | 021320 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should not convert every regional-builder PF fear into full 4B or hard 4C when the price path has moderate MAE, tradable MFE and no confirmed non-price break. KCC Construction is a RiskWatch/no-hard-4C boundary row. | True | True |
| TRG_R10L74-C30-021320-KCC-CONSTRUCTION-RISKWATCH-NO-HARD4C | 021320 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should not convert every regional-builder PF fear into full 4B or hard 4C when the price path has moderate MAE, tradable MFE and no confirmed non-price break. KCC Construction is a RiskWatch/no-hard-4C boundary row. | True | True |
| R13L12_FP_X10_021320_Stage2-Actionable_2024-03-27 | 021320 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive | False | False |
| TRG_R5L81-C19-023530-LOTTE-SHOPPING-RETAIL-MARGIN-VALUEUP-LIFECYCLE | 023530 | C19_BRAND_RETAIL_INVENTORY_MARGIN | C19 should allow department-store/retail positives only when value-up or channel recovery maps to inventory turnover, cost control, revenue mix and margin bridge. Lotte Shopping had a tradable early MFE but later high MAE, so it is lifecycle-managed rather than durable Green. | True | True |
| TRG_R5L78-C19-023530-LOTTE-SHOPPING-RETAIL-INVENTORY-MARGIN-LIFECYCLE | 023530 | C19_BRAND_RETAIL_INVENTORY_MARGIN | C19 should allow large-cap retail inventory-normalization positives when channel productivity, inventory turnover, markdown discipline, cost control and margin bridge are visible. Lotte Shopping produced a meaningful MFE from a low-risk entry, but the later post-peak drawdown requires lifecycle local 4B if inventory/margin evidence fades. | True | True |
| TRG_R9L75-C29-023800-INZI-CONTROLS-THERMAL-MANAGEMENT-BETA-FADE | 023800 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should not treat thermal-management or cooling-system theme beta as durable Stage2 unless customer volume, OEM program, pricing/mix and margin bridge refreshes. Inzi Controls had a sharp tradable spike but later opened large MAE and drawdown. | True | True |
| TR_R11L11_HEUNGGU_STAGE2_2024_06_03 | 024060 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| R11L11_T_024060_20240603_Stage2_Event_Watch | 024060 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| TRG_R6L73-C21-024110-IBK-HIGH-DIVIDEND-PBR-ROE-BRIDGE | 024110 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | C21 should include slower high-dividend/value-up bank paths when dividend yield, low PBR, capital discipline and stable ROE support the rerating. IBK produced strong MFE with essentially no entry-basis MAE. | True | True |
| T_IBK_2025_04_25_STAGE2_ACTIONABLE | 024110 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_late | False | False |
| TRG_R6L73-C21-024110-IBK-HIGH-DIVIDEND-PBR-ROE-BRIDGE | 024110 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | C21 should include slower high-dividend/value-up bank paths when dividend yield, low PBR, capital discipline and stable ROE support the rerating. IBK produced strong MFE with essentially no entry-basis MAE. | True | True |
| R6L13_C21_IBK_T2_20240226 | 024110 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | False | False |
| TRG_R9L75-C29-024900-DY-DEOKYANG-BODY-BATTERY-HOUSING-BETA-FADE | 024900 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should not treat body-module, interior or battery-housing beta as durable Stage2 unless OEM volume, product mix, program award, pricing and margin bridge are visible. Deokyang Industrial produced a strong early MFE but then opened high MAE and a deep drawdown. | True | True |
| TRG_R4L79-C17-025000-KPX-CHEMICAL-POLYOL-SPREAD-DEFENSIVE-NO-STAGE2 | 025000 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | C17 should not force local 4B when a chemical name has bounded MAE and defensive cashflow, but it also should not mark Stage2 unless spread expansion, volume, utilization and margin bridge are visible. KPX Chemical is a low-volatility boundary row. | True | True |
| TRG_R4L82-C17-025000-KPX-CHEMICAL-POLYOL-SPREAD-BOUNDED | 025000 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | C17 should allow chemical spread recovery candidates only when input-cost pass-through, customer volume, utilization, pricing and margin bridge are visible. KPX Chemical had bounded MAE and mild MFE, so it is a RiskWatch/Stage2-Yellow candidate after source repair, not a forced 4B row. | True | True |
| TRG_R9L80-C29-025540-KET-AUTO-CONNECTOR-THEME-LOCAL4B | 025540 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should not treat auto connector/electronics theme beta as durable Stage2 unless customer program volume, connector content growth, utilization, pricing and margin bridge are visible. Korea Electric Terminal had modest MFE and later high MAE. | True | True |
| R4L16_C15_025820_T1 | 025820 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_missed_structural | False | False |
| R4L16_C15_025820_T1 | 025820 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_missed_structural | False | False |
| TRG_R4L74-C15-025820-IGU-COPPER-FABRICATOR-SPREAD-BRIDGE | 025820 | C15_MATERIAL_SPREAD_SUPERCYCLE | C15 should allow Stage2 when copper rally is tied to product-specific spread, inventory effect, export price and margin bridge. Igu Industry produced a strong copper-cycle MFE, but the late-2024 collapse requires local 4B-watch if spread/margin evidence stops refreshing. | True | True |
| TRG_R4L77-C15-025820-IGOO-COPPER-SPREAD-INVENTORY-MARGIN-LIFECYCLE | 025820 | C15_MATERIAL_SPREAD_SUPERCYCLE | C15 should allow nonferrous/copper processors when copper price/spread, inventory revaluation, volume and margin bridge are visible. Igoo Industry produced large MFE with controlled entry-basis MAE, but later drawdown requires lifecycle local 4B if spread/margin evidence fades. | True | True |
| TRG_R4L74-C15-025820-IGU-COPPER-FABRICATOR-SPREAD-BRIDGE | 025820 | C15_MATERIAL_SPREAD_SUPERCYCLE | C15 should allow Stage2 when copper rally is tied to product-specific spread, inventory effect, export price and margin bridge. Igu Industry produced a strong copper-cycle MFE, but the late-2024 collapse requires local 4B-watch if spread/margin evidence stops refreshing. | True | True |
| R4L15_C16_T001 | 025860 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_missed_structural | False | False |
| R13L15_X_TRIG_R4L15_C16_T001 | 025860 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_missed_structural | False | False |
| R10L13_C30_025950_T_STAGE2_20240327 | 025950 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive | False | False |
| R13L13_ACC_X11_025950_20240327 | 025950 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | False | False |
| R13L27_C16_027580_T1 | 027580 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_false_positive | False | False |
| R12L13_C31_027710_FEED_THEME_HIGH_MAE_T_STAGE2_20220224 | 027710 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| TRG_R12L81-C31-027710-FARMSTORY-FEED-FOOD-SECURITY-THEME-FADE | 027710 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should not treat feed/food-security policy beta as durable Stage2 unless direct feed/meat demand, input cost pass-through, customer volume, revenue and margin bridge are visible. FarmStory had almost no post-entry MFE and then a persistent MAE path. | True | True |
| R12L13_C31_027710_FEED_THEME_HIGH_MAE_T_4B_20220426 | 027710 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_4B_too_early | False | False |
| R13L13_X_R12L13_C31_027710_FEED_THEME_HIGH_MAE_T_STAGE2_20220224 | 027710 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R12L13_C31_027710_FEED_THEME_HIGH_MAE_T_STAGE2_20220224 | 027710 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L13_X_R12L13_C31_027710_FEED_THEME_HIGH_MAE_T_4B_20220426 | 027710 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_early | False | False |
| R12L13_C31_027710_FEED_THEME_HIGH_MAE_T_4B_20220426 | 027710 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_early | False | False |
| TRG_C05_028050_20230131_STAGE2_ACTIONABLE | 028050 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | current_profile_missed_structural_if_C05_has_no_runtime_weight | True | True |
| TRG_SAMSUNG_EA_2023_OVERSEAS_EPC_STAGE2_ACTIONABLE_2023_01_31 | 028050 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_too_late | False | False |
| TRG_SAMSUNG_EA_2023_STAGE3_GREEN_LATE_4B_WATCH_2023_07_31 | 028050 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_too_late | False | False |
| R11L13_C31_KVU_SCT_028260_STAGE2A_FALSE_20240226 | 028260 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| R7L13-C23-HLB-20240517-4C | 028300 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_4C_too_late | False | False |
| TRG_R7L10_HLB_2024-05-17_CRL_4C | 028300 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_4C_too_late_if_waiting_for_confirmed_financials | False | False |
| R7L46-HLB-20240517-4C | 028300 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_4C_too_late | False | False |
| T48_028300_20240517_4C_CRL | 028300 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_4C_too_late | False | False |
| R7L14-C23-028300-FDA-CRL-20240517 | 028300 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_4C_too_late | False | False |
| HLB_4C_CRL_2024_05_17 | 028300 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_4C_too_late | False | False |
| TRG_R7L10_HLB_2024-04-22_PDUFA_RUNUP | 028300 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive | False | False |
| R7L46-HLB-20240516-FPG | 028300 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive | False | False |
| TR_R7L10_028300_2024-04-30_PRE_PDUFA_EVENT_PREMIUM | 028300 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive | False | False |
| T-028300-2024-03-08-SPECULATIVE-PDUFA | 028300 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive | False | False |
| HLB_PRE_CRL_EXPECTATION_STRESS_2024_05_16 | 028300 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive | False | False |
| T48_028300_20240425_FALSE_GREEN_PDUFA_EXPECTATION | 028300 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive | False | False |
| T_HLB_20240430_PRE_PDUFA_FALSE_GREEN | 028300 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive | False | False |
| R7L13-C23-HLB-20240516-GREEN-FP | 028300 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive | False | False |
| R7L14-T006 | 028300 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive | False | False |
| R7L11-C23-028300-T1-pre-pdufa-false-green | 028300 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive | False | False |
| R7L11_T03_HLB_20240516_FALSE_GREEN_PRE_PDUFA_UNRESOLVED_REGULATORY_RISK | 028300 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive | False | False |
| R7L14-T006 | 028300 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive | False | False |
| T-C23-HLB-STAGE3Y-20240321 | 028300 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive | False | False |
| R7L12_C23_HLB_PRE_CRL_EXPECTATION_2024-05-14 | 028300 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive | False | False |
| T-C23-HLB-4C-20240517 | 028300 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_4C_too_late | False | False |
| R7L14-T007 | 028300 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_4C_too_late | False | False |
| R7L12_C23_HLB_4C_CRL_2024-05-17 | 028300 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_4C_too_late | False | False |
| R7L11_T03B_HLB_20240517_HARD_4C_CRL_REGULATORY_REJECTION | 028300 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_4C_too_late | False | False |
| R7L14-T007 | 028300 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_4C_too_late | False | False |
| C24-HLB-20240326-4B_PRECAP | 028300 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_4B_too_late | False | False |
| C24-HLB-20240517-4C | 028300 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_4B_too_late | False | False |
| R7L12-C24-028300-T1-PRE-EVENT-FALSE-GREEN-20240516 | 028300 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_false_positive | False | False |
| R7L13_C24_028300_2024-05-16_4B_RISK | 028300 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_false_positive | False | False |
| TRG_R7L16_028300_20240517_STAGE4C | 028300 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_4C_too_late | False | False |
| R7L13_C24_028300_2024-05-17_4C_CONFIRM | 028300 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_4C_too_late | False | False |
| TRG_R7L11_028300_4C_20240520 | 028300 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_4C_too_late | False | False |
| R13L13_X_R7L13-C23-HLB-20240517-4C | 028300 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4C_too_late | False | False |
| R13L14_X_TRIG_R7L14-C23-028300-FDA-CRL-20240517 | 028300 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4C_too_late | False | False |
| R7L13-C23-HLB-20240517-4C | 028300 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4C_too_late | False | False |
| R13L13_X_R7L13-C23-HLB-20240516-GREEN-FP | 028300 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R7L13-C23-HLB-20240516-GREEN-FP | 028300 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L15_X_TRIG_T-C23-HLB-STAGE3Y-20240321 | 028300 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L12_REDTEAM__R7L12_C23_HLB_PRE_CRL_EXPECTATION_2024-05-14 | 028300 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L15_X_TRIG_T-C23-HLB-4C-20240517 | 028300 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4C_too_late | False | False |
| R13L11_HIGHMAE_X04_028300_FALSEGREEN_20240516 | 028300 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | False | False |
| R13L14_G03_08_028300_R7L14-T006 | 028300 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | False | False |
| R13L14_G06_09_028300_R7L14-T007 | 028300 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_4C_too_late | False | False |
| R13L12_FP_X09_028300_Stage3-Green-candidate-false-positive_2024-05-16 | 028300 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive | False | False |
| R9L14_C29_PAN_2021_DRYBULK_4B_OVERLAY | 028670 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_4B_too_late | False | False |
| T_R9L13_028670_4B_20210629 | 028670 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_4B_too_late | False | False |
| R13L13_X_T_R9L13_028670_4B_20210629 | 028670 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late | False | False |
| T_R9L13_028670_4B_20210629 | 028670 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late | False | False |
| R6L15-C21-SAMCAR-20240202-S2A | 029780 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_missed_structural | False | False |
| R6L15-C21-SAMCAR-20240202-S2A | 029780 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_missed_structural | False | False |
| R13L15_X_TRIG_R6L15-C21-SAMCAR-20240202-S2A | 029780 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_missed_structural | False | False |
| TRG_R8L81-C26-030000-CHEIL-WORLDWIDE-AD-AGENCY-BOUNDED-RISKWATCH | 030000 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | C26 should not force stable large ad-agency rows into 4B when MAE is bounded and no client-budget or margin break is confirmed, but it also should not call durable Stage2 without verified ad spend recovery, client budget, operating leverage and margin bridge. | True | True |
| TRG_R6L77-C21-030210-DAOL-SECURITIES-BROKERAGE-VALUEUP-BETA-FADE | 030210 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | C21 should not treat brokerage/value-up beta as durable Stage2 unless ROE recovery, capital buffer, shareholder return, balance-sheet risk reduction and earnings bridge are visible. Daol Investment had only a small MFE, then drifted into a prolonged drawdown, making it a local 4B-watch boundary rather than a capital-return Green. | True | True |
| R8L12_C28_HANCOM_T1_STAGE2_ACTIONABLE_2023-11-20 | 030520 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_4B_too_late | False | False |
| R8L12_C28_HANCOM_T1_STAGE2_ACTIONABLE_2023-11-20 | 030520 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_4B_too_late | False | False |
| R8L10_C28_TRG_003A_HANCOM_STAGE2_ACTIONABLE_2024_01_10 | 030520 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive | False | False |
| R8L12_C28_T008 | 030520 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive | False | False |
| R8L12_C28_HANCOM_GREEN_20240110 | 030520 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_too_late | False | False |
| R8L12_C28_HANCOM_T2_4B_OVERLAY_2024-01-22 | 030520 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_4B_too_late | False | False |
| TRG_R2L76-C10-031980-PSK-HOLDINGS-ADVANCED-PACKAGING-EQUIPMENT-CYCLE | 031980 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | C10 should allow equipment-cycle Stage2 when memory/advanced-package equipment demand connects to actual order, customer capacity, delivery and margin bridge. PSK Holdings produced high MFE with controlled entry-basis MAE; post-peak drawdown requires lifecycle local 4B if order/margin evidence fades. | True | True |
| TRG_R12L82-C31-032350-LOTTE-TOURISM-RESORT-VISA-VOLUME-MARGIN | 032350 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should allow tourism policy positives only when visa/reopening policy maps to inbound volume, casino drop, hotel occupancy, ADR, revenue conversion and margin bridge. Lotte Tour Development had moderate MFE with bounded MAE, but share-count validation is needed before runtime promotion. | True | True |
| R12_C31_TOUR_002_T1 | 032350 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_4B_too_late | False | False |
| TRG_R12L78-C31-032620-UBCARE-TELEMEDICINE-POLICY-DIRECT-DEMAND | 032620 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 can allow telemedicine/digital-health policy rows when policy relaxation maps to direct clinic/EMR platform usage, claim/workflow demand, paid usage, revenue conversion and margin bridge. UBCare produced a large MFE, but later drawdown means it cannot remain Green unless direct-demand and margin evidence refreshes. | True | True |
| TRG_R1L81-C04-032820-WOORITECH-NUCLEAR-CONTROL-SYSTEM-RS-SHARECOUNT | 032820 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | C04 should protect nuclear control-system positives when project/order evidence, customer quality, delivery schedule, revenue conversion and margin bridge are visible. Woori Technology produced very large MFE with nearly no early MAE, but share-count validation is required before runtime promotion. | True | True |
| TRG_R11L78-C04-032820-WOORI-TECH-NUCLEAR-IANDC-PROJECT-LIFECYCLE | 032820 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | C04 should protect nuclear control/I&C positives when project-policy demand maps to control-system order, customer/project visibility, delivery/revenue bridge and margin conversion. Woori Technology produced a strong MFE with almost no entry-basis MAE, but share-count movement requires validation. | True | True |
| TRG_R1L75-C04-032820-WOORI-TECH-NUCLEAR-CONTROL-SYSTEM-BRIDGE | 032820 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | C04 should include nuclear control/I&C suppliers when policy/project attention converts into project scope, order or customer validation. Woori Technology produced very high MFE and no entry-basis negative MAE, but share-count changes and later drawdown require validation and lifecycle local 4B. | True | True |
| R6L10-C21-SLIF-T01 | 032830 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_late | False | False |
| TRG_R6L78-C22-032830-SAMSUNG-LIFE-RATE-RESERVE-CAPITAL-RETURN | 032830 | C22_INSURANCE_RATE_CYCLE_RESERVE | C22 should allow life-insurance positives when rate cycle, CSM/reserve quality, capital buffer, dividend/buyback and shareholder-return bridge are visible. Samsung Life produced large MFE with almost no entry-basis MAE, but later drawdown requires lifecycle local 4B if reserve/capital-return evidence fades. | True | True |
| TRG_R6L80-C22-032830-SAMSUNG-LIFE-RATE-CYCLE-CAPITAL-RETURN | 032830 | C22_INSURANCE_RATE_CYCLE_RESERVE | C22 should preserve life-insurance positives when rate cycle, CSM/reserve quality, capital buffer, dividend/buyback policy and earnings durability are visible. Samsung Life produced large MFE with almost no entry-basis MAE, but later drawdown requires lifecycle monitoring. | True | True |
| R6L14_T01_SAMSUNGLIFE_20240202_STAGE2_ACTIONABLE_LIFE_CSM_KICS | 032830 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_too_late | False | False |
| TR-032830-20240227-S2A | 032830 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_too_early | False | False |
| TR-032830-20240227-S2A | 032830 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_too_early | False | False |
| R6L47_T02_032830_STAGE3_GREEN_RESERVE_BRIDGE | 032830 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_too_late | False | False |
| TR-032830-20240305-GREEN-COMP | 032830 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_too_early | False | False |
| TR-032830-20240305-GREEN-COMP | 032830 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_too_early | False | False |
| R13L17_C22_032830_SAMSUNG_LIFE_BLOWOFF_2024_T1 | 032830 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_4B_too_late | False | False |
| R13L14_X_TRIG_R6L14_T01_SAMSUNGLIFE_20240202_STAGE2_ACTIONABLE_LIFE_CSM_KICS | 032830 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_too_late | False | False |
| TRG_R12L78-C31-032850-BITCOMPUTER-TELEMEDICINE-IT-POLICY-THEME-FADE | 032850 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should not treat telemedicine or healthcare-IT policy beta as durable Stage2 unless policy event maps to direct installed-base demand, contract conversion, usage/revenue and margin evidence. BitComputer had an immediate MFE spike and then a long drawdown, making it local 4B rather than Green. | True | True |
| TRG_R1L76-C02-033100-JERYONG-TRANSFORMER-GRID-CAPEX-BACKLOG | 033100 | C02_POWER_GRID_DATACENTER_CAPEX | C02 should allow transformer suppliers when grid/datacenter capex converts into export order backlog, delivery slot, ASP and margin bridge. Jeryong Electric had extreme MFE and no entry-basis MAE, but later drawdown requires lifecycle local 4B if backlog/order evidence fades. | True | True |
| TRG_R9L74-C29-033530-SJG-SEJONG-HYDROGEN-EXHAUST-PARTS-BETA-FADE | 033530 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should not treat hydrogen/exhaust/auto-parts theme beta as durable Stage2 unless customer volume, OEM program, pricing or margin bridge is visible. SJG Sejong had a tradable spike but later MAE and post-peak drawdown opened. | True | True |
| TRG_R9L74-C29-033530-SJG-SEJONG-HYDROGEN-EXHAUST-PARTS-BETA-FADE | 033530 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should not treat hydrogen/exhaust/auto-parts theme beta as durable Stage2 unless customer volume, OEM program, pricing or margin bridge is visible. SJG Sejong had a tradable spike but later MAE and post-peak drawdown opened. | True | True |
| R13L14_X_TRIG_R12L14C32_033780_T_STAGE2_20221026 | 033780 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_too_early | False | False |
| R1L12_C04_034020_CZECH_NSSS_HIGH_MAE_STAGE2_ACTIONABLE | 034020 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_4B_too_early | False | False |
| T034020_STAGE2_20240717_CZ_PREFERRED_BIDDER | 034020 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_too_early | False | False |
| C04_DOOSAN_20240718_STAGE2_ACTIONABLE | 034020 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_too_early | False | False |
| TRG_R1L16_C04_034020_CZECH_PREF_HIGH_MAE | 034020 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_too_early | False | False |
| R1L12_C04_034020_CZECH_NSSS_HIGH_MAE_LOCAL_4B_OVERLAY | 034020 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_4B_too_early | False | False |
| C04_DOOSAN_20241031_PROCEDURAL_LEGAL_DELAY_WATCH | 034020 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_4C_too_early_if_hard_routed | False | False |
| TR_R13L29_DOOSANENER_STAGE2_20220310 | 034020 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| R11C31_034020_T1_STAGE2 | 034020 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_too_late | False | False |
| R11C31_034020_T1_STAGE2 | 034020 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_too_late | False | False |
| TR_R13L29_DOOSANENER_4B_20220311 | 034020 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_4B_too_early | False | False |
| R12L14C31_034230_T_STAGE2_20230810 | 034230 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| R12_C31_TOUR_004_T1 | 034230 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| R12L14C31_034230_T_4B_20230814 | 034230 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_4B_too_late | False | False |
| R13L14_X_TRIG_R12L14C31_034230_T_STAGE2_20230810 | 034230 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L14_X_TRIG_R12L14C31_034230_T_4B_20230814 | 034230 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late | False | False |
| R1L15_C05_SSGC_STAGE2_DIRECT_SUPPORT_CONTROL_20240327 | 034300 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | current_profile_missed_structural | False | False |
| TRG_R10L76-C30-034300-SHINSEGAE-CONSTRUCTION-POST-CA-SUPPORT-NO-HARD4C | 034300 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should not convert every PF fear or construction liquidity story into hard 4C when post-CA price action recovers and stabilizes. Shinsegae Construction requires post-corporate-action validation, but the post-CA window is a no-hard-4C boundary unless non-price solvency/refinancing break is confirmed. | True | True |
| R10L11_T02_SHINSEGAE_STAGE2_PARENT_SUPPORT | 034300 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_missed_structural | False | False |
| TRG_R10L73-C30-034300-SHINSEGAE-CONSTRUCTION-PF-RECAP-BUFFER | 034300 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should not convert every PF-liquidity headline into hard 4C when parent recapitalization, tender/de-listing path, or capital buffer changes the equity path. The stock-web path had large MFE after the recapitalization candidate, so this is a no-hard-4C buffer row, not a hard break row. | True | True |
| TRG_R10L73-C30-034300-SHINSEGAE-CONSTRUCTION-PF-RECAP-BUFFER | 034300 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should not convert every PF-liquidity headline into hard 4C when parent recapitalization, tender/de-listing path, or capital buffer changes the equity path. The stock-web path had large MFE after the recapitalization candidate, so this is a no-hard-4C buffer row, not a hard break row. | True | True |
| TR-C30-034300-S2WATCH | 034300 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive | False | False |
| TR-C30-034300-S2WATCH | 034300 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive | False | False |
| R13L15_X_TRIG_R1L15_C05_SSGC_STAGE2_DIRECT_SUPPORT_CONTROL_20240327 | 034300 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_missed_structural | False | False |
| TRG_R11L82-C32-034730-SK-HOLDCO-VALUEUP-SHARECOUNT-WHIPSAW | 034730 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should not treat holding-company value-up or control-discount beta as durable Stage2 unless event mechanics, asset/NAV bridge, capital allocation, shareholder process, timing and downside cap are visible. SK had early MFE but then a deep MAE path and stock-web share-count movement, so validation is mandatory. | True | True |
| R12L14C31_035250_T_STAGE2_20220418 | 035250 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| R13L14_X_TRIG_R12L14C31_035250_T_STAGE2_20220418 | 035250 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| TRG_NAVER_2020Q1_STAGE2_ACTIONABLE_2020_04_27 | 035420 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_too_late | False | False |
| TRG_C26_NAVER_2020_STAGE2_ACTIONABLE | 035420 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_too_late | False | False |
| TRG_C26_NAVER_2023_11_06_STAGE2A | 035420 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_too_early | False | False |
| R8L11_C26_NAVER_T1_STAGE2_EARNINGS_2024-05-03 | 035420 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| R8L11_C26_NAVER_T1_STAGE2_EARNINGS_2024-05-03 | 035420 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| R8L12_C26_TRG_005A_NAVER_STAGE2_EVENT_ONLY_POSHMARK_2022_10_04 | 035420 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| TR_NAVER_20200710_GREEN | 035420 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_too_late | False | False |
| R8L12_C26_TRG_001B_NAVER_STAGE3_GREEN_2021_03_18 | 035420 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_too_late | False | False |
| C26_NAVER_T2_GREEN_20210623 | 035420 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_too_late | False | False |
| R8L13_C26_NAVER_GREEN_2024-01-10 | 035420 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_too_late | False | False |
| TRG_C26_NAVER_2021_STAGE3_YELLOW_COMPARISON | 035420 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_too_late | False | False |
| R13L11_REDTEAM__R8L11_C26_NAVER_T1_STAGE2_EARNINGS_2024-05-03 | 035420 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L15_X_TRIG_TR_NAVER_20200710_GREEN | 035420 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_too_late | False | False |
| TR_KAKAO_20210908_4B | 035720 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_4B_too_late | False | False |
| TRG_C26_KAKAO_2021_4B_REGULATORY_OVERLAY | 035720 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_4B_too_late | False | False |
| C26_KAKAO_T1_4C_20210908 | 035720 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_4C_too_late | False | False |
| TRG_KAKAO_2020Q1_STAGE2_ACTIONABLE_2020_05_08 | 035720 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_too_late | False | False |
| TRG_C26_KAKAO_2021_STAGE2_ACTIONABLE | 035720 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_4B_too_late | False | False |
| KAKAO_STAGE2_Q3_RECOVERY_GOV_OVERHANG_20231109 | 035720 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| TRG_C26_KAKAO_2023_11_10_STAGE2A | 035720 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| TR_KAKAO_20210624_GREEN | 035720 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| R8L13_C26_KAKAO_GREEN_2024-01-11 | 035720 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_too_late | False | False |
| KAKAO_4B_VALUATION_GOVERNANCE_CAP_20240111 | 035720 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_4B_too_late | False | False |
| R8L11_C26_KAKAO_T1_REGULATORY_4C_2021-09-08 | 035720 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_4C_too_late | False | False |
| R8L11_C26_KAKAO_T1_REGULATORY_4C_2021-09-08 | 035720 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_4C_too_late | False | False |
| R8L12_C26_TRG_004A_KAKAO_4C_REGULATORY_BREAK_2021_09_09 | 035720 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_4C_too_late | False | False |
| R13L15_X_TRIG_TR_KAKAO_20210908_4B | 035720 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late | False | False |
| R13L15_X_TRIG_TR_KAKAO_20210624_GREEN | 035720 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R8L11_C27_TRG_005A_CJENM_STAGE2_WATCH_2021_09_23 | 035760 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_4B_too_late | False | False |
| TRG_R10L76-C30-035890-SEOHEE-CONSTRUCTION-ORDERBOOK-BUFFER-NO-HARD4C | 035890 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should keep PF/orderbook RiskWatch active for builders, but bounded MAE and recovery rows should not be escalated into hard 4C. Seohee Construction showed a low-MAE recovery path; without non-price PF/refinancing or solvency break it should remain RiskWatch/no-hard-4C. | True | True |
| R10L12-C30-SEOHEE-20240327-T1 | 035890 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_missed_structural | False | False |
| R10L15_T01_SEOHEE_STAGE2_H1_SURVIVOR_MARGIN_REPAIR | 035890 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_missed_structural | False | False |
| R13L15_X_TRIG_R10L15_T01_SEOHEE_STAGE2_H1_SURVIVOR_MARGIN_REPAIR | 035890 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_missed_structural | False | False |
| JYP_STAGE2_20210517 | 035900 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_too_late | False | False |
| R8L15_C27_JYP_T1_STAGE2_ACTIONABLE | 035900 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_too_late | False | False |
| T_C27_JYP_2023_STAGE2_20230113 | 035900 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_too_late | False | False |
| R8L10_C27_JYP_T1_STAGE2_ACTIONABLE | 035900 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_too_late | False | False |
| R8L11-C27-JYP-T1 | 035900 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_too_late | False | False |
| JYP_STAGE3_20211020 | 035900 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_too_late | False | False |
| R8L15_C27_JYP_T2_STAGE3_GREEN | 035900 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_too_late | False | False |
| T_C27_JYP_2023_GREEN_20230516 | 035900 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_too_late | False | False |
| C27_036420_20211118_4B_EVENT_CAP | 036420 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_4B_too_late | False | False |
| C27_036420_20211123_4C_EVENT_REVERSAL | 036420 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_4C_too_late | False | False |
| TR_R11L13_KOGAS_POLICY_STAGE2A_20240603 | 036460 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| R11L11_T_036460_20240603_Stage2_Event_Watch | 036460 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| R11C31_036460_T1_STAGE2 | 036460 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| R11C31_036460_T1_STAGE2 | 036460 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| TR_R11L13_KOGAS_4B_PRICE_20240620 | 036460 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_4B_too_late | False | False |
| R13L11_REDTEAM__R11L11_T_036460_20240603_Stage2_Event_Watch | 036460 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| TRG_R12L72-C32-036560-YOUNGPOONG-PRECISION-TENDER-BATTLE-CAP | 036560 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 can allow Stage2 when a tender/control battle has explicit tender price and strategic control context, but extreme post-peak drawdown after the tender window requires local 4B-watch. Runtime must separate tender-cap math from open-ended governance rerating. | True | True |
| TRG_KZP_20241011_TENDER_RAISE_COUNTEREXAMPLE | 036560 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive | False | False |
| TRG_R12L72-C32-036560-YOUNGPOONG-PRECISION-TENDER-BATTLE-CAP | 036560 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 can allow Stage2 when a tender/control battle has explicit tender price and strategic control context, but extreme post-peak drawdown after the tender window requires local 4B-watch. Runtime must separate tender-cap math from open-ended governance rerating. | True | True |
| TRG_R11L80-C32-036560-YOUNGPOONG-PRECISION-TENDER-BATTLE-CAP | 036560 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should allow tender-battle positives only when tender price, acceptance window, ownership structure, free-float and event-end mechanics are explicit. Young Poong Precision/KZ Precision produced enormous event MFE, then the post-event path required local 4B discipline. | True | True |
| TRG_R12L75-C32-036560-YP-PRECISION-TENDER-CONTROL-PREMIUM-LIFECYCLE | 036560 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should allow a tender/control-premium lifecycle candidate when the listed company is a direct economic beneficiary of tender terms, control dispute or stake economics. Young Poong Precision/KZ Precision produced very large MFE, but post-tender drawdown means lifecycle local 4B is mandatory once tender/control-premium evidence fades. | True | True |
| T-C19-036620-2024-02-23-4B | 036620 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_4B_too_early | False | False |
| T-C19-036620-2023-05-15-S2A | 036620 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_missed_structural | False | False |
| T_C19_GAMSUNG_2023Q1_STAGE2_ACTIONABLE | 036620 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_missed_structural | False | False |
| TRG-R13L42-036620-S2A-20240222 | 036620 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_too_late | False | False |
| R13L45_036620_STAGE2_2024-02-22 | 036620 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_too_late | False | False |
| R13L45_036620_STAGE3_GREEN_2024-05-21 | 036620 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_too_late | False | False |
| TRG-R13L42-036620-GREEN-20240523 | 036620 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_too_late | False | False |
| TRG_R2L74-C07-036810-FST-EUV-CHILLER-ANCILLARY-EQUIPMENT-RS | 036810 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | C07 can include ancillary equipment when relative strength is tied to customer adoption, capex timing and margin conversion. FST had strong early MFE, but the later collapse shows that price strength must decay into local 4B if order/customer bridge evidence fails to refresh. | True | True |
| TRG_R2L74-C07-036810-FST-EUV-CHILLER-ANCILLARY-EQUIPMENT-RS | 036810 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | C07 can include ancillary equipment when relative strength is tied to customer adoption, capex timing and margin conversion. FST had strong early MFE, but the later collapse shows that price strength must decay into local 4B if order/customer bridge evidence fails to refresh. | True | True |
| TR_R4L71_C16_036830_S2A_20190701 | 036830 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_missed_structural | False | False |
| TRG_R2L82-C09-036930-JUSUNG-ALD-EQUIPMENT-VALUATION-BLOWOFF-SHARECOUNT | 036930 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | C09 should not treat ALD/deposition equipment theme beta as durable Stage2 unless named customer order, delivery schedule, backlog conversion, revenue and margin bridge are visible. Jusung produced a fast spike and then deep MAE; the 2024 shard also shows share-count change, so validation is required. | True | True |
| TRG_R2L79-C09-036930-JUSUNG-ADVANCED-EQUIPMENT-THEME-BLOWOFF-FADE | 036930 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | C09 should not treat advanced deposition/equipment theme beta as durable Stage2 unless customer order, backlog conversion, delivery, customer capacity and margin bridge refreshes. Jusung Engineering had a tradable MFE, then opened a high-MAE drawdown path. | True | True |
| None | 036930 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_error_if_advanced_equipment_label_is_allowed_to_substitute_for_order_backlog | False | False |
| TRG-R2L11-C10-JUSUNG-20230324 | 036930 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_too_early | False | False |
| TRG_R2L76-C10-036930-JUSUNG-EQUIPMENT-CYCLE-BETA-FADE | 036930 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | C10 should not treat generic equipment-cycle or memory recovery beta as durable Stage2 unless customer order, delivery, capex conversion and margin evidence refreshes. Jusung Engineering produced only limited MFE and then high MAE; share-count movement inside the window requires validation. | True | True |
| None | 036930 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | None | True | True |
| R13_CROSS_036930_2024-02-28_Stage2-FalsePositive_/_Stage4B-Local-PriceOnly | 036930 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | None | True | True |
| R2L16_C10_036930_STAGE2WATCH_2024-02-28 | 036930 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_false_positive | False | False |
| None | 036930 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_green_too_loose_if_valuation_beta_counts_as_visibility | False | False |
| T_R2L15_039030_STAGE2A_20240119 | 039030 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_too_late | False | False |
| R13L13_C09_039030_S2A_2024-01-19 | 039030 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_4B_too_late | False | False |
| T_R2L15_039030_LATE_GREEN_20240412 | 039030 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_4B_too_late | False | False |
| R13L13_C09_039030_4B_2024-04-12 | 039030 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_4B_too_late | False | False |
| R13L15_T_R2L15_039030_LATE_GREEN_20240412 | 039030 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late | False | False |
| R12_C31_TOUR_001_T1 | 039130 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_too_early | False | False |
| TRG_R12L82-C31-039130-HANATOUR-TRAVEL-VISA-THEME-FADE | 039130 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should not treat tourism/visa reopening beta as durable Stage2 unless package bookings, air-seat supply, ASP, commission take-rate, revenue and margin bridge are visible. Hanatour had modest early MFE and then high-MAE fade. | True | True |
| R12L14C31_039130_T_4B_20230302 | 039130 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_4B_too_late | False | False |
| R13L14_X_TRIG_R12L14C31_039130_T_4B_20230302 | 039130 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late | False | False |
| R7L11_T02_OSCOTEC_20240820_STAGE2_APPROVAL_CO_DEVELOPER_HIGH_MAE | 039200 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive | False | False |
| R7L12_C23_039200_2024-08-21_STAGE2A | 039200 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive | False | False |
| TRG_R13L32_039200_STAGE2_20200921 | 039200 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_correct | True | False |
| R7L12-C24-039200-T1-MARIPOSA-STAGE2A-20231023 | 039200 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_missed_structural | False | False |
| R7L27-T003 | 039200 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_too_late | False | False |
| R7L27-T003 | 039200 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_too_late | False | False |
| TRG_R7L16_039200_20240220_STAGE2_ACTIONABLE | 039200 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_missed_structural | False | False |
| R7L12-C24-039200-T2-4B-TRIAL-DATA-RERATING-20240716 | 039200 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_4B_too_late | False | False |
| TRG_R13L32_039200_4C_20210107 | 039200 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_4C_too_late | True | False |
| R2L13_C07_039440_STAGE2WATCH_20240213 | 039440 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_false_positive | False | False |
| TRG_R6L81-C21-039490-KIWOOM-BROKERAGE-TRADING-VOLUME-CAPITAL-RETURN | 039490 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | C21 should allow brokerage platform positives when market turnover, customer asset quality, retail brokerage, credit balance, capital return and earnings bridge are visible. Kiwoom produced a very large MFE with controlled entry-basis MAE, but stock-web share count changes need validation. | True | True |
| C21-BROKER-KIWOOM-S2A-20240201 | 039490 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_missed_structural | False | False |
| R6L16_T_KIWOOM_BROKERAGE_BETA_20240226_REP | 039490 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_4B_too_late | False | False |
| R6L16_T_KIWOOM_4B_20240716 | 039490 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_4B_too_late | False | False |
| TRG_R11L74-C31-039610-HWASUNG-VALVE-GAS-POLICY-CONTRACT-BRIDGE | 039610 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 can allow a policy-event lifecycle candidate when a valve or pipeline-infra name later connects to named procurement, order, EPC, utility or offshore infrastructure bridge. Hwasung Valve had a large MFE and later secondary peak, but still needs source repair and lifecycle local 4B after the peak. | True | True |
| TRG_R11L74-C31-039610-HWASUNG-VALVE-GAS-POLICY-CONTRACT-BRIDGE | 039610 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 can allow a policy-event lifecycle candidate when a valve or pipeline-infra name later connects to named procurement, order, EPC, utility or offshore infrastructure bridge. Hwasung Valve had a large MFE and later secondary peak, but still needs source repair and lifecycle local 4B after the peak. | True | True |
| TRG_R11L76-C31-039610-HWASEONG-VALVE-EASTSEA-GAS-POLICY-LIFECYCLE | 039610 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 can allow a policy-event lifecycle candidate when a gas-field/resource-development policy shock maps to a direct valve/pipeline beneficiary and then to actual order, project schedule, revenue and margin bridge. Hwaseong Valve produced large MFE, but post-peak drawdown requires lifecycle local 4B if the policy-to-order bridge fades. | True | True |
| TR_R11L11_HSVALVE_STAGE2_2024_06_03 | 039610 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_too_late | False | False |
| R13L11_HIGHMAE_X07_039610_STAGE2WATCH_20240604 | 039610 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_too_late_for_watch_but_not_green | False | False |
| R7L10_C25_DIO_2023_STAGE3Y | 039840 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive | False | False |
| R12L13_C32_YTN_STAGE2_2023_10_24 | 040300 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive | False | False |
| TR_YTN_EUGENE_20231024_STAGE2A | 040300 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive | False | False |
| R12L15_TR_YTN_STAGE2_20231024 | 040300 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive | False | False |
| T_C32_040300_20230308_STAGE2_EVENT_RUMOR | 040300 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive | False | False |
| TRG_R12L74-C32-040300-YTN-PRIVATIZATION-CONTROL-SALE-FADE | 040300 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should not treat privatization or control-sale approval as durable Stage2 unless minority tender economics, closing certainty, capital policy or earnings bridge is explicit. YTN had a short control-sale pop but then suffered high MAE and post-peak drawdown. | True | True |
| TRG_R12L74-C32-040300-YTN-PRIVATIZATION-CONTROL-SALE-FADE | 040300 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should not treat privatization or control-sale approval as durable Stage2 unless minority tender economics, closing certainty, capital policy or earnings bridge is explicit. YTN had a short control-sale pop but then suffered high MAE and post-peak drawdown. | True | True |
| R13L15_X_TRIG_R12L15_TR_YTN_STAGE2_20231024 | 040300 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| SM_EVENT_20230210 | 041510 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_false_positive | False | False |
| R8L14_C27_SM_T1_STAGE2A_20230413 | 041510 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_too_late | False | False |
| R8L11_C27_TRG_003A_SM_STAGE2_EVENT_2023_02_10 | 041510 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_false_positive | False | False |
| R12L11C32_041510_T2_KAKAO_150K_TENDER_CAP_4B | 041510 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_4B_too_late | False | False |
| TR_C32_041510_4B_2023-03-08 | 041510 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_4B_too_late | False | False |
| TRG-C32-SM-20230210-STAGE2A | 041510 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_missed_structural | False | False |
| R11L12_C32_SM_2023_T1 | 041510 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_4B_too_late | False | False |
| R12L11C32_041510_SM_HYBE_KAKAO_TENDER_BATTLE_T1_STAGE2_ACTIONABLE | 041510 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_4B_too_late | False | False |
| R12L15_TR_SM_STAGE2_20230210 | 041510 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_too_late | False | False |
| TR_C32_041510_STAGE2_2023-02-10 | 041510 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive | False | False |
| R12L10C32_SM_T1_STAGE2_EVENT_2023_02_10 | 041510 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive | False | False |
| TR_R11L14_SM_HYBE_TENDER_STAGE2A_20230210 | 041510 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_too_late | False | False |
| T_C32_041510_20230307_STAGE2_CAP_GUARD | 041510 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive | False | False |
| R13L15_X_TRIG_R12L15_TR_SM_STAGE2_20230210 | 041510 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_too_late | False | False |
| R13L14_X_TRIG_R8L14_C27_SM_T1_STAGE2A_20230413 | 041510 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_too_late | False | False |
| TRG_R7L82-C25-041830-INBODY-DIAGNOSTIC-DEVICE-EXPORT-BOUNDED | 041830 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | C25 should allow bounded diagnostic-device export positives only when export channel, hospital/fitness/clinic reorder, reimbursement or distributor channel quality, revenue conversion and margin bridge are visible. InBody had moderate MFE with bounded MAE, so it should be RiskWatch/Stage2-Yellow after source repair, not forced 4B. | True | True |
| T-041830-2023-02-28-S2A | 041830 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive | False | False |
| T-041830-2023-02-28-S2A | 041830 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive | False | False |
| TRG_C26_CAFE24_2024_06_20_4B | 042000 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_4B_too_late | False | False |
| TRG_C26_CAFE24_2023_12_06_STAGE2A | 042000 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_missed_structural | False | False |
| R13L54_C28_042510_4C_20221013 | 042510 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_4C_too_late | False | False |
| R2L13_C07_042700_STAGE2A_20230925 | 042700 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_too_late | False | False |
| R13L12_T001_042700_STAGE2 | 042700 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_too_late | False | False |
| R2L12_T01_HANMI_STAGE2_TCBONDER_ORDER_RS | 042700 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_too_late | False | False |
| R13L12_T002_042700_GREEN_LATE | 042700 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_too_late | False | False |
| R2L14_C09_042700_HANMI_4B_VALUATION_BLOWOFF | 042700 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_4B_too_late | False | False |
| R13L14_X_TRIG_R2L14_C09_042700_HANMI_4B_VALUATION_BLOWOFF | 042700 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late | False | False |
| TRG_R7L82-C25-043150-VATECH-DENTAL-IMAGING-EXPORT-FADE | 043150 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | C25 should not treat dental-imaging device export/reimbursement theme beta as durable Stage2 unless distributor channel order, dental clinic demand, reimbursement or capex cycle, revenue conversion and margin bridge are visible. Vatech had almost no forward MFE and a persistent MAE path. | True | True |
| TRG_R7L77-C25-043150-VATECH-DENTAL-IMAGING-EXPORT-BETA-FADE | 043150 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | C25 should not treat dental imaging/export-device beta as durable Stage2 unless export channel reorder, installed-base utilization, distributor inventory and margin bridge are visible. Vatech failed to generate meaningful MFE and then drifted lower, so it is a no-durable-Green/local-4B boundary. | True | True |
| None | 043150 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | None | True | True |
| R13_CROSS_043150_2024-02-01_Stage4B-Local-DentalImagingExportWeakness | 043150 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | None | True | True |
| TR_R9L31_C29_044450_STAGE2A_20210416 | 044450 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_too_early | False | False |
| R11L13_C31_045060_20200220_4B | 045060 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_4B_too_late | True | False |
| R11L13_C31_045060_20200120_T1 | 045060 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | True | False |
| R12L14_C31_045060_STAGE2WATCH_20200120 | 045060 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| R13L13_X_R11L13_C31_045060_20200220_4B | 045060 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late | False | False |
| R11L13_C31_045060_20200220_4B | 045060 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late | False | False |
| R13L13_X_R11L13_C31_045060_20200120_T1 | 045060 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R11L13_C31_045060_20200120_T1 | 045060 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| TRG_R1L81-C04-046120-ORBITECH-NUCLEAR-INSPECTION-THEME-FADE | 046120 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | C04 should not treat nuclear inspection/radiation-safety theme beta as durable Stage2 unless inspection backlog, project order, customer quality, revenue and margin bridge are visible. Orbitech had only small MFE and then a deep MAE path. | True | True |
| TRG_R11L78-C04-046120-ORBITEC-NUCLEAR-INSPECTION-THEME-DELAY-FADE | 046120 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | C04 should not treat nuclear-inspection/radiation policy beta as durable Stage2 unless inspection work, named project, regulatory path, order backlog and margin bridge are visible. Orbitec had limited MFE and then a deep drawdown, making it local 4B-watch rather than durable Green. | True | True |
| TRG_C05_047040_20230131_STAGE2_FALSE_POSITIVE | 047040 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | current_profile_false_positive_if_order_headline_scored_without_margin_bridge | True | True |
| R1L11_C05_047040_STAGE2WATCH_20240131 | 047040 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | current_profile_false_positive | False | False |
| TRG_R10L81-C30-047040-DAEWOO-E&C-BOUNDED-BUILDER-NO-FORCED4B | 047040 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should keep PF/orderbook monitoring active for bounded large builders, but should not force local 4B or hard 4C when MAE is contained and no non-price refinancing, liquidity or solvency break is confirmed. | True | True |
| TRG_R10L77-C30-047040-DAEWOO-E&C-LARGECAP-PF-RISKWATCH-NO-HARD4C | 047040 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should keep PF/orderbook RiskWatch active for large builders, but bounded MAE and recovery/sideways price action should not become hard 4C without refinancing, impairment, covenant, auditor/control or solvency break evidence. Daewoo E&C is a no-hard-4C boundary row. | True | True |
| R10L11_T01_DAEWOO_STAGE2_POLICY_BACKSTOP | 047040 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_missed_structural | False | False |
| TRG_R10L73-C30-047040-DAEWOO-LARGE-BUILDER-BUFFER-NOFULL4B | 047040 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should distinguish large-builder PF fear from a balance-sheet break. 대우건설 had bounded MAE and later tradable MFE, so it should remain RiskWatch/no-full-4B unless explicit impairment/refinancing/default evidence appears. | True | True |
| TRG_R10L73-C30-047040-DAEWOO-LARGE-BUILDER-BUFFER-NOFULL4B | 047040 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30 should distinguish large-builder PF fear from a balance-sheet break. 대우건설 had bounded MAE and later tradable MFE, so it should remain RiskWatch/no-full-4B unless explicit impairment/refinancing/default evidence appears. | True | True |
| TRG_R10L12_047040_20221031_SECTOR_PF_PANIC_COUNTEREXAMPLE | 047040 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive | False | False |
| TRG_R10L12_047040_20221031_SECTOR_PF_PANIC_COUNTEREXAMPLE | 047040 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive | False | False |
| R4L15_C16_T002 | 047400 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_false_positive | False | False |
| R13L27_C16_047400_T1 | 047400 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_false_positive | False | False |
| R13L15_X_TRIG_R4L15_C16_T002 | 047400 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| TRG_R8L75-C28-047560-ESTSOFT-AI-AVATAR-SOFTWARE-THEME-SPIKE-FADE | 047560 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | C28 should not treat AI software/avatar headline MFE as durable Stage2 unless enterprise contract retention, paid seat expansion, ARR/license revenue or margin bridge is visible. ESTsoft produced an enormous MFE, but later drawdown shows that theme-spike winners need lifecycle local 4B when bridge evidence fades. | True | True |
| R8L12_C28_ESTSOFT_AI_HYPE_20240108 | 047560 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive | False | False |
| R1L13_C03_047810_STAGE2WATCH_20220720 | 047810 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_false_positive | False | False |
| R13L59-T004 | 047810 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_false_positive | False | False |
| R1L11_T03_KAI_STAGE2_FA50_POLAND_CONTRACT | 047810 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_false_positive | False | False |
| R1L14-C03-KAI-20220916-STAGE3FALSE | 047810 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_false_positive | False | False |
| R1L11_T03B_KAI_4C_HIGH_MAE_GUARD | 047810 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_4C_too_late | False | False |
| R13L11_REDTEAM__R1L11_T03_KAI_STAGE2_FA50_POLAND_CONTRACT | 047810 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L11_REDTEAM__R1L11_T03B_KAI_4C_HIGH_MAE_GUARD | 047810 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4C_too_late | False | False |
| TRG_R11L73-C31-051600-KEPCO-KPS-CZECH-NUCLEAR-SERVICE-PROXY-RISKWATCH | 051600 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should flag nuclear service proxies as RiskWatch unless service scope, O&M participation, or backlog bridge is verified. KEPCO KPS had bounded MAE and later recovery, so it should not become full 4B or hard 4C from the policy headline alone. | False | True |
| TRG_R11L73-C31-051600-KEPCO-KPS-CZECH-NUCLEAR-SERVICE-PROXY-RISKWATCH | 051600 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should flag nuclear service proxies as RiskWatch unless service scope, O&M participation, or backlog bridge is verified. KEPCO KPS had bounded MAE and later recovery, so it should not become full 4B or hard 4C from the policy headline alone. | False | True |
| R5L13_C20_051900_20211027_4C | 051900 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | False | False |
| R5L13_C20_051900_20220110_4C_CONFIRM | 051900 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_4C_too_late | False | False |
| TRG_R5L80-C20-051900-LG-HH-CHINA-BRAND-RECOVERY-BOUNDARY | 051900 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | C20 should not force bounded large-cap China beauty recovery rows into 4B when MAE is controlled, but it also should not mark durable Stage2 without sell-through, channel inventory, brand mix, revenue and margin bridge. LG H&H is a bounded no-forced-4B boundary. | True | True |
| R5L17_T04_LGHNH_REOPEN_FALSE | 051900 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | False | False |
| R5L11-C20-LGHNH-STAGE2A-20220128 | 051900 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | False | False |
| T_LGHNH_20220128_FALSE_STAGE2 | 051900 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | False | False |
| T_C20_LGHH_2022_REOPENING_FALSE_POSITIVE | 051900 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | False | False |
| R5L34_C20_051900_T_STAGE2_2024_04_26 | 051900 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | False | False |
| T_C20_LGHH_20240510_WATCH | 051900 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | False | False |
| R5L10_C20_LGHNH_T2_20210624 | 051900 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | False | False |
| TRG_R5L11_C20_051900_LGHNH_REOPENING_FALSE_20240510_Stage3_Yellow | 051900 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | False | False |
| R5L34_C20_051900_T_4B_2024_05_23 | 051900 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_4B_too_late | False | False |
| R5L11-C20-LGHNH-4C-20220314 | 051900 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_4C_too_late | False | False |
| T_LGHNH_20220512_4C_THESIS_BREAK | 051900 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_4C_too_late | False | False |
| R13L13_X_T_LGHNH_20220128_FALSE_STAGE2 | 051900 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| T_LGHNH_20220128_FALSE_STAGE2 | 051900 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L10_X04_051900_Stage2-candidate-rejected | 051900 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L13_X_T_LGHNH_20220512_4C_THESIS_BREAK | 051900 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4C_too_late | False | False |
| T_LGHNH_20220512_4C_THESIS_BREAK | 051900 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4C_too_late | False | False |
| R13L13_ACC_X06_051900_20211027 | 051900 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | False | False |
| TRG-R3L12-051910-STAGE2A-20240207 | 051910 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_false_positive | False | False |
| TRG_R3L81-C13-051910-LG-CHEM-CATHODE-AMPC-IRA-THEME-FADE | 051910 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | C13 should not treat cathode/IRA/AMPC policy beta as durable Stage2 unless JV utilization, customer volume, subsidy economics, revenue conversion and margin bridge are visible. LG Chem had an early MFE but then a severe high-MAE drawdown path. | True | True |
| TRG-R3L14-C14-051910-GM-CATHODE-LONGDATED-20240207 | 051910 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_false_positive | False | False |
| TRG_R3L73-C14-051910-LGCHEM-INTEGRATED-MATERIALS-DEMAND-RISK-NO-HARD4C | 051910 | C14_EV_DEMAND_SLOWDOWN_4B_4C | C14 should flag EV/material demand slowdown risk, but not convert diversified integrated chemical/cathode exposure into hard 4C when later rebound and business-buffer evidence can exist. The correct label is RiskWatch/local 4B boundary, not hard thesis break without non-price evidence. | True | True |
| TRG_R3L73-C14-051910-LGCHEM-INTEGRATED-MATERIALS-DEMAND-RISK-NO-HARD4C | 051910 | C14_EV_DEMAND_SLOWDOWN_4B_4C | C14 should flag EV/material demand slowdown risk, but not convert diversified integrated chemical/cathode exposure into hard 4C when later rebound and business-buffer evidence can exist. The correct label is RiskWatch/local 4B boundary, not hard thesis break without non-price evidence. | True | True |
| R13L14_X_TRIG_TRG-R3L14-C14-051910-GM-CATHODE-LONGDATED-20240207 | 051910 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R1L12_C04_052690_CZECH_DESIGN_PURE_PLAY_SPIKE_STAGE2_ACTIONABLE | 052690 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive | False | False |
| T052690_STAGE2_20240717_CZ_PREFERRED_BIDDER | 052690 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_too_early | False | False |
| C04_KEPCO_EC_20240718_STAGE2_ACTIONABLE | 052690 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive | False | False |
| TRG_R1L16_C04_052690_CZECH_PREF_DESIGN_PROXY_FALSE_GREEN | 052690 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive | False | False |
| R1L12_C04_052690_CZECH_DESIGN_PURE_PLAY_SPIKE_LOCAL_4B_OVERLAY | 052690 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_false_positive | False | False |
| TR_R13L29_KEPCO_STAGE2_20220310 | 052690 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| R11C31_052690_T1_STAGE2 | 052690 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| R11C31_052690_T1_STAGE2 | 052690 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| TRG_R11L73-C31-052690-KEPCO-ENC-CZECH-NUCLEAR-EPC-PROXY-CHASE | 052690 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should not treat the nuclear preferred-bidder headline as durable Stage2 for EPC/engineering proxies unless named scope, contract allocation, revenue timing, or backlog bridge is visible. KEPCO E&C gapped into the event but then opened severe MAE and drawdown. | False | True |
| TRG_R11L73-C31-052690-KEPCO-ENC-CZECH-NUCLEAR-EPC-PROXY-CHASE | 052690 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should not treat the nuclear preferred-bidder headline as durable Stage2 for EPC/engineering proxies unless named scope, contract allocation, revenue timing, or backlog bridge is visible. KEPCO E&C gapped into the event but then opened severe MAE and drawdown. | False | True |
| R13L12_REDTEAM__R1L12_C04_052690_CZECH_DESIGN_PURE_PLAY_SPIKE_STAGE2_ACTIONABLE | 052690 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| T053290-S2-20210304 | 053290 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| TRG_R11L75-C31-053290-NE-NEUNGYULE-MEDQUOTA-EDU-PROXY-FADE | 053290 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should not treat broad education-policy beta as durable Stage2 unless the policy connects to direct product demand, paid course enrollment, channel expansion or margin bridge. NE Neungyule had only tiny MFE and then severe drawdown before later theme rebounds. | True | True |
| R12_C31_053290_STAGE2WATCH_20210304 | 053290 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_4B_too_late | False | False |
| R13L15_X_TRIG_TR_R12L15_C31_053290_STAGE2_20200224 | 053290 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L10_X08_053290_Stage2_event_premium_risk_watch | 053290 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late | False | False |
| TRG_R8L82-C28-053580-WEBCASH-FINTECH-SOFTWARE-RETENTION-FADE | 053580 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | C28 should not treat B2B fintech software retention theme beta as durable Stage2 unless customer retention, paid conversion, renewal, usage, revenue and margin bridge are visible. WebCash had modest MFE and then high-MAE fade. | True | True |
| R10L14_C30_053690_T_STAGE2_20240327 | 053690 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_missed_structural | False | False |
| R8L21_C28_053800_T1_FALSE_STAGE2 | 053800 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive | False | False |
| R8L21_C28_053800_T1_FALSE_STAGE2 | 053800 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive | False | False |
| R13L39_C28_053800_STAGE2_FALSE_20220311 | 053800 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive | False | False |
| TR-C28-053800-S2-2022-01-05 | 053800 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive | False | False |
| R8L12_C28_AHNLAB_T1_PRICE_ONLY_BLOWOFF_2022-03-23 | 053800 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive | False | False |
| R8L12_C28_AHNLAB_T1_PRICE_ONLY_BLOWOFF_2022-03-23 | 053800 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive | False | False |
| R8L10_C28_TRG_004A_AHNLAB_STAGE2_WATCH_2022_03_11 | 053800 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive | False | False |
| R8L12_C28_AHNLAB_EVENT_PREMIUM_20220323 | 053800 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_4B_too_late | False | False |
| R8L21_C28_053800_T2_4B_PRICE_ONLY | 053800 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive | False | False |
| R8L21_C28_053800_T2_4B_PRICE_ONLY | 053800 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive | False | False |
| TR-C28-053800-4B-2022-03-23 | 053800 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive | False | False |
| R13L39_C28_053800_4B_20220324 | 053800 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_4B_too_late | False | False |
| R13L39_C28_053800_4C_20220415 | 053800 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_4C_too_late | False | False |
| R13L12_REDTEAM__R8L12_C28_AHNLAB_T1_PRICE_ONLY_BLOWOFF_2022-03-23 | 053800 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L10_X06_053800_Stage2-Watch | 053800 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| TRG_R12L81-C31-054050-NONGWOO-BIO-SEED-AGRI-POLICY-BOUNDED | 054050 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should keep seed/agri policy monitoring active, but should not force local 4B when MAE is bounded and no non-price demand or margin break is confirmed. Nongwoo Bio is a RiskWatch/no durable Stage2/no forced 4B boundary. | True | True |
| TRG_R6L79-C21-055550-SHINHAN-BANK-HOLDCO-CAPITAL-RETURN | 055550 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | C21 should protect bank-holding positives when ROE/PBR rerating maps to capital buffer, dividend, buyback, treasury cancellation and earnings-quality bridge. Shinhan produced large MFE with bounded entry-basis MAE, but raw share-count changes inside the window require validation before runtime promotion. | True | True |
| TRG_R6L15_SHINHAN_20240729_STAGE2A | 055550 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | False | False |
| R6L10_C21_055550_VALUEUP_CAPITAL_RETURN_POS_GREEN_20240726 | 055550 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_late | False | False |
| R13L25_C21_SHINHAN_055550_GREEN_20240726 | 055550 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_late | False | False |
| TR_R11L12_SHINHAN_VALUEUP_STAGE2_20240226 | 055550 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_too_late | False | False |
| TRG_R12L80-C31-057030-YBMNET-ONLINE-EDUCATION-POLICY-FADE | 057030 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should not treat online education or language-learning policy beta as durable Stage2 unless paid conversion, institutional demand, subscription revenue and margin bridge are visible. YBM Net produced a tradable MFE but then a high-MAE fade. | True | True |
| R13L15_X_TRIG_TR_R12L15_C31_057030_STAGE2_20200224 | 057030 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late | False | False |
| R13L15_X_TRIG_TR_R12L15_C31_057030_4B_20200828 | 057030 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late | False | False |
| R13L12_T008_058470_COUNTER | 058470 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_false_positive | False | False |
| R2L10_C08_RINO_T1 | 058470 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_too_late | False | False |
| R2L11_T01_RINO_STAGE2_TEST_SOCKET_AI_EDGE_DEVICE | 058470 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_too_late | False | False |
| T_R2L14_058470_STAGE2A_20240122 | 058470 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_too_early | False | False |
| R2L11_C08_058470_GREEN_20240412 | 058470 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_too_late | False | False |
| R2L13_C08_058470_T2 | 058470 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_4B_too_early | False | False |
| R2L11_T01B_RINO_LATE_GREEN_4B_OVERLAY | 058470 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_4B_too_late | False | False |
| R13L13_C09_058470_THEME_2024-03-11 | 058470 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_false_positive | False | False |
| R2L14_C09_058470_RINO_4B_VALUATION_BLOWOFF | 058470 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_4B_too_early | False | False |
| R13L13_X_R2L13_C08_058470_T2 | 058470 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_early | False | False |
| R13L14_X_TRIG_R2L14_C09_058470_RINO_4B_VALUATION_BLOWOFF | 058470 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_early | False | False |
| R2L13_C08_058470_T2 | 058470 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_early | False | False |
| R13L14_G01_02_058470_T_R2L14_058470_STAGE2A_20240122 | 058470 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_too_early | False | False |
| TRG_R8L75-C28-058970-EMRO-PROCUREMENT-SAAS-CONTRACT-RETENTION-BRIDGE | 058970 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | C28 should allow a delayed Stage2 when procurement SaaS / supply-chain AI demand connects to actual enterprise contract retention, customer expansion, recurring license or margin bridge. EMRO produced controlled-MAE follow-through after the August reset, but the price shard shows share-count changes, so runtime promotion needs validation. | True | True |
| TRG_C26_NHNKCP_2024_02_14_STAGE2A | 060250 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| C25_CUREXO_S2A_20230626 | 060280 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_too_early | False | False |
| C25_CUREXO_4B_20230824 | 060280 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_4B_too_late | False | False |
| TRG_R8L82-C28-060850-YOUNGLIMWON-ERP-CONTRACT-RETENTION-FADE | 060850 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | C28 should not treat ERP/cloud software theme beta as durable Stage2 unless ARR/subscription, renewal, churn control, implementation backlog, revenue conversion and margin bridge are visible. YoungLimWon had a theme spike and then high MAE, so it is local-4B unless retention economics are source-repaired. | True | True |
| TRG_COM2USHOLDINGS_2021_P2E_TOKEN_4B_2021_11_02 | 063080 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_4B_too_late | False | False |
| TRG_C26_DANAL_2021_12_13_4B | 064260 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_4B_too_late | False | False |
| TRG_C26_DANAL_2021_11_17_STAGE2A | 064260 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_4B_too_late | False | False |
| R2L13_C08_064290_T1 | 064290 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_false_positive | False | False |
| R2L14_C09_064290_INTEKPLUS_FAILED_BLOWOFF | 064290 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_false_positive | False | False |
| R13L13_X_R2L13_C08_064290_T1 | 064290 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R2L13_C08_064290_T1 | 064290 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L14_X_TRIG_R2L14_C09_064290_INTEKPLUS_FAILED_BLOWOFF | 064290 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| TRG_R11L79-C03-064350-HYUNDAI-ROTEM-GROUND-SYSTEM-EXPORT-BACKLOG | 064350 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | C03 should allow ground-system positives when export framework or follow-on contract maps to named customer/project, backlog, delivery schedule, revenue recognition and margin bridge. Hyundai Rotem produced very large MFE with controlled entry-basis MAE, but lifecycle 4B is needed if delivery/margin evidence fades. | True | True |
| TRG_R1L74-C03-064350-HYUNDAI-ROTEM-K2-GROUND-SYSTEMS-BACKLOG | 064350 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | C03 should allow Stage2 when defense-export attention is tied to a named ground-systems framework, backlog visibility, production cadence and margin bridge. Hyundai Rotem's stock-web path had large MFE and limited entry-basis MAE; after the late-2024 peak, a local 4B lifecycle guard is still needed if export/backlog evidence stops refreshing. | True | True |
| TRG_R1L74-C03-064350-HYUNDAI-ROTEM-K2-GROUND-SYSTEMS-BACKLOG | 064350 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | C03 should allow Stage2 when defense-export attention is tied to a named ground-systems framework, backlog visibility, production cadence and margin bridge. Hyundai Rotem's stock-web path had large MFE and limited entry-basis MAE; after the late-2024 peak, a local 4B lifecycle guard is still needed if export/backlog evidence stops refreshing. | True | True |
| C03_064350_20220826_STAGE3_YELLOW_EXECUTIVE | 064350 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_green_too_easy_if_contract_only | False | False |
| TRG_R9L77-C29-064350-HYUNDAI-ROTEM-RAIL-MOBILITY-ORDERBOOK-MARGIN | 064350 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should allow rail/mobility equipment positives when orderbook, delivery slots, export/customer cadence, utilization and margin bridge are visible. Hyundai Rotem produced very large MFE with controlled entry-basis MAE, but the move must be lifecycle-managed if orderbook/margin evidence fades. | True | True |
| TRG_R2L73-C08-064760-TCK-SIC-CONSUMABLE-CUSTOMER-QUALITY-LOCAL4B | 064760 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | C08 should not treat high-quality semi consumables as Green when near-term customer utilization or margin bridge is absent. TCK had an initial MFE but later opened large MAE and drawdown, requiring local 4B-watch rather than durable Stage2. | True | True |
| TRG_R2L73-C08-064760-TCK-SIC-CONSUMABLE-CUSTOMER-QUALITY-LOCAL4B | 064760 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | C08 should not treat high-quality semi consumables as Green when near-term customer utilization or margin bridge is absent. TCK had an initial MFE but later opened large MAE and drawdown, requiring local 4B-watch rather than durable Stage2. | True | True |
| TRG_R9L80-C29-064960-SNT-MOTIV-MOTOR-DRIVETRAIN-BOUNDED-RISKWATCH | 064960 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should not force bounded motor/drivetrain supplier rows into 4B when MAE is contained, but it also should not mark durable Stage2 without customer volume, mix, drivetrain content and margin bridge. SNT Motiv is a bounded RiskWatch row. | True | True |
| TR-C29-SNTMOTIV-S2-20230412 | 064960 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| TRG_R9L75-C29-064960-SNT-MOTIVE-MOTOR-DEFENSE-AUTO-MIX-MARGIN | 064960 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should include slow mobility suppliers when motor/module mix, electrification component exposure, customer program stability and margin bridge are visible. SNT Motive is not an explosive beta row; it is a low-volatility supplier rerating candidate that should not be overblocked but still needs non-price mix/margin evidence. | True | True |
| R1L13-VICTEK-20240529-PRICEONLY | 065450 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_false_positive | False | False |
| TRG_R7L82-C25-065510-HUVITZ-OPHTHALMIC-DEVICE-SHARECOUNT-FADE | 065510 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | C25 should not treat ophthalmic/optical device export theme beta as durable Stage2 unless customer order, distributor channel, reimbursement/capex cycle, revenue conversion and margin bridge are visible. Huvitz had an early spike, a severe high-MAE fade, and 2024 shard share-count changes that require validation. | True | True |
| R11L13_C31_065950_20200220_4B | 065950 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_4B_too_late | True | False |
| R11L13_C31_065950_20200120_T1 | 065950 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | True | False |
| R12L14_C31_065950_STAGE2A_20200120 | 065950 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_4B_too_late | False | False |
| WELCRON_STAGE2_2020_01_20_FIRST_CASE | 065950 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| R13L13_X_R11L13_C31_065950_20200220_4B | 065950 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late | False | False |
| R11L13_C31_065950_20200220_4B | 065950 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late | False | False |
| R13L13_X_R11L13_C31_065950_20200120_T1 | 065950 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L15_WELCRON_STAGE2_2020_01_20_FIRST_CASE | 065950 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R11L13_C31_065950_20200120_T1 | 065950 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| C27_066410_20210924_PRICE_ASSOCIATION_FALSE_GREEN | 066410 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_false_positive | False | False |
| C27_066410_20211122_4C_ASSOCIATION_REVERSAL | 066410 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_4C_too_late | False | False |
| T_C11_LNF_STAGE2A_2023_02_28 | 066970 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive | False | False |
| R3L12_T_LNF_STAGE2_20230302 | 066970 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive | False | False |
| TRG-R3L13-C11-066970-LNF-TESLA-ORDERBOOK-CALLOFF-20230228 | 066970 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive | False | False |
| R3L10-C11-003-T1 | 066970 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive | False | False |
| R3L12_T_LNF_4C_20231107 | 066970 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_4C_too_late | False | False |
| TRG-R3L12-066970-STAGE2A-20230228 | 066970 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_false_positive | False | False |
| C12-066970-20230726-RISK | 066970 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_4B_too_late | False | False |
| TR_R3L15_C14_LNF_20230726_4B_OVERLAY | 066970 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_4B_too_late | False | False |
| R3L11-C14-LNF-4C-20230726 | 066970 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_4C_too_late | False | False |
| TRG_C14_066970_20240125_LF_LITHIUM_PRICE_ONLY_COUNTEREXAMPLE | 066970 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_false_positive | False | False |
| TR_C14_066970_20241107_STAGE4B_WATCH | 066970 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_4C_too_early | False | False |
| R13L55_C14_066970_4C_LATE_20230726 | 066970 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_4C_too_late | False | False |
| R3L11_T03_LNF_20231031_HARD_4C_FALSE_BREAK | 066970 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_4C_too_late | False | False |
| TR_C14_LNF_20240725_STAGE4C | 066970 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_4C_too_late | False | False |
| R13L12_REDTEAM__TRG-R3L12-066970-STAGE2A-20230228 | 066970 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L13_X_TRG-R3L13-C11-066970-LNF-TESLA-ORDERBOOK-CALLOFF-20230228 | 066970 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| TRG-R3L13-C11-066970-LNF-TESLA-ORDERBOOK-CALLOFF-20230228 | 066970 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L11_HIGHMAE_X06_066970_4B4C_20230726 | 066970 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_4C_too_late | False | False |
| C26_SOOP_T2_4B_20240228 | 067160 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_4B_too_late | False | False |
| TRG_C26_SOOP_2024_07_11_4B | 067160 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_4B_too_late | False | False |
| TR_SOOP_20210430_S2A | 067160 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_too_late | False | False |
| TRG_SOOP_2021Q1_STAGE2_ACTIONABLE_2021_05_03 | 067160 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_too_late | False | False |
| R8L12_C26_TRG_003A_SOOP_STAGE2_ACTIONABLE_2023_12_07 | 067160 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_too_late | False | False |
| R8L11_C26_SOOP_T1_STAGE2_ACTIONABLE_2023-12-07 | 067160 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_too_late | False | False |
| R8L11_C26_SOOP_T1_STAGE2_ACTIONABLE_2023-12-07 | 067160 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_too_late | False | False |
| TRG_C26_SOOP_2023_12_07_STAGE2A | 067160 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_missed_structural | False | False |
| TR_SOOP_20210907_GREEN | 067160 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_too_late | False | False |
| R8L11_C26_SOOP_T2_STAGE3_GREEN_CONFIRMATION_2024-04-26 | 067160 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_too_late | False | False |
| R8L11_C26_SOOP_T2_STAGE3_GREEN_CONFIRMATION_2024-04-26 | 067160 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_too_late | False | False |
| TRG_SOOP_2021_PRICE_LOCAL_4B_OVERLAY_2021_11_09 | 067160 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_4B_too_early | False | False |
| SOOP_4B_LOCAL_REPRICE_20240228 | 067160 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_4B_too_early_if_price_only | False | False |
| R13L15_X_TRIG_TR_SOOP_20210430_S2A | 067160 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_too_late | False | False |
| R13L15_X_TRIG_TR_SOOP_20210907_GREEN | 067160 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_too_late | False | False |
| R13L12_FP_X03_067160_Stage2-Actionable_2023-12-07 | 067160 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_too_late | False | False |
| TRG_R2L73-C08-067310-HANAMICRON-OSAT-HBM-BETA-WEAK-UTILIZATION | 067310 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | C08 must not allow OSAT/HBM packaging beta to become durable Stage2 without utilization, customer quality, margin, or package mix evidence. Hana Micron generated only small MFE and then severe MAE. | True | True |
| TRG_R2L73-C08-067310-HANAMICRON-OSAT-HBM-BETA-WEAK-UTILIZATION | 067310 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | C08 must not allow OSAT/HBM packaging beta to become durable Stage2 without utilization, customer quality, margin, or package mix evidence. Hana Micron generated only small MFE and then severe MAE. | True | True |
| R13L54_C28_067920_STAGE2A_20210204 | 067920 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_too_late | False | False |
| TRG_R8L75-C28-067920-IGLOO-CYBERSECURITY-CONTRACT-RETENTION-BETA-FADE | 067920 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | C28 should not treat cybersecurity/SIEM/SOC theme spikes as durable Stage2 unless recurring contract retention, renewal rate, managed security service backlog or margin bridge is visible. IGLOO had a strong early MFE but then faded into high MAE and post-peak drawdown. | True | True |
| R13L54_C28_067920_GREEN_20210507 | 067920 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_too_late | False | False |
| TRG_R7L73-C23-068270-CELLTRION-ZYMFENTRA-COMMERCIALIZATION-BRIDGE | 068270 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | C23 should reward regulatory approval only when it becomes commercialization evidence: launch, reimbursement access, channel uptake, direct sales or margin bridge. Celltrion has a slower but cleaner large-cap commercialization path with controlled MAE. | True | True |
| TRG_R7L73-C23-068270-CELLTRION-ZYMFENTRA-COMMERCIALIZATION-BRIDGE | 068270 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | C23 should reward regulatory approval only when it becomes commercialization evidence: launch, reimbursement access, channel uptake, direct sales or margin bridge. Celltrion has a slower but cleaner large-cap commercialization path with controlled MAE. | True | True |
| TRG_R7L81-C23-068270-CELLTRION-BIOSIMILAR-COMMERCIALIZATION-POSTCA | 068270 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | C23 should not overblock large-cap biosimilar commercialization rows when MAE is controlled and commercialization/export revenue bridge may be visible. Celltrion requires post-CA and share-count continuity validation because the profile flags a 2024-01-12 corporate-action candidate and the 2024 shard shows share-count changes. | True | True |
| TRG_R4L79-C17-069260-TKG-HUCHEMS-NITRIC-ACID-SPREAD-FADE | 069260 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | C17 should not treat nitric-acid/TDI/MNB spread exposure as durable Stage2 unless volume, contract price, utilization, raw-material spread and margin bridge refreshes. TKG Huchems produced tiny MFE and then a persistent drawdown path. | True | True |
| T48_069620_20190207_STAGE2_APPROVAL_COUNTEREXAMPLE | 069620 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive | False | False |
| R7L16_C23_069620_STAGE3_APPROVAL_ONLY_FALSE_GREEN_2019_02_07 | 069620 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive | False | False |
| TRG_R5L74-C19-069960-HYUNDAI-DS-VALUEUP-TRAFFIC-MARGIN | 069960 | C19_BRAND_RETAIL_INVENTORY_MARGIN | C19 should allow Stage2 only when low-PBR/value-up retail attention connects to traffic, inventory discipline, duty-free recovery or margin conversion. Hyundai Department Store produced a controlled-MAE positive path, but later drawdown still needs local 4B-watch if the margin bridge stops refreshing. | True | True |
| TRG_R5L74-C19-069960-HYUNDAI-DS-VALUEUP-TRAFFIC-MARGIN | 069960 | C19_BRAND_RETAIL_INVENTORY_MARGIN | C19 should allow Stage2 only when low-PBR/value-up retail attention connects to traffic, inventory discipline, duty-free recovery or margin conversion. Hyundai Department Store produced a controlled-MAE positive path, but later drawdown still needs local 4B-watch if the margin bridge stops refreshing. | True | True |
| TRG_R11L76-C31-071090-HISTEEL-EASTSEA-GAS-POLICY-PIPE-BETA-FADE | 071090 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should not treat steel-pipe/resource-policy beta as durable Stage2 unless actual project order, customer, delivery schedule and margin bridge is visible. Hi Steel produced a small MFE and then a large MAE drawdown, making it a policy-proxy local 4B row. | True | True |
| TRG_R12L79-C31-071320-DISTRICT-HEATING-TARIFF-RECOVERY-BRIDGE | 071320 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should preserve utility tariff normalization positives when policy adjustment maps to cost pass-through, direct earnings recovery, dividend/capital policy and regulatory visibility. Korea District Heating produced very large MFE with controlled entry-basis MAE, but the post-peak drawdown needs lifecycle management. | True | True |
| TR-C29-KUMHOTIRE-S2A-20231110 | 073240 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_4B_too_late | False | False |
| TR-C29-KUMHOTIRE-S2A-20231110 | 073240 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_4B_too_late | False | False |
| TRG_R9L78-C29-073240-KUMHO-TIRE-OE-REPLACEMENT-MIX-MARGIN | 073240 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should allow tire names when OE/replacement volume, product mix, utilization, raw-material spread and margin bridge are visible. Kumho Tire produced large MFE, but later high MAE and post-peak drawdown require lifecycle local 4B if mix/margin evidence fades. | True | True |
| TR-C29-KUMHOTIRE-4B-20240507 | 073240 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_4B_too_late | False | False |
| TRG_R2L16_C10_074600_WONIKQNC_PRICEONLY_20240607 | 074600 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_false_positive | False | False |
| TRG_R4L78-C16-075970-DONGKUK-RNS-RAREEARTH-REFRACTORY-THEME-FADE | 075970 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | C16 should not treat rare-earth/refractory theme spikes as durable Stage2 unless policy shock maps to direct order, volume, pricing and margin bridge. Dongkuk R&S produced only modest MFE and then a persistent drawdown, making it local 4B-watch rather than durable Green. | True | True |
| TRG_R1L83-C01-077970-STX-ENGINE-MARINE-ENGINE-BACKLOG-MARGIN | 077970 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | C01 should protect industrial orderbacklog positives only when customer/program backlog, delivery schedule, revenue recognition and margin bridge are visible. STX Engine produced very large MFE with effectively no entry-basis MAE, but post-peak drawdown still requires lifecycle 4B if order/delivery/margin evidence fades. | True | True |
| TRG_R1L79-C01-077970-STX-ENGINE-ORDER-BACKLOG-DELIVERY-MARGIN | 077970 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | C01 should preserve ship/defense engine suppliers when order backlog, delivery schedule, customer quality, revenue recognition and margin bridge are visible. STX Engine produced high MFE with essentially no entry-basis MAE, but lifecycle local 4B is needed if backlog or margin evidence fades. | True | True |
| TRG_COM2US_2023_SUMMONERS_CHRONICLES_GLOBAL_2023_03_09 | 078340 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_false_positive | False | False |
| R5L16_C20_ABLECNC_T2_REJECT_20240510 | 078520 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | False | False |
| TRG_R3L77-C11-078600-DAEJOO-SILICON-ANODE-ORDERBOOK-MARGIN | 078600 | C11_BATTERY_ORDERBOOK_RERATING | C11 should allow battery-material orderbook Stage2 when a silicon-anode customer ramp, call-off/orderbook, capacity absorption and margin bridge are visible. Daejoo Electronic Materials produced high MFE with almost no entry-basis MAE; post-peak drawdown still requires lifecycle local 4B if orderbook/margin evidence fades. | True | True |
| None | 079940 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | None | True | True |
| R13_CROSS_079940_2024-02-22_Stage2-FalsePositive_/_CloudAIBetaLocal4B | 079940 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | None | True | True |
| TRG_R12L82-C31-080160-MODETOUR-TRAVEL-VISA-REOPENING-FADE | 080160 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should not treat travel-agency reopening theme beta as durable Stage2 unless booking volume, package margin, channel mix, air-seat cost, revenue conversion and margin bridge are visible. Modetour had almost no forward MFE and then severe MAE. | True | True |
| TRG_R2L81-C08-080580-OKINS-ELECTRONICS-SOCKET-THEME-FADE | 080580 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | C08 should not treat socket/probe/interface theme beta as durable Stage2 unless named customer quality, reorder, utilization, delivery and margin bridge are visible. Okins Electronics had a tradable early MFE, then a severe high-MAE fade. | True | True |
| TRG_R2L78-C08-080580-OKINS-TEST-SOCKET-THEME-FADE | 080580 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | C08 should not treat socket/connector/HBM theme beta as durable Stage2 unless customer qualification, socket reorder, shipment, ASP and margin bridge are visible. Okins Electronics had an early MFE but then opened a severe MAE drawdown path. | True | True |
| TRG_R4L75-C16-081150-TFLEX-RARE-METAL-PROCESSING-SUPPLY-BRIDGE | 081150 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | C16 should allow Stage2 when strategic-resource policy heat connects to real rare-metal processing, customer demand, inventory/supply and margin bridge. T-Flex produced controlled-MAE follow-through and later 2025 highs, but runtime promotion still requires non-proxy customer/supply evidence. | True | True |
| R13L45_081660_STAGE2_FALSE_2024-02-13 | 081660 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_false_positive | False | False |
| None | 081660 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | True | True |
| R13_CROSS_081660_2024-04-11_Stage2-Actionable-InventoryCleanup | 081660 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | True | True |
| TRG_R5L76-C19-081660-FILA-HOLDINGS-GLOBAL-BRAND-INVENTORY-MARGIN | 081660 | C19_BRAND_RETAIL_INVENTORY_MARGIN | C19 should preserve low-MAE global brand rerating candidates when inventory destocking, channel mix, royalty/brand margin and capital return evidence are visible. FILA Holdings had modest MFE but a controlled risk profile; it still needs lifecycle monitoring if inventory/margin evidence fades. | True | True |
| T_C19_FILA_2021_REOPENING_PRICE_ONLY | 081660 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_4B_too_early | False | False |
| T_C19_FILA_2021_LOCAL_4B_PRICE_ONLY | 081660 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_4B_too_early | False | False |
| R13L45_081660_4B_2024-08-01 | 081660 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_false_positive | False | False |
| R6L15_C22_082640_T1 | 082640 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_4B_too_late | False | False |
| R6L14_T02_DONGLIFE_20240202_STAGE2_ACTIONABLE_LIFE_CSM_EVENT_PREMIUM | 082640 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_4B_too_late | False | False |
| TRG_R6L78-C22-082640-TONGYANG-LIFE-HIGHBETA-RESERVE-CAPITAL-RETURN | 082640 | C22_INSURANCE_RATE_CYCLE_RESERVE | C22 can allow high-beta life-insurance positives when reserve quality, rate-cycle leverage, capital buffer and shareholder-return bridge are explicit. Tong Yang Life produced very large MFE with low entry-basis MAE, but the post-peak drawdown shows high beta must be lifecycle-managed. | True | True |
| TRG_R6L82-C22-082640-TONGLIFE-LIFE-INSURANCE-RATE-CYCLE-EVENT-WHIPSAW | 082640 | C22_INSURANCE_RATE_CYCLE_RESERVE | C22 can protect life-insurance positives when CSM/reserve quality, rate-cycle sensitivity, capital return and payout bridge are visible. Tongyang Life had very large MFE but also a violent post-peak whipsaw, so event mechanics and bridge refresh are required. | True | True |
| R6L15_C22_082640_T4B | 082640 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_4B_too_late | False | False |
| R13L14_X_TRIG_R6L14_T02_DONGLIFE_20240202_STAGE2_ACTIONABLE_LIFE_CSM_EVENT_PREMIUM | 082640 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late | False | False |
| TRG_R1L79-C01-082740-HANWHA-ENGINE-SHIP-ENGINE-BACKLOG-MARGIN | 082740 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | C01 should allow industrial ship-engine positives when shipbuilding orderbook maps to engine order backlog, delivery slots, pricing, revenue recognition and margin conversion. Hanwha Engine produced a large MFE, but raw share-count movement inside the window requires validation before runtime promotion. | True | True |
| TRG_R1L83-C01-082740-HANWHA-ENGINE-MARINE-ENGINE-BACKLOG-NAME-SHARECOUNT | 082740 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | C01 can protect marine-engine positives when shipbuilding customer orderbook, delivery schedule, revenue conversion and margin bridge are visible. Hanwha Engine had large MFE and controlled early MAE, but 2024 name/share-count continuity must be validated before runtime promotion. | True | True |
| R1L12_C04_083650_CZECH_BOILER_EQUIPMENT_HIGH_BETA_STAGE2_ACTIONABLE | 083650 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_too_late | False | False |
| TRG_R11L73-C31-083650-BHI-CZECH-NUCLEAR-EQUIPMENT-DELAYED-BRIDGE | 083650 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should not overblock true nuclear equipment/backlog beneficiaries, but the entry should not be a blind policy-headline chase. BHI had severe early MAE before later rerating; Stage2 requires non-proxy equipment order/backlog evidence and a lifecycle local 4B after peak. | False | True |
| TRG_R11L73-C31-083650-BHI-CZECH-NUCLEAR-EQUIPMENT-DELAYED-BRIDGE | 083650 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should not overblock true nuclear equipment/backlog beneficiaries, but the entry should not be a blind policy-headline chase. BHI had severe early MAE before later rerating; Stage2 requires non-proxy equipment order/backlog evidence and a lifecycle local 4B after peak. | False | True |
| TRG_R2L77-C07-084370-EUGENE-TECH-DEPOSITION-EQUIPMENT-RS | 084370 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | C07 should preserve equipment relative-strength rows when customer capex, deposition equipment orders, delivery schedule and margin bridge are visible. Eugene Technology had a controlled-MAE rerating path; later drawdown should be lifecycle-managed, not treated as hard 4C without order or margin break. | True | True |
| TRG_R2L74-C07-084370-EUGENE-TECH-DEPOSITION-EQUIPMENT-RS | 084370 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | C07 should allow Stage2 when front-end deposition equipment relative strength connects to HBM/DRAM capex, customer order visibility and margin bridge. Eugene Tech produced high MFE with limited entry MAE, but later post-peak drawdown means a lifecycle local 4B guard is needed if order/margin evidence stops refreshing. | True | True |
| TRG_R2L74-C07-084370-EUGENE-TECH-DEPOSITION-EQUIPMENT-RS | 084370 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | C07 should allow Stage2 when front-end deposition equipment relative strength connects to HBM/DRAM capex, customer order visibility and margin bridge. Eugene Tech produced high MFE with limited entry MAE, but later post-peak drawdown means a lifecycle local 4B guard is needed if order/margin evidence stops refreshing. | True | True |
| TRG_R2L16_C10_084370_EUGENE_STAGE2A_20240119 | 084370 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_too_early | False | False |
| R2L16_C10_084370_STAGE2A_2024-01-25 | 084370 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_too_late | False | False |
| None | 084370 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | None | True | True |
| R13_CROSS_084370_2024-02-20_Stage2-Actionable | 084370 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | None | True | True |
| TRG_R7L71_C24_084990_ENGENSIS_DPN_PHASE3_FAILURE | 084990 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_4C_too_late | False | False |
| R7L27-T006 | 084990 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_4C_too_early | False | False |
| R7L27-T006 | 084990 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_4C_too_early | False | False |
| TRG_R7L71_C24_084990_ENGENSIS_DPN_PHASE3_FAILURE | 084990 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_4C_too_late | False | False |
| R6L15_C22_085620_T1 | 085620 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive | False | False |
| TRG_R6L74-C22-085620-MIRAE-LIFE-BETA-BRIDGE-FADE | 085620 | C22_INSURANCE_RATE_CYCLE_RESERVE | C22 should not treat life-insurance/value-up beta as durable Stage2 unless CSM quality, reserve sensitivity, K-ICS and capital-return evidence refreshes. Mirae Asset Life had an early MFE but quickly opened 90D MAE and never produced a strong rerating path. | True | True |
| TRG_R6L74-C22-085620-MIRAE-LIFE-BETA-BRIDGE-FADE | 085620 | C22_INSURANCE_RATE_CYCLE_RESERVE | C22 should not treat life-insurance/value-up beta as durable Stage2 unless CSM quality, reserve sensitivity, K-ICS and capital-return evidence refreshes. Mirae Asset Life had an early MFE but quickly opened 90D MAE and never produced a strong rerating path. | True | True |
| TRG_R6L78-C22-085620-MIRAEASSET-LIFE-INSURANCE-BETA-FADE | 085620 | C22_INSURANCE_RATE_CYCLE_RESERVE | C22 should not treat life-insurance rate/value-up beta as durable Stage2 unless reserve quality, capital buffer, shareholder return and earnings bridge are visible. Mirae Asset Life had a tradable early MFE, then opened a high-MAE drawdown path. | True | True |
| TRG_R6L82-C22-085620-MIRAE-ASSET-LIFE-RATE-CYCLE-FADE | 085620 | C22_INSURANCE_RATE_CYCLE_RESERVE | C22 should not treat life-insurance value-up/rate-cycle beta as durable Stage2 unless CSM quality, reserve adequacy, payout policy, solvency ratio and ROE bridge are visible. Mirae Asset Life had an early spike and then persistent MAE, so it is a local-4B fade candidate. | True | True |
| TRG_R6L80-C22-085620-MIRAE-ASSET-LIFE-THEME-FADE | 085620 | C22_INSURANCE_RATE_CYCLE_RESERVE | C22 should not treat life-insurance value-up/rate-cycle beta as durable Stage2 unless CSM, reserve quality, capital return, investment spread and earnings bridge are visible. Mirae Asset Life had an initial spike, then a high-MAE fade. | True | True |
| TRG_R6L76-C22-085620-MIRAE-ASSET-LIFE-VALUEUP-BETA-RESERVE-FADE | 085620 | C22_INSURANCE_RATE_CYCLE_RESERVE | C22 should not treat life-insurance value-up beta as durable Stage2 unless CSM/IFRS17 reserve quality, K-ICS buffer, new-business margin, capital return and shareholder-return evidence refreshes. Mirae Asset Life had a tradable spike but then opened high MAE, making it a local 4B row. | True | True |
| None | 085620 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | True | True |
| R13_CROSS_085620_2024-02-01_Stage2-FalsePositive_/_LifeInsurerPriceOnlyValueupBeta | 085620 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | True | True |
| R6L14_T04_MIRAEASSETLIFE_20240202_FALSE_STAGE2_LIFE_BETA_LOW_LIQUIDITY | 085620 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive | False | False |
| R6L47_T06_085620_FALSE_GREEN_POLICY_ONLY_BLOWOFF | 085620 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive | False | False |
| R6L15_C22_085620_T4C | 085620 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_4C_too_late | False | False |
| R13L14_X_TRIG_R6L14_T04_MIRAEASSETLIFE_20240202_FALSE_STAGE2_LIFE_BETA_LOW_LIQUIDITY | 085620 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| TR-C29-GLOVIS-S2LOG-20230125 | 086280 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_too_early | False | False |
| TR-C29-GLOVIS-S2LOG-20230125 | 086280 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_too_early | False | False |
| T_R9L12_086280_STAGE2_20230608 | 086280 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_too_late | False | False |
| T_C29_086280_S2_20240807 | 086280 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_too_late | False | False |
| TRG_R9L73-C29-086280-GLOVIS-PCC-LOGISTICS-MARGIN-POST-CA | 086280 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should include logistics/PCC/CKD operating leverage when freight rate, capacity and capital-return bridge are visible. Because Hyundai Glovis had 2024 corporate-action candidates, the entry is placed after the 2024-08-02 candidate; the post-CA path is strong but needs source repair. | True | True |
| T_C29_086280_S2_20240807 | 086280 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_too_late | False | False |
| TRG_R9L73-C29-086280-GLOVIS-PCC-LOGISTICS-MARGIN-POST-CA | 086280 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should include logistics/PCC/CKD operating leverage when freight rate, capacity and capital-return bridge are visible. Because Hyundai Glovis had 2024 corporate-action candidates, the entry is placed after the 2024-08-02 candidate; the post-CA path is strong but needs source repair. | True | True |
| TRG_R6L12_HANA_STAGE2_20240226 | 086790 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_late | False | False |
| HANA-C21-S2A-20240226 | 086790 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_late | False | False |
| R6L11_T02_HANA_20240226_STAGE2_ACTIONABLE_VALUEUP_CAPITAL_RETURN | 086790 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_late | False | False |
| R6L45_T03_HANA_VALUEUP_STAGE2 | 086790 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_late | False | False |
| TR_HANA_GREEN_20240314 | 086790 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_late | False | False |
| R6L45_T04_HANA_CONFIRMED_GREEN | 086790 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_late | False | False |
| TRG_R6L12_HANA_4B_20241025 | 086790 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_4B_too_late | False | False |
| R6L41_C22_088350_T1_STAGE2_POLICY_ONLY | 088350 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive | True | True |
| R13L17_C22_088350_HANWHA_LIFE_EVENT_PREMIUM_2024_T1 | 088350 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive | False | False |
| R6L15_C22_088350_T1 | 088350 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive | False | False |
| R6L13_C22_HANWHALIFE_20240222_POLICY_BETA_RESERVE_GAP_T1 | 088350 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive | False | False |
| R13L20_C22_088350_S2A_20240222 | 088350 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive | False | False |
| R13L20_C22_088350_S2A_20240222 | 088350 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive | False | False |
| T_R13L21_088350_STAGE2_20250213 | 088350 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_too_early | False | False |
| R6L14_T03_HANWHALIFE_20240202_FALSE_STAGE2_RATE_BETA_NEGATIVE_SPREAD_GUARD | 088350 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive | False | False |
| R6L47_T04_088350_FALSE_GREEN_PRICE_RS_ONLY | 088350 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive | False | False |
| R6L41_C22_088350_T2_4C_WATCH | 088350 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_4C_too_late | True | True |
| R13L14_X_TRIG_R6L14_T03_HANWHALIFE_20240202_FALSE_STAGE2_RATE_BETA_NEGATIVE_SPREAD_GUARD | 088350 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L12_T004_089030_STAGE2 | 089030 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_missed_structural | False | False |
| R2L13_C07_089030_STAGE2A_20240119 | 089030 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_too_late | False | False |
| R13L12_T005_089030_GREEN_LATE | 089030 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_too_late | False | False |
| R13L13_C09_089030_S2A_2024-01-19 | 089030 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_4B_too_early | False | False |
| R9L14_C29_089590_T1_STAGE2_ACTIONABLE_20230118 | 089590 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| TR_R9L12_C29_03_089590_Stage2_Actionable | 089590 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| R9L14_C29_JEJUAIR_2023_REOPENING_FALSEBRIDGE_STAGE2_ACTIONABLE | 089590 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| T_R9L12_089590_STAGE2_20230509 | 089590 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| TRG_R9L81-C29-089590-JEJU-AIR-LCC-PASSENGER-YIELD-FADE | 089590 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should not treat LCC passenger recovery beta as durable Stage2 unless passenger volume, load factor, yield, fuel cost and operating margin bridge are visible. Jeju Air had almost no forward MFE after entry and then a persistent high-MAE path. | True | True |
| None | 089590 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | True | True |
| R13_CROSS_089590_2024-01-05_Stage4B-Local-AirlinePassengerBeta | 089590 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | True | True |
| R9L14_C29_089590_T3_4C_THESIS_BREAK_20230907 | 089590 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_4C_too_late | False | False |
| R13L14_X_TRIG_R9L14_C29_089590_T1_STAGE2_ACTIONABLE_20230118 | 089590 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L14_X_TRIG_R9L14_C29_089590_T3_4C_THESIS_BREAK_20230907 | 089590 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4C_too_late | False | False |
| NASMEDIA_STAGE2_AD_RECOVERY_20201106 | 089600 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_too_late | False | False |
| C26_NASMEDIA_T1_STAGE2_20210205 | 089600 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| TRG_C26_NASMEDIA_2021_STAGE2_ACTIONABLE | 089600 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| R8L13_C26_NASMEDIA_FALSE_2023-07-10 | 089600 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| R8L13_C26_NASMEDIA_FALSE_2023-07-10 | 089600 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| NASMEDIA_GREEN_REVISION_20210205 | 089600 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_too_late | False | False |
| TRG_NASMEDIA_2021_AD_RECOVERY_FALSE_POSITIVE_2021_02_10 | 089600 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| TRG_C26_NASMEDIA_2021_STAGE3_YELLOW_FALSE_POSITIVE | 089600 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| TRG_R9L82-C29-089860-LOTTE-RENTAL-FLEET-UTILIZATION-MARGIN | 089860 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should allow rental/mobility positives only when fleet utilization, used-car residual value, pricing, rental demand, revenue conversion and margin bridge are visible. Lotte Rental produced bounded MAE and later MFE, so it is a protected RiskWatch/Stage2-Yellow candidate after source repair rather than forced 4B. | True | True |
| None | 089860 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | True | True |
| R13_CROSS_089860_2024-02-23_Stage2-Actionable-FleetUtilizationMarginBridge | 089860 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | True | True |
| R10L14_C30_090410_T_STAGE2_20240327 | 090410 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive | False | False |
| R5L13_C20_090430_20210908_4C_CONFIRM | 090430 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_4C_too_late | False | False |
| R5L11-C20-AMORE-STAGE2-20230202 | 090430 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | False | False |
| R5L10_C20_AMORE_STAGE2_20240429 | 090430 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_4C_too_late | False | False |
| R5L13_C20_090430_20210512_STAGE2_FALSE_POSITIVE | 090430 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | False | False |
| T_C20_AMORE_2022_REOPENING_FALSE_POSITIVE | 090430 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | False | False |
| R5L10_T04_AMORE_STAGE2_FALSE_POSITIVE | 090430 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | False | False |
| T_AMORE_20230201_FALSE_STAGE2 | 090430 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | False | False |
| R5L34_C20_090430_T_STAGE2_2024_04_26 | 090430 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | False | False |
| R5L12-C20-AMORE-S2-NARR-20240514 | 090430 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | False | False |
| R5L71-C20-03-T1 | 090430 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | False | False |
| R13L24_C20_003_T1_STAGE2_YELLOW | 090430 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | False | False |
| R5L10_C20_AMORE_T2_20210510 | 090430 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | False | False |
| R5L11_T03_AMORE_20230210_FALSE_GREEN_CHINA_REOPENING | 090430 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | False | False |
| R5L14_C20_090430_T1_STAGE2Y_2024-04-30 | 090430 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | False | False |
| R5L38_C20_090430_FALSE_GREEN | 090430 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | False | False |
| R5L38_C20_090430_FALSE_GREEN | 090430 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | False | False |
| R5L12-C20-AMORE-4B-PRICE-20240531 | 090430 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_4B_too_early | False | False |
| R5L34_C20_090430_T_4B_2024_05_31 | 090430 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_4B_too_late | False | False |
| R5L12-C20-AMORE-4C-20240807 | 090430 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_4C_too_late | False | False |
| R13L24_C20_003_T2_4C_THESIS_BREAK | 090430 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_4C_too_late | False | False |
| R5L10_C20_AMORE_4C_20240807 | 090430 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_4C_too_late | False | False |
| R13L13_X_T_AMORE_20230201_FALSE_STAGE2 | 090430 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| T_AMORE_20230201_FALSE_STAGE2 | 090430 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L13_ACC_X07_090430_20210512 | 090430 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | False | False |
| TR_R9L12_C29_05_091810_Stage2_Actionable | 091810 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| R9L14_C29_TWAY_2023_ROUTE_VOLUME_FALSEBRIDGE_STAGE2_ACTIONABLE | 091810 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| T_R9L12_091810_STAGE2_20230515 | 091810 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_4C_too_late | False | False |
| TRG_R9L81-C29-091810-TWAY-LCC-ROUTE-YIELD-SHARECOUNT-LIFECYCLE | 091810 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 can allow airline/LCC positives only when passenger volume, route expansion, load factor, yield, fuel-cost sensitivity and margin bridge are visible. T'way produced later MFE but had large interim MAE and stock-web share-count changes, so source repair and share-count validation are mandatory. | True | True |
| T_R9L12_091810_4C_20231024 | 091810 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_4C_too_late | False | False |
| TRG_R12L74-C32-091810-TWAY-AIR-CONTROL-PREMIUM-DISPUTE-LIFECYCLE | 091810 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should allow a delayed control-premium dispute candidate when stake accumulation, management-rights pressure and strategic airline-route economics become credible. T'way produced a large MFE into early 2025, but the later collapse requires lifecycle local 4B if control-premium or route/capacity execution evidence fades. | True | True |
| TRG_R12L74-C32-091810-TWAY-AIR-CONTROL-PREMIUM-DISPUTE-LIFECYCLE | 091810 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should allow a delayed control-premium dispute candidate when stake accumulation, management-rights pressure and strategic airline-route economics become credible. T'way produced a large MFE into early 2025, but the later collapse requires lifecycle local 4B if control-premium or route/capacity execution evidence fades. | True | True |
| R13L12_REDTEAM__T_R9L12_091810_STAGE2_20230515 | 091810 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4C_too_late | False | False |
| TRG_R2L73-C08-092870-EXICON-HBM-TESTER-POST-CA-ADOPTION-BRIDGE | 092870 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | C08 can permit Stage2 when tester demand is tied to verified customer adoption/reorder and the entry window is after corporate-action contamination. Exicon's post-CA path had strong MFE with controlled MAE, but source repair is required before runtime promotion. | True | True |
| TRG_R2L73-C08-092870-EXICON-HBM-TESTER-POST-CA-ADOPTION-BRIDGE | 092870 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | C08 can permit Stage2 when tester demand is tied to verified customer adoption/reorder and the entry window is after corporate-action contamination. Exicon's post-CA path had strong MFE with controlled MAE, but source repair is required before runtime promotion. | True | True |
| R5L71-C19-002-S2 | 093050 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_false_positive | True | False |
| TRG_R5L76-C19-093050-LF-APPAREL-BRAND-INVENTORY-MARGIN-RECOVERY | 093050 | C19_BRAND_RETAIL_INVENTORY_MARGIN | C19 should allow slow brand/retail positives when inventory normalization, DTC/channel mix, markdown control and margin bridge are visible. LF produced a moderate MFE with controlled MAE; not explosive, but useful to avoid overfitting C19 only to high-beta consumer names. | True | True |
| R13L27_C16_093370_T1 | 093370 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_too_early | False | False |
| TRG_R8L82-C28-094280-HYOSUNG-ITX-ITOUTSOURCING-CONTRACT-RETENTION-BOUNDED | 094280 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | C28 should allow software/IT service positives only when recurring contract retention, renewal, managed-service orderbook, revenue conversion and margin bridge are visible. Hyosung ITX had bounded MAE and later MFE, so it is a RiskWatch/Stage2-Yellow candidate after source repair rather than a forced 4B row. | True | True |
| R13L12_T007_095340_COUNTER | 095340 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_false_positive | False | False |
| R2L13_C08_095340_T1 | 095340 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_false_positive | False | False |
| T_R2L14_095340_STAGE2A_20240311 | 095340 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_false_positive | False | False |
| R2L11_T03_ISC_STAGE3_FALSE_GREEN_SOCKET_BLOWOFF | 095340 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_false_positive | False | False |
| R2L11_C08_095340_GREENFALSE_20240308 | 095340 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_false_positive | False | False |
| R2L11_T03B_ISC_4C_WATCH_AFTER_BLOWOFF | 095340 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_4C_too_late | False | False |
| R2L14_C09_095340_ISC_FALSE_GREEN_BLOWOFF | 095340 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_false_positive | False | False |
| R13L13_C09_095340_THEME_2024-03-08 | 095340 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_false_positive | False | False |
| R13L13_C09_095340_4C_2024-06-21 | 095340 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_4C_too_late | False | False |
| R13L13_X_R2L13_C08_095340_T1 | 095340 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R2L13_C08_095340_T1 | 095340 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L14_X_TRIG_R2L14_C09_095340_ISC_FALSE_GREEN_BLOWOFF | 095340 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L11_REDTEAM__R2L11_T03_ISC_STAGE3_FALSE_GREEN_SOCKET_BLOWOFF | 095340 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L11_REDTEAM__R2L11_T03B_ISC_4C_WATCH_AFTER_BLOWOFF | 095340 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4C_too_late | False | False |
| R13L14_G02_03_095340_T_R2L14_095340_STAGE2A_20240311 | 095340 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | False | False |
| TRG_R2L74-C07-095610-TES-HBM-EQUIPMENT-BETA-BRIDGE-FADE | 095610 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | C07 should not treat a one-month equipment beta spike as durable Stage2 unless named customer order, HBM-related capex, backlog or margin bridge refreshes. TES had strong initial MFE but later opened severe MAE and drawdown, making it a local 4B-watch / false Stage2 row. | True | True |
| TRG_R2L74-C07-095610-TES-HBM-EQUIPMENT-BETA-BRIDGE-FADE | 095610 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | C07 should not treat a one-month equipment beta spike as durable Stage2 unless named customer order, HBM-related capex, backlog or margin bridge refreshes. TES had strong initial MFE but later opened severe MAE and drawdown, making it a local 4B-watch / false Stage2 row. | True | True |
| None | 095610 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_error_if_price_spike_or_memory_beta_is_counted_as_order_visibility | False | False |
| TRG-R2L11-C10-TES-20230324 | 095610 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_false_positive | False | False |
| None | 095610 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_false_green_risk_if_generic_cycle_is_treated_as_visibility | False | False |
| R2L16_C10_095610_STAGE2WATCH_2024-04-02 | 095610 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_4B_too_late | False | False |
| R2L16_C10_095610_4B_WATCH_2024-04-17 | 095610 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_4B_too_late | False | False |
| TRG_R8L71_C27_095660_STAGE2_LAUNCH_PRICED_IN | 095660 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_false_positive | False | False |
| R8L14_T03_095660_STAGE2_ACTIONABLE_LIES_OF_P_RELEASE | 095660 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_false_positive | False | False |
| TRG_R8L78-C27-095660-NEOWIZ-GAME-IP-THEME-FADE | 095660 | C27_CONTENT_IP_GLOBAL_MONETIZATION | C27 should not treat game-IP or PC/console title beta as durable Stage2 unless user retention, live-ops, revenue rank, content pipeline and margin bridge are visible. Neowiz had a brief MFE and then a large drawdown, making it a local 4B-watch boundary rather than durable Green. | True | True |
| TRG_NEOWIZ_2023_LIES_OF_P_LAUNCH_2023_09_19 | 095660 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_false_positive | False | False |
| R8L14_T04_095660_4C_THESIS_BREAK_WATCH | 095660 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_4C_too_late | False | False |
| R13L14_G02_06_095660_R8L14_T03_095660_STAGE2_ACTIONABLE_LIES_OF_P_RELEASE | 095660 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_false_positive | False | False |
| TRG_R12L80-C31-095720-WOONGJIN-THINKBIG-EDTECH-POLICY-FADE | 095720 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should not treat education/AI textbook policy beta as durable Stage2 unless direct beneficiary mapping, procurement timing, paid user conversion, revenue and margin bridge are visible. Woongjin Thinkbig had a small policy MFE and then a deep MAE path. | True | True |
| R11L13_C31_096530_20200218_T1 | 096530 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_correct | True | False |
| SEEGENE_4B_2020_07_10_PRICE_ONLY_LOCAL_PEAK | 096530 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_4B_too_early | False | False |
| R13L15_SEEGENE_4B_2020_07_10_PRICE_ONLY_LOCAL_PEAK | 096530 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_early | False | False |
| R3L70_C13_096770_T1_STAGE2_ACTIONABLE_BLUEOVAL_SK_LOAN | 096770 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_false_positive | False | False |
| TRG_R3L14_C13_SKI_20230726_STAGE2_THEME_CAPPED | 096770 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_false_positive | False | False |
| TRG_R1L73-C01-097230-HJSC-ORDER_BETA_WEAK_MARGIN_CONVERSION | 097230 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | C01 should not treat shipbuilding/construction order beta as Stage2 unless backlog quality and margin conversion are explicit. HJ Heavy produced a short MFE but later opened drawdown, making it a false Stage2 / local 4B-watch candidate. | True | True |
| TRG_R1L73-C01-097230-HJSC-ORDER_BETA_WEAK_MARGIN_CONVERSION | 097230 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | C01 should not treat shipbuilding/construction order beta as Stage2 unless backlog quality and margin conversion are explicit. HJ Heavy produced a short MFE but later opened drawdown, making it a false Stage2 / local 4B-watch candidate. | True | True |
| R5L16-C18-097950-T1 | 097950 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | False | False |
| TRG_R5L79-C18-097950-CJ-CHEILJEDANG-KFOOD-GLOBAL-CHANNEL-REORDER | 097950 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | C18 should allow K-food/global food positives when overseas channel reorder, distribution expansion, volume growth, price/mix and margin bridge are visible. CJ CheilJedang produced strong MFE with bounded entry-basis MAE, but later drawdown means channel/revenue/margin evidence must refresh. | True | True |
| R5L11-C18-004-S2A-2024-05-17 | 097950 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive_if_promoted_yellow | False | False |
| TRG_R5L77-C18-097950-CJ-CHEILJEDANG-KFOOD-CHANNEL-MARGIN-LIFECYCLE | 097950 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | C18 should preserve large-cap food export/channel positives when global channel reorder, product mix, price-cost spread and margin bridge are visible. CJ CheilJedang produced moderate MFE with controlled MAE, then faded; it should be lifecycle-managed rather than treated as permanent Green. | True | True |
| R5L12_C18_CJFOOD_T2_REJECT_20230510 | 097950 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | False | False |
| R5L15-C18-097950-T1 | 097950 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | False | False |
| R5L15-C18-097950-T1 | 097950 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | False | False |
| R2L10_C08_MICROCONTACT_T1 | 098120 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_false_positive | False | False |
| T_R2L14_098120_STAGE2A_20240122 | 098120 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_false_positive | False | False |
| TRG_R2L78-C08-098120-MICROCONTACTSOL-IC-SOCKET-CUSTOMER-QUALITY-FADE | 098120 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | C08 should not treat IC-socket/test-parts exposure as durable Stage2 unless customer quality, socket demand, order visibility and margin bridge refreshes. Micro Contact Solution had limited MFE and then a large MAE drawdown. | True | True |
| TRG_R2L81-C08-098120-MICROCONTACTSOL-TEST-SOCKET-THEME-FADE | 098120 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | C08 should not treat IC/test-socket theme beta as durable Stage2 unless customer quality, reorder cadence, delivery/revenue and margin bridge are visible. Micro Contact Solution had only small early MFE and then severe MAE. | True | True |
| R13L10_X02_098120_Stage2-Actionable_candidate_rejected | 098120 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| C25_R13L33_004_T2_4C_PROTECTION | 099190 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_4C_too_late | False | False |
| R7L13-C25-099190-T1-CGM-STAGE2-20230718 | 099190 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive | False | False |
| C25_R13L33_004_T1_STAGE2_ACTIONABLE | 099190 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive | False | False |
| TRG_R7L75-C25-099190-ISENS-CGM-REIMBURSEMENT-ADOPTION-BETA-FADE | 099190 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | C25 should not treat CGM/reimbursement or launch attention as durable Stage2 unless adoption, prescription refill, reimbursement coverage, utilization and margin evidence refreshes. i-SENS had only small initial MFE and then severe MAE/drawdown. | True | True |
| TRG_R7L77-C25-099190-ISENS-CGM-REIMBURSEMENT-EXPORT-BETA-FADE | 099190 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | C25 should not treat CGM/reimbursement or diabetes-device theme beta as durable Stage2 unless adoption, reimbursement coverage, distributor sell-through, export reorder and margin bridge are visible. i-SENS had only a small early MFE and then a high-MAE drawdown path. | True | True |
| TRG_R7L79-C25-099190-ISENS-CGM-REIMBURSEMENT-EXPORT-THEME-FADE | 099190 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | C25 should not treat CGM reimbursement/export theme beta as durable Stage2 unless reimbursement coverage, prescription/adoption, distributor revenue, recurring consumables and margin bridge are visible. i-SENS produced only small early MFE and then a deep MAE path. | True | True |
| None | 099190 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | None | True | True |
| R13_CROSS_099190_2024-02-01_Stage2-FalsePositive_/_CGMReimbursementLaunchBeta | 099190 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | None | True | True |
| TRG_R1L77-C01-100090-SK-OCEANPLANT-OFFSHORE-ORDERBOOK-BETA-FADE | 100090 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | C01 should not treat offshore plant / orderbook beta as durable Stage2 unless project award, backlog conversion, delivery schedule, utilization and margin bridge are visible. SK Oceanplant had only small MFE and then a large MAE drawdown, making it local 4B-watch rather than a backlog Green. | True | True |
| R11L15-C31-100130-S2A-20220816 | 100130 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| R13L15_X_TRIG_R11L15-C31-100130-S2A-20220816 | 100130 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R1L12_C04_100840_CZECH_HEAT_EXCHANGER_SUPPLY_CHAIN_STAGE2_ACTIONABLE | 100840 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_too_late | False | False |
| R1L12_C04_100840_CZECH_HEAT_EXCHANGER_SUPPLY_CHAIN_LOCAL_4B_OVERLAY | 100840 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | current_profile_too_late | False | False |
| R13L12_REDTEAM__R1L12_C04_100840_CZECH_HEAT_EXCHANGER_SUPPLY_CHAIN_STAGE2_ACTIONABLE | 100840 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_too_late | False | False |
| TRG_R1L82-C03-103140-POONGSAN-AMMO-EXPORT-BACKLOG-MARGIN | 103140 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | C03 should protect defense/ammunition positives only when export backlog, customer country/program, delivery schedule, metal spread, revenue recognition and margin bridge are visible. Poongsan produced a very large MFE with shallow entry-basis MAE, but post-peak drawdown requires lifecycle 4B if backlog/margin evidence fades. | True | True |
| TRG_R11L79-C03-103140-POONGSAN-AMMO-EXPORT-DEMAND-BACKLOG | 103140 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | C03 should preserve ammo/munitions positives when defense export demand, backlog visibility, order/shipment cadence, raw-material spread and margin bridge are visible. Poongsan produced a very large MFE with bounded entry-basis MAE, but post-peak drawdown requires lifecycle management. | True | True |
| R13L26_C15_001_T1_STAGE2_ACTIONABLE | 103140 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_missed_structural | False | False |
| R4L12_C15_103140_T1 | 103140 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_missed_structural | False | False |
| R13L26_C15_001_T2_STAGE4B_WATCH | 103140 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_4B_too_early | False | False |
| TRIG_R1L13_C02_ILJIN_POST_CA_STAGE2_20240214 | 103590 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_missed_structural | False | False |
| TRG_R1L78-C02-103590-ILJIN-ELECTRIC-POWER-CABLE-TRANSFORMER-POST-CA | 103590 | C02_POWER_GRID_DATACENTER_CAPEX | C02 should allow power cable/transformer names when datacenter/grid capex maps to order backlog, delivery slots, ASP/copper pass-through and margin bridge. Iljin Electric produced very large MFE after the 2024-02-13 corporate-action candidate; runtime promotion requires post-CA continuity validation and source repair. | True | True |
| R13L13_X_TRIG_R1L13_C02_ILJIN_POST_CA_STAGE2_20240214 | 103590 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_missed_structural | False | False |
| TRIG_R1L13_C02_ILJIN_POST_CA_STAGE2_20240214 | 103590 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_missed_structural | False | False |
| C21-KB-S2A-20240201 | 105560 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_late | False | False |
| R6L15-C21-KB-20240208-S2A | 105560 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_late | False | False |
| R6L15-C21-KB-20240208-S2A | 105560 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_late | False | False |
| R6L14_T002_KB_STAGE2_VALUEUP | 105560 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_late | False | False |
| TRG_R6L12_KB_STAGE2_20240226 | 105560 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_late | False | False |
| KB-C21-S2A-20240226 | 105560 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_late | False | False |
| R6L10-C21-KBFG-T01 | 105560 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_missed_structural | False | False |
| R6L11_T01_KB_20240226_STAGE2_ACTIONABLE_VALUEUP_CAPITAL_RETURN | 105560 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_late | False | False |
| T_KBFG_2025_04_25_STAGE2_ACTIONABLE | 105560 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_late | False | False |
| R6L32-C21-KBFG-GREEN-2024-03-14 | 105560 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_late | False | False |
| R13L30_C21_KB_GREEN_20240426 | 105560 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_late | False | False |
| R13L25_C21_KB_105560_GREEN_20240724 | 105560 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_late | False | False |
| C21-KB-S3Y-20240426 | 105560 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_late | False | False |
| R6L11_T01B_KB_20240314_PRICE_ONLY_LOCAL_4B_TOO_EARLY | 105560 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_4B_too_early | False | False |
| R13L30_C21_KB_4B_20241025 | 105560 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_4B_too_late | False | False |
| R6L13_C21_KB_T02_4B_LOCAL_OVERHEAT_20241025 | 105560 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_4B_too_early | False | False |
| TRG_R6L15_KB_20241025_4B_LOCAL_OVERLAY | 105560 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_4B_too_early | False | False |
| R6L45_T02_KBFG_LOCAL_4B_STRESS | 105560 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_4B_too_early | False | False |
| TRG_R6L12_KB_4B_20241025 | 105560 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_4B_too_late | False | False |
| C21-KB-4B-20241025 | 105560 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_4B_too_late | False | False |
| KB-C21-4B-20241025 | 105560 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_4B_too_early | False | False |
| TR_R11L13_KB_VALUEUP_STAGE2A_20240226 | 105560 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_missed_structural | False | False |
| R13L15_X_TRIG_R6L15-C21-KB-20240208-S2A | 105560 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_too_late | False | False |
| R13L11_REDTEAM__R6L11_T01_KB_20240226_STAGE2_ACTIONABLE_VALUEUP_CAPITAL_RETURN | 105560 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_too_late | False | False |
| R13L11_REDTEAM__R6L11_T01B_KB_20240314_PRICE_ONLY_LOCAL_4B_TOO_EARLY | 105560 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_early | False | False |
| R13L13_X_R6L13_C21_KB_T02_4B_LOCAL_OVERHEAT_20241025 | 105560 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_early | False | False |
| R6L13_C21_KB_T02_4B_LOCAL_OVERHEAT_20241025 | 105560 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_early | False | False |
| R13L12_FP_X02_105560_Stage2-Actionable_2024-02-26 | 105560 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_too_late | False | False |
| R5L12_T02_HANSAE_20210528_4B_CHANNEL_INVENTORY_OVERHEAT | 105630 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_4B_too_late | False | False |
| R5L12_T02_HANSAE_20210528_4B_CHANNEL_INVENTORY_OVERHEAT | 105630 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_4B_too_late | False | False |
| T_C19_HANSAE_2022Q1_STAGE2_FALSE_POSITIVE | 105630 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_false_positive | False | False |
| T_HANSAE_20220517_FALSE_STAGE2 | 105630 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_false_positive | False | False |
| R5L31_T05_HANSAE_4B_INVENTORY_RERATING_OVERHEAT_20231031 | 105630 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_4B_too_late | False | False |
| T_HANSAE_20220519_4C_DESTOCKING_BREAK | 105630 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_4C_too_late | False | False |
| T_C19_HANSAE_2022_4C_INVENTORY_DESTOCKING | 105630 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_4C_too_late | False | False |
| R13L14_X_TRIG_T_HANSAE_20220517_FALSE_STAGE2 | 105630 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L14_X_TRIG_T_HANSAE_20220519_4C_DESTOCKING_BREAK | 105630 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4C_too_late | False | False |
| TRG_R1L75-C04-105840-WOOJIN-INSTRUMENTATION-POLICY-PROXY-FADE | 105840 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | C04 should not treat nuclear instrumentation or policy proxy beta as durable Stage2 unless project scope, order, customer, safety instrumentation, replacement cycle or margin bridge is verified. Woojin produced an early pop but later opened severe MAE and post-peak drawdown. | True | True |
| R10L14_C30_109610_T_STAGE2_20240327 | 109610 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_4B_too_late | False | False |
| T-C19-110790-2022-05-16-4B | 110790 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_4B_too_late | False | False |
| R5L12_T03_YOUNGONE_20230515_STAGE2_ACTIONABLE_REORDER | 111770 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_too_late | False | False |
| R5L12_T03_YOUNGONE_20230515_STAGE2_ACTIONABLE_REORDER | 111770 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_too_late | False | False |
| T-C19-111770-2022-08-16-S2A | 111770 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_too_late | False | False |
| R5L71-C19-001-S2A | 111770 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_missed_structural | True | False |
| TRG_R5L78-C19-111770-YOUNGONE-APPAREL-OEM-INVENTORY-MARGIN-FADE | 111770 | C19_BRAND_RETAIL_INVENTORY_MARGIN | C19 should not treat apparel OEM or restocking exposure as durable Stage2 unless customer reorder, inventory normalization, shipment cadence, FX/cost spread and margin bridge refreshes. Youngone had a tradable early MFE, then a large drawdown into the spring/summer window. | True | True |
| None | 111770 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | True | True |
| R13_CROSS_111770_2024-02-01_Stage2-FalsePositive_/_InventoryDestockingWatch | 111770 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | True | True |
| R5L71-C19-004-4B | 111770 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_4B_too_late | True | False |
| TRG_WEMADE_2021_MIR4_WEMIX_STAGE2_2021_10_14 | 112040 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_4B_too_late | False | False |
| R8L31_C27_WEMADE_P2E_TOKENIZED_IP_20211119 | 112040 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_false_positive | False | False |
| R8L31_C27_WEMADE_4C_TOKEN_BREAK_20220210 | 112040 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_4C_too_late | False | False |
| R11L15-C31-112610-S2A-20220816 | 112610 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_missed_structural | False | False |
| TR_R13L29_CSW_STAGE2_20220816 | 112610 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_too_late | False | False |
| TR_R13L29_CSW_GREEN_20221116 | 112610 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_too_late | False | False |
| TR_R13L29_CSW_4B_20230424 | 112610 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_4B_too_late | False | False |
| R13L15_X_TRIG_R11L15-C31-112610-S2A-20220816 | 112610 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_missed_structural | False | False |
| R12L14C31_114090_T_STAGE2_20230810 | 114090 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| R12L14C31_114090_T_4B_20230911 | 114090 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_4B_too_late | False | False |
| R13L14_X_TRIG_R12L14C31_114090_T_STAGE2_20230810 | 114090 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L14_X_TRIG_R12L14C31_114090_T_4B_20230911 | 114090 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late | False | False |
| TRG_R3L82-C11-114190-KANGWON-ENERGY-BATTERY-MATERIAL-EQUIPMENT-THEME-FADE | 114190 | C11_BATTERY_ORDERBOOK_RERATING | C11 should not treat battery material/equipment theme beta as durable orderbook rerating unless direct customer order, material supply volume, delivery, revenue and margin bridge are visible. Kangwon Energy had strong early MFE but then high MAE and post-peak drawdown. | True | True |
| TRG_R11L80-C32-115390-LOCKNLOCK-TENDER-PRICE-CAP-DELISTING | 115390 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should distinguish tender-offer price-cap trades from open-ended governance rerating. LocknLock was anchored by a tender/de-listing style price cap and later became inactive_or_delisted_like, so runtime ingestion requires status validation. | True | True |
| TRG_R12L76-C32-115390-LOCKNLOCK-VOLUNTARY-DELISTING-TENDER-FLOOR | 115390 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should preserve tender-floor minority-economics positives when the listed minority shareholder is the direct beneficiary of a tender/voluntary-delisting floor. Lock&Lock showed a controlled-MAE tender rerating and then price pinning near the offer floor; C32 should treat this as event-floor lifecycle, not perpetual operating Stage2. | True | True |
| TR_R11L11_DAESUNG_STAGE2_2024_06_03 | 117580 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| TRG_R12L79-C31-117580-DAESUNG-ENERGY-GAS-POLICY-THEME-BETA | 117580 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should not treat city-gas or energy policy/geopolitical beta as durable Stage2 unless tariff formula, direct beneficiary mapping, volume, cost pass-through, earnings and margin bridge are visible. Daesung Energy produced tradable MFE but also a drawdown path; without direct-economics proof it should be local 4B-watch rather than Green. | True | True |
| TR-C29-MOTREX-S2VOL-20230412 | 118990 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| TR-C29-MOTREX-S2VOL-20230412 | 118990 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| TRG_R12L76-C32-119860-CONNECTWAVE-TENDER-CAP-NO-FURTHER-GREEN | 119860 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should distinguish tender-floor tradability from ongoing rerating. Connectwave produced a large controlled-MAE move into the tender/floor region and then pinned near the floor, so it is a good counterexample against treating tender-floor MFE as permanent Green. | True | True |
| TRG_R4L76-C17-120110-KOLON-INDUSTRIES-CHEMICAL-MATERIAL-SPREAD-FADE | 120110 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | C17 should not treat industrial chemical/material spread beta as durable Stage2 unless volume, product mix, price-cost spread and margin bridge are visible. Kolon Industries had very limited MFE and then a persistent drawdown, so it is a local 4B-watch row rather than a spread-cycle Green. | True | True |
| TRG_R4L73-C17-120110-KOLONIND-INDUSTRIAL-MATERIAL-SPREAD-FADE | 120110 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | C17 industrial materials should require spread-to-margin refresh. 코오롱인더 produced an initial MFE on industrial-material optimism, but later MAE and drawdown widened; this supports local 4B-watch unless aramid/tire-cord/film margin evidence refreshes. | True | True |
| TRG_R4L73-C17-120110-KOLONIND-INDUSTRIAL-MATERIAL-SPREAD-FADE | 120110 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | C17 industrial materials should require spread-to-margin refresh. 코오롱인더 produced an initial MFE on industrial-material optimism, but later MAE and drawdown widened; this supports local 4B-watch unless aramid/tire-cord/film margin evidence refreshes. | True | True |
| TRG_R3L74-C11-121600-NANO-CNT-MATERIAL-ORDERBOOK-BRIDGE | 121600 | C11_BATTERY_ORDERBOOK_RERATING | C11 should include battery material orderbook rerating when CNT additive capacity, customer qualification, order visibility and margin bridge are visible. Nano New Materials had a strong event-window MFE, but the later 2024 collapse shows lifecycle local 4B is necessary if customer/order evidence stops refreshing. | True | True |
| TRG_R3L74-C11-121600-NANO-CNT-MATERIAL-ORDERBOOK-BRIDGE | 121600 | C11_BATTERY_ORDERBOOK_RERATING | C11 should include battery material orderbook rerating when CNT additive capacity, customer qualification, order visibility and margin bridge are visible. Nano New Materials had a strong event-window MFE, but the later 2024 collapse shows lifecycle local 4B is necessary if customer/order evidence stops refreshing. | True | True |
| TRG_R3L78-C12-121600-NANO-CNT-CUSTOMER-CALLOFF-LIFECYCLE | 121600 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | C12 should allow battery-material positives when customer contract visibility maps to call-off volume, capacity absorption, shipment cadence and margin bridge. Nano New Material produced large MFE with controlled early MAE, but the later post-peak drawdown requires lifecycle local 4B if customer call-off or margin evidence fades. | True | True |
| TRG_R3L76-C13-121600-NANOSIN-CNT-CONDUCTIVE-ADDITIVE-US-UTILIZATION | 121600 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | C13 should include CNT/conductive additive suppliers only when US/local supply, customer ramp, utilization and margin bridge is visible. Nano New Material produced strong early MFE, but the later utilization/demand drawdown means the signal must be lifecycle-managed and share-count validated. | True | True |
| YG_4C_20230607 | 122870 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_4C_too_late | False | False |
| YG_STAGE2_20230512 | 122870 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_4C_too_late | False | False |
| R8L14_C27_YG_T1_STAGE2A_20230512 | 122870 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_4B_too_late | False | False |
| R8L11-C27-YG-T1 | 122870 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_4B_too_late | False | False |
| R8L14_C27_YG_T2_4B_CONTRACT_OVERHANG_20230921 | 122870 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_4B_too_late | False | False |
| R8L11-C27-YG-T2 | 122870 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_4B_too_late | False | False |
| R13L14_X_TRIG_R8L14_C27_YG_T1_STAGE2A_20230512 | 122870 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late | False | False |
| R13L14_X_TRIG_R8L14_C27_YG_T2_4B_CONTRACT_OVERHANG_20230921 | 122870 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late | False | False |
| R10L14_C30_123890_T_STAGE2_20240327 | 123890 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive | False | False |
| TRG_R1L81-C04-126720-SUSAN-INDUSTRIES-NUCLEAR-OM-PROJECT-BRIDGE | 126720 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | C04 should allow nuclear O&M/maintenance positives when policy attention maps to maintenance project orderbook, outage/regular-maintenance demand, revenue recognition and margin bridge. Susan Industries had controlled entry-basis MAE and moderate MFE, so it should not be overblocked after source repair. | True | True |
| R7L16_C23_128940_STAGE3_APPROVAL_TOO_EARLY_2022_09_13 | 128940 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_too_early | False | False |
| TRG_R1L75-C04-130660-KEPCO-INDUSTRIAL-NUCLEAR-SERVICE-PROJECT-BRIDGE | 130660 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | C04 should allow Stage2 when nuclear policy attention is tied to actual service/O&M/project scope, operating contract visibility and margin bridge. KEPCO Industrial produced very high MFE with controlled entry-basis MAE, but post-peak drawdown requires lifecycle local 4B if project-scope evidence fades. | True | True |
| R2L11_C08_131290_STAGE2_20240424 | 131290 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_too_early | False | False |
| R2L11_T02B_TSE_LATE_GREEN_4B_OVERLAY | 131290 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_too_late | False | False |
| R2L11_C08_131290_GREEN_20240426 | 131290 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_too_early | False | False |
| R2L14_C09_131290_TSE_LATE_GREEN_BLOWOFF | 131290 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_too_late | False | False |
| R13L14_X_TRIG_R2L14_C09_131290_TSE_LATE_GREEN_BLOWOFF | 131290 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_too_late | False | False |
| R13L39_C28_131370_STAGE2_20200217 | 131370 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_4B_too_late | False | False |
| TR-C28-131370-S2-2020-02-18 | 131370 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_4B_too_late | False | False |
| R8L10_C28_TRG_005A_RSUPPORT_STAGE2_ACTIONABLE_2020_03_11 | 131370 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_4B_too_late | False | False |
| R13L39_C28_131370_4B_20200828 | 131370 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_4B_too_late | False | False |
| TR-C28-131370-4B-2020-08-28 | 131370 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_4B_too_late | False | False |
| TRG_R11L75-C31-133750-MEGA-MD-MEDQUOTA-POLICY-PROXY-FADE | 133750 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should not treat medical-school quota policy education-proxy spikes as durable Stage2 unless paid enrollment, course demand, retention or margin bridge is visible. MegaMD had a small MFE and then a deep MAE/drawdown. | True | True |
| R13L15_X_TRIG_TR_R12L15_C31_133750_STAGE2_20200224 | 133750 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| C28_WINS_2020_STAGE2A_2020-04-16 | 136540 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_too_late | False | False |
| None | 136540 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | None | True | True |
| R13_CROSS_136540_2024-04-11_Stage2-Actionable-SecurityMaintenanceRetention | 136540 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | None | True | True |
| TRG_R8L79-C28-136540-WINS-SECURITY-CONTRACT-RETENTION-DEFENSIVE | 136540 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | C28 should allow defensive security software positives when maintenance renewal, public/enterprise customer retention, recurring revenue and margin bridge are visible. Wins had bounded entry-basis MAE and later recovery MFE; it is Stage2-Yellow only after source repair, not a security theme blowoff. | True | True |
| C28_WINS_2020_GREEN_2020-09-11 | 136540 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_too_late | False | False |
| TRG_R3L74-C11-137400-PNT-BATTERY-EQUIPMENT-ORDERBOOK-BRIDGE | 137400 | C11_BATTERY_ORDERBOOK_RERATING | C11 should allow Stage2 when equipment orderbook and delivery-slot visibility convert into margin/revision bridge. PNT produced very high MFE after the trigger, but later post-peak drawdown and an in-window share-count change require lifecycle local 4B and coding-agent validation. | True | True |
| TRG_R3L74-C11-137400-PNT-BATTERY-EQUIPMENT-ORDERBOOK-BRIDGE | 137400 | C11_BATTERY_ORDERBOOK_RERATING | C11 should allow Stage2 when equipment orderbook and delivery-slot visibility convert into margin/revision bridge. PNT produced very high MFE after the trigger, but later post-peak drawdown and an in-window share-count change require lifecycle local 4B and coding-agent validation. | True | True |
| TRG_R3L82-C11-137400-PNT-BATTERY-EQUIPMENT-ORDERBOOK-LIFECYCLE | 137400 | C11_BATTERY_ORDERBOOK_RERATING | C11 should protect battery equipment orderbook positives only when customer orderbook, delivery schedule, capacity utilization, revenue recognition and margin bridge are visible. PNT produced very large MFE with shallow entry-basis MAE, but stock-web shard shows share-count movement and post-peak drawdown requires lifecycle 4B discipline. | True | True |
| R6L13_C21_MERITZ_T01_STAGE2_ACTIONABLE_20230515 | 138040 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_late | False | False |
| R6L14_T001_MERITZ_STAGE2_CAPRETURN | 138040 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_late | False | False |
| R6L13_C21_MERITZ_T2A_20240628 | 138040 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_late | False | False |
| R13L13_X_R6L13_C21_MERITZ_T01_STAGE2_ACTIONABLE_20230515 | 138040 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_too_late | False | False |
| R6L13_C21_MERITZ_T01_STAGE2_ACTIONABLE_20230515 | 138040 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_too_late | False | False |
| R13L13_ACC_X02_138040_20240628 | 138040 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_too_late | False | False |
| TRG_R6L79-C21-138930-BNK-REGIONAL-BANK-VALUEUP-BOUNDARY | 138930 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | C21 should avoid forcing regional-bank value-up rows into 4B when entry-basis MAE is bounded and recovery MFE is meaningful. BNK needs ROE, credit-cost, capital buffer and shareholder-return source repair before Stage2, but price action alone does not support hard local 4B. | True | True |
| R13L30_C21_BNK_POLICY_S2_20240208 | 138930 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_early | False | False |
| TRG_R6L75-C21-138930-BNK-FINANCIAL-REGIONAL-BANK-CAPITAL-RETURN | 138930 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | C21 should keep slower regional-bank capital return winners when ROE stability, dividend path, treasury cancellation and CET1/capital buffer support the rerating. BNK had modest early MFE but a durable low-MAE rerating path; share-count validation remains required. | True | True |
| T-BNK-S2A-20250113 | 138930 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_late | True | True |
| TRG_R6L77-C21-138930-BNK-FINANCIAL-ROE-PBR-CAPITAL-RETURN | 138930 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | C21 should preserve slow regional-financial rerating rows when sustainable ROE, PBR discount, CET1/capital buffer, dividend policy and capital-return bridge are visible. BNK produced slow controlled-MAE MFE and share-count movement that likely relates to capital policy, but runtime promotion requires share-count validation. | True | True |
| R13L30_C21_BNK_YELLOW_20240729 | 138930 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_late | False | False |
| R6L16_T_DGBFG_GOVERNANCE_DISCOUNT_20240226_REP | 139130 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | False | False |
| R6L16_T_DGBFG_4C_WATCH_20240419 | 139130 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_4C_too_late | False | False |
| T_EMART_20210810_FALSE_STAGE2 | 139480 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_false_positive | False | False |
| TRG_R5L74-C19-139480-EMART-GROCERY-TURNAROUND-PRICE-BETA | 139480 | C19_BRAND_RETAIL_INVENTORY_MARGIN | C19 should not treat grocery retail/value-up price beta as durable Stage2 unless inventory turns, SSG/online losses, store traffic and margin bridge improve. E-Mart had early MFE but then opened deep MAE and a large post-peak drawdown, so the first signal should be local 4B-watch rather than Green. | True | True |
| TRG_R5L74-C19-139480-EMART-GROCERY-TURNAROUND-PRICE-BETA | 139480 | C19_BRAND_RETAIL_INVENTORY_MARGIN | C19 should not treat grocery retail/value-up price beta as durable Stage2 unless inventory turns, SSG/online losses, store traffic and margin bridge improve. E-Mart had early MFE but then opened deep MAE and a large post-peak drawdown, so the first signal should be local 4B-watch rather than Green. | True | True |
| TRG_R5L81-C19-139480-EMART-MART-INVENTORY-MARGIN-FADE | 139480 | C19_BRAND_RETAIL_INVENTORY_MARGIN | C19 should not treat mart/value-up or retail restructuring beta as durable Stage2 unless inventory cleanup, online/offline mix, cost control, revenue recovery and margin bridge are visible. E-Mart had a sharp early MFE and then a high-MAE fade. | True | True |
| R13L14_X_TRIG_T_EMART_20210810_FALSE_STAGE2 | 139480 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| TRG_R7L78-C24-141080-LIGACHEM-ADC-DATA-PARTNERING-POST-CA | 141080 | C24_BIO_TRIAL_DATA_EVENT_RISK | C24 should allow ADC/platform positives only when trial-data quality, partner validation, named program visibility, milestone economics and cash runway bridge are visible. LigaChem Bio produced very large MFE after the 2024-04-23 corporate-action/share-count discontinuity; runtime promotion requires post-CA and share-count validation. | True | True |
| TRG_R7L80-C24-141080-LIGACHEM-ADC-POSTCA-DATA-LICENSE-MILESTONE | 141080 | C24_BIO_TRIAL_DATA_EVENT_RISK | C24 should allow ADC platform positives when post-CA continuity, trial data, license economics, milestone runway, partner quality and commercialization bridge are visible. LigaChem Bio produced a large post-CA MFE, but runtime ingestion requires post-CA/name-change validation. | True | True |
| TRG_R7L76-C24-141080-LIGACHEM-ADC-TRIAL-DATA-POST-CA-LIFECYCLE | 141080 | C24_BIO_TRIAL_DATA_EVENT_RISK | C24 should allow ADC-platform trial-data / partner-validation positives only after corporate-action windows are handled. LigaChem Bio had a 2024-04-23 corporate-action candidate, so the post-CA entry is deliberately 2024-04-24; the post-entry path produced very large MFE, but requires source repair and CA validation before runtime promotion. | True | True |
| TRG_R7L74-C24-141080-LCB-ADC-PLATFORM-DATA-DERISKING | 141080 | C24_BIO_TRIAL_DATA_EVENT_RISK | C24 should not treat a biotech data/platform event as instant Green at the first gap, but it should allow delayed Stage2 when clinical/platform derisking and partner validation become real. LigaChem Bio required post-CA validation and later lifecycle 4B after the November peak. | True | True |
| TRG_R7L74-C24-141080-LCB-ADC-PLATFORM-DATA-DERISKING | 141080 | C24_BIO_TRIAL_DATA_EVENT_RISK | C24 should not treat a biotech data/platform event as instant Green at the first gap, but it should allow delayed Stage2 when clinical/platform derisking and partner validation become real. LigaChem Bio required post-CA validation and later lifecycle 4B after the November peak. | True | True |
| R7L26-T003 | 145020 휴젤 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_too_late | False | False |
| R7L11-C23-145020-T1-letybo-fda | 145020 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_missed_structural | False | False |
| R7L12_C23_HUGEL_STAGE2_APPROVAL_2024-03-04 | 145020 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_missed_structural | False | False |
| HUGEL_STAGE2_APPROVAL_2024_03_04 | 145020 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_too_late | False | False |
| R7L26-T003 | 145020 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_too_late | False | False |
| R7L12_C23_HUGEL_4B_POSITIONING_2024-11-06 | 145020 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_4B_too_late | False | False |
| T-C23-HUGEL-4B-20241106 | 145020 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_4B_too_late | False | False |
| R13L15_X_TRIG_T-C23-HUGEL-4B-20241106 | 145020 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late | False | False |
| R7L12_C25_145720_T1_STAGE2 | 145720 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_too_late | False | False |
| C25_R13L33_003_T1_STAGE2_ACTIONABLE | 145720 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_too_early | False | False |
| R7L10_C25_DENTIUM_2023_STAGE3Y | 145720 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_too_early | False | False |
| R7L12_C25_145720_T2_4B_OVERLAY | 145720 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_4B_too_late | False | False |
| TRG_R11L81-C31-159580-ZERO2SEVEN-CHILDCARE-POLICY-THEME-FADE | 159580 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should not treat childcare/low-birth-rate policy beta as durable Stage2 unless direct beneficiary mapping, channel demand, paid conversion, product sell-through, revenue and margin bridge are visible. Zero to Seven had small policy MFE and then a severe MAE path. | True | True |
| TRG_R12L77-C31-159580-ZEROTOSEVEN-LOW-BIRTH-POLICY-THEME-FADE | 159580 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should not treat childcare/low-birth policy beta as durable Stage2 unless direct demand, channel reorder, sell-through and margin evidence refreshes. Zero to Seven had a tradable MFE, but then high MAE and post-peak fade, making it local 4B rather than Green. | True | True |
| C27_160550_20160324_GREEN_FALSE_POSITIVE | 160550 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_false_positive | False | False |
| R4L15_C17_T04_AEKYUNG_20230411_FALSE_GREEN | 161000 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive | False | False |
| R4L15_C17_T04_AEKYUNG_20230411_FALSE_GREEN | 161000 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive | False | False |
| TR-C29-HANKOOKTIRE-S2A-20231101 | 161390 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_missed_structural | False | False |
| TR-C29-HANKOOKTIRE-S2A-20231101 | 161390 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_missed_structural | False | False |
| T_R9L11_161390_STAGE2 | 161390 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_too_late | False | False |
| TRG_R9L73-C29-161390-HANKOOKTIRE-PRICE-MIX-MARGIN-LEVERAGE | 161390 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should include tire price/mix and replacement-demand margin leverage, not only OEM vehicle volume. 한국타이어 produced a strong MFE with controlled early MAE, but later post-peak drawdown means local 4B-watch is needed if margin/mix evidence stops refreshing. | True | True |
| T_C29_161390_S2_20240201 | 161390 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| TRG_R9L73-C29-161390-HANKOOKTIRE-PRICE-MIX-MARGIN-LEVERAGE | 161390 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should include tire price/mix and replacement-demand margin leverage, not only OEM vehicle volume. 한국타이어 produced a strong MFE with controlled early MAE, but later post-peak drawdown means local 4B-watch is needed if margin/mix evidence stops refreshing. | True | True |
| T_C29_161390_S2_20240201 | 161390 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| TRG_R9L77-C29-161390-HANKOOK-TIRE-OE-REPLACEMENT-MIX-MARGIN-FADE | 161390 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should not treat tire/OE/replacement-cycle beta as durable Stage2 unless OE/replacement volume, product mix, raw-material cost spread and margin bridge refreshes. Hankook Tire had a tradable MFE, then opened a high-MAE drawdown path. | True | True |
| TRG_R9L79-C29-161390-HANKOOK-TIRE-MIX-MARGIN-LIFECYCLE | 161390 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 can preserve tire volume/mix positives when OE/replacement demand, product mix, raw-material cost spread, pricing and margin bridge are visible. Hankook Tire produced meaningful MFE, but later high MAE after the peak means the signal must be lifecycle-managed instead of permanent Green. | True | True |
| T_R9L11_161390_4B | 161390 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_4B_too_late | False | False |
| TR-C29-HANKOOKTIRE-4B-20240416 | 161390 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_4B_too_late | False | False |
| C18-R13L44-161890-T1-stage2 | 161890 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_too_late | False | False |
| C18-R13L44-161890-T1-stage2 | 161890 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_too_late | False | False |
| C18-R13L44-161890-T2-green | 161890 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_too_late | False | False |
| C18-R13L44-161890-T2-green | 161890 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_too_late | False | False |
| C18-R13L44-161890-T3-4b | 161890 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_4B_too_early | False | False |
| C18-R13L44-161890-T3-4b | 161890 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_4B_too_early | False | False |
| R5L16_C20_KOLMAR_T2A_20240510 | 161890 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_too_late | False | False |
| R5L12-C20-KOLMAR-S2A-20240513 | 161890 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_too_late | False | False |
| R5L71-C20-02-T1 | 161890 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_4B_too_late | False | False |
| TRG_R2L16_C10_166090_HANA_STAGE2A_20240119 | 166090 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_too_early | False | False |
| TRG_R6L77-C21-175330-JB-FINANCIAL-ROE-PBR-CAPITAL-RETURN | 175330 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | C21 should allow regional-bank value-up positives when PBR discount, sustainable ROE, CET1/capital buffer, dividend/buyback and shareholder-return bridge are visible. JB Financial produced high MFE with essentially no entry-basis MAE; it should be protected after source repair while still requiring lifecycle monitoring if capital-return evidence fades. | True | True |
| TRG_R6L75-C21-175330-JB-FINANCIAL-ROE-CAPITAL-RETURN-BRIDGE | 175330 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | C21 should allow Stage2 when low-PBR/value-up attention connects to durable ROE, payout, treasury cancellation or capital-return bridge. JB Financial produced high MFE with controlled entry-basis MAE; share-count movement should be validated before runtime promotion. | True | True |
| R6L16_T_JBFG_ROE_CAPRETURN_20240226_REP | 175330 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_late | False | False |
| T_JBFG_2025_04_25_STAGE2_ACTIONABLE | 175330 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_late | False | False |
| R13L20-C32-HJKAL-STAGE2-20201116 | 180640 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive | False | False |
| R11L15_C32_HK_180640_T1_KDB_ASIANA_POLICY_STAGE2_FALSE_POSITIVE | 180640 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive | False | False |
| None | 180640 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | None | True | True |
| R13_CROSS_R12L71-C32-180640-HANJINKAL-CONTROL-BATTLE-BLOWOFF_180640_2020-03-27_Stage4B-Local-PriceOnly-GovernanceBlowoff | 180640 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | None | True | True |
| R8L14_C27_CUBE_T1_STAGE2A_20230516 | 182360 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_false_positive | False | False |
| R13L14_X_TRIG_R8L14_C27_CUBE_T1_STAGE2A_20230516 | 182360 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L54_C28_184230_STAGE2A_20210223 | 184230 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_too_late | False | False |
| R13L54_C28_184230_4B_20210617 | 184230 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_4B_too_early | False | False |
| TRG_R1L80-C02-189860-SEOJEON-ELECTRIC-SWITCHGEAR-THEME-BACKLOG-GAP | 189860 | C02_POWER_GRID_DATACENTER_CAPEX | C02 should not treat switchgear/grid/nuclear theme beta as durable Stage2 unless named customer, order backlog, delivery schedule, revenue recognition and margin bridge are visible. Seojeon Electric produced tradable MFE, then a post-peak drawdown, making it local 4B-watch rather than durable Green. | True | True |
| TRG_R8L79-C28-192250-KSIGN-SECURITY-THEME-LOCAL4B-CA-CAVEAT | 192250 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | C28 should not treat security/encryption/authentication theme MFE as durable Stage2 unless contract retention, renewal rate, recurring revenue, public/enterprise customer quality and margin bridge are visible. KSign produced a sharp MFE and then high MAE; 2024-11-01 corporate-action candidate is outside the selected 180D interpretation but must be validated before any extended ingestion. | True | True |
| TRG_R5L73-C18-192820-COSMAX-ODM-GLOBAL-CUSTOMER-REORDER | 192820 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | C18 should reward ODM/customer reorder only when global customer demand and margin conversion are visible. Cosmax shows a strong MFE path with manageable entry-basis MAE, but source repair is required before promotion. | True | True |
| C18-R13L44-192820-T1-stage2 | 192820 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_too_late | False | False |
| C18-R13L44-192820-T1-stage2 | 192820 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_too_late | False | False |
| TRG_R5L73-C18-192820-COSMAX-ODM-GLOBAL-CUSTOMER-REORDER | 192820 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | C18 should reward ODM/customer reorder only when global customer demand and margin conversion are visible. Cosmax shows a strong MFE path with manageable entry-basis MAE, but source repair is required before promotion. | True | True |
| TRG_R5L82-C18-192820-COSMAX-ODM-GLOBAL-CHANNEL-REORDER | 192820 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | C18 should allow global ODM/channel positives when customer mix, export channel sell-through, reorder cadence, capacity utilization, revenue conversion and margin bridge are visible. Cosmax had strong MFE but not without MAE, so source repair is required before Stage2 promotion. | True | True |
| C18-R13L44-192820-T2-green | 192820 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_too_late | False | False |
| C18-R13L44-192820-T2-green | 192820 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_too_late | False | False |
| C18-R13L44-192820-T3-4b | 192820 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_4B_too_early | False | False |
| C18-R13L44-192820-T3-4b | 192820 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_4B_too_early | False | False |
| TRG_R5L80-C20-192820-COSMAX-BEAUTY-ODM-GLOBAL-REORDER-MARGIN | 192820 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | C20 should protect beauty ODM/OEM positives when global channel reorder, customer quality, US/China volume, revenue conversion and margin bridge are visible. Cosmax produced a large MFE but later drawdown means lifecycle 4B is needed if channel/revenue/margin evidence fades. | True | True |
| R5L13_C20_192820_20240513_STAGE2A | 192820 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_too_early | False | False |
| R5L10_T03_COSMAX_STAGE2_ACTIONABLE | 192820 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_too_early | False | False |
| R5L12-C20-COSMAX-S2A-20240513 | 192820 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_too_early | False | False |
| R5L11-C20-COSMAX-STAGE2A-20240514 | 192820 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_too_early | False | False |
| R13L55_192820_STAGE2_20240516 | 192820 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | False | False |
| R13L55_192820_STAGE2_20240516 | 192820 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | False | False |
| R5L71-C20-01-T1 | 192820 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_4B_too_late | False | False |
| R5L11_T02_COSMAX_20230515_STAGE3_YELLOW_ODM_REORDER | 192820 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_too_late | False | False |
| R13L55_192820_YELLOW_20240614 | 192820 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | False | False |
| R13L55_192820_YELLOW_20240614 | 192820 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | False | False |
| R5L71-C20-01-T2 | 192820 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_4B_too_late | False | False |
| R5L71-C20-01-T2 | 192820 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_4B_too_late | False | False |
| R13L11_HIGHMAE_X03_192820_STAGE2A_20240514 | 192820 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_too_early | False | False |
| R8L13_C27_DEVSISTERS_T2_4C_20240704 | 194480 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_4C_too_late | False | False |
| TRG_DEV_2021_COOKIE_RUN_STAGE2_2021_01_21 | 194480 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_too_late | False | False |
| TRG_R8L78-C27-194480-DEVSISTERS-GAME-IP-GLOBAL-MONETIZATION | 194480 | C27_CONTENT_IP_GLOBAL_MONETIZATION | C27 should preserve game-IP monetization positives only when launch/update traction, DAU retention, revenue rank, overseas channel and margin bridge are visible. Devsisters produced very large MFE with controlled entry-basis MAE, but later drawdown requires lifecycle 4B if IP monetization evidence fades. Share-count movement inside the raw shard requires validation. | True | True |
| TRG_R8L76-C27-194480-DEVSISTERS-GAME-IP-GLOBAL-LAUNCH-MONETIZATION | 194480 | C27_CONTENT_IP_GLOBAL_MONETIZATION | C27 should allow game-IP positives when global launch, DAU/MAU, IAP revenue, platform monetization, royalty/licensing and margin bridge are visible. Devsisters produced large MFE but later post-peak drawdown and share-count movement require lifecycle local 4B and validation. | True | True |
| R8L13_C27_DEVSISTERS_T1_STAGE2A_20240626 | 194480 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_false_positive | False | False |
| TRG_R8L80-C27-194480-DEVSISTERS-COOKIE-IP-GLOBAL-LAUNCH-MARGIN | 194480 | C27_CONTENT_IP_GLOBAL_MONETIZATION | C27 should allow game-IP launch/live-ops positives when global launch cadence, user acquisition, sales ranking, revenue conversion and margin bridge are visible. Devsisters produced large MFE, but later drawdown makes lifecycle 4B necessary if post-launch metrics fade. | True | True |
| R13L13_X_R8L13_C27_DEVSISTERS_T2_4C_20240704 | 194480 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4C_too_late | False | False |
| R8L13_C27_DEVSISTERS_T2_4C_20240704 | 194480 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4C_too_late | False | False |
| R13L13_X_R8L13_C27_DEVSISTERS_T1_STAGE2A_20240626 | 194480 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R8L13_C27_DEVSISTERS_T1_STAGE2A_20240626 | 194480 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| TRG_R7L73-C23-195940-HKINNO-KCAB-GLOBAL-COMMERCIALIZATION-RAMP | 195940 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | C23 should distinguish real prescription/export commercialization ramp from pure regulatory excitement. HK inno.N produced an attractive path, but later post-peak drawdown requires local 4B-watch if prescription/partner revenue evidence stops refreshing. | True | True |
| TRG_R7L73-C23-195940-HKINNO-KCAB-GLOBAL-COMMERCIALIZATION-RAMP | 195940 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | C23 should distinguish real prescription/export commercialization ramp from pure regulatory excitement. HK inno.N produced an attractive path, but later post-peak drawdown requires local 4B-watch if prescription/partner revenue evidence stops refreshing. | True | True |
| R7L14-T001 | 196170 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_too_late | False | False |
| R7L11-C23-196170-T1-commercial-optionality | 196170 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_missed_structural | False | False |
| T-196170-2024-02-23-CONTRACT | 196170 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_missed_structural | False | False |
| R7L46-ALT-20240223-S2A | 196170 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_missed_structural | False | False |
| TR_R7L10_196170_2024-02-22_MERCK_EXCLUSIVE_AMENDMENT | 196170 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_too_late | False | False |
| R7L14-T001 | 196170 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_too_late | False | False |
| R7L14-T002 | 196170 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_too_late | False | False |
| R7L14-T002 | 196170 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_too_late | False | False |
| TRG_R7L11_196170_STAGE2_20240223 | 196170 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_too_late | False | False |
| C24-ALTEOGEN-20241120-S2A | 196170 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_too_early | False | False |
| TRG_R1L80-C02-199820-CHEIL-ELECTRIC-POST-CA-SWITCHGEAR-FADE | 199820 | C02_POWER_GRID_DATACENTER_CAPEX | C02 should not treat post-CA switchgear/datacenter theme beta as durable Stage2 unless order backlog, customer quality, delivery schedule, revenue recognition and margin bridge survive the corporate-action reset. Cheil Electric's post-CA path had small MFE and high MAE. | True | True |
| C27_200350_20221125_4B_RATINGS_EVENT_CAP | 200350 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_4B_too_late | False | False |
| C27_200350_20221226_4C_POST_EVENT_FADE | 200350 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_4C_too_late | False | False |
| TRG_R9L80-C29-200880-SEOYON-EHWA-AUTO-INTERIOR-VOLUME-MIX-LIFECYCLE | 200880 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 should preserve auto interior/module positives when customer program volume, product mix, utilization, pricing and margin bridge are visible. Seoyon E-Hwa produced a very large early MFE but later high MAE requires lifecycle local 4B if volume/mix/margin evidence fades. | True | True |
| R13L54_C28_203650_4B_20230310 | 203650 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_4B_too_early | False | False |
| T-C29-HLMANDO-20210108-S2A | 204320 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| R9L33-T003-HLMANDO-STAGE2-FY22 | 204320 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| T_R9L10_204320_STAGE2 | 204320 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | False | True |
| TR_R9L10_204320_S2_20230210 | 204320 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| R9L13_C29_HLMANDO_2023_CUSTOMER_WIN_FALSE_POSITIVE | 204320 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| TR-C29-HLMANDO-GREEN-20240605 | 204320 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| R9L10-C29-HLMANDO-FALSEGREEN-20240605 | 204320 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| R9L33-T004-HLMANDO-4B-LOCALPEAK | 204320 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_4B_too_late | False | False |
| R9L10-C29-HLMANDO-4C-WATCH-20240909 | 204320 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_4C_too_late_if_not_flagged | False | False |
| TRG_R8L76-C27-206560-DEXTER-VFX-CONTENT-PRODUCTION-PIPELINE | 206560 | C27_CONTENT_IP_GLOBAL_MONETIZATION | C27 should not only include idol/label/game names; VFX/content production pipelines can be C27 when order backlog, production schedule, global IP service revenue and margin bridge are visible. Dexter produced controlled-MAE follow-through, but needs non-price order/pipeline evidence before runtime promotion. | True | True |
| TRG_R7L75-C25-206640-BODITECH-IVD-EXPORT-CHANNEL-MARGIN-BRIDGE | 206640 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | C25 should allow Stage2 when IVD device export/channel reorder converts into installed base, reagent pull-through, utilization and margin bridge. Boditech Med produced high MFE with controlled entry-basis MAE, but later drawdown requires lifecycle local 4B if export/reagent bridge fades. | True | True |
| TRG_R8L76-C27-207760-MRBLUE-WEBTOON-IP-THEME-SPIKE-FADE | 207760 | C27_CONTENT_IP_GLOBAL_MONETIZATION | C27 should not treat webtoon/IP/platform theme spikes as durable Stage2 unless paid-content revenue, subscriber/traffic conversion, global distribution, licensing and margin bridge are visible. Mr. Blue produced large MFE but later collapsed into a high-MAE local 4B path; share-count movement requires validation. | True | True |
| R7L12_C25_214150_T1_STAGE2 | 214150 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_too_late | False | False |
| R7L12_C25_214150_T2_GREEN_COMPARISON | 214150 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_too_late | False | False |
| R7L10_C25_CLASSYS_2024_4B | 214150 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_4B_too_early | False | False |
| FSN_STAGE2_THEME_SPIKE_20211110 | 214270 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| TRG_C26_FSN_2024_02_01_STAGE2A | 214270 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| TRG_R8L73-C26-214270-FSN-DIGITAL-ADTECH-PRICE-BETA-LOCAL4B | 214270 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | C26 should not treat digital-adtech or platform theme MFE as durable Stage2 unless recurring ad revenue, take-rate, client retention and margin conversion are visible. FSN had a sharp MFE but later severe MAE and post-peak drawdown. | True | True |
| TRG_R8L73-C26-214270-FSN-DIGITAL-ADTECH-PRICE-BETA-LOCAL4B | 214270 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | C26 should not treat digital-adtech or platform theme MFE as durable Stage2 unless recurring ad revenue, take-rate, client retention and margin conversion are visible. FSN had a sharp MFE but later severe MAE and post-peak drawdown. | True | True |
| FSN_4B_THEME_BLOWOFF_20211230 | 214270 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_4B_too_late | False | False |
| TRG_R8L73-C26-214320-INNOCEAN-AD-AGENCY-OPERATING-LEVERAGE-WEAK | 214320 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | C26 should distinguish ad-agency campaign stability from true platform operating leverage. Innocean had limited MFE and later MAE; without client-budget, digital mix or margin revision evidence it should remain RiskWatch / no durable Green rather than Stage2. | True | True |
| TRG_R8L73-C26-214320-INNOCEAN-AD-AGENCY-OPERATING-LEVERAGE-WEAK | 214320 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | C26 should distinguish ad-agency campaign stability from true platform operating leverage. Innocean had limited MFE and later MAE; without client-budget, digital mix or margin revision evidence it should remain RiskWatch / no durable Green rather than Stage2. | True | True |
| TRG_R5L73-C18-214420-TONYMOLY-KBEAUTY-EXPORT-CHANNEL-REORDER | 214420 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | C18 should allow Stage2 when small-brand export/channel reorder connects to operating leverage, but should add local 4B-watch after a blowoff if reorder evidence stops refreshing. | True | True |
| TRG_R5L73-C18-214420-TONYMOLY-KBEAUTY-EXPORT-CHANNEL-REORDER | 214420 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | C18 should allow Stage2 when small-brand export/channel reorder connects to operating leverage, but should add local 4B-watch after a blowoff if reorder evidence stops refreshing. | True | True |
| TRG_R5L82-C18-214420-TONYMOLY-KBEAUTY-BRAND-THEME-SPIKE-FADE | 214420 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | C18 should not treat K-beauty brand/channel theme spikes as durable Stage2 unless export sell-through, channel restocking, repeat order cadence, revenue and margin bridge are visible. TonyMoly had large MFE but also sharp post-peak fade, so it is a theme-spike/local-4B boundary until direct channel proof is repaired. | True | True |
| TRG_R5L80-C20-214420-TONYMOLY-BEAUTY-BRAND-GLOBAL-CHANNEL-LIFECYCLE | 214420 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | C20 should allow beauty-brand positives when global channel reorder, offline/online sell-through, product mix, revenue and margin bridge are visible. TonyMoly produced a very large MFE, but its post-peak drawdown requires lifecycle local 4B if sell-through or margin proof fades. | True | True |
| R5L10_T05_TONYMOLY_PRICE_ONLY_LOCAL_4B_20240614 | 214420 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_4B_too_late | False | False |
| TRG_R7L77-C25-214450-PHARMARESEARCH-AESTHETIC-MEDDEVICE-EXPORT-MARGIN | 214450 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | C25 should allow aesthetic/regenerative medical-device positives when export channel reorder, approval/registration visibility, pricing and margin bridge are visible. PharmaResearch produced very large MFE with almost no entry-basis MAE, but later price pinning and post-peak drawdown require lifecycle local 4B if export/margin evidence fades. | True | True |
| TRG_R7L75-C25-214680-DRTECH-XRAY-DETECTOR-EXPORT-ORDER-BETA-FADE | 214680 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | C25 should not treat X-ray detector/export/OEM order beta as durable Stage2 unless named export orders, OEM channel expansion, reimbursement or margin bridge is visible. DRTech had tradable MFE but later drawdown opened enough to require local 4B-watch. | True | True |
| TRG_R7L76-C24-215600-SILLAJEN-ONCOLOGY-TRIAL-DATA-POST-CA-BETA-FADE | 215600 | C24_BIO_TRIAL_DATA_EVENT_RISK | C24 should not treat oncology-trial or financing/post-CA bio beta as durable Stage2 unless endpoint quality, safety, regulatory path, financing runway and commercialization bridge are visible. SillaJen had only a small MFE after the post-CA entry and then opened a high-MAE decline. | True | True |
| R7L15-C24-215600-T1-PRE-FUTILITY-FALSE-GREEN-20190801 | 215600 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_false_positive | False | False |
| R7L15-C24-215600-T1-PRE-FUTILITY-FALSE-GREEN-20190801 | 215600 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_false_positive | False | False |
| TRG_R13L32_215600_4C_20190802 | 215600 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_4C_too_late | True | False |
| R7L15-C24-215600-T2-HARD-4C-FUTILITY-20190802 | 215600 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_4C_too_late | False | False |
| R7L15-C24-215600-T2-HARD-4C-FUTILITY-20190802 | 215600 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_4C_too_late | False | False |
| R13L15_R7L15_C24_215600_T1_PRE_FUTILITY_FALSE_GREEN_20190801 | 215600 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L15_R7L15_C24_215600_T2_HARD_4C_FUTILITY_20190802 | 215600 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4C_too_late | False | False |
| INCROSS_STAGE2_TDEAL_ADTECH_20201106 | 216050 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_too_late | False | False |
| C26_INCROSS_T1_STAGE2_20210208 | 216050 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| R8L13_C26_INCROSS_FALSE_2023-07-10 | 216050 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| R8L13_C26_INCROSS_FALSE_2023-07-10 | 216050 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| INCROSS_GREEN_RECOGNITION_20210215 | 216050 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_too_late | False | False |
| TRG_INCROSS_2021_ADTECH_RECOVERY_FALSE_POSITIVE_2021_02_10 | 216050 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| C26_INCROSS_T2_YELLOW_20210329 | 216050 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_too_early | False | False |
| R12L10C31_218150_T1 | 218150 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| R12L11_C31_218150_GREEN_20220322 | 218150 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_too_late | False | False |
| R12L13_C31_218150_FEED_ADDITIVE_DIRECT_T_4B_20220322 | 218150 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_4B_too_early | False | False |
| R13L10_T12_MIRAE_LATE_EVENT_HIGH_MAE | 218150 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L13_X_R12L13_C31_218150_FEED_ADDITIVE_DIRECT_T_4B_20220322 | 218150 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_early | False | False |
| R12L13_C31_218150_FEED_ADDITIVE_DIRECT_T_4B_20220322 | 218150 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_early | False | False |
| TRG_R7L78-C24-220100-FUTURECHEM-RADIOPHARMA-TRIAL-DATA | 220100 | C24_BIO_TRIAL_DATA_EVENT_RISK | C24 should preserve radiopharma positives when clinical-data quality, regulatory path, patient enrollment, partner/commercial route and financing bridge are visible. FutureChem produced very large MFE with controlled entry-basis MAE, but post-peak volatility still requires lifecycle local 4B if data/commercial bridge decays. | True | True |
| TRG_R3L74-C11-222080-CIS-EQUIPMENT-CAPEX-BETA-FADE | 222080 | C11_BATTERY_ORDERBOOK_RERATING | C11 should not treat battery equipment or solid-state capex beta as durable Stage2 unless orderbook, delivery, customer or margin evidence refreshes. CIS generated a sharp MFE but later gave it back and opened large MAE, making it a false Stage2 / local 4B-watch row. | True | True |
| TRG_R3L74-C11-222080-CIS-EQUIPMENT-CAPEX-BETA-FADE | 222080 | C11_BATTERY_ORDERBOOK_RERATING | C11 should not treat battery equipment or solid-state capex beta as durable Stage2 unless orderbook, delivery, customer or margin evidence refreshes. CIS generated a sharp MFE but later gave it back and opened large MAE, making it a false Stage2 / local 4B-watch row. | True | True |
| TRG_R2L75-C06-222800-SIMMTECH-DDR5-HBM-SUBSTRATE-CYCLE-FADE | 222800 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | C06 should not reward memory substrate restocking beta unless customer order, utilization, ASP or margin bridge is visible. Simmtech produced only moderate MFE and then a deep late-2024 drawdown, so it belongs in false Stage2/local 4B-watch until bridge evidence is repaired. | True | True |
| TRG_R8L71_C27_225570_STAGE2_LAUNCH_SPIKE | 225570 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_4B_too_late | False | False |
| TRG_R8L78-C27-225570-NEXON-GAMES-GLOBAL-LAUNCH-LIVEOPS | 225570 | C27_CONTENT_IP_GLOBAL_MONETIZATION | C27 should allow game-IP launch positives when global launch, user traction, live-ops retention, monetization and operating-leverage bridge are visible. Nexon Games produced large MFE, but the later post-peak drawdown means user/revenue/retention evidence must refresh. Share-count changes inside the window need validation. | True | True |
| TRG_R8L74-C27-225570-NEXONGAMES-GLOBAL-LAUNCH-RETENTION-LIFECYCLE | 225570 | C27_CONTENT_IP_GLOBAL_MONETIZATION | C27 should allow a global launch name only if launch traction converts into retention, paying-user monetization, live-ops cadence and revenue bridge. Nexon Games produced a huge launch-window MFE, but later drawdown makes lifecycle local 4B mandatory unless retention/monetization evidence refreshes. | True | True |
| TRG_R8L71_C27_225570_STAGE2_LAUNCH_SPIKE | 225570 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_4B_too_late | False | False |
| TRG_R8L74-C27-225570-NEXONGAMES-GLOBAL-LAUNCH-RETENTION-LIFECYCLE | 225570 | C27_CONTENT_IP_GLOBAL_MONETIZATION | C27 should allow a global launch name only if launch traction converts into retention, paying-user monetization, live-ops cadence and revenue bridge. Nexon Games produced a huge launch-window MFE, but later drawdown makes lifecycle local 4B mandatory unless retention/monetization evidence refreshes. | True | True |
| TRG_R8L71_C27_225570_STAGE4B_FULL_WINDOW_OVERLAY | 225570 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_4B_too_late | False | False |
| None | 226400 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | None | True | True |
| R13_CROSS_226400_2024-07-01_Stage2-Actionable-OrthopedicExportBridge | 226400 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | None | True | True |
| R13L50_C25_228670_T1_STAGE2 | 228670 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive | False | False |
| T-228670-2023-05-15-S2A | 228670 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive | False | False |
| T-228670-2023-05-15-S2A | 228670 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive | False | False |
| R13L50_C25_228670_T2_4B | 228670 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_4B_too_late | False | False |
| T-228670-2023-08-14-4C | 228670 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_4C_too_late | False | False |
| T-228670-2023-08-14-4C | 228670 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_4C_too_late | False | False |
| TRG_R2L80-C07-232140-YC-HBM-TEST-EQUIPMENT-CUSTOMER-ORDER-RS | 232140 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | C07 should preserve memory-test equipment positives when relative strength is backed by customer order quality, HBM capacity expansion, delivery cadence, revenue conversion and margin bridge. YC produced explosive MFE but later drawdown requires lifecycle treatment and source repair. | True | True |
| TRG_R2L77-C07-232140-YC-HBM-TESTER-ORDER-RS-LIFECYCLE | 232140 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | C07 should allow HBM/AI tester equipment winners when relative strength connects to customer capex, tester order, delivery backlog and margin bridge. YC/YIK produced extreme MFE with controlled entry-basis MAE, but the post-peak drawdown requires lifecycle local 4B if order/backlog/margin evidence fades. | True | True |
| R2L12_T03_YC_STAGE2_TESTER_RS_HIGH_MAE | 232140 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_too_early | False | False |
| TRG_R8L81-C26-236810-NBT-REWARD-AD-PLATFORM-THEME-FADE | 236810 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | C26 should not treat reward-ad or mobile-ad platform theme beta as durable Stage2 unless advertiser budget, DAU/MAU or conversion metrics, retention, revenue conversion and margin bridge are visible. NBT had a small/medium MFE and then a severe high-MAE fade. | True | True |
| TRG_C26_PLAYD_2021_02_10_STAGE2A | 237820 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| TRG_R8L77-C26-237820-PLAYD-ADTECH-ROAS-BUDGET-OPERATING-LEVERAGE | 237820 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | C26 should allow adtech/platform positives only when advertiser budget recovery, ROAS/performance evidence, media-buying platform revenue and operating leverage bridge are visible. PlayD produced very large MFE with controlled entry-basis MAE, but the later post-peak drawdown requires lifecycle local 4B if ad-budget/ROAS/margin evidence fades. | True | True |
| TRG_R8L81-C26-237820-PLAYD-PERFORMANCE-AD-AI-MARKETING-LIFECYCLE | 237820 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | C26 should allow adtech/performance-marketing positives only when AI/digital ad attention maps to client budget, conversion metrics, recurring advertiser spend, revenue conversion and margin bridge. PlayD produced a very large MFE but later post-peak drawdown demands lifecycle 4B if the bridge fades. | True | True |
| C18-R13L44-237880-T1-stage2 | 237880 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | False | False |
| C18-R13L44-237880-T1-stage2 | 237880 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | False | False |
| C18-R13L44-237880-T2-green-fp | 237880 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | False | False |
| C18-R13L44-237880-T2-green-fp | 237880 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | False | False |
| C18-R13L44-237880-T3-4c | 237880 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_4C_too_late | False | False |
| C18-R13L44-237880-T3-4c | 237880 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_4C_too_late | False | False |
| R5L10_C20_CLIO_STAGE2_20240509 | 237880 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | False | False |
| T_C20_CLIO_2023_08_10_STAGE2A_COUNTER | 237880 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | False | False |
| R5L10_C20_237880_T1_STAGE2_ACTIONABLE_20230810 | 237880 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_too_late | False | False |
| R5L16_C20_CLIO_T2A_20240513 | 237880 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_4C_too_late | False | False |
| R13L55_237880_STAGE2_20240514 | 237880 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | False | False |
| R13L55_237880_STAGE2_20240514 | 237880 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | False | False |
| TR-R5L42-237880-S2A-20240516 | 237880 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | False | False |
| T_C20_CLIO_2023_09_19_GREEN_COUNTER | 237880 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | False | False |
| R13L55_237880_4C_20241111 | 237880 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_4C_too_late | False | False |
| TR-R5L42-237880-4C-20241111 | 237880 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_4C_too_late | False | False |
| R13L55_237880_4C_20241111 | 237880 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_4C_too_late | False | False |
| TRG_R2L79-C09-240810-WONIKIPS-ADVANCED-EQUIPMENT-ORDER-QUALITY-POSITIVE | 240810 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | C09 should not block advanced-equipment positives when customer quality, tool order/backlog, delivery schedule, utilization/customer capacity and margin bridge are visible. Wonik IPS produced a meaningful MFE with bounded MAE, so it is a protected candidate after source repair rather than a pure blowoff. | True | True |
| TRG_R2L82-C09-240810-WONIK-IPS-SEMICAP-ORDER-BRIDGE-LIFECYCLE | 240810 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | C09 should not mechanically reject all advanced-equipment MFE. Wonik IPS had a credible semicap/order-cycle price path, but promotion requires memory capex, customer order, delivery/revenue and margin evidence; later drawdown requires lifecycle 4B if bridge fades. | True | True |
| T_R2L15_240810_PRICEONLY_20240704 | 240810 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_false_positive | False | False |
| None | 240810 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_should_route_to_local_4b_watch_not_new_green | False | False |
| TRG-R2L11-C10-WIPS-20230317 | 240810 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_false_positive | False | False |
| TRG_R2L76-C10-240810-WONIK-IPS-MEMORY-PROCESS-EQUIPMENT-CYCLE | 240810 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | C10 should preserve process-equipment recovery winners when memory capex/order recovery, customer schedule and margin bridge are visible. Wonik IPS produced a strong early MFE with moderate MAE, then faded, so C10 needs lifecycle local 4B after bridge decay. | True | True |
| None | 240810 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | None | True | True |
| None | 240810 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_should_keep_stage2_actionable_not_green | False | False |
| R13_CROSS_240810_2024-02-29_Stage2-Actionable | 240810 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | None | True | True |
| TRG_R1L83-C01-241560-DOOSAN-BOBCAT-EQUIPMENT-CYCLE-FADE | 241560 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | C01 should not treat construction-equipment backlog/cycle beta as durable Stage2 unless dealer channel inventory, rental demand, production scheduling, revenue conversion and margin bridge are visible. Doosan Bobcat had modest MFE and then high MAE, so it is local 4B-watch unless the bridge is repaired. | True | True |
| TRG_R1L79-C01-241560-DOOSAN-BOBCAT-CONSTRUCTION-EQUIPMENT-BACKLOG-FADE | 241560 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | C01 should not treat construction-equipment backlog/channel beta as durable Stage2 unless dealer inventory, order intake, utilization, pricing and margin bridge refreshes. Doosan Bobcat had a modest MFE and then a high-MAE drawdown, making it a local 4B-watch row. | True | True |
| TRG_R12L73-C32-241560-DOOSANBOBCAT-MERGER-RATIO-MINORITY-RISK | 241560 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should not treat a chaebol restructuring headline as positive control-premium evidence for the operating subsidiary when merger-ratio and minority-shareholder dilution risk dominate. Bobcat showed a brief squeeze but then opened deep MAE. | False | True |
| TRG_R12L73-C32-241560-DOOSANBOBCAT-MERGER-RATIO-MINORITY-RISK | 241560 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should not treat a chaebol restructuring headline as positive control-premium evidence for the operating subsidiary when merger-ratio and minority-shareholder dilution risk dominate. Bobcat showed a brief squeeze but then opened deep MAE. | False | True |
| R5L12_T04_HWASEUNG_20220516_FALSE_REORDER | 241590 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | False | False |
| R5L12_T04_HWASEUNG_20220516_FALSE_REORDER | 241590 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | False | False |
| R13L12_REDTEAM__R5L12_T04_HWASEUNG_20220516_FALSE_REORDER | 241590 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| TRG_R5L82-C18-241710-COSMECCA-KOREA-ODM-EXPORT-REORDER | 241710 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | C18 should protect ODM/export positives only when export channel sell-through, customer quality, reorder cadence, revenue conversion and margin bridge are visible. Cosmecca Korea produced very large MFE with moderate interim MAE, but later drawdown requires lifecycle 4B if channel/reorder proof fades. | True | True |
| T_C20_COSMECCA_2023_05_15_STAGE2A | 241710 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_too_late | False | False |
| T_C20_COSMECCA_2023_10_13_GREEN | 241710 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_too_late | False | False |
| T_C20_COSMECCA_2023_11_08_4B | 241710 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_4B_too_late | False | False |
| C27_241840_20220630_S2_WOO_YOUNG_WOO_FIRST_SIGNAL | 241840 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_too_late | False | False |
| C27_241840_20220713_GREEN_WOO_GLOBAL_RANKING_CONFIRMATION | 241840 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_too_late | False | False |
| R3L11_C11_247540_4C_2024-06-24 | 247540 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_4C_too_late | False | False |
| TR_R3L66_247540_20230203_S2A | 247540 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_missed_structural | False | False |
| R3L12_T_ECOPROBM_STAGE2_20231204 | 247540 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive | False | False |
| R3L11_C11_247540_S2_2024-01-05 | 247540 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive | False | False |
| R3L10-C11-005-T1 | 247540 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_4B_too_late | False | False |
| R3L13-C11-247540-PRICE-ONLY-4B-20230726 | 247540 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_4B_too_early | False | False |
| TRG-R3L13-C11-247540-ECOPROBM-ORDERBOOK-SLOWDOWN-4C-20240425 | 247540 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_4C_too_late | False | False |
| C12-247540-20230726-4B | 247540 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_4B_too_late | False | False |
| TR_R3L15_C14_EBM_20230726_4B_OVERLAY | 247540 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_4B_too_late | False | False |
| R3L11_T01B_ECOPROBM_20230726_PRICE_ONLY_BLOWOFF_OVERLAY | 247540 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_4B_too_early | False | False |
| T_R3L16_ECOPROBM_20230726_4B_PRICE_OVERLAY | 247540 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_4B_too_late | False | False |
| R13L55_C14_247540_4C_LATE_20230726 | 247540 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_4C_too_late | False | False |
| R3L11_T01_ECOPROBM_20240425_EV_SLOWDOWN_4C_WATCH | 247540 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_4C_too_late | False | False |
| TRG-R3L14-C14-247540-REUSED-EV-SLOWDOWN-20240425 | 247540 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_4C_too_late | False | False |
| TR_C14_ECOPROBM_20240725_STAGE4C | 247540 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_4C_too_late | False | False |
| TRG_C14_247540_20241028_ECOPROBM_CATHODE_READTHROUGH | 247540 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_missed_structural | False | False |
| R13L10_X03_247540_Stage4B | 247540 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late | False | False |
| R13L15_TR_R3L15_C14_EBM_20230726_4B_OVERLAY | 247540 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late | False | False |
| R13L11_REDTEAM__R3L11_T01B_ECOPROBM_20230726_PRICE_ONLY_BLOWOFF_OVERLAY | 247540 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_early | False | False |
| R13L13_X_R3L13-C11-247540-PRICE-ONLY-4B-20230726 | 247540 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_early | False | False |
| R3L13-C11-247540-PRICE-ONLY-4B-20230726 | 247540 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_early | False | False |
| R13L11_REDTEAM__R3L11_T01_ECOPROBM_20240425_EV_SLOWDOWN_4C_WATCH | 247540 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4C_too_late | False | False |
| R13L13_X_TRG-R3L13-C11-247540-ECOPROBM-ORDERBOOK-SLOWDOWN-4C-20240425 | 247540 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4C_too_late | False | False |
| R13L14_X_TRIG_TRG-R3L14-C14-247540-REUSED-EV-SLOWDOWN-20240425 | 247540 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4C_too_late | False | False |
| TRG-R3L13-C11-247540-ECOPROBM-ORDERBOOK-SLOWDOWN-4C-20240425 | 247540 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4C_too_late | False | False |
| R13L12_FP_X06_247540_Stage2-Actionable_2023-12-04 | 247540 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive | False | False |
| R12L11_C31_248170_STAGE2WATCH_20230607 | 248170 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| R12L11_C31_248170_4B_20230620 | 248170 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_4B_too_late | False | False |
| R12L12C31_250000_T1_STAGE2_ACTIONABLE | 250000 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_4B_too_late | False | False |
| R12L12C31_250000_T2_4B_OVERLAY | 250000 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_4B_too_late | False | False |
| R8L13_C27_NETMARBLE_T1_STAGE2A_20240508 | 251270 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_too_early | False | False |
| R8L31_C27_NETMARBLE_SOLO_LEVELING_LAUNCH_20240508 | 251270 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_false_positive | False | False |
| R8L31_C27_NETMARBLE_LOCAL_4B_20240510 | 251270 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_4B_too_late | False | False |
| R13L13_X_R8L13_C27_NETMARBLE_T1_STAGE2A_20240508 | 251270 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_too_early | False | False |
| R8L13_C27_NETMARBLE_T1_STAGE2A_20240508 | 251270 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_too_early | False | False |
| T_C27_STUDIO_2021_STAGE2_20211119 | 253450 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_false_positive | False | False |
| R8L10_C27_SDRAGON_T1_STAGE2_ACTIONABLE | 253450 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_false_positive | False | False |
| R8L11_C27_TRG_004A_STUDIO_DRAGON_STAGE2_WATCH_2021_09_27 | 253450 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_false_positive | False | False |
| R8L11-C27-SD-T1 | 253450 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_false_positive | False | False |
| C27_253450_20210120_GREEN_LATE | 253450 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_too_late | False | False |
| SD_STAGE3_FALSE_20210120 | 253450 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_false_positive | False | False |
| R13L10_T08_STUDIODRAGON_CONTENT_FALSE_POSITIVE | 253450 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R2L13_C07_253590_STAGE2WATCH_20240122 | 253590 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_false_positive | False | False |
| R11L13_C31_253840_20200331_4B | 253840 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_4B_too_late | True | False |
| R11L13_C31_253840_20200220_T1 | 253840 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_4B_too_late | True | False |
| R13L13_X_R11L13_C31_253840_20200331_4B | 253840 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late | False | False |
| R11L13_C31_253840_20200331_4B | 253840 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late | False | False |
| R13L13_X_R11L13_C31_253840_20200220_T1 | 253840 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late | False | False |
| R11L13_C31_253840_20200220_T1 | 253840 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late | False | False |
| S2_4B_POSITIONING_OVERHEAT_2024_06_19 | 257720 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_4B_too_late | False | False |
| R5L10_C20_257720_T1_STAGE2_ACTIONABLE_20230509 | 257720 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_missed_structural | False | False |
| R5L11_T01_SILICON2_20230515_STAGE2_ACTIONABLE_PLATFORM_REORDER | 257720 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_missed_structural | False | False |
| T_C20_SILICONTWO_2023_05_16_STAGE2A | 257720 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_too_late | False | False |
| S2_STAGE2_KBEAUTY_EXPORT_REORDER_2024_03_20 | 257720 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_too_late | False | False |
| R5L10_C20_SILICON2_STAGE2A_20240509 | 257720 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_missed_structural | False | False |
| R13L24_C20_001_T1_STAGE2_ACTIONABLE | 257720 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_missed_structural | False | False |
| TR_C20_257720_20240516_S2A | 257720 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_too_late | False | False |
| R13L55_257720_GREEN_20240510 | 257720 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_too_late | False | False |
| T_C20_SILICON2_2024Q1_STAGE3_GREEN | 257720 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_too_late | False | False |
| T_C20_SILICONTWO_2024_05_10_GREEN | 257720 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_too_late | False | False |
| R13L55_257720_GREEN_20240510 | 257720 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_too_late | False | False |
| R5L34_C20_257720_T_GREEN_2024_05_16 | 257720 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_too_late | False | False |
| R13L24_C20_001_T2_STAGE3_GREEN_LATE | 257720 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_too_late | False | False |
| TR-R5L42-257720-GREEN-20240612 | 257720 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_too_late | False | False |
| R5L11_T01B_SILICON2_20231013_PRICE_ONLY_LOCAL_4B_TOO_EARLY | 257720 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_4B_too_early | False | False |
| T_C20_SILICONTWO_2024_06_12_4B | 257720 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_4B_too_late | False | False |
| R13L24_C20_001_T3_4B_PRICE_ONLY | 257720 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_4B_too_early | False | False |
| TR-R5L42-257720-4B-20240619 | 257720 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_4B_too_early | False | False |
| TR_C20_257720_20241114_4B | 257720 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_4B_too_late | False | False |
| R13L11_REDTEAM__R5L11_T01_SILICON2_20230515_STAGE2_ACTIONABLE_PLATFORM_REORDER | 257720 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_missed_structural | False | False |
| R13L11_REDTEAM__R5L11_T01B_SILICON2_20231013_PRICE_ONLY_LOCAL_4B_TOO_EARLY | 257720 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_early | False | False |
| R8L31_C27_KRAFTON_STAGE2_BGMI_PUBG_20231108 | 259960 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_too_late | False | False |
| TRG_R8L80-C27-259960-KRAFTON-GAME-IP-GLOBAL-LIVEOPS-MONETIZATION | 259960 | C27_CONTENT_IP_GLOBAL_MONETIZATION | C27 should protect game-IP positives only when global live-ops, user metrics, monetization, publishing cadence, revenue conversion and margin bridge are visible. Krafton produced strong MFE with almost no entry-basis MAE, so it should not be overblocked after source repair. | True | True |
| TRG_R8L74-C27-259960-KRAFTON-PUBG-GLOBAL-MONETIZATION | 259960 | C27_CONTENT_IP_GLOBAL_MONETIZATION | C27 should allow Stage2 when global game IP monetization is tied to live-ops, regional monetization, MAU/ARPU and margin bridge. Krafton produced a large, low-MAE rerating path; this is a positive anchor that should not be overblocked by generic content-beta guards. | True | True |
| TRG_R8L71_C27_259960_STAGE2_LIVE_SERVICE_MONETIZATION | 259960 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_missed_structural | False | False |
| TRG_R8L74-C27-259960-KRAFTON-PUBG-GLOBAL-MONETIZATION | 259960 | C27_CONTENT_IP_GLOBAL_MONETIZATION | C27 should allow Stage2 when global game IP monetization is tied to live-ops, regional monetization, MAU/ARPU and margin bridge. Krafton produced a large, low-MAE rerating path; this is a positive anchor that should not be overblocked by generic content-beta guards. | True | True |
| TRG_R8L71_C27_259960_STAGE2_LIVE_SERVICE_MONETIZATION | 259960 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_missed_structural | False | False |
| TRG_R12L78-C31-263700-CARELabs-DIGITAL-HEALTH-PLATFORM-POLICY-FADE | 263700 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should not treat digital-health platform policy beta as durable Stage2 unless policy maps to appointment/transaction volume, hospital/clinic adoption, revenue conversion and margin bridge. CareLabs produced a sharp MFE, but then a severe drawdown path, so the row is useful as local 4B boundary. | True | True |
| C27_263720_20240108_S2_SOLO_LEVELING_ANIME_ROUTE | 263720 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_too_early | False | False |
| C27_263720_20240510_4B_GAME_RELEASE_EVENT_CAP | 263720 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_4B_too_late | False | False |
| R8L15_C27_PEARL_T1_STAGE2_ACTIONABLE | 263750 | C27_CONTENT_IP_GLOBAL_MONETIZATION | current_profile_false_positive | False | False |
| TRG_R8L74-C27-263750-PEARLABYSS-TRAILER-ANTICIPATION-BETA-FADE | 263750 | C27_CONTENT_IP_GLOBAL_MONETIZATION | C27 should not treat trailer/release-expectation beta as durable Stage2 unless release date, preorder/wishlist conversion, monetization model and revenue timing are visible. Pearl Abyss had limited MFE and then large MAE, so this is a false Stage2/local 4B row. | True | True |
| TRG_R8L74-C27-263750-PEARLABYSS-TRAILER-ANTICIPATION-BETA-FADE | 263750 | C27_CONTENT_IP_GLOBAL_MONETIZATION | C27 should not treat trailer/release-expectation beta as durable Stage2 unless release date, preorder/wishlist conversion, monetization model and revenue timing are visible. Pearl Abyss had limited MFE and then large MAE, so this is a false Stage2/local 4B row. | True | True |
| R13L39_C28_263860_STAGE2_20230125 | 263860 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_too_late | False | False |
| R8L12_C28_T004 | 263860 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_missed_structural | False | False |
| R8L21_C28_263860_T1_STAGE2_ACTIONABLE | 263860 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_4B_too_late | False | False |
| R8L21_C28_263860_T1_STAGE2_ACTIONABLE | 263860 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_4B_too_late | False | False |
| C28_GENIANS_2023_STAGE2A_2023-05-17 | 263860 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_too_late | False | False |
| C28_GENIANS_2023_GREEN_2023-06-09 | 263860 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_too_late | False | False |
| R8L12_C28_T005 | 263860 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_too_late | False | False |
| R13L39_C28_263860_4B_20230612 | 263860 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_4B_too_late | False | False |
| R8L21_C28_263860_T2_4B_OVERLAY | 263860 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_4B_too_late | False | False |
| R8L21_C28_263860_T2_4B_OVERLAY | 263860 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_4B_too_late | False | False |
| TRG_C01_267260_20230413_STAGE2A | 267260 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | current_profile_correct_but_C01_bridge_would_explain_signal_cleaner | True | False |
| C02_267260_20230127_STAGE2_TRANSFORMER_BACKLOG | 267260 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_missed_structural_scope_C02_absent_or_underweighted | True | False |
| TRIG_R1L13_C02_HDHE_STAGE2_20240103 | 267260 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_too_late | False | False |
| R1L10_C02_267260_STAGE2A_2024_01_03 | 267260 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_too_late | False | True |
| R1L12_C02_HDHE_STAGE2A_20240131 | 267260 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_too_late | False | False |
| None | 267260 | C02_POWER_GRID_DATACENTER_CAPEX | None | True | True |
| R13_CROSS_267260_2024-04-23_Stage2-Actionable | 267260 | C02_POWER_GRID_DATACENTER_CAPEX | None | True | True |
| R13L13_X_TRIG_R1L13_C02_HDHE_STAGE2_20240103 | 267260 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_too_late | False | False |
| TRIG_R1L13_C02_HDHE_STAGE2_20240103 | 267260 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_too_late | False | False |
| R13L12_FP_X01_267260_Stage2-Actionable_2024-01-31 | 267260 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_too_late | False | False |
| TRG_R5L79-C18-271560-ORION-CHINA-CHANNEL-REORDER-RESET-BOUNDARY | 271560 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | C18 should not treat all confectionery or China-channel reorder resets as durable Stage2. Orion produced bounded MAE and a modest recovery MFE, so it should not be forced into 4B, but the price path did not validate a high-conviction export/channel rerating either. | True | True |
| R5L16-C18-271560-T1 | 271560 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | False | False |
| TRG_R5L77-C18-271560-ORION-GLOBAL-DISTRIBUTION-BETA-FADE | 271560 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | C18 should not treat global snack distribution beta as durable Stage2 unless overseas reorder, sell-through, distributor inventory, pricing and margin bridge are visible. Orion had only limited MFE and a weak range-bound path, so it is a counterexample against generic global-distribution Green. | True | True |
| R5L12_C18_ORION_T2_REJECT_20230428 | 271560 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | False | False |
| R13L11_T007_271560_COUNTER | 271560 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | False | False |
| TRG_ORION_2024_CHINA_GROWTH_SLOWDOWN_FALSE_STAGE2_2024_01_16 | 271560 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | False | False |
| T_ORION_20230516_FALSE_STAGE2 | 271560 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | False | False |
| T_ORION_20230516_FALSE_STAGE2 | 271560 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | False | False |
| ORION_STAGE2_GLOBAL_CHANNEL_2024_02_16 | 271560 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | False | False |
| ORION_PSEUDO_GREEN_FOOD_CHANNEL_2024_06_17 | 271560 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | False | False |
| R13L15_X_TRIG_T_ORION_20230516_FALSE_STAGE2 | 271560 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| TRG_R1L82-C03-272210-HANWHA-SYSTEMS-DEFENSE-ELECTRONICS-BACKLOG | 272210 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | C03 should allow defense electronics positives when radar/C4I/sensor program backlog, export customer, delivery milestones, revenue conversion and margin bridge are visible. Hanwha Systems produced strong MFE with controlled entry-basis MAE, but bridge refresh is required after post-peak drawdown. | True | True |
| TRG_R11L77-C03-272210-HANWHA-SYSTEMS-DEFENSE-ELECTRONICS-BACKLOG | 272210 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | C03 should include defense electronics / radar / C4I names only when policy-defense demand maps to backlog, customer program, delivery schedule and margin bridge. Hanwha Systems produced solid MFE with controlled MAE, but later drawdown says C03 must lifecycle-manage the signal. | True | True |
| TR_R9L12_C29_04_272450_Stage2_Actionable | 272450 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| R9L14_C29_JINAIR_2023_REOPENING_HIGHMAE_STAGE2_ACTIONABLE | 272450 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| T_R9L13_272450_STAGE2_20230515 | 272450 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_4C_too_late | False | False |
| T_R9L13_272450_4C_20231020 | 272450 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_4C_too_late | False | False |
| R13L13_X_T_R9L13_272450_STAGE2_20230515 | 272450 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4C_too_late | False | False |
| T_R9L13_272450_STAGE2_20230515 | 272450 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4C_too_late | False | False |
| R13L13_X_T_R9L13_272450_4C_20231020 | 272450 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4C_too_late | False | False |
| T_R9L13_272450_4C_20231020 | 272450 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4C_too_late | False | False |
| TRG_R8L77-C26-273060-WISEBIRDS-AD-PLATFORM-THEME-FADE | 273060 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | C26 should not treat digital-ad or AI-ad platform beta as durable Stage2 unless advertiser budget, ROAS, media buying efficiency, repeat spend and margin bridge refreshes. Wisebirds had a tradable MFE but then a deep post-peak fade, making it a local 4B-watch row rather than durable Green. | True | True |
| R12L12C31_277410_T1_STAGE2_ACTIONABLE | 277410 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_4B_too_late | False | False |
| INSANGA_STAGE2_2023_06_07_SALT_PANIC | 277410 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| R12L11_C31_277410_STAGE2WATCH_20230607 | 277410 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| R12L11_C31_277410_4B_20230615 | 277410 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_4B_too_late | False | False |
| R12L12C31_277410_T2_4B_OVERLAY | 277410 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_4B_too_late | False | False |
| R13L15_INSANGA_STAGE2_2023_06_07_SALT_PANIC | 277410 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| TRG-R3L16-C11-278280-STAGE2-20240102 | 278280 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive | False | False |
| TRG-R3L16-C11-278280-STAGE2-20240102 | 278280 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive | False | False |
| C12-278280-20230425-RISK | 278280 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_missed_structural | False | False |
| R3L69_C12_T03_STAGE2 | 278280 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_false_positive | False | False |
| TRG_R3L76-C13-278280-CHUNBO-ELECTROLYTE-ADDITIVE-UTILIZATION-FADE | 278280 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | C13 should not treat electrolyte/additive or IRA supply-chain beta as durable Stage2 unless customer utilization, local supply, call-off and margin evidence refreshes. Chunbo had limited MFE and then a high-MAE utilization fade. | True | True |
| R3L11-C14-CHEONBO-4C-20230814 | 278280 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_4C_too_late | False | False |
| TRG_LOTTE_WELLFOOD_2024_COST_RECOVERY_EXPORT_OPTION_STAGE2_2024_04_01 | 280360 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_too_late | False | False |
| TRG_R5L75-C18-280360-LOTTE-WELLFOOD-KFOOD-EXPORT-CHANNEL-MARGIN | 280360 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | C18 should allow Stage2 when K-food/export attention is tied to channel reorder, overseas sell-through, product mix and margin bridge. Lotte Wellfood produced large MFE with controlled early MAE, but post-peak drawdown requires lifecycle local 4B if channel reorder evidence fades. | True | True |
| TRG_R5L77-C18-280360-LOTTE-WELLFOOD-GLOBAL-SNACK-CHANNEL-REORDER | 280360 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | C18 should allow packaged-food/snack exporters when overseas channel reorder, category mix, pricing and margin bridge are visible. Lotte Wellfood produced high MFE with controlled MAE, but the later post-peak drawdown requires lifecycle local 4B if global channel/margin evidence fades. | True | True |
| R13L11_T008_280360_HOLDOUT | 280360 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_missed_structural | False | False |
| TRG_LOTTE_WELLFOOD_2024_LOCAL_PEAK_4B_WATCH_2024_06_18 | 280360 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_4B_too_late | False | False |
| T_LOTTEWELLFOOD_20240517_STAGE2_ACTIONABLE | 280360 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_too_late | False | False |
| T_LOTTEWELLFOOD_20240517_STAGE2_ACTIONABLE | 280360 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_too_late | False | False |
| T_LOTTEWELLFOOD_20240610_STAGE3_GREEN_PROXY | 280360 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_too_late | False | False |
| R13L15_X_TRIG_T_LOTTEWELLFOOD_20240517_STAGE2_ACTIONABLE | 280360 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_too_late | False | False |
| R13L15_X_TRIG_T_LOTTEWELLFOOD_20240610_STAGE3_GREEN_PROXY | 280360 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_too_late | False | False |
| TRG_R5L81-C19-282330-BGF-RETAIL-CONVENIENCE-MARGIN-BOUNDED-RECOVERY | 282330 | C19_BRAND_RETAIL_INVENTORY_MARGIN | C19 should not call bounded convenience-store recovery hard 4C when no non-price margin or demand break is confirmed, but it also should not mark durable Stage2 without same-store sales, mix, cost control and margin bridge. BGF Retail is a RiskWatch/no-hard-4C boundary. | True | True |
| TRG_R7L79-C25-287410-JEISYS-MEDICAL-AESTHETIC-DEVICE-STRATEGIC-EVENT | 287410 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | C25 should protect aesthetic-device export/commercialization positives when export channel, installed-base, consumables, distributor reorder, revenue and margin bridge are visible. Jeisys Medical produced strong MFE and later a stabilized strategic-event price path, but status/delisting-like caveat requires validation. | True | True |
| R7L15-C24-288330-T1 | 288330 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_false_positive | False | False |
| TRG_R12L80-C31-289010-ICECREAM-EDU-AI-DIGITAL-TEXTBOOK-LIFECYCLE | 289010 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should allow under-covered education-policy rows only when AI digital textbook policy maps to direct school/customer adoption, paid conversion, subscription revenue and margin bridge. Icecream Edu produced tradable MFE but later high MAE, so it is a lifecycle candidate only after source repair. | True | True |
| R13L15_X_TRIG_TR_R12L15_C31_289010_STAGE2_20200224 | 289010 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late | False | False |
| TRG_R8L80-C27-293490-KAKAOGAMES-GAME-PORTFOLIO-THEME-FADE | 293490 | C27_CONTENT_IP_GLOBAL_MONETIZATION | C27 should not treat game portfolio or new-title theme beta as durable Stage2 unless global IP traction, launch metrics, user retention, revenue conversion and margin bridge are visible. Kakao Games had small MFE and then a persistent MAE/downtrend path. | True | True |
| TRG_R7L16_293780_20220801_STAGE2_FALSE_POSITIVE | 293780 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_false_positive | False | False |
| None | 294570 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | None | True | True |
| R13_CROSS_294570_2024-02-01_Stage2-FalsePositive_/_DataAPIContractRetentionWeak | 294570 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | None | True | True |
| R1L15_C05_HDC_4C_SAFETY_TRUST_BREAK_20220112 | 294870 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | current_profile_4C_too_late | False | False |
| R10L15_T003 | 294870 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_4C_too_late | False | False |
| R10L10_T01_HDC_2022_4C_QUALITY_BREAK | 294870 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_4C_too_late | False | False |
| TRG_HDC_2022_COLLAPSE_HARD_4C_2022_01_12 | 294870 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_4C_too_late | False | False |
| R10L10_T02_HDC_2024_BALANCE_REPAIR_STAGE2 | 294870 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_missed_structural | False | False |
| R10L10_C30_HDC_T2 | 294870 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_4B_too_late | False | False |
| TR-C30-294870-4C-20220112 | 294870 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_4C_too_late | False | False |
| R13L15_R10L15_T003 | 294870 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4C_too_late | False | False |
| R13L10_T09_HDC_QUALITY_HARD_4C | 294870 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4C_too_late | False | False |
| R13L12_REDTEAM__TR-C30-294870-4C-20220112 | 294870 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4C_too_late | False | False |
| R13L15_X_TRIG_R1L15_C05_HDC_4C_SAFETY_TRUST_BREAK_20220112 | 294870 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4C_too_late | False | False |
| R11L15-C31-297090-S2A-20220816 | 297090 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| R13L15_X_TRIG_R11L15-C31-297090-S2A-20220816 | 297090 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R4L9_C15_298000_T1 | 298000 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_false_positive | False | False |
| R4L15_C17_T05_HYOSUNGCHEM_20210503_FALSE_STAGE2 | 298000 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive | False | False |
| R4L15_C17_T05_HYOSUNGCHEM_20210503_FALSE_STAGE2 | 298000 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive | False | False |
| R4L9_C15_298020_T1 | 298020 | C15_MATERIAL_SPREAD_SUPERCYCLE | current_profile_too_late | False | False |
| R4L10_C17_298020_T1 | 298020 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_correct | False | True |
| R4L16_C17_298020_T1_STAGE2 | 298020 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_4B_too_late | False | False |
| R13L26_C17_001_T1_STAGE2_ACTIONABLE | 298020 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_missed_structural | False | False |
| R4L12-C17-HTNC-GREEN-20210325 | 298020 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_too_late | False | False |
| R13L26_C17_001_T2_STAGE3_GREEN_LATE | 298020 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_too_late | False | False |
| R4L12-C17-HTNC-4B-20210716 | 298020 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_4B_too_early | False | False |
| R4L10_C17_298020_T4B | 298020 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_correct | False | True |
| R4L11_T02B_HYOSUNGTNC_20210716_4B_SPREAD_PEAK_OVERLAY | 298020 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_4B_too_late | False | False |
| TRIG_R1L13_C02_HYOSUNG_STAGE2_20240103 | 298040 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_too_late | False | False |
| R1L10_C02_298040_STAGE2A_2024_01_03 | 298040 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_too_late | False | True |
| R1L12_C02_HSHEAVY_STAGE2A_20240305 | 298040 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_too_late | False | False |
| None | 298040 | C02_POWER_GRID_DATACENTER_CAPEX | None | True | True |
| R13_CROSS_298040_2024-04-29_Stage2-Actionable | 298040 | C02_POWER_GRID_DATACENTER_CAPEX | None | True | True |
| R13L13_X_TRIG_R1L13_C02_HYOSUNG_STAGE2_20240103 | 298040 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_too_late | False | False |
| TRIG_R1L13_C02_HYOSUNG_STAGE2_20240103 | 298040 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_too_late | False | False |
| TRG_R13L32_298380_STAGE2_20220112 | 298380 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_false_positive | True | False |
| R7L15-C24-298380-T1-ABL301-SANOFI-STAGE2A-20220112 | 298380 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_too_early | False | False |
| R7L15-C24-298380-T1-ABL301-SANOFI-STAGE2A-20220112 | 298380 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_too_early | False | False |
| TRG_R7L80-C24-298380-ABL-BIO-BIOPLATFORM-DATA-LICENSE-MILESTONE | 298380 | C24_BIO_TRIAL_DATA_EVENT_RISK | C24 should protect platform-biotech positives only when trial data, partner/license economics, milestone runway, cash runway and commercialization path are visible. ABL Bio produced a strong MFE but still needs lifecycle 4B if the data/license bridge fades. | True | True |
| TRG_R7L76-C24-298380-ABL-BIO-BISPECIFIC-ADC-TRIAL-DATA-BRIDGE | 298380 | C24_BIO_TRIAL_DATA_EVENT_RISK | C24 should allow a trial-data/platform-event Stage2 when clinical data, partner validation, differentiated modality and downstream commercialization bridge are visible. ABL Bio produced high MFE with almost no entry-basis MAE, but later post-peak fading still requires lifecycle local 4B if clinical/partner bridge evidence goes stale. | True | True |
| TRG_R7L74-C24-298380-ABL-BISPECIFIC-PLATFORM-DATA-RERATING | 298380 | C24_BIO_TRIAL_DATA_EVENT_RISK | C24 should distinguish platform-data derisking from simple biotech beta. ABL Bio had an early tradable MFE, then later re-accelerated into a larger 180D MFE; however later drawdown and share-count change require lifecycle and validation controls. | True | True |
| TRG_R7L74-C24-298380-ABL-BISPECIFIC-PLATFORM-DATA-RERATING | 298380 | C24_BIO_TRIAL_DATA_EVENT_RISK | C24 should distinguish platform-data derisking from simple biotech beta. ABL Bio had an early tradable MFE, then later re-accelerated into a larger 180D MFE; however later drawdown and share-count change require lifecycle and validation controls. | True | True |
| TRG_R13L32_298380_4B_20220121 | 298380 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_correct | True | False |
| TRG-R13L42-298540-S2-20240215 | 298540 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_false_positive | False | False |
| T_C19_NATURE_2022Q1_FALSE_POSITIVE | 298540 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_false_positive | False | False |
| T-C19-298540-2022-12-12-S2A | 298540 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_false_positive | False | False |
| R5L31_T04_NATURE_STAGE2_INVENTORY_OVERHANG_20230516 | 298540 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_false_positive | False | False |
| R13L45_298540_STAGE2_FALSE_2024-04-01 | 298540 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_false_positive | False | False |
| R13L45_298540_STAGE3_YELLOW_FALSE_2024-05-31 | 298540 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_false_positive | False | False |
| TRG-R13L42-298540-4C-20240614 | 298540 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_4C_too_late | False | False |
| TR_R9L31_C29_298690_REOPENING_SPIKE_20230120 | 298690 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| TRG_R3L82-C11-299030-HANA-TECH-BATTERY-EQUIPMENT-ORDERBOOK-FADE | 299030 | C11_BATTERY_ORDERBOOK_RERATING | C11 should not treat battery equipment orderbook theme beta as durable Stage2 unless customer order, delivery schedule, backlog conversion, revenue and margin bridge are visible. Hana Technology had a sharp early MFE, then severe high-MAE fade and share-count changes. | True | True |
| TR_R7L10_302440_2022-06-29_DOMESTIC_APPROVAL | 302440 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive | False | False |
| TRG_R7L81-C23-302440-SK-BIOSCIENCE-VACCINE-COMMERCIALIZATION-THEME-FADE | 302440 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | C23 should not treat vaccine platform or regulatory commercialization theme beta as durable Stage2 unless product approval, procurement/order visibility, manufacturing utilization, revenue conversion and margin bridge are visible. SK Bioscience had tiny MFE and then a high-MAE fade. | True | True |
| TRG_R7L71_C24_302440_SKY_COVIONE_PHASE3_DEMAND_TRAP | 302440 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_false_positive | False | False |
| TRG_R7L11_302440_STAGE2_20220706 | 302440 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_false_positive | False | False |
| TRG_R7L71_C24_302440_SKY_COVIONE_PHASE3_DEMAND_TRAP | 302440 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_false_positive | False | False |
| TRG_R5L78-C19-306040-SJ-GROUP-BRAND-INVENTORY-TURNAROUND-FADE | 306040 | C19_BRAND_RETAIL_INVENTORY_MARGIN | C19 should not treat fashion-brand inventory-turnaround beta as durable Stage2 unless sell-through, channel productivity, inventory clearance, reorder and margin bridge are visible. SJ Group produced only small MFE, then persistent MAE and post-peak fade. | True | True |
| TRG_R8L79-C28-307950-HYUNDAI-AUTOEVER-AUTO-SW-CONTRACT-RETENTION | 307950 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | C28 should preserve software/SI positives when contract retention, captive/customer quality, recurring maintenance, project backlog, revenue recognition and margin bridge are visible. Hyundai AutoEver produced a slow MFE with moderate MAE; it should not be overblocked after source repair, but lifecycle 4B is needed if contract/revenue/margin evidence fades. | True | True |
| R7L15-C24-310210-T1 | 310210 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_too_late | False | False |
| R13L30_C21_WOORI_POLICY_S2_20240208 | 316140 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_early | False | False |
| TR_WOORI_S2_20230208 | 316140 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_early | False | False |
| TRG_R6L73-C21-316140-WOORI-VALUEUP-CAPITAL-RETURN-BRIDGE | 316140 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | C21 should allow Stage2 when low-PBR bank rerating is backed by shareholder-return, buyback/cancellation, dividend and ROE bridge. Woori produced controlled MAE and later MFE, but share-count change inside the window needs coding-agent validation. | True | True |
| TRG_R6L79-C21-316140-WOORI-BANK-HOLDCO-CAPITAL-RETURN | 316140 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | C21 should preserve bank-holdco capital-return rows when PBR discount, capital ratio, shareholder-return policy, earnings durability and buyback/cancellation evidence are visible. Woori Financial produced a controlled-MAE MFE path, but share-count changes inside the raw shard require validation. | True | True |
| WOORI-C21-S2A-20240226 | 316140 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | False | False |
| T_C21_WOORI_20240729_STAGE2A | 316140 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | False | False |
| T-WOORI-S2A-20250210 | 316140 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_late | True | True |
| TRG_R6L73-C21-316140-WOORI-VALUEUP-CAPITAL-RETURN-BRIDGE | 316140 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | C21 should allow Stage2 when low-PBR bank rerating is backed by shareholder-return, buyback/cancellation, dividend and ROE bridge. Woori produced controlled MAE and later MFE, but share-count change inside the window needs coding-agent validation. | True | True |
| R6L16_T_WOORIFG_HEADLINE_UNDERPOWER_20240226_REP | 316140 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_early | False | False |
| R13L30_C21_WOORI_FALSE_GREEN_20240726 | 316140 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | False | False |
| R11L11_T_316140_20240226_Stage2_Actionable | 316140 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| TR_R11L12_WOORI_VALUEUP_STAGE2_20240226 | 316140 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_too_early | False | False |
| R11L13_C31_HDENERGY_20220729_STAGE2A | 322000 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_too_early | False | False |
| TRG_R2L77-C07-322310-AUROS-METROLOGY-EQUIPMENT-THEME-FADE | 322310 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | C07 should not treat metrology/overlay equipment beta as durable Stage2 unless customer order, delivery, tool adoption and margin bridge are visible. Auros Technology had a tradable early MFE, but then opened a high-MAE drawdown path, making it local 4B-watch rather than durable Green. | True | True |
| TRG_R2L82-C09-322310-AUROS-METROLOGY-VALUATION-BLOWOFF | 322310 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | C09 should cap overlay metrology/inspection equipment MFE when it is mostly valuation/theme beta. Without customer order, delivery, revenue conversion and margin bridge, Oros' early spike should be treated as local 4B/fade rather than durable Stage2. | True | True |
| R7L13-C25-322510-T1-STAGE2A-20230517 | 322510 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_too_early | False | False |
| R7L12_C25_322510_T1_STAGE2 | 322510 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive | False | False |
| C25_JLK_FALSE_GREEN_20230810 | 322510 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive | False | False |
| R7L13-C25-322510-T2-PRICE-ONLY-4B-20230724 | 322510 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_4B_too_early | False | False |
| R6L13_C21_KAKAOBANK_T02_4C_THESIS_BREAK_20220114 | 323410 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_4C_too_late | False | False |
| R6L14_T007_KAKAOBANK_4C_GOVERNANCE | 323410 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_4C_too_late | False | False |
| R6L11_T03_KAKAOBANK_20240226_FALSE_STAGE2_DIGITAL_PREMIUM | 323410 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | False | False |
| R6L44-C21-003-T1 | 323410 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | False | False |
| T-KAKAOBANK-S2-20250210 | 323410 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | True | True |
| TR_KAKAO_S2_20210806 | 323410 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | False | False |
| C21-KAKAO-S2A-20240201 | 323410 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | False | False |
| R6L10_C21_KAKAOBANK_FALSE_POSITIVE_2024-02-02 | 323410 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | False | False |
| R6L14_T004_KAKAOBANK_FALSE_STAGE2 | 323410 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | False | False |
| T_C21_KAKAOBANK_20240208_STAGE2A | 323410 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | False | False |
| R6L23_T06_KAKAOBANK_STAGE2_VALUEUP_20240226 | 323410 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive_if_sector_beta_only | False | False |
| R6L10_C21_323410_STAGE2_20240226 | 323410 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | False | False |
| KAKAO_POLICY_ONLY_2024_02_26 | 323410 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | False | False |
| KAKAOBANK-C21-S2A-20240226 | 323410 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | False | False |
| R6L10_C21_KAKAOBANK_STAGE2A_20240226 | 323410 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | False | False |
| R6L45_T05_KAKAOBANK_VALUEUP_FALSE_STAGE2 | 323410 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | False | False |
| R6L35-C21-KAKAOBANK-S2-20240227 | 323410 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | False | False |
| R13L25_C21_KAKAOBANK_323410_STAGE2_20240226 | 323410 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | False | False |
| T_KAKAOBANK_2024_02_15_FALSE_POSITIVE | 323410 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | False | False |
| TRG_R6L12_KAKAOBANK_POLICY_BETA_20240226 | 323410 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | False | False |
| R6L32-C21-KAKAOBANK-BLOCKED-2024-01-26 | 323410 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | False | False |
| R6L12_C21_KAKAOBANK_20240227_POLICY_BETA_FAIL_T1 | 323410 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | False | False |
| R6L60_C21_KAKAOBANK_POLICYONLY_20240226 | 323410 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | False | False |
| R6L60_C21_KAKAOBANK_POLICYONLY_20240226 | 323410 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | False | False |
| TRG_R6L15_KAKAOBANK_20240227_STAGE2_POLICY_ONLY | 323410 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | False | False |
| R6L40_C21_KAKAO_323410_T01_STAGE2_VALUEUP_POLICY | 323410 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | False | False |
| R6L44-C21-003-T2 | 323410 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_4B_too_late_if_price_only_guard_ignored | False | False |
| TR_KAKAO_4B_20210819 | 323410 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_4B_too_late | False | False |
| T-KAKAOBANK-4B-20250624 | 323410 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_4B_too_late | True | True |
| T-KAKAOBANK-4B-20250624 | 323410 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_4B_too_late | True | True |
| R6L40_C21_KAKAO_323410_T02_4C_THESIS_BREAK | 323410 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_4C_too_late | False | False |
| R13L25_C21_KAKAOBANK_323410_4C_WATCH_20240627 | 323410 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_4C_too_early | False | False |
| R6L13_C21_KAKAOBANK_T01_IPO_DIGITAL_FINANCE_20210806 | 323410 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | False | False |
| R13L13_X_R6L13_C21_KAKAOBANK_T02_4C_THESIS_BREAK_20220114 | 323410 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4C_too_late | False | False |
| R6L13_C21_KAKAOBANK_T02_4C_THESIS_BREAK_20220114 | 323410 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4C_too_late | False | False |
| R13L13_X_R6L13_C21_KAKAOBANK_T01_IPO_DIGITAL_FINANCE_20210806 | 323410 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R6L13_C21_KAKAOBANK_T01_IPO_DIGITAL_FINANCE_20210806 | 323410 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L14_G06_14_323410_R6L14_T007_KAKAOBANK_4C_GOVERNANCE | 323410 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | current_profile_4C_too_late | False | False |
| R13L12_FP_X08_323410_Stage2-FalsePositive_2024-02-26 | 323410 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | current_profile_false_positive | False | False |
| TRG_R7L80-C24-323990-VAXCELL-TRIAL-THEME-FADE | 323990 | C24_BIO_TRIAL_DATA_EVENT_RISK | C24 should not treat cell-therapy trial theme beta as durable Stage2 unless trial data quality, regulatory path, partner/commercial economics and cash runway are visible. VaxCell had a tradable MFE but then a high-MAE fade. | True | True |
| C25_R13L33_005_T1_STAGE2_ACTIONABLE | 328130 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive | False | False |
| R7L12_C25_328130_T1_STAGE2 | 328130 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive | False | False |
| R7L14-C25-003-S2-2024-02-20 | 328130 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive | False | False |
| R7L14-C25-003-S2-2024-02-20 | 328130 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive | False | False |
| TRG_R1L77-C01-329180-HD-HYUNDAI-HI-SHIPBUILDING-ORDERBOOK-MARGIN | 329180 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | C01 should preserve large shipbuilding orderbook winners when customer quality, delivery slots, naval/LNG mix, ASP and margin bridge are visible. HD Hyundai Heavy produced high MFE with controlled MAE; later drawdown should be lifecycle-managed, not treated as a hard 4C without order/margin break. | True | True |
| TRG_R1L73-C01-329180-HDHHI-LNG-NAVAL-BACKLOG-MARGIN-BRIDGE | 329180 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | C01 should allow Stage2 when shipbuilding backlog is not just order volume but connects to LNG/naval mix, rising newbuild prices and margin conversion. The stock-web path shows structural MFE with controlled early MAE, but source repair is needed before runtime weight promotion. | True | True |
| TRG_R1L73-C01-329180-HDHHI-LNG-NAVAL-BACKLOG-MARGIN-BRIDGE | 329180 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | C01 should allow Stage2 when shipbuilding backlog is not just order volume but connects to LNG/naval mix, rising newbuild prices and margin conversion. The stock-web path shows structural MFE with controlled early MAE, but source repair is needed before runtime weight promotion. | True | True |
| R13L50_C25_335890_T1_STAGE2 | 335890 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_too_late | False | False |
| R11L13_C31_DFC_20220729_STAGE2A | 336260 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| T336260-S2-20220811 | 336260 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| TRG_R3L80-C12-336370-SOLUS-COPPERFOIL-POSTCA-CALLOFF-LIFECYCLE | 336370 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | C12 should not overblock post-CA copperfoil/material names when recovery MFE and bounded entry MAE are visible, but it still requires customer volume, utilization and margin evidence before Stage2 promotion. | True | True |
| TRG_R3L13_C12_SOLUS_20230222_STAGE2_CAPPED | 336370 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_false_positive | False | False |
| TRG_R3L13_C12_SOLUS_20230222_STAGE2_CAPPED | 336370 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_false_positive | False | False |
| R3L69_C12_T04_STAGE2 | 336370 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_false_positive | False | False |
| TRG_R7L79-C25-336570-WONTECH-AESTHETIC-DEVICE-EXPORT-MARGIN-LIFECYCLE | 336570 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | C25 should allow medical-aesthetic device positives when export demand, distributor reorder, installed-base utilization, consumables/service revenue and margin bridge are visible. Wontech produced large MFE, then a high post-peak drawdown, so it needs lifecycle 4B if export/reorder/margin evidence fades. | True | True |
| TRG-R13L42-337930-S2A-20240529 | 337930 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_too_late | False | False |
| R13L45_337930_STAGE2_2024-05-29 | 337930 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_4B_too_late | False | False |
| R13L45_337930_STAGE3_GREEN_2024-08-09 | 337930 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_4B_too_late | False | False |
| TRG-R13L42-337930-4B-20241002 | 337930 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_4B_too_late | False | False |
| R13L45_337930_4B_2024-10-02 | 337930 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_4B_too_late | False | False |
| C25_R13L33_001_T3_STAGE4B_OVERLAY | 338220 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_4B_too_late | False | False |
| T-338220-2023-02-24-S2A | 338220 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_too_late | False | False |
| T-338220-2023-02-24-S2A | 338220 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_too_late | False | False |
| R7L13-C25-338220-T1-STAGE2A-20230602 | 338220 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_missed_structural | False | False |
| R13L50_C25_338220_T1_STAGE2 | 338220 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_false_positive | False | False |
| C25_VUNO_GREEN_COMPARE_20230829 | 338220 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_too_late | False | False |
| C25_R13L33_001_T2_STAGE3_YELLOW_COMPARISON | 338220 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_too_late | False | False |
| R13L50_C25_338220_T2_4B | 338220 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_4B_too_late | False | False |
| R7L13-C25-338220-T2-4B-20230906 | 338220 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | current_profile_4B_too_late | False | False |
| TRG_R11L75-C31-339950-IVY-KIMYOUNG-MEDQUOTA-ADMISSION-DEMAND-LIFECYCLE | 339950 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 can allow a policy-event lifecycle candidate when a medical-school quota policy shock connects to transfer/admission-course demand, paid enrollment, retention and margin bridge. Ivy Kimyoung produced large MFE, but the post-peak drawdown says lifecycle local 4B is mandatory if the policy-demand bridge fades. | True | True |
| TRG_R2L80-C07-348210-NEXTIN-INSPECTION-METROLOGY-THEME-FADE | 348210 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | C07 should not treat semiconductor inspection/metrology theme beta as durable Stage2 unless HBM/customer order, capacity expansion, delivery, recurring service and margin bridge are visible. Nextin had small early MFE and then a deep MAE path, making it a local 4B boundary rather than Green. | True | True |
| TRG-R3L16-C11-348370-STAGE2-20240102 | 348370 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_too_late | False | False |
| TRG-R3L16-C11-348370-STAGE2-20240102 | 348370 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_too_late | False | False |
| R3L11_C11_348370_4B_2024-04-08 | 348370 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_4B_too_late | False | False |
| TRG_R3L76-C13-348370-ENCHEM-US-ELECTROLYTE-IRA-LOCAL-SUPPLY-LIFECYCLE | 348370 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | C13 should allow Stage2 when US/IRA battery supply-chain attention connects to actual electrolyte local supply, customer qualification, utilization, AMPC or margin bridge. Enchem produced extreme MFE with controlled entry-basis MAE, but the post-peak drawdown and share-count changes require lifecycle local 4B and validation. | True | True |
| TRG_R2L75-C06-353200-DAEDUCK-FCBGA-MEMORY-PACKAGE-SUBSTRATE-BETA-FADE | 353200 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | C06 should not treat package substrate or AI memory-adjacent beta as durable Stage2 unless customer capacity, utilization, order or margin bridge refreshes. Daeduck Electronics produced limited MFE and then a severe 180D MAE path, making it a false Stage2/local 4B row. | True | True |
| R13L54_C28_356890_STAGE2_BLOCKED_20230220 | 356890 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive | False | False |
| R13L54_C28_356890_4B_20230221 | 356890 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_4B_too_early | False | False |
| TRG_R3L75-C12-361610-SK-IET-SEPARATOR-CUSTOMER-CALLOFF-RISK | 361610 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | C12 should not treat separator beta as durable Stage2 unless customer call-off schedule, utilization, pricing and margin evidence refreshes. SK IET had a brief rebound but then opened severe MAE as EV demand and separator utilization risk dominated. | True | True |
| TRG_R3L78-C12-361610-SKIET-SEPARATOR-CALLOFF-LOCAL4B | 361610 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | C12 should not treat separator customer-contract exposure as durable Stage2 unless call-off volume, utilization, pricing and margin bridge refreshes. SK IE Technology had only a small early MFE and then a severe high-MAE drawdown path. | True | True |
| TRG_R3L80-C12-361610-SKIET-SEPARATOR-CALLOFF-UTILIZATION-LOCAL4B | 361610 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | C12 should flag separator/customer-calloff risk when customer volume, utilization, pricing and margin bridge weaken. SK IET produced only a small early MFE and then a deep high-MAE path. | True | True |
| C12-R3L65-361610-T1 | 361610 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_too_late | False | False |
| TRG_R3L73-C14-361610-SKIET-SEPARATOR-DEMAND-SLOWDOWN-LOCAL4B | 361610 | C14_EV_DEMAND_SLOWDOWN_4B_4C | C14 should fire local 4B-watch when EV demand slowdown translates into separator utilization pressure and the stock path opens severe MAE. Hard 4C still requires non-price evidence such as plant impairment, contract cancellation, insolvency, or structural customer loss. | True | True |
| TRG_R3L73-C14-361610-SKIET-SEPARATOR-DEMAND-SLOWDOWN-LOCAL4B | 361610 | C14_EV_DEMAND_SLOWDOWN_4B_4C | C14 should fire local 4B-watch when EV demand slowdown translates into separator utilization pressure and the stock path opens severe MAE. Hard 4C still requires non-price evidence such as plant impairment, contract cancellation, insolvency, or structural customer loss. | True | True |
| TRG-R3L15-C14-361610-4C-20240425 | 361610 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_4C_too_late | False | False |
| R13L15_X_TRIG_TRG-R3L15-C14-361610-4C-20240425 | 361610 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4C_too_late | False | False |
| R5L10_C20_362320_T1_STAGE2_NARRATIVE_GUARD_20230119 | 362320 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | False | False |
| R5L10_C20_362320_T2_4C_GUARD_20230726 | 362320 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_4C_too_late | False | False |
| TRG_R8L77-C26-363260-MOBIDAYS-POST-CA-ADTECH-THEME-FADE | 363260 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | C26 should not treat post-corporate-action adtech theme spikes as durable Stage2 unless advertiser budget, campaign ROAS, platform revenue retention and operating leverage bridge are verified. Mobidays was measured only after the 2024-05-24 corporate-action candidate; the post-entry path showed weak MFE and high MAE, so it is a post-CA local 4B boundary. | True | True |
| R7L15-C24-365270-T1 | 365270 | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_4C_too_late | False | False |
| R3L11_C11_373220_S2_2024-04-26 | 373220 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_too_early | False | False |
| R3L10-C11-004-T1 | 373220 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_too_early | False | False |
| C12-R3L65-373220-T1 | 373220 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_false_positive | False | False |
| R3L67_T02_LGES_2024_Q1_AMPC_GUARD | 373220 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_too_early | False | False |
| R3L67_T02_LGES_2024_Q1_AMPC_GUARD | 373220 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_too_early | False | False |
| R3L67_T01_LGES_2025_Q1_AMPC_STAGE2A | 373220 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_too_late | False | False |
| R3L67_T01_LGES_2025_Q1_AMPC_STAGE2A | 373220 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_too_late | False | False |
| TRG_R3L14_C13_LGES_20230411_STAGE3Y_AMPC_LAG | 373220 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_too_early | False | False |
| TR-C13-LGES-20240725-Q2-AMPC-CUT-CAPEX-PACING | 373220 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_4B_too_early | False | False |
| R3L10-C13-373220-T2 | 373220 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_too_early | False | False |
| R3L10-C13-373220-T2 | 373220 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | current_profile_too_early | False | False |
| TRG_R13_C14_373220_20240725_FALSE4C | 373220 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_4C_too_early | False | False |
| R13L55_C14_373220_4B_20230726 | 373220 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_4C_too_late | False | False |
| TR_C14_373220_20241115_STAGE4B_COUNTER | 373220 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_4B_too_early | False | False |
| R3L11-C14-LGES-FALSE4C-20231025 | 373220 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_false_positive | False | False |
| TRG-R3L14-C14-373220-Q1-SLOW-EV-CAPEX-20240425 | 373220 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_too_early | False | False |
| T_R3L16_LGES_20240425_STAGE4C_WATCH | 373220 | C14_EV_DEMAND_SLOWDOWN_4B_4C | current_profile_4C_too_early | False | False |
| R13L14_X_TRIG_TRG-R3L14-C14-373220-Q1-SLOW-EV-CAPEX-20240425 | 373220 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_too_early | False | False |
| R1L11_C05_375500_FALSEGREEN_20240110 | 375500 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | current_profile_false_positive | False | False |
| R1L15_C05_DLENC_STAGE2_POLICY_BETA_MARGIN_CAP_20240327 | 375500 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | current_profile_false_positive | False | False |
| R10L10-C30-DLEC-STAGE2-20240110 | 375500 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive | False | False |
| R10L11_T03_DL_POLICY_BETA_CAP | 375500 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive | False | False |
| TRG_R10L12_375500_20231010_PF_DISCOUNT_REVERSAL_COUNTEREXAMPLE | 375500 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive | False | False |
| TRG_R10L12_375500_20231010_PF_DISCOUNT_REVERSAL_COUNTEREXAMPLE | 375500 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive | False | False |
| R10L10_C30_DL_T1 | 375500 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive | False | False |
| R10L10_C30_DL_T2 | 375500 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_4C_too_late | False | False |
| R13L15_X_TRIG_R1L15_C05_DLENC_STAGE2_POLICY_BETA_MARGIN_CAP_20240327 | 375500 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L11_REDTEAM__R10L11_T03_DL_POLICY_BETA_CAP | 375500 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| TRG_R8L73-C26-376300-DEARU-SUBSCRIPTION-PLATFORM-OPERATING-LEVERAGE | 376300 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | C26 should allow Stage2 when a platform has subscription/user or ARPU expansion that can convert into operating leverage. DearU produced very high MFE with almost no entry-basis MAE, but later local 4B-watch is still needed if subscriber/artist expansion evidence stops refreshing after the peak. | True | True |
| TRG_R8L73-C26-376300-DEARU-SUBSCRIPTION-PLATFORM-OPERATING-LEVERAGE | 376300 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | C26 should allow Stage2 when a platform has subscription/user or ARPU expansion that can convert into operating leverage. DearU produced very high MFE with almost no entry-basis MAE, but later local 4B-watch is still needed if subscriber/artist expansion evidence stops refreshing after the peak. | True | True |
| TRG_R6L75-C21-377300-KAKAOPAY-DIGITAL-FINANCE-PBR-BETA-FADE | 377300 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | C21 should not treat digital-finance/value-up beta as durable Stage2 unless ROE inflection, capital return, profitability and shareholder-return bridge are visible. KakaoPay produced an event spike but then entered a long high-MAE decline, making it a false Stage2/local 4B row. | True | True |
| R6L13_C21_KAKAOPAY_T2_REJECT_20240226 | 377300 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | False | False |
| R6L13_C21_KAKAOPAY_T01_IPO_DIGITAL_PAYMENT_20211103 | 377300 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | False | False |
| R13L13_X_R6L13_C21_KAKAOPAY_T01_IPO_DIGITAL_PAYMENT_20211103 | 377300 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R6L13_C21_KAKAOPAY_T01_IPO_DIGITAL_PAYMENT_20211103 | 377300 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L13_ACC_X05_377300_20240226 | 377300 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | False | False |
| R13L41_C18_FNF_4C_2024_01_15 | 383220 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_4C_too_late | False | False |
| R13L41_C18_FNF_STAGE2_2023_08_01 | 383220 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | False | False |
| R5L39_C18_383220_STAGE2_FALSE_20240503 | 383220 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | False | False |
| C18-R13L44-383220-T1-stage2 | 383220 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | False | False |
| C18-R13L44-383220-T1-stage2 | 383220 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | False | False |
| C18-R13L44-383220-T2-4c | 383220 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_4C_too_late | False | False |
| R5L39_C18_383220_4CWATCH_20240805 | 383220 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_4C_too_late | False | False |
| C18-R13L44-383220-T2-4c | 383220 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_4C_too_late | False | False |
| TRG-R13L42-383220-S2-20230906 | 383220 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_false_positive | False | False |
| R5L31_T03_FNF_STAGE2_INVENTORY_RISK_20230516 | 383220 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_false_positive | False | False |
| T-C19-383220-2023-02-15-GREEN-CAND | 383220 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_false_positive | False | False |
| R5L31_T06_FNF_4C_INVENTORY_THESIS_BREAK_20230719 | 383220 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_4C_too_late | False | False |
| TRG-R13L42-383220-4C-20231115 | 383220 | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_4C_too_late | False | False |
| R11L15-C31-389260-S2A-20220816 | 389260 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_4B_too_late | False | False |
| R11L15-C31-389260-4B-20220901 | 389260 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_4B_too_late | False | False |
| R13L15_X_TRIG_R11L15-C31-389260-S2A-20220816 | 389260 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late | False | False |
| R13L15_X_TRIG_R11L15-C31-389260-4B-20220901 | 389260 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4B_too_late | False | False |
| TR_R3L66_393890_20230203_S2A | 393890 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive | False | False |
| TRG-R3L16-C11-393890-STAGE2-20240102 | 393890 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive | False | False |
| TRG-R3L16-C11-393890-STAGE2-20240102 | 393890 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive | False | False |
| TRG-R3L16-C11-393890-4C-WATCH-20240722 | 393890 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_4C_too_late | False | False |
| TRG-R3L16-C11-393890-4C-WATCH-20240722 | 393890 | C11_BATTERY_ORDERBOOK_RERATING | current_profile_4C_too_late | False | False |
| TRG_R3L78-C12-393890-WCP-SEPARATOR-CUSTOMER-CALLOFF-FADE | 393890 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | C12 should not treat separator customer-calloff exposure as durable Stage2 unless customer order, utilization, shipment and margin bridge are visible. WCP had tradable MFE but then a deep post-peak drawdown, making it local 4B-watch rather than durable Green. | True | True |
| TRG_R3L13_C12_WCP_20230726_STAGE2_CAPPED | 393890 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_false_positive | False | False |
| TRG_R3L13_C12_WCP_20230726_STAGE2_CAPPED | 393890 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_false_positive | False | False |
| TRG_R3L73-C14-393890-WCP-SEPARATOR-CUSTOMER-DEMAND-LOCAL4B | 393890 | C14_EV_DEMAND_SLOWDOWN_4B_4C | Separator suppliers need stricter C14 treatment than diversified cell or chemical names. WCP produced initial MFE, but the later 180D MAE and post-peak drawdown show customer demand/utilization risk converting into local 4B-watch. | True | True |
| TRG_R3L73-C14-393890-WCP-SEPARATOR-CUSTOMER-DEMAND-LOCAL4B | 393890 | C14_EV_DEMAND_SLOWDOWN_4B_4C | Separator suppliers need stricter C14 treatment than diversified cell or chemical names. WCP produced initial MFE, but the later 180D MAE and post-peak drawdown show customer demand/utilization risk converting into local 4B-watch. | True | True |
| R13L13_ACC_X08_393890_20230726 | 393890 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | current_profile_false_positive | False | False |
| R11L11_T_402340_20240226_Stage2_Actionable | 402340 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_missed_structural | False | False |
| T_R9L15_403550_STAGE2_20220822 | 403550 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| TRG_R9L82-C29-403550-SOCAR-CARSHARING-UTILIZATION-MARGIN | 403550 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29 can protect car-sharing/platform mobility positives only when fleet utilization, active user demand, pricing, unit economics, revenue conversion and margin bridge are visible. Socar had controlled entry-basis MAE and strong MFE, but stock-web share count changes require validation before runtime promotion. | True | True |
| R13L15_X_TRIG_T_R9L15_403550_STAGE2_20220822 | 403550 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| T_R2L15_403870_GREEN_BLOWOFF_20240214 | 403870 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_false_positive | False | False |
| TRG_R2L79-C09-403870-HPSP-ADVANCED-EQUIPMENT-VALUATION-BLOWOFF | 403870 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | C09 should detect advanced-equipment valuation blowoff when a large MFE arrives before refreshed tool order, customer capacity and margin evidence. HPSP produced a huge early MFE and then a deep MAE/post-peak drawdown; runtime ingestion also needs share-count validation. | True | True |
| R13L15_T_R2L15_403870_GREEN_BLOWOFF_20240214 | 403870 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| TRG_R12L77-C31-407400-GGUMBI-LOW-BIRTH-BABYPRODUCT-THEME-FADE | 407400 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should not treat baby-product / low-birth policy theme spikes as durable Stage2 unless policy support maps to direct demand, channel sell-through, replenishment and margin bridge. Ggumbi produced an early MFE and then a severe drawdown path. | True | True |
| TRG_R11L81-C31-407400-GGUMBI-CHILDCARE-POLICY-THEME-FADE | 407400 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31 should not treat babycare/childcare policy beta as durable Stage2 unless direct beneficiary policy, customer demand, channel sell-through, product revenue and margin bridge are visible. Ggumbi produced a modest MFE but then a high-MAE drawdown. | True | True |
| R2L10_C08_TFE_T1 | 425420 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_false_positive | False | False |
| TRG_R2L78-C08-425420-TFE-TEST-SOCKET-CUSTOMER-QUALITY-LIFECYCLE | 425420 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | C08 should allow test-socket / probe-pin positives only when customer quality, HBM or advanced package qualification, reorder cadence and margin bridge are visible. TFE had strong early MFE, but the later drawdown means the signal must be lifecycle-managed if quality/reorder/margin evidence fades. | True | True |
| TRG_R2L81-C08-425420-TFE-TEST-SOCKET-CUSTOMER-QUALITY-LIFECYCLE | 425420 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | C08 should preserve test-socket/interface-board positives when customer quality, reorder visibility, capacity utilization, delivery cadence and margin bridge are visible. TFE produced a large MFE, but the later high-MAE drawdown forces lifecycle local 4B if reorder/margin evidence fades. | True | True |
| TR_C20_439090_20230608_IPO | 439090 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | False | False |
| TRG_R3L80-C12-450080-ECOPRO-MATERIALS-PRECURSOR-CALLOFF-FADE | 450080 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | C12 should not treat precursor/material contract beta as durable Stage2 unless customer call-off, volume visibility, utilization, pricing and margin bridge remain visible. Ecopro Materials had an early MFE but then opened a severe high-MAE drawdown path. | True | True |
| TRG_R12L73-C32-454910-DOOSANROBOTICS-VALUATION-BETA-LOCAL4B | 454910 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should cap the acquirer/beneficiary valuation beta when the proposed restructuring implies control benefit but no earnings or closing bridge. Doosan Robotics had a large first-day MFE and then severe MAE, so price-only governance beta should be local 4B-watch. | False | True |
| TRG_R12L73-C32-454910-DOOSANROBOTICS-VALUATION-BETA-LOCAL4B | 454910 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32 should cap the acquirer/beneficiary valuation beta when the proposed restructuring implies control benefit but no earnings or closing bridge. Doosan Robotics had a large first-day MFE and then severe MAE, so price-only governance beta should be local 4B-watch. | False | True |
| TRG_R7L73-C23-950210-PRESTIGE-BIOSIMILAR-APPROVAL-HEADLINE-CHASE | 950210 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | C23 should not convert a late approval/regulatory headline chase into durable Stage2 unless reimbursement, launch timing, partner orders and sales bridge are visible. The stock showed same-day MFE but later MAE and drawdown widened. | True | True |
| TRG_R7L73-C23-950210-PRESTIGE-BIOSIMILAR-APPROVAL-HEADLINE-CHASE | 950210 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | C23 should not convert a late approval/regulatory headline chase into durable Stage2 unless reimbursement, launch timing, partner orders and sales bridge are visible. The stock showed same-day MFE but later MAE and drawdown widened. | True | True |
| TRG_R7L78-C24-950220-NEOIMMUNETECH-IMMUNO-ONCOLOGY-DATA-FADE | 950220 | C24_BIO_TRIAL_DATA_EVENT_RISK | C24 should not treat immuno-oncology trial-data theme beta as durable Stage2 unless efficacy/safety, endpoint quality, regulatory path, financing runway and commercialization bridge are visible. NeoImmuneTech had a tradable spike but no durable rerating and then a broad drawdown path. | True | True |
| TRG_R7L74-C24-950220-NEOIMMUNETECH-IMMUNOTHERAPY-TRIAL-HEADLINE-FADE | 950220 | C24_BIO_TRIAL_DATA_EVENT_RISK | C24 should not treat immunotherapy trial/headline spikes as durable Stage2 unless data quality, endpoint durability, partner path or commercialization bridge is visible. NeoImmuneTech had large MFE but later collapsed into high MAE and post-peak drawdown. | True | True |
| TRG_R7L74-C24-950220-NEOIMMUNETECH-IMMUNOTHERAPY-TRIAL-HEADLINE-FADE | 950220 | C24_BIO_TRIAL_DATA_EVENT_RISK | C24 should not treat immunotherapy trial/headline spikes as durable Stage2 unless data quality, endpoint durability, partner path or commercialization bridge is visible. NeoImmuneTech had large MFE but later collapsed into high MAE and post-peak drawdown. | True | True |
| `R1L11_C05_000720_STAGE2A_20240125` | `000720` | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | False | False |
| `R1L11_C05_006360_4C_20230706` | `006360` | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | False | False |
| `R1L11_C05_047040_STAGE2WATCH_20240131` | `047040` | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | False | False |
| `R1L11_C05_375500_FALSEGREEN_20240110` | `375500` | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | False | False |
| TR_LSE_20240701_S2A | None | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_too_early | False | False |
| TR_LSE_20240723_4B | None | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_4B_too_early | False | False |
| R1L13_C03_010820_STAGE2WATCH_20220224 | None | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_false_positive | False | False |
| R1L13_C03_047810_STAGE2WATCH_20220720 | None | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_false_positive | False | False |
| R1L13_C03_012450_STAGE2A_20220302 | None | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | current_profile_too_late | False | False |
| C06_SKH_202310_Q3_HBM_CUSTOMER_TRACTION_STAGE2A | None | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_missed_structural | False | False |
| C06_SEC_202407_Q2_MEMORY_RECOVERY_NO_HBM_QUAL_FALSE_POSITIVE | None | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_false_positive | False | False |
| C06_SKH_202407_PRICE_ONLY_LOCAL_4B_OVERLAY | None | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_4B_too_early | False | False |
| C06_SEC_202410_HBM3E_DELAY_HARD4C_PROTECTION | None | C06_HBM_MEMORY_CUSTOMER_CAPACITY | current_profile_4C_too_late | False | False |
| R2L13_C07_253590_STAGE2WATCH_20240122 | None | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_false_positive | False | False |
| R2L13_C07_039440_STAGE2WATCH_20240213 | None | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_false_positive | False | False |
| R2L13_C07_042700_STAGE2A_20230925 | None | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_too_late | False | False |
| R2L13_C07_089030_STAGE2A_20240119 | None | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | current_profile_too_late | False | False |
| T_R2L14_098120_STAGE2A_20240122 | None | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_false_positive | False | False |
| T_R2L14_058470_STAGE2A_20240122 | None | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_too_early | False | False |
| T_R2L14_095340_STAGE2A_20240311 | None | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_false_positive | False | False |
| R2L11_C08_131290_STAGE2_20240424 | None | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_too_early | False | False |
| R2L11_C08_095340_GREENFALSE_20240308 | None | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_false_positive | False | False |
| R2L11_C08_058470_GREEN_20240412 | None | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_too_late | False | False |
| R2L11_C08_131290_GREEN_20240426 | None | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | current_profile_too_early | False | False |
| R13L13_C09_089030_S2A_2024-01-19 | None | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_4B_too_early | False | False |
| R13L13_C09_039030_S2A_2024-01-19 | None | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_4B_too_late | False | False |
| R13L13_C09_095340_THEME_2024-03-08 | None | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_false_positive | False | False |
| R13L13_C09_058470_THEME_2024-03-11 | None | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_false_positive | False | False |
| R13L13_C09_039030_4B_2024-04-12 | None | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_4B_too_late | False | False |
| R13L13_C09_095340_4C_2024-06-21 | None | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | current_profile_4C_too_late | False | False |
| R2L16_C10_084370_STAGE2A_2024-01-25 | None | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_too_late | False | False |
| R2L16_C10_036930_STAGE2WATCH_2024-02-28 | None | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_false_positive | False | False |
| R2L16_C10_095610_STAGE2WATCH_2024-04-02 | None | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_4B_too_late | False | False |
| R2L16_C10_095610_4B_WATCH_2024-04-17 | None | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | current_profile_4B_too_late | False | False |
| R3L12_T_LNF_STAGE2_20230302 | None | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive | False | False |
| R3L12_T_ECOPROBM_STAGE2_20231204 | None | C11_BATTERY_ORDERBOOK_RERATING | current_profile_false_positive | False | False |
| R3L69_C12_T03_STAGE2 | None | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_false_positive | False | False |
| R3L69_C12_T04_STAGE2 | None | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | current_profile_false_positive | False | False |
| R4L18-C17-KPIC-S2-2023-02-14 | None | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive | False | False |
| R4L18-C17-LOTTECHEM-S2-2023-02-14 | None | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive | False | False |
| R4L10-C17-OCI-S2A-20210215 | None | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_too_early | False | False |
| R4L10-C17-LOTTECHEM-S2A-20210223 | None | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive | False | False |
| R4L12-C17-KPIC-S2-20230302 | None | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive | False | False |
| R4L12-C17-LOTTE-S2-20230302 | None | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive | False | False |
| R5L12_C18_NONGSHIM_T2A_20230516 | None | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_too_late | False | False |
| R5L12_C18_ORION_T2_REJECT_20230428 | None | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | False | False |
| R5L12_C18_CJFOOD_T2_REJECT_20230510 | None | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_false_positive | False | False |
| R5L12_C18_NONGSHIM_GREEN_20231113 | None | C18_CONSUMER_EXPORT_CHANNEL_REORDER | current_profile_too_late | False | False |
| T-C19-110790-2022-05-16-4B | None | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_4B_too_late | False | False |
| T-C19-036620-2024-02-23-4B | None | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_4B_too_early | False | False |
| T-C19-111770-2022-08-16-S2A | None | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_too_late | False | False |
| T-C19-298540-2022-12-12-S2A | None | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_false_positive | False | False |
| T-C19-036620-2023-05-15-S2A | None | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_missed_structural | False | False |
| T-C19-383220-2023-02-15-GREEN-CAND | None | C19_BRAND_RETAIL_INVENTORY_MARGIN | current_profile_false_positive | False | False |
| R5L34_C20_090430_T_STAGE2_2024_04_26 | None | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | False | False |
| R5L34_C20_051900_T_STAGE2_2024_04_26 | None | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | False | False |
| T_C20_LGHH_20240510_WATCH | None | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | False | False |
| R5L10_C20_AMORE_T2_20210510 | None | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | False | False |
| R5L10_C20_LGHNH_T2_20210624 | None | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | False | False |
| R5L34_C20_257720_T_GREEN_2024_05_16 | None | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_too_late | False | False |
| R5L14_C20_090430_T1_STAGE2Y_2024-04-30 | None | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_false_positive | False | False |
| R5L34_C20_051900_T_4B_2024_05_23 | None | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_4B_too_late | False | False |
| R5L34_C20_090430_T_4B_2024_05_31 | None | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | current_profile_4B_too_late | False | False |
| R6L44-C21-003-T1 | None | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | False | False |
| R13L30_C21_WOORI_POLICY_S2_20240208 | None | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_early | False | False |
| R13L30_C21_BNK_POLICY_S2_20240208 | None | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_early | False | False |
| T-KAKAOBANK-S2-20250210 | None | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | False | True |
| T-BNK-S2A-20250113 | None | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_late | False | True |
| T-WOORI-S2A-20250210 | None | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_late | False | True |
| T_IBK_2025_04_25_STAGE2_ACTIONABLE | None | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_late | False | False |
| T_JBFG_2025_04_25_STAGE2_ACTIONABLE | None | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_late | False | False |
| T_KBFG_2025_04_25_STAGE2_ACTIONABLE | None | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_late | False | False |
| T_KAKAOBANK_2024_02_15_FALSE_POSITIVE | None | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | False | False |
| R6L60_C21_KAKAOBANK_POLICYONLY_20240226 | None | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | False | False |
| R13L30_C21_KB_GREEN_20240426 | None | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_late | False | False |
| R13L30_C21_WOORI_FALSE_GREEN_20240726 | None | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_false_positive | False | False |
| R13L30_C21_BNK_YELLOW_20240729 | None | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_too_late | False | False |
| R13L30_C21_KB_4B_20241025 | None | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | current_profile_4B_too_late | False | False |
| R7L46-HLB-20240517-4C | None | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_4C_too_late | False | False |
| T48_028300_20240517_4C_CRL | None | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_4C_too_late | False | False |
| HLB_4C_CRL_2024_05_17 | None | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_4C_too_late | False | False |
| T48_069620_20190207_STAGE2_APPROVAL_COUNTEREXAMPLE | None | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive | False | False |
| R7L46-ALT-20240223-S2A | None | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_missed_structural | False | False |
| R7L12_C23_HUGEL_STAGE2_APPROVAL_2024-03-04 | None | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_missed_structural | False | False |
| HUGEL_STAGE2_APPROVAL_2024_03_04 | None | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_too_late | False | False |
| R7L46-HLB-20240516-FPG | None | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive | False | False |
| R7L12_C23_YUHAN_STAGE2_APPROVAL_2024-08-20 | None | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_too_late | False | False |
| T-C23-YUHAN-STAGE2A-20240821 | None | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_too_late | False | False |
| T48_000100_20240821_STAGE2_APPROVAL | None | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_too_late | False | False |
| T48_028300_20240425_FALSE_GREEN_PDUFA_EXPECTATION | None | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive | False | False |
| T48_000100_20240828_STAGE3_GREEN_LATE | None | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_too_late | False | False |
| R7L12_C23_YUHAN_STAGE3_GREEN_2024-09-24 | None | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_too_late | False | False |
| T-C23-YUHAN-STAGE3G-20240924 | None | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_too_late | False | False |
| T-C23-HLB-STAGE3Y-20240321 | None | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive | False | False |
| R7L12_C23_HLB_PRE_CRL_EXPECTATION_2024-05-14 | None | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_false_positive | False | False |
| R7L12_C23_HUGEL_4B_POSITIONING_2024-11-06 | None | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_4B_too_late | False | False |
| T-C23-HUGEL-4B-20241106 | None | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_4B_too_late | False | False |
| R7L12_C23_HLB_4C_CRL_2024-05-17 | None | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_4C_too_late | False | False |
| T-C23-HLB-4C-20240517 | None | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | current_profile_4C_too_late | False | False |
| R7L15-C24-365270-T1 | None | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_4C_too_late | False | False |
| R7L15-C24-310210-T1 | None | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_too_late | False | False |
| R7L15-C24-288330-T1 | None | C24_BIO_TRIAL_DATA_EVENT_RISK | current_profile_false_positive | False | False |
| TRG_C26_KAKAO_2021_4B_REGULATORY_OVERLAY | None | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_4B_too_late | False | False |
| C26_SOOP_T2_4B_20240228 | None | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_4B_too_late | False | False |
| C26_KAKAO_T1_4C_20210908 | None | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_4C_too_late | False | False |
| TRG_C26_NAVER_2020_STAGE2_ACTIONABLE | None | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_too_late | False | False |
| C26_NASMEDIA_T1_STAGE2_20210205 | None | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| C26_INCROSS_T1_STAGE2_20210208 | None | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| TR_SOOP_20210430_S2A | None | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_too_late | False | False |
| TRG_C26_KAKAO_2021_STAGE2_ACTIONABLE | None | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_4B_too_late | False | False |
| TRG_C26_NASMEDIA_2021_STAGE2_ACTIONABLE | None | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| R8L13_C26_INCROSS_FALSE_2023-07-10 | None | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| R8L13_C26_NASMEDIA_FALSE_2023-07-10 | None | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| TRG_C26_NAVER_2023_11_06_STAGE2A | None | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_too_early | False | False |
| TRG_C26_KAKAO_2023_11_10_STAGE2A | None | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| TRG_C26_SOOP_2023_12_07_STAGE2A | None | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_missed_structural | False | False |
| C26_NAVER_T2_GREEN_20210623 | None | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_too_late | False | False |
| TR_KAKAO_20210624_GREEN | None | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| R8L13_C26_NAVER_GREEN_2024-01-10 | None | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_too_late | False | False |
| R8L13_C26_KAKAO_GREEN_2024-01-11 | None | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_too_late | False | False |
| TRG_C26_NAVER_2021_STAGE3_YELLOW_COMPARISON | None | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_too_late | False | False |
| C26_INCROSS_T2_YELLOW_20210329 | None | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_too_early | False | False |
| TRG_C26_NASMEDIA_2021_STAGE3_YELLOW_FALSE_POSITIVE | None | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| R8L21_C28_053800_T1_FALSE_STAGE2 | None | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_false_positive | False | False |
| R8L21_C28_263860_T1_STAGE2_ACTIONABLE | None | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | current_profile_4B_too_late | False | False |
| R9L14_C29_JEJUAIR_2023_REOPENING_FALSEBRIDGE_STAGE2_ACTIONABLE | None | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| R9L14_C29_JINAIR_2023_REOPENING_HIGHMAE_STAGE2_ACTIONABLE | None | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| R9L14_C29_TWAY_2023_ROUTE_VOLUME_FALSEBRIDGE_STAGE2_ACTIONABLE | None | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| R9L13_C29_MOBIS_2023_VOLUME_READTHROUGH | None | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| T_R9L12_089590_STAGE2_20230509 | None | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| T_R9L13_272450_STAGE2_20230515 | None | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_4C_too_late | False | False |
| T_R9L12_091810_STAGE2_20230515 | None | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_4C_too_late | False | False |
| R9L13_C29_HLMANDO_2023_CUSTOMER_WIN_FALSE_POSITIVE | None | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| T_R9L12_086280_STAGE2_20230608 | None | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_too_late | False | False |
| R9L13_C29_KAL_2023_REOPENING_VOLUME_COUNTER | None | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| T_R9L13_003490_STAGE2_20240130 | None | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | False | False |
| R9L14_C29_PAN_2021_DRYBULK_4B_OVERLAY | None | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_4B_too_late | False | False |
| T_R9L13_028670_4B_20210629 | None | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_4B_too_late | False | False |
| T_R9L13_000120_4B_20240202 | None | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_4B_too_late | False | False |
| R9L13_C29_KIA_2024_STAGE4B_OVERLAY | None | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_4B_too_late | False | False |
| R9L13_C29_HMC_2024_STAGE4B_OVERLAY | None | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_4B_too_late | False | False |
| T_R9L13_272450_4C_20231020 | None | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_4C_too_late | False | False |
| T_R9L12_091810_4C_20231024 | None | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_4C_too_late | False | False |
| R10L15_T003 | None | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_4C_too_late | False | False |
| R10L15_T002 | None | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_4C_too_late | False | False |
| R10L15_T001 | None | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_too_late | False | False |
| R10L11_T02_SHINSEGAE_STAGE2_PARENT_SUPPORT | None | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_missed_structural | False | False |
| R10L11_T01_DAEWOO_STAGE2_POLICY_BACKSTOP | None | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_missed_structural | False | False |
| R10L11_T04_KYERYONG_POLICY_BETA_CAP | None | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_too_early | False | False |
| R10L11_T03_DL_POLICY_BETA_CAP | None | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive | False | False |
| R10L11_T05_DONGBU_POLICY_BETA_CAP | None | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive | False | False |
| TRG_R10L12_047040_20221031_SECTOR_PF_PANIC_COUNTEREXAMPLE | None | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive | False | False |
| TRG_R10L12_375500_20231010_PF_DISCOUNT_REVERSAL_COUNTEREXAMPLE | None | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive | False | False |
| R10L15_T001G | None | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_too_late | False | False |
| R10L10_C30_DL_T1 | None | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_false_positive | False | False |
| TRG_R10L12_006360_20230706_4B_QUALITY_LEGAL_OVERLAY | None | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_4C_too_early | False | False |
| R10L11_T02B_SHINSEGAE_4B_EVENT_PREMIUM_OVERLAY | None | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | current_profile_4B_too_late | False | False |
| WELCRON_STAGE2_2020_01_20_FIRST_CASE | None | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| R12L12C31_250000_T1_STAGE2_ACTIONABLE | None | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_4B_too_late | False | False |
| R12L12C31_277410_T1_STAGE2_ACTIONABLE | None | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_4B_too_late | False | False |
| INSANGA_STAGE2_2023_06_07_SALT_PANIC | None | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| R12L12C31_011150_T1_RELEASE_ANNOUNCEMENT | None | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| R12L12C31_014710_T1_RELEASE_ANNOUNCEMENT | None | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| R11L13_C31_KVU_SCT_028260_STAGE2A_FALSE_20240226 | None | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| R11L13_C31_KVU_KEPCO_015760_STAGE2A_FALSE_20240226 | None | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_false_positive | False | False |
| SEEGENE_4B_2020_07_10_PRICE_ONLY_LOCAL_PEAK | None | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_4B_too_early | False | False |
| R12L12C31_250000_T2_4B_OVERLAY | None | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_4B_too_late | False | False |
| R12L12C31_277410_T2_4B_OVERLAY | None | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | current_profile_4B_too_late | False | False |
| R12L11C32_041510_T2_KAKAO_150K_TENDER_CAP_4B | None | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_4B_too_late | False | False |
| TR_C32_041510_4B_2023-03-08 | None | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_4B_too_late | False | False |
| R12L11C32_010130_T2_SHARE_ISSUE_FSS_4B | None | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_4B_too_late | False | False |
| TR_C32_010130_4B_2024-12-05 | None | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_4B_too_late | False | False |
| TR_C32_000240_4C_2023-12-15 | None | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_4C_too_late | False | False |
| R12L11C32_011200_T2_SALE_COLLAPSE_4C | None | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_4C_too_late | False | False |
| R12L11C32_008930_T2_PROXY_REVERSAL_4C | None | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_4C_too_late | False | False |
| R12L11C32_041510_SM_HYBE_KAKAO_TENDER_BATTLE_T1_STAGE2_ACTIONABLE | None | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_4B_too_late | False | False |
| TR_C32_041510_STAGE2_2023-02-10 | None | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive | False | False |
| TR_C32_000990_STAGE2_2023-03-08 | None | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_missed_structural | False | False |
| TR_C32_000240_STAGE2_2023-12-05 | None | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive | False | False |
| R12L11C32_011200_HMM_PREFERRED_BIDDER_FINANCING_OVERHANG_T1_STAGE2_ACTIONABLE | None | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive | False | False |
| R12L11C32_008930_HANMI_SCIENCE_OCI_INTEGRATION_PROXY_REVERSAL_T1_STAGE2_ACTIONABLE | None | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive | False | False |
| TR_C32_008930_STAGE2_2024-01-15 | None | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_false_positive | False | False |
| R12L11C32_010130_KOREA_ZINC_HOSTILE_TENDER_CONTROL_PREMIUM_T1_STAGE2_ACTIONABLE | None | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_4B_too_late | False | False |
| TR_C32_010130_STAGE2_2024-09-13 | None | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_too_early | False | False |
| TR_R13L44_KZ_4B_CAPITAL_RAISE_FSS_20241031 | None | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | current_profile_4B_too_early | False | False |
| R13L12_REDTEAM__R5L12_T04_HWASEUNG_20220516_FALSE_REORDER | None | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L12_REDTEAM__TRG-R3L12-066970-STAGE2A-20230228 | None | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L12_REDTEAM__T_R9L12_091810_STAGE2_20230515 | None | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4C_too_late | False | False |
| R13L12_REDTEAM__R12L12C31_011150_T1_RELEASE_ANNOUNCEMENT | None | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L12_REDTEAM__R11L12_C32_HMM_2023_T1 | None | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L12_REDTEAM__R6L12_T03_HYUNDAIMARINE_20240202_FALSE_STAGE2_RATE_BETA_RESERVE_GUARD | None | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L12_REDTEAM__R1L12_C04_100840_CZECH_HEAT_EXCHANGER_SUPPLY_CHAIN_STAGE2_ACTIONABLE | None | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_too_late | False | False |
| R13L12_REDTEAM__R1L12_C04_052690_CZECH_DESIGN_PURE_PLAY_SPIKE_STAGE2_ACTIONABLE | None | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L12_REDTEAM__R7L12_C23_YUHAN_STAGE2_APPROVAL_2024-08-20 | None | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_too_late | False | False |
| R13L12_REDTEAM__R8L12_C28_AHNLAB_T1_PRICE_ONLY_BLOWOFF_2022-03-23 | None | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L12_REDTEAM__R2L12_T04_DI_STAGE3_FALSE_GREEN_TESTER_THEME | None | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L12_REDTEAM__R7L12_C23_HLB_PRE_CRL_EXPECTATION_2024-05-14 | None | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_false_positive | False | False |
| R13L12_REDTEAM__TR-C30-294870-4C-20220112 | None | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | current_profile_4C_too_late | False | False |
