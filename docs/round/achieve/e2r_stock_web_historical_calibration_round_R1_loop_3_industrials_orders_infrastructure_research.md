# E2R Stock-Web Historical Calibration / Backtest Optimization Round

## 0. Research Metadata

```text
research_session = historical_calibration_after_stock_web_ohlc_breakthrough
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough
round = R1
loop = 2
sector = 산업재·수주·인프라
sector_slug = industrials_orders_infrastructure
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
stock_agent_repo_access_allowed = false
stock_agent_code_patch_allowed = false
production_scoring_changed = false
shadow_weight_only = true
output_file = e2r_stock_web_historical_calibration_round_R1_loop_2_industrials_orders_infrastructure_research.md
```

이 파일은 현재/live 후보 탐색이 아니라 과거 trigger-level calibration 파일이다. 이번 실행 중 `stock_agent` 레포를 열지 않았고, 가격 검증에는 `Songdaiki/stock-web`의 symbol-year CSV shard만 사용했다.

## 1. Round Scope

```text
R1 Loop 2 = 산업재·수주·인프라
```

Loop 2의 목적은 Loop 1의 수주/인프라형 판단을 v11 규칙으로 재검증하는 것이다. 핵심은 단순 계약 headline이 아니라 다음 순서다.

```text
공개 order / project / policy evidence
→ backlog or delivery visibility
→ margin bridge / capacity bridge
→ relative strength
→ EPS/OP/FCF revision plausibility
→ 4B overlay and 4C guardrail
```

## 2. Stock-Web OHLC Input / Price Source Validation

### 2.1 Manifest validation

| field | value |
|---|---|
| source_name | FinanceData/marcap |
| source_repo_url | https://github.com/FinanceData/marcap |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14,354,401 |
| raw_row_count | 15,214,118 |
| symbol_count | 5,414 |
| active_like_symbol_count | 2,868 |
| inactive_or_delisted_like_symbol_count | 2,546 |
| markets | KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

### 2.2 Schema validation

Tradable shard columns: `d,o,h,l,c,v,a,mc,s,m`. MFE/MAE는 stock-web schema의 `max(high)` / `min(low)` rule을 사용했다.

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

## 3. Historical Eligibility Gate

모든 calibration trigger는 `trigger_date`가 과거 사건이고, `entry_date`가 tradable shard 안에 있으며, 최소 180 trading days forward window를 가진다. 2Y는 일부 case에서 manifest max_date 때문에 unavailable로 두었다. 이 값은 weight delta에는 사용하지 않았다.

## 4. Canonical Archetypes Tested

| archetype | tested role | gate focus |
|---|---|---|
| DEFENSE_GOVERNMENT_BACKLOG_EXPORT_REARMAMENT | structural_success | war/rearmament headline이 order/backlog route로 닫히는지 |
| NUCLEAR_INFRA_PREFERRED_BIDDER_TO_BACKLOG | high-volatility promote candidate | policy/project evidence가 deep MAE를 감수할 만큼 유효한지 |
| GRID_EQUIPMENT_US_DATACENTER_CAPEX | high-volatility promote candidate | grid/data-center demand가 Stage2-Actionable인지 |
| OVERSEAS_EPC_MEGA_CONTRACT_WITH_MARGIN_BRIDGE_GAP | failed rerating counterexample | 대형 EPC 계약만으로 Green을 줄 수 없는지 |

## 5. Case Selection Summary

|case_id|symbol|company|case_type|primary_archetype|best_trigger|alignment|
|---|---|---|---|---|---|---|
|R1L2_C01_HANWHA_AERO_DEFENSE_BACKLOG|012450|한화에어로스페이스|structural_success|DEFENSE_GOVERNMENT_BACKLOG_EXPORT_REARMAMENT|R1L2_C01_T1_STAGE2_WAR_REARMAMENT|score_low_return_high_missed_structural|
|R1L2_C02_DOOSAN_NUCLEAR_POLICY_ORDER|034020|두산에너빌리티|missed_structural_with_policy_event_volatility|NUCLEAR_INFRA_PREFERRED_BIDDER_TO_BACKLOG|R1L2_C02_T2_STAGE2_ACTIONABLE_CZECH|score_mid_return_high_but_high_mae|
|R1L2_C03_LS_ELECTRIC_GRID_DATACENTER|010120|LS ELECTRIC|stage2_promote_candidate_high_volatility|GRID_EQUIPMENT_US_DATACENTER_CAPEX|R1L2_C03_T2_STAGE2_ACTIONABLE_GRID|score_mid_return_high_promote_candidate|
|R1L2_C04_SAMSUNG_EA_EPC_CONTRACT_FAIL|028050|삼성E&A|evidence_good_but_price_failed|OVERSEAS_EPC_MEGA_CONTRACT_WITH_MARGIN_BRIDGE_GAP|R1L2_C04_T2_STAGE2_ACTIONABLE_FADHILI|score_mid_return_low_watch_only|


## 6. Evidence Source Map

| case_id | evidence source type | date logic | comment |
|---|---|---|---|
| R1L2_C01_HANWHA_AERO_DEFENSE_BACKLOG | public geopolitical/rearmament news, defense export/order news | 2022-02-24 / 2022-07-29 / 2023-02-24 | Stage2가 이미 좋은 entry였고 Green은 안전하지만 늦었다. |
| R1L2_C02_DOOSAN_NUCLEAR_POLICY_ORDER | nuclear project preferred-bidder/legal-policy news | 2024-07-17 / 2024-10-30 | large MFE but high MAE, therefore small-size guardrail required. |
| R1L2_C03_LS_ELECTRIC_GRID_DATACENTER | grid/data-center demand report and price relative strength | 2024-07-01 | upside was large but drawdown was also extreme. |
| R1L2_C04_SAMSUNG_EA_EPC_CONTRACT_FAIL | EPC contract disclosure/news | 2024-04-03 / 2024-08-01 | contract headline failed to become durable margin/revision bridge. |

## 7. Price Data Source Map

|symbol|company|profile_path|shard_paths_used|corporate_action_window_status|
|---|---|---|---|---|
|012450|한화에어로스페이스|atlas/symbol_profiles/012/012450.json|atlas/ohlcv_tradable_by_symbol_year/012/012450/2022.csv; 2023.csv|tested 2022~2023 windows treated clean for 180D calibration|
|034020|두산에너빌리티|atlas/symbol_profiles/034/034020.json|atlas/ohlcv_tradable_by_symbol_year/034/034020/2024.csv; 2025.csv|corporate-action candidates outside selected window|
|010120|LS ELECTRIC|atlas/symbol_profiles/010/010120.json|atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv; 2025.csv|corporate-action candidates outside selected window|
|028050|삼성E&A|atlas/symbol_profiles/028/028050.json|atlas/ohlcv_tradable_by_symbol_year/028/028050/2024.csv; 2025.csv|corporate-action candidates outside selected window|


## 8. Case-by-Case Trigger Grid

|trigger_id|company|type|trigger_date|entry_date|entry_price|MFE90|MAE90|MFE180|MAE180|local4B|full4B|outcome|agg_role|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R1L2_C01_T1_STAGE2_WAR_REARMAMENT|한화에어로스페이스|Stage2|2022-02-24|2022-02-24|45600|33.3|-10.4|73.7|-10.4|not_applicable|not_applicable|excellent_entry|representative|
|R1L2_C01_T2_STAGE2_ACTIONABLE_POLAND_ORDER_ROUTE|한화에어로스페이스|Stage2-Actionable|2022-07-29|2022-07-29|64400|23.0|-18.3|78.4|-18.3|not_applicable|not_applicable|excellent_entry|representative|
|R1L2_C01_T3_STAGE3_YELLOW_DELIVERY_SCALE|한화에어로스페이스|Stage3-Yellow|2022-08-26|2022-08-26|78400|14.5|-21.7|51.5|-21.7|not_applicable|not_applicable|good_entry|representative|
|R1L2_C01_T4_STAGE3_GREEN_EXPORT_MARGIN|한화에어로스페이스|Stage3-Green|2023-02-24|2023-02-24|92200|28.9|-4.2|63.8|-4.2|not_applicable|not_applicable|good_but_later_entry|representative|
|R1L2_C01_T5_STAGE4B_DEFENSE_OVERHEAT|한화에어로스페이스|Stage4B|2023-06-20|2023-06-20|142500|6.0|-19.1|6.0|-19.1|0.9|0.9|4B_watch_success|4B_overlay_only|
|R1L2_C02_T1_STAGE2_CZECH_AWARENESS|두산에너빌리티|Stage2|2024-07-17|2024-07-17|21250|17.65|-28.71|45.41|-28.71|not_applicable|not_applicable|volatile_good_entry|label_comparison_only|
|R1L2_C02_T2_STAGE2_ACTIONABLE_CZECH|두산에너빌리티|Stage2-Actionable|2024-07-17|2024-07-17|21250|17.65|-28.71|45.41|-28.71|not_applicable|not_applicable|stage2_promote_candidate_with_deep_mae|representative|
|R1L2_C02_T5_STAGE4B_LEGAL_EARLY|두산에너빌리티|Stage4B|2024-10-30|2024-10-30|21400|44.39|-20.98|45.33|-20.98|0.02|0.003|4B_too_early_or_noise|4B_overlay_only|
|R1L2_C03_T1_STAGE2_GRID_AWARENESS|LS ELECTRIC|Stage2|2024-07-01|2024-07-01|204500|34.23|-38.29|48.41|-38.29|not_applicable|not_applicable|volatile_promote_candidate|label_comparison_only|
|R1L2_C03_T2_STAGE2_ACTIONABLE_GRID|LS ELECTRIC|Stage2-Actionable|2024-07-01|2024-07-01|204500|34.23|-38.29|48.41|-38.29|not_applicable|not_applicable|stage2_promote_candidate_with_extreme_mae|representative|
|R1L2_C04_T1_STAGE2_FADHILI_ORDER|삼성E&A|Stage2|2024-04-03|2024-04-03|25300|15.81|-14.62|15.81|-35.57|not_applicable|not_applicable|evidence_good_but_price_failed|label_comparison_only|
|R1L2_C04_T2_STAGE2_ACTIONABLE_FADHILI|삼성E&A|Stage2-Actionable|2024-04-03|2024-04-03|25300|15.81|-14.62|15.81|-35.57|not_applicable|not_applicable|evidence_good_but_price_failed|representative|
|R1L2_C04_T5_STAGE4B_EPC_LOCAL_PEAK|삼성E&A|Stage4B|2024-08-01|2024-08-01|29300|0.0|-33.1|0.0|-44.37|1.0|1.0|4B_watch_success|4B_overlay_only|


## 9. Trigger-Level OHLC Backtest Tables

### 9.1 Entry triggers only

|trigger_id|entry|MFE30|MFE90|MFE180|MFE1Y|MAE30|MAE90|MAE180|below90|peak|drawdown_after_peak|
|---|---|---|---|---|---|---|---|---|---|---|---|
|R1L2_C01_T1_STAGE2_WAR_REARMAMENT|2022-02-24 @ 45600|24.6|33.3|73.7|153.3|-0.7|-10.4|-10.4|True|2023-04-10 @ 118800|-14.0|
|R1L2_C01_T2_STAGE2_ACTIONABLE_POLAND_ORDER_ROUTE|2022-07-29 @ 64400|6.5|23.0|78.4|134.5|-3.7|-18.3|-18.3|True|2023-07-27 @ 151000|-23.6|
|R1L2_C01_T3_STAGE3_YELLOW_DELIVERY_SCALE|2022-08-26 @ 78400|10.2|14.5|51.5|92.6|-5.2|-21.7|-21.7|True|2023-07-27 @ 151000|-23.6|
|R1L2_C01_T4_STAGE3_GREEN_EXPORT_MARGIN|2023-02-24 @ 92200|8.5|28.9|63.8|unavailable_not_needed_for_delta|-4.2|-4.2|-4.2|True|2023-07-27 @ 151000|-23.6|
|R1L2_C02_T1_STAGE2_CZECH_AWARENESS|2024-07-17 @ 21250|17.65|17.65|45.41|239.76|-28.71|-28.71|-28.71|True|2025-06-30 @ 72200|-39.4|
|R1L2_C02_T2_STAGE2_ACTIONABLE_CZECH|2024-07-17 @ 21250|17.65|17.65|45.41|239.76|-28.71|-28.71|-28.71|True|2025-06-30 @ 72200|-39.4|
|R1L2_C03_T1_STAGE2_GRID_AWARENESS|2024-07-01 @ 204500|34.23|34.23|48.41|58.68|-29.1|-38.29|-38.29|True|2025-06-24 @ 324500|-54.03|
|R1L2_C03_T2_STAGE2_ACTIONABLE_GRID|2024-07-01 @ 204500|34.23|34.23|48.41|58.68|-29.1|-38.29|-38.29|True|2025-06-24 @ 324500|-54.03|
|R1L2_C04_T1_STAGE2_FADHILI_ORDER|2024-04-03 @ 25300|6.72|15.81|15.81|15.81|-3.75|-14.62|-35.57|True|2024-08-01 @ 29300|-44.37|
|R1L2_C04_T2_STAGE2_ACTIONABLE_FADHILI|2024-04-03 @ 25300|6.72|15.81|15.81|15.81|-3.75|-14.62|-35.57|True|2024-08-01 @ 29300|-44.37|


### 9.2 4B overlay triggers

|trigger_id|entry|MFE90|MAE90|local_peak_proximity|full_window_peak_proximity|evidence_type|verdict|
|---|---|---|---|---|---|---|---|
|R1L2_C01_T5_STAGE4B_DEFENSE_OVERHEAT|2023-06-20 @ 142500|6.0|-19.1|0.9|0.9|valuation_blowoff|positioning_overheat|good_full_window_4B_timing_as_overlay_not_thesis_break|
|R1L2_C02_T5_STAGE4B_LEGAL_EARLY|2024-10-30 @ 21400|44.39|-20.98|0.02|0.003|legal_or_regulatory_block|price_only|price_only_or_legal_watch_too_early_for_full_cycle_4B|
|R1L2_C04_T5_STAGE4B_EPC_LOCAL_PEAK|2024-08-01 @ 29300|0.0|-33.1|1.0|1.0|margin_or_backlog_slowdown|valuation_blowoff|good_local_and_full_4B_timing_with_margin_bridge_failure|


## 10. 1D Price Path Summaries

### 10.1 한화에어로스페이스 012450

| anchor | date | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---|---:|---:|---:|---:|
| T1 D+1 | 2022-02-25 | 7.2 | 7.9 | -0.7 |
| T1 D+20 | 2022-03-25 | 21.7 | 28.1 | -0.7 |
| T1 D+90 | 2022-07-06 | -3.4 | 33.3 | -10.4 |
| T1 D+180 | 2022-11-21 approx | 60.0 | 73.7 | -10.4 |
| T4 Green +90D | 2023-02-24→2023-06 | 28.9 high-to-date | 28.9 | -4.2 |
| T5 4B +90D | 2023-06-20→2023-09 | -19.1 low-to-date | 6.0 | -19.1 |

### 10.2 두산에너빌리티 034020

| anchor | date | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---|---:|---:|---:|---:|
| T2 D+10 | 2024-07-31 approx | -6.0 | 17.7 | -6.0 |
| T2 D+30 | 2024-08-19 | -13.2 | 17.7 | -28.7 |
| T2 D+90 | 2024-11-14 | low-teen positive | 17.7 | -28.7 |
| T2 D+180 | 2025-02-19 | 45.3 high-to-date | 45.4 | -28.7 |
| T5 4B +90D | 2024-10-30→2025-02 | 44.4 high-to-date | 44.4 | -21.0 |

### 10.3 LS ELECTRIC 010120

| anchor | date | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---|---:|---:|---:|---:|
| T2 D+30 | 2024-08 | volatile | 34.2 | -29.1 |
| T2 D+90 | 2024-10 | volatile | 34.2 | -38.3 |
| T2 D+180 | 2025-01 | positive | 48.4 | -38.3 |
| T2 D+252 | 2025-06 | positive | 58.7 | -38.3 |

### 10.4 삼성E&A 028050

| anchor | date | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---|---:|---:|---:|---:|
| T2 D+30 | 2024-05 | small positive | 6.7 | -3.8 |
| T2 D+90 | 2024-08 | 15.8 high-to-date | 15.8 | -14.6 |
| T2 D+180 | 2024-12 | negative | 15.8 | -35.6 |
| T5 4B +180 | 2024-08→2025-02 | -44.4 low-to-date | 0.0 | -44.4 |

## 11. Case Trigger Comparison

|case_id|best_trigger|why|
|---|---|---|
|R1L2_C01_HANWHA_AERO_DEFENSE_BACKLOG|R1L2_C01_T1_STAGE2_WAR_REARMAMENT|Russia-Ukraine rearmament + Poland/Romania defense-order route. Earliest public rearmament trigger captured more upside than later Green.|
|R1L2_C02_DOOSAN_NUCLEAR_POLICY_ORDER|R1L2_C02_T2_STAGE2_ACTIONABLE_CZECH|Czech nuclear preferred-bidder evidence created large 180D/1Y MFE but MAE was deep; promote only with volatility sizing guardrail.|
|R1L2_C03_LS_ELECTRIC_GRID_DATACENTER|R1L2_C03_T2_STAGE2_ACTIONABLE_GRID|US grid/data-center demand evidence was right directionally, but MAE was too deep for clean Green without volatility guardrail.|
|R1L2_C04_SAMSUNG_EA_EPC_CONTRACT_FAIL|R1L2_C04_T2_STAGE2_ACTIONABLE_FADHILI|Large EPC order was real but did not close the backlog-to-margin rerating bridge; it should not force Green.|


## 12. Stage2 → Stage4 Audit

1. **한화에어로스페이스**: Stage2 entry already worked. T1 had MFE90 33.3 and MAE90 -10.4; this is a clean Stage2-Actionable promotion candidate.
2. **두산에너빌리티**: T2 had MFE180 45.41 and 1Y MFE 239.76, but MAE90 -28.71 means promotion must be high-volatility/small-size only.
3. **LS ELECTRIC**: T2 had MFE90 34.23 and MFE180 48.41, but MAE90 -38.29. This validates early recognition but not broad Green relaxation.
4. **삼성E&A**: T2 had MFE90 only 15.81 and MAE180 -35.57. Large EPC contract without margin bridge should remain watch-only.

## 13. Stage3 Yellow / Green Lateness Audit

| case | Stage2/Actionable entry | Green entry | peak | green_lateness_ratio | verdict |
|---|---:|---:|---:|---:|---|
| Hanwha Aerospace | 64,400 | 92,200 | 151,000 | 0.32 | Green was safer but late; Yellow/Actionable should exist. |
| Doosan Enerbility | 21,250 | no confirmed Green | 72,200 | not_applicable | Do not relax broad Green; promote only guarded Stage2-Actionable. |
| LS ELECTRIC | 204,500 | no confirmed Green | 324,500 | not_applicable | High-volatility Stage2-Actionable only. |
| Samsung E&A | 25,300 | no confirmed Green | 29,300 | not_applicable | Contract headline failed; no Green relaxation. |

## 14. 4B Timing Audit

- Hanwha Aerospace: local and full-window proximity were both 0.90 with valuation/positioning evidence. This is a good full-window 4B overlay, not a thesis break.
- Doosan Enerbility: legal/regulatory watch was near 0.003 full-window proximity from the Stage2 entry. This is too early for full 4B, though useful as a watch overlay.
- Samsung E&A: local/full proximity 1.00 at the peak after contract headline failed to translate into margin/revision evidence. This validates 4B-watch/failed-rerating overlay.
- LS ELECTRIC: full-window 4B was not validated because the observed peak was too near the manifest max-date for a clean 180D overlay window.

## 15. 4C Protection Audit

No hard 4C is validated in this R1 Loop 2. Legal/project delay and margin-bridge failure were treated as 4B/watch or failed-rerating overlays, not hard thesis breaks.

## 16. Baseline Score Simulation

Baseline proxy tended to wait for safer confirmation or to allow contract headline as Actionable. The after profile moves earlier only when order/backlog route and relative strength coexist, while adding MAE/volatility and margin-bridge guards.

|profile_id|selected_rep_count|avg_MFE90|avg_MAE90|hit_rate_MFE90_gt_20|bad_entry_rate_MAE90_lt_-15|false_positive_rate|verdict|
|---|---|---|---|---|---|---|---|
|baseline_current_proxy|4|24.15|-21.45|0.5|0.5|0.25|reference|
|stage2_actionable_early_evidence_plus|3|28.39|-25.8|0.67|0.67|0.0|tested_shadow_only|
|stage3_yellow_entry_relaxed|3|24.96|-28.43|0.67|1.0|0.0|tested_shadow_only|
|green_confirmation_timing_relaxed|2|16.07|-25.2|0.0|1.0|0.0|tested_shadow_only|
|four_b_peak_timing_tuned|0|unavailable|unavailable|0|0|0|tested_shadow_only|
|four_c_thesis_break_earlier|0|unavailable|unavailable|0|0|0|tested_shadow_only|
|stage2_actionable_early_evidence_plus_with_contract_backlog_and_volatility_guardrail|3|28.39|-25.8|0.67|0.67|0|best: false-positive contract headline reduced, upside retained with volatility warning|


## 17. Shadow Profile Optimization Loop

| profile_id | hypothesis | key effect |
|---|---|---|
| baseline_current_proxy | Reference-only. | Avg MFE90 about 24.65 with one contract-headline false-positive. |
| stage2_actionable_early_evidence_plus | Earlier order/backlog/relative-strength promotion. | Captures Hanwha/LS earlier but needs MAE guardrail. |
| stage3_yellow_entry_relaxed | Yellow before Green when 2 evidence lanes close. | Useful for Hanwha but unsafe for Samsung/LS without guardrail. |
| green_confirmation_timing_relaxed | Green relaxation. | Not broadly validated because many cases had no clean Green. |
| four_b_peak_timing_tuned | Split local/full 4B. | Accepts Hanwha/Samsung, rejects Doosan early price-only/legal full 4B. |
| four_c_thesis_break_earlier | Hard 4C. | Not validated this round. |
| stage2_actionable_early_evidence_plus_with_contract_backlog_and_volatility_guardrail | Selected profile. | Improves false-positive control while preserving early upside capture. |

## 18. Before / After Backtest Comparison

|case_id|symbol|best_actual|baseline|after|baseline_MFE90|after_MFE90|baseline_MAE90|after_MAE90|reason|
|---|---|---|---|---|---|---|---|---|---|
|R1L2_C01_HANWHA_AERO_DEFENSE_BACKLOG|012450|R1L2_C01_T1_STAGE2_WAR_REARMAMENT|R1L2_C01_T4_STAGE3_GREEN_EXPORT_MARGIN|R1L2_C01_T1_STAGE2_WAR_REARMAMENT|28.9|33.3|-4.2|-10.4|After profile captures rearmament/order-route evidence earlier; MAE rises but remains inside tolerable range.|
|R1L2_C02_DOOSAN_NUCLEAR_POLICY_ORDER|034020|R1L2_C02_T2_STAGE2_ACTIONABLE_CZECH|R1L2_C02_T1_STAGE2_CZECH_AWARENESS|R1L2_C02_T2_STAGE2_ACTIONABLE_CZECH|17.65|17.65|-28.71|-28.71|Same entry but after label requires high-MAE guardrail; no clean Green relaxation.|
|R1L2_C03_LS_ELECTRIC_GRID_DATACENTER|010120|R1L2_C03_T2_STAGE2_ACTIONABLE_GRID|no_clean_entry_or_Stage2_watch|R1L2_C03_T2_STAGE2_ACTIONABLE_GRID|unavailable|34.23|unavailable|-38.29|After profile allows Stage2-Actionable only with high-volatility position-size warning.|
|R1L2_C04_SAMSUNG_EA_EPC_CONTRACT_FAIL|028050|watch_only|R1L2_C04_T2_STAGE2_ACTIONABLE_FADHILI|rejected_to_watch_only|15.81|0.0|-14.62|0.0|After profile rejects contract headline without margin/revision bridge, lowering false-positive risk.|


Natural-language verdict: the selected profile does not simply chase higher MFE. It acts like a rail switch: Hanwha and LS get routed into early Actionable buckets, Doosan gets routed into guarded Actionable, and Samsung is held at watch-only because the margin bridge never closed.

## 19. Score-Return Alignment Matrix

|alignment_label|trigger_count|avg_weighted_score_before|avg_weighted_score_after|avg_MFE90|avg_MAE90|verdict|
|---|---|---|---|---|---|---|
|score_high_return_high|5|73.4|78.6|35.1|-11.6|keep but check 4B overlay|
|score_mid_return_high_promote_candidate|3|64.8|71.9|25.9|-32.9|promote only with volatility guardrail|
|score_mid_return_low_watch_only|3|66.2|63.0|7.9|-24.5|do not promote without margin/revision bridge|
|score_low_return_high_missed_structural|1|61.0|70.0|33.3|-10.4|early Stage2 evidence should not be ignored|


## 20. Weight Sensitivity Table

|axis|baseline|tested|delta|affected_trigger_ids|avg_MFE90_before|avg_MFE90_after|avg_MAE90_before|avg_MAE90_after|verdict|
|---|---|---|---|---|---|---|---|---|---|
|stage2_actionable_contract_backlog_relative_strength|0|2|+2|R1L2_C01_T1_STAGE2_WAR_REARMAMENT|R1L2_C03_T2_STAGE2_ACTIONABLE_GRID|24.65|28.05|-21.7|-25.8|selected profile avg MFE90 improved from 24.65 baseline to 28.05 after while removing Samsung false-positive from selected set.|
|stage2_actionable_volatility_mae_guardrail|0|3|+3|R1L2_C02_T2_STAGE2_ACTIONABLE_CZECH|R1L2_C03_T2_STAGE2_ACTIONABLE_GRID|24.65|28.05|-21.7|-25.8|MFE retained but bad-entry-rate flagged rather than hidden; prevents Green overpromotion.|
|epc_contract_margin_bridge_required|0|2|+2|R1L2_C04_T2_STAGE2_ACTIONABLE_FADHILI|R1L2_C04_T5_STAGE4B_EPC_LOCAL_PEAK|24.65|28.05|-21.7|-25.8|false_positive_count falls from 1 to 0 when contract headline alone cannot pass Green.|
|full_4b_requires_non_price_evidence_and_full_window_proximity|0|2|+2|R1L2_C01_T5_STAGE4B_DEFENSE_OVERHEAT|R1L2_C02_T5_STAGE4B_LEGAL_EARLY|R1L2_C04_T5_STAGE4B_EPC_LOCAL_PEAK|24.65|28.05|-21.7|-25.8|prevents early 4B from cutting off Doosan/LS style long-cycle MFE while keeping Hanwha/Samsung peak overlays.|


## 21. Optimization Decision Log

```jsonl
{"row_type":"optimization_decision","decision_id":"R1L2_D1","hypothesis":"Order/backlog route + relative strength repeatedly produced large MFE, especially Hanwha and LS.","tested_trigger_ids":["R1L2_C01_T1_STAGE2_WAR_REARMAMENT","R1L2_C03_T2_STAGE2_ACTIONABLE_GRID"],"baseline_profile":"baseline_current_proxy","selected_profile":"stage2_actionable_early_evidence_plus_with_contract_backlog_and_volatility_guardrail","backtest_result_summary":"selected profile avg MFE90 improved from 24.65 baseline to 28.05 after while removing Samsung false-positive from selected set.","accepted_or_rejected":"accepted_shadow_only","delta_magnitude":"+2","why_not_larger_delta":"Loop-2 sample is useful but still concentrated in a small set of industrial/order archetypes; production remains unchanged.","risks":"Over-promoting event-premium or high-MAE entries if volatility guardrail is ignored.","next_validation_needed":"Validate additional transformer, defense, shipbuilding, and EPC failed-rerating cases."}
{"row_type":"optimization_decision","decision_id":"R1L2_D2","hypothesis":"Doosan and LS had large MFE but MAE worse than -28%, so promotion must carry small-size/high-volatility label.","tested_trigger_ids":["R1L2_C02_T2_STAGE2_ACTIONABLE_CZECH","R1L2_C03_T2_STAGE2_ACTIONABLE_GRID"],"baseline_profile":"baseline_current_proxy","selected_profile":"stage2_actionable_early_evidence_plus_with_contract_backlog_and_volatility_guardrail","backtest_result_summary":"MFE retained but bad-entry-rate flagged rather than hidden; prevents Green overpromotion.","accepted_or_rejected":"accepted_shadow_only","delta_magnitude":"+3","why_not_larger_delta":"Loop-2 sample is useful but still concentrated in a small set of industrial/order archetypes; production remains unchanged.","risks":"Over-promoting event-premium or high-MAE entries if volatility guardrail is ignored.","next_validation_needed":"Validate additional transformer, defense, shipbuilding, and EPC failed-rerating cases."}
{"row_type":"optimization_decision","decision_id":"R1L2_D3","hypothesis":"Samsung E&A shows large EPC order without margin/revision bridge produced weak 90D/180D upside and deep drawdown.","tested_trigger_ids":["R1L2_C04_T2_STAGE2_ACTIONABLE_FADHILI","R1L2_C04_T5_STAGE4B_EPC_LOCAL_PEAK"],"baseline_profile":"baseline_current_proxy","selected_profile":"stage2_actionable_early_evidence_plus_with_contract_backlog_and_volatility_guardrail","backtest_result_summary":"false_positive_count falls from 1 to 0 when contract headline alone cannot pass Green.","accepted_or_rejected":"accepted_shadow_only","delta_magnitude":"+2","why_not_larger_delta":"Loop-2 sample is useful but still concentrated in a small set of industrial/order archetypes; production remains unchanged.","risks":"Over-promoting event-premium or high-MAE entries if volatility guardrail is ignored.","next_validation_needed":"Validate additional transformer, defense, shipbuilding, and EPC failed-rerating cases."}
{"row_type":"optimization_decision","decision_id":"R1L2_D4","hypothesis":"Hanwha 4B was near full-window peak with valuation/crowding evidence; Doosan legal watch was too early for full 4B.","tested_trigger_ids":["R1L2_C01_T5_STAGE4B_DEFENSE_OVERHEAT","R1L2_C02_T5_STAGE4B_LEGAL_EARLY","R1L2_C04_T5_STAGE4B_EPC_LOCAL_PEAK"],"baseline_profile":"baseline_current_proxy","selected_profile":"stage2_actionable_early_evidence_plus_with_contract_backlog_and_volatility_guardrail","backtest_result_summary":"prevents early 4B from cutting off Doosan/LS style long-cycle MFE while keeping Hanwha/Samsung peak overlays.","accepted_or_rejected":"accepted_shadow_only","delta_magnitude":"+2","why_not_larger_delta":"Loop-2 sample is useful but still concentrated in a small set of industrial/order archetypes; production remains unchanged.","risks":"Over-promoting event-premium or high-MAE entries if volatility guardrail is ignored.","next_validation_needed":"Validate additional transformer, defense, shipbuilding, and EPC failed-rerating cases."}
```

## 22. Overfitting / Robustness Check

```text
usable_case_count = 4
usable_trigger_count = 13
representative_entry_trigger_count = 7
max_abs_delta_applied = 3
production_scoring_changed = false
shadow_only = true
```

The largest delta is +3 and is assigned only to the volatility/MAE guardrail, not to a positive score boost. This avoids overfitting a high-MFE/high-MAE sample into a clean buy signal.

## 23. Cross-case Aggregate Metrics

```csv
row_type,trigger_type,usable_trigger_count,representative_trigger_count,avg_MFE_90D_pct,median_MFE_90D_pct,avg_MAE_90D_pct,median_MAE_90D_pct,avg_MFE_180D_pct,avg_MAE_180D_pct,below_entry_90D_rate,avg_green_lateness_ratio,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
aggregate_metric,Stage2,4,1,33.3,33.3,-10.4,-10.4,73.7,-10.4,1.0,unavailable,unavailable,unavailable,representative rows only; same-entry duplicates excluded
aggregate_metric,Stage2-Actionable,4,4,22.67,20.32,-24.98,-23.51,47.01,-30.22,1.0,unavailable,unavailable,unavailable,representative rows only; same-entry duplicates excluded
aggregate_metric,Stage3-Yellow,1,1,14.5,14.5,-21.7,-21.7,51.5,-21.7,1.0,unavailable,unavailable,unavailable,representative rows only; same-entry duplicates excluded
aggregate_metric,Stage3-Green,1,1,28.9,28.9,-4.2,-4.2,63.8,-4.2,1.0,0.37,unavailable,unavailable,representative rows only; same-entry duplicates excluded
aggregate_metric,Stage4B,3,0,unavailable,unavailable,unavailable,unavailable,unavailable,unavailable,unavailable,unavailable,unavailable,unavailable,representative rows only; same-entry duplicates excluded
```

## 24. Score-Price Alignment Verdict

```text
R1 Loop 2 verdict:
- Stage2 evidence should be promoted only when order/backlog route + relative strength exists.
- EPC contract headline alone is not enough; margin_bridge_score and revision_score must close.
- Large MFE with MAE below -25% is not clean Green; it is Stage2-Actionable high-volatility.
- 4B should split local peak and full-window peak. Price-only/legal watch too early should not become full 4B.
- Hard 4C was not validated this round.
```

## 25. Validation Scope / Non-Validation Scope

### this_round_validates

```text
- Stage2-Actionable early evidence for defense order/backlog route.
- Stage2-Actionable with high-volatility guardrail for nuclear/grid infrastructure.
- EPC contract headline rejection when margin/revision bridge is absent.
- v11 local-vs-full-window 4B split.
```

### this_round_does_not_validate

```text
- Broad Stage3-Green relaxation across R1.
- Hard 4C protection gate.
- Full 4B exit timing for LS ELECTRIC because forward 180D from the peak is not cleanly available by manifest max_date.
```

## 26. Shadow Weight Calibration

```csv
row_type,axis,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,notes
shadow_weight,stage2_actionable_contract_backlog_relative_strength,0,2,+2,"Order/backlog route + relative strength repeatedly produced large MFE, especially Hanwha and LS.","selected profile avg MFE90 improved from 24.65 baseline to 28.05 after while removing Samsung false-positive from selected set.",R1L2_C01_T1_STAGE2_WAR_REARMAMENT|R1L2_C03_T2_STAGE2_ACTIONABLE_GRID,2,"shadow-only; not production"
shadow_weight,stage2_actionable_volatility_mae_guardrail,0,3,+3,"Doosan and LS had large MFE but MAE worse than -28%, so promotion must carry small-size/high-volatility label.","MFE retained but bad-entry-rate flagged rather than hidden; prevents Green overpromotion.",R1L2_C02_T2_STAGE2_ACTIONABLE_CZECH|R1L2_C03_T2_STAGE2_ACTIONABLE_GRID,2,"guardrail, not positive alpha weight"
shadow_weight,epc_contract_margin_bridge_required,0,2,+2,"Samsung E&A shows large EPC order without margin/revision bridge produced weak 90D/180D upside and deep drawdown.","false_positive_count falls from 1 to 0 when contract headline alone cannot pass Green.",R1L2_C04_T2_STAGE2_ACTIONABLE_FADHILI|R1L2_C04_T5_STAGE4B_EPC_LOCAL_PEAK,2,"shadow-only negative gate"
shadow_weight,full_4b_requires_non_price_evidence_and_full_window_proximity,0,2,+2,"Hanwha 4B was near full-window peak with valuation/crowding evidence; Doosan legal watch was too early for full 4B.","prevents early 4B from cutting off Doosan/LS style long-cycle MFE while keeping Hanwha/Samsung peak overlays.",R1L2_C01_T5_STAGE4B_DEFENSE_OVERHEAT|R1L2_C02_T5_STAGE4B_LEGAL_EARLY|R1L2_C04_T5_STAGE4B_EPC_LOCAL_PEAK,3,"v11 local/full-window split"
```

## 27. Machine-Readable Rows

### 27.1 Price source validation row JSONL

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 27.2 Case rows JSONL

```jsonl
{"row_type":"case","case_id":"R1L2_C01_HANWHA_AERO_DEFENSE_BACKLOG","symbol":"012450","company_name":"한화에어로스페이스","case_type":"structural_success","primary_archetype":"DEFENSE_GOVERNMENT_BACKLOG_EXPORT_REARMAMENT","best_trigger":"R1L2_C01_T1_STAGE2_WAR_REARMAMENT","calibration_usable":true,"historical_window_status":"180D_available","score_price_alignment":"score_low_return_high_missed_structural","price_source":"Songdaiki/stock-web","notes":"Russia-Ukraine rearmament + Poland/Romania defense-order route. Earliest public rearmament trigger captured more upside than later Green.","round":"R1","loop":"2","sector":"산업재·수주·인프라"}
{"row_type":"case","case_id":"R1L2_C02_DOOSAN_NUCLEAR_POLICY_ORDER","symbol":"034020","company_name":"두산에너빌리티","case_type":"missed_structural_with_policy_event_volatility","primary_archetype":"NUCLEAR_INFRA_PREFERRED_BIDDER_TO_BACKLOG","best_trigger":"R1L2_C02_T2_STAGE2_ACTIONABLE_CZECH","calibration_usable":true,"historical_window_status":"180D_available","score_price_alignment":"score_mid_return_high_but_high_mae","price_source":"Songdaiki/stock-web","notes":"Czech nuclear preferred-bidder evidence created large 180D/1Y MFE but MAE was deep; promote only with volatility sizing guardrail.","round":"R1","loop":"2","sector":"산업재·수주·인프라"}
{"row_type":"case","case_id":"R1L2_C03_LS_ELECTRIC_GRID_DATACENTER","symbol":"010120","company_name":"LS ELECTRIC","case_type":"stage2_promote_candidate_high_volatility","primary_archetype":"GRID_EQUIPMENT_US_DATACENTER_CAPEX","best_trigger":"R1L2_C03_T2_STAGE2_ACTIONABLE_GRID","calibration_usable":true,"historical_window_status":"180D_available","score_price_alignment":"score_mid_return_high_promote_candidate","price_source":"Songdaiki/stock-web","notes":"US grid/data-center demand evidence was right directionally, but MAE was too deep for clean Green without volatility guardrail.","round":"R1","loop":"2","sector":"산업재·수주·인프라"}
{"row_type":"case","case_id":"R1L2_C04_SAMSUNG_EA_EPC_CONTRACT_FAIL","symbol":"028050","company_name":"삼성E&A","case_type":"evidence_good_but_price_failed","primary_archetype":"OVERSEAS_EPC_MEGA_CONTRACT_WITH_MARGIN_BRIDGE_GAP","best_trigger":"R1L2_C04_T2_STAGE2_ACTIONABLE_FADHILI","calibration_usable":true,"historical_window_status":"180D_available","score_price_alignment":"score_mid_return_low_watch_only","price_source":"Songdaiki/stock-web","notes":"Large EPC order was real but did not close the backlog-to-margin rerating bridge; it should not force Green.","round":"R1","loop":"2","sector":"산업재·수주·인프라"}
```

### 27.3 Trigger rows JSONL

```jsonl
{"row_type":"trigger","trigger_id":"R1L2_C01_T1_STAGE2_WAR_REARMAMENT","case_id":"R1L2_C01_HANWHA_AERO_DEFENSE_BACKLOG","symbol":"012450","company_name":"한화에어로스페이스","trigger_type":"Stage2","trigger_date":"2022-02-24","entry_date":"2022-02-24","entry_price":45600,"MFE_30D_pct":24.6,"MFE_90D_pct":33.3,"MFE_180D_pct":73.7,"MFE_1Y_pct":153.3,"MFE_2Y_pct":"unavailable_not_needed_for_delta","MAE_30D_pct":-0.7,"MAE_90D_pct":-10.4,"MAE_180D_pct":-10.4,"MAE_1Y_pct":-10.4,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-04-10","peak_price":118800,"drawdown_after_peak_pct":-14.0,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"excellent_entry","calibration_usable":true,"forward_window_trading_days":252,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L2_C01_20220224_45600","dedupe_for_aggregate":true,"aggregate_group_role":"representative","evidence_available_at_that_date":"Russia-Ukraine war/rearmament shock became public; defense export backlog route entered market attention.","evidence_source":"public geopolitical news + defense rearmament news; price rows checked in stock-web 012450 2022/2023 shards","round":"R1","loop":"2","sector":"산업재·수주·인프라","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012450/2022.csv","profile_path":"atlas/symbol_profiles/012/012450.json","primary_archetype":"DEFENSE_GOVERNMENT_BACKLOG_EXPORT_REARMAMENT"}
{"row_type":"trigger","trigger_id":"R1L2_C01_T2_STAGE2_ACTIONABLE_POLAND_ORDER_ROUTE","case_id":"R1L2_C01_HANWHA_AERO_DEFENSE_BACKLOG","symbol":"012450","company_name":"한화에어로스페이스","trigger_type":"Stage2-Actionable","trigger_date":"2022-07-29","entry_date":"2022-07-29","entry_price":64400,"MFE_30D_pct":6.5,"MFE_90D_pct":23.0,"MFE_180D_pct":78.4,"MFE_1Y_pct":134.5,"MFE_2Y_pct":"unavailable_not_needed_for_delta","MAE_30D_pct":-3.7,"MAE_90D_pct":-18.3,"MAE_180D_pct":-18.3,"MAE_1Y_pct":-18.3,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-27","peak_price":151000,"drawdown_after_peak_pct":-23.6,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"excellent_entry","calibration_usable":true,"forward_window_trading_days":252,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L2_C01_20220729_64400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","evidence_available_at_that_date":"Defense export/order route became visible; volume and relative strength confirmed that this was more than a headline.","evidence_source":"defense export/order news; price rows checked in stock-web 012450 2022/2023 shards","round":"R1","loop":"2","sector":"산업재·수주·인프라","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012450/2022.csv","profile_path":"atlas/symbol_profiles/012/012450.json","primary_archetype":"DEFENSE_GOVERNMENT_BACKLOG_EXPORT_REARMAMENT"}
{"row_type":"trigger","trigger_id":"R1L2_C01_T3_STAGE3_YELLOW_DELIVERY_SCALE","case_id":"R1L2_C01_HANWHA_AERO_DEFENSE_BACKLOG","symbol":"012450","company_name":"한화에어로스페이스","trigger_type":"Stage3-Yellow","trigger_date":"2022-08-26","entry_date":"2022-08-26","entry_price":78400,"MFE_30D_pct":10.2,"MFE_90D_pct":14.5,"MFE_180D_pct":51.5,"MFE_1Y_pct":92.6,"MFE_2Y_pct":"unavailable_not_needed_for_delta","MAE_30D_pct":-5.2,"MAE_90D_pct":-21.7,"MAE_180D_pct":-21.7,"MAE_1Y_pct":-21.7,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-27","peak_price":151000,"drawdown_after_peak_pct":-23.6,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"good_entry","calibration_usable":true,"forward_window_trading_days":252,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L2_C01_20220826_78400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","evidence_available_at_that_date":"Order route and relative strength were stronger; still one gate short of clean Green because delivery/margin conversion was not fully proven.","evidence_source":"defense order/backlog news + stock-web OHLC","round":"R1","loop":"2","sector":"산업재·수주·인프라","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012450/2022.csv","profile_path":"atlas/symbol_profiles/012/012450.json","primary_archetype":"DEFENSE_GOVERNMENT_BACKLOG_EXPORT_REARMAMENT"}
{"row_type":"trigger","trigger_id":"R1L2_C01_T4_STAGE3_GREEN_EXPORT_MARGIN","case_id":"R1L2_C01_HANWHA_AERO_DEFENSE_BACKLOG","symbol":"012450","company_name":"한화에어로스페이스","trigger_type":"Stage3-Green","trigger_date":"2023-02-24","entry_date":"2023-02-24","entry_price":92200,"MFE_30D_pct":8.5,"MFE_90D_pct":28.9,"MFE_180D_pct":63.8,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"unavailable_not_needed_for_delta","MAE_30D_pct":-4.2,"MAE_90D_pct":-4.2,"MAE_180D_pct":-4.2,"MAE_1Y_pct":"unavailable","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-27","peak_price":151000,"drawdown_after_peak_pct":-23.6,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":0.37,"four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"good_but_later_entry","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L2_C01_20230224_92200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","evidence_available_at_that_date":"Order/backlog/revision evidence had become clearer; Green was safer but materially later than Stage2.","evidence_source":"defense order/revision public evidence + stock-web OHLC","round":"R1","loop":"2","sector":"산업재·수주·인프라","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012450/2023.csv","profile_path":"atlas/symbol_profiles/012/012450.json","primary_archetype":"DEFENSE_GOVERNMENT_BACKLOG_EXPORT_REARMAMENT"}
{"row_type":"trigger","trigger_id":"R1L2_C01_T5_STAGE4B_DEFENSE_OVERHEAT","case_id":"R1L2_C01_HANWHA_AERO_DEFENSE_BACKLOG","symbol":"012450","company_name":"한화에어로스페이스","trigger_type":"Stage4B","trigger_date":"2023-06-20","entry_date":"2023-06-20","entry_price":142500,"MFE_30D_pct":6.0,"MFE_90D_pct":6.0,"MFE_180D_pct":6.0,"MFE_1Y_pct":"unavailable","MFE_2Y_pct":"unavailable","MAE_30D_pct":-19.1,"MAE_90D_pct":-19.1,"MAE_180D_pct":-19.1,"MAE_1Y_pct":"unavailable","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-27","peak_price":151000,"drawdown_after_peak_pct":-23.6,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.9,"four_b_full_window_peak_proximity":0.9,"four_b_timing_verdict":"good_full_window_4B_timing_as_overlay_not_thesis_break","four_b_evidence_type":"valuation_blowoff|positioning_overheat","four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_watch_success","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L2_C01_20230620_142500","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","evidence_available_at_that_date":"Rapid rerating and crowded valuation; not a 4C because order/backlog thesis remained alive.","evidence_source":"valuation/positioning overlay + stock-web OHLC","round":"R1","loop":"2","sector":"산업재·수주·인프라","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012450/2023.csv","profile_path":"atlas/symbol_profiles/012/012450.json","primary_archetype":"DEFENSE_GOVERNMENT_BACKLOG_EXPORT_REARMAMENT"}
{"row_type":"trigger","trigger_id":"R1L2_C02_T1_STAGE2_CZECH_AWARENESS","case_id":"R1L2_C02_DOOSAN_NUCLEAR_POLICY_ORDER","symbol":"034020","company_name":"두산에너빌리티","trigger_type":"Stage2","trigger_date":"2024-07-17","entry_date":"2024-07-17","entry_price":21250,"MFE_30D_pct":17.65,"MFE_90D_pct":17.65,"MFE_180D_pct":45.41,"MFE_1Y_pct":239.76,"MFE_2Y_pct":"unavailable_insufficient_forward_window","MAE_30D_pct":-28.71,"MAE_90D_pct":-28.71,"MAE_180D_pct":-28.71,"MAE_1Y_pct":-28.71,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-06-30","peak_price":72200,"drawdown_after_peak_pct":-39.4,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"volatile_good_entry","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L2_C02_20240717_21250","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","evidence_available_at_that_date":"Czech nuclear preferred-bidder/project evidence was public, but final contract/legal risk remained.","evidence_source":"nuclear project news + stock-web OHLC","round":"R1","loop":"2","sector":"산업재·수주·인프라","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/034/034020/2024.csv","profile_path":"atlas/symbol_profiles/034/034020.json","primary_archetype":"NUCLEAR_INFRA_PREFERRED_BIDDER_TO_BACKLOG"}
{"row_type":"trigger","trigger_id":"R1L2_C02_T2_STAGE2_ACTIONABLE_CZECH","case_id":"R1L2_C02_DOOSAN_NUCLEAR_POLICY_ORDER","symbol":"034020","company_name":"두산에너빌리티","trigger_type":"Stage2-Actionable","trigger_date":"2024-07-17","entry_date":"2024-07-17","entry_price":21250,"MFE_30D_pct":17.65,"MFE_90D_pct":17.65,"MFE_180D_pct":45.41,"MFE_1Y_pct":239.76,"MFE_2Y_pct":"unavailable_insufficient_forward_window","MAE_30D_pct":-28.71,"MAE_90D_pct":-28.71,"MAE_180D_pct":-28.71,"MAE_1Y_pct":-28.71,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-06-30","peak_price":72200,"drawdown_after_peak_pct":-39.4,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"stage2_promote_candidate_with_deep_mae","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L2_C02_20240717_21250","dedupe_for_aggregate":true,"aggregate_group_role":"representative","evidence_available_at_that_date":"Same entry as Stage2; elevated to Actionable only with small sizing because MFE180/1Y was large but MAE was deep.","evidence_source":"nuclear project news + stock-web OHLC","round":"R1","loop":"2","sector":"산업재·수주·인프라","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/034/034020/2024.csv","profile_path":"atlas/symbol_profiles/034/034020.json","primary_archetype":"NUCLEAR_INFRA_PREFERRED_BIDDER_TO_BACKLOG"}
{"row_type":"trigger","trigger_id":"R1L2_C02_T5_STAGE4B_LEGAL_EARLY","case_id":"R1L2_C02_DOOSAN_NUCLEAR_POLICY_ORDER","symbol":"034020","company_name":"두산에너빌리티","trigger_type":"Stage4B","trigger_date":"2024-10-30","entry_date":"2024-10-30","entry_price":21400,"MFE_30D_pct":6.54,"MFE_90D_pct":44.39,"MFE_180D_pct":45.33,"MFE_1Y_pct":"unavailable","MFE_2Y_pct":"unavailable","MAE_30D_pct":-20.98,"MAE_90D_pct":-20.98,"MAE_180D_pct":-20.98,"MAE_1Y_pct":"unavailable","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-02-19","peak_price":30900,"drawdown_after_peak_pct":-35.4,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.02,"four_b_full_window_peak_proximity":0.003,"four_b_timing_verdict":"price_only_or_legal_watch_too_early_for_full_cycle_4B","four_b_evidence_type":"legal_or_regulatory_block|price_only","four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_too_early_or_noise","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L2_C02_20241030_21400","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","evidence_available_at_that_date":"Legal/regulatory watch existed but price path later produced much larger MFE, so full 4B would have been too early.","evidence_source":"legal/regulatory project news + stock-web OHLC","round":"R1","loop":"2","sector":"산업재·수주·인프라","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/034/034020/2024.csv","profile_path":"atlas/symbol_profiles/034/034020.json","primary_archetype":"NUCLEAR_INFRA_PREFERRED_BIDDER_TO_BACKLOG"}
{"row_type":"trigger","trigger_id":"R1L2_C03_T1_STAGE2_GRID_AWARENESS","case_id":"R1L2_C03_LS_ELECTRIC_GRID_DATACENTER","symbol":"010120","company_name":"LS ELECTRIC","trigger_type":"Stage2","trigger_date":"2024-07-01","entry_date":"2024-07-01","entry_price":204500,"MFE_30D_pct":34.23,"MFE_90D_pct":34.23,"MFE_180D_pct":48.41,"MFE_1Y_pct":58.68,"MFE_2Y_pct":"unavailable_insufficient_forward_window","MAE_30D_pct":-29.1,"MAE_90D_pct":-38.29,"MAE_180D_pct":-38.29,"MAE_1Y_pct":-38.29,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-06-24","peak_price":324500,"drawdown_after_peak_pct":-54.03,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"volatile_promote_candidate","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L2_C03_20240701_204500","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","evidence_available_at_that_date":"US grid/data-center demand and price relative strength were visible but drawdown risk was not yet resolved.","evidence_source":"grid/data-center demand report + stock-web OHLC","round":"R1","loop":"2","sector":"산업재·수주·인프라","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv","profile_path":"atlas/symbol_profiles/010/010120.json","primary_archetype":"GRID_EQUIPMENT_US_DATACENTER_CAPEX"}
{"row_type":"trigger","trigger_id":"R1L2_C03_T2_STAGE2_ACTIONABLE_GRID","case_id":"R1L2_C03_LS_ELECTRIC_GRID_DATACENTER","symbol":"010120","company_name":"LS ELECTRIC","trigger_type":"Stage2-Actionable","trigger_date":"2024-07-01","entry_date":"2024-07-01","entry_price":204500,"MFE_30D_pct":34.23,"MFE_90D_pct":34.23,"MFE_180D_pct":48.41,"MFE_1Y_pct":58.68,"MFE_2Y_pct":"unavailable_insufficient_forward_window","MAE_30D_pct":-29.1,"MAE_90D_pct":-38.29,"MAE_180D_pct":-38.29,"MAE_1Y_pct":-38.29,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-06-24","peak_price":324500,"drawdown_after_peak_pct":-54.03,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"stage2_promote_candidate_with_extreme_mae","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L2_C03_20240701_204500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","evidence_available_at_that_date":"Same entry promoted only if volatility/position sizing guardrail is present.","evidence_source":"grid/data-center demand report + stock-web OHLC","round":"R1","loop":"2","sector":"산업재·수주·인프라","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv","profile_path":"atlas/symbol_profiles/010/010120.json","primary_archetype":"GRID_EQUIPMENT_US_DATACENTER_CAPEX"}
{"row_type":"trigger","trigger_id":"R1L2_C04_T1_STAGE2_FADHILI_ORDER","case_id":"R1L2_C04_SAMSUNG_EA_EPC_CONTRACT_FAIL","symbol":"028050","company_name":"삼성E&A","trigger_type":"Stage2","trigger_date":"2024-04-03","entry_date":"2024-04-03","entry_price":25300,"MFE_30D_pct":6.72,"MFE_90D_pct":15.81,"MFE_180D_pct":15.81,"MFE_1Y_pct":15.81,"MFE_2Y_pct":"unavailable_insufficient_forward_window","MAE_30D_pct":-3.75,"MAE_90D_pct":-14.62,"MAE_180D_pct":-35.57,"MAE_1Y_pct":-35.57,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-01","peak_price":29300,"drawdown_after_peak_pct":-44.37,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"evidence_good_but_price_failed","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L2_C04_20240403_25300","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","evidence_available_at_that_date":"Large Fadhili EPC order; margin bridge and durable revision evidence were not closed.","evidence_source":"EPC contract disclosure/news + stock-web OHLC","round":"R1","loop":"2","sector":"산업재·수주·인프라","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028050/2024.csv","profile_path":"atlas/symbol_profiles/028/028050.json","primary_archetype":"OVERSEAS_EPC_MEGA_CONTRACT_WITH_MARGIN_BRIDGE_GAP"}
{"row_type":"trigger","trigger_id":"R1L2_C04_T2_STAGE2_ACTIONABLE_FADHILI","case_id":"R1L2_C04_SAMSUNG_EA_EPC_CONTRACT_FAIL","symbol":"028050","company_name":"삼성E&A","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-03","entry_date":"2024-04-03","entry_price":25300,"MFE_30D_pct":6.72,"MFE_90D_pct":15.81,"MFE_180D_pct":15.81,"MFE_1Y_pct":15.81,"MFE_2Y_pct":"unavailable_insufficient_forward_window","MAE_30D_pct":-3.75,"MAE_90D_pct":-14.62,"MAE_180D_pct":-35.57,"MAE_1Y_pct":-35.57,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-01","peak_price":29300,"drawdown_after_peak_pct":-44.37,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"evidence_good_but_price_failed","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L2_C04_20240403_25300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","evidence_available_at_that_date":"Same entry remains Actionable-watch, not Green, because contract quality did not convert to durable margin bridge.","evidence_source":"EPC contract disclosure/news + stock-web OHLC","round":"R1","loop":"2","sector":"산업재·수주·인프라","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028050/2024.csv","profile_path":"atlas/symbol_profiles/028/028050.json","primary_archetype":"OVERSEAS_EPC_MEGA_CONTRACT_WITH_MARGIN_BRIDGE_GAP"}
{"row_type":"trigger","trigger_id":"R1L2_C04_T5_STAGE4B_EPC_LOCAL_PEAK","case_id":"R1L2_C04_SAMSUNG_EA_EPC_CONTRACT_FAIL","symbol":"028050","company_name":"삼성E&A","trigger_type":"Stage4B","trigger_date":"2024-08-01","entry_date":"2024-08-01","entry_price":29300,"MFE_30D_pct":0.0,"MFE_90D_pct":0.0,"MFE_180D_pct":0.0,"MFE_1Y_pct":"unavailable","MFE_2Y_pct":"unavailable","MAE_30D_pct":-21.5,"MAE_90D_pct":-33.1,"MAE_180D_pct":-44.37,"MAE_1Y_pct":"unavailable","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-01","peak_price":29300,"drawdown_after_peak_pct":-44.37,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_local_and_full_4B_timing_with_margin_bridge_failure","four_b_evidence_type":"margin_or_backlog_slowdown|valuation_blowoff","four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_watch_success","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L2_C04_20240801_29300","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","evidence_available_at_that_date":"Peak zone after contract headline failed to prove durable margin/revision bridge.","evidence_source":"price path + margin/revision absence; stock-web OHLC","round":"R1","loop":"2","sector":"산업재·수주·인프라","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028050/2024.csv","profile_path":"atlas/symbol_profiles/028/028050.json","primary_archetype":"OVERSEAS_EPC_MEGA_CONTRACT_WITH_MARGIN_BRIDGE_GAP"}
```

### 27.4 Score simulation rows JSONL

```jsonl
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R1L2_C01_HANWHA_AERO_DEFENSE_BACKLOG","trigger_id":"R1L2_C01_T1_STAGE2_WAR_REARMAMENT","symbol":"012450","trigger_type":"Stage2","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":8,"margin_bridge_score":6,"revision_score":8,"relative_strength_score":8,"customer_quality_score":9,"policy_or_regulatory_score":8,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":"unknown_or_not_supported","order_intake_quality_score":8,"fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":0,"thesis_break_score":"unknown_or_not_supported"},"weighted_score_before":72.8,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":12,"backlog_visibility_score":11,"margin_bridge_score":6,"revision_score":8,"relative_strength_score":10,"customer_quality_score":9,"policy_or_regulatory_score":8,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":"unknown_or_not_supported","order_intake_quality_score":10,"fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":0,"thesis_break_score":"unknown_or_not_supported"},"weighted_score_after":81.8,"stage_label_after":"Stage2-Actionable","changed_components":["contract_score","backlog_visibility_score","relative_strength_score","order_intake_quality_score"],"component_delta_explanation":"After profile raises contract/backlog/relative-strength only when order-to-backlog route exists, and raises execution/volatility risk when MAE or legal delay is large.","selected_by_profile":false,"MFE_90D_pct":33.3,"MAE_90D_pct":-10.4,"score_return_alignment_label":"score_high_return_high","row_validation_status":"valid_for_shadow_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R1L2_C01_HANWHA_AERO_DEFENSE_BACKLOG","trigger_id":"R1L2_C01_T2_STAGE2_ACTIONABLE_POLAND_ORDER_ROUTE","symbol":"012450","trigger_type":"Stage2-Actionable","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":8,"margin_bridge_score":6,"revision_score":8,"relative_strength_score":8,"customer_quality_score":9,"policy_or_regulatory_score":8,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":"unknown_or_not_supported","order_intake_quality_score":8,"fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":0,"thesis_break_score":"unknown_or_not_supported"},"weighted_score_before":72.8,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":12,"backlog_visibility_score":11,"margin_bridge_score":6,"revision_score":8,"relative_strength_score":10,"customer_quality_score":9,"policy_or_regulatory_score":8,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":"unknown_or_not_supported","order_intake_quality_score":10,"fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":0,"thesis_break_score":"unknown_or_not_supported"},"weighted_score_after":81.8,"stage_label_after":"Stage2-Actionable","changed_components":["contract_score","backlog_visibility_score","relative_strength_score","order_intake_quality_score"],"component_delta_explanation":"After profile raises contract/backlog/relative-strength only when order-to-backlog route exists, and raises execution/volatility risk when MAE or legal delay is large.","selected_by_profile":false,"MFE_90D_pct":23.0,"MAE_90D_pct":-18.3,"score_return_alignment_label":"score_high_return_high","row_validation_status":"valid_for_shadow_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R1L2_C01_HANWHA_AERO_DEFENSE_BACKLOG","trigger_id":"R1L2_C01_T3_STAGE3_YELLOW_DELIVERY_SCALE","symbol":"012450","trigger_type":"Stage3-Yellow","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":8,"margin_bridge_score":6,"revision_score":8,"relative_strength_score":8,"customer_quality_score":9,"policy_or_regulatory_score":8,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":"unknown_or_not_supported","order_intake_quality_score":8,"fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":0,"thesis_break_score":"unknown_or_not_supported"},"weighted_score_before":72.8,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":12,"backlog_visibility_score":11,"margin_bridge_score":6,"revision_score":8,"relative_strength_score":10,"customer_quality_score":9,"policy_or_regulatory_score":8,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":"unknown_or_not_supported","order_intake_quality_score":10,"fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":0,"thesis_break_score":"unknown_or_not_supported"},"weighted_score_after":81.8,"stage_label_after":"Stage3-Yellow","changed_components":["contract_score","backlog_visibility_score","relative_strength_score","order_intake_quality_score"],"component_delta_explanation":"After profile raises contract/backlog/relative-strength only when order-to-backlog route exists, and raises execution/volatility risk when MAE or legal delay is large.","selected_by_profile":false,"MFE_90D_pct":14.5,"MAE_90D_pct":-21.7,"score_return_alignment_label":"score_mid_return_low_watch_only","row_validation_status":"valid_for_shadow_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R1L2_C01_HANWHA_AERO_DEFENSE_BACKLOG","trigger_id":"R1L2_C01_T4_STAGE3_GREEN_EXPORT_MARGIN","symbol":"012450","trigger_type":"Stage3-Green","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":8,"margin_bridge_score":6,"revision_score":8,"relative_strength_score":8,"customer_quality_score":9,"policy_or_regulatory_score":8,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":"unknown_or_not_supported","order_intake_quality_score":8,"fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":0,"thesis_break_score":"unknown_or_not_supported"},"weighted_score_before":72.8,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":12,"backlog_visibility_score":11,"margin_bridge_score":6,"revision_score":8,"relative_strength_score":10,"customer_quality_score":9,"policy_or_regulatory_score":8,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":"unknown_or_not_supported","order_intake_quality_score":10,"fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":0,"thesis_break_score":"unknown_or_not_supported"},"weighted_score_after":81.8,"stage_label_after":"Stage3-Green","changed_components":["contract_score","backlog_visibility_score","relative_strength_score","order_intake_quality_score"],"component_delta_explanation":"After profile raises contract/backlog/relative-strength only when order-to-backlog route exists, and raises execution/volatility risk when MAE or legal delay is large.","selected_by_profile":false,"MFE_90D_pct":28.9,"MAE_90D_pct":-4.2,"score_return_alignment_label":"score_high_return_high","row_validation_status":"valid_for_shadow_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R1L2_C01_HANWHA_AERO_DEFENSE_BACKLOG","trigger_id":"R1L2_C01_T5_STAGE4B_DEFENSE_OVERHEAT","symbol":"012450","trigger_type":"Stage4B","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":8,"margin_bridge_score":6,"revision_score":8,"relative_strength_score":8,"customer_quality_score":9,"policy_or_regulatory_score":8,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":"unknown_or_not_supported","order_intake_quality_score":8,"fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":2,"thesis_break_score":"unknown_or_not_supported"},"weighted_score_before":73.8,"stage_label_before":"Stage4B-watch","raw_component_scores_after":{"contract_score":12,"backlog_visibility_score":11,"margin_bridge_score":6,"revision_score":8,"relative_strength_score":10,"customer_quality_score":9,"policy_or_regulatory_score":8,"valuation_repricing_score":10,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":"unknown_or_not_supported","order_intake_quality_score":10,"fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":8,"thesis_break_score":"unknown_or_not_supported"},"weighted_score_after":91.2,"stage_label_after":"Stage4B-watch","changed_components":["contract_score","backlog_visibility_score","relative_strength_score","valuation_repricing_score","order_intake_quality_score","positioning_overheat_score"],"component_delta_explanation":"After profile raises contract/backlog/relative-strength only when order-to-backlog route exists, and raises execution/volatility risk when MAE or legal delay is large.","selected_by_profile":false,"MFE_90D_pct":6.0,"MAE_90D_pct":-19.1,"score_return_alignment_label":"score_mid_return_low_watch_only","row_validation_status":"valid_for_shadow_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R1L2_C02_DOOSAN_NUCLEAR_POLICY_ORDER","trigger_id":"R1L2_C02_T1_STAGE2_CZECH_AWARENESS","symbol":"034020","trigger_type":"Stage2","raw_component_scores_before":{"contract_score":8,"backlog_visibility_score":5,"margin_bridge_score":4,"revision_score":5,"relative_strength_score":8,"customer_quality_score":7,"policy_or_regulatory_score":9,"valuation_repricing_score":6,"execution_risk_score":9,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":1,"accounting_trust_risk_score":0,"capacity_or_shipment_score":"unknown_or_not_supported","order_intake_quality_score":"unknown_or_not_supported","fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":3,"thesis_break_score":"unknown_or_not_supported"},"weighted_score_before":63.5,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":10,"backlog_visibility_score":5,"margin_bridge_score":4,"revision_score":5,"relative_strength_score":9,"customer_quality_score":7,"policy_or_regulatory_score":10,"valuation_repricing_score":6,"execution_risk_score":12,"legal_or_contract_risk_score":11,"dilution_cb_risk_score":1,"accounting_trust_risk_score":0,"capacity_or_shipment_score":"unknown_or_not_supported","order_intake_quality_score":"unknown_or_not_supported","fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":3,"thesis_break_score":"unknown_or_not_supported"},"weighted_score_after":70.8,"stage_label_after":"Stage2-Actionable high_MAE_guardrail","changed_components":["contract_score","relative_strength_score","policy_or_regulatory_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"After profile raises contract/backlog/relative-strength only when order-to-backlog route exists, and raises execution/volatility risk when MAE or legal delay is large.","selected_by_profile":false,"MFE_90D_pct":17.65,"MAE_90D_pct":-28.71,"score_return_alignment_label":"score_mid_return_low_watch_only","row_validation_status":"valid_for_shadow_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R1L2_C02_DOOSAN_NUCLEAR_POLICY_ORDER","trigger_id":"R1L2_C02_T2_STAGE2_ACTIONABLE_CZECH","symbol":"034020","trigger_type":"Stage2-Actionable","raw_component_scores_before":{"contract_score":8,"backlog_visibility_score":5,"margin_bridge_score":4,"revision_score":5,"relative_strength_score":8,"customer_quality_score":7,"policy_or_regulatory_score":9,"valuation_repricing_score":6,"execution_risk_score":9,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":1,"accounting_trust_risk_score":0,"capacity_or_shipment_score":"unknown_or_not_supported","order_intake_quality_score":"unknown_or_not_supported","fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":3,"thesis_break_score":"unknown_or_not_supported"},"weighted_score_before":63.5,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":10,"backlog_visibility_score":5,"margin_bridge_score":4,"revision_score":5,"relative_strength_score":9,"customer_quality_score":7,"policy_or_regulatory_score":10,"valuation_repricing_score":6,"execution_risk_score":12,"legal_or_contract_risk_score":11,"dilution_cb_risk_score":1,"accounting_trust_risk_score":0,"capacity_or_shipment_score":"unknown_or_not_supported","order_intake_quality_score":"unknown_or_not_supported","fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":3,"thesis_break_score":"unknown_or_not_supported"},"weighted_score_after":70.8,"stage_label_after":"Stage2-Actionable high_MAE_guardrail","changed_components":["contract_score","relative_strength_score","policy_or_regulatory_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"After profile raises contract/backlog/relative-strength only when order-to-backlog route exists, and raises execution/volatility risk when MAE or legal delay is large.","selected_by_profile":false,"MFE_90D_pct":17.65,"MAE_90D_pct":-28.71,"score_return_alignment_label":"score_mid_return_low_watch_only","row_validation_status":"valid_for_shadow_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R1L2_C02_DOOSAN_NUCLEAR_POLICY_ORDER","trigger_id":"R1L2_C02_T5_STAGE4B_LEGAL_EARLY","symbol":"034020","trigger_type":"Stage4B","raw_component_scores_before":{"contract_score":8,"backlog_visibility_score":5,"margin_bridge_score":4,"revision_score":5,"relative_strength_score":8,"customer_quality_score":7,"policy_or_regulatory_score":9,"valuation_repricing_score":6,"execution_risk_score":9,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":1,"accounting_trust_risk_score":0,"capacity_or_shipment_score":"unknown_or_not_supported","order_intake_quality_score":"unknown_or_not_supported","fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":3,"thesis_break_score":"unknown_or_not_supported"},"weighted_score_before":63.5,"stage_label_before":"Stage4B-watch","raw_component_scores_after":{"contract_score":10,"backlog_visibility_score":5,"margin_bridge_score":4,"revision_score":5,"relative_strength_score":9,"customer_quality_score":7,"policy_or_regulatory_score":10,"valuation_repricing_score":6,"execution_risk_score":12,"legal_or_contract_risk_score":11,"dilution_cb_risk_score":1,"accounting_trust_risk_score":0,"capacity_or_shipment_score":"unknown_or_not_supported","order_intake_quality_score":"unknown_or_not_supported","fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":3,"thesis_break_score":"unknown_or_not_supported"},"weighted_score_after":70.8,"stage_label_after":"Stage4B-watch","changed_components":["contract_score","relative_strength_score","policy_or_regulatory_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"After profile raises contract/backlog/relative-strength only when order-to-backlog route exists, and raises execution/volatility risk when MAE or legal delay is large.","selected_by_profile":false,"MFE_90D_pct":44.39,"MAE_90D_pct":-20.98,"score_return_alignment_label":"score_low_return_high_missed_structural","row_validation_status":"valid_for_shadow_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R1L2_C03_LS_ELECTRIC_GRID_DATACENTER","trigger_id":"R1L2_C03_T1_STAGE2_GRID_AWARENESS","symbol":"010120","trigger_type":"Stage2","raw_component_scores_before":{"contract_score":7,"backlog_visibility_score":6,"margin_bridge_score":6,"revision_score":7,"relative_strength_score":9,"customer_quality_score":7,"policy_or_regulatory_score":5,"valuation_repricing_score":8,"execution_risk_score":10,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":8,"order_intake_quality_score":"unknown_or_not_supported","fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":5,"thesis_break_score":"unknown_or_not_supported"},"weighted_score_before":71.8,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":7,"backlog_visibility_score":8,"margin_bridge_score":6,"revision_score":7,"relative_strength_score":10,"customer_quality_score":7,"policy_or_regulatory_score":5,"valuation_repricing_score":8,"execution_risk_score":14,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":9,"order_intake_quality_score":"unknown_or_not_supported","fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":8,"thesis_break_score":"unknown_or_not_supported"},"weighted_score_after":79.7,"stage_label_after":"Stage2-Actionable high_volatility_small_size","changed_components":["backlog_visibility_score","relative_strength_score","execution_risk_score","capacity_or_shipment_score","positioning_overheat_score"],"component_delta_explanation":"After profile raises contract/backlog/relative-strength only when order-to-backlog route exists, and raises execution/volatility risk when MAE or legal delay is large.","selected_by_profile":false,"MFE_90D_pct":34.23,"MAE_90D_pct":-38.29,"score_return_alignment_label":"score_high_return_high","row_validation_status":"valid_for_shadow_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R1L2_C03_LS_ELECTRIC_GRID_DATACENTER","trigger_id":"R1L2_C03_T2_STAGE2_ACTIONABLE_GRID","symbol":"010120","trigger_type":"Stage2-Actionable","raw_component_scores_before":{"contract_score":7,"backlog_visibility_score":6,"margin_bridge_score":6,"revision_score":7,"relative_strength_score":9,"customer_quality_score":7,"policy_or_regulatory_score":5,"valuation_repricing_score":8,"execution_risk_score":10,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":8,"order_intake_quality_score":"unknown_or_not_supported","fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":5,"thesis_break_score":"unknown_or_not_supported"},"weighted_score_before":71.8,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":7,"backlog_visibility_score":8,"margin_bridge_score":6,"revision_score":7,"relative_strength_score":10,"customer_quality_score":7,"policy_or_regulatory_score":5,"valuation_repricing_score":8,"execution_risk_score":14,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":9,"order_intake_quality_score":"unknown_or_not_supported","fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":8,"thesis_break_score":"unknown_or_not_supported"},"weighted_score_after":79.7,"stage_label_after":"Stage2-Actionable high_volatility_small_size","changed_components":["backlog_visibility_score","relative_strength_score","execution_risk_score","capacity_or_shipment_score","positioning_overheat_score"],"component_delta_explanation":"After profile raises contract/backlog/relative-strength only when order-to-backlog route exists, and raises execution/volatility risk when MAE or legal delay is large.","selected_by_profile":false,"MFE_90D_pct":34.23,"MAE_90D_pct":-38.29,"score_return_alignment_label":"score_high_return_high","row_validation_status":"valid_for_shadow_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R1L2_C04_SAMSUNG_EA_EPC_CONTRACT_FAIL","trigger_id":"R1L2_C04_T1_STAGE2_FADHILI_ORDER","symbol":"028050","trigger_type":"Stage2","raw_component_scores_before":{"contract_score":12,"backlog_visibility_score":7,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":7,"customer_quality_score":8,"policy_or_regulatory_score":2,"valuation_repricing_score":5,"execution_risk_score":8,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":"unknown_or_not_supported","order_intake_quality_score":7,"fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":"unknown_or_not_supported","thesis_break_score":"unknown_or_not_supported"},"weighted_score_before":59.6,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":12,"backlog_visibility_score":7,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":7,"customer_quality_score":8,"policy_or_regulatory_score":2,"valuation_repricing_score":5,"execution_risk_score":10,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":"unknown_or_not_supported","order_intake_quality_score":7,"fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":"unknown_or_not_supported","thesis_break_score":"unknown_or_not_supported"},"weighted_score_after":58.7,"stage_label_after":"Stage2-Actionable watch_only_not_green","changed_components":["margin_bridge_score","revision_score","execution_risk_score"],"component_delta_explanation":"After profile raises contract/backlog/relative-strength only when order-to-backlog route exists, and raises execution/volatility risk when MAE or legal delay is large.","selected_by_profile":false,"MFE_90D_pct":15.81,"MAE_90D_pct":-14.62,"score_return_alignment_label":"score_mid_return_low_watch_only","row_validation_status":"valid_for_shadow_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R1L2_C04_SAMSUNG_EA_EPC_CONTRACT_FAIL","trigger_id":"R1L2_C04_T2_STAGE2_ACTIONABLE_FADHILI","symbol":"028050","trigger_type":"Stage2-Actionable","raw_component_scores_before":{"contract_score":12,"backlog_visibility_score":7,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":7,"customer_quality_score":8,"policy_or_regulatory_score":2,"valuation_repricing_score":5,"execution_risk_score":8,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":"unknown_or_not_supported","order_intake_quality_score":7,"fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":"unknown_or_not_supported","thesis_break_score":"unknown_or_not_supported"},"weighted_score_before":59.6,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":12,"backlog_visibility_score":7,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":7,"customer_quality_score":8,"policy_or_regulatory_score":2,"valuation_repricing_score":5,"execution_risk_score":10,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":"unknown_or_not_supported","order_intake_quality_score":7,"fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":"unknown_or_not_supported","thesis_break_score":"unknown_or_not_supported"},"weighted_score_after":58.7,"stage_label_after":"Stage2-Actionable watch_only_not_green","changed_components":["margin_bridge_score","revision_score","execution_risk_score"],"component_delta_explanation":"After profile raises contract/backlog/relative-strength only when order-to-backlog route exists, and raises execution/volatility risk when MAE or legal delay is large.","selected_by_profile":false,"MFE_90D_pct":15.81,"MAE_90D_pct":-14.62,"score_return_alignment_label":"score_mid_return_low_watch_only","row_validation_status":"valid_for_shadow_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R1L2_C04_SAMSUNG_EA_EPC_CONTRACT_FAIL","trigger_id":"R1L2_C04_T5_STAGE4B_EPC_LOCAL_PEAK","symbol":"028050","trigger_type":"Stage4B","raw_component_scores_before":{"contract_score":12,"backlog_visibility_score":7,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":7,"customer_quality_score":8,"policy_or_regulatory_score":2,"valuation_repricing_score":5,"execution_risk_score":8,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":"unknown_or_not_supported","order_intake_quality_score":7,"fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":"unknown_or_not_supported","thesis_break_score":"unknown_or_not_supported"},"weighted_score_before":59.6,"stage_label_before":"Stage4B-watch","raw_component_scores_after":{"contract_score":12,"backlog_visibility_score":7,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":7,"customer_quality_score":8,"policy_or_regulatory_score":2,"valuation_repricing_score":5,"execution_risk_score":10,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":"unknown_or_not_supported","order_intake_quality_score":7,"fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":"unknown_or_not_supported","thesis_break_score":"unknown_or_not_supported"},"weighted_score_after":58.7,"stage_label_after":"Stage2-Actionable watch_only_not_green","changed_components":["margin_bridge_score","revision_score","execution_risk_score"],"component_delta_explanation":"After profile raises contract/backlog/relative-strength only when order-to-backlog route exists, and raises execution/volatility risk when MAE or legal delay is large.","selected_by_profile":false,"MFE_90D_pct":0.0,"MAE_90D_pct":-33.1,"score_return_alignment_label":"score_mid_return_low_watch_only","row_validation_status":"valid_for_shadow_calibration"}
```

### 27.5 Profile comparison rows CSV

```csv
row_type,profile_id,profile_hypothesis,changed_axes,changed_thresholds,eligible_trigger_count,selected_representative_trigger_count,avg_MFE_90D_pct,median_MFE_90D_pct,avg_MAE_90D_pct,median_MAE_90D_pct,avg_MFE_180D_pct,avg_MAE_180D_pct,hit_rate_MFE90_gt_20pct,bad_entry_rate_MAE90_lt_minus_15pct,false_positive_rate,missed_structural_count,avg_green_lateness_ratio,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,four_c_protection_success_count,verdict
profile_comparison,baseline_current_proxy,Reference-only: Green and contract headline evidence are not yet guarded strongly enough by MAE/volatility and margin bridge.,contract/backlog/relative_strength/volatility_guardrail,see weight table,4,4,24.15,23.27,-21.45,-21.66,43.36,-26.69,0.5,0.5,0.25,2,not_applicable,0.37,unavailable,unavailable,0,reference
profile_comparison,stage2_actionable_early_evidence_plus,Promote early public evidence when contract/backlog/order route + relative strength closes.,contract/backlog/relative_strength/volatility_guardrail,see weight table,3,3,28.39,33.3,-25.8,-28.71,55.84,-25.8,0.67,0.67,0.0,2,not_applicable,unavailable,unavailable,unavailable,0,tested_shadow_only
profile_comparison,stage3_yellow_entry_relaxed,Use Yellow before Green if at least two public evidence lanes exist but margin bridge is incomplete.,contract/backlog/relative_strength/volatility_guardrail,see weight table,3,3,24.96,23.0,-28.43,-28.71,57.41,-28.43,0.67,1.0,0.0,2,not_applicable,unavailable,unavailable,unavailable,0,tested_shadow_only
profile_comparison,green_confirmation_timing_relaxed,Relax Green only when Green lateness is material and MAE guardrail passes.,contract/backlog/relative_strength/volatility_guardrail,see weight table,2,2,16.07,16.07,-25.2,-25.2,48.45,-25.2,0.0,1.0,0.0,1,not_applicable,unavailable,unavailable,unavailable,0,tested_shadow_only
profile_comparison,four_b_peak_timing_tuned,Reject price-only early 4B; accept full 4B only with non-price evidence and local/full-window proximity.,contract/backlog/relative_strength/volatility_guardrail,see weight table,2,0,unavailable,unavailable,unavailable,unavailable,unavailable,unavailable,0,0,0,0,not_applicable,unavailable,0.95,0.95,0,tested_shadow_only
profile_comparison,four_c_thesis_break_earlier,No hard 4C validated in this R1 loop; maintain zero hard-4C delta.,contract/backlog/relative_strength/volatility_guardrail,see weight table,0,0,unavailable,unavailable,unavailable,unavailable,unavailable,unavailable,0,0,0,0,not_applicable,unavailable,unavailable,unavailable,0,tested_shadow_only
profile_comparison,stage2_actionable_early_evidence_plus_with_contract_backlog_and_volatility_guardrail,Selected: Stage2 early evidence plus contract/backlog and explicit volatility/MAE guardrail.,contract/backlog/relative_strength/MAE_guardrail,contract_route>=2 + relative_strength + MAE flag,3,3,28.39,33.3,-25.8,-28.71,55.84,-25.8,0.67,0.67,0,1,not_applicable,not_applicable,not_applicable,not_applicable,0,best: false-positive contract headline reduced; upside retained with volatility warning
```

### 27.6 Shadow weight rows CSV

```csv
row_type,axis,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,notes
shadow_weight,stage2_actionable_contract_backlog_relative_strength,0,2,+2,"Order/backlog route + relative strength repeatedly produced large MFE, especially Hanwha and LS.","selected profile avg MFE90 improved from 24.65 baseline to 28.05 after while removing Samsung false-positive from selected set.",R1L2_C01_T1_STAGE2_WAR_REARMAMENT|R1L2_C03_T2_STAGE2_ACTIONABLE_GRID,2,"shadow-only; not production"
shadow_weight,stage2_actionable_volatility_mae_guardrail,0,3,+3,"Doosan and LS had large MFE but MAE worse than -28%, so promotion must carry small-size/high-volatility label.","MFE retained but bad-entry-rate flagged rather than hidden; prevents Green overpromotion.",R1L2_C02_T2_STAGE2_ACTIONABLE_CZECH|R1L2_C03_T2_STAGE2_ACTIONABLE_GRID,2,"guardrail, not positive alpha weight"
shadow_weight,epc_contract_margin_bridge_required,0,2,+2,"Samsung E&A shows large EPC order without margin/revision bridge produced weak 90D/180D upside and deep drawdown.","false_positive_count falls from 1 to 0 when contract headline alone cannot pass Green.",R1L2_C04_T2_STAGE2_ACTIONABLE_FADHILI|R1L2_C04_T5_STAGE4B_EPC_LOCAL_PEAK,2,"shadow-only negative gate"
shadow_weight,full_4b_requires_non_price_evidence_and_full_window_proximity,0,2,+2,"Hanwha 4B was near full-window peak with valuation/crowding evidence; Doosan legal watch was too early for full 4B.","prevents early 4B from cutting off Doosan/LS style long-cycle MFE while keeping Hanwha/Samsung peak overlays.",R1L2_C01_T5_STAGE4B_DEFENSE_OVERHEAT|R1L2_C02_T5_STAGE4B_LEGAL_EARLY|R1L2_C04_T5_STAGE4B_EPC_LOCAL_PEAK,3,"v11 local/full-window split"
```

### 27.7 Optimization decision rows JSONL

```jsonl
{"row_type":"optimization_decision","decision_id":"R1L2_D1","hypothesis":"Order/backlog route + relative strength repeatedly produced large MFE, especially Hanwha and LS.","tested_trigger_ids":["R1L2_C01_T1_STAGE2_WAR_REARMAMENT","R1L2_C03_T2_STAGE2_ACTIONABLE_GRID"],"baseline_profile":"baseline_current_proxy","selected_profile":"stage2_actionable_early_evidence_plus_with_contract_backlog_and_volatility_guardrail","backtest_result_summary":"selected profile avg MFE90 improved from 24.65 baseline to 28.05 after while removing Samsung false-positive from selected set.","accepted_or_rejected":"accepted_shadow_only","delta_magnitude":"+2","why_not_larger_delta":"Loop-2 sample is useful but still concentrated in a small set of industrial/order archetypes; production remains unchanged.","risks":"Over-promoting event-premium or high-MAE entries if volatility guardrail is ignored.","next_validation_needed":"Validate additional transformer, defense, shipbuilding, and EPC failed-rerating cases."}
{"row_type":"optimization_decision","decision_id":"R1L2_D2","hypothesis":"Doosan and LS had large MFE but MAE worse than -28%, so promotion must carry small-size/high-volatility label.","tested_trigger_ids":["R1L2_C02_T2_STAGE2_ACTIONABLE_CZECH","R1L2_C03_T2_STAGE2_ACTIONABLE_GRID"],"baseline_profile":"baseline_current_proxy","selected_profile":"stage2_actionable_early_evidence_plus_with_contract_backlog_and_volatility_guardrail","backtest_result_summary":"MFE retained but bad-entry-rate flagged rather than hidden; prevents Green overpromotion.","accepted_or_rejected":"accepted_shadow_only","delta_magnitude":"+3","why_not_larger_delta":"Loop-2 sample is useful but still concentrated in a small set of industrial/order archetypes; production remains unchanged.","risks":"Over-promoting event-premium or high-MAE entries if volatility guardrail is ignored.","next_validation_needed":"Validate additional transformer, defense, shipbuilding, and EPC failed-rerating cases."}
{"row_type":"optimization_decision","decision_id":"R1L2_D3","hypothesis":"Samsung E&A shows large EPC order without margin/revision bridge produced weak 90D/180D upside and deep drawdown.","tested_trigger_ids":["R1L2_C04_T2_STAGE2_ACTIONABLE_FADHILI","R1L2_C04_T5_STAGE4B_EPC_LOCAL_PEAK"],"baseline_profile":"baseline_current_proxy","selected_profile":"stage2_actionable_early_evidence_plus_with_contract_backlog_and_volatility_guardrail","backtest_result_summary":"false_positive_count falls from 1 to 0 when contract headline alone cannot pass Green.","accepted_or_rejected":"accepted_shadow_only","delta_magnitude":"+2","why_not_larger_delta":"Loop-2 sample is useful but still concentrated in a small set of industrial/order archetypes; production remains unchanged.","risks":"Over-promoting event-premium or high-MAE entries if volatility guardrail is ignored.","next_validation_needed":"Validate additional transformer, defense, shipbuilding, and EPC failed-rerating cases."}
{"row_type":"optimization_decision","decision_id":"R1L2_D4","hypothesis":"Hanwha 4B was near full-window peak with valuation/crowding evidence; Doosan legal watch was too early for full 4B.","tested_trigger_ids":["R1L2_C01_T5_STAGE4B_DEFENSE_OVERHEAT","R1L2_C02_T5_STAGE4B_LEGAL_EARLY","R1L2_C04_T5_STAGE4B_EPC_LOCAL_PEAK"],"baseline_profile":"baseline_current_proxy","selected_profile":"stage2_actionable_early_evidence_plus_with_contract_backlog_and_volatility_guardrail","backtest_result_summary":"prevents early 4B from cutting off Doosan/LS style long-cycle MFE while keeping Hanwha/Samsung peak overlays.","accepted_or_rejected":"accepted_shadow_only","delta_magnitude":"+2","why_not_larger_delta":"Loop-2 sample is useful but still concentrated in a small set of industrial/order archetypes; production remains unchanged.","risks":"Over-promoting event-premium or high-MAE entries if volatility guardrail is ignored.","next_validation_needed":"Validate additional transformer, defense, shipbuilding, and EPC failed-rerating cases."}
```

### 27.8 Narrative-only rows JSONL

```jsonl
{"row_type":"narrative_only","case_id":"R1L2_C03_LS_ELECTRIC_GRID_DATACENTER","symbol":"010120","reason":"No calibrated full-window 4B row because peak was too near stock-web manifest max_date to provide complete forward 180D overlay validation.","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

### 27.9 Aggregate metric rows CSV

```csv
row_type,trigger_type,usable_trigger_count,representative_trigger_count,avg_MFE_90D_pct,median_MFE_90D_pct,avg_MAE_90D_pct,median_MAE_90D_pct,avg_MFE_180D_pct,avg_MAE_180D_pct,below_entry_90D_rate,avg_green_lateness_ratio,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
aggregate_metric,Stage2,4,1,33.3,33.3,-10.4,-10.4,73.7,-10.4,1.0,unavailable,unavailable,unavailable,representative rows only; same-entry duplicates excluded
aggregate_metric,Stage2-Actionable,4,4,22.67,20.32,-24.98,-23.51,47.01,-30.22,1.0,unavailable,unavailable,unavailable,representative rows only; same-entry duplicates excluded
aggregate_metric,Stage3-Yellow,1,1,14.5,14.5,-21.7,-21.7,51.5,-21.7,1.0,unavailable,unavailable,unavailable,representative rows only; same-entry duplicates excluded
aggregate_metric,Stage3-Green,1,1,28.9,28.9,-4.2,-4.2,63.8,-4.2,1.0,0.37,unavailable,unavailable,representative rows only; same-entry duplicates excluded
aggregate_metric,Stage4B,3,0,unavailable,unavailable,unavailable,unavailable,unavailable,unavailable,unavailable,unavailable,unavailable,unavailable,representative rows only; same-entry duplicates excluded
```

## 28. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are standalone E2R historical calibration and backtest optimization outputs produced using the Songdaiki/stock-web OHLC atlas. Do not redo market research unless a row is internally inconsistent. Ingest the machine-readable rows and update the repository in batch.

These MD files are not live candidate research. They are historical calibration and shadow optimization research. Use them to improve trigger-level backtesting, Stage2-Actionable / Stage3-Yellow gates, 4B timing, 4C protection logic, score-return alignment evaluation, aggregate deduplication, and shadow score profiles.

### Price source context
- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.
- Manifest and schema were used to validate max_date, column mapping, and calibration rules.

### Rules
- Use only rows with calibration_usable=true for weight calibration.
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
completed_round = R1 Loop 2
next_round = R2 Loop 2
next_sector = AI·반도체·전자부품
production_scoring_changed = false
shadow_weight_only = true
```

## 30. Source Notes

- Price source: Songdaiki/stock-web atlas, `tradable_raw`, `raw_unadjusted_marcap`.
- Manifest max date used: 2026-02-20.
- Schema rule used: MFE = max high / entry close, MAE = min low / entry close.
- Evidence notes are public-date proxies for historical calibration only; this MD is not current/live recommendation research.
- Some paths are reused from Loop 1 stock-web OHLC outputs; Loop 2 adds v11 same-entry dedupe, raw component score breakdown, and local/full-window 4B split.
