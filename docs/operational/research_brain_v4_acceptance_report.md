# Research Brain v4 Acceptance Report

- report_base_commit_sha: 1cb0783858e8ae6bb90938d276bae87b7e175a2d
- final_status: PRODUCTION_READY
- production_ready: True
- test_command: `PYTHONPATH=src python -m unittest discover -s tests -v`
- test_status: full suite pass, 4619 tests OK after structured extraction patch

## Planner
- real_provider_success_count: 30
- real_provider_failure_count: 0
- fake_provider_used_count: 0
- R13_invalid_primary_rejected_count: 0
- schema_violations: 0

## Source Acquisition
- source_task_executed_count: 257
- real_document_fetched_count: 255
- provider_failure_count: 119
- budget_exhausted_count: 0
- unbounded_source_task_count: 0

## Evidence Extraction
- documents_to_assertions: 533
- assertions_to_claims: 533
- accepted_claims: 56
- synthetic_assertion_count: 0
- forced_current/positive/target: 0 / 0 / 0

## Score / Stage
- deterministic_scorer_output_count: 5
- stagecourt_trace_count: 30
- watchlist_count: 30
- score_pending_provider_pending_count: 25

## A2 Source Quality
- attempted: 200
- promoted: 0
- source_proxy_to_A2: 0
- repair_gap: 100

## Multi-day Shadow
- day_count: 5
- repeat_variance: 0
- accepted_claim_total: 390
- deterministic_stage_output_total: 29

## Static Audit
- critical_count_sum: 0
- critical_audit_pass: True

## Production Verdict
- verdict: PRODUCTION_READY
- blockers: []
