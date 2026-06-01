# E2R Stock-Web v12 Residual Research — R12 Loop 77 / L10 / C31

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R12",
  "scheduled_loop": 77,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R12",
  "completed_loop": 77,
  "computed_next_round": "R13",
  "computed_next_loop": 77,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "fine_archetype_id": "LOW_BIRTH_CHILDCARE_POLICY_DIRECT_DEMAND_BRIDGE_VS_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "policy_event_bridge_guardrail",
    "4B_non_price_requirement_stress_test",
    "low_birth_childcare_policy_direct_demand_mapping",
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

Previous completed state in this interactive run: R11 / loop 77.

Therefore:

```text
scheduled_round = R12
scheduled_loop = 77
allowed_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC or relevant under-covered service/agri sector
selected_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
selected_canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
computed_next_round = R13
computed_next_loop = 77
```

R12 was routed to C31 because this is a low-birth / childcare policy event bridge guardrail, not a normal consumer operating-leverage round.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C31 concentration in:

```text
112610, 034020, 336260, UNKNOWN_SYMBOL, 036460
```

This run uses three different symbols:

```text
013990 / 아가방컴퍼니 / low-birth childcare policy lifecycle candidate
159580 / 제로투세븐 / low-birth policy theme fade
407400 / 꿈비 / baby-product policy theme fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
No selected row has a profile-level 2024 corporate-action candidate inside the selected window.
```

## Research thesis

C31 is not “정책 테마가 올랐다.”

For low-birth / childcare policy rows, the bridge must pass through:

```text
policy / subsidy / demographic announcement
→ direct beneficiary mapping
→ channel demand, sell-through or reorder
→ inventory and margin bridge
→ durable rerating
```

정책 headline은 확성기다.  
C31은 그 소리가 실제 매장 수요, 재주문, 재고 회전, 마진으로 돌아오는지를 본다.

---

## Case 1 — Policy lifecycle candidate: 013990 / 아가방컴퍼니

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is direct childcare-product demand, channel sell-through, reorder, inventory and margin bridge evidence.

```text
evidence_family = LOW_BIRTH_POLICY_CHILDCARE_SUBSIDY_DIRECT_DEMAND_RETAIL_SELLTHROUGH_MARGIN_BRIDGE_CANDIDATE
case_role = policy_lifecycle_positive_with_later_4b_watch
trigger_date = 2024-01-02
entry_date = 2024-01-03
entry_price = 4,200
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/013/013990/2024.csv`:

```text
2024-01-03,4200,5630,4130,5630
2024-01-18,7040,7180,6000,6140
2024-05-30,5440,5900,5430,5510
2024-06-20,6230,6380,5410,5430
2024-08-05,3990,4065,3400,3455
```

### Backtest

```text
MFE_30D  = +70.95%
MAE_30D  = -1.67%
MFE_90D  = +70.95%
MAE_90D  = -1.67%
MFE_180D = +70.95%
MAE_180D = -19.05%
peak_180 = 7,180 on 2024-01-18
trough_180 = 3,400 on 2024-08-05
peak_to_later_drawdown = -52.65%
```

### Interpretation

This is the low-birth policy lifecycle winner.  
The policy shock created real tradable MFE, but it cannot remain permanent Green without direct-demand and margin evidence.

Correct treatment:

```text
source repair first
possible policy lifecycle Stage2-Yellow
later local 4B if direct-demand / reorder / margin bridge fades
```

---

## Case 2 — Counterexample / local 4B: 159580 / 제로투세븐

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests low-birth / childcare consumer policy beta without enough direct reorder and margin bridge.

```text
evidence_family = LOW_BIRTH_POLICY_CHILDCARE_CONSUMER_THEME_WITH_WEAK_DIRECT_REORDER_MARGIN_BRIDGE
case_role = counterexample_low_birth_policy_beta_local4b
trigger_date = 2024-01-02
entry_date = 2024-01-03
entry_price = 6,730
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/159/159580/2024.csv`:

```text
2024-01-03,6730,8440,6650,8020
2024-01-18,7570,8590,7020,7320
2024-04-09,5420,5540,5420,5450
2024-08-05,4625,4760,3820,4035
2024-09-09,3820,4015,3805,4015
```

### Backtest

```text
MFE_30D  = +27.64%
MAE_30D  = -3.71%
MFE_90D  = +27.64%
MAE_90D  = -19.47%
MFE_180D = +27.64%
MAE_180D = -43.46%
peak_180 = 8,590 on 2024-01-18
trough_180 = 3,805 on 2024-09-09
peak_to_later_drawdown = -55.70%
```

### Interpretation

This is a policy-theme false positive.  
The first move was tradable, but the later MAE and drawdown say the low-birth policy bridge did not become durable.

Correct treatment:

```text
childcare / low-birth policy beta
→ no verified sell-through / reorder / margin bridge
→ local 4B-watch
```

---

## Case 3 — Counterexample / local 4B: 407400 / 꿈비

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests baby-product / low-birth policy theme beta without enough direct demand and margin evidence.

```text
evidence_family = LOW_BIRTH_POLICY_BABY_PRODUCT_THEME_WITH_WEAK_DIRECT_DEMAND_MARGIN_BRIDGE
case_role = counterexample_babyproduct_policy_theme_local4b
trigger_date = 2024-01-02
entry_date = 2024-01-03
entry_price = 12,390
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/407/407400/2024.csv`:

```text
2024-01-03,12390,14700,12230,13410
2024-01-31,10160,10470,10050,10110
2024-03-20,9290,10960,9290,10150
2024-08-05,7340,7490,5880,6070
2024-08-29,8200,8900,7110,7130
```

### Backtest

```text
MFE_30D  = +18.64%
MAE_30D  = -18.89%
MFE_90D  = +18.64%
MAE_90D  = -35.92%
MFE_180D = +18.64%
MAE_180D = -52.54%
peak_180 = 14,700 on 2024-01-03
trough_180 = 5,880 on 2024-08-05
peak_to_later_drawdown = -60.00%
```

### Interpretation

This is the harshest low-birth theme fade.  
The policy headline did not become a durable direct-demand bridge.

Correct treatment:

```text
baby-product / low-birth policy beta
→ no direct demand / reorder / margin bridge
→ local 4B-watch
```

---

## Cross-case residual finding

### What this strengthens

```text
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
stage2_required_bridge = strengthen
full_4b_requires_non_price_evidence = keep
```

### What this does not justify

```text
do_not_raise_generic_C31_low_birth_policy_weight = true
do_not_treat_low_birth_policy_headline_as_Green_without_direct_demand_bridge = true
do_not_convert_policy_theme_drawdown_to_hard_4C_without_non_price_policy_reversal_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
LOW_BIRTH_CHILDCARE_POLICY_DIRECT_DEMAND_BRIDGE_VS_THEME_FADE
```

This fine archetype covers:

```text
1. childcare policy MFE with possible direct-demand bridge → policy lifecycle candidate after source repair
2. childcare consumer policy beta without reorder/margin bridge → false Stage2 / local 4B
3. baby-product policy beta without direct-demand bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R12L77-C31-013990-AGABANG-LOW-BIRTH-CHILDCARE-POLICY-LIFECYCLE", "symbol": "013990", "company_name": "아가방컴퍼니", "round": "R12", "loop": "77", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "LOW_BIRTH_CHILDCARE_POLICY_DIRECT_DEMAND_BRIDGE_VS_THEME_FADE", "case_type": "policy_subsidy_legislation_event_low_birth_childcare", "positive_or_counterexample": "policy_lifecycle_positive", "best_trigger": "Stage2-PolicyLifecycle-LowBirthChildcareDirectDemandBridgeWithLocal4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C31 can allow a policy-event lifecycle candidate when low-birth or childcare policy maps to direct beneficiary demand, sell-through, inventory normalization and margin bridge. Agabang produced a large MFE, but later drawdown means it cannot remain Green unless direct-demand and margin evidence refreshes.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy policy support, direct beneficiary mapping, channel sell-through, reorder, inventory and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R12L77-C31-159580-ZEROTOSEVEN-LOW-BIRTH-POLICY-THEME-FADE", "symbol": "159580", "company_name": "제로투세븐", "round": "R12", "loop": "77", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "LOW_BIRTH_CHILDCARE_POLICY_DIRECT_DEMAND_BRIDGE_VS_THEME_FADE", "case_type": "policy_subsidy_legislation_event_low_birth_childcare", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / LowBirthChildcarePolicyThemeFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C31 should not treat childcare/low-birth policy beta as durable Stage2 unless direct demand, channel reorder, sell-through and margin evidence refreshes. Zero to Seven had a tradable MFE, but then high MAE and post-peak fade, making it local 4B rather than Green.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy policy support, direct beneficiary mapping, channel sell-through, reorder, inventory and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R12L77-C31-407400-GGUMBI-LOW-BIRTH-BABYPRODUCT-THEME-FADE", "symbol": "407400", "company_name": "꿈비", "round": "R12", "loop": "77", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "LOW_BIRTH_CHILDCARE_POLICY_DIRECT_DEMAND_BRIDGE_VS_THEME_FADE", "case_type": "policy_subsidy_legislation_event_low_birth_childcare", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / BabyProductLowBirthPolicyThemeFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C31 should not treat baby-product / low-birth policy theme spikes as durable Stage2 unless policy support maps to direct demand, channel sell-through, replenishment and margin bridge. Ggumbi produced an early MFE and then a severe drawdown path.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy policy support, direct beneficiary mapping, channel sell-through, reorder, inventory and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R12L77-C31-013990-AGABANG-LOW-BIRTH-CHILDCARE-POLICY-LIFECYCLE", "case_id": "R12L77-C31-013990-AGABANG-LOW-BIRTH-CHILDCARE-POLICY-LIFECYCLE", "symbol": "013990", "company_name": "아가방컴퍼니", "round": "R12", "loop": "77", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "LOW_BIRTH_CHILDCARE_POLICY_DIRECT_DEMAND_BRIDGE_VS_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|policy_event_bridge_guardrail", "trigger_type": "Stage2-PolicyLifecycle-LowBirthChildcareDirectDemandBridgeWithLocal4B", "trigger_date": "2024-01-02", "entry_date": "2024-01-03", "entry_price": 4200.0, "evidence_available_at_that_date": "LOW_BIRTH_POLICY_CHILDCARE_SUBSIDY_DIRECT_DEMAND_RETAIL_SELLTHROUGH_MARGIN_BRIDGE_CANDIDATE", "evidence_source": "source_proxy_manual_verification_required:AGABANG_2024_LOW_BIRTH_CHILDCARE_POLICY_DIRECT_DEMAND_SELLTHROUGH_MARGIN_BRIDGE", "stage2_evidence_fields": ["policy_event", "direct_beneficiary_mapping_candidate", "sellthrough_reorder_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "inventory_or_channel_productivity_candidate"], "stage4b_evidence_fields": ["policy_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/013/013990/2024.csv", "profile_path": "atlas/symbol_profiles/013/013990.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 70.95, "MFE_90D_pct": 70.95, "MFE_180D_pct": 70.95, "MAE_30D_pct": -1.67, "MAE_90D_pct": -1.67, "MAE_180D_pct": -19.05, "peak_date": "2024-01-18", "peak_price": 7180.0, "drawdown_after_peak_pct": -52.65, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_low_birth_policy_peak_if_direct_demand_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_policy_reversal_channel_loss_inventory_margin_or_financing_break", "trigger_outcome_label": "policy_lifecycle_positive_with_later_4b_watch", "current_profile_verdict": "C31 can allow a policy-event lifecycle candidate when low-birth or childcare policy maps to direct beneficiary demand, sell-through, inventory normalization and margin bridge. Agabang produced a large MFE, but later drawdown means it cannot remain Green unless direct-demand and margin evidence refreshes.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C31_LOWBIRTH_POLICY_013990_2024-01-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R12L77-C31-159580-ZEROTOSEVEN-LOW-BIRTH-POLICY-THEME-FADE", "case_id": "R12L77-C31-159580-ZEROTOSEVEN-LOW-BIRTH-POLICY-THEME-FADE", "symbol": "159580", "company_name": "제로투세븐", "round": "R12", "loop": "77", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "LOW_BIRTH_CHILDCARE_POLICY_DIRECT_DEMAND_BRIDGE_VS_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|policy_event_bridge_guardrail", "trigger_type": "Stage2-FalsePositive / LowBirthChildcarePolicyThemeFade", "trigger_date": "2024-01-02", "entry_date": "2024-01-03", "entry_price": 6730.0, "evidence_available_at_that_date": "LOW_BIRTH_POLICY_CHILDCARE_CONSUMER_THEME_WITH_WEAK_DIRECT_REORDER_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:ZEROTOSEVEN_2024_LOW_BIRTH_POLICY_CHILDCARE_DIRECT_REORDER_SELLTHROUGH_MARGIN_BRIDGE", "stage2_evidence_fields": ["policy_event", "direct_beneficiary_mapping_candidate", "sellthrough_reorder_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "inventory_or_channel_productivity_candidate"], "stage4b_evidence_fields": ["policy_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/159/159580/2024.csv", "profile_path": "atlas/symbol_profiles/159/159580.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 27.64, "MFE_90D_pct": 27.64, "MFE_180D_pct": 27.64, "MAE_30D_pct": -3.71, "MAE_90D_pct": -19.47, "MAE_180D_pct": -43.46, "peak_date": "2024-01-18", "peak_price": 8590.0, "drawdown_after_peak_pct": -55.7, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_low_birth_policy_peak_if_direct_demand_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_policy_reversal_channel_loss_inventory_margin_or_financing_break", "trigger_outcome_label": "counterexample_low_birth_policy_beta_local4b", "current_profile_verdict": "C31 should not treat childcare/low-birth policy beta as durable Stage2 unless direct demand, channel reorder, sell-through and margin evidence refreshes. Zero to Seven had a tradable MFE, but then high MAE and post-peak fade, making it local 4B rather than Green.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C31_LOWBIRTH_POLICY_159580_2024-01-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R12L77-C31-407400-GGUMBI-LOW-BIRTH-BABYPRODUCT-THEME-FADE", "case_id": "R12L77-C31-407400-GGUMBI-LOW-BIRTH-BABYPRODUCT-THEME-FADE", "symbol": "407400", "company_name": "꿈비", "round": "R12", "loop": "77", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "LOW_BIRTH_CHILDCARE_POLICY_DIRECT_DEMAND_BRIDGE_VS_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|policy_event_bridge_guardrail", "trigger_type": "Stage2-FalsePositive / BabyProductLowBirthPolicyThemeFade", "trigger_date": "2024-01-02", "entry_date": "2024-01-03", "entry_price": 12390.0, "evidence_available_at_that_date": "LOW_BIRTH_POLICY_BABY_PRODUCT_THEME_WITH_WEAK_DIRECT_DEMAND_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:GGUMBI_2024_LOW_BIRTH_POLICY_BABY_PRODUCT_DEMAND_REORDER_MARGIN_BRIDGE", "stage2_evidence_fields": ["policy_event", "direct_beneficiary_mapping_candidate", "sellthrough_reorder_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "inventory_or_channel_productivity_candidate"], "stage4b_evidence_fields": ["policy_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/407/407400/2024.csv", "profile_path": "atlas/symbol_profiles/407/407400.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 18.64, "MFE_90D_pct": 18.64, "MFE_180D_pct": 18.64, "MAE_30D_pct": -18.89, "MAE_90D_pct": -35.92, "MAE_180D_pct": -52.54, "peak_date": "2024-01-03", "peak_price": 14700.0, "drawdown_after_peak_pct": -60.0, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_low_birth_policy_peak_if_direct_demand_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_policy_reversal_channel_loss_inventory_margin_or_financing_break", "trigger_outcome_label": "counterexample_babyproduct_policy_theme_local4b", "current_profile_verdict": "C31 should not treat baby-product / low-birth policy theme spikes as durable Stage2 unless policy support maps to direct demand, channel sell-through, replenishment and margin bridge. Ggumbi produced an early MFE and then a severe drawdown path.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C31_LOWBIRTH_POLICY_407400_2024-01-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L77-C31-013990-AGABANG-LOW-BIRTH-CHILDCARE-POLICY-LIFECYCLE", "trigger_id": "TRG_R12L77-C31-013990-AGABANG-LOW-BIRTH-CHILDCARE-POLICY-LIFECYCLE", "symbol": "013990", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"policy_or_regulatory_score": 14, "direct_beneficiary_mapping_score": 12, "direct_demand_score": 10, "sellthrough_reorder_score": 9, "margin_bridge_score": 8, "relative_strength_score": 14, "execution_risk_score": 12, "source_confidence_score": 2}, "weighted_score_before": 68, "stage_label_before": "Policy lifecycle candidate after source repair", "raw_component_scores_after": {"policy_or_regulatory_score": 8, "direct_beneficiary_mapping_score": 15, "direct_demand_score": 13, "sellthrough_reorder_score": 12, "margin_bridge_score": 11, "relative_strength_score": 12, "execution_risk_score": 13, "source_confidence_score": 2}, "weighted_score_after": 74, "stage_label_after": "Policy lifecycle Stage2-Yellow after source repair + local 4B", "changed_components": ["policy_or_regulatory_score", "direct_beneficiary_mapping_score", "direct_demand_score", "sellthrough_reorder_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Cap policy-event scores unless low-birth/childcare policy maps to direct beneficiary economics, sell-through, replenishment and margin bridge.", "MFE_90D_pct": 70.95, "MAE_90D_pct": -1.67, "score_return_alignment_label": "policy_lifecycle_with_later_4b", "current_profile_verdict": "C31 can allow a policy-event lifecycle candidate when low-birth or childcare policy maps to direct beneficiary demand, sell-through, inventory normalization and margin bridge. Agabang produced a large MFE, but later drawdown means it cannot remain Green unless direct-demand and margin evidence refreshes."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L77-C31-159580-ZEROTOSEVEN-LOW-BIRTH-POLICY-THEME-FADE", "trigger_id": "TRG_R12L77-C31-159580-ZEROTOSEVEN-LOW-BIRTH-POLICY-THEME-FADE", "symbol": "159580", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"policy_or_regulatory_score": 14, "direct_beneficiary_mapping_score": 4, "direct_demand_score": 2, "sellthrough_reorder_score": 2, "margin_bridge_score": 1, "relative_strength_score": 7, "execution_risk_score": 21, "source_confidence_score": 2}, "weighted_score_before": 48, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"policy_or_regulatory_score": 8, "direct_beneficiary_mapping_score": 2, "direct_demand_score": 1, "sellthrough_reorder_score": 1, "margin_bridge_score": 1, "relative_strength_score": 4, "execution_risk_score": 23, "source_confidence_score": 2}, "weighted_score_after": 35, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["policy_or_regulatory_score", "direct_beneficiary_mapping_score", "direct_demand_score", "sellthrough_reorder_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Cap policy-event scores unless low-birth/childcare policy maps to direct beneficiary economics, sell-through, replenishment and margin bridge.", "MFE_90D_pct": 27.64, "MAE_90D_pct": -19.47, "score_return_alignment_label": "policy_theme_false_positive_bridge_gap", "current_profile_verdict": "C31 should not treat childcare/low-birth policy beta as durable Stage2 unless direct demand, channel reorder, sell-through and margin evidence refreshes. Zero to Seven had a tradable MFE, but then high MAE and post-peak fade, making it local 4B rather than Green."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L77-C31-407400-GGUMBI-LOW-BIRTH-BABYPRODUCT-THEME-FADE", "trigger_id": "TRG_R12L77-C31-407400-GGUMBI-LOW-BIRTH-BABYPRODUCT-THEME-FADE", "symbol": "407400", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"policy_or_regulatory_score": 14, "direct_beneficiary_mapping_score": 4, "direct_demand_score": 2, "sellthrough_reorder_score": 2, "margin_bridge_score": 1, "relative_strength_score": 7, "execution_risk_score": 21, "source_confidence_score": 2}, "weighted_score_before": 48, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"policy_or_regulatory_score": 8, "direct_beneficiary_mapping_score": 2, "direct_demand_score": 1, "sellthrough_reorder_score": 1, "margin_bridge_score": 1, "relative_strength_score": 4, "execution_risk_score": 23, "source_confidence_score": 2}, "weighted_score_after": 35, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["policy_or_regulatory_score", "direct_beneficiary_mapping_score", "direct_demand_score", "sellthrough_reorder_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Cap policy-event scores unless low-birth/childcare policy maps to direct beneficiary economics, sell-through, replenishment and margin bridge.", "MFE_90D_pct": 18.64, "MAE_90D_pct": -35.92, "score_return_alignment_label": "policy_theme_false_positive_bridge_gap", "current_profile_verdict": "C31 should not treat baby-product / low-birth policy theme spikes as durable Stage2 unless policy support maps to direct demand, channel sell-through, replenishment and margin bridge. Ggumbi produced an early MFE and then a severe drawdown path."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R12", "loop": 77, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "LOW_BIRTH_CHILDCARE_POLICY_DIRECT_DEMAND_BRIDGE_VS_THEME_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 1, "positive_case_count": 1, "counterexample_count": 2, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "current_profile_error_count": 2, "diversity_score_summary": "+3 underused C31 low-birth/childcare symbols outside top-covered resource/power/value-up policy set, +1 low-birth policy trigger family, +1 direct-demand lifecycle MFE candidate, +2 policy-theme local-4B counterexamples, no hard duplicate", "residual_contribution_label": "policy_event_bridge_guardrail_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R12", "loop": 77, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "axis": "low_birth_childcare_policy_direct_demand_bridge_vs_theme_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C31 should split low-birth/childcare policy direct-demand lifecycle trades from generic policy theme beta. Stage2 requires explicit policy event plus direct beneficiary mapping, demand/sell-through, channel reorder, inventory normalization and margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["013990", "159580", "407400"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R12", "loop": 77, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "existing_axis_strengthened": ["price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "stage2_required_bridge", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C31 low-birth/childcare policy events need direct-demand proof. Agabang shows a policy lifecycle MFE candidate after source repair; Zero to Seven and Ggumbi show policy theme beta fading into local 4B when direct sell-through, reorder and margin bridge are absent."}
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
013990:
  name = 아가방컴퍼니 from 2007-04-23
  corporate_action_candidate_dates = 2008-05-16
  selected window = 2024-01-03~D+180
  contamination = false

159580:
  name = 제로투세븐
  corporate_action_candidate_dates = 2018-11-13
  selected window = 2024-01-03~D+180
  contamination = false

407400:
  name = 꿈비
  corporate_action_candidate_dates = 2023-07-19
  selected window = 2024-01-03~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C31 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C31 rule-shape discovery,
but coding-agent promotion requires non-proxy low-birth/childcare policy evidence, direct beneficiary mapping, sell-through, reorder, inventory and margin bridge evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R12/C31 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair.

Candidate axis:
low_birth_childcare_policy_direct_demand_bridge_vs_theme_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 013990, 159580 and 407400.
4. Keep generic C31 policy-event weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - policy/subsidy event is explicit,
   - direct beneficiary mapping is visible,
   - direct demand, sell-through or reorder evidence exists,
   - inventory and margin bridge is credible,
   - MAE remains controlled or the signal is lifecycle-managed.
6. Consider local 4B-watch when:
   - the trigger is low-birth/childcare policy theme beta only,
   - direct-demand/sell-through/margin bridge is absent or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
7. Do not convert local 4B-watch into full 4B/4C without non-price policy reversal, channel loss, inventory issue, margin collapse, financing or liquidity evidence.
8. Emit before/after diagnostics and reject if verified direct-demand policy lifecycle positives are overblocked.
```

---

## Final round state

```text
completed_round = R12
completed_loop = 77
next_round = R13
next_loop = 77
round_schedule_status = valid
round_sector_consistency = pass
```

