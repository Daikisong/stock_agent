# E2R Stock-Web Historical Calibration / Backtest Optimization Round

## 0. Research Metadata

```text
research_session = historical_calibration_after_stock_web_ohlc_breakthrough
round = R8
loop = 1
sector = 플랫폼·콘텐츠·SW·보안
output_format = one_standalone_markdown_file
price_source = Songdaiki/stock-web
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
validation_scope_required = true
component_breakdown_required = true
aggregate_deduplication_required = true
```

## 1. Round Scope

이번 R8 Loop 1은 플랫폼·콘텐츠·소프트웨어·보안 영역에서 세 가지 구조를 검증했다.

1. `GAME_LIVE_SERVICE_RERATING`: 게임 live-service 수익성이 가격에 재반영되는 구조.
2. `ENTERPRISE_AI_SAAS_RERATING`: ERP/그룹웨어/클라우드/AI 기능이 기업용 SW valuation을 다시 여는 구조.
3. `SECURITY_POLITICAL_EVENT_PREMIUM`: 보안 기업이지만 실제 주가 움직임은 정치/이벤트 premium인 반례.

핵심 결론은 단순하다. R8에서는 **Stage3-Green이 안전하다는 이유로 너무 늦게 뜨면 이미 리레이팅의 절반 이상을 놓칠 수 있다.** 다만 price-only relative strength만으로 Stage2-Actionable을 열면 AhnLab 같은 정치 이벤트 premium이 섞인다. 그래서 `early_evidence_plus`는 필요하지만, 반드시 `business_component_guardrail`이 같이 붙어야 한다.

## 2. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| source_name | FinanceData/marcap |
| source_repo_url | https://github.com/FinanceData/marcap |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14354401 |
| raw_row_count | 15214118 |
| symbol_count | 5414 |
| active_like_symbol_count | 2868 |
| inactive_or_delisted_like_symbol_count | 2546 |
| markets | KONEX|KOSDAQ|KOSDAQ GLOBAL|KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

## 3. Historical Eligibility Gate

| rule | result |
|---|---|
| historical trigger only | pass |
| current/live candidate discovery | not used |
| entry row exists in tradable shard | pass for all usable triggers |
| forward 180 trading days available | pass |
| 180D corporate-action contamination | pass |
| MFE/MAE 30D/90D/180D computed | pass |
| raw shard used for calibration | no |

## 4. Canonical Archetypes Tested

| archetype | tested cases | verdict |
|---|---:|---|
| GAME_LIVE_SERVICE_RERATING | 1 | Stage2/Yellow earlier than Green worked better |
| ENTERPRISE_AI_SAAS_RERATING | 1 | Stage2 evidence + RS was the best entry |
| SECURITY_POLITICAL_EVENT_PREMIUM | 1 | must be rejected from structural R8 scoring |

## 5. Case Selection Summary

| case_id | symbol | company_name | case_type | primary_archetype | best_trigger | score_price_alignment | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R8L1_KRF_259960_2024 | 259960 | 크래프톤 | structural_success | GAME_LIVE_SERVICE_RERATING | R8L1_KRF_T1 | Stage2_promote_candidate | Green confirmation was valid but late; Stage2/early-Yellow captured much more upside. |
| R8L1_DZ_012510_2024 | 012510 | 더존비즈온 | missed_structural | ENTERPRISE_AI_SAAS_RERATING | R8L1_DZ_T1 | missed_structural | Stage2 price+AI-enterprise evidence had exceptional MFE/MAE before Green. |
| R8L1_AHN_053800_2022 | 053800 | 안랩 | event_premium_overheat | SECURITY_POLITICAL_EVENT_PREMIUM | none_for_fundamental_entry | price_moved_without_evidence | Large MFE came from political event premium, not security-business rerating; guardrail should reject. |

## 6. Evidence Source Map

| case_id | evidence source class | date discipline | notes |
|---|---|---|---|
| R8L1_KRF_259960_2024 | earnings / IR / financial news / report | trigger date uses public earnings and price confirmation windows | public business evidence supports live-service rerating, but exact filing URL should be revalidated in coding batch |
| R8L1_DZ_012510_2024 | company/financial news/reports around enterprise AI·ERP·cloud | trigger date separated from price result | early AI/SaaS repricing evidence was visible before late Green |
| R8L1_AHN_053800_2022 | election/political event context + OHLC | not a cybersecurity revenue trigger | price moved hard, but structural R8 evidence was missing |

## 7. Price Data Source Map

| symbol | company | profile_path | shard_paths | corporate_action_window_status |
|---|---|---|---|---|
| 259960 | 크래프톤 | atlas/symbol_profiles/259/259960.json | atlas/ohlcv_tradable_by_symbol_year/259/259960/2024.csv; 2025.csv | clean_180D_window |
| 012510 | 더존비즈온 | atlas/symbol_profiles/012/012510.json | atlas/ohlcv_tradable_by_symbol_year/012/012510/2024.csv | clean_180D_window |
| 053800 | 안랩 | atlas/symbol_profiles/053/053800.json | atlas/ohlcv_tradable_by_symbol_year/053/053800/2022.csv | clean_180D_window |

## 8. Case-by-Case Trigger Grid

| trigger_id | case_id | type | trigger_date | entry_date | entry_price | MFE90 | MAE90 | MFE180 | MAE180 | peak | outcome | dedupe | role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R8L1_KRF_T1 | R8L1_KRF_259960_2024 | Stage2 | 2024-02-13 | 2024-02-13 | 230000 | 29.1 | -8.5 | 54.3 | -8.5 | 2025-02-10/390000 | good_entry | True | representative |
| R8L1_KRF_T2 | R8L1_KRF_259960_2024 | Stage2-Actionable | 2024-05-09 | 2024-05-09 | 263500 | 34.7 | -8.9 | 34.7 | -8.9 | 2025-05-07/393000 | excellent_entry | True | representative |
| R8L1_KRF_T4 | R8L1_KRF_259960_2024 | Stage3-Green | 2024-08-13 | 2024-08-13 | 331000 | 7.3 | -12.4 | 17.8 | -12.4 | 2025-05-07/393000 | late_entry | True | representative |
| R8L1_KRF_T5 | R8L1_KRF_259960_2024 | Stage4B | 2024-08-22 | 2024-08-22 | 346000 | 2.3 | -15.6 | 12.7 | -15.6 | 2025-05-07/393000 | event_premium | False | 4B_overlay_only |
| R8L1_DZ_T1 | R8L1_DZ_012510_2024 | Stage2 | 2024-01-18 | 2024-01-18 | 40800 | 55.1 | 0.0 | 91.9 | 0.0 | 2024-07-08/78300 | excellent_entry | True | representative |
| R8L1_DZ_T2 | R8L1_DZ_012510_2024 | Stage2-Actionable | 2024-04-09 | 2024-04-09 | 57800 | 35.5 | -11.8 | 35.5 | -18.7 | 2024-07-08/78300 | good_entry | True | representative |
| R8L1_DZ_T3 | R8L1_DZ_012510_2024 | Stage3-Yellow | 2024-04-30 | 2024-04-30 | 59900 | 30.7 | -15.0 | 30.7 | -21.5 | 2024-07-08/78300 | good_entry | True | representative |
| R8L1_DZ_T4 | R8L1_DZ_012510_2024 | Stage3-Green | 2024-06-26 | 2024-06-26 | 75900 | 3.2 | -38.1 | 3.2 | -38.1 | 2024-07-08/78300 | late_entry | True | representative |
| R8L1_DZ_T5 | R8L1_DZ_012510_2024 | Stage4B | 2024-07-08 | 2024-07-08 | 75300 | 4.0 | -37.6 | 4.0 | -37.6 | 2024-07-08/78300 | event_premium | False | 4B_overlay_only |
| R8L1_AHN_T1 | R8L1_AHN_053800_2022 | Stage2 | 2022-03-03 | 2022-03-03 | 70800 | 208.6 | -5.6 | 208.6 | -16.5 | 2022-03-24/218500 | price_moved_without_evidence | True | representative |
| R8L1_AHN_T2 | R8L1_AHN_053800_2022 | Stage2-Actionable | 2022-03-11 | 2022-03-11 | 86500 | 152.6 | -7.5 | 152.6 | -31.7 | 2022-03-24/218500 | price_moved_without_evidence | True | representative |
| R8L1_AHN_T5 | R8L1_AHN_053800_2022 | Stage4B | 2022-03-23 | 2022-03-23 | 175800 | 24.3 | -53.9 | 24.3 | -66.4 | 2022-03-24/218500 | event_premium | False | 4B_overlay_only |
| R8L1_AHN_T6 | R8L1_AHN_053800_2022 | Stage4C | 2022-03-30 | 2022-03-30 | 122800 | 4.8 | -34.0 | 4.8 | -51.9 | 2022-03-24/218500 | thesis_break | False | 4C_overlay_only |

## 9. Trigger-Level OHLC Backtest Tables

The following table is the same trigger-level backtest grid, optimized for calibration reading.

| trigger_id | entry | MFE30 | MFE90 | MFE180 | MFE1Y | MAE30 | MAE90 | MAE180 | below30 | below90 | green_lateness | 4B local | 4B full |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---:|---:|---:|
| R8L1_KRF_T1 | 230000 | 15.2 | 29.1 | 54.3 | 69.6 | -8.5 | -8.5 | -8.5 | True | True | unavailable | unavailable | unavailable |
| R8L1_KRF_T2 | 263500 | 12.7 | 34.7 | 34.7 | 49.1 | -8.9 | -8.9 | -8.9 | True | True | 0.0 | unavailable | unavailable |
| R8L1_KRF_T4 | 331000 | 7.3 | 7.3 | 17.8 | 18.7 | -9.1 | -12.4 | -12.4 | True | True | 0.8 | unavailable | unavailable |
| R8L1_KRF_T5 | 346000 | 2.3 | 2.3 | 12.7 | 13.6 | -10.4 | -15.6 | -15.6 | True | True | unavailable | 0.9 | 0.8 |
| R8L1_DZ_T1 | 40800 | 38.0 | 55.1 | 91.9 | 91.9 | 0.0 | 0.0 | 0.0 | False | False | unavailable | unavailable | unavailable |
| R8L1_DZ_T2 | 57800 | 9.5 | 35.5 | 35.5 | 35.5 | -11.8 | -11.8 | -18.7 | True | True | 0.5 | unavailable | unavailable |
| R8L1_DZ_T3 | 59900 | 9.5 | 30.7 | 30.7 | 30.7 | -15.0 | -15.0 | -21.5 | True | True | 0.5 | unavailable | unavailable |
| R8L1_DZ_T4 | 75900 | 3.2 | 3.2 | 3.2 | 3.2 | -19.9 | -38.1 | -38.1 | True | True | 0.9 | unavailable | unavailable |
| R8L1_DZ_T5 | 75300 | 4.0 | 4.0 | 4.0 | 4.0 | -35.6 | -37.6 | -37.6 | True | True | unavailable | 0.9 | 0.9 |
| R8L1_AHN_T1 | 70800 | 208.6 | 208.6 | 208.6 | 208.6 | -5.6 | -5.6 | -16.5 | True | True | unavailable | unavailable | unavailable |
| R8L1_AHN_T2 | 86500 | 152.6 | 152.6 | 152.6 | 152.6 | 0.0 | -7.5 | -31.7 | False | True | unavailable | unavailable | unavailable |
| R8L1_AHN_T5 | 175800 | 24.3 | 24.3 | 24.3 | 24.3 | -46.5 | -53.9 | -66.4 | True | True | unavailable | 0.7 | 0.7 |
| R8L1_AHN_T6 | 122800 | 2.3 | 4.8 | 4.8 | 4.8 | -23.5 | -34.0 | -51.9 | True | True | unavailable | unavailable | unavailable |

## 10. 1D Price Path Summaries


### R8L1_KRF_259960_2024 best trigger path: entry 2024-02-13 close 230,000

| point | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---|---:|---:|---:|
| D+1 | 4.1 | 5.7 | -1.5 |
| D+5 | 2.2 | 5.9 | -2.2 |
| D+10 | -2.6 | 5.9 | -5.2 |
| D+20 | -7.4 | 5.9 | -8.5 |
| D+30 | 11.7 | 15.2 | -8.5 |
| D+60 | 8.7 | 15.2 | -8.5 |
| D+90 | 26.1 | 29.1 | -8.5 |
| D+180 | 44.6 | 54.3 | -8.5 |
| D+252 | 62.6 | 69.6 | -8.5 |

### R8L1_DZ_012510_2024 best trigger path: entry 2024-01-18 close 40,800

| point | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---|---:|---:|---:|
| D+1 | 7.5 | 14.7 | 1.8 |
| D+5 | 13.1 | 27.2 | 1.8 |
| D+10 | 20.0 | 29.4 | 1.8 |
| D+20 | 36.8 | 38.0 | 1.8 |
| D+30 | 10.5 | 38.0 | 1.8 |
| D+60 | 31.9 | 50.0 | 1.8 |
| D+90 | 50.7 | 60.5 | 1.8 |
| D+180 | 39.0 | 91.9 | 0.0 |
| D+252 | 56.1 | 91.9 | -1.2 |

### R8L1_AHN_053800_2022 event premium path: entry 2022-03-03 close 70,800

| point | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---|---:|---:|---:|
| D+1 | -2.1 | 8.1 | -3.4 |
| D+5 | 22.2 | 30.1 | -5.6 |
| D+10 | 43.6 | 43.6 | -5.6 |
| D+20 | 73.4 | 208.6 | -5.6 |
| D+30 | 57.8 | 208.6 | -5.6 |
| D+60 | 60.5 | 208.6 | -5.6 |
| D+90 | 14.3 | 208.6 | -5.6 |
| D+180 | -6.4 | 208.6 | -16.5 |
| D+252 | -5.9 | 208.6 | -16.5 |


## 11. Case Trigger Comparison

### 크래프톤

- Best trigger: `R8L1_KRF_T1`, not Green.
- Stage3-Green at 2024-08-13 was directionally correct but late. Its 90D MFE was only 7.3%, while the early Stage2 trigger had 29.1% MFE90 and 54.3% MFE180.
- The live-service earnings thesis is not pure narrative. It had margin/revision/customer-quality components.

### 더존비즈온

- Best trigger: `R8L1_DZ_T1`.
- Early Stage2 at 2024-01-18 had 91.9% MFE180 with almost no adverse excursion before the peak.
- Green candidate at 2024-06-26 was effectively a late-cycle entry: 3.2% MFE90 versus -38.1% MAE90.

### 안랩

- Best structural trigger: none.
- The price path was explosive, but the evidence was political/event premium rather than security revenue, customer, margin, or revision evidence.
- This case is useful precisely because it warns the model not to treat all R8 relative strength as SW/security rerating.

## 12. Stage2 → Stage4 Audit

| case | Stage2 MFE large? | MAE acceptable? | Stage2 better than Green? | evidence reason | classification |
|---|---|---|---|---|---|
| 크래프톤 | yes | yes | yes | earnings + live-service monetization + RS | Stage2_promote_candidate |
| 더존비즈온 | yes | yes | yes | enterprise AI/SaaS repricing + RS | missed_structural |
| 안랩 | yes | price path yes, evidence no | not applicable | political event premium, not business evidence | price_moved_without_evidence |

## 13. Stage3 Yellow / Green Lateness Audit

| case | Stage2-Actionable entry | Stage3-Green entry | peak | green_lateness_ratio | verdict |
|---|---:|---:|---:|---:|---|
| 크래프톤 | 263,500 | 331,000 | 393,000 | 0.78 | Green captured validation but missed large upside |
| 더존비즈온 | 57,800 | 75,900 | 78,300 | 0.91 | Green was near-cycle peak |
| 안랩 | not_applicable | none | 218,500 | not_applicable | no confirmed structural Green |

## 14. 4B Timing Audit

| trigger_id | local proximity | full-window proximity | evidence type | timing verdict |
|---|---:|---:|---|---|
| R8L1_KRF_T5 | 0.92 | 0.77 | price_only | price-only local/full peak watch, not full 4B |
| R8L1_DZ_T5 | 0.94 | 0.94 | price_only | good price timing, but non-price 4B evidence not confirmed |
| R8L1_AHN_T5 | 0.68 | 0.68 | price_only | price-only local 4B too early/nonactionable |

R8에서 4B를 매도 신호처럼 쓰면 noise가 커진다. 이번 라운드에서는 4B를 `watch overlay`로만 인정하고, full 4B 승격에는 valuation blowoff + revision slowdown, dilution/CB, legal block, margin/backlog slowdown 같은 비가격 evidence가 필요하다고 본다.

## 15. 4C Protection Audit

| case | 4C candidate | protection label | verdict |
|---|---|---|---|
| 크래프톤 | none | not_applicable | hard 4C not validated |
| 더존비즈온 | none | not_applicable | hard 4C not validated |
| 안랩 | R8L1_AHN_T6 | hard_4c_late_for_event_unwind | this is event unwind, not normal thesis break |

## 16. Baseline Score Simulation

Baseline proxy is reference-only. It should not be read as the actual production score.

| case | baseline selection | baseline problem |
|---|---|---|
| 크래프톤 | Stage3-Green `R8L1_KRF_T4` | too late; MFE90 only 7.3 |
| 더존비즈온 | Stage3-Green `R8L1_DZ_T4` | very late; MFE90 3.2, MAE90 -38.1 |
| 안랩 | reject if event-premium guardrail exists | correct reject; without guardrail, RS would contaminate the training set |

## 17. Shadow Profile Optimization Loop

row_type,profile_id,case_count,selected_trigger_count,selected_representative_trigger_count,avg_MFE_90D_pct,median_MFE_90D_pct,avg_MAE_90D_pct,median_MAE_90D_pct,avg_MFE_180D_pct,avg_MAE_180D_pct,hit_rate_MFE90_gt_20pct,bad_entry_rate_MAE90_lt_minus_15pct,false_positive_rate,missed_structural_count,late_green_count,avg_green_lateness_ratio,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
profile_comparison,baseline_current_proxy,3,2,2,5.2,5.2,-25.2,-25.2,10.5,-25.2,0.0,50.0,0.0,2,2,0.8,,,reference; safe but late and low upside capture
profile_comparison,stage2_actionable_early_evidence_plus_with_event_premium_guardrail,3,2,2,42.1,42.1,-4.2,-4.2,73.1,-4.2,100.0,0.0,0.0,0,0,,,,"selected; improved MFE and sharply reduced MAE, while rejecting political event premium"
profile_comparison,stage3_yellow_entry_relaxed,3,2,2,35.1,35.1,-10.4,-10.4,35.1,-13.8,100.0,0.0,0.0,0,0,0.8,,,"good backup, but not as early as P1"
profile_comparison,green_confirmation_timing_relaxed,3,2,2,12.6,12.6,-14.5,-14.5,18.4,-18.0,0.0,50.0,0.0,1,1,0.65,,,cautious; still late for R8 fast repricing
profile_comparison,four_b_peak_timing_tuned,3,3,0,10.2,4.0,-35.7,-37.6,13.7,-39.9,33.3,66.7,0.0,0,0,,0.8,0.8,do not treat price-only as full 4B; use overlay watch only
profile_comparison,four_c_thesis_break_earlier,3,1,0,4.8,4.8,-34.0,-34.0,4.8,-51.9,0.0,100.0,0.0,0,0,,,,not validated as hard 4C; event unwind only

## 18. Before / After Backtest Comparison

| case_id | symbol | best_actual_trigger | baseline_selected_trigger | after_selected_trigger | baseline_MFE_90D_pct | after_MFE_90D_pct | baseline_MAE_90D_pct | after_MAE_90D_pct | return_improvement_90D_pct | risk_change_90D_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R8L1_KRF_259960_2024 | 259960 | R8L1_KRF_T1 | R8L1_KRF_T4 | R8L1_KRF_T1 | 7.3 | 29.1 | -12.4 | -8.5 | 21.8 | 3.9 |
| R8L1_DZ_012510_2024 | 012510 | R8L1_DZ_T1 | R8L1_DZ_T4 | R8L1_DZ_T1 | 3.2 | 55.1 | -38.1 | 0.0 | 51.9 | 38.1 |
| R8L1_AHN_053800_2022 | 053800 | none_for_structural_entry | reject | reject | 0 | 0 | 0 | 0 | 0 | 0 |

Natural-language summary: selected profile `stage2_actionable_early_evidence_plus_with_event_premium_guardrail` improves upside capture because it promotes two early R8 business-evidence triggers and rejects AhnLab-style non-business event premium. The mechanism is important: it does **not** simply reward price strength. It requires earnings/customer/margin/revision evidence, then uses relative strength as a throttle rather than as the engine.

## 19. Score-Return Alignment Matrix

| alignment_label | trigger_count | avg_weighted_score_before | avg_weighted_score_after | avg_MFE_90D_pct | avg_MAE_90D_pct | verdict |
|---|---:|---:|---:|---:|---:|---|
| score_mid_return_high_promote_candidate | 5 | 65.0 | 73.6 | 37.9 | -5.6 | promote early validated business evidence |
| score_high_return_low_false_positive | 2 | 85.0 | 85.0 | 5.2 | -25.3 | Green late/poor entry timing |
| score_low_return_high_missed_structural | 2 | 54.5 | 35.0 | 180.6 | -6.5 | not structural; event premium guardrail |
| score_mid_return_low_watch_only | 4 | 58.8 | 44.5 | 7.5 | -31.9 | watch only, no weight increase |

## 20. Weight Sensitivity Table

| axis | baseline_weight_or_threshold | tested_weight_or_threshold | delta | affected_trigger_ids | affected_case_count | avg_MFE_90D_before | avg_MFE_90D_after | avg_MAE_90D_before | avg_MAE_90D_after | false_positive_count_before | false_positive_count_after | missed_structural_count_before | missed_structural_count_after | verdict |
|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| stage2_actionable_validated_earnings_or_customer_evidence | 0 | 2 | +2 | R8L1_KRF_T1; R8L1_DZ_T1 | 2 | 5.2 | 42.1 | -25.2 | -4.3 | 0 | 0 | 2 | 0 | positive adjustment |
| green_confirmation_lateness_penalty_for_fast_repricing_R8 | 0 | -2 | -2 | R8L1_KRF_T4; R8L1_DZ_T4 | 2 | 5.2 | 42.1 | -25.2 | -4.3 | 0 | 0 | 2 | 0 | promote earlier tier |
| political_or_event_premium_without_business_component_guardrail | 0 | -3 | -3 | R8L1_AHN_T1; R8L1_AHN_T2; R8L1_AHN_T5 | 1 | 180.6 | 0.0 | -6.5 | 0.0 | 1 | 0 | 0 | 0 | reject adjustment |

## 21. Optimization Decision Log

```jsonl
{"row_type": "optimization_decision", "decision_id": "R8L1_DEC_01", "hypothesis": "Stage2-Actionable should promote early earnings/customer/AI-SaaS evidence plus relative strength before full Green confirmation.", "tested_trigger_ids": ["R8L1_KRF_T1", "R8L1_DZ_T1"], "baseline_profile": "baseline_current_proxy", "selected_profile": "stage2_actionable_early_evidence_plus_with_event_premium_guardrail", "backtest_result_summary": "Selected representative MFE90 improves from 5.2 to 42.1 and MAE90 improves from -25.2 to -4.3.", "accepted_or_rejected": "accepted", "delta_magnitude": "+2", "why_not_larger_delta": "Only two structural cases in this round; sample size caps delta at +2.", "risks": "Could over-promote AI-product announcements without revenue/customer evidence.", "next_validation_needed": "Validate against more platform/SW false positives in R8 Loop 2."}
{"row_type": "optimization_decision", "decision_id": "R8L1_DEC_02", "hypothesis": "Price-only 4B should not become full 4B without valuation/revision/dilution/legal evidence.", "tested_trigger_ids": ["R8L1_KRF_T5", "R8L1_DZ_T5", "R8L1_AHN_T5"], "baseline_profile": "baseline_current_proxy", "selected_profile": "four_b_peak_timing_tuned", "backtest_result_summary": "Local/full peak proximity can be high, but price-only signals were not sufficient to infer thesis deterioration.", "accepted_or_rejected": "accepted_as_guardrail", "delta_magnitude": "-2 to full-4B promotion", "why_not_larger_delta": "4B evidence remains useful as watch overlay.", "risks": "May miss pure price exhaustion in event bubbles.", "next_validation_needed": "Find R8 cases with valuation blowoff + revision slowdown."}
{"row_type": "optimization_decision", "decision_id": "R8L1_DEC_03", "hypothesis": "Political/event premium must be rejected for structural software/security rerating unless business components validate it.", "tested_trigger_ids": ["R8L1_AHN_T1", "R8L1_AHN_T2", "R8L1_AHN_T6"], "baseline_profile": "baseline_current_proxy", "selected_profile": "stage2_actionable_early_evidence_plus_with_event_premium_guardrail", "backtest_result_summary": "AhnLab shows huge MFE but fails structural score-return alignment; drawdown after peak was about -72.9.", "accepted_or_rejected": "accepted", "delta_magnitude": "-3 guardrail", "why_not_larger_delta": "AhnLab is one clean counterexample but still a single event-premium case.", "risks": "Some policy/security spending events may be real demand shocks; require customer/order evidence.", "next_validation_needed": "Compare with cybersecurity demand-shock case, not political figure linkage."}
```

## 22. Overfitting / Robustness Check

- Usable trigger count: 13.
- Representative entry trigger count: 9.
- Structural business-evidence cases: 2.
- Counterexample/event-premium case: 1.
- Because the true structural case count is only 2, accepted positive deltas are capped at +2.
- AhnLab prevents overfitting to relative strength. It shows that price-path success alone is not enough to promote an R8 trigger.

## 23. Cross-case Aggregate Metrics

```csv
row_type,trigger_type,usable_trigger_count,representative_trigger_count,avg_MFE_90D_pct,median_MFE_90D_pct,avg_MAE_90D_pct,median_MAE_90D_pct,avg_green_lateness_ratio,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
aggregate_metric,Stage2,3,3,97.6,55.1,-4.7,-5.6,unavailable,unavailable,unavailable,representative rows only; duplicate same-entry labels excluded
aggregate_metric,Stage2-Actionable,3,3,74.3,35.5,-9.4,-8.9,0.2,unavailable,unavailable,representative rows only; duplicate same-entry labels excluded
aggregate_metric,Stage3-Green,2,2,5.2,5.2,-25.2,-25.2,0.8,unavailable,unavailable,representative rows only; duplicate same-entry labels excluded
aggregate_metric,Stage3-Yellow,1,1,30.7,30.7,-15.0,-15.0,0.5,unavailable,unavailable,representative rows only; duplicate same-entry labels excluded
```

## 24. Score-Price Alignment Verdict

```text
round_verdict = early_validated_R8_business_evidence_outperformed_late_green
best_shadow_profile = stage2_actionable_early_evidence_plus_with_event_premium_guardrail
primary_adjustment = promote Stage2-Actionable when earnings/customer/margin/revision evidence exists plus relative strength
primary_guardrail = reject price-only/political-event premium for structural software/security rerating
production_scoring_changed = false
shadow_weight_only = true
```

## 25. Validation Scope / Non-Validation Scope

### this_round_validates

- Stage2-Actionable promotion for R8 cases where at least one business component is real: earnings/margin/revision/customer quality plus relative strength.
- Stage3-Green lateness in fast-repricing R8 cases.
- Price-only 4B should remain watch overlay, not full 4B.
- Political/event premium must be rejected when there is no software/security business evidence.

### this_round_does_not_validate

- Broad Stage3-Green relaxation across all platforms.
- Hard 4C protection for genuine software/security thesis breaks.
- Full 4B exit timing with valuation blowoff + revision slowdown.
- Platform MAU/ARPU-specific scoring; this round had no clean platform MAU case.

No weight/gate delta is proposed for items in `this_round_does_not_validate`.

## 26. Shadow Weight Calibration

```csv
row_type,axis,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,notes
shadow_weight,stage2_actionable_validated_earnings_or_customer_evidence,0,2,+2,Krafton and Douzone Stage2/early Actionable entries produced far better MFE90 with lower MAE than late Green.,P0 avg MFE90 5.2 / avg MAE90 -25.2 improved to P1 avg MFE90 42.1 / avg MAE90 -4.3 on selected representative entries.,R8L1_KRF_T1|R8L1_DZ_T1,2,shadow-only; event-premium guardrail required
shadow_weight,green_confirmation_lateness_penalty_for_fast_repricing_R8,0,-2,-2,Krafton Green lateness ratio 0.78 and Douzone 0.91 show Green confirmation often arrived after most upside.,Late Green selected entries MFE90 7.3 and 3.2 versus early entries 29.1 and 55.1.,R8L1_KRF_T4|R8L1_DZ_T4,2,shadow-only; do not relax Green broadly without earnings/customer evidence
shadow_weight,political_or_event_premium_without_business_component_guardrail,0,-3,-3,AhnLab delivered large MFE but from political-event premium rather than security EPS/FCF; without guardrail it would contaminate R8 success calibration.,AhnLab T2 MFE90 152.6 but MAE180 -31.7 and no validated security-business component; proposed profile rejects it.,R8L1_AHN_T1|R8L1_AHN_T2|R8L1_AHN_T5,3,shadow-only; preserves R8 security archetype quality
```

## 27. Machine-Readable Rows

### 27.1 Price source validation row JSONL

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 27.2 Case rows JSONL

```jsonl
{"row_type": "case", "round": "R8", "loop": "1", "sector": "플랫폼·콘텐츠·SW·보안", "calibration_usable": true, "historical_window_status": "180D_available", "price_source": "Songdaiki/stock-web", "case_id": "R8L1_KRF_259960_2024", "symbol": "259960", "company_name": "크래프톤", "case_type": "structural_success", "primary_archetype": "GAME_LIVE_SERVICE_RERATING", "best_trigger": "R8L1_KRF_T1", "score_price_alignment": "Stage2_promote_candidate", "notes": "Green confirmation was valid but late; Stage2/early-Yellow captured much more upside."}
{"row_type": "case", "round": "R8", "loop": "1", "sector": "플랫폼·콘텐츠·SW·보안", "calibration_usable": true, "historical_window_status": "180D_available", "price_source": "Songdaiki/stock-web", "case_id": "R8L1_DZ_012510_2024", "symbol": "012510", "company_name": "더존비즈온", "case_type": "missed_structural", "primary_archetype": "ENTERPRISE_AI_SAAS_RERATING", "best_trigger": "R8L1_DZ_T1", "score_price_alignment": "missed_structural", "notes": "Stage2 price+AI-enterprise evidence had exceptional MFE/MAE before Green."}
{"row_type": "case", "round": "R8", "loop": "1", "sector": "플랫폼·콘텐츠·SW·보안", "calibration_usable": true, "historical_window_status": "180D_available", "price_source": "Songdaiki/stock-web", "case_id": "R8L1_AHN_053800_2022", "symbol": "053800", "company_name": "안랩", "case_type": "event_premium_overheat", "primary_archetype": "SECURITY_POLITICAL_EVENT_PREMIUM", "best_trigger": "none_for_fundamental_entry", "score_price_alignment": "price_moved_without_evidence", "notes": "Large MFE came from political event premium, not security-business rerating; guardrail should reject."}
```

### 27.3 Trigger rows JSONL

```jsonl
{"row_type": "trigger", "trigger_id": "R8L1_KRF_T1", "case_id": "R8L1_KRF_259960_2024", "symbol": "259960", "company_name": "크래프톤", "round": "R8", "loop": "1", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "GAME_LIVE_SERVICE_RERATING", "trigger_type": "Stage2", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "FY2023/Q4 and early-2024 live-service earnings evidence; PUBG/BGMI mobile strength and PC/mobile monetization recovery became public evidence before the later Q2 confirmation.", "evidence_source": "earnings release / IR material / financial news; exact filing should be revalidated in coding handoff", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/259/259960/2024.csv", "profile_path": "atlas/symbol_profiles/259/259960.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-13", "entry_price": 230000, "MFE_30D_pct": 15.2, "MFE_90D_pct": 29.1, "MFE_180D_pct": 54.3, "MFE_1Y_pct": 69.6, "MFE_2Y_pct": null, "MAE_30D_pct": -8.5, "MAE_90D_pct": -8.5, "MAE_180D_pct": -8.5, "MAE_1Y_pct": -8.5, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-02-10", "peak_price": 390000, "drawdown_after_peak_pct": -20.1, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "", "four_b_evidence_type": "", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_entry", "calibration_usable": true, "forward_window_trading_days": 252, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L1_KRF_G1", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R8L1_KRF_T2", "case_id": "R8L1_KRF_259960_2024", "symbol": "259960", "company_name": "크래프톤", "round": "R8", "loop": "1", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "GAME_LIVE_SERVICE_RERATING", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-09", "evidence_available_at_that_date": "Q1/early-year earnings and price relative-strength confirmation; live-service monetization thesis had moved beyond pure theme.", "evidence_source": "earnings / report / financial-news confirmation; source-level revalidation required before coding", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/259/259960/2024.csv", "profile_path": "atlas/symbol_profiles/259/259960.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-09", "entry_price": 263500, "MFE_30D_pct": 12.7, "MFE_90D_pct": 34.7, "MFE_180D_pct": 34.7, "MFE_1Y_pct": 49.1, "MFE_2Y_pct": null, "MAE_30D_pct": -8.9, "MAE_90D_pct": -8.9, "MAE_180D_pct": -8.9, "MAE_1Y_pct": -8.9, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-05-07", "peak_price": 393000, "drawdown_after_peak_pct": -26.1, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": 0.0, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "", "four_b_evidence_type": "", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "excellent_entry", "calibration_usable": true, "forward_window_trading_days": 252, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L1_KRF_G2", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R8L1_KRF_T4", "case_id": "R8L1_KRF_259960_2024", "symbol": "259960", "company_name": "크래프톤", "round": "R8", "loop": "1", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "GAME_LIVE_SERVICE_RERATING", "trigger_type": "Stage3-Green", "trigger_date": "2024-08-13", "evidence_available_at_that_date": "Q2-style public confirmation: revenue/OP path, mobile strength and price breakout had all aligned.", "evidence_source": "earnings / report confirmation", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/259/259960/2024.csv", "profile_path": "atlas/symbol_profiles/259/259960.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-08-13", "entry_price": 331000, "MFE_30D_pct": 7.3, "MFE_90D_pct": 7.3, "MFE_180D_pct": 17.8, "MFE_1Y_pct": 18.7, "MFE_2Y_pct": null, "MAE_30D_pct": -9.1, "MAE_90D_pct": -12.4, "MAE_180D_pct": -12.4, "MAE_1Y_pct": -12.4, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-05-07", "peak_price": 393000, "drawdown_after_peak_pct": -26.1, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": 0.78, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "", "four_b_evidence_type": "", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "late_entry", "calibration_usable": true, "forward_window_trading_days": 252, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L1_KRF_G3", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R8L1_KRF_T5", "case_id": "R8L1_KRF_259960_2024", "symbol": "259960", "company_name": "크래프톤", "round": "R8", "loop": "1", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "GAME_LIVE_SERVICE_RERATING", "trigger_type": "Stage4B", "trigger_date": "2024-08-22", "evidence_available_at_that_date": "Price-only local peak watch after Q2 rally; no clear non-price thesis-break or revision slowdown used for full 4B.", "evidence_source": "price-only OHLC; non-price 4B evidence not confirmed", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/259/259960/2024.csv", "profile_path": "atlas/symbol_profiles/259/259960.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-08-22", "entry_price": 346000, "MFE_30D_pct": 2.3, "MFE_90D_pct": 2.3, "MFE_180D_pct": 12.7, "MFE_1Y_pct": 13.6, "MFE_2Y_pct": null, "MAE_30D_pct": -10.4, "MAE_90D_pct": -15.6, "MAE_180D_pct": -15.6, "MAE_1Y_pct": -15.6, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-05-07", "peak_price": 393000, "drawdown_after_peak_pct": -26.1, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": null, "four_b_local_peak_proximity": 0.92, "four_b_full_window_peak_proximity": 0.77, "four_b_timing_verdict": "price_only_local_4B_not_full_4B", "four_b_evidence_type": "price_only", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "event_premium", "calibration_usable": true, "forward_window_trading_days": 252, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L1_KRF_G4", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only"}
{"row_type": "trigger", "trigger_id": "R8L1_DZ_T1", "case_id": "R8L1_DZ_012510_2024", "symbol": "012510", "company_name": "더존비즈온", "round": "R8", "loop": "1", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "ENTERPRISE_AI_SAAS_RERATING", "trigger_type": "Stage2", "trigger_date": "2024-01-18", "evidence_available_at_that_date": "Enterprise AI/ERP repricing awareness with unusually strong volume/relative-strength; this was still early and not fully earnings-confirmed.", "evidence_source": "company/financial-news AI product and enterprise software evidence; source-level revalidation required", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/012/012510/2024.csv", "profile_path": "atlas/symbol_profiles/012/012510.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-18", "entry_price": 40800, "MFE_30D_pct": 38.0, "MFE_90D_pct": 55.1, "MFE_180D_pct": 91.9, "MFE_1Y_pct": 91.9, "MFE_2Y_pct": null, "MAE_30D_pct": 0.0, "MAE_90D_pct": 0.0, "MAE_180D_pct": 0.0, "MAE_1Y_pct": -1.2, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": false, "peak_date": "2024-07-08", "peak_price": 78300, "drawdown_after_peak_pct": -40.0, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "", "four_b_evidence_type": "", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "excellent_entry", "calibration_usable": true, "forward_window_trading_days": 252, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L1_DZ_G1", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R8L1_DZ_T2", "case_id": "R8L1_DZ_012510_2024", "symbol": "012510", "company_name": "더존비즈온", "round": "R8", "loop": "1", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "ENTERPRISE_AI_SAAS_RERATING", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-09", "evidence_available_at_that_date": "AI/ERP thesis plus second price-leg confirmation; still before fully relaxed Green but already actionable.", "evidence_source": "company/financial news/reports; revalidate source-level details", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/012/012510/2024.csv", "profile_path": "atlas/symbol_profiles/012/012510.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-04-09", "entry_price": 57800, "MFE_30D_pct": 9.5, "MFE_90D_pct": 35.5, "MFE_180D_pct": 35.5, "MFE_1Y_pct": 35.5, "MFE_2Y_pct": null, "MAE_30D_pct": -11.8, "MAE_90D_pct": -11.8, "MAE_180D_pct": -18.7, "MAE_1Y_pct": -18.7, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-08", "peak_price": 78300, "drawdown_after_peak_pct": -40.0, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": 0.45, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "", "four_b_evidence_type": "", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_entry", "calibration_usable": true, "forward_window_trading_days": 252, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L1_DZ_G2", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R8L1_DZ_T3", "case_id": "R8L1_DZ_012510_2024", "symbol": "012510", "company_name": "더존비즈온", "round": "R8", "loop": "1", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "ENTERPRISE_AI_SAAS_RERATING", "trigger_type": "Stage3-Yellow", "trigger_date": "2024-04-30", "evidence_available_at_that_date": "Momentum and thesis confirmation after second leg; valuation/MAE risk had increased.", "evidence_source": "price + AI/SaaS public evidence", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/012/012510/2024.csv", "profile_path": "atlas/symbol_profiles/012/012510.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-04-30", "entry_price": 59900, "MFE_30D_pct": 9.5, "MFE_90D_pct": 30.7, "MFE_180D_pct": 30.7, "MFE_1Y_pct": 30.7, "MFE_2Y_pct": null, "MAE_30D_pct": -15.0, "MAE_90D_pct": -15.0, "MAE_180D_pct": -21.5, "MAE_1Y_pct": -21.5, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-08", "peak_price": 78300, "drawdown_after_peak_pct": -40.0, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": 0.53, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "", "four_b_evidence_type": "", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_entry", "calibration_usable": true, "forward_window_trading_days": 252, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L1_DZ_G3", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R8L1_DZ_T4", "case_id": "R8L1_DZ_012510_2024", "symbol": "012510", "company_name": "더존비즈온", "round": "R8", "loop": "1", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "ENTERPRISE_AI_SAAS_RERATING", "trigger_type": "Stage3-Green", "trigger_date": "2024-06-26", "evidence_available_at_that_date": "Late Green candidate after price and AI/ERP thesis had already repriced strongly.", "evidence_source": "earnings/report/price confirmation", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/012/012510/2024.csv", "profile_path": "atlas/symbol_profiles/012/012510.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-06-26", "entry_price": 75900, "MFE_30D_pct": 3.2, "MFE_90D_pct": 3.2, "MFE_180D_pct": 3.2, "MFE_1Y_pct": 3.2, "MFE_2Y_pct": null, "MAE_30D_pct": -19.9, "MAE_90D_pct": -38.1, "MAE_180D_pct": -38.1, "MAE_1Y_pct": -38.1, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-08", "peak_price": 78300, "drawdown_after_peak_pct": -40.0, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": 0.91, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "", "four_b_evidence_type": "", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "late_entry", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L1_DZ_G4", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R8L1_DZ_T5", "case_id": "R8L1_DZ_012510_2024", "symbol": "012510", "company_name": "더존비즈온", "round": "R8", "loop": "1", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "ENTERPRISE_AI_SAAS_RERATING", "trigger_type": "Stage4B", "trigger_date": "2024-07-08", "evidence_available_at_that_date": "Price-only local/full peak after AI rerating; non-price 4B evidence not strong enough for full 4B.", "evidence_source": "price-only OHLC", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/012/012510/2024.csv", "profile_path": "atlas/symbol_profiles/012/012510.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-08", "entry_price": 75300, "MFE_30D_pct": 4.0, "MFE_90D_pct": 4.0, "MFE_180D_pct": 4.0, "MFE_1Y_pct": 4.0, "MFE_2Y_pct": null, "MAE_30D_pct": -35.6, "MAE_90D_pct": -37.6, "MAE_180D_pct": -37.6, "MAE_1Y_pct": -37.6, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-08", "peak_price": 78300, "drawdown_after_peak_pct": -40.0, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": null, "four_b_local_peak_proximity": 0.94, "four_b_full_window_peak_proximity": 0.94, "four_b_timing_verdict": "price_only_peak_watch_not_full_4B", "four_b_evidence_type": "price_only", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "event_premium", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L1_DZ_G5", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only"}
{"row_type": "trigger", "trigger_id": "R8L1_AHN_T1", "case_id": "R8L1_AHN_053800_2022", "symbol": "053800", "company_name": "안랩", "round": "R8", "loop": "1", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "SECURITY_POLITICAL_EVENT_PREMIUM", "trigger_type": "Stage2", "trigger_date": "2022-03-03", "evidence_available_at_that_date": "Ahn Cheol-soo presidential-race withdrawal/coalition period generated political-event attention; this was not cybersecurity EPS/FCF evidence.", "evidence_source": "election/news/political event; not fundamental security demand evidence", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/053/053800/2022.csv", "profile_path": "atlas/symbol_profiles/053/053800.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-03-03", "entry_price": 70800, "MFE_30D_pct": 208.6, "MFE_90D_pct": 208.6, "MFE_180D_pct": 208.6, "MFE_1Y_pct": 208.6, "MFE_2Y_pct": null, "MAE_30D_pct": -5.6, "MAE_90D_pct": -5.6, "MAE_180D_pct": -16.5, "MAE_1Y_pct": -16.5, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-03-24", "peak_price": 218500, "drawdown_after_peak_pct": -72.9, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "", "four_b_evidence_type": "", "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "price_moved_without_evidence", "calibration_usable": true, "forward_window_trading_days": 252, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L1_AHN_G1", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R8L1_AHN_T2", "case_id": "R8L1_AHN_053800_2022", "symbol": "053800", "company_name": "안랩", "round": "R8", "loop": "1", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "SECURITY_POLITICAL_EVENT_PREMIUM", "trigger_type": "Stage2-Actionable", "trigger_date": "2022-03-11", "evidence_available_at_that_date": "Relative-strength only candidate during political theme; no security revenue/customer/revision confirmation.", "evidence_source": "political/news + OHLC only", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/053/053800/2022.csv", "profile_path": "atlas/symbol_profiles/053/053800.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-03-11", "entry_price": 86500, "MFE_30D_pct": 152.6, "MFE_90D_pct": 152.6, "MFE_180D_pct": 152.6, "MFE_1Y_pct": 152.6, "MFE_2Y_pct": null, "MAE_30D_pct": 0.0, "MAE_90D_pct": -7.5, "MAE_180D_pct": -31.7, "MAE_1Y_pct": -31.7, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": true, "peak_date": "2022-03-24", "peak_price": 218500, "drawdown_after_peak_pct": -72.9, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "", "four_b_evidence_type": "", "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "price_moved_without_evidence", "calibration_usable": true, "forward_window_trading_days": 252, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L1_AHN_G2", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R8L1_AHN_T5", "case_id": "R8L1_AHN_053800_2022", "symbol": "053800", "company_name": "안랩", "round": "R8", "loop": "1", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "SECURITY_POLITICAL_EVENT_PREMIUM", "trigger_type": "Stage4B", "trigger_date": "2022-03-23", "evidence_available_at_that_date": "Price-only blowoff before/near peak; no confirmed non-price security-business 4B evidence.", "evidence_source": "price-only OHLC and political event context", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/053/053800/2022.csv", "profile_path": "atlas/symbol_profiles/053/053800.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-03-23", "entry_price": 175800, "MFE_30D_pct": 24.3, "MFE_90D_pct": 24.3, "MFE_180D_pct": 24.3, "MFE_1Y_pct": 24.3, "MFE_2Y_pct": null, "MAE_30D_pct": -46.5, "MAE_90D_pct": -53.9, "MAE_180D_pct": -66.4, "MAE_1Y_pct": -66.4, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-03-24", "peak_price": 218500, "drawdown_after_peak_pct": -72.9, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": null, "four_b_local_peak_proximity": 0.68, "four_b_full_window_peak_proximity": 0.68, "four_b_timing_verdict": "price_only_local_4B_too_early_or_nonactionable", "four_b_evidence_type": "price_only", "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_premium", "calibration_usable": true, "forward_window_trading_days": 252, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L1_AHN_G3", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only"}
{"row_type": "trigger", "trigger_id": "R8L1_AHN_T6", "case_id": "R8L1_AHN_053800_2022", "symbol": "053800", "company_name": "안랩", "round": "R8", "loop": "1", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "SECURITY_POLITICAL_EVENT_PREMIUM", "trigger_type": "Stage4C", "trigger_date": "2022-03-30", "evidence_available_at_that_date": "Event unwind after parabolic peak; not a normal thesis break because no business thesis had been confirmed.", "evidence_source": "price/event context only", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/053/053800/2022.csv", "profile_path": "atlas/symbol_profiles/053/053800.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-03-30", "entry_price": 122800, "MFE_30D_pct": 2.3, "MFE_90D_pct": 4.8, "MFE_180D_pct": 4.8, "MFE_1Y_pct": 4.8, "MFE_2Y_pct": null, "MAE_30D_pct": -23.5, "MAE_90D_pct": -34.0, "MAE_180D_pct": -51.9, "MAE_1Y_pct": -51.9, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-03-24", "peak_price": 218500, "drawdown_after_peak_pct": -72.9, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "", "four_b_evidence_type": "", "four_c_protection_label": "hard_4c_late_for_event_unwind", "trigger_outcome_label": "thesis_break", "calibration_usable": true, "forward_window_trading_days": 252, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L1_AHN_G4", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only"}
```

### 27.4 Score simulation rows JSONL

```jsonl
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R8L1_KRF_259960_2024", "trigger_id": "R8L1_KRF_T1", "symbol": "259960", "trigger_type": "Stage2", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 6, "revision_score": 7, "relative_strength_score": 5, "customer_quality_score": 6, "policy_or_regulatory_score": 1, "valuation_repricing_score": 5, "execution_risk_score": 2, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 58, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 7, "revision_score": 8, "relative_strength_score": 7, "customer_quality_score": 7, "policy_or_regulatory_score": 1, "valuation_repricing_score": 6, "execution_risk_score": 2, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 68, "stage_label_after": "Stage2-Actionable", "changed_components": ["revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "R8 proxy separates validated earnings/customer/AI-SaaS evidence from price-only or political-event relative strength.", "selected_by_profile": false, "MFE_90D_pct": 29.1, "MAE_90D_pct": -8.5, "score_return_alignment_label": "score_mid_return_high_promote_candidate"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R8L1_KRF_259960_2024", "trigger_id": "R8L1_KRF_T2", "symbol": "259960", "trigger_type": "Stage2-Actionable", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 8, "revision_score": 8, "relative_strength_score": 8, "customer_quality_score": 7, "policy_or_regulatory_score": 1, "valuation_repricing_score": 6, "execution_risk_score": 2, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 72, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 9, "revision_score": 9, "relative_strength_score": 9, "customer_quality_score": 8, "policy_or_regulatory_score": 1, "valuation_repricing_score": 7, "execution_risk_score": 2, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 80, "stage_label_after": "Stage3-Yellow", "changed_components": ["revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "R8 proxy separates validated earnings/customer/AI-SaaS evidence from price-only or political-event relative strength.", "selected_by_profile": false, "MFE_90D_pct": 34.7, "MAE_90D_pct": -8.9, "score_return_alignment_label": "score_mid_return_high_promote_candidate"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R8L1_KRF_259960_2024", "trigger_id": "R8L1_KRF_T4", "symbol": "259960", "trigger_type": "Stage3-Green", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 9, "revision_score": 9, "relative_strength_score": 9, "customer_quality_score": 8, "policy_or_regulatory_score": 1, "valuation_repricing_score": 5, "execution_risk_score": 2, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 86, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 9, "revision_score": 9, "relative_strength_score": 9, "customer_quality_score": 8, "policy_or_regulatory_score": 1, "valuation_repricing_score": 5, "execution_risk_score": 2, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 86, "stage_label_after": "Stage3-Green", "changed_components": ["revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "R8 proxy separates validated earnings/customer/AI-SaaS evidence from price-only or political-event relative strength.", "selected_by_profile": true, "MFE_90D_pct": 7.3, "MAE_90D_pct": -12.4, "score_return_alignment_label": "score_high_return_low_false_positive"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R8L1_KRF_259960_2024", "trigger_id": "R8L1_KRF_T5", "symbol": "259960", "trigger_type": "Stage4B", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 9, "revision_score": 8, "relative_strength_score": 10, "customer_quality_score": 8, "policy_or_regulatory_score": 1, "valuation_repricing_score": 3, "execution_risk_score": 2, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3+4B-watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 9, "revision_score": 8, "relative_strength_score": 10, "customer_quality_score": 8, "policy_or_regulatory_score": 1, "valuation_repricing_score": 3, "execution_risk_score": 2, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 82, "stage_label_after": "Stage3+4B-watch", "changed_components": ["revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "R8 proxy separates validated earnings/customer/AI-SaaS evidence from price-only or political-event relative strength.", "selected_by_profile": false, "MFE_90D_pct": 2.3, "MAE_90D_pct": -15.6, "score_return_alignment_label": "score_mid_return_low_watch_only"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R8L1_DZ_012510_2024", "trigger_id": "R8L1_DZ_T1", "symbol": "012510", "trigger_type": "Stage2", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 1, "margin_bridge_score": 4, "revision_score": 3, "relative_strength_score": 8, "customer_quality_score": 6, "policy_or_regulatory_score": 2, "valuation_repricing_score": 7, "execution_risk_score": 3, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 55, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 1, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 10, "customer_quality_score": 7, "policy_or_regulatory_score": 2, "valuation_repricing_score": 8, "execution_risk_score": 3, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 68, "stage_label_after": "Stage2-Actionable", "changed_components": ["revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "R8 proxy separates validated earnings/customer/AI-SaaS evidence from price-only or political-event relative strength.", "selected_by_profile": false, "MFE_90D_pct": 55.1, "MAE_90D_pct": 0.0, "score_return_alignment_label": "score_mid_return_high_promote_candidate"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R8L1_DZ_012510_2024", "trigger_id": "R8L1_DZ_T2", "symbol": "012510", "trigger_type": "Stage2-Actionable", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 1, "margin_bridge_score": 6, "revision_score": 6, "relative_strength_score": 8, "customer_quality_score": 7, "policy_or_regulatory_score": 2, "valuation_repricing_score": 6, "execution_risk_score": 3, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 1, "margin_bridge_score": 7, "revision_score": 7, "relative_strength_score": 9, "customer_quality_score": 7, "policy_or_regulatory_score": 2, "valuation_repricing_score": 6, "execution_risk_score": 3, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 78, "stage_label_after": "Stage3-Yellow", "changed_components": ["revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "R8 proxy separates validated earnings/customer/AI-SaaS evidence from price-only or political-event relative strength.", "selected_by_profile": false, "MFE_90D_pct": 35.5, "MAE_90D_pct": -11.8, "score_return_alignment_label": "score_mid_return_high_promote_candidate"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R8L1_DZ_012510_2024", "trigger_id": "R8L1_DZ_T3", "symbol": "012510", "trigger_type": "Stage3-Yellow", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 1, "margin_bridge_score": 7, "revision_score": 7, "relative_strength_score": 9, "customer_quality_score": 7, "policy_or_regulatory_score": 2, "valuation_repricing_score": 5, "execution_risk_score": 4, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 78, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 1, "margin_bridge_score": 7, "revision_score": 7, "relative_strength_score": 9, "customer_quality_score": 7, "policy_or_regulatory_score": 2, "valuation_repricing_score": 5, "execution_risk_score": 4, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 78, "stage_label_after": "Stage3-Yellow", "changed_components": ["revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "R8 proxy separates validated earnings/customer/AI-SaaS evidence from price-only or political-event relative strength.", "selected_by_profile": false, "MFE_90D_pct": 30.7, "MAE_90D_pct": -15.0, "score_return_alignment_label": "score_mid_return_high_promote_candidate"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R8L1_DZ_012510_2024", "trigger_id": "R8L1_DZ_T4", "symbol": "012510", "trigger_type": "Stage3-Green", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 1, "margin_bridge_score": 8, "revision_score": 8, "relative_strength_score": 9, "customer_quality_score": 7, "policy_or_regulatory_score": 2, "valuation_repricing_score": 3, "execution_risk_score": 5, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 84, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 1, "margin_bridge_score": 8, "revision_score": 8, "relative_strength_score": 9, "customer_quality_score": 7, "policy_or_regulatory_score": 2, "valuation_repricing_score": 3, "execution_risk_score": 5, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 84, "stage_label_after": "Stage3-Green", "changed_components": ["revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "R8 proxy separates validated earnings/customer/AI-SaaS evidence from price-only or political-event relative strength.", "selected_by_profile": true, "MFE_90D_pct": 3.2, "MAE_90D_pct": -38.1, "score_return_alignment_label": "score_high_return_low_false_positive"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R8L1_DZ_012510_2024", "trigger_id": "R8L1_DZ_T5", "symbol": "012510", "trigger_type": "Stage4B", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 1, "margin_bridge_score": 7, "revision_score": 7, "relative_strength_score": 10, "customer_quality_score": 7, "policy_or_regulatory_score": 2, "valuation_repricing_score": 2, "execution_risk_score": 6, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 77, "stage_label_before": "Stage3+4B-watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 1, "margin_bridge_score": 7, "revision_score": 7, "relative_strength_score": 10, "customer_quality_score": 7, "policy_or_regulatory_score": 2, "valuation_repricing_score": 2, "execution_risk_score": 6, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 77, "stage_label_after": "Stage3+4B-watch", "changed_components": ["revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "R8 proxy separates validated earnings/customer/AI-SaaS evidence from price-only or political-event relative strength.", "selected_by_profile": false, "MFE_90D_pct": 4.0, "MAE_90D_pct": -37.6, "score_return_alignment_label": "score_mid_return_low_watch_only"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R8L1_AHN_053800_2022", "trigger_id": "R8L1_AHN_T1", "symbol": "053800", "trigger_type": "Stage2", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 1, "revision_score": 0, "relative_strength_score": 7, "customer_quality_score": 2, "policy_or_regulatory_score": 7, "valuation_repricing_score": 0, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 48, "stage_label_before": "Stage2-watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 1, "revision_score": 0, "relative_strength_score": 3, "customer_quality_score": 2, "policy_or_regulatory_score": 7, "valuation_repricing_score": 0, "execution_risk_score": 8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 34, "stage_label_after": "Reject/event-premium", "changed_components": ["relative_strength_score", "execution_risk_score"], "component_delta_explanation": "R8 proxy separates validated earnings/customer/AI-SaaS evidence from price-only or political-event relative strength.", "selected_by_profile": false, "MFE_90D_pct": 208.6, "MAE_90D_pct": -5.6, "score_return_alignment_label": "score_low_return_high_missed_structural"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R8L1_AHN_053800_2022", "trigger_id": "R8L1_AHN_T2", "symbol": "053800", "trigger_type": "Stage2-Actionable", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 1, "revision_score": 0, "relative_strength_score": 10, "customer_quality_score": 2, "policy_or_regulatory_score": 8, "valuation_repricing_score": 0, "execution_risk_score": 7, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 61, "stage_label_before": "Stage2-Actionable-if-no-guardrail", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 1, "revision_score": 0, "relative_strength_score": 3, "customer_quality_score": 2, "policy_or_regulatory_score": 8, "valuation_repricing_score": 0, "execution_risk_score": 9, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 36, "stage_label_after": "Reject/event-premium", "changed_components": ["relative_strength_score", "execution_risk_score"], "component_delta_explanation": "R8 proxy separates validated earnings/customer/AI-SaaS evidence from price-only or political-event relative strength.", "selected_by_profile": false, "MFE_90D_pct": 152.6, "MAE_90D_pct": -7.5, "score_return_alignment_label": "score_low_return_high_missed_structural"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R8L1_AHN_053800_2022", "trigger_id": "R8L1_AHN_T5", "symbol": "053800", "trigger_type": "Stage4B", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 1, "revision_score": 0, "relative_strength_score": 10, "customer_quality_score": 2, "policy_or_regulatory_score": 8, "valuation_repricing_score": 0, "execution_risk_score": 10, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 56, "stage_label_before": "4B-watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 1, "revision_score": 0, "relative_strength_score": 2, "customer_quality_score": 2, "policy_or_regulatory_score": 8, "valuation_repricing_score": 0, "execution_risk_score": 10, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 31, "stage_label_after": "Reject/full-4B-not-confirmed", "changed_components": ["relative_strength_score", "execution_risk_score"], "component_delta_explanation": "R8 proxy separates validated earnings/customer/AI-SaaS evidence from price-only or political-event relative strength.", "selected_by_profile": false, "MFE_90D_pct": 24.3, "MAE_90D_pct": -53.9, "score_return_alignment_label": "score_low_return_high_missed_structural"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R8L1_AHN_053800_2022", "trigger_id": "R8L1_AHN_T6", "symbol": "053800", "trigger_type": "Stage4C", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 1, "revision_score": 0, "relative_strength_score": 5, "customer_quality_score": 2, "policy_or_regulatory_score": 8, "valuation_repricing_score": 0, "execution_risk_score": 10, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 38, "stage_label_before": "4C-watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 1, "revision_score": 0, "relative_strength_score": 1, "customer_quality_score": 2, "policy_or_regulatory_score": 8, "valuation_repricing_score": 0, "execution_risk_score": 10, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 25, "stage_label_after": "Event-unwind-reject", "changed_components": ["relative_strength_score", "execution_risk_score"], "component_delta_explanation": "R8 proxy separates validated earnings/customer/AI-SaaS evidence from price-only or political-event relative strength.", "selected_by_profile": false, "MFE_90D_pct": 4.8, "MAE_90D_pct": -34.0, "score_return_alignment_label": "score_mid_return_low_watch_only"}
```

### 27.5 Profile comparison rows CSV

```csv
row_type,profile_id,case_count,selected_trigger_count,selected_representative_trigger_count,avg_MFE_90D_pct,median_MFE_90D_pct,avg_MAE_90D_pct,median_MAE_90D_pct,avg_MFE_180D_pct,avg_MAE_180D_pct,hit_rate_MFE90_gt_20pct,bad_entry_rate_MAE90_lt_minus_15pct,false_positive_rate,missed_structural_count,late_green_count,avg_green_lateness_ratio,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
profile_comparison,baseline_current_proxy,3,2,2,5.2,5.2,-25.2,-25.2,10.5,-25.2,0.0,50.0,0.0,2,2,0.8,,,reference; safe but late and low upside capture
profile_comparison,stage2_actionable_early_evidence_plus_with_event_premium_guardrail,3,2,2,42.1,42.1,-4.2,-4.2,73.1,-4.2,100.0,0.0,0.0,0,0,,,,"selected; improved MFE and sharply reduced MAE, while rejecting political event premium"
profile_comparison,stage3_yellow_entry_relaxed,3,2,2,35.1,35.1,-10.4,-10.4,35.1,-13.8,100.0,0.0,0.0,0,0,0.8,,,"good backup, but not as early as P1"
profile_comparison,green_confirmation_timing_relaxed,3,2,2,12.6,12.6,-14.5,-14.5,18.4,-18.0,0.0,50.0,0.0,1,1,0.65,,,cautious; still late for R8 fast repricing
profile_comparison,four_b_peak_timing_tuned,3,3,0,10.2,4.0,-35.7,-37.6,13.7,-39.9,33.3,66.7,0.0,0,0,,0.8,0.8,do not treat price-only as full 4B; use overlay watch only
profile_comparison,four_c_thesis_break_earlier,3,1,0,4.8,4.8,-34.0,-34.0,4.8,-51.9,0.0,100.0,0.0,0,0,,,,not validated as hard 4C; event unwind only
```

### 27.6 Shadow weight CSV

```csv
row_type,axis,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,notes
shadow_weight,stage2_actionable_validated_earnings_or_customer_evidence,0,2,+2,Krafton and Douzone Stage2/early Actionable entries produced far better MFE90 with lower MAE than late Green.,P0 avg MFE90 5.2 / avg MAE90 -25.2 improved to P1 avg MFE90 42.1 / avg MAE90 -4.3 on selected representative entries.,R8L1_KRF_T1|R8L1_DZ_T1,2,shadow-only; event-premium guardrail required
shadow_weight,green_confirmation_lateness_penalty_for_fast_repricing_R8,0,-2,-2,Krafton Green lateness ratio 0.78 and Douzone 0.91 show Green confirmation often arrived after most upside.,Late Green selected entries MFE90 7.3 and 3.2 versus early entries 29.1 and 55.1.,R8L1_KRF_T4|R8L1_DZ_T4,2,shadow-only; do not relax Green broadly without earnings/customer evidence
shadow_weight,political_or_event_premium_without_business_component_guardrail,0,-3,-3,AhnLab delivered large MFE but from political-event premium rather than security EPS/FCF; without guardrail it would contaminate R8 success calibration.,AhnLab T2 MFE90 152.6 but MAE180 -31.7 and no validated security-business component; proposed profile rejects it.,R8L1_AHN_T1|R8L1_AHN_T2|R8L1_AHN_T5,3,shadow-only; preserves R8 security archetype quality
```

### 27.7 Optimization decision rows JSONL

```jsonl
{"row_type": "optimization_decision", "decision_id": "R8L1_DEC_01", "hypothesis": "Stage2-Actionable should promote early earnings/customer/AI-SaaS evidence plus relative strength before full Green confirmation.", "tested_trigger_ids": ["R8L1_KRF_T1", "R8L1_DZ_T1"], "baseline_profile": "baseline_current_proxy", "selected_profile": "stage2_actionable_early_evidence_plus_with_event_premium_guardrail", "backtest_result_summary": "Selected representative MFE90 improves from 5.2 to 42.1 and MAE90 improves from -25.2 to -4.3.", "accepted_or_rejected": "accepted", "delta_magnitude": "+2", "why_not_larger_delta": "Only two structural cases in this round; sample size caps delta at +2.", "risks": "Could over-promote AI-product announcements without revenue/customer evidence.", "next_validation_needed": "Validate against more platform/SW false positives in R8 Loop 2."}
{"row_type": "optimization_decision", "decision_id": "R8L1_DEC_02", "hypothesis": "Price-only 4B should not become full 4B without valuation/revision/dilution/legal evidence.", "tested_trigger_ids": ["R8L1_KRF_T5", "R8L1_DZ_T5", "R8L1_AHN_T5"], "baseline_profile": "baseline_current_proxy", "selected_profile": "four_b_peak_timing_tuned", "backtest_result_summary": "Local/full peak proximity can be high, but price-only signals were not sufficient to infer thesis deterioration.", "accepted_or_rejected": "accepted_as_guardrail", "delta_magnitude": "-2 to full-4B promotion", "why_not_larger_delta": "4B evidence remains useful as watch overlay.", "risks": "May miss pure price exhaustion in event bubbles.", "next_validation_needed": "Find R8 cases with valuation blowoff + revision slowdown."}
{"row_type": "optimization_decision", "decision_id": "R8L1_DEC_03", "hypothesis": "Political/event premium must be rejected for structural software/security rerating unless business components validate it.", "tested_trigger_ids": ["R8L1_AHN_T1", "R8L1_AHN_T2", "R8L1_AHN_T6"], "baseline_profile": "baseline_current_proxy", "selected_profile": "stage2_actionable_early_evidence_plus_with_event_premium_guardrail", "backtest_result_summary": "AhnLab shows huge MFE but fails structural score-return alignment; drawdown after peak was about -72.9.", "accepted_or_rejected": "accepted", "delta_magnitude": "-3 guardrail", "why_not_larger_delta": "AhnLab is one clean counterexample but still a single event-premium case.", "risks": "Some policy/security spending events may be real demand shocks; require customer/order evidence.", "next_validation_needed": "Compare with cybersecurity demand-shock case, not political figure linkage."}
```

### 27.8 Narrative-only rows JSONL

```jsonl
{"row_type":"narrative_only","case_id":"R8L1_SOURCE_LIMITATION","symbol":"multiple","reason":"some evidence source URLs were not stable in search result; OHLC calculations remain stock-web derived, but exact disclosure URLs should be revalidated before code ingestion","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

### 27.9 Aggregate metric rows CSV

```csv
row_type,trigger_type,usable_trigger_count,representative_trigger_count,avg_MFE_90D_pct,median_MFE_90D_pct,avg_MAE_90D_pct,median_MAE_90D_pct,avg_green_lateness_ratio,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
aggregate_metric,Stage2,3,3,97.6,55.1,-4.7,-5.6,unavailable,unavailable,unavailable,representative rows only; duplicate same-entry labels excluded
aggregate_metric,Stage2-Actionable,3,3,74.3,35.5,-9.4,-8.9,0.2,unavailable,unavailable,representative rows only; duplicate same-entry labels excluded
aggregate_metric,Stage3-Green,2,2,5.2,5.2,-25.2,-25.2,0.8,unavailable,unavailable,representative rows only; duplicate same-entry labels excluded
aggregate_metric,Stage3-Yellow,1,1,30.7,30.7,-15.0,-15.0,0.5,unavailable,unavailable,representative rows only; duplicate same-entry labels excluded
```

## 28. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are standalone E2R historical calibration and backtest optimization outputs produced using the Songdaiki/stock-web OHLC atlas. Do not redo market research unless a row is internally inconsistent. Ingest the machine-readable rows and update the repository in batch.

These MD files are not live candidate research. They are historical calibration and shadow optimization research. Use them to improve trigger-level backtesting, Stage2-Actionable / Stage3-Yellow gates, 4B timing, 4C protection logic, score-return alignment evaluation, aggregate deduplication, and shadow score profiles.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: `atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv`.
- Symbol profile pattern: `atlas/symbol_profiles/<prefix>/<ticker>.json`.
- Manifest and schema were used to validate max_date, column mapping, and calibration rules.

### Rules

- Use only rows with `calibration_usable=true` for weight calibration.
- Reject narrative-only rows for score changes.
- Reject rows without OHLC-derived MFE/MAE.
- Reject rows without at least 180 trading days forward window.
- Reject rows blocked by corporate-action-contaminated 180D window unless the user explicitly allows a separate adjusted-price revalidation.
- Reject shadow_weight rows that do not include before/after backtest effect.
- Reject score_simulation rows that have weighted_score_before/after but no raw_component_scores_before/after.
- Reject shadow_weight rows if the changed axis is not traceable to component-level score changes and OHLC backtest effect.
- Preserve shadow-only calibration separately from production rules.
- Keep Stage2-Actionable as a shadow trigger type unless already supported.
- Do not hardcode historical company names into scoring logic.
- Production scoring must not change unless the user explicitly approves applying the shadow profile.

### Repository tasks

1. Parse case / trigger / score_simulation / profile_comparison / optimization_decision / shadow weight / aggregate rows.
2. Validate price_source_validation rows.
3. Validate MFE / MAE / peak / drawdown values.
4. Validate green_lateness_ratio.
5. Validate four_b_local_peak_proximity.
6. Validate four_b_full_window_peak_proximity.
7. Reject price-only local 4B as full 4B unless non-price 4B evidence exists.
8. Validate 4C protection labels.
9. Validate calibration_usable filtering.
10. Validate same_entry_group_id.
11. Validate dedupe_for_aggregate.
12. Aggregate metrics must not double-count trigger rows sharing the same same_entry_group_id.
13. Validate raw_component_scores_before/after in score_simulation rows.
14. Validate before/after profile comparison rows.
15. Validate score-return alignment labels.
16. Validate Validation Scope / Non-Validation Scope and reject deltas for unvalidated gates.
17. Append valid case rows to abstract case library.
18. Append valid trigger rows to trigger calibration dataset.
19. Append score_simulation and profile_comparison rows to shadow calibration dataset.
20. Append shadow weight rows to shadow calibration profile only if before/after backtest effect and component-level explanation exist.
21. Add tests that narrative-only, non-OHLC, insufficient-forward-window, and corporate-action-contaminated rows cannot change weights.
22. Add tests for optimization decision validation.
23. Add tests for aggregate deduplication by same_entry_group_id.
24. Produce checkpoint summary.

### Expected output

- Concise implementation summary.
- Files changed.
- Tests run.
- Rows accepted.
- Rows rejected and why.
- Shadow profile rows accepted.
- Shadow weight rows accepted.
- Shadow weight rows rejected.
- No investment recommendation language.

## 29. Next Round State

```text
current_round_completed = R8 Loop 1
next_round = R9 Loop 1
next_sector = 모빌리티·운송·레저
production_scoring_changed = false
shadow_weight_only = true
```

## 30. Source Notes


- Stock-Web manifest: `atlas/manifest.json`; source is FinanceData/marcap, max_date 2026-02-20, raw/unadjusted OHLC, calibration shard root `atlas/ohlcv_tradable_by_symbol_year`.
- Stock-Web schema: `atlas/schema.json`; tradable columns are `d,o,h,l,c,v,a,mc,s,m`; MFE/MAE formulas match schema.
- Price profile paths checked: `atlas/symbol_profiles/259/259960.json`, `atlas/symbol_profiles/012/012510.json`, `atlas/symbol_profiles/053/053800.json`.
- Price shards checked: `atlas/ohlcv_tradable_by_symbol_year/259/259960/2024.csv`, `.../259960/2025.csv`, `atlas/ohlcv_tradable_by_symbol_year/012/012510/2024.csv`, `atlas/ohlcv_tradable_by_symbol_year/053/053800/2022.csv`.
- Evidence notes are deliberately separated from price data. Some Korean earnings/report source URLs were not stable in search results; rows requiring exact disclosure-link ingestion should be revalidated in the later coding-agent batch. This does not affect OHLC-derived MFE/MAE values.
- External context sources reviewed for event classification include public election/Ahn Cheol-soo background and Krafton/PUBG/BGMI market context. The AhnLab case is intentionally classified as event premium, not cybersecurity rerating.

