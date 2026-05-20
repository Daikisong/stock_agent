# Checkpoint 28A Round 295 R13 Loop 14 Cross-archetype RedTeam Price Validation

## 반영 내용

- `docs/round/round_295.md`를 R13 Loop 14 cross-archetype RedTeam 케이스팩으로 반영했다.
- 신규 canonical archetype 8개를 추가했다.
  - `DEFENSE_BACKLOG_DILUTION_4B`
  - `SIGNED_CONTRACT_COLLAPSE_HARD_4C`
  - `RESOURCE_DISCOVERY_PRICE_MOVED_WITHOUT_EVIDENCE`
  - `AI_CLOUD_IPO_FALSE_POSITIVE`
  - `VALUE_UP_SHAREHOLDER_RETURN_FALSE_POSITIVE`
  - `DATA_TRUST_HARD_4C`
  - `LOCALIZATION_CAPEX_FALSE_POSITIVE`
  - `CONTROL_PREMIUM_4B_GOVERNANCE_WATCH`
- 케이스 8개를 calibration-only case record로 저장했다.
- production scoring, StageClassifier, candidate generation은 변경하지 않았다.
- full adjusted OHLC가 없는 항목은 `reported_event_anchor_not_full_ohlc` 또는 관련 anchor 상태로 남겼다.

## 케이스 요약

| 케이스 | 판정 | 핵심 교훈 |
|---|---|---|
| Hanwha Aerospace | 4B-watch / false positive | 방산 backlog가 좋아도 증자 희석과 공시 품질을 EPS에 반영해야 한다. |
| L&F / Tesla | hard 4C | 고객명과 signed amount는 실제 call-off 매출이 아니다. |
| Korea Gas / Blue Whale | price moved without evidence | 대통령 발표와 자원 estimate는 시추·경제성 전까지 Green 증거가 아니다. |
| LG CNS | evidence good but price failed | AI/cloud 매출 비중과 IPO 청약경쟁률보다 aftermarket price 검증이 우선이다. |
| Samsung C&T | false positive | Value-Up proposal은 board adoption과 실제 주주환원 실행 전까지 Green이 아니다. |
| SK Telecom | hard 4C | 데이터 신뢰 훼손은 매출전망, 보안투자, 보상, 우발부채로 내려오면 thesis break다. |
| Hyundai Steel | false positive | 현지화 CAPEX는 funding clarity, IRR, customer demand 없이 Green이 아니다. |
| Korea Zinc | 4B-watch / event premium | 지배권 premium은 영업현금흐름 rerating과 분리해야 한다. |

쉬운 예시로, `Tesla와 2.9B USD 계약`이라는 headline은 좋아 보이지만 실제 call-off가 거의 0으로 줄면 Stage 3-Green이 아니라 hard 4C다.

## 생성 파일

- `data/e2r_case_library/cases_r13_loop14_round295.jsonl`
- `data/sector_taxonomy/round295_r13_loop14_cross_archetype_redteam_price_validation_audit.json`
- `output/e2r_round295_r13_loop14_cross_archetype_redteam_price_validation/round295_r13_loop14_price_validation_summary.md`
- `output/e2r_round295_r13_loop14_cross_archetype_redteam_price_validation/round295_r13_loop14_case_matrix.csv`
- `output/e2r_round295_r13_loop14_cross_archetype_redteam_price_validation/round295_r13_loop14_shadow_weights.csv`
- `output/e2r_round295_r13_loop14_cross_archetype_redteam_price_validation/round295_r13_loop14_green_gate_review.md`
- `output/e2r_round295_r13_loop14_cross_archetype_redteam_price_validation/round295_r13_loop14_stage4b_4c_review.md`

## Shadow 보정축

올릴 축:

- `actual_calloff_vs_signed_contract`
- `dilution_adjusted_EPS`
- `capital_raise_disclosure_quality`
- `capex_IRR_and_funding_clarity`
- `aftermarket_price_validation`
- `data_trust_internal_control`
- `contingent_liability_risk`
- `governance_execution_not_proposal`
- `control_premium_separation`
- `resource_economic_viability`

내릴 패턴:

- `headline_order_backlog_only`
- `large_customer_name_only`
- `policy_or_presidential_announcement_only`
- `IPO_oversubscription_only`
- `activist_or_valueup_proposal_only`
- `control_premium_as_operating_green`
- `capex_localization_headline_only`
- `resource_estimate_without_drilling`
- `data_breach_treated_as_oneoff`

## 테스트

실행:

```bash
PYTHONPATH=src python -m unittest tests.test_round295_r13_loop14_cross_archetype_redteam_price_validation -v
```

결과:

```text
Ran 6 tests in 0.006s
OK
```

## 주의

- 이 라운드는 case library calibration이다.
- production scoring은 바꾸지 않았다.
- Stage 3-Green threshold를 낮추지 않았다.
- 케이스 레코드는 candidate-generation input으로 쓰면 안 된다.
- full adjusted OHLC가 없는 항목의 MFE/MAE는 만들지 않았다.

