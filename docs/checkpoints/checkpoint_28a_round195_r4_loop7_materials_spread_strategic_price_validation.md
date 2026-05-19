# Checkpoint 28A Round 195: R4 Loop 7 Materials/Spread Price Validation

## 목적

Round 195는 R4 `MATERIALS_SPREAD_STRATEGIC`의 가격경로 검증 팩이다. 이번 라운드는 소재/스프레드 섹터에서 Stage 3-Green을 늘리는 작업이 아니라, commodity price spike, 구조조정 기대, 공개매수, 미확정 보도, 매각 루머를 구조적 EPS/FCF 리레이팅으로 착각하지 않게 막는 보정 자료다.

쉬운 예: `as_of_date=2026-04-14`에 OCI-SpaceX 폴리실리콘 보도가 있어도 회사와 고객이 확인하지 않았으면 Stage 3-Green으로 올리면 안 된다. 확인된 계약, 물량, 가격, 기간, 마진, FCF가 필요하다.

## 반영 파일

- `src/e2r/sector/round195_r4_loop7_materials_spread_strategic_price_validation.py`
- `src/e2r/cli/build_round195_r4_loop7_report.py`
- `tests/test_round195_r4_loop7_materials_spread_strategic_price_validation.py`
- `data/e2r_case_library/cases_r4_loop7_round195.jsonl`
- `data/sector_taxonomy/round195_r4_loop7_materials_spread_strategic_price_validation_audit.json`
- `output/e2r_round195_r4_loop7_materials_spread_strategic_price_validation/`

## 케이스 요약

| case | 결론 | Stage 3 처리 |
| --- | --- | --- |
| 롯데케미칼 | 2024 손실/공급과잉은 4C, 구조조정은 Stage 2 watch | 보류 |
| LG화학 | 석유화학 손실과 NCC 원료차질 watch | Green 금지 |
| SK이노베이션 | 정유마진 반전은 cyclical success | 구조적 Green 아님 |
| 고려아연 | 경영권 event premium과 critical minerals Stage 2 evidence 분리 | 보류 |
| POSCO홀딩스 | 리튬 원료확보는 Stage 2 후보, 리튬 가격 이벤트는 Green 아님 | 보류 |
| OCI홀딩스 | 미확정 SpaceX 폴리실리콘 보도는 Stage 1 attention | Green 금지 |
| 풍산 | 방산부문 매각 루머 후 부인은 event thesis break | Green 금지 |

## Green Gate

필수 증거:

- `actual_product_spread`
- `cost_curve_advantage`
- `supply_discipline_or_capacity_shutdown_confirmed`
- `inventory_not_building`
- `fcf_conversion_or_cashflow_improvement`
- `price_floor_or_offtake_or_long_term_contract`
- `medium_term_eps_revision`
- `capex_and_dilution_risk_passed`

금지 패턴:

- `commodity_price_spike`
- `tender_offer_premium`
- `governance_battle`
- `policy_support_expectation`
- `unconfirmed_media_report`
- `restructuring_plan_only`
- `lithium_or_polysilicon_price_event`
- `geopolitical_refining_margin_spike`

## 산출물

- `round195_r4_loop7_price_validation_summary.md`
- `round195_r4_loop7_case_matrix.csv`
- `round195_r4_loop7_target_aliases.csv`
- `round195_r4_loop7_score_adjustments.csv`
- `round195_r4_loop7_price_backfill_fields.csv`
- `round195_r4_loop7_green_gate_review.md`
- `round195_r4_loop7_price_backfill_plan.md`
- `round195_r4_loop7_stage4b_4c_review.md`

## 검증

```bash
PYTHONPATH=src python -m unittest tests.test_round195_r4_loop7_materials_spread_strategic_price_validation -v
PYTHONPATH=src python -m e2r.cli.build_round195_r4_loop7_report
```

결과:

- Round195 단위 테스트 10개 통과
- 케이스 7개 생성
- Stage 3 케이스 수 0개
- production scoring 변경 없음
- candidate generation input 아님
- shadow weight only
- OHLC backfill 필요

## 다음 작업

Round195는 가격과 스프레드를 확정하지 않는다. 다음에는 공식 OHLC와 원자재/스프레드 데이터를 붙여 Stage 2 기준 MFE/MAE, event premium fade, spread reversal, inventory build, FCF after working capital을 채워야 한다.
