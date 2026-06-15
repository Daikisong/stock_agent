# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R11
selected_loop: 103
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: VALUEUP_FINANCIAL_INSURANCE_POLICY_TO_CAPITAL_RETURN_RESERVE_CASH_BRIDGE_VS_LOW_PBR_LABEL
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
  stock_web_manifest: read_ok
  uncached_symbol_shards: cache_miss_observed
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

`C31_POLICY_SUBSIDY_LEGISLATION_EVENT` remains Priority 0 in the current no-repeat index: 3 representative rows, still 27 rows short of the 30-row minimum. The v12 scheduler maps C31 to `R11 / L10_POLICY_EVENT_CROSS_REDTEAM_MISC`.

This run continues the current local C31 sequence after `R11/C31 loop 102`. It uses the Korea Value-up / financial-policy lens, but it does not treat every low-PBR financial or insurance stock as a successful policy beneficiary.

Direct uncached stock-web symbol shards returned cache misses in this turn, so this MD reuses current-session stock-web-derived C21/C22 rows already calculated from `Songdaiki/stock-web` tradable 1D OHLC. This file changes the canonical scope to C31 and asks whether the policy headline became a company-specific capital-return, reserve, solvency, payout, or cashflow bridge. No production scoring is changed.

---

## 1. Research thesis

C31 is not `policy headline = value unlocked`.

It is the policy-to-company-cash bridge:

```text
Value-up / shareholder-return policy / financial-sector rerating / insurance-capital policy
→ CET1, payout, buyback/cancellation, ROE, reserve quality, CSM, solvency, loss ratio or capital return
→ price path validation
```

The market often trades a policy umbrella first. C31 should only keep Stage2 when the umbrella becomes a pipe into company cashflow.

This loop separates five routes:

1. **Nonlife insurer reserve/capital-return bridge**
   - Value-up or financial policy pressure is valid only when reserve quality, loss-ratio discipline and capital-return execution are traceable.

2. **Reinsurance rate-cycle reserve bridge**
   - A reinsurance name can be a low-volatility policy/rate-cycle control, but modest MFE means Watch unless capital-return execution strengthens.

3. **Life-insurance Value-up label**
   - CSM, solvency and payout evidence are required. Label alone is capped.

4. **Bank-holding capital-return bridge with high-MAE watch**
   - Capital-return bridge can be real, but CET1, credit-cost and payout refresh are needed before Green.

5. **Low-PBR bank label without incremental execution**
   - Low-PBR / Value-up vocabulary is not enough. If MFE is weak and MAE meaningful, policy bonus is capped or blocked.

---

## 2. Source validation

```yaml
stock_web_manifest:
  source_name: FinanceData/marcap
  price_adjustment_status: raw_unadjusted_marcap
  max_date: 2026-02-20
  calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
  caveat: Raw/unadjusted OHLC; corporate-action-contaminated windows blocked by default.
```

Local stock-web-derived row provenance:

```yaml
reused_price_rows_from_current_session:
  - R6/C21 loop 112
  - R6/C22 loop 111
  - R13 Stage2 false-positive loop 9
  - R13 accounting-trust loop 10
  - R13 high-MAE loop 7
reason:
  - all rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - current file changes canonical scope to C31 policy/subsidy/legislation event
  - exact source-archetype keys should be deduped separately from this C31 canonical key
  - no production scoring changed
```

Symbol caveats:

```yaml
005830:
  name: DB손해보험
  source_archetype: C22_INSURANCE_RATE_CYCLE_RESERVE
  role: nonlife reserve/loss-ratio/capital-return bridge under Value-up / financial policy lens
  calibration_usable: true

003690:
  name: 코리안리
  source_archetype: C22_INSURANCE_RATE_CYCLE_RESERVE
  role: reinsurance rate-cycle reserve low-vol control
  calibration_usable: true

088350:
  name: 한화생명
  source_archetype: C22_INSURANCE_RATE_CYCLE_RESERVE
  role: life-insurance Value-up label without CSM/solvency/payout bridge
  calibration_usable: true

105560:
  name: KB금융
  source_archetype: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
  role: bank capital-return bridge with high-MAE local 4B
  calibration_usable: true

316140:
  name: 우리금융지주
  source_archetype: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
  role: low-PBR bank label with weak incremental execution
  calibration_usable: true
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R11","loop":103,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"VALUEUP_NONLIFE_RESERVE_CAPITAL_RETURN_POLICY_CASH_BRIDGE_POSITIVE_CONTROL","source_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"005830","name":"DB손해보험","trigger_type":"Stage2-Actionable","entry_date":"2024-02-26","entry_close":95000,"price_basis":"tradable_raw","mfe_30d_pct":15.79,"mae_30d_pct":-4.11,"mfe_90d_pct":27.05,"mae_90d_pct":-9.26,"mfe_180d_pct":30.53,"mae_180d_pct":-9.26,"forward_high_30d":110000,"forward_low_30d":91100,"forward_high_90d":120700,"forward_low_90d":86200,"forward_high_180d":124000,"forward_low_180d":86200,"calibration_usable":true,"case_role":"policy_cash_bridge_positive_control","novelty_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|005830|Stage2-Actionable|2024-02-26","non_price_bridge":"Value-up / financial policy pressure reached nonlife reserve quality, loss-ratio discipline and capital-return bridge","score_alignment":"keep Stage2; allow Yellow path while reserve quality, payout and capital-return execution stay refreshed"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R11","loop":103,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"VALUEUP_REINSURANCE_RATE_CYCLE_POLICY_LOW_VOL_WATCH","source_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"003690","name":"코리안리","trigger_type":"Stage2-Watch","entry_date":"2024-02-26","entry_close":7930,"price_basis":"tradable_raw","mfe_30d_pct":6.81,"mae_30d_pct":-1.01,"mfe_90d_pct":6.81,"mae_90d_pct":-5.42,"mfe_180d_pct":13.49,"mae_180d_pct":-5.42,"forward_high_30d":8470,"forward_low_30d":7850,"forward_high_90d":8470,"forward_low_90d":7500,"forward_high_180d":9000,"forward_low_180d":7500,"calibration_usable":true,"case_role":"low_vol_watch_control","novelty_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|003690|Stage2-Watch|2024-02-26","non_price_bridge":"reinsurance rate-cycle, underwriting and reserve-discipline bridge under financial Value-up lens","score_alignment":"Stage2-Watch only; MFE is modest, so require payout/ROE or reserve bridge refresh before Actionable"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R11","loop":103,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"LIFE_INSURANCE_VALUEUP_POLICY_LABEL_WITHOUT_CSM_SOLVENCY_BRIDGE_CAP","source_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"088350","name":"한화생명","trigger_type":"Stage2-Watch","entry_date":"2024-02-26","entry_close":3060,"price_basis":"tradable_raw","mfe_30d_pct":9.31,"mae_30d_pct":-8.17,"mfe_90d_pct":9.31,"mae_90d_pct":-15.69,"mfe_180d_pct":9.31,"mae_180d_pct":-15.69,"forward_high_30d":3345,"forward_low_30d":2810,"forward_high_90d":3345,"forward_low_90d":2580,"forward_high_180d":3345,"forward_low_180d":2580,"calibration_usable":true,"case_role":"policy_label_cap","novelty_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|088350|Stage2-Watch|2024-02-26","non_price_bridge":"life-insurance Value-up policy label without refreshed CSM, solvency, reserve quality or payout bridge","score_alignment":"cap C31 policy bonus; require CSM/solvency/capital-return evidence before Actionable"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R11","loop":103,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"VALUEUP_BANK_CAPITAL_RETURN_POLICY_BRIDGE_HIGH_MAE_LOCAL_4B","source_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"105560","name":"KB금융","trigger_type":"Stage2-Actionable","entry_date":"2024-07-26","entry_close":87900,"price_basis":"tradable_raw","mfe_30d_pct":5.12,"mae_30d_pct":-15.81,"mfe_90d_pct":18.20,"mae_90d_pct":-15.81,"mfe_180d_pct":18.20,"mae_180d_pct":-15.81,"forward_high_30d":92400,"forward_low_30d":74000,"forward_high_90d":103900,"forward_low_90d":74000,"forward_high_180d":103900,"forward_low_180d":74000,"calibration_usable":true,"case_role":"policy_bridge_local_4B","novelty_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|105560|Stage2-Actionable|2024-07-26","non_price_bridge":"Value-up bank capital-return policy bridge, but CET1, credit-cost and payout refresh required after high-ish MAE","score_alignment":"Stage2 may open; local 4B until capital, payout, credit-cost and earnings bridge refresh"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R11","loop":103,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"LOW_PBR_BANK_VALUEUP_POLICY_LABEL_WITHOUT_INCREMENTAL_EXECUTION_CAP","source_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"316140","name":"우리금융지주","trigger_type":"Stage2-Watch","entry_date":"2024-07-26","entry_close":16180,"price_basis":"tradable_raw","mfe_30d_pct":4.08,"mae_30d_pct":-15.08,"mfe_90d_pct":5.69,"mae_90d_pct":-15.08,"mfe_180d_pct":5.69,"mae_180d_pct":-15.08,"forward_high_30d":16840,"forward_low_30d":13740,"forward_high_90d":17100,"forward_low_90d":13740,"forward_high_180d":17100,"forward_low_180d":13740,"calibration_usable":true,"case_role":"policy_label_cap","novelty_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|316140|Stage2-Watch|2024-07-26","non_price_bridge":"low-PBR bank Value-up policy label without sufficiently differentiated payout, buyback or CET1 execution bridge","score_alignment":"cap C31 policy bonus; require incremental capital-return execution before Actionable"}
```

---

## 4. Case analysis

### 4.1 DB Insurance / 005830 — policy became reserve and capital-return bridge

DB Insurance is the positive control. The policy/value-up umbrella mattered because it reached a company-specific insurance accounting bridge.

```yaml
entry_close: 95000
30D_MFE_MAE: +15.79 / -4.11
90D_MFE_MAE: +27.05 / -9.26
180D_MFE_MAE: +30.53 / -9.26
route: Stage2-Actionable
```

This is the correct C31 outcome: policy headline plus traceable reserve quality, loss-ratio discipline and shareholder-return execution.

---

### 4.2 Korean Re / 003690 — low-vol reinsurance watch

Korean Re has a clean reserve/rate-cycle bridge but modest MFE.

```yaml
entry_close: 7930
30D_MFE_MAE: +6.81 / -1.01
90D_MFE_MAE: +6.81 / -5.42
180D_MFE_MAE: +13.49 / -5.42
route: Stage2-Watch
```

Policy contribution stays capped until capital-return or underwriting-cycle evidence strengthens.

---

### 4.3 Hanwha Life / 088350 — life-insurance policy label cap

Hanwha Life is the policy-label cap. The label is visible, but C31 cannot assume CSM, solvency or payout economics.

```yaml
entry_close: 3060
30D_MFE_MAE: +9.31 / -8.17
90D_MFE_MAE: +9.31 / -15.69
180D_MFE_MAE: +9.31 / -15.69
route: Stage2-Watch / cap
```

---

### 4.4 KB Financial / 105560 — bank capital-return bridge, but 4B

KB Financial has a real Value-up/capital-return bridge, but MAE is large enough to block Green.

```yaml
entry_close: 87900
30D_MFE_MAE: +5.12 / -15.81
90D_MFE_MAE: +18.20 / -15.81
180D_MFE_MAE: +18.20 / -15.81
route: Stage2-Actionable with local 4B
```

The bridge needs refresh through CET1, payout, buyback, credit cost and ROE.

---

### 4.5 Woori Financial / 316140 — low-PBR policy label cap

Woori is the low-PBR bank label cap. It did not differentiate enough through incremental capital-return execution.

```yaml
entry_close: 16180
30D_MFE_MAE: +4.08 / -15.08
90D_MFE_MAE: +5.69 / -15.08
180D_MFE_MAE: +5.69 / -15.08
route: Stage2-Watch / cap
```

---

## 5. Score-return alignment

```yaml
new_independent_case_count: 5
new_visible_C31_symbol_count: 5
same_archetype_new_trigger_family_count: 5
calibration_usable_case_count: 5
calibration_usable_trigger_count: 5
positive_case_count: 2
counterexample_or_cap_count: 3
local_4B_watch_count: 1
current_profile_error_count: 3
```

| symbol | source | role | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---|---:|---:|---:|---:|---|
| 005830 | C22 | positive-control | +15.79 / -4.11 | +27.05 / -9.26 | +30.53 / -9.26 | policy works when reserve/capital-return bridge validates |
| 003690 | C22 | low-vol watch | +6.81 / -1.01 | +6.81 / -5.42 | +13.49 / -5.42 | rate-cycle bridge is clean but modest |
| 088350 | C22 | policy cap | +9.31 / -8.17 | +9.31 / -15.69 | +9.31 / -15.69 | life-insurance label needs CSM/solvency evidence |
| 105560 | C21 | bank 4B | +5.12 / -15.81 | +18.20 / -15.81 | +18.20 / -15.81 | bank capital-return bridge needs refresh |
| 316140 | C21 | low-PBR cap | +4.08 / -15.08 | +5.69 / -15.08 | +5.69 / -15.08 | low-PBR bank label lacks incremental execution |

---

## 6. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"005830","raw_policy_directness":3,"raw_company_cash_bridge":5,"raw_reserve_or_capital_quality":5,"raw_payout_execution":4,"raw_validation":4,"raw_label_only_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2Actionable_policy_cash_bridge_positive"}
{"row_type":"score_simulation","symbol":"003690","raw_policy_directness":2,"raw_company_cash_bridge":3,"raw_reserve_or_capital_quality":3,"raw_payout_execution":2,"raw_validation":2,"raw_label_only_risk":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Stage2Watch_reinsurance_low_vol"}
{"row_type":"score_simulation","symbol":"088350","raw_policy_directness":3,"raw_company_cash_bridge":1,"raw_reserve_or_capital_quality":1,"raw_payout_execution":1,"raw_validation":0,"raw_label_only_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2Cap_life_label"}
{"row_type":"score_simulation","symbol":"105560","raw_policy_directness":4,"raw_company_cash_bridge":4,"raw_reserve_or_capital_quality":3,"raw_payout_execution":4,"raw_validation":3,"raw_label_only_risk":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2Actionable_local4B_bank_capital_return"}
{"row_type":"score_simulation","symbol":"316140","raw_policy_directness":3,"raw_company_cash_bridge":1,"raw_reserve_or_capital_quality":2,"raw_payout_execution":1,"raw_validation":0,"raw_label_only_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2Cap_lowPBR_bank_label"}
```

---

## 7. Current calibrated profile stress test

### Existing error risk

C31 can over-credit:

```text
Value-up
low PBR
financial policy
insurance policy
```

The correct C31 bridge is narrower:

```text
policy -> company cash bridge -> price validation
```

A policy is wind. The company still needs a sail and a rudder. For banks and insurers, the sail is CET1, payout, reserve quality, CSM, solvency, ROE and actual capital-return execution.

### Rule candidate

```text
C31_VALUEUP_FINANCIAL_POLICY_TO_CASH_BRIDGE_REQUIREMENT_V103

if C31
and Valueup_or_financial_policy_label == true
and CET1_payout_buyback_ROE_reserve_CSM_solvency_or_capital_return_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C31
and insurance_policy_label == true
and reserve_loss_ratio_CSM_solvency_or_capital_return_bridge == false:
    stage2_actionable_bonus = 0
    route = Stage2Cap
```

```text
if C31
and bank_policy_label == true
and CET1_credit_cost_payout_buyback_or_ROE_bridge == false:
    stage2_actionable_bonus = 0
    route = Stage2Cap
```

```text
if C31
and company_specific_financial_cash_bridge == true
and MFE_90D_pct >= +20
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
```

```text
if C31
and company_specific_financial_cash_bridge == true
and MAE_90D_pct <= -12:
    local_4B_watch = true
    block_stage3_green_until_capital_earnings_refresh = true
```

---

## 8. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: C31_VALUEUP_FINANCIAL_POLICY_TO_CASH_BRIDGE_REQUIREMENT_V103
existing_axis_strengthened:
  - C31_policy_label_not_enough_without_company_cash_bridge
  - C31_nonlife_reserve_capital_return_policy_positive_escape_hatch
  - C31_reinsurance_policy_low_vol_watch
  - C31_life_insurance_policy_label_stage2_cap
  - C31_bank_capital_return_policy_local_4B
  - C31_low_PBR_bank_label_policy_bonus_cap
existing_axis_weakened: null
```

---

## 9. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Batch this C31 loop with C31 loops 100~102, C21 loop 112, C22 loop 111 and R13 accounting-trust / Stage2 false-positive / high-MAE guardrail files. Extract `C31_VALUEUP_FINANCIAL_POLICY_TO_CASH_BRIDGE_REQUIREMENT_V103` as a shadow-rule candidate. Preserve financial-policy positives only when company-specific CET1, payout, buyback, ROE, reserve, CSM, solvency or capital-return bridge exists; cap low-PBR / Value-up label-only rows.
```

---

## 10. Next research state

```yaml
completed_round: R11
completed_loop: 103
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C18_CONSUMER_EXPORT_CHANNEL_REORDER
  - C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
  - C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
  - C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
  - C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
```
