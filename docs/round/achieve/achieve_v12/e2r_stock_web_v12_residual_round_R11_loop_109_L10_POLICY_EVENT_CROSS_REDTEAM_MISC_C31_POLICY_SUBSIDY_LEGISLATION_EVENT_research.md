# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R11
selected_loop: 109
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: POLICY_HEADLINE_TO_LEGISLATION_BUDGET_COMPANY_CASHFLOW_HOLDOUT_V109_VALUEUP_AMPC_RESERVE_EXPLORATION_CONSTRUCTION_SPLIT
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
  stock_web_manifest: read_ok
  direct_stock_web_shards:
    - 373220/2024: reused_from_prior_local_C13_C31_boundary_row
    - 361610/2024: reused_from_prior_local_C13_C31_boundary_row
    - 036460/2024: reused_from_prior_local_C16_C31_boundary_row
    - 105560/2024: reused_from_prior_local_C21_C31_boundary_row
    - 316140/2024: reused_from_prior_local_C21_C31_boundary_row
    - 005830/2024: reused_from_prior_local_C22_C31_boundary_row
    - 088350/2024: reused_from_prior_local_C21_C22_C31_boundary_row
    - 004960/2024: reused_from_prior_local_C30_C31_boundary_row
    - additional_policy_subsidy_candidates: not_recomputed_this_turn
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
loop_objective:
  - holdout_validation
  - duplicate_low_value_loop_marker
  - policy_headline_to_legislation_budget_company_cashflow_gate
  - AMPC_IRA_policy_cash_conversion_positive_control
  - valueup_policy_execution_vs_label_split
  - exploration_policy_headline_4B_guard
  - construction_support_policy_watch_guard
price_source: Songdaiki/stock-web
price_data_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

`C31_POLICY_SUBSIDY_LEGISLATION_EVENT` remains a Priority 0 archetype. The current no-repeat index marks C31 at only 3 representative rows, so it remains one of the lowest-coverage policy/event archetypes. The v12 scheduler maps C31 to `R11 / L10_POLICY_EVENT_CROSS_REDTEAM_MISC`.

This file continues the local C31 policy sequence after previously referenced `R11/C31 loops 103~108`; selected loop is therefore `109`.

This is a **dedupe-aware holdout validation / cache-miss TODO** MD. It does not claim fresh independent stock-web evidence. The trigger rows below reuse current-session stock-web-derived policy boundary rows that already contain complete 30D/90D/180D MFE and MAE from `Songdaiki/stock-web` tradable OHLC. Additional C31 policy/subsidy/legislation candidates were not recomputed in this execution and are kept as future TODO rows. Exact duplicate `same_entry_group_id` rows should be deduped during batch ingest. No production scoring is changed.

---

## 1. Research thesis

C31 should not reward `policy`, `subsidy`, `value-up`, `IRA`, `AMPC`, `support package`, or `government plan` as labels.

C31 should reward policy only when the policy enters the company’s financial plumbing:

```text
policy / subsidy / legislation / budget / government plan / value-up label
→ enacted rule or binding budget
→ eligibility and company-specific allocation
→ production, payout, tax credit, guarantee, tariff or reimbursement mechanism
→ accounting recognition and timing
→ margin, cashflow, capital return or balance-sheet repair
→ price path validation
```

The recurring false positive is:

```text
policy headline
press-conference exploration theme
value-up label without executed payout
construction support label without refinancing
localization label without utilization
insurance policy label without solvency / reserve / payout bridge
```

Policy is a bridge, not a destination. It starts as a headline, becomes real only when it has a legal beam, budget concrete, eligibility bolts, and a cash lane into the company. Without those pieces, the bridge ends over water and the stock is only trading the signboard.

The C31 route split:

```text
policy + company-specific eligibility + production/cash recognition
→ Stage2 can survive

policy + strong MFE but no commercial/cash proof
→ local 4B, no Green

value-up policy + executed payout/buyback/capital adequacy bridge
→ Stage2 may survive

value-up label without differentiated execution
→ Stage2-Watch / cap

insurance policy/capital-return row
→ reclassify to C22 if reserve/CSM/solvency dominates

construction support policy
→ Watch only until refinancing, PF and cash collection prove through

exploration policy headline
→ local 4B until reserve/commerciality/cash bridge

localization/separator policy without utilization
→ hard 4C
```

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 8
  actual_trigger_rows: 8
  narrative_only_future_todo_rows: 1
  source_archetypes:
    - C31_POLICY_SUBSIDY_LEGISLATION_EVENT
    - C13_BATTERY_JV_UTILIZATION_AMPC_IRA
    - C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
    - C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
    - C22_INSURANCE_RATE_CYCLE_RESERVE
    - C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
    - R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
    - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
    - R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
    - R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
  price_windows:
    - 30D MFE/MAE
    - 90D MFE/MAE
    - 180D MFE/MAE
  output_use:
    - C31 holdout validation
    - policy-headline-to-cashflow gate
    - value-up execution guard
    - AMPC/IRA cash-conversion positive-control
    - exploration and construction support 4B/watch guard
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
  - R3/C13 loop 136
  - R4/C16 loop 115
  - R6/C21 loops 112~113
  - R6/C22 loops 111~112
  - R10/C30 loop 107
  - R11/C31 loops 103~108
  - R13 accounting-trust loops 12~14
  - R13 Stage2 false-positive loop 11
  - R13 high-MAE loop 9
  - R13 4B/4C loop 104
reason:
  - all reused rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - direct fresh C31 policy/subsidy/legislation candidate shards were unavailable or not recomputed in this execution
  - exact duplicate C31 keys should be deduped during batch ingest
  - this file is holdout validation / duplicate-low-value evidence only
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","selected_round":"R11","selected_loop":109,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"AMPC_IRA_POLICY_TO_PRODUCTION_CASH_CONVERSION_POSITIVE_CONTROL","symbol":"373220","name":"LG에너지솔루션","trigger_type":"Stage2-Actionable","entry_date":"2024-07-25","entry_price":332500,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":18.50,"MAE_30D_pct":-6.47,"MFE_90D_pct":33.53,"MAE_90D_pct":-6.47,"MFE_180D_pct":33.53,"MAE_180D_pct":-6.47,"forward_high_30d":394000,"forward_low_30d":311000,"forward_high_90d":444000,"forward_low_90d":311000,"forward_high_180d":444000,"forward_low_180d":311000,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C31|373220|Stage2-Actionable|2024-07-25","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control","reuse_reason":"same LGES AMPC/IRA utilization row from C13/C31 guardrails","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"AMPC_IRA_policy_cash_positive","novelty_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|373220|Stage2-Actionable|2024-07-25","non_price_bridge":"IRA/AMPC policy support plus utilization, customer diversification and ESS/non-EV demand bridge points toward production-linked cash recognition","score_alignment":"Stage2 can survive; Green blocked until AMPC cash conversion, qualification, utilization and accounting timing refresh"}
{"row_type":"trigger","selected_round":"R11","selected_loop":109,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"SEPARATOR_LOCALIZATION_POLICY_WITHOUT_UTILIZATION_OR_CASH_HARD_4C","symbol":"361610","name":"SK아이이테크놀로지","trigger_type":"Stage4C","entry_date":"2024-05-16","entry_price":57600,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.04,"MAE_30D_pct":-25.87,"MFE_90D_pct":1.04,"MAE_90D_pct":-46.27,"MFE_180D_pct":1.04,"MAE_180D_pct":-60.68,"forward_high_30d":58200,"forward_low_30d":42700,"forward_high_90d":58200,"forward_low_90d":30950,"forward_high_180d":58200,"forward_low_180d":22650,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C31|361610|Stage4C|2024-05-16","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","reuse_reason":"same separator localization policy false-positive row from C13/C31 guardrails","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"localization_policy_without_cash_hard_4C","novelty_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|361610|Stage4C|2024-05-16","non_price_bridge":"separator/localization policy exposure without customer pull, utilization, parent financing, qualification or cash-conversion bridge","score_alignment":"hard 4C; policy/localization vocabulary cannot substitute for utilization and cashflow"}
{"row_type":"trigger","selected_round":"R11","selected_loop":109,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"EXPLORATION_POLICY_HEADLINE_WITHOUT_RESERVE_COMMERCIALITY_CASH_LOCAL_4B","symbol":"036460","name":"한국가스공사","trigger_type":"Stage4B","entry_date":"2024-06-03","entry_price":38700,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":66.67,"MAE_30D_pct":-3.49,"MFE_90D_pct":66.67,"MAE_90D_pct":-5.68,"MFE_180D_pct":66.67,"MAE_180D_pct":-23.51,"forward_high_30d":64500,"forward_low_30d":37350,"forward_high_90d":64500,"forward_low_90d":36500,"forward_high_180d":64500,"forward_low_180d":29600,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C31|036460|Stage4B|2024-06-03","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_policy_headline_4B","reuse_reason":"same KOGAS exploration-policy row from C16/C31 guardrails","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"exploration_policy_local_4B","novelty_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|036460|Stage4B|2024-06-03","non_price_bridge":"East Sea oil/gas exploration policy headline without confirmed reserve, commerciality, recoverability, regulated return or company cashflow bridge","score_alignment":"local 4B; large MFE cannot become Green until reserve/commerciality/cash bridge is confirmed"}
{"row_type":"trigger","selected_round":"R11","selected_loop":109,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"BANK_VALUEUP_POLICY_CAPITAL_RETURN_REAL_BRIDGE_LOCAL_4B","symbol":"105560","name":"KB금융","trigger_type":"Stage4B","entry_date":"2024-07-26","entry_price":87900,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.12,"MAE_30D_pct":-15.81,"MFE_90D_pct":18.20,"MAE_90D_pct":-15.81,"MFE_180D_pct":18.20,"MAE_180D_pct":-15.81,"forward_high_30d":92400,"forward_low_30d":74000,"forward_high_90d":103900,"forward_low_90d":74000,"forward_high_180d":103900,"forward_low_180d":74000,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C31|105560|Stage4B|2024-07-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_valueup_local_4B","reuse_reason":"same KB value-up/capital-return local-4B row from C21/C31 guardrails","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"bank_valueup_policy_local_4B","novelty_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|105560|Stage4B|2024-07-26","non_price_bridge":"bank Value-up and capital-return policy bridge, but CET1, payout, buyback/cancellation, credit-cost and earnings refresh are required","score_alignment":"local 4B until capital-return execution and credit-cost bridge refresh"}
{"row_type":"trigger","selected_round":"R11","selected_loop":109,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"LOW_PBR_BANK_VALUEUP_LABEL_WITHOUT_DIFFERENTIATED_EXECUTION_CAP","symbol":"316140","name":"우리금융지주","trigger_type":"Stage2-Watch","entry_date":"2024-07-26","entry_price":16180,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.08,"MAE_30D_pct":-15.08,"MFE_90D_pct":5.69,"MAE_90D_pct":-15.08,"MFE_180D_pct":5.69,"MAE_180D_pct":-15.08,"forward_high_30d":16840,"forward_low_30d":13740,"forward_high_90d":17100,"forward_low_90d":13740,"forward_high_180d":17100,"forward_low_180d":13740,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C31|316140|Stage2-Watch|2024-07-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_valueup_cap","reuse_reason":"same low-PBR bank value-up cap row from C21/C31 guardrails","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"valueup_label_cap","novelty_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|316140|Stage2-Watch|2024-07-26","non_price_bridge":"low-PBR bank value-up label without differentiated payout, buyback, CET1 or ROE execution bridge","score_alignment":"Stage2-Watch/cap; require incremental capital-return execution before Actionable"}
{"row_type":"trigger","selected_round":"R11","selected_loop":109,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"NONLIFE_VALUEUP_RESERVE_CAPITAL_RETURN_POLICY_POSITIVE_RECLASSIFY_C22","symbol":"005830","name":"DB손해보험","trigger_type":"Stage2-Actionable","entry_date":"2024-02-26","entry_price":95000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.79,"MAE_30D_pct":-4.11,"MFE_90D_pct":27.05,"MAE_90D_pct":-9.26,"MFE_180D_pct":30.53,"MAE_180D_pct":-9.26,"forward_high_30d":110000,"forward_low_30d":91100,"forward_high_90d":120700,"forward_low_90d":86200,"forward_high_180d":124000,"forward_low_180d":86200,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C31|005830|Stage2-Actionable|2024-02-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_elsewhere","reuse_reason":"same DB Insurance positive row from C22/C31 guardrails","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"insurance_policy_positive_reclassify_C22","novelty_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|005830|Stage2-Actionable|2024-02-26","non_price_bridge":"nonlife reserve quality, loss-ratio discipline and capital-return policy bridge; more specific to C22 but useful C31 boundary positive","score_alignment":"Stage2 can survive as policy/capital-return bridge, but cap C31 if reserve/CSM mechanics dominate C22"}
{"row_type":"trigger","selected_round":"R11","selected_loop":109,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"LIFE_INSURANCE_VALUEUP_LABEL_WITHOUT_CSM_SOLVENCY_PAYOUT_CAP","symbol":"088350","name":"한화생명","trigger_type":"Stage2-Watch","entry_date":"2024-02-26","entry_price":3060,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.31,"MAE_30D_pct":-8.17,"MFE_90D_pct":9.31,"MAE_90D_pct":-15.69,"MFE_180D_pct":9.31,"MAE_180D_pct":-15.69,"forward_high_30d":3345,"forward_low_30d":2810,"forward_high_90d":3345,"forward_low_90d":2580,"forward_high_180d":3345,"forward_low_180d":2580,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C31|088350|Stage2-Watch|2024-02-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_life_insurance_cap","reuse_reason":"same life-insurance value-up cap row from C21/C22/C31 controls","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"life_insurance_valueup_cap","novelty_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|088350|Stage2-Watch|2024-02-26","non_price_bridge":"life-insurance value-up label without refreshed CSM, solvency, reserve quality or payout bridge","score_alignment":"cap C31 contribution; require CSM/solvency/payout evidence or reclassify to C22"}
{"row_type":"trigger","selected_round":"R11","selected_loop":109,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"CONSTRUCTION_SUPPORT_POLICY_WITHOUT_REFINANCING_PF_CASH_WATCH","symbol":"004960","name":"한신공영","trigger_type":"Stage2-Watch","entry_date":"2024-03-27","entry_price":6720,"entry_close":6720,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.48,"MAE_30D_pct":-8.33,"MFE_90D_pct":8.48,"MAE_90D_pct":-8.33,"MFE_180D_pct":18.60,"MAE_180D_pct":-8.63,"forward_high_30d":7290,"forward_low_30d":6160,"forward_high_90d":7290,"forward_low_90d":6160,"forward_high_180d":7970,"forward_low_180d":6140,"corporate_action_window_status":"not_flagged_in_prior_local_validation","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C31|004960|Stage2-Watch|2024-03-27","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_construction_support_watch","reuse_reason":"same Hanshin E&C modest rebound row from C30/C31 boundary files","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"construction_support_policy_watch","novelty_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|004960|Stage2-Watch|2024-03-27","non_price_bridge":"small/mid-builder construction support beta without clear refinancing, PF exposure relief or project cash collection bridge","score_alignment":"Stage2-Watch only; require policy guarantee, refinancing, unsold inventory and project cash evidence before Actionable"}
```

---

## 5. Narrative-only future TODO

```jsonl
{"row_type":"narrative_only_future_todo","selected_round":"R11","selected_loop":109,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_NEW_POLICY_SUBSIDY_LEGISLATION_REPRICE_TODO_AFTER_CACHE_MISS","candidate_symbols":["034020","010120","267260","298040","005380","000270","009410","034300","009830","096770","000660","042660"],"candidate_names":["두산에너빌리티","LS ELECTRIC","HD현대일렉트릭","효성중공업","현대차","기아","태영건설","신세계건설","한화솔루션","SK이노베이션","SK하이닉스","한화오션"],"why_not_trigger_row_now":"fresh stock-web symbol-year shards for new C31 policy/subsidy/budget/legal events were not recomputed in this execution; no fresh 30D/90D/180D MFE/MAE computed here","calibration_usable":false,"score_alignment":"future run should compute stock-web windows before counting these as new C31 evidence; distinguish policy headline from enacted budget, eligibility, company allocation, cash recognition and adjacent archetype drivers"}
```

---

## 6. Case analysis

### 6.1 LG Energy Solution / 373220 — AMPC/IRA positive-control

```yaml
entry_price: 332500
90D_MFE_MAE: +33.53 / -6.47
180D_MFE_MAE: +33.53 / -6.47
route: Stage2-Actionable
```

This is the best C31 positive-control in this holdout. The policy bridge is not just a headline; it can reach company economics through qualified production, AMPC recognition, utilization and customer demand. Green still requires direct cash-recognition timing and accounting proof.

### 6.2 SK IE Technology / 361610 — localization policy hard 4C

```yaml
entry_price: 57600
90D_MFE_MAE: +1.04 / -46.27
180D_MFE_MAE: +1.04 / -60.68
route: Stage4C
```

This row is the policy-label failure. Localization vocabulary without utilization, financing, qualification and customer pull did not become cashflow.

### 6.3 KOGAS / 036460 — exploration policy local 4B

```yaml
entry_price: 38700
90D_MFE_MAE: +66.67 / -5.68
180D_MFE_MAE: +66.67 / -23.51
route: Stage4B
```

The policy headline created a powerful 90D path, but C31 should not turn it into Green until reserve, commerciality, regulated return and company cashflow are established.

### 6.4 Value-up finance rows

```yaml
valueup_rows:
  - 105560: real capital-return bridge, local 4B until CET1/payout/credit-cost refresh.
  - 316140: low-PBR value-up label, Stage2-Watch cap.
```

Value-up is not a uniform policy factor. It only becomes C31-positive when the company executes payout, buyback, cancellation, capital adequacy and earnings discipline.

### 6.5 Insurance policy/capital-return boundary rows

```yaml
insurance_rows:
  - 005830: positive, but dominant mechanics may belong to C22.
  - 088350: value-up label without CSM/solvency/payout proof remains cap.
```

C31 can recognize policy/capital-return pressure, but if the real bridge is reserve quality or solvency, the row should be reclassified to C22.

### 6.6 Construction support watch

```yaml
entry_price: 6720
90D_MFE_MAE: +8.48 / -8.33
180D_MFE_MAE: +18.60 / -8.63
route: Stage2-Watch
```

Support policy is not balance-sheet repair. It becomes meaningful only after refinancing, guarantee, project cash collection and inventory relief appear.

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
positive_case_count: 3
counterexample_count: 5
local_4B_watch_count: 2
hard_4C_count: 1
wrong_archetype_reclassification_count: 2
current_profile_error_count: 6
diversity_score_summary: "AMPC/IRA positive, localization hard 4C, exploration policy 4B, financial value-up 4B/cap, insurance reclassification, construction support watch covered; all rows reused"
loop_contribution_label: duplicate_low_value_loop_with_cache_miss_todo
do_not_propose_new_weight_delta: true
```

| symbol | role | 90D MFE/MAE | 180D MFE/MAE | C31 lesson |
|---|---:|---:|---:|---|
| 373220 | AMPC positive | +33.53 / -6.47 | +33.53 / -6.47 | policy reaches production cash |
| 361610 | localization 4C | +1.04 / -46.27 | +1.04 / -60.68 | policy label failed |
| 036460 | exploration 4B | +66.67 / -5.68 | +66.67 / -23.51 | headline not commerciality |
| 105560 | value-up 4B | +18.20 / -15.81 | +18.20 / -15.81 | execution refresh needed |
| 316140 | value-up cap | +5.69 / -15.08 | +5.69 / -15.08 | low-PBR label not enough |
| 005830 | insurance positive elsewhere | +27.05 / -9.26 | +30.53 / -9.26 | reclassify to C22 if reserve dominates |
| 088350 | life value-up cap | +9.31 / -15.69 | +9.31 / -15.69 | CSM/solvency/payout required |
| 004960 | construction support watch | +8.48 / -8.33 | +18.60 / -8.63 | support needs refinancing/cash proof |

---

## 8. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"373220","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":3,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":4,"customer_quality_score":4,"policy_or_regulatory_score":5,"valuation_repricing_score":4,"execution_risk_score":2,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_before":84,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":3,"backlog_visibility_score":3,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":4,"customer_quality_score":4,"policy_or_regulatory_score":5,"valuation_repricing_score":4,"execution_risk_score":2,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_after":86,"stage_label_after":"Stage2_Actionable_GreenBlocked","changed_components":["revision_score","accounting_trust_risk_score"],"component_delta_explanation":"AMPC/IRA support reaches production-utilization economics, but cash recognition and qualification timing require refresh before Green.","MFE_90D_pct":33.53,"MAE_90D_pct":-6.47,"score_return_alignment_label":"AMPC_policy_cash_positive","current_profile_verdict":"current_profile_correct_if_green_blocked"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"361610","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":1,"customer_quality_score":2,"policy_or_regulatory_score":4,"valuation_repricing_score":2,"execution_risk_score":5,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":62,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":38,"stage_label_after":"Stage4C","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score"],"component_delta_explanation":"Localization policy label lacked utilization and cash conversion; price path rejected it.","MFE_90D_pct":1.04,"MAE_90D_pct":-46.27,"score_return_alignment_label":"localization_policy_hard_4C","current_profile_verdict":"current_profile_false_positive_if_stage2"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"036460","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":5,"customer_quality_score":0,"policy_or_regulatory_score":5,"valuation_repricing_score":5,"execution_risk_score":5,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":70,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":3,"customer_quality_score":0,"policy_or_regulatory_score":3,"valuation_repricing_score":3,"execution_risk_score":5,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":55,"stage_label_after":"Stage4B_policy_headline","changed_components":["contract_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","legal_or_contract_risk_score"],"component_delta_explanation":"Exploration policy headline created MFE, but reserve/commerciality/cash bridge was missing.","MFE_90D_pct":66.67,"MAE_90D_pct":-5.68,"score_return_alignment_label":"exploration_policy_local_4B","current_profile_verdict":"current_profile_too_generous_if_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"105560","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":3,"customer_quality_score":0,"policy_or_regulatory_score":4,"valuation_repricing_score":4,"execution_risk_score":3,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":77,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":2,"customer_quality_score":0,"policy_or_regulatory_score":3,"valuation_repricing_score":2,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_after":67,"stage_label_after":"Stage4B_capital_policy_refresh","changed_components":["margin_bridge_score","revision_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Value-up policy bridge exists, but CET1, payout, credit-cost and execution refresh are required.","MFE_90D_pct":18.20,"MAE_90D_pct":-15.81,"score_return_alignment_label":"bank_valueup_policy_local_4B","current_profile_verdict":"current_profile_correct_if_4B"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"316140","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":1,"customer_quality_score":0,"policy_or_regulatory_score":4,"valuation_repricing_score":2,"execution_risk_score":3,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":68,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":2,"valuation_repricing_score":0,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":47,"stage_label_after":"Stage2_cap","changed_components":["margin_bridge_score","revision_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Low-PBR value-up label lacked differentiated payout, buyback, CET1 or ROE execution bridge.","MFE_90D_pct":5.69,"MAE_90D_pct":-15.08,"score_return_alignment_label":"valueup_label_cap","current_profile_verdict":"current_profile_false_positive_if_actionable"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"005830","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":4,"customer_quality_score":0,"policy_or_regulatory_score":4,"valuation_repricing_score":4,"execution_risk_score":2,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_before":85,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":3,"customer_quality_score":0,"policy_or_regulatory_score":3,"valuation_repricing_score":3,"execution_risk_score":2,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_after":70,"stage_label_after":"Stage2_Actionable_reclassify_C22_boundary","changed_components":["margin_bridge_score","revision_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","accounting_trust_risk_score"],"component_delta_explanation":"Nonlife reserve/capital-return bridge is real but more specific to C22 than generic C31 policy learning.","MFE_90D_pct":27.05,"MAE_90D_pct":-9.26,"score_return_alignment_label":"insurance_policy_positive_elsewhere","current_profile_verdict":"requires_C22_reclassification_if_reserve_dominates"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"088350","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":1,"customer_quality_score":0,"policy_or_regulatory_score":3,"valuation_repricing_score":2,"execution_risk_score":3,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":66,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":1,"valuation_repricing_score":0,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":44,"stage_label_after":"Stage2_cap","changed_components":["margin_bridge_score","revision_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Life-insurance value-up label lacked CSM/solvency/reserve quality/payout bridge.","MFE_90D_pct":9.31,"MAE_90D_pct":-15.69,"score_return_alignment_label":"life_valueup_policy_cap","current_profile_verdict":"current_profile_false_positive_if_actionable"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"004960","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":2,"valuation_repricing_score":2,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":63,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":1,"customer_quality_score":1,"policy_or_regulatory_score":1,"valuation_repricing_score":1,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":48,"stage_label_after":"Stage2_Watch_contribution_cap","changed_components":["margin_bridge_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","accounting_trust_risk_score"],"component_delta_explanation":"Construction support beta lacked refinancing, inventory and project cash bridge.","MFE_90D_pct":8.48,"MAE_90D_pct":-8.33,"score_return_alignment_label":"construction_support_policy_watch","current_profile_verdict":"current_profile_correct_if_watch"}
```

---

## 9. Current calibrated profile stress test

The C31 policy-to-cashflow gate held:

```text
AMPC/IRA policy with production and utilization bridge
→ Stage2 can survive, Green blocked until cash-recognition proof

localization policy without utilization
→ hard 4C

exploration policy headline without commerciality
→ local 4B, no Green

financial value-up policy with partial execution
→ local 4B / Watch until payout, CET1 and credit-cost proof

low-PBR value-up label
→ cap

insurance policy/capital-return bridge
→ positive but reclassify to C22 if reserve/CSM/solvency dominates

construction support policy
→ Watch until refinancing, PF and project cash proof
```

### Rule candidate retained, not newly proposed

```text
C31_POLICY_HEADLINE_TO_LEGISLATION_BUDGET_COMPANY_CASHFLOW_GATE_V109_HELD_OUT

if C31
and policy_subsidy_legislation_valueup_or_government_headline == true
and enacted_rule_budget_eligibility_allocation_accounting_recognition_or_company_cashflow_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C31
and policy_cashflow_bridge == true
and MFE_90D_pct >= +25
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
    block_stage3_green_until_cash_recognition_refresh = true
```

```text
if C31
and policy_headline_MFE_spike == true
and commerciality_or_company_cashflow == false:
    local_4B_watch = true
    block_stage3_green = true
```

```text
if C31
and valueup_policy_label == true
and executed_payout_buyback_cancellation_capital_adequacy_or_ROE_bridge == false:
    cap_stage2_actionable_bonus = true
```

```text
if C31
and policy_localization_or_support_label == true
and MFE_90D_pct < +10
and MAE_90D_pct <= -20:
    route = Stage4C
```

```text
if C31
and dominant_driver_belongs_to_C13_C16_C21_C22_or_C30 == true:
    cap_C31_contribution = true
    require_reclassification = true
```

---

## 10. Profile comparison shadow-only summary

```yaml
profile_comparison:
  P0_e2r_2_2_rolling_calibrated_proxy:
    hypothesis: current rolling profile with bridge/4B/4C guards
    eligible_trigger_count: 8
    avg_MFE_90D_pct: 21.50
    avg_MAE_90D_pct: -15.30
    false_positive_risk: high_if_policy_label_or_valueup_headline_is_left_actionable
    verdict: adequate_only_with_C31_policy_cashflow_gate
  P0b_e2r_2_1_reference:
    hypothesis: prior calibrated profile may overcredit policy headlines if no cash bridge is required
    eligible_trigger_count: 8
    false_positive_risk: higher
    verdict: inferior
  P1_sector_specific_candidate_profile:
    hypothesis: L10 policy rows require enacted mechanism and company allocation
    changed_axes: none_new_holdout_only
    verdict: pass_holdout
  P2_canonical_archetype_candidate_profile:
    hypothesis: C31 requires policy-to-cash conversion, not headline MFE
    changed_axes: none_new_holdout_only
    verdict: pass_holdout
  P3_counterexample_guard_profile:
    hypothesis: localization/exploration/support labels without company cash route to 4C/4B/watch
    changed_axes: none_new_holdout_only
    verdict: strongest_for_false_positive_control
```

---

## 11. Coverage matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---:|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | POLICY_HEADLINE_TO_CASHFLOW_HOLDOUT_V109 | 3 | 5 | 2 | 1 | 0 | 8 | 8 | 0 | 6 | false | false | 27 |

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
  - C31|373220|Stage2-Actionable|2024-07-25
  - C31|361610|Stage4C|2024-05-16
  - C31|036460|Stage4B|2024-06-03
  - C31|105560|Stage4B|2024-07-26
  - C31|316140|Stage2-Watch|2024-07-26
  - C31|005830|Stage2-Actionable|2024-02-26
  - C31|088350|Stage2-Watch|2024-02-26
  - C31|004960|Stage2-Watch|2024-03-27
new_symbol_count: 0
new_trigger_family_count: 0
narrative_only_future_todo_count: 1
tested_existing_calibrated_axes:
  - stage2_required_bridge
  - local_4b_watch_guard
  - hard_4c_thesis_break_routes_to_4c
  - C31_policy_to_legislation_budget_cashflow_gate
  - adjacent_archetype_reclassification_guard
residual_error_types_found:
  - policy_headline_without_company_cashflow
  - localization_without_utilization
  - valueup_label_without_execution
  - exploration_policy_without_commerciality
  - construction_support_without_refinancing_cash
new_axis_proposed: null
existing_axis_strengthened:
  - C31_POLICY_HEADLINE_TO_LEGISLATION_BUDGET_COMPANY_CASHFLOW_GATE_V109_HELD_OUT
existing_axis_weakened: null
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
no_new_signal_reason: all rows reused holdout validation after direct fresh C31 policy candidates were unavailable or not recomputed
loop_contribution_label: duplicate_low_value_loop_with_cache_miss_todo
do_not_propose_new_weight_delta: true
```

```jsonl
{"row_type":"residual_contribution","round":"R11","loop":"109","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","new_independent_case_count":0,"reused_case_count":8,"new_symbol_count":0,"new_trigger_family_count":0,"narrative_only_future_todo_count":1,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","hard_4c_thesis_break_routes_to_4c","C31_policy_to_legislation_budget_cashflow_gate","adjacent_archetype_reclassification_guard"],"residual_error_types_found":["policy_headline_without_company_cashflow","localization_without_utilization","valueup_label_without_execution","exploration_policy_without_commerciality","construction_support_without_refinancing_cash"],"loop_contribution_label":"duplicate_low_value_loop_with_cache_miss_todo","do_not_propose_new_weight_delta":true}
```

---

## 14. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Treat this R11/C31 loop 109 as holdout validation only. Batch it with C31 loops 103~108, C13 AMPC/IRA rows, C16 policy-resource rows, C21/C22 value-up/capital-return rows, C30 construction support rows, and R13 accounting-trust / Stage2 false-positive / high-MAE / 4B-4C guardrails. If exact same_entry_group_id rows already exist, dedupe them. Preserve the C31 policy-headline-to-legislation/budget/company-cashflow gate and adjacent-archetype reclassification guard, but do not create a new weight delta from this loop because no new independent case was added. Future research should directly reprice new C31 policy/subsidy/legal events such as grid budget, defense subsidy, shipbuilding support, value-up executions, AMPC eligibility changes, nuclear project law/budget events, and PF guarantee policies when stock-web shards are accessible.
```

---

## 15. Next research state

```yaml
completed_round: R11
completed_loop: 109
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
  - C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
  - C15_MATERIAL_SPREAD_SUPERCYCLE
  - C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
  - C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
```
