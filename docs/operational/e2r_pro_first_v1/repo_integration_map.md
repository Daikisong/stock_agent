# E2R Pro-first v1 저장소 통합 지도

## 기준과 범위

- 기준 커밋: `b408b0b6887ea3ca20367a3dc64f543263cd123f`
- 작업 브랜치: `feature/e2r-pro-first-browser-platform-20260822`
- 목적: ChatGPT Pro 웹 Deep Research를 연구 리드로 사용하되, 기존 E2R의 증거·점수·Stage 권한은 그대로 보존한다.
- 금지: 새 점수 엔진, 새 Stage 임계값, 자동 로그인, hidden ChatGPT API, 쿠키·토큰 반출, Tampermonkey 런타임 의존, Pro가 제안한 총점·Stage 복사.

쉽게 말하면 Pro는 “자료를 조사해 구조화하는 선임 연구원”이고, 최종 점수와 Stage를 확정하는 결재선은 기존 E2R 그대로다.

## 전체 연결 경로

```text
KoreaCheapScanner
→ ProCandidateSelector
→ ResearchPacketV1Builder
→ PlaywrightChatGPTWebAdapter
→ 사용자 1회 승인 / exactly-once submit
→ MD-first atomic capture / CAPTURE_COMPLETE
→ ResearchDossierV1Importer
→ ProSourceVerifier
→ EvidenceFact compiler
→ EvidenceGapAssessment / material-gap-only supplemental planner
→ ComponentResearchMemo bridge
→ LLMComponentScoringMemoEngine (7 × 3 Judges)
→ DeterministicScoreAggregator / ResearchCalibratedComponentScorer contract
→ ResearcherStageCourt / AtomicStageCourtV2
→ local dashboard publication
```

## 기존 KRX scanner 재사용

| 기존 자산 | 위치 | Pro-first 사용 방식 |
|---|---|---|
| `KoreaCheapScanner` | `src/e2r/cheap_scan/korea_scanner.py` | morning/evening persisted scheduler가 동일 scanner의 `run()`을 호출한다. 새 scanner는 만들지 않는다. |
| `KoreaCheapScanConfig` | 같은 파일 | `as_of_date`, market, lookback, threshold를 schedule window별 config로 주입한다. |
| `KoreaCheapScanResult` | 같은 파일 | scan run과 candidate receipt의 원천이다. cheap score는 우선순위에만 사용한다. |
| `CheapScanCandidate` | `src/e2r/cheap_scan/models.py` | `production_candidate=true`, `test_injected=false`, `DEEP_RESEARCH`만 Pro 후보로 받는다. |
| `RecommendedNextLayer` | 같은 파일 | `EVENT_SEARCH`를 곧바로 Pro job으로 올리지 않는 경계다. |
| `KoreaCheapScanSources` | `src/e2r/cheap_scan/korea_sources.py` | KRX/OpenDART/KIND/FSC source bundle을 그대로 사용한다. |
| `candidate_event_from_mapping` | `src/e2r/research_brain/candidate_context.py` | 선택된 candidate를 기존 Research Brain event 문맥으로 투영한다. |

`cheap_scan_total_score`는 `full_e2r_score`가 아니다. Candidate receipt에는 최종 점수·Stage가 보이지 않았음을 명시한다.

## Candidate에서 Pro job으로 변환

새 `candidate_selector.py`가 다음 순서를 지킨다.

1. production/deep-research 조건을 검증한다.
2. `symbol + as_of_date + trigger_fingerprint + research_mode` dedupe key를 계산한다.
3. 기존 usable dossier와 source delta를 보고 `FULL_RESEARCH`, `DELTA_RESEARCH`, `NO_MATERIAL_DELTA`를 결정한다.
4. `CandidateSelectionReceipt`를 SQLite 장부와 compact runtime artifact에 함께 기록한다.
5. 선정 시점 payload에서 최종 score·Stage 필드를 제거하고 정적 검사를 건다.

## EvidenceFact schema 재사용

| 기존 자산 | 위치 | 연결 방식 |
|---|---|---|
| `EvidenceFact` | `src/e2r/research_brain/researcher_mode/schemas.py` | 검증을 통과한 Pro fact candidate만 이 canonical schema로 변환한다. |
| `EvidenceDirection` / `EvidenceLifecycle` | 같은 파일 | positive/counter/resolution과 CURRENT/OPEN/RESOLVED/SUPERSEDED를 강제한다. |
| `compile_claim_eligibility_decisions` | `src/e2r/research_brain/scoring/claim_eligibility.py` | source-backed claim의 component/stage eligibility를 기존 규칙으로 판단한다. |
| `MechanismScopeValidator` | `src/e2r/research_brain/scoring/business_mechanism_scope.py` | subject/segment/product/economic mechanism 범위를 재검증한다. |
| `PageFetcher` | `src/e2r/research/page_fetcher.py` | fixture-first, as-of-aware full document fetch와 동일 URL cache를 재사용한다. |
| `PDFTextExtractor` | `src/e2r/research/pdf_text_extractor.py` | PDF source의 실제 본문을 추출한다. snippet은 fact로 승격하지 않는다. |

Pro 보고서 자체는 EvidenceFact가 아니다. URL을 열고, `published_at <= as_of_date`, quote 본문 일치, target/subject/segment/product/currentness가 모두 통과한 row만 변환한다.

## Gap disposition 재사용

`src/e2r/research_brain/researcher_mode/evidence_gap.py`의 다음 authority를 직접 사용한다.

- `EvidenceGapKey`: stable objective/snapshot/source identity
- `EvidenceGapAssessment`: core/corroboration/monitoring 분류와 component effect
- `EvidenceGapClass`: `CORE_SCORE_BLOCKER`, `CORROBORATION_CAP`, `MONITORING_GAP`
- `GapScoreMaterialityAssessment`: score/Stage 경계 materiality
- `EvidenceGapDisposition`: gap별 비차단 disposition과 reopen lineage
- `SemanticNoNewRouteFixpoint`: 같은 snapshot에서 새 route가 없는 상태의 안정적 종결

Pro가 제안한 `STAGE_BOUNDARY_GAP`과 `HARD_BREAK_GAP`은 planner hint일 뿐이다. deterministic gap assessment가 최종 보충 허용 여부를 결정한다. `CORROBORATION_CAP`과 `MONITORING_GAP`은 supplemental search를 시작하지 않는다. Pro dossier 뒤 기존 exhaustive source graph 전체를 재시작하지 않는다.

## Component / Judge / scorer / StageCourt 연결

| 단계 | 기존 authority | Pro-first bridge |
|---|---|---|
| 7 component memo | `ComponentResearchMemo`, `CanonicalResearchDossierBuilder` | Pro component analysis에서 검증된 fact id만 남겨 canonical memo를 만든다. |
| 21 Judge | `LLMComponentScoringMemoEngine`, `AnalystJudge`, `SkepticJudge`, `CalibrationJudge` | `EVIDENCE_ONLY_NO_SEARCH` 문맥으로 7 × 3 역할을 실행한다. provider 실패는 pending이다. |
| deterministic component aggregation | `DeterministicScoreAggregator` | 21개 Judge lineage와 fact/anchor를 검증해 7개 component를 합산한다. |
| calibrated score contract | `ResearchCalibratedComponentScorer` | 기존 assessment/impact/profile totality를 유지한다. Pro 총점은 입력하지 않는다. |
| deterministic Stage | `ResearcherStageCourt`, `AtomicStageCourtV2` | accepted claim, impact, assessment, OPEN hard-break lineage만으로 canonical Stage를 결정한다. |

master goal에 적힌 `component_judge_aggregator.py`는 현재 저장소에 존재하지 않는다. 현행 동등 경로는 다음처럼 분리돼 있으므로 이 두 production 모듈을 재사용한다.

```text
component_scoring_memos.py  # 7 × Analyst/Skeptic/Calibration Judge
score_aggregator.py         # deterministic component/total aggregation
```

## 새로 필요한 계층

```text
src/e2r/pro_first/
├─ durable SQLite job/event/artifact store
├─ optimistic state machine와 no-progress guard
├─ persisted morning/evening scheduler
├─ candidate selector와 full/delta dedupe
├─ ResearchPacketV1 / prompt builder
├─ Playwright browser worker / ChatGPT DOM adapter
├─ approval nonce / exactly-once submit gate
├─ stable completion monitor / MD-first download capture
├─ atomic artifact store / CAPTURE_COMPLETE dispatcher
├─ strict dossier parser/importer
├─ source/quote/date/scope/lifecycle verifier
├─ material-gap-only planner
├─ component/Judge/scorer/Stage bridge
├─ result publisher
└─ FastAPI local dashboard
```

추가 CLI는 stack, scan, job prepare, offline E2E, browser mock E2E, shadow check, readiness 검증을 담당한다. Windows PowerShell script는 dedicated Chrome CDP 실행과 one-command stack 시작만 제공하며 로그인 동작은 하지 않는다.

## 수정하지 않을 기존 계층

- canonical Stage enum과 `StageClassifier` 임계값
- C01~C36 scoring profile과 archetype component max points
- `EvidenceFact`의 source/claim-or-quote lineage 요구조건
- `ResearchCalibratedComponentScorer`의 full-score validity 계약
- `AtomicStageCourtV2`의 accepted claim/impact/assessment 원자성
- Gate 1 exact-gap disposition과 no-new-route fixpoint 의미
- existing KRX/OpenDART/KIND/FSC connector semantics
- 기존 Researcher Mode의 exhaustive/backfill 구현

Pro-first는 기존 exhaustive Researcher Mode를 삭제하지 않는다. 다만 Pro dossier를 받은 production job에서 이를 처음부터 다시 돌리는 호출 경로를 만들지 않는다.

## 권한 경계

```text
ChatGPT Pro
  research lead / structured dossier proposal
  score_authority=false
  stage_authority=false

stock_agent deterministic layers
  source verification
  EvidenceFact acceptance
  gap disposition
  component/Judge lineage validation
  score
  canonical StageCourt
```

예를 들어 Pro가 “82점, Stage 3-Green”이라고 써도 importer가 해당 필드를 권한 입력으로 전달하지 않는다. 검증된 fact와 21개 Judge를 기존 deterministic 경로에 넣어 나온 결과만 게시한다.

## 테스트와 완료 증명

- unit: state machine, scheduler, candidate, packet, capture/import, verifier, gap, scoring bridge, dashboard API
- browser mock: 실제 `PlaywrightChatGPTWebAdapter`가 upload/prepare/approval/submit/monitor/download를 조작
- golden E2E: C06, C17, C24 또는 C28 production handler chain
- reuse: 동일 dossier 재실행 시 submit/supplement/fetch 0과 score/Stage variance 0
- shadow: 로그인된 Chrome에서 prepare까지만 수행하고 `submit_count=0`
- regression: 기존 full suite보다 test count 감소 없음, 새 skip 없음, compileall, static critical 0

