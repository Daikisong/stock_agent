# Checkpoint 28A Round 299 R4 Loop 15 Materials/Spread/Strategic Resources Trigger Validation

## 목적

`docs/round/round_299.md`의 R4 Loop 15 내용을 calibration-only 자료로 반영했다.

이번 라운드의 핵심은 소재/전략자원 headline을 그대로 Stage 3-Green으로 올리지 않고, tariff, spread, TC/RC, funding, control premium, export-control risk를 분리하는 것이다.

쉬운 예:

- 중국 흑연 관세로 POSCO Future M이 급등하면 Stage2-Actionable 후보가 될 수 있다.
- 하지만 비중국 capacity, 품질 인증, 고객 award, anode margin이 없으면 Green은 아니다.
- Korea Zinc가 공개매수/경영권 분쟁으로 급등하면 control premium 4B이지, 아연/동 제련 margin Green이 아니다.

## 반영 파일

- `src/e2r/sector/round299_r4_loop15_materials_spread_strategic_trigger_validation.py`
- `src/e2r/cli/build_round299_r4_loop15_report.py`
- `tests/test_round299_r4_loop15_materials_spread_strategic_trigger_validation.py`
- `data/e2r_case_library/cases_r4_loop15_round227.jsonl`
- `data/e2r_trigger_calibration/triggers_r4_loop15_round227.jsonl`
- `data/sector_taxonomy/round299_r4_loop15_materials_spread_strategic_trigger_validation_audit.json`
- `data/sector_taxonomy/score_weight_profiles_round227_r4_loop15_v1.csv`
- `output/e2r_round299_r4_loop15_materials_spread_strategic_trigger_validation/`

## 추가/확장 archetype

- `GRAPHITE_TARIFF_STAGE2_ACTIONABLE`
- `UPSTREAM_LITHIUM_SUPPLY_SECURITY_STAGE2`
- `STEEL_ANTIDUMPING_SPREAD_STAGE2_ACTIONABLE`
- `STEEL_WEAK_DEMAND_FAILED_RERATING`
- `KOREA_ZINC_CONTROL_PREMIUM_4B`
- `CRITICAL_MINERALS_SMELTER_STAGE2_WITH_DILUTION_4B`
- `COPPER_TCRC_SPREAD_4C_WATCH`
- `CHINA_STRATEGIC_MINERAL_EXPORT_CONTROL_4C`

`LOCALIZATION_CAPEX_FALSE_POSITIVE`는 기존 archetype을 재사용했다.

## 산출 요약

- cases: 10
- triggers: 11
- Stage2-Actionable candidates: 4
- Stage3-Yellow candidates: 3
- Stage3-Green candidates: 0
- Stage3-Green confirmed: 0
- 4B watch cases: 4
- 4C watch cases: 5
- hard 4C cases: 0
- production scoring changed: false
- candidate generation input: false
- full adjusted OHLC complete: false
- shadow weight only: true

## 주요 판정

POSCO Future M graphite tariff는 Stage2-Actionable / Stage3-Yellow 후보로 기록했다. 다만 capacity, quality certification, customer award, anode margin이 닫히지 않아 Green은 아니다.

CATL Yichun lithium mine suspension은 lithium price event premium이다. 리튬 가격 반등과 관련주 반응은 있었지만, durable price와 소재 margin으로 연결됐다는 증거가 부족하다.

POSCO/MinRes lithium JV는 upstream lithium supply-security Stage2 후보로 기록했다. 지분과 광산 exposure는 공급 안정성에 유리하지만, downstream cost advantage와 margin 확인이 필요하다.

Hyundai Steel/POSCO anti-dumping은 tariff rate, import share, market-relative return이 확인되어 Stage2-Actionable이다. 단 ASP, volume, utilization, raw-material spread가 확인되기 전에는 Green이 아니다.

Hyundai Steel weak-demand와 U.S. localization capex는 각각 4C-watch / false-positive score로 기록했다. 예를 들어 미국 공장 headline이 있어도 funding, IRR, customer demand가 없으면 구조적 evidence가 아니다.

Korea Zinc tender battle은 control premium 4B다. U.S. critical-minerals refinery는 Stage2 strategic-resource 후보지만, funding, offtake, governance, dilution overlay가 닫혀야 한다.

Copper TC/RC squeeze와 China strategic mineral export controls는 전략자원 positive catalyst가 아니라 4C-watch overlay로 분리했다.

## 점수축 보정 방향

올릴 축:

- `tariff_rate_and_import_share`
- `china_dependency_reduction`
- `non_china_capacity_quality_certification`
- `spread_margin_visibility`
- `raw_material_price_durability`
- `tcrc_smelt_margin`
- `strategic_resource_offtake_contract`
- `funding_irr_capex_clarity`
- `control_premium_separation`
- `export_control_exposure`

내릴 축:

- `commodity_price_event_only`
- `control_premium_as_operating_green`
- `localization_capex_without_funding`
- `upstream_stake_without_downstream_margin`
- `tariff_headline_without_ASP_volume`
- `lithium_supply_shock_without_inventory_draw`
- `metal_price_without_spread`
- `strategic_resource_label_only`

## 주의

- production scoring은 변경하지 않았다.
- Stage3-Green threshold를 낮추지 않았다.
- round299 case와 trigger record는 candidate-generation input으로 쓰면 안 된다.
- commodity price rally는 company spread/margin evidence가 아니다.
- control premium은 operating rerating evidence가 아니다.
- full OHLC가 없는데 MFE/MAE를 발명하지 않는다.

## 검증 명령

```bash
PYTHONPATH=src python -m unittest tests.test_round299_r4_loop15_materials_spread_strategic_trigger_validation -v
PYTHONPATH=src python -m e2r.cli.build_round299_r4_loop15_report
```
