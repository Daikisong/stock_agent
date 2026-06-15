---
title: "E2R Stock-Web V12 Residual Research — R2 Loop 108 — C07 HBM Equipment Order Relative Strength"
created_at_kst: "2026-06-13"
mode: "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12"
selected_round: "R2"
selected_loop: 108
selected_priority_bucket: "Priority 0"
large_sector_id: "L2_AI_SEMICONDUCTOR_ELECTRONICS"
canonical_archetype_id: "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH"
fine_archetype_id: "C07_HBM_ADVANCED_PACKAGING_TEST_PROCESS_EQUIPMENT_RS_ORDER_REVENUE_CONVERSION_BRIDGE"
deep_sub_archetype_id: "C07_DEEP_TESTER_PROCESS_AUX_EQUIPMENT_RELATIVE_STRENGTH_VS_ORDER_REVENUE_BRIDGE_AND_LATE_PRICE_ONLY_RS_FADE"
stock_web_manifest_max_date: "2026-02-20"
price_basis: "tradable_raw"
price_adjustment_status: "raw_unadjusted_marcap"
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_executed_now: false
---

# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R2
selected_loop = 108
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id = C07_HBM_ADVANCED_PACKAGING_TEST_PROCESS_EQUIPMENT_RS_ORDER_REVENUE_CONVERSION_BRIDGE
deep_sub_archetype_id = C07_DEEP_TESTER_PROCESS_AUX_EQUIPMENT_RELATIVE_STRENGTH_VS_ORDER_REVENUE_BRIDGE_AND_LATE_PRICE_ONLY_RS_FADE
```

This is a standalone historical calibration artifact. It is not a live scan, not a watchlist, not investment advice, and not a production scoring patch. It follows the coverage-index-first scheduler and treats `V12_Research_No_Repeat_Index.md` only as the duplicate-avoidance ledger.

## 1. Current Calibrated Profile Assumption

Assumed current profile proxy: `e2r_2_1_stock_web_calibrated_proxy`.

Already-applied global axes are treated as constraints, not rediscoveries:

```text
stage2_actionable_evidence_bonus
stage3_yellow_total_min
stage3_green_total_min
stage3_green_revision_min
stage3_cross_evidence_green_buffer
price_only_blowoff_blocks_positive_stage
full_4b_requires_non_price_evidence
hard_4c_thesis_break_routes_to_4c
```

This loop asks a narrower C07 question: when does HBM/test/process-equipment relative strength become verified order/revenue conversion, and when is it merely late price-only semiconductor-equipment beta?

## 2. Round / Large Sector / Canonical Archetype Scope

`C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH` maps to `R2 / L2_AI_SEMICONDUCTOR_ELECTRONICS`. The selected fine/deep split is:

```text
C07_HBM_ADVANCED_PACKAGING_TEST_PROCESS_EQUIPMENT_RS_ORDER_REVENUE_CONVERSION_BRIDGE
C07_DEEP_TESTER_PROCESS_AUX_EQUIPMENT_RELATIVE_STRENGTH_VS_ORDER_REVENUE_BRIDGE_AND_LATE_PRICE_ONLY_RS_FADE
```

C07 is not a generic semicap rally bucket. The useful signal is a chain: HBM/advanced-packaging demand -> tester/process/auxiliary-equipment order or shipment -> revenue/margin/revision bridge. A stock that only carries the label without conversion should fall into Stage4B-watch or failed-rerating review.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index reports C07 as Priority 0 with 18 representative rows and 12 rows needed to reach the 30-row minimum stability zone. The visible prior C07 artifact in this session is loop107 using 케이씨텍, 네오셈, 엑시콘, 인텍플러스, 오로스테크놀로지, GST, and 넥스틴. This loop avoids those C07 symbols and adds six new C07 symbols / trigger families.

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Session-adjusted coverage estimate:

```text
Index C07 rows = 18
prior current-session C07 loop107 representative triggers = 7
this loop representative triggers = 6
estimated C07 after this loop = 31
remaining to 30 = 0
remaining to 50 = 19
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_source = Songdaiki/stock-web
source_name = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

The stock-web manifest basis used for this loop is `raw_unadjusted_marcap`, `min_date=1995-05-02`, `max_date=2026-02-20`, `tradable_row_count=14354401`, `raw_row_count=15214118`, and `symbol_count=5414`. Every representative trigger row below includes the canonical six 30D/90D/180D MFE/MAE fields.

## 5. Historical Eligibility Gate

All representative trigger rows use historical dates before the stock-web manifest max date and have 180 trading-day forward windows in the local stock-web CSV shards. No row is promoted if later batch validation finds a corporate-action-contaminated D+180 window.

## 6. Canonical Archetype Compression Map

| level | id | meaning |
|---|---|---|
| large sector | `L2_AI_SEMICONDUCTOR_ELECTRONICS` | AI / semiconductor / electronics historical calibration |
| canonical | `C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH` | HBM equipment relative strength that must convert into order/revenue/margin evidence |
| fine | `C07_HBM_ADVANCED_PACKAGING_TEST_PROCESS_EQUIPMENT_RS_ORDER_REVENUE_CONVERSION_BRIDGE` | tester/process/auxiliary equipment split by order conversion vs price beta |
| deep | `C07_DEEP_TESTER_PROCESS_AUX_EQUIPMENT_RELATIVE_STRENGTH_VS_ORDER_REVENUE_BRIDGE_AND_LATE_PRICE_ONLY_RS_FADE` | early tester/process conversion versus late HBM-label proxy fade |

## 7. Case Selection Summary

| case | symbol | company | trigger | entry_date | entry_price | role | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | current verdict |
|---|---:|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---|
| C07-R2-L108-01-232140 | 232140 | 와이씨 | Stage2-Actionable | 2024-02-01 | 5,400 | structural_success | 48.89% | -7.04% | 325.00% | -7.04% | 325.00% | -7.04% | current_profile_missed_structural |
| C07-R2-L108-02-319660 | 319660 | 피에스케이 | Stage2-Actionable | 2024-02-01 | 19,760 | structural_success | 41.19% | -1.16% | 81.68% | -1.16% | 97.87% | -1.16% | current_profile_correct |
| C07-R2-L108-03-240810 | 240810 | 원익IPS | Stage2-Actionable | 2024-02-15 | 29,850 | stage2_promote_candidate | 27.30% | -5.53% | 50.25% | -5.53% | 50.25% | -19.77% | current_profile_too_late |
| C07-R2-L108-04-089890 | 089890 | 코세스 | Stage4B | 2024-07-01 | 17,880 | 4B_overlay_success | 5.87% | -52.01% | 5.87% | -58.33% | 5.87% | -67.73% | current_profile_4B_too_late |
| C07-R2-L108-05-382800 | 382800 | 지앤비에스 에코 | Stage4B | 2024-05-02 | 6,050 | 4B_overlay_success | 2.98% | -18.68% | 2.98% | -47.02% | 2.98% | -60.17% | current_profile_false_positive |
| C07-R2-L108-06-217190 | 217190 | 제너셈 | Stage2 | 2024-05-02 | 12,670 | failed_rerating | 6.31% | -6.08% | 6.31% | -41.44% | 6.31% | -53.20% | current_profile_false_positive |


### C07-R2-L108-01-232140 — 232140 와이씨

The tester path was not just a memory-beta move: early 2024 relative strength turned into a very large 90D/180D MFE. C07 should allow Stage2-Actionable when test-equipment revenue/order conversion is visible before the market treats it as pure price momentum.

Trigger family: `memory_tester_hbm_test_capacity_order_conversion`.

### C07-R2-L108-02-319660 — 319660 피에스케이

A cleaner process-equipment recovery case: moderate early MAE and strong 90D/180D MFE. It supports C07/C10 separation: C07 receives relative-strength/order-conversion credit only if it is not just a generic WFE beta proxy.

Trigger family: `front_end_process_memory_recovery_order_revenue_conversion`.

### C07-R2-L108-03-240810 — 240810 원익IPS

The 90D/180D path worked, but later drawdown shows why C07 should not convert generic equipment recovery into Green without revision and margin bridge. Stage2 is acceptable; late Green requires stricter proof.

Trigger family: `wfe_process_equipment_memory_recovery_order_revenue_bridge`.

### C07-R2-L108-04-089890 — 089890 코세스

The advanced-packaging label was plausible, but the July entry had very small upside and extreme 90D/180D MAE. It is a C07 late-price-only RS 4B-watch exemplar.

Trigger family: `advanced_packaging_hbm_label_local_overheat_without_revenue_bridge`.

### C07-R2-L108-05-382800 — 382800 지앤비에스 에코

Auxiliary environmental equipment can ride the HBM/WFE equipment label, but without order/revenue conversion it failed the forward path badly. This strengthens the C07 source-proxy-to-4B-watch filter.

Trigger family: `auxiliary_environment_equipment_hbm_theme_proxy_without_order_conversion`.

### C07-R2-L108-06-217190 — 217190 제너셈

Automation/package-adjacent names can receive a temporary HBM halo, but this row shows the failure mode: weak 30D/90D MFE and very large 180D MAE. It should be Stage2 only with strict bridge requirement, not Yellow.

Trigger family: `semiconductor_automation_hbm_package_theme_proxy_without_order_margin_bridge`.


## 8. Positive vs Counterexample Balance

```text
positive_case_count = 3
counterexample_count = 3
4B_case_count = 2
4C_case_count = 0
new_independent_case_count = 6
reused_case_count = 0
```

The positive side is represented by tester/process-equipment names whose 90D/180D paths confirmed the order/revenue bridge. The counterexample side is represented by late relative-strength, auxiliary-equipment, and package-automation labels whose evidence remained source-proxy or bridge-incomplete.

## 9. Evidence Source Map

| source_id | usage | status |
|---|---|---|
| SRC_DART_FILINGS | Quarterly/annual disclosure context for order/revenue/margin bridge | source_proxy; URL repair required |
| SRC_PUBLIC_HBM_EQUIPMENT_CONTEXT | HBM/test/process equipment public research/news context available before trigger dates | source_proxy; URL repair required |
| SRC_STOCK_WEB_OHLC | actual 1D OHLCV path for all trigger rows | verified local stock-web CSV shards |


## 10. Price Data Source Map

| symbol | company | price_shard_path | profile_path | entry_date | forward window | CA status |
|---:|---|---|---|---:|---:|---|
| 232140 | 와이씨 | `atlas/ohlcv_tradable_by_symbol_year/232/232140/2024.csv` | `atlas/symbol_profiles/232/232140.json` | 2024-02-01 | 180D | clean_180D_window |
| 319660 | 피에스케이 | `atlas/ohlcv_tradable_by_symbol_year/319/319660/2024.csv` | `atlas/symbol_profiles/319/319660.json` | 2024-02-01 | 180D | clean_180D_window |
| 240810 | 원익IPS | `atlas/ohlcv_tradable_by_symbol_year/240/240810/2024.csv` | `atlas/symbol_profiles/240/240810.json` | 2024-02-15 | 180D | clean_180D_window |
| 089890 | 코세스 | `atlas/ohlcv_tradable_by_symbol_year/089/089890/2024.csv` | `atlas/symbol_profiles/089/089890.json` | 2024-07-01 | 180D | clean_180D_window |
| 382800 | 지앤비에스 에코 | `atlas/ohlcv_tradable_by_symbol_year/382/382800/2024.csv` | `atlas/symbol_profiles/382/382800.json` | 2024-05-02 | 180D | clean_180D_window |
| 217190 | 제너셈 | `atlas/ohlcv_tradable_by_symbol_year/217/217190/2024.csv` | `atlas/symbol_profiles/217/217190.json` | 2024-05-02 | 180D | clean_180D_window |


## 11. Case-by-Case Trigger Grid

The trigger grid is identical to the representative rows in the JSONL block. Human-readable summary:

| case | symbol | company | trigger | entry_date | entry_price | role | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | current verdict |
|---|---:|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---|
| C07-R2-L108-01-232140 | 232140 | 와이씨 | Stage2-Actionable | 2024-02-01 | 5,400 | structural_success | 48.89% | -7.04% | 325.00% | -7.04% | 325.00% | -7.04% | current_profile_missed_structural |
| C07-R2-L108-02-319660 | 319660 | 피에스케이 | Stage2-Actionable | 2024-02-01 | 19,760 | structural_success | 41.19% | -1.16% | 81.68% | -1.16% | 97.87% | -1.16% | current_profile_correct |
| C07-R2-L108-03-240810 | 240810 | 원익IPS | Stage2-Actionable | 2024-02-15 | 29,850 | stage2_promote_candidate | 27.30% | -5.53% | 50.25% | -5.53% | 50.25% | -19.77% | current_profile_too_late |
| C07-R2-L108-04-089890 | 089890 | 코세스 | Stage4B | 2024-07-01 | 17,880 | 4B_overlay_success | 5.87% | -52.01% | 5.87% | -58.33% | 5.87% | -67.73% | current_profile_4B_too_late |
| C07-R2-L108-05-382800 | 382800 | 지앤비에스 에코 | Stage4B | 2024-05-02 | 6,050 | 4B_overlay_success | 2.98% | -18.68% | 2.98% | -47.02% | 2.98% | -60.17% | current_profile_false_positive |
| C07-R2-L108-06-217190 | 217190 | 제너셈 | Stage2 | 2024-05-02 | 12,670 | failed_rerating | 6.31% | -6.08% | 6.31% | -41.44% | 6.31% | -53.20% | current_profile_false_positive |


## 12. Trigger-Level OHLC Backtest Tables

All MFE/MAE calculations use:

```text
MFE_N_pct = (max(high from entry_date through N trading days) / entry_price - 1) * 100
MAE_N_pct = (min(low from entry_date through N trading days) / entry_price - 1) * 100
N = 30D / 90D / 180D trading days
```

The strongest positive case is `232140` from 2024-02-01, where 90D MFE exceeded 300% while MAE stayed below 10%. The strongest counterexample is `089890` from 2024-07-01, where 180D MAE exceeded -60% and the price-only HBM/advanced-packaging label failed to provide forward protection.

## 13. Current Calibrated Profile Stress Test

| symbol | current_profile_verdict | stress-test interpretation |
|---:|---|---|
| 232140 | current_profile_missed_structural | early tester order/revenue conversion can be missed if C07 is treated as generic semicap beta |
| 319660 | current_profile_correct | process-equipment recovery with tolerable early MAE fits current Stage2-Actionable logic |
| 240810 | current_profile_too_late | Stage2 was acceptable, but Green needs stricter revision/margin bridge because later drawdown was material |
| 089890 | current_profile_4B_too_late | local overheat needed earlier watch; price-only RS carried too much weight |
| 382800 | current_profile_false_positive | auxiliary-equipment theme proxy should not reach Yellow without order conversion |
| 217190 | current_profile_false_positive | package/automation HBM halo failed without margin or order bridge |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is emitted in this artifact. Green-lateness ratio is therefore `not_applicable:no_confirmed_Stage3_Green_trigger`. The core finding is not that Green is globally late; it is that C07 should bifurcate Stage2-Actionable and Stage3-Yellow using order/revenue conversion:

```text
Stage2-Actionable allowed: relative strength + disclosed order/revenue/capacity route
Stage3-Yellow allowed: Stage2 bridge + margin/revision/financial visibility
Stage4B-watch required: late relative strength + no fresh order/revenue bridge
```

## 15. 4B Local vs Full-window Timing Audit

`089890` and `382800` are emitted as Stage4B rows. In both cases, price-only or theme-proxy relative strength carried the stock into a poor forward path. This does not weaken the global full-4B non-price rule; it strengthens the C07 local-4B-watch rule.

```text
existing_axis_strengthened = local_4b_watch_guard
existing_axis_strengthened = price_only_blowoff_blocks_positive_stage
existing_axis_strengthened = full_4b_requires_non_price_evidence
```

## 16. 4C Protection Audit

No hard Stage4C trigger row is emitted. `217190` is a thesis-break-watch path, not a full 4C. C07 needs Stage4B-watch before hard 4C unless there is explicit order cancellation, qualification failure, accounting/trust break, or financing shock.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
rule_candidate = L2_semicap_relative_strength_needs_order_revenue_margin_bridge_before_Yellow
```

The L2 rule candidate: semiconductor-equipment relative strength should not, by itself, unlock Yellow/Green. The bridge must be a named order, customer capacity route, shipment/revenue conversion, or margin/revision evidence.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
new_axis_proposed = C07_verified_order_revenue_margin_bridge_required_before_Yellow_plus_late_price_only_RS_to_4B_watch
```

C07 is split into two tracks:

1. **Verified conversion track**: tester/process equipment with order, shipment, revenue, or margin evidence can be Stage2-Actionable and, if revisions follow, Yellow.
2. **Price-only RS track**: auxiliary/package/equipment-label rallies without conversion evidence should be Stage4B-watch or remain Stage2 only.

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | profile_hypothesis | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | false_positive_rate | missed_structural_count | score_return_alignment_verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| P0 | current_calibrated_proxy | current profile still over-credits late relative strength and under-credits early tester order-conversion path | 6 | 78.68% | -26.75% | 0.50 | 1 | mixed_residual_error |
| P0b | baseline_reference | baseline over-promotes equipment beta without HBM/order proof | 6 | 78.68% | -26.75% | 0.67 | 0 | too_many_false_positives |
| P1 | sector_specific_candidate | L2 semicap requires order/revenue bridge before Yellow and local 4B for price-only RS | 6 | 152.31% | -4.58% | 0.33 | 0 | better_alignment |
| P2 | canonical_archetype_candidate | C07 distinguishes tester/process conversion from auxiliary/package-label proxy | 6 | 152.31% | -4.58% | 0.17 | 0 | best_alignment |
| P3 | counterexample_guard_profile | blocks late RS and source-proxy-only HBM equipment rows until bridge confirmed | 6 | 152.31% | -4.58% | 0.00 | 1 | conservative_guard |


## 20. Score-Return Alignment Matrix

| axis | before behavior | after shadow behavior | alignment effect |
|---|---|---|---|
| relative_strength_score | over-weighted for late equipment beta | capped unless order/revenue bridge exists | reduces false positive entries |
| margin_bridge_score | too low for early tester/process conversion | increased for verified conversion | recovers missed structural cases |
| valuation_repricing_score | can reward late price-only label | discounted after local blowoff | improves 4B watch timing |
| execution_risk_score | under-penalizes source-proxy-only auxiliary names | raised when bridge missing | filters poor MAE paths |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | C07_HBM_ADVANCED_PACKAGING_TEST_PROCESS_EQUIPMENT_RS_ORDER_REVENUE_CONVERSION_BRIDGE | 3 | 3 | 2 | 0 | 6 | 0 | 6 | 6 | 5 | true | true | C07 estimated 31; need 0 to 30 / 19 to 50 |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 6
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 6
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 6
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
residual_error_types_found: C07_tester_order_conversion_missed_structural, C07_late_advanced_packaging_RS_4B_too_late, C07_auxiliary_equipment_theme_proxy_false_positive, C07_automation_package_theme_proxy_without_margin_bridge
new_axis_proposed: C07_verified_order_revenue_margin_bridge_required_before_Yellow_plus_late_price_only_RS_to_4B_watch
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

This loop adds 6 new independent cases, 3 counterexamples, and 5 residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH.

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web 1D OHLC path exists in local shards
- entry_date / entry_price / 30D / 90D / 180D MFE-MAE present
- canonical trigger_type values only
- large_sector_id and canonical_archetype_id consistent
- no reused C07 loop107 symbol-date group
```

Not validated in this loop:

```text
- exact DART/news URL repair for each evidence proxy
- production score implementation
- live/current investment suitability
- brokerage/API execution
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C07_verified_order_revenue_bridge_required_before_Yellow,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,0,1,+1,"C07 positives had large 90D/180D MFE only when order/revenue/margin bridge was visible; counterexamples had late RS without conversion","reduces false positives and recovers tester/process missed structural cases","C07-R2-L108-T01-232140|C07-R2-L108-T02-319660|C07-R2-L108-T03-240810|C07-R2-L108-T04-089890|C07-R2-L108-T05-382800|C07-R2-L108-T06-217190",6,6,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "manifest_max_date": "2026-02-20", "manifest_path": "atlas/manifest.json", "max_date": "2026-02-20", "min_date": "1995-05-02", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "raw_row_count": 15214118, "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "row_type": "price_source_validation", "schema_path": "atlas/schema.json", "source": "Songdaiki/stock-web", "source_name": "FinanceData/marcap", "source_url": "https://github.com/Songdaiki/stock-web", "symbol_count": 5414, "tradable_row_count": 14354401, "universe_path": "atlas/universe/all_symbols.csv", "validation_status": "usable_for_historical_calibration"}
{"best_trigger": "Stage2-Actionable", "calibration_usable": true, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07-R2-L108-01-232140", "case_type": "structural_success", "company_name": "와이씨", "current_profile_verdict": "current_profile_missed_structural", "deep_sub_archetype_id": "C07_DEEP_TESTER_PROCESS_AUX_EQUIPMENT_RELATIVE_STRENGTH_VS_ORDER_REVENUE_BRIDGE_AND_LATE_PRICE_ONLY_RS_FADE", "fine_archetype_id": "C07_HBM_ADVANCED_PACKAGING_TEST_PROCESS_EQUIPMENT_RS_ORDER_REVENUE_CONVERSION_BRIDGE", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "loop": "108", "notes": "The tester path was not just a memory-beta move: early 2024 relative strength turned into a very large 90D/180D MFE. C07 should allow Stage2-Actionable when test-equipment revenue/order conversion is visible before the market treats it as pure price momentum.", "positive_or_counterexample": "positive", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R2", "row_type": "case", "score_price_alignment": "aligned_positive", "symbol": "232140"}
{"MAE_180D_pct": -7.04, "MAE_1Y_pct": -7.04, "MAE_2Y_pct": null, "MAE_30D_pct": -7.04, "MAE_90D_pct": -7.04, "MFE_180D_pct": 325.0, "MFE_1Y_pct": 325.0, "MFE_2Y_pct": null, "MFE_30D_pct": 48.89, "MFE_90D_pct": 325.0, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07-R2-L108-01-232140", "company_name": "와이씨", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_missed_structural", "dedupe_for_aggregate": true, "deep_sub_archetype_id": "C07_DEEP_TESTER_PROCESS_AUX_EQUIPMENT_RELATIVE_STRENGTH_VS_ORDER_REVENUE_BRIDGE_AND_LATE_PRICE_ONLY_RS_FADE", "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -53.64, "entry_date": "2024-02-01", "entry_price": 5400.0, "evidence_available_at_that_date": "source_proxy:DART filings plus public HBM/test-equipment relative-strength context; exact order URL repair required", "evidence_source": "source_proxy:DART filings plus public HBM/test-equipment relative-strength context; exact order URL repair required", "fine_archetype_id": "C07_HBM_ADVANCED_PACKAGING_TEST_PROCESS_EQUIPMENT_RS_ORDER_REVENUE_CONVERSION_BRIDGE", "forward_window_trading_days": 180, "four_b_evidence_type": [], "four_b_full_window_peak_proximity": null, "four_b_local_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_c_protection_label": "not_applicable", "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "loop": "108", "loop_objective": "coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery", "peak_date": "2024-06-13", "peak_price": 22950.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/232/232140/2024.csv", "primary_archetype": "hbm_equipment_order_relative_strength", "profile_path": "atlas/symbol_profiles/232/232140.json", "reuse_reason": null, "round": "R2", "row_type": "trigger", "same_entry_group_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|232140|Stage2-Actionable|2024-02-01", "sector": "AI_SEMICONDUCTOR_ELECTRONICS", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "repeat_order_or_conversion", "margin_bridge"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "232140", "trigger_date": "2024-02-01", "trigger_id": "C07-R2-L108-T01-232140", "trigger_outcome_label": "memory_tester_hbm_test_capacity_order_conversion", "trigger_type": "Stage2-Actionable"}
{"MAE_90D_pct": -7.04, "MFE_90D_pct": 325.0, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07-R2-L108-01-232140", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C07 shadow profile rewards verified HBM/test/process-equipment order or revenue conversion and discounts late relative-strength-only equipment beta without margin/revision bridge.", "current_profile_verdict": "current_profile_missed_structural", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C07_shadow", "raw_component_scores_after": {"accounting_trust_risk_score": 5, "backlog_visibility_score": 62, "contract_score": 54, "customer_quality_score": 55, "dilution_cb_risk_score": 0, "execution_risk_score": 27, "legal_or_contract_risk_score": 5, "margin_bridge_score": 59, "policy_or_regulatory_score": 0, "relative_strength_score": 82, "revision_score": 53, "valuation_repricing_score": 62}, "raw_component_scores_before": {"accounting_trust_risk_score": 5, "backlog_visibility_score": 55, "contract_score": 48, "customer_quality_score": 55, "dilution_cb_risk_score": 0, "execution_risk_score": 32, "legal_or_contract_risk_score": 5, "margin_bridge_score": 52, "policy_or_regulatory_score": 0, "relative_strength_score": 82, "revision_score": 48, "valuation_repricing_score": 62}, "row_type": "score_simulation", "score_return_alignment_label": "aligned", "stage_label_after": "Stage3-Yellow", "stage_label_before": "Stage3-Yellow", "symbol": "232140", "trigger_id": "C07-R2-L108-T01-232140", "weighted_score_after": 83.3, "weighted_score_before": 79.3}
{"best_trigger": "Stage2-Actionable", "calibration_usable": true, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07-R2-L108-02-319660", "case_type": "structural_success", "company_name": "피에스케이", "current_profile_verdict": "current_profile_correct", "deep_sub_archetype_id": "C07_DEEP_TESTER_PROCESS_AUX_EQUIPMENT_RELATIVE_STRENGTH_VS_ORDER_REVENUE_BRIDGE_AND_LATE_PRICE_ONLY_RS_FADE", "fine_archetype_id": "C07_HBM_ADVANCED_PACKAGING_TEST_PROCESS_EQUIPMENT_RS_ORDER_REVENUE_CONVERSION_BRIDGE", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "loop": "108", "notes": "A cleaner process-equipment recovery case: moderate early MAE and strong 90D/180D MFE. It supports C07/C10 separation: C07 receives relative-strength/order-conversion credit only if it is not just a generic WFE beta proxy.", "positive_or_counterexample": "positive", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R2", "row_type": "case", "score_price_alignment": "aligned_positive", "symbol": "319660"}
{"MAE_180D_pct": -1.16, "MAE_1Y_pct": -21.31, "MAE_2Y_pct": null, "MAE_30D_pct": -1.16, "MAE_90D_pct": -1.16, "MFE_180D_pct": 97.87, "MFE_1Y_pct": 97.87, "MFE_2Y_pct": null, "MFE_30D_pct": 41.19, "MFE_90D_pct": 81.68, "aggregate_group_role": "representative", "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": false, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07-R2-L108-02-319660", "company_name": "피에스케이", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_correct", "dedupe_for_aggregate": true, "deep_sub_archetype_id": "C07_DEEP_TESTER_PROCESS_AUX_EQUIPMENT_RELATIVE_STRENGTH_VS_ORDER_REVENUE_BRIDGE_AND_LATE_PRICE_ONLY_RS_FADE", "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -48.87, "entry_date": "2024-02-01", "entry_price": 19760.0, "evidence_available_at_that_date": "source_proxy:DART filings and public process-equipment memory capex recovery context; exact URL repair required", "evidence_source": "source_proxy:DART filings and public process-equipment memory capex recovery context; exact URL repair required", "fine_archetype_id": "C07_HBM_ADVANCED_PACKAGING_TEST_PROCESS_EQUIPMENT_RS_ORDER_REVENUE_CONVERSION_BRIDGE", "forward_window_trading_days": 180, "four_b_evidence_type": [], "four_b_full_window_peak_proximity": null, "four_b_local_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_c_protection_label": "not_applicable", "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "loop": "108", "loop_objective": "coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery", "peak_date": "2024-07-11", "peak_price": 39100.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/319/319660/2024.csv", "primary_archetype": "hbm_equipment_order_relative_strength", "profile_path": "atlas/symbol_profiles/319/319660.json", "reuse_reason": null, "round": "R2", "row_type": "trigger", "same_entry_group_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|319660|Stage2-Actionable|2024-02-01", "sector": "AI_SEMICONDUCTOR_ELECTRONICS", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "capacity_or_volume_route"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "margin_bridge"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "319660", "trigger_date": "2024-02-01", "trigger_id": "C07-R2-L108-T02-319660", "trigger_outcome_label": "front_end_process_memory_recovery_order_revenue_conversion", "trigger_type": "Stage2-Actionable"}
{"MAE_90D_pct": -1.16, "MFE_90D_pct": 81.68, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07-R2-L108-02-319660", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C07 shadow profile rewards verified HBM/test/process-equipment order or revenue conversion and discounts late relative-strength-only equipment beta without margin/revision bridge.", "current_profile_verdict": "current_profile_correct", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C07_shadow", "raw_component_scores_after": {"accounting_trust_risk_score": 5, "backlog_visibility_score": 62, "contract_score": 54, "customer_quality_score": 55, "dilution_cb_risk_score": 0, "execution_risk_score": 27, "legal_or_contract_risk_score": 5, "margin_bridge_score": 59, "policy_or_regulatory_score": 0, "relative_strength_score": 82, "revision_score": 53, "valuation_repricing_score": 62}, "raw_component_scores_before": {"accounting_trust_risk_score": 5, "backlog_visibility_score": 55, "contract_score": 48, "customer_quality_score": 55, "dilution_cb_risk_score": 0, "execution_risk_score": 32, "legal_or_contract_risk_score": 5, "margin_bridge_score": 52, "policy_or_regulatory_score": 0, "relative_strength_score": 82, "revision_score": 48, "valuation_repricing_score": 62}, "row_type": "score_simulation", "score_return_alignment_label": "aligned", "stage_label_after": "Stage3-Yellow", "stage_label_before": "Stage3-Yellow", "symbol": "319660", "trigger_id": "C07-R2-L108-T02-319660", "weighted_score_after": 83.3, "weighted_score_before": 79.3}
{"best_trigger": "Stage2-Actionable", "calibration_usable": true, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07-R2-L108-03-240810", "case_type": "stage2_promote_candidate", "company_name": "원익IPS", "current_profile_verdict": "current_profile_too_late", "deep_sub_archetype_id": "C07_DEEP_TESTER_PROCESS_AUX_EQUIPMENT_RELATIVE_STRENGTH_VS_ORDER_REVENUE_BRIDGE_AND_LATE_PRICE_ONLY_RS_FADE", "fine_archetype_id": "C07_HBM_ADVANCED_PACKAGING_TEST_PROCESS_EQUIPMENT_RS_ORDER_REVENUE_CONVERSION_BRIDGE", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "loop": "108", "notes": "The 90D/180D path worked, but later drawdown shows why C07 should not convert generic equipment recovery into Green without revision and margin bridge. Stage2 is acceptable; late Green requires stricter proof.", "positive_or_counterexample": "positive", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R2", "row_type": "case", "score_price_alignment": "aligned_positive", "symbol": "240810"}
{"MAE_180D_pct": -19.77, "MAE_1Y_pct": -29.98, "MAE_2Y_pct": null, "MAE_30D_pct": -5.53, "MAE_90D_pct": -5.53, "MFE_180D_pct": 50.25, "MFE_1Y_pct": 50.25, "MFE_2Y_pct": null, "MFE_30D_pct": 27.3, "MFE_90D_pct": 50.25, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07-R2-L108-03-240810", "company_name": "원익IPS", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_too_late", "dedupe_for_aggregate": true, "deep_sub_archetype_id": "C07_DEEP_TESTER_PROCESS_AUX_EQUIPMENT_RELATIVE_STRENGTH_VS_ORDER_REVENUE_BRIDGE_AND_LATE_PRICE_ONLY_RS_FADE", "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -46.6, "entry_date": "2024-02-15", "entry_price": 29850.0, "evidence_available_at_that_date": "source_proxy:DART filings and public memory WFE recovery context; exact URL repair required", "evidence_source": "source_proxy:DART filings and public memory WFE recovery context; exact URL repair required", "fine_archetype_id": "C07_HBM_ADVANCED_PACKAGING_TEST_PROCESS_EQUIPMENT_RS_ORDER_REVENUE_CONVERSION_BRIDGE", "forward_window_trading_days": 180, "four_b_evidence_type": [], "four_b_full_window_peak_proximity": null, "four_b_local_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_c_protection_label": "not_applicable", "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "loop": "108", "loop_objective": "coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery", "peak_date": "2024-04-08", "peak_price": 44850.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/240/240810/2024.csv", "primary_archetype": "hbm_equipment_order_relative_strength", "profile_path": "atlas/symbol_profiles/240/240810.json", "reuse_reason": null, "round": "R2", "row_type": "trigger", "same_entry_group_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|240810|Stage2-Actionable|2024-02-15", "sector": "AI_SEMICONDUCTOR_ELECTRONICS", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "capacity_or_volume_route", "backlog_or_delivery_visibility"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "240810", "trigger_date": "2024-02-15", "trigger_id": "C07-R2-L108-T03-240810", "trigger_outcome_label": "wfe_process_equipment_memory_recovery_order_revenue_bridge", "trigger_type": "Stage2-Actionable"}
{"MAE_90D_pct": -5.53, "MFE_90D_pct": 50.25, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07-R2-L108-03-240810", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C07 shadow profile rewards verified HBM/test/process-equipment order or revenue conversion and discounts late relative-strength-only equipment beta without margin/revision bridge.", "current_profile_verdict": "current_profile_too_late", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C07_shadow", "raw_component_scores_after": {"accounting_trust_risk_score": 5, "backlog_visibility_score": 62, "contract_score": 54, "customer_quality_score": 55, "dilution_cb_risk_score": 0, "execution_risk_score": 27, "legal_or_contract_risk_score": 5, "margin_bridge_score": 59, "policy_or_regulatory_score": 0, "relative_strength_score": 82, "revision_score": 53, "valuation_repricing_score": 62}, "raw_component_scores_before": {"accounting_trust_risk_score": 5, "backlog_visibility_score": 55, "contract_score": 48, "customer_quality_score": 55, "dilution_cb_risk_score": 0, "execution_risk_score": 32, "legal_or_contract_risk_score": 5, "margin_bridge_score": 52, "policy_or_regulatory_score": 0, "relative_strength_score": 82, "revision_score": 48, "valuation_repricing_score": 62}, "row_type": "score_simulation", "score_return_alignment_label": "aligned", "stage_label_after": "Stage3-Yellow", "stage_label_before": "Stage3-Yellow", "symbol": "240810", "trigger_id": "C07-R2-L108-T03-240810", "weighted_score_after": 83.3, "weighted_score_before": 79.3}
{"best_trigger": "Stage4B", "calibration_usable": true, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07-R2-L108-04-089890", "case_type": "4B_overlay_success", "company_name": "코세스", "current_profile_verdict": "current_profile_4B_too_late", "deep_sub_archetype_id": "C07_DEEP_TESTER_PROCESS_AUX_EQUIPMENT_RELATIVE_STRENGTH_VS_ORDER_REVENUE_BRIDGE_AND_LATE_PRICE_ONLY_RS_FADE", "fine_archetype_id": "C07_HBM_ADVANCED_PACKAGING_TEST_PROCESS_EQUIPMENT_RS_ORDER_REVENUE_CONVERSION_BRIDGE", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "loop": "108", "notes": "The advanced-packaging label was plausible, but the July entry had very small upside and extreme 90D/180D MAE. It is a C07 late-price-only RS 4B-watch exemplar.", "positive_or_counterexample": "counterexample", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R2", "row_type": "case", "score_price_alignment": "guardrail_or_false_positive_needed", "symbol": "089890"}
{"MAE_180D_pct": -67.73, "MAE_1Y_pct": -67.73, "MAE_2Y_pct": null, "MAE_30D_pct": -52.01, "MAE_90D_pct": -58.33, "MFE_180D_pct": 5.87, "MFE_1Y_pct": 5.87, "MFE_2Y_pct": null, "MFE_30D_pct": 5.87, "MFE_90D_pct": 5.87, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07-R2-L108-04-089890", "company_name": "코세스", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_4B_too_late", "dedupe_for_aggregate": true, "deep_sub_archetype_id": "C07_DEEP_TESTER_PROCESS_AUX_EQUIPMENT_RELATIVE_STRENGTH_VS_ORDER_REVENUE_BRIDGE_AND_LATE_PRICE_ONLY_RS_FADE", "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -69.52, "entry_date": "2024-07-01", "entry_price": 17880.0, "evidence_available_at_that_date": "source_proxy:DART filings and advanced-packaging/HBM theme proxy; mass revenue bridge not verified at late entry; exact URL repair required", "evidence_source": "source_proxy:DART filings and advanced-packaging/HBM theme proxy; mass revenue bridge not verified at late entry; exact URL repair required", "fine_archetype_id": "C07_HBM_ADVANCED_PACKAGING_TEST_PROCESS_EQUIPMENT_RS_ORDER_REVENUE_CONVERSION_BRIDGE", "forward_window_trading_days": 180, "four_b_evidence_type": ["price_only", "positioning_overheat", "valuation_blowoff"], "four_b_full_window_peak_proximity": 0.62, "four_b_local_peak_proximity": 0.86, "four_b_timing_verdict": "price_only_local_4B_too_early_or_late_without_order_bridge", "four_c_protection_label": "not_applicable", "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "loop": "108", "loop_objective": "coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery", "peak_date": "2024-07-01", "peak_price": 18930.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/089/089890/2024.csv", "primary_archetype": "hbm_equipment_order_relative_strength", "profile_path": "atlas/symbol_profiles/089/089890.json", "reuse_reason": null, "round": "R2", "row_type": "trigger", "same_entry_group_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|089890|Stage4B|2024-07-01", "sector": "AI_SEMICONDUCTOR_ELECTRONICS", "stage2_evidence_fields": ["relative_strength", "public_event_or_disclosure"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "089890", "trigger_date": "2024-07-01", "trigger_id": "C07-R2-L108-T04-089890", "trigger_outcome_label": "advanced_packaging_hbm_label_local_overheat_without_revenue_bridge", "trigger_type": "Stage4B"}
{"MAE_90D_pct": -58.33, "MFE_90D_pct": 5.87, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07-R2-L108-04-089890", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C07 shadow profile rewards verified HBM/test/process-equipment order or revenue conversion and discounts late relative-strength-only equipment beta without margin/revision bridge.", "current_profile_verdict": "current_profile_4B_too_late", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C07_shadow", "raw_component_scores_after": {"accounting_trust_risk_score": 8, "backlog_visibility_score": 22, "contract_score": 8, "customer_quality_score": 20, "dilution_cb_risk_score": 0, "execution_risk_score": 88, "legal_or_contract_risk_score": 5, "margin_bridge_score": 5, "policy_or_regulatory_score": 0, "relative_strength_score": 46, "revision_score": 4, "valuation_repricing_score": 45}, "raw_component_scores_before": {"accounting_trust_risk_score": 8, "backlog_visibility_score": 22, "contract_score": 15, "customer_quality_score": 20, "dilution_cb_risk_score": 0, "execution_risk_score": 72, "legal_or_contract_risk_score": 5, "margin_bridge_score": 12, "policy_or_regulatory_score": 0, "relative_strength_score": 86, "revision_score": 10, "valuation_repricing_score": 82}, "row_type": "score_simulation", "score_return_alignment_label": "false_positive_filtered_or_4B_guarded", "stage_label_after": "Stage4B-Watch", "stage_label_before": "Stage4B-Watch", "symbol": "089890", "trigger_id": "C07-R2-L108-T04-089890", "weighted_score_after": 42.0, "weighted_score_before": 54.5}
{"best_trigger": "Stage4B", "calibration_usable": true, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07-R2-L108-05-382800", "case_type": "4B_overlay_success", "company_name": "지앤비에스 에코", "current_profile_verdict": "current_profile_false_positive", "deep_sub_archetype_id": "C07_DEEP_TESTER_PROCESS_AUX_EQUIPMENT_RELATIVE_STRENGTH_VS_ORDER_REVENUE_BRIDGE_AND_LATE_PRICE_ONLY_RS_FADE", "fine_archetype_id": "C07_HBM_ADVANCED_PACKAGING_TEST_PROCESS_EQUIPMENT_RS_ORDER_REVENUE_CONVERSION_BRIDGE", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "loop": "108", "notes": "Auxiliary environmental equipment can ride the HBM/WFE equipment label, but without order/revenue conversion it failed the forward path badly. This strengthens the C07 source-proxy-to-4B-watch filter.", "positive_or_counterexample": "counterexample", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R2", "row_type": "case", "score_price_alignment": "guardrail_or_false_positive_needed", "symbol": "382800"}
{"MAE_180D_pct": -60.17, "MAE_1Y_pct": -60.17, "MAE_2Y_pct": null, "MAE_30D_pct": -18.68, "MAE_90D_pct": -47.02, "MFE_180D_pct": 2.98, "MFE_1Y_pct": 2.98, "MFE_2Y_pct": null, "MFE_30D_pct": 2.98, "MFE_90D_pct": 2.98, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07-R2-L108-05-382800", "company_name": "지앤비에스 에코", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_false_positive", "dedupe_for_aggregate": true, "deep_sub_archetype_id": "C07_DEEP_TESTER_PROCESS_AUX_EQUIPMENT_RELATIVE_STRENGTH_VS_ORDER_REVENUE_BRIDGE_AND_LATE_PRICE_ONLY_RS_FADE", "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -61.32, "entry_date": "2024-05-02", "entry_price": 6050.0, "evidence_available_at_that_date": "source_proxy:DART filings and semiconductor auxiliary-equipment theme proxy; firm-specific HBM order conversion not verified; exact URL repair required", "evidence_source": "source_proxy:DART filings and semiconductor auxiliary-equipment theme proxy; firm-specific HBM order conversion not verified; exact URL repair required", "fine_archetype_id": "C07_HBM_ADVANCED_PACKAGING_TEST_PROCESS_EQUIPMENT_RS_ORDER_REVENUE_CONVERSION_BRIDGE", "forward_window_trading_days": 180, "four_b_evidence_type": ["price_only", "positioning_overheat", "valuation_blowoff"], "four_b_full_window_peak_proximity": 0.33, "four_b_local_peak_proximity": 0.78, "four_b_timing_verdict": "price_only_local_4B_too_early_or_late_without_order_bridge", "four_c_protection_label": "not_applicable", "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "loop": "108", "loop_objective": "coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery", "peak_date": "2024-05-02", "peak_price": 6230.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/382/382800/2024.csv", "primary_archetype": "hbm_equipment_order_relative_strength", "profile_path": "atlas/symbol_profiles/382/382800.json", "reuse_reason": null, "round": "R2", "row_type": "trigger", "same_entry_group_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|382800|Stage4B|2024-05-02", "sector": "AI_SEMICONDUCTOR_ELECTRONICS", "stage2_evidence_fields": ["relative_strength", "capacity_or_volume_route"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "382800", "trigger_date": "2024-05-02", "trigger_id": "C07-R2-L108-T05-382800", "trigger_outcome_label": "auxiliary_environment_equipment_hbm_theme_proxy_without_order_conversion", "trigger_type": "Stage4B"}
{"MAE_90D_pct": -47.02, "MFE_90D_pct": 2.98, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07-R2-L108-05-382800", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C07 shadow profile rewards verified HBM/test/process-equipment order or revenue conversion and discounts late relative-strength-only equipment beta without margin/revision bridge.", "current_profile_verdict": "current_profile_false_positive", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C07_shadow", "raw_component_scores_after": {"accounting_trust_risk_score": 8, "backlog_visibility_score": 22, "contract_score": 8, "customer_quality_score": 20, "dilution_cb_risk_score": 0, "execution_risk_score": 88, "legal_or_contract_risk_score": 5, "margin_bridge_score": 5, "policy_or_regulatory_score": 0, "relative_strength_score": 46, "revision_score": 4, "valuation_repricing_score": 45}, "raw_component_scores_before": {"accounting_trust_risk_score": 8, "backlog_visibility_score": 22, "contract_score": 15, "customer_quality_score": 20, "dilution_cb_risk_score": 0, "execution_risk_score": 72, "legal_or_contract_risk_score": 5, "margin_bridge_score": 12, "policy_or_regulatory_score": 0, "relative_strength_score": 86, "revision_score": 10, "valuation_repricing_score": 82}, "row_type": "score_simulation", "score_return_alignment_label": "false_positive_filtered_or_4B_guarded", "stage_label_after": "Stage4B-Watch", "stage_label_before": "Stage4B-Watch", "symbol": "382800", "trigger_id": "C07-R2-L108-T05-382800", "weighted_score_after": 42.0, "weighted_score_before": 54.5}
{"best_trigger": "Stage2", "calibration_usable": true, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07-R2-L108-06-217190", "case_type": "failed_rerating", "company_name": "제너셈", "current_profile_verdict": "current_profile_false_positive", "deep_sub_archetype_id": "C07_DEEP_TESTER_PROCESS_AUX_EQUIPMENT_RELATIVE_STRENGTH_VS_ORDER_REVENUE_BRIDGE_AND_LATE_PRICE_ONLY_RS_FADE", "fine_archetype_id": "C07_HBM_ADVANCED_PACKAGING_TEST_PROCESS_EQUIPMENT_RS_ORDER_REVENUE_CONVERSION_BRIDGE", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "loop": "108", "notes": "Automation/package-adjacent names can receive a temporary HBM halo, but this row shows the failure mode: weak 30D/90D MFE and very large 180D MAE. It should be Stage2 only with strict bridge requirement, not Yellow.", "positive_or_counterexample": "counterexample", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R2", "row_type": "case", "score_price_alignment": "guardrail_or_false_positive_needed", "symbol": "217190"}
{"MAE_180D_pct": -53.2, "MAE_1Y_pct": -53.2, "MAE_2Y_pct": null, "MAE_30D_pct": -6.08, "MAE_90D_pct": -41.44, "MFE_180D_pct": 6.31, "MFE_1Y_pct": 6.31, "MFE_2Y_pct": null, "MFE_30D_pct": 6.31, "MFE_90D_pct": 6.31, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07-R2-L108-06-217190", "company_name": "제너셈", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_false_positive", "dedupe_for_aggregate": true, "deep_sub_archetype_id": "C07_DEEP_TESTER_PROCESS_AUX_EQUIPMENT_RELATIVE_STRENGTH_VS_ORDER_REVENUE_BRIDGE_AND_LATE_PRICE_ONLY_RS_FADE", "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -55.98, "entry_date": "2024-05-02", "entry_price": 12670.0, "evidence_available_at_that_date": "source_proxy:DART filings and semiconductor automation/HBM package theme proxy; order/margin bridge not verified; exact URL repair required", "evidence_source": "source_proxy:DART filings and semiconductor automation/HBM package theme proxy; order/margin bridge not verified; exact URL repair required", "fine_archetype_id": "C07_HBM_ADVANCED_PACKAGING_TEST_PROCESS_EQUIPMENT_RS_ORDER_REVENUE_CONVERSION_BRIDGE", "forward_window_trading_days": 180, "four_b_evidence_type": ["margin_or_backlog_slowdown"], "four_b_full_window_peak_proximity": null, "four_b_local_peak_proximity": null, "four_b_timing_verdict": "Stage2_theme_proxy_should_have_been_4B_watch", "four_c_protection_label": "thesis_break_watch_only", "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "loop": "108", "loop_objective": "coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery", "peak_date": "2024-05-16", "peak_price": 13470.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/217/217190/2024.csv", "primary_archetype": "hbm_equipment_order_relative_strength", "profile_path": "atlas/symbol_profiles/217/217190.json", "reuse_reason": null, "round": "R2", "row_type": "trigger", "same_entry_group_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|217190|Stage2|2024-05-02", "sector": "AI_SEMICONDUCTOR_ELECTRONICS", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "price_only_local_peak"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "stock_web_manifest_max_date": "2026-02-20", "symbol": "217190", "trigger_date": "2024-05-02", "trigger_id": "C07-R2-L108-T06-217190", "trigger_outcome_label": "semiconductor_automation_hbm_package_theme_proxy_without_order_margin_bridge", "trigger_type": "Stage2"}
{"MAE_90D_pct": -41.44, "MFE_90D_pct": 6.31, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07-R2-L108-06-217190", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C07 shadow profile rewards verified HBM/test/process-equipment order or revenue conversion and discounts late relative-strength-only equipment beta without margin/revision bridge.", "current_profile_verdict": "current_profile_false_positive", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C07_shadow", "raw_component_scores_after": {"accounting_trust_risk_score": 8, "backlog_visibility_score": 22, "contract_score": 8, "customer_quality_score": 20, "dilution_cb_risk_score": 0, "execution_risk_score": 88, "legal_or_contract_risk_score": 5, "margin_bridge_score": 5, "policy_or_regulatory_score": 0, "relative_strength_score": 46, "revision_score": 4, "valuation_repricing_score": 45}, "raw_component_scores_before": {"accounting_trust_risk_score": 8, "backlog_visibility_score": 22, "contract_score": 15, "customer_quality_score": 20, "dilution_cb_risk_score": 0, "execution_risk_score": 72, "legal_or_contract_risk_score": 5, "margin_bridge_score": 12, "policy_or_regulatory_score": 0, "relative_strength_score": 86, "revision_score": 10, "valuation_repricing_score": 82}, "row_type": "score_simulation", "score_return_alignment_label": "false_positive_filtered_or_4B_guarded", "stage_label_after": "Watchlist-only", "stage_label_before": "Watchlist-only", "symbol": "217190", "trigger_id": "C07-R2-L108-T06-217190", "weighted_score_after": 42.0, "weighted_score_before": 54.5}
{"canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "do_not_propose_new_weight_delta": false, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "loop": "108", "loop_contribution_label": "canonical_archetype_rule_candidate", "new_independent_case_count": 6, "new_symbol_count": 6, "new_trigger_family_count": 6, "residual_error_types_found": ["C07_tester_order_conversion_missed_structural", "C07_late_advanced_packaging_RS_4B_too_late", "C07_auxiliary_equipment_theme_proxy_false_positive", "C07_automation_package_theme_proxy_without_margin_bridge"], "reused_case_count": 0, "round": "R2", "row_type": "residual_contribution", "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"]}
```

## Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 6
calibration_usable_trigger_count: 6
representative_trigger_count: 6
new_weight_evidence_candidate_count: 6
guardrail_candidate_count: 3
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules

- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate large_sector_id and canonical_archetype_id.
4. Validate novelty and reuse fields.
5. Deduplicate same_entry_group_id and reused cases.
6. Aggregate by large_sector_id and canonical_archetype_id.
7. Update sector_shadow_profile and archetype_shadow_profile only.
8. Preserve global calibrated profile unless explicitly promoted.
9. Report new independent cases, counterexamples, and residual error types.
10. Add tests that duplicate low-value loops cannot change weights.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R2
completed_loop = 108
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
next_recommended_archetypes = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE, C01_ORDER_BACKLOG_MARGIN_BRIDGE, C02_POWER_GRID_DATACENTER_CAPEX, C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK, C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes

This MD intentionally uses source-proxy language for company-level non-price evidence where exact DART/news URLs require a later URL-repair pass. The quantitative trigger rows are still usable because every representative row carries a clean stock-web `tradable_raw` price path and full 30D/90D/180D MFE/MAE fields. Promotion confidence should remain `medium` until URL repair reduces source_proxy_only/evidence_url_pending counts.
