너는 Daikisong/stock_agent 레포의 E2R Production Cutover Gate v2를 구현하는 coding agent다.

현재 전제:
- Evidence OS v2는 구현되어 있고, parser keyword direct score/risk 경로는 차단되어 있다.
- Research Brain v4 / Production Cutover Gate v1은 DAILY_PRODUCTION_SHADOW_PASS까지 도달했다.
- 최신 report는 production_ready=false, production_verdict=NOT_READY다.
- 현재 blocker는 다음이다.
  - A2 real replay verified count is 0
  - explicit source/provider gap keeps cutover NOT_READY
- 현재 source connector 일부는 LocalSnapshotConnector alias이며, live mode에서 provider_failed를 반환한다.
- 현재 contract-blind extraction은 안전장치가 있으나 실제 LLM document understanding보다는 rule/keyword extractor에 가깝다.
- 현재 watchlist는 대부분 accepted claim 1개, verified_score 1.5~4.4, base_stage=1, insufficient primitive coverage로 끝난다.
- 따라서 아직 Census Mode로 넘어가면 안 된다.

이번 Goal의 이름:
E2R Production Cutover Gate v2 — Live Source Connector, A2 Replay, Deep Claim Extraction, Meaningful Stage Split

최종 목표:
실제 운영 전 마지막 문턱을 닫는다.

실제 KRX universe
→ actual official source trigger scan
→ CandidateEvent
→ Research Brain planner
→ live official-first SourceTask
→ real provider document fetch
→ EvidenceDocument / EvidenceAnchor
→ contract-blind LLM claim extraction
→ target/temporal/primitive adjudication
→ accepted AdmissibleClaim
→ ScoreContributionLedger
→ DeterministicScorer
→ StageCourt
→ meaningful Daily Watchlist

단, Census Mode는 아직 구현하지 않는다.
이번 Goal은 Census Mode를 만들 수 있는 상태인지 판단 가능한 production cutover completeness를 확보하는 것이 목적이다.

절대 원칙:
1. Research Brain은 score/stage를 직접 계산하지 않는다.
2. Research Brain output은 FeatureInput, ScoreContribution, risk field를 직접 mutate하지 않는다.
3. LocalSnapshotConnector를 LiveConnector로 위장하지 않는다.
4. provider_failed를 no_evidence로 위장하지 않는다.
5. source_proxy_only/evidence_url_pending/price_path_only memory는 current production score evidence가 아니다.
6. A2_REAL_REPLAY_VERIFIED가 0이면 PRODUCTION_READY 금지다.
7. accepted claim은 real provider fetch 또는 valid stored snapshot with provider request lineage를 가져야 한다.
8. event_summary, candidate_reason, planner rationale은 quote가 아니다.
9. cheap_scan_total_score는 verified_score가 아니다.
10. score/stage threshold와 weight는 변경하지 않는다.
11. 특정 종목명, 특정 URL, 특정 키워드 예외 처리 금지.
12. final report가 READY라고 주장하려면 current git HEAD, command, config hash, source hash, planner hash, evidence schema hash가 모두 있어야 한다.

================================================================================
1. 현재 상태 재라벨링과 Census Gate 보류
================================================================================

수정/생성:
docs/operational/production_cutover_v1_to_v2_gap.md
docs/operational/census_mode_prerequisite_gate.md

내용:
- v1/v4는 DAILY_PRODUCTION_SHADOW_PASS다.
- production_ready=false가 맞다.
- NOT_READY 사유:
  - A2 real replay verified count 0
  - live source connector gap
  - CompanyGuide / IR / KIND / TrustedNews provider failure
  - Watchlist 대부분 Stage1 / insufficient primitive coverage
  - contract-blind extractor가 아직 rule extractor 중심
- Census Mode는 다음 조건 전까지 보류한다.
  - A2_REAL_REPLAY_VERIFIED_count > 0
  - live official connector pass
  - meaningful stage split pass
  - Watchlist에 Stage2-Actionable / Yellow-Pending / ProviderPending / Reject/Red가 구분됨
  - full ticker run이 Stage0/SourcePending/NoCurrentCatalyst를 지원할 준비가 됨

Acceptance:
- 기존 NOT_READY 상태를 PRODUCTION_READY로 바꾸지 않는다.
- Census Mode 구현은 이번 Goal에서 금지한다.
- Census Mode는 다음 Goal 후보로만 문서화한다.

================================================================================
2. Live Source Connector 실구현
================================================================================

현재 opendart_live_connector.py, companyguide_live_connector.py가 LocalSnapshotConnector alias로 되어 있다.
이것을 실제 connector로 교체하거나, 아직 실제 API 구현이 불가능하면 명확히 NOT_READY로 유지하라.

구현 대상:
src/e2r/production/source_connectors/
    opendart_live_connector.py
    kind_live_connector.py
    krx_live_connector.py
    companyguide_live_connector.py
    issuer_ir_connector.py
    trusted_news_connector.py
    source_provider_registry.py

각 connector는 SourceFetchResult를 반환한다.

SourceFetchResult:
{
  "provider_name": "...",
  "source_class": "...",
  "mode": "live|fresh_provider_cache|snapshot|frozen",
  "request_id": "...",
  "request_params": {},
  "status": "FETCHED|NO_RESULT|PROVIDER_FAILED|RATE_LIMITED|AUTH_FAILED|REJECTED_BY_POLICY",
  "canonical_url": "...",
  "official_document_id": "...",
  "published_at": "...",
  "available_at": "...",
  "fetched_at": "...",
  "content_hash": "...",
  "raw_text": "...",
  "structured_payload": {},
  "provider_error": null,
  "provider_request_id": "...",
  "freshness_seconds": null
}

필수 live connector 기준:
- OpenDART:
  - corp code / company info
  - disclosure list
  - disclosure detail/document or official API record
  - financial statement or xbrl/API record where available
- KIND/KRX:
  - risk/trading halt/market warning/listing flags
  - provider failure를 명확히 기록
- CompanyGuide:
  - revision/report metadata
  - 실제 connector가 불가능하면 PROVIDER_FAILED로 명시
- IssuerIR:
  - 회사 IR/newsroom URL discovery
  - no result과 provider failed 구분
- TrustedNews:
  - trusted news only fallback
  - Naver/general search와 분리

금지:
- LocalSnapshotConnector를 LiveConnector로 alias하기
- snapshot://를 live evidence로 세기
- data/raw fixture/cache 파일을 production live source로 세기
- provider_failed를 no_result로 처리하기
- content_hash 없는 문서를 fetched로 처리하기
- official_document_id/canonical_url 없는 문서를 score evidence로 처리하기

Acceptance:
- OpenDART live connector 실제 FETCHED >= 10
- at least 3 provider classes exercised
- CompanyGuide/KIND/IR/TrustedNews가 구현되지 않았으면 provider gap으로 남고 PRODUCTION_READY 금지
- source_task_accepted_without_provider_fetch_count = 0
- snapshot_only_counted_as_live_count = 0
- provider_failed_final_score_count = 0
- fetched document마다 provider_request_id, content_hash, canonical_url 또는 official_document_id가 있음

Reports:
docs/operational/production_cutover_v2_source_connector_report.json
docs/operational/production_cutover_v2_provider_gap_report.json

Tests:
tests/test_cutover_v2_live_connectors_not_aliases.py
tests/test_cutover_v2_opendart_real_fetch.py
tests/test_cutover_v2_snapshot_not_live.py
tests/test_cutover_v2_provider_failed_not_no_result.py

================================================================================
3. A2 Real Replay Promotion Gate
================================================================================

현재 A2_REAL_REPLAY_VERIFIED_count = 0이다.
이번 Goal에서 최소한 일부 URL-backed 연구자료를 실제 A2로 승격하라.

A2_REAL_REPLAY_VERIFIED 조건:
- source_proxy_only=false
- evidence_url_pending=false
- source_url 또는 official API/snapshot URI 존재
- fetch 또는 stored provider snapshot load 성공
- content_hash 존재
- published_at 또는 official filing date verified
- EvidenceAnchor 생성
- exact quote / table cell / API locator verified
- subject/target directness verified
- temporal status verified
- primitive mapping accepted
- Evidence OS score eligibility 통과
- replay fixture expected primitive와 일치

우선순위:
1. C06 URL-backed rows
   - SK hynix HBM sold-out
   - SK hynix HBM revenue mix
   - Samsung qualification lag watch
2. C08 URL-backed rows
   - ISC VIP customer mix
   - Leeno margin/socket bridge
   - Okins Samsung socket supply
   - product/profile-only false positives
3. C15 URL-backed rows
   - paper price pass-through
   - commodity weather false positives
   - realized margin/phase guard examples

명시적으로 금지:
- C24/C28/C17 source_proxy_only/evidence_url_pending rows를 A2로 승격 금지
- URL 문자열만으로 A2 금지
- source_proxy narrative를 quote처럼 쓰기 금지
- MFE/MAE outcome을 extraction prompt에 넣기 금지

Acceptance:
- A2_REAL_REPLAY_VERIFIED_count >= 30
- C06 A2 >= 8
- C08 A2 >= 6
- C15 A2 >= 8
- source_proxy_to_A2_count = 0
- evidence_url_pending_to_A2_count = 0
- A2_without_anchor_count = 0
- A2_without_source_date_count = 0
- A2_without_accepted_claim_id_count = 0
- failed promotion rows must have failure_reason

Reports:
docs/operational/production_cutover_v2_A2_replay_promotion_report.json
docs/operational/production_cutover_v2_A2_promoted_claims.jsonl
docs/operational/production_cutover_v2_A2_failed_queue.json

Tests:
tests/test_cutover_v2_a2_real_replay_promotion.py
tests/test_cutover_v2_source_proxy_never_a2.py
tests/test_cutover_v2_url_string_only_not_a2.py
tests/test_cutover_v2_c06_c08_c15_a2_fixtures.py

================================================================================
4. Contract-blind LLM Claim Extraction 강화
================================================================================

현재 contract_blind_extractor는 안전하지만 rule/keyword 중심이다.
Production Cutover v2에서는 실제 LLM extractor를 붙이되, Evidence OS의 금지 규칙을 유지하라.

구현:
src/e2r/production/claim_extraction/llm_contract_blind_extractor.py
src/e2r/production/claim_extraction/extractor_provider.py
src/e2r/production/claim_extraction/extraction_validator.py

LLM Extractor 입력:
- target company identity/aliases
- as_of_date
- document metadata
- document text or API/table record
- source_url / official_document_id
- no score
- no stage
- no failed green gates
- no desired primitive
- no MFE/MAE
- no outcome label

LLM Extractor 출력:
RawAssertion list:
- subject
- predicate
- object/value
- unit
- polarity proposal
- modality
- event_date
- effective period
- exact quote or API/table locator
- related entities
- uncertainty reason

금지:
- primitive id 출력 금지
- score/stage 출력 금지
- hard_break final 출력 금지
- current_score_eligible 출력 금지
- source task primitive_gap을 보여주기 금지
- Evidence Contract를 RawAssertion extractor에 보여주기 금지

후속 단계:
RawAssertion
→ anchor validator
→ entity resolver
→ temporal adjudicator
→ primitive mapper
→ score eligibility derivation

Acceptance:
- real_document_to_raw_assertion_count >= 100 across validation
- llm_raw_assertion_extractor_used_count >= 30
- rule_fallback_mention_only_count reported separately
- forced_target_subject_count = 0
- forced_positive_polarity_count = 0
- forced_current_temporal_count = 0
- contract_visible_to_raw_extractor_count = 0
- primitive_gap_direct_mapping_count = 0
- event_summary_used_as_exact_quote_count = 0
- accepted claim must have quote/API/table locator validated by code

Reports:
docs/operational/production_cutover_v2_claim_extraction_report.json
docs/operational/production_cutover_v2_llm_extraction_samples.jsonl

Tests:
tests/test_cutover_v2_llm_contract_blind_extractor.py
tests/test_cutover_v2_no_contract_in_raw_extractor.py
tests/test_cutover_v2_no_forced_subject_polarity_temporal.py
tests/test_cutover_v2_quote_anchor_validation.py

================================================================================
5. Meaningful Stage Split Gate
================================================================================

현재 watchlist 대부분은 base_stage=1, verified_score 1.5~4.4, insufficient primitive coverage다.
이 상태에서는 Census Mode로 넘어가면 전체 시장이 회색 지도가 된다.

이번 Goal에서는 production shadow watchlist가 최소한 의미 있게 갈라지는지 검증하라.

목표 section:
- Stage3-Green
- Stage3-Yellow-Pending
- Stage2-Actionable
- Stage2-Watch
- 4B-watch
- Reject/Red
- Provider/Source Pending
- NoCurrentCatalyst

Daily production shadow에서 반드시 Green이 나와야 하는 것은 아니다.
하지만 Stage2-Actionable / Yellow-Pending / ProviderPending / Reject/Red 중 일부가 실제로 나와야 한다.

Rules:
- accepted claim 1개짜리 minor disclosure는 Stage1/Watch로 남겨도 됨
- provider gap이 있으면 ProviderPending
- core source missing but material gap이면 PendingMaterialGaps
- false-positive guard가 작동하면 Stage2-Watch 또는 Reject/Red
- hard break는 current OPEN direct source-backed claim 필요
- no current event는 NoCurrentCatalyst

Acceptance:
- deterministic_scorer_output_count >= 50
- Stage2_or_higher_count >= 5 OR report NOT_READY with source/provider explanation
- PendingMaterialGaps_count >= 1 if material source gaps exist
- ProviderPending_count equals provider material failures
- Reject/Red_count >= 1 in regression/adversarial slice
- all stage rows have StageCourt trace
- all nonzero scores have claim IDs
- score meaning audit explains every low score

Reports:
docs/operational/production_cutover_v2_stage_distribution_report.json
docs/operational/production_cutover_v2_score_meaning_audit.json

Tests:
tests/test_cutover_v2_meaningful_stage_split.py
tests/test_cutover_v2_provider_gap_pending.py
tests/test_cutover_v2_no_gray_map_ready.py

================================================================================
6. Trigger Taxonomy / Claim Access Policy
================================================================================

Census Mode 전에, 무엇을 트리거로 볼지 정책을 고정해야 한다.

생성:
configs/e2r_trigger_taxonomy_v1.json
configs/e2r_claim_access_policy_v1.json
docs/operational/trigger_taxonomy_and_claim_access_policy.md

Trigger categories:
1. Official Positive Trigger
   - DART supply contract
   - facility investment
   - earnings preannouncement
   - major contract update
   - share buyback/cancellation
   - confirmed capacity/order/IR disclosure

2. Official Risk Trigger
   - contract cancellation
   - audit opinion issue
   - trading halt
   - administrative issue
   - litigation/regulatory sanction
   - capital dilution event

3. Financial/Revision Trigger
   - actual OPM/FCF improvement
   - EPS/OP consensus revision
   - target price/report revision
   - revenue/margin bridge

4. Market Anomaly Trigger
   - volume spike
   - relative strength
   - breakout/gap
   - sector-wide move
   - price anomaly is never score evidence; only investigation trigger

5. Information Trigger
   - issuer IR
   - conference call
   - company newsroom
   - trusted news
   - broker report
   - snippet is query hint only, not score evidence

6. Census Assessment Trigger
   - no new event, but periodic full-universe baseline assessment
   - should not force score if no current evidence exists

Claim access policy:
- trigger can open investigation
- only accepted claim can open score
- market anomaly cannot become score evidence
- news headline cannot score without full source/date/quote/target validation
- source_proxy memory cannot score
- old risk cannot score without current OPEN lifecycle
- missing evidence is UNKNOWN, not ABSENT

Acceptance:
- every CandidateEvent has trigger_category
- every trigger_category has allowed source families
- every trigger_category has score eligibility policy
- market-only events produce investigation tasks, not score contributions
- Census AssessmentEvent can produce Stage0/NoCurrentCatalyst without deep source fetch

Reports:
docs/operational/production_cutover_v2_trigger_policy_audit.json

Tests:
tests/test_trigger_taxonomy_policy.py
tests/test_market_anomaly_not_score_evidence.py
tests/test_census_assessment_trigger_no_forced_score.py

================================================================================
7. Production Source Provider Completeness Report
================================================================================

지금 source gaps를 더 깊게 분해하라.

생성:
docs/operational/production_cutover_v2_provider_completeness_matrix.json

For each provider:
- provider_name
- implemented
- live_mode_supported
- auth_required
- env_key_required
- env_key_present
- fetch_success_count
- fetch_failure_count
- no_result_count
- rate_limit_count
- average_latency
- used_for_score_claim_count
- blocking_cutover
- blocker_reason

Required providers:
- OpenDART
- KIND
- KRX
- CompanyGuide or report radar
- Issuer IR
- TrustedNews fallback

PRODUCTION_READY requires:
- OpenDART live success
- KRX/KIND risk source either success or explicit nonblocking source gap
- at least one revision/report source success or explicit NOT_READY
- provider matrix generated
- unresolved blocking providers prevent PRODUCTION_READY

================================================================================
8. Multi-day Real Official Shadow Run 강화
================================================================================

현재 multiday는 좋게 찍혔지만 A2와 provider gap 때문에 NOT_READY다.
v2에서는 실제 provider completeness와 A2 replay를 포함해 다시 돌린다.

Run:
- 5 trading days live official source shadow OR frozen provider snapshots captured from live connector
- 10 frozen repeat days after live capture
- repeat 3 times for 3 frozen days
- same config hash
- same source snapshot hash
- repeat variance 0
- provider failures must become ProviderPending or source gap
- no fixture candidates
- no source_proxy_to_score

Acceptance:
- five_day_live_official_shadow_count >= 5
- frozen_repeat_day_with_3_runs_count >= 3
- repeat_variance = 0
- accepted_claim_total >= 100
- deterministic_stage_output_total >= 100
- A2_REAL_REPLAY_VERIFIED_count >= 30
- unresolved provider blocker count = 0 for PRODUCTION_READY
- otherwise NOT_READY with exact blockers

Reports:
docs/operational/production_cutover_v2_multiday_validation.json
docs/operational/production_cutover_v2_stability_report.md

Tests:
tests/test_cutover_v2_multiday_with_a2_gate.py

================================================================================
9. Census Mode Readiness Report
================================================================================

이번 Goal에서 Census Mode를 구현하지 말고, 구현 가능 여부만 판정하라.

생성:
docs/operational/census_mode_readiness_report.md
docs/operational/census_mode_design_backlog.json

Census readiness checks:
- production cutover ready?
- A2 replay verified count > 0?
- live connectors sufficient?
- trigger taxonomy complete?
- meaningful stage split available?
- Stage0/NoCurrentCatalyst supported?
- ProviderPending supported?
- NoCurrentEvent assessment supported?
- full universe candidate purity supported?
- SLA/budget sufficient?
- source gap rate acceptable?

Census readiness labels:
- NOT_READY_FOR_CENSUS
- READY_FOR_CENSUS_DESIGN
- READY_FOR_CENSUS_IMPLEMENTATION

Rules:
- If Production Cutover is NOT_READY, Census label cannot exceed READY_FOR_CENSUS_DESIGN.
- If A2 count = 0, Census implementation forbidden.
- If Stage split is all Stage1, Census implementation forbidden.
- If provider gap material, Census implementation forbidden.

================================================================================
10. SLA / Runtime Hardening
================================================================================

Production mode must finish.

Add:
- max wall time
- max candidates
- max source tasks
- max LLM calls
- max source fetches
- per-provider circuit breaker
- retry policy
- partial completion report

Budget states:
- COMPLETE
- PARTIAL_WITH_PENDING
- RUNTIME_BUDGET_EXHAUSTED
- PROVIDER_CIRCUIT_OPEN

Rules:
- runtime budget exhausted candidates become RuntimeBudgetPending
- no final reject on provider/runtime failure
- no unbounded fetch
- no hidden background work

Reports:
docs/operational/production_cutover_v2_sla_report.json

Tests:
tests/test_cutover_v2_runtime_budget_pending.py
tests/test_cutover_v2_provider_circuit_breaker.py

================================================================================
11. Operator Digest v2
================================================================================

Generate human-facing digest.

Files:
output/production_cutover_v2/YYYY-MM-DD/operator_digest.md
output/production_cutover_v2/YYYY-MM-DD/operator_digest.json
docs/operational/production_cutover_v2_operator_digest_sample.md

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

Acceptance:
- every item has next_action
- every pending item has follow-up task
- every scored item has support claim IDs
- every low-score item has reason
- every provider failure item is not final reject

================================================================================
12. Static Logic Audit v2
================================================================================

Implement:
src/e2r/cli/audit_production_cutover_v2_readiness.py

Critical counts:
- production_ready_despite_A2_zero_count
- live_connector_alias_to_snapshot_count
- source_task_accepted_without_live_or_fresh_provider_doc_count
- provider_failed_final_score_count
- no_result_masked_provider_failed_count
- source_proxy_to_score_count
- source_proxy_to_A2_count
- event_summary_used_as_quote_count
- contract_visible_to_raw_extractor_count
- primitive_gap_visible_to_raw_extractor_count
- forced_subject_target_count
- forced_positive_polarity_count
- forced_current_temporal_count
- cheap_scan_score_as_verified_score_count
- all_stage1_but_ready_count
- census_enabled_before_cutover_ready_count
- market_anomaly_to_score_count
- old_risk_without_current_open_to_score_count
- source_provider_gap_ignored_count
- missing_report_hash_count
- one_line_large_report_count
- unbounded_fetch_config_count

All critical counts must be 0.

Reports:
docs/operational/production_cutover_v2_static_logic_audit.json

================================================================================
13. Required Tests
================================================================================

Add or strengthen:

tests/test_cutover_v2_live_connectors_not_aliases.py
tests/test_cutover_v2_opendart_real_fetch.py
tests/test_cutover_v2_a2_real_replay_promotion.py
tests/test_cutover_v2_llm_contract_blind_extractor.py
tests/test_cutover_v2_provider_gap_blocks_ready.py
tests/test_cutover_v2_meaningful_stage_split.py
tests/test_cutover_v2_trigger_taxonomy_policy.py
tests/test_cutover_v2_census_readiness_gate.py
tests/test_cutover_v2_runtime_budget_pending.py
tests/test_cutover_v2_operator_digest.py
tests/test_cutover_v2_static_logic_audit.py
tests/test_cutover_v2_no_production_ready_with_a2_zero.py
tests/test_cutover_v2_no_census_before_cutover_ready.py

Full command:
PYTHONPATH=src python -m unittest discover -s tests -v

No skipped cutover tests allowed.

================================================================================
14. Final Reports
================================================================================

Generate:

docs/operational/production_cutover_v2_acceptance_report.md
docs/operational/production_cutover_v2_readiness_verdict.md
docs/operational/production_cutover_v2_source_connector_report.json
docs/operational/production_cutover_v2_provider_completeness_matrix.json
docs/operational/production_cutover_v2_A2_replay_promotion_report.json
docs/operational/production_cutover_v2_claim_extraction_report.json
docs/operational/production_cutover_v2_stage_distribution_report.json
docs/operational/production_cutover_v2_trigger_policy_audit.json
docs/operational/production_cutover_v2_multiday_validation.json
docs/operational/production_cutover_v2_static_logic_audit.json
docs/operational/census_mode_readiness_report.md
docs/operational/census_mode_design_backlog.json

Output:
output/production_cutover_v2/YYYY-MM-DD/
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
15. Completion Labels
================================================================================

Allowed labels:
- IMPLEMENTATION_MERGED
- LIVE_CONNECTOR_PASS
- A2_REPLAY_PASS
- LLM_EXTRACTION_PASS
- MEANINGFUL_STAGE_SPLIT_PASS
- TRIGGER_POLICY_PASS
- MULTIDAY_SHADOW_PASS
- CUTOVER_READY
- READY_FOR_CENSUS_DESIGN
- READY_FOR_CENSUS_IMPLEMENTATION

Goal completion minimum:
- LIVE_CONNECTOR_PASS
- A2_REPLAY_PASS
- LLM_EXTRACTION_PASS
- MEANINGFUL_STAGE_SPLIT_PASS
- TRIGGER_POLICY_PASS
- static critical count 0

Production cutover:
- CUTOVER_READY only if:
  - A2_REAL_REPLAY_VERIFIED_count >= 30
  - source provider blocker count = 0
  - real source connector success pass
  - meaningful stage split pass
  - multiday validation pass
  - no fixture/source_proxy/snapshot-only contamination
  - report reproducibility pass
  - full tests pass

Census:
- READY_FOR_CENSUS_DESIGN allowed if CUTOVER_READY is false but architecture is documented.
- READY_FOR_CENSUS_IMPLEMENTATION only if CUTOVER_READY is true.

================================================================================
16. Final Answer Format
================================================================================

After completion, report only:

1. Final status
2. Commit SHA / message / push status / working tree
3. Test result
4. Source connector status
5. A2 replay status
6. Claim extraction status
7. Stage distribution
8. Provider gap matrix
9. Trigger taxonomy result
10. Multiday validation
11. Census readiness label
12. Production verdict
13. Remaining blockers

================================================================================
17. Prohibitions
================================================================================

- Do not implement Census Mode in this Goal.
- Do not claim PRODUCTION_READY while A2 count is 0.
- Do not claim PRODUCTION_READY while any blocking provider gap remains.
- Do not alias LocalSnapshotConnector as LiveConnector.
- Do not treat snapshot:// as live evidence.
- Do not use source_proxy_only as score evidence.
- Do not use evidence_url_pending as replay fixture.
- Do not use event_summary as quote.
- Do not expose primitive_gap to raw extractor.
- Do not force polarity/current/subject defaults.
- Do not make market anomaly a score claim.
- Do not finalize low score on provider failure.
- Do not change scoring weights or Stage thresholds.
- Do not hardcode symbol/company/url exceptions.
- Do not output one-line huge reports.

================================================================================
18. One-line goal
================================================================================

이번 Goal의 목적은 Census Mode가 아니라,
Census Mode를 만들 수 있을 정도로 production cutover를 실제 source와 실제 claim으로 닫는 것이다.

즉:

real source connector
→ A2 replay verified evidence
→ LLM contract-blind claim extraction
→ meaningful Stage split
→ trigger/claim access policy
→ multiday validation
→ Census readiness decision

이 경로가 닫혀야 다음에 전체 티커 Stage 지도 구현으로 넘어갈 수 있다.