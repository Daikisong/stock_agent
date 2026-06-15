# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R11
selected_loop: 105
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: POLICY_TO_COMPANY_CASH_BRIDGE_HOLDOUT_VALIDATION_BATTERY_VALUEUP_PF
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
  stock_web_manifest: read_ok
  uncached_symbol_shards:
    - 051910: cache_miss_observed
    - 096770: cache_miss_observed
    - 006360: cache_miss_observed
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
loop_objective:
  - holdout_validation
  - policy_label_to_company_cash_bridge_gate
  - cross_policy_family_consistency_check
price_source: Songdaiki/stock-web
price_data_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

`C31_POLICY_SUBSIDY_LEGISLATION_EVENT` remains Priority 0 in the current no-repeat index: 3 representative rows and 27 rows short of the 30-row minimum. The v12 scheduler maps C31 to `R11 / L10_POLICY_EVENT_CROSS_REDTEAM_MISC`.

This file continues the local C31 sequence after `R11/C31 loop 104`; selected loop is therefore `105`.

This is a **holdout validation / cross-policy-family consolidation** MD. It does not pretend to discover fresh live policy cases. Direct uncached symbol shards for several additional policy-sensitive names returned cache miss in this turn, so this file reuses current-session stock-web-derived C31/C13/C21/C22/C30 rows that already contain complete 30D/90D/180D MFE and MAE from `Songdaiki/stock-web` tradable OHLC. Exact duplicate source keys should be deduped during batch ingest. No production scoring is changed.

---

## 1. Research thesis

C31 is not `policy headline exists`.

It is the policy-to-company-cash bridge:

```text
battery IRA / AMPC / localization
financial Value-up / capital-return policy
PF / housing / liquidity support
governance or public-policy pressure
→ must become company-specific cashflow, tax credit, utilization, payout, buyback, refinancing, guarantee relief, presale, debt-service, reserve quality or margin
→ then price path decides Stage2, local 4B, or hard 4C
```

The recurring mistake is the same across sectors:

```text
policy umbrella
≠ company cash bridge
```

This loop validates the current C31 gate across three policy families:

1. **Battery policy / AMPC**
   - AMPC/IRA only works if utilization, customer call-off, ESS/non-EV demand and cash conversion appear.

2. **Financial Value-up**
   - Value-up only works if CET1, payout, buyback, ROE, reserve quality, CSM, solvency or capital-return execution appears.

3. **PF / housing policy**
   - PF support only works if refinancing, guarantee relief, presale, debt-service or cash conversion reaches the issuer.

The goal is not to add a new weight delta. The goal is to test whether the same bridge-first rule survives across very different policy labels.

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 8
  actual_cases: 10
  source_archetypes:
    - C31_POLICY_SUBSIDY_LEGISLATION_EVENT
    - C13_BATTERY_JV_UTILIZATION_AMPC_IRA
    - C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
    - C22_INSURANCE_RATE_CYCLE_RESERVE
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
    - C31 canonical rule holdout validation
    - policy label false-positive guard
    - delayed bridge no-backfill guard
    - local 4B vs hard 4C split
    - no production scoring changes
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
  - R11/C31 loop 102
  - R11/C31 loop 103
  - R11/C31 loop 104
  - R3/C13 loop 135
  - R6/C21 loop 112
  - R6/C22 loop 111
  - R10/C30 loop 102
  - R13 accounting-trust / Stage2 false-positive / high-MAE / 4B-4C guardrails
reason:
  - all reused rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - uncached additional policy-sensitive symbol shards returned cache miss in this turn
  - exact duplicate C31 keys should be deduped during batch ingest
  - this file is holdout validation / consolidation evidence only
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","selected_round":"R11","selected_loop":105,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"BATTERY_AMPC_IRA_CUSTOMER_DIVERSIFICATION_CASH_BRIDGE_POSITIVE","symbol":"373220","name":"LG에너지솔루션","trigger_type":"Stage2-Actionable","entry_date":"2024-07-25","entry_price":332500,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":18.50,"MAE_30D_pct":-6.47,"MFE_90D_pct":33.53,"MAE_90D_pct":-6.47,"MFE_180D_pct":33.53,"MAE_180D_pct":-6.47,"forward_high_30d":394000,"forward_low_30d":311000,"forward_high_90d":444000,"forward_low_90d":311000,"forward_high_180d":444000,"forward_low_180d":311000,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C31|373220|Stage2-Actionable|2024-07-25","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control","reuse_reason":"same C31 battery-policy positive row from loop 102","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"battery_policy_positive_control","novelty_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|373220|Stage2-Actionable|2024-07-25","non_price_bridge":"IRA/AMPC support plus customer diversification and ESS/non-EV demand bridge","score_alignment":"keep Stage2; require AMPC cash conversion, utilization and customer call-off refresh before Green"}
{"row_type":"trigger","selected_round":"R11","selected_loop":105,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"SEPARATOR_POLICY_LABEL_WITHOUT_UTILIZATION_CASH_BRIDGE_HARD_4C","symbol":"361610","name":"SK아이이테크놀로지","trigger_type":"Stage4C","entry_date":"2024-05-16","entry_price":57600,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":1.04,"MAE_30D_pct":-25.87,"MFE_90D_pct":1.04,"MAE_90D_pct":-46.27,"MFE_180D_pct":1.04,"MAE_180D_pct":-60.68,"forward_high_30d":58200,"forward_low_30d":42700,"forward_high_90d":58200,"forward_low_90d":30950,"forward_high_180d":58200,"forward_low_180d":22650,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C31|361610|Stage4C|2024-05-16","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","reuse_reason":"same C31 separator false-positive row from loop 102","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"battery_policy_hard_counterexample","novelty_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|361610|Stage4C|2024-05-16","non_price_bridge":"separator/material policy exposure without customer pull, utilization, parent financing or cash-conversion bridge","score_alignment":"hard 4C; policy/localization label cannot substitute for utilization and cashflow"}
{"row_type":"trigger","selected_round":"R11","selected_loop":105,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"VALUEUP_NONLIFE_RESERVE_CAPITAL_RETURN_POLICY_POSITIVE","symbol":"005830","name":"DB손해보험","trigger_type":"Stage2-Actionable","entry_date":"2024-02-26","entry_price":95000,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":15.79,"MAE_30D_pct":-4.11,"MFE_90D_pct":27.05,"MAE_90D_pct":-9.26,"MFE_180D_pct":30.53,"MAE_180D_pct":-9.26,"forward_high_30d":110000,"forward_low_30d":91100,"forward_high_90d":120700,"forward_low_90d":86200,"forward_high_180d":124000,"forward_low_180d":86200,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C31|005830|Stage2-Actionable|2024-02-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control","reuse_reason":"same C31 financial-policy positive row from loop 103","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"financial_policy_positive_control","novelty_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|005830|Stage2-Actionable|2024-02-26","non_price_bridge":"Value-up policy pressure reached nonlife reserve quality, loss-ratio discipline and capital-return bridge","score_alignment":"keep Stage2; allow Yellow only while reserve quality, payout and capital-return execution stay refreshed"}
{"row_type":"trigger","selected_round":"R11","selected_loop":105,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"BANK_CAPITAL_RETURN_POLICY_REAL_BRIDGE_LOCAL_4B","symbol":"105560","name":"KB금융","trigger_type":"Stage4B","entry_date":"2024-07-26","entry_price":87900,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":5.12,"MAE_30D_pct":-15.81,"MFE_90D_pct":18.20,"MAE_90D_pct":-15.81,"MFE_180D_pct":18.20,"MAE_180D_pct":-15.81,"forward_high_30d":92400,"forward_low_30d":74000,"forward_high_90d":103900,"forward_low_90d":74000,"forward_high_180d":103900,"forward_low_180d":74000,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C31|105560|Stage4B|2024-07-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_local_4B","reuse_reason":"same C31 bank policy local-4B row from loops 103/104","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"financial_policy_local_4B","novelty_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|105560|Stage4B|2024-07-26","non_price_bridge":"Value-up bank capital-return policy bridge, but CET1, credit-cost and payout refresh required","score_alignment":"local 4B until capital, payout, credit-cost and earnings bridge refresh"}
{"row_type":"trigger","selected_round":"R11","selected_loop":105,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"LOW_PBR_BANK_POLICY_LABEL_WITHOUT_EXECUTION_CAP","symbol":"316140","name":"우리금융지주","trigger_type":"Stage2-Watch","entry_date":"2024-07-26","entry_price":16180,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":4.08,"MAE_30D_pct":-15.08,"MFE_90D_pct":5.69,"MAE_90D_pct":-15.08,"MFE_180D_pct":5.69,"MAE_180D_pct":-15.08,"forward_high_30d":16840,"forward_low_30d":13740,"forward_high_90d":17100,"forward_low_90d":13740,"forward_high_180d":17100,"forward_low_180d":13740,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C31|316140|Stage2-Watch|2024-07-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_stage2_cap","reuse_reason":"same low-PBR bank label cap from loops 103/104","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"financial_policy_cap","novelty_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|316140|Stage2-Watch|2024-07-26","non_price_bridge":"low-PBR bank Value-up policy label without differentiated payout, buyback, CET1 or ROE execution bridge","score_alignment":"cap C31 policy bonus; require incremental capital-return execution before Actionable"}
{"row_type":"trigger","selected_round":"R11","selected_loop":105,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"PF_POLICY_LARGE_BUILDER_SURVIVOR_WATCH","symbol":"000720","name":"현대건설","trigger_type":"Stage2-Watch","entry_date":"2024-01-26","entry_price":33100,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":7.30,"MAE_30D_pct":-3.50,"MFE_90D_pct":8.80,"MAE_90D_pct":-5.70,"MFE_180D_pct":8.80,"MAE_180D_pct":-12.20,"forward_high_30d":34850,"forward_low_30d":31950,"forward_high_90d":36000,"forward_low_90d":31200,"forward_high_180d":36000,"forward_low_180d":29050,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C31|000720|Stage2-Watch|2024-01-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_survivor_watch","reuse_reason":"same PF-policy large-builder watch row from C31 loop 104","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"pf_policy_watch","novelty_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|000720|Stage2-Watch|2024-01-26","non_price_bridge":"PF/housing support policy stabilized large-builder risk, but issuer-specific refinancing/cash bridge remained insufficient","score_alignment":"Stage2-Watch only; require debt-service, margin, receivable or cash conversion bridge before Actionable"}
{"row_type":"trigger","selected_round":"R11","selected_loop":105,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"PF_POLICY_WEAK_LIQUIDITY_LABEL_HARD_4C","symbol":"002990","name":"금호건설","trigger_type":"Stage4C","entry_date":"2024-01-26","entry_price":5030,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":5.00,"MAE_30D_pct":-4.60,"MFE_90D_pct":5.00,"MAE_90D_pct":-27.50,"MFE_180D_pct":5.00,"MAE_180D_pct":-41.00,"forward_high_30d":5280,"forward_low_30d":4800,"forward_high_90d":5280,"forward_low_90d":3650,"forward_high_180d":5280,"forward_low_180d":2970,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C31|002990|Stage4C|2024-01-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","reuse_reason":"same PF-policy weak-liquidity hard-block row from C31 loop 104","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"pf_policy_hard_counterexample","novelty_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|002990|Stage4C|2024-01-26","non_price_bridge":"PF relief vocabulary without liquidity, debt-service, guarantee relief or cash bridge","score_alignment":"hard 4C; policy umbrella did not reach issuer cashflow"}
{"row_type":"trigger","selected_round":"R11","selected_loop":105,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"PF_HOUSING_POLICY_DELAYED_LOCAL_4B_NO_BACKFILL","symbol":"294870","name":"HDC현대산업개발","trigger_type":"Stage4B","entry_date":"2024-05-13","entry_price":17920,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":2.12,"MAE_30D_pct":-6.58,"MFE_90D_pct":37.28,"MAE_90D_pct":-6.58,"MFE_180D_pct":57.37,"MAE_180D_pct":-6.58,"forward_high_30d":18300,"forward_low_30d":16740,"forward_high_90d":24600,"forward_low_90d":16740,"forward_high_180d":28200,"forward_low_180d":16740,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C31|294870|Stage4B|2024-05-13","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_delayed_local_4B","reuse_reason":"same PF/housing delayed local-4B row from C31 loop 104","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"pf_policy_delayed_4B","novelty_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|294870|Stage4B|2024-05-13","non_price_bridge":"housing/PF soft-landing path helped later, but issuer-specific refinancing/liquidity bridge was not visible at entry","score_alignment":"local 4B; do not backfill later rebound as immediate Stage2"}
{"row_type":"trigger","selected_round":"R11","selected_loop":105,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"WORKOUT_POLICY_STRESS_CONTROL_NOT_CLEAN_EQUITY_RECOVERY","symbol":"009410","name":"태영건설","trigger_type":"Stage2-Watch","entry_date":"2024-01-11","entry_price":3765,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":9.16,"MAE_30D_pct":-42.10,"MFE_90D_pct":9.16,"MAE_90D_pct":-42.10,"MFE_180D_pct":62.28,"MAE_180D_pct":-42.10,"forward_high_30d":4110,"forward_low_30d":2180,"forward_high_90d":4110,"forward_low_90d":2180,"forward_high_180d":6110,"forward_low_180d":2180,"corporate_action_window_status":"workout_or_trading_gap_contamination_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":false,"same_entry_group_id":"C31|009410|Stage2-Watch|2024-01-11","dedupe_for_aggregate":true,"aggregate_group_role":"stress_control_only","reuse_reason":"same workout stress-control row from C31 loop 104 / C30 loop 102","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"workout_stress_control_only","novelty_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|009410|Stage2-Watch|2024-01-11","non_price_bridge":"workout / debt restructuring policy framework may preserve creditors before equity; corporate-action/trading-gap window not clean","score_alignment":"exclude from clean aggregate; use as stress-control for policy-workout-not-equity-recovery"}
{"row_type":"trigger","selected_round":"R11","selected_loop":105,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"LIFE_INSURANCE_VALUEUP_POLICY_LABEL_STAGE2_CAP","symbol":"088350","name":"한화생명","trigger_type":"Stage2-Watch","entry_date":"2024-02-26","entry_price":3060,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":9.31,"MAE_30D_pct":-8.17,"MFE_90D_pct":9.31,"MAE_90D_pct":-15.69,"MFE_180D_pct":9.31,"MAE_180D_pct":-15.69,"forward_high_30d":3345,"forward_low_30d":2810,"forward_high_90d":3345,"forward_low_90d":2580,"forward_high_180d":3345,"forward_low_180d":2580,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C31|088350|Stage2-Watch|2024-02-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_stage2_cap","reuse_reason":"same life-insurance policy label cap from C31 loop 103","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"financial_policy_cap","novelty_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|088350|Stage2-Watch|2024-02-26","non_price_bridge":"life-insurance Value-up policy label without refreshed CSM, solvency, reserve quality or payout bridge","score_alignment":"cap C31 policy bonus; require CSM/solvency/capital-return evidence before Actionable"}
```

---

## 5. Case analysis

### 5.1 LG Energy Solution / 373220 — battery-policy positive control

AMPC/IRA support worked because it connected to company-level customer diversification, utilization and cashflow.

```yaml
entry_close: 332500
90D_MFE_MAE: +33.53 / -6.47
180D_MFE_MAE: +33.53 / -6.47
route: KeepStage2
```

### 5.2 SK IE Technology / 361610 — battery-policy hard 4C

Separator policy exposure did not become utilization or cash bridge.

```yaml
entry_close: 57600
90D_MFE_MAE: +1.04 / -46.27
180D_MFE_MAE: +1.04 / -60.68
route: Stage4C
```

### 5.3 DB Insurance / 005830 — Value-up policy positive control

Financial policy worked because it connected to reserve and capital-return bridge.

```yaml
entry_close: 95000
90D_MFE_MAE: +27.05 / -9.26
180D_MFE_MAE: +30.53 / -9.26
route: KeepStage2
```

### 5.4 KB Financial / 105560 — real bridge, local 4B

The bank capital-return bridge is real, but needs refresh.

```yaml
entry_close: 87900
90D_MFE_MAE: +18.20 / -15.81
180D_MFE_MAE: +18.20 / -15.81
route: Stage4B
```

### 5.5 Woori Financial / 316140 — low-PBR policy cap

Low-PBR label is not enough.

```yaml
entry_close: 16180
90D_MFE_MAE: +5.69 / -15.08
180D_MFE_MAE: +5.69 / -15.08
route: Stage2-Watch
```

### 5.6 Hyundai E&C / 000720 — PF policy survivor watch

Stabilization is visible, but cash bridge is not.

```yaml
entry_close: 33100
90D_MFE_MAE: +8.80 / -5.70
180D_MFE_MAE: +8.80 / -12.20
route: Stage2-Watch
```

### 5.7 Kumho E&C / 002990 — PF policy hard 4C

Policy umbrella did not reach issuer liquidity.

```yaml
entry_close: 5030
90D_MFE_MAE: +5.00 / -27.50
180D_MFE_MAE: +5.00 / -41.00
route: Stage4C
```

### 5.8 HDC Hyundai Development / 294870 — delayed PF local 4B

Later validation cannot be backfilled.

```yaml
entry_close: 17920
90D_MFE_MAE: +37.28 / -6.58
180D_MFE_MAE: +57.37 / -6.58
route: Stage4B
```

### 5.9 Taeyoung E&C / 009410 — workout stress-control

Not clean aggregate.

```yaml
entry_close: 3765
90D_MFE_MAE: +9.16 / -42.10
180D_MFE_MAE: +62.28 / -42.10
route: stress-control only
```

### 5.10 Hanwha Life / 088350 — life-insurance policy cap

Value-up label lacks CSM/solvency/payout bridge.

```yaml
entry_close: 3060
90D_MFE_MAE: +9.31 / -15.69
180D_MFE_MAE: +9.31 / -15.69
route: Stage2-Watch
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
calibration_usable_case_count: 9
calibration_usable_trigger_count: 9
stress_control_case_count: 1
positive_case_count: 3
counterexample_count: 4
local_4B_watch_count: 3
current_profile_error_count: 6
diversity_score_summary: "battery-policy, financial-policy, PF-policy, cap, 4B, hard 4C covered; all rows reused"
loop_contribution_label: duplicate_low_value_loop
do_not_propose_new_weight_delta: true
```

| symbol | policy family | route | 90D MFE/MAE | 180D MFE/MAE |
|---|---:|---:|---:|---:|
| 373220 | battery AMPC | keep Stage2 | +33.53 / -6.47 | +33.53 / -6.47 |
| 361610 | battery policy label | hard 4C | +1.04 / -46.27 | +1.04 / -60.68 |
| 005830 | Value-up insurance | keep Stage2 | +27.05 / -9.26 | +30.53 / -9.26 |
| 105560 | Value-up bank | local 4B | +18.20 / -15.81 | +18.20 / -15.81 |
| 316140 | low-PBR bank | cap | +5.69 / -15.08 | +5.69 / -15.08 |
| 000720 | PF survivor | watch | +8.80 / -5.70 | +8.80 / -12.20 |
| 002990 | weak PF | hard 4C | +5.00 / -27.50 | +5.00 / -41.00 |
| 294870 | delayed PF | local 4B | +37.28 / -6.58 | +57.37 / -6.58 |
| 009410 | workout | stress only | +9.16 / -42.10 | +62.28 / -42.10 |
| 088350 | life policy cap | watch | +9.31 / -15.69 | +9.31 / -15.69 |

---

## 7. Current calibrated profile stress test

The C31 policy-to-cash bridge rule held across three families:

```text
AMPC/IRA -> only useful with utilization/customer/cash bridge
Value-up -> only useful with payout/ROE/reserve/capital bridge
PF/housing policy -> only useful with issuer-specific refinancing/cash bridge
```

### Rule candidate retained, not newly proposed

```text
C31_POLICY_TO_COMPANY_CASH_BRIDGE_GATE_V105_HELD_OUT

if C31
and policy_label == true
and company_specific_cash_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C31
and policy_cash_bridge == true
and MFE_90D_pct >= +20
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
```

```text
if C31
and policy_cash_bridge == true
and MAE_90D_pct <= -12:
    local_4B_watch = true
    block_stage3_green_until_cash_bridge_refresh = true
```

```text
if C31
and policy_label == true
and MFE_90D_pct <= +5
and MAE_90D_pct <= -20
and company_specific_cash_bridge == false:
    route = Stage4C
```

```text
if C31
and delayed_policy_validation == true:
    route = delayed_local_4B
    do_not_backfill_as_immediate_Stage2 = true
```

---

## 8. Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 10
calibration_usable_trigger_count: 9
representative_trigger_count: 0
new_weight_evidence_candidate_count: 0
guardrail_candidate_count: 10
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
  - C31_POLICY_TO_COMPANY_CASH_BRIDGE_GATE_V105_HELD_OUT
existing_axis_weakened: null
one_line_summary: "This loop adds 0 new independent cases and validates the C31 policy-to-company-cash bridge gate across battery, financial and PF policy families."
```

---

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Treat this R11/C31 loop 105 as holdout validation only. Batch it with C31 loops 100~104, C13, C21, C22, C30 and R13 policy/accounting-trust guardrails. If exact same_entry_group_id rows already exist, dedupe them. Preserve the C31 policy-to-company-cash bridge gate, but do not create a new weight delta from this loop because uncached additional symbol shards returned cache miss and no new independent case was added.
```

---

## 11. Next research state

```yaml
completed_round: R11
completed_loop: 105
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
  - C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
  - C15_MATERIAL_SPREAD_SUPERCYCLE
  - R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
  - C18_CONSUMER_EXPORT_CHANNEL_REORDER
```
