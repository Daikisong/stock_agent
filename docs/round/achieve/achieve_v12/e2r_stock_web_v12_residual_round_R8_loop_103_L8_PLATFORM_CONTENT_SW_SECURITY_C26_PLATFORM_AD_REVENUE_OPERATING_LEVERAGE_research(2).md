# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R8
selected_loop: 103
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: OWNED_INVENTORY_ARPU_MARGIN_HOLDOUT_VALIDATION_VS_ADTECH_AGENCY_TRUE_PLATFORM_LABEL
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
  stock_web_manifest: read_ok
  uncached_symbol_shards:
    - 089600: cache_miss_observed
    - 123570: cache_miss_observed
    - 237820: cache_miss_observed
    - 042000: cache_miss_observed
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
loop_objective:
  - holdout_validation
  - owned_inventory_monetization_bridge_gate
  - adtech_agency_reclassification_guard
  - true_platform_without_leverage_cap
price_source: Songdaiki/stock-web
price_data_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

`C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE` remains Priority 0 in the no-repeat index: 3 representative rows and 27 rows short of the 30-row minimum. The v12 scheduler maps C26~C28 to `R8 / L8_PLATFORM_CONTENT_SW_SECURITY`.

This file continues the local C26 sequence after `R8/C26 loop 102`; selected loop is therefore `103`.

This is a **holdout validation / rule-consolidation** MD. It does not claim fresh independent price discovery. Direct uncached symbol shards for additional adtech/platform candidates returned cache miss in this turn, so the trigger rows below reuse current-session stock-web-derived C26 rows that already contain complete 30D/90D/180D MFE and MAE from `Songdaiki/stock-web` tradable OHLC. Exact duplicate keys should be deduped during batch ingest. No production scoring is changed.

---

## 1. Research thesis

C26 is the owned-inventory monetization bridge, not the digital-ad vocabulary bucket.

```text
owned platform surface / owned feed / search / commerce / live-streaming
→ owned ad inventory
→ ARPU, take-rate, conversion, retention, creator/user stickiness
→ margin leverage, FCF, revision
→ price path validation
```

The recurring false positive is simple:

```text
adtech
agency
marketing service
ad-cycle recovery
true platform identity without margin leverage
```

A company can be near advertising but not own the toll road. C26 should only reward the toll road when traffic becomes toll revenue and margin.

This holdout pass validates six route types:

1. **Owned search-commerce platform positive-control**
   - Keep Stage2 when owned inventory, ARPU, commerce conversion and margin bridge validate.

2. **Owned live-streaming platform local 4B**
   - Real platform bridge survives, but high MAE requires ARPU/creator retention/global monetization refresh.

3. **True platform surface without leverage**
   - Platform identity alone is not enough when margin, trust, regulation and execution do not validate.

4. **Adtech / marketing service hard 4C**
   - Block when there is no owned inventory or durable operating leverage.

5. **Advertising agency reclassification**
   - Agency can benefit from ad-cycle recovery, but it is not C26 owned-platform leverage.

6. **Weak ad recovery watch**
   - Keep Watch until ARPU/take-rate/retention/margin bridge appears.

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 6
  actual_trigger_rows: 6
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
    - C26 holdout validation
    - owned platform vs adtech/agency split
    - local 4B vs hard 4C split
    - true-platform-without-leverage cap
    - no production scoring changes
```

---

## 3. Source validation

```yaml
stock_web_manifest:
  source_name: FinanceData/marcap
  source_repo_url: https://github.com/FinanceData/marcap
  price_adjustment_status: raw_unadjusted_marcap
  min_date: 1995-05-02
  max_date: 2026-02-20
  calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
  raw_shard_root: atlas/ohlcv_raw_by_symbol_year
  deprecated_or_compat_shard_root: atlas/ohlcv_min_by_symbol_year
  symbol_count: 5414
  active_like_symbol_count: 2868
  inactive_or_delisted_like_symbol_count: 2546
  tradable_row_count: 14354401
  raw_row_count: 15214118
  corporate_action_candidate_count: 14435
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
  - R8/C26 loop 102
  - R13 accounting-trust loops 12~13
  - R13 Stage2 false-positive loop 10
  - R13 high-MAE loop 8
  - R13 4B/4C loop 103
reason:
  - all rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - uncached additional adtech/platform shards returned cache miss in this turn
  - exact duplicate C26 keys should be deduped during batch ingest
  - this file is holdout validation / consolidation evidence only
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","selected_round":"R8","selected_loop":103,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"OWNED_SEARCH_COMMERCE_AD_INVENTORY_ARPU_MARGIN_POSITIVE_CONTROL","symbol":"035420","name":"NAVER","trigger_type":"Stage2-Actionable","entry_date":"2024-11-08","entry_price":174600,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":26.00,"MAE_30D_pct":-1.78,"MFE_90D_pct":34.88,"MAE_90D_pct":-1.78,"MFE_180D_pct":34.88,"MAE_180D_pct":-1.78,"forward_high_30d":220000,"forward_low_30d":171500,"forward_high_90d":235500,"forward_low_90d":171500,"forward_high_180d":235500,"forward_low_180d":171500,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C26|035420|Stage2-Actionable|2024-11-08","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control","reuse_reason":"same C26 owned platform positive-control row from loops 100~102","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"owned_platform_positive_control","novelty_key":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|035420|Stage2-Actionable|2024-11-08","non_price_bridge":"owned search/commerce platform ad inventory, ARPU, commerce conversion and margin leverage bridge","score_alignment":"keep Stage2; allow Yellow only while ad revenue, commerce conversion, retention and margin bridge remain refreshed"}
{"row_type":"trigger","selected_round":"R8","selected_loop":103,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"LIVE_STREAMING_PLATFORM_MONETIZATION_HIGH_MAE_LOCAL_4B","symbol":"067160","name":"SOOP","trigger_type":"Stage4B","entry_date":"2024-06-20","entry_price":117000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":22.91,"MAE_30D_pct":-18.38,"MFE_90D_pct":22.91,"MAE_90D_pct":-26.07,"MFE_180D_pct":22.91,"MAE_180D_pct":-32.82,"forward_high_30d":143800,"forward_low_30d":95500,"forward_high_90d":143800,"forward_low_90d":86500,"forward_high_180d":143800,"forward_low_180d":78600,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C26|067160|Stage4B|2024-06-20","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_real_platform_4B","reuse_reason":"same C26 live-platform local-4B row from loops 101~102","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"real_platform_local_4B","novelty_key":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|067160|Stage4B|2024-06-20","non_price_bridge":"owned live-streaming platform, rebrand/global expansion, creator-viewer monetization and ARPU bridge","score_alignment":"local 4B; block Green until creator retention, ARPU, global monetization and margin refresh"}
{"row_type":"trigger","selected_round":"R8","selected_loop":103,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"TRUE_PLATFORM_SURFACE_WITHOUT_AD_ARPU_MARGIN_LEVERAGE_CAP","symbol":"035720","name":"카카오","trigger_type":"Stage2-Watch","entry_date":"2024-05-09","entry_price":48600,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":4.12,"MAE_30D_pct":-13.48,"MFE_90D_pct":4.12,"MAE_90D_pct":-32.30,"MFE_180D_pct":4.12,"MAE_180D_pct":-33.02,"forward_high_30d":50600,"forward_low_30d":42050,"forward_high_90d":50600,"forward_low_90d":32900,"forward_high_180d":50600,"forward_low_180d":32550,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C26|035720|Stage2-Watch|2024-05-09","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_platform_surface_cap","reuse_reason":"same C26 platform-cap row from loops 101~102","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"true_platform_without_leverage_cap","novelty_key":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|035720|Stage2-Watch|2024-05-09","non_price_bridge":"true platform surface, but ad recovery did not become ARPU/margin leverage due to execution, cost, trust/regulatory overhang","score_alignment":"cap Stage2; require Talk Biz ARPU, commerce conversion, margin and trust/regulatory bridge before Actionable"}
{"row_type":"trigger","selected_round":"R8","selected_loop":103,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"ADTECH_MARKETING_SERVICE_LABEL_NO_OWNED_INVENTORY_HARD_4C","symbol":"214270","name":"FSN","trigger_type":"Stage4C","entry_date":"2024-07-18","entry_price":2105,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":16.63,"MAE_30D_pct":-26.37,"MFE_90D_pct":19.00,"MAE_90D_pct":-26.37,"MFE_180D_pct":19.00,"MAE_180D_pct":-49.64,"forward_high_30d":2455,"forward_low_30d":1550,"forward_high_90d":2505,"forward_low_90d":1550,"forward_high_180d":2505,"forward_low_180d":1060,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C26|214270|Stage4C|2024-07-18","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","reuse_reason":"same C26 adtech hard-block row from loops 101~102","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"adtech_hard_4C","novelty_key":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|214270|Stage4C|2024-07-18","non_price_bridge":"adtech/marketing service label without owned ad inventory, ARPU, retention, take-rate or durable margin bridge","score_alignment":"hard 4C; label-only adtech exposure fails C26 bridge test"}
{"row_type":"trigger","selected_round":"R8","selected_loop":103,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"AD_AGENCY_DIGITAL_MARKETING_RECLASSIFY_NOT_PLATFORM_LEVERAGE","symbol":"030000","name":"제일기획","trigger_type":"Stage2-FalsePositive","entry_date":"2024-05-09","entry_price":19470,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":0.51,"MAE_30D_pct":-6.88,"MFE_90D_pct":0.51,"MAE_90D_pct":-10.38,"MFE_180D_pct":0.51,"MAE_180D_pct":-13.82,"forward_high_30d":19570,"forward_low_30d":18130,"forward_high_90d":19570,"forward_low_90d":17450,"forward_high_180d":19570,"forward_low_180d":16780,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C26|030000|Stage2-FalsePositive|2024-05-09","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_reclassification_control","reuse_reason":"same C26 ad-agency reclassification row from loops 101~102","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"ad_agency_reclassification","novelty_key":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|030000|Stage2-FalsePositive|2024-05-09","non_price_bridge":"advertising agency/digital marketing label without owned user-feed ad inventory or ARPU leverage","score_alignment":"block C26 Stage2 bonus; reclassify to ad-cycle service axis rather than platform operating leverage"}
{"row_type":"trigger","selected_round":"R8","selected_loop":103,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"WEAK_AD_RECOVERY_LABEL_WITHOUT_ARPU_MARGIN_WATCH","symbol":"216050","name":"인크로스","trigger_type":"Stage2-Watch","entry_date":"2024-10-23","entry_price":7320,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":11.48,"MAE_30D_pct":-5.19,"MFE_90D_pct":11.48,"MAE_90D_pct":-6.56,"MFE_180D_pct":11.48,"MAE_180D_pct":-15.85,"forward_high_30d":8160,"forward_low_30d":6940,"forward_high_90d":8160,"forward_low_90d":6840,"forward_high_180d":8160,"forward_low_180d":6160,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C26|216050|Stage2-Watch|2024-10-23","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_weak_watch","reuse_reason":"same C26 weak ad-recovery watch row from loops 101~102","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"weak_bridge_watch","novelty_key":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|216050|Stage2-Watch|2024-10-23","non_price_bridge":"ad recovery label without durable owned-platform ARPU, take-rate, retention, conversion or margin leverage bridge","score_alignment":"Stage2-Watch only; require ARPU/margin bridge before Actionable"}
```

---

## 5. Case analysis

### 5.1 NAVER / 035420 — owned platform positive-control

NAVER remains the C26 positive-control.

```yaml
entry_close: 174600
90D_MFE_MAE: +34.88 / -1.78
180D_MFE_MAE: +34.88 / -1.78
route: KeepStage2
```

### 5.2 SOOP / 067160 — live platform local 4B

SOOP is a real platform but has insufficient monetization refresh after high MAE.

```yaml
entry_close: 117000
90D_MFE_MAE: +22.91 / -26.07
180D_MFE_MAE: +22.91 / -32.82
route: Local4B
```

### 5.3 Kakao / 035720 — true platform surface cap

True platform identity did not validate C26 operating leverage.

```yaml
entry_close: 48600
90D_MFE_MAE: +4.12 / -32.30
180D_MFE_MAE: +4.12 / -33.02
route: Stage2 cap
```

### 5.4 FSN / 214270 — adtech hard 4C

Adtech label lacked the owned-inventory monetization bridge.

```yaml
entry_close: 2105
90D_MFE_MAE: +19.00 / -26.37
180D_MFE_MAE: +19.00 / -49.64
route: Stage4C
```

### 5.5 Cheil Worldwide / 030000 — agency reclassification

Agency revenue is not owned-platform leverage.

```yaml
entry_close: 19470
90D_MFE_MAE: +0.51 / -10.38
180D_MFE_MAE: +0.51 / -13.82
route: reclassify away from C26
```

### 5.6 Incross / 216050 — weak watch

Ad recovery label stays watch until ARPU/margin bridge appears.

```yaml
entry_close: 7320
90D_MFE_MAE: +11.48 / -6.56
180D_MFE_MAE: +11.48 / -15.85
route: Stage2-Watch
```

---

## 6. Score-return alignment

```yaml
new_independent_case_count: 0
reused_case_count: 6
new_symbol_count: 0
same_archetype_new_symbol_count: 0
same_archetype_new_trigger_family_count: 0
new_trigger_family_count: 0
calibration_usable_case_count: 6
calibration_usable_trigger_count: 6
positive_case_count: 2
counterexample_count: 4
local_4B_watch_count: 1
hard_4C_count: 1
wrong_archetype_reclassification_count: 1
current_profile_error_count: 4
diversity_score_summary: "owned-platform positive, live-platform 4B, true-platform cap, adtech hard 4C, agency reclassification, weak watch covered; all rows reused"
loop_contribution_label: duplicate_low_value_loop
do_not_propose_new_weight_delta: true
```

| symbol | role | 90D MFE/MAE | 180D MFE/MAE | C26 lesson |
|---|---:|---:|---:|---|
| 035420 | positive-control | +34.88 / -1.78 | +34.88 / -1.78 | owned inventory/ARPU validates |
| 067160 | local 4B | +22.91 / -26.07 | +22.91 / -32.82 | monetization refresh needed |
| 035720 | platform cap | +4.12 / -32.30 | +4.12 / -33.02 | platform identity fails |
| 214270 | hard 4C | +19.00 / -26.37 | +19.00 / -49.64 | adtech label lacks owned inventory |
| 030000 | reclassify | +0.51 / -10.38 | +0.51 / -13.82 | agency is not C26 |
| 216050 | watch | +11.48 / -6.56 | +11.48 / -15.85 | ad recovery needs ARPU proof |

---

## 7. Current calibrated profile stress test

The C26 gate held in holdout form:

```text
owned inventory + ARPU/margin bridge -> keep Stage2
real platform but high MAE -> local 4B
true platform identity without leverage -> cap
adtech/marketing service without owned inventory -> hard 4C
ad agency -> reclassify
weak ad recovery -> Watch
```

### Rule candidate retained, not newly proposed

```text
C26_OWNED_INVENTORY_MONETIZATION_BRIDGE_REQUIREMENT_V103_HELD_OUT

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
    route = Stage4C_or_reclassification
```

---

## 8. Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 6
calibration_usable_trigger_count: 6
representative_trigger_count: 0
new_weight_evidence_candidate_count: 0
guardrail_candidate_count: 6
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
batch_ingest_recommendation: dedupe_as_holdout_validation_only
```

---

## 9. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: true
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
holdout_validation_passed: true
loop_contribution_label: duplicate_low_value_loop
new_axis_proposed: null
existing_axis_strengthened:
  - C26_OWNED_INVENTORY_MONETIZATION_BRIDGE_REQUIREMENT_V103_HELD_OUT
existing_axis_weakened: null
one_line_summary: "This loop adds 0 new independent cases and validates the C26 owned-inventory monetization bridge gate across owned-platform positives, local 4B, platform cap, adtech hard 4C, agency reclassification, and weak-watch controls."
```

---

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Treat this R8/C26 loop 103 as holdout validation only. Batch it with C26 loops 97~102 and R13 accounting-trust / Stage2 false-positive / high-MAE / 4B-4C guardrails. If exact same_entry_group_id rows already exist, dedupe them. Preserve the C26 owned-inventory monetization bridge gate, but do not create a new weight delta from this loop because uncached additional adtech/platform symbol shards returned cache miss and no new independent case was added.
```

---

## 11. Next research state

```yaml
completed_round: R8
completed_loop: 103
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
