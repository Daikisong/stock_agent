# E2R Stock-Web v12 Residual Research — R5 / C18 Consumer Export Channel Reorder

## 0. Metadata

```text
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R5
selected_loop: 117
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: CONSUMER_EXPORT_CHANNEL_REORDER_REPEAT_DEMAND_SELLTHROUGH_MARGIN_BRIDGE_VS_EXPORT_LABEL_PRICE_ONLY_SPIKE
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
new_independent_case_count: 5
reused_case_count: 0
same_archetype_new_symbol_count: 5
same_archetype_new_trigger_family_count: 5
calibration_usable_case_count: 5
calibration_usable_trigger_count: 5
positive_case_count: 1
mixed_positive_count: 2
counterexample_count: 2
local_4b_watch_count: 3
current_profile_error_count: 5
auto_selected_coverage_gap_static_index: C18 rows 3 -> 8 if accepted; still Priority 0, need 22 to 30
auto_selected_coverage_gap_conversation_local: C18 rows 3 -> 8 if accepted; still Priority 0, need 22 to reach 30
```

## 1. Selection rationale

`V12_Research_No_Repeat_Index.md`의 Priority 0 표에서 `C18_CONSUMER_EXPORT_CHANNEL_REORDER`는 static rows 3 / need-to-30 27로 남아 있었다. 직전 conversation-local ledger에서는 C19와 C27을 30-row floor까지 채운 것으로 보았고, 다음 under-covered canonical archetype은 C18이다.

이번 loop는 `coverage_gap_fill`, `sector_specific_rule_discovery`, `counterexample_mining`, `4B_non_price_requirement_stress_test`를 동시에 수행한다. C18의 핵심 질문은 “수출 채널이 있다”가 아니라 “첫 입점 이후 reorder가 반복되고, 그것이 매출·OPM·revision으로 되돌아왔는가”다. 편의점에 물건을 한 번 깔아둔 것은 진열이고, 재주문이 반복되는 것은 소비자의 손이 실제로 움직였다는 증거다. C18은 이 둘을 나눠야 한다.

## 2. Price atlas validation scope

- price_atlas_repo: `Songdaiki/stock-web`
- manifest: `atlas/manifest.json`
- source_name: `FinanceData/marcap`
- price_adjustment_status: `raw_unadjusted_marcap`
- calibration_shard_root: `atlas/ohlcv_tradable_by_symbol_year`
- manifest max_date: `2026-02-20`
- row basis: 1D tradable OHLCV shard only
- corporate action rule: profile에 corporate-action candidate가 있어도 2024 entry~180D window와 직접 겹치지 않으면 calibration usable로 유지했다. 과거 원시 불연속은 caveat에 남긴다.

Validated profiles and shards:

```text
003230 삼양식품: atlas/symbol_profiles/003/003230.json + 2024/2025 shards
005180 빙그레: atlas/symbol_profiles/005/005180.json + 2024 shard
271560 오리온: atlas/symbol_profiles/271/271560.json + 2024 shard
280360 롯데웰푸드: atlas/symbol_profiles/280/280360.json + 2024 shard
097950 CJ제일제당: atlas/symbol_profiles/097/097950.json + 2024 shard
```

## 3. Case summary

|ticker|name|entry|type|class|MFE30|MAE30|MFE90|MAE90|MFE180|MAE180|
|---|---|---|---|---|---|---|---|---|---|---|
|003230|삼양식품|2024-04-17|Stage3-Yellow|positive|131.9%|-3.5%|175.6%|-3.5%|197.5%|-3.5%|
|005180|빙그레|2024-04-17|Stage3-Yellow|mixed_positive|51.5%|-3.9%|83.6%|-3.9%|83.6%|-8.2%|
|271560|오리온|2024-04-11|Stage2-Actionable|counterexample|2.1%|-7.6%|10.6%|-7.6%|10.6%|-10.5%|
|280360|롯데웰푸드|2024-04-22|4B-Local-Watch|mixed_positive|22.6%|-4.2%|57.8%|-4.2%|57.8%|-22.0%|
|097950|CJ제일제당|2024-04-22|Stage2-Actionable|counterexample|8.9%|-5.2%|17.4%|-5.2%|17.4%|-30.7%|

## 4. Case notes

### 4.1 003230 삼양식품 — clean positive anchor

Entry `2024-04-17` close 260,500. The path immediately converted into a large MFE: 30D +131.9%, 90D +175.6%, 180D +197.5%. This is not just a food/export label case. It is the type of C18 case where export reorder, channel expansion, product pull, and margin/revision should be allowed to graduate from Stage3-Yellow into Stage3-Green. The guardrail should not punish this case merely because price moved fast; it should require the non-price reorder bridge to be present.

### 4.2 005180 빙그레 — local spike, mixed positive

Entry `2024-04-17` close 64,500. It reached +83.6% MFE but later showed 180D MAE -8.2%. This is useful but not clean Green. The path behaves like a seasonal/reorder hybrid: a first strong export/seasonal restocking impulse created a large local MFE, but the later path did not prove the same durability as 삼양식품. The rule should keep it eligible for Yellow or local 4B, then demand a second reorder confirmation.

### 4.3 271560 오리온 — defensive overseas channel false positive

Entry `2024-04-11` close 96,500. 30D MFE was only +2.1% and 180D MAE was -10.5%. This is the quiet false positive: it has overseas channel quality, but not necessarily a new reorder acceleration. The current calibrated profile can still over-score such cases if quality/defensiveness and overseas exposure are mistaken for a new C18 flywheel.

### 4.4 280360 롯데웰푸드 — tradable MFE but high reversal risk

Entry `2024-04-22` close 132,100. The path reached +57.8% MFE by 90D but later fell to -22.0% MAE in the 180D window. This is a classic C18 mixed case: the first move is useful for a watchlist or Yellow, but not enough for durable Green unless repeat order, export segment mix, OPM, and distributor inventory are confirmed.

### 4.5 097950 CJ제일제당 — broad food margin is not pure C18 reorder

Entry `2024-04-22` close 347,000. 90D MFE was +17.4%, but 180D MAE reached -30.7%. This is a counterexample for broad food/margin labels. The business can have global food exposure and margin improvement, but C18 should not grant full positive stage unless the consumer export channel reorder mechanism is visible and separable from bio, commodity, or general margin cycle noise.

## 5. Current calibrated profile stress test

Current proxy:

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
```

Residual finding:

```text
The global profile already blocks pure price-only blowoff, but C18 still needs a consumer-export-specific bridge:
export label -> channel sell-through -> repeat reorder -> revenue/margin/revision -> cash conversion.
```

Mechanism:

```text
A first shipment is inventory leaving the company.
A reorder is proof that inventory left the shelf.
C18 should score the second event higher than the first.
```

Profile errors observed:

```text
1. Positive anchor can be under-compressed: 삼양식품-style reorder + margin revision deserves a sector-specific positive bridge.
2. Local spike can be over-promoted: 빙그레/롯데웰푸드-style theme/reorder mix should remain Yellow/4B until repeat order confirmation.
3. Quality can be over-scored: 오리온-style overseas stability should not be treated as new C18 acceleration.
4. General food margin can be over-scored: CJ제일제당-style broad margin/bio mix should not substitute for consumer export reorder.
```

## 6. Proposed C18 shadow rule

```text
C18_reorder_sellthrough_OPM_bridge_required:
  For Stage3-Green, require at least two of:
  - repeat reorder evidence after first channel fill
  - sell-through or channel inventory improvement
  - export revenue acceleration tied to the same product/channel
  - segment OPM/revision improvement
  - cash conversion / working-capital discipline

C18_export_label_price_only_local_4B_cap:
  If the evidence is mostly K-food/export label + price spike, route to 4B-Local-Watch or Stage2.
  Do not let it become Stage3-Green without non-price reorder bridge.

C18_inventory_AR_channel_stuffing_guard:
  If inventory or AR rises faster than sales, or distributor filling is not separated from consumer pull,
  cap the signal and require another reporting period.

C18_slow_quality_overseas_not_reorder_guard:
  Existing overseas quality franchises need an incremental reorder/revision trigger.
  Stable foreign sales alone should not satisfy C18.
```

## 7. Machine-readable case rows

```jsonl
{"row_type": "case_row", "case_id": "C18_003230_2024_04_17_EXPORT_REORDER_MARGIN_STRUCTURAL_POSITIVE", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "ticker": "003230", "name": "삼양식품", "entry_date": "2024-04-17", "evidence_family": "export_reorder_margin_revision_bridge", "classification": "positive", "stage_alignment": "Stage3-Yellow early, Stage3-Green only after repeat export order + margin revision bridge", "note": "Export reorder and margin evidence converted into a durable rerating. This is the clean positive anchor for C18."}
{"row_type": "case_row", "case_id": "C18_005180_2024_04_17_EXPORT_SUMMER_REORDER_LOCAL_SPIKE_MIXED", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "ticker": "005180", "name": "빙그레", "entry_date": "2024-04-17", "evidence_family": "export_channel_reorder_seasonality_margin_mixed", "classification": "mixed_positive", "stage_alignment": "Stage3-Yellow valid; Green should wait for repeat reorder beyond seasonal heat wave / channel restocking", "note": "Big MFE arrived fast but post-spike retention weakened. C18 needs a seasonal/reorder split rather than treating the export label as durable."}
{"row_type": "case_row", "case_id": "C18_271560_2024_04_11_OVERSEAS_CHANNEL_DEFENSIVE_FALSE_POSITIVE", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "ticker": "271560", "name": "오리온", "entry_date": "2024-04-11", "evidence_family": "overseas_channel_growth_without_reorder_acceleration", "classification": "counterexample", "stage_alignment": "Stage2 possible, Stage3 should be capped without visible acceleration in reorder or revision", "note": "A stable overseas business does not equal a new reorder impulse. The calibrated profile can still over-score quality/defensiveness as C18 export momentum."}
{"row_type": "case_row", "case_id": "C18_280360_2024_04_22_GLOBAL_SNACK_EXPORT_SPIKE_REVERSAL_MIXED", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "ticker": "280360", "name": "롯데웰푸드", "entry_date": "2024-04-22", "evidence_family": "global_snack_export_channel_reorder_price_spike_reversal", "classification": "mixed_positive", "stage_alignment": "Local 4B/Yellow acceptable; Green should require repeat reorder, segment margin and distributor inventory evidence", "note": "The path gives a tradable 90D MFE but later reversion. C18 needs to distinguish export-channel reorder from one-time food theme rerating."}
{"row_type": "case_row", "case_id": "C18_097950_2024_04_22_GLOBAL_FOOD_MARGIN_GENERALIST_HIGH_MAE_COUNTER", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "ticker": "097950", "name": "CJ제일제당", "entry_date": "2024-04-22", "evidence_family": "global_food_margin_bridge_not_pure_reorder_high_MAE", "classification": "counterexample", "stage_alignment": "Stage2 only; broad food margin / bio mix should not become C18 Green without consumer export channel reorder proof", "note": "General food margin evidence produced a small MFE but later high MAE. C18 should require pure consumer export channel and reorder signal."}
```

## 8. Machine-readable trigger rows

```jsonl
{"row_type": "trigger_row_representative", "research_version": "v12", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "ticker": "003230", "name": "삼양식품", "trigger_type": "Stage3-Yellow", "entry_date": "2024-04-17", "entry_price": 260500, "mfe_30d_pct": 131.9, "mae_30d_pct": -3.5, "mfe_90d_pct": 175.6, "mae_90d_pct": -3.5, "mfe_180d_pct": 197.5, "mae_180d_pct": -3.5, "peak_180d_date": "2025-01-02", "peak_180d_price": 775000, "worst_180d_date": "2024-04-17", "worst_180d_price": 251500, "classification": "positive", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "duplicate_key": "C18_CONSUMER_EXPORT_CHANNEL_REORDER|003230|Stage3-Yellow|2024-04-17", "source_profile": "atlas/symbol_profiles/003/003230.json", "source_shards": ["atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv", "atlas/ohlcv_tradable_by_symbol_year/003/003230/2025.csv"]}
{"row_type": "trigger_row_representative", "research_version": "v12", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "ticker": "005180", "name": "빙그레", "trigger_type": "Stage3-Yellow", "entry_date": "2024-04-17", "entry_price": 64500, "mfe_30d_pct": 51.5, "mae_30d_pct": -3.9, "mfe_90d_pct": 83.6, "mae_90d_pct": -3.9, "mfe_180d_pct": 83.6, "mae_180d_pct": -8.2, "peak_180d_date": "2024-06-11", "peak_180d_price": 118400, "worst_180d_date": "2024-09-09", "worst_180d_price": 59200, "classification": "mixed_positive", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "duplicate_key": "C18_CONSUMER_EXPORT_CHANNEL_REORDER|005180|Stage3-Yellow|2024-04-17", "source_profile": "atlas/symbol_profiles/005/005180.json", "source_shards": ["atlas/ohlcv_tradable_by_symbol_year/005/005180/2024.csv"]}
{"row_type": "trigger_row_representative", "research_version": "v12", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "ticker": "271560", "name": "오리온", "trigger_type": "Stage2-Actionable", "entry_date": "2024-04-11", "entry_price": 96500, "mfe_30d_pct": 2.1, "mae_30d_pct": -7.6, "mfe_90d_pct": 10.6, "mae_90d_pct": -7.6, "mfe_180d_pct": 10.6, "mae_180d_pct": -10.5, "peak_180d_date": "2024-06-18", "peak_180d_price": 106700, "worst_180d_date": "2024-09-09", "worst_180d_price": 86400, "classification": "counterexample", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "duplicate_key": "C18_CONSUMER_EXPORT_CHANNEL_REORDER|271560|Stage2-Actionable|2024-04-11", "source_profile": "atlas/symbol_profiles/271/271560.json", "source_shards": ["atlas/ohlcv_tradable_by_symbol_year/271/271560/2024.csv"]}
{"row_type": "trigger_row_representative", "research_version": "v12", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "ticker": "280360", "name": "롯데웰푸드", "trigger_type": "4B-Local-Watch", "entry_date": "2024-04-22", "entry_price": 132100, "mfe_30d_pct": 22.6, "mae_30d_pct": -4.2, "mfe_90d_pct": 57.8, "mae_90d_pct": -4.2, "mfe_180d_pct": 57.8, "mae_180d_pct": -22.0, "peak_180d_date": "2024-06-18", "peak_180d_price": 208500, "worst_180d_date": "2024-11-15", "worst_180d_price": 103000, "classification": "mixed_positive", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "duplicate_key": "C18_CONSUMER_EXPORT_CHANNEL_REORDER|280360|4B-Local-Watch|2024-04-22", "source_profile": "atlas/symbol_profiles/280/280360.json", "source_shards": ["atlas/ohlcv_tradable_by_symbol_year/280/280360/2024.csv"]}
{"row_type": "trigger_row_representative", "research_version": "v12", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "ticker": "097950", "name": "CJ제일제당", "trigger_type": "Stage2-Actionable", "entry_date": "2024-04-22", "entry_price": 347000, "mfe_30d_pct": 8.9, "mae_30d_pct": -5.2, "mfe_90d_pct": 17.4, "mae_90d_pct": -5.2, "mfe_180d_pct": 17.4, "mae_180d_pct": -30.7, "peak_180d_date": "2024-06-26", "peak_180d_price": 407500, "worst_180d_date": "2024-11-14", "worst_180d_price": 240500, "classification": "counterexample", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "duplicate_key": "C18_CONSUMER_EXPORT_CHANNEL_REORDER|097950|Stage2-Actionable|2024-04-22", "source_profile": "atlas/symbol_profiles/097/097950.json", "source_shards": ["atlas/ohlcv_tradable_by_symbol_year/097/097950/2024.csv"]}
```

## 9. Score simulation rows

```jsonl
{"row_type": "score_simulation", "simulation_id": "C18_shadow_rule_reorder_bridge_v1", "current_profile_proxy": "e2r_2_1_stock_web_calibrated", "axis": "consumer_export_reorder_bridge", "rule": "C18 positive requires at least two of: repeat reorder evidence, sell-through/channel inventory improvement, export revenue acceleration, segment OPM/revision bridge.", "expected_effect": "raise Samyang-like structural reorder cases; cap Orion/CJ-like quality or food-margin labels at Stage2 unless reorder bridge exists"}
{"row_type": "score_simulation", "simulation_id": "C18_shadow_rule_local_4b_guard_v1", "axis": "one_time_food_export_price_spike_cap", "rule": "If export/food label is mostly price action or one-time distributor restocking, route to 4B-Local-Watch and require non-price reorder confirmation before Green.", "expected_effect": "reduce Binggrae/Lotte-style post-peak MAE without losing early watchlist usefulness"}
```

## 10. Aggregate / shadow weight / residual contribution rows

```jsonl
{"row_type": "aggregate_metrics", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "case_count": 5, "positive_case_count": 1, "mixed_positive_count": 2, "counterexample_count": 2, "local_4b_watch_count": 3, "median_mfe_90d_pct": 57.8, "median_mae_180d_pct": -10.5, "positive_median_mfe_180d_pct": 197.5, "counterexample_median_mae_180d_pct": -20.6, "residual_error": "current calibrated profile still confuses consumer export label / broad food margin / defensive overseas channel with true reorder flywheel"}
{"row_type": "shadow_weight_candidate", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "production_scoring_changed": false, "shadow_weight_only": true, "proposed_axes": [{"axis": "C18_reorder_sellthrough_OPM_bridge_required", "direction": "+", "candidate_delta": 2.0, "condition": "repeat reorder + export acceleration + segment margin/revision bridge"}, {"axis": "C18_export_label_price_only_local_4B_cap", "direction": "-", "candidate_delta": -2.0, "condition": "export label without channel sell-through or reorder proof"}, {"axis": "C18_inventory_AR_channel_stuffing_guard", "direction": "-", "candidate_delta": -1.5, "condition": "inventory/AR buildup or distributor stuffing risk present"}, {"axis": "C18_slow_quality_overseas_not_reorder_guard", "direction": "-", "candidate_delta": -1.0, "condition": "stable overseas franchise but no incremental reorder impulse"}]}
{"row_type": "residual_contribution", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "loop_contribution_label": "canonical_archetype_rule_candidate", "new_axis_proposed": ["C18_reorder_sellthrough_OPM_bridge_required", "C18_export_label_price_only_local_4B_cap", "C18_inventory_AR_channel_stuffing_guard", "C18_slow_quality_overseas_not_reorder_guard"], "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "local_4b_watch_guard", "high_MAE_guardrail"], "existing_axis_weakened": []}
{"row_type": "narrative_only", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "message": "C18 should behave like a reorder flywheel test, not a broad K-food/export label test. A channel is a pipe; a reorder is water continuing to run through it after first fill. The rule should reward the continuing flow, not the pipe label."}
```

## 11. Validation caveats

```text
non_price_evidence_status = source_proxy_only
evidence_url_pending = true
price_validation_status = verified_against_stock_web_tradable_shards
production_scoring_changed = false
code_patch_written = false
current_live_candidate_scan = false
```

The rows above are usable for calibration because 30D/90D/180D windows are available in stock-web, and no 2024 entry-to-180D window overlaps the listed corporate-action candidate dates in a way that blocks the selected window. Where the profile has old raw discontinuities, the caveat remains attached but does not invalidate the 2024 window.

## 12. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent. Do not run this handoff inside the research session that created this MD.

Task:
- Ingest this standalone v12 residual research file.
- Add its machine-readable rows to the v12 calibration registry only after schema validation.
- Do not change production scoring directly.
- Treat all proposed axes as shadow-rule candidates:
  C18_reorder_sellthrough_OPM_bridge_required
  C18_export_label_price_only_local_4B_cap
  C18_inventory_AR_channel_stuffing_guard
  C18_slow_quality_overseas_not_reorder_guard
- Preserve duplicate key:
  canonical_archetype_id + symbol + trigger_type + entry_date.
- Mark non-price evidence as source_proxy_only / evidence_url_pending until URL verification is performed.
- If later promoted, C18 should reward repeat reorder + sell-through + OPM/revision bridge and cap export-label-only price spikes to 4B-local/Stage2.
```

## 13. Next research state

```text
completed_round = R5
completed_loop = 117
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id = CONSUMER_EXPORT_CHANNEL_REORDER_REPEAT_DEMAND_SELLTHROUGH_MARGIN_BRIDGE_VS_EXPORT_LABEL_PRICE_ONLY_SPIKE
calibration_usable case 수 = 5
calibration_usable trigger 수 = 5
positive_case_count = 1
mixed_positive_count = 2
counterexample_count = 2
local_4b_watch_count = 3
current_profile_error_count = 5
auto_selected_coverage_gap_static_index = C18 rows 3 -> 8 if accepted; still Priority 0, need 22 to 30
auto_selected_coverage_gap_conversation_local = C18 rows 3 -> 8 if accepted; still Priority 0, need 22 to reach 30
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
do_not_propose_new_weight_delta = false
new_axis_proposed = C18_reorder_sellthrough_OPM_bridge_required | C18_export_label_price_only_local_4B_cap | C18_inventory_AR_channel_stuffing_guard | C18_slow_quality_overseas_not_reorder_guard
existing_axis_strengthened = stage2_required_bridge | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | local_4b_watch_guard | high_MAE_guardrail
existing_axis_weakened = null
next_recommended_archetypes = C18_CONSUMER_EXPORT_CHANNEL_REORDER_second_pass_to_30, C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE, C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE, C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK, C31_POLICY_SUBSIDY_LEGISLATION_EVENT, C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
```
