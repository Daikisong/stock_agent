# Research Brain v1 Acceptance Report

## 1. Commit

- commit_sha: d4cce0bb13af4b28ded9b449d1c3406e182d9604 (implementation/report commit; final metadata commit SHA is reported in the chat response)
- commit_message: Research Brain v1 운영 두뇌 계층 구현
- push_status: pushed to origin/main
- working_tree_status: clean after final verification

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

- scanned_file_count: 22474
- parsed_artifact_count: 22474
- parsed_row_count: 119362
- parse_error_count: 0
- duplicate_count: 3684
- source_proxy_count: 74126
- evidence_url_pending_count: 63009
- url_backed_count: 11968
- production_fixture_count: 2922

## 5. Memory store

- memory_record_count: 308317
- memory_type_counts: `{"4b_watch_condition": 34315, "4c_thesis_break_condition": 21311, "counterexample": 4448, "evidence_contract_candidate": 848, "false_positive_pattern": 4448, "green_blocker": 8343, "hard_break_pattern": 21311, "ontology_only_rule_candidate": 21986, "primitive_failure_case": 10347, "primitive_partial_case": 2, "primitive_success_case": 35689, "production_fixture_candidate": 1461, "query_success_pattern": 48119, "replay_fixture_candidate": 1461, "score_weight_support": 19285, "source_family_reliability": 28412, "source_gap": 9990, "source_route_pattern": 28412, "stage2_watch_cap": 8129}`
- source_quality_class_counts: `{"A_URL_BACKED_REPLAY_READY": 11968, "B_URL_BACKED_REPAIR_NEEDED": 16986, "C_SOURCE_PROXY_ONTOLOGY_ONLY": 136321, "D_PRICE_PATH_ONLY_OR_FUTURE_LEAKAGE_RISK": 118221, "E_INVALID_OR_DUPLICATE": 24821}`
- usage_policy_counts: `{"allowed_for_evidence_extraction_prompt": 0, "allowed_for_ontology": 283496, "allowed_for_query_planning": 165275, "allowed_for_red_team_planning": 283496, "allowed_for_replay_fixture": 11968, "allowed_for_runtime_planning": 283496, "allowed_for_score_contribution": 0}`
- idempotency result: frozen_import_duplicate_growth_count=0

## 6. Archetype matrix

- C01-C36 profile coverage: 36/36
- ready_profile_count: 31
- planning_only_profile_count: 5
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
- official/general source ratio: 1.0 / 0.5
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
