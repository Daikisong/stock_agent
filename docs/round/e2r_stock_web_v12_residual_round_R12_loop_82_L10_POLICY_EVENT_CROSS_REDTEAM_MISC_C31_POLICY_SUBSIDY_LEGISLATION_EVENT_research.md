# E2R Stock-Web v12 Residual Research — R12 Loop 82 / L10 / C31

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R12",
  "scheduled_loop": 82,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R12",
  "completed_loop": 82,
  "computed_next_round": "R13",
  "computed_next_loop": 82,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "fine_archetype_id": "TRAVEL_TOURISM_VISA_REOPENING_DIRECT_VOLUME_MARGIN_BRIDGE_VS_TOURISM_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "policy_event_bridge_guardrail",
    "4B_non_price_requirement_stress_test",
    "tourism_visa_reopening_direct_beneficiary_mapping",
    "travel_agency_casino_resort_volume_margin_bridge",
    "service_policy_theme_fade_boundary",
    "under_covered_service_sector_expansion",
    "share_count_validation_queue_creation",
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

Previous completed state in this interactive run: R11 / loop 82.

Therefore:

```text
scheduled_round = R12
scheduled_loop = 82
allowed_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC or relevant under-covered service/agri sector
selected_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
selected_canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
computed_next_round = R13
computed_next_loop = 82
```

R12 was routed to C31 because this is an under-covered tourism/service policy event bridge guardrail, not a normal consumer round.  
This file deliberately avoids loop-81 childcare/agri-policy names and loop-82 C32 governance names.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C31 concentration in:

```text
UNKNOWN_SYMBOL, 036460, 112610, 005380, 005860, 218150
```

This run uses three different tourism/service policy symbols:

```text
032350 / 롯데관광개발 / casino-resort tourism policy volume bridge
039130 / 하나투어 / travel-agency visa/reopening theme fade
080160 / 모두투어 / travel-agency tourism policy reopening fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
032350 shows share-count changes inside the selected 2024 shard and requires coding-agent validation before runtime promotion.
```

## Research thesis

C31 is not “관광정책 테마가 올랐다.”

For tourism / visa / reopening rows, the bridge must pass through:

```text
policy / visa / reopening headline
→ direct beneficiary mapping
→ booking volume or casino/resort volume
→ capacity, ASP, commission or occupancy economics
→ revenue conversion and margin bridge
→ durable rerating
```

관광정책 headline은 공항 전광판이다.  
C31이 보려는 것은 전광판의 출발편이 실제 예약, 객실 점유, 카지노 드롭, 수수료율, 매출, 마진으로 착륙하는지다.

---

## Case 1 — Bounded tourism resort candidate: 032350 / 롯데관광개발

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_validation_required = true
source_repair_required = true
```

The source-repair task is tourism/visa policy, casino-resort inbound volume, hotel occupancy, ADR, revenue conversion and margin bridge evidence.

```text
evidence_family = TOURISM_VISA_REOPENING_CASINO_RESORT_INBOUND_VOLUME_OCCUPANCY_REVENUE_MARGIN_BRIDGE
case_role = positive_bounded_tourism_resort_volume_candidate_with_sharecount_validation_no_forced4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 9,020
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/032/032350/2024.csv`:

```text
2024-02-01,9020,9090,8860,9050
2024-02-07,9560,9650,9360,9420
2024-03-27,9490,9990,9400,9990
2024-04-01,9980,10720,9890,10340
2024-08-05,9270,9370,8090,8470
2024-09-27,9630,10200,9580,10200
2024-10-25,9650,9750,9440,9480
2024-10-31,9590,9720,9410,9720
```

### Backtest

```text
MFE_30D  = +6.98%
MAE_30D  = -2.33%
MFE_90D  = +18.85%
MAE_90D  = -2.33%
MFE_180D = +18.85%
MAE_180D = -10.31%
peak_180 = 10,720 on 2024-04-01
trough_180 = 8,090 on 2024-08-05
peak_to_later_drawdown = -24.53%
```

### Interpretation

This is a bounded C31 tourism/casino-resort policy candidate, not an explosive Green.  
The MAE was controlled enough to avoid forced 4B, but share-count validation and direct volume/margin proof are required.

Correct treatment:

```text
verified tourism/visa policy / casino-resort volume / occupancy / ADR / margin bridge → Stage2-Yellow possible
share-count validation first
bounded MAE + weak bridge → RiskWatch
no forced 4B without non-price demand or margin deterioration
```

---

## Case 2 — Counterexample / local 4B: 039130 / 하나투어

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests travel-agency visa/reopening beta without enough bookings, ASP, commission and margin bridge.

```text
evidence_family = TRAVEL_AGENCY_VISA_REOPENING_OUTBOUND_INBOUND_VOLUME_THEME_WITH_WEAK_PACKAGE_BOOKING_REVENUE_MARGIN_BRIDGE
case_role = counterexample_travel_agency_visa_reopening_theme_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 63,100
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/039/039130/2024.csv`:

```text
2024-02-01,63100,64000,62200,63100
2024-02-06,67000,68800,64100,65800
2024-03-25,70000,70600,68300,68700
2024-04-16,53800,53800,52200,52600
2024-08-05,48050,48900,44150,44700
2024-09-27,49600,51000,49450,50100
2024-10-25,47500,47850,46350,46900
2024-10-31,48300,49300,47350,49300
```

### Backtest

```text
MFE_30D  = +9.03%
MAE_30D  = -5.23%
MFE_90D  = +11.89%
MAE_90D  = -17.27%
MFE_180D = +11.89%
MAE_180D = -30.03%
peak_180 = 70,600 on 2024-03-25
trough_180 = 44,150 on 2024-08-05
peak_to_later_drawdown = -37.46%
```

### Interpretation

This is a C31 travel-agency reopening theme-fade row.  
The policy/visa headline did not validate durable booking-volume or margin economics.

Correct treatment:

```text
travel / visa reopening theme beta
→ no verified booking volume / ASP / commission / revenue / margin bridge
→ local 4B-watch
```

---

## Case 3 — Counterexample / local 4B: 080160 / 모두투어

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests travel-agency tourism reopening beta without enough booking-volume and package-margin bridge.

```text
evidence_family = TRAVEL_AGENCY_TOURISM_POLICY_REOPENING_THEME_WITH_WEAK_BOOKING_VOLUME_REVENUE_MARGIN_BRIDGE
case_role = counterexample_travel_agency_policy_reopening_theme_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 17,180
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/080/080160/2024.csv`:

```text
2024-02-01,17180,17220,16790,17090
2024-02-14,16560,17760,16470,17740
2024-03-20,15490,15530,15220,15240
2024-06-28,15110,15200,14960,15030
2024-08-05,12400,12410,10200,11300
2024-09-20,10490,10690,10270,10270
2024-10-25,9990,9990,9850,9850
2024-10-31,9840,10040,9690,9980
```

### Backtest

```text
MFE_30D  = +3.38%
MAE_30D  = -11.41%
MFE_90D  = +3.38%
MAE_90D  = -13.04%
MFE_180D = +3.38%
MAE_180D = -43.60%
peak_180 = 17,760 on 2024-02-14
trough_180 = 9,690 on 2024-10-31
peak_to_later_drawdown = -45.44%
```

### Interpretation

This is a C31 travel-agency policy-theme false-positive boundary.  
The post-entry MFE was tiny and the later drawdown widened into local-4B territory.

Correct treatment:

```text
travel-agency reopening theme beta
→ no verified booking volume / package margin / channel mix / revenue bridge
→ local 4B-watch
```

---

## Cross-case residual finding

### What this strengthens

```text
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
stage2_required_bridge = strengthen
direct_beneficiary_mapping_required = strengthen
undercovered_service_policy_guard = strengthen
share_count_validation_guard = strengthen
full_4b_requires_non_price_evidence = keep
```

### What this does not justify

```text
do_not_raise_generic_C31_tourism_policy_theme_weight = true
do_not_treat_tourism_or_visa_reopening_headline_as_Green_without_direct_volume_margin_bridge = true
do_not_ingest_sharecount_changed_tourism_rows_without_validation = true
do_not_convert_tourism_policy_drawdown_to_hard_4C_without_non_price_policy_reversal_booking_collapse_channel_loss_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
TRAVEL_TOURISM_VISA_REOPENING_DIRECT_VOLUME_MARGIN_BRIDGE_VS_TOURISM_THEME_FADE
```

This fine archetype covers:

```text
1. casino-resort tourism volume candidate → Stage2-Yellow possible after source repair and validation
2. travel-agency visa/reopening beta without booking economics → false Stage2 / local 4B
3. travel-agency tourism policy beta without package margin bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R12L82-C31-032350-LOTTE-TOURISM-RESORT-VISA-VOLUME-MARGIN", "symbol": "032350", "company_name": "롯데관광개발", "round": "R12", "loop": "82", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "TRAVEL_TOURISM_VISA_REOPENING_DIRECT_VOLUME_MARGIN_BRIDGE_VS_TOURISM_THEME_FADE", "case_type": "policy_subsidy_legislation_event_tourism_service", "positive_or_counterexample": "positive", "best_trigger": "RiskWatch-PositiveTourismVisaCasinoResortVolumeMarginBridgeWithSharecountValidation", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C31 should allow tourism policy positives only when visa/reopening policy maps to inbound volume, casino drop, hotel occupancy, ADR, revenue conversion and margin bridge. Lotte Tour Development had moderate MFE with bounded MAE, but share-count validation is needed before runtime promotion.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy tourism/visa policy, direct beneficiary mapping, booking or casino/resort volume, pricing, revenue conversion and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R12L82-C31-039130-HANATOUR-TRAVEL-VISA-THEME-FADE", "symbol": "039130", "company_name": "하나투어", "round": "R12", "loop": "82", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "TRAVEL_TOURISM_VISA_REOPENING_DIRECT_VOLUME_MARGIN_BRIDGE_VS_TOURISM_THEME_FADE", "case_type": "policy_subsidy_legislation_event_tourism_service", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / TravelVisaReopeningVolumeMarginFadeWithLocal4BWatch", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C31 should not treat tourism/visa reopening beta as durable Stage2 unless package bookings, air-seat supply, ASP, commission take-rate, revenue and margin bridge are visible. Hanatour had modest early MFE and then high-MAE fade.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy tourism/visa policy, direct beneficiary mapping, booking or casino/resort volume, pricing, revenue conversion and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R12L82-C31-080160-MODETOUR-TRAVEL-VISA-REOPENING-FADE", "symbol": "080160", "company_name": "모두투어", "round": "R12", "loop": "82", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "TRAVEL_TOURISM_VISA_REOPENING_DIRECT_VOLUME_MARGIN_BRIDGE_VS_TOURISM_THEME_FADE", "case_type": "policy_subsidy_legislation_event_tourism_service", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / TravelAgencyVisaReopeningThemeFadeWithLocal4BWatch", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C31 should not treat travel-agency reopening theme beta as durable Stage2 unless booking volume, package margin, channel mix, air-seat cost, revenue conversion and margin bridge are visible. Modetour had almost no forward MFE and then severe MAE.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy tourism/visa policy, direct beneficiary mapping, booking or casino/resort volume, pricing, revenue conversion and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R12L82-C31-032350-LOTTE-TOURISM-RESORT-VISA-VOLUME-MARGIN", "case_id": "R12L82-C31-032350-LOTTE-TOURISM-RESORT-VISA-VOLUME-MARGIN", "symbol": "032350", "company_name": "롯데관광개발", "round": "R12", "loop": "82", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "TRAVEL_TOURISM_VISA_REOPENING_DIRECT_VOLUME_MARGIN_BRIDGE_VS_TOURISM_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|policy_event_bridge_guardrail|undercovered_service_tourism_axis", "trigger_type": "RiskWatch-PositiveTourismVisaCasinoResortVolumeMarginBridgeWithSharecountValidation", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 9020.0, "evidence_available_at_that_date": "TOURISM_VISA_REOPENING_CASINO_RESORT_INBOUND_VOLUME_OCCUPANCY_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:LOTTE_TOURISM_2024_VISA_REOPENING_CASINO_RESORT_INBOUND_VOLUME_OCCUPANCY_ADR_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["tourism_or_visa_policy_event", "direct_beneficiary_mapping_candidate", "booking_volume_or_resort_revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "channel_or_capacity_utilization_candidate"], "stage4b_evidence_fields": ["tourism_policy_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/032/032350/2024.csv", "profile_path": "atlas/symbol_profiles/032/032350.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 6.98, "MFE_90D_pct": 18.85, "MFE_180D_pct": 18.85, "MAE_30D_pct": -2.33, "MAE_90D_pct": -2.33, "MAE_180D_pct": -10.31, "peak_date": "2024-04-01", "peak_price": 10720.0, "drawdown_after_peak_pct": -24.53, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_tourism_policy_peak_if_booking_volume_resort_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_policy_reversal_booking_collapse_channel_loss_financing_or_margin_break", "trigger_outcome_label": "positive_bounded_tourism_resort_volume_candidate_with_sharecount_validation_no_forced4b", "current_profile_verdict": "C31 should allow tourism policy positives only when visa/reopening policy maps to inbound volume, casino drop, hotel occupancy, ADR, revenue conversion and margin bridge. Lotte Tour Development had moderate MFE with bounded MAE, but share-count validation is needed before runtime promotion.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_sharecount_validation_required", "share_count_change_inside_window": true, "same_entry_group_id": "C31_TOURISM_POLICY_032350_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R12L82-C31-039130-HANATOUR-TRAVEL-VISA-THEME-FADE", "case_id": "R12L82-C31-039130-HANATOUR-TRAVEL-VISA-THEME-FADE", "symbol": "039130", "company_name": "하나투어", "round": "R12", "loop": "82", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "TRAVEL_TOURISM_VISA_REOPENING_DIRECT_VOLUME_MARGIN_BRIDGE_VS_TOURISM_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|policy_event_bridge_guardrail|undercovered_service_tourism_axis", "trigger_type": "Stage2-FalsePositive / TravelVisaReopeningVolumeMarginFadeWithLocal4BWatch", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 63100.0, "evidence_available_at_that_date": "TRAVEL_AGENCY_VISA_REOPENING_OUTBOUND_INBOUND_VOLUME_THEME_WITH_WEAK_PACKAGE_BOOKING_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:HANATOUR_2024_TRAVEL_VISA_REOPENING_PACKAGE_BOOKING_AIR_SEAT_SUPPLY_ASP_COMMISSION_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["tourism_or_visa_policy_event", "direct_beneficiary_mapping_candidate", "booking_volume_or_resort_revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "channel_or_capacity_utilization_candidate"], "stage4b_evidence_fields": ["tourism_policy_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/039/039130/2024.csv", "profile_path": "atlas/symbol_profiles/039/039130.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 9.03, "MFE_90D_pct": 11.89, "MFE_180D_pct": 11.89, "MAE_30D_pct": -5.23, "MAE_90D_pct": -17.27, "MAE_180D_pct": -30.03, "peak_date": "2024-03-25", "peak_price": 70600.0, "drawdown_after_peak_pct": -37.46, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_tourism_policy_peak_if_booking_volume_resort_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_policy_reversal_booking_collapse_channel_loss_financing_or_margin_break", "trigger_outcome_label": "counterexample_travel_agency_visa_reopening_theme_local4b", "current_profile_verdict": "C31 should not treat tourism/visa reopening beta as durable Stage2 unless package bookings, air-seat supply, ASP, commission take-rate, revenue and margin bridge are visible. Hanatour had modest early MFE and then high-MAE fade.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_sharecount_validation_required", "share_count_change_inside_window": false, "same_entry_group_id": "C31_TOURISM_POLICY_039130_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R12L82-C31-080160-MODETOUR-TRAVEL-VISA-REOPENING-FADE", "case_id": "R12L82-C31-080160-MODETOUR-TRAVEL-VISA-REOPENING-FADE", "symbol": "080160", "company_name": "모두투어", "round": "R12", "loop": "82", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "TRAVEL_TOURISM_VISA_REOPENING_DIRECT_VOLUME_MARGIN_BRIDGE_VS_TOURISM_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|policy_event_bridge_guardrail|undercovered_service_tourism_axis", "trigger_type": "Stage2-FalsePositive / TravelAgencyVisaReopeningThemeFadeWithLocal4BWatch", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 17180.0, "evidence_available_at_that_date": "TRAVEL_AGENCY_TOURISM_POLICY_REOPENING_THEME_WITH_WEAK_BOOKING_VOLUME_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:MODETOUR_2024_TRAVEL_AGENCY_POLICY_REOPENING_BOOKING_VOLUME_PACKAGE_MARGIN_CHANNEL_MIX_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["tourism_or_visa_policy_event", "direct_beneficiary_mapping_candidate", "booking_volume_or_resort_revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "channel_or_capacity_utilization_candidate"], "stage4b_evidence_fields": ["tourism_policy_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/080/080160/2024.csv", "profile_path": "atlas/symbol_profiles/080/080160.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.38, "MFE_90D_pct": 3.38, "MFE_180D_pct": 3.38, "MAE_30D_pct": -11.41, "MAE_90D_pct": -13.04, "MAE_180D_pct": -43.6, "peak_date": "2024-02-14", "peak_price": 17760.0, "drawdown_after_peak_pct": -45.44, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_tourism_policy_peak_if_booking_volume_resort_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_policy_reversal_booking_collapse_channel_loss_financing_or_margin_break", "trigger_outcome_label": "counterexample_travel_agency_policy_reopening_theme_local4b", "current_profile_verdict": "C31 should not treat travel-agency reopening theme beta as durable Stage2 unless booking volume, package margin, channel mix, air-seat cost, revenue conversion and margin bridge are visible. Modetour had almost no forward MFE and then severe MAE.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_sharecount_validation_required", "share_count_change_inside_window": false, "same_entry_group_id": "C31_TOURISM_POLICY_080160_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L82-C31-032350-LOTTE-TOURISM-RESORT-VISA-VOLUME-MARGIN", "trigger_id": "TRG_R12L82-C31-032350-LOTTE-TOURISM-RESORT-VISA-VOLUME-MARGIN", "symbol": "032350", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"policy_event_score": 13, "direct_beneficiary_mapping_score": 13, "booking_or_resort_volume_score": 12, "pricing_capacity_score": 11, "revenue_margin_bridge_score": 12, "relative_strength_score": 6, "sharecount_validation_risk": 10, "execution_risk_score": 11, "source_confidence_score": 2}, "weighted_score_before": 68, "stage_label_before": "RiskWatch / Stage2-Yellow after source repair", "raw_component_scores_after": {"policy_event_score": 9, "direct_beneficiary_mapping_score": 15, "booking_or_resort_volume_score": 14, "pricing_capacity_score": 13, "revenue_margin_bridge_score": 14, "relative_strength_score": 5, "sharecount_validation_risk": 12, "execution_risk_score": 12, "source_confidence_score": 2}, "weighted_score_after": 74, "stage_label_after": "Stage2-Yellow only after source repair + validation", "changed_components": ["policy_event_score", "direct_beneficiary_mapping_score", "booking_or_resort_volume_score", "pricing_capacity_score", "revenue_margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Cap policy-event score unless tourism/visa policy maps to direct beneficiary economics, booking or casino/resort volume, pricing, revenue conversion and margin bridge.", "MFE_90D_pct": 18.85, "MAE_90D_pct": -2.33, "score_return_alignment_label": "tourism_policy_bounded_candidate", "current_profile_verdict": "C31 should allow tourism policy positives only when visa/reopening policy maps to inbound volume, casino drop, hotel occupancy, ADR, revenue conversion and margin bridge. Lotte Tour Development had moderate MFE with bounded MAE, but share-count validation is needed before runtime promotion."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L82-C31-039130-HANATOUR-TRAVEL-VISA-THEME-FADE", "trigger_id": "TRG_R12L82-C31-039130-HANATOUR-TRAVEL-VISA-THEME-FADE", "symbol": "039130", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"policy_event_score": 13, "direct_beneficiary_mapping_score": 4, "booking_or_resort_volume_score": 3, "pricing_capacity_score": 2, "revenue_margin_bridge_score": 1, "relative_strength_score": 3, "sharecount_validation_risk": 0, "execution_risk_score": 24, "source_confidence_score": 2}, "weighted_score_before": 42, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"policy_event_score": 9, "direct_beneficiary_mapping_score": 2, "booking_or_resort_volume_score": 1, "pricing_capacity_score": 1, "revenue_margin_bridge_score": 1, "relative_strength_score": 2, "sharecount_validation_risk": 0, "execution_risk_score": 26, "source_confidence_score": 2}, "weighted_score_after": 31, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["policy_event_score", "direct_beneficiary_mapping_score", "booking_or_resort_volume_score", "pricing_capacity_score", "revenue_margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Cap policy-event score unless tourism/visa policy maps to direct beneficiary economics, booking or casino/resort volume, pricing, revenue conversion and margin bridge.", "MFE_90D_pct": 11.89, "MAE_90D_pct": -17.27, "score_return_alignment_label": "tourism_policy_theme_false_positive_direct_economics_gap", "current_profile_verdict": "C31 should not treat tourism/visa reopening beta as durable Stage2 unless package bookings, air-seat supply, ASP, commission take-rate, revenue and margin bridge are visible. Hanatour had modest early MFE and then high-MAE fade."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L82-C31-080160-MODETOUR-TRAVEL-VISA-REOPENING-FADE", "trigger_id": "TRG_R12L82-C31-080160-MODETOUR-TRAVEL-VISA-REOPENING-FADE", "symbol": "080160", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"policy_event_score": 13, "direct_beneficiary_mapping_score": 4, "booking_or_resort_volume_score": 3, "pricing_capacity_score": 2, "revenue_margin_bridge_score": 1, "relative_strength_score": 3, "sharecount_validation_risk": 0, "execution_risk_score": 24, "source_confidence_score": 2}, "weighted_score_before": 42, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"policy_event_score": 9, "direct_beneficiary_mapping_score": 2, "booking_or_resort_volume_score": 1, "pricing_capacity_score": 1, "revenue_margin_bridge_score": 1, "relative_strength_score": 2, "sharecount_validation_risk": 0, "execution_risk_score": 26, "source_confidence_score": 2}, "weighted_score_after": 31, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["policy_event_score", "direct_beneficiary_mapping_score", "booking_or_resort_volume_score", "pricing_capacity_score", "revenue_margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Cap policy-event score unless tourism/visa policy maps to direct beneficiary economics, booking or casino/resort volume, pricing, revenue conversion and margin bridge.", "MFE_90D_pct": 3.38, "MAE_90D_pct": -13.04, "score_return_alignment_label": "tourism_policy_theme_false_positive_direct_economics_gap", "current_profile_verdict": "C31 should not treat travel-agency reopening theme beta as durable Stage2 unless booking volume, package margin, channel mix, air-seat cost, revenue conversion and margin bridge are visible. Modetour had almost no forward MFE and then severe MAE."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R12", "loop": 82, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "TRAVEL_TOURISM_VISA_REOPENING_DIRECT_VOLUME_MARGIN_BRIDGE_VS_TOURISM_THEME_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "four_b_case_count": 2, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 1, "current_profile_error_count": 1, "diversity_score_summary": "+3 C31 tourism/service policy symbols outside top-covered UNKNOWN/036460/112610/005380/005860/218150 set and outside loop-81/82 childcare-agri-governance names, +3 casino-resort/travel-agency trigger families, +1 bounded tourism resort candidate, +2 travel-agency local-4B counterexamples, no hard duplicate", "residual_contribution_label": "policy_event_bridge_guardrail_with_undercovered_tourism_service_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R12", "loop": 82, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "axis": "travel_tourism_visa_reopening_direct_volume_margin_bridge_vs_tourism_theme_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C31 should split verified tourism/visa/reopening direct-beneficiary volume-margin trades from generic tourism policy theme beta. Stage2 requires explicit policy/visa/reopening event plus direct beneficiary mapping, booking or casino/resort volume, capacity/pricing, revenue conversion and margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch. Share-count flags require validation before runtime promotion.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["032350", "039130", "080160"], "share_count_validation_required": ["032350"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R12", "loop": 82, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "existing_axis_strengthened": ["price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "stage2_required_bridge", "direct_beneficiary_mapping_required", "undercovered_service_policy_guard", "share_count_validation_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C31 tourism policy events need direct-beneficiary proof. Lotte Tour Development is a bounded tourism/casino-resort candidate after source repair and share-count validation; Hanatour and Modetour show travel-agency tourism/visa reopening beta fading into local 4B when booking volume, ASP, commission, revenue and margin bridge are absent or stale."}
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
032350:
  name = 롯데관광개발
  corporate_action_candidate_dates = 2013-09-06, 2015-11-18, 2016-09-08, 2018-11-01
  selected window = 2024-02-01~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required

039130:
  name = 하나투어
  corporate_action_candidate_dates = 2003-09-09, 2003-09-30, 2004-11-19
  selected window = 2024-02-01~D+180
  contamination = false

080160:
  name = 모두투어
  corporate_action_candidate_dates = 2006-06-05, 2006-06-16, 2012-06-22, 2017-07-18
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C31 rows are source_proxy_only / evidence_url_pending.
032350 requires share-count validation before runtime promotion.
This MD is useful for stock-web path calibration and C31 tourism/service policy rule-shape discovery,
but coding-agent promotion requires non-proxy tourism/visa policy evidence, direct beneficiary mapping, booking or casino/resort volume, pricing, revenue conversion and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R12/C31 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair and 032350 needs share-count validation.

Candidate axis:
travel_tourism_visa_reopening_direct_volume_margin_bridge_vs_tourism_theme_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 032350, 039130 and 080160.
4. Validate 032350 share-count changes inside the selected window.
5. Keep generic C31 policy-event/tourism theme weight unchanged until source repair is complete.
6. Consider Stage2 only when:
   - tourism / visa / reopening policy event is explicit,
   - direct beneficiary mapping is visible,
   - booking volume or casino/resort volume is visible,
   - capacity, ASP, commission or occupancy economics are visible,
   - revenue conversion and margin bridge are credible,
   - MAE remains controlled or the signal is lifecycle-managed.
7. Consider local 4B-watch when:
   - the trigger is tourism policy theme beta only,
   - booking / resort volume / revenue / margin bridge is absent or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
8. Do not force local 4B when bounded tourism rows have controlled MAE and no confirmed non-price bridge break.
9. Do not convert local 4B-watch into full 4B/4C without non-price policy reversal, booking collapse, channel loss, financing or margin break.
10. Emit before/after diagnostics and reject if verified direct-beneficiary tourism positives or bounded resort rows are overblocked.
```

---

## Final round state

```text
completed_round = R12
completed_loop = 82
next_round = R13
next_loop = 82
round_schedule_status = valid
round_sector_consistency = pass
```

