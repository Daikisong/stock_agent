# Checkpoint 28A Round 246 R3 Loop 11 Battery EV Green Price Validation

## 반영 범위

`docs/round/round_246.md`의 R3 Loop 11 가격검증 내용을 calibration-only 데이터로 반영했다.

생산 점수, 후보 생성, StageClassifier threshold는 바꾸지 않았다.

## 추가 파일

- `src/e2r/sector/round246_r3_loop11_battery_ev_green_price_validation.py`
- `src/e2r/cli/build_round246_r3_loop11_report.py`
- `tests/test_round246_r3_loop11_battery_ev_green_price_validation.py`
- `data/e2r_case_library/cases_r3_loop11_round246.jsonl`
- `data/sector_taxonomy/round246_r3_loop11_battery_ev_green_price_validation_audit.json`
- `output/e2r_round246_r3_loop11_battery_ev_green_price_validation/`

## Archetype 반영

신규 또는 명시 보강한 canonical archetype:

- `US_BATTERY_LOCALIZATION`
- `EV_BATTERY_CONTRACT_QUALITY_BREAK`
- `BATTERY_SUPPLY_CHAIN_DEMAND_SHOCK`
- `LITHIUM_RESOURCE_SECURITY`
- `LITHIUM_OFFTAKE_DLE_OPTIONALITY`
- `EV_FACTORY_EXECUTION_LABOR_IMMIGRATION_RISK`

기존 R3 archetype도 Round 246 기준으로 정의를 보강했다:

- `ESS_LFP_GRID_STORAGE`
- `EV_TO_ESS_CAPACITY_REDEPLOYMENT`
- `SOLAR_US_SUPPLY_CHAIN_LOCALIZATION`
- `SOLAR_CUSTOMS_UFLPA_4C_WATCH`

쉬운 예시:

- 삼성SDI LFP ESS 계약은 좋은 `Stage 2` 단서다.
- 하지만 실제 납품, 가동률, OPM, FCF가 확인되기 전에는 `Stage 3-Green`이 아니다.
- LGES Ford/Freudenberg 계약취소는 계약 헤드라인이 실제 매출이 아닐 수 있음을 보여주는 `hard 4C` 사례다.

## 케이스 요약

- 케이스 수: 8
- `success_candidate`: 5
- `failed_rerating`: 2
- `hard 4C`: 1
- Stage 3 dated case: 0
- 4B-watch: 5
- 4C-watch/hard 4C: 4

주요 케이스:

- Samsung SDI America LFP ESS: `Stage 2`, +6.1% Reuters event anchor, 고객/납품/가동률/마진 확인 전 Green 금지.
- LGES / Tesla-source LFP ESS: `Stage 2`, 고객 비공식 source와 납품 전 상태 때문에 Green 금지.
- SK On / Flatiron: `Stage 2`, 7.2GWh와 2026~2030 공급기간은 강하지만 계약금액과 마진 확인 필요.
- LGES Ford/Freudenberg cancellations: `hard 4C`, 13.5조 원 기대매출 손실과 -7.6% 이벤트 anchor.
- POSCO / MinRes lithium JV: resource security `Stage 2`, lithium cycle과 downstream margin 확인 필요.
- Hanwha Qcells customs disruption: solar localization `Stage 2` plus 4C-watch.
- Ford EV retreat basket: battery supply-chain demand shock 4C-watch.
- Hyundai-LG Georgia raid: factory execution/labor/visa 4C-watch. 정확한 일자를 만들지 않고 `stage4c_month=2025-09` 메타데이터로 보존했다.

## Green Gate

Round 246 R3 Stage 3-Green 필수 조건:

- binding contract
- customer/GWh/supply period 확인
- actual delivery 또는 revenue recognition 시작
- utilization improvement
- OPM 또는 gross margin 확인
- FCF after capex
- subsidy 제외 이익 품질
- customer EV strategy 또는 ESS demand risk 통과
- supply-chain/customs/labor execution risk 통과
- price path follows evidence

금지 패턴:

- EV capacity announcement only
- ESS/LFP theme only
- customer name only
- unofficial customer source only
- factory construction only
- lithium resource headline only
- solar localization headline only
- subsidy 제외 적자
- contract value without utilization

## 산출물

- `round246_r3_loop11_price_validation_summary.md`
- `round246_r3_loop11_case_matrix.csv`
- `round246_r3_loop11_target_aliases.csv`
- `round246_r3_loop11_score_adjustments.csv`
- `round246_r3_loop11_shadow_weights.csv`
- `round246_r3_loop11_deep_sub_archetypes.csv`
- `round246_r3_loop11_price_validation_fields.csv`
- `round246_r3_loop11_green_gate_review.md`
- `round246_r3_loop11_price_validation_plan.md`
- `round246_r3_loop11_stage4b_4c_review.md`

## 검증

실행한 명령:

```bash
PYTHONPATH=src python -m py_compile src/e2r/sector/archetypes.py src/e2r/sector/round246_r3_loop11_battery_ev_green_price_validation.py src/e2r/cli/build_round246_r3_loop11_report.py tests/test_round246_r3_loop11_battery_ev_green_price_validation.py
PYTHONPATH=src python -m unittest tests.test_round246_r3_loop11_battery_ev_green_price_validation -v
PYTHONPATH=src python -m e2r.cli.build_round246_r3_loop11_report
PYTHONPATH=src python -m compileall -q src tests
PYTHONPATH=src python -m unittest discover -s tests -v
git diff --check
```

결과:

- Round 246 신규 테스트 8개 통과.
- 전체 테스트 2963개 통과.
- 리포트 생성 CLI 통과.
- `git diff --check` 통과.

## 다음 단계

이 라운드는 shadow weight와 case-library 보강이다. 다음 scoring 구현 단계에서는 이 케이스를 직접 후보 생성 입력으로 쓰면 안 된다. 대신 `ESS 계약 → 납품/가동률/마진/FCF 확인`, `현지화 → customs/labor execution 확인`처럼 증거 축을 feature로 일반화해야 한다.
