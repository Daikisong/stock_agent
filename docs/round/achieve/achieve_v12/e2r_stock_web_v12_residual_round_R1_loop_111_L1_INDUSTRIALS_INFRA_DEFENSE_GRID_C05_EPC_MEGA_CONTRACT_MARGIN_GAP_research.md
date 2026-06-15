# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R1
selected_loop: 111
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id: SAUDI_GAS_EPC_CONTRACT_SIZE_TO_MARGIN_CASH_BRIDGE_VS_HEADLINE_SIZE_FAILURE
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

`C05_EPC_MEGA_CONTRACT_MARGIN_GAP` was selected because the index still marks it as below practical calibration depth. Repository registry shows the pair already reached `R1/C05 loop 110`, so this run continues as `loop 111`.

This loop is deliberately narrow: it re-tests Saudi gas EPC awards where the contract headline is undeniably large, but the stock path asks whether the award became margin, working-capital, and cash conversion.

---

## 1. Research thesis

C05 is not “big EPC contract announced.” It is:

```text
signed EPC award
→ scope / procurement / payment terms / execution risk
→ margin and working-capital bridge
→ listed-company equity rerating
```

A mega-contract headline is the bell. The score should care whether the bell is connected to a crankshaft. If not, contract size becomes steam rather than torque.

This loop compares:

1. `028050 삼성E&A`: huge Fadhili award; local positive but only modest MFE and no clean full-window Green.
2. `006360 GS건설`: Fadhili smaller share but clearer delayed equity rerating; reused control from prior C05.
3. `000720 현대건설`: Jafurah/gas-network mega-deal headline but weak equity rerating; reused hard counter/control from prior C05.

The repeated controls are not counted as new independent cases, but they anchor the rule. The new incremental case is Samsung E&A’s direct Fadhili share.

---

## 2. Price source and duplicate validation

```yaml
stock_web_manifest:
  source_name: FinanceData/marcap
  price_adjustment_status: raw_unadjusted_marcap
  calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
  max_date: 2026-02-20
  caveat: Raw/unadjusted OHLC; corporate-action windows blocked by default.
```

```yaml
duplicate_check:
  006360_2024-04-03_Fadhili:
    prior_registry: loop_107
    role_this_loop: reused_positive_control
    new_independent_case_credit: false
  000720_2024-07-01_Jafurah:
    prior_registry: loop_107
    role_this_loop: reused_counter_control
    new_independent_case_credit: false
  028050_2024-04-03_Fadhili:
    prior_registry_visible_top_symbol: true
    exact_tuple_in_visible_registry: not confirmed in fetched snippets
    role_this_loop: incremental_case
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R1","loop":111,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"FADHILI_SAMSUNG_EA_CONTRACT_SIZE_LOCAL_POSITIVE_WITH_MARGIN_CASH_WATCH","symbol":"028050","name":"삼성E&A","trigger_type":"Stage2-Actionable","entry_date":"2024-04-03","entry_close":25300,"price_basis":"tradable_raw","mfe_30d_pct":6.72,"mae_30d_pct":-5.34,"mfe_90d_pct":6.72,"mae_90d_pct":-14.62,"mfe_180d_pct":10.47,"mae_180d_pct":-14.62,"forward_high_30d":27000,"forward_low_30d":23950,"forward_high_90d":27000,"forward_low_90d":21600,"forward_high_180d":27950,"forward_low_180d":21600,"calibration_usable":true,"case_role":"incremental_positive_with_margin_watch","novelty_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|028050|Stage2-Actionable|2024-04-03","non_price_bridge":"Samsung E&A won the major Fadhili package, but equity path stayed modest relative to headline size","score_alignment":"Stage2 may open; Stage3-Green blocked until margin/cash bridge refresh"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R1","loop":111,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"FADHILI_GS_EC_DELAYED_POSITIVE_WITH_4B_WATCH_REUSED_CONTROL","symbol":"006360","name":"GS건설","trigger_type":"Stage2-Actionable","entry_date":"2024-04-03","entry_close":15630,"price_basis":"tradable_raw","mfe_30d_pct":6.97,"mae_30d_pct":-10.17,"mfe_90d_pct":6.97,"mae_90d_pct":-10.17,"mfe_180d_pct":39.16,"mae_180d_pct":-10.17,"forward_high_30d":16720,"forward_low_30d":14040,"forward_high_90d":16720,"forward_low_90d":14040,"forward_high_180d":21750,"forward_low_180d":14040,"calibration_usable":true,"case_role":"reused_positive_control","novelty_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|006360|Stage2-Actionable|2024-04-03","non_price_bridge":"Fadhili EPC award, delayed but meaningful equity response","score_alignment":"keep Stage2-Actionable but use local 4B watch because early MAE was double-digit"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R1","loop":111,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"JAFURAH_HYUNDAI_EC_MEGA_CONTRACT_SIZE_WEAK_RERATING_REUSED_COUNTER","symbol":"000720","name":"현대건설","trigger_type":"Stage2-FalsePositive","entry_date":"2024-07-01","entry_close":33200,"price_basis":"tradable_raw","mfe_30d_pct":5.12,"mae_30d_pct":-4.52,"mfe_90d_pct":5.12,"mae_90d_pct":-12.50,"mfe_180d_pct":5.12,"mae_180d_pct":-27.41,"forward_high_30d":34900,"forward_low_30d":31700,"forward_high_90d":34900,"forward_low_90d":29050,"forward_high_180d":34900,"forward_low_180d":24100,"calibration_usable":true,"case_role":"reused_counter_control","novelty_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|000720|Stage2-FalsePositive|2024-07-01","non_price_bridge":"Jafurah/main gas network headline did not translate into durable equity rerating","score_alignment":"contract size alone should not earn Stage2-Actionable bonus without margin/cash bridge"}
```

---

## 4. Case analysis

### 4.1 Samsung E&A / Fadhili — huge package, modest equity bridge

**Trigger:** Aramco awarded Fadhili expansion EPC contracts in April 2024. Samsung E&A was the primary Korean package winner.

**Price path:**

```yaml
entry_date: 2024-04-03
entry_close: 25300
30d_high: 27000
30d_low: 23950
90d_high: 27000
90d_low: 21600
180d_high: 27950
180d_low: 21600
mfe_30d_pct: 6.72
mae_30d_pct: -5.34
mfe_90d_pct: 6.72
mae_90d_pct: -14.62
mfe_180d_pct: 10.47
mae_180d_pct: -14.62
```

**Interpretation:** This is not a hard false positive. The headline was real, and the local response was real. But compared with the headline size, equity MFE was modest. The case says: C05 may open Stage2, but it should not promote to Green unless the contract is accompanied by margin, procurement-risk, advance-payment, or working-capital confirmation.

---

### 4.2 GS E&C / Fadhili — delayed positive, but reused control

**Trigger:** Same Fadhili EPC award basket.

**Price path:**

```yaml
entry_date: 2024-04-03
entry_close: 15630
30d_high: 16720
30d_low: 14040
90d_high: 16720
90d_low: 14040
180d_high: 21750
180d_low: 14040
mfe_30d_pct: 6.97
mae_30d_pct: -10.17
mfe_90d_pct: 6.97
mae_90d_pct: -10.17
mfe_180d_pct: 39.16
mae_180d_pct: -10.17
```

**Interpretation:** GS E&C is a useful positive-control. It had early drawdown but later repriced. The rule should not block all EPC awards; it should require evidence that the award can pass through the execution-risk pipe. Because this exact tuple appeared in a prior C05 loop, it is reused as a control and not counted as new independent coverage.

---

### 4.3 Hyundai E&C / Jafurah — mega-contract headline, weak rerating

**Trigger:** Aramco announced over USD 25B of Jafurah/main gas network expansion contracts; Hyundai E&C was included through a consortium.

**Price path:**

```yaml
entry_date: 2024-07-01
entry_close: 33200
30d_high: 34900
30d_low: 31700
90d_high: 34900
90d_low: 29050
180d_high: 34900
180d_low: 24100
mfe_30d_pct: 5.12
mae_30d_pct: -4.52
mfe_90d_pct: 5.12
mae_90d_pct: -12.50
mfe_180d_pct: 5.12
mae_180d_pct: -27.41
```

**Interpretation:** This is the counter-control. The project number was large, but the stock path did not convert. That means C05 scoring must distinguish `contract amount in headline` from `listed-company equity bridge`.

---

## 5. Score-return alignment

```yaml
new_independent_case_count: 1
reused_control_case_count: 2
same_archetype_new_trigger_family_count: 1
calibration_usable_case_count: 3
calibration_usable_trigger_count: 3
positive_or_watch_count: 2
counterexample_count: 1
current_profile_error_count: 2
```

| symbol | role | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 028050 | incremental positive with margin watch | +6.72 / -5.34 | +6.72 / -14.62 | +10.47 / -14.62 | huge contract, modest equity bridge |
| 006360 | reused positive-control | +6.97 / -10.17 | +6.97 / -10.17 | +39.16 / -10.17 | delayed positive, but not immediate Green |
| 000720 | reused counter-control | +5.12 / -4.52 | +5.12 / -12.50 | +5.12 / -27.41 | headline size failed to become equity rerating |

---

## 6. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"028050","raw_EPS_revision_bridge":2,"raw_visibility":4,"raw_bottleneck_supply":1,"raw_mispricing":1,"raw_validation":2,"raw_capital_return":0,"raw_info_edge":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Stage2-Actionable-with-margin-cash-watch"}
{"row_type":"score_simulation","symbol":"006360","raw_EPS_revision_bridge":2,"raw_visibility":3,"raw_bottleneck_supply":1,"raw_mispricing":2,"raw_validation":2,"raw_capital_return":0,"raw_info_edge":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2-Actionable-with-4B-watch"}
{"row_type":"score_simulation","symbol":"000720","raw_EPS_revision_bridge":0,"raw_visibility":3,"raw_bottleneck_supply":1,"raw_mispricing":1,"raw_validation":1,"raw_capital_return":0,"raw_info_edge":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2-FalsePositive"}
```

---

## 7. Current calibrated profile stress test

### Existing error risk

C05 can still over-score this pattern:

```text
mega contract amount
+ named Korean EPC contractor
+ overseas energy project
```

That is too broad. A contract is a river entering a mill; the score should ask whether the water reaches the wheel. Procurement, subcontracting, inflation, scope, payment terms, advance payments, FX, and working capital are the sluices.

### Strengthened rule candidate

```text
C05_CONTRACT_SIZE_NEEDS_MARGIN_CASH_BRIDGE

if C05
and signed_EPC_contract_or_award == true
and contract_size_large == true
and company_specific_margin_working_capital_cash_bridge == false:
    stage2_actionable_bonus = min(stage2_actionable_bonus, 1.0)
    block_stage3_green = true
```

### False-positive block

```text
if C05
and MFE_180D_pct < +10
and MAE_180D_pct <= -20
and margin_cash_bridge_refreshed == false:
    route = Stage2_FalsePositive_Block
    stage2_actionable_bonus = 0
```

### Positive escape hatch

```text
if C05
and signed_EPC_contract_or_award == true
and MFE_180D_pct >= +25
and MAE_180D_pct > -15:
    keep_stage2_actionable_bonus = true
    local_4B_watch = true if early_MAE <= -10
```

---

## 8. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: C05_CONTRACT_SIZE_NEEDS_MARGIN_CASH_BRIDGE
existing_axis_strengthened:
  - C05_contract_size_not_enough_without_margin_cash_bridge
  - C05_working_capital_bridge_required_for_stage3_green
  - C05_reused_positive_control_delayed_rerating
  - C05_mega_contract_weak_rerating_false_positive_block
existing_axis_weakened: null
```

---

## 9. Next recommended archetypes

```text
C18_CONSUMER_EXPORT_CHANNEL_REORDER
C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
C05_EPC_MEGA_CONTRACT_MARGIN_GAP_third_party_EPC_controls
```
