# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R10
selected_loop: 107
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: PF_LIQUIDITY_BALANCE_SHEET_BREAK_VS_BARGAIN_REBOUND_HOLDOUT_V107_BUILDER_QUALITY_SUPPORT_EPC_BOUNDARY_SPLIT
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
  stock_web_manifest: read_ok
  direct_stock_web_shards:
    - 294870/2024: reused_from_prior_local_C05_C30_boundary_row
    - 047040/2024: reused_from_prior_local_C05_C30_boundary_row
    - 375500/2024: reused_from_prior_local_C05_C30_boundary_row
    - 000720/2024: reused_from_prior_local_C05_C30_boundary_row
    - 004960/2024: reused_from_prior_local_C05_C30_boundary_row
    - 006360/2024: reused_from_prior_local_C05_C30_boundary_row
    - 028050/2024: reused_as_wrong_archetype_boundary
    - additional_PF_break_candidates: not_recomputed_this_turn
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
loop_objective:
  - holdout_validation
  - duplicate_low_value_loop_marker
  - PF_liquidity_balance_sheet_break_vs_bargain_rebound_gate
  - construction_support_label_false_positive_guard
  - delayed_rebound_no_backfill_guard
  - EPC_C05_boundary_reclassification_guard
  - source_proxy_reprice_todo_for_true_PF_break_names
price_source: Songdaiki/stock-web
price_data_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

`C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK` remains a Priority 0 archetype. The current no-repeat index marks C30 at only 3 representative rows, so it is one of the lowest-coverage canonical archetypes. The v12 scheduler maps C30 to `R10 / L9_CONSTRUCTION_REALESTATE_HOUSING`.

This file continues the local C30 construction/PF sequence after previously referenced `R10/C30 loops 102~106`; selected loop is therefore `107`.

This is a **dedupe-aware holdout validation / cache-miss TODO** MD. It does not claim fresh independent stock-web evidence. The trigger rows below reuse current-session stock-web-derived construction/PF boundary rows that already contain complete 30D/90D/180D MFE and MAE from `Songdaiki/stock-web` tradable OHLC. Additional true PF-break candidates were not recomputed in this execution and are kept as future TODO rows. Exact duplicate `same_entry_group_id` rows should be deduped during batch ingest. No production scoring is changed.

---

## 1. Research thesis

C30 should not reward `construction rebound`, `low PBR builder`, or `government support` as labels.

C30 is the PF and balance-sheet break archetype:

```text
PF exposure / liquidity stress / unsold inventory / receivable risk / debt maturity / construction support
→ balance-sheet survivability
→ refinancing or guarantee path
→ inventory and project cash collection
→ impairment / cost overrun / working-capital relief
→ margin recovery
→ price path validation
```

The recurring false positive is:

```text
large builder support label
cheap PBR
delayed sector rebound
EPC order headline
quality balance-sheet label
housing policy headline
```

A PF crisis is not a valuation problem first; it is a plumbing problem. Cash must pass through project finance, receivables, unsold units, refinancing windows and cost-to-complete. A cheap builder can stay cheap if the pipe is clogged. C30 scores the unclogging, not the sign saying “cheap.”

The C30 route split:

```text
PF/balance-sheet stress repaired + inventory/cash collection visible
→ Stage2 may survive

delayed construction rebound without entry-date cash repair
→ local 4B / no-backfill

quality builder label without project cash evidence
→ Stage2-Watch cap

large-builder support label with low MFE and deep 180D MAE
→ Stage2 false-positive block

EPC mega contract bridge
→ reclassify to C05 unless PF/balance-sheet evidence dominates

small-builder support beta without refinancing/cash proof
→ Watch only

true PF hard break / workout / liquidity event
→ future direct reprice required; do not infer without stock-web window
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
    - PF balance-sheet break vs bargain rebound split
    - delayed rebound no-backfill guard
    - C05 EPC boundary reclassification guard
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
  - R1/C05 loop 111
  - R1/C05 loop 114
  - R1/C05 loop 115
  - R10/C30 loops 102~106
  - R13 accounting-trust loops 12~14
  - R13 Stage2 false-positive loop 11
  - R13 high-MAE loop 9
  - R13 4B/4C loop 104
reason:
  - all reused rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - direct fresh true-PF-break candidate shards were unavailable or not recomputed in this execution
  - exact duplicate C30 keys should be deduped during batch ingest
  - this file is holdout validation / duplicate-low-value evidence only
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","selected_round":"R10","selected_loop":107,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"DELAYED_PROJECT_REBOUND_WITH_BALANCE_SHEET_REPAIR_WATCH_POSITIVE","symbol":"294870","name":"HDC현대산업개발","trigger_type":"Stage2-Actionable","entry_date":"2024-05-13","entry_price":17920,"entry_close":17920,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.12,"MAE_30D_pct":-6.58,"MFE_90D_pct":37.28,"MAE_90D_pct":-6.58,"MFE_180D_pct":57.37,"MAE_180D_pct":-6.58,"forward_high_30d":18300,"forward_low_30d":16740,"forward_high_90d":24600,"forward_low_90d":16740,"forward_high_180d":28200,"forward_low_180d":16740,"corporate_action_window_status":"not_flagged_in_prior_local_validation","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C30|294870|Stage2-Actionable|2024-05-13","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_delayed_rebound","reuse_reason":"same HDC Hyundai Development delayed construction rebound row from C05/C30 boundary files","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"bargain_rebound_positive_with_cash_repair_watch","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|294870|Stage2-Actionable|2024-05-13","non_price_bridge":"construction/project rebound with implied balance-sheet relief; requires project cash, unsold inventory and receivable refresh","score_alignment":"Stage2 can survive for C30 if balance-sheet repair is confirmed; no Green without PF/cash collection proof"}
{"row_type":"trigger","selected_round":"R10","selected_loop":107,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"SECTOR_REBOUND_BALANCE_SHEET_REPAIR_BOUNDARY_STAGE2_WATCH","symbol":"047040","name":"대우건설","trigger_type":"Stage2-Watch","entry_date":"2024-05-13","entry_price":3775,"entry_close":3775,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.72,"MAE_30D_pct":-4.64,"MFE_90D_pct":31.52,"MAE_90D_pct":-6.09,"MFE_180D_pct":31.52,"MAE_180D_pct":-6.75,"forward_high_30d":3840,"forward_low_30d":3600,"forward_high_90d":4965,"forward_low_90d":3545,"forward_high_180d":4965,"forward_low_180d":3520,"corporate_action_window_status":"not_flagged_in_prior_local_validation","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C30|047040|Stage2-Watch|2024-05-13","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_boundary","reuse_reason":"same Daewoo E&C construction rebound row from C05/C30 rows","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"sector_rebound_balance_sheet_boundary","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|047040|Stage2-Watch|2024-05-13","non_price_bridge":"construction sector rebound and possible balance-sheet relief; issuer-specific PF and cash bridge not isolated","score_alignment":"Stage2-Watch; C30 contribution capped until PF exposure, inventory and cash conversion are verified"}
{"row_type":"trigger","selected_round":"R10","selected_loop":107,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"QUALITY_BUILDER_LABEL_WITHOUT_PROJECT_CASH_BRIDGE_CAP","symbol":"375500","name":"DL이앤씨","trigger_type":"Stage2-Watch","entry_date":"2024-05-13","entry_price":34650,"entry_close":34650,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.90,"MAE_30D_pct":-4.04,"MFE_90D_pct":14.00,"MAE_90D_pct":-17.46,"MFE_180D_pct":14.00,"MAE_180D_pct":-17.46,"forward_high_30d":36000,"forward_low_30d":33250,"forward_high_90d":39500,"forward_low_90d":28600,"forward_high_180d":39500,"forward_low_180d":28600,"corporate_action_window_status":"not_flagged_in_prior_local_validation","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C30|375500|Stage2-Watch|2024-05-13","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_quality_label_cap","reuse_reason":"same DL E&C quality-label row from C05/C30 boundary files","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"quality_builder_balance_sheet_cap","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|375500|Stage2-Watch|2024-05-13","non_price_bridge":"quality/balance-sheet label without fresh project cash collection or PF relief proof","score_alignment":"cap Stage2-Actionable; require PF exposure, project receivables, unsold inventory and cash bridge"}
{"row_type":"trigger","selected_round":"R10","selected_loop":107,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"LARGE_BUILDER_SUPPORT_LABEL_LOW_MFE_FULL_WINDOW_BREAK_FALSE_POSITIVE","symbol":"000720","name":"현대건설","trigger_type":"Stage2-FalsePositive","entry_date":"2024-03-27","entry_price":33250,"entry_close":33250,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.81,"MAE_30D_pct":-6.17,"MFE_90D_pct":8.27,"MAE_90D_pct":-6.17,"MFE_180D_pct":8.27,"MAE_180D_pct":-27.52,"forward_high_30d":34850,"forward_low_30d":31200,"forward_high_90d":36000,"forward_low_90d":31200,"forward_high_180d":36000,"forward_low_180d":24100,"corporate_action_window_status":"not_flagged_in_prior_local_validation","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C30|000720|Stage2-FalsePositive|2024-03-27","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_false_positive","reuse_reason":"same Hyundai E&C large-builder support label false-positive from C05/C30 rows","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"large_builder_support_false_positive","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|000720|Stage2-FalsePositive|2024-03-27","non_price_bridge":"large-builder support/project label without visible PF repair, inventory cash collection or balance-sheet catalyst","score_alignment":"block Stage2-Actionable; 180D drawdown confirms support label alone failed"}
{"row_type":"trigger","selected_round":"R10","selected_loop":107,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"MEGA_EPC_HEADLINE_NOT_PF_REPAIR_WRONG_ARCHETYPE_FALSE_POSITIVE","symbol":"000720","name":"현대건설","trigger_type":"Stage2-FalsePositive","entry_date":"2024-07-01","entry_price":33200,"entry_close":33200,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.12,"MAE_30D_pct":-4.52,"MFE_90D_pct":5.12,"MAE_90D_pct":-12.50,"MFE_180D_pct":5.12,"MAE_180D_pct":-27.41,"forward_high_30d":34900,"forward_low_30d":31700,"forward_high_90d":34900,"forward_low_90d":29050,"forward_high_180d":34900,"forward_low_180d":24100,"corporate_action_window_status":"not_flagged_in_prior_local_validation","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C30|000720|Stage2-FalsePositive|2024-07-01","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_wrong_archetype_false_positive","reuse_reason":"same Hyundai E&C mega-contract weak rerating row from C05/C30 boundary files","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"EPC_headline_not_PF_repair","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|000720|Stage2-FalsePositive|2024-07-01","non_price_bridge":"Jafurah/main gas network EPC headline did not prove domestic PF or balance-sheet repair","score_alignment":"cap C30 contribution and reclassify to C05 if EPC margin evidence dominates; price path still false-positive"}
{"row_type":"trigger","selected_round":"R10","selected_loop":107,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"SMALL_BUILDER_SUPPORT_BETA_MODEST_MFE_WATCH_ONLY","symbol":"004960","name":"한신공영","trigger_type":"Stage2-Watch","entry_date":"2024-03-27","entry_price":6720,"entry_close":6720,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.48,"MAE_30D_pct":-8.33,"MFE_90D_pct":8.48,"MAE_90D_pct":-8.33,"MFE_180D_pct":18.60,"MAE_180D_pct":-8.63,"forward_high_30d":7290,"forward_low_30d":6160,"forward_high_90d":7290,"forward_low_90d":6160,"forward_high_180d":7970,"forward_low_180d":6140,"corporate_action_window_status":"not_flagged_in_prior_local_validation","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C30|004960|Stage2-Watch|2024-03-27","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_modest_rebound_cap","reuse_reason":"same Hanshin E&C modest rebound row from C05/C30 files","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"small_builder_support_beta_watch","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|004960|Stage2-Watch|2024-03-27","non_price_bridge":"small/mid-builder support beta without clear refinancing, PF exposure relief or cash collection bridge","score_alignment":"Stage2-Watch only; require refinancing, unsold inventory and project cash proof"}
{"row_type":"trigger","selected_round":"R10","selected_loop":107,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"EPC_AWARD_DELAYED_REBOUND_BOUNDARY_NOT_CLEAN_C30_LOCAL_4B","symbol":"006360","name":"GS건설","trigger_type":"Stage4B","entry_date":"2024-04-03","entry_price":15630,"entry_close":15630,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.97,"MAE_30D_pct":-10.17,"MFE_90D_pct":6.97,"MAE_90D_pct":-10.17,"MFE_180D_pct":39.16,"MAE_180D_pct":-10.17,"forward_high_30d":16720,"forward_low_30d":14040,"forward_high_90d":16720,"forward_low_90d":14040,"forward_high_180d":21750,"forward_low_180d":14040,"corporate_action_window_status":"not_flagged_in_prior_local_validation","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C30|006360|Stage4B|2024-04-03","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_EPC_boundary_4B","reuse_reason":"same GS E&C Fadhili delayed positive row from C05/C30 boundary files","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"EPC_boundary_delayed_rebound_4B","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|006360|Stage4B|2024-04-03","non_price_bridge":"Fadhili EPC award and delayed rebound; not clean C30 unless domestic PF/liquidity repair also proven","score_alignment":"local 4B boundary; reclassify to C05 unless PF/balance-sheet repair is dominant"}
{"row_type":"trigger","selected_round":"R10","selected_loop":107,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PURE_EPC_AWARD_WRONG_ARCHETYPE_C05_RECLASSIFICATION_CAP","symbol":"028050","name":"삼성E&A","trigger_type":"Stage2-Watch","entry_date":"2024-04-03","entry_price":25300,"entry_close":25300,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.72,"MAE_30D_pct":-5.34,"MFE_90D_pct":6.72,"MAE_90D_pct":-14.62,"MFE_180D_pct":10.47,"MAE_180D_pct":-14.62,"forward_high_30d":27000,"forward_low_30d":23950,"forward_high_90d":27000,"forward_low_90d":21600,"forward_high_180d":27950,"forward_low_180d":21600,"corporate_action_window_status":"not_flagged_in_prior_local_validation","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C30|028050|Stage2-Watch|2024-04-03","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_wrong_archetype_cap","reuse_reason":"same Samsung E&A Fadhili row from C05 loop 111; reused as C30 wrong-archetype boundary","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"pure_EPC_wrong_archetype_C05","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|028050|Stage2-Watch|2024-04-03","non_price_bridge":"pure overseas EPC award headline; no domestic PF, liquidity, unsold inventory or construction balance-sheet break evidence","score_alignment":"cap C30 and reclassify to C05 EPC margin gap; not a PF balance-sheet repair row"}
```

---

## 5. Narrative-only future TODO

```jsonl
{"row_type":"narrative_only_future_todo","selected_round":"R10","selected_loop":107,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_TRUE_PF_BREAK_REPRICE_TODO_AFTER_CACHE_MISS","candidate_symbols":["009410","034300","013580","014790","001470","001540","002410","003070","002150"],"candidate_names":["태영건설","신세계건설","계룡건설","HL D&I","삼부토건","안국약품-noise-exclusion","범양건영","코오롱글로벌","도화엔지니어링-boundary"],"why_not_trigger_row_now":"fresh stock-web symbol-year shards for true PF-break/workout/liquidity stress cases were not recomputed in this execution; no fresh 30D/90D/180D MFE/MAE computed here","calibration_usable":false,"score_alignment":"future run should compute stock-web windows before counting these as new C30 evidence; distinguish PF hard break, workout and liquidity stress from generic construction rebound or C05 EPC order headlines"}
```

---

## 6. Case analysis

### 6.1 HDC Hyundai Development / 294870 — bargain rebound positive with cash-repair watch

```yaml
entry_price: 17920
90D_MFE_MAE: +37.28 / -6.58
180D_MFE_MAE: +57.37 / -6.58
route: Stage2-Actionable with Green blocked
```

This is the positive-control shape for C30 in the reused set. The price path supports the bargain-rebound side of the archetype, but the non-price bridge still needs direct PF exposure, inventory, receivables and cash collection verification before any Green.

### 6.2 Daewoo E&C / 047040 — sector rebound boundary

```yaml
entry_price: 3775
90D_MFE_MAE: +31.52 / -6.09
180D_MFE_MAE: +31.52 / -6.75
route: Stage2-Watch
```

This row is useful, but it is not a clean PF repair row. It should remain Watch unless the model can isolate balance-sheet repair rather than broad construction beta.

### 6.3 DL E&C / 375500 — quality label cap

```yaml
entry_price: 34650
90D_MFE_MAE: +14.00 / -17.46
180D_MFE_MAE: +14.00 / -17.46
route: Stage2-Watch / cap
```

The quality label alone is not C30 Actionable. A good balance sheet is the bridge pillar, but the road still needs project cash and inventory relief.

### 6.4 Hyundai E&C / 000720 — repeated false-positive control

```yaml
2024-03-27:
  90D_MFE_MAE: +8.27 / -6.17
  180D_MFE_MAE: +8.27 / -27.52
  route: Stage2-FalsePositive

2024-07-01:
  90D_MFE_MAE: +5.12 / -12.50
  180D_MFE_MAE: +5.12 / -27.41
  route: Stage2-FalsePositive
```

Large-builder and mega-contract headlines failed twice. This is the C30 lesson: size and reputation do not repair PF plumbing.

### 6.5 Hanshin E&C / 004960 — small builder support beta

```yaml
entry_price: 6720
90D_MFE_MAE: +8.48 / -8.33
180D_MFE_MAE: +18.60 / -8.63
route: Stage2-Watch
```

This is a Watch row only. It needs refinancing, unsold inventory, and project cash evidence before promotion.

### 6.6 GS E&C / 006360 and Samsung E&A / 028050 — C05 boundary

```yaml
006360:
  90D_MFE_MAE: +6.97 / -10.17
  180D_MFE_MAE: +39.16 / -10.17
  route: local 4B / C05 boundary

028050:
  90D_MFE_MAE: +6.72 / -14.62
  180D_MFE_MAE: +10.47 / -14.62
  route: C05 reclassification cap
```

These rows belong mostly to EPC-margin analysis, not PF-balance-sheet repair. C30 must not steal C05 evidence.

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
local_4B_watch_count: 2
hard_or_false_positive_count: 2
wrong_archetype_reclassification_count: 2
current_profile_error_count: 5
diversity_score_summary: "bargain rebound, sector rebound, quality-label cap, large-builder false positive, small-builder watch, EPC wrong-archetype boundary covered; true PF-break candidates deferred to direct reprice"
loop_contribution_label: duplicate_low_value_loop_with_cache_miss_todo
do_not_propose_new_weight_delta: true
```

| symbol | role | 90D MFE/MAE | 180D MFE/MAE | C30 lesson |
|---|---:|---:|---:|---|
| 294870 | bargain rebound positive | +37.28 / -6.58 | +57.37 / -6.58 | rebound can work if cash repair proves |
| 047040 | sector rebound watch | +31.52 / -6.09 | +31.52 / -6.75 | isolate PF repair before promotion |
| 375500 | quality label cap | +14.00 / -17.46 | +14.00 / -17.46 | quality label alone insufficient |
| 000720 | support false positive | +8.27 / -6.17 | +8.27 / -27.52 | large-builder support failed |
| 000720 | EPC headline false positive | +5.12 / -12.50 | +5.12 / -27.41 | contract headline not PF repair |
| 004960 | small-builder watch | +8.48 / -8.33 | +18.60 / -8.63 | refinancing/cash proof required |
| 006360 | C05 boundary 4B | +6.97 / -10.17 | +39.16 / -10.17 | delayed rebound, no C30 backfill |
| 028050 | C05 reclassify | +6.72 / -14.62 | +10.47 / -14.62 | pure EPC, not C30 |

---

## 8. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"294870","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":5,"customer_quality_score":1,"policy_or_regulatory_score":2,"valuation_repricing_score":4,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":4,"customer_quality_score":1,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_after":73,"stage_label_after":"Stage2_Actionable_GreenBlocked","changed_components":["relative_strength_score","policy_or_regulatory_score"],"component_delta_explanation":"Delayed bargain rebound validates a C30 watch-positive path, but balance-sheet cash repair must be refreshed before Green.","MFE_90D_pct":37.28,"MAE_90D_pct":-6.58,"score_return_alignment_label":"bargain_rebound_cash_repair_watch","current_profile_verdict":"current_profile_correct_if_green_blocked"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"047040","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":4,"customer_quality_score":1,"policy_or_regulatory_score":2,"valuation_repricing_score":4,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":72,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":3,"customer_quality_score":1,"policy_or_regulatory_score":1,"valuation_repricing_score":3,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_after":65,"stage_label_after":"Stage2_Watch_contribution_cap","changed_components":["margin_bridge_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score"],"component_delta_explanation":"Sector rebound had price validation, but issuer-specific PF repair and cash bridge were not isolated.","MFE_90D_pct":31.52,"MAE_90D_pct":-6.09,"score_return_alignment_label":"sector_rebound_C30_cap","current_profile_verdict":"current_profile_correct_if_watch"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"375500","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":2,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":64,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":1,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":45,"stage_label_after":"Stage2_cap","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","accounting_trust_risk_score"],"component_delta_explanation":"Quality-builder label lacked PF/inventory/receivable cash bridge; cap Actionable.","MFE_90D_pct":14.00,"MAE_90D_pct":-17.46,"score_return_alignment_label":"quality_builder_label_cap","current_profile_verdict":"current_profile_false_positive_if_actionable"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"000720","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":1,"customer_quality_score":3,"policy_or_regulatory_score":2,"valuation_repricing_score":2,"execution_risk_score":4,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":62,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":3,"policy_or_regulatory_score":1,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":39,"stage_label_after":"Stage2_FalsePositive_Block","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Large-builder support label lacked PF cash repair; 180D drawdown confirms block.","MFE_90D_pct":8.27,"MAE_90D_pct":-6.17,"score_return_alignment_label":"large_builder_support_false_positive","current_profile_verdict":"current_profile_false_positive_if_stage2"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"000720","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":3,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":1,"customer_quality_score":4,"policy_or_regulatory_score":2,"valuation_repricing_score":2,"execution_risk_score":5,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":66,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":4,"policy_or_regulatory_score":1,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":41,"stage_label_after":"Stage2_FalsePositive_Block_or_C05_reclassify","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score"],"component_delta_explanation":"Mega EPC headline did not repair PF balance sheet and also failed price validation.","MFE_90D_pct":5.12,"MAE_90D_pct":-12.50,"score_return_alignment_label":"EPC_headline_not_PF_repair","current_profile_verdict":"requires_C05_reclassification_or_block"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"004960","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":60,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":1,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":45,"stage_label_after":"Stage2_Watch_contribution_cap","changed_components":["margin_bridge_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","accounting_trust_risk_score"],"component_delta_explanation":"Small-builder support beta lacked refinancing, inventory and project cash bridge.","MFE_90D_pct":8.48,"MAE_90D_pct":-8.33,"score_return_alignment_label":"small_builder_watch_cap","current_profile_verdict":"current_profile_correct_if_watch"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"006360","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":3,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":2,"customer_quality_score":4,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":4,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":2,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":4,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_after":59,"stage_label_after":"Stage4B_C05_boundary","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","policy_or_regulatory_score","accounting_trust_risk_score"],"component_delta_explanation":"Delayed rebound belongs more to EPC/C05 unless PF repair evidence dominates; keep 4B boundary.","MFE_90D_pct":6.97,"MAE_90D_pct":-10.17,"score_return_alignment_label":"EPC_boundary_not_clean_C30","current_profile_verdict":"requires_C05_reclassification_or_PF_evidence"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"028050","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":5,"backlog_visibility_score":4,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":1,"customer_quality_score":4,"policy_or_regulatory_score":1,"valuation_repricing_score":1,"execution_risk_score":4,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":3,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_after":42,"stage_label_after":"Reclassify_C05","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"Pure overseas EPC award is not C30 PF balance-sheet repair; reclassify to C05.","MFE_90D_pct":6.72,"MAE_90D_pct":-14.62,"score_return_alignment_label":"pure_EPC_wrong_archetype_C05","current_profile_verdict":"requires_reclassification"}
```

---

## 9. Current calibrated profile stress test

The C30 PF/balance-sheet break gate held:

```text
construction bargain rebound with cash repair evidence
→ Stage2 can survive, Green blocked until inventory/PF/cash proof

sector rebound without issuer-specific PF repair
→ Stage2-Watch cap

quality-builder label
→ cap until project cash evidence appears

large-builder support label
→ false-positive block if 180D drawdown emerges

EPC mega-contract headline
→ reclassify to C05 unless PF balance-sheet repair dominates

small-builder support beta
→ Watch only

true workout / PF hard break
→ must be directly repriced before scoring
```

### Rule candidate retained, not newly proposed

```text
C30_PF_LIQUIDITY_BALANCE_SHEET_BREAK_VS_BARGAIN_REBOUND_GATE_V107_HELD_OUT

if C30
and construction_lowPBR_support_rebound_or_quality_label == true
and PF_exposure_refinancing_unsold_inventory_receivables_or_project_cash_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C30
and bargain_rebound_price_path == true
and MFE_90D_pct >= +30
and MAE_90D_pct > -10
and balance_sheet_repair_evidence == partial:
    keep_stage2_watch_or_actionable = true
    block_stage3_green_until_PF_inventory_cash_refresh = true
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

```text
if C30
and MFE_90D_pct < +10
and MAE_180D_pct <= -25
and PF_cash_repair_bridge == false:
    route = Stage2_FalsePositive_Block
```

---

## 10. Profile comparison shadow-only summary

```yaml
profile_comparison:
  P0_e2r_2_2_rolling_calibrated_proxy:
    hypothesis: current rolling profile with global Stage2 bridge and 4C guards
    eligible_trigger_count: 8
    avg_MFE_90D_pct: 14.92
    avg_MAE_90D_pct: -10.24
    false_positive_risk: high_if_support_or_EPC_headlines_are_left_actionable
    verdict: adequate_only_with_C30_PF_cash_bridge_and_reclassification_gate
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
    hypothesis: C30 requires balance-sheet repair, not generic construction rebound
    changed_axes: none_new_holdout_only
    verdict: pass_holdout
  P3_counterexample_guard_profile:
    hypothesis: large-builder support and EPC headlines without PF cash repair route to block/reclassify
    changed_axes: none_new_holdout_only
    verdict: strongest_for_false_positive_control
```

---

## 11. Coverage matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_or_false_positive_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---:|
| L9_CONSTRUCTION_REALESTATE_HOUSING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | PF_BALANCE_SHEET_BREAK_HOLDOUT_V107 | 2 | 6 | 2 | 2 | 0 | 8 | 8 | 0 | 5 | false | false | 27 |

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
  - C30|294870|Stage2-Actionable|2024-05-13
  - C30|047040|Stage2-Watch|2024-05-13
  - C30|375500|Stage2-Watch|2024-05-13
  - C30|000720|Stage2-FalsePositive|2024-03-27
  - C30|000720|Stage2-FalsePositive|2024-07-01
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
  - construction_support_label_without_cash_repair
  - delayed_rebound_backfill_risk
  - quality_builder_label_without_project_cash
  - EPC_headline_wrong_archetype
  - true_PF_break_reprice_gap
new_axis_proposed: null
existing_axis_strengthened:
  - C30_PF_LIQUIDITY_BALANCE_SHEET_BREAK_VS_BARGAIN_REBOUND_GATE_V107_HELD_OUT
existing_axis_weakened: null
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
no_new_signal_reason: all rows reused holdout validation after direct fresh true-PF-break candidate shards were unavailable or not recomputed
loop_contribution_label: duplicate_low_value_loop_with_cache_miss_todo
do_not_propose_new_weight_delta: true
```

```jsonl
{"row_type":"residual_contribution","round":"R10","loop":"107","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","new_independent_case_count":0,"reused_case_count":8,"new_symbol_count":0,"new_trigger_family_count":0,"narrative_only_future_todo_count":1,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","hard_4c_thesis_break_routes_to_4c","C30_PF_liquidity_balance_sheet_break_gate","C05_EPC_reclassification_guard"],"residual_error_types_found":["construction_support_label_without_cash_repair","delayed_rebound_backfill_risk","quality_builder_label_without_project_cash","EPC_headline_wrong_archetype","true_PF_break_reprice_gap"],"loop_contribution_label":"duplicate_low_value_loop_with_cache_miss_todo","do_not_propose_new_weight_delta":true}
```

---

## 14. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Treat this R10/C30 loop 107 as holdout validation only. Batch it with C30 loops 102~106, C05 EPC boundary files, and R13 accounting-trust / Stage2 false-positive / high-MAE / 4B-4C guardrails. If exact same_entry_group_id rows already exist, dedupe them. Preserve the C30 PF/liquidity/balance-sheet break versus bargain-rebound gate, delayed rebound no-backfill rule, and C05 EPC reclassification guard, but do not create a new weight delta from this loop because no new independent case was added. Future research should directly reprice 태영건설(009410), 신세계건설(034300), 계룡건설(013580), HL D&I(014790), 삼부토건(001470), 범양건영(002410), 코오롱글로벌(003070) and other true PF/workout/liquidity-stress cases when stock-web shards are accessible.
```

---

## 15. Next research state

```yaml
completed_round: R10
completed_loop: 107
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
