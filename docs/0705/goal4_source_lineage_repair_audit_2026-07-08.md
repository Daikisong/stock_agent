# Goal4 Source Lineage Repair Audit - 2026-07-08

작성 시점: 2026-07-08 KST

이 문서는 Goal4 진행 중 추가한 source-lineage repair audit의 목적, 결과, 다음 작업을 기록한다.

## 결론

Goal4는 아직 완료가 아니다.

이번 작업은 다음 질문에 답하기 위한 전수 감사다.

```text
문장/claim 후보는 있었는데
source route 또는 original lineage 문제 때문에
accepted claim이 되지 못한 사례가 얼마나 있는가?
```

쉬운 예:

```text
더존비즈온 리포트에서 "ARR 성장" 문장을 찾았다.
그런데 URL이 검증된 증권사 원본 리포트로 인정되지 않으면
점수창구는 "그냥 웹검색 결과라서 점수 근거 불가"로 반려한다.
```

이 audit은 그런 반려를 전수로 모은다. 단, 이 row들은 점수 근거가 아니다. 다음 runtime attempt에서 다시 source anchor, direct target, current temporal, accepted primitive mapping을 통과해야 한다.

## 새 산출물

생성 파일:

```text
docs/operational/source_lineage_repair_audit_2026-07-05.json
docs/operational/source_lineage_repair_audit_2026-07-05.md
docs/operational/source_lineage_repair_audit.json
```

코드:

```text
src/e2r/census/source_lineage_repair_audit.py
```

연결:

```text
write_research_to_runtime_parity_artifacts()
→ write_source_lineage_repair_audit()
```

즉 Goal4 parity artifact를 다시 만들면 source-lineage repair audit도 같이 생성된다.

## 전수 집계 결과

기준 output root:

```text
output/census_v4/2026-07-05-research-to-runtime-parity-self-repair-01-20260707T130702Z
```

요약:

```text
raw_assertion_rejection_count = 2502
lineage_rejection_count = 524
route_only_candidate_count = 29
current_code_verified_retry_candidate_count = 50
```

의미:

```text
lineage_rejection_count:
source route/original lineage 계열 이유가 포함된 rejected claim 후보

route_only_candidate_count:
semantic, target, temporal, primitive mapping은 통과했고
source route 쪽만 막힌 후보

current_code_verified_retry_candidate_count:
이번 broker report route 패치 후 현재 코드로는
verified report original 후보로 재시도할 가치가 있는 row
```

## C28 판단

C28 더존비즈온은 이번 패치의 직접 수혜 후보다.

```text
C28 lineage_rejection_count = 26
C28 route_only_candidate_count = 4
C28 current_code_verified_retry_candidate_count = 26
domains = bbn.kiwoom.com, securities.miraeasset.com
```

해석:

```text
키움/미래에셋 리포트 route에서 버려진 C28 후보가 있고,
그중 일부는 route-only candidate다.
```

쉬운 예:

```text
채점 답안지는 거의 작성됐는데
"이 서류가 원본 리포트인지 확인 안 됨" 도장 때문에 탈락한 케이스가 있다.
```

따라서 다음 runtime attempt에서는 C28을 우선 재시도해야 한다. 단, 과거 rejected row를 바로 점수로 쓰면 안 된다. 새 attempt에서 accepted Evidence OS claim이 생성되어야 한다.

## C08 판단

C08 리노공업도 broker report route 후보가 있다.

```text
C08 lineage_rejection_count = 23
C08 route_only_candidate_count = 1
C08 current_code_verified_retry_candidate_count = 14
domains = eugenefn.com, dart.fss.or.kr, valueline.co.kr
```

하지만 C08은 C28보다 조심해야 한다.

많은 sample에 다음이 같이 붙어 있다.

```text
semantic_rejected
target_scope_not_allowed
primitive_mapping_rejected
```

쉬운 예:

```text
서류 접수창구 문제도 있지만,
서류 안의 문장이 "리노공업 고객 품질/qualification/repeat order"를
직접 말하는지부터 다시 확인해야 한다.
```

즉 C08은 source route만 고쳐서는 충분하지 않을 수 있다. LLM planner가 customer-quality primitive에 직접 맞는 문서/문단을 다시 찾아야 한다.

## 전체 아키타입 의미

상위 source class:

```text
BrokerReportPublicPDF = 395
CompanyNewsroom = 49
TrustedNews = 49
CompanyGuide = 31
```

이 숫자는 Goal4의 남은 작업이 단순 C28 하나가 아니라는 뜻이다.

```text
증권사 리포트 원본 route
회사 newsroom/IR 원본 route
trusted news 원본 route
CompanyGuide/공식 데이터 route
```

를 각 아키타입 primitive에 맞게 계속 수리해야 한다.

## 안전 원칙

이번 audit은 다음을 보장한다.

```text
1. rejected row는 점수 근거가 아니다.
2. source_proxy_only/evidence_url_pending은 여전히 점수 금지다.
3. current_code_verified_retry_candidate는 "재시도 후보"일 뿐이다.
4. 새 runtime attempt에서 accepted claim이 생기기 전까지 full thesis pass로 세면 안 된다.
5. C28 재시도 성공 여부와 C08 semantic/primitive 문제를 분리해서 봐야 한다.
```

## 다음 작업

우선순위:

```text
1. C28 next runtime attempt를 bounded로 재실행해
   bbn.kiwoom.com / securities.miraeasset.com route가
   실제 accepted claim으로 닫히는지 확인한다.

2. C08은 source route retry와 별도로
   customer_quality / qualification / repeat_order primitive에 맞는
   직접 문장 추출 실패를 분해한다.

3. route_only_candidate_count가 있는 다른 아키타입도
   next attempt planner feedback에 우선순위로 반영한다.

4. Goal4 완료 선언은 여전히 금지한다.
   현재 최종 상태는 MEANINGFUL_RUNTIME_PARITY_NOT_READY다.
```
