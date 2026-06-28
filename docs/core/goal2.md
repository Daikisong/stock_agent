너는 Daikisong/stock_agent 레포의 E2R 운영 파이프라인을 최종 운영 승인 가능한 상태로 만드는 coding agent다.

이번 작업의 목표는 단순 버그 수정이나 특정 종목 패치가 아니다.

최종 목표는 다음이다.

무료로 접근 가능한 공시, IR, 실적자료, 뉴스, 리포트에서
LLM이 감사 가능한 evidence claim 장부를 작성하고,
코드는 그 claim의 출처, 날짜, 주체, 현재성, 중복, 충돌, source family, lifecycle을 검증한 뒤
deterministic score/stage engine으로 현재 종목의 score와 Stage를 계산하는 운영 파이프라인을 완성하라.

LLM에게 “이 종목 몇 점인가?”를 묻지 마라.
LLM에게 “이 문서에서 점수표에 들어갈 수 있는 claim은 무엇이고, 왜 들어갈 수 있거나 없는가?”를 쓰게 하라.

가장 중요한 원칙:

1. parser keyword는 score/risk를 직접 만들 수 없다.
2. LLM raw output은 score/risk를 직접 만들 수 없다.
3. EvidenceMention은 score/risk에 직접 들어갈 수 없다.
4. nonzero ScoreContribution은 반드시 accepted, current, target-direct, source-backed claim_id를 가져야 한다.
5. hard break는 반드시 issuer-scoped, current OPEN, material, source-quorum-passed claim_id를 가져야 한다.
6. score-gap loop는 append-only다. 기존 claim ledger를 조용히 삭제하거나 전체 agent_extracted_fields를 다시 작성하지 마라.
7. UNKNOWN은 PRESENT도 ABSENT도 아니다.
8. 오래된 미확인 risk는 현재 penalty가 아니라 follow-up task다.
9. source_proxy_only / evidence_url_pending / snippet-only / LLM-only inference는 production score contribution이 될 수 없다.
10. 특정 종목명, 특정 기사, 특정 한국어 키워드 예외로 문제를 해결하지 마라.

이번 작업은 레포 전체를 고쳐도 된다. 단, weight와 Stage threshold는 바꾸지 마라.
문제는 가중치가 아니라 evidence → claim → primitive → score 경로의 신뢰성이다.

================================================================================
0. 현재 실패 결과 폐기 및 안전장치
================================================================================

먼저 기존 잘못된 live 결과를 deprecated 처리하라.

다음 결과는 운영 검증 결과로 쓰면 안 된다.

- 삼성전자 63점대 / 4C
- SK하이닉스 63점대 / 3-Red
- 삼성전자 90점대 Yellow와 후속 63점대 결과를 같은 전후 비교로 취급한 기록

폐기 사유를 명시하라.

- 월덱스 기사 “감사의견 적정”이 삼성전자 accounting/trust risk로 오귀속됨
- 정상 감사의견 문구가 risk로 들어감
- score-gap round_limit_reached인데 score_valid=true로 확정됨
- 90점대 실행과 63점대 실행은 commit/config/query/corpus/fetch policy가 달랐음
- Green gate 실패는 점수를 깎지 않는데, 실제 점수가 바뀌었으므로 입력 field/risk signal이 변한 것임

필수 산출물:

docs/operational/deprecated_live_results_2026-06-21.md

내용:
- deprecated result path
- symbol
- old score/stage
- 폐기 이유
- 다시 사용할 수 없는 이유
- 대체 검증 명령

================================================================================
1. Legacy parser → score/risk 직접 경로 완전 차단
================================================================================

현재 parser나 web_research_runner 안에서 다음 같은 field를 직접 만드는 경로를 전수조사하라.

예:
- accounting_or_trust_issue
- contract_cancelled_or_delayed
- customer_loss
- qualification_failure
- dilution_cb_risk
- legal_or_contract_risk
- hard_break
- any risk boolean
- any primitive boolean
- any score component

parser는 앞으로 EvidenceMention까지만 만들 수 있다.

EvidenceMention 예:

{
  "evidence_id": "...",
  "source_url": "...",
  "source_title": "...",
  "published_at": "...",
  "fetched_at": "...",
  "raw_text_span": "...",
  "mentioned_entities": [...],
  "possible_dates": [...],
  "possible_numbers": [...],
  "parser_notes": [...]
}

금지:
- EvidenceMention에서 FeatureInput risk field 직접 생성
- EvidenceMention에서 ScoreContribution 직접 생성
- keyword match로 hard break 생성
- keyword match로 accounting/trust risk 생성
- keyword match로 contract/customer/revenue primitive 생성

필수 구현:
- legacy_parser_field_quarantine layer
- legacy fields는 diagnostics 또는 mention notes까지만 보존
- old parser fields가 score/risk로 흘러가면 test failure

필수 테스트:
- “감사의견은 적정” → accounting hard break 0
- 타사 감사의견 + target company 고객사 언급 → target risk 0
- “적정이지만 계속기업 불확실성 강조” → normal이 아니라 mixed/needs adjudication
- “계약하지 않았다” → contract=true 금지
- “공급 예정”과 “공급계약 체결” 구분
- “업계 수요 증가”와 “대상 회사 수주” 구분
- “고객사 CAPA 확대”와 “대상 회사 CAPA 확대” 구분

완료 증거:
- parser keyword → score/risk direct path count = 0
- pytest에 legacy quarantine regression 포함
- run log에 parser_mentions_count와 score_eligible_from_mentions_count=0 출력

================================================================================
2. Evidence OS v2 데이터 모델 정리
================================================================================

다음 객체를 명확히 분리하라.

EvidenceDocument:
- document_id
- canonical_url
- source_type
- source_family
- original_source
- canonical_source
- content_hash
- published_at
- available_at
- fetched_at
- observed_at
- revision_id
- parser_version
- source_proxy_only
- snippet_only
- evidence_url_pending
- source_lineage_id
- underlying_event_id

EvidenceAnchor:
- anchor_id
- document_id
- anchor_type
  - TEXT_SPAN
  - TABLE_CELL
  - XBRL_FACT
  - API_RECORD
  - PDF_PAGE_REGION
- locator
- exact_text
- normalized_value
- anchor_hash
- anchor_verified

RawAssertion:
- assertion_id
- evidence_anchor_id
- subject_entity_id
- subject_name
- predicate
- object_entity_ids
- value
- unit
- polarity
  - POSITIVE
  - NEGATIVE
  - NORMAL
  - MIXED
  - CONDITIONAL
- modality
  - CONFIRMED
  - EXPECTED
  - GUIDED
  - RUMORED
  - DENIED
- event_date
- effective_start
- effective_end
- exact_quote
- extraction_method
- llm_prompt_hash
- extraction_schema_version

TargetAdjudication:
- assertion_id
- target_entity_id
- relation_to_target
  - DIRECT
  - SUBSIDIARY
  - PARENT
  - CUSTOMER
  - SUPPLIER
  - PEER
  - INDUSTRY
  - UNRELATED
  - UNKNOWN
- directness
  - DIRECT_TARGET
  - INDIRECT_RELEVANT
  - CONTEXT_ONLY
  - NOT_APPLICABLE
- target_scope_status
- semantic_verification_status
  - PASS
  - FAIL
  - NEEDS_REVIEW
- adjudication_reason

TemporalAdjudication:
- assertion_id
- as_of_date
- event_date_status
- source_date_status
- temporal_status
  - CURRENT
  - HISTORICAL
  - EXPIRED
  - RESOLVED
  - SUPERSEDED
  - OPEN
  - UNKNOWN
- last_confirmed_at
- superseded_by_claim_ids
- resolved_by_claim_ids
- followup_required
- followup_reason

PrimitiveMappingProposal:
- assertion_id
- archetype_id
- candidate_primitive_id
- direction
  - SUPPORT
  - COUNTER
  - GUARD
  - NEUTRAL
- mapping_status
  - PROPOSED
  - ACCEPTED
  - REJECTED
  - CONTRADICTED
- mapping_reason
- contract_rule_id

AdmissibleClaim:
- claim_id
- assertion_id
- evidence_anchor_id
- target_entity_id
- archetype_id
- primitive_id
- support_or_counter
- score_eligibility_status
  - ELIGIBLE
  - NOT_ELIGIBLE
  - PENDING
- not_eligible_reason
- source_quorum_status
- contradiction_status
- current_score_eligible

중요:
LLM은 verified, current_score_eligible, score, stage, hard_break를 최종값으로 쓰면 안 된다.
LLM은 assertion과 판단 재료를 쓴다.
코드가 eligibility를 파생한다.

current_score_eligible = true 조건:

- anchor_verified = true
- source_url 또는 API/XBRL/table anchor 존재
- source date verified
- event_date <= as_of_date
- target directness가 DIRECT_TARGET 또는 contract가 허용한 직접 관계
- temporal_status가 CURRENT 또는 OPEN
- polarity와 primitive 방향이 일치
- mapping_status = ACCEPTED
- source_proxy_only = false
- snippet_only = false
- evidence_url_pending = false
- contradiction resolved
- source quorum passed
- future leakage 없음

================================================================================
3. Entity Registry / Target Scope Resolver
================================================================================

issuer_scoped boolean 하나로 처리하지 마라.

EntityRegistry를 구현하거나 기존 corp_code/ticker mapping을 강화하라.

필수 지원:
- KRX ticker
- DART corp_code
- 한글 법인명
- 영문명
- 과거 상호
- 자회사/모회사
- 고객사/공급사/파트너
- 기사 내 subject와 검색 대상 target 분리

월덱스 fixture:

문서:
- subject: 월덱스
- related entity: 삼성전자, relation=major_customer 또는 customer mention
- assertion: 월덱스 감사의견 적정
- polarity: NORMAL
- target: 삼성전자

기대 결과:
- relation_to_target != DIRECT
- directness = NOT_APPLICABLE 또는 CONTEXT_ONLY
- primitive mapping rejected
- current_score_eligible=false
- Samsung accounting risk score = 0
- hard_break=false
- Stage4C 불가

삼성전자 자체 과거 risk fixture:

문서:
- subject: 삼성전자
- event_date: 2020
- polarity: NEGATIVE
- as_of_date: 2026-06-21

후속 최신 공시가 없으면:
- temporal_status=UNKNOWN 또는 HISTORICAL
- current_score_eligible=false
- risk score=0
- followup_required=true

후속 최신 감사보고서/정정/해소 claim이 있으면:
- temporal_status=RESOLVED 또는 SUPERSEDED
- risk score=0

현재 OPEN 공식 claim이 있으면:
- temporal_status=OPEN
- source quorum passed
- risk score 반영 가능

================================================================================
4. Contract-blind LLM Claim Extractor
================================================================================

LLM Extractor는 evidence contract, missing primitive, current score gap을 보지 않게 하라.

입력:
- target company identity/aliases
- as_of_date
- EvidenceDocument metadata
- document text
- optional source context

금지 입력:
- current score
- failed green gates
- missing primitive
- desired primitive
- score component
- stage threshold
- “이 문서로 Green을 열 수 있는가?” 같은 질문

출력:
- document 안의 factual assertion list
- subject
- predicate
- value
- polarity
- modality
- event_date
- effective period
- exact quote
- related entities
- uncertainty reason

그 뒤 별도 단계로 나눠라.

A. Anchor Validator
- quote가 원문에 실제 존재하는지 substring/span/hash로 검증
- PDF/table/API anchor도 지원
- LLM의 “quote”를 코드가 검증

B. Target/Temporal Adjudicator
- 이 assertion이 target company에 직접 귀속되는지 판단
- 현재 as_of_date에도 살아 있는지 판단
- 해결/대체/만료 여부 판단

C. Primitive Mapper
- 검증된 assertion만 evidence contract에 매핑
- mapping proposal과 accepted mapping 분리

D. Follow-up Planner
- UNKNOWN/PENDING claim만 보고 다음 source task 제안

================================================================================
5. Evidence Contract v2 전 아키타입 확장
================================================================================

전 C01~C36 canonical archetype에 Evidence Contract v2를 만든다.

각 contract는 단순 primitive list가 아니라 다음을 포함해야 한다.

- canonical_archetype_id
- large_sector_id
- description
- positive primitives
- green required primitives
- yellow required primitives
- stage2 actionable primitives
- guard primitives
- hard-break primitives
- false-positive patterns
- any/all/k-of-n gate logic
- alternative primitive aliases
- source family priority
- source quorum
- freshness policy
- expiry rule
- supersession rule
- guard mode
  - block_if_present
  - must_explicitly_clear
  - search_exhaustion_clearable
- aggregation rule
- duplicate/syndication rule
- follow-up source policy
- max query/fetch budget per primitive
- stop condition per primitive

중요:
아키타입별 ontology는 필요하다.
하지만 종목별 if문, 고정 검색어만으로 된 contract, 특정 키워드 예외는 금지다.

좋은 구조:
contract = registry.get(archetype_id)
source_task = source_router.plan(contract, primitive_gap, current_claims)

나쁜 구조:
if symbol == "005930": ...
if "감사의견" in text: ...
if archetype == C06: query = "{company} HBM 장기공급계약 선수금"

검색어는 LLM Follow-up Planner가 현재 claim ledger와 missing primitive를 보고 만들 수 있다.
하지만 Source Router가 공식 source 우선순위, budget, allowed domains, dedupe, stop rule을 강제한다.

================================================================================
6. Source Router / Acquisition Budget
================================================================================

네이버 일반검색을 기본 수집기가 아니라 fallback으로 강등하라.

Source priority:

1. Official structured
   - OpenDART
   - KIND
   - KRX
   - data.go.kr
   - SEC EDGAR
   - XBRL/API records

2. Issuer official
   - company IR
   - earnings release
   - conference call material
   - company newsroom
   - annual/quarterly report PDF

3. Domain-specific official
   - FDA/EMA/MFDS/ClinicalTrials for bio
   - customer official announcement
   - exchange/regulator notices
   - government project/tender sites

4. Public research / reports
   - legally accessible broker PDF
   - industry association data
   - company-hosted PDFs

5. Trusted news
   - Reuters / Yonhap / major media / specialist industry media

6. General search / Naver
   - discovery/follow-up hint only unless full article, date, quote, target scope verified

금지:
- top_results=None
- score_gap_query_retry_max=None
- primitive task without max_fetches
- fetch-before-dedupe
- unbounded page fetch
- snippet-only score evidence

SourceTask schema:

{
  "task_id": "...",
  "target_entity_id": "...",
  "archetype_id": "...",
  "primitive_gap": "...",
  "source_classes": [...],
  "allowed_domains": [...],
  "date_window": {...},
  "required_source_tier": "...",
  "max_queries": 3,
  "max_candidates": 20,
  "max_fetches": 5,
  "stop_condition": {
    "accepted_claim_count": 1,
    "counter_claim_check_done": true
  },
  "fallback_policy": "official_to_trusted_news_to_general_search",
  "web_search_allowed": true_or_false
}

예:
- FCF gap은 DART/XBRL/API only, web_search_allowed=false
- supply contract gap은 DART/KIND/company IR 우선
- HBM qualification은 issuer IR/customer official/trusted news
- ARR/RPO/renewal은 사업보고서/IR/earnings call/public broker PDF
- bio endpoint/regulatory는 company disclosure/regulator/clinical registry
- commodity spread는 company report/price source/realized margin/FCF bridge

================================================================================
7. Historical Research Backtrace / Fixture Build
================================================================================

기존 연구자료는 production score 정답이 아니다.
운영 schema, evidence contract, replay fixture를 만드는 재료다.

전 아키타입별로 과거 연구자료를 역추적하라.

각 canonical_archetype_id별로 다음을 만든다.

A. Research Corpus Inventory
- research_file
- canonical_archetype_id
- large_sector_id
- cases
- positive/counterexample/4B/4C count
- source_proxy_only count
- evidence_url_pending count
- actual URL count
- production-ready count
- fixture-usable count
- source-gap count

B. Source Route Matrix
- positive case는 어떤 source로 Green/Yellow가 됐는가
- guard case는 어떤 source로 4B/4C가 됐는가
- source가 실제 URL인지 proxy인지 구분
- source_proxy_only면 production fixture 정답으로 쓰지 말고 contract 설계 참고로만 사용
- 어떤 primitive가 필요했는지 추출
- 어떤 bridge가 없으면 Stage를 막아야 하는지 추출
- 무료 source로 운영 재현 가능한지 표시

C. Replay Fixture Set
각 C01~C36에 대해 최소 다음 fixture를 만든다.

- positive fixture
- guard fixture
- wrong-subject fixture
- old-risk-resolved fixture
- current-hard-break fixture
- source-missing pending fixture

실제 URL-backed 사례가 부족한 archetype은 source_gap으로 명시하라.
source_gap을 숨기고 synthetic success로 처리하지 마라.

과거 연구 예시 기준:
- C06은 실제 URL-backed 사례가 많다. source_proxy_only_count=0, evidence_url_pending_count=0인 C06 research는 golden replay 후보로 우선 사용한다.
- C08은 직접 URL이 붙은 테스트소켓/고객품질 사례가 있으므로 replay 후보로 사용 가능하다.
- C15/C17/C24/C28 중 source_proxy_only/evidence_url_pending이 붙은 자료는 production fixture 정답이 아니라 ontology/contract 설계 자료로만 사용한다.
- C07처럼 source_proxy_only=true/evidence_url_pending=true/batch_reverification_required=true인 자료는 runtime promotion fixture가 아니라 pending/source-gap fixture로 분류한다.
- C23/C24 바이오 자료는 approval/event-only와 commercialization/partner/funding bridge를 분리한다.

중요:
과거 연구 MD에는 미래 MFE/MAE와 outcome label이 들어 있다.
Evidence extraction fixture에는 미래 결과를 넣지 마라.
LLM extraction에는 당시 원문 snapshot/기사/공시만 제공하라.
MFE/MAE는 replay expected outcome 검증 단계에서만 사용한다.

================================================================================
8. Append-only Claim Ledger / Score-gap 재조사
================================================================================

score-gap loop를 완전히 바꿔라.

나쁜 방식:
- 1차 점수 계산
- gap search
- LLM이 전체 agent_extracted_fields 재작성
- 기존 visibility/bottleneck/risk 판단까지 바뀜
- 90점이 60점으로 흔들림

좋은 방식:
- 기존 accepted claim ledger freeze
- missing material primitive만 SourceTask 생성
- 새 claim append
- 기존 claim을 무효화하려면 invalidation event append
- supersession/contradiction/resolution edge append
- 영향받은 primitive/component만 재계산
- 모든 score delta를 claim delta로 설명

Ledger는 immutable이어야 한다.
claim row를 수정하지 말고 relation/event row를 append하라.

필수 relation:
- CONFIRMS
- UPDATES
- SUPERSEDES
- RESOLVES
- CONTRADICTS
- DUPLICATES
- REFERS_TO
- INVALIDATES

Claim ID는 deterministic해야 한다.

claim_id = hash(
  document_hash,
  anchor_locator,
  normalized_subject_entity_id,
  normalized_predicate,
  normalized_value,
  extraction_schema_version
)

같은 문서를 다시 처리해도 claim이 증식하면 안 된다.

================================================================================
9. Score Contribution Ledger / Score Validity
================================================================================

ScoreContribution schema:

{
  "component_key": "...",
  "criterion_id": "...",
  "raw_points": 0.0,
  "max_points": 20.0,
  "support_claim_ids": [...],
  "counter_claim_ids": [...],
  "cap_reason": "...",
  "source_tier_cap": "...",
  "freshness_cap": "...",
  "contradiction_cap": "...",
  "target_scope_cap": "...",
  "evidence_family_cap": "...",
  "rationale": "..."
}

규칙:
- raw_points != 0이면 support_claim_ids 필수
- support_claim_ids 안의 모든 claim은 current_score_eligible=true여야 함
- source_proxy_only/snippet_only/pending claim은 점수 불가
- orphan score count는 항상 0이어야 함
- LLM confidence는 점수 가중치로 쓰지 말고 review priority로만 사용

provisional_score, verified_score, score_interval을 분리하라.

- provisional_score: 미검증/snippet/LLM candidate를 포함한 조사 우선순위용
- verified_score: admissible claim만 사용한 운영 점수
- score_interval: unresolved material gaps를 반영한 lower/upper bound

Stage는 verified_score와 deterministic gates만 사용한다.

score_valid status:

- FINAL
- FINAL_WITH_NONMATERIAL_GAPS
- PENDING_MATERIAL_GAPS
- INVALID_EVIDENCE
- PROVIDER_FAILURE
- NON_COMPARABLE_RUN

round_limit_reached만으로 무조건 invalid는 아니다.
하지만 unresolved gap이 Stage/score 경계에 material하면 pending이어야 한다.

예:
verified_score=63, unresolved gap max impact +1, hard-break 없음
→ FINAL_WITH_NONMATERIAL_GAPS 가능

verified_score=84, unresolved gap max impact +8, Green 경계 열림
→ PENDING_MATERIAL_GAPS

unresolved hard-break candidate 존재
→ Stage4 확정 금지, PENDING_MATERIAL_GAPS

provider failure 때문에 핵심 source를 못 봄
→ PROVIDER_FAILURE 또는 PENDING

================================================================================
10. Stage Court 재설계
================================================================================

Stage를 하나의 string으로만 처리하지 말고 세 축으로 분리하라.

base_stage:
- Stage0
- Stage1
- Stage2
- Stage2-Actionable
- Stage3-Yellow
- Stage3-Green
- Stage3-Red
- Reject

investigation_status:
- COMPLETE
- PENDING
- EXHAUSTED
- CONTRADICTED
- PROVIDER_FAILED
- INVALID_EVIDENCE

transition_overlay:
- NONE
- 4A
- 4B
- 4C

4C는 기존 thesis가 있고, current OPEN hard-break claim이 있을 때만 transition_overlay로 붙여라.
처음 평가하는 종목에 current hard break가 있으면 4C 전이가 아니라 Reject/Red일 수 있다.

hard break 조건:
- direct target
- negative
- current OPEN
- material
- source anchor verified
- source quorum satisfied
- contradiction resolved
- evidence contract hard-break primitive에 매핑됨

qualification delay는 기본적으로 4B/watch 또는 execution risk다.
confirmed cancellation, permanent customer loss, current unresolved accounting/trust break만 hard 4C 후보가 된다.

================================================================================
11. Run Fingerprint / Score Delta Audit
================================================================================

모든 run은 다음 fingerprint를 남겨라.

- commit_sha
- config_hash
- as_of_date
- source_corpus_hash
- query_set_hash
- cache_snapshot_id
- llm_model
- llm_prompt_hash
- llm_schema_version
- scoring_schema_version
- stage_schema_version
- evidence_contract_version
- source_router_version

비교 등급:

A. EXACT_REPLAY
- code/config/model/corpus/query/cache 모두 동일

B. EVIDENCE_UPDATE
- code/scoring/stage 동일, corpus만 변경

C. EXTRACTION_UPDATE
- corpus 동일, prompt/schema/model 변경

D. SCORING_UPDATE
- evidence 동일, weight/stage schema 변경

E. NON_COMPARABLE
- 여러 축이 동시에 변경되어 분리 불가

90점 실행과 63점 실행 같은 경우는 NON_COMPARABLE이어야 한다.

ScoreDeltaLedger:

모든 component delta는 claim delta로 설명되어야 한다.
5점 이상만이 아니라 0보다 큰 모든 delta가 설명돼야 한다.

{
  "component": "earnings_visibility",
  "before": 19.0,
  "after": 11.0,
  "delta": -8.0,
  "comparison_class": "EVIDENCE_UPDATE",
  "added_claim_ids": [],
  "removed_claim_ids": [],
  "superseded_claim_ids": ["..."],
  "contradicted_claim_ids": [],
  "invalidation_event_ids": ["..."],
  "reason": "source date unverifiable"
}

규칙:
- delta > 0 또는 delta < 0인데 claim delta가 없으면 audit failure
- 5점 이상 delta는 critical audit event
- NON_COMPARABLE run끼리는 “점수 개선/악화”라고 말하지 마라

================================================================================
12. Source lineage / duplicate / syndication 처리
================================================================================

URL 개수와 evidence family 개수를 구분하라.

필수 필드:
- canonical_document_id
- original_source_id
- syndication_parent_id
- underlying_event_id
- source_lineage_id
- source_family
- independent_origin_count

동일 Reuters 기사 재배포 20개는 evidence family 1개다.
회사 IR을 그대로 인용한 기사 5개도 독립 source family가 아니다.
Green evidence family diversity는 URL 수가 아니라 independent origin 수로 계산하라.

테스트:
- Reuters 원문 + 네이버 재배포 + 블로그 인용 → independent source family 1
- 회사 IR + 기사 인용 → source family 계산에서 company IR origin 우선
- 같은 URL 수정본 → revision_id와 content_hash로 분리

================================================================================
13. 전 섹터 / 전 아키타입 운영 검증
================================================================================

운영 승인 전 반드시 전 섹터를 돌려라.

레포에서 large_sector_id와 canonical_archetype_id 목록을 자동 추출하라.
하드코딩하지 말고 configs/docs/index에서 발견하라.

최소 검증 단위:

A. Archetype Replay Matrix
C01~C36 전체에 대해 다음 status를 채워라.

- has_evidence_contract_v2
- has_positive_fixture
- has_guard_fixture
- has_wrong_subject_fixture
- has_old_risk_resolved_fixture
- has_current_hard_break_fixture
- has_source_missing_pending_fixture
- has_url_backed_fixture
- has_source_proxy_only_fixture
- has_runtime_source_route
- fixture_pass_count
- fixture_fail_count
- source_gap_reason

B. Sector Smoke Matrix
각 large_sector_id별로 최소 3개 canonical archetype을 실제 실행하라.

각 sector에서:
- positive/Actionable 후보 1개
- guard/false-positive 후보 1개
- source-missing/pending 후보 1개

가능하면 live가 아니라 frozen corpus replay부터 수행하라.
그 다음 bounded live smoke를 수행하라.

C. Cross-sector adversarial tests
모든 아키타입 공통 adversarial suite를 통과해야 한다.

필수 adversarial cases:

1. 타사 정상 감사의견 + target 고객사 언급
2. target 자체 과거 문제 + 최신 해소 공시
3. target 자체 과거 문제 + 현재 OPEN 공식 확인
4. 자회사 문제와 모회사 문제 구분
5. 고객사 CAPA와 공급사 CAPA 구분
6. 업계 수요와 issuer 주문 구분
7. 주장과 회사 반박이 동시에 존재
8. “계약하지 않았다” 부정문
9. “적정이지만 계속기업 불확실성” 혼합문
10. 전망·가이던스와 실제 실적 구분
11. 기사 작성일과 사건 발생일 구분
12. 최신 기사가 오래된 사건을 회고하는 경우
13. 정정·철회된 공시
14. 동일 기사 재배포 20개
15. URL은 같지만 문서가 수정된 경우
16. 정확한 quote를 변조한 경우
17. snippet만 있고 원문 fetch 실패
18. as_of_date 이후 문서
19. 같은 문서를 두 번 처리해도 claim이 증식하지 않음
20. LLM이 새 primitive 이름을 임의 생성하는 경우
21. source_proxy_only research row가 운영 점수로 들어가지 않음
22. current hard break가 없는 과거 negative claim
23. positive claim이 만료·supersede된 경우
24. prompt injection 문구가 포함된 웹페이지
25. generic theme headline이 issuer-level primitive로 들어가는 경우
26. broker report snippet만 있고 PDF 원문이 없는 경우
27. FCF gap을 네이버 검색으로 해결하려는 경우
28. DART로 해결 가능한 gap에서 general web fetch가 발생하는 경우

================================================================================
14. Historical Research 재검증 기준
================================================================================

과거 연구자료를 다시 찾아보고 각 아키타입별로 운영 재현성을 평가하라.

Research artifact classification:

A. URL-backed replay-ready
- source_proxy_only=false
- evidence_url_pending=false
- source URL 있음
- as-of source와 trigger date 정합
- 원문 fetch 가능 또는 snapshot 가능
- quote/anchor 생성 가능
- runtime primitive로 매핑 가능

B. URL-backed but repair needed
- URL은 있으나 원문 snapshot/quote/date anchor 미완성

C. Source-proxy ontology only
- source_proxy_only=true 또는 evidence_url_pending=true
- production score fixture로 사용 금지
- evidence contract 설계, false-positive pattern, source task 설계에만 사용

D. Price-path only / future-leakage risk
- MFE/MAE 중심
- 운영 evidence fixture로 사용 금지
- guardrail 설계 참고만 가능

반드시 각 연구 row를 이 네 등급으로 분류하라.

C06 예시:
- SK하이닉스 HBM sold-out / HBM revenue mix / 삼성 qualification lag 등 실제 URL-backed C06 rows는 golden replay 후보
- 단, 삼성 qualification lag는 4B/watch와 current hard break를 구분해야 함
- old claim은 현재 as_of_date 재평가에 그대로 들어가면 안 됨

C08 예시:
- test socket/customer quality/direct order/profile-only 구분
- named customer/order는 Actionable 가능
- product profile/award만으로 Green 금지

C15/C17 예시:
- raw commodity weather와 issuer-level pass-through/margin/FCF bridge 분리
- realized margin bridge 없는 spread narrative는 Green 금지

C23/C24 예시:
- approval-only / endpoint-only / trial headline은 Green 금지
- partner, regulatory path, commercialization, funding runway bridge 필요
- CRL/rejection은 current hard break로 볼 수 있으나 resubmission/reapproval/reopen lifecycle 확인 필요

C28 예시:
- software/security keyword만으로 Stage2/Green 금지
- ARR/RPO/renewal/retention/churn/margin bridge 필요

C29 예시:
- auto parts vocabulary만으로 promotion 금지
- volume/platform mix/utilization/margin/FCF bridge 필요

================================================================================
15. 운영형 Candidate Discovery 검증
================================================================================

현재 목표는 과거 연구가 아니라 현재 좋은 종목을 찾는 운영 파이프라인이다.

따라서 targeted smoke만으로 완료하지 마라.

필수 운영 흐름:

1. 전 시장 structured scan
   - DART/KIND/KRX/CompanyGuide/price/volume/relative strength
   - 신규 공시, 계약, 실적 변동, 시설투자, 컨센서스 변화, 리스크 이벤트 감지

2. CandidateEvent 생성
   - symbol
   - company
   - event_date
   - event_type
   - source
   - magnitude
   - freshness
   - candidate_reason

3. LLM archetype hypothesis
   - primary_archetype
   - secondary_archetype
   - positive thesis
   - counter thesis
   - required primitives

4. Source Router로 primitive별 조사
   - 공식 source 우선
   - bounded budget
   - stop-on-resolution

5. Evidence claim ledger
6. verified score/stage
7. pending/exhausted/complete 상태 출력

테스트:
- 종목을 직접 지정하지 않아도 후보가 생성되어야 한다.
- 후보 생성 이유가 구체적 신규 사건이어야 한다.
- 무작정 네이버에서 수천 건 fetch하면 실패다.
- DART/IR/CompanyGuide로 해결 가능한 gap은 general search를 호출하지 않아야 한다.
- 각 sector에서 최소 3개 이상 CandidateEvent가 생성되거나, source/provider gap을 명시해야 한다.

운영 기본 fetch budget:
- initial general web query per candidate <= 5
- max candidates per query <= 10
- max page fetch per primitive <= 5
- max page fetch per candidate <= 40
- score-gap max material primitive tasks <= 5
- source dedupe before fetch 필수
- top_results=None 금지
- retry_max=None 금지

================================================================================
16. Live Smoke / Bounded Batch 검증
================================================================================

완료 전 다음 실행을 수행하라.

A. Frozen replay
- 모든 fixture는 network 없이 deterministic하게 돌아야 한다.
- 동일 commit/config/corpus로 3회 실행 시 claim_id, score, stage 동일해야 한다.

B. Bounded live smoke
- 각 large sector에서 최소 3개 후보
- 전체 최소 30개 종목
- 가능하면 C01~C36 중 최소 1개씩 cover
- source budget 제한
- live page fetch 제한
- provider error 발생 시 pending/provider_failed로 처리

C. Known regression live smoke
- 삼성전자 005930
- SK하이닉스 000660
- 월덱스 wrong-subject fixture
- C06 SK하이닉스 URL-backed positive
- C06 삼성 qualification lag 4B/watch fixture
- C08 direct customer/order fixture
- C15 pass-through vs raw commodity false positive fixture
- C23/C24 bio approval/event hard-break/reopen fixture
- C28 software/security retention bridge fixture
- C29 mobility volume/margin fixture

D. Production discovery dry-run
- targeted_smoke_only=false
- actual candidate discovery path 사용
- top 후보 20~50개
- 각 후보의 candidate_event, archetype hypothesis, source tasks, verified_score, provisional_score, score_interval, stage 출력

================================================================================
17. 운영 Report / Audit Artifacts
================================================================================

다음 파일들을 반드시 생성하라.

docs/operational/evidence_os_v2_acceptance_report.md
docs/operational/evidence_os_v2_sector_matrix.json
docs/operational/evidence_os_v2_archetype_matrix.json
docs/operational/evidence_os_v2_replay_results.json
docs/operational/evidence_os_v2_live_smoke_results.json
docs/operational/evidence_os_v2_source_gap_inventory.json
docs/operational/evidence_os_v2_score_delta_audit.json
docs/operational/evidence_os_v2_legacy_quarantine_audit.json
docs/operational/evidence_os_v2_known_regressions.md

각 report에는 다음을 포함하라.

- commit_sha
- test command
- pass/fail/skip count
- replay corpus hash
- source corpus hash
- evidence contract version
- scoring schema version
- stage schema version
- LLM prompt/schema hash
- all failures
- unresolved source gaps
- production cutover decision

운영 run output에는 항상 다음 필드를 포함하라.

- raw_score
- provisional_score
- verified_score
- score_interval_lower
- score_interval_upper
- score_valid_status
- base_stage
- investigation_status
- transition_overlay
- stage_blockers
- failed_green_gates
- claim_backed_score_ratio
- orphan_score_count
- unresolved_contradiction_count
- future_leakage_count
- source_family_diversity
- accepted_claim_count
- pending_claim_count
- rejected_claim_count
- source_proxy_contribution_count
- snippet_only_contribution_count
- hard_break_claim_ids
- score_delta_ledger_path
- run_fingerprint
- comparison_class

================================================================================
18. 필수 pytest / 테스트 파일
================================================================================

최소 다음 테스트 파일 또는 동등한 테스트를 추가하라.

tests/test_evidence_os_legacy_quarantine.py
tests/test_evidence_os_entity_scope.py
tests/test_evidence_os_temporal_lifecycle.py
tests/test_evidence_os_anchor_validation.py
tests/test_evidence_os_primitive_mapping.py
tests/test_evidence_os_score_contribution.py
tests/test_evidence_os_score_delta_audit.py
tests/test_evidence_os_stage_court.py
tests/test_evidence_os_source_router_budget.py
tests/test_evidence_os_source_lineage_dedupe.py
tests/test_evidence_os_replay_fixtures_all_archetypes.py
tests/test_evidence_os_adversarial_global.py
tests/test_evidence_os_material_gap_score_validity.py
tests/test_evidence_os_run_fingerprint.py
tests/test_evidence_os_prompt_injection.py
tests/test_operational_discovery_pipeline.py

필수 assertion:

- parser keyword direct score/risk path count == 0
- nonzero ScoreContribution orphan count == 0
- source_proxy_only production contribution count == 0
- snippet_only production contribution count == 0
- hard break without current OPEN direct claim count == 0
- old unresolved risk penalty count == 0
- wrong-subject risk penalty count == 0
- future leakage contribution count == 0
- score delta without claim delta count == 0
- unbounded query/fetch config count == 0
- repeated frozen replay score/stage variance == 0
- same document duplicate claim growth == 0

================================================================================
19. Cutover 규칙
================================================================================

새 Evidence OS v2가 모든 acceptance를 통과하기 전에는 legacy parser→score 경로를 제거하지 마라.

단계:
1. dual-run mode
   - old pipeline output
   - Evidence OS v2 output
   - production decision은 v2가 아니라 diagnostics unless acceptance pass

2. quarantine mode
   - old parser fields는 mention-only
   - old score path는 diagnostics
   - v2 score가 verified_score로 출력

3. acceptance pass
   - all tests pass
   - all replay pass or source_gap documented
   - live smoke bounded pass
   - score delta audit clean
   - sector matrix complete

4. default cutover
   - v2 becomes default
   - legacy score path removed or behind debug flag
   - parser keyword direct risk impossible by construction

중요:
중간 단계에서 “완료”라고 보고하지 마라.
구현 완료와 운영 승인 완료를 분리하라.

상태 라벨:
- IMPLEMENTATION_MERGED
- REPLAY_PASS
- SECTOR_SMOKE_PASS
- LIVE_SMOKE_PASS
- ACCEPTANCE_PASS
- PRODUCTION_CUTOVER_READY

최종 완료는 ACCEPTANCE_PASS + PRODUCTION_CUTOVER_READY일 때만 선언한다.

================================================================================
20. 최종 완료 조건
================================================================================

다음 조건이 모두 만족되어야 Goal 완료다.

1. parser keyword가 직접 score/risk를 만들지 않는다.
2. 모든 비영점 점수는 source-backed accepted claim_id를 가진다.
3. 모든 hard break는 issuer-scoped, current OPEN, source-quorum-passed claim을 가진다.
4. 오래된 미확인 risk는 현재 penalty가 아니라 follow-up task가 된다.
5. wrong-subject claim은 target score/risk에 들어가지 않는다.
6. score-gap loop는 append-only이며 기존 claim을 조용히 삭제하지 않는다.
7. 모든 score delta는 claim delta로 설명된다.
8. source_proxy_only/evidence_url_pending/snippet-only/LLM-only inference는 production score에 들어가지 않는다.
9. 전 C01~C36 아키타입에 Evidence Contract v2가 있다.
10. 전 C01~C36 아키타입에 positive/guard/wrong-subject/old-risk/current-hard-break/source-missing fixture 또는 명시적 source gap이 있다.
11. 각 large sector에서 최소 3개 이상 bounded smoke가 통과한다.
12. 실제 candidate discovery path가 targeted smoke 없이 후보를 생성한다.
13. DART/IR/CompanyGuide로 해결 가능한 gap은 general web search로 가지 않는다.
14. 네이버/general search는 fallback이며 bounded budget 안에서만 실행된다.
15. run fingerprint 없이는 점수 전후 비교를 하지 않는다.
16. NON_COMPARABLE run끼리는 점수 변화로 설명하지 않는다.
17. frozen replay 3회 실행에서 claim_id/score/stage가 동일하다.
18. 삼성전자/월덱스 회귀 테스트에서 삼성 accounting risk=0, hard_break=false.
19. SK하이닉스 C06 URL-backed positive replay가 expected Stage를 재현한다.
20. 삼성 qualification lag는 current lifecycle 확인 없이 hard 4C가 되지 않는다.
21. 전역 adversarial suite가 통과한다.
22. 전체 pytest 통과.
23. acceptance report가 생성된다.
24. production cutover decision이 명시된다.
25. 워킹트리 clean.
26. 한글 커밋 메시지로 단일 최종 커밋 후 push.
27. 최종 답변에는 commit SHA, test 결과, replay 결과, live smoke 결과, unresolved source gaps, production readiness verdict를 포함한다.

================================================================================
21. 금지사항
================================================================================

- 특정 종목명 예외 처리 금지
- 특정 기사 URL 예외 처리 금지
- “감사의견 + 적정” 같은 단어쌍 예외만으로 해결 금지
- HBM 전용 임시 패치 금지
- score threshold 조정 금지
- Stage threshold 조정 금지
- source_proxy_only를 production fixture로 승격 금지
- future MFE/MAE를 LLM extraction 입력으로 제공 금지
- top_results=None 금지
- retry_max=None 금지
- 전체 웹 무제한 fetch 금지
- 중간 테스트 일부 통과를 Goal 완료라고 보고 금지
- 4000개 pytest 통과만으로 운영 승인 주장 금지
- 삼성/하이닉스 targeted smoke만으로 운영 승인 주장 금지

================================================================================
22. 최종 응답 형식
================================================================================

작업 완료 후 다음 형식으로만 보고하라.

1. 최종 상태
- IMPLEMENTATION_MERGED / REPLAY_PASS / SECTOR_SMOKE_PASS / LIVE_SMOKE_PASS / ACCEPTANCE_PASS / PRODUCTION_CUTOVER_READY 중 어디인지

2. 커밋
- commit SHA
- commit message
- push status
- working tree status

3. 테스트
- pytest command
- pass/fail/skip count
- failed tests if any

4. Legacy quarantine audit
- parser keyword direct path count
- old risk field direct score path count
- quarantine proof

5. Replay coverage
- C01~C36 matrix summary
- positive/guard/wrong-subject/old-risk/current-hard-break/source-missing fixture count
- source gap list

6. Sector smoke
- large sector별 실행 종목 수
- pass/fail/pending
- 대표 Stage output

7. Live smoke
- 삼성전자
- SK하이닉스
- 월덱스 fixture
- 각 sector 대표 후보
- score_valid_status
- stage
- hard_break_claim_ids
- score delta ledger

8. Source router audit
- general search count
- Naver count
- official source count
- unbounded fetch count
- DART/IR로 해결 가능한 gap이 web으로 간 사례 count

9. Score stability
- frozen replay 3회 variance
- score delta without claim delta count
- NON_COMPARABLE comparison count

10. Production verdict
- READY / NOT_READY
- 남은 blocker
- source gaps
- 다음 작업이 있으면 정확히 무엇인지

Goal 완료라고 말하려면 Production verdict가 READY여야 한다.