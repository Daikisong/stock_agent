# Checkpoint 28A Round 296 R1 Loop 15 Industrial Trigger-Level Validation

## 반영 내용

- `docs/round/round_296.md`를 R1 Loop 15 산업재·수주·인프라 trigger-level validation pack으로 반영했다.
- 이번 라운드부터 case 하나에 Stage 하나만 붙이지 않고, T0~T6 trigger를 분해해서 어떤 trigger가 entry 후보였는지 기록한다.
- 신규 canonical archetype 7개를 추가했다.
  - `DEFENSE_EXPORT_STAGE2_ACTIONABLE`
  - `MISSILE_DEFENSE_ORDER_4B_TIMING`
  - `DEFENSE_BACKLOG_DILUTION_OVERLAY`
  - `SHIPBUILDING_BACKLOG_PRICE_STAGE2_ACTIONABLE`
  - `GRID_EQUIPMENT_US_GROWTH_STAGE2_PROMOTE`
  - `OVERSEAS_EPC_ORDER_STAGE2_YELLOW`
  - `NUCLEAR_EXPORT_PREFERRED_BIDDER_STAGE2`
- production scoring, StageClassifier, candidate generation은 변경하지 않았다.

## 핵심 원칙

- full adjusted OHLC가 없다는 이유만으로 Stage 후보를 강등하지 않는다.
- 대신 `price_data_unavailable_after_deep_search` 또는 `reported_event_anchor_not_full_ohlc`로 가격검증 상태를 분리한다.
- Stage3-Green은 확정하지 않았다.
- Stage2-Actionable과 Stage3-Yellow 후보를 새로 분리했다.

쉬운 예시:

`as_of_date=2024-04-09`에 현대 로템이 K2 출하, OP 추정치 상향, 매출 기여, 주가 상대강도를 동시에 보였다면 Stage2보다 강하게 볼 수 있다. 하지만 장기 delivery margin과 cash collection이 아직 없으면 Green은 아니다.

## 케이스 요약

| 케이스 | 판정 | 핵심 교훈 |
|---|---|---|
| Hyundai Rotem | Stage2-Actionable / Stage3-Yellow 후보 | 출하, OP estimate beat, revenue contribution, relative strength가 동시에 닫히면 plain Stage2보다 강하다. |
| LIG Nex1 | Stage2-Actionable + 4B timing audit | 1H +69% 후 downgrade는 4B trim 신호지만 신규 수주 pipeline이 살아 있으면 hard exit는 이르다. |
| Hanwha Aerospace | Stage3-Yellow + 4B overlay | backlog/order evidence가 강하면 Stage3 후보로 두고, 이후 증자 희석은 4B overlay로 병기한다. |
| Shipbuilding basket | Stage2-Actionable | 수주, 선가 지수, 3년 backlog, sector relative strength가 동시에 있으면 단순 event premium보다 강하다. |
| LS Electric | evidence good but price failed | target +87%와 미국 매출 mix evidence가 있어도 당일 -5.4%라 full-window retest가 필요하다. |
| Samsung E&A | Stage3-Yellow 후보 | $6B order와 상대강도는 강하지만 EPC execution margin, working capital, cash collection 전까지 Green은 아니다. |
| Czech nuclear | Stage2 + legal 4C-watch | preferred bidder는 final contract와 legal clearance 전까지 Green이 아니다. |

## 생성 파일

- `data/e2r_case_library/cases_r1_loop15_round296.jsonl`
- `data/e2r_trigger_calibration/triggers_r1_loop15_round296.jsonl`
- `data/sector_taxonomy/round296_r1_loop15_industrial_trigger_validation_audit.json`
- `output/e2r_round296_r1_loop15_industrial_trigger_validation/round296_r1_loop15_trigger_validation_summary.md`
- `output/e2r_round296_r1_loop15_industrial_trigger_validation/round296_r1_loop15_case_matrix.csv`
- `output/e2r_round296_r1_loop15_industrial_trigger_validation/round296_r1_loop15_trigger_grid.csv`
- `output/e2r_round296_r1_loop15_industrial_trigger_validation/round296_r1_loop15_shadow_weights.csv`
- `output/e2r_round296_r1_loop15_industrial_trigger_validation/round296_r1_loop15_stage_rules.md`
- `output/e2r_round296_r1_loop15_industrial_trigger_validation/round296_r1_loop15_stage4b_4c_review.md`

## Shadow 보정축

올릴 축:

- `shipment_revenue_contribution`
- `op_estimate_vs_consensus`
- `relative_strength_on_evidence_day`
- `backlog_duration_quality`
- `pricing_power_index_or_ASP`
- `target_price_revision_with_estimate_raise`
- `export_contract_repeatability`
- `stage3_plus_4b_overlay_handling`

내릴 축:

- `order_value_only`
- `preferred_bidder_only`
- `mou_or_partnership_only`
- `target_price_raise_without_price_strength`
- `event_pop_without_margin_visibility`
- `sector_hype_without_company_estimate`

## 테스트

실행:

```bash
PYTHONPATH=src python -m unittest tests.test_round296_r1_loop15_industrial_trigger_validation -v
```

결과:

```text
Ran 6 tests in 0.005s
OK
```

## 주의

- 이 라운드는 calibration/report material이다.
- production scoring은 변경하지 않았다.
- Stage3-Green threshold를 낮추지 않았다.
- case와 trigger record는 candidate-generation input으로 쓰면 안 된다.
- preferred bidder, MOU, order value only는 Green 금지다.
