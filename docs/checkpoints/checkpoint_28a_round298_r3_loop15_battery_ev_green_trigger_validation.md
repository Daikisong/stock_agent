# Checkpoint 28A Round 298 R3 Loop 15 Battery/EV/Green Trigger Validation

## 목적

`docs/round/round_298.md`의 R3 Loop 15 내용을 calibration-only 자료로 반영했다.

이번 라운드의 핵심은 `2차전지 계약`, `EV 성장`, `리튬 가격 반등` 같은 headline을 그대로 Stage 3-Green으로 올리지 않는 것이다. 실제 판단에는 고객 call-off, 납품, 보조금 제외 margin, ESS 전환 실행, FEOC/IRA 적합성, 안전/공시 신뢰를 따로 닫아야 한다.

쉬운 예:

- `2조원 ESS 계약 + 납품 일정 + EV 라인 전환`은 Stage2-Actionable 후보가 될 수 있다.
- 하지만 `납품 시작`, `전환 라인 가동률`, `ESS margin`이 없으면 Green은 아니다.
- `Tesla 계약 29억 달러`처럼 커 보이는 계약도 실제 call-off가 사라지면 hard 4C다.

## 반영 파일

- `src/e2r/sector/round298_r3_loop15_battery_ev_green_trigger_validation.py`
- `src/e2r/cli/build_round298_r3_loop15_report.py`
- `tests/test_round298_r3_loop15_battery_ev_green_trigger_validation.py`
- `data/e2r_case_library/cases_r3_loop15_round226.jsonl`
- `data/e2r_trigger_calibration/triggers_r3_loop15_round226.jsonl`
- `data/sector_taxonomy/round298_r3_loop15_battery_ev_green_trigger_validation_audit.json`
- `data/sector_taxonomy/score_weight_profiles_round226_r3_loop15_v1.csv`
- `output/e2r_round298_r3_loop15_battery_ev_green_trigger_validation/`

## 추가 archetype

- `BATTERY_AMPC_PROFIT_STAGE2_YELLOW`
- `ESS_LFP_PIVOT_STAGE2_ACTIONABLE`
- `EV_DEMAND_CONTRACT_CANCELLATION_4C`
- `SIGNED_CATHODE_CONTRACT_COLLAPSE_HARD_4C`
- `LITHIUM_PRICE_EVENT_PREMIUM`
- `UPSTREAM_LITHIUM_SUPPLY_STAGE2`
- `FEOC_CATHODE_OWNERSHIP_STAGE2`
- `BATTERY_SAFETY_TRUST_HARD_4C_REFERENCE`

## 산출 요약

- cases: 8
- triggers: 9
- Stage2-Actionable candidates: 4
- Stage3-Yellow candidates: 2
- Stage3-Green candidates: 0
- Stage3-Green confirmed: 0
- 4B watch cases: 3
- 4C watch cases: 4
- hard 4C cases: 2
- production scoring changed: false
- candidate generation input: false
- full adjusted OHLC complete: false
- shadow weight only: true

## 주요 판정

LG Energy Solution은 AMPC 포함 OP beat가 강하지만, 보조금 제외 OP가 약하고 Ford/Freudenberg cancellation overlay가 있어 Stage3-Yellow 후보에 머문다.

Samsung SDI는 ESS LFP 계약, 납품 일정, EV-to-ESS 라인 전환, 시장 대비 강한 반응이 있어 Stage2-Actionable이다. 단 2027년 delivery와 전환 라인 margin 확인 전에는 Green이 아니다.

SK On/Ford JV termination과 LGES Ford/Freudenberg cancellation은 EV battery 계약 story가 고객 모델과 생산 일정이 깨지면 4C-watch로 바뀐다는 기준 케이스다.

L&F/Tesla cathode 계약은 hard 4C다. 계약액이 29억 달러에서 7,386달러로 붕괴했으므로, signed contract amount는 actual call-off 없이 Green 근거가 될 수 없다.

CATL Yichun mine suspension에 따른 lithium rally는 event premium이다. POSCO Future M, L&F, Samsung SDI, LGES가 반응했지만, durable lithium price와 소재 ASP/margin이 확인되기 전에는 Stage3가 아니다.

POSCO/MinRes lithium JV는 Stage2 supply-security다. upstream stake와 offtake right는 좋아졌지만, 비용우위와 downstream margin이 아직 닫히지 않았다.

LG Chem/Toyota Tsusho cathode plant ownership change는 Stage2 regulatory-risk reduction이다. China exposure는 낮아졌지만 customer award, IRA benefit, cathode margin이 필요하다.

Aricell/S-Connect 및 EV battery supplier disclosure 이슈는 battery safety/trust hard gate다. 배터리 업종에서 안전과 공시 신뢰는 단순 부가 리스크가 아니라 Stage 4C 판단 축이다.

## 점수축 보정 방향

올릴 축:

- `actual_customer_calloff`
- `contract_cancellation_risk`
- `ex_subsidy_operating_margin`
- `ampc_subsidy_durability`
- `ess_lfp_contract_quality`
- `line_conversion_execution`
- `customer_model_survival`
- `battery_safety_disclosure_trust`
- `raw_material_price_durability`
- `feoc_ira_compliance_quality`

내릴 축:

- `signed_contract_amount_only`
- `ev_growth_headline_only`
- `subsidy_included_op_only`
- `lithium_price_event_only`
- `upstream_stake_without_margin`
- `line_conversion_without_delivery`
- `customer_name_without_model_survival`
- `battery_safety_ignored`

## 주의

- production scoring은 변경하지 않았다.
- Stage3-Green threshold를 낮추지 않았다.
- case와 trigger record는 candidate-generation input으로 쓰면 안 된다.
- signed contract amount는 actual call-off가 아니다.
- AMPC 포함 OP는 보조금 제외 margin이 아니다.
- lithium price event return은 durable ASP/margin이 아니다.
- safety/disclosure trust issue는 battery/EV hard gate로 유지한다.
- full OHLC가 없는데 MFE/MAE를 발명하지 않는다.

## 검증 명령

```bash
PYTHONPATH=src python -m unittest tests.test_round298_r3_loop15_battery_ev_green_trigger_validation -v
PYTHONPATH=src python -m e2r.cli.build_round298_r3_loop15_report
```
