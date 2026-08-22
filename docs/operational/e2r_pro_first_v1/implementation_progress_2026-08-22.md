# Pro-first 실제 구현 진행 기록 — 2026-08-22

이 문서는 외부 검수자가 코드 diff만 읽지 않아도 실제 작업 순서, 실패 원인,
수정 근거, 현재 canonical runtime 상태를 재구성할 수 있게 계속 갱신한다.

## 1. 범위와 불변식

- 브랜치: `feature/e2r-pro-first-browser-platform-20260822`
- Draft PR: `#7`
- 실제 대상: `000660 / SK하이닉스`
- `as_of_date`: `2026-08-22`
- archetype: `C06_HBM_MEMORY_CUSTOMER_CAPACITY`
- job: `PROJOB-70e6a50ae757bd874e602a85`
- run: `PRORUN-643c723370681970b5bcc582`
- conversation: `WEB:baa35b0b-ceac-4727-9942-383e58046f08`
- ChatGPT 제출/캡처: `1/1`; 재제출 금지
- Pro의 점수·Stage는 권한 없음. 최종 score/Stage는 deterministic engine만 계산한다.

로컬 실제 runtime은 다음 위치에 있다.

```text
/mnt/c/Users/eorb9/AppData/Local/E2R/ProFirstRuntime
```

raw browser capture는 다음 파일로 보존돼 있다.

```text
jobs/PROJOB-70e6a50ae757bd874e602a85/capture/incoming/pro_report.md
jobs/PROJOB-70e6a50ae757bd874e602a85/capture/incoming/research_dossier.json
jobs/PROJOB-70e6a50ae757bd874e602a85/capture/incoming/browser_capture_receipt.json
```

## 2. 현재 canonical 상태

2026-08-22 현재 job 상태는 `FINAL`이며 publication까지 완료됐다.

| 항목 | 현재값 |
|---|---:|
| Pro candidate facts | 35 |
| source 검문 통과 | 26 |
| 현재 positive | 16 |
| counter | 10 |
| source 불가 | 5 |
| wrong segment | 3 |
| quote mismatch | 1 |
| EvidenceFact | 26 |
| component가 하나도 없는 accepted fact | 0 |
| CORE_SCORE_BLOCKER | 0 |
| CORROBORATION_CAP | 13 |
| supplemental task | 0 |
| 새 query/search | 0/0 |
| validated impact | 33 |
| component | 7/7 |
| Judge | 21/21 |
| deterministic score | 23.202275 |
| score interval | 23.202275~23.202275 |
| score valid | true |
| canonical Stage | 0 FINAL |

component별 source-backed fact coverage는 다음과 같다. 한 fact가 여러 component에
관련될 수 있으므로 합계는 26보다 크다.

```text
eps_fcf_explosion      7
earnings_visibility   19
bottleneck_pricing    15
market_mispricing      6
valuation_rerating     6
capital_allocation     9
information_confidence 14
```

최신 source verification:

```text
semantics: e2r_pro_source_verification_v6
verification id: PROVERIFY-73c6d8d67a458128b03a1d0e
verification hash: dd13f59782c86066f5c03f7f4bbda74ff0a5af95c17c0125e2af460600046a1f
document cache reuse: 33
fixed-URL fetch: 2
query/search: 0/0
mechanism scope mapping: 35/35
mapping hash: 8a7d6ac1012387d63a31aab13584291a25d9621ad929c45d5f351dc4a8ecf061
```

최신 gap adjudication:

```text
fact snapshot: 69127233abf7288bf4fd0fdd16c0dff1cab99ca0db5c633e90ad30e473706578
CORE_SCORE_BLOCKER: 0
CORROBORATION_CAP: 13
supplemental task: 0
full research restart: 0
```

## 3. 발견한 문제와 수정 이력

### 3.1 Pro dossier import dialect

실제 Pro 결과는 내용이 잘못된 것이 아니라 strict schema와 일부 표기 dialect가
달랐다. raw capture는 변경하지 않고, allowlist 구조 변환만 수행하는
`ResearchDossierDialectAdapter`를 추가했다. statement, URL, quote, value, date 등
증거 내용은 변환할 수 없도록 보호한다.

### 3.2 quote verifier의 literal-match 누락

- 반복 anchor가 있을 때 첫 위치만 보고 실패하던 문제를 backtracking으로 수정했다.
- 긴 exact anchor와 함께 있는 짧은 숫자 cell(`100%`)을 보존했다.
- semantic paraphrase는 여전히 검문 통과할 수 없다.

결과적으로 source 검문 통과가 `0`에서 `26`으로 회복됐다.

### 3.3 hash-verified full-document cache

동일 job의 `URL + as_of_date + SHA256`가 일치하는 full document만 재사용한다.
파일 경로는 job root 밖으로 나갈 수 없고 UTF-8/해시 검증 실패 시 재사용하지 않는다.

### 3.4 자유형 Pro predicate를 단어 목록으로 다시 버린 문제

초기 component 배치기는 자유형 predicate와 product 문구를 keyword priority로
추측했다. 예를 들어 `DRAM and NAND`를 NAND 하나로 고르거나, 순현금/FCF/buyback을
`CORPORATE_GENERIC`이라는 이유로 valuation/capital component에서 버렸다.

수정 원칙:

```text
자연어 → Codex가 기존 contract enum으로 구조화
contract enum → 기존 MechanismScopeValidator가 deterministic 검증
component credit → downstream validator/scorer가 결정
```

35개 scope mapping은 다음 durable 파일에 저장한다.

```text
verification/mechanism_scope_mappings.jsonl
```

같은 roster와 mapping hash면 다음 실행은 Codex를 다시 부르지 않고 이 파일을
재사용한다.

### 3.5 material gap 무한 검색

기존에는 component마다 검증 fact가 있어도 open-ended 세부 gap을 모두 CORE로
취급해 5개 supplemental task가 생겼다. 첫 실행은 13 query/29 candidate/10 fetch,
두 번째 실행은 12 query/31 candidate/11 fetch였지만 EvidenceFact는 0이었다.

원인은 두 가지였다.

1. 임의 `NEED-*`를 Evidence OS contract primitive로 넘겨 유효 claim도 exact task를
   만족시키지 못했다.
2. 이미 검증된 component coverage가 있는데도 추가 세부정보를 core source 부재로
   취급했다.

수정 후에는 13개 모두 `CORROBORATION_CAP`, supplemental task 0이다. 즉 부족한
세부정보는 uncertainty/cap으로 남지만 점수 파이프라인을 무한 검색으로 막지 않는다.

과거 supplemental 실행은 덮어쓰지 않고 다음에 보존됐다.

```text
supplemental/attempts/f12e2f16910367946fcb735a940f2aba192340012b3be8053e402f059a2446b4/
```

## 4. 폐기한 접근

`ProValidatedImpactCompiler`가 26개 fact를 각각 별도 Codex proposal/skeptic 호출로
재해석하는 실행을 시작했으나 약 8분 후 수동 중단했다. 자료를 component 판단기로
한 번에 넘기면 될 일을 fact별 parser처럼 반복하는 구조였기 때문이다. 종료 코드는
`130 (KeyboardInterrupt)`이고 job은 상태 전이 전이므로 `COMPONENT_RESEARCH`를 유지한다.

이 접근의 산출물은 canonical score receipt로 채택하지 않는다.

## 5. 확정한 후반 파이프라인

```text
Pro report MD 전체
+ normalized dossier
+ source-verified EvidenceFact 26
+ gap dispositions 13
        ↓
bounded component 판단 agent
  - 자료 재검색 금지
  - verified fact ID만 인용
  - 7개 component memo/impact 제안
        ↓
existing deterministic lineage/mechanism/credit validator
        ↓
21 Evidence-only Judge
        ↓
deterministic scorer
        ↓
AtomicStageCourtV2
        ↓
publication
```

parser의 책임은 `URL·날짜·quote·주체·fact lineage` 검문까지다. 자유형 Pro 문장을
keyword로 점수 component에 억지 삽입하는 책임은 parser에 두지 않는다.

### 5.1 2026-08-22 구현 반영

운영 기본 impact provider를 `CodexDossierImpactProvider`로 교체했다. 입력은 다음을
한 번에 받는다.

```text
Pro report MD 전체
+ normalized component research
+ source-verified claim catalog
+ claim별 deterministic allowed impact edge
+ gap dispositions
+ applicable rubric
```

LLM 출력에는 `score`, `Stage`, `direction`, `source_family`, `temporal_scope`,
`mechanism_scope_match` 필드가 아예 없다. 판단기는 검증 claim마다 허용된 edge를
선택하고 강도·완결성·한계만 제안한다. 방향·source lineage·현재성·mechanism
scope는 deterministic 코드가 주입하거나 재검증한다.

기존 per-claim provider 경로는 주입형 단위테스트의 호환성만 위해 남겼으며,
`OperationalProScoringInputProvider`는 whole-dossier provider만 사용한다.

실제 000660 실행에서 primary whole-dossier 응답은 32개 impact를 만들었다. 이 중
3개는 deterministic allowed edge와 exact match하지 않아 점수 재료에서 제외하고
claim/edge/reason을 audit row에 보존했다. 32개 유효 impact가 6개 component를
덮었고 `market_mispricing`만 비어서, 전체 연구나 source fetch가 아닌 단 한 번의
missing-component semantic repair를 실행했다. 결과 1개가 추가돼 33개 impact와
7/7 coverage가 완성됐다.

```text
primary whole-dossier provider: 1회
missing-component repair:       1회
fact별 provider loop:           0회
scoring query/fetch:            0/0
```

두 응답은 다음 runtime cache에 즉시 저장된다.

```text
scoring/whole_dossier_impact_response.json
scoring/whole_dossier_impact_repair_response.json
```

Judge 21개도 각 응답을 `scoring/judge_response_cache/`에 즉시 저장한다. 따라서
중간에 13번째 Judge가 실패해도 1번째부터 다시 호출하지 않는다.

쉬운 예:

```text
판단기가 PROCLAIM-1을 valuation에 연결
→ PROCLAIM-1의 allowed edge에 valuation이 있으면 다음 검문으로 이동
→ allowed edge에 없거나 mapping ID를 새로 만들면 즉시 batch pending
→ 유효 edge만 ClaimImpactLedgerBuilder와 ImpactValidator가 다시 검증
```

쉬운 예:

```text
순현금 69.37조
→ parser가 valuation인지 capital인지 단어로 결정하지 않음
→ 판단 agent가 MD 문맥에서 두 component 관련성을 제안
→ 기존 validator가 허용 edge와 fact lineage를 확인
→ Judge와 deterministic scorer가 최종 숫자를 계산
```

## 6. 검증 현황

최근 focused 검증:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_business_mechanism_scope \
  tests.test_e2r_pro_first_source_verification \
  tests.test_e2r_pro_first_gap_adjudication \
  tests.test_e2r_pro_first_scoring_bridge -v
```

확인된 결과:

- source/gap/scoring 묶음 72 tests PASS
- business mechanism operational audit: PASS, critical 0
- gap 재판정: CORE 0, supplemental 0
- 실제 Pro submit/capture는 여전히 1/1
- whole-dossier provider 경계 테스트 3개 PASS
  - 전체 dossier 단일 호출
  - score/Stage/source/direction 출력 권한 없음
  - provider가 만든 미등록 mapping은 scoring 전에 거부

실제 live canary 후반 결과:

```text
source-verified facts: 26
credit-validated impacts: 33
component: 7/7
Judge: 21/21
deterministic score: 23.202275
score_valid: true
AtomicStageCourtV2: Stage 0 FINAL
publication: PUBLISHED
investment recommendation: false
```

동일 snapshot 재실행에는 호출되면 즉시 예외를 내는 provider를 주입했다.

```text
impact artifact reused: true
impact provider calls: 0
Judge response reused: 21
Judge provider calls: 0
query/fetch: 0/0
```

이 결과는 기존 Gate 1의 000660 `70.2 / Stage 2` receipt를 덮어쓰지 않는다.
Gate 1은 기존 별도 evidence snapshot의 결과이고, 이 문서의 `23.202275 / Stage 0`은
2026-08-22 Pro-first live canary에서 새로 수집·검증된 26 facts로 계산한 결과다.

### 6.1 실행 중 발견해 수정한 후반 경계 결함

1. component confidence가 `HIGH_ON_REPORTED_ACTUALS_MEDIUM_ON_RUN_RATE`처럼
   들어오면 숫자 변환에서 실패했다. 허용된 HIGH/MEDIUM/LOW band만 인식하고
   복합 표현은 가장 낮은 band를 쓰도록 수정했다.
2. structured output schema의 `uniqueItems`가 실제 provider API에서 허용되지 않아
   400이 발생했다. 중복 검문은 deterministic 코드에 있으므로 schema 키를 제거했다.
3. historical anchor가 0개인데도 Judge가 anchor를 꾸며내도록 강제하는 모순이
   있었다. anchor가 있으면 ID와 비교를 함께 필수로 하고, 없으면 둘 다 빈 상태만
   허용하도록 수정했다.
4. provider 응답을 decoder 통과 뒤에만 저장해 invalid 한 건이면 전체 응답을
   잃었다. 이제 응답 직후 hash-verified cache로 저장하고 decoder 수정·재실행은
   provider 0회로 수행한다.

### 6.2 2026-08-23 최종 검증 진행

후반 수정 뒤 focused 묶음은 119/119 PASS다. 최초 전체 suite에서는 다음 3개가
실패했다.

```text
claim eligibility operational audit 1개
semantic scoring known-bad 2개
```

원인은 서로 다른 코드 결함 3개가 아니었다. 최신 eligibility 계산값과 tracked JSON
영수증이 달랐고, known-bad 두 검사는 그 첫 검사를 detector로 다시 실행해 연쇄
실패한 것이었다. 공식 CLI로만 영수증을 재생성했다.

```bash
PYTHONPATH=src python -m e2r.cli.compile_e2r_claim_eligibility_audit \
  --repo-root . --output docs/operational/e2r_claim_eligibility_audit.json
PYTHONPATH=src python -m e2r.cli.compile_e2r_evidence_to_score_known_bad \
  --output docs/operational/e2r_semantic_scoring_known_bad_audit.json
```

재검증 결과는 eligibility `39 decisions / critical 0`, known-bad `35 cases /
critical 0`, 문제 3개 단독 실행 `3/3 PASS`다.

현재 완료된 독립 검증:

```text
focused source/gap/scoring/browser: 119/119 PASS
Pro-first core unit:               188/188 PASS
browser mock E2E:                    44/44 PASS
golden offline E2E:                   4/4 PASS
Phase100:                            15/15 PASS
Pro-first static audit:         critical 0 PASS
production static audit:        critical 0 PASS
compileall:                         PASS
git diff --check:                   PASS
```

전수 unittest는 사용자 중단으로 최종 summary가 사라진 첫 실행을 성공 근거로 쓰지
않고 처음부터 재실행했다. 그 재실행은 다음처럼 종료됐다.

```text
Ran 7,403 tests in 521.692s
failures 5 / skipped 38
```

3개는 scope contract 변경 뒤 impact/dedupe/question tracked 감사 JSON이 낡은
문제였다. 2개는 실제 generic scope 회귀였다.

1. `GENERIC_INFORMATION + INFORMATION_ONLY`를 market/valuation에도 허용해 일반
   회사 정보가 시장 오판 근거처럼 통과했다.
2. issuer consolidated actual이 EPS/FCF 전용 tuple로 인식된 뒤에도 다른 component
   검사에서 generic corporate 규칙으로 fallback해 `information_confidence`가 중복
   부여됐다.

수정 후 market/valuation corporate fact에는
`VALUATION_EARNINGS_BRIDGE`, `MARKET_EXPECTATION_GAP`, `RISK_COUNTER`만 허용하고,
closed consolidated-actual tuple은 EPS/FCF 외 component로 fallback하지 않는다.
두 실제 회귀와 새 generic-information 회귀 테스트는 3/3 PASS, 원래 실패 5개는
공식 감사 compiler 재생성 후 5/5 PASS다.

최종 전수 재실행은 다음처럼 완료됐다. 이 검증은 live web, 새 연구, 새
query/fetch를 호출하지 않았다.

```text
Ran 7,404 tests in 511.786s
OK (skipped=38)
failure/error: 0/0
```

최종 코드 기준 추가 게이트도 다시 확인했다.

```text
Phase100: 15/15 PASS
production static audit: E2R_V6_PRODUCTION_STATIC_AUDIT_PASS, critical 0
production static audit hash: 5e3c32cbf4257235441639291fa720e338d0ce6eef12d23e8b79bcb6518067b1
final Pro-first offline CI: PRO_FIRST_OFFLINE_CI_PASS
  - core 188/188
  - browser mock 44/44
  - golden offline E2E 4/4
  - compileall PASS
  - git diff --check PASS
```

## 7. 남은 작업

1. 한글 commit/push 후 Draft PR #7 본문을 실제 FINAL 상태로 갱신한다.
2. 새 PR head의 GitHub Actions 결과를 확인한다.

이 문서를 포함한 PR head SHA가 최종 코드 identity다. commit 객체 안에 자기 자신의
SHA를 적으면 내용 변경으로 SHA가 다시 바뀌므로, 고정 문자열을 억지로 적지 않고
Git/PR head를 authority로 둔다.
