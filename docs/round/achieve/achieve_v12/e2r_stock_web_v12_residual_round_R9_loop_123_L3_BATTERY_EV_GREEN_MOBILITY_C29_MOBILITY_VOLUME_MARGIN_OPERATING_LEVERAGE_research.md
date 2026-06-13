# E2R Stock-Web v12 Residual Research — R9 Loop 123 / C29 Mobility Volume-Margin Operating Leverage

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "output_file": "e2r_stock_web_v12_residual_round_R9_loop_123_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md",
  "selected_round": "R9",
  "selected_loop": 123,
  "selected_large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "selected_canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE",
  "selected_priority_bucket": "Priority 0",
  "round_schedule_status": "coverage_index_first_not_sequential",
  "round_sector_consistency": "valid_R9_L3_C29",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "handoff_prompt_embedded": true,
  "handoff_prompt_executed_now": false,
  "stock_agent_code_access_allowed": false,
  "stock_agent_code_patch_allowed": false,
  "current_stock_discovery_allowed": false,
  "auto_trading_allowed": false,
  "brokerage_api_allowed": false,
  "price_source": "Songdaiki/stock-web",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "stock_web_manifest_max_date": "2026-02-20",
  "new_independent_case_count": 4,
  "usable_trigger_row_count": 5,
  "representative_trigger_count": 4,
  "positive_case_count": 2,
  "counterexample_count": 2,
  "stage4b_overlay_count": 1,
  "current_profile_error_count": 3,
  "coverage_before_representative_rows": 3,
  "coverage_after_if_accepted_representative_rows": 7,
  "fine_archetype_set": [
    "OEM_VOLUME_MIX_MARGIN_CAPITAL_RETURN_RERATING",
    "AUTO_PARTS_MARGIN_RECOVERY_AS_MIX_BRIDGE",
    "AUTO_PARTS_ORDER_INTAKE_WITH_NET_PROFIT_EXPECTATION_MISS",
    "LARGE_OEM_RECORD_OPM_ALREADY_PRICED_WITH_VOLUME_MIX_DECELERATION",
    "OEM_CAPITAL_RETURN_RERATING_LOCAL_4B_OVERLAY"
  ]
}
```

## 1. Execution Scope

이번 산출물은 `Songdaiki/stock-web`의 실제 1D OHLCV row를 사용한 historical trigger-level residual research다. 현재/live 종목 추천, 자동매매, 증권사 API 연결, `stock_agent` 코드 패치, production scoring 변경은 하지 않았다. 산출물은 나중에 batch calibration coding agent가 읽을 수 있는 standalone Markdown이다.

current_default_profile_proxy는 `e2r_2_1_stock_web_calibrated`로 둔다. 이 루프의 목표는 이미 반영된 global calibrated rule을 반복 증명하는 것이 아니라, C29 안에서 아직 남은 sector/canonical residual error를 찾는 것이다.

## 2. Coverage Index / No-Repeat Check

`V12_Research_No_Repeat_Index.md` 기준 C29는 representative row 3개, need-to-30 27개, need-to-50 47개인 Priority 0 구간이다. 직전 세션 산출물 C18/R5 loop121, C26/R8 loop122는 새 장부에 쌓인 것으로 간주하고 피했다. 기존 C29 대표 row에서 확인된 SJG세종(033530) / 2024-01-02류 legacy exhaust auto-parts 조합은 반복하지 않았다.

```text
selected_priority_bucket = Priority 0
selected_archetype = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
selected_round = R9
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
hard_duplicate_avoidance = canonical_archetype_id + symbol + trigger_type + entry_date
new_symbols_used = 000270, 012330, 204320, 005380
```

## 3. Stock-Web Price Atlas Validation

```json
{
  "manifest_url": "https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json",
  "schema_url": "https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/schema.json",
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
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "price_basis": "tradable_raw",
  "mfe_formula": "(max high from entry_date through N tradable rows / entry_price - 1) * 100",
  "mae_formula": "(min low from entry_date through N tradable rows / entry_price - 1) * 100"
}
```

MFE/MAE는 schema의 공식 그대로 계산했다. `entry_date`부터 N개의 tradable row를 포함해 최고가 high와 최저가 low를 찾고, 각각 entry_price 대비 수익률로 환산했다. 모든 row는 180 forward tradable days를 갖고 있고, 각 symbol profile의 corporate-action 후보일은 180D window 밖에 있다.

## 4. Canonical Compression

| canonical_archetype_id | fine_archetype_id | compression_reason |
| --- | --- | --- |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | OEM_VOLUME_MIX_MARGIN_CAPITAL_RETURN_RERATING | 완성차 volume/mix/margin + 자본정책이 rerating을 여는 경우 |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | AUTO_PARTS_MARGIN_RECOVERY_AS_MIX_BRIDGE | 부품주는 매출 성장보다 AS/mix/margin bridge가 먼저 보이는 leaf |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | AUTO_PARTS_ORDER_INTAKE_WITH_NET_PROFIT_EXPECTATION_MISS | 수주/OP 개선 headline이 있어도 순이익·기대치 품질이 깨지면 Stage2 false positive |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | LARGE_OEM_RECORD_OPM_ALREADY_PRICED_WITH_VOLUME_MIX_DECELERATION | 대형 OEM record OPM headline이 이미 가격에 반영되어 있으면 추가 rerating 근거가 약함 |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | OEM_CAPITAL_RETURN_RERATING_LOCAL_4B_OVERLAY | 실적/자본정책 rerating 후 고점권 추격을 막는 local 4B overlay |

## 5. Case Selection Summary

| case_id | symbol | name | case_role | trigger_type | trigger_date | entry_date | fine_archetype_id | evidence_family | current_profile_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C29_R9_L123_CASE_001_000270_KIA_2023_ANNUAL_OPM_CAPITAL_RETURN | 000270 | 기아 | positive | Stage3-Yellow | 2024-01-25 | 2024-01-26 | OEM_VOLUME_MIX_MARGIN_CAPITAL_RETURN_RERATING | annual_results/mix_margin/capital_return | current_profile_correct_positive |
| C29_R9_L123_CASE_001B_000270_KIA_LOCAL_4B_OVERLAY | 000270 | 기아 | 4B_overlay_only | Stage4B | 2024-06-19 | 2024-06-19 | OEM_CAPITAL_RETURN_RERATING_LOCAL_4B_OVERLAY | post_positive_price_extension/capital_return_rerating_saturation | current_profile_needs_local_4b_watch_not_full_4b |
| C29_R9_L123_CASE_002_012330_MOBIS_2024_MARGIN_RECOVERY | 012330 | 현대모비스 | positive | Stage2-Actionable | 2025-01-23 | 2025-01-24 | AUTO_PARTS_MARGIN_RECOVERY_AS_MIX_BRIDGE | annual_results/parts_margin_recovery/as_mix | current_profile_too_late_if_requires_topline_volume_growth |
| C29_R9_L123_CASE_003_204320_HL_MANDO_Q2_MISS | 204320 | HL만도 | counterexample | Stage2-Actionable | 2024-07-26 | 2024-07-29 | AUTO_PARTS_ORDER_INTAKE_WITH_NET_PROFIT_EXPECTATION_MISS | quarterly_results/new_order_intake/net_profit_miss/expectation_miss | current_profile_false_positive_if_orders_and_op_margin_are_overweighted_without_net_profit_quality |
| C29_R9_L123_CASE_004_005380_HYUNDAI_Q2_RECORD_ALREADY_PRICED | 005380 | 현대차 | counterexample | Stage2-Actionable | 2024-07-25 | 2024-07-26 | LARGE_OEM_RECORD_OPM_ALREADY_PRICED_WITH_VOLUME_MIX_DECELERATION | quarterly_results/record_opm/delivery_mix_deceleration/already_priced | current_profile_false_positive_if_record_opm_is_treated_as_new_rerating_without_incremental_volume_or_capital_return_shock |

## 6. Evidence Map

| symbol | name | trigger_date | evidence_url | evidence_summary |
| --- | --- | --- | --- | --- |
| 000270 | 기아 | 2024-01-25 | https://worldwide.kia.com/en/newsroom/view/?id=161711 | 2023년 연간 매출 +15.3%, 영업이익 11.61조원, OPM 11.6%와 고수익 차종 mix/가격 효과, 자사주 매입·소각/배당 정책이 함께 확인된 OEM volume/mix/margin rerating 케이스. |
| 000270 | 기아 | 2024-06-19 | https://worldwide.kia.com/en/newsroom/view/?id=161711 | 1월의 실적·자본정책 rerating이 6월 고점까지 거의 소진된 가격경로. 새 volume/margin bridge가 아니라 기존 rerating의 local 4B watch overlay로만 사용한다. |
| 012330 | 현대모비스 | 2025-01-23 | https://www.mk.co.kr/en/stock/11225880 | 2024년 매출은 감소했지만 영업이익과 OPM이 큰 폭으로 개선된 부품 margin recovery 케이스. 단기 MFE는 약했으나 180D MFE가 24.10%까지 확장되어 C29의 'volume보다 margin bridge가 먼저 오는' leaf를 보강한다. |
| 204320 | HL만도 | 2024-07-26 | https://en.yna.co.kr/view/AEN20240726008300320 | 매출과 영업이익은 개선됐지만 순이익 급감과 기대치 미달이 동시에 확인된 부품주 반례. 수주/OPM 단어만으로 Stage2-Actionable을 주면 30D MAE -22.58%를 맞는다. |
| 005380 | 현대차 | 2024-07-25 | https://www.hyundai.com/worldwide/en/newsroom/detail/hyundai-motor-announces-2024-q2-business-results-0000000801 | 2Q24 record revenue/profit/OPM와 배당이 있었지만 delivery growth와 mix의 추가 가속은 약했고 EV 판매 둔화도 있었다. 이미 가격에 반영된 대형 OEM record-OPM headline은 C29에서 Stage2-Actionable이 아니라 watch/hold로 낮춰야 하는 반례다. |

## 7. Trigger-Level Stock-Web Backtest Table

| case_id | symbol | trigger_type | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_180D_date | peak_180D_price | trough_180D_date | trough_180D_price | drawdown_after_peak_pct | representative_for_aggregate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C29_R9_L123_CASE_001_000270_KIA_2023_ANNUAL_OPM_CAPITAL_RETURN | 000270 | Stage3-Yellow | 2024-01-26 | 94400.00 | 39.51 | -1.80 | 39.51 | -1.80 | 43.01 | -4.66 | 2024-06-19 | 135000 | 2024-10-24 | 90000 | -33.33 | True |
| C29_R9_L123_CASE_001B_000270_KIA_LOCAL_4B_OVERLAY | 000270 | Stage4B | 2024-06-19 | 132300.00 | 2.04 | -16.86 | 2.04 | -32.05 | 2.04 | -32.35 | 2024-06-19 | 135000 | 2024-11-15 | 89500 | -33.70 | False |
| C29_R9_L123_CASE_002_012330_MOBIS_2024_MARGIN_RECOVERY | 012330 | Stage2-Actionable | 2025-01-24 | 263500.00 | 2.09 | -8.73 | 10.25 | -11.95 | 24.10 | -11.95 | 2025-09-09 | 327000 | 2025-04-14 | 232000 | -12.69 | True |
| C29_R9_L123_CASE_003_204320_HL_MANDO_Q2_MISS | 204320 | Stage2-Actionable | 2024-07-29 | 39850.00 | 1.25 | -22.58 | 8.91 | -22.58 | 17.94 | -22.58 | 2025-02-13 | 47000 | 2024-09-09 | 30850 | -30.85 | True |
| C29_R9_L123_CASE_004_005380_HYUNDAI_Q2_RECORD_ALREADY_PRICED | 005380 | Stage2-Actionable | 2024-07-26 | 243500.00 | 9.65 | -11.09 | 9.65 | -18.97 | 9.65 | -27.80 | 2024-08-29 | 267000 | 2025-04-11 | 175800 | -34.16 | True |

## 8. Positive / Counterexample Balance

Representative 기준 positive 2개, counterexample 2개다. 4B overlay 1개는 같은 기아 rerating 경로의 추격 방지용이므로 aggregate 대표 row에는 넣지 않았다. 대표 4개 row의 평균 MFE90은 17.08%, 평균 MAE90은 -13.82%, 평균 MFE180은 23.68%, 평균 MAE180은 -16.75%다.

C29는 자동차·부품 sector라 headline이 숫자로 좋아 보여도 경로가 거칠다. Kia처럼 volume/mix/margin + capital return이 함께 움직이면 180D MFE가 43.01%까지 열리지만, HL만도와 현대차 2Q24처럼 headline은 좋아도 기대치·순이익·추가 volume bridge가 약하면 90D/180D MAE가 먼저 커진다.

## 9. Case Notes

### 9.1 기아 — annual OPM + capital return positive

기아는 2023년 연간 실적에서 매출, 영업이익, OPM, 고수익 차종 mix, 자본정책이 같은 방향으로 맞물렸다. C29에서 Stage3-Yellow까지 허용 가능한 이유는 단순 판매대수 증가가 아니라, volume/mix/margin/return이 하나의 기어처럼 물린 점이다. entry 94,400원 이후 180D MFE 43.01%, MAE -4.66%로 reward/risk가 가장 깨끗하다.

### 9.2 기아 — local 4B overlay

같은 기아라도 2024-06-19 entry는 다른 사건이다. entry 132,300원은 같은 180D window의 최고가 135,000원에 거의 붙어 있었고, 이후 MAE90 -32.05%, MAE180 -32.35%가 나왔다. 이 row는 positive가 아니라, C29에서 `price_only_blowoff_blocks_positive_stage`와 `full_4b_requires_non_price_evidence`를 보강하는 local 4B overlay다.

### 9.3 현대모비스 — parts margin recovery positive

현대모비스는 매출 감소 headline만 보면 약해 보이지만, 영업이익/OPM 개선이 부품·AS mix quality를 보여준다. 30D MFE는 2.09%로 느렸고 MAE도 -8.73%였지만 180D MFE가 24.10%로 확장됐다. C29 안에서는 완성차 volume leaf와 부품 margin-recovery leaf를 분리해야 한다.

### 9.4 HL만도 — order/OPM headline false positive

HL만도는 매출과 영업이익 개선 및 신규 수주 단어가 있어도 순이익 급감/기대치 미달이 붙었다. entry 이후 30D MFE는 1.25%뿐인데 MAE30이 -22.58%다. 이 row는 수주와 OPM 개선 단어만 보고 Stage2-Actionable을 주면 안 된다는 counterexample이다.

### 9.5 현대차 — record OPM already priced false positive

현대차 2Q24는 record revenue/profit/OPM과 배당이 있었지만, entry 이후 MFE90은 9.65%에서 멈추고 MAE180은 -27.80%까지 열렸다. C29에서 대형 OEM record OPM headline은 이미 가격에 상당 부분 반영된 경우가 많아, incremental volume/mix/return shock 없이 Stage2-Actionable로 올리면 false positive가 된다.

## 10. Stage2 / Yellow / Green Stress Test

| profile_id | included_rows | false_positive_count | too_late_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | profile_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0_current_e2r_2_1_stock_web_calibrated_proxy | all_4_representative | 2 | 1 | 17.08 | -13.82 | 23.68 | -16.75 | works for Kia but still overcredits record-OPM/OP-only headlines and may undercredit parts margin recovery when revenue is not growing |
| P1_shadow_C29_volume_margin_capital_return_gate_v1 | 2 positive promoted; 2 counterexamples downgraded | 0 | 0 | 24.88 | -6.88 | 33.56 | -8.31 | requires incremental volume/mix or margin bridge plus capital-return/quality confirmation; downgrades net-profit miss and already-priced large OEM headlines |
| P2_shadow_local_4b_watch_overlay | Kia 2024-06-19 4B overlay only | 0 | 0 | 2.04 | -32.05 | 2.04 | -32.35 | after a +40% rerating, if no new non-price bridge exists, C29 should treat the move as local 4B watch rather than continuation |

Stage3-Green gate는 완화하지 않는다. 이번 C29 row는 Green unlock 연구가 아니라, Stage2-Actionable/Stage3-Yellow의 질을 갈라내는 연구다. Kia annual은 Yellow 허용, Mobis는 Stage2-Actionable/Yellow watch 후보, Mando/Hyundai는 Stage2-Watch 또는 hold로 낮추는 것이 score-return alignment를 개선한다.

## 11. 4B Local vs Full Window Proximity

기아 positive entry 2024-01-26의 entry 94,400원, full-window peak 135,000원, local 4B overlay entry 132,300원을 비교하면 4B overlay는 full rerating range의 93.35% 지점에 있었다. 즉 새 evidence 없이 같은 rerating을 추격한 위치였고, 이후 90D MAE -32.05%가 발생했다. C29의 4B는 '가격이 올랐으니 좋은 stage'가 아니라, 새 non-price bridge가 없는 고점권 추격을 막는 과열 표식으로 써야 한다.

```json
{
  "row_type": "four_b_audit",
  "symbol": "000270",
  "positive_entry_date": "2024-01-26",
  "positive_entry_price": 94400,
  "full_window_peak_date": "2024-06-19",
  "full_window_peak_price": 135000,
  "stage4b_overlay_entry_date": "2024-06-19",
  "stage4b_overlay_entry_price": 132300,
  "proximity_to_full_window_peak_range": 0.9335,
  "overlay_MFE_90D_pct": 2.04,
  "overlay_MAE_90D_pct": -32.05,
  "overlay_MFE_180D_pct": 2.04,
  "overlay_MAE_180D_pct": -32.35,
  "rule_read": "local_4b_watch_not_positive_continuation"
}
```

## 12. Proposed Sector / Canonical Shadow Rule

### C29_VOLUME_MARGIN_CAPITAL_RETURN_GATE_V1

C29에서 Stage2-Actionable 이상을 주려면 최소 하나의 좋은 headline이 아니라, 아래 bridge 중 둘 이상이 같은 방향이어야 한다.

```text
positive bridge candidates:
- volume growth or mix improvement with pricing/incentive discipline
- margin bridge that is not only FX/tax/noise-driven
- capital return policy that is backed by earnings/FCF visibility
- parts/AS mix recovery that improves OPM even when revenue is flat/down

negative blockers:
- net profit miss, tax/subsidiary drag, or estimate miss attached to OP headline
- record OPM headline after a large prior rerating with no incremental volume/mix evidence
- MFE90 < 10% while MAE30 <= -15%, especially in large OEMs or auto parts with weak expectation quality
- price-only extension after prior capital-return rerating: Stage4B-Watch, not positive continuation
```

이 규칙은 production scoring 변경이 아니라 shadow rule 후보다. C29 row가 아직 3→7 수준이라 production patch로 바로 반영하기보다는 20~30개까지 더 쌓으면서 coefficient를 안정화해야 한다.

## 13. Raw Component Score Breakdown

| case_id | symbol | trigger_type | current_profile_score | proposed_shadow_score | current_profile_stage | proposed_shadow_stage | score_return_alignment |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C29_R9_L123_CASE_001_000270_KIA_2023_ANNUAL_OPM_CAPITAL_RETURN | 000270 | Stage3-Yellow | 82.00 | 84.00 | Stage3-Yellow | Stage3-Yellow | aligned_positive |
| C29_R9_L123_CASE_002_012330_MOBIS_2024_MARGIN_RECOVERY | 012330 | Stage2-Actionable | 69.00 | 75.50 | Stage2 | Stage2-Actionable | current_profile_too_late_shadow_improves |
| C29_R9_L123_CASE_003_204320_HL_MANDO_Q2_MISS | 204320 | Stage2-Actionable | 74.00 | 61.00 | Stage2-Actionable | Stage2-Watch | current_profile_false_positive_shadow_blocks |
| C29_R9_L123_CASE_004_005380_HYUNDAI_Q2_RECORD_ALREADY_PRICED | 005380 | Stage2-Actionable | 78.00 | 65.00 | Stage2-Actionable | Stage2-Watch | current_profile_false_positive_shadow_blocks |
| C29_R9_L123_CASE_001B_000270_KIA_LOCAL_4B_OVERLAY | 000270 | Stage4B | 76.00 | 58.00 | Stage3-Yellow-continuation | Stage4B-Watch | 4b_overlay_prevents_late_chase |

```jsonl
{"row_type": "score_simulation", "case_id": "C29_R9_L123_CASE_001_000270_KIA_2023_ANNUAL_OPM_CAPITAL_RETURN", "symbol": "000270", "trigger_type": "Stage3-Yellow", "current_profile_score": 82.0, "proposed_shadow_score": 84.0, "current_profile_stage": "Stage3-Yellow", "proposed_shadow_stage": "Stage3-Yellow", "raw_component_scores_current": {"volume_mix_visibility": 8.5, "margin_bridge": 9.0, "operating_leverage": 8.5, "capital_return": 8.0, "revision_quality": 8.0, "valuation_rerating_headroom": 7.5, "evidence_confidence": 9.0, "risk_penalty": 2.0}, "raw_component_scores_shadow": {"volume_mix_visibility": 8.5, "margin_bridge": 9.0, "operating_leverage": 8.5, "capital_return": 9.0, "revision_quality": 8.0, "valuation_rerating_headroom": 7.5, "evidence_confidence": 9.0, "risk_penalty": 2.0}, "score_return_alignment": "aligned_positive"}
{"row_type": "score_simulation", "case_id": "C29_R9_L123_CASE_002_012330_MOBIS_2024_MARGIN_RECOVERY", "symbol": "012330", "trigger_type": "Stage2-Actionable", "current_profile_score": 69.0, "proposed_shadow_score": 75.5, "current_profile_stage": "Stage2", "proposed_shadow_stage": "Stage2-Actionable", "raw_component_scores_current": {"volume_mix_visibility": 4.0, "margin_bridge": 7.5, "operating_leverage": 6.5, "capital_return": 3.5, "revision_quality": 5.0, "valuation_rerating_headroom": 7.0, "evidence_confidence": 7.0, "risk_penalty": 3.5}, "raw_component_scores_shadow": {"volume_mix_visibility": 4.0, "margin_bridge": 8.5, "operating_leverage": 7.5, "capital_return": 3.5, "revision_quality": 5.5, "valuation_rerating_headroom": 7.0, "evidence_confidence": 8.0, "risk_penalty": 3.0}, "score_return_alignment": "current_profile_too_late_shadow_improves"}
{"row_type": "score_simulation", "case_id": "C29_R9_L123_CASE_003_204320_HL_MANDO_Q2_MISS", "symbol": "204320", "trigger_type": "Stage2-Actionable", "current_profile_score": 74.0, "proposed_shadow_score": 61.0, "current_profile_stage": "Stage2-Actionable", "proposed_shadow_stage": "Stage2-Watch", "raw_component_scores_current": {"volume_mix_visibility": 5.5, "margin_bridge": 6.5, "operating_leverage": 6.0, "capital_return": 2.0, "revision_quality": 4.5, "valuation_rerating_headroom": 5.5, "evidence_confidence": 6.5, "risk_penalty": 6.0}, "raw_component_scores_shadow": {"volume_mix_visibility": 5.0, "margin_bridge": 5.5, "operating_leverage": 5.0, "capital_return": 2.0, "revision_quality": 3.5, "valuation_rerating_headroom": 5.0, "evidence_confidence": 6.5, "risk_penalty": 8.5}, "score_return_alignment": "current_profile_false_positive_shadow_blocks"}
{"row_type": "score_simulation", "case_id": "C29_R9_L123_CASE_004_005380_HYUNDAI_Q2_RECORD_ALREADY_PRICED", "symbol": "005380", "trigger_type": "Stage2-Actionable", "current_profile_score": 78.0, "proposed_shadow_score": 65.0, "current_profile_stage": "Stage2-Actionable", "proposed_shadow_stage": "Stage2-Watch", "raw_component_scores_current": {"volume_mix_visibility": 6.0, "margin_bridge": 8.0, "operating_leverage": 7.5, "capital_return": 5.5, "revision_quality": 5.5, "valuation_rerating_headroom": 5.0, "evidence_confidence": 8.5, "risk_penalty": 4.0}, "raw_component_scores_shadow": {"volume_mix_visibility": 4.0, "margin_bridge": 6.5, "operating_leverage": 6.0, "capital_return": 5.0, "revision_quality": 4.5, "valuation_rerating_headroom": 3.0, "evidence_confidence": 8.5, "risk_penalty": 7.5}, "score_return_alignment": "current_profile_false_positive_shadow_blocks"}
{"row_type": "score_simulation", "case_id": "C29_R9_L123_CASE_001B_000270_KIA_LOCAL_4B_OVERLAY", "symbol": "000270", "trigger_type": "Stage4B", "current_profile_score": 76.0, "proposed_shadow_score": 58.0, "current_profile_stage": "Stage3-Yellow-continuation", "proposed_shadow_stage": "Stage4B-Watch", "raw_component_scores_current": {"volume_mix_visibility": 8.0, "margin_bridge": 8.0, "operating_leverage": 8.0, "capital_return": 8.0, "revision_quality": 7.0, "valuation_rerating_headroom": 2.0, "evidence_confidence": 8.0, "risk_penalty": 6.0}, "raw_component_scores_shadow": {"volume_mix_visibility": 7.0, "margin_bridge": 7.0, "operating_leverage": 7.0, "capital_return": 7.0, "revision_quality": 6.0, "valuation_rerating_headroom": 1.0, "evidence_confidence": 8.0, "risk_penalty": 9.0}, "score_return_alignment": "4b_overlay_prevents_late_chase"}
```

## 14. Residual Contribution Summary

```json
{
  "row_type": "residual_contribution",
  "selected_round": "R9",
  "selected_loop": 123,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE",
  "coverage_before_rows": 3,
  "coverage_after_if_accepted_rows": 7,
  "new_symbol_count": 4,
  "new_trigger_family_count": 5,
  "positive_count": 2,
  "counterexample_count": 2,
  "stage4b_overlay_count": 1,
  "current_profile_error_count": 3,
  "residual_label": "C29 needs separate OEM/parts margin-quality gates; not all record OPM or order-intake headlines are rerating-safe",
  "next_recommended_archetypes": [
    "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK",
    "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
    "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP",
    "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY",
    "C15_MATERIAL_SPREAD_SUPERCYCLE"
  ]
}
```

이번 row들이 새로 주는 정보는 'C29는 완성차와 부품을 같은 score gate로 묶으면 안 된다'는 점이다. 완성차 positive는 volume/mix/margin/capital return 동시성, 부품 positive는 AS/margin recovery, 반례는 net profit/expectation quality와 already-priced record OPM에서 갈린다.

## 15. Validation Scope / Non-Validation Scope

validated:

```text
- 5 trigger rows have entry_date and entry_price
- 5 trigger rows have MFE/MAE 30D/90D/180D
- 5 trigger rows use Songdaiki/stock-web tradable_raw shards
- 5 trigger rows have clean 180D corporate-action windows
- 4 representative rows are used for aggregate; 1 Kia 4B overlay is calibration usable but aggregate excluded
```

not validated / intentionally not done:

```text
- no live/current stock recommendation
- no broker/API route
- no stock_agent code inspection or patch
- no production scoring change
- no revised financial model beyond evidence-date headline facts
```

## 16. Batch Ingest Self-Audit

```json
{
  "expected_v12_result_file": true,
  "filename_pattern_pass": true,
  "metadata_filename_consistency": "pass",
  "selected_round": "R9",
  "selected_loop": 123,
  "selected_large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "selected_canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE",
  "round_sector_pair_valid": true,
  "compact_filename_forbidden": true,
  "jsonl_trigger_row_count": 5,
  "calibration_usable_trigger_count": 5,
  "representative_trigger_count": 4,
  "positive_case_count": 2,
  "counterexample_count": 2,
  "stage4b_overlay_count": 1,
  "trigger_rows_missing_required_mfe_mae": 0,
  "entry_price_missing_count": 0,
  "entry_date_missing_count": 0,
  "trigger_type_noncanonical_count": 0,
  "corporate_action_contaminated_180D_count": 0,
  "insufficient_forward_window_count": 0,
  "price_source_status": "stock_web_manifest_schema_verified",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "ready_for_batch_ingest": true
}
```

## 17. Machine-Readable Case Rows JSONL

```jsonl
{"row_type": "case", "schema_version": "e2r_v12_case_row_1", "research_file": "e2r_stock_web_v12_residual_round_R9_loop_123_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md", "case_id": "C29_R9_L123_CASE_001_000270_KIA_2023_ANNUAL_OPM_CAPITAL_RETURN", "symbol": "000270", "company_name": "기아", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "OEM_VOLUME_MIX_MARGIN_CAPITAL_RETURN_RERATING", "case_role": "positive", "trigger_date": "2024-01-25", "entry_date": "2024-01-26", "evidence_url": "https://worldwide.kia.com/en/newsroom/view/?id=161711", "evidence_family": "annual_results|mix_margin|capital_return", "calibration_usable": true, "representative_for_aggregate": true, "current_profile_verdict": "current_profile_correct_positive"}
{"row_type": "case", "schema_version": "e2r_v12_case_row_1", "research_file": "e2r_stock_web_v12_residual_round_R9_loop_123_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md", "case_id": "C29_R9_L123_CASE_001B_000270_KIA_LOCAL_4B_OVERLAY", "symbol": "000270", "company_name": "기아", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "OEM_CAPITAL_RETURN_RERATING_LOCAL_4B_OVERLAY", "case_role": "4B_overlay_only", "trigger_date": "2024-06-19", "entry_date": "2024-06-19", "evidence_url": "https://worldwide.kia.com/en/newsroom/view/?id=161711", "evidence_family": "post_positive_price_extension|capital_return_rerating_saturation", "calibration_usable": true, "representative_for_aggregate": false, "current_profile_verdict": "current_profile_needs_local_4b_watch_not_full_4b"}
{"row_type": "case", "schema_version": "e2r_v12_case_row_1", "research_file": "e2r_stock_web_v12_residual_round_R9_loop_123_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md", "case_id": "C29_R9_L123_CASE_002_012330_MOBIS_2024_MARGIN_RECOVERY", "symbol": "012330", "company_name": "현대모비스", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_PARTS_MARGIN_RECOVERY_AS_MIX_BRIDGE", "case_role": "positive", "trigger_date": "2025-01-23", "entry_date": "2025-01-24", "evidence_url": "https://www.mk.co.kr/en/stock/11225880", "evidence_family": "annual_results|parts_margin_recovery|as_mix", "calibration_usable": true, "representative_for_aggregate": true, "current_profile_verdict": "current_profile_too_late_if_requires_topline_volume_growth"}
{"row_type": "case", "schema_version": "e2r_v12_case_row_1", "research_file": "e2r_stock_web_v12_residual_round_R9_loop_123_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md", "case_id": "C29_R9_L123_CASE_003_204320_HL_MANDO_Q2_MISS", "symbol": "204320", "company_name": "HL만도", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_PARTS_ORDER_INTAKE_WITH_NET_PROFIT_EXPECTATION_MISS", "case_role": "counterexample", "trigger_date": "2024-07-26", "entry_date": "2024-07-29", "evidence_url": "https://en.yna.co.kr/view/AEN20240726008300320", "evidence_family": "quarterly_results|new_order_intake|net_profit_miss|expectation_miss", "calibration_usable": true, "representative_for_aggregate": true, "current_profile_verdict": "current_profile_false_positive_if_orders_and_op_margin_are_overweighted_without_net_profit_quality"}
{"row_type": "case", "schema_version": "e2r_v12_case_row_1", "research_file": "e2r_stock_web_v12_residual_round_R9_loop_123_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md", "case_id": "C29_R9_L123_CASE_004_005380_HYUNDAI_Q2_RECORD_ALREADY_PRICED", "symbol": "005380", "company_name": "현대차", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "LARGE_OEM_RECORD_OPM_ALREADY_PRICED_WITH_VOLUME_MIX_DECELERATION", "case_role": "counterexample", "trigger_date": "2024-07-25", "entry_date": "2024-07-26", "evidence_url": "https://www.hyundai.com/worldwide/en/newsroom/detail/hyundai-motor-announces-2024-q2-business-results-0000000801", "evidence_family": "quarterly_results|record_opm|delivery_mix_deceleration|already_priced", "calibration_usable": true, "representative_for_aggregate": true, "current_profile_verdict": "current_profile_false_positive_if_record_opm_is_treated_as_new_rerating_without_incremental_volume_or_capital_return_shock"}
```

## 18. Machine-Readable Trigger Rows JSONL

```jsonl
{"row_type": "trigger", "schema_version": "e2r_v12_trigger_row_1", "research_file": "e2r_stock_web_v12_residual_round_R9_loop_123_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md", "selected_round": "R9", "selected_loop": 123, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "OEM_VOLUME_MIX_MARGIN_CAPITAL_RETURN_RERATING", "case_id": "C29_R9_L123_CASE_001_000270_KIA_2023_ANNUAL_OPM_CAPITAL_RETURN", "symbol": "000270", "company_name": "기아", "market": "KOSPI", "trigger_type": "Stage3-Yellow", "trigger_date": "2024-01-25", "entry_date": "2024-01-26", "entry_price": 94400.0, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "price_shards": ["atlas/ohlcv_tradable_by_symbol_year/000/000270/2024.csv"], "MFE_30D_pct": 39.51, "MAE_30D_pct": -1.8, "MFE_90D_pct": 39.51, "MAE_90D_pct": -1.8, "MFE_180D_pct": 43.01, "MAE_180D_pct": -4.66, "peak_30D_date": "2024-03-11", "peak_30D_price": 131700, "trough_30D_date": "2024-01-26", "trough_30D_price": 92700, "peak_90D_date": "2024-03-11", "peak_90D_price": 131700, "trough_90D_date": "2024-01-26", "trough_90D_price": 92700, "peak_180D_date": "2024-06-19", "peak_180D_price": 135000, "trough_180D_date": "2024-10-24", "trough_180D_price": 90000, "drawdown_after_peak_pct": -33.33, "window_30D_corporate_action_contaminated": false, "window_90D_corporate_action_contaminated": false, "window_180D_corporate_action_contaminated": false, "corporate_action_window_180D": "clean", "profile_corporate_action_candidate_dates": ["1999-only"], "calibration_usable": true, "representative_for_aggregate": true, "dedupe_for_aggregate": true, "same_entry_group_id": "C29_000270_2024-01-26_Stage3-Yellow", "dedupe_key": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|000270|Stage3-Yellow|2024-01-26", "evidence_family": "annual_results|mix_margin|capital_return", "evidence_url": "https://worldwide.kia.com/en/newsroom/view/?id=161711", "evidence_url_status": "verified_url_not_proxy", "case_role": "positive", "current_profile_verdict": "current_profile_correct_positive", "independent_evidence_weight": 1.0}
{"row_type": "trigger", "schema_version": "e2r_v12_trigger_row_1", "research_file": "e2r_stock_web_v12_residual_round_R9_loop_123_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md", "selected_round": "R9", "selected_loop": 123, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "OEM_CAPITAL_RETURN_RERATING_LOCAL_4B_OVERLAY", "case_id": "C29_R9_L123_CASE_001B_000270_KIA_LOCAL_4B_OVERLAY", "symbol": "000270", "company_name": "기아", "market": "KOSPI", "trigger_type": "Stage4B", "trigger_date": "2024-06-19", "entry_date": "2024-06-19", "entry_price": 132300.0, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "price_shards": ["atlas/ohlcv_tradable_by_symbol_year/000/000270/2024.csv"], "MFE_30D_pct": 2.04, "MAE_30D_pct": -16.86, "MFE_90D_pct": 2.04, "MAE_90D_pct": -32.05, "MFE_180D_pct": 2.04, "MAE_180D_pct": -32.35, "peak_30D_date": "2024-06-19", "peak_30D_price": 135000, "trough_30D_date": "2024-07-26", "trough_30D_price": 110000, "peak_90D_date": "2024-06-19", "peak_90D_price": 135000, "trough_90D_date": "2024-10-25", "trough_90D_price": 89900, "peak_180D_date": "2024-06-19", "peak_180D_price": 135000, "trough_180D_date": "2024-11-15", "trough_180D_price": 89500, "drawdown_after_peak_pct": -33.7, "window_30D_corporate_action_contaminated": false, "window_90D_corporate_action_contaminated": false, "window_180D_corporate_action_contaminated": false, "corporate_action_window_180D": "clean", "profile_corporate_action_candidate_dates": ["1999-only"], "calibration_usable": true, "representative_for_aggregate": false, "dedupe_for_aggregate": false, "same_entry_group_id": "C29_000270_2024-06-19_Stage4B", "dedupe_key": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|000270|Stage4B|2024-06-19", "evidence_family": "post_positive_price_extension|capital_return_rerating_saturation", "evidence_url": "https://worldwide.kia.com/en/newsroom/view/?id=161711", "evidence_url_status": "verified_url_not_proxy", "case_role": "4B_overlay_only", "current_profile_verdict": "current_profile_needs_local_4b_watch_not_full_4b", "independent_evidence_weight": 0.5, "aggregate_exclusion_reason": "same_symbol_follow_on_4B_overlay_after_representative_positive_case"}
{"row_type": "trigger", "schema_version": "e2r_v12_trigger_row_1", "research_file": "e2r_stock_web_v12_residual_round_R9_loop_123_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md", "selected_round": "R9", "selected_loop": 123, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_PARTS_MARGIN_RECOVERY_AS_MIX_BRIDGE", "case_id": "C29_R9_L123_CASE_002_012330_MOBIS_2024_MARGIN_RECOVERY", "symbol": "012330", "company_name": "현대모비스", "market": "KOSPI", "trigger_type": "Stage2-Actionable", "trigger_date": "2025-01-23", "entry_date": "2025-01-24", "entry_price": 263500.0, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "price_shards": ["atlas/ohlcv_tradable_by_symbol_year/012/012330/2025.csv"], "MFE_30D_pct": 2.09, "MAE_30D_pct": -8.73, "MFE_90D_pct": 10.25, "MAE_90D_pct": -11.95, "MFE_180D_pct": 24.1, "MAE_180D_pct": -11.95, "peak_30D_date": "2025-02-21", "peak_30D_price": 269000, "trough_30D_date": "2025-03-12", "trough_30D_price": 240500, "peak_90D_date": "2025-06-12", "peak_90D_price": 290500, "trough_90D_date": "2025-04-14", "trough_90D_price": 232000, "peak_180D_date": "2025-09-09", "peak_180D_price": 327000, "trough_180D_date": "2025-04-14", "trough_180D_price": 232000, "drawdown_after_peak_pct": -12.69, "window_30D_corporate_action_contaminated": false, "window_90D_corporate_action_contaminated": false, "window_180D_corporate_action_contaminated": false, "corporate_action_window_180D": "clean", "profile_corporate_action_candidate_dates": ["1997/1999 only"], "calibration_usable": true, "representative_for_aggregate": true, "dedupe_for_aggregate": true, "same_entry_group_id": "C29_012330_2025-01-24_Stage2-Actionable", "dedupe_key": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|012330|Stage2-Actionable|2025-01-24", "evidence_family": "annual_results|parts_margin_recovery|as_mix", "evidence_url": "https://www.mk.co.kr/en/stock/11225880", "evidence_url_status": "verified_url_not_proxy", "case_role": "positive", "current_profile_verdict": "current_profile_too_late_if_requires_topline_volume_growth", "independent_evidence_weight": 1.0}
{"row_type": "trigger", "schema_version": "e2r_v12_trigger_row_1", "research_file": "e2r_stock_web_v12_residual_round_R9_loop_123_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md", "selected_round": "R9", "selected_loop": 123, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_PARTS_ORDER_INTAKE_WITH_NET_PROFIT_EXPECTATION_MISS", "case_id": "C29_R9_L123_CASE_003_204320_HL_MANDO_Q2_MISS", "symbol": "204320", "company_name": "HL만도", "market": "KOSPI", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-07-26", "entry_date": "2024-07-29", "entry_price": 39850.0, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "price_shards": ["atlas/ohlcv_tradable_by_symbol_year/204/204320/2024.csv", "atlas/ohlcv_tradable_by_symbol_year/204/204320/2025.csv"], "MFE_30D_pct": 1.25, "MAE_30D_pct": -22.58, "MFE_90D_pct": 8.91, "MAE_90D_pct": -22.58, "MFE_180D_pct": 17.94, "MAE_180D_pct": -22.58, "peak_30D_date": "2024-07-29", "peak_30D_price": 40350, "trough_30D_date": "2024-09-09", "trough_30D_price": 30850, "peak_90D_date": "2024-11-21", "peak_90D_price": 43400, "trough_90D_date": "2024-09-09", "trough_90D_price": 30850, "peak_180D_date": "2025-02-13", "peak_180D_price": 47000, "trough_180D_date": "2024-09-09", "trough_180D_price": 30850, "drawdown_after_peak_pct": -30.85, "window_30D_corporate_action_contaminated": false, "window_90D_corporate_action_contaminated": false, "window_180D_corporate_action_contaminated": false, "corporate_action_window_180D": "clean", "profile_corporate_action_candidate_dates": ["2018-05-08 only"], "calibration_usable": true, "representative_for_aggregate": true, "dedupe_for_aggregate": true, "same_entry_group_id": "C29_204320_2024-07-29_Stage2-Actionable", "dedupe_key": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|204320|Stage2-Actionable|2024-07-29", "evidence_family": "quarterly_results|new_order_intake|net_profit_miss|expectation_miss", "evidence_url": "https://en.yna.co.kr/view/AEN20240726008300320", "evidence_url_status": "verified_url_not_proxy", "case_role": "counterexample", "current_profile_verdict": "current_profile_false_positive_if_orders_and_op_margin_are_overweighted_without_net_profit_quality", "independent_evidence_weight": 1.0}
{"row_type": "trigger", "schema_version": "e2r_v12_trigger_row_1", "research_file": "e2r_stock_web_v12_residual_round_R9_loop_123_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md", "selected_round": "R9", "selected_loop": 123, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "LARGE_OEM_RECORD_OPM_ALREADY_PRICED_WITH_VOLUME_MIX_DECELERATION", "case_id": "C29_R9_L123_CASE_004_005380_HYUNDAI_Q2_RECORD_ALREADY_PRICED", "symbol": "005380", "company_name": "현대차", "market": "KOSPI", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-07-25", "entry_date": "2024-07-26", "entry_price": 243500.0, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "price_shards": ["atlas/ohlcv_tradable_by_symbol_year/005/005380/2024.csv", "atlas/ohlcv_tradable_by_symbol_year/005/005380/2025.csv"], "MFE_30D_pct": 9.65, "MAE_30D_pct": -11.09, "MFE_90D_pct": 9.65, "MAE_90D_pct": -18.97, "MFE_180D_pct": 9.65, "MAE_180D_pct": -27.8, "peak_30D_date": "2024-08-29", "peak_30D_price": 267000, "trough_30D_date": "2024-08-05", "trough_30D_price": 216500, "peak_90D_date": "2024-08-29", "peak_90D_price": 267000, "trough_90D_date": "2024-11-14", "trough_90D_price": 197300, "peak_180D_date": "2024-08-29", "peak_180D_price": 267000, "trough_180D_date": "2025-04-11", "trough_180D_price": 175800, "drawdown_after_peak_pct": -34.16, "window_30D_corporate_action_contaminated": false, "window_90D_corporate_action_contaminated": false, "window_180D_corporate_action_contaminated": false, "corporate_action_window_180D": "clean", "profile_corporate_action_candidate_dates": ["1998/1999 only"], "calibration_usable": true, "representative_for_aggregate": true, "dedupe_for_aggregate": true, "same_entry_group_id": "C29_005380_2024-07-26_Stage2-Actionable", "dedupe_key": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|005380|Stage2-Actionable|2024-07-26", "evidence_family": "quarterly_results|record_opm|delivery_mix_deceleration|already_priced", "evidence_url": "https://www.hyundai.com/worldwide/en/newsroom/detail/hyundai-motor-announces-2024-q2-business-results-0000000801", "evidence_url_status": "verified_url_not_proxy", "case_role": "counterexample", "current_profile_verdict": "current_profile_false_positive_if_record_opm_is_treated_as_new_rerating_without_incremental_volume_or_capital_return_shock", "independent_evidence_weight": 1.0}
```

## 19. Machine-Readable Aggregate / Shadow / Residual Rows JSONL

```jsonl
{"row_type": "aggregate_metrics", "selected_canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "representative_trigger_count": 4, "positive_representative_count": 2, "counterexample_representative_count": 2, "avg_MFE_90D_pct_all_representative": 17.08, "avg_MAE_90D_pct_all_representative": -13.82, "avg_MFE_180D_pct_all_representative": 23.68, "avg_MAE_180D_pct_all_representative": -16.75, "avg_MFE_90D_pct_positive_only": 24.88, "avg_MAE_90D_pct_positive_only": -6.88, "avg_MFE_180D_pct_positive_only": 33.55, "avg_MAE_180D_pct_positive_only": -8.3, "false_positive_count_current_proxy": 2, "too_late_count_current_proxy": 1, "profile_error_count": 3, "rule_candidate": "C29_VOLUME_MARGIN_CAPITAL_RETURN_GATE_V1"}
{"row_type": "profile_comparison", "profile_id": "P0_current_e2r_2_1_stock_web_calibrated_proxy", "included_rows": "all_4_representative", "false_positive_count": 2, "too_late_count": 1, "avg_MFE_90D_pct": 17.08, "avg_MAE_90D_pct": -13.82, "avg_MFE_180D_pct": 23.68, "avg_MAE_180D_pct": -16.75, "profile_read": "works for Kia but still overcredits record-OPM/OP-only headlines and may undercredit parts margin recovery when revenue is not growing"}
{"row_type": "profile_comparison", "profile_id": "P1_shadow_C29_volume_margin_capital_return_gate_v1", "included_rows": "2 positive promoted; 2 counterexamples downgraded", "false_positive_count": 0, "too_late_count": 0, "avg_MFE_90D_pct": 24.88, "avg_MAE_90D_pct": -6.88, "avg_MFE_180D_pct": 33.56, "avg_MAE_180D_pct": -8.31, "profile_read": "requires incremental volume/mix or margin bridge plus capital-return/quality confirmation; downgrades net-profit miss and already-priced large OEM headlines"}
{"row_type": "profile_comparison", "profile_id": "P2_shadow_local_4b_watch_overlay", "included_rows": "Kia 2024-06-19 4B overlay only", "false_positive_count": 0, "too_late_count": 0, "avg_MFE_90D_pct": 2.04, "avg_MAE_90D_pct": -32.05, "avg_MFE_180D_pct": 2.04, "avg_MAE_180D_pct": -32.35, "profile_read": "after a +40% rerating, if no new non-price bridge exists, C29 should treat the move as local 4B watch rather than continuation"}
{"row_type": "shadow_weight_candidate", "rule_id": "C29_VOLUME_MARGIN_CAPITAL_RETURN_GATE_V1", "scope": "canonical_archetype", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "do_not_apply_now": true, "production_scoring_changed": false, "positive_adjustments": {"incremental_volume_or_mix_visibility": "+0.50 to +0.80", "margin_bridge_or_AS_mix_quality": "+0.60 to +1.00", "capital_return_with_earnings_visibility": "+0.40 to +0.70"}, "negative_adjustments": {"net_profit_miss_or_tax_subsidiary_drag": "-0.70 to -1.20", "already_priced_record_OPM_without_new_volume_bridge": "-0.80 to -1.50", "MAE30_below_minus_15_with_MFE90_below_10": "force Stage2-Watch / block actionable promotion"}, "evidence_count": 4, "needs_more_rows_before_production": true}
{"row_type": "residual_contribution", "selected_round": "R9", "selected_loop": 123, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "coverage_before_rows": 3, "coverage_after_if_accepted_rows": 7, "new_symbol_count": 4, "new_trigger_family_count": 5, "positive_count": 2, "counterexample_count": 2, "stage4b_overlay_count": 1, "current_profile_error_count": 3, "residual_label": "C29 needs separate OEM/parts margin-quality gates; not all record OPM or order-intake headlines are rerating-safe", "next_recommended_archetypes": ["C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "C15_MATERIAL_SPREAD_SUPERCYCLE"]}
```

## 20. Deferred Coding Agent Handoff Prompt

```text
You are the later batch implementation/coding agent for Songdaiki/stock_agent. Do not infer production changes directly from this single MD. First run the repository's v12 calibration ingest over all standard v12 result MD files, validate every trigger row schema, deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date, reject rows missing 30/90/180D MFE/MAE or contaminated by corporate action windows, and compare this file's shadow rule candidate against aggregate C29 evidence. If and only if the batch evidence remains supportive, consider a narrowly scoped C29 shadow-to-production patch that improves Stage2-Actionable gating for mobility volume/mix/margin operating leverage and local 4B watch behavior. Preserve Stage3-Green hard gates and do not loosen Green thresholds from this file alone.
```

## 21. Next Research State

```text
last_completed_round = R9
last_completed_loop = 123
last_completed_large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
last_completed_canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
coverage_after_if_accepted = C29 rows 3 -> 7 representative rows
next_recommended_priority_bucket = Priority 0
next_recommended_archetypes = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK, C31_POLICY_SUBSIDY_LEGISLATION_EVENT, C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP, C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY, C15_MATERIAL_SPREAD_SUPERCYCLE
do_not_repeat_next = C29|000270|Stage3-Yellow|2024-01-26; C29|000270|Stage4B|2024-06-19; C29|012330|Stage2-Actionable|2025-01-24; C29|204320|Stage2-Actionable|2024-07-29; C29|005380|Stage2-Actionable|2024-07-26
```

## 22. Source URL Appendix

```text
MAIN_EXECUTION_PROMPT=https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
NO_REPEAT_INDEX=https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
STOCK_WEB_MANIFEST=https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
STOCK_WEB_SCHEMA=https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/schema.json
KIA_2023_ANNUAL=https://worldwide.kia.com/en/newsroom/view/?id=161711
HYUNDAI_2024_Q2=https://www.hyundai.com/worldwide/en/newsroom/detail/hyundai-motor-announces-2024-q2-business-results-0000000801
HL_MANDO_2024_Q2=https://en.yna.co.kr/view/AEN20240726008300320
HYUNDAI_MOBIS_2024_ANNUAL=https://www.mk.co.kr/en/stock/11225880
PRICE_000270_2024=https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/000/000270/2024.csv
PRICE_012330_2025=https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/012/012330/2025.csv
PRICE_204320_2024=https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/204/204320/2024.csv
PRICE_204320_2025=https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/204/204320/2025.csv
PRICE_005380_2024=https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/005/005380/2024.csv
PRICE_005380_2025=https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/005/005380/2025.csv
```
