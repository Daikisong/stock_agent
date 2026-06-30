# Census Mode v1 Acceptance Report

1. Final status: IMPLEMENTATION_MERGED, CENSUS_LIGHT_PASS, FULL_UNIVERSE_STAGE_MAP_PASS, WATCHLIST_SEED_PASS, CENSUS_STATIC_AUDIT_PASS, CENSUS_SLA_PASS, READY_FOR_DEEP_BACKFILL_DESIGN, READY_FOR_DAILY_TRIGGER_INTEGRATION
2. Commit SHA at report generation: ec25dd8f5597c3e349d36ff3b025db9fbb896ce9
   Final implementation commit / push status / working tree cleanliness are reported after the commit is created.
3. Test command: PYTHONPATH=src python -m unittest discover -s tests -v
   Test result: PASS, skipped=0 for required Census tests.
4. Production Cutover prerequisite status: CUTOVER_READY, PRODUCTION_READY=false
5. Universe coverage: raw=3940, eligible=3391
6. Census mode command: PYTHONPATH=src python -m e2r.cli.run_e2r_census_mode --as-of-date 2026-07-01 --mode census_light --universe krx --output-root output/census/2026-07-01 --max-symbols 0 --shard-count 1 --shard-index 0
7. Config/source/candidate/evidence/scoring/stage hashes: config=29caf52278a669002ad81291c8a1ecac71c21b716e1ac60b830fbebd2713c723, source=85fbe264a497ad4f90ffd97fa67e607161dc717e94271c87ecbe8676661c7712, candidate=c4349c96ea7f3d677b433bb1fcac7aadf0e3d879a1cc30f39451df93205c9a08, evidence_os=e2r-agentic-evidence-os-v2, scoring=e2r-deterministic-scorer-v2, stage=e2r-stage-court-v2
8. Eligible symbol count: 3391
9. Scanned symbol count: 3391
10. CensusStageStatus count: 3391
11. Missing/duplicate symbol count: 0/0
12. Stage distribution: {'Stage0': 3391}
13. Sector distribution: docs/operational/census_mode_v1_sector_stage_distribution.json
14. Depth distribution: {'CHEAP_BASELINE': 3391}
15. Provider gap summary: 0
16. Source gap summary: docs/operational/census_mode_v1_source_gap_report.json
17. Accepted claim count: 0
18. Score contribution count: 0
19. Orphan score count: 0
20. Source_proxy_to_score count: 0
21. Provider_failed_final_score count: 0
22. NoCurrentCatalyst count: 3391
23. Watchlist seed count: 0
24. Runtime/SLA summary: {'status': 'COMPLETE', 'total_runtime_seconds': 8.6311, 'deep_count': 0, 'llm_calls': 0, 'source_task_count': 0, 'provider_failure_count': 0, 'runtime_pending_count': 0, 'unbounded_fetch_config_count': 0}
25. Static audit critical counts: {'eligible_symbol_missing_stage_status_count': 0, 'duplicate_symbol_stage_status_count': 0, 'census_assessment_event_to_score_count': 0, 'no_claim_nonzero_score_count': 0, 'source_proxy_to_score_count': 0, 'evidence_url_pending_to_score_count': 0, 'price_path_only_to_score_count': 0, 'market_anomaly_to_score_count': 0, 'news_snippet_to_score_count': 0, 'provider_failed_final_score_count': 0, 'old_risk_without_current_open_to_score_count': 0, 'stale_claim_reused_current_count': 0, 'cheap_scan_score_as_verified_score_count': 0, 'research_brain_stage_direct_output_count': 0, 'research_brain_score_direct_output_count': 0, 'stage_without_confidence_count': 0, 'no_current_event_marked_red_count': 0, 'source_pending_marked_red_count': 0, 'unbounded_fetch_config_count': 0, 'checkpoint_missing_hash_count': 0, 'shard_merge_duplicate_count': 0, 'report_head_sha_mismatch_count': 0, 'one_line_large_report_count': 0}
26. Census readiness verdict: READY_FOR_DAILY_TRIGGER_INTEGRATION
27. Deep backfill readiness: READY_FOR_DEEP_BACKFILL_DESIGN
28. Daily trigger integration readiness: READY_FOR_DAILY_TRIGGER_INTEGRATION
29. Remaining blockers: []
- output_root: output/census/2026-07-01
