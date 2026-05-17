# Checkpoint 28A Round55 R2 Loop-2 AI / Semiconductor / Electronics

## Scope

Round55 반영 범위는 `docs/round/round_55.md`의 R2 Loop 2 보강이다.

핵심 변경은 AI 수혜주를 하나의 바구니로 보지 않고, 경제 구조별로 분리한 것이다.

예:

- `HBM`은 CAPA 병목, 고객 공급확보, 다년 EPS 상향이 같이 있으면 Green 후보가 될 수 있다.
- `범용 DRAM/NAND 반등`은 EPS 회복은 가능하지만 HBM보다 visibility가 약하므로 Watch/Yellow 우선이다.
- `AI 서버 ODM/EMS`는 매출 성장이 커도 저마진, 재고, 고객집중, 회계 신뢰 이슈가 있으면 Green을 막는다.
- `네오클라우드 GPU 렌탈`은 대형 계약이 있어도 부채, FCF 적자, GPU 감가, 고객집중이 풀리기 전에는 Green이 아니다.
- `감사인 사임/공시 지연/내부통제 이슈`는 AI 성장보다 먼저 보는 hard RedTeam gate다.

## Added

- `src/e2r/sector/round55_r2_loop2_ai_semiconductor.py`
- `src/e2r/cli/build_round55_r2_loop2_report.py`
- `tests/test_round55_r2_loop2_ai_semiconductor.py`

## Archetype Updates

Round55에서 명시적으로 다루는 R2 Loop-2 target은 18개다.

- `MEMORY_HBM_CAPACITY`
- `COMMODITY_MEMORY_GENERAL_SEMI`
- `SEMI_EQUIPMENT_CAPEX`
- `SEMI_MATERIALS_PROCESS`
- `ADVANCED_PACKAGING_PCB`
- `ADVANCED_PACKAGING_COWOS_EMIB`
- `DISPLAY_OLED_SUPPLYCHAIN`
- `ELECTRONIC_COMPONENTS_MLCC_SENSOR`
- `AI_CHIP_FABRIC_INFRA`
- `AI_ACCELERATOR_CHIP_PUREPLAY`
- `AI_SERVER_ODM_EMS_SUPPLY_CHAIN`
- `NEOCLOUD_GPU_RENTAL`
- `OPTICAL_NETWORKING_AI_DATACENTER`
- `INDUSTRIAL_GASES_SEMICONDUCTOR_INFRA`
- `AI_DATA_CENTER_COOLING`
- `DATA_CENTER_REIT_INFRASTRUCTURE`
- `AI_GRID_FLEXIBILITY_SOFTWARE`
- `REDTEAM_ACCOUNTING_TRUST_OVERLAY`

## Case Pack

Generated calibration cases:

- `data/e2r_case_library/cases_r2_loop2_round55.jsonl`

Case count:

- total: 12
- structural_success: 1
- success_candidate: 5
- cyclical_success: 1
- overheat: 1
- failed_rerating: 2
- 4B-watch marker cases: 2
- 4C thesis-break cases: 1

Important cases:

- `sk_hynix_hbm_rerating_success_case`
- `applied_materials_ai_packaging_growth_case`
- `nvidia_cowos_l_transition_case`
- `broadcom_optical_pcb_leadtime_case`
- `foxconn_ai_server_rack_growth_case`
- `ecolab_coolit_liquid_cooling_case`
- `coreweave_openai_contract_ipo_case`
- `coreweave_downsized_ipo_debt_case`
- `supermicro_ey_resignation_case`
- `samsung_ai_boom_labor_execution_case`
- `commodity_memory_price_rebound_case`
- `cxl_glass_substrate_theme_case`

## Outputs

Generated files:

- `data/sector_taxonomy/score_weight_profiles_round55_r2_loop2_v2.csv`
- `output/e2r_round55_r2_loop2_ai_semiconductor/round55_r2_loop2_ai_semiconductor_summary.md`
- `output/e2r_round55_r2_loop2_ai_semiconductor/round55_r2_loop2_case_matrix.csv`
- `output/e2r_round55_r2_loop2_ai_semiconductor/round55_r2_loop2_stage_date_plan.csv`
- `output/e2r_round55_r2_loop2_ai_semiconductor/round55_r2_loop2_green_guardrails.md`
- `output/e2r_round55_r2_loop2_ai_semiconductor/round55_r2_loop2_risk_overlays.md`
- `output/e2r_round55_r2_loop2_ai_semiconductor/round55_r2_loop2_price_validation_plan.md`
- `output/e2r_round55_r2_loop2_ai_semiconductor/round55_r2_loop2_price_fields.csv`

## Guardrails

- Production scoring was not changed.
- Case records are calibration/evaluation material only.
- Case records are not candidate-generation input.
- Stage 3-Green thresholds were not loosened.
- Missing prices and stage prices remain null until backfilled from official price history.
- No numeric contract amount, margin, price band, prepayment, or FCF field is invented.

Simple example:

`OpenAI contract` can be visibility evidence for a GPU cloud company. It is still not enough for Green if the same record has high debt, negative FCF, GPU depreciation, and one-customer concentration.

## Verification

Commands run:

```bash
PYTHONPATH=src python -m compileall -q src/e2r/sector/round55_r2_loop2_ai_semiconductor.py src/e2r/cli/build_round55_r2_loop2_report.py tests/test_round55_r2_loop2_ai_semiconductor.py
PYTHONPATH=src python -m unittest tests.test_round55_r2_loop2_ai_semiconductor -v
PYTHONPATH=src python -m e2r.cli.build_round55_r2_loop2_report
```

Round55 targeted tests:

- 13 tests passed.

Full repository test result is recorded in the final commit message/report for this round.

Full verification after report generation:

```bash
PYTHONPATH=src python -m compileall -q src tests
PYTHONPATH=src python -m unittest discover -s tests -v
```

Result:

- 850 tests passed.
