# E2R Stock-Web v12 Residual Research — R12 Loop 73 / L10 / C32

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R12",
  "scheduled_loop": 73,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R12",
  "completed_loop": 73,
  "computed_next_round": "R13",
  "computed_next_loop": 73,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP",
  "fine_archetype_id": "DOOSAN_RESTRUCTURING_MERGER_RATIO_CONTROL_PREMIUM_VS_MINORITY_EXECUTION_RISK",
  "loop_objective": [
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression",
    "source_repair_queue_creation",
    "governance_restructuring_lifecycle_test"
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

Previous completed state in this interactive run: R11 / loop 73.

Therefore:

```text
scheduled_round = R12
scheduled_loop = 73
allowed_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC or under-covered service/agri
selected_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
selected_canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
computed_next_round = R13
computed_next_loop = 73
```

R12 was routed to C32 because this is a governance restructuring / merger-ratio / control-premium lifecycle test.  
This file deliberately avoids the high-repeat Korea Zinc / SM / Hanmi / Hanyang set used in prior C32 research.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C32 concentration in `010130`, `041510`, `000240`, 고려아연 and 에스엠.  
This run adds a new governance-restructuring family:

```text
241560 / 두산밥캣 / merger-ratio minority risk
454910 / 두산로보틱스 / valuation beta / acquirer-beneficiary risk
000150 / 두산 / delayed holdco control-premium option value
```

## Evidence event

The evidence event is the 2024 Doosan restructuring controversy involving Doosan Bobcat and Doosan Robotics.  
The publicly reported issue was not a simple tender price. It was a merger/restructuring ratio and minority-shareholder treatment problem: operating-subsidiary value, acquirer valuation, and holding-company control economics pointed in different directions.

```text
evidence_family = DOOSAN_RESTRUCTURING_MERGER_RATIO_CONTROL_PREMIUM
trigger_date = 2024-07-11
entry_date = 2024-07-12
```

## Research thesis

C32 is not simply “governance event means control premium.”

A restructuring is a machine with different gears:

```text
operating subsidiary
→ merger ratio / minority treatment risk

acquirer or nominal beneficiary
→ valuation beta / execution risk

holding company
→ delayed control-premium option value
```

The same headline can help one class of shareholder and hurt another.  
C32 must therefore classify by economic seat, not by headline temperature.

---

## Case 1 — Counterexample / local 4B: 241560 / 두산밥캣

### Evidence status

```text
event source = non-proxy
company-level merger-ratio / minority-treatment bridge = evidence_url_pending
```

```text
evidence_family = DOOSAN_BOBCAT_ROBOTICS_RESTRUCTURING_MERGER_RATIO_MINORITY_SHAREHOLDER_RISK
case_role = counterexample
trigger_date = 2024-07-11
entry_date = 2024-07-12
entry_price = 51,500
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/241/241560/2024.csv` and `2025.csv`:

```text
2024-07-12,51500,59500,49850,54600
2024-07-25,47000,47950,41150,44150
2024-08-05,38400,38700,33350,34250
2025-01-24,49550,53400,48900,52500
```

### Backtest

```text
MFE_30D  = +15.53%
MAE_30D  = -35.24%
MFE_90D  = +15.53%
MAE_90D  = -35.24%
MFE_180D = +15.53%
MAE_180D = -35.24%
peak_180 = 59,500 on 2024-07-12
trough_180 = 33,350 on 2024-08-05
peak_to_later_drawdown = -43.95%
```

### Interpretation

This is the operating-subsidiary minority-risk row.  
A price-only model may call the first day a control premium. The later path says the market quickly repriced merger-ratio and minority treatment risk.

The C32 rule should mark this as:

```text
local 4B-watch / false Stage2
```

unless the transaction terms are revised in a way that protects minority economics.

---

## Case 2 — Counterexample / local 4B: 454910 / 두산로보틱스

### Evidence status

```text
event source = non-proxy
company-level earnings / closing / valuation bridge = evidence_url_pending
```

```text
evidence_family = DOOSAN_ROBOTICS_RESTRUCTURING_CONTROL_VALUE_BETA_WITH_WEAK_EARNINGS_BRIDGE
case_role = counterexample
trigger_date = 2024-07-11
entry_date = 2024-07-12
entry_price = 95,000
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/454/454910/2024.csv` and `2025.csv`:

```text
2024-07-12,95000,109300,92200,105700
2024-08-05,66600,66700,53900,59300
2025-02-18,69800,77000,69100,76300
2025-04-09,39550,41700,39550,40300
```

### Backtest

```text
MFE_30D  = +15.05%
MAE_30D  = -43.26%
MFE_90D  = +15.05%
MAE_90D  = -43.26%
MFE_180D = +15.05%
MAE_180D = -58.37%
peak_180 = 109,300 on 2024-07-12
trough_180 = 39,550 on 2025-04-09
peak_to_later_drawdown = -63.82%
```

### Interpretation

This is the acquirer/beneficiary valuation-beta failure.  
If the restructuring implies control value but the earnings and closing bridge is weak, the first MFE can still become a trap.

C32 should cap this kind of acquirer beta:

```text
no verified economics → local 4B-watch
no hard 4C without non-price business break
```

---

## Case 3 — Delayed positive with early local 4B: 000150 / 두산

### Evidence status

```text
event source = non-proxy
holding-company beneficiary economics / execution bridge = evidence_url_pending
```

```text
evidence_family = DOOSAN_HOLDCO_CONTROL_PREMIUM_RESTRUCTURING_OPTION_VALUE_WITH_EARLY_EXECUTION_RISK
case_role = delayed_positive_with_early_local4b
trigger_date = 2024-07-11
entry_date = 2024-07-12
entry_price = 263,500
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/000/000150/2024.csv` and `2025.csv`:

```text
2024-07-12,263500,263500,221000,237000
2024-08-05,142200,143000,122000,128100
2025-02-26,367000,386000,360500,367500
2025-04-07,246500,250000,236500,239500
```

### Backtest

```text
MFE_30D  = +0.00%
MAE_30D  = -53.70%
MFE_90D  = +0.00%
MAE_90D  = -53.70%
MFE_180D = +46.49%
MAE_180D = -53.70%
peak_180 = 386,000 on 2025-02-26
trough_180 = 122,000 on 2024-08-05
peak_to_later_drawdown = -38.73%
```

### Interpretation

This is the nuanced C32 row.

The event-entry was bad: early MAE was enormous.  
But the holding company later produced a delayed control-premium rerating.

C32 should therefore avoid two errors:

```text
1. Do not call the initial governance headline Green.
2. Do not overblock the holding-company beneficiary if later execution/option value evidence becomes real.
```

This should be a delayed Stage2 candidate only after source repair, with early local 4B risk acknowledged.

---

## Cross-case residual finding

### What this strengthens

```text
price_only_blowoff_blocks_positive_stage = strengthen
full_4b_requires_non_price_evidence = keep
local_4b_watch_guard = strengthen
stage2_required_bridge = strengthen
```

### What this does not justify

```text
do_not_raise_generic_C32_restructuring_weight = true
do_not_treat_restructuring_headline_as_Green_without_economic_beneficiary_bridge = true
do_not_apply_same_label_to_subsidiary_acquirer_and_holdco = true
do_not_convert_governance_drawdown_to_hard_4C_without_non_price_business_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
DOOSAN_RESTRUCTURING_MERGER_RATIO_CONTROL_PREMIUM_VS_MINORITY_EXECUTION_RISK
```

This fine archetype covers:

```text
1. operating subsidiary merger-ratio/minority risk → false Stage2 / local 4B
2. acquirer/beneficiary valuation beta without earnings bridge → false Stage2 / local 4B
3. holding-company delayed control-premium option value → delayed Stage2 only after source repair
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R12L73-C32-241560-DOOSANBOBCAT-MERGER-RATIO-MINORITY-RISK", "symbol": "241560", "company_name": "두산밥캣", "round": "R12", "loop": "73", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "DOOSAN_RESTRUCTURING_MERGER_RATIO_CONTROL_PREMIUM_VS_MINORITY_EXECUTION_RISK", "case_type": "governance_control_premium_restructuring_merger_ratio", "positive_or_counterexample": "counterexample", "best_trigger": "Stage4B-Local-MergerRatioMinorityRisk", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.7, "score_price_alignment": "C32 should not treat a chaebol restructuring headline as positive control-premium evidence for the operating subsidiary when merger-ratio and minority-shareholder dilution risk dominate. Bobcat showed a brief squeeze but then opened deep MAE.", "current_profile_verdict": "company_level_execution_closing_bridge_source_repair_required", "price_source": "Songdaiki/stock-web", "notes": "Event source is non-proxy, but company-level closing, merger-ratio, shareholder-approval, cancellation/revision and intrinsic-value bridge require source repair."}
{"row_type": "case", "case_id": "R12L73-C32-454910-DOOSANROBOTICS-VALUATION-BETA-LOCAL4B", "symbol": "454910", "company_name": "두산로보틱스", "round": "R12", "loop": "73", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "DOOSAN_RESTRUCTURING_MERGER_RATIO_CONTROL_PREMIUM_VS_MINORITY_EXECUTION_RISK", "case_type": "governance_control_premium_restructuring_merger_ratio", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / RoboticsMergerValuationBeta", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.7, "score_price_alignment": "C32 should cap the acquirer/beneficiary valuation beta when the proposed restructuring implies control benefit but no earnings or closing bridge. Doosan Robotics had a large first-day MFE and then severe MAE, so price-only governance beta should be local 4B-watch.", "current_profile_verdict": "company_level_execution_closing_bridge_source_repair_required", "price_source": "Songdaiki/stock-web", "notes": "Event source is non-proxy, but company-level closing, merger-ratio, shareholder-approval, cancellation/revision and intrinsic-value bridge require source repair."}
{"row_type": "case", "case_id": "R12L73-C32-000150-DOOSAN-HOLDCO-DELAYED-CONTROL-PREMIUM", "symbol": "000150", "company_name": "두산", "round": "R12", "loop": "73", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "DOOSAN_RESTRUCTURING_MERGER_RATIO_CONTROL_PREMIUM_VS_MINORITY_EXECUTION_RISK", "case_type": "governance_control_premium_restructuring_merger_ratio", "positive_or_counterexample": "delayed_positive", "best_trigger": "Stage2-DelayedPositive / HoldcoControlPremiumAfterEarly4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.7, "score_price_alignment": "C32 should not blindly block the holding company if control-premium option value later becomes visible, but the entry cannot be pure event chase because early MAE was severe. Doosan is a delayed positive with early local 4B risk and later lifecycle drawdown.", "current_profile_verdict": "company_level_execution_closing_bridge_source_repair_required", "price_source": "Songdaiki/stock-web", "notes": "Event source is non-proxy, but company-level closing, merger-ratio, shareholder-approval, cancellation/revision and intrinsic-value bridge require source repair."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R12L73-C32-241560-DOOSANBOBCAT-MERGER-RATIO-MINORITY-RISK", "case_id": "R12L73-C32-241560-DOOSANBOBCAT-MERGER-RATIO-MINORITY-RISK", "symbol": "241560", "company_name": "두산밥캣", "round": "R12", "loop": "73", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "DOOSAN_RESTRUCTURING_MERGER_RATIO_CONTROL_PREMIUM_VS_MINORITY_EXECUTION_RISK", "loop_objective": "governance_restructuring_lifecycle_test|counterexample_mining|4B_non_price_requirement_stress_test", "trigger_type": "Stage4B-Local-MergerRatioMinorityRisk", "trigger_date": "2024-07-11", "entry_date": "2024-07-12", "entry_price": 51500.0, "evidence_available_at_that_date": "DOOSAN_BOBCAT_ROBOTICS_RESTRUCTURING_MERGER_RATIO_MINORITY_SHAREHOLDER_RISK", "evidence_source": "https://www.ft.com/content/ef858c18-dede-4927-b36d-3ccef9abb135", "stage2_evidence_fields": ["governance_event", "restructuring", "control_premium_or_merger_ratio_attention"], "stage3_evidence_fields": ["relative_strength", "execution_or_closing_bridge_candidate"], "stage4b_evidence_fields": ["merger_ratio_risk", "minority_shareholder_risk", "post_peak_drawdown", "early_MAE"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/241/241560/2024.csv", "profile_path": "atlas/symbol_profiles/241/241560.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 15.53, "MFE_90D_pct": 15.53, "MFE_180D_pct": 15.53, "MAE_30D_pct": -35.24, "MAE_90D_pct": -35.24, "MAE_180D_pct": -35.24, "peak_date": "2024-07-12", "peak_price": 59500.0, "drawdown_after_peak_pct": -43.95, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_merger_ratio_or_execution_risk_opens", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_deal_failure_shareholder_rejection_or_closing_break", "trigger_outcome_label": "counterexample", "current_profile_verdict": "C32 should not treat a chaebol restructuring headline as positive control-premium evidence for the operating subsidiary when merger-ratio and minority-shareholder dilution risk dominate. Bobcat showed a brief squeeze but then opened deep MAE.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C32_DOOSAN_RESTRUCTURING_20240712_GROUP", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.7, "do_not_count_as_new_case": false, "source_proxy_only": false, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R12L73-C32-454910-DOOSANROBOTICS-VALUATION-BETA-LOCAL4B", "case_id": "R12L73-C32-454910-DOOSANROBOTICS-VALUATION-BETA-LOCAL4B", "symbol": "454910", "company_name": "두산로보틱스", "round": "R12", "loop": "73", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "DOOSAN_RESTRUCTURING_MERGER_RATIO_CONTROL_PREMIUM_VS_MINORITY_EXECUTION_RISK", "loop_objective": "governance_restructuring_lifecycle_test|counterexample_mining|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-FalsePositive / RoboticsMergerValuationBeta", "trigger_date": "2024-07-11", "entry_date": "2024-07-12", "entry_price": 95000.0, "evidence_available_at_that_date": "DOOSAN_ROBOTICS_RESTRUCTURING_CONTROL_VALUE_BETA_WITH_WEAK_EARNINGS_BRIDGE", "evidence_source": "https://www.ft.com/content/ef858c18-dede-4927-b36d-3ccef9abb135", "stage2_evidence_fields": ["governance_event", "restructuring", "control_premium_or_merger_ratio_attention"], "stage3_evidence_fields": ["relative_strength", "execution_or_closing_bridge_candidate"], "stage4b_evidence_fields": ["merger_ratio_risk", "minority_shareholder_risk", "post_peak_drawdown", "early_MAE"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/454/454910/2024.csv", "profile_path": "atlas/symbol_profiles/454/454910.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 15.05, "MFE_90D_pct": 15.05, "MFE_180D_pct": 15.05, "MAE_30D_pct": -43.26, "MAE_90D_pct": -43.26, "MAE_180D_pct": -58.37, "peak_date": "2024-07-12", "peak_price": 109300.0, "drawdown_after_peak_pct": -63.82, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_merger_ratio_or_execution_risk_opens", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_deal_failure_shareholder_rejection_or_closing_break", "trigger_outcome_label": "counterexample", "current_profile_verdict": "C32 should cap the acquirer/beneficiary valuation beta when the proposed restructuring implies control benefit but no earnings or closing bridge. Doosan Robotics had a large first-day MFE and then severe MAE, so price-only governance beta should be local 4B-watch.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C32_DOOSAN_RESTRUCTURING_20240712_GROUP", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.7, "do_not_count_as_new_case": false, "source_proxy_only": false, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R12L73-C32-000150-DOOSAN-HOLDCO-DELAYED-CONTROL-PREMIUM", "case_id": "R12L73-C32-000150-DOOSAN-HOLDCO-DELAYED-CONTROL-PREMIUM", "symbol": "000150", "company_name": "두산", "round": "R12", "loop": "73", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "DOOSAN_RESTRUCTURING_MERGER_RATIO_CONTROL_PREMIUM_VS_MINORITY_EXECUTION_RISK", "loop_objective": "governance_restructuring_lifecycle_test|counterexample_mining|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-DelayedPositive / HoldcoControlPremiumAfterEarly4B", "trigger_date": "2024-07-11", "entry_date": "2024-07-12", "entry_price": 263500.0, "evidence_available_at_that_date": "DOOSAN_HOLDCO_CONTROL_PREMIUM_RESTRUCTURING_OPTION_VALUE_WITH_EARLY_EXECUTION_RISK", "evidence_source": "https://www.ft.com/content/ef858c18-dede-4927-b36d-3ccef9abb135", "stage2_evidence_fields": ["governance_event", "restructuring", "control_premium_or_merger_ratio_attention"], "stage3_evidence_fields": ["relative_strength", "execution_or_closing_bridge_candidate"], "stage4b_evidence_fields": ["merger_ratio_risk", "minority_shareholder_risk", "post_peak_drawdown", "early_MAE"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000150/2024.csv", "profile_path": "atlas/symbol_profiles/000/000150.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 0.0, "MFE_90D_pct": 0.0, "MFE_180D_pct": 46.49, "MAE_30D_pct": -53.7, "MAE_90D_pct": -53.7, "MAE_180D_pct": -53.7, "peak_date": "2025-02-26", "peak_price": 386000.0, "drawdown_after_peak_pct": -38.73, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_merger_ratio_or_execution_risk_opens", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_deal_failure_shareholder_rejection_or_closing_break", "trigger_outcome_label": "delayed_positive_with_early_local4b", "current_profile_verdict": "C32 should not blindly block the holding company if control-premium option value later becomes visible, but the entry cannot be pure event chase because early MAE was severe. Doosan is a delayed positive with early local 4B risk and later lifecycle drawdown.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C32_DOOSAN_RESTRUCTURING_20240712_GROUP", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.7, "do_not_count_as_new_case": false, "source_proxy_only": false, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L73-C32-241560-DOOSANBOBCAT-MERGER-RATIO-MINORITY-RISK", "trigger_id": "TRG_R12L73-C32-241560-DOOSANBOBCAT-MERGER-RATIO-MINORITY-RISK", "symbol": "241560", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"governance_event_score": 15, "control_premium_score": 8, "tender_or_closing_score": 2, "merger_ratio_risk_score": 14, "minority_shareholder_risk_score": 16, "relative_strength_score": 5, "execution_risk_score": 15, "valuation_repricing_score": 6, "source_confidence_score": 3}, "weighted_score_before": 60, "stage_label_before": "Stage2-Watch / governance restructuring beta", "raw_component_scores_after": {"governance_event_score": 8, "control_premium_score": 6, "tender_or_closing_score": 1, "merger_ratio_risk_score": 18, "minority_shareholder_risk_score": 18, "relative_strength_score": 4, "execution_risk_score": 18, "valuation_repricing_score": 4, "source_confidence_score": 3}, "weighted_score_after": 44, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["control_premium_score", "merger_ratio_risk_score", "minority_shareholder_risk_score", "execution_risk_score"], "component_delta_explanation": "Governance restructuring should be capped unless merger ratio, minority treatment, shareholder approval, closing path, and beneficiary economics are verified.", "MFE_90D_pct": 15.53, "MAE_90D_pct": -35.24, "score_return_alignment_label": "restructuring_false_positive", "current_profile_verdict": "C32 should not treat a chaebol restructuring headline as positive control-premium evidence for the operating subsidiary when merger-ratio and minority-shareholder dilution risk dominate. Bobcat showed a brief squeeze but then opened deep MAE."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L73-C32-454910-DOOSANROBOTICS-VALUATION-BETA-LOCAL4B", "trigger_id": "TRG_R12L73-C32-454910-DOOSANROBOTICS-VALUATION-BETA-LOCAL4B", "symbol": "454910", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"governance_event_score": 15, "control_premium_score": 8, "tender_or_closing_score": 2, "merger_ratio_risk_score": 14, "minority_shareholder_risk_score": 10, "relative_strength_score": 5, "execution_risk_score": 15, "valuation_repricing_score": 6, "source_confidence_score": 3}, "weighted_score_before": 60, "stage_label_before": "Stage2-Watch / governance restructuring beta", "raw_component_scores_after": {"governance_event_score": 8, "control_premium_score": 6, "tender_or_closing_score": 1, "merger_ratio_risk_score": 18, "minority_shareholder_risk_score": 12, "relative_strength_score": 4, "execution_risk_score": 18, "valuation_repricing_score": 4, "source_confidence_score": 3}, "weighted_score_after": 44, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["control_premium_score", "merger_ratio_risk_score", "minority_shareholder_risk_score", "execution_risk_score"], "component_delta_explanation": "Governance restructuring should be capped unless merger ratio, minority treatment, shareholder approval, closing path, and beneficiary economics are verified.", "MFE_90D_pct": 15.05, "MAE_90D_pct": -43.26, "score_return_alignment_label": "restructuring_false_positive", "current_profile_verdict": "C32 should cap the acquirer/beneficiary valuation beta when the proposed restructuring implies control benefit but no earnings or closing bridge. Doosan Robotics had a large first-day MFE and then severe MAE, so price-only governance beta should be local 4B-watch."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L73-C32-000150-DOOSAN-HOLDCO-DELAYED-CONTROL-PREMIUM", "trigger_id": "TRG_R12L73-C32-000150-DOOSAN-HOLDCO-DELAYED-CONTROL-PREMIUM", "symbol": "000150", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"governance_event_score": 15, "control_premium_score": 13, "tender_or_closing_score": 2, "merger_ratio_risk_score": 10, "minority_shareholder_risk_score": 10, "relative_strength_score": 10, "execution_risk_score": 15, "valuation_repricing_score": 12, "source_confidence_score": 3}, "weighted_score_before": 72, "stage_label_before": "Stage2-Watch / governance restructuring beta", "raw_component_scores_after": {"governance_event_score": 8, "control_premium_score": 14, "tender_or_closing_score": 1, "merger_ratio_risk_score": 12, "minority_shareholder_risk_score": 12, "relative_strength_score": 12, "execution_risk_score": 14, "valuation_repricing_score": 13, "source_confidence_score": 3}, "weighted_score_after": 76, "stage_label_after": "Delayed Stage2 candidate after source repair + early local 4B", "changed_components": ["control_premium_score", "merger_ratio_risk_score", "minority_shareholder_risk_score", "execution_risk_score"], "component_delta_explanation": "Governance restructuring should be capped unless merger ratio, minority treatment, shareholder approval, closing path, and beneficiary economics are verified.", "MFE_90D_pct": 0.0, "MAE_90D_pct": -53.7, "score_return_alignment_label": "delayed_holdco_control_premium_after_early_mae", "current_profile_verdict": "C32 should not blindly block the holding company if control-premium option value later becomes visible, but the entry cannot be pure event chase because early MAE was severe. Doosan is a delayed positive with early local 4B risk and later lifecycle drawdown."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R12", "loop": 73, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "DOOSAN_RESTRUCTURING_MERGER_RATIO_CONTROL_PREMIUM_VS_MINORITY_EXECUTION_RISK", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 1, "positive_case_count": 1, "counterexample_count": 2, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 0, "evidence_url_pending_count": 3, "current_profile_error_count": 3, "diversity_score_summary": "+3 underused C32 Doosan-restructuring symbols, +1 merger-ratio/control-premium trigger family, +2 merger-ratio/valuation beta false positives, +1 delayed holdco control-premium path, no hard duplicate", "residual_contribution_label": "canonical_archetype_rule_candidate_with_execution_bridge_source_repair"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R12", "loop": 73, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "axis": "doosan_restructuring_merger_ratio_control_premium_vs_minority_execution_risk", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C32 should split governance restructuring by shareholder class and economic beneficiary. Operating subsidiaries can be local 4B when merger-ratio/minority treatment risk dominates. Holding-company control premium can be delayed-positive only after execution evidence and beneficiary economics are verified. No generic Green from restructuring headlines.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["241560", "454910", "000150"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R12", "loop": 73, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "existing_axis_strengthened": ["price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "local_4b_watch_guard", "stage2_required_bridge"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C32 should not treat restructuring headlines as one-size-fits-all control premium. Doosan Bobcat and Doosan Robotics show merger-ratio/minority/valuation beta failure; Doosan holdco shows delayed control-premium option value after severe early MAE. Source repair is required before runtime promotion."}
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
241560:
  corporate_action_candidate_dates = none
  selected window = 2024-07-12~D+180
  contamination = false

454910:
  corporate_action_candidate_dates = none
  selected window = 2024-07-12~D+180
  contamination = false

000150:
  corporate_action_candidate_dates = 1997-10-22, 1998-10-09, 1999-12-03
  selected window = 2024-07-12~D+180
  contamination = false
```

Data-quality caveat:

```text
The restructuring event source is non-proxy.
Company-level closing, merger-ratio, minority-treatment and beneficiary-economics bridge still require source repair.
This MD is useful for stock-web path calibration and C32 rule-shape discovery,
but coding-agent promotion requires non-proxy transaction and shareholder-treatment evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R12/C32 artifact is marked do_not_propose_new_weight_delta=true because company-level execution bridge evidence needs source repair.

Candidate axis:
doosan_restructuring_merger_ratio_control_premium_vs_minority_execution_risk

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy transaction source URLs for 241560, 454910 and 000150.
4. Keep generic C32 restructuring weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - transaction mechanics are explicit,
   - shareholder approval or closing path is credible,
   - economic beneficiary is clear by listed entity,
   - merger ratio / minority treatment risk is not dominant,
   - MAE remains controlled or the signal is deliberately delayed after early local 4B risk.
6. Consider local 4B-watch when:
   - the trigger is restructuring or control-premium headline only,
   - MAE_30D or MAE_90D opens sharply,
   - merger-ratio/minority-treatment risk dominates,
   - post-peak drawdown <= -35%.
7. Do not apply the same label to operating subsidiary, acquirer/beneficiary and holding company.
8. Do not convert local 4B-watch into hard 4C without non-price business deterioration, deal failure, legal break, or insolvency evidence.
9. Emit before/after diagnostics and reject if verified delayed holding-company positives are overblocked.
```

---

## Final round state

```text
completed_round = R12
completed_loop = 73
next_round = R13
next_loop = 73
round_schedule_status = valid
round_sector_consistency = pass
```

