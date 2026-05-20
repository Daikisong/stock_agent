# Checkpoint 28A Round 233 R3 Loop 10 Battery EV Green Price Validation

## 반영 내용

- `docs/round/round_233.md`의 R3 Loop 10 라운드를 calibration-only 검증팩으로 구조화했다.
- 배터리/EV/ESS/태양광/수소/리튬 이벤트 케이스를 `BATTERY_EV_GREEN` 대섹터 팩으로 추가했다.
- LGES, SK On, Samsung SDI, LG Chem, Hanwha Qcells, SKIET/EcoPro Materials, POSCO Future M/L&F, Hyundai hydrogen capex 케이스를 저장했다.
- Reuters/MarketWatch/AP/WSJ류 reported anchor에서 확인된 GWh, CAPEX, JV, 지분, 인력 감축, 이벤트 수익률만 저장했다.
- 원시 OHLC가 없는 항목은 `price_data_unavailable_after_deep_search` 또는 `reported_event_anchor_not_full_ohlc`로 명시했다.
- production scoring과 candidate generation은 변경하지 않았다.

## 핵심 케이스

- LG Energy Solution: 5GWh ESS 계약과 Tennessee ESS 전환은 Stage 2 watch이지만, Ohio Ultium 재가동 불확실성과 850명 layoff 때문에 4C-watch를 붙였다.
- SK On: Flatiron 7.2GWh LFP ESS order는 Stage 2지만, 계약금액, utilization, OPM, FCF 전에는 Green 금지로 남겼다.
- Samsung SDI: GM Indiana JV는 27GWh에서 36GWh까지 확장 가능하고 이벤트 당일 +3.2% anchor가 있지만, GM EV forecast cut과 2027년 양산 시점 때문에 Stage 2 watch로 유지했다.
- LG Chem: Toyota Tsusho 25% 참여와 Huayou 49%에서 24% 축소는 supply-chain derisking 증거지만, offtake, OPM, FCF 확인 전에는 Green이 아니다.
- Hanwha Qcells: 미국 현지화와 $2.3B facility는 Stage 2 증거지만, UFLPA/customs detention, 1,000명 reduced hours/pay, 300명 contract worker cut은 4C-watch다.
- SKIET/EcoPro Materials basket: Ford EV retreat와 hybrid pivot 충격으로 separator/precursor 계열은 수요 확인 전 Green 금지다.
- POSCO Future M/L&F: lithium futures +8%와 소재주 당일 상승은 price-only event premium으로 처리했다.
- Hyundai hydrogen fuel-cell plant: 9,300억 원 capex와 2027년 완공 계획은 Stage 2 watch이지만, order book, utilization, margin, FCF 확인 전에는 Green이 아니다.

## Green Gate 보강

R3 Stage 3-Green은 단순히 `배터리`, `ESS`, `친환경`, `미국 현지화` 수혜가 아니다.

예를 들어, `5GWh ESS contract`는 좋은 씨앗이지만 Stage 3는 그 씨앗이 실제 call-off, 매출, 가동률, OPM, FCF로 확인되는 순간이다.

필수 조건:

- binding contract
- actual call-off
- GWh 또는 tonnage volume
- utilization improvement
- OPM 또는 gross margin improvement
- FCF after CAPEX
- subsidy 제외 profit quality
- customer EV strategy risk 통과
- supply-chain disruption risk 통과
- evidence 이후 price path 확인

금지 조건:

- 고객명만 있음
- factory groundbreaking만 있음
- JV restructuring만 있음
- ESS/LFP theme만 있음
- capacity conversion만 있음
- lithium price event만 있음
- AMPC/subsidy 품질 저하 무시
- EV demand slowdown 무시

## 산출물

- `data/e2r_case_library/cases_r3_loop10_round233.jsonl`
- `data/sector_taxonomy/round233_r3_loop10_battery_ev_green_price_validation_audit.json`
- `output/e2r_round233_r3_loop10_battery_ev_green_price_validation/round233_r3_loop10_price_validation_summary.md`
- `output/e2r_round233_r3_loop10_battery_ev_green_price_validation/round233_r3_loop10_case_matrix.csv`
- `output/e2r_round233_r3_loop10_battery_ev_green_price_validation/round233_r3_loop10_shadow_weights.csv`
- `output/e2r_round233_r3_loop10_battery_ev_green_price_validation/round233_r3_loop10_green_gate_review.md`
- `output/e2r_round233_r3_loop10_battery_ev_green_price_validation/round233_r3_loop10_stage4b_4c_review.md`
- `output/e2r_round233_r3_loop10_battery_ev_green_price_validation/round233_r3_loop10_price_validation_plan.md`

## 검증

- `PYTHONPATH=src python -m unittest tests/test_round233_r3_loop10_battery_ev_green_price_validation.py -v`
- `PYTHONPATH=src python -m e2r.cli.build_round233_r3_loop10_report`

## 다음 단계

- 원시 수정주가 OHLC를 확보하면 `reported_event_anchor_not_full_ohlc` 항목의 MFE/MAE를 정밀 backfill한다.
- R3 shadow weight는 아직 production scoring에 적용하지 않는다.
- 다음 scoring 라운드에서는 `actual_calloff`, `utilization`, `opm_fcf`, `customer_quality`, `supply_chain_derisking`을 Green gate 후보 축으로 shadow 비교한다.
