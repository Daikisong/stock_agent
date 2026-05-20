# Checkpoint 28A Round 293 R11 Loop 14 Policy Geopolitics Disaster Event Price Validation

## 반영 범위

- 입력 문서: `docs/round/round_293.md`
- analyst round id: `round_221`
- 대섹터: `POLICY_GEOPOLITICS_DISASTER_EVENT`
- 생산 점수 변경: 없음
- candidate generation 입력 사용: 없음
- 적용 방식: `shadow_weight_only`

이번 라운드는 정책·지정학·재난 이벤트를 “뉴스가 크다”로 보지 않고, 실제 법안·예산·제재 해소·손익·현금흐름·서비스/생산 연속성으로 닫혔는지 검증하는 팩이다. 예를 들어 `동해 가스전 14B boe 가능성`은 가격을 크게 움직일 수 있지만, 시추 결과와 경제성, CAPEX/IRR이 없으면 Stage 3-Green이 아니다.

## 추가된 Canonical Archetype

- `RESOURCE_DISCOVERY_POLICY_EVENT_PREMIUM`
- `GEOPOLITICAL_SANCTIONS_SUPPLY_CHAIN_4C`
- `POLITICAL_LIQUIDITY_SHOCK_HARD_REFERENCE`
- `TAX_POLICY_MARKET_CONFIDENCE_4C`
- `MARKET_ACCESS_REFORM_STAGE2`
- `MEDICAL_REFORM_SERVICE_DISRUPTION_4C_REFERENCE`
- `NATURAL_DISASTER_RECOVERY_POLICY_REFERENCE`
- `GEOPOLITICAL_DEFENSE_ORDER_STAGE2`
- `LABOR_POLICY_SYSTEMIC_EXPORT_RISK_4C`

## 케이스 요약

| case | 판정 | 핵심 |
|---|---|---|
| Korea Gas / Blue Whale | event premium + 4B-watch | KOGAS +30%, 14B boe 가능성, 성공확률 20%. 시추·경제성·CAPEX/IRR 전에는 Green 금지 |
| Hanwha Ocean China sanctions | hard 4C-watch | 중국 제재로 거래/협력 제한, Hanwha Ocean -5.8%. 수주잔고보다 counterparty 접근성이 먼저 |
| Martial law liquidity shock | hard reference | KOSPI -1.4%~nearly -2%, 10T 주식 안정기금, 40T 채권 안정기금. 정치 유동성은 전 섹터 hard gate |
| Tax policy / AI windfall tax | market-confidence 4C-watch | 세제 패키지 KOSPI -3.9%, AI tax 발언 장중 -5%. Value-Up/AI narrative도 세제 일관성이 필요 |
| Short-selling / market access | Stage 2 | 공매도 정상화, MSCI accessibility 개선, 100% order penalty. Green은 외국인 flow와 증권사 실적 확인 후 |
| Medical reform doctors strike | service-disruption reference | 전공의 9,000명 walkout, 수술 취소, 군의관/공보의 투입. 정책 목적이 좋아도 서비스 capacity가 깨지면 Green 불가 |
| 2025 wildfires | disaster reference | 28명 사망, 118,265 acres 소실, 3만명 이상 이재민. 복구 수혜는 claims, 예산, 계약, margin 확인 필요 |
| Hanwha Aerospace Romania K9 | defense order Stage 2 | $1B Romania K9 order, backlog 5.1T→30T KRW, +5%. 납품, margin, cash collection, dilution-adjusted EPS 필요 |
| Samsung strike risk | systemic export 4C-watch | 18일 파업 위협, 1일 중단 손실 최대 1T KRW, 장기 피해 100T KRW. 생산 연속성 확인 전 Green 불가 |

## Green Gate 보정 방향

올릴 축:

- policy implementation certainty
- legal / regulatory finality
- geopolitical counterparty risk
- sanction / export-control exposure
- political liquidity risk
- tax policy consistency
- market access foreign flow
- service continuity under policy
- disaster damage to cashflow
- labor continuity systemic risk

내릴 축:

- government announcement only
- presidential headline only
- resource estimate without drilling
- policy beneficiary theme only
- sanction ignored order backlog
- tax reform without market consistency
- market access reform without foreign flow
- disaster recovery without budget/contract
- defense order without delivery/margin

## 4B / 4C 해석

- `4B-watch`: 자원 발표 후 +20~30%, 방산 수주 record high, 세제 완화 기대, 시장접근성 개혁 선반영, 재난 복구 테마처럼 가격이 증거보다 먼저 가는 상태.
- `hard 4C`: 계엄·헌정 위기, 외국 제재로 거래/협력 차단, 투자자 수익률을 훼손하는 세제 충격, 전국 의료서비스 disruption, 대형 재난, 시스템 수출기업 장기 파업 리스크.

## 생성 산출물

- `data/e2r_case_library/cases_r11_loop14_round293.jsonl`
- `data/sector_taxonomy/round293_r11_loop14_policy_geopolitics_disaster_event_price_validation_audit.json`
- `output/e2r_round293_r11_loop14_policy_geopolitics_disaster_event_price_validation/round293_r11_loop14_price_validation_summary.md`
- `output/e2r_round293_r11_loop14_policy_geopolitics_disaster_event_price_validation/round293_r11_loop14_case_matrix.csv`
- `output/e2r_round293_r11_loop14_policy_geopolitics_disaster_event_price_validation/round293_r11_loop14_shadow_weights.csv`
- `output/e2r_round293_r11_loop14_policy_geopolitics_disaster_event_price_validation/round293_r11_loop14_green_gate_review.md`
- `output/e2r_round293_r11_loop14_policy_geopolitics_disaster_event_price_validation/round293_r11_loop14_stage4b_4c_review.md`

## 검증

```bash
PYTHONPATH=src python -m unittest tests/test_round293_r11_loop14_policy_geopolitics_disaster_event_price_validation.py -v
PYTHONPATH=src python -m e2r.cli.build_round293_r11_loop14_report
PYTHONPATH=src python -m unittest discover -s tests -v
```

## 다음 라운드에 남긴 기준

R11은 정책 headline을 좋아하는 라운드가 아니다. 쉽게 말해 “정부가 한다고 말했다”는 Stage 1이고, “법·예산·집행·회사 손익·현금흐름·가격경로가 닫혔다”가 Stage 3 후보가 된다. 제재, 정치 유동성, 의료서비스 disruption, 재난, 노동 리스크는 긍정 증거가 아니라 Green을 막는 RedTeam 입력이다.
