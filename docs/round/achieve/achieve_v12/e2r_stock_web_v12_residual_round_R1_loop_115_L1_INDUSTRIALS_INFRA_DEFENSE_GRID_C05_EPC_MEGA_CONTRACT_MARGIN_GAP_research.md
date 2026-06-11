# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R1
selected_loop: 115
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id: EPC_MEGA_CONTRACT_TO_MARGIN_WORKING_CAPITAL_CASH_BRIDGE_HOLDOUT_V115_SAUDI_GAS_CONSTRUCTION_REBOUND_PF_ADJACENT_SPLIT
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
  stock_web_manifest: read_ok
  direct_new_symbol_shards:
    - 028050/2024: cache_miss_or_reused_from_prior_local_file
    - 006360/2024: cache_miss_or_reused_from_prior_local_file
    - 000720/2024: cache_miss_or_reused_from_prior_local_file
    - 294870/2024: reused_from_prior_local_file
    - 047040/2024: reused_from_prior_local_file
    - 375500/2024: reused_from_prior_local_file
    - 004960/2024: reused_from_prior_local_file
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
loop_objective:
  - holdout_validation
  - duplicate_low_value_loop_marker
  - EPC_contract_size_to_margin_cash_bridge_gate
  - working_capital_receivable_cost_overrun_guard
  - delayed_construction_rebound_no_backfill_guard
  - PF_adjacent_reclassification_cap_guard
price_source: Songdaiki/stock-web
price_data_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

`C05_EPC_MEGA_CONTRACT_MARGIN_GAP` remains a Priority 0 archetype. The current no-repeat index marks C05 as under the 30-row minimum, and the v12 scheduler maps C01~C05 to `R1 / L1_INDUSTRIALS_INFRA_DEFENSE_GRID`.

This file continues the local C05 sequence after `R1/C05 loop 114`; selected loop is therefore `115`.

This is a **dedupe-aware holdout validation / cache-miss TODO** MD. It does not claim fresh independent stock-web evidence because direct fresh symbol-year shard recomputation was unavailable in this execution. The trigger rows below reuse current-session stock-web-derived C05/C30 rows that already contain complete 30D/90D/180D MFE and MAE from `Songdaiki/stock-web` tradable OHLC. Exact duplicate `same_entry_group_id` rows should be deduped during batch ingest. No production scoring is changed.

---

## 1. Research thesis

C05 is not `large EPC contract announced`.

C05 is the gap between headline backlog and equity economics:

```text
EPC / mega contract / plant package / construction project / order rebound
→ scope quality
→ procurement and pass-through terms
→ cost escalation risk
→ working capital and receivables
→ execution risk
→ margin and cash conversion
→ price path validation
```

The recurring false positive is:

```text
mega contract size
sector rebound
construction support label
PF/housing beta
quality balance-sheet label
one delayed price rebound
```

A contract headline is the crane on the skyline. C05 scores only when that crane is bolted to the foundation: margin, receivables, cash collection and cost discipline.

This holdout pass validates five route types:

1. **Saudi gas EPC award positive with margin watch**
   - Stage2 can open when a named EPC package is won.
   - Stage3-Green remains blocked until margin/cash evidence refreshes.

2. **Delayed EPC / construction rebound**
   - 90D/180D MFE may validate later.
   - Do not backfill delayed rebound into immediate Stage2-Actionable.

3. **Project or balance-sheet quality label**
   - Watch/cap if no project margin, cost, receivable or cash bridge exists.

4. **Large-builder support / mega contract false positive**
   - Low MFE and deep 180D MAE block Stage2-Actionable.

5. **PF-adjacent or housing beta**
   - Useful as boundary evidence, but C05 contribution is capped when PF/housing balance-sheet mechanics dominate C30.

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 8
  actual_trigger_rows: 8
  narrative_only_future_todo_rows: 1
  source_archetypes:
    - C05_EPC_MEGA_CONTRACT_MARGIN_GAP
    - C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
    - R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
    - R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
    - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
    - R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
  price_windows:
    - 30D MFE/MAE
    - 90D MFE/MAE
    - 180D MFE/MAE
  output_use:
    - C05 holdout validation
    - EPC contract-size-to-margin-cash bridge gate
    - delayed rebound no-backfill guard
    - PF/construction reclassification cap guard
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
  - R10/C30 loops 102~106
  - R13 accounting-trust loops 12~14
  - R13 Stage2 false-positive loop 11
  - R13 high-MAE loop 9
  - R13 4B/4C loop 104
reason:
  - all reused rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - direct fresh C05 candidate shards were unavailable or not recomputed in this execution
  - exact duplicate C05 keys should be deduped during batch ingest
  - this file is holdout validation / duplicate-low-value evidence only
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","selected_round":"R1","selected_loop":115,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"FADHILI_SAMSUNG_EA_CONTRACT_SIZE_LOCAL_POSITIVE_WITH_MARGIN_CASH_WATCH","symbol":"028050","name":"삼성E&A","trigger_type":"Stage2-Actionable","entry_date":"2024-04-03","entry_price":25300,"entry_close":25300,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.72,"MAE_30D_pct":-5.34,"MFE_90D_pct":6.72,"MAE_90D_pct":-14.62,"MFE_180D_pct":10.47,"MAE_180D_pct":-14.62,"forward_high_30d":27000,"forward_low_30d":23950,"forward_high_90d":27000,"forward_low_90d":21600,"forward_high_180d":27950,"forward_low_180d":21600,"corporate_action_window_status":"not_flagged_in_prior_local_validation","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C05|028050|Stage2-Actionable|2024-04-03","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_incremental_positive","reuse_reason":"same Samsung E&A Fadhili row from C05 loop 111","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"direct_EPC_award_positive_with_margin_watch","novelty_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|028050|Stage2-Actionable|2024-04-03","non_price_bridge":"Samsung E&A won a major Fadhili EPC package, but equity path stayed modest relative to headline size","score_alignment":"Stage2 may open; Stage3-Green blocked until margin, working-capital and cash bridge refresh"}
{"row_type":"trigger","selected_round":"R1","selected_loop":115,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"FADHILI_GS_EC_DELAYED_POSITIVE_WITH_4B_WATCH_CONTROL","symbol":"006360","name":"GS건설","trigger_type":"Stage2-Actionable","entry_date":"2024-04-03","entry_price":15630,"entry_close":15630,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.97,"MAE_30D_pct":-10.17,"MFE_90D_pct":6.97,"MAE_90D_pct":-10.17,"MFE_180D_pct":39.16,"MAE_180D_pct":-10.17,"forward_high_30d":16720,"forward_low_30d":14040,"forward_high_90d":16720,"forward_low_90d":14040,"forward_high_180d":21750,"forward_low_180d":14040,"corporate_action_window_status":"not_flagged_in_prior_local_validation","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C05|006360|Stage2-Actionable|2024-04-03","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_delayed_positive_control","reuse_reason":"same GS E&C Fadhili row from C05 loop 111","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"delayed_positive_with_4B_watch","novelty_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|006360|Stage2-Actionable|2024-04-03","non_price_bridge":"Fadhili EPC award with delayed but meaningful 180D equity response","score_alignment":"keep Stage2-Actionable but local 4B watch is required because early MAE was double-digit and margin/cash bridge was not immediate"}
{"row_type":"trigger","selected_round":"R1","selected_loop":115,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"JAFURAH_HYUNDAI_EC_MEGA_CONTRACT_SIZE_WEAK_RERATING_FALSE_POSITIVE","symbol":"000720","name":"현대건설","trigger_type":"Stage2-FalsePositive","entry_date":"2024-07-01","entry_price":33200,"entry_close":33200,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.12,"MAE_30D_pct":-4.52,"MFE_90D_pct":5.12,"MAE_90D_pct":-12.50,"MFE_180D_pct":5.12,"MAE_180D_pct":-27.41,"forward_high_30d":34900,"forward_low_30d":31700,"forward_high_90d":34900,"forward_low_90d":29050,"forward_high_180d":34900,"forward_low_180d":24100,"corporate_action_window_status":"not_flagged_in_prior_local_validation","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C05|000720|Stage2-FalsePositive|2024-07-01","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_counter_control","reuse_reason":"same Hyundai E&C Jafurah row from C05 loop 111","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"mega_contract_size_false_positive","novelty_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|000720|Stage2-FalsePositive|2024-07-01","non_price_bridge":"Jafurah/main gas network headline did not translate into durable equity rerating","score_alignment":"contract size alone should not earn Stage2-Actionable bonus without margin and cash bridge"}
{"row_type":"trigger","selected_round":"R1","selected_loop":115,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"DELAYED_CONSTRUCTION_PROJECT_REBOUND_WITH_MARGIN_CASH_BRIDGE_REQUIRED","symbol":"294870","name":"HDC현대산업개발","trigger_type":"Stage2-Watch","entry_date":"2024-05-13","entry_price":17920,"entry_close":17920,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.12,"MAE_30D_pct":-6.58,"MFE_90D_pct":37.28,"MAE_90D_pct":-6.58,"MFE_180D_pct":57.37,"MAE_180D_pct":-6.58,"forward_high_30d":18300,"forward_low_30d":16740,"forward_high_90d":24600,"forward_low_90d":16740,"forward_high_180d":28200,"forward_low_180d":16740,"corporate_action_window_status":"not_flagged_in_prior_local_validation","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C05|294870|Stage2-Watch|2024-05-13","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_delayed_positive","reuse_reason":"same HDC Hyundai Development delayed construction rebound row from C05 loop 114 and C30 rows","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"delayed_positive_with_margin_bridge_requirement","novelty_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|294870|Stage2-Watch|2024-05-13","non_price_bridge":"delayed construction/project rebound; no direct EPC margin or cash bridge at entry","score_alignment":"allow delayed local 4B; block Stage2-Actionable until project margin, receivable, cost and cash bridge refresh"}
{"row_type":"trigger","selected_round":"R1","selected_loop":115,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"CONSTRUCTION_EPC_SECTOR_REBOUND_WITH_C05_CONTRIBUTION_CAP","symbol":"047040","name":"대우건설","trigger_type":"Stage2-Watch","entry_date":"2024-05-13","entry_price":3775,"entry_close":3775,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.72,"MAE_30D_pct":-4.64,"MFE_90D_pct":31.52,"MAE_90D_pct":-6.09,"MFE_180D_pct":31.52,"MAE_180D_pct":-6.75,"forward_high_30d":3840,"forward_low_30d":3600,"forward_high_90d":4965,"forward_low_90d":3545,"forward_high_180d":4965,"forward_low_180d":3520,"corporate_action_window_status":"not_flagged_in_prior_local_validation","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C05|047040|Stage2-Watch|2024-05-13","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_boundary","reuse_reason":"same Daewoo E&C construction/EPC sector rebound row from C05 loop 114","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"positive_boundary_control","novelty_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|047040|Stage2-Watch|2024-05-13","non_price_bridge":"construction/EPC sector rebound; issuer-specific margin and working-capital bridge not isolated","score_alignment":"cap C05 contribution; Stage2-Watch until backlog margin and cash conversion confirm"}
{"row_type":"trigger","selected_round":"R1","selected_loop":115,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"BALANCE_SHEET_QUALITY_LABEL_WITHOUT_PROJECT_MARGIN_CASH_BRIDGE_STAGE2_CAP","symbol":"375500","name":"DL이앤씨","trigger_type":"Stage2-Watch","entry_date":"2024-05-13","entry_price":34650,"entry_close":34650,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.90,"MAE_30D_pct":-4.04,"MFE_90D_pct":14.00,"MAE_90D_pct":-17.46,"MFE_180D_pct":14.00,"MAE_180D_pct":-17.46,"forward_high_30d":36000,"forward_low_30d":33250,"forward_high_90d":39500,"forward_low_90d":28600,"forward_high_180d":39500,"forward_low_180d":28600,"corporate_action_window_status":"not_flagged_in_prior_local_validation","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C05|375500|Stage2-Watch|2024-05-13","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_quality_label_cap","reuse_reason":"same DL E&C quality-label row from C05 loop 114","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"quality_label_cap","novelty_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|375500|Stage2-Watch|2024-05-13","non_price_bridge":"better quality/balance-sheet label without fresh project margin or cash-collection proof","score_alignment":"cap Stage2-Actionable; require EPC margin, cost, receivable and cash bridge before upgrade"}
{"row_type":"trigger","selected_round":"R1","selected_loop":115,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"LARGE_BUILDER_SUPPORT_LABEL_LOW_MFE_HIGH_MAE_STAGE2_BLOCK","symbol":"000720","name":"현대건설","trigger_type":"Stage2-FalsePositive","entry_date":"2024-03-27","entry_price":33250,"entry_close":33250,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.81,"MAE_30D_pct":-6.17,"MFE_90D_pct":8.27,"MAE_90D_pct":-6.17,"MFE_180D_pct":8.27,"MAE_180D_pct":-27.52,"forward_high_30d":34850,"forward_low_30d":31200,"forward_high_90d":36000,"forward_low_90d":31200,"forward_high_180d":36000,"forward_low_180d":24100,"corporate_action_window_status":"not_flagged_in_prior_local_validation","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C05|000720|Stage2-FalsePositive|2024-03-27","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_counterexample","reuse_reason":"same Hyundai E&C large-builder support label false-positive from C05 loop 114","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"hard_counterexample","novelty_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|000720|Stage2-FalsePositive|2024-03-27","non_price_bridge":"large-builder support/project label without project margin, cost or cash bridge; full-window drawdown invalidates Stage2","score_alignment":"block Stage2-Actionable unless new issuer-specific contract margin/cash evidence appears"}
{"row_type":"trigger","selected_round":"R1","selected_loop":115,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"SMALL_BUILDER_SUPPORT_BETA_MODEST_MFE_C05_CONTRIBUTION_CAP","symbol":"004960","name":"한신공영","trigger_type":"Stage2-Watch","entry_date":"2024-03-27","entry_price":6720,"entry_close":6720,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.48,"MAE_30D_pct":-8.33,"MFE_90D_pct":8.48,"MAE_90D_pct":-8.33,"MFE_180D_pct":18.60,"MAE_180D_pct":-8.63,"forward_high_30d":7290,"forward_low_30d":6160,"forward_high_90d":7290,"forward_low_90d":6160,"forward_high_180d":7970,"forward_low_180d":6140,"corporate_action_window_status":"not_flagged_in_prior_local_validation","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C05|004960|Stage2-Watch|2024-03-27","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_modest_rebound_cap","reuse_reason":"same Hanshin E&C modest rebound row from C05 loop 114","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"modest_rebound_contribution_cap","novelty_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|004960|Stage2-Watch|2024-03-27","non_price_bridge":"small/mid-builder support beta without clear EPC contract margin or working-capital bridge","score_alignment":"Stage2-Watch only; require contract margin, receivable and cash conversion proof"}
```

---

## 5. Narrative-only future TODO

```jsonl
{"row_type":"narrative_only_future_trigger_todo","selected_round":"R1","selected_loop":115,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_NEW_EPC_CONTRACT_REPRICE_TODO_AFTER_CACHE_MISS","candidate_symbols":["028050","006360","000720","047040","375500","010130","034020"],"candidate_names":["삼성E&A","GS건설","현대건설","대우건설","DL이앤씨","고려아연-EPC_CAPEX_noise_check","두산에너빌리티-project_margin_check"],"why_not_trigger_row_now":"fresh stock-web symbol-year shards were unavailable or not recomputed in this execution; no fresh 30D/90D/180D MFE/MAE computed here","calibration_usable":false,"score_alignment":"future run should compute fresh stock-web windows before counting new C05 evidence; distinguish EPC contract margin bridge from C30 PF/housing balance-sheet beta or C04/C16 project-policy noise"}
```

---

## 6. Case analysis

### 6.1 Saudi gas EPC award rows — contract headline is not enough

```yaml
028050:
  entry_price: 25300
  90D_MFE_MAE: +6.72 / -14.62
  180D_MFE_MAE: +10.47 / -14.62
  route: Stage2-Actionable with Green blocked

006360:
  entry_price: 15630
  90D_MFE_MAE: +6.97 / -10.17
  180D_MFE_MAE: +39.16 / -10.17
  route: Stage2-Actionable / delayed 4B watch

000720:
  entry_price: 33200
  90D_MFE_MAE: +5.12 / -12.50
  180D_MFE_MAE: +5.12 / -27.41
  route: Stage2-FalsePositive
```

The Saudi package rows are the cleanest C05 stress test. The headline size is visible, but price path demands margin and cash confirmation. Samsung E&A and GS E&C can remain Stage2/Watch because the award is named, but neither should be Green without margin and working-capital bridge repair. Hyundai E&C’s Jafurah-style headline row is the false-positive control.

### 6.2 Construction rebound rows — delayed MFE is not immediate C05 proof

```yaml
294870:
  90D_MFE_MAE: +37.28 / -6.58
  180D_MFE_MAE: +57.37 / -6.58
  route: delayed local 4B

047040:
  90D_MFE_MAE: +31.52 / -6.09
  180D_MFE_MAE: +31.52 / -6.75
  route: Stage2-Watch / C05 contribution cap
```

These rows are real price-path positives, but the bridge is not pure C05. They carry PF/housing/construction beta and need issuer-specific margin, receivable and cash collection proof before promotion.

### 6.3 Quality label rows — Watch, not Actionable

```yaml
375500:
  90D_MFE_MAE: +14.00 / -17.46
  180D_MFE_MAE: +14.00 / -17.46
  route: Stage2-Watch / cap

004960:
  90D_MFE_MAE: +8.48 / -8.33
  180D_MFE_MAE: +18.60 / -8.63
  route: Stage2-Watch / cap
```

The model should not treat a quality balance-sheet or small-builder support label as direct EPC margin evidence.

### 6.4 Large-builder support false-positive

```yaml
000720:
  entry_date: 2024-03-27
  90D_MFE_MAE: +8.27 / -6.17
  180D_MFE_MAE: +8.27 / -27.52
  route: Stage2-FalsePositive
```

This row says the same thing as the Jafurah row in a different trigger family: large-builder label plus support narrative is not enough.

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
positive_case_count: 4
counterexample_count: 4
local_4B_watch_count: 4
hard_or_false_positive_count: 2
wrong_archetype_reclassification_count: 2
current_profile_error_count: 5
diversity_score_summary: "Saudi gas EPC award, delayed construction rebound, quality-label cap, large-builder false-positive and PF-adjacent contribution cap covered; all rows reused"
loop_contribution_label: duplicate_low_value_loop_with_cache_miss_todo
do_not_propose_new_weight_delta: true
```

| symbol | role | 90D MFE/MAE | 180D MFE/MAE | C05 lesson |
|---|---:|---:|---:|---|
| 028050 | direct EPC award watch | +6.72 / -14.62 | +10.47 / -14.62 | contract size needs margin/cash bridge |
| 006360 | EPC delayed positive | +6.97 / -10.17 | +39.16 / -10.17 | delayed MFE, no Green |
| 000720 | mega contract false positive | +5.12 / -12.50 | +5.12 / -27.41 | headline failed |
| 294870 | delayed project rebound | +37.28 / -6.58 | +57.37 / -6.58 | no immediate backfill |
| 047040 | sector rebound cap | +31.52 / -6.09 | +31.52 / -6.75 | margin/cash not isolated |
| 375500 | quality label cap | +14.00 / -17.46 | +14.00 / -17.46 | balance-sheet quality is not EPC margin |
| 000720 | support label false positive | +8.27 / -6.17 | +8.27 / -27.52 | support label failed |
| 004960 | modest rebound cap | +8.48 / -8.33 | +18.60 / -8.63 | small builder beta not enough |

---

## 8. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"028050","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_score":5,"backlog_visibility_score":4,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":1,"customer_quality_score":4,"policy_or_regulatory_score":1,"valuation_repricing_score":1,"execution_risk_score":4,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":4,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":1,"customer_quality_score":4,"policy_or_regulatory_score":1,"valuation_repricing_score":1,"execution_risk_score":4,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_after":68,"stage_label_after":"Stage2_Actionable_GreenBlocked","changed_components":["margin_bridge_score","accounting_trust_risk_score"],"component_delta_explanation":"Named EPC award opens Stage2, but modest MFE and missing margin/cash bridge block Green.","MFE_90D_pct":6.72,"MAE_90D_pct":-14.62,"score_return_alignment_label":"EPC_award_positive_margin_watch","current_profile_verdict":"current_profile_correct_if_green_blocked"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"006360","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":3,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":2,"customer_quality_score":4,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":4,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":4,"backlog_visibility_score":3,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":2,"customer_quality_score":4,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":4,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_after":66,"stage_label_after":"Stage4B_delayed_EPC_watch","changed_components":["margin_bridge_score","accounting_trust_risk_score"],"component_delta_explanation":"Fadhili award produced delayed 180D validation but early MAE and missing cash bridge require 4B watch.","MFE_90D_pct":6.97,"MAE_90D_pct":-10.17,"score_return_alignment_label":"delayed_EPC_positive_no_Green","current_profile_verdict":"current_profile_too_generous_if_actionable_without_refresh"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"000720","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":3,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":1,"customer_quality_score":4,"policy_or_regulatory_score":2,"valuation_repricing_score":2,"execution_risk_score":5,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":66,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":4,"policy_or_regulatory_score":1,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":42,"stage_label_after":"Stage2_FalsePositive_Block","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score"],"component_delta_explanation":"Mega-contract headline did not become margin/cash bridge and price path rejected it.","MFE_90D_pct":5.12,"MAE_90D_pct":-12.50,"score_return_alignment_label":"mega_contract_size_false_positive","current_profile_verdict":"current_profile_false_positive_if_stage2"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"294870","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":5,"customer_quality_score":2,"policy_or_regulatory_score":2,"valuation_repricing_score":4,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":73,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":4,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":3,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_after":66,"stage_label_after":"Stage4B_delayed_no_backfill","changed_components":["margin_bridge_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score"],"component_delta_explanation":"Delayed construction rebound is useful but entry-date EPC margin/cash bridge was not visible.","MFE_90D_pct":37.28,"MAE_90D_pct":-6.58,"score_return_alignment_label":"delayed_project_rebound_no_backfill","current_profile_verdict":"current_profile_correct_if_no_backfill"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"047040","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":4,"customer_quality_score":2,"policy_or_regulatory_score":2,"valuation_repricing_score":4,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":72,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":3,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":3,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_after":65,"stage_label_after":"Stage2_Watch_contribution_cap","changed_components":["margin_bridge_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score"],"component_delta_explanation":"Construction/EPC rebound had price validation, but issuer-specific backlog margin and cash conversion were not isolated.","MFE_90D_pct":31.52,"MAE_90D_pct":-6.09,"score_return_alignment_label":"sector_rebound_C05_contribution_cap","current_profile_verdict":"requires_C30_or_general_construction_reclassification_check"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"375500","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":2,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":64,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":1,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":45,"stage_label_after":"Stage2_cap","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","accounting_trust_risk_score"],"component_delta_explanation":"Balance-sheet quality label lacked fresh project margin, cost, receivable or cash bridge.","MFE_90D_pct":14.00,"MAE_90D_pct":-17.46,"score_return_alignment_label":"quality_label_without_margin_bridge_cap","current_profile_verdict":"current_profile_false_positive_if_actionable"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"000720","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":1,"customer_quality_score":3,"policy_or_regulatory_score":2,"valuation_repricing_score":2,"execution_risk_score":4,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":62,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":3,"policy_or_regulatory_score":1,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":39,"stage_label_after":"Stage2_FalsePositive_Block","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Large-builder support/project label lacked margin and cash bridge; 180D MAE confirms block.","MFE_90D_pct":8.27,"MAE_90D_pct":-6.17,"score_return_alignment_label":"support_label_full_window_failure","current_profile_verdict":"current_profile_false_positive_if_stage2"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"004960","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":60,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":1,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":45,"stage_label_after":"Stage2_Watch_contribution_cap","changed_components":["margin_bridge_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","accounting_trust_risk_score"],"component_delta_explanation":"Small-builder support beta lacked clear EPC contract margin or working-capital bridge.","MFE_90D_pct":8.48,"MAE_90D_pct":-8.33,"score_return_alignment_label":"small_builder_beta_cap","current_profile_verdict":"current_profile_correct_if_watch"}
```

---

## 9. Current calibrated profile stress test

The C05 EPC-contract-to-margin-cash bridge gate held:

```text
named EPC award
→ Stage2 may open

contract size without margin/cash bridge
→ no Green

delayed rebound
→ local 4B / Watch, no immediate backfill

sector or PF/housing beta
→ cap C05 and reclassify if C30 dominates

quality balance-sheet label
→ cap until project margin/cash bridge appears

large-builder support label with low MFE/deep 180D MAE
→ false-positive block
```

### Rule candidate retained, not newly proposed

```text
C05_EPC_CONTRACT_SIZE_TO_MARGIN_WORKING_CAPITAL_CASH_GATE_V115_HELD_OUT

if C05
and EPC_contract_project_or_construction_order_headline == true
and project_margin_working_capital_receivable_cost_or_cash_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C05
and named_EPC_award == true
and MFE_90D_pct < +10
and MAE_90D_pct <= -10
and margin_cash_bridge == false:
    route = local_4B_or_Stage2_Watch
    block_stage3_green = true
```

```text
if C05
and delayed_rebound_after_90D_or_180D == true
and entry_date_margin_cash_bridge == false:
    route = delayed_local_4B
    do_not_backfill_as_immediate_Stage2_Actionable = true
```

```text
if C05
and construction_PF_housing_balance_sheet_beta_dominates == true:
    cap_C05_contribution = true
    require_reclassification_to_C30_or_adjacent_construction_axis = true
```

```text
if C05
and MFE_90D_pct < +10
and MAE_180D_pct <= -25
and contract_margin_cash_bridge == false:
    route = Stage2_FalsePositive_Block
```

---

## 10. Profile comparison shadow-only summary

```yaml
profile_comparison:
  P0_e2r_2_1_stock_web_calibrated_proxy:
    hypothesis: current profile with global Stage2 bridge and 4C guards
    eligible_trigger_count: 8
    avg_MFE_90D_pct: 14.41
    avg_MAE_90D_pct: -10.74
    false_positive_risk: high_if_contract_size_or_construction_beta_is_left_actionable
    verdict: adequate_only_with_C05_margin_working_capital_cash_gate
  P0b_e2r_2_0_baseline_reference:
    hypothesis: older profile pays too much for mega-contract headline size
    eligible_trigger_count: 8
    false_positive_risk: higher
    verdict: inferior
  P1_sector_specific_candidate_profile:
    hypothesis: L1 EPC/project rows require margin, receivable and cash conversion proof
    changed_axes: none_new_holdout_only
    verdict: pass_holdout
  P2_canonical_archetype_candidate_profile:
    hypothesis: C05 requires contract-to-margin bridge, not contract value
    changed_axes: none_new_holdout_only
    verdict: pass_holdout
  P3_counterexample_guard_profile:
    hypothesis: large-builder support / mega-contract headlines without cash bridge route to false-positive block
    changed_axes: none_new_holdout_only
    verdict: strongest_for_false_positive_control
```

---

## 11. Coverage matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_or_false_positive_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---:|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | EPC_CONTRACT_TO_MARGIN_CASH_HOLDOUT_V115 | 4 | 4 | 4 | 2 | 0 | 8 | 8 | 0 | 5 | false | false | 17 |

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
  - C05|028050|Stage2-Actionable|2024-04-03
  - C05|006360|Stage2-Actionable|2024-04-03
  - C05|000720|Stage2-FalsePositive|2024-07-01
  - C05|294870|Stage2-Watch|2024-05-13
  - C05|047040|Stage2-Watch|2024-05-13
  - C05|375500|Stage2-Watch|2024-05-13
  - C05|000720|Stage2-FalsePositive|2024-03-27
  - C05|004960|Stage2-Watch|2024-03-27
new_symbol_count: 0
new_trigger_family_count: 0
narrative_only_future_todo_count: 1
tested_existing_calibrated_axes:
  - stage2_required_bridge
  - local_4b_watch_guard
  - hard_4c_thesis_break_routes_to_4c
  - C05_contract_to_margin_working_capital_cash_gate
  - no_backfill_later_evidence
  - construction_PF_reclassification_cap
residual_error_types_found:
  - contract_size_without_margin_cash_bridge
  - delayed_rebound_backfill_risk
  - construction_sector_beta_misfile
  - quality_label_without_project_cash_bridge
  - large_builder_support_false_positive
new_axis_proposed: null
existing_axis_strengthened:
  - C05_EPC_CONTRACT_SIZE_TO_MARGIN_WORKING_CAPITAL_CASH_GATE_V115_HELD_OUT
existing_axis_weakened: null
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
no_new_signal_reason: all rows reused holdout validation after direct fresh C05 candidate shards were unavailable or not recomputed
loop_contribution_label: duplicate_low_value_loop_with_cache_miss_todo
do_not_propose_new_weight_delta: true
```

```jsonl
{"row_type":"residual_contribution","round":"R1","loop":"115","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","new_independent_case_count":0,"reused_case_count":8,"new_symbol_count":0,"new_trigger_family_count":0,"narrative_only_future_todo_count":1,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","hard_4c_thesis_break_routes_to_4c","C05_contract_to_margin_working_capital_cash_gate","no_backfill_later_evidence","construction_PF_reclassification_cap"],"residual_error_types_found":["contract_size_without_margin_cash_bridge","delayed_rebound_backfill_risk","construction_sector_beta_misfile","quality_label_without_project_cash_bridge","large_builder_support_false_positive"],"loop_contribution_label":"duplicate_low_value_loop_with_cache_miss_todo","do_not_propose_new_weight_delta":true}
```

---

## 14. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Treat this R1/C05 loop 115 as holdout validation only. Batch it with C05 loops 111 and 114, C30 PF/construction boundary rows, and R13 accounting-trust / Stage2 false-positive / high-MAE / 4B-4C guardrails. If exact same_entry_group_id rows already exist, dedupe them. Preserve the C05 EPC-contract-size-to-margin-working-capital-cash bridge gate and the delayed-rebound no-backfill guard, but do not create a new weight delta from this loop because no new independent case was added. Future research should reprice Samsung E&A(028050), GS건설(006360), 현대건설(000720), 대우건설(047040), DL이앤씨(375500) and additional EPC/plant cases when stock-web shards are accessible.
```

---

## 15. Next research state

```yaml
completed_round: R1
completed_loop: 115
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C13_BATTERY_JV_UTILIZATION_AMPC_IRA
  - C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
  - C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
  - C19_BRAND_RETAIL_INVENTORY_MARGIN
  - C27_CONTENT_IP_GLOBAL_MONETIZATION
```
