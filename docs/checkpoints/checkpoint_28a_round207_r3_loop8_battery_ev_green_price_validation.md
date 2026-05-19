# Checkpoint 28A Round207 R3 Loop8 Battery EV Green Price Validation

## 목적

`docs/round/round_207.md`의 R3 Loop 8 내용을 별도 가격경로 검증 팩으로 반영했다.

이번 라운드의 핵심은 Stage 3-Green 발굴이 아니라 **false Green 차단**이다. 배터리/EV/ESS 섹터는 계약, 고객명, CAPA, 보조금, 리튬 가격 이벤트가 강하게 보일 수 있지만, 실제 `GWh/call-off -> 가동률 -> OPM/FCF -> EPS revision`으로 내려오기 전에는 Green으로 올리면 안 된다.

쉬운 예:

`as_of_date=2025-07-30`에 LG에너지솔루션이 43억 달러 ESS 계약을 발표했더라도, 배송이 2027년 이후이고 마진/FCF가 아직 없으면 Stage 3-Green이 아니라 Stage 2 watch다.

## 추가 파일

- `src/e2r/sector/round207_r3_loop8_battery_ev_green_price_validation.py`
- `src/e2r/cli/build_round207_r3_loop8_report.py`
- `tests/test_round207_r3_loop8_battery_ev_green_price_validation.py`
- `data/e2r_case_library/cases_r3_loop8_round207.jsonl`
- `data/sector_taxonomy/round207_r3_loop8_battery_ev_green_price_validation_audit.json`
- `output/e2r_round207_r3_loop8_battery_ev_green_price_validation/`

## 케이스 요약

| case | 판단 | 가격/계약 anchor |
| --- | --- | --- |
| LG에너지솔루션 | ESS Stage 2 + 4C watch/hard gate | Q2 이벤트 -1.6%, Ford 취소 -7.6%, 기대매출 13.5조 원 손실 |
| L&F | hard 4C | Tesla 계약가치 $2.9B -> $7,386 |
| 삼성SDI | ESS Stage 2 + 자금조달 watch | ESS 계약 +6.1%, 유상증자 가격 -13.6%, YTD -29.5% |
| SK이노베이션/SK온 | failed rerating / restructuring relief | 합병 승인 +5%, 순부채 +437.9%, 10분기 연속 손실 |
| SKIET | separator demand-cycle break | SK온 손실 18.6B -> 332B, +1684.9% |
| 포스코퓨처엠 | lithium event premium | CATL lithium event +8.3%, Ford shock -8.2% |
| 에코프로머티리얼즈 | overheat / price moved without evidence | -11% to 119,200원, implied prior 133,933원 |

## Green Gate 보정 방향

올릴 축:

- `binding_contract_quality`
- `actual_calloff`
- `gwh_or_tonnage_volume`
- `utilization_rate`
- `opm_visibility`
- `fcf_after_capex`
- `ess_revenue_conversion`
- `customer_quality`
- `subsidy_quality_adjustment`

내릴 축:

- `ev_theme_only`
- `ess_theme_only`
- `customer_name_only`
- `contract_value_headline_without_calloff`
- `capa_announcement`
- `subsidy_dependent_profit`
- `negative_fcf_or_debt_burden`
- `ipo_or_vertical_integration_story`
- `lithium_price_event`

## 4B / 4C 기준

4B-watch:

- ESS/LFP 계약 발표만으로 주가가 먼저 급등
- 리튬 가격 이벤트로 배터리 supply chain이 동반 상승
- AMPC 포함 이익만으로 실적 서프라이즈처럼 보이는 경우
- IPO/수직계열화 narrative가 증거보다 먼저 가격에 반영되는 경우

Hard 4C:

- 계약 취소
- 계약가치 붕괴
- 고객 EV 모델 취소
- 고객 전략 후퇴
- GWh call-off 실패
- 가동률 지연
- negative FCF
- 부채 부담 / 비상경영
- 보조금 제외 이익 붕괴
- 약한 수요 환경에서의 유상증자/희석

## 안전장치

- `production_scoring_changed = false`
- `candidate_generation_input = false`
- `shadow_weight_only = true`
- `price_validation_completed = partial_with_reported_price_anchors`
- `full_ohlc_complete = false`

이번 라운드는 production scoring을 바꾸지 않는다. 케이스는 calibration/evaluation 자료이며, 후보 생성 입력으로 쓰면 안 된다.
