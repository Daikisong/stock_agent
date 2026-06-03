# E2R Stock-Web v12 Residual Research — R12 Loop 76 / L10 / C32

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R12",
  "scheduled_loop": 76,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R12",
  "completed_loop": 76,
  "computed_next_round": "R13",
  "computed_next_loop": 76,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP",
  "fine_archetype_id": "VOLUNTARY_DELISTING_TENDER_FLOOR_MINORITY_ECONOMICS_BRIDGE_VS_TENDER_CAP_NO_FURTHER_GREEN",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "governance_event_lifecycle_test",
    "tender_floor_cap_guardrail",
    "minority_economics_direct_beneficiary_mapping",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression",
    "source_repair_queue_creation"
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

Previous completed state in this interactive run: R11 / loop 76.

Therefore:

```text
scheduled_round = R12
scheduled_loop = 76
allowed_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC or under-covered service/agri sector
selected_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
selected_canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
computed_next_round = R13
computed_next_loop = 76
```

R12 was routed to C32 because this is a governance / tender / voluntary-delisting lifecycle test, not a sector operating-leverage round.

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

This run uses three different symbols and avoids loop-75 R12 names:

```text
003410 / 쌍용C&E / voluntary-delisting tender floor
115390 / 락앤락 / tender-floor minority economics
119860 / 커넥트웨이브 / tender-floor cap / no further Green boundary
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
All three are inactive_or_delisted_like by stock-web profile, so this is an event-lifecycle study rather than live discovery.
119860 shows share-count changes inside the selected window and requires coding-agent validation before runtime promotion.
```

## Research thesis

C32 is not “governance stock went up.”

The mechanism must identify the economic seat of the listed minority shareholder:

```text
tender / voluntary delisting / control transfer
→ tender mechanics and closing certainty
→ minority economics and floor/cap terms
→ listed-entity beneficiary mapping
→ event-lifecycle exit
```

A tender headline is the auction bell.  
C32 cares whether the minority shareholder actually has a floor, a closing path, and a reason to leave once the floor is reached.

---

## Case 1 — Tender-floor lifecycle positive: 003410 / 쌍용C&E

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is tender terms, voluntary-delisting mechanics, minority floor price and closing certainty evidence.

```text
evidence_family = VOLUNTARY_DELISTING_TENDER_OFFER_MINORITY_FLOOR_CLOSING_CERTAINTY_BRIDGE
case_role = governance_tender_floor_positive_no_operating_green
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 6,030
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/003/003410/2024.csv`:

```text
2024-02-01,6030,6320,6030,6320
2024-02-05,6930,6960,6930,6940
2024-03-15,7000,7040,7000,7000
2024-04-08,7000,7010,7000,7000
profile_last_date,2024-06-20
```

### Backtest

```text
MFE_30D  = +16.75%
MAE_30D  = +0.00%
MFE_90D  = +16.75%
MAE_90D  = +0.00%
MFE_180D = +16.75%
MAE_180D = +0.00%
peak_180 = 7,040 on 2024-03-15
trough_180 = 6,030 on 2024-02-01
peak_to_later_drawdown = -0.57%
```

### Interpretation

This is a clean C32 tender-floor event.  
The price action pins near the tender floor and produces controlled-MAE MFE.

Correct treatment:

```text
tender floor / minority economics verified → event-lifecycle Stage2
after tender floor is reached → no operating Green unless separate bridge exists
```

---

## Case 2 — Tender-floor lifecycle positive: 115390 / 락앤락

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is tender-offer terms, minority economics, floor price, closing certainty and voluntary-delisting path evidence.

```text
evidence_family = VOLUNTARY_DELISTING_TENDER_OFFER_MINORITY_ECONOMICS_FLOOR_PRICE_BRIDGE
case_role = governance_tender_floor_positive_with_cap_watch
trigger_date = 2024-02-16
entry_date = 2024-02-19
entry_price = 5,920
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/115/115390/2024.csv`:

```text
2024-02-19,5920,6320,5910,6300
2024-03-18,7790,7950,7580,7950
2024-07-24,8750,8760,8750,8750
2024-08-08,8760,8790,8750,8760
2024-10-11,8630,8640,8270,8600
```

### Backtest

```text
MFE_30D  = +34.29%
MAE_30D  = -0.17%
MFE_90D  = +48.14%
MAE_90D  = -0.17%
MFE_180D = +48.48%
MAE_180D = -0.17%
peak_180 = 8,790 on 2024-08-08
trough_180 = 5,910 on 2024-02-19
peak_to_later_drawdown = -5.92%
```

### Interpretation

This is another C32 tender-floor positive.  
But it is still an event-lifecycle row, not an infinite rerating row.

Correct treatment:

```text
tender/minority floor verified → Stage2 event-lifecycle
price pinned near floor → exit/cap logic required
```

---

## Case 3 — Tender-cap boundary / no permanent Green: 119860 / 커넥트웨이브

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
source_repair_required = true
```

This row tests whether tender-floor MFE should be treated as permanent C32 Green.

```text
evidence_family = CONTROL_SHAREHOLDER_TENDER_FLOOR_CAP_WITH_LIMITED_POST_FLOOR_UPSIDE
case_role = counterexample_tender_cap_no_permanent_green
trigger_date = 2024-03-13
entry_date = 2024-03-14
entry_price = 12,250
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/119/119860/2024.csv`:

```text
2024-03-14,12250,13520,12110,13400
2024-03-18,15040,16390,14940,16290
2024-03-21,17350,17390,14010,14550
2024-07-24,17960,18010,17960,18000
2024-08-05,18000,18010,17700,17810
2024-08-13,17960,18040,17960,18040
```

### Backtest

```text
MFE_30D  = +41.96%
MAE_30D  = -1.14%
MFE_90D  = +47.10%
MAE_90D  = -1.14%
MFE_180D = +47.27%
MAE_180D = -1.14%
peak_180 = 18,040 on 2024-08-13
trough_180 = 12,110 on 2024-03-14
peak_to_later_drawdown = -1.88%
```

### Interpretation

This is not a failed trade.  
It is a failed *permanent Green* label.

The signal worked as a tender-floor event, then price pinned near the floor. C32 should mark it as event-lifecycle, not a continuing operating rerating.

Correct treatment:

```text
tender-floor MFE recognized
but no further Green after cap/floor unless separate operating bridge exists
```

---

## Cross-case residual finding

### What this strengthens

```text
price_only_blowoff_blocks_positive_stage = strengthen
full_4b_requires_non_price_evidence = keep
local_4b_watch_guard = strengthen
stage2_required_bridge = strengthen
share_count_validation_guard = strengthen
event_lifecycle_exit_guard = strengthen
```

### What this does not justify

```text
do_not_raise_generic_C32_governance_headline_weight = true
do_not_treat_tender_floor_MFE_as_permanent_Green = true
do_not_apply_same_label_to_tender_seller_acquirer_operating_company_and_minority_holder = true
do_not_convert_tender_cap_drawdown_to_hard_4C_without_deal_or_business_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
VOLUNTARY_DELISTING_TENDER_FLOOR_MINORITY_ECONOMICS_BRIDGE_VS_TENDER_CAP_NO_FURTHER_GREEN
```

This fine archetype covers:

```text
1. voluntary-delisting tender floor → event-lifecycle Stage2 after source repair
2. minority economics / floor price pinning → event-lifecycle positive with exit/cap
3. tender-floor MFE with limited post-floor upside → no permanent Green
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R12L76-C32-003410-SSANGYONGCNE-VOLUNTARY-DELISTING-TENDER-FLOOR", "symbol": "003410", "company_name": "쌍용C&E", "round": "R12", "loop": "76", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "VOLUNTARY_DELISTING_TENDER_FLOOR_MINORITY_ECONOMICS_BRIDGE_VS_TENDER_CAP_NO_FURTHER_GREEN", "case_type": "governance_control_premium_tender_cap", "positive_or_counterexample": "governance_lifecycle_positive", "best_trigger": "Stage2-GovernanceLifecycle / VoluntaryDelistingTenderFloorBridge", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C32 should allow tender-floor lifecycle candidates when minority shareholders have explicit tender mechanics, floor price, closing path and direct economic beneficiary mapping. Ssangyong C&E produced a low-MAE tender-floor move and then price pinning, but this is not an operating Green; it is a governance-event floor trade that ends when tender mechanics complete.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy tender terms, closing certainty, minority economics, floor/cap mechanics and listed-shareholder beneficiary bridge required before runtime promotion."}
{"row_type": "case", "case_id": "R12L76-C32-115390-LOCKNLOCK-VOLUNTARY-DELISTING-TENDER-FLOOR", "symbol": "115390", "company_name": "락앤락", "round": "R12", "loop": "76", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "VOLUNTARY_DELISTING_TENDER_FLOOR_MINORITY_ECONOMICS_BRIDGE_VS_TENDER_CAP_NO_FURTHER_GREEN", "case_type": "governance_control_premium_tender_cap", "positive_or_counterexample": "governance_lifecycle_positive", "best_trigger": "Stage2-GovernanceLifecycle / TenderFloorMinorityEconomicsBridge", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C32 should preserve tender-floor minority-economics positives when the listed minority shareholder is the direct beneficiary of a tender/voluntary-delisting floor. Lock&Lock showed a controlled-MAE tender rerating and then price pinning near the offer floor; C32 should treat this as event-floor lifecycle, not perpetual operating Stage2.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy tender terms, closing certainty, minority economics, floor/cap mechanics and listed-shareholder beneficiary bridge required before runtime promotion."}
{"row_type": "case", "case_id": "R12L76-C32-119860-CONNECTWAVE-TENDER-CAP-NO-FURTHER-GREEN", "symbol": "119860", "company_name": "커넥트웨이브", "round": "R12", "loop": "76", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "VOLUNTARY_DELISTING_TENDER_FLOOR_MINORITY_ECONOMICS_BRIDGE_VS_TENDER_CAP_NO_FURTHER_GREEN", "case_type": "governance_control_premium_tender_cap", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-Boundary / TenderFloorCapNoFurtherGreen", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C32 should distinguish tender-floor tradability from ongoing rerating. Connectwave produced a large controlled-MAE move into the tender/floor region and then pinned near the floor, so it is a good counterexample against treating tender-floor MFE as permanent Green.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy tender terms, closing certainty, minority economics, floor/cap mechanics and listed-shareholder beneficiary bridge required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R12L76-C32-003410-SSANGYONGCNE-VOLUNTARY-DELISTING-TENDER-FLOOR", "case_id": "R12L76-C32-003410-SSANGYONGCNE-VOLUNTARY-DELISTING-TENDER-FLOOR", "symbol": "003410", "company_name": "쌍용C&E", "round": "R12", "loop": "76", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "VOLUNTARY_DELISTING_TENDER_FLOOR_MINORITY_ECONOMICS_BRIDGE_VS_TENDER_CAP_NO_FURTHER_GREEN", "loop_objective": "governance_event_lifecycle_test|counterexample_mining|tender_floor_cap_guardrail", "trigger_type": "Stage2-GovernanceLifecycle / VoluntaryDelistingTenderFloorBridge", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 6030.0, "evidence_available_at_that_date": "VOLUNTARY_DELISTING_TENDER_OFFER_MINORITY_FLOOR_CLOSING_CERTAINTY_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:SSANGYONG_CNE_2024_VOLUNTARY_DELISTING_TENDER_OFFER_MINORITY_FLOOR_CLOSING_BRIDGE", "stage2_evidence_fields": ["tender_or_voluntary_delisting_event", "minority_economics_candidate", "floor_price_or_closing_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "tender_floor_pin_or_closing_certainty_candidate"], "stage4b_evidence_fields": ["tender_cap_no_further_green", "bridge_stale_or_absent", "sharecount_or_delisting_validation"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003410/2024.csv", "profile_path": "atlas/symbol_profiles/003/003410.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 16.75, "MFE_90D_pct": 16.75, "MFE_180D_pct": 16.75, "MAE_30D_pct": 0.0, "MAE_90D_pct": 0.0, "MAE_180D_pct": 0.0, "peak_date": "2024-03-15", "peak_price": 7040.0, "drawdown_after_peak_pct": -0.57, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_or_event_exit_after_tender_floor_when_no_additional_economic_bridge_exists", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_deal_failure_tender_revision_financing_legal_or_business_break", "trigger_outcome_label": "governance_tender_floor_positive_no_operating_green", "current_profile_verdict": "C32 should allow tender-floor lifecycle candidates when minority shareholders have explicit tender mechanics, floor price, closing path and direct economic beneficiary mapping. Ssangyong C&E produced a low-MAE tender-floor move and then price pinning, but this is not an operating Green; it is a governance-event floor trade that ends when tender mechanics complete.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_delisting_floor_event", "share_count_change_inside_window": false, "same_entry_group_id": "C32_TENDER_FLOOR_003410_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R12L76-C32-115390-LOCKNLOCK-VOLUNTARY-DELISTING-TENDER-FLOOR", "case_id": "R12L76-C32-115390-LOCKNLOCK-VOLUNTARY-DELISTING-TENDER-FLOOR", "symbol": "115390", "company_name": "락앤락", "round": "R12", "loop": "76", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "VOLUNTARY_DELISTING_TENDER_FLOOR_MINORITY_ECONOMICS_BRIDGE_VS_TENDER_CAP_NO_FURTHER_GREEN", "loop_objective": "governance_event_lifecycle_test|counterexample_mining|tender_floor_cap_guardrail", "trigger_type": "Stage2-GovernanceLifecycle / TenderFloorMinorityEconomicsBridge", "trigger_date": "2024-02-16", "entry_date": "2024-02-19", "entry_price": 5920.0, "evidence_available_at_that_date": "VOLUNTARY_DELISTING_TENDER_OFFER_MINORITY_ECONOMICS_FLOOR_PRICE_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:LOCKNLOCK_2024_TENDER_OFFER_VOLUNTARY_DELISTING_MINORITY_FLOOR_PRICE_CLOSING_BRIDGE", "stage2_evidence_fields": ["tender_or_voluntary_delisting_event", "minority_economics_candidate", "floor_price_or_closing_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "tender_floor_pin_or_closing_certainty_candidate"], "stage4b_evidence_fields": ["tender_cap_no_further_green", "bridge_stale_or_absent", "sharecount_or_delisting_validation"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/115/115390/2024.csv", "profile_path": "atlas/symbol_profiles/115/115390.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 34.29, "MFE_90D_pct": 48.14, "MFE_180D_pct": 48.48, "MAE_30D_pct": -0.17, "MAE_90D_pct": -0.17, "MAE_180D_pct": -0.17, "peak_date": "2024-08-08", "peak_price": 8790.0, "drawdown_after_peak_pct": -5.92, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_or_event_exit_after_tender_floor_when_no_additional_economic_bridge_exists", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_deal_failure_tender_revision_financing_legal_or_business_break", "trigger_outcome_label": "governance_tender_floor_positive_with_cap_watch", "current_profile_verdict": "C32 should preserve tender-floor minority-economics positives when the listed minority shareholder is the direct beneficiary of a tender/voluntary-delisting floor. Lock&Lock showed a controlled-MAE tender rerating and then price pinning near the offer floor; C32 should treat this as event-floor lifecycle, not perpetual operating Stage2.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_delisting_floor_event", "share_count_change_inside_window": false, "same_entry_group_id": "C32_TENDER_FLOOR_115390_2024-02-19", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R12L76-C32-119860-CONNECTWAVE-TENDER-CAP-NO-FURTHER-GREEN", "case_id": "R12L76-C32-119860-CONNECTWAVE-TENDER-CAP-NO-FURTHER-GREEN", "symbol": "119860", "company_name": "커넥트웨이브", "round": "R12", "loop": "76", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "VOLUNTARY_DELISTING_TENDER_FLOOR_MINORITY_ECONOMICS_BRIDGE_VS_TENDER_CAP_NO_FURTHER_GREEN", "loop_objective": "governance_event_lifecycle_test|counterexample_mining|tender_floor_cap_guardrail", "trigger_type": "Stage2-Boundary / TenderFloorCapNoFurtherGreen", "trigger_date": "2024-03-13", "entry_date": "2024-03-14", "entry_price": 12250.0, "evidence_available_at_that_date": "CONTROL_SHAREHOLDER_TENDER_FLOOR_CAP_WITH_LIMITED_POST_FLOOR_UPSIDE", "evidence_source": "source_proxy_manual_verification_required:CONNECTWAVE_2024_TENDER_FLOOR_CONTROL_SHAREHOLDER_CLOSING_MINORITY_ECONOMICS_CAP_BRIDGE", "stage2_evidence_fields": ["tender_or_voluntary_delisting_event", "minority_economics_candidate", "floor_price_or_closing_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "tender_floor_pin_or_closing_certainty_candidate"], "stage4b_evidence_fields": ["tender_cap_no_further_green", "bridge_stale_or_absent", "sharecount_or_delisting_validation"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/119/119860/2024.csv", "profile_path": "atlas/symbol_profiles/119/119860.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 41.96, "MFE_90D_pct": 47.1, "MFE_180D_pct": 47.27, "MAE_30D_pct": -1.14, "MAE_90D_pct": -1.14, "MAE_180D_pct": -1.14, "peak_date": "2024-08-13", "peak_price": 18040.0, "drawdown_after_peak_pct": -1.88, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_or_event_exit_after_tender_floor_when_no_additional_economic_bridge_exists", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_deal_failure_tender_revision_financing_legal_or_business_break", "trigger_outcome_label": "counterexample_tender_cap_no_permanent_green", "current_profile_verdict": "C32 should distinguish tender-floor tradability from ongoing rerating. Connectwave produced a large controlled-MAE move into the tender/floor region and then pinned near the floor, so it is a good counterexample against treating tender-floor MFE as permanent Green.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_delisting_floor_event", "share_count_change_inside_window": true, "same_entry_group_id": "C32_TENDER_FLOOR_119860_2024-03-14", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L76-C32-003410-SSANGYONGCNE-VOLUNTARY-DELISTING-TENDER-FLOOR", "trigger_id": "TRG_R12L76-C32-003410-SSANGYONGCNE-VOLUNTARY-DELISTING-TENDER-FLOOR", "symbol": "003410", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"governance_event_score": 15, "tender_floor_score": 16, "closing_certainty_score": 13, "minority_economics_score": 15, "listed_entity_beneficiary_score": 15, "ongoing_operating_green_score": 4, "relative_strength_score": 13, "execution_risk_score": 8, "dilution_or_sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_before": 82, "stage_label_before": "Governance tender-floor lifecycle after source repair", "raw_component_scores_after": {"governance_event_score": 8, "tender_floor_score": 18, "closing_certainty_score": 15, "minority_economics_score": 17, "listed_entity_beneficiary_score": 17, "ongoing_operating_green_score": 1, "relative_strength_score": 12, "execution_risk_score": 9, "dilution_or_sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_after": 86, "stage_label_after": "Event-lifecycle Stage2 after source repair; exit/cap after tender floor", "changed_components": ["tender_floor_score", "closing_certainty_score", "minority_economics_score", "ongoing_operating_green_score", "execution_risk_score"], "component_delta_explanation": "Governance event score should be capped unless tender terms, closing certainty, minority economics and listed-shareholder beneficiary bridge are verified; tender-floor MFE does not imply ongoing operating Green.", "MFE_90D_pct": 16.75, "MAE_90D_pct": 0.0, "score_return_alignment_label": "tender_floor_lifecycle_positive", "current_profile_verdict": "C32 should allow tender-floor lifecycle candidates when minority shareholders have explicit tender mechanics, floor price, closing path and direct economic beneficiary mapping. Ssangyong C&E produced a low-MAE tender-floor move and then price pinning, but this is not an operating Green; it is a governance-event floor trade that ends when tender mechanics complete."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L76-C32-115390-LOCKNLOCK-VOLUNTARY-DELISTING-TENDER-FLOOR", "trigger_id": "TRG_R12L76-C32-115390-LOCKNLOCK-VOLUNTARY-DELISTING-TENDER-FLOOR", "symbol": "115390", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"governance_event_score": 15, "tender_floor_score": 16, "closing_certainty_score": 13, "minority_economics_score": 15, "listed_entity_beneficiary_score": 15, "ongoing_operating_green_score": 4, "relative_strength_score": 13, "execution_risk_score": 8, "dilution_or_sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_before": 82, "stage_label_before": "Governance tender-floor lifecycle after source repair", "raw_component_scores_after": {"governance_event_score": 8, "tender_floor_score": 18, "closing_certainty_score": 15, "minority_economics_score": 17, "listed_entity_beneficiary_score": 17, "ongoing_operating_green_score": 1, "relative_strength_score": 12, "execution_risk_score": 9, "dilution_or_sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_after": 86, "stage_label_after": "Event-lifecycle Stage2 after source repair; exit/cap after tender floor", "changed_components": ["tender_floor_score", "closing_certainty_score", "minority_economics_score", "ongoing_operating_green_score", "execution_risk_score"], "component_delta_explanation": "Governance event score should be capped unless tender terms, closing certainty, minority economics and listed-shareholder beneficiary bridge are verified; tender-floor MFE does not imply ongoing operating Green.", "MFE_90D_pct": 48.14, "MAE_90D_pct": -0.17, "score_return_alignment_label": "tender_floor_lifecycle_positive", "current_profile_verdict": "C32 should preserve tender-floor minority-economics positives when the listed minority shareholder is the direct beneficiary of a tender/voluntary-delisting floor. Lock&Lock showed a controlled-MAE tender rerating and then price pinning near the offer floor; C32 should treat this as event-floor lifecycle, not perpetual operating Stage2."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L76-C32-119860-CONNECTWAVE-TENDER-CAP-NO-FURTHER-GREEN", "trigger_id": "TRG_R12L76-C32-119860-CONNECTWAVE-TENDER-CAP-NO-FURTHER-GREEN", "symbol": "119860", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"governance_event_score": 15, "tender_floor_score": 16, "closing_certainty_score": 10, "minority_economics_score": 12, "listed_entity_beneficiary_score": 15, "ongoing_operating_green_score": 2, "relative_strength_score": 13, "execution_risk_score": 12, "dilution_or_sharecount_validation_risk": 8, "source_confidence_score": 2}, "weighted_score_before": 68, "stage_label_before": "Tender-floor cap boundary / no further Green", "raw_component_scores_after": {"governance_event_score": 8, "tender_floor_score": 18, "closing_certainty_score": 12, "minority_economics_score": 13, "listed_entity_beneficiary_score": 17, "ongoing_operating_green_score": 1, "relative_strength_score": 12, "execution_risk_score": 13, "dilution_or_sharecount_validation_risk": 10, "source_confidence_score": 2}, "weighted_score_after": 60, "stage_label_after": "No permanent Green after tender floor / cap boundary", "changed_components": ["tender_floor_score", "closing_certainty_score", "minority_economics_score", "ongoing_operating_green_score", "execution_risk_score"], "component_delta_explanation": "Governance event score should be capped unless tender terms, closing certainty, minority economics and listed-shareholder beneficiary bridge are verified; tender-floor MFE does not imply ongoing operating Green.", "MFE_90D_pct": 47.1, "MAE_90D_pct": -1.14, "score_return_alignment_label": "tender_floor_cap_no_further_green", "current_profile_verdict": "C32 should distinguish tender-floor tradability from ongoing rerating. Connectwave produced a large controlled-MAE move into the tender/floor region and then pinned near the floor, so it is a good counterexample against treating tender-floor MFE as permanent Green."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R12", "loop": 76, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "VOLUNTARY_DELISTING_TENDER_FLOOR_MINORITY_ECONOMICS_BRIDGE_VS_TENDER_CAP_NO_FURTHER_GREEN", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 2, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 1, "inactive_or_delisted_like_count": 3, "current_profile_error_count": 1, "diversity_score_summary": "+3 underused C32 tender/voluntary-delisting symbols outside top-covered KoreaZinc/SM set and outside loop-75 R12 names, +2 tender-floor positive paths, +1 tender-cap no-permanent-Green boundary, no hard duplicate", "residual_contribution_label": "governance_tender_floor_lifecycle_guardrail_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R12", "loop": 76, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "axis": "voluntary_delisting_tender_floor_minority_economics_bridge_vs_tender_cap_no_further_green", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C32 should split true tender-floor minority-economics lifecycle trades from ongoing operating rerating. Stage2 requires tender mechanics, closing certainty, minority economics, listed-shareholder beneficiary and floor/cap terms. Once price pins near the tender floor, the signal should be event-lifecycle managed and should not remain permanent Green without a separate operating bridge.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["003410", "115390", "119860"], "share_count_validation_required": ["119860"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R12", "loop": 76, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "existing_axis_strengthened": ["price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "local_4b_watch_guard", "stage2_required_bridge", "share_count_validation_guard", "event_lifecycle_exit_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C32 tender/voluntary-delisting events need minority-economics proof. Ssangyong C&E and Lock&Lock show tender-floor lifecycle positives; Connectwave shows the cap boundary where tender-floor MFE should not be treated as permanent Green."}
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
all_selected_180D_windows_available_where_profile_allows = true
production_scoring_changed = false
shadow_weight_only = true
```

Profile checks:

```text
003410:
  name = 쌍용C&E
  profile last_date = 2024-06-20, raw_last_date = 2024-07-08
  corporate_action_candidate_dates = 1999-05-20, 1999-06-15, 2000-11-15, 2004-01-07, 2005-12-19, 2018-07-11
  selected window = 2024-02-01~available event lifecycle window
  contamination = false by profile, but inactive/delisting lifecycle handling required

115390:
  name = 락앤락
  profile last_date = 2024-11-19, raw_last_date = 2024-12-06
  corporate_action_candidate_dates = none
  selected window = 2024-02-19~available event lifecycle window
  contamination = false

119860:
  name = 커넥트웨이브
  corporate_action_candidate_dates = 2016-12-28, 2017-01-19, 2022-12-16
  selected window = 2024-03-14~available event lifecycle window
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required
```

Data-quality caveat:

```text
All selected C32 rows are source_proxy_only / evidence_url_pending.
All three are inactive_or_delisted_like by stock-web profile, so runtime promotion must treat them as historical event-lifecycle rows, not live candidates.
119860 also requires share-count validation before any row ingestion.
This MD is useful for stock-web path calibration and C32 rule-shape discovery,
but coding-agent promotion requires non-proxy tender terms, closing certainty, minority economics, floor/cap mechanics and listed-shareholder beneficiary bridge evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R12/C32 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair and 119860 needs share-count validation.

Candidate axis:
voluntary_delisting_tender_floor_minority_economics_bridge_vs_tender_cap_no_further_green

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 003410, 115390 and 119860.
4. Validate delisting/inactive-like lifecycle handling for 003410, 115390 and 119860.
5. Validate 119860 share-count changes inside the selected window.
6. Consider Stage2 only when:
   - tender or voluntary-delisting mechanics are explicit,
   - minority shareholder economics are visible,
   - floor/cap terms and closing path are credible,
   - listed-entity beneficiary is clear,
   - MAE remains controlled or the signal is deliberately event-lifecycle-managed.
7. After price pins near the tender floor, stop treating the row as continuing Green unless a separate operating bridge exists.
8. Do not apply the same label to seller, acquirer, operating company and minority shareholder.
9. Do not convert tender-cap drawdown into hard 4C without non-price deal failure, legal break, financing, operating deterioration or insolvency evidence.
10. Emit before/after diagnostics and reject if verified tender-floor lifecycle positives are overblocked or treated as perpetual Green.
```

---

## Final round state

```text
completed_round = R12
completed_loop = 76
next_round = R13
next_loop = 76
round_schedule_status = valid
round_sector_consistency = pass
```

