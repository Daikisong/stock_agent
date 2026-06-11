# E2R v12 R13 cross-archetype residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R13
selected_loop: 102
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
fine_archetype_id: NUCLEAR_MATERIAL_CONSUMER_FINANCIAL_INSURANCE_LOCAL_4B_VS_HARD_4C_ROUTE_SPLIT
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

R13 is a cross-archetype checkpoint, not a sector-specific discovery round. This file uses the most recent C04, C15, C20, C21 and C22 sector-rule rows to test the 4B/4C switch:

```text
real bridge but incomplete / delayed / unrefreshed
→ local 4B

label-only or wrong-archetype bridge with low MFE or deep MAE
→ hard 4C / Stage2 false-positive block
```

The previous local `R13_CROSS_ARCHETYPE_4B_4C_REDTEAM` run reached loop 101, so this run continues as `loop 102`.

---

## 1. Research thesis

The same drawdown can mean different things depending on the bridge behind it.

```text
A. real bridge + incomplete proof
   → inspect in local 4B

B. label-only + no cash bridge
   → hard block

C. later evidence appears after the trigger
   → create a new trigger row; do not backfill

D. bridge belongs to another archetype
   → cap selected archetype and reclassify
```

This loop compares five archetype families:

1. **Nuclear project / C04**
   - Preferred-bidder or direct-scope evidence can create a tradable spike.
   - If final contract, legal clearance and cash bridge were absent at the trigger date, route to local 4B or cap.
   - Small supplier price-only spikes are hard 4C.

2. **Materials / C15**
   - Company-specific margin bridge survives.
   - Material label high-MFE / high-MAE stays local 4B until margin/FCF refresh.
   - Low-MFE / high-MAE material labels hard block.

3. **Global consumer distribution / C20**
   - Sell-through / OPM / revision bridge survives.
   - Brand or channel label with inventory decay hard blocks.

4. **Financial capital return / C21**
   - ROE / payout / buyback execution bridge survives.
   - Low-PBR label without execution hard blocks.

5. **Insurance / C22**
   - Nonlife reserve/capital-return bridge survives.
   - GA distribution or life-insurance Value-up label without reserve/CSM/solvency bridge should cap or reclassify.

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 10
  actual_cases: 10
  source_archetypes:
    - C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
    - C15_MATERIAL_SPREAD_SUPERCYCLE
    - C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
    - C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
    - C22_INSURANCE_RATE_CYCLE_RESERVE
  price_windows:
    - 30D MFE/MAE
    - 90D MFE/MAE
    - 180D MFE/MAE
  output_use:
    - R13 4B/4C route split
    - local 4B vs hard 4C separation
    - no-backfill guard
    - wrong-archetype reclassification guard
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
  caveat: Raw/unadjusted OHLC; corporate-action-contaminated windows blocked by default.
```

Local stock-web-derived row provenance:

```yaml
reused_price_rows_from_current_session:
  - R1/C04 loop 114
  - R4/C15 loop 105
  - R5/C20 loop 115
  - R6/C21 loop 112
  - R6/C22 loop 111
  - R13 Stage2 false-positive loop 9
  - R13 high-MAE loop 7
reason:
  - all rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - this file changes canonical scope to R13 4B/4C red-team
  - exact source-archetype keys should be deduped separately from this R13 guardrail key
  - no production scoring changed
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":102,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"NUCLEAR_PREFERRED_BIDDER_LOCAL_4B_NO_FINAL_CONTRACT_BACKFILL","source_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"034020","name":"두산에너빌리티","trigger_type":"Stage2-Watch","entry_date":"2024-07-17","entry_close":21250,"price_basis":"tradable_raw","mfe_30d_pct":17.65,"mae_30d_pct":-28.71,"mfe_90d_pct":17.65,"mae_90d_pct":-28.71,"mfe_180d_pct":17.65,"mae_180d_pct":-28.71,"forward_high_30d":25000,"forward_low_30d":15150,"forward_high_90d":25000,"forward_low_90d":15150,"forward_high_180d":25000,"forward_low_180d":15150,"calibration_usable":true,"case_role":"local_4B_no_backfill","novelty_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|034020|Stage2-Watch|2024-07-17","route":"Local4B_NoFinalContractBackfill","guardrail_lesson":"preferred-bidder spike can be local 4B, but later final contract cannot be backfilled into the original trigger"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":102,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"NUCLEAR_SMALL_SUPPLIER_THEME_SPIKE_HARD_4C","source_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"457550","name":"우진엔텍","trigger_type":"Stage2-FalsePositive","entry_date":"2024-07-18","entry_close":31500,"price_basis":"tradable_raw","mfe_30d_pct":32.06,"mae_30d_pct":-50.83,"mfe_90d_pct":32.06,"mae_90d_pct":-58.25,"mfe_180d_pct":32.06,"mae_180d_pct":-58.25,"forward_high_30d":41600,"forward_low_30d":15490,"forward_high_90d":41600,"forward_low_90d":13150,"forward_high_180d":41600,"forward_low_180d":13150,"calibration_usable":true,"case_role":"hard_4C_counterexample","novelty_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|457550|Stage2-FalsePositive|2024-07-18","route":"Hard4C_Stage2FalsePositiveBlock","guardrail_lesson":"supplier theme spike with severe MAE and no contract-scope cash bridge should not remain Stage2"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":102,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"MATERIAL_MARGIN_LOW_MAE_POSITIVE_CONTROL","source_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","symbol":"002380","name":"KCC","trigger_type":"Stage2-Actionable","entry_date":"2024-01-30","entry_close":244000,"price_basis":"tradable_raw","mfe_30d_pct":17.62,"mae_30d_pct":-2.46,"mfe_90d_pct":20.49,"mae_90d_pct":-7.79,"mfe_180d_pct":41.39,"mae_180d_pct":-7.79,"forward_high_30d":287000,"forward_low_30d":238000,"forward_high_90d":294000,"forward_low_90d":225000,"forward_high_180d":345000,"forward_low_180d":225000,"calibration_usable":true,"case_role":"positive_control_block_4C","novelty_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|002380|Stage2-Actionable|2024-01-30","route":"KeepStage2_BlockHard4C","guardrail_lesson":"company-specific material margin bridge with controlled MAE should not be downgraded to 4C"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":102,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"BATTERY_FOIL_MATERIAL_HIGH_MFE_HIGH_MAE_LOCAL_4B","source_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","symbol":"006110","name":"삼아알미늄","trigger_type":"Stage2-Watch","entry_date":"2024-05-20","entry_close":75500,"price_basis":"tradable_raw","mfe_30d_pct":28.34,"mae_30d_pct":-7.28,"mfe_90d_pct":28.34,"mae_90d_pct":-47.55,"mfe_180d_pct":28.34,"mae_180d_pct":-53.58,"forward_high_30d":96900,"forward_low_30d":70000,"forward_high_90d":96900,"forward_low_90d":39600,"forward_high_180d":96900,"forward_low_180d":35050,"calibration_usable":true,"case_role":"local_4B_then_block_if_no_refresh","novelty_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|006110|Stage2-Watch|2024-05-20","route":"Local4BThenBlockIfNoMarginRefresh","guardrail_lesson":"material high-MFE/high-MAE can remain 4B only while utilization and margin bridge are being refreshed"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":102,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"GLOBAL_FOOD_DISTRIBUTION_LOW_MAE_POSITIVE_CONTROL","source_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","symbol":"003230","name":"삼양식품","trigger_type":"Stage2-Actionable","entry_date":"2024-05-20","entry_close":502000,"price_basis":"tradable_raw","mfe_30d_pct":43.03,"mae_30d_pct":-4.68,"mfe_90d_pct":43.03,"mae_90d_pct":-9.26,"mfe_180d_pct":59.36,"mae_180d_pct":-9.26,"forward_high_30d":718000,"forward_low_30d":478500,"forward_high_90d":718000,"forward_low_90d":455500,"forward_high_180d":800000,"forward_low_180d":455500,"calibration_usable":true,"case_role":"positive_control_block_4C","novelty_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|003230|Stage2-Actionable|2024-05-20","route":"KeepStage2_BlockHard4C","guardrail_lesson":"global distribution sell-through and OPM bridge with controlled MAE should remain Stage2"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":102,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"GLOBAL_BRAND_INVENTORY_LABEL_HARD_4C","source_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","symbol":"383220","name":"F&F","trigger_type":"Stage2-FalsePositive","entry_date":"2024-07-17","entry_close":74000,"price_basis":"tradable_raw","mfe_30d_pct":3.24,"mae_30d_pct":-33.99,"mfe_90d_pct":3.24,"mae_90d_pct":-33.99,"mfe_180d_pct":3.24,"mae_180d_pct":-33.99,"forward_high_30d":76400,"forward_low_30d":48850,"forward_high_90d":76400,"forward_low_90d":48850,"forward_high_180d":76400,"forward_low_180d":48850,"calibration_usable":true,"case_role":"hard_4C_counterexample","novelty_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|383220|Stage2-FalsePositive|2024-07-17","route":"Hard4C_Stage2FalsePositiveBlock","guardrail_lesson":"brand/global channel label with low MFE and deep MAE should hard-block without sell-through and inventory proof"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":102,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"CAPITAL_RETURN_LOW_MAE_FINANCIAL_POSITIVE_CONTROL","source_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"005940","name":"NH투자증권","trigger_type":"Stage2-Actionable","entry_date":"2024-02-26","entry_close":11420,"price_basis":"tradable_raw","mfe_30d_pct":14.71,"mae_30d_pct":-2.36,"mfe_90d_pct":14.71,"mae_90d_pct":-2.36,"mfe_180d_pct":26.09,"mae_180d_pct":-2.36,"forward_high_30d":13100,"forward_low_30d":11150,"forward_high_90d":13100,"forward_low_90d":11150,"forward_high_180d":14400,"forward_low_180d":11150,"calibration_usable":true,"case_role":"positive_control_block_4C","novelty_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|005940|Stage2-Actionable|2024-02-26","route":"KeepStage2_BlockHard4C","guardrail_lesson":"ROE and capital-return bridge with low MAE should survive 4C red-team"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":102,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"LOW_PBR_BROKERAGE_LABEL_HARD_4C","source_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"006800","name":"미래에셋증권","trigger_type":"Stage2-FalsePositive","entry_date":"2024-02-26","entry_close":8680,"price_basis":"tradable_raw","mfe_30d_pct":5.53,"mae_30d_pct":-10.71,"mfe_90d_pct":5.53,"mae_90d_pct":-20.16,"mfe_180d_pct":5.53,"mae_180d_pct":-23.96,"forward_high_30d":9160,"forward_low_30d":7750,"forward_high_90d":9160,"forward_low_90d":6930,"forward_high_180d":9160,"forward_low_180d":6600,"calibration_usable":true,"case_role":"hard_4C_counterexample","novelty_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|006800|Stage2-FalsePositive|2024-02-26","route":"Hard4C_Stage2FalsePositiveBlock","guardrail_lesson":"low-PBR label without capital-return execution and high MAE should hard-block"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":102,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"NONLIFE_RESERVE_CAPITAL_RETURN_LOW_MAE_POSITIVE_CONTROL","source_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"005830","name":"DB손해보험","trigger_type":"Stage2-Actionable","entry_date":"2024-02-26","entry_close":95000,"price_basis":"tradable_raw","mfe_30d_pct":15.79,"mae_30d_pct":-4.11,"mfe_90d_pct":27.05,"mae_90d_pct":-9.26,"mfe_180d_pct":30.53,"mae_180d_pct":-9.26,"forward_high_30d":110000,"forward_low_30d":91100,"forward_high_90d":120700,"forward_low_90d":86200,"forward_high_180d":124000,"forward_low_180d":86200,"calibration_usable":true,"case_role":"positive_control_block_4C","novelty_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|005830|Stage2-Actionable|2024-02-26","route":"KeepStage2_BlockHard4C","guardrail_lesson":"nonlife reserve/loss-ratio/capital-return bridge with controlled MAE should not be hard-blocked"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":102,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"GA_DISTRIBUTION_WRONG_ARCHETYPE_STAGE2_CAP","source_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"244920","name":"에이플러스에셋","trigger_type":"Stage2-Watch","entry_date":"2024-05-10","entry_close":4100,"price_basis":"tradable_raw","mfe_30d_pct":9.76,"mae_30d_pct":-2.32,"mfe_90d_pct":9.76,"mae_90d_pct":-13.78,"mfe_180d_pct":14.63,"mae_180d_pct":-13.78,"forward_high_30d":4500,"forward_low_30d":4005,"forward_high_90d":4500,"forward_low_90d":3535,"forward_high_180d":4700,"forward_low_180d":3535,"calibration_usable":true,"case_role":"reclassification_cap","novelty_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|244920|Stage2-Watch|2024-05-10","route":"Stage2Cap_Reclassify","guardrail_lesson":"GA commission bridge is real but wrong for C22 reserve-cycle; cap selected archetype and reclassify"}
```

---

## 5. Case analysis

### 5.1 Doosan Enerbility / 034020 — local 4B, not backfilled Green

Preferred-bidder exposure created tradable movement, but final contract evidence was not present at the 2024 trigger.

```text
route = Local4B_NoFinalContractBackfill
```

### 5.2 Woojin Entech / 457550 — hard 4C supplier spike

The move had high MFE, but severe MAE and no named contract-scope economics. This is hard 4C.

```text
route = Hard4C_Stage2FalsePositiveBlock
```

### 5.3 KCC / 002380 — Stage2 positive control

Company-specific material margin bridge validates and should not be hard-blocked.

```text
route = KeepStage2_BlockHard4C
```

### 5.4 Sam-A Aluminium / 006110 — local 4B, then block if no refresh

High MFE was real enough for watch, but the severe drawdown requires margin/utilization refresh before any Green path.

```text
route = Local4BThenBlockIfNoMarginRefresh
```

### 5.5 Samyang Foods / 003230 — export distribution positive control

Sell-through and OPM bridge validate. This is a positive control against over-blocking.

```text
route = KeepStage2_BlockHard4C
```

### 5.6 F&F / 383220 — global brand hard block

Brand/global-channel label failed without sell-through and inventory bridge.

```text
route = Hard4C_Stage2FalsePositiveBlock
```

### 5.7 NH Investment & Securities / 005940 — financial positive control

ROE and capital-return bridge with low MAE should survive 4C red-team.

```text
route = KeepStage2_BlockHard4C
```

### 5.8 Mirae Asset Securities / 006800 — low-PBR hard block

Low-PBR label did not become capital-return execution.

```text
route = Hard4C_Stage2FalsePositiveBlock
```

### 5.9 DB Insurance / 005830 — nonlife positive control

Reserve, loss-ratio and capital-return bridge validates.

```text
route = KeepStage2_BlockHard4C
```

### 5.10 A Plus Asset / 244920 — reclassification cap

GA distribution economics may be real, but not C22 reserve-cycle. This is reclassification, not Green.

```text
route = Stage2Cap_Reclassify
```

---

## 6. Score-return alignment

```yaml
new_independent_case_count: 10
calibration_usable_case_count: 10
calibration_usable_trigger_count: 10
positive_control_count: 4
local_4B_watch_count: 2
hard_4C_or_stage2_block_count: 3
stage2_cap_or_reclassification_count: 1
current_profile_error_count: 6
```

| symbol | source | route | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 034020 | C04 | local 4B | +17.65 / -28.71 | +17.65 / -28.71 | preferred bidder is not final contract |
| 457550 | C04 | hard 4C | +32.06 / -58.25 | +32.06 / -58.25 | supplier spike has no cash bridge |
| 002380 | C15 | keep Stage2 | +20.49 / -7.79 | +41.39 / -7.79 | company material margin bridge |
| 006110 | C15 | local 4B | +28.34 / -47.55 | +28.34 / -53.58 | battery-foil label needs refresh |
| 003230 | C20 | keep Stage2 | +43.03 / -9.26 | +59.36 / -9.26 | sell-through/OPM bridge |
| 383220 | C20 | hard 4C | +3.24 / -33.99 | +3.24 / -33.99 | brand/inventory label fails |
| 005940 | C21 | keep Stage2 | +14.71 / -2.36 | +26.09 / -2.36 | ROE/capital-return bridge |
| 006800 | C21 | hard 4C | +5.53 / -20.16 | +5.53 / -23.96 | low-PBR label fails |
| 005830 | C22 | keep Stage2 | +27.05 / -9.26 | +30.53 / -9.26 | reserve/capital-return bridge |
| 244920 | C22 | reclassify | +9.76 / -13.78 | +14.63 / -13.78 | GA bridge belongs elsewhere |

---

## 7. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"034020","raw_bridge_quality":2,"raw_accounting_trust":1,"raw_mfe_validation":1,"raw_mae_penalty":4,"raw_label_only_risk":3,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Local4B_NoFinalContractBackfill"}
{"row_type":"score_simulation","symbol":"457550","raw_bridge_quality":0,"raw_accounting_trust":0,"raw_mfe_validation":1,"raw_mae_penalty":5,"raw_label_only_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C_Stage2FalsePositiveBlock"}
{"row_type":"score_simulation","symbol":"002380","raw_bridge_quality":5,"raw_accounting_trust":5,"raw_mfe_validation":4,"raw_mae_penalty":1,"raw_label_only_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_BlockHard4C"}
{"row_type":"score_simulation","symbol":"006110","raw_bridge_quality":1,"raw_accounting_trust":1,"raw_mfe_validation":2,"raw_mae_penalty":5,"raw_label_only_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Local4BThenBlockIfNoRefresh"}
{"row_type":"score_simulation","symbol":"003230","raw_bridge_quality":5,"raw_accounting_trust":5,"raw_mfe_validation":5,"raw_mae_penalty":1,"raw_label_only_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_BlockHard4C"}
{"row_type":"score_simulation","symbol":"383220","raw_bridge_quality":0,"raw_accounting_trust":0,"raw_mfe_validation":0,"raw_mae_penalty":5,"raw_label_only_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C_Stage2FalsePositiveBlock"}
{"row_type":"score_simulation","symbol":"005940","raw_bridge_quality":5,"raw_accounting_trust":5,"raw_mfe_validation":4,"raw_mae_penalty":0,"raw_label_only_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_BlockHard4C"}
{"row_type":"score_simulation","symbol":"006800","raw_bridge_quality":0,"raw_accounting_trust":0,"raw_mfe_validation":0,"raw_mae_penalty":4,"raw_label_only_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C_Stage2FalsePositiveBlock"}
{"row_type":"score_simulation","symbol":"005830","raw_bridge_quality":5,"raw_accounting_trust":5,"raw_mfe_validation":4,"raw_mae_penalty":1,"raw_label_only_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_BlockHard4C"}
{"row_type":"score_simulation","symbol":"244920","raw_bridge_quality":2,"raw_accounting_trust":1,"raw_mfe_validation":1,"raw_mae_penalty":2,"raw_label_only_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2Cap_Reclassify"}
```

---

## 8. Current calibrated profile stress test

### Existing error risk

The profile can still treat three different situations too similarly:

```text
real bridge + drawdown
label-only + drawdown
wrong-archetype bridge + drawdown
```

The correct routing is:

```text
real bridge + controlled MAE
→ keep Stage2

real bridge but unrefreshed + high MAE
→ local 4B

label-only + high MAE
→ hard 4C

wrong-archetype bridge
→ reclassification cap
```

A bridge is like a load-bearing beam. If the beam exists but is uninspected, send the case to 4B. If there is only painted scenery, send it to 4C.

### Rule candidate

```text
R13_4B_4C_BRIDGE_FIRST_ROUTE_SPLIT_V102

if company_specific_accounting_bridge == true
and MFE_90D_pct >= +20
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
    block_hard_4C = true
```

```text
if company_specific_bridge == true
and MFE_30D_pct >= +20
and MAE_90D_pct <= -25
and bridge_refresh_missing == true:
    route = local_4B_watch
    block_stage3_green = true
```

```text
if label_only_or_price_only_spike == true
and MAE_90D_pct <= -25:
    route = hard_4C_or_Stage2_FalsePositive_Block
    stage2_actionable_bonus = 0
```

```text
if selected_archetype_bridge_missing == true
and real_bridge_belongs_to_other_archetype == true:
    cap_selected_archetype_contribution = true
    require_reclassification = true
```

```text
if later_final_contract_or_later_bridge_appears_after_original_trigger == true:
    do_not_backfill = true
    require_new_trigger_from_later_evidence_date = true
```

---

## 9. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
cross_archetype_rule_candidate: true
loop_contribution_label: cross_archetype_4B_4C_redteam_guardrail_candidate
new_axis_proposed: R13_4B_4C_BRIDGE_FIRST_ROUTE_SPLIT_V102
existing_axis_strengthened:
  - real_bridge_controlled_MAE_keep_stage2
  - real_bridge_high_MAE_local_4B
  - label_only_high_MAE_hard_4C
  - wrong_archetype_bridge_reclassification_cap
  - later_evidence_no_backfill_guard
existing_axis_weakened: null
```

---

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this single MD. Batch this R13 4B/4C loop with R13 high-MAE loop 7, R13 Stage2 false-positive loop 9, R13 accounting-trust loop 10, and source loops C04/C15/C20/C21/C22 from this session. Extract `R13_4B_4C_BRIDGE_FIRST_ROUTE_SPLIT_V102` as a cross-archetype shadow rule. Preserve real company-specific accounting bridges with controlled MAE, route real-but-unrefreshed high-MAE bridges to local 4B, hard-block label-only high-MAE rows, and force reclassification where the bridge belongs to another archetype.
```

---

## 11. Next research state

```yaml
completed_round: R13
completed_loop: 102
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C18_CONSUMER_EXPORT_CHANNEL_REORDER
  - C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
  - C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
  - C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
  - C31_POLICY_SUBSIDY_LEGISLATION_EVENT
```
