# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R6
selected_loop: 115
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: ROE_PBR_VALUEUP_CAPITAL_RETURN_EXECUTION_HOLDOUT_V115_BANK_SECURITIES_INSURANCE_BOUNDARY_SPLIT
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
  stock_web_manifest: read_ok
  direct_stock_web_shards:
    - 005940/2024: reused_from_prior_local_C21_loop_114_positive_row
    - 105560/2024: reused_from_prior_local_C21_loop_114_bank_4B_row
    - 316140/2024: reused_from_prior_local_C21_loop_114_valueup_cap_row
    - 006800/2024: reused_from_prior_local_C21_loop_114_hard_4C_row
    - 005830/2024: reused_from_prior_local_C22_C31_C32_boundary_row
    - 088350/2024: reused_from_prior_local_C22_C31_boundary_row
    - 055550/2024: not_recomputed_this_turn_future_bank_capital_return_candidate
    - 086790/2024: not_recomputed_this_turn_future_bank_capital_return_candidate
    - 024110/2024: not_recomputed_this_turn_future_bank_capital_return_candidate
    - 138930/2024: not_recomputed_this_turn_future_regional_bank_valueup_candidate
    - 323410/2024: not_recomputed_this_turn_future_digital_bank_boundary
    - 039490/2024: not_recomputed_this_turn_future_brokerage_capital_return_candidate
    - 016360/2024: not_recomputed_this_turn_future_brokerage_capital_return_candidate
    - 071050/2024: not_recomputed_this_turn_future_brokerage_holdco_candidate
    - 001450/2024: not_recomputed_this_turn_future_C22_insurance_boundary
    - 000810/2024: not_recomputed_this_turn_future_C22_insurance_boundary
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
loop_objective:
  - holdout_validation
  - duplicate_low_value_loop_marker
  - ROE_PBR_valueup_to_executed_capital_return_gate
  - bank_CET1_payout_buyback_credit_cost_bridge
  - securities_capital_return_positive_vs_lowPBR_label_false_positive_split
  - insurance_reserve_C22_reclassification_guard
price_source: Songdaiki/stock-web
price_data_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

`C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN` remains Priority 0. The current no-repeat index marks C21 at only 6 representative rows, so it remains below the 30-row minimum. The v12 scheduler maps C21~C22 to `R6 / L6_FINANCIAL_CAPITAL_RETURN_DIGITAL`.

This file continues the local C21 sequence after `R6/C21 loop 114`; selected loop is therefore `115`.

This is a **dedupe-aware holdout validation / cache-miss TODO** MD. It does not claim fresh independent stock-web evidence. Direct fresh C21 financial capital-return candidate shards were not recomputed in this execution, so the trigger rows below reuse current-session stock-web-derived C21/C22/C31/C32 boundary rows that already contain complete 30D/90D/180D MFE and MAE from `Songdaiki/stock-web` tradable OHLC. Exact duplicate `same_entry_group_id` rows should be deduped during batch ingest. No production scoring is changed.

---

## 1. Research thesis

```yaml
loop_115_note:
  independence_status: duplicate_holdout_only
  fresh_reprice_status: not_recomputed_this_execution
  reason: C21 remains under-covered, but this run reuses prior C21/C22/C31/C32 boundary rows and must not create a new weight delta.
```


C21 should not reward `low PBR`, `value-up`, `financial holding`, or `shareholder return` as labels.

C21 should reward capital-return execution when ROE/PBR discount closes through financial plumbing:

```text
low PBR / value-up / shareholder return / ROE discount / capital policy
→ CET1 or solvency capacity
→ payout, buyback, cancellation, DPS visibility
→ sustainable ROE and credit cost
→ earnings quality and balance-sheet risk
→ actual capital return execution
→ price path validation
```

The recurring false positive is:

```text
low-PBR label
value-up policy headline
financial beta
brokerage cheapness
insurance reserve or CSM mechanics misfiled as generic value-up
capital-return promise without cancellation or payout execution
```

C21 is not a “cheap stock” bucket. It is a capital-return execution bucket. A financial stock can look cheap for years if ROE is weak, credit cost rises, solvency is constrained, or buybacks are not retired. The model should therefore score the cash leaving the balance sheet, not the slogan on the slide.

The route split in this holdout:

```text
securities or bank capital-return execution with contained MAE
→ Stage2 can survive

bank value-up with partial execution but credit-cost/CET1 uncertainty
→ local 4B, no Green

low-PBR bank value-up label without differentiated execution
→ Stage2-Watch cap

brokerage label without capital-return execution
→ hard 4C

insurance reserve/capital-return bridge
→ positive elsewhere, but reclassify to C22/C31 if reserve/CSM/solvency dominates

life-insurance value-up label without CSM/solvency/payout proof
→ Stage2 cap
```

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 6
  actual_trigger_rows: 6
  narrative_only_future_todo_rows: 1
  source_archetypes:
    - C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
    - C22_INSURANCE_RATE_CYCLE_RESERVE
    - C31_POLICY_SUBSIDY_LEGISLATION_EVENT
    - C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
    - R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
    - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
    - R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
    - R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
  price_windows:
    - 30D MFE/MAE
    - 90D MFE/MAE
    - 180D MFE/MAE
  output_use:
    - C21 holdout validation
    - value-up-to-executed-capital-return gate
    - low-PBR false-positive guard
    - insurance reserve reclassification guard
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
  - R6/C21 loops 112~114
  - R6/C22 loops 111~112
  - R11/C31 loops 103~109
  - R12/C32 loops 104~109
  - R13 accounting-trust loops 12~14
  - R13 Stage2 false-positive loop 11
  - R13 high-MAE loop 9
  - R13 4B/4C loop 104
reason:
  - all reused rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - direct fresh C21 financial capital-return candidate shards were not recomputed in this execution
  - exact duplicate C21 keys should be deduped during batch ingest
  - this file is holdout validation / duplicate-low-value evidence only
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","selected_round":"R6","selected_loop":115,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"SECURITIES_CAPITAL_RETURN_EXECUTION_POSITIVE_CONTROL","symbol":"005940","name":"NH투자증권","trigger_type":"Stage2-Actionable","entry_date":"2024-02-26","entry_price":11420,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":14.71,"MAE_30D_pct":-2.36,"MFE_90D_pct":14.71,"MAE_90D_pct":-2.36,"MFE_180D_pct":26.09,"MAE_180D_pct":-2.36,"forward_high_30d":13100,"forward_low_30d":11150,"forward_high_90d":13100,"forward_low_90d":11150,"forward_high_180d":14400,"forward_low_180d":11150,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C21|005940|Stage2-Actionable|2024-02-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control","reuse_reason":"same securities capital-return positive row from C21/C32 boundary guardrails","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"securities_capital_return_positive_control","novelty_key":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|005940|Stage2-Actionable|2024-02-26","non_price_bridge":"securities ROE/PBR capital-return bridge with contained MAE and later 180D validation","score_alignment":"Stage2 can survive; Green requires payout/buyback/cancellation and ROE sustainability refresh"}
{"row_type":"trigger","selected_round":"R6","selected_loop":115,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUEUP_CAPITAL_RETURN_PARTIAL_EXECUTION_LOCAL_4B","symbol":"105560","name":"KB금융","trigger_type":"Stage4B","entry_date":"2024-07-26","entry_price":87900,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.12,"MAE_30D_pct":-15.81,"MFE_90D_pct":18.20,"MAE_90D_pct":-15.81,"MFE_180D_pct":18.20,"MAE_180D_pct":-15.81,"forward_high_30d":92400,"forward_low_30d":74000,"forward_high_90d":103900,"forward_low_90d":74000,"forward_high_180d":103900,"forward_low_180d":74000,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C21|105560|Stage4B|2024-07-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_bank_4B","reuse_reason":"same KB value-up/capital-return local-4B row from C21/C31/C32 guardrails","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"bank_valueup_capital_return_local_4B","novelty_key":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|105560|Stage4B|2024-07-26","non_price_bridge":"bank value-up and capital-return bridge exists, but CET1, payout, buyback/cancellation, credit-cost and earnings refresh are required","score_alignment":"local 4B; block Green until capital-return execution and credit-cost bridge refresh"}
{"row_type":"trigger","selected_round":"R6","selected_loop":115,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"LOW_PBR_BANK_VALUEUP_LABEL_WITHOUT_DIFFERENTIATED_EXECUTION_CAP","symbol":"316140","name":"우리금융지주","trigger_type":"Stage2-Watch","entry_date":"2024-07-26","entry_price":16180,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.08,"MAE_30D_pct":-15.08,"MFE_90D_pct":5.69,"MAE_90D_pct":-15.08,"MFE_180D_pct":5.69,"MAE_180D_pct":-15.08,"forward_high_30d":16840,"forward_low_30d":13740,"forward_high_90d":17100,"forward_low_90d":13740,"forward_high_180d":17100,"forward_low_180d":13740,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C21|316140|Stage2-Watch|2024-07-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_label_cap","reuse_reason":"same low-PBR bank value-up cap row from C21/C31/C32 guardrails","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"low_PBR_valueup_label_cap","novelty_key":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|316140|Stage2-Watch|2024-07-26","non_price_bridge":"low-PBR bank value-up label without differentiated payout, buyback, cancellation, CET1 or ROE execution bridge","score_alignment":"Stage2-Watch/cap; require incremental capital-return execution before Actionable"}
{"row_type":"trigger","selected_round":"R6","selected_loop":115,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"LOW_PBR_BROKERAGE_LABEL_WITHOUT_CAPITAL_RETURN_EXECUTION_HARD_4C","symbol":"006800","name":"미래에셋증권","trigger_type":"Stage4C","entry_date":"2024-02-26","entry_price":8680,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.53,"MAE_30D_pct":-10.71,"MFE_90D_pct":5.53,"MAE_90D_pct":-20.16,"MFE_180D_pct":5.53,"MAE_180D_pct":-23.96,"forward_high_30d":9160,"forward_low_30d":7750,"forward_high_90d":9160,"forward_low_90d":6930,"forward_high_180d":9160,"forward_low_180d":6600,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C21|006800|Stage4C|2024-02-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","reuse_reason":"same low-PBR brokerage hard-block row from C21/C32 guardrails","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"brokerage_label_without_execution_hard_4C","novelty_key":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|006800|Stage4C|2024-02-26","non_price_bridge":"low-PBR brokerage / shareholder-return label lacked capital-return execution and suffered weak MFE with deep 90D MAE","score_alignment":"hard 4C; cheapness or value-up language alone failed"}
{"row_type":"trigger","selected_round":"R6","selected_loop":115,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"NONLIFE_RESERVE_CAPITAL_RETURN_POSITIVE_ELSEWHERE_RECLASSIFY_C22","symbol":"005830","name":"DB손해보험","trigger_type":"Stage2-Actionable","entry_date":"2024-02-26","entry_price":95000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.79,"MAE_30D_pct":-4.11,"MFE_90D_pct":27.05,"MAE_90D_pct":-9.26,"MFE_180D_pct":30.53,"MAE_180D_pct":-9.26,"forward_high_30d":110000,"forward_low_30d":91100,"forward_high_90d":120700,"forward_low_90d":86200,"forward_high_180d":124000,"forward_low_180d":86200,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C21|005830|Stage2-Actionable|2024-02-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_elsewhere","reuse_reason":"same DB Insurance positive row from C22/C31/C32 controls, reused as C21 boundary","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"insurance_capital_return_positive_elsewhere","novelty_key":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|005830|Stage2-Actionable|2024-02-26","non_price_bridge":"nonlife reserve quality, loss-ratio discipline and capital-return bridge; positive but more specific to C22 reserve/capital mechanics","score_alignment":"Stage2 can survive if capital-return bridge dominates; reclassify to C22 if reserve/CSM/solvency mechanics dominate"}
{"row_type":"trigger","selected_round":"R6","selected_loop":115,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"LIFE_INSURANCE_VALUEUP_LABEL_WITHOUT_CSM_SOLVENCY_PAYOUT_CAP","symbol":"088350","name":"한화생명","trigger_type":"Stage2-Watch","entry_date":"2024-02-26","entry_price":3060,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.31,"MAE_30D_pct":-8.17,"MFE_90D_pct":9.31,"MAE_90D_pct":-15.69,"MFE_180D_pct":9.31,"MAE_180D_pct":-15.69,"forward_high_30d":3345,"forward_low_30d":2810,"forward_high_90d":3345,"forward_low_90d":2580,"forward_high_180d":3345,"forward_low_180d":2580,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C21|088350|Stage2-Watch|2024-02-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_life_insurance_cap","reuse_reason":"same life-insurance value-up cap row from C21/C22/C31 controls","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"life_insurance_valueup_cap","novelty_key":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|088350|Stage2-Watch|2024-02-26","non_price_bridge":"life-insurance value-up label without refreshed CSM, solvency, reserve quality or payout bridge","score_alignment":"cap C21 contribution; require CSM/solvency/payout evidence or reclassify to C22"}
```

---

## 5. Narrative-only future TODO

```jsonl
{"row_type":"narrative_only_future_todo","selected_round":"R6","selected_loop":115,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"C21_NEW_FINANCIAL_CAPITAL_RETURN_REPRICE_TODO_AFTER_CACHE_MISS","candidate_symbols":["055550","086790","024110","138930","323410","039490","016360","071050","001450","000810"],"candidate_names":["신한지주","하나금융지주","기업은행","BNK금융지주","카카오뱅크","키움증권","삼성증권","한국금융지주","현대해상","삼성화재"],"why_not_trigger_row_now":"fresh stock-web symbol-year shards for new C21 financial capital-return candidates were not recomputed in this execution; no fresh 30D/90D/180D MFE/MAE computed here","calibration_usable":false,"score_alignment":"future run should compute stock-web windows before counting these as new C21 evidence; distinguish value-up label from executed payout, buyback cancellation, CET1/solvency, ROE sustainability and credit-cost control"}
```

---

## 6. Case analysis

### 6.1 NH Investment & Securities / 005940 — securities capital-return positive-control

```yaml
entry_price: 11420
90D_MFE_MAE: +14.71 / -2.36
180D_MFE_MAE: +26.09 / -2.36
route: Stage2-Actionable
```

This row is a positive-control for C21. The 90D path was modest, but the drawdown stayed shallow and the 180D path validated the capital-return setup. It should remain Stage2 rather than Green unless payout, buyback/cancellation and ROE sustainability are refreshed.

### 6.2 KB Financial / 105560 — bank value-up local 4B

```yaml
entry_price: 87900
90D_MFE_MAE: +18.20 / -15.81
180D_MFE_MAE: +18.20 / -15.81
route: Stage4B
```

The capital-return bridge exists, but the entry still needs CET1, payout, buyback/cancellation, credit-cost and earnings-quality confirmation. The lesson is not “block all banks”; it is “do not Green a value-up bank before execution is visible.”

### 6.3 Woori Financial / 316140 — low-PBR label cap

```yaml
entry_price: 16180
90D_MFE_MAE: +5.69 / -15.08
180D_MFE_MAE: +5.69 / -15.08
route: Stage2-Watch / cap
```

This row is the label trap. Low PBR and value-up language alone did not become a strong price path.

### 6.4 Mirae Asset Securities / 006800 — brokerage hard 4C

```yaml
entry_price: 8680
90D_MFE_MAE: +5.53 / -20.16
180D_MFE_MAE: +5.53 / -23.96
route: Stage4C
```

This is the hard counterexample: cheapness without executed capital return failed.

### 6.5 DB Insurance / 005830 — positive but C22 boundary

```yaml
entry_price: 95000
90D_MFE_MAE: +27.05 / -9.26
180D_MFE_MAE: +30.53 / -9.26
route: Stage2-Actionable / C22 boundary
```

This row can help C21, but if the real evidence is reserve quality, loss-ratio discipline and solvency, C22 is the sharper bucket.

### 6.6 Hanwha Life / 088350 — life-insurance value-up cap

```yaml
entry_price: 3060
90D_MFE_MAE: +9.31 / -15.69
180D_MFE_MAE: +9.31 / -15.69
route: Stage2-Watch / cap
```

Life-insurance value-up needs CSM, solvency, reserve and payout proof. The label alone is not enough.

---

## 7. Score-return alignment

```yaml
new_independent_case_count: 0
reused_case_count: 6
new_symbol_count: 0
same_archetype_new_symbol_count: 0
same_archetype_new_trigger_family_count: 0
new_trigger_family_count: 0
narrative_only_future_todo_count: 1
calibration_usable_case_count: 6
calibration_usable_trigger_count: 6
positive_case_count: 2
counterexample_count: 4
local_4B_watch_count: 1
hard_4C_count: 1
wrong_archetype_reclassification_count: 2
current_profile_error_count: 4
diversity_score_summary: "securities capital-return positive, bank value-up 4B, low-PBR bank cap, brokerage hard 4C, nonlife insurance positive boundary, life-insurance value-up cap covered; all rows reused"
loop_contribution_label: duplicate_low_value_loop_with_cache_miss_todo
do_not_propose_new_weight_delta: true
```

| symbol | role | 90D MFE/MAE | 180D MFE/MAE | C21 lesson |
|---|---:|---:|---:|---|
| 005940 | securities positive | +14.71 / -2.36 | +26.09 / -2.36 | capital-return execution can validate |
| 105560 | bank value-up 4B | +18.20 / -15.81 | +18.20 / -15.81 | execution refresh needed |
| 316140 | low-PBR cap | +5.69 / -15.08 | +5.69 / -15.08 | label not enough |
| 006800 | brokerage 4C | +5.53 / -20.16 | +5.53 / -23.96 | cheapness failed |
| 005830 | insurance positive boundary | +27.05 / -9.26 | +30.53 / -9.26 | positive but may be C22 |
| 088350 | life value-up cap | +9.31 / -15.69 | +9.31 / -15.69 | CSM/solvency/payout required |

---

## 8. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"005940","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"capital_return_execution":4,"roe_quality":3,"pbr_discount_closure":3,"capital_adequacy":3,"credit_cost_risk":2,"earnings_quality":3,"relative_strength":2,"policy_valueup_support":2,"execution_risk":2,"accounting_trust_risk":2},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"capital_return_execution":4,"roe_quality":3,"pbr_discount_closure":3,"capital_adequacy":3,"credit_cost_risk":2,"earnings_quality":3,"relative_strength":2,"policy_valueup_support":1,"execution_risk":2,"accounting_trust_risk":2},"weighted_score_after":72,"stage_label_after":"Stage2-Actionable_GreenBlocked","changed_components":["policy_valueup_support"],"component_delta_explanation":"Contained MAE and later 180D validation support Stage2, but Green requires executed payout/buyback/cancellation refresh.","MFE_90D_pct":14.71,"MAE_90D_pct":-2.36,"score_return_alignment_label":"securities_capital_return_positive","current_profile_verdict":"current_profile_correct_if_green_blocked"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"105560","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"capital_return_execution":3,"roe_quality":3,"pbr_discount_closure":4,"capital_adequacy":3,"credit_cost_risk":4,"earnings_quality":3,"relative_strength":3,"policy_valueup_support":4,"execution_risk":3,"accounting_trust_risk":3},"weighted_score_before":77,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"capital_return_execution":3,"roe_quality":2,"pbr_discount_closure":2,"capital_adequacy":3,"credit_cost_risk":4,"earnings_quality":2,"relative_strength":2,"policy_valueup_support":2,"execution_risk":4,"accounting_trust_risk":4},"weighted_score_after":64,"stage_label_after":"Stage4B_capital_return_refresh","changed_components":["roe_quality","pbr_discount_closure","earnings_quality","relative_strength","policy_valueup_support","execution_risk","accounting_trust_risk"],"component_delta_explanation":"Bank value-up bridge existed but execution/credit-cost evidence was insufficient for Actionable or Green.","MFE_90D_pct":18.20,"MAE_90D_pct":-15.81,"score_return_alignment_label":"bank_valueup_local_4B","current_profile_verdict":"current_profile_too_generous_if_actionable"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"316140","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"capital_return_execution":2,"roe_quality":2,"pbr_discount_closure":3,"capital_adequacy":2,"credit_cost_risk":4,"earnings_quality":2,"relative_strength":1,"policy_valueup_support":4,"execution_risk":3,"accounting_trust_risk":4},"weighted_score_before":68,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"capital_return_execution":1,"roe_quality":1,"pbr_discount_closure":1,"capital_adequacy":2,"credit_cost_risk":4,"earnings_quality":1,"relative_strength":0,"policy_valueup_support":2,"execution_risk":4,"accounting_trust_risk":5},"weighted_score_after":47,"stage_label_after":"Stage2_cap","changed_components":["capital_return_execution","roe_quality","pbr_discount_closure","earnings_quality","relative_strength","policy_valueup_support","execution_risk","accounting_trust_risk"],"component_delta_explanation":"Low-PBR/value-up label lacked differentiated capital-return execution and price path was weak.","MFE_90D_pct":5.69,"MAE_90D_pct":-15.08,"score_return_alignment_label":"low_PBR_valueup_cap","current_profile_verdict":"current_profile_false_positive_if_actionable"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"006800","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"capital_return_execution":1,"roe_quality":1,"pbr_discount_closure":2,"capital_adequacy":2,"credit_cost_risk":3,"earnings_quality":1,"relative_strength":1,"policy_valueup_support":2,"execution_risk":4,"accounting_trust_risk":4},"weighted_score_before":60,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"capital_return_execution":0,"roe_quality":0,"pbr_discount_closure":0,"capital_adequacy":1,"credit_cost_risk":4,"earnings_quality":0,"relative_strength":0,"policy_valueup_support":0,"execution_risk":5,"accounting_trust_risk":5},"weighted_score_after":38,"stage_label_after":"Stage4C","changed_components":["capital_return_execution","roe_quality","pbr_discount_closure","capital_adequacy","credit_cost_risk","earnings_quality","relative_strength","policy_valueup_support","execution_risk","accounting_trust_risk"],"component_delta_explanation":"Brokerage cheapness/value-up label lacked executed capital return and 90D MAE breached hard-block threshold.","MFE_90D_pct":5.53,"MAE_90D_pct":-20.16,"score_return_alignment_label":"brokerage_label_hard_4C","current_profile_verdict":"current_profile_false_positive_if_stage2"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"005830","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"capital_return_execution":4,"roe_quality":4,"pbr_discount_closure":4,"capital_adequacy":4,"credit_cost_risk":1,"earnings_quality":4,"relative_strength":4,"policy_valueup_support":3,"execution_risk":2,"accounting_trust_risk":1},"weighted_score_before":85,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"capital_return_execution":3,"roe_quality":3,"pbr_discount_closure":3,"capital_adequacy":3,"credit_cost_risk":1,"earnings_quality":3,"relative_strength":3,"policy_valueup_support":2,"execution_risk":2,"accounting_trust_risk":2},"weighted_score_after":74,"stage_label_after":"Stage2_Actionable_reclassify_C22_boundary","changed_components":["capital_return_execution","roe_quality","pbr_discount_closure","capital_adequacy","earnings_quality","relative_strength","policy_valueup_support","accounting_trust_risk"],"component_delta_explanation":"Capital-return path is positive, but dominant reserve/loss-ratio/solvency mechanics may belong to C22.","MFE_90D_pct":27.05,"MAE_90D_pct":-9.26,"score_return_alignment_label":"insurance_positive_boundary","current_profile_verdict":"requires_C22_reclassification_if_reserve_dominates"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"088350","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"capital_return_execution":1,"roe_quality":1,"pbr_discount_closure":2,"capital_adequacy":2,"credit_cost_risk":2,"earnings_quality":1,"relative_strength":1,"policy_valueup_support":3,"execution_risk":3,"accounting_trust_risk":4},"weighted_score_before":66,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"capital_return_execution":0,"roe_quality":0,"pbr_discount_closure":0,"capital_adequacy":1,"credit_cost_risk":2,"earnings_quality":0,"relative_strength":0,"policy_valueup_support":1,"execution_risk":4,"accounting_trust_risk":5},"weighted_score_after":44,"stage_label_after":"Stage2_cap","changed_components":["capital_return_execution","roe_quality","pbr_discount_closure","capital_adequacy","earnings_quality","relative_strength","policy_valueup_support","execution_risk","accounting_trust_risk"],"component_delta_explanation":"Life-insurance value-up label lacked CSM/solvency/payout evidence, so generic C21 credit is capped.","MFE_90D_pct":9.31,"MAE_90D_pct":-15.69,"score_return_alignment_label":"life_valueup_cap","current_profile_verdict":"current_profile_false_positive_if_actionable"}
```

---

## 9. Current calibrated profile stress test

The C21 ROE/PBR-to-capital-return gate held:

```text
securities capital-return with shallow MAE and later validation
→ Stage2 can survive, Green blocked until execution proof

bank value-up with partial execution and mid-teen MAE
→ local 4B, no Green

low-PBR bank label without differentiated payout/buyback execution
→ Stage2-Watch cap

brokerage cheapness without capital-return execution
→ hard 4C

insurance reserve/capital-return positive
→ useful boundary, but reclassify to C22 if reserve/CSM/solvency dominates

life-insurance value-up label without CSM/solvency/payout
→ Stage2 cap
```

### Rule candidate retained, not newly proposed

```text
C21_ROE_PBR_VALUEUP_CAPITAL_RETURN_EXECUTION_GATE_V115_HELD_OUT

if C21
and lowPBR_valueup_financial_or_shareholder_return_label == true
and executed_payout_buyback_cancellation_CET1_solvency_ROE_or_credit_cost_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C21
and capital_return_execution_bridge == true
and MFE_180D_pct >= +20
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
    block_stage3_green_until_payout_buyback_cancellation_refresh = true
```

```text
if C21
and bank_valueup_bridge == partial
and MAE_90D_pct <= -15
and credit_cost_or_CET1_bridge == unrefreshed:
    local_4B_watch = true
    block_stage3_green = true
```

```text
if C21
and lowPBR_or_valueup_label == true
and MFE_90D_pct < +10
and MAE_90D_pct <= -20:
    route = Stage4C
```

```text
if C21
and insurance_reserve_CSM_solvency_driver_dominates == true:
    cap_C21_contribution = true
    require_reclassification_to_C22 = true
```

---

## 10. Profile comparison shadow-only summary

```yaml
profile_comparison:
  P0_e2r_2_2_rolling_calibrated_proxy:
    hypothesis: current rolling profile with bridge/4B/4C guards
    eligible_trigger_count: 6
    avg_MFE_90D_pct: 13.42
    avg_MAE_90D_pct: -13.06
    false_positive_risk: high_if_valueup_or_lowPBR_label_is_left_actionable
    verdict: adequate_only_with_C21_execution_gate
  P0b_e2r_2_1_reference:
    hypothesis: prior calibrated profile may overcredit low-PBR/value-up labels
    eligible_trigger_count: 6
    false_positive_risk: higher
    verdict: inferior
  P1_sector_specific_candidate_profile:
    hypothesis: L6 financial rows require executed capital-return and balance-sheet capacity
    changed_axes: none_new_holdout_only
    verdict: pass_holdout
  P2_canonical_archetype_candidate_profile:
    hypothesis: C21 requires payout/buyback/cancellation and ROE sustainability, not cheapness
    changed_axes: none_new_holdout_only
    verdict: pass_holdout
  P3_counterexample_guard_profile:
    hypothesis: low-PBR brokerage/bank labels without execution route cap/4C
    changed_axes: none_new_holdout_only
    verdict: strongest_for_false_positive_control
```

---

## 11. Coverage matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---:|
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | ROE_PBR_VALUEUP_CAPITAL_RETURN_EXECUTION_HOLDOUT_V115 | 2 | 4 | 1 | 1 | 0 | 6 | 6 | 0 | 4 | false | false | 24 |

---

## 12. Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 6
calibration_usable_trigger_count: 6
representative_trigger_count: 0
new_weight_evidence_candidate_count: 0
guardrail_candidate_count: 6
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
reused_case_count: 6
reused_case_ids:
  - C21|005940|Stage2-Actionable|2024-02-26
  - C21|105560|Stage4B|2024-07-26
  - C21|316140|Stage2-Watch|2024-07-26
  - C21|006800|Stage4C|2024-02-26
  - C21|005830|Stage2-Actionable|2024-02-26
  - C21|088350|Stage2-Watch|2024-02-26
new_symbol_count: 0
new_trigger_family_count: 0
narrative_only_future_todo_count: 1
tested_existing_calibrated_axes:
  - stage2_required_bridge
  - local_4b_watch_guard
  - hard_4c_thesis_break_routes_to_4c
  - C21_ROE_PBR_valueup_capital_return_execution_gate
  - C22_insurance_reclassification_guard
residual_error_types_found:
  - valueup_label_without_execution
  - lowPBR_bank_cap
  - brokerage_cheapness_hard_4C
  - insurance_reserve_wrong_archetype_boundary
  - direct_stock_web_shard_cache_miss_gap
new_axis_proposed: null
existing_axis_strengthened:
  - C21_ROE_PBR_VALUEUP_CAPITAL_RETURN_EXECUTION_GATE_V115_HELD_OUT
existing_axis_weakened: null
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
no_new_signal_reason: all rows reused holdout validation after direct fresh C21 financial capital-return candidate shards were not recomputed
loop_contribution_label: duplicate_low_value_loop_with_cache_miss_todo
do_not_propose_new_weight_delta: true
```

```jsonl
{"row_type":"residual_contribution","round":"R6","loop":"115","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","new_independent_case_count":0,"reused_case_count":6,"new_symbol_count":0,"new_trigger_family_count":0,"narrative_only_future_todo_count":1,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","hard_4c_thesis_break_routes_to_4c","C21_ROE_PBR_valueup_capital_return_execution_gate","C22_insurance_reclassification_guard"],"residual_error_types_found":["valueup_label_without_execution","lowPBR_bank_cap","brokerage_cheapness_hard_4C","insurance_reserve_wrong_archetype_boundary","direct_stock_web_shard_cache_miss_gap"],"loop_contribution_label":"duplicate_low_value_loop_with_cache_miss_todo","do_not_propose_new_weight_delta":true}
```

---

## 14. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Treat this R6/C21 loop 115 as holdout validation only. Batch it with C21 loops 112~114, C22 insurance boundary rows, C31 value-up policy rows, C32 governance reclassification rows, and R13 accounting-trust / Stage2 false-positive / high-MAE / 4B-4C guardrails. If exact same_entry_group_id rows already exist, dedupe them. Preserve the C21 ROE/PBR/value-up-to-executed-capital-return gate, low-PBR hard-4C/cap guard, and C22 insurance reserve reclassification guard, but do not create a new weight delta from this loop because no new independent case was added and direct C21 stock-web shards cache-missed. Future research should directly reprice 신한지주(055550), 하나금융지주(086790), 기업은행(024110), BNK금융지주(138930), 카카오뱅크(323410), 키움증권(039490), 삼성증권(016360), 한국금융지주(071050), 현대해상(001450), 삼성화재(000810), JB금융지주(175330), DGB금융지주(139130), 메리츠금융지주(138040) when stock-web shards are accessible.
```

---

## 15. Next research state

```yaml
completed_round: R6
completed_loop: 115
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C22_INSURANCE_RATE_CYCLE_RESERVE
  - C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
  - C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
  - C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
  - C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
```
