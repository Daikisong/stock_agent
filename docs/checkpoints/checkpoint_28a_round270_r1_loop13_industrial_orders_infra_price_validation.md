# Checkpoint 28A Round 270 R1 Loop 13

## 반영 내용

`docs/round/round_270.md`의 R1 Loop 13 산업재·수주·인프라 가격경로 검증 라운드를 calibration-only 팩으로 구조화했다.

추가한 산출물:

- `src/e2r/sector/round270_r1_loop13_industrial_orders_infra_price_validation.py`
- `src/e2r/cli/build_round270_r1_loop13_report.py`
- `tests/test_round270_r1_loop13_industrial_orders_infra_price_validation.py`
- `data/e2r_case_library/cases_r1_loop13_round270.jsonl`
- `data/sector_taxonomy/round270_r1_loop13_industrial_orders_infra_price_validation_audit.json`
- `output/e2r_round270_r1_loop13_industrial_orders_infra_price_validation/`

## 핵심 결론

이번 라운드는 R1에서 자주 나오는 착시를 분리한다.

쉬운 예시:

- `수주 공시`는 Stage 2 후보가 될 수 있지만, 납품·마진·운전자본·현금회수가 확인되기 전에는 Stage 3-Green이 아니다.
- `합병/MASGA/미국 조선협력`은 좋은 테마지만, 실제 U.S. award와 FCF가 없으면 Green이 아니라 4B-watch다.
- `IPO 첫날 +96%`는 사업모델이 좋아도 가격이 증거보다 먼저 간 상태다.

## 추가 케이스

- HD Hyundai Heavy / HD Hyundai Mipo: MASGA·합병 Stage 2 + 4B-watch
- Hanwha Ocean: U.S. Navy MRO option + China sanction 4C-watch
- Samsung Heavy Industries: Zvezda 수주취소 hard 4C
- Hyundai Rotem Morocco ONCF: rail-export mega order Stage 2
- HD Hyundai Marine Solution: marine after-market recurring service 후보지만 IPO overheat
- Rainbow Robotics: Samsung strategic equity option, 실제 로봇 매출 전 Green 금지
- Korea Aerospace Industries: 방산 항공우주 optionality Stage 2 + 4B-watch
- 한국 조선 broad basket: 조선 수주 사이클 cyclical success + 4B-watch

## Green Gate 보정

강화할 축:

- final contract quality
- delivery schedule visibility
- backlog margin quality
- cash collection quality
- counterparty sanction check
- recurring service revenue
- aftermarket margin visibility
- naval MRO contract award
- integration synergy realization
- actual robot order revenue

감점할 축:

- order headline only
- MOU / merger headline only
- IPO pop only
- defense sector rerating only
- strategic equity investment only
- U.S. shipbuilding policy theme only
- counterparty sanction risk
- contract cancellation risk
- geopolitical port-fee risk

## 4B / 4C

4B-watch:

- 조선주가 수주 cycle 뉴스로 하루 +10~16% 급등
- IPO 첫날 +40~100% 상승
- 합병/MASGA headline으로 record high
- 방산주 YTD +50~130% 상승
- 전략 지분투자만으로 로봇주가 리레이팅

hard 4C:

- contract cancellation
- counterparty illegal termination
- sanctioned customer / sanctioned subsidiary
- arbitration / advance-payment dispute
- delivery impossible due war / sanctions

이번 라운드의 hard 4C는 Samsung Heavy Zvezda cancellation이다. Hanwha Ocean China sanctions는 hard 4C가 아니라 강한 4C-watch로 기록했다.

## 안전장치

- production scoring 변경 없음
- candidate generation 입력 아님
- shadow weight only
- full adjusted OHLC가 없는 항목은 `price_data_unavailable_after_deep_search` 또는 reported anchor로만 표시
- 가격, Stage 날짜, MFE/MAE를 임의 생성하지 않음

## 검증

사용 명령:

```bash
PYTHONPATH=src python -m unittest tests.test_round270_r1_loop13_industrial_orders_infra_price_validation -v
PYTHONPATH=src python -m e2r.cli.build_round270_r1_loop13_report
PYTHONPATH=src python -m compileall -q src tests
PYTHONPATH=src python -m unittest discover -s tests -v
git diff --check
```

이 라운드는 투자 권고가 아니라 E2R Stage 상태기계의 보정용 케이스 라이브러리 확장이다.
