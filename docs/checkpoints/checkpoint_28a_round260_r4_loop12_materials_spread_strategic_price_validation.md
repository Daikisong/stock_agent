# Checkpoint 28A Round 260 R4 Loop 12 Materials Spread Strategic Resources Price Validation

## 반영 내용

- `docs/round/round_260.md`의 R4 Loop 12 내용을 calibration-only 팩으로 구조화했다.
- 대상 대섹터는 `MATERIALS_SPREAD_STRATEGIC`이고, `round_id=round_188`로 기록했다.
- Poongsan M&A rumor, Korea Zinc 전략광물 smelter, 중국 희토류 end-use 압박, 철강 관세 양면성, Hyundai Steel 미국 CAPEX false positive, 석유화학 credit break, Lotte/HD Hyundai 구조조정 relief, critical-minerals policy relief를 8개 케이스로 추가했다.
- `full_adjusted_ohlc_complete=false`인 항목은 stage 가격과 MFE/MAE를 만들지 않고 `price_data_unavailable_after_deep_search` 또는 reported-event anchor로 표시했다.
- production scoring, candidate generation, StageClassifier threshold는 변경하지 않았다.

## 추가 파일

- `src/e2r/sector/round260_r4_loop12_materials_spread_strategic_price_validation.py`
- `src/e2r/cli/build_round260_r4_loop12_report.py`
- `tests/test_round260_r4_loop12_materials_spread_strategic_price_validation.py`
- `data/e2r_case_library/cases_r4_loop12_round260.jsonl`
- `data/sector_taxonomy/round260_r4_loop12_materials_spread_strategic_price_validation_audit.json`
- `output/e2r_round260_r4_loop12_materials_spread_strategic_price_validation/`

## Canonical Archetype 보강

새 라운드에서 요구한 canonical archetype을 추가했다.

- `DEFENSE_METALS_AMMUNITION_OPTIONALITY`
- `CRITICAL_MINERALS_RECYCLING_SMELTER`
- `RARE_EARTH_EXPORT_CONTROL_SUPPLY_CHAIN_4C`
- `STEEL_TARIFF_TWO_SIDED_RELIEF_RISK`
- `CRITICAL_MINERALS_POLICY_RELIEF`

기존 archetype 중 아래도 라운드260 target으로 재사용했다.

- `POLICY_CAPEX_FALSE_POSITIVE`
- `PETROCHEMICAL_CAPACITY_RESTRUCTURING`
- `STANDALONE_NCC_CREDIT_BREAK`

## 케이스 요약

- cases: 8
- success_candidate: 2
- event_premium: 2
- failed_rerating: 2
- watch_cases: 2
- Stage 3 dated cases: 0
- hard 4C confirmed: 0
- price_validation_completed: `partial_with_reported_price_anchors`
- full_ohlc_complete: false

## 핵심 보정

올릴 shadow 축:

- `product_spread`
- `cost_curve_advantage`
- `offtake_quality`
- `supply_discipline`
- `capacity_shutdown_confirmed`
- `working_capital_control`
- `FCF_after_restructuring`
- `critical_minerals_supply_security`
- `governance_and_dilution_control`
- `export_control_resilience`

내릴 shadow 축:

- `M&A_rumor_only`
- `policy_relief_only`
- `strategic_material_headline_only`
- `US_CAPEX_without_ROI`
- `capacity_shutdown_without_spread_recovery`
- `restructuring_plan_undisclosed`
- `China_customer_or_material_concentration`
- `rare_earth_end_use_restriction`
- `tariff_export_risk`
- `dilution_for_project_capex`

쉬운 예시:

- Poongsan은 방산·구리 optionality가 있지만, 인수 rumor만으로는 매출이나 FCF가 바뀐 것이 아니다.
- 철강 anti-dumping relief는 국내 spread에는 좋을 수 있지만, 미국 50% tariff가 export margin을 때리면 같은 기업에도 반대 방향으로 작용한다.
- 석유화학 capacity shutdown은 위기 완화일 수 있지만, 제품 spread와 FCF가 회복되기 전에는 구조적 Green이 아니다.

## Green Gate

R4 Stage 3-Green은 아래가 확인되기 전에는 열지 않는다.

- 제품 spread 개선
- cost curve advantage
- offtake / price floor / take-or-pay
- supply discipline 또는 실제 capacity shutdown
- restructuring 이후 OPM / FCF 개선
- working capital 안정
- 중국 희토류 end-use / 관세 / 제재 리스크 통과
- 희석 / 지배구조 리스크 통과
- evidence 이후 가격경로 확인

금지 패턴:

- M&A rumor only
- 정책지원 only
- 전략자원 headline only
- 미국 CAPEX only
- 구조조정 계획 undisclosed
- capacity shutdown만 있고 spread 회복 없음
- 희토류·중국 end-use restriction 존재

## 검증

- `PYTHONPATH=src python -m unittest tests.test_round260_r4_loop12_materials_spread_strategic_price_validation -v`
- `PYTHONPATH=src python -m e2r.cli.build_round260_r4_loop12_report`

## 결론

라운드260은 R4에서 “전략자원·희토류·관세·구조조정·미국 CAPEX”라는 단어를 Green 근거로 쓰지 않도록 막는 가격경로 검증팩이다. 실제 Stage 3 근거는 제품 spread, offtake, 원가곡선, working capital, FCF, 그리고 중국 end-use restriction·관세·희석·신용위험 통과로 닫혀야 한다.
