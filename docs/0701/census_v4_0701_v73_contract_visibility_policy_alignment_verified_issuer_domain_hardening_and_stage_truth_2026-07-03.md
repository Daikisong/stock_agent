# Census v4 0701 v73 Contract Visibility Policy Alignment / Verified Issuer Domain Hardening / Stage Truth

작성일: 2026-07-03

이 문서는 v72 교차검증 피드백을 반영한 v73 감사 패킷이다. 다음 에이전트는 이 문서를 성공 보고서로 읽으면 안 된다.

한 줄 결론:

```text
v73은 contract_visibility가 일반 웹으로 새는 경로와
verified_issuer_original 도메인 과허용 경로를 더 막았다.

하지만 운영자가 사용할 수 있는 FULL_THESIS Stage는 여전히 0개다.
```

쉬운 예:

```text
계약 가시성(contract_visibility)
  -> 계약 원문, 정정, 기간, 금액, 상대방은 DART/KIND/IR 같은 공식 원문에서 먼저 닫아야 한다.
  -> 뉴스는 배경 설명일 수 있지만, 이 primitive 자체를 뉴스 검색으로 바로 채우면 안 된다.

회사 공식 뉴스룸
  -> www.skhynix.com의 하위 도메인인 news.skhynix.com은 자동 verified issuer original 후보가 될 수 있다.
  -> news.skhynix.co.kr처럼 이름은 비슷하지만 별도 등록 도메인은 자동 통과시키지 않는다.
  -> 별도 공식 도메인을 허용하려면 issuer-domain registry가 필요하다.
```

## 1. 현재 Stage 질문에 대한 정확한 답

v73 기준 답:

```text
Stage처럼 보이는 상태판 행은 있다.
하지만 운영 Stage는 없다.
```

근거 artifact:

```text
output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v73/readiness_verdict.json
output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v73/census_stage_status.jsonl
```

숫자:

| 항목 | v73 값 | 해석 |
| --- | ---: | --- |
| `census_stage_status.jsonl` rows | 3391 | 전체 상태판 행 |
| `stage_scope=CENSUS_EVENT_BOARD` | 3391 | 전부 상태판 scope |
| `operator_stage_use=NOT_FULL_THESIS_STAGE` | 3391 | 운영 Stage로 쓰면 안 됨 |
| `FULL_THESIS` row | 0 | 운영 full thesis Stage 없음 |
| `FULL_E2R_100` verified score row | 0 | 운영 100점 체계 점수 없음 |
| event-board non-Stage0 row | 85 | full thesis refresh queue 후보 |

현재 base stage 분포:

```text
Stage0       3306
Stage1         54
Stage2-Watch   30
Red             1
```

중요:

```text
위 Stage0/Stage1/Stage2-Watch/Red는 CENSUS_EVENT_BOARD 상태판 label이다.
삼성전자/하이닉스 같은 실제 운영 FULL_THESIS Stage가 아니다.
```

## 2. v72 교차검증에서 나온 P0 지적

교차검증 A:

```text
v72는 FULL_THESIS Stage를 만들지 않았다.
accepted_claim=1, StageCourt trace=1 같은 조각만 보면 성공처럼 보일 수 있지만,
full_thesis_stage_row_count=0, operational_stage_use_allowed=false, verdict=NOT_READY다.
```

교차검증 B:

```text
contract_visibility 정책이 planner / v3 validator / source acquisition runner에서 완전히 같지 않았다.
planner와 validator는 contract_visibility를 official-solvable로 보는데,
runner 단독 경로는 contract_visibility web fallback을 허용할 수 있었다.

verified_issuer_original 도메인 판정도 같은 brand stem이면 별도 등록 도메인을 열 수 있었다.
예: company.com이 공식 홈페이지인데 company.net 같은 host가 title/snippet에 회사명을 넣으면 과허용 위험이 있었다.

bridge도 verified_issuer_original 문자열만 보면 lineage를 믿을 수 있었다.
```

이 지적은 타당했다. v73은 이를 일부 코드로 막았다.

## 3. v73 코드 패치

패치 파일:

```text
src/e2r/research_brain/v4_source_acquisition_runner.py
src/e2r/research_brain/v4_evidence_extraction_bridge.py
tests/test_research_brain_v4_real_source_acquisition.py
tests/test_research_brain_v4_evidence_extraction_from_real_document.py
```

### 3.1 `contract_visibility` official-first 정책 정렬

변경:

```text
v4_source_acquisition_runner._OFFICIAL_SOLVABLE_PRIMITIVE_IDS에 contract_visibility 추가
_is_official_solvable_gap() token set에 contract 추가
```

효과:

```text
planner가 contract_visibility를 공식 소스 우선으로 정리해도,
runner 단독 경로가 다시 뉴스/web fetch로 여는 불일치가 줄었다.
```

쉬운 예:

```text
나쁜 경로:
  contract_visibility
  -> TrustedNews / NaverSearch로 바로 fetch
  -> 계약 원문 없이 뉴스 배경으로 점수 후보 생성

v73 경로:
  contract_visibility
  -> official-solvable policy rejection 또는 DART/KIND/IR 우선
  -> 일반 웹은 별도 primitive나 후속 source task에서만 제한적으로 접근
```

### 3.2 verified issuer domain 판정 보수화

변경:

```text
기존:
  homepage host와 result host의 brand stem이 같으면 verified_issuer_original 가능

v73:
  result host == homepage host
  또는 result host가 homepage host의 하위 subdomain일 때만 자동 verified_issuer_original
```

예:

| homepage seed | result URL | v73 판정 |
| --- | --- | --- |
| `skhynix.com` | `https://news.skhynix.com/...` | verified issuer original 후보 |
| `skhynix.com` | `https://news.skhynix.co.kr/...` | 자동 verified 아님 |
| `skhynix.com` | `https://skhynix.com.fake-domain.com/...` | verified 아님 |
| `skhynix.com` | `https://skhynix-investor.co.kr/...` | verified 아님 |

중요한 tradeoff:

```text
news.skhynix.co.kr이 실제 공식 뉴스룸일 수 있어도,
CompanyGuide homepage seed가 skhynix.com뿐이면 v73은 자동으로 열지 않는다.

이건 보수적인 선택이다.
별도 공식 도메인을 안전하게 열려면 issuer official domain registry가 필요하다.
```

### 3.3 bridge lineage 재검증

변경:

```text
v4_evidence_extraction_bridge._document_has_verified_issuer_original_lineage()
  - source_lineage_id에 marker가 있는지만 보지 않음
  - lineage의 homepage/result host를 파싱
  - document.canonical_url host가 lineage result host와 같은지 확인
  - result host가 homepage host와 같거나 하위 subdomain인지 확인
```

쉬운 예:

```text
source_lineage_id에
  verified_issuer_original:issuer_official_domain:skhynix.com:news.skhynix.co.kr
라고 써 있어도,

canonical URL host가 news.skhynix.co.kr이고
이 host가 skhynix.com의 하위 도메인이 아니면
verified issuer original로 인정하지 않는다.
```

## 4. v73 live smoke 결과

실행:

```bash
E2R_CODEX_PLANNER_TIMEOUT_SECONDS=120 E2R_CODEX_EXTRACTOR_TIMEOUT_SECONDS=120 PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --output-root output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v73 \
  --v3-output-root output/census_v3/2026-07-01 \
  --run-mode BRAIN_AND_WEB_ACQUISITION_ENABLED \
  --brain-web-mode enabled \
  --brain-planner-provider codex_cli \
  --brain-source-acquisition live_full_bounded \
  --brain-universe-limit 1 \
  --brain-planner-success-limit 1 \
  --brain-planner-batch-size 1 \
  --brain-max-source-tasks-per-plan 3 \
  --brain-max-fetches-per-task 1 \
  --brain-claim-extractor-timeout-seconds 120 \
  --brain-stage-promotion-mode strict \
  --target-gate brain_web \
  --write-operational-docs false \
  --fail-on-critical-audit false \
  --test-result-artifact output/census_v4/2026-07-01/full_unittest_result_artifact.json
```

결과:

```text
exit code = 1
stdout = NOT_READY
```

Brain/Web readiness:

| 항목 | v73 값 | minimum | 해석 |
| --- | ---: | ---: | --- |
| planner rows | 22 | 30 | 부족 |
| real planner success | 2 | - | v72의 1보다 개선 |
| web search tasks | 5 | 20 | 부족 |
| web search calls | 5 | 20 | 부족 |
| web results | 41 | - | 검색은 됨 |
| fetched documents | 1 | 10 | 부족 |
| LLM extractor attempts | 1 | 10 | 부족 |
| extractor provider errors | 0 | - | provider error는 없음 |
| web/LLM accepted claims | 0 | 3 | 핵심 차단 |
| promoted brain stage rows | 0 | - | 승격 없음 |

Source task execution:

```text
source_task rows = 104
EVIDENCE_OS_ACCEPTED = 61
EVIDENCE_OS_BASELINE_ONLY = 32
NO_EVIDENCE_FOUND = 8
PROVIDER_FAILED = 2
REJECTED_BY_POLICY = 1
```

Web fetched document:

```text
url = https://stock.pstatic.net/stock-research/company/34/20251104_company_405753000.pdf
verified_issuer_original = false
```

즉 v73 live smoke는 official/company-newsroom claim을 성공시킨 실행이 아니다.
general web/research PDF 후보 1개를 fetch했고, accepted web/LLM claim은 0개다.

## 5. v72 대비 개선과 악화가 아닌 차단

개선:

```text
v72 provider_error:
  codex_cli_timeout 1개
  real_provider_success 1개

v73 provider_error:
  codex_cli_timeout 없음
  real_provider_success 2개

v72 Brain/Web web task/call:
  2 / 2

v73 Brain/Web web task/call:
  5 / 5
```

차단 유지:

```text
web_or_llm_accepted_claim_count = 0
brain_promoted_stage_row_count = 0
FULL_THESIS row = 0
FULL_E2R_100 row = 0
verdict = NOT_READY
```

이건 실패를 숨기는 게 아니라, 오히려 더 정직한 상태다.

쉬운 예:

```text
v72:
  "계약 가시성"을 뉴스로 열 수 있는 뒷문이 있었다.

v73:
  그 뒷문은 닫혔다.
  대신 진짜 공식 원문이나 안전한 issuer domain registry가 없으면 pending으로 남는다.
```

## 6. Goal matrix 기준 현재 완료/미완료

Artifact:

```text
output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v73/goal_requirement_matrix_audit.json
```

요약:

```text
required_goal_completion_count = 19
pass = 14
pending = 5
fail = 0
goal_completion_minimum_pass = false
```

남은 pending 5개:

| gate | 상태 | blocker |
| --- | --- | --- |
| `FULL_THESIS_SMOKE_PASS` | PENDING | `full_thesis_smoke_pending` |
| `FULL_THESIS_PRODUCTION_PASS` | PENDING | `full_thesis_production_pass_false` |
| `FULL_THESIS_SEED_PROMOTION_PASS` | PENDING | `full_thesis_seed_promotion_pass_false` |
| `BRAIN_WEB_EVIDENCE_PASS` | PENDING | `brain_web_evidence_pass_false` |
| `ALL_ARCHETYPE_SOURCE_BACKED_REPLAY_PASS` | PENDING | `source_backed_replay_parity_all_archetypes_pending` |

통과한 중요한 guard:

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
ATOMIC_STAGE_DECISION_PASS
SCORE_SCALE_PASS
STAGE_SEMANTICS_PASS
SEMANTIC_PRIMITIVE_GUARD_PASS
SOURCE_TASK_SATISFACTION_PASS
KNOWN_BAD_REGRESSION_PASS
SELF_REPAIR_LOOP_PASS
```

의미:

```text
가짜 성공을 막는 안전장치는 많이 통과했다.
하지만 운영 full thesis 점수/Stage를 생성하는 경로는 아직 통과하지 못했다.
```

## 7. Full thesis seed 상태

Artifact:

```text
output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v73/full_thesis_seed_materialization_audit.json
```

숫자:

```text
seed_event_count = 85
trace_row_count = 85
planner_run_seed_count = 21
real_provider_success_seed_count = 1
accepted_claim_seed_count = 1
stagecourt_trace_seed_count = 1
full_thesis_promoted_seed_count = 0
```

status_counts:

```text
PLANNER_NOT_RUN = 64
PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS = 20
STAGECOURT_READY_NOT_PROMOTED = 1
```

가장 가까운 후보:

```text
SK하이닉스 000660
accepted official claim = 1
StageCourt trace = 1
하지만 FULL_THESIS promoted = 0
```

이유:

```text
Green primitive coverage가 닫히지 않았고,
web/LLM accepted claim도 0개다.
```

## 8. 삼성전자/하이닉스 smoke 상태

Artifact:

```text
output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v73/samsung_hynix_full_thesis_smoke.json
```

숫자:

```text
verdict = PENDING_FULL_THESIS_REFRESH
full_thesis_status = PENDING_FULL_THESIS_REFRESH
smoke_task_count = 14
score_allowed_before_execution = false
daily_event_and_full_thesis_separated = true
hardcoded_query_count = 0
```

해석:

```text
삼성전자/하이닉스는 여전히 "운영 점수 몇 점, Stage 몇"으로 말할 수 있는 상태가 아니다.
smoke task는 준비돼 있지만 full thesis refresh가 끝나지 않았다.
```

## 9. 남은 핵심 병목

### 9.1 web/LLM accepted claim이 0개

v73에서 Brain/Web gate가 막힌 가장 직접적인 이유:

```text
web_or_llm_accepted_claim_count = 0
minimum = 3
```

문서를 하나 가져온 것과 점수 claim이 생긴 것은 다르다.

쉬운 예:

```text
PDF를 1개 fetch했다.
  -> 문서를 가져온 것.

그 PDF 원문에서 "SK하이닉스의 HBM 고객 물량 배정이 현재 확정"이라는
direct/current/source-backed claim이 만들어졌다.
  -> 점수 재료.

v73은 첫 번째만 했고, 두 번째는 못 했다.
```

### 9.2 issuer official alternate domain registry 부재

v73은 같은 stem의 다른 등록 도메인을 자동으로 믿지 않는다.

좋은 점:

```text
company.net 같은 spoof를 official로 열 위험이 줄었다.
```

나쁜 점:

```text
실제 회사가 별도 공식 뉴스룸 도메인을 쓰는 경우도 자동으로 막힐 수 있다.
```

다음 패치 방향:

```text
issuer official domain registry를 만들어야 한다.
입력은 CompanyGuide homepage, 회사 IR에 명시된 official links, DART 회사개황 URL, 수동 검증된 issuer domain snapshot이어야 한다.
검색 결과의 brand stem만으로 registry를 만들면 안 된다.
```

### 9.3 stop-on-resolution은 아직 완전하지 않다

교차검증 지적:

```text
LIVE_FULL_BOUNDED는 official source가 잡혀도 같은 task에서 web을 병합할 수 있다.
```

v73에서는 이 부분을 전면 수정하지 않았다.

이유:

```text
acquisition 단계의 PARSED 문서가 실제 primitive를 만족하는 accepted claim인지
그 시점에는 아직 모른다.
무작정 official fetch가 있으면 web을 닫으면,
coverage-only official 문서 때문에 필요한 follow-up이 막힐 수 있다.
```

다음 패치 방향:

```text
stop-on-resolution은 acquisition-only가 아니라
source task execution의 accepted direct claim 기준으로 걸어야 한다.

즉:
  official document fetched
  -> claim extraction/adjudication/mapping
  -> direct accepted claim이 task primitive를 만족
  -> 그때 같은 task의 web fallback 중단
```

## 10. 다음 에이전트 공격 지시

다음 에이전트는 아래를 우선 공격해야 한다.

1. `web_or_llm_accepted_claim_count=0`을 해결하라.
   - 단, generic news를 점수 경로로 열지 말 것.
   - 공식 원문 또는 verified issuer domain registry로 원문성을 먼저 닫을 것.

2. issuer official domain registry를 구현하라.
   - CompanyGuide homepage의 하위 도메인만 자동 인정하는 v73 기본값은 유지.
   - 다른 등록 도메인은 registry에 source anchor가 있을 때만 인정.
   - 예: `news.skhynix.co.kr`를 열려면 "이 host가 SK하이닉스 공식 뉴스룸"이라는 별도 source-backed registry row가 필요.

3. accepted direct claim 기준 stop-on-resolution을 구현하라.
   - 문서 fetch만으로 web fallback을 닫지 말 것.
   - task primitive를 직접 만족한 accepted claim이 생겼을 때만 닫을 것.

4. `FULL_THESIS` promotion을 실제로 닫아라.
   - queue row, event-board Stage, official-only partial trace를 운영 Stage로 쓰지 말 것.
   - `FULL_THESIS` scope row와 `FULL_E2R_100` verified score row가 실제로 생겨야 한다.

5. all-archetype source-backed replay gap을 줄여라.
   - 현재 required archetype 32개 중 source-backed ready 6개, missing 26개다.
   - source_proxy_only 연구자료를 fixture 정답으로 쓰면 안 된다.

## 11. 검증

Targeted tests:

```text
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_real_source_acquisition.ResearchBrainV4RealSourceAcquisitionTests.test_live_full_bounded_marks_company_homepage_subdomain_as_verified_newsroom_original \
  tests.test_research_brain_v4_real_source_acquisition.ResearchBrainV4RealSourceAcquisitionTests.test_live_full_bounded_does_not_mark_issuer_domain_spoof_hosts_as_verified_original \
  tests.test_research_brain_v4_real_source_acquisition.ResearchBrainV4RealSourceAcquisitionTests.test_contract_visibility_gap_is_not_sent_to_web_fallback \
  tests.test_research_brain_v4_evidence_extraction_from_real_document.ResearchBrainV4EvidenceExtractionFromRealDocumentTests.test_verified_company_newsroom_original_avoids_general_web_lineage_block_but_profile_claim_still_not_scored \
  tests.test_research_brain_v4_evidence_extraction_from_real_document.ResearchBrainV4EvidenceExtractionFromRealDocumentTests.test_verified_company_newsroom_original_can_score_direct_customer_allocation_claim \
  tests.test_research_brain_v4_evidence_extraction_from_real_document.ResearchBrainV4EvidenceExtractionFromRealDocumentTests.test_verified_company_newsroom_lineage_requires_homepage_subdomain_match -v

Ran 6 tests
OK
```

Related regression:

```text
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_operational_modes \
  tests.test_research_brain_v4_real_source_acquisition \
  tests.test_research_brain_v4_evidence_extraction_from_real_document \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_brain_stage_promotion_gate -v

Ran 150 tests
OK
```

Full suite:

```text
PYTHONPATH=src python -m unittest discover -s tests -v

Ran 5106 tests in 216.313s
OK
```

Diff check:

```text
git diff --check
OK
```

## 12. 최종 판단

v73은 READY가 아니다.

정확한 상태:

```text
anti-fake / stage-scope / score-scope / semantic guard는 계속 단단해지고 있다.
contract_visibility web leakage와 verified issuer domain over-acceptance는 v73에서 더 막았다.

하지만 Brain/Web accepted claim과 FULL_THESIS promotion이 아직 없다.
따라서 운영 파이프라인이라고 말하면 안 된다.
```

운영자용 한 줄:

```text
현재 산출물은 전체 상태판과 refresh queue까지는 있다.
하지만 실제 full thesis 채점지와 운영 Stage는 아직 없다.
```
