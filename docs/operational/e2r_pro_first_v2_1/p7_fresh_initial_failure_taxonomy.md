# P7 첫 fresh initial 실패 분류와 수정 장부

> 후속 상태(2026-08-26): 이 문서는 1차 conversation의 diagnostic taxonomy로 보존한다. 해당 job은
> `old_job_frozen_at=2026-08-25T00:13:07.514455Z`와
> `superseded_by_fresh_job_id=PROJOB-ab48ce7e94097cf9b6846602`로 봉인됐다. generic 수정 뒤 완전히 새
> conversation에서 실행한 2차 C06은 initial material `16/18=88.8889%`로 Gate를 통과했다. 성공
> 증거는 `p7_c06_fresh_initial_success_receipt.json`과 `implementation_progress.md`의 P7 최종 절을
> 따른다. 이 후속 성공은 아래 1차 실패 artifact를 덮어쓰거나 재분류하지 않는다.

기준 문서는 `e2r_pro_first_v2_1_fresh_session_verifier_ready_master_goal.md`의 13~14절이다.
첫 fresh conversation의 initial acceptance가 80% 미만이므로 같은 conversation을 repair로 길게
끌지 않고 diagnostic-only로 봉인했다.

## 판정 요약

```text
target / as_of_date       000660 / 2026-08-23
archetype                 C06 + 공통 R13 guards
initial submit            1
mandatory questions       28/28
material candidates       0
accepted                  0
acceptance                0.0%
gate                      OPERATIONAL_EFFICIENCY_GATE_FAILED
score / Stage             생성하지 않음
next action               generic patch 뒤 새 conversation blind rerun
```

## F01 — 최종 DossierV3 직렬화 누락

분류: `INITIAL_PROMPT_OUTPUT_DEFECT / CRITICAL`

관측:

- 화면 보고서는 조사 결론, 질문별 상태, counter, gap, self-audit를 포함했다.
- 보고서 스스로 최종 JSON 직렬화를 완료하지 못했다고 명시했다.
- `E2R_RESEARCH_DOSSIER_JSON_BEGIN/END`가 없고 MD attachment도 없었다.
- 한 source lineage의 exact excerpt 총량이 내부 인용 한도를 한 단어 넘었다는 이유로 dossier 전체를
  보류했다.

영향:

- fact별 exact excerpt–source URL–question binding을 검증할 수 없다.
- 설명을 그대로 material fact로 승격하면 LLM-only 추론이 점수 재료가 되므로 금지해야 한다.
- initial candidate가 0이 되어 80% gate 이전에 `NO_INITIAL_MATERIAL_CANDIDATES`가 발생한다.

generic 수정:

- Initial Prompt V3에 JSON 직렬화 우선 규칙을 추가했다.
- self-audit 불합격 시 dossier 전체를 버리지 않고 해당 fact만 gap으로 내리게 했다.
- 응답 길이가 부족하면 Markdown과 fact 수를 줄이되 mandatory question roster와 유효한 JSON을
  남기게 했다.
- 도구 종료 위험이 있으면 검증 완료 fact와 명시적 gap을 담은 dossier를 먼저 출력하게 했다.
- 36개 canonical prompt snapshot을 모두 재생성했다.

금지한 우회:

- 000660/C06 전용 검색어나 답안 추가
- exact excerpt 없는 서술을 사실로 간주
- acceptance threshold 완화
- 같은 conversation에서 repair로 80% 만들기

## F02 — 화면 citation의 URL이 innerText에서 사라짐

분류: `SOURCE_REPRESENTATION_RESOLVABLE / TRANSPORT`

관측:

- visible report에는 citation pill이 있었지만 `inner_text()`에는 실제 href가 남지 않았다.
- raw report를 훼손하지 않고 assistant turn의 visible `a[href]` 3개를 별도 registry로 붙였다.

수정:

- `E2R_VISIBLE_CITATION_REGISTRY_BEGIN/END` transport normalization을 추가했다.
- raw report와 normalized report의 hash를 모두 보존했다.
- 이 registry는 citation을 새로 만드는 기능이 아니라 이미 화면에 보이는 href를 보존하는 기능이다.

## F03 — readable report는 있는데 dossier marker가 없음

분류: `TRANSPORT_RECOVERY`

관측:

- exact job/run marker, citation, 안정된 report hash는 있었지만 dossier marker가 없었다.
- 기존 adapter는 이런 완료 결과를 캡처하지 못했다.

수정:

- 세 번 동일 hash로 관측된 terminal readable report만 `RESULT_DETECTED`로 인정한다.
- 자동 재전송은 금지한다.
- capture는 exact marker/hash를 다시 검사한다.
- Codex structurer는 보고서 안의 claim/excerpt/URL만 representation으로 옮길 수 있고 browse, fetch,
  score, Stage 권한이 없다.

## F04 — fact 0개에서 mechanism mapper 예외

분류: `LOCAL_VERIFIER_CONTROL_FLOW`

관측:

- 구조적으로 유효하지만 material fact가 0개인 dossier가
  `mechanism scope mapping requires facts and contracts`로 중단됐다.

수정:

- 빈 fact roster에서는 mapper/provider를 호출하지 않는다.
- candidate/accepted/compiled/fetch/query/search가 모두 0인 source verification receipt를 남긴다.
- 이후 efficiency gate가 정책에 따라 FAIL을 결정한다.

쉬운 예: 시험 답안이 0개면 채점기는 “0개 제출” 영수증을 만들고 불합격 처리해야지, 채점기 자체가
예외로 죽으면 안 된다.

## F05 — post-capture 재개가 브라우저를 다시 열려고 함

분류: `RECOVERY_PHASE_CONFUSION`

관측:

- `USER_ATTENTION_REQUIRED`가 browser와 downstream verifier에서 공용으로 쓰인다.
- capture_count=1인 verifier 오류도 pre-capture 오류로 오인할 수 있었다.

수정:

- `USER_ATTENTION_REQUIRED && capture_count=0`일 때만 browser result recovery를 허용한다.
- capture_count=1이면 immutable capture/import에서 verification만 재개한다.
- live 재개에서 upload/composer/send는 모두 0이었다.

## F06 — 완료된 import를 재실행하며 idempotency 충돌

분류: `POST_IMPORT_IDEMPOTENCY`

관측:

- verifier 오류 뒤 재개 코드가 이미 완료된 dossier import를 다시 수행했다.
- DB commit 전 canonical receipt 파일의 `imported_at`만 바뀐 상태에서 idempotency conflict가 났다.

수정:

- dossier_id와 durable import ledger가 있으면 `USER_ATTENTION_REQUIRED`에서도 기존 import를 재사용한다.
- normalized dossier hash와 모든 evidence-bearing receipt field가 동일하고 `imported_at`만 다를 때만
  DB ledger의 canonical timestamp로 복구한다.
- 다른 필드가 다르면 자동 복구하지 않고 계속 fail-closed한다.

## 보존한 Pro 결과

Pro 서술을 버리거나 0점 처리하지 않았다. 다음 항목을 diagnostic dossier에 보존했다.

- mandatory question result 28개
- Pro가 보고한 material/source/route 수 28/18/122
- explicit unresolved gap 11개
- C06 positive/partial/counter 판단
- parser pending: 반기 cash flow 본문, 고객집중도, 반기 검토보고서
- provider pending: multi-provider revision, positioning/crowding
- likely nonpublic: 고객별 qualification, HBM 세대 mix, HBM ASP/margin, yield/throughput 등

다만 exact excerpt와 URL이 atomic fact 단위로 묶이지 않았으므로 score evidence로 승격하지 않았다.
후속 fresh run은 이 답안을 packet에 복사하지 않고, 수정된 generic prompt만 사용해 독립 조사한다.

## 불변 조건

```text
old answer leakage             0
first conversation submit      1
automatic resubmit             false
source verifier fetch          0
new query/search               0/0
score authority                false
Stage authority                false
publication withheld           true
same conversation continuation forbidden
```

## 다음 PASS 조건

새 conversation에서 다음을 모두 다시 증명해야 한다.

```text
mandatory question coverage                100%
material candidate count                   > 0
post-preflight verifier acceptance         >= 80%
local/source-representation defect to Pro  0
genuine semantic repair                    max(5, candidates의 10%) 이하
score/Stage authority                      false/false
```
