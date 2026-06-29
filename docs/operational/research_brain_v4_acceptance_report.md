# Research Brain v4 Acceptance Report

- report_base_commit_sha: 974ba62ca6943f47370a2bec82c147ca45b54cc5
- final_status: DAILY_WATCHLIST_PASS
- production_ready: False
- test_command: `PYTHONPATH=src python -m unittest discover -s tests -v`
- test_status: full suite pass, 4618 tests OK

## Planner
- real_provider_success_count: 30
- real_provider_failure_count: 0
- fake_provider_used_count: 0
- R13_invalid_primary_rejected_count: 0
- schema_violations: 0

## Source Acquisition
- source_task_executed_count: 237
- real_document_fetched_count: 230
- provider_failure_count: 124
- budget_exhausted_count: 0
- unbounded_source_task_count: 0

## Evidence Extraction
- documents_to_assertions: 519
- assertions_to_claims: 519
- accepted_claims: 85
- synthetic_assertion_count: 0
- forced_current/positive/target: 0 / 0 / 0

## Score / Stage
- deterministic_scorer_output_count: 6
- stagecourt_trace_count: 30
- watchlist_count: 30
- score_pending_provider_pending_count: 24

## A2 Source Quality
- attempted: 200
- promoted: 0
- source_proxy_to_A2: 0
- repair_gap: 100

## Multi-day Shadow
- day_count: 5
- repeat_variance: 2
- accepted_claim_total: 337
- deterministic_stage_output_total: 28

## Static Audit
- critical_count_sum: 0
- critical_audit_pass: True

## Production Verdict
- verdict: DAILY_WATCHLIST_PASS
- blockers: ['repeated frozen run variance is not zero']
