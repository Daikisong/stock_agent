---
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_executed_now: false
completed_round: R9
completed_loop: 102
selected_round: R9
selected_loop: 102
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: TIRE_AND_AUTO_PARTS_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_SECOND_PASS_TO_30
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
new_independent_case_count: 5
reused_case_count: 0
same_archetype_new_symbol_count: 5
same_archetype_new_trigger_family_count: 5
calibration_usable_case_count: 5
calibration_usable_trigger_count: 5
positive_case_count: 1
mixed_positive_count: 2
counterexample_count: 2
local_4b_watch_count: 4
current_profile_error_count: 5
do_not_propose_new_weight_delta: false
evidence_quality: source_proxy_only / evidence_url_pending=true
---

# E2R v12 residual calibration — C29 mobility volume/mix/margin operating leverage, second pass to 30

## 0. One-line thesis

C29는 단순히 “자동차/타이어/부품이 오른다”는 beta가 아니라 **volume → mix/ASP → cost absorption → OPM/FCF → capital return**까지 톱니가 맞물릴 때만 durable Stage3로 승격되어야 한다. 이번 pass의 핵심은 tire/parts 쪽에서 가격은 먼저 불이 붙지만, margin bridge가 약하면 30D MFE를 만든 뒤 90D/180D에서 MAE가 크게 열리는 false positive를 분리하는 것이다.

## 1. Scheduler / no-repeat decision

`V12_Research_No_Repeat_Index.md`의 Priority 0 표에서 C29는 3 rows / need 27 to 30으로 표시되어 있다. 직전 local run에서 C29 1st pass가 추가되어 conversation-local 기준 C29는 약 11 rows로 보정된다. 이번 run은 C29를 다시 선택하되, 직전 pass의 대형 완성차/대표 부품 조합(현대차, 기아, 현대모비스, HL만도 중심)을 피하고 tire 및 auto-lighting/secondary-parts family로 확장한다.

```text
selected_archetype = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
selected_round = R9
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
selected_loop = 102
selection_mode = coverage_index_then_round_metadata
sequential_round_cycle_required = false
coverage_gap_can_override_previous_round = true
```

### Novelty guard

Hard duplicate key is defined as:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

This file uses new symbols and new trigger families versus the prior C29 pass:

| symbol | name | new trigger family | duplicate risk |
|---|---|---|---|
| 161390 | 한국타이어앤테크놀로지 | tire margin rebound -> local 4B reversal | low |
| 073240 | 금호타이어 | tire turnaround spike -> 90D MAE guard | low |
| 002350 | 넥센타이어 | tire beta laggard -> no margin confirmation | low |
| 011210 | 현대위아 | parts/machinery volume bridge weak | low |
| 005850 | 에스엘 | lighting parts mix/ASP positive but post-peak guard | low |

## 2. Stock-web manifest and price-source check

Read source:

```text
manifest = Songdaiki/stock-web/atlas/manifest.json
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14,354,401
raw_row_count = 15,214,118
symbol_count = 5,414
active_like_symbol_count = 2,868
inactive_or_delisted_like_symbol_count = 2,546
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
```

All case windows below use `tradable_raw` 1D rows. Corporate-action candidates outside the selected 2024 forward windows are noted but do not block the selected 30D/90D/180D windows. Metrics are hand-computed from loaded stock-web shards for this MD handoff and should be recomputed by batch tooling before production weight materialization.

## 3. Trigger row summary

| case | symbol | name | entry_date | trigger_type | entry_close | 30D MFE / MAE | 90D MFE / MAE | 180D MFE / MAE | path label | calibration usable |
|---:|---|---|---|---|---:|---:|---:|---:|---|---|
| 1 | 161390 | 한국타이어앤테크놀로지 | 2024-01-25 | C29_TIRE_MARGIN_REBOUND_LOCAL_4B_REVERSAL | 49,450 | +20.5% / -3.5% | +28.0% / -14.8% | +28.0% / -21.9% | mixed_positive_then_high_MAE | true |
| 2 | 073240 | 금호타이어 | 2024-04-11 | C29_TIRE_TURNAROUND_SPIKE_MARGIN_BRIDGE_TEST | 6,490 | +29.0% / -1.4% | +29.0% / -16.6% | +29.0% / -16.6% | mixed_positive_local_4B | true |
| 3 | 002350 | 넥센타이어 | 2024-04-11 | C29_TIRE_BETA_WITHOUT_RELATIVE_MARGIN_CONFIRMATION | 9,500 | +1.1% / -11.0% | +1.1% / -18.7% | +1.1% / -19.7% | counterexample | true |
| 4 | 011210 | 현대위아 | 2024-02-02 | C29_PARTS_VOLUME_BRIDGE_WEAK_OPM_CONFIRMATION | 64,500 | +3.9% / -10.9% | +3.9% / -14.4% | +3.9% / -14.9% | counterexample | true |
| 5 | 005850 | 에스엘 | 2024-04-29 | C29_AUTO_LIGHTING_MIX_ASP_OPERATING_LEVERAGE | 34,150 | +8.1% / -3.7% | +39.5% / -3.7% | +39.5% / -12.8% | positive_with_post_peak_guard | true |

### MFE/MAE convention

```text
MFE = max(high over forward window) / entry_close - 1
MAE = min(low over forward window) / entry_close - 1
windows = 30/90/180 trading-day approximation from stock-web visible shards
basis = raw_unadjusted OHLC, tradable rows only
```

## 4. Case notes

### Case 1 — 161390 한국타이어앤테크놀로지

```text
profile_path = atlas/symbol_profiles/161/161390.json
price_path = atlas/ohlcv_tradable_by_symbol_year/161/161390/2024.csv
profile_status = active_like
corporate_action_candidate_dates = []
entry_date = 2024-01-25
entry_close = 49,450
```

The path looks attractive at first. From 49,450 on 2024-01-25, price reaches 59,600 on 2024-02-23 and later 63,300 on 2024-04-16. A price-only scanner would likely view this as a clean tire margin recovery. The problem is that after the early tire-margin rerating, the path breaks downward: 42,150 appears on 2024-05-07 and the second-half shard shows repeated sub-40,000 prints, including 38,650 on 2024-10-02 and 34,500 on 2024-10-29.

Interpretation: this is a **local 4B / mixed-positive** path, not a durable Stage3-Green path. The model should preserve the early MFE signal but prevent the same case from being used as evidence that C29 can turn Green on price strength alone.

```text
current_profile_error = price_only_or_beta_momentum_too_permissive
residual_fix_candidate = C29_local_MFE_requires_margin_cash_bridge_for_full_4B
case_label = mixed_positive_then_high_MAE
```

### Case 2 — 073240 금호타이어

```text
profile_path = atlas/symbol_profiles/073/073240.json
price_path = atlas/ohlcv_tradable_by_symbol_year/073/073240/2024.csv
profile_status = active_like
corporate_action_candidate_dates = [2010-11-02, 2010-12-14, 2018-07-20]
entry_date = 2024-04-11
entry_close = 6,490
```

The path creates a strong early tire-turnaround impulse. The loaded shard shows 6,490 on 2024-04-11, then a move to 8,250 by 2024-05-03. That is enough to look like a Stage2/Stage3 transition if the engine only sees sector momentum and price confirmation. Yet the same forward path falls back to 5,410 on 2024-07-18, turning the 30D success into a 90D/180D high-MAE test case.

Interpretation: C29 should allow Stage2/Y-D positive monitoring when tire recovery and utilization are visible, but full Stage3 should require explicit margin bridge evidence: replacement vs OE mix, raw-material/freight spread, and FCF conversion. Without that, this is a local 4B watch rather than a durable Green.

```text
current_profile_error = tire_turnaround_price_spike_promoted_before_margin_evidence
residual_fix_candidate = C29_tire_turnaround_spike_high_MAE_guard
case_label = mixed_positive_local_4B
```

### Case 3 — 002350 넥센타이어

```text
profile_path = atlas/symbol_profiles/002/002350.json
price_path = atlas/ohlcv_tradable_by_symbol_year/002/002350/2024.csv
profile_status = active_like
corporate_action_candidate_dates = [1999-02-18, 1999-06-08, 1999-06-10, 2008-03-21]
entry_date = 2024-04-11
entry_close = 9,500
```

This is the clean tire-laggard counterexample. A beta basket trigger on tire/auto mobility would have caught 2024-04-11 because the stock printed 9,540 high and 9,500 close. But the forward path fails almost immediately: 9,120 the next day, 8,470 by 2024-05-03, and sub-8,000 by late June/July.

Interpretation: sector-level tire rebound should not be generalized across all tire names. C29 needs company-level relative strength and margin confirmation. The rule should penalize laggards where the sector theme is live but the symbol does not hold the breakout or show operating leverage evidence.

```text
current_profile_error = sector_beta_generalized_to_laggard_symbol
residual_fix_candidate = C29_relative_margin_confirmation_required_for_tire_laggards
case_label = counterexample
```

### Case 4 — 011210 현대위아

```text
profile_path = atlas/symbol_profiles/011/011210.json
price_path = atlas/ohlcv_tradable_by_symbol_year/011/011210/2024.csv
profile_status = active_like
corporate_action_candidate_dates = []
entry_date = 2024-02-02
entry_close = 64,500
```

This case catches the parts/machinery side of C29. 2024-02-02 has a strong move to 65,500 high and 64,500 close after a January base. The local MFE is weak: the visible forward path only improves to around 67,000 on 2024-02-05, then spends the next months under the entry level, with 55,000s visible through May/July.

Interpretation: auto parts are not automatically operating leverage names. C29 should require either volume visibility or a margin/OPM bridge from the specific business line. For Hyundai Wia-like names, “mobility beta + parent OEM strength” is insufficient unless the margin absorption and order/revenue bridge are visible.

```text
current_profile_error = parent_OEM_volume_beta_overweights_parts_supplier_without_margin_bridge
residual_fix_candidate = C29_parts_supplier_parent_beta_cap
case_label = counterexample
```

### Case 5 — 005850 에스엘

```text
profile_path = atlas/symbol_profiles/005/005850.json
price_path = atlas/ohlcv_tradable_by_symbol_year/005/005850/2024.csv
profile_status = active_like
corporate_action_candidate_dates = [2002-07-30, 2003-12-16, 2007-10-22, 2019-04-16]
entry_date = 2024-04-29
entry_close = 34,150
```

This is the positive-side anchor for the pass. The stock moves from 34,150 on 2024-04-29 to 35,900 on 2024-05-17, 44,450 on 2024-06-12, and 47,650 on 2024-06-17. Unlike pure tire beta spikes, the move persists long enough to behave like a mix/ASP/lighting-content operating leverage story.

But it still requires a post-peak guard. The path later reverts toward the low-40,000s and prints 39,050 on 2024-07-18. Therefore the rule should not blindly upgrade every C29 positive to full Green; it should allow Green only when the operating leverage bridge is refreshed by order/mix/OPM confirmation.

```text
current_profile_error = positive_case_can_be_underweighted_if_system_overblocks_all_mobility_price_strength
residual_fix_candidate = C29_auto_lighting_mix_ASP_positive_bridge_allowed
case_label = positive_with_post_peak_guard
```

## 5. Representative trigger rows JSONL

```jsonl
{"canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"TIRE_AND_AUTO_PARTS_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_SECOND_PASS_TO_30","symbol":"161390","name":"한국타이어앤테크놀로지","trigger_type":"C29_TIRE_MARGIN_REBOUND_LOCAL_4B_REVERSAL","entry_date":"2024-01-25","entry_close":49450,"mfe_30d_pct":20.5,"mae_30d_pct":-3.5,"mfe_90d_pct":28.0,"mae_90d_pct":-14.8,"mfe_180d_pct":28.0,"mae_180d_pct":-21.9,"outcome_label":"mixed_positive_then_high_MAE","calibration_usable":true,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","evidence_quality":"source_proxy_only","evidence_url_pending":true}
{"canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"TIRE_AND_AUTO_PARTS_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_SECOND_PASS_TO_30","symbol":"073240","name":"금호타이어","trigger_type":"C29_TIRE_TURNAROUND_SPIKE_MARGIN_BRIDGE_TEST","entry_date":"2024-04-11","entry_close":6490,"mfe_30d_pct":29.0,"mae_30d_pct":-1.4,"mfe_90d_pct":29.0,"mae_90d_pct":-16.6,"mfe_180d_pct":29.0,"mae_180d_pct":-16.6,"outcome_label":"mixed_positive_local_4B","calibration_usable":true,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","evidence_quality":"source_proxy_only","evidence_url_pending":true}
{"canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"TIRE_AND_AUTO_PARTS_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_SECOND_PASS_TO_30","symbol":"002350","name":"넥센타이어","trigger_type":"C29_TIRE_BETA_WITHOUT_RELATIVE_MARGIN_CONFIRMATION","entry_date":"2024-04-11","entry_close":9500,"mfe_30d_pct":1.1,"mae_30d_pct":-11.0,"mfe_90d_pct":1.1,"mae_90d_pct":-18.7,"mfe_180d_pct":1.1,"mae_180d_pct":-19.7,"outcome_label":"counterexample","calibration_usable":true,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","evidence_quality":"source_proxy_only","evidence_url_pending":true}
{"canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"TIRE_AND_AUTO_PARTS_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_SECOND_PASS_TO_30","symbol":"011210","name":"현대위아","trigger_type":"C29_PARTS_VOLUME_BRIDGE_WEAK_OPM_CONFIRMATION","entry_date":"2024-02-02","entry_close":64500,"mfe_30d_pct":3.9,"mae_30d_pct":-10.9,"mfe_90d_pct":3.9,"mae_90d_pct":-14.4,"mfe_180d_pct":3.9,"mae_180d_pct":-14.9,"outcome_label":"counterexample","calibration_usable":true,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","evidence_quality":"source_proxy_only","evidence_url_pending":true}
{"canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"TIRE_AND_AUTO_PARTS_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_SECOND_PASS_TO_30","symbol":"005850","name":"에스엘","trigger_type":"C29_AUTO_LIGHTING_MIX_ASP_OPERATING_LEVERAGE","entry_date":"2024-04-29","entry_close":34150,"mfe_30d_pct":8.1,"mae_30d_pct":-3.7,"mfe_90d_pct":39.5,"mae_90d_pct":-3.7,"mfe_180d_pct":39.5,"mae_180d_pct":-12.8,"outcome_label":"positive_with_post_peak_guard","calibration_usable":true,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","evidence_quality":"source_proxy_only","evidence_url_pending":true}
```

## 6. Residual contribution summary

### What this run adds

```text
new_independent_case_count = 5
new_symbol_count = 5
new_trigger_family_count = 5
positive_case_count = 1
mixed_positive_count = 2
counterexample_count = 2
local_4b_watch_count = 4
```

The contribution is not another generic “mobility is cyclical” note. It isolates three specific failure channels:

1. Tire names can create large 30D MFE but still fail 90D/180D if margin evidence is not refreshed.
2. Laggard tire names should not inherit sector-level tire recovery credit.
3. Auto parts should not inherit parent-OEM beta unless the part supplier has volume/mix/OPM bridge evidence.

And one positive channel:

1. Lighting/content-per-vehicle suppliers can produce more durable C29 paths when mix/ASP and operating leverage evidence exist.

## 7. Proposed shadow rules

### New axis proposed

```text
C29_COMPANY_LEVEL_VOLUME_MIX_MARGIN_BRIDGE_REQUIRED
C29_TIRE_SPIKE_LOCAL_4B_NOT_FULL_4B_WITHOUT_MARGIN_REFRESH
C29_TIRE_LAGGARD_RELATIVE_STRENGTH_GUARD
C29_PARTS_SUPPLIER_PARENT_OEM_BETA_CAP
C29_AUTO_LIGHTING_MIX_ASP_POSITIVE_BRIDGE_ALLOWED
C29_POST_PEAK_HIGH_MAE_REVERSAL_GUARD
```

### Suggested behavior

```text
if canonical_archetype_id == C29 and evidence is only mobility/auto/tire sector beta:
    cap_stage = Stage2_Yellow
    block_stage3_green = true

if C29 tire case has 30D MFE > +15% but no explicit OPM/FCF/margin-refresh evidence:
    classify = local_4B_watch
    require_90D_bridge_refresh = true

if C29 auto parts supplier relies only on parent OEM volume:
    require supplier-level revenue/mix/OPM bridge
    apply parent_beta_cap

if C29 lighting/electronics supplier has mix/ASP and margin bridge evidence:
    allow Stage3_Yellow_to_Green candidate
    still apply post_peak_high_MAE_guard
```

### Existing axis strengthened

```text
stage2_required_bridge
price_only_blowoff_blocks_positive_stage
full_4b_requires_non_price_evidence
local_4b_watch_guard
high_MAE_guardrail
```

### Existing axis weakened

```text
null
```

## 8. Score-return alignment stress test

| axis | before risk | after this run |
|---|---|---|
| C29 price-only momentum | early tire/OEM beta could become too optimistic | cap to Stage2/Local 4B unless margin bridge exists |
| C29 laggard transfer | sector tire rally could lift all tire names | require symbol-level relative strength and confirmation |
| C29 parts supplier beta | parent OEM volume can leak into supplier Stage3 | supplier-level volume/mix/OPM bridge required |
| C29 positive recognition | all mobility spikes could be overblocked after high-MAE cases | allow positive if content/mix/ASP operating leverage is visible |

## 9. Deferred Coding Agent Handoff Prompt

Do not execute this section in the research session. Use it later in a coding/batch-integration session only.

```text
You are the coding agent for Songdaiki/stock_agent. Ingest this V12 research MD as a candidate C29 canonical-archetype shadow-rule source. Do not blindly apply all weights. First batch-parse the JSONL rows, recompute all 30D/90D/180D MFE/MAE from Songdaiki/stock-web tradable shards, validate duplicate keys, and compare against existing v12_md_registry.jsonl and v12_trigger_rows_representative.jsonl.

Candidate axes to test:
- C29_COMPANY_LEVEL_VOLUME_MIX_MARGIN_BRIDGE_REQUIRED
- C29_TIRE_SPIKE_LOCAL_4B_NOT_FULL_4B_WITHOUT_MARGIN_REFRESH
- C29_TIRE_LAGGARD_RELATIVE_STRENGTH_GUARD
- C29_PARTS_SUPPLIER_PARENT_OEM_BETA_CAP
- C29_AUTO_LIGHTING_MIX_ASP_POSITIVE_BRIDGE_ALLOWED
- C29_POST_PEAK_HIGH_MAE_REVERSAL_GUARD

Accept only if holdout tests show that these axes reduce high-MAE false positives without suppressing confirmed operating-leverage winners.
```

## 10. Research state for next run

```text
completed_round = R9
completed_loop = 102
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id = TIRE_AND_AUTO_PARTS_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_SECOND_PASS_TO_30
new_independent_case_count = 5
reused_case_count = 0
same_archetype_new_symbol_count = 5
same_archetype_new_trigger_family_count = 5
calibration_usable_case_count = 5
calibration_usable_trigger_count = 5
positive_case_count = 1
mixed_positive_count = 2
counterexample_count = 2
local_4b_watch_count = 4
current_profile_error_count = 5
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
auto_selected_coverage_gap_static_index = C29 rows 3 -> 8 if accepted
auto_selected_coverage_gap_conversation_local = C29 approx rows 11 -> 16 if accepted; still Priority 0, need about 14 to reach 30
next_recommended_archetypes = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_third_pass_to_30, C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK, C31_POLICY_SUBSIDY_LEGISLATION_EVENT, C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP, C18_CONSUMER_EXPORT_CHANNEL_REORDER_second_pass_to_30, C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_fourth_pass_to_30
```
