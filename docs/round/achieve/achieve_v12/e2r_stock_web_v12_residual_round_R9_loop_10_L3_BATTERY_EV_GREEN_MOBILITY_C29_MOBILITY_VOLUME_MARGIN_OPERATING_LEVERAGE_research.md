# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R9
loop = 10
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id = OEM_VOLUME_MIX_MARGIN_BRIDGE_VS_COMPONENT_SUPPLIER_COST_PASS_THROUGH_GAP
output_file = e2r_stock_web_v12_residual_round_R9_loop_10_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This file is historical calibration research only. It is not a live watchlist, not a current-stock discovery file, not a brokerage/API workflow, and not a code patch.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

The research does not re-propose these global axes. It stress-tests them inside C29 and proposes shadow-only sector/canonical-archetype refinements.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R9
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
loop_objective = residual_false_positive_mining
loop_objective += residual_missed_structural_mining
loop_objective += sector_specific_rule_discovery
loop_objective += canonical_archetype_compression
loop_objective += 4B_non_price_requirement_stress_test
loop_objective += coverage_gap_fill
```

C29 should not score "vehicle shipments up" as a standalone rerating signal. The economic mechanism is:

```text
volume recovery
→ utilization / fixed-cost absorption
→ ASP or mix protection
→ input-cost/pass-through discipline
→ OP/EPS revision
→ rerating
```

The residual found in this loop is that the current proxy can over-credit component suppliers when OEM volume recovers but price-cost pass-through and margin conversion are not confirmed.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifacts show `docs/round` already covered R1~R13 and loops 1~9 with 398 MDs, 1,940 validated trigger rows, and 1,376 aggregate representative rows. This loop therefore uses loop 10 and five new independent C29 cases not reused from this session.

Already-applied global axes are treated as existing baselines, not new findings. The new contribution is the C29-specific split between:

```text
OEM volume + mix/ASP + margin bridge = positive C29
component supplier volume + cost/pass-through gap = capped C29
price-only local peak = 4B watch, not full 4B
```

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

Manifest-confirmed context:

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

## 5. Historical Eligibility Gate

All representative triggers satisfy:

```text
trigger_date is historical
entry_date exists in stock-web tradable shard
entry_date has at least 180 forward tradable rows before manifest max_date
OHLCV fields are positive and present
MFE/MAE 30D, 90D, 180D are computed from tradable_raw rows
corporate_action_window_status = clean_180D_window
```

Corporate action profile notes:

```text
005380 corporate_action_candidate_dates: 1998-12-02, 1999-04-15, 1999-06-11, 1999-08-16, 1999-12-24
000270 corporate_action_candidate_dates: 1999-03-05, 1999-04-21, 1999-07-16
204320 corporate_action_candidate_dates: 2018-05-08
011210 corporate_action_candidate_dates: none
018880 corporate_action_candidate_dates: 2004-05-12, 2016-02-16, 2025-01-09, 2026-01-12
```

No representative 180D window overlaps a candidate corporate action date.

## 6. Canonical Archetype Compression Map

| fine_archetype | canonical_archetype_id | compression rule |
|---|---|---|
| OEM_VOLUME_MIX_MARGIN_BRIDGE | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | OEM shipments count only when linked to ASP/mix and OP/EPS revision. |
| COMPONENT_SUPPLIER_VOLUME_COST_PASS_THROUGH_GAP | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | Supplier volume/customer quality is capped without pass-through and margin bridge. |
| MOBILITY_THEME_VOLUME_OPTIONALITY_HIGH_MAE | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | Theme/local spikes are not clean positive calibration if MAE is large. |
| PRICE_ONLY_LOCAL_4B_WATCH | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | Price-only peak is 4B watch; full 4B requires non-price evidence. |

## 7. Case Selection Summary

|case_id|symbol|company|role|pos/counter|best_trigger|verdict|
|---|---|---|---|---|---|---|
|R9L10_C29_005380_2023_VOLUME_MIX_MARGIN_SUCCESS|005380|현대차|structural_success|positive|TR_R9L10_005380_S2_20230126|current_profile_correct|
|R9L10_C29_000270_2023_VOLUME_MIX_MARGIN_SUCCESS|000270|기아|structural_success|positive|TR_R9L10_000270_S2_20230127|current_profile_correct|
|R9L10_C29_204320_2023_VOLUME_WITH_MARGIN_GAP|204320|HL만도|failed_rerating|counterexample|TR_R9L10_204320_S2_20230210|current_profile_false_positive|
|R9L10_C29_011210_2023_HIGH_MAE_VOLUME_OPTIONALITY|011210|현대위아|high_mae_success|counterexample|TR_R9L10_011210_S2_20230411|current_profile_too_early|
|R9L10_C29_018880_2023_THERMAL_VOLUME_MARGIN_GAP|018880|한온시스템|false_positive_green|counterexample|TR_R9L10_018880_S2_20230412|current_profile_false_positive|

## 8. Positive vs Counterexample Balance

```text
positive_structural_success = 2
counterexample_or_failed_rerating = 3
4B_or_4C_case = 1
minimum_calibration_usable_case_count = 5
new_independent_case_ratio = 5 / 5 = 1.00
```

Positive cases are OEMs where volume, mix, ASP/pricing and margin moved together. Counterexamples are suppliers/options where customer exposure or mobility volume narrative existed but margin pass-through was weak, producing high MAE or failed rerating.

## 9. Evidence Source Map

| symbol | evidence family | Stage2 evidence | Stage3 evidence | Red-team evidence |
|---|---|---|---|---|
| 005380 | OEM volume/mix/margin | shipment recovery, mix, early revision | Q1 margin confirmation | low red-team risk |
| 000270 | OEM volume/mix/margin | shipment recovery, mix, early revision | Q1 margin confirmation | price-only 4B watch |
| 204320 | component customer/ADAS volume | customer quality, auto volume | insufficient margin bridge | supplier pass-through gap |
| 011210 | group volume / EV optionality | relative strength, optionality | no durable margin bridge | high MAE |
| 018880 | EV thermal customer volume | customer quality, EV exposure | insufficient margin bridge | cost/restructuring burden |

## 10. Price Data Source Map

| symbol | profile_path | representative price_shard_path |
|---|---|---|
| 005380 | atlas/symbol_profiles/005/005380.json | atlas/ohlcv_tradable_by_symbol_year/005/005380/2023.csv |
| 000270 | atlas/symbol_profiles/000/000270.json | atlas/ohlcv_tradable_by_symbol_year/000/000270/2023.csv |
| 204320 | atlas/symbol_profiles/204/204320.json | atlas/ohlcv_tradable_by_symbol_year/204/204320/2023.csv |
| 011210 | atlas/symbol_profiles/011/011210.json | atlas/ohlcv_tradable_by_symbol_year/011/011210/2023.csv |
| 018880 | atlas/symbol_profiles/018/018880.json | atlas/ohlcv_tradable_by_symbol_year/018/018880/2023.csv |

## 11. Case-by-Case Trigger Grid

|trigger_id|symbol|type|trigger_date|entry|MFE90|MAE90|MFE180|MAE180|outcome|P0|agg|
|---|---|---|---|---|---|---|---|---|---|---|---|
|TR_R9L10_005380_S2_20230126|005380|Stage2-Actionable|2023-01-26|2023-01-27 / 173900|21.62|-3.97|21.62|-3.97|structural_success|current_profile_correct|representative|
|TR_R9L10_005380_GREEN_20230425|005380|Stage3-Green|2023-04-25|2023-04-26 / 201500|4.96|-4.52|4.96|-4.52|late_green_comparison|current_profile_too_late|label_comparison_only|
|TR_R9L10_000270_S2_20230127|000270|Stage2-Actionable|2023-01-27|2023-01-30 / 68600|33.97|-2.62|33.97|-2.62|structural_success|current_profile_correct|representative|
|TR_R9L10_000270_GREEN_20230425|000270|Stage3-Green|2023-04-25|2023-04-26 / 85700|7.23|-5.72|7.23|-5.72|late_green_comparison|current_profile_too_late|label_comparison_only|
|TR_R9L10_000270_4B_PRICE_LOCAL_20230511|000270|Stage4B-price-local-only|2023-05-11|2023-05-11 / 90100|1.99|-10.21|1.99|-10.21|4B_overlay_success_as_watch_only|current_profile_correct|4B_overlay_only|
|TR_R9L10_204320_S2_20230210|204320|Stage2-Actionable-false-positive|2023-02-10|2023-02-10 / 47600|9.03|-7.56|14.5|-7.56|failed_rerating|current_profile_false_positive|representative|
|TR_R9L10_011210_S2_20230411|011210|Stage2-Actionable-high-MAE|2023-04-11|2023-04-11 / 64400|9.47|-13.82|9.47|-13.82|high_mae_success_not_clean_positive|current_profile_too_early|representative|
|TR_R9L10_018880_S2_20230412|018880|Stage2-Actionable-false-positive|2023-04-12|2023-04-12 / 9170|10.91|-11.56|10.91|-11.56|false_positive_green_candidate|current_profile_false_positive|representative|

## 12. Trigger-Level OHLC Backtest Tables

### Representative triggers

|trigger_id|symbol|type|entry|MFE90|MAE90|MFE180|MAE180|outcome|P0|
|---|---|---|---|---|---|---|---|---|---|
|TR_R9L10_005380_S2_20230126|005380|Stage2-Actionable|2023-01-27 / 173900|21.62|-3.97|21.62|-3.97|structural_success|current_profile_correct|
|TR_R9L10_000270_S2_20230127|000270|Stage2-Actionable|2023-01-30 / 68600|33.97|-2.62|33.97|-2.62|structural_success|current_profile_correct|
|TR_R9L10_204320_S2_20230210|204320|Stage2-Actionable-false-positive|2023-02-10 / 47600|9.03|-7.56|14.5|-7.56|failed_rerating|current_profile_false_positive|
|TR_R9L10_011210_S2_20230411|011210|Stage2-Actionable-high-MAE|2023-04-11 / 64400|9.47|-13.82|9.47|-13.82|high_mae_success_not_clean_positive|current_profile_too_early|
|TR_R9L10_018880_S2_20230412|018880|Stage2-Actionable-false-positive|2023-04-12 / 9170|10.91|-11.56|10.91|-11.56|false_positive_green_candidate|current_profile_false_positive|

Aggregate representative result:

```text
representative_trigger_count = 5
avg_MFE_90D_pct = 17.0
avg_MAE_90D_pct = -7.91
avg_MFE_180D_pct = 18.09
avg_MAE_180D_pct = -7.91
false_positive_like_representatives = 3 / 5
clean_positive_representatives = 2 / 5
```

## 13. Current Calibrated Profile Stress Test

1. P0 correctly recognizes OEM Stage2-Actionable evidence for 005380 and 000270.
2. P0 is still too broad for 204320 and 018880 when it credits volume/customer exposure without a pass-through margin bridge.
3. P0 is too early for 011210 if the move is scored as a clean positive rather than high-MAE optionality.
4. The existing Stage2 bonus is useful for OEM positives but needs a C29 margin-conversion gate.
5. Yellow threshold 75 is acceptable if supplier names are capped before Yellow.
6. Green threshold 87 / revision 55 is directionally right but should require C29-specific margin evidence rather than generic revenue/customer evidence.
7. Price-only blowoff guard remains correct.
8. Full 4B non-price requirement remains correct and should be specialized: C29 full 4B needs revision slowdown, margin slowdown, backlog/order slowdown, or policy/legal cap.

## 14. Stage2 / Yellow / Green Comparison

| pair | Stage2 entry | Stage3 entry | peak after Stage2 | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---:|---|
| 005380 | 173900 | 201500 | 211500 | 0.73 | Green captured confirmation but missed most upside from Stage2. |
| 000270 | 68600 | 85700 | 91900 | 0.73 | Green was late versus Stage2-Actionable. |
| 204320 | 47600 | no confirmed Green | 54500 | not_applicable | Supplier volume lacked clean Green evidence. |
| 011210 | 64400 | no confirmed Green | 70500 | not_applicable | Optionality spike; high MAE prevents clean promotion. |
| 018880 | 9170 | no confirmed Green | 10170 | not_applicable | EV thermal/customer route lacked durable margin conversion. |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | four_b_evidence_type | local proximity | full-window proximity | verdict |
|---|---|---:|---:|---|
| TR_R9L10_000270_4B_PRICE_LOCAL_20230511 | price_only | 0.92 | 0.92 | price-only local peak is watch-only, not full 4B |
| TR_R9L10_011210_S2_20230411 | price_only | 0.47 | 0.47 | price-only local 4B too early |
| TR_R9L10_204320_S2_20230210 | margin_or_backlog_slowdown | n/a | n/a | supplier margin slowdown belongs to risk guard, not positive entry |
| TR_R9L10_018880_S2_20230412 | margin_or_backlog_slowdown | n/a | n/a | risk guard / 4C-watch |

## 16. 4C Protection Audit

Exact 4C protection score is not computed because these cases are primarily entry-gate and 4B-watch calibration. Labels:

```text
005380 = not_applicable
000270 = not_applicable
204320 = thesis_break_watch_only
011210 = thesis_break_watch_only
018880 = hard_4c_late
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = mobility_volume_margin_bridge_required
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
candidate = true
```

Rule: in L3 mobility names, volume recovery should promote Stage2/Yellow only if at least one of the following is present:

```text
1. OEM mix/ASP/pricing evidence
2. confirmed operating-margin bridge
3. EPS/OP revision from volume + margin, not volume alone
4. supplier pass-through evidence for input cost / FX / freight / labor
```

Without one of these, customer exposure and shipment growth remain watchlist evidence, not positive rerating evidence.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
candidate = true
```

Proposed C29 compression:

```text
C29_positive = volume_route + margin_bridge + revision_or_low_red_team
C29_watch = volume_route + customer_quality - margin_bridge
C29_guard = supplier_volume + cost_pass_through_gap
C29_4B_full = price strength + non_price_slowdown_evidence
```

## 19. Before / After Backtest Comparison

|profile_id|scope|eligible_trigger_count|avg_MFE_90D_pct|avg_MAE_90D_pct|false_positive_rate|late_green_count|verdict|
|---|---|---|---|---|---|---|---|
|P0 e2r_2_1_stock_web_calibrated_proxy|current global proxy|5|17.0|-7.91|3/5|2|too broad for component-supplier volume cases|
|P0b e2r_2_0_baseline_reference|rollback reference|5|17.0|-7.91|3/5|2|less explicit about 4B and component pass-through; weaker than P0|
|P1 sector_specific_candidate_profile|L3 mobility|5|17.0|-7.91|1/5|1|improves by requiring volume-to-margin bridge|
|P2 canonical_archetype_candidate_profile|C29|5|17.0|-7.91|0-1/5|1|best explanatory compression|
|P3 counterexample_guard_profile|component supplier guard|3|9.8|-10.98|0/3 after guard|0|caps supplier volume without pass-through|

## 20. Score-Return Alignment Matrix

| symbol | P0 score issue | observed return path | proposed alignment |
|---|---|---|---|
| 005380 | OK but Green late | clean MFE with low MAE | promote Stage2/Yellow earlier when volume + margin bridge exist |
| 000270 | OK but Green late | clean MFE with low MAE | same as 005380 |
| 204320 | overpromoted volume/customer quality | modest MFE, repeated drawdown | cap supplier without pass-through |
| 011210 | overpromoted optionality | high MAE, unstable follow-through | high-MAE theme optionality guard |
| 018880 | overpromoted EV/customer exposure | failed durable rerating | require cost/pass-through margin evidence |

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|L3_BATTERY_EV_GREEN_MOBILITY|C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|OEM_VOLUME_MIX_MARGIN_BRIDGE_VS_COMPONENT_SUPPLIER_COST_PASS_THROUGH_GAP|2|3|1|1|5|0|8|5|3|True|True|C29 now has OEM positive vs supplier margin-gap counterexample balance; still needs non-Korea OEM holdout if later added.|

## 22. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - component_supplier_volume_false_positive
  - high_mae_theme_volume_optionality
  - green_late_after_oem_margin_bridge
new_axis_proposed:
  - c29_volume_to_margin_bridge_required
  - c29_component_supplier_cost_pass_through_guard
  - c29_4b_requires_revision_or_margin_slowdown
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence
  - price_only_blowoff_blocks_positive_stage
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- actual stock-web tradable_raw OHLC rows
- 30D / 90D / 180D MFE and MAE for representative triggers
- clean 180D corporate-action window using profile candidate dates
- C29 positive/counterexample balance
- current calibrated profile stress test
```

Not validated:

```text
- live/current C29 candidates
- investment recommendation
- production code behavior
- exact production scoring internals
- brokerage execution
- non-stock-web adjusted-price reruns
```

## 24. Shadow Weight Calibration

### CSV rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c29_volume_to_margin_bridge_required,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1 gate,"OEM volume recovery only became clean positive when paired with ASP/mix/operating-margin bridge; supplier volume without pass-through created false positives.","Separates 005380/000270 clean positives from 204320/018880 margin-gap cases.",TR_R9L10_005380_S2_20230126|TR_R9L10_000270_S2_20230127|TR_R9L10_204320_S2_20230210|TR_R9L10_018880_S2_20230412,5,5,3,medium,canonical_archetype_shadow_only,"not production; post-calibrated residual"
shadow_weight,c29_component_supplier_cost_pass_through_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1 guard,"HL만도/한온시스템 show that customer volume and EV exposure are insufficient without margin pass-through or confirmed revision.","Reduces false positive Green/Stage2 promotion in component names with input-cost or restructuring drag.",TR_R9L10_204320_S2_20230210|TR_R9L10_018880_S2_20230412,2,2,2,medium,canonical_archetype_shadow_only,"not production; post-calibrated residual"
shadow_weight,c29_4b_requires_revision_or_margin_slowdown,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,full_4b_requires_non_price_evidence,margin/revision slowdown subtype,subtype guard,"Price-only local peak in Kia should be a watch overlay, not full 4B, unless revision/margin/order slowdown appears.","Strengthens existing full_4b_requires_non_price_evidence specifically for C29 mobility names.",TR_R9L10_000270_4B_PRICE_LOCAL_20230511,1,1,0,low,archetype_shadow_only,"not production; overlay calibration only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"case_id":"R9L10_C29_005380_2023_VOLUME_MIX_MARGIN_SUCCESS","symbol":"005380","company_name":"현대차","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TR_R9L10_005380_S2_20230126","score_price_alignment":"Stage2-Actionable captured most of the OEM volume/mix margin bridge before later Green confirmation.","current_profile_verdict":"current_profile_correct","notes":"OEM-level volume recovery was accompanied by pricing/mix, FX and operating margin expansion; supplier-style pure volume gates would understate the evidence quality.","row_type":"case","round":"R9","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"OEM_VOLUME_MIX_MARGIN_BRIDGE_VS_COMPONENT_SUPPLIER_COST_PASS_THROUGH_GAP","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"price_source":"Songdaiki/stock-web"}
{"case_id":"R9L10_C29_000270_2023_VOLUME_MIX_MARGIN_SUCCESS","symbol":"000270","company_name":"기아","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TR_R9L10_000270_S2_20230127","score_price_alignment":"Stage2-Actionable worked because volume recovery was tied to ASP/mix and operating leverage rather than unit shipment alone.","current_profile_verdict":"current_profile_correct","notes":"Positive C29 exemplar: shipment normalization plus mix/ASP and low red-team risk before Green.","row_type":"case","round":"R9","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"OEM_VOLUME_MIX_MARGIN_BRIDGE_VS_COMPONENT_SUPPLIER_COST_PASS_THROUGH_GAP","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"price_source":"Songdaiki/stock-web"}
{"case_id":"R9L10_C29_204320_2023_VOLUME_WITH_MARGIN_GAP","symbol":"204320","company_name":"HL만도","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TR_R9L10_204320_S2_20230210","score_price_alignment":"Volume/customer route alone produced only modest upside with repeated drawdown; margin conversion evidence was insufficient.","current_profile_verdict":"current_profile_false_positive","notes":"Component supplier volume exposure needs pass-through/margin bridge; OEM demand does not mechanically become supplier EPS rerating.","row_type":"case","round":"R9","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"OEM_VOLUME_MIX_MARGIN_BRIDGE_VS_COMPONENT_SUPPLIER_COST_PASS_THROUGH_GAP","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"price_source":"Songdaiki/stock-web"}
{"case_id":"R9L10_C29_011210_2023_HIGH_MAE_VOLUME_OPTIONALITY","symbol":"011210","company_name":"현대위아","case_type":"high_mae_success","positive_or_counterexample":"counterexample","best_trigger":"TR_R9L10_011210_S2_20230411","score_price_alignment":"Theme/volume optionality produced a large local spike, but without durable margin conversion it suffered high MAE and unstable follow-through.","current_profile_verdict":"current_profile_too_early","notes":"This is a C29 residual: high return windows can still be bad calibration positives if MAE is large and evidence is theme/capacity-optionality rather than realized margin.","row_type":"case","round":"R9","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"OEM_VOLUME_MIX_MARGIN_BRIDGE_VS_COMPONENT_SUPPLIER_COST_PASS_THROUGH_GAP","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"price_source":"Songdaiki/stock-web"}
{"case_id":"R9L10_C29_018880_2023_THERMAL_VOLUME_MARGIN_GAP","symbol":"018880","company_name":"한온시스템","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"TR_R9L10_018880_S2_20230412","score_price_alignment":"EV thermal / customer-volume narrative did not translate into durable margin bridge; score should be capped until margin/revision evidence confirms.","current_profile_verdict":"current_profile_false_positive","notes":"Supplier with restructuring/input-cost burden: C29 must distinguish order/volume from price-cost pass-through.","row_type":"case","round":"R9","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"OEM_VOLUME_MIX_MARGIN_BRIDGE_VS_COMPONENT_SUPPLIER_COST_PASS_THROUGH_GAP","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"price_source":"Songdaiki/stock-web"}
```

### 25.3 trigger rows

```jsonl
{"trigger_id":"TR_R9L10_005380_S2_20230126","case_id":"R9L10_C29_005380_2023_VOLUME_MIX_MARGIN_SUCCESS","symbol":"005380","company_name":"현대차","trigger_type":"Stage2-Actionable","trigger_date":"2023-01-26","entry_date":"2023-01-27","entry_price":173900,"evidence_available_at_that_date":"2022 full-year/4Q result and 2023 shipment/mix guidance available by/after 2023-01-26; unknown intraday timing uses next trading date close.","evidence_source":"public earnings/guidance event + stock-web OHLC rows","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","early_revision_signal","relative_strength"],"stage3_evidence_fields":["margin_bridge","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"MFE_30D_pct":3.74,"MFE_90D_pct":21.62,"MFE_180D_pct":21.62,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-3.97,"MAE_90D_pct":-3.97,"MAE_180D_pct":-3.97,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-05-11","peak_price":211500,"drawdown_after_peak_pct":-9.64,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L10_005380_20230127_173900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"row_type":"trigger","round":"R9","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"OEM_VOLUME_MIX_MARGIN_BRIDGE_VS_COMPONENT_SUPPLIER_COST_PASS_THROUGH_GAP","sector":"모빌리티·운송·레저 / EV green mobility overlap","primary_archetype":"mobility volume margin operating leverage","loop_objective":"residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|coverage_gap_fill","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005380/2023.csv","profile_path":"atlas/symbol_profiles/005/005380.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"calibration_block_reasons":[]}
{"trigger_id":"TR_R9L10_005380_GREEN_20230425","case_id":"R9L10_C29_005380_2023_VOLUME_MIX_MARGIN_SUCCESS","symbol":"005380","company_name":"현대차","trigger_type":"Stage3-Green","trigger_date":"2023-04-25","entry_date":"2023-04-26","entry_price":201500,"evidence_available_at_that_date":"Q1 confirmation converts Stage2 volume/mix evidence into stronger margin/revision visibility.","evidence_source":"public Q1 result confirmation + stock-web OHLC rows","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"MFE_30D_pct":4.96,"MFE_90D_pct":4.96,"MFE_180D_pct":4.96,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.63,"MAE_90D_pct":-4.52,"MAE_180D_pct":-4.52,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-05-11","peak_price":211500,"drawdown_after_peak_pct":-9.64,"green_lateness_ratio":0.73,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"late_green_comparison","current_profile_verdict":"current_profile_too_late","forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L10_005380_20230426_201500","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.25,"do_not_count_as_new_case":true,"row_type":"trigger","round":"R9","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"OEM_VOLUME_MIX_MARGIN_BRIDGE_VS_COMPONENT_SUPPLIER_COST_PASS_THROUGH_GAP","sector":"모빌리티·운송·레저 / EV green mobility overlap","primary_archetype":"mobility volume margin operating leverage","loop_objective":"residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|coverage_gap_fill","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005380/2023.csv","profile_path":"atlas/symbol_profiles/005/005380.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"calibration_block_reasons":[]}
{"trigger_id":"TR_R9L10_000270_S2_20230127","case_id":"R9L10_C29_000270_2023_VOLUME_MIX_MARGIN_SUCCESS","symbol":"000270","company_name":"기아","trigger_type":"Stage2-Actionable","trigger_date":"2023-01-27","entry_date":"2023-01-30","entry_price":68600,"evidence_available_at_that_date":"2022/4Q result and 2023 wholesale/mix margin guidance available by/after 2023-01-27; unknown intraday timing uses next trading date close.","evidence_source":"public earnings/guidance event + stock-web OHLC rows","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","early_revision_signal","relative_strength"],"stage3_evidence_fields":["margin_bridge","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"MFE_30D_pct":17.2,"MFE_90D_pct":33.97,"MFE_180D_pct":33.97,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.62,"MAE_90D_pct":-2.62,"MAE_180D_pct":-2.62,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-05-11","peak_price":91900,"drawdown_after_peak_pct":-12.84,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L10_000270_20230130_68600","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"row_type":"trigger","round":"R9","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"OEM_VOLUME_MIX_MARGIN_BRIDGE_VS_COMPONENT_SUPPLIER_COST_PASS_THROUGH_GAP","sector":"모빌리티·운송·레저 / EV green mobility overlap","primary_archetype":"mobility volume margin operating leverage","loop_objective":"residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|coverage_gap_fill","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000270/2023.csv","profile_path":"atlas/symbol_profiles/000/000270.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"calibration_block_reasons":[]}
{"trigger_id":"TR_R9L10_000270_GREEN_20230425","case_id":"R9L10_C29_000270_2023_VOLUME_MIX_MARGIN_SUCCESS","symbol":"000270","company_name":"기아","trigger_type":"Stage3-Green","trigger_date":"2023-04-25","entry_date":"2023-04-26","entry_price":85700,"evidence_available_at_that_date":"Q1 confirmation validates margin bridge after Stage2 evidence was already visible.","evidence_source":"public Q1 result confirmation + stock-web OHLC rows","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"MFE_30D_pct":7.23,"MFE_90D_pct":7.23,"MFE_180D_pct":7.23,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.37,"MAE_90D_pct":-5.72,"MAE_180D_pct":-5.72,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-05-11","peak_price":91900,"drawdown_after_peak_pct":-12.84,"green_lateness_ratio":0.73,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"late_green_comparison","current_profile_verdict":"current_profile_too_late","forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L10_000270_20230426_85700","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.25,"do_not_count_as_new_case":true,"row_type":"trigger","round":"R9","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"OEM_VOLUME_MIX_MARGIN_BRIDGE_VS_COMPONENT_SUPPLIER_COST_PASS_THROUGH_GAP","sector":"모빌리티·운송·레저 / EV green mobility overlap","primary_archetype":"mobility volume margin operating leverage","loop_objective":"residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|coverage_gap_fill","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000270/2023.csv","profile_path":"atlas/symbol_profiles/000/000270.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"calibration_block_reasons":[]}
{"trigger_id":"TR_R9L10_000270_4B_PRICE_LOCAL_20230511","case_id":"R9L10_C29_000270_2023_VOLUME_MIX_MARGIN_SUCCESS","symbol":"000270","company_name":"기아","trigger_type":"Stage4B-price-local-only","trigger_date":"2023-05-11","entry_date":"2023-05-11","entry_price":90100,"evidence_available_at_that_date":"Local price peak after strong run; no clear non-price 4B evidence at that date.","evidence_source":"stock-web local peak observation only","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"MFE_30D_pct":0.0,"MFE_90D_pct":1.99,"MFE_180D_pct":1.99,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-10.21,"MAE_90D_pct":-10.21,"MAE_180D_pct":-10.21,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-05-11","peak_price":91900,"drawdown_after_peak_pct":-12.84,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.92,"four_b_full_window_peak_proximity":0.92,"four_b_timing_verdict":"price_only_local_4B_watch_not_full_4B","four_b_evidence_type":["price_only"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_success_as_watch_only","current_profile_verdict":"current_profile_correct","forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L10_000270_20230511_90100","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.25,"do_not_count_as_new_case":true,"row_type":"trigger","round":"R9","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"OEM_VOLUME_MIX_MARGIN_BRIDGE_VS_COMPONENT_SUPPLIER_COST_PASS_THROUGH_GAP","sector":"모빌리티·운송·레저 / EV green mobility overlap","primary_archetype":"mobility volume margin operating leverage","loop_objective":"residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|coverage_gap_fill","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000270/2023.csv","profile_path":"atlas/symbol_profiles/000/000270.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"calibration_block_reasons":[]}
{"trigger_id":"TR_R9L10_204320_S2_20230210","case_id":"R9L10_C29_204320_2023_VOLUME_WITH_MARGIN_GAP","symbol":"204320","company_name":"HL만도","trigger_type":"Stage2-Actionable-false-positive","trigger_date":"2023-02-10","entry_date":"2023-02-10","entry_price":47600,"evidence_available_at_that_date":"Auto production recovery and customer/ADAS volume route narrative without confirmed margin pass-through.","evidence_source":"public sector/customer narrative + stock-web OHLC rows","stage2_evidence_fields":["customer_or_order_quality","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"MFE_30D_pct":9.45,"MFE_90D_pct":9.03,"MFE_180D_pct":14.5,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.56,"MAE_90D_pct":-7.56,"MAE_180D_pct":-7.56,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-06-30","peak_price":54500,"drawdown_after_peak_pct":-15.32,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive","forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L10_204320_20230210_47600","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"row_type":"trigger","round":"R9","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"OEM_VOLUME_MIX_MARGIN_BRIDGE_VS_COMPONENT_SUPPLIER_COST_PASS_THROUGH_GAP","sector":"모빌리티·운송·레저 / EV green mobility overlap","primary_archetype":"mobility volume margin operating leverage","loop_objective":"residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|coverage_gap_fill","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/204/204320/2023.csv","profile_path":"atlas/symbol_profiles/204/204320.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"calibration_block_reasons":[]}
{"trigger_id":"TR_R9L10_011210_S2_20230411","case_id":"R9L10_C29_011210_2023_HIGH_MAE_VOLUME_OPTIONALITY","symbol":"011210","company_name":"현대위아","trigger_type":"Stage2-Actionable-high-MAE","trigger_date":"2023-04-11","entry_date":"2023-04-11","entry_price":64400,"evidence_available_at_that_date":"Mobility/thermal/EV optionality and group volume route sparked a local move, but durable margin conversion remained unclear.","evidence_source":"public mobility optionality narrative + stock-web OHLC rows","stage2_evidence_fields":["capacity_or_volume_route","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"MFE_30D_pct":4.04,"MFE_90D_pct":9.47,"MFE_180D_pct":9.47,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-13.82,"MAE_90D_pct":-13.82,"MAE_180D_pct":-13.82,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-06","peak_price":70500,"drawdown_after_peak_pct":-13.48,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.47,"four_b_full_window_peak_proximity":0.47,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["price_only"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"high_mae_success_not_clean_positive","current_profile_verdict":"current_profile_too_early","forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L10_011210_20230411_64400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"row_type":"trigger","round":"R9","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"OEM_VOLUME_MIX_MARGIN_BRIDGE_VS_COMPONENT_SUPPLIER_COST_PASS_THROUGH_GAP","sector":"모빌리티·운송·레저 / EV green mobility overlap","primary_archetype":"mobility volume margin operating leverage","loop_objective":"residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|coverage_gap_fill","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011210/2023.csv","profile_path":"atlas/symbol_profiles/011/011210.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"calibration_block_reasons":[]}
{"trigger_id":"TR_R9L10_018880_S2_20230412","case_id":"R9L10_C29_018880_2023_THERMAL_VOLUME_MARGIN_GAP","symbol":"018880","company_name":"한온시스템","trigger_type":"Stage2-Actionable-false-positive","trigger_date":"2023-04-12","entry_date":"2023-04-12","entry_price":9170,"evidence_available_at_that_date":"EV thermal/customer volume route existed, but cost/pass-through and restructuring burden blocked durable margin expansion.","evidence_source":"public sector narrative + stock-web OHLC rows","stage2_evidence_fields":["customer_or_order_quality","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"MFE_30D_pct":10.91,"MFE_90D_pct":10.91,"MFE_180D_pct":10.91,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-10.25,"MAE_90D_pct":-11.56,"MAE_180D_pct":-11.56,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-05-10","peak_price":10170,"drawdown_after_peak_pct":-20.26,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"false_positive_green_candidate","current_profile_verdict":"current_profile_false_positive","forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L10_018880_20230412_9170","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"row_type":"trigger","round":"R9","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"OEM_VOLUME_MIX_MARGIN_BRIDGE_VS_COMPONENT_SUPPLIER_COST_PASS_THROUGH_GAP","sector":"모빌리티·운송·레저 / EV green mobility overlap","primary_archetype":"mobility volume margin operating leverage","loop_objective":"residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|coverage_gap_fill","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/018/018880/2023.csv","profile_path":"atlas/symbol_profiles/018/018880.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"calibration_block_reasons":[]}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L10_C29_005380_2023_VOLUME_MIX_MARGIN_SUCCESS","trigger_id":"TR_R9L10_005380_S2_20230126","symbol":"005380","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":20,"backlog_visibility_score":50,"margin_bridge_score":85,"revision_score":70,"relative_strength_score":65,"customer_quality_score":85,"policy_or_regulatory_score":30,"valuation_repricing_score":70,"execution_risk_score":20,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":50,"margin_bridge_score":90,"revision_score":70,"relative_strength_score":65,"customer_quality_score":85,"policy_or_regulatory_score":30,"valuation_repricing_score":75,"execution_risk_score":20,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":86,"stage_label_after":"Stage3-Yellow candidate","changed_components":["margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C29 shadow profile gives positive credit only when volume is tied to OEM mix/ASP/margin evidence; component suppliers without pass-through are capped.","MFE_90D_pct":21.62,"MAE_90D_pct":-3.97,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L10_C29_000270_2023_VOLUME_MIX_MARGIN_SUCCESS","trigger_id":"TR_R9L10_000270_S2_20230127","symbol":"000270","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":20,"backlog_visibility_score":45,"margin_bridge_score":90,"revision_score":75,"relative_strength_score":75,"customer_quality_score":85,"policy_or_regulatory_score":25,"valuation_repricing_score":75,"execution_risk_score":15,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":84,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":45,"margin_bridge_score":95,"revision_score":75,"relative_strength_score":75,"customer_quality_score":85,"policy_or_regulatory_score":25,"valuation_repricing_score":80,"execution_risk_score":15,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":88,"stage_label_after":"Stage3-Yellow candidate","changed_components":["margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C29 shadow profile gives positive credit only when volume is tied to OEM mix/ASP/margin evidence; component suppliers without pass-through are capped.","MFE_90D_pct":33.97,"MAE_90D_pct":-2.62,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L10_C29_204320_2023_VOLUME_WITH_MARGIN_GAP","trigger_id":"TR_R9L10_204320_S2_20230210","symbol":"204320","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":35,"backlog_visibility_score":45,"margin_bridge_score":35,"revision_score":45,"relative_strength_score":55,"customer_quality_score":70,"policy_or_regulatory_score":20,"valuation_repricing_score":45,"execution_risk_score":55,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":45,"margin_bridge_score":25,"revision_score":45,"relative_strength_score":55,"customer_quality_score":70,"policy_or_regulatory_score":20,"valuation_repricing_score":45,"execution_risk_score":65,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":63,"stage_label_after":"Stage1/2-watch","changed_components":["margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C29 shadow profile gives positive credit only when volume is tied to OEM mix/ASP/margin evidence; component suppliers without pass-through are capped.","MFE_90D_pct":9.03,"MAE_90D_pct":-7.56,"score_return_alignment_label":"before_profile_overpromoted","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L10_C29_011210_2023_HIGH_MAE_VOLUME_OPTIONALITY","trigger_id":"TR_R9L10_011210_S2_20230411","symbol":"011210","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":20,"margin_bridge_score":30,"revision_score":35,"relative_strength_score":75,"customer_quality_score":60,"policy_or_regulatory_score":55,"valuation_repricing_score":45,"execution_risk_score":65,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":10,"backlog_visibility_score":20,"margin_bridge_score":20,"revision_score":35,"relative_strength_score":75,"customer_quality_score":60,"policy_or_regulatory_score":55,"valuation_repricing_score":45,"execution_risk_score":75,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":61,"stage_label_after":"Stage1 theme-watch","changed_components":["margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C29 shadow profile gives positive credit only when volume is tied to OEM mix/ASP/margin evidence; component suppliers without pass-through are capped.","MFE_90D_pct":9.47,"MAE_90D_pct":-13.82,"score_return_alignment_label":"before_profile_overpromoted","current_profile_verdict":"current_profile_too_early"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L10_C29_018880_2023_THERMAL_VOLUME_MARGIN_GAP","trigger_id":"TR_R9L10_018880_S2_20230412","symbol":"018880","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":30,"backlog_visibility_score":35,"margin_bridge_score":20,"revision_score":25,"relative_strength_score":50,"customer_quality_score":70,"policy_or_regulatory_score":35,"valuation_repricing_score":30,"execution_risk_score":75,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":71,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":30,"backlog_visibility_score":35,"margin_bridge_score":10,"revision_score":25,"relative_strength_score":50,"customer_quality_score":70,"policy_or_regulatory_score":35,"valuation_repricing_score":30,"execution_risk_score":85,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":58,"stage_label_after":"Stage1/2-watch or 4C-watch","changed_components":["margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C29 shadow profile gives positive credit only when volume is tied to OEM mix/ASP/margin evidence; component suppliers without pass-through are capped.","MFE_90D_pct":10.91,"MAE_90D_pct":-11.56,"score_return_alignment_label":"before_profile_overpromoted","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 shadow_weight rows

```jsonl
{"row_type":"shadow_weight","axis":"c29_volume_to_margin_bridge_required","scope":"canonical_archetype_specific","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","baseline_value":0,"tested_value":1,"delta":"+1 gate","reason":"OEM volume recovery only became clean positive when paired with ASP/mix/operating-margin bridge; supplier volume without pass-through created false positives.","backtest_effect":"Separates 005380/000270 clean positives from 204320/018880 margin-gap cases.","trigger_ids":"TR_R9L10_005380_S2_20230126|TR_R9L10_000270_S2_20230127|TR_R9L10_204320_S2_20230210|TR_R9L10_018880_S2_20230412","calibration_usable_count":5,"new_independent_case_count":5,"counterexample_count":3,"confidence":"medium","proposal_type":"canonical_archetype_shadow_only","notes":"not production; post-calibrated residual"}
{"row_type":"shadow_weight","axis":"c29_component_supplier_cost_pass_through_guard","scope":"canonical_archetype_specific","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","baseline_value":0,"tested_value":1,"delta":"+1 guard","reason":"HL만도/한온시스템 show that customer volume and EV exposure are insufficient without margin pass-through or confirmed revision.","backtest_effect":"Reduces false positive Green/Stage2 promotion in component names with input-cost or restructuring drag.","trigger_ids":"TR_R9L10_204320_S2_20230210|TR_R9L10_018880_S2_20230412","calibration_usable_count":2,"new_independent_case_count":2,"counterexample_count":2,"confidence":"medium","proposal_type":"canonical_archetype_shadow_only","notes":"not production; post-calibrated residual"}
{"row_type":"shadow_weight","axis":"c29_4b_requires_revision_or_margin_slowdown","scope":"canonical_archetype_specific","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","baseline_value":"full_4b_requires_non_price_evidence","tested_value":"margin/revision slowdown subtype","delta":"subtype guard","reason":"Price-only local peak in Kia should be a watch overlay, not full 4B, unless revision/margin/order slowdown appears.","backtest_effect":"Strengthens existing full_4b_requires_non_price_evidence specifically for C29 mobility names.","trigger_ids":"TR_R9L10_000270_4B_PRICE_LOCAL_20230511","calibration_usable_count":1,"new_independent_case_count":1,"counterexample_count":0,"confidence":"low","proposal_type":"archetype_shadow_only","notes":"not production; overlay calibration only"}
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R9","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","new_independent_case_count":5,"reused_case_count":0,"new_symbol_count":5,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_total_min","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["component_supplier_volume_false_positive","high_mae_theme_volume_optionality","green_late_after_oem_margin_bridge"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"R9L10_C29_HOLDOUT_NON_KOREA_OEM","symbol":"000000","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","reason":"future_holdout_validation_needed_non_korea_oem_or_transport_operator","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

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
next_round = R10_loop_10_or_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
alternative = R9_holdout_transport_operator_or_auto_supplier
```

## 28. Source Notes

```text
stock-web manifest: atlas/manifest.json
stock-web schema: atlas/schema.json
stock-web profile paths:
  - atlas/symbol_profiles/005/005380.json
  - atlas/symbol_profiles/000/000270.json
  - atlas/symbol_profiles/204/204320.json
  - atlas/symbol_profiles/011/011210.json
  - atlas/symbol_profiles/018/018880.json
stock-web price rows:
  - atlas/ohlcv_tradable_by_symbol_year/005/005380/2023.csv
  - atlas/ohlcv_tradable_by_symbol_year/000/000270/2023.csv
  - atlas/ohlcv_tradable_by_symbol_year/204/204320/2023.csv
  - atlas/ohlcv_tradable_by_symbol_year/011/011210/2023.csv
  - atlas/ohlcv_tradable_by_symbol_year/018/018880/2023.csv
stock_agent research artifacts:
  - reports/e2r_calibration/ingest_summary.md
  - reports/e2r_calibration/applied_scoring_diff.md
```

No stock_agent source code was opened or modified.
