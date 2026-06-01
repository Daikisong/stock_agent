# E2R Stock-Web v12 Residual Research — R11 Loop 80 / L10 / C32

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R11",
  "scheduled_loop": 80,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R11",
  "completed_loop": 80,
  "computed_next_round": "R12",
  "computed_next_loop": 80,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP",
  "fine_archetype_id": "CONTROL_PREMIUM_TENDER_CAP_EVENT_PRICE_ANCHOR_VS_GOVERNANCE_SPIKE_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "governance_control_premium_tender_cap_guardrail",
    "tender_price_event_anchor_vs_unanchored_governance_spike",
    "event_cap_status_validation_queue_creation",
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

Previous completed state in this interactive run: R10 / loop 80.

Therefore:

```text
scheduled_round = R11
scheduled_loop = 80
allowed_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC or L1_INDUSTRIALS_INFRA_DEFENSE_GRID depending on policy-defense linkage
selected_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
selected_canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
computed_next_round = R12
computed_next_loop = 80
```

R11 was routed to C32 because this run focuses on governance/control premium and tender-cap mechanics, not defense export framework.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C32 concentration in:

```text
010130, 041510, 000240, 고려아연, 에스엠
```

This run uses three different symbols:

```text
036560 / 영풍정밀·KZ정밀 / tender battle price-anchor event lifecycle
008930 / 한미사이언스 / unanchored governance merger/proxy-fight spike fade
115390 / 락앤락 / tender offer price-cap and delisting/status validation
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
008930 requires share-count validation.
115390 requires inactive/delisted-like status validation.
036560 requires event-end / later name-change continuity validation.
```

## Research thesis

C32 is not “지배구조 이슈로 올랐다.”

The mechanism must pass through:

```text
control-premium / tender / governance event
→ explicit tender or control-price anchor
→ ownership, free-float or vote mechanics
→ acceptance window or legal/event timetable
→ completion probability and downside cap
→ event-end / status validation
```

지배구조 이벤트는 불꽃이 아니라 계약서의 유효기간이다.  
C32가 보려는 것은 불꽃의 높이가 아니라 가격 앵커, 수락 기간, 표 대결, 완료 확률, 종료 후 낙폭이다.

---

## Case 1 — Tender battle positive: 036560 / 영풍정밀·KZ정밀

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
name_change_after_window = true
event_end_validation_required = true
source_repair_required = true
```

The source-repair task is tender price, acceptance window, ownership/free-float mechanics and event-end bridge evidence.

```text
evidence_family = CONTROL_PREMIUM_TENDER_BATTLE_TENDER_PRICE_ANCHOR_OWNERSHIP_STRUCTURE_ACCEPTANCE_WINDOW_FREEFLOAT_EVENT_END_BRIDGE
case_role = positive_tender_battle_price_anchor_with_event_end_4b_watch
trigger_date = 2024-09-12
entry_date = 2024-09-13
entry_price = 12,180
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/036/036560/2024.csv` and 2025 continuation:

```text
2024-09-13,12180,12180,12180,12180
2024-09-19,15830,15830,15830,15830
2024-09-20,20550,20550,20550,20550
2024-09-26,25150,25300,24700,24950
2024-10-04,29900,32850,29850,31850
2024-10-07,34200,36700,33300,34700
2024-10-18,28900,30050,22300,22650
2024-10-31,18430,22250,17050,19300
2025-04-07,10410,11010,10260,10290
```

### Backtest

```text
MFE_30D  = +201.31%
MAE_30D  = +0.00%
MFE_90D  = +201.31%
MAE_90D  = -10.26%
MFE_180D = +201.31%
MAE_180D = -15.76%
peak_180 = 36,700 on 2024-10-07
trough_180 = 10,260 on 2025-04-07
peak_to_later_drawdown = -72.04%
```

### Interpretation

This is a C32 event-anchored positive, not a normal rerating row.  
The tender/control premium made the MFE real, but event-end drawdown risk is the point.

Correct treatment:

```text
verified tender price / ownership / free-float / acceptance window → Stage2 event candidate
event anchor ends or completion bridge fades → lifecycle local 4B-watch
```

---

## Case 2 — Governance spike fade: 008930 / 한미사이언스

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_validation_required = true
source_repair_required = true
```

This row tests governance merger / proxy-fight beta without a stable tender/control-price anchor.

```text
evidence_family = GOVERNANCE_MERGER_PROXY_FIGHT_CONTROL_PREMIUM_THEME_WITH_WEAK_TENDER_PRICE_ANCHOR_AND_COMPLETION_BRIDGE
case_role = counterexample_unanchored_governance_spike_local4b
trigger_date = 2024-01-12
entry_date = 2024-01-15
entry_price = 46,350
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/008/008930/2024.csv`:

```text
2024-01-15,46350,47650,40450,43300
2024-01-16,42300,56200,42200,56200
2024-01-19,43700,44550,40450,41000
2024-03-28,41350,47000,38000,44350
2024-08-05,30000,30250,25750,26750
2024-10-24,32850,42150,32400,39150
2024-10-30,43300,52500,42600,52100
2024-11-01,49200,49200,34500,36250
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

This is the C32 unanchored governance-spike counterexample.  
Without tender/control price, vote-completion probability and downside cap, the spike should not be durable Stage2.

Correct treatment:

```text
governance/proxy-fight theme beta
→ no verified tender price / completion / vote bridge
→ local 4B-watch
```

---

## Case 3 — Tender price cap / status validation: 115390 / 락앤락

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
status_validation_required = true
source_repair_required = true
```

The source-repair task is tender offer price, acceptance window, completion, free-float and delisting/status bridge evidence.

```text
evidence_family = TENDER_OFFER_VOLUNTARY_DELISTING_PRICE_CAP_ACCEPTANCE_WINDOW_FREEFLOAT_COMPLETION_STATUS_BRIDGE
case_role = positive_tender_price_cap_status_validation
trigger_date = 2024-04-16
entry_date = 2024-04-17
entry_price = 7,360
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/115/115390/2024.csv`:

```text
2024-04-17,7360,8290,7360,8180
2024-04-18,8700,8720,8670,8680
2024-04-26,8700,8710,8690,8700
2024-05-08,8700,8890,8700,8700
2024-06-11,8760,8820,8750,8780
2024-08-05,8760,8760,8750,8750
2024-10-11,8630,8640,8270,8600
2024-11-08,8650,8690,8650,8660
```

### Backtest

```text
MFE_30D  = +20.79%
MAE_30D  = +0.00%
MFE_90D  = +20.79%
MAE_90D  = +0.00%
MFE_180D = +20.79%
MAE_180D = -0.14%
peak_180 = 8,890 on 2024-05-08
trough_180 = 7,350 on 2024-04-17
peak_to_later_drawdown = -7.42%
```

### Interpretation

This is a tender price-cap row.  
The upside was capped and the price later stayed near event terms, but runtime ingestion must validate inactive/delisted-like status.

Correct treatment:

```text
verified tender offer / acceptance window / delisting bridge → event Stage2 candidate
status validation first
after completion → do not extrapolate as ordinary rerating
```

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
tender_price_anchor_required = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
status_validation_guard = strengthen
event_end_validation_guard = strengthen
full_4b_requires_non_price_evidence = keep
```

### What this does not justify

```text
do_not_raise_generic_C32_governance_theme_weight = true
do_not_treat_all_governance_MFE_as_Green = true
do_not_ingest_tender_or_delisting_rows_without_status_validation = true
do_not_convert_governance_drawdown_to_hard_4C_without_non_price_tender_failure_vote_failure_or_legal_block = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
CONTROL_PREMIUM_TENDER_CAP_EVENT_PRICE_ANCHOR_VS_GOVERNANCE_SPIKE_FADE
```

This fine archetype covers:

```text
1. tender/control premium battle with explicit price anchor → event Stage2 possible, lifecycle-managed
2. unanchored governance/proxy-fight spike → false Stage2 / local 4B
3. tender-offer price cap with delisting/status endpoint → event candidate only after status validation
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R11L80-C32-036560-YOUNGPOONG-PRECISION-TENDER-BATTLE-CAP", "symbol": "036560", "company_name": "영풍정밀/KZ정밀", "round": "R11", "loop": "80", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_CAP_EVENT_PRICE_ANCHOR_VS_GOVERNANCE_SPIKE_FADE", "case_type": "governance_control_premium_tender_cap", "positive_or_counterexample": "positive", "best_trigger": "Stage2-EventLifecycle-ControlPremiumTenderBattlePriceAnchorWithLocal4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C32 should allow tender-battle positives only when tender price, acceptance window, ownership structure, free-float and event-end mechanics are explicit. Young Poong Precision/KZ Precision produced enormous event MFE, then the post-event path required local 4B discipline.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy tender price, acceptance window, ownership/free-float, vote/timetable, completion probability, event-end and status validation required before runtime promotion."}
{"row_type": "case", "case_id": "R11L80-C32-008930-HANMI-SCIENCE-GOVERNANCE-MERGER-PROXY-SPIKE-FADE", "symbol": "008930", "company_name": "한미사이언스", "round": "R11", "loop": "80", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_CAP_EVENT_PRICE_ANCHOR_VS_GOVERNANCE_SPIKE_FADE", "case_type": "governance_control_premium_tender_cap", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / GovernanceMergerProxyFightSpikeFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C32 should not treat governance/proxy-fight spike beta as durable Stage2 unless a clear tender/control-price anchor, completion probability, legal timetable, shareholder vote mechanics and downside cap are visible. Hanmi Science produced a sharp spike then a severe drawdown.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy tender price, acceptance window, ownership/free-float, vote/timetable, completion probability, event-end and status validation required before runtime promotion."}
{"row_type": "case", "case_id": "R11L80-C32-115390-LOCKNLOCK-TENDER-PRICE-CAP-DELISTING", "symbol": "115390", "company_name": "락앤락", "round": "R11", "loop": "80", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_CAP_EVENT_PRICE_ANCHOR_VS_GOVERNANCE_SPIKE_FADE", "case_type": "governance_control_premium_tender_cap", "positive_or_counterexample": "positive", "best_trigger": "Stage2-EventCap-TenderOfferPriceCapWithStatusValidation", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C32 should distinguish tender-offer price-cap trades from open-ended governance rerating. LocknLock was anchored by a tender/de-listing style price cap and later became inactive_or_delisted_like, so runtime ingestion requires status validation.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy tender price, acceptance window, ownership/free-float, vote/timetable, completion probability, event-end and status validation required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R11L80-C32-036560-YOUNGPOONG-PRECISION-TENDER-BATTLE-CAP", "case_id": "R11L80-C32-036560-YOUNGPOONG-PRECISION-TENDER-BATTLE-CAP", "symbol": "036560", "company_name": "영풍정밀/KZ정밀", "round": "R11", "loop": "80", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_CAP_EVENT_PRICE_ANCHOR_VS_GOVERNANCE_SPIKE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|governance_control_premium_tender_cap_guardrail", "trigger_type": "Stage2-EventLifecycle-ControlPremiumTenderBattlePriceAnchorWithLocal4B", "trigger_date": "2024-09-12", "entry_date": "2024-09-13", "entry_price": 12180.0, "evidence_available_at_that_date": "CONTROL_PREMIUM_TENDER_BATTLE_TENDER_PRICE_ANCHOR_OWNERSHIP_STRUCTURE_ACCEPTANCE_WINDOW_FREEFLOAT_EVENT_END_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:YOUNGPOONG_PRECISION_2024_CONTROL_PREMIUM_TENDER_BATTLE_ACCEPTANCE_WINDOW_FREEFLOAT_EVENT_END_BRIDGE", "stage2_evidence_fields": ["tender_or_control_price_anchor", "ownership_freefloat_or_vote_candidate", "completion_status_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "acceptance_window_or_event_timetable_candidate"], "stage4b_evidence_fields": ["governance_theme_beta", "event_anchor_stale_or_absent", "post_peak_drawdown", "event_end_gap"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/036/036560/2024.csv", "profile_path": "atlas/symbol_profiles/036/036560.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 201.31, "MFE_90D_pct": 201.31, "MFE_180D_pct": 201.31, "MAE_30D_pct": 0.0, "MAE_90D_pct": -10.26, "MAE_180D_pct": -15.76, "peak_date": "2024-10-07", "peak_price": 36700.0, "drawdown_after_peak_pct": -72.04, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_control_premium_peak_if_tender_anchor_vote_completion_or_status_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_tender_failure_vote_failure_legal_block_completion_failure_or_financing_break", "trigger_outcome_label": "positive_tender_battle_price_anchor_with_event_end_4b_watch", "current_profile_verdict": "C32 should allow tender-battle positives only when tender price, acceptance window, ownership structure, free-float and event-end mechanics are explicit. Young Poong Precision/KZ Precision produced enormous event MFE, then the post-event path required local 4B discipline.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_status_validation_required", "share_count_change_inside_window": false, "same_entry_group_id": "C32_GOVERNANCE_CONTROL_036560_2024-09-13", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R11L80-C32-008930-HANMI-SCIENCE-GOVERNANCE-MERGER-PROXY-SPIKE-FADE", "case_id": "R11L80-C32-008930-HANMI-SCIENCE-GOVERNANCE-MERGER-PROXY-SPIKE-FADE", "symbol": "008930", "company_name": "한미사이언스", "round": "R11", "loop": "80", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_CAP_EVENT_PRICE_ANCHOR_VS_GOVERNANCE_SPIKE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|governance_control_premium_tender_cap_guardrail", "trigger_type": "Stage2-FalsePositive / GovernanceMergerProxyFightSpikeFade", "trigger_date": "2024-01-12", "entry_date": "2024-01-15", "entry_price": 46350.0, "evidence_available_at_that_date": "GOVERNANCE_MERGER_PROXY_FIGHT_CONTROL_PREMIUM_THEME_WITH_WEAK_TENDER_PRICE_ANCHOR_AND_COMPLETION_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:HANMI_SCIENCE_2024_GOVERNANCE_MERGER_PROXY_FIGHT_TENDER_PRICE_ANCHOR_VOTE_COMPLETION_BRIDGE", "stage2_evidence_fields": ["tender_or_control_price_anchor", "ownership_freefloat_or_vote_candidate", "completion_status_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "acceptance_window_or_event_timetable_candidate"], "stage4b_evidence_fields": ["governance_theme_beta", "event_anchor_stale_or_absent", "post_peak_drawdown", "event_end_gap"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/008/008930/2024.csv", "profile_path": "atlas/symbol_profiles/008/008930.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 21.25, "MFE_90D_pct": 21.25, "MFE_180D_pct": 21.25, "MAE_30D_pct": -16.5, "MAE_90D_pct": -24.7, "MAE_180D_pct": -44.44, "peak_date": "2024-01-16", "peak_price": 56200.0, "drawdown_after_peak_pct": -54.18, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_control_premium_peak_if_tender_anchor_vote_completion_or_status_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_tender_failure_vote_failure_legal_block_completion_failure_or_financing_break", "trigger_outcome_label": "counterexample_unanchored_governance_spike_local4b", "current_profile_verdict": "C32 should not treat governance/proxy-fight spike beta as durable Stage2 unless a clear tender/control-price anchor, completion probability, legal timetable, shareholder vote mechanics and downside cap are visible. Hanmi Science produced a sharp spike then a severe drawdown.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_status_validation_required", "share_count_change_inside_window": true, "same_entry_group_id": "C32_GOVERNANCE_CONTROL_008930_2024-01-15", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R11L80-C32-115390-LOCKNLOCK-TENDER-PRICE-CAP-DELISTING", "case_id": "R11L80-C32-115390-LOCKNLOCK-TENDER-PRICE-CAP-DELISTING", "symbol": "115390", "company_name": "락앤락", "round": "R11", "loop": "80", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_CAP_EVENT_PRICE_ANCHOR_VS_GOVERNANCE_SPIKE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|governance_control_premium_tender_cap_guardrail", "trigger_type": "Stage2-EventCap-TenderOfferPriceCapWithStatusValidation", "trigger_date": "2024-04-16", "entry_date": "2024-04-17", "entry_price": 7360.0, "evidence_available_at_that_date": "TENDER_OFFER_VOLUNTARY_DELISTING_PRICE_CAP_ACCEPTANCE_WINDOW_FREEFLOAT_COMPLETION_STATUS_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:LOCKNLOCK_2024_TENDER_OFFER_VOLUNTARY_DELISTING_PRICE_CAP_ACCEPTANCE_COMPLETION_STATUS_BRIDGE", "stage2_evidence_fields": ["tender_or_control_price_anchor", "ownership_freefloat_or_vote_candidate", "completion_status_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "acceptance_window_or_event_timetable_candidate"], "stage4b_evidence_fields": ["governance_theme_beta", "event_anchor_stale_or_absent", "post_peak_drawdown", "event_end_gap"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/115/115390/2024.csv", "profile_path": "atlas/symbol_profiles/115/115390.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 20.79, "MFE_90D_pct": 20.79, "MFE_180D_pct": 20.79, "MAE_30D_pct": 0.0, "MAE_90D_pct": 0.0, "MAE_180D_pct": -0.14, "peak_date": "2024-05-08", "peak_price": 8890.0, "drawdown_after_peak_pct": -7.42, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_control_premium_peak_if_tender_anchor_vote_completion_or_status_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_tender_failure_vote_failure_legal_block_completion_failure_or_financing_break", "trigger_outcome_label": "positive_tender_price_cap_status_validation", "current_profile_verdict": "C32 should distinguish tender-offer price-cap trades from open-ended governance rerating. LocknLock was anchored by a tender/de-listing style price cap and later became inactive_or_delisted_like, so runtime ingestion requires status validation.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_status_validation_required", "share_count_change_inside_window": false, "same_entry_group_id": "C32_GOVERNANCE_CONTROL_115390_2024-04-17", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L80-C32-036560-YOUNGPOONG-PRECISION-TENDER-BATTLE-CAP", "trigger_id": "TRG_R11L80-C32-036560-YOUNGPOONG-PRECISION-TENDER-BATTLE-CAP", "symbol": "036560", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"tender_price_anchor_score": 15, "ownership_vote_freefloat_score": 14, "completion_probability_score": 13, "event_timetable_status_score": 13, "downside_cap_score": 12, "relative_strength_score": 14, "validation_risk": 10, "execution_risk_score": 10, "source_confidence_score": 2}, "weighted_score_before": 80, "stage_label_before": "Event lifecycle candidate after source repair", "raw_component_scores_after": {"tender_price_anchor_score": 17, "ownership_vote_freefloat_score": 16, "completion_probability_score": 15, "event_timetable_status_score": 15, "downside_cap_score": 14, "relative_strength_score": 13, "validation_risk": 12, "execution_risk_score": 11, "source_confidence_score": 2}, "weighted_score_after": 86, "stage_label_after": "Event-capped Stage2 after source repair + lifecycle 4B", "changed_components": ["tender_price_anchor_score", "ownership_vote_freefloat_score", "completion_probability_score", "event_timetable_status_score", "downside_cap_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified tender/control-price anchor, ownership/free-float/vote mechanics, completion probability, event timetable and downside cap; cap unanchored governance/proxy-fight spikes.", "MFE_90D_pct": 201.31, "MAE_90D_pct": -10.26, "score_return_alignment_label": "control_premium_tender_cap_positive_with_lifecycle_4b", "current_profile_verdict": "C32 should allow tender-battle positives only when tender price, acceptance window, ownership structure, free-float and event-end mechanics are explicit. Young Poong Precision/KZ Precision produced enormous event MFE, then the post-event path required local 4B discipline."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L80-C32-008930-HANMI-SCIENCE-GOVERNANCE-MERGER-PROXY-SPIKE-FADE", "trigger_id": "TRG_R11L80-C32-008930-HANMI-SCIENCE-GOVERNANCE-MERGER-PROXY-SPIKE-FADE", "symbol": "008930", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"tender_price_anchor_score": 4, "ownership_vote_freefloat_score": 4, "completion_probability_score": 2, "event_timetable_status_score": 2, "downside_cap_score": 2, "relative_strength_score": 14, "validation_risk": 10, "execution_risk_score": 24, "source_confidence_score": 2}, "weighted_score_before": 42, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"tender_price_anchor_score": 2, "ownership_vote_freefloat_score": 2, "completion_probability_score": 1, "event_timetable_status_score": 1, "downside_cap_score": 1, "relative_strength_score": 3, "validation_risk": 12, "execution_risk_score": 26, "source_confidence_score": 2}, "weighted_score_after": 31, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["tender_price_anchor_score", "ownership_vote_freefloat_score", "completion_probability_score", "event_timetable_status_score", "downside_cap_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified tender/control-price anchor, ownership/free-float/vote mechanics, completion probability, event timetable and downside cap; cap unanchored governance/proxy-fight spikes.", "MFE_90D_pct": 21.25, "MAE_90D_pct": -24.7, "score_return_alignment_label": "false_positive_unanchored_governance_spike", "current_profile_verdict": "C32 should not treat governance/proxy-fight spike beta as durable Stage2 unless a clear tender/control-price anchor, completion probability, legal timetable, shareholder vote mechanics and downside cap are visible. Hanmi Science produced a sharp spike then a severe drawdown."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L80-C32-115390-LOCKNLOCK-TENDER-PRICE-CAP-DELISTING", "trigger_id": "TRG_R11L80-C32-115390-LOCKNLOCK-TENDER-PRICE-CAP-DELISTING", "symbol": "115390", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"tender_price_anchor_score": 15, "ownership_vote_freefloat_score": 14, "completion_probability_score": 13, "event_timetable_status_score": 13, "downside_cap_score": 12, "relative_strength_score": 14, "validation_risk": 10, "execution_risk_score": 10, "source_confidence_score": 2}, "weighted_score_before": 80, "stage_label_before": "Event lifecycle candidate after source repair", "raw_component_scores_after": {"tender_price_anchor_score": 17, "ownership_vote_freefloat_score": 16, "completion_probability_score": 15, "event_timetable_status_score": 15, "downside_cap_score": 14, "relative_strength_score": 13, "validation_risk": 12, "execution_risk_score": 11, "source_confidence_score": 2}, "weighted_score_after": 86, "stage_label_after": "Event-capped Stage2 after source repair + lifecycle 4B", "changed_components": ["tender_price_anchor_score", "ownership_vote_freefloat_score", "completion_probability_score", "event_timetable_status_score", "downside_cap_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified tender/control-price anchor, ownership/free-float/vote mechanics, completion probability, event timetable and downside cap; cap unanchored governance/proxy-fight spikes.", "MFE_90D_pct": 20.79, "MAE_90D_pct": 0.0, "score_return_alignment_label": "control_premium_tender_cap_positive_with_lifecycle_4b", "current_profile_verdict": "C32 should distinguish tender-offer price-cap trades from open-ended governance rerating. LocknLock was anchored by a tender/de-listing style price cap and later became inactive_or_delisted_like, so runtime ingestion requires status validation."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R11", "loop": 80, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_CAP_EVENT_PRICE_ANCHOR_VS_GOVERNANCE_SPIKE_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 2, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 1, "status_validation_required_count": 1, "name_change_or_event_end_validation_count": 1, "current_profile_error_count": 1, "diversity_score_summary": "+3 C32 governance/control-premium symbols outside top-covered 010130/041510/000240/SM set, +3 tender-battle/proxy-fight/tender-cap trigger families, +2 event-anchored positives, +1 unanchored governance spike local-4B counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_status_and_event_end_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R11", "loop": 80, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "axis": "control_premium_tender_cap_event_price_anchor_vs_governance_spike_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C32 should split event-anchored tender/control-premium trades from unanchored governance/proxy-fight spikes. Stage2 requires tender/control price, ownership/free-float or vote mechanics, acceptance window/event timetable, completion probability and downside cap. If event anchor ends or completion bridge fails, route to local 4B-watch. Status/name-change/share-count flags block runtime promotion until validated.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["036560", "008930", "115390"], "status_validation_required": ["115390"], "share_count_validation_required": ["008930"], "event_end_or_name_change_validation_required": ["036560"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R11", "loop": 80, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "existing_axis_strengthened": ["stage2_required_bridge", "tender_price_anchor_required", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "status_validation_guard", "event_end_validation_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C32 needs tender/control price, ownership/free-float or vote mechanics, acceptance window, completion probability and status proof. Young Poong Precision and LocknLock show event-anchored tender-cap positives after validation; Hanmi Science shows an unanchored governance/proxy-fight spike fading into local 4B."}
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
production_scoring_changed = false
shadow_weight_only = true
```

Profile checks:

```text
036560:
  name = 영풍정밀 during selected 2024 window; KZ정밀 from 2025-04-10
  corporate_action_candidate_dates = 2008-04-14
  selected window starts 2024-09-13
  contamination = false by profile
  event_end_or_name_change_validation_required = true

008930:
  name = 한미사이언스
  corporate_action_candidate_dates = 1999-04-19, 2010-07-30, 2010-10-21, 2012-05-14
  selected window = 2024-01-15~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required

115390:
  name = 락앤락
  corporate_action_candidate_dates = none
  selected window starts 2024-04-17
  status_inferred = inactive_or_delisted_like
  status_validation_required = true
```

Data-quality caveat:

```text
All selected C32 rows are source_proxy_only / evidence_url_pending.
036560 requires event-end / later name-change validation.
008930 requires share-count validation.
115390 requires status / inactive-or-delisted-like validation.
This MD is useful for stock-web path calibration and C32 rule-shape discovery,
but coding-agent promotion requires non-proxy tender price, vote/free-float, acceptance window, completion probability and status evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R11/C32 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair and several rows need status/event/share-count validation.

Candidate axis:
control_premium_tender_cap_event_price_anchor_vs_governance_spike_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 036560, 008930 and 115390.
4. Validate 036560 event-end and later KZ정밀 name-change continuity.
5. Validate 008930 share-count changes inside the selected window.
6. Validate 115390 inactive/delisted-like status and tender-completion treatment.
7. Keep generic C32 governance theme weight unchanged until source repair is complete.
8. Consider Stage2 only when:
   - tender/control price anchor is explicit,
   - ownership/free-float or vote mechanics are visible,
   - acceptance window or legal/event timetable exists,
   - completion probability and downside cap are credible,
   - status/event-end bridge is validated.
9. Consider local 4B-watch when:
   - governance/proxy-fight theme beta lacks tender price anchor,
   - completion/vote/status bridge is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%,
   - event-end gap opens after completion.
10. Do not convert local 4B-watch into full 4B/4C without non-price tender failure, vote failure, legal block, completion failure, financing break or status break.
11. Emit before/after diagnostics and reject if event-anchored tender positives or status-capped rows are overblocked.
```

---

## Final round state

```text
completed_round = R11
completed_loop = 80
next_round = R12
next_loop = 80
round_schedule_status = valid
round_sector_consistency = pass
```

