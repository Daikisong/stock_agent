# Checkpoint 28A Round 218 R1 Loop 9 Industrial Infra Price Validation

## 목적

`docs/round/round_218.md`의 산업재·수주·인프라 가격경로 검증 내용을 case-library 형식으로 반영했다. 이번 패치는 production scoring을 바꾸지 않는다. 예를 들어 HD현대마린솔루션이 상장 첫날 크게 올랐다는 사실은 가격경로로 기록하지만, 반복 MRO 매출·마진·FCF가 확인되지 않았으므로 Stage 3-Green 증거로 쓰지 않는다.

## 반영 파일

- `src/e2r/sector/round218_r1_loop9_industrial_infra_price_validation.py`
- `src/e2r/cli/build_round218_r1_loop9_report.py`
- `tests/test_round218_r1_loop9_industrial_infra_price_validation.py`
- `data/e2r_case_library/cases_r1_loop9_round218.jsonl`
- `data/sector_taxonomy/round218_r1_loop9_industrial_infra_price_validation_audit.json`
- `output/e2r_round218_r1_loop9_industrial_infra_price_validation/*`

## 케이스 요약

| case | 판정 | 핵심 |
|---|---|---|
| LS ELECTRIC | Stage 2 watch | 미국 grid exposure와 목표가 상향은 좋지만 보도 시점 가격 -5.4%라 `evidence_good_but_price_failed` |
| HD현대일렉트릭/효성중공업 | Stage 2 sector evidence | transformer 수요 +274%/+116%, 가격 +80%, lead time 4년. 회사별 order/margin/FCF 전 Green 보류 |
| 삼성E&A | Stage 2 aligned | Fadhili $6B 계약과 +8.5% 가격반응은 Stage 2 근거. EPC margin/cash collection 전 Green 보류 |
| 두산에너빌리티 | policy-to-contract Stage 2 | 체코 원전 preferred bidder에서 계약까지 일부 검증. 장비 backlog/margin 전 Green 보류 |
| HD현대중공업/HD현대미포 | 4B-watch | MASGA·합병 이벤트로 +11.3%/+14.6% 신고가. funded order 전 event premium |
| 한화오션 | 4C-watch | 중국 제재 당일 -5.8%, 장중 -8% 이상. 실제 매출·수주 차질 전 hard 4C는 아님 |
| HD현대마린솔루션 | overheat / event premium | IPO 83,400원에서 163,900원, +96.5%. 운영 증거 전 Stage 3 금지 |

## Green Gate

Round 218의 Green 필수 조건은 다음처럼 강화했다.

- 계약금액, 고객, 납기 확인
- 실제 납품 또는 매출 인식 확인
- 마진, 원가통제, 현금회수 확인
- 수주잔고가 매출·EPS·FCF로 내려오는 경로 확인
- 가격경로가 증거 이후 따라오는지 확인
- 지정학, 자금조달, 희석, 제재 리스크 통과

금지 패턴도 명시했다. 정책/MOU/합병 뉴스, IPO 첫날 급등, 수주 headline만 있는 경우, EPC 원가율 미확인, 조선정책 신고가, 제재 리스크 무시는 Green 근거가 아니다.

## 생성 산출물

- `round218_r1_loop9_price_validation_summary.md`
- `round218_r1_loop9_case_matrix.csv`
- `round218_r1_loop9_target_aliases.csv`
- `round218_r1_loop9_score_adjustments.csv`
- `round218_r1_loop9_shadow_weights.csv`
- `round218_r1_loop9_price_validation_fields.csv`
- `round218_r1_loop9_green_gate_review.md`
- `round218_r1_loop9_price_validation_plan.md`
- `round218_r1_loop9_stage4b_4c_review.md`

## 검증

실행한 명령:

```bash
PYTHONPATH=src python -m unittest tests.test_round218_r1_loop9_industrial_infra_price_validation -v
PYTHONPATH=src python -m compileall -q src/e2r/sector/archetypes.py src/e2r/sector/round218_r1_loop9_industrial_infra_price_validation.py src/e2r/cli/build_round218_r1_loop9_report.py tests/test_round218_r1_loop9_industrial_infra_price_validation.py
PYTHONPATH=src python -m e2r.cli.build_round218_r1_loop9_report
```

결과:

- Round 218 전용 테스트 12개 통과
- case record 7개 생성 및 schema validate 통과
- production scoring 변경 없음
- candidate generation input 아님
- full OHLC는 아직 미완성, reported price anchor 기반 partial validation

## 다음 작업

Round 218은 “전력기기·원전·EPC·조선정책은 Stage 2와 4B가 자주 겹친다”는 점을 case library에 남겼다. 다음 라운드에서는 full OHLC backfill이 되면 MFE/MAE를 더 정밀하게 채우고, shadow weight가 실제 Stage promotion autopsy에서 어떤 후보를 과대/과소평가하는지 비교해야 한다.
