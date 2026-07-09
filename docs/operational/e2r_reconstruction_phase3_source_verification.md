# E2R Reconstruction Phase 3 — Case-Level Source Verification

## 판정

`CASE_LEVEL_SOURCE_VERIFICATION_COMPILER_PASS`

이 라벨은 source verifier의 조건과 방어선이 통과했다는 뜻이다. 전체 과거 corpus의 source repair가 끝났다는 뜻은 아니다. 현재 full registry 결과의 `historical_replay_ready_count`는 의도적으로 0이며, `production_runtime_ready=false`다.

## 왜 필요한가

URL이 있다는 것과 case가 검증됐다는 것은 다르다.

쉬운 예:

- 나쁜 승격: POSCO case에 현대제철 기사 URL이 있으니 A2라고 표시
- 새 판정: 기사 snapshot의 대상은 `004020 현대제철`이고 POSCO는 `005490`이므로 `URL_FETCHED_WRONG_SUBJECT`
- 날짜 위반: case as-of가 2021-04-26인데 기사는 2021-04-27이면 `URL_FETCHED_DATE_INVALID`
- URL만 존재: 본문 snapshot과 hash가 없으면 `URL_PRESENT_UNVERIFIED`

## canonical source state

다음 열 개 상태를 유지한다.

1. `SOURCE_PROXY_ONLY`
2. `EVIDENCE_URL_PENDING`
3. `URL_PRESENT_UNVERIFIED`
4. `URL_FETCH_FAILED`
5. `URL_FETCHED_NO_ANCHOR`
6. `URL_FETCHED_WRONG_SUBJECT`
7. `URL_FETCHED_DATE_INVALID`
8. `URL_FETCHED_ANCHORED`
9. `URL_FETCHED_ANCHORED_CASE_MATCH`
10. `HISTORICAL_REPLAY_READY`

마지막 상태는 다음 검사가 모두 true일 때만 가능하다.

- case-level URL 또는 official document id 연결
- fetched content 또는 valid provider snapshot
- 실제 파일 SHA-256 일치
- published date와 available date 존재
- 두 날짜 모두 historical case as-of 이하
- 대상 회사/종목 directness
- snapshot 안에 실제 존재하는 exact quote/table/API locator
- 검증 provenance hash가 있는 case/source semantic link
- case summary와 source가 일치
- historical replay와 current score의 완전한 분리

하나라도 빠지면 blocker와 repair task를 남긴다.

## 두 종류의 실행 결과

### 1. Full registry, provider snapshot 미등록

Phase 2의 10,920개 case를 전부 통과시켰지만 snapshot registry는 주지 않았다.

| 항목 | 결과 |
|---|---:|
| verification | 14,201 |
| historical replay ready | 0 |
| source repair task | 10,920 |
| SOURCE_PROXY_ONLY | 5,044 |
| EVIDENCE_URL_PENDING | 112 |
| URL_PRESENT_UNVERIFIED | 9,045 |

이 결과가 중요한 이유는 URL 9,045건을 A2로 과장하지 않았다는 데 있다. 예를 들어 URL 문자열만 있는 case는 “본문을 가져오고 hash와 anchor를 확인하라”는 repair task가 된다.

### 2. Controlled historical snapshot golden

기존 저장소의 현대제철 2021-04-27 historical replay excerpt를 실제 SHA-256으로 다시 계산했다.

- source URL: Yonhap historical article
- content SHA-256: `93021bbf3942eb46673eef23497ac0469c188f1dfd273145cb19e2da874b96db`
- exact anchor: 제품 가격 인상이 강한 수요와 함께 분기 이익을 개선했다는 기사 문장
- published/available date: 2021-04-27
- case as-of: 2021-04-27
- target: `004020 Hyundai Steel`
- current score eligible: false

이 한 건만 `HISTORICAL_REPLAY_READY`가 됐다. 같은 snapshot을 POSCO case에 연결한 adversarial row는 wrong-subject로, case 날짜를 하루 앞당긴 row는 future-data 위반으로 차단됐다.

controlled snapshot은 test/historical replay 경로의 compiler 검증 자료다. live fetch나 current production score의 증거라고 부르지 않는다.

## mandatory golden 판정

Phase 2 mandatory golden의 C06/C08/C15 URL-backed case는 아직 registered provider snapshot이 없으므로 모두 `PROVIDER_SNAPSHOT_NOT_FOUND` exact blocker를 가진다. C17/C24/C28 source-proxy case는 모두 planning-only repair task를 가진다.

따라서 다음 두 조건이 동시에 성립한다.

- URL-backed golden 3/3: replay ready 또는 exact blocker
- source-proxy golden 3/3: replay-ready 0, planning-only 3

## 출력

공식 compile CLI는 `source_verification/` 아래에 다음을 쓴다.

- `provider_snapshots.jsonl`
- `case_source_links.jsonl`
- `source_verifications.jsonl`
- `historical_replay_ready_sources.jsonl`
- `source_repair_queue.jsonl`
- `case_source_statuses.jsonl`
- `source_verification_manifest.json`
- `source_verification_report.md`

## 아직 통과하지 않은 것

Phase 3는 “이 과거 source가 이 case를 실제로 뒷받침하는가”만 검증한다. 어떤 primitive 질문을 어떤 source family와 section에서 찾아야 하는지는 Phase 4 EvidenceRecipe가 담당한다. 현재 case의 검색·문서 선택·claim extraction·deterministic score·StageCourt 연결도 아직 완료 상태가 아니다.
