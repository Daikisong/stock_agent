# E2R Stock-Web v12 Residual Research — R8 / C26 Platform Ad Revenue Operating Leverage

## 0. Metadata

```text
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
schema_family: v12_sector_archetype_residual
selected_round: R8
selected_loop: 103
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: ADTECH_PERFORMANCE_MARKETING_AND_PLATFORM_MONETIZATION_OPERATING_LEVERAGE_BRIDGE_VS_AD_RECOVERY_PRICE_SPIKE
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
loop_objective: coverage_gap_fill | counterexample_mining | sector_specific_rule_discovery | 4B_non_price_requirement_stress_test | canonical_archetype_compression
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
local_4b_watch_count: 4
current_profile_error_count: 5
auto_selected_coverage_gap_static_index: C26 rows 3 -> 8 if accepted; still Priority 0, need 22 to 30
auto_selected_coverage_gap_conversation_local: C26 approx rows 10 -> 15 if accepted; still Priority 0, need about 15 to reach 30
```

## 1. Selection rationale

The current V12 index keeps `C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE` in Priority 0 with only 3 static rows. In the conversation-local ledger, C26 has already been expanded by earlier R8/C26 loops using `067160`, `089600`, `216050`, `035760`, `035720`, `030000`, and `214320`. This pass therefore avoids those symbols and also avoids simply repeating the same broad platform traffic thesis.

C26 is not “advertising market recovered” by itself. The useful mechanism is narrower:

```text
traffic / advertiser spend / campaign volume
    -> monetization yield, take-rate, ROAS, booking or agency margin
    -> operating leverage, OPM / EPS revision, cash conversion
```

A platform can look crowded while the toll booth stays quiet. C26 should reward the toll booth, not the crowd noise.

## 2. Stock-Web validation scope

```text
price_atlas_repo = Songdaiki/stock-web
manifest = atlas/manifest.json
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
manifest_max_date = 2026-02-20
```

Validated profiles and shards:

| symbol | name | profile | price shard | calibration caveat |
|---:|---|---|---|---|
| 181710 | NHN | atlas/symbol_profiles/181/181710.json | atlas/ohlcv_tradable_by_symbol_year/181/181710/2024.csv | old corporate-action candidates only; 2024 window usable |
| 214270 | FSN | atlas/symbol_profiles/214/214270.json | atlas/ohlcv_tradable_by_symbol_year/214/214270/2024.csv | old corporate-action candidates only; 2024 window usable |
| 273060 | 와이즈버즈 | atlas/symbol_profiles/273/273060.json | atlas/ohlcv_tradable_by_symbol_year/273/273060/2024.csv | 2020 SPAC transition candidate only; 2024 window usable |
| 123570 | 이엠넷 | atlas/symbol_profiles/123/123570.json | atlas/ohlcv_tradable_by_symbol_year/123/123570/2024.csv | old corporate-action candidates only; 2024 window usable |
| 230360 | 에코마케팅 | atlas/symbol_profiles/230/230360.json | atlas/ohlcv_tradable_by_symbol_year/230/230360/2024.csv | old corporate-action candidates only; 2024 window usable |

All rows below use tradable 1D OHLCV. Non-price evidence remains `source_proxy_only / evidence_url_pending=true`, so this MD proposes shadow-rule candidates, not production scoring changes.

## 3. Case summary

| ticker | name | entry | trigger_type | class | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 |
|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|
| 181710 | NHN | 2024-01-29 | Stage2-Actionable | mixed_positive | 30.3% | -3.6% | 30.3% | -7.8% | 30.3% | -11.9% |
| 214270 | FSN | 2024-01-26 | 4B-Local-Watch | counterexample | 41.7% | -7.7% | 41.7% | -22.3% | 41.7% | -32.4% |
| 273060 | 와이즈버즈 | 2024-02-20 | 4B-Local-Watch | counterexample | 26.8% | -7.3% | 26.8% | -20.1% | 26.8% | -20.1% |
| 123570 | 이엠넷 | 2024-02-26 | 4B-Local-Watch | local_4b_counter | 43.3% | -3.3% | 43.3% | -10.3% | 43.3% | -20.4% |
| 230360 | 에코마케팅 | 2024-03-14 | Stage2-Actionable | positive_mixed | 27.2% | -5.5% | 27.2% | -5.5% | 27.2% | -5.5% |

## 4. OHLC anchor rows used

| symbol | entry anchor | peak / low anchors |
|---:|---|---|
| 181710 | 2024-01-29 close 22,450 | 2024-02-20 high 29,250; 2024-06-27 low 20,400; 2024-07-05 low 19,780 |
| 214270 | 2024-01-26 close 2,665 | 2024-02-02 high 3,775; 2024-04-18 low 2,070; 2024-06-25 low 1,802 |
| 273060 | 2024-02-20 close 1,446 | 2024-03-06 high 1,834; 2024-04-11 low 1,155; later drift kept the case below durable-positive status |
| 123570 | 2024-02-26 close 3,650 | 2024-03-06 high 5,230; 2024-06-28 low 2,975; 2024-07-23 low 2,905 |
| 230360 | 2024-03-14 close 10,930 | 2024-03-29 high 13,900; 2024-04-03 low 13,000; path stayed materially above entry in the sampled 90D window |

## 5. Case notes

### 5.1 181710 NHN — mixed positive, but bridge must be explicit

Entry `2024-01-29` close 22,450. The early path was useful: 30D MFE +30.3% with low initial MAE. However, the same window later lost force and drifted toward -11.9% MAE. The case supports Stage2-Actionable only if campaign volume, payment/platform margin, or game/platform monetization has already started to convert into operating leverage. Without that bridge, the move becomes a one-quarter recovery trade.

### 5.2 214270 FSN — adtech spike that needs 4B local cap

Entry `2024-01-26` close 2,665. The price reached a 30D high of 3,775, but then fell into a deep 180D MAE around -32.4%. This is the canonical C26 false positive: the word “adtech” can ignite a short fire, but if ROAS, client budget retention, and agency margin do not follow, the flame runs out of oxygen. This should be local 4B-watch, not full Green.

### 5.3 273060 와이즈버즈 — AI/ad keyword proxy without durable operating leverage

Entry `2024-02-20` close 1,446. The stock produced a local MFE of +26.8%, but its low path quickly moved below -20%. This is useful as a counterexample against over-crediting AI-ad or platform-campaign vocabulary. A keyword spike is not an ad revenue flywheel.

### 5.4 123570 이엠넷 — high MFE but high reversal, not clean positive

Entry `2024-02-26` close 3,650. It reached 5,230 quickly, but the later path fell below 3,000. This is an important local 4B case: price confirms attention, but not persistent operating leverage. C26 should require margin or client-spend evidence before converting a spike into durable Stage3.

### 5.5 230360 에코마케팅 — cleaner positive/mixed anchor

Entry `2024-03-14` close 10,930. The path reached a 30D high of 13,900 while keeping drawdown contained in the visible sampled window. This is closer to a valid C26 case because the thesis can plausibly tie performance marketing, client ROAS, and margin conversion. Still, it should not be Green unless the non-price bridge confirms recurring campaign budget and operating leverage.

## 6. Current calibrated profile stress test

Current proxy:

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

Residual error pattern:

| case | current profile risk | desired C26-specific adjustment |
|---|---|---|
| NHN | may over-score broad platform recovery if monetization bridge is vague | require operating leverage / revision bridge for Stage2-Actionable |
| FSN | may preserve too much local MFE as positive evidence | cap at 4B-local unless agency margin/revenue conversion appears |
| 와이즈버즈 | AI/ad label can create price-only spike | block Stage2 if no non-price ad revenue bridge |
| 이엠넷 | high local MFE can look like confirmation | split local-MFE watch from durable Stage3 |
| 에코마케팅 | cleaner path but still needs evidence | allow Stage2, require recurring campaign/margin evidence for Green |

## 7. Proposed shadow rule candidates

```text
C26_PLATFORM_AD_MONETIZATION_MARGIN_BRIDGE_REQUIRED
C26_ADTECH_AI_KEYWORD_PRICE_ONLY_LOCAL_4B_CAP
C26_AGENCY_RECOVERY_REQUIRES_OPM_REVISION_OR_CLIENT_BUDGET_RETENTION
C26_HIGH_MFE_HIGH_MAE_SPIKE_SPLIT
```

No global weights are changed. These are canonical-archetype-specific shadow rules for future batch implementation review.

## 8. Trigger rows — JSONL

```jsonl
{"row_type":"trigger","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","selected_round":"R8","selected_loop":103,"ticker":"181710","name":"NHN","trigger_type":"Stage2-Actionable","entry_date":"2024-01-29","entry_price":22450,"mfe_30d_pct":30.3,"mae_30d_pct":-3.6,"mfe_90d_pct":30.3,"mae_90d_pct":-7.8,"mfe_180d_pct":30.3,"mae_180d_pct":-11.9,"classification":"mixed_positive","evidence_status":"source_proxy_only","calibration_usable":true,"duplicate_key":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|181710|Stage2-Actionable|2024-01-29"}
{"row_type":"trigger","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","selected_round":"R8","selected_loop":103,"ticker":"214270","name":"FSN","trigger_type":"4B-Local-Watch","entry_date":"2024-01-26","entry_price":2665,"mfe_30d_pct":41.7,"mae_30d_pct":-7.7,"mfe_90d_pct":41.7,"mae_90d_pct":-22.3,"mfe_180d_pct":41.7,"mae_180d_pct":-32.4,"classification":"counterexample","evidence_status":"source_proxy_only","calibration_usable":true,"duplicate_key":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|214270|4B-Local-Watch|2024-01-26"}
{"row_type":"trigger","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","selected_round":"R8","selected_loop":103,"ticker":"273060","name":"와이즈버즈","trigger_type":"4B-Local-Watch","entry_date":"2024-02-20","entry_price":1446,"mfe_30d_pct":26.8,"mae_30d_pct":-7.3,"mfe_90d_pct":26.8,"mae_90d_pct":-20.1,"mfe_180d_pct":26.8,"mae_180d_pct":-20.1,"classification":"counterexample","evidence_status":"source_proxy_only","calibration_usable":true,"duplicate_key":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|273060|4B-Local-Watch|2024-02-20"}
{"row_type":"trigger","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","selected_round":"R8","selected_loop":103,"ticker":"123570","name":"이엠넷","trigger_type":"4B-Local-Watch","entry_date":"2024-02-26","entry_price":3650,"mfe_30d_pct":43.3,"mae_30d_pct":-3.3,"mfe_90d_pct":43.3,"mae_90d_pct":-10.3,"mfe_180d_pct":43.3,"mae_180d_pct":-20.4,"classification":"local_4b_counter","evidence_status":"source_proxy_only","calibration_usable":true,"duplicate_key":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|123570|4B-Local-Watch|2024-02-26"}
{"row_type":"trigger","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","selected_round":"R8","selected_loop":103,"ticker":"230360","name":"에코마케팅","trigger_type":"Stage2-Actionable","entry_date":"2024-03-14","entry_price":10930,"mfe_30d_pct":27.2,"mae_30d_pct":-5.5,"mfe_90d_pct":27.2,"mae_90d_pct":-5.5,"mfe_180d_pct":27.2,"mae_180d_pct":-5.5,"classification":"positive_mixed","evidence_status":"source_proxy_only","calibration_usable":true,"duplicate_key":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|230360|Stage2-Actionable|2024-03-14"}
```

## 9. Aggregate rows — JSONL

```jsonl
{"row_type":"aggregate","selected_round":"R8","selected_loop":103,"canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","new_independent_case_count":5,"reused_case_count":0,"same_archetype_new_symbol_count":5,"same_archetype_new_trigger_family_count":5,"calibration_usable_case_count":5,"positive_case_count":1,"mixed_positive_count":2,"counterexample_count":2,"local_4b_watch_count":4,"current_profile_error_count":5}
{"row_type":"shadow_weight","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","do_not_propose_new_weight_delta":false,"new_axis_proposed":["C26_PLATFORM_AD_MONETIZATION_MARGIN_BRIDGE_REQUIRED","C26_ADTECH_AI_KEYWORD_PRICE_ONLY_LOCAL_4B_CAP","C26_AGENCY_RECOVERY_REQUIRES_OPM_REVISION_OR_CLIENT_BUDGET_RETENTION","C26_HIGH_MFE_HIGH_MAE_SPIKE_SPLIT"],"existing_axis_strengthened":["stage2_required_bridge","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"existing_axis_weakened":[]}
{"row_type":"residual_contribution","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","loop_contribution_label":"canonical_archetype_rule_candidate","summary":"C26 needs an explicit ad/platform monetization-to-operating-leverage bridge. Local adtech spikes should be split from durable Stage3 positives."}
```

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not execute this handoff inside the research runner session.

Later batch implementation task:
1. Ingest this MD as a v12 sector-archetype residual research artifact.
2. Parse trigger rows and aggregate rows.
3. Keep production scoring unchanged until multiple C26 artifacts support the same compression.
4. Evaluate shadow axes:
   - C26_PLATFORM_AD_MONETIZATION_MARGIN_BRIDGE_REQUIRED
   - C26_ADTECH_AI_KEYWORD_PRICE_ONLY_LOCAL_4B_CAP
   - C26_AGENCY_RECOVERY_REQUIRES_OPM_REVISION_OR_CLIENT_BUDGET_RETENTION
   - C26_HIGH_MFE_HIGH_MAE_SPIKE_SPLIT
5. Treat source_proxy_only rows as lower confidence until evidence URLs are repaired.
6. Do not change global stage2_actionable_evidence_bonus or global 4B rules from this single MD.
```

## 11. Completion state

```text
completed_round = R8
completed_loop = 103
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_third_pass_to_30, C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE, C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK, C31_POLICY_SUBSIDY_LEGISLATION_EVENT, C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP, C18_CONSUMER_EXPORT_CHANNEL_REORDER_second_pass_to_30
```
