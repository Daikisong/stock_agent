# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

- research_session: `post_calibrated_sector_archetype_residual_research`
- mode: `historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12`
- round: `R13`
- loop: `37`
- large_sector_id: `L8_PLATFORM_CONTENT_SW_SECURITY`
- canonical_archetype_id: `C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE`
- fine_archetype_id: `OWNED_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE`
- output_file: `e2r_stock_web_v12_residual_round_R13_loop_37_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md`
- live_candidate_mode: `false`
- current_stock_discovery_allowed: `false`
- stock_agent_code_access_allowed: `false`
- stock_agent_code_patch_allowed: `false`
- production_scoring_changed: `false`
- shadow_weight_only: `true`

This file is historical calibration research only. It is not a live watchlist, investment recommendation, or repository patch.


## 1. Current Calibrated Profile Assumption

Current profile proxy:

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This loop does not re-propose those global axes. It stress-tests them inside C26 and proposes only shadow sector/canonical rules.


## 2. Round / Large Sector / Canonical Archetype Scope

- large_sector_id: `L8_PLATFORM_CONTENT_SW_SECURITY`
- canonical_archetype_id: `C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE`
- fine_archetype_id: `OWNED_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE`
- selected loop objectives:
  - `holdout_validation`
  - `residual_missed_structural_mining`
  - `yellow_threshold_stress_test`
  - `green_strictness_stress_test`
  - `stage2_actionable_bonus_stress_test`
  - `4B_non_price_requirement_stress_test`
  - `4C_thesis_break_timing_test`
  - `sector_specific_rule_discovery`
  - `canonical_archetype_compression`
  - `counterexample_mining`
  - `coverage_gap_fill`

C26 is compressed as: **owned platform ad / traffic monetization operating leverage**. The key residual question is whether the score distinguishes a platform that owns traffic/inventory/retention from an advertising agency or media-rep recovery that merely rides the same ad cycle.


## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifacts were used only for coverage and duplicate avoidance.

- discovered_result_md_count: 107
- validated_trigger_rows: 1940
- aggregate_representative_trigger_rows: 1376
- rounds_covered: R1~R13
- loops_covered: 1~9
- applied global axes already include Stage2 bonus, stricter Green, price-only blowoff guard, non-price 4B requirement, and hard 4C thesis-break routing.

Novelty decision:

```text
required_new_independent_case_ratio = 0.60
calibration_usable_cases = 4
new_independent_cases = 4
new_independent_case_ratio = 1.00
loop_contribution_label = canonical_archetype_rule_candidate
```

No `stock_agent/src/e2r` code was opened or inferred.


## 4. Stock-Web OHLC Input / Price Source Validation

```json
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

Manifest fields used:

```json
{
  "source_name": "FinanceData/marcap",
  "source_repo_url": "https://github.com/FinanceData/marcap",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "min_date": "1995-05-02",
  "max_date": "2026-02-20",
  "tradable_row_count": 14354401,
  "raw_row_count": 15214118,
  "symbol_count": 5414,
  "active_like_symbol_count": 2868,
  "inactive_or_delisted_like_symbol_count": 2546,
  "markets": [
    "KONEX",
    "KOSDAQ",
    "KOSDAQ GLOBAL",
    "KOSPI"
  ],
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv"
}
```

Schema basis:

```text
tradable shard columns = d,o,h,l,c,v,a,mc,s,m
raw shard columns      = d,o,h,l,c,v,a,mc,s,m,rs
price_basis            = tradable_raw
price_adjustment_status= raw_unadjusted_marcap
```

All quantitative rows below use `atlas/ohlcv_tradable_by_symbol_year`.


## 5. Historical Eligibility Gate

|symbol|profile_path|first_date|last_date|trading_day_count|corporate_action_candidate_dates|eligibility_decision|
|---|---|---|---|---|---|---|
|035420|atlas/symbol_profiles/035/035420.json|2002-10-29|2026-02-20|5730|2004-02-26;2004-03-26;2006-07-14;2006-08-16;2013-08-29;2018-10-12|candidate windows blocked; 2020-2021 window clean|
|035720|atlas/symbol_profiles/035/035720.json|1999-11-11|2026-02-20|6457|2000-02-03;2000-03-03;2006-05-19;2014-10-14;2021-04-15|post-2021-04-15 windows used only|
|067160|atlas/symbol_profiles/067/067160.json|2003-12-19|2026-02-20|5450|2005-12-27;2007-06-05;2007-06-14;2008-01-24;2011-01-27|2021 window clean|
|089600|atlas/symbol_profiles/089/089600.json|2013-07-17|2026-02-20|3090|[]|clean|


## 6. Canonical Archetype Compression Map

```text
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE

fine_archetype compression:
- OWNED_SEARCH_DISPLAY_COMMERCE_AD_LEVERAGE       -> C26
- MESSAGING_PLATFORM_TALK_BIZ_AD_LEVERAGE         -> C26
- CREATOR_STREAMING_PLATFORM_TRAFFIC_MONETIZATION -> C26
- AD_AGENCY_MEDIA_REP_CYCLICAL_RECOVERY           -> C26 counterexample / guard
```

C26 should not be a generic "ad sales went up" bucket. The scoring distinction is whether the business has **owned demand, owned inventory, repeat advertiser/merchant routing, and operating leverage**.


## 7. Case Selection Summary

|case_id|symbol|company_name|case_type|positive_or_counterexample|best_trigger|current_profile_verdict|
|---|---|---|---|---|---|---|
|C26_NAVER_2020_AD_COMMERCE_OPERATING_LEVERAGE|035420|NAVER|structural_success|positive|TRG_C26_NAVER_2020_STAGE2_ACTIONABLE|current_profile_too_late|
|C26_KAKAO_2021_TALK_BIZ_REGULATORY_4B|035720|카카오|4B_overlay_success|positive_then_4B|TRG_C26_KAKAO_2021_STAGE2_ACTIONABLE|current_profile_4B_too_late|
|C26_SOOP_2021_CREATOR_PLATFORM_OPERATING_LEVERAGE|067160|SOOP|structural_success|positive|TRG_C26_SOOP_2021_STAGE2_ACTIONABLE|current_profile_correct|
|C26_NASMEDIA_2021_AD_AGENCY_FALSE_POSITIVE|089600|KT나스미디어|false_positive_green|counterexample|TRG_C26_NASMEDIA_2021_STAGE2_ACTIONABLE|current_profile_false_positive|


## 8. Positive vs Counterexample Balance

```text
positive_structural_success = 2
positive_then_4B = 1
counterexample_or_failed_rerating = 1
4B_or_4C_case = 1
minimum_calibration_usable_case_count = 3
actual_calibration_usable_case_count = 4
```

The balance is usable for a canonical-archetype-specific shadow rule because the case set includes both owned-platform successes and one agency/media-rep counterexample.


## 9. Evidence Source Map

| case_id | trigger evidence family | Stage2 evidence | Stage3 evidence | 4B/4C evidence |
|---|---|---|---|---|
| C26_NAVER_2020_AD_COMMERCE_OPERATING_LEVERAGE | earnings/IR + search/display/commerce route | ad resilience, commerce/pay traffic, relative strength | later financial confirmation | none |
| C26_KAKAO_2021_TALK_BIZ_REGULATORY_4B | earnings/IR + post-split price rows + platform regulation | Talk Biz and platform operating leverage | later revision visibility | non-price regulatory overhang becomes 4B overlay |
| C26_SOOP_2021_CREATOR_PLATFORM_OPERATING_LEVERAGE | earnings/IR + creator traffic/paid-item monetization | owned traffic and monetization | margin bridge and durable user/customer route | none |
| C26_NASMEDIA_2021_AD_AGENCY_FALSE_POSITIVE | earnings/IR + ad recovery narrative | advertising cycle recovery | limited financial visibility | agency/pass-through guard; no owned-platform retention |

No trigger is created from price action alone.


## 10. Price Data Source Map

|symbol|company_name|price_shard_examples|profile_path|corporate_action_window_status|
|---|---|---|---|---|
|035420|NAVER|atlas/ohlcv_tradable_by_symbol_year/035/035420/2020.csv; 2021.csv|atlas/symbol_profiles/035/035420.json|clean_180D_window|
|035720|카카오|atlas/ohlcv_tradable_by_symbol_year/035/035720/2021.csv; 2022.csv|atlas/symbol_profiles/035/035720.json|post-2021-04-15 only; clean_180D_window|
|067160|SOOP|atlas/ohlcv_tradable_by_symbol_year/067/067160/2021.csv|atlas/symbol_profiles/067/067160.json|clean_180D_window|
|089600|KT나스미디어|atlas/ohlcv_tradable_by_symbol_year/089/089600/2021.csv|atlas/symbol_profiles/089/089600.json|clean_180D_window|


## 11. Case-by-Case Trigger Grid

|trigger_id|case_id|trigger_type|trigger_date|entry_date|entry_price|trigger_outcome_label|current_profile_verdict|aggregate_group_role|
|---|---|---|---|---|---|---|---|---|
|TRG_C26_NAVER_2020_STAGE2_ACTIONABLE|C26_NAVER_2020_AD_COMMERCE_OPERATING_LEVERAGE|Stage2-Actionable|2020-07-30|2020-07-31|301000|structural_success|current_profile_too_late|representative|
|TRG_C26_NAVER_2021_STAGE3_YELLOW_COMPARISON|C26_NAVER_2020_AD_COMMERCE_OPERATING_LEVERAGE|Stage3-Yellow|2021-01-28|2021-01-29|343000|late_but_valid_yellow|current_profile_too_late|label_comparison_only|
|TRG_C26_KAKAO_2021_STAGE2_ACTIONABLE|C26_KAKAO_2021_TALK_BIZ_REGULATORY_4B|Stage2-Actionable|2021-05-06|2021-05-07|114500|structural_success_then_regulatory_4B|current_profile_4B_too_late|representative|
|TRG_C26_KAKAO_2021_4B_REGULATORY_OVERLAY|C26_KAKAO_2021_TALK_BIZ_REGULATORY_4B|4B|2021-09-07|2021-09-07|154000|4B_overlay_success|current_profile_4B_too_late|4B_overlay_only|
|TRG_C26_SOOP_2021_STAGE2_ACTIONABLE|C26_SOOP_2021_CREATOR_PLATFORM_OPERATING_LEVERAGE|Stage2-Actionable|2021-04-30|2021-05-03|89500|structural_success|current_profile_correct|representative|
|TRG_C26_SOOP_2021_STAGE3_GREEN_COMPARISON|C26_SOOP_2021_CREATOR_PLATFORM_OPERATING_LEVERAGE|Stage3-Green|2021-07-27|2021-07-27|136600|green_not_too_late|current_profile_correct|label_comparison_only|
|TRG_C26_NASMEDIA_2021_STAGE2_ACTIONABLE|C26_NASMEDIA_2021_AD_AGENCY_FALSE_POSITIVE|Stage2-Actionable|2021-05-06|2021-05-07|36950|failed_structural_rerating|current_profile_false_positive|representative|
|TRG_C26_NASMEDIA_2021_STAGE3_YELLOW_FALSE_POSITIVE|C26_NASMEDIA_2021_AD_AGENCY_FALSE_POSITIVE|Stage3-Yellow|2021-06-18|2021-06-18|43300|false_positive_yellow|current_profile_false_positive|label_comparison_only|


## 12. Trigger-Level OHLC Backtest Tables

|trigger_id|entry_date|entry_price|MFE_30D_pct|MAE_30D_pct|MFE_90D_pct|MAE_90D_pct|MFE_180D_pct|MAE_180D_pct|peak_date|peak_price|drawdown_after_peak_pct|corporate_action_window_status|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|TRG_C26_NAVER_2020_STAGE2_ACTIONABLE|2020-07-31|301000|15.28|-0.33|15.28|-9.14|36.21|-9.14|2021-03-18|410000|-18.41|clean_180D_window|
|TRG_C26_NAVER_2021_STAGE3_YELLOW_COMPARISON|2021-01-29|343000|18.22|-0.44|19.53|-2.48|19.53|-2.48|2021-03-18|410000|-18.41|clean_180D_window|
|TRG_C26_KAKAO_2021_STAGE2_ACTIONABLE|2021-05-07|114500|37.55|-5.68|51.09|-5.68|51.09|-28.21|2021-06-24|173000|-52.49|clean_180D_window|
|TRG_C26_KAKAO_2021_4B_REGULATORY_OVERLAY|2021-09-07|154000|1.3|-28.25|1.3|-28.25|1.3|-46.62|2021-09-08|156000|-47.05|clean_180D_window|
|TRG_C26_SOOP_2021_STAGE2_ACTIONABLE|2021-05-03|89500|25.59|-2.01|91.4|-2.01|178.32|-2.01|2021-11-09|249100|-35.0|clean_180D_window|
|TRG_C26_SOOP_2021_STAGE3_GREEN_COMPARISON|2021-07-27|136600|19.99|-6.3|82.36|-6.3|82.36|-26.06|2021-11-09|249100|-35.0|clean_180D_window|
|TRG_C26_NASMEDIA_2021_STAGE2_ACTIONABLE|2021-05-07|36950|17.19|-5.28|21.52|-5.41|21.52|-10.69|2021-06-24|44900|-26.5|clean_180D_window|
|TRG_C26_NASMEDIA_2021_STAGE3_YELLOW_FALSE_POSITIVE|2021-06-18|43300|3.7|-11.2|3.7|-23.79|3.7|-23.79|2021-06-24|44900|-26.5|clean_180D_window|


## 13. Current Calibrated Profile Stress Test

| case_id | current profile decision | actual MFE/MAE alignment | residual verdict |
|---|---|---|---|
| C26_NAVER_2020_AD_COMMERCE_OPERATING_LEVERAGE | Stage2 likely passes, Green waits for stronger revision | Stage2 MFE_180D +36.21%, MAE_180D -9.14% | `current_profile_too_late` |
| C26_KAKAO_2021_TALK_BIZ_REGULATORY_4B | Stage2 correct; 4B needs non-price evidence | Stage2 MFE_90D +51.09%, later 4B overlay avoids deep drawdown | `current_profile_4B_too_late` |
| C26_SOOP_2021_CREATOR_PLATFORM_OPERATING_LEVERAGE | Stage2/Yellow works | Stage2 MFE_180D +178.32%, MAE_180D -2.01% | `current_profile_correct` |
| C26_NASMEDIA_2021_AD_AGENCY_FALSE_POSITIVE | Stage2/Yellow may over-promote on ad-cycle recovery | MFE_90D +21.52% but drawdown after peak -26.50% and no durable rerating | `current_profile_false_positive` |

Existing global axes are kept. The residual is C26-specific: owned-platform retention should promote; ad-agency pass-through should cap.


## 14. Stage2 / Yellow / Green Comparison

| comparison | Stage2 entry | later Yellow/Green entry | peak after Stage2 | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---:|---|
| NAVER | 301000 | 343000 | 410000 | 0.385 | Green/Yellow not disastrous, but Stage2 captured materially better asymmetry |
| SOOP | 89500 | 136600 | 249100 | 0.295 | Green was not too late because 2Q confirmation still left large upside |
| Nasmedia | 36950 | 43300 | 44900 | 0.799 | Late Yellow near local peak; should be capped by pass-through guard |
| Kakao | 114500 | n/a | 173000 | n/a | The key issue was 4B non-price overlay, not Green lateness |

C26 needs a split gate: Stage2 can be early when the platform owns the traffic/inventory, but late Yellow/Green can be a false-positive when the stock is only an ad-cycle proxy.


## 15. 4B Local vs Full-window Timing Audit

| trigger_id | four_b_evidence_type | local_peak_proximity | full_window_peak_proximity | timing verdict |
|---|---|---:|---:|---|
| TRG_C26_KAKAO_2021_4B_REGULATORY_OVERLAY | legal_or_regulatory_block; explicit_event_cap; positioning_overheat | 0.675 | 0.675 | good_non_price_4B_risk_overlay_before_full_thesis_break |
| TRG_C26_NASMEDIA_2021_STAGE3_YELLOW_FALSE_POSITIVE | valuation_blowoff; margin_or_backlog_slowdown | 0.799 | 0.799 | false_positive_late_yellow_near_local_top |

This keeps the applied global guard intact: price-only local peak is still not a full 4B. Kakao's 4B is non-price, while Nasmedia's late Yellow acts as a counterexample guard.


## 16. 4C Protection Audit

- Kakao: `hard_4c_watch_before_full_thesis_break`. The 2021-09 regulatory event is better coded as 4B overlay first. Full 4C requires thesis evidence to break, not only price decline.
- Nasmedia: `false_break`. The signal should be blocked before becoming Green rather than routed as a late 4C.
- NAVER/SOOP: no hard 4C evidence in the calibration window.


## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = c26_dominant_platform_regulatory_4b_overlay
scope = L8_PLATFORM_CONTENT_SW_SECURITY
proposal_type = sector_shadow_only
delta = +1 risk overlay, not positive promotion
```

When a dominant consumer/platform business is already in a C26 positive stage, explicit non-price regulation/fee/platform-governance intervention can trigger a 4B overlay before EPS revisions fully roll over. This is not a price-only 4B and does not weaken the global non-price 4B requirement.


## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
axis_1 = c26_owned_platform_inventory_bonus
axis_2 = c26_ad_agency_pass_through_guard
canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
```

Proposed C26 compression:

- Promote when evidence shows owned traffic, owned ad inventory, first-party audience data, repeat advertiser/merchant route, and margin bridge.
- Cap when evidence is only ad-market recovery, media-rep/agency pass-through, or one-off campaign spend without retention.
- Treat dominant-platform regulation as 4B/4C risk, not as a negative score inside Stage2 itself.


## 19. Before / After Backtest Comparison

|profile_id|scope|hypothesis|eligible_trigger_count|avg_MFE_90D_pct|avg_MAE_90D_pct|false_positive_rate|missed_structural_count|late_green_count|verdict|
|---|---|---|---|---|---|---|---|---|---|
|P0 e2r_2_1_stock_web_calibrated_proxy|global current|Current global calibration without C26-specific owned-platform/agency split|4|44.82|-5.56|25%|1|1|good global base but residual sector/archetype errors remain|
|P0b e2r_2_0_baseline_reference|rollback reference|Older baseline, no Stage2 bonus / weaker 4B/4C routing|4|44.82|-5.56|25%|2|2|too late for NAVER/SOOP and still unable to guard Nasmedia|
|P1 sector_specific_candidate_profile|L8 sector shadow|L8 dominant-platform regulatory 4B overlay is allowed before earnings thesis break|4|44.82|-5.56|25%|1|1|improves Kakao 4B timing without weakening non-price 4B requirement|
|P2 canonical_archetype_candidate_profile|C26 shadow|Owned inventory / first-party traffic / advertiser retention promote; agency pass-through caps|4|52.59|-5.61|0% after guard|0|1|best score-return alignment for C26|
|P3 counterexample_guard_profile|C26 guard|Ad recovery without owned-platform retention cannot cross Yellow/Green|4|44.82|-5.56|0% for agency-like rows|1|1|safer, but should not suppress owned-platform cases|


## 20. Score-Return Alignment Matrix

|trigger_id|weighted_score_before|stage_label_before|weighted_score_after|stage_label_after|MFE_90D_pct|MAE_90D_pct|score_return_alignment_label|current_profile_verdict|
|---|---|---|---|---|---|---|---|---|
|TRG_C26_NAVER_2020_STAGE2_ACTIONABLE|74|Stage2-Actionable|78|Stage3-Yellow|15.28|-9.14|risk_overlay|current_profile_too_late|
|TRG_C26_NAVER_2021_STAGE3_YELLOW_COMPARISON|72|label_comparison_only|72|label_comparison_only|19.53|-2.48|risk_overlay|current_profile_too_late|
|TRG_C26_KAKAO_2021_STAGE2_ACTIONABLE|76|Stage2-Actionable|80|Stage3-Yellow|51.09|-5.68|aligned|current_profile_4B_too_late|
|TRG_C26_KAKAO_2021_4B_REGULATORY_OVERLAY|72|label_comparison_only|72|label_comparison_only|1.3|-28.25|risk_overlay|current_profile_4B_too_late|
|TRG_C26_SOOP_2021_STAGE2_ACTIONABLE|79|Stage3-Yellow|84|Stage3-Yellow|91.4|-2.01|aligned|current_profile_correct|
|TRG_C26_SOOP_2021_STAGE3_GREEN_COMPARISON|72|label_comparison_only|72|label_comparison_only|82.36|-6.3|aligned|current_profile_correct|
|TRG_C26_NASMEDIA_2021_STAGE2_ACTIONABLE|76|Stage3-Yellow|70|Stage2|21.52|-5.41|aligned|current_profile_false_positive|
|TRG_C26_NASMEDIA_2021_STAGE3_YELLOW_FALSE_POSITIVE|72|label_comparison_only|72|label_comparison_only|3.7|-23.79|false_positive_guard_needed|current_profile_false_positive|


## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|L8_PLATFORM_CONTENT_SW_SECURITY|C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|OWNED_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|3|1|1|0|4|0|8|4|3|True|True|C26 now has owned-platform positives plus ad-agency counterexample; still needs more global ad-tech / app-store / marketplace holdouts.|


## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - stage3_cross_evidence_green_buffer
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - current_profile_too_late
  - current_profile_false_positive
  - current_profile_4B_too_late
new_axis_proposed:
  - c26_owned_platform_inventory_bonus
  - c26_ad_agency_pass_through_guard
  - c26_dominant_platform_regulatory_4b_overlay
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - stage3_cross_evidence_green_buffer
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
```


## 23. Validation Scope / Non-Validation Scope

Validation scope:

- Historical trigger-level calibration only.
- Actual stock-web 1D OHLCV rows from tradable shards.
- 180D windows clean of corporate-action contamination.
- Current calibrated profile stress test.
- C26-specific score-return alignment and counterexample guard.

Non-validation scope:

- No current/live candidate discovery.
- No 2026 live scan.
- No automated trading or brokerage API.
- No `stock_agent/src/e2r` code review.
- No production scoring change.
- No investment recommendation language.


## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c26_owned_platform_inventory_bonus,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,1,+1,"Owned inventory/first-party traffic separated NAVER/Kakao/SOOP positives from ad-agency bounce.","Improved score-return alignment for 3 positives while not promoting Nasmedia",TRG_C26_NAVER_2020_STAGE2_ACTIONABLE|TRG_C26_KAKAO_2021_STAGE2_ACTIONABLE|TRG_C26_SOOP_2021_STAGE2_ACTIONABLE|TRG_C26_NASMEDIA_2021_STAGE2_ACTIONABLE,4,4,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c26_ad_agency_pass_through_guard,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,1,+1,"Agency/media-rep recovery without owned-platform retention had weak forward alignment.","Reduced false positive Yellow/Green risk in Nasmedia",TRG_C26_NASMEDIA_2021_STAGE2_ACTIONABLE|TRG_C26_NASMEDIA_2021_STAGE3_YELLOW_FALSE_POSITIVE,2,1,1,medium,counterexample_guard_shadow_only,"not production; post-calibrated residual"
shadow_weight,c26_dominant_platform_regulatory_4b_overlay,sector_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,1,+1,"Non-price regulatory overhang protected better than price-only local peak logic in dominant platforms.","Converted late positive continuation into 4B overlay for Kakao",TRG_C26_KAKAO_2021_4B_REGULATORY_OVERLAY,1,1,0,low,sector_shadow_only,"risk overlay only; not positive promotion"
```


## 25. Machine-Readable Rows

### 25.1 JSONL

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "C26_NAVER_2020_AD_COMMERCE_OPERATING_LEVERAGE", "symbol": "035420", "company_name": "NAVER", "round": "R13", "loop": "37", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "OWNED_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "TRG_C26_NAVER_2020_STAGE2_ACTIONABLE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Stage2 caught the move before later confirmed revision, but Green confirmation arrived after a meaningful part of the upside.", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "Owned search/display platform plus commerce/pay route; not a pure price-only move."}
{"row_type": "case", "case_id": "C26_KAKAO_2021_TALK_BIZ_REGULATORY_4B", "symbol": "035720", "company_name": "카카오", "round": "R13", "loop": "37", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "OWNED_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "case_type": "4B_overlay_success", "positive_or_counterexample": "positive_then_4B", "best_trigger": "TRG_C26_KAKAO_2021_STAGE2_ACTIONABLE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Early Talk Biz platform leverage was real, but non-price regulatory risk became a better 4B overlay than price-only peak logic.", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "Uses post-2021-04-15 stock split window only; pre-split windows are not used for calibration."}
{"row_type": "case", "case_id": "C26_SOOP_2021_CREATOR_PLATFORM_OPERATING_LEVERAGE", "symbol": "067160", "company_name": "SOOP", "round": "R13", "loop": "37", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "OWNED_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "TRG_C26_SOOP_2021_STAGE2_ACTIONABLE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Owned traffic, paid item/ad inventory, and margin leverage aligned with a very strong 180D MFE and low early MAE.", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Name at trigger date was 아프리카TV; current profile name is SOOP."}
{"row_type": "case", "case_id": "C26_NASMEDIA_2021_AD_AGENCY_FALSE_POSITIVE", "symbol": "089600", "company_name": "KT나스미디어", "round": "R13", "loop": "37", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "OWNED_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "TRG_C26_NASMEDIA_2021_STAGE2_ACTIONABLE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Advertising recovery produced a tradable bounce, but lacked durable owned-platform retention and faded before a structural rerating.", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Current latest name is KT나스미디어; trigger-period name was 나스미디어."}
{"row_type": "trigger", "trigger_id": "TRG_C26_NAVER_2020_STAGE2_ACTIONABLE", "case_id": "C26_NAVER_2020_AD_COMMERCE_OPERATING_LEVERAGE", "symbol": "035420", "company_name": "NAVER", "round": "R13", "loop": "37", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "OWNED_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "owned platform search/display ad + commerce operating leverage", "loop_objective": ["holdout_validation", "residual_missed_structural_mining", "yellow_threshold_stress_test", "green_strictness_stress_test", "stage2_actionable_bonus_stress_test", "4B_non_price_requirement_stress_test", "4C_thesis_break_timing_test", "sector_specific_rule_discovery", "canonical_archetype_compression", "counterexample_mining", "coverage_gap_fill"], "trigger_type": "Stage2-Actionable", "trigger_date": "2020-07-30", "evidence_available_at_that_date": "2Q20 public earnings/IR evidence: search/display ad resilience plus commerce/fintech route; public and tradable by next close.", "evidence_source": "NAVER 2Q20 earnings/IR and DART semiannual filing cross-check", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/035/035420/2020.csv", "profile_path": "atlas/symbol_profiles/035/035420.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2020-07-31", "entry_price": 301000, "MFE_30D_pct": 15.28, "MFE_90D_pct": 15.28, "MFE_180D_pct": 36.21, "MFE_1Y_pct": 54.49, "MFE_2Y_pct": 54.49, "MAE_30D_pct": -0.33, "MAE_90D_pct": -9.14, "MAE_180D_pct": -9.14, "MAE_1Y_pct": -9.14, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-03-18", "peak_price": 410000, "drawdown_after_peak_pct": -18.41, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C26_NAVER_2020_2020-07-31_301000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_C26_NAVER_2021_STAGE3_YELLOW_COMPARISON", "case_id": "C26_NAVER_2020_AD_COMMERCE_OPERATING_LEVERAGE", "symbol": "035420", "company_name": "NAVER", "round": "R13", "loop": "37", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "OWNED_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "owned platform search/display ad + commerce operating leverage", "loop_objective": ["holdout_validation", "residual_missed_structural_mining", "yellow_threshold_stress_test", "green_strictness_stress_test", "stage2_actionable_bonus_stress_test", "4B_non_price_requirement_stress_test", "4C_thesis_break_timing_test", "sector_specific_rule_discovery", "canonical_archetype_compression", "counterexample_mining", "coverage_gap_fill"], "trigger_type": "Stage3-Yellow", "trigger_date": "2021-01-28", "evidence_available_at_that_date": "Later confirmed earnings/revision evidence; used only to compare Green/Yellow lateness versus Stage2-Actionable.", "evidence_source": "NAVER 4Q20/FY20 earnings/IR", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "multiple_public_sources", "financial_visibility", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/035/035420/2021.csv", "profile_path": "atlas/symbol_profiles/035/035420.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-01-29", "entry_price": 343000, "MFE_30D_pct": 18.22, "MFE_90D_pct": 19.53, "MFE_180D_pct": 19.53, "MFE_1Y_pct": 19.53, "MFE_2Y_pct": 19.53, "MAE_30D_pct": -0.44, "MAE_90D_pct": -2.48, "MAE_180D_pct": -2.48, "MAE_1Y_pct": -16.03, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-03-18", "peak_price": 410000, "drawdown_after_peak_pct": -18.41, "green_lateness_ratio": 0.385, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "late_but_valid_yellow", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C26_NAVER_2021_2021-01-29_343000", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": false, "reuse_reason": null, "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "TRG_C26_KAKAO_2021_STAGE2_ACTIONABLE", "case_id": "C26_KAKAO_2021_TALK_BIZ_REGULATORY_4B", "symbol": "035720", "company_name": "카카오", "round": "R13", "loop": "37", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "OWNED_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "messaging platform ad/commerce operating leverage with dominant-platform regulation risk", "loop_objective": ["holdout_validation", "residual_missed_structural_mining", "yellow_threshold_stress_test", "green_strictness_stress_test", "stage2_actionable_bonus_stress_test", "4B_non_price_requirement_stress_test", "4C_thesis_break_timing_test", "sector_specific_rule_discovery", "canonical_archetype_compression", "counterexample_mining", "coverage_gap_fill"], "trigger_type": "Stage2-Actionable", "trigger_date": "2021-05-06", "evidence_available_at_that_date": "Q1 platform/Talk Biz operating leverage after the stock split; public and tradable after split, avoiding the 2021-04-15 contaminated window.", "evidence_source": "Kakao 1Q21 earnings/IR and post-split tradable stock-web rows", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["financial_visibility", "multiple_public_sources", "confirmed_revision"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/035/035720/2021.csv", "profile_path": "atlas/symbol_profiles/035/035720.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-05-07", "entry_price": 114500, "MFE_30D_pct": 37.55, "MFE_90D_pct": 51.09, "MFE_180D_pct": 51.09, "MFE_1Y_pct": 51.09, "MFE_2Y_pct": 51.09, "MAE_30D_pct": -5.68, "MAE_90D_pct": -5.68, "MAE_180D_pct": -28.21, "MAE_1Y_pct": -44.8, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-06-24", "peak_price": 173000, "drawdown_after_peak_pct": -52.49, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "watch_only_until_regulatory_thesis_break", "trigger_outcome_label": "structural_success_then_regulatory_4B", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C26_KAKAO_2021_2021-05-07_114500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_C26_KAKAO_2021_4B_REGULATORY_OVERLAY", "case_id": "C26_KAKAO_2021_TALK_BIZ_REGULATORY_4B", "symbol": "035720", "company_name": "카카오", "round": "R13", "loop": "37", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "OWNED_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "messaging platform ad/commerce operating leverage with dominant-platform regulation risk", "loop_objective": ["holdout_validation", "residual_missed_structural_mining", "yellow_threshold_stress_test", "green_strictness_stress_test", "stage2_actionable_bonus_stress_test", "4B_non_price_requirement_stress_test", "4C_thesis_break_timing_test", "sector_specific_rule_discovery", "canonical_archetype_compression", "counterexample_mining", "coverage_gap_fill"], "trigger_type": "4B", "trigger_date": "2021-09-07", "evidence_available_at_that_date": "Non-price 4B evidence: dominant-platform regulatory/fee/financial-platform overhang became explicit before the full earnings thesis broke.", "evidence_source": "Public regulatory/news event family; stock-web price row uses 2021-09-07 close", "stage2_evidence_fields": ["public_event_or_disclosure"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": ["legal_or_regulatory_block", "explicit_event_cap", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/035/035720/2021.csv", "profile_path": "atlas/symbol_profiles/035/035720.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-09-07", "entry_price": 154000, "MFE_30D_pct": 1.3, "MFE_90D_pct": 1.3, "MFE_180D_pct": 1.3, "MFE_1Y_pct": 1.3, "MFE_2Y_pct": 1.3, "MAE_30D_pct": -28.25, "MAE_90D_pct": -28.25, "MAE_180D_pct": -46.62, "MAE_1Y_pct": -62.34, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-09-08", "peak_price": 156000, "drawdown_after_peak_pct": -47.05, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.675, "four_b_full_window_peak_proximity": 0.675, "four_b_timing_verdict": "good_non_price_4B_risk_overlay_before_full_thesis_break", "four_b_evidence_type": ["legal_or_regulatory_block", "explicit_event_cap", "positioning_overheat"], "four_c_protection_label": "hard_4c_watch_before_full_thesis_break", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C26_KAKAO_2021_2021-09-07_154000", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": null, "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "TRG_C26_SOOP_2021_STAGE2_ACTIONABLE", "case_id": "C26_SOOP_2021_CREATOR_PLATFORM_OPERATING_LEVERAGE", "symbol": "067160", "company_name": "SOOP", "round": "R13", "loop": "37", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "OWNED_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "creator/live-streaming platform traffic and monetization leverage", "loop_objective": ["holdout_validation", "residual_missed_structural_mining", "yellow_threshold_stress_test", "green_strictness_stress_test", "stage2_actionable_bonus_stress_test", "4B_non_price_requirement_stress_test", "4C_thesis_break_timing_test", "sector_specific_rule_discovery", "canonical_archetype_compression", "counterexample_mining", "coverage_gap_fill"], "trigger_type": "Stage2-Actionable", "trigger_date": "2021-04-30", "evidence_available_at_that_date": "Q1 traffic/creator monetization operating leverage; owned platform plus paid-item/ad inventory control.", "evidence_source": "AfreecaTV/SOOP Q1 2021 earnings/IR", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility", "durable_customer_confirmation"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/067/067160/2021.csv", "profile_path": "atlas/symbol_profiles/067/067160.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-05-03", "entry_price": 89500, "MFE_30D_pct": 25.59, "MFE_90D_pct": 91.4, "MFE_180D_pct": 178.32, "MFE_1Y_pct": 178.32, "MFE_2Y_pct": 178.32, "MAE_30D_pct": -2.01, "MAE_90D_pct": -2.01, "MAE_180D_pct": -2.01, "MAE_1Y_pct": -31.84, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-11-09", "peak_price": 249100, "drawdown_after_peak_pct": -35.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C26_SOOP_2021_2021-05-03_89500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_C26_SOOP_2021_STAGE3_GREEN_COMPARISON", "case_id": "C26_SOOP_2021_CREATOR_PLATFORM_OPERATING_LEVERAGE", "symbol": "067160", "company_name": "SOOP", "round": "R13", "loop": "37", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "OWNED_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "creator/live-streaming platform traffic and monetization leverage", "loop_objective": ["holdout_validation", "residual_missed_structural_mining", "yellow_threshold_stress_test", "green_strictness_stress_test", "stage2_actionable_bonus_stress_test", "4B_non_price_requirement_stress_test", "4C_thesis_break_timing_test", "sector_specific_rule_discovery", "canonical_archetype_compression", "counterexample_mining", "coverage_gap_fill"], "trigger_type": "Stage3-Green", "trigger_date": "2021-07-27", "evidence_available_at_that_date": "Later confirmed operating leverage and strong market reaction; used as Green lateness comparison.", "evidence_source": "AfreecaTV/SOOP Q2 2021 earnings/IR and stock-web price row", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "multiple_public_sources", "financial_visibility", "durable_customer_confirmation", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/067/067160/2021.csv", "profile_path": "atlas/symbol_profiles/067/067160.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-07-27", "entry_price": 136600, "MFE_30D_pct": 19.99, "MFE_90D_pct": 82.36, "MFE_180D_pct": 82.36, "MFE_1Y_pct": 82.36, "MFE_2Y_pct": 82.36, "MAE_30D_pct": -6.3, "MAE_90D_pct": -6.3, "MAE_180D_pct": -26.06, "MAE_1Y_pct": -44.0, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-11-09", "peak_price": 249100, "drawdown_after_peak_pct": -35.0, "green_lateness_ratio": 0.295, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "green_not_too_late", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C26_SOOP_2021_2021-07-27_136600", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": false, "reuse_reason": null, "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "TRG_C26_NASMEDIA_2021_STAGE2_ACTIONABLE", "case_id": "C26_NASMEDIA_2021_AD_AGENCY_FALSE_POSITIVE", "symbol": "089600", "company_name": "KT나스미디어", "round": "R13", "loop": "37", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "OWNED_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "ad agency/media rep cyclic recovery without owned platform retention", "loop_objective": ["holdout_validation", "residual_missed_structural_mining", "yellow_threshold_stress_test", "green_strictness_stress_test", "stage2_actionable_bonus_stress_test", "4B_non_price_requirement_stress_test", "4C_thesis_break_timing_test", "sector_specific_rule_discovery", "canonical_archetype_compression", "counterexample_mining", "coverage_gap_fill"], "trigger_type": "Stage2-Actionable", "trigger_date": "2021-05-06", "evidence_available_at_that_date": "Advertising recovery evidence; however, owned-platform retention and self-serve ad inventory control were weak.", "evidence_source": "Nasmedia Q1 2021 earnings/IR and stock-web price row", "stage2_evidence_fields": ["public_event_or_disclosure", "early_revision_signal"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": ["margin_or_backlog_slowdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/089/089600/2021.csv", "profile_path": "atlas/symbol_profiles/089/089600.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-05-07", "entry_price": 36950, "MFE_30D_pct": 17.19, "MFE_90D_pct": 21.52, "MFE_180D_pct": 21.52, "MFE_1Y_pct": 21.52, "MFE_2Y_pct": 21.52, "MAE_30D_pct": -5.28, "MAE_90D_pct": -5.41, "MAE_180D_pct": -10.69, "MAE_1Y_pct": -33.0, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-06-24", "peak_price": 44900, "drawdown_after_peak_pct": -26.5, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": ["margin_or_backlog_slowdown"], "four_c_protection_label": "false_break_watch_only", "trigger_outcome_label": "failed_structural_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C26_NASMEDIA_2021_2021-05-07_36950", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_C26_NASMEDIA_2021_STAGE3_YELLOW_FALSE_POSITIVE", "case_id": "C26_NASMEDIA_2021_AD_AGENCY_FALSE_POSITIVE", "symbol": "089600", "company_name": "KT나스미디어", "round": "R13", "loop": "37", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "OWNED_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "ad agency/media rep cyclic recovery without owned platform retention", "loop_objective": ["holdout_validation", "residual_missed_structural_mining", "yellow_threshold_stress_test", "green_strictness_stress_test", "stage2_actionable_bonus_stress_test", "4B_non_price_requirement_stress_test", "4C_thesis_break_timing_test", "sector_specific_rule_discovery", "canonical_archetype_compression", "counterexample_mining", "coverage_gap_fill"], "trigger_type": "Stage3-Yellow", "trigger_date": "2021-06-18", "evidence_available_at_that_date": "Later advertising recovery was already priced; lacked recurring retention and owned inventory control.", "evidence_source": "Nasmedia 2021 recovery narrative and stock-web price row", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": ["valuation_blowoff", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/089/089600/2021.csv", "profile_path": "atlas/symbol_profiles/089/089600.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-06-18", "entry_price": 43300, "MFE_30D_pct": 3.7, "MFE_90D_pct": 3.7, "MFE_180D_pct": 3.7, "MFE_1Y_pct": 3.7, "MFE_2Y_pct": 3.7, "MAE_30D_pct": -11.2, "MAE_90D_pct": -23.79, "MAE_180D_pct": -23.79, "MAE_1Y_pct": -43.0, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-06-24", "peak_price": 44900, "drawdown_after_peak_pct": -26.5, "green_lateness_ratio": 0.799, "four_b_local_peak_proximity": 0.799, "four_b_full_window_peak_proximity": 0.799, "four_b_timing_verdict": "false_positive_late_yellow_near_local_top", "four_b_evidence_type": ["valuation_blowoff", "margin_or_backlog_slowdown"], "four_c_protection_label": "false_break", "trigger_outcome_label": "false_positive_yellow", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C26_NASMEDIA_2021_2021-06-18_43300", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": false, "reuse_reason": null, "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_c26_shadow", "case_id": "C26_NAVER_2020_AD_COMMERCE_OPERATING_LEVERAGE", "trigger_id": "TRG_C26_NAVER_2020_STAGE2_ACTIONABLE", "symbol": "035420", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 8, "revision_score": 12, "relative_strength_score": 15, "customer_quality_score": 13, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "owned_platform_inventory_score": "unknown_or_not_supported", "first_party_traffic_score": "unknown_or_not_supported", "advertiser_retention_score": "unknown_or_not_supported", "ad_agency_pass_through_risk_score": "unknown_or_not_supported", "dominant_platform_regulatory_risk_score": "unknown_or_not_supported"}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 8, "revision_score": 12, "relative_strength_score": 15, "customer_quality_score": 13, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "owned_platform_inventory_score": 12, "first_party_traffic_score": 10, "advertiser_retention_score": 8, "ad_agency_pass_through_risk_score": 0, "dominant_platform_regulatory_risk_score": 2}, "weighted_score_after": 78, "stage_label_after": "Stage3-Yellow", "changed_components": ["owned_platform_inventory_score", "first_party_traffic_score", "advertiser_retention_score", "ad_agency_pass_through_risk_score", "dominant_platform_regulatory_risk_score"], "component_delta_explanation": "C26 shadow profile separates owned-platform ad operating leverage from pass-through ad agency cyclic recovery; non-price regulation is treated as 4B/4C risk, not positive promotion.", "MFE_90D_pct": 15.28, "MAE_90D_pct": -9.14, "score_return_alignment_label": "risk_overlay", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_c26_shadow", "case_id": "C26_NAVER_2020_AD_COMMERCE_OPERATING_LEVERAGE", "trigger_id": "TRG_C26_NAVER_2021_STAGE3_YELLOW_COMPARISON", "symbol": "035420", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 0, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "owned_platform_inventory_score": "unknown_or_not_supported", "first_party_traffic_score": "unknown_or_not_supported", "advertiser_retention_score": "unknown_or_not_supported", "ad_agency_pass_through_risk_score": "unknown_or_not_supported", "dominant_platform_regulatory_risk_score": "unknown_or_not_supported"}, "weighted_score_before": 72, "stage_label_before": "label_comparison_only", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 0, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 72, "stage_label_after": "label_comparison_only", "changed_components": [], "component_delta_explanation": "C26 shadow profile separates owned-platform ad operating leverage from pass-through ad agency cyclic recovery; non-price regulation is treated as 4B/4C risk, not positive promotion.", "MFE_90D_pct": 19.53, "MAE_90D_pct": -2.48, "score_return_alignment_label": "risk_overlay", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_c26_shadow", "case_id": "C26_KAKAO_2021_TALK_BIZ_REGULATORY_4B", "trigger_id": "TRG_C26_KAKAO_2021_STAGE2_ACTIONABLE", "symbol": "035720", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 10, "revision_score": 13, "relative_strength_score": 16, "customer_quality_score": 12, "policy_or_regulatory_score": 4, "valuation_repricing_score": 9, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "owned_platform_inventory_score": "unknown_or_not_supported", "first_party_traffic_score": "unknown_or_not_supported", "advertiser_retention_score": "unknown_or_not_supported", "ad_agency_pass_through_risk_score": "unknown_or_not_supported", "dominant_platform_regulatory_risk_score": "unknown_or_not_supported"}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 10, "revision_score": 13, "relative_strength_score": 16, "customer_quality_score": 12, "policy_or_regulatory_score": 4, "valuation_repricing_score": 9, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "owned_platform_inventory_score": 11, "first_party_traffic_score": 12, "advertiser_retention_score": 8, "ad_agency_pass_through_risk_score": 0, "dominant_platform_regulatory_risk_score": 6}, "weighted_score_after": 80, "stage_label_after": "Stage3-Yellow", "changed_components": ["owned_platform_inventory_score", "first_party_traffic_score", "advertiser_retention_score", "ad_agency_pass_through_risk_score", "dominant_platform_regulatory_risk_score"], "component_delta_explanation": "C26 shadow profile separates owned-platform ad operating leverage from pass-through ad agency cyclic recovery; non-price regulation is treated as 4B/4C risk, not positive promotion.", "MFE_90D_pct": 51.09, "MAE_90D_pct": -5.68, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_c26_shadow", "case_id": "C26_KAKAO_2021_TALK_BIZ_REGULATORY_4B", "trigger_id": "TRG_C26_KAKAO_2021_4B_REGULATORY_OVERLAY", "symbol": "035720", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 0, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "owned_platform_inventory_score": "unknown_or_not_supported", "first_party_traffic_score": "unknown_or_not_supported", "advertiser_retention_score": "unknown_or_not_supported", "ad_agency_pass_through_risk_score": "unknown_or_not_supported", "dominant_platform_regulatory_risk_score": "unknown_or_not_supported"}, "weighted_score_before": 72, "stage_label_before": "label_comparison_only", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 0, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 72, "stage_label_after": "label_comparison_only", "changed_components": [], "component_delta_explanation": "C26 shadow profile separates owned-platform ad operating leverage from pass-through ad agency cyclic recovery; non-price regulation is treated as 4B/4C risk, not positive promotion.", "MFE_90D_pct": 1.3, "MAE_90D_pct": -28.25, "score_return_alignment_label": "risk_overlay", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_c26_shadow", "case_id": "C26_SOOP_2021_CREATOR_PLATFORM_OPERATING_LEVERAGE", "trigger_id": "TRG_C26_SOOP_2021_STAGE2_ACTIONABLE", "symbol": "067160", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 15, "revision_score": 14, "relative_strength_score": 18, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "owned_platform_inventory_score": "unknown_or_not_supported", "first_party_traffic_score": "unknown_or_not_supported", "advertiser_retention_score": "unknown_or_not_supported", "ad_agency_pass_through_risk_score": "unknown_or_not_supported", "dominant_platform_regulatory_risk_score": "unknown_or_not_supported"}, "weighted_score_before": 79, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 15, "revision_score": 14, "relative_strength_score": 18, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "owned_platform_inventory_score": 10, "first_party_traffic_score": 14, "advertiser_retention_score": 9, "ad_agency_pass_through_risk_score": 0, "dominant_platform_regulatory_risk_score": 1}, "weighted_score_after": 84, "stage_label_after": "Stage3-Yellow", "changed_components": ["owned_platform_inventory_score", "first_party_traffic_score", "advertiser_retention_score", "ad_agency_pass_through_risk_score", "dominant_platform_regulatory_risk_score"], "component_delta_explanation": "C26 shadow profile separates owned-platform ad operating leverage from pass-through ad agency cyclic recovery; non-price regulation is treated as 4B/4C risk, not positive promotion.", "MFE_90D_pct": 91.4, "MAE_90D_pct": -2.01, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_c26_shadow", "case_id": "C26_SOOP_2021_CREATOR_PLATFORM_OPERATING_LEVERAGE", "trigger_id": "TRG_C26_SOOP_2021_STAGE3_GREEN_COMPARISON", "symbol": "067160", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 0, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "owned_platform_inventory_score": "unknown_or_not_supported", "first_party_traffic_score": "unknown_or_not_supported", "advertiser_retention_score": "unknown_or_not_supported", "ad_agency_pass_through_risk_score": "unknown_or_not_supported", "dominant_platform_regulatory_risk_score": "unknown_or_not_supported"}, "weighted_score_before": 72, "stage_label_before": "label_comparison_only", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 0, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 72, "stage_label_after": "label_comparison_only", "changed_components": [], "component_delta_explanation": "C26 shadow profile separates owned-platform ad operating leverage from pass-through ad agency cyclic recovery; non-price regulation is treated as 4B/4C risk, not positive promotion.", "MFE_90D_pct": 82.36, "MAE_90D_pct": -6.3, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_c26_shadow", "case_id": "C26_NASMEDIA_2021_AD_AGENCY_FALSE_POSITIVE", "trigger_id": "TRG_C26_NASMEDIA_2021_STAGE2_ACTIONABLE", "symbol": "089600", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 10, "customer_quality_score": 5, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "owned_platform_inventory_score": "unknown_or_not_supported", "first_party_traffic_score": "unknown_or_not_supported", "advertiser_retention_score": "unknown_or_not_supported", "ad_agency_pass_through_risk_score": "unknown_or_not_supported", "dominant_platform_regulatory_risk_score": "unknown_or_not_supported"}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 10, "customer_quality_score": 5, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "owned_platform_inventory_score": 2, "first_party_traffic_score": 2, "advertiser_retention_score": 2, "ad_agency_pass_through_risk_score": 12, "dominant_platform_regulatory_risk_score": 0}, "weighted_score_after": 70, "stage_label_after": "Stage2", "changed_components": ["owned_platform_inventory_score", "first_party_traffic_score", "advertiser_retention_score", "ad_agency_pass_through_risk_score", "dominant_platform_regulatory_risk_score"], "component_delta_explanation": "C26 shadow profile separates owned-platform ad operating leverage from pass-through ad agency cyclic recovery; non-price regulation is treated as 4B/4C risk, not positive promotion.", "MFE_90D_pct": 21.52, "MAE_90D_pct": -5.41, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_c26_shadow", "case_id": "C26_NASMEDIA_2021_AD_AGENCY_FALSE_POSITIVE", "trigger_id": "TRG_C26_NASMEDIA_2021_STAGE3_YELLOW_FALSE_POSITIVE", "symbol": "089600", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 0, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "owned_platform_inventory_score": "unknown_or_not_supported", "first_party_traffic_score": "unknown_or_not_supported", "advertiser_retention_score": "unknown_or_not_supported", "ad_agency_pass_through_risk_score": "unknown_or_not_supported", "dominant_platform_regulatory_risk_score": "unknown_or_not_supported"}, "weighted_score_before": 72, "stage_label_before": "label_comparison_only", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 0, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 72, "stage_label_after": "label_comparison_only", "changed_components": [], "component_delta_explanation": "C26 shadow profile separates owned-platform ad operating leverage from pass-through ad agency cyclic recovery; non-price regulation is treated as 4B/4C risk, not positive promotion.", "MFE_90D_pct": 3.7, "MAE_90D_pct": -23.79, "score_return_alignment_label": "false_positive_guard_needed", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R13", "loop": "37", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "stage3_green_revision_min", "stage3_cross_evidence_green_buffer", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["current_profile_too_late", "current_profile_false_positive", "current_profile_4B_too_late"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

### 25.2 shadow_weight CSV

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c26_owned_platform_inventory_bonus,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,1,+1,"Owned inventory/first-party traffic separated NAVER/Kakao/SOOP positives from ad-agency bounce.","Improved score-return alignment for 3 positives while not promoting Nasmedia",TRG_C26_NAVER_2020_STAGE2_ACTIONABLE|TRG_C26_KAKAO_2021_STAGE2_ACTIONABLE|TRG_C26_SOOP_2021_STAGE2_ACTIONABLE|TRG_C26_NASMEDIA_2021_STAGE2_ACTIONABLE,4,4,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c26_ad_agency_pass_through_guard,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,1,+1,"Agency/media-rep recovery without owned-platform retention had weak forward alignment.","Reduced false positive Yellow/Green risk in Nasmedia",TRG_C26_NASMEDIA_2021_STAGE2_ACTIONABLE|TRG_C26_NASMEDIA_2021_STAGE3_YELLOW_FALSE_POSITIVE,2,1,1,medium,counterexample_guard_shadow_only,"not production; post-calibrated residual"
shadow_weight,c26_dominant_platform_regulatory_4b_overlay,sector_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,1,+1,"Non-price regulatory overhang protected better than price-only local peak logic in dominant platforms.","Converted late positive continuation into 4B overlay for Kakao",TRG_C26_KAKAO_2021_4B_REGULATORY_OVERLAY,1,1,0,low,sector_shadow_only,"risk overlay only; not positive promotion"
```


## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row.
Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules

- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate large_sector_id and canonical_archetype_id.
4. Validate novelty and reuse fields.
5. Deduplicate same_entry_group_id and reused cases.
6. Aggregate by large_sector_id and canonical_archetype_id.
7. Update sector_shadow_profile and archetype_shadow_profile only.
8. Preserve global calibrated profile unless explicitly promoted.
9. Report new independent cases, counterexamples, and residual error types.
10. Add tests that duplicate low-value loops cannot change weights.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.


## 27. Next Round State

```text
next_round: R13_loop_38
suggested_large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
suggested_canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
reason: Continue L8 coverage but switch from ad operating leverage to content/IP monetization where subscription, licensing, platform take-rate, and overseas distribution differ from C26.
```


## 28. Source Notes

Stock-Web files inspected for this MD:

- `atlas/manifest.json`
- `atlas/schema.json`
- `atlas/symbol_profiles/035/035420.json`
- `atlas/symbol_profiles/035/035720.json`
- `atlas/symbol_profiles/067/067160.json`
- `atlas/symbol_profiles/089/089600.json`
- `atlas/ohlcv_tradable_by_symbol_year/035/035420/2020.csv`
- `atlas/ohlcv_tradable_by_symbol_year/035/035420/2021.csv`
- `atlas/ohlcv_tradable_by_symbol_year/035/035720/2021.csv`
- `atlas/ohlcv_tradable_by_symbol_year/035/035720/2022.csv`
- `atlas/ohlcv_tradable_by_symbol_year/067/067160/2021.csv`
- `atlas/ohlcv_tradable_by_symbol_year/089/089600/2021.csv`

Stock-agent research artifacts inspected only for duplicate avoidance / applied-axis context:

- `reports/e2r_calibration/ingest_summary.md`
- `reports/e2r_calibration/applied_scoring_diff.md`

The price rows are raw/unadjusted marcap data. This MD does not infer adjusted returns.
