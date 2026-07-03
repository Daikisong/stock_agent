너는 Daikisong/stock_agent 레포의 E2R Census v4 / Meaningful Operational Stage Gate를 구현하는 coding agent다.

이번 Goal은 단순 기능 추가가 아니다.

이번 Goal의 목적은 다음 세 작업을 한 번에 닫는 것이다.

A. Census v3의 anti-fake full-universe status board를 runtime-proven leaf artifact 기반으로 검증한다.
B. Census v3 audit에서 발견된 Stage/score/trace atomicity, score scale, Stage2-Watch 의미 혼동, semantic primitive noise를 고친다.
C. Research Brain + Web/Naver/IR/Report acquisition이 실제로 실행되었는지, 또는 실행되지 않았다면 그 라벨을 정직하게 낮추는 Gate를 만든다.

현재 전제:
- Evidence OS v2의 기본 철학은 유지한다.
- Production Cutover v3는 CUTOVER_READY였다.
- Census v3는 c5bc76a에서 구현되고 baaf2e7에서 acceptance report push 상태가 갱신되었다.
- baaf2e7은 report-only commit이다.
- Census v3 acceptance report는 FULL_UNIVERSE_STAGE_MAP_PASS를 주장한다.
- 하지만 docs/0701/census_v3_stage_map_audit_2026-07-01.md의 독립 감사는 현재 결과를 “운영 확정 Stage 지도”가 아니라 “가짜 점수 방지용 전체 상태판”에 가깝다고 판정했다.
- 현재 v3 결과에는 다음 문제가 있다.
  1. Stage/score/status/trace가 한 원자적 StageCourt 결과에서 오지 않는 사례가 있다.
  2. 삼부토건 001470은 최종 row가 Stage2-Watch / 4.4인데 연결 trace는 Stage1 / 4.0이다.
  3. SK하이닉스 000660은 최종 score_interval_lower와 linked stagecourt trace score_interval이 다르다.
  4. verified_score가 full E2R 100점인지, 단일 공식 이벤트 점수인지 섞인다.
  5. Stage2-Watch가 canonical Stage2인지, official event watch signal인지 혼동된다.
  6. 자기주식취득신탁계약/주식담보제공계약 같은 금융·관리성 계약이 contract_quality/earnings_visibility로 샐 수 있다.
  7. 삼성전자/하이닉스 Census row는 HBM/C06 full thesis score가 아니라 최근 DART 이벤트 점수다.
  8. Research Brain + Naver/Web/IR/Report acquisition이 실제로 돈 것인지 leaf artifact로 명확히 증명되지 않았다.

이번 Goal 이름:
E2R Census v4 — Atomic Stage Decision, Score Scale Split, Semantic Primitive Guard, Real Brain/Web Evidence Gate

한 줄 목표:
전체 KRX universe 상태판을 “운영 확정 Stage 지도”처럼 보이게 만드는 것이 아니라,
각 row가 어떤 종류의 Stage/점수인지 정직하게 구분하고,
full thesis Stage가 필요한 후보는 Research Brain + official/web/IR/report SourceTask + Evidence OS + StageCourt로 실제 trace를 닫으며,
그 trace가 같은 원자적 StageCourt 결과에서 나왔음을 증명하는 것이다.

절대 원칙:
1. report 숫자는 source of truth가 아니다. leaf artifacts와 atomic trace가 source of truth다.
2. `ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS`와 `MEANINGFUL_OPERATIONAL_STAGE_PASS`를 분리한다.
3. `FULL_UNIVERSE_STAGE_MAP_PASS`는 현재처럼 모호하게 쓰지 않는다. 의미를 바꾸거나 폐기한다.
4. `verified_score`는 `score_scale=FULL_E2R_100`일 때만 허용한다.
5. 단일 공식 이벤트 점수는 `event_evidence_score`로만 표시한다.
6. raw contribution fallback은 `raw_contribution_score` 또는 `event_evidence_score`로만 표시한다.
7. `Stage2-Watch`는 canonical Stage2와 watch signal을 분리한다.
8. 최종 Census row의 stage/score/status/trace/claims/contributions는 하나의 `AtomicStageDecision`에서 와야 한다.
9. 여러 날짜/여러 이벤트/여러 trace를 종목 단위로 합칠 때, representative decision 하나를 고르고 나머지는 additional/backlog trace로 분리한다.
10. DART title에 “계약”이 있다는 이유로 `contract_quality`나 `earnings_visibility`를 열지 않는다.
11. 자기주식취득신탁, 주식담보, 유상증자, 지분증권, 해명공시, 정정/관리성 공시는 revenue-facing contract가 아니다.
12. 삼성전자/하이닉스 C06/HBM full thesis refresh와 daily DART event score를 같은 필드에 넣지 않는다.
13. Research Brain/Web/Naver/IR/Report가 실행되지 않았으면 실행됐다고 말하지 않는다.
14. 네이버/웹검색은 전 종목 무차별 실행이 아니라 L3/L4 이상 선별 후보에 bounded source task로만 실행한다.
15. snippets/headlines는 score evidence가 아니다. full source, quote/date/subject/target/current validation이 있어야 한다.
16. source_proxy_only/evidence_url_pending/price_path_only research memory는 score evidence가 아니다.
17. provider failure는 low score나 Red가 아니라 Pending이다.
18. 최근 공시 window는 Stage cutoff가 아니다. 마지막 유효 thesis/lifecycle이 기준이다.
19. scoring weights와 Stage threshold는 바꾸지 않는다.
20. 특정 종목명/URL/키워드 예외 처리 금지.
21. 실패하면 원인 파일/함수까지 찾고, 패치하고, 같은 명령으로 재실행한다.
22. 외부 API/키/계약/네트워크 장애만 `EXTERNAL_PROVIDER_BLOCKER_NOT_READY`로 남길 수 있다. 코드 wiring/semantic/audit 결함은 반드시 고친다.

================================================================================
0. 내부 통합 플랜 작성
================================================================================

코드 패치 전에 반드시 내부 계획 문서를 작성하라.

생성:
docs/operational/census_mode_v4_internal_patch_plan.md

이 문서는 세 묶음으로 나눈다.

Bundle A — Runtime Proof / Anti-Fake Hardening
- legacy runner lockout
- leaf artifact manifest
- report generated from leaf audit only
- claim-to-stage trace forensic audit
- source task realness audit
- known-bad regression

Bundle B — Meaningful Stage Semantics
- AtomicStageDecision
- score field split
- Stage2-Watch meaning split
- investigation_status split
- risk overlay split
- semantic primitive guard
- official claim counters

Bundle C — Real Brain/Web Evidence Gate
- LLM planner run trace
- Naver/Web/TrustedNews/IR/Report acquisition task
- LLM claim extractor trace
- official-first validator
- full thesis refresh task
- Samsung/Hynix C06/HBM smoke separation

Acceptance:
- internal_patch_plan exists.
- each bundle has file targets, test targets, output artifacts, acceptance gates.
- coding begins only after this plan is written.
- final acceptance report must include which bundle passed.

================================================================================
1. docs/0701 Audit Packet Ingestion
================================================================================

The two user-provided audit files must become tracked operational artifacts.

Input files:
- docs/0701/README.md
- docs/0701/census_v3_stage_map_audit_2026-07-01.md

If these files are not yet in the repo:
- add them exactly under docs/0701/
- do not silently rewrite their conclusions
- cite them in v4 acceptance report as the motivating audit

Also create:
docs/operational/census_mode_v3_forensic_review.md

Must include:
- Census v3 is useful as anti-fake status board.
- Census v3 is not yet meaningful operational Stage map.
- non-Stage0 count = 85
- claim/score/StageCourt trace rows = 74
- Stage2-Watch = 37
- Red = 1
- Stage3-Green/Yellow = 0
- Samsung/Hynix rows are DART event scores, not HBM full thesis scores.
- Sambo/Hyundai mismatch examples.
- list of P0/P1 patch requirements from docs/0701.

Acceptance:
- docs/0701 exists in git.
- census_mode_v3_forensic_review.md exists.
- v3 PASS labels are reinterpreted as `ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS`, not `MEANINGFUL_OPERATIONAL_STAGE_PASS`.

================================================================================
2. Readiness Label Split
================================================================================

Current v3 `FULL_UNIVERSE_STAGE_MAP_PASS` is ambiguous.

Introduce labels:

A. ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
Meaning:
- every eligible symbol has a row
- no claimless nonzero score
- no source_proxy_to_score
- no provider failure final score
- no price-only score
- Stage0/NoCurrentCatalyst rows are safe
- some official event/watch rows may exist
- does NOT mean operational full thesis score quality

B. MEANINGFUL_OPERATIONAL_STAGE_PASS
Meaning:
- Stage/score/status/trace/claims/contributions come from same AtomicStageDecision
- score scale is explicit
- full_e2r_verified_score only when FULL_E2R_100
- event score is separated from full thesis score
- Stage2/Red/4B/4C semantics are not mixed
- semantic primitive guard passes
- full thesis controlled smoke passes
- Research Brain/Web evidence gate is honest

C. FULL_THESIS_REFRESH_PASS
Meaning:
- selected high-priority symbols have full thesis refresh tasks
- Research Brain planner ran
- official/web/IR/report acquisition ran where required
- Evidence OS accepted claims support full thesis components
- deterministic StageCourt produced full thesis status

D. BRAIN_WEB_EVIDENCE_PASS
Meaning:
- LLM planner call count > 0
- web/news/IR/report acquisition count > 0
- LLM claim extractor or structured official extractor produced accepted claims
- snippets did not score
- official-first rule passed

Rules:
- `FULL_UNIVERSE_STAGE_MAP_PASS` cannot be used alone anymore.
- If retained, it must expand to:
  - ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
  - plus explicit statement whether MEANINGFUL_OPERATIONAL_STAGE_PASS is true or false.
- `READY_FOR_DAILY_TRIGGER_INTEGRATION` requires at least ANTI_FAKE pass + atomic trace pass.
- `READY_FOR_OPERATIONAL_STAGE_USE` requires MEANINGFUL_OPERATIONAL_STAGE_PASS.
- `READY_FOR_FULL_THESIS_OPERATION` requires FULL_THESIS_REFRESH_PASS.

Tests:
tests/test_census_v4_readiness_label_split.py
tests/test_census_v4_no_ambiguous_full_universe_stage_map_pass.py

Acceptance:
- v4 readiness report has separate labels.
- v3 report-only label cannot imply operational Stage quality.
- if MEANINGFUL_OPERATIONAL_STAGE_PASS is false, final report must say why.

================================================================================
3. AtomicStageDecision
================================================================================

Implement:
src/e2r/census/atomic_stage_decision.py

Schema:

AtomicStageDecision:
{
  "atomic_stage_decision_id": "...",
  "symbol": "...",
  "company_name": "...",
  "as_of_date": "...",
  "candidate_event_id": "...",
  "source_task_ids": [],
  "source_task_execution_ids": [],
  "stagecourt_trace_id": "...",
  "base_stage": "...",
  "canonical_stage": "...",
  "stage_signal": "...",
  "risk_stage_signal": null,
  "transition_overlay": "NONE|4A|4B|4C",
  "stage_decision_status": "FINAL|PENDING_MATERIAL_GAPS|PROVIDER_PENDING|SOURCE_PENDING|EVENT_WATCH_ONLY|NO_CURRENT_CATALYST|RISK_REVIEW",
  "score_scale": "FULL_E2R_100|EVENT_WEIGHTED_PARTIAL|RAW_CONTRIBUTION_SUM|NO_SCORE",
  "score_source": "STAGECOURT_SCORE_INTERVAL|WATCHLIST_WEIGHTED_SCORE|RAW_CONTRIBUTION_FALLBACK|NONE",
  "event_evidence_score": null,
  "full_e2r_verified_score": null,
  "raw_contribution_score": null,
  "score_interval_lower": null,
  "score_interval_upper": null,
  "score_valid_status": "...",
  "accepted_claim_ids": [],
  "score_contribution_ids": [],
  "primitive_state_ids": [],
  "failed_stage_gates": [],
  "missing_primitives": [],
  "material_gap_ids": [],
  "source_cutover_date": "...",
  "is_representative": true,
  "additional_stage_decision_ids": []
}

Rules:
- CensusStageStatus for claim-backed rows must be built from exactly one representative AtomicStageDecision.
- `base_stage`, `stage_signal`, `risk_stage_signal`, `score fields`, `score_valid_status`, `accepted_claim_ids`, `score_contribution_ids`, and `stagecourt_trace_id` must all come from that same decision.
- Do not mix stage from trace A, score from watch row B, status from row C, trace id from trace D.
- If multiple stage decisions exist for a symbol:
  - choose representative by deterministic policy
  - preserve all others in additional_stage_decision_ids
  - report conflict summary
- Representative selection policy:
  1. Prefer full thesis decision over daily event decision.
  2. Prefer current direct risk decision for risk overlay.
  3. Prefer higher assessment depth only if score scale comparable.
  4. Never compare FULL_E2R_100 and EVENT_WEIGHTED_PARTIAL as same score.
  5. If conflict remains, mark `stage_decision_status=SOURCE_PENDING` or `TRACE_CONFLICT`, not final.

Hard fail:
- stage_trace_stage_mismatch_count > 0
- stage_trace_score_interval_mismatch_count > 0
- stage_trace_score_status_mismatch_count > 0
- stage_trace_claim_set_mismatch_count > 0
- stage_trace_contribution_set_mismatch_count > 0

Tests:
tests/test_census_v4_atomic_stage_decision.py
tests/test_census_v4_sambo_trace_mismatch_fails.py
tests/test_census_v4_multiple_trace_representative_selection.py
tests/test_census_v4_trace_score_interval_mismatch_fails.py

================================================================================
4. Score Field Split and verified_score Deprecation
================================================================================

Current `verified_score` is misleading.

Change schema:

Deprecated:
- verified_score

New:
- full_e2r_verified_score
- event_evidence_score
- raw_contribution_score
- score_scale
- score_source
- score_semantics

Score scale meanings:
- FULL_E2R_100:
  full E2R deterministic score on canonical 0~100 scale.
- EVENT_WEIGHTED_PARTIAL:
  limited event/source-task score, not full company thesis.
- RAW_CONTRIBUTION_SUM:
  simple sum of raw contribution points; diagnostics only unless promoted by scorer.
- NO_SCORE:
  no scoring.

Rules:
- `full_e2r_verified_score` may be non-null only if score_scale=FULL_E2R_100.
- `event_evidence_score` is used for single DART/event scores.
- `raw_contribution_score` is used for fallback/raw contribution diagnostics.
- `verified_score` may remain only as deprecated alias in reports, but must be null unless score_scale=FULL_E2R_100.
- If any row displays `verified_score` with score_scale != FULL_E2R_100, hard fail.
- Stage2-Watch with event score 1.5~4.4 must be shown as `event_evidence_score`, not `verified_score`.
- Red row with event score must show `risk_stage_signal`, not imply score-driven Red.

Audit counts:
- verified_score_not_full_e2r_count
- score_scale_missing_count
- score_source_missing_count
- score_scale_mixed_fallback_count
- raw_contribution_fallback_as_verified_score_count
- event_evidence_score_present_count
- full_e2r_verified_score_present_count

Tests:
tests/test_census_v4_score_field_split.py
tests/test_census_v4_verified_score_only_full_e2r.py
tests/test_census_v4_event_score_not_verified_score.py

================================================================================
5. Stage Signal Split
================================================================================

Stage2-Watch currently hides two meanings.

Add fields:
- canonical_stage
- stage_signal
- risk_stage_signal
- investigation_status
- stage_decision_status
- transition_overlay

stage_signal enum:
- NO_CURRENT_CATALYST
- OFFICIAL_EVENT_WATCH
- MATERIAL_CLAIM_WATCH
- FULL_THESIS_STAGE
- FULL_THESIS_PENDING
- PROVIDER_PENDING
- SOURCE_PENDING
- RISK_REVIEW
- EVIDENCE_INSUFFICIENT
- TRACE_CONFLICT

risk_stage_signal enum:
- NONE
- RISK_REVIEW
- CURRENT_DIRECT_RISK
- HISTORICAL_RISK_ONLY
- HARD_BREAK_CANDIDATE
- HARD_BREAK_CONFIRMED

Rules:
- `Stage2-Watch` is not enough. It must have stage_signal.
- Most current Census v3 Stage2-Watch rows should become:
  - canonical_stage = Stage1 or Stage2-Watch depending policy
  - stage_signal = MATERIAL_CLAIM_WATCH or OFFICIAL_EVENT_WATCH
  - stage_decision_status = PENDING_MATERIAL_GAPS if gaps remain
- `investigation_status=COMPLETE` is allowed only when no material gap remains.
- PENDING_MATERIAL_GAPS row cannot be COMPLETE.
- Red/Reject/4B/4C must show risk_stage_signal or transition_overlay.
- Red due risk must not look score-driven.

Hard fail:
- pending_material_marked_complete_count > 0
- stage2_without_stage_signal_count > 0
- red_without_risk_signal_or_trace_count > 0
- source_pending_marked_red_count > 0

Tests:
tests/test_census_v4_stage_signal_split.py
tests/test_census_v4_pending_material_not_complete.py
tests/test_census_v4_red_requires_risk_signal.py

================================================================================
6. Semantic Primitive Guard for Contracts
================================================================================

현재 `contract_quality`가 너무 넓다.

Implement:
src/e2r/evidence/contract_semantic_classifier.py
src/e2r/evidence/primitive_semantic_guard.py
configs/e2r_contract_semantic_guard_v1.json

Contract/event classes:
- commercial_supply_contract
- customer_order_or_backlog
- framework_agreement_without_revenue_visibility
- capacity_or_delivery_contract
- financial_contract
- shareholder_return_contract
- share_buyback_trust_contract
- pledge_or_collateral_contract
- equity_issuance_or_security_registration
- capital_allocation_event
- administrative_disclosure
- clarification_or_rumor_response
- information_confidence_only
- risk_or_listing_event
- unrelated_contract_or_wrong_subject

Rules:
`contract_quality -> earnings_visibility` allowed only if:
- target company direct
- commercial/customer/product/service scope exists
- counterparty/customer or product/service is identifiable
- revenue/volume/order value/period/backlog/shipment or margin conversion exists
- not share buyback trust
- not pledge/collateral
- not equity issuance/security registration
- not rumor clarification
- not administrative disclosure
- not pure capital allocation
- not wrong subject

Mapping examples:
- 단일판매공급계약 with amount/period/counterparty → commercial_supply_contract / customer_order_or_backlog
- 자기주식취득신탁계약체결결정 → shareholder_return_contract / capital_allocation_event, not earnings_visibility
- 주식담보제공계약체결 → pledge_or_collateral_contract / risk_or_capital_event, not contract_quality
- 유상증자결정 / 증권신고서 → capital_allocation_event / information_confidence, not earnings_visibility
- 풍문또는보도에대한해명 → information_confidence_only
- 관리종목/거래정지 → risk_or_listing_event

LLM role:
- classify document/event contract type
- extract subject/counterparty/product/value/period
- mark uncertainty

Code role:
- enforce allowed primitive mapping
- block score eligibility if semantic guard fails

Hard fail:
- share_buyback_trust_to_contract_quality_count > 0
- pledge_contract_to_customer_contract_quality_count > 0
- equity_issuance_to_earnings_visibility_count > 0
- clarification_to_contract_quality_count > 0
- administrative_disclosure_to_revenue_visibility_count > 0
- contract_quality_semantic_guard_missing_count > 0

Tests:
tests/test_contract_semantic_classifier.py
tests/test_census_v4_share_buyback_not_contract_quality.py
tests/test_census_v4_pledge_not_customer_contract.py
tests/test_census_v4_equity_issuance_not_earnings_visibility.py
tests/test_census_v4_rumor_clarification_information_only.py

================================================================================
7. SourceTask Satisfaction Audit
================================================================================

Clarify whether a source task directly satisfied its primitive or only reused baseline claims.

SourceTaskExecution satisfaction fields:
- satisfies_source_task: true/false
- satisfaction_type:
  - DIRECT_ACCEPTED_CLAIM
  - BASELINE_ACCEPTED_CLAIM_REUSE
  - LIFECYCLE_REFRESH_ONLY
  - REPORT_REPLAY_REFERENCE_ONLY
  - NO_EVIDENCE_FOUND
  - PROVIDER_FAILED
  - PENDING_SOURCE
- accepted_claim_ids
- score_claim_ids
- primitive_gap_satisfied_ids
- primitive_gap_unsatisfied_ids

Rules:
- EVIDENCE_OS_ACCEPTED means source task directly produced accepted claim.
- EVIDENCE_OS_BASELINE_ONLY means baseline claim exists but task did not directly satisfy primitive.
- baseline-only claim may support event status but cannot be reported as direct source task success.
- If `satisfies_source_task=false`, it cannot unlock full thesis stage.
- Stage promotion must report whether evidence was direct, baseline reuse, or pending.

Audit counts:
- baseline_only_score_claim_count
- baseline_only_stage_promotion_count
- source_task_claim_satisfaction_mismatch_count
- direct_task_without_accepted_claim_count
- accepted_claim_without_satisfaction_path_count

Hard fail:
- source_task_claim_satisfaction_mismatch_count > 0
- direct_task_without_accepted_claim_count > 0
- baseline_only_stage_promotion_to_full_thesis_count > 0

Tests:
tests/test_census_v4_source_task_satisfaction.py
tests/test_census_v4_baseline_only_not_direct_task_success.py

================================================================================
8. Official Event Counters
================================================================================

Currently DART accepted claims can exist while recent_official_event_count remains 0.

Fix counters:
- recent_candidate_event_count
- accepted_official_claim_count
- official_source_task_count
- official_evidence_document_count
- official_stage_decision_count

Count official evidence if:
- candidate_event.source_family in DART/KIND/KRX/OpenDART
- accepted_claim.source_provider in OpenDART/KIND/KRX
- source_task_execution.provider in OpenDART/KIND/KRX
- evidence_document.canonical_url or official_document_id from official provider

Hard fail:
- accepted_official_claim_count > 0 and official event/source counters all zero
- official_claim_but_recent_official_event_zero_count > 0 unless no recent window applies and latest_official_claim_count is nonzero
- official source task exists but official_source_task_count zero

Tests:
tests/test_census_v4_official_event_counters.py

================================================================================
9. Samsung/Hynix Full Thesis Refresh Separation
================================================================================

Create separate task types:
- daily_event_task
- full_thesis_refresh_task

For 삼성전자 005930 / SK하이닉스 000660:
- daily_event_task captures recent DART events.
- full_thesis_refresh_task evaluates C06/HBM thesis.

C06/HBM full thesis must check:
- HBM customer allocation
- capacity sold-out / pre-sold status
- qualification pass or lag
- HBM shipment
- HBM revenue mix
- margin/FCF/revision bridge
- conventional memory drag
- customer concentration / Nvidia dependency
- current as_of_date lifecycle

Output fields:
- daily_event_stage_signal
- daily_event_evidence_score
- full_thesis_primary_archetype
- full_thesis_verified_score
- full_thesis_score_scale
- full_thesis_stage
- full_thesis_score_valid_status
- full_thesis_missing_primitives
- full_thesis_source_tasks
- full_thesis_accepted_claim_ids

Rules:
- daily DART event score cannot overwrite full thesis score.
- full thesis missing source → full_thesis_status=PENDING_MATERIAL_GAPS or PROVIDER_PENDING.
- Samsung/Hynix smoke must report both daily event and full thesis separately.
- If full thesis is not run, report `FULL_THESIS_NOT_RUN`, not Stage1/4.0.
- C06/HBM full thesis must not be inferred from a generic DART clarification or issuance filing.

Required smoke:
- 005930 Samsung Electronics
- 000660 SK Hynix
- at least one C06 positive fixture from research memory with URL-backed evidence
- at least one C06 guard fixture, e.g. Samsung qualification lag

Tests:
tests/test_census_v4_samsung_hynix_daily_vs_full_thesis.py
tests/test_census_v4_c06_full_thesis_refresh.py
tests/test_census_v4_hbm_thesis_not_dart_event_score.py

================================================================================
10. Real Brain + Web/Naver/IR/Report Acquisition Gate
================================================================================

This section proves whether the “brain” actually ran.

Run modes:
- OFFICIAL_BASELINE_ONLY
- BRAIN_TRIAGE_ENABLED
- BRAIN_AND_WEB_ACQUISITION_ENABLED
- FULL_LIVE_BRAIN_CENSUS
- LEDGER_REFRESH_CENSUS
- REPLAY_VALIDATION_CENSUS
- HYBRID_CENSUS

Rules:
- If llm_planner_call_count=0, do not say “두뇌가 판단했다.”
- If naver_search_call_count=0 and web_search_call_count=0 and trusted_news_search_call_count=0, do not say “네이버/웹을 썼다.”
- If llm_claim_extractor_attempt_count=0, do not say “LLM이 원문 claim을 추출했다.”
- If run mode is OFFICIAL_BASELINE_ONLY or LEDGER_REFRESH_CENSUS, final label cannot be BRAIN_WEB_EVIDENCE_PASS.
- Naver/web search is not run for all tickers. It runs only for L3/L4 selected deep symbols with bounded SourceTasks.
- official-first rule: DART/KIND/KRX/CompanyGuide/IR-solvable gaps must not go to Naver first.
- Web snippets/headlines cannot score.
- Full article/PDF/IR document must be fetched and Evidence OS must validate quote/date/subject/target/current status.

Required artifacts:
output/census_v4/YYYY-MM-DD/planner_runs.jsonl
output/census_v4/YYYY-MM-DD/llm_prompts.jsonl
output/census_v4/YYYY-MM-DD/llm_responses.jsonl
output/census_v4/YYYY-MM-DD/web_search_tasks.jsonl
output/census_v4/YYYY-MM-DD/web_search_results.jsonl
output/census_v4/YYYY-MM-DD/web_fetched_documents.jsonl
output/census_v4/YYYY-MM-DD/web_rejected_documents.jsonl
output/census_v4/YYYY-MM-DD/claim_extractor_runs.jsonl
output/census_v4/YYYY-MM-DD/brain_to_claim_trace.jsonl

Minimum Brain/Web acceptance:
- selected_deep_symbol_count >= 30 OR EXTERNAL_PROVIDER_BLOCKER_NOT_READY
- llm_planner_call_count >= 30 OR EXTERNAL_PROVIDER_BLOCKER_NOT_READY
- web_search_task_count >= 20 OR explicitly OFFICIAL_BASELINE_ONLY with honest label
- naver_search_call_count + trusted_news_search_call_count + general_web_search_call_count >= 20 OR documented external blocker
- web_fetched_document_count >= 10 OR documented source/provider gap
- llm_claim_extractor_attempt_count >= 10 for unstructured docs OR structured-official-only label
- web_or_llm_accepted_claim_count >= 3 OR all fetched docs rejected with reasons and label below BRAIN_WEB_EVIDENCE_PASS
- official_first_violation_count = 0
- snippet_to_score_count = 0
- provider_failure_final_score_count = 0

Critical counts:
- llm_claimed_but_zero_calls_count = 0
- web_claimed_but_zero_search_count = 0
- naver_claimed_but_zero_naver_count = 0
- brain_plan_without_prompt_hash_count = 0
- planner_output_score_stage_key_count = 0
- web_result_snippet_to_score_count = 0
- unstructured_rule_fallback_score_count = 0
- brain_claim_missing_stage_trace_count = 0
- official_first_violation_count = 0

Tests:
tests/test_census_v4_brain_planner_real_calls.py
tests/test_census_v4_web_naver_acquisition.py
tests/test_census_v4_llm_claim_extractor_realness.py
tests/test_census_v4_brain_to_claim_trace.py
tests/test_census_v4_run_mode_honesty.py
tests/test_census_v4_no_brain_claim_with_zero_llm_calls.py
tests/test_census_v4_no_web_claim_with_zero_web_calls.py
tests/test_census_v4_official_first_before_naver.py
tests/test_census_v4_snippet_never_scores.py

================================================================================
11. Meaningful Operational Stage Acceptance
================================================================================

Add a new acceptance tier:

ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS requires:
- full universe row coverage
- no fake score
- no source_proxy score
- no provider failure final score
- Stage0/NoCurrentCatalyst safe
- atomic trace audit may pass for event rows
- does not require full thesis scores

MEANINGFUL_OPERATIONAL_STAGE_PASS requires:
- all Stage2/3/Red/4 rows have AtomicStageDecision match
- score fields split and score_scale valid
- PENDING_MATERIAL_GAPS not COMPLETE
- source task satisfaction audit pass
- semantic primitive guard pass
- full thesis controlled smoke pass
- run mode honestly labeled
- Brain/Web gate pass if claiming brain/web
- controlled replay includes expected Stage2/3-Yellow/3-Green/3-Red/4B/4C or source gap task
- readiness verdict uses full test summary, self-repair, leaf audit, reviewer outputs as hard inputs

Controlled replay required:
- C06 HBM positive and qualification-lag guard
- C08 test socket customer/order/profile-only guard
- C15 material spread pass-through and raw commodity false positive
- C17 chemical spread realized margin bridge guard
- C24 clinical binary event guard
- C28 software/security retention bridge guard
- wrong-subject risk fixture
- old-risk-resolved fixture
- provider failure pending fixture
- semantic contract guard fixture

Tests:
tests/test_census_v4_meaningful_operational_stage_acceptance.py
tests/test_census_v4_controlled_replay_stage_semantics.py

================================================================================
12. Leaf Artifact and Reviewer Audits
================================================================================

Strengthen leaf audit.

Add counts:
- stage_trace_stage_mismatch_count
- stage_trace_score_interval_mismatch_count
- stage_trace_score_status_mismatch_count
- stage_trace_claim_set_mismatch_count
- stage_trace_contribution_set_mismatch_count
- score_scale_missing_count
- score_source_missing_count
- verified_score_not_full_e2r_count
- pending_material_marked_complete_count
- stage2_pending_material_count
- baseline_only_score_claim_count
- baseline_only_stage_promotion_count
- contract_quality_semantic_guard_missing_count
- official_claim_but_recent_official_event_zero_count
- readiness_missing_test_gate_count
- readiness_missing_self_repair_gate_count
- llm_claimed_but_zero_calls_count
- web_claimed_but_zero_search_count

Hard fail:
- any trace mismatch > 0
- score_scale_missing_count > 0
- verified_score_not_full_e2r_count > 0
- pending_material_marked_complete_count > 0
- contract_quality_semantic_guard_missing_count > 0
- semantic guard failures > 0
- run mode honesty violations > 0

Reviewer A/B/C/D/E:
- A trace atomicity
- B source realness
- C stage semantics
- D runtime/brain/web honesty
- E semantic primitive guard

Each reviewer reads only leaf artifacts and configs, not acceptance report.

Tests:
tests/test_census_v4_leaf_audit_atomic_counts.py
tests/test_census_v4_reviewer_semantic_guard.py
tests/test_census_v4_reviewer_run_mode_honesty.py

================================================================================
13. Known-Bad Regression Bundle
================================================================================

Create known-bad fixtures that must fail.

fixtures/census_v4_known_bad/
  stage_trace_mismatch_sambo/
  score_interval_mismatch_hynix/
  verified_score_event_partial/
  stage2_pending_marked_complete/
  buyback_trust_as_contract_quality/
  pledge_contract_as_customer_contract/
  equity_issuance_as_earnings_visibility/
  dart_event_score_as_hbm_full_thesis/
  llm_claimed_but_zero_calls/
  web_claimed_but_zero_calls/
  snippet_to_score/
  provider_failed_final_red/
  source_proxy_to_score/
  old_active_contract_dropped_by_recent_cutoff/
  report_label_overclaim/

Acceptance:
- every known-bad fixture fails with expected critical count.
- if known-bad fixture passes, Goal fails.
- no xfail/skip for known-bad tests.

Tests:
tests/test_census_v4_known_bad_regressions.py

================================================================================
14. Self-Repair Loop
================================================================================

The Goal is not complete until self-repair loop passes.

Run:
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --mode HYBRID_CENSUS \
  --brain-web-mode enabled \
  --max-iterations 10 \
  --fail-on-run-mode-overclaim true \
  --fail-on-atomic-mismatch true \
  --fail-on-semantic-guard true \
  --output-root output/census_v4/2026-07-01

Self-repair must:
- run census
- run leaf audits
- run reviewers
- run known-bad regression
- classify failures
- patch code/config
- rerun same command
- rerun tests
- compare before/after metrics
- stop only when hard gates pass or external blocker is documented

Failure classes:
- ATOMIC_STAGE_TRACE_MISMATCH
- VERIFIED_SCORE_SCALE_MISUSE
- STAGE2_WATCH_SEMANTIC_AMBIGUITY
- PENDING_MATERIAL_MARKED_COMPLETE
- CONTRACT_SEMANTIC_GUARD_FAILURE
- DAILY_EVENT_FULL_THESIS_MIXED
- BRAIN_CLAIMED_BUT_ZERO_LLM_CALLS
- WEB_CLAIMED_BUT_ZERO_SEARCH_CALLS
- SNIPPET_TO_SCORE
- SOURCE_TASK_SATISFACTION_MISMATCH
- OFFICIAL_COUNTER_MISMATCH
- REPORT_LABEL_OVERCLAIM
- KNOWN_BAD_REGRESSION_PASSED
- EXTERNAL_PROVIDER_BLOCKER

Rules:
- Do not loosen thresholds to pass.
- Do not delete failing fixtures.
- Do not change scoring weights/stage thresholds.
- Do not fake LLM/web counts.
- Do not mark external provider blocker as success.
- If external blocker exists, final status must be EXTERNAL_PROVIDER_BLOCKER_NOT_READY or lower honest label.

Tests:
tests/test_census_v4_self_repair_loop.py
tests/test_census_v4_no_threshold_loosening.py
tests/test_census_v4_no_fake_llm_web_counts.py

================================================================================
15. Required Reports
================================================================================

Generate and commit:

docs/0701/README.md
docs/0701/census_v3_stage_map_audit_2026-07-01.md

docs/operational/census_mode_v3_forensic_review.md
docs/operational/census_mode_v4_internal_patch_plan.md
docs/operational/census_mode_v4_acceptance_report.md
docs/operational/census_mode_v4_readiness_verdict.md
docs/operational/census_mode_v4_artifact_manifest.json
docs/operational/census_mode_v4_atomic_stage_decision_audit.json
docs/operational/census_mode_v4_score_scale_audit.json
docs/operational/census_mode_v4_stage_signal_audit.json
docs/operational/census_mode_v4_semantic_primitive_guard_audit.json
docs/operational/census_mode_v4_source_task_satisfaction_audit.json
docs/operational/census_mode_v4_official_event_counter_audit.json
docs/operational/census_mode_v4_samsung_hynix_full_thesis_smoke.json
docs/operational/census_mode_v4_brain_planner_audit.json
docs/operational/census_mode_v4_web_naver_acquisition_audit.json
docs/operational/census_mode_v4_llm_claim_extraction_audit.json
docs/operational/census_mode_v4_brain_to_claim_trace_audit.json
docs/operational/census_mode_v4_leaf_artifact_audit.json
docs/operational/census_mode_v4_reviewer_A_trace_atomicity.json
docs/operational/census_mode_v4_reviewer_B_source_realness.json
docs/operational/census_mode_v4_reviewer_C_stage_semantics.json
docs/operational/census_mode_v4_reviewer_D_runtime_brain_web_honesty.json
docs/operational/census_mode_v4_reviewer_E_semantic_guard.json
docs/operational/census_mode_v4_known_bad_regression_report.json
docs/operational/census_mode_v4_self_repair_summary.md

Output:
output/census_v4/2026-07-01/
  run_metadata.json
  universe.jsonl
  source_timelines.jsonl
  last_effective_thesis_states.jsonl
  baseline_scan_results.jsonl
  census_events.jsonl
  depth_decisions.jsonl
  atomic_stage_decisions.jsonl
  source_tasks.jsonl
  source_task_executions.jsonl
  evidence_documents.jsonl
  evidence_anchors.jsonl
  raw_assertions.jsonl
  adjudicated_claims.jsonl
  accepted_claims.jsonl
  primitive_states.jsonl
  score_contributions.jsonl
  stagecourt_traces.jsonl
  claim_to_stage_trace.jsonl
  brain_to_claim_trace.jsonl
  planner_runs.jsonl
  web_search_tasks.jsonl
  web_search_results.jsonl
  claim_extractor_runs.jsonl
  census_stage_status.jsonl
  census_stage_map.jsonl
  census_stage_map.csv
  operator_digest.md
  watchlist_seed_candidates.json
  deep_backfill_plan.json
  audit_summary.json

If full output is too large:
- commit manifest with row counts, sha256, byte sizes.
- commit full scored-row sample bundle, all Stage2+/Red/risk rows, all Samsung/Hynix rows, all mismatch-regression rows, all web/LLM accepted claim rows.

================================================================================
16. Required Tests
================================================================================

Add/strengthen:

tests/test_census_v4_atomic_stage_decision.py
tests/test_census_v4_sambo_trace_mismatch_fails.py
tests/test_census_v4_score_field_split.py
tests/test_census_v4_verified_score_only_full_e2r.py
tests/test_census_v4_stage_signal_split.py
tests/test_census_v4_pending_material_not_complete.py
tests/test_contract_semantic_classifier.py
tests/test_census_v4_share_buyback_not_contract_quality.py
tests/test_census_v4_pledge_not_customer_contract.py
tests/test_census_v4_equity_issuance_not_earnings_visibility.py
tests/test_census_v4_source_task_satisfaction.py
tests/test_census_v4_official_event_counters.py
tests/test_census_v4_samsung_hynix_daily_vs_full_thesis.py
tests/test_census_v4_c06_full_thesis_refresh.py
tests/test_census_v4_brain_planner_real_calls.py
tests/test_census_v4_web_naver_acquisition.py
tests/test_census_v4_llm_claim_extractor_realness.py
tests/test_census_v4_brain_to_claim_trace.py
tests/test_census_v4_run_mode_honesty.py
tests/test_census_v4_meaningful_operational_stage_acceptance.py
tests/test_census_v4_known_bad_regressions.py
tests/test_census_v4_self_repair_loop.py

Full command:
PYTHONPATH=src python -m unittest discover -s tests -v

Rules:
- No skipped Census v4 tests.
- No xfail.
- Known-bad fixtures must fail as expected.
- Tests must not only read acceptance report; they must inspect leaf artifacts/configs.

================================================================================
17. Hard Acceptance Gates
================================================================================

ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS:
- eligible symbols all represented exactly once
- no claimless nonzero score
- no source_proxy_to_score
- no provider_failed_final_score
- no market/news snippet score
- no one-line huge report
- leaf audit pass
- reviewer pass

ATOMIC_STAGE_DECISION_PASS:
- stage_trace_stage_mismatch_count = 0
- stage_trace_score_interval_mismatch_count = 0
- stage_trace_score_status_mismatch_count = 0
- stage_trace_claim_set_mismatch_count = 0
- stage_trace_contribution_set_mismatch_count = 0
- Sambo mismatch fixture fails before patch and passes after patch

SCORE_SCALE_PASS:
- score_scale_missing_count = 0
- verified_score_not_full_e2r_count = 0
- raw_contribution_fallback_as_verified_score_count = 0
- event_evidence_score used for partial event scores

STAGE_SEMANTICS_PASS:
- stage_signal present for all non-Stage0 rows
- pending_material_marked_complete_count = 0
- red_without_risk_signal_or_trace_count = 0
- ProviderPending not Red

SEMANTIC_PRIMITIVE_GUARD_PASS:
- semantic contract guard failures = 0
- buyback/pledge/equity issuance/clarification do not map to earnings_visibility contract_quality

FULL_THESIS_SMOKE_PASS:
- Samsung/Hynix daily event and C06/HBM full thesis outputs separated
- full thesis task run or explicitly pending
- DART event score not used as HBM full thesis score

BRAIN_WEB_GATE_PASS:
- if claiming brain/web, llm planner calls and web/news acquisition traces exist
- snippets do not score
- official-first violations = 0
- if no LLM/web, honest lower label is used

MEANINGFUL_OPERATIONAL_STAGE_PASS:
- all above pass
- controlled replay pass
- no unresolved material semantic/trace/source blockers
- readiness verdict uses tests/self-repair/auditors as hard inputs

================================================================================
18. Final Status Labels
================================================================================

Allowed labels:
- IMPLEMENTATION_MERGED
- V3_FORENSIC_REVIEW_COMPLETE
- ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
- ATOMIC_STAGE_DECISION_PASS
- SCORE_SCALE_PASS
- STAGE_SEMANTICS_PASS
- SEMANTIC_PRIMITIVE_GUARD_PASS
- FULL_THESIS_SMOKE_PASS
- BRAIN_TRIAGE_PASS
- BRAIN_WEB_EVIDENCE_PASS
- MEANINGFUL_OPERATIONAL_STAGE_PASS
- READY_FOR_DAILY_TRIGGER_INTEGRATION
- READY_FOR_FULL_THESIS_OPERATION
- EXTERNAL_PROVIDER_BLOCKER_NOT_READY

Do not use:
- ambiguous FULL_UNIVERSE_STAGE_MAP_PASS alone

Goal completion minimum:
- V3_FORENSIC_REVIEW_COMPLETE
- ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
- ATOMIC_STAGE_DECISION_PASS
- SCORE_SCALE_PASS
- STAGE_SEMANTICS_PASS
- SEMANTIC_PRIMITIVE_GUARD_PASS
- FULL_THESIS_SMOKE_PASS
- self-repair loop pass
- known-bad regression pass
- full tests pass

Operational completion:
- MEANINGFUL_OPERATIONAL_STAGE_PASS
- plus BRAIN_WEB_EVIDENCE_PASS if claiming brain/web source acquisition
- plus READY_FOR_DAILY_TRIGGER_INTEGRATION only if output labels are honest.

================================================================================
19. Final Answer Format
================================================================================

After completion, report only:

1. Final status
2. Commit SHA / message / push status / working tree
3. Tests
4. v3 forensic review result
5. AtomicStageDecision audit
6. Score scale audit
7. Stage semantics audit
8. Semantic primitive guard audit
9. SourceTask satisfaction audit
10. Samsung/Hynix full thesis smoke
11. Brain/Web/Naver/IR/Report gate
12. Leaf artifact / reviewer verdicts
13. Known-bad regression result
14. Self-repair iterations
15. Remaining blockers
16. Exact next step

================================================================================
20. Prohibitions
================================================================================

- Do not claim Meaningful Operational Stage if only anti-fake board passed.
- Do not use ambiguous FULL_UNIVERSE_STAGE_MAP_PASS alone.
- Do not call event_evidence_score “verified_score.”
- Do not compare EVENT_WEIGHTED_PARTIAL with FULL_E2R_100.
- Do not mix stage/score/status/trace from different StageCourt rows.
- Do not keep Sambo-style mismatch.
- Do not mark PENDING_MATERIAL_GAPS as COMPLETE.
- Do not map share buyback trust/pledge/equity issuance/clarification to earnings_visibility contract_quality.
- Do not say Samsung/Hynix HBM thesis was evaluated from DART event score.
- Do not say Brain/Web/Naver ran if llm/web call artifacts are absent.
- Do not score snippets.
- Do not score source_proxy/evidence_url_pending research memory.
- Do not fake LLM/web counts.
- Do not loosen thresholds to pass.
- Do not delete known-bad fixtures.
- Do not change scoring weights or Stage thresholds.
- Do not hide source gaps.
- Do not output one-line huge reports.

================================================================================
21. One-line goal
================================================================================

Census v4의 목적은 전 종목 상태판을 더 그럴듯하게 꾸미는 것이 아니다.

목적은:

“이 row는 단일 공식 이벤트 watch인지, full thesis Stage인지, risk overlay인지, source pending인지”를 명확히 분리하고,
점수와 Stage가 같은 AtomicStageDecision에서 나왔음을 증명하며,
필요한 후보에는 Research Brain + official/web/IR/report SourceTask + Evidence OS claim까지 실제로 연결해,
운영자가 오해하지 않는 전 시장 E2R 상태판을 만드는 것이다.