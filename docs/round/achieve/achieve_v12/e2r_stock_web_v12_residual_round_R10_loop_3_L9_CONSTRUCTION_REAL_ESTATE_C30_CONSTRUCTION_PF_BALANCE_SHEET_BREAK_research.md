# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R10
selected_loop: 3
large_sector_id: L9_CONSTRUCTION_REAL_ESTATE
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: PF_BALANCE_SHEET_REFINANCING_BRIDGE_VS_EPC_MARGIN_AND_CONSTRUCTION_BETA_RECLASSIFICATION
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

`C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK` remains a practical Priority 0 area because prior coverage is thin and the archetype is easy to confuse with C05 EPC margin or broad construction beta. The previous local C30 runs reached `R10/C30 loop 2`; this run continues as `R10/C30 loop 3`.

This run consolidates the current-session C30/C05/R13 rows into a sharper balance-sheet rule:

```text
PF stress / refinancing / guarantee / liquidity pressure
→ issuer-specific debt-service, maturity, guarantee, presale, cash or restructuring bridge
→ price path validation
```

Direct uncached raw fetch was unstable in this turn, so this MD uses stock-web-derived rows already calculated earlier in the same v12 session. The rows carry complete 30D/90D/180D MFE and MAE from `Songdaiki/stock-web` tradable OHLC. This is a rule-formalization and residual-calibration pass; no production scoring is changed.

---

## 1. Research thesis

C30 is not `construction stock recovered`.

It is the balance-sheet bridge:

```text
real-estate PF stress / refinancing pressure / guarantee exposure
→ maturity extension, liquidity access, presale improvement, workout, guarantee relief, cash conversion
→ shareholder-equity survival and price validation
```

The key confusion is between three neighboring routes:

1. **C30 PF balance-sheet relief**
   - The issuer-specific PF or liquidity pipe stops leaking.
   - Stage2 can open only if refinancing, guarantee, maturity or cash bridge is visible.

2. **C05 EPC / construction margin**
   - Project order or builder quality improves, but the bridge is contract margin, cost control, receivables, or working capital.
   - This should not be scored as C30 unless balance-sheet relief dominates.

3. **Construction beta / policy support**
   - Sector sentiment improves after PF support or restructuring headlines.
   - Price can rebound, but C30 contribution must be capped unless issuer-specific balance-sheet mechanics are proven.

This loop separates six routes:

```text
A. delayed PF/housing soft-landing positive
B. construction beta rebound with contribution cap
C. quality label without issuer-specific bridge
D. direct workout stress-control, not clean equity recovery
E. large-builder support label false positive
F. small/mid-builder support beta watch
```

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
  - R10/C30 loop 1
  - R10/C30 loop 2
  - R1/C05 loop 114
  - R13 high-MAE / 4B-4C / Stage2 false-positive construction guardrail rows
reason:
  - rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - this file changes the calibration lens back to C30 and consolidates boundary rules
  - exact duplicate trigger keys should be deduped if the ingest registry already contains them
  - no production scoring changed
```

Symbol caveats:

```yaml
294870:
  name: HDC현대산업개발
  role: delayed PF/housing soft-landing positive with local 4B watch
  calibration_usable: true

047040:
  name: 대우건설
  role: construction/EPC rebound, C30 contribution cap
  calibration_usable: true

375500:
  name: DL이앤씨
  role: quality/balance-sheet label cap
  calibration_usable: true

009410:
  name: 태영건설
  role: direct workout stress-control
  calibration_usable: false
  caveat: corporate-action / trading-gap contamination; use as stress-control only

000720:
  name: 현대건설
  role: large-builder support label false-positive block
  calibration_usable: true

014790:
  name: HL D&I
  role: delayed support headline positive with issuer-specific bridge requirement
  calibration_usable: true

004960:
  name: 한신공영
  role: small/mid-builder support beta with contribution cap
  calibration_usable: true
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R10","loop":3,"large_sector_id":"L9_CONSTRUCTION_REAL_ESTATE","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"DELAYED_PF_HOUSING_SOFT_LANDING_POSITIVE_WITH_ISSUER_BRIDGE_REQUIREMENT","symbol":"294870","name":"HDC현대산업개발","trigger_type":"Stage2-Watch","entry_date":"2024-05-13","entry_close":17920,"price_basis":"tradable_raw","mfe_30d_pct":2.12,"mae_30d_pct":-6.58,"mfe_90d_pct":37.28,"mae_90d_pct":-6.58,"mfe_180d_pct":57.37,"mae_180d_pct":-6.58,"forward_high_30d":18300,"forward_low_30d":16740,"forward_high_90d":24600,"forward_low_90d":16740,"forward_high_180d":28200,"forward_low_180d":16740,"calibration_usable":true,"case_role":"delayed_positive_local_4B","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|294870|Stage2-Watch|2024-05-13","non_price_bridge":"delayed PF/housing soft-landing path, but issuer-specific refinancing/liquidity bridge not visible at entry","score_alignment":"local 4B; do not backfill later rebound as immediate Stage2-Actionable"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R10","loop":3,"large_sector_id":"L9_CONSTRUCTION_REAL_ESTATE","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CONSTRUCTION_REBOUND_WITH_PF_BALANCE_SHEET_ATTRIBUTION_CAP","symbol":"047040","name":"대우건설","trigger_type":"Stage2-Watch","entry_date":"2024-05-13","entry_close":3775,"price_basis":"tradable_raw","mfe_30d_pct":1.72,"mae_30d_pct":-4.64,"mfe_90d_pct":31.52,"mae_90d_pct":-6.09,"mfe_180d_pct":31.52,"mae_180d_pct":-6.75,"forward_high_30d":3840,"forward_low_30d":3600,"forward_high_90d":4965,"forward_low_90d":3545,"forward_high_180d":4965,"forward_low_180d":3520,"calibration_usable":true,"case_role":"rebound_with_C30_contribution_cap","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|047040|Stage2-Watch|2024-05-13","non_price_bridge":"construction/EPC rebound and sector beta; issuer-specific PF debt-service relief not isolated","score_alignment":"cap C30 contribution; reclassify to C05 if margin/order bridge dominates"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R10","loop":3,"large_sector_id":"L9_CONSTRUCTION_REAL_ESTATE","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"QUALITY_BALANCE_SHEET_LABEL_WITHOUT_PF_CASH_BRIDGE_STAGE2_CAP","symbol":"375500","name":"DL이앤씨","trigger_type":"Stage2-Watch","entry_date":"2024-05-13","entry_close":34650,"price_basis":"tradable_raw","mfe_30d_pct":3.90,"mae_30d_pct":-4.04,"mfe_90d_pct":14.00,"mae_90d_pct":-17.46,"mfe_180d_pct":14.00,"mae_180d_pct":-17.46,"forward_high_30d":36000,"forward_low_30d":33250,"forward_high_90d":39500,"forward_low_90d":28600,"forward_high_180d":39500,"forward_low_180d":28600,"calibration_usable":true,"case_role":"quality_label_cap","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|375500|Stage2-Watch|2024-05-13","non_price_bridge":"quality/balance-sheet label without fresh PF refinancing, guarantee relief or cash bridge","score_alignment":"Stage2-Watch only; require issuer-specific PF bridge before Actionable"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R10","loop":3,"large_sector_id":"L9_CONSTRUCTION_REAL_ESTATE","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"DIRECT_WORKOUT_STRESS_CONTROL_NOT_CLEAN_EQUITY_RECOVERY","symbol":"009410","name":"태영건설","trigger_type":"Stage2-Watch","entry_date":"2024-01-11","entry_close":3765,"price_basis":"tradable_raw","mfe_30d_pct":9.16,"mae_30d_pct":-42.10,"mfe_90d_pct":9.16,"mae_90d_pct":-42.10,"mfe_180d_pct":62.28,"mae_180d_pct":-42.10,"forward_high_30d":4110,"forward_low_30d":2180,"forward_high_90d":4110,"forward_low_90d":2180,"forward_high_180d":6110,"forward_low_180d":2180,"calibration_usable":false,"case_role":"workout_stress_control","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|009410|Stage2-Watch|2024-01-11","non_price_bridge":"direct workout / debt restructuring survival bridge, but equity recovery and corporate-action window are not clean","score_alignment":"exclude from clean aggregate; use as stress-control for workout-not-equity-recovery rule"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R10","loop":3,"large_sector_id":"L9_CONSTRUCTION_REAL_ESTATE","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"LARGE_BUILDER_SUPPORT_LABEL_NO_ISSUER_PF_BRIDGE_FALSE_POSITIVE","symbol":"000720","name":"현대건설","trigger_type":"Stage2-FalsePositive","entry_date":"2024-03-27","entry_close":33250,"price_basis":"tradable_raw","mfe_30d_pct":4.81,"mae_30d_pct":-6.17,"mfe_90d_pct":8.27,"mae_90d_pct":-6.17,"mfe_180d_pct":8.27,"mae_180d_pct":-27.52,"forward_high_30d":34850,"forward_low_30d":31200,"forward_high_90d":36000,"forward_low_90d":31200,"forward_high_180d":36000,"forward_low_180d":24100,"calibration_usable":true,"case_role":"hard_counterexample","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|000720|Stage2-FalsePositive|2024-03-27","non_price_bridge":"large-builder/support label without issuer-specific PF refinancing or cash relief bridge","score_alignment":"Stage2-FalsePositive; block Actionable unless new PF balance-sheet evidence appears"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R10","loop":3,"large_sector_id":"L9_CONSTRUCTION_REAL_ESTATE","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"MID_BUILDER_SUPPORT_HEADLINE_DELAYED_POSITIVE_4B","symbol":"014790","name":"HL D&I","trigger_type":"Stage2-Watch","entry_date":"2024-03-27","entry_close":2010,"price_basis":"tradable_raw","mfe_30d_pct":1.74,"mae_30d_pct":-3.73,"mfe_90d_pct":32.34,"mae_90d_pct":-3.73,"mfe_180d_pct":32.34,"mae_180d_pct":-3.73,"forward_high_30d":2045,"forward_low_30d":1935,"forward_high_90d":2660,"forward_low_90d":1935,"forward_high_180d":2660,"forward_low_180d":1935,"calibration_usable":true,"case_role":"delayed_positive_watch","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|014790|Stage2-Watch|2024-03-27","non_price_bridge":"builder liquidity/PF soft-landing support headline; delayed price validation but no immediate issuer-specific bridge","score_alignment":"local 4B; do not backfill as immediate Actionable"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R10","loop":3,"large_sector_id":"L9_CONSTRUCTION_REAL_ESTATE","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"SMALL_BUILDER_SUPPORT_BETA_WITH_PF_BRIDGE_REQUIREMENT","symbol":"004960","name":"한신공영","trigger_type":"Stage2-Watch","entry_date":"2024-03-27","entry_close":6720,"price_basis":"tradable_raw","mfe_30d_pct":8.48,"mae_30d_pct":-8.33,"mfe_90d_pct":8.48,"mae_90d_pct":-8.33,"mfe_180d_pct":18.60,"mae_180d_pct":-8.63,"forward_high_30d":7290,"forward_low_30d":6160,"forward_high_90d":7290,"forward_low_90d":6160,"forward_high_180d":7970,"forward_low_180d":6140,"calibration_usable":true,"case_role":"support_beta_cap","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|004960|Stage2-Watch|2024-03-27","non_price_bridge":"small/mid-builder support beta without direct PF exposure reduction or refinancing proof","score_alignment":"Stage2-Watch only; require PF exposure, debt rollover or cash conversion bridge before Actionable"}
```

---

## 4. Case analysis

### 4.1 HDC Hyundai Development / 294870 — delayed positive, not immediate Actionable

The later price path was strong, but the 30D window was nearly flat. This is the signature of delayed local 4B.

```yaml
entry_close: 17920
30d_MFE_MAE: +2.12 / -6.58
90d_MFE_MAE: +37.28 / -6.58
180d_MFE_MAE: +57.37 / -6.58
route: delayed local 4B
```

Do not backfill the May trigger as immediate accounting trust. The bridge needs later confirmation: refinancing, presale, cash-flow, guarantee relief or housing-cycle evidence.

---

### 4.2 Daewoo E&C / 047040 — construction rebound with C30 contribution cap

Daewoo produced a good price path, but the attribution is not cleanly C30. It may be construction beta or C05 margin/order recovery rather than direct PF balance-sheet relief.

```yaml
entry_close: 3775
90d_MFE_MAE: +31.52 / -6.09
180d_MFE_MAE: +31.52 / -6.75
route: contribution cap
```

---

### 4.3 DL E&C / 375500 — quality label cap

A stronger balance-sheet label is useful but not sufficient. C30 must see actual risk transfer.

```yaml
entry_close: 34650
90d_MFE_MAE: +14.00 / -17.46
180d_MFE_MAE: +14.00 / -17.46
route: Stage2 cap
```

---

### 4.4 Taeyoung E&C / 009410 — direct workout stress-control

Workout is not automatically equity recovery. The survival bridge and shareholder bridge are different pipes.

```yaml
entry_close: 3765
30d_MFE_MAE: +9.16 / -42.10
180d_MFE_MAE: +62.28 / -42.10
route: stress-control only
```

Use this row to keep the model honest, not for clean aggregate scoring.

---

### 4.5 Hyundai E&C / 000720 — large-builder support label false positive

Hyundai E&C is the hard counterexample. Large-builder status plus support headline did not create a validated C30 bridge.

```yaml
entry_close: 33250
90d_MFE_MAE: +8.27 / -6.17
180d_MFE_MAE: +8.27 / -27.52
route: Stage2-FalsePositive
```

---

### 4.6 HL D&I / 014790 — delayed support headline positive

HL D&I shows why C30 should not over-block every support headline. The delayed move was real and drawdown was shallow. But it remains local 4B until issuer-specific bridge appears.

```yaml
entry_close: 2010
30d_MFE_MAE: +1.74 / -3.73
90d_MFE_MAE: +32.34 / -3.73
route: delayed local 4B
```

---

### 4.7 Hanshin Engineering / 004960 — support beta with bridge requirement

Hanshin had a modest rebound, not enough for Actionable.

```yaml
entry_close: 6720
90d_MFE_MAE: +8.48 / -8.33
180d_MFE_MAE: +18.60 / -8.63
route: Stage2-Watch
```

---

## 5. Score-return alignment

```yaml
new_independent_case_count: 0
reused_control_case_count: 7
calibration_usable_case_count: 6
calibration_usable_trigger_count: 6
stress_control_case_count: 1
positive_or_delayed_positive_count: 3
counterexample_or_cap_count: 4
local_4B_or_contribution_cap_count: 5
current_profile_error_count: 4
duplicate_note: exact C30 novelty keys likely already represented in C30 loop 1~2; use this MD as rule-formalization evidence unless batch ingest finds a new key
```

| symbol | role | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 294870 | delayed 4B | +2.12 / -6.58 | +37.28 / -6.58 | +57.37 / -6.58 | delayed support path needs bridge refresh |
| 047040 | contribution cap | +1.72 / -4.64 | +31.52 / -6.09 | +31.52 / -6.75 | construction rebound is not always C30 |
| 375500 | quality label cap | +3.90 / -4.04 | +14.00 / -17.46 | +14.00 / -17.46 | quality label lacks direct PF cash bridge |
| 009410 | stress-control only | +9.16 / -42.10 | +9.16 / -42.10 | +62.28 / -42.10 | workout is not clean equity recovery |
| 000720 | hard counterexample | +4.81 / -6.17 | +8.27 / -6.17 | +8.27 / -27.52 | large-builder support label failed |
| 014790 | delayed positive | +1.74 / -3.73 | +32.34 / -3.73 | +32.34 / -3.73 | delayed 4B only, no immediate Stage2 |
| 004960 | support beta watch | +8.48 / -8.33 | +8.48 / -8.33 | +18.60 / -8.63 | small/mid-builder support beta needs proof |

---

## 6. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"294870","raw_PF_refinancing_bridge":2,"raw_liquidity_survival_bridge":2,"raw_equity_value_bridge":2,"raw_cash_conversion":1,"raw_validation":2,"raw_reclassification_risk_C05":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"DelayedLocal4B"}
{"row_type":"score_simulation","symbol":"047040","raw_PF_refinancing_bridge":1,"raw_liquidity_survival_bridge":2,"raw_equity_value_bridge":2,"raw_cash_conversion":1,"raw_validation":2,"raw_reclassification_risk_C05":3,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"ContributionCap"}
{"row_type":"score_simulation","symbol":"375500","raw_PF_refinancing_bridge":1,"raw_liquidity_survival_bridge":2,"raw_equity_value_bridge":1,"raw_cash_conversion":1,"raw_validation":1,"raw_reclassification_risk_C05":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"QualityLabelCap"}
{"row_type":"score_simulation","symbol":"009410","raw_PF_refinancing_bridge":4,"raw_liquidity_survival_bridge":3,"raw_equity_value_bridge":0,"raw_cash_conversion":0,"raw_validation":0,"raw_reclassification_risk_C05":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"StressControlOnly"}
{"row_type":"score_simulation","symbol":"000720","raw_PF_refinancing_bridge":0,"raw_liquidity_survival_bridge":1,"raw_equity_value_bridge":0,"raw_cash_conversion":1,"raw_validation":0,"raw_reclassification_risk_C05":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2FalsePositiveBlock"}
{"row_type":"score_simulation","symbol":"014790","raw_PF_refinancing_bridge":2,"raw_liquidity_survival_bridge":2,"raw_equity_value_bridge":2,"raw_cash_conversion":1,"raw_validation":2,"raw_reclassification_risk_C05":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"DelayedLocal4B"}
{"row_type":"score_simulation","symbol":"004960","raw_PF_refinancing_bridge":1,"raw_liquidity_survival_bridge":1,"raw_equity_value_bridge":1,"raw_cash_conversion":1,"raw_validation":1,"raw_reclassification_risk_C05":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2Watch"}
```

---

## 7. Current calibrated profile stress test

### Existing error risk

C30 can over-credit:

```text
PF support headline
construction rebound
large builder label
workout survival story
```

These are four different pipes. Some carry cash. Some carry only hope. Some save creditors before they save equity.

Correct C30 scoring should ask:

```text
Did issuer-specific refinancing, guarantee relief, maturity extension, presale, cash conversion, or debt-service capacity improve?
```

If the answer is no, the signal belongs to Watch, C05 boundary, or hard block.

### Rule candidate

```text
C30_PF_BALANCE_SHEET_CASH_BRIDGE_REQUIREMENT_V3

if C30
and PF_support_or_construction_rebound_label == true
and issuer_specific_refinancing_guarantee_presale_cash_or_debt_service_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C30
and MFE_30D_pct < +5
and MFE_90D_pct >= +25:
    route = delayed_local_4B
    do_not_backfill_as_immediate_Stage2_Actionable = true
```

```text
if C30
and direct_workout_or_debt_restructuring == true
and shareholder_equity_bridge == false:
    route = StressControl_ExcludeCleanAggregate
    stage2_actionable_bonus = 0
```

```text
if C30
and construction_EPC_margin_or_order_bridge_dominates == true:
    cap_C30_contribution = true
    require_reclassification_to_C05 = true
```

```text
if C30
and large_builder_or_quality_label == true
and MFE_90D_pct < +15
and MAE_180D_pct <= -15
and issuer_specific_PF_bridge == false:
    route = Stage2_Watch_or_FalsePositive_Block
```

---

## 8. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_formalization_from_existing_controls
new_axis_proposed: C30_PF_BALANCE_SHEET_CASH_BRIDGE_REQUIREMENT_V3
existing_axis_strengthened:
  - C30_PF_support_headline_not_enough_without_issuer_bridge
  - C30_delayed_local_4B_do_not_backfill_immediate_stage2
  - C30_direct_workout_survival_not_equity_recovery
  - C30_EPC_margin_reclassification_to_C05
  - C30_large_builder_quality_label_stage2_cap
existing_axis_weakened: null
```

---

## 9. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this single MD. Batch this C30 loop with C30 loops 1~2, C05 loop 114, and R13 construction/PF high-MAE / 4B-4C / accounting-trust guardrails. Extract `C30_PF_BALANCE_SHEET_CASH_BRIDGE_REQUIREMENT_V3` as a shadow-rule candidate. Preserve delayed local 4B paths while blocking large-builder/support labels without issuer-specific refinancing, guarantee relief, presale, cash conversion, or debt-service bridge. Reclassify EPC margin/order-dominant rows to C05.
```

---

## 10. Next research state

```yaml
completed_round: R10
completed_loop: 3
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C31_POLICY_SUBSIDY_LEGISLATION_EVENT
  - C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
  - C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
  - C15_MATERIAL_SPREAD_SUPERCYCLE
  - R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
```
