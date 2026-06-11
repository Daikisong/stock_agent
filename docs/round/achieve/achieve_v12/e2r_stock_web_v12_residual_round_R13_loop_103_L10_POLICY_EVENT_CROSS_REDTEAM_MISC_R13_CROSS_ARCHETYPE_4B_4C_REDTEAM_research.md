# E2R v12 R13 cross-archetype residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R13
selected_loop: 103
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
fine_archetype_id: CONSUMER_PLATFORM_MOBILITY_CONSTRUCTION_POLICY_LOCAL_4B_VS_HARD_4C_ROUTE_SPLIT
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

R13 is a cross-archetype checkpoint, not a sector-positive discovery round. This file uses the latest current-session C18, C26, C29, C30 and C31 rows and asks one routing question:

```text
Should the row be kept as local 4B, or should it be escalated to hard 4C?
```

The previous local `R13_CROSS_ARCHETYPE_4B_4C_REDTEAM` run reached loop 102. This continuation is `loop 103`.

---

## 1. Research thesis

4B and 4C should not be assigned by price shape alone.

```text
real company-specific bridge + high MFE / later MAE
→ local 4B, bridge refresh required

label-only / price-only spike + high MAE
→ hard 4C or Stage2 false-positive block

true business bridge but wrong selected archetype
→ cap selected archetype and reclassify

delayed price validation after weak trigger
→ local 4B, no backfill to original trigger
```

This loop compares five bridge families:

1. **Consumer export / DTC channel**
   - DTC/device or sell-through bridge can survive.
   - Brand/channel inventory label without repeat order must hard block.

2. **Platform ad operating leverage**
   - Owned platform inventory/ARPU bridge can survive.
   - Adtech/agency label without owned inventory must hard block.
   - Real platform with drawdown requires local 4B.

3. **Mobility operating leverage**
   - OEM mix/margin bridge can survive.
   - Value-up label without operating confirmation should cap.
   - Auto-parts theme blowoff gets local 4B first, then block if no bridge refresh.

4. **Construction / PF policy**
   - Delayed soft-landing can stay local 4B.
   - Weak-liquidity PF relief label should hard block.

5. **Financial policy / Value-up**
   - Bank capital-return bridge can stay local 4B under C31/C21.
   - Low-PBR policy label without differentiated execution should cap.

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 10
  actual_cases: 12
  source_archetypes:
    - C18_CONSUMER_EXPORT_CHANNEL_REORDER
    - C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
    - C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
    - C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
    - C31_POLICY_SUBSIDY_LEGISLATION_EVENT
  price_windows:
    - 30D MFE/MAE
    - 90D MFE/MAE
    - 180D MFE/MAE
  output_use:
    - cross-archetype 4B/4C route split
    - local 4B vs hard 4C separation
    - delayed bridge no-backfill guard
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
  - R5/C18 loop 144
  - R8/C26 loop 101
  - R9/C29 loop 104
  - R10/C30 loop 102
  - R11/C31 loop 104
  - R13 accounting-trust loop 11
  - R13 Stage2 false-positive loop 10
  - R13 high-MAE loop 8
reason:
  - all reused rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - this file changes canonical scope to R13 4B/4C red-team
  - exact source-archetype keys should be deduped separately from this R13 guardrail key
  - no production scoring changed
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":103,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"DTC_EXPORT_VERTICAL_MFE_REAL_BRIDGE_LOCAL_4B","source_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","symbol":"278470","name":"에이피알","trigger_type":"Stage4B","entry_date":"2025-02-27","entry_close":60100,"price_basis":"tradable_raw","MFE_30D_pct":20.63,"MAE_30D_pct":-8.82,"MFE_90D_pct":204.99,"MAE_90D_pct":-8.82,"MFE_180D_pct":365.06,"MAE_180D_pct":-8.82,"calibration_usable":true,"case_role":"real_bridge_vertical_MFE_local_4B","novelty_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|278470|Stage4B|2025-02-27","route":"Local4B_DTCReorderMarginRefresh","guardrail_lesson":"vertical MFE should not become Green automatically; DTC/channel bridge must keep refreshing"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":103,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"BRAND_CHANNEL_INVENTORY_LABEL_HARD_4C","source_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","symbol":"383220","name":"F&F","trigger_type":"Stage4C","entry_date":"2024-07-17","entry_close":74000,"price_basis":"tradable_raw","MFE_30D_pct":3.24,"MAE_30D_pct":-33.99,"MFE_90D_pct":3.24,"MAE_90D_pct":-33.99,"MFE_180D_pct":3.24,"MAE_180D_pct":-33.99,"calibration_usable":true,"case_role":"hard_4C_counterexample","novelty_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|383220|Stage4C|2024-07-17","route":"Hard4C_ChannelInventoryBlock","guardrail_lesson":"brand/export-channel label with low MFE and deep MAE should hard-block without sell-through proof"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":103,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"OWNED_PLATFORM_LOW_MAE_POSITIVE_CONTROL","source_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"035420","name":"NAVER","trigger_type":"Stage2-Actionable","entry_date":"2024-11-08","entry_close":174600,"price_basis":"tradable_raw","MFE_30D_pct":26.00,"MAE_30D_pct":-1.78,"MFE_90D_pct":34.88,"MAE_90D_pct":-1.78,"MFE_180D_pct":34.88,"MAE_180D_pct":-1.78,"forward_high_30d":220000,"forward_low_30d":171500,"forward_high_90d":235500,"forward_low_90d":171500,"forward_high_180d":235500,"forward_low_180d":171500,"calibration_usable":true,"case_role":"positive_control_block_hard_4C","novelty_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|035420|Stage2-Actionable|2024-11-08","route":"KeepStage2_BlockHard4C","guardrail_lesson":"owned platform inventory/ARPU bridge with low MAE should not be downgraded to 4C"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":103,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"LIVE_STREAMING_PLATFORM_HIGH_MAE_LOCAL_4B","source_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"067160","name":"SOOP","trigger_type":"Stage4B","entry_date":"2024-06-20","entry_close":117000,"price_basis":"tradable_raw","MFE_30D_pct":22.91,"MAE_30D_pct":-18.38,"MFE_90D_pct":22.91,"MAE_90D_pct":-26.07,"MFE_180D_pct":22.91,"MAE_180D_pct":-32.82,"forward_high_30d":143800,"forward_low_30d":95500,"forward_high_90d":143800,"forward_low_90d":86500,"forward_high_180d":143800,"forward_low_180d":78600,"calibration_usable":true,"case_role":"real_platform_local_4B","novelty_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|067160|Stage4B|2024-06-20","route":"Local4B_RequireARPUCreatorRetentionRefresh","guardrail_lesson":"real platform bridge with high MAE should stay local 4B until monetization refresh"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":103,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"ADTECH_LABEL_WITHOUT_OWNED_INVENTORY_HARD_4C","source_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"214270","name":"FSN","trigger_type":"Stage4C","entry_date":"2024-07-18","entry_close":2105,"price_basis":"tradable_raw","MFE_30D_pct":16.63,"MAE_30D_pct":-26.37,"MFE_90D_pct":19.00,"MAE_90D_pct":-26.37,"MFE_180D_pct":19.00,"MAE_180D_pct":-49.64,"forward_high_30d":2455,"forward_low_30d":1550,"forward_high_90d":2505,"forward_low_90d":1550,"forward_high_180d":2505,"forward_low_180d":1060,"calibration_usable":true,"case_role":"hard_4C_counterexample","novelty_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|214270|Stage4C|2024-07-18","route":"Hard4C_AdtechLabelBlock","guardrail_lesson":"adtech label without owned inventory/ARPU bridge and high MAE should hard-block"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":103,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"OEM_MIX_MARGIN_LOW_MAE_POSITIVE_CONTROL","source_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"000270","name":"기아","trigger_type":"Stage2-Actionable","entry_date":"2024-01-25","entry_close":93000,"price_basis":"tradable_raw","MFE_30D_pct":41.61,"MAE_30D_pct":-7.42,"MFE_90D_pct":45.16,"MAE_90D_pct":-7.42,"MFE_180D_pct":45.16,"MAE_180D_pct":-7.42,"forward_high_30d":131700,"forward_low_30d":86100,"forward_high_90d":135000,"forward_low_90d":86100,"forward_high_180d":135000,"forward_low_180d":86100,"calibration_usable":true,"case_role":"positive_control_block_hard_4C","novelty_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|000270|Stage2-Actionable|2024-01-25","route":"KeepStage2_BlockHard4C","guardrail_lesson":"OEM volume/mix/margin bridge with controlled MAE should not be routed to hard 4C"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":103,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"OEM_VALUEUP_LABEL_WITHOUT_OPERATING_BRIDGE_CAP","source_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"005380","name":"현대차","trigger_type":"Stage2","entry_date":"2024-08-28","entry_close":259000,"price_basis":"tradable_raw","MFE_30D_pct":3.09,"MAE_30D_pct":-14.48,"MFE_90D_pct":3.09,"MAE_90D_pct":-22.78,"MFE_180D_pct":3.09,"MAE_180D_pct":-32.12,"forward_high_30d":267000,"forward_low_30d":221500,"forward_high_90d":267000,"forward_low_90d":200000,"forward_high_180d":267000,"forward_low_180d":175800,"calibration_usable":true,"case_role":"stage2_cap","novelty_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|005380|Stage2|2024-08-28","route":"Stage2Cap_C29BridgeMissing","guardrail_lesson":"shareholder-return label may belong elsewhere but C29 operating bridge did not validate"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":103,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"AUTO_PARTS_THEME_BLOWOFF_LOCAL_4B_THEN_4C","source_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"010690","name":"화신","trigger_type":"Stage4B","entry_date":"2024-06-12","entry_close":11690,"price_basis":"tradable_raw","MFE_30D_pct":35.93,"MAE_30D_pct":-4.53,"MFE_90D_pct":35.93,"MAE_90D_pct":-30.28,"MFE_180D_pct":35.93,"MAE_180D_pct":-47.39,"forward_high_30d":15890,"forward_low_30d":11160,"forward_high_90d":15890,"forward_low_90d":8150,"forward_high_180d":15890,"forward_low_180d":6150,"calibration_usable":true,"case_role":"local_4B_then_hard_block_if_no_refresh","novelty_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|010690|Stage4B|2024-06-12","route":"Local4BThenHard4CIfNoVolumeMarginRefresh","guardrail_lesson":"theme blowoff may get local 4B, but no durable volume/margin bridge means hard block"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":103,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"PF_POLICY_WEAK_LIQUIDITY_LABEL_HARD_4C","source_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"002990","name":"금호건설","trigger_type":"Stage4C","entry_date":"2024-01-26","entry_close":5030,"price_basis":"tradable_raw","MFE_30D_pct":5.00,"MAE_30D_pct":-4.60,"MFE_90D_pct":5.00,"MAE_90D_pct":-27.50,"MFE_180D_pct":5.00,"MAE_180D_pct":-41.00,"forward_high_30d":5280,"forward_low_30d":4800,"forward_high_90d":5280,"forward_low_90d":3650,"forward_high_180d":5280,"forward_low_180d":2970,"calibration_usable":true,"case_role":"hard_4C_counterexample","novelty_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|002990|Stage4C|2024-01-26","route":"Hard4C_WeakLiquidityBlock","guardrail_lesson":"PF relief label without liquidity/cash bridge and deep MAE should hard-block"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":103,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"PF_POLICY_DELAYED_REBOUND_LOCAL_4B_NO_BACKFILL","source_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"294870","name":"HDC현대산업개발","trigger_type":"Stage4B","entry_date":"2024-05-13","entry_close":17920,"price_basis":"tradable_raw","MFE_30D_pct":2.12,"MAE_30D_pct":-6.58,"MFE_90D_pct":37.28,"MAE_90D_pct":-6.58,"MFE_180D_pct":57.37,"MAE_180D_pct":-6.58,"forward_high_30d":18300,"forward_low_30d":16740,"forward_high_90d":24600,"forward_low_90d":16740,"forward_high_180d":28200,"forward_low_180d":16740,"calibration_usable":true,"case_role":"delayed_local_4B","novelty_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|294870|Stage4B|2024-05-13","route":"DelayedLocal4B_NoBackfill","guardrail_lesson":"later PF/housing validation can stay 4B, but original trigger should not be upgraded retroactively"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":103,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"BANK_POLICY_CAPITAL_RETURN_LOCAL_4B_WRONG_FOR_TENDER","source_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"105560","name":"KB금융","trigger_type":"Stage4B","entry_date":"2024-07-26","entry_close":87900,"price_basis":"tradable_raw","MFE_30D_pct":5.12,"MAE_30D_pct":-15.81,"MFE_90D_pct":18.20,"MAE_90D_pct":-15.81,"MFE_180D_pct":18.20,"MAE_180D_pct":-15.81,"forward_high_30d":92400,"forward_low_30d":74000,"forward_high_90d":103900,"forward_low_90d":74000,"forward_high_180d":103900,"forward_low_180d":74000,"calibration_usable":true,"case_role":"policy_capital_return_local_4B_reclassification","novelty_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|105560|Stage4B|2024-07-26","route":"Local4B_ReclassifyToC21C31","guardrail_lesson":"capital-return bridge may be real, but it is not tender mechanics; keep 4B in the correct archetype"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":103,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"LOW_PBR_BANK_POLICY_LABEL_CAP","source_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"316140","name":"우리금융지주","trigger_type":"Stage2","entry_date":"2024-07-26","entry_close":16180,"price_basis":"tradable_raw","MFE_30D_pct":4.08,"MAE_30D_pct":-15.08,"MFE_90D_pct":5.69,"MAE_90D_pct":-15.08,"MFE_180D_pct":5.69,"MAE_180D_pct":-15.08,"forward_high_30d":16840,"forward_low_30d":13740,"forward_high_90d":17100,"forward_low_90d":13740,"forward_high_180d":17100,"forward_low_180d":13740,"calibration_usable":true,"case_role":"stage2_cap","novelty_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|316140|Stage2|2024-07-26","route":"Stage2Cap_LowPBRPolicyBridgeMissing","guardrail_lesson":"low-PBR policy label without differentiated execution should cap rather than hard 4C if MAE is not severe"}
```

---

## 5. Case analysis

### 5.1 APR / 278470 — vertical positive, but local 4B

The bridge was real enough to avoid 4C, but vertical rerating still requires reorder and margin refresh.

```text
route = Local4B_DTCReorderMarginRefresh
```

### 5.2 F&F / 383220 — hard 4C

Brand/channel inventory label failed.

```text
route = Hard4C_ChannelInventoryBlock
```

### 5.3 NAVER / 035420 — positive control

Owned platform bridge survived.

```text
route = KeepStage2_BlockHard4C
```

### 5.4 SOOP / 067160 — real bridge, high MAE 4B

Live-streaming platform bridge was real but unrefreshed.

```text
route = Local4B_RequireARPUCreatorRetentionRefresh
```

### 5.5 FSN / 214270 — hard 4C

Adtech vocabulary lacked owned inventory and margin leverage.

```text
route = Hard4C_AdtechLabelBlock
```

### 5.6 Kia / 000270 — OEM positive control

OEM mix and margin bridge validated.

```text
route = KeepStage2_BlockHard4C
```

### 5.7 Hyundai Motor / 005380 — Stage2 cap

Shareholder-return intent exists, but C29 operating bridge did not validate.

```text
route = Stage2Cap_C29BridgeMissing
```

### 5.8 Hwashin / 010690 — 4B then 4C if no refresh

Auto-parts theme got early MFE but failed durability.

```text
route = Local4BThenHard4CIfNoVolumeMarginRefresh
```

### 5.9 Kumho E&C / 002990 — hard 4C

PF relief label failed the liquidity/cash bridge test.

```text
route = Hard4C_WeakLiquidityBlock
```

### 5.10 HDC Hyundai Development / 294870 — delayed 4B

Later validation exists, but immediate trigger upgrade is forbidden.

```text
route = DelayedLocal4B_NoBackfill
```

### 5.11 KB Financial / 105560 — local 4B in the right archetype

Capital-return bridge may stay under C21/C31, not C32 tender mechanics.

```text
route = Local4B_ReclassifyToC21C31
```

### 5.12 Woori Financial / 316140 — cap, not hard block

Low-PBR policy label was weak but not severe enough for hard 4C in this row.

```text
route = Stage2Cap_LowPBRPolicyBridgeMissing
```

---

## 6. Score-return alignment

```yaml
new_independent_case_count: 12
calibration_usable_case_count: 12
calibration_usable_trigger_count: 12
positive_control_count: 3
local_4B_count: 5
hard_4C_count: 3
stage2_cap_or_reclassification_count: 3
current_profile_error_count: 8
```

| symbol | source | route | 90D MFE/MAE | 180D MFE/MAE | route lesson |
|---|---:|---:|---:|---:|---|
| 278470 | C18 | local 4B | +204.99 / -8.82 | +365.06 / -8.82 | vertical bridge needs refresh |
| 383220 | C18 | hard 4C | +3.24 / -33.99 | +3.24 / -33.99 | brand label fails |
| 035420 | C26 | keep Stage2 | +34.88 / -1.78 | +34.88 / -1.78 | owned platform bridge |
| 067160 | C26 | local 4B | +22.91 / -26.07 | +22.91 / -32.82 | real platform, unrefreshed |
| 214270 | C26 | hard 4C | +19.00 / -26.37 | +19.00 / -49.64 | adtech label fails |
| 000270 | C29 | keep Stage2 | +45.16 / -7.42 | +45.16 / -7.42 | OEM margin bridge |
| 005380 | C29 | cap | +3.09 / -22.78 | +3.09 / -32.12 | value-up label lacks C29 bridge |
| 010690 | C29 | 4B -> 4C | +35.93 / -30.28 | +35.93 / -47.39 | theme blowoff lacks durability |
| 002990 | C30/C31 | hard 4C | +5.00 / -27.50 | +5.00 / -41.00 | weak liquidity label fails |
| 294870 | C30/C31 | delayed 4B | +37.28 / -6.58 | +57.37 / -6.58 | no backfill |
| 105560 | C31 | local 4B/reclassify | +18.20 / -15.81 | +18.20 / -15.81 | real bridge belongs elsewhere |
| 316140 | C31 | cap | +5.69 / -15.08 | +5.69 / -15.08 | weak policy label cap |

---

## 7. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"278470","raw_bridge_quality":5,"raw_accounting_trust":4,"raw_mfe_validation":5,"raw_mae_penalty":1,"raw_label_only_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Local4B_DTCReorderMarginRefresh"}
{"row_type":"score_simulation","symbol":"383220","raw_bridge_quality":0,"raw_accounting_trust":0,"raw_mfe_validation":0,"raw_mae_penalty":5,"raw_label_only_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C_ChannelInventoryBlock"}
{"row_type":"score_simulation","symbol":"035420","raw_bridge_quality":5,"raw_accounting_trust":5,"raw_mfe_validation":4,"raw_mae_penalty":0,"raw_label_only_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_BlockHard4C"}
{"row_type":"score_simulation","symbol":"067160","raw_bridge_quality":4,"raw_accounting_trust":3,"raw_mfe_validation":3,"raw_mae_penalty":4,"raw_label_only_risk":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Local4B_RequireMonetizationRefresh"}
{"row_type":"score_simulation","symbol":"214270","raw_bridge_quality":0,"raw_accounting_trust":0,"raw_mfe_validation":1,"raw_mae_penalty":5,"raw_label_only_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C_AdtechLabelBlock"}
{"row_type":"score_simulation","symbol":"000270","raw_bridge_quality":5,"raw_accounting_trust":5,"raw_mfe_validation":5,"raw_mae_penalty":1,"raw_label_only_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_BlockHard4C"}
{"row_type":"score_simulation","symbol":"005380","raw_bridge_quality":1,"raw_accounting_trust":1,"raw_mfe_validation":0,"raw_mae_penalty":4,"raw_label_only_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2Cap_C29BridgeMissing"}
{"row_type":"score_simulation","symbol":"010690","raw_bridge_quality":1,"raw_accounting_trust":1,"raw_mfe_validation":2,"raw_mae_penalty":5,"raw_label_only_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Local4BThenHard4CIfNoRefresh"}
{"row_type":"score_simulation","symbol":"002990","raw_bridge_quality":0,"raw_accounting_trust":0,"raw_mfe_validation":0,"raw_mae_penalty":5,"raw_label_only_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C_WeakLiquidityBlock"}
{"row_type":"score_simulation","symbol":"294870","raw_bridge_quality":2,"raw_accounting_trust":1,"raw_mfe_validation":3,"raw_mae_penalty":1,"raw_label_only_risk":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"DelayedLocal4B_NoBackfill"}
{"row_type":"score_simulation","symbol":"105560","raw_bridge_quality":4,"raw_accounting_trust":3,"raw_mfe_validation":2,"raw_mae_penalty":3,"raw_label_only_risk":1,"raw_wrong_archetype_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Local4B_ReclassifyToC21C31"}
{"row_type":"score_simulation","symbol":"316140","raw_bridge_quality":1,"raw_accounting_trust":1,"raw_mfe_validation":0,"raw_mae_penalty":3,"raw_label_only_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2Cap_LowPBRPolicyBridgeMissing"}
```

---

## 8. Current calibrated profile stress test

### Existing error risk

The current profile can still confuse:

```text
good 4B
bad 4B
hard 4C
```

The correct split is:

```text
good 4B = real bridge, but refresh needed
bad 4B = price-only spike waiting to become 4C
hard 4C = label-only / no bridge / severe MAE
```

A 4B row is the inspection bay. A 4C row is the scrap yard. The model must not park broken machinery in the inspection bay forever.

### Rule candidate

```text
R13_4B_4C_REFRESH_OR_BLOCK_GATE_V103

if company_specific_bridge == true
and MFE_90D_pct >= +20
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
    block_hard_4C = true
```

```text
if company_specific_bridge == true
and MFE_90D_pct >= +20
and MAE_90D_pct <= -20:
    route = local_4B_watch
    block_stage3_green = true
    require_bridge_refresh = true
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
if MFE_30D_pct < +5
and MFE_90D_pct >= +25:
    route = delayed_local_4B
    do_not_backfill_as_immediate_Stage2 = true
```

---

## 9. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
cross_archetype_rule_candidate: true
loop_contribution_label: cross_archetype_4B_4C_redteam_guardrail_candidate
new_axis_proposed: R13_4B_4C_REFRESH_OR_BLOCK_GATE_V103
existing_axis_strengthened:
  - local_4B_requires_real_bridge
  - high_MFE_high_MAE_requires_bridge_refresh
  - label_only_high_MAE_hard_4C
  - wrong_archetype_reclassification_cap
  - delayed_rebound_no_backfill
existing_axis_weakened: null
```

---

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this single MD. Batch this R13 4B/4C loop with R13 accounting-trust loop 11, R13 Stage2 false-positive loop 10, R13 high-MAE loop 8, and source loops C18/C26/C29/C30/C31 from this session. Extract `R13_4B_4C_REFRESH_OR_BLOCK_GATE_V103` as a cross-archetype shadow rule. Keep real but unrefreshed bridges in local 4B, hard-block label-only high-MAE rows, and reclassify rows whose real bridge belongs to another archetype.
```

---

## 11. Next research state

```yaml
completed_round: R13
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
  - C31_POLICY_SUBSIDY_LEGISLATION_EVENT
```
