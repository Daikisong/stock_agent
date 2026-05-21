# Checkpoint 28A Round 317 R9 Loop 16 Trigger-level Calibration

## 반영 내용

- `docs/round/round_317.md`의 R9 Loop 16 모빌리티·운송·레저 trigger-level validation을 구조화했다.
- Hyundai hybrid/value-up, Hyundai/Kia tariff and localization, Hyundai/Boston Dynamics robotics, Hyundai/Glovis logistics disruption, Korean Air/Asiana consolidation, Jeju Air crash, China tourism/leisure, HMM/Red Sea freight beta를 calibration case로 추가했다.
- full adjusted OHLC window는 확보하지 못한 라운드이므로, reported event return과 event anchor를 별도 trigger row로 저장했다.
- 생산 scoring, staging, candidate generation은 변경하지 않았다.

## 추가한 canonical archetype

- `AUTO_HYBRID_VALUEUP_STAGE2_ACTIONABLE`
- `AUTO_TARIFF_4C_AND_LOCALIZATION_HEDGE`
- `AUTO_ROBOTICS_OPTIONALITY_STAGE2_WITH_LABOR_4B`
- `AUTO_EXPORT_LOGISTICS_DISRUPTION_4C_WATCH`
- `AIRLINE_CONSOLIDATION_STAGE2_WITH_INTEGRATION_4B`
- `CHINA_TOURISM_LEISURE_STAGE2_EVENT`
- `CONTAINER_SHIPPING_FREIGHT_BETA_STAGE2_WITH_NORMALIZATION_4B`

기존 `AVIATION_SAFETY_HARD_4C`는 라운드 317의 Jeju Air hard 4C 케이스에 재사용했다.

## 핵심 보정

- Hybrid/EREV narrative는 실제 OP margin과 FCF로 닫히기 전에는 Green이 아니다.
- U.S. tariff relief headline은 실제 tariff savings가 없으면 4C-watch가 유지된다.
- U.S. localization capex는 utilization과 ROI가 보여야 Yellow/Green 후보가 된다.
- Robotics optionality는 unit economics, plant productivity, labor agreement가 필요하다.
- Airline consolidation은 route yield, cost synergy, mileage/fare/labor integration이 필요하다.
- Fatal aviation accident는 hard 4C다.
- Tourism policy는 arrivals보다 spending, RevPAR, casino drop, duty-free margin, airline yield가 중요하다.
- Freight-rate spike는 contract duration과 route normalization risk를 분리해야 한다.

쉬운 예시:
`as_of_date=2025-08-06`에 중국 단체관광 비자면제 뉴스가 나오고 Hotel Shilla가 올랐더라도, 그날 바로 Green이 아니다. 실제 중국 관광객의 객단가, 호텔 RevPAR, 카지노 drop, 면세점 margin이 나중에 확인되어야 Stage 3 후보로 올라갈 수 있다.

## 생성 파일

- `src/e2r/sector/round317_r9_loop16_mobility_transport_leisure_trigger_validation.py`
- `src/e2r/cli/build_round317_r9_loop16_report.py`
- `tests/test_round317_r9_loop16_mobility_transport_leisure_trigger_validation.py`
- `data/e2r_case_library/cases_r9_loop16_round245.jsonl`
- `data/e2r_trigger_calibration/triggers_r9_loop16_round245.jsonl`
- `data/sector_taxonomy/round317_r9_loop16_mobility_transport_leisure_trigger_validation_audit.json`
- `data/sector_taxonomy/score_weight_profiles_round245_r9_loop16_v1.csv`
- `output/e2r_round317_r9_loop16_mobility_transport_leisure_trigger_validation/`

## 안전장치

- `production_scoring_changed = false`
- `candidate_generation_input = false`
- `shadow_weight_only = true`
- `stage3_green_confirmed_count = 0`
- `full_adjusted_ohlc_complete = false`
- Case library는 calibration/evaluation material이며 production candidate-generation input이 아니다.

## 다음 단계

- R10 Loop 16에서 건설·부동산·건자재 라운드를 같은 방식으로 반영한다.
- 라운드 317의 reported event anchor는 나중에 adjusted OHLC backfill row와 분리해 MFE/MAE를 채워야 한다.
