# E2R Stock-Web v12 Residual Research — R12 Loop 74 / L10 / C32

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R12",
  "scheduled_loop": 74,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R12",
  "completed_loop": 74,
  "computed_next_round": "R13",
  "computed_next_loop": 74,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP",
  "fine_archetype_id": "CONTROL_TRANSFER_PRIVATIZATION_AIRLINE_STAKE_DISPUTE_ECONOMIC_BENEFICIARY_BRIDGE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "governance_event_lifecycle_test",
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

Previous completed state in this interactive run: R11 / loop 74.

Therefore:

```text
scheduled_round = R12
scheduled_loop = 74
allowed_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC or under-covered service/agri
selected_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
selected_canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
computed_next_round = R13
computed_next_loop = 74
```

R12 was routed to C32 because this is a governance / control-transfer / tender-cap lifecycle test, not a sector operating-leverage round.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C32 is concentrated in:

```text
010130, 041510, 000240, 고려아연, 에스엠
```

This run uses three different symbols:

```text
003920 / 남양유업 / control-transfer premium cap
040300 / YTN / privatization control-sale fade
091810 / 티웨이항공 / airline control-premium dispute lifecycle
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
003920 has a 2024-11-20 corporate-action candidate, but the selected Jan-2024 180-trading-day window is kept before that area; extended validation must not cross the 2024-11-20 action without adjustment.
```

## Research thesis

C32 is not “control headline went up.”

The mechanism must identify the listed shareholder's economic seat:

```text
control-transfer or stake event
→ tender / closing / minority economics
→ listed-entity beneficiary bridge
→ operating or capital policy bridge
→ durable rerating
```

A control headline is a door opening in the boardroom.  
The question is whether minority shareholders are invited through the door or left in the hallway.

---

## Case 1 — Counterexample / premium cap: 003920 / 남양유업

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is control-transfer resolution, tender/minority economics, capital policy and operating turnaround evidence.

```text
evidence_family = CONTROL_TRANSFER_DISPUTE_RESOLUTION_WITH_WEAK_OPERATIONAL_OR_TENDER_PREMIUM_BRIDGE
case_role = counterexample_control_transfer_cap
trigger_date = 2024-01-04
entry_date = 2024-01-05
entry_price = 616,000
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/003/003920/2024.csv`:

```text
2024-01-05,616000,645000,597000,605000
2024-02-19,580000,632000,576000,620000
2024-04-08,526000,526000,499000,502000
2024-08-05,488000,504000,472000,475000
2024-09-10,555000,581000,510000,529000
```

### Backtest

```text
MFE_30D  = +4.71%
MAE_30D  = -10.71%
MFE_90D  = +4.71%
MAE_90D  = -18.99%
MFE_180D = +4.71%
MAE_180D = -23.38%
peak_180 = 645,000 on 2024-01-05
trough_180 = 472,000 on 2024-08-05
peak_to_later_drawdown = -26.82%
```

### Interpretation

This is a C32 premium-cap counterexample.  
The legal/control-transfer event was real, but the stock-web path did not confirm a durable minority-shareholder rerating.

The rule should require:

```text
tender floor
minority economics
capital policy
or operating turnaround bridge
```

before Stage2/Green.

---

## Case 2 — Counterexample / local 4B: 040300 / YTN

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is privatization closing certainty, tender/minority economics, governance plan and earnings bridge evidence.

```text
evidence_family = MEDIA_PRIVATIZATION_CONTROL_SALE_HEADLINE_WITH_WEAK_MINORITIY_PREMIUM_OR_EARNINGS_BRIDGE
case_role = counterexample_privatization_sale_cap
trigger_date = 2024-02-04
entry_date = 2024-02-05
entry_price = 5,630
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/040/040300/2024.csv`:

```text
2024-02-05,5630,6220,5630,5840
2024-02-07,6170,6580,5610,5670
2024-04-12,4060,4080,3955,3960
2024-08-05,3345,3350,2525,2765
2024-09-30,3350,3880,3335,3570
```

### Backtest

```text
MFE_30D  = +16.87%
MAE_30D  = -13.77%
MFE_90D  = +16.87%
MAE_90D  = -29.75%
MFE_180D = +16.87%
MAE_180D = -55.15%
peak_180 = 6,580 on 2024-02-07
trough_180 = 2,525 on 2024-08-05
peak_to_later_drawdown = -61.63%
```

### Interpretation

This is the privatization/control-sale false-positive shape.  
The market bought the headline. The bridge did not hold.

C32 should route this to local 4B-watch unless actual minority economics, tender terms, earnings bridge or post-closing capital policy is visible.

---

## Case 3 — Delayed positive with lifecycle 4B: 091810 / 티웨이항공

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is stake accumulation, management-rights pressure, route/capacity economics, capital structure and listed-entity beneficiary bridge evidence.

```text
evidence_family = AIRLINE_STAKE_ACCUMULATION_CONTROL_PREMIUM_DISPUTE_ROUTE_CAPACITY_EXECUTION_BRIDGE
case_role = delayed_positive_with_later_4b_watch
trigger_date = 2024-08-26
entry_date = 2024-08-27
entry_price = 2,725
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/091/091810/2024.csv` and `2025.csv`:

```text
2024-08-27,2725,2790,2710,2785
2024-09-20,2985,3300,2950,3295
2024-10-10,3680,3990,3320,3770
2025-01-31,4125,4500,3830,3900
2025-04-09,1993,2015,1935,1935
```

### Backtest

```text
MFE_30D  = +42.39%
MAE_30D  = -0.55%
MFE_90D  = +46.42%
MAE_90D  = -0.55%
MFE_180D = +65.14%
MAE_180D = -28.99%
peak_180 = 4,500 on 2025-01-31
trough_180 = 1,935 on 2025-04-09
peak_to_later_drawdown = -57.00%
```

### Interpretation

This is the useful C32 positive side.  
The control-premium dispute / stake-accumulation story created a real MFE path. But it was not a permanent Green: after the January peak, the drawdown became severe.

Correct treatment:

```text
economic beneficiary bridge verified → delayed Stage2 possible
bridge stale or execution risk opens → lifecycle local 4B-watch
```

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
do_not_raise_generic_C32_governance_weight = true
do_not_treat_control_transfer_headline_as_Green_without_minority_economics = true
do_not_apply_same_label_to_control_seller_acquirer_and_minorities = true
do_not_convert_governance_drawdown_to_hard_4C_without_non_price_business_or_deal_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
CONTROL_TRANSFER_PRIVATIZATION_AIRLINE_STAKE_DISPUTE_ECONOMIC_BENEFICIARY_BRIDGE
```

This fine archetype covers:

```text
1. control-transfer legal resolution without tender/operating bridge → false Stage2 / premium cap
2. privatization control-sale headline without minority/earnings bridge → false Stage2 / local 4B
3. airline stake/control-premium dispute with route/capacity economics → delayed Stage2 possible, later local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R12L74-C32-003920-NAMYANG-CONTROL-TRANSFER-PREMIUM-CAP", "symbol": "003920", "company_name": "남양유업", "round": "R12", "loop": "74", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_TRANSFER_PRIVATIZATION_AIRLINE_STAKE_DISPUTE_ECONOMIC_BENEFICIARY_BRIDGE", "case_type": "governance_control_premium_tender_cap", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / ControlTransferPremiumCap", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C32 should not treat legal/control-transfer resolution as durable Green unless minority economics, tender floor, capital policy, operational turnaround or closing economics bridge is visible. Namyang had small MFE and persistent MAE before the later share-split/corporate-action area, so it is a control-transfer premium-cap counterexample.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy control-transfer, tender/minority economics, closing certainty, route/capacity or operating bridge required before runtime promotion."}
{"row_type": "case", "case_id": "R12L74-C32-040300-YTN-PRIVATIZATION-CONTROL-SALE-FADE", "symbol": "040300", "company_name": "YTN", "round": "R12", "loop": "74", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_TRANSFER_PRIVATIZATION_AIRLINE_STAKE_DISPUTE_ECONOMIC_BENEFICIARY_BRIDGE", "case_type": "governance_control_premium_tender_cap", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / PrivatizationControlSaleFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C32 should not treat privatization or control-sale approval as durable Stage2 unless minority tender economics, closing certainty, capital policy or earnings bridge is explicit. YTN had a short control-sale pop but then suffered high MAE and post-peak drawdown.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy control-transfer, tender/minority economics, closing certainty, route/capacity or operating bridge required before runtime promotion."}
{"row_type": "case", "case_id": "R12L74-C32-091810-TWAY-AIR-CONTROL-PREMIUM-DISPUTE-LIFECYCLE", "symbol": "091810", "company_name": "티웨이항공", "round": "R12", "loop": "74", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_TRANSFER_PRIVATIZATION_AIRLINE_STAKE_DISPUTE_ECONOMIC_BENEFICIARY_BRIDGE", "case_type": "governance_control_premium_tender_cap", "positive_or_counterexample": "delayed_positive", "best_trigger": "Stage2-DelayedPositive / AirlineControlPremiumDisputeLifecycle", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C32 should allow a delayed control-premium dispute candidate when stake accumulation, management-rights pressure and strategic airline-route economics become credible. T'way produced a large MFE into early 2025, but the later collapse requires lifecycle local 4B if control-premium or route/capacity execution evidence fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy control-transfer, tender/minority economics, closing certainty, route/capacity or operating bridge required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R12L74-C32-003920-NAMYANG-CONTROL-TRANSFER-PREMIUM-CAP", "case_id": "R12L74-C32-003920-NAMYANG-CONTROL-TRANSFER-PREMIUM-CAP", "symbol": "003920", "company_name": "남양유업", "round": "R12", "loop": "74", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_TRANSFER_PRIVATIZATION_AIRLINE_STAKE_DISPUTE_ECONOMIC_BENEFICIARY_BRIDGE", "loop_objective": "governance_event_lifecycle_test|counterexample_mining|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-FalsePositive / ControlTransferPremiumCap", "trigger_date": "2024-01-04", "entry_date": "2024-01-05", "entry_price": 616000.0, "evidence_available_at_that_date": "CONTROL_TRANSFER_DISPUTE_RESOLUTION_WITH_WEAK_OPERATIONAL_OR_TENDER_PREMIUM_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:NAMYANG_2024_CONTROL_TRANSFER_DISPUTE_RESOLUTION_TENDER_MINORITY_OPERATIONAL_BRIDGE", "stage2_evidence_fields": ["governance_event", "control_transfer_or_stake_dispute", "economic_beneficiary_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "closing_or_operating_bridge_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "minority_or_tender_cap_risk", "post_peak_drawdown", "early_MAE"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003920/2024.csv", "profile_path": "atlas/symbol_profiles/003/003920.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.71, "MFE_90D_pct": 4.71, "MFE_180D_pct": 4.71, "MAE_30D_pct": -10.71, "MAE_90D_pct": -18.99, "MAE_180D_pct": -23.38, "peak_date": "2024-01-05", "peak_price": 645000.0, "drawdown_after_peak_pct": -26.82, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_control_premium_peak_if_economic_beneficiary_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_deal_failure_minorities_tender_cap_operating_or_financing_break", "trigger_outcome_label": "counterexample_control_transfer_cap", "current_profile_verdict": "C32 should not treat legal/control-transfer resolution as durable Green unless minority economics, tender floor, capital policy, operational turnaround or closing economics bridge is visible. Namyang had small MFE and persistent MAE before the later share-split/corporate-action area, so it is a control-transfer premium-cap counterexample.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C32_GOV_003920_2024-01-05", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R12L74-C32-040300-YTN-PRIVATIZATION-CONTROL-SALE-FADE", "case_id": "R12L74-C32-040300-YTN-PRIVATIZATION-CONTROL-SALE-FADE", "symbol": "040300", "company_name": "YTN", "round": "R12", "loop": "74", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_TRANSFER_PRIVATIZATION_AIRLINE_STAKE_DISPUTE_ECONOMIC_BENEFICIARY_BRIDGE", "loop_objective": "governance_event_lifecycle_test|counterexample_mining|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-FalsePositive / PrivatizationControlSaleFade", "trigger_date": "2024-02-04", "entry_date": "2024-02-05", "entry_price": 5630.0, "evidence_available_at_that_date": "MEDIA_PRIVATIZATION_CONTROL_SALE_HEADLINE_WITH_WEAK_MINORITIY_PREMIUM_OR_EARNINGS_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:YTN_2024_PRIVATIZATION_CONTROL_SALE_APPROVAL_TENDER_EARNINGS_BRIDGE", "stage2_evidence_fields": ["governance_event", "control_transfer_or_stake_dispute", "economic_beneficiary_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "closing_or_operating_bridge_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "minority_or_tender_cap_risk", "post_peak_drawdown", "early_MAE"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/040/040300/2024.csv", "profile_path": "atlas/symbol_profiles/040/040300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 16.87, "MFE_90D_pct": 16.87, "MFE_180D_pct": 16.87, "MAE_30D_pct": -13.77, "MAE_90D_pct": -29.75, "MAE_180D_pct": -55.15, "peak_date": "2024-02-07", "peak_price": 6580.0, "drawdown_after_peak_pct": -61.63, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_control_premium_peak_if_economic_beneficiary_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_deal_failure_minorities_tender_cap_operating_or_financing_break", "trigger_outcome_label": "counterexample_privatization_sale_cap", "current_profile_verdict": "C32 should not treat privatization or control-sale approval as durable Stage2 unless minority tender economics, closing certainty, capital policy or earnings bridge is explicit. YTN had a short control-sale pop but then suffered high MAE and post-peak drawdown.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C32_GOV_040300_2024-02-05", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R12L74-C32-091810-TWAY-AIR-CONTROL-PREMIUM-DISPUTE-LIFECYCLE", "case_id": "R12L74-C32-091810-TWAY-AIR-CONTROL-PREMIUM-DISPUTE-LIFECYCLE", "symbol": "091810", "company_name": "티웨이항공", "round": "R12", "loop": "74", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_TRANSFER_PRIVATIZATION_AIRLINE_STAKE_DISPUTE_ECONOMIC_BENEFICIARY_BRIDGE", "loop_objective": "governance_event_lifecycle_test|counterexample_mining|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-DelayedPositive / AirlineControlPremiumDisputeLifecycle", "trigger_date": "2024-08-26", "entry_date": "2024-08-27", "entry_price": 2725.0, "evidence_available_at_that_date": "AIRLINE_STAKE_ACCUMULATION_CONTROL_PREMIUM_DISPUTE_ROUTE_CAPACITY_EXECUTION_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:TWAY_AIR_2024_CONTROL_PREMIUM_STAKE_ACCUMULATION_ROUTE_CAPACITY_EXECUTION_BRIDGE", "stage2_evidence_fields": ["governance_event", "control_transfer_or_stake_dispute", "economic_beneficiary_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "closing_or_operating_bridge_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "minority_or_tender_cap_risk", "post_peak_drawdown", "early_MAE"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/091/091810/2024.csv", "profile_path": "atlas/symbol_profiles/091/091810.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 42.39, "MFE_90D_pct": 46.42, "MFE_180D_pct": 65.14, "MAE_30D_pct": -0.55, "MAE_90D_pct": -0.55, "MAE_180D_pct": -28.99, "peak_date": "2025-01-31", "peak_price": 4500.0, "drawdown_after_peak_pct": -57.0, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_control_premium_peak_if_economic_beneficiary_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_deal_failure_minorities_tender_cap_operating_or_financing_break", "trigger_outcome_label": "delayed_positive_with_later_4b_watch", "current_profile_verdict": "C32 should allow a delayed control-premium dispute candidate when stake accumulation, management-rights pressure and strategic airline-route economics become credible. T'way produced a large MFE into early 2025, but the later collapse requires lifecycle local 4B if control-premium or route/capacity execution evidence fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C32_GOV_091810_2024-08-27", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L74-C32-003920-NAMYANG-CONTROL-TRANSFER-PREMIUM-CAP", "trigger_id": "TRG_R12L74-C32-003920-NAMYANG-CONTROL-TRANSFER-PREMIUM-CAP", "symbol": "003920", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"governance_event_score": 15, "control_premium_score": 7, "tender_or_closing_score": 3, "minority_economics_score": 4, "operating_bridge_score": 2, "relative_strength_score": 5, "execution_risk_score": 15, "valuation_repricing_score": 5, "source_confidence_score": 2}, "weighted_score_before": 52, "stage_label_before": "Stage2-Watch / governance beta", "raw_component_scores_after": {"governance_event_score": 8, "control_premium_score": 4, "tender_or_closing_score": 2, "minority_economics_score": 3, "operating_bridge_score": 1, "relative_strength_score": 3, "execution_risk_score": 18, "valuation_repricing_score": 4, "source_confidence_score": 2}, "weighted_score_after": 42, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["control_premium_score", "tender_or_closing_score", "minority_economics_score", "operating_bridge_score", "execution_risk_score"], "component_delta_explanation": "Governance events should be capped unless tender/minority economics, closing certainty, route/capacity or operating beneficiary bridge is verified.", "MFE_90D_pct": 4.71, "MAE_90D_pct": -18.99, "score_return_alignment_label": "governance_event_false_positive_tender_cap", "current_profile_verdict": "C32 should not treat legal/control-transfer resolution as durable Green unless minority economics, tender floor, capital policy, operational turnaround or closing economics bridge is visible. Namyang had small MFE and persistent MAE before the later share-split/corporate-action area, so it is a control-transfer premium-cap counterexample."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L74-C32-040300-YTN-PRIVATIZATION-CONTROL-SALE-FADE", "trigger_id": "TRG_R12L74-C32-040300-YTN-PRIVATIZATION-CONTROL-SALE-FADE", "symbol": "040300", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"governance_event_score": 15, "control_premium_score": 7, "tender_or_closing_score": 3, "minority_economics_score": 2, "operating_bridge_score": 2, "relative_strength_score": 5, "execution_risk_score": 15, "valuation_repricing_score": 5, "source_confidence_score": 2}, "weighted_score_before": 52, "stage_label_before": "Stage2-Watch / governance beta", "raw_component_scores_after": {"governance_event_score": 8, "control_premium_score": 4, "tender_or_closing_score": 2, "minority_economics_score": 1, "operating_bridge_score": 1, "relative_strength_score": 3, "execution_risk_score": 18, "valuation_repricing_score": 4, "source_confidence_score": 2}, "weighted_score_after": 42, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["control_premium_score", "tender_or_closing_score", "minority_economics_score", "operating_bridge_score", "execution_risk_score"], "component_delta_explanation": "Governance events should be capped unless tender/minority economics, closing certainty, route/capacity or operating beneficiary bridge is verified.", "MFE_90D_pct": 16.87, "MAE_90D_pct": -29.75, "score_return_alignment_label": "governance_event_false_positive_tender_cap", "current_profile_verdict": "C32 should not treat privatization or control-sale approval as durable Stage2 unless minority tender economics, closing certainty, capital policy or earnings bridge is explicit. YTN had a short control-sale pop but then suffered high MAE and post-peak drawdown."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L74-C32-091810-TWAY-AIR-CONTROL-PREMIUM-DISPUTE-LIFECYCLE", "trigger_id": "TRG_R12L74-C32-091810-TWAY-AIR-CONTROL-PREMIUM-DISPUTE-LIFECYCLE", "symbol": "091810", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"governance_event_score": 15, "control_premium_score": 12, "tender_or_closing_score": 3, "minority_economics_score": 2, "operating_bridge_score": 9, "relative_strength_score": 13, "execution_risk_score": 15, "valuation_repricing_score": 12, "source_confidence_score": 2}, "weighted_score_before": 72, "stage_label_before": "Stage2-Watch / governance beta", "raw_component_scores_after": {"governance_event_score": 8, "control_premium_score": 15, "tender_or_closing_score": 2, "minority_economics_score": 1, "operating_bridge_score": 11, "relative_strength_score": 12, "execution_risk_score": 15, "valuation_repricing_score": 13, "source_confidence_score": 2}, "weighted_score_after": 78, "stage_label_after": "Delayed Stage2 candidate after source repair + lifecycle local 4B", "changed_components": ["control_premium_score", "tender_or_closing_score", "minority_economics_score", "operating_bridge_score", "execution_risk_score"], "component_delta_explanation": "Governance events should be capped unless tender/minority economics, closing certainty, route/capacity or operating beneficiary bridge is verified.", "MFE_90D_pct": 46.42, "MAE_90D_pct": -0.55, "score_return_alignment_label": "delayed_control_premium_positive_with_lifecycle_4b", "current_profile_verdict": "C32 should allow a delayed control-premium dispute candidate when stake accumulation, management-rights pressure and strategic airline-route economics become credible. T'way produced a large MFE into early 2025, but the later collapse requires lifecycle local 4B if control-premium or route/capacity execution evidence fades."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R12", "loop": 74, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_TRANSFER_PRIVATIZATION_AIRLINE_STAKE_DISPUTE_ECONOMIC_BENEFICIARY_BRIDGE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "current_profile_error_count": 2, "diversity_score_summary": "+3 underused C32 governance/control-transfer symbols, +3 control-transfer/privatization/airline-stake trigger families, +1 delayed control-premium positive, +2 tender/minority premium-cap false positives, no hard duplicate", "residual_contribution_label": "governance_lifecycle_guardrail_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R12", "loop": 74, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "axis": "control_transfer_privatization_airline_stake_dispute_economic_beneficiary_bridge", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C32 should split true economic-beneficiary control-premium disputes from control-transfer or privatization headline beta. Stage2 requires tender/minority economics, closing certainty, capital policy, operating bridge, route/capacity economics or clear listed-entity beneficiary. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["003920", "040300", "091810"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R12", "loop": 74, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "existing_axis_strengthened": ["price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "local_4b_watch_guard", "stage2_required_bridge"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C32 governance events need economic-beneficiary proof. Namyang and YTN show control-transfer/privatization premium caps without durable bridge; T'way Air shows a delayed control-premium dispute positive but later lifecycle local 4B when evidence fades."}
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
003920:
  corporate_action_candidate_dates = 2024-11-20
  selected window = 2024-01-05~approximately D+180 trading days
  contamination = false for measured window before the 2024-11-20 candidate
  caveat = extended validation must not cross 2024-11-20 without adjustment

040300:
  corporate_action_candidate_dates = none
  selected window = 2024-02-05~D+180
  contamination = false

091810:
  corporate_action_candidate_dates = 2020-11-27, 2022-05-12, 2023-02-23, 2025-09-15, 2026-01-13
  selected window = 2024-08-27~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C32 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C32 rule-shape discovery,
but coding-agent promotion requires non-proxy control-transfer, tender/minority economics, closing certainty, capital policy, stake accumulation, route/capacity and operating bridge evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R12/C32 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair.

Candidate axis:
control_transfer_privatization_airline_stake_dispute_economic_beneficiary_bridge

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 003920, 040300 and 091810.
4. Validate that 003920 measurement does not cross the 2024-11-20 corporate-action window without adjustment.
5. Keep generic C32 governance/control-premium weight unchanged until source repair is complete.
6. Consider Stage2 only when:
   - transaction mechanics are explicit,
   - tender/minority economics or shareholder benefit is visible,
   - closing path or stake-control path is credible,
   - economic beneficiary is clear by listed entity,
   - MAE remains controlled or the signal is deliberately delayed after an early-risk phase.
7. Consider local 4B-watch when:
   - the trigger is governance/control/privatization headline only,
   - minority/tender/operating bridge is absent or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
8. Do not apply the same label to seller, acquirer, operating company and minority shareholder.
9. Do not convert local 4B-watch into hard 4C without non-price deal failure, legal break, financing, operating deterioration or insolvency evidence.
10. Emit before/after diagnostics and reject if verified delayed control-premium positives are overblocked.
```

---

## Final round state

```text
completed_round = R12
completed_loop = 74
next_round = R13
next_loop = 74
round_schedule_status = valid
round_sector_consistency = pass
```

