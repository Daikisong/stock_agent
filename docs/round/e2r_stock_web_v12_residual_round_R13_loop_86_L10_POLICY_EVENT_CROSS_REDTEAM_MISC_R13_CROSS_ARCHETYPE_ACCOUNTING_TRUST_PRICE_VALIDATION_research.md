# E2R Stock-Web v12 Residual Research — R13 Loop 86 / L10 / Price Validation Checkpoint

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R13",
  "scheduled_loop": 86,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R13",
  "completed_loop": 86,
  "computed_next_round": "R1",
  "computed_next_loop": 87,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION",
  "fine_archetype_id": "LOOP86_STOCK_WEB_PRICE_CA_SOURCE_PROXY_4B_4C_VALIDATION_CHECKPOINT",
  "loop_objective": [
    "cross_archetype_price_validation_checkpoint",
    "corporate_action_window_caveat_review",
    "source_proxy_runtime_promotion_blocker_review",
    "local_4B_vs_full_4B_vs_hard_4C_routing_review",
    "high_MAE_guardrail_review",
    "positive_path_not_green_without_bridge_review",
    "dedupe_and_independent_evidence_weight_review",
    "canonical_bridge_family_compression",
    "do_not_count_as_new_sector_case",
    "do_not_propose_new_weight_delta"
  ],
  "source_round_span": "R1~R12 loop 86",
  "source_md_count": 12,
  "source_trigger_count": 36,
  "source_false_positive_trigger_count": 19,
  "source_positive_trigger_count": 17,
  "price_source": "Songdaiki/stock-web",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "stock_web_manifest_max_date": "2026-02-20",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "handoff_prompt_executed_now": false,
  "do_not_propose_new_weight_delta": true,
  "do_not_count_as_new_case": true,
  "do_not_count_as_new_sector_case": true
}
```

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_executed_now = false
```

This file is a standalone R13 cross-archetype checkpoint. It does not patch `stock_agent`, does not run live discovery, and does not propose immediate production scoring changes.

## 2. R13 Scope Resolution

```text
scheduled_round = R13
scheduled_loop = 86
allowed_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC only
selected_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
selected_canonical_archetype_id = R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
computed_next_round = R1
computed_next_loop = 87
round_schedule_status = valid
round_sector_consistency = pass
```

R13 is not a new sector research round. It is a cross-archetype RedTeam checkpoint. Therefore this MD does not add new positive cases, does not add new symbols, and does not count source cases again.

```text
new_independent_case_count = 0
new_symbol_count = 0
do_not_count_as_new_case = true
do_not_count_as_new_sector_case = true
```

## 3. No-Repeat / Duplicate Handling

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
R13_cross_case_policy = do_not_count_as_new_case=true
```

No-Repeat shows the R13 accounting / price validation bucket has only 12 rows / 12 symbols, while 4B/4C RedTeam is already much thicker. This makes `R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION` a useful loop86 checkpoint.

## 4. Stock-Web Price Source Context

```text
price_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
```

R13 does not compute a fresh OHLC entry window. It inherits the Stock-Web validations and trigger-level MFE/MAE calculations from R1~R12 loop86 source MDs.

## 5. Source MD Inventory — Loop 86

| round | large_sector_id | source canonical | positives | false positives | source proxy rows | CA caveat rows | fine route |
|---|---|---|---:|---:|---:|---:|---|
| R1 | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 1 | 2 | 3 | 3 | CZECH_NUCLEAR_POLICY_PROJECT_EQUIPMENT_SUPPLY_LEGAL_DELAY_MARGIN_BRIDGE_VS_NUCLEAR_THEME_FADE |
| R2 | L2_AI_SEMICONDUCTOR_ELECTRONICS | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 1 | 2 | 3 | 3 | OVERLAY_METROLOGY_ETCH_EQUIPMENT_SIC_PARTS_RELATIVE_STRENGTH_ORDER_ACCEPTANCE_REVENUE_BRIDGE_VS_EQUIPMENT_THEME_BLOWOFF_FADE |
| R3 | L3_BATTERY_EV_GREEN_MOBILITY | C11_BATTERY_ORDERBOOK_RERATING | 2 | 1 | 3 | 3 | CELL_CATHODE_PRECURSOR_ORDERBOOK_CAPACITY_UTILIZATION_CUSTOMER_CALLOFF_MARGIN_BRIDGE_VS_SPECULATIVE_BATTERY_THEME_FADE |
| R4 | L4_MATERIALS_SPREAD_RESOURCE | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | 1 | 2 | 3 | 3 | COPPER_RARE_EARTH_NICKEL_STRATEGIC_RESOURCE_POLICY_SUPPLY_PROJECT_ECONOMICS_BRIDGE_VS_THEME_SPIKE_FADE |
| R5 | L5_CONSUMER_BRAND_DISTRIBUTION | C19_BRAND_RETAIL_INVENTORY_MARGIN | 2 | 1 | 3 | 3 | ATHLEISURE_FASHION_BEAUTY_BRAND_INVENTORY_NORMALIZATION_SELLTHROUGH_ARPU_MARGIN_BRIDGE_VS_RETAIL_THEME_FADE |
| R6 | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C22_INSURANCE_RATE_CYCLE_RESERVE | 1 | 2 | 3 | 3 | REINSURANCE_NONLIFE_SMALL_INSURANCE_RATE_RESERVE_CAPITAL_BUFFER_PAYOUT_BRIDGE_VS_VALUEUP_THEME_SPIKE_FADE |
| R7 | L7_BIO_HEALTHCARE_MEDICAL | C24_BIO_TRIAL_DATA_EVENT_RISK | 2 | 1 | 3 | 3 | ADC_BIOSIMILAR_CELL_THERAPY_TRIAL_DATA_LICENSE_MILESTONE_REIMBURSEMENT_BRIDGE_VS_EVENT_BLOWOFF_FADE |
| R8 | L8_PLATFORM_CONTENT_SW_SECURITY | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 1 | 2 | 3 | 3 | DATA_SECURITY_AUTHENTICATION_THREAT_INTELLIGENCE_CONTRACT_RETENTION_ARR_RENEWAL_MARGIN_BRIDGE_VS_SECURITY_AI_THEME_FADE |
| R9 | L3_BATTERY_EV_GREEN_MOBILITY | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 2 | 1 | 3 | 3 | HYBRID_CANISTER_SEAT_INTERIOR_AUTO_PARTS_VOLUME_PLATFORM_MIX_MARGIN_BRIDGE_VS_AUTO_PARTS_THEME_FADE |
| R10 | L9_CONSTRUCTION_REALESTATE_HOUSING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 1 | 2 | 3 | 3 | LARGE_DEVELOPER_BUILDING_MATERIALS_MID_BUILDER_PF_DEBT_ORDERBOOK_CASHFLOW_MARGIN_BRIDGE_VS_VALUEUP_HOUSING_THEME_FADE |
| R11 | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 2 | 1 | 3 | 3 | TENDER_OFFER_DELISTING_CONTROL_PREMIUM_ACCEPTANCE_THRESHOLD_CAP_VS_TENDER_CAP_LOW_MFE_FADE |
| R12 | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 1 | 2 | 3 | 3 | AGRI_FOOD_GRAIN_INPUT_COST_SUPPLY_POLICY_MARGIN_BRIDGE_VS_FEED_GRAIN_THEME_SPIKE_FADE |

## 6. Aggregate Trigger Statistics

```json
{
  "source_md_count": 12,
  "source_trigger_count": 36,
  "source_case_count": 36,
  "positive_trigger_count": 17,
  "false_positive_trigger_count": 19,
  "source_proxy_trigger_count": 36,
  "corporate_action_caveat_trigger_count": 36,
  "no_profile_CA_candidate_or_clean_profile_trigger_count": 8,
  "local_4B_watch_trigger_count": 18,
  "hard_4C_non_price_protection_label_count": 36,
  "high_MAE_180D_leq_minus30_count": 12,
  "all_avg_MFE90": 35.91,
  "all_avg_MAE90": -13.37,
  "all_avg_MFE180": 42.97,
  "all_avg_MAE180": -23.98,
  "positive_avg_MFE90": 57.07,
  "positive_avg_MAE90": -6.41,
  "positive_avg_MFE180": 71.66,
  "positive_avg_MAE180": -12.27,
  "false_positive_avg_MFE90": 16.97,
  "false_positive_avg_MAE90": -19.6,
  "false_positive_avg_MFE180": 17.3,
  "false_positive_avg_MAE180": -34.45,
  "worst_MAE180": -54.25,
  "best_MFE180": 201.31
}
```

Loop86 produced 36 source triggers across 12 MDs. The cross-checkpoint shape is:

```text
actual Stock-Web price row
+ source_proxy_only evidence
+ raw_unadjusted_marcap caveat
+ CA-window caveat where applicable
+ MFE/MAE and post-peak drawdown
= calibration usable, but not runtime-promotion ready
```

## 7. Worst MAE / Price-Trust Review Rows

| source round | symbol | company | canonical | MFE180 | MAE180 | CA/window status | outcome |
|---|---:|---|---|---:|---:|---|---|
| R8 | 411080 | 샌즈랩 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 30.59 | -54.25 | clean_2024_window_no_profile_CA_candidate | security_AI_theme_MFE_then_deep_MAE_false_positive |
| R3 | 001570 | 금양 | C11_BATTERY_ORDERBOOK_RERATING | 61.76 | -51.57 | clean_2024_window_after_old_2007_CA_candidate | large_theme_MFE_then_deep_MAE_speculative_battery_false_positive |
| R2 | 322310 | 오로스테크놀로지 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 30.61 | -51.51 | clean_2024_window_no_profile_CA_candidate | early_equipment_MFE_then_deep_MAE_false_positive |
| R7 | 174900 | 앱클론 | C24_BIO_TRIAL_DATA_EVENT_RISK | 4.98 | -48.67 | clean_2024_window_after_old_2020_CA_candidates | trial_data_MFE_then_high_MAE_event_risk_false_positive |
| R1 | 011700 | 한신기계 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 14.94 | -48.53 | clean_2024_2025_window_after_old_2006_CA_candidate | same_day_MFE_then_deep_MAE_nuclear_theme_false_positive |
| R9 | 024900 | 덕양산업 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 17.37 | -42.94 | clean_2024_window_after_old_2014_CA_candidate | theme_MFE_then_deep_MAE_auto_interior_false_positive |
| R6 | 000540 | 흥국화재 | C22_INSURANCE_RATE_CYCLE_RESERVE | 25.0 | -39.39 | clean_2024_window_after_old_2011_CA_candidate | large_same_week_MFE_then_deep_MAE_small_insurance_false_positive |
| R10 | 002990 | 금호건설 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 0.97 | -38.61 | clean_2024_window_after_old_2013_CA_candidates | very_low_MFE_deep_MAE_mid_builder_PF_theme_false_positive |
| R3 | 005070 | 코스모신소재 | C11_BATTERY_ORDERBOOK_RERATING | 23.68 | -38.57 | clean_2024_window_after_old_2019_CA_candidate | cathode_MFE_positive_but_later_high_MAE_margin_bridge_watch_required |
| R8 | 203650 | 드림시큐리티 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 9.4 | -38.39 | clean_2024_window_after_old_2019_CA_candidate | low_MFE_high_MAE_authentication_security_theme_false_positive |
| R2 | 089970 | 브이엠 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 34.94 | -36.69 | clean_2024_window_no_profile_CA_candidate | equipment_cycle_MFE_then_high_MAE_theme_fade |
| R12 | 002140 | 고려산업 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 17.31 | -32.05 | clean_2024_window_after_old_2013_CA_candidate | same_week_grain_theme_MFE_then_deep_MAE_false_positive |

## 8. Highest MFE Rows Needing 4B / Bridge Watch

| source round | symbol | company | canonical | MFE180 | MAE180 | 4B verdict |
|---|---:|---|---|---:|---:|---|
| R11 | 036560 | 영풍정밀 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 201.31 | 0.0 | local_4B_watch_after_tender_war_MFE_if_offer_escalation_acceptance_control_bridge_stalls |
| R1 | 083650 | 비에이치아이 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 181.5 | -20.54 | local_4B_watch_after_nuclear_project_MFE_if_named_order_legal_margin_bridge_stalls |
| R7 | 000250 | 삼천당제약 | C24_BIO_TRIAL_DATA_EVENT_RISK | 165.9 | -10.06 | local_4B_watch_after_biosimilar_event_MFE_if_regulatory_license_reimbursement_margin_bridge_stalls |
| R5 | 337930 | 브랜드엑스코퍼레이션 | C19_BRAND_RETAIL_INVENTORY_MARGIN | 112.72 | -6.99 | local_4B_watch_after_DTC_brand_MFE_if_sellthrough_inventory_margin_bridge_stalls |
| R8 | 150900 | 파수 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 101.94 | -25.78 | local_4B_watch_after_security_SW_MFE_if_ARR_renewal_margin_bridge_stalls |
| R7 | 141080 | 리가켐바이오 | C24_BIO_TRIAL_DATA_EVENT_RISK | 74.17 | -11.39 | local_4B_watch_after_ADC_event_MFE_if_data_quality_milestone_commercial_bridge_stalls |
| R4 | 103140 | 풍산 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | 68.33 | -3.9 | local_4B_watch_after_copper_resource_MFE_if_product_spread_inventory_margin_bridge_stalls |
| R3 | 001570 | 금양 | C11_BATTERY_ORDERBOOK_RERATING | 61.76 | -51.57 | speculative_battery_theme_MFE_rejected_or_local_4B_watch_without_customer_orderbook_revenue_margin_bridge |

## 9. Corporate-Action / Price Window Caveat Sample

| source round | symbol | company | corporate-action window status | profile path | usable |
|---|---:|---|---|---|---|
| R1 | 083650 | 비에이치아이 | clean_2024_2025_window_after_old_2015_CA_candidates | atlas/symbol_profiles/083/083650.json | True |
| R1 | 011700 | 한신기계 | clean_2024_2025_window_after_old_2006_CA_candidate | atlas/symbol_profiles/011/011700.json | True |
| R1 | 046120 | 오르비텍 | clean_2024_2025_window_after_old_2017_CA_candidate | atlas/symbol_profiles/046/046120.json | True |
| R2 | 064760 | 티씨케이 | clean_2024_window_no_profile_CA_candidate | atlas/symbol_profiles/064/064760.json | True |
| R2 | 322310 | 오로스테크놀로지 | clean_2024_window_no_profile_CA_candidate | atlas/symbol_profiles/322/322310.json | True |
| R2 | 089970 | 브이엠 | clean_2024_window_no_profile_CA_candidate | atlas/symbol_profiles/089/089970.json | True |
| R3 | 006400 | 삼성SDI | clean_2024_window_after_old_2014_CA_candidate | atlas/symbol_profiles/006/006400.json | True |
| R3 | 005070 | 코스모신소재 | clean_2024_window_after_old_2019_CA_candidate | atlas/symbol_profiles/005/005070.json | True |
| R3 | 001570 | 금양 | clean_2024_window_after_old_2007_CA_candidate | atlas/symbol_profiles/001/001570.json | True |
| R4 | 103140 | 풍산 | clean_2024_window_no_profile_CA_candidate | atlas/symbol_profiles/103/103140.json | True |
| R4 | 047400 | 유니온머티리얼 | clean_2024_window_after_old_2011_CA_candidate | atlas/symbol_profiles/047/047400.json | True |
| R4 | 032560 | 황금에스티 | clean_2024_window_after_old_2010_CA_candidates | atlas/symbol_profiles/032/032560.json | True |
| R5 | 337930 | 브랜드엑스코퍼레이션 | clean_2024_2025_window_after_old_2021_CA_candidate | atlas/symbol_profiles/337/337930.json | True |
| R5 | 093050 | LF | clean_2024_window_no_profile_CA_candidate | atlas/symbol_profiles/093/093050.json | True |
| R5 | 031430 | 신세계인터내셔날 | clean_2024_window_after_old_2022_CA_candidate | atlas/symbol_profiles/031/031430.json | True |
| R6 | 003690 | 코리안리 | clean_2024_window_after_old_2004_CA_candidate | atlas/symbol_profiles/003/003690.json | True |

## 10. Cross-Archetype Checkpoint Rows

| cross_case_id | cross_scope | decision | verdict |
|---|---|---|---|
| R13L86-PRICE-01 | corporate_action_window_validation | use_clean_or_post_CA_windows_only | stock_web_usable_with_CA_caveat_not_auto_promotion |
| R13L86-PRICE-02 | source_proxy_runtime_promotion_blocker | hold_shadow_only_until_primary_evidence_repair | block_runtime_promotion_until_source_repair |
| R13L86-PRICE-03 | local_4B_vs_hard_4C_routing | allow_local_4B_watch_keep_hard_4C_non_price_only | local_4B_allowed_hard_4C_requires_non_price_break |
| R13L86-PRICE-04 | high_MAE_guardrail_review | block_clean_green_when_MAE_or_post_peak_drawdown_is_deep | high_MAE_blocks_clean_Green |
| R13L86-PRICE-05 | canonical_specific_bridge_family_compression | keep_bridge_rules_canonical_specific_not_global_weight | do_not_apply_new_global_weight |
| R13L86-PRICE-06 | dedupe_and_independent_evidence_review | do_not_count_R13_as_new_case | R13_cross_checkpoint_only |

## 11. Finding 1 — Stock-Web Price Is Usable, But Only With Window Hygiene

The source MDs repeatedly validate that Stock-Web 1D OHLC is useful for historical calibration. But raw/unadjusted marcap rows are not magically split-adjusted. Corporate-action windows must be checked at profile level, and selected trigger windows must be clean or explicitly post-event.

```text
price_path = usable for calibration
corporate_action_candidate = window caveat required
raw_unadjusted_marcap = never production-promotion proof by itself
```

## 12. Finding 2 — Source Proxy Blocks Runtime Promotion

All loop86 source MDs are `source_proxy_only / evidence_url_pending`.

```text
source_proxy_only = calibration ledger allowed
source_proxy_only != runtime scoring promotion
evidence_url_pending = source-repair queue
```

Price can show that a trigger was worth studying. It cannot prove publication timing, direct beneficiary mapping, contract terms, order quality, reserve quality, inventory margin, tender threshold, or regulatory path.

## 13. Finding 3 — Local 4B Is A Speed Warning, Hard 4C Is A Thesis Break

Loop86 has many rows where MFE was large but post-peak drawdown later became large. These should not be promoted to hard 4C unless there is non-price evidence.

```text
local_4B_watch = allowed when MFE outruns the bridge
full_4B = requires non-price deterioration
hard_4C = requires confirmed thesis break
```

Hard 4C candidates need evidence like tender failure, customer order loss, reserve/capital break, regulatory failure, project-loss break, inventory impairment, pass-through failure, or margin thesis break.

## 14. Finding 4 — High MAE Blocks Clean Green Even For Positives

Positive rows can still be non-Green:

```text
positive_avg_MFE180 = 71.66%
positive_avg_MAE180 = -12.27%
```

That profile is useful, but it is not clean Green without bridge repair. High MAE turns the signal into Stage2-Actionable + RiskWatch, not Stage3-Green.

## 15. Finding 5 — Canonical Bridge Family Beats A Global Penalty

The same pattern repeats, but the proof grammar differs by canonical:

```text
C04 = named nuclear order + legal clearance + schedule + margin
C07 = named customer order + acceptance + delivery + utilization + margin
C11 = customer orderbook + call-off + utilization + ASP/cost spread + margin
C16 = direct beneficiary + product/resource spread + inventory + margin
C19 = sell-through + inventory turns + reorder + discount control + margin
C22 = reserve adequacy + combined ratio + capital buffer + payout
C24 = data durability + regulatory path + partner milestone + commercial bridge
C28 = contract wins + ARR + renewal retention + margin
C29 = platform mix + OEM volume + utilization + cost spread + margin
C30 = PF refinancing + debt/liquidity + orderbook + cash-flow + project margin
C31 = policy/supply + input cost + inventory + pricing pass-through + margin
C32 = tender price + residual spread + acceptance threshold + delisting/control path
```

A blunt global penalty would flatten the map. The correct repair is canonical-specific grammar plus source repair.

## 16. Before / After Cross-Checkpoint Comparison

| checkpoint profile | new independent cases | price handling | source handling | 4B/4C routing | production impact |
|---|---:|---|---|---|---|
| P0 current calibrated proxy | 0 | price path can tempt over-promotion | source proxy may tempt promotion | full 4B/4C can be late/misrouted | none |
| P1 R13 loop86 price-validation checkpoint | 0 | CA-window hygiene required | source repair mandatory | local 4B allowed, hard 4C non-price only | none |

## 17. Score-Return Alignment Matrix

| cross_case_id | weighted before | label before | weighted after | label after | alignment |
|---|---:|---|---:|---|---|
| R13L86-PRICE-01 | 62 | Potential calibration row | 72 | Calibration usable only with CA-window caveat | improved |
| R13L86-PRICE-02 | 66 | Stage2-Actionable candidate | 48 | Hold: source-repair queue | improved |
| R13L86-PRICE-03 | 64 | possible full 4B / possible price-only 4C | 76 | Local 4B Watch; hard 4C blocked until non-price break | improved |
| R13L86-PRICE-04 | 72 | Stage2-Actionable / possible Green | 68 | Stage2-Actionable + high-MAE/local-4B watch | improved |
| R13L86-PRICE-05 | 60 | possible new global rule | 74 | Canonical-specific shadow family only | improved |
| R13L86-PRICE-06 | 50 | Could double-count source MDs | 80 | do_not_count_as_new_case=true; independent_evidence_weight=0.0 | improved |

## 18. Coverage Matrix

| large_sector_id | canonical_archetype_id | positive | counterexample | 4B | 4C | new cases | reused source MDs | usable cross triggers | current errors | sector rule | canonical rule | coverage gap after |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | 0 | 0 | 1-watch family | 1-watch family | 0 | 12 | 6 | 6 | no | cross checkpoint only | source repair / CA ledger audit |

## 19. Residual Contribution Summary

```text
new_independent_case_count: 0
reused_case_count: 12
reused_case_ids: R1~R12 loop86 source MDs
new_symbol_count: 0
new_canonical_archetype_count: 0
new_fine_archetype_count: 0
new_trigger_family_count: 0
source_trigger_count: 36
source_positive_trigger_count: 17
source_false_positive_trigger_count: 19
source_proxy_trigger_count: 36
corporate_action_caveat_trigger_count: 36
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
  - source_proxy_only_blocks_runtime_promotion
  - high_MAE_guardrail
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
residual_error_types_found:
  - raw_unadjusted_stock_web_CA_window_caveat_required
  - source_proxy_runtime_promotion_risk
  - local_4B_vs_hard_4C_misroute_risk
  - high_MAE_blocks_clean_Green
  - canonical_bridge_family_required_not_global_weight
  - R13_double_counting_risk
new_axis_proposed: false
existing_axis_strengthened:
  - source_proxy_only_blocks_runtime_promotion
  - high_MAE_blocks_clean_Green
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
  - hard_4C_requires_non_price_thesis_break
  - corporate_action_window_caveat_required
existing_axis_weakened: null
existing_axis_kept:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: null
canonical_archetype_rule_candidate: R13_cross_checkpoint_only
no_new_signal_reason: R13 is cross-archetype checkpoint, not sector research
loop_contribution_label: cross_archetype_accounting_trust_price_validation
do_not_propose_new_weight_delta: true
do_not_count_as_new_case: true
```

## 20. Validation Scope / Non-Validation Scope

Validated in this MD:

```text
- R13 scheduled round/loop consistency
- R13 large_sector_id hard gate
- R13 canonical scope
- source MD inventory for loop86 R1~R12
- aggregate source trigger counts
- Stock-Web price source usage inherited from source MDs
- corporate-action window caveat policy
- source-proxy runtime blocker principle
- local-vs-full 4B distinction
- hard 4C non-price thesis-break principle
- do_not_count_as_new_case policy
```

Not validated in this MD:

```text
- new primary evidence URL
- new OHLC entry window
- new independent case
- new stock symbol
- production scoring implementation
- code patch
```

## 21. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,R13_loop86_price_CA_source_proxy_local4B_hard4C_validation_checkpoint,cross_archetype_checkpoint_only,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION,0,1,+1,"Loop86 R1~R12 rows repeatedly show Stock-Web price rows are usable for calibration with CA-window caveats, source_proxy_only must not promote, local 4B can precede full 4B, and hard 4C requires non-price thesis break","no production weight; reinforces price validation, source repair, high-MAE and 4B/4C guardrails","R13L86-PRICE-01-CA-WINDOW-USABLE-NOT-PROMOTION|R13L86-PRICE-02-SOURCE-PROXY-BLOCKER|R13L86-PRICE-03-LOCAL-4B-YES-HARD-4C-NO|R13L86-PRICE-04-HIGH-MAE-GUARDRAIL|R13L86-PRICE-05-CANONICAL-BRIDGE-FAMILY|R13L86-PRICE-06-DEDUPE-INDEPENDENCE",6,0,0,medium,r13_cross_checkpoint_shadow_only,"do_not_count_as_new_case=true; source repair required; not production"
```

## 22. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "cross_checkpoint_uses_source_MD_price_validations"}
{"row_type": "narrative_only", "narrative_id": "R13L86-SOURCE-R1", "round": "R13", "loop": 86, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION", "source_round": "R1", "source_file": "e2r_stock_web_v12_residual_round_R1_loop_86_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_research.md", "source_large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "source_canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "source_fine_archetype_id": "CZECH_NUCLEAR_POLICY_PROJECT_EQUIPMENT_SUPPLY_LEGAL_DELAY_MARGIN_BRIDGE_VS_NUCLEAR_THEME_FADE", "trigger_count": 3, "positive_count": 1, "false_positive_count": 2, "source_proxy_trigger_count": 3, "ca_caveat_count": 3, "do_not_count_as_new_case": true, "calibration_usable": false, "notes": "R13 source inventory row; used for cross-checkpoint only"}
{"row_type": "narrative_only", "narrative_id": "R13L86-SOURCE-R2", "round": "R13", "loop": 86, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION", "source_round": "R2", "source_file": "e2r_stock_web_v12_residual_round_R2_loop_86_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md", "source_large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "source_canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "source_fine_archetype_id": "OVERLAY_METROLOGY_ETCH_EQUIPMENT_SIC_PARTS_RELATIVE_STRENGTH_ORDER_ACCEPTANCE_REVENUE_BRIDGE_VS_EQUIPMENT_THEME_BLOWOFF_FADE", "trigger_count": 3, "positive_count": 1, "false_positive_count": 2, "source_proxy_trigger_count": 3, "ca_caveat_count": 3, "do_not_count_as_new_case": true, "calibration_usable": false, "notes": "R13 source inventory row; used for cross-checkpoint only"}
{"row_type": "narrative_only", "narrative_id": "R13L86-SOURCE-R3", "round": "R13", "loop": 86, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION", "source_round": "R3", "source_file": "e2r_stock_web_v12_residual_round_R3_loop_86_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md", "source_large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "source_canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "source_fine_archetype_id": "CELL_CATHODE_PRECURSOR_ORDERBOOK_CAPACITY_UTILIZATION_CUSTOMER_CALLOFF_MARGIN_BRIDGE_VS_SPECULATIVE_BATTERY_THEME_FADE", "trigger_count": 3, "positive_count": 2, "false_positive_count": 1, "source_proxy_trigger_count": 3, "ca_caveat_count": 3, "do_not_count_as_new_case": true, "calibration_usable": false, "notes": "R13 source inventory row; used for cross-checkpoint only"}
{"row_type": "narrative_only", "narrative_id": "R13L86-SOURCE-R4", "round": "R13", "loop": 86, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION", "source_round": "R4", "source_file": "e2r_stock_web_v12_residual_round_R4_loop_86_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md", "source_large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "source_canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "source_fine_archetype_id": "COPPER_RARE_EARTH_NICKEL_STRATEGIC_RESOURCE_POLICY_SUPPLY_PROJECT_ECONOMICS_BRIDGE_VS_THEME_SPIKE_FADE", "trigger_count": 3, "positive_count": 1, "false_positive_count": 2, "source_proxy_trigger_count": 3, "ca_caveat_count": 3, "do_not_count_as_new_case": true, "calibration_usable": false, "notes": "R13 source inventory row; used for cross-checkpoint only"}
{"row_type": "narrative_only", "narrative_id": "R13L86-SOURCE-R5", "round": "R13", "loop": 86, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION", "source_round": "R5", "source_file": "e2r_stock_web_v12_residual_round_R5_loop_86_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md", "source_large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "source_canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "source_fine_archetype_id": "ATHLEISURE_FASHION_BEAUTY_BRAND_INVENTORY_NORMALIZATION_SELLTHROUGH_ARPU_MARGIN_BRIDGE_VS_RETAIL_THEME_FADE", "trigger_count": 3, "positive_count": 2, "false_positive_count": 1, "source_proxy_trigger_count": 3, "ca_caveat_count": 3, "do_not_count_as_new_case": true, "calibration_usable": false, "notes": "R13 source inventory row; used for cross-checkpoint only"}
{"row_type": "narrative_only", "narrative_id": "R13L86-SOURCE-R6", "round": "R13", "loop": 86, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION", "source_round": "R6", "source_file": "e2r_stock_web_v12_residual_round_R6_loop_86_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md", "source_large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "source_canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "source_fine_archetype_id": "REINSURANCE_NONLIFE_SMALL_INSURANCE_RATE_RESERVE_CAPITAL_BUFFER_PAYOUT_BRIDGE_VS_VALUEUP_THEME_SPIKE_FADE", "trigger_count": 3, "positive_count": 1, "false_positive_count": 2, "source_proxy_trigger_count": 3, "ca_caveat_count": 3, "do_not_count_as_new_case": true, "calibration_usable": false, "notes": "R13 source inventory row; used for cross-checkpoint only"}
{"row_type": "narrative_only", "narrative_id": "R13L86-SOURCE-R7", "round": "R13", "loop": 86, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION", "source_round": "R7", "source_file": "e2r_stock_web_v12_residual_round_R7_loop_86_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md", "source_large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "source_canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "source_fine_archetype_id": "ADC_BIOSIMILAR_CELL_THERAPY_TRIAL_DATA_LICENSE_MILESTONE_REIMBURSEMENT_BRIDGE_VS_EVENT_BLOWOFF_FADE", "trigger_count": 3, "positive_count": 2, "false_positive_count": 1, "source_proxy_trigger_count": 3, "ca_caveat_count": 3, "do_not_count_as_new_case": true, "calibration_usable": false, "notes": "R13 source inventory row; used for cross-checkpoint only"}
{"row_type": "narrative_only", "narrative_id": "R13L86-SOURCE-R8", "round": "R13", "loop": 86, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION", "source_round": "R8", "source_file": "e2r_stock_web_v12_residual_round_R8_loop_86_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md", "source_large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "source_canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "source_fine_archetype_id": "DATA_SECURITY_AUTHENTICATION_THREAT_INTELLIGENCE_CONTRACT_RETENTION_ARR_RENEWAL_MARGIN_BRIDGE_VS_SECURITY_AI_THEME_FADE", "trigger_count": 3, "positive_count": 1, "false_positive_count": 2, "source_proxy_trigger_count": 3, "ca_caveat_count": 3, "do_not_count_as_new_case": true, "calibration_usable": false, "notes": "R13 source inventory row; used for cross-checkpoint only"}
{"row_type": "narrative_only", "narrative_id": "R13L86-SOURCE-R9", "round": "R13", "loop": 86, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION", "source_round": "R9", "source_file": "e2r_stock_web_v12_residual_round_R9_loop_86_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md", "source_large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "source_canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "source_fine_archetype_id": "HYBRID_CANISTER_SEAT_INTERIOR_AUTO_PARTS_VOLUME_PLATFORM_MIX_MARGIN_BRIDGE_VS_AUTO_PARTS_THEME_FADE", "trigger_count": 3, "positive_count": 2, "false_positive_count": 1, "source_proxy_trigger_count": 3, "ca_caveat_count": 3, "do_not_count_as_new_case": true, "calibration_usable": false, "notes": "R13 source inventory row; used for cross-checkpoint only"}
{"row_type": "narrative_only", "narrative_id": "R13L86-SOURCE-R10", "round": "R13", "loop": 86, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION", "source_round": "R10", "source_file": "e2r_stock_web_v12_residual_round_R10_loop_86_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md", "source_large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "source_canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "source_fine_archetype_id": "LARGE_DEVELOPER_BUILDING_MATERIALS_MID_BUILDER_PF_DEBT_ORDERBOOK_CASHFLOW_MARGIN_BRIDGE_VS_VALUEUP_HOUSING_THEME_FADE", "trigger_count": 3, "positive_count": 1, "false_positive_count": 2, "source_proxy_trigger_count": 3, "ca_caveat_count": 3, "do_not_count_as_new_case": true, "calibration_usable": false, "notes": "R13 source inventory row; used for cross-checkpoint only"}
{"row_type": "narrative_only", "narrative_id": "R13L86-SOURCE-R11", "round": "R13", "loop": 86, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION", "source_round": "R11", "source_file": "e2r_stock_web_v12_residual_round_R11_loop_86_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md", "source_large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "source_canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "source_fine_archetype_id": "TENDER_OFFER_DELISTING_CONTROL_PREMIUM_ACCEPTANCE_THRESHOLD_CAP_VS_TENDER_CAP_LOW_MFE_FADE", "trigger_count": 3, "positive_count": 2, "false_positive_count": 1, "source_proxy_trigger_count": 3, "ca_caveat_count": 3, "do_not_count_as_new_case": true, "calibration_usable": false, "notes": "R13 source inventory row; used for cross-checkpoint only"}
{"row_type": "narrative_only", "narrative_id": "R13L86-SOURCE-R12", "round": "R13", "loop": 86, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION", "source_round": "R12", "source_file": "e2r_stock_web_v12_residual_round_R12_loop_86_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md", "source_large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "source_canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "source_fine_archetype_id": "AGRI_FOOD_GRAIN_INPUT_COST_SUPPLY_POLICY_MARGIN_BRIDGE_VS_FEED_GRAIN_THEME_SPIKE_FADE", "trigger_count": 3, "positive_count": 1, "false_positive_count": 2, "source_proxy_trigger_count": 3, "ca_caveat_count": 3, "do_not_count_as_new_case": true, "calibration_usable": false, "notes": "R13 source inventory row; used for cross-checkpoint only"}
{"row_type": "trigger", "trigger_id": "R13L86-PRICE-01-CA-WINDOW-USABLE-NOT-PROMOTION", "case_id": "R13L86-PRICE-01", "symbol": "R13_CROSS_ARCHETYPE", "company_name": "Cross-archetype loop86 price/accounting/source validation checkpoint", "round": "R13", "loop": 86, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION", "fine_archetype_id": "LOOP86_STOCK_WEB_PRICE_CA_SOURCE_PROXY_4B_4C_VALIDATION_CHECKPOINT", "loop_objective": "cross_archetype_price_validation|corporate_action_review|source_proxy_blocker|local_4B_hard_4C_protection|canonical_bridge_compression", "trigger_type": "R13_CROSS_PRICE_VALIDATION_REVIEW", "trigger_date": "2026-06-02", "entry_date": null, "entry_price": null, "evidence_available_at_that_date": "Stock-Web raw prices are useful for historical calibration only when the selected forward window is not contaminated by a corporate-action candidate.", "evidence_source": "derived_from_loop86_source_MDs; source_proxy_only_rows_not_promoted", "source_rounds": ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10", "R11", "R12"], "price_data_source": "Songdaiki/stock-web via source MDs", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": null, "MFE_90D_pct": 35.91, "MFE_180D_pct": null, "MAE_30D_pct": null, "MAE_90D_pct": -13.37, "MAE_180D_pct": null, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "stock_web_usable_with_CA_caveat_not_auto_promotion", "four_b_evidence_type": ["cross_checkpoint", "price_validation", "non_price_bridge_required"], "four_c_protection_label": "hard_4C_requires_non_price_thesis_break", "trigger_outcome_label": "use_clean_or_post_CA_windows_only", "current_profile_verdict": "stock_web_usable_with_CA_caveat_not_auto_promotion", "calibration_usable": true, "do_not_count_as_new_case": true, "dedupe_for_aggregate": true, "aggregate_group_role": "r13_cross_checkpoint", "is_new_independent_case": false, "reuse_reason": "R13 cross checkpoint; source cases already counted in R1~R12", "independent_evidence_weight": 0.0, "cross_scope": "corporate_action_window_validation", "residual_error": "raw_unadjusted_marcap requires CA-window caveat, even when 2024 trigger window is usable"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L86-PRICE-01", "trigger_id": "R13L86-PRICE-01-CA-WINDOW-USABLE-NOT-PROMOTION", "symbol": "R13_CROSS_ARCHETYPE", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION", "raw_component_scores_before": {"price_path_score": 60, "CA_caveat_score": 30, "source_quality_score": 45, "promotion_risk_score": 70}, "weighted_score_before": 62, "stage_label_before": "Potential calibration row", "raw_component_scores_after": {"price_path_score": 60, "CA_caveat_score": 85, "source_quality_score": 45, "promotion_risk_score": 35}, "weighted_score_after": 72, "stage_label_after": "Calibration usable only with CA-window caveat", "changed_components": ["price_path_score", "CA_caveat_score", "source_quality_score", "runtime_promotion_score", "bridge_confirmation_score", "local_4B_score", "hard_4C_score", "canonical_specificity_score", "duplicate_risk_score"], "component_delta_explanation": "Stock-Web raw prices are useful for historical calibration only when the selected forward window is not contaminated by a corporate-action candidate.", "MFE_90D_pct": 35.91, "MAE_90D_pct": -13.37, "score_return_alignment_label": "use_clean_or_post_CA_windows_only", "current_profile_verdict": "stock_web_usable_with_CA_caveat_not_auto_promotion", "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R13L86-PRICE-02-SOURCE-PROXY-BLOCKER", "case_id": "R13L86-PRICE-02", "symbol": "R13_CROSS_ARCHETYPE", "company_name": "Cross-archetype loop86 price/accounting/source validation checkpoint", "round": "R13", "loop": 86, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION", "fine_archetype_id": "LOOP86_STOCK_WEB_PRICE_CA_SOURCE_PROXY_4B_4C_VALIDATION_CHECKPOINT", "loop_objective": "cross_archetype_price_validation|corporate_action_review|source_proxy_blocker|local_4B_hard_4C_protection|canonical_bridge_compression", "trigger_type": "R13_CROSS_SOURCE_REPAIR_BLOCKER", "trigger_date": "2026-06-02", "entry_date": null, "entry_price": null, "evidence_available_at_that_date": "Price-path calibration cannot replace primary evidence timing, direct beneficiary mapping, contract detail, accounting quality or commercial bridge.", "evidence_source": "derived_from_loop86_source_MDs; source_proxy_only_rows_not_promoted", "source_rounds": ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10", "R11", "R12"], "price_data_source": "Songdaiki/stock-web via source MDs", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": null, "MFE_90D_pct": 57.07, "MFE_180D_pct": null, "MAE_30D_pct": null, "MAE_90D_pct": -6.41, "MAE_180D_pct": null, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "block_runtime_promotion_until_source_repair", "four_b_evidence_type": ["cross_checkpoint", "price_validation", "non_price_bridge_required"], "four_c_protection_label": "hard_4C_requires_non_price_thesis_break", "trigger_outcome_label": "hold_shadow_only_until_primary_evidence_repair", "current_profile_verdict": "block_runtime_promotion_until_source_repair", "calibration_usable": true, "do_not_count_as_new_case": true, "dedupe_for_aggregate": true, "aggregate_group_role": "r13_cross_checkpoint", "is_new_independent_case": false, "reuse_reason": "R13 cross checkpoint; source cases already counted in R1~R12", "independent_evidence_weight": 0.0, "cross_scope": "source_proxy_runtime_promotion_blocker", "residual_error": "loop86 rows repeatedly mark evidence_source=source_proxy_only/evidence_url_pending"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L86-PRICE-02", "trigger_id": "R13L86-PRICE-02-SOURCE-PROXY-BLOCKER", "symbol": "R13_CROSS_ARCHETYPE", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION", "raw_component_scores_before": {"price_alignment_score": 65, "source_quality_score": 20, "runtime_promotion_score": 50, "bridge_confirmation_score": 30}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable candidate", "raw_component_scores_after": {"price_alignment_score": 65, "source_quality_score": 5, "runtime_promotion_score": 0, "bridge_confirmation_score": 10}, "weighted_score_after": 48, "stage_label_after": "Hold: source-repair queue", "changed_components": ["price_path_score", "CA_caveat_score", "source_quality_score", "runtime_promotion_score", "bridge_confirmation_score", "local_4B_score", "hard_4C_score", "canonical_specificity_score", "duplicate_risk_score"], "component_delta_explanation": "Price-path calibration cannot replace primary evidence timing, direct beneficiary mapping, contract detail, accounting quality or commercial bridge.", "MFE_90D_pct": 57.07, "MAE_90D_pct": -6.41, "score_return_alignment_label": "hold_shadow_only_until_primary_evidence_repair", "current_profile_verdict": "block_runtime_promotion_until_source_repair", "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R13L86-PRICE-03-LOCAL-4B-YES-HARD-4C-NO", "case_id": "R13L86-PRICE-03", "symbol": "R13_CROSS_ARCHETYPE", "company_name": "Cross-archetype loop86 price/accounting/source validation checkpoint", "round": "R13", "loop": 86, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION", "fine_archetype_id": "LOOP86_STOCK_WEB_PRICE_CA_SOURCE_PROXY_4B_4C_VALIDATION_CHECKPOINT", "loop_objective": "cross_archetype_price_validation|corporate_action_review|source_proxy_blocker|local_4B_hard_4C_protection|canonical_bridge_compression", "trigger_type": "R13_CROSS_4B_4C_PROTECTION", "trigger_date": "2026-06-02", "entry_date": null, "entry_price": null, "evidence_available_at_that_date": "Local 4B is a warning after MFE outruns the evidence bridge; hard 4C needs a confirmed non-price thesis break.", "evidence_source": "derived_from_loop86_source_MDs; source_proxy_only_rows_not_promoted", "source_rounds": ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10", "R11", "R12"], "price_data_source": "Songdaiki/stock-web via source MDs", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": null, "MFE_90D_pct": 35.91, "MFE_180D_pct": null, "MAE_30D_pct": null, "MAE_90D_pct": -13.37, "MAE_180D_pct": null, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "local_4B_allowed_hard_4C_requires_non_price_break", "four_b_evidence_type": ["cross_checkpoint", "price_validation", "non_price_bridge_required"], "four_c_protection_label": "hard_4C_requires_non_price_thesis_break", "trigger_outcome_label": "allow_local_4B_watch_keep_hard_4C_non_price_only", "current_profile_verdict": "local_4B_allowed_hard_4C_requires_non_price_break", "calibration_usable": true, "do_not_count_as_new_case": true, "dedupe_for_aggregate": true, "aggregate_group_role": "r13_cross_checkpoint", "is_new_independent_case": false, "reuse_reason": "R13 cross checkpoint; source cases already counted in R1~R12", "independent_evidence_weight": 0.0, "cross_scope": "local_4B_vs_hard_4C_routing", "residual_error": "large post-peak drawdowns could be misrouted as hard 4C if price-only routing is allowed"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L86-PRICE-03", "trigger_id": "R13L86-PRICE-03-LOCAL-4B-YES-HARD-4C-NO", "symbol": "R13_CROSS_ARCHETYPE", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION", "raw_component_scores_before": {"post_peak_drawdown_score": 75, "non_price_break_score": 20, "local_4B_score": 45, "hard_4C_score": 65, "misroute_risk_score": 80}, "weighted_score_before": 64, "stage_label_before": "Possible full 4B / possible price-only 4C", "raw_component_scores_after": {"post_peak_drawdown_score": 75, "non_price_break_score": 20, "local_4B_score": 90, "hard_4C_score": 20, "misroute_risk_score": 30}, "weighted_score_after": 76, "stage_label_after": "Local 4B Watch; hard 4C blocked until non-price break", "changed_components": ["price_path_score", "CA_caveat_score", "source_quality_score", "runtime_promotion_score", "bridge_confirmation_score", "local_4B_score", "hard_4C_score", "canonical_specificity_score", "duplicate_risk_score"], "component_delta_explanation": "Local 4B is a warning after MFE outruns the evidence bridge; hard 4C needs a confirmed non-price thesis break.", "MFE_90D_pct": 35.91, "MAE_90D_pct": -13.37, "score_return_alignment_label": "allow_local_4B_watch_keep_hard_4C_non_price_only", "current_profile_verdict": "local_4B_allowed_hard_4C_requires_non_price_break", "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R13L86-PRICE-04-HIGH-MAE-GUARDRAIL", "case_id": "R13L86-PRICE-04", "symbol": "R13_CROSS_ARCHETYPE", "company_name": "Cross-archetype loop86 price/accounting/source validation checkpoint", "round": "R13", "loop": 86, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION", "fine_archetype_id": "LOOP86_STOCK_WEB_PRICE_CA_SOURCE_PROXY_4B_4C_VALIDATION_CHECKPOINT", "loop_objective": "cross_archetype_price_validation|corporate_action_review|source_proxy_blocker|local_4B_hard_4C_protection|canonical_bridge_compression", "trigger_type": "R13_CROSS_HIGH_MAE_PRICE_VALIDATION", "trigger_date": "2026-06-02", "entry_date": null, "entry_price": null, "evidence_available_at_that_date": "A path can be positive and still not be clean Green; high MAE forces bridge repair or local 4B watch.", "evidence_source": "derived_from_loop86_source_MDs; source_proxy_only_rows_not_promoted", "source_rounds": ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10", "R11", "R12"], "price_data_source": "Songdaiki/stock-web via source MDs", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": null, "MFE_90D_pct": 22.19, "MFE_180D_pct": null, "MAE_30D_pct": null, "MAE_90D_pct": -19.96, "MAE_180D_pct": null, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "high_MAE_blocks_clean_Green", "four_b_evidence_type": ["cross_checkpoint", "price_validation", "non_price_bridge_required"], "four_c_protection_label": "hard_4C_requires_non_price_thesis_break", "trigger_outcome_label": "block_clean_green_when_MAE_or_post_peak_drawdown_is_deep", "current_profile_verdict": "high_MAE_blocks_clean_Green", "calibration_usable": true, "do_not_count_as_new_case": true, "dedupe_for_aggregate": true, "aggregate_group_role": "r13_cross_checkpoint", "is_new_independent_case": false, "reuse_reason": "R13 cross checkpoint; source cases already counted in R1~R12", "independent_evidence_weight": 0.0, "cross_scope": "high_MAE_guardrail_review", "residual_error": "loop86 contains positives with MFE but also substantial MAE/post-peak drawdown"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L86-PRICE-04", "trigger_id": "R13L86-PRICE-04-HIGH-MAE-GUARDRAIL", "symbol": "R13_CROSS_ARCHETYPE", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION", "raw_component_scores_before": {"MFE_score": 70, "MAE_control_score": 35, "bridge_confirmation_score": 35, "green_readiness_score": 60}, "weighted_score_before": 72, "stage_label_before": "Stage2-Actionable / possible Green", "raw_component_scores_after": {"MFE_score": 70, "MAE_control_score": 20, "bridge_confirmation_score": 25, "green_readiness_score": 20, "riskwatch_score": 85}, "weighted_score_after": 68, "stage_label_after": "Stage2-Actionable + high-MAE/local-4B watch", "changed_components": ["price_path_score", "CA_caveat_score", "source_quality_score", "runtime_promotion_score", "bridge_confirmation_score", "local_4B_score", "hard_4C_score", "canonical_specificity_score", "duplicate_risk_score"], "component_delta_explanation": "A path can be positive and still not be clean Green; high MAE forces bridge repair or local 4B watch.", "MFE_90D_pct": 22.19, "MAE_90D_pct": -19.96, "score_return_alignment_label": "block_clean_green_when_MAE_or_post_peak_drawdown_is_deep", "current_profile_verdict": "high_MAE_blocks_clean_Green", "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R13L86-PRICE-05-CANONICAL-BRIDGE-FAMILY", "case_id": "R13L86-PRICE-05", "symbol": "R13_CROSS_ARCHETYPE", "company_name": "Cross-archetype loop86 price/accounting/source validation checkpoint", "round": "R13", "loop": 86, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION", "fine_archetype_id": "LOOP86_STOCK_WEB_PRICE_CA_SOURCE_PROXY_4B_4C_VALIDATION_CHECKPOINT", "loop_objective": "cross_archetype_price_validation|corporate_action_review|source_proxy_blocker|local_4B_hard_4C_protection|canonical_bridge_compression", "trigger_type": "R13_CROSS_CANONICAL_COMPRESSION", "trigger_date": "2026-06-02", "entry_date": null, "entry_price": null, "evidence_available_at_that_date": "A global rule would flatten very different machines; the proper repair is canonical grammar plus source repair.", "evidence_source": "derived_from_loop86_source_MDs; source_proxy_only_rows_not_promoted", "source_rounds": ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10", "R11", "R12"], "price_data_source": "Songdaiki/stock-web via source MDs", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": null, "MFE_90D_pct": 35.91, "MFE_180D_pct": null, "MAE_30D_pct": null, "MAE_90D_pct": -13.37, "MAE_180D_pct": null, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "do_not_apply_new_global_weight", "four_b_evidence_type": ["cross_checkpoint", "price_validation", "non_price_bridge_required"], "four_c_protection_label": "hard_4C_requires_non_price_thesis_break", "trigger_outcome_label": "keep_bridge_rules_canonical_specific_not_global_weight", "current_profile_verdict": "do_not_apply_new_global_weight", "calibration_usable": true, "do_not_count_as_new_case": true, "dedupe_for_aggregate": true, "aggregate_group_role": "r13_cross_checkpoint", "is_new_independent_case": false, "reuse_reason": "R13 cross checkpoint; source cases already counted in R1~R12", "independent_evidence_weight": 0.0, "cross_scope": "canonical_specific_bridge_family_compression", "residual_error": "same source/bridge gap recurs but each canonical uses different non-price proof"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L86-PRICE-05", "trigger_id": "R13L86-PRICE-05-CANONICAL-BRIDGE-FAMILY", "symbol": "R13_CROSS_ARCHETYPE", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION", "raw_component_scores_before": {"global_rule_simplicity_score": 70, "canonical_specificity_score": 35, "overfit_risk_score": 75, "source_repair_need_score": 80}, "weighted_score_before": 60, "stage_label_before": "Possible new global rule", "raw_component_scores_after": {"global_rule_simplicity_score": 30, "canonical_specificity_score": 90, "overfit_risk_score": 35, "source_repair_need_score": 80}, "weighted_score_after": 74, "stage_label_after": "Canonical-specific shadow family only", "changed_components": ["price_path_score", "CA_caveat_score", "source_quality_score", "runtime_promotion_score", "bridge_confirmation_score", "local_4B_score", "hard_4C_score", "canonical_specificity_score", "duplicate_risk_score"], "component_delta_explanation": "A global rule would flatten very different machines; the proper repair is canonical grammar plus source repair.", "MFE_90D_pct": 35.91, "MAE_90D_pct": -13.37, "score_return_alignment_label": "keep_bridge_rules_canonical_specific_not_global_weight", "current_profile_verdict": "do_not_apply_new_global_weight", "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R13L86-PRICE-06-DEDUPE-INDEPENDENCE", "case_id": "R13L86-PRICE-06", "symbol": "R13_CROSS_ARCHETYPE", "company_name": "Cross-archetype loop86 price/accounting/source validation checkpoint", "round": "R13", "loop": 86, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION", "fine_archetype_id": "LOOP86_STOCK_WEB_PRICE_CA_SOURCE_PROXY_4B_4C_VALIDATION_CHECKPOINT", "loop_objective": "cross_archetype_price_validation|corporate_action_review|source_proxy_blocker|local_4B_hard_4C_protection|canonical_bridge_compression", "trigger_type": "R13_CROSS_DEDUPE_REVIEW", "trigger_date": "2026-06-02", "entry_date": null, "entry_price": null, "evidence_available_at_that_date": "R13 is a checkpoint ledger, not a new sector discovery; source triggers remain counted only in R1~R12.", "evidence_source": "derived_from_loop86_source_MDs; source_proxy_only_rows_not_promoted", "source_rounds": ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10", "R11", "R12"], "price_data_source": "Songdaiki/stock-web via source MDs", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": null, "MFE_90D_pct": null, "MFE_180D_pct": null, "MAE_30D_pct": null, "MAE_90D_pct": null, "MAE_180D_pct": null, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "R13_cross_checkpoint_only", "four_b_evidence_type": ["cross_checkpoint", "price_validation", "non_price_bridge_required"], "four_c_protection_label": "hard_4C_requires_non_price_thesis_break", "trigger_outcome_label": "do_not_count_R13_as_new_case", "current_profile_verdict": "R13_cross_checkpoint_only", "calibration_usable": true, "do_not_count_as_new_case": true, "dedupe_for_aggregate": true, "aggregate_group_role": "r13_cross_checkpoint", "is_new_independent_case": false, "reuse_reason": "R13 cross checkpoint; source cases already counted in R1~R12", "independent_evidence_weight": 0.0, "cross_scope": "dedupe_and_independent_evidence_review", "residual_error": "R13 aggregates source cases and must not inflate corpus counts"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L86-PRICE-06", "trigger_id": "R13L86-PRICE-06-DEDUPE-INDEPENDENCE", "symbol": "R13_CROSS_ARCHETYPE", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION", "raw_component_scores_before": {"aggregate_counting_score": 30, "duplicate_risk_score": 90, "independence_score": 20}, "weighted_score_before": 50, "stage_label_before": "Could double-count source MDs", "raw_component_scores_after": {"aggregate_counting_score": 90, "duplicate_risk_score": 10, "independence_score": 90}, "weighted_score_after": 80, "stage_label_after": "do_not_count_as_new_case=true; independent_evidence_weight=0.0", "changed_components": ["price_path_score", "CA_caveat_score", "source_quality_score", "runtime_promotion_score", "bridge_confirmation_score", "local_4B_score", "hard_4C_score", "canonical_specificity_score", "duplicate_risk_score"], "component_delta_explanation": "R13 is a checkpoint ledger, not a new sector discovery; source triggers remain counted only in R1~R12.", "MFE_90D_pct": null, "MAE_90D_pct": null, "score_return_alignment_label": "do_not_count_R13_as_new_case", "current_profile_verdict": "R13_cross_checkpoint_only", "do_not_count_as_new_case": true}
{"row_type": "shadow_weight", "axis": "R13_loop86_price_CA_source_proxy_local4B_hard4C_validation_checkpoint", "scope": "cross_archetype_checkpoint_only", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Loop86 R1~R12 rows repeatedly show Stock-Web price rows are usable for calibration with CA-window caveats, source_proxy_only must block runtime promotion, local 4B should be allowed after MFE, and hard 4C requires non-price thesis break.", "backtest_effect": "no production weight; reinforces price validation, source repair, high-MAE and 4B/4C guardrails", "trigger_ids": "R13L86-PRICE-01-CA-WINDOW-USABLE-NOT-PROMOTION|R13L86-PRICE-02-SOURCE-PROXY-BLOCKER|R13L86-PRICE-03-LOCAL-4B-YES-HARD-4C-NO|R13L86-PRICE-04-HIGH-MAE-GUARDRAIL|R13L86-PRICE-05-CANONICAL-BRIDGE-FAMILY|R13L86-PRICE-06-DEDUPE-INDEPENDENCE", "calibration_usable_count": 6, "new_independent_case_count": 0, "counterexample_count": 0, "confidence": "medium", "proposal_type": "r13_cross_checkpoint_shadow_only", "notes": "do_not_count_as_new_case=true; source repair required; not production"}
{"row_type": "residual_contribution", "round": "R13", "loop": 86, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION", "new_independent_case_count": 0, "reused_case_count": 12, "new_symbol_count": 0, "new_trigger_family_count": 0, "source_trigger_count": 36, "source_false_positive_trigger_count": 19, "source_positive_trigger_count": 17, "source_proxy_trigger_count": 36, "corporate_action_caveat_trigger_count": 36, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "source_proxy_only_blocks_runtime_promotion", "high_MAE_guardrail", "local_4B_watch_before_full_4B_when_MFE_outruns_bridge"], "residual_error_types_found": ["raw_unadjusted_stock_web_CA_window_caveat_required", "source_proxy_runtime_promotion_risk", "local_4B_vs_hard_4C_misroute_risk", "high_MAE_blocks_clean_Green", "canonical_bridge_family_required_not_global_weight", "R13_double_counting_risk"], "loop_contribution_label": "cross_archetype_accounting_trust_price_validation", "do_not_propose_new_weight_delta": true, "do_not_count_as_new_case": true}
```

## 23. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

This R13 file is not live candidate research and is not a new sector-positive source. It is a cross-archetype price / accounting-trust / source-proxy / 4B-4C validation review over loop86 R1~R12 source MDs.

### Rules

- Treat every R13 `trigger` row as `do_not_count_as_new_case=true`.
- Do not add R13 rows to new independent case counts.
- Do not infer new runtime weights from R13 alone.
- Use R13 rows to validate guardrails:
  - Stock-Web raw/unadjusted prices are usable only with CA-window hygiene
  - source_proxy_only/evidence_url_pending blocks runtime promotion
  - local 4B watch can exist before full 4B
  - hard 4C requires non-price thesis break
  - high MAE blocks clean Green
  - canonical bridge rules should remain sector/canonical-specific
- Keep production scoring unchanged unless a later batch validates primary evidence and aggregate thresholds.

## 24. Next Round State

```text
completed_round = R13
completed_loop = 86
next_round = R1
next_loop = 87
round_schedule_status = valid
round_sector_consistency = pass
```

## 25. Source Notes

```text
MAIN_EXECUTION_PROMPT = docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
NO_REPEAT_INDEX = docs/core/V12_Research_No_Repeat_Index.md
price_source = Songdaiki/stock-web
```
