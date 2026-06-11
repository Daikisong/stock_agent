# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R10
selected_loop: 109
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: PF_LIQUIDITY_BALANCE_SHEET_BREAK_HOLDOUT_V109_LARGE_BUILDER_SURVIVOR_WEAK_LIQUIDITY_DELAYED_REBOUND_SPLIT
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
  stock_web_manifest: read_ok
  direct_stock_web_shards:
    - 009410/2024: not_recomputed_this_turn_future_true_PF_workout_candidate
    - 034300/2024: not_recomputed_this_turn_future_true_PF_liquidity_candidate
    - 013580/2024: not_recomputed_this_turn_future_regional_builder_PF_candidate
    - 000720/2024: reused_from_prior_local_C30_loop_108_large_builder_survivor_row
    - 047040/2024: reused_from_prior_local_C30_loop_108_delayed_rebound_rows
    - 002990/2024: reused_from_prior_local_C30_loop_108_weak_liquidity_false_positive_row
    - 375500/2024: reused_from_prior_local_C30_loop_108_quality_builder_cap_row
    - 004960/2024: reused_from_prior_local_C30_loop_108_small_builder_watch_row
    - 006360/2024: reused_from_prior_local_C30_loop_108_EPC_boundary_4B
    - 028050/2024: reused_from_prior_local_C30_loop_108_pure_EPC_reclassify_row
    - 014790/2024: not_recomputed_this_turn_future_PF_liquidity_candidate
    - 001470/2024: not_recomputed_this_turn_future_weak_builder_liquidity_candidate
    - 002410/2024: not_recomputed_this_turn_future_small_builder_PF_candidate
    - 003070/2024: not_recomputed_this_turn_future_construction_PF_candidate
    - 002150/2024: not_recomputed_this_turn_C05_engineering_boundary
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
loop_objective:
  - holdout_validation
  - duplicate_low_value_loop_marker
  - PF_liquidity_balance_sheet_survivor_vs_weak_liquidity_decay_gate
  - large_builder_survivor_low_MAE_positive_control
  - weak_builder_PF_label_false_positive_guard
  - delayed_rebound_no_backfill_guard
  - EPC_wrong_archetype_reclassification_guard
price_source: Songdaiki/stock-web
price_data_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

`C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK` remains Priority 0 in the no-repeat index. The current index shows only 3 representative rows for C30, so C30 remains one of the lowest-coverage archetypes. The v12 scheduler maps C30 to `R10 / L9_CONSTRUCTION_REALESTATE_HOUSING`.

This file continues the local C30 sequence after `R10/C30 loop 108`; selected loop is therefore `109`.

This is a **dedupe-aware holdout validation / cache-miss TODO** MD. It does not claim fresh independent stock-web evidence. Direct fresh C30 true-PF-break/workout/liquidity-stress candidate shards were not recomputed in this execution, so the trigger rows below reuse previously generated stock-web-derived C30/C05 boundary rows with complete 30D/90D/180D MFE and MAE. Exact duplicate `same_entry_group_id` rows should be deduped during batch ingest. No production scoring is changed.

---

## 1. Research thesis

```yaml
loop_109_note:
  independence_status: duplicate_holdout_only
  fresh_reprice_status: not_recomputed_this_execution
  reason: C30 remains one of the lowest-row Priority 0 archetypes, but this run reuses prior C30/C05 boundary rows and must not create a new weight delta.
```


C30 is not a generic construction rebound bucket. It is the balance-sheet plumbing archetype:

```text
PF exposure / liquidity stress / unsold inventory / receivable risk / project cost-to-complete
→ refinancing or guarantee path
→ cash collection from projects
→ inventory and receivable normalization
→ impairment / cost overrun containment
→ balance-sheet survivability
→ margin recovery
→ price path validation
```

The recurring false positive is:

```text
large-builder support label
low-PBR construction rebound
policy support headline
EPC order headline
quality balance-sheet label
PF relief vocabulary without refinancing/cash proof
```

A construction company can look like a bargain while the pipes are clogged. C30 should ask whether the cash can actually pass through PF maturities, receivables, unsold units and project completion costs. If the bridge is only “cheap builder” or “support expected,” the score should cap or route to 4C.

The C30 route split in this holdout:

```text
large-builder survivor with bounded MAE
→ Stage2 can survive, but not Green

delayed sector rebound
→ local 4B / Watch; do not backfill as immediate Stage2 if entry-date PF cash bridge was absent

weak-liquidity builder after PF-relief vocabulary
→ Stage2 false-positive / hard watch guard

quality-builder label without project cash
→ Stage2 cap

EPC headline or overseas project award
→ reclassify to C05 unless PF/balance-sheet repair dominates

small-builder support beta
→ Watch only until refinancing / unsold inventory / project cash proof
```

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 8
  actual_trigger_rows: 8
  narrative_only_future_todo_rows: 1
  source_archetypes:
    - C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
    - C05_EPC_MEGA_CONTRACT_MARGIN_GAP
    - C31_POLICY_SUBSIDY_LEGISLATION_EVENT
    - R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
    - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
    - R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
    - R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
  price_windows:
    - 30D MFE/MAE
    - 90D MFE/MAE
    - 180D MFE/MAE
  output_use:
    - C30 holdout validation
    - PF/liquidity weak-builder false-positive guard
    - delayed-rebound no-backfill guard
    - EPC wrong-archetype reclassification guard
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
  - R10/C30 loop 100
  - R10/C30 loop 107
  - R10/C30 loop 108
  - R1/C05 loops 111/114/115/116
  - R13 accounting-trust loops 12~14
  - R13 Stage2 false-positive loop 11
  - R13 high-MAE loop 9
  - R13 4B/4C loop 104
reason:
  - direct fresh C30 true-PF-break/workout/liquidity-stress candidate shards were not recomputed in this execution
  - reused rows already contain complete 30D/90D/180D MFE and MAE
  - this file is holdout validation / duplicate-low-value evidence only
  - no row should create new production weight delta
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","selected_round":"R10","selected_loop":109,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"LARGE_BUILDER_BALANCE_SHEET_SURVIVOR_LOW_MAE","symbol":"000720","name":"현대건설","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-25","entry_date":"2024-01-26","entry_price":33100,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.30,"MAE_30D_pct":-3.50,"MFE_90D_pct":8.80,"MAE_90D_pct":-5.70,"MFE_180D_pct":8.80,"MAE_180D_pct":-12.20,"forward_high_90d":36000,"forward_low_90d":31200,"peak_date":"2024-05-09","peak_price":36000,"drawdown_after_peak_pct":-19.30,"corporate_action_window_status":"clean_180D_window","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C30|000720|Stage2-Actionable|2024-01-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_large_builder_survivor","reuse_reason":"same Hyundai E&C survivor row from C30 loop 100","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"large_builder_survivor_low_MAE_positive","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|000720|Stage2-Actionable|2024-01-26","non_price_bridge":"large-builder balance-sheet survivor and order-quality bridge visible by Jan-2024","score_alignment":"Stage2 can survive, but modest MFE and later drawdown block Green"}
{"row_type":"trigger","selected_round":"R10","selected_loop":109,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"BUILDER_DELAYED_REBOUND_AFTER_PF_RELIEF","symbol":"047040","name":"대우건설","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-25","entry_date":"2024-01-26","entry_price":4015,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.60,"MAE_30D_pct":-5.60,"MFE_90D_pct":2.60,"MAE_90D_pct":-10.80,"MFE_180D_pct":23.70,"MAE_180D_pct":-12.30,"forward_high_180d":4965,"forward_low_180d":3520,"peak_date":"2024-07-18","peak_price":4965,"drawdown_after_peak_pct":-29.10,"corporate_action_window_status":"clean_180D_window","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C30|047040|Stage2-Actionable|2024-01-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_delayed_positive","reuse_reason":"same Daewoo E&C delayed rebound row from C30 loop 100","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"builder_delayed_rebound","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|047040|Stage2-Actionable|2024-01-26","non_price_bridge":"PF relief and order/margin bridge partially visible, but price validation arrived late","score_alignment":"Stage2/Watch can survive, but delayed rebound must not be backfilled as immediate Green"}
{"row_type":"trigger","selected_round":"R10","selected_loop":109,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"WEAK_LIQUIDITY_BUILDER_PF_LABEL_FALSE_POSITIVE","symbol":"002990","name":"금호건설","trigger_type":"Stage2-FalsePositive","trigger_date":"2024-01-25","entry_date":"2024-01-26","entry_price":5030,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.00,"MAE_30D_pct":-4.60,"MFE_90D_pct":5.00,"MAE_90D_pct":-27.50,"MFE_180D_pct":5.00,"MAE_180D_pct":-41.00,"peak_date":"2024-02-01","peak_price":5280,"drawdown_after_peak_pct":-47.00,"corporate_action_window_status":"clean_180D_window","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C30|002990|Stage2-FalsePositive|2024-01-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_weak_liquidity_false_positive","reuse_reason":"same weak-liquidity PF false-positive row from C30 loop 100","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"weak_liquidity_decay_false_positive","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|002990|Stage2-FalsePositive|2024-01-26","non_price_bridge":"weak-liquidity builder exposed to PF/real-estate balance-sheet concern; relief vocabulary did not become cash bridge","score_alignment":"false-positive block; MAE90 and MAE180 show PF label failed"}
{"row_type":"trigger","selected_round":"R10","selected_loop":109,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PRICE_SPIKE_LOCAL_4B_WATCH_AFTER_PF_REBOUND","symbol":"047040","name":"대우건설","trigger_type":"Stage4B","trigger_date":"2024-07-18","entry_date":"2024-07-18","entry_price":4250,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":16.80,"MAE_30D_pct":-16.60,"MFE_90D_pct":16.80,"MAE_90D_pct":-17.20,"MFE_180D_pct":16.80,"MAE_180D_pct":-30.80,"peak_date":"2024-07-18","peak_price":4965,"drawdown_after_peak_pct":-40.80,"corporate_action_window_status":"clean_180D_window","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C30|047040|Stage4B|2024-07-18","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_4B_peak_overlay","reuse_reason":"same Daewoo E&C 4B overlay row from C30 loop 100","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"local_4B_peak_after_rebound","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|047040|Stage4B|2024-07-18","non_price_bridge":"price spike after delayed construction rebound; non-price PF cash bridge was not refreshed at entry","score_alignment":"local 4B / no-backfill; price-only rebound spike should not be promoted"}
{"row_type":"trigger","selected_round":"R10","selected_loop":109,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"QUALITY_BUILDER_LABEL_WITHOUT_PROJECT_CASH_BRIDGE_CAP","symbol":"375500","name":"DL이앤씨","trigger_type":"Stage2-Watch","entry_date":"2024-05-13","entry_price":34650,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.90,"MAE_30D_pct":-4.04,"MFE_90D_pct":14.00,"MAE_90D_pct":-17.46,"MFE_180D_pct":14.00,"MAE_180D_pct":-17.46,"forward_high_90d":39500,"forward_low_90d":28600,"corporate_action_window_status":"not_flagged_in_prior_local_validation","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C30|375500|Stage2-Watch|2024-05-13","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_quality_label_cap","reuse_reason":"same DL E&C quality-builder cap row from C30 loop 107","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"quality_builder_balance_sheet_cap","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|375500|Stage2-Watch|2024-05-13","non_price_bridge":"quality/balance-sheet label without fresh project cash collection or PF relief proof","score_alignment":"cap Stage2-Actionable; require PF exposure, project receivables, unsold inventory and cash bridge"}
{"row_type":"trigger","selected_round":"R10","selected_loop":109,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"SMALL_BUILDER_SUPPORT_BETA_MODEST_MFE_WATCH_ONLY","symbol":"004960","name":"한신공영","trigger_type":"Stage2-Watch","entry_date":"2024-03-27","entry_price":6720,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.48,"MAE_30D_pct":-8.33,"MFE_90D_pct":8.48,"MAE_90D_pct":-8.33,"MFE_180D_pct":18.60,"MAE_180D_pct":-8.63,"forward_high_180d":7970,"forward_low_180d":6140,"corporate_action_window_status":"not_flagged_in_prior_local_validation","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C30|004960|Stage2-Watch|2024-03-27","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_small_builder_watch","reuse_reason":"same Hanshin E&C support-beta row from C30 loop 107","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"small_builder_support_watch","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|004960|Stage2-Watch|2024-03-27","non_price_bridge":"small/mid-builder support beta without clear refinancing, PF exposure relief or cash collection bridge","score_alignment":"Stage2-Watch only; require refinancing, unsold inventory and project cash proof"}
{"row_type":"trigger","selected_round":"R10","selected_loop":109,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"EPC_AWARD_DELAYED_REBOUND_BOUNDARY_NOT_CLEAN_C30_LOCAL_4B","symbol":"006360","name":"GS건설","trigger_type":"Stage4B","entry_date":"2024-04-03","entry_price":15630,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.97,"MAE_30D_pct":-10.17,"MFE_90D_pct":6.97,"MAE_90D_pct":-10.17,"MFE_180D_pct":39.16,"MAE_180D_pct":-10.17,"forward_high_180d":21750,"forward_low_180d":14040,"corporate_action_window_status":"not_flagged_in_prior_local_validation","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C30|006360|Stage4B|2024-04-03","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_EPC_boundary_4B","reuse_reason":"same GS E&C EPC/PF boundary row from C30 loop 107","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"EPC_boundary_delayed_rebound_4B","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|006360|Stage4B|2024-04-03","non_price_bridge":"Fadhili EPC award and delayed rebound; not clean C30 unless domestic PF/liquidity repair also proven","score_alignment":"local 4B boundary; reclassify to C05 unless PF/balance-sheet repair is dominant"}
{"row_type":"trigger","selected_round":"R10","selected_loop":109,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PURE_EPC_AWARD_WRONG_ARCHETYPE_C05_RECLASSIFICATION_CAP","symbol":"028050","name":"삼성E&A","trigger_type":"Stage2-Watch","entry_date":"2024-04-03","entry_price":25300,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.72,"MAE_30D_pct":-5.34,"MFE_90D_pct":6.72,"MAE_90D_pct":-14.62,"MFE_180D_pct":10.47,"MAE_180D_pct":-14.62,"forward_high_180d":27950,"forward_low_180d":21600,"corporate_action_window_status":"not_flagged_in_prior_local_validation","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C30|028050|Stage2-Watch|2024-04-03","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_wrong_archetype_C05","reuse_reason":"same Samsung E&A pure EPC row from C30/C05 boundary files","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"pure_EPC_wrong_archetype_C05","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|028050|Stage2-Watch|2024-04-03","non_price_bridge":"pure overseas EPC award headline; no domestic PF, liquidity, unsold inventory or construction balance-sheet break evidence","score_alignment":"cap C30 and reclassify to C05 EPC margin gap; not a PF balance-sheet repair row"}
```

---

## 5. Narrative-only future TODO

```jsonl
{"row_type":"narrative_only_future_todo","selected_round":"R10","selected_loop":109,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_TRUE_PF_BREAK_REPRICE_TODO_AFTER_CACHE_MISS_V108","candidate_symbols":["009410","034300","013580","014790","001470","002990","002410","003070","002150"],"candidate_names":["태영건설","신세계건설","계룡건설","HL D&I","삼부토건","금호건설","범양건영","코오롱글로벌","도화엔지니어링-boundary"],"why_not_trigger_row_now":"fresh stock-web symbol-year shards for true PF-break/workout/liquidity stress cases were not recomputed in this execution; no fresh 30D/90D/180D MFE/MAE computed here","calibration_usable":false,"score_alignment":"future run should compute stock-web windows before counting these as new C30 evidence; distinguish PF hard break, workout and liquidity stress from generic construction rebound or C05 EPC order headlines"}
```

---

## 6. Case analysis

### 6.1 Large-builder survivor versus weak-liquidity builder

```yaml
survivor_positive:
  - 000720: low MAE but modest MFE; Stage2 only, not Green.

weak_liquidity_false_positive:
  - 002990: low MFE, deep MAE, prolonged decay.
```

This split is the core of C30. A balance-sheet survivor may deserve Stage2, but a weak-liquidity builder with PF-relief vocabulary should not. The same headline can be medicine for one balance sheet and water for another.

### 6.2 Delayed rebound / no-backfill

```yaml
delayed_rebound:
  - 047040 Jan entry: delayed 180D rebound but weak 90D validation.
  - 047040 Jul overlay: local 4B peak, price-only.
```

The delayed rebound rows show why C30 should avoid backfilling. A later sector move does not prove that the entry-date PF cash bridge existed.

### 6.3 Quality-builder label and small-builder support

```yaml
cap_rows:
  - 375500: quality label without project cash.
  - 004960: small-builder support beta without refinancing proof.
```

Quality or support can lower risk, but C30 needs project cash collection and refinancing evidence before promotion.

### 6.4 EPC boundary rows

```yaml
C05_boundary:
  - 006360: EPC award plus delayed rebound, local 4B boundary.
  - 028050: pure overseas EPC award, reclassify C05.
```

These rows protect C30 from stealing EPC evidence. If the economic bridge is contract margin and working capital, C05 is the sharper bucket.

---

## 7. Score-return alignment

```yaml
new_independent_case_count: 0
reused_case_count: 8
new_symbol_count: 0
same_archetype_new_symbol_count: 0
same_archetype_new_trigger_family_count: 0
new_trigger_family_count: 0
narrative_only_future_todo_count: 1
calibration_usable_case_count: 8
calibration_usable_trigger_count: 8
positive_case_count: 2
counterexample_count: 6
local_4B_watch_count: 3
hard_or_false_positive_count: 1
wrong_archetype_reclassification_count: 2
current_profile_error_count: 5
diversity_score_summary: "large-builder survivor, delayed rebound, weak-liquidity false positive, quality-label cap, small-builder support watch, EPC boundary reclassification covered"
loop_contribution_label: duplicate_low_value_loop_with_cache_miss_todo
do_not_propose_new_weight_delta: true
```

| symbol | role | 90D MFE/MAE | 180D MFE/MAE | C30 lesson |
|---|---:|---:|---:|---|
| 000720 | large-builder survivor | +8.80 / -5.70 | +8.80 / -12.20 | survivor yes, Green no |
| 047040 | delayed rebound | +2.60 / -10.80 | +23.70 / -12.30 | do not backfill |
| 002990 | weak liquidity false positive | +5.00 / -27.50 | +5.00 / -41.00 | PF label failed |
| 047040 | local 4B peak | +16.80 / -17.20 | +16.80 / -30.80 | price-only spike |
| 375500 | quality cap | +14.00 / -17.46 | +14.00 / -17.46 | project cash needed |
| 004960 | support watch | +8.48 / -8.33 | +18.60 / -8.63 | refinancing proof needed |
| 006360 | EPC boundary 4B | +6.97 / -10.17 | +39.16 / -10.17 | C05 unless PF dominates |
| 028050 | pure EPC reclassify | +6.72 / -14.62 | +10.47 / -14.62 | not C30 |

---

## 8. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"000720","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"PF_refinancing_bridge":2,"project_cash_collection":2,"unsold_inventory_relief":2,"receivable_quality":2,"balance_sheet_survivability":4,"margin_recovery":1,"relative_strength":2,"policy_support":2,"execution_risk":2,"accounting_trust_risk":3},"weighted_score_before":70,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"PF_refinancing_bridge":2,"project_cash_collection":1,"unsold_inventory_relief":1,"receivable_quality":2,"balance_sheet_survivability":4,"margin_recovery":1,"relative_strength":1,"policy_support":1,"execution_risk":3,"accounting_trust_risk":4},"weighted_score_after":63,"stage_label_after":"Stage2_Actionable_GreenBlocked","changed_components":["project_cash_collection","unsold_inventory_relief","relative_strength","policy_support","execution_risk","accounting_trust_risk"],"component_delta_explanation":"Large-builder survivor status held drawdown in check, but MFE was modest and project cash evidence was not enough for Green.","MFE_90D_pct":8.80,"MAE_90D_pct":-5.70,"score_return_alignment_label":"large_builder_survivor_low_MAE","current_profile_verdict":"current_profile_correct_if_green_blocked"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"047040","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"PF_refinancing_bridge":2,"project_cash_collection":1,"unsold_inventory_relief":1,"receivable_quality":2,"balance_sheet_survivability":3,"margin_recovery":2,"relative_strength":1,"policy_support":2,"execution_risk":3,"accounting_trust_risk":4},"weighted_score_before":68,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"PF_refinancing_bridge":2,"project_cash_collection":1,"unsold_inventory_relief":1,"receivable_quality":2,"balance_sheet_survivability":3,"margin_recovery":1,"relative_strength":1,"policy_support":1,"execution_risk":4,"accounting_trust_risk":4},"weighted_score_after":60,"stage_label_after":"Stage2_Watch_delayed_rebound","changed_components":["margin_recovery","policy_support","execution_risk"],"component_delta_explanation":"The 180D rebound arrived late; entry-date 90D path was weak, so this should not be backfilled as early Green.","MFE_90D_pct":2.60,"MAE_90D_pct":-10.80,"score_return_alignment_label":"delayed_rebound_no_backfill","current_profile_verdict":"current_profile_correct_if_watch_or_4B"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"002990","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"PF_refinancing_bridge":1,"project_cash_collection":0,"unsold_inventory_relief":0,"receivable_quality":0,"balance_sheet_survivability":1,"margin_recovery":0,"relative_strength":1,"policy_support":2,"execution_risk":5,"accounting_trust_risk":5},"weighted_score_before":58,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"PF_refinancing_bridge":0,"project_cash_collection":0,"unsold_inventory_relief":0,"receivable_quality":0,"balance_sheet_survivability":0,"margin_recovery":0,"relative_strength":0,"policy_support":0,"execution_risk":5,"accounting_trust_risk":5},"weighted_score_after":32,"stage_label_after":"Stage2_FalsePositive_Block","changed_components":["PF_refinancing_bridge","balance_sheet_survivability","relative_strength","policy_support"],"component_delta_explanation":"PF relief vocabulary did not repair weak liquidity; MAE90 and MAE180 reject Stage2.","MFE_90D_pct":5.00,"MAE_90D_pct":-27.50,"score_return_alignment_label":"weak_liquidity_false_positive","current_profile_verdict":"current_profile_false_positive_if_stage2"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"047040","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"PF_refinancing_bridge":1,"project_cash_collection":0,"unsold_inventory_relief":1,"receivable_quality":1,"balance_sheet_survivability":2,"margin_recovery":1,"relative_strength":4,"policy_support":1,"execution_risk":5,"accounting_trust_risk":4},"weighted_score_before":64,"stage_label_before":"Stage4B","raw_component_scores_after":{"PF_refinancing_bridge":0,"project_cash_collection":0,"unsold_inventory_relief":0,"receivable_quality":1,"balance_sheet_survivability":2,"margin_recovery":0,"relative_strength":2,"policy_support":0,"execution_risk":5,"accounting_trust_risk":5},"weighted_score_after":48,"stage_label_after":"Stage4B_price_spike_watch","changed_components":["PF_refinancing_bridge","unsold_inventory_relief","margin_recovery","relative_strength","policy_support","accounting_trust_risk"],"component_delta_explanation":"July rebound spike was a local peak with weak non-price evidence; keep 4B watch.","MFE_90D_pct":16.80,"MAE_90D_pct":-17.20,"score_return_alignment_label":"local_4B_peak_no_backfill","current_profile_verdict":"current_profile_correct_if_4B"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"375500","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"PF_refinancing_bridge":1,"project_cash_collection":1,"unsold_inventory_relief":1,"receivable_quality":2,"balance_sheet_survivability":4,"margin_recovery":1,"relative_strength":2,"policy_support":1,"execution_risk":3,"accounting_trust_risk":4},"weighted_score_before":64,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"PF_refinancing_bridge":0,"project_cash_collection":0,"unsold_inventory_relief":0,"receivable_quality":1,"balance_sheet_survivability":3,"margin_recovery":0,"relative_strength":1,"policy_support":0,"execution_risk":3,"accounting_trust_risk":5},"weighted_score_after":45,"stage_label_after":"Stage2_cap","changed_components":["PF_refinancing_bridge","project_cash_collection","unsold_inventory_relief","receivable_quality","balance_sheet_survivability","margin_recovery","relative_strength","policy_support","accounting_trust_risk"],"component_delta_explanation":"Quality-builder label lacked direct PF/inventory/receivable cash bridge.","MFE_90D_pct":14.00,"MAE_90D_pct":-17.46,"score_return_alignment_label":"quality_builder_label_cap","current_profile_verdict":"current_profile_false_positive_if_actionable"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"004960","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"PF_refinancing_bridge":1,"project_cash_collection":0,"unsold_inventory_relief":1,"receivable_quality":1,"balance_sheet_survivability":2,"margin_recovery":0,"relative_strength":2,"policy_support":2,"execution_risk":3,"accounting_trust_risk":4},"weighted_score_before":60,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"PF_refinancing_bridge":0,"project_cash_collection":0,"unsold_inventory_relief":0,"receivable_quality":1,"balance_sheet_survivability":1,"margin_recovery":0,"relative_strength":1,"policy_support":1,"execution_risk":3,"accounting_trust_risk":5},"weighted_score_after":45,"stage_label_after":"Stage2_Watch_contribution_cap","changed_components":["PF_refinancing_bridge","unsold_inventory_relief","balance_sheet_survivability","relative_strength","policy_support","accounting_trust_risk"],"component_delta_explanation":"Support beta lacked refinancing and project cash proof.","MFE_90D_pct":8.48,"MAE_90D_pct":-8.33,"score_return_alignment_label":"small_builder_support_watch","current_profile_verdict":"current_profile_correct_if_watch"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"006360","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"PF_refinancing_bridge":1,"project_cash_collection":0,"unsold_inventory_relief":1,"receivable_quality":1,"balance_sheet_survivability":2,"margin_recovery":1,"relative_strength":2,"policy_support":1,"execution_risk":4,"accounting_trust_risk":4},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"PF_refinancing_bridge":0,"project_cash_collection":0,"unsold_inventory_relief":0,"receivable_quality":1,"balance_sheet_survivability":1,"margin_recovery":1,"relative_strength":2,"policy_support":0,"execution_risk":4,"accounting_trust_risk":4},"weighted_score_after":59,"stage_label_after":"Stage4B_C05_boundary","changed_components":["PF_refinancing_bridge","unsold_inventory_relief","balance_sheet_survivability","policy_support"],"component_delta_explanation":"Delayed rebound belongs more to EPC/C05 unless PF repair evidence dominates.","MFE_90D_pct":6.97,"MAE_90D_pct":-10.17,"score_return_alignment_label":"EPC_boundary_not_clean_C30","current_profile_verdict":"requires_C05_reclassification_or_PF_evidence"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"028050","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"PF_refinancing_bridge":0,"project_cash_collection":0,"unsold_inventory_relief":0,"receivable_quality":1,"balance_sheet_survivability":2,"margin_recovery":2,"relative_strength":1,"policy_support":1,"execution_risk":4,"accounting_trust_risk":3},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"PF_refinancing_bridge":0,"project_cash_collection":0,"unsold_inventory_relief":0,"receivable_quality":0,"balance_sheet_survivability":0,"margin_recovery":0,"relative_strength":0,"policy_support":0,"execution_risk":3,"accounting_trust_risk":3},"weighted_score_after":42,"stage_label_after":"Reclassify_C05","changed_components":["receivable_quality","balance_sheet_survivability","margin_recovery","relative_strength","policy_support","execution_risk"],"component_delta_explanation":"Pure overseas EPC award is not domestic PF balance-sheet repair.","MFE_90D_pct":6.72,"MAE_90D_pct":-14.62,"score_return_alignment_label":"pure_EPC_wrong_archetype_C05","current_profile_verdict":"requires_reclassification"}
```

---

## 9. Current calibrated profile stress test

The C30 PF/liquidity balance-sheet break gate held:

```text
large-builder survivor with bounded drawdown
→ Stage2 can survive, but no Green

delayed rebound
→ 4B / Watch; do not backfill later sector recovery

weak-liquidity builder with PF relief vocabulary
→ false-positive block

quality label
→ cap until project cash appears

small-builder support beta
→ Watch only

EPC award rows
→ reclassify C05 unless PF repair dominates
```

### Rule candidate retained, not newly proposed

```text
C30_PF_LIQUIDITY_BALANCE_SHEET_BREAK_SURVIVOR_VS_WEAK_DECAY_GATE_V109_HELD_OUT

if C30
and construction_lowPBR_support_rebound_or_quality_label == true
and PF_refinancing_unsold_inventory_receivable_project_cash_or_balance_sheet_survivability_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C30
and large_builder_survivor_low_MAE == true
and MFE_90D_pct < +15:
    keep_stage2_watch_or_actionable = true
    block_stage3_green_until_project_cash_refresh = true
```

```text
if C30
and weak_liquidity_builder == true
and MFE_90D_pct < +10
and MAE_90D_pct <= -20:
    route = Stage2_FalsePositive_Block
```

```text
if C30
and delayed_rebound_after_90D_or_180D == true
and entry_date_PF_cash_bridge == false:
    route = local_4B_or_watch
    do_not_backfill_as_immediate_Stage2_Actionable = true
```

```text
if C30
and EPC_contract_margin_bridge_dominates == true:
    cap_C30_contribution = true
    require_reclassification_to_C05 = true
```

---

## 10. Profile comparison shadow-only summary

```yaml
profile_comparison:
  P0_e2r_2_2_rolling_calibrated_proxy:
    hypothesis: current rolling profile with bridge/4B/4C guards
    eligible_trigger_count: 8
    avg_MFE_90D_pct: 8.93
    avg_MAE_90D_pct: -13.48
    false_positive_risk: high_if_support_or_quality_labels_are_left_actionable
    verdict: adequate_only_with_C30_PF_cash_bridge_and_weak_liquidity_guard
  P0b_e2r_2_1_reference:
    hypothesis: prior profile likely overcredits construction support/rebound labels
    eligible_trigger_count: 8
    false_positive_risk: higher
    verdict: inferior
  P1_sector_specific_candidate_profile:
    hypothesis: L9 construction rows require PF/liquidity/inventory/cash bridge
    changed_axes: none_new_holdout_only
    verdict: pass_holdout
  P2_canonical_archetype_candidate_profile:
    hypothesis: C30 requires balance-sheet plumbing repair, not generic construction rebound
    changed_axes: none_new_holdout_only
    verdict: pass_holdout
  P3_counterexample_guard_profile:
    hypothesis: weak-liquidity and EPC wrong-archetype rows route to block/reclassify
    changed_axes: none_new_holdout_only
    verdict: strongest_for_false_positive_control
```

---

## 11. Coverage matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_or_false_positive_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---:|
| L9_CONSTRUCTION_REALESTATE_HOUSING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | PF_LIQUIDITY_BALANCE_SHEET_BREAK_HOLDOUT_V109 | 2 | 6 | 3 | 1 | 0 | 8 | 8 | 0 | 5 | false | false | 27 |

---

## 12. Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 8
calibration_usable_trigger_count: 8
representative_trigger_count: 0
new_weight_evidence_candidate_count: 0
guardrail_candidate_count: 8
narrative_only_future_todo_count: 1
narrative_only_or_rejected_count: 1
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
reused_case_count: 8
reused_case_ids:
  - C30|000720|Stage2-Actionable|2024-01-26
  - C30|047040|Stage2-Actionable|2024-01-26
  - C30|002990|Stage2-FalsePositive|2024-01-26
  - C30|047040|Stage4B|2024-07-18
  - C30|375500|Stage2-Watch|2024-05-13
  - C30|004960|Stage2-Watch|2024-03-27
  - C30|006360|Stage4B|2024-04-03
  - C30|028050|Stage2-Watch|2024-04-03
new_symbol_count: 0
new_trigger_family_count: 0
narrative_only_future_todo_count: 1
tested_existing_calibrated_axes:
  - stage2_required_bridge
  - local_4b_watch_guard
  - hard_4c_thesis_break_routes_to_4c
  - C30_PF_liquidity_balance_sheet_break_gate
  - C05_EPC_reclassification_guard
residual_error_types_found:
  - weak_liquidity_builder_false_positive
  - delayed_rebound_backfill_risk
  - quality_builder_label_without_project_cash
  - small_builder_support_without_refinancing_cash
  - EPC_headline_wrong_archetype
  - true_PF_break_reprice_gap
new_axis_proposed: null
existing_axis_strengthened:
  - C30_PF_LIQUIDITY_BALANCE_SHEET_BREAK_SURVIVOR_VS_WEAK_DECAY_GATE_V109_HELD_OUT
existing_axis_weakened: null
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
no_new_signal_reason: all rows reused holdout validation after direct fresh C30 true-PF-break/workout/liquidity-stress candidate shards were not recomputed
loop_contribution_label: duplicate_low_value_loop_with_cache_miss_todo
do_not_propose_new_weight_delta: true
```

```jsonl
{"row_type":"residual_contribution","round":"R10","loop":"109","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","new_independent_case_count":0,"reused_case_count":8,"new_symbol_count":0,"new_trigger_family_count":0,"narrative_only_future_todo_count":1,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","hard_4c_thesis_break_routes_to_4c","C30_PF_liquidity_balance_sheet_break_gate","C05_EPC_reclassification_guard"],"residual_error_types_found":["weak_liquidity_builder_false_positive","delayed_rebound_backfill_risk","quality_builder_label_without_project_cash","small_builder_support_without_refinancing_cash","EPC_headline_wrong_archetype","true_PF_break_reprice_gap"],"loop_contribution_label":"duplicate_low_value_loop_with_cache_miss_todo","do_not_propose_new_weight_delta":true}
```

---

## 14. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Treat this R10/C30 loop 109 as holdout validation only. Batch it with C30 loops 100~108, C05 EPC boundary files, and R13 accounting-trust / Stage2 false-positive / high-MAE / 4B-4C guardrails. If exact same_entry_group_id rows already exist, dedupe them. Preserve the C30 PF/liquidity/balance-sheet break gate, weak-liquidity false-positive guard, delayed rebound no-backfill rule, and C05 EPC reclassification guard, but do not create a new weight delta from this loop because no new independent case was added. Future research should directly reprice 태영건설(009410), 신세계건설(034300), 계룡건설(013580), HL D&I(014790), 삼부토건(001470), 금호건설(002990), 범양건영(002410), 코오롱글로벌(003070), 도화엔지니어링(002150), 동부건설(005960), 남광토건(001260), 일성건설(013360) when stock-web shards are accessible.
```

---

## 15. Next research state

```yaml
completed_round: R10
completed_loop: 109
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C31_POLICY_SUBSIDY_LEGISLATION_EVENT
  - C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
  - C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
  - C15_MATERIAL_SPREAD_SUPERCYCLE
  - C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
```
