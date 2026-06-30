봤어. **이번엔 꽤 많이 좋아졌어.**
근데 결론은 아직 이거야.

```text
현재 상태:
Production Cutover v2 상당 부분 통과
READY_FOR_CENSUS_DESIGN 가능

아직 아님:
CUTOVER_READY
PRODUCTION_READY
CENSUS_IMPLEMENTATION 진입
```

# 핵심 판정

최신 커밋은 `c8f98bb cutover SLA 산출물 갱신`까지 올라와 있고, 최근 커밋들이 전부 cutover, SLA, report lineage, A2 보류, multiday 검증 쪽으로 이어져 있어. 즉 네가 시킨 방향으로 계속 패치된 건 맞아. ([GitHub][1])

이번 v2 acceptance는 라벨상으로는 `LIVE_CONNECTOR_PASS`, `A2_REPLAY_PASS`, `LLM_EXTRACTION_PASS`, `MEANINGFUL_STAGE_SPLIT_PASS`, `TRIGGER_POLICY_PASS`, `READY_FOR_CENSUS_DESIGN`까지 찍혀 있어. 그런데 같은 리포트가 `production_verdict: NOT_READY`, `production_ready: False`라고 명시한다. ([GitHub][2])

즉 지금은:

```text
Census 설계로 넘어갈 준비는 됨
운영 cutover는 아직 안 됨
```

이렇게 보는 게 맞아.

# 좋아진 부분

## 1. A2가 드디어 0이 아님

이전 blocker였던 `A2_REAL_REPLAY_VERIFIED_count = 0`은 이제 해결된 것으로 보인다. readiness verdict에 `A2_REAL_REPLAY_VERIFIED_count: 30`이 찍혀 있어. 이건 큰 진전이야. ([GitHub][3])

과거 연구자료는 그냥 점수 정답지가 아니라 “원문 replay 가능한 판례”로 승격되어야 했고, A2가 생겼다는 건 최소한 일부 URL-backed 연구 row가 Evidence OS replay에 올라왔다는 뜻이야. 이건 Census 전에 꼭 필요했던 문턱이었어.

## 2. static audit은 깨끗함

`production_cutover_v2_static_logic_audit.json` 기준으로 critical count가 0이고, source_proxy_to_score, source_proxy_to_A2, market anomaly to score, old risk to score, cheap scan score as verified score, unbounded fetch config 같은 핵심 위험 카운트도 0으로 찍혀 있어. ([GitHub][4])

이건 월덱스류 오귀속, source-proxy 점수화, cheap score를 verified score로 쓰는 사고는 꽤 잘 막고 있다는 뜻이야.

## 3. OpenDART live는 실제로 붙음

Provider matrix에서 OpenDART는 `live_mode_supported: true`, `fetch_success_count: 53`, `used_for_score_claim_count: 53`, `blocking_cutover: false`로 나온다. ([GitHub][5])

즉 적어도 DART 공식자료를 실제 운영 source로 쓰는 길은 열렸어.

## 4. stage/score 경로도 이전보다 정직함

Stage distribution 쪽을 보면 단일 공시 claim 하나로 Green이나 Yellow를 억지로 만들지 않고, `base_stage: 1`, `verified_score: 4.0`, `missing_green_primitives: repeat_evidence_family / cash_or_revision_conversion`, `stage_decision_reason: low claim-backed official disclosure score; no Green/Yellow bridge`처럼 낮게 남긴다. ([GitHub][6])

이건 좋은 신호야. 예전처럼 “공시 하나 있음 → 갑자기 80점대”가 아니라, 증거가 얕으면 낮은 Stage로 남기는 방식이 됐어.

# 아직 운영으로 못 넘기는 이유

## 1. provider blocker가 5개 남아 있음

가장 큰 blocker는 이거야.

```text
provider_blocker_count: 5
```

Readiness verdict도 명확히 말해. `blocking source provider gaps remain`, `multiday live shadow validation not complete` 때문에 `NOT_READY`야. ([GitHub][3])

Provider matrix를 보면 OpenDART만 live success고, KIND, KRX, CompanyGuide, IssuerIR, TrustedNews는 `live provider not fully implemented/configured`, `fetch_success_count: 0`, `blocking_cutover: true`로 남아 있어. ([GitHub][5])

이 상태에서 실제 운영하면 이런 문제가 남아.

```text
DART 공시 기반 종목은 어느 정도 작동
하지만
리스크/KIND/KRX
컨센서스/CompanyGuide
IR/뉴스/TrustedNews
쪽으로 필요한 primitive가 비면 ProviderPending이 많아짐
```

즉 아직 “전체 운영”이 아니라 **OpenDART 중심 official disclosure scanner**에 가까워.

## 2. multiday 검증이 아직 부족함

Multiday report를 보면 실제 완료된 live day는 1일이고, required live dry run은 5일, frozen day는 10일, repeated frozen day는 3일이 남아 있어. summary도 `MULTIDAY_SHADOW_NOT_COMPLETE`다. ([GitHub][7])

Census나 운영 cutover 전에 multi-day가 중요한 이유는 간단해.

```text
하루만 돌리면:
오늘 DART 공시 많은 날인지
특정 섹터만 걸린 건지
provider 실패가 일시적인 건지
score/stage가 반복 안정적인지
알 수 없음
```

지금은 하루짜리 성공이지, 운영 안정성 검증은 아직 덜 됐어.

## 3. claim extraction은 여전히 rule fallback 중심이 남아 있음

`LLMContractBlindRawAssertionExtractor`는 provider가 없으면 기본으로 `RuleFallbackExtractorProvider()`를 쓴다. ([GitHub][8])

그리고 `ContractBlindRawAssertionExtractor`는 문장을 쪼개고 `계약`, `수주`, `감사의견`, `영업이익`, `FCF`, `마진` 같은 키워드로 predicate/polarity를 잡는 구조야. 물론 Evidence OS 이전의 키워드 직행 점수보다 훨씬 안전하지만, 아직 “LLM이 문서 전체를 읽고 claim을 복원하는 최종형”이라고 보긴 어렵다. ([GitHub][9])

원래 Evidence OS 목표는 문서 원문에서 “누가, 언제, 무엇을 주장했는가 → 대상 회사에 직접 귀속되는가 → 현재 살아 있는가 → 어느 primitive인가 → 그래서 몇 점인가”라는 장부를 만드는 것이었어. 이 원칙 자체는 맞게 따라가고 있지만, 실제 claim extractor는 아직 더 깊어질 여지가 있어. 

## 4. 현재 Watchlist는 아직 Stage1 중심

Stage trace를 보면 대부분 단일 공시 claim 하나로 `base_stage: 1`, `verified_score: 4.0`, `single official disclosure is not enough for Green` 같은 형태야. ([GitHub][6])

이게 틀린 건 아니야. 오히려 안전해졌다는 증거야.

하지만 Census Mode로 넘어가서 전체 티커를 돌리면, 지금 상태에서는 대부분이:

```text
Stage1
low claim-backed official disclosure
insufficient primitive coverage
```

로 나올 가능성이 커.

우리가 원하는 전체 Stage 지도는:

```text
Stage0 / No Current Catalyst
Stage1 / Weak Watch
Stage2-Watch
Stage2-Actionable
Yellow-Pending
Green
ProviderPending
Reject/Red
```

이렇게 갈라져야 해. 지금은 그 분화가 아직 부족해.

# 지금 다음 단계는?

**Census 구현은 아직 이르다.**

하지만 **Census 설계는 시작해도 된다.**
리포트도 `READY_FOR_CENSUS_DESIGN`까지만 찍고, `production_cutover_ready: False`, `provider blocker count: 5`라서 Census implementation은 막고 있어. ([GitHub][10])

내 판정은 이거야.

```text
다음에 바로 할 것:
Provider gap 해소 + multiday shadow completion + Stage split 강화

아직 하지 말 것:
전체 티커 Census Mode 본구현
```

# 남은 핵심 패치

다음 Goal은 짧게 말하면 이거야.

```text
Production Cutover v3
= DART만 되는 시스템에서
  DART + KRX/KIND + CompanyGuide/Report + IR + TrustedNews까지
  source coverage를 넓히고,
  5일 shadow / frozen repeat를 끝내고,
  Stage1 회색지도가 아니라 Stage 분포가 갈라지는지 검증하는 Gate
```

특히 다음 4개가 닫혀야 해.

```text
1. provider_blocker_count = 0 또는 nonblocking source gap으로 명확히 재분류
2. multiday live official shadow 5일 완료
3. frozen repeat 검증 완료
4. Stage2/Yellow/Pending/Reject가 실제로 분화되는지 검증
```

# 다음 Goal 프롬프트

```text
너는 Daikisong/stock_agent 레포의 E2R Production Cutover Gate v3를 구현하는 coding agent다.

현재 전제:
- Evidence OS v2는 통과 상태다.
- Production Cutover Gate v2는 상당 부분 통과했다.
- 최신 v2 report는 LIVE_CONNECTOR_PASS, A2_REPLAY_PASS, LLM_EXTRACTION_PASS, MEANINGFUL_STAGE_SPLIT_PASS, TRIGGER_POLICY_PASS, READY_FOR_CENSUS_DESIGN 라벨을 가진다.
- 그러나 production_verdict는 NOT_READY다.
- 현재 blocker는 다음이다.
  1. provider_blocker_count = 5
  2. KIND/KRX/CompanyGuide/IssuerIR/TrustedNews live provider가 fully implemented/configured 상태가 아니다.
  3. multiday live shadow validation이 완료되지 않았다.
  4. 현재 watchlist는 주로 OpenDART 단일 공시 claim 기반 Stage1/low-score row가 많다.
- Census Mode는 아직 구현하지 마라.
- 이번 Goal은 Census를 구현하기 전, 실제 production cutover 가능 상태까지 provider coverage와 multiday stability를 닫는 것이다.

이번 Goal의 이름:
E2R Production Cutover Gate v3 — Provider Coverage, Multi-day Stability, Stage Split Completion

최종 목표:
DART 중심 daily shadow에서 벗어나
KIND/KRX risk, CompanyGuide/revision/report, Issuer IR, TrustedNews fallback까지 provider path를 닫고,
5일 이상 live official shadow 및 frozen repeat 검증을 완료하며,
Daily Watchlist가 Stage1 회색지도가 아니라 Stage2/Yellow/Pending/Reject로 의미 있게 분화되는지 증명한다.

절대 원칙:
1. Research Brain은 score/stage를 직접 계산하지 않는다.
2. Score/Stage는 Evidence OS accepted claim과 deterministic scorer/StageCourt만 사용한다.
3. source_proxy_only/evidence_url_pending/price_path_only memory는 current score evidence가 아니다.
4. provider_failed는 no_result가 아니다.
5. provider failure 상태에서 낮은 score나 Reject를 확정하지 않는다.
6. Market anomaly는 trigger일 뿐 score evidence가 아니다.
7. Census Mode는 이번 Goal에서 구현하지 않는다.
8. Census는 production cutover가 READY가 된 뒤 별도 Goal에서 구현한다.
9. scoring weight와 Stage threshold는 변경하지 않는다.
10. 특정 종목명, 특정 URL, 특정 키워드 예외 처리 금지.
11. report가 READY를 주장하려면 current git HEAD, command, config hash, source hash, planner hash, evidence schema hash가 모두 있어야 한다.

================================================================================
1. 현재 v2 상태 재라벨링
================================================================================

수정/생성:
docs/operational/production_cutover_v2_to_v3_gap.md

내용:
- v2는 READY_FOR_CENSUS_DESIGN이지 CUTOVER_READY가 아니다.
- v2에서 통과한 것:
  - OpenDART live success
  - A2 replay count 30
  - static critical count 0
  - DART-based source task / accepted claim / deterministic score path
  - trigger policy
- v2에서 부족한 것:
  - provider_blocker_count 5
  - KIND/KRX/CompanyGuide/IssuerIR/TrustedNews live provider gap
  - multiday shadow incomplete
  - Stage 분포가 대부분 low Stage1 official disclosure row에 집중
  - LLM extraction provider/fallback 사용 현황이 명확히 더 분리되어야 함
- Census implementation은 보류한다.

Acceptance:
- 기존 v2 production_verdict=NOT_READY 유지
- Census Mode 구현 금지
- Census readiness는 READY_FOR_CENSUS_DESIGN 이하로 유지

================================================================================
2. Provider Completeness v3
================================================================================

목표:
provider_blocker_count를 0으로 만들거나, 각 provider gap을 blocking/nonblocking으로 정당하게 재분류한다.

대상 provider:
- OpenDART
- KIND
- KRX
- CompanyGuide
- IssuerIR
- TrustedNews

각 provider는 다음 중 하나여야 한다.

A. LIVE_READY
- live_mode_supported=true
- fetch_success_count > 0
- provider_request_id 있음
- content_hash 있음
- used_for_score_claim_count 또는 used_for_pending_claim_count 기록
- blocker 없음

B. NONBLOCKING_OPTIONAL
- production cutover에 필수 provider가 아님
- 어떤 primitive/source family에 쓰이는지 명시
- 없어도 CUTOVER_READY 가능한 이유 명시

C. BLOCKING_GAP
- 아직 구현/인증/API 문제가 있음
- CUTOVER_READY 금지
- exact next action 명시

필수 구현:
- KIND/KRX risk connector 실제 구현 또는 NONBLOCKING_OPTIONAL로 정당 분류
- CompanyGuide/revision/report connector 실제 구현 또는 BLOCKING_GAP 명시
- IssuerIR discovery/fetch connector 구현 또는 NONBLOCKING_OPTIONAL/BLOCKING_GAP 분류
- TrustedNews fallback connector 구현 또는 NONBLOCKING_OPTIONAL/BLOCKING_GAP 분류

금지:
- LocalSnapshotConnector를 live connector로 alias
- provider_failed를 no_result로 처리
- provider가 안 되는데 production_ready=True
- provider gap을 문서에서만 숨김 처리

Reports:
docs/operational/production_cutover_v3_provider_completeness_matrix.json
docs/operational/production_cutover_v3_provider_gap_resolution.md

Acceptance:
- provider_blocker_count = 0 for CUTOVER_READY
- 또는 provider_blocker_count > 0이면 production_verdict=NOT_READY
- provider_failed_final_score_count = 0
- no_result_masked_provider_failed_count = 0
- at least OpenDART + one risk provider + one revision/report/IR provider path exercised
- provider mode, request_id, content_hash, latency, error recorded

Tests:
tests/test_cutover_v3_provider_completeness.py
tests/test_cutover_v3_provider_failed_not_no_result.py
tests/test_cutover_v3_no_ready_with_provider_blocker.py

================================================================================
3. Multi-day Shadow Completion
================================================================================

현재 multiday는 1일 완료 상태다.
v3에서는 요구된 multi-day 검증을 끝낸다.

Run requirements:
- live official shadow >= 5 trading days
- frozen replay days >= 10
- repeated frozen days with 3 runs >= 3
- same config hash for repeated runs
- same source corpus hash for frozen repeat
- repeat variance = 0
- fixture candidate in live = 0
- fake/frozen provider in live = 0
- provider failures become ProviderPending, not final Reject/Red

Reports:
docs/operational/production_cutover_v3_multiday_validation.json
docs/operational/production_cutover_v3_stability_report.md

Acceptance:
- five_day_live_official_shadow_count >= 5
- required_frozen_day_count >= 10
- frozen_repeat_day_with_3_runs_count >= 3
- repeat_variance = 0
- source_provider_failure rows have pending status
- production_verdict cannot be CUTOVER_READY without this pass

Tests:
tests/test_cutover_v3_multiday_validation_complete.py
tests/test_cutover_v3_frozen_repeat_variance_zero.py
tests/test_cutover_v3_provider_failure_pending_in_multiday.py

================================================================================
4. Claim Extraction Provider Audit
================================================================================

현재 contract-blind extraction은 rule fallback 중심 경로가 남아 있다.
v3에서는 LLM extraction과 rule fallback을 명확히 분리하고, 운영 readiness에 어떤 extractor가 쓰였는지 기록한다.

필수 metrics:
- llm_extractor_attempt_count
- llm_extractor_success_count
- llm_extractor_failure_count
- rule_fallback_extractor_count
- rule_fallback_score_eligible_claim_count
- mention_only_count
- accepted_claim_from_llm_count
- accepted_claim_from_rule_count
- forced_target_subject_count
- forced_positive_polarity_count
- forced_current_temporal_count
- contract_visible_to_raw_extractor_count
- primitive_gap_visible_to_raw_extractor_count

Rules:
- rule fallback may create mention/raw assertion candidates.
- rule fallback accepted score claims are allowed only for official structured API records with explicit subject/date/value/locator.
- free text article/PDF claim extraction should prefer LLM extractor.
- if LLM extractor unavailable and source is unstructured text, claim stays mention-only/pending.
- production_ready requires either:
  A. LLM extractor success on unstructured documents, or
  B. explicit policy that current production mode is structured-official-only.

Reports:
docs/operational/production_cutover_v3_claim_extractor_provider_audit.json

Acceptance:
- contract_visible_to_raw_extractor_count = 0
- primitive_gap_visible_to_raw_extractor_count = 0
- forced_* counts = 0
- rule_fallback_score_eligible_claim_count justified by structured official API only
- unstructured_text_rule_score_count = 0
- if no LLM extraction success, production mode must be declared STRUCTURED_OFFICIAL_ONLY and Census implementation stays blocked

Tests:
tests/test_cutover_v3_claim_extractor_provider_audit.py
tests/test_cutover_v3_unstructured_text_requires_llm_or_pending.py
tests/test_cutover_v3_rule_fallback_structured_only.py

================================================================================
5. Stage Split Completion
================================================================================

현재 Stage는 대부분 base_stage=1 / verified_score=4 official disclosure row다.
v3에서는 meaningful stage split을 더 강하게 검증한다.

Daily shadow must produce or explicitly account for:
- Stage2-Actionable
- Stage2-Watch
- Yellow-Pending
- Provider/Source Pending
- Reject/Red or RiskReview
- NoCurrentCatalyst not required until Census, but policy must exist

Rules:
- Single official disclosure claim can remain Stage1.
- Multi-source / cash/revision / repeat evidence can unlock Stage2/Yellow if Evidence OS accepted.
- Provider failure creates ProviderPending.
- Risk source creates RiskReview/Reject only if current direct OPEN claim exists.
- Market-only event cannot score.
- If all 50 rows are Stage1, CUTOVER_READY is forbidden unless the run is explicitly “low-signal day” and multiday contains split across other days.

Reports:
docs/operational/production_cutover_v3_stage_distribution_report.json

Acceptance:
- across 5 live shadow days:
  - deterministic_scorer_output_count >= 100
  - Stage2_or_higher_count >= 10 OR documented low-signal market with NOT_READY
  - ProviderPending_count >= provider material failure count
  - RiskReview_or_Reject_count >= 1 from risk fixtures or live risk source
  - YellowPending_count >= 1 from replay or live multi-source case
- all Stage rows have StageCourt trace
- all nonzero score rows have claim IDs

Tests:
tests/test_cutover_v3_stage_split_multiday.py
tests/test_cutover_v3_all_stage1_blocks_cutover_ready.py
tests/test_cutover_v3_provider_pending_not_final_reject.py

================================================================================
6. Trigger Taxonomy Enforcement
================================================================================

v2 created trigger policy. v3 must enforce it in production shadow.

Every CandidateEvent must include:
- trigger_category
- allowed_source_families
- score_eligibility_policy
- investigation_only flag if market/news/snippet trigger
- source task generation policy
- no score evidence until accepted claim

Critical checks:
- market_anomaly_to_score_count = 0
- news_snippet_to_score_count = 0
- census_assessment_trigger_used_before_census_count = 0
- old_risk_without_current_open_to_score_count = 0

Reports:
docs/operational/production_cutover_v3_trigger_policy_audit.json

Tests:
tests/test_cutover_v3_trigger_policy_enforced.py

================================================================================
7. Production Readiness Verdict v3
================================================================================

새 verdict 생성:
docs/operational/production_cutover_v3_readiness_verdict.md
docs/operational/production_cutover_v3_acceptance_report.md

Possible verdicts:
- NOT_READY
- READY_FOR_CENSUS_DESIGN
- CUTOVER_READY
- PRODUCTION_READY

Rules:
- CUTOVER_READY requires:
  - provider_blocker_count = 0
  - multiday shadow complete
  - static critical count = 0
  - A2_REAL_REPLAY_VERIFIED_count >= 30
  - meaningful stage split pass
  - report reproducibility pass
  - no fixture/source_proxy contamination
  - no unbounded fetch
  - score/stage trace complete
- PRODUCTION_READY additionally requires:
  - operator digest generated for 5 days
  - SLA pass
  - provider failure handling observed
  - no high severity warnings
  - manual user approval flag or explicit final cutover flag

Census:
- READY_FOR_CENSUS_DESIGN may remain true.
- READY_FOR_CENSUS_IMPLEMENTATION only if CUTOVER_READY true.
- Census Mode implementation is forbidden in this Goal.

================================================================================
8. Operator Digest v3
================================================================================

Generate 5-day operator digest samples.

Each item:
- symbol
- company
- trigger category
- event summary
- primary archetype
- current stage
- verified score
- score status
- supporting claims
- missing primitives
- provider/source gaps
- next action
- operator note

Next actions:
- WATCH
- INVESTIGATE
- RECHECK_SOURCE
- RISK_REVIEW
- IGNORE
- PROVIDER_WAIT
- CENSUS_BASELINE_CANDIDATE

No buy/sell language.

Reports:
docs/operational/production_cutover_v3_operator_digest_summary.md
output/production_cutover_v3/YYYY-MM-DD/operator_digest.md
output/production_cutover_v3/YYYY-MM-DD/operator_digest.json

Acceptance:
- every item has next_action
- every pending item has follow-up task
- every scored item has support claim IDs
- every provider failure item is not final reject

================================================================================
9. SLA / Runtime v3
================================================================================

The system must finish.

Metrics:
- total runtime
- planner runtime
- source acquisition runtime
- extraction runtime
- scoring runtime
- API call count
- LLM call count
- provider failures
- retry count
- cache hit/miss
- runtime budget exhausted candidates

Rules:
- runtime budget exhausted candidates become RuntimeBudgetPending.
- no final reject on provider/runtime failure.
- no top_results=None.
- no retry_max=None.
- no hidden background work.

Reports:
docs/operational/production_cutover_v3_sla_report.json

Acceptance:
- 5-day shadow average runtime under configured budget
- no unbounded fetch
- budget exhausted rows pending

Tests:
tests/test_cutover_v3_sla_runtime.py

================================================================================
10. Static Logic Audit v3
================================================================================

Implement:
src/e2r/cli/audit_production_cutover_v3_readiness.py

Critical counts:
- production_ready_with_provider_blocker_count
- cutover_ready_with_multiday_incomplete_count
- all_stage1_but_ready_count
- rule_fallback_unstructured_text_score_count
- live_connector_alias_to_snapshot_count
- provider_failed_final_score_count
- source_proxy_to_score_count
- source_proxy_to_A2_count
- evidence_url_pending_to_fixture_count
- market_anomaly_to_score_count
- news_snippet_to_score_count
- old_risk_without_current_open_to_score_count
- accepted_claim_without_anchor_count
- accepted_claim_without_date_count
- score_without_claim_count
- unbounded_fetch_config_count
- census_implementation_before_cutover_ready_count
- missing_report_hash_count
- report_head_sha_mismatch_count

All critical counts must be 0.

Reports:
docs/operational/production_cutover_v3_static_logic_audit.json

================================================================================
11. Tests
================================================================================

Add/strengthen:

tests/test_cutover_v3_provider_completeness.py
tests/test_cutover_v3_multiday_validation_complete.py
tests/test_cutover_v3_claim_extractor_provider_audit.py
tests/test_cutover_v3_stage_split_multiday.py
tests/test_cutover_v3_trigger_policy_enforced.py
tests/test_cutover_v3_operator_digest.py
tests/test_cutover_v3_sla_runtime.py
tests/test_cutover_v3_static_logic_audit.py
tests/test_cutover_v3_no_census_before_cutover_ready.py
tests/test_cutover_v3_no_ready_with_provider_blocker.py

Full command:
PYTHONPATH=src python -m unittest discover -s tests -v

No skipped cutover tests allowed.

================================================================================
12. Final reports
================================================================================

Generate:

docs/operational/production_cutover_v3_acceptance_report.md
docs/operational/production_cutover_v3_readiness_verdict.md
docs/operational/production_cutover_v3_provider_completeness_matrix.json
docs/operational/production_cutover_v3_provider_gap_resolution.md
docs/operational/production_cutover_v3_multiday_validation.json
docs/operational/production_cutover_v3_stability_report.md
docs/operational/production_cutover_v3_claim_extractor_provider_audit.json
docs/operational/production_cutover_v3_stage_distribution_report.json
docs/operational/production_cutover_v3_trigger_policy_audit.json
docs/operational/production_cutover_v3_operator_digest_summary.md
docs/operational/production_cutover_v3_sla_report.json
docs/operational/production_cutover_v3_static_logic_audit.json
docs/operational/census_mode_readiness_report.md

Output:
output/production_cutover_v3/YYYY-MM-DD/
  candidate_events.json
  provider_fetch_results.jsonl
  source_tasks.json
  source_task_executions.json
  evidence_documents.jsonl
  evidence_anchors.jsonl
  raw_assertions.jsonl
  adjudicated_claims.jsonl
  accepted_claims.jsonl
  primitive_states.jsonl
  score_contributions.jsonl
  stagecourt_traces.json
  daily_watchlist.json
  operator_digest.md
  audit_summary.json

================================================================================
13. Completion labels
================================================================================

Allowed labels:
- IMPLEMENTATION_MERGED
- PROVIDER_COMPLETENESS_PASS
- MULTIDAY_SHADOW_PASS
- CLAIM_EXTRACTOR_AUDIT_PASS
- MEANINGFUL_STAGE_SPLIT_PASS
- TRIGGER_POLICY_ENFORCED
- OPERATOR_DIGEST_PASS
- SLA_PASS
- CUTOVER_READY
- PRODUCTION_READY
- READY_FOR_CENSUS_DESIGN
- READY_FOR_CENSUS_IMPLEMENTATION

Goal completion minimum:
- PROVIDER_COMPLETENESS_PASS
- MULTIDAY_SHADOW_PASS
- CLAIM_EXTRACTOR_AUDIT_PASS
- MEANINGFUL_STAGE_SPLIT_PASS
- TRIGGER_POLICY_ENFORCED
- static critical count 0

CUTOVER_READY:
- all goal completion minimum
- provider_blocker_count = 0
- multiday complete
- A2 >= 30
- no source/provider blocker
- no fixture/source_proxy contamination
- report reproducibility pass

PRODUCTION_READY:
- CUTOVER_READY
- 5-day operator digest pass
- SLA pass
- user explicit approval flag or final cutover flag

Census:
- READY_FOR_CENSUS_DESIGN allowed.
- READY_FOR_CENSUS_IMPLEMENTATION only if CUTOVER_READY.

================================================================================
14. Final answer format
================================================================================

After completion, report only:

1. Final status
2. Commit SHA / message / push status / working tree
3. Test result
4. Provider completeness
5. Multiday validation
6. Claim extractor audit
7. Stage distribution
8. Trigger policy
9. Operator digest
10. SLA
11. Census readiness label
12. Production verdict
13. Remaining blockers

================================================================================
15. Prohibitions
================================================================================

- Do not implement Census Mode.
- Do not claim CUTOVER_READY with provider_blocker_count > 0.
- Do not claim CUTOVER_READY with multiday incomplete.
- Do not claim PRODUCTION_READY without CUTOVER_READY.
- Do not treat provider_failed as no_result.
- Do not finalize low score on provider failure.
- Do not score source_proxy/evidence_url_pending rows.
- Do not score market anomaly or news snippet.
- Do not change scoring weights or Stage thresholds.
- Do not hardcode symbol/company/url exceptions.
- Do not output one-line huge reports.

================================================================================
16. One-line goal
================================================================================

이번 Goal은 Census Mode 구현이 아니다.

이번 Goal은:
provider gaps를 닫고,
5일 이상 shadow run을 완주하고,
claim extraction provider 사용을 투명화하고,
Stage가 의미 있게 갈라지는지 증명해서,
Census Mode를 실제로 구현해도 되는지 결정하는 마지막 cutover gate다.
```

# 최종 결론

이번 완료 상태는 **좋다. 하지만 아직 “다음 단계=Census 구현”은 아니다.**

정확히는:

```text
지금 가능:
Census 설계 문서화
Census 요구사항 정의
Stage0/NoCurrentCatalyst 정책 설계

아직 보류:
전체 티커 Census Mode 구현
```

다음 패치에서 provider blockers와 multiday가 닫히면 그때 Census Mode로 넘어가는 게 맞아.
지금 바로 Census를 만들면, 전체 시장 지도가 아니라 **DART 단일 공시 기반 Stage1 회색지도**가 될 가능성이 높아.

[1]: https://github.com/Daikisong/stock_agent/commits/main "Commits · Daikisong/stock_agent · GitHub"
[2]: https://raw.githubusercontent.com/Daikisong/stock_agent/main/docs/operational/production_cutover_v2_acceptance_report.md "raw.githubusercontent.com"
[3]: https://raw.githubusercontent.com/Daikisong/stock_agent/main/docs/operational/production_cutover_v2_readiness_verdict.md "raw.githubusercontent.com"
[4]: https://raw.githubusercontent.com/Daikisong/stock_agent/main/docs/operational/production_cutover_v2_static_logic_audit.json "raw.githubusercontent.com"
[5]: https://github.com/Daikisong/stock_agent/blob/main/docs/operational/production_cutover_v2_provider_completeness_matrix.json "stock_agent/docs/operational/production_cutover_v2_provider_completeness_matrix.json at main · Daikisong/stock_agent · GitHub"
[6]: https://github.com/Daikisong/stock_agent/blob/main/docs/operational/production_cutover_v2_stage_distribution_report.json "stock_agent/docs/operational/production_cutover_v2_stage_distribution_report.json at main · Daikisong/stock_agent · GitHub"
[7]: https://raw.githubusercontent.com/Daikisong/stock_agent/main/docs/operational/production_cutover_v2_multiday_validation.json "raw.githubusercontent.com"
[8]: https://raw.githubusercontent.com/Daikisong/stock_agent/main/src/e2r/production/claim_extraction/llm_contract_blind_extractor.py "raw.githubusercontent.com"
[9]: https://raw.githubusercontent.com/Daikisong/stock_agent/main/src/e2r/production/claim_extraction/contract_blind_extractor.py "raw.githubusercontent.com"
[10]: https://raw.githubusercontent.com/Daikisong/stock_agent/main/docs/operational/census_mode_readiness_report.md "raw.githubusercontent.com"
