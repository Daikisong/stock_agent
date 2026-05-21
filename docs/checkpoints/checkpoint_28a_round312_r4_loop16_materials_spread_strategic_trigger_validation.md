# Checkpoint 28A Round 312 R4 Loop 16 소재·스프레드·전략자원 Trigger Validation

## 목적

`docs/round/round_312.md`의 R4 Loop 16 내용을 calibration/evaluation 자료로 반영했다. 이번 라운드는 소재 섹터를 하나로 보지 않고, 원자재 가격, 회사 spread, 전략자원 capex, offtake, 구조조정 실행, 희석/지배구조, TC/RC 압박을 trigger 단위로 분리한다.

쉬운 예시:

- 구리 가격이 올라도 제련소가 받는 TC/RC가 무너지면 제련 마진은 나빠질 수 있다.
- 철강 반덤핑은 국내 ASP/spread relief가 될 수 있지만, 미국 수출 관세는 export spread 4C-watch가 될 수 있다.
- 리튬 광산 중단으로 소재주가 급등해도 cathode ASP, 재고평가손 환입, 마진 회복이 없으면 Green이 아니다.

## 반영 파일

- `src/e2r/sector/round312_r4_loop16_materials_spread_strategic_trigger_validation.py`
- `src/e2r/cli/build_round312_r4_loop16_report.py`
- `tests/test_round312_r4_loop16_materials_spread_strategic_trigger_validation.py`
- `data/e2r_case_library/cases_r4_loop16_round240.jsonl`
- `data/e2r_trigger_calibration/triggers_r4_loop16_round240.jsonl`
- `data/sector_taxonomy/round312_r4_loop16_materials_spread_strategic_trigger_validation_audit.json`
- `data/sector_taxonomy/score_weight_profiles_round240_r4_loop16_v1.csv`
- `output/e2r_round312_r4_loop16_materials_spread_strategic_trigger_validation/`

## Canonical Archetype 추가

- `STEEL_TARIFF_4C_AND_ANTIDUMPING_RELIEF`
- `STEEL_US_LOCALIZATION_CAPEX_4B`
- `PETROCHEMICAL_OVER_SUPPLY_FAILED_RERATING`
- `PETROCHEMICAL_CAPACITY_RESTRUCTURING_STAGE2_RELIEF`
- `CRITICAL_MINERALS_REFINERY_STAGE2_WITH_DILUTION_4B`
- `LITHIUM_MINE_JV_STRATEGIC_RESOURCE_STAGE2`
- `LITHIUM_PRICE_BETA_CYCLICAL_STAGE2`
- `COPPER_TC_RC_SPREAD_4C_WATCH`
- `SODIUM_ION_MATERIAL_OPTIONALITY_STAGE2`

## 케이스 요약

| case | 판정 |
| --- | --- |
| Hyundai Steel / POSCO tariff vs anti-dumping | U.S. tariff는 4C-watch, Korea anti-dumping은 Stage2 relief |
| Hyundai Steel Louisiana capex | 현지화 capex + intraday reversal. ROI 확인 전 4B |
| LG Chem / Lotte Chemical oversupply | 석유화학 oversupply와 영업손실. failed rerating / 4C-watch |
| Lotte / HD Hyundai petrochemical restructuring | capacity cut 계획은 Stage2 relief. 실제 shutdown과 spread 회복 전 Green 금지 |
| Korea Zinc Tennessee refinery | 전략광물 Stage2 + 신주발행/지배구조 4B |
| POSCO / MinRes lithium JV | 전략자원 Stage2. POSCO 가격 anchor와 offtake margin 미확인 |
| CATL Yichun lithium beta | cyclical Stage2 / event premium. 소재 margin 확인 전 Green 금지 |
| Copper TC/RC compression | copper bull과 smelter margin을 분리해야 하는 4C-watch |
| LG Chem / Sinopec sodium-ion | 차세대 소재 optionality. 고객계약/상업화 전 Stage2 |

## Trigger 결과

- case_candidate_count: `9`
- trigger_count: `11`
- target_archetype_count: `9`
- stage2_actionable_candidate_count: `2`
- stage2_event_candidate_count: `5`
- stage3_yellow_candidate_count: `0`
- stage3_green_confirmed_count: `0`
- stage4b_watch_count: `5`
- stage4c_watch_count: `4`
- hard_4c_case_count: `0`

## 핵심 보정 방향

올릴 축:

- `domestic_spread_recovery`
- `tariff_exposure_absorption`
- `actual_capacity_cut`
- `naphtha_spread_recovery`
- `strategic_resource_offtake`
- `dilution_governance_overlay`
- `lithium_price_duration`
- `smelter_TC_RC_margin`
- `commercialization_contract`

내릴 축:

- `commodity_price_headline_without_margin`
- `tariff_policy_without_spread_proof`
- `strategic_resource_capex_without_offtake`
- `restructuring_plan_without_shutdown`
- `petrochemical_recovery_without_capacity_cut`
- `lithium_JV_without_price_anchor`
- `copper_bull_without_TCRC`

## Guardrail

- production scoring 변경 없음
- candidate generation input 아님
- shadow weight only
- full adjusted OHLC 미확보
- OHLC 미확보만으로 Stage2/Yellow 후보를 강등하지 않음
- 원자재 가격, 전략자원 capex, 구조조정 계획만으로 Stage3-Green 금지
- spread, margin, offtake, capacity cut, dilution/governance gate를 분리 기록

## 검증

실행한 핵심 명령:

```bash
PYTHONPATH=src python -m unittest tests/test_round312_r4_loop16_materials_spread_strategic_trigger_validation.py -v
PYTHONPATH=src python -m e2r.cli.build_round312_r4_loop16_report
```

전용 테스트와 리포트 생성은 통과했다. 전체 테스트는 최종 커밋 전 다시 실행한다.
