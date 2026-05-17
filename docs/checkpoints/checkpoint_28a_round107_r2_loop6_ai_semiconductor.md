# Checkpoint 28A Round 107 R2 Loop 6 AI / Semiconductor / Electronics

## 요약

Round 107은 AI·반도체·전자부품을 하나의 `AI 수혜`로 보지 않고, 실제 EPS/FCF 체급 변화를 만드는 경제 구조별로 나눈 calibration pack이다.

간단한 예:

- SK하이닉스 HBM은 `MEMORY_HBM_CAPACITY`와 `MEMORY_HBM_LTA_PREPAYMENT` 축으로 본다.
- 삼성전자 HBM4 출하는 `HBM_CATCHUP_EXECUTION`이다. 출하만으로 Green이 아니라 qualification, yield, volume이 필요하다.
- Broadcom custom ASIC은 `CUSTOM_AI_ASIC_HYPERSCALER`다. HBM처럼 보지 않고 고객집중, TSMC capacity, custom-chip margin을 따로 본다.
- CoreWeave식 supplier/customer/investor overlap은 `CIRCULAR_AI_FINANCING_OVERLAY`로 RedTeam gate다.

## 반영 내용

- `MEMORY_HBM_LTA_PREPAYMENT` 추가
- `MEMORY_SUPPLY_REALLOCATION` 추가
- `CUSTOM_AI_ASIC_HYPERSCALER` 추가
- `CUSTOM_AI_ASIC_MARGIN_CONCENTRATION` 추가
- Round 107 전용 case pack, score profile, report CLI 추가
- Round 107 price-field plan에 HBM LTA/선수금, custom ASIC, memory reallocation 필드 추가
- 생산 scoring/staging/red-team 로직은 변경하지 않음

## 산출물

- `src/e2r/sector/round107_r2_loop6_ai_semiconductor.py`
- `src/e2r/cli/build_round107_r2_loop6_report.py`
- `tests/test_round107_r2_loop6_ai_semiconductor.py`
- `data/e2r_case_library/cases_r2_loop6_round107.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round107_r2_loop6_v6.csv`
- `output/e2r_round107_r2_loop6_ai_semiconductor/`

## 결과 수치

- target_count: 26
- case_candidate_count: 24
- structural_success_count: 1
- success_candidate_count: 13
- event_premium_count: 1
- overheat_count: 2
- failed_rerating_count: 2
- stage4b_case_count: 5
- stage4c_case_count: 1
- green_possible_count: 6
- watch_yellow_first_count: 15
- redteam_first_count: 5
- hard_gate_target_count: 3

## Guardrail

- 이 pack은 calibration/evaluation 자료이며 candidate-generation input이 아니다.
- v6 weight는 아직 production scoring에 적용하지 않는다.
- HBM LTA, custom ASIC, AI server ODM, neocloud, theme-only AI chip을 같은 증거로 취급하지 않는다.
- 계약금액, 고객명, duration, prepayment, yield, margin, stage price, FCF를 invent하지 않는다.
- price-only AI CAPEX crowding은 Green 증거가 아니라 4B overlay다.

## 검증

실행:

```bash
PYTHONPATH=src python -m unittest tests.test_round107_r2_loop6_ai_semiconductor -v
PYTHONPATH=src python -m e2r.cli.build_round107_r2_loop6_report
```

결과:

- Round 107 단위 테스트 통과
- Round 107 JSONL/CSV/Markdown 보고서 생성 완료

