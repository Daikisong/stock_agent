# E2R Production Cutover Acceptance Report

- final_status: DAILY_PRODUCTION_SHADOW_PASS
- production_verdict: NOT_READY
- production_ready: False
- blockers: ['A2 real replay verified count is 0; explicit source/provider gap keeps cutover NOT_READY']

## 핵심 해석
v4는 shadow 실행 증거로 보존하지만, 이 cutover gate는 fixture/cache/snapshot-only 증거를 운영 READY 증거로 승격하지 않는다.

쉬운 예: 복사본 서류로 예행연습은 통과할 수 있지만, 실제 창구 제출용 원본 서류로 보지는 않는다.

## Counts

### candidate

```json
{
  "active_large_sector_count": 9,
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
  "sector_coverage": {
    "active": {
      "L1_INDUSTRIALS_INFRA_DEFENSE_GRID": {
        "candidate_attempt_count": 10,
        "classification_sources": [
          "OpenDART company.json induty_code"
        ],
        "production_eligible_candidate_count": 10,
        "sample_symbols": [
          "060900",
          "130660",
          "270520",
          "351320",
          "130660",
          "417840",
          "037350",
          "060900",
          "378340",
          "282720"
        ],
        "source_gap": null
      },
      "L2_AI_SEMICONDUCTOR_ELECTRONICS": {
        "candidate_attempt_count": 4,
        "classification_sources": [
          "OpenDART company.json induty_code"
        ],
        "production_eligible_candidate_count": 4,
        "sample_symbols": [
          "148250",
          "260870",
          "360070",
          "248070"
        ],
        "source_gap": null
      },
      "L3_BATTERY_EV_GREEN_MOBILITY": {
        "candidate_attempt_count": 4,
        "classification_sources": [
          "OpenDART company.json induty_code"
        ],
        "production_eligible_candidate_count": 4,
        "sample_symbols": [
          "381970",
          "104040",
          "028670",
          "403550"
        ],
        "source_gap": null
      },
      "L4_MATERIALS_SPREAD_RESOURCE": {
        "candidate_attempt_count": 7,
        "classification_sources": [
          "OpenDART company.json induty_code"
        ],
        "production_eligible_candidate_count": 7,
        "sample_symbols": [
          "083660",
          "083660",
          "175250",
          "007460",
          "216080",
          "216080",
          "357550"
        ],
        "source_gap": null
      },
      "L5_CONSUMER_BRAND_DISTRIBUTION": {
        "candidate_attempt_count": 2,
        "classification_sources": [
          "OpenDART company.json induty_code"
        ],
        "production_eligible_candidate_count": 2,
        "sample_symbols": [
          "368970",
          "063170"
        ],
        "source_gap": null
      },
      "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL": {
        "candidate_attempt_count": 8,
        "classification_sources": [
          "OpenDART company.json induty_code"
        ],
        "production_eligible_candidate_count": 8,
        "sample_symbols": [
          "021960",
          "003530",
          "003380",
          "003530",
          "003530",
          "003530",
          "003540",
          "003540"
        ],
        "source_gap": null
      },
      "L7_BIO_HEALTHCARE_MEDICAL": {
        "candidate_attempt_count": 3,
        "classification_sources": [
          "OpenDART company.json induty_code"
        ],
        "production_eligible_candidate_count": 3,
        "sample_symbols": [
          "226950",
          "226950",
          "226950"
        ],
        "source_gap": null
      },
      "L8_PLATFORM_CONTENT_SW_SECURITY": {
        "candidate_attempt_count": 9,
        "classification_sources": [
          "OpenDART company.json induty_code"
        ],
        "production_eligible_candidate_count": 9,
        "sample_symbols": [
          "208640",
          "377030",
          "377030",
          "347700",
          "347700",
          "347700",
          "208640",
          "208640",
          "440320"
        ],
        "source_gap": null
      },
      "L9_CONSTRUCTION_REALESTATE_HOUSING": {
        "candidate_attempt_count": 3,
        "classification_sources": [
          "OpenDART company.json induty_code"
        ],
        "production_eligible_candidate_count": 3,
        "sample_symbols": [
          "006050",
          "006050",
          "097230"
        ],
        "source_gap": null
      }
    },
    "inactive": {
      "L10_POLICY_EVENT_CROSS_REDTEAM_MISC": {
        "candidate_attempt_count": 0,
        "classification_sources": [],
        "production_eligible_candidate_count": 0,
        "sample_symbols": [],
        "source_gap": "no_candidate_attempt_in_current_daily_scan"
      }
    },
    "summary": {
      "active_large_sector_count": 9,
      "inactive_large_sector_count": 1,
      "large_sector_total": 10,
      "unknown_sector_candidate_count": 0
    }
  },
  "snapshot_uri_source_count": 0,
  "symbol_not_in_registry_count": 0,
  "total_candidate_event_count": 50,
  "unknown_sector_candidate_count": 0
}
```

### planner

```json
{
  "endpoints": {
    "codex-cli": 50
  },
  "fake_frozen_provider_used_count": 0,
  "planner_default_model_unpinned_count": 0,
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
  "companyguide_call_count": 3,
  "dart_call_count": 53,
  "fetched_document_count": 50,
  "issuer_ir_call_count": 3,
  "kind_call_count": 3,
  "krx_call_count": 3,
  "live_or_fresh_provider_document_count": 50,
  "provider_call_counts": {
    "CompanyGuide": 3,
    "IssuerIR": 3,
    "KIND": 3,
    "KRX": 3,
    "OpenDART": 53,
    "TrustedNews": 3
  },
  "provider_failure_count": 18,
  "provider_failure_counts": {
    "CompanyGuide": 3,
    "IssuerIR": 3,
    "KIND": 3,
    "KRX": 3,
    "OpenDART": 3,
    "TrustedNews": 3
  },
  "real_document_fetched_count": 50,
  "real_source_document_fetched_count": 50,
  "snapshot_only_counted_as_live_count": 0,
  "snapshot_only_document_count": 0,
  "source_gaps": {
    "CompanyGuide": "connector exercised; local live implementation currently returns explicit PROVIDER_FAILED",
    "IR": "connector exercised; local live implementation currently returns explicit PROVIDER_FAILED",
    "KIND": "connector exercised; local live implementation currently returns explicit PROVIDER_FAILED",
    "KRX": "connector exercised; OpenDART corpCode/company APIs supplied universe and industry coverage for this run",
    "TrustedNews": "connector exercised; local live implementation currently returns explicit PROVIDER_FAILED"
  },
  "source_task_accepted_without_provider_fetch_count": 0,
  "stored_snapshot_only_documents": 0,
  "trusted_news_call_count": 3
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
