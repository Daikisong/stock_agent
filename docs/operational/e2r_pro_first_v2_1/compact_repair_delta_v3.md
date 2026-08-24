# E2R Pro-First V2.1 Compact RepairDeltaV3

P5는 source verifier가 반려한 사실을 고칠 때 전체 `ResearchDossierV3`를 다시 출력시키지
않는 경계다. P4가 로컬 기계 결함을 먼저 제거하므로, P5에는 실제 initial-output 결함 또는
의미/source support 결함인 material candidate만 들어온다.

## 이전 방식과 변경점

```text
이전 V2 repair
반려 fact 1~N개
→ 전체 ResearchDossierV2 재출력
→ 기존 fact/source/question/route까지 다시 echo

V3 compact repair
반려 fact 1~N개
→ 같은 source + 같은 root cause + 같은 question scope로 grouping
→ candidate별 CORRECT|REPLACE|NARROW|WITHDRAW만 출력
→ replacement만 deterministic preflight/source reverify
```

쉬운 예:

```text
원래 candidate: HBM 계약 가격이 25% 상승했다.
실제 fetched source: HBM 계약 가격이 20% 상승했다.

NARROW
→ 20%를 직접 지지하는 atomic replacement fact 1개
→ 기존 accepted fact는 그대로 유지
→ replacement를 source verifier가 다시 확인
```

`fetched_excerpt`는 반려된 Pro 인용문을 되풀이하지 않는다. fetch 원문에 claimed excerpt가
실제로 있으면 그 literal span을 쓰고, 없으면 `source_locator`가 포함된 실제 문장만
deterministically 잘라 넣는다. locator도 없으면 빈 문자열로 남기며 semantic similarity로
문장을 만들지 않는다.

## 출력 schema와 marker

tracked schema:

```text
configs/e2r_pro_repair_delta_v3.schema.json
```

응답은 다음 marker 사이의 JSON 객체 하나다.

```text
E2R_REPAIR_DELTA_JSON_BEGIN
{ e2r_pro_repair_delta_v3 }
E2R_REPAIR_DELTA_JSON_END
```

핵심 roster:

```text
job_id / run_id / research_pass_id / parent_pass_id
target / as_of_date
repair_actions
new_source_documents
new_route_receipts
score_authority=false
stage_authority=false
```

각 action은 compiled packet의 다음 값을 그대로 echo해야 한다.

```text
candidate_id
question_family_ids
rejection_category
original_statement
source_document_id
canonical_url
fetched_excerpt
allowed_action=CORRECT|REPLACE|NARROW|WITHDRAW
```

## grouping과 prompt budget

group key:

```text
source_document_id
+ root cause class
+ sorted question_family_ids
```

같은 공식 문서에서 fact 8개가 반려돼도 full fetched source text는 group에 한 번만 들어간다.
각 candidate에는 original atomic fact와 짧은 literal fetched excerpt만 둔다.

```text
target prompt size  <= 60,000 chars
hard prompt size    <= 100,000 chars
hard 초과           즉시 FAIL
transport batching  성공 처리에 사용하지 않음
```

prompt receipt에는 `full_dossier_reoutput_requested_count=0`을 기록한다.

## Pro에 보낼 수 있는 분류

허용:

```text
INITIAL_PROMPT_OUTPUT_DEFECT
GENUINE_SEMANTIC_OR_SOURCE_DEFECT
```

금지:

```text
LOCAL_NORMALIZABLE
SOURCE_REPRESENTATION_RESOLVABLE
NONMATERIAL_AUXILIARY_REJECTION
```

금지 분류에 `send_to_pro_allowed=true`가 붙으면 compiler가 실행을 거절한다. 즉 로컬에서
tracking URL을 고칠 수 있는데 Pro에 다시 묻는 경로는 없다.

## action 검문

- `CORRECT`, `NARROW`: 기존 source document를 유지하고 replacement fact 1개를 요구한다.
- `REPLACE`: 기존 source 또는 `new_source_documents`에 정확히 선언된 official source 1개를
  참조한다.
- `WITHDRAW`: replacement source/fact를 모두 금지하고 question을 public gap으로 되돌린다.
- 모든 replacement는 새 fact ID, 동일 target·fact kind·question scope, 현재 repair pass ID,
  Initial V3 `verifier_preflight` 계약을 가져야 한다.
- 모든 replacement fact는 현재 pass의 `new_route_receipts` 한 개 이상에 결박돼야 한다.
- packet 밖 candidate/question, score/Stage field, accepted fact 대상 action은 거절한다.

새 source document가 새 lineage ID를 선언하면 독립성을 과대평가하지 않도록 publisher와 URL
host의 deterministic 조합으로 conservative independence group을 만든다. 동일 publisher/host는
같은 group이므로 문서 개수를 독립 증거 개수로 부풀리지 않는다.

## 적용과 재검문

원본 dossier 파일을 덮어쓰지 않고 effective snapshot을 만든다.

```text
validated RepairDeltaV3
→ rejected candidate와 stale derived metric 제거
→ 과거 route의 candidate를 accepted → rejected roster로 이동
→ replacement source/fact/route append 또는 WITHDRAW
→ ResearchDossierV3 전체 graph validation
→ Local Evidence Preflight 재실행
→ deterministic source verifier 재실행
→ question status 복원 또는 pending/public 유지
```

repair 전에 이미 accepted였던 fact는 hash까지 같아야 하고 재검문에서도 accepted 상태를
유지해야 한다. 둘 중 하나라도 깨지면 `operational_ready_allowed=false`다.

fresh efficiency gate는 compact repair를 최대 한 번만 허용한다.

```text
repair_pass_ordinal = 1  허용
repair_pass_ordinal > 1  SECOND_REPAIR_PASS_BLOCKS_OPERATIONAL_READY
```

이는 두 번째 수정이 기술적으로 불가능하다는 뜻이 아니라, 같은 fresh session을 운영 효율
성공으로 포장하지 않는다는 뜻이다. 후속 정책은 P6 fresh-session orchestration에서 새 대화
실패 경계와 연결한다.

## runtime 산출물

`job_root/repair_v3/`에 atomic write한다.

```text
compact_repair_prompt.md
compact_repair_prompt_receipt.json
repair_delta_v3.json
repair_actions.jsonl
reverification_rows.jsonl
research_dossier.repaired.json
compact_repair_receipt.json
```

실제 source 원문과 Pro 응답은 runtime에 남고 Git에는 복제하지 않는다.

## 구현과 테스트

```text
src/e2r/pro_first/repair/models_v3.py
src/e2r/pro_first/repair/prompt_v3.py
src/e2r/pro_first/repair/parser_v3.py
src/e2r/pro_first/repair/delta_v3.py
src/e2r/pro_first/repair/service_v3.py
tests/test_e2r_pro_first_v2_1_compact_repair_v3.py
```

테스트는 marker parser, grouping, local/nonmaterial routing 금지, 100k hard fail,
WITHDRAW/NARROW/REPLACE, accepted fact 보존, question scope 차단, V3 preflight 계약, 새 source
lineage, 실제 preflight→verifier 재검문, 두 번째 repair 차단을 fixture로 검증한다. ChatGPT Pro나
live web search는 호출하지 않는다.

P5 완료는 실제 Pro 전송 완료가 아니다. P6에서 fresh job/pass/conversation identity와 exactly-once
browser transport에 이 compiler/parser/service를 연결해야 한다.
