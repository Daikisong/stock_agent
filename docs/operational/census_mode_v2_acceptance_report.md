# Census Mode v2 Acceptance Report

1. Final status: CENSUS_V1_RECLASSIFIED, BASELINE_SOURCE_WIRED_PASS, SOURCE_TIMELINE_PASS, LAST_EFFECTIVE_THESIS_PASS, CENSUS_LIGHT_PASS, CENSUS_SELECTIVE_DEEP_PASS, FULL_UNIVERSE_STAGE_MAP_PASS, SELF_REPAIR_LOOP_PASS, CENSUS_STATIC_AUDIT_PASS
2. Commit SHA at report generation: 8010e3f7c27b5a214706b809c1354e08f654364d
3. Test command: PYTHONPATH=src python -m unittest discover -s tests -v
   Test result: 4787 tests passed in 93.291s
4. Universe coverage: raw=3940, eligible=3391
5. output_root: output/census_v2/2026-07-01
6. hashes: config=ddac6ca5851f4479ccb42272a35764c39f8e86f414a483206430eb3bc54df36b, source=5bc00ed6e847327fe0bf560974c8e0e396df90d0842b4dc266b2a159c314b58f, candidate=1e780772b9498c6da13a07f929da59c1455fb4e714ca15ebf61ed2e0879da728, scoring=e2r-deterministic-scorer-v2, stage=e2r-stage-court-v2
7. Stage distribution: {'Stage0': 3306, 'Stage1': 47, 'Stage2-Watch': 37, 'Red': 1}
8. Status distribution: {'SCANNED': 3306, 'DEEP_VERIFIED': 74, 'LIGHT_ONLY': 3, 'PENDING_SOURCE': 8}
9. Accepted claim count: 92
10. Score contribution count: 92
11. Source task count: 141
12. Provider pending rate: 0.0
13. Unknown count: 0
14. Static audit critical counts: {'eligible_symbol_missing_stage_status_count': 0, 'duplicate_symbol_stage_status_count': 0, 'census_assessment_event_to_score_count': 0, 'no_claim_nonzero_score_count': 0, 'source_proxy_to_score_count': 0, 'evidence_url_pending_to_score_count': 0, 'price_path_only_to_score_count': 0, 'market_anomaly_to_score_count': 0, 'news_snippet_to_score_count': 0, 'provider_failed_final_score_count': 0, 'old_risk_without_current_open_to_score_count': 0, 'stale_claim_reused_current_count': 0, 'cheap_scan_score_as_verified_score_count': 0, 'research_brain_stage_direct_output_count': 0, 'research_brain_score_direct_output_count': 0, 'stage_without_confidence_count': 0, 'no_current_event_marked_red_count': 0, 'source_pending_marked_red_count': 0, 'unbounded_fetch_config_count': 0, 'checkpoint_missing_hash_count': 0, 'shard_merge_duplicate_count': 0, 'report_head_sha_mismatch_count': 0, 'one_line_large_report_count': 0, 'unknown_stage_status_count': 0, 'provider_pending_rate_over_30pct_count': 0, 'status_bucket_lt_4_count': 0, 'base_stage_bucket_lt_3_count': 0, 'accepted_claim_total_zero_count': 0, 'score_contribution_total_zero_count': 0, 'source_task_total_zero_count': 0, 'all_stage0_or_provider_pending_count': 0}
15. Readiness verdict: FULL_UNIVERSE_STAGE_MAP_PASS
16. Runtime seconds: 0.67
17. Baseline source family counts: {'IR': 3, 'ReportRadar': 14, 'CompanyGuide': 9, 'TrustedNews': 1, 'KRXPrice': 12}

쉬운 예: 전 종목은 출석체크를 받았지만, 점수는 accepted claim이 있는 종목만 받았다.
