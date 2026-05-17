# Checkpoint 28A Round 96 R4 Loop 5 Materials / Spread / Strategic Resources

## 목적

`docs/round/round_96.md`의 R4 Loop 5 내용을 case library / score-profile 설계 자료로 반영했다. 이번 패치는 생산 scoring을 바꾸지 않는다. 목적은 소재·스프레드·전략자원 대섹터에서 “가격 상승”과 “EPS/FCF 체급 변화가 고정되는 구조”를 분리하는 것이다.

쉬운 예시는 이렇다. 구리 가격이 올랐다는 사실은 Stage 1~2 후보 근거가 될 수 있다. 하지만 sulfuric acid 같은 처리비용이 같이 오르거나 관세 재고가 가격을 왜곡했다면 Green 근거가 아니라 RedTeam overlay다. 반대로 희토류가 정부 투자, price floor, offtake, 생산능력, FCF까지 연결되면 제한적으로 Stage 3 후보가 될 수 있다.

## 반영 내용

- 신규 모듈: `src/e2r/sector/round96_r4_loop5_materials_spread_strategic.py`
- 신규 CLI: `src/e2r/cli/build_round96_r4_loop5_report.py`
- 신규 테스트: `tests/test_round96_r4_loop5_materials_spread_strategic.py`
- 신규/확장 archetype:
  - `RARE_EARTH_MAGNET_SUPPLY_CHAIN`
  - `COPPER_PROCESSING_INPUT_COST_OVERLAY`
  - `GOLD_MINER_JURISDICTION_RERATING`
  - `IRON_ORE_CHINA_DEMAND_CYCLE`
  - `DISCLOSURE_CONFIDENCE_CAP`
- 기존 R4 Loop 4의 MP Materials 단일 케이스를 두 경로로 분리:
  - `mp_materials_dod_price_floor_case`
  - `mp_materials_apple_magnet_contract_case`

## 산출물

- `data/e2r_case_library/cases_r4_loop5_round96.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round96_r4_loop5_v5.csv`
- `output/e2r_round96_r4_loop5_materials_spread_strategic/round96_r4_loop5_materials_spread_strategic_summary.md`
- `output/e2r_round96_r4_loop5_materials_spread_strategic/round96_r4_loop5_case_matrix.csv`
- `output/e2r_round96_r4_loop5_materials_spread_strategic/round96_r4_loop5_stage_date_plan.csv`
- `output/e2r_round96_r4_loop5_materials_spread_strategic/round96_r4_loop5_green_guardrails.md`
- `output/e2r_round96_r4_loop5_materials_spread_strategic/round96_r4_loop5_risk_overlays.md`
- `output/e2r_round96_r4_loop5_materials_spread_strategic/round96_r4_loop5_price_validation_plan.md`
- `output/e2r_round96_r4_loop5_materials_spread_strategic/round96_r4_loop5_price_fields.csv`

## 요약 수치

- target_count: 22
- case_candidate_count: 16
- structural_success_count: 0
- success_candidate_count: 5
- cyclical_success_count: 2
- event_premium_count: 4
- overheat_count: 1
- stage4b_case_count: 3
- stage4c_case_count: 4
- green_possible_count: 6
- redteam_first_count: 8
- gate_only_target_count: 4

## 해석

Round 96의 핵심은 R4를 가격 반응만으로 보지 않는 것이다.

- `RARE_METALS_PRICE_FLOOR_OFFTAKE`: 정부투자, price floor, offtake, 생산능력, FCF가 같이 있어야 한다.
- `RARE_EARTH_MAGNET_SUPPLY_CHAIN`: Apple/DoD 같은 고객, 자석 생산, recycled feedstock, 고객 qualification을 raw rare-earth 가격과 분리한다.
- `COPPER_PROCESSING_INPUT_COST_OVERLAY`: AI 전력망 수요가 있어도 처리비용, 광산차질, 관세 재고왜곡이 있으면 Green을 막는다.
- `GOLD_MINER_JURISDICTION_RERATING`: 안전 관할권과 M&A는 후보 근거지만, dilution, integration, AISC, 생산량을 같이 봐야 한다.
- `EVENT_PREMIUM_GOVERNANCE_OVERLAY`: Korea Zinc식 공개매수·경영권 이벤트는 구조적 FCF 리레이팅이 아니라 event premium으로 먼저 분류한다.

## 검증 명령

```bash
PYTHONPATH=src python -m e2r.cli.build_round96_r4_loop5_report
PYTHONPATH=src python -m unittest tests.test_round96_r4_loop5_materials_spread_strategic -v
```

전체 테스트는 커밋 전 최종 검증에서 실행한다.

## Guardrails

- 생산 scoring threshold는 변경하지 않았다.
- case records는 candidate-generation input이 아니다.
- spread, offtake, price floor, 생산능력, FCF, capital return, FID, stage price는 추정하지 않는다.
- 원자재 가격 상승만으로 Stage 3-Green을 만들지 않는다.
- 공개매수, governance event, disclosure gap, commodity price crash는 positive score가 아니라 RedTeam / cap / 4C overlay다.
