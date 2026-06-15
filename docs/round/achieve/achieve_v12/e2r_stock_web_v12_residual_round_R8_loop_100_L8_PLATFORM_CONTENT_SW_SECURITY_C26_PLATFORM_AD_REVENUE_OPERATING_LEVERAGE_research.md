# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file: e2r_stock_web_v12_residual_round_R8_loop_100_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md
selected_round: R8
selected_loop: 100
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: mixed_C26_fine_archetype_set
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - canonical_archetype_compression
  - 4B_non_price_requirement_stress_test
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 / under 30 rows
auto_selected_coverage_gap: C26 had 3 representative rows in the no-repeat index; this loop adds five independent usable C26 rows.
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
investment_recommendation_language: false
```

This file is a standalone historical calibration research artifact. It is not a live scan, not a trading recommendation, and not a production scoring patch.

## 1. Current Calibrated Profile Assumption

```yaml
current_default_profile_proxy: e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id: e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus: kept_for_stress_test_only
stage3_yellow_total_min: 75.0
stage3_green_total_min: 87.0
stage3_green_revision_min: 55.0
price_only_blowoff_blocks_positive_stage: true
full_4b_requires_non_price_evidence: true
hard_4c_thesis_break_routes_to_4c: true
```

The residual question here is narrow: **C26 should not treat every digital-ad recovery as the same rerating mechanism.** Owned ad platforms with actual margin bridge behaved very differently from media-rep cyclicality, group-level platform conglomerates, and NFT/metaverse event premiums.

## 2. Round / Large Sector / Canonical Archetype Scope

```yaml
round_sector_consistency: pass
round: R8
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
canonical_scope_definition: platform advertising revenue or platform monetization that converts into operating leverage
invalid_round_sector_pair: false
```

C26 maps to R8 / L8. R13 is not used because this is an individual platform/SW/content sector archetype expansion, not a cross-archetype red-team checkpoint.

## 3. Previous Coverage / Duplicate Avoidance Check

```yaml
no_repeat_index_role: duplicate_ledger_only
priority_bucket_seen: Priority 0
C26_index_rows_before_this_loop: 3
C26_need_to_30_before_this_loop: 27
hard_duplicate_key: canonical_archetype_id + symbol + trigger_type + entry_date
known_existing_C26_case_to_avoid: Cafe24 / 042000 / 2024-05-09 family
previous_same_session_output_avoided: C18_CONSUMER_EXPORT_CHANNEL_REORDER / loop 113
new_symbol_count: 5
reused_case_count: 0
new_trigger_family_count: 5
```

All five rows below are new C26 symbols relative to the visible C26 ledger family. They intentionally avoid reusing the prior C26 Cafe24 trigger family and also avoid the prior same-session C18 consumer-export research.

## 4. Stock-Web OHLC Input / Price Source Validation

```yaml
source: Songdaiki/stock-web
upstream_source: FinanceData/marcap
source_repo_url: https://github.com/Songdaiki/stock-web
manifest_path: atlas/manifest.json
schema_path: atlas/schema.json
universe_path: atlas/universe/all_symbols.csv
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14354401
raw_row_count: 15214118
symbol_count: 5414
active_like_symbol_count: 2868
inactive_or_delisted_like_symbol_count: 2546
markets: KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
price_adjustment_status: raw_unadjusted_marcap
```

The schema calculation used here is:

```text
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
```

## 5. Historical Eligibility Gate

| symbol | entry_date | 180D_end | entry_exists | forward_180D | MFE/MAE_6_fields | corp_action_status | overlap_dates | share_var_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 035420 | 2020-07-30 | 2021-04-22 | yes | yes | yes | clean | - | 0.0 |
| 067160 | 2021-07-26 | 2022-04-19 | yes | yes | yes | clean | - | 0.0 |
| 035720 | 2021-08-06 | 2022-05-02 | yes | yes | yes | clean | - | 0.4073 |
| 089600 | 2021-08-13 | 2022-05-10 | yes | yes | yes | clean | - | 9.7351 |
| 214270 | 2021-11-30 | 2022-08-22 | yes | yes | yes | clean | - | 5.4884 |


All five trigger rows have entry date, entry price, forward 180 tradable rows, and complete 30D/90D/180D MFE and MAE fields. No profile-level corporate-action candidate date overlaps the entry-to-180D window. Minor share-count variation below the profile's blocking candidate threshold is retained as a caveat for Kakao, Nasmedia, and FSN but does not block the 180D calibration row.

## 6. Canonical Archetype Compression Map

```yaml
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
compression_goal: collapse multiple platform/ad-looking stories into C26 but preserve fine-level gates
fine_archetypes:
  - SEARCH_COMMERCE_AD_RECOVERY_OPERATING_LEVERAGE
  - LIVE_STREAMING_AD_PLATFORM_OPERATING_LEVERAGE
  - TALK_BIZ_AD_COMMERCE_GROUP_COST_DRAG
  - MEDIA_REP_AD_RECOVERY_NOT_OWNED_PLATFORM
  - DIGITAL_MARKETING_NFT_THEME_EVENT_CAP
```

Compression rule: **C26 positive promotion should require owned-platform monetization plus a margin/OP bridge.** A media-rep recovery, a platform conglomerate with visible cost/regulatory drag, or an NFT/theme premium is still C26 scope, but it should not receive the same positive-stage multiplier.

## 7. Case Selection Summary

| symbol | company | case_type | trigger_type | fine_archetype | entry_date | entry_price | MFE90 | MAE90 | MFE180 | MAE180 | current_profile_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 035420 | NAVER | structural_success | Stage3-Yellow | SEARCH_COMMERCE_AD_RECOVERY_OPERATING_LEVERAGE | 2020-07-30 | 294,000 | 18.03 | -6.97 | 39.46 | -6.97 | current_profile_correct |
| 067160 | SOOP/AfreecaTV | structural_success | Stage3-Yellow | LIVE_STREAMING_AD_PLATFORM_OPERATING_LEVERAGE | 2021-07-26 | 127,800 | 94.91 | -7.43 | 94.91 | -7.43 | current_profile_too_late |
| 035720 | Kakao | failed_rerating | Stage2-Actionable | TALK_BIZ_AD_COMMERCE_GROUP_COST_DRAG | 2021-08-06 | 145,500 | 8.25 | -24.05 | 8.25 | -43.51 | current_profile_false_positive |
| 089600 | Nasmedia | failed_rerating | Stage2-Actionable | MEDIA_REP_AD_RECOVERY_NOT_OWNED_PLATFORM | 2021-08-13 | 39,100 | 2.3 | -22.63 | 2.3 | -34.02 | current_profile_false_positive |
| 214270 | FSN | 4B_overlay_success | Stage4B | DIGITAL_MARKETING_NFT_THEME_EVENT_CAP | 2021-11-30 | 10,250 | 38.54 | -31.71 | 38.54 | -60.98 | current_profile_correct |


## 8. Positive vs Counterexample Balance

```yaml
positive_structural_success: 2
counterexample_or_failed_rerating: 2
4B_or_4C_case: 1
4C_case: 0
minimum_positive_case_count_met: true
minimum_counterexample_count_met: true
minimum_calibration_usable_case_count_met: true
```

The two positives are both owned-platform monetization cases with actual operating-profit bridge. The two counterexamples are ad/platform growth stories where the listed equity did not reward the signal. The one 4B case is an event-premium/NFT theme cap with large later MAE.

## 9. Evidence Source Map

| case | trigger_date | source_url | evidence_use |
| --- | --- | --- | --- |
| NAVER | 2020-07-30 | https://koreajoongangdaily.joins.com/2020/07/30/business/industry/Naver-Q2-earnings/20200730181700420.html | Q2 2020 record sales/OP; search-ad and commerce revenue growth. |
| SOOP/AfreecaTV | 2021-07-26 | https://www.koreaherald.com/article/2660482 | Q2 2021 revenue +44%, operating profit +97%; platform/ad leverage. |
| Kakao | 2021-08-06 | https://www.asiae.co.kr/en/article/2021080609394402183 | Q2 2021 platform and Talk Biz growth; useful counterexample due later path. |
| Nasmedia | 2021-08-12 | https://www.nasmedia.co.kr/%EB%B3%B4%EB%8F%84%EC%9E%90%EB%A3%8C/%EB%82%98%EC%8A%A4%EB%AF%B8%EB%94%94%EC%96%B4-2%EB%B6%84%EA%B8%B0-%EB%A7%A4%EC%B6%9C-%EB%B0%8F-%EC%98%81%EC%97%85%EC%9D%B5-%EC%9E%91%EB%85%84%EB%B9%84-%EB%91%90-%EC%9E%90%EB%A6%AC-%EC%88%98-%EC%84%B1/ | Company press release: Q2 revenue/OP double-digit growth, online DA/SA/mobile platform ads. |
| FSN | 2021-11-30 | https://www.etnews.com/20211130000111 | NFT-theme stock move for a mobile-ad/digital-marketing company; event-cap 4B evidence. |


## 10. Price Data Source Map

| symbol | profile_path | price_shards_used | price_basis | adjustment |
| --- | --- | --- | --- | --- |
| 035420 | atlas/symbol_profiles/035/035420.json | atlas/ohlcv_tradable_by_symbol_year/035/035420/2020.csv + atlas/ohlcv_tradable_by_symbol_year/035/035420/2021.csv | tradable_raw | raw_unadjusted_marcap |
| 067160 | atlas/symbol_profiles/067/067160.json | atlas/ohlcv_tradable_by_symbol_year/067/067160/2021.csv + atlas/ohlcv_tradable_by_symbol_year/067/067160/2022.csv | tradable_raw | raw_unadjusted_marcap |
| 035720 | atlas/symbol_profiles/035/035720.json | atlas/ohlcv_tradable_by_symbol_year/035/035720/2021.csv + atlas/ohlcv_tradable_by_symbol_year/035/035720/2022.csv | tradable_raw | raw_unadjusted_marcap |
| 089600 | atlas/symbol_profiles/089/089600.json | atlas/ohlcv_tradable_by_symbol_year/089/089600/2021.csv + atlas/ohlcv_tradable_by_symbol_year/089/089600/2022.csv | tradable_raw | raw_unadjusted_marcap |
| 214270 | atlas/symbol_profiles/214/214270.json | atlas/ohlcv_tradable_by_symbol_year/214/214270/2021.csv + atlas/ohlcv_tradable_by_symbol_year/214/214270/2022.csv | tradable_raw | raw_unadjusted_marcap |


## 11. Case-by-Case Trigger Grid

### 11.1 NAVER / 035420 / structural success

- Trigger: 2020-07-30 Q2 earnings.
- Evidence mechanism: search-based advertising and commerce revenue growth flowed into record sales and operating profit.
- E2R interpretation: Stage3-Yellow is justified; Stage3-Green should still wait for durable revision confirmation.
- Price path: MFE180 +39.46%, MAE180 -6.97%.
- Residual lesson: owned search/commerce ad platform deserves more C26 weight than generic ad-cycle recovery.

### 11.2 SOOP/AfreecaTV / 067160 / structural success with later 4B overlay

- Trigger: 2021-07-26 Q2 earnings.
- Evidence mechanism: live-streaming platform monetization and digital ad-platform strengthening created operating leverage.
- E2R interpretation: current profile likely under-recognizes the owned-platform ad operating leverage; however, a 4B overlay is needed after the rapid run.
- Price path: MFE90 +94.91%, MAE90 -7.43%, but drawdown after 180D peak -47.01%.
- Residual lesson: C26 needs a two-stage rule: faster recognition for real owned-platform monetization, then 4B watch when price extension becomes crowded.

### 11.3 Kakao / 035720 / failed rerating

- Trigger: 2021-08-06 Q2 earnings.
- Evidence mechanism: Talk Biz and platform segment growth looked like platform ad/commercial monetization.
- E2R interpretation: C26 scoring is too early if it ignores group-level cost, regulatory pressure, and non-ad segment drag.
- Price path: MFE180 +8.25%, MAE180 -43.51%.
- Residual lesson: platform conglomerates need an aggregate expense/regulatory risk gate before Yellow/Green.

### 11.4 Nasmedia / 089600 / failed rerating

- Trigger: 2021-08-12 earnings release; next tradable close used as entry date 2021-08-13.
- Evidence mechanism: online DA/search/mobile-platform ad recovery and strong operating profit.
- E2R interpretation: a media rep's ad-cycle recovery is not the same as owned-platform monetization.
- Price path: MFE180 +2.30%, MAE180 -34.02%.
- Residual lesson: C26 should cap generic ad-market recovery at Stage2 unless two-quarter durability or owned-platform take-rate evidence appears.

### 11.5 FSN / 214270 / Stage4B event cap

- Trigger: 2021-11-30 NFT-theme stock move.
- Evidence mechanism: mobile-ad/digital-marketing company caught in the NFT/metaverse event premium.
- E2R interpretation: route to Stage4B/event cap, not positive C26 promotion.
- Price path: MFE180 +38.54%, MAE180 -60.98%, drawdown after peak -71.83%.
- Residual lesson: C26 must separate operating leverage from event-premium platform optionality.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | 30D_end | MFE30 | MAE30 | 90D_end | MFE90 | MAE90 | 180D_end | MFE180 | MAE180 | peak_date | peak_price | DD_after_peak |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 035420 | 2020-07-30 | 294,000 | 2020-09-10 | 18.03 | -1.02 | 2020-12-09 | 18.03 | -6.97 | 2021-04-22 | 39.46 | -6.97 | 2021-03-18 | 410,000 | -9.27 |
| 067160 | 2021-07-26 | 127,800 | 2021-09-06 | 32.24 | -7.43 | 2021-12-06 | 94.91 | -7.43 | 2022-04-19 | 94.91 | -7.43 | 2021-11-09 | 249,100 | -47.01 |
| 035720 | 2021-08-06 | 145,500 | 2021-09-17 | 8.25 | -18.9 | 2021-12-17 | 8.25 | -24.05 | 2022-05-02 | 8.25 | -43.51 | 2021-09-03 | 157,500 | -47.81 |
| 089600 | 2021-08-13 | 39,100 | 2021-09-29 | 2.3 | -15.6 | 2021-12-24 | 2.3 | -22.63 | 2022-05-10 | 2.3 | -34.02 | 2021-08-13 | 40,000 | -35.5 |
| 214270 | 2021-11-30 | 10,250 | 2022-01-11 | 38.54 | -2.44 | 2022-04-12 | 38.54 | -31.71 | 2022-08-22 | 38.54 | -60.98 | 2022-01-03 | 14,200 | -71.83 |


## 13. Current Calibrated Profile Stress Test

| symbol | weighted_before | stage_before | weighted_after_shadow | stage_after_shadow | component_delta_explanation |
| --- | --- | --- | --- | --- | --- |
| 035420 | 78.0 | Stage3-Yellow | 81.0 | Stage3-Yellow | Owned-platform search/commerce evidence gets modest C26 reinforcement; no global threshold change. |
| 067160 | 72.0 | Stage2-Actionable | 88.0 | Stage3-Green | Owned live-streaming ad-platform operating leverage is stronger than generic digital-ad recovery; allow C26-specific fast Green only with margin bridge. |
| 035720 | 76.0 | Stage3-Yellow | 66.0 | Stage2-Actionable | Demote platform conglomerate ad growth when group cost/regulatory risk and non-ad segment drag overwhelm ad evidence. |
| 089600 | 73.0 | Stage2-Actionable | 61.0 | Stage1-Watch | Media-rep ad market recovery should not receive the same C26 multiplier as owned-platform monetization. |
| 214270 | 68.0 | Stage2-Actionable | 58.0 | Stage4B | NFT/theme premium is explicitly capped as Stage4B; no positive C26 promotion from event-premium alone. |


Stress-test conclusions:

```yaml
current_profile_correct:
  - NAVER: Stage3-Yellow signal aligns with clean positive path.
  - FSN: if non-price NFT/theme evidence is recognized, Stage4B routing is correct.
current_profile_too_late:
  - SOOP/AfreecaTV: owned-platform ad operating leverage was stronger than a generic platform label.
current_profile_false_positive:
  - Kakao: ad/platform growth was not enough once group cost/regulatory drag was considered.
  - Nasmedia: media-rep ad recovery should not inherit owned-platform C26 upside weight.
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence for NFT/metaverse event premium inside C26
existing_axis_weakened: null
```

## 14. Stage2 / Yellow / Green Comparison

```yaml
Stage2_Actionable:
  good_use: public earnings/event plus early ad-revenue recovery
  risk: too generous for media-rep or conglomerate ad growth without margin durability
Stage3_Yellow:
  good_use: actual owned-platform ad/commercial monetization plus OP or margin bridge
  risk: too early if valuation/regulation/cost drag overwhelms the ad segment
Stage3_Green:
  good_use: owned platform + repeat monetization + confirmed margin bridge + low red-team risk
  risk: should not be reached by event premium, one-quarter ad recovery, or theme/NFT optionality
Stage4B:
  good_use: NFT/metaverse/platform-optionality event cap; post-extension owned-platform 4B overlay
Stage4C:
  no hard 4C thesis-break case found in this loop
```

## 15. 4B Local vs Full-window Timing Audit

```yaml
4B_cases:
  - FSN / 214270 / 2021-11-30
4B_evidence_type:
  - valuation_blowoff
  - positioning_overheat
  - explicit_event_cap
FSN_post_trigger_peak:
  entry_price: 10250
  peak_180D_price: 14200
  MFE_180D_pct: 38.54
  drawdown_after_peak_180D_pct: -71.83
  MAE_180D_pct: -60.98
  timing_verdict: good_full_window_4B_timing_with_non_price_theme_evidence
SOOP_overlay_watch:
  MFE_90D_pct: 94.91
  drawdown_after_peak_180D_pct: -47.01
  timing_verdict: positive_stage_first_but_requires_4B_overlay_after_fast_extension
```

FSN is not a price-only 4B. The non-price event evidence was the NFT/theme frame around a mobile-ad/digital-marketing company. SOOP is the opposite shape: the operating leverage was real, but the later price extension needed a 4B overlay.

## 16. 4C Protection Audit

```yaml
hard_4c_case_found: false
four_c_label: thesis_break_watch_only
reason: no cancellation, regulatory rejection, accounting/trust break, forced liquidation, or explicit thesis evidence break was established at trigger date
```

The high-MAE cases here are better handled by 4B/event-cap and false-positive gates rather than hard 4C.

## 17. Sector-Specific Rule Candidate

```yaml
rule_scope: sector_specific
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
sector_rule_candidate: L8_C26_PLATFORM_AD_OPERATING_LEVERAGE_SPLIT
candidate_rule:
  - owned-platform ad/commercial products with actual OP/margin bridge can receive higher C26 positive weight
  - media-rep or agency ad recovery receives Stage2 ceiling unless durability is confirmed
  - platform conglomerates require group-level cost/regulatory drag check before Yellow/Green
  - NFT/metaverse/platform-optionality event premium routes to 4B, not positive Stage2/3
supporting_cases:
  positive:
    - NAVER
    - SOOP/AfreecaTV
  counterexample:
    - Kakao
    - Nasmedia
  4B:
    - FSN
confidence: medium
production_action: none_now_shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```yaml
rule_scope: canonical_archetype_specific
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
canonical_rule_candidate: C26_OWNED_PLATFORM_AD_MARGIN_BRIDGE_GATE
positive_gate:
  require_at_least_two:
    - actual platform ad/commercial revenue acceleration
    - confirmed operating-profit or margin bridge
    - owned traffic/customer base or high-retention monetization surface
counterexample_gate:
  demote_if_any:
    - media-rep/agency recovery without owned-platform take-rate
    - group-level cost/regulatory drag bigger than ad-segment growth
    - theme/NFT/metaverse premium without confirmed revenue conversion
4B_overlay:
  route_to_4B_if:
    - event premium is non-price visible
    - ad/platform claim is optionality rather than revenue conversion
    - post-trigger extension becomes crowded after real operating leverage
```

## 19. Before / After Backtest Comparison

| profile_id | scope | hypothesis | eligible_triggers | positive_stage_entries | avg_MFE90 | avg_MAE90 | avg_MFE180 | avg_MAE180 | false_positive_rate | missed_structural | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0 e2r_2_1_proxy | current | Generic calibrated C26 proxy | 5 | 5 | 32.41 | -18.56 | 36.69 | -30.58 | 0.40 | 1 | mixed: positive average hides high-MAE false positives |
| P0b e2r_2_0_ref | rollback | Less strict pre-stock-web reference | 5 | 5 | similar | worse | similar | worse | >=0.40 | 1 | do not roll back |
| P1 sector_shadow | L8 | Weight owned-platform ad/margin bridge; penalize media-rep recovery | 5 | 2 | 56.47 | -7.2 | 67.18 | -7.2 | 0.00 | 0 | better alignment |
| P2 canonical_shadow | C26 | C26 gate: owned platform + margin bridge + cost/regulatory check | 5 | 2 | 56.47 | -7.2 | 67.18 | -7.2 | 0.00 | 0 | preferred |
| P3 guard_profile | C26 | Theme/event premium becomes 4B overlay, not positive stage | 5 | 2 | 56.47 | -7.2 | 67.18 | -7.2 | 0.00 | 0 | keeps high-MAE FSN out of positives |


## 20. Score-Return Alignment Matrix

```yaml
NAVER:
  score_return_alignment: aligned_positive
  evidence_quality: owned platform + actual earnings + clean 180D path
SOOP_AfreecaTV:
  score_return_alignment: missed_structural_then_4B_overlay
  evidence_quality: owned platform + strong OP bridge + later peak drawdown
Kakao:
  score_return_alignment: false_positive_if_segment_growth_overweighted
  evidence_quality: strong Talk Biz but group-level risk dominated price path
Nasmedia:
  score_return_alignment: false_positive_if_media_rep_recovery_overweighted
  evidence_quality: actual earnings, but no owned-platform rerating path
FSN:
  score_return_alignment: 4B_guardrail_validated
  evidence_quality: event/theme evidence rather than operating leverage
```

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_count | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L8_PLATFORM_CONTENT_SW_SECURITY | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 5 | 2 | 2 | 1 | 0 | 5 | 0 | 5 | 5 | 3 | C26 expected rows 3 -> 8; need_to_30 22 |


## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 1
new_fine_archetype_count: 5
new_trigger_family_count: 5
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - owned_platform_ad_operating_leverage_too_late
  - media_rep_ad_recovery_false_positive
  - platform_conglomerate_cost_regulatory_drag_false_positive
  - nft_theme_event_cap_high_MAE
new_axis_proposed:
  - C26_OWNED_PLATFORM_AD_MARGIN_BRIDGE_GATE
  - C26_MEDIA_REP_AD_RECOVERY_CEILING
  - C26_THEME_EVENT_PREMIUM_4B_CAP
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
sector_specific_rule_candidate: L8_C26_PLATFORM_AD_OPERATING_LEVERAGE_SPLIT
canonical_archetype_rule_candidate: C26_OWNED_PLATFORM_AD_MARGIN_BRIDGE_GATE
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

- Korean listed equities only.
- Historical triggers before the stock-web manifest max date.
- Entry and forward windows drawn only from stock-web tradable shards.
- 30D/90D/180D MFE and MAE are computed using raw/unadjusted OHLC.
- All five rows are calibration usable under the 180D clean-window rule.

Non-validation scope:

- No live candidate scan.
- No current stock recommendation.
- No production score patch.
- No brokerage API or trading workflow.
- No claim that C26 should receive a global rule change.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,owned_platform_ad_margin_bridge_gate,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,1,+1,"Promote only owned-platform ad products with actual margin/OP bridge and repeat monetization evidence.","NAVER/SOOP positives separate cleanly from Kakao/Nasmedia false positives.","TRG_C26_R8_L100_035420_20200730_NAVER_SEARCH_COMMERCE|TRG_C26_R8_L100_067160_20210726_AFREECATV_AD_PLATFORM",5,5,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,media_rep_ad_recovery_ceiling,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,1,+1,"Generic digital ad market recovery at a media rep/agency receives Stage2 ceiling unless owned-platform monetization or 2Q margin durability exists.","Nasmedia Q2 beat had MFE180 2.30 and MAE180 -34.02.","TRG_C26_R8_L100_089600_20210813_NASMEDIA_MEDIAREP_RECOVERY",5,5,2,medium,canonical_shadow_only,"limits false positive green"
shadow_weight,theme_event_premium_4B_cap,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,1,+1,"NFT/metaverse/platform-optionality without confirmed ad-revenue conversion routes to Stage4B/event cap.","FSN MFE180 38.54 but MAE180 -60.98 and DD after peak -71.83.","TRG_C26_R8_L100_214270_20211130_FSN_NFT_THEME_CAP",5,5,2,medium,guardrail_shadow_only,"4B overlay/risk calibration only"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C26_R8_L100_035420_20200730_NAVER_SEARCH_COMMERCE","symbol":"035420","company_name":"NAVER","round":"R8","loop":"100","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"SEARCH_COMMERCE_AD_RECOVERY_OPERATING_LEVERAGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TRG_C26_R8_L100_035420_20200730_NAVER_SEARCH_COMMERCE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Owned search/commerce platform, actual earnings, clean forward path; no Green-only promotion required."}
{"row_type":"case","case_id":"C26_R8_L100_067160_20210726_AFREECATV_AD_PLATFORM","symbol":"067160","company_name":"SOOP/AfreecaTV","round":"R8","loop":"100","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"LIVE_STREAMING_AD_PLATFORM_OPERATING_LEVERAGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TRG_C26_R8_L100_067160_20210726_AFREECATV_AD_PLATFORM","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"missed_structural_with_4B_overlay_after_peak","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"True owned-platform operating leverage; later full-window drawdown means Green should carry a 4B overlay once extension becomes crowded."}
{"row_type":"case","case_id":"C26_R8_L100_035720_20210806_KAKAO_TALKBIZ_COST_DRAG","symbol":"035720","company_name":"Kakao","round":"R8","loop":"100","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"TALK_BIZ_AD_COMMERCE_GROUP_COST_DRAG","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TRG_C26_R8_L100_035720_20210806_KAKAO_TALKBIZ_COST_DRAG","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"good_business_signal_bad_stock_path","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Post-split entry avoids 2021-04-15 corporate-action candidate. C26 needs aggregate cost/regulatory drag gate for platform conglomerates."}
{"row_type":"case","case_id":"C26_R8_L100_089600_20210813_NASMEDIA_MEDIAREP_RECOVERY","symbol":"089600","company_name":"Nasmedia","round":"R8","loop":"100","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"MEDIA_REP_AD_RECOVERY_NOT_OWNED_PLATFORM","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TRG_C26_R8_L100_089600_20210813_NASMEDIA_MEDIAREP_RECOVERY","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"ad_market_recovery_not_platform_rerating","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Digital ad recovery without owned-platform monetization did not convert into a favorable 180D stock path."}
{"row_type":"case","case_id":"C26_R8_L100_214270_20211130_FSN_NFT_THEME_CAP","symbol":"214270","company_name":"FSN","round":"R8","loop":"100","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"DIGITAL_MARKETING_NFT_THEME_EVENT_CAP","case_type":"4B_overlay_success","positive_or_counterexample":"4B","best_trigger":"TRG_C26_R8_L100_214270_20211130_FSN_NFT_THEME_CAP","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"4B_guardrail_validated_by_high_MAE","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Non-price theme evidence plus large subsequent drawdown supports event-cap 4B classification rather than positive C26 promotion."}
{"row_type":"trigger","trigger_id":"TRG_C26_R8_L100_035420_20200730_NAVER_SEARCH_COMMERCE","case_id":"C26_R8_L100_035420_20200730_NAVER_SEARCH_COMMERCE","symbol":"035420","company_name":"NAVER","round":"R8","loop":"100","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"SEARCH_COMMERCE_AD_RECOVERY_OPERATING_LEVERAGE","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage3-Yellow","trigger_date":"2020-07-30","entry_date":"2020-07-30","entry_price":294000.0,"evidence_available_at_that_date":"Q2 2020 record sales and operating profit; e-commerce and search-based advertising revenue grew with online shopping demand.","evidence_source":"https://koreajoongangdaily.joins.com/2020/07/30/business/industry/Naver-Q2-earnings/20200730181700420.html","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","repeat_order_or_conversion","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/035/035420/2020.csv|atlas/ohlcv_tradable_by_symbol_year/035/035420/2021.csv","profile_path":"atlas/symbol_profiles/035/035420.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":18.03,"MFE_90D_pct":18.03,"MFE_180D_pct":39.46,"MAE_30D_pct":-1.02,"MAE_90D_pct":-6.97,"MAE_180D_pct":-6.97,"peak_date":"2021-03-18","peak_price":410000.0,"drawdown_after_peak_pct":-9.27,"green_lateness_ratio":0.35,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_a_4B_trigger","trigger_outcome_label":"score_return_aligned_positive","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","corporate_action_candidate_dates_in_profile":["2004-02-26","2004-03-26","2006-07-14","2006-08-16","2013-08-29","2018-10-12"],"corporate_action_candidate_overlap_180D":[],"share_count_variation_180D_pct":0.0,"data_caveat":null,"same_entry_group_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE:035420:Stage3-Yellow:2020-07-30","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":false}
{"row_type":"trigger","trigger_id":"TRG_C26_R8_L100_067160_20210726_AFREECATV_AD_PLATFORM","case_id":"C26_R8_L100_067160_20210726_AFREECATV_AD_PLATFORM","symbol":"067160","company_name":"SOOP/AfreecaTV","round":"R8","loop":"100","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"LIVE_STREAMING_AD_PLATFORM_OPERATING_LEVERAGE","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage3-Yellow","trigger_date":"2021-07-26","entry_date":"2021-07-26","entry_price":127800.0,"evidence_available_at_that_date":"Q2 2021 revenue +44% and operating profit +97%; live-streaming platform strengthened into digital advertising platform.","evidence_source":"https://www.koreaherald.com/article/2660482","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","repeat_order_or_conversion","durable_customer_confirmation"],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/067/067160/2021.csv|atlas/ohlcv_tradable_by_symbol_year/067/067160/2022.csv","profile_path":"atlas/symbol_profiles/067/067160.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":32.24,"MFE_90D_pct":94.91,"MFE_180D_pct":94.91,"MAE_30D_pct":-7.43,"MAE_90D_pct":-7.43,"MAE_180D_pct":-7.43,"peak_date":"2021-11-09","peak_price":249100.0,"drawdown_after_peak_pct":-47.01,"green_lateness_ratio":0.2,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_a_4B_trigger","trigger_outcome_label":"missed_structural_with_4B_overlay_after_peak","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","corporate_action_candidate_dates_in_profile":["2005-12-27","2007-06-05","2007-06-14","2008-01-24","2011-01-27"],"corporate_action_candidate_overlap_180D":[],"share_count_variation_180D_pct":0.0,"data_caveat":null,"same_entry_group_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE:067160:Stage3-Yellow:2021-07-26","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":false}
{"row_type":"trigger","trigger_id":"TRG_C26_R8_L100_035720_20210806_KAKAO_TALKBIZ_COST_DRAG","case_id":"C26_R8_L100_035720_20210806_KAKAO_TALKBIZ_COST_DRAG","symbol":"035720","company_name":"Kakao","round":"R8","loop":"100","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"TALK_BIZ_AD_COMMERCE_GROUP_COST_DRAG","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2021-08-06","entry_date":"2021-08-06","entry_price":145500.0,"evidence_available_at_that_date":"Q2 2021 Talk Biz and platform growth were strong, but the listed vehicle carried group-level cost, regulation and non-ad segment drag.","evidence_source":"https://www.asiae.co.kr/en/article/2021080609394402183","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","financial_visibility"],"stage4b_evidence_fields":["legal_or_regulatory_block","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/035/035720/2021.csv|atlas/ohlcv_tradable_by_symbol_year/035/035720/2022.csv","profile_path":"atlas/symbol_profiles/035/035720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.25,"MFE_90D_pct":8.25,"MFE_180D_pct":8.25,"MAE_30D_pct":-18.9,"MAE_90D_pct":-24.05,"MAE_180D_pct":-43.51,"peak_date":"2021-09-03","peak_price":157500.0,"drawdown_after_peak_pct":-47.81,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_a_4B_trigger","trigger_outcome_label":"good_business_signal_bad_stock_path","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","corporate_action_candidate_dates_in_profile":["2000-02-03","2000-03-03","2006-05-19","2014-10-14","2021-04-15"],"corporate_action_candidate_overlap_180D":[],"share_count_variation_180D_pct":0.4073,"data_caveat":"minor_share_count_variation_non_blocking","same_entry_group_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE:035720:Stage2-Actionable:2021-08-06","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":false}
{"row_type":"trigger","trigger_id":"TRG_C26_R8_L100_089600_20210813_NASMEDIA_MEDIAREP_RECOVERY","case_id":"C26_R8_L100_089600_20210813_NASMEDIA_MEDIAREP_RECOVERY","symbol":"089600","company_name":"Nasmedia","round":"R8","loop":"100","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"MEDIA_REP_AD_RECOVERY_NOT_OWNED_PLATFORM","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2021-08-12","entry_date":"2021-08-13","entry_price":39100.0,"evidence_available_at_that_date":"Q2 2021 revenue and operating profit grew double digits as online display/search/mobile-platform ads recovered, but it was mostly media-rep/cyclical recovery.","evidence_source":"https://www.nasmedia.co.kr/%EB%B3%B4%EB%8F%84%EC%9E%90%EB%A3%8C/%EB%82%98%EC%8A%A4%EB%AF%B8%EB%94%94%EC%96%B4-2%EB%B6%84%EA%B8%B0-%EB%A7%A4%EC%B6%9C-%EB%B0%8F-%EC%98%81%EC%97%85%EC%9D%B5-%EC%9E%91%EB%85%84%EB%B9%84-%EB%91%90-%EC%9E%90%EB%A6%AC-%EC%88%98-%EC%84%B1/","stage2_evidence_fields":["public_event_or_disclosure","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","financial_visibility"],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089600/2021.csv|atlas/ohlcv_tradable_by_symbol_year/089/089600/2022.csv","profile_path":"atlas/symbol_profiles/089/089600.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.3,"MFE_90D_pct":2.3,"MFE_180D_pct":2.3,"MAE_30D_pct":-15.6,"MAE_90D_pct":-22.63,"MAE_180D_pct":-34.02,"peak_date":"2021-08-13","peak_price":40000.0,"drawdown_after_peak_pct":-35.5,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_a_4B_trigger","trigger_outcome_label":"ad_market_recovery_not_platform_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","corporate_action_candidate_dates_in_profile":[],"corporate_action_candidate_overlap_180D":[],"share_count_variation_180D_pct":9.7351,"data_caveat":"minor_share_count_variation_non_blocking","same_entry_group_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE:089600:Stage2-Actionable:2021-08-13","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":false}
{"row_type":"trigger","trigger_id":"TRG_C26_R8_L100_214270_20211130_FSN_NFT_THEME_CAP","case_id":"C26_R8_L100_214270_20211130_FSN_NFT_THEME_CAP","symbol":"214270","company_name":"FSN","round":"R8","loop":"100","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"DIGITAL_MARKETING_NFT_THEME_EVENT_CAP","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage4B","trigger_date":"2021-11-30","entry_date":"2021-11-30","entry_price":10250.0,"evidence_available_at_that_date":"FSN traded as a mobile-ad/digital-marketing company caught in the 2021 NFT theme; this is an event-premium cap rather than clean ad-operating-leverage.","evidence_source":"https://www.etnews.com/20211130000111","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","explicit_event_cap"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/214/214270/2021.csv|atlas/ohlcv_tradable_by_symbol_year/214/214270/2022.csv","profile_path":"atlas/symbol_profiles/214/214270.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":38.54,"MFE_90D_pct":38.54,"MFE_180D_pct":38.54,"MAE_30D_pct":-2.44,"MAE_90D_pct":-31.71,"MAE_180D_pct":-60.98,"peak_date":"2022-01-03","peak_price":14200.0,"drawdown_after_peak_pct":-71.83,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"good_full_window_4B_timing_with_non_price_theme_evidence","trigger_outcome_label":"4B_guardrail_validated_by_high_MAE","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","corporate_action_candidate_dates_in_profile":["2016-10-05","2018-03-05","2021-11-08"],"corporate_action_candidate_overlap_180D":[],"share_count_variation_180D_pct":5.4884,"data_caveat":"minor_share_count_variation_non_blocking","same_entry_group_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE:214270:Stage4B:2021-11-30","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C26_shadow","case_id":"C26_R8_L100_035420_20200730_NAVER_SEARCH_COMMERCE","trigger_id":"TRG_C26_R8_L100_035420_20200730_NAVER_SEARCH_COMMERCE","symbol":"035420","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":78,"revision_score":72,"relative_strength_score":65,"customer_quality_score":70,"policy_or_regulatory_score":0,"valuation_repricing_score":62,"execution_risk_score":20,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":78.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":82,"revision_score":76,"relative_strength_score":68,"customer_quality_score":74,"policy_or_regulatory_score":0,"valuation_repricing_score":62,"execution_risk_score":18,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":81.0,"stage_label_after":"Stage3-Yellow","changed_components":["margin_bridge_score","revision_score","customer_quality_score","valuation_repricing_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"Owned-platform search/commerce evidence gets modest C26 reinforcement; no global threshold change.","MFE_90D_pct":18.03,"MAE_90D_pct":-6.97,"score_return_alignment_label":"score_return_aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C26_shadow","case_id":"C26_R8_L100_067160_20210726_AFREECATV_AD_PLATFORM","trigger_id":"TRG_C26_R8_L100_067160_20210726_AFREECATV_AD_PLATFORM","symbol":"067160","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":74,"revision_score":70,"relative_strength_score":75,"customer_quality_score":68,"policy_or_regulatory_score":0,"valuation_repricing_score":66,"execution_risk_score":24,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":72.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":88,"revision_score":83,"relative_strength_score":84,"customer_quality_score":82,"policy_or_regulatory_score":0,"valuation_repricing_score":70,"execution_risk_score":22,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":88.0,"stage_label_after":"Stage3-Green","changed_components":["margin_bridge_score","revision_score","customer_quality_score","valuation_repricing_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"Owned live-streaming ad-platform operating leverage is stronger than generic digital-ad recovery; allow C26-specific fast Green only with margin bridge.","MFE_90D_pct":94.91,"MAE_90D_pct":-7.43,"score_return_alignment_label":"missed_structural_with_4B_overlay_after_peak","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C26_shadow","case_id":"C26_R8_L100_035720_20210806_KAKAO_TALKBIZ_COST_DRAG","trigger_id":"TRG_C26_R8_L100_035720_20210806_KAKAO_TALKBIZ_COST_DRAG","symbol":"035720","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":72,"revision_score":75,"relative_strength_score":63,"customer_quality_score":82,"policy_or_regulatory_score":0,"valuation_repricing_score":70,"execution_risk_score":30,"legal_or_contract_risk_score":22,"dilution_cb_risk_score":0,"accounting_trust_risk_score":6},"weighted_score_before":76.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":64,"revision_score":70,"relative_strength_score":55,"customer_quality_score":80,"policy_or_regulatory_score":0,"valuation_repricing_score":54,"execution_risk_score":48,"legal_or_contract_risk_score":42,"dilution_cb_risk_score":0,"accounting_trust_risk_score":8},"weighted_score_after":66.0,"stage_label_after":"Stage2-Actionable","changed_components":["margin_bridge_score","revision_score","customer_quality_score","valuation_repricing_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"Demote platform conglomerate ad growth when group cost/regulatory risk and non-ad segment drag overwhelm ad evidence.","MFE_90D_pct":8.25,"MAE_90D_pct":-24.05,"score_return_alignment_label":"good_business_signal_bad_stock_path","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C26_shadow","case_id":"C26_R8_L100_089600_20210813_NASMEDIA_MEDIAREP_RECOVERY","trigger_id":"TRG_C26_R8_L100_089600_20210813_NASMEDIA_MEDIAREP_RECOVERY","symbol":"089600","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":70,"revision_score":68,"relative_strength_score":50,"customer_quality_score":50,"policy_or_regulatory_score":0,"valuation_repricing_score":58,"execution_risk_score":34,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":73.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":58,"revision_score":60,"relative_strength_score":42,"customer_quality_score":42,"policy_or_regulatory_score":0,"valuation_repricing_score":44,"execution_risk_score":48,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":61.0,"stage_label_after":"Stage1-Watch","changed_components":["margin_bridge_score","revision_score","customer_quality_score","valuation_repricing_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"Media-rep ad market recovery should not receive the same C26 multiplier as owned-platform monetization.","MFE_90D_pct":2.3,"MAE_90D_pct":-22.63,"score_return_alignment_label":"ad_market_recovery_not_platform_rerating","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C26_shadow","case_id":"C26_R8_L100_214270_20211130_FSN_NFT_THEME_CAP","trigger_id":"TRG_C26_R8_L100_214270_20211130_FSN_NFT_THEME_CAP","symbol":"214270","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":45,"revision_score":55,"relative_strength_score":82,"customer_quality_score":45,"policy_or_regulatory_score":0,"valuation_repricing_score":78,"execution_risk_score":48,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_before":68.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":35,"revision_score":45,"relative_strength_score":80,"customer_quality_score":35,"policy_or_regulatory_score":0,"valuation_repricing_score":42,"execution_risk_score":65,"legal_or_contract_risk_score":18,"dilution_cb_risk_score":16,"accounting_trust_risk_score":12},"weighted_score_after":58.0,"stage_label_after":"Stage4B","changed_components":["margin_bridge_score","revision_score","customer_quality_score","valuation_repricing_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"NFT/theme premium is explicitly capped as Stage4B; no positive C26 promotion from event-premium alone.","MFE_90D_pct":38.54,"MAE_90D_pct":-31.71,"score_return_alignment_label":"4B_guardrail_validated_by_high_MAE","current_profile_verdict":"current_profile_correct"}
{"row_type":"residual_contribution","round":"R8","loop":"100","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","new_independent_case_count":5,"reused_case_count":0,"new_symbol_count":5,"new_trigger_family_count":5,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["owned_platform_ad_operating_leverage_too_late","media_rep_ad_recovery_false_positive","platform_conglomerate_cost_regulatory_drag_false_positive","nft_theme_event_cap_high_MAE"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,owned_platform_ad_margin_bridge_gate,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,1,+1,"Promote only owned-platform ad products with actual margin/OP bridge and repeat monetization evidence.","NAVER/SOOP positives separate cleanly from Kakao/Nasmedia false positives.","TRG_C26_R8_L100_035420_20200730_NAVER_SEARCH_COMMERCE|TRG_C26_R8_L100_067160_20210726_AFREECATV_AD_PLATFORM",5,5,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,media_rep_ad_recovery_ceiling,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,1,+1,"Generic digital ad market recovery at a media rep/agency receives Stage2 ceiling unless owned-platform monetization or 2Q margin durability exists.","Nasmedia Q2 beat had MFE180 2.30 and MAE180 -34.02.","TRG_C26_R8_L100_089600_20210813_NASMEDIA_MEDIAREP_RECOVERY",5,5,2,medium,canonical_shadow_only,"limits false positive green"
shadow_weight,theme_event_premium_4B_cap,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,1,+1,"NFT/metaverse/platform-optionality without confirmed ad-revenue conversion routes to Stage4B/event cap.","FSN MFE180 38.54 but MAE180 -60.98 and DD after peak -71.83.","TRG_C26_R8_L100_214270_20211130_FSN_NFT_THEME_CAP",5,5,2,medium,guardrail_shadow_only,"4B overlay/risk calibration only"
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/{prefix}/{ticker}/{year}.csv.
- Symbol profile pattern: atlas/symbol_profiles/{prefix}/{ticker}.json.

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

```yaml
completed_round: R8
completed_loop: 100
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 / under 30 rows
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: mixed_C26_fine_archetype_set
next_recommended_archetypes:
  - C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
  - C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
  - C31_POLICY_SUBSIDY_LEGISLATION_EVENT
  - C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
  - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
```

Next execution should again read the latest no-repeat index first. It should not mechanically continue to R9 unless C29 remains the best coverage gap.

## 28. Source Notes

```yaml
execution_prompt: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
no_repeat_index: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
stock_web_manifest: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
stock_web_schema: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/schema.json
evidence_sources:
  NAVER: https://koreajoongangdaily.joins.com/2020/07/30/business/industry/Naver-Q2-earnings/20200730181700420.html
  SOOP_AfreecaTV: https://www.koreaherald.com/article/2660482
  Kakao: https://www.asiae.co.kr/en/article/2021080609394402183
  Nasmedia_official: https://www.nasmedia.co.kr/%EB%B3%B4%EB%8F%84%EC%9E%90%EB%A3%8C/%EB%82%98%EC%8A%A4%EB%AF%B8%EB%94%94%EC%96%B4-2%EB%B6%84%EA%B8%B0-%EB%A7%A4%EC%B6%9C-%EB%B0%8F-%EC%98%81%EC%97%85%EC%9D%B5-%EC%9E%91%EB%85%84%EB%B9%84-%EB%91%90-%EC%9E%90%EB%A6%AC-%EC%88%98-%EC%84%B1/
  Nasmedia_alt: https://www.newstomato.com/ReadNews.aspx?no=1066607
  FSN_NFT_theme: https://www.etnews.com/20211130000111
  FSN_official_profile: https://www.fsn.co.kr/
  FSN_company_profile: https://www.marketscreener.com/quote/stock/FSN-CO-LTD-120972383/company/
price_shards_downloaded_for_this_research:
  - /mnt/data/035420_2020.csv
  - /mnt/data/035420_2021.csv
  - /mnt/data/067160_2021.csv
  - /mnt/data/067160_2022.csv
  - /mnt/data/035720_2021.csv
  - /mnt/data/035720_2022.csv
  - /mnt/data/089600_2021.csv
  - /mnt/data/089600_2022.csv
  - /mnt/data/214270_2021.csv
  - /mnt/data/214270_2022.csv
```

## Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 5
calibration_usable_trigger_count: 5
representative_trigger_count: 5
new_weight_evidence_candidate_count: 5
guardrail_candidate_count: 1
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
standard_filename_ok: true
filename_matches_metadata: true
uses_no_repeat_index_as_ledger_only: true
uses_stock_web_actual_ohlcv: true
source_proxy_only_rows: 0
future_data_leakage_detected: false
production_code_patch_included: false
production_scoring_patch_applied: false
ready_for_batch_ingest: true
```
