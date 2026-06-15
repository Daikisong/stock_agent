# E2R v12 R13 cross-archetype residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R13
selected_loop: 7
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
fine_archetype_id: OPERATING_CASH_BRIDGE_HIGH_MAE_ROUTE_SPLIT_EXPORT_PLATFORM_MOBILITY_CONSTRUCTION_FINANCIAL_INSURANCE
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

R13 is a cross-archetype checkpoint, not a sector-specific positive-discovery round. This file uses the latest current-session C18/C26/C29/C30/C21/C22 rows and asks one routing question:

```text
When does high MAE mean temporary local 4B, and when does it mean hard false positive?
```

The previous local `R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL` run reached loop 6. This continuation is `loop 7`.

---

## 1. Research thesis

High MAE is not one thing.

```text
company-specific cash bridge + drawdown
→ local 4B; do not Green until bridge refreshes

label-only / wrong-archetype bridge + drawdown
→ Stage2 cap, reclassification, or hard block

low MFE + high MAE + no bridge
→ false positive
```

The guardrail must not punish real business bridges too early, but it must stop the model from repeatedly reopening label-only themes.

This loop compares six bridge families:

1. **Consumer export**
   - Sell-through and reorder bridge with controlled MAE should survive.
   - Brand/channel label with deep MAE should block.

2. **Platform advertising**
   - Owned platform ARPU/margin bridge should survive.
   - Adtech/agency label with high MAE should block.

3. **Mobility**
   - OEM mix/margin bridge should survive.
   - Auto-parts theme blowoff with deep MAE should route 4B then block if no refresh.

4. **Construction/PF**
   - Delayed rebound should not be backfilled as immediate Stage2.
   - Builder label with no margin/PF cash bridge should block.

5. **Financial/low-PBR**
   - Low-PBR brokerage label with high MAE should block.
   - Real capital-return bridge may stay 4B if capital/payout refresh is pending.

6. **Insurance**
   - GA distribution and life Value-up labels should not become C22 Green without reserve/CSM/solvency bridge.

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 8
  actual_cases: 10
  source_archetypes:
    - C18_CONSUMER_EXPORT_CHANNEL_REORDER
    - C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
    - C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
    - C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
    - C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
    - C22_INSURANCE_RATE_CYCLE_RESERVE
  price_windows:
    - 30D MFE/MAE
    - 90D MFE/MAE
    - 180D MFE/MAE
  output_use:
    - high-MAE routing
    - local 4B vs hard 4C split
    - delayed-rebound no-backfill rule
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
  caveat: Raw/unadjusted OHLC; corporate-action contaminated windows blocked by default.
```

Local stock-web-derived row provenance:

```yaml
reused_price_rows_from_current_session:
  - R5/C18 loop 142
  - R8/C26 loop 100
  - R9/C29 loop 103
  - R10/C30 loop 3
  - R6/C21 loop 112
  - R6/C22 loop 111
  - R13 accounting-trust loop 10
  - R13 Stage2 false-positive loop 9
reason:
  - all reused rows were calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - this file changes canonical scope to R13 high-MAE guardrail
  - exact source-archetype keys should be deduped separately from this R13 guardrail key
  - no production scoring changed
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":7,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"CONSUMER_EXPORT_REORDER_LOW_MAE_POSITIVE_CONTROL","source_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","symbol":"003230","name":"삼양식품","trigger_type":"Stage2-Actionable","entry_date":"2024-05-20","entry_close":502000,"price_basis":"tradable_raw","mfe_30d_pct":43.03,"mae_30d_pct":-4.68,"mfe_90d_pct":43.03,"mae_90d_pct":-9.26,"mfe_180d_pct":59.36,"mae_180d_pct":-9.26,"forward_high_30d":718000,"forward_low_30d":478500,"forward_high_90d":718000,"forward_low_90d":455500,"forward_high_180d":800000,"forward_low_180d":455500,"calibration_usable":true,"case_role":"positive_control_block_hard_4C","novelty_key":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|003230|Stage2-Actionable|2024-05-20","route":"KeepStage2_BlockHard4C","guardrail_lesson":"export sell-through/reorder bridge with controlled MAE should not be hard-blocked"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":7,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"BRAND_EXPORT_CHANNEL_LABEL_DEEP_MAE_HARD_BLOCK","source_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","symbol":"383220","name":"F&F","trigger_type":"Stage2-FalsePositive","entry_date":"2024-07-17","entry_close":74000,"price_basis":"tradable_raw","mfe_30d_pct":3.24,"mae_30d_pct":-33.99,"mfe_90d_pct":3.24,"mae_90d_pct":-33.99,"mfe_180d_pct":3.24,"mae_180d_pct":-33.99,"forward_high_30d":76400,"forward_low_30d":48850,"forward_high_90d":76400,"forward_low_90d":48850,"forward_high_180d":76400,"forward_low_180d":48850,"calibration_usable":true,"case_role":"hard_counterexample","novelty_key":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|383220|Stage2-FalsePositive|2024-07-17","route":"Hard4C_Stage2FalsePositiveBlock","guardrail_lesson":"brand/export label with low MFE and deep MAE should hard-block without sell-through/inventory proof"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":7,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"OWNED_PLATFORM_ARPU_MARGIN_LOW_MAE_POSITIVE_CONTROL","source_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"035420","name":"NAVER","trigger_type":"Stage2-Actionable","entry_date":"2024-11-08","entry_close":174600,"price_basis":"tradable_raw","mfe_30d_pct":26.00,"mae_30d_pct":-1.78,"mfe_90d_pct":34.88,"mae_90d_pct":-1.78,"mfe_180d_pct":34.88,"mae_180d_pct":-1.78,"forward_high_30d":220000,"forward_low_30d":171500,"forward_high_90d":235500,"forward_low_90d":171500,"forward_high_180d":235500,"forward_low_180d":171500,"calibration_usable":true,"case_role":"positive_control_block_hard_4C","novelty_key":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|035420|Stage2-Actionable|2024-11-08","route":"KeepStage2_BlockHard4C","guardrail_lesson":"owned platform inventory/ARPU/margin bridge with low MAE should survive high-MAE red-team"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":7,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"ADTECH_SERVICE_LABEL_HIGH_MAE_HARD_BLOCK","source_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"214270","name":"FSN","trigger_type":"Stage2-FalsePositive","entry_date":"2024-07-18","entry_close":2105,"price_basis":"tradable_raw","mfe_30d_pct":16.63,"mae_30d_pct":-26.37,"mfe_90d_pct":19.00,"mae_90d_pct":-26.37,"mfe_180d_pct":19.00,"mae_180d_pct":-49.64,"forward_high_30d":2455,"forward_low_30d":1550,"forward_high_90d":2505,"forward_low_90d":1550,"forward_high_180d":2505,"forward_low_180d":1060,"calibration_usable":true,"case_role":"hard_counterexample","novelty_key":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|214270|Stage2-FalsePositive|2024-07-18","route":"Hard4C_Stage2FalsePositiveBlock","guardrail_lesson":"adtech label without owned-platform bridge and high MAE should hard-block"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":7,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"OEM_VOLUME_MIX_MARGIN_LOW_MAE_POSITIVE_CONTROL","source_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"000270","name":"기아","trigger_type":"Stage2-Actionable","entry_date":"2024-01-25","entry_close":93000,"price_basis":"tradable_raw","mfe_30d_pct":41.61,"mae_30d_pct":-7.42,"mfe_90d_pct":45.16,"mae_90d_pct":-7.42,"mfe_180d_pct":45.16,"mae_180d_pct":-7.42,"forward_high_30d":131700,"forward_low_30d":86100,"forward_high_90d":135000,"forward_low_90d":86100,"forward_high_180d":135000,"forward_low_180d":86100,"calibration_usable":true,"case_role":"positive_control_block_hard_4C","novelty_key":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|000270|Stage2-Actionable|2024-01-25","route":"KeepStage2_BlockHard4C","guardrail_lesson":"OEM volume/mix/margin bridge with controlled MAE should not be routed to 4C"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":7,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"AUTO_PARTS_THEME_HIGH_MFE_HIGH_MAE_LOCAL_4B_THEN_BLOCK","source_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"010690","name":"화신","trigger_type":"Stage2-Watch","entry_date":"2024-06-12","entry_close":11690,"price_basis":"tradable_raw","mfe_30d_pct":35.93,"mae_30d_pct":-4.53,"mfe_90d_pct":35.93,"mae_90d_pct":-30.28,"mfe_180d_pct":35.93,"mae_180d_pct":-47.39,"forward_high_30d":15890,"forward_low_30d":11160,"forward_high_90d":15890,"forward_low_90d":8150,"forward_high_180d":15890,"forward_low_180d":6150,"calibration_usable":true,"case_role":"local_4B_then_block","novelty_key":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|010690|Stage2-Watch|2024-06-12","route":"Local4BThenBlockIfNoRefresh","guardrail_lesson":"auto-parts theme can get 4B after MFE, but high MAE demands customer-volume/margin refresh or block"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":7,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"CONSTRUCTION_DELAYED_REBOUND_LOCAL_4B_NO_BACKFILL","source_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"294870","name":"HDC현대산업개발","trigger_type":"Stage2-Watch","entry_date":"2024-05-13","entry_close":17920,"price_basis":"tradable_raw","mfe_30d_pct":2.12,"mae_30d_pct":-6.58,"mfe_90d_pct":37.28,"mae_90d_pct":-6.58,"mfe_180d_pct":57.37,"mae_180d_pct":-6.58,"forward_high_30d":18300,"forward_low_30d":16740,"forward_high_90d":24600,"forward_low_90d":16740,"forward_high_180d":28200,"forward_low_180d":16740,"calibration_usable":true,"case_role":"delayed_local_4B","novelty_key":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|294870|Stage2-Watch|2024-05-13","route":"DelayedLocal4B_DoNotBackfillImmediateStage2","guardrail_lesson":"delayed rebound with low 30D MFE should not be backfilled as immediate Stage2"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":7,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"LOW_PBR_BROKERAGE_HIGH_MAE_HARD_BLOCK","source_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"006800","name":"미래에셋증권","trigger_type":"Stage2-FalsePositive","entry_date":"2024-02-26","entry_close":8680,"price_basis":"tradable_raw","mfe_30d_pct":5.53,"mae_30d_pct":-10.71,"mfe_90d_pct":5.53,"mae_90d_pct":-20.16,"mfe_180d_pct":5.53,"mae_180d_pct":-23.96,"forward_high_30d":9160,"forward_low_30d":7750,"forward_high_90d":9160,"forward_low_90d":6930,"forward_high_180d":9160,"forward_low_180d":6600,"calibration_usable":true,"case_role":"hard_counterexample","novelty_key":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|006800|Stage2-FalsePositive|2024-02-26","route":"Hard4C_Stage2FalsePositiveBlock","guardrail_lesson":"low-PBR brokerage label with low MFE and high MAE should hard-block without capital-return execution"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":7,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"INSURANCE_GA_DISTRIBUTION_RECLASSIFICATION_CAP","source_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"244920","name":"에이플러스에셋","trigger_type":"Stage2-Watch","entry_date":"2024-05-10","entry_close":4100,"price_basis":"tradable_raw","mfe_30d_pct":9.76,"mae_30d_pct":-2.32,"mfe_90d_pct":9.76,"mae_90d_pct":-13.78,"mfe_180d_pct":14.63,"mae_180d_pct":-13.78,"forward_high_30d":4500,"forward_low_30d":4005,"forward_high_90d":4500,"forward_low_90d":3535,"forward_high_180d":4700,"forward_low_180d":3535,"calibration_usable":true,"case_role":"reclassification_cap","novelty_key":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|244920|Stage2-Watch|2024-05-10","route":"Stage2Cap_Reclassify","guardrail_lesson":"GA commission bridge can be real, but selected C22 reserve-cycle bridge is missing"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":7,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"LIFE_INSURANCE_VALUEUP_LABEL_WITHOUT_CSM_SOLVENCY_STAGE2_CAP","source_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"088350","name":"한화생명","trigger_type":"Stage2-Watch","entry_date":"2024-02-26","entry_close":3060,"price_basis":"tradable_raw","mfe_30d_pct":9.31,"mae_30d_pct":-8.17,"mfe_90d_pct":9.31,"mae_90d_pct":-15.69,"mfe_180d_pct":9.31,"mae_180d_pct":-15.69,"forward_high_30d":3345,"forward_low_30d":2810,"forward_high_90d":3345,"forward_low_90d":2580,"forward_high_180d":3345,"forward_low_180d":2580,"calibration_usable":true,"case_role":"stage2_cap","novelty_key":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|088350|Stage2-Watch|2024-02-26","route":"Stage2Cap","guardrail_lesson":"life-insurance Value-up label needs CSM, solvency and payout bridge before Stage2 Actionable"}
```

---

## 5. Case analysis

### 5.1 Samyang Foods / 003230 — low-MAE positive control

This is a positive control against over-blocking. Export reorder bridge is real and drawdown stayed controlled.

```text
route = KeepStage2_BlockHard4C
```

### 5.2 F&F / 383220 — brand label hard block

This is a clean hard-block case. No sell-through bridge, low MFE, deep MAE.

```text
route = Hard4C_Stage2FalsePositiveBlock
```

### 5.3 NAVER / 035420 — owned-platform low-MAE positive control

Owned platform monetization bridge validated. Hard 4C would be wrong.

```text
route = KeepStage2_BlockHard4C
```

### 5.4 FSN / 214270 — adtech high-MAE hard block

High MAE plus no owned inventory/ARPU bridge makes this a false positive.

```text
route = Hard4C_Stage2FalsePositiveBlock
```

### 5.5 Kia / 000270 — OEM margin positive control

Volume and mix bridge was strong enough to survive the guardrail.

```text
route = KeepStage2_BlockHard4C
```

### 5.6 Hwashin / 010690 — high-MFE local 4B, then block without refresh

The early MFE was real, but not durable. This is the classic local 4B to hard-block route.

```text
route = Local4BThenBlockIfNoRefresh
```

### 5.7 HDC Hyundai Development / 294870 — delayed local 4B

This row prevents the model from backfilling late success into early Stage2.

```text
route = DelayedLocal4B_DoNotBackfillImmediateStage2
```

### 5.8 Mirae Asset Securities / 006800 — low-PBR high-MAE hard block

Cheapness did not turn into capital-return execution.

```text
route = Hard4C_Stage2FalsePositiveBlock
```

### 5.9 A Plus Asset / 244920 — reclassification cap

The business may have commission economics, but the selected C22 bridge is missing.

```text
route = Stage2Cap_Reclassify
```

### 5.10 Hanwha Life / 088350 — life-insurance Value-up cap

No CSM/solvency/payout bridge, so the label stays capped.

```text
route = Stage2Cap
```

---

## 6. Score-return alignment

```yaml
new_independent_case_count: 10
calibration_usable_case_count: 10
calibration_usable_trigger_count: 10
positive_control_count: 3
local_4B_or_delayed_watch_count: 2
stage2_cap_or_reclassification_count: 2
hard_4C_or_stage2_block_count: 3
current_profile_error_count: 7
```

| symbol | source | route | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 003230 | C18 | keep Stage2 | +43.03 / -9.26 | +59.36 / -9.26 | real reorder bridge |
| 383220 | C18 | hard block | +3.24 / -33.99 | +3.24 / -33.99 | brand label fails |
| 035420 | C26 | keep Stage2 | +34.88 / -1.78 | +34.88 / -1.78 | owned platform bridge |
| 214270 | C26 | hard block | +19.00 / -26.37 | +19.00 / -49.64 | adtech label fails |
| 000270 | C29 | keep Stage2 | +45.16 / -7.42 | +45.16 / -7.42 | OEM margin bridge |
| 010690 | C29 | 4B -> block | +35.93 / -30.28 | +35.93 / -47.39 | theme MFE lacks durability |
| 294870 | C30 | delayed 4B | +37.28 / -6.58 | +57.37 / -6.58 | delayed rebound no backfill |
| 006800 | C21 | hard block | +5.53 / -20.16 | +5.53 / -23.96 | low-PBR label fails |
| 244920 | C22 | reclassify | +9.76 / -13.78 | +14.63 / -13.78 | wrong bridge for selected archetype |
| 088350 | C22 | cap | +9.31 / -15.69 | +9.31 / -15.69 | life value-up label lacks CSM/solvency |

---

## 7. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"003230","raw_bridge_quality":5,"raw_accounting_trust":5,"raw_mfe_validation":5,"raw_mae_penalty":1,"raw_label_only_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_BlockHard4C"}
{"row_type":"score_simulation","symbol":"383220","raw_bridge_quality":0,"raw_accounting_trust":0,"raw_mfe_validation":0,"raw_mae_penalty":5,"raw_label_only_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C_Stage2FalsePositiveBlock"}
{"row_type":"score_simulation","symbol":"035420","raw_bridge_quality":5,"raw_accounting_trust":5,"raw_mfe_validation":4,"raw_mae_penalty":0,"raw_label_only_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_BlockHard4C"}
{"row_type":"score_simulation","symbol":"214270","raw_bridge_quality":0,"raw_accounting_trust":0,"raw_mfe_validation":1,"raw_mae_penalty":5,"raw_label_only_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C_Stage2FalsePositiveBlock"}
{"row_type":"score_simulation","symbol":"000270","raw_bridge_quality":5,"raw_accounting_trust":5,"raw_mfe_validation":5,"raw_mae_penalty":1,"raw_label_only_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_BlockHard4C"}
{"row_type":"score_simulation","symbol":"010690","raw_bridge_quality":1,"raw_accounting_trust":1,"raw_mfe_validation":2,"raw_mae_penalty":5,"raw_label_only_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Local4BThenBlockIfNoRefresh"}
{"row_type":"score_simulation","symbol":"294870","raw_bridge_quality":2,"raw_accounting_trust":1,"raw_mfe_validation":3,"raw_mae_penalty":1,"raw_label_only_risk":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"DelayedLocal4B_NoBackfill"}
{"row_type":"score_simulation","symbol":"006800","raw_bridge_quality":0,"raw_accounting_trust":0,"raw_mfe_validation":0,"raw_mae_penalty":4,"raw_label_only_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C_Stage2FalsePositiveBlock"}
{"row_type":"score_simulation","symbol":"244920","raw_bridge_quality":1,"raw_accounting_trust":1,"raw_mfe_validation":1,"raw_mae_penalty":2,"raw_label_only_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2Cap_Reclassify"}
{"row_type":"score_simulation","symbol":"088350","raw_bridge_quality":1,"raw_accounting_trust":1,"raw_mfe_validation":0,"raw_mae_penalty":3,"raw_label_only_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2Cap"}
```

---

## 8. Current calibrated profile stress test

### Existing error risk

The current profile can still make two symmetric mistakes:

```text
bad block:
high MAE anywhere -> hard 4C
```

This would overpunish high-MFE names where a real bridge exists but needs refresh.

```text
bad reward:
any high MFE -> keep Stage2 / Green
```

This would overlearn theme blowoffs and label-only moves.

The correct rule is mechanical:

```text
bridge quality decides route first
price path decides severity second
```

### Rule candidate

```text
R13_HIGH_MAE_LABEL_TO_BRIDGE_ROUTE_SPLIT_V7

if company_specific_accounting_bridge == true
and MFE_90D_pct >= +20
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
    block_hard_4C = true
```

```text
if company_specific_bridge_is_real_but_unrefreshed == true
and MFE_30D_pct >= +30
and MAE_90D_pct <= -20:
    route = local_4B_watch
    block_stage3_green = true
    require_bridge_refresh = true
```

```text
if label_only_or_wrong_archetype_bridge == true
and MFE_90D_pct < +10
and MAE_90D_pct <= -15:
    stage2_actionable_bonus = 0
    route = Stage2Cap_or_Hard4C
```

```text
if label_only_or_wrong_archetype_bridge == true
and MAE_90D_pct <= -20:
    route = hard_4C_or_Stage2_FalsePositive_Block
```

```text
if MFE_30D_pct < +5
and MFE_90D_pct >= +25
and bridge_refreshed_later == true:
    route = delayed_local_4B
    do_not_backfill_as_immediate_stage2 = true
```

```text
if bridge_belongs_to_other_archetype == true:
    cap_selected_archetype_contribution = true
    require_reclassification = true
```

---

## 9. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
cross_archetype_rule_candidate: true
loop_contribution_label: cross_archetype_high_MAE_guardrail_candidate
new_axis_proposed: R13_HIGH_MAE_LABEL_TO_BRIDGE_ROUTE_SPLIT_V7
existing_axis_strengthened:
  - company_specific_bridge_low_MAE_keep_stage2
  - high_MFE_unrefreshed_bridge_local_4B
  - label_only_high_MAE_hard_4C
  - wrong_archetype_bridge_reclassification_guard
  - delayed_rebound_no_backfill
existing_axis_weakened: null
```

---

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this single MD. Batch this R13 high-MAE loop with R13 Stage2 false-positive loop 9, R13 accounting-trust loop 10, and source loops C18/C26/C29/C30/C21/C22 from this session. Extract `R13_HIGH_MAE_LABEL_TO_BRIDGE_ROUTE_SPLIT_V7` as a cross-archetype shadow rule. Preserve cases with company-specific accounting bridge and controlled MAE, keep real-but-unrefreshed high-MFE bridges in local 4B, and hard-block label-only or wrong-archetype rows when MAE expands.
```

---

## 11. Next research state

```yaml
completed_round: R13
completed_loop: 7
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
  - C15_MATERIAL_SPREAD_SUPERCYCLE
  - C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
  - C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
  - C22_INSURANCE_RATE_CYCLE_RESERVE
```
