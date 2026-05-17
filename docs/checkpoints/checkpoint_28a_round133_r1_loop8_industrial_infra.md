# Checkpoint 28A Round 133 R1 Loop 8 Industrial Infrastructure

## 목적

`docs/round/round_133.md`의 R1 Loop 8 내용을 캘리브레이션 팩으로 반영했다.

이번 라운드는 산업재·인프라에서 단순한 수주 증가가 아니라 다음 흐름이 실제로 이어지는지를 분리한다.

```text
계약/백로그/승인 게이트
-> 매출·마진·EPS·FCF 전환
-> 가격 경로 정합성
-> 4B/4C RedTeam 감시
```

쉬운 예로, 변압기 쇼티지 뉴스만 있으면 Stage 1이다. 계약금액·납기·고객·마진이 보이면 Stage 2가 될 수 있고, 그 계약이 OP/EPS/FCF 상향과 가격 경로까지 맞아야 Stage 3 후보가 된다.

## 반영 내용

- `src/e2r/sector/round133_r1_loop8_industrial_infra.py` 추가
- `src/e2r/cli/build_round133_r1_loop8_report.py` 추가
- `tests/test_round133_r1_loop8_industrial_infra.py` 추가
- `E2RArchetype.POWER_EQUIPMENT_BACKLOG_TO_FCF` 추가
- Round 133 전용 case pack과 score profile 생성

## 핵심 변경점

- v8 기본 점수표를 별도 캘리브레이션 자료로 기록
  - EPS/FCF: 25
  - 계약·백로그 visibility: 22
  - 병목·pricing power: 18
  - mispricing: 10
  - valuation room: 7
  - capital discipline/FCF conversion: 10
  - information confidence: 8
- `POWER_EQUIPMENT_BACKLOG_TO_FCF`를 별도 archetype으로 분리
- 신규 반례 추가
  - `siemens_orders_profit_miss_case`: 주문/백로그가 좋아도 매출·이익 미스면 Green 금지
  - `oklo_smr_no_revenue_watch_case`: SMR 규제 milestone만으로는 Stage 3 금지
- score-stage-price alignment 표를 6개에서 9개로 확대
- Stage cap에 `profit_miss`, `FSS correction`, `no revenue SMR`, `PPA/grid approval gate`를 명시

## 산출물

- `data/e2r_case_library/cases_r1_loop8_round133.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round133_r1_loop8_v8.csv`
- `output/e2r_round133_r1_loop8_industrial_infra/round133_r1_loop8_industrial_infra_summary.md`
- `output/e2r_round133_r1_loop8_industrial_infra/round133_r1_loop8_case_matrix.csv`
- `output/e2r_round133_r1_loop8_industrial_infra/round133_r1_loop8_score_stage_price_alignment.md`

## 안전장치

- production scoring은 변경하지 않았다.
- case library는 candidate-generation input이 아니다.
- 종목명 하드코딩으로 Stage를 올리는 로직은 추가하지 않았다.
- 계약금액, 마진, stage price, FCF는 없는 값을 만들지 않는다.

## 검증

```bash
PYTHONPATH=src python -m unittest tests/test_round133_r1_loop8_industrial_infra.py -v
PYTHONPATH=src python -m e2r.cli.build_round133_r1_loop8_report
```

두 명령 모두 통과했다.
