# Census v4 0701 Latest C15 Source-Backed Replay Patch / Stage Truth

작성 시점: 2026-07-02 KST  
repo: `/home/eorb915/projects/stock_agent`  
canonical output: `output/census_v4/2026-07-01`  
as_of_date: `2026-07-01`

> 최신 수치 주의: 이 문서는 C15 패치 직후 스냅샷이다. C24 source-backed replay 이후 최신값은 `census_v4_0701_stage_existence_c24_patch_cross_review_packet_2026-07-02.md`와 `README.md`를 기준으로 한다. 최신 replay matrix는 `source_backed_ready_count=5`, `guard_replay_ready_count=5`, `missing_required_archetype_count=27`, controlled semantic replay는 `9/10 pass`다. Stage truth 자체는 변하지 않았다. 운영 `FULL_THESIS` row는 여전히 0개다.

## 한 줄 결론

```text
C15 source-backed semantic replay가 닫혔다.
이제 C06, C08, C15 세 아키타입은 source-backed positive + guard replay ready다.

하지만 운영 FULL_THESIS / FULL_E2R_100 Stage row는 여전히 0개다.
```

쉬운 예:

```text
원문 읽기 시험은 32과목 중 3과목이 통과했다.
하지만 전 종목 정식 E2R 100점 채점지는 아직 없다.
```

## 이번 패치로 바뀐 것

### 1. C15 source-backed replay 산출물 추가

새 canonical 산출물:

```text
output/census_v4/2026-07-01/c15_source_backed_semantic_replay.json
```

현재 값:

```text
positive_replay_pass = true
guard_replay_pass = true
accepted_claim_count = 6

positive_accepted_primitive_ids:
  fcf_quality_score
  pricing_power_confirmed
  spread_expansion

guard_accepted_primitive_ids = []
raw_commodity_guard_leaked_primitives = []
blockers = []
replay_only = true
production_score_evidence_allowed = false
```

사용한 source-backed replay URLs:

```text
https://en.yna.co.kr/view/AEN20210427007052320
https://www.posco.co.kr/homepage/servlet/FileDownLoad?fileCategory=irDataFd&fileNum=407
https://www.businesskorea.co.kr/news/articleView.html?idxno=60900
```

해석:

```text
Hyundai Steel / POSCO source excerpt는 제품 판가, 원재료 상승, 영업이익/OPM bridge를 열었다.
Poongsan raw copper-price headline guard는 C15 점수 primitive를 열지 않았다.
```

쉬운 예:

```text
"구리 가격이 올랐다"
  -> 원자재 headline이다.
  -> C15 점수 0, 조사 트리거/guard만 가능.

"제품 판가가 올라 원재료 상승에도 영업이익률이 개선됐다"
  -> issuer-level pass-through / spread / margin bridge다.
  -> C15 positive primitive 가능.
```

### 2. Matrix 집계 수정

`_all_archetype_replay_matrix`가 C15를 완전히 세도록 수정했다.

수정된 항목:

```text
C15 accepted_claim_count 반영
C15 guard_case_count 반영
C15 guard_case_pass_count 반영
C15 source_backed_replay_symbols 반영
```

현재 matrix:

```text
source_backed_ready_count = 3
guard_replay_ready_count = 3
missing_required_archetype_count = 29
```

READY:

```text
C06_HBM_MEMORY_CUSTOMER_CAPACITY
C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
C15_MATERIAL_SPREAD_SUPERCYCLE
```

PENDING priority:

```text
C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
C24_BIO_TRIAL_DATA_EVENT_RISK
C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
```

### 3. Controlled semantic replay 개선

현재 controlled semantic replay:

```text
case_count = 10
pass_count = 7
pending_count = 3
fail_count = 0
controlled_semantic_replay_pass = false
```

새로 PASS가 된 case:

```text
C15_MATERIAL_SPREAD_PASS_THROUGH_RAW_COMMODITY_GUARD
```

아직 pending:

```text
C17_CHEMICAL_SPREAD_REALIZED_MARGIN_BRIDGE_GUARD
C24_CLINICAL_BINARY_EVENT_GUARD
C28_SOFTWARE_SECURITY_RETENTION_BRIDGE_GUARD
```

## 변하지 않은 것

### 운영 Stage truth

```text
census_stage_status rows = 3391

stage_scope:
  CENSUS_EVENT_BOARD = 3391
  FULL_THESIS = 0

score_scope:
  NO_SCORE = 3324
  EVENT_WEIGHTED_PARTIAL = 67
  FULL_E2R_100 = 0

canonical_stage:
  0 = 3306
  1 = 54
  2 = 30
  3-Red = 1

verified_score_present_count = 0
full_e2r_verified_score_count = 0
```

해석:

```text
C15 replay가 닫혔다고 해서 운영 full-thesis Stage가 생긴 것은 아니다.
Stage 라벨은 여전히 Census Event Board 상태판이다.
```

### Goal은 아직 완료가 아니다

`goal_completion_audit.json` blockers:

```text
brain_web_evidence_pass_false
full_thesis_smoke_pending
full_thesis_production_pass_false
source_backed_replay_parity_all_archetypes_pending
controlled_semantic_replay_pending
goal_requirement_matrix_pass_false
```

해석:

```text
C15 하나는 줄었지만 아직 C17/C24/C28 replay와 full thesis production, Brain/Web evidence gate가 남아 있다.
```

## 검증

Targeted tests:

```text
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_all_archetype_replay_matrix \
  tests.test_census_v4_goal_required_audits -v

Ran 10 tests
OK
```

Census v4 tests:

```text
PYTHONPATH=src python -m unittest $(rg --files tests | rg 'tests/test_census_v4_.*\.py$' | sed 's#/#.#g; s#\.py$##') -v

Ran 113 tests
OK
```

Full repo test artifact:

```text
PYTHONPATH=src python -m e2r.cli.run_test_command_with_artifact \
  --artifact output/test_full_repo_0701/full_unittest_result_artifact.json \
  --log output/test_full_repo_0701/full_unittest.log \
  -- python -m unittest discover -s tests -v

status = OK
test_count = 4994
failed_count = 0
error_count = 0
duration_seconds = 175.8148
log_sha256 = 7dc403b409915f97e4429d16309d61cb61ebeae476bebbb8534bd41c4f92ca8f
```

Canonical output 재생성:

```text
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --output-root output/census_v4/2026-07-01 \
  --v3-output-root output/census_v3/2026-07-01 \
  --target-gate anti_fake \
  --test-result-artifact output/test_full_repo_0701/full_unittest_result_artifact.json

ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
```

## 다음 패치 방향

우선순위:

```text
1. C17 source-backed replay
   positive: realized spread / OPM / EPS 또는 FCF bridge
   guard: raw material spread-only 문장을 margin conversion으로 오인하지 않기

2. C24 source-backed replay
   positive: endpoint / regulatory / partner economics / runway bridge
   guard: binary event headline만으로 Green bridge를 열지 않기

3. C28 source-backed replay
   positive: ARR / RPO / renewal / retention / churn bridge
   guard: software/security 키워드만으로 contract retention을 열지 않기

4. FULL_THESIS production runner

5. Real Brain/Web evidence gate
```

## 외부 리뷰어 공격 질문

```text
1. C15 replay는 replay_only=true / production_score_evidence_allowed=false인가?
2. raw commodity headline guard가 spread/pricing/margin/FCF primitive를 열지 않았는가?
3. C15 accepted_claim_count=6이 matrix accepted_claim_count에 반영됐는가?
4. C15 guard_case_count=1, guard_case_pass_count=1이 matrix에 반영됐는가?
5. controlled semantic replay가 6/10 -> 7/10으로 바뀌었는가?
6. 남은 pending이 C17/C24/C28만 맞는가?
7. C15 replay를 운영 Stage나 production score로 오해하게 만드는 출력이 없는가?
```
