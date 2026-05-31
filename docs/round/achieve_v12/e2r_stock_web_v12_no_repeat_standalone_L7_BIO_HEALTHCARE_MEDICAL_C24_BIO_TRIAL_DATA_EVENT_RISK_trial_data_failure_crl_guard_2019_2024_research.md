# E2R V12 No-Repeat Standalone Residual Research
## R7 / L7 / C24 — Bio trial data event risk / CRL guard

metadata:
```text
selected_round: R7
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id: TRIAL_DATA_FAILURE_CRL_4C_GUARD
loop_objective: coverage_gap_fill|counterexample_mining|4B_4C_guard_validation|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_trial_data_failure_crl_guard_2019_2024_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C24_BIO_TRIAL_DATA_EVENT_RISK current coverage:
rows=39, symbols=14, date range=2019-08-02~2024-11-20, good/bad S2=15/2, 4B/4C=1/5
top covered symbols: 000100(6), 028300(5), 009420(4), 039200(4), UNKNOWN_SYMBOL(4)
```

This run avoids those top-covered C24 symbols and adds 215600, 084990, and 067630.  
Each row uses a new `C24 + symbol + trigger_type + entry_date` hard key.

## 2. Stock-Web source check

Manifest:
```text
source_name: FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14354401
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
```

Selected profiles:
```text
215600 신라젠: 2019 forward window clean; corporate-action candidates are 2022-10-13 and 2024-07-09.
084990 헬릭스미스: 2019-09-24 forward window starts after the 2019-09-05 corporate-action candidate; forward event window treated as usable with caveat.
067630 HLB생명과학: 2024 forward window clean; corporate-action candidates are old, outside the test window.
```

## 3. Research thesis

C24 is not a generic "bio bad news" bucket. It should detect the point where the asset-level bridge breaks:

```text
trial or regulatory catalyst
→ data readability / endpoint integrity / regulatory pathway
→ cash runway and resubmission scope
→ commercialization probability
→ valuation support
```

The guardrail is severe because a single-asset biotech does not fade like a normal cyclical stock. When the pivotal trial or regulatory pathway cracks, the floor is not inventory or margin; the floor is belief itself.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C24_215600_SILLAJEN_20190802_PEXAVEC_TRIAL_FUTILITY_HARD_4C | 215600 | hard_4c_protective_success | 2019-08-02 | 31200 | 31200 on 2019-08-02 | 7820 on 2019-09-30 | 0.0% | 0.0% | 0.0% | -74.94% | -74.94% |
| C24_084990_HELIXMITH_20190924_VM202_PHASE3_DATA_4C_WATCH | 084990 | trial_data_quality_counterexample | 2019-09-24 | 120000 | 120000 on 2019-09-24 | 56500 on 2020-03-19 | 0.0% | 0.0% | 0.0% | -52.92% | -52.92% |
| C24_067630_HLBBIO_20240517_RIVOCERANIB_CRL_GROUP_EVENT_FALSE_GREEN | 067630 | regulatory_complete_response_false_green_counterexample | 2024-05-17 | 10020 | 13500 on 2024-07-09 | 7700 on 2024-05-20 | 12.18% | 34.73% | 34.73% | -23.15% | -40.74% |

## 5. Stage evidence split

### Stage2 / Stage3
- Bio event attention alone is not positive evidence.
- After a pivotal data failure, data-quality issue, or CRL, the row must require non-price restoration: endpoint clarity, regulatory path, resubmission scope, and cash runway.

### 4B
- 067630 shows the rebound trap. A post-CRL group rebound can generate strong local MFE, but without resubmission clarity it should be local 4B/counterexample, not fresh Green.
- Technical rebound after a clinical shock is the market's echo, not proof that the asset bridge is repaired.

### 4C
- 215600 is the hard 4C anchor: pivotal-trial futility destroyed the investable bridge.
- 084990 is the data-quality 4C-watch example: trial ambiguity becomes a valuation problem when the market needed clean Phase 3 readability.
- 067630 is the regulatory-pathway example: CRL/review risk should stay Yellow/4C-watch until the company can show the path back to approval.

## 6. Raw component score breakdown

```json
{
  "C24_067630_HLBBIO_20240517_RIVOCERANIB_CRL_GROUP_EVENT_FALSE_GREEN": {
    "bottleneck_pricing_power": 3,
    "capital_allocation": 1,
    "eps_fcf_explosion": 2,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 17,
    "valuation_rerating_runway": 2,
    "visibility_quality": 2
  },
  "C24_084990_HELIXMITH_20190924_VM202_PHASE3_DATA_4C_WATCH": {
    "bottleneck_pricing_power": 2,
    "capital_allocation": 0,
    "eps_fcf_explosion": 1,
    "information_confidence": 4,
    "market_mispricing": 2,
    "total": 10,
    "valuation_rerating_runway": 0,
    "visibility_quality": 1
  },
  "C24_215600_SILLAJEN_20190802_PEXAVEC_TRIAL_FUTILITY_HARD_4C": {
    "bottleneck_pricing_power": 1,
    "capital_allocation": 0,
    "eps_fcf_explosion": 0,
    "information_confidence": 5,
    "market_mispricing": 1,
    "total": 7,
    "valuation_rerating_runway": 0,
    "visibility_quality": 0
  }
}
```

## 7. Current calibrated profile stress test

Suggested C24 guard:
```text
if pivotal_trial_failure_or_futility:
    stage = Stage4C-Hard
    block_stage2_green = true

if trial_data_quality_problem and single_asset_dependency_high:
    route_to_4C_watch = true
    require_data_readability_before_any_recovery_upgrade = true

if crl_or_regulatory_rejection and no resubmission_scope_or_cash_runway_clarity:
    cap_stage = Stage3-Yellow or 4C-watch
    route_post_event_rebound_to_local_4B = true
```

Residual errors:
```text
current_profile_error_count = 2
- 084990 / 2019-09-24: trial-data quality ambiguity can be under-penalized if the model treats it as ordinary volatility instead of asset-bridge damage.
- 067630 / 2024-05-17: post-CRL rebound can be over-promoted if resubmission pathway and cash runway are not required.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -74.94, "MAE_30D_pct": -71.15, "MAE_90D_pct": -74.94, "MFE_180D_pct": 0.0, "MFE_30D_pct": 0.0, "MFE_90D_pct": 0.0, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "case_id": "C24_215600_SILLAJEN_20190802_PEXAVEC_TRIAL_FUTILITY_HARD_4C", "case_role": "hard_4c_protective_success", "company_name": "신라젠", "corporate_action_window_status": "clean_entry_forward_window_or_candidate_outside_forward_window", "current_profile_error": false, "current_profile_verdict": "Hard 4C should activate when pivotal-trial futility or discontinuation destroys the core asset thesis; no fresh Stage2/Green should be allowed on technical rebound alone.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -74.94, "entry_date": "2019-08-02", "entry_price": 31200, "evidence_family": "pivotal_trial_futility_stop_bio_event_risk_hard_4c", "evidence_url_pending": false, "fine_archetype_id": "TRIAL_DATA_FAILURE_CRL_4C_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "low_date_180d": "2019-09-30", "low_price_180d": 7820, "peak_date": "2019-08-02", "peak_price": 31200, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/215/215600.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 1, "capital_allocation": 0, "eps_fcf_explosion": 0, "information_confidence": 5, "market_mispricing": 1, "total": 7, "valuation_rerating_runway": 0, "visibility_quality": 0}, "reuse_reason": null, "same_entry_group_id": "C24_215600_SILLAJEN_20190802_PEXAVEC_TRIAL_FUTILITY_HARD_4C", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R7", "source_proxy_only": false, "stage2_evidence_fields": ["bio_event_attention", "trial_or_regulatory_asset_dependency", "technical_rebound_or_event_premium"], "stage3_evidence_fields": ["clean_trial_data_required", "regulatory_pathway_clarity_required", "cash_runway_and_resubmission_scope_required"], "stage4b_evidence_fields": ["post_event_rebound_without_new_non_price_clarity", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["pivotal_trial_failure_or_futility", "trial_data_quality_break", "regulatory_crl_or_resubmission_uncertainty"], "symbol": "215600", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/215/215600/2019.csv", "trigger_date": "2019-08-02", "trigger_type": "Stage4C-Hard", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -52.92, "MAE_30D_pct": -46.33, "MAE_90D_pct": -46.33, "MFE_180D_pct": 0.0, "MFE_30D_pct": 0.0, "MFE_90D_pct": 0.0, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "case_id": "C24_084990_HELIXMITH_20190924_VM202_PHASE3_DATA_4C_WATCH", "case_role": "trial_data_quality_counterexample", "company_name": "헬릭스미스", "corporate_action_window_status": "clean_entry_forward_window_or_candidate_outside_forward_window", "current_profile_error": true, "current_profile_verdict": "Trial-data ambiguity should not be treated as a mild Yellow if the single-asset valuation depends on clean Phase 3 efficacy and regulatory readability.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -52.92, "entry_date": "2019-09-24", "entry_price": 120000, "evidence_family": "phase3_trial_data_quality_problem_without_clean_regulatory_bridge", "evidence_url_pending": false, "fine_archetype_id": "TRIAL_DATA_FAILURE_CRL_4C_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "low_date_180d": "2020-03-19", "low_price_180d": 56500, "peak_date": "2019-09-24", "peak_price": 120000, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/084/084990.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 2, "capital_allocation": 0, "eps_fcf_explosion": 1, "information_confidence": 4, "market_mispricing": 2, "total": 10, "valuation_rerating_runway": 0, "visibility_quality": 1}, "reuse_reason": null, "same_entry_group_id": "C24_084990_HELIXMITH_20190924_VM202_PHASE3_DATA_4C_WATCH", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R7", "source_proxy_only": false, "stage2_evidence_fields": ["bio_event_attention", "trial_or_regulatory_asset_dependency", "technical_rebound_or_event_premium"], "stage3_evidence_fields": ["clean_trial_data_required", "regulatory_pathway_clarity_required", "cash_runway_and_resubmission_scope_required"], "stage4b_evidence_fields": ["post_event_rebound_without_new_non_price_clarity", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["pivotal_trial_failure_or_futility", "trial_data_quality_break", "regulatory_crl_or_resubmission_uncertainty"], "symbol": "084990", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/084/084990/2019.csv", "trigger_date": "2019-09-24", "trigger_type": "Stage4C-Watch", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -23.15, "MAE_30D_pct": -23.15, "MAE_90D_pct": -23.15, "MFE_180D_pct": 34.73, "MFE_30D_pct": 12.18, "MFE_90D_pct": 34.73, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "case_id": "C24_067630_HLBBIO_20240517_RIVOCERANIB_CRL_GROUP_EVENT_FALSE_GREEN", "case_role": "regulatory_complete_response_false_green_counterexample", "company_name": "HLB생명과학", "corporate_action_window_status": "clean_entry_forward_window_or_candidate_outside_forward_window", "current_profile_error": true, "current_profile_verdict": "Post-CRL rebound should stay Yellow/local 4B unless resubmission pathway, deficiency resolution, trial/regulatory scope and cash runway are clear.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -40.74, "entry_date": "2024-05-17", "entry_price": 10020, "evidence_family": "crl_group_regulatory_event_rebound_without_resubmission_clarity", "evidence_url_pending": false, "fine_archetype_id": "TRIAL_DATA_FAILURE_CRL_4C_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "low_date_180d": "2024-05-20", "low_price_180d": 7700, "peak_date": "2024-07-09", "peak_price": 13500, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/067/067630.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 3, "capital_allocation": 1, "eps_fcf_explosion": 2, "information_confidence": 3, "market_mispricing": 4, "total": 17, "valuation_rerating_runway": 2, "visibility_quality": 2}, "reuse_reason": null, "same_entry_group_id": "C24_067630_HLBBIO_20240517_RIVOCERANIB_CRL_GROUP_EVENT_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R7", "source_proxy_only": false, "stage2_evidence_fields": ["bio_event_attention", "trial_or_regulatory_asset_dependency", "technical_rebound_or_event_premium"], "stage3_evidence_fields": ["clean_trial_data_required", "regulatory_pathway_clarity_required", "cash_runway_and_resubmission_scope_required"], "stage4b_evidence_fields": ["post_event_rebound_without_new_non_price_clarity", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["pivotal_trial_failure_or_futility", "trial_data_quality_break", "regulatory_crl_or_resubmission_uncertainty"], "symbol": "067630", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/067/067630/2024.csv", "trigger_date": "2024-05-17", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "TRIAL_DATA_FAILURE_CRL_4C_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL",
  "loop_contribution_label": "bio_trial_data_crl_4c_guard_counterexample_added",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R7",
  "shadow_rule_candidate": "C24 bio trial-data/regulatory event rows should hard-block Green after pivotal data failure, trial-data-quality break, or CRL unless clean regulatory pathway, resubmission scope, data readability, and cash runway are confirmed; technical rebounds should route to local 4B or 4C-watch.",
  "source_proxy_only_count": 0
}
```

## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C24 + symbol + trigger_type + entry_date.
3. Add C24-specific hard 4C / data-readability / CRL-resubmission guard only as a shadow candidate until more rows exist.

Candidate rule:
- C24_PIVOTAL_TRIAL_FAILURE_HARD_4C
- C24_TRIAL_DATA_QUALITY_BREAK_4C_WATCH
- C24_CRL_WITHOUT_RESUBMISSION_CLARITY_STAGE3_CAP
- C24_POST_EVENT_REBOUND_LOCAL_4B_ONLY

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R7/L7_BIO_HEALTHCARE_MEDICAL/C24_BIO_TRIAL_DATA_EVENT_RISK.

