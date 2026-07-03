# Census Mode v3 Forensic Review

작성일: 2026-07-01

근거:

- `docs/0701/README.md`
- `docs/0701/census_v3_stage_map_audit_2026-07-01.md`
- `output/census_v3/2026-07-01`
- 구현 커밋 `c5bc76a`
- report-only 커밋 `baaf2e72c3c0861969f5144691cfea0db6e4ffe5`

## 결론

Census v3는 유용한 **anti-fake full-universe status board**다.

하지만 아직 **meaningful operational Stage map**은 아니다.

쉬운 예:

```text
v3가 잘한 것:
전 종목 출석부를 만들고, 채점지 없는 학생에게 점수를 주지 않았다.

v3가 아직 못한 것:
그 채점지가 full thesis 시험지인지, 단일 이벤트 쪽지시험인지 명확히 구분하지 못했다.
```

## 핵심 수치

`output/census_v3/2026-07-01` 기준:

```text
eligible_symbol_count: 3391
non-Stage0 count: 85
claim/score/StageCourt trace rows: 74
Stage2-Watch: 37
Red: 1
Stage3-Green/Yellow: 0
4A/4B/4C: 0
```

## 대표 문제

### 1. Stage/score/trace 원자성 깨짐

삼부토건 `001470`:

```text
final row:
  base_stage = Stage2-Watch
  score = 4.4

linked stagecourt trace:
  base_stage = 1
  score_interval = 4.0 ~ 4.0
```

쉬운 예:

```text
성적표에는 4.4점이라고 쓰고,
첨부 채점지는 4.0점짜리를 붙인 상태다.
```

SK하이닉스 `000660`:

```text
final row score_interval_lower = 4.0
linked stagecourt trace score_interval.lower = 3.2
```

### 2. score 의미 혼동

`verified_score=4.0` 또는 `4.4`는 full E2R 100점 점수가 아니다.

삼성전자 `005930`:

```text
Stage1 / 4.0
근거: 2026-06-24 DART 풍문또는보도에대한해명(미확정)
```

이건 HBM/C06 full thesis 평가가 아니다.

SK하이닉스 `000660`:

```text
Stage1 / 4.0
근거: 유상증자/증권신고서 DART 이벤트
```

이것도 HBM full thesis 평가가 아니다.

### 3. Stage2-Watch 의미 혼동

현재 `Stage2-Watch`는 높은 점수의 Stage2라는 뜻이 아니다.

대부분은 다음 뜻에 가깝다.

```text
직접 공식 공시 기반 material watch primitive가 있음.
하지만 cash/revision/repeat evidence family는 아직 없음.
```

실측:

```text
Stage2-Watch 37개 중 36개 = PENDING_MATERIAL_GAPS
```

### 4. semantic primitive noise

`contract_quality` 안에 다음이 섞일 수 있다.

```text
자기주식취득신탁계약
주식담보제공계약
유상증자/지분증권
풍문 해명/관리성 공시
```

이들은 고객 수주/매출 가시성 계약과 다르다.

## v3 라벨 재해석

v3의 `FULL_UNIVERSE_STAGE_MAP_PASS`는 운영상 다음처럼 읽어야 한다.

```text
PROVISIONAL_REPORT_PASS
또는
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
```

다음으로 읽으면 안 된다.

```text
MEANINGFUL_OPERATIONAL_STAGE_PASS
READY_FOR_FULL_THESIS_OPERATION
```

## v4 P0 요구사항

1. `AtomicStageDecision` 도입
2. `verified_score` deprecate 또는 `FULL_E2R_100`일 때만 허용
3. `event_evidence_score`, `raw_contribution_score`, `full_e2r_verified_score` 분리
4. `stage_signal`, `risk_stage_signal`, `stage_decision_status` 분리
5. `PENDING_MATERIAL_GAPS`를 `COMPLETE`로 표시하지 않기
6. semantic primitive guard 도입
7. 삼성전자/하이닉스 daily DART event와 HBM full thesis refresh 분리
8. Brain/Web/Naver를 실행하지 않았다면 실행했다고 말하지 않기

## 최종 판정

v3는 폐기할 것이 아니라 v4의 입력/반면교사로 재사용한다.

단, v3 산출물을 그대로 운영 확정 Stage 지도라고 부르는 것은 금지한다.
