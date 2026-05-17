# Checkpoint 28A Round 138 R6 Loop 8 Financial / Capital / Digital

## 목적

`docs/round/round_138.md`의 R6 Loop 8 내용을 별도 calibration pack으로 반영했다.

R6는 금융, 자본배분, 밸류업, 지주사 NAV, 핀테크, 스테이블코인, 디지털자산 거래소 노출을 다룬다. 이번 라운드의 핵심은 “싸다”와 “할인 요인이 실제로 제거된다”를 분리하는 것이다.

쉬운 예시는 다음과 같다.

- `저PBR 은행주`는 Stage 1 신호일 수 있다.
- 하지만 ROE, CET1, credit cost, PF exposure, 실제 배당·소각 실행이 확인되지 않으면 Stage 3-Green 근거가 아니다.
- `자사주 매입`은 `자사주 소각 완료`와 다르다. 소각 후에도 본업 EPS/FCF가 약하면 Green을 막는다.
- `스테이블코인 법안`은 옵션이고, reserve, redemption, circulation, fee/reserve income, issuer margin이 확인되어야 높은 단계로 올라간다.
- `거래소 지분투자`는 Stage 1~2 근거지만, 지분법이익·협업매출·보안사고 부재가 확인되기 전에는 Stage 3 근거가 아니다.

## 반영 파일

- `src/e2r/sector/round138_r6_loop8_financial_capital_digital.py`
- `src/e2r/cli/build_round138_r6_loop8_report.py`
- `tests/test_round138_r6_loop8_financial_capital_digital.py`
- `data/e2r_case_library/cases_r6_loop8_round138.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round138_r6_loop8_v8.csv`
- `output/e2r_round138_r6_loop8_financial_capital_digital/`

## v8 기본 점수축

| component | weight | 해석 |
| --- | ---: | --- |
| roe_eps_fcf_durability | 22 | 저PBR이 아니라 ROE/EPS/FCF 지속성이 Stage 3 핵심 |
| capital_return_execution | 18 | 계획보다 실제 소각, 배당 확대, 반복 환원정책을 중시 |
| capital_ratio_credit_cost_stability | 18 | CET1, K-ICS, PF exposure, reserve build, credit cost는 hard gate |
| regulated_revenue_model_visibility | 14 | stablecoin reserve/redemption, exchange fee/custody/tokenization, fintech take rate |
| market_mispricing_rerating_gap | 8 | old low-PBR frame 또는 non-bank discount가 실제 실행 후에도 남아 있는지 확인 |
| valuation_room_4b_runway | 8 | value-up, stablecoin IPO, exchange stake narrative가 이미 crowded인지 확인 |
| information_security_governance_confidence | 12 | governance execution, disclosure detail, exchange security, reserve design, regulation 강화 |

## 케이스 방향

- Stage 1~2 tailwind: `Korea Commercial Act treasury cancellation mandate`
- Stage 2 후보: `SK Square buyback cancellation`, `Hana Bank-Dunamu stake`
- Stage 2~3 후보 + 4B-watch: `Circle / USDC regulated stablecoin infra`
- 실패/RedTeam: `Samsung Electronics cancellation but business risk`, `Samsung C&T activist rejection`, `PF credit cost`, `Clear Street IPO valuation cut`, `Bybit hack`, `TerraUSD/Luna`, `BoE stablecoin rule`, `AI citizen dividend policy shock`

## Guardrail

- production scoring은 변경하지 않았다.
- case record는 candidate-generation input이 아니다.
- 저PBR, 밸류업 지수 편입, 자사주 매입, IPO 기대, 원화 스테이블코인 법안, 거래소 지분투자, 거래소 점유율만으로 Green을 만들지 않는다.
- Stage 3는 ROE/PBR band 변화, 반복 환원정책, credit cost 안정, FCF·자본비율 유지, regulated revenue economics, 실제 가격경로 동행을 요구한다.
- exchange hack, de-peg, reserve failure, PF credit spike, activist rejection, IPO valuation cut, policy shock은 RedTeam overlay로 유지한다.

## 검증

실행한 명령:

```bash
PYTHONPATH=src python -m unittest tests/test_round138_r6_loop8_financial_capital_digital.py -v
PYTHONPATH=src python -m e2r.cli.build_round138_r6_loop8_report
```

결과:

- Round 138 전용 테스트 14개 통과
- v8 score profile 생성
- case JSONL 생성
- summary, guardrail, risk overlay, price validation, stage cap, score-stage-price alignment 리포트 생성
