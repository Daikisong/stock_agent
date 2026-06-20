# Parser Target Revision Date Leak Fix

## 결론

삼전/하닉을 보다가 찾은 문제지만 HBM 전용 문제가 아니다.

리포트 parser가 `목표주가 상향` 같은 라벨 뒤 숫자를 찾을 때 줄바꿈을 넘어가면서 다음 줄의 날짜를 목표가 상향률로 잘못 읽었다.

쉬운 예:

- 원문 제목: `삼양식품 1Q24 Review 컨센서스 상회 목표주가 상향`
- 다음 줄: `2024.05.16`
- 잘못된 해석: `target_revision_pct = 2024.05`
- 올바른 해석: 제목에는 숫자가 없으니 건너뛰고, 본문 `목표주가 상향: 45%`를 읽어야 한다.

## 영향 범위

이 문제는 HBM이 아니라 전 섹터 공통 리포트 파싱 문제다.

수정 전 benchmark autopsy에서 `hard_audit_count > 0`인 row는 45/120개였다.

모두 같은 audit code였다.

| audit code | count |
| --- | ---: |
| `target_price_revision_too_high` | 45 |

회사별 분포:

| company | count |
| --- | ---: |
| 효성중공업 | 11 |
| HD현대일렉트릭 | 11 |
| 삼양식품 | 11 |
| 한화에어로스페이스 | 12 |

관측된 잘못된 값 예:

| company | bad field | observed_value |
| --- | --- | ---: |
| 효성중공업 | `target_price_revision_1m` | 2023.05 |
| HD현대일렉트릭 | `target_price_revision_1m` | 2023.07 |
| 삼양식품 | `target_price_revision_1m` | 2024.05 |

즉 "목표가를 2023% 올렸다"처럼 불가능한 값이 들어갔고, parser audit가 Green을 막는 hard finding을 만들었다.

## 코드 수정

수정 파일:

- `src/e2r/research/report_parser.py`
- `tests/test_report_parser.py`

변경 내용:

1. `_number_after()`가 label 뒤 숫자를 찾을 때 줄바꿈을 넘지 못하게 했다.
2. `_target_price_value()`의 fallback target-price 패턴도 줄바꿈을 넘지 못하게 했다.
3. autopsy row에 `audit_finding_codes`, `audit_finding_fields`, `audit_finding_actions`를 추가했다.
4. hard audit 설명이 audit 원인뿐 아니라 Stage2/Stage3 gate 실패도 같이 보여주게 했다.
5. `test_target_revision_label_does_not_leak_next_line_date`와 hard audit autopsy test를 추가했다.

핵심은 `[^0-9\-]*`를 `[^\n0-9\-]*`로 바꾼 것이다.

쉬운 예:

- 이전: `목표주가 상향`을 보고 다음 줄 `2024.05.16`까지 내려가서 `2024.05`를 잡을 수 있었다.
- 이후: 같은 줄에 숫자가 없으면 그 라벨은 실패하고, 다음 라벨을 다시 찾는다.

## 수정 후 재실행 결과

재실행 명령:

```bash
PYTHONPATH=src python -m e2r.cli.analyze_asof_stage_promotion \
  --asof-output output/0619_asof_replay_benchmark_current_2023_2026/2023-01-01_to_2026-05-14 \
  --output-directory output/0619_asof_stage_promotion_benchmark_current_2023_2026 \
  --top-candidates 120 \
  --max-queries-per-candidate 8 \
  --max-results-per-query 10 \
  --report-date 2026-06-19
```

수정 후:

| metric | value |
| --- | ---: |
| analyzed rows | 120 |
| `hard_audit_count > 0` | 0 |
| Stage 3-Green | 0 |
| Stage 3-Yellow | 12 |
| Stage 2 | 34 |
| Stage 1 | 67 |
| Stage 0 | 7 |
| `failed_stage3_total_score` | 120 |
| `failed_stage3_bottleneck` | 120 |
| `failed_stage3_visibility` | 87 |

## 점수 변화

가짜 audit가 제거되면서 일부 non-HBM 사례 점수가 올라갔다.

| company | before best score | after best score | after stage | 주요 남은 실패 |
| --- | ---: | ---: | --- | --- |
| 효성중공업 | 68.6325 | 71.7472 | Stage2 | total, visibility, bottleneck, contract_quality |
| HD현대일렉트릭 | 66.3585 | 72.9633 | Stage2 | total, bottleneck, contract_quality |
| 삼양식품 | 57.0212 | 62.5526 | Stage1 | Stage2 total, domain evidence, sector bottleneck |
| 한화에어로스페이스 | 29.4010 | 35.6473 | Stage1 | EPS/FCF, info, total, bottleneck |

삼전/하닉의 핵심 score gap은 거의 그대로다.

| company | best row | stage | score | 남은 실패 |
| --- | --- | --- | ---: | --- |
| SK하이닉스 | 2024-05-01 | 3-Yellow | 76.7639 | total, bottleneck |
| 삼성전자 | 2024-04-01 | Stage2 | 68.6752 | total, visibility, bottleneck |

## 해석

이번 패치는 잘못 잠긴 audit 자물쇠를 푼 것이다.

하지만 Green 0개 문제의 본체는 아직 남아 있다. 모든 row가 여전히 `failed_stage3_total_score`와 `failed_stage3_bottleneck`에 걸린다.

쉬운 예:

- 잘못된 문제: "목표가 상향률이 2023%라서 위험해 보인다."
- 이번 수정: "그건 날짜를 잘못 읽은 것이니 제거한다."
- 남은 문제: "수주잔고, CAPA 잠김, 고객 lock-in, 마진 전환, revision 같은 연구축이 runtime bottleneck/visibility 점수로 충분히 안 들어간다."

따라서 다음 구현은 HBM 보너스가 아니라 전 아키타입 evidence bridge와 adapter 보강이어야 한다.

## 검증

```bash
PYTHONPATH=src python -m unittest tests.test_report_parser tests.test_report_parser_fixture_fields tests.test_report_consensus_proxy -v
```

결과: 19 tests OK.

추가 검증:

```bash
PYTHONPATH=src python -m unittest tests.test_asof_stage_promotion_autopsy tests.test_report_parser tests.test_report_parser_fixture_fields tests.test_report_consensus_proxy -v
```

결과: 25 tests OK.
