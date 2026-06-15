# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R12
selected_loop: 106
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: FORMAL_MINORITY_CASH_EXIT_GATE_HOLDOUT_V106_VS_VALUEUP_CAPITAL_RETURN_AND_ACTIVISM_LABEL
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
  stock_web_manifest: read_ok
  uncached_symbol_shards:
    - additional_governance_candidate_shards: cache_miss_observed
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
loop_objective:
  - holdout_validation
  - duplicate_low_value_loop_marker
  - formal_minority_cash_exit_gate
  - wrong_archetype_reclassification_guard
  - post_resolution_4B_guard
price_source: Songdaiki/stock-web
price_data_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

`C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP` remains Priority 0 in the no-repeat index: 3 representative rows and 27 rows short of the 30-row minimum. The v12 scheduler maps C32 to `R12 / L10_POLICY_EVENT_CROSS_REDTEAM_MISC`.

This file continues the local C32 sequence after `R12/C32 loop 105`; selected loop is therefore `106`.

This is a **holdout validation / duplicate-aware reclassification guard** MD. It does not claim fresh independent price evidence because additional governance/tender candidate shards were unavailable in this execution. The trigger rows below reuse current-session stock-web-derived C32/C21/C22/C31 rows that already contain complete 30D/90D/180D MFE and MAE from `Songdaiki/stock-web` tradable OHLC. Exact duplicate keys should be deduped during batch ingest. No production scoring is changed.

---

## 1. Research thesis

C32 is the formal minority cash-exit archetype.

```text
formal tender / appraisal / squeeze-out / binding minority exit price / control-battle cash offer
→ legally visible participation mechanics
→ price path validation
→ post-resolution local 4B
```

C32 is **not** the generic shareholder-return bucket.

```text
capital return
Value-up
low PBR
buyback language
dividend policy
NAV activism proposal
control sale headline
```

Those signals may be valuable, but they belong to C21, C22, C31, or an activism/watch bucket unless minority holders have an executable cash-exit path.

The C32 holdout rule is:

```text
real tender / minority cash-exit bridge
→ keep Stage2 while mechanics are active

post-resolution or offer fade
→ local 4B

control sale without minority cash-exit
→ hard 4C

capital return / Value-up bridge but no tender mechanics
→ cap C32 and reclassify

low-PBR label with weak price path
→ hard 4C or Stage2 cap
```

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 8
  actual_trigger_rows: 10
  source_archetypes:
    - C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
    - C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
    - C22_INSURANCE_RATE_CYCLE_RESERVE
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
    - C32 holdout validation
    - formal cash-exit vs capital-return split
    - post-resolution 4B guard
    - wrong-archetype reclassification guard
    - no production scoring changes
```

---

## 3. Source validation

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
  - R12/C32 loops 102~105
  - R6/C21 loop 112
  - R6/C22 loop 111
  - R11/C31 loops 103~106
  - R13 accounting-trust / Stage2 false-positive / high-MAE / 4B-4C guardrail rows
reason:
  - all reused rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - additional governance/tender candidate shards were not available in this execution
  - exact duplicate C32 keys should be deduped during batch ingest
  - this file is holdout validation / consolidation evidence only
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","selected_round":"R12","selected_loop":106,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"FORMAL_TENDER_CASH_EXIT_POSITIVE_POST_RESOLUTION_4B","symbol":"041510","name":"에스엠","trigger_type":"Stage2-Actionable","entry_date":"2023-02-10","entry_price":114700,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":40.54,"MAE_30D_pct":-6.45,"MFE_90D_pct":40.54,"MAE_90D_pct":-21.10,"MFE_180D_pct":40.54,"MAE_180D_pct":-21.10,"forward_high_30d":161200,"forward_low_30d":107300,"forward_high_90d":161200,"forward_low_90d":90500,"forward_high_180d":161200,"forward_low_180d":90500,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C32|041510|Stage2-Actionable|2023-02-10","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control","reuse_reason":"same C32 formal tender row from loops 104~105","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"formal_tender_positive_control","novelty_key":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|041510|Stage2-Actionable|2023-02-10","non_price_bridge":"formal tender/control contest cash path with visible minority exit mechanics","score_alignment":"keep Stage2 while tender mechanics are active; post-resolution local 4B watch required"}
{"row_type":"trigger","selected_round":"R12","selected_loop":106,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"CONTROL_BATTLE_AFFILIATE_TENDER_CASH_PATH_POSITIVE_CONTROL","symbol":"036560","name":"KZ정밀","trigger_type":"Stage2-Actionable","entry_date":"2024-09-13","entry_price":12180,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":201.31,"MAE_30D_pct":0.00,"MFE_90D_pct":201.31,"MAE_90D_pct":0.00,"MFE_180D_pct":201.31,"MAE_180D_pct":-11.25,"forward_high_30d":36700,"forward_low_30d":12180,"forward_high_90d":36700,"forward_low_90d":12180,"forward_high_180d":36700,"forward_low_180d":10810,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C32|036560|Stage2-Actionable|2024-09-13","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control","reuse_reason":"same C32 control-battle affiliate tender row from loops 104~105","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"formal_tender_positive_control","novelty_key":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|036560|Stage2-Actionable|2024-09-13","non_price_bridge":"control-battle affiliate tender cash-exit mechanics with legal price anchor","score_alignment":"Stage2 valid during tender mechanics; post-offer normalization watch required"}
{"row_type":"trigger","selected_round":"R12","selected_loop":106,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"CONTROL_SALE_WITHOUT_MINORITY_TENDER_HARD_4C","symbol":"040300","name":"YTN","trigger_type":"Stage4C","entry_date":"2023-10-24","entry_price":7800,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":23.08,"MAE_30D_pct":-30.64,"MFE_90D_pct":23.08,"MAE_90D_pct":-30.64,"MFE_180D_pct":23.08,"MAE_180D_pct":-49.29,"forward_high_30d":9600,"forward_low_30d":5410,"forward_high_90d":9600,"forward_low_90d":5410,"forward_high_180d":9600,"forward_low_180d":3955,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C32|040300|Stage4C|2023-10-24","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","reuse_reason":"same C32 control-sale hard counterexample row from loops 104~105","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"control_sale_no_minority_cash_exit","novelty_key":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|040300|Stage4C|2023-10-24","non_price_bridge":"control-sale headline without public minority tender/appraisal/squeeze-out cash path","score_alignment":"hard 4C; control sale is not minority cash exit"}
{"row_type":"trigger","selected_round":"R12","selected_loop":106,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"ACTIVISM_NAV_PROPOSAL_WITHOUT_EXECUTED_CASH_EXIT_WATCH","symbol":"028260","name":"삼성물산","trigger_type":"Stage2-Watch","entry_date":"2024-03-15","entry_price":154100,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":7.98,"MAE_30D_pct":-10.32,"MFE_90D_pct":7.98,"MAE_90D_pct":-14.02,"MFE_180D_pct":7.98,"MAE_180D_pct":-15.96,"forward_high_30d":166400,"forward_low_30d":138200,"forward_high_90d":166400,"forward_low_90d":132500,"forward_high_180d":166400,"forward_low_180d":129500,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C32|028260|Stage2-Watch|2024-03-15","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_watch_control","reuse_reason":"same C32 activism watch row from loops 104~105","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"activism_watch","novelty_key":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|028260|Stage2-Watch|2024-03-15","non_price_bridge":"NAV-discount activism proposal without passed vote, tender, appraisal, buyback/cancellation or cash-exit mechanics","score_alignment":"Watch only; require executed minority cash mechanics before C32 Actionable"}
{"row_type":"trigger","selected_round":"R12","selected_loop":106,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"SECURITIES_CAPITAL_RETURN_POSITIVE_ELSEWHERE_NOT_TENDER_RECLASSIFY","symbol":"005940","name":"NH투자증권","trigger_type":"Stage2-Watch","entry_date":"2024-02-26","entry_price":11420,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":14.71,"MAE_30D_pct":-2.36,"MFE_90D_pct":14.71,"MAE_90D_pct":-2.36,"MFE_180D_pct":26.09,"MAE_180D_pct":-2.36,"forward_high_30d":13100,"forward_low_30d":11150,"forward_high_90d":13100,"forward_low_90d":11150,"forward_high_180d":14400,"forward_low_180d":11150,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C32|005940|Stage2-Watch|2024-02-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_wrong_archetype_positive_elsewhere","reuse_reason":"same C32 reclassification positive-elsewhere row from loops 104~105","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"wrong_archetype_positive_elsewhere","novelty_key":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|005940|Stage2-Watch|2024-02-26","non_price_bridge":"securities ROE/capital-return bridge is positive in C21, but has no C32 tender/appraisal/control-premium cash-exit mechanics","score_alignment":"cap C32 contribution; reclassify to C21 rather than C32"}
{"row_type":"trigger","selected_round":"R12","selected_loop":106,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"BANK_VALUEUP_CAPITAL_RETURN_LOCAL_4B_NOT_C32_TENDER","symbol":"105560","name":"KB금융","trigger_type":"Stage4B","entry_date":"2024-07-26","entry_price":87900,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":5.12,"MAE_30D_pct":-15.81,"MFE_90D_pct":18.20,"MAE_90D_pct":-15.81,"MFE_180D_pct":18.20,"MAE_180D_pct":-15.81,"forward_high_30d":92400,"forward_low_30d":74000,"forward_high_90d":103900,"forward_low_90d":74000,"forward_high_180d":103900,"forward_low_180d":74000,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C32|105560|Stage4B|2024-07-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_wrong_archetype_local_4B","reuse_reason":"same C32 bank capital-return reclassification row from loops 104~105","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"wrong_archetype_local_4B","novelty_key":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|105560|Stage4B|2024-07-26","non_price_bridge":"bank Value-up/capital-return bridge may be real, but it is not a minority tender/control-premium cash-exit event","score_alignment":"cap C32 contribution; reclassify to C21/C31 and require capital/payout refresh there"}
{"row_type":"trigger","selected_round":"R12","selected_loop":106,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"NONLIFE_CAPITAL_RETURN_POSITIVE_BUT_NOT_C32_TENDER_RECLASSIFY","symbol":"005830","name":"DB손해보험","trigger_type":"Stage2-Watch","entry_date":"2024-02-26","entry_price":95000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":15.79,"MAE_30D_pct":-4.11,"MFE_90D_pct":27.05,"MAE_90D_pct":-9.26,"MFE_180D_pct":30.53,"MAE_180D_pct":-9.26,"forward_high_30d":110000,"forward_low_30d":91100,"forward_high_90d":120700,"forward_low_90d":86200,"forward_high_180d":124000,"forward_low_180d":86200,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C32|005830|Stage2-Watch|2024-02-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_wrong_archetype_positive_elsewhere","reuse_reason":"same C32 insurance capital-return reclassification row from loops 104~105","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"wrong_archetype_positive_elsewhere","novelty_key":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|005830|Stage2-Watch|2024-02-26","non_price_bridge":"nonlife reserve/capital-return bridge is positive in C22/C31, but lacks formal tender, appraisal or control-premium minority exit mechanics","score_alignment":"cap C32 contribution; reclassify to C22/C31"}
{"row_type":"trigger","selected_round":"R12","selected_loop":106,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"LOW_PBR_BROKERAGE_LABEL_WITHOUT_TENDER_OR_EXECUTION_HARD_4C","symbol":"006800","name":"미래에셋증권","trigger_type":"Stage4C","entry_date":"2024-02-26","entry_price":8680,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":5.53,"MAE_30D_pct":-10.71,"MFE_90D_pct":5.53,"MAE_90D_pct":-20.16,"MFE_180D_pct":5.53,"MAE_180D_pct":-23.96,"forward_high_30d":9160,"forward_low_30d":7750,"forward_high_90d":9160,"forward_low_90d":6930,"forward_high_180d":9160,"forward_low_180d":6600,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C32|006800|Stage4C|2024-02-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","reuse_reason":"same C32 low-PBR brokerage hard counterexample from loops 104~105","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"low_PBR_hard_4C","novelty_key":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|006800|Stage4C|2024-02-26","non_price_bridge":"low-PBR brokerage label lacked both capital-return execution and C32 tender/control-premium cash-exit mechanics","score_alignment":"hard 4C; cheapness or value-up label is not tender premium"}
{"row_type":"trigger","selected_round":"R12","selected_loop":106,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"LIFE_INSURANCE_VALUEUP_LABEL_WITHOUT_C32_TENDER_CAP","symbol":"088350","name":"한화생명","trigger_type":"Stage2-Watch","entry_date":"2024-02-26","entry_price":3060,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":9.31,"MAE_30D_pct":-8.17,"MFE_90D_pct":9.31,"MAE_90D_pct":-15.69,"MFE_180D_pct":9.31,"MAE_180D_pct":-15.69,"forward_high_30d":3345,"forward_low_30d":2810,"forward_high_90d":3345,"forward_low_90d":2580,"forward_high_180d":3345,"forward_low_180d":2580,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C32|088350|Stage2-Watch|2024-02-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_label_cap","reuse_reason":"same C32 life-insurance value-up cap row from loops 104~105","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"wrong_archetype_cap","novelty_key":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|088350|Stage2-Watch|2024-02-26","non_price_bridge":"life-insurance Value-up label without CSM/solvency bridge and without C32 minority cash-exit mechanics","score_alignment":"cap C32; reclassify only if C22/C31 bridge appears"}
{"row_type":"trigger","selected_round":"R12","selected_loop":106,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"GA_DISTRIBUTION_COMMISSION_WRONG_ARCHETYPE_NOT_C32_TENDER","symbol":"244920","name":"에이플러스에셋","trigger_type":"Stage2-Watch","entry_date":"2024-05-10","entry_price":4100,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":9.76,"MAE_30D_pct":-2.32,"MFE_90D_pct":9.76,"MAE_90D_pct":-13.78,"MFE_180D_pct":14.63,"MAE_180D_pct":-13.78,"forward_high_30d":4500,"forward_low_30d":4005,"forward_high_90d":4500,"forward_low_90d":3535,"forward_high_180d":4700,"forward_low_180d":3535,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C32|244920|Stage2-Watch|2024-05-10","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_reclassification_control","reuse_reason":"same C32 GA distribution reclassification row from loops 104~105","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"wrong_archetype_reclassification","novelty_key":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|244920|Stage2-Watch|2024-05-10","non_price_bridge":"GA distribution commission bridge may exist, but it is neither insurance reserve-cycle nor C32 tender cash-exit mechanics","score_alignment":"cap C32 contribution and reclassify to distribution commission axis"}
```

---

## 5. Case analysis

### 5.1 SM Entertainment / 041510 — tender positive control

Formal tender mechanics are the C32 bridge.

```yaml
entry_close: 114700
90D_MFE_MAE: +40.54 / -21.10
180D_MFE_MAE: +40.54 / -21.10
route: Keep Stage2 during tender, then post-resolution 4B
```

### 5.2 KZ Precision / 036560 — tender affiliate positive control

The control-battle tender anchor validates minority cash-exit mechanics.

```yaml
entry_close: 12180
90D_MFE_MAE: +201.31 / 0.00
180D_MFE_MAE: +201.31 / -11.25
route: Keep Stage2 during offer, then watch
```

### 5.3 YTN / 040300 — control sale hard 4C

Control sale is not public minority tender.

```yaml
entry_close: 7800
90D_MFE_MAE: +23.08 / -30.64
180D_MFE_MAE: +23.08 / -49.29
route: Stage4C
```

### 5.4 Samsung C&T / 028260 — activism watch

NAV activism proposal needs execution.

```yaml
entry_close: 154100
90D_MFE_MAE: +7.98 / -14.02
180D_MFE_MAE: +7.98 / -15.96
route: Stage2-Watch
```

### 5.5 NH Investment & Securities / 005940 — reclassify positive elsewhere

Capital return belongs to C21, not C32.

```yaml
entry_close: 11420
90D_MFE_MAE: +14.71 / -2.36
180D_MFE_MAE: +26.09 / -2.36
route: reclassify
```

### 5.6 KB Financial / 105560 — reclassify local 4B

Bank Value-up can be real, but not tender mechanics.

```yaml
entry_close: 87900
90D_MFE_MAE: +18.20 / -15.81
180D_MFE_MAE: +18.20 / -15.81
route: reclassify to C21/C31
```

### 5.7 DB Insurance / 005830 — reclassify positive elsewhere

Reserve/capital return belongs to C22/C31.

```yaml
entry_close: 95000
90D_MFE_MAE: +27.05 / -9.26
180D_MFE_MAE: +30.53 / -9.26
route: reclassify
```

### 5.8 Mirae Asset Securities / 006800 — low-PBR hard 4C

Cheapness is not tender premium.

```yaml
entry_close: 8680
90D_MFE_MAE: +5.53 / -20.16
180D_MFE_MAE: +5.53 / -23.96
route: Stage4C
```

### 5.9 Hanwha Life / 088350 — Value-up label cap

No formal minority cash-exit mechanics.

```yaml
entry_close: 3060
90D_MFE_MAE: +9.31 / -15.69
180D_MFE_MAE: +9.31 / -15.69
route: Stage2-Watch
```

### 5.10 A Plus Asset / 244920 — commission bridge wrong room

Commission economics is not a tender cash-exit event.

```yaml
entry_close: 4100
90D_MFE_MAE: +9.76 / -13.78
180D_MFE_MAE: +14.63 / -13.78
route: reclassify
```

---

## 6. Score-return alignment

```yaml
new_independent_case_count: 0
reused_case_count: 10
new_symbol_count: 0
same_archetype_new_symbol_count: 0
same_archetype_new_trigger_family_count: 0
new_trigger_family_count: 0
calibration_usable_case_count: 10
calibration_usable_trigger_count: 10
positive_case_count: 2
counterexample_count: 8
local_4B_watch_count: 3
wrong_archetype_reclassification_count: 6
hard_4C_count: 2
current_profile_error_count: 7
diversity_score_summary: "formal tender positives, control-sale hard 4C, activism watch, capital-return reclassification, low-PBR hard 4C covered; all rows reused"
loop_contribution_label: duplicate_low_value_loop
do_not_propose_new_weight_delta: true
```

| symbol | role | 90D MFE/MAE | 180D MFE/MAE | C32 lesson |
|---|---:|---:|---:|---|
| 041510 | tender positive | +40.54 / -21.10 | +40.54 / -21.10 | formal cash-exit validates |
| 036560 | tender positive | +201.31 / 0.00 | +201.31 / -11.25 | tender anchor validates |
| 040300 | control-sale hard 4C | +23.08 / -30.64 | +23.08 / -49.29 | no minority exit |
| 028260 | activism watch | +7.98 / -14.02 | +7.98 / -15.96 | proposal needs execution |
| 005940 | reclassify | +14.71 / -2.36 | +26.09 / -2.36 | C21, not C32 |
| 105560 | reclassify 4B | +18.20 / -15.81 | +18.20 / -15.81 | C21/C31, not tender |
| 005830 | reclassify | +27.05 / -9.26 | +30.53 / -9.26 | C22/C31, not tender |
| 006800 | hard 4C | +5.53 / -20.16 | +5.53 / -23.96 | cheapness is not premium |
| 088350 | cap | +9.31 / -15.69 | +9.31 / -15.69 | Value-up label lacks tender |
| 244920 | reclassify | +9.76 / -13.78 | +14.63 / -13.78 | commission bridge belongs elsewhere |

---

## 7. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"041510","raw_tender_cash_exit":5,"raw_legal_visibility":5,"raw_execution_status":4,"raw_minority_participation":5,"raw_wrong_archetype_risk":0,"raw_price_validation":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"TenderPositive_PostResolution4B"}
{"row_type":"score_simulation","symbol":"036560","raw_tender_cash_exit":5,"raw_legal_visibility":5,"raw_execution_status":4,"raw_minority_participation":5,"raw_wrong_archetype_risk":0,"raw_price_validation":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"TenderPositive_PostOfferWatch"}
{"row_type":"score_simulation","symbol":"040300","raw_tender_cash_exit":0,"raw_legal_visibility":1,"raw_execution_status":1,"raw_minority_participation":0,"raw_wrong_archetype_risk":1,"raw_price_validation":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C_ControlSaleNoTender"}
{"row_type":"score_simulation","symbol":"028260","raw_tender_cash_exit":0,"raw_legal_visibility":2,"raw_execution_status":0,"raw_minority_participation":1,"raw_wrong_archetype_risk":2,"raw_price_validation":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"ActivismWatch"}
{"row_type":"score_simulation","symbol":"005940","raw_tender_cash_exit":0,"raw_legal_visibility":1,"raw_execution_status":3,"raw_minority_participation":1,"raw_wrong_archetype_risk":5,"raw_price_validation":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"ReclassifyC21"}
{"row_type":"score_simulation","symbol":"105560","raw_tender_cash_exit":0,"raw_legal_visibility":1,"raw_execution_status":3,"raw_minority_participation":1,"raw_wrong_archetype_risk":5,"raw_price_validation":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"ReclassifyC21C31"}
{"row_type":"score_simulation","symbol":"005830","raw_tender_cash_exit":0,"raw_legal_visibility":1,"raw_execution_status":3,"raw_minority_participation":1,"raw_wrong_archetype_risk":5,"raw_price_validation":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"ReclassifyC22C31"}
{"row_type":"score_simulation","symbol":"006800","raw_tender_cash_exit":0,"raw_legal_visibility":0,"raw_execution_status":0,"raw_minority_participation":0,"raw_wrong_archetype_risk":5,"raw_price_validation":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C_LowPBRNoTender"}
{"row_type":"score_simulation","symbol":"088350","raw_tender_cash_exit":0,"raw_legal_visibility":1,"raw_execution_status":1,"raw_minority_participation":1,"raw_wrong_archetype_risk":5,"raw_price_validation":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2Cap_LifeValueup"}
{"row_type":"score_simulation","symbol":"244920","raw_tender_cash_exit":0,"raw_legal_visibility":0,"raw_execution_status":1,"raw_minority_participation":0,"raw_wrong_archetype_risk":5,"raw_price_validation":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"ReclassifyCommissionBridge"}
```

---

## 8. Current calibrated profile stress test

The C32 gate held:

```text
formal tender / minority cash-exit mechanics -> keep Stage2 while active
post-resolution drawdown -> local 4B
control sale without minority cash-exit -> hard 4C
capital return / Value-up / payout -> reclassify to C21/C22/C31
low-PBR label without execution -> cap or hard block
```

### Rule candidate retained, not newly proposed

```text
C32_FORMAL_MINORITY_CASH_EXIT_REQUIREMENT_V106_HELD_OUT

if C32
and governance_control_premium_or_shareholder_friendly_label == true
and formal_tender_appraisal_squeezeout_binding_cash_exit_or_defined_minority_exit_price == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C32
and formal_tender_or_cash_exit_path == true
and legally_visible_price_or_mechanics == true:
    keep_stage2_actionable_bonus = true
    if offer_resolution_expiry_or_cash_path_fade == true:
        local_4B_watch = true
```

```text
if C32
and capital_return_or_valueup_bridge == true
and tender_or_control_cash_exit_mechanics == false:
    cap_C32_contribution = true
    require_reclassification_to_C21_C22_or_C31 = true
```

```text
if C32
and control_sale_headline == true
and minority_cash_exit_path == false
and MAE_90D_pct <= -20:
    route = Stage4C
```

```text
if C32
and low_PBR_or_shareholder_return_label == true
and MFE_90D_pct < +10
and tender_cash_exit_path == false:
    route = Stage2Cap_or_Stage4C
```

---

## 9. Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 10
calibration_usable_trigger_count: 10
representative_trigger_count: 0
new_weight_evidence_candidate_count: 0
guardrail_candidate_count: 10
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
batch_ingest_recommendation: dedupe_as_holdout_validation_only
```

---

## 10. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: true
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
holdout_validation_passed: true
loop_contribution_label: duplicate_low_value_loop
new_axis_proposed: null
existing_axis_strengthened:
  - C32_FORMAL_MINORITY_CASH_EXIT_REQUIREMENT_V106_HELD_OUT
existing_axis_weakened: null
one_line_summary: "This loop adds 0 new independent cases and validates the C32 formal minority cash-exit gate against tender positives, control-sale hard 4C, activism watch, capital-return reclassification, and low-PBR hard-block controls."
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Treat this R12/C32 loop 106 as holdout validation only. Batch it with C32 loops 102~105, C21/C22/C31 loops, and R13 accounting-trust / Stage2 false-positive / high-MAE / 4B-4C files. If exact same_entry_group_id rows already exist, dedupe them. Preserve the C32 formal minority cash-exit gate, but do not create a new weight delta from this loop because additional governance/tender symbol shards were not available and no new independent case was added.
```

---

## 12. Next research state

```yaml
completed_round: R12
completed_loop: 106
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
  - C15_MATERIAL_SPREAD_SUPERCYCLE
  - R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
  - C18_CONSUMER_EXPORT_CHANNEL_REORDER
  - C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
```
