# Checkpoint 28A Round 194: R3 Loop 7 Battery/EV/Green Price Validation

## 목적

Round 194는 R3 `BATTERY_EV_GREEN`의 가격경로 검증 팩이다. 이번 라운드는 Stage 3-Green 후보를 늘리는 작업이 아니라, EV/ESS/배터리 소재에서 거짓 Green을 막는 보정 자료다.

쉬운 예: `as_of_date=2025-11-03`에 Tesla ESS 보도가 있어도 회사가 “아직 결정된 것 없음”이라고 말하면 Stage 3-Green으로 올리면 안 된다. 계약 확인, GWh, 출하, OPM, FCF, EPS/FCF revision이 필요하다.

## 반영 파일

- `src/e2r/sector/round194_r3_loop7_battery_ev_green_price_validation.py`
- `src/e2r/cli/build_round194_r3_loop7_report.py`
- `tests/test_round194_r3_loop7_battery_ev_green_price_validation.py`
- `data/e2r_case_library/cases_r3_loop7_round194.jsonl`
- `data/sector_taxonomy/round194_r3_loop7_battery_ev_green_price_validation_audit.json`
- `output/e2r_round194_r3_loop7_battery_ev_green_price_validation/`

## 케이스 요약

| case | 결론 | Stage 3 처리 |
| --- | --- | --- |
| LG에너지솔루션 | ESS LFP 계약은 Stage 2 가능, EV 계약 손실은 4C-watch | 보류 |
| L&F | Tesla cathode 계약가치 축소는 hard 4C calibration | Green 금지 |
| SK이노베이션/SK온 | ESS pivot은 watch, 기존 EV thesis는 훼손 | 보류 |
| 삼성SDI | 미확정 Tesla ESS 보도는 Stage 1 attention | Green 금지 |
| SK아이이테크놀로지 | 분리막도 EV 수요 둔화와 고객 재무난에 취약 | Green 금지 |
| 포스코퓨처엠 | 리튬 이벤트/장기계약 headline과 구조적 이익을 분리 | Green 금지 |
| 에코프로머티리얼즈 | IPO/전구체/그룹 내재화 스토리만으로는 부족 | Green 금지 |

## Green Gate

필수 증거:

- `binding_contract`
- `gwh_or_tonnage_volume`
- `customer_calloff_or_shipment`
- `utilization_rate`
- `opm_or_gross_margin_improvement`
- `fcf_after_capex`
- `eps_fcf_revision`
- `ev_or_ess_demand_durability`
- `tax_credit_quality_separated_from_underlying_profit`

금지 패턴:

- `ev_theme`
- `ess_theme`
- `capa_announcement`
- `customer_name_only`
- `unconfirmed_media_report`
- `lithium_price_spike`
- `ipo_premium`
- `contract_value_without_actual_order`
- `operating_loss_ex_tax_credit`

## 산출물

- `round194_r3_loop7_price_validation_summary.md`
- `round194_r3_loop7_case_matrix.csv`
- `round194_r3_loop7_target_aliases.csv`
- `round194_r3_loop7_score_adjustments.csv`
- `round194_r3_loop7_price_backfill_fields.csv`
- `round194_r3_loop7_green_gate_review.md`
- `round194_r3_loop7_price_backfill_plan.md`
- `round194_r3_loop7_stage4b_4c_review.md`

## 검증

```bash
PYTHONPATH=src python -m unittest tests.test_round194_r3_loop7_battery_ev_green_price_validation -v
PYTHONPATH=src python -m e2r.cli.build_round194_r3_loop7_report
```

결과:

- Round194 단위 테스트 9개 통과
- 케이스 7개 생성
- Stage 3 케이스 수 0개
- production scoring 변경 없음
- candidate generation input 아님
- shadow weight only
- OHLC backfill 필요

## 다음 작업

Round194는 가격과 운영지표를 확정하지 않는다. 다음에는 공식 OHLC와 재무 데이터를 붙여 Stage 2 기준 MFE/MAE, peak/drawdown, AMPC 제외 이익, utilization, OPM/FCF를 채워야 한다.
