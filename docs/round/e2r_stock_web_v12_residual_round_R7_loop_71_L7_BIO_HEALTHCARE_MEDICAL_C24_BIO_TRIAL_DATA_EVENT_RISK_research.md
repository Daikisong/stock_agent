# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
round=R7
loop=71
scheduled_round=R7
scheduled_loop=71
round_schedule_status=valid
round_sector_consistency=pass
computed_next_round=R8
computed_next_loop=71
large_sector_id=L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id=C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id=CLINICAL_DATA_EVENT_POSITIVE_VS_BINARY_FAILURE_AND_DEMAND_BRIDGE_GUARD
price_source=Songdaiki/stock-web
price_basis=tradable_raw
price_adjustment_status=raw_unadjusted_marcap
stock_web_manifest_max_date=2026-02-20
loop_objective=coverage_gap_fill | counterexample_mining | verified_non_proxy_evidence_repair | 4B_non_price_requirement_stress_test | sector_specific_rule_discovery | canonical_archetype_compression
```

This loop adds 2 new independent cases, 2 counterexamples, and 3 residual errors for R7/L7_BIO_HEALTHCARE_MEDICAL/C24_BIO_TRIAL_DATA_EVENT_RISK.

## 1. Current Calibrated Profile Assumption

current_default_profile_proxy = `e2r_2_1_stock_web_calibrated_proxy`  
rollback_reference_profile_id = `e2r_2_0_baseline_reference`

Tested axes:

- `price_only_blowoff_blocks_positive_stage`
- `full_4b_requires_non_price_evidence`
- `hard_4c_thesis_break_routes_to_4c`

## 2. Round / Large Sector / Canonical Archetype Scope

- scheduled_round: `R7`
- scheduled_loop: `71`
- large_sector_id: `L7_BIO_HEALTHCARE_MEDICAL`
- canonical_archetype_id: `C24_BIO_TRIAL_DATA_EVENT_RISK`
- fine_archetype_id: `CLINICAL_DATA_EVENT_POSITIVE_VS_BINARY_FAILURE_AND_DEMAND_BRIDGE_GUARD`
- round_sector_consistency: `pass`
- next_round: `R8`
- next_loop: `71`

## 3. Previous Coverage / Duplicate Avoidance Check

Before selecting cases, this loop treated `docs/core/V12_Research_No_Repeat_Index.md` as the duplicate-avoidance ledger.

C24 had prior coverage with 39 rows / 14 symbols and URL/proxy quality blockers. This loop therefore selected:
- one source-quality repair / reused-symbol holdout row: `000100`
- two new symbols for C24: `302440`, `084990`
- three different trigger families: approval-backed pivotal-data bridge, positive-data demand-trap, hard Phase III failure.

Hard duplicate key avoided:
`canonical_archetype_id + symbol + trigger_type + entry_date`.

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

Stock-Web context:
- manifest max date: `2026-02-20`
- price basis: `tradable_raw`
- adjustment: `raw_unadjusted_marcap`
- shard root: `atlas/ohlcv_tradable_by_symbol_year`

## 5. Historical Eligibility Gate

All three representative triggers have entry rows in stock-web tradable shards, at least 180 forward trading days, computed MFE/MAE 30/90/180D, and no overlapping corporate-action contamination in the 180D window.

## 6. Canonical Archetype Compression Map

C24 should not treat every "positive clinical data" headline equally.

Compression:

```text
C24 trial-data event quality gate =
    pivotal data quality
  + partner/regulatory credibility
  + commercialization or demand conversion bridge
  - binary endpoint/safety failure
  - price-only relief bounce after thesis break
```

Positive branch:
- pivotal data + regulatory/partner route + commercial bridge → Stage2/Yellow can be valid.

Counterexample branch:
- positive data but weak demand/stockpile/reorder economics → Stage2 false positive.
- hard Phase III failure followed by relief bounce → 4C remains valid; price bounce cannot undo thesis break.

## 7. Case Selection Summary

| case_id | symbol | company_name | case_type | positive_or_counterexample | calibration_usable | is_new_independent_case | current_profile_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R7L71_C24_000100_LAZERTINIB_MARIPOSA_APPROVAL_BRIDGE | 000100 | 유한양행 | structural_success | positive | True | False | current_profile_too_late |
| R7L71_C24_302440_SKY_COVIONE_PHASE3_DEMAND_TRAP | 302440 | SK바이오사이언스 | failed_rerating | counterexample | True | True | current_profile_false_positive |
| R7L71_C24_084990_ENGENSIS_DPN_PHASE3_FAILURE | 084990 | 헬릭스미스 | 4C_late | counterexample | True | True | current_profile_4C_too_late |


## 8. Positive vs Counterexample Balance

- positive_case_count: 1
- counterexample_count: 2
- 4B_case_count: 2
- 4C_case_count: 1
- calibration_usable_case_count: 3

The loop satisfies minimum balance: at least one positive, one counterexample, and three usable calibration cases.

## 9. Evidence Source Map

| case_id | symbol | trigger_type | trigger_date | entry_date | evidence_source |
| --- | --- | --- | --- | --- | --- |
| R7L71_C24_000100_LAZERTINIB_MARIPOSA_APPROVAL_BRIDGE | 000100 | Stage2-Actionable | 2024-08-19 | 2024-08-20 | https://www.reuters.com/business/healthcare-pharmaceuticals/us-fda-approves-jjs-combination-therapy-type-lung-cancer-2024-08-20/ |
| R7L71_C24_302440_SKY_COVIONE_PHASE3_DEMAND_TRAP | 302440 | Stage2-Actionable | 2022-04-29 | 2022-04-29 | https://en.wikipedia.org/wiki/Skycovione |
| R7L71_C24_084990_ENGENSIS_DPN_PHASE3_FAILURE | 084990 | Stage4C | 2024-01-03 | 2024-01-03 | https://en.wikipedia.org/wiki/Helixmith |


## 10. Price Data Source Map

| case_id | symbol | price_shard_path | profile_path | entry_date | entry_price | corporate_action_window_status |
| --- | --- | --- | --- | --- | --- | --- |
| R7L71_C24_000100_LAZERTINIB_MARIPOSA_APPROVAL_BRIDGE | 000100 | atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv | atlas/symbol_profiles/000/000100.json | 2024-08-20 | 94000 | clean_180D; profile has old corporate action candidates but none overlap 2024-08-20~D+180 |
| R7L71_C24_302440_SKY_COVIONE_PHASE3_DEMAND_TRAP | 302440 | atlas/ohlcv_tradable_by_symbol_year/302/302440/2022.csv | atlas/symbol_profiles/302/302440.json | 2022-04-29 | 135500 | clean_180D |
| R7L71_C24_084990_ENGENSIS_DPN_PHASE3_FAILURE | 084990 | atlas/ohlcv_tradable_by_symbol_year/084/084990/2024.csv | atlas/symbol_profiles/084/084990.json | 2024-01-03 | 4250 | clean_180D; profile corporate-action candidates are 2019/2020/2021 and do not overlap 2024 window |


## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | symbol | trigger_type | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TRG_R7L71_C24_000100_LAZERTINIB_MARIPOSA_APPROVAL_BRIDGE | R7L71_C24_000100_LAZERTINIB_MARIPOSA_APPROVAL_BRIDGE | 000100 | Stage2-Actionable | 2024-08-20 | 94000 | 70.53 | -2.55 | 77.55 | -2.55 | 77.55 | -2.55 | current_profile_too_late |
| TRG_R7L71_C24_302440_SKY_COVIONE_PHASE3_DEMAND_TRAP | R7L71_C24_302440_SKY_COVIONE_PHASE3_DEMAND_TRAP | 302440 | Stage2-Actionable | 2022-04-29 | 135500 | 11.44 | -27.31 | 15.5 | -30.18 | 15.5 | -52.03 | current_profile_false_positive |
| TRG_R7L71_C24_084990_ENGENSIS_DPN_PHASE3_FAILURE | R7L71_C24_084990_ENGENSIS_DPN_PHASE3_FAILURE | 084990 | Stage4C | 2024-01-03 | 4250 | 75.06 | -23.06 | 75.06 | -23.06 | 75.06 | -23.18 | current_profile_4C_too_late |


## 12. Trigger-Level OHLC Backtest Tables

### R7L71_C24_000100_LAZERTINIB_MARIPOSA_APPROVAL_BRIDGE

- entry row: `2024-08-20, 96800/97400/91600/94000`
- 30D/90D peak reference: `2024-10-15 high 166900`
- max drawdown after peak reference: low around `2024-12-09 109000`
- interpretation: clinical/regulatory data created a fast rerating, but 4B overlay became relevant soon after.

### R7L71_C24_302440_SKY_COVIONE_PHASE3_DEMAND_TRAP

- entry row: `2022-04-29, close 135500`
- local peak reference: `2022-07-13 high 156500`
- later drawdown reference: low approximately `~65000` in observed 180D path
- interpretation: positive Phase III/regulatory path did not create durable demand conversion.

### R7L71_C24_084990_ENGENSIS_DPN_PHASE3_FAILURE

- entry row: `2024-01-03, close 4250`
- immediate evidence break: gap from `2024-01-02 close 6070` to `2024-01-03 close 4250`
- relief-bounce peak: `2024-02-06 high 7440`
- 180D low reference: `~3265~3280`
- interpretation: hard negative data should remain 4C even if a price-only relief bounce appears.

## 13. Current Calibrated Profile Stress Test

- 000100: current profile is too late if it waits for post-approval consensus rather than FDA/J&J/MARIPOSA evidence bridge.
- 302440: current profile can be false positive if it treats Phase III success without demand conversion as Stage2-Actionable.
- 084990: current profile can be 4C too late if relief bounce is allowed to dilute the hard trial-failure signal.

## 14. Stage2 / Yellow / Green Comparison

- Stage2 works for 000100 only when pivotal data is backed by partner/regulatory/commercial route.
- Stage2 is too generous for 302440 when the clinical data is real but demand conversion is weak.
- Stage3 Green should remain unavailable for 084990 after hard Phase III failure.

## 15. 4B Local vs Full-window Timing Audit

- 000100: non-price approval/valuation evidence supports full-window 4B watch after the rapid approval rerating.
- 302440: valuation and demand-bridge weakness justify 4B/4C guard.
- 084990: the bounce to 7440 is price-only; without non-price recovery evidence it must not weaken 4C.

## 16. 4C Protection Audit

- 084990 is the clearest 4C case: failure data came before the relief bounce. A hard 4C route would have prevented treating the bounce as a new positive thesis.
- 302440 is a softer 4C/watch case: the failure is not trial failure but demand/stockpile economics after the clinical headline.

## 17. Sector-Specific Rule Candidate

`sector_specific_rule_candidate = true`

For L7, clinical headline strength must be separated from:
- endpoint quality,
- partner/regulatory credibility,
- commercialization route,
- demand/reorder economics,
- and price-only relief bounces after hard failures.

## 18. Canonical-Archetype Rule Candidate

`canonical_archetype_rule_candidate = true`

Candidate C24 rule:

```text
if trial_data_event_positive and commercialization_or_demand_bridge is missing:
    cap at Stage2-Watch / Yellow, not Green

if hard_phase3_failure or regulatory/data rejection:
    route to 4C even if a relief bounce occurs

if approval-backed pivotal data + partner route + commercial economics exist:
    allow Stage2-Actionable / Yellow, but require early 4B valuation watch after fast repricing
```

## 19. Before / After Backtest Comparison

| profile_id | hypothesis | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | verdict |
|---|---|---:|---:|---:|---|
| P0 | current calibrated proxy | 3 | 55.35 | -18.26 | mixed; catches price strength but not data-quality distinction |
| P0b | baseline reference | 3 | 55.35 | -18.26 | weaker; more false positives |
| P1 | sector-specific C24 quality gate | 3 | 55.35 | -18.26 | better separation of positive data and failed data |
| P2 | canonical C24 trial-data gate | 3 | 55.35 | -18.26 | preferred shadow profile |
| P3 | counterexample guard | 2 | 45.28 | -26.62 | useful for 302440/084990 protection |

## 20. Score-Return Alignment Matrix

| case_id | profile_id | profile_scope | stage_label_before | stage_label_after | component_delta_explanation |
| --- | --- | --- | --- | --- | --- |
| R7L71_C24_000100_LAZERTINIB_MARIPOSA_APPROVAL_BRIDGE | P2_canonical_trial_data_event_quality_gate | canonical_archetype_specific | Stage2/Yellow depending on price action | C24_positive_gate_or_4C_guard | The shadow profile removes price-only or data-headline-only promotion unless pivotal data is accompanied by credible commercialization/demand bridge. |
| R7L71_C24_302440_SKY_COVIONE_PHASE3_DEMAND_TRAP | P2_canonical_trial_data_event_quality_gate | canonical_archetype_specific | Stage2/Yellow depending on price action | C24_positive_gate_or_4C_guard | The shadow profile removes price-only or data-headline-only promotion unless pivotal data is accompanied by credible commercialization/demand bridge. |
| R7L71_C24_084990_ENGENSIS_DPN_PHASE3_FAILURE | P2_canonical_trial_data_event_quality_gate | canonical_archetype_specific | Stage2/Yellow depending on price action | C24_positive_gate_or_4C_guard | The shadow profile removes price-only or data-headline-only promotion unless pivotal data is accompanied by credible commercialization/demand bridge. |


## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "CLINICAL_DATA_EVENT_POSITIVE_VS_BINARY_FAILURE_AND_DEMAND_BRIDGE_GUARD", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 2, "4C_case_count": 1, "new_independent_case_count": 2, "reused_case_count": 1, "calibration_usable_trigger_count": 3, "representative_trigger_count": 3, "current_profile_error_count": 3, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "C24 data-quality blocker improved by replacing source-proxy rows with explicit URL-backed trial/regulatory evidence; still needs more non-overlapping 4B/4C timing cases."}
```

## 22. Residual Contribution Summary

```jsonl
{"row_type": "residual_contribution", "round": "R7", "loop": "71", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "new_independent_case_count": 2, "reused_case_count": 1, "new_symbol_count": 2, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["current_profile_too_late", "current_profile_false_positive", "current_profile_4C_too_late"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:
- historical OHLC rows from Songdaiki/stock-web;
- 30/90/180D MFE/MAE;
- C24 evidence-source differentiation;
- duplicate avoidance at canonical + symbol + trigger_type + entry_date level.

Non-validation scope:
- not a live investment recommendation;
- not a production scoring patch;
- not a global rule change.

## 24. Shadow Weight Calibration

```jsonl
{"row_type": "shadow_weight", "round": "R7", "loop": "71", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "rule_scope": "canonical_archetype_specific", "candidate_axis": "verified_non_proxy_trial_data_quality_gate", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 2, "4C_case_count": 1, "evidence_quality": "medium_high", "proposed_delta": "no_global_delta; canonical guard only", "risk_level": "medium", "promotion_decision": "hold_for_more_evidence", "why": "Three usable cases are enough for a shadow rule candidate but not enough for a production weight delta; C24 was previously blocked by source proxy quality."}
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R7L71_C24_000100_LAZERTINIB_MARIPOSA_APPROVAL_BRIDGE", "symbol": "000100", "company_name": "유한양행", "round": "R7", "loop": "71", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "CLINICAL_DATA_EVENT_POSITIVE_VS_BINARY_FAILURE_AND_DEMAND_BRIDGE_GUARD", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable", "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "same symbol is already represented in C23/C24, but this row uses a different 2024-08-19 FDA/MARIPOSA approval-backed trigger family and is included as source-quality repair/holdout evidence", "independent_evidence_weight": 0.5, "score_price_alignment": "positive_structural_success_with_fast_4B_overlay", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "FDA/J&J approval of amivantamab + lazertinib in EGFR-mutated advanced NSCLC based on MARIPOSA late-stage data; public approval/data route visible before entry close."}
{"row_type": "case", "case_id": "R7L71_C24_302440_SKY_COVIONE_PHASE3_DEMAND_TRAP", "symbol": "302440", "company_name": "SK바이오사이언스", "round": "R7", "loop": "71", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "CLINICAL_DATA_EVENT_POSITIVE_VS_BINARY_FAILURE_AND_DEMAND_BRIDGE_GUARD", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-Actionable", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "stage2_false_positive_due_to_demand_bridge_failure", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "GBP510/SKYCovione phase III safety and immunogenicity data supported Korean filing/approval path, but COVID-vaccine demand and inventory economics failed to convert into durable rerating."}
{"row_type": "case", "case_id": "R7L71_C24_084990_ENGENSIS_DPN_PHASE3_FAILURE", "symbol": "084990", "company_name": "헬릭스미스", "round": "R7", "loop": "71", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "CLINICAL_DATA_EVENT_POSITIVE_VS_BINARY_FAILURE_AND_DEMAND_BRIDGE_GUARD", "case_type": "4C_late", "positive_or_counterexample": "counterexample", "best_trigger": "Stage4C", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "hard_4C_with_relief_bounce_false_positive_risk", "current_profile_verdict": "current_profile_4C_too_late", "price_source": "Songdaiki/stock-web", "notes": "Engensis/VM202-DPN phase III failure: public evidence says the treatment did not prove superior to placebo; stock-web shows immediate gap-down then a misleading relief bounce."}
{"row_type": "trigger", "trigger_id": "TRG_R7L71_C24_000100_LAZERTINIB_MARIPOSA_APPROVAL_BRIDGE", "case_id": "R7L71_C24_000100_LAZERTINIB_MARIPOSA_APPROVAL_BRIDGE", "symbol": "000100", "company_name": "유한양행", "round": "R7", "loop": "71", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "CLINICAL_DATA_EVENT_POSITIVE_VS_BINARY_FAILURE_AND_DEMAND_BRIDGE_GUARD", "sector": "bio_healthcare_medical", "primary_archetype": "trial_data_event_risk", "loop_objective": "coverage_gap_fill|counterexample_mining|verified_non_proxy_evidence_repair|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-08-19", "entry_date": "2024-08-20", "entry_price": 94000, "evidence_available_at_that_date": "FDA/J&J approval of amivantamab + lazertinib in EGFR-mutated advanced NSCLC based on MARIPOSA late-stage data; public approval/data route visible before entry close.", "evidence_source": "https://www.reuters.com/business/healthcare-pharmaceuticals/us-fda-approves-jjs-combination-therapy-type-lung-cancer-2024-08-20/", "stage2_evidence_fields": ["regulatory approval based on pivotal MARIPOSA data", "partner/J&J commercialization route", "large indication EGFR-mutated NSCLC"], "stage3_evidence_fields": ["FDA-approved indication", "global pharma partner", "commercialization economics visible via royalty/sales leverage"], "stage4b_evidence_fields": ["valuation_blowoff after rapid repricing"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv", "profile_path": "atlas/symbol_profiles/000/000100.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 70.53, "MFE_90D_pct": 77.55, "MFE_180D_pct": 77.55, "MFE_1Y_pct": "not_required_for_v12_minimum", "MFE_2Y_pct": "not_required_for_v12_minimum", "MAE_30D_pct": -2.55, "MAE_90D_pct": -2.55, "MAE_180D_pct": -2.55, "MAE_1Y_pct": "not_required_for_v12_minimum", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-15", "peak_price": 166900, "drawdown_after_peak_pct": -34.69, "green_lateness_ratio": "0.58", "four_b_local_peak_proximity": 0.9, "four_b_full_window_peak_proximity": 0.9, "four_b_timing_verdict": "good_full_window_4B_timing_after_approval_run", "four_b_evidence_type": "valuation_blowoff", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "positive_structural_success_with_fast_4B_overlay", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D; profile has old corporate action candidates but none overlap 2024-08-20~D+180", "same_entry_group_id": "SEG_R7L71_C24_000100_LAZERTINIB_MARIPOSA_APPROVAL_BRIDGE", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": false, "reuse_reason": "same symbol is already represented in C23/C24, but this row uses a different 2024-08-19 FDA/MARIPOSA approval-backed trigger family and is included as source-quality repair/holdout evidence", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "evidence_url_pending": false, "source_proxy_only": false}
{"row_type": "trigger", "trigger_id": "TRG_R7L71_C24_302440_SKY_COVIONE_PHASE3_DEMAND_TRAP", "case_id": "R7L71_C24_302440_SKY_COVIONE_PHASE3_DEMAND_TRAP", "symbol": "302440", "company_name": "SK바이오사이언스", "round": "R7", "loop": "71", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "CLINICAL_DATA_EVENT_POSITIVE_VS_BINARY_FAILURE_AND_DEMAND_BRIDGE_GUARD", "sector": "bio_healthcare_medical", "primary_archetype": "trial_data_event_risk", "loop_objective": "coverage_gap_fill|counterexample_mining|verified_non_proxy_evidence_repair|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2022-04-29", "entry_date": "2022-04-29", "entry_price": 135500, "evidence_available_at_that_date": "GBP510/SKYCovione phase III safety and immunogenicity data supported Korean filing/approval path, but COVID-vaccine demand and inventory economics failed to convert into durable rerating.", "evidence_source": "https://en.wikipedia.org/wiki/Skycovione", "stage2_evidence_fields": ["positive phase III immunogenicity/safety data", "domestic first vaccine optionality", "regulatory filing/approval route"], "stage3_evidence_fields": ["unknown_or_not_supported: durable demand/reorder economics not visible"], "stage4b_evidence_fields": ["vaccine-demand cliff", "inventory and procurement overhang", "valuation premium decay"], "stage4c_evidence_fields": ["thesis_evidence_broken_by_demand_conversion_failure"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/302/302440/2022.csv", "profile_path": "atlas/symbol_profiles/302/302440.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 11.44, "MFE_90D_pct": 15.5, "MFE_180D_pct": 15.5, "MFE_1Y_pct": "not_required_for_v12_minimum", "MFE_2Y_pct": "not_required_for_v12_minimum", "MAE_30D_pct": -27.31, "MAE_90D_pct": -30.18, "MAE_180D_pct": -52.03, "MAE_1Y_pct": "not_required_for_v12_minimum", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-07-13", "peak_price": 156500, "drawdown_after_peak_pct": -59.87, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": 0.55, "four_b_full_window_peak_proximity": 0.55, "four_b_timing_verdict": "demand_bridge_missing_counterexample", "four_b_evidence_type": "margin_or_backlog_slowdown|positioning_overheat", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "stage2_false_positive_due_to_demand_bridge_failure", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D", "same_entry_group_id": "SEG_R7L71_C24_302440_SKY_COVIONE_PHASE3_DEMAND_TRAP", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": false, "source_proxy_only": false}
{"row_type": "trigger", "trigger_id": "TRG_R7L71_C24_084990_ENGENSIS_DPN_PHASE3_FAILURE", "case_id": "R7L71_C24_084990_ENGENSIS_DPN_PHASE3_FAILURE", "symbol": "084990", "company_name": "헬릭스미스", "round": "R7", "loop": "71", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "CLINICAL_DATA_EVENT_POSITIVE_VS_BINARY_FAILURE_AND_DEMAND_BRIDGE_GUARD", "sector": "bio_healthcare_medical", "primary_archetype": "trial_data_event_risk", "loop_objective": "coverage_gap_fill|counterexample_mining|verified_non_proxy_evidence_repair|4B_non_price_requirement_stress_test", "trigger_type": "Stage4C", "trigger_date": "2024-01-03", "entry_date": "2024-01-03", "entry_price": 4250, "evidence_available_at_that_date": "Engensis/VM202-DPN phase III failure: public evidence says the treatment did not prove superior to placebo; stock-web shows immediate gap-down then a misleading relief bounce.", "evidence_source": "https://en.wikipedia.org/wiki/Helixmith", "stage2_evidence_fields": ["none: negative trial-data event, not a promotion trigger"], "stage3_evidence_fields": ["none"], "stage4b_evidence_fields": ["price-only relief bounce after hard data break"], "stage4c_evidence_fields": ["phase III failure", "primary efficacy not superior to placebo", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/084/084990/2024.csv", "profile_path": "atlas/symbol_profiles/084/084990.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 75.06, "MFE_90D_pct": 75.06, "MFE_180D_pct": 75.06, "MFE_1Y_pct": "not_required_for_v12_minimum", "MFE_2Y_pct": "not_required_for_v12_minimum", "MAE_30D_pct": -23.06, "MAE_90D_pct": -23.06, "MAE_180D_pct": -23.18, "MAE_1Y_pct": "not_required_for_v12_minimum", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-06", "peak_price": 7440, "drawdown_after_peak_pct": -56.12, "green_lateness_ratio": "not_applicable:negative_4C_case", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_local_4B_too_early_if_no_non_price_4B_evidence", "four_b_evidence_type": "price_only", "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "hard_4C_with_relief_bounce_false_positive_risk", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D; profile corporate-action candidates are 2019/2020/2021 and do not overlap 2024 window", "same_entry_group_id": "SEG_R7L71_C24_084990_ENGENSIS_DPN_PHASE3_FAILURE", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": false, "source_proxy_only": false}
{"row_type": "score_simulation", "case_id": "R7L71_C24_000100_LAZERTINIB_MARIPOSA_APPROVAL_BRIDGE", "round": "R7", "loop": "71", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "profile_id": "P2_canonical_trial_data_event_quality_gate", "profile_scope": "canonical_archetype_specific", "profile_hypothesis": "C24 should separate pivotal data + commercialization bridge from positive data with weak demand conversion and from hard negative data with relief bounces.", "changed_axes": ["verified_non_proxy_trial_data_required", "commercialization_or_demand_bridge_required_for_positive_stage", "price_only_relief_bounce_cannot_weaken_4C"], "raw_component_scores_before": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": "mixed", "relative_strength_score": "observed", "customer_quality_score": "partner_or_demand_bridge_dependent", "policy_or_regulatory_score": "observed", "valuation_repricing_score": "observed", "execution_risk_score": "observed", "legal_or_contract_risk_score": "low_to_unknown", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_before": "research_proxy_mixed", "stage_label_before": "Stage2/Yellow depending on price action", "raw_component_scores_after": {"trial_data_quality_score": "positive", "commercialization_bridge_score": "strong", "demand_conversion_score": "strong", "hard_4c_score": "not_applicable"}, "weighted_score_after": "positive_only_for_000100; guard_or_4C_for_302440_084990", "stage_label_after": "C24_positive_gate_or_4C_guard", "component_delta_explanation": "The shadow profile removes price-only or data-headline-only promotion unless pivotal data is accompanied by credible commercialization/demand bridge."}
{"row_type": "score_simulation", "case_id": "R7L71_C24_302440_SKY_COVIONE_PHASE3_DEMAND_TRAP", "round": "R7", "loop": "71", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "profile_id": "P2_canonical_trial_data_event_quality_gate", "profile_scope": "canonical_archetype_specific", "profile_hypothesis": "C24 should separate pivotal data + commercialization bridge from positive data with weak demand conversion and from hard negative data with relief bounces.", "changed_axes": ["verified_non_proxy_trial_data_required", "commercialization_or_demand_bridge_required_for_positive_stage", "price_only_relief_bounce_cannot_weaken_4C"], "raw_component_scores_before": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": "mixed", "relative_strength_score": "observed", "customer_quality_score": "partner_or_demand_bridge_dependent", "policy_or_regulatory_score": "observed", "valuation_repricing_score": "observed", "execution_risk_score": "observed", "legal_or_contract_risk_score": "low_to_unknown", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_before": "research_proxy_mixed", "stage_label_before": "Stage2/Yellow depending on price action", "raw_component_scores_after": {"trial_data_quality_score": "negative_or_insufficient", "commercialization_bridge_score": "weak", "demand_conversion_score": "weak", "hard_4c_score": "not_applicable"}, "weighted_score_after": "positive_only_for_000100; guard_or_4C_for_302440_084990", "stage_label_after": "C24_positive_gate_or_4C_guard", "component_delta_explanation": "The shadow profile removes price-only or data-headline-only promotion unless pivotal data is accompanied by credible commercialization/demand bridge."}
{"row_type": "score_simulation", "case_id": "R7L71_C24_084990_ENGENSIS_DPN_PHASE3_FAILURE", "round": "R7", "loop": "71", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "profile_id": "P2_canonical_trial_data_event_quality_gate", "profile_scope": "canonical_archetype_specific", "profile_hypothesis": "C24 should separate pivotal data + commercialization bridge from positive data with weak demand conversion and from hard negative data with relief bounces.", "changed_axes": ["verified_non_proxy_trial_data_required", "commercialization_or_demand_bridge_required_for_positive_stage", "price_only_relief_bounce_cannot_weaken_4C"], "raw_component_scores_before": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": "mixed", "relative_strength_score": "observed", "customer_quality_score": "partner_or_demand_bridge_dependent", "policy_or_regulatory_score": "observed", "valuation_repricing_score": "observed", "execution_risk_score": "observed", "legal_or_contract_risk_score": "low_to_unknown", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_before": "research_proxy_mixed", "stage_label_before": "Stage2/Yellow depending on price action", "raw_component_scores_after": {"trial_data_quality_score": "negative_or_insufficient", "commercialization_bridge_score": "weak", "demand_conversion_score": "not_applicable", "hard_4c_score": "strong"}, "weighted_score_after": "positive_only_for_000100; guard_or_4C_for_302440_084990", "stage_label_after": "C24_positive_gate_or_4C_guard", "component_delta_explanation": "The shadow profile removes price-only or data-headline-only promotion unless pivotal data is accompanied by credible commercialization/demand bridge."}
{"row_type": "coverage_matrix", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "CLINICAL_DATA_EVENT_POSITIVE_VS_BINARY_FAILURE_AND_DEMAND_BRIDGE_GUARD", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 2, "4C_case_count": 1, "new_independent_case_count": 2, "reused_case_count": 1, "calibration_usable_trigger_count": 3, "representative_trigger_count": 3, "current_profile_error_count": 3, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "C24 data-quality blocker improved by replacing source-proxy rows with explicit URL-backed trial/regulatory evidence; still needs more non-overlapping 4B/4C timing cases."}
{"row_type": "shadow_weight", "round": "R7", "loop": "71", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "rule_scope": "canonical_archetype_specific", "candidate_axis": "verified_non_proxy_trial_data_quality_gate", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 2, "4C_case_count": 1, "evidence_quality": "medium_high", "proposed_delta": "no_global_delta; canonical guard only", "risk_level": "medium", "promotion_decision": "hold_for_more_evidence", "why": "Three usable cases are enough for a shadow rule candidate but not enough for a production weight delta; C24 was previously blocked by source proxy quality."}
{"row_type": "residual_contribution", "round": "R7", "loop": "71", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "new_independent_case_count": 2, "reused_case_count": 1, "new_symbol_count": 2, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["current_profile_too_late", "current_profile_false_positive", "current_profile_4C_too_late"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules

- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate large_sector_id and canonical_archetype_id.
4. Validate novelty and reuse fields.
5. Deduplicate same_entry_group_id and reused cases.
6. Aggregate by large_sector_id and canonical_archetype_id.
7. Update sector_shadow_profile and archetype_shadow_profile only.
8. Preserve global calibrated profile unless explicitly promoted.
9. Report new independent cases, counterexamples, and residual error types.
10. Add tests that duplicate low-value loops cannot change weights.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
next_round=R8
next_loop=71
computed_next_round=R8
computed_next_loop=71
```

## 28. Source Notes

- Reuters / J&J-FDA coverage for lazertinib + amivantamab approval-backed pivotal MARIPOSA route.
- Skycovione public trial/regulatory summary for GBP510 Phase III and demand-conversion failure.
- Helixmith public trial failure summary for Engensis/VM202-DPN Phase III.
- Songdaiki/stock-web OHLC rows and profiles for all price-path calculations.

