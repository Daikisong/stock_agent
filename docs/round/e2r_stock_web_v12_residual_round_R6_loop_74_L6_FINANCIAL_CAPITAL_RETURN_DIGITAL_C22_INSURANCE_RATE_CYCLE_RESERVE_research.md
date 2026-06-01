# E2R Stock-Web v12 Residual Research — R6 Loop 74 / L6 / C22

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R6",
  "scheduled_loop": 74,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R6",
  "completed_loop": 74,
  "computed_next_round": "R7",
  "computed_next_loop": 74,
  "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL",
  "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE",
  "fine_archetype_id": "NON_TOP_INSURER_CSM_RESERVE_CAPITAL_RETURN_VS_LIFE_INSURANCE_BETA_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression",
    "source_repair_queue_creation",
    "share_count_validation_queue_creation"
  ],
  "price_source": "Songdaiki/stock-web",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "stock_web_manifest_max_date": "2026-02-20",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "handoff_prompt_executed_now": false,
  "do_not_propose_new_weight_delta": true
}
```

## Execution compliance note

This file is a standalone historical calibration / sector-archetype residual research Markdown artifact.  
It does not patch `stock_agent`, does not run live discovery, and does not propose immediate production scoring changes.

The execution used `Songdaiki/stock-web` as the sole price atlas:

```text
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_executed_now = false
```

## Round / scope resolution

Previous completed state in this interactive run: R5 / loop 74.

Therefore:

```text
scheduled_round = R6
scheduled_loop = 74
allowed_large_sector = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
selected_large_sector = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
selected_canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
computed_next_round = R7
computed_next_loop = 74
```

R6 was routed to C22 because loop 73 had used C21 and No-Repeat shows C22 is concentrated in top-covered insurers.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C22 is concentrated in:

```text
000810, 005830, 088350, 001450, 000400
```

This run uses three different symbols:

```text
000370 / 한화손해보험 / P&C reserve/capital-return bridge
003690 / 코리안리 / reinsurance rate-cycle reserve/capital buffer
085620 / 미래에셋생명 / life-insurance value-up beta bridge fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
003690 shows a late-2024 share-count change in the price shard and therefore requires coding-agent validation before runtime promotion.
```

## Research thesis

C22 is not “insurance stock went up.”

The mechanism is:

```text
insurance rate cycle / IFRS17 attention
→ CSM and reserve quality
→ loss-ratio, pricing, K-ICS or capital buffer
→ dividend / buyback / shareholder-return bridge
→ durable rerating
```

Insurance rerating is an actuarial bridge.  
The price can jump first, but the reserve and capital math must still walk across.

---

## Case 1 — Positive: 000370 / 한화손해보험

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is CSM quality, reserve release, loss ratio/pricing, K-ICS and capital-return evidence.

```text
evidence_family = P_AND_C_INSURANCE_CSM_RESERVE_RELEASE_LOSS_RATIO_CAPITAL_RETURN_BRIDGE
case_role = positive_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 4,320
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/000/000370/2024.csv`:

```text
2024-02-01,4320,5640,4150,5120
2024-02-13,5590,6170,5380,5520
2024-08-20,5840,6230,5810,6190
2024-10-02,5000,5050,4865,4895
```

### Backtest

```text
MFE_30D  = +42.82%
MAE_30D  = -3.94%
MFE_90D  = +42.82%
MAE_90D  = -3.94%
MFE_180D = +44.21%
MAE_180D = -3.94%
peak_180 = 6,230 on 2024-08-20
trough_180 = 4,150 on 2024-02-01
peak_to_later_drawdown = -21.91%
```

### Interpretation

This is the strongest C22 row in this set.  
The price path supports a P&C reserve/capital-return bridge, but source repair is still required before runtime promotion.

---

## Case 2 — Positive slow bridge with share-count validation: 003690 / 코리안리

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
source_repair_required = true
```

The source-repair task is reinsurance pricing cycle, reserve adequacy, capital buffer and shareholder-return evidence.

```text
evidence_family = REINSURANCE_RATE_CYCLE_RESERVE_STRENGTH_CAPITAL_BUFFER_BRIDGE
case_role = positive_slow_with_sharecount_validation
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 7,580
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/003/003690/2024.csv`:

```text
2024-02-01,7580,7960,7470,7810
2024-03-22,8360,8550,8340,8510
2024-11-05,9280,9550,9280,9520
2024-11-25,7850,7920,7700,7920
```

### Backtest

```text
MFE_30D  = +9.89%
MAE_30D  = -1.45%
MFE_90D  = +12.80%
MAE_90D  = -1.45%
MFE_180D = +25.99%
MAE_180D = -1.45%
peak_180 = 9,550 on 2024-11-05
trough_180 = 7,470 on 2024-02-01
peak_to_later_drawdown = -19.37%
```

### Interpretation

This is a slow C22 positive.  
The rerating is less explosive than P&C value-up names, but the low MAE says the bridge can be structurally useful.

However, the price shard shows a share-count change in late 2024, so this row should not promote to runtime evidence without validation.

---

## Case 3 — Counterexample / local 4B: 085620 / 미래에셋생명

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests life-insurance value-up/rate beta without enough visible CSM, reserve, K-ICS or capital-return refresh.

```text
evidence_family = LIFE_INSURANCE_VALUEUP_RATE_BETA_WITH_WEAK_CSM_RESERVE_CAPITAL_RETURN_REFRESH
case_role = counterexample
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 5,670
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/085/085620/2024.csv`:

```text
2024-02-01,5670,6420,5610,5770
2024-02-06,6320,6500,6100,6240
2024-03-20,4550,4560,4500,4500
2024-08-05,5050,5090,4660,4950
```

### Backtest

```text
MFE_30D  = +14.64%
MAE_30D  = -11.82%
MFE_90D  = +14.64%
MAE_90D  = -20.63%
MFE_180D = +14.64%
MAE_180D = -20.63%
peak_180 = 6,500 on 2024-02-06
trough_180 = 4,500 on 2024-03-20
peak_to_later_drawdown = -30.77%
```

### Interpretation

This is the C22 beta-fade case.  
The early move was real, but the stock quickly opened a 90D MAE shock. Without CSM, reserve, K-ICS or capital-return bridge, this should not be durable Green.

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
```

### What this does not justify

```text
do_not_raise_generic_C22_insurance_beta_weight = true
do_not_treat_all_insurance_valueup_beta_as_Green = true
do_not_convert_insurance_drawdown_to_hard_4C_without_non_price_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
NON_TOP_INSURER_CSM_RESERVE_CAPITAL_RETURN_VS_LIFE_INSURANCE_BETA_FADE
```

This fine archetype covers:

```text
1. P&C reserve/CSM/loss-ratio/capital-return bridge → Stage2 possible after source repair
2. reinsurer rate-cycle/reserve/capital buffer → slow Stage2 possible after source repair
3. life-insurance value-up beta without CSM/capital-return refresh → false Stage2 / local 4B-watch
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R6L74-C22-000370-HANWHA-GI-RESERVE-CAPITAL-RETURN", "symbol": "000370", "company_name": "한화손해보험", "round": "R6", "loop": "74", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "NON_TOP_INSURER_CSM_RESERVE_CAPITAL_RETURN_VS_LIFE_INSURANCE_BETA_FADE", "case_type": "insurance_rate_cycle_reserve", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-GIReserveCapitalReturnBridge", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C22 should allow Stage2 when non-top P&C insurers show CSM, reserve release, loss-ratio improvement, K-ICS/capital return or shareholder-return bridge. Hanwha General Insurance produced high MFE with controlled entry-basis MAE, but later local 4B-watch is needed if the reserve/capital-return evidence stops refreshing.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy CSM/reserve/K-ICS/loss-ratio/capital-return evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R6L74-C22-003690-KOREANRE-REINSURANCE-CYCLE-CAPITAL-BUFFER", "symbol": "003690", "company_name": "코리안리", "round": "R6", "loop": "74", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "NON_TOP_INSURER_CSM_RESERVE_CAPITAL_RETURN_VS_LIFE_INSURANCE_BETA_FADE", "case_type": "insurance_rate_cycle_reserve", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-ReinsuranceRateCycleCapitalBuffer", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C22 should include reinsurers when pricing cycle, reserve adequacy and capital buffer translate into low-MAE rerating. Korean Re produced slow but durable MFE; however a late-2024 share-count change in the shard requires validation before runtime promotion.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy CSM/reserve/K-ICS/loss-ratio/capital-return evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R6L74-C22-085620-MIRAE-LIFE-BETA-BRIDGE-FADE", "symbol": "085620", "company_name": "미래에셋생명", "round": "R6", "loop": "74", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "NON_TOP_INSURER_CSM_RESERVE_CAPITAL_RETURN_VS_LIFE_INSURANCE_BETA_FADE", "case_type": "insurance_rate_cycle_reserve", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / LifeInsuranceBetaBridgeFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C22 should not treat life-insurance/value-up beta as durable Stage2 unless CSM quality, reserve sensitivity, K-ICS and capital-return evidence refreshes. Mirae Asset Life had an early MFE but quickly opened 90D MAE and never produced a strong rerating path.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy CSM/reserve/K-ICS/loss-ratio/capital-return evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R6L74-C22-000370-HANWHA-GI-RESERVE-CAPITAL-RETURN", "case_id": "R6L74-C22-000370-HANWHA-GI-RESERVE-CAPITAL-RETURN", "symbol": "000370", "company_name": "한화손해보험", "round": "R6", "loop": "74", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "NON_TOP_INSURER_CSM_RESERVE_CAPITAL_RETURN_VS_LIFE_INSURANCE_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable-GIReserveCapitalReturnBridge", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 4320.0, "evidence_available_at_that_date": "P_AND_C_INSURANCE_CSM_RESERVE_RELEASE_LOSS_RATIO_CAPITAL_RETURN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:HANWHA_GENERAL_INSURANCE_2024_CSM_RESERVE_LOSS_RATIO_CAPITAL_RETURN_BRIDGE", "stage2_evidence_fields": ["insurance_rate_cycle", "reserve_or_csm_bridge_candidate", "capital_return_candidate"], "stage3_evidence_fields": ["relative_strength", "csms_or_loss_ratio_bridge_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000370/2024.csv", "profile_path": "atlas/symbol_profiles/000/000370.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 42.82, "MFE_90D_pct": 42.82, "MFE_180D_pct": 44.21, "MAE_30D_pct": -3.94, "MAE_90D_pct": -3.94, "MAE_180D_pct": -3.94, "peak_date": "2024-08-20", "peak_price": 6230.0, "drawdown_after_peak_pct": -21.91, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_insurance_rate_or_csm_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_reserve_kics_or_capital_return_break", "trigger_outcome_label": "positive_with_later_4b_watch", "current_profile_verdict": "C22 should allow Stage2 when non-top P&C insurers show CSM, reserve release, loss-ratio improvement, K-ICS/capital return or shareholder-return bridge. Hanwha General Insurance produced high MFE with controlled entry-basis MAE, but later local 4B-watch is needed if the reserve/capital-return evidence stops refreshing.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C22_INSURANCE_000370_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R6L74-C22-003690-KOREANRE-REINSURANCE-CYCLE-CAPITAL-BUFFER", "case_id": "R6L74-C22-003690-KOREANRE-REINSURANCE-CYCLE-CAPITAL-BUFFER", "symbol": "003690", "company_name": "코리안리", "round": "R6", "loop": "74", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "NON_TOP_INSURER_CSM_RESERVE_CAPITAL_RETURN_VS_LIFE_INSURANCE_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable-ReinsuranceRateCycleCapitalBuffer", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 7580.0, "evidence_available_at_that_date": "REINSURANCE_RATE_CYCLE_RESERVE_STRENGTH_CAPITAL_BUFFER_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:KOREAN_RE_2024_REINSURANCE_RATE_CYCLE_RESERVE_CAPITAL_BUFFER_BRIDGE", "stage2_evidence_fields": ["insurance_rate_cycle", "reserve_or_csm_bridge_candidate", "capital_return_candidate"], "stage3_evidence_fields": ["relative_strength", "csms_or_loss_ratio_bridge_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003690/2024.csv", "profile_path": "atlas/symbol_profiles/003/003690.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 9.89, "MFE_90D_pct": 12.8, "MFE_180D_pct": 25.99, "MAE_30D_pct": -1.45, "MAE_90D_pct": -1.45, "MAE_180D_pct": -1.45, "peak_date": "2024-11-05", "peak_price": 9550.0, "drawdown_after_peak_pct": -19.37, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_insurance_rate_or_csm_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_reserve_kics_or_capital_return_break", "trigger_outcome_label": "positive_slow_with_sharecount_validation", "current_profile_verdict": "C22 should include reinsurers when pricing cycle, reserve adequacy and capital buffer translate into low-MAE rerating. Korean Re produced slow but durable MFE; however a late-2024 share-count change in the shard requires validation before runtime promotion.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": true, "same_entry_group_id": "C22_INSURANCE_003690_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R6L74-C22-085620-MIRAE-LIFE-BETA-BRIDGE-FADE", "case_id": "R6L74-C22-085620-MIRAE-LIFE-BETA-BRIDGE-FADE", "symbol": "085620", "company_name": "미래에셋생명", "round": "R6", "loop": "74", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "NON_TOP_INSURER_CSM_RESERVE_CAPITAL_RETURN_VS_LIFE_INSURANCE_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-FalsePositive / LifeInsuranceBetaBridgeFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 5670.0, "evidence_available_at_that_date": "LIFE_INSURANCE_VALUEUP_RATE_BETA_WITH_WEAK_CSM_RESERVE_CAPITAL_RETURN_REFRESH", "evidence_source": "source_proxy_manual_verification_required:MIRAE_ASSET_LIFE_2024_LIFE_INSURANCE_VALUEUP_CSM_RESERVE_KICS_CAPITAL_RETURN_BRIDGE", "stage2_evidence_fields": ["insurance_rate_cycle", "reserve_or_csm_bridge_candidate", "capital_return_candidate"], "stage3_evidence_fields": ["relative_strength", "csms_or_loss_ratio_bridge_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/085/085620/2024.csv", "profile_path": "atlas/symbol_profiles/085/085620.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 14.64, "MFE_90D_pct": 14.64, "MFE_180D_pct": 14.64, "MAE_30D_pct": -11.82, "MAE_90D_pct": -20.63, "MAE_180D_pct": -20.63, "peak_date": "2024-02-06", "peak_price": 6500.0, "drawdown_after_peak_pct": -30.77, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_insurance_rate_or_csm_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_reserve_kics_or_capital_return_break", "trigger_outcome_label": "counterexample", "current_profile_verdict": "C22 should not treat life-insurance/value-up beta as durable Stage2 unless CSM quality, reserve sensitivity, K-ICS and capital-return evidence refreshes. Mirae Asset Life had an early MFE but quickly opened 90D MAE and never produced a strong rerating path.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C22_INSURANCE_085620_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L74-C22-000370-HANWHA-GI-RESERVE-CAPITAL-RETURN", "trigger_id": "TRG_R6L74-C22-000370-HANWHA-GI-RESERVE-CAPITAL-RETURN", "symbol": "000370", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"rate_cycle_score": 11, "reserve_csm_score": 14, "kics_capital_score": 12, "loss_ratio_or_pricing_score": 12, "capital_return_score": 12, "relative_strength_score": 13, "valuation_repricing_score": 12, "execution_risk_score": 5, "dilution_or_sharecount_risk_score": 0, "source_confidence_score": 2}, "weighted_score_before": 82, "stage_label_before": "Stage2-Actionable after source repair", "raw_component_scores_after": {"rate_cycle_score": 12, "reserve_csm_score": 16, "kics_capital_score": 13, "loss_ratio_or_pricing_score": 13, "capital_return_score": 14, "relative_strength_score": 13, "valuation_repricing_score": 11, "execution_risk_score": 5, "dilution_or_sharecount_risk_score": 0, "source_confidence_score": 2}, "weighted_score_after": 88, "stage_label_after": "Stage2/Green candidate after source repair + lifecycle 4B", "changed_components": ["reserve_csm_score", "capital_return_score", "execution_risk_score", "dilution_or_sharecount_risk_score"], "component_delta_explanation": "Reward only verified CSM/reserve/K-ICS/capital-return bridge; cap life-insurance beta when reserve and capital-return evidence fails to refresh.", "MFE_90D_pct": 42.82, "MAE_90D_pct": -3.94, "score_return_alignment_label": "aligned_positive_with_source_repair", "current_profile_verdict": "C22 should allow Stage2 when non-top P&C insurers show CSM, reserve release, loss-ratio improvement, K-ICS/capital return or shareholder-return bridge. Hanwha General Insurance produced high MFE with controlled entry-basis MAE, but later local 4B-watch is needed if the reserve/capital-return evidence stops refreshing."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L74-C22-003690-KOREANRE-REINSURANCE-CYCLE-CAPITAL-BUFFER", "trigger_id": "TRG_R6L74-C22-003690-KOREANRE-REINSURANCE-CYCLE-CAPITAL-BUFFER", "symbol": "003690", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"rate_cycle_score": 11, "reserve_csm_score": 14, "kics_capital_score": 12, "loss_ratio_or_pricing_score": 7, "capital_return_score": 12, "relative_strength_score": 13, "valuation_repricing_score": 12, "execution_risk_score": 5, "dilution_or_sharecount_risk_score": 5, "source_confidence_score": 2}, "weighted_score_before": 82, "stage_label_before": "Stage2-Actionable after source repair", "raw_component_scores_after": {"rate_cycle_score": 12, "reserve_csm_score": 16, "kics_capital_score": 13, "loss_ratio_or_pricing_score": 6, "capital_return_score": 14, "relative_strength_score": 13, "valuation_repricing_score": 11, "execution_risk_score": 5, "dilution_or_sharecount_risk_score": 8, "source_confidence_score": 2}, "weighted_score_after": 88, "stage_label_after": "Stage2/Green candidate after source repair + lifecycle 4B", "changed_components": ["reserve_csm_score", "capital_return_score", "execution_risk_score", "dilution_or_sharecount_risk_score"], "component_delta_explanation": "Reward only verified CSM/reserve/K-ICS/capital-return bridge; cap life-insurance beta when reserve and capital-return evidence fails to refresh.", "MFE_90D_pct": 12.8, "MAE_90D_pct": -1.45, "score_return_alignment_label": "aligned_positive_with_source_repair", "current_profile_verdict": "C22 should include reinsurers when pricing cycle, reserve adequacy and capital buffer translate into low-MAE rerating. Korean Re produced slow but durable MFE; however a late-2024 share-count change in the shard requires validation before runtime promotion."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L74-C22-085620-MIRAE-LIFE-BETA-BRIDGE-FADE", "trigger_id": "TRG_R6L74-C22-085620-MIRAE-LIFE-BETA-BRIDGE-FADE", "symbol": "085620", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"rate_cycle_score": 7, "reserve_csm_score": 4, "kics_capital_score": 4, "loss_ratio_or_pricing_score": 7, "capital_return_score": 4, "relative_strength_score": 6, "valuation_repricing_score": 6, "execution_risk_score": 15, "dilution_or_sharecount_risk_score": 0, "source_confidence_score": 2}, "weighted_score_before": 54, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"rate_cycle_score": 5, "reserve_csm_score": 2, "kics_capital_score": 2, "loss_ratio_or_pricing_score": 6, "capital_return_score": 3, "relative_strength_score": 4, "valuation_repricing_score": 5, "execution_risk_score": 18, "dilution_or_sharecount_risk_score": 0, "source_confidence_score": 2}, "weighted_score_after": 43, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["reserve_csm_score", "capital_return_score", "execution_risk_score", "dilution_or_sharecount_risk_score"], "component_delta_explanation": "Reward only verified CSM/reserve/K-ICS/capital-return bridge; cap life-insurance beta when reserve and capital-return evidence fails to refresh.", "MFE_90D_pct": 14.64, "MAE_90D_pct": -20.63, "score_return_alignment_label": "false_positive_life_insurance_beta_bridge_gap", "current_profile_verdict": "C22 should not treat life-insurance/value-up beta as durable Stage2 unless CSM quality, reserve sensitivity, K-ICS and capital-return evidence refreshes. Mirae Asset Life had an early MFE but quickly opened 90D MAE and never produced a strong rerating path."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R6", "loop": 74, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "NON_TOP_INSURER_CSM_RESERVE_CAPITAL_RETURN_VS_LIFE_INSURANCE_BETA_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 1, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 1, "current_profile_error_count": 1, "diversity_score_summary": "+3 underused C22 insurance symbols outside top-covered set, +3 P&C/reinsurance/life-insurance trigger families, +2 controlled-MAE positives, +1 life-insurance beta fade counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_and_sharecount_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R6", "loop": 74, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "axis": "non_top_insurer_csm_reserve_capital_return_vs_life_insurance_beta_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C22 should split verified CSM/reserve/K-ICS/capital-return bridge from generic insurance value-up beta. P&C and reinsurer positives may be Stage2 when reserve release, loss ratio/pricing and capital return are explicit. Life-insurance beta should route to local 4B-watch if MAE opens and CSM/capital-return evidence is weak or stale.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["000370", "003690", "085620"], "share_count_validation_required": ["003690"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R6", "loop": 74, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C22 needs reserve/capital proof. Hanwha General Insurance and Korean Re show non-top insurer P&C/reinsurance positives after source repair; Mirae Asset Life shows insurance value-up beta fading into local 4B when CSM/reserve/capital-return evidence is weak."}
```

---

## Validation scope

```text
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
forward_window_basis = stock_web_manifest_max_date
all_selected_entry_dates_present_in_tradable_shards = true
all_selected_180D_windows_available = true
production_scoring_changed = false
shadow_weight_only = true
```

Profile checks:

```text
000370:
  corporate_action_candidate_dates = 2001-01-16, 2003-02-27, 2004-04-28, 2007-03-06, 2010-01-20, 2013-11-28, 2017-11-23
  selected window = 2024-02-01~D+180
  contamination = false

003690:
  corporate_action_candidate_dates = 1997-03-29, 2004-07-20
  selected window = 2024-02-01~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required

085620:
  corporate_action_candidate_dates = 2018-03-23
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C22 rows are source_proxy_only / evidence_url_pending.
003690 also requires share-count validation before runtime promotion.
This MD is useful for stock-web path calibration and C22 rule-shape discovery,
but coding-agent promotion requires non-proxy CSM, reserve, K-ICS, loss-ratio and capital-return evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R6/C22 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair.

Candidate axis:
non_top_insurer_csm_reserve_capital_return_vs_life_insurance_beta_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 000370, 003690 and 085620.
4. Validate 003690 share-count change inside the selected window.
5. Keep generic C22 insurance beta weight unchanged until source repair is complete.
6. Consider Stage2 only when:
   - CSM or reserve-quality evidence is explicit,
   - K-ICS/capital buffer or capital-return policy is visible,
   - loss-ratio/pricing or reinsurance rate-cycle bridge exists,
   - MAE remains controlled.
7. Consider local 4B-watch when:
   - the trigger is insurance value-up/rate beta only,
   - CSM/reserve/capital-return evidence is weak or stale,
   - MAE_90D <= -20% or post-peak drawdown <= -30~35%.
8. Do not convert local 4B-watch into full 4B/4C without non-price reserve deterioration, K-ICS shock, capital impairment, regulatory or solvency break.
9. Emit before/after diagnostics and reject if verified P&C/reinsurance positives are overblocked.
```

---

## Final round state

```text
completed_round = R6
completed_loop = 74
next_round = R7
next_loop = 74
round_schedule_status = valid
round_sector_consistency = pass
```

