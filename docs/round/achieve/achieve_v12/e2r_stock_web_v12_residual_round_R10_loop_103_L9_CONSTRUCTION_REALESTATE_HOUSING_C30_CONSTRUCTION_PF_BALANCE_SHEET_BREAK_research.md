# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R10
selected_loop: 103
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: PF_REFINANCING_DEBT_SERVICE_CASH_BRIDGE_HOLDOUT_VALIDATION_VS_POLICY_REBOUND_LABEL
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
  stock_web_manifest: read_ok
  uncached_symbol_shards:
    - 006360: cache_miss
    - 001880: cache_miss
    - 013580: cache_miss
    - 005960: cache_miss
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
loop_objective:
  - holdout_validation
  - 4B_non_price_requirement_stress_test
  - residual_false_positive_mining
price_source: Songdaiki/stock-web
price_data_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

`C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK` remains a thin Priority 0 archetype in the no-repeat index. It maps to `R10 / L9_CONSTRUCTION_REALESTATE_HOUSING` under the v12 scheduler.

This file is a **holdout-validation / rule-consolidation** MD. It does not pretend to add new independent stock-web rows because direct uncached symbol-shard fetch for additional construction names returned cache miss during this turn. Instead, it reuses current-session C30 rows that already contain complete 30D/90D/180D MFE and MAE from `Songdaiki/stock-web` tradable OHLC. Exact duplicate keys should be deduped during batch ingest. No production scoring is changed.

---

## 1. Research thesis

C30 should not reward generic construction relief.

It should reward this narrower bridge:

```text
PF stress / low-PBR builder / housing relief / liquidity support
→ issuer-specific refinancing, maturity rollover, guarantee relief, presale improvement, debt-service capacity, cash conversion
→ equity price validation
```

The recurring false positive:

```text
sector policy headline
+ low-PBR builder label
+ short rebound
```

This is not enough. The model must see whether the specific builder’s balance sheet stopped leaking.

This loop validates the current C30 gate:

1. **Large-builder survivor**  
   A low-MAE survivor can stay Watch/Stage2, but not Green without cash and margin bridge.

2. **Delayed rebound**  
   Later price validation is useful, but the original trigger cannot be backfilled as immediate Stage2.

3. **Weak-liquidity false positive**  
   Low MFE and deep MAE with no issuer cash bridge should hard block.

4. **Price-only 4B overlay**  
   A later spike without non-price confirmation remains local 4B only.

5. **Direct workout stress-control**  
   Workout can preserve creditors before equity. It is not clean aggregate evidence.

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 5
  actual_trigger_rows: 7
  source_archetypes:
    - C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
    - C31_POLICY_SUBSIDY_LEGISLATION_EVENT
    - R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
    - R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
    - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
    - R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
  price_windows:
    - 30D MFE/MAE
    - 90D MFE/MAE
    - 180D MFE/MAE
  output_use:
    - C30 holdout validation
    - PF/refinancing cash-bridge gate verification
    - delayed rebound no-backfill guard
    - stress-control exclusion for workout rows
```

---

## 3. Source validation

```yaml
stock_web_manifest:
  source_name: FinanceData/marcap
  price_adjustment_status: raw_unadjusted_marcap
  max_date: 2026-02-20
  calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
  raw_shard_root: atlas/ohlcv_raw_by_symbol_year
  symbol_count: 5414
  tradable_row_count: 14354401
  raw_row_count: 15214118
  caveat: Raw/unadjusted OHLC; corporate-action-contaminated windows blocked by default.
```

Local stock-web-derived row provenance:

```yaml
reused_price_rows_from_current_session:
  - R10/C30 loop 102
  - R10/C30 loop 3
  - R11/C31 loop 104
  - R13 accounting-trust loop 12
  - R13 Stage2 false-positive loop 10
  - R13 high-MAE loop 8
  - R13 4B/4C loop 103
reason:
  - all reused rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - uncached additional symbol shards returned cache miss in this turn
  - exact duplicate C30 keys should be deduped during batch ingest
  - this file is holdout validation only
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","selected_round":"R10","selected_loop":103,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"LARGE_BUILDER_BALANCE_SHEET_SURVIVOR_LOW_MAE_CONTROL","symbol":"000720","name":"현대건설","trigger_type":"Stage2-Watch","entry_date":"2024-01-26","entry_price":33100,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":7.30,"MAE_30D_pct":-3.50,"MFE_90D_pct":8.80,"MAE_90D_pct":-5.70,"MFE_180D_pct":8.80,"MAE_180D_pct":-12.20,"forward_high_30d":34850,"forward_low_30d":31950,"forward_high_90d":36000,"forward_low_90d":31200,"forward_high_180d":36000,"forward_low_180d":29050,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C30|000720|Stage2-Watch|2024-01-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_survivor_control","reuse_reason":"same C30 survivor-control row from loop 102; used for holdout validation","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"large_builder_survivor_watch","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|000720|Stage2-Watch|2024-01-26","non_price_bridge":"large-builder balance-sheet survivor / order-quality bridge under PF relief lens; not Green without margin and cash conversion bridge","score_alignment":"Stage2-Watch only; require issuer-specific margin, receivable and cash conversion refresh before promotion"}
{"row_type":"trigger","selected_round":"R10","selected_loop":103,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"DELAYED_BUILDER_REBOUND_NO_BACKFILL","symbol":"047040","name":"대우건설","trigger_type":"Stage2-Watch","entry_date":"2024-01-26","entry_price":4015,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":2.60,"MAE_30D_pct":-5.60,"MFE_90D_pct":2.60,"MAE_90D_pct":-10.80,"MFE_180D_pct":23.70,"MAE_180D_pct":-12.30,"forward_high_30d":4120,"forward_low_30d":3790,"forward_high_90d":4120,"forward_low_90d":3580,"forward_high_180d":4965,"forward_low_180d":3520,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C30|047040|Stage2-Watch|2024-01-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_delayed_rebound","reuse_reason":"same C30 delayed-rebound row from loop 102; used to validate no-backfill guard","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"delayed_rebound_control","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|047040|Stage2-Watch|2024-01-26","non_price_bridge":"PF relief plus construction rebound narrative, but validation arrived late","score_alignment":"delayed local 4B; do not backfill 180D rebound as immediate Stage2-Actionable"}
{"row_type":"trigger","selected_round":"R10","selected_loop":103,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"WEAK_LIQUIDITY_PF_RELIEF_LABEL_HARD_4C","symbol":"002990","name":"금호건설","trigger_type":"Stage4C","entry_date":"2024-01-26","entry_price":5030,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":5.00,"MAE_30D_pct":-4.60,"MFE_90D_pct":5.00,"MAE_90D_pct":-27.50,"MFE_180D_pct":5.00,"MAE_180D_pct":-41.00,"forward_high_30d":5280,"forward_low_30d":4800,"forward_high_90d":5280,"forward_low_90d":3650,"forward_high_180d":5280,"forward_low_180d":2970,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C30|002990|Stage4C|2024-01-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","reuse_reason":"same C30 weak-liquidity hard-block row from loop 102","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"hard_4C_counterexample","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|002990|Stage4C|2024-01-26","non_price_bridge":"low-PBR/PF-relief vocabulary without liquidity, debt-service, margin or cash bridge","score_alignment":"hard 4C; policy umbrella did not reach issuer cashflow"}
{"row_type":"trigger","selected_round":"R10","selected_loop":103,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PRICE_ONLY_LOCAL_4B_AFTER_REBOUND_NO_GREEN","symbol":"047040","name":"대우건설","trigger_type":"Stage4B","entry_date":"2024-07-18","entry_price":4250,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":16.80,"MAE_30D_pct":-16.60,"MFE_90D_pct":16.80,"MAE_90D_pct":-17.20,"MFE_180D_pct":16.80,"MAE_180D_pct":-30.80,"forward_high_30d":4965,"forward_low_30d":3545,"forward_high_90d":4965,"forward_low_90d":3520,"forward_high_180d":4965,"forward_low_180d":2940,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C30|047040|Stage4B|2024-07-18","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_price_only_4B","reuse_reason":"same C30 price-only 4B overlay from loop 102","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"price_only_4B_overlay","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|047040|Stage4B|2024-07-18","non_price_bridge":"price spike after construction/PF rebound vocabulary; non-price confirmation insufficient for full positive action","score_alignment":"local 4B only; no Green without non-price issuer cash bridge"}
{"row_type":"trigger","selected_round":"R10","selected_loop":103,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"DEVELOPER_DELAYED_HOUSING_PF_SOFT_LANDING_LOCAL_4B","symbol":"294870","name":"HDC현대산업개발","trigger_type":"Stage4B","entry_date":"2024-05-13","entry_price":17920,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":2.12,"MAE_30D_pct":-6.58,"MFE_90D_pct":37.28,"MAE_90D_pct":-6.58,"MFE_180D_pct":57.37,"MAE_180D_pct":-6.58,"forward_high_30d":18300,"forward_low_30d":16740,"forward_high_90d":24600,"forward_low_90d":16740,"forward_high_180d":28200,"forward_low_180d":16740,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C30|294870|Stage4B|2024-05-13","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_delayed_local_4B","reuse_reason":"same C30 delayed soft-landing row from loop 102 / C31 loop 104","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"delayed_positive_local_4B","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|294870|Stage4B|2024-05-13","non_price_bridge":"delayed PF/housing soft-landing path, but issuer-specific refinancing/liquidity bridge not visible at entry","score_alignment":"local 4B; do not backfill later rebound as immediate Stage2-Actionable"}
{"row_type":"trigger","selected_round":"R10","selected_loop":103,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"MID_BUILDER_SUPPORT_HEADLINE_DELAYED_LOCAL_4B","symbol":"014790","name":"HL D&I","trigger_type":"Stage4B","entry_date":"2024-03-27","entry_price":2010,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":1.74,"MAE_30D_pct":-3.73,"MFE_90D_pct":32.34,"MAE_90D_pct":-3.73,"MFE_180D_pct":32.34,"MAE_180D_pct":-3.73,"forward_high_30d":2045,"forward_low_30d":1935,"forward_high_90d":2660,"forward_low_90d":1935,"forward_high_180d":2660,"forward_low_180d":1935,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C30|014790|Stage4B|2024-03-27","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_delayed_local_4B","reuse_reason":"same C30 delayed support row from loop 102 / loop 3","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"mid_builder_delayed_local_4B","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|014790|Stage4B|2024-03-27","non_price_bridge":"mid-builder support headline with delayed price validation but no immediate issuer-specific bridge","score_alignment":"local 4B; require timestamped refinancing, presale or cash conversion bridge before promotion"}
{"row_type":"trigger","selected_round":"R10","selected_loop":103,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"DIRECT_WORKOUT_STRESS_CONTROL_NOT_CLEAN_AGGREGATE","symbol":"009410","name":"태영건설","trigger_type":"Stage2-Watch","entry_date":"2024-01-11","entry_price":3765,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":9.16,"MAE_30D_pct":-42.10,"MFE_90D_pct":9.16,"MAE_90D_pct":-42.10,"MFE_180D_pct":62.28,"MAE_180D_pct":-42.10,"forward_high_30d":4110,"forward_low_30d":2180,"forward_high_90d":4110,"forward_low_90d":2180,"forward_high_180d":6110,"forward_low_180d":2180,"corporate_action_window_status":"workout_or_trading_gap_contamination_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":false,"same_entry_group_id":"C30|009410|Stage2-Watch|2024-01-11","dedupe_for_aggregate":true,"aggregate_group_role":"stress_control_only","reuse_reason":"same workout stress-control row from C30 loop 102; not clean aggregate","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"workout_stress_control_only","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|009410|Stage2-Watch|2024-01-11","non_price_bridge":"direct workout / debt restructuring survival bridge, but equity recovery and corporate-action/trading-gap window are not clean","score_alignment":"exclude from clean aggregate; use as stress-control for workout-not-equity-recovery rule"}
```

---

## 5. Case analysis

### 5.1 Hyundai E&C / 000720 — survivor watch

Low drawdown means the row is not a hard block. But modest MFE means it is not a Green unlock either.

```yaml
entry_close: 33100
90D_MFE_MAE: +8.80 / -5.70
180D_MFE_MAE: +8.80 / -12.20
route: Stage2-Watch
```

### 5.2 Daewoo E&C / 047040 — delayed rebound

The 180D rebound should not rewrite the 30D/90D weakness.

```yaml
entry_close: 4015
90D_MFE_MAE: +2.60 / -10.80
180D_MFE_MAE: +23.70 / -12.30
route: delayed local 4B
```

### 5.3 Kumho E&C / 002990 — hard 4C

This is the clean C30 false positive.

```yaml
entry_close: 5030
90D_MFE_MAE: +5.00 / -27.50
180D_MFE_MAE: +5.00 / -41.00
route: Stage4C
```

### 5.4 Daewoo E&C / 047040 — price-only 4B overlay

A later spike without non-price bridge stays local 4B only.

```yaml
entry_close: 4250
90D_MFE_MAE: +16.80 / -17.20
180D_MFE_MAE: +16.80 / -30.80
route: Stage4B
```

### 5.5 HDC Hyundai Development / 294870 — delayed local 4B

Delayed validation exists, but entry-date issuer bridge was incomplete.

```yaml
entry_close: 17920
90D_MFE_MAE: +37.28 / -6.58
180D_MFE_MAE: +57.37 / -6.58
route: Stage4B
```

### 5.6 HL D&I / 014790 — mid-builder delayed 4B

Shallow drawdown and delayed MFE are useful, but not immediate Actionable.

```yaml
entry_close: 2010
90D_MFE_MAE: +32.34 / -3.73
180D_MFE_MAE: +32.34 / -3.73
route: Stage4B
```

### 5.7 Taeyoung E&C / 009410 — workout stress-control

This row is informative, but not calibration-clean aggregate.

```yaml
entry_close: 3765
90D_MFE_MAE: +9.16 / -42.10
180D_MFE_MAE: +62.28 / -42.10
route: stress-control only
```

---

## 6. Score-return alignment

```yaml
new_independent_case_count: 0
reused_case_count: 7
new_symbol_count: 0
same_archetype_new_symbol_count: 0
same_archetype_new_trigger_family_count: 0
new_trigger_family_count: 0
calibration_usable_case_count: 6
calibration_usable_trigger_count: 6
stress_control_case_count: 1
positive_case_count: 3
counterexample_count: 2
local_4B_watch_count: 4
current_profile_error_count: 4
diversity_score_summary: "C30 bridge types covered, but all rows are reused holdout controls due cache-miss on additional shards"
loop_contribution_label: duplicate_low_value_loop
do_not_propose_new_weight_delta: true
```

| symbol | role | 90D MFE/MAE | 180D MFE/MAE | holdout lesson |
|---|---:|---:|---:|---|
| 000720 | survivor watch | +8.80 / -5.70 | +8.80 / -12.20 | stable but not Green |
| 047040 | delayed rebound | +2.60 / -10.80 | +23.70 / -12.30 | no backfill |
| 002990 | hard 4C | +5.00 / -27.50 | +5.00 / -41.00 | weak liquidity label fails |
| 047040 | price-only 4B | +16.80 / -17.20 | +16.80 / -30.80 | no Green without evidence |
| 294870 | delayed 4B | +37.28 / -6.58 | +57.37 / -6.58 | later validation only |
| 014790 | delayed 4B | +32.34 / -3.73 | +32.34 / -3.73 | needs timestamped bridge |
| 009410 | stress control | +9.16 / -42.10 | +62.28 / -42.10 | workout is not clean equity recovery |

---

## 7. Current calibrated profile stress test

The current C30 rule held up as a holdout pattern:

```text
issuer-specific bridge incomplete + delayed rebound -> local 4B
weak liquidity label + deep MAE -> hard 4C
price-only rebound -> local 4B only
workout/restructuring -> stress-control, not clean aggregate
```

### Rule candidate retained, not newly proposed

```text
C30_PF_REFINANCING_TO_ISSUER_CASH_BRIDGE_REQUIREMENT_V102_HELD_OUT

if C30
and PF_support_construction_rebound_or_low_PBR_label == true
and issuer_specific_refinancing_guarantee_presale_cash_or_debt_service_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C30
and MFE_30D_pct < +5
and MFE_90D_pct >= +25:
    route = delayed_local_4B
    do_not_backfill_as_immediate_Stage2_Actionable = true
```

```text
if C30
and price_only_rebound_or_local_peak == true
and non_price_bridge == false:
    route = local_4B_watch
    block_stage3_green = true
```

```text
if C30
and MFE_90D_pct <= +5
and MAE_90D_pct <= -20
and liquidity_cash_bridge == false:
    route = Stage4C
```

```text
if C30
and direct_workout_or_debt_restructuring == true
and shareholder_equity_bridge == false:
    route = StressControl_ExcludeCleanAggregate
```

---

## 8. Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 7
calibration_usable_trigger_count: 6
representative_trigger_count: 0
new_weight_evidence_candidate_count: 0
guardrail_candidate_count: 7
narrative_only_or_rejected_count: 1
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
batch_ingest_recommendation: dedupe_as_holdout_validation_only
```

---

## 9. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: true
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
holdout_validation_passed: true
loop_contribution_label: duplicate_low_value_loop
new_axis_proposed: null
existing_axis_strengthened:
  - C30_PF_REFINANCING_TO_ISSUER_CASH_BRIDGE_REQUIREMENT_V102_HELD_OUT
existing_axis_weakened: null
one_line_summary: "This loop adds 0 new independent cases, 2 counterexamples, and 4 residual-error holdout controls for R10/L9/C30."
```

---

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Treat this R10/C30 loop 103 as holdout validation only. Batch it with C30 loops 1~3 and 100~102 plus C31/R13 PF-policy guardrails. If exact same_entry_group_id rows already exist, dedupe them. Preserve the C30 PF-refinancing-to-issuer-cash bridge gate, but do not create a new weight delta from this loop because uncached additional construction symbol shards returned cache miss and no new independent case was added.
```

---

## 11. Next research state

```yaml
completed_round: R10
completed_loop: 103
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C31_POLICY_SUBSIDY_LEGISLATION_EVENT
  - C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
  - C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
  - C15_MATERIAL_SPREAD_SUPERCYCLE
  - R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
```
