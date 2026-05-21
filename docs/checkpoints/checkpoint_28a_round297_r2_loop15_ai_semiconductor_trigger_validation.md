# Checkpoint 28A Round 297 R2 Loop 15 AI/Semiconductor Trigger Validation

## 목적

`docs/round/round_297.md`의 R2 Loop 15 내용을 calibration-only 자료로 반영했다.

이번 라운드의 핵심은 `AI 좋다`, `HBM 좋다` 같은 넓은 테마가 아니다. 공개 trigger가 나왔던 시점에 실제로 어떤 증거가 같이 있었는지를 분리했다.

쉬운 예:

- `HBM3E 양산 + OP 추정 상향 + 당일 상대강도`가 같이 있으면 단순 Stage2보다 강하다.
- 반대로 `OpenAI/Nvidia headline`이 이미 1~2년 급등한 뒤 나오면 좋은 수요 증거이면서 동시에 4B-watch다.

## 반영 파일

- `src/e2r/sector/round297_r2_loop15_ai_semiconductor_trigger_validation.py`
- `src/e2r/cli/build_round297_r2_loop15_report.py`
- `tests/test_round297_r2_loop15_ai_semiconductor_trigger_validation.py`
- `data/e2r_case_library/cases_r2_loop15_round225.jsonl`
- `data/e2r_trigger_calibration/triggers_r2_loop15_round225.jsonl`
- `data/sector_taxonomy/round297_r2_loop15_ai_semiconductor_trigger_validation_audit.json`
- `data/sector_taxonomy/score_weight_profiles_round225_r2_loop15_v1.csv`
- `output/e2r_round297_r2_loop15_ai_semiconductor_trigger_validation/`

## 추가 archetype

- `HBM_FIRST_MOVER_STAGE2_TO_GREEN`
- `HBM_EQUIPMENT_STAGE2_ACTIONABLE`
- `HBM_CATCHUP_LATE_STAGE2`
- `OPENAI_STARGATE_MEMORY_4B_WATCH`
- `SEMICONDUCTOR_EXPORT_CONTROL_4C_WATCH`
- `AI_DEVICE_COMPONENT_STAGE2_ACTIONABLE`
- `DISPLAY_OLED_APPLE_RECOVERY_STAGE2`
- `SEMICONDUCTOR_LABOR_SUPPLY_CHAIN_4C`

## 산출 요약

- cases: 8
- triggers: 10
- Stage2-Actionable candidates: 6
- Stage3-Yellow candidates: 4
- Stage3-Green candidates: 2
- Stage3-Green confirmed: 0
- 4B watch cases: 3
- 4C watch cases: 5
- hard 4C confirmed: 0
- production scoring changed: false
- candidate generation input: false
- full adjusted OHLC complete: false
- shadow weight only: true

## 주요 판정

SK Hynix HBM first-mover는 `missed_structural` 위험이 큰 기준 케이스다. 2024년 HBM mix, OP estimate revision, HBM3E mass production, 상대강도 trigger를 Stage2로만 두면 실제 Stage3-Yellow 진입 시점을 늦게 잡는다.

Hanmi Semiconductor는 `Stage2-Actionable`이다. named customer, HBM packaging equipment, KRW21.48B order, repeat wins, +16% event move가 같이 있었다.

Samsung Electronics는 late catch-up이다. OpenAI/Nvidia/HBM4 trigger는 강하지만 SK Hynix 대비 상대강도가 약하고, labor continuity가 4C-watch로 남아 Green을 막는다.

SK Hynix OpenAI/Stargate/ASML trigger는 demand confirmation이지만 4B overlay가 필요하다. 이미 큰 rerating 이후의 수요 headline은 Green 증거와 과열 감시 신호가 동시에 될 수 있다.

China equipment restriction과 Samsung labor strike는 R2의 4C-watch다. AI memory upcycle이 유지돼도 중국 fab equipment access, 생산 연속성, 노동 리스크는 별도 Red Team overlay다.

LG Innotek은 AI-device `Stage2-Actionable`이다. Apple AI upgrade 기대, OP estimate beat, +19% event move가 강했다. 단 Green은 sell-through, component ASP, inventory 확인 전까지 막는다.

LG Display는 Stage2 evidence에 머문다. Apple OLED order와 loss beat는 좋지만 지속 흑자 guidance와 가격 검증이 없다.

## 점수축 보정 방향

올릴 축:

- `hbm_mix_revenue_share`
- `op_estimate_revision_vs_consensus`
- `mass_production_or_customer_qualification`
- `named_customer_equipment_order`
- `repeat_order_backlog_quality`
- `relative_strength_on_evidence_day`
- `ai_capex_customer_commitment`
- `device_upgrade_op_estimate`

내릴 축:

- `ai_theme_only`
- `customer_name_without_allocation`
- `target_price_raise_without_price_strength`
- `late_catchup_without_relative_strength`
- `capex_without_ROIC_or_dilution_check`
- `openai_or_nvidia_headline_after_parabolic_rally`

## 주의

- production scoring은 변경하지 않았다.
- Stage3-Green threshold를 낮추지 않았다.
- case와 trigger record는 candidate-generation input으로 쓰면 안 된다.
- AI/HBM theme-only는 매출/마진 증거가 아니다.
- full OHLC가 없다는 이유만으로 Stage 후보를 강등하지 않는다.
- full OHLC가 없는데도 MFE/MAE를 발명하지 않는다.
- China export-control, labor continuity, parabolic rally after OpenAI/Nvidia headline은 4B/4C overlay로 유지한다.

## 검증 명령

```bash
PYTHONPATH=src python -m unittest tests.test_round297_r2_loop15_ai_semiconductor_trigger_validation -v
PYTHONPATH=src python -m e2r.cli.build_round297_r2_loop15_report
```
