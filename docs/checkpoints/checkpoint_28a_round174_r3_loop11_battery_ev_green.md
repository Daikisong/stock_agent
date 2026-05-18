# Checkpoint 28A Round 174: R3 Loop 11 Korea Battery / EV / Green

## 목적

`docs/round/round_174.md`의 R3 Loop 11 내용을 calibration pack으로 반영했다.
이번 라운드는 국장 배터리·ESS·양극재·음극재·분리막·전해액·리튬·소재 과열 케이스를 분리해서 본다.

핵심은 단순하다.
`EV`, `ESS`, `리튬`, `흑연`, `양극재`라는 이름만으로는 Stage 3-Green이 아니다.
고객, 계약금액, 공급기간, GWh/톤수, 생산 시작, 라인 전환, 가동률, OPM, FCF, 원재료 노출, 고객사 EV 전략, 가격 경로가 같이 확인되어야 한다.

쉬운 예로, 삼성SDI ESS LFP 계약은 큰 계약과 라인 전환이 있어 Stage 2 strong 후보가 될 수 있다.
하지만 고객 비공개, ESS OPM 미확인, 전환 라인 가동률 미확인 상태라면 Stage 3-Green은 막는다.

## 반영 파일

- `src/e2r/sector/round174_r3_loop11_battery_ev_green.py`
- `src/e2r/cli/build_round174_r3_loop11_report.py`
- `tests/test_round174_r3_loop11_battery_ev_green.py`
- `data/e2r_case_library/cases_r3_loop11_round174.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round174_r3_loop11_v11.csv`
- `output/e2r_round174_r3_loop11_battery_ev_green/`

## R3 Loop 11 Target

원문 canonical target 12개를 그대로 분리했다.

| target | 역할 |
| --- | --- |
| `ESS_LFP_GRID_STORAGE_KOREA` | 삼성SDI형 ESS LFP 장기공급계약 / 라인 전환 |
| `EV_TO_ESS_CAPACITY_REDEPLOYMENT_KOREA` | EV CAPA를 ESS로 재배치하는 경로 |
| `ANODE_GRAPHITE_SUPPLYCHAIN_KOREA` | POSCO Future M / Syrah형 흑연 공급망 |
| `CATHODE_LONG_CONTRACT_VISIBILITY` | LG Chem형 양극재 장기계약·지분 재편 |
| `LITHIUM_RESOURCE_SECURITY_KOREA` | POSCO Holdings형 리튬 광산·자원안보 |
| `BATTERY_MATERIALS_CAPEX_OVERHEAT_KOREA` | EcoPro Materials형 CAPA narrative 과열 |
| `SEPARATOR_EV_DEMAND_CYCLE` | SKIET/WCP형 분리막 EV 수요 사이클 |
| `ELECTROLYTE_CAPA_SUPPLYCHAIN` | Enchem형 전해액 CAPA·고객 backfill |
| `SILICON_ANODE_COMMERCIALIZATION` | 대주전자재료형 실리콘 음극재 상용화 |
| `EVENT_LITHIUM_PRICE_RALLY` | CATL 광산 중단 같은 리튬 이벤트 랠리 |
| `CONTRACT_CANCELLATION_CUSTOMER_STRATEGY_RISK` | 고객 전략 변경·계약 취소 hard gate |
| `DISCLOSURE_CONFIDENCE_CAP` | 고객·금액·기간·마진 detail 부족 cap |

## 기본 점수축

| component | points |
| --- | ---: |
| EPS/FCF/OPM conversion | 24 |
| contract visibility | 22 |
| CAPA utilization / line conversion | 14 |
| structural demand shift | 12 |
| early price-path validation | 10 |
| safety / regulatory / disclosure confidence | 8 |
| valuation room / 4B runway | 10 |

이번 라운드는 배터리 소재에서 “CAPA가 있다”를 점수로 바로 인정하지 않는다.
예를 들어 EV 수요 둔화로 놀고 있는 라인을 ESS로 돌린다고 해도, 실제 ESS 고객 계약과 가동률, OPM이 없으면 긍정 증거가 아니라 비용 리스크일 수 있다.

## 케이스 요약

| case | 판정 |
| --- | --- |
| 삼성SDI ESS LFP | 2조원+ / 2027년부터 3년 공급 / 라인 전환. Stage 2 strong, Green cap |
| POSCO Future M graphite | Syrah 6년 offtake + 미국 흑연 관세 이벤트. Stage 2 + 4B-watch |
| POSCO Holdings lithium | Wodgina/Mt Marion JV 지분. 자원안보 Stage 2, 리튬 사이클 cap |
| LG Chem Toyota Tsusho | 양극재 지분 재편. 공급망 Stage 2, OPM/가동률 전 Green 금지 |
| LG Chem-Exxon | non-binding lithium deal. Stage 1/2 option, 확정계약 전 cap |
| L&F/POSCO Future M lithium event | CATL Yichun mine suspension 이벤트 랠리. 구조적 Green 아님 |
| SKIET | EV 둔화, SK On 손실, sale review. 4C-watch |
| EcoPro Materials | IPO/CAPA/vertical narrative와 EV 둔화·손실 충돌. 4C-watch |
| WCP | 분리막 수요·가동률 backfill 전 Watch/Red |
| Enchem | 전해액 CAPA는 고객·OPM·가격경로 확인 전 Watch |
| Daejoo | 실리콘 음극재 상용화는 고객 qualification·volume revenue 전 Stage 1/2 |

## 산출 요약

| 항목 | 값 |
| --- | ---: |
| target | 12 |
| source canonical target | 12 |
| case candidate | 11 |
| base score component | 7 |
| stage cap | 6 |
| score-stage-price alignment | 10 |
| structural success | 0 |
| success candidate | 5 |
| event premium | 2 |
| failed rerating | 1 |
| Stage 4B case | 1 |
| Stage 4C case | 2 |
| Green possible target | 1 |
| hard gate target | 2 |

## 핵심 가드레일

- Round 174 case pack은 candidate generation input이 아니다.
- production scoring/staging/RedTeam 로직은 변경하지 않았다.
- Stage 3-Green은 ESS·리튬·흑연·양극재·분리막·전해액 이름이 아니라 계약 detail, 가동률, OPM, FCF, 고객 전략 안정성이 맞을 때만 가능하다.
- policy/tariff/lithium 이벤트 랠리는 Stage 4B-watch로 식힌다.
- non-binding deal은 연구 라우팅 근거일 수 있지만 Stage 3 근거가 아니다.
- 고객 계약 취소, 공장 idle, sale review, 고객사 EV 전략 후퇴, 지속 영업손실은 hard RedTeam으로 둔다.
- 고객명·계약금액·GWh/톤수·가동률·마진·stage price·MFE/MAE는 없으면 비워둔다.

## 산출물

- `round174_r3_loop11_battery_ev_green_summary.md`
- `round174_r3_loop11_case_matrix.csv`
- `round174_r3_loop11_stage_date_plan.csv`
- `round174_r3_loop11_green_guardrails.md`
- `round174_r3_loop11_risk_overlays.md`
- `round174_r3_loop11_price_validation_plan.md`
- `round174_r3_loop11_price_fields.csv`
- `round174_r3_loop11_base_score_weights.csv`
- `round174_r3_loop11_stage_caps.csv`
- `round174_r3_loop11_score_stage_price_alignment.csv`
- `round174_r3_loop11_score_stage_price_alignment.md`

## 검증

- `PYTHONPATH=src python -m e2r.cli.build_round174_r3_loop11_report` 통과.
- `PYTHONPATH=src python -m unittest tests.test_round174_r3_loop11_battery_ev_green -v` 통과. `13 tests`.
- `PYTHONPATH=src python -m compileall -q src tests` 통과.
- `PYTHONPATH=src python -m unittest discover -s tests -v` 통과. `2241 tests`.
- `git diff --check` 통과.
