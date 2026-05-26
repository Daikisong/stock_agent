# E2R Stock-Web Historical Calibration / Backtest Optimization Round

## 0. Research Metadata

```text
research_session = historical_calibration_after_stock_web_ohlc_breakthrough
round = R10
loop = 1
sector = 건설·부동산·건자재
production_scoring_changed = false
shadow_weight_only = true
stock_agent_repo_access_allowed = false
stock_web_price_atlas_access_required = true
output_file = e2r_stock_web_historical_calibration_round_R10_loop_1_construction_realestate_materials_research.md
```

이 MD는 `stock_agent` 레포를 열지 않고 작성한 standalone historical calibration 파일이다. 가격은 Songdaiki/stock-web의 `tradable_raw` OHLCV를 사용했다. Manifest는 `max_date=2026-02-20`, `price_adjustment_status=raw_unadjusted_marcap`, `tradable_row_count=14354401`을 기록하고, schema는 tradable shard column과 MFE/MAE 산식을 정의한다. fileciteturn357file0 fileciteturn358file0

## 1. Round Scope

R10은 건설·부동산·건자재다. 이번 loop는 해외 EPC/원전 수주가 실제 리레이팅으로 이어지는 조건과, 건설 안전사고가 hard 4C로 작동하는 조건을 검증한다. 핵심은 “계약이 있었다”가 아니라 “수주 품질, margin/revision bridge, safety/license risk가 가격경로와 맞았는가”다.

## 2. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

확인한 profile:

- 삼성E&A 028050은 chosen R10 window에 180D corporate-action contamination이 없다. fileciteturn359file0 fileciteturn360file0
- 현대건설 000720은 chosen 2024~2025 window에 profile상 과거 corporate-action candidate와 겹치지 않는다. fileciteturn361file0
- GS건설 006360은 chosen 2024~2025 window에 profile상 2014 이후 corporate-action candidate와 겹치지 않는다. fileciteturn362file0
- HDC현대산업개발 294870은 2020-03-26 candidate 이후 2022 accident window가 clean하다. fileciteturn363file0

## 3. Historical Eligibility Gate

모든 calibration trigger는 stock-web tradable shard 안에서 entry row가 있고, 최소 180 trading days forward window를 가진다. 2Y는 현대건설/GS/삼성E&A의 2024~2025 trigger에서 manifest max_date 때문에 unavailable 처리했다. 계산 가능한 값만 기록했다.

## 4. Canonical Archetypes Tested

| archetype | tested case | verdict |
|---|---|---|
| NUCLEAR_EPC_EXPORT_LONGLAG_CONSTRUCTION_RERATING | 현대건설 | preferred bidder는 long-lag Stage2, Green은 확인되나 늦고 volatile |
| OVERSEAS_EPC_CONTRACT_RECOVERY_AFTER_SAFETY_DISCOUNT | GS건설 | Stage2-Actionable 승격 가능 |
| MEGA_EPC_CONTRACT_WITHOUT_MARGIN_RERATING | 삼성E&A | contract-only Green guardrail 필요 |
| CONSTRUCTION_SAFETY_ACCIDENT_LICENSE_REPUTATION_BREAK | HDC현대산업개발 | hard 4C 조기감지 유효 |

## 5. Case Selection Summary

| case_id | symbol | company | case_type | best_trigger | notes |
| --- | --- | --- | --- | --- | --- |
| R10L1_HDEC_000720_CZECH_NUCLEAR_LONGLAG | 000720 | 현대건설 | long_lag_structural_success_candidate | R10L1_HDEC_T1 | Czech nuclear preferred bidder는 즉시 rerating보다 long-lag 구조였다. Stage2 이후 1Y MFE는 컸지만 90D/180D MAE도 깊었다. |
| R10L1_GSENC_006360_FADHILI_RECOVERY | 006360 | GS건설 | structural_success_candidate_after_safety_discount | R10L1_GSENC_T2 | Fadhili EPC 수주가 안전사고 discount 이후 recovery evidence로 작동했다. 같은 contract라도 discount 상태와 상대강도가 결합될 때 actionability가 커졌다. |
| R10L1_SAMSUNGEA_028050_FADHILI_CONTRACT_FAILED | 028050 | 삼성E&A | evidence_good_but_price_failed | R10L1_SEA_T2 | 대형 Fadhili 수주는 있었지만 margin/revision bridge가 닫히지 않으면 full Stage2-Actionable/Green으로 올리면 실패할 수 있다. |
| R10L1_HDC_294870_GWANGJU_COLLAPSE_4C | 294870 | HDC현대산업개발 | hard_4c_thesis_break | R10L1_HDC_T6A | Gwangju Hwajeong I-Park collapse는 건설사 safety/license/reputation thesis break의 hard 4C 기준점이다. |


## 6. Evidence Source Map

- Czech nuclear: Reuters는 2024-07-17 Czech government가 KHNP를 두 원전의 preferred bidder로 선정했다고 보도했고, 2024-10-30에는 경쟁사 appeals로 watchdog이 최종화를 일시 차단했다고 보도했다. 이 둘은 Stage2와 legal 4B-watch를 분리하는 evidence다. citeturn940526news1 citeturn940526news0
- Czech final confirmation: AP는 court clearance 이후 Czechs가 South Korea와 원전 건설 계약을 체결했다고 보도했다. 이는 HDEC Stage3-Green confirmation trigger로만 사용했다. citeturn940526news4
- Fadhili EPC: Reuters는 2024-04-02 Aramco가 Fadhili gas expansion 관련 $7.7bn EPC contracts를 Samsung Engineering, GS E&C, Nesma에 awarded했다고 보도했다. citeturn542411news0
- HDC collapse: Gwangju Hwajeong I-Park exterior wall collapse는 2022-01-11 발생했고, 6명이 사망했으며 HDC가 investigation 대상이 됐다. citeturn669761search0

## 7. Price Data Source Map

주요 stock-web row anchor:

- 삼성E&A 2024: 2024-04-03 close 25,300, 2024-07-30 high 29,300, 2024-12-09 low 16,300 등이 확인된다. fileciteturn364file0 fileciteturn365file0
- 현대건설 2024~2025: 2024-07-17 close 34,450, 2025-06-25 high 85,100 등이 확인된다. fileciteturn369file0 fileciteturn370file0 fileciteturn372file0
- GS건설 2024~2025: 2024-04-03 close 15,630, 2024-08-27 high 21,750, 2025-04~05 lows are visible. fileciteturn371file0 fileciteturn373file0
- HDC현대산업개발 2022: 2022-01-12 close 20,850 and high 22,700, later lows near 9,790~10,000 are visible. fileciteturn368file0 fileciteturn374file0

## 8. Case-by-Case Trigger Grid

| trigger_id | company | type | trigger_date | entry_date | entry_price | MFE90 | MAE90 | outcome | role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R10L1_HDEC_T1 | 현대건설 | Stage2 | 2024-07-17 | 2024-07-17 | 34450 | 1.5 | -19.9 | long_lag_missed_structural_but_high_MAE | representative |
| R10L1_HDEC_T5 | 현대건설 | Stage4B | 2024-10-30 | 2024-10-30 | 28250 | 32.9 | -14.5 | 4B_too_early_if_hard_exit | 4B_overlay_only |
| R10L1_HDEC_T4 | 현대건설 | Stage3-Green | 2025-06-04 | 2025-06-04 | 68800 | 23.7 | -21.1 | confirmed_but_late_and_volatile_green | representative |
| R10L1_GSENC_T1 | GS건설 | Stage2 | 2024-04-03 | 2024-04-03 | 15630 | 30.5 | -10.4 | score_mid_return_high_promote_candidate | label_comparison_only |
| R10L1_GSENC_T2 | GS건설 | Stage2-Actionable | 2024-04-03 | 2024-04-03 | 15630 | 30.5 | -10.4 | excellent_entry | representative |
| R10L1_GSENC_T4 | GS건설 | Stage3-Green | 2024-07-17 | 2024-07-17 | 18220 | 19.2 | -9.1 | good_but_later_entry | representative |
| R10L1_GSENC_T5 | GS건설 | Stage4B | 2024-08-27 | 2024-08-27 | 21550 | 0.9 | -18.6 | good_local_4B_watch | 4B_overlay_only |
| R10L1_SEA_T1 | 삼성E&A | Stage2 | 2024-04-03 | 2024-04-03 | 25300 | 15.8 | -14.6 | evidence_good_but_price_failed | label_comparison_only |
| R10L1_SEA_T2 | 삼성E&A | Stage2-Actionable | 2024-04-03 | 2024-04-03 | 25300 | 15.8 | -14.6 | watch_only_not_actionable | representative |
| R10L1_SEA_T4 | 삼성E&A | Stage3-Green | 2024-07-26 | 2024-07-26 | 27900 | 5.0 | -34.9 | false_positive_score | representative |
| R10L1_HDC_T6A | HDC현대산업개발 | Stage4C | 2022-01-11 | 2022-01-12 | 20850 | 8.2 | -36.9 | hard_4c_success | 4C_overlay_only |
| R10L1_HDC_T6B | HDC현대산업개발 | Stage4C-late | 2022-03-14 | 2022-03-14 | 16400 | 17.4 | -36.3 | hard_4c_late | 4C_overlay_only |


## 9. Trigger-Level OHLC Backtest Tables

| trigger_id | symbol | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MFE1Y | MAE30 | MAE90 | MAE180 | MAE1Y | peak_date | peak_price | DD_after_peak |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R10L1_HDEC_T1 | 000720 | 2024-07-17 | 34450 | 1.5 | 1.5 | 21.6 | 147.0 | -15.9 | -19.9 | -30.0 | -30.0 | 2025-06-25 | 85100 | -36.4 |
| R10L1_HDEC_T5 | 000720 | 2024-10-30 | 28250 | 5.8 | 32.9 | 201.2 | 201.2 | -14.5 | -14.5 | -14.5 | -14.5 | 2025-06-25 | 85100 | -36.4 |
| R10L1_HDEC_T4 | 000720 | 2025-06-04 | 68800 | 23.7 | 23.7 | 23.7 | insufficient_forward_window_in_stock_web | -6.3 | -21.1 | -21.4 | insufficient_forward_window_in_stock_web | 2025-06-25 | 85100 | -36.4 |
| R10L1_GSENC_T1 | 006360 | 2024-04-03 | 15630 | 7.0 | 30.5 | 39.2 | 39.2 | -10.4 | -10.4 | -10.4 | -10.4 | 2024-08-27 | 21750 | -30.2 |
| R10L1_GSENC_T2 | 006360 | 2024-04-03 | 15630 | 7.0 | 30.5 | 39.2 | 39.2 | -10.4 | -10.4 | -10.4 | -10.4 | 2024-08-27 | 21750 | -30.2 |
| R10L1_GSENC_T4 | 006360 | 2024-07-17 | 18220 | 18.8 | 19.2 | 19.2 | 19.2 | -9.1 | -9.1 | -16.5 | -16.5 | 2024-08-27 | 21750 | -30.2 |
| R10L1_GSENC_T5 | 006360 | 2024-08-27 | 21550 | 0.9 | 0.9 | 0.9 | 0.9 | -16.1 | -18.6 | -29.5 | -29.5 | 2024-08-27 | 21750 | -30.2 |
| R10L1_SEA_T1 | 028050 | 2024-04-03 | 25300 | 6.7 | 15.8 | 15.8 | 15.8 | -5.3 | -14.6 | -35.6 | -35.6 | 2024-07-30 | 29300 | -44.4 |
| R10L1_SEA_T2 | 028050 | 2024-04-03 | 25300 | 6.7 | 15.8 | 15.8 | 15.8 | -5.3 | -14.6 | -35.6 | -35.6 | 2024-07-30 | 29300 | -44.4 |
| R10L1_SEA_T4 | 028050 | 2024-07-26 | 27900 | 5.0 | 5.0 | 5.0 | 5.0 | -16.0 | -34.9 | -41.6 | -41.6 | 2024-07-30 | 29300 | -44.4 |
| R10L1_HDC_T6A | 294870 | 2022-01-12 | 20850 | 8.2 | 8.2 | 8.2 | 8.2 | -35.3 | -36.9 | -49.9 | -53.0 | 2022-01-12 | 22700 | -56.9 |
| R10L1_HDC_T6B | 294870 | 2022-03-14 | 16400 | 17.4 | 17.4 | 17.4 | 17.4 | -10.7 | -36.3 | -40.3 | -40.3 | 2022-03-14 | 19250 | -49.1 |


## 10. 1D Price Path Summaries

### 현대건설 000720 Czech nuclear long-lag path

| checkpoint | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---|---:|---:|---:|
| D+1 | -3.0 | +1.5 | -4.4 |
| D+30 | -6.0 | +1.5 | -15.9 |
| D+90 | -20.8 | +1.5 | -19.9 |
| D+180 | +16.7 | +21.6 | -30.0 |
| D+252 | +97.4 | +147.0 | -30.0 |

Czech nuclear Stage2는 “바로 달리는 엔진”이 아니라 “긴 철로를 깐 신호”였다. 90D 기대값은 나빴지만 1Y MFE가 커서 long-lag rule이 필요하다.

### GS건설 006360 Fadhili recovery path

| checkpoint | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---|---:|---:|---:|
| D+1 | -2.8 | +5.4 | -3.8 |
| D+20 | +0.1 | +7.0 | -10.4 |
| D+60 | +17.8 | +19.2 | -10.4 |
| D+90 | +28.4 | +30.5 | -10.4 |
| D+180 | +12.6 | +39.2 | -10.4 |

GS건설은 safety discount 이후 contract-quality가 회복 명분이 된 case다. 같은 Fadhili라도 GS는 discount-to-recovery, Samsung E&A는 contract-only로 갈라졌다.

### 삼성E&A 028050 Fadhili contract-only path

| checkpoint | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---|---:|---:|---:|
| D+1 | +3.0 | +6.7 | 0.0 |
| D+20 | +5.7 | +7.7 | -5.3 |
| D+60 | -8.9 | +7.7 | -11.7 |
| D+90 | +0.6 | +15.8 | -14.6 |
| D+180 | -34.7 | +15.8 | -35.6 |

대형 수주는 진짜였지만, margin/revision bridge가 닫히지 않으면 가격은 수주 소식의 무게를 오래 들고 가지 못했다.

### HDC현대산업개발 294870 hard 4C path

| checkpoint | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---|---:|---:|---:|
| D+1 | -1.2 | +8.2 | -6.2 |
| D+5 | -22.8 | +8.2 | -22.8 |
| D+30 | -25.9 | +8.2 | -35.3 |
| D+90 | -36.3 | +8.2 | -36.9 |
| D+180 | -45.6 | +8.2 | -49.9 |
| D+252 | -52.0 | +8.2 | -53.0 |

HDC는 재무 숫자가 먼저 깨진 게 아니라 “건설사로서 믿을 수 있는가”라는 바닥이 먼저 무너진 case다. 이건 watch가 아니라 hard 4C에 가깝다.

## 11. Case Trigger Comparison

| case_id | symbol | best_actual | baseline_selected | after_selected | baseline_date | after_date | baseline_px | after_px | baseline_MFE90 | after_MFE90 | baseline_MAE90 | after_MAE90 | return_improvement | risk_change | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R10L1_HDEC_000720_CZECH_NUCLEAR_LONGLAG | 000720 | R10L1_HDEC_T1 | R10L1_HDEC_T4 | R10L1_HDEC_T4 | 2025-06-04 | 2025-06-04 | 68800 | 68800 | 23.7 | 23.7 | -21.1 | -21.1 | 0.0 | 0.0 | P1 selected: contract quality + margin/revision guardrail + earlier 4C |
| R10L1_GSENC_006360_FADHILI_RECOVERY | 006360 | R10L1_GSENC_T2 | R10L1_GSENC_T4 | R10L1_GSENC_T2 | 2024-07-17 | 2024-04-03 | 18220 | 15630 | 19.2 | 30.5 | -9.1 | -10.4 | 11.3 | -1.3 | P1 selected: contract quality + margin/revision guardrail + earlier 4C |
| R10L1_SAMSUNGEA_028050_FADHILI_CONTRACT_FAILED | 028050 | R10L1_SEA_T2 | R10L1_SEA_T4 | R10L1_SEA_T2 | 2024-07-26 | 2024-04-03 | 27900 | 25300 | 5.0 | 15.8 | -34.9 | -14.6 | 10.8 | 20.3 | P1 selected: contract quality + margin/revision guardrail + earlier 4C |
| R10L1_HDC_294870_GWANGJU_COLLAPSE_4C | 294870 | R10L1_HDC_T6A | R10L1_HDC_T6B | R10L1_HDC_T6A | 2022-03-14 | 2022-01-12 | 16400 | 20850 | 17.4 | 8.2 | -36.3 | -36.9 | -9.2 | -0.6 | P1 selected: contract quality + margin/revision guardrail + earlier 4C |


## 12. Stage2 → Stage4 Audit

1. GS건설은 Stage2-Actionable에서 MFE90 30.5%, MAE90 -10.4%로 Green보다 우수했다.
2. 현대건설은 Stage2 이후 1Y MFE가 147.0%였지만 90D/180D MAE가 깊어 일반 early-entry가 아니라 long-lag optionality로 분리해야 한다.
3. 삼성E&A는 수주 evidence가 좋아도 margin/revision bridge가 없으면 Stage2-Actionable을 watch-only로 낮춰야 한다.
4. HDC는 Stage2~Stage3 entry 문제가 아니라 thesis break이므로 hard 4C가 핵심이다.

## 13. Stage3 Yellow / Green Lateness Audit

| case | Stage2/Actionable entry | Green entry | peak | green_lateness_ratio | verdict |
|---|---:|---:|---:|---:|---|
| 현대건설 | 34,450 | 68,800 | 85,100 | 0.76 | Green은 확인됐지만 upside 대부분을 놓침 |
| GS건설 | 15,630 | 18,220 | 21,750 | 0.56 | Green은 다소 늦음 |
| 삼성E&A | 25,300 | 27,900 | 29,300 | not_applicable | Green이 local peak 직전 false-positive |
| HDC | not_applicable | not_applicable | 22,700 | not_applicable | 4C case |

## 14. 4B Timing Audit

| trigger | local_peak_proximity | full_window_peak_proximity | evidence_type | verdict |
|---|---:|---:|---|---|
| R10L1_HDEC_T5 | -0.12 | -0.12 | legal_or_regulatory_block | legal 4B-watch, hard exit로 쓰면 너무 빠름 |
| R10L1_GSENC_T5 | 0.97 | 0.97 | price_only, positioning_overheat | local peak watch는 좋지만 full 4B evidence 약함 |

## 15. 4C Protection Audit

HDC_T6A는 hard 4C 성공이다. 사고 다음 거래일 기준 entry 이후 MFE90은 8.2%에 그쳤고 MAE90은 -36.9%, MAE1Y는 -53.0%였다. HDC_T6B처럼 2022-03-14 이후 확인하면 MAE90 -36.3%는 비슷하지만 이미 손상된 가격에서의 late 4C가 된다.

## 16. Baseline Score Simulation

Baseline proxy는 Green confirmation을 높게 평가해 현대건설/GS건설/삼성E&A를 늦게 잡거나 contract-only Green을 허용할 위험이 있었다. Proposed profile은 GS건설의 discount-recovery contract는 Stage2-Actionable로 승격하고, 삼성E&A처럼 margin/revision bridge 없는 mega-contract는 watch-only로 낮춘다. HDC safety accident는 early hard 4C로 당긴다.

## 17. Shadow Profile Optimization Loop

```csv
row_type,profile_id,case_count,selected_trigger_count,selected_representative_trigger_count,avg_MFE_90D_pct,avg_MAE_90D_pct,hit_rate_MFE90_gt_20pct,bad_entry_rate_MAE90_lt_minus_15pct,false_positive_rate,missed_structural_count,late_green_count,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
profile_comparison,baseline_current_proxy,4,4,2,16.3,-25.3,0.25,0.75,0.5,1,3,unavailable,unavailable,"reference; late Green and safety late 4C"
profile_comparison,stage2_actionable_contract_quality_plus_4c_safety_guardrail,4,4,2,19.6,-20.8,0.5,0.5,0.0,0,1,unavailable,unavailable,"best; contract-quality early promotion plus safety 4C guardrail"
profile_comparison,stage3_yellow_entry_relaxed,4,4,2,18.7,-21.6,0.5,0.5,0.25,0,2,unavailable,unavailable,"mixed; only with margin/revision guardrails"
profile_comparison,green_confirmation_timing_relaxed,4,4,2,16.3,-25.3,0.25,0.75,0.5,1,3,unavailable,unavailable,reject broad Green relaxation
profile_comparison,four_b_peak_timing_tuned,4,2,0,overlay_only,overlay_only,overlay_only,overlay_only,0,0,0,0.97,0.97,"accepted only for watch overlay; legal 4B not exit"
profile_comparison,four_c_thesis_break_earlier,4,2,0,overlay_only,overlay_only,overlay_only,overlay_only,0,0,0,unavailable,unavailable,accepted for construction safety accident hard 4C
```

Best profile: `stage2_actionable_contract_quality_plus_4c_safety_guardrail`.

## 18. Before / After Backtest Comparison

| case_id | symbol | best_actual | baseline_selected | after_selected | baseline_date | after_date | baseline_px | after_px | baseline_MFE90 | after_MFE90 | baseline_MAE90 | after_MAE90 | return_improvement | risk_change | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R10L1_HDEC_000720_CZECH_NUCLEAR_LONGLAG | 000720 | R10L1_HDEC_T1 | R10L1_HDEC_T4 | R10L1_HDEC_T4 | 2025-06-04 | 2025-06-04 | 68800 | 68800 | 23.7 | 23.7 | -21.1 | -21.1 | 0.0 | 0.0 | P1 selected: contract quality + margin/revision guardrail + earlier 4C |
| R10L1_GSENC_006360_FADHILI_RECOVERY | 006360 | R10L1_GSENC_T2 | R10L1_GSENC_T4 | R10L1_GSENC_T2 | 2024-07-17 | 2024-04-03 | 18220 | 15630 | 19.2 | 30.5 | -9.1 | -10.4 | 11.3 | -1.3 | P1 selected: contract quality + margin/revision guardrail + earlier 4C |
| R10L1_SAMSUNGEA_028050_FADHILI_CONTRACT_FAILED | 028050 | R10L1_SEA_T2 | R10L1_SEA_T4 | R10L1_SEA_T2 | 2024-07-26 | 2024-04-03 | 27900 | 25300 | 5.0 | 15.8 | -34.9 | -14.6 | 10.8 | 20.3 | P1 selected: contract quality + margin/revision guardrail + earlier 4C |
| R10L1_HDC_294870_GWANGJU_COLLAPSE_4C | 294870 | R10L1_HDC_T6A | R10L1_HDC_T6B | R10L1_HDC_T6A | 2022-03-14 | 2022-01-12 | 16400 | 20850 | 17.4 | 8.2 | -36.3 | -36.9 | -9.2 | -0.6 | P1 selected: contract quality + margin/revision guardrail + earlier 4C |


## 19. Score-Return Alignment Matrix

| alignment_label | trigger_count | avg_score_before | avg_score_after | avg_MFE90 | avg_MAE90 | verdict |
| --- | --- | --- | --- | --- | --- | --- |
| score_high_return_high | 4 | 73.0 | 78.2 | 21.0 | -20.4 | reference |
| score_high_return_low_false_positive | 2 | 75.5 | 70.5 | 11.2 | -35.6 | guardrail |
| score_low_return_high_missed_structural | 1 | 58.0 | 64.0 | 1.5 | -19.9 | reference |
| score_mid_return_high_promote_candidate | 2 | 62.0 | 74.0 | 30.5 | -10.4 | promote |
| score_mid_return_low_watch_only | 3 | 72.0 | 65.3 | 10.8 | -15.9 | guardrail |


## 20. Weight Sensitivity Table

```csv
row_type,axis,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,notes
"shadow_weight","stage2_actionable_contract_quality_with_discount_or_relative_strength",0,2,"+2","GS E&C Fadhili produced better entry as Stage2-Actionable than later Green.","GS T2 MFE90 30.5 / MAE90 -10.4 vs GS T4 MFE90 19.2 / MAE90 -9.1.","R10L1_GSENC_T2|R10L1_GSENC_T4",2,"shadow-only"
"shadow_weight","mega_contract_without_margin_revision_guardrail",0,3,"+3","Samsung E&A shows large EPC award alone should not become Green without margin/revision bridge.","SEA T4 MFE90 5.0 / MAE90 -34.9 after contract-only price confirmation.","R10L1_SEA_T1|R10L1_SEA_T2|R10L1_SEA_T4",3,"shadow-only; guardrail, not positive weight"
"shadow_weight","construction_safety_accident_hard_4c",0,3,"+3","HDC collapse shows safety/license/reputation break must be hard 4C early.","HDC early 4C MFE90 8.2 / MAE90 -36.9 and later 1Y MAE -53.0; late 4C missed much of risk.","R10L1_HDC_T6A|R10L1_HDC_T6B",2,"shadow-only"
"shadow_weight","legal_regulatory_4b_watch_not_hard_exit",0,2,"+2","Czech appeal block was legal 4B-watch but too early as hard exit because later MFE180 was 201.2.","HDEC legal 4B T5 MFE180 201.2 / MAE180 -14.5; treat as overlay watch, not exit.","R10L1_HDEC_T5|R10L1_HDEC_T4",2,"shadow-only"
```

## 21. Optimization Decision Log

```jsonl
{"row_type":"optimization_decision","decision_id":"R10L1_DECISION_01","hypothesis":"Contract quality plus recovery discount can promote Stage2 to Stage2-Actionable.","tested_trigger_ids":["R10L1_GSENC_T2","R10L1_GSENC_T4"],"baseline_profile":"baseline_current_proxy","selected_profile":"stage2_actionable_contract_quality_plus_4c_safety_guardrail","backtest_result_summary":"GS Stage2-Actionable captured more MFE90 than Green with acceptable MAE.","accepted_or_rejected":"accepted","delta_magnitude":"+2","why_not_larger_delta":"Samsung E&A counterexample shows mega-contract-only is not enough.","risks":"over-promoting low-margin EPC orders","next_validation_needed":"Add more overseas EPC cases with disclosed margin/revision bridge"}
{"row_type":"optimization_decision","decision_id":"R10L1_DECISION_02","hypothesis":"Mega EPC contract without margin/revision bridge should be watch-only.","tested_trigger_ids":["R10L1_SEA_T1","R10L1_SEA_T2","R10L1_SEA_T4"],"baseline_profile":"baseline_current_proxy","selected_profile":"stage2_actionable_contract_quality_plus_4c_safety_guardrail","backtest_result_summary":"Samsung E&A contract trigger failed to produce durable MFE and Green had deep MAE.","accepted_or_rejected":"accepted","delta_magnitude":"+3_guardrail","why_not_larger_delta":"One Samsung case is strong but not enough to suppress all EPC orders.","risks":"may miss genuine high-margin project mix shift","next_validation_needed":"Validate with Petrochem/LNG EPC cases"}
{"row_type":"optimization_decision","decision_id":"R10L1_DECISION_03","hypothesis":"Construction safety accident is a hard 4C gate when license/reputation/project execution can break.","tested_trigger_ids":["R10L1_HDC_T6A","R10L1_HDC_T6B"],"baseline_profile":"baseline_current_proxy","selected_profile":"four_c_thesis_break_earlier","backtest_result_summary":"Early 4C immediately after Gwangju collapse preceded deep drawdown; later 4C was too late.","accepted_or_rejected":"accepted","delta_magnitude":"+3","why_not_larger_delta":"Only one direct accident case used in this loop.","risks":"false 4C if accident is isolated and legally contained","next_validation_needed":"Add GS Geomdan with full evidence source and clean trigger timing"}
{"row_type":"optimization_decision","decision_id":"R10L1_DECISION_04","hypothesis":"Legal/regulatory delay after preferred-bidder selection should be 4B-watch, not hard exit, if project thesis remains alive.","tested_trigger_ids":["R10L1_HDEC_T5","R10L1_HDEC_T4"],"baseline_profile":"baseline_current_proxy","selected_profile":"four_b_peak_timing_tuned","backtest_result_summary":"HDEC T5 had large subsequent MFE180; hard exit would miss long-lag rerating.","accepted_or_rejected":"accepted","delta_magnitude":"+2_watch_overlay","why_not_larger_delta":"Legal appeals can still become hard block in other cases.","risks":"under-reacting to irreversible cancellation","next_validation_needed":"Find failed overseas concession/order cases"}
```

## 22. Overfitting / Robustness Check

- usable case count: 4
- usable trigger count: 12
- representative entry trigger count: 6
- Counterexamples: Samsung E&A mega-contract-only failed rerating, Hyundai E&C legal 4B-watch too early as hard exit.
- Hard 4C is validated only for severe safety/license/reputation accidents, not for ordinary cost overrun.

## 23. Cross-case Aggregate Metrics

| trigger_type | usable_trigger_count | representative_trigger_count | avg_MFE90 | median_MFE90 | avg_MAE90 | median_MAE90 | avg_MFE180 | avg_MAE180 | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Stage2 | 3 | 1 | 1.5 | 1.5 | -19.9 | -19.9 | 21.6 | -30.0 | representative rows only; overlay and same-entry labels excluded |
| Stage2-Actionable | 2 | 2 | 23.1 | 23.1 | -12.5 | -12.5 | 27.5 | -23.0 | representative rows only; overlay and same-entry labels excluded |
| Stage3-Green | 3 | 3 | 16.0 | 19.2 | -21.7 | -21.1 | 16.0 | -26.5 | representative rows only; overlay and same-entry labels excluded |


## 24. Score-Price Alignment Verdict

```text
selected_shadow_profile = stage2_actionable_contract_quality_plus_4c_safety_guardrail
score_price_alignment = partially_aligned_after_guardrail
main_positive = GS E&C contract-quality + discount recovery Stage2-Actionable
main_negative = Samsung E&A mega-contract-only Green false-positive
long_lag_note = Hyundai E&C nuclear preferred bidder should remain long-lag Stage2/Yellow until contract confirmation
4B_verdict = legal/regulatory 4B-watch must not become hard exit unless thesis is cancelled
4C_verdict = severe safety/license/reputation accident validates early hard 4C
```

## 25. Validation Scope / Non-Validation Scope

### this_round_validates

- Contract-quality + backlog/recovery evidence as Stage2-Actionable when discount and relative strength align.
- Mega EPC contract guardrail when margin/revision bridge is absent.
- Legal/regulatory 4B-watch separation from hard exit.
- Construction safety accident as hard 4C when license/reputation/project continuity breaks.

### this_round_does_not_validate

- Broad real-estate cycle bottom entry.
- Ordinary PF/liquidity event 4C.
- Full 2Y performance for 2024~2025 triggers due stock-web manifest max_date.
- GS Geomdan safety case, because evidence-source retrieval was incomplete in this run.

## 26. Shadow Weight Calibration

Recommended shadow-only changes:

1. `stage2_actionable_contract_quality_with_discount_or_relative_strength`: +2
2. `mega_contract_without_margin_revision_guardrail`: +3 guardrail
3. `construction_safety_accident_hard_4c`: +3
4. `legal_regulatory_4b_watch_not_hard_exit`: +2 overlay rule

No production scoring is changed.

## 27. Machine-Readable Rows

### 27.1 Price source validation row JSONL

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 27.2 Case rows JSONL

```jsonl
{"row_type":"case","case_id":"R10L1_HDEC_000720_CZECH_NUCLEAR_LONGLAG","symbol":"000720","company_name":"현대건설","case_type":"long_lag_structural_success_candidate","primary_archetype":"NUCLEAR_EPC_EXPORT_LONGLAG_CONSTRUCTION_RERATING","best_trigger":"R10L1_HDEC_T1","notes":"Czech nuclear preferred bidder는 즉시 rerating보다 long-lag 구조였다. Stage2 이후 1Y MFE는 컸지만 90D/180D MAE도 깊었다.","round":"R10","loop":"1","sector":"건설·부동산·건자재","calibration_usable":true,"historical_window_status":"180D_available_for_core_triggers","score_price_alignment":"mixed; contract-quality and safety-break gates validate, mega-contract-only Green rejected","price_source":"Songdaiki/stock-web"}
{"row_type":"case","case_id":"R10L1_GSENC_006360_FADHILI_RECOVERY","symbol":"006360","company_name":"GS건설","case_type":"structural_success_candidate_after_safety_discount","primary_archetype":"OVERSEAS_EPC_CONTRACT_RECOVERY_AFTER_SAFETY_DISCOUNT","best_trigger":"R10L1_GSENC_T2","notes":"Fadhili EPC 수주가 안전사고 discount 이후 recovery evidence로 작동했다. 같은 contract라도 discount 상태와 상대강도가 결합될 때 actionability가 커졌다.","round":"R10","loop":"1","sector":"건설·부동산·건자재","calibration_usable":true,"historical_window_status":"180D_available_for_core_triggers","score_price_alignment":"mixed; contract-quality and safety-break gates validate, mega-contract-only Green rejected","price_source":"Songdaiki/stock-web"}
{"row_type":"case","case_id":"R10L1_SAMSUNGEA_028050_FADHILI_CONTRACT_FAILED","symbol":"028050","company_name":"삼성E&A","case_type":"evidence_good_but_price_failed","primary_archetype":"MEGA_EPC_CONTRACT_WITHOUT_MARGIN_RERATING","best_trigger":"R10L1_SEA_T2","notes":"대형 Fadhili 수주는 있었지만 margin/revision bridge가 닫히지 않으면 full Stage2-Actionable/Green으로 올리면 실패할 수 있다.","round":"R10","loop":"1","sector":"건설·부동산·건자재","calibration_usable":true,"historical_window_status":"180D_available_for_core_triggers","score_price_alignment":"mixed; contract-quality and safety-break gates validate, mega-contract-only Green rejected","price_source":"Songdaiki/stock-web"}
{"row_type":"case","case_id":"R10L1_HDC_294870_GWANGJU_COLLAPSE_4C","symbol":"294870","company_name":"HDC현대산업개발","case_type":"hard_4c_thesis_break","primary_archetype":"CONSTRUCTION_SAFETY_ACCIDENT_LICENSE_REPUTATION_BREAK","best_trigger":"R10L1_HDC_T6A","notes":"Gwangju Hwajeong I-Park collapse는 건설사 safety/license/reputation thesis break의 hard 4C 기준점이다.","round":"R10","loop":"1","sector":"건설·부동산·건자재","calibration_usable":true,"historical_window_status":"180D_available_for_core_triggers","score_price_alignment":"mixed; contract-quality and safety-break gates validate, mega-contract-only Green rejected","price_source":"Songdaiki/stock-web"}
```

### 27.3 Trigger rows JSONL

```jsonl
{"row_type":"trigger","trigger_id":"R10L1_HDEC_T1","case_id":"R10L1_HDEC_000720_CZECH_NUCLEAR_LONGLAG","symbol":"000720","company_name":"현대건설","round":"R10","loop":"1","sector":"건설·부동산·건자재","primary_archetype":"NUCLEAR_EPC_EXPORT_LONGLAG_CONSTRUCTION_RERATING","trigger_type":"Stage2","trigger_date":"2024-07-17","evidence_available_at_that_date":"Czech government selected KHNP as preferred bidder; Hyundai E&C exposure was nuclear EPC export optionality rather than immediate earnings closure.","evidence_source":"Reuters Czech nuclear preferred bidder + stock-web OHLC","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000720/2024.csv","profile_path":"atlas/symbol_profiles/000/000720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-07-17","entry_price":34450,"MFE_30D_pct":1.5,"MFE_90D_pct":1.5,"MFE_180D_pct":21.6,"MFE_1Y_pct":147.0,"MFE_2Y_pct":"insufficient_forward_window_in_stock_web","MAE_30D_pct":-15.9,"MAE_90D_pct":-19.9,"MAE_180D_pct":-30.0,"MAE_1Y_pct":-30.0,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-06-25","peak_price":85100,"drawdown_after_peak_pct":-36.4,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":0.76,"four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"long_lag_missed_structural_but_high_MAE","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R10L1_HDEC_000720_CZECH_NUCLEAR_LONGLAG::2024-07-17::34450","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R10L1_HDEC_T5","case_id":"R10L1_HDEC_000720_CZECH_NUCLEAR_LONGLAG","symbol":"000720","company_name":"현대건설","round":"R10","loop":"1","sector":"건설·부동산·건자재","primary_archetype":"NUCLEAR_EPC_EXPORT_LONGLAG_CONSTRUCTION_RERATING","trigger_type":"Stage4B","trigger_date":"2024-10-30","evidence_available_at_that_date":"Czech watchdog temporarily blocked finalization after appeals; legal 4B-watch, not hard exit.","evidence_source":"Reuters Czech watchdog temporary block + stock-web OHLC","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000720/2024.csv","profile_path":"atlas/symbol_profiles/000/000720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-10-30","entry_price":28250,"MFE_30D_pct":5.8,"MFE_90D_pct":32.9,"MFE_180D_pct":201.2,"MFE_1Y_pct":201.2,"MFE_2Y_pct":"insufficient_forward_window_in_stock_web","MAE_30D_pct":-14.5,"MAE_90D_pct":-14.5,"MAE_180D_pct":-14.5,"MAE_1Y_pct":-14.5,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-06-25","peak_price":85100,"drawdown_after_peak_pct":-36.4,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":-0.12,"four_b_full_window_peak_proximity":-0.12,"four_b_timing_verdict":"legal_4B_watch_too_early_as_exit","four_b_evidence_type":"legal_or_regulatory_block","four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_too_early_if_hard_exit","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R10L1_HDEC_000720_CZECH_NUCLEAR_LONGLAG::2024-10-30::28250","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only"}
{"row_type":"trigger","trigger_id":"R10L1_HDEC_T4","case_id":"R10L1_HDEC_000720_CZECH_NUCLEAR_LONGLAG","symbol":"000720","company_name":"현대건설","round":"R10","loop":"1","sector":"건설·부동산·건자재","primary_archetype":"NUCLEAR_EPC_EXPORT_LONGLAG_CONSTRUCTION_RERATING","trigger_type":"Stage3-Green","trigger_date":"2025-06-04","evidence_available_at_that_date":"Contract signing / court-cleared confirmation moved trigger quality from optionality to confirmed project evidence.","evidence_source":"AP Czech contract signing context + stock-web OHLC","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000720/2025.csv","profile_path":"atlas/symbol_profiles/000/000720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-06-04","entry_price":68800,"MFE_30D_pct":23.7,"MFE_90D_pct":23.7,"MFE_180D_pct":23.7,"MFE_1Y_pct":"insufficient_forward_window_in_stock_web","MFE_2Y_pct":"insufficient_forward_window_in_stock_web","MAE_30D_pct":-6.3,"MAE_90D_pct":-21.1,"MAE_180D_pct":-21.4,"MAE_1Y_pct":"insufficient_forward_window_in_stock_web","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-06-25","peak_price":85100,"drawdown_after_peak_pct":-36.4,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":0.76,"four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"confirmed_but_late_and_volatile_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R10L1_HDEC_000720_CZECH_NUCLEAR_LONGLAG::2025-06-04::68800","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R10L1_GSENC_T1","case_id":"R10L1_GSENC_006360_FADHILI_RECOVERY","symbol":"006360","company_name":"GS건설","round":"R10","loop":"1","sector":"건설·부동산·건자재","primary_archetype":"OVERSEAS_EPC_CONTRACT_RECOVERY_AFTER_SAFETY_DISCOUNT","trigger_type":"Stage2","trigger_date":"2024-04-03","evidence_available_at_that_date":"Aramco Fadhili EPC award announced; after safety discount, contract/backlog evidence plus early relative strength was visible.","evidence_source":"Reuters Fadhili EPC award + stock-web OHLC","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006360/2024.csv","profile_path":"atlas/symbol_profiles/006/006360.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-03","entry_price":15630,"MFE_30D_pct":7.0,"MFE_90D_pct":30.5,"MFE_180D_pct":39.2,"MFE_1Y_pct":39.2,"MFE_2Y_pct":"insufficient_forward_window_in_stock_web","MAE_30D_pct":-10.4,"MAE_90D_pct":-10.4,"MAE_180D_pct":-10.4,"MAE_1Y_pct":-10.4,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-27","peak_price":21750,"drawdown_after_peak_pct":-30.2,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":0.56,"four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"score_mid_return_high_promote_candidate","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R10L1_GSENC_006360_FADHILI_RECOVERY::2024-04-03::15630","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only"}
{"row_type":"trigger","trigger_id":"R10L1_GSENC_T2","case_id":"R10L1_GSENC_006360_FADHILI_RECOVERY","symbol":"006360","company_name":"GS건설","round":"R10","loop":"1","sector":"건설·부동산·건자재","primary_archetype":"OVERSEAS_EPC_CONTRACT_RECOVERY_AFTER_SAFETY_DISCOUNT","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-03","evidence_available_at_that_date":"Same entry as T1, promoted because contract quality and safety-discount recovery combined with relative strength.","evidence_source":"Reuters Fadhili EPC award + stock-web OHLC","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006360/2024.csv","profile_path":"atlas/symbol_profiles/006/006360.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-03","entry_price":15630,"MFE_30D_pct":7.0,"MFE_90D_pct":30.5,"MFE_180D_pct":39.2,"MFE_1Y_pct":39.2,"MFE_2Y_pct":"insufficient_forward_window_in_stock_web","MAE_30D_pct":-10.4,"MAE_90D_pct":-10.4,"MAE_180D_pct":-10.4,"MAE_1Y_pct":-10.4,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-27","peak_price":21750,"drawdown_after_peak_pct":-30.2,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":0.56,"four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"excellent_entry","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R10L1_GSENC_006360_FADHILI_RECOVERY::2024-04-03::15630","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R10L1_GSENC_T4","case_id":"R10L1_GSENC_006360_FADHILI_RECOVERY","symbol":"006360","company_name":"GS건설","round":"R10","loop":"1","sector":"건설·부동산·건자재","primary_archetype":"OVERSEAS_EPC_CONTRACT_RECOVERY_AFTER_SAFETY_DISCOUNT","trigger_type":"Stage3-Green","trigger_date":"2024-07-17","evidence_available_at_that_date":"Relative strength and recovery confirmation appeared, but Green captured less upside than the April actionable trigger.","evidence_source":"stock-web OHLC + post-contract recovery context","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006360/2024.csv","profile_path":"atlas/symbol_profiles/006/006360.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-07-17","entry_price":18220,"MFE_30D_pct":18.8,"MFE_90D_pct":19.2,"MFE_180D_pct":19.2,"MFE_1Y_pct":19.2,"MFE_2Y_pct":"insufficient_forward_window_in_stock_web","MAE_30D_pct":-9.1,"MAE_90D_pct":-9.1,"MAE_180D_pct":-16.5,"MAE_1Y_pct":-16.5,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-27","peak_price":21750,"drawdown_after_peak_pct":-30.2,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":0.56,"four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"good_but_later_entry","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R10L1_GSENC_006360_FADHILI_RECOVERY::2024-07-17::18220","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R10L1_GSENC_T5","case_id":"R10L1_GSENC_006360_FADHILI_RECOVERY","symbol":"006360","company_name":"GS건설","round":"R10","loop":"1","sector":"건설·부동산·건자재","primary_archetype":"OVERSEAS_EPC_CONTRACT_RECOVERY_AFTER_SAFETY_DISCOUNT","trigger_type":"Stage4B","trigger_date":"2024-08-27","evidence_available_at_that_date":"Local price peak after recovery. Non-price 4B evidence was weak, so this is watch not full exit.","evidence_source":"stock-web OHLC","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006360/2024.csv","profile_path":"atlas/symbol_profiles/006/006360.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-08-27","entry_price":21550,"MFE_30D_pct":0.9,"MFE_90D_pct":0.9,"MFE_180D_pct":0.9,"MFE_1Y_pct":0.9,"MFE_2Y_pct":"insufficient_forward_window_in_stock_web","MAE_30D_pct":-16.1,"MAE_90D_pct":-18.6,"MAE_180D_pct":-29.5,"MAE_1Y_pct":-29.5,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-27","peak_price":21750,"drawdown_after_peak_pct":-30.2,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.97,"four_b_full_window_peak_proximity":0.97,"four_b_timing_verdict":"good_local_peak_timing_but_price_only_watch","four_b_evidence_type":"price_only|positioning_overheat","four_c_protection_label":"not_applicable","trigger_outcome_label":"good_local_4B_watch","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R10L1_GSENC_006360_FADHILI_RECOVERY::2024-08-27::21550","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only"}
{"row_type":"trigger","trigger_id":"R10L1_SEA_T1","case_id":"R10L1_SAMSUNGEA_028050_FADHILI_CONTRACT_FAILED","symbol":"028050","company_name":"삼성E&A","round":"R10","loop":"1","sector":"건설·부동산·건자재","primary_archetype":"MEGA_EPC_CONTRACT_WITHOUT_MARGIN_RERATING","trigger_type":"Stage2","trigger_date":"2024-04-03","evidence_available_at_that_date":"Fadhili EPC award was real, but price path did not prove durable margin/revision rerating.","evidence_source":"Reuters Fadhili EPC award + stock-web OHLC","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028050/2024.csv","profile_path":"atlas/symbol_profiles/028/028050.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-03","entry_price":25300,"MFE_30D_pct":6.7,"MFE_90D_pct":15.8,"MFE_180D_pct":15.8,"MFE_1Y_pct":15.8,"MFE_2Y_pct":"insufficient_forward_window_in_stock_web","MAE_30D_pct":-5.3,"MAE_90D_pct":-14.6,"MAE_180D_pct":-35.6,"MAE_1Y_pct":-35.6,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-30","peak_price":29300,"drawdown_after_peak_pct":-44.4,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"evidence_good_but_price_failed","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R10L1_SAMSUNGEA_028050_FADHILI_CONTRACT_FAILED::2024-04-03::25300","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only"}
{"row_type":"trigger","trigger_id":"R10L1_SEA_T2","case_id":"R10L1_SAMSUNGEA_028050_FADHILI_CONTRACT_FAILED","symbol":"028050","company_name":"삼성E&A","round":"R10","loop":"1","sector":"건설·부동산·건자재","primary_archetype":"MEGA_EPC_CONTRACT_WITHOUT_MARGIN_RERATING","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-03","evidence_available_at_that_date":"Same contract trigger. After-profile keeps it as watch because margin/revision bridge was not supported.","evidence_source":"Reuters Fadhili EPC award + stock-web OHLC","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028050/2024.csv","profile_path":"atlas/symbol_profiles/028/028050.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-03","entry_price":25300,"MFE_30D_pct":6.7,"MFE_90D_pct":15.8,"MFE_180D_pct":15.8,"MFE_1Y_pct":15.8,"MFE_2Y_pct":"insufficient_forward_window_in_stock_web","MAE_30D_pct":-5.3,"MAE_90D_pct":-14.6,"MAE_180D_pct":-35.6,"MAE_1Y_pct":-35.6,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-30","peak_price":29300,"drawdown_after_peak_pct":-44.4,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"watch_only_not_actionable","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R10L1_SAMSUNGEA_028050_FADHILI_CONTRACT_FAILED::2024-04-03::25300","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R10L1_SEA_T4","case_id":"R10L1_SAMSUNGEA_028050_FADHILI_CONTRACT_FAILED","symbol":"028050","company_name":"삼성E&A","round":"R10","loop":"1","sector":"건설·부동산·건자재","primary_archetype":"MEGA_EPC_CONTRACT_WITHOUT_MARGIN_RERATING","trigger_type":"Stage3-Green","trigger_date":"2024-07-26","evidence_available_at_that_date":"Price confirmation after contract turned into false-positive Green because upside was already local and drawdown was deep.","evidence_source":"stock-web OHLC + contract context","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028050/2024.csv","profile_path":"atlas/symbol_profiles/028/028050.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-07-26","entry_price":27900,"MFE_30D_pct":5.0,"MFE_90D_pct":5.0,"MFE_180D_pct":5.0,"MFE_1Y_pct":5.0,"MFE_2Y_pct":"insufficient_forward_window_in_stock_web","MAE_30D_pct":-16.0,"MAE_90D_pct":-34.9,"MAE_180D_pct":-41.6,"MAE_1Y_pct":-41.6,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-30","peak_price":29300,"drawdown_after_peak_pct":-44.4,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"false_positive_score","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R10L1_SAMSUNGEA_028050_FADHILI_CONTRACT_FAILED::2024-07-26::27900","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R10L1_HDC_T6A","case_id":"R10L1_HDC_294870_GWANGJU_COLLAPSE_4C","symbol":"294870","company_name":"HDC현대산업개발","round":"R10","loop":"1","sector":"건설·부동산·건자재","primary_archetype":"CONSTRUCTION_SAFETY_ACCIDENT_LICENSE_REPUTATION_BREAK","trigger_type":"Stage4C","trigger_date":"2022-01-11","evidence_available_at_that_date":"Gwangju Hwajeong I-Park exterior wall collapse triggered safety/license/reputation thesis break.","evidence_source":"public accident report + stock-web OHLC","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv","profile_path":"atlas/symbol_profiles/294/294870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-01-12","entry_price":20850,"MFE_30D_pct":8.2,"MFE_90D_pct":8.2,"MFE_180D_pct":8.2,"MFE_1Y_pct":8.2,"MFE_2Y_pct":8.2,"MAE_30D_pct":-35.3,"MAE_90D_pct":-36.9,"MAE_180D_pct":-49.9,"MAE_1Y_pct":-53.0,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-01-12","peak_price":22700,"drawdown_after_peak_pct":-56.9,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"hard_4c_success","trigger_outcome_label":"hard_4c_success","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R10L1_HDC_294870_GWANGJU_COLLAPSE_4C::2022-01-12::20850","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only"}
{"row_type":"trigger","trigger_id":"R10L1_HDC_T6B","case_id":"R10L1_HDC_294870_GWANGJU_COLLAPSE_4C","symbol":"294870","company_name":"HDC현대산업개발","round":"R10","loop":"1","sector":"건설·부동산·건자재","primary_archetype":"CONSTRUCTION_SAFETY_ACCIDENT_LICENSE_REPUTATION_BREAK","trigger_type":"Stage4C-late","trigger_date":"2022-03-14","evidence_available_at_that_date":"Later hard 4C confirmation after much of the collapse reaction had already occurred.","evidence_source":"stock-web OHLC + safety accident follow-through","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv","profile_path":"atlas/symbol_profiles/294/294870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-03-14","entry_price":16400,"MFE_30D_pct":17.4,"MFE_90D_pct":17.4,"MFE_180D_pct":17.4,"MFE_1Y_pct":17.4,"MFE_2Y_pct":17.4,"MAE_30D_pct":-10.7,"MAE_90D_pct":-36.3,"MAE_180D_pct":-40.3,"MAE_1Y_pct":-40.3,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-03-14","peak_price":19250,"drawdown_after_peak_pct":-49.1,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"hard_4c_late","trigger_outcome_label":"hard_4c_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R10L1_HDC_294870_GWANGJU_COLLAPSE_4C::2022-03-14::16400","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only"}
```

### 27.4 Score simulation rows JSONL

```jsonl
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R10L1_HDEC_000720_CZECH_NUCLEAR_LONGLAG","trigger_id":"R10L1_HDEC_T1","symbol":"000720","trigger_type":"Stage2","raw_component_scores_before":{"contract_score":7,"backlog_visibility_score":5,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":8,"customer_quality_score":10,"policy_or_regulatory_score":10,"valuation_repricing_score":4,"execution_risk_score":5,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":58,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":8,"backlog_visibility_score":7,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":8,"customer_quality_score":11,"policy_or_regulatory_score":11,"valuation_repricing_score":5,"execution_risk_score":6,"legal_or_contract_risk_score":6,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":64,"stage_label_after":"Stage2-watch","changed_components":["contract_score","backlog_visibility_score","revision_score","customer_quality_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"research proxy score only; component deltas are tied to dated evidence and OHLC MFE/MAE, not production scoring.","selected_by_profile":false,"MFE_90D_pct":1.5,"MAE_90D_pct":-19.9,"score_return_alignment_label":"score_low_return_high_missed_structural","row_validation_status":"valid_for_shadow_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R10L1_HDEC_000720_CZECH_NUCLEAR_LONGLAG","trigger_id":"R10L1_HDEC_T5","symbol":"000720","trigger_type":"Stage4B","raw_component_scores_before":{"contract_score":6,"backlog_visibility_score":5,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":3,"customer_quality_score":9,"policy_or_regulatory_score":8,"valuation_repricing_score":0,"execution_risk_score":8,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":61,"stage_label_before":"Stage3+4B-watch","raw_component_scores_after":{"contract_score":6,"backlog_visibility_score":5,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":3,"customer_quality_score":9,"policy_or_regulatory_score":8,"valuation_repricing_score":0,"execution_risk_score":9,"legal_or_contract_risk_score":12,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":64,"stage_label_after":"4B-watch_only","changed_components":["execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"research proxy score only; component deltas are tied to dated evidence and OHLC MFE/MAE, not production scoring.","selected_by_profile":false,"MFE_90D_pct":32.9,"MAE_90D_pct":-14.5,"score_return_alignment_label":"score_high_return_high","row_validation_status":"valid_for_shadow_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R10L1_HDEC_000720_CZECH_NUCLEAR_LONGLAG","trigger_id":"R10L1_HDEC_T4","symbol":"000720","trigger_type":"Stage3-Green","raw_component_scores_before":{"contract_score":13,"backlog_visibility_score":12,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":15,"customer_quality_score":12,"policy_or_regulatory_score":12,"valuation_repricing_score":11,"execution_risk_score":7,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":83,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":13,"backlog_visibility_score":13,"margin_bridge_score":6,"revision_score":6,"relative_strength_score":13,"customer_quality_score":12,"policy_or_regulatory_score":12,"valuation_repricing_score":10,"execution_risk_score":8,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":84,"stage_label_after":"Stage3-Green","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"research proxy score only; component deltas are tied to dated evidence and OHLC MFE/MAE, not production scoring.","selected_by_profile":true,"MFE_90D_pct":23.7,"MAE_90D_pct":-21.1,"score_return_alignment_label":"score_high_return_high","row_validation_status":"valid_for_shadow_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R10L1_GSENC_006360_FADHILI_RECOVERY","trigger_id":"R10L1_GSENC_T1","symbol":"006360","trigger_type":"Stage2","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":8,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":8,"customer_quality_score":11,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":62,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":12,"backlog_visibility_score":10,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":11,"customer_quality_score":12,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":74,"stage_label_after":"Stage2-Actionable","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","customer_quality_score","valuation_repricing_score"],"component_delta_explanation":"research proxy score only; component deltas are tied to dated evidence and OHLC MFE/MAE, not production scoring.","selected_by_profile":false,"MFE_90D_pct":30.5,"MAE_90D_pct":-10.4,"score_return_alignment_label":"score_mid_return_high_promote_candidate","row_validation_status":"valid_for_shadow_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R10L1_GSENC_006360_FADHILI_RECOVERY","trigger_id":"R10L1_GSENC_T2","symbol":"006360","trigger_type":"Stage2-Actionable","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":8,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":8,"customer_quality_score":11,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":62,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":12,"backlog_visibility_score":10,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":11,"customer_quality_score":12,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":74,"stage_label_after":"Stage2-Actionable","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","customer_quality_score","valuation_repricing_score"],"component_delta_explanation":"research proxy score only; component deltas are tied to dated evidence and OHLC MFE/MAE, not production scoring.","selected_by_profile":true,"MFE_90D_pct":30.5,"MAE_90D_pct":-10.4,"score_return_alignment_label":"score_mid_return_high_promote_candidate","row_validation_status":"valid_for_shadow_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R10L1_GSENC_006360_FADHILI_RECOVERY","trigger_id":"R10L1_GSENC_T4","symbol":"006360","trigger_type":"Stage3-Green","raw_component_scores_before":{"contract_score":12,"backlog_visibility_score":10,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":15,"customer_quality_score":12,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":81,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":12,"backlog_visibility_score":10,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":14,"customer_quality_score":12,"policy_or_regulatory_score":0,"valuation_repricing_score":9,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":79,"stage_label_after":"Stage3-Yellow","changed_components":["relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"research proxy score only; component deltas are tied to dated evidence and OHLC MFE/MAE, not production scoring.","selected_by_profile":false,"MFE_90D_pct":19.2,"MAE_90D_pct":-9.1,"score_return_alignment_label":"score_high_return_high","row_validation_status":"valid_for_shadow_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R10L1_GSENC_006360_FADHILI_RECOVERY","trigger_id":"R10L1_GSENC_T5","symbol":"006360","trigger_type":"Stage4B","raw_component_scores_before":{"contract_score":12,"backlog_visibility_score":10,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":18,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":13,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82,"stage_label_before":"Stage3-Green+4B-watch","raw_component_scores_after":{"contract_score":12,"backlog_visibility_score":10,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":14,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":14,"execution_risk_score":9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":84,"stage_label_after":"Stage3-Green+4B-watch","changed_components":["relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"research proxy score only; component deltas are tied to dated evidence and OHLC MFE/MAE, not production scoring.","selected_by_profile":false,"MFE_90D_pct":0.9,"MAE_90D_pct":-18.6,"score_return_alignment_label":"score_mid_return_low_watch_only","row_validation_status":"valid_for_shadow_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R10L1_SAMSUNGEA_028050_FADHILI_CONTRACT_FAILED","trigger_id":"R10L1_SEA_T1","symbol":"028050","trigger_type":"Stage2","raw_component_scores_before":{"contract_score":13,"backlog_visibility_score":11,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":6,"customer_quality_score":12,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":67,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":13,"backlog_visibility_score":11,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":5,"customer_quality_score":12,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":56,"stage_label_after":"Stage2-watch_only","changed_components":["margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"research proxy score only; component deltas are tied to dated evidence and OHLC MFE/MAE, not production scoring.","selected_by_profile":false,"MFE_90D_pct":15.8,"MAE_90D_pct":-14.6,"score_return_alignment_label":"score_mid_return_low_watch_only","row_validation_status":"valid_for_shadow_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R10L1_SAMSUNGEA_028050_FADHILI_CONTRACT_FAILED","trigger_id":"R10L1_SEA_T2","symbol":"028050","trigger_type":"Stage2-Actionable","raw_component_scores_before":{"contract_score":13,"backlog_visibility_score":11,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":6,"customer_quality_score":12,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":67,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":13,"backlog_visibility_score":11,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":5,"customer_quality_score":12,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":56,"stage_label_after":"Stage2-watch_only","changed_components":["margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"research proxy score only; component deltas are tied to dated evidence and OHLC MFE/MAE, not production scoring.","selected_by_profile":true,"MFE_90D_pct":15.8,"MAE_90D_pct":-14.6,"score_return_alignment_label":"score_mid_return_low_watch_only","row_validation_status":"valid_for_shadow_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R10L1_SAMSUNGEA_028050_FADHILI_CONTRACT_FAILED","trigger_id":"R10L1_SEA_T4","symbol":"028050","trigger_type":"Stage3-Green","raw_component_scores_before":{"contract_score":13,"backlog_visibility_score":12,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":16,"customer_quality_score":12,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":81,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":13,"backlog_visibility_score":11,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":9,"customer_quality_score":12,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":58,"stage_label_after":"Stage2-watch_only","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"research proxy score only; component deltas are tied to dated evidence and OHLC MFE/MAE, not production scoring.","selected_by_profile":false,"MFE_90D_pct":5.0,"MAE_90D_pct":-34.9,"score_return_alignment_label":"score_high_return_low_false_positive","row_validation_status":"valid_for_shadow_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R10L1_HDC_294870_GWANGJU_COLLAPSE_4C","trigger_id":"R10L1_HDC_T6A","symbol":"294870","trigger_type":"Stage4C","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":4,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":12,"legal_or_contract_risk_score":12,"dilution_cb_risk_score":0,"accounting_trust_risk_score":8},"weighted_score_before":67,"stage_label_before":"4C-watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":1,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":18,"legal_or_contract_risk_score":18,"dilution_cb_risk_score":0,"accounting_trust_risk_score":13},"weighted_score_after":86,"stage_label_after":"hard_4C","changed_components":["relative_strength_score","valuation_repricing_score","execution_risk_score","legal_or_contract_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"research proxy score only; component deltas are tied to dated evidence and OHLC MFE/MAE, not production scoring.","selected_by_profile":true,"MFE_90D_pct":8.2,"MAE_90D_pct":-36.9,"score_return_alignment_label":"score_high_return_high","row_validation_status":"valid_for_shadow_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R10L1_HDC_294870_GWANGJU_COLLAPSE_4C","trigger_id":"R10L1_HDC_T6B","symbol":"294870","trigger_type":"Stage4C-late","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":3,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":14,"legal_or_contract_risk_score":14,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_before":70,"stage_label_before":"4C-watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":17,"legal_or_contract_risk_score":17,"dilution_cb_risk_score":0,"accounting_trust_risk_score":12},"weighted_score_after":83,"stage_label_after":"hard_4C_late","changed_components":["relative_strength_score","valuation_repricing_score","execution_risk_score","legal_or_contract_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"research proxy score only; component deltas are tied to dated evidence and OHLC MFE/MAE, not production scoring.","selected_by_profile":false,"MFE_90D_pct":17.4,"MAE_90D_pct":-36.3,"score_return_alignment_label":"score_high_return_low_false_positive","row_validation_status":"valid_for_shadow_calibration"}
```

### 27.5 Profile comparison rows CSV

```csv
row_type,profile_id,case_count,selected_trigger_count,selected_representative_trigger_count,avg_MFE_90D_pct,avg_MAE_90D_pct,hit_rate_MFE90_gt_20pct,bad_entry_rate_MAE90_lt_minus_15pct,false_positive_rate,missed_structural_count,late_green_count,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
profile_comparison,baseline_current_proxy,4,4,2,16.3,-25.3,0.25,0.75,0.5,1,3,unavailable,unavailable,"reference; late Green and safety late 4C"
profile_comparison,stage2_actionable_contract_quality_plus_4c_safety_guardrail,4,4,2,19.6,-20.8,0.5,0.5,0.0,0,1,unavailable,unavailable,"best; contract-quality early promotion plus safety 4C guardrail"
profile_comparison,stage3_yellow_entry_relaxed,4,4,2,18.7,-21.6,0.5,0.5,0.25,0,2,unavailable,unavailable,"mixed; only with margin/revision guardrails"
profile_comparison,green_confirmation_timing_relaxed,4,4,2,16.3,-25.3,0.25,0.75,0.5,1,3,unavailable,unavailable,reject broad Green relaxation
profile_comparison,four_b_peak_timing_tuned,4,2,0,overlay_only,overlay_only,overlay_only,overlay_only,0,0,0,0.97,0.97,"accepted only for watch overlay; legal 4B not exit"
profile_comparison,four_c_thesis_break_earlier,4,2,0,overlay_only,overlay_only,overlay_only,overlay_only,0,0,0,unavailable,unavailable,accepted for construction safety accident hard 4C
```

### 27.6 Shadow weight CSV

```csv
row_type,axis,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,notes
"shadow_weight","stage2_actionable_contract_quality_with_discount_or_relative_strength",0,2,"+2","GS E&C Fadhili produced better entry as Stage2-Actionable than later Green.","GS T2 MFE90 30.5 / MAE90 -10.4 vs GS T4 MFE90 19.2 / MAE90 -9.1.","R10L1_GSENC_T2|R10L1_GSENC_T4",2,"shadow-only"
"shadow_weight","mega_contract_without_margin_revision_guardrail",0,3,"+3","Samsung E&A shows large EPC award alone should not become Green without margin/revision bridge.","SEA T4 MFE90 5.0 / MAE90 -34.9 after contract-only price confirmation.","R10L1_SEA_T1|R10L1_SEA_T2|R10L1_SEA_T4",3,"shadow-only; guardrail, not positive weight"
"shadow_weight","construction_safety_accident_hard_4c",0,3,"+3","HDC collapse shows safety/license/reputation break must be hard 4C early.","HDC early 4C MFE90 8.2 / MAE90 -36.9 and later 1Y MAE -53.0; late 4C missed much of risk.","R10L1_HDC_T6A|R10L1_HDC_T6B",2,"shadow-only"
"shadow_weight","legal_regulatory_4b_watch_not_hard_exit",0,2,"+2","Czech appeal block was legal 4B-watch but too early as hard exit because later MFE180 was 201.2.","HDEC legal 4B T5 MFE180 201.2 / MAE180 -14.5; treat as overlay watch, not exit.","R10L1_HDEC_T5|R10L1_HDEC_T4",2,"shadow-only"
```

### 27.7 Optimization decision rows JSONL

```jsonl
{"row_type":"optimization_decision","decision_id":"R10L1_DECISION_01","hypothesis":"Contract quality plus recovery discount can promote Stage2 to Stage2-Actionable.","tested_trigger_ids":["R10L1_GSENC_T2","R10L1_GSENC_T4"],"baseline_profile":"baseline_current_proxy","selected_profile":"stage2_actionable_contract_quality_plus_4c_safety_guardrail","backtest_result_summary":"GS Stage2-Actionable captured more MFE90 than Green with acceptable MAE.","accepted_or_rejected":"accepted","delta_magnitude":"+2","why_not_larger_delta":"Samsung E&A counterexample shows mega-contract-only is not enough.","risks":"over-promoting low-margin EPC orders","next_validation_needed":"Add more overseas EPC cases with disclosed margin/revision bridge"}
{"row_type":"optimization_decision","decision_id":"R10L1_DECISION_02","hypothesis":"Mega EPC contract without margin/revision bridge should be watch-only.","tested_trigger_ids":["R10L1_SEA_T1","R10L1_SEA_T2","R10L1_SEA_T4"],"baseline_profile":"baseline_current_proxy","selected_profile":"stage2_actionable_contract_quality_plus_4c_safety_guardrail","backtest_result_summary":"Samsung E&A contract trigger failed to produce durable MFE and Green had deep MAE.","accepted_or_rejected":"accepted","delta_magnitude":"+3_guardrail","why_not_larger_delta":"One Samsung case is strong but not enough to suppress all EPC orders.","risks":"may miss genuine high-margin project mix shift","next_validation_needed":"Validate with Petrochem/LNG EPC cases"}
{"row_type":"optimization_decision","decision_id":"R10L1_DECISION_03","hypothesis":"Construction safety accident is a hard 4C gate when license/reputation/project execution can break.","tested_trigger_ids":["R10L1_HDC_T6A","R10L1_HDC_T6B"],"baseline_profile":"baseline_current_proxy","selected_profile":"four_c_thesis_break_earlier","backtest_result_summary":"Early 4C immediately after Gwangju collapse preceded deep drawdown; later 4C was too late.","accepted_or_rejected":"accepted","delta_magnitude":"+3","why_not_larger_delta":"Only one direct accident case used in this loop.","risks":"false 4C if accident is isolated and legally contained","next_validation_needed":"Add GS Geomdan with full evidence source and clean trigger timing"}
{"row_type":"optimization_decision","decision_id":"R10L1_DECISION_04","hypothesis":"Legal/regulatory delay after preferred-bidder selection should be 4B-watch, not hard exit, if project thesis remains alive.","tested_trigger_ids":["R10L1_HDEC_T5","R10L1_HDEC_T4"],"baseline_profile":"baseline_current_proxy","selected_profile":"four_b_peak_timing_tuned","backtest_result_summary":"HDEC T5 had large subsequent MFE180; hard exit would miss long-lag rerating.","accepted_or_rejected":"accepted","delta_magnitude":"+2_watch_overlay","why_not_larger_delta":"Legal appeals can still become hard block in other cases.","risks":"under-reacting to irreversible cancellation","next_validation_needed":"Find failed overseas concession/order cases"}
```

### 27.8 Narrative-only rows JSONL

```jsonl
{"row_type":"narrative_only","case_id":"R10L1_GSENC_GEOMDAN_006360","symbol":"006360","reason":"Geomdan collapse can be safety 4C candidate, but in-session evidence-source retrieval was insufficient for machine-readable weight delta. OHLC rows were inspected, but row is excluded from calibration deltas.","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

### 27.9 Aggregate metric rows CSV

```csv
row_type,trigger_type,usable_trigger_count,representative_trigger_count,avg_MFE_90D_pct,median_MFE_90D_pct,avg_MAE_90D_pct,median_MAE_90D_pct,avg_MFE_180D_pct,avg_MAE_180D_pct,verdict
aggregate_metric,Stage2,3,1,1.5,1.5,-19.9,-19.9,21.6,-30.0,"representative rows only; overlay and same-entry labels excluded"
aggregate_metric,Stage2-Actionable,2,2,23.1,23.1,-12.5,-12.5,27.5,-23.0,"representative rows only; overlay and same-entry labels excluded"
aggregate_metric,Stage3-Green,3,3,16.0,19.2,-21.7,-21.1,16.0,-26.5,"representative rows only; overlay and same-entry labels excluded"
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
current_round = R10
current_loop = 1
next_round = R11
next_sector = 정책·지정학·재난·이벤트
carry_forward_questions =
- GS Geomdan safety 4C needs full evidence-source validation.
- PF/liquidity 4C remains outside this round.
- Nuclear long-lag optionality needs additional non-Hyundai cases.
```

## 30. Source Notes

Stock-web manifest/schema/profile/price rows are cited inline above. Evidence sources are public historical event sources and are separated from OHLC. No current/live candidate screening was performed.
