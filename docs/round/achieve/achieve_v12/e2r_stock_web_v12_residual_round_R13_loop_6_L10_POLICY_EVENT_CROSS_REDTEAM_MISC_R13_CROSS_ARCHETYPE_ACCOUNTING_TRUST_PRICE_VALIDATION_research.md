# E2R v12 R13 cross-archetype residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R13
selected_loop: 6
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
fine_archetype_id: DIRECT_CASH_BRIDGE_VALIDATION_VS_OPTIONALITY_LABEL_AND_DELAYED_PF_SOFT_LANDING
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

R13 is not a sector-discovery round. It is the checkpoint that asks whether a prior sector label is actually supported by accounting-quality evidence and price-return alignment.

The prior local `R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION` run reached loop 5, so this same canonical pair continues as loop 6.

This loop uses recent C20, C27 and C30 outputs:

- `003230 / C20 / 삼양식품`: global distribution sell-through validated.
- `086980 / C27 / 쇼박스`: direct box-office cash bridge validated, but one-hit cap.
- `294870 / C30 / HDC현대산업개발`: delayed PF/housing soft-landing path; not immediate accounting validation.
- `375500 / C30 / DL이앤씨`: quality/balance-sheet label with insufficient price accounting validation.
- `271560 / C20 / 오리온`: mature global footprint but low incremental MFE.
- `263720 / C27 / 디앤씨미디어`: IP optionality with high-MFE/high-MAE; requires cash bridge refresh.

---

## 1. Research thesis

Accounting trust is the question:

```text
Can the headline be traced into revenue, margin, cash transfer, debt relief, or legally visible economics?
```

If yes, Stage2 can stay open. If not, the signal should be capped, watched, or blocked.

This loop splits six routes:

```text
A. Direct sell-through/export bridge + strong price validation
   → keep Stage2-Actionable; allow Stage3-Yellow path

B. Direct box-office/purchase cash bridge + contained MAE
   → keep Stage2-Actionable, but apply one-off-hit cap

C. IP optionality with high MFE but deep MAE
   → local 4B watch; require royalty/licensing/game/platform cash bridge

D. Mature global footprint with low MFE
   → cap Stage2; require incremental distribution/reorder proof

E. PF/restructuring headline with delayed price repair
   → delayed 4B; do not backfill as immediate accounting validation

F. Balance-sheet quality label without explicit margin/refinancing/cash bridge
   → Stage2 cap
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

Symbol caveats:

```yaml
003230:
  name: 삼양식품
  source_archetype: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
  corporate_action_candidate_dates: [2003-07-25]
  relevant_window_after_candidate: true

086980:
  name: 쇼박스
  source_archetype: C27_CONTENT_IP_GLOBAL_MONETIZATION
  corporate_action_candidate_dates: [2011-05-17]
  relevant_window_after_candidate: true

294870:
  name: HDC현대산업개발
  source_archetype: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
  corporate_action_candidate_dates: [2020-03-26]
  relevant_window_after_candidate: true

375500:
  name: DL이앤씨
  source_archetype: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
  corporate_action_candidate_dates: [2022-04-08, 2022-04-28]
  relevant_window_after_candidate: true

271560:
  name: 오리온
  source_archetype: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
  corporate_action_candidate_count: 0
  calibration_caveat: clean

263720:
  name: 디앤씨미디어
  source_archetype: C27_CONTENT_IP_GLOBAL_MONETIZATION
  corporate_action_candidate_dates: [2017-11-29, 2017-12-20]
  relevant_window_after_candidate: true
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":6,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"KFOOD_EXPORT_SELLTHROUGH_ACCOUNTING_TRUST_VALIDATED","source_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","symbol":"003230","name":"삼양식품","trigger_type":"Stage2-Actionable","entry_date":"2024-05-20","entry_close":502000,"price_basis":"tradable_raw","mfe_30d_pct":43.03,"mae_30d_pct":-4.68,"mfe_90d_pct":43.03,"mae_90d_pct":-9.26,"mfe_180d_pct":59.36,"mae_180d_pct":-9.26,"forward_high_30d":718000,"forward_low_30d":478500,"forward_high_90d":718000,"forward_low_90d":455500,"forward_high_180d":800000,"forward_low_180d":455500,"calibration_usable":true,"case_role":"positive_control","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|003230|Stage2-Actionable|2024-05-20","accounting_bridge":"export sell-through / reorder / margin operating leverage","route":"AccountingTrustValidated_KeepStage2"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":6,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"BOX_OFFICE_DIRECT_CASH_BRIDGE_VALIDATED_WITH_ONE_OFF_HIT_CAP","source_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","symbol":"086980","name":"쇼박스","trigger_type":"Stage2-Actionable","entry_date":"2024-02-22","entry_close":3670,"price_basis":"tradable_raw","mfe_30d_pct":23.84,"mae_30d_pct":-0.41,"mfe_90d_pct":23.84,"mae_90d_pct":-6.40,"mfe_180d_pct":23.84,"mae_180d_pct":-6.40,"forward_high_30d":4545,"forward_low_30d":3655,"forward_high_90d":4545,"forward_low_90d":3435,"forward_high_180d":4545,"forward_low_180d":3435,"calibration_usable":true,"case_role":"positive_control_with_one_off_cap","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|086980|Stage2-Actionable|2024-02-22","accounting_bridge":"direct theatrical distribution / box-office cash bridge","route":"AccountingTrustValidated_OneOffHitCap"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":6,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"PF_RESTRUCTURING_DELAYED_PRICE_REPAIR_NOT_IMMEDIATE_ACCOUNTING_VALIDATION","source_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"294870","name":"HDC현대산업개발","trigger_type":"Stage2-Watch","entry_date":"2024-05-13","entry_close":17920,"price_basis":"tradable_raw","mfe_30d_pct":2.12,"mae_30d_pct":-6.58,"mfe_90d_pct":37.28,"mae_90d_pct":-6.58,"mfe_180d_pct":57.37,"mae_180d_pct":-6.58,"forward_high_30d":18300,"forward_low_30d":16740,"forward_high_90d":24600,"forward_low_90d":16740,"forward_high_180d":28200,"forward_low_180d":16740,"calibration_usable":true,"case_role":"delayed_positive_watch","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|294870|Stage2-Watch|2024-05-13","accounting_bridge":"PF support/restructuring macro bridge but issuer-specific refinancing/cash bridge not immediate","route":"Delayed4B_DoNotBackfillImmediateAccountingTrust"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":6,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"BALANCE_SHEET_QUALITY_LABEL_WITHOUT_PRICE_ACCOUNTING_VALIDATION","source_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"375500","name":"DL이앤씨","trigger_type":"Stage2-Watch","entry_date":"2024-05-13","entry_close":34650,"price_basis":"tradable_raw","mfe_30d_pct":3.90,"mae_30d_pct":-4.04,"mfe_90d_pct":14.00,"mae_90d_pct":-17.46,"mfe_180d_pct":14.00,"mae_180d_pct":-17.46,"forward_high_30d":36000,"forward_low_30d":33250,"forward_high_90d":39500,"forward_low_90d":28600,"forward_high_180d":39500,"forward_low_180d":28600,"calibration_usable":true,"case_role":"quality_label_cap","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|375500|Stage2-Watch|2024-05-13","accounting_bridge":"balance-sheet quality label but no fresh PF refinancing/margin/cash validation","route":"AccountingTrustNotValidated_Stage2Cap"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":6,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"MATURE_GLOBAL_FOOTPRINT_LOW_MFE_INCREMENTAL_BRIDGE_CAP","source_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","symbol":"271560","name":"오리온","trigger_type":"Stage2-Watch","entry_date":"2024-06-10","entry_close":97900,"price_basis":"tradable_raw","mfe_30d_pct":8.99,"mae_30d_pct":-6.54,"mfe_90d_pct":8.99,"mae_90d_pct":-11.44,"mfe_180d_pct":8.99,"mae_180d_pct":-11.44,"forward_high_30d":106700,"forward_low_30d":91500,"forward_high_90d":106700,"forward_low_90d":86700,"forward_high_180d":106700,"forward_low_180d":86700,"calibration_usable":true,"case_role":"low_MFE_cap","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|271560|Stage2-Watch|2024-06-10","accounting_bridge":"mature global footprint without incremental distribution/reorder/margin catalyst at trigger","route":"AccountingTrustIncrementalBridgeMissing_Stage2Cap"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":6,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"WEBTOON_IP_OPTIONALITY_HIGH_MFE_HIGH_MAE_CASH_BRIDGE_REQUIRED","source_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","symbol":"263720","name":"디앤씨미디어","trigger_type":"Stage2-Actionable","entry_date":"2024-01-08","entry_close":29850,"price_basis":"tradable_raw","mfe_30d_pct":29.31,"mae_30d_pct":-19.26,"mfe_90d_pct":29.31,"mae_90d_pct":-26.30,"mfe_180d_pct":29.31,"mae_180d_pct":-27.81,"forward_high_30d":38600,"forward_low_30d":24100,"forward_high_90d":38600,"forward_low_90d":22000,"forward_high_180d":38600,"forward_low_180d":21550,"calibration_usable":true,"case_role":"high_MFE_high_MAE_4B_watch","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|263720|Stage2-Actionable|2024-01-08","accounting_bridge":"webtoon/anime IP optionality but royalty/licensing/game/platform cash bridge not refreshed in price path","route":"Local4B_RequireCashBridgeRefresh"}
```

---

## 4. Case analysis

### 4.1 Samyang Foods / 003230 — accounting trust validated

Samyang is the cleanest validation row. The non-price bridge is not abstract brand awareness. Buldak/global ramen demand translated into shelf access, export sell-through, and margin leverage. The price path confirms it.

```yaml
entry_close: 502000
30d_high: 718000
30d_low: 478500
90d_high: 718000
90d_low: 455500
180d_high: 800000
180d_low: 455500
```

Route:

```text
AccountingTrustValidated_KeepStage2
```

This is the escape hatch. If a trigger has direct sell-through and price alignment, R13 should not over-block it.

---

### 4.2 Showbox / 086980 — direct cash bridge, one-hit cap

Showbox has a direct theatrical cash bridge. Exhuma was not just “content IP noise”; it was a box-office event distributed by Showbox.

```yaml
entry_close: 3670
30d_high: 4545
30d_low: 3655
90d_high: 4545
90d_low: 3435
180d_high: 4545
180d_low: 3435
```

Route:

```text
AccountingTrustValidated_OneOffHitCap
```

The cap matters. One box-office hit can be real accounting trust, but it is not automatically a durable library/franchise monetization engine.

---

### 4.3 HDC Hyundai Development / 294870 — delayed positive, no immediate accounting trust

HDC’s path is a delayed repair after PF restructuring and housing sentiment improved. The 30D path was weak, while 90D and 180D became strong.

```yaml
entry_close: 17920
30d_high: 18300
90d_high: 24600
180d_high: 28200
low: 16740
```

Route:

```text
Delayed4B_DoNotBackfillImmediateAccountingTrust
```

This is a timing guardrail. The model can give delayed 4B credit, but should not backfill the May trigger as immediately accounting-trust validated unless issuer-specific PF refinancing or liquidity bridge is visible.

---

### 4.4 DL E&C / 375500 — quality label cap

DL E&C shows why quality/balance-sheet labels are not enough. The price path had limited MFE and a meaningful drawdown.

```yaml
entry_close: 34650
30d_high: 36000
90d_high: 39500
90d_low: 28600
```

Route:

```text
AccountingTrustNotValidated_Stage2Cap
```

The company can be higher-quality than peers, but C30 accounting trust requires explicit risk relief, margin stabilization, refinancing, or cash conversion.

---

### 4.5 Orion / 271560 — mature footprint without incremental bridge

Orion is global, but the selected trigger did not produce enough incremental price validation.

```yaml
entry_close: 97900
forward_high: 106700
forward_low: 86700
```

Route:

```text
AccountingTrustIncrementalBridgeMissing_Stage2Cap
```

A mature footprint is the road. The trigger still needs a new truck: incremental SKU rollout, channel expansion, reorder acceleration, or margin revision.

---

### 4.6 D&C Media / 263720 — IP optionality needs cash bridge refresh

D&C Media had a legitimate Solo Leveling IP optionality move. But the high-MFE/high-MAE path says the market later questioned listed-company cash capture.

```yaml
entry_close: 29850
forward_high: 38600
30d_low: 24100
90d_low: 22000
180d_low: 21550
```

Route:

```text
Local4B_RequireCashBridgeRefresh
```

The stock recognized the IP spark. R13 asks whether that spark became cash through royalties, licensing, game revenue, drama/platform payments, or book volume.

---

## 5. Score-return alignment

```yaml
new_independent_case_count: 6
calibration_usable_case_count: 6
calibration_usable_trigger_count: 6
accounting_trust_validated_count: 2
one_off_cap_count: 1
delayed_4B_count: 1
stage2_cap_count: 2
local_4B_cash_bridge_required_count: 1
current_profile_error_count: 4
```

| symbol | source | route | 90D MFE/MAE | 180D MFE/MAE | accounting lesson |
|---|---:|---:|---:|---:|---|
| 003230 | C20 | validated | +43.03 / -9.26 | +59.36 / -9.26 | export sell-through and margin bridge are price-validated |
| 086980 | C27 | validated + one-hit cap | +23.84 / -6.40 | +23.84 / -6.40 | direct box-office cash bridge works, but library cap needed |
| 294870 | C30 | delayed 4B | +37.28 / -6.58 | +57.37 / -6.58 | delayed PF/housing repair, not immediate trust validation |
| 375500 | C30 | Stage2 cap | +14.00 / -17.46 | +14.00 / -17.46 | quality label without fresh cash/refinancing bridge is capped |
| 271560 | C20 | Stage2 cap | +8.99 / -11.44 | +8.99 / -11.44 | mature global footprint lacks incremental bridge |
| 263720 | C27 | local 4B | +29.31 / -26.30 | +29.31 / -27.81 | IP optionality needs listed-company cash bridge refresh |

---

## 6. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"003230","raw_revenue_bridge":5,"raw_margin_cash_bridge":5,"raw_validation":5,"raw_visibility":5,"raw_incremental_bridge":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"AccountingTrustValidated"}
{"row_type":"score_simulation","symbol":"086980","raw_revenue_bridge":4,"raw_margin_cash_bridge":3,"raw_validation":4,"raw_visibility":4,"raw_incremental_bridge":3,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"AccountingTrustValidated_OneOffCap"}
{"row_type":"score_simulation","symbol":"294870","raw_revenue_bridge":1,"raw_margin_cash_bridge":1,"raw_validation":2,"raw_visibility":3,"raw_incremental_bridge":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Delayed4B_NoImmediateTrust"}
{"row_type":"score_simulation","symbol":"375500","raw_revenue_bridge":1,"raw_margin_cash_bridge":1,"raw_validation":1,"raw_visibility":3,"raw_incremental_bridge":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2Cap"}
{"row_type":"score_simulation","symbol":"271560","raw_revenue_bridge":2,"raw_margin_cash_bridge":1,"raw_validation":1,"raw_visibility":4,"raw_incremental_bridge":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2Cap_MatureFootprint"}
{"row_type":"score_simulation","symbol":"263720","raw_revenue_bridge":2,"raw_margin_cash_bridge":1,"raw_validation":2,"raw_visibility":5,"raw_incremental_bridge":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Local4B_RequireCashBridge"}
```

---

## 7. Current calibrated profile stress test

### Existing error risk

The profile can over-score:

```text
brand/IP/PF/global footprint label
+ one price spike
```

It can also under-score:

```text
direct sell-through or box-office cash bridge
+ strong price validation
```

So the accounting-trust gate must not be a blanket punishment. It should behave like a ledger auditor:

```text
Can the event be traced to revenue, margin, cash, debt relief, or legally visible economics?
Did price confirm that bridge?
Was the bridge repeatable, or one-off?
```

### Rule candidate

```text
R13_ACCOUNTING_TRUST_PRICE_ALIGNMENT_GATE_V6

if direct_revenue_or_cash_bridge == true
and MFE_90D_pct >= +20
and MAE_90D_pct > -15:
    accounting_trust_validated = true
    keep_stage2_actionable_bonus = true
```

```text
if direct_revenue_or_cash_bridge == true
and one_off_event == true:
    keep_stage2_actionable_bonus = true
    cap_stage3_green_until_repeat_or_library_bridge = true
```

```text
if MFE_30D_pct < +5
and MFE_90D_pct >= +25
and bridge_refresh_occurs_later == true:
    route = delayed_local_4B
    do_not_backfill_as_immediate_accounting_validation = true
```

```text
if headline_label == true
and incremental_revenue_margin_cash_bridge == false
and MFE_90D_pct < +15:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if MFE_30D_pct >= +20
and MAE_90D_pct <= -20
and refreshed_cash_bridge == false:
    local_4B_watch = true
    block_stage3_green = true
```

---

## 8. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
cross_archetype_rule_candidate: true
loop_contribution_label: cross_archetype_accounting_trust_price_validation_candidate
new_axis_proposed: R13_ACCOUNTING_TRUST_PRICE_ALIGNMENT_GATE_V6
existing_axis_strengthened:
  - direct_revenue_cash_bridge_validated_escape_hatch
  - one_off_hit_cap_until_repeat_bridge
  - delayed_4B_do_not_backfill_as_immediate_validation
  - mature_global_or_quality_label_stage2_cap
  - high_MFE_high_MAE_cash_bridge_refresh_requirement
existing_axis_weakened: null
```

---

## 9. Next recommended archetypes

```text
C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
C22_INSURANCE_RATE_CYCLE_RESERVE
C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_retest_with_direct_workout_controls
C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
```
