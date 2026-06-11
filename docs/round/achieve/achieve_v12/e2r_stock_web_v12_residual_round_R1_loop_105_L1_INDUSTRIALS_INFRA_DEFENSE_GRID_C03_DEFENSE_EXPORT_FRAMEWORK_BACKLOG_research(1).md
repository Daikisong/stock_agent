# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R1
selected_loop: 105
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id: DEFENSE_EXPORT_SIGNED_CONTRACT_BACKLOG_DELIVERY_MARGIN_BRIDGE_VS_FRAMEWORK_LABEL_AND_HIGH_MAE_4B
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

`C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG` remains under practical depth in the no-repeat index: 9 rows / 8 symbols. The visible top-covered symbols are `103140`, `005870`, `042660`, `047810`, `065450`, and `077970`, so this loop uses new C03 visible tuples: `012450`, `064350`, and `079550`.

The registry already has parsed `R1/C03` through loop 104. This run continues as `R1/C03 loop 105`.

---

## 1. Research thesis

C03 is not "defense stock went up." It is the bridge:

```text
signed export contract / executable framework
→ delivery schedule, backlog, localization or support package
→ revenue recognition, margin and cash conversion
→ price path validation
```

This loop separates:

1. **Signed export contract with backlog bridge**  
   Hanwha Aerospace and LIG Nex1 show that signed, named export deals can justify Stage2 when delivery, system scope and backlog bridge are clear.

2. **Direct foreign-government contract with local-production component**  
   Hyundai Rotem is a clean contract bridge, but it still requires delivery timing and local-production margin refresh.

3. **High MFE / high MAE 4B path**  
   Defense names can make strong MFE but later draw down; C03 must prevent Stage3-Green unless backlog-to-margin conversion is refreshed.

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

Symbol caveats:

```yaml
012450:
  name: 한화에어로스페이스
  corporate_action_candidate_dates: [1996-01-03, 1997-01-03, 1999-04-08, 1999-07-06, 2009-02-20]
  relevant_window_after_candidate: true

064350:
  name: 현대로템
  corporate_action_candidate_dates: [2020-08-14]
  relevant_window_after_candidate: true

079550:
  name: LIG넥스원
  corporate_action_candidate_count: 0
  calibration_caveat: clean
```

External contract anchors:

```text
2024-07-09: Hanwha Aerospace won a roughly USD 1B Romania K9 order for 54 K9 howitzers, ammunition, and 36 K10 resupply vehicles, with contract running to July 2029.
2025-08-01: Poland signed a second major Hyundai Rotem K2 contract for 180 tanks, reportedly around USD 6.5B, including local production in Poland.
2024-02 / 2024-09: LIG Nex1 Cheongung-II export chain: Saudi Arabia deal followed by Iraq USD 2.8B deal, confirming export-system status.
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R1","loop":105,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"K9_ROMANIA_SIGNED_CONTRACT_DELIVERY_BACKLOG_MARGIN_BRIDGE_WITH_4B_WATCH","symbol":"012450","name":"한화에어로스페이스","trigger_type":"Stage2-Actionable","entry_date":"2024-07-10","entry_close":256500,"price_basis":"tradable_raw","mfe_30d_pct":28.65,"mae_30d_pct":-3.70,"mfe_90d_pct":42.11,"mae_90d_pct":-3.70,"mfe_180d_pct":65.69,"mae_180d_pct":-3.70,"forward_high_30d":330000,"forward_low_30d":247000,"forward_high_90d":364500,"forward_low_90d":247000,"forward_high_180d":425000,"forward_low_180d":247000,"calibration_usable":true,"case_role":"positive_with_4B_watch","novelty_key":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|012450|Stage2-Actionable|2024-07-10","non_price_bridge":"Romania K9/K10 signed export contract with ammunition/support package and multi-year delivery bridge","score_alignment":"Stage2 opens; Stage3-Green requires delivery-margin and backlog conversion refresh"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R1","loop":105,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"K2_POLAND_SECOND_BATCH_DIRECT_CONTRACT_LOCAL_PRODUCTION_BRIDGE","symbol":"064350","name":"현대로템","trigger_type":"Stage2-Actionable","entry_date":"2025-08-01","entry_close":194000,"price_basis":"tradable_raw","mfe_30d_pct":6.96,"mae_30d_pct":-14.95,"mfe_90d_pct":28.61,"mae_90d_pct":-14.95,"mfe_180d_pct":28.61,"mae_180d_pct":-14.95,"forward_high_30d":207500,"forward_low_30d":165000,"forward_high_90d":249500,"forward_low_90d":165000,"forward_high_180d":249500,"forward_low_180d":165000,"calibration_usable":true,"case_role":"direct_contract_positive_with_local_4B_watch","novelty_key":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|064350|Stage2-Actionable|2025-08-01","non_price_bridge":"Poland K2 second-batch signed contract with local production and service package","score_alignment":"Stage2 opens; early drawdown blocks Green until delivery/local-production margin bridge is refreshed"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R1","loop":105,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"CHEONGUNG_II_MIDDLE_EAST_EXPORT_SYSTEM_BACKLOG_POSITIVE_CONTROL","symbol":"079550","name":"LIG넥스원","trigger_type":"Stage2-Actionable","entry_date":"2024-02-07","entry_close":113400,"price_basis":"tradable_raw","mfe_30d_pct":64.46,"mae_30d_pct":-0.53,"mfe_90d_pct":64.46,"mae_90d_pct":-0.53,"mfe_180d_pct":119.58,"mae_180d_pct":-0.53,"forward_high_30d":186500,"forward_low_30d":112800,"forward_high_90d":186500,"forward_low_90d":112800,"forward_high_180d":249000,"forward_low_180d":112800,"calibration_usable":true,"case_role":"positive_control","novelty_key":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|079550|Stage2-Actionable|2024-02-07","non_price_bridge":"Cheongung-II/M-SAM export system status, Middle East missile-defense backlog chain","score_alignment":"clean positive; export-system bridge and price path both validated"}
```

---

## 4. Case analysis

### 4.1 Hanwha Aerospace / 012450 — signed K9 contract, delivery-margin bridge

Hanwha Aerospace is a strong C03 case because the export was not only a vague framework. The Romania package names platforms, quantities, ammunition and K10 resupply vehicles, with a multi-year contract window. The price path from 2024-07-10 confirms a strong positive response.

```yaml
entry_close: 256500
30d_high: 330000
30d_low: 247000
90d_high: 364500
90d_low: 247000
180d_high: 425000
180d_low: 247000
```

Interpretation:

```text
classification = Stage2-Actionable with 4B watch
```

C03 should keep Stage2 open. However, the contract must still be converted into delivery schedule, production mix, ammunition/support package margin and working-capital path before Stage3-Green.

---

### 4.2 Hyundai Rotem / 064350 — direct K2 contract, but local-production economics matter

Hyundai Rotem is the clean foreign-government signed-contract bridge. The Poland K2 second-batch contract includes local production and support/service elements, making it materially stronger than a framework headline.

```yaml
entry_close: 194000
30d_high: 207500
30d_low: 165000
90d_high: 249500
90d_low: 165000
180d_high: 249500
180d_low: 165000
```

Interpretation:

```text
classification = Stage2-Actionable with local 4B watch
```

The path validates the direct contract, but the initial drawdown prevents Green. The bridge must refresh through delivery timing, local production economics, margin, FX, support package and cash collection.

---

### 4.3 LIG Nex1 / 079550 — export-system positive-control

LIG Nex1 is the cleanest positive-control in this loop. The Cheongung-II/M-SAM export chain is a system-level backlog story: UAE, Saudi Arabia, then Iraq. The price path after the Saudi deal window was extremely strong with shallow drawdown.

```yaml
entry_close: 113400
30d_high: 186500
30d_low: 112800
90d_high: 186500
90d_low: 112800
180d_high: 249000
180d_low: 112800
```

Interpretation:

```text
classification = Stage2-Actionable positive-control
```

This is what C03 should learn: named export system, follow-on country adoption, backlog visibility, and price confirmation.

---

## 5. Score-return alignment

```yaml
new_independent_case_count: 3
new_visible_C03_symbol_count: 3
same_archetype_new_trigger_family_count: 3
calibration_usable_case_count: 3
calibration_usable_trigger_count: 3
positive_case_count: 3
counterexample_or_cap_count: 2
current_profile_error_count: 1
```

| symbol | role | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 012450 | positive + 4B watch | +28.65 / -3.70 | +42.11 / -3.70 | +65.69 / -3.70 | signed package works, but margin/delivery bridge needed |
| 064350 | direct contract + 4B watch | +6.96 / -14.95 | +28.61 / -14.95 | +28.61 / -14.95 | direct contract works, early MAE blocks Green |
| 079550 | positive-control | +64.46 / -0.53 | +64.46 / -0.53 | +119.58 / -0.53 | export-system backlog chain validates C03 |

---

## 6. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"012450","raw_EPS_revision_bridge":3,"raw_visibility":4,"raw_export_backlog":5,"raw_delivery_schedule":4,"raw_margin_bridge":3,"raw_validation":4,"raw_capital_return":0,"raw_info_edge":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2-Actionable-with-4B-watch"}
{"row_type":"score_simulation","symbol":"064350","raw_EPS_revision_bridge":3,"raw_visibility":4,"raw_export_backlog":5,"raw_delivery_schedule":3,"raw_margin_bridge":2,"raw_validation":3,"raw_capital_return":0,"raw_info_edge":3,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2-Actionable-local-4B-watch"}
{"row_type":"score_simulation","symbol":"079550","raw_EPS_revision_bridge":4,"raw_visibility":4,"raw_export_backlog":5,"raw_delivery_schedule":4,"raw_margin_bridge":4,"raw_validation":5,"raw_capital_return":0,"raw_info_edge":3,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2-Actionable-positive-control"}
```

---

## 7. Current calibrated profile stress test

### Existing error risk

C03 can over-reward:

```text
defense label
+ geopolitical tension
+ export framework / MOU
```

That is too broad. A defense export thesis is a convoy: contract signing is the lead vehicle, but revenue and margin arrive only if delivery, support, ammunition, localization, FX and working capital all follow. A framework without these vehicles is only a flag on the road.

### Rule candidate

```text
C03_SIGNED_CONTRACT_DELIVERY_BACKLOG_REQUIREMENT

if C03
and defense_export_label_or_framework == true
and signed_contract_quantity_delivery_schedule_or_backlog_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C03
and signed_foreign_government_contract == true
and MFE_90D_pct >= +20:
    keep_stage2_actionable_bonus = true
```

```text
if C03
and MFE_30D_pct >= +20
and MAE_90D_pct <= -10
and delivery_margin_cash_bridge_refreshed == false:
    local_4B_watch = true
    block_stage3_green = true
```

```text
if C03
and dominant_driver_is_system_export_adoption_chain == true
and follow_on_country_order == true:
    allow_positive_control_credit = true
```

---

## 8. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: C03_SIGNED_CONTRACT_DELIVERY_BACKLOG_REQUIREMENT
existing_axis_strengthened:
  - C03_signed_contract_not_MOU_requirement
  - C03_delivery_schedule_margin_cash_bridge_required_for_Green
  - C03_direct_foreign_government_contract_escape_hatch
  - C03_follow_on_export_system_adoption_positive_control
existing_axis_weakened: null
```

---

## 9. Next recommended archetypes

```text
C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_retest_with_digital_financial_and_brokerage_counterexamples
C22_INSURANCE_RATE_CYCLE_RESERVE_retest_with_healthcare_underwriting_controls
R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
C31_POLICY_SUBSIDY_LEGISLATION_EVENT_retest_with_valueup_and_energy_policy_controls
C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
```
