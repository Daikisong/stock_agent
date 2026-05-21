# Checkpoint 28A Round 310 R2 Loop 16 AI·반도체·전자부품 Trigger Validation

## 목적

`docs/round/round_310.md`의 R2 Loop 16 내용을 calibration/evaluation 자료로 반영했다. 이번 라운드는 HBM, DRAM/NAND ASP, OpenAI/Stargate, 파운드리 대형계약, 후공정 장비, 수출통제, 노동 리스크, 전자부품/센서 전략투자를 한 덩어리로 보지 않고 trigger 단위로 분리한다.

쉬운 예시:

- SK Hynix의 HBM4 인증과 EUV CAPA 투자는 Stage3-Yellow 후보가 될 수 있다.
- 하지만 고객 volume shipment, margin, 고객집중도, full OHLC가 닫히기 전에는 Stage3-Green으로 확정하지 않는다.
- OpenAI/Stargate 협력은 수요 방향을 보여주지만, binding wafer order가 없으면 실제 출하/매출 증거로 보지 않는다.

## 반영 파일

- `src/e2r/sector/round310_r2_loop16_ai_semiconductor_electronic_components_trigger_validation.py`
- `src/e2r/cli/build_round310_r2_loop16_report.py`
- `tests/test_round310_r2_loop16_ai_semiconductor_electronic_components_trigger_validation.py`
- `data/e2r_case_library/cases_r2_loop16_round238.jsonl`
- `data/e2r_trigger_calibration/triggers_r2_loop16_round238.jsonl`
- `data/sector_taxonomy/round310_r2_loop16_ai_semiconductor_electronic_components_trigger_validation_audit.json`
- `data/sector_taxonomy/score_weight_profiles_round238_r2_loop16_v1.csv`
- `output/e2r_round310_r2_loop16_ai_semiconductor_electronic_components_trigger_validation/`

## Canonical Archetype 추가

- `HBM_LEADERSHIP_STAGE2_TO_GREEN_CANDIDATE`
- `MEMORY_SUPERCYCLE_ASP_STAGE2_YELLOW`
- `OPENAI_STARGATE_HBM_DEMAND_STAGE2_ACTIONABLE`
- `FOUNDRY_MEGA_CONTRACT_STAGE2_WITH_YIELD_4B`
- `ADVANCED_PACKAGING_EQUIPMENT_STAGE2_WITH_RUMOR_4B`
- `HBM_CERTIFICATION_DELAY_FALSE_POSITIVE`
- `ELECTRONIC_COMPONENT_LIDAR_STAGE2_ORDER_GATE`

기존 canonical archetype 중 아래 2개도 이번 target alias로 재사용했다.

- `CHINA_FAB_EXPORT_CONTROL_4C_WATCH`
- `SEMICONDUCTOR_LABOR_STRIKE_4C_WATCH`

## 케이스 요약

| case | 판정 |
| --- | --- |
| SK Hynix HBM3E/HBM4/EUV | Stage3-Yellow 후보. Green은 volume shipment, HBM margin, 고객집중도 확인 전 보류 |
| Samsung memory supercycle | ASP와 OP guidance beat 기반 Stage3-Yellow 후보. labor/export-control/HBM lag는 4B/4C overlay |
| Samsung/SK Hynix OpenAI Stargate | Stage2-Actionable demand trigger. binding PO 전에는 Green 금지 |
| Samsung foundry $16.5B | Stage2 + 4B-watch. node/yield/customer/fab utilization 필요 |
| Hanmi Semiconductor HBM equipment | Stage2-Actionable + rumor 4B. Micron 미확정 루머는 signed order 전 Green 금지 |
| Samsung HBM certification delay | HBM qualification 4C-watch |
| Samsung/SK Hynix China fab export curbs | export-control 4C-watch |
| Samsung labor strike | DRAM/NAND output continuity 4C-watch |
| LG Innotek / Aeva lidar | Stage2 component diversification. design-in과 mass production order 필요 |

## Trigger 결과

- case_candidate_count: `9`
- trigger_count: `11`
- target_archetype_count: `9`
- stage2_actionable_candidate_count: `4`
- stage2_event_candidate_count: `2`
- stage3_yellow_candidate_count: `4`
- stage3_green_confirmed_count: `0`
- stage4b_watch_count: `5`
- stage4c_watch_count: `3`
- hard_4c_case_count: `0`

## 핵심 보정 방향

올릴 축:

- `hbm_customer_certification`
- `hbm_mass_production_shipment`
- `memory_asp_contract_power`
- `op_estimate_guidance_beat`
- `euv_capacity_commitment`
- `advanced_packaging_order_visibility`
- `binding_ai_infra_purchase`
- `export_license_stability`
- `labor_output_continuity`

내릴 축:

- `hbm_headline_without_customer_certification`
- `foundry_contract_without_node_yield`
- `ai_partnership_without_binding_order`
- `equipment_rumor_without_signed_order`

## Guardrail

- production scoring 변경 없음
- candidate generation input 아님
- shadow weight only
- full adjusted OHLC 미확보
- OHLC 미확보만으로 Stage2/Yellow 후보를 강등하지 않음
- AI 반도체 headline만으로 Stage3-Green 금지
- HBM/메모리/파운드리/후공정/수출통제/노동/센서 partnership row를 분리

## 검증

실행한 핵심 명령:

```bash
PYTHONPATH=src python -m unittest tests/test_round310_r2_loop16_ai_semiconductor_electronic_components_trigger_validation.py -v
PYTHONPATH=src python -m e2r.cli.build_round310_r2_loop16_report
```

전용 테스트와 리포트 생성은 통과했다. 전체 테스트는 최종 커밋 전 다시 실행한다.
