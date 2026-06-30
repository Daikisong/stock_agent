# E2R Production Cutover Gate v3 Acceptance

- labels: IMPLEMENTATION_MERGED, PROVIDER_COMPLETENESS_PASS, MULTIDAY_SHADOW_PASS, CLAIM_EXTRACTOR_AUDIT_PASS, MEANINGFUL_STAGE_SPLIT_PASS, TRIGGER_POLICY_ENFORCED, OPERATOR_DIGEST_PASS, SLA_PASS, CUTOVER_READY, READY_FOR_CENSUS_DESIGN
- production_verdict: CUTOVER_READY
- production_ready: False
- static critical count: 0

v3는 Census Mode를 구현하지 않고, provider/multiday/stage cutover gate만 닫는다.

## Reproducibility Metadata

- git_head_sha: 997fe133d15633e4c92a15a30ec0c9c4d8a55c87
- report_base_commit_sha: 997fe133d15633e4c92a15a30ec0c9c4d8a55c87
- command: PYTHONPATH=src python -m e2r.cli.run_e2r_production_cutover_v3 --as-of-date 2026-06-30 --planner-provider real --candidate-min-count 20 --live-shadow-days 5 --output-root output/production_cutover_v3
- config_hash: ee67f63b718b78ecbc50a33d8ebcfda8a50fff1bdef7387059c2081cdc5168e7
- source_corpus_hash: f74422c923ae8dcf648f9f89cd7d2e766307d3f210a4cfc5a98d6ab556367f15
- candidate_event_hash: f532eced9d196b97b2d7a115d3087d327dfdffdd4df24e9af370843420e01059
- planner_prompt_hash: 28531e409e7ffcaea0c3755e8989ebf23aabba59b88b45f8f3cb426fa93b53bc
- planner_response_hash: 544414260302e1f0052db1b740ce7308e809084e31b220a9cfc8d0086010e093
- evidence_os_schema_version: e2r-agentic-evidence-os-v2
- scoring_schema_version: e2r-deterministic-scorer-v2
- stage_schema_version: e2r-stage-court-v2
