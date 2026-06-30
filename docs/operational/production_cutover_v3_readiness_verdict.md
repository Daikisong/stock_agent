# E2R Production Cutover Gate v3 Verdict

- production_verdict: CUTOVER_READY
- labels: IMPLEMENTATION_MERGED, PROVIDER_COMPLETENESS_PASS, MULTIDAY_SHADOW_PASS, CLAIM_EXTRACTOR_AUDIT_PASS, MEANINGFUL_STAGE_SPLIT_PASS, TRIGGER_POLICY_ENFORCED, OPERATOR_DIGEST_PASS, SLA_PASS, CUTOVER_READY, READY_FOR_CENSUS_DESIGN
- static_critical_count_sum: 0
- blockers: []

쉬운 예: provider와 multiday가 통과해도 사용자 승인 플래그가 없으면 PRODUCTION_READY가 아니라 CUTOVER_READY까지만 간다.

## Reproducibility Metadata

- git_head_sha: bee2fee72c586cffeb122e8a8f9f0d50a9c2c27b
- report_base_commit_sha: bee2fee72c586cffeb122e8a8f9f0d50a9c2c27b
- command: PYTHONPATH=src python -m e2r.cli.run_e2r_production_cutover_v3 --as-of-date 2026-06-30 --planner-provider real --candidate-min-count 20 --live-shadow-days 5 --frozen-replay-days 10 --repeated-frozen-days 3 --output-root output/production_cutover_v3 --validation-output-root output/production_cutover_v3 --docs-dir docs/operational --repo-root . --fetch-a2-live true --run-llm-extractor false --a2-fetch-limit-per-arch 80 --llm-extractor-document-limit 50 --final-cutover-approved false --fail-on-critical-audit true
- config_hash: ee67f63b718b78ecbc50a33d8ebcfda8a50fff1bdef7387059c2081cdc5168e7
- source_corpus_hash: 7e50e842d128bb49a78cab3f9cbe753fed2e42705642d21b106fc4364a985651
- candidate_event_hash: f532eced9d196b97b2d7a115d3087d327dfdffdd4df24e9af370843420e01059
- planner_prompt_hash: 28531e409e7ffcaea0c3755e8989ebf23aabba59b88b45f8f3cb426fa93b53bc
- planner_response_hash: 0f08fbb35b982095d2d8b23516467bdda3f26030cd0cb1b334e2d19c215a1eb9
- evidence_os_schema_version: e2r-agentic-evidence-os-v2
- scoring_schema_version: e2r-deterministic-scorer-v2
- stage_schema_version: e2r-stage-court-v2
