# Checkpoint 28A Round 157: R12 Loop 9 Agriculture / Life Services / Misc

## 목적

`docs/round/round_157.md`의 R12 Loop 9 내용을 별도 calibration pack으로 반영했다.
이 라운드는 농업, 교육, 생활가전, 키오스크, 전자담배, cannabis 같은 테마성 높은 영역에서
단순 뉴스와 반복 현금흐름을 분리하는 데 초점이 있다.

예를 들어 조류독감 뉴스만 있으면 Stage 1 재료다. 하지만 정부 백신 주문,
반복 접종, 매출과 OPM이 확인되면 Stage 2 이상으로 볼 수 있다. 반대로
AI 교육 기능 출시가 있어도 bookings miss와 margin 압박이 같이 나오면 RedTeam 신호다.

## 반영 파일

- `src/e2r/sector/round157_r12_loop9_agri_life_misc.py`
- `src/e2r/cli/build_round157_r12_loop9_report.py`
- `tests/test_round157_r12_loop9_agri_life_misc.py`
- `data/e2r_case_library/cases_r12_loop9_round157.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round157_r12_loop9_v9.csv`
- `output/e2r_round157_r12_loop9_agri_life_misc/`

## R12 v9 기본 점수축

R12 Loop 9은 생산 점수를 바꾸지 않고, 아래 7개 축을 calibration 산출물로만 추가했다.

| axis | weight |
| --- | ---: |
| EPS/FCF·OPM conversion | 22 |
| recurring contract/revenue/regulatory visibility | 20 |
| unit economics / price pass-through / demand durability | 18 |
| regulation / litigation / public health / disclosure | 16 |
| capital discipline / debt / cash runway | 10 |
| market mispricing / rerating gap | 8 |
| valuation room / 4B margin | 6 |

## R12 v9 Stage cap

이번 라운드는 점수축보다 Stage cap을 더 명시했다. 예를 들어 `AI 교육 기능 출시`는 사용자가 늘어도
bookings와 paid conversion이 같이 좋아지기 전까지 Stage 1~2에 머문다.

| cap | band | cap |
| --- | --- | --- |
| `stage1_theme_event_cap` | Stage 1 | 45 |
| `stage2_repeat_revenue_unit_economics_cap` | Stage 2 | 70 |
| `stage3_recurring_fcf_gate` | Stage 3 | requires score above 70 and recurring FCF |
| `stage4b_4c_misc_theme_unwind_gate` | 4B/4C | watch or break |

## 핵심 가드레일

- Stage 3-Green 기준은 낮추지 않았다.
- R12 Loop 9 case pack은 candidate generation input이 아니다.
- `round_157.md`의 핵심 target 29개에 맞췄다. 이전 R12 보조 overlay 중 일부는 case의 `secondary_archetypes` 참고값으로만 남기고, v9 score target에서는 제외했다.
- 질병, 곡물가격, AI 교육, 스마트팜, 셀프체크아웃, 니코틴, cannabis 뉴스만으로 Green을 만들지 않는다.
- 반복계약, 반복매출, unit economics, 판가전가, 규제승인 범위, public-health gate, FCF가 확인돼야 한다.
- right-to-repair, Chapter 11, bookings miss, dividend suspension, local self-checkout regulation, youth-safety warning은 RedTeam 자료로 유지한다.

## 산출 요약

| 항목 | 값 |
| --- | ---: |
| score target | 29 |
| base score axis | 7 |
| stage cap | 4 |
| case candidate | 23 |
| success candidate | 5 |
| cyclical success | 2 |
| event premium | 2 |
| failed rerating | 5 |
| Stage 4B case | 3 |
| Stage 4C case | 9 |
| Green possible | 0 |
| Watch/Yellow first | 17 |
| RedTeam first | 12 |
| gate-only target | 8 |

해석하면, 이번 라운드는 “새 Green 후보를 만들기”보다 “테마성 뉴스가 반복 현금흐름으로 전환되는지 검증하기”에 가깝다.
예를 들어 `vertical farming`은 농업 혁신처럼 보일 수 있지만 unit economics와 cash runway가 무너지면 Stage 4C 쪽 증거가 된다.
반대로 animal-health 백신은 단순 질병 뉴스가 아니라 조건부 승인, 정부/농가 반복 주문, OPM/FCF가 같이 확인될 때만 Stage 2 이상으로 올라갈 수 있다.

## 산출물

- `round157_r12_loop9_agri_life_misc_summary.md`
- `round157_r12_loop9_case_matrix.csv`
- `round157_r12_loop9_stage_date_plan.csv`
- `round157_r12_loop9_green_guardrails.md`
- `round157_r12_loop9_unit_economics_caps.md`
- `round157_r12_loop9_price_validation_plan.md`
- `round157_r12_loop9_price_fields.csv`
- `round157_r12_loop9_base_score_axes.csv`
- `round157_r12_loop9_stage_caps.csv`

## 검증

- round157 전용 테스트가 R12 Loop 9 대상 archetype, base score axis, stage cap, writer 산출물, production import guard를 확인한다.
- `PYTHONPATH=src python -m e2r.cli.build_round157_r12_loop9_report`
- `PYTHONPATH=src python -m unittest tests/test_round157_r12_loop9_agri_life_misc.py -v`
- 전체 테스트는 `PYTHONPATH=src python -m unittest discover -s tests -v`로 검증한다.
