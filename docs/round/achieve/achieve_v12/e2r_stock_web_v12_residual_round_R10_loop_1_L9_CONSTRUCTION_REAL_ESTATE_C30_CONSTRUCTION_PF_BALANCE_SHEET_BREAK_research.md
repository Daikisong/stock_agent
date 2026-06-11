# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R10
selected_loop: 1
large_sector_id: L9_CONSTRUCTION_REAL_ESTATE
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: PF_RESTRUCTURING_SOFT_LANDING_AND_CONSTRUCTION_BALANCE_SHEET_RERATING_VS_LABEL_ONLY_REBOUND
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

`C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK` is one of the thinnest visible areas in the no-repeat index: 3 rows / 3 symbols. The visible covered names are `009410`, `034300`, and `183190`, so this loop avoids those and uses new C30 tuples:

- `294870 HDC현대산업개발`
- `047040 대우건설`
- `375500 DL이앤씨`

No parsed C30 loop file was found in the fetched registry/search snippets, so this run starts the local C30 continuation as `loop 1`.

---

## 1. Research thesis

C30 is not “construction sector is bad.” It is the specific balance-sheet bridge:

```text
PF / real-estate project-financing stress
→ maturity extension, guarantee roll, liquidity support, or restructuring
→ survival / dilution / debt service / margin hit
→ price path validation
```

A construction stock can rise for a sector beta rebound, government support, housing sentiment, or short covering. C30 should only reward the part that is tied to balance-sheet risk being actually defused.

This loop separates:

1. **Delayed PF soft-landing / housing rebound path** — HDC현대산업개발 shows low immediate MFE after FSS/FSC support headlines, but a delayed 90D/180D rerating when construction/housing risk perception improved.
2. **Tradable sector rebound, not a clean balance-sheet repair** — 대우건설 shows a strong summer move, but the bridge is not pure PF resolution.
3. **Balance-sheet quality label with margin/PF caution** — DL이앤씨 has quality/balance-sheet appeal, but price path says the label alone is not enough for Green.

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
294870:
  name: HDC현대산업개발
  corporate_action_candidate_dates: [2020-03-26]
  relevant_window_after_candidate: true

047040:
  name: 대우건설
  corporate_action_candidate_dates: [2001-07-13, 2003-11-18, 2011-01-18]
  relevant_window_after_candidate: true

375500:
  name: DL이앤씨
  corporate_action_candidate_dates: [2022-04-08, 2022-04-28]
  relevant_window_after_candidate: true
```

External macro anchor:

```text
2024-03-27: Korean authorities announced financial support for small businesses and builders, including guarantees, loans, and market-stabilization support for profitable real-estate projects.
2024-05-13: FSS announced tougher and broader real-estate PF project assessments to accelerate restructuring, after delinquency rates had risen.
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R10","loop":1,"large_sector_id":"L9_CONSTRUCTION_REAL_ESTATE","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"HDC_DELAYED_PF_SOFT_LANDING_AND_HOUSING_REBOUND_WITH_4B_WATCH","symbol":"294870","name":"HDC현대산업개발","trigger_type":"Stage2-Watch","entry_date":"2024-05-13","entry_close":17920,"price_basis":"tradable_raw","mfe_30d_pct":2.12,"mae_30d_pct":-6.58,"mfe_90d_pct":37.28,"mae_90d_pct":-6.58,"mfe_180d_pct":57.37,"mae_180d_pct":-6.58,"forward_high_30d":18300,"forward_low_30d":16740,"forward_high_90d":24600,"forward_low_90d":16740,"forward_high_180d":28200,"forward_low_180d":16740,"calibration_usable":true,"case_role":"delayed_positive_with_4B_watch","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|294870|Stage2-Watch|2024-05-13","non_price_bridge":"PF restructuring/sector soft-landing plus housing sentiment rebound, but not an immediate balance-sheet repair proof","score_alignment":"do not grant immediate Stage2-Actionable; allow delayed local 4B watch if liquidity/refinancing bridge is refreshed"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R10","loop":1,"large_sector_id":"L9_CONSTRUCTION_REAL_ESTATE","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"DAEWOO_EC_SECTOR_REBOUND_WITHOUT_PURE_PF_BALANCE_SHEET_BREAK_RESOLUTION","symbol":"047040","name":"대우건설","trigger_type":"Stage2-Watch","entry_date":"2024-05-13","entry_close":3775,"price_basis":"tradable_raw","mfe_30d_pct":1.72,"mae_30d_pct":-4.64,"mfe_90d_pct":31.52,"mae_90d_pct":-6.09,"mfe_180d_pct":31.52,"mae_180d_pct":-6.75,"forward_high_30d":3840,"forward_low_30d":3600,"forward_high_90d":4965,"forward_low_90d":3545,"forward_high_180d":4965,"forward_low_180d":3520,"calibration_usable":true,"case_role":"tradable_rebound_with_contribution_cap","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|047040|Stage2-Watch|2024-05-13","non_price_bridge":"construction-sector rebound after PF restructuring scrutiny, but no isolated listed-company PF balance-sheet repair bridge in price trigger","score_alignment":"keep as Stage2-Watch; cap C30 contribution unless PF exposure, debt rollover, or cash-flow bridge is explicit"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R10","loop":1,"large_sector_id":"L9_CONSTRUCTION_REAL_ESTATE","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"DL_EC_BALANCE_SHEET_QUALITY_LABEL_WITH_MARGIN_PF_HEADWIND_STAGE2_CAP","symbol":"375500","name":"DL이앤씨","trigger_type":"Stage2-Watch","entry_date":"2024-05-13","entry_close":34650,"price_basis":"tradable_raw","mfe_30d_pct":3.90,"mae_30d_pct":-4.04,"mfe_90d_pct":14.00,"mae_90d_pct":-17.46,"mfe_180d_pct":14.00,"mae_180d_pct":-17.46,"forward_high_30d":36000,"forward_low_30d":33250,"forward_high_90d":39500,"forward_low_90d":28600,"forward_high_180d":39500,"forward_low_180d":28600,"calibration_usable":true,"case_role":"quality_label_counterexample_or_watch","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|375500|Stage2-Watch|2024-05-13","non_price_bridge":"balance-sheet quality label, but margin/PF/housing cycle risk not fully cleared by trigger","score_alignment":"cap Stage2-Actionable; require explicit PF risk reduction or margin/cash conversion bridge"}
```

---

## 4. Case analysis

### 4.1 HDC Hyundai Development / 294870 — delayed positive, not immediate Green

HDC is the best delayed-positive case in this loop. From the 2024-05-13 PF restructuring assessment anchor, the stock did not immediately re-rate in 30D. It later moved strongly in July–August.

```yaml
entry_close: 17920
30d_high: 18300
30d_low: 16740
90d_high: 24600
90d_low: 16740
180d_high: 28200
180d_low: 16740
mfe_30d_pct: 2.12
mae_30d_pct: -6.58
mfe_90d_pct: 37.28
mae_90d_pct: -6.58
mfe_180d_pct: 57.37
mae_180d_pct: -6.58
```

Interpretation:

```text
classification = Stage2-Watch / delayed-positive with local 4B watch
```

The model should not score the May 13 PF assessment as immediate Actionable. It should route HDC to 4B watch until a better liquidity, refinancing, presale, or housing-cycle bridge appears. Once the price confirms and balance-sheet concerns ease, delayed contribution is allowed, but it should not be backfilled as an instant C30 success.

---

### 4.2 Daewoo E&C / 047040 — tradable rebound with C30 contribution cap

Daewoo E&C produced a tradable move from the same 2024-05-13 anchor, especially around July. But the move is not cleanly attributable to PF balance-sheet repair.

```yaml
entry_close: 3775
30d_high: 3840
30d_low: 3600
90d_high: 4965
90d_low: 3545
180d_high: 4965
180d_low: 3520
mfe_30d_pct: 1.72
mae_30d_pct: -4.64
mfe_90d_pct: 31.52
mae_90d_pct: -6.09
mfe_180d_pct: 31.52
mae_180d_pct: -6.75
```

Interpretation:

```text
classification = Stage2-Watch / tradable rebound with contribution cap
```

This is a good price case, but not automatically a C30 balance-sheet repair case. The rule should require issuer-specific PF exposure reduction, refinancing confirmation, cash-flow improvement, or debt-service relief before awarding full C30 Stage2-Actionable credit.

---

### 4.3 DL E&C / 375500 — balance-sheet quality label is not enough

DL E&C is the counter/control case. It has a stronger quality/balance-sheet perception than stressed mid-sized builders, but the selected PF restructuring trigger does not create a durable rerating.

```yaml
entry_close: 34650
30d_high: 36000
30d_low: 33250
90d_high: 39500
90d_low: 28600
180d_high: 39500
180d_low: 28600
mfe_30d_pct: 3.90
mae_30d_pct: -4.04
mfe_90d_pct: 14.00
mae_90d_pct: -17.46
mfe_180d_pct: 14.00
mae_180d_pct: -17.46
```

Interpretation:

```text
classification = Stage2-Watch / quality-label cap
```

A better balance sheet is necessary, but not sufficient. C30 must see risk transfer into actual credit access, lower guarantee risk, margin stabilization, cash conversion, or valuation repair.

---

## 5. Score-return alignment

```yaml
new_independent_case_count: 3
new_visible_C30_symbol_count: 3
same_archetype_new_trigger_family_count: 3
calibration_usable_case_count: 3
calibration_usable_trigger_count: 3
positive_or_delayed_positive_count: 2
counterexample_or_cap_count: 2
current_profile_error_count: 2
```

| symbol | role | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 294870 | delayed positive / 4B watch | +2.12 / -6.58 | +37.28 / -6.58 | +57.37 / -6.58 | delayed housing/PF soft-landing path, not immediate Actionable |
| 047040 | tradable rebound / contribution cap | +1.72 / -4.64 | +31.52 / -6.09 | +31.52 / -6.75 | price works, but C30 attribution needs issuer-specific bridge |
| 375500 | quality-label cap | +3.90 / -4.04 | +14.00 / -17.46 | +14.00 / -17.46 | balance-sheet label alone is not enough |

---

## 6. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"294870","raw_EPS_revision_bridge":1,"raw_visibility":3,"raw_PF_refinancing_bridge":2,"raw_balance_sheet_relief":2,"raw_cash_conversion":1,"raw_validation":2,"raw_info_edge":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Stage2-Watch-delayed-positive-local-4B"}
{"row_type":"score_simulation","symbol":"047040","raw_EPS_revision_bridge":1,"raw_visibility":3,"raw_PF_refinancing_bridge":1,"raw_balance_sheet_relief":1,"raw_cash_conversion":1,"raw_validation":2,"raw_info_edge":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Stage2-Watch-contribution-cap"}
{"row_type":"score_simulation","symbol":"375500","raw_EPS_revision_bridge":1,"raw_visibility":3,"raw_PF_refinancing_bridge":1,"raw_balance_sheet_relief":2,"raw_cash_conversion":1,"raw_validation":1,"raw_info_edge":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2-Watch-quality-label-cap"}
```

---

## 7. Current calibrated profile stress test

### Existing error risk

C30 can over-reward two things:

```text
construction sector rebound
+ PF support headline
```

and:

```text
large builder / quality balance-sheet label
```

Both can be incomplete. A PF crisis is not solved by the word "support." It is solved when maturities roll, guarantees stop leaking, bad projects are restructured, and cash can pass through the balance sheet without breaking the pipes.

### Rule candidate

```text
C30_PF_BALANCE_SHEET_BRIDGE_REQUIREMENT

if C30
and construction_PF_support_or_restructuring_headline == true
and issuer_specific_refinancing_liquidity_or_debt_service_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C30
and MFE_30D_pct < +5
and MFE_90D_pct >= +25
and issuer_specific_PF_bridge_refreshed == true:
    route = delayed_local_4B_positive
    do_not_backfill_as_immediate_Stage2_Actionable = true
```

```text
if C30
and construction_sector_beta_rebound == true
and PF_exposure_reduction_or_cash_conversion_bridge == false:
    cap_C30_contribution = true
    require_cross_archetype_reclassification_if_housing_beta_dominates = true
```

```text
if C30
and balance_sheet_quality_label == true
and margin_cash_or_PF_refinancing_bridge == false
and MFE_90D_pct < +15:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

---

## 8. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: C30_PF_BALANCE_SHEET_BRIDGE_REQUIREMENT
existing_axis_strengthened:
  - C30_PF_support_headline_not_enough_without_issuer_specific_bridge
  - C30_delayed_4B_positive_after_refinancing_liquidity_refresh
  - C30_construction_sector_beta_contribution_cap
  - C30_balance_sheet_quality_label_stage2_cap
existing_axis_weakened: null
```

---

## 9. Next recommended archetypes

```text
R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
C22_INSURANCE_RATE_CYCLE_RESERVE
C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_retest_with_direct_workout_controls
C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
```
