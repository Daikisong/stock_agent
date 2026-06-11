# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R8
selected_loop: 100
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: OWNED_PLATFORM_AD_ARPU_OPERATING_LEVERAGE_VS_ADTECH_AGENCY_AND_PLATFORM_LABEL_FALSE_POSITIVE
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

`C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE` remains a Priority 0 archetype in the no-repeat index: 3 representative rows and 27 rows short of the 30-row minimum. The prior local C26 files reached `R8/C26 loop 99`, so this run continues as `R8/C26 loop 100`.

This run is a sector-rule formalization pass. Direct uncached stock-web shard fetch was unstable in recent turns, so the MD reuses stock-web-derived C26 rows already calculated in the current v12 session. Those rows contain full 30D/90D/180D MFE and MAE from `Songdaiki/stock-web` tradable 1D OHLC. In batch ingest, exact trigger keys should be deduped against loops 97~99. This MD should still be useful as a canonical C26 rule candidate because it compares owned-platform positives, local 4B cases, platform-label caps, and adtech/agency false positives under one C26 scoring lens.

---

## 1. Research thesis

C26 is not `digital advertising recovered`.

It is a narrower operating-leverage bridge:

```text
owned platform traffic / search / commerce / feed / live-streaming / creator ecosystem
→ ad inventory, ARPU, take-rate, conversion, retention, margin leverage
→ price path validation
```

A company can be in advertising without being a C26 platform. Ad agencies, adtech service firms, and weak platform labels often move with the ad cycle but do not have owned inventory, ARPU, or operating leverage. The model should not give them the same Stage2 bonus.

This loop separates six routes:

1. **Owned search/commerce platform with operating leverage**
   - Stage2 should stay open when ad recovery reaches search-commerce revenue and margin leverage.

2. **Owned live-streaming platform with creator/viewer migration**
   - Stage2 can open, but high MAE means local 4B until monetization, ARPU, creator retention and global expansion prove durable.

3. **True platform surface but weak operating leverage**
   - Stage2 should be capped when regulation, trust, cost, or execution prevents ad recovery from reaching margin.

4. **Adtech / marketing service label**
   - Stage2 should be blocked if the company lacks owned user-feed inventory, ARPU, retention, or margin bridge.

5. **Ad agency / digital marketing label**
   - Ad-cycle beta is not platform operating leverage.

6. **Small ad-recovery name with low MFE**
   - Ad recovery label without durable margin or ARPU bridge should remain Stage2-Watch or false-positive.

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
  - e2r_stock_web_v12_residual_round_R8_loop_97_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md
  - e2r_stock_web_v12_residual_round_R8_loop_98_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md
  - e2r_stock_web_v12_residual_round_R8_loop_99_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md
  - relevant R13 accounting-trust / high-MAE / 4B/4C guardrail outputs
reason:
  - rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - this file formalizes C26-specific bridge rules after local loop 97~99 evidence
  - exact duplicate trigger keys should not be counted again as new aggregate rows
  - no production scoring changed
```

Symbol caveats:

```yaml
035420:
  name: NAVER
  role: owned search/commerce platform operating-leverage positive control
  calibration_usable: true
  aggregate_credit_note: exact key from C26 loop 98; use as reused control if deduped

067160:
  name: SOOP
  role: live-streaming platform rebrand/global expansion local 4B
  calibration_usable: true
  aggregate_credit_note: exact key from C26 loop 99 or 97; use as reused control if deduped

035720:
  name: 카카오
  role: true platform surface but ad leverage/trust/regulatory overhang cap
  calibration_usable: true
  aggregate_credit_note: exact key from C26 loop 99 or 97; use as reused control if deduped

214270:
  name: FSN
  role: adtech/marketing-service label without platform leverage
  calibration_usable: true
  aggregate_credit_note: exact key from C26 loop 98; use as reused control if deduped

030000:
  name: 제일기획
  role: ad agency label without owned platform inventory
  calibration_usable: true
  aggregate_credit_note: exact key from C26 loop 99; use as reused control if deduped

216050:
  name: 인크로스
  role: weak ad-recovery label without durable operating leverage
  calibration_usable: true
  aggregate_credit_note: exact key from C26 loop 98; use as reused control if deduped
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R8","loop":100,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"SEARCH_COMMERCE_AD_PLATFORM_OPERATING_LEVERAGE_POSITIVE_CONTROL","symbol":"035420","name":"NAVER","trigger_type":"Stage2-Actionable","entry_date":"2024-11-08","entry_close":174600,"price_basis":"tradable_raw","mfe_30d_pct":26.00,"mae_30d_pct":-1.78,"mfe_90d_pct":34.88,"mae_90d_pct":-1.78,"mfe_180d_pct":34.88,"mae_180d_pct":-1.78,"forward_high_30d":220000,"forward_low_30d":171500,"forward_high_90d":235500,"forward_low_90d":171500,"forward_high_180d":235500,"forward_low_180d":171500,"calibration_usable":true,"case_role":"reused_positive_control","novelty_key":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|035420|Stage2-Actionable|2024-11-08","non_price_bridge":"owned search/commerce platform ad recovery and operating leverage bridge","score_alignment":"keep Stage2-Actionable; allow Stage3-Yellow path when ad revenue, commerce conversion and margin leverage remain refreshed","aggregate_credit_note":"exact key from C26 loop 98; dedupe if already represented"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R8","loop":100,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"LIVE_STREAMING_PLATFORM_REBRAND_MONETIZATION_LOCAL_4B","symbol":"067160","name":"SOOP","trigger_type":"Stage2-Actionable","entry_date":"2024-06-20","entry_close":117000,"price_basis":"tradable_raw","mfe_30d_pct":22.91,"mae_30d_pct":-18.38,"mfe_90d_pct":22.91,"mae_90d_pct":-26.07,"mfe_180d_pct":22.91,"mae_180d_pct":-32.82,"forward_high_30d":143800,"forward_low_30d":95500,"forward_high_90d":143800,"forward_low_90d":86500,"forward_high_180d":143800,"forward_low_180d":78600,"calibration_usable":true,"case_role":"reused_local_4B_watch","novelty_key":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|067160|Stage2-Actionable|2024-06-20","non_price_bridge":"owned live-streaming platform, rebrand/global expansion, creator/viewer monetization bridge","score_alignment":"Stage2 may open; high MAE blocks Green until creator retention, ARPU, global monetization and margin bridge refresh","aggregate_credit_note":"exact key from C26 loop 99; dedupe if already represented"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R8","loop":100,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"TALK_AD_COMMERCE_TRUE_PLATFORM_BUT_OPERATING_LEVERAGE_CAP","symbol":"035720","name":"카카오","trigger_type":"Stage2-Watch","entry_date":"2024-05-09","entry_close":48600,"price_basis":"tradable_raw","mfe_30d_pct":4.12,"mae_30d_pct":-13.48,"mfe_90d_pct":4.12,"mae_90d_pct":-32.30,"mfe_180d_pct":4.12,"mae_180d_pct":-33.02,"forward_high_30d":50600,"forward_low_30d":42050,"forward_high_90d":50600,"forward_low_90d":32900,"forward_high_180d":50600,"forward_low_180d":32550,"calibration_usable":true,"case_role":"platform_label_cap","novelty_key":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|035720|Stage2-Watch|2024-05-09","non_price_bridge":"true platform surface, but ad recovery did not translate into operating leverage due to execution, cost, trust/regulatory overhang","score_alignment":"cap Stage2; require Talk Biz ad ARPU, commerce conversion, margin and trust/regulatory bridge before Actionable","aggregate_credit_note":"exact key from C26 loop 99; dedupe if already represented"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R8","loop":100,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"ADTECH_MARKETING_SERVICE_LABEL_WITHOUT_OWNED_PLATFORM_ARPU_BRIDGE","symbol":"214270","name":"FSN","trigger_type":"Stage2-FalsePositive","entry_date":"2024-07-18","entry_close":2105,"price_basis":"tradable_raw","mfe_30d_pct":16.63,"mae_30d_pct":-26.37,"mfe_90d_pct":19.00,"mae_90d_pct":-26.37,"mfe_180d_pct":19.00,"mae_180d_pct":-49.64,"forward_high_30d":2455,"forward_low_30d":1550,"forward_high_90d":2505,"forward_low_90d":1550,"forward_high_180d":2505,"forward_low_180d":1060,"calibration_usable":true,"case_role":"hard_counterexample","novelty_key":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|214270|Stage2-FalsePositive|2024-07-18","non_price_bridge":"adtech/marketing service label without owned ad inventory, ARPU, retention or durable margin bridge","score_alignment":"block Stage2-Actionable; high MAE and weak MFE reject label-only platform leverage","aggregate_credit_note":"exact key from C26 loop 98; dedupe if already represented"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R8","loop":100,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"AD_AGENCY_LABEL_NOT_OWNED_PLATFORM_INVENTORY_FALSE_POSITIVE","symbol":"030000","name":"제일기획","trigger_type":"Stage2-FalsePositive","entry_date":"2024-05-09","entry_close":19470,"price_basis":"tradable_raw","mfe_30d_pct":0.51,"mae_30d_pct":-6.88,"mfe_90d_pct":0.51,"mae_90d_pct":-10.38,"mfe_180d_pct":0.51,"mae_180d_pct":-13.82,"forward_high_30d":19570,"forward_low_30d":18130,"forward_high_90d":19570,"forward_low_90d":17450,"forward_high_180d":19570,"forward_low_180d":16780,"calibration_usable":true,"case_role":"ad_agency_counterexample","novelty_key":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|030000|Stage2-FalsePositive|2024-05-09","non_price_bridge":"advertising agency/digital marketing label without owned user-feed ad inventory leverage","score_alignment":"block C26 Stage2 bonus; reclassify as ad-cycle beta rather than platform operating leverage","aggregate_credit_note":"exact key from C26 loop 99; dedupe if already represented"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R8","loop":100,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"AD_RECOVERY_LABEL_WITHOUT_DURABLE_MARGIN_OR_ARPU_BRIDGE","symbol":"216050","name":"인크로스","trigger_type":"Stage2-Watch","entry_date":"2024-10-23","entry_close":7320,"price_basis":"tradable_raw","mfe_30d_pct":11.48,"mae_30d_pct":-5.19,"mfe_90d_pct":11.48,"mae_90d_pct":-6.56,"mfe_180d_pct":11.48,"mae_180d_pct":-15.85,"forward_high_30d":8160,"forward_low_30d":6940,"forward_high_90d":8160,"forward_low_90d":6840,"forward_high_180d":8160,"forward_low_180d":6160,"calibration_usable":true,"case_role":"weak_bridge_watch","novelty_key":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|216050|Stage2-Watch|2024-10-23","non_price_bridge":"ad recovery label without durable owned-platform ARPU, take-rate, retention, or margin leverage bridge","score_alignment":"Stage2-Watch only; require margin/ARPU bridge before Actionable","aggregate_credit_note":"exact key from C26 loop 98; dedupe if already represented"}
```

---

## 4. Case analysis

### 4.1 NAVER / 035420 — owned search-commerce platform positive-control

NAVER is the route the C26 model should preserve. The trigger had a direct owned-platform bridge: search, commerce, ad inventory, conversion, and operating leverage. The price path confirmed with strong MFE and shallow MAE.

```yaml
entry_close: 174600
30d_MFE_MAE: +26.00 / -1.78
90d_MFE_MAE: +34.88 / -1.78
180d_MFE_MAE: +34.88 / -1.78
route: Stage2-Actionable positive-control
```

### 4.2 SOOP / 067160 — owned live platform, but local 4B after drawdown

SOOP has a real owned-platform bridge: creator/viewer ecosystem, live-streaming surface, and global rebrand optionality. But the later drawdown makes it local 4B, not Green.

```yaml
entry_close: 117000
30d_MFE_MAE: +22.91 / -18.38
90d_MFE_MAE: +22.91 / -26.07
180d_MFE_MAE: +22.91 / -32.82
route: Stage2-Actionable with local 4B watch
```

### 4.3 Kakao / 035720 — true platform surface, but operating leverage failed

Kakao is the most important nuance. It is a real platform, not an ad agency. But the 2024 entry path did not validate ad operating leverage.

```yaml
entry_close: 48600
30d_MFE_MAE: +4.12 / -13.48
90d_MFE_MAE: +4.12 / -32.30
180d_MFE_MAE: +4.12 / -33.02
route: Stage2-Watch / cap
```

True platform status alone is insufficient. C26 needs ad ARPU, commerce conversion, margin and trust/regulatory bridge.

### 4.4 FSN / 214270 — adtech label false positive

FSN is the adtech/marketing-service false positive. It had some MFE but high MAE, and no owned-platform monetization bridge.

```yaml
entry_close: 2105
30d_MFE_MAE: +16.63 / -26.37
90d_MFE_MAE: +19.00 / -26.37
180d_MFE_MAE: +19.00 / -49.64
route: Stage2-FalsePositive
```

### 4.5 Cheil Worldwide / 030000 — ad agency is not C26 platform leverage

Cheil Worldwide shows why ad agency beta should not receive C26 credit. It is an advertising business, but not owned-feed inventory or ARPU operating leverage.

```yaml
entry_close: 19470
30d_MFE_MAE: +0.51 / -6.88
90d_MFE_MAE: +0.51 / -10.38
180d_MFE_MAE: +0.51 / -13.82
route: Stage2-FalsePositive
```

### 4.6 Incross / 216050 — weak ad-recovery label

Incross is not a hard crash case, but MFE and bridge quality are too weak for Actionable.

```yaml
entry_close: 7320
30d_MFE_MAE: +11.48 / -5.19
90d_MFE_MAE: +11.48 / -6.56
180d_MFE_MAE: +11.48 / -15.85
route: Stage2-Watch
```

---

## 5. Score-return alignment

```yaml
new_independent_case_count: 0
reused_control_case_count: 6
calibration_usable_case_count: 6
calibration_usable_trigger_count: 6
positive_case_count: 2
counterexample_or_cap_count: 4
local_4B_watch_count: 1
current_profile_error_count: 4
duplicate_note: exact C26 novelty keys are likely already present in loops 97~99; batch ingest should dedupe them and use this MD as C26 rule-formalization evidence
```

| symbol | role | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 035420 | positive-control | +26.00 / -1.78 | +34.88 / -1.78 | +34.88 / -1.78 | owned search-commerce platform leverage validates |
| 067160 | local 4B | +22.91 / -18.38 | +22.91 / -26.07 | +22.91 / -32.82 | real platform but monetization bridge needs refresh |
| 035720 | platform label cap | +4.12 / -13.48 | +4.12 / -32.30 | +4.12 / -33.02 | true platform still failed operating leverage path |
| 214270 | hard counterexample | +16.63 / -26.37 | +19.00 / -26.37 | +19.00 / -49.64 | adtech label without owned platform bridge fails |
| 030000 | agency counterexample | +0.51 / -6.88 | +0.51 / -10.38 | +0.51 / -13.82 | ad agency is not C26 platform leverage |
| 216050 | weak watch | +11.48 / -5.19 | +11.48 / -6.56 | +11.48 / -15.85 | ad recovery label needs ARPU/margin bridge |

---

## 6. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"035420","raw_owned_platform_inventory":5,"raw_ad_ARPU_take_rate":4,"raw_commerce_conversion":4,"raw_retention_or_user_base":4,"raw_margin_leverage":4,"raw_validation":4,"raw_label_only_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2-Actionable-positive-control"}
{"row_type":"score_simulation","symbol":"067160","raw_owned_platform_inventory":4,"raw_ad_ARPU_take_rate":3,"raw_commerce_conversion":2,"raw_retention_or_user_base":3,"raw_margin_leverage":2,"raw_validation":2,"raw_label_only_risk":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2-Actionable-local-4B-watch"}
{"row_type":"score_simulation","symbol":"035720","raw_owned_platform_inventory":4,"raw_ad_ARPU_take_rate":1,"raw_commerce_conversion":2,"raw_retention_or_user_base":2,"raw_margin_leverage":0,"raw_validation":0,"raw_label_only_risk":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2-Watch-platform-leverage-cap"}
{"row_type":"score_simulation","symbol":"214270","raw_owned_platform_inventory":0,"raw_ad_ARPU_take_rate":1,"raw_commerce_conversion":1,"raw_retention_or_user_base":1,"raw_margin_leverage":0,"raw_validation":0,"raw_label_only_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2-FalsePositive-adtech-label"}
{"row_type":"score_simulation","symbol":"030000","raw_owned_platform_inventory":0,"raw_ad_ARPU_take_rate":0,"raw_commerce_conversion":1,"raw_retention_or_user_base":0,"raw_margin_leverage":1,"raw_validation":0,"raw_label_only_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2-FalsePositive-ad-agency-label"}
{"row_type":"score_simulation","symbol":"216050","raw_owned_platform_inventory":1,"raw_ad_ARPU_take_rate":1,"raw_commerce_conversion":1,"raw_retention_or_user_base":1,"raw_margin_leverage":1,"raw_validation":1,"raw_label_only_risk":3,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2-Watch-weak-ad-recovery-label"}
```

---

## 7. Current calibrated profile stress test

### Existing error risk

C26 can over-credit:

```text
digital ad recovery
adtech label
marketing agency
platform name
```

The correct bridge is narrower:

```text
owned platform inventory -> ad ARPU / take-rate -> conversion / retention -> operating leverage -> margin / FCF
```

A billboard seller is not the same as a city that owns the road. C26 should reward the road owner only when traffic becomes toll revenue and margin.

### Rule candidate

```text
C26_OWNED_PLATFORM_AD_ARPU_OPERATING_LEVERAGE_REQUIREMENT_V100

if C26
and digital_ad_or_platform_label == true
and owned_platform_inventory_ARPU_take_rate_conversion_margin_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C26
and owned_platform_ad_revenue_operating_leverage_bridge == true
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
    route = Stage2Watch_or_FalsePositiveBlock
```

---

## 8. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_formalization_from_existing_controls
new_axis_proposed: C26_OWNED_PLATFORM_AD_ARPU_OPERATING_LEVERAGE_REQUIREMENT_V100
existing_axis_strengthened:
  - C26_owned_platform_inventory_positive_escape_hatch
  - C26_platform_bridge_high_MAE_local_4B
  - C26_true_platform_surface_not_enough_without_margin_leverage
  - C26_adtech_agency_label_stage2_block
  - C26_ad_recovery_label_requires_ARPU_margin_refresh
existing_axis_weakened: null
```

---

## 9. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this single MD. Batch this C26 loop with C26 loops 97~99 and adjacent R13 accounting-trust/high-MAE/4B-4C files. Extract `C26_OWNED_PLATFORM_AD_ARPU_OPERATING_LEVERAGE_REQUIREMENT_V100` as a shadow-rule candidate. Ingest exact trigger rows only if dedupe does not already contain them; otherwise use this file as sector-rule formalization evidence. Preserve owned-platform positive controls, route real platform/high-MAE cases to local 4B, and block adtech/agency/digital-marketing labels without owned ad inventory, ARPU, retention, conversion, or margin leverage bridge.
```

---

## 10. Next research state

```yaml
completed_round: R8
completed_loop: 100
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
