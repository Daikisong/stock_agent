# E2R v12 Residual Research — R8 / L8 / C26 PLATFORM_AD_REVENUE_OPERATING_LEVERAGE

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R8
selected_loop = 101
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id = PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_TRAFFIC_RETENTION_BRIDGE_VS_AD_RECOVERY_THEME_FALSE_POSITIVE
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_accessed = false
stock_agent_code_patch_written = false
```

## 1. Why this loop exists

`C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE` remains below the 50-row practical calibration zone.  The gap is not simply about “platforms went up or down.”  The useful separator is whether the platform has become a toll road: traffic must convert into paid impressions, commerce or item take-rate, operating leverage, and finally margin/FCF.

This loop therefore tests three distinct paths:

1. **SOOP / AfreecaTV** — platform traffic migration shock after Twitch Korea exit; strong positive path but still needs monetization proof.
2. **NAVER** — strong search-platform/commerce earnings headline that failed to hold full-window price support.
3. **Kakao** — Talk Biz / messenger-ad recovery label that produced almost no MFE and deep full-window MAE.

The research goal is not to alter production scoring now.  It is to propose a C26-specific shadow rule for later batch implementation.

## 2. Data-source validation

- Primary OHLC source: `Songdaiki/stock-web`
- Shard root: `atlas/ohlcv_tradable_by_symbol_year`
- Source basis: FinanceData/marcap transformed into assistant-readable symbol-year CSV shards
- Price basis: `tradable_raw`
- Adjustment status: `raw_unadjusted_marcap`
- Manifest max date: `2026-02-20`
- Corporate-action policy: raw/unadjusted; contaminated windows should be blocked unless no overlap exists.

## 3. Case table

| case | ticker | trigger | entry | entry close | peak | trough | MFE | MAE | classification |
|---|---:|---|---|---:|---|---|---:|---:|---|
| SOOP platform migration | 067160 | 2023-12-06 Twitch Korea exit / streaming migration | 2023-12-06 | 83,400 | 2024-02-28 / 139,600 | 2023-12-08 / 74,500 | 67.39% | -10.67% | positive |
| NAVER ad-commerce earnings | 035420 | 2024-05-03 Q1 search-platform ad + commerce earnings | 2024-05-03 | 194,600 | 2024-05-07 / 198,500 | 2024-07-04 / 159,600 | 2.0% | -17.99% | counterexample |
| Kakao Talk Biz recovery | 035720 | 2024-02-15 Q4/Talk Biz ad recovery label | 2024-02-15 | 59,200 | 2024-02-20 / 60,000 | 2024-11-14 / 32,550 | 1.35% | -45.02% | counterexample |

## 4. Case notes

### 4.1 SOOP / AfreecaTV — platform migration positive, but monetization bridge still required

Twitch announced on 2023-12-06 that it would exit South Korea effective 2024-02-27, citing high local network costs.  This created a platform traffic migration shock.  SOOP, formerly AfreecaTV, is a South Korean live-streaming platform that later relaunched under the SOOP brand in 2024.

Price path:

```text
trigger_date = 2023-12-06
entry_date = 2023-12-06
entry_close = 83,400
peak_date = 2024-02-28
peak_high = 139,600
trough_date = 2023-12-08
trough_low = 74,500
mfe_pct = 67.39%
mae_pct = -10.67%
```

Interpretation: this is the good C26 setup.  The trigger is not merely “platform theme.”  A competitor exited a local market, and the beneficiary had a direct user/creator migration route.  Still, for future production rules this should not be full Green unless it later shows paid item revenue, ad inventory fill, retention, or OPM conversion.

### 4.2 NAVER — search ad / commerce earnings headline, but full-window fade

NAVER’s Q1 2024 headline looked C26-friendly: revenue and operating profit rose, search-platform ad sales grew, and commerce revenue grew.  The price path did not validate a durable rerating.

```text
trigger_date = 2024-05-03
entry_date = 2024-05-03
entry_close = 194,600
peak_date = 2024-05-07
peak_high = 198,500
trough_date = 2024-07-04
trough_low = 159,600
mfe_pct = 2.0%
mae_pct = -17.99%
```

Interpretation: this is a C26 largecap false-positive archetype.  Search ad and commerce recovery can be true, but if capex, AI investment, competitive pressure, or multiple compression dominates the forward window, current scoring should avoid promoting the signal above Stage2 unless sustained margin/traffic-share proof is present.

### 4.3 Kakao — Talk Biz / messenger-ad recovery label with low MFE and hard MAE

Kakao’s platform structure includes Talk Biz advertising and commerce.  That makes it tempting to route any ad-recovery label into C26.  The price path says not to.

```text
trigger_date = 2024-02-15
entry_date = 2024-02-15
entry_close = 59,200
peak_date = 2024-02-20
peak_high = 60,000
trough_date = 2024-11-14
trough_low = 32,550
mfe_pct = 1.35%
mae_pct = -45.02%
```

Interpretation: this is the clean counterexample.  A messenger super-app can contain ad inventory, commerce, and user data, but that is not automatically operating leverage.  C26 should require ad revenue acceleration plus OPM expansion and no major governance/regulatory/content/capex drag.

## 5. Current calibrated profile stress test

The current stock-web calibrated profile already blocks many price-only blowoffs through:

```text
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

Residual error found here:

- SOOP can be under-scored if the engine treats platform migration as a plain theme headline.
- NAVER can be over-scored if search ad/commerce earnings are read without forward OPM and competitive/capex context.
- Kakao can be over-scored if Talk Biz / messenger ad recovery is promoted without operating leverage.

## 6. Proposed shadow rule candidate

```text
new_axis_proposed = c26_sustained_ad_revenue_op_margin_traffic_retention_bridge_required_for_stage2_actionable_shadow_only
production_scoring_changed = false
shadow_weight_only = true
```

Rule draft:

```text
For C26 platform/ad/operating leverage signals:

promote_to_stage2_actionable_only_if:
    1. ad/platform revenue acceleration is visible, and
    2. traffic/user/creator retention or share-gain evidence exists, and
    3. OPM or contribution margin is expanding, and
    4. capex/regulatory/governance/content-cost drag is not thesis-breaking

route_to_4B_or_stage2_block_if:
    - signal is only ad-recovery label,
    - only traffic migration without monetization proof,
    - largecap platform has strong earnings but forward multiple/capex/regulatory drag dominates,
    - Talk Biz / search ad / commerce terms are present without margin bridge.
```

## 7. Machine-readable rows

### 7.1 case rows

```jsonl
{"row_type":"case","research_session":"post_calibrated_sector_archetype_residual_research","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","case_id":"C26_SOOP_TWITCH_KOREA_EXIT_PLATFORM_MIGRATION_POSITIVE","ticker":"067160","name":"SOOP(구 아프리카TV)","trigger_date":"2023-12-06","entry_date":"2023-12-06","entry_price":83400,"peak_date":"2024-02-28","peak_price":139600,"trough_date":"2023-12-08","trough_price":74500,"mfe_pct":67.39,"mae_pct":-10.67,"classification":"positive","calibration_usable":true,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap"}
{"row_type":"case","research_session":"post_calibrated_sector_archetype_residual_research","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","case_id":"C26_NAVER_Q1_2024_SEARCH_AD_COMMERCE_OPERATING_PROFIT_HIGH_MAE_COUNTEREXAMPLE","ticker":"035420","name":"NAVER","trigger_date":"2024-05-03","entry_date":"2024-05-03","entry_price":194600,"peak_date":"2024-05-07","peak_price":198500,"trough_date":"2024-07-04","trough_price":159600,"mfe_pct":2.0,"mae_pct":-17.99,"classification":"counterexample","calibration_usable":true,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap"}
{"row_type":"case","research_session":"post_calibrated_sector_archetype_residual_research","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","case_id":"C26_KAKAO_Q4_2023_TALKBIZ_AD_RECOVERY_LOW_MFE_HARD_FADE","ticker":"035720","name":"카카오","trigger_date":"2024-02-15","entry_date":"2024-02-15","entry_price":59200,"peak_date":"2024-02-20","peak_price":60000,"trough_date":"2024-11-14","trough_price":32550,"mfe_pct":1.35,"mae_pct":-45.02,"classification":"counterexample","calibration_usable":true,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap"}
```

### 7.2 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"C26_TWITCH_KOREA_EXIT_USER_MIGRATION__067160__2023-12-06","case_id":"C26_SOOP_TWITCH_KOREA_EXIT_PLATFORM_MIGRATION_POSITIVE","trigger_type":"platform_user_migration_operating_leverage","evidence_family":"Twitch Korea exit -> domestic streaming traffic/creator migration -> platform monetization optionality","entry_date":"2023-12-06","entry_price":83400,"mfe_pct":67.39,"mae_pct":-10.67,"stage_current_proxy":"Stage2-Actionable / Green-watch","current_profile_error":"under-recognizes platform migration operating leverage if treated as mere theme headline","evidence_url":"https://en.wikipedia.org/wiki/Twitch_(service); https://en.wikipedia.org/wiki/Soop_(service)"}
{"row_type":"trigger","trigger_id":"C26_NAVER_Q1_SEARCH_AD_COMMERCE_EARNINGS__035420__2024-05-03","case_id":"C26_NAVER_Q1_2024_SEARCH_AD_COMMERCE_OPERATING_PROFIT_HIGH_MAE_COUNTEREXAMPLE","trigger_type":"search_platform_ad_commerce_earnings","evidence_family":"search-platform ad growth + commerce growth + operating profit beat, but competitive/AI/cost multiple drag","entry_date":"2024-05-03","entry_price":194600,"mfe_pct":2.0,"mae_pct":-17.99,"stage_current_proxy":"Stage2 only / 4B-watch","current_profile_error":"can over-score largecap platform earnings when ad recovery lacks durable rerating and capex/competition overhang remains","evidence_url":"https://www.wsj.com/articles/naver-1q-rev-krw2-526t-vs-krw2-280t-035420-se-666b7aff"}
{"row_type":"trigger","trigger_id":"C26_KAKAO_Q4_TALKBIZ_AD_RECOVERY__035720__2024-02-15","case_id":"C26_KAKAO_Q4_2023_TALKBIZ_AD_RECOVERY_LOW_MFE_HARD_FADE","trigger_type":"messenger_ad_platform_recovery","evidence_family":"Talk Biz/advertising structure and earnings-recovery label without durable operating leverage","entry_date":"2024-02-15","entry_price":59200,"mfe_pct":1.35,"mae_pct":-45.02,"stage_current_proxy":"Stage2 false positive -> 4B/4C watch","current_profile_error":"ad-recovery label can be promoted too early when regulation/content-loss/AI-cost drag remains","evidence_url":"https://www.investopedia.com/articles/investing/062315/how-kakaotalk-makes-money.asp","verified_url_repair_required":true}
```

### 7.3 score simulation rows

```jsonl
{"row_type":"score_simulation","case_id":"C26_SOOP_TWITCH_KOREA_EXIT_PLATFORM_MIGRATION_POSITIVE","baseline_current_proxy_total":76.5,"proposed_shadow_total":80.0,"stage_before":"Stage3-Yellow","stage_after_shadow":"Stage3-Yellow/Green-watch","reason":"user migration is observable and monetization leverage is plausible, but ad/ARPU proof still required"}
{"row_type":"score_simulation","case_id":"C26_NAVER_Q1_2024_SEARCH_AD_COMMERCE_OPERATING_PROFIT_HIGH_MAE_COUNTEREXAMPLE","baseline_current_proxy_total":76.0,"proposed_shadow_total":70.0,"stage_before":"Stage3-Yellow false positive risk","stage_after_shadow":"Stage2 only","reason":"ad/commerce growth did not defend the forward window; require sustained segment OPM and traffic-share proof"}
{"row_type":"score_simulation","case_id":"C26_KAKAO_Q4_2023_TALKBIZ_AD_RECOVERY_LOW_MFE_HARD_FADE","baseline_current_proxy_total":74.0,"proposed_shadow_total":63.0,"stage_before":"Stage2/Yellow false positive risk","stage_after_shadow":"Stage2 blocked / 4C-watch","reason":"Talk Biz label without durable operating leverage produced low-MFE/high-MAE path"}
```

### 7.4 aggregate rows

```jsonl
{"row_type":"aggregate","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","case_count":3,"positive_case_count":1,"counterexample_count":2,"avg_mfe_pct":23.58,"avg_mae_pct":-24.56,"shadow_rule_candidate":"c26_sustained_ad_revenue_op_margin_traffic_retention_bridge_required_for_stage2_actionable_shadow_only"}
```

### 7.5 shadow weight rows

```jsonl
{"row_type":"shadow_weight","production_scoring_changed":false,"shadow_weight_only":true,"canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","new_axis_proposed":"c26_sustained_ad_revenue_op_margin_traffic_retention_bridge_required_for_stage2_actionable_shadow_only","suggested_direction":"penalize ad/platform theme rallies unless revenue growth, OPM expansion, retention/traffic share and capex/regulatory risk are simultaneously checked","suggested_delta":"narrative_only_no_weight_delta_now"}
```

### 7.6 residual contribution rows

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","loop_contribution_label":"canonical_archetype_rule_candidate","residual_error_type":["largecap_platform_ad_recovery_false_positive","platform_migration_positive_underrecognition","operating_leverage_missing_bridge"],"batch_handoff_priority":"medium_high_after_priority1_minimum_coverage"}
```

### 7.7 narrative-only rows

```jsonl
{"row_type":"narrative_only","text":"C26 should behave like a toll road, not like a billboard. Traffic growth matters only when toll collection improves: ad revenue, ARPU, retention, operating margin and capex/regulatory drag must be connected."}
```

## 8. Residual contribution summary

```text
new_independent_case_count = 3
reused_case_count = 0
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
positive_case_count = 1
counterexample_count = 2
current_profile_error_count = 2
verified_url_repair_needed_count = 1
do_not_propose_new_weight_delta = false
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
next_recommended_archetypes = C22_INSURANCE_RATE_CYCLE_RESERVE, C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN, C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
```

## 9. Deferred Coding Agent Handoff Prompt

```text
You are a later batch coding agent.  Do not execute this prompt during the research run.

Input:
- This Markdown file is one C26 residual research artifact.
- It contains stock-web 1D OHLC-based historical cases and JSONL rows.

Task:
1. Ingest the JSONL rows only after schema validation.
2. Do not change production scoring unless multiple independent C26 artifacts support the same axis.
3. Treat the proposed rule as shadow-only:
   c26_sustained_ad_revenue_op_margin_traffic_retention_bridge_required_for_stage2_actionable_shadow_only
4. Use the SOOP case as positive platform-migration evidence only when monetization/retention is present.
5. Use NAVER and Kakao cases as counterexamples to block plain ad-recovery or platform-label promotion.
6. Keep global calibrated rules unchanged unless aggregated residual statistics justify a scoped C26 rule.
7. Preserve the no-repeat key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
```
