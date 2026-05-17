# Checkpoint 28A Round 72 R6 Loop 3: Financial / Capital / Digital

## 목적

Round 72는 금융·자본배분·디지털금융 영역에서 `저PBR`, `밸류업`, `사용자 수`, `스테이블코인`, `거래소 인수` 같은 이름표와 실제 rerating 증거를 분리하기 위한 케이스 팩이다.

쉬운 예로 `저PBR 은행`은 Stage 1 신호일 뿐이다. Stage 2/3 후보가 되려면 `ROE 개선 + CET1 안정 + credit cost 안정 + 배당/소각 실행`이 같이 확인되어야 한다.

## 반영 파일

- `src/e2r/sector/round72_r6_loop3_financial_capital_digital.py`
- `src/e2r/cli/build_round72_r6_loop3_report.py`
- `tests/test_round72_r6_loop3_financial_capital_digital.py`
- `data/e2r_case_library/cases_r6_loop3_round72.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round72_r6_loop3_v3.csv`
- `output/e2r_round72_r6_loop3_financial_capital_digital/`

## 분류 요약

- target_count: 16
- case_candidate_count: 15
- Green possible targets: 2
- Watch / Yellow-first targets: 8
- RedTeam-first targets: 6
- gate-only overlays: 4

## Green 가능 축

- `FINANCIAL_SPREAD_BALANCE_SHEET`
- `INSURANCE_UNDERWRITING_CYCLE`

은행·금융지주는 `ROE`, `CET1`, `credit cost`, `PF exposure`, `반복 환원`을 같이 봐야 한다. 보험은 `CSM quality`, `K-ICS`, `손해율`, `대체투자 손실`, `환원 실행`을 따로 봐야 한다.

## Watch / Yellow-first 축

- `SECURITIES_BROKERAGE_CYCLE`
- `VALUE_UP_SHAREHOLDER_RETURN`
- `HOLDING_RESTRUCTURING_GOVERNANCE`
- `PAYMENT_FINTECH_INFRA`
- `DIGITAL_ASSET_TOKENIZATION`
- `REGULATED_STABLECOIN_INFRA`
- `CREDIT_DATA_INFRA`
- `DIGITAL_ASSET_EXCHANGE_CONSOLIDATION`

예를 들어 `Toss 사용자 3,000만 명`은 Stage 1에는 유용하지만, Green 증거가 되려면 거래액, take rate, FCF, 보안, 신용손실이 확인되어야 한다. `Circle/USDC`류도 regulated stablecoin 인프라 후보지만, 준비금·상환·발행량·거래량·수수료 모델 전에는 Green을 제한한다.

## RedTeam 오버레이

- `EVENT_PREMIUM_GOVERNANCE_BATTLE`
- `ALGORITHMIC_STABLECOIN_FAILURE`
- `TAX_POLICY_MARKET_SHOCK_OVERLAY`
- `GOVERNANCE_EXECUTION_FAILURE_OVERLAY`
- `STABLECOIN_CONVERTIBILITY_OVERLAY`
- `VC_EXIT_MARKET_CYCLE`

`Korea Zinc 공개매수`처럼 가격이 크게 움직여도 우선 event premium이다. `TerraUSD/Luna`처럼 algorithmic stablecoin이 de-peg 또는 reserve failure를 보이면 hard 4C로 본다.

## 케이스 팩

추가한 주요 케이스:

- `korea_commercial_act_treasury_cancel_case`
- `sk_square_buyback_cancel_case`
- `samsung_electronics_treasury_cancel_case`
- `samsung_ct_activist_rejection_case`
- `korea_zinc_tender_offer_event_case`
- `korea_zinc_share_issue_probe_case`
- `korea_tax_policy_shock_case`
- `ai_windfall_tax_comment_case`
- `stripe_payment_infra_profit_case`
- `mynt_gcash_ipo_case`
- `toss_global_stablecoin_case`
- `circle_stablecoin_ipo_valuation_case`
- `boe_stablecoin_rules_reconsider_case`
- `terrausd_do_kwon_case`
- `naver_dunamu_upbit_deal_case`

월 단위나 연도 범위만 있는 케이스는 날짜를 만들지 않았다. 예를 들어 `AI windfall tax comment`는 2026년 5월 수준으로만 주어졌기 때문에 `stage4c_date=null`로 두고 `needs_exact_stage_date_backfill`로 표시했다.

## 안전 원칙

- production scoring 변경 없음.
- case library는 candidate generation input이 아님.
- Stage 3-Green threshold를 낮추지 않음.
- ROE, CET1, K-ICS, CSM, 소각금액, take rate, FCF, stablecoin volume, reserve ratio, exchange security status, stage price를 만들지 않음.
- 공개매수, 행동주의 거부, 미소각, 세금정책 shock, de-peg, 준비금 실패, 비정상 출금은 RedTeam 필드로 유지.

## 검증

실행 명령:

```bash
PYTHONPATH=src python -m unittest tests.test_round72_r6_loop3_financial_capital_digital -v
PYTHONPATH=src python -m e2r.cli.build_round72_r6_loop3_report
PYTHONPATH=src python -m compileall -q src tests
PYTHONPATH=src python -m unittest discover -s tests -v
git diff --check
```

전체 테스트를 통과한 뒤 커밋했다.
