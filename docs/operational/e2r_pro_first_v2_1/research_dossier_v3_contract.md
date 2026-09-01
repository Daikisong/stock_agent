# ResearchDossierV3 검증 계약

## 목적

V3는 source 문서와 atomic fact를 분리한다. old V2처럼 fact마다 URL·publisher·날짜를
반복하지 않는다.

쉬운 예:

```text
같은 반기보고서
├─ FACT-REVENUE  매출 atomic predicate + exact quote A
├─ FACT-CFO      영업현금흐름 atomic predicate + exact quote B
└─ FACT-CAPEX    현금 CAPEX atomic predicate + exact quote C

DERIVED-FCF = FACT-CFO - FACT-CAPEX
```

반기보고서의 URL·publisher·publication date·lineage는 `SourceDocumentV3` 한 곳에만
둔다. 계산된 FCF는 원문 quote fact처럼 꾸미지 않고 `DerivedMetricV3`에 둔다.

## 고정 불변식

각 atomic fact는 다음을 모두 만족해야 한다.

```text
one atomic predicate
one source_document_id
one exact supporting_excerpt
one target/subject scope
one or more question_family_ids
terminal lifecycle (UNKNOWN 금지)
verifier_preflight 9 true + derived_mixed false
```

JSON Schema뿐 아니라 deterministic graph validator가 다음을 추가 검사한다.

- canonical source URL 중복·tracking parameter·fragment 금지
- publication/availability/event date의 `as_of_date` 초과 금지
- collection과 `fact_kind` 불일치 금지
- source/predicate/subject/excerpt가 모두 같은 중복 atomic fact 금지
- fact가 모르는 source document·question·research pass를 참조하는 것 금지
- derived metric이 모르는 input fact를 참조하는 것 금지
- lineage의 document/fact roster가 실제 graph와 다른 것 금지
- Pro dossier와 derived metric의 score/Stage authority 금지

## V2 호환 경계

V1/V2 schema와 validator는 삭제하거나 V3로 덮어쓰지 않았다. 기존 artifact는 기존
version으로 계속 검증한다. 새 fresh production job만 V3를 사용하도록 전환하는 작업은
후속 fresh-session orchestration 단계에서 수행한다.

```text
old V1/V2 artifact  → read/verify compatibility 유지
fresh job output    → e2r_pro_research_dossier_v3
```

V3 parser는 원문 evidence를 고치지 않는다. transport가 아직 알 수 없던 최초
`conversation_id`와 durable pass receipt만 capture 뒤 결박할 수 있고, fact·quote·source
document는 그대로 보존한다.

## Pending 허용

provider 자체가 실패한 경우 빈 evidence graph를 `PROVIDER_PENDING`으로 보존할 수 있다.
이는 0점 확정이 아니다. 반대로 fact가 하나라도 있으면 source document와 lineage가 반드시
존재해야 한다.

## 구현 위치

```text
configs/e2r_pro_research_dossier_v3.schema.json
src/e2r/pro_first/dossier/v3.py
src/e2r/pro_first/dossier/validator.py
tests/test_e2r_pro_first_v3_dossier.py
```
