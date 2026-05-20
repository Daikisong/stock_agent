# Checkpoint 28A Round 284 R2 Loop 14 AI Semiconductor Electronic Components Price Validation

## 반영 범위

- 원문: `docs/round/round_284.md`
- analyst round id: `round_212`
- large sector: `AI_SEMICONDUCTOR_ELECTRONIC_COMPONENTS`
- production scoring changed: false
- candidate generation input: false
- shadow weight only: true
- hard 4C confirmed: false
- hard 4C watch confirmed: true
- price validation: partial with reported price anchors
- full adjusted OHLC: false

이번 라운드는 AI·반도체·전자부품에서 `AI`, `HBM`, `Nvidia`, `OpenAI`, `Apple AI`, `OLED`, `AI chip startup` 같은 단어가 Stage 3-Green을 자동으로 만들지 않도록 검증팩을 추가했다.

쉬운 예: `OpenAI LOI`는 강한 수요 신호지만, binding take-or-pay 계약과 ASP/margin, capacity allocation, shipment schedule이 확인되기 전에는 Green 근거가 아니다.

## 추가된 canonical archetype

- `HBM_DOMINANCE_STAGE3_AND_4B`
- `SAMSUNG_HBM_CATCHUP_AND_LABOR_4C_WATCH`
- `TC_BONDER_HBM_EQUIPMENT_EVENT_PREMIUM`
- `ON_DEVICE_AI_IPHONE_COMPONENT_STAGE2`
- `OLED_PORTFOLIO_RESTRUCTURING_STAGE2`
- `KOREAN_AI_CHIP_FABLESS_STAGE2`
- `AI_INFRA_MEMORY_SUPPLY_MOU_4B`
- `CONSUMER_ELECTRONICS_COMPONENT_COST_4C_WATCH`

## 추가된 케이스

| case | 판정 | 핵심 |
|---|---|---|
| SK Hynix HBM | structural success + 4B-watch | Q2 2024 OP 5.47T KRW, Q4 2025 OP 19.2T KRW, HBM share 61%, 2026 valuation/crowding watch |
| Samsung Electronics HBM catch-up | success candidate + 4C-watch | AI memory rally는 있으나 China restriction, HBM qualification, strike gate 잔존 |
| Hanmi Semiconductor TC bonder | success candidate + rumor 4B | SK Hynix 계약은 Stage 2, Micron rumor +22%는 4B-watch |
| LG Innotek AI iPhone | evidence good but price failed | Q2 OP estimate 106.4B KRW, consensus 대비 +31.2%, 주가 -0.4% |
| LG Display OLED restructuring | Stage 2 candidate | Guangzhou LCD sale $1.54B, OLED capex 1.1T KRW, utilization/FCF gate |
| Rebellions/Sapeon AI chip | Stage 2 insufficient evidence | merger/funding/NPU evidence는 있으나 listed EPS bridge 없음 |
| Samsung/SK OpenAI Stargate | event premium / 4B-watch | SK Hynix +10%, Samsung +3.5%, 900,000 wafer/month LOI headline |
| LG Electronics component cost | 4C-watch | Q4 2025 operating loss 109B KRW, net loss 725.9B KRW, component-cost pressure |

## 산출물

- `data/e2r_case_library/cases_r2_loop14_round284.jsonl`
- `data/sector_taxonomy/round284_r2_loop14_ai_semiconductor_electronics_price_validation_audit.json`
- `output/e2r_round284_r2_loop14_ai_semiconductor_electronics_price_validation/round284_r2_loop14_price_validation_summary.md`
- `output/e2r_round284_r2_loop14_ai_semiconductor_electronics_price_validation/round284_r2_loop14_case_matrix.csv`
- `output/e2r_round284_r2_loop14_ai_semiconductor_electronics_price_validation/round284_r2_loop14_shadow_weights.csv`
- `output/e2r_round284_r2_loop14_ai_semiconductor_electronics_price_validation/round284_r2_loop14_green_gate_review.md`
- `output/e2r_round284_r2_loop14_ai_semiconductor_electronics_price_validation/round284_r2_loop14_stage4b_4c_review.md`

## Green gate 교정

강화해야 할 축:

- actual HBM allocation
- customer delivery/call-off
- HBM ASP/mix margin
- capacity utilization
- equipment PO-to-revenue
- customer diversification
- device sell-through
- component mix margin
- OLED utilization
- labor supply continuity

제한해야 할 패턴:

- AI keyword only
- HBM theme without customer delivery
- LOI/MOU without binding contract
- rumored customer PO
- on-device AI expectation only
- capacity capex without utilization
- unlisted AI chip read-through
- consumer OEM exposed to memory cost
- labor disruption risk

## 4B / 4C 교훈

- `SK Hynix`: 구조 성공이 맞아도 2026년처럼 주가/시총이 과도하게 앞서면 4B-watch가 필요하다.
- `Samsung Electronics`: HBM catch-up rally는 Stage 2가 가능하지만 qualification, China exposure, strike가 hard-watch gate다.
- `Hanmi Semiconductor`: 실제 SK Hynix 계약은 Stage 2, 미확인 Micron 고객 루머는 4B-watch다.
- `OpenAI Stargate`: LOI와 wafer demand headline은 demand signal이지 binding revenue가 아니다.
- `LG Electronics`: AI memory shortage는 memory supplier에는 수혜지만 consumer OEM에는 component-cost pressure가 될 수 있다.

## 검증

실행한 명령:

```bash
PYTHONPATH=src python -m unittest tests.test_round284_r2_loop14_ai_semiconductor_electronics_price_validation -v
PYTHONPATH=src python -m e2r.cli.build_round284_r2_loop14_report
```

라운드 단위 테스트는 통과했다. 전체 테스트는 최종 커밋 전 별도로 실행한다.

## 남은 일

- 이번 팩은 reported price anchor 기반 partial validation이다. 전체 조정 OHLC, 30D/90D/180D/1Y MFE/MAE는 아직 backfill해야 한다.
- 생산 점수 로직에는 반영하지 않았다. 예를 들어 `actual_hbm_allocation +5`는 shadow weight로만 저장됐고, StageClassifier threshold는 바뀌지 않았다.
- 다음 R2 반복에서는 HBM allocation, 고객 delivery/call-off, PO-to-revenue, sell-through, utilization, labor-continuity의 실제 숫자 backfill이 필요하다.
