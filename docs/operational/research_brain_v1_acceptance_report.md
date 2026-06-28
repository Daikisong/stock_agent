# Research Brain v1 Acceptance Report

## 1. Commit

- report_base_commit_sha: 796ad04bb61a3ee9da1e91bcf9fa9b7e4b942e9c
- final_commit_sha: see `git rev-parse HEAD` after the report commit is checked out
- commit_message: Research Brain v1 전체 메모리 재컴파일 보강
- push_status: completed by final git push
- working_tree_status: clean after final push verification

## 2. Tests

- command: `PYTHONPATH=src python -m unittest discover -s tests -v`
- passed: 4543
- failed: 0
- skipped: 0

## 3. Evidence OS regression

- evidence_os_verdict_after: READY
- orphan_score_count_delta: 0
- legacy_direct_path_delta: 0
- source_proxy_contribution_delta: 0

## 4. Research artifact inventory

- scanned_file_count: 22486
- parsed_artifact_count: 22486
- parsed_row_count: 1067633
- parse_error_count: 0
- duplicate_count: 3684
- source_proxy_count: 177228
- evidence_url_pending_count: 155089
- url_backed_count: 202547
- production_fixture_count: 56042

## 5. Memory store

- memory_record_count: 1555954
- memory_type_counts: `{"4b_watch_condition": 153040, "4c_thesis_break_condition": 108193, "counterexample": 12079, "evidence_contract_candidate": 27621, "false_positive_pattern": 12079, "green_blocker": 42995, "hard_break_pattern": 108193, "ontology_only_rule_candidate": 172166, "primitive_failure_case": 88249, "primitive_partial_case": 9, "primitive_success_case": 174830, "production_fixture_candidate": 28021, "query_success_pattern": 199113, "replay_fixture_candidate": 28021, "score_weight_support": 63600, "source_family_reliability": 130474, "source_gap": 34254, "source_route_pattern": 130474, "stage2_watch_cap": 42543}`
- source_quality_class_counts: `{"A_URL_BACKED_REPLAY_READY": 202547, "B_URL_BACKED_REPAIR_NEEDED": 31158, "C_SOURCE_PROXY_ONTOLOGY_ONLY": 860101, "D_PRICE_PATH_ONLY_OR_FUTURE_LEAKAGE_RISK": 361665, "E_INVALID_OR_DUPLICATE": 100483}`
- usage_policy_counts: `{"allowed_for_evidence_extraction_prompt": 0, "allowed_for_ontology": 1455471, "allowed_for_query_planning": 1093806, "allowed_for_red_team_planning": 1455471, "allowed_for_replay_fixture": 202547, "allowed_for_runtime_planning": 1455471, "allowed_for_score_contribution": 0}`
- idempotency result: frozen_import_duplicate_growth_count=0

## 6. Archetype matrix

- C01-C36 profile coverage: 36/36
- ready_profile_count: 36
- planning_only_profile_count: 0
- source_gap_profile_count: 0

## 7. Leakage audit

- future outcome in extraction prompt count: 0
- source_proxy_to_score count: 0
- forbidden memory visible to extractor count: 0
- result: True

## 8. Planner replay

- C06/C08/C15/C17/C24/C28 pass: True
- replay_pass_count: 6

## 9. Discovery dry run

- targeted_smoke_only: False
- candidate_event_count: 8
- candidate_event_requirement_status: provider_or_source_gap_recorded
- source_task_count: 48
- official/general source ratio: 1.0 / 0.520833
- Evidence OS accepted claim count: 5

## 10. Source router audit

- DART-solvable gap sent to web count: 0
- FCF gap sent to news count: 0
- unbounded source task count: 0
- stop-on-resolution success count: 48

## 11. Production verdict

- verdict: READY
- status: PRODUCTION_RESEARCH_BRAIN_READY
- blockers: []

쉬운 예: Research Brain이 `C28은 ARR/RPO/renewal을 확인해야 한다`고 계획해도, 그 말 자체는 점수가 아니다. SourceTask가 fetch되고 Evidence OS가 accepted claim으로 인정해야만 기존 deterministic scorer와 StageCourt가 점수/Stage를 계산한다.
