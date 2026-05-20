# Checkpoint 28A Round 286 R4 Loop 14 Materials Spreads Strategic Resources Price Validation

`docs/round/round_286.md`의 R4 Loop 14 내용을 케이스 라이브러리용 구조화 자료로 반영했다. 이번 라운드는 석유화학, 철강, 전략금속, 리튬, 희토류, 양극재 공급망에서 headline/event price move와 실제 EPS/FCF 전환을 분리하는 검증팩이다.

## 반영 범위

- 신규 R4 Loop 14 canonical archetype 8개 추가:
  - `PETROCHEMICAL_SPREAD_COLLAPSE_4C`
  - `PETROCHEMICAL_RESTRUCTURING_STAGE2_NOT_GREEN`
  - `STEEL_ANTI_DUMPING_EVENT_PREMIUM`
  - `STRATEGIC_METAL_CONTROL_PREMIUM_4B`
  - `LITHIUM_RESOURCE_INTEGRATION_STAGE2`
  - `LITHIUM_PRICE_SQUEEZE_EVENT_PREMIUM`
  - `BATTERY_MATERIAL_CONTRACT_COLLAPSE_HARD_4C`
  - `CATHODE_SUPPLY_CHAIN_REBALANCING_STAGE2`
- 기존 `RARE_EARTH_EXPORT_CONTROL_SUPPLY_CHAIN_4C`를 Loop 14 희토류 수출통제 검증 target으로 재사용.
- 생산 scoring, staging, candidate generation 변경 없음.
- Round 286 케이스는 calibration/evaluation material 전용이다.

## 산출물

- `src/e2r/sector/round286_r4_loop14_materials_spreads_strategic_resources_price_validation.py`
- `src/e2r/cli/build_round286_r4_loop14_report.py`
- `tests/test_round286_r4_loop14_materials_spreads_strategic_resources_price_validation.py`
- `data/e2r_case_library/cases_r4_loop14_round286.jsonl`
- `data/sector_taxonomy/round286_r4_loop14_materials_spreads_strategic_resources_price_validation_audit.json`
- `output/e2r_round286_r4_loop14_materials_spreads_strategic_resources_price_validation/`

## 케이스 요약

- total cases: 9
- success_candidate: 3
- event_premium: 2
- failed_rerating: 1
- hard 4C: 1
- hard 4C watch: 3
- Stage 3 dated candidates: 0
- Stage 4B watch: 5
- Stage 4C watch: 4

## 핵심 가드레일

- 석유화학 구조조정은 정책 지원만으로 Green이 아니다. 실제 shutdown, spread 회복, cash margin 회복이 필요하다.
- 철강 반덤핑은 event premium일 수 있지만, 물리적 수요와 steel spread가 없으면 Stage 3-Green 근거가 아니다.
- Korea Zinc 같은 지배권 프리미엄은 4B-watch이며, smelter margin, governance, dilution control 없이는 operating Green이 아니다.
- 리튬 광산 지분은 Stage 2 후보지만, offtake와 processing utilization, 고객 call-off가 있어야 구조적 증거가 된다.
- CATL Yichun 같은 리튬 squeeze headline은 ASP, inventory, margin 확인 전에는 event premium이다.
- L&F/Tesla 4680 계약 축소는 고객명 계약이 실제 call-off와 계약가치로 닫히지 않을 때 hard 4C가 될 수 있음을 보여준다.
- 희토류 수출통제는 수혜주 evidence가 아니라 RedTeam supply-chain overlay다.

쉬운 예시: `리튬 가격 반등` 뉴스만으로 양극재 기업을 Green으로 올리면 안 된다. 가격 반등이 실제 판가, 재고평가손익, 고객 발주, 마진으로 이어지는지 확인해야 한다.

## 검증

- `PYTHONPATH=src python -m py_compile src/e2r/sector/archetypes.py src/e2r/sector/round286_r4_loop14_materials_spreads_strategic_resources_price_validation.py src/e2r/cli/build_round286_r4_loop14_report.py tests/test_round286_r4_loop14_materials_spreads_strategic_resources_price_validation.py`
- `PYTHONPATH=src python -m unittest tests.test_round286_r4_loop14_materials_spreads_strategic_resources_price_validation -v`
- `PYTHONPATH=src python -m e2r.cli.build_round286_r4_loop14_report`

## 다음 작업

Round 286은 가격검증 anchor가 `partial_with_reported_price_anchors` 상태다. 다음 R4 확장에서는 full adjusted OHLC, stage-date price, MFE/MAE, spread/commodity data를 backfill해 event premium과 true rerating을 더 엄격히 분리해야 한다.
