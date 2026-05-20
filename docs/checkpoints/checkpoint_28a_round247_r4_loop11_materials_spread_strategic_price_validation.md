# Checkpoint 28A Round 247 R4 Loop 11 Materials Spread Strategic Resources Price Validation

## 반영 내용

- `docs/round/round_247.md`의 R4 Loop 11 내용을 calibration-only case pack으로 구조화했다.
- 신규 canonical archetype을 추가했다.
  - `CRITICAL_MINERALS_SUPPLY_CHAIN`
  - `STRATEGIC_METALS_DILUTION_GOVERNANCE`
  - `PETROCHEMICAL_CAPACITY_RESTRUCTURING`
  - `STANDALONE_NCC_CREDIT_BREAK`
  - `STEEL_ANTIDUMPING_POLICY_RELIEF`
  - `STEEL_TARIFF_EXPORT_RISK`
  - `CATHODE_SUPPLY_CHAIN_DERISKING`
  - `NON_CHINA_POLYSILICON_OPTIONALITY`
  - `BATTERY_MATERIAL_CONTRACT_QUALITY_BREAK`
  - `COMMODITY_PRICE_EVENT_PREMIUM`
- `LITHIUM_RESOURCE_SECURITY`는 기존 canonical archetype을 그대로 사용했다.
- production scoring과 candidate generation은 변경하지 않았다.

쉬운 예시: `OCI + SpaceX 보도`는 관심 신호가 될 수 있지만, 고객·계약·offtake가 확인되지 않았으므로 Stage 3-Green 근거가 아니다. 이번 패치는 이런 경우를 `event premium / 4B-watch`로 남기기 위한 검증 자료다.

## 생성 파일

- `src/e2r/sector/round247_r4_loop11_materials_spread_strategic_price_validation.py`
- `src/e2r/cli/build_round247_r4_loop11_report.py`
- `tests/test_round247_r4_loop11_materials_spread_strategic_price_validation.py`
- `data/e2r_case_library/cases_r4_loop11_round247.jsonl`
- `data/sector_taxonomy/round247_r4_loop11_materials_spread_strategic_price_validation_audit.json`
- `output/e2r_round247_r4_loop11_materials_spread_strategic_price_validation/`

## 케이스 요약

| case | 분류 | Stage 3 | 핵심 판단 |
|---|---|---|---|
| Korea Zinc | success_candidate + governance watch | 없음 | 전략광물 프로젝트는 Stage 2지만 FID/offtake/margin/FCF와 governance/dilution 통과 전 Green 금지 |
| Lotte Chemical / HD Hyundai Chemical | failed_rerating + restructuring relief | 없음 | Daesan NCC shutdown은 relief지만 spread/OPM/FCF 확인 전 Green 금지 |
| YNCC | 4C-watch | 없음 | standalone NCC credit break로 RedTeam 우선 |
| Hyundai Steel / POSCO | event premium + tariff 4C-watch | 없음 | 국내 anti-dumping relief와 export tariff risk를 동시에 봐야 함 |
| LG Chem / Toyota Tsusho | success_candidate | 없음 | China exposure derisking은 Stage 2, cathode offtake/volume/margin 필요 |
| POSCO / MinRes | success_candidate + lithium cycle watch | 없음 | resource security는 Stage 2, downstream margin/FCF 필요 |
| OCI / SpaceX | success_candidate + event premium | 없음 | Texas expansion은 Stage 2, SpaceX 보도는 미확정 media report |
| L&F / Tesla | hard 4C | 없음 | 고객명과 계약 headline만으로 Green을 주면 안 되는 hard 4C 기준점 |

## 핵심 Green Gate

R4 Stage 3-Green은 다음이 실제로 확인되어야 한다.

- `product_spread_confirmed`
- `cost_curve_advantage`
- `supply_discipline_or_capacity_shutdown_confirmed`
- `offtake_price_floor_or_take_or_pay`
- `fcf_after_working_capital`
- `contract_quality_confirmed`
- `china_tariff_sanction_governance_risk_passed`
- `capex_burden_and_dilution_risk_passed`
- `price_path_after_evidence`

금지 패턴도 명시했다.

- `commodity_price_spike_only`
- `strategic_material_headline_only`
- `policy_relief_only`
- `unconfirmed_media_report`
- `restructuring_plan_only`
- `customer_name_only_material_contract`
- `resource_deal_without_offtake`
- `governance_dilution_unresolved`

## 4B / 4C 기준

- 4B-watch: 원자재 가격 반등, 전략광물 headline, 반덤핑 relief, 구조조정 기대, 미확정 고객 보도처럼 가격이 증거보다 먼저 움직이는 경우
- hard 4C: 계약가치 붕괴, 계약취소, spread reversal, China oversupply, standalone cracker credit break, share issuance/governance abuse, tariff shock, offtake failure, FCF deterioration
- 이번 라운드의 확정 hard 4C는 `L&F / Tesla cathode contract value collapse`다.

## 산출 요약

- case count: 8
- target archetype count: 11
- success_candidate: 4
- failed_rerating: 2
- event_premium: 1
- hard_4c: 1
- Stage 3 dated cases: 0
- full OHLC complete: false
- price validation: partial with reported price anchors
- production scoring changed: false
- candidate generation input: false
- shadow weight only: true

## 실행한 명령

```bash
PYTHONPATH=src python -m py_compile src/e2r/sector/archetypes.py src/e2r/sector/round247_r4_loop11_materials_spread_strategic_price_validation.py src/e2r/cli/build_round247_r4_loop11_report.py tests/test_round247_r4_loop11_materials_spread_strategic_price_validation.py
PYTHONPATH=src python -m unittest tests.test_round247_r4_loop11_materials_spread_strategic_price_validation -v
PYTHONPATH=src python -m e2r.cli.build_round247_r4_loop11_report
```

## 남은 작업

- full OHLC가 없으므로 MFE/MAE 장기 검증은 아직 제한적이다.
- 다음 단계에서도 이 case pack은 scoring input이 아니라 calibration/evaluation 자료로만 써야 한다.
- 예: `lithium resource security`가 Stage 2로 좋아 보여도, downstream margin과 FCF가 없으면 Stage 3-Green으로 올리지 않는다.
