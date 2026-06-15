# E2R stock-web v12 residual research — R8 loop 96 / L8_PLATFORM_CONTENT_SW_SECURITY / C27_CONTENT_IP_GLOBAL_MONETIZATION

```text
schema_family = v12_sector_archetype_residual
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R8
selected_loop = 96
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id = KPOP_AND_DRAMA_CONTENT_IP_GLOBAL_PLATFORM_REPEAT_MONETIZATION_VS_HEADLINE_ONLY_FALSE_POSITIVE
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
auto_selected_coverage_gap = C27 rows 24, 30-row minimum까지 6 부족
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Selection memo

C27_CONTENT_IP_GLOBAL_MONETIZATION is still a Priority 0 thin archetype. The no-repeat index says Priority 0 should prefer new symbol, new trigger family, counterexample, 4B/4C path, and URL/source validation repair before expanding already-crowded archetypes. This run therefore avoids reusing brand-retail inventory cases and compresses C27 into a narrower question:

> Does the market response come from repeatable global IP monetization, or only from a one-off content/platform/fandom headline?

C27 should not treat every content hit, artist schedule, platform distribution, or fan-community story as equal. A true C27 Stage2-Actionable bridge needs repeatable monetization: album/tour/fan-platform revenue, recurring IP exploitation, licensing/royalty, platform distribution with margin visibility, or a visible operating-leverage/revision path. Without that bridge, a headline can look like a sunrise but behave like a flare.

## 2. Price source validation

Stock-web manifest confirms the atlas uses FinanceData/marcap, raw/unadjusted OHLC, min_date 1995-05-02, max_date 2026-02-20, tradable_row_count 14,354,401, and `atlas/ohlcv_tradable_by_symbol_year` as calibration shard root.

Validated symbol profiles and yearly shards:

| symbol | name | profile path | OHLC shard(s) used | calibration caveat |
|---|---|---|---|---|
| 035900 | JYP Ent. | `atlas/symbol_profiles/035/035900.json` | `atlas/ohlcv_tradable_by_symbol_year/035/035900/2023.csv` | active_like, KOSDAQ GLOBAL |
| 352820 | 하이브 | `atlas/symbol_profiles/352/352820.json` | `atlas/ohlcv_tradable_by_symbol_year/352/352820/2023.csv` | active_like, no corporate-action caveat |
| 253450 | 스튜디오드래곤 | `atlas/symbol_profiles/253/253450.json` | `atlas/ohlcv_tradable_by_symbol_year/253/253450/2023.csv` | active_like, no corporate-action caveat |

This run does not use live/current candidate discovery. Future price path is used only as calibration label, not as evidence available at trigger date.

## 3. Case table

| case | symbol | classification | entry | peak/trough | MFE | MAE | C27 lesson |
|---|---:|---|---:|---|---:|---:|---|
| JYP global fandom repeat monetization | 035900 | positive | 2023-02-22 @ 76,000 | peak 2023-06-21 high 140,600; trough 2023-03-16 low 68,500 | +85.00% | -9.87% | Album/tour/global fandom monetization plus operating leverage can justify Stage2-Actionable → Yellow/Green watch. |
| HYBE multi-label platform monetization | 352820 | positive with 4B watch | 2023-04-06 @ 205,000 | peak 2023-06-22 high 312,500; trough 2023-04-07 low 200,500 | +52.44% | -2.20% | Multi-label + platform/fan-community monetization can work, but full-window 4B watch should activate once price outruns fresh non-price confirmation. |
| Studio Dragon platform distribution false positive | 253450 | counterexample | 2023-02-07 @ 83,100 | peak 2023-02-09 high 84,500; trough 2023-07-10 low 48,550 | +1.68% | -41.58% | Platform/global distribution headline without repeat margin/revision bridge is not enough; should be watch-only or 4B/4C risk. |

## 4. Trigger-level notes

### 4.1 JYP Ent. — positive C27 bridge

Entry row: 2023-02-22 close 76,000. The price path then moved through the global-fandom monetization phase and reached a high of 140,600 on 2023-06-21. The path had a meaningful but tolerable interim drawdown to 68,500, then a large MFE.

Interpretation:

```text
C27 positive condition:
- multiple monetization routes exist: album, tour, fandom platform, merchandise/IP
- revenue is not one-off title exposure
- market receives evidence as repeat monetization, not only as a content hit
- drawdown is not thesis-breaking before peak
```

The calibrated profile should permit Stage2-Actionable and Stage3-Yellow here. The Green gate should still wait for revision/OPM confirmation rather than treating fandom heat alone as proof.

### 4.2 HYBE — positive but 4B watch should be earlier

Entry row: 2023-04-06 close 205,000. Forward path reached a high of 312,500 on 2023-06-22. MAE was shallow at -2.20%, so the positive case is real; however, a +50% move in a short window should force a 4B local/full-window check unless there is new non-price confirmation.

Interpretation:

```text
C27 positive with 4B watch:
- multi-label system and fan platform improve repeat monetization probability
- price path confirms Stage2/Yellow usefulness
- full-window overheat risk rises when price runs faster than revision evidence
- current profile can be right on direction but late on 4B overlay
```

This is the key residual: C27 needs both a positive unlock and a blowoff governor. A content/IP engine can be real and still become late-entry dangerous.

### 4.3 Studio Dragon — counterexample

Entry row: 2023-02-07 close 83,100. The next local high was only 84,500 on 2023-02-09; the path then decayed to a 48,550 low by 2023-07-10. The MFE/MAE shape is a classic false positive: almost no upside after trigger, large downside, and no evidence that global platform distribution translated into repeat monetization and margin.

Interpretation:

```text
C27 negative condition:
- content/platform headline exists
- repeat monetization is unclear
- margin/revision/royalty visibility is weak
- price does not validate after trigger
- should remain Stage2-watch-only or 4B/4C risk, not Stage2-Actionable
```

The failure mode is not “content business is bad.” It is narrower: platform-distribution headline without a repeat cash bridge is not an IP monetization bridge.

## 5. Current calibrated profile stress test

Current calibrated profile already has:

```text
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

Residual C27 issue:

```text
current profile can still over-credit:
- platform distribution headline
- artist/fandom buzz
- content release schedule
- global availability without monetization proof
```

Shadow fix:

```text
C27 Stage2-Actionable should require at least one monetization bridge:
1. repeatable IP revenue evidence,
2. fan platform / tour / album / licensing conversion,
3. OPM or revision visibility,
4. distribution channel that improves unit economics, not just reach.

If none exists:
- keep Stage2-watch-only
- block Yellow
- activate 4B watch if price has already run.
```

## 6. Local 4B vs full-window 4B split

| case | local 4B | full-window 4B | action |
|---|---|---|---|
| JYP | not immediate at trigger | yes after large MFE | allow positive but require post-run non-price confirmation |
| HYBE | not immediate at trigger | yes near +50% move | allow Stage2/Yellow but apply full-window 4B governor |
| Studio Dragon | not a blowoff; more like thesis decay | 4C/false-positive watch | downgrade because monetization bridge absent |

C27 should not confuse two different creatures: a runaway positive with 4B risk and a weak headline that never validates. The first needs a governor; the second needs a gate.

## 7. Proposed shadow rule candidate

```text
new_axis_proposed =
c27_repeat_ip_monetization_margin_bridge_required_for_stage2_actionable_shadow_only
```

Rule candidate:

```text
For canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION:

Stage2-Actionable unlock requires:
- content/IP evidence is repeatable, not one-off;
- monetization route is explicit: album, tour, fan platform, licensing, royalty, recurring distribution, or merchandise;
- there is at least one margin/revision/cash-conversion bridge.

Downgrade to Stage2-watch-only if:
- only platform/distribution/headline evidence exists;
- no repeat monetization proof exists;
- content production cost or margin pressure is unresolved;
- no revision or operating leverage visibility exists.

Apply full-window 4B watch if:
- MFE exceeds +45% before a fresh non-price confirmation;
- market cap expansion outruns monetization evidence;
- title/artist/platform narrative becomes price-only.
```

This is not a production patch. It is a shadow-only candidate for later batch implementation.

## 8. Machine-readable JSONL

```jsonl
{"row_type":"price_source_validation","schema_family":"v12_sector_archetype_residual","selected_round":"R8","selected_loop":96,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","price_source":"Songdaiki/stock-web","manifest_path":"atlas/manifest.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","symbols_validated":["035900","352820","253450"],"validation_scope":"symbol_profile + yearly OHLCV shard lines; no live scan; no stock_agent code access"}
{"row_type":"case","schema_family":"v12_sector_archetype_residual","case_id":"C27_JYP_2023_GLOBAL_FANDOM_REPEAT_MONETIZATION","round":"R8","loop":"96","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"KPOP_AND_DRAMA_CONTENT_IP_GLOBAL_PLATFORM_REPEAT_MONETIZATION_VS_HEADLINE_ONLY_FALSE_POSITIVE","symbol":"035900","name":"JYP Ent.","trigger_date":"2023-02-22","entry_date":"2023-02-22","entry_price":76000,"trigger_type":"stage2_actionable_content_ip_global_fandom_monetization","trigger_family":"KPOP_GLOBAL_FANDOM_ALBUM_TOUR_PLATFORM_REPEAT_MONETIZATION","evidence_family":"source_proxy_content_ip_sales_tour_platform_repeat","classification":"positive","stage_proxy":"Stage3-Yellow-to-Green-success","mfe_pct":85.0,"mae_pct":-9.87,"peak_date":"2023-06-21","peak_high":140600,"trough_date":"2023-03-16","trough_low":68500,"calibration_usable":true,"novelty_status":"same_archetype_new_symbol_or_new_trigger_family","evidence_url_status":"source_proxy_only"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","case_id":"C27_JYP_2023_GLOBAL_FANDOM_REPEAT_MONETIZATION","round":"R8","loop":"96","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"KPOP_AND_DRAMA_CONTENT_IP_GLOBAL_PLATFORM_REPEAT_MONETIZATION_VS_HEADLINE_ONLY_FALSE_POSITIVE","symbol":"035900","name":"JYP Ent.","trigger_date":"2023-02-22","entry_date":"2023-02-22","entry_price":76000,"trigger_type":"stage2_actionable_content_ip_global_fandom_monetization","trigger_family":"KPOP_GLOBAL_FANDOM_ALBUM_TOUR_PLATFORM_REPEAT_MONETIZATION","evidence_family":"source_proxy_content_ip_sales_tour_platform_repeat","mfe_pct":85.0,"mae_pct":-9.87,"peak_date":"2023-06-21","peak_high":140600,"trough_date":"2023-03-16","trough_low":68500,"aggregate_representative":true,"hard_duplicate_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|035900|stage2_actionable_content_ip_global_fandom_monetization|2023-02-22"}
{"row_type":"case","schema_family":"v12_sector_archetype_residual","case_id":"C27_HYBE_2023_MULTI_LABEL_PLATFORM_MONETIZATION","round":"R8","loop":"96","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"KPOP_AND_DRAMA_CONTENT_IP_GLOBAL_PLATFORM_REPEAT_MONETIZATION_VS_HEADLINE_ONLY_FALSE_POSITIVE","symbol":"352820","name":"하이브","trigger_date":"2023-04-06","entry_date":"2023-04-06","entry_price":205000,"trigger_type":"stage2_actionable_content_ip_platform_multilabel_monetization","trigger_family":"KPOP_MULTI_LABEL_WEVERSE_PLATFORM_TOUR_IP_MONETIZATION","evidence_family":"source_proxy_multi_label_platform_tour_fan_community","classification":"positive_with_4b_watch","stage_proxy":"Stage3-Yellow-success-but-4B-watch","mfe_pct":52.44,"mae_pct":-2.2,"peak_date":"2023-06-22","peak_high":312500,"trough_date":"2023-04-07","trough_low":200500,"calibration_usable":true,"novelty_status":"same_archetype_new_symbol_or_new_trigger_family","evidence_url_status":"source_proxy_only"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","case_id":"C27_HYBE_2023_MULTI_LABEL_PLATFORM_MONETIZATION","round":"R8","loop":"96","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"KPOP_AND_DRAMA_CONTENT_IP_GLOBAL_PLATFORM_REPEAT_MONETIZATION_VS_HEADLINE_ONLY_FALSE_POSITIVE","symbol":"352820","name":"하이브","trigger_date":"2023-04-06","entry_date":"2023-04-06","entry_price":205000,"trigger_type":"stage2_actionable_content_ip_platform_multilabel_monetization","trigger_family":"KPOP_MULTI_LABEL_WEVERSE_PLATFORM_TOUR_IP_MONETIZATION","evidence_family":"source_proxy_multi_label_platform_tour_fan_community","mfe_pct":52.44,"mae_pct":-2.2,"peak_date":"2023-06-22","peak_high":312500,"trough_date":"2023-04-07","trough_low":200500,"aggregate_representative":true,"hard_duplicate_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|352820|stage2_actionable_content_ip_platform_multilabel_monetization|2023-04-06"}
{"row_type":"case","schema_family":"v12_sector_archetype_residual","case_id":"C27_STUDIODRAGON_2023_GLOBAL_CONTENT_IP_FALSE_POSITIVE","round":"R8","loop":"96","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"KPOP_AND_DRAMA_CONTENT_IP_GLOBAL_PLATFORM_REPEAT_MONETIZATION_VS_HEADLINE_ONLY_FALSE_POSITIVE","symbol":"253450","name":"스튜디오드래곤","trigger_date":"2023-02-07","entry_date":"2023-02-07","entry_price":83100,"trigger_type":"stage2_content_ip_global_platform_headline_without_repeat_margin","trigger_family":"DRAMA_GLOBAL_PLATFORM_DISTRIBUTION_HEADLINE_NO_REPEAT_MARGIN","evidence_family":"source_proxy_content_platform_distribution_margin_pressure","classification":"counterexample","stage_proxy":"Stage2-false-positive-to-4B/4C-watch","mfe_pct":1.68,"mae_pct":-41.58,"peak_date":"2023-02-09","peak_high":84500,"trough_date":"2023-07-10","trough_low":48550,"calibration_usable":true,"novelty_status":"same_archetype_new_symbol_or_new_trigger_family","evidence_url_status":"source_proxy_only"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","case_id":"C27_STUDIODRAGON_2023_GLOBAL_CONTENT_IP_FALSE_POSITIVE","round":"R8","loop":"96","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"KPOP_AND_DRAMA_CONTENT_IP_GLOBAL_PLATFORM_REPEAT_MONETIZATION_VS_HEADLINE_ONLY_FALSE_POSITIVE","symbol":"253450","name":"스튜디오드래곤","trigger_date":"2023-02-07","entry_date":"2023-02-07","entry_price":83100,"trigger_type":"stage2_content_ip_global_platform_headline_without_repeat_margin","trigger_family":"DRAMA_GLOBAL_PLATFORM_DISTRIBUTION_HEADLINE_NO_REPEAT_MARGIN","evidence_family":"source_proxy_content_platform_distribution_margin_pressure","mfe_pct":1.68,"mae_pct":-41.58,"peak_date":"2023-02-09","peak_high":84500,"trough_date":"2023-07-10","trough_low":48550,"aggregate_representative":true,"hard_duplicate_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|253450|stage2_content_ip_global_platform_headline_without_repeat_margin|2023-02-07"}
{"row_type":"score_simulation","schema_family":"v12_sector_archetype_residual","round":"R8","loop":"96","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"KPOP_AND_DRAMA_CONTENT_IP_GLOBAL_PLATFORM_REPEAT_MONETIZATION_VS_HEADLINE_ONLY_FALSE_POSITIVE","case_id":"C27_JYP_2023_GLOBAL_FANDOM_REPEAT_MONETIZATION","symbol":"035900","baseline_proxy_stage":"Stage2-Actionable","current_calibrated_profile_stage":"Stage3-Yellow","shadow_c27_stage":"Stage3-Yellow/Green-watch","raw_component_score_breakdown":{"ip_repeat_monetization":21,"global_platform_distribution":16,"operating_leverage":14,"revision_visibility":16,"risk_penalty":-4},"alignment":"current_profile_ok","error_type":null}
{"row_type":"score_simulation","schema_family":"v12_sector_archetype_residual","round":"R8","loop":"96","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"KPOP_AND_DRAMA_CONTENT_IP_GLOBAL_PLATFORM_REPEAT_MONETIZATION_VS_HEADLINE_ONLY_FALSE_POSITIVE","case_id":"C27_HYBE_2023_MULTI_LABEL_PLATFORM_MONETIZATION","symbol":"352820","baseline_proxy_stage":"Stage2-Actionable","current_calibrated_profile_stage":"Stage3-Yellow","shadow_c27_stage":"Stage3-Yellow + full_window_4B_watch","raw_component_score_breakdown":{"ip_repeat_monetization":18,"global_platform_distribution":18,"operating_leverage":11,"revision_visibility":12,"risk_penalty":-8},"alignment":"positive_but_current_profile_too_slow_to_raise_4b_watch","error_type":"4b_watch_late_or_underweighted"}
{"row_type":"score_simulation","schema_family":"v12_sector_archetype_residual","round":"R8","loop":"96","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"KPOP_AND_DRAMA_CONTENT_IP_GLOBAL_PLATFORM_REPEAT_MONETIZATION_VS_HEADLINE_ONLY_FALSE_POSITIVE","case_id":"C27_STUDIODRAGON_2023_GLOBAL_CONTENT_IP_FALSE_POSITIVE","symbol":"253450","baseline_proxy_stage":"Stage2-Actionable","current_calibrated_profile_stage":"Stage2-Actionable_or_Yellow_false_positive","shadow_c27_stage":"Stage2-watch-only / 4B","raw_component_score_breakdown":{"ip_repeat_monetization":7,"global_platform_distribution":12,"operating_leverage":2,"revision_visibility":3,"risk_penalty":-16},"alignment":"current_profile_error","error_type":"platform_headline_without_repeat_margin_bridge_false_positive"}
{"row_type":"aggregate_metric","schema_family":"v12_sector_archetype_residual","round":"R8","loop":"96","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"KPOP_AND_DRAMA_CONTENT_IP_GLOBAL_PLATFORM_REPEAT_MONETIZATION_VS_HEADLINE_ONLY_FALSE_POSITIVE","case_count":3,"trigger_count":3,"positive_case_count":2,"counterexample_count":1,"current_profile_error_count":2,"median_mfe_pct":52.44,"median_mae_pct":-9.87,"mean_mfe_pct":46.37,"mean_mae_pct":-17.88,"residual_axis":"repeat_ip_monetization_margin_bridge_vs_headline_only_platform_distribution","do_not_propose_new_weight_delta":false}
{"row_type":"shadow_weight","schema_family":"v12_sector_archetype_residual","round":"R8","loop":"96","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"KPOP_AND_DRAMA_CONTENT_IP_GLOBAL_PLATFORM_REPEAT_MONETIZATION_VS_HEADLINE_ONLY_FALSE_POSITIVE","new_axis_proposed":"c27_repeat_ip_monetization_margin_bridge_required_for_stage2_actionable_shadow_only","shadow_rule_candidate":{"require_for_stage2_actionable":["repeatable_ip_monetization_evidence","global_platform_or_tour_distribution","margin_or_operating_leverage_bridge"],"downgrade_to_watch_only_if":["one_off_hit_only","platform_distribution_headline_only","production_cost_or_margin_pressure","no_revision_visibility"],"force_4b_watch_if":["mfe_gt_45pct_without_new_non_price_confirmation","fan_platform_headline_plus_high_multiple_compression","post_hit_revenue_gap"]},"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","schema_family":"v12_sector_archetype_residual","round":"R8","loop":"96","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"KPOP_AND_DRAMA_CONTENT_IP_GLOBAL_PLATFORM_REPEAT_MONETIZATION_VS_HEADLINE_ONLY_FALSE_POSITIVE","loop_contribution_label":"canonical_archetype_rule_candidate","new_axis_proposed":"c27_repeat_ip_monetization_margin_bridge_required_for_stage2_actionable_shadow_only","existing_axis_strengthened":"full_4b_requires_non_price_evidence scoped to C27 content/IP headline and fandom-platform blowoff","existing_axis_weakened":null,"next_recommended_archetypes":["C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","C13_BATTERY_JV_UTILIZATION_AMPC_IRA","C24_BIO_TRIAL_DATA_EVENT_RISK"]}
{"row_type":"coverage_matrix","schema_family":"v12_sector_archetype_residual","round":"R8","loop":"96","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","selected_priority_bucket":"Priority 0","auto_selected_coverage_gap":"C27 rows 24, 30-row minimum까지 6 부족","new_independent_case_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3}
```

## 9. Residual contribution summary

```text
new_independent_case_count = 3
reused_case_count = 0
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
positive_case_count = 2
counterexample_count = 1
current_profile_error_count = 2
diversity_score_summary = C27 Priority 0 부족권 + K-pop fandom/platform positive와 drama platform headline false positive를 분리
do_not_propose_new_weight_delta = false
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
new_axis_proposed = c27_repeat_ip_monetization_margin_bridge_required_for_stage2_actionable_shadow_only
existing_axis_strengthened = full_4b_requires_non_price_evidence scoped to C27 content/IP headline and fandom-platform blowoff
existing_axis_weakened = null
next_recommended_archetypes = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK, C13_BATTERY_JV_UTILIZATION_AMPC_IRA, C24_BIO_TRIAL_DATA_EVENT_RISK
```

## 10. Deferred Coding Agent Handoff Prompt

```text
You are the later batch implementation coding agent for stock_agent.

Do not treat this MD as an immediate patch request. First ingest all v12 residual MD files and run the normal parser/validation/dedupe/aggregate pipeline.

Candidate axis from this MD:
c27_repeat_ip_monetization_margin_bridge_required_for_stage2_actionable_shadow_only

Scope:
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION

Intent:
C27 should require a repeat monetization and margin/revision bridge before Stage2-Actionable or Yellow promotion. Platform/headline/content-hit evidence alone should remain watch-only. For positive cases whose price path validates but already produced large MFE, full-window 4B watch should be applied unless there is new non-price confirmation.

Implementation constraints:
- Keep production_scoring_changed=false until batch promotion planner approves.
- Preserve stage3_green_total_min and stage3_green_revision_min.
- Do not loosen Green.
- Add only shadow rule candidate rows unless aggregate evidence clears promotion gates.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
```
