# Checkpoint 28A Round 59: R6 Loop 2 금융·자본배분·디지털금융

## 반영 요약

- 원문: `docs/round/round_59.md`
- 신규 calibration 모듈: `src/e2r/sector/round59_r6_loop2_financial_capital_digital.py`
- 신규 CLI: `src/e2r/cli/build_round59_r6_loop2_report.py`
- 신규 테스트: `tests/test_round59_r6_loop2_financial_capital_digital.py`
- 케이스 팩: `data/e2r_case_library/cases_r6_loop2_round59.jsonl`
- 점수 비중 초안: `data/sector_taxonomy/score_weight_profiles_round59_r6_loop2_v2.csv`
- 산출물 디렉터리: `output/e2r_round59_r6_loop2_financial_capital_digital/`

## 핵심 판단

R6 Loop 2는 `저PBR`, `밸류업`, `자사주`, `사용자 수`, `스테이블코인` 같은 이름표를 실제 E2R 증거와 분리한다.

쉬운 예시:

- `자사주 매입 발표`는 Stage 1~2 신호일 수 있다.
- 하지만 `실제 소각 + ROE 개선 + 반복 배당/환원 + PBR-ROE band 변화`가 없으면 Stage 3-Green 근거로 쓰면 안 된다.
- `스테이블코인 사업 진출`도 뉴스만 있으면 Watch다. 준비금, 상환 가능성, 실제 발행량, 거래량, 수수료 모델이 확인되어야 한다.

## 추가된 archetype / overlay

- `GOVERNANCE_EXECUTION_FAILURE_OVERLAY`
- `TAX_POLICY_MARKET_SHOCK_OVERLAY`
- `STABLECOIN_CONVERTIBILITY_OVERLAY`

이 3개는 positive score bucket이 아니라 RedTeam gate다.

## Round 59 coverage

- target_count: 13
- case_candidate_count: 15
- success_candidate_count: 5
- event_premium_count: 4
- stage4c_case_count: 6
- green_possible_count: 2
- watch_yellow_first_count: 6
- redteam_first_count: 5
- gate_only_target_count: 3

## 주요 케이스

- `korea_commercial_act_treasury_cancel_case`: 밸류업 정책 배경. 개별 종목 Green은 실제 소각/ROE 필요.
- `sk_square_buyback_cancel_case`: NAV discount + 실제 소각 + 독립이사. 지주사 value-up 실행 후보.
- `samsung_electronics_buyback_case`: buyback-only rebound. 사업 경쟁력과 EPS/FCF는 별도 gate.
- `korea_zinc_tender_offer_event_case`: 공개매수 가격반응은 event premium이지 구조적 value-up이 아님.
- `korea_tax_policy_shock_case`: 거래세/양도세/법인세 shock은 증권·밸류업 rally의 4C-watch.
- `boe_stablecoin_convertibility_case`: 준비금/상환/convertibility 불확실성은 stablecoin RedTeam gate.
- `terrausd_do_kwon_case`: algorithmic stablecoin collapse는 hard 4C 기준.

## Green Guardrails

- 낮은 PBR만으로 Green 금지.
- 밸류업 지수 편입만으로 Green 금지.
- 자사주 매입을 소각과 동일시 금지.
- 공개매수·경영권 분쟁을 구조적 value-up으로 오분류 금지.
- 핀테크 사용자 수를 take rate/FCF로 대체 금지.
- 스테이블코인/STO 법안 뉴스를 실제 금융 인프라 매출로 대체 금지.
- ROE, CET1, K-ICS, CSM, 자사주 소각 규모, take rate, 준비금, 거래량, stage price는 비어 있으면 비워 둔다.

## 검증

실행한 테스트:

```bash
PYTHONPATH=src python -m unittest tests.test_round59_r6_loop2_financial_capital_digital -v
```

결과:

- 13개 테스트 통과

## 다음 단계

R7 Loop 2로 넘어가기 전까지 R6는 production scoring을 바꾸지 않는다. 이번 산출물은 예를 들어 “은행은 ROE/CET1/credit cost, 핀테크는 take rate/FCF, 스테이블코인은 준비금/상환”처럼 향후 shadow scoring과 price-path backfill에서 확인할 체크리스트다.
