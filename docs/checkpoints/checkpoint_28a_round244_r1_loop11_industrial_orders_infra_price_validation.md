# Checkpoint 28A Round 244 R1 Loop 11 Industrial Orders Infra Price Validation

## 목적

`docs/round/round_244.md`를 R1 Loop 11 산업재·수주·인프라 가격경로 검증 팩으로 구조화했다. 이번 작업은 케이스 라이브러리와 shadow calibration 산출물만 추가하며, 생산 scoring, StageClassifier, candidate generation은 바꾸지 않는다.

쉬운 예시:

- 체코 원전은 `preferred bidder`보다 `signed contract`가 강한 Stage 2 증거다. 그래도 두산에너빌리티·한전기술·한전KPS 같은 상장사별 package, margin, cash collection이 확인되기 전에는 Stage 3-Green이 아니다.
- HD현대마린솔루션은 MRO recurring service 후보지만, IPO 첫날 `83,400원 -> 163,900원` 급등은 실적 검증 전 4B-watch다.
- 삼성중공업/Zvezda 계약 취소는 수주잔고 headline이 Green이 될 수 없다는 hard 4C 기준점이다.

## 반영 파일

- `src/e2r/sector/archetypes.py`
- `src/e2r/sector/round244_r1_loop11_industrial_orders_infra_price_validation.py`
- `src/e2r/cli/build_round244_r1_loop11_report.py`
- `tests/test_round244_r1_loop11_industrial_orders_infra_price_validation.py`
- `data/e2r_case_library/cases_r1_loop11_round244.jsonl`
- `data/sector_taxonomy/round244_r1_loop11_industrial_orders_infra_price_validation_audit.json`
- `output/e2r_round244_r1_loop11_industrial_orders_infra_price_validation/`

## 추가한 아키타입

Round 244가 요구한 target alias를 canonical enum으로 보존했다.

- `NUCLEAR_EPC_EXPORT_ORDER`
- `NUCLEAR_SMR_POLICY_MOU`
- `POWER_GRID_CABLE_TRANSFORMER_EXPORT`
- `MARINE_MRO_RECURRING_SERVICE`
- `SHIPBUILDING_CONTRACT_CANCELLATION_4C`
- `DEFENSE_LOCAL_PRODUCTION_DILUTION_WATCH`

또한 기존 enum이었지만 정의가 없던 다음 항목의 정의도 보강했다.

- `SHIPBUILDING_US_POLICY_MASGA`
- `GEOPOLITICAL_SHIPBUILDING_SANCTION`
- `CONTRACT_HEADLINE_NOT_STAGE3`

## 케이스 요약

총 9개 케이스를 추가했다.

| case | 해석 |
|---|---|
| Doosan / KEPCO Czech nuclear | signed contract까지 올라온 강한 Stage 2, listed-company package/margin/cash collection 전 Green 금지 |
| Doosan SMR / AI power | X-energy/AWS/Fermi MOU는 Stage 2 watch, funded order 전 Green 금지 |
| LS Electric / LS Corp grid cable | 계약과 U.S. mix는 좋지만 이벤트 당일 가격 실패, Stage 2 watch |
| HD Hyundai Marine Solution | MRO recurring service 후보지만 IPO 첫날 +96.5%는 4B-watch |
| HD Hyundai Heavy / Mipo MASGA | MASGA/합병/record high는 Stage 2 + 4B-watch |
| Samsung Heavy / Zvezda | 계약 취소 hard 4C |
| Hanwha Aerospace Poland JV | 방산 현지생산 Stage 2, 대형 증자 shock 때문에 dilution 4B-watch |
| Hyundai Rotem Morocco rail | 2.2조 원 철도 수출 Stage 2, 납품·마진·working capital 전 Green 보류 |
| Hanwha Ocean China sanctions | U.S. 조선 exposure가 있어도 China sanctions는 4C-watch |

## Green Gate

R1 Stage 3-Green은 다음을 요구한다.

- signed contract 또는 firm order
- 계약금액, 고객, 납기 확인
- 실제 납품 또는 매출 인식 시작
- OPM / EPS revision 확인
- working capital / cash collection 안정
- 지정학, 법적, 제재 리스크 통과
- dilution / capital allocation 리스크 통과
- evidence 이후 가격경로 확인

반대로 다음은 Green 금지 패턴이다.

- preferred bidder만 있음
- MOU만 있음
- 정책 summit headline만 있음
- IPO 첫날 급등만 있음
- record high policy rally
- 러시아·제재 고객 exposure
- 계약취소위험이 가격에 반영되지 않음
- 납품·마진·현금회수 불명확

## 산출물

생성한 산출물:

- `round244_r1_loop11_price_validation_summary.md`
- `round244_r1_loop11_case_matrix.csv`
- `round244_r1_loop11_target_aliases.csv`
- `round244_r1_loop11_score_adjustments.csv`
- `round244_r1_loop11_shadow_weights.csv`
- `round244_r1_loop11_deep_sub_archetypes.csv`
- `round244_r1_loop11_price_validation_fields.csv`
- `round244_r1_loop11_green_gate_review.md`
- `round244_r1_loop11_price_validation_plan.md`
- `round244_r1_loop11_stage4b_4c_review.md`

## 검증

실행한 핵심 검증:

```bash
PYTHONPATH=src python -m py_compile \
  src/e2r/sector/archetypes.py \
  src/e2r/sector/round244_r1_loop11_industrial_orders_infra_price_validation.py \
  src/e2r/cli/build_round244_r1_loop11_report.py \
  tests/test_round244_r1_loop11_industrial_orders_infra_price_validation.py

PYTHONPATH=src python -m unittest tests.test_round244_r1_loop11_industrial_orders_infra_price_validation -v

PYTHONPATH=src python -m e2r.cli.build_round244_r1_loop11_report
```

최종 전체 테스트와 `git diff --check`는 커밋 전 검증 단계에서 수행한다.

## 변경하지 않은 것

- 생산 scoring threshold 변경 없음
- StageClassifier threshold 변경 없음
- case library를 candidate generation 입력으로 사용하지 않음
- round case를 종목명 하드코딩 규칙으로 사용하지 않음
- full OHLC가 없는 MFE/MAE를 조작하지 않음

## 다음 작업

Round 244는 R1 산업재·수주·인프라 케이스에서 “수주 headline과 Stage 3를 분리하는” 가격검증 팩이다. 다음에는 full OHLC backfill로 `price_validation_status`를 갱신하고, R1 케이스들이 실제 Stage 2/4B/4C shadow scoring에서 어떤 gate를 통과하거나 실패하는지 비교해야 한다.
