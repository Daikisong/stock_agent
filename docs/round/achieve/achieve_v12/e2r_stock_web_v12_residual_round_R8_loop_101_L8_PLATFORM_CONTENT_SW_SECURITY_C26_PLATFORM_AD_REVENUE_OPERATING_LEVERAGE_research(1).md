# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R8
selected_loop: 101
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: OWNED_PLATFORM_INVENTORY_ARPU_RETENTION_MARGIN_BRIDGE_VS_ADTECH_AGENCY_LABEL_AND_TRUE_PLATFORM_CAP
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

`C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE` remains a top Priority 0 archetype in the latest no-repeat index: 3 representative rows, 27 rows short of the 30-row minimum. The v12 scheduler maps C26~C28 to `R8 / L8_PLATFORM_CONTENT_SW_SECURITY`.

The previous local C26 formalization file reached `R8/C26 loop 100`; this file continues as `R8/C26 loop 101`.

This is not a live platform-stock scan. It is a historical calibration / residual rule file. Direct uncached `stock-web` symbol shards returned cache misses in this turn, so the trigger rows below reuse stock-web-derived C26 rows already calculated in the current v12 session. Exact trigger keys should be deduped against prior C26 loops if already represented. No production scoring is changed.

---

## 1. Research thesis

C26 is not `advertising recovery = platform operating leverage`.

It is the owned-platform monetization bridge:

```text
owned user surface / search / commerce / feed / live-streaming
→ owned ad inventory, ARPU, take-rate, conversion, retention, creator/user stickiness
→ operating leverage, margin, FCF
→ price path validation
```

The failure mode is vocabulary leakage. Adtech companies, agencies, and weak digital-ad recovery names may sit near the ad cycle, but they do not own the toll road. C26 should pay the road owner only when traffic becomes toll revenue and margin.

This loop separates six routes:

1. **Owned search-commerce platform**
   - Stage2 survives when owned inventory, ARPU, conversion and margin bridge validate with low MAE.

2. **Owned live-streaming platform**
   - Stage2 may survive, but high MAE routes to local 4B until creator retention, ARPU and monetization refresh.

3. **True platform surface but failed leverage**
   - A company can be a real platform and still fail C26 if margin leverage, trust/regulatory bridge and ad ARPU do not validate.

4. **Adtech / marketing-service label**
   - Stage2 false positive when there is no owned inventory, retention or margin bridge.

5. **Advertising agency label**
   - Reclassify to ad-cycle service axis; not C26 platform leverage.

6. **Weak ad-recovery label**
   - Watch only unless ARPU/take-rate/margin bridge appears.

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 6
  actual_cases: 6
  source_archetypes:
    - C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
    - R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
    - R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
    - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
  price_windows:
    - 30D MFE/MAE
    - 90D MFE/MAE
    - 180D MFE/MAE
  output_use:
    - C26 canonical rule refinement
    - owned-platform vs adtech/agency split
    - local 4B vs hard false-positive block
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
  - e2r_stock_web_v12_residual_round_R8_loop_97_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md
  - e2r_stock_web_v12_residual_round_R8_loop_98_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md
  - e2r_stock_web_v12_residual_round_R8_loop_99_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md
  - e2r_stock_web_v12_residual_round_R8_loop_100_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md
  - R13 accounting-trust / Stage2 false-positive / high-MAE guardrail files
reason:
  - rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - current file formalizes C26 owned-platform monetization after R13 bridge checks
  - exact duplicate trigger keys should not be counted again as new aggregate rows
  - no production scoring changed
```

Symbol caveats:

```yaml
035420:
  name: NAVER
  role: owned search/commerce platform operating-leverage positive control
  calibration_usable: true
  aggregate_credit_note: exact key likely present in C26 loop 98/100; use as positive-control if deduped

067160:
  name: SOOP
  role: live-streaming platform rebrand/global monetization local 4B
  calibration_usable: true
  aggregate_credit_note: exact key likely present in C26 loop 99/100; use as local 4B control if deduped

035720:
  name: 카카오
  role: true platform surface but ad leverage/trust/regulatory overhang cap
  calibration_usable: true
  aggregate_credit_note: exact key likely present in C26 loop 99/100; use as cap control if deduped

214270:
  name: FSN
  role: adtech/marketing-service label without owned platform leverage
  calibration_usable: true
  aggregate_credit_note: exact key likely present in C26 loop 98/100; use as hard counterexample if deduped

030000:
  name: 제일기획
  role: ad agency without owned platform inventory
  calibration_usable: true
  aggregate_credit_note: exact key likely present in C26 loop 99/100; use as reclassification counterexample if deduped

216050:
  name: 인크로스
  role: weak ad-recovery label without durable ARPU/margin bridge
  calibration_usable: true
  aggregate_credit_note: exact key likely present in C26 loop 98/100; use as Watch control if deduped
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R8","loop":101,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"OWNED_SEARCH_COMMERCE_AD_ARPU_MARGIN_POSITIVE_CONTROL","symbol":"035420","name":"NAVER","trigger_type":"Stage2-Actionable","entry_date":"2024-11-08","entry_close":174600,"price_basis":"tradable_raw","mfe_30d_pct":26.00,"mae_30d_pct":-1.78,"mfe_90d_pct":34.88,"mae_90d_pct":-1.78,"mfe_180d_pct":34.88,"mae_180d_pct":-1.78,"forward_high_30d":220000,"forward_low_30d":171500,"forward_high_90d":235500,"forward_low_90d":171500,"forward_high_180d":235500,"forward_low_180d":171500,"calibration_usable":true,"case_role":"positive_control","novelty_key":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|035420|Stage2-Actionable|2024-11-08","non_price_bridge":"owned search/commerce platform ad inventory, ARPU, commerce conversion and margin leverage bridge","score_alignment":"keep Stage2; allow Stage3-Yellow while ad revenue, commerce conversion, retention and margin bridge remain refreshed","aggregate_credit_note":"exact key likely already represented; use as positive-control if deduped"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R8","loop":101,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"LIVE_STREAMING_OWNED_PLATFORM_MONETIZATION_HIGH_MAE_LOCAL_4B","symbol":"067160","name":"SOOP","trigger_type":"Stage2-Actionable","entry_date":"2024-06-20","entry_close":117000,"price_basis":"tradable_raw","mfe_30d_pct":22.91,"mae_30d_pct":-18.38,"mfe_90d_pct":22.91,"mae_90d_pct":-26.07,"mfe_180d_pct":22.91,"mae_180d_pct":-32.82,"forward_high_30d":143800,"forward_low_30d":95500,"forward_high_90d":143800,"forward_low_90d":86500,"forward_high_180d":143800,"forward_low_180d":78600,"calibration_usable":true,"case_role":"local_4B_watch","novelty_key":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|067160|Stage2-Actionable|2024-06-20","non_price_bridge":"owned live-streaming platform, rebrand/global expansion and creator-viewer monetization bridge","score_alignment":"Stage2 may open; high MAE blocks Green until creator retention, ARPU, global monetization and margin refresh","aggregate_credit_note":"exact key likely already represented; use as local 4B control if deduped"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R8","loop":101,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"TRUE_PLATFORM_SURFACE_WITHOUT_AD_MARGIN_LEVERAGE_STAGE2_CAP","symbol":"035720","name":"카카오","trigger_type":"Stage2-Watch","entry_date":"2024-05-09","entry_close":48600,"price_basis":"tradable_raw","mfe_30d_pct":4.12,"mae_30d_pct":-13.48,"mfe_90d_pct":4.12,"mae_90d_pct":-32.30,"mfe_180d_pct":4.12,"mae_180d_pct":-33.02,"forward_high_30d":50600,"forward_low_30d":42050,"forward_high_90d":50600,"forward_low_90d":32900,"forward_high_180d":50600,"forward_low_180d":32550,"calibration_usable":true,"case_role":"platform_label_cap","novelty_key":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|035720|Stage2-Watch|2024-05-09","non_price_bridge":"true platform surface, but ad recovery did not become ARPU/margin leverage due to execution, cost, trust/regulatory overhang","score_alignment":"cap Stage2; require Talk Biz ARPU, commerce conversion, margin and trust/regulatory bridge before Actionable","aggregate_credit_note":"exact key likely already represented; use as cap control if deduped"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R8","loop":101,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"ADTECH_MARKETING_SERVICE_LABEL_WITHOUT_OWNED_INVENTORY_HARD_BLOCK","symbol":"214270","name":"FSN","trigger_type":"Stage2-FalsePositive","entry_date":"2024-07-18","entry_close":2105,"price_basis":"tradable_raw","mfe_30d_pct":16.63,"mae_30d_pct":-26.37,"mfe_90d_pct":19.00,"mae_90d_pct":-26.37,"mfe_180d_pct":19.00,"mae_180d_pct":-49.64,"forward_high_30d":2455,"forward_low_30d":1550,"forward_high_90d":2505,"forward_low_90d":1550,"forward_high_180d":2505,"forward_low_180d":1060,"calibration_usable":true,"case_role":"hard_counterexample","novelty_key":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|214270|Stage2-FalsePositive|2024-07-18","non_price_bridge":"adtech/marketing service label without owned ad inventory, ARPU, retention, take-rate or durable margin bridge","score_alignment":"block Stage2-Actionable; high MAE and weak bridge reject label-only C26 credit","aggregate_credit_note":"exact key likely already represented; use as hard counterexample if deduped"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R8","loop":101,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"AD_AGENCY_DIGITAL_MARKETING_LABEL_RECLASSIFY_NOT_PLATFORM_LEVERAGE","symbol":"030000","name":"제일기획","trigger_type":"Stage2-FalsePositive","entry_date":"2024-05-09","entry_close":19470,"price_basis":"tradable_raw","mfe_30d_pct":0.51,"mae_30d_pct":-6.88,"mfe_90d_pct":0.51,"mae_90d_pct":-10.38,"mfe_180d_pct":0.51,"mae_180d_pct":-13.82,"forward_high_30d":19570,"forward_low_30d":18130,"forward_high_90d":19570,"forward_low_90d":17450,"forward_high_180d":19570,"forward_low_180d":16780,"calibration_usable":true,"case_role":"ad_agency_reclassification_counterexample","novelty_key":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|030000|Stage2-FalsePositive|2024-05-09","non_price_bridge":"advertising agency/digital marketing label without owned user-feed ad inventory or ARPU leverage","score_alignment":"block C26 Stage2 bonus; reclassify to ad-cycle service axis rather than platform operating leverage","aggregate_credit_note":"exact key likely already represented; use as reclassification control if deduped"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R8","loop":101,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"AD_RECOVERY_LABEL_WITHOUT_ARPU_MARGIN_BRIDGE_WATCH_ONLY","symbol":"216050","name":"인크로스","trigger_type":"Stage2-Watch","entry_date":"2024-10-23","entry_close":7320,"price_basis":"tradable_raw","mfe_30d_pct":11.48,"mae_30d_pct":-5.19,"mfe_90d_pct":11.48,"mae_90d_pct":-6.56,"mfe_180d_pct":11.48,"mae_180d_pct":-15.85,"forward_high_30d":8160,"forward_low_30d":6940,"forward_high_90d":8160,"forward_low_90d":6840,"forward_high_180d":8160,"forward_low_180d":6160,"calibration_usable":true,"case_role":"weak_bridge_watch","novelty_key":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|216050|Stage2-Watch|2024-10-23","non_price_bridge":"ad recovery label without durable owned-platform ARPU, take-rate, retention, conversion or margin leverage bridge","score_alignment":"Stage2-Watch only; require ARPU/margin bridge before Actionable","aggregate_credit_note":"exact key likely already represented; use as Watch control if deduped"}
```

---

## 5. Case analysis

### 5.1 NAVER / 035420 — owned search-commerce platform positive-control

NAVER is the C26 case to preserve. It owns the platform surface and can convert traffic into ad inventory, commerce conversion and margin.

```yaml
entry_close: 174600
30D_MFE_MAE: +26.00 / -1.78
90D_MFE_MAE: +34.88 / -1.78
180D_MFE_MAE: +34.88 / -1.78
route: KeepStage2
```

### 5.2 SOOP / 067160 — real platform, but high-MAE local 4B

SOOP has a real platform bridge, but the 90D/180D drawdown is too large for Green.

```yaml
entry_close: 117000
30D_MFE_MAE: +22.91 / -18.38
90D_MFE_MAE: +22.91 / -26.07
180D_MFE_MAE: +22.91 / -32.82
route: Local4B
```

The model should require creator retention, ARPU, global monetization and margin refresh before promotion.

### 5.3 Kakao / 035720 — true platform surface, failed leverage

Kakao is the important nuance. It is a real platform, but the price path says the 2024 trigger did not validate operating leverage.

```yaml
entry_close: 48600
30D_MFE_MAE: +4.12 / -13.48
90D_MFE_MAE: +4.12 / -32.30
180D_MFE_MAE: +4.12 / -33.02
route: Stage2 cap
```

### 5.4 FSN / 214270 — adtech label hard counterexample

FSN is the high-MAE false positive. It had adtech vocabulary but no owned-inventory/ARPU bridge.

```yaml
entry_close: 2105
30D_MFE_MAE: +16.63 / -26.37
90D_MFE_MAE: +19.00 / -26.37
180D_MFE_MAE: +19.00 / -49.64
route: Stage2-FalsePositive
```

### 5.5 Cheil Worldwide / 030000 — ad agency is not C26

Cheil is an agency/service reclassification guard.

```yaml
entry_close: 19470
30D_MFE_MAE: +0.51 / -6.88
90D_MFE_MAE: +0.51 / -10.38
180D_MFE_MAE: +0.51 / -13.82
route: Reclassify / block C26 bonus
```

### 5.6 Incross / 216050 — weak ad recovery watch

Incross is not a crash, but the bridge is too weak for Actionable.

```yaml
entry_close: 7320
30D_MFE_MAE: +11.48 / -5.19
90D_MFE_MAE: +11.48 / -6.56
180D_MFE_MAE: +11.48 / -15.85
route: Stage2-Watch
```

---

## 6. Score-return alignment

```yaml
new_independent_case_count: 0
reused_control_case_count: 6
calibration_usable_case_count: 6
calibration_usable_trigger_count: 6
positive_case_count: 2
counterexample_or_cap_count: 4
local_4B_watch_count: 1
current_profile_error_count: 4
duplicate_note: exact C26 novelty keys are likely already represented in loops 97~100; use this file as rule-formalization evidence unless batch ingest finds new keys
```

| symbol | role | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 035420 | positive-control | +26.00 / -1.78 | +34.88 / -1.78 | +34.88 / -1.78 | owned platform ARPU/margin validates |
| 067160 | local 4B | +22.91 / -18.38 | +22.91 / -26.07 | +22.91 / -32.82 | real platform needs monetization refresh |
| 035720 | platform cap | +4.12 / -13.48 | +4.12 / -32.30 | +4.12 / -33.02 | true platform surface still failed leverage |
| 214270 | hard counterexample | +16.63 / -26.37 | +19.00 / -26.37 | +19.00 / -49.64 | adtech label lacks owned platform bridge |
| 030000 | agency reclassification | +0.51 / -6.88 | +0.51 / -10.38 | +0.51 / -13.82 | agency beta is not C26 operating leverage |
| 216050 | weak watch | +11.48 / -5.19 | +11.48 / -6.56 | +11.48 / -15.85 | ad recovery label needs ARPU/margin proof |

---

## 7. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"035420","raw_owned_platform_inventory":5,"raw_ARPU_take_rate":4,"raw_conversion_retention":4,"raw_margin_leverage":4,"raw_validation":4,"raw_label_only_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_OwnedPlatformBridge"}
{"row_type":"score_simulation","symbol":"067160","raw_owned_platform_inventory":4,"raw_ARPU_take_rate":3,"raw_conversion_retention":3,"raw_margin_leverage":2,"raw_validation":2,"raw_label_only_risk":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Local4B_MonetizationRefresh"}
{"row_type":"score_simulation","symbol":"035720","raw_owned_platform_inventory":4,"raw_ARPU_take_rate":1,"raw_conversion_retention":2,"raw_margin_leverage":0,"raw_validation":0,"raw_label_only_risk":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2Cap_TruePlatformNoLeverage"}
{"row_type":"score_simulation","symbol":"214270","raw_owned_platform_inventory":0,"raw_ARPU_take_rate":1,"raw_conversion_retention":1,"raw_margin_leverage":0,"raw_validation":0,"raw_label_only_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2FalsePositive_AdtechLabel"}
{"row_type":"score_simulation","symbol":"030000","raw_owned_platform_inventory":0,"raw_ARPU_take_rate":0,"raw_conversion_retention":0,"raw_margin_leverage":1,"raw_validation":0,"raw_label_only_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Reclassify_AdAgency"}
{"row_type":"score_simulation","symbol":"216050","raw_owned_platform_inventory":1,"raw_ARPU_take_rate":1,"raw_conversion_retention":1,"raw_margin_leverage":1,"raw_validation":1,"raw_label_only_risk":3,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2Watch_WeakAdRecovery"}
```

---

## 8. Current calibrated profile stress test

### Existing error risk

C26 can still over-credit familiar words:

```text
digital ad
adtech
AI marketing
platform company
agency recovery
```

The correct C26 question is narrower:

```text
does the company own monetizable inventory, and does traffic become ARPU/margin?
```

An ad agency rents attention. A platform owns the road. C26 should reward the road only when traffic turns into tolls.

### Rule candidate

```text
C26_OWNED_PLATFORM_ARPU_RETENTION_MARGIN_BRIDGE_REQUIREMENT_V101

if C26
and digital_ad_platform_or_adtech_label == true
and owned_inventory_ARPU_retention_conversion_margin_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C26
and owned_platform_inventory_ARPU_margin_bridge == true
and MFE_90D_pct >= +20
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
    allow_stage3_yellow_path = true
```

```text
if C26
and owned_platform_bridge == true
and MFE_30D_pct >= +20
and MAE_90D_pct <= -20:
    local_4B_watch = true
    block_stage3_green = true
    require_ARPU_retention_margin_refresh = true
```

```text
if C26
and adtech_agency_or_marketing_service_label == true
and owned_inventory_bridge == false:
    route = Stage2_FalsePositive_Block
    require_reclassification_to_ad_cycle_service_axis = true
```

```text
if C26
and true_platform_surface == true
and MFE_90D_pct < +10
and MAE_90D_pct <= -20
and margin_leverage_bridge == false:
    stage2_actionable_bonus = 0
    route = Stage2Cap_or_FalsePositiveBlock
```

---

## 9. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_formalization_from_existing_controls
new_axis_proposed: C26_OWNED_PLATFORM_ARPU_RETENTION_MARGIN_BRIDGE_REQUIREMENT_V101
existing_axis_strengthened:
  - C26_owned_platform_ARPU_margin_positive_escape_hatch
  - C26_true_platform_without_margin_leverage_stage2_cap
  - C26_live_streaming_platform_high_MAE_local_4B
  - C26_adtech_agency_label_stage2_block
  - C26_weak_ad_recovery_watch_until_ARPU_margin_refresh
existing_axis_weakened: null
```

---

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this single MD. Batch this C26 loop with C26 loops 97~100 and adjacent R13 accounting-trust, Stage2 false-positive, 4B/4C and high-MAE files. Extract `C26_OWNED_PLATFORM_ARPU_RETENTION_MARGIN_BRIDGE_REQUIREMENT_V101` as a shadow-rule candidate. Preserve owned-platform positives with ARPU/margin bridge, route real-but-unrefreshed platform cases to local 4B, and block/reclassify adtech, agency and marketing-service labels without owned inventory or operating leverage.
```

---

## 11. Next research state

```yaml
completed_round: R8
completed_loop: 101
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
  - C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
  - C31_POLICY_SUBSIDY_LEGISLATION_EVENT
  - C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
  - C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
```
