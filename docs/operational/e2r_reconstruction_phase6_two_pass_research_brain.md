# E2R Reconstruction Phase 6 — Two-Pass LLM Research Brain

## 판정

`TWO_PASS_PLANNER_PHASE_CONTRACT_PASS`

이 판정은 blind Pass A와 balanced-memory Pass B, deterministic validator, provider pending 전환이 Phase 6 계약을 만족한다는 뜻이다. 실제 provider의 Pass B 완료와 production daily 연결은 아직 통과하지 않았으므로 `production_runtime_ready=false`다.

## 왜 두 번 생각하게 하는가

한 번에 archetype을 고르게 하면 과거 정답이나 익숙한 종목 이름을 보고 답을 베낄 위험이 있다. 새 planner는 다음처럼 역할을 분리한다.

| 순서 | LLM이 보는 것 | LLM이 하는 일 | 보지 못하는 것 |
|---|---|---|---|
| Pass A | 대상 identity, `as_of_date`, current facts | 경제적 메커니즘 가설 생성 | sector context, `source_primary`, archetype label, score, Stage, 과거 outcome |
| Pass B | Pass A 결과, current facts, balanced memory, reviewed recipe | canonical 후보를 비판하고 반증·질문·source-task 초안 생성 | score/Stage 결정권, 미래 데이터 |
| deterministic validator | 두 pass의 구조화 출력 | 사실 ID, target/sector, recipe, budget, leakage 검증 | 새 query나 투자 판단 창작 |

쉬운 예:

- 현재 사실: “대상 회사의 HBM CAPA가 고객 배정으로 잠겼고 ASP가 상승했다.”
- Pass A: “고객 배정과 가격 상승이 함께 나타나는 구조적 공급 제약일 수 있다.”
- Pass B: positive case만 보지 않고 “취소 가능 물량인가, 선수금·장기계약·RPO가 있는가, 경쟁사 물량을 대상 회사 사실로 잘못 읽지 않았는가”를 함께 묻는다.
- 마지막 score와 Stage는 여전히 deterministic scorer가 계산한다. LLM은 이를 쓰거나 바꾸지 못한다.

## Pass A blind 경계

`compile_blind_hypothesis_input`은 허용 필드만 새 schema로 복사한다. 원본 row에 `source_primary`, expected archetype, score, Stage가 있어도 해당 필드는 전달하지 않는다. 미래 날짜, MFE/MAE 같은 outcome, canonical archetype token이 섞인 텍스트도 제거하거나 row를 제외한다. sector context는 input provenance에는 보존하지만 Pass A prompt에는 넣지 않고 deterministic plausibility 검사에만 쓴다.

예: `as_of_date=2025-01-01`일 때 `observed_date=2025-01-02`인 리포트는 Pass A에 들어가지 않는다. “나중에 실제로 급등했다”는 사실을 1월 1일 가설 생성에 쓰지 않는다는 뜻이다.

Pass A 출력은 최대 5개 mechanism hypothesis이며, 각각 다음을 가져야 한다.

- contiguous rank
- 현재 fact ID로 연결된 supporting/contradicting facts
- mechanism summary와 strength
- must-verify questions
- 불충분할 때 명시적 abstention과 사유

## Pass B balanced critique

Pass B memory는 Phase 5 graph에서 다음 여섯 역할을 균형 있게 받는다.

- direct recipe
- positive case
- counterexample/guard
- source success
- source failure
- wrong-subject semantic guard

단순히 “비슷한 성공 사례”만 주지 않는다. 예를 들어 수주 headline이 있어도 대상 회사 직접성, 계약 lifecycle, 취소·supersession, 실제 매출 전환을 확인하도록 counter thesis와 red-team question을 함께 만든다.

Pass B의 non-abstaining 결과에는 leading archetype의 reviewed recipe와 bounded official-first source-task draft가 필요하다. 공식 source보다 Naver를 먼저 두거나 `max_fetches`를 무제한으로 내면 validator가 결과를 거절한다.

## deterministic validator

코드는 다음을 강제로 검증한다.

- JSON exact key와 실제 타입: 문자열 `"false"`를 boolean `false`로 자동 변환하지 않는다.
- score/Stage/final classification 필드와 문구 차단
- `source_primary` 복사와 historical outcome token 차단
- canonical taxonomy 밖 ID와 balanced retrieval에 없던 ID 차단
- current fact에 없는 supporting ID 차단
- peer-only 또는 stale fact만으로 non-abstaining 대상 가설 확정 차단
- explicit sector와 leading archetype이 맞지 않으면 차단
- leading recipe가 없으면 abstention 요구
- official-first 순서와 positive bounded budget 요구
- guard/hard-break recipe에는 do-not-promote reason 요구

쉬운 예: 경쟁사 B의 증설 기사만 있는데 대상 A의 사실처럼 C06을 확정하면 `PlannerPending`이다. 반대로 “경쟁사 기사라 대상 직접성이 부족하다”고 abstain하면 허용된다.

## provider 실패와 hash

provider 미설정, CLI timeout, provider rejection, schema/decoder rejection은 낮은 점수나 Stage 0 점수로 바꾸지 않는다. 결과는 `PlannerPending`이며 실패한 pass, reason, provider 이름, prompt hash와 response hash를 보존한다.

provider가 응답을 반환한 뒤 validator에서 탈락했다면 오류문 해시가 아니라 실제 반환된 raw response 해시를 남긴다. 응답 자체가 없었던 timeout만 명시적 “response unavailable” provenance를 해시한다.

프로젝트 `.env`는 기존 process environment의 빈 값만 채우고, `E2R_CODEX_PLANNER_*` 설정으로 공용 Codex transport를 만든다. 기존 V4 planner도 같은 process/JSON transport를 사용하되 기존 public behavior와 test patch point는 유지한다.

## blind benchmark

Phase 5와 같은 61개 raw-evidence benchmark를 사용했다. expected archetype과 primitive는 evaluator에만 있고 provider prompt에는 넣지 않았다.

| 지표 | 결과 | 기준 |
|---|---:|---:|
| archetype 평가 분모 | 60 | outcome-derived R13 1개 제외 |
| blind top-3 | 60/60 = 100% | 95% 이상 |
| blind top-1 | 57/60 = 95% | 85% 이상 |
| ambiguity abstention | 27 | 지원 필요 |
| critical guard case | 5 | 관찰 |
| critical guard misroute | 0 | 0 |
| impossible assignment | 0 | 0 |
| score/Stage mutation | 0 | 0 |
| source-primary copy | 0 | 0 |
| prompt/response hash 누락 | 0 | 0 |

이 benchmark provider는 fixture다. 따라서 orchestration과 validator 계약만 증명하며 실제 LLM 성능이나 production readiness를 증명하지 않는다.

## real provider smoke의 정직한 상태

실제 Codex provider smoke에서 Pass A real completion은 확인했다. Pass B는 한 번은 supporting-current-fact 계약 위반으로 deterministic validator가 거절했고, 강화된 schema로 재시도했을 때는 CLI timeout으로 끝났다. 두 경우 모두 `MEMORY_CRITIQUE`의 `PlannerPending`으로 남았다.

즉, 실패를 정상 점수로 위장하지 않는 안전 경로는 확인했지만 real Pass B 성공은 아직 확인하지 못했다. 이 smoke에 production acceptance credit을 주지 않는다. Phase 13 production cutover 전에 real provider 성공과 runtime 연결을 별도로 통과해야 한다.

## 검증 결과

- Phase 0~6 compiler/planner targeted chain: 102개 통과
- 기존 V4 operational/provider regression: 95개 통과
- full suite: 5,409개 실행, 18개 실패
- Phase 0 baseline의 알려진 실패: 동일한 18개
- Phase 6 때문에 새로 생긴 실패: 0개

18개는 mutable goal4 research-to-runtime 운영 snapshot의 현재 값과 과거 기대값 불일치다. Phase 5 full suite에서도 같은 18개가 기준선으로 기록되었다. 따라서 이를 숨겨 “전체 통과”라고 부르지는 않지만 Phase 6 회귀로도 세지 않는다.

## 주요 파일

- `planning/two_pass_brain_planner.py`: two-pass orchestration, prompts, decoder, validator, pending
- `planning/provider_transport.py`: 공용 structured Codex CLI transport
- `planning/two_pass_benchmark.py`: evaluator-only blind benchmark
- `intelligence_schema.py`: planner input/output/pending provenance schema
- `tests/test_two_pass_brain_planner.py`: leakage, routing, abstention, 타입, target/sector, hash, `.env` 검증

## 다음 경계

현재 source-task는 Phase 6의 draft다. accepted predicate, entity/value/time scope, counter question, rejection condition, exhaustion 의미를 완전한 실행 계약으로 만드는 작업은 Phase 7 `QuestionSourceTask`에서 수행한다.
