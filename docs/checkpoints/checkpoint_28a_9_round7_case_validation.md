# Checkpoint 28A-9: Round 7 Case Validation

## Summary

Round 7 was applied as calibration/report material only. Production scoring and
StageClassifier thresholds were not changed.

Round 7 adds stricter success/counterexample rules:

```text
high score + price rerating + EPS/FCF confirmation + no fast 4C
= success validation candidate

price up without EPS/FCF
= theme/event/cycle counterexample
```

쉬운 예시:

```text
플랫폼 기업의 MAU가 늘어도 ARPU, OPM, FCF가 안 따라오면 Stage 3-Green 근거가 아니다.
```

## Implemented Files

- `src/e2r/sector/round7_case_validation_framework.py`
- `src/e2r/cli/build_round7_case_validation_report.py`
- `tests/test_round7_case_validation_framework.py`
- `docs/e2r_case_validation_round7.md`
- `output/e2r_round7_case_validation/round7_case_validation_framework.md`
- `output/e2r_round7_case_validation/round7_success_counterexample_rules.md`
- `output/e2r_round7_case_validation/round7_archetype_validation_matrix.csv`
- `output/e2r_round7_case_validation/round7_case_validation_gap_report.md`
- `output/e2r_round7_case_validation/round7_next_backfill_plan.md`

## Archetype Postures

- `GREEN_ELIGIBLE_AFTER_VALIDATION`: 성공/반례와 price path가 채워진 뒤 shadow scoring 후보
- `WATCH_YELLOW_DEFAULT`: 기본은 Watch/Yellow, Green은 반복성/FCF 검증 후
- `REDTEAM_GUARDRAIL`: RedTeam과 4B/4C 방어가 우선

## Round 7 Additions

- Platform/Software는 ARPU, take-rate, OPM, FCF를 요구한다.
- Game/IP는 신작 기대와 반복 monetization을 분리한다.
- Travel/Leisure는 reopening rebound와 구조적 rerating을 분리한다.
- Construction/Credit은 수주보다 PF/유동성/cash flow를 먼저 본다.
- CDMO는 pre-revenue biotech과 분리해 장기 생산계약과 가동률을 본다.
- Holding/Financial/Rare Metals는 event premium과 true rerating을 분리한다.

## Current Output

The current case pack still has many records requiring price-path validation.
That is expected. Round 7’s purpose is to make those gaps visible before score
weights are changed.

## What Not To Change

- Do not lower Stage 3-Green thresholds.
- Do not use case records as production candidate-generation input.
- Do not treat price-only rallies as EPS/FCF evidence.
- Do not apply score weights until case validation coverage is filled.

## Verification

Commands run:

```bash
PYTHONPATH=src python -m unittest tests.test_round7_case_validation_framework -v
PYTHONPATH=src python -m e2r.cli.build_round7_case_validation_report --cases data/e2r_case_library/cases_v02.jsonl --output-directory output/e2r_round7_case_validation
```

Full test run was executed after the patch before commit.
