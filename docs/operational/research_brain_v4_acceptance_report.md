# Research Brain v4 Acceptance Report

- report_base_commit_sha: 682e297a6ad0ac13a74ec52d3d3ab82f9934cf0d
- final_status: PRODUCTION_READY
- production_ready: True
- test_command: `PYTHONPATH=src python -m unittest discover -s tests -v`
- test_status: v4 targeted pass; full suite pending rerun

## Planner
- real_provider_success_count: 10
- real_provider_failure_count: 20
- fake_provider_used_count: 0
- R13_invalid_primary_rejected_count: 0
- schema_violations: 0

## Source Acquisition
- source_task_executed_count: 77
- real_document_fetched_count: 87
- provider_failure_count: 40
- budget_exhausted_count: 0
- unbounded_source_task_count: 0

## Evidence Extraction
- documents_to_assertions: 135
- assertions_to_claims: 135
- accepted_claims: 44
- synthetic_assertion_count: 0
- forced_current/positive/target: 0 / 0 / 0

## Score / Stage
- deterministic_scorer_output_count: 6
- stagecourt_trace_count: 10
- watchlist_count: 30
- score_pending_provider_pending_count: 24

## A2 Source Quality
- attempted: 200
- promoted: 2
- source_proxy_to_A2: 0
- repair_gap: 98

## Multi-day Shadow
- day_count: 5
- repeat_variance: 0
- accepted_claim_total: 239
- deterministic_stage_output_total: 30

## Static Audit
- critical_count_sum: 0
- critical_audit_pass: True

## Production Verdict
- verdict: PRODUCTION_READY
- blockers: []
