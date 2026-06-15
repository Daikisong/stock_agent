# E2R v12 R13 cross-archetype residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R13
selected_loop: 10
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
fine_archetype_id: CONSUMER_PLATFORM_MOBILITY_CONSTRUCTION_OPERATING_CASH_BRIDGE_VALIDATION
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
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

R13 is a cross-archetype checkpoint, not a sector-positive discovery round. This loop compares recent C18, C26, C29 and C30 outputs through the same accounting-trust question:

```text
Did the story enter the company’s accounts as sell-through, reorder, ARPU, margin, utilization, order, working capital or cash?
```

The previous local `R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION` run reached loop 9. This continuation is `loop 10`.

---

## 1. Research thesis

Accounting trust is the difference between a label and a cash machine.

```text
consumer export label
→ must become sell-through, reorder and margin

platform label
→ must become owned inventory, ARPU, conversion, retention and margin leverage

mobility label
→ must become volume, mix, utilization, customer order and margin

construction / EPC / PF label
→ must become project margin, receivable, refinancing, guarantee relief or cash conversion
```

The price path then decides whether the bridge was accepted, still under inspection, or rejected.

This loop splits eight routes:

1. **Consumer export sell-through positive-control** — keep Stage2.
2. **Legacy brand/channel label decay** — cap or block until non-China sell-through and margin return.
3. **Owned-platform ARPU operating-leverage positive-control** — keep Stage2.
4. **Adtech/marketing-service label** — block when there is no owned ad inventory.
5. **OEM mobility mix/margin positive-control** — keep Stage2.
6. **Auto-parts theme blowoff** — local 4B, then block without customer-volume/margin refresh.
7. **Construction delayed rebound** — delayed local 4B, do not backfill immediate Stage2.
8. **Large-builder/support label false positive** — hard block without margin/cash/PF bridge.

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 8
  actual_cases: 8
  source_archetypes:
    - C18_CONSUMER_EXPORT_CHANNEL_REORDER
    - C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
    - C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
    - C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
  price_windows:
    - 30D MFE/MAE
    - 90D MFE/MAE
    - 180D MFE/MAE
  output_use:
    - cross-archetype accounting-trust gate
    - bridge-vs-label route split
    - local 4B vs false-positive block
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
reason:
  - rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - this file changes canonical scope to R13 accounting-trust validation
  - exact source-archetype keys should be deduped separately from this R13 guardrail key
  - no production scoring changed
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":10,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"CONSUMER_EXPORT_SELLTHROUGH_REORDER_MARGIN_ACCOUNTING_TRUST_VALIDATED","source_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","symbol":"003230","name":"삼양식품","trigger_type":"Stage2-Actionable","entry_date":"2024-05-20","entry_close":502000,"price_basis":"tradable_raw","mfe_30d_pct":43.03,"mae_30d_pct":-4.68,"mfe_90d_pct":43.03,"mae_90d_pct":-9.26,"mfe_180d_pct":59.36,"mae_180d_pct":-9.26,"forward_high_30d":718000,"forward_low_30d":478500,"forward_high_90d":718000,"forward_low_90d":455500,"forward_high_180d":800000,"forward_low_180d":455500,"calibration_usable":true,"case_role":"accounting_trust_validated","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|003230|Stage2-Actionable|2024-05-20","accounting_bridge":"export sell-through, reorder, shelf expansion and margin bridge","route":"KeepStage2_ExportReorderBridge"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":10,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"LEGACY_BRAND_CHANNEL_DECAY_ACCOUNTING_TRUST_CAP","source_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","symbol":"090430","name":"아모레퍼시픽","trigger_type":"Stage2-Watch","entry_date":"2024-05-20","entry_close":179700,"price_basis":"tradable_raw","mfe_30d_pct":11.58,"mae_30d_pct":-6.17,"mfe_90d_pct":11.58,"mae_90d_pct":-18.81,"mfe_180d_pct":11.58,"mae_180d_pct":-44.63,"forward_high_30d":200500,"forward_low_30d":168600,"forward_high_90d":200500,"forward_low_90d":145900,"forward_high_180d":200500,"forward_low_180d":99500,"calibration_usable":true,"case_role":"accounting_trust_cap","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|090430|Stage2-Watch|2024-05-20","accounting_bridge":"legacy K-beauty brand and China-channel label without refreshed non-China sell-through and margin bridge","route":"Stage2Cap_ChannelDecay"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":10,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"OWNED_SEARCH_COMMERCE_PLATFORM_ARPU_MARGIN_BRIDGE_VALIDATED","source_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"035420","name":"NAVER","trigger_type":"Stage2-Actionable","entry_date":"2024-11-08","entry_close":174600,"price_basis":"tradable_raw","mfe_30d_pct":26.00,"mae_30d_pct":-1.78,"mfe_90d_pct":34.88,"mae_90d_pct":-1.78,"mfe_180d_pct":34.88,"mae_180d_pct":-1.78,"forward_high_30d":220000,"forward_low_30d":171500,"forward_high_90d":235500,"forward_low_90d":171500,"forward_high_180d":235500,"forward_low_180d":171500,"calibration_usable":true,"case_role":"accounting_trust_validated","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|035420|Stage2-Actionable|2024-11-08","accounting_bridge":"owned search/commerce ad inventory, ARPU, conversion and margin leverage","route":"KeepStage2_OwnedPlatformBridge"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":10,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"ADTECH_MARKETING_SERVICE_LABEL_NO_OWNED_INVENTORY_BLOCK","source_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"214270","name":"FSN","trigger_type":"Stage2-FalsePositive","entry_date":"2024-07-18","entry_close":2105,"price_basis":"tradable_raw","mfe_30d_pct":16.63,"mae_30d_pct":-26.37,"mfe_90d_pct":19.00,"mae_90d_pct":-26.37,"mfe_180d_pct":19.00,"mae_180d_pct":-49.64,"forward_high_30d":2455,"forward_low_30d":1550,"forward_high_90d":2505,"forward_low_90d":1550,"forward_high_180d":2505,"forward_low_180d":1060,"calibration_usable":true,"case_role":"accounting_trust_not_validated","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|214270|Stage2-FalsePositive|2024-07-18","accounting_bridge":"adtech/marketing service label without owned inventory, ARPU, retention or durable margin bridge","route":"Stage2FalsePositiveBlock"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":10,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"OEM_VOLUME_MIX_MARGIN_ACCOUNTING_TRUST_VALIDATED","source_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"000270","name":"기아","trigger_type":"Stage2-Actionable","entry_date":"2024-01-25","entry_close":93000,"price_basis":"tradable_raw","mfe_30d_pct":41.61,"mae_30d_pct":-7.42,"mfe_90d_pct":45.16,"mae_90d_pct":-7.42,"mfe_180d_pct":45.16,"mae_180d_pct":-7.42,"forward_high_30d":131700,"forward_low_30d":86100,"forward_high_90d":135000,"forward_low_90d":86100,"forward_high_180d":135000,"forward_low_180d":86100,"calibration_usable":true,"case_role":"accounting_trust_validated","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|000270|Stage2-Actionable|2024-01-25","accounting_bridge":"OEM volume, mix, ASP, margin and shareholder-return bridge","route":"KeepStage2_OEMMarginBridge"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":10,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"AUTO_PARTS_THEME_BLOWOFF_WITHOUT_MARGIN_CASH_BRIDGE","source_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"010690","name":"화신","trigger_type":"Stage2-Watch","entry_date":"2024-06-12","entry_close":11690,"price_basis":"tradable_raw","mfe_30d_pct":35.93,"mae_30d_pct":-4.53,"mfe_90d_pct":35.93,"mae_90d_pct":-30.28,"mfe_180d_pct":35.93,"mae_180d_pct":-47.39,"forward_high_30d":15890,"forward_low_30d":11160,"forward_high_90d":15890,"forward_low_90d":8150,"forward_high_180d":15890,"forward_low_180d":6150,"calibration_usable":true,"case_role":"accounting_trust_not_durable","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|010690|Stage2-Watch|2024-06-12","accounting_bridge":"auto-parts theme MFE without durable customer-volume, margin or cash bridge","route":"Local4BThenBlockIfNoRefresh"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":10,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"CONSTRUCTION_DELAYED_REBOUND_WITH_INCOMPLETE_MARGIN_CASH_BRIDGE","source_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"294870","name":"HDC현대산업개발","trigger_type":"Stage2-Watch","entry_date":"2024-05-13","entry_close":17920,"price_basis":"tradable_raw","mfe_30d_pct":2.12,"mae_30d_pct":-6.58,"mfe_90d_pct":37.28,"mae_90d_pct":-6.58,"mfe_180d_pct":57.37,"mae_180d_pct":-6.58,"forward_high_30d":18300,"forward_low_30d":16740,"forward_high_90d":24600,"forward_low_90d":16740,"forward_high_180d":28200,"forward_low_180d":16740,"calibration_usable":true,"case_role":"delayed_local_4B","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|294870|Stage2-Watch|2024-05-13","accounting_bridge":"delayed construction/PF rebound, but entry-date issuer-specific margin/cash bridge incomplete","route":"DelayedLocal4B_DoNotBackfillImmediateStage2"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":10,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"LARGE_BUILDER_SUPPORT_LABEL_WITHOUT_MARGIN_CASH_BRIDGE_BLOCK","source_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"000720","name":"현대건설","trigger_type":"Stage2-FalsePositive","entry_date":"2024-03-27","entry_close":33250,"price_basis":"tradable_raw","mfe_30d_pct":4.81,"mae_30d_pct":-6.17,"mfe_90d_pct":8.27,"mae_90d_pct":-6.17,"mfe_180d_pct":8.27,"mae_180d_pct":-27.52,"forward_high_30d":34850,"forward_low_30d":31200,"forward_high_90d":36000,"forward_low_90d":31200,"forward_high_180d":36000,"forward_low_180d":24100,"calibration_usable":true,"case_role":"hard_counterexample","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|000720|Stage2-FalsePositive|2024-03-27","accounting_bridge":"large-builder/support label without project margin, PF bridge or cash conversion","route":"Stage2FalsePositiveBlock"}
```

---

## 5. Case analysis

### 5.1 Samyang Foods / 003230 — export reorder bridge validates

Samyang is the consumer accounting-trust positive control. Export sell-through and margin were visible enough to sustain Stage2.

```text
route = KeepStage2_ExportReorderBridge
```

### 5.2 Amorepacific / 090430 — brand label decayed

Amorepacific proves that legacy brand and China-channel exposure do not equal reorder accounting trust.

```text
route = Stage2Cap_ChannelDecay
```

### 5.3 NAVER / 035420 — owned platform bridge validates

NAVER is the platform positive control. Owned ad inventory and commerce conversion reached price validation.

```text
route = KeepStage2_OwnedPlatformBridge
```

### 5.4 FSN / 214270 — adtech service label fails

FSN had advertising vocabulary, but not owned platform economics.

```text
route = Stage2FalsePositiveBlock
```

### 5.5 Kia / 000270 — OEM margin bridge validates

Kia validates the mobility margin bridge: volume, mix, ASP and shareholder-return economics.

```text
route = KeepStage2_OEMMarginBridge
```

### 5.6 Hwashin / 010690 — theme blowoff lacks durable bridge

Hwashin had vertical MFE, but high MAE shows the cash bridge was not durable.

```text
route = Local4BThenBlockIfNoRefresh
```

### 5.7 HDC Hyundai Development / 294870 — delayed local 4B

Delayed rebound is not immediate accounting trust.

```text
route = DelayedLocal4B_DoNotBackfillImmediateStage2
```

### 5.8 Hyundai E&C / 000720 — large-builder label block

Builder/support label failed without project margin or cash bridge.

```text
route = Stage2FalsePositiveBlock
```

---

## 6. Score-return alignment

```yaml
new_independent_case_count: 8
calibration_usable_case_count: 8
calibration_usable_trigger_count: 8
accounting_trust_validated_count: 3
stage2_cap_or_local_4B_count: 3
stage2_false_positive_count: 2
current_profile_error_count: 5
```

| symbol | source | route | 90D MFE/MAE | 180D MFE/MAE | accounting lesson |
|---|---:|---:|---:|---:|---|
| 003230 | C18 | KeepStage2 | +43.03 / -9.26 | +59.36 / -9.26 | sell-through/reorder validates |
| 090430 | C18 | Stage2 cap | +11.58 / -18.81 | +11.58 / -44.63 | legacy brand channel decays |
| 035420 | C26 | KeepStage2 | +34.88 / -1.78 | +34.88 / -1.78 | owned platform ARPU/margin bridge validates |
| 214270 | C26 | hard block | +19.00 / -26.37 | +19.00 / -49.64 | adtech label lacks owned-inventory bridge |
| 000270 | C29 | KeepStage2 | +45.16 / -7.42 | +45.16 / -7.42 | OEM mix/margin bridge validates |
| 010690 | C29 | 4B->block | +35.93 / -30.28 | +35.93 / -47.39 | parts theme lacks durable bridge |
| 294870 | C30 | delayed 4B | +37.28 / -6.58 | +57.37 / -6.58 | delayed rebound not immediate Stage2 |
| 000720 | C30 | hard block | +8.27 / -6.17 | +8.27 / -27.52 | builder label lacks cash bridge |

---

## 7. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"003230","raw_direct_cash_bridge":5,"raw_accounting_trust":5,"raw_price_validation":5,"raw_label_only_risk":0,"raw_drawdown_risk":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_ExportReorderBridge"}
{"row_type":"score_simulation","symbol":"090430","raw_direct_cash_bridge":1,"raw_accounting_trust":1,"raw_price_validation":1,"raw_label_only_risk":4,"raw_drawdown_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2Cap_ChannelDecay"}
{"row_type":"score_simulation","symbol":"035420","raw_direct_cash_bridge":5,"raw_accounting_trust":5,"raw_price_validation":4,"raw_label_only_risk":0,"raw_drawdown_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_OwnedPlatformBridge"}
{"row_type":"score_simulation","symbol":"214270","raw_direct_cash_bridge":0,"raw_accounting_trust":0,"raw_price_validation":1,"raw_label_only_risk":5,"raw_drawdown_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2FalsePositiveBlock"}
{"row_type":"score_simulation","symbol":"000270","raw_direct_cash_bridge":5,"raw_accounting_trust":5,"raw_price_validation":5,"raw_label_only_risk":0,"raw_drawdown_risk":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_OEMMarginBridge"}
{"row_type":"score_simulation","symbol":"010690","raw_direct_cash_bridge":1,"raw_accounting_trust":1,"raw_price_validation":2,"raw_label_only_risk":4,"raw_drawdown_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Local4BThenBlockIfNoRefresh"}
{"row_type":"score_simulation","symbol":"294870","raw_direct_cash_bridge":2,"raw_accounting_trust":1,"raw_price_validation":3,"raw_label_only_risk":2,"raw_drawdown_risk":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"DelayedLocal4B"}
{"row_type":"score_simulation","symbol":"000720","raw_direct_cash_bridge":0,"raw_accounting_trust":0,"raw_price_validation":0,"raw_label_only_risk":4,"raw_drawdown_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2FalsePositiveBlock"}
```

---

## 8. Current calibrated profile stress test

### Existing error risk

The current profile can still confuse:

```text
label
trend
bridge
```

The accounting-trust gate should work like customs. A story cannot enter Stage2 with a label alone. It needs papers: reorder, ARPU, margin, utilization, cash conversion, refinancing, or direct revenue.

### Rule candidate

```text
R13_OPERATING_CASH_BRIDGE_ACCOUNTING_TRUST_GATE_V10

if company_specific_reorder_ARPU_margin_volume_utilization_or_cash_bridge == true
and MFE_90D_pct >= +20
and MAE_90D_pct > -10:
    accounting_trust_validated = true
    keep_stage2_actionable_bonus = true
```

```text
if label_only_or_channel_theme == true
and company_specific_accounting_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if MFE_30D_pct >= +30
and MAE_90D_pct <= -20
and durable_bridge_refresh == false:
    route = local_4B_then_block_if_no_refresh
```

```text
if MFE_30D_pct < +5
and MFE_90D_pct >= +25:
    route = delayed_local_4B
    do_not_backfill_as_immediate_Stage2 = true
```

```text
if MFE_90D_pct < +10
and MAE_180D_pct <= -25
and accounting_bridge == false:
    route = Stage2_FalsePositive_Block
```

---

## 9. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
cross_archetype_rule_candidate: true
loop_contribution_label: cross_archetype_accounting_trust_operating_cash_bridge_candidate
new_axis_proposed: R13_OPERATING_CASH_BRIDGE_ACCOUNTING_TRUST_GATE_V10
existing_axis_strengthened:
  - consumer_export_reorder_bridge_keep_stage2
  - owned_platform_ARPU_margin_bridge_keep_stage2
  - OEM_mix_margin_bridge_keep_stage2
  - label_only_theme_without_cash_bridge_stage2_block
  - delayed_rebound_not_immediate_stage2
existing_axis_weakened: null
```

---

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this single MD. Batch this R13 loop with C18 loop 142, C26 loop 100, C29 loop 103, C30 loop 3, and adjacent R13 high-MAE/4B-4C/Stage2 false-positive files. Extract `R13_OPERATING_CASH_BRIDGE_ACCOUNTING_TRUST_GATE_V10` as a cross-archetype shadow rule. Preserve cases where sell-through, ARPU, margin, mix, utilization or cash bridge validates; block label-only and delayed-backfill cases without fresh bridge evidence.
```

---

## 11. Next research state

```yaml
completed_round: R13
completed_loop: 10
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
