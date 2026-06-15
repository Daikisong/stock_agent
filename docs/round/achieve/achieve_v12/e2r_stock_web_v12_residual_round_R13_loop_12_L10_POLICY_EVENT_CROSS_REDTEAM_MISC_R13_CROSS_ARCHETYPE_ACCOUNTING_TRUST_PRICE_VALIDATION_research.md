# E2R v12 R13 cross-archetype residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R13
selected_loop: 12
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
fine_archetype_id: CONSUMER_PLATFORM_MOBILITY_PF_POLICY_LABEL_TO_OPERATING_CASH_BRIDGE_VALIDATION
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

R13 is a cross-archetype checkpoint, not a sector-specific positive discovery round. This file uses the latest current-session C18, C26, C29, C30 and C31 rows and asks the accounting-trust question:

```text
Did the label become a company-specific operating cash bridge at the trigger date?
```

The previous local `R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION` run reached loop 11. This continuation is therefore `loop 12`.

---

## 1. Research thesis

Accounting trust is the border between narrative and ledger.

```text
consumer export label
→ must become sell-through, reorder, inventory quality, margin and cash

platform label
→ must become owned inventory, ARPU, retention, conversion and margin leverage

mobility label
→ must become volume, mix, ASP, customer order, utilization and margin

PF / housing policy label
→ must become refinancing, guarantee relief, presale, debt-service or cash conversion

financial policy / Value-up label
→ must become CET1, payout, buyback, ROE, credit-cost or capital-return execution
```

This loop deliberately mixes strong positives, local 4B candidates, hard 4C counterexamples and wrong-archetype caps. The goal is not to crown winners. The goal is to keep the gate honest.

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
    - cross-archetype accounting-trust validation
    - Stage2 false-positive prevention
    - 4B/4C refresh-or-block routing
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
  - R13 Stage2 false-positive loop 10
  - R13 high-MAE loop 8
  - R13 4B/4C loop 103
reason:
  - all rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - current file changes canonical scope to R13 accounting-trust validation
  - exact source-archetype keys should be deduped separately from this R13 guardrail key
  - no production scoring changed
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":12,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"DTC_EXPORT_REORDER_MARGIN_ACCOUNTING_TRUST_VALIDATED_BUT_VERTICAL_4B","source_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","symbol":"278470","name":"에이피알","trigger_type":"Stage4B","entry_date":"2025-02-27","entry_close":60100,"price_basis":"tradable_raw","mfe_30d_pct":20.63,"mae_30d_pct":-8.82,"mfe_90d_pct":204.99,"mae_90d_pct":-8.82,"mfe_180d_pct":365.06,"mae_180d_pct":-8.82,"calibration_usable":true,"case_role":"accounting_trust_validated_vertical_4B","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|278470|Stage4B|2025-02-27","accounting_bridge":"DTC/device global channel expansion, overseas demand, revenue and reorder bridge","route":"Local4B_DTCReorderMarginRefresh"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":12,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"BRAND_CHANNEL_INVENTORY_LABEL_ACCOUNTING_TRUST_ABSENT_BLOCK","source_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","symbol":"383220","name":"F&F","trigger_type":"Stage4C","entry_date":"2024-07-17","entry_close":74000,"price_basis":"tradable_raw","mfe_30d_pct":3.24,"mae_30d_pct":-33.99,"mfe_90d_pct":3.24,"mae_90d_pct":-33.99,"mfe_180d_pct":3.24,"mae_180d_pct":-33.99,"calibration_usable":true,"case_role":"accounting_trust_absent_hard_block","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|383220|Stage4C|2024-07-17","accounting_bridge":"brand/export-channel label without sell-through, inventory normalization or reorder proof","route":"Hard4C_ChannelInventoryBlock"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":12,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"OWNED_PLATFORM_ARPU_MARGIN_ACCOUNTING_TRUST_VALIDATED","source_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"035420","name":"NAVER","trigger_type":"Stage2-Actionable","entry_date":"2024-11-08","entry_close":174600,"price_basis":"tradable_raw","mfe_30d_pct":26.00,"mae_30d_pct":-1.78,"mfe_90d_pct":34.88,"mae_90d_pct":-1.78,"mfe_180d_pct":34.88,"mae_180d_pct":-1.78,"forward_high_30d":220000,"forward_low_30d":171500,"forward_high_90d":235500,"forward_low_90d":171500,"forward_high_180d":235500,"forward_low_180d":171500,"calibration_usable":true,"case_role":"accounting_trust_validated","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|035420|Stage2-Actionable|2024-11-08","accounting_bridge":"owned search/commerce platform ad inventory, ARPU, conversion and margin leverage","route":"KeepStage2_OwnedPlatformBridge"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":12,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"LIVE_PLATFORM_MONETIZATION_UNREFRESHED_LOCAL_4B","source_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"067160","name":"SOOP","trigger_type":"Stage4B","entry_date":"2024-06-20","entry_close":117000,"price_basis":"tradable_raw","mfe_30d_pct":22.91,"mae_30d_pct":-18.38,"mfe_90d_pct":22.91,"mae_90d_pct":-26.07,"mfe_180d_pct":22.91,"mae_180d_pct":-32.82,"forward_high_30d":143800,"forward_low_30d":95500,"forward_high_90d":143800,"forward_low_90d":86500,"forward_high_180d":143800,"forward_low_180d":78600,"calibration_usable":true,"case_role":"accounting_trust_unrefreshed_local_4B","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|067160|Stage4B|2024-06-20","accounting_bridge":"owned live-streaming platform, rebrand/global expansion and creator-viewer monetization bridge, but refresh missing after high MAE","route":"Local4B_RequireARPUCreatorRetentionRefresh"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":12,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"ADTECH_LABEL_NO_OWNED_INVENTORY_ACCOUNTING_TRUST_BLOCK","source_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"214270","name":"FSN","trigger_type":"Stage4C","entry_date":"2024-07-18","entry_close":2105,"price_basis":"tradable_raw","mfe_30d_pct":16.63,"mae_30d_pct":-26.37,"mfe_90d_pct":19.00,"mae_90d_pct":-26.37,"mfe_180d_pct":19.00,"mae_180d_pct":-49.64,"forward_high_30d":2455,"forward_low_30d":1550,"forward_high_90d":2505,"forward_low_90d":1550,"forward_high_180d":2505,"forward_low_180d":1060,"calibration_usable":true,"case_role":"accounting_trust_absent_hard_block","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|214270|Stage4C|2024-07-18","accounting_bridge":"adtech/marketing service label without owned ad inventory, ARPU, retention, take-rate or durable margin bridge","route":"Hard4C_AdtechLabelBlock"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":12,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"OEM_MIX_MARGIN_ACCOUNTING_TRUST_VALIDATED","source_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"000270","name":"기아","trigger_type":"Stage2-Actionable","entry_date":"2024-01-25","entry_close":93000,"price_basis":"tradable_raw","mfe_30d_pct":41.61,"mae_30d_pct":-7.42,"mfe_90d_pct":45.16,"mae_90d_pct":-7.42,"mfe_180d_pct":45.16,"mae_180d_pct":-7.42,"forward_high_30d":131700,"forward_low_30d":86100,"forward_high_90d":135000,"forward_low_90d":86100,"forward_high_180d":135000,"forward_low_180d":86100,"calibration_usable":true,"case_role":"accounting_trust_validated","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|000270|Stage2-Actionable|2024-01-25","accounting_bridge":"OEM volume, mix, ASP, margin and shareholder-return bridge","route":"KeepStage2_OEMMarginBridge"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":12,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"OEM_VALUEUP_LABEL_WITHOUT_C29_ACCOUNTING_BRIDGE_CAP","source_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"005380","name":"현대차","trigger_type":"Stage2","entry_date":"2024-08-28","entry_close":259000,"price_basis":"tradable_raw","mfe_30d_pct":3.09,"mae_30d_pct":-14.48,"mfe_90d_pct":3.09,"mae_90d_pct":-22.78,"mfe_180d_pct":3.09,"mae_180d_pct":-32.12,"forward_high_30d":267000,"forward_low_30d":221500,"forward_high_90d":267000,"forward_low_90d":200000,"forward_high_180d":267000,"forward_low_180d":175800,"calibration_usable":true,"case_role":"accounting_trust_absent_stage2_cap","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|005380|Stage2|2024-08-28","accounting_bridge":"shareholder-return intent existed, but C29 volume/mix/margin operating bridge did not validate","route":"Stage2Cap_C29BridgeMissing"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":12,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"AUTO_PARTS_THEME_NO_DURABLE_ACCOUNTING_BRIDGE_4B_TO_4C","source_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"010690","name":"화신","trigger_type":"Stage4B","entry_date":"2024-06-12","entry_close":11690,"price_basis":"tradable_raw","mfe_30d_pct":35.93,"mae_30d_pct":-4.53,"mfe_90d_pct":35.93,"mae_90d_pct":-30.28,"mfe_180d_pct":35.93,"mae_180d_pct":-47.39,"forward_high_30d":15890,"forward_low_30d":11160,"forward_high_90d":15890,"forward_low_90d":8150,"forward_high_180d":15890,"forward_low_180d":6150,"calibration_usable":true,"case_role":"accounting_trust_unrefreshed_4B_to_4C","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|010690|Stage4B|2024-06-12","accounting_bridge":"auto-parts theme/volume label without durable customer-volume or margin bridge; vertical MFE followed by deep MAE","route":"Local4BThenHard4CIfNoVolumeMarginRefresh"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":12,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"PF_POLICY_WEAK_LIQUIDITY_ACCOUNTING_TRUST_ABSENT_BLOCK","source_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"002990","name":"금호건설","trigger_type":"Stage4C","entry_date":"2024-01-26","entry_close":5030,"price_basis":"tradable_raw","mfe_30d_pct":5.00,"mae_30d_pct":-4.60,"mfe_90d_pct":5.00,"mae_90d_pct":-27.50,"mfe_180d_pct":5.00,"mae_180d_pct":-41.00,"forward_high_30d":5280,"forward_low_30d":4800,"forward_high_90d":5280,"forward_low_90d":3650,"forward_high_180d":5280,"forward_low_180d":2970,"calibration_usable":true,"case_role":"accounting_trust_absent_hard_block","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|002990|Stage4C|2024-01-26","accounting_bridge":"PF relief vocabulary without liquidity, debt-service, margin, guarantee relief or cash bridge","route":"Hard4C_WeakLiquidityBlock"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":12,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"PF_POLICY_DELAYED_ACCOUNTING_BRIDGE_NO_BACKFILL","source_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"294870","name":"HDC현대산업개발","trigger_type":"Stage4B","entry_date":"2024-05-13","entry_close":17920,"price_basis":"tradable_raw","mfe_30d_pct":2.12,"mae_30d_pct":-6.58,"mfe_90d_pct":37.28,"mae_90d_pct":-6.58,"mfe_180d_pct":57.37,"mae_180d_pct":-6.58,"forward_high_30d":18300,"forward_low_30d":16740,"forward_high_90d":24600,"forward_low_90d":16740,"forward_high_180d":28200,"forward_low_180d":16740,"calibration_usable":true,"case_role":"accounting_trust_delayed_local_4B","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|294870|Stage4B|2024-05-13","accounting_bridge":"housing/PF soft-landing path helped later, but issuer-specific refinancing/liquidity bridge was not visible at entry","route":"DelayedLocal4B_NoBackfill"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":12,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"BANK_POLICY_CAPITAL_RETURN_ACCOUNTING_BRIDGE_RECLASSIFICATION_4B","source_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"105560","name":"KB금융","trigger_type":"Stage4B","entry_date":"2024-07-26","entry_close":87900,"price_basis":"tradable_raw","mfe_30d_pct":5.12,"mae_30d_pct":-15.81,"mfe_90d_pct":18.20,"mae_90d_pct":-15.81,"mfe_180d_pct":18.20,"mae_180d_pct":-15.81,"forward_high_30d":92400,"forward_low_30d":74000,"forward_high_90d":103900,"forward_low_90d":74000,"forward_high_180d":103900,"forward_low_180d":74000,"calibration_usable":true,"case_role":"accounting_trust_real_but_archetype_specific_4B","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|105560|Stage4B|2024-07-26","accounting_bridge":"bank Value-up/capital-return bridge may be real, but must remain in the financial/policy archetype and needs refresh","route":"Local4B_ReclassifyToC21C31"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":12,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"LOW_PBR_BANK_POLICY_LABEL_ACCOUNTING_BRIDGE_MISSING_CAP","source_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"316140","name":"우리금융지주","trigger_type":"Stage2","entry_date":"2024-07-26","entry_close":16180,"price_basis":"tradable_raw","mfe_30d_pct":4.08,"mae_30d_pct":-15.08,"mfe_90d_pct":5.69,"mae_90d_pct":-15.08,"mfe_180d_pct":5.69,"mae_180d_pct":-15.08,"forward_high_30d":16840,"forward_low_30d":13740,"forward_high_90d":17100,"forward_low_90d":13740,"forward_high_180d":17100,"forward_low_180d":13740,"calibration_usable":true,"case_role":"accounting_trust_missing_stage2_cap","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|316140|Stage2|2024-07-26","accounting_bridge":"low-PBR bank policy label without sufficiently differentiated payout, buyback, CET1 or ROE execution bridge","route":"Stage2Cap_LowPBRPolicyBridgeMissing"}
```

---

## 5. Case analysis

### 5.1 APR / 278470 — accounting bridge validated, but vertical 4B

The DTC/device channel bridge is real, but the vertical rerating needs repeat-order and margin refresh.

```text
route = Local4B_DTCReorderMarginRefresh
```

### 5.2 F&F / 383220 — accounting trust absent

Brand/channel label did not become sell-through or inventory normalization.

```text
route = Hard4C_ChannelInventoryBlock
```

### 5.3 NAVER / 035420 — owned-platform accounting trust

Owned inventory, ARPU, conversion and margin bridge validate Stage2.

```text
route = KeepStage2_OwnedPlatformBridge
```

### 5.4 SOOP / 067160 — real bridge, unrefreshed

The platform bridge exists, but high MAE requires ARPU/retention refresh.

```text
route = Local4B_RequireARPUCreatorRetentionRefresh
```

### 5.5 FSN / 214270 — adtech label block

Adtech vocabulary did not reach owned-inventory accounting trust.

```text
route = Hard4C_AdtechLabelBlock
```

### 5.6 Kia / 000270 — OEM bridge validates

Volume/mix/margin bridge validates.

```text
route = KeepStage2_OEMMarginBridge
```

### 5.7 Hyundai Motor / 005380 — Value-up label without C29 bridge

Shareholder-return label did not validate the C29 operating bridge.

```text
route = Stage2Cap_C29BridgeMissing
```

### 5.8 Hwashin / 010690 — theme bridge unrefreshed

Theme MFE came first, but durable accounting trust failed.

```text
route = Local4BThenHard4CIfNoVolumeMarginRefresh
```

### 5.9 Kumho E&C / 002990 — PF relief label block

PF relief vocabulary lacked issuer-specific cash bridge.

```text
route = Hard4C_WeakLiquidityBlock
```

### 5.10 HDC Hyundai Development / 294870 — delayed bridge, no backfill

Later validation does not upgrade the entry-date evidence.

```text
route = DelayedLocal4B_NoBackfill
```

### 5.11 KB Financial / 105560 — real bridge, correct room needed

Capital-return bridge may be real, but it belongs in C21/C31 and needs refresh.

```text
route = Local4B_ReclassifyToC21C31
```

### 5.12 Woori Financial / 316140 — weak policy label cap

Low-PBR policy label is not enough.

```text
route = Stage2Cap_LowPBRPolicyBridgeMissing
```

---

## 6. Score-return alignment

```yaml
new_independent_case_count: 12
calibration_usable_case_count: 12
calibration_usable_trigger_count: 12
accounting_trust_validated_count: 3
local_4B_or_delayed_count: 5
stage2_false_positive_or_4C_count: 3
stage2_cap_or_reclassification_count: 3
current_profile_error_count: 8
```

| symbol | source | route | 90D MFE/MAE | 180D MFE/MAE | accounting lesson |
|---|---:|---:|---:|---:|---|
| 278470 | C18 | local 4B | +204.99 / -8.82 | +365.06 / -8.82 | DTC bridge real but refresh needed |
| 383220 | C18 | hard 4C | +3.24 / -33.99 | +3.24 / -33.99 | brand label lacks bridge |
| 035420 | C26 | keep Stage2 | +34.88 / -1.78 | +34.88 / -1.78 | owned platform bridge validates |
| 067160 | C26 | local 4B | +22.91 / -26.07 | +22.91 / -32.82 | platform bridge needs monetization refresh |
| 214270 | C26 | hard 4C | +19.00 / -26.37 | +19.00 / -49.64 | adtech label lacks owned inventory |
| 000270 | C29 | keep Stage2 | +45.16 / -7.42 | +45.16 / -7.42 | OEM mix/margin bridge validates |
| 005380 | C29 | cap | +3.09 / -22.78 | +3.09 / -32.12 | Value-up label lacks C29 bridge |
| 010690 | C29 | 4B -> 4C | +35.93 / -30.28 | +35.93 / -47.39 | theme bridge failed durability |
| 002990 | C30 | hard 4C | +5.00 / -27.50 | +5.00 / -41.00 | PF relief lacks liquidity bridge |
| 294870 | C31 | delayed 4B | +37.28 / -6.58 | +57.37 / -6.58 | no backfill |
| 105560 | C31 | local 4B/reclassify | +18.20 / -15.81 | +18.20 / -15.81 | real bridge belongs in C21/C31 |
| 316140 | C31 | cap | +5.69 / -15.08 | +5.69 / -15.08 | low-PBR label lacks execution |

---

## 7. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"278470","raw_label_signal":2,"raw_company_specific_cash_bridge":5,"raw_accounting_trust":4,"raw_price_validation":5,"raw_false_positive_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Local4B_DTCRefresh"}
{"row_type":"score_simulation","symbol":"383220","raw_label_signal":4,"raw_company_specific_cash_bridge":0,"raw_accounting_trust":0,"raw_price_validation":0,"raw_false_positive_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C"}
{"row_type":"score_simulation","symbol":"035420","raw_label_signal":2,"raw_company_specific_cash_bridge":5,"raw_accounting_trust":5,"raw_price_validation":4,"raw_false_positive_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2"}
{"row_type":"score_simulation","symbol":"067160","raw_label_signal":2,"raw_company_specific_cash_bridge":4,"raw_accounting_trust":3,"raw_price_validation":2,"raw_false_positive_risk":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Local4B"}
{"row_type":"score_simulation","symbol":"214270","raw_label_signal":4,"raw_company_specific_cash_bridge":0,"raw_accounting_trust":0,"raw_price_validation":1,"raw_false_positive_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C"}
{"row_type":"score_simulation","symbol":"000270","raw_label_signal":2,"raw_company_specific_cash_bridge":5,"raw_accounting_trust":5,"raw_price_validation":5,"raw_false_positive_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2"}
{"row_type":"score_simulation","symbol":"005380","raw_label_signal":4,"raw_company_specific_cash_bridge":1,"raw_accounting_trust":1,"raw_price_validation":0,"raw_false_positive_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2Cap"}
{"row_type":"score_simulation","symbol":"010690","raw_label_signal":4,"raw_company_specific_cash_bridge":1,"raw_accounting_trust":1,"raw_price_validation":2,"raw_false_positive_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"4BThen4C"}
{"row_type":"score_simulation","symbol":"002990","raw_label_signal":4,"raw_company_specific_cash_bridge":0,"raw_accounting_trust":0,"raw_price_validation":0,"raw_false_positive_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C"}
{"row_type":"score_simulation","symbol":"294870","raw_label_signal":3,"raw_company_specific_cash_bridge":2,"raw_accounting_trust":1,"raw_price_validation":3,"raw_false_positive_risk":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Delayed4B"}
{"row_type":"score_simulation","symbol":"105560","raw_label_signal":3,"raw_company_specific_cash_bridge":4,"raw_accounting_trust":3,"raw_price_validation":2,"raw_false_positive_risk":1,"raw_reclassification_need":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Local4B_Reclassify"}
{"row_type":"score_simulation","symbol":"316140","raw_label_signal":4,"raw_company_specific_cash_bridge":1,"raw_accounting_trust":1,"raw_price_validation":0,"raw_false_positive_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2Cap"}
```

---

## 8. Current calibrated profile stress test

### Existing error risk

The current profile can still let the same word pass in one sector and fail in another without asking the common question:

```text
Where is the cash bridge?
```

A bridge is valid only if the company can walk across it.

### Rule candidate

```text
R13_ACCOUNTING_TRUST_OPERATING_CASH_BRIDGE_GATE_V12

if trigger_label_exists == true
and company_specific_operating_or_financial_cash_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if company_specific_operating_or_financial_cash_bridge == true
and MFE_90D_pct >= +20
and MAE_90D_pct > -10:
    accounting_trust_validated = true
    keep_stage2_actionable_bonus = true
```

```text
if bridge_exists_but_refresh_missing == true
and MAE_90D_pct <= -20:
    route = local_4B_watch
    block_stage3_green = true
```

```text
if label_only == true
and MAE_90D_pct <= -25:
    route = hard_4C_or_Stage2_FalsePositive_Block
```

```text
if bridge_belongs_to_other_archetype == true:
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
loop_contribution_label: cross_archetype_accounting_trust_operating_cash_bridge_candidate
new_axis_proposed: R13_ACCOUNTING_TRUST_OPERATING_CASH_BRIDGE_GATE_V12
existing_axis_strengthened:
  - company_specific_cash_bridge_required
  - real_bridge_local_4B_until_refresh
  - label_only_high_MAE_hard_4C
  - wrong_archetype_reclassification_guard
  - delayed_rebound_no_backfill
existing_axis_weakened: null
```

---

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this single MD. Batch this R13 accounting-trust loop with R13 loops 8/10/103 and source loops C18/C26/C29/C30/C31 from this session. Extract `R13_ACCOUNTING_TRUST_OPERATING_CASH_BRIDGE_GATE_V12` as a cross-archetype shadow rule. Preserve rows where company-specific cash bridge is visible, route unrefreshed bridges to local 4B, hard-block label-only rows, reclassify wrong-archetype bridges, and prevent delayed validation from being backfilled into the original trigger.
```

---

## 11. Next research state

```yaml
completed_round: R13
completed_loop: 12
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
