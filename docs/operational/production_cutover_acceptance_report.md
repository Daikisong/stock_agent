# E2R Production Cutover Acceptance Report

- final_status: DAILY_PRODUCTION_SHADOW_PASS
- production_verdict: NOT_READY
- production_ready: False
- blockers: ['working tree dirty at report generation, so PRODUCTION_CUTOVER_READY is forbidden', 'multi-day validation below 10 frozen/live-equivalent days', 'five live official dry runs not completed']

## 핵심 해석
v4는 shadow 실행 증거로 보존하지만, 이 cutover gate는 fixture/cache/snapshot-only 증거를 운영 READY 증거로 승격하지 않는다.

쉬운 예: 복사본 서류로 예행연습은 통과할 수 있지만, 실제 창구 제출용 원본 서류로 보지는 않는다.

## Counts

### candidate

```json
{
  "actual_krx_universe_count": 3972,
  "cached_fixture_source_count": 0,
  "cached_path_count": 0,
  "combined_registry_count": 3972,
  "company_name_mismatch_count": 0,
  "fixture_candidate_event_count": 0,
  "fixture_candidate_event_count_in_production": 0,
  "mode": "production_shadow_live",
  "production_candidate_event_count": 50,
  "production_eligible_candidate_event_count": 50,
  "sector_coverage": {},
  "snapshot_uri_source_count": 0,
  "symbol_not_in_registry_count": 0,
  "total_candidate_event_count": 50
}
```

### planner

```json
{
  "endpoints": {
    "codex-cli": 50
  },
  "fake_frozen_provider_used_count": 0,
  "planner_output_score_stage_key_count": 0,
  "planner_prompt_hash_count": 50,
  "planner_provider_model_null_count": 0,
  "planner_response_hash_count": 50,
  "planner_response_missing_hash_count": 0,
  "planner_run_count": 50,
  "planner_schema_reject_count": 0,
  "raw_prompt_response_file_missing_count": 0,
  "real_planner_success_count": 50,
  "real_provider_names": {
    "codex_cli_planner": 50
  }
}
```

### source

```json
{
  "companyguide_call_count": 0,
  "dart_call_count": 50,
  "fetched_document_count": 50,
  "issuer_ir_call_count": 0,
  "kind_call_count": 0,
  "krx_call_count": 0,
  "live_or_fresh_provider_document_count": 50,
  "provider_call_counts": {
    "OpenDART": 50
  },
  "provider_failure_count": 0,
  "provider_failure_counts": {},
  "real_document_fetched_count": 50,
  "real_source_document_fetched_count": 50,
  "snapshot_only_counted_as_live_count": 0,
  "snapshot_only_document_count": 0,
  "source_gaps": {
    "CompanyGuide": "not required for DART disclosure event verification",
    "IR": "follow-up source class, not primary for DART disclosure verification",
    "KIND": "not required for OpenDART disclosure-based daily shadow",
    "KRX": "OpenDART corpCode stock_code universe used as official listed universe for this shadow run"
  },
  "source_task_accepted_without_provider_fetch_count": 0,
  "stored_snapshot_only_documents": 0,
  "trusted_news_call_count": 0
}
```

### extraction

```json
{
  "accepted_claim_count": 50,
  "accepted_claim_without_anchor_count": 0,
  "assertion_to_claim_count": 50,
  "contract_visible_to_raw_extractor_count": 0,
  "event_summary_used_as_exact_quote_count": 0,
  "forced_current_temporal_count": 0,
  "forced_positive_polarity_count": 0,
  "forced_target_subject_count": 0,
  "historical_only_rejected_count": 0,
  "primitive_gap_direct_to_mapping_count": 0,
  "real_document_to_assertion_count": 50,
  "source_field_existence_to_score_without_adjudication_count": 0,
  "wrong_subject_rejected_count": 0
}
```

### score_stage

```json
{
  "canonical_score_scale_max": 100,
  "canonical_score_scale_min": 0,
  "deterministic_scorer_configured_min_count": 15,
  "deterministic_scorer_output_count": 50,
  "pending_material_gap_count": 0,
  "pending_or_provider_count": 0,
  "provider_failed_final_score_count": 0,
  "provider_failed_score_count": 0,
  "score_contribution_count": 50,
  "score_without_claim_count": 0,
  "stagecourt_trace_count": 50,
  "watchlist_count": 50
}
```

## Test Summary

- latest full test command: `PYTHONPATH=src python -m unittest discover -s tests -v`
- latest full test result is recorded in `docs/operational/production_cutover_test_summary.json`.
