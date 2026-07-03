왜냐면 baaf2e7은 실제 구현 커밋이 아니라 acceptance report의 push 상태 한 줄을 바꾼 report-only 커밋이야. GitHub commit 페이지에도 Census v3 acceptance report 푸시 상태 갱신, 1 file changed, 대상 파일이 docs/operational/census_mode_v3_acceptance_report.md 하나라고 나온다. 그리고 구현 커밋은 그 전의 c5bc76a Census v3 전체지도 leaf audit 구현이라고 명시돼 있어.

c5bc76a 자체는 꽤 큰 패치야. census_runner_v3.py, leaf_artifact_auditor.py, production_cutover_leaf_loader.py, reviewers.py, run_e2r_census_v3_until_pass.py, 여러 source_family_collectors, 그리고 Census v3 테스트 파일들이 대량 추가됐어. 즉 “아무것도 안 함”은 아니고, 네가 시킨 방향의 구조는 많이 들어갔다.

그런데 문제는 검증 산출물이 아직 너무 report 중심이라는 거야. census_mode_v3_acceptance_report.md는 FULL_UNIVERSE_STAGE_MAP_PASS, 3391 symbols, accepted claims 92, score contributions 92, StageCourt traces 92, claim-to-stage trace 3391이라고 말한다. 하지만 이건 report 텍스트야. 실제 output/census_v3/2026-07-01/... leaf artifact들이 레포에 같이 올라와 있지 않으면, 내가 외부에서 claim_to_stage_trace.jsonl, accepted_claims.jsonl, score_contributions.jsonl, stagecourt_traces.jsonl, census_stage_status.jsonl을 독립 재계산할 수 없어. 실제로 해당 output 경로는 GitHub에서 404로 확인돼.

그리고 치명적인 혼선이 하나 더 있어. main의 기존 src/e2r/census/census_runner.py에는 여전히 구형 Census runner가 남아 있고, 그 경로는 build_stage_status(... accepted_claims=(), score_contributions=())를 넘긴다. v3 runner가 별도 파일로 생긴 건 맞지만, 기본 CLI/운영 진입점이 v3만 쓰는지, 구형 runner가 실수로 사용될 여지가 없는지 더 막아야 해. 구형 runner가 남아 있는 한, 나중에 누가 run_e2r_census_mode를 실행하면 다시 빈 claim/score 상태판을 만들 수 있다.

또 v3 acceptance report의 runtime이 3.67초라고 되어 있다. 3391개 전 종목에 대해 진짜 DART/KIND/KRX/CompanyGuide/IR/뉴스/기존 claim lifecycle, selective deep, Evidence OS, StageCourt까지 강하게 돈 결과라면 3.67초는 너무 짧아. 이 숫자는 실제 live source fetch라기보다 기존 cutover leaf/report를 읽어 Census map으로 재조립한 경량 실행일 가능성이 크다. report는 Stage 분포를 보여주지만, 그걸 만든 leaf artifact 전체가 공개/재현 가능하지 않으면 pass를 확정하면 안 된다.

원래 목표는 report가 아니라, 문서 원문에서 claim 장부를 만들고, 그 claim의 주체·날짜·현재성·대상회사 직접 귀속을 검증한 뒤 deterministic score/stage에 넣는 구조였어. 그 원칙에 따르면 “accepted claim 92개”라는 합계가 중요한 게 아니라, 각 Stage row가 어떤 claim_id, score_contribution_id, stagecourt_trace_id를 물고 있는지가 증명돼야 한다.

또 과거 연구 원료도 조심해야 해. C06/C08처럼 URL-backed row가 있는 자료는 replay 원료로 쓸 수 있지만, C24/C28/C17 일부는 source_proxy_only, evidence_url_pending, shadow_weight_only라서 production score 근거로 쓰면 안 된다. C24 연구는 source-proxy/pending을 명시하고 production scoring 변경이 아니라고 했고, C28/C17 연구도 URL repair 전 promotion 금지 성격이 강하다.

아래 프롬프트는 이제 못 속이게 만드는 Census v4 Goal이야. 이번에는 “성공했다는 report”가 아니라 실제 leaf bundle + 재실행 + 구형 runner 차단 + random row audit + live/snapshot 구분까지 요구해야 해.

너는 Daikisong/stock_agent 레포의 E2R Census Mode v4 / Runtime-Proven Full Universe Stage Map을 구현하는 coding agent다.

현재 전제:
- Production Cutover v3는 CUTOVER_READY였다.
- Census v1은 전 종목 row만 만들었고 Unknown/ProviderPending 100%였다.
- Census v2는 report synthesis/replay 성격이 강했고 claim-to-stage 연결이 불충분했다.
- Census v3는 c5bc76a에서 leaf audit, reviewer, self-repair 구조를 구현했고 baaf2e7에서 acceptance report push 상태를 갱신했다.
- 그러나 baaf2e7은 report-only commit이다.
- 현재 v3 acceptance report는 FULL_UNIVERSE_STAGE_MAP_PASS를 주장하지만, output/census_v3/2026-07-01 leaf artifacts 전체가 repo에서 독립 검증 가능하지 않다.
- main의 기존 src/e2r/census/census_runner.py에는 여전히 accepted_claims=(), score_contributions=()를 넘기는 구형 runner 경로가 남아 있다.
- 따라서 v3를 운영 통합 기준으로 받기 전에, 실제 runtime proof와 committed/hashed leaf artifact bundle이 필요하다.

이번 Goal 이름:
E2R Census Mode v4 — Runtime Proof, Committed Leaf Bundle, Legacy Runner Lockout, Claim-to-Stage Forensic Audit

최종 목표:
FULL_UNIVERSE_STAGE_MAP_PASS를 “report 문구”가 아니라 “재현 가능한 실행 + leaf artifact + 독립 audit + trace forensic”으로 증명한다.

즉:

실제 Census v4 command
→ output/census_v4/YYYY-MM-DD leaf artifacts 생성
→ 모든 eligible symbol의 source timeline / last effective thesis / baseline / depth / stage row 생성
→ selected deep rows는 source task → evidence document → accepted claim → score contribution → StageCourt trace까지 연결
→ leaf artifact auditor가 report를 읽지 않고 재계산
→ random row forensic auditor가 실제 row 내부 연결을 샘플링 검증
→ legacy runner/old CLI로는 FULL_UNIVERSE_STAGE_MAP_PASS를 낼 수 없게 차단
→ committed manifest와 artifact hashes로 외부 검증 가능
→ FULL_UNIVERSE_STAGE_MAP_PASS

까지 닫혀야 한다.

절대 원칙:
1. report 숫자는 source of truth가 아니다.
2. source of truth는 leaf artifacts다.
3. leaf artifacts가 repo에 없거나 artifact manifest/hash로 재현 불가하면 pass 금지.
4. accepted_claim_count 합계만으로 pass 금지.
5. 각 scored Stage row가 accepted_claim_ids, score_contribution_ids, stagecourt_trace_id를 가져야 한다.
6. 기존 report/cutover/candidate_event를 replay한 source task는 “reference/replay”로만 세고 real source execution으로 세지 않는다.
7. source task execution의 accepted_claim_ids가 비어 있으면 claim-producing task가 아니다.
8. main의 legacy census_runner.py 경로가 production/pass CLI로 남아 있으면 실패다.
9. `run_e2r_census_mode`가 구형 v1 runner를 호출하면 실패다.
10. `run_e2r_census_v3_until_pass` 또는 v4 CLI가 실제 운영 진입점이어야 한다.
11. source_proxy_only/evidence_url_pending/price_path_only memory는 score evidence가 아니다.
12. 최근 공시 window는 Stage cutoff가 아니다. 마지막 유효 thesis/lifecycle이 기준이다.
13. 실패하면 원인 분석 → 코드 패치 → 같은 명령 재실행 → leaf audit 재검증까지 반복한다.
14. 외부 API 장애만 EXTERNAL_BLOCKER_NOT_READY로 남길 수 있다. 코드 wiring/report overclaim은 반드시 고친다.
15. scoring weight와 Stage threshold는 변경하지 않는다.
16. 특정 종목명/URL/키워드 예외 처리 금지.

================================================================================
0. v3 상태 재분류
================================================================================

먼저 v3를 정확히 재분류하라.

생성/수정:
docs/operational/census_mode_v3_forensic_review.md

내용:
- baaf2e7은 report-only commit이며 implementation commit은 c5bc76a임을 명시한다.
- c5bc76a는 Census v3 runner/auditor/reviewer/test를 추가했지만, FULL_UNIVERSE_STAGE_MAP_PASS는 leaf artifact가 외부 검증 가능할 때만 인정된다고 명시한다.
- output/census_v3/2026-07-01 leaf artifacts가 repo에 없거나 artifact manifest로 재현 불가하면 v3 pass는 provisional이다.
- 기존 src/e2r/census/census_runner.py의 v1 path가 accepted_claims=(), score_contributions=()를 넘기는 구형 경로임을 명시한다.
- v4의 목표는 “report pass”가 아니라 “runtime-proven pass”다.

Acceptance:
- v3 report는 삭제하지 않고 PROVISIONAL_REPORT_PASS로 재라벨링.
- v4 pass 전까지 v3만으로 READY_FOR_DAILY_TRIGGER_INTEGRATION 확정 금지.
- forensic review 문서에 root-cause file/function 목록 포함.

================================================================================
1. Legacy Census Runner Lockout
================================================================================

현재 main에는 v1/v3 경로가 혼재되어 있다.
구형 runner가 실수로 pass를 만들 수 없게 막아라.

Required:
- src/e2r/census/census_runner.py를 legacy로 명확히 재라벨링하거나 v4 runner로 forward한다.
- accepted_claims=(), score_contributions=()를 넘기는 경로가 production/census pass CLI에서 절대 실행되지 않게 한다.
- CLI `run_e2r_census_mode`가 구형 v1 runner를 호출하지 않도록 하거나, 실행 시 deprecation error를 내게 한다.
- 새 공식 CLI는 `run_e2r_census_v4_until_pass.py`다.
- old v1 runner는 test fixture 전용으로만 남기고, production/pass label 생성 금지.

Static rule:
- production census path에서 `accepted_claims=()` 문자열 감지 시 critical fail.
- production census path에서 `score_contributions=()` 문자열 감지 시 critical fail.
- `run_e2r_census_mode`가 legacy runner를 부르면 critical fail.
- old runner가 FULL_UNIVERSE_STAGE_MAP_PASS label을 만들면 critical fail.

Tests:
tests/test_census_v4_legacy_runner_lockout.py
tests/test_census_v4_no_empty_claims_in_production_path.py
tests/test_census_v4_cli_uses_v4_runner.py

Acceptance:
- legacy_runner_production_reachable_count = 0.
- empty_claims_stage_builder_production_count = 0.
- old_cli_can_claim_pass_count = 0.
- official CLI documented and tested.

================================================================================
2. Runtime-Proven Leaf Artifact Bundle
================================================================================

v4는 반드시 실제 output leaf artifacts를 생성하고, repo에 audit 가능한 manifest를 남긴다.

Required output:
output/census_v4/YYYY-MM-DD/
  run_metadata.json
  universe.jsonl
  census_assessment_events.jsonl
  source_timelines.jsonl
  last_effective_thesis_states.jsonl
  baseline_inputs_summary.json
  baseline_scan_results.jsonl
  census_events.jsonl
  depth_decisions.jsonl
  research_brain_plans.jsonl
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
  census_stage_status.jsonl
  census_stage_map.jsonl
  census_stage_map.csv
  census_stage_summary.json
  leaf_artifact_audit.json
  reviewer_A_trace_audit.json
  reviewer_B_source_audit.json
  reviewer_C_stage_audit.json
  operator_digest.md
  watchlist_seed_candidates.json
  deep_backfill_plan.json
  audit_summary.json

If output is too large for git:
- commit a manifest with sha256, byte_size, row_count, schema_version, and local path for every leaf.
- commit a deterministic reproduction command.
- commit at least a representative sampled bundle:
  - 50 Stage0/NoKnownThesis rows
  - all Stage2+ rows
  - all Red/RiskReview rows
  - all ProviderPending/SourcePending rows
  - all rows with accepted_claim_ids
  - all rows with score_contribution_ids
  - all rows in watchlist seed
- full local artifact manifest must match report.

Required docs:
docs/operational/census_mode_v4_artifact_manifest.json
docs/operational/census_mode_v4_sample_leaf_bundle.jsonl
docs/operational/census_mode_v4_reproduction_command.md

Acceptance:
- Every leaf artifact has row_count, sha256, byte_size.
- Report numbers equal manifest row_counts.
- sample bundle includes every scored row, not just random examples.
- If full leaf output is not committed, manifest must prove existence and reproducibility.
- Missing claim_to_stage_trace.jsonl is critical fail.
- Missing accepted_claims.jsonl while accepted_claim_count > 0 is critical fail.
- Missing score_contributions.jsonl while score_contribution_count > 0 is critical fail.

Tests:
tests/test_census_v4_artifact_manifest.py
tests/test_census_v4_manifest_counts_match_report.py
tests/test_census_v4_sample_bundle_contains_all_scored_rows.py

================================================================================
3. Report 생성 금지: Leaf Audit First
================================================================================

Acceptance report must be generated only after independent leaf audit.

Flow:
1. Run census.
2. Write leaf artifacts.
3. Close files.
4. Reopen leaf artifacts from disk.
5. Independent LeafArtifactAuditor recalculates all metrics.
6. Reviewer A/B/C read only leaf artifacts.
7. Acceptance report uses auditor output only.
8. If report in-memory counters differ from leaf audit, fail.

Ban:
- acceptance report generated from in-memory stage_summary.
- acceptance report generated before leaf artifact audit.
- same function generating report and auditor counters.
- report-only commit claiming new pass without rerun/manifest update.

Acceptance:
- report_generated_from_leaf_audit = true.
- in_memory_summary_used_for_acceptance_count = 0.
- leaf_report_metric_mismatch_count = 0.
- report_only_commit_without_rerun cannot change final status except wording fix.

Tests:
tests/test_census_v4_report_generated_from_leaf_audit.py
tests/test_census_v4_report_only_commit_cannot_change_status.py

================================================================================
4. Claim-to-Stage Forensic Audit
================================================================================

각 scored row에 대해 실제 연결을 증명한다.

For every row in census_stage_status.jsonl:

If verified_score is not null or score_valid_status indicates FINAL/FINAL_WITH_NONMATERIAL_GAPS:
- accepted_claim_ids non-empty
- score_contribution_ids non-empty
- stagecourt_trace_id non-null
- every accepted_claim_id exists in accepted_claims.jsonl
- every score_contribution_id exists in score_contributions.jsonl
- stagecourt_trace_id exists in stagecourt_traces.jsonl
- score contribution support_claim_ids subset of accepted_claim_ids or explicitly linked by claim_to_stage_trace
- no support claim is source_proxy_only/evidence_url_pending/price_path_only
- no support claim lacks source_url or official API locator
- no support claim lacks event/source date
- no support claim lacks target/temporal adjudication

If base_stage in Stage2-Watch/Stage2-Actionable/Stage3-Yellow/Stage3-Green/Red/Reject:
- must have either score trace or explicit non-scored guard/pending reason.
- Red/Reject requires current direct negative claim or explicit guard status.
- Provider failure cannot be Red/Reject.

If Stage0/NoKnownThesis:
- source_timeline_id and last_effective_thesis_id required.
- source families attempted or existing ledger checked.
- reason must not be “recent lookback expired”.
- if provider failures exist, status must be ProviderPending, not Stage0.

If ProviderPending/SourcePending:
- provider/source gap record required.
- no final score.

Reports:
docs/operational/census_mode_v4_claim_to_stage_forensic_audit.json

Acceptance:
- scored_row_missing_claim_ids = 0
- scored_row_missing_score_contribution_ids = 0
- scored_row_missing_stagecourt_trace = 0
- claim_id_not_found_count = 0
- score_contribution_id_not_found_count = 0
- stagecourt_trace_id_not_found_count = 0
- support_claim_not_accepted_count = 0
- source_proxy_support_claim_count = 0
- source_pending_marked_red_count = 0
- provider_failed_final_score_count = 0
- stage0_without_timeline_count = 0
- no_current_thesis_recent_cutoff_reason_count = 0

Tests:
tests/test_census_v4_claim_to_stage_forensic_audit.py
tests/test_census_v4_scored_rows_have_trace.py
tests/test_census_v4_stage0_requires_source_timeline.py
tests/test_census_v4_provider_pending_never_red.py

================================================================================
5. SourceTask Realness Audit
================================================================================

SourceTask 숫자가 “기존 report replay”를 의미하면 안 된다.

Classify each source task execution:
- REAL_PROVIDER_FETCH
- FRESH_PROVIDER_CACHE
- EXISTING_ACCEPTED_CLAIM_LIFECYCLE_REFRESH
- REPORT_REPLAY_REFERENCE_ONLY
- RESEARCH_MEMORY_REFERENCE_ONLY
- PROVIDER_FAILED
- NO_EVIDENCE_FOUND
- BUDGET_EXHAUSTED

Rules:
- REAL_PROVIDER_FETCH and FRESH_PROVIDER_CACHE may create new EvidenceDocument/Anchor.
- EXISTING_ACCEPTED_CLAIM_LIFECYCLE_REFRESH may reuse claim only with lifecycle refresh.
- REPORT_REPLAY_REFERENCE_ONLY cannot count as real source execution.
- RESEARCH_MEMORY_REFERENCE_ONLY cannot count as real source execution.
- source_task_execution status PARSED with accepted_claim_ids=[] cannot count as accepted evidence.
- source task count for acceptance must split planned/executed/claim-producing.
- “source task executed 92” is meaningless unless claim-producing count is separately shown.

Reports:
docs/operational/census_mode_v4_source_task_realness_audit.json

Acceptance:
- source_task_planned_count reported.
- source_task_real_fetch_count reported.
- source_task_lifecycle_refresh_count reported.
- source_task_report_replay_reference_count reported.
- source_task_claim_producing_count reported.
- claim_producing_source_task_count > 0.
- report_replay_count not included in real_fetch_count.
- source_task_accepted_with_empty_claim_ids_count = 0.
- PARSED_without_claim_count not counted as evidence.

Tests:
tests/test_census_v4_source_task_realness_audit.py
tests/test_census_v4_report_replay_not_real_execution.py
tests/test_census_v4_parsed_without_claim_not_claim_producing.py

================================================================================
6. Existing Ledger Reuse Audit
================================================================================

If Census v4 relies on production_cutover leaf claims, make that explicit and safe.

For every reused claim:
- original_run_id
- original_as_of_date
- source_document_id
- source_url or official API locator
- original_claim_id
- lifecycle_refresh_status
- as_of_date_current_status
- reused_in_symbol
- reused_in_stage_row
- freshness/lifecycle policy
- supersession check
- contradiction check

Rules:
- existing claim can be reused only after lifecycle refresh.
- previous Stage cannot be copied blindly.
- old positive claim must remain active.
- old risk claim must be current OPEN to score.
- reused claim must appear in claim_to_stage_trace if it affects stage/score.

Reports:
docs/operational/census_mode_v4_existing_ledger_reuse_audit.json

Acceptance:
- reused_claim_count reported.
- lifecycle_refreshed_reused_claim_count == reused_claim_count.
- stale_claim_reused_current_count = 0.
- previous_stage_blind_copy_count = 0.
- existing_claim_without_source_locator_count = 0.
- reused_claim_not_in_trace_count = 0.

Tests:
tests/test_census_v4_existing_ledger_reuse_audit.py
tests/test_census_v4_no_stale_claim_reuse.py
tests/test_census_v4_no_previous_stage_blind_copy.py

================================================================================
7. Last Effective Thesis Must Not Be Cosmetic
================================================================================

LastEffectiveThesisState cannot be a dummy row for every symbol.

For each symbol:
- status derived from SourceTimeline
- source family attempts present
- if NO_KNOWN_THESIS:
  - latest regular report or official/price/ledger check attempted
  - no candidate event / no accepted current claim / no active research memory claim
- if ACTIVE_THESIS:
  - support event or claim exists
  - lifecycle active
- if PROVIDER_PENDING:
  - provider failure exists
- if SOURCE_PENDING:
  - event exists but verification source missing
- if HISTORICAL_ONLY:
  - old event exists but expired/resolved/superseded

Reports:
docs/operational/census_mode_v4_last_effective_thesis_audit.json

Acceptance:
- last_effective_thesis_count == eligible_count.
- dummy_no_known_thesis_count = 0.
- no_known_thesis_without_any_source_attempt_count = 0.
- active_thesis_without_event_or_claim_count = 0.
- provider_pending_without_provider_failure_count = 0.
- historical_only_without_historical_event_count = 0.
- recent_lookback_used_as_stage_cutoff_count = 0.

Tests:
tests/test_census_v4_last_effective_thesis_not_dummy.py
tests/test_census_v4_no_known_thesis_requires_source_attempt.py
tests/test_census_v4_active_thesis_requires_support.py

================================================================================
8. Real Source Coverage, Not Just Cutover Replay
================================================================================

Census v4 may reuse cutover leaf artifacts, but must also demonstrate actual Census-time source coverage.

Minimum:
- OpenDART/KIND/KRX/CompanyGuide or provider cache attempts across full universe.
- price/volume anomaly detection attempted.
- report/news/IR sources either attempted or explicit nonblocking gap.
- existing ledger loaded.
- research memory hints loaded as planning-only.

Reports:
docs/operational/census_mode_v4_source_coverage_audit.json

Metrics:
- census_time_opendart_attempt_count
- census_time_kind_krx_attempt_count
- census_time_companyguide_attempt_count
- census_time_price_attempt_count
- census_time_existing_ledger_attempt_count
- census_time_report_news_ir_attempt_count
- provider_cache_used_count
- stale_cache_used_count
- cutover_replay_only_symbol_count
- symbol_without_any_census_time_source_attempt_count

Acceptance:
- symbol_without_any_census_time_source_attempt_count = 0.
- cutover_replay_only_symbol_count must be reported and cannot be all scored rows.
- if all accepted claims are reused from cutover, Census status must say “ledger refresh map”, not “new full source map”.
- at least one Census-time source family must run over the full universe.
- accepted claim rows must distinguish reused vs newly verified.

Tests:
tests/test_census_v4_source_coverage_audit.py
tests/test_census_v4_no_symbol_without_source_attempt.py
tests/test_census_v4_reused_vs_new_claim_distinction.py

================================================================================
9. Runtime Plausibility Audit
================================================================================

If a full universe run claims to use many live/LLM paths but finishes in a few seconds, that is suspicious.
Runtime is not pass/fail alone, but must match declared work.

Add:
RuntimePlausibilityAudit

Checks:
- runtime_seconds
- eligible_count
- provider_call_count
- LLM_call_count
- source_task_real_fetch_count
- evidence_extraction_count
- average_time_per_real_fetch
- average_time_per_llm_call
- zero_llm_but_llm_claimed_count
- runtime_too_short_for_declared_live_fetch_count
- runtime_too_short_for_declared_llm_extraction_count
- report_claims_live_but_only_replay_count

Rules:
- If LLM_call_count=0, report must not say LLM-driven Census.
- If source_task_real_fetch_count=0, report must not say real source execution.
- If runtime < threshold and claimed live fetch count high, require provider request log proof.
- Runtime proof uses provider request logs and prompt/response logs, not summary text.

Reports:
docs/operational/census_mode_v4_runtime_plausibility_audit.json

Acceptance:
- zero_llm_but_llm_claimed_count = 0.
- report_claims_live_but_only_replay_count = 0.
- runtime_too_short_for_declared_live_fetch_count = 0 or provider logs explain cache/fresh provider cache.
- runtime mode is clearly labeled:
  - FULL_LIVE
  - FRESH_PROVIDER_CACHE
  - LEDGER_REFRESH
  - REPLAY_VALIDATION
  - HYBRID

Tests:
tests/test_census_v4_runtime_plausibility_audit.py
tests/test_census_v4_no_llm_claim_when_llm_zero.py
tests/test_census_v4_no_live_claim_when_replay_only.py

================================================================================
10. Independent Anti-Cheat Reviewers v4
================================================================================

Reviewer A/B/C from v3 were too easy if they trusted v3 artifacts.
Strengthen them:

Reviewer A: Trace Forensics
- samples 100 Stage0 rows, all Stage2+ rows, all Red rows, all scored rows.
- verifies source_timeline_id / last_effective_thesis_id / claim IDs / score IDs / StageCourt trace IDs exist.
- checks row IDs in leaf artifacts, not report.

Reviewer B: Source Realness
- classifies every source task execution.
- checks provider request IDs, cache freshness, report replay markers.
- verifies source_proxy/evidence_url_pending cannot score.

Reviewer C: Stage Semantics
- checks Stage0 reasons, ProviderPending reasons, Red reasons, Stage2 reasons.
- checks last effective thesis lifecycle and recent cutoff misuse.
- checks accepted claims actually support stage semantics.

Reviewer D: Runtime Plausibility
- checks runtime/provider/LLM counts vs claimed mode.

All reviewers:
- read only leaf artifacts and manifests.
- do not import acceptance report.
- do not share counters with report generator.
- any critical fail blocks pass.
- 99/100 is fail if one critical item fails.

Reports:
docs/operational/census_mode_v4_reviewer_A_trace_forensics.json
docs/operational/census_mode_v4_reviewer_B_source_realness.json
docs/operational/census_mode_v4_reviewer_C_stage_semantics.json
docs/operational/census_mode_v4_reviewer_D_runtime_plausibility.json

Acceptance:
- Reviewer A/B/C/D verdict = PASS.
- critical_count = 0 for each.
- sampled row IDs included.
- all scored rows reviewed, not sampled.

Tests:
tests/test_census_v4_reviewer_trace_forensics.py
tests/test_census_v4_reviewer_source_realness.py
tests/test_census_v4_reviewer_stage_semantics.py
tests/test_census_v4_reviewer_runtime_plausibility.py

================================================================================
11. Self-Repair Until Runtime-Proven Pass
================================================================================

Keep the self-repair loop, but require actual patch/rerun when failures occur.

Failure classes:
- LEGACY_RUNNER_REACHABLE
- OUTPUT_LEAF_BUNDLE_MISSING
- CLAIM_TO_STAGE_DISCONNECTED
- SOURCE_TASK_REPLAY_COUNTED_AS_REAL
- REPORT_GENERATED_BEFORE_LEAF_AUDIT
- LAST_EFFECTIVE_THESIS_DUMMY
- SOURCE_COVERAGE_COSMETIC
- RUNTIME_IMPLAUSIBLE
- LLM_CLAIMED_BUT_ZERO_CALLS
- LIVE_CLAIMED_BUT_REPLAY_ONLY
- SOURCE_PROXY_SCORE
- PROVIDER_FAILURE_FINAL_SCORE
- RECENT_CUTOFF_MISUSE
- ACCEPTANCE_REPORT_OVERCLAIM
- EXTERNAL_PROVIDER_BLOCKER

Self-repair must:
- name exact file/function.
- patch code/config.
- rerun same command.
- rerun tests.
- rerun leaf audit.
- compare before/after metrics.

Acceptance:
- self_repair_log includes actual iterations.
- unresolved non-external failures = 0.
- no threshold loosening.
- no fake artifact generation.
- no report-only fix counted as repair.
- If pass happens on first run, run known-bad regression fixtures to prove failures are detected.

Tests:
tests/test_census_v4_self_repair_requires_rerun.py
tests/test_census_v4_no_report_only_repair.py
tests/test_census_v4_known_bad_regressions_fail.py

================================================================================
12. Known-Bad Regression Bundle
================================================================================

Create fixtures that must fail.

fixtures/census_v4_known_bad/
  accepted_claim_summary_only/
  source_task_replay_as_execution/
  all_unknown_fake_pass/
  all_provider_pending_fake_pass/
  all_stage0_without_source_proof/
  stage2_without_trace/
  score_without_claim/
  source_proxy_score/
  recent_cutoff_drops_active_contract/
  provider_failure_marked_red/
  report_leaf_mismatch/
  runtime_claims_llm_but_zero_calls/

For each:
- auditor must fail.
- reviewer must fail if relevant.
- acceptance report cannot pass.

Tests:
tests/test_census_v4_known_bad_bundle.py

Acceptance:
- every known-bad fixture produces expected critical failures.
- any known-bad fixture passing is critical failure.

================================================================================
13. Realistic Run Modes
================================================================================

Census v4 must label its run mode honestly.

Allowed run modes:
- FULL_LIVE_CENSUS
  real provider calls and/or fresh provider cache across universe.
- FRESH_PROVIDER_CACHE_CENSUS
  provider cache generated by current run, no stale replay.
- LEDGER_REFRESH_CENSUS
  primarily reuses existing accepted claims with lifecycle refresh.
- REPLAY_VALIDATION_CENSUS
  validates old outputs only; cannot claim FULL_UNIVERSE_STAGE_MAP_PASS for live operation.
- HYBRID_CENSUS
  mixture; must show proportions.

For each mode, report:
- provider call count
- provider cache count
- existing ledger reuse count
- new accepted claim count
- reused accepted claim count
- LLM call count
- Research Brain plan count
- real source task count
- replay reference task count

Acceptance:
- final label must match run mode.
- REPLAY_VALIDATION_CENSUS cannot claim READY_FOR_DAILY_TRIGGER_INTEGRATION.
- LEDGER_REFRESH_CENSUS can claim FULL_UNIVERSE_STAGE_MAP_PASS only if it clearly says stage map is based on existing ledger refresh, not new source discovery.
- FULL_LIVE_CENSUS requires provider logs.
- HYBRID_CENSUS requires source proportion table.

Tests:
tests/test_census_v4_run_mode_honesty.py
tests/test_census_v4_replay_mode_cannot_claim_live_ready.py

================================================================================
14. Final Hard Gates
================================================================================

FULL_UNIVERSE_STAGE_MAP_PASS requires all:

A. Universe
- eligible_count > 1000
- stage_status_count == eligible_count
- no missing/duplicate symbols

B. Baseline
- source_timeline_count == eligible_count
- last_effective_thesis_count == eligible_count
- baseline_scan_count == eligible_count
- symbol_without_any_source_attempt_count = 0

C. Trace
- claim_to_stage_trace_count == eligible_count
- all scored rows have accepted claim IDs, score contribution IDs, StageCourt trace
- all Stage2+ rows have trace or explicit pending/guard reason

D. Evidence
- accepted_claim_count > 0
- score_contribution_count > 0
- source_task_claim_producing_count > 0
- accepted_claims linked to stage rows or backlog with reason

E. Safety
- no claimless nonzero score
- no source_proxy/evidence_url_pending/price_path_only score
- no market anomaly/news snippet score
- no provider failure final score
- no stale claim reuse
- no recent cutoff misuse

F. Source realness
- source task realness audit pass
- report replay not counted as real
- source coverage audit pass

G. Review
- leaf audit pass
- reviewers A/B/C/D pass
- known-bad bundle fails

H. Reproducibility
- command, config hash, source corpus hash, artifact manifest present
- report generated from leaf audit
- no one-line huge report
- no report-only pass

I. Runtime honesty
- run mode correctly labeled
- runtime plausible for claimed work

If any hard gate fails:
- final status = NOT_READY or EXTERNAL_BLOCKER_NOT_READY.
- do not use FULL_UNIVERSE_STAGE_MAP_PASS.

================================================================================
15. Required Tests
================================================================================

Add/strengthen:

tests/test_census_v4_legacy_runner_lockout.py
tests/test_census_v4_artifact_manifest.py
tests/test_census_v4_report_generated_from_leaf_audit.py
tests/test_census_v4_claim_to_stage_forensic_audit.py
tests/test_census_v4_source_task_realness_audit.py
tests/test_census_v4_existing_ledger_reuse_audit.py
tests/test_census_v4_last_effective_thesis_not_dummy.py
tests/test_census_v4_source_coverage_audit.py
tests/test_census_v4_runtime_plausibility_audit.py
tests/test_census_v4_reviewer_trace_forensics.py
tests/test_census_v4_reviewer_source_realness.py
tests/test_census_v4_reviewer_stage_semantics.py
tests/test_census_v4_reviewer_runtime_plausibility.py
tests/test_census_v4_known_bad_bundle.py
tests/test_census_v4_run_mode_honesty.py
tests/test_census_v4_hard_gates.py
tests/test_census_v4_no_report_only_pass.py
tests/test_census_v4_no_summary_only_pass.py
tests/test_census_v4_no_replay_as_live.py

Full test command:
PYTHONPATH=src python -m unittest discover -s tests -v

No skipped Census v4 tests.
No xfail for known issues.
No threshold-loosening tests.
Known-bad fixtures must fail correctly.

================================================================================
16. Required Reports
================================================================================

Generate:

docs/operational/census_mode_v4_acceptance_report.md
docs/operational/census_mode_v4_readiness_verdict.md
docs/operational/census_mode_v4_artifact_manifest.json
docs/operational/census_mode_v4_sample_leaf_bundle.jsonl
docs/operational/census_mode_v4_reproduction_command.md
docs/operational/census_mode_v4_leaf_artifact_audit.json
docs/operational/census_mode_v4_claim_to_stage_forensic_audit.json
docs/operational/census_mode_v4_source_task_realness_audit.json
docs/operational/census_mode_v4_existing_ledger_reuse_audit.json
docs/operational/census_mode_v4_last_effective_thesis_audit.json
docs/operational/census_mode_v4_source_coverage_audit.json
docs/operational/census_mode_v4_runtime_plausibility_audit.json
docs/operational/census_mode_v4_reviewer_A_trace_forensics.json
docs/operational/census_mode_v4_reviewer_B_source_realness.json
docs/operational/census_mode_v4_reviewer_C_stage_semantics.json
docs/operational/census_mode_v4_reviewer_D_runtime_plausibility.json
docs/operational/census_mode_v4_known_bad_regression_report.json
docs/operational/census_mode_v4_self_repair_summary.md

Output:
output/census_v4/YYYY-MM-DD/...
or if too large:
output manifest + sample bundle + reproduction command must be committed.

================================================================================
17. Final Answer Format
================================================================================

After completion, report only:

1. Final status
2. Commit SHA / message / push status / working tree
3. Test result
4. Run mode
5. Artifact manifest summary
6. Universe / stage distribution
7. Source coverage
8. Source task realness
9. Existing ledger reuse
10. Claim-to-stage forensic audit
11. Leaf artifact audit
12. Reviewer A/B/C/D
13. Runtime plausibility
14. Known-bad regression result
15. Watchlist seed / deep backfill plan
16. Final verdict
17. Remaining blockers

================================================================================
18. Prohibitions
================================================================================

- Do not claim pass from acceptance report alone.
- Do not claim pass without leaf artifact manifest.
- Do not claim pass without claim_to_stage_trace.jsonl.
- Do not use old census_runner.py for pass.
- Do not leave accepted_claims=(), score_contributions=() in production/pass path.
- Do not count report replay as real source execution.
- Do not count PARSED-with-empty-claims as claim-producing.
- Do not claim live/LLM if provider/LLM calls are zero.
- Do not mark all Stage0/Unknown/ProviderPending as pass.
- Do not use source_proxy/evidence_url_pending/price_path_only as score.
- Do not use market anomaly/news snippet as score.
- Do not use recent lookback as Stage cutoff.
- Do not finalize low score on provider failure.
- Do not hardcode symbols/URLs/keywords.
- Do not loosen thresholds to pass.
- Do not create fake leaf artifacts.
- Do not output one-line huge reports.

================================================================================
19. One-line goal
================================================================================

Census v4의 목적은 “FULL_UNIVERSE_STAGE_MAP_PASS라고 쓰인 report”가 아니다.

목적은:

전체 KRX universe의 각 symbol마다
source timeline,
last effective thesis,
baseline,
depth,
source task,
accepted claim,
score contribution,
StageCourt trace,
CensusStageStatus가
leaf artifact로 연결되어 있고,
독립 auditor가 report 없이 재계산해도 같은 결론이 나오는 전 시장 Stage 지도다.

실패하면 숨기지 말고,
원인을 찾아 패치하고,
같은 명령으로 재실행해서,
runtime-proven FULL_UNIVERSE_STAGE_MAP_PASS가 될 때까지 반복하라.

핵심만 다시 말하면, 지금 baaf2e7은 보고서 상태를 바꾼 report-only 커밋이고, 구현은 c5bc76a야. c5bc76a는 Census v3 구조를 많이 넣었지만, 외부에서 봤을 때 full output leaf artifacts가 없고, 구형 runner 경로도 그대로 남아 있어서 “진짜 전체지도 성공”을 확정하기엔 아직 부족해.

다음 Goal은 “또 통과했다고 쓰기”가 아니라, 통과를 증명하는 물증을 커밋하게 만드는 것이야.
