# Checkpoint 28A Round 306 R11 Loop 15 Policy / Geopolitics / Disaster Trigger Validation

## 반영 내용

- `docs/round/round_306.md`의 R11 Loop 15 분석을 calibration-only 데이터팩으로 반영했다.
- 생산 scoring, staging, candidate generation은 바꾸지 않았다.
- full adjusted OHLC가 없으므로 MFE/MAE를 만들지 않고, 보도된 event return, market-relative return, 계약금액, 정책물량, 피해규모를 trigger anchor로만 저장했다.

쉬운 예시:

- `Hyundai Rotem / Poland K2`는 단순 방산 뉴스가 아니라 18대 납품, 매출 기여, OP 추정치 상향, +9.3% 가격반응이 이어져 Stage2-Actionable이다.
- `Hormuz energy shock`는 대체 원유/나프타 루트가 생겨도 성장 증거가 아니라 충격 완화다. 그래서 Stage3-Green 증거가 아니라 4C + relief로 둔다.

## 추가된 canonical archetype

- `DEFENSE_EXPORT_BACKLOG_STAGE2_ACTIONABLE`
- `GROUND_WEAPON_EXPORT_DELIVERY_STAGE2_YELLOW`
- `CHIP_EXPORT_CONTROL_4C_WATCH`
- `SEMICONDUCTOR_LABOR_STRIKE_4C_WATCH`
- `POLITICAL_SYSTEM_SHOCK_MARKET_4C`
- `HORMUZ_ENERGY_SECURITY_4C_WITH_POLICY_RELIEF`
- `NAVAL_SHIPBUILDING_GEOPOLITICAL_STAGE2_WITH_DILUTION_4B`
- `NATURAL_DISASTER_RECOVERY_STAGE2_REFERENCE`

## 산출물

- `data/e2r_case_library/cases_r11_loop15_round234.jsonl`
- `data/e2r_trigger_calibration/triggers_r11_loop15_round234.jsonl`
- `data/sector_taxonomy/round306_r11_loop15_policy_geopolitical_event_trigger_validation_audit.json`
- `data/sector_taxonomy/score_weight_profiles_round234_r11_loop15_v1.csv`
- `output/e2r_round306_r11_loop15_policy_geopolitical_event_trigger_validation/`

## 요약 지표

- case candidates: 8
- trigger rows: 10
- target archetypes: 8
- Stage2-Actionable candidates: 3
- Stage3-Yellow candidates: 3
- Stage3-Green confirmed: 0
- Stage2 relief rows: 1
- Stage4B watch rows: 2
- Stage4C watch rows: 4
- hard 4C cases: 3
- disaster reference rows: 1

## 핵심 보정

올릴 축:

- `signed_defense_contract_value`
- `delivery_to_revenue_conversion`
- `defense_backlog_growth`
- `local_production_technology_transfer_terms`
- `trade_policy_license_risk`
- `labor_disruption_output_risk`
- `political_system_stability`
- `energy_chokepoint_exposure`
- `alternative_supply_route_relief`
- `disaster_direct_cost_and_recovery`

내릴 축:

- `geopolitical_theme_only`
- `preferred_supplier_without_signed_contract`
- `defense_order_without_delivery_margin`
- `policy_relief_without_earnings`
- `energy_supply_relief_as_growth`
- `political_false_break_as_structural`
- `technology_transfer_headline_only`

## Stage 판단

- Hanwha Aerospace / Romania K9: Stage2-Actionable. Green은 delivery, margin, cash collection, dilution absorption 확인 전까지 보류.
- Hyundai Rotem / Poland K2: Stage2-Actionable 및 Stage3-Yellow 후보. Green은 multi-quarter delivery, margin, local production execution 확인 전까지 보류.
- Samsung/SK Hynix export curbs: 4C-watch. China fab upgrade ceiling은 성장 증거가 아니라 RedTeam overlay.
- Samsung labor strike: 4C-watch. 노동 이슈가 DRAM/NAND 공급, 고객 납기, 국가 수출에 영향을 줄 수 있기 때문.
- Martial-law crisis: hard political 4C. 빠른 reversal은 false-break relief이지 구조적 개선이 아니다.
- Hormuz energy shock: hard geopolitical 4C + Stage2 relief. 대체 루트는 downside containment이지 growth trigger가 아니다.
- Hanwha Ocean U.S. naval shipbuilding: Stage2 optionality + 4B overlay. formal contract, tech transfer, shipyard economics 확인 전까지 Green 금지.
- 2025 wildfires: disaster reference. 직접 KRX equity trigger가 없어 Stage3 판단에 쓰지 않는다.

## 바꾸지 않은 것

- 생산 scoring 변경 없음.
- candidate generation input 아님.
- benchmark/case label을 scoring input으로 쓰지 않음.
- full adjusted OHLC 없이 MFE/MAE를 만들지 않음.
- 정책/지정학/재난 headline만으로 Stage3-Green을 만들지 않음.

## 검증

- `PYTHONPATH=src python -m unittest tests.test_round306_r11_loop15_policy_geopolitical_event_trigger_validation -v`
- 전체 테스트는 커밋 전 실행 대상.
