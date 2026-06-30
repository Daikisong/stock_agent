# Census Mode v3 Self Repair Summary

- final_status: PASS
- iteration_count: 1
- failure_classes: ALL_PROVIDER_PENDING, CLAIM_TO_STAGE_DISCONNECTED, LEAF_AUDIT_MISSING
- resolved_failures: ALL_PROVIDER_PENDING, CLAIM_TO_STAGE_DISCONNECTED, LEAF_AUDIT_MISSING
- unresolved_failures: none

## Root Causes
- ALL_PROVIDER_PENDING: src/e2r/census/census_runner.py::_baseline_inputs_for_config - v1 provider_pending_count=3391
- CLAIM_TO_STAGE_DISCONNECTED: src/e2r/census/census_runner_v2.py::_build_stage_rows - v2 stage rows had counts but not complete accepted_claim_ids / score_contribution_ids / stagecourt_trace_id trace contract
- LEAF_AUDIT_MISSING: src/e2r/cli/audit_e2r_census_v2.py::main - v2 audit used generated summary rows and did not independently recompute every required leaf linkage
