# Checkpoint 28A Round 68: R2 Loop 3 AI / Semiconductor / Electronics

## 목적

Round 68은 R2 AI·반도체·전자부품 섹터를 Loop 3 기준으로 다시 좁힌 작업이다.

핵심은 단순하다.

```text
AI 수혜
≠ Green

HBM, 범용 메모리, 장비, 패키징, 광통신, 서버 ODM,
네오클라우드, 냉각, AI칩 pure-play는 서로 다른 경제구조다.
EPS/FCF와 가격경로가 같이 맞은 축만 Green 후보가 될 수 있다.
```

예를 들어 HBM은 구조적 Green 후보가 될 수 있다. 하지만 이미 시장이 대부분 인정한 SK하이닉스형 가격경로는 동시에 `4B-watch`로 봐야 한다. 반대로 CoreWeave형 네오클라우드는 대형 계약이 있어도 고부채, FCF 적자, GPU 감가상각, 고객집중이 해결되기 전까지 Green이 아니다.

## 반영 내용

- 추가 canonical archetype
  - `AI_CAPEX_CROWDING_OVERLAY`
- 추가 모듈
  - `src/e2r/sector/round68_r2_loop3_ai_semiconductor.py`
  - `src/e2r/cli/build_round68_r2_loop3_report.py`
  - `tests/test_round68_r2_loop3_ai_semiconductor.py`
- 생성 산출물
  - `data/e2r_case_library/cases_r2_loop3_round68.jsonl`
  - `data/sector_taxonomy/score_weight_profiles_round68_r2_loop3_v3.csv`
  - `output/e2r_round68_r2_loop3_ai_semiconductor/round68_r2_loop3_ai_semiconductor_summary.md`
  - `output/e2r_round68_r2_loop3_ai_semiconductor/round68_r2_loop3_case_matrix.csv`
  - `output/e2r_round68_r2_loop3_ai_semiconductor/round68_r2_loop3_stage_date_plan.csv`
  - `output/e2r_round68_r2_loop3_ai_semiconductor/round68_r2_loop3_green_guardrails.md`
  - `output/e2r_round68_r2_loop3_ai_semiconductor/round68_r2_loop3_risk_overlays.md`
  - `output/e2r_round68_r2_loop3_ai_semiconductor/round68_r2_loop3_price_validation_plan.md`
  - `output/e2r_round68_r2_loop3_ai_semiconductor/round68_r2_loop3_price_fields.csv`

## 요약

- target: 17개
- case candidate: 15개
- structural success: 1개
- success candidate: 7개
- overheat: 2개
- failed rerating: 2개
- Stage 4B marker 포함: 3개
- Stage 4C thesis break: 1개
- Green possible: 4개
- Watch/Yellow first: 11개
- RedTeam first: 2개
- hard gate target: 1개

## Loop 3 핵심 변경

1. `MEMORY_HBM_CAPACITY`는 Green 후보로 유지하되, valuation credit을 낮추고 `customer_price_resistance`, `capacity_normalization`, `AI CAPEX slowdown`을 4B/4C 감시축으로 추가했다.
2. `COMMODITY_MEMORY_GENERAL_SEMI`는 Kioxia형 AI storage 수요를 반영해 EPS/FCF credit을 높였지만, NAND/DRAM cycle reversal과 supply rebound를 강하게 남겼다.
3. `OPTICAL_NETWORKING_AI_DATACENTER`는 Broadcom형 lead time 병목을 반영해 bottleneck/pricing을 강화했다.
4. `AI_SERVER_ODM_EMS_SUPPLY_CHAIN`은 매출 성장은 인정하지만, 저마진·consignment·재고·고객집중·회계 리스크 때문에 Green을 쉽게 주지 않는다.
5. `NEOCLOUD_GPU_RENTAL`은 OpenAI형 대형 계약 visibility를 인정하되, debt/FCF/GPU depreciation/customer concentration을 Green 차단 조건으로 둔다.
6. `REDTEAM_ACCOUNTING_TRUST_OVERLAY`는 hard gate로 유지했다. Supermicro식 auditor resignation, filing delay, internal control 문제는 AI 매출 성장보다 우선한다.
7. `AI_CAPEX_CROWDING_OVERLAY`를 추가했다. 이건 긍정 점수가 아니라 4B/4C 감시용 overlay다.

## 검증

실행한 명령:

```bash
PYTHONPATH=src python -m unittest tests.test_round68_r2_loop3_ai_semiconductor -v
PYTHONPATH=src python -m e2r.cli.build_round68_r2_loop3_report
```

결과:

- Round 68 전용 테스트 12개 통과
- Round 68 리포트 생성 성공
- production scoring/staging/red-team 모듈은 Round 68 case pack을 import하지 않음

## 주의

- production scoring threshold는 바꾸지 않았다.
- case record는 candidate generation input이 아니다.
- HBM yield, 고객명, 계약금액, stage price, 마진, FCF는 확인된 값만 써야 한다.
- API key 또는 민감정보는 산출물에 쓰지 않았다.
- 투자 권고 문구는 추가하지 않았다.
