너는 Daikisong/stock_agent 레포의 E2R Research Brain v1을 구현하는 coding agent다.

현재 전제:
- Evidence OS v2는 이미 운영 READY 상태로 간주한다.
- Evidence OS v2는 문서 → claim → target/temporal adjudication → primitive mapping → ScoreContribution → deterministic StageCourt 경로를 담당한다.
- 이제 할 일은 Evidence OS를 다시 고치는 것이 아니라, 기존 대량 연구 MD/output/reports를 런타임 조사 두뇌로 바꾸는 Research Brain / Memory Compiler / Runtime Planner를 구현하는 것이다.

최종 목표:

과거 E2R 연구자료 전체를 읽어
각 아키타입별 성공 조건, 실패 조건, Green blocker, 4B/4C guard, false-positive pattern, source route, query-success pattern, source-gap을 ResearchMemoryRecord로 정규화하고,
현재 시장에서 생긴 CandidateEvent를 보았을 때
“이 후보는 어느 아키타입이고, 과거 연구상 무엇을 더 확인해야 하며, 어떤 source family를 먼저 봐야 하는가”를 LLM이 계획하게 하라.

단:
- Research Brain은 절대 점수를 직접 주지 않는다.
- Research Brain은 Stage를 직접 결정하지 않는다.
- Research Brain은 source task, investigation plan, hypothesis, counter-thesis, missing primitive priority만 만든다.
- 실제 점수와 Stage는 기존 Evidence OS v2 + deterministic scorer + StageCourt가 계산한다.
- Evidence OS가 accepted/current/direct/source-backed claim으로 인정하지 않은 내용은 score/stage에 절대 들어가지 않는다.

================================================================================
0. 기존 Evidence OS v2 불변 조건
================================================================================

이 작업에서 다음은 건드리지 마라.

1. scoring weight
2. Stage threshold
3. deterministic StageCourt gate
4. Evidence OS v2 eligibility rule
5. ScoreContribution claim-backed rule
6. legacy parser quarantine rule
7. source_proxy_only production contribution 차단
8. snippet-only production contribution 차단
9. hard break current OPEN/direct/source-quorum rule
10. score delta audit rule

작업 전과 작업 후 다음 테스트는 계속 통과해야 한다.

PYTHONPATH=src python -m unittest discover -s tests -v

Evidence OS v2 acceptance report 기준을 깨면 이번 Goal은 실패다.

새 Research Brain은 Evidence OS v2 위에 얹히는 두뇌 계층이다.
Evidence OS의 법정 심리를 우회하는 새 점수 경로를 만들지 마라.

================================================================================
1. 개념 분리
================================================================================

이 프로젝트에는 이제 세 층이 있다.

A. Evidence OS
- 문서 하나가 점수에 들어갈 수 있는지 판정
- claim의 source, quote/anchor, subject, target scope, date, lifecycle, primitive mapping, contradiction을 검증
- ScoreContribution과 StageCourt를 deterministic하게 실행

B. Research Brain
- 과거 연구자료에서 배운 아키타입별 판례를 memory로 보관
- 현재 후보의 evidence gap과 stage blocker를 보고 무엇을 더 조사해야 하는지 계획
- source task, missing primitive priority, red-team task, source family route를 생성
- 점수 직접 계산 금지

C. Runtime Discovery
- 전 시장 structured scan으로 CandidateEvent 생성
- Research Brain이 아키타입 가설과 조사계획 생성
- Source Router가 공식자료 우선으로 bounded acquisition 실행
- Evidence OS가 claim 검증
- deterministic scorer/stage가 최종 출력

쉬운 비유:
- Research Brain = 과거 판례를 기억하는 조사 전략가
- Evidence OS = 증거능력을 심사하는 판사/서기
- Scorer/StageCourt = 점수와 판결을 계산하는 deterministic 엔진

================================================================================
2. 새 모듈 구조
================================================================================

다음 모듈을 새로 추가하거나 동등한 구조로 구현하라.

src/e2r/research_brain/
    __init__.py
    schemas.py
    artifact_discovery.py
    research_artifact_parser.py
    research_row_normalizer.py
    source_quality_classifier.py
    memory_record.py
    memory_store.py
    memory_graph.py
    memory_compiler.py
    archetype_memory_compiler.py
    source_route_memory.py
    query_pattern_memory.py
    counterexample_memory.py
    green_blocker_memory.py
    stage_transition_memory.py
    memory_retriever.py
    candidate_context.py
    hypothesis_builder.py
    investigation_planner.py
    runtime_planner.py
    red_team_planner.py
    source_task_bridge.py
    evidence_os_bridge.py
    memory_leakage_audit.py
    memory_acceptance.py
    reports.py

configs/e2r_research_brain_v1.json
configs/e2r_research_memory_usage_policy_v1.json

docs/operational/research_brain_v1_acceptance_report.md
docs/operational/research_brain_v1_inventory.json
docs/operational/research_brain_v1_archetype_matrix.json
docs/operational/research_brain_v1_source_quality_matrix.json
docs/operational/research_brain_v1_memory_records_sample.jsonl
docs/operational/research_brain_v1_leakage_audit.json
docs/operational/research_brain_v1_planner_replay_results.json
docs/operational/research_brain_v1_discovery_dry_run_results.json
docs/operational/research_brain_v1_source_route_audit.json
docs/operational/research_brain_v1_gap_inventory.json
docs/operational/research_brain_v1_known_regressions.md

필수 CLI 또는 동등한 실행 entrypoint:

src/e2r/cli/build_research_memory.py
src/e2r/cli/audit_research_memory.py
src/e2r/cli/run_research_brain_replay.py
src/e2r/cli/run_research_brain_discovery_dry_run.py
src/e2r/cli/research_brain_report.py

기존 `src/e2r/pipeline/daily_scan.py`, `morning_pipeline.py`, `company_research.py`, `korea_live_lite.py`, `stage_update.py`와 연결하라.
기존 `src/e2r/research/source_router.py`, `official_follow_up_provider.py`, `report_radar.py`, `search_budget.py`, `search_result_ranker.py`, `search_snapshot_store.py`, `report_snapshot_store.py`와도 연결하라.

================================================================================
3. ResearchMemoryRecord 스키마
================================================================================

과거 연구 MD/output/report에서 뽑은 모든 memory row는 아래 스키마 또는 동등한 엄격 스키마를 가져야 한다.

ResearchMemoryRecord:

{
  "record_id": "...",
  "schema_version": "research_memory_v1",

  "source_artifact_path": "...",
  "source_artifact_sha256": "...",
  "source_artifact_type": "md|json|jsonl|csv|report",
  "source_line_or_span": "...",

  "research_session": "...",
  "mode": "...",
  "round": "R2",
  "loop": 209,
  "large_sector_id": "...",
  "canonical_archetype_id": "...",
  "fine_archetype_id": "...",

  "row_type": "case|trigger|score_simulation|shadow_weight|residual_contribution|aggregate_metric|price_source_validation",
  "case_id": "...",
  "trigger_id": "...",
  "symbol": "...",
  "company_name": "...",
  "trigger_type": "...",
  "trigger_date": "YYYY-MM-DD",
  "entry_date": "YYYY-MM-DD",

  "memory_type": "primitive_success_case|primitive_failure_case|green_blocker|stage_gate_failure|false_positive_pattern|counterexample|4b_watch_condition|4c_thesis_break_condition|source_route_pattern|query_success_pattern|query_failure_pattern|source_gap|lifecycle_rule|score_weight_support|replay_fixture_candidate",

  "positive_or_counterexample": "positive|counterexample|guard|mixed|unknown",
  "stage_before": "...",
  "stage_after": "...",
  "expected_stage_effect": "...",

  "primitive_ids": [],
  "required_bridges": [],
  "missing_bridges": [],
  "green_blockers": [],
  "guard_primitives": [],
  "hard_break_primitives": [],
  "false_positive_patterns": [],

  "source_family": "...",
  "source_url": "...",
  "source_quality": "url_backed|url_backed_repair_needed|source_proxy_only|evidence_url_pending|price_path_only|invalid|unknown",
  "evidence_url_status": "present|pending|missing|not_applicable",
  "source_proxy_only": false,
  "evidence_url_pending": false,
  "production_ready_evidence": false,
  "fixture_usable": false,
  "ontology_usable": true,
  "runtime_score_eligible": false,

  "free_source_route_hints": [],
  "preferred_source_classes": [],
  "fallback_source_classes": [],
  "forbidden_source_classes": [],
  "query_pattern_hints": [],
  "bad_query_patterns": [],

  "price_outcome": {
    "mfe_30d_pct": null,
    "mae_30d_pct": null,
    "mfe_90d_pct": null,
    "mae_90d_pct": null,
    "mfe_180d_pct": null,
    "mae_180d_pct": null,
    "post_peak_drawdown_pct": null,
    "corporate_action_contaminated": false,
    "future_outcome_zone": true
  },

  "usage_policy": {
    "allowed_for_runtime_planning": true,
    "allowed_for_evidence_extraction_prompt": false,
    "allowed_for_score_contribution": false,
    "allowed_for_replay_fixture": false,
    "allowed_for_ontology": true,
    "allowed_for_query_planning": true,
    "allowed_for_red_team_planning": true
  },

  "leakage_controls": {
    "contains_future_price_outcome": true,
    "contains_future_stage_label": true,
    "may_be_seen_by_runtime_llm": false,
    "may_be_seen_by_extractor_llm": false,
    "may_be_seen_by_planner_llm_as_pattern_summary": true
  },

  "dedupe_key": "...",
  "confidence": "high|medium|low",
  "notes": "..."
}

중요:
- `price_outcome`은 runtime evidence extraction LLM에게 절대 보여주지 마라.
- MFE/MAE/outcome label은 Research Brain의 aggregate pattern과 replay 평가에는 쓸 수 있지만, 현재 후보의 claim extraction이나 score contribution에는 들어가면 안 된다.
- `source_proxy_only=true`인 row는 production score fixture가 아니다.
- `evidence_url_pending=true`인 row는 production score fixture가 아니다.
- source_proxy row도 ontology, false-positive pattern, source route, Green blocker 설계에는 쓸 수 있다.

================================================================================
4. 연구자료 등급 분류
================================================================================

모든 연구 artifact row를 아래 등급으로 분류하라.

A_URL_BACKED_REPLAY_READY
조건:
- source_proxy_only=false
- evidence_url_pending=false
- 실제 source_url 있음
- as_of_date/trigger_date와 source_date 정합
- source anchor 또는 quote 생성 가능
- target/primitive mapping 가능
- corporate-action window clean
- production fixture로 사용 가능

B_URL_BACKED_REPAIR_NEEDED
조건:
- URL은 있음
- 그러나 quote/date/anchor/snapshot/parse 중 일부 수리 필요
- production fixture 전에는 repair task 필요

C_SOURCE_PROXY_ONTOLOGY_ONLY
조건:
- source_proxy_only=true 또는 evidence_url_pending=true
- business narrative는 있음
- production score fixture로 사용 금지
- ontology, primitive, false-positive, source route 설계에만 사용

D_PRICE_PATH_ONLY_OR_FUTURE_LEAKAGE_RISK
조건:
- price path, MFE/MAE, outcome label 중심
- non-price evidence가 약함
- production evidence fixture 금지
- calibration/guardrail 참고만 가능

E_INVALID_OR_DUPLICATE
조건:
- hard duplicate
- corporate-action contaminated
- missing entry
- inconsistent schema
- out-of-scope
- future leakage cannot be separated

각 record에는 반드시 `source_quality_class`와 `usage_policy`가 있어야 한다.

예시 분류:
- C06 HBM SK하이닉스 sold-out / HBM revenue mix / 삼성 qualification lag 등 URL-backed rows는 A 또는 B 후보.
- C08 customer/order/product-profile cases with URLs는 A/B 후보.
- C15 direct URL spread/pass-through rows는 A/B 후보. 단 raw commodity headline과 issuer-level pass-through를 분리해야 함.
- C17/C24/C28의 source_proxy_only/evidence_url_pending rows는 C로 분류.
- C24 binary event price-path only rows는 D 또는 C로 분류하고 production score 정답으로 금지.

================================================================================
5. Artifact Discovery
================================================================================

레포 안의 다음 위치를 자동 스캔하라.

- docs/
- docs/core/
- docs/0619/
- docs/round/
- output/
- reports/e2r_calibration/
- fixtures/historical/
- configs/
- any e2r_stock_web_v12_residual_round_*.md
- any V12 research ledger/index/report json/csv/md

하드코딩된 파일 리스트로 끝내지 마라.
glob과 manifest discovery를 같이 사용하라.

각 artifact에 대해:

- file path
- sha256
- created/modified if available
- detected schema_family
- detected canonical_archetype_id
- detected large_sector_id
- detected round/loop
- detected row blocks
- JSONL rows parse count
- table rows parse count
- evidence URL count
- source_proxy count
- evidence_url_pending count
- calibration_usable count
- duplicate count
- parse errors

를 inventory로 남겨라.

필수 산출물:
docs/operational/research_brain_v1_inventory.json

================================================================================
6. Research Artifact Parser
================================================================================

MD 안에 섞여 있는 다음 형식을 모두 파싱하라.

- YAML front matter
- fenced json/jsonl blocks
- fenced csv blocks
- markdown tables
- plain text metadata
- evidence source maps
- score simulation rows
- shadow_weight rows
- residual contribution rows
- handoff prompt caveats
- validation caveats

파싱 결과는 RawResearchRow로 만든 뒤 ResearchMemoryRecord로 normalize하라.

중요:
- JSONL row가 source of truth다.
- Markdown table은 보조다.
- plain narrative는 LLM parser를 통해 pattern candidate로 추출할 수 있으나, source_proxy_only일 가능성이 높으므로 usage_policy를 보수적으로 둬라.
- handoff prompt의 “do not promote”, “shadow_only”, “production_scoring_changed=false”, “source_proxy_only”, “evidence_url_pending” 문구를 반드시 usage_policy에 반영하라.

================================================================================
7. Memory Type 분해
================================================================================

하나의 연구 row에서 여러 memory record가 나올 수 있다.

예:
C06 SK하이닉스 sold-out row
→ primitive_success_case: hbm_capacity_pre_sold
→ source_route_pattern: Reuters trusted news for HBM sold-out/capacity
→ green_blocker: cashflow/repeat evidence needed
→ 4B_watch_condition: post-peak drawdown / conventional memory drag

C28 security theme false positive row
→ false_positive_pattern: security keyword without ARR/RPO/renewal
→ green_blocker: retention bridge absent
→ source_gap: source_proxy_only/evidence_url_pending
→ source_route_hint: IR/사업보고서/earnings call/broker PDF needed for ARR/RPO/renewal

C15 raw commodity row
→ false_positive_pattern: commodity weather without issuer pass-through
→ source_route_pattern: DART/IR for OPM/FCF, product price/pass-through
→ 4B_watch_condition: local peak / late phase

C24 binary clinical event
→ hard_break_pattern: negative binary regulatory/clinical resolution
→ green_blocker: endpoint/regulatory/partner/funding bridge required
→ source_route_pattern: company disclosure/regulator/clinical registry
→ leakage rule: future approval/rejection outcome cannot be shown to extraction prompt

필수 memory_type enum:

- primitive_success_case
- primitive_failure_case
- primitive_partial_case
- green_blocker
- yellow_blocker
- stage2_actionable_unlock
- stage2_watch_cap
- false_positive_pattern
- counterexample
- 4b_watch_condition
- 4b_late_phase_condition
- 4c_thesis_break_condition
- hard_break_pattern
- lifecycle_rule
- source_route_pattern
- source_family_reliability
- source_gap
- query_success_pattern
- query_failure_pattern
- evidence_contract_candidate
- source_quorum_hint
- replay_fixture_candidate
- production_fixture_candidate
- ontology_only_rule_candidate
- score_weight_support
- score_weight_counterexample

================================================================================
8. Research Memory Store
================================================================================

ResearchMemoryStore를 구현하라.

요구사항:
- JSONL store 지원
- SQLite 또는 parquet optional 지원
- content-addressed artifact hash 저장
- record_id deterministic
- dedupe_key deterministic
- 동일 artifact 재처리 idempotent
- 같은 row 재처리 시 memory record 증식 금지
- source_proxy와 URL-backed 분리 인덱스
- archetype_id, large_sector_id, memory_type, primitive_id, source_quality_class, usage_policy별 조회
- as_of_date leakage filter 지원

필수 API:

ResearchMemoryStore.add_records(records)
ResearchMemoryStore.query(
    archetype_id=None,
    large_sector_id=None,
    memory_type=None,
    primitive_id=None,
    source_quality_class=None,
    allowed_for_runtime_planning=True,
    exclude_future_leakage=True,
    limit=...
)

ResearchMemoryStore.get_archetype_profile(archetype_id)
ResearchMemoryStore.get_source_routes(archetype_id, primitive_id)
ResearchMemoryStore.get_false_positive_patterns(archetype_id)
ResearchMemoryStore.get_green_blockers(archetype_id)
ResearchMemoryStore.get_replay_fixtures(archetype_id)
ResearchMemoryStore.get_source_gaps(archetype_id)

================================================================================
9. Archetype Memory Profile
================================================================================

각 C01~C36에 대해 ArchetypeMemoryProfile을 생성하라.

ArchetypeMemoryProfile:

{
  "canonical_archetype_id": "...",
  "large_sector_id": "...",

  "memory_record_count": 0,
  "url_backed_count": 0,
  "source_proxy_count": 0,
  "price_path_only_count": 0,
  "production_fixture_count": 0,
  "ontology_only_count": 0,

  "positive_patterns": [],
  "failure_patterns": [],
  "false_positive_patterns": [],
  "green_blockers": [],
  "yellow_blockers": [],
  "stage2_unlock_conditions": [],
  "stage2_cap_conditions": [],
  "4b_watch_conditions": [],
  "4c_thesis_break_conditions": [],

  "required_primitives_observed": [],
  "optional_primitives_observed": [],
  "guard_primitives_observed": [],
  "hard_break_primitives_observed": [],

  "source_routes": [],
  "source_family_reliability": [],
  "query_pattern_hints": [],
  "bad_query_patterns": [],

  "fixture_status": {
    "positive_url_backed": false,
    "guard_url_backed": false,
    "wrong_subject": false,
    "old_risk_resolved": false,
    "current_hard_break": false,
    "source_missing_pending": false
  },

  "source_gap_summary": [],
  "runtime_usage_policy": "ready|planning_only|source_gap|unsupported"
}

출력:
docs/operational/research_brain_v1_archetype_matrix.json

================================================================================
10. Research Brain Prompting 원칙
================================================================================

Research Brain LLM에게 과거 memory를 보여줄 수 있다.
하지만 다음 제한을 반드시 지켜라.

허용:
- 아키타입별 일반화된 pattern summary
- source route hint
- false-positive guard
- Green blocker
- missing primitive priority
- query-success pattern
- query-failure pattern
- source family reliability
- source gap warning

금지:
- 현재 후보 문서 extraction prompt에 과거 MFE/MAE 직접 제공
- 현재 후보 claim extraction에 미래 outcome label 제공
- source_proxy_only narrative를 현재 사실처럼 제공
- “과거에 이 케이스가 올랐으니 현재도 positive” 식의 prompt
- 특정 종목명 성공 사례를 그대로 current candidate bias로 사용
- 현재 후보와 무관한 과거 ticker를 점수 근거처럼 제시
- Research Brain LLM이 score/stage를 반환하는 schema

Research Brain LLM 출력은 다음까지만 허용:

{
  "primary_archetype_hypothesis": "...",
  "secondary_archetype_hypotheses": [],
  "positive_thesis": "...",
  "counter_thesis": "...",
  "recalled_memory_patterns": [],
  "must_verify_primitives": [],
  "green_blockers_to_close": [],
  "red_team_checks": [],
  "source_tasks": [],
  "query_suggestions": [],
  "do_not_promote_reasons": [],
  "planning_confidence": "high|medium|low"
}

금지 출력:
- score
- stage
- current_score_eligible
- hard_break final
- verified final
- accepted claim final

================================================================================
11. CandidateEvent 통합
================================================================================

Runtime Discovery는 종목명을 직접 넣는 targeted smoke만으로 끝나면 안 된다.

CandidateEvent 스키마를 명확히 하라.

CandidateEvent:

{
  "candidate_event_id": "...",
  "symbol": "...",
  "company_name": "...",
  "event_date": "YYYY-MM-DD",
  "event_type": "supply_contract|facility_investment|earnings_surprise|revision_up|report_radar|relative_strength|risk_event|ir_update|news_discovery|other",
  "source_family": "DART|KIND|KRX|CompanyGuide|IR|ReportRadar|Price|News|Manual",
  "source_id": "...",
  "magnitude": {},
  "freshness_days": 0,
  "candidate_reason": "...",
  "initial_evidence_ids": [],
  "structured_fields": {},
  "price_context": {},
  "eligible_for_research_brain": true
}

전 시장 scan에서 CandidateEvent가 생성되어야 한다.

사용할 수 있는 기존 경로:
- daily_scan.py
- morning_pipeline.py
- company_research.py
- report_radar.py
- official_follow_up_provider.py
- CompanyGuide / DART / KRX / KIND / price/volume connector

Research Brain은 CandidateEvent를 입력받아 hypothesis와 investigation plan을 만든다.

================================================================================
12. Runtime Planner Flow
================================================================================

최종 운영 flow:

1. Structured Scan
   - DART/KIND/KRX/CompanyGuide/ReportRadar/price로 CandidateEvent 생성

2. Candidate Triage
   - event freshness/magnitude/source quality/price context로 조사 우선순위 부여

3. Research Brain Hypothesis
   - CandidateEvent + existing evidence + archetype memory profile 입력
   - primary/secondary archetype hypothesis 생성
   - positive thesis / counter thesis 생성

4. Memory Retrieval
   - 해당 archetype의 success/failure/green blocker/source route/false-positive pattern 검색

5. Investigation Plan
   - must_verify_primitives
   - red_team_checks
   - source_tasks
   - follow-up queries
   - stop conditions

6. Source Router Bridge
   - Research Brain source_tasks를 기존 SourceRouter SourceTask로 변환
   - official-first
   - bounded budget
   - dedupe-before-fetch
   - stop-on-resolution

7. Evidence OS
   - fetched documents를 Evidence OS v2에 넣어 claim 검증

8. Score/Stage
   - deterministic score/stage 계산
   - Research Brain은 여기서 점수 개입 금지

9. Output
   - Green
   - Yellow-Pending
   - Stage2-Actionable
   - Stage2-Watch
   - 4B-watch
   - Reject/Red
   - follow-up tasks

================================================================================
13. SourceTask 생성 규칙
================================================================================

Research Brain은 “검색어”만 내면 안 된다.
SourceTask를 우선 만들어야 한다.

SourceTask:

{
  "task_id": "...",
  "candidate_event_id": "...",
  "symbol": "...",
  "company_name": "...",
  "archetype_id": "...",
  "primitive_gap": "...",
  "task_type": "positive_verify|green_closure|red_team|source_repair|lifecycle_followup|contradiction_resolution",
  "preferred_source_classes": [],
  "fallback_source_classes": [],
  "forbidden_source_classes": [],
  "allowed_domains": [],
  "date_window": {},
  "max_queries": 3,
  "max_candidates": 20,
  "max_fetches": 5,
  "stop_condition": {
    "accepted_claim_count": 1,
    "counter_claim_check_done": true
  },
  "llm_query_allowed": true,
  "general_search_allowed": false,
  "reason_from_memory": "...",
  "memory_record_ids": []
}

예:
- FCF gap → DART/XBRL/API only, general_search_allowed=false
- 공급계약 gap → DART/KIND/company IR 우선
- C06 qualification gap → issuer IR/customer official/trusted news
- C28 ARR/RPO/renewal gap → 사업보고서/IR/earnings call/public broker PDF
- C24 endpoint/regulatory gap → company disclosure/regulator/clinical registry
- C15/C17 spread gap → DART/IR/product price/realized margin/FCF bridge

금지:
- 모든 gap을 네이버 검색어로 변환
- FCF gap을 뉴스 검색으로 해결
- DART/IR로 해결 가능한 gap에서 general web fetch
- top_results=None
- retry_max=None
- max_fetches 없는 source task
- dedupe 전 fetch

================================================================================
14. Research Brain과 Evidence OS 연결
================================================================================

Research Brain이 만든 source task의 결과는 반드시 Evidence OS로 들어간다.

절대 금지:
Research Brain planning output → FeatureInput 직접 입력
Research Brain planning output → ScoreContribution 직접 입력
Research Brain planning output → risk field 직접 입력
Research Brain planning output → StageCourt 직접 override

허용:
Research Brain planning output → SourceTask
SourceTask → fetch/parse
fetched document → Evidence OS
Evidence OS accepted claim → ScoreContribution
ScoreContribution → deterministic score/stage

테스트:
- Research Brain이 “C28 ARR 필요”라고 해도 ARR claim이 Evidence OS에서 accepted되지 않으면 C28 score는 올라가지 않아야 한다.
- Research Brain이 “C24 hard 4C risk”라고 해도 current OPEN direct source-backed claim 없으면 hard 4C가 되면 안 된다.
- Research Brain이 source_proxy_only memory를 recall해도 production score contribution은 0이어야 한다.

================================================================================
15. Memory Leakage Audit
================================================================================

과거 연구자료에는 미래 MFE/MAE, outcome label, 현재 profile error verdict가 들어 있다.
이것은 runtime planner의 pattern memory에는 제한적으로 쓸 수 있지만, current evidence extraction에는 절대 들어가면 안 된다.

Leakage zones:

A. PLANNING_PRIOR_ALLOWED
- aggregate false-positive pattern
- source route hint
- green blocker
- do-not-promote rule
- archetype guard pattern

B. EXTRACTION_FORBIDDEN
- MFE/MAE
- peak/trough
- future drawdown
- outcome label
- “이 케이스는 성공했다/실패했다”
- future stage override
- score-return alignment

C. REPLAY_EVALUATION_ONLY
- expected future path
- expected stage label after outcome
- calibrated profile error

MemoryLeakageAudit는 다음을 검사해야 한다.

- current candidate Evidence OS extraction prompt에 MFE/MAE 없음
- current candidate claim extraction prompt에 future outcome 없음
- source_proxy_only narrative가 current claim으로 쓰이지 않음
- memory record with contains_future_price_outcome=true는 extractor LLM에 전달되지 않음
- planning prompt에는 pattern summary만 전달되고 raw future tables는 전달되지 않음
- replay fixture에서는 as_of source와 future outcome을 분리

출력:
docs/operational/research_brain_v1_leakage_audit.json

필수 결과:
future_outcome_in_extraction_prompt_count = 0
source_proxy_to_score_count = 0
memory_record_without_usage_policy_count = 0
runtime_llm_seen_forbidden_future_field_count = 0

================================================================================
16. Query Pattern Memory
================================================================================

QueryPatternMemory는 deterministic query template이 아니다.

나쁜 방식:
if archetype == C06:
    query = "{company} HBM 장기공급계약 선수금"

좋은 방식:
Research Brain retrieves:
- C06 requires customer allocation / capacity sold-out / HBM revenue mix / cashflow bridge.
- Strong sources historically include Reuters, issuer IR, earnings release, customer official, DART cashflow.
Then LLM planner generates context-specific query:
- "{company} 2026 earnings call HBM revenue mix customer allocation"
- "{company} HBM sold out capacity 2026 customer demand IR"
But SourceRouter validates:
- company scope
- date window
- source class
- no duplicate
- no future leakage
- max_fetches

QueryPatternMemory fields:
{
  "pattern_id": "...",
  "archetype_id": "...",
  "primitive_id": "...",
  "successful_source_classes": [],
  "unsuccessful_source_classes": [],
  "good_query_intent": "...",
  "bad_query_intent": "...",
  "example_queries": [],
  "must_not_hardcode": true,
  "source_route_first": true
}

Example queries are training examples only.
Do not turn them into deterministic templates.

================================================================================
17. Red Team Memory
================================================================================

각 아키타입별 counterexample/false-positive/4B/4C memory를 RedTeamPlanner가 써야 한다.

RedTeamPlanner input:
- candidate_event
- archetype hypothesis
- accepted positive claims
- recalled false-positive patterns
- recalled 4B/4C patterns
- unresolved guard primitives

RedTeamPlanner output:
{
  "red_team_checks": [
    {
      "guard_primitive": "...",
      "reason_from_memory": "...",
      "source_task": {...}
    }
  ],
  "do_not_promote_reasons": [],
  "hard_break_checks": []
}

예:
C06:
- HBM word only
- package substrate sympathy
- qualification lag with reopen path = 4B/watch, not hard 4C
- customer allocation absent
- cashflow/repeat evidence absent

C08:
- product profile only
- customer quality award without order/revenue conversion
- high MAE on valid bridge blocks Green, not Stage2

C15/C17:
- raw commodity weather
- realized spread/OPM/FCF absent
- late phase/result-only Green trap
- high MAE without route death = watch/phase cap, not hard 4C

C24:
- approval/event-only
- endpoint/regulatory/partner/funding bridge absent
- binary clinical failure requires current direct source
- resubmission/reopen lifecycle must be checked

C28:
- software/security keyword only
- ARR/RPO/renewal/retention/churn absent
- public contract headline without recurring revenue bridge

================================================================================
18. Research Brain Planner Replay
================================================================================

Research Brain은 실제 운영 전에 과거 fixture로 replay되어야 한다.

Replay 종류:

A. Source-backed positive replay
- URL-backed A-grade research row를 사용
- Research Brain이 필요한 primitive/source route를 복원해야 함
- Evidence OS가 accepted claim을 만들 수 있어야 함

B. Source-proxy ontology replay
- source_proxy_only row를 사용
- Research Brain은 pattern/source gap으로만 분류해야 함
- production score fixture로 승격하면 실패

C. False-positive replay
- Research Brain이 do-not-promote / guard / missing bridge를 찾아야 함

D. Wrong-source/wrong-subject replay
- Research Brain이 source task로 넘기더라도 Evidence OS가 score 차단해야 함

E. Lifecycle replay
- 과거 risk → 현재 follow-up or resolved/superseded

F. Discovery replay
- CandidateEvent만 보고 적절한 archetype hypothesis와 source tasks 생성

필수 아키타입:
- C06
- C08
- C15
- C17
- C24
- C28

전 C01~C36은 최소 memory profile과 source gap status가 있어야 한다.

================================================================================
19. C06 / C08 / C15 / C17 / C24 / C28 기준 예시
================================================================================

C06_HBM_MEMORY_CUSTOMER_CAPACITY:
Memory must learn:
- HBM keyword alone is not enough.
- Strong positive: customer allocation, capacity pre-sold, HBM revenue mix, shipment visibility.
- SK hynix sold-out/revenue mix rows are URL-backed positive replay candidates.
- Samsung qualification lag is 4B/watch if optimization/reopen path remains alive.
- package substrate/FCBGA/MLB sympathy is Stage2 cap unless issuer-level order/revenue/margin conversion exists.
- Green requires repeat evidence and cashflow/margin bridge.

C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY:
Memory must learn:
- product roadmap/profile only is Stage2 cap or watch.
- named customer/order/qualification can unlock Actionable.
- customer-quality award alone does not unlock Yellow/Green.
- direct order bridge with high MAE preserves Stage2 but blocks Green.
- hard 4C requires customer loss/order cancellation/failed qualification/revenue collapse, not price drawdown alone.

C15_MATERIAL_SPREAD_SUPERCYCLE:
Memory must learn:
- commodity weather is not issuer pass-through.
- product price/pass-through/customer route unlocks Stage2-Actionable.
- realized margin/OPM/EPS revision/FCF required for Yellow/Green.
- stale result after theme rerating becomes 4B/watch.
- high MAE with surviving route is phase/watch, not hard 4C.

C17_CHEMICAL_COMMODITY_MARGIN_SPREAD:
Memory must learn:
- spread narrative must convert to realized spread or OPM/FCF.
- feedstock/product price changes need inventory lag and issuer margin bridge.
- spread false positive if realized margin bridge absent.
- 4B audit after high MFE and spread-cycle peak.

C24_BIO_TRIAL_DATA_EVENT_RISK:
Memory must learn:
- data/approval/pre-approval headline is binary event risk.
- Stage2 requires endpoint quality, regulatory path, partner/platform validation, funding runway or commercialization route.
- Green blocked by default unless non-binary commercialization bridge exists.
- negative binary resolution can be hard break only if current direct source-backed claim exists.
- source_proxy_only clinical rows are ontology only until URL repair.

C28_SOFTWARE_SECURITY_CONTRACT_RETENTION:
Memory must learn:
- software/security keyword is signboard, not contract quality.
- Stage2-Actionable requires ARR/RPO/renewal/retention/churn/contract backlog/recurring service evidence.
- security theme spike without retention bridge is false positive.
- ERP/SaaS operating leverage can work but needs renewal/churn/margin/cash bridge before Yellow/Green.

================================================================================
20. Candidate Discovery Dry Run
================================================================================

Research Brain 완료 전 targeted smoke만 돌리지 마라.

필수 dry run:
- targeted_smoke_only=false
- 실제 CandidateEvent discovery path 사용
- DART/KIND/KRX/CompanyGuide/ReportRadar/price structured scan 사용
- 최소 30개 candidate event 생성 또는 provider/source gap 명시
- 각 large_sector_id에서 최소 3개 candidate event 시도
- 각 candidate에 Research Brain hypothesis 생성
- source task 생성
- Evidence OS로 최소 일부 claim 검증
- deterministic stage 출력

출력 필드:
{
  "candidate_event_id": "...",
  "symbol": "...",
  "company_name": "...",
  "event_type": "...",
  "event_date": "...",
  "primary_archetype_hypothesis": "...",
  "recalled_memory_count": 0,
  "source_task_count": 0,
  "official_source_task_count": 0,
  "general_search_task_count": 0,
  "accepted_claim_count": 0,
  "verified_score": null,
  "provisional_score": null,
  "score_valid_status": "...",
  "base_stage": "...",
  "investigation_status": "...",
  "transition_overlay": "...",
  "green_blockers": [],
  "red_team_checks": [],
  "follow_up_tasks": []
}

================================================================================
21. Official-first 운영 원칙
================================================================================

Research Brain은 source route를 memory에서 배워야 한다.

우선순위:
1. DART / KIND / KRX / official structured
2. company IR / earnings release / conference call / newsroom
3. domain official: regulator, clinical registry, customer official, government tender/project
4. publicly accessible broker/industry PDF
5. trusted news
6. general search/Naver fallback

금지:
- Research Brain이 모든 task를 general search로 보냄
- 네이버 검색으로 FCF gap 해결
- 네이버 검색으로 DART 공급계약 해결
- source_proxy_only memory를 일반검색 반복으로 무작정 repair
- max_fetches 없는 source task
- 무제한 fetch

감사 지표:
- official_task_ratio
- general_search_task_ratio
- DART_solvable_gap_sent_to_web_count
- IR_solvable_gap_sent_to_web_count
- FCF_gap_sent_to_news_count
- unbounded_source_task_count
- stop_on_resolution_success_count

================================================================================
22. Integration with Existing Evidence OS v2 Reports
================================================================================

Research Brain acceptance report는 Evidence OS v2 report를 참조해야 한다.

필수:
- Evidence OS v2 acceptance report exists
- Evidence OS v2 verdict READY
- Research Brain tests run after Evidence OS tests
- Research Brain does not increase:
  - orphan score count
  - legacy direct path count
  - source_proxy contribution count
  - snippet-only contribution count
  - score delta without claim delta count

Research Brain은 Evidence OS v2의 산출물을 깎아먹으면 실패다.

================================================================================
23. 필수 테스트 파일
================================================================================

최소 다음 테스트 파일 또는 동등한 테스트를 추가하라.

tests/test_research_brain_artifact_discovery.py
tests/test_research_brain_row_parser.py
tests/test_research_brain_source_quality_classifier.py
tests/test_research_brain_memory_record_schema.py
tests/test_research_brain_memory_store_idempotency.py
tests/test_research_brain_usage_policy.py
tests/test_research_brain_leakage_audit.py
tests/test_research_brain_archetype_profiles.py
tests/test_research_brain_source_route_memory.py
tests/test_research_brain_query_pattern_memory.py
tests/test_research_brain_counterexample_memory.py
tests/test_research_brain_hypothesis_builder.py
tests/test_research_brain_investigation_planner.py
tests/test_research_brain_source_task_bridge.py
tests/test_research_brain_evidence_os_bridge.py
tests/test_research_brain_planner_replay_c06.py
tests/test_research_brain_planner_replay_c08.py
tests/test_research_brain_planner_replay_c15_c17.py
tests/test_research_brain_planner_replay_c24_c28.py
tests/test_research_brain_discovery_dry_run.py
tests/test_research_brain_no_score_direct_path.py
tests/test_research_brain_no_hardcoded_query_templates.py
tests/test_research_brain_no_source_proxy_score.py
tests/test_research_brain_with_evidence_os_v2_regression.py

필수 assertion:
- all memory records have usage_policy
- source_proxy_only production score eligibility count == 0
- evidence_url_pending production fixture count == 0
- extractor prompt future MFE/MAE count == 0
- Research Brain score output keys count == 0
- Research Brain stage override keys count == 0
- Research Brain direct FeatureInput mutation count == 0
- Research Brain source task without budget count == 0
- DART-solvable FCF task sent to general search count == 0
- repeated memory import duplicate growth == 0
- C01-C36 archetype profile exists
- C06 URL-backed replay route pass
- C24 source-proxy row classified ontology-only
- C28 security keyword false-positive memory retrieved
- C15 raw commodity weather guard retrieved
- Evidence OS v2 acceptance tests still pass

================================================================================
24. Hardcoding Audit
================================================================================

다음 패턴을 코드에서 검사하라.

금지:
- if symbol == ...
- if company_name == ...
- if archetype_id == "C06" then fixed query string
- if missing_primitive == "contract_quality" then fixed query string
- if "감사의견" in text then score/risk
- deterministic fallback query templates that bypass LLM planner
- source_proxy_only auto promotion
- MFE/MAE used inside current candidate extraction
- Research Brain output written directly into scoring payload

허용:
- registry.get(archetype_id)
- evidence_contract.get(archetype_id)
- source_route_policy.get(archetype_id, primitive_id)
- memory_store.query(archetype_id, memory_type)
- LLM planner creates query under source router constraints
- deterministic validator checks query scope/date/dedupe/future leakage

출력:
docs/operational/research_brain_v1_hardcoding_audit.json

================================================================================
25. Acceptance Matrix
================================================================================

Research Brain v1 완료 조건:

1. Evidence OS v2 acceptance still READY.
2. 전체 테스트 통과.
3. 연구 artifact inventory 생성.
4. ResearchMemoryRecord store 생성.
5. 모든 memory record에 source_quality_class와 usage_policy 있음.
6. source_proxy_only/evidence_url_pending row가 production score fixture로 승격되지 않음.
7. C01-C36 전체 ArchetypeMemoryProfile 생성.
8. 각 archetype에 URL-backed fixture 또는 explicit source gap/ontology-only 상태 표시.
9. C06/C08/C15/C17/C24/C28 planner replay 통과.
10. current candidate extraction prompt에 future outcome leakage 0.
11. Research Brain이 score/stage 직접 출력하지 않음.
12. Research Brain output이 FeatureInput/ScoreContribution을 직접 mutate하지 않음.
13. SourceTask는 모두 bounded budget 보유.
14. general search fallback ratio가 report에 기록됨.
15. DART/IR/CompanyGuide로 해결 가능한 gap은 general search로 가지 않음.
16. CandidateEvent discovery dry run이 targeted_smoke_only=false로 실행됨.
17. 최소 30개 candidate event 또는 provider/source gap 명시.
18. 각 large_sector_id에서 최소 3개 candidate event 시도 또는 source gap 명시.
19. Research Brain output이 Evidence OS로만 연결됨.
20. Evidence OS accepted claim 없는 점수 상승 0.
21. source_proxy_only memory recall 후 score contribution 0.
22. frozen memory import 3회 idempotent.
23. planner replay 3회 deterministic under fake/mock LLM.
24. live/dry-run LLM provider error는 pending/provider_failed로 기록.
25. acceptance report 생성.
26. working tree clean.
27. 한글 커밋 메시지로 commit/push.
28. 최종 답변에 commit SHA, test count, memory inventory, archetype matrix, leakage audit, discovery dry run, source gap, production readiness verdict 포함.

상태 라벨:
- IMPLEMENTATION_MERGED
- MEMORY_IMPORT_PASS
- LEAKAGE_AUDIT_PASS
- PLANNER_REPLAY_PASS
- DISCOVERY_DRY_RUN_PASS
- EVIDENCE_OS_INTEGRATION_PASS
- RESEARCH_BRAIN_READY
- PRODUCTION_RESEARCH_BRAIN_READY

Goal 완료라고 말하려면 최소:
RESEARCH_BRAIN_READY + EVIDENCE_OS_INTEGRATION_PASS + DISCOVERY_DRY_RUN_PASS

운영 준비 완료라고 말하려면:
PRODUCTION_RESEARCH_BRAIN_READY

================================================================================
26. 출력 Report 형식
================================================================================

최종 보고 파일:
docs/operational/research_brain_v1_acceptance_report.md

반드시 포함:

1. Commit
- commit_sha
- commit_message
- push_status
- working_tree_status

2. Tests
- command
- passed
- failed
- skipped
- failures if any

3. Evidence OS regression
- evidence_os_verdict_before
- evidence_os_verdict_after
- orphan_score_count_delta
- legacy_direct_path_delta
- source_proxy_contribution_delta

4. Research artifact inventory
- scanned_file_count
- parsed_artifact_count
- parsed_row_count
- parse_error_count
- duplicate_count
- source_proxy_count
- evidence_url_pending_count
- url_backed_count
- production_fixture_count

5. Memory store
- memory_record_count
- memory_type counts
- source_quality_class counts
- usage_policy counts
- idempotency result

6. Archetype matrix
- C01-C36 rows
- memory count
- URL-backed count
- ontology-only count
- source gap status
- fixture status

7. Leakage audit
- future outcome in extraction prompt count
- source_proxy_to_score count
- forbidden memory visible to extractor count
- result

8. Planner replay
- C06 result
- C08 result
- C15 result
- C17 result
- C24 result
- C28 result
- failures

9. Discovery dry run
- candidate_event_count
- sector coverage
- archetype coverage
- source task count
- official/general search ratio
- Evidence OS accepted claim count
- sample outputs

10. Source router audit
- DART-solvable gap sent to web count
- FCF gap sent to news count
- unbounded source task count
- stop-on-resolution success count

11. Production verdict
- READY / NOT_READY
- blockers
- source gaps
- exact next step if NOT_READY

================================================================================
27. 최종 응답 형식
================================================================================

작업 완료 후 사용자에게 다음 형식으로만 보고하라.

1. 최종 상태
- IMPLEMENTATION_MERGED / MEMORY_IMPORT_PASS / LEAKAGE_AUDIT_PASS / PLANNER_REPLAY_PASS / DISCOVERY_DRY_RUN_PASS / EVIDENCE_OS_INTEGRATION_PASS / RESEARCH_BRAIN_READY / PRODUCTION_RESEARCH_BRAIN_READY

2. 커밋
- SHA
- message
- push status
- working tree clean 여부

3. 테스트
- command
- pass/fail/skip

4. Memory inventory
- scanned files
- parsed rows
- memory records
- source quality breakdown

5. Archetype coverage
- C01-C36 profile coverage
- source gaps
- URL-backed fixture counts
- ontology-only counts

6. Leakage audit
- forbidden future leakage count
- source_proxy_to_score count
- result

7. Planner replay
- C06/C08/C15/C17/C24/C28 결과
- 전 아키타입 요약

8. Discovery dry run
- candidate count
- sector coverage
- top sample outputs
- official/general source ratio

9. Evidence OS regression
- Evidence OS v2 still READY인지
- score/orphan/legacy/source_proxy regression 여부

10. Production verdict
- READY / NOT_READY
- blocker
- 다음 단계

================================================================================
28. 금지사항
================================================================================

- Research Brain이 score 직접 출력 금지
- Research Brain이 Stage 직접 출력 금지
- source_proxy_only를 production score로 승격 금지
- evidence_url_pending을 production fixture로 승격 금지
- 과거 MFE/MAE를 current extraction prompt에 제공 금지
- 특정 종목명 하드코딩 금지
- 특정 research file만 처리하고 전체 inventory 생략 금지
- C06/C08만 통과하고 전 아키타입 matrix 생략 금지
- targeted smoke만 돌리고 discovery dry run 생략 금지
- general web/Naver를 기본 source로 사용 금지
- SourceTask budget 없는 fetch 금지
- 점수/Stage threshold 변경 금지
- Evidence OS v2 acceptance 깨뜨리기 금지
- 테스트 일부 통과를 Goal 완료라고 말하기 금지

================================================================================
29. 한 줄 목표
================================================================================

Research Brain v1의 목적은 다음이다.

과거 연구를 “점수 정답지”로 쓰는 것이 아니라,
현재 후보를 조사할 때 필요한 판례 기억으로 바꾸는 것이다.

즉:

과거 연구 MD/output/reports
→ ResearchMemoryRecord
→ ArchetypeMemoryProfile
→ CandidateEvent hypothesis
→ investigation plan
→ bounded SourceTask
→ Evidence OS accepted claim
→ deterministic score/stage

이 경로를 완성하라.