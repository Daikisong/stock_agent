# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R1
selected_loop: 114
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id: EPC_CONSTRUCTION_ORDER_REBOUND_VS_MARGIN_WORKING_CAPITAL_AND_PF_RISK_GAP
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
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

`C05_EPC_MEGA_CONTRACT_MARGIN_GAP` is still a Priority 0 archetype in the no-repeat index: 13 representative rows, still 17 rows short of the 30-row minimum. The visible top-covered symbols include `000720`, `028050`, and `047040`, so this loop uses construction/EPC rows from the current stock-web-derived session as boundary evidence and marks reused/top-covered symbols explicitly.

This run is not a construction-PF balance-sheet study. It uses construction/PF-adjacent rows only to test the C05 question:

```text
Does an order / project / EPC / construction rebound actually become margin, working-capital, cash-collection and earnings bridge?
```

Direct uncached stock-web shard fetch has been unstable in recent turns, so this MD reuses stock-web-derived rows already calculated in the current v12 session. No production scoring is changed.

---

## 1. Research thesis

C05 is not `large project headline = earnings upside`.

It is the gap between a project headline and profit:

```text
EPC / mega project / construction order / sector rebound
→ contract terms, cost escalation, execution risk, working capital, cash collection, margin
→ price path validation
```

The core failure mode is that the market sees the contract value, but the company later eats the cost overrun, delayed receivable, FX loss, warranty burden, or PF-linked balance-sheet drag. Revenue is the top of the bridge; margin and cash are the load-bearing beams.

This loop splits four routes:

1. **Delayed construction/EPC rebound with shallow MAE**
   - Price path can validate a tradable rebound.
   - But C05 contribution should be capped unless the margin/cash bridge is issuer-specific.

2. **Sector beta or PF support masquerading as EPC order quality**
   - A strong move may be real, but not necessarily C05.
   - If housing/PF beta dominates, reclassification or contribution cap is required.

3. **Quality balance-sheet label without project margin bridge**
   - Higher-quality builder label alone should not open Stage2-Actionable.

4. **Large-builder / support-label false positive**
   - Low MFE and deep full-window MAE show that project/sector label failed.

---

## 2. Source validation

```yaml
stock_web_manifest:
  source_name: FinanceData/marcap
  price_adjustment_status: raw_unadjusted_marcap
  max_date: 2026-02-20
  calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
  caveat: Raw/unadjusted OHLC; corporate-action contaminated windows blocked by default.
```

Local stock-web-derived row provenance:

```yaml
reused_price_rows_from_current_session:
  - e2r_stock_web_v12_residual_round_R10_loop_1_L9_CONSTRUCTION_REAL_ESTATE_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
  - e2r_stock_web_v12_residual_round_R10_loop_2_L9_CONSTRUCTION_REAL_ESTATE_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
  - e2r_stock_web_v12_residual_round_R13_loop_5_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md
reason:
  - rows were calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - this file converts construction/PF-adjacent rows into a C05 EPC-margin bridge test
  - exact trigger rows should be deduped if already represented in C30/R13 outputs
  - no production scoring changed
```

Symbol caveats:

```yaml
294870:
  name: HDC현대산업개발
  role: delayed construction/project rebound; C05 contribution cap because housing/PF beta dominates
  calibration_usable: true

047040:
  name: 대우건설
  role: construction/EPC rebound boundary control
  calibration_usable: true
  no_repeat_note: visible top-covered C05 symbol, use as control if deduped

375500:
  name: DL이앤씨
  role: quality label / margin bridge cap
  calibration_usable: true

000720:
  name: 현대건설
  role: large-builder label false-positive block
  calibration_usable: true
  no_repeat_note: visible top-covered C05 symbol, use as hard control if deduped

004960:
  name: 한신공영
  role: small/mid-builder support beta with modest MFE and contribution cap
  calibration_usable: true
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R1","loop":114,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"DELAYED_CONSTRUCTION_PROJECT_REBOUND_WITH_MARGIN_CASH_BRIDGE_REQUIRED","symbol":"294870","name":"HDC현대산업개발","trigger_type":"Stage2-Watch","entry_date":"2024-05-13","entry_close":17920,"price_basis":"tradable_raw","mfe_30d_pct":2.12,"mae_30d_pct":-6.58,"mfe_90d_pct":37.28,"mae_90d_pct":-6.58,"mfe_180d_pct":57.37,"mae_180d_pct":-6.58,"forward_high_30d":18300,"forward_low_30d":16740,"forward_high_90d":24600,"forward_low_90d":16740,"forward_high_180d":28200,"forward_low_180d":16740,"calibration_usable":true,"case_role":"delayed_positive_with_margin_bridge_requirement","novelty_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|294870|Stage2-Watch|2024-05-13","non_price_bridge":"delayed construction/project rebound; not enough direct EPC margin/cash bridge at entry","score_alignment":"allow delayed local 4B; block Stage2-Actionable until project margin, receivable, cost and cash bridge refresh"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R1","loop":114,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"CONSTRUCTION_EPC_SECTOR_REBOUND_WITH_C05_CONTRIBUTION_CAP","symbol":"047040","name":"대우건설","trigger_type":"Stage2-Watch","entry_date":"2024-05-13","entry_close":3775,"price_basis":"tradable_raw","mfe_30d_pct":1.72,"mae_30d_pct":-4.64,"mfe_90d_pct":31.52,"mae_90d_pct":-6.09,"mfe_180d_pct":31.52,"mae_180d_pct":-6.75,"forward_high_30d":3840,"forward_low_30d":3600,"forward_high_90d":4965,"forward_low_90d":3545,"forward_high_180d":4965,"forward_low_180d":3520,"calibration_usable":true,"case_role":"positive_boundary_control","novelty_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|047040|Stage2-Watch|2024-05-13","non_price_bridge":"construction/EPC sector rebound; issuer-specific margin and working-capital bridge not isolated","score_alignment":"cap C05 contribution; use as Stage2-Watch until backlog margin and cash conversion confirm","aggregate_credit_note":"047040 is visible top-covered for C05; dedupe or control-only if already represented"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R1","loop":114,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"BALANCE_SHEET_QUALITY_LABEL_WITHOUT_PROJECT_MARGIN_CASH_BRIDGE_STAGE2_CAP","symbol":"375500","name":"DL이앤씨","trigger_type":"Stage2-Watch","entry_date":"2024-05-13","entry_close":34650,"price_basis":"tradable_raw","mfe_30d_pct":3.90,"mae_30d_pct":-4.04,"mfe_90d_pct":14.00,"mae_90d_pct":-17.46,"mfe_180d_pct":14.00,"mae_180d_pct":-17.46,"forward_high_30d":36000,"forward_low_30d":33250,"forward_high_90d":39500,"forward_low_90d":28600,"forward_high_180d":39500,"forward_low_180d":28600,"calibration_usable":true,"case_role":"quality_label_cap","novelty_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|375500|Stage2-Watch|2024-05-13","non_price_bridge":"better quality/balance-sheet label without fresh project margin or cash-collection proof","score_alignment":"cap Stage2-Actionable; require EPC margin/cost/receivable bridge before upgrade"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R1","loop":114,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"LARGE_BUILDER_SUPPORT_LABEL_LOW_MFE_HIGH_MAE_STAGE2_BLOCK","symbol":"000720","name":"현대건설","trigger_type":"Stage2-FalsePositive","entry_date":"2024-03-27","entry_close":33250,"price_basis":"tradable_raw","mfe_30d_pct":4.81,"mae_30d_pct":-6.17,"mfe_90d_pct":8.27,"mae_90d_pct":-6.17,"mfe_180d_pct":8.27,"mae_180d_pct":-27.52,"forward_high_30d":34850,"forward_low_30d":31200,"forward_high_90d":36000,"forward_low_90d":31200,"forward_high_180d":36000,"forward_low_180d":24100,"calibration_usable":true,"case_role":"hard_counterexample","novelty_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|000720|Stage2-FalsePositive|2024-03-27","non_price_bridge":"large-builder support/project label without project margin, cost or cash bridge; full-window drawdown invalidates Stage2","score_alignment":"block Stage2-Actionable unless new issuer-specific contract margin/cash evidence appears","aggregate_credit_note":"000720 is visible top-covered for C05; dedupe or control-only if already represented"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R1","loop":114,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"SMALL_BUILDER_SUPPORT_BETA_MODEST_MFE_C05_CONTRIBUTION_CAP","symbol":"004960","name":"한신공영","trigger_type":"Stage2-Watch","entry_date":"2024-03-27","entry_close":6720,"price_basis":"tradable_raw","mfe_30d_pct":8.48,"mae_30d_pct":-8.33,"mfe_90d_pct":8.48,"mae_90d_pct":-8.33,"mfe_180d_pct":18.60,"mae_180d_pct":-8.63,"forward_high_30d":7290,"forward_low_30d":6160,"forward_high_90d":7290,"forward_low_90d":6160,"forward_high_180d":7970,"forward_low_180d":6140,"calibration_usable":true,"case_role":"modest_rebound_contribution_cap","novelty_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|004960|Stage2-Watch|2024-03-27","non_price_bridge":"small/mid-builder support beta without clear EPC contract margin or working-capital bridge","score_alignment":"Stage2-Watch only; require contract margin, receivable and cash conversion proof"}
```

---

## 4. Case analysis

### 4.1 HDC Hyundai Development / 294870 — delayed positive, not immediate C05 Actionable

HDC had a powerful delayed move, but the selected trigger does not isolate a direct EPC margin bridge.

```yaml
entry_close: 17920
30d_MFE_MAE: +2.12 / -6.58
90d_MFE_MAE: +37.28 / -6.58
180d_MFE_MAE: +57.37 / -6.58
route: delayed local 4B
```

The route should not backfill the later move as immediate C05 Stage2-Actionable. C05 needs project margin, receivables, cost-to-complete, and cash collection evidence.

---

### 4.2 Daewoo E&C / 047040 — tradable rebound, contribution capped

Daewoo E&C produced a strong 90D/180D move, but the bridge is not cleanly EPC margin.

```yaml
entry_close: 3775
30d_MFE_MAE: +1.72 / -4.64
90d_MFE_MAE: +31.52 / -6.09
180d_MFE_MAE: +31.52 / -6.75
route: Stage2-Watch / contribution cap
```

This is a good price path, but not enough to claim C05 unless backlog margin and working capital are proven.

---

### 4.3 DL E&C / 375500 — quality label cap

DL E&C illustrates that a better perceived balance sheet is not the same as project margin recovery.

```yaml
entry_close: 34650
30d_MFE_MAE: +3.90 / -4.04
90d_MFE_MAE: +14.00 / -17.46
180d_MFE_MAE: +14.00 / -17.46
route: Stage2 cap
```

Without fresh margin/cash evidence, Stage2-Actionable stays blocked.

---

### 4.4 Hyundai E&C / 000720 — large-builder false positive

Hyundai E&C is the clean hard counterexample.

```yaml
entry_close: 33250
30d_MFE_MAE: +4.81 / -6.17
90d_MFE_MAE: +8.27 / -6.17
180d_MFE_MAE: +8.27 / -27.52
route: Stage2-FalsePositive
```

A large-builder label and support headline do not solve C05’s question. The company must prove margin and cash.

---

### 4.5 Hanshin Engineering / 004960 — modest rebound, not enough C05 bridge

Hanshin had a modest recovery, but not enough to open C05 Actionable.

```yaml
entry_close: 6720
30d_MFE_MAE: +8.48 / -8.33
90d_MFE_MAE: +8.48 / -8.33
180d_MFE_MAE: +18.60 / -8.63
route: Stage2-Watch
```

---

## 5. Score-return alignment

```yaml
new_independent_case_count: 3
reused_control_case_count: 2
calibration_usable_case_count: 5
calibration_usable_trigger_count: 5
positive_or_delayed_positive_count: 2
counterexample_or_cap_count: 4
local_4B_or_contribution_cap_count: 4
current_profile_error_count: 4
```

| symbol | role | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 294870 | delayed 4B | +2.12 / -6.58 | +37.28 / -6.58 | +57.37 / -6.58 | later rebound needs margin/cash bridge |
| 047040 | positive boundary cap | +1.72 / -4.64 | +31.52 / -6.09 | +31.52 / -6.75 | price works, C05 attribution capped |
| 375500 | quality label cap | +3.90 / -4.04 | +14.00 / -17.46 | +14.00 / -17.46 | balance-sheet label not project margin |
| 000720 | hard counterexample | +4.81 / -6.17 | +8.27 / -6.17 | +8.27 / -27.52 | large-builder support label failed |
| 004960 | modest watch | +8.48 / -8.33 | +8.48 / -8.33 | +18.60 / -8.63 | support beta needs contract/cash proof |

---

## 6. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"294870","raw_contract_visibility":2,"raw_margin_bridge":1,"raw_cost_overrun_control":1,"raw_working_capital_cash_bridge":1,"raw_validation":2,"raw_reclassification_risk":3,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"DelayedLocal4B"}
{"row_type":"score_simulation","symbol":"047040","raw_contract_visibility":3,"raw_margin_bridge":1,"raw_cost_overrun_control":1,"raw_working_capital_cash_bridge":1,"raw_validation":2,"raw_reclassification_risk":3,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Stage2Watch_C05ContributionCap"}
{"row_type":"score_simulation","symbol":"375500","raw_contract_visibility":2,"raw_margin_bridge":1,"raw_cost_overrun_control":1,"raw_working_capital_cash_bridge":1,"raw_validation":1,"raw_reclassification_risk":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2Cap_QualityLabel"}
{"row_type":"score_simulation","symbol":"000720","raw_contract_visibility":1,"raw_margin_bridge":0,"raw_cost_overrun_control":0,"raw_working_capital_cash_bridge":1,"raw_validation":0,"raw_reclassification_risk":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2FalsePositiveBlock"}
{"row_type":"score_simulation","symbol":"004960","raw_contract_visibility":1,"raw_margin_bridge":1,"raw_cost_overrun_control":1,"raw_working_capital_cash_bridge":1,"raw_validation":1,"raw_reclassification_risk":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2Watch_ModestBeta"}
```

---

## 7. Current calibrated profile stress test

### Existing error risk

C05 can over-credit:

```text
large construction/EPC name
+ project or support headline
+ delayed price rebound
```

The correct test is not order size. It is margin and cash.

A mega contract is a huge pipe. C05 asks whether the pipe leaks through cost overrun, receivables, working capital, warranty, PF drag, and margin squeeze.

### Rule candidate

```text
C05_EPC_MARGIN_WORKING_CAPITAL_BRIDGE_REQUIREMENT_V114

if C05
and EPC_contract_project_or_builder_label == true
and project_margin_cost_control_receivable_or_cash_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C05
and MFE_30D_pct < +5
and MFE_90D_pct >= +25
and margin_cash_bridge_refreshed_later == true:
    route = delayed_local_4B
    do_not_backfill_as_immediate_Stage2_Actionable = true
```

```text
if C05
and construction_sector_beta_or_PF_support_dominates == true:
    cap_C05_contribution = true
    require_reclassification_to_C30_if_balance_sheet_bridge_dominates = true
```

```text
if C05
and MFE_90D_pct < +10
and MAE_180D_pct <= -25
and project_margin_cash_bridge == false:
    route = Stage2_FalsePositive_Block
```

---

## 8. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: C05_EPC_MARGIN_WORKING_CAPITAL_BRIDGE_REQUIREMENT_V114
existing_axis_strengthened:
  - C05_project_or_builder_label_not_enough_without_margin_cash_bridge
  - C05_delayed_rebound_local_4B_not_immediate_actionable
  - C05_construction_PF_beta_reclassification_cap
  - C05_large_builder_low_MFE_high_MAE_stage2_block
existing_axis_weakened: null
```

---

## 9. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Batch this C05 loop with earlier C05 rows, C30 PF/balance-sheet files, and R13 high-MAE/accounting-trust guardrail files. Extract `C05_EPC_MARGIN_WORKING_CAPITAL_BRIDGE_REQUIREMENT_V114` as a shadow-rule candidate. Preserve contract-margin/cash positive controls, but block builder/project labels without cost-control, receivable, working-capital, margin or cash evidence. Reclassify PF/balance-sheet dominated rows to C30 when appropriate.
```

---

## 10. Next research state

```yaml
completed_round: R1
completed_loop: 114
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C24_BIO_TRIAL_DATA_EVENT_RISK
  - C31_POLICY_SUBSIDY_LEGISLATION_EVENT_retest_with_battery_and_grid_policy_controls
  - R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
  - C18_CONSUMER_EXPORT_CHANNEL_REORDER
  - C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
```
