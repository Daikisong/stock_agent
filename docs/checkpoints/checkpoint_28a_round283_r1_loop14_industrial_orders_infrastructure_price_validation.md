# Checkpoint 28A Round 283 R1 Loop 14 Industrial Orders Infrastructure Price Validation

## 반영 범위

- 원문: `docs/round/round_283.md`
- analyst round id: `round_211`
- large sector: `INDUSTRIALS_ORDERS_INFRASTRUCTURE`
- production scoring changed: false
- candidate generation input: false
- shadow weight only: true
- price validation: partial with reported price anchors
- full adjusted OHLC: false

이번 라운드는 산업재·수주·인프라에서 `수주`, `방산`, `전력망`, `조선`, `로봇`, `IPO` 같은 좋은 단어가 Stage 3-Green을 자동으로 만들지 않도록 검증팩을 추가했다.

쉬운 예: `수주 공시`는 Stage 1/2 신호가 될 수 있지만, 실제 납품과 매출 인식, 마진, 운전자본, 현금회수가 확인되기 전에는 Green 근거가 아니다.

## 추가된 canonical archetype

- `DEFENSE_EXPORT_DELIVERY_STAGE3_CANDIDATE`
- `GRID_EQUIPMENT_US_GROWTH_STAGE2`
- `TRANSFORMER_CAPACITY_EXPANSION_STAGE2`
- `SHIPBUILDING_MERGER_MASGA_4B`
- `SHIPBUILDING_ORDER_CANCELLATION_HARD_4C`
- `DEFENSE_DILUTION_FALSE_POSITIVE`
- `ROBOTICS_STRATEGIC_STAKE_EVENT_PREMIUM`
- `INDUSTRIAL_SERVICE_IPO_OVERHEAT`

## 추가된 케이스

| case | 판정 | 핵심 |
|---|---|---|
| Hyundai Rotem K2 Poland | aligned partial Stage 3 candidate | 18대 납품, Q1 매출 270B KRW, OP 추정 59.1B KRW, 주가 +9.3% |
| LS Electric US grid | evidence good but price failed | 미국 매출 비중/목표가 상향은 좋지만 이벤트 가격 -5.4% |
| Hyosung Heavy/HICO | Stage 2 success candidate | GSU 수요 +274%, 납기 143주, Memphis 증설 $157M, 주가 anchor 부족 |
| HD HHI/Mipo merger | event premium / 4B-watch | MASGA·합병 테마로 +11.3%/+14.6%, 실제 미국 주문/시너지 전 |
| Samsung Heavy/Zvezda | hard 4C | 4.85T KRW / $3.54B 계약취소, arbitration/sanctions risk |
| Hanwha Aerospace share sale | false positive / 4B-watch | 3.6T KRW 증자 계획, -13%, FSS filing-quality gate |
| Rainbow Robotics/Samsung | event premium | 267B KRW 지분투자, 실제 출하/ASP/margin 전 |
| HD Hyundai Marine IPO | IPO overheat / 4B-watch | IPO 83,400 → 163,900 KRW, +96.5%, post-IPO durability gate |

## 산출물

- `data/e2r_case_library/cases_r1_loop14_round283.jsonl`
- `data/sector_taxonomy/round283_r1_loop14_industrial_orders_infrastructure_price_validation_audit.json`
- `output/e2r_round283_r1_loop14_industrial_orders_infrastructure_price_validation/round283_r1_loop14_price_validation_summary.md`
- `output/e2r_round283_r1_loop14_industrial_orders_infrastructure_price_validation/round283_r1_loop14_case_matrix.csv`
- `output/e2r_round283_r1_loop14_industrial_orders_infrastructure_price_validation/round283_r1_loop14_shadow_weights.csv`
- `output/e2r_round283_r1_loop14_industrial_orders_infrastructure_price_validation/round283_r1_loop14_green_gate_review.md`
- `output/e2r_round283_r1_loop14_industrial_orders_infrastructure_price_validation/round283_r1_loop14_stage4b_4c_review.md`

## Green gate 교정

강화해야 할 축:

- actual delivery revenue
- backlog-to-revenue conversion
- order margin visibility
- working-capital control
- local production execution
- capacity utilization
- customer financing visibility
- dilution-adjusted EPS
- contract cancellation risk
- aftermarket IPO demand

제한해야 할 패턴:

- order headline only
- customer/parent name only
- strategic stake only
- capacity expansion without backlog
- IPO first-day pop only
- merger theme without synergy
- defence order expectation without funding
- dilutive share issue
- geopolitical contract execution risk

## 4B / 4C 교훈

- `HD HHI/Mipo`: 합병/MASGA headline로 급등하면 4B-watch다. 실제 funded US order와 integration margin이 필요하다.
- `HD Hyundai Marine`: 첫날 +96.5% IPO는 좋은 사업과 별개로 4B-watch다. 상장 후 수요와 실적 지속성을 봐야 한다.
- `Samsung Heavy`: 큰 backlog도 취소·제재·arbitration으로 실행 불가능해지면 hard 4C다.
- `Hanwha Aerospace`: 방산 주문 기대가 강해도 대형 증자와 공시 품질 이슈는 dilution-adjusted EPS gate다.

## 검증

실행한 명령:

```bash
PYTHONPATH=src python -m unittest tests.test_round283_r1_loop14_industrial_orders_infrastructure_price_validation -v
PYTHONPATH=src python -m e2r.cli.build_round283_r1_loop14_report
```

라운드 단위 테스트는 통과했다. 전체 테스트는 최종 커밋 전 별도로 실행한다.

## 남은 일

- 이번 팩은 가격 anchor 기반 partial validation이다. 전체 조정 OHLC, 30D/90D/180D/1Y MFE/MAE는 아직 backfill해야 한다.
- 생산 점수 로직에는 반영하지 않았다. 예를 들어 `actual_delivery_revenue +5`는 shadow weight로만 저장됐고, StageClassifier threshold는 바뀌지 않았다.
- 다음 R1 반복에서는 수주가 매출·마진·현금으로 닫히는지 확인하는 price-path backfill이 필요하다.
