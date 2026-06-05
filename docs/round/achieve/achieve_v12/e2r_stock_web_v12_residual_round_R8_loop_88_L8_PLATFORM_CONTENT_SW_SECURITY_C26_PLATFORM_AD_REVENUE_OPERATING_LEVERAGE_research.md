# E2R Stock-Web v12 Residual Research — R8 / Loop 88 / L8 / C26

```yaml
document_type: e2r_stock_web_v12_residual_research
schema_version: v12_stock_web_price_path_residual
scheduled_round: R8
scheduled_loop: 88
completed_round: R8
completed_loop: 88
next_round: R9
next_loop: 88
round_schedule_status: valid
round_sector_consistency: pass

large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: LIVE_STREAMING_SEARCH_TALK_AD_OPERATING_LEVERAGE_VS_TRAFFIC_HEADLINE_FADE

research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false

primary_price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year

new_independent_case_count: 3
same_archetype_new_symbol_count: 1
soft_repeat_symbol_count: 2
positive_case_count: 1
counterexample_count: 2
local_4b_overlay_case_count: 1
calibration_usable_case_count: 3
do_not_propose_new_weight_delta: true
loop_contribution_label: residual_error_found
```

---

## 1. Scope

This R8 run stays inside:

```text
R8 -> L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
```

C26 is useful here because the existing No-Repeat snapshot is shallow and counterexample-heavy:

```text
C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
rows = 13
symbols = 10
positive/counterexample = 2/6
4B/4C = 0/1
top_repeat_symbols = 042000(2), 214270(2), 237820(2), 030000(1), 035420(1), 035720(1)
```

To avoid hard duplication, this run does not reuse the same `canonical_archetype_id + symbol + trigger_type + entry_date` key. It uses one new C26 symbol (`067160 SOOP`) and two soft-repeat large-cap platform symbols (`035420 NAVER`, `035720 Kakao`) with new trigger dates / trigger family.

---

## 2. Research question

C26 often looks easy on headlines:

```text
traffic migration
search-platform advertising improvement
Talk/portal advertising recovery
AI/search/commerce platform leverage
```

But the stock-web path says the signal is only durable when **traffic/revenue evidence becomes operating leverage**:

```text
ad inventory -> fill rate / pricing
platform traffic -> monetized MAU / paying user / ARPU
search or Talk ads -> segment margin / consolidated OP bridge
commerce / content / AI cost -> does not eat the ad recovery
```

This run stress-tests the residual error:

> C26 should not upgrade a platform name merely because traffic, AI, or ad-recovery headlines appear. It needs segment-level ad revenue and operating-leverage evidence; otherwise the trigger is usually a short-lived beta rally or high-MAE false positive.

---

## 3. Price atlas checks

```jsonl
{"row_type":"price_atlas_manifest","source":"Songdaiki/stock-web","source_name":"FinanceData/marcap","price_adjustment_status":"raw_unadjusted_marcap","min_date":"1995-05-02","max_date":"2026-02-20","tradable_row_count":14354401,"symbol_count":5414,"active_like_symbol_count":2868,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year"}
{"row_type":"symbol_profile_check","symbol":"067160","name":"SOOP","latest_market":"KOSDAQ GLOBAL","available_years":"2003-2026","corporate_action_candidate_dates":"2005-12-27;2007-06-05;2007-06-14;2008-01-24;2011-01-27","entry_window_corporate_action_overlap":false,"price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true}
{"row_type":"symbol_profile_check","symbol":"035420","name":"NAVER","latest_market":"KOSPI","available_years":"2002-2026","corporate_action_candidate_dates":"2004-02-26;2004-03-26;2006-07-14;2006-08-16;2013-08-29;2018-10-12","entry_window_corporate_action_overlap":false,"price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true}
{"row_type":"symbol_profile_check","symbol":"035720","name":"카카오","latest_market":"KOSPI","available_years":"1999-2026","corporate_action_candidate_dates":"2000-02-03;2000-03-03;2006-05-19;2014-10-14;2021-04-15","entry_window_corporate_action_overlap":false,"price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true}
```

---

## 4. Case grid

### Case A — 067160 SOOP — positive with local 4B overlay

```text
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: LIVE_STREAMING_TRAFFIC_MIGRATION_TO_MONETIZED_PLATFORM_LEVERAGE
trigger_family: traffic_migration_plus_platform_operating_leverage
trigger_date: 2024-01-08
entry_date: 2024-01-08
entry_price: 98,800
entry_basis: close
```

Evidence interpretation:

- Twitch Korea exit / streamer-viewer migration created a visible traffic-transfer setup.
- SOOP/AfreecaTV had direct monetization levers: live-streaming platform traffic, paid items, creator economy, ad inventory, and platform operating leverage.
- This is not pure “traffic headline”; the route to monetization is closer to the platform’s core model.

Stock-web path:

```text
Entry close: 2024-01-08 = 98,800
30D peak: 2024-02-15 high = 126,000
90D peak: 2024-02-28 high = 139,600
180D peak: 2024-07-11 high = 143,800
180D trough: 2024-08-05 low = 84,900
```

Price-path metrics:

```jsonl
{"row_type":"trigger","case_id":"R8L88_C26_SOOP_067160_20240108_TRAFFIC_MIGRATION_OP_LEVERAGE","symbol":"067160","name":"SOOP","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"LIVE_STREAMING_TRAFFIC_MIGRATION_TO_MONETIZED_PLATFORM_LEVERAGE","trigger_type":"traffic_migration_plus_platform_operating_leverage","trigger_date":"2024-01-08","entry_date":"2024-01-08","entry_price":98800,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":27.5,"mae_30d_pct":-3.5,"mfe_90d_pct":41.3,"mae_90d_pct":-3.5,"mfe_180d_pct":45.5,"mae_180d_pct":-14.1,"peak_date":"2024-07-11","peak_price":143800,"trough_date":"2024-08-05","trough_price":84900,"case_verdict":"positive_with_local_4b_overlay","stage2_actionable_result":"pass_with_non_price_bridge","stage3_green_result":"not_global_rule_candidate","local_4b_watch":true,"full_4b":false,"calibration_usable":true,"do_not_count_as_new_case":false}
```

Interpretation:

SOOP is the positive control. The key distinction is that traffic migration mapped to a native monetization surface. However, after the peak the path gave back hard enough to justify local 4B watch once the rerating moved above +40% without new global monetization proof.

---

### Case B — 035420 NAVER — counterexample / search-ad earnings beat not enough

```text
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: SEARCH_AD_COMMERCE_EARNINGS_BEAT_VS_COMPETITION_COST_DRAG
trigger_family: search_ad_earnings_beat_without_durable_revaluation
trigger_date: 2024-05-03
entry_date: 2024-05-03
entry_price: 194,600
entry_basis: close
```

Evidence interpretation:

- Q1 2024 numbers showed a clean headline: revenue +11% YoY, operating profit +33% YoY, e-commerce +16%, and search-platform ad sales +6.2%.
- But this did not create a clean 90D/180D platform operating-leverage rerating because the market still had to absorb e-commerce competition, AI/product investment, and platform multiple compression.
- This is exactly the C26 residual: headline ad/search growth can be true yet still not enough for Stage2-Actionable if the revenue bridge does not outrun cost / competitive pressure.

Stock-web path:

```text
Entry close: 2024-05-03 = 194,600
30D peak: 2024-05-07 high = 198,500
30D trough: 2024-05-31 low = 170,000
90D trough: 2024-08-05 low = 151,100
180D peak: 2024-12-11 high = 218,000
```

Price-path metrics:

```jsonl
{"row_type":"trigger","case_id":"R8L88_C26_NAVER_035420_20240503_SEARCH_AD_EARNINGS_BEAT","symbol":"035420","name":"NAVER","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"SEARCH_AD_COMMERCE_EARNINGS_BEAT_VS_COMPETITION_COST_DRAG","trigger_type":"search_ad_earnings_beat_without_durable_revaluation","trigger_date":"2024-05-03","entry_date":"2024-05-03","entry_price":194600,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":2.0,"mae_30d_pct":-12.6,"mfe_90d_pct":2.0,"mae_90d_pct":-22.4,"mfe_180d_pct":12.0,"mae_180d_pct":-22.4,"peak_date":"2024-12-11","peak_price":218000,"trough_date":"2024-08-05","trough_price":151100,"case_verdict":"counterexample_high_mae_late_recovery","stage2_actionable_result":"fail_without_margin_durability_bridge","stage3_green_result":"fail","local_4b_watch":false,"full_4b":false,"calibration_usable":true,"do_not_count_as_new_case":false}
```

Interpretation:

NAVER is not a failed business signal; it is a failed immediate rerating signal. The ad/search evidence was real, but the price path says C26 needs a “growth + margin persistence + cost containment” bridge before upgrading beyond Watch/Stage2.

---

### Case C — 035720 Kakao — counterexample / Talk Biz beta without structural trust bridge

```text
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: TALK_BIZ_AD_PLATFORM_BETA_VS_GOVERNANCE_CONTENT_COST_DRAG
trigger_family: talk_biz_ad_recovery_beta_without_operating_leverage
trigger_date: 2024-02-15
entry_date: 2024-02-15
entry_price: 59,200
entry_basis: close
```

Evidence interpretation:

- Kakao has a natural C26 surface: KakaoTalk, Talk Biz advertising, commerce, portal ads, and platform services.
- However, early-2024 platform rebound price action did not have enough operating-leverage proof. Content, governance, regulation, and cost drag kept the ad-platform headline from becoming a durable stage transition.
- This is a useful false-positive: “large platform + ad surface + rebound candle” is not enough.

Stock-web path:

```text
Entry close: 2024-02-15 = 59,200
30D peak: 2024-02-15 high = 61,400
90D trough: 2024-04-05 low = 48,200
180D trough: 2024-09-09 low = 32,900
```

Price-path metrics:

```jsonl
{"row_type":"trigger","case_id":"R8L88_C26_KAKAO_035720_20240215_TALK_BIZ_AD_BETA","symbol":"035720","name":"카카오","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"TALK_BIZ_AD_PLATFORM_BETA_VS_GOVERNANCE_CONTENT_COST_DRAG","trigger_type":"talk_biz_ad_recovery_beta_without_operating_leverage","trigger_date":"2024-02-15","entry_date":"2024-02-15","entry_price":59200,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":3.7,"mae_30d_pct":-17.4,"mfe_90d_pct":3.7,"mae_90d_pct":-31.9,"mfe_180d_pct":3.7,"mae_180d_pct":-44.4,"peak_date":"2024-02-15","peak_price":61400,"trough_date":"2024-09-09","trough_price":32900,"case_verdict":"counterexample_false_positive_high_mae","stage2_actionable_result":"fail_without_segment_op_bridge","stage3_green_result":"fail","local_4b_watch":false,"full_4b":false,"calibration_usable":true,"do_not_count_as_new_case":false}
```

Interpretation:

Kakao is the sharpest guardrail case. C26 should penalize platform beta when governance/content/cost drag prevents ad-surface evidence from becoming a consolidated operating-profit bridge.

---

## 5. Aggregate rows

```jsonl
{"row_type":"aggregate_metric","scheduled_round":"R8","scheduled_loop":88,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"LIVE_STREAMING_SEARCH_TALK_AD_OPERATING_LEVERAGE_VS_TRAFFIC_HEADLINE_FADE","case_count":3,"positive_case_count":1,"counterexample_count":2,"local_4b_overlay_case_count":1,"calibration_usable_case_count":3,"avg_mfe_30d_pct":11.1,"avg_mae_30d_pct":-11.2,"avg_mfe_90d_pct":15.7,"avg_mae_90d_pct":-19.3,"avg_mfe_180d_pct":20.4,"avg_mae_180d_pct":-27.0,"positive_to_counterexample_ratio":"1:2","do_not_propose_new_weight_delta":true,"residual_error_type":"traffic_or_ad_headline_without_operating_leverage_bridge","current_profile_stress_result":"needs_c26_specific_bridge_guard"}
{"row_type":"residual_contribution","scheduled_round":"R8","scheduled_loop":88,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","contribution_label":"residual_error_found","new_axis_proposed":null,"existing_axis_strengthened":"c26_requires_segment_operating_leverage_bridge","existing_axis_weakened":null,"promotion_recommendation":"hold_for_more_evidence","reason":"1 positive / 2 counterexamples; sufficient to strengthen Watch/Stage2 guard wording, insufficient for new global weight delta"}
```

---

## 6. Raw component score stress test

Pre-calibration style score components can over-credit large platforms. The residual correction is to require evidence that platform traffic is monetized and flows into operating profit.

| Case | EPS/FCF explosion | Earnings visibility | Bottleneck/pricing | Market mispricing | Valuation rerating | Capital allocation | Info confidence | Raw total | Calibrated verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SOOP | 14 | 16 | 13 | 11 | 12 | 2 | 4 | 72 | Stage2 / Watch, not Green; local 4B watch after +40% |
| NAVER | 10 | 13 | 9 | 9 | 7 | 3 | 4 | 55 | Watch only; require margin durability |
| Kakao | 7 | 8 | 7 | 8 | 5 | 2 | 3 | 40 | Reject Stage2; platform beta false positive |

Key scoring stress result:

```text
C26 should not treat traffic/ad headline as equivalent to operating leverage.
```

Required bridge:

```text
C26 Stage2-Actionable requires at least two of:
1. segment ad/search/Talk revenue acceleration,
2. segment or consolidated OP margin expansion,
3. monetized user/ARPU/fill-rate/pricing evidence,
4. traffic migration with native paid-item/ad inventory monetization,
5. cost/investment drag not overwhelming platform gross profit.
```

---

## 7. 4B / 4C notes

```jsonl
{"row_type":"shadow_weight","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","axis":"local_4b_watch_guard","evidence_case_ids":["R8L88_C26_SOOP_067160_20240108_TRAFFIC_MIGRATION_OP_LEVERAGE"],"candidate_rule":"If C26 price path reaches +40%~+45% MFE while the next evidence is still traffic/share migration rather than segment OP acceleration, mark local 4B watch instead of allowing automatic Green carry.","promotion_recommendation":"hold_for_more_evidence","reason":"Only one positive-with-giveback case in this run."}
{"row_type":"shadow_weight","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","axis":"stage2_required_bridge","evidence_case_ids":["R8L88_C26_NAVER_035420_20240503_SEARCH_AD_EARNINGS_BEAT","R8L88_C26_KAKAO_035720_20240215_TALK_BIZ_AD_BETA"],"candidate_rule":"C26 Stage2-Actionable should require explicit segment-level ad/platform revenue plus operating leverage bridge; headline ad recovery or platform beta alone remains Watch.","promotion_recommendation":"hold_for_more_evidence","reason":"Two counterexamples, but NAVER later recovered by 180D; rule should be guard wording, not weight delta."}
```

No hard 4C is proposed. Kakao is a high-MAE false positive, but the evidence is not a clean thesis-break 4C because it is more “insufficient bridge” than “confirmed structural break”.

---

## 8. Novelty / duplicate check

```jsonl
{"row_type":"novelty_check","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","hard_duplicate_key_fields":"canonical_archetype_id + symbol + trigger_type + entry_date","checked_against_no_repeat_index":true,"top_repeat_symbols_avoided_or_changed":"042000,214270,237820 avoided; 035420/035720 reused only as soft-repeat with new trigger_date and trigger_type","new_symbols":"067160","soft_repeat_symbols":"035420,035720","hard_duplicate_observed":false}
```

---

## 9. Validation scope

```jsonl
{"row_type":"validation_scope","price_basis":"tradable_raw","adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","forward_window":"entry_date_to_D+180_trading_days","corporate_action_overlap":"none inside tested 180D windows","calibration_usable":true,"live_candidate_scan":false,"production_scoring_changed":false}
```

---

## 10. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working in Songdaiki/stock_agent after v12 research ingestion.

Do not treat this MD as a production patch request by itself.
Parse the machine-readable rows only after normal v12 validation / dedupe.

Research file:
e2r_stock_web_v12_residual_round_R8_loop_88_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md

Suggested guarded interpretation:
- Strengthen C26 narrative/guard tests for "platform traffic/ad headline without operating leverage bridge."
- Candidate guard axis:
  c26_requires_segment_operating_leverage_bridge
- Do not apply global score delta from this file alone.
- Do not lower Stage3 thresholds.
- Do not weaken existing price-only positive block.
- Local 4B watch may be considered for C26 cases with +40%~+45% MFE and no new OP bridge.
- Aggregate this MD with other R8/C26 rows before any runtime profile change.

Validation requirements:
- Keep only calibration_usable=true rows.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Preserve SOOP as positive-with-local-4B overlay.
- Preserve NAVER/Kakao as counterexample/high-MAE bridge-failure rows.
```

---

## 11. Final round state

```text
completed_round = R8
completed_loop = 88
next_round = R9
next_loop = 88
round_schedule_status = valid
round_sector_consistency = pass
```
