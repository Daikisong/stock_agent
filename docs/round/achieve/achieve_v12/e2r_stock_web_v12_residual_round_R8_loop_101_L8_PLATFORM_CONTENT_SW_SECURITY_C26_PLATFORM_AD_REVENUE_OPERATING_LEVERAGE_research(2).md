# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file: e2r_stock_web_v12_residual_round_R8_loop_101_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md
selected_round: R8
selected_loop: 101
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: mixed_C26_digital_ad_rep_owned_platform_operating_leverage_quality_holdout
loop_objective:
  - holdout_validation
  - counterexample_mining
  - canonical_archetype_compression
  - 4B_non_price_requirement_stress_test
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 2 / quality holdout after session-adjusted Priority 0-1 fills
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
auto_selected_coverage_gap: C26 static 106 rows; this session adds holdout quality rows only, not a coverage-gap fill claim
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

The residual question is narrower than the prior C26 pass: **digital-ad recovery, media-rep earnings, portal AI relabeling, and owned-platform operating leverage should not share the same C26 promotion path.** C26 needs a fine gate that rewards durable monetization and margin bridge, while capping agency/event stories that create high-MAE price paths.

## 2. Round / Large Sector / Canonical Archetype Scope

```yaml
round: R8
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
canonical_scope_definition: platform advertising revenue, digital-ad monetization, and platform operating leverage
invalid_round_sector_pair: false
```

C26 maps to R8 / L8. R13 is not used because this is an individual platform/SW/content archetype quality holdout, not a cross-archetype red-team checkpoint.

## 3. Previous Coverage / Duplicate Avoidance Check

```yaml
no_repeat_index_role: duplicate_ledger_only
static_index_C26_rows: 106
static_index_guidance: Priority 2 quality holdout; URL/proxy repair, counterexample balance, and 4B/4C balance before new quantity
previous_C26_symbols_avoided:
  - 035420
  - 067160
  - 035720
  - 089600
  - 214270
  - 042000
hard_duplicate_key: canonical_archetype_id + symbol + trigger_type + entry_date
new_symbol_count: 8
reused_case_count: 0
new_trigger_family_count: 8
```

All cases below are new C26 symbols relative to the visible current-session C26 row set. The prior owned-platform examples are not repeated.

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

| symbol | entry_date | 180D_end | entry_exists | forward_180D | MFE/MAE_6_fields | corp_action_status | overlap_dates |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 030000 | 2024-04-26 | 2025-01-22 | yes | yes | yes | clean_180D_window | - |
| 216050 | 2025-01-23 | 2025-10-23 | yes | yes | yes | clean_180D_window | - |
| 237820 | 2023-11-06 | 2024-07-29 | yes | yes | yes | clean_180D_window | - |
| 123570 | 2024-06-28 | 2025-03-27 | yes | yes | yes | clean_180D_window | - |
| 236810 | 2024-05-14 | 2025-02-11 | yes | yes | yes | clean_180D_window | - |
| 363260 | 2024-06-24 | 2025-03-21 | yes | yes | yes | clean_180D_window | - |
| 273060 | 2025-05-16 | 2026-02-06 | yes | yes | yes | clean_180D_window | - |
| 239340 | 2024-04-01 | 2024-12-24 | yes | yes | yes | clean_180D_window | - |

All representative trigger rows have entry date, entry price, forward 180 tradable rows, and complete 30D/90D/180D MFE and MAE fields. No profile-level corporate-action candidate date overlaps the entry-to-180D windows. The Mobidays prior corporate-action candidate date is before the chosen entry window and is retained as a non-blocking caveat.

## 6. Canonical Archetype Compression Map

```yaml
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
compression_goal: separate owned/durable ad operating leverage from agency/media-rep/event/AI relabeling stories
fine_archetypes:
  - GLOBAL_AGENCY_DIGITAL_BTL_MARGIN_BRIDGE_WEAK
  - MEDIAREP_AD_BUSINESS_TOPLINE_OPERATING_LEVERAGE
  - PERFORMANCE_MARKETING_OPERATING_LEVERAGE_FORECAST
  - NAVER_AD_AGENCY_REVENUE_INCREASE_WITH_WEAK_DURABILITY
  - OFFERWALL_PLATFORM_MAU_WITH_PROFITABILITY_GAP
  - MOBILE_MARKETING_PLATFORM_NEW_BUSINESS_INVESTMENT_COST_DRAG
  - DIGITAL_AD_AGENCY_RECORD_QUARTER_TURNAROUND_LEVERAGE
  - PORTAL_AD_BUSINESS_DECLINE_AI_RENAME_EVENT_CAP
```

Compression rule: **C26 should promote faster only when digital-ad monetization has durable customer/owned-platform quality and an operating-profit bridge.** Generic ad-cycle recovery, portal relabeling, agency gross billings, and event-premium narratives stay capped at Stage2 or local 4B watch until revenue retention and margin conversion appear.

## 7. Case Selection Summary

| symbol | company | case_type | trigger_type | entry_date | entry_price | MFE90 | MAE90 | MFE180 | MAE180 | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 030000 | 제일기획 | failed_rerating | Stage2-Actionable | 2024-04-26 | 18750 | 4.3733 | -12.5333 | 4.3733 | -12.5333 | current_profile_false_positive |
| 216050 | 인크로스 | structural_success | Stage3-Yellow | 2025-01-23 | 7340 | 13.079 | -16.0763 | 28.2016 | -16.0763 | current_profile_too_late |
| 237820 | 플레이디 | high_mae_success | Stage3-Yellow | 2023-11-06 | 4360 | 144.4954 | -6.3073 | 144.4954 | -6.3073 | current_profile_correct |
| 123570 | 이엠넷 | failed_rerating | Stage2-Actionable | 2024-06-28 | 2980 | 20.8054 | -22.8188 | 20.8054 | -28.5235 | current_profile_false_positive |
| 236810 | 엔비티 | failed_rerating | Stage2-Actionable | 2024-05-14 | 6260 | 25.3994 | -48.4824 | 25.3994 | -54.8722 | current_profile_false_positive |
| 363260 | 모비데이즈 | failed_rerating | Stage2-Actionable | 2024-06-24 | 2310 | 29.2208 | -32.7273 | 29.2208 | -39.2208 | current_profile_false_positive |
| 273060 | 와이즈버즈 | structural_success | Stage3-Yellow | 2025-05-16 | 1061 | 30.066 | -8.1056 | 35.8153 | -24.5994 | current_profile_too_late |
| 239340 | 이스트에이드 | failed_rerating | Stage2-Actionable | 2024-04-01 | 3065 | 0.6525 | -51.093 | 0.6525 | -54.0294 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

```yaml
positive_structural_success: 3
counterexample_or_failed_rerating: 5
4B_or_4C_case: 6
4C_case: 0
minimum_positive_case_count_met: true
minimum_counterexample_count_met: true
minimum_calibration_usable_case_count_met: true
```

This is not a broad C26 promotion file. It is a quality holdout: it keeps positive rows where revenue/OP bridge was actually visible, but forces a guardrail on agency/portal/event stories whose 90D/180D MAE became too deep.

## 9. Evidence Source Map

| symbol | company | trigger_date | evidence_source | evidence_use |
| --- | --- | --- | --- | --- |
| 030000 | 제일기획 | 2024-04-26 | https://buffettlab.co.kr/news/view.php?idx=47053 | 2024년 1분기 실적은 전년 대비 영업이익 소폭 증가와 디지털/BTL 중심 방어를 보였지만, agency gross-profit mix가 owned-platform ad leverage로 전환된 근거는 약했다. |
| 216050 | 인크로스 | 2025-01-22 | https://www.incross.com/ko/investment/ir.asp?idx=10203&mode=view&page=1&pageSize=10&searchStr=&serboardsort= | 2024년 4분기 광고사업 호조와 top-line 확대에 따른 레버리지 효과가 있었지만 일회성 비용도 같이 확인되어 Green보다는 Yellow/4B watch가 맞았다. |
| 237820 | 플레이디 | 2023-11-03 | https://ssl.pstatic.net/imgstock/upload/research/company/1698966461488.pdf | 2024년 광고시장 회복, KT그룹향 캡티브 광고, 비용 절감과 영업레버리지 전망이 붙어 90D MFE가 크게 열렸지만 이후 drawdown이 커 4B overlay가 필요했다. |
| 123570 | 이엠넷 | 2024-06-28 | https://stock.pstatic.net/stock-research/company/72/20240628_company_482347000.pdf | 2024년 1분기 네이버 광고대행 매출 증가와 디지털 광고 전문성은 Stage2 근거지만, channel/retention/margin bridge가 약해 MAE가 깊어졌다. |
| 236810 | 엔비티 | 2024-05-14 | https://file.alphasquare.co.kr/media/pdfs/company-ir/20240514%EC%97%94%EB%B9%84%ED%8B%B0_%ED%9A%8C%EC%82%AC_%EC%86%8C%EA%B0%9C_%EB%B0%8F_%EC%A3%BC%EC%9A%94_%EC%82%AC%EC%97%85%ED%98%84%ED%99%A9.pdf | 애디슨 오퍼월의 점유율/MAU/네이버웹툰 도입 근거는 플랫폼 monetization의 Stage2 근거였지만, 수익성·영업손실 guard가 없으면 180D MAE가 크게 열렸다. |
| 363260 | 모비데이즈 | 2024-06-21 | https://www.hanaw.com/download/research/FileServer/WEB/info/small_cap/2024/06/21/240624_mobidays.pdf | 2024년 1분기 매출은 YoY +72.4%였지만 신사업 투자로 영업손실을 기록했고, TikTok/K-pop platform optionality는 C26 Stage3보다 4B watch가 맞았다. |
| 273060 | 와이즈버즈 | 2025-05-15 | https://www.hankyung.com/article/202505155071O | 2025년 1분기 매출 +111.7%, 영업이익 흑자전환/개선이 확인되어 C26 operating leverage positive였지만, 180D MAE가 -20%를 넘어 local 4B watch가 필요했다. |
| 239340 | 이스트에이드 | 2024-04-01 | https://www.ddaily.co.kr/page/view/2024033118081470309 | 줌인터넷/이스트에이드의 광고사업 매출 감소와 사명변경·AI 포털 optionality가 같이 있었지만, 광고 revenue operating leverage로 보기는 어려워 Stage2 false-positive였다. |

## 10. Price Data Source Map

| symbol | profile_path | price_shards_used | price_basis | adjustment |
| --- | --- | --- | --- | --- |
| 030000 | atlas/symbol_profiles/030/030000.json | atlas/ohlcv_tradable_by_symbol_year/030/030000/2024.csv+atlas/ohlcv_tradable_by_symbol_year/030/030000/2025.csv | tradable_raw | raw_unadjusted_marcap |
| 216050 | atlas/symbol_profiles/216/216050.json | atlas/ohlcv_tradable_by_symbol_year/216/216050/2025.csv | tradable_raw | raw_unadjusted_marcap |
| 237820 | atlas/symbol_profiles/237/237820.json | atlas/ohlcv_tradable_by_symbol_year/237/237820/2023.csv+atlas/ohlcv_tradable_by_symbol_year/237/237820/2024.csv | tradable_raw | raw_unadjusted_marcap |
| 123570 | atlas/symbol_profiles/123/123570.json | atlas/ohlcv_tradable_by_symbol_year/123/123570/2024.csv+atlas/ohlcv_tradable_by_symbol_year/123/123570/2025.csv | tradable_raw | raw_unadjusted_marcap |
| 236810 | atlas/symbol_profiles/236/236810.json | atlas/ohlcv_tradable_by_symbol_year/236/236810/2024.csv+atlas/ohlcv_tradable_by_symbol_year/236/236810/2025.csv | tradable_raw | raw_unadjusted_marcap |
| 363260 | atlas/symbol_profiles/363/363260.json | atlas/ohlcv_tradable_by_symbol_year/363/363260/2024.csv+atlas/ohlcv_tradable_by_symbol_year/363/363260/2025.csv | tradable_raw | raw_unadjusted_marcap |
| 273060 | atlas/symbol_profiles/273/273060.json | atlas/ohlcv_tradable_by_symbol_year/273/273060/2025.csv+atlas/ohlcv_tradable_by_symbol_year/273/273060/2026.csv | tradable_raw | raw_unadjusted_marcap |
| 239340 | atlas/symbol_profiles/239/239340.json | atlas/ohlcv_tradable_by_symbol_year/239/239340/2024.csv | tradable_raw | raw_unadjusted_marcap |

## 11. Case-by-Case Trigger Grid

### C26_L101_CASE_01_030000 / 제일기획 / 030000

- Trigger date: `2024-04-26`
- Trigger type: `Stage2-Actionable`
- Evidence mechanism: 2024년 1분기 실적은 전년 대비 영업이익 소폭 증가와 디지털/BTL 중심 방어를 보였지만, agency gross-profit mix가 owned-platform ad leverage로 전환된 근거는 약했다.
- Stage2 evidence fields: `public_event_or_disclosure, early_revision_signal, relative_strength`
- Stage3 evidence fields: `financial_visibility`
- 4B evidence fields: `margin_or_backlog_slowdown`
- Price path: MFE180 `4.3733` / MAE180 `-12.5333` / peak `2024-05-10 @ 19570.0`.
- Current profile verdict: `current_profile_false_positive`.
- Residual lesson: `agency_digital_btl_defense_low_mfe_counterexample`.

### C26_L101_CASE_02_216050 / 인크로스 / 216050

- Trigger date: `2025-01-22`
- Trigger type: `Stage3-Yellow`
- Evidence mechanism: 2024년 4분기 광고사업 호조와 top-line 확대에 따른 레버리지 효과가 있었지만 일회성 비용도 같이 확인되어 Green보다는 Yellow/4B watch가 맞았다.
- Stage2 evidence fields: `public_event_or_disclosure, customer_or_order_quality, early_revision_signal`
- Stage3 evidence fields: `financial_visibility, margin_bridge, multiple_public_sources`
- 4B evidence fields: `margin_or_backlog_slowdown`
- Price path: MFE180 `28.2016` / MAE180 `-16.0763` / peak `2025-06-24 @ 9410.0`.
- Current profile verdict: `current_profile_too_late`.
- Residual lesson: `ad_business_recovery_with_oneoff_cost_yellow_positive`.

### C26_L101_CASE_03_237820 / 플레이디 / 237820

- Trigger date: `2023-11-03`
- Trigger type: `Stage3-Yellow`
- Evidence mechanism: 2024년 광고시장 회복, KT그룹향 캡티브 광고, 비용 절감과 영업레버리지 전망이 붙어 90D MFE가 크게 열렸지만 이후 drawdown이 커 4B overlay가 필요했다.
- Stage2 evidence fields: `public_event_or_disclosure, capacity_or_volume_route, early_revision_signal`
- Stage3 evidence fields: `confirmed_revision, margin_bridge, financial_visibility`
- 4B evidence fields: `valuation_blowoff, price_only_local_peak, positioning_overheat`
- Price path: MFE180 `144.4954` / MAE180 `-6.3073` / peak `2024-03-06 @ 10660.0`.
- Current profile verdict: `current_profile_correct`.
- Residual lesson: `performance_marketing_forecast_large_mfe_with_4b_overlay`.

### C26_L101_CASE_04_123570 / 이엠넷 / 123570

- Trigger date: `2024-06-28`
- Trigger type: `Stage2-Actionable`
- Evidence mechanism: 2024년 1분기 네이버 광고대행 매출 증가와 디지털 광고 전문성은 Stage2 근거지만, channel/retention/margin bridge가 약해 MAE가 깊어졌다.
- Stage2 evidence fields: `public_event_or_disclosure, customer_or_order_quality, early_revision_signal`
- Stage3 evidence fields: `none`
- 4B evidence fields: `margin_or_backlog_slowdown, price_only_local_peak`
- Price path: MFE180 `20.8054` / MAE180 `-28.5235` / peak `2024-07-30 @ 3600.0`.
- Current profile verdict: `current_profile_false_positive`.
- Residual lesson: `naver_ad_agency_revenue_increase_high_mae_counterexample`.

### C26_L101_CASE_05_236810 / 엔비티 / 236810

- Trigger date: `2024-05-14`
- Trigger type: `Stage2-Actionable`
- Evidence mechanism: 애디슨 오퍼월의 점유율/MAU/네이버웹툰 도입 근거는 플랫폼 monetization의 Stage2 근거였지만, 수익성·영업손실 guard가 없으면 180D MAE가 크게 열렸다.
- Stage2 evidence fields: `public_event_or_disclosure, customer_or_order_quality, capacity_or_volume_route`
- Stage3 evidence fields: `none`
- 4B evidence fields: `margin_or_backlog_slowdown, positioning_overheat, price_only_local_peak`
- Price path: MFE180 `25.3994` / MAE180 `-54.8722` / peak `2024-06-03 @ 7850.0`.
- Current profile verdict: `current_profile_false_positive`.
- Residual lesson: `offerwall_mau_platform_profitability_gap_high_mae_counterexample`.

### C26_L101_CASE_06_363260 / 모비데이즈 / 363260

- Trigger date: `2024-06-21`
- Trigger type: `Stage2-Actionable`
- Evidence mechanism: 2024년 1분기 매출은 YoY +72.4%였지만 신사업 투자로 영업손실을 기록했고, TikTok/K-pop platform optionality는 C26 Stage3보다 4B watch가 맞았다.
- Stage2 evidence fields: `public_event_or_disclosure, policy_or_regulatory_optionality, early_revision_signal`
- Stage3 evidence fields: `none`
- 4B evidence fields: `margin_or_backlog_slowdown, positioning_overheat, price_only_local_peak`
- Price path: MFE180 `29.2208` / MAE180 `-39.2208` / peak `2024-10-23 @ 2985.0`.
- Current profile verdict: `current_profile_false_positive`.
- Residual lesson: `mobile_marketing_growth_with_investment_cost_drag_counterexample`.

### C26_L101_CASE_07_273060 / 와이즈버즈 / 273060

- Trigger date: `2025-05-15`
- Trigger type: `Stage3-Yellow`
- Evidence mechanism: 2025년 1분기 매출 +111.7%, 영업이익 흑자전환/개선이 확인되어 C26 operating leverage positive였지만, 180D MAE가 -20%를 넘어 local 4B watch가 필요했다.
- Stage2 evidence fields: `public_event_or_disclosure, early_revision_signal, relative_strength`
- Stage3 evidence fields: `confirmed_revision, margin_bridge, financial_visibility`
- 4B evidence fields: `positioning_overheat, price_only_local_peak`
- Price path: MFE180 `35.8153` / MAE180 `-24.5994` / peak `2026-01-30 @ 1441.0`.
- Current profile verdict: `current_profile_too_late`.
- Residual lesson: `record_quarter_turnaround_operating_leverage_positive_with_4b`.

### C26_L101_CASE_08_239340 / 이스트에이드 / 239340

- Trigger date: `2024-04-01`
- Trigger type: `Stage2-Actionable`
- Evidence mechanism: 줌인터넷/이스트에이드의 광고사업 매출 감소와 사명변경·AI 포털 optionality가 같이 있었지만, 광고 revenue operating leverage로 보기는 어려워 Stage2 false-positive였다.
- Stage2 evidence fields: `public_event_or_disclosure, policy_or_regulatory_optionality`
- Stage3 evidence fields: `none`
- 4B evidence fields: `explicit_event_cap, margin_or_backlog_slowdown, price_only_local_peak`
- Price path: MFE180 `0.6525` / MAE180 `-54.0294` / peak `2024-04-01 @ 3085.0`.
- Current profile verdict: `current_profile_false_positive`.
- Residual lesson: `portal_ad_decline_ai_rename_event_cap_counterexample`.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 030000 | 2024-04-26 | 18750 | 4.3733 | -2.3467 | 4.3733 | -12.5333 | 4.3733 | -12.5333 | 2024-05-10 | 19570 | -16.1983 |
| 216050 | 2025-01-23 | 7340 | 5.7221 | -6.812 | 13.079 | -16.0763 | 28.2016 | -16.0763 | 2025-06-24 | 9410 | -27.2051 |
| 237820 | 2023-11-06 | 4360 | 27.2936 | -6.3073 | 144.4954 | -6.3073 | 144.4954 | -6.3073 | 2024-03-06 | 10660 | -50.1876 |
| 123570 | 2024-06-28 | 2980 | 20.8054 | -22.8188 | 20.8054 | -22.8188 | 20.8054 | -28.5235 | 2024-07-30 | 3600 | -40.8333 |
| 236810 | 2024-05-14 | 6260 | 25.3994 | -16.1342 | 25.3994 | -48.4824 | 25.3994 | -54.8722 | 2024-06-03 | 7850 | -64.0127 |
| 363260 | 2024-06-24 | 2310 | 21.2121 | -17.7922 | 29.2208 | -32.7273 | 29.2208 | -39.2208 | 2024-10-23 | 2985 | -52.9648 |
| 273060 | 2025-05-16 | 1061 | 9.9906 | -8.1056 | 30.066 | -8.1056 | 35.8153 | -24.5994 | 2026-01-30 | 1441 | -19.5003 |
| 239340 | 2024-04-01 | 3065 | 0.6525 | -12.5612 | 0.6525 | -51.093 | 0.6525 | -54.0294 | 2024-04-01 | 3085 | -54.3274 |

## 13. Current Calibrated Profile Stress Test

| question | answer |
|---|---|
| current calibrated profile 판단 | Owned-platform 또는 durable ad operating leverage와 단순 agency/media-rep/event story를 일부 구분하지만, C26 내부 fine gate가 약하면 제일기획·이엠넷·엔비티·모비데이즈·이스트에이드를 Stage2-Actionable 이상으로 과승격할 수 있다. |
| 실제 MFE/MAE와 정합성 | 평균 MFE180 `36.1205` 대비 평균 MAE180 `-29.5203`로, positive와 counterexample의 분산이 크다. |
| Stage2 bonus | agency/portal/event story에는 과했다. 운영레버리지 실현이 확인된 인크로스·플레이디·와이즈버즈에는 필요했다. |
| Yellow threshold 75 | durable margin bridge가 있는 row에는 적절하지만, revenue-only agency row에는 낮다. |
| Green threshold 87/revision 55 | 이번 holdout에서는 Green 승격을 거의 허용하지 않는 편이 맞다. |
| price-only blowoff guard | 플레이디·엔비티·모비데이즈·와이즈버즈에서 local 4B watch로 유지해야 한다. |
| full 4B non-price requirement | 단순 price spike만 full 4B로 보지 않되, investment-cost drag/AI rename/event premium은 non-price 4B 근거로 본다. |
| hard 4C routing | 계약취소·강한 thesis break가 없어 4C는 쓰지 않는다. |

## 14. Stage2 / Yellow / Green Comparison

```yaml
Stage2_or_Stage2_Actionable_rows: 5
Stage3_Yellow_rows: 3
Stage3_Green_rows: 0
Stage3_Green_lateness_audit: not_applicable_no_confirmed_Green_trigger
```

The safe compression is: Stage2 can open on public earnings/platform evidence, Yellow requires operating-profit bridge and durability, and Green should wait for repeat evidence because most C26 small/mid ad-platform rows had deep full-window drawdowns.

## 15. 4B Local vs Full-window Timing Audit

```yaml
local_4B_watch_rows: 6
full_4B_rows: 0
4B_reasoning: price-only or event-premium spikes are not full 4B without non-price overhang; however, cost drag, event cap, and weak margin conversion justify local 4B watch.
```

Rows with local 4B watch: `237820, 123570, 236810, 363260, 273060, 239340`.

## 16. 4C Protection Audit

```yaml
4C_case_count: 0
four_c_protection_label: not_applicable
reason: no hard contract cancellation, regulatory rejection, accounting break, forced liquidation, or confirmed thesis break was required for these C26 rows
```

## 17. Sector-Specific Rule Candidate

```text
L8_C26_PLATFORM_AD_OPERATING_LEVERAGE_REQUIRES_DURABLE_MONETIZATION_AND_MARGIN_BRIDGE_WITH_AGENCY_EVENT_4B_CAP
```

Rule effect: within L8, platform/ad stocks should not be treated as a single beta bucket. Owned-platform or high-retention ad monetization can promote to Yellow faster; agency/media-rep/portal/event-premium stories require margin bridge and lower execution risk before any Yellow promotion.

## 18. Canonical-Archetype Rule Candidate

```text
C26_DURABLE_AD_MONETIZATION_OP_BRIDGE_GATE_WITH_AGENCY_MEDIAREP_EVENT_PREMIUM_CAP
```

Canonical effect: C26 scoring should add a positive gate for actual OP bridge and a negative guard for revenue-only or event-only stories.

## 19. Before / After Backtest Comparison

| profile_id | profile_hypothesis | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | score_return_alignment_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0_e2r_2_1_stock_web_calibrated_proxy | current profile without C26 fine gate | 8 | 33.5115 | -24.768 | 36.1205 | -29.5203 | 0.625 | 2 | 2 | mixed_current_profile_alignment |
| P0b_e2r_2_0_baseline_reference | older broad platform/ad beta profile | 8 | 33.5115 | -24.768 | 36.1205 | -29.5203 | 0.75 | 2 | 2 | mixed_current_profile_alignment |
| P1_sector_specific_candidate_profile | L8 rule requiring durable monetization and OP bridge | 8 | 33.5115 | -24.768 | 36.1205 | -29.5203 | 0.5 | 0 | 1 | improves_C26_split |
| P2_canonical_archetype_candidate_profile | C26 owned-platform/ad-agency split gate | 8 | 33.5115 | -24.768 | 36.1205 | -29.5203 | 0.375 | 0 | 1 | improves_C26_split |
| P3_counterexample_guard_profile | harder cap for agency/event/AI rename stories lacking margin bridge | 8 | 33.5115 | -24.768 | 36.1205 | -29.5203 | 0.25 | 0 | 1 | improves_C26_split |

## 20. Score-Return Alignment Matrix

| alignment bucket | symbols | lesson |
|---|---|---|
| positive with durable margin bridge | 216050, 237820, 273060 | Allow Yellow, but require 4B watch after sharp repricing. |
| agency/media-rep revenue without durable bridge | 030000, 123570 | Stage2 cap; do not extrapolate revenue to owned-platform leverage. |
| platform MAU/topline but profitability gap | 236810, 363260 | Stage2 may open, but local 4B watch should block Yellow. |
| portal/AI rename event cap | 239340 | Treat as event-premium/4B watch, not C26 Green. |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L8_PLATFORM_CONTENT_SW_SECURITY | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | mixed_C26_digital_ad_rep_owned_platform_operating_leverage_quality_holdout | 3 | 5 | 6 | 0 | 8 | 0 | 8 | 8 | 7 | L8_C26_PLATFORM_AD_OPERATING_LEVERAGE_REQUIRES_DURABLE_MONETIZATION_AND_MARGIN_BRIDGE_WITH_AGENCY_EVENT_4B_CAP | C26_DURABLE_AD_MONETIZATION_OP_BRIDGE_GATE_WITH_AGENCY_MEDIAREP_EVENT_PREMIUM_CAP | C26 static 106 rows; this session adds holdout quality rows only, not a coverage-gap fill claim |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 8
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 8
new_canonical_archetype_count: 0
new_fine_archetype_count: 8
new_trigger_family_count: 8
tested_existing_calibrated_axes:
  - stage2_required_bridge
  - local_4b_watch_guard
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - agency_or_mediarep_ad_recovery_false_positive
  - owned_platform_operating_leverage_missed_or_late
  - event_or_AI_rename_premium_high_MAE
  - profitability_gap_after_topline_growth
new_axis_proposed: C26_DURABLE_AD_MONETIZATION_OP_BRIDGE_GATE_WITH_AGENCY_MEDIAREP_EVENT_PREMIUM_CAP
existing_axis_strengthened:
  - stage2_required_bridge
  - local_4b_watch_guard
existing_axis_weakened: null
existing_axis_kept:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
sector_specific_rule_candidate: L8_C26_PLATFORM_AD_OPERATING_LEVERAGE_REQUIRES_DURABLE_MONETIZATION_AND_MARGIN_BRIDGE_WITH_AGENCY_EVENT_4B_CAP
canonical_archetype_rule_candidate: C26_DURABLE_AD_MONETIZATION_OP_BRIDGE_GATE_WITH_AGENCY_MEDIAREP_EVENT_PREMIUM_CAP
no_new_signal_reason: null
loop_contribution_label: holdout_validation_passed
do_not_propose_new_weight_delta: false
```

This loop adds 8 new independent cases, 5 counterexamples, and 7 residual errors for L8_PLATFORM_CONTENT_SW_SECURITY/C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE.

## 23. Validation Scope / Non-Validation Scope

```yaml
validated:
  - selected canonical/round/sector consistency
  - stock-web entry row availability
  - 180D forward tradable windows
  - 30D/90D/180D MFE and MAE fields
  - corporate-action candidate overlap screen
  - positive/counterexample balance
not_validated:
  - production scoring patch
  - live watchlist
  - investment recommendation
  - brokerage execution
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C26_durable_ad_monetization_op_bridge_gate,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,1,+1,"promote only when durable monetization and OP bridge appear","reduced false-positive agency/event rows while retaining positive operating leverage rows","C26_L101_TRG_01_030000_2024-04-26|C26_L101_TRG_02_216050_2025-01-23|C26_L101_TRG_03_237820_2023-11-06|C26_L101_TRG_04_123570_2024-06-28|C26_L101_TRG_05_236810_2024-05-14|C26_L101_TRG_06_363260_2024-06-24|C26_L101_TRG_07_273060_2025-05-16|C26_L101_TRG_08_239340_2024-04-01",8,8,5,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C26_agency_mediarep_event_premium_cap,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,1,+1,"cap revenue-only agency/media-rep/portal/event stories at Stage2 or local 4B","improves MAE control for 030000/123570/236810/363260/239340","C26_L101_TRG_01_030000_2024-04-26|C26_L101_TRG_04_123570_2024-06-28|C26_L101_TRG_05_236810_2024-05-14|C26_L101_TRG_06_363260_2024-06-24|C26_L101_TRG_08_239340_2024-04-01",5,5,5,medium,canonical_shadow_only,"not production; guardrail candidate"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C26_L101_CASE_01_030000","symbol":"030000","company_name":"제일기획","round":"R8","loop":"101","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"mixed_C26_digital_ad_rep_owned_platform_operating_leverage_quality_holdout","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"agency_digital_btl_defense_low_mfe_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"2024년 1분기 실적은 전년 대비 영업이익 소폭 증가와 디지털/BTL 중심 방어를 보였지만, agency gross-profit mix가 owned-platform ad leverage로 전환된 근거는 약했다."}
{"row_type":"case","case_id":"C26_L101_CASE_02_216050","symbol":"216050","company_name":"인크로스","round":"R8","loop":"101","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"mixed_C26_digital_ad_rep_owned_platform_operating_leverage_quality_holdout","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage3-Yellow","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"ad_business_recovery_with_oneoff_cost_yellow_positive","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"2024년 4분기 광고사업 호조와 top-line 확대에 따른 레버리지 효과가 있었지만 일회성 비용도 같이 확인되어 Green보다는 Yellow/4B watch가 맞았다."}
{"row_type":"case","case_id":"C26_L101_CASE_03_237820","symbol":"237820","company_name":"플레이디","round":"R8","loop":"101","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"mixed_C26_digital_ad_rep_owned_platform_operating_leverage_quality_holdout","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"Stage3-Yellow","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"performance_marketing_forecast_large_mfe_with_4b_overlay","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"2024년 광고시장 회복, KT그룹향 캡티브 광고, 비용 절감과 영업레버리지 전망이 붙어 90D MFE가 크게 열렸지만 이후 drawdown이 커 4B overlay가 필요했다."}
{"row_type":"case","case_id":"C26_L101_CASE_04_123570","symbol":"123570","company_name":"이엠넷","round":"R8","loop":"101","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"mixed_C26_digital_ad_rep_owned_platform_operating_leverage_quality_holdout","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"naver_ad_agency_revenue_increase_high_mae_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"2024년 1분기 네이버 광고대행 매출 증가와 디지털 광고 전문성은 Stage2 근거지만, channel/retention/margin bridge가 약해 MAE가 깊어졌다."}
{"row_type":"case","case_id":"C26_L101_CASE_05_236810","symbol":"236810","company_name":"엔비티","round":"R8","loop":"101","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"mixed_C26_digital_ad_rep_owned_platform_operating_leverage_quality_holdout","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"offerwall_mau_platform_profitability_gap_high_mae_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"애디슨 오퍼월의 점유율/MAU/네이버웹툰 도입 근거는 플랫폼 monetization의 Stage2 근거였지만, 수익성·영업손실 guard가 없으면 180D MAE가 크게 열렸다."}
{"row_type":"case","case_id":"C26_L101_CASE_06_363260","symbol":"363260","company_name":"모비데이즈","round":"R8","loop":"101","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"mixed_C26_digital_ad_rep_owned_platform_operating_leverage_quality_holdout","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"mobile_marketing_growth_with_investment_cost_drag_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"2024년 1분기 매출은 YoY +72.4%였지만 신사업 투자로 영업손실을 기록했고, TikTok/K-pop platform optionality는 C26 Stage3보다 4B watch가 맞았다."}
{"row_type":"case","case_id":"C26_L101_CASE_07_273060","symbol":"273060","company_name":"와이즈버즈","round":"R8","loop":"101","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"mixed_C26_digital_ad_rep_owned_platform_operating_leverage_quality_holdout","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage3-Yellow","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"record_quarter_turnaround_operating_leverage_positive_with_4b","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"2025년 1분기 매출 +111.7%, 영업이익 흑자전환/개선이 확인되어 C26 operating leverage positive였지만, 180D MAE가 -20%를 넘어 local 4B watch가 필요했다."}
{"row_type":"case","case_id":"C26_L101_CASE_08_239340","symbol":"239340","company_name":"이스트에이드","round":"R8","loop":"101","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"mixed_C26_digital_ad_rep_owned_platform_operating_leverage_quality_holdout","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"portal_ad_decline_ai_rename_event_cap_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"줌인터넷/이스트에이드의 광고사업 매출 감소와 사명변경·AI 포털 optionality가 같이 있었지만, 광고 revenue operating leverage로 보기는 어려워 Stage2 false-positive였다."}
{"row_type":"trigger","trigger_id":"C26_L101_TRG_01_030000_2024-04-26","case_id":"C26_L101_CASE_01_030000","symbol":"030000","company_name":"제일기획","round":"R8","loop":"101","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"mixed_C26_digital_ad_rep_owned_platform_operating_leverage_quality_holdout","sector":"platform_content_sw_security","primary_archetype":"platform_ad_revenue_operating_leverage","loop_objective":"holdout_validation|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-26","evidence_available_at_that_date":"2024년 1분기 실적은 전년 대비 영업이익 소폭 증가와 디지털/BTL 중심 방어를 보였지만, agency gross-profit mix가 owned-platform ad leverage로 전환된 근거는 약했다.","evidence_source":"https://buffettlab.co.kr/news/view.php?idx=47053","stage2_evidence_fields":["public_event_or_disclosure","early_revision_signal","relative_strength"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/030/030000/2024.csv+atlas/ohlcv_tradable_by_symbol_year/030/030000/2025.csv","profile_path":"atlas/symbol_profiles/030/030000.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-26","entry_price":18750.0,"MFE_30D_pct":4.3733,"MFE_90D_pct":4.3733,"MFE_180D_pct":4.3733,"MFE_1Y_pct":4.3733,"MFE_2Y_pct":null,"MAE_30D_pct":-2.3467,"MAE_90D_pct":-12.5333,"MAE_180D_pct":-12.5333,"MAE_1Y_pct":-12.5333,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-10","peak_price":19570.0,"drawdown_after_peak_pct":-16.1983,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"agency_digital_btl_defense_low_mfe_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE:030000:2024-04-26:18750.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C26_L101_TRG_02_216050_2025-01-23","case_id":"C26_L101_CASE_02_216050","symbol":"216050","company_name":"인크로스","round":"R8","loop":"101","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"mixed_C26_digital_ad_rep_owned_platform_operating_leverage_quality_holdout","sector":"platform_content_sw_security","primary_archetype":"platform_ad_revenue_operating_leverage","loop_objective":"holdout_validation|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage3-Yellow","trigger_date":"2025-01-22","evidence_available_at_that_date":"2024년 4분기 광고사업 호조와 top-line 확대에 따른 레버리지 효과가 있었지만 일회성 비용도 같이 확인되어 Green보다는 Yellow/4B watch가 맞았다.","evidence_source":"https://www.incross.com/ko/investment/ir.asp?idx=10203&mode=view&page=1&pageSize=10&searchStr=&serboardsort=","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","early_revision_signal"],"stage3_evidence_fields":["financial_visibility","margin_bridge","multiple_public_sources"],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/216/216050/2025.csv","profile_path":"atlas/symbol_profiles/216/216050.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-01-23","entry_price":7340.0,"MFE_30D_pct":5.7221,"MFE_90D_pct":13.079,"MFE_180D_pct":28.2016,"MFE_1Y_pct":28.2016,"MFE_2Y_pct":null,"MAE_30D_pct":-6.812,"MAE_90D_pct":-16.0763,"MAE_180D_pct":-16.0763,"MAE_1Y_pct":-16.0763,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-06-24","peak_price":9410.0,"drawdown_after_peak_pct":-27.2051,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"ad_business_recovery_with_oneoff_cost_yellow_positive","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE:216050:2025-01-23:7340.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C26_L101_TRG_03_237820_2023-11-06","case_id":"C26_L101_CASE_03_237820","symbol":"237820","company_name":"플레이디","round":"R8","loop":"101","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"mixed_C26_digital_ad_rep_owned_platform_operating_leverage_quality_holdout","sector":"platform_content_sw_security","primary_archetype":"platform_ad_revenue_operating_leverage","loop_objective":"holdout_validation|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage3-Yellow","trigger_date":"2023-11-03","evidence_available_at_that_date":"2024년 광고시장 회복, KT그룹향 캡티브 광고, 비용 절감과 영업레버리지 전망이 붙어 90D MFE가 크게 열렸지만 이후 drawdown이 커 4B overlay가 필요했다.","evidence_source":"https://ssl.pstatic.net/imgstock/upload/research/company/1698966461488.pdf","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/237/237820/2023.csv+atlas/ohlcv_tradable_by_symbol_year/237/237820/2024.csv","profile_path":"atlas/symbol_profiles/237/237820.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-11-06","entry_price":4360.0,"MFE_30D_pct":27.2936,"MFE_90D_pct":144.4954,"MFE_180D_pct":144.4954,"MFE_1Y_pct":144.4954,"MFE_2Y_pct":null,"MAE_30D_pct":-6.3073,"MAE_90D_pct":-6.3073,"MAE_180D_pct":-6.3073,"MAE_1Y_pct":-6.3073,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-06","peak_price":10660.0,"drawdown_after_peak_pct":-50.1876,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4b_watch","four_b_evidence_type":["valuation_blowoff","price_only_local_peak","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"performance_marketing_forecast_large_mfe_with_4b_overlay","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE:237820:2023-11-06:4360.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C26_L101_TRG_04_123570_2024-06-28","case_id":"C26_L101_CASE_04_123570","symbol":"123570","company_name":"이엠넷","round":"R8","loop":"101","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"mixed_C26_digital_ad_rep_owned_platform_operating_leverage_quality_holdout","sector":"platform_content_sw_security","primary_archetype":"platform_ad_revenue_operating_leverage","loop_objective":"holdout_validation|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-06-28","evidence_available_at_that_date":"2024년 1분기 네이버 광고대행 매출 증가와 디지털 광고 전문성은 Stage2 근거지만, channel/retention/margin bridge가 약해 MAE가 깊어졌다.","evidence_source":"https://stock.pstatic.net/stock-research/company/72/20240628_company_482347000.pdf","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","early_revision_signal"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/123/123570/2024.csv+atlas/ohlcv_tradable_by_symbol_year/123/123570/2025.csv","profile_path":"atlas/symbol_profiles/123/123570.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-28","entry_price":2980.0,"MFE_30D_pct":20.8054,"MFE_90D_pct":20.8054,"MFE_180D_pct":20.8054,"MFE_1Y_pct":20.8054,"MFE_2Y_pct":null,"MAE_30D_pct":-22.8188,"MAE_90D_pct":-22.8188,"MAE_180D_pct":-28.5235,"MAE_1Y_pct":-28.5235,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-30","peak_price":3600.0,"drawdown_after_peak_pct":-40.8333,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4b_watch","four_b_evidence_type":["margin_or_backlog_slowdown","price_only_local_peak"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"naver_ad_agency_revenue_increase_high_mae_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE:123570:2024-06-28:2980.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C26_L101_TRG_05_236810_2024-05-14","case_id":"C26_L101_CASE_05_236810","symbol":"236810","company_name":"엔비티","round":"R8","loop":"101","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"mixed_C26_digital_ad_rep_owned_platform_operating_leverage_quality_holdout","sector":"platform_content_sw_security","primary_archetype":"platform_ad_revenue_operating_leverage","loop_objective":"holdout_validation|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-14","evidence_available_at_that_date":"애디슨 오퍼월의 점유율/MAU/네이버웹툰 도입 근거는 플랫폼 monetization의 Stage2 근거였지만, 수익성·영업손실 guard가 없으면 180D MAE가 크게 열렸다.","evidence_source":"https://file.alphasquare.co.kr/media/pdfs/company-ir/20240514%EC%97%94%EB%B9%84%ED%8B%B0_%ED%9A%8C%EC%82%AC_%EC%86%8C%EA%B0%9C_%EB%B0%8F_%EC%A3%BC%EC%9A%94_%EC%82%AC%EC%97%85%ED%98%84%ED%99%A9.pdf","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/236/236810/2024.csv+atlas/ohlcv_tradable_by_symbol_year/236/236810/2025.csv","profile_path":"atlas/symbol_profiles/236/236810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-14","entry_price":6260.0,"MFE_30D_pct":25.3994,"MFE_90D_pct":25.3994,"MFE_180D_pct":25.3994,"MFE_1Y_pct":25.3994,"MFE_2Y_pct":null,"MAE_30D_pct":-16.1342,"MAE_90D_pct":-48.4824,"MAE_180D_pct":-54.8722,"MAE_1Y_pct":-55.9105,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-03","peak_price":7850.0,"drawdown_after_peak_pct":-64.0127,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4b_watch","four_b_evidence_type":["margin_or_backlog_slowdown","positioning_overheat","price_only_local_peak"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"offerwall_mau_platform_profitability_gap_high_mae_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE:236810:2024-05-14:6260.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C26_L101_TRG_06_363260_2024-06-24","case_id":"C26_L101_CASE_06_363260","symbol":"363260","company_name":"모비데이즈","round":"R8","loop":"101","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"mixed_C26_digital_ad_rep_owned_platform_operating_leverage_quality_holdout","sector":"platform_content_sw_security","primary_archetype":"platform_ad_revenue_operating_leverage","loop_objective":"holdout_validation|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-06-21","evidence_available_at_that_date":"2024년 1분기 매출은 YoY +72.4%였지만 신사업 투자로 영업손실을 기록했고, TikTok/K-pop platform optionality는 C26 Stage3보다 4B watch가 맞았다.","evidence_source":"https://www.hanaw.com/download/research/FileServer/WEB/info/small_cap/2024/06/21/240624_mobidays.pdf","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","early_revision_signal"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/363/363260/2024.csv+atlas/ohlcv_tradable_by_symbol_year/363/363260/2025.csv","profile_path":"atlas/symbol_profiles/363/363260.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-24","entry_price":2310.0,"MFE_30D_pct":21.2121,"MFE_90D_pct":29.2208,"MFE_180D_pct":29.2208,"MFE_1Y_pct":29.2208,"MFE_2Y_pct":null,"MAE_30D_pct":-17.7922,"MAE_90D_pct":-32.7273,"MAE_180D_pct":-39.2208,"MAE_1Y_pct":-39.2208,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-23","peak_price":2985.0,"drawdown_after_peak_pct":-52.9648,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4b_watch","four_b_evidence_type":["margin_or_backlog_slowdown","positioning_overheat","price_only_local_peak"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"mobile_marketing_growth_with_investment_cost_drag_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE:363260:2024-06-24:2310.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C26_L101_TRG_07_273060_2025-05-16","case_id":"C26_L101_CASE_07_273060","symbol":"273060","company_name":"와이즈버즈","round":"R8","loop":"101","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"mixed_C26_digital_ad_rep_owned_platform_operating_leverage_quality_holdout","sector":"platform_content_sw_security","primary_archetype":"platform_ad_revenue_operating_leverage","loop_objective":"holdout_validation|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage3-Yellow","trigger_date":"2025-05-15","evidence_available_at_that_date":"2025년 1분기 매출 +111.7%, 영업이익 흑자전환/개선이 확인되어 C26 operating leverage positive였지만, 180D MAE가 -20%를 넘어 local 4B watch가 필요했다.","evidence_source":"https://www.hankyung.com/article/202505155071O","stage2_evidence_fields":["public_event_or_disclosure","early_revision_signal","relative_strength"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility"],"stage4b_evidence_fields":["positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/273/273060/2025.csv+atlas/ohlcv_tradable_by_symbol_year/273/273060/2026.csv","profile_path":"atlas/symbol_profiles/273/273060.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-05-16","entry_price":1061.0,"MFE_30D_pct":9.9906,"MFE_90D_pct":30.066,"MFE_180D_pct":35.8153,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-8.1056,"MAE_90D_pct":-8.1056,"MAE_180D_pct":-24.5994,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2026-01-30","peak_price":1441.0,"drawdown_after_peak_pct":-19.5003,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4b_watch","four_b_evidence_type":["positioning_overheat","price_only_local_peak"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"record_quarter_turnaround_operating_leverage_positive_with_4b","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE:273060:2025-05-16:1061.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C26_L101_TRG_08_239340_2024-04-01","case_id":"C26_L101_CASE_08_239340","symbol":"239340","company_name":"이스트에이드","round":"R8","loop":"101","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"mixed_C26_digital_ad_rep_owned_platform_operating_leverage_quality_holdout","sector":"platform_content_sw_security","primary_archetype":"platform_ad_revenue_operating_leverage","loop_objective":"holdout_validation|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-01","evidence_available_at_that_date":"줌인터넷/이스트에이드의 광고사업 매출 감소와 사명변경·AI 포털 optionality가 같이 있었지만, 광고 revenue operating leverage로 보기는 어려워 Stage2 false-positive였다.","evidence_source":"https://www.ddaily.co.kr/page/view/2024033118081470309","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["explicit_event_cap","margin_or_backlog_slowdown","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/239/239340/2024.csv","profile_path":"atlas/symbol_profiles/239/239340.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-01","entry_price":3065.0,"MFE_30D_pct":0.6525,"MFE_90D_pct":0.6525,"MFE_180D_pct":0.6525,"MFE_1Y_pct":23.8173,"MFE_2Y_pct":null,"MAE_30D_pct":-12.5612,"MAE_90D_pct":-51.093,"MAE_180D_pct":-54.0294,"MAE_1Y_pct":-58.2382,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-01","peak_price":3085.0,"drawdown_after_peak_pct":-54.3274,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4b_watch","four_b_evidence_type":["explicit_event_cap","margin_or_backlog_slowdown","price_only_local_peak"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"portal_ad_decline_ai_rename_event_cap_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE:239340:2024-04-01:3065.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C26_L101_CASE_01_030000","trigger_id":"C26_L101_TRG_01_030000_2024-04-26","symbol":"030000","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":2,"customer_quality_score":3,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":3,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_before":23.25,"stage_label_before":"Stage1","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":2,"customer_quality_score":3,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_after":20.5,"stage_label_after":"Stage1","changed_components":["margin_bridge_score","customer_quality_score","execution_risk_score"],"component_delta_explanation":"C26 shadow gate rewards owned/customer-quality ad operating leverage and penalizes agency/portal/event stories lacking durable revenue and margin bridge.","MFE_90D_pct":4.3733,"MAE_90D_pct":-12.5333,"score_return_alignment_label":"agency_digital_btl_defense_low_mfe_counterexample","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C26_L101_CASE_02_216050","trigger_id":"C26_L101_TRG_02_216050_2025-01-23","symbol":"216050","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":2,"margin_bridge_score":7,"revision_score":6,"relative_strength_score":2,"customer_quality_score":6,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":3,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_before":33.25,"stage_label_before":"Stage1","raw_component_scores_after":{"contract_score":3,"backlog_visibility_score":2,"margin_bridge_score":8,"revision_score":6,"relative_strength_score":2,"customer_quality_score":7,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":2,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_after":36.0,"stage_label_after":"Stage1","changed_components":["margin_bridge_score","customer_quality_score","execution_risk_score"],"component_delta_explanation":"C26 shadow gate rewards owned/customer-quality ad operating leverage and penalizes agency/portal/event stories lacking durable revenue and margin bridge.","MFE_90D_pct":13.079,"MAE_90D_pct":-16.0763,"score_return_alignment_label":"ad_business_recovery_with_oneoff_cost_yellow_positive","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C26_L101_CASE_03_237820","trigger_id":"C26_L101_TRG_03_237820_2023-11-06","symbol":"237820","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":2,"margin_bridge_score":7,"revision_score":6,"relative_strength_score":6,"customer_quality_score":6,"policy_or_regulatory_score":1,"valuation_repricing_score":6,"execution_risk_score":3,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_before":41.25,"stage_label_before":"Stage1","raw_component_scores_after":{"contract_score":3,"backlog_visibility_score":2,"margin_bridge_score":8,"revision_score":6,"relative_strength_score":6,"customer_quality_score":7,"policy_or_regulatory_score":1,"valuation_repricing_score":6,"execution_risk_score":2,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_after":44.0,"stage_label_after":"Stage1","changed_components":["margin_bridge_score","customer_quality_score","execution_risk_score"],"component_delta_explanation":"C26 shadow gate rewards owned/customer-quality ad operating leverage and penalizes agency/portal/event stories lacking durable revenue and margin bridge.","MFE_90D_pct":144.4954,"MAE_90D_pct":-6.3073,"score_return_alignment_label":"performance_marketing_forecast_large_mfe_with_4b_overlay","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C26_L101_CASE_04_123570","trigger_id":"C26_L101_TRG_04_123570_2024-06-28","symbol":"123570","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":6,"customer_quality_score":3,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":7,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_before":22.25,"stage_label_before":"Stage1","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":6,"customer_quality_score":3,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":8,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_after":19.5,"stage_label_after":"Stage1","changed_components":["margin_bridge_score","customer_quality_score","execution_risk_score"],"component_delta_explanation":"C26 shadow gate rewards owned/customer-quality ad operating leverage and penalizes agency/portal/event stories lacking durable revenue and margin bridge.","MFE_90D_pct":20.8054,"MAE_90D_pct":-22.8188,"score_return_alignment_label":"naver_ad_agency_revenue_increase_high_mae_counterexample","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C26_L101_CASE_05_236810","trigger_id":"C26_L101_TRG_05_236810_2024-05-14","symbol":"236810","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":6,"customer_quality_score":3,"policy_or_regulatory_score":1,"valuation_repricing_score":6,"execution_risk_score":7,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_before":26.25,"stage_label_before":"Stage1","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":6,"customer_quality_score":3,"policy_or_regulatory_score":1,"valuation_repricing_score":6,"execution_risk_score":8,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_after":23.5,"stage_label_after":"Stage1","changed_components":["margin_bridge_score","customer_quality_score","execution_risk_score"],"component_delta_explanation":"C26 shadow gate rewards owned/customer-quality ad operating leverage and penalizes agency/portal/event stories lacking durable revenue and margin bridge.","MFE_90D_pct":25.3994,"MAE_90D_pct":-48.4824,"score_return_alignment_label":"offerwall_mau_platform_profitability_gap_high_mae_counterexample","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C26_L101_CASE_06_363260","trigger_id":"C26_L101_TRG_06_363260_2024-06-24","symbol":"363260","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":6,"customer_quality_score":3,"policy_or_regulatory_score":3,"valuation_repricing_score":6,"execution_risk_score":7,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_before":28.25,"stage_label_before":"Stage1","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":6,"customer_quality_score":3,"policy_or_regulatory_score":3,"valuation_repricing_score":6,"execution_risk_score":8,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_after":25.5,"stage_label_after":"Stage1","changed_components":["margin_bridge_score","customer_quality_score","execution_risk_score"],"component_delta_explanation":"C26 shadow gate rewards owned/customer-quality ad operating leverage and penalizes agency/portal/event stories lacking durable revenue and margin bridge.","MFE_90D_pct":29.2208,"MAE_90D_pct":-32.7273,"score_return_alignment_label":"mobile_marketing_growth_with_investment_cost_drag_counterexample","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C26_L101_CASE_07_273060","trigger_id":"C26_L101_TRG_07_273060_2025-05-16","symbol":"273060","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":2,"margin_bridge_score":7,"revision_score":6,"relative_strength_score":6,"customer_quality_score":6,"policy_or_regulatory_score":1,"valuation_repricing_score":6,"execution_risk_score":7,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_before":38.25,"stage_label_before":"Stage1","raw_component_scores_after":{"contract_score":3,"backlog_visibility_score":2,"margin_bridge_score":8,"revision_score":6,"relative_strength_score":6,"customer_quality_score":7,"policy_or_regulatory_score":1,"valuation_repricing_score":6,"execution_risk_score":7,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_after":40.25,"stage_label_after":"Stage1","changed_components":["margin_bridge_score","customer_quality_score","execution_risk_score"],"component_delta_explanation":"C26 shadow gate rewards owned/customer-quality ad operating leverage and penalizes agency/portal/event stories lacking durable revenue and margin bridge.","MFE_90D_pct":30.066,"MAE_90D_pct":-8.1056,"score_return_alignment_label":"record_quarter_turnaround_operating_leverage_positive_with_4b","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C26_L101_CASE_08_239340","trigger_id":"C26_L101_TRG_08_239340_2024-04-01","symbol":"239340","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":2,"customer_quality_score":3,"policy_or_regulatory_score":3,"valuation_repricing_score":2,"execution_risk_score":7,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_before":20.25,"stage_label_before":"Stage1","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":2,"customer_quality_score":3,"policy_or_regulatory_score":3,"valuation_repricing_score":2,"execution_risk_score":8,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_after":17.5,"stage_label_after":"Stage1","changed_components":["margin_bridge_score","customer_quality_score","execution_risk_score"],"component_delta_explanation":"C26 shadow gate rewards owned/customer-quality ad operating leverage and penalizes agency/portal/event stories lacking durable revenue and margin bridge.","MFE_90D_pct":0.6525,"MAE_90D_pct":-51.093,"score_return_alignment_label":"portal_ad_decline_ai_rename_event_cap_counterexample","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R8","loop":"101","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","new_independent_case_count":8,"reused_case_count":0,"new_symbol_count":8,"new_trigger_family_count":8,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["agency_or_mediarep_ad_recovery_false_positive","owned_platform_operating_leverage_missed_or_late","event_or_AI_rename_premium_high_MAE","profitability_gap_after_topline_growth"],"loop_contribution_label":"holdout_validation_passed","do_not_propose_new_weight_delta":false}
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
completed_loop: 101
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 2 / quality holdout after session-adjusted Priority 0-1 fills
next_recommended_archetypes:
  - C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_holdout_only_if_new_owned_platform_or_margin_bridge
  - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_holdout_quality_only
  - C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_quality_holdout
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
```

## 28. Source Notes

- Main execution prompt source: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- No-repeat index source: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
- Stock-Web manifest: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
- Stock-Web schema: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/schema.json
- Evidence URLs are listed in Section 9 and repeated inside each JSONL trigger row.

## Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 8
calibration_usable_trigger_count: 8
representative_trigger_count: 8
new_weight_evidence_candidate_count: 8
guardrail_candidate_count: 6
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
future_data_leakage_detected: false
corporate_action_contaminated_rows: 0
insufficient_forward_window_rows: 0
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
ready_for_batch_ingest: true
```
