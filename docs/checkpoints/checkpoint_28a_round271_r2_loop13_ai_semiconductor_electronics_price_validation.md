# Checkpoint 28A Round 271 R2 Loop 13

## 반영 내용

`docs/round/round_271.md`의 R2 Loop 13 AI·반도체·전자부품 가격경로 검증 라운드를 calibration-only 팩으로 구조화했다.

추가한 산출물:

- `src/e2r/sector/round271_r2_loop13_ai_semiconductor_electronics_price_validation.py`
- `src/e2r/cli/build_round271_r2_loop13_report.py`
- `tests/test_round271_r2_loop13_ai_semiconductor_electronics_price_validation.py`
- `data/e2r_case_library/cases_r2_loop13_round271.jsonl`
- `data/sector_taxonomy/round271_r2_loop13_ai_semiconductor_electronics_price_validation_audit.json`
- `output/e2r_round271_r2_loop13_ai_semiconductor_electronics_price_validation/`

## 핵심 결론

이번 라운드는 R2에서 자주 나오는 착시를 분리한다.

쉬운 예시:

- `HBM`이라는 단어만으로는 Stage 3-Green이 아니다. 고객 인증, 양산, shipment, margin, FCF가 필요하다.
- `Nvidia Blackwell 칩을 산다`는 AI infra Stage 2일 수 있지만, 한국 상장사의 EPS 증가 증거는 아니다.
- `IPO 600배 청약`은 흥행 신호지만 납품·마진 증거가 아니므로 4B-watch로 본다.

## 추가 케이스

- SK Hynix: HBM structural success benchmark, 현재는 4B-watch
- Samsung Electronics: memory recovery Stage 2 + HBM lag / China curbs / labor 4C-watch
- Hanwha Precision Machinery carve-out: HBM equipment Stage 2, confirmation sell-the-news
- Rebellions / Sapeon: 비상장 AI chip merger Stage 2, listed revenue bridge 전 Green 금지
- TeraView KOSDAQ IPO: semiconductor inspection Stage 2 + IPO overheat
- Korea state-private foundry policy: policy relief, operator/utilization 전 Green 금지
- Nvidia Blackwell Korea supply: AI infra Stage 2, capex ROI 전 EPS 증거 아님
- China fab export-control basket: hard 4C는 아니지만 persistent 4C-watch

## Green Gate 보정

강화할 축:

- HBM volume certification
- customer qualification
- mass production readiness
- equipment order backlog
- delivered order book
- gross margin visibility
- OP revision quality
- labor operational resilience
- China fab export-control clearance
- capex ROI bridge

감점할 축:

- AI chip keyword only
- policy foundry headline only
- IPO oversubscription only
- strategic equity or unlisted merger only
- equipment carve-out without orders
- capex consumption without EPS
- HBM rumor without customer qualification
- China fab exposure
- labor strike unresolved

## 4B / 4C

4B-watch:

- HBM/AI memory로 1년 3~5배 상승
- $1T market-cap milestone headline
- IPO oversubscription 100x~600x
- P/E 40x+ before listed delivery record
- spin-off rumor +15% 후 confirmation sell-the-news
- Nvidia infra / AI chip merger headline로 revenue 전 basket rally

4C-watch / hard gate 후보:

- HBM qualification failure
- customer shipment delay
- China fab equipment license denial
- export-control escalation
- labor strike causing production halt
- foundry utilization failure

이번 라운드에서는 hard 4C를 확정하지 않았다. Samsung HBM lag/labor risk와 China fab export-control은 강한 4C-watch로 기록했다.

## 안전장치

- production scoring 변경 없음
- candidate generation 입력 아님
- shadow weight only
- full adjusted OHLC가 없는 항목은 reported anchor 또는 `price_data_unavailable_after_deep_search`로 표시
- 가격, Stage 날짜, MFE/MAE를 임의 생성하지 않음

## 검증

사용 명령:

```bash
PYTHONPATH=src python -m unittest tests.test_round271_r2_loop13_ai_semiconductor_electronics_price_validation -v
PYTHONPATH=src python -m e2r.cli.build_round271_r2_loop13_report
PYTHONPATH=src python -m compileall -q src tests
PYTHONPATH=src python -m unittest discover -s tests -v
git diff --check
```

이 라운드는 투자 권고가 아니라 E2R Stage 상태기계의 보정용 케이스 라이브러리 확장이다.
