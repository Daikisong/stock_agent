# Checkpoint 28A Round 125 - R6 Loop 7 Financial / Capital / Digital

## 반영 요약

- 입력 문서: `docs/round/round_125.md`
- 추가 모듈: `src/e2r/sector/round125_r6_loop7_financial_capital_digital.py`
- 추가 CLI: `src/e2r/cli/build_round125_r6_loop7_report.py`
- 추가 테스트: `tests/test_round125_r6_loop7_financial_capital_digital.py`
- 산출 케이스: `data/e2r_case_library/cases_r6_loop7_round125.jsonl`
- 산출 점수표: `data/sector_taxonomy/score_weight_profiles_round125_r6_loop7_v7.csv`
- 산출 리포트: `output/e2r_round125_r6_loop7_financial_capital_digital/`

## 핵심 판단

Round 125는 금융, 자본배분, 디지털금융에서 `싸다`와 `할인 요인이 실제로 제거된다`를 분리한다.

쉬운 예시는 다음과 같다.

- `저PBR 은행주`는 Stage 1 재료다.
- `ROE 개선 + CET1 안정 + PF 신용비용 안정 + 실제 소각/배당 확대`가 같이 있어야 Stage 2/3 검토가 가능하다.
- `스테이블코인 법안`은 Stage 1 옵션이다. Stage 3 후보가 되려면 승인, 준비금, 상환, 유통량, 수수료/준비금 수익이 보여야 한다.
- `거래소 지분 투자`는 전략적 옵션이다. 지분법이익, 협업 매출, 규제 승인, 보안 이슈가 확인되기 전에는 Green 증거가 아니다.

## 추가된 Loop 7 축

- `roe_eps_fcf_durability`: 22
- `capital_return_execution`: 18
- `capital_ratio_credit_cost_stability`: 18
- `regulated_revenue_model_visibility`: 14
- `market_mispricing_rerating_gap`: 10
- `valuation_room_4b_runway`: 8
- `information_security_governance_confidence`: 10

이 값은 프로덕션 점수에 적용하지 않았다. 케이스 라이브러리와 shadow calibration용 자료다.

## Stage Cap

- Stage 1 cap: 저PBR, value-up, 자사주 기대, 스테이블코인 법안, IPO 기대, 거래소 지분 루머만 있는 경우
- Stage 2 cap: 실제 소각/배당 확대, CET1/K-ICS 안정, 지분 취득, 스테이블코인 유통량/준비금 수익, IPO valuation filing
- Stage 3 후보: ROE/PBR band 변화, 반복 환원, 신용비용 안정, 자본비율 유지, 규제된 디지털금융 수익모델, 가격경로 동행
- 4B-watch: value-up, 스테이블코인 인프라, 디지털자산 거래소 노출이 이미 과도하게 가격에 반영된 경우
- 4C: PF 신용비용, activist rejection, 소각 이후 사업 실패, IPO valuation cut, 거래소 해킹, de-peg, 준비금 실패, 세제 충격

## 케이스 정합성

- `sk_square_buyback_cancel_case`: NAV discount와 실제 소각 실행은 Stage 2 증거로 둔다.
- `samsung_electronics_treasury_cancel_case`: 소각은 있었지만 가격경로와 사업 EPS/FCF가 따라오지 않으면 failed rerating으로 둔다.
- `hana_bank_dunamu_stake_case`: 거래소 지분 취득은 Stage 2 옵션으로 보되 지분법이익과 협업 매출 전에는 Stage 3을 막는다.
- `circle_usdc_stablecoin_earnings_case`: regulated stablecoin infra 후보지만 IPO 이후 과열과 규제 경제성 gate를 동시에 둔다.
- `korea_pf_credit_cost_overlay_case`: PF 연체율과 충당금은 value-up 금융주 Green을 막는 hard gate다.
- `clear_street_ipo_valuation_cut_case`: IPO size/valuation cut은 fintech optionality의 4C-watch다.
- `bybit_exchange_hack_case`: 거래소 보안 사고는 시장점유율 이야기보다 우선하는 hard 4C다.
- `terrausd_do_kwon_case`: algorithmic stablecoin은 fiat-backed regulated stablecoin과 분리해 hard RedTeam으로 둔다.

## 산출 파일

- `round125_r6_loop7_financial_capital_digital_summary.md`
- `round125_r6_loop7_case_matrix.csv`
- `round125_r6_loop7_stage_date_plan.csv`
- `round125_r6_loop7_green_guardrails.md`
- `round125_r6_loop7_risk_overlays.md`
- `round125_r6_loop7_price_validation_plan.md`
- `round125_r6_loop7_price_fields.csv`
- `round125_r6_loop7_base_score_weights.csv`
- `round125_r6_loop7_stage_caps.csv`
- `round125_r6_loop7_score_stage_price_alignment.csv`
- `round125_r6_loop7_score_stage_price_alignment.md`

## Guardrail

- 케이스 기록은 후보 생성 입력이 아니다.
- 프로덕션 scoring/staging/RedTeam 로직은 round125 팩을 import하지 않는다.
- Stage 3-Green 기준을 낮추지 않았다.
- ROE, CET1, K-ICS, PF 연체율, 소각금액, 준비금, 유통량, 지분법이익, 보안 상태, stage price는 새로 꾸며 넣지 않았다.

## 검증

- `PYTHONPATH=src python -m unittest tests/test_round125_r6_loop7_financial_capital_digital.py -v`
- `PYTHONPATH=src python -m e2r.cli.build_round125_r6_loop7_report`

