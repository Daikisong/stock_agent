# E2R Stock-Web v12 Residual Research — R7 Loop 73 / L7 / C23

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R7",
  "scheduled_loop": 73,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R7",
  "completed_loop": 73,
  "computed_next_round": "R8",
  "computed_next_loop": 73,
  "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL",
  "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION",
  "fine_archetype_id": "BIO_DRUG_APPROVAL_COMMERCIALIZATION_BRIDGE_VS_APPROVAL_HEADLINE_CHASE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "commercialization_bridge_test",
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
```

## Round / scope resolution

Previous completed state in this interactive run: R6 / loop 73.

Therefore:

```text
scheduled_round = R7
scheduled_loop = 73
allowed_large_sector = L7_BIO_HEALTHCARE_MEDICAL
selected_large_sector = L7_BIO_HEALTHCARE_MEDICAL
selected_canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
computed_next_round = R8
computed_next_loop = 73
```

R7 was routed to C23 because loop 71 used C24 and loop 72 used C25.  
This file tests regulatory approval as a commercialization bridge, not a headline-only bio event.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C23 is concentrated in `000100`, `028300`, `UNKNOWN_SYMBOL`, `145020`, and `196170`.  
This run uses:

```text
068270 / 셀트리온 / FDA-approved biologic commercialization bridge
950210 / 프레스티지바이오파마 / biosimilar approval headline chase
195940 / HK이노엔 / K-CAB-style prescription/export commercialization ramp
```

Data-quality note:

```text
All three rows are stock-web calibration usable.
All three rows are source_proxy_only=true / evidence_url_pending=true.
This file is a source-repair queue plus stock-web path calibration, not immediate runtime weight evidence.
```

## Research thesis

C23 is not “drug approved.”

The real path is:

```text
approval
→ launch or reimbursement access
→ partner order / prescription uptake / channel fill
→ sales and margin bridge
→ durable rerating
```

Approval is the passport.  
Commercialization is the plane actually leaving the runway.

---

## Case 1 — Positive slow bridge: 068270 / 셀트리온

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is U.S. launch, reimbursement access, channel uptake, direct sales and margin bridge.

```text
evidence_family = FDA_APPROVED_BIOLOGIC_US_COMMERCIALIZATION_REIMBURSEMENT_RAMP_BRIDGE
case_role = positive_slow_with_controlled_mae
trigger_date = 2024-04-26
entry_date = 2024-04-29
entry_price = 178,500
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/068/068270/2024.csv`:

```text
2024-04-29,178500,183800,178500,183700
2024-05-07,191000,197000,191000,194400
2024-07-30,207000,211000,203500,209000
2024-11-12,172600,174100,165700,165900
```

### Backtest

```text
MFE_30D  = +10.36%
MAE_30D  = -1.34%
MFE_90D  = +18.21%
MAE_90D  = -3.08%
MFE_180D = +18.21%
MAE_180D = -7.17%
peak_180 = 211,000 on 2024-07-30
trough_180 = 165,700 on 2024-11-12
peak_to_later_drawdown = -21.47%
```

### Interpretation

This is a slower C23 positive.  
The path did not explode like a small-cap approval headline, but the MAE stayed controlled. That is the kind of route a commercialization bridge should allow if reimbursement and sales evidence are verified.

---

## Case 2 — Counterexample: 950210 / 프레스티지바이오파마

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests a late approval/regulatory headline chase without enough visible near-term commercialization bridge.

```text
evidence_family = BIOSIMILAR_REGULATORY_APPROVAL_HEADLINE_WITH_WEAK_NEAR_TERM_COMMERCIALIZATION_BRIDGE
case_role = counterexample
trigger_date = 2024-10-25
entry_date = 2024-10-28
entry_price = 18,150
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/950/950210/2024.csv`:

```text
2024-10-28,18150,20900,18110,19880
2024-11-13,16860,16860,15920,15930
2024-12-09,14320,14540,13140,13350
2024-12-16,15340,16420,15000,16270
```

### Backtest

```text
MFE_30D  = +15.15%
MAE_30D  = -27.60%
MFE_90D  = +15.15%
MAE_90D  = -27.60%
MFE_180D = +15.15%
MAE_180D = -27.60%
peak_180 = 20,900 on 2024-10-28
trough_180 = 13,140 on 2024-12-09
peak_to_later_drawdown = -37.13%
```

### Interpretation

This is the C23 approval-headline trap.  
The same-day MFE existed, but the later path says the approval headline was not enough. C23 should require reimbursement, launch timing, partner order or sales ramp before it becomes durable Stage2.

---

## Case 3 — Positive with later 4B-watch: 195940 / HK이노엔

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is prescription growth, export partner, global launch and revenue conversion evidence.

```text
evidence_family = K_CAP_PRESCRIPTION_EXPORT_PARTNER_COMMERCIALIZATION_REVENUE_BRIDGE
case_role = positive_with_later_4b_watch
trigger_date = 2024-06-14
entry_date = 2024-06-17
entry_price = 36,100
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/195/195940/2024.csv`:

```text
2024-06-17,36100,42400,34550,38000
2024-07-23,41750,42850,40650,40650
2024-08-05,38550,38600,34450,35500
2024-10-07,51900,52000,49850,50400
2024-11-27,39800,39800,35850,37950
```

### Backtest

```text
MFE_30D  = +18.70%
MAE_30D  = -4.29%
MFE_90D  = +44.04%
MAE_90D  = -4.57%
MFE_180D = +44.04%
MAE_180D = -4.57%
peak_180 = 52,000 on 2024-10-07
trough_180 = 34,450 on 2024-08-05
peak_to_later_drawdown = -31.06%
```

### Interpretation

This is the commercial ramp version of C23.  
The price path is better than a pure approval chase: MFE builds over months and entry-basis MAE is contained. Still, if prescription/export partner revenue evidence stops refreshing after the peak, later local 4B-watch should activate.

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
do_not_raise_generic_C23_approval_weight = true
do_not_treat_approval_headline_as_Green_without_commercialization_bridge = true
do_not_convert_commercialization_drawdown_to_hard_4C_without_safety_or_regulatory_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
BIO_DRUG_APPROVAL_COMMERCIALIZATION_BRIDGE_VS_APPROVAL_HEADLINE_CHASE
```

This fine archetype covers:

```text
1. FDA-approved biologic commercialization bridge → slower Stage2 possible after source repair
2. biosimilar approval headline chase without near-term sales bridge → false Stage2 / local 4B
3. prescription/export partner commercialization ramp → Stage2 possible, later local 4B if bridge fades
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R7L73-C23-068270-CELLTRION-ZYMFENTRA-COMMERCIALIZATION-BRIDGE", "symbol": "068270", "company_name": "셀트리온", "round": "R7", "loop": "73", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIO_DRUG_APPROVAL_COMMERCIALIZATION_BRIDGE_VS_APPROVAL_HEADLINE_CHASE", "case_type": "bio_regulatory_approval_commercialization", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-BiologicCommercializationBridge", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C23 should reward regulatory approval only when it becomes commercialization evidence: launch, reimbursement access, channel uptake, direct sales or margin bridge. Celltrion has a slower but cleaner large-cap commercialization path with controlled MAE.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy approval, reimbursement, partner order, prescription uptake, launch and revenue evidence must be attached before runtime promotion."}
{"row_type": "case", "case_id": "R7L73-C23-950210-PRESTIGE-BIOSIMILAR-APPROVAL-HEADLINE-CHASE", "symbol": "950210", "company_name": "프레스티지바이오파마", "round": "R7", "loop": "73", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIO_DRUG_APPROVAL_COMMERCIALIZATION_BRIDGE_VS_APPROVAL_HEADLINE_CHASE", "case_type": "bio_regulatory_approval_commercialization", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / ApprovalHeadlineChaseLocal4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C23 should not convert a late approval/regulatory headline chase into durable Stage2 unless reimbursement, launch timing, partner orders and sales bridge are visible. The stock showed same-day MFE but later MAE and drawdown widened.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy approval, reimbursement, partner order, prescription uptake, launch and revenue evidence must be attached before runtime promotion."}
{"row_type": "case", "case_id": "R7L73-C23-195940-HKINNO-KCAB-GLOBAL-COMMERCIALIZATION-RAMP", "symbol": "195940", "company_name": "HK이노엔", "round": "R7", "loop": "73", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIO_DRUG_APPROVAL_COMMERCIALIZATION_BRIDGE_VS_APPROVAL_HEADLINE_CHASE", "case_type": "bio_regulatory_approval_commercialization", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-DrugCommercializationRamp", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C23 should distinguish real prescription/export commercialization ramp from pure regulatory excitement. HK inno.N produced an attractive path, but later post-peak drawdown requires local 4B-watch if prescription/partner revenue evidence stops refreshing.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy approval, reimbursement, partner order, prescription uptake, launch and revenue evidence must be attached before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R7L73-C23-068270-CELLTRION-ZYMFENTRA-COMMERCIALIZATION-BRIDGE", "case_id": "R7L73-C23-068270-CELLTRION-ZYMFENTRA-COMMERCIALIZATION-BRIDGE", "symbol": "068270", "company_name": "셀트리온", "round": "R7", "loop": "73", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIO_DRUG_APPROVAL_COMMERCIALIZATION_BRIDGE_VS_APPROVAL_HEADLINE_CHASE", "loop_objective": "coverage_gap_fill|counterexample_mining|commercialization_bridge_test", "trigger_type": "Stage2-Actionable-BiologicCommercializationBridge", "trigger_date": "2024-04-26", "entry_date": "2024-04-29", "entry_price": 178500.0, "evidence_available_at_that_date": "FDA_APPROVED_BIOLOGIC_US_COMMERCIALIZATION_REIMBURSEMENT_RAMP_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:CELLTRION_ZYMFENTRA_US_LAUNCH_REIMBURSEMENT_COMMERCIALIZATION_BRIDGE_2024", "stage2_evidence_fields": ["regulatory_approval", "commercialization_bridge_candidate", "partner_or_reimbursement_candidate"], "stage3_evidence_fields": ["relative_strength", "sales_or_prescription_ramp_candidate"], "stage4b_evidence_fields": ["later_local_4b_after_commercialization_peak_if_bridge_stale"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/068/068270/2024.csv", "profile_path": "atlas/symbol_profiles/068/068270.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 10.36, "MFE_90D_pct": 18.21, "MFE_180D_pct": 18.21, "MAE_30D_pct": -1.34, "MAE_90D_pct": -3.08, "MAE_180D_pct": -7.17, "peak_date": "2024-07-30", "peak_price": 211000.0, "drawdown_after_peak_pct": -21.47, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_approval_or_commercialization_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_commercial_failure_or_safety_regulatory_break", "trigger_outcome_label": "positive_slow_with_controlled_mae", "current_profile_verdict": "C23 should reward regulatory approval only when it becomes commercialization evidence: launch, reimbursement access, channel uptake, direct sales or margin bridge. Celltrion has a slower but cleaner large-cap commercialization path with controlled MAE.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C23_BIO_COMMERCIALIZATION_068270_2024-04-29", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R7L73-C23-950210-PRESTIGE-BIOSIMILAR-APPROVAL-HEADLINE-CHASE", "case_id": "R7L73-C23-950210-PRESTIGE-BIOSIMILAR-APPROVAL-HEADLINE-CHASE", "symbol": "950210", "company_name": "프레스티지바이오파마", "round": "R7", "loop": "73", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIO_DRUG_APPROVAL_COMMERCIALIZATION_BRIDGE_VS_APPROVAL_HEADLINE_CHASE", "loop_objective": "coverage_gap_fill|counterexample_mining|commercialization_bridge_test", "trigger_type": "Stage2-FalsePositive / ApprovalHeadlineChaseLocal4B", "trigger_date": "2024-10-25", "entry_date": "2024-10-28", "entry_price": 18150.0, "evidence_available_at_that_date": "BIOSIMILAR_REGULATORY_APPROVAL_HEADLINE_WITH_WEAK_NEAR_TERM_COMMERCIALIZATION_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:PRESTIGE_BIOPHARMA_BIOSIMILAR_APPROVAL_COMMERCIALIZATION_PARTNER_ORDER_BRIDGE_2024", "stage2_evidence_fields": ["regulatory_approval", "commercialization_bridge_candidate", "partner_or_reimbursement_candidate"], "stage3_evidence_fields": ["relative_strength", "sales_or_prescription_ramp_candidate"], "stage4b_evidence_fields": ["commercialization_bridge_stale_or_absent", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/950/950210/2024.csv", "profile_path": "atlas/symbol_profiles/950/950210.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 15.15, "MFE_90D_pct": 15.15, "MFE_180D_pct": 15.15, "MAE_30D_pct": -27.6, "MAE_90D_pct": -27.6, "MAE_180D_pct": -27.6, "peak_date": "2024-10-28", "peak_price": 20900.0, "drawdown_after_peak_pct": -37.13, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_approval_or_commercialization_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_commercial_failure_or_safety_regulatory_break", "trigger_outcome_label": "counterexample", "current_profile_verdict": "C23 should not convert a late approval/regulatory headline chase into durable Stage2 unless reimbursement, launch timing, partner orders and sales bridge are visible. The stock showed same-day MFE but later MAE and drawdown widened.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C23_BIO_COMMERCIALIZATION_950210_2024-10-28", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R7L73-C23-195940-HKINNO-KCAB-GLOBAL-COMMERCIALIZATION-RAMP", "case_id": "R7L73-C23-195940-HKINNO-KCAB-GLOBAL-COMMERCIALIZATION-RAMP", "symbol": "195940", "company_name": "HK이노엔", "round": "R7", "loop": "73", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIO_DRUG_APPROVAL_COMMERCIALIZATION_BRIDGE_VS_APPROVAL_HEADLINE_CHASE", "loop_objective": "coverage_gap_fill|counterexample_mining|commercialization_bridge_test", "trigger_type": "Stage2-Actionable-DrugCommercializationRamp", "trigger_date": "2024-06-14", "entry_date": "2024-06-17", "entry_price": 36100.0, "evidence_available_at_that_date": "K_CAP_PRESCRIPTION_EXPORT_PARTNER_COMMERCIALIZATION_REVENUE_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:HK_INNO_N_KCAB_GLOBAL_COMMERCIALIZATION_PARTNER_PRESCRIPTION_REVENUE_BRIDGE_2024", "stage2_evidence_fields": ["regulatory_approval", "commercialization_bridge_candidate", "partner_or_reimbursement_candidate"], "stage3_evidence_fields": ["relative_strength", "sales_or_prescription_ramp_candidate"], "stage4b_evidence_fields": ["later_local_4b_after_commercialization_peak_if_bridge_stale"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/195/195940/2024.csv", "profile_path": "atlas/symbol_profiles/195/195940.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 18.7, "MFE_90D_pct": 44.04, "MFE_180D_pct": 44.04, "MAE_30D_pct": -4.29, "MAE_90D_pct": -4.57, "MAE_180D_pct": -4.57, "peak_date": "2024-10-07", "peak_price": 52000.0, "drawdown_after_peak_pct": -31.06, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_approval_or_commercialization_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_commercial_failure_or_safety_regulatory_break", "trigger_outcome_label": "positive_with_later_4b_watch", "current_profile_verdict": "C23 should distinguish real prescription/export commercialization ramp from pure regulatory excitement. HK inno.N produced an attractive path, but later post-peak drawdown requires local 4B-watch if prescription/partner revenue evidence stops refreshing.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C23_BIO_COMMERCIALIZATION_195940_2024-06-17", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L73-C23-068270-CELLTRION-ZYMFENTRA-COMMERCIALIZATION-BRIDGE", "trigger_id": "TRG_R7L73-C23-068270-CELLTRION-ZYMFENTRA-COMMERCIALIZATION-BRIDGE", "symbol": "068270", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_scores_before": {"regulatory_approval_score": 15, "commercialization_bridge_score": 13, "reimbursement_or_partner_score": 10, "sales_ramp_score": 8, "relative_strength_score": 11, "margin_bridge_score": 7, "execution_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage2-Actionable after source repair", "raw_component_scores_after": {"regulatory_approval_score": 14, "commercialization_bridge_score": 15, "reimbursement_or_partner_score": 12, "sales_ramp_score": 10, "relative_strength_score": 11, "margin_bridge_score": 8, "execution_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 88, "stage_label_after": "Stage3-Yellow/Green candidate after source repair", "changed_components": ["commercialization_bridge_score", "reimbursement_or_partner_score", "sales_ramp_score", "execution_risk_score"], "component_delta_explanation": "Reward approval only when reimbursement, partner order, prescription uptake, launch or sales ramp bridge is verified; cap headline chase without commercialization bridge.", "MFE_90D_pct": 18.21, "MAE_90D_pct": -3.08, "score_return_alignment_label": "aligned_positive_or_lifecycle_positive", "current_profile_verdict": "C23 should reward regulatory approval only when it becomes commercialization evidence: launch, reimbursement access, channel uptake, direct sales or margin bridge. Celltrion has a slower but cleaner large-cap commercialization path with controlled MAE."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L73-C23-950210-PRESTIGE-BIOSIMILAR-APPROVAL-HEADLINE-CHASE", "trigger_id": "TRG_R7L73-C23-950210-PRESTIGE-BIOSIMILAR-APPROVAL-HEADLINE-CHASE", "symbol": "950210", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_scores_before": {"regulatory_approval_score": 12, "commercialization_bridge_score": 3, "reimbursement_or_partner_score": 2, "sales_ramp_score": 2, "relative_strength_score": 8, "margin_bridge_score": 2, "execution_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 58, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"regulatory_approval_score": 8, "commercialization_bridge_score": 1, "reimbursement_or_partner_score": 1, "sales_ramp_score": 1, "relative_strength_score": 5, "margin_bridge_score": 1, "execution_risk_score": 18, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 44, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["commercialization_bridge_score", "reimbursement_or_partner_score", "sales_ramp_score", "execution_risk_score"], "component_delta_explanation": "Reward approval only when reimbursement, partner order, prescription uptake, launch or sales ramp bridge is verified; cap headline chase without commercialization bridge.", "MFE_90D_pct": 15.15, "MAE_90D_pct": -27.6, "score_return_alignment_label": "approval_headline_false_positive_bridge_gap", "current_profile_verdict": "C23 should not convert a late approval/regulatory headline chase into durable Stage2 unless reimbursement, launch timing, partner orders and sales bridge are visible. The stock showed same-day MFE but later MAE and drawdown widened."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L73-C23-195940-HKINNO-KCAB-GLOBAL-COMMERCIALIZATION-RAMP", "trigger_id": "TRG_R7L73-C23-195940-HKINNO-KCAB-GLOBAL-COMMERCIALIZATION-RAMP", "symbol": "195940", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_scores_before": {"regulatory_approval_score": 15, "commercialization_bridge_score": 13, "reimbursement_or_partner_score": 10, "sales_ramp_score": 8, "relative_strength_score": 11, "margin_bridge_score": 7, "execution_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage2-Actionable after source repair", "raw_component_scores_after": {"regulatory_approval_score": 14, "commercialization_bridge_score": 15, "reimbursement_or_partner_score": 12, "sales_ramp_score": 10, "relative_strength_score": 11, "margin_bridge_score": 8, "execution_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 88, "stage_label_after": "Stage3-Yellow/Green candidate after source repair", "changed_components": ["commercialization_bridge_score", "reimbursement_or_partner_score", "sales_ramp_score", "execution_risk_score"], "component_delta_explanation": "Reward approval only when reimbursement, partner order, prescription uptake, launch or sales ramp bridge is verified; cap headline chase without commercialization bridge.", "MFE_90D_pct": 44.04, "MAE_90D_pct": -4.57, "score_return_alignment_label": "aligned_positive_or_lifecycle_positive", "current_profile_verdict": "C23 should distinguish real prescription/export commercialization ramp from pure regulatory excitement. HK inno.N produced an attractive path, but later post-peak drawdown requires local 4B-watch if prescription/partner revenue evidence stops refreshing."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R7", "loop": 73, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIO_DRUG_APPROVAL_COMMERCIALIZATION_BRIDGE_VS_APPROVAL_HEADLINE_CHASE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 2, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "current_profile_error_count": 1, "diversity_score_summary": "+3 underused C23 symbols, +3 approval/commercialization trigger families, +2 commercialization positives, +1 approval-headline chase counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R7", "loop": 73, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "axis": "bio_drug_approval_commercialization_bridge_vs_approval_headline_chase", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C23 should split verified regulatory-commercialization bridge from approval headline chase. Stage2 requires launch, reimbursement, partner order, prescription uptake, sales ramp or margin conversion evidence. If MFE is followed by stale commercialization evidence and post-peak drawdown, route to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["068270", "950210", "195940"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R7", "loop": 73, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C23 needs commercialization proof. 셀트리온 and HK이노엔 show slower commercialization positives; 프레스티지바이오파마 shows an approval-headline chase that should be capped without near-term reimbursement/launch/order bridge."}
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
068270:
  corporate_action_candidate_dates = 2006-10-13, 2008-06-10, 2008-09-24, 2012-06-29, 2013-03-22, 2024-01-12
  selected window = 2024-04-29~D+180
  contamination = false because the selected entry is after the 2024-01-12 candidate window

950210:
  corporate_action_candidate_dates = none
  selected window = 2024-10-28~D+180
  contamination = false

195940:
  corporate_action_candidate_dates = none
  selected window = 2024-06-17~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C23 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C23 rule-shape discovery,
but coding-agent promotion requires non-proxy approval, reimbursement, launch, partner order, prescription uptake, sales ramp and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R7/C23 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair.

Candidate axis:
bio_drug_approval_commercialization_bridge_vs_approval_headline_chase

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 068270, 950210 and 195940.
4. Keep generic C23 approval weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - regulatory approval is explicit,
   - reimbursement, launch, prescription uptake, partner order or sales ramp is visible,
   - commercialization bridge connects to revenue or margin,
   - MAE remains controlled.
6. Consider local 4B-watch when:
   - the trigger is approval/regulatory headline only,
   - commercialization evidence is stale or absent,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
7. Do not convert local 4B-watch into full 4B/4C without non-price safety, regulatory, clinical, or commercial failure evidence.
8. Emit before/after diagnostics and reject if verified commercialization positives are overblocked.
```

---

## Final round state

```text
completed_round = R7
completed_loop = 73
next_round = R8
next_loop = 73
round_schedule_status = valid
round_sector_consistency = pass
```

