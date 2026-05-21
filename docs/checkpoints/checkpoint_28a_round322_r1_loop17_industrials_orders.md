# Checkpoint 28A Round 322: R1 Loop 17 Industrials / Orders / Infrastructure

## 목적

Round 322는 산업재·수주·인프라 대섹터의 trigger-level price validation 라운드다.

이번 라운드는 전력기기, 조선, 방산형 산업재, 원전/SMR 장비, 대형 EPC, 수주 취소를 한 묶음으로 보되, 생산 점수나 StageClassifier는 바꾸지 않았다. 케이스 라이브러리와 트리거 보정 자료만 추가했다.

쉬운 예시로, `HD Hyundai Heavy / Mipo` 합병은 발표 당일 가격 반응이 강해서 Stage2-Actionable 근거가 된다. 하지만 실제 미국 수주, 작업 배분, 합병 후 마진이 확인되기 전에는 Stage3-Green이 아니다.

## 반영 내용

- source round: `docs/round/round_322.md`
- analyst round id: `round_250`
- loop: `R1 Loop 17`
- large sector: `INDUSTRIALS_ORDERS_INFRASTRUCTURE`
- method: `trigger_level_backtest_v1_after_redteam`
- 생산 점수 변경: 없음
- 후보 생성 입력 사용: 없음
- shadow weight only: 예
- full adjusted OHLC 완료: 아니오

추가 또는 확장한 canonical archetype:

- `SHIPBUILDING_MASGA_MERGER_STAGE2_ACTIONABLE`
- `SHIPBUILDING_NAVAL_EXPORT_STAGE2_WITH_SANCTION_4B`
- `DEFENSE_INDUSTRIAL_EXPORT_STAGE2_YELLOW`
- `GRID_EQUIPMENT_AI_POWER_STAGE2_PROMOTE`
- `GRID_EQUIPMENT_US_CAPACITY_STAGE2_WITH_PRICE_FAILED`
- `TRANSFORMER_CAPACITY_EXPANSION_STAGE2_NO_PRICE`
- `NUCLEAR_SMR_INDUSTRIAL_SUPPLY_STAGE2_WITH_FINAL_CONTRACT_GATE`
- `SHIPBUILDING_ORDER_CANCELLATION_4C`

## 케이스 요약

- `HD Hyundai Heavy / HD Hyundai Mipo`: MASGA와 미국 조선 협력 맥락의 합병. +11.3% / +14.6%와 record-high context가 있어 가장 깨끗한 Stage2-Actionable이다. 실제 미국 수주와 post-merger margin은 아직 gate다.
- `Hanwha Ocean`: 미국 해군 frigate optionality에는 +6% 반응이 있었지만, 중국 제재에는 -5.8% 반응이 있었다. Stage2 naval optionality + geopolitical 4B로 둔다.
- `Hyundai Rotem`: K2 Poland 수출 기대에 +9.3%, 이후 180대 규모 반복 계약과 현지생산 footprint가 있다. Stage3-Yellow 후보지만 delivery margin과 기술이전 비용이 gate다.
- `HD Hyundai Electric`: AI/data-center 전력 수요가 전력기기로 확장되며 +333% broad move가 보고됐다. 너무 보수적으로 두면 missed structural이 될 수 있으나, backlog/margin/ASP 확인 전에는 Green이 아니다.
- `LS Electric`: 목표가 상향과 미국 매출비중 확대 전망은 좋지만, 당일 주가가 -5.4%였다. `evidence_good_but_price_failed`다.
- `Hyosung Heavy / Hyosung HICO`: 미국 GSU 수요 +274%, lead time 143주, Memphis $157M 증설은 Stage2 capacity evidence다. 직접 가격, orderbook, margin이 없다.
- `Doosan Enerbility`: X-energy/AWS/Fermi America와 연결된 SMR/AI power supply-chain Stage2다. MOU/협력은 최종 장비 수주가 아니다.
- `Samsung Heavy`: Zvezda icebreaker 4.85조원 / $3.54B 수주 취소는 backlog quality를 깨는 4C thesis break다.

## Stage 보정

Stage2-Actionable 승격 후보는 다음 신호를 본다.

- reported event return +5% 이상
- market-relative return +5%p 이상
- contract/deal/order value가 명확함
- 수주가 매출 또는 수주잔고로 연결됨
- 반복 수주 또는 신규 시장 진입이 있음
- 생산능력/현지화가 고객 수요와 직접 연결됨
- sanction, cancellation, MOU-only, margin unknown 4B가 식별되어 있음

Stage3-Green은 여전히 엄격하다.

- 계약 또는 수주가 최종 상태임
- 수주잔고가 이익 있는 매출로 전환됨
- 생산능력과 가동률이 보임
- 마진과 현금전환이 확인됨
- 제재, 취소, MOU-only, 법적 리스크가 해결됨
- full-window MFE/MAE가 확보되고 우호적임

## 산출물

- `data/e2r_case_library/cases_r1_loop17_round250.jsonl`
- `data/e2r_trigger_calibration/triggers_r1_loop17_round250.jsonl`
- `data/sector_taxonomy/round322_r1_loop17_industrials_orders_audit.json`
- `data/sector_taxonomy/score_weight_profiles_round250_r1_loop17_v1.csv`
- `output/e2r_round322_r1_loop17_industrials_orders_infrastructure/`

## 검증

실행한 명령:

```bash
PYTHONPATH=src python -m unittest tests.test_round322_r1_loop17_industrials_orders_infrastructure -v
PYTHONPATH=src python -m e2r.cli.build_round322_r1_loop17_report
```

결과:

- Round322 전용 테스트 통과
- 케이스 JSONL, 트리거 JSONL, 감사 JSON, shadow weight CSV 생성 완료
- Stage2-Actionable candidate count: `3`
- Stage3-Yellow candidate count: `4`
- Stage3-Green confirmed: `0`
- strong 4C case count: `1`

## 다음 작업

다음 순서는 `R2 Loop 17`이다. 이번 R1에서 만든 규칙은 AI/반도체/전자부품으로 넘어갈 때도 유용하다. 예를 들어 “AI 인프라 수혜”라는 말만으로 Green을 주면 안 되고, 실제 수주, 가격 검증, capacity utilization, margin gate가 닫히는지를 봐야 한다.
