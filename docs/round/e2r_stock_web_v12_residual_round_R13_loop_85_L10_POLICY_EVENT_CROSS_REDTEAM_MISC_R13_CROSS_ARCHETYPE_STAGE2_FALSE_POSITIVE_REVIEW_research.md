# E2R Stock-Web v12 Residual Research — R13 Loop 85 / L10 / Stage2 False-Positive Review

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohl_breakthrough_v12",
  "scheduled_round": "R13",
  "scheduled_loop": 85,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R13",
  "completed_loop": 85,
  "computed_next_round": "R1",
  "computed_next_loop": 86,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW",
  "fine_archetype_id": "LOOP85_FALSE_POSITIVE_THEME_MFE_HIGH_MAE_SOURCE_PROXY_BRIDGE_GAP_REVIEW",
  "loop_objective": [
    "cross_archetype_stage2_false_positive_review",
    "theme_headline_MFE_vs_economics_bridge_split",
    "high_MAE_false_positive_guardrail",
    "low_MFE_value_trap_guardrail",
    "source_proxy_runtime_promotion_blocker_review",
    "local_4B_timing_review",
    "hard_4C_non_price_thesis_break_protection",
    "canonical_bridge_family_compression",
    "do_not_count_as_new_sector_case",
    "do_not_propose_new_weight_delta"
  ],
  "source_round_span": "R1~R12 loop 85",
  "source_md_count": 12,
  "source_trigger_count": 36,
  "source_false_positive_trigger_count": 21,
  "source_positive_trigger_count": 15,
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
scheduled_loop = 85
allowed_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC only
selected_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
selected_canonical_archetype_id = R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
computed_next_round = R1
computed_next_loop = 86
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

This file deliberately avoids creating a new C20/C21/C23/C26/C31 sector row under R13. Every machine-readable R13 `trigger` row is a cross-checkpoint with `independent_evidence_weight = 0.0`.

## 4. Stock-Web Price Source Context

```text
price_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
```

R13 does not compute a fresh OHLC entry window. It inherits the Stock-Web validations and trigger-level MFE/MAE calculations from R1~R12 loop85 source MDs.

## 5. Source MD Inventory — Loop 85

| round | large_sector_id | source canonical | positives | false positives | fine route |
|---|---|---|---:|---:|---|
| R1 | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 2 | 1 | INDUSTRIAL_FITTINGS_OFFSHORE_ORDER_BACKLOG_DELIVERY_MARGIN_BRIDGE_VS_ORDER_THEME_HIGH_MAE_FADE |
| R2 | L2_AI_SEMICONDUCTOR_ELECTRONICS | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 1 | 2 | HBM_TEST_HANDLER_PROBE_CARD_OSAT_CUSTOMER_QUALITY_REVENUE_BRIDGE_VS_TEST_THEME_BLOWOFF_FADE |
| R3 | L3_BATTERY_EV_GREEN_MOBILITY | C14_EV_DEMAND_SLOWDOWN_4B_4C | 0 | 3 | CNT_ELECTROLYTE_COPPERFOIL_EV_DEMAND_SLOWDOWN_INVENTORY_MARGIN_BRIDGE_BREAK_VS_REBOUND_THEME_FADE |
| R4 | L4_MATERIALS_SPREAD_RESOURCE | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 0 | 3 | SPECIALTY_CHEMICAL_SULFUR_NITRIC_ACID_PRODUCT_SPREAD_INVENTORY_MARGIN_BRIDGE_VS_CHEMICAL_REBOUND_THEME_FADE |
| R5 | L5_CONSUMER_BRAND_DISTRIBUTION | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 2 | 1 | K_FOOD_DAIRY_PLANT_BASED_BAKERY_GLOBAL_DISTRIBUTION_SELL_THROUGH_MARGIN_BRIDGE_VS_FOOD_THEME_FADE |
| R6 | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 2 | 1 | BROKERAGE_ROE_TRADING_VOLUME_DIVIDEND_CAPITAL_RETURN_BRIDGE_VS_VALUEUP_BETA_LOW_MFE_FADE |
| R7 | L7_BIO_HEALTHCARE_MEDICAL | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 1 | 2 | PHARMA_LICENSING_REGULATORY_COMMERCIALIZATION_REVENUE_MARGIN_BRIDGE_VS_PIPELINE_EVENT_FADE |
| R8 | L8_PLATFORM_CONTENT_SW_SECURITY | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 1 | 2 | AD_TECH_AGENCY_REWARD_PLATFORM_TRAFFIC_MONETIZATION_TAKE_RATE_OPERATING_LEVERAGE_BRIDGE_VS_AI_AD_THEME_FADE |
| R9 | L3_BATTERY_EV_GREEN_MOBILITY | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 2 | 1 | AUTO_LIGHTING_ADAS_CHASSIS_PARTS_VOLUME_MIX_COST_SPREAD_MARGIN_BRIDGE_VS_AUTO_PARTS_BETA_FADE |
| R10 | L9_CONSTRUCTION_REALESTATE_HOUSING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 2 | 1 | SMALL_MID_BUILDER_PF_THEME_ORDERBOOK_MARGIN_BRIDGE_VS_HOUSING_SQUEEZE_FADE |
| R11 | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 1 | 2 | EAST_SEA_GAS_EXPLORATION_POLICY_EVENT_RESOURCE_OPTIONALITY_VS_THEME_SPIKE_FADE |
| R12 | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 1 | 2 | EDUCATION_POLICY_MEDICAL_SCHOOL_QUOTA_PRIVATE_EDU_DEMAND_REVENUE_BRIDGE_VS_THEME_SPIKE_FADE |

## 6. Aggregate Trigger Statistics

```json
{
  "source_md_count": 12,
  "source_trigger_count": 36,
  "source_case_count": 36,
  "positive_trigger_count": 15,
  "false_positive_trigger_count": 21,
  "fp_avg_MFE30": 12.42,
  "fp_avg_MFE90": 13.96,
  "fp_avg_MFE180": 14.52,
  "fp_avg_MAE30": -11.78,
  "fp_avg_MAE90": -22.37,
  "fp_avg_MAE180": -35.43,
  "pos_avg_MFE30": 39.13,
  "pos_avg_MFE90": 59.96,
  "pos_avg_MFE180": 73.29,
  "pos_avg_MAE30": -5.18,
  "pos_avg_MAE90": -6.41,
  "pos_avg_MAE180": -9.67
}
```

Loop85 produced 36 source triggers. The core R13 observation is that false positives were not random. They had a repeatable shape:

```text
headline/theme MFE
+ missing canonical economics bridge
+ source_proxy_only evidence
+ high MAE or post-peak drawdown
= Stage2 rejected or RiskWatch, not clean Stage2/Green
```

## 7. Worst False-Positive / High-MAE Rows

| source round | symbol | company | canonical | MFE90 | MAE90 | MAE180 | outcome |
|---|---:|---|---|---:|---:|---:|---|
| R2 | 330860 | 네패스아크 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 25.75 | -42.68 | -67.48 | short_MFE_deep_MAE_test_theme_false_positive |
| R8 | 236810 | 엔비티 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 23.62 | -27.26 | -56.48 | traffic_monetization_theme_MFE_then_deep_MAE_false_positive |
| R4 | 005950 | 이수화학 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 10.91 | -30.96 | -49.82 | theme_spike_high_MAE_chemical_margin_false_positive |
| R3 | 121600 | 나노신소재 | C14_EV_DEMAND_SLOWDOWN_4B_4C | 17.76 | -17.09 | -48.88 | initial_MFE_then_EV_demand_slowdown_high_MAE_4B_watch |
| R3 | 278280 | 천보 | C14_EV_DEMAND_SLOWDOWN_4B_4C | 5.05 | -23.79 | -48.42 | small_MFE_then_large_MAE_EV_slowdown_false_positive |
| R12 | 053290 | NE능률 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 20.23 | -25.67 | -47.61 | policy_theme_spike_MFE_then_deep_MAE_false_positive |
| R12 | 133750 | 메가엠디 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 22.54 | -45.01 | -45.01 | admissions_policy_theme_MFE_then_deep_MAE_false_positive |
| R8 | 216050 | 인크로스 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 4.12 | -29.55 | -44.01 | low_MFE_high_MAE_ad_revenue_rebound_false_positive |
| R4 | 014680 | 한솔케미칼 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 7.0 | -13.45 | -41.9 | small_MFE_then_large_MAE_chemical_rebound_false_positive |
| R9 | 010690 | 화신 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 25.02 | -16.21 | -38.08 | MFE_then_deep_MAE_auto_parts_beta_false_positive |

## 8. Cross-Archetype Checkpoint Rows

| cross_case_id | cross_scope | source rounds | decision | verdict |
|---|---|---|---|---|
| R13L85-S2FP-01 | theme_headline_MFE_not_stage2_without_bridge | R1, R2, R3, R4, R5, R7, R8, R9, R10, R11, R12 | demote_theme_only_stage2 | theme_only_MFE_not_stage2_actionable |
| R13L85-S2FP-02 | high_MAE_false_positive_rejection | R2, R3, R4, R8, R12 | reject_or_riskwatch_high_MAE_false_positive | high_MAE_false_positive_blocks_stage2_validation |
| R13L85-S2FP-03 | low_MFE_false_positive_value_trap_review | R3, R4, R8, R10 | reject_low_MFE_stage2_watch | low_MFE_without_bridge_rejected |
| R13L85-S2FP-04 | source_proxy_evidence_url_pending_runtime_blocker | R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12 | hold_shadow_only_do_not_promote | block_runtime_promotion_until_source_repair |
| R13L85-S2FP-05 | local_4B_watch_before_full_4B_or_hard_4C | R2, R5, R8, R10, R11, R12 | allow_local_4B_keep_hard_4C_non_price_only | local_4B_yes_hard_4C_no_without_non_price_break |
| R13L85-S2FP-06 | canonical_specific_bridge_family_compression | R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12 | keep_bridge_rules_canonical_specific_not_global_weight | do_not_apply_new_global_weight |

## 9. R13 Finding 1 — Theme MFE Is Not Stage2 Without a Bridge

Across loop85, false positives averaged:

```text
false_positive_avg_MFE90 = 13.96%
false_positive_avg_MAE90 = -22.37%
false_positive_avg_MAE180 = -35.43%
```

The problem is not that false positives never move. Many of them move first and fail later. The repeated error is treating a theme candle as if it already proved the business bridge.

## 10. R13 Finding 2 — High-MAE False Positives Need Hard Demotion

The worst rows shared a repeated contour:

```text
short or medium MFE
→ bridge evidence absent
→ MAE widens
→ post-peak drawdown validates false-positive route
```

Representative rows:

```text
330860 / C08 / OSAT test capacity theme
236810 / C26 / reward-ad traffic monetization theme
005950 / C17 / sulfur-specialty chemical theme
121600 / C14 / battery-material rebound theme
053290 and 133750 / C31 / education-policy theme
```

These should not be rescued by “the price did move.” The move was the trapdoor.

## 11. R13 Finding 3 — Low-MFE Rows Are Often Cleaner Rejections

Some rows did not even produce enough MFE to justify Stage2 watch:

```text
low_MFE_false_positive_count = 9
low_MFE_false_positive_avg_MFE90 = 5.21%
low_MFE_false_positive_avg_MAE90 = -16.75%
```

Low-MFE plus missing bridge is not “early.” It is usually a false-positive value trap or weak rebound.

## 12. R13 Finding 4 — Source Proxy Blocks Runtime Promotion

Every loop85 sector MD still carries `source_proxy_only / evidence_url_pending` on selected evidence.

```text
source_proxy_only = calibration ledger allowed
source_proxy_only != runtime scoring promotion
evidence_url_pending = source-repair queue
```

Price can show that a trigger was worth studying. It cannot prove the original publication time, source quality, direct beneficiary mapping, order quality, or economics bridge.

## 13. R13 Finding 5 — Local 4B Watch Is Earlier Than Full 4B

The loop85 cases often peaked before the source bridge could be repaired. Full 4B still needs non-price deterioration, but local 4B watch is appropriate when price outruns the evidence bridge.

```text
local_4B_watch = allowed when MFE outruns evidence bridge
full_4B = still requires non-price evidence
hard_4C = never price-only
```

## 14. R13 Finding 6 — Canonical Bridge Family, Not Global Weight

The failure is shared, but the repair is not one global blunt rule.

```text
C01 = backlog quality + delivery + ASP/cost pass-through + margin
C08 = named customer + order/acceptance + delivery/utilization + margin
C14 = EV demand + call-off + inventory + utilization + margin
C17 = product spread + inventory + ASP pass-through + utilization + margin
C20 = sell-through + reorder + capacity + ASP/mix + margin
C21 = ROE quality + payout + capital buffer + revenue mix
C23 = approval/launch + partner + milestone/reimbursement + sales + margin
C26 = traffic quality + advertiser retention + ad revenue + take-rate + operating leverage
C29 = volume + platform/order mix + utilization + ASP/cost spread + margin
C30 = PF refinancing + debt/liquidity + orderbook + cash-flow + project margin
C31 resource = beneficiary + license/working-interest + reserve + capex + economics
C31 education = beneficiary + leads + enrollment + ARPU/capacity + margin
```

A global penalty would act like one wrench on twelve machines. The correct repair is a family of canonical-specific bridge checks.

## 15. Stage2 / Yellow / Green / 4B / 4C Cross Comparison

| gate | loop85 cross result | R13 decision |
|---|---|---|
| Stage2-Actionable | allowed when bridge-positive, but source repair still pending | keep as shadow only |
| Stage2-Watch / FalsePositive | frequent when headline MFE lacks bridge | demote or RiskWatch |
| Stage3-Yellow | useful only when partial bridge exists | keep |
| Stage3-Green | unsafe under high-MAE or source-proxy conditions | block |
| Local 4B Watch | needed when MFE outruns bridge | allow |
| Full 4B | still needs non-price deterioration evidence | keep requirement |
| Hard 4C | price drawdown alone is insufficient | keep non-price thesis-break requirement |

## 16. Before / After Cross-Checkpoint Comparison

| checkpoint profile | new independent cases | false-positive handling | high-MAE handling | source handling | 4B/4C routing | production impact |
|---|---:|---|---|---|---|---|
| P0 current calibrated proxy | 0 | theme-only may still tempt Stage2 | inconsistent without bridge gate | source proxy may tempt promotion | full 4B/4C can be late/misrouted | none |
| P1 R13 Stage2 FP checkpoint | 0 | theme-only demoted | high-MAE blocks Stage2 validation | source repair mandatory | local 4B allowed, hard 4C non-price only | none |

## 17. Score-Return Alignment Matrix

| cross_case_id | weighted before | label before | weighted after | label after | alignment |
|---|---:|---|---:|---|---|
| R13L85-S2FP-01 | 58 | Stage2-Watch/FalsePositive | 44 | Rejected-Stage2 / RiskWatch | improved |
| R13L85-S2FP-02 | 60 | Stage2-Watch/FalsePositive | 43 | Rejected-Stage2 / High-MAE RiskWatch | improved |
| R13L85-S2FP-03 | 56 | Stage2-Watch/FalsePositive | 42 | Rejected-Stage2 / Low-MFE RiskWatch | improved |
| R13L85-S2FP-04 | 63 | Stage2-Actionable candidate | 48 | Hold: source-repair queue | improved |
| R13L85-S2FP-05 | 64 | possible full 4B / possible hard 4C | 72 | Local 4B Watch; hard 4C blocked until non-price break | improved |
| R13L85-S2FP-06 | 58 | possible new global rule | 74 | canonical-specific shadow family only | improved |

## 18. Coverage Matrix

| large_sector_id | canonical_archetype_id | positive | counterexample | 4B | 4C | new cases | reused source MDs | usable cross triggers | current errors | sector rule | canonical rule | coverage gap after |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | 0 | 0 | 1-watch family | 1-watch family | 0 | 12 | 6 | 6 | no | cross checkpoint only | source repair / threshold audit |

## 19. Residual Contribution Summary

```text
new_independent_case_count: 0
reused_case_count: 12
reused_case_ids: R1~R12 loop85 source MDs
new_symbol_count: 0
new_canonical_archetype_count: 0
new_fine_archetype_count: 0
new_trigger_family_count: 0
source_trigger_count: 36
source_positive_trigger_count: 15
source_false_positive_trigger_count: 21
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
  - source_proxy_only_blocks_runtime_promotion
  - high_MAE_guardrail
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
residual_error_types_found:
  - theme_headline_MFE_not_stage2_without_bridge
  - high_MAE_false_positive_rejection
  - low_MFE_value_trap_rejection
  - source_proxy_runtime_promotion_risk
  - local_4B_late_when_MFE_outruns_bridge
  - price_only_hard_4C_misroute_risk
  - global_weight_overfit_risk
new_axis_proposed: false
existing_axis_strengthened:
  - source_proxy_only_blocks_runtime_promotion
  - high_MAE_blocks_clean_Green
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
  - hard_4C_requires_non_price_thesis_break
existing_axis_weakened: null
existing_axis_kept:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: null
canonical_archetype_rule_candidate: R13_cross_checkpoint_only
no_new_signal_reason: R13 is cross-archetype checkpoint, not sector research
loop_contribution_label: cross_archetype_stage2_false_positive_review
do_not_propose_new_weight_delta: true
do_not_count_as_new_case: true
```

## 20. Validation Scope / Non-Validation Scope

Validated in this MD:

```text
- R13 scheduled round/loop consistency
- R13 large_sector_id hard gate
- R13 canonical scope
- source MD inventory for loop85 R1~R12
- aggregate source trigger counts
- false-positive MFE/MAE aggregation
- do_not_count_as_new_case policy
- source-proxy runtime blocker principle
- local-vs-full 4B distinction
- hard 4C non-price thesis-break principle
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
shadow_weight,R13_loop85_stage2_false_positive_bridge_source_repair_local_4B_guardrail,cross_archetype_checkpoint_only,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW,0,1,+1,"Loop85 R1~R12 cases repeatedly show Stage2 false positives arise from theme MFE without canonical economics bridge; source-proxy rows must not promote; local 4B can precede full 4B; hard 4C requires non-price thesis break","no production weight; reinforces existing false-positive and bridge guardrails","R13L85-S2FP-01-THEME-MFE-DEMOTION|R13L85-S2FP-02-HIGH-MAE-REJECTION|R13L85-S2FP-03-LOW-MFE-VALUE-TRAP|R13L85-S2FP-04-SOURCE-PROXY-BLOCKER|R13L85-S2FP-05-LOCAL-4B-NOT-FULL-4C|R13L85-S2FP-06-CANONICAL-BRIDGE-FAMILY",6,0,0,medium,r13_cross_checkpoint_shadow_only,"do_not_count_as_new_case=true; source repair required; not production"
```

## 22. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "cross_checkpoint_uses_source_MD_price_validations"}
{"row_type": "narrative_only", "narrative_id": "R13L85-SOURCE-R1", "round": "R13", "loop": 85, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW", "source_round": "R1", "source_file": "e2r_stock_web_v12_residual_round_R1_loop_85_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md", "source_large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "source_canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "source_fine_archetype_id": "INDUSTRIAL_FITTINGS_OFFSHORE_ORDER_BACKLOG_DELIVERY_MARGIN_BRIDGE_VS_ORDER_THEME_HIGH_MAE_FADE", "trigger_count": 3, "positive_count": 2, "false_positive_count": 1, "do_not_count_as_new_case": true, "calibration_usable": false, "notes": "R13 source inventory row; used for cross-checkpoint only"}
{"row_type": "narrative_only", "narrative_id": "R13L85-SOURCE-R2", "round": "R13", "loop": 85, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW", "source_round": "R2", "source_file": "e2r_stock_web_v12_residual_round_R2_loop_85_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md", "source_large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "source_canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "source_fine_archetype_id": "HBM_TEST_HANDLER_PROBE_CARD_OSAT_CUSTOMER_QUALITY_REVENUE_BRIDGE_VS_TEST_THEME_BLOWOFF_FADE", "trigger_count": 3, "positive_count": 1, "false_positive_count": 2, "do_not_count_as_new_case": true, "calibration_usable": false, "notes": "R13 source inventory row; used for cross-checkpoint only"}
{"row_type": "narrative_only", "narrative_id": "R13L85-SOURCE-R3", "round": "R13", "loop": 85, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW", "source_round": "R3", "source_file": "e2r_stock_web_v12_residual_round_R3_loop_85_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md", "source_large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "source_canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "source_fine_archetype_id": "CNT_ELECTROLYTE_COPPERFOIL_EV_DEMAND_SLOWDOWN_INVENTORY_MARGIN_BRIDGE_BREAK_VS_REBOUND_THEME_FADE", "trigger_count": 3, "positive_count": 0, "false_positive_count": 3, "do_not_count_as_new_case": true, "calibration_usable": false, "notes": "R13 source inventory row; used for cross-checkpoint only"}
{"row_type": "narrative_only", "narrative_id": "R13L85-SOURCE-R4", "round": "R13", "loop": 85, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW", "source_round": "R4", "source_file": "e2r_stock_web_v12_residual_round_R4_loop_85_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md", "source_large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "source_canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "source_fine_archetype_id": "SPECIALTY_CHEMICAL_SULFUR_NITRIC_ACID_PRODUCT_SPREAD_INVENTORY_MARGIN_BRIDGE_VS_CHEMICAL_REBOUND_THEME_FADE", "trigger_count": 3, "positive_count": 0, "false_positive_count": 3, "do_not_count_as_new_case": true, "calibration_usable": false, "notes": "R13 source inventory row; used for cross-checkpoint only"}
{"row_type": "narrative_only", "narrative_id": "R13L85-SOURCE-R5", "round": "R13", "loop": 85, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW", "source_round": "R5", "source_file": "e2r_stock_web_v12_residual_round_R5_loop_85_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md", "source_large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "source_canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "source_fine_archetype_id": "K_FOOD_DAIRY_PLANT_BASED_BAKERY_GLOBAL_DISTRIBUTION_SELL_THROUGH_MARGIN_BRIDGE_VS_FOOD_THEME_FADE", "trigger_count": 3, "positive_count": 2, "false_positive_count": 1, "do_not_count_as_new_case": true, "calibration_usable": false, "notes": "R13 source inventory row; used for cross-checkpoint only"}
{"row_type": "narrative_only", "narrative_id": "R13L85-SOURCE-R6", "round": "R13", "loop": 85, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW", "source_round": "R6", "source_file": "e2r_stock_web_v12_residual_round_R6_loop_85_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md", "source_large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "source_canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "source_fine_archetype_id": "BROKERAGE_ROE_TRADING_VOLUME_DIVIDEND_CAPITAL_RETURN_BRIDGE_VS_VALUEUP_BETA_LOW_MFE_FADE", "trigger_count": 3, "positive_count": 2, "false_positive_count": 1, "do_not_count_as_new_case": true, "calibration_usable": false, "notes": "R13 source inventory row; used for cross-checkpoint only"}
{"row_type": "narrative_only", "narrative_id": "R13L85-SOURCE-R7", "round": "R13", "loop": 85, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW", "source_round": "R7", "source_file": "e2r_stock_web_v12_residual_round_R7_loop_85_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md", "source_large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "source_canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "source_fine_archetype_id": "PHARMA_LICENSING_REGULATORY_COMMERCIALIZATION_REVENUE_MARGIN_BRIDGE_VS_PIPELINE_EVENT_FADE", "trigger_count": 3, "positive_count": 1, "false_positive_count": 2, "do_not_count_as_new_case": true, "calibration_usable": false, "notes": "R13 source inventory row; used for cross-checkpoint only"}
{"row_type": "narrative_only", "narrative_id": "R13L85-SOURCE-R8", "round": "R13", "loop": 85, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW", "source_round": "R8", "source_file": "e2r_stock_web_v12_residual_round_R8_loop_85_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md", "source_large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "source_canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "source_fine_archetype_id": "AD_TECH_AGENCY_REWARD_PLATFORM_TRAFFIC_MONETIZATION_TAKE_RATE_OPERATING_LEVERAGE_BRIDGE_VS_AI_AD_THEME_FADE", "trigger_count": 3, "positive_count": 1, "false_positive_count": 2, "do_not_count_as_new_case": true, "calibration_usable": false, "notes": "R13 source inventory row; used for cross-checkpoint only"}
{"row_type": "narrative_only", "narrative_id": "R13L85-SOURCE-R9", "round": "R13", "loop": 85, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW", "source_round": "R9", "source_file": "e2r_stock_web_v12_residual_round_R9_loop_85_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md", "source_large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "source_canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "source_fine_archetype_id": "AUTO_LIGHTING_ADAS_CHASSIS_PARTS_VOLUME_MIX_COST_SPREAD_MARGIN_BRIDGE_VS_AUTO_PARTS_BETA_FADE", "trigger_count": 3, "positive_count": 2, "false_positive_count": 1, "do_not_count_as_new_case": true, "calibration_usable": false, "notes": "R13 source inventory row; used for cross-checkpoint only"}
{"row_type": "narrative_only", "narrative_id": "R13L85-SOURCE-R10", "round": "R13", "loop": 85, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW", "source_round": "R10", "source_file": "e2r_stock_web_v12_residual_round_R10_loop_85_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md", "source_large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "source_canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "source_fine_archetype_id": "SMALL_MID_BUILDER_PF_THEME_ORDERBOOK_MARGIN_BRIDGE_VS_HOUSING_SQUEEZE_FADE", "trigger_count": 3, "positive_count": 2, "false_positive_count": 1, "do_not_count_as_new_case": true, "calibration_usable": false, "notes": "R13 source inventory row; used for cross-checkpoint only"}
{"row_type": "narrative_only", "narrative_id": "R13L85-SOURCE-R11", "round": "R13", "loop": 85, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW", "source_round": "R11", "source_file": "e2r_stock_web_v12_residual_round_R11_loop_85_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md", "source_large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "source_canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "source_fine_archetype_id": "EAST_SEA_GAS_EXPLORATION_POLICY_EVENT_RESOURCE_OPTIONALITY_VS_THEME_SPIKE_FADE", "trigger_count": 3, "positive_count": 1, "false_positive_count": 2, "do_not_count_as_new_case": true, "calibration_usable": false, "notes": "R13 source inventory row; used for cross-checkpoint only"}
{"row_type": "narrative_only", "narrative_id": "R13L85-SOURCE-R12", "round": "R13", "loop": 85, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW", "source_round": "R12", "source_file": "e2r_stock_web_v12_residual_round_R12_loop_85_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md", "source_large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "source_canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "source_fine_archetype_id": "EDUCATION_POLICY_MEDICAL_SCHOOL_QUOTA_PRIVATE_EDU_DEMAND_REVENUE_BRIDGE_VS_THEME_SPIKE_FADE", "trigger_count": 3, "positive_count": 1, "false_positive_count": 2, "do_not_count_as_new_case": true, "calibration_usable": false, "notes": "R13 source inventory row; used for cross-checkpoint only"}
{"row_type": "trigger", "trigger_id": "R13L85-S2FP-01-THEME-MFE-DEMOTION", "case_id": "R13L85-S2FP-01", "symbol": "R13_CROSS_ARCHETYPE", "company_name": "Cross-archetype loop85 Stage2 false-positive review", "round": "R13", "loop": 85, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW", "fine_archetype_id": "LOOP85_FALSE_POSITIVE_THEME_MFE_HIGH_MAE_SOURCE_PROXY_BRIDGE_GAP_REVIEW", "loop_objective": "cross_archetype_stage2_false_positive_review|source_proxy_blocker|local_4B_review|hard_4C_protection|canonical_bridge_compression", "trigger_type": "R13_CROSS_STAGE2_FALSE_POSITIVE_REVIEW", "trigger_date": "2026-06-02", "entry_date": null, "entry_price": null, "evidence_available_at_that_date": "A theme candle can mark attention, but without a sector-specific economics bridge it should not validate Stage2.", "evidence_source": "derived_from_loop85_source_MDs; source_proxy_only_rows_not_promoted", "source_rounds": ["R1", "R2", "R3", "R4", "R5", "R7", "R8", "R9", "R10", "R11", "R12"], "source_canonical_group": "C01|C08|C14|C17|C20|C23|C26|C29|C30|C31", "price_data_source": "Songdaiki/stock-web via source MDs", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": null, "MFE_90D_pct": 13.96, "MFE_180D_pct": null, "MAE_30D_pct": null, "MAE_90D_pct": -22.37, "MAE_180D_pct": null, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "theme_only_MFE_not_stage2_actionable", "four_b_evidence_type": ["cross_checkpoint", "stage2_false_positive_review", "non_price_bridge_required"], "four_c_protection_label": "hard_4C_requires_non_price_thesis_break", "trigger_outcome_label": "demote_theme_only_stage2", "current_profile_verdict": "theme_only_MFE_not_stage2_actionable", "calibration_usable": true, "do_not_count_as_new_case": true, "dedupe_for_aggregate": true, "aggregate_group_role": "r13_cross_checkpoint", "is_new_independent_case": false, "reuse_reason": "R13 cross checkpoint; source cases already counted in R1~R12", "independent_evidence_weight": 0.0, "cross_scope": "theme_headline_MFE_not_stage2_without_bridge", "residual_error": "headline/theme MFE recurs without economics bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L85-S2FP-01", "trigger_id": "R13L85-S2FP-01-THEME-MFE-DEMOTION", "symbol": "R13_CROSS_ARCHETYPE", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW", "raw_component_scores_before": {"headline_strength_score": 65, "MFE_score": 45, "bridge_confirmation_score": 15, "source_quality_score": 20, "false_positive_risk_score": 75}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"headline_strength_score": 25, "MFE_score": 20, "bridge_confirmation_score": 5, "source_quality_score": 5, "false_positive_risk_score": 90}, "weighted_score_after": 44, "stage_label_after": "Rejected-Stage2 / RiskWatch", "changed_components": ["headline_strength_score", "MFE_score", "MAE_control_score", "bridge_confirmation_score", "source_quality_score", "riskwatch_score", "hard_4C_score", "canonical_specificity_score"], "component_delta_explanation": "A theme candle can mark attention, but without a sector-specific economics bridge it should not validate Stage2.", "MFE_90D_pct": 13.96, "MAE_90D_pct": -22.37, "score_return_alignment_label": "demote_theme_only_stage2", "current_profile_verdict": "theme_only_MFE_not_stage2_actionable", "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R13L85-S2FP-02-HIGH-MAE-REJECTION", "case_id": "R13L85-S2FP-02", "symbol": "R13_CROSS_ARCHETYPE", "company_name": "Cross-archetype loop85 Stage2 false-positive review", "round": "R13", "loop": 85, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW", "fine_archetype_id": "LOOP85_FALSE_POSITIVE_THEME_MFE_HIGH_MAE_SOURCE_PROXY_BRIDGE_GAP_REVIEW", "loop_objective": "cross_archetype_stage2_false_positive_review|source_proxy_blocker|local_4B_review|hard_4C_protection|canonical_bridge_compression", "trigger_type": "R13_CROSS_HIGH_MAE_FALSE_POSITIVE_REVIEW", "trigger_date": "2026-06-02", "entry_date": null, "entry_price": null, "evidence_available_at_that_date": "When the path gives a quick peak and then deep MAE, the bridge was usually missing at entry.", "evidence_source": "derived_from_loop85_source_MDs; source_proxy_only_rows_not_promoted", "source_rounds": ["R2", "R3", "R4", "R8", "R12"], "source_canonical_group": "C08|C14|C17|C26|C31", "price_data_source": "Songdaiki/stock-web via source MDs", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": null, "MFE_90D_pct": 23.56, "MFE_180D_pct": null, "MAE_30D_pct": null, "MAE_90D_pct": -33.58, "MAE_180D_pct": null, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "high_MAE_false_positive_blocks_stage2_validation", "four_b_evidence_type": ["cross_checkpoint", "stage2_false_positive_review", "non_price_bridge_required"], "four_c_protection_label": "hard_4C_requires_non_price_thesis_break", "trigger_outcome_label": "reject_or_riskwatch_high_MAE_false_positive", "current_profile_verdict": "high_MAE_false_positive_blocks_stage2_validation", "calibration_usable": true, "do_not_count_as_new_case": true, "dedupe_for_aggregate": true, "aggregate_group_role": "r13_cross_checkpoint", "is_new_independent_case": false, "reuse_reason": "R13 cross checkpoint; source cases already counted in R1~R12", "independent_evidence_weight": 0.0, "cross_scope": "high_MAE_false_positive_rejection", "residual_error": "tradable MFE followed by severe MAE is common in false positives"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L85-S2FP-02", "trigger_id": "R13L85-S2FP-02-HIGH-MAE-REJECTION", "symbol": "R13_CROSS_ARCHETYPE", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW", "raw_component_scores_before": {"MFE_score": 55, "MAE_control_score": 20, "bridge_confirmation_score": 10, "riskwatch_score": 60, "green_readiness_score": 30}, "weighted_score_before": 60, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"MFE_score": 25, "MAE_control_score": 10, "bridge_confirmation_score": 0, "riskwatch_score": 95, "green_readiness_score": 0}, "weighted_score_after": 43, "stage_label_after": "Rejected-Stage2 / High-MAE RiskWatch", "changed_components": ["headline_strength_score", "MFE_score", "MAE_control_score", "bridge_confirmation_score", "source_quality_score", "riskwatch_score", "hard_4C_score", "canonical_specificity_score"], "component_delta_explanation": "When the path gives a quick peak and then deep MAE, the bridge was usually missing at entry.", "MFE_90D_pct": 23.56, "MAE_90D_pct": -33.58, "score_return_alignment_label": "reject_or_riskwatch_high_MAE_false_positive", "current_profile_verdict": "high_MAE_false_positive_blocks_stage2_validation", "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R13L85-S2FP-03-LOW-MFE-VALUE-TRAP", "case_id": "R13L85-S2FP-03", "symbol": "R13_CROSS_ARCHETYPE", "company_name": "Cross-archetype loop85 Stage2 false-positive review", "round": "R13", "loop": 85, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW", "fine_archetype_id": "LOOP85_FALSE_POSITIVE_THEME_MFE_HIGH_MAE_SOURCE_PROXY_BRIDGE_GAP_REVIEW", "loop_objective": "cross_archetype_stage2_false_positive_review|source_proxy_blocker|local_4B_review|hard_4C_protection|canonical_bridge_compression", "trigger_type": "R13_CROSS_LOW_MFE_FALSE_POSITIVE_REVIEW", "trigger_date": "2026-06-02", "entry_date": null, "entry_price": null, "evidence_available_at_that_date": "If even the favorable window cannot produce enough MFE, the trigger is usually only theme language, not E2R.", "evidence_source": "derived_from_loop85_source_MDs; source_proxy_only_rows_not_promoted", "source_rounds": ["R3", "R4", "R8", "R10"], "source_canonical_group": "C14|C17|C26|C30", "price_data_source": "Songdaiki/stock-web via source MDs", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": null, "MFE_90D_pct": 5.21, "MFE_180D_pct": null, "MAE_30D_pct": null, "MAE_90D_pct": -16.75, "MAE_180D_pct": null, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "low_MFE_without_bridge_rejected", "four_b_evidence_type": ["cross_checkpoint", "stage2_false_positive_review", "non_price_bridge_required"], "four_c_protection_label": "hard_4C_requires_non_price_thesis_break", "trigger_outcome_label": "reject_low_MFE_stage2_watch", "current_profile_verdict": "low_MFE_without_bridge_rejected", "calibration_usable": true, "do_not_count_as_new_case": true, "dedupe_for_aggregate": true, "aggregate_group_role": "r13_cross_checkpoint", "is_new_independent_case": false, "reuse_reason": "R13 cross checkpoint; source cases already counted in R1~R12", "independent_evidence_weight": 0.0, "cross_scope": "low_MFE_false_positive_value_trap_review", "residual_error": "low-MFE cases are often value traps or weak rebounds"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L85-S2FP-03", "trigger_id": "R13L85-S2FP-03-LOW-MFE-VALUE-TRAP", "symbol": "R13_CROSS_ARCHETYPE", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW", "raw_component_scores_before": {"MFE_score": 20, "MAE_control_score": 35, "bridge_confirmation_score": 10, "theme_score": 40, "false_positive_risk_score": 65}, "weighted_score_before": 56, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"MFE_score": 5, "MAE_control_score": 25, "bridge_confirmation_score": 0, "theme_score": 15, "false_positive_risk_score": 85}, "weighted_score_after": 42, "stage_label_after": "Rejected-Stage2 / Low-MFE RiskWatch", "changed_components": ["headline_strength_score", "MFE_score", "MAE_control_score", "bridge_confirmation_score", "source_quality_score", "riskwatch_score", "hard_4C_score", "canonical_specificity_score"], "component_delta_explanation": "If even the favorable window cannot produce enough MFE, the trigger is usually only theme language, not E2R.", "MFE_90D_pct": 5.21, "MAE_90D_pct": -16.75, "score_return_alignment_label": "reject_low_MFE_stage2_watch", "current_profile_verdict": "low_MFE_without_bridge_rejected", "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R13L85-S2FP-04-SOURCE-PROXY-BLOCKER", "case_id": "R13L85-S2FP-04", "symbol": "R13_CROSS_ARCHETYPE", "company_name": "Cross-archetype loop85 Stage2 false-positive review", "round": "R13", "loop": 85, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW", "fine_archetype_id": "LOOP85_FALSE_POSITIVE_THEME_MFE_HIGH_MAE_SOURCE_PROXY_BRIDGE_GAP_REVIEW", "loop_objective": "cross_archetype_stage2_false_positive_review|source_proxy_blocker|local_4B_review|hard_4C_protection|canonical_bridge_compression", "trigger_type": "R13_CROSS_SOURCE_REPAIR_BLOCKER", "trigger_date": "2026-06-02", "entry_date": null, "entry_price": null, "evidence_available_at_that_date": "Observed price-path alignment is useful for calibration, but it cannot replace primary source timing and non-price evidence.", "evidence_source": "derived_from_loop85_source_MDs; source_proxy_only_rows_not_promoted", "source_rounds": ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10", "R11", "R12"], "source_canonical_group": "all_loop85_canonicals", "price_data_source": "Songdaiki/stock-web via source MDs", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": null, "MFE_90D_pct": 13.96, "MFE_180D_pct": null, "MAE_30D_pct": null, "MAE_90D_pct": -22.37, "MAE_180D_pct": null, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "block_runtime_promotion_until_source_repair", "four_b_evidence_type": ["cross_checkpoint", "stage2_false_positive_review", "non_price_bridge_required"], "four_c_protection_label": "hard_4C_requires_non_price_thesis_break", "trigger_outcome_label": "hold_shadow_only_do_not_promote", "current_profile_verdict": "block_runtime_promotion_until_source_repair", "calibration_usable": true, "do_not_count_as_new_case": true, "dedupe_for_aggregate": true, "aggregate_group_role": "r13_cross_checkpoint", "is_new_independent_case": false, "reuse_reason": "R13 cross checkpoint; source cases already counted in R1~R12", "independent_evidence_weight": 0.0, "cross_scope": "source_proxy_evidence_url_pending_runtime_blocker", "residual_error": "every loop85 MD marks evidence as source_proxy_only/evidence_url_pending"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L85-S2FP-04", "trigger_id": "R13L85-S2FP-04-SOURCE-PROXY-BLOCKER", "symbol": "R13_CROSS_ARCHETYPE", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW", "raw_component_scores_before": {"price_alignment_score": 60, "source_quality_score": 20, "bridge_confirmation_score": 25, "runtime_promotion_score": 45, "false_positive_risk_score": 65}, "weighted_score_before": 63, "stage_label_before": "Stage2-Actionable candidate", "raw_component_scores_after": {"price_alignment_score": 60, "source_quality_score": 5, "bridge_confirmation_score": 10, "runtime_promotion_score": 0, "false_positive_risk_score": 85}, "weighted_score_after": 48, "stage_label_after": "Hold: source-repair queue", "changed_components": ["headline_strength_score", "MFE_score", "MAE_control_score", "bridge_confirmation_score", "source_quality_score", "riskwatch_score", "hard_4C_score", "canonical_specificity_score"], "component_delta_explanation": "Observed price-path alignment is useful for calibration, but it cannot replace primary source timing and non-price evidence.", "MFE_90D_pct": 13.96, "MAE_90D_pct": -22.37, "score_return_alignment_label": "hold_shadow_only_do_not_promote", "current_profile_verdict": "block_runtime_promotion_until_source_repair", "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R13L85-S2FP-05-LOCAL-4B-NOT-FULL-4C", "case_id": "R13L85-S2FP-05", "symbol": "R13_CROSS_ARCHETYPE", "company_name": "Cross-archetype loop85 Stage2 false-positive review", "round": "R13", "loop": 85, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW", "fine_archetype_id": "LOOP85_FALSE_POSITIVE_THEME_MFE_HIGH_MAE_SOURCE_PROXY_BRIDGE_GAP_REVIEW", "loop_objective": "cross_archetype_stage2_false_positive_review|source_proxy_blocker|local_4B_review|hard_4C_protection|canonical_bridge_compression", "trigger_type": "R13_CROSS_LOCAL_4B_4C_PROTECTION", "trigger_date": "2026-06-02", "entry_date": null, "entry_price": null, "evidence_available_at_that_date": "Local 4B is a speed warning after MFE; hard 4C still requires a non-price thesis break.", "evidence_source": "derived_from_loop85_source_MDs; source_proxy_only_rows_not_promoted", "source_rounds": ["R2", "R5", "R8", "R10", "R11", "R12"], "source_canonical_group": "C08|C20|C26|C30|C31", "price_data_source": "Songdaiki/stock-web via source MDs", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": null, "MFE_90D_pct": 13.96, "MFE_180D_pct": null, "MAE_30D_pct": null, "MAE_90D_pct": -22.37, "MAE_180D_pct": null, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "local_4B_yes_hard_4C_no_without_non_price_break", "four_b_evidence_type": ["cross_checkpoint", "stage2_false_positive_review", "non_price_bridge_required"], "four_c_protection_label": "hard_4C_requires_non_price_thesis_break", "trigger_outcome_label": "allow_local_4B_keep_hard_4C_non_price_only", "current_profile_verdict": "local_4B_yes_hard_4C_no_without_non_price_break", "calibration_usable": true, "do_not_count_as_new_case": true, "dedupe_for_aggregate": true, "aggregate_group_role": "r13_cross_checkpoint", "is_new_independent_case": false, "reuse_reason": "R13 cross checkpoint; source cases already counted in R1~R12", "independent_evidence_weight": 0.0, "cross_scope": "local_4B_watch_before_full_4B_or_hard_4C", "residual_error": "post-peak drawdown can tempt over-routing into hard 4C"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L85-S2FP-05", "trigger_id": "R13L85-S2FP-05-LOCAL-4B-NOT-FULL-4C", "symbol": "R13_CROSS_ARCHETYPE", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW", "raw_component_scores_before": {"post_peak_drawdown_score": 80, "non_price_break_score": 20, "local_4B_score": 45, "hard_4C_score": 65, "misroute_risk_score": 80}, "weighted_score_before": 64, "stage_label_before": "possible full 4B / possible hard 4C", "raw_component_scores_after": {"post_peak_drawdown_score": 80, "non_price_break_score": 20, "local_4B_score": 90, "hard_4C_score": 25, "misroute_risk_score": 35}, "weighted_score_after": 72, "stage_label_after": "Local 4B Watch; hard 4C blocked until non-price break", "changed_components": ["headline_strength_score", "MFE_score", "MAE_control_score", "bridge_confirmation_score", "source_quality_score", "riskwatch_score", "hard_4C_score", "canonical_specificity_score"], "component_delta_explanation": "Local 4B is a speed warning after MFE; hard 4C still requires a non-price thesis break.", "MFE_90D_pct": 13.96, "MAE_90D_pct": -22.37, "score_return_alignment_label": "allow_local_4B_keep_hard_4C_non_price_only", "current_profile_verdict": "local_4B_yes_hard_4C_no_without_non_price_break", "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R13L85-S2FP-06-CANONICAL-BRIDGE-FAMILY", "case_id": "R13L85-S2FP-06", "symbol": "R13_CROSS_ARCHETYPE", "company_name": "Cross-archetype loop85 Stage2 false-positive review", "round": "R13", "loop": 85, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW", "fine_archetype_id": "LOOP85_FALSE_POSITIVE_THEME_MFE_HIGH_MAE_SOURCE_PROXY_BRIDGE_GAP_REVIEW", "loop_objective": "cross_archetype_stage2_false_positive_review|source_proxy_blocker|local_4B_review|hard_4C_protection|canonical_bridge_compression", "trigger_type": "R13_CROSS_CANONICAL_COMPRESSION", "trigger_date": "2026-06-02", "entry_date": null, "entry_price": null, "evidence_available_at_that_date": "A blunt global penalty would flatten the map; the correct repair is canonical-specific grammar.", "evidence_source": "derived_from_loop85_source_MDs; source_proxy_only_rows_not_promoted", "source_rounds": ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10", "R11", "R12"], "source_canonical_group": "all_loop85_canonicals", "price_data_source": "Songdaiki/stock-web via source MDs", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": null, "MFE_90D_pct": 13.96, "MFE_180D_pct": null, "MAE_30D_pct": null, "MAE_90D_pct": -22.37, "MAE_180D_pct": null, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "do_not_apply_new_global_weight", "four_b_evidence_type": ["cross_checkpoint", "stage2_false_positive_review", "non_price_bridge_required"], "four_c_protection_label": "hard_4C_requires_non_price_thesis_break", "trigger_outcome_label": "keep_bridge_rules_canonical_specific_not_global_weight", "current_profile_verdict": "do_not_apply_new_global_weight", "calibration_usable": true, "do_not_count_as_new_case": true, "dedupe_for_aggregate": true, "aggregate_group_role": "r13_cross_checkpoint", "is_new_independent_case": false, "reuse_reason": "R13 cross checkpoint; source cases already counted in R1~R12", "independent_evidence_weight": 0.0, "cross_scope": "canonical_specific_bridge_family_compression", "residual_error": "the same headline-to-economics gap recurs, but each sector has a different bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L85-S2FP-06", "trigger_id": "R13L85-S2FP-06-CANONICAL-BRIDGE-FAMILY", "symbol": "R13_CROSS_ARCHETYPE", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW", "raw_component_scores_before": {"global_rule_simplicity_score": 70, "canonical_specificity_score": 35, "overfit_risk_score": 70, "bridge_family_score": 60, "source_repair_need_score": 80}, "weighted_score_before": 58, "stage_label_before": "possible new global rule", "raw_component_scores_after": {"global_rule_simplicity_score": 35, "canonical_specificity_score": 85, "overfit_risk_score": 35, "bridge_family_score": 90, "source_repair_need_score": 80}, "weighted_score_after": 74, "stage_label_after": "canonical-specific shadow family only", "changed_components": ["headline_strength_score", "MFE_score", "MAE_control_score", "bridge_confirmation_score", "source_quality_score", "riskwatch_score", "hard_4C_score", "canonical_specificity_score"], "component_delta_explanation": "A blunt global penalty would flatten the map; the correct repair is canonical-specific grammar.", "MFE_90D_pct": 13.96, "MAE_90D_pct": -22.37, "score_return_alignment_label": "keep_bridge_rules_canonical_specific_not_global_weight", "current_profile_verdict": "do_not_apply_new_global_weight", "do_not_count_as_new_case": true}
{"row_type": "shadow_weight", "axis": "R13_loop85_stage2_false_positive_bridge_source_repair_local_4B_guardrail", "scope": "cross_archetype_checkpoint_only", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Loop85 R1~R12 cases repeatedly show Stage2 false positives arise from theme MFE without canonical economics bridge; source-proxy rows must not promote; local 4B can precede full 4B; hard 4C requires non-price thesis break.", "backtest_effect": "no production weight; cross-checkpoint reinforces existing false-positive and bridge guardrails", "trigger_ids": "R13L85-S2FP-01-THEME-MFE-DEMOTION|R13L85-S2FP-02-HIGH-MAE-REJECTION|R13L85-S2FP-03-LOW-MFE-VALUE-TRAP|R13L85-S2FP-04-SOURCE-PROXY-BLOCKER|R13L85-S2FP-05-LOCAL-4B-NOT-FULL-4C|R13L85-S2FP-06-CANONICAL-BRIDGE-FAMILY", "calibration_usable_count": 6, "new_independent_case_count": 0, "counterexample_count": 0, "confidence": "medium", "proposal_type": "r13_cross_checkpoint_shadow_only", "notes": "do_not_count_as_new_case=true; source repair required; not production"}
{"row_type": "residual_contribution", "round": "R13", "loop": 85, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW", "new_independent_case_count": 0, "reused_case_count": 12, "new_symbol_count": 0, "new_trigger_family_count": 0, "source_trigger_count": 36, "source_false_positive_trigger_count": 21, "source_positive_trigger_count": 15, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "source_proxy_only_blocks_runtime_promotion", "high_MAE_guardrail", "local_4B_watch_before_full_4B_when_MFE_outruns_bridge"], "residual_error_types_found": ["theme_headline_MFE_not_stage2_without_bridge", "high_MAE_false_positive_rejection", "low_MFE_value_trap_rejection", "source_proxy_runtime_promotion_risk", "local_4B_late_when_MFE_outruns_bridge", "price_only_hard_4C_misroute_risk", "global_weight_overfit_risk"], "loop_contribution_label": "cross_archetype_stage2_false_positive_review", "do_not_propose_new_weight_delta": true, "do_not_count_as_new_case": true}
```

## 23. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

This R13 file is not live candidate research and is not a new sector-positive source. It is a cross-archetype Stage2 false-positive review over loop85 R1~R12 source MDs.

### Rules

- Treat every R13 `trigger` row as `do_not_count_as_new_case=true`.
- Do not add R13 rows to new independent case counts.
- Do not infer new runtime weights from R13 alone.
- Use R13 rows to validate guardrails:
  - theme/headline MFE cannot validate Stage2 without canonical economics bridge
  - low-MFE false positives are rejected
  - high-MAE false positives are rejected or wrapped as RiskWatch
  - source_proxy_only/evidence_url_pending blocks runtime promotion
  - local 4B watch can exist before full 4B
  - hard 4C requires non-price thesis break
  - bridge rules should remain canonical-specific, not global blunt weights
- Keep production scoring unchanged unless a later batch validates primary evidence and aggregate thresholds.

## 24. Next Round State

```text
completed_round = R13
completed_loop = 85
next_round = R1
next_loop = 86
round_schedule_status = valid
round_sector_consistency = pass
```

## 25. Source Notes

```text
MAIN_EXECUTION_PROMPT = docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
NO_REPEAT_INDEX = docs/core/V12_Research_No_Repeat_Index.md
price_source = Songdaiki/stock-web
```
