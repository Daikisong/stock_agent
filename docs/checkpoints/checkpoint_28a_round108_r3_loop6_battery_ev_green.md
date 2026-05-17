# Checkpoint 28A Round 108 R3 Loop 6 Battery / EV / Green Energy

## 요약

Round 108은 R3 `2차전지·전기차·친환경`을 EV 성장 narrative가 아니라 실제 EPS/FCF 체급 변화 경로로 다시 나눈 calibration pack이다.

쉬운 예:

- EV 배터리 공장 CAPA가 늘어도 공장이 멈추면 `4C`에 가깝다.
- ESS 계약은 좋아도 고객명, 계약금액, GWh, 마진, 가동률이 없으면 Stage 3-Green을 만들 수 없다.
- SK On-Ford JV 해체는 ESS pivot option이지만, EV 수요둔화와 영업손실도 같이 보이는 Watch 사례다.
- 흑연 공급망 안보는 중요하지만, 미국 생산비·정책금융·offtake가 없으면 Green 근거가 아니다.

## 반영 내용

- R3 Loop 6 전용 pack 추가
- 신규 archetype 추가:
  - `EV_BATTERY_JV_RESTRUCTURING`
  - `SECOND_LIFE_BATTERY_GRID_STORAGE`
  - `BATTERY_GRAPHITE_SUPPLYCHAIN_SECURITY`
  - `SODIUM_ION_SUBSTITUTION_OVERLAY`
  - `SOLID_STATE_COMMERCIALIZATION_LICENSE`
  - `BESS_SAFETY_PERMITTING`
- `ESS_TESLA_MEGAPACK_SUPPLY_CHAIN` visibility 상향
- `BATTERY_MATERIALS_CAPEX_OVERHEAT`, `BATTERY_EQUIPMENT_PARTS`는 EV 둔화·CAPA·계약취소 감점 강화
- price-field plan에 JV restructuring, graphite, second-life, solid-state, sodium-ion, BESS permitting 필드 추가
- production scoring/staging/red-team 로직은 변경하지 않음

## 산출물

- `src/e2r/sector/round108_r3_loop6_battery_ev_green.py`
- `src/e2r/cli/build_round108_r3_loop6_report.py`
- `tests/test_round108_r3_loop6_battery_ev_green.py`
- `data/e2r_case_library/cases_r3_loop6_round108.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round108_r3_loop6_v6.csv`
- `output/e2r_round108_r3_loop6_battery_ev_green/`

## 결과 수치

- target_count: 26
- case_candidate_count: 23
- structural_success_count: 1
- success_candidate_count: 10
- cyclical_success_count: 1
- failed_rerating_count: 2
- overheat_count: 1
- stage4b_case_count: 2
- stage4c_case_count: 8
- green_possible_count: 2
- watch_yellow_first_count: 14
- redteam_first_count: 10
- gate_only_target_count: 6

## Guardrail

- 이 pack은 calibration/evaluation 자료이며 candidate-generation input이 아니다.
- v6 weight는 아직 production scoring에 적용하지 않는다.
- EV 성장, ESS, 폐배터리, 흑연, 수소, 태양광, 풍력, 리튬 label만으로 Green을 만들지 않는다.
- 계약금액, 고객명, 기간, GWh, 마진, 가동률, 회수량, SOH, graphite cost, offtake, royalty, stage price, FCF를 invent하지 않는다.
- EV 계약취소, JV 해체, 공장 idle, sodium-ion 대체, BESS 화재, SOH 불투명성은 RedTeam으로 남긴다.

## 검증

실행:

```bash
PYTHONPATH=src python -m unittest tests.test_round108_r3_loop6_battery_ev_green -v
PYTHONPATH=src python -m e2r.cli.build_round108_r3_loop6_report
```

결과:

- Round 108 단위 테스트 통과
- Round 108 JSONL/CSV/Markdown 보고서 생성 완료
