# Checkpoint 28A Round 285 R3 Loop 14 Secondary Battery EV Green Energy Price Validation

## 반영 내용

- `docs/round/round_285.md`의 R3 Loop 14 가격경로 검증 라운드를 calibration-only case pack으로 반영했다.
- 신규 canonical archetype 8개를 추가했다.
- LGES/Ford/Freudenberg 계약취소, Samsung SDI/GM JV, SK On 구조조정/ESS pivot, EcoPro Materials/SK IE battery-material beta, Hanwha/Qcells solar customs gate, Hyundai hydrogen capex, SK/Group14 silicon anode, 한국 배터리 ESS pivot basket을 저장했다.
- Reuters / MarketWatch anchor 기반의 event return, 계약금액, 영업손실, 공장투자, JV reset, furlough, funding metrics를 저장했다.
- full adjusted OHLC가 없는 항목은 `price_data_unavailable_after_deep_search` 또는 `reported_event_anchor_not_full_ohlc`로 명시했다.
- production scoring과 candidate generation은 변경하지 않았다.

## 생성 파일

- `src/e2r/sector/round285_r3_loop14_secondary_battery_ev_green_energy_price_validation.py`
- `src/e2r/cli/build_round285_r3_loop14_report.py`
- `tests/test_round285_r3_loop14_secondary_battery_ev_green_energy_price_validation.py`
- `data/e2r_case_library/cases_r3_loop14_round285.jsonl`
- `data/sector_taxonomy/round285_r3_loop14_secondary_battery_ev_green_energy_price_validation_audit.json`
- `output/e2r_round285_r3_loop14_secondary_battery_ev_green_energy_price_validation/`

## 핵심 결론

- LG Energy Solution은 R3 hard 4C reference다. Ford 9.6T KRW와 Freudenberg 3.9T KRW 계약취소로 combined expected revenue loss가 13.5T KRW까지 커졌다.
- Samsung SDI / GM JV는 Stage 2다. $3.5B JV와 27GWh~36GWh capacity는 의미 있지만, EV demand와 Q4 operating loss가 Green을 막는다.
- SK Innovation / SK On은 restructuring + ESS pivot Stage 2다. SK E&S merger와 Flatiron 7.2GWh ESS deal은 긍정적이나, Ford JV 해체와 손실 확대가 남아 있다.
- EcoPro Materials / SK IE Technology는 customer model-mix beta다. Ford의 BEV-to-hybrid/EREV 전환은 vehicle당 battery content 감소 리스크다.
- Hanwha/Qcells는 solar policy success_candidate지만 customs gate가 있다. DOE loan guarantee보다 부품 통관, factory utilization, module ASP가 중요하다.
- Hyundai hydrogen plant는 green capex Stage 2다. 공장 착공은 수요가 아니며 utilization과 unit economics가 필요하다.
- SK/Group14는 silicon-anode technology Stage 2다. 비상장 기술 scale-up은 listed EPS/value bridge 없이는 Green이 아니다.
- ESS pivot basket은 다음 cycle 후보지만, PO value, shipment, installation, margin, repeat order 전에는 Green이 아니다.

## Shadow Weight 보정

올릴 축:

- `customer_calloff_visibility`
- `contract_cancellation_risk`
- `plant_utilization`
- `EV_model_mix_battery_content`
- `subsidy_tariff_policy_stability`
- `ESS_PO_value_and_margin`
- `supply_chain_customs_clearance`
- `localization_execution`
- `raw_material_cost_pass_through`
- `listed_value_bridge_for_unlisted_tech`

내릴 축:

- `EV_growth_headline_only`
- `signed_contract_without_calloff`
- `capacity_capex_without_utilization`
- `IRA_or_policy_loan_only`
- `ESS_pivot_without_contract_value`
- `hybrid_shift_ignored`
- `unlisted_material_tech_readthrough`
- `solar_factory_without_customs_clearance`
- `hydrogen_capex_without_demand`

## Green Gate

R3 Stage 3-Green은 “배터리·EV·IRA·태양광·수소·ESS” 같은 단어가 아니라 다음 증거가 닫힐 때만 가능하다.

- 실제 고객 call-off / shipment / revenue recognition
- 공장 utilization
- AMPC / IRA / tariff / subsidy 지속성
- BEV-to-hybrid/EREV 전환에 따른 battery content 감소 여부
- ESS PO value / installation / margin
- 소재 raw-material pass-through와 customer production schedule
- 태양광 customs clearance와 full supply-chain localization
- 수소 customer demand와 unit economics
- 비상장 기술의 listed EPS/value bridge
- evidence 이후 price path 확인

## 검증

- 전용 테스트: `PYTHONPATH=src python -m unittest tests.test_round285_r3_loop14_secondary_battery_ev_green_energy_price_validation -v`
- 라운드 산출물 생성: `PYTHONPATH=src python -m e2r.cli.build_round285_r3_loop14_report`

## 금지 사항

- 이 case pack을 candidate-generation input으로 쓰지 않는다.
- Stage 3-Green threshold를 낮추지 않는다.
- full OHLC, stage price, MFE/MAE를 임의 생성하지 않는다.
- 정책자금, 공장착공, JV, ESS pivot, 수소/태양광/배터리 키워드만으로 Green을 만들지 않는다.
