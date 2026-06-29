너는 Daikisong/stock_agent 레포의 E2R Production Cutover Gate v1을 구현하는 coding agent다.

현재 전제:
- Evidence OS v2는 구현되어 있다.
- Research Brain v4는 production-shadow 리포트를 만들고 있다.
- 최신 v4 리포트는 PRODUCTION_READY를 주장하지만, 정적 감사상 아직 실제 운영 readiness로 보기 어렵다.
- 이유:
  1. candidate_event_report에 fixture-like symbols(111111, 222222, 333333, 000000 등)와 cached/source fixture path가 섞여 있다.
  2. SourceAcquisitionRunnerV4는 live API/원문 fetch라기보다 stored source snapshot을 EvidenceDocument로 변환하는 구조가 남아 있다.
  3. Evidence extraction은 structured row field를 primitive로 매핑하는 경로가 남아 있어, 완전한 contract-blind 원문 claim extraction이라고 보기 어렵다.
  4. A2_REAL_REPLAY_VERIFIED promoted count가 0인데 production_ready=True가 나왔다.
  5. deterministic_scorer_output_count가 5개뿐이고, watchlist 대부분은 pending이다.
  6. report_base_commit_sha가 최신 commit SHA와 다를 수 있어 report reproducibility가 약하다.
  7. v4 report 파일 중 일부가 한 줄 JSON/MD로 생성되어 diff/audit/line-based review가 어렵다.

이번 Goal의 이름:
E2R Production Cutover Gate v1 — Real Market Live-Ready Verification

최종 목표:
실제 운영 모드에서 다음 경로를 끝까지 닫는다.

실제 KRX universe
→ 실제 official source trigger scan
→ CandidateEvent
→ real LLM Research Brain Planner
→ bounded official-first SourceTask
→ 실제 DART/KIND/KRX/CompanyGuide/IR/Report/TrustedNews source acquisition
→ EvidenceDocument / EvidenceAnchor
→ contract-blind Evidence OS claim extraction
→ target/temporal/primitive adjudication
→ accepted AdmissibleClaim
→ ScoreContributionLedger
→ DeterministicScorer
→ StageCourt
→ Daily Watchlist
→ 운영자가 볼 수 있는 READY/PENDING/REJECT 상태판

절대 원칙:
1. Research Brain은 score/stage를 직접 계산하지 않는다.
2. Research Brain output은 FeatureInput, ScoreContribution, risk field를 직접 mutate하지 않는다.
3. source snapshot은 frozen/shadow 검증에는 쓸 수 있지만, live production readiness의 real source fetch로 계산하지 않는다.
4. fixture-like symbol, synthetic company, stored fixture CSV는 production readiness candidate count에 포함하지 않는다.
5. accepted claim은 실제 source document 또는 공식 API record의 anchor를 가져야 한다.
6. event_summary, candidate_reason, planner rationale은 quote가 아니다.
7. source_proxy_only, evidence_url_pending, price_path_only memory는 current production score evidence가 아니다.
8. A2_REAL_REPLAY_VERIFIED가 0이면 PRODUCTION_READY 금지다.
9. fake provider, frozen provider, cached-only provider는 PRODUCTION_READY 금지다.
10. report_base_commit_sha는 현재 git HEAD와 정확히 일치해야 한다.
11. scoring weight와 Stage threshold는 변경하지 않는다.
12. 특정 종목명, 특정 URL, 특정 키워드 예외 처리 금지.
13. 운영 리포트가 READY를 주장하려면 실제 실행 command와 artifact hash가 재현 가능해야 한다.

================================================================================
0. 현재 v4 PRODUCTION_READY 재라벨링
================================================================================

먼저 현재 v4 산출물을 재분류하라.

생성/수정:
docs/operational/research_brain_v4_readiness_reclassification.md

내용:
- v4 report의 final_status=PRODUCTION_READY는 실제 live production readiness가 아니라 production-shadow readiness로 재라벨링한다.
- v4가 통과한 것:
  - planner schema guard
  - snapshot/source-record 기반 SourceTask execution
  - Evidence OS bridge 일부
  - deterministic scorer 일부
  - static audit counters
- v4가 아직 통과하지 못한 것:
  - real market universe only
  - no fixture-like symbol
  - live official source connector execution
  - full text claim extraction
  - A2 real replay promotion
  - multi-day real official source run
  - operational latency/budget SLA
  - report/current HEAD reproducibility

필수:
- 기존 v4 reports를 삭제하지 마라.
- v4는 PRODUCTION_SHADOW_READY 또는 READY_FOR_CUTOVER_AUDIT로 재라벨링하라.
- PRODUCTION_READY는 이번 Cutover Gate 완료 전까지 금지한다.

Acceptance:
- docs/operational/research_brain_v4_production_readiness_verdict.md에 “v4 was shadow-ready, not production-cutover-ready” 문구가 들어가야 한다.
- v4 report의 기존 수치는 보존하되 status 해석을 바로잡아라.

================================================================================
1. Report SHA / Artifact Reproducibility Gate
================================================================================

모든 운영 report는 다음 metadata를 가져야 한다.

ReportMetadata:
{
  "git_head_sha": "...",
  "report_generated_at": "...",
  "report_generator": "...",
  "command": "...",
  "config_hash": "...",
  "source_corpus_hash": "...",
  "candidate_event_hash": "...",
  "planner_prompt_hash": "...",
  "planner_response_hash": "...",
  "evidence_os_schema_version": "...",
  "scoring_schema_version": "...",
  "stage_schema_version": "...",
  "repo_dirty": false
}

필수 규칙:
- report_base_commit_sha != git HEAD이면 report invalid.
- git working tree dirty이면 PRODUCTION_READY 금지.
- report command가 없으면 PRODUCTION_READY 금지.
- source/candidate/planner/evidence/scoring hash가 없으면 PRODUCTION_READY 금지.
- JSON/MD reports는 pretty-print와 line-based review 가능 형식으로 써라.
- 한 줄짜리 대형 JSON/MD 산출물 금지.

새 감사:
src/e2r/cli/audit_operational_report_reproducibility.py

검사:
- report_head_sha_mismatch_count
- missing_command_count
- missing_config_hash_count
- one_line_large_report_count
- dirty_worktree_ready_claim_count
- report_generated_without_test_command_count

필수 결과:
모든 critical count = 0

Reports:
docs/operational/production_cutover_report_reproducibility_audit.json

================================================================================
2. Production CandidateEvent Purity Gate
================================================================================

현재 v4 candidate_event_report에는 fixture-like symbols와 sample companies가 포함되어 있다.
Production Cutover에서는 실제 KRX/DART universe에 존재하는 종목만 candidate로 인정한다.

구현:
src/e2r/production/candidate_event_purity.py

CandidateEventProductionEligibility:
- symbol must exist in KRX universe or allowed foreign universe
- symbol must not match synthetic pattern:
  - 000000
  - 111111
  - 222222
  - 333333
  - 444444
  - 555555
  - 666666
  - TEST*
  - SAMPLE*
  - fixture-only ids
- company_name must match official instrument/company registry
- source_id must not be fixtures/historical/* unless mode=frozen_replay
- source_id must not be data/raw/korea_cheap_scan fixture CSV unless mode=frozen_replay
- source_family must be verified by provider registry
- CandidateEvent must have detected_at, event_date, source_family, source_id, source anchor
- event_date cannot be after as_of_date
- stale stored_source_event cannot be counted as fresh daily event unless intentionally backfill mode

Modes:
- frozen_replay: fixtures allowed
- production_shadow: fixtures forbidden
- production_live: fixtures forbidden

Acceptance:
- production_candidate_event_count excludes all fixture-like symbols.
- fixture_candidate_event_count is reported separately.
- PRODUCTION_READY requires fixture_candidate_event_count_in_production = 0.
- cached_path_count in production candidate report must be 0 unless mode=frozen_replay.
- source_id pointing to fixture.csv must fail production purity.

Reports:
docs/operational/production_cutover_candidate_purity_report.json

Tests:
tests/test_production_candidate_event_purity.py
tests/test_production_no_fixture_symbols.py
tests/test_production_no_cached_fixture_source_ids.py

================================================================================
3. Real Official Source Connector Gate
================================================================================

SourceAcquisitionRunnerV4 currently reads stored source snapshots.
Production Cutover requires true connector execution or explicitly-labeled provider failure.

Implement:
src/e2r/production/source_connectors/
    __init__.py
    opendart_live_connector.py
    kind_live_connector.py
    krx_live_connector.py
    companyguide_live_connector.py
    issuer_ir_connector.py
    trusted_news_connector.py
    source_provider_registry.py

Each connector returns:
SourceFetchResult:
{
  "provider_name": "...",
  "source_class": "...",
  "mode": "live|snapshot|frozen",
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
  "provider_error": null
}

Rules:
- In production_live and production_shadow_live modes, source provider must actually call or load from an official provider cache generated during that run.
- Stored snapshot may be used only if it has:
  - snapshot_run_id
  - source_fetch_request_id
  - fetched_at within allowed freshness
  - provider_name
  - content_hash
  - original URL or official document id
- `snapshot://` URI alone does not count as live source.
- source task accepted claim requires SourceFetchResult with status FETCHED and content_hash.
- provider failure must stay PROVIDER_FAILED, not NO_EVIDENCE_FOUND.
- DART/KIND/KRX/CompanyGuide connector errors must be reported per provider.

SourceTaskExecution must record:
- provider_request_id
- provider_name
- provider_mode
- canonical_url
- content_hash
- document_id
- anchor_id
- claim_ids

Acceptance:
- In production_shadow_live, at least:
  - DART live connector exercised >= 1
  - KIND/KRX connector exercised >= 1
  - CompanyGuide or report connector exercised >= 1
  - issuer IR/report connector exercised >= 1 or documented source gap
- real_document_fetched_count counts only documents with provider request id and content hash.
- stored snapshot-only documents are counted separately.
- PRODUCTION_READY requires live_or_fresh_provider_document_count >= configured threshold.

Reports:
docs/operational/production_cutover_source_connector_report.json
docs/operational/production_cutover_provider_error_report.json

Tests:
tests/test_production_live_source_connectors.py
tests/test_production_source_snapshot_not_live.py
tests/test_production_provider_failure_not_no_result.py

================================================================================
4. Contract-blind Real Document Claim Extraction Gate
================================================================================

Current v4 extraction still maps structured row fields to primitives.
Production Cutover requires a contract-blind extraction phase before primitive mapping.

Implement/strengthen:
src/e2r/production/claim_extraction/
    contract_blind_extractor.py
    anchor_validator.py
    entity_temporal_adjudicator.py
    primitive_mapper.py
    extraction_audit.py

Flow:
EvidenceDocument
→ EvidenceAnchor
→ ContractBlindRawAssertionExtractor
→ AnchorValidator
→ EntityResolver
→ TemporalAdjudicator
→ PrimitiveMapper
→ derive_score_eligibility
→ AppendOnlyEvidenceLedger

Extractor input:
- target company identity/aliases
- as_of_date
- source metadata
- document text or structured official record
- no score
- no stage
- no failed green gates
- no desired primitive
- no MFE/MAE
- no outcome label

Extractor output:
RawAssertion only:
- subject
- predicate
- object/value
- polarity proposal
- modality
- event_date
- effective period
- exact quote or API/table locator
- related entities
- uncertainty reason

PrimitiveMapper may see EvidenceContract after claim extraction and adjudication.
Extraction stage must not see desired primitive.

Ban in production:
- `structured_field_presence_positive_by_contract` as final polarity
- default polarity positive
- default temporal current
- default subject target
- task.primitive_gap → accepted mapping without claim semantics
- event_summary → exact_quote
- row field existence → score claim without semantic adjudication

Allowed:
- official API structured facts can become RawAssertion if the API field itself is the claim and has locator, value, unit, date, subject.
- structured API extraction must still pass target/temporal/primitive mapping.

Acceptance:
- forced_positive_polarity_count = 0
- forced_current_temporal_count = 0
- forced_target_subject_count = 0
- event_summary_used_as_exact_quote_count = 0
- primitive_gap_direct_to_mapping_count = 0
- contract_visible_to_raw_extractor_count = 0
- source_field_existence_to_score_without_adjudication_count = 0
- accepted claim must have:
  - document_id
  - anchor_id
  - quote/table/API locator
  - subject_entity_id
  - target_entity_id
  - temporal_status
  - mapping accepted
  - score eligibility result

Reports:
docs/operational/production_cutover_claim_extraction_audit.json

Tests:
tests/test_contract_blind_extraction_no_primitive_leak.py
tests/test_no_default_positive_current_target.py
tests/test_structured_api_claim_requires_adjudication.py
tests/test_event_summary_never_quote.py

================================================================================
5. Real LLM Planner Provider Gate
================================================================================

Current report says real provider success, but endpoint is codex-cli and model may be null.
Production Cutover requires planner provider identity and reproducibility.

PlannerProviderRun must record:
- provider_name
- endpoint
- model
- command
- prompt_hash
- response_hash
- raw_response_path
- schema_validation_status
- rejected_by_validator
- latency_ms
- cost/token estimate if available
- provider_mode
- is_real_provider

Rules:
- model cannot be null in production_ready report.
- endpoint cannot be vague if provider is counted as real.
- frozen planner snapshot is shadow, not production live.
- Codex CLI is allowed only if raw prompt/response hash is saved and provider identity is clear.
- Planner output may propose SourceTasks only.
- Planner output score/stage/hard_break/current_score_eligible keys cause rejection.

Acceptance:
- real_planner_success_count >= 30 over production shadow.
- raw prompt/response files saved for each planner run.
- planner_provider_model_null_count = 0.
- planner_response_missing_hash_count = 0.
- planner_schema_reject_count reported.
- fake/frozen provider used count = 0 for production-ready.

Reports:
docs/operational/production_cutover_planner_provider_report.json

Tests:
tests/test_production_planner_provider_identity.py
tests/test_production_planner_prompt_response_hash.py
tests/test_production_planner_no_model_null.py

================================================================================
6. Real Score/Stage Meaning Gate
================================================================================

Production Watchlist score must be meaningful and on the canonical E2R scale.

Current v4 has verified_score values like 4.3333 for accepted CompanyGuide claims.
This may be mathematically valid if only tiny primitive contribution exists, but the report must make it explicit.

Implement:
ScoreMeaningAudit:
- canonical_score_scale_min/max
- score_contribution_component_count
- accepted_claim_to_component_map
- primitive_coverage_pct
- expected max score under current evidence
- why score is low/high
- score_valid_status reason
- stage decision reason

Rules:
- `verified_score` is allowed to be low, but it must be explainable by ScoreContributionLedger.
- A watchlist item with accepted claims but tiny score must say “insufficient primitive coverage”, not look like a final rejection unless material gaps are nonmaterial.
- StageCourt trace must include:
  - score interval
  - missing green primitives
  - missing yellow primitives
  - hard break status
  - score contribution IDs
  - provider/material gap status
- If accepted claims support only one minor primitive, score_valid should be FINAL_WITH_NONMATERIAL_GAPS only if remaining gaps cannot change stage boundary. Otherwise PENDING_MATERIAL_GAPS.

Acceptance:
- watchlist item with verified_score not null has full score explanation.
- deterministic_scorer_output_count >= 15 across production shadow, or report says NOT_READY.
- final score status must distinguish:
  - FINAL
  - FINAL_WITH_NONMATERIAL_GAPS
  - PENDING_MATERIAL_GAPS
  - PROVIDER_FAILED
  - INVALID_EVIDENCE
- If 25/30 watchlist rows are pending, PRODUCTION_READY forbidden unless explicitly “shadow observation mode” and not cutover.

Reports:
docs/operational/production_cutover_score_meaning_audit.json

Tests:
tests/test_score_meaning_audit.py
tests/test_low_verified_score_explained_by_contributions.py
tests/test_pending_material_gaps_block_final_reject.py

================================================================================
7. Real Daily Production Shadow Run
================================================================================

Implement a new entrypoint:

src/e2r/cli/run_e2r_production_cutover_shadow.py

Required arguments:
--as-of-date
--mode production_shadow_live|production_live_dry_run|frozen_replay
--planner-provider real
--source-mode live_official_first
--candidate-min-count 50
--sector-min-events 3
--max-source-tasks-per-candidate 5
--max-fetches-per-task 3
--output-dir output/production_cutover/YYYY-MM-DD
--fail-on-critical-audit true

Flow:
1. Build actual KRX universe.
2. Run official cheap scan.
3. Run DART/KIND/KRX event scan.
4. Run CompanyGuide/report radar.
5. Run issuer IR/report snapshot only if fresh and provider-sourced.
6. Create CandidateEventV2.
7. Apply CandidateEvent purity filter.
8. Cluster events by symbol.
9. Run real planner.
10. Generate bounded SourceTasks.
11. Execute real source connectors.
12. Run contract-blind extraction.
13. Run Evidence OS.
14. Run deterministic scorer/stage.
15. Emit daily watchlist.
16. Emit full audit bundle.

Minimum production shadow acceptance:
- actual_krx_universe_count > 1000
- candidate_event_count >= 50 or market/provider gap documented
- production_eligible_candidate_event_count >= 30
- fixture_candidate_event_count = 0
- real_planner_success_count >= 30
- real_source_document_fetched_count >= 50
- Evidence OS accepted claim count >= 20
- deterministic_scorer_output_count >= 15
- at least 5 non-pending watchlist items
- sector coverage:
  - at least 6 large sectors with candidate attempts
  - each active large sector has source gap if no candidate
- provider failure rows pending, not final score
- static audit critical count = 0

Reports:
output/production_cutover/YYYY-MM-DD/
  candidate_events.json
  planner_runs.json
  source_tasks.json
  source_task_executions.json
  evidence_claim_ledger.jsonl
  score_contributions.jsonl
  stagecourt_traces.json
  daily_watchlist.json
  daily_watchlist.md
  audit_summary.json

docs/operational/production_cutover_shadow_latest.md
docs/operational/production_cutover_shadow_latest.json

Tests:
tests/test_production_cutover_shadow_entrypoint.py
tests/test_production_cutover_no_fixture_candidates.py
tests/test_production_cutover_real_source_required.py

================================================================================
8. Multi-day Live/Snapshot Validation
================================================================================

Production ready requires more than one day.

Run:
- 10 trading-day frozen replay using source snapshots captured by production cutover shadow
- 5 live official-source dry runs
- same config repeated 3 times for at least 3 frozen days
- score/stage variance must be 0 for frozen repeats
- provider failures must be stable and explicit
- no source_proxy_to_score
- no fixture candidates

Metrics:
- day_count
- candidate_event_count per day
- eligible_candidate_event_count per day
- planner success per day
- source fetched per day
- accepted claims per day
- scored items per day
- watchlist sections per day
- variance
- provider gap
- critical audit count

Acceptance:
- 10 frozen days pass
- 5 live official dry runs pass
- repeated frozen variance = 0
- fake/frozen planner provider in live = 0
- fixture candidate in live = 0
- production-ready only if all critical audit count = 0

Reports:
docs/operational/production_cutover_multiday_validation.json
docs/operational/production_cutover_stability_report.md

Tests:
tests/test_production_cutover_multiday_validation.py
tests/test_production_cutover_frozen_repeatability.py

================================================================================
9. Research Memory Production Usage Audit
================================================================================

Re-audit historical research memory one final time.

Rules:
- C06/C08/C15 URL-backed rows may be A2 only after real fetch/snapshot anchor verification.
- C24/C28/C17 source_proxy/evidence_url_pending rows remain ontology/source-route/false-positive memory.
- source_proxy_only rows cannot become production fixture.
- price outcome cannot enter planner prompt except as aggregate pattern summary.
- MFE/MAE cannot enter claim extraction prompt.

Required reports:
docs/operational/production_cutover_research_memory_usage_audit.json

Critical counts:
- source_proxy_to_score_count = 0
- source_proxy_to_A2_count = 0
- evidence_url_pending_to_fixture_count = 0
- price_outcome_in_extraction_prompt_count = 0
- raw_future_label_in_planner_prompt_count = 0

Reference examples:
- C06 URL-backed HBM sold-out and revenue mix may become A2 after actual source replay.
- C08 URL-backed customer/order examples may become A2 after source replay.
- C15 URL-backed pass-through examples may become A2 after source replay.
- C24/C28/C17 source_proxy rows stay ontology-only until URL repair.

================================================================================
10. Latency / Budget / Operational SLA
================================================================================

A system that never finishes is not operational.

Implement SLA audit:
- total runtime
- planner runtime
- source acquisition runtime
- extraction runtime
- scoring runtime
- max candidate runtime
- max source task runtime
- API call count
- LLM call count
- retry count
- cache hit/miss
- cost estimate if available

Production defaults:
- no top_results=None
- no retry_max=None
- max source tasks per candidate <= 5
- max fetches per task <= 3
- max planner batch size bounded
- max total live run wall time configurable
- if wall time exceeded, remaining candidates become PENDING_RUNTIME_BUDGET

Acceptance:
- daily shadow run completes under configured max runtime
- no unbounded fetch
- budget-exhausted candidates pending, not final reject
- SLA report generated

Reports:
docs/operational/production_cutover_sla_report.json

Tests:
tests/test_production_cutover_sla_budget.py

================================================================================
11. Alert / Operator Workflow
================================================================================

Create operator-facing outputs.

Daily Watchlist sections:
- Stage3-Green
- Stage3-Yellow-Pending
- Stage2-Actionable
- Stage2-Watch
- 4B-watch
- Reject/Red
- Provider/Source Pending
- Planner Pending
- Runtime Budget Pending

Each item must show:
- why it triggered
- primary archetype
- Research MemoryCard used
- accepted claims
- score contributions
- missing primitives
- next source tasks
- red-team checks
- score/stage validity
- operator action:
  - WATCH
  - INVESTIGATE
  - IGNORE
  - RECHECK_SOURCE
  - RISK_REVIEW

No direct buy/sell recommendation language.

Outputs:
output/production_cutover/YYYY-MM-DD/operator_digest.md
output/production_cutover/YYYY-MM-DD/operator_digest.json

Acceptance:
- operator digest generated
- every item has next_action
- every pending item has reason and follow-up task
- every Green/Yellow item has supporting claim IDs

================================================================================
12. Final Static Logic Audit
================================================================================

Implement:
src/e2r/cli/audit_production_cutover_readiness.py

Critical checks:
- current_head_sha_mismatch_count
- dirty_worktree_ready_count
- fixture_candidate_in_production_count
- cached_fixture_source_in_production_count
- snapshot_only_counted_as_live_count
- source_task_accepted_without_provider_fetch_count
- synthetic_assertion_count
- event_summary_used_as_quote_count
- default_positive_polarity_count
- default_current_temporal_count
- default_target_subject_count
- primitive_gap_direct_mapping_count
- contract_visible_to_raw_extractor_count
- source_proxy_to_score_count
- source_proxy_to_A2_count
- evidence_url_pending_to_fixture_count
- future_outcome_in_extraction_prompt_count
- MFE_MAE_in_current_prompt_count
- accepted_claim_without_anchor_count
- accepted_claim_without_date_count
- accepted_claim_without_subject_target_adjudication_count
- score_without_claim_count
- hard_break_without_current_open_direct_claim_count
- provider_failed_final_score_count
- pending_material_gap_final_reject_count
- cheap_scan_score_as_verified_score_count
- deterministic_scorer_output_below_min_count
- unbounded_fetch_config_count
- one_line_large_report_count
- production_ready_with_blockers_count

All critical counts must be 0.

Warnings:
- provider failure rate high
- accepted claim rate low
- sector coverage gap
- A2 promotion gap
- candidate count low

Reports:
docs/operational/production_cutover_static_logic_audit.json

================================================================================
13. Required Test Suite
================================================================================

Add or strengthen:

tests/test_cutover_report_reproducibility.py
tests/test_cutover_candidate_event_purity.py
tests/test_cutover_real_source_connectors.py
tests/test_cutover_snapshot_not_live.py
tests/test_cutover_contract_blind_extraction.py
tests/test_cutover_no_default_positive_current_target.py
tests/test_cutover_planner_provider_identity.py
tests/test_cutover_score_meaning_audit.py
tests/test_cutover_daily_shadow_entrypoint.py
tests/test_cutover_multiday_validation.py
tests/test_cutover_research_memory_usage_policy.py
tests/test_cutover_sla_budget.py
tests/test_cutover_operator_digest.py
tests/test_cutover_static_logic_audit.py
tests/test_cutover_no_production_ready_with_blockers.py

Full command:
PYTHONPATH=src python -m unittest discover -s tests -v

Required:
- all tests pass
- no skipped production cutover tests
- report includes pass/fail/skip count
- tests must fail if fixture-like candidate appears in production mode
- tests must fail if source snapshot is counted as live source without provider run id
- tests must fail if PRODUCTION_READY is claimed with A2 promoted count 0

================================================================================
14. Production Readiness Labels
================================================================================

Allowed labels:
- IMPLEMENTATION_MERGED
- REPORT_REPRODUCIBILITY_PASS
- CANDIDATE_PURITY_PASS
- REAL_SOURCE_CONNECTOR_PASS
- CONTRACT_BLIND_EXTRACTION_PASS
- REAL_PLANNER_IDENTITY_PASS
- REAL_SCORE_STAGE_PASS
- DAILY_PRODUCTION_SHADOW_PASS
- MULTIDAY_SHADOW_PASS
- OPERATOR_DIGEST_PASS
- PRODUCTION_CUTOVER_READY

Goal completion minimum:
DAILY_PRODUCTION_SHADOW_PASS + all critical static audit count 0

Actual production cutover:
PRODUCTION_CUTOVER_READY only if:
- report reproducibility pass
- candidate purity pass
- real source connector pass
- contract-blind extraction pass
- real planner identity pass
- real score/stage pass
- multi-day validation pass
- operator digest pass
- source_proxy_to_score = 0
- fixture candidate in production = 0
- A2 promoted count > 0 or explicit A2 source provider gap with NOT_READY
- deterministic_scorer_output_count >= configured minimum
- no production blockers

================================================================================
15. Final Reports
================================================================================

Generate:

docs/operational/production_cutover_acceptance_report.md
docs/operational/production_cutover_readiness_verdict.md
docs/operational/production_cutover_report_reproducibility_audit.json
docs/operational/production_cutover_candidate_purity_report.json
docs/operational/production_cutover_source_connector_report.json
docs/operational/production_cutover_provider_error_report.json
docs/operational/production_cutover_claim_extraction_audit.json
docs/operational/production_cutover_planner_provider_report.json
docs/operational/production_cutover_score_meaning_audit.json
docs/operational/production_cutover_shadow_latest.md
docs/operational/production_cutover_shadow_latest.json
docs/operational/production_cutover_multiday_validation.json
docs/operational/production_cutover_stability_report.md
docs/operational/production_cutover_research_memory_usage_audit.json
docs/operational/production_cutover_sla_report.json
docs/operational/production_cutover_static_logic_audit.json

Output:
output/production_cutover/YYYY-MM-DD/
  candidate_events.json
  planner_runs.json
  source_tasks.json
  source_task_executions.json
  evidence_documents.jsonl
  evidence_anchors.jsonl
  evidence_claim_ledger.jsonl
  primitive_states.jsonl
  score_contributions.jsonl
  stagecourt_traces.json
  daily_watchlist.json
  daily_watchlist.md
  operator_digest.md
  operator_digest.json
  audit_summary.json

================================================================================
16. Final Answer Format
================================================================================

After completion, report only in this format:

1. Final status
- IMPLEMENTATION_MERGED / REPORT_REPRODUCIBILITY_PASS / CANDIDATE_PURITY_PASS / REAL_SOURCE_CONNECTOR_PASS / CONTRACT_BLIND_EXTRACTION_PASS / REAL_PLANNER_IDENTITY_PASS / REAL_SCORE_STAGE_PASS / DAILY_PRODUCTION_SHADOW_PASS / MULTIDAY_SHADOW_PASS / OPERATOR_DIGEST_PASS / PRODUCTION_CUTOVER_READY

2. Commit
- SHA
- message
- push status
- working tree clean

3. Tests
- command
- passed / failed / skipped
- failed test names if any

4. Report reproducibility
- git_head_sha
- report_head_sha
- dirty_worktree
- config/source/candidate/planner/evidence/scoring hashes
- one-line report count

5. Candidate purity
- total candidate events
- production eligible candidate events
- fixture candidate count
- cached fixture source count
- sector coverage

6. Planner
- real provider name/model/endpoint
- real success/failure
- prompt/response hash count
- fake/frozen provider count
- validator reject count

7. Source connectors
- DART/KIND/KRX/CompanyGuide/IR/trusted news call counts
- fetched documents
- provider failures
- snapshot-only documents
- source gaps

8. Evidence extraction
- real documents to assertions
- assertions to claims
- accepted claims
- synthetic/default/forced counts
- wrong-subject rejections
- historical-only rejections

9. Score/Stage
- deterministic scorer outputs
- StageCourt traces
- watchlist sections
- pending material gaps
- score contribution count
- score without claim count

10. Multi-day validation
- day count
- repeat variance
- accepted claim totals
- deterministic stage totals
- source/provider failures

11. Operator digest
- item count
- next action counts
- Green/Yellow/Stage2/Watch/Reject/Pending counts

12. Production verdict
- READY / NOT_READY
- blockers
- exact next step

================================================================================
17. Prohibitions
================================================================================

- Do not claim PRODUCTION_READY from v4 report alone.
- Do not count fixture symbols as production candidates.
- Do not count snapshot:// documents as live source fetches.
- Do not use event_summary as quote.
- Do not use structured field presence as final positive polarity without adjudication.
- Do not allow source_proxy_only or evidence_url_pending rows to score.
- Do not promote A2 without real fetch/snapshot anchor and claim replay.
- Do not use cheap_scan_total_score as verified_score.
- Do not finalize low score on provider failure.
- Do not change scoring weights or Stage thresholds.
- Do not hardcode symbol/company/url exceptions.
- Do not generate one-line huge reports.
- Do not push without full test and cutover reports.

================================================================================
18. One-line goal
================================================================================

이번 Goal의 목적은 “Research Brain v4가 좋아 보인다”가 아니라,
실제 운영에서 매일 돌려도 되는지 증명하는 것이다.

즉:

실제 시장 event
→ 실제 source
→ 실제 원문 claim
→ 실제 Evidence OS accepted claim
→ 실제 deterministic score/stage
→ 실제 operator watchlist

이 경로가 fixture, snapshot-only, source_proxy, cheap score, synthetic assertion 없이 닫혀야 한다.