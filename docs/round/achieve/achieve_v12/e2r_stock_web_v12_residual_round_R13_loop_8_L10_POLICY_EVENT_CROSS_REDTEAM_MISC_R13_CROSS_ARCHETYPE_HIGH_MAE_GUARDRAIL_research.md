# E2R v12 R13 cross-archetype residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R13
selected_loop: 8
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
fine_archetype_id: CONTRACT_MATERIAL_CONSUMER_FINANCIAL_POLICY_TENDER_HIGH_MAE_ROUTE_SPLIT
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

R13 is a cross-archetype checkpoint, not a sector-positive discovery round. This file uses the latest current-session C04, C15, C20, C21, C22, C31 and C32 rows and asks:

```text
When MAE is high, should the row remain local 4B, or should it become hard 4C / Stage2 false positive?
```

The previous local `R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL` run reached loop 7. This continuation is `loop 8`.

---

## 1. Research thesis

High MAE is not a single diagnosis.

```text
real bridge + high MAE
→ local 4B until bridge refresh

label-only + high MAE
→ hard 4C / Stage2 false-positive block

wrong-archetype bridge + high MAE
→ cap selected archetype and reclassify

later evidence after trigger
→ do not backfill; create a new trigger row
```

The core mistake is to let price shape decide everything. Price is the smoke. The bridge is the fire.

This loop compares seven bridge families:

1. **Nuclear project / contract bridge**
   - Preferred bidder or supplier theme can move price.
   - Without final contract, legal clearance, order scope and cash bridge, high MAE should block Green.
   - Supplier-only high-MFE/high-MAE spikes should become hard 4C.

2. **Material spread**
   - Company-specific margin bridge survives.
   - Material label with no ASP/utilization/margin/FCF refresh stays local 4B or blocks.

3. **Consumer distribution**
   - Sell-through and OPM bridge survives.
   - Legacy brand/channel label with deep MAE hard blocks.

4. **Financial capital return**
   - ROE/payout bridge with low MAE survives.
   - Low-PBR label with high MAE blocks.

5. **Insurance reserve / capital return**
   - Nonlife reserve/capital-return bridge survives.
   - Insurance label without reserve/CSM/solvency bridge caps.

6. **Policy support**
   - Policy-to-issuer cash bridge can be delayed local 4B.
   - Policy umbrella with no issuer cash bridge blocks.

7. **Governance / tender**
   - Formal tender cash-exit can survive even with post-resolution MAE.
   - Capital-return cash is not tender cash-exit; reclassify.

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 10
  actual_cases: 12
  source_archetypes:
    - C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
    - C15_MATERIAL_SPREAD_SUPERCYCLE
    - C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
    - C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
    - C22_INSURANCE_RATE_CYCLE_RESERVE
    - C31_POLICY_SUBSIDY_LEGISLATION_EVENT
    - C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
  price_windows:
    - 30D MFE/MAE
    - 90D MFE/MAE
    - 180D MFE/MAE
  output_use:
    - high-MAE route split
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
  - R11/C31 loops 103~104
  - R12/C32 loop 104
  - R13 accounting-trust loop 11
  - R13 Stage2 false-positive loop 10
  - R13 4B/4C loop 102
reason:
  - all rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - current file changes canonical scope to R13 high-MAE guardrail
  - exact source-archetype keys should be deduped separately from this R13 guardrail key
  - no production scoring changed
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":8,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"NUCLEAR_PREFERRED_BIDDER_HIGH_MAE_LOCAL_4B_NO_BACKFILL","source_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"034020","name":"두산에너빌리티","trigger_type":"Stage2-Watch","entry_date":"2024-07-17","entry_close":21250,"price_basis":"tradable_raw","mfe_30d_pct":17.65,"mae_30d_pct":-28.71,"mfe_90d_pct":17.65,"mae_90d_pct":-28.71,"mfe_180d_pct":17.65,"mae_180d_pct":-28.71,"forward_high_30d":25000,"forward_low_30d":15150,"forward_high_90d":25000,"forward_low_90d":15150,"forward_high_180d":25000,"forward_low_180d":15150,"calibration_usable":true,"case_role":"local_4B_no_backfill","novelty_key":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|034020|Stage2-Watch|2024-07-17","route":"Local4B_NoFinalContractBackfill","guardrail_lesson":"preferred-bidder story had bridge potential, but high MAE and missing final contract keep it local 4B"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":8,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"NUCLEAR_SUPPLIER_THEME_HIGH_MFE_SEVERE_MAE_HARD_4C","source_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"457550","name":"우진엔텍","trigger_type":"Stage2-FalsePositive","entry_date":"2024-07-18","entry_close":31500,"price_basis":"tradable_raw","mfe_30d_pct":32.06,"mae_30d_pct":-50.83,"mfe_90d_pct":32.06,"mae_90d_pct":-58.25,"mfe_180d_pct":32.06,"mae_180d_pct":-58.25,"forward_high_30d":41600,"forward_low_30d":15490,"forward_high_90d":41600,"forward_low_90d":13150,"forward_high_180d":41600,"forward_low_180d":13150,"calibration_usable":true,"case_role":"hard_4C_counterexample","novelty_key":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|457550|Stage2-FalsePositive|2024-07-18","route":"Hard4C_Stage2FalsePositiveBlock","guardrail_lesson":"supplier theme spike with severe MAE and no contract-scope bridge should hard-block"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":8,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"MATERIAL_MARGIN_LOW_MAE_POSITIVE_CONTROL","source_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","symbol":"002380","name":"KCC","trigger_type":"Stage2-Actionable","entry_date":"2024-01-30","entry_close":244000,"price_basis":"tradable_raw","mfe_30d_pct":17.62,"mae_30d_pct":-2.46,"mfe_90d_pct":20.49,"mae_90d_pct":-7.79,"mfe_180d_pct":41.39,"mae_180d_pct":-7.79,"forward_high_30d":287000,"forward_low_30d":238000,"forward_high_90d":294000,"forward_low_90d":225000,"forward_high_180d":345000,"forward_low_180d":225000,"calibration_usable":true,"case_role":"positive_control_block_hard_4C","novelty_key":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|002380|Stage2-Actionable|2024-01-30","route":"KeepStage2_BlockHard4C","guardrail_lesson":"company-specific material margin bridge with controlled MAE should not be routed to hard 4C"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":8,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"MATERIAL_FOIL_HIGH_MFE_SEVERE_MAE_LOCAL_4B_THEN_BLOCK","source_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","symbol":"006110","name":"삼아알미늄","trigger_type":"Stage2-Watch","entry_date":"2024-05-20","entry_close":75500,"price_basis":"tradable_raw","mfe_30d_pct":28.34,"mae_30d_pct":-7.28,"mfe_90d_pct":28.34,"mae_90d_pct":-47.55,"mfe_180d_pct":28.34,"mae_180d_pct":-53.58,"forward_high_30d":96900,"forward_low_30d":70000,"forward_high_90d":96900,"forward_low_90d":39600,"forward_high_180d":96900,"forward_low_180d":35050,"calibration_usable":true,"case_role":"local_4B_then_block_if_no_refresh","novelty_key":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|006110|Stage2-Watch|2024-05-20","route":"Local4BThenBlockIfNoMarginRefresh","guardrail_lesson":"high-MFE material label can be 4B only while utilization/margin bridge is being refreshed"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":8,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"GLOBAL_CONSUMER_SELLTHROUGH_LOW_MAE_POSITIVE_CONTROL","source_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","symbol":"003230","name":"삼양식품","trigger_type":"Stage2-Actionable","entry_date":"2024-05-17","entry_close":446500,"price_basis":"tradable_raw","mfe_30d_pct":60.81,"mae_30d_pct":0.00,"mfe_90d_pct":60.81,"mae_90d_pct":0.00,"mfe_180d_pct":106.05,"mae_180d_pct":0.00,"calibration_usable":true,"case_role":"positive_control_block_hard_4C","novelty_key":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|003230|Stage2-Actionable|2024-05-17","route":"KeepStage2_BlockHard4C","guardrail_lesson":"sell-through/OPM bridge with no drawdown should survive high-MAE guardrail"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":8,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"LEGACY_BEAUTY_LABEL_LOW_MFE_HIGH_MAE_HARD_4C","source_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","symbol":"090430","name":"아모레퍼시픽","trigger_type":"Stage2-FalsePositive","entry_date":"2024-05-31","entry_close":194200,"price_basis":"tradable_raw","mfe_30d_pct":3.24,"mae_30d_pct":-14.68,"mfe_90d_pct":3.24,"mae_90d_pct":-40.32,"mfe_180d_pct":3.24,"mae_180d_pct":-48.76,"calibration_usable":true,"case_role":"hard_4C_counterexample","novelty_key":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|090430|Stage2-FalsePositive|2024-05-31","route":"Hard4C_Stage2FalsePositiveBlock","guardrail_lesson":"legacy brand/channel label with low MFE and deep MAE should hard-block without sell-through bridge"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":8,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"FINANCIAL_CAPITAL_RETURN_LOW_MAE_POSITIVE_CONTROL","source_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"005940","name":"NH투자증권","trigger_type":"Stage2-Actionable","entry_date":"2024-02-26","entry_close":11420,"price_basis":"tradable_raw","mfe_30d_pct":14.71,"mae_30d_pct":-2.36,"mfe_90d_pct":14.71,"mae_90d_pct":-2.36,"mfe_180d_pct":26.09,"mae_180d_pct":-2.36,"forward_high_30d":13100,"forward_low_30d":11150,"forward_high_90d":13100,"forward_low_90d":11150,"forward_high_180d":14400,"forward_low_180d":11150,"calibration_usable":true,"case_role":"positive_control_block_hard_4C","novelty_key":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|005940|Stage2-Actionable|2024-02-26","route":"KeepStage2_BlockHard4C","guardrail_lesson":"ROE/capital-return bridge with low MAE should not be hard-blocked"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":8,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"LOW_PBR_FINANCIAL_LABEL_HIGH_MAE_HARD_4C","source_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"006800","name":"미래에셋증권","trigger_type":"Stage2-FalsePositive","entry_date":"2024-02-26","entry_close":8680,"price_basis":"tradable_raw","mfe_30d_pct":5.53,"mae_30d_pct":-10.71,"mfe_90d_pct":5.53,"mae_90d_pct":-20.16,"mfe_180d_pct":5.53,"mae_180d_pct":-23.96,"forward_high_30d":9160,"forward_low_30d":7750,"forward_high_90d":9160,"forward_low_90d":6930,"forward_high_180d":9160,"forward_low_180d":6600,"calibration_usable":true,"case_role":"hard_4C_counterexample","novelty_key":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|006800|Stage2-FalsePositive|2024-02-26","route":"Hard4C_Stage2FalsePositiveBlock","guardrail_lesson":"low-PBR label with high MAE and no capital-return bridge should hard-block"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":8,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"NONLIFE_RESERVE_CAPITAL_RETURN_LOW_MAE_POSITIVE_CONTROL","source_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"005830","name":"DB손해보험","trigger_type":"Stage2-Actionable","entry_date":"2024-02-26","entry_close":95000,"price_basis":"tradable_raw","mfe_30d_pct":15.79,"mae_30d_pct":-4.11,"mfe_90d_pct":27.05,"mae_90d_pct":-9.26,"mfe_180d_pct":30.53,"mae_180d_pct":-9.26,"forward_high_30d":110000,"forward_low_30d":91100,"forward_high_90d":120700,"forward_low_90d":86200,"forward_high_180d":124000,"forward_low_180d":86200,"calibration_usable":true,"case_role":"positive_control_block_hard_4C","novelty_key":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|005830|Stage2-Actionable|2024-02-26","route":"KeepStage2_BlockHard4C","guardrail_lesson":"reserve/loss-ratio/capital-return bridge with low MAE should survive high-MAE red-team"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":8,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"PF_POLICY_DELAYED_CASH_BRIDGE_LOCAL_4B_NO_BACKFILL","source_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"294870","name":"HDC현대산업개발","trigger_type":"Stage2-Watch","entry_date":"2024-05-13","entry_close":17920,"price_basis":"tradable_raw","mfe_30d_pct":2.12,"mae_30d_pct":-6.58,"mfe_90d_pct":37.28,"mae_90d_pct":-6.58,"mfe_180d_pct":57.37,"mae_180d_pct":-6.58,"forward_high_30d":18300,"forward_low_30d":16740,"forward_high_90d":24600,"forward_low_90d":16740,"forward_high_180d":28200,"forward_low_180d":16740,"calibration_usable":true,"case_role":"delayed_local_4B","novelty_key":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|294870|Stage2-Watch|2024-05-13","route":"DelayedLocal4B_DoNotBackfill","guardrail_lesson":"delayed policy/cash bridge can stay 4B, but the original trigger must not be upgraded retroactively"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":8,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"FORMAL_TENDER_POST_RESOLUTION_HIGH_MAE_LOCAL_4B_NOT_HARD_BLOCK","source_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"041510","name":"에스엠","trigger_type":"Stage2-Actionable","entry_date":"2023-02-10","entry_close":114700,"price_basis":"tradable_raw","mfe_30d_pct":40.54,"mae_30d_pct":-6.45,"mfe_90d_pct":40.54,"mae_90d_pct":-21.10,"mfe_180d_pct":40.54,"mae_180d_pct":-21.10,"forward_high_30d":161200,"forward_low_30d":107300,"forward_high_90d":161200,"forward_low_90d":90500,"forward_high_180d":161200,"forward_low_180d":90500,"calibration_usable":true,"case_role":"positive_with_post_resolution_local_4B","novelty_key":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|041510|Stage2-Actionable|2023-02-10","route":"KeepStage2_PostResolution4B","guardrail_lesson":"formal tender cash bridge can survive high MAE; post-resolution MAE routes to 4B, not hard 4C"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":8,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"CAPITAL_RETURN_WRONG_ARCHETYPE_RECLASSIFICATION_HIGH_MAE_CAP","source_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"105560","name":"KB금융","trigger_type":"Stage2-Watch","entry_date":"2024-07-26","entry_close":87900,"price_basis":"tradable_raw","mfe_30d_pct":5.12,"mae_30d_pct":-15.81,"mfe_90d_pct":18.20,"mae_90d_pct":-15.81,"mfe_180d_pct":18.20,"mae_180d_pct":-15.81,"forward_high_30d":92400,"forward_low_30d":74000,"forward_high_90d":103900,"forward_low_90d":74000,"forward_high_180d":103900,"forward_low_180d":74000,"calibration_usable":true,"case_role":"wrong_archetype_reclassification_cap","novelty_key":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|105560|Stage2-Watch|2024-07-26","route":"Reclassify_C32Cap","guardrail_lesson":"capital-return bridge may be real elsewhere, but it is not C32 tender mechanics"}
```

---

## 5. Case analysis

### 5.1 Doosan Enerbility / 034020 — high MAE but local 4B, not hard 4C

The preferred-bidder bridge was incomplete at trigger date. High MAE blocks Green, but the row can remain local 4B because the project bridge was not purely imaginary.

```text
route = Local4B_NoFinalContractBackfill
```

### 5.2 Woojin Entech / 457550 — severe MAE hard 4C

This is price-only supplier heat without contract-scope cash economics.

```text
route = Hard4C_Stage2FalsePositiveBlock
```

### 5.3 KCC / 002380 — positive control

Company-specific margin bridge validates. Hard 4C would be wrong.

```text
route = KeepStage2_BlockHard4C
```

### 5.4 Sam-A Aluminium / 006110 — high-MFE material 4B then block

The early move was real enough for 4B, but severe MAE requires margin refresh.

```text
route = Local4BThenBlockIfNoMarginRefresh
```

### 5.5 Samyang Foods / 003230 — distribution positive control

The bridge reached sell-through, OPM and price validation.

```text
route = KeepStage2_BlockHard4C
```

### 5.6 Amorepacific / 090430 — label hard 4C

Legacy brand label failed after deep MAE.

```text
route = Hard4C_Stage2FalsePositiveBlock
```

### 5.7 NH Investment & Securities / 005940 — capital-return low-MAE control

A real capital-return bridge should not be blocked.

```text
route = KeepStage2_BlockHard4C
```

### 5.8 Mirae Asset Securities / 006800 — low-PBR high-MAE block

Cheapness did not become execution.

```text
route = Hard4C_Stage2FalsePositiveBlock
```

### 5.9 DB Insurance / 005830 — insurance reserve positive control

Reserve/capital-return bridge validates.

```text
route = KeepStage2_BlockHard4C
```

### 5.10 HDC Hyundai Development / 294870 — delayed 4B

Delayed validation is not immediate Stage2.

```text
route = DelayedLocal4B_DoNotBackfill
```

### 5.11 SM Entertainment / 041510 — high MAE after real tender bridge

The post-resolution drawdown should not erase the fact that formal tender mechanics existed. This is 4B, not 4C.

```text
route = KeepStage2_PostResolution4B
```

### 5.12 KB Financial / 105560 — high-MAE reclassification cap

The capital-return bridge may exist, but the selected C32 lens is wrong. Reclassify instead of hard-blocking the underlying business bridge.

```text
route = Reclassify_C32Cap
```

---

## 6. Score-return alignment

```yaml
new_independent_case_count: 12
calibration_usable_case_count: 12
calibration_usable_trigger_count: 12
positive_control_count: 4
local_4B_or_delayed_watch_count: 4
hard_4C_or_stage2_block_count: 3
reclassification_cap_count: 1
current_profile_error_count: 8
```

| symbol | source | route | 90D MFE/MAE | 180D MFE/MAE | high-MAE lesson |
|---|---:|---:|---:|---:|---|
| 034020 | C04 | local 4B | +17.65 / -28.71 | +17.65 / -28.71 | incomplete project bridge blocks Green |
| 457550 | C04 | hard 4C | +32.06 / -58.25 | +32.06 / -58.25 | supplier heat lacks cash bridge |
| 002380 | C15 | keep Stage2 | +20.49 / -7.79 | +41.39 / -7.79 | material margin bridge validates |
| 006110 | C15 | 4B -> block | +28.34 / -47.55 | +28.34 / -53.58 | material label needs refresh |
| 003230 | C20 | keep Stage2 | +60.81 / 0.00 | +106.05 / 0.00 | sell-through bridge validates |
| 090430 | C20 | hard 4C | +3.24 / -40.32 | +3.24 / -48.76 | brand label fails |
| 005940 | C21 | keep Stage2 | +14.71 / -2.36 | +26.09 / -2.36 | capital-return bridge validates |
| 006800 | C21 | hard 4C | +5.53 / -20.16 | +5.53 / -23.96 | low-PBR label fails |
| 005830 | C22 | keep Stage2 | +27.05 / -9.26 | +30.53 / -9.26 | reserve/capital bridge validates |
| 294870 | C31 | delayed 4B | +37.28 / -6.58 | +57.37 / -6.58 | delayed bridge no backfill |
| 041510 | C32 | Stage2 + 4B | +40.54 / -21.10 | +40.54 / -21.10 | tender bridge survives post-resolution drawdown |
| 105560 | C32 boundary | reclassify | +18.20 / -15.81 | +18.20 / -15.81 | wrong selected archetype, not hard 4C |

---

## 7. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"034020","raw_bridge_quality":2,"raw_accounting_trust":1,"raw_mfe_validation":1,"raw_mae_penalty":4,"raw_label_only_risk":3,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Local4B_NoBackfill"}
{"row_type":"score_simulation","symbol":"457550","raw_bridge_quality":0,"raw_accounting_trust":0,"raw_mfe_validation":1,"raw_mae_penalty":5,"raw_label_only_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C_Stage2FalsePositiveBlock"}
{"row_type":"score_simulation","symbol":"002380","raw_bridge_quality":5,"raw_accounting_trust":5,"raw_mfe_validation":4,"raw_mae_penalty":1,"raw_label_only_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_BlockHard4C"}
{"row_type":"score_simulation","symbol":"006110","raw_bridge_quality":1,"raw_accounting_trust":1,"raw_mfe_validation":2,"raw_mae_penalty":5,"raw_label_only_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Local4BThenBlockIfNoRefresh"}
{"row_type":"score_simulation","symbol":"003230","raw_bridge_quality":5,"raw_accounting_trust":5,"raw_mfe_validation":5,"raw_mae_penalty":0,"raw_label_only_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_BlockHard4C"}
{"row_type":"score_simulation","symbol":"090430","raw_bridge_quality":0,"raw_accounting_trust":0,"raw_mfe_validation":0,"raw_mae_penalty":5,"raw_label_only_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C_Stage2FalsePositiveBlock"}
{"row_type":"score_simulation","symbol":"005940","raw_bridge_quality":5,"raw_accounting_trust":5,"raw_mfe_validation":4,"raw_mae_penalty":0,"raw_label_only_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_BlockHard4C"}
{"row_type":"score_simulation","symbol":"006800","raw_bridge_quality":0,"raw_accounting_trust":0,"raw_mfe_validation":0,"raw_mae_penalty":4,"raw_label_only_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C_Stage2FalsePositiveBlock"}
{"row_type":"score_simulation","symbol":"005830","raw_bridge_quality":5,"raw_accounting_trust":5,"raw_mfe_validation":4,"raw_mae_penalty":1,"raw_label_only_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_BlockHard4C"}
{"row_type":"score_simulation","symbol":"294870","raw_bridge_quality":2,"raw_accounting_trust":1,"raw_mfe_validation":3,"raw_mae_penalty":1,"raw_label_only_risk":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"DelayedLocal4B"}
{"row_type":"score_simulation","symbol":"041510","raw_bridge_quality":5,"raw_accounting_trust":5,"raw_mfe_validation":4,"raw_mae_penalty":3,"raw_label_only_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_PostResolution4B"}
{"row_type":"score_simulation","symbol":"105560","raw_bridge_quality":4,"raw_accounting_trust":3,"raw_mfe_validation":2,"raw_mae_penalty":3,"raw_label_only_risk":1,"raw_wrong_archetype_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Reclassify_C32Cap"}
```

---

## 8. Current calibrated profile stress test

### Existing error risk

The profile can still make two wrong moves:

```text
high MAE everywhere -> hard 4C
```

This would over-block formal tender rows or real margin/capital bridges after post-resolution / cycle drawdown.

```text
high MFE first -> keep Stage2
```

This would over-keep supplier spikes, material labels and brand labels that later fail.

Correct route:

```text
bridge quality first
MAE severity second
archetype ownership third
```

### Rule candidate

```text
R13_HIGH_MAE_BRIDGE_QUALITY_ROUTE_SPLIT_V8

if company_specific_cash_bridge == true
and MFE_90D_pct >= +20
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
    block_hard_4C = true
```

```text
if company_specific_bridge == true
and MAE_90D_pct <= -20
and bridge_refresh_missing == true:
    route = local_4B_watch
    block_stage3_green = true
```

```text
if formal_tender_cash_exit_bridge == true
and post_resolution_MAE == true:
    route = local_4B_watch
    do_not_hard_4C_if_tender_bridge_was_real = true
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
if later_evidence_after_trigger == true:
    do_not_backfill_to_original_trigger = true
```

---

## 9. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
cross_archetype_rule_candidate: true
loop_contribution_label: cross_archetype_high_MAE_guardrail_candidate
new_axis_proposed: R13_HIGH_MAE_BRIDGE_QUALITY_ROUTE_SPLIT_V8
existing_axis_strengthened:
  - bridge_quality_before_MAE_route
  - real_bridge_high_MAE_local_4B
  - label_only_high_MAE_hard_4C
  - formal_tender_post_resolution_4B_not_hard_4C
  - wrong_archetype_high_MAE_reclassification_guard
  - later_evidence_no_backfill_guard
existing_axis_weakened: null
```

---

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this single MD. Batch this R13 high-MAE loop with R13 accounting-trust loop 11, R13 Stage2 false-positive loop 10, R13 4B/4C loop 102, and source loops C04/C15/C20/C21/C22/C31/C32 from this session. Extract `R13_HIGH_MAE_BRIDGE_QUALITY_ROUTE_SPLIT_V8` as a cross-archetype shadow rule. Preserve rows with real cash bridges even when post-resolution or refresh-related MAE appears; hard-block label-only high-MAE rows; reclassify rows whose real bridge belongs to another archetype.
```

---

## 11. Next research state

```yaml
completed_round: R13
completed_loop: 8
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
