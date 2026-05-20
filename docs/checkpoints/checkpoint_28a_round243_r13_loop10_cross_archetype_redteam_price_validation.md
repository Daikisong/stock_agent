# Checkpoint 28A Round 243 R13 Loop 10 Cross-Archetype RedTeam Price Validation

## 목적

`docs/round/round_243.md`를 R13 Loop 10 교차 아키타입 RedTeam / 가격 검증 팩으로 구조화했다. 이번 작업은 케이스 라이브러리와 shadow calibration 산출물만 추가하며, 생산 scoring, staging, candidate generation은 바꾸지 않는다.

쉬운 예시:

- `SK하이닉스`처럼 Stage 3 이후 큰 MFE가 확인된 사례는 구조적 성공 기준점이 된다. 다만 이후 시가총액·crowding headline이 붙으면 신규 Green이 아니라 4B-watch로 봐야 한다.
- `삼성SDS`처럼 KKR CB와 AI 투자 이벤트로 하루 +20%가 나와도, 반복 AI 매출·마진·FCF가 확인되기 전에는 Stage 2 / 4B-watch다.
- `L&F`처럼 큰 고객명과 계약 headline이 있어도 실제 call-off, volume, margin, FCF 없이 계약 가치가 무너지면 hard 4C다.

## 반영 파일

- `src/e2r/sector/archetypes.py`
- `src/e2r/sector/round243_r13_loop10_cross_archetype_redteam_price_validation.py`
- `src/e2r/cli/build_round243_r13_loop10_report.py`
- `tests/test_round243_r13_loop10_cross_archetype_redteam_price_validation.py`
- `data/e2r_case_library/cases_r13_loop10_round243.jsonl`
- `data/sector_taxonomy/round243_r13_loop10_cross_archetype_redteam_price_validation_audit.json`
- `output/e2r_round243_r13_loop10_cross_archetype_redteam_price_validation/`

## 추가한 아키타입

Round 243에서 필요한 교차 RedTeam 아키타입을 canonical enum에 추가했다.

- `AI_CAPITAL_ALLOCATION_EVENT_PREMIUM`
- `POLICY_CAPEX_FALSE_POSITIVE`
- `CONTRACT_QUALITY_HARD_4C`
- `OPERATIONAL_SAFETY_HARD_4C`
- `MACRO_GEOPOLITICAL_HARD_4C`
- `DIGITAL_ASSET_POLICY_OVERHEAT`
- `PRICE_MOVED_WITHOUT_EVIDENCE`

기존 성공/경고 아키타입인 `STRUCTURAL_SUCCESS_ALIGNED`, `STRUCTURAL_SUCCESS_BUT_4B_WATCH`, `CROWDED_RERATING_4B_WATCH`, `EVIDENCE_GOOD_BUT_PRICE_FAILED`와 함께 Round 243 target alias 11개를 모두 매핑했다.

## 케이스 요약

총 8개 케이스를 추가했다.

| case | 해석 |
|---|---|
| SK하이닉스 HBM | Stage 3 성공 benchmark이지만 2026년 큰 rerating 이후 4B-watch 필요 |
| APR / Medicube | K-beauty device 해외 매출 전환 성공 후보이지만 매출 집중도와 valuation 4B-watch |
| 삼성SDS KKR AI 이벤트 | AI capital allocation event premium, 반복 AI 매출 전 Green 금지 |
| 현대제철 미국 CAPEX | 정책 CAPEX false-positive, funding/margin/FCF 불명확 시 Green 금지 |
| L&F Tesla 양극재 계약 | 계약 가치 붕괴 hard 4C |
| 제주항공 안전사고 | fatal safety accident hard 4C |
| Hormuz / Iran shock | 에너지·운송·제조·환율을 덮는 macro hard 4C overlay |
| KRW stablecoin basket | 발행권·reserve income 전 price_moved_without_evidence |

## Green Guardrails

Round 243은 Green을 쉽게 만들기 위한 작업이 아니다. Green 후보는 최소한 다음을 확인해야 한다.

- 회사 단위 증거
- 매출, EPS, 또는 FCF 전환
- 증거 이후 가격경로
- Stage 3 이후 MFE 확인
- 과도한 MAE 부재
- 4B 포화 구간 아님
- hard RedTeam 부재
- 계약, 운영, 거버넌스, 보안 신뢰 통과

반대로 다음은 Green 금지 패턴이다.

- 정책 뉴스만 존재
- stablecoin 테마만 존재
- 반복 AI 매출 없는 AI capital allocation 이벤트
- 실제 call-off 없는 계약 headline
- funding/margin 불명확한 CAPEX
- 매출 전환 없는 M&A/CB 이벤트
- IPO/debut 프리미엄
- 가격 검증 없는 높은 점수
- fatal safety accident
- 거시 지정학 shock 무시

## 산출물

생성한 산출물은 다음과 같다.

- `round243_r13_loop10_price_validation_summary.md`
- `round243_r13_loop10_case_matrix.csv`
- `round243_r13_loop10_target_aliases.csv`
- `round243_r13_loop10_score_adjustments.csv`
- `round243_r13_loop10_shadow_weights.csv`
- `round243_r13_loop10_deep_sub_archetypes.csv`
- `round243_r13_loop10_price_validation_fields.csv`
- `round243_r13_loop10_green_gate_review.md`
- `round243_r13_loop10_price_validation_plan.md`
- `round243_r13_loop10_stage4b_4c_review.md`

## 검증

실행한 핵심 검증:

```bash
PYTHONPATH=src python -m py_compile \
  src/e2r/sector/archetypes.py \
  src/e2r/sector/round243_r13_loop10_cross_archetype_redteam_price_validation.py \
  src/e2r/cli/build_round243_r13_loop10_report.py \
  tests/test_round243_r13_loop10_cross_archetype_redteam_price_validation.py

PYTHONPATH=src python -m unittest tests.test_round243_r13_loop10_cross_archetype_redteam_price_validation -v

PYTHONPATH=src python -m e2r.cli.build_round243_r13_loop10_report
```

최종 전체 테스트와 `git diff --check`는 커밋 전 검증 단계에서 수행한다.

## 변경하지 않은 것

- 생산 scoring threshold 변경 없음
- StageClassifier threshold 변경 없음
- case library를 candidate generation 입력으로 사용하지 않음
- round case를 종목명 하드코딩 규칙으로 사용하지 않음
- full OHLC가 없는 가격·MFE·MAE를 조작하지 않음

## 다음 작업

Round 243은 R13 Loop 10의 RedTeam 가격 검증 기준점을 추가한 단계다. 다음에는 이 케이스들이 기존 R1~R12 아키타입별 case pack과 충돌하지 않는지 보고, full OHLC가 필요한 항목은 가격 backfill로 `price_validation_status`를 갱신해야 한다.
