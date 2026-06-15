# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R8
selected_loop: 102
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: OWNED_PLATFORM_INVENTORY_MONETIZATION_BRIDGE_VS_ADTECH_AGENCY_TRUE_PLATFORM_AND_WEAK_AD_RECOVERY_LABEL
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
  stock_web_manifest: read_ok
  uncached_symbol_shards:
    - 042000: cache_miss
    - 237820: cache_miss
    - 181710: cache_miss
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

`C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE` remains Priority 0 in the no-repeat index: 3 representative rows and 27 rows short of the 30-row minimum. The v12 scheduler maps C26~C28 to `R8 / L8_PLATFORM_CONTENT_SW_SECURITY`.

This run continues the local C26 sequence after `R8/C26 loop 101`; selected loop is therefore `102`.

This is not a live platform-stock screen. It is a historical calibration / residual rule file. Direct uncached symbol shards for additional platform-ad candidates returned cache misses in this turn, so this file uses current-session stock-web-derived C26 rows that already contain complete 30D/90D/180D MFE and MAE from `Songdaiki/stock-web` tradable OHLC. Because exact row keys are likely already represented in C26 loops 97~101, this MD should be treated as **rule-consolidation evidence** unless batch ingest finds a genuinely new canonical key. No production scoring is changed.

---

## 1. Research thesis

C26 is not `digital ad recovery` and it is not `platform company`.

It is the operating leverage bridge:

```text
owned platform inventory / owned user surface / owned feed / search / commerce / live-streaming
→ ARPU, take-rate, conversion, retention, creator/user stickiness
→ margin leverage, FCF, revision
→ price path validation
```

The repeated false-positive path is vocabulary leakage:

```text
adtech
agency
marketing service
ad-cycle recovery
true platform surface without margin leverage
```

The model should ask a mechanical question:

```text
Does the company own monetizable inventory, and did that inventory become ARPU and margin?
```

If yes, C26 can keep Stage2.  
If the bridge is real but unrefreshed, route to local 4B.  
If the company only rents attention or sells agency service, C26 should block or reclassify.

This loop separates six routes:

1. **Owned search-commerce platform**
   - Keep Stage2 when ad inventory, commerce conversion, ARPU and margin bridge validate.

2. **Owned live-streaming platform**
   - Stage2 can open, but high MAE requires local 4B until creator retention, ARPU, global monetization and margin refresh.

3. **True platform surface but failed leverage**
   - A platform can be real and still fail C26 if cost, execution, trust/regulatory or margin bridge prevents conversion to accounts.

4. **Adtech / marketing-service label**
   - Block when there is no owned inventory, retention or margin leverage.

5. **Advertising agency**
   - Reclassify to ad-cycle service axis; not C26.

6. **Weak ad-recovery label**
   - Watch only until ARPU, take-rate, retention, margin or FCF bridge appears.

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
    - R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
  price_windows:
    - 30D MFE/MAE
    - 90D MFE/MAE
    - 180D MFE/MAE
  output_use:
    - C26 canonical rule refinement
    - owned-platform vs adtech/agency split
    - true-platform-without-leverage cap
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
  - R8/C26 loop 97
  - R8/C26 loop 98
  - R8/C26 loop 99
  - R8/C26 loop 100
  - R8/C26 loop 101
  - R13 accounting-trust / Stage2 false-positive / high-MAE / 4B-4C guardrail rows
reason:
  - rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - current file consolidates C26-owned-platform monetization rule after repeated R13 bridge checks
  - exact duplicate trigger keys should not be counted again as new aggregate rows
  - no production scoring changed
```

Symbol caveats:

```yaml
035420:
  name: NAVER
  role: owned search/commerce platform positive-control
  calibration_usable: true
  aggregate_credit_note: exact key likely present in C26 loops 98/100/101; control-only if duplicate

067160:
  name: SOOP
  role: live-streaming owned platform local 4B
  calibration_usable: true
  aggregate_credit_note: exact key likely present in C26 loops 99/100/101; control-only if duplicate

035720:
  name: 카카오
  role: true platform surface but operating leverage failed
  calibration_usable: true
  aggregate_credit_note: exact key likely present in C26 loops 99/100/101; cap-control if duplicate

214270:
  name: FSN
  role: adtech/marketing service false positive
  calibration_usable: true
  aggregate_credit_note: exact key likely present in C26 loops 98/100/101; hard-control if duplicate

030000:
  name: 제일기획
  role: advertising agency reclassification counterexample
  calibration_usable: true
  aggregate_credit_note: exact key likely present in C26 loops 99/100/101; reclassification-control if duplicate

216050:
  name: 인크로스
  role: weak ad-recovery watch row
  calibration_usable: true
  aggregate_credit_note: exact key likely present in C26 loops 98/100/101; watch-control if duplicate
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R8","loop":102,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"OWNED_SEARCH_COMMERCE_AD_INVENTORY_ARPU_MARGIN_POSITIVE_CONTROL","symbol":"035420","name":"NAVER","trigger_type":"Stage2-Actionable","entry_date":"2024-11-08","entry_close":174600,"price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":26.00,"MAE_30D_pct":-1.78,"MFE_90D_pct":34.88,"MAE_90D_pct":-1.78,"MFE_180D_pct":34.88,"MAE_180D_pct":-1.78,"forward_high_30d":220000,"forward_low_30d":171500,"forward_high_90d":235500,"forward_low_90d":171500,"forward_high_180d":235500,"forward_low_180d":171500,"calibration_usable":true,"case_role":"reused_positive_control","novelty_key":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|035420|Stage2-Actionable|2024-11-08","trigger_outcome_label":"owned_search_commerce_ARPU_margin_positive_control","current_profile_verdict":"current_profile_correct","non_price_bridge":"owned search/commerce platform ad inventory, ARPU, commerce conversion and margin leverage bridge","dedupe_for_aggregate":true,"aggregate_group_role":"representative","do_not_count_as_new_case":true,"reuse_reason":"C26 loop 101 positive-control row"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R8","loop":102,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"LIVE_STREAMING_PLATFORM_MONETIZATION_HIGH_MAE_LOCAL_4B","symbol":"067160","name":"SOOP","trigger_type":"Stage4B","entry_date":"2024-06-20","entry_close":117000,"price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":22.91,"MAE_30D_pct":-18.38,"MFE_90D_pct":22.91,"MAE_90D_pct":-26.07,"MFE_180D_pct":22.91,"MAE_180D_pct":-32.82,"forward_high_30d":143800,"forward_low_30d":95500,"forward_high_90d":143800,"forward_low_90d":86500,"forward_high_180d":143800,"forward_low_180d":78600,"calibration_usable":true,"case_role":"reused_real_platform_local_4B","novelty_key":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|067160|Stage4B|2024-06-20","trigger_outcome_label":"owned_live_platform_high_MAE_local_4B","current_profile_verdict":"current_profile_4B_too_late","non_price_bridge":"owned live-streaming platform, rebrand/global expansion, creator-viewer monetization and ARPU bridge","dedupe_for_aggregate":true,"aggregate_group_role":"representative","do_not_count_as_new_case":true,"reuse_reason":"C26 loop 101 local-4B control row"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R8","loop":102,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"TRUE_PLATFORM_SURFACE_WITHOUT_AD_ARPU_MARGIN_LEVERAGE_CAP","symbol":"035720","name":"카카오","trigger_type":"Stage2-Watch","entry_date":"2024-05-09","entry_close":48600,"price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.12,"MAE_30D_pct":-13.48,"MFE_90D_pct":4.12,"MAE_90D_pct":-32.30,"MFE_180D_pct":4.12,"MAE_180D_pct":-33.02,"forward_high_30d":50600,"forward_low_30d":42050,"forward_high_90d":50600,"forward_low_90d":32900,"forward_high_180d":50600,"forward_low_180d":32550,"calibration_usable":true,"case_role":"reused_platform_surface_cap","novelty_key":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|035720|Stage2-Watch|2024-05-09","trigger_outcome_label":"true_platform_surface_without_margin_leverage_cap","current_profile_verdict":"current_profile_false_positive","non_price_bridge":"true platform surface, but ad recovery did not become ARPU/margin leverage due to execution, cost, trust/regulatory overhang","dedupe_for_aggregate":true,"aggregate_group_role":"representative","do_not_count_as_new_case":true,"reuse_reason":"C26 loop 101 platform-cap row"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R8","loop":102,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"ADTECH_MARKETING_SERVICE_LABEL_NO_OWNED_INVENTORY_HARD_4C","symbol":"214270","name":"FSN","trigger_type":"Stage4C","entry_date":"2024-07-18","entry_close":2105,"price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":16.63,"MAE_30D_pct":-26.37,"MFE_90D_pct":19.00,"MAE_90D_pct":-26.37,"MFE_180D_pct":19.00,"MAE_180D_pct":-49.64,"forward_high_30d":2455,"forward_low_30d":1550,"forward_high_90d":2505,"forward_low_90d":1550,"forward_high_180d":2505,"forward_low_180d":1060,"calibration_usable":true,"case_role":"reused_hard_counterexample","novelty_key":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|214270|Stage4C|2024-07-18","trigger_outcome_label":"adtech_label_without_owned_inventory_hard_block","current_profile_verdict":"current_profile_false_positive","non_price_bridge":"adtech/marketing service label without owned ad inventory, ARPU, retention, take-rate or durable margin bridge","dedupe_for_aggregate":true,"aggregate_group_role":"representative","do_not_count_as_new_case":true,"reuse_reason":"C26 loop 101 hard counterexample row"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R8","loop":102,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"AD_AGENCY_DIGITAL_MARKETING_RECLASSIFY_NOT_PLATFORM_LEVERAGE","symbol":"030000","name":"제일기획","trigger_type":"Stage2-FalsePositive","entry_date":"2024-05-09","entry_close":19470,"price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.51,"MAE_30D_pct":-6.88,"MFE_90D_pct":0.51,"MAE_90D_pct":-10.38,"MFE_180D_pct":0.51,"MAE_180D_pct":-13.82,"forward_high_30d":19570,"forward_low_30d":18130,"forward_high_90d":19570,"forward_low_90d":17450,"forward_high_180d":19570,"forward_low_180d":16780,"calibration_usable":true,"case_role":"reused_ad_agency_reclassification","novelty_key":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|030000|Stage2-FalsePositive|2024-05-09","trigger_outcome_label":"ad_agency_reclassify_not_platform_leverage","current_profile_verdict":"current_profile_reclassification_needed","non_price_bridge":"advertising agency/digital marketing label without owned user-feed ad inventory or ARPU leverage","dedupe_for_aggregate":true,"aggregate_group_role":"control","do_not_count_as_new_case":true,"reuse_reason":"C26 loop 101 reclassification control row"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R8","loop":102,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"WEAK_AD_RECOVERY_LABEL_WITHOUT_ARPU_MARGIN_WATCH","symbol":"216050","name":"인크로스","trigger_type":"Stage2-Watch","entry_date":"2024-10-23","entry_close":7320,"price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.48,"MAE_30D_pct":-5.19,"MFE_90D_pct":11.48,"MAE_90D_pct":-6.56,"MFE_180D_pct":11.48,"MAE_180D_pct":-15.85,"forward_high_30d":8160,"forward_low_30d":6940,"forward_high_90d":8160,"forward_low_90d":6840,"forward_high_180d":8160,"forward_low_180d":6160,"calibration_usable":true,"case_role":"reused_weak_bridge_watch","novelty_key":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|216050|Stage2-Watch|2024-10-23","trigger_outcome_label":"weak_ad_recovery_label_watch","current_profile_verdict":"current_profile_watch_correct","non_price_bridge":"ad recovery label without durable owned-platform ARPU, take-rate, retention, conversion or margin leverage bridge","dedupe_for_aggregate":true,"aggregate_group_role":"control","do_not_count_as_new_case":true,"reuse_reason":"C26 loop 101 watch control row"}
```

---

## 5. Case analysis

### 5.1 NAVER / 035420 — owned-platform positive control

NAVER is the positive side of C26. It owns the road: search, commerce, ad inventory and conversion surface.

```yaml
entry_close: 174600
30D_MFE_MAE: +26.00 / -1.78
90D_MFE_MAE: +34.88 / -1.78
180D_MFE_MAE: +34.88 / -1.78
route: KeepStage2
```

### 5.2 SOOP / 067160 — real platform, high-MAE 4B

SOOP is not an adtech false positive. It has an owned platform. But the monetization bridge was not refreshed strongly enough to avoid local 4B.

```yaml
entry_close: 117000
30D_MFE_MAE: +22.91 / -18.38
90D_MFE_MAE: +22.91 / -26.07
180D_MFE_MAE: +22.91 / -32.82
route: Stage4B
```

### 5.3 Kakao / 035720 — true platform but failed leverage

Kakao proves that C26 cannot reward platform identity alone.

```yaml
entry_close: 48600
30D_MFE_MAE: +4.12 / -13.48
90D_MFE_MAE: +4.12 / -32.30
180D_MFE_MAE: +4.12 / -33.02
route: Stage2 cap
```

### 5.4 FSN / 214270 — adtech hard 4C

FSN lacks the owned-inventory bridge. The price path confirms rejection.

```yaml
entry_close: 2105
30D_MFE_MAE: +16.63 / -26.37
90D_MFE_MAE: +19.00 / -26.37
180D_MFE_MAE: +19.00 / -49.64
route: Stage4C
```

### 5.5 Cheil Worldwide / 030000 — agency reclassification

Cheil is an advertising business, but not an owned platform operating-leverage case.

```yaml
entry_close: 19470
30D_MFE_MAE: +0.51 / -6.88
90D_MFE_MAE: +0.51 / -10.38
180D_MFE_MAE: +0.51 / -13.82
route: reclassify away from C26
```

### 5.6 Incross / 216050 — weak watch

Incross is not a hard crash row, but ARPU/margin leverage is too weak for C26 Actionable.

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
hard_4C_count: 1
wrong_archetype_reclassification_count: 1
current_profile_error_count: 4
duplicate_note: exact C26 novelty keys are likely already represented in loops 97~101; use this file as rule-formalization evidence unless batch ingest finds new keys
```

| symbol | role | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 035420 | owned platform positive | +26.00 / -1.78 | +34.88 / -1.78 | +34.88 / -1.78 | owned inventory and ARPU validate |
| 067160 | real platform 4B | +22.91 / -18.38 | +22.91 / -26.07 | +22.91 / -32.82 | real bridge but refresh missing |
| 035720 | platform identity cap | +4.12 / -13.48 | +4.12 / -32.30 | +4.12 / -33.02 | platform surface alone fails |
| 214270 | adtech hard 4C | +16.63 / -26.37 | +19.00 / -26.37 | +19.00 / -49.64 | adtech label lacks owned inventory |
| 030000 | agency reclassify | +0.51 / -6.88 | +0.51 / -10.38 | +0.51 / -13.82 | agency business is not C26 |
| 216050 | weak watch | +11.48 / -5.19 | +11.48 / -6.56 | +11.48 / -15.85 | ad recovery label needs ARPU proof |

---

## 7. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"035420","raw_owned_inventory":5,"raw_ARPU_take_rate":4,"raw_conversion_retention":4,"raw_margin_leverage":4,"raw_validation":4,"raw_label_only_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_OwnedPlatform"}
{"row_type":"score_simulation","symbol":"067160","raw_owned_inventory":4,"raw_ARPU_take_rate":3,"raw_conversion_retention":3,"raw_margin_leverage":2,"raw_validation":2,"raw_label_only_risk":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Local4B_MonetizationRefresh"}
{"row_type":"score_simulation","symbol":"035720","raw_owned_inventory":4,"raw_ARPU_take_rate":1,"raw_conversion_retention":2,"raw_margin_leverage":0,"raw_validation":0,"raw_label_only_risk":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2Cap_TruePlatformNoLeverage"}
{"row_type":"score_simulation","symbol":"214270","raw_owned_inventory":0,"raw_ARPU_take_rate":1,"raw_conversion_retention":1,"raw_margin_leverage":0,"raw_validation":0,"raw_label_only_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C_AdtechNoInventory"}
{"row_type":"score_simulation","symbol":"030000","raw_owned_inventory":0,"raw_ARPU_take_rate":0,"raw_conversion_retention":0,"raw_margin_leverage":1,"raw_validation":0,"raw_label_only_risk":5,"raw_reclassification_need":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"ReclassifyAdAgency"}
{"row_type":"score_simulation","symbol":"216050","raw_owned_inventory":1,"raw_ARPU_take_rate":1,"raw_conversion_retention":1,"raw_margin_leverage":1,"raw_validation":1,"raw_label_only_risk":3,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2WatchWeakAdRecovery"}
```

---

## 8. Current calibrated profile stress test

### Existing error risk

C26 can still over-credit two phrases:

```text
platform
ad recovery
```

The first phrase is too broad. The second is too cyclical. C26 should require:

```text
owned inventory -> monetization -> operating leverage
```

A platform is a city. C26 only pays when the city owns the toll road and tolls show up in the ledger.

### Rule candidate

```text
C26_OWNED_INVENTORY_MONETIZATION_BRIDGE_REQUIREMENT_V102

if C26
and platform_adtech_agency_or_ad_recovery_label == true
and owned_inventory_ARPU_retention_conversion_margin_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C26
and owned_inventory_ARPU_margin_bridge == true
and MFE_90D_pct >= +20
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
    allow_stage3_yellow_path = true
```

```text
if C26
and owned_platform_bridge == true
and MFE_90D_pct >= +20
and MAE_90D_pct <= -20:
    local_4B_watch = true
    block_stage3_green = true
    require_ARPU_retention_margin_refresh = true
```

```text
if C26
and adtech_agency_or_marketing_service_label == true
and owned_inventory_bridge == false:
    route = Stage2_FalsePositive_Block_or_Stage4C
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
new_axis_proposed: C26_OWNED_INVENTORY_MONETIZATION_BRIDGE_REQUIREMENT_V102
existing_axis_strengthened:
  - C26_owned_inventory_ARPU_margin_positive_escape_hatch
  - C26_real_platform_high_MAE_local_4B
  - C26_true_platform_without_margin_leverage_cap
  - C26_adtech_agency_label_hard_block_or_reclassify
  - C26_weak_ad_recovery_watch_until_ARPU_margin_refresh
existing_axis_weakened: null
```

---

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this single MD. Batch this C26 loop with C26 loops 97~101 and adjacent R13 accounting-trust / Stage2 false-positive / high-MAE / 4B-4C guardrails. Extract `C26_OWNED_INVENTORY_MONETIZATION_BRIDGE_REQUIREMENT_V102` as a shadow-rule candidate. Preserve owned-platform positives, keep real-but-unrefreshed platform rows in local 4B, block or reclassify adtech/agency labels without owned inventory, and cap true-platform rows that fail ARPU/margin leverage.
```

---

## 11. Next research state

```yaml
completed_round: R8
completed_loop: 102
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
