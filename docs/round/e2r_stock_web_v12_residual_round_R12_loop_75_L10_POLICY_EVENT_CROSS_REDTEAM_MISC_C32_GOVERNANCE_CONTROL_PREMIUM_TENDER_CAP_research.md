# E2R Stock-Web v12 Residual Research — R12 Loop 75 / L10 / C32

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R12",
  "scheduled_loop": 75,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R12",
  "completed_loop": 75,
  "computed_next_round": "R13",
  "computed_next_loop": 75,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP",
  "fine_archetype_id": "TENDER_OFFER_CONTROL_TRANSFER_DISPUTE_ECONOMIC_BENEFICIARY_BRIDGE_VS_HEADLINE_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "governance_event_lifecycle_test",
    "tender_control_premium_guardrail",
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

Previous completed state in this interactive run: R11 / loop 75.

Therefore:

```text
scheduled_round = R12
scheduled_loop = 75
allowed_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC or under-covered service/agri sector
selected_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
selected_canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
computed_next_round = R13
computed_next_loop = 75
```

R12 was routed to C32 because this is a governance / tender / control-premium lifecycle test, not a sector operating-leverage round.

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
036560 / 영풍정밀·KZ정밀 / tender-control premium lifecycle
001750 / 한양증권 / securities control-sale premium fade
008930 / 한미사이언스 / family control-dispute beneficiary fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
008930 shows share-count changes inside the selected window and requires coding-agent validation before runtime promotion.
```

## Research thesis

C32 is not “control headline went up.”

The mechanism must identify the economic seat of the listed shareholder:

```text
tender / control transfer / stake dispute
→ transaction mechanics and closing certainty
→ minority economics or listed-entity beneficiary
→ capital policy, operating bridge or tender floor
→ durable rerating
```

A control headline is the auction bell.  
C32 cares whether minority shareholders actually get a paddle in the room.

---

## Case 1 — Tender lifecycle positive: 036560 / 영풍정밀·KZ정밀

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is tender terms, control-premium mechanics, listed-entity beneficiary mapping, closing certainty and minority economics evidence.

```text
evidence_family = TENDER_OFFER_CONTROL_PREMIUM_KOREA_ZINC_STAKE_DISPUTE_LISTED_ENTITY_BENEFICIARY_BRIDGE
case_role = governance_lifecycle_positive_with_later_4b_watch
trigger_date = 2024-09-12
entry_date = 2024-09-13
entry_price = 12,180
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/036/036560/2024.csv` and `2025.csv`:

```text
2024-09-13,12180,12180,12180,12180
2024-09-20,20550,20550,20550,20550
2024-10-07,34200,36700,33300,34700
2024-10-18,28900,30050,22300,22650
2025-04-07,10410,11010,10260,10290
```

### Backtest

```text
MFE_30D  = +201.31%
MAE_30D  = +0.00%
MFE_90D  = +201.31%
MAE_90D  = -2.38%
MFE_180D = +201.31%
MAE_180D = -15.76%
peak_180 = 36,700 on 2024-10-07
trough_180 = 10,260 on 2025-04-07
peak_to_later_drawdown = -72.04%
```

### Interpretation

This is a true C32 lifecycle winner, but not a permanent Green.

The tender/control-premium setup created extraordinary MFE. Yet once tender evidence and control-premium heat faded, the post-peak drawdown became severe.

Correct treatment:

```text
source repair first
possible governance lifecycle Stage2
later local 4B if tender / control-premium bridge fades
```

---

## Case 2 — Counterexample / local 4B: 001750 / 한양증권

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests securities-company control-sale headline beta without enough minority tender economics, closing certainty or listed-shareholder beneficiary bridge.

```text
evidence_family = SECURITIES_CONTROL_SALE_HEADLINE_WITH_WEAK_MINORITIY_TENDER_CLOSING_ECONOMIC_BENEFICIARY_BRIDGE
case_role = counterexample_control_sale_premium_fade
trigger_date = 2024-07-23
entry_date = 2024-07-24
entry_price = 15,650
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/001/001750/2024.csv`:

```text
2024-07-24,15650,16200,15580,16000
2024-08-05,19000,19410,15490,16160
2024-08-27,15510,18150,14500,15250
2024-09-12,16150,17420,15900,17310
2024-10-15,12480,12500,12220,12470
```

### Backtest

```text
MFE_30D  = +24.03%
MAE_30D  = -9.78%
MFE_90D  = +24.03%
MAE_90D  = -16.93%
MFE_180D = +24.03%
MAE_180D = -21.92%
peak_180 = 19,410 on 2024-08-05
trough_180 = 12,220 on 2024-10-15
peak_to_later_drawdown = -37.04%
```

### Interpretation

This is the control-sale premium fade.

The event was tradable, but C32 should not call it durable Stage2 unless minority economics, tender floor or closing-beneficiary bridge is visible.

Correct treatment:

```text
control-sale headline
→ source repair required
→ local 4B-watch if closing/minority bridge fades
```

---

## Case 3 — Counterexample / local 4B: 008930 / 한미사이언스

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
source_repair_required = true
```

This row tests family control-dispute / group-combination headline beta without clear listed-shareholder economic beneficiary bridge.

```text
evidence_family = FAMILY_CONTROL_DISPUTE_GROUP_COMBINATION_HEADLINE_WITH_WEAK_MINORITIY_ECONOMIC_BENEFICIARY_BRIDGE
case_role = counterexample_control_dispute_local4b_with_sharecount_validation
trigger_date = 2024-01-12
entry_date = 2024-01-15
entry_price = 46,350
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/008/008930/2024.csv`:

```text
2024-01-15,46350,47650,40450,43300
2024-01-16,42300,56200,42200,56200
2024-03-28,41350,47000,38000,44350
2024-08-05,30000,30250,25750,26750
2024-10-30,43300,52500,42600,52100
```

### Backtest

```text
MFE_30D  = +21.25%
MAE_30D  = -16.50%
MFE_90D  = +21.25%
MAE_90D  = -24.70%
MFE_180D = +21.25%
MAE_180D = -44.44%
peak_180 = 56,200 on 2024-01-16
trough_180 = 25,750 on 2024-08-05
peak_to_later_drawdown = -54.18%
```

### Interpretation

This is a governance headline false positive.  
The later October rally does not rescue the original January trigger. The first signal opened severe MAE and lacked confirmed minority-beneficiary economics.

Correct treatment:

```text
family control-dispute headline
→ no listed-beneficiary bridge
→ local 4B-watch
```

until non-price mechanics are validated.

---

## Cross-case residual finding

### What this strengthens

```text
price_only_blowoff_blocks_positive_stage = strengthen
full_4b_requires_non_price_evidence = keep
local_4b_watch_guard = strengthen
stage2_required_bridge = strengthen
share_count_validation_guard = strengthen
```

### What this does not justify

```text
do_not_raise_generic_C32_governance_headline_weight = true
do_not_treat_all_control_sale_or_tender_MFE_as_Green = true
do_not_apply_same_label_to_seller_acquirer_operating_company_and_minority_shareholder = true
do_not_convert_governance_drawdown_to_hard_4C_without_non_price_deal_or_business_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
TENDER_OFFER_CONTROL_TRANSFER_DISPUTE_ECONOMIC_BENEFICIARY_BRIDGE_VS_HEADLINE_FADE
```

This fine archetype covers:

```text
1. direct tender/control-premium beneficiary → governance lifecycle Stage2 possible after source repair
2. control-sale headline without minority/tender bridge → false Stage2 / local 4B
3. family control-dispute headline without listed-beneficiary economics → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R12L75-C32-036560-YP-PRECISION-TENDER-CONTROL-PREMIUM-LIFECYCLE", "symbol": "036560", "company_name": "영풍정밀/KZ정밀", "round": "R12", "loop": "75", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "TENDER_OFFER_CONTROL_TRANSFER_DISPUTE_ECONOMIC_BENEFICIARY_BRIDGE_VS_HEADLINE_FADE", "case_type": "governance_control_premium_tender_cap", "positive_or_counterexample": "governance_lifecycle_positive", "best_trigger": "Stage2-PolicyLifecycle / TenderOfferControlPremiumBridgeWithLater4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C32 should allow a tender/control-premium lifecycle candidate when the listed company is a direct economic beneficiary of tender terms, control dispute or stake economics. Young Poong Precision/KZ Precision produced very large MFE, but post-tender drawdown means lifecycle local 4B is mandatory once tender/control-premium evidence fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy tender/control mechanics, closing certainty, minority economics, listed-entity beneficiary, capital policy and operating bridge required before runtime promotion."}
{"row_type": "case", "case_id": "R12L75-C32-001750-HANYANG-SECURITIES-CONTROL-SALE-PREMIUM-FADE", "symbol": "001750", "company_name": "한양증권", "round": "R12", "loop": "75", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "TENDER_OFFER_CONTROL_TRANSFER_DISPUTE_ECONOMIC_BENEFICIARY_BRIDGE_VS_HEADLINE_FADE", "case_type": "governance_control_premium_tender_cap", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / SecuritiesControlSalePremiumFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C32 should not treat a control-sale or preferred-bidder headline as durable Stage2 unless minority economics, tender floor, closing certainty or listed-shareholder beneficiary bridge is explicit. Hanyang Securities had a tradable MFE but then faded into local 4B risk.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy tender/control mechanics, closing certainty, minority economics, listed-entity beneficiary, capital policy and operating bridge required before runtime promotion."}
{"row_type": "case", "case_id": "R12L75-C32-008930-HANMI-SCIENCE-CONTROL-DISPUTE-BENEFICIARY-FADE", "symbol": "008930", "company_name": "한미사이언스", "round": "R12", "loop": "75", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "TENDER_OFFER_CONTROL_TRANSFER_DISPUTE_ECONOMIC_BENEFICIARY_BRIDGE_VS_HEADLINE_FADE", "case_type": "governance_control_premium_tender_cap", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / FamilyControlDisputeBeneficiaryFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C32 should not treat control dispute or group-combination headlines as durable Stage2 unless listed-shareholder beneficiary, transaction mechanics, closing certainty, capital policy or operating bridge is explicit. Hanmi Science produced an event spike but later opened severe MAE and requires share-count validation.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy tender/control mechanics, closing certainty, minority economics, listed-entity beneficiary, capital policy and operating bridge required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R12L75-C32-036560-YP-PRECISION-TENDER-CONTROL-PREMIUM-LIFECYCLE", "case_id": "R12L75-C32-036560-YP-PRECISION-TENDER-CONTROL-PREMIUM-LIFECYCLE", "symbol": "036560", "company_name": "영풍정밀/KZ정밀", "round": "R12", "loop": "75", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "TENDER_OFFER_CONTROL_TRANSFER_DISPUTE_ECONOMIC_BENEFICIARY_BRIDGE_VS_HEADLINE_FADE", "loop_objective": "governance_event_lifecycle_test|counterexample_mining|tender_control_premium_guardrail", "trigger_type": "Stage2-PolicyLifecycle / TenderOfferControlPremiumBridgeWithLater4B", "trigger_date": "2024-09-12", "entry_date": "2024-09-13", "entry_price": 12180.0, "evidence_available_at_that_date": "TENDER_OFFER_CONTROL_PREMIUM_KOREA_ZINC_STAKE_DISPUTE_LISTED_ENTITY_BENEFICIARY_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:YOUNG_POONG_PRECISION_KZ_PRECISION_2024_TENDER_CONTROL_PREMIUM_LISTED_BENEFICIARY_BRIDGE", "stage2_evidence_fields": ["governance_event", "tender_or_control_transfer_candidate", "economic_beneficiary_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "closing_or_minority_economics_bridge_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "minority_or_tender_cap_risk", "post_peak_drawdown", "MAE_widening"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/036/036560/2024.csv", "profile_path": "atlas/symbol_profiles/036/036560.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 201.31, "MFE_90D_pct": 201.31, "MFE_180D_pct": 201.31, "MAE_30D_pct": 0.0, "MAE_90D_pct": -2.38, "MAE_180D_pct": -15.76, "peak_date": "2024-10-07", "peak_price": 36700.0, "drawdown_after_peak_pct": -72.04, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_tender_or_control_premium_peak_if_economic_beneficiary_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_deal_failure_tender_cap_minority_closing_financing_or_operating_break", "trigger_outcome_label": "governance_lifecycle_positive_with_later_4b_watch", "current_profile_verdict": "C32 should allow a tender/control-premium lifecycle candidate when the listed company is a direct economic beneficiary of tender terms, control dispute or stake economics. Young Poong Precision/KZ Precision produced very large MFE, but post-tender drawdown means lifecycle local 4B is mandatory once tender/control-premium evidence fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C32_GOVERNANCE_036560_2024-09-13", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R12L75-C32-001750-HANYANG-SECURITIES-CONTROL-SALE-PREMIUM-FADE", "case_id": "R12L75-C32-001750-HANYANG-SECURITIES-CONTROL-SALE-PREMIUM-FADE", "symbol": "001750", "company_name": "한양증권", "round": "R12", "loop": "75", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "TENDER_OFFER_CONTROL_TRANSFER_DISPUTE_ECONOMIC_BENEFICIARY_BRIDGE_VS_HEADLINE_FADE", "loop_objective": "governance_event_lifecycle_test|counterexample_mining|tender_control_premium_guardrail", "trigger_type": "Stage2-FalsePositive / SecuritiesControlSalePremiumFade", "trigger_date": "2024-07-23", "entry_date": "2024-07-24", "entry_price": 15650.0, "evidence_available_at_that_date": "SECURITIES_CONTROL_SALE_HEADLINE_WITH_WEAK_MINORITIY_TENDER_CLOSING_ECONOMIC_BENEFICIARY_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:HANYANG_SECURITIES_2024_CONTROL_SALE_PREFERRED_BIDDER_TENDER_MINORITY_CLOSING_BRIDGE", "stage2_evidence_fields": ["governance_event", "tender_or_control_transfer_candidate", "economic_beneficiary_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "closing_or_minority_economics_bridge_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "minority_or_tender_cap_risk", "post_peak_drawdown", "MAE_widening"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001750/2024.csv", "profile_path": "atlas/symbol_profiles/001/001750.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 24.03, "MFE_90D_pct": 24.03, "MFE_180D_pct": 24.03, "MAE_30D_pct": -9.78, "MAE_90D_pct": -16.93, "MAE_180D_pct": -21.92, "peak_date": "2024-08-05", "peak_price": 19410.0, "drawdown_after_peak_pct": -37.04, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_tender_or_control_premium_peak_if_economic_beneficiary_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_deal_failure_tender_cap_minority_closing_financing_or_operating_break", "trigger_outcome_label": "counterexample_control_sale_premium_fade", "current_profile_verdict": "C32 should not treat a control-sale or preferred-bidder headline as durable Stage2 unless minority economics, tender floor, closing certainty or listed-shareholder beneficiary bridge is explicit. Hanyang Securities had a tradable MFE but then faded into local 4B risk.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C32_GOVERNANCE_001750_2024-07-24", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R12L75-C32-008930-HANMI-SCIENCE-CONTROL-DISPUTE-BENEFICIARY-FADE", "case_id": "R12L75-C32-008930-HANMI-SCIENCE-CONTROL-DISPUTE-BENEFICIARY-FADE", "symbol": "008930", "company_name": "한미사이언스", "round": "R12", "loop": "75", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "TENDER_OFFER_CONTROL_TRANSFER_DISPUTE_ECONOMIC_BENEFICIARY_BRIDGE_VS_HEADLINE_FADE", "loop_objective": "governance_event_lifecycle_test|counterexample_mining|tender_control_premium_guardrail", "trigger_type": "Stage2-FalsePositive / FamilyControlDisputeBeneficiaryFade", "trigger_date": "2024-01-12", "entry_date": "2024-01-15", "entry_price": 46350.0, "evidence_available_at_that_date": "FAMILY_CONTROL_DISPUTE_GROUP_COMBINATION_HEADLINE_WITH_WEAK_MINORITIY_ECONOMIC_BENEFICIARY_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:HANMI_SCIENCE_2024_CONTROL_DISPUTE_GROUP_COMBINATION_LISTED_SHAREHOLDER_BENEFICIARY_BRIDGE", "stage2_evidence_fields": ["governance_event", "tender_or_control_transfer_candidate", "economic_beneficiary_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "closing_or_minority_economics_bridge_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "minority_or_tender_cap_risk", "post_peak_drawdown", "MAE_widening"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/008/008930/2024.csv", "profile_path": "atlas/symbol_profiles/008/008930.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 21.25, "MFE_90D_pct": 21.25, "MFE_180D_pct": 21.25, "MAE_30D_pct": -16.5, "MAE_90D_pct": -24.7, "MAE_180D_pct": -44.44, "peak_date": "2024-01-16", "peak_price": 56200.0, "drawdown_after_peak_pct": -54.18, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_tender_or_control_premium_peak_if_economic_beneficiary_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_deal_failure_tender_cap_minority_closing_financing_or_operating_break", "trigger_outcome_label": "counterexample_control_dispute_local4b_with_sharecount_validation", "current_profile_verdict": "C32 should not treat control dispute or group-combination headlines as durable Stage2 unless listed-shareholder beneficiary, transaction mechanics, closing certainty, capital policy or operating bridge is explicit. Hanmi Science produced an event spike but later opened severe MAE and requires share-count validation.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": true, "same_entry_group_id": "C32_GOVERNANCE_008930_2024-01-15", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L75-C32-036560-YP-PRECISION-TENDER-CONTROL-PREMIUM-LIFECYCLE", "trigger_id": "TRG_R12L75-C32-036560-YP-PRECISION-TENDER-CONTROL-PREMIUM-LIFECYCLE", "symbol": "036560", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"governance_event_score": 15, "tender_or_control_premium_score": 16, "closing_certainty_score": 10, "minority_economics_score": 13, "listed_entity_beneficiary_score": 14, "relative_strength_score": 16, "execution_risk_score": 10, "dilution_or_sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_before": 82, "stage_label_before": "Governance lifecycle Stage2 after source repair", "raw_component_scores_after": {"governance_event_score": 8, "tender_or_control_premium_score": 18, "closing_certainty_score": 12, "minority_economics_score": 16, "listed_entity_beneficiary_score": 16, "relative_strength_score": 15, "execution_risk_score": 12, "dilution_or_sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_after": 88, "stage_label_after": "Governance lifecycle Stage2/Yellow after source repair + local 4B", "changed_components": ["tender_or_control_premium_score", "closing_certainty_score", "minority_economics_score", "listed_entity_beneficiary_score", "execution_risk_score"], "component_delta_explanation": "Governance event scores should be capped unless tender terms, closing certainty, minority economics and listed-entity beneficiary bridge are verified.", "MFE_90D_pct": 201.31, "MAE_90D_pct": -2.38, "score_return_alignment_label": "tender_control_premium_lifecycle_positive", "current_profile_verdict": "C32 should allow a tender/control-premium lifecycle candidate when the listed company is a direct economic beneficiary of tender terms, control dispute or stake economics. Young Poong Precision/KZ Precision produced very large MFE, but post-tender drawdown means lifecycle local 4B is mandatory once tender/control-premium evidence fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L75-C32-001750-HANYANG-SECURITIES-CONTROL-SALE-PREMIUM-FADE", "trigger_id": "TRG_R12L75-C32-001750-HANYANG-SECURITIES-CONTROL-SALE-PREMIUM-FADE", "symbol": "001750", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"governance_event_score": 15, "tender_or_control_premium_score": 8, "closing_certainty_score": 3, "minority_economics_score": 2, "listed_entity_beneficiary_score": 4, "relative_strength_score": 8, "execution_risk_score": 18, "dilution_or_sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_before": 54, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"governance_event_score": 8, "tender_or_control_premium_score": 4, "closing_certainty_score": 2, "minority_economics_score": 1, "listed_entity_beneficiary_score": 2, "relative_strength_score": 5, "execution_risk_score": 21, "dilution_or_sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_after": 41, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["tender_or_control_premium_score", "closing_certainty_score", "minority_economics_score", "listed_entity_beneficiary_score", "execution_risk_score"], "component_delta_explanation": "Governance event scores should be capped unless tender terms, closing certainty, minority economics and listed-entity beneficiary bridge are verified.", "MFE_90D_pct": 24.03, "MAE_90D_pct": -16.93, "score_return_alignment_label": "governance_headline_false_positive_bridge_gap", "current_profile_verdict": "C32 should not treat a control-sale or preferred-bidder headline as durable Stage2 unless minority economics, tender floor, closing certainty or listed-shareholder beneficiary bridge is explicit. Hanyang Securities had a tradable MFE but then faded into local 4B risk."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L75-C32-008930-HANMI-SCIENCE-CONTROL-DISPUTE-BENEFICIARY-FADE", "trigger_id": "TRG_R12L75-C32-008930-HANMI-SCIENCE-CONTROL-DISPUTE-BENEFICIARY-FADE", "symbol": "008930", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"governance_event_score": 15, "tender_or_control_premium_score": 8, "closing_certainty_score": 3, "minority_economics_score": 2, "listed_entity_beneficiary_score": 4, "relative_strength_score": 8, "execution_risk_score": 18, "dilution_or_sharecount_validation_risk": 8, "source_confidence_score": 2}, "weighted_score_before": 54, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"governance_event_score": 8, "tender_or_control_premium_score": 4, "closing_certainty_score": 2, "minority_economics_score": 1, "listed_entity_beneficiary_score": 2, "relative_strength_score": 5, "execution_risk_score": 21, "dilution_or_sharecount_validation_risk": 10, "source_confidence_score": 2}, "weighted_score_after": 41, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["tender_or_control_premium_score", "closing_certainty_score", "minority_economics_score", "listed_entity_beneficiary_score", "execution_risk_score"], "component_delta_explanation": "Governance event scores should be capped unless tender terms, closing certainty, minority economics and listed-entity beneficiary bridge are verified.", "MFE_90D_pct": 21.25, "MAE_90D_pct": -24.7, "score_return_alignment_label": "governance_headline_false_positive_bridge_gap", "current_profile_verdict": "C32 should not treat control dispute or group-combination headlines as durable Stage2 unless listed-shareholder beneficiary, transaction mechanics, closing certainty, capital policy or operating bridge is explicit. Hanmi Science produced an event spike but later opened severe MAE and requires share-count validation."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R12", "loop": 75, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "TENDER_OFFER_CONTROL_TRANSFER_DISPUTE_ECONOMIC_BENEFICIARY_BRIDGE_VS_HEADLINE_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 1, "current_profile_error_count": 2, "diversity_score_summary": "+3 underused C32 governance/control symbols outside top-covered set and outside loop-74 R12 names, +3 tender/control-sale/family-dispute trigger families, +1 tender lifecycle winner, +2 governance headline fade local-4B counterexamples, no hard duplicate", "residual_contribution_label": "governance_lifecycle_guardrail_with_source_repair_and_sharecount_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R12", "loop": 75, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "axis": "tender_offer_control_transfer_dispute_economic_beneficiary_bridge_vs_headline_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C32 should split true tender/control-premium listed-beneficiary cases from control-sale or family-dispute headline beta. Stage2 requires tender mechanics, closing certainty, minority economics, listed-entity beneficiary, capital policy or operating bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["036560", "001750", "008930"], "share_count_validation_required": ["008930"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R12", "loop": 75, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "existing_axis_strengthened": ["price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "local_4b_watch_guard", "stage2_required_bridge", "share_count_validation_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C32 governance events need economic-beneficiary proof. Young Poong Precision/KZ Precision shows tender/control-premium lifecycle MFE; Hanyang Securities and Hanmi Science show control-sale/control-dispute headlines fading into local 4B when minority economics or listed-beneficiary bridge is absent."}
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
036560:
  name = 영풍정밀 in 2024, KZ정밀 after 2025-04-10
  corporate_action_candidate_dates = 2008-04-14
  selected window = 2024-09-13~D+180
  contamination = false

001750:
  corporate_action_candidate_dates = none
  selected window = 2024-07-24~D+180
  contamination = false

008930:
  corporate_action_candidate_dates = 1999-04-19, 2010-07-30, 2010-10-21, 2012-05-14
  selected window = 2024-01-15~D+180
  contamination = false
  share_count_change_inside_window = true → coding-agent validation required
```

Data-quality caveat:

```text
All selected C32 rows are source_proxy_only / evidence_url_pending.
008930 also requires share-count validation before runtime promotion.
This MD is useful for stock-web path calibration and C32 rule-shape discovery,
but coding-agent promotion requires non-proxy tender/control mechanics, closing certainty, minority economics, listed-entity beneficiary, capital policy and operating bridge evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R12/C32 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair and 008930 needs share-count validation.

Candidate axis:
tender_offer_control_transfer_dispute_economic_beneficiary_bridge_vs_headline_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 036560, 001750 and 008930.
4. Validate 008930 share-count changes inside the selected window.
5. Keep generic C32 governance/control-premium weight unchanged until source repair is complete.
6. Consider Stage2 only when:
   - transaction mechanics are explicit,
   - tender terms, minority economics or shareholder benefit is visible,
   - closing path or stake-control path is credible,
   - economic beneficiary is clear by listed entity,
   - MAE remains controlled or the signal is deliberately lifecycle-managed.
7. Consider local 4B-watch when:
   - the trigger is governance/control/tender headline only,
   - minority/tender/beneficiary bridge is absent or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
8. Do not apply the same label to seller, acquirer, operating company and minority shareholder.
9. Do not convert local 4B-watch into hard 4C without non-price deal failure, legal break, financing, operating deterioration or insolvency evidence.
10. Emit before/after diagnostics and reject if verified tender/control-premium lifecycle positives are overblocked.
```

---

## Final round state

```text
completed_round = R12
completed_loop = 75
next_round = R13
next_loop = 75
round_schedule_status = valid
round_sector_consistency = pass
```

