# E2R Pro-First V2.1 Local Evidence Preflight

이 문서는 `ResearchDossierV3`를 deterministic source verifier에 넣기 전에 수행하는 P4
기계 검문을 설명한다. 이 단계의 목적은 자료를 다시 조사하는 것이 아니라, 코드가 고칠 수
있는 표현 차이 때문에 같은 자료를 Pro에 반복해서 보내는 일을 없애는 것이다.

## 실행 순서

```text
ResearchDossierV3
→ V3 field/schema 사전 정규화
→ URL canonicalization
→ 원문 및 동일 lineage의 공식 대체 표현 fetch
→ text/quote literal normalization
→ issuer·publisher alias 정규화
→ segment/product closed-enum mapping
→ published/availability/Last-Modified 날짜 판정
→ atomic fact projection 및 preflight
→ 기존 deterministic source verifier
→ 모든 반려의 root-cause 분류
```

`ProDossierImporter`는 엄격한 V3 validator보다 먼저 명시적 alias와 기계적 표현만
정규화한다. `ProSourceVerificationService`는 source verifier보다 먼저 전체 preflight를
실행하고, preflight가 이미 가져온 문서를 verifier가 재사용하게 한다. V3 dossier를
preflight 없이 `ProSourceVerifier`에 직접 넣으면 실행이 거절된다.

쉬운 예:

```text
Pro 출력 URL
https://example.com/report/?utm_source=chatgpt#page-3

로컬 canonical URL
https://example.com/report
```

이 차이는 기업 사실의 의미와 무관하므로 Pro에 새 질문을 보내지 않는다. 반대로 URL의 모든
공식 표현을 열었는데도 인용문이 글자 그대로 존재하지 않으면 로컬 정규화로 사실을 꾸미지
않고 의미/source 결함으로 남긴다.

## canonical dossier와 verifier projection

P4는 두 형태를 의도적으로 분리한다.

```text
research_dossier.preflight.json
└─ canonical ResearchDossierV3
   ├─ SourceDocumentV3가 URL/제목/발행자/날짜를 소유
   └─ AtomicFactV3는 source_document_id만 참조

verifier_projection.json
└─ 기존 verifier용 일회성 투영
   └─ fact에 source_url/title/publisher/date를 복사해 호환
```

따라서 verifier 호환 필드가 다시 V3 canonical fact의 중복 source 소유권으로 굳어지지
않는다. 점수와 Stage 권한은 두 형태 모두 갖지 않는다.

## 코드가 자동으로 해결하는 범위

다음은 deterministic local operation이며 검색·ChatGPT Pro repair를 호출하지 않는다.

- `utm_*`, fragment, 기본 port, query 순서, trailing slash 정규화
- redirect가 돌려준 final URL 사용
- CRLF/HTML entity/Unicode quote·dash·공백 정규화
- 주체 alias와 주입된 known publisher alias 정규화
- V2/V3 field alias와 source/lineage identity alias 결박
- contract에서 읽은 segment/product closed enum mapping
- 확인된 published date를 HTTP `Last-Modified`보다 우선
- canonical/opened URL 및 같은 lineage·발행자·target의 공식 대체 표현 사용
- 구조화된 각 atomic part에 독립 literal quote span이 있을 때만 compound fact split

quote 검문은 다음 literal 순서만 허용한다.

```text
transport-normalized exact
→ Unicode/whitespace/punctuation-normalized exact
→ locator로 제한한 exact
→ 동일 official lineage의 alternate representation exact
```

semantic similarity만으로는 절대 `ACCEPTED_*`가 되지 않는다. 예를 들어 “매출이 크게
증가했다”와 “revenue rose 31%”가 의미상 비슷해도 literal anchor가 없으면 이 단계가 임의로
통과시키지 않는다.

## 반려 분류와 Pro 전송 경계

| root cause | 처리 | Pro repair |
|---|---|---|
| `LOCAL_NORMALIZABLE` | 로컬 수정 후 재검문 | 금지 |
| `SOURCE_REPRESENTATION_RESOLVABLE` | 동일 공식 표현/로컬 parser로 해결 후 재검문 | 금지 |
| `INITIAL_PROMPT_OUTPUT_DEFECT` | 현재 run의 compact semantic repair 후보 + generic prompt 결함 기록 | P5 계약에서만 허용 |
| `GENUINE_SEMANTIC_OR_SOURCE_DEFECT` | 실제 의미·source 결함으로 보존 | P5 compact repair 허용 |
| `NONMATERIAL_AUXILIARY_REJECTION` | 진단에만 기록 | 금지 |

모든 verifier rejection은 한 분류를 가져야 한다. receipt의 다음 값은 항상 감사한다.

```text
local_normalizable_sent_to_pro_count = 0
source_representation_sent_to_pro_count = 0
unclassified_rejection_count = 0
query_count = 0
search_count = 0
```

P4는 분류까지만 구현한다. 실제 Pro repair payload와 전송은 P5 범위다.

## 영속 산출물과 해시 결박

job runtime의 `verification/preflight/`에 다음 파일을 atomic write한다.

```text
research_dossier.preflight.json
verifier_projection.json
preflight_operations.jsonl
preflight_issues.jsonl
preflight_receipt.json
```

verification 단계에는 다음이 추가된다.

```text
verification/rejection_classifications.jsonl
source_verification_receipt.json의 preflight receipt hash와 root-cause counts
verification_hash의 preflight receipt hash와 classification rows
```

원문 page body와 runtime dossier는 Git에 넣지 않는다. Git에는 코드, 테스트, 이 설명만 두며
실제 실행 산출물은 기존 job runtime 경계를 따른다.

## 구현 위치

```text
src/e2r/pro_first/preflight/
├── canonical_url.py
├── text_normalizer.py
├── issuer_alias.py
├── scope_mapper.py
├── date_resolver.py
├── source_representation.py
├── atomic_fact.py
├── rejection_classifier.py
├── models.py
└── service.py
```

핵심 회귀 테스트는
`tests/test_e2r_pro_first_v2_1_local_preflight.py`에 있다. tracking URL, CRLF/HTML/Unicode,
Last-Modified precedence, alias와 enum, redirect, 동일 lineage 대체 표현, nonissuer alias,
V3 preflight 우회 차단, literal-only quote, compound split, rejection routing과 durable lifecycle
integration을 fixture로 검증한다. fixture fetch만 쓰므로 Pro provider나 새 web search는 호출하지
않는다.

## P4 완료 경계

P4 완료는 “새 Pro 조사 완료”가 아니다. 다음만 뜻한다.

```text
V3 → local preflight → verifier 순서가 강제됨
기계적 결함은 로컬에서 닫힘
의미/source 결함만 다음 compact repair 후보가 됨
모든 결정과 변환이 receipt/hash로 재현 가능함
```

fresh ChatGPT conversation 생성과 실제 000660/C17/C28 전송은 각각 P6 이후 범위다.
