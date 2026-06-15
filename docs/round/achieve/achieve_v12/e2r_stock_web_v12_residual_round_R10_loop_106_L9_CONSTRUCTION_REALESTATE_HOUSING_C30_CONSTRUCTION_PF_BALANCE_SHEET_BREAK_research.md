# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R10
selected_loop: 106
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: PF_REFINANCING_TO_ISSUER_CASH_BRIDGE_HOLDOUT_V106_SURVIVOR_DELAYED_REBOUND_WORKOUT_SPLIT
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
  stock_web_manifest: read_ok
  uncached_symbol_shards:
    - 006360/2024: cache_miss_observed
    - 375500/2024: cache_miss_observed
    - 013580/2024: cache_miss_observed
    - 005960/2024: cache_miss_observed
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
loop_objective:
  - holdout_validation
  - duplicate_low_value_loop_marker
  - pf_refinancing_to_issuer_cash_bridge_gate
  - delayed_rebound_no_backfill_guard
  - price_only_4B_guard
  - workout_stress_control_exclusion
  - cache_miss_todo_for_future_reprice
price_source: Songdaiki/stock-web
price_data_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

`C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK` remains Priority 0 in the current no-repeat index. The v12 scheduler maps C30 to `R10 / L9_CONSTRUCTION_REALESTATE_HOUSING`.

This file continues the local C30 sequence after `R10/C30 loop 105`; selected loop is therefore `106`.

This is a **dedupe-aware holdout validation / cache-miss TODO** MD. It does not claim fresh independent stock-web evidence because additional construction/PF candidate shards returned cache miss in this execution. The trigger rows below reuse current-session stock-web-derived C30/C31/R13 construction rows that already contain complete 30D/90D/180D MFE and MAE from `Songdaiki/stock-web` tradable OHLC. Exact duplicate `same_entry_group_id` rows should be deduped during batch ingest. No production scoring is changed.

---

## 1. Research thesis

C30 should not score a construction stock because the policy hose is open. It should score only when the water reaches that issuer.

```text
PF stress / liquidity support / construction rebound / low-PBR builder label
→ issuer-specific refinancing
→ maturity rollover
→ guarantee relief
→ presale improvement
→ debt-service capacity
→ receivables quality
→ cash conversion
→ equity price validation
```

The recurring false positive is:

```text
sector support headline
+ low-PBR builder label
+ one local rebound
```

That may be worth a local inspection bay, but it is not enough for Stage2-Actionable or Green. A builder is not repaired when the government announces a hose; it is repaired when its own balance sheet stops leaking.

The C30 decision tree remains:

```text
issuer-specific cash bridge visible
→ Stage2 can survive

delayed price validation only
→ local 4B, no backfill

price-only rebound without non-price bridge
→ local 4B only

weak-liquidity label with deep MAE
→ hard 4C

direct workout / restructuring
→ stress-control only unless clean shareholder-equity bridge is proven
```

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 6
  actual_trigger_rows: 7
  narrative_only_future_todo_rows: 1
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
    - duplicate control after cache-miss on new shards
    - PF/refinancing issuer-cash bridge gate verification
    - delayed rebound no-backfill guard
    - workout stress-control exclusion
    - no production scoring changes
```

---

## 3. Source validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","source_name":"FinanceData/marcap","validation_status":"usable_for_historical_calibration","caveat":"raw/unadjusted OHLC; corporate-action-contaminated windows blocked by default"}
```

```yaml
stock_web_manifest:
  source_name: FinanceData/marcap
  source_repo_url: https://github.com/FinanceData/marcap
  price_adjustment_status: raw_unadjusted_marcap
  min_date: 1995-05-02
  max_date: 2026-02-20
  calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
  raw_shard_root: atlas/ohlcv_raw_by_symbol_year
  deprecated_or_compat_shard_root: atlas/ohlcv_min_by_symbol_year
  symbol_count: 5414
  active_like_symbol_count: 2868
  inactive_or_delisted_like_symbol_count: 2546
  tradable_row_count: 14354401
  raw_row_count: 15214118
  corporate_action_candidate_count: 14435
  caveat: Raw/unadjusted OHLC; corporate-action-contaminated windows blocked by default.
```

Local stock-web-derived row provenance:

```yaml
reused_price_rows_from_current_session:
  - R10/C30 loops 102~105
  - R11/C31 loops 104~107
  - R13 accounting-trust loops 12~14
  - R13 Stage2 false-positive loop 11
  - R13 high-MAE loop 9
  - R13 4B/4C loop 104
reason:
  - all reused rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - uncached additional C30 candidate shards returned cache miss in this execution
  - exact duplicate C30 keys should be deduped during batch ingest
  - this file is holdout validation / duplicate-low-value marker only
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","selected_round":"R10","selected_loop":106,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"LARGE_BUILDER_BALANCE_SHEET_SURVIVOR_LOW_MAE_CONTROL","symbol":"000720","name":"현대건설","trigger_type":"Stage2-Watch","entry_date":"2024-01-26","entry_price":33100,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.30,"MAE_30D_pct":-3.50,"MFE_90D_pct":8.80,"MAE_90D_pct":-5.70,"MFE_180D_pct":8.80,"MAE_180D_pct":-12.20,"forward_high_30d":34850,"forward_low_30d":31950,"forward_high_90d":36000,"forward_low_90d":31200,"forward_high_180d":36000,"forward_low_180d":29050,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C30|000720|Stage2-Watch|2024-01-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_survivor_control","reuse_reason":"same C30 survivor-control row from loops 102~105; used for holdout validation after new-shard cache miss","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"large_builder_survivor_watch","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|000720|Stage2-Watch|2024-01-26","non_price_bridge":"large-builder balance-sheet survivor / order-quality bridge under PF relief lens; not Green without margin and cash conversion bridge","score_alignment":"Stage2-Watch only; require issuer-specific margin, receivable and cash conversion refresh before promotion"}
{"row_type":"trigger","selected_round":"R10","selected_loop":106,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"DELAYED_BUILDER_REBOUND_NO_BACKFILL","symbol":"047040","name":"대우건설","trigger_type":"Stage2-Watch","entry_date":"2024-01-26","entry_price":4015,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.60,"MAE_30D_pct":-5.60,"MFE_90D_pct":2.60,"MAE_90D_pct":-10.80,"MFE_180D_pct":23.70,"MAE_180D_pct":-12.30,"forward_high_30d":4120,"forward_low_30d":3790,"forward_high_90d":4120,"forward_low_90d":3580,"forward_high_180d":4965,"forward_low_180d":3520,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C30|047040|Stage2-Watch|2024-01-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_delayed_rebound","reuse_reason":"same C30 delayed-rebound row from loops 102~105","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"delayed_rebound_control","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|047040|Stage2-Watch|2024-01-26","non_price_bridge":"PF relief plus construction rebound narrative, but validation arrived late","score_alignment":"delayed local 4B; do not backfill 180D rebound as immediate Stage2-Actionable"}
{"row_type":"trigger","selected_round":"R10","selected_loop":106,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"WEAK_LIQUIDITY_PF_RELIEF_LABEL_HARD_4C","symbol":"002990","name":"금호건설","trigger_type":"Stage4C","entry_date":"2024-01-26","entry_price":5030,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.00,"MAE_30D_pct":-4.60,"MFE_90D_pct":5.00,"MAE_90D_pct":-27.50,"MFE_180D_pct":5.00,"MAE_180D_pct":-41.00,"forward_high_30d":5280,"forward_low_30d":4800,"forward_high_90d":5280,"forward_low_90d":3650,"forward_high_180d":5280,"forward_low_180d":2970,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C30|002990|Stage4C|2024-01-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","reuse_reason":"same C30 weak-liquidity hard-block row from loops 102~105 and R13 guardrails","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"hard_4C_counterexample","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|002990|Stage4C|2024-01-26","non_price_bridge":"low-PBR/PF-relief vocabulary without liquidity, debt-service, margin or cash bridge","score_alignment":"hard 4C; policy umbrella did not reach issuer cashflow"}
{"row_type":"trigger","selected_round":"R10","selected_loop":106,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PRICE_ONLY_LOCAL_4B_AFTER_REBOUND_NO_GREEN","symbol":"047040","name":"대우건설","trigger_type":"Stage4B","entry_date":"2024-07-18","entry_price":4250,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":16.80,"MAE_30D_pct":-16.60,"MFE_90D_pct":16.80,"MAE_90D_pct":-17.20,"MFE_180D_pct":16.80,"MAE_180D_pct":-30.80,"forward_high_30d":4965,"forward_low_30d":3545,"forward_high_90d":4965,"forward_low_90d":3520,"forward_high_180d":4965,"forward_low_180d":2940,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C30|047040|Stage4B|2024-07-18","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_price_only_4B","reuse_reason":"same C30 price-only 4B overlay from loops 102~105","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"price_only_4B_overlay","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|047040|Stage4B|2024-07-18","non_price_bridge":"price spike after construction/PF rebound vocabulary; non-price confirmation insufficient for full positive action","score_alignment":"local 4B only; no Green without non-price issuer cash bridge"}
{"row_type":"trigger","selected_round":"R10","selected_loop":106,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"DEVELOPER_DELAYED_HOUSING_PF_SOFT_LANDING_LOCAL_4B","symbol":"294870","name":"HDC현대산업개발","trigger_type":"Stage4B","entry_date":"2024-05-13","entry_price":17920,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.12,"MAE_30D_pct":-6.58,"MFE_90D_pct":37.28,"MAE_90D_pct":-6.58,"MFE_180D_pct":57.37,"MAE_180D_pct":-6.58,"forward_high_30d":18300,"forward_low_30d":16740,"forward_high_90d":24600,"forward_low_90d":16740,"forward_high_180d":28200,"forward_low_180d":16740,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C30|294870|Stage4B|2024-05-13","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_delayed_local_4B","reuse_reason":"same C30 delayed soft-landing row from loops 3/102~105 and C31 policy rows","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"delayed_positive_local_4B","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|294870|Stage4B|2024-05-13","non_price_bridge":"delayed PF/housing soft-landing path, but issuer-specific refinancing/liquidity bridge not visible at entry","score_alignment":"local 4B; do not backfill later rebound as immediate Stage2-Actionable"}
{"row_type":"trigger","selected_round":"R10","selected_loop":106,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"MID_BUILDER_SUPPORT_HEADLINE_DELAYED_LOCAL_4B","symbol":"014790","name":"HL D&I","trigger_type":"Stage4B","entry_date":"2024-03-27","entry_price":2010,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.74,"MAE_30D_pct":-3.73,"MFE_90D_pct":32.34,"MAE_90D_pct":-3.73,"MFE_180D_pct":32.34,"MAE_180D_pct":-3.73,"forward_high_30d":2045,"forward_low_30d":1935,"forward_high_90d":2660,"forward_low_90d":1935,"forward_high_180d":2660,"forward_low_180d":1935,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C30|014790|Stage4B|2024-03-27","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_delayed_local_4B","reuse_reason":"same C30 delayed support row from loops 3/102~105","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"mid_builder_delayed_local_4B","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|014790|Stage4B|2024-03-27","non_price_bridge":"mid-builder support headline with delayed price validation but no immediate issuer-specific bridge","score_alignment":"local 4B; require timestamped refinancing, presale or cash conversion bridge before promotion"}
{"row_type":"trigger","selected_round":"R10","selected_loop":106,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"DIRECT_WORKOUT_STRESS_CONTROL_NOT_CLEAN_AGGREGATE","symbol":"009410","name":"태영건설","trigger_type":"Stage2-Watch","entry_date":"2024-01-11","entry_price":3765,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.16,"MAE_30D_pct":-42.10,"MFE_90D_pct":9.16,"MAE_90D_pct":-42.10,"MFE_180D_pct":62.28,"MAE_180D_pct":-42.10,"forward_high_30d":4110,"forward_low_30d":2180,"forward_high_90d":4110,"forward_low_90d":2180,"forward_high_180d":6110,"forward_low_180d":2180,"corporate_action_window_status":"workout_or_trading_gap_contamination_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":false,"same_entry_group_id":"C30|009410|Stage2-Watch|2024-01-11","dedupe_for_aggregate":true,"aggregate_group_role":"stress_control_only","reuse_reason":"same workout stress-control row from loops 102~105 and C31 policy rows","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"workout_stress_control_only","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|009410|Stage2-Watch|2024-01-11","non_price_bridge":"direct workout / debt restructuring survival bridge, but equity recovery and corporate-action/trading-gap window are not clean","score_alignment":"exclude from clean aggregate; use as stress-control for workout-not-equity-recovery rule"}
```

---

## 5. Narrative-only future TODO

```jsonl
{"row_type":"narrative_only_future_trigger_todo","selected_round":"R10","selected_loop":106,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CACHE_MISS_C30_NEW_SYMBOL_REPRICE_TODO","candidate_symbols":["006360","375500","013580","005960"],"candidate_names":["GS건설","DL이앤씨","계룡건설","동부건설"],"why_not_trigger_row_now":"uncached 2024 stock-web symbol shards returned cache miss in this execution; no fresh 30D/90D/180D MFE/MAE computed here","calibration_usable":false,"score_alignment":"future run should compute stock-web windows for these candidates before counting them as new C30 evidence"}
```

---

## 6. Case analysis

### 6.1 Hyundai E&C / 000720 — survivor watch

Low drawdown does not equal repair. This is a stable survivor row, but not Green.

```yaml
entry_close: 33100
90D_MFE_MAE: +8.80 / -5.70
180D_MFE_MAE: +8.80 / -12.20
route: Stage2-Watch
```

### 6.2 Daewoo E&C / 047040 — delayed rebound

The delayed 180D rebound cannot be backfilled into the original weak trigger.

```yaml
entry_close: 4015
90D_MFE_MAE: +2.60 / -10.80
180D_MFE_MAE: +23.70 / -12.30
route: delayed local 4B
```

### 6.3 Kumho E&C / 002990 — weak-liquidity hard 4C

The policy umbrella did not reach the issuer’s balance sheet.

```yaml
entry_close: 5030
90D_MFE_MAE: +5.00 / -27.50
180D_MFE_MAE: +5.00 / -41.00
route: Stage4C
```

### 6.4 Daewoo E&C / 047040 — price-only 4B overlay

Local spike without a non-price issuer bridge remains local 4B only.

```yaml
entry_close: 4250
90D_MFE_MAE: +16.80 / -17.20
180D_MFE_MAE: +16.80 / -30.80
route: Stage4B
```

### 6.5 HDC Hyundai Development / 294870 — delayed PF soft landing

The delayed price path is useful evidence, but the entry-date cash bridge remained incomplete.

```yaml
entry_close: 17920
90D_MFE_MAE: +37.28 / -6.58
180D_MFE_MAE: +57.37 / -6.58
route: Stage4B
```

### 6.6 HL D&I / 014790 — mid-builder delayed 4B

This row validates delayed inspection, not immediate promotion.

```yaml
entry_close: 2010
90D_MFE_MAE: +32.34 / -3.73
180D_MFE_MAE: +32.34 / -3.73
route: Stage4B
```

### 6.7 Taeyoung E&C / 009410 — workout stress-control

Workout is useful for stress testing, but not for clean equity aggregate.

```yaml
entry_close: 3765
90D_MFE_MAE: +9.16 / -42.10
180D_MFE_MAE: +62.28 / -42.10
route: stress-control only
```

---

## 7. Score-return alignment

```yaml
new_independent_case_count: 0
reused_case_count: 7
new_symbol_count: 0
same_archetype_new_symbol_count: 0
same_archetype_new_trigger_family_count: 0
new_trigger_family_count: 0
narrative_only_future_todo_count: 1
calibration_usable_case_count: 6
calibration_usable_trigger_count: 6
stress_control_case_count: 1
positive_case_count: 3
counterexample_count: 2
local_4B_watch_count: 4
hard_4C_count: 1
current_profile_error_count: 4
diversity_score_summary: "large-builder watch, delayed rebound, weak-liquidity hard 4C, price-only 4B, delayed soft-landing, workout stress-control covered; all rows reused"
loop_contribution_label: duplicate_low_value_loop_with_cache_miss_todo
do_not_propose_new_weight_delta: true
```

| symbol | role | 90D MFE/MAE | 180D MFE/MAE | C30 lesson |
|---|---:|---:|---:|---|
| 000720 | survivor watch | +8.80 / -5.70 | +8.80 / -12.20 | stable but not Green |
| 047040 | delayed rebound | +2.60 / -10.80 | +23.70 / -12.30 | no backfill |
| 002990 | hard 4C | +5.00 / -27.50 | +5.00 / -41.00 | weak liquidity label fails |
| 047040 | price-only 4B | +16.80 / -17.20 | +16.80 / -30.80 | no Green without evidence |
| 294870 | delayed 4B | +37.28 / -6.58 | +57.37 / -6.58 | later validation only |
| 014790 | delayed 4B | +32.34 / -3.73 | +32.34 / -3.73 | needs timestamped issuer bridge |
| 009410 | stress-control | +9.16 / -42.10 | +62.28 / -42.10 | workout is not clean equity recovery |

---

## 8. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"000720","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":1,"customer_quality_score":3,"policy_or_regulatory_score":3,"valuation_repricing_score":2,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":67,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":1,"customer_quality_score":3,"policy_or_regulatory_score":2,"valuation_repricing_score":1,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_after":61,"stage_label_after":"Stage2-Watch","changed_components":["margin_bridge_score","policy_or_regulatory_score","valuation_repricing_score","accounting_trust_risk_score"],"component_delta_explanation":"Large-builder stability is useful, but issuer-specific cash conversion and margin bridge were insufficient for promotion.","MFE_90D_pct":8.80,"MAE_90D_pct":-5.70,"score_return_alignment_label":"survivor_watch_not_green","current_profile_verdict":"current_profile_correct_if_watch"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"047040","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":0,"customer_quality_score":2,"policy_or_regulatory_score":3,"valuation_repricing_score":1,"execution_risk_score":4,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":62,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":0,"customer_quality_score":2,"policy_or_regulatory_score":2,"valuation_repricing_score":1,"execution_risk_score":4,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_after":59,"stage_label_after":"DelayedLocal4B_NoBackfill","changed_components":["policy_or_regulatory_score"],"component_delta_explanation":"Original trigger lacked immediate issuer cash bridge; 180D rebound should not be backfilled.","MFE_90D_pct":2.60,"MAE_90D_pct":-10.80,"score_return_alignment_label":"delayed_rebound_no_backfill","current_profile_verdict":"current_profile_too_generous_if_actionable"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"002990","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":1,"customer_quality_score":1,"policy_or_regulatory_score":3,"valuation_repricing_score":2,"execution_risk_score":5,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":58,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":37,"stage_label_after":"Stage4C","changed_components":["relative_strength_score","policy_or_regulatory_score","valuation_repricing_score"],"component_delta_explanation":"PF-relief label did not reach liquidity, debt-service, guarantee relief or cash bridge; deep MAE confirms 4C.","MFE_90D_pct":5.00,"MAE_90D_pct":-27.50,"score_return_alignment_label":"weak_liquidity_hard_4C","current_profile_verdict":"current_profile_false_positive_if_stage2"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"047040","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":3,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":3,"execution_risk_score":4,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":63,"stage_label_before":"Stage4B","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":5,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":52,"stage_label_after":"Stage4B_price_only_no_green","changed_components":["relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Price-only rebound lacked non-price issuer bridge; local 4B only.","MFE_90D_pct":16.80,"MAE_90D_pct":-17.20,"score_return_alignment_label":"price_only_local_4B","current_profile_verdict":"current_profile_correct_if_no_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"294870","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":5,"customer_quality_score":2,"policy_or_regulatory_score":3,"valuation_repricing_score":4,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":74,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":4,"customer_quality_score":2,"policy_or_regulatory_score":2,"valuation_repricing_score":3,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_after":67,"stage_label_after":"Stage4B_delayed_no_backfill","changed_components":["margin_bridge_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","accounting_trust_risk_score"],"component_delta_explanation":"Delayed PF/housing soft landing path is useful but entry-date issuer refinancing/liquidity bridge was incomplete.","MFE_90D_pct":37.28,"MAE_90D_pct":-6.58,"score_return_alignment_label":"delayed_soft_landing_local_4B","current_profile_verdict":"current_profile_correct_if_no_backfill"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"014790","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":4,"customer_quality_score":2,"policy_or_regulatory_score":3,"valuation_repricing_score":4,"execution_risk_score":2,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":73,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":3,"customer_quality_score":2,"policy_or_regulatory_score":2,"valuation_repricing_score":3,"execution_risk_score":2,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_after":66,"stage_label_after":"Stage4B_delayed_support","changed_components":["margin_bridge_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","accounting_trust_risk_score"],"component_delta_explanation":"Delayed support row needs timestamped refinancing, presale or cash conversion bridge before promotion.","MFE_90D_pct":32.34,"MAE_90D_pct":-3.73,"score_return_alignment_label":"mid_builder_delayed_4B","current_profile_verdict":"current_profile_correct_if_4B"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"009410","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":5,"valuation_repricing_score":2,"execution_risk_score":5,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":60,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":1,"policy_or_regulatory_score":3,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":42,"stage_label_after":"StressControlOnly","changed_components":["contract_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score"],"component_delta_explanation":"Workout framework is useful for stress-control, but corporate-action/trading-gap contamination and lack of clean equity bridge prevent aggregate use.","MFE_90D_pct":9.16,"MAE_90D_pct":-42.10,"score_return_alignment_label":"workout_stress_control_only","current_profile_verdict":"exclude_from_clean_aggregate"}
```

---

## 9. Current calibrated profile stress test

The C30 PF/refinancing-to-issuer-cash gate held again:

```text
low-MAE survivor
→ Watch, not Green

delayed rebound
→ local 4B, no backfill

weak-liquidity PF label
→ hard 4C

price-only rebound
→ local 4B only

workout
→ stress-control, not clean aggregate
```

### Rule candidate retained, not newly proposed

```text
C30_PF_REFINANCING_TO_ISSUER_CASH_BRIDGE_REQUIREMENT_V106_HELD_OUT

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

## 10. Profile comparison shadow-only summary

```yaml
profile_comparison:
  P0_e2r_2_1_stock_web_calibrated_proxy:
    hypothesis: current profile with global Stage2 bridge and 4C guards
    eligible_trigger_count: 6
    stress_control_count: 1
    avg_MFE_90D_pct: 17.14
    avg_MAE_90D_pct: -11.92
    false_positive_risk: high_if_policy_or_price_rebound_rows_are_left_actionable
    verdict: adequate_only_with_C30_issuer_cash_bridge_gate
  P0b_e2r_2_0_baseline_reference:
    hypothesis: older profile pays too much for construction/PF rebound labels
    eligible_trigger_count: 6
    false_positive_rate: higher
    verdict: inferior
  P1_sector_specific_candidate_profile:
    hypothesis: L9 construction names require issuer-specific refinancing/cash bridge
    changed_axes: none_new_holdout_only
    verdict: pass_holdout
  P2_canonical_archetype_candidate_profile:
    hypothesis: C30 requires issuer cash bridge rather than PF umbrella
    changed_axes: none_new_holdout_only
    verdict: pass_holdout
  P3_counterexample_guard_profile:
    hypothesis: weak-liquidity rows route hard 4C and workout rows remain stress-control
    changed_axes: none_new_holdout_only
    verdict: strongest_for_false_positive_control
```

---

## 11. Coverage matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---:|
| L9_CONSTRUCTION_REALESTATE_HOUSING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | PF_REFINANCING_TO_ISSUER_CASH_BRIDGE_HOLDOUT_V106 | 3 | 2 | 4 | 1 | 0 | 7 | 6 | 0 | 4 | false | false | 27 |

---

## 12. Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 7
calibration_usable_trigger_count: 6
representative_trigger_count: 0
new_weight_evidence_candidate_count: 0
guardrail_candidate_count: 7
narrative_only_future_todo_count: 1
narrative_only_or_rejected_count: 2
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
batch_ingest_recommendation: dedupe_as_holdout_validation_only
```

---

## 13. Residual contribution summary

```yaml
new_independent_case_count: 0
reused_case_count: 7
reused_case_ids:
  - C30|000720|Stage2-Watch|2024-01-26
  - C30|047040|Stage2-Watch|2024-01-26
  - C30|002990|Stage4C|2024-01-26
  - C30|047040|Stage4B|2024-07-18
  - C30|294870|Stage4B|2024-05-13
  - C30|014790|Stage4B|2024-03-27
  - C30|009410|Stage2-Watch|2024-01-11
new_symbol_count: 0
new_trigger_family_count: 0
narrative_only_future_todo_count: 1
tested_existing_calibrated_axes:
  - stage2_required_bridge
  - local_4b_watch_guard
  - hard_4c_thesis_break_routes_to_4c
  - C30_PF_refinancing_to_issuer_cash_bridge
  - no_backfill_later_evidence
residual_error_types_found:
  - PF_policy_without_issuer_cash
  - delayed_rebound_backfill_risk
  - weak_liquidity_label_hard_break
  - workout_not_clean_equity_recovery
new_axis_proposed: null
existing_axis_strengthened:
  - C30_PF_REFINANCING_TO_ISSUER_CASH_BRIDGE_REQUIREMENT_V106_HELD_OUT
existing_axis_weakened: null
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
no_new_signal_reason: all rows reused holdout validation after additional C30 candidate shards returned cache miss
loop_contribution_label: duplicate_low_value_loop_with_cache_miss_todo
do_not_propose_new_weight_delta: true
```

```jsonl
{"row_type":"residual_contribution","round":"R10","loop":"106","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","new_independent_case_count":0,"reused_case_count":7,"new_symbol_count":0,"new_trigger_family_count":0,"narrative_only_future_todo_count":1,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","hard_4c_thesis_break_routes_to_4c","C30_PF_refinancing_to_issuer_cash_bridge","no_backfill_later_evidence"],"residual_error_types_found":["PF_policy_without_issuer_cash","delayed_rebound_backfill_risk","weak_liquidity_label_hard_break","workout_not_clean_equity_recovery"],"loop_contribution_label":"duplicate_low_value_loop_with_cache_miss_todo","do_not_propose_new_weight_delta":true}
```

---

## 14. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Treat this R10/C30 loop 106 as holdout validation only. Batch it with C30 loops 1~3 and 100~105 plus C31/R13 construction/PF guardrails. If exact same_entry_group_id rows already exist, dedupe them. Preserve the C30 PF-refinancing-to-issuer-cash bridge gate. Do not create a new weight delta from this loop because additional C30 symbol shards returned cache miss and no new independent case was added. Future research should reprice GS건설(006360), DL이앤씨(375500), 계룡건설(013580), 동부건설(005960) when stock-web shards are accessible.
```

---

## 15. Next research state

```yaml
completed_round: R10
completed_loop: 106
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
