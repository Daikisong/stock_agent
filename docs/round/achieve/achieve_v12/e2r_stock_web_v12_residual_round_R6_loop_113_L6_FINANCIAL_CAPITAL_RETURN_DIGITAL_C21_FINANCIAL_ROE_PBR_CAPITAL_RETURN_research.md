# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R6
selected_loop: 113
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: VALUEUP_ROE_PBR_CAPITAL_RETURN_HOLDOUT_V113_BANK_SECURITIES_INSURANCE_RECLASSIFICATION_SPLIT
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
  stock_web_manifest: read_ok
  additional_financial_candidate_shards:
    - 055550/2024: not_recomputed_this_turn
    - 086790/2024: not_recomputed_this_turn
    - 138040/2024: not_recomputed_this_turn
    - 016360/2024: not_recomputed_this_turn
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
loop_objective:
  - holdout_validation
  - duplicate_low_value_loop_marker
  - ROE_PBR_valueup_to_executed_capital_return_gate
  - bank_CET1_payout_buyback_refresh_guard
  - securities_valueup_execution_vs_low_PBR_label_split
  - insurance_wrong_archetype_reclassification_guard
price_source: Songdaiki/stock-web
price_data_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

`C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN` remains Priority 0 in the no-repeat index. The v12 scheduler maps C21~C22 to `R6 / L6_FINANCIAL_CAPITAL_RETURN_DIGITAL`.

This file continues the local C21 sequence after previously referenced `R6/C21 loop 112`; selected loop is therefore `113`.

This is a **dedupe-aware holdout validation / cache-miss TODO** MD. It does not claim fresh independent stock-web evidence because additional bank/securities candidate shards were not recomputed in this execution. The trigger rows below reuse current-session stock-web-derived C21/C22/C31/C32 financial rows that already contain complete 30D/90D/180D MFE and MAE from `Songdaiki/stock-web` tradable OHLC. Exact duplicate `same_entry_group_id` rows should be deduped during batch ingest. No production scoring is changed.

---

## 1. Research thesis

C21 is not simply `low PBR` or `Value-up`.

C21 should reward financial capital return only when it passes into executable shareholder economics:

```text
ROE / PBR / Value-up / capital policy label
→ capital adequacy
→ payout / buyback / cancellation / DPS
→ ROE or cost discipline
→ credit-cost / trading-income / fee-income quality
→ price path validation
```

The repeating false positive is:

```text
low PBR
sector-wide Value-up label
buyback language without size/timing/cancellation
bank capital-return headline without CET1/credit-cost refresh
securities label without earnings/revision bridge
insurance reserve/CSM bridge misfiled into C21
```

A cheap financial stock is like a discounted bond without a maturity date. C21 only pays when management writes the maturity date into actual capital-return execution.

This holdout pass validates six route types:

1. **Securities ROE/capital-return positive-control**
   - Stage2 can open when capital-return bridge and earnings/revision path are visible.

2. **Bank Value-up local 4B**
   - Real bridge may exist, but CET1, payout, buyback/cancellation and credit-cost refresh are required.

3. **Low-PBR bank label cap**
   - Sector-wide Value-up label without differentiated execution stays Watch/cap.

4. **Low-PBR brokerage hard 4C**
   - Cheapness without execution and weak price path should hard-block.

5. **Insurance reserve/capital-return positive elsewhere**
   - Positive financial row can be real, but belongs to C22/C31 if reserve/CSM/solvency is the bridge.

6. **Life insurance label cap**
   - Value-up label without CSM/solvency/payout bridge remains cap.

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
    - R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
    - R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
    - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
    - R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
  price_windows:
    - 30D MFE/MAE
    - 90D MFE/MAE
    - 180D MFE/MAE
  output_use:
    - C21 holdout validation
    - capital-return execution gate
    - bank/securities/insurance reclassification split
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
  - R6/C21 loop 112
  - R6/C22 loop 111
  - R11/C31 loops 103~108
  - R12/C32 loops 104~108
  - R13 accounting-trust loops 12~14
  - R13 Stage2 false-positive loop 11
  - R13 high-MAE loop 9
  - R13 4B/4C loop 104
reason:
  - all reused rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - additional C21 bank/securities candidates were not recomputed in this execution
  - exact duplicate C21 keys should be deduped during batch ingest
  - this file is holdout validation / duplicate-low-value evidence only
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","selected_round":"R6","selected_loop":113,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"SECURITIES_ROE_CAPITAL_RETURN_SLOW_POSITIVE_CONTROL","symbol":"005940","name":"NH투자증권","trigger_type":"Stage2-Actionable","entry_date":"2024-02-26","entry_price":11420,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":14.71,"MAE_30D_pct":-2.36,"MFE_90D_pct":14.71,"MAE_90D_pct":-2.36,"MFE_180D_pct":26.09,"MAE_180D_pct":-2.36,"forward_high_30d":13100,"forward_low_30d":11150,"forward_high_90d":13100,"forward_low_90d":11150,"forward_high_180d":14400,"forward_low_180d":11150,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C21|005940|Stage2-Actionable|2024-02-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_slow_positive","reuse_reason":"same financial capital-return positive row previously used as C32 reclassification control","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"securities_capital_return_slow_positive","novelty_key":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|005940|Stage2-Actionable|2024-02-26","non_price_bridge":"securities ROE/PBR capital-return bridge with contained MAE and delayed 180D validation","score_alignment":"Stage2 can open; Green requires payout/buyback and earnings/revision refresh"}
{"row_type":"trigger","selected_round":"R6","selected_loop":113,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUEUP_CAPITAL_RETURN_REAL_BRIDGE_LOCAL_4B","symbol":"105560","name":"KB금융","trigger_type":"Stage4B","entry_date":"2024-07-26","entry_price":87900,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.12,"MAE_30D_pct":-15.81,"MFE_90D_pct":18.20,"MAE_90D_pct":-15.81,"MFE_180D_pct":18.20,"MAE_180D_pct":-15.81,"forward_high_30d":92400,"forward_low_30d":74000,"forward_high_90d":103900,"forward_low_90d":74000,"forward_high_180d":103900,"forward_low_180d":74000,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C21|105560|Stage4B|2024-07-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_local_4B","reuse_reason":"same KB capital-return local-4B row from C31/C32 guardrails","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"bank_capital_return_local_4B","novelty_key":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|105560|Stage4B|2024-07-26","non_price_bridge":"bank Value-up and capital-return bridge, but CET1, payout, buyback/cancellation, credit-cost and earnings refresh required","score_alignment":"local 4B until capital-return execution and credit-cost bridge refresh"}
{"row_type":"trigger","selected_round":"R6","selected_loop":113,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"LOW_PBR_BANK_VALUEUP_LABEL_WITHOUT_DIFFERENTIATED_EXECUTION_CAP","symbol":"316140","name":"우리금융지주","trigger_type":"Stage2-Watch","entry_date":"2024-07-26","entry_price":16180,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.08,"MAE_30D_pct":-15.08,"MFE_90D_pct":5.69,"MAE_90D_pct":-15.08,"MFE_180D_pct":5.69,"MAE_180D_pct":-15.08,"forward_high_30d":16840,"forward_low_30d":13740,"forward_high_90d":17100,"forward_low_90d":13740,"forward_high_180d":17100,"forward_low_180d":13740,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C21|316140|Stage2-Watch|2024-07-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_stage2_cap","reuse_reason":"same low-PBR bank cap row from C31 loops","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"low_PBR_bank_cap","novelty_key":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|316140|Stage2-Watch|2024-07-26","non_price_bridge":"low-PBR bank Value-up label without differentiated payout, buyback, CET1 or ROE execution bridge","score_alignment":"Stage2-Watch/cap; require incremental capital-return execution before Actionable"}
{"row_type":"trigger","selected_round":"R6","selected_loop":113,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"LOW_PBR_BROKERAGE_LABEL_WITHOUT_CAPITAL_RETURN_EXECUTION_HARD_4C","symbol":"006800","name":"미래에셋증권","trigger_type":"Stage4C","entry_date":"2024-02-26","entry_price":8680,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.53,"MAE_30D_pct":-10.71,"MFE_90D_pct":5.53,"MAE_90D_pct":-20.16,"MFE_180D_pct":5.53,"MAE_180D_pct":-23.96,"forward_high_30d":9160,"forward_low_30d":7750,"forward_high_90d":9160,"forward_low_90d":6930,"forward_high_180d":9160,"forward_low_180d":6600,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C21|006800|Stage4C|2024-02-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","reuse_reason":"same low-PBR brokerage hard-block row from C32/C21 guardrails","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"low_PBR_brokerage_hard_4C","novelty_key":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|006800|Stage4C|2024-02-26","non_price_bridge":"low-PBR brokerage label lacked capital-return execution, earnings revision, buyback/cancellation or ROE bridge","score_alignment":"hard 4C; cheapness alone failed C21 capital-return gate"}
{"row_type":"trigger","selected_round":"R6","selected_loop":113,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"NONLIFE_RESERVE_CAPITAL_RETURN_POSITIVE_ELSEWHERE_RECLASSIFY_C22","symbol":"005830","name":"DB손해보험","trigger_type":"Stage2-Watch","entry_date":"2024-02-26","entry_price":95000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.79,"MAE_30D_pct":-4.11,"MFE_90D_pct":27.05,"MAE_90D_pct":-9.26,"MFE_180D_pct":30.53,"MAE_180D_pct":-9.26,"forward_high_30d":110000,"forward_low_30d":91100,"forward_high_90d":120700,"forward_low_90d":86200,"forward_high_180d":124000,"forward_low_180d":86200,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C21|005830|Stage2-Watch|2024-02-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_wrong_archetype_positive_elsewhere","reuse_reason":"same DB Insurance positive row from C22/C31/C32 reclassification controls","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"insurance_positive_elsewhere","novelty_key":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|005830|Stage2-Watch|2024-02-26","non_price_bridge":"nonlife reserve quality, loss-ratio discipline and capital-return bridge; positive but more specific to C22/C31 than C21","score_alignment":"cap C21 contribution; reclassify to C22/C31 rather than learn as generic C21"}
{"row_type":"trigger","selected_round":"R6","selected_loop":113,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"LIFE_INSURANCE_VALUEUP_LABEL_WITHOUT_CSM_SOLVENCY_PAYOUT_CAP","symbol":"088350","name":"한화생명","trigger_type":"Stage2-Watch","entry_date":"2024-02-26","entry_price":3060,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.31,"MAE_30D_pct":-8.17,"MFE_90D_pct":9.31,"MAE_90D_pct":-15.69,"MFE_180D_pct":9.31,"MAE_180D_pct":-15.69,"forward_high_30d":3345,"forward_low_30d":2810,"forward_high_90d":3345,"forward_low_90d":2580,"forward_high_180d":3345,"forward_low_180d":2580,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C21|088350|Stage2-Watch|2024-02-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_stage2_cap","reuse_reason":"same life-insurance Value-up cap row from C31/C32 controls","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"life_insurance_label_cap","novelty_key":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|088350|Stage2-Watch|2024-02-26","non_price_bridge":"life-insurance Value-up label without refreshed CSM, solvency, reserve quality or payout bridge","score_alignment":"cap C21 contribution; require CSM/solvency/payout evidence or reclassify to C22"}
```

---

## 5. Narrative-only future TODO

```jsonl
{"row_type":"narrative_only_future_trigger_todo","selected_round":"R6","selected_loop":113,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"C21_BANK_SECURITIES_NEW_SYMBOL_REPRICE_TODO","candidate_symbols":["055550","086790","138040","016360","039490"],"candidate_names":["신한지주","하나금융지주","메리츠금융지주","삼성증권","키움증권"],"why_not_trigger_row_now":"stock-web symbol-year shards were not recomputed in this execution; no fresh 30D/90D/180D MFE/MAE computed here","calibration_usable":false,"score_alignment":"future run should compute stock-web windows before counting these as new C21 evidence"}
```

---

## 6. Case analysis

### 6.1 NH Investment & Securities / 005940 — securities slow positive

NH is the cleaner securities positive-control in this holdout set. The 90D move was modest, but 180D validation and contained MAE support Stage2 if capital-return execution is refreshed.

```yaml
entry_close: 11420
90D_MFE_MAE: +14.71 / -2.36
180D_MFE_MAE: +26.09 / -2.36
route: Stage2-Actionable with Green blocked
```

### 6.2 KB Financial / 105560 — bank capital-return local 4B

KB has a real Value-up/capital-return bridge, but the row needs CET1, credit-cost, payout and buyback/cancellation refresh.

```yaml
entry_close: 87900
90D_MFE_MAE: +18.20 / -15.81
180D_MFE_MAE: +18.20 / -15.81
route: Stage4B
```

### 6.3 Woori Financial / 316140 — low-PBR bank cap

The policy/low-PBR label is not enough without differentiated execution.

```yaml
entry_close: 16180
90D_MFE_MAE: +5.69 / -15.08
180D_MFE_MAE: +5.69 / -15.08
route: Stage2-Watch / cap
```

### 6.4 Mirae Asset Securities / 006800 — low-PBR brokerage hard 4C

Cheapness did not become shareholder-return execution.

```yaml
entry_close: 8680
90D_MFE_MAE: +5.53 / -20.16
180D_MFE_MAE: +5.53 / -23.96
route: Stage4C
```

### 6.5 DB Insurance / 005830 — positive elsewhere, not generic C21

DB Insurance validates financial capital-return quality, but the more precise bridge is C22/C31.

```yaml
entry_close: 95000
90D_MFE_MAE: +27.05 / -9.26
180D_MFE_MAE: +30.53 / -9.26
route: Reclassify to C22/C31
```

### 6.6 Hanwha Life / 088350 — life insurance cap

A life-insurance Value-up label needs CSM, solvency and payout proof.

```yaml
entry_close: 3060
90D_MFE_MAE: +9.31 / -15.69
180D_MFE_MAE: +9.31 / -15.69
route: Stage2-Watch / cap
```

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
diversity_score_summary: "securities positive, bank 4B, low-PBR bank cap, brokerage hard 4C, insurance reclassification and life cap covered; all rows reused"
loop_contribution_label: duplicate_low_value_loop_with_cache_miss_todo
do_not_propose_new_weight_delta: true
```

| symbol | role | 90D MFE/MAE | 180D MFE/MAE | C21 lesson |
|---|---:|---:|---:|---|
| 005940 | securities slow positive | +14.71 / -2.36 | +26.09 / -2.36 | capital-return bridge can survive |
| 105560 | bank local 4B | +18.20 / -15.81 | +18.20 / -15.81 | refresh CET1/payout/credit-cost |
| 316140 | bank cap | +5.69 / -15.08 | +5.69 / -15.08 | low-PBR label not enough |
| 006800 | brokerage hard 4C | +5.53 / -20.16 | +5.53 / -23.96 | cheapness failed |
| 005830 | positive elsewhere | +27.05 / -9.26 | +30.53 / -9.26 | reclassify C22/C31 |
| 088350 | life cap | +9.31 / -15.69 | +9.31 / -15.69 | CSM/solvency/payout needed |

---

## 8. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"005940","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":3,"customer_quality_score":0,"policy_or_regulatory_score":3,"valuation_repricing_score":3,"execution_risk_score":2,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":72,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":3,"customer_quality_score":0,"policy_or_regulatory_score":3,"valuation_repricing_score":3,"execution_risk_score":2,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_after":76,"stage_label_after":"Stage2-Actionable_GreenBlocked","changed_components":["margin_bridge_score","revision_score","accounting_trust_risk_score"],"component_delta_explanation":"Securities capital-return bridge had contained MAE and later 180D validation, but Green requires payout/buyback and earnings refresh.","MFE_90D_pct":14.71,"MAE_90D_pct":-2.36,"score_return_alignment_label":"securities_capital_return_slow_positive","current_profile_verdict":"current_profile_correct_if_green_blocked"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"105560","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":3,"customer_quality_score":0,"policy_or_regulatory_score":4,"valuation_repricing_score":4,"execution_risk_score":3,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":77,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":2,"customer_quality_score":0,"policy_or_regulatory_score":3,"valuation_repricing_score":2,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_after":67,"stage_label_after":"Stage4B_capital_refresh","changed_components":["margin_bridge_score","revision_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Bank capital-return bridge exists, but CET1, payout, credit-cost and earnings refresh are needed.","MFE_90D_pct":18.20,"MAE_90D_pct":-15.81,"score_return_alignment_label":"bank_capital_return_local_4B","current_profile_verdict":"current_profile_correct_if_4B"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"316140","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":1,"customer_quality_score":0,"policy_or_regulatory_score":4,"valuation_repricing_score":2,"execution_risk_score":3,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":68,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":2,"valuation_repricing_score":0,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":47,"stage_label_after":"Stage2_cap","changed_components":["margin_bridge_score","revision_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Low-PBR bank policy label lacked differentiated payout, buyback, CET1 or ROE execution bridge.","MFE_90D_pct":5.69,"MAE_90D_pct":-15.08,"score_return_alignment_label":"low_PBR_bank_cap","current_profile_verdict":"current_profile_false_positive_if_actionable"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"006800","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":2,"customer_quality_score":0,"policy_or_regulatory_score":2,"valuation_repricing_score":3,"execution_risk_score":3,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":64,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":43,"stage_label_after":"Stage4C","changed_components":["margin_bridge_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Low-PBR brokerage label lacked capital-return execution and earnings revision; price path rejected it.","MFE_90D_pct":5.53,"MAE_90D_pct":-20.16,"score_return_alignment_label":"low_PBR_brokerage_hard_4C","current_profile_verdict":"current_profile_false_positive_if_stage2"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"005830","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":4,"customer_quality_score":0,"policy_or_regulatory_score":4,"valuation_repricing_score":4,"execution_risk_score":2,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_before":85,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":2,"customer_quality_score":0,"policy_or_regulatory_score":2,"valuation_repricing_score":2,"execution_risk_score":2,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_after":57,"stage_label_after":"Reclassify_C22_C31","changed_components":["margin_bridge_score","revision_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","accounting_trust_risk_score"],"component_delta_explanation":"Nonlife reserve/capital-return bridge is real but belongs to C22/C31, not generic C21 learning.","MFE_90D_pct":27.05,"MAE_90D_pct":-9.26,"score_return_alignment_label":"insurance_positive_elsewhere_reclassify","current_profile_verdict":"requires_reclassification"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"088350","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":1,"customer_quality_score":0,"policy_or_regulatory_score":3,"valuation_repricing_score":2,"execution_risk_score":3,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":66,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":1,"valuation_repricing_score":0,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":44,"stage_label_after":"Stage2_cap","changed_components":["margin_bridge_score","revision_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Life-insurance Value-up label lacked CSM/solvency/reserve quality/payout bridge.","MFE_90D_pct":9.31,"MAE_90D_pct":-15.69,"score_return_alignment_label":"life_insurance_policy_cap","current_profile_verdict":"current_profile_false_positive_if_actionable"}
```

---

## 9. Current calibrated profile stress test

The C21 capital-return execution gate held:

```text
securities ROE/PBR capital-return bridge
→ Stage2 can survive, Green blocked until payout/revision refresh

bank capital-return bridge with refresh missing
→ local 4B

sector-wide low-PBR bank label
→ cap

brokerage low-PBR label without execution
→ hard 4C

insurance reserve/CSM/solvency bridge
→ reclassify to C22/C31

life insurance Value-up label without CSM/solvency/payout
→ cap
```

### Rule candidate retained, not newly proposed

```text
C21_ROE_PBR_CAPITAL_RETURN_EXECUTION_GATE_V113_HELD_OUT

if C21
and ROE_PBR_Valueup_or_low_PBR_label == true
and executed_or_timestamped_payout_buyback_cancellation_CET1_ROE_or_earnings_revision_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C21
and capital_return_bridge == true
and MFE_180D_pct >= +20
and MAE_180D_pct > -10:
    keep_stage2_actionable_bonus = true
    block_stage3_green_until_payout_or_revision_refresh = true
```

```text
if C21
and bank_capital_return_bridge == true
and MAE_90D_pct <= -12:
    local_4B_watch = true
    require_CET1_payout_credit_cost_refresh = true
```

```text
if C21
and low_PBR_financial_label == true
and MFE_90D_pct < +10
and MAE_90D_pct <= -20:
    route = Stage4C
```

```text
if C21
and dominant_bridge_is_insurance_reserve_CSM_solvency == true:
    cap_C21_contribution = true
    require_reclassification_to_C22_or_C31 = true
```

---

## 10. Profile comparison shadow-only summary

```yaml
profile_comparison:
  P0_e2r_2_1_stock_web_calibrated_proxy:
    hypothesis: current profile with global Stage2 bridge and 4C guards
    eligible_trigger_count: 6
    avg_MFE_90D_pct: 13.42
    avg_MAE_90D_pct: -12.61
    false_positive_risk: high_if_low_PBR_or_insurance_rows_are_left_as_generic_C21
    verdict: adequate_only_with_C21_execution_and_reclassification_gate
  P0b_e2r_2_0_baseline_reference:
    hypothesis: older profile pays too much for low-PBR/Value-up labels
    eligible_trigger_count: 6
    false_positive_risk: higher
    verdict: inferior
  P1_sector_specific_candidate_profile:
    hypothesis: L6 financials require executed capital return, not cheapness
    changed_axes: none_new_holdout_only
    verdict: pass_holdout
  P2_canonical_archetype_candidate_profile:
    hypothesis: C21 requires payout/buyback/CET1/ROE bridge and reclassifies insurance-reserve rows
    changed_axes: none_new_holdout_only
    verdict: pass_holdout
  P3_counterexample_guard_profile:
    hypothesis: low-PBR brokerage with weak MFE/deep MAE routes to hard 4C
    changed_axes: none_new_holdout_only
    verdict: strongest_for_false_positive_control
```

---

## 11. Coverage matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---:|
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | VALUEUP_ROE_PBR_CAPITAL_RETURN_HOLDOUT_V113 | 2 | 4 | 1 | 1 | 0 | 6 | 6 | 0 | 4 | false | false | 24 |

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
  - C21|005830|Stage2-Watch|2024-02-26
  - C21|088350|Stage2-Watch|2024-02-26
new_symbol_count: 0
new_trigger_family_count: 0
narrative_only_future_todo_count: 1
tested_existing_calibrated_axes:
  - stage2_required_bridge
  - local_4b_watch_guard
  - hard_4c_thesis_break_routes_to_4c
  - C21_capital_return_execution_gate
  - insurance_reclassification_guard
residual_error_types_found:
  - low_PBR_label_without_execution
  - bank_capital_return_refresh_missing
  - insurance_reserve_bridge_wrong_archetype
  - brokerage_low_PBR_hard_failure
new_axis_proposed: null
existing_axis_strengthened:
  - C21_ROE_PBR_CAPITAL_RETURN_EXECUTION_GATE_V113_HELD_OUT
existing_axis_weakened: null
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
no_new_signal_reason: all rows reused holdout validation after additional C21 bank/securities candidates were not recomputed
loop_contribution_label: duplicate_low_value_loop_with_cache_miss_todo
do_not_propose_new_weight_delta: true
```

```jsonl
{"row_type":"residual_contribution","round":"R6","loop":"113","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","new_independent_case_count":0,"reused_case_count":6,"new_symbol_count":0,"new_trigger_family_count":0,"narrative_only_future_todo_count":1,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","hard_4c_thesis_break_routes_to_4c","C21_capital_return_execution_gate","insurance_reclassification_guard"],"residual_error_types_found":["low_PBR_label_without_execution","bank_capital_return_refresh_missing","insurance_reserve_bridge_wrong_archetype","brokerage_low_PBR_hard_failure"],"loop_contribution_label":"duplicate_low_value_loop_with_cache_miss_todo","do_not_propose_new_weight_delta":true}
```

---

## 14. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Treat this R6/C21 loop 113 as holdout validation only. Batch it with C21 loops up to 112, C22/C31/C32 financial-policy guardrails, and R13 accounting-trust / Stage2 false-positive / high-MAE / 4B-4C files. If exact same_entry_group_id rows already exist, dedupe them. Preserve the C21 ROE/PBR capital-return execution gate and insurance reclassification guard, but do not create a new weight delta from this loop because no new independent case was added. Future research should reprice 신한지주(055550), 하나금융지주(086790), 메리츠금융지주(138040), 삼성증권(016360), 키움증권(039490) when stock-web shards are accessible.
```

---

## 15. Next research state

```yaml
completed_round: R6
completed_loop: 113
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
