# Census v4 Live Brain Candidate / OpenDART Forensic - 2026-07-01

이 문서는 다음 에이전트가 `Brain/Web enabled` 경로를 빡세게 리뷰할 수 있게, 최신 probe와 패치 결과를 고정한다.

핵심 질문:

```text
Stage가 있는 애들이 있긴 한가?
Brain/Web을 켜면 진짜 운영 후보와 진짜 DART 원문을 보고 있나?
그래도 아직 왜 NOT_READY인가?
```

## 결론

```text
Stage label은 있다.
하지만 full thesis 운영 Stage는 여전히 0개다.

Brain/Web enabled probe는 이제 첫 planner 후보를 fixture/cache가 아니라
URL-backed live DART 후보로 잡는다.

OpenDART document.xml ZIP도 더 이상 PK 바이너리로 claim에 새지 않는다.
CSS 노이즈도 제거되어 실제 공시 본문이 raw assertion에 들어온다.

하지만 최신 enabled probe는 아직 accepted Brain claim 0개다.
선택된 대웅 공시는 시설투자 종료일 연장 정정이라,
C29/C31 긍정 primitive로 억지 승인하지 않고 막힌 상태다.
이 방어는 Brain/Web attempt 경로 기준으로는 맞다.

단, 같은 `/tmp` 산출물 안의 기존 event-board leaf에는
대웅 `003090` 공시의 accepted claim / score contribution leaf가 여전히 남아 있다.
이전에는 대표 `census_stage_status` row도 `event_evidence_score=1.5`,
`Stage2-Watch`로 읽혔다.
최신 패치 후에는 대표 row에서 `semantic_guard_status=BLOCKED`,
`semantic_guard_class=facility_investment_correction_followup_required`,
`score_scale=NO_SCORE`, `base_stage=Stage1`로 차단된다.
정확한 판정은 "claim/contribution leaf는 감사 추적용으로 남아 있지만,
대표 event-board 점수와 Stage 승격은 semantic guard가 막는다"이다.
```

쉬운 예:

```text
이전 상태:
  조사원이 시험지 대신 캐시 메모장이나 fixture 샘플을 들고 출발했다.
  OpenDART 원문도 ZIP 봉투째 읽어서 PK... 같은 깨진 글자를 봤다.

현재 상태:
  조사원이 실제 DART URL 문서까지는 가져온다.
  봉투도 열고 CSS 껍데기도 어느 정도 걷어낸다.

아직 남은 상태:
  가져온 문서가 "공장 투자 종료일 연장"이면
  그걸 성장 Green 근거로 채점하면 안 된다.
  그래서 Evidence OS가 accepted claim으로 승인하지 않았다.

주의:
  새 Brain/Web attempt 채점관은 보류했지만,
  기존 event-board leaf에는 이 공시의 claim/contribution 흔적이 남아 있다.
  최신 패치는 대표 row 점수 반영을 semantic guard로 막는다.
```

## 최신 Probe 명령

격리 output:

```text
/tmp/census_v4_enabled_probe
```

명령:

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --output-root /tmp/census_v4_enabled_probe \
  --v3-output-root output/census_v3/2026-07-01 \
  --run-mode BRAIN_AND_WEB_ACQUISITION_ENABLED \
  --brain-web-mode enabled \
  --brain-planner-provider real \
  --brain-source-acquisition live_official_only \
  --brain-universe-limit 3 \
  --brain-planner-success-limit 1 \
  --brain-planner-batch-size 1 \
  --brain-max-fetches-per-task 2 \
  --brain-stage-promotion-mode disabled \
  --target-gate brain_web \
  --fail-on-critical-audit false \
  --write-operational-docs false
```

결과:

```text
exit code: 1
stdout: NOT_READY
```

## Stage 존재 여부

최신 probe의 `census_stage_summary.json` 기준:

```text
stage_status_count: 3391

stage_distribution:
  Stage0:       3306
  Stage1:         54
  Stage2-Watch:   30
  Red:             1

canonical_stage_distribution:
  0:       3306
  1:         54
  2:         30
  3-Red:      1

full_thesis_stage_distribution:
  FULL_THESIS_NOT_RUN: 3391

full_e2r_verified_score_count: 0
operator_stage_use_distribution:
  NOT_FULL_THESIS_STAGE: 3391
```

해석:

```text
Stage label은 있다.
하지만 모두 CENSUS_EVENT_BOARD 상태 label이다.
FULL_THESIS 운영 Stage는 아직 0개다.
```

틀린 해석:

```text
Stage1/Stage2-Watch가 있으니 전 종목 full E2R 점수가 끝났다.
```

맞는 해석:

```text
Stage1/Stage2-Watch는 "이번 전체지도에서 볼 만한 이벤트/claim이 있다"는 상태판이다.
100점 만점 full thesis 점수와 Green/Yellow 확정은 아니다.
```

## 이번에 고친 것

### 1. live planner 후보 오염 완화

이전 enabled probe에서는 첫 planner 후보가 fixture 또는 cache였다.

관측된 나쁜 예:

```text
111111 한전변압기
source_id: data/raw/korea_cheap_scan/opendart/disclosures/fixture.csv

000000 관리주의샘플
source_id: data/raw/kind/risk_flags/risk_flags.csv

000660 SK하이닉스
source_id: data/cache/company_guide/2026-06-28/000660_recent_reports.json
```

패치:

```text
src/e2r/research_brain/v4_production_orchestrator.py

discover_daily_candidate_events_v4()
  -> output/production_cutover_v3/*/candidate_events.json의
     CE-LIVE-DART-* URL-backed 후보를 먼저 로드

_planner_candidate_order()
  -> live official mode에서 production-live 후보를 cache/fixture보다 우선

_discovery_limit_for_config()
  -> real planner + live source mode에서는 universe_limit로 너무 일찍 잘라내지 않음
```

최신 probe 첫 planner 후보:

```text
symbol: 003090
company_name: 대웅
candidate_event_id: CE-LIVE-DART-003090-20260630801612
source_family: DART
source_id: https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260630801612
provider_name: codex_cli_planner
real_provider_success: true
```

### 2. instrument registry 연결 보강

문제:

```text
003090 대웅, 069620 대웅제약, 114450 그린생명과학 같은 실제 Census universe 종목이
candidate purity에서 symbol_not_in_instrument_registry로 밀렸다.
```

원인:

```text
production candidate purity registry는
data/historical_official/universe/universe.csv 14줄과 일부 raw KRX fixture만 보고 있었다.

반면 실제 Census universe는 output/census_v3/2026-07-01/universe.jsonl 쪽에 3391개가 있었다.
```

패치:

```text
src/e2r/production/candidate_event_purity.py

load_instrument_registry()
  -> output/census_v3/*/universe.jsonl
  -> output/census_v4/*/universe.jsonl
를 alias registry로 읽는다.
```

주의:

```text
이 universe jsonl은 점수 증거가 아니다.
오직 "이 symbol이 실제 Census universe에 있는가"를 확인하는 entity registry 보조 장부다.
```

최신 로컬 확인:

```text
registry combined: 3956
official: 13

003090 대웅 DART https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260630801612
eligible: True
reasons: ()
```

### 3. OpenDART document.xml ZIP 디코딩

문제:

```text
OpenDART document.xml 응답은 ZIP payload인데,
live connector가 response.text를 그대로 raw_document로 넣었다.

그 결과 raw assertion quote가 PK...xml... 같은 바이너리로 시작했다.
```

나쁜 예:

```text
exact_quote: "PK\u0003\u0004..."
```

패치:

```text
src/e2r/production/source_connectors/opendart_live_connector.py

_fetch_detail_text()
  -> response.content를 보고 ZIP이면 내부 XML을 열어서 decode
```

회귀 테스트:

```text
tests/test_research_brain_v4_real_source_acquisition.py
  test_opendart_live_connector_decodes_document_xml_zip_payload
```

### 4. OpenDART XML CSS 노이즈 제거

문제:

```text
ZIP을 열어도 XML 내부 첫 text가 CSS 스타일이면
claim quote가 .xforms * { font-family: ... } 같은 서식으로 시작했다.
```

패치:

```text
src/e2r/sources/opendart.py

extract_document_text()
  -> CSS rule / font-family / border-collapse / padding / line-height 제거
```

회귀 테스트:

```text
tests/test_sources.py
  test_opendart_extract_document_text_strips_css_noise
```

최신 raw assertion 예:

```text
exact_quote:
  대웅/신규시설투자등/(2026.06.30)신규시설투자등 정정신고(보고)
  정정일자 2026-06-30
  정정사유 종료일 연장
  정정전 2026-06-30
  정정후 2027-05-31
```

이제 `PK...`도 아니고 CSS도 아니다.

### 5. 시설투자 일정 primitive 매핑 보강

패치:

```text
src/e2r/research_brain/v4_evidence_extraction_bridge.py

expected_completion_date
contract_start
contract_end
  -> implementation_timeline

facility_investment_amount
facility_investment_to_market_cap
  -> capacity_expansion / implementation_timeline 후보
```

중요:

```text
시설투자 금액이 있다고 direct_company_cash_route나 subsidy_capture로 자동 승격하지 않는다.
투자금액은 회사의 현금 유입이 아니라 보통 현금 유출이다.
```

회귀 테스트:

```text
tests/test_research_brain_v4_evidence_extraction_from_real_document.py
  test_facility_completion_date_becomes_implementation_timeline_claim
```

## 최신 enabled probe 수치

`brain_web_attempt_audit.json`:

```text
verdict: ATTEMPTED_NOT_CUTOVER_READY
planner_run_count: 21
real_provider_success_count: 1
source_task_execution_count: 7
real_document_fetched_count: 6
unique_real_document_fetched_count: 4
brain_source_task_exported_count: 7
brain_source_task_execution_exported_count: 7
brain_evidence_document_exported_count: 4
brain_evidence_anchor_exported_count: 6
brain_raw_assertion_exported_count: 6
accepted_claim_count: 0
unique_accepted_claim_count: 0
brain_score_contribution_exported_count: 0
brain_stagecourt_trace_exported_count: 0
blockers:
  - Research Brain source tasks produced no accepted claims
```

즉:

```text
LLM planner는 호출됐다.
source task도 실행됐다.
DART/CompanyGuide/KIND/KRX 문서도 fetch됐다.
raw/adjudicated claim도 생겼다.
하지만 accepted claim은 0개다.
```

`leaf_artifact_audit.json`:

```text
verdict: FAIL
critical_count: 2
critical_counts:
  web_claimed_but_zero_search_count: 1
  llm_claim_extractor_claimed_but_zero_count: 1
```

해석:

```text
이 /tmp probe는 "실제 official 문서 fetch와 ZIP/CSS 처리" 검증에는 쓸 수 있다.
하지만 Brain/Web full readiness나 전체 leaf artifact PASS로 쓰면 안 된다.
```

대웅 `003090`에 대한 이중 상태:

```text
기존 event-board leaf claim/contribution:
  accepted_claims.jsonl:
    claim_id: CLM-d4ccf4c0a0b39f2b0142
    primitive_id: capacity_expansion
    score_eligible: true

  score_contributions.jsonl:
    SCON-39d486c6eb07fb5f9d98

최신 representative census_stage_status.jsonl:
  base_stage: Stage1
  canonical_stage: 1
  score_scale: NO_SCORE
  event_evidence_score: null
  semantic_guard_status: BLOCKED
  semantic_guard_class: facility_investment_correction_followup_required
  blocked_claim_ids: [CLM-d4ccf4c0a0b39f2b0142]
  blocked_score_contribution_ids: [SCON-39d486c6eb07fb5f9d98]

이번 Brain/Web attempt:
  candidate_event_id: CE-LIVE-DART-003090-20260630801612
  raw/adjudicated assertion: 6개
  accepted Brain claim: 0개
  Brain score contribution: 0개
  Brain StageCourt trace: 0개
```

쉬운 예:

```text
새 채점관은 "이건 일정 연장 정정이라 성장 점수로 못 준다"고 멈췄다.
이전 이벤트 보드 점수표에는 "capacity_expansion 1.5점" 흔적이 남아 있었다.
최신 패치 후에는 그 흔적을 삭제하지 않고 blocked claim으로 남긴 뒤,
대표 상태판 점수에는 0점으로 처리한다.
```

## 왜 accepted claim 0개가 맞을 수 있나

최신 첫 후보는 대웅의 신규시설투자 정정 공시다.

핵심 본문:

```text
정정사유: 종료일 연장
투자기간 종료일:
  정정전 2026-06-30
  정정후 2027-05-31
GMP 승인예정일 기준으로 종료 시점을 판단
일정 변동 시 정정공시 예정
```

이걸 긍정 claim으로 바로 넣으면 안 된다.

쉬운 예:

```text
공장 투자를 한다
  -> 성장 가능성 조사 트리거는 맞다.

공장 투자 종료일이 11개월 밀렸다
  -> Green 근거가 아니라 일정 리스크/추가 확인 대상일 수 있다.
```

따라서 현재 `mapping_not_accepted:REJECTED`는 무조건 버그가 아니다.
이 문서에서 C29의 `volume_growth_visible`, `operating_leverage_visible`, `fcf_quality_score`가 확인되지 않았으면 accepted claim 0개가 맞다.

단, 이 말은 Brain/Web attempt 경로에 한정된다.
기존 event-board leaf에서 같은 대웅 정정공시가 `capacity_expansion`으로 추출된 흔적은 남아 있다.
최신 패치 후 대표 row에서는 이 claim과 contribution이 `blocked_*`로 이동해 점수와 Stage 승격에는 쓰이지 않는다.

## 아직 막힌 것

`brain_web_readiness_gate_audit.json` blockers:

```text
- web/news/Naver acquisition has zero search/fetch rows and no accepted Brain/Web claim
- Brain/Web acquisition mode requires web/news search task rows
- Brain/Web acquisition mode requires fetched full-source web/news documents
- LLM claim extractor has zero attempts and no accepted Brain/Web claim
- web/LLM accepted claim count is zero
- Brain/Web source task rows missing fetched document refs: 1
- Brain/Web StageCourt traces are not promoted into census_stage_status
- brain stage promotion verdict is not PROMOTION_APPLIED: PROMOTION_DISABLED_BY_POLICY
```

해석:

```text
live_official_only probe는 official source fetch를 확인하는 데는 유용하다.
하지만 현재 brain_web target gate는 web/news/Naver + LLM claim extractor까지 요구한다.
따라서 official-only만으로 brain_web gate를 통과하면 안 된다.
```

다음 에이전트가 정해야 할 것:

```text
1. official-only readiness gate와 full Brain/Web gate를 분리할지
2. 아니면 brain_source_acquisition=live_full_bounded에서
   official-first 후 web/news/LLM extractor까지 실제로 실행하게 할지
```

## 다음 패치 순서

1. `live_official_only` gate와 `full_brain_web` gate 이름/조건 분리

   지금은 official-only smoke에도 web/news/Naver blocker가 붙는다.
   이것은 정직하지만, 디버깅 목적과 full readiness 목적이 섞여 있다.

2. 후보 선택을 "accepted 가능성이 있는 official event"로 개선

   지금 첫 후보는 최신 DART URL이라 좋지만, 종료일 연장 정정 공시라 accepted claim이 0개일 수 있다.
   다음 smoke에는 `단일판매·공급계약체결`, `잠정실적`, `수주/계약 금액`처럼 deterministic parser가 이미 받는 event를 우선해야 한다.
   단, 종목명 하드코딩은 금지한다.

   주의:

   ```text
   smoke 디버그용:
     accepted claim이 실제로 생기는 official event를 일부러 골라
     claim -> score -> StageCourt -> promotion 연결을 검증할 수 있다.

   production daily용:
     긍정 이벤트만 고르면 안 된다.
     신규시설투자 정정, 지연, 취소, 리스크 공시도 그대로 후보로 보고
     positive / negative / follow-up required를 의미 판정해야 한다.
   ```

3. OpenDART detail parser 강화

   현재 `투자기간 종료일 정정전/정정후`는 text에는 보이지만,
   structured field로 `expected_completion_date`까지 안정적으로 들어왔는지 계속 검산해야 한다.

4. LLM claim extractor 실가동

   현재 `claim_extractor_runs.jsonl`은 0개다.
   deterministic structured parser만으로는 문장 의미, 일정 지연, 정정 전후 비교를 충분히 판정하기 어렵다.

5. Brain StageCourt promotion strict mode 검증

   accepted Brain claim이 생긴 뒤에만 `brain_stage_promotion_mode=strict`를 켜야 한다.
   accepted claim 0개에서 promotion을 켜면 빈 성적표 승격이 된다.

6. 완료됨: 기존 event-board partial score semantic guard 재검산

   대웅 시설투자 종료일 연장 정정처럼,
   Brain/Web attempt는 보류했지만 기존 event-board leaf가
   `capacity_expansion` 점수를 주던 사례를 막았다.

   예:

   ```text
   신규시설투자 공시
     -> 조사 트리거 가능

   종료일 연장 정정
     -> 바로 capacity_expansion positive score가 아니라
        implementation_timeline delay / follow-up required일 수 있음
   ```

   이 패치는 종목명 예외가 아니라,
   공시 유형, 정정 사유, 정정 전후 날짜, 생산능력/매출/FCF bridge 유무를 보는 semantic guard다.

7. 완료됨: source task execution traceability 보강

   이번 Brain attempt의 `source_task_executions` row는
   nested `source_task`뿐 아니라 top-level에도
   `symbol`, `company_name`, `candidate_event_id`,
   `source_origin`, `source_task_execution_origin`을 채운다.

8. full thesis smoke 실행

   삼성전자/하이닉스는 아직 `PENDING_FULL_THESIS_REFRESH`다.
   daily event-board Stage와 HBM/C06 full thesis Stage를 절대 섞지 말 것.

## 현재 테스트 증거

최신 타깃 테스트:

```text
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_real_source_acquisition \
  tests.test_research_brain_v4_candidate_discovery_live_official \
  tests.test_cutover_candidate_event_purity -v

Ran 15 tests
OK
```

추가 parser / Evidence OS 타깃 테스트:

```text
PYTHONPATH=src python -m unittest \
  tests.test_sources \
  tests.test_research_brain_v4_evidence_extraction_from_real_document \
  tests.test_research_brain_v4_real_source_acquisition -v

Ran 28 tests
OK
```

전체 suite:

```text
PYTHONPATH=src python -m unittest discover -s tests -v

Ran 4942 tests in 170.248s
OK
```

주의:

```text
이 테스트 통과는 현재 워크트리의 회귀 테스트 통과다.
Brain/Web full readiness나 full thesis Stage pass가 됐다는 뜻은 아니다.
canonical output/test_result_artifact.json도 4942개 결과로 재생성했다.
```

## 최종 판정

```text
이번 패치로 개선된 것:
  fixture/cache first planner 문제 완화
  incomplete registry 때문에 실제 종목이 ineligible 되는 문제 완화
  OpenDART document.xml ZIP 바이너리 유출 제거
  OpenDART XML CSS quote 노이즈 제거
  시설투자 일정 primitive 매핑 회귀 테스트 추가

아직 안 된 것:
  Brain/Web accepted claim 생성
  Brain/Web score contribution 생성
  Brain/Web StageCourt trace 생성
  Brain/Web representative census_stage_status 승격
  full thesis verified score/stage
```

한 문장으로:

> 현재는 live official 배관이 실제 문서를 보기 시작한 상태다. 하지만 아직 그 문서를 의미 있는 accepted claim과 운영 Stage로 승격하는 Brain/Web full path는 막혀 있다.
