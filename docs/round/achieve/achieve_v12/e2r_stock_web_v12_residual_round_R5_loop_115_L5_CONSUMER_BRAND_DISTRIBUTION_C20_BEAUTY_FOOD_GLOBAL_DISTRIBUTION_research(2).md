# E2R Stock-Web V12 Residual Research — R5 Loop 115 / C20 Beauty-Food Global Distribution

## 0. Metadata / Execution Envelope

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R5
selected_loop: 115
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id: mixed_C20_kbeauty_kfood_global_distribution_quality_holdout
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 2 / 50+ rows / quality holdout
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
stock_web_manifest_max_date: 2026-02-20
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_executed_now: false
```

## 1. Canonical Selection / No-Repeat Ledger Read

No-Repeat Index 기준 C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION은 78 rows의 Priority 2 품질 보강 구역이다. 따라서 이번 실행은 새 수량 채우기가 아니라 K-beauty/K-food global distribution evidence가 repeat channel reorder, export mix, margin bridge, durable sell-through로 이어지는지 확인하는 quality holdout으로 설계했다. 직전 C18/C19 소비재 연구와 hard duplicate가 되지 않도록 C20 전용 symbol/trigger family를 사용했다.

## 2. Stock-Web Manifest / Schema Validation

```yaml
price_atlas_repo: Songdaiki/stock-web
manifest_path: atlas/manifest.json
schema_path: atlas/schema.json
stock_web_manifest_max_date: 2026-02-20
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
MFE_MAE_formula: entry_date 이후 N개 tradable rows의 high/low 기준
corporate_action_policy: entry_date~D+180 window contamination 시 calibration_usable=false
```

## 3. Research Question

C20에서 글로벌 유통, K-beauty/K-food export, ODM order, overseas channel recovery headline을 모두 같은 Stage3로 처리하면 오류가 난다. 이번 holdout의 질문은 다음이다.

```text
Can C20 separate durable global distribution rerating from one-off channel recovery / legacy beauty rebound / roadshop export spike by requiring repeat channel reorder, export mix, revenue recognition, and margin bridge?
```

## 4. Case Set Summary

| role | symbol | company | entry_date | trigger_type | outcome | key lesson |
|---|---:|---|---|---|---|---|
| positive | 257720 | 실리콘투 | 2024-05-23 | Stage3-Yellow | positive_with_local_4B_watch | P0 kept rerating but under-flagged post-peak 4B risk |
| positive | 003230 | 삼양식품 | 2024-05-17 | Stage3-Green | clean_positive | P0/P2 both align; named global demand + margin bridge justified Stage3-Green |
| positive | 192820 | 코스맥스 | 2025-02-25 | Stage3-Yellow | positive_with_local_4B_watch | Stage3-Yellow correct, but local 4B needed after fast 90D MFE |
| counterexample | 051900 | LG생활건강 | 2024-04-26 | Stage2-Actionable | counterexample_local_4B | P0 can over-promote legacy channel recovery; P2 should require repeat-order bridge |
| counterexample | 090430 | 아모레퍼시픽 | 2025-02-07 | Stage2-Actionable | counterexample_stage2_watch | Global/COSRX bridge helped, but MAE profile argues Stage2-Watch before Stage3 |
| counterexample | 214420 | 토니모리 | 2024-05-28 | Stage2-Actionable | counterexample_high_MAE_local_4B | Strong MFE does not equal durable distribution rerating; local 4B is mandatory |

## 5. Evidence Notes

- 실리콘투는 K-beauty 글로벌 유통 네트워크와 해외 물류/법인망, 글로벌 대형 유통 파트너 노출이 핵심이다. 2024년 가격경로는 구조적 수혜를 확인했지만 peak 이후 drawdown이 커 local 4B watch를 요구한다.
- 삼양식품은 불닭/수출 volume과 ASP/margin bridge가 동시에 확인되어 C20에서 가장 깨끗한 Stage3-Green positive holdout이다.
- 코스맥스는 K-beauty indie brand ODM 수요와 2024년 record sales/OP가 90D/180D MFE로 이어졌지만, 빠른 peak 이후 drawdown은 4B overlay가 필요하다.
- LG생활건강과 아모레퍼시픽은 legacy beauty recovery, China/US channel improvement, COSRX integration이 있어도 repeat reorder/export mix/margin bridge가 충분히 선명하지 않으면 Stage2-Watch가 적합하다.
- 토니모리는 export-channel recovery와 빠른 MFE가 있었지만 180D MAE와 peak drawdown이 과도해 durable C20 rerating으로 압축하면 안 된다.

## 6. Trigger-Level Price Backtest

| symbol | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | DD after peak |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 257720 | 2024-05-23 | 31450 | 72.34% | -7.31% | 72.34% | -7.31% | 72.34% | -25.91% | 2024-06-19 | 54200 | -57.01% |
| 003230 | 2024-05-17 | 446500 | 60.81% | 0.00% | 60.81% | 0.00% | 89.70% | 0.00% | 2025-02-13 | 847000 | -5.90% |
| 192820 | 2025-02-25 | 166000 | 13.07% | -4.52% | 72.89% | -10.18% | 72.89% | -10.18% | 2025-06-25 | 287000 | -45.92% |
| 051900 | 2024-04-26 | 392000 | 22.45% | -4.46% | 22.45% | -18.11% | 22.45% | -24.87% | 2024-05-23 | 480000 | -38.65% |
| 090430 | 2025-02-07 | 118700 | 6.99% | -8.34% | 24.35% | -16.01% | 24.94% | -16.01% | 2025-06-24 | 148300 | -21.65% |
| 214420 | 2024-05-28 | 9460 | 81.71% | -0.85% | 81.71% | -20.72% | 81.71% | -42.81% | 2024-06-14 | 17190 | -68.53% |

Aggregate: avg_MFE_90D_pct=55.7583, avg_MAE_90D_pct=-12.055, avg_MFE_180D_pct=60.6717, avg_MAE_180D_pct=-19.9633.

## 7. Positive / Counterexample Balance

```yaml
positive_case_count: 3
counterexample_count: 3
local_4B_watch_count: 5
Stage4C_case_count: 0
calibration_usable_trigger_count: 6
representative_trigger_count: 6
new_independent_symbol_count: 6
reused_case_count: 0
```

## 8. Current Calibrated Profile Stress Test

| symbol | current profile risk | shadow correction |
|---:|---|---|
| 257720 | structural winner retained, but local 4B timing under-flagged | keep Stage3-Yellow, add post-peak/high-MAE 4B cap |
| 003230 | clean alignment | allow Stage3-Green when export volume + margin + capacity bridge align |
| 192820 | Stage3-Yellow correct but fast MFE can overheat | local 4B after rapid 90D vertical MFE |
| 051900 | legacy channel recovery can be over-promoted | require repeat reorder/export mix bridge; otherwise Stage2-Watch |
| 090430 | COSRX/global recovery is partial bridge, not automatic Stage3 | Stage2-Actionable until margin/reorder durability improves |
| 214420 | high MFE hides fragile distribution rerating | Stage2-Watch + local 4B; do not treat as durable Green |

## 9. Raw Component Score Breakdown — Research Proxy Only

| symbol | EPS/FCF | visibility | bottleneck/pricing | mispricing | rerating | capital allocation | info confidence | total before | total after |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 257720 | 78 | 74 | 66 | 82 | 72 | 50 | 78 | 80 | 78 |
| 003230 | 92 | 88 | 78 | 84 | 82 | 55 | 90 | 88 | 89 |
| 192820 | 83 | 82 | 72 | 77 | 76 | 52 | 84 | 84 | 83 |
| 051900 | 62 | 66 | 55 | 64 | 58 | 50 | 72 | 74 | 63 |
| 090430 | 66 | 70 | 60 | 66 | 64 | 50 | 74 | 76 | 71 |
| 214420 | 74 | 62 | 56 | 80 | 60 | 45 | 68 | 77 | 68 |

## 10. Profile Comparison: P0 / P0b / P1 / P2 / P3

| profile | rule concept | false-positive pressure | positive preservation | avg 180D alignment | verdict |
|---|---|---:|---:|---|---|
| P0 current proxy | global calibrated profile only | 3/6 | 3/3 | mixed, MAE180 avg -19.96% | still leaves C20 legacy/channel false positives |
| P0b stricter Stage2 bridge | require public evidence + margin signal | 2/6 | 3/3 | better | helps but misses peak drawdown guard |
| P1 distribution-quality gate | require export mix or named channel reorder | 2/6 | 3/3 | better | useful C20-specific split |
| P2 distribution + local 4B cap | require repeat channel/reorder/margin bridge and cap high-MAE | 1/6 | 3/3 | best balance | recommended shadow profile |
| P3 overly strict Green cap | require two quarters of confirmed margin | 0/6 | 1/3 | too conservative | blocks Samyang/Cosmax too much |

## 11. Stage2 / Stage3 / 4B / 4C Interpretation

Stage2 can open on public export/channel/earnings evidence. Stage3-Yellow requires repeat channel reorder, export mix, margin bridge, or ODM/customer order durability. Stage3-Green is reserved for cases like Samyang Foods where export volume, margin, and capacity/demand bridge are unusually clean. Stage4B should overlay fast-MFE/high-MAE or post-peak drawdown cases. Stage4C is not triggered here because no case showed confirmed thesis break; the failures are mostly durability/entry-quality/overpromotion errors rather than hard thesis breaks.

## 12. 4B Local vs Full-Window Proximity

| symbol | local_4B_needed | full_window_4B_needed | reason |
|---:|---|---|---|
| 257720 | true | true | DD -57.01%, MAE180 -25.91% |
| 003230 | false | false | DD -5.90%, MAE180 0.00% |
| 192820 | true | true | DD -45.92%, MAE180 -10.18% |
| 051900 | true | false | DD -38.65%, MAE180 -24.87% |
| 090430 | true | false | DD -21.65%, MAE180 -16.01% |
| 214420 | true | true | DD -68.53%, MAE180 -42.81% |

## 13. Sector-Specific Rule Candidate

```text
L5_C20_GLOBAL_DISTRIBUTION_REORDER_EXPORT_MIX_MARGIN_BRIDGE_GATE
```

A C20 Stage3 upgrade should require at least two of: repeat reorder/channel sell-through, export mix expansion outside one legacy market, gross/operating margin bridge, named distributor/platform route, or ODM/customer order durability. If price-only vertical MFE appears before the second confirmation, attach local 4B watch instead of Green.

## 14. Canonical Archetype Rule Candidate

```text
C20_GLOBAL_DISTRIBUTION_REQUIRES_REPEAT_CHANNEL_REORDER_EXPORT_MIX_AND_MARGIN_BRIDGE_WITH_LOCAL_4B_CAP
```

## 15. Shadow Weight Proposal

```csv
canonical_archetype_id,axis,delta,reason,production_apply_now
C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,earnings_visibility,+0.04,repeat reorder/export mix should matter more,false
C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,information_confidence,+0.03,named channel and source-backed evidence reduce false positives,false
C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,valuation_rerating,-0.03,price-only rerating causes local 4B mistakes,false
C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,market_mispricing,-0.02,legacy channel rebound should not overpower margin bridge,false
```

## 16. Residual Contribution Summary

```yaml
loop_contribution_label: canonical_archetype_rule_candidate
residual_error_found: true
current_profile_error_count: 4
new_axis_proposed: C20_GLOBAL_DISTRIBUTION_REQUIRES_REPEAT_CHANNEL_REORDER_EXPORT_MIX_AND_MARGIN_BRIDGE_WITH_LOCAL_4B_CAP
existing_axis_strengthened:
  - stage2_required_bridge
  - local_4b_watch_guard
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
do_not_propose_new_weight_delta: false
```

## 17. Novelty / Duplicate Check

```yaml
hard_duplicate_key: canonical_archetype_id + symbol + trigger_type + entry_date
new_independent_case_count: 6
reused_case_count: 0
same_archetype_new_symbol_count: 6
same_archetype_new_trigger_family_count: 6
source_sector_duplicate_count: 0
```

## 18. Corporate Action / Forward Window Validation

All six case windows use Stock-Web tradable shards with at least 180 forward tradable rows before manifest max_date 2026-02-20. Checked profile caveat basis: no corporate-action candidate date overlaps entry_date through D+180 for the selected windows. All rows remain calibration_usable=true.

## 19. Machine-Readable JSONL Rows

```jsonl
{"row_type":"price_source_validation","price_data_repo":"Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","stock_web_manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","mfe_mae_formula":"MFE_N=(max_high(entry_date..N)/entry_price-1)*100; MAE_N=(min_low(entry_date..N)/entry_price-1)*100","all_case_forward_windows_checked":true,"corporate_action_policy":"block if candidate date overlaps entry_date through D+180"}
{"row_type":"case","case_id":"C20-257720-2024-05-23-SILICON2-GLOBAL-KBEAUTY-DISTRIBUTION","symbol":"257720","company_name":"실리콘투","selected_round":"R5","selected_loop":115,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"mixed_C20_kbeauty_kfood_global_distribution_quality_holdout","case_role":"positive","evidence_family":"KBEAUTY_GLOBAL_DISTRIBUTOR_REORDER_MARGIN","new_independent_case":true,"dedupe_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|257720|Stage3-Yellow|2024-05-23"}
{"row_type":"trigger","trigger_id":"C20-257720-2024-05-23-SILICON2-GLOBAL-KBEAUTY-DISTRIBUTION-TRIGGER","case_id":"C20-257720-2024-05-23-SILICON2-GLOBAL-KBEAUTY-DISTRIBUTION","symbol":"257720","company_name":"실리콘투","round":"R5","loop":115,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"mixed_C20_kbeauty_kfood_global_distribution_quality_holdout","trigger_type":"Stage3-Yellow","trigger_date":"2024-05-22","evidence_available_at_that_date":true,"evidence_timing_rule":"report_after_1Q24_results","evidence_source_url":"https://www.siliconii.com/en/sub/sub03_01.php?boardid=newsen&category=&idx=5&mode=view&offset=&sk=&sw=","stage2_evidence":["global_distribution_or_export_channel_signal","reported_sales_or_operating_profit_improvement","public_source_before_entry"],"stage3_evidence":["repeat_channel_reorder_or_global_demand_bridge","margin_bridge"],"stage4b_evidence":["post_peak_drawdown","local_price_blowoff_or_high_MAE"],"stage4c_evidence":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv|atlas/ohlcv_tradable_by_symbol_year/257/257720/2025.csv","profile_path":"atlas/symbol_profiles/257/257720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","entry_date":"2024-05-23","entry_price":31450,"MFE_30D_pct":72.34,"MAE_30D_pct":-7.31,"MFE_90D_pct":72.34,"MAE_90D_pct":-7.31,"MFE_180D_pct":72.34,"MAE_180D_pct":-25.91,"MFE_1Y_pct":null,"MAE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"below_entry_30D":true,"below_entry_90D":true,"peak_date":"2024-06-19","peak_price":54200,"drawdown_after_peak_pct":-57.01,"green_lateness_ratio":"not_applicable","four_b_timing_verdict":"local_4B_watch_required","four_c_protection_label":"no_thesis_break_confirmed","trigger_outcome_label":"positive_with_local_4B_watch","current_profile_verdict":"P0 kept rerating but under-flagged post-peak 4B risk","calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","calibration_block_reasons":[],"same_entry_group_id":"C20-257720-2024-05-23-SILICON2-GLOBAL-KBEAUTY-DISTRIBUTION","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","case_id":"C20-257720-2024-05-23-SILICON2-GLOBAL-KBEAUTY-DISTRIBUTION","symbol":"257720","profile_id":"C20_shadow_holdout_profile_P2","component_scores":{"eps_fcf_explosion":78,"earnings_visibility":74,"bottleneck_pricing":66,"market_mispricing":82,"valuation_rerating":72,"capital_allocation":50,"information_confidence":78},"total_before_shadow_rule":80,"total_after_shadow_rule":78,"stage_before_shadow_rule":"Stage3-Yellow","stage_after_shadow_rule":"Stage3-Yellow","score_delta_after_rule":-2}
{"row_type":"case","case_id":"C20-003230-2024-05-17-SAMYANG-EXPORT-NOODLE-MARGIN","symbol":"003230","company_name":"삼양식품","selected_round":"R5","selected_loop":115,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"mixed_C20_kbeauty_kfood_global_distribution_quality_holdout","case_role":"positive","evidence_family":"KFOOD_GLOBAL_EXPORT_VOLUME_MARGIN","new_independent_case":true,"dedupe_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|003230|Stage3-Green|2024-05-17"}
{"row_type":"trigger","trigger_id":"C20-003230-2024-05-17-SAMYANG-EXPORT-NOODLE-MARGIN-TRIGGER","case_id":"C20-003230-2024-05-17-SAMYANG-EXPORT-NOODLE-MARGIN","symbol":"003230","company_name":"삼양식품","round":"R5","loop":115,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"mixed_C20_kbeauty_kfood_global_distribution_quality_holdout","trigger_type":"Stage3-Green","trigger_date":"2024-05-16","evidence_available_at_that_date":true,"evidence_timing_rule":"earnings_after_close","evidence_source_url":"https://www.asiae.co.kr/article/2024051617534058348","stage2_evidence":["global_distribution_or_export_channel_signal","reported_sales_or_operating_profit_improvement","public_source_before_entry"],"stage3_evidence":["repeat_channel_reorder_or_global_demand_bridge","margin_bridge"],"stage4b_evidence":[],"stage4c_evidence":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv|atlas/ohlcv_tradable_by_symbol_year/003/003230/2025.csv","profile_path":"atlas/symbol_profiles/003/003230.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","entry_date":"2024-05-17","entry_price":446500,"MFE_30D_pct":60.81,"MAE_30D_pct":0.0,"MFE_90D_pct":60.81,"MAE_90D_pct":0.0,"MFE_180D_pct":89.7,"MAE_180D_pct":0.0,"MFE_1Y_pct":null,"MAE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"below_entry_30D":false,"below_entry_90D":false,"peak_date":"2025-02-13","peak_price":847000,"drawdown_after_peak_pct":-5.9,"green_lateness_ratio":"not_applicable","four_b_timing_verdict":"no_4B_required","four_c_protection_label":"no_thesis_break_confirmed","trigger_outcome_label":"clean_positive","current_profile_verdict":"P0/P2 both align; named global demand + margin bridge justified Stage3-Green","calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","calibration_block_reasons":[],"same_entry_group_id":"C20-003230-2024-05-17-SAMYANG-EXPORT-NOODLE-MARGIN","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","case_id":"C20-003230-2024-05-17-SAMYANG-EXPORT-NOODLE-MARGIN","symbol":"003230","profile_id":"C20_shadow_holdout_profile_P2","component_scores":{"eps_fcf_explosion":92,"earnings_visibility":88,"bottleneck_pricing":78,"market_mispricing":84,"valuation_rerating":82,"capital_allocation":55,"information_confidence":90},"total_before_shadow_rule":88,"total_after_shadow_rule":89,"stage_before_shadow_rule":"Stage3-Green","stage_after_shadow_rule":"Stage3-Green","score_delta_after_rule":1}
{"row_type":"case","case_id":"C20-192820-2025-02-25-COSMAX-ODM-GLOBAL-INDIE-BRANDS","symbol":"192820","company_name":"코스맥스","selected_round":"R5","selected_loop":115,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"mixed_C20_kbeauty_kfood_global_distribution_quality_holdout","case_role":"positive","evidence_family":"KBEAUTY_ODM_GLOBAL_INDIE_BRAND_ORDERBOOK","new_independent_case":true,"dedupe_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|192820|Stage3-Yellow|2025-02-25"}
{"row_type":"trigger","trigger_id":"C20-192820-2025-02-25-COSMAX-ODM-GLOBAL-INDIE-BRANDS-TRIGGER","case_id":"C20-192820-2025-02-25-COSMAX-ODM-GLOBAL-INDIE-BRANDS","symbol":"192820","company_name":"코스맥스","round":"R5","loop":115,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"mixed_C20_kbeauty_kfood_global_distribution_quality_holdout","trigger_type":"Stage3-Yellow","trigger_date":"2025-02-24","evidence_available_at_that_date":true,"evidence_timing_rule":"annual_2024_result_event","evidence_source_url":"https://www.mk.co.kr/en/business/11249094","stage2_evidence":["global_distribution_or_export_channel_signal","reported_sales_or_operating_profit_improvement","public_source_before_entry"],"stage3_evidence":["repeat_channel_reorder_or_global_demand_bridge","margin_bridge"],"stage4b_evidence":["post_peak_drawdown","local_price_blowoff_or_high_MAE"],"stage4c_evidence":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/192/192820/2024.csv|atlas/ohlcv_tradable_by_symbol_year/192/192820/2025.csv","profile_path":"atlas/symbol_profiles/192/192820.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","entry_date":"2025-02-25","entry_price":166000,"MFE_30D_pct":13.07,"MAE_30D_pct":-4.52,"MFE_90D_pct":72.89,"MAE_90D_pct":-10.18,"MFE_180D_pct":72.89,"MAE_180D_pct":-10.18,"MFE_1Y_pct":null,"MAE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"below_entry_30D":true,"below_entry_90D":true,"peak_date":"2025-06-25","peak_price":287000,"drawdown_after_peak_pct":-45.92,"green_lateness_ratio":"not_applicable","four_b_timing_verdict":"local_4B_watch_required","four_c_protection_label":"no_thesis_break_confirmed","trigger_outcome_label":"positive_with_local_4B_watch","current_profile_verdict":"Stage3-Yellow correct, but local 4B needed after fast 90D MFE","calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","calibration_block_reasons":[],"same_entry_group_id":"C20-192820-2025-02-25-COSMAX-ODM-GLOBAL-INDIE-BRANDS","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","case_id":"C20-192820-2025-02-25-COSMAX-ODM-GLOBAL-INDIE-BRANDS","symbol":"192820","profile_id":"C20_shadow_holdout_profile_P2","component_scores":{"eps_fcf_explosion":83,"earnings_visibility":82,"bottleneck_pricing":72,"market_mispricing":77,"valuation_rerating":76,"capital_allocation":52,"information_confidence":84},"total_before_shadow_rule":84,"total_after_shadow_rule":83,"stage_before_shadow_rule":"Stage3-Yellow","stage_after_shadow_rule":"Stage3-Yellow","score_delta_after_rule":-1}
{"row_type":"case","case_id":"C20-051900-2024-04-26-LGHH-BEAUTY-RECOVERY-CHANNEL-MIX","symbol":"051900","company_name":"LG생활건강","selected_round":"R5","selected_loop":115,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"mixed_C20_kbeauty_kfood_global_distribution_quality_holdout","case_role":"counterexample","evidence_family":"LEGACY_BEAUTY_CHANNEL_RECOVERY_MARGIN_WATCH","new_independent_case":true,"dedupe_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|051900|Stage2-Actionable|2024-04-26"}
{"row_type":"trigger","trigger_id":"C20-051900-2024-04-26-LGHH-BEAUTY-RECOVERY-CHANNEL-MIX-TRIGGER","case_id":"C20-051900-2024-04-26-LGHH-BEAUTY-RECOVERY-CHANNEL-MIX","symbol":"051900","company_name":"LG생활건강","round":"R5","loop":115,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"mixed_C20_kbeauty_kfood_global_distribution_quality_holdout","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-25","evidence_available_at_that_date":true,"evidence_timing_rule":"Q1_2024_result_after_close","evidence_source_url":"https://www.asiae.co.kr/article/2024042515582326422","stage2_evidence":["global_distribution_or_export_channel_signal","reported_sales_or_operating_profit_improvement","public_source_before_entry"],"stage3_evidence":["partial_brand_or_channel_recovery","insufficient_repeat_reorder_bridge"],"stage4b_evidence":["post_peak_drawdown","local_price_blowoff_or_high_MAE"],"stage4c_evidence":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/051/051900/2024.csv|atlas/ohlcv_tradable_by_symbol_year/051/051900/2025.csv","profile_path":"atlas/symbol_profiles/051/051900.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","entry_date":"2024-04-26","entry_price":392000,"MFE_30D_pct":22.45,"MAE_30D_pct":-4.46,"MFE_90D_pct":22.45,"MAE_90D_pct":-18.11,"MFE_180D_pct":22.45,"MAE_180D_pct":-24.87,"MFE_1Y_pct":null,"MAE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"below_entry_30D":true,"below_entry_90D":true,"peak_date":"2024-05-23","peak_price":480000,"drawdown_after_peak_pct":-38.65,"green_lateness_ratio":"not_applicable","four_b_timing_verdict":"local_4B_watch_required","four_c_protection_label":"no_thesis_break_confirmed","trigger_outcome_label":"counterexample_local_4B","current_profile_verdict":"P0 can over-promote legacy channel recovery; P2 should require repeat-order bridge","calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","calibration_block_reasons":[],"same_entry_group_id":"C20-051900-2024-04-26-LGHH-BEAUTY-RECOVERY-CHANNEL-MIX","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","case_id":"C20-051900-2024-04-26-LGHH-BEAUTY-RECOVERY-CHANNEL-MIX","symbol":"051900","profile_id":"C20_shadow_holdout_profile_P2","component_scores":{"eps_fcf_explosion":62,"earnings_visibility":66,"bottleneck_pricing":55,"market_mispricing":64,"valuation_rerating":58,"capital_allocation":50,"information_confidence":72},"total_before_shadow_rule":74,"total_after_shadow_rule":63,"stage_before_shadow_rule":"Stage2-Actionable","stage_after_shadow_rule":"Stage2-Actionable","score_delta_after_rule":-11}
{"row_type":"case","case_id":"C20-090430-2025-02-07-AMORE-COSRX-INTEGRATION-GLOBAL-MARGIN","symbol":"090430","company_name":"아모레퍼시픽","selected_round":"R5","selected_loop":115,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"mixed_C20_kbeauty_kfood_global_distribution_quality_holdout","case_role":"counterexample","evidence_family":"LEGACY_BEAUTY_COSRX_INTEGRATION_GLOBAL_MARGIN","new_independent_case":true,"dedupe_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|090430|Stage2-Actionable|2025-02-07"}
{"row_type":"trigger","trigger_id":"C20-090430-2025-02-07-AMORE-COSRX-INTEGRATION-GLOBAL-MARGIN-TRIGGER","case_id":"C20-090430-2025-02-07-AMORE-COSRX-INTEGRATION-GLOBAL-MARGIN","symbol":"090430","company_name":"아모레퍼시픽","round":"R5","loop":115,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"mixed_C20_kbeauty_kfood_global_distribution_quality_holdout","trigger_type":"Stage2-Actionable","trigger_date":"2025-02-06","evidence_available_at_that_date":true,"evidence_timing_rule":"FY2024_result_event","evidence_source_url":"https://www.apgroup.com/int/en/news/2025-02-06.html","stage2_evidence":["global_distribution_or_export_channel_signal","reported_sales_or_operating_profit_improvement","public_source_before_entry"],"stage3_evidence":["partial_brand_or_channel_recovery","insufficient_repeat_reorder_bridge"],"stage4b_evidence":["post_peak_drawdown","local_price_blowoff_or_high_MAE"],"stage4c_evidence":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/090/090430/2024.csv|atlas/ohlcv_tradable_by_symbol_year/090/090430/2025.csv","profile_path":"atlas/symbol_profiles/090/090430.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","entry_date":"2025-02-07","entry_price":118700,"MFE_30D_pct":6.99,"MAE_30D_pct":-8.34,"MFE_90D_pct":24.35,"MAE_90D_pct":-16.01,"MFE_180D_pct":24.94,"MAE_180D_pct":-16.01,"MFE_1Y_pct":null,"MAE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"below_entry_30D":true,"below_entry_90D":true,"peak_date":"2025-06-24","peak_price":148300,"drawdown_after_peak_pct":-21.65,"green_lateness_ratio":"not_applicable","four_b_timing_verdict":"local_4B_watch_required","four_c_protection_label":"no_thesis_break_confirmed","trigger_outcome_label":"counterexample_stage2_watch","current_profile_verdict":"Global/COSRX bridge helped, but MAE profile argues Stage2-Watch before Stage3","calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","calibration_block_reasons":[],"same_entry_group_id":"C20-090430-2025-02-07-AMORE-COSRX-INTEGRATION-GLOBAL-MARGIN","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","case_id":"C20-090430-2025-02-07-AMORE-COSRX-INTEGRATION-GLOBAL-MARGIN","symbol":"090430","profile_id":"C20_shadow_holdout_profile_P2","component_scores":{"eps_fcf_explosion":66,"earnings_visibility":70,"bottleneck_pricing":60,"market_mispricing":66,"valuation_rerating":64,"capital_allocation":50,"information_confidence":74},"total_before_shadow_rule":76,"total_after_shadow_rule":71,"stage_before_shadow_rule":"Stage3-Yellow","stage_after_shadow_rule":"Stage2-Actionable","score_delta_after_rule":-5}
{"row_type":"case","case_id":"C20-214420-2024-05-28-TONYMOLY-EXPORT-CHANNEL-RECOVERY","symbol":"214420","company_name":"토니모리","selected_round":"R5","selected_loop":115,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"mixed_C20_kbeauty_kfood_global_distribution_quality_holdout","case_role":"counterexample","evidence_family":"ROADSHOP_EXPORT_CHANNEL_RECOVERY_HIGH_MAE","new_independent_case":true,"dedupe_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|214420|Stage2-Actionable|2024-05-28"}
{"row_type":"trigger","trigger_id":"C20-214420-2024-05-28-TONYMOLY-EXPORT-CHANNEL-RECOVERY-TRIGGER","case_id":"C20-214420-2024-05-28-TONYMOLY-EXPORT-CHANNEL-RECOVERY","symbol":"214420","company_name":"토니모리","round":"R5","loop":115,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"mixed_C20_kbeauty_kfood_global_distribution_quality_holdout","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-27","evidence_available_at_that_date":true,"evidence_timing_rule":"Q1_2024_export_channel_recovery","evidence_source_url":"https://www.thebk.co.kr/news/articleView.html?idxno=207023","stage2_evidence":["global_distribution_or_export_channel_signal","reported_sales_or_operating_profit_improvement","public_source_before_entry"],"stage3_evidence":["partial_brand_or_channel_recovery","insufficient_repeat_reorder_bridge"],"stage4b_evidence":["post_peak_drawdown","local_price_blowoff_or_high_MAE"],"stage4c_evidence":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/214/214420/2024.csv|atlas/ohlcv_tradable_by_symbol_year/214/214420/2025.csv","profile_path":"atlas/symbol_profiles/214/214420.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","entry_date":"2024-05-28","entry_price":9460,"MFE_30D_pct":81.71,"MAE_30D_pct":-0.85,"MFE_90D_pct":81.71,"MAE_90D_pct":-20.72,"MFE_180D_pct":81.71,"MAE_180D_pct":-42.81,"MFE_1Y_pct":null,"MAE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"below_entry_30D":true,"below_entry_90D":true,"peak_date":"2024-06-14","peak_price":17190,"drawdown_after_peak_pct":-68.53,"green_lateness_ratio":"not_applicable","four_b_timing_verdict":"local_4B_watch_required","four_c_protection_label":"no_thesis_break_confirmed","trigger_outcome_label":"counterexample_high_MAE_local_4B","current_profile_verdict":"Strong MFE does not equal durable distribution rerating; local 4B is mandatory","calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","calibration_block_reasons":[],"same_entry_group_id":"C20-214420-2024-05-28-TONYMOLY-EXPORT-CHANNEL-RECOVERY","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","case_id":"C20-214420-2024-05-28-TONYMOLY-EXPORT-CHANNEL-RECOVERY","symbol":"214420","profile_id":"C20_shadow_holdout_profile_P2","component_scores":{"eps_fcf_explosion":74,"earnings_visibility":62,"bottleneck_pricing":56,"market_mispricing":80,"valuation_rerating":60,"capital_allocation":45,"information_confidence":68},"total_before_shadow_rule":77,"total_after_shadow_rule":68,"stage_before_shadow_rule":"Stage3-Yellow","stage_after_shadow_rule":"Stage2-Actionable","score_delta_after_rule":-9}
{"row_type":"aggregate","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","trigger_count":6,"positive_case_count":3,"counterexample_count":3,"local_4B_watch_count":5,"stage4C_count":0,"avg_MFE_90D_pct":55.7583,"avg_MAE_90D_pct":-12.055,"avg_MFE_180D_pct":60.6717,"avg_MAE_180D_pct":-19.9633,"residual_error_found":true}
{"row_type":"residual_contribution","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","proposed_rule_candidate":"C20_GLOBAL_DISTRIBUTION_REQUIRES_REPEAT_CHANNEL_REORDER_EXPORT_MIX_AND_MARGIN_BRIDGE_WITH_LOCAL_4B_CAP","existing_axis_strengthened":["stage2_required_bridge","local_4b_watch_guard","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"expected_effect":"reduce legacy beauty/channel recovery false positives while preserving export-led positive reratings"}
```

## 20. Machine-Readable Shadow Weight Row

```jsonl
{"row_type": "shadow_weight", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "rule_candidate": "C20_GLOBAL_DISTRIBUTION_REQUIRES_REPEAT_CHANNEL_REORDER_EXPORT_MIX_AND_MARGIN_BRIDGE_WITH_LOCAL_4B_CAP", "production_apply_now": false, "requires_later_batch_validation": true, "expected_false_positive_reduction": "legacy beauty/channel recovery and roadshop export spike cases", "expected_positive_preservation": "Samyang export-margin and Cosmax/Silicon2 distribution positives"}
```

## 21. Narrative-Only Notes

This file intentionally does not patch stock_agent and does not change production scoring. The evidence is designed for later batch ingestion and profile shadow comparison. C20 should not be collapsed into C18 consumer export reorder or C19 retail inventory; C20 specifically needs a global distribution / brand or food export monetization bridge.

## 22. Deferred Coding Agent Handoff Prompt

```text
You are the later batch implementation agent. Do not treat this MD as production patch instructions. Ingest the JSONL rows only after validating file naming, MFE/MAE fields, corporate-action windows, dedupe keys, trigger_type canonical labels, and source availability. Compare the C20 shadow rule candidate against existing C20 rows and reject it if it reduces positive preservation for verified export-margin reratings such as Samyang Foods. If accepted, add only shadow-profile deltas and produce an applied/rejected decision report.
```

## 23. Batch Ingest Self-Audit

```yaml
standard_filename_ok: true
filename_matches_metadata: true
uses_no_repeat_index_as_ledger_only: true
uses_stock_web_actual_ohlcv: true
jsonl_trigger_row_count: 6
calibration_usable_rows: 6
representative_rows: 6
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
future_data_leakage_detected: false
corporate_action_contaminated_rows: 0
insufficient_forward_window_rows: 0
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
ready_for_batch_ingest: true
```

## 24. Completed Round / Next Research State

```yaml
completed_round: R5
completed_loop: 115
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 2 / quality holdout / C20 rows 78
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_holdout_only_if_new_global_channel_or_margin_bridge
  - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_holdout_quality_only
  - C31_POLICY_SUBSIDY_LEGISLATION_EVENT_quality_holdout
```

## 25. Final Compact Result

```yaml
output_file: e2r_stock_web_v12_residual_round_R5_loop_115_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md
positive_counterexample_4B_4C: 3 / 3 / 5 / 0
calibration_usable_rows: 6
proposed_rule_candidate: C20_GLOBAL_DISTRIBUTION_REQUIRES_REPEAT_CHANNEL_REORDER_EXPORT_MIX_AND_MARGIN_BRIDGE_WITH_LOCAL_4B_CAP
```

## 26. Source URL Register

- 257720 실리콘투: https://www.siliconii.com/en/sub/sub03_01.php?boardid=newsen&category=&idx=5&mode=view&offset=&sk=&sw=
- 003230 삼양식품: https://www.asiae.co.kr/article/2024051617534058348
- 192820 코스맥스: https://www.mk.co.kr/en/business/11249094
- 051900 LG생활건강: https://www.asiae.co.kr/article/2024042515582326422
- 090430 아모레퍼시픽: https://www.apgroup.com/int/en/news/2025-02-06.html
- 214420 토니모리: https://www.thebk.co.kr/news/articleView.html?idxno=207023

## 27. Validation Scope Limitation

This research uses only the historical trigger window and Stock-Web max_date available at 2026-02-20. It does not attempt live candidate discovery, current valuation assessment, or trade recommendation.

## 28. End of Standalone MD
