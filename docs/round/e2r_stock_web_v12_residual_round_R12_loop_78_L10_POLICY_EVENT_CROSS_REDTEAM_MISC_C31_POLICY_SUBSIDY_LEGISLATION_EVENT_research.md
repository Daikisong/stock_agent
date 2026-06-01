# E2R Stock-Web v12 Residual Research — R12 Loop 78 / L10 / C31

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R12",
  "scheduled_loop": 78,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R12",
  "completed_loop": 78,
  "computed_next_round": "R13",
  "computed_next_loop": 78,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "fine_archetype_id": "TELEMEDICINE_DIGITAL_HEALTH_POLICY_DIRECT_DEMAND_BRIDGE_VS_POLICY_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "policy_event_bridge_guardrail",
    "4B_non_price_requirement_stress_test",
    "telemedicine_digital_health_policy_direct_beneficiary_mapping",
    "digital_health_policy_theme_fade_boundary",
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

Previous completed state in this interactive run: R11 / loop 78.

Therefore:

```text
scheduled_round = R12
scheduled_loop = 78
allowed_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC or relevant under-covered service/agri sector
selected_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
selected_canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
computed_next_round = R13
computed_next_loop = 78
```

R12 was routed to C31 because this is a telemedicine / digital-health policy event bridge guardrail, not a normal healthcare-device, platform, or consumer operating-leverage round.

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

This run uses three different symbols and avoids loop-77 low-birth names:

```text
032620 / 유비케어 / telemedicine policy EMR-platform direct-demand lifecycle candidate
032850 / 비트컴퓨터 / telemedicine healthcare-IT policy theme fade
263700 / 케어랩스 / digital-health platform policy theme fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
No selected row has a profile-level 2024 corporate-action candidate inside the selected window.
```

## Research thesis

C31 is not “정책 테마가 올랐다.”

For telemedicine / digital-health policy rows, the bridge must pass through:

```text
policy / regulation / temporary relaxation
→ direct beneficiary mapping
→ installed-base usage, transaction or claim/workflow demand
→ contract / paid conversion or revenue bridge
→ margin conversion
→ durable rerating
```

정책 headline은 문을 여는 손잡이다.  
C31이 보려는 것은 그 문을 지난 실제 사용량, 계약, 매출, 마진이 방 안으로 들어오는지다.

---

## Case 1 — Policy lifecycle candidate: 032620 / 유비케어

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is telemedicine/digital-health policy, EMR/clinic platform installed base, workflow demand, usage/revenue conversion and margin bridge evidence.

```text
evidence_family = TELEMEDICINE_POLICY_EMR_CLINIC_PLATFORM_DIRECT_DEMAND_USAGE_REVENUE_MARGIN_BRIDGE_CANDIDATE
case_role = policy_lifecycle_positive_with_later_4b_watch
trigger_date = 2024-01-30
entry_date = 2024-02-01
entry_price = 5,200
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/032/032620/2024.csv`:

```text
2024-02-01,5200,5980,4990,5000
2024-02-16,5170,6200,5170,6200
2024-02-19,6810,7370,6330,6570
2024-02-23,6130,7910,6050,7170
2024-03-19,5690,5700,5330,5450
2024-08-05,4200,4285,3460,3570
2024-11-01,3840,4950,3780,4540
```

### Backtest

```text
MFE_30D  = +52.12%
MAE_30D  = -11.25%
MFE_90D  = +52.12%
MAE_90D  = -11.25%
MFE_180D = +52.12%
MAE_180D = -33.46%
peak_180 = 7,910 on 2024-02-23
trough_180 = 3,460 on 2024-08-05
peak_to_later_drawdown = -56.26%
```

### Interpretation

This is the telemedicine policy lifecycle winner.  
The policy shock created real tradable MFE, but it cannot remain permanent Green without direct usage, revenue and margin evidence.

Correct treatment:

```text
source repair first
possible policy lifecycle Stage2-Yellow
later local 4B if direct usage / contract / revenue / margin bridge fades
```

---

## Case 2 — Counterexample / local 4B: 032850 / 비트컴퓨터

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests telemedicine / healthcare-IT policy beta without enough installed-base usage and revenue bridge.

```text
evidence_family = TELEMEDICINE_POLICY_HEALTHCARE_IT_THEME_WITH_WEAK_USAGE_REVENUE_MARGIN_BRIDGE
case_role = counterexample_telemedicine_IT_policy_beta_local4b
trigger_date = 2024-01-30
entry_date = 2024-02-01
entry_price = 8,040
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/032/032850/2024.csv`:

```text
2024-02-01,8040,9550,7910,8280
2024-02-19,9000,9290,8130,8450
2024-02-23,7800,9050,7720,8310
2024-03-19,6780,6810,6500,6580
2024-08-05,5410,5490,4605,4740
2024-10-25,4890,4950,4750,4770
```

### Backtest

```text
MFE_30D  = +18.78%
MAE_30D  = -16.79%
MFE_90D  = +18.78%
MAE_90D  = -27.24%
MFE_180D = +18.78%
MAE_180D = -42.72%
peak_180 = 9,550 on 2024-02-01
trough_180 = 4,605 on 2024-08-05
peak_to_later_drawdown = -51.78%
```

### Interpretation

This is a telemedicine-policy false positive.  
The first move was tradable, but the later MAE and drawdown say the policy bridge did not become durable.

Correct treatment:

```text
telemedicine / healthcare-IT policy beta
→ no verified usage / contract / revenue / margin bridge
→ local 4B-watch
```

---

## Case 3 — Counterexample / local 4B: 263700 / 케어랩스

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests digital-health platform / telemedicine policy beta without enough transaction, adoption and margin evidence.

```text
evidence_family = DIGITAL_HEALTH_PLATFORM_TELEMEDICINE_POLICY_THEME_WITH_WEAK_TRANSACTION_REVENUE_MARGIN_BRIDGE
case_role = counterexample_digital_health_platform_policy_beta_local4b
trigger_date = 2024-01-30
entry_date = 2024-02-01
entry_price = 4,310
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/263/263700/2024.csv`:

```text
2024-02-01,4310,5180,4310,4530
2024-02-16,4520,5730,4485,5730
2024-02-19,6870,7440,6480,7440
2024-02-20,7650,7800,6680,7030
2024-03-05,5780,6000,5210,5220
2024-08-05,3600,3600,2900,3035
2024-10-22,3025,3025,2890,2890
```

### Backtest

```text
MFE_30D  = +81.00%
MAE_30D  = -3.36%
MFE_90D  = +81.00%
MAE_90D  = -4.64%
MFE_180D = +81.00%
MAE_180D = -32.71%
peak_180 = 7,800 on 2024-02-20
trough_180 = 2,900 on 2024-08-05
peak_to_later_drawdown = -62.82%
```

### Interpretation

This is a high-MFE policy-theme fade.  
The price move was powerful, but without transaction/revenue/margin bridge it should not be treated as durable C31 Green.

Correct treatment:

```text
digital-health platform policy beta
→ no transaction / adoption / revenue / margin bridge
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
do_not_raise_generic_C31_telemedicine_policy_weight = true
do_not_treat_telemedicine_policy_headline_as_Green_without_direct_demand_bridge = true
do_not_convert_policy_theme_drawdown_to_hard_4C_without_non_price_policy_reversal_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
TELEMEDICINE_DIGITAL_HEALTH_POLICY_DIRECT_DEMAND_BRIDGE_VS_POLICY_THEME_FADE
```

This fine archetype covers:

```text
1. telemedicine policy MFE with possible EMR/clinic direct-demand bridge → policy lifecycle candidate after source repair
2. healthcare-IT policy beta without usage/revenue bridge → false Stage2 / local 4B
3. digital-health platform policy beta without transaction/margin bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R12L78-C31-032620-UBCARE-TELEMEDICINE-POLICY-DIRECT-DEMAND", "symbol": "032620", "company_name": "유비케어", "round": "R12", "loop": "78", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "TELEMEDICINE_DIGITAL_HEALTH_POLICY_DIRECT_DEMAND_BRIDGE_VS_POLICY_THEME_FADE", "case_type": "policy_subsidy_legislation_event_telemedicine_digital_health", "positive_or_counterexample": "policy_lifecycle_positive", "best_trigger": "Stage2-PolicyLifecycle-TelemedicineDigitalHealthDirectDemandBridgeWithLocal4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C31 can allow telemedicine/digital-health policy rows when policy relaxation maps to direct clinic/EMR platform usage, claim/workflow demand, paid usage, revenue conversion and margin bridge. UBCare produced a large MFE, but later drawdown means it cannot remain Green unless direct-demand and margin evidence refreshes.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy telemedicine/digital-health policy event, direct beneficiary mapping, usage/transaction volume, contract conversion, revenue and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R12L78-C31-032850-BITCOMPUTER-TELEMEDICINE-IT-POLICY-THEME-FADE", "symbol": "032850", "company_name": "비트컴퓨터", "round": "R12", "loop": "78", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "TELEMEDICINE_DIGITAL_HEALTH_POLICY_DIRECT_DEMAND_BRIDGE_VS_POLICY_THEME_FADE", "case_type": "policy_subsidy_legislation_event_telemedicine_digital_health", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / TelemedicineITPolicyThemeFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C31 should not treat telemedicine or healthcare-IT policy beta as durable Stage2 unless policy event maps to direct installed-base demand, contract conversion, usage/revenue and margin evidence. BitComputer had an immediate MFE spike and then a long drawdown, making it local 4B rather than Green.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy telemedicine/digital-health policy event, direct beneficiary mapping, usage/transaction volume, contract conversion, revenue and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R12L78-C31-263700-CARELabs-DIGITAL-HEALTH-PLATFORM-POLICY-FADE", "symbol": "263700", "company_name": "케어랩스", "round": "R12", "loop": "78", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "TELEMEDICINE_DIGITAL_HEALTH_POLICY_DIRECT_DEMAND_BRIDGE_VS_POLICY_THEME_FADE", "case_type": "policy_subsidy_legislation_event_telemedicine_digital_health", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / DigitalHealthPlatformPolicyThemeFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C31 should not treat digital-health platform policy beta as durable Stage2 unless policy maps to appointment/transaction volume, hospital/clinic adoption, revenue conversion and margin bridge. CareLabs produced a sharp MFE, but then a severe drawdown path, so the row is useful as local 4B boundary.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy telemedicine/digital-health policy event, direct beneficiary mapping, usage/transaction volume, contract conversion, revenue and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R12L78-C31-032620-UBCARE-TELEMEDICINE-POLICY-DIRECT-DEMAND", "case_id": "R12L78-C31-032620-UBCARE-TELEMEDICINE-POLICY-DIRECT-DEMAND", "symbol": "032620", "company_name": "유비케어", "round": "R12", "loop": "78", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "TELEMEDICINE_DIGITAL_HEALTH_POLICY_DIRECT_DEMAND_BRIDGE_VS_POLICY_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|policy_event_bridge_guardrail", "trigger_type": "Stage2-PolicyLifecycle-TelemedicineDigitalHealthDirectDemandBridgeWithLocal4B", "trigger_date": "2024-01-30", "entry_date": "2024-02-01", "entry_price": 5200.0, "evidence_available_at_that_date": "TELEMEDICINE_POLICY_EMR_CLINIC_PLATFORM_DIRECT_DEMAND_USAGE_REVENUE_MARGIN_BRIDGE_CANDIDATE", "evidence_source": "source_proxy_manual_verification_required:UBCARE_2024_TELEMEDICINE_POLICY_EMR_PLATFORM_USAGE_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["policy_event", "direct_beneficiary_mapping_candidate", "usage_transaction_revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "contract_conversion_or_installed_base_candidate"], "stage4b_evidence_fields": ["policy_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/032/032620/2024.csv", "profile_path": "atlas/symbol_profiles/032/032620.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 52.12, "MFE_90D_pct": 52.12, "MFE_180D_pct": 52.12, "MAE_30D_pct": -11.25, "MAE_90D_pct": -11.25, "MAE_180D_pct": -33.46, "peak_date": "2024-02-23", "peak_price": 7910.0, "drawdown_after_peak_pct": -56.26, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_telemedicine_policy_peak_if_usage_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_policy_reversal_contract_loss_usage_collapse_margin_or_financing_break", "trigger_outcome_label": "policy_lifecycle_positive_with_later_4b_watch", "current_profile_verdict": "C31 can allow telemedicine/digital-health policy rows when policy relaxation maps to direct clinic/EMR platform usage, claim/workflow demand, paid usage, revenue conversion and margin bridge. UBCare produced a large MFE, but later drawdown means it cannot remain Green unless direct-demand and margin evidence refreshes.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C31_TELEMEDICINE_POLICY_032620_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R12L78-C31-032850-BITCOMPUTER-TELEMEDICINE-IT-POLICY-THEME-FADE", "case_id": "R12L78-C31-032850-BITCOMPUTER-TELEMEDICINE-IT-POLICY-THEME-FADE", "symbol": "032850", "company_name": "비트컴퓨터", "round": "R12", "loop": "78", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "TELEMEDICINE_DIGITAL_HEALTH_POLICY_DIRECT_DEMAND_BRIDGE_VS_POLICY_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|policy_event_bridge_guardrail", "trigger_type": "Stage2-FalsePositive / TelemedicineITPolicyThemeFade", "trigger_date": "2024-01-30", "entry_date": "2024-02-01", "entry_price": 8040.0, "evidence_available_at_that_date": "TELEMEDICINE_POLICY_HEALTHCARE_IT_THEME_WITH_WEAK_USAGE_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:BITCOMPUTER_2024_TELEMEDICINE_POLICY_HEALTHCARE_IT_USAGE_CONTRACT_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["policy_event", "direct_beneficiary_mapping_candidate", "usage_transaction_revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "contract_conversion_or_installed_base_candidate"], "stage4b_evidence_fields": ["policy_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/032/032850/2024.csv", "profile_path": "atlas/symbol_profiles/032/032850.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 18.78, "MFE_90D_pct": 18.78, "MFE_180D_pct": 18.78, "MAE_30D_pct": -16.79, "MAE_90D_pct": -27.24, "MAE_180D_pct": -42.72, "peak_date": "2024-02-01", "peak_price": 9550.0, "drawdown_after_peak_pct": -51.78, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_telemedicine_policy_peak_if_usage_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_policy_reversal_contract_loss_usage_collapse_margin_or_financing_break", "trigger_outcome_label": "counterexample_telemedicine_IT_policy_beta_local4b", "current_profile_verdict": "C31 should not treat telemedicine or healthcare-IT policy beta as durable Stage2 unless policy event maps to direct installed-base demand, contract conversion, usage/revenue and margin evidence. BitComputer had an immediate MFE spike and then a long drawdown, making it local 4B rather than Green.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C31_TELEMEDICINE_POLICY_032850_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R12L78-C31-263700-CARELabs-DIGITAL-HEALTH-PLATFORM-POLICY-FADE", "case_id": "R12L78-C31-263700-CARELabs-DIGITAL-HEALTH-PLATFORM-POLICY-FADE", "symbol": "263700", "company_name": "케어랩스", "round": "R12", "loop": "78", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "TELEMEDICINE_DIGITAL_HEALTH_POLICY_DIRECT_DEMAND_BRIDGE_VS_POLICY_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|policy_event_bridge_guardrail", "trigger_type": "Stage2-FalsePositive / DigitalHealthPlatformPolicyThemeFade", "trigger_date": "2024-01-30", "entry_date": "2024-02-01", "entry_price": 4310.0, "evidence_available_at_that_date": "DIGITAL_HEALTH_PLATFORM_TELEMEDICINE_POLICY_THEME_WITH_WEAK_TRANSACTION_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:CARELABS_2024_DIGITAL_HEALTH_PLATFORM_TELEMEDICINE_POLICY_TRANSACTION_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["policy_event", "direct_beneficiary_mapping_candidate", "usage_transaction_revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "contract_conversion_or_installed_base_candidate"], "stage4b_evidence_fields": ["policy_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/263/263700/2024.csv", "profile_path": "atlas/symbol_profiles/263/263700.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 81.0, "MFE_90D_pct": 81.0, "MFE_180D_pct": 81.0, "MAE_30D_pct": -3.36, "MAE_90D_pct": -4.64, "MAE_180D_pct": -32.71, "peak_date": "2024-02-20", "peak_price": 7800.0, "drawdown_after_peak_pct": -62.82, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_telemedicine_policy_peak_if_usage_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_policy_reversal_contract_loss_usage_collapse_margin_or_financing_break", "trigger_outcome_label": "counterexample_digital_health_platform_policy_beta_local4b", "current_profile_verdict": "C31 should not treat digital-health platform policy beta as durable Stage2 unless policy maps to appointment/transaction volume, hospital/clinic adoption, revenue conversion and margin bridge. CareLabs produced a sharp MFE, but then a severe drawdown path, so the row is useful as local 4B boundary.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C31_TELEMEDICINE_POLICY_263700_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L78-C31-032620-UBCARE-TELEMEDICINE-POLICY-DIRECT-DEMAND", "trigger_id": "TRG_R12L78-C31-032620-UBCARE-TELEMEDICINE-POLICY-DIRECT-DEMAND", "symbol": "032620", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"policy_or_regulatory_score": 14, "direct_beneficiary_mapping_score": 13, "usage_transaction_score": 11, "contract_revenue_conversion_score": 10, "margin_bridge_score": 9, "relative_strength_score": 13, "execution_risk_score": 12, "source_confidence_score": 2}, "weighted_score_before": 70, "stage_label_before": "Policy lifecycle candidate after source repair", "raw_component_scores_after": {"policy_or_regulatory_score": 8, "direct_beneficiary_mapping_score": 16, "usage_transaction_score": 14, "contract_revenue_conversion_score": 13, "margin_bridge_score": 12, "relative_strength_score": 12, "execution_risk_score": 13, "source_confidence_score": 2}, "weighted_score_after": 76, "stage_label_after": "Policy lifecycle Stage2-Yellow after source repair + local 4B", "changed_components": ["policy_or_regulatory_score", "direct_beneficiary_mapping_score", "usage_transaction_score", "contract_revenue_conversion_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Cap policy-event scores unless telemedicine/digital-health policy maps to direct beneficiary economics, usage/transaction volume, contract conversion, revenue and margin bridge.", "MFE_90D_pct": 52.12, "MAE_90D_pct": -11.25, "score_return_alignment_label": "policy_lifecycle_with_later_4b", "current_profile_verdict": "C31 can allow telemedicine/digital-health policy rows when policy relaxation maps to direct clinic/EMR platform usage, claim/workflow demand, paid usage, revenue conversion and margin bridge. UBCare produced a large MFE, but later drawdown means it cannot remain Green unless direct-demand and margin evidence refreshes."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L78-C31-032850-BITCOMPUTER-TELEMEDICINE-IT-POLICY-THEME-FADE", "trigger_id": "TRG_R12L78-C31-032850-BITCOMPUTER-TELEMEDICINE-IT-POLICY-THEME-FADE", "symbol": "032850", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"policy_or_regulatory_score": 14, "direct_beneficiary_mapping_score": 4, "usage_transaction_score": 2, "contract_revenue_conversion_score": 2, "margin_bridge_score": 1, "relative_strength_score": 5, "execution_risk_score": 22, "source_confidence_score": 2}, "weighted_score_before": 48, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"policy_or_regulatory_score": 8, "direct_beneficiary_mapping_score": 2, "usage_transaction_score": 1, "contract_revenue_conversion_score": 1, "margin_bridge_score": 1, "relative_strength_score": 4, "execution_risk_score": 24, "source_confidence_score": 2}, "weighted_score_after": 34, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["policy_or_regulatory_score", "direct_beneficiary_mapping_score", "usage_transaction_score", "contract_revenue_conversion_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Cap policy-event scores unless telemedicine/digital-health policy maps to direct beneficiary economics, usage/transaction volume, contract conversion, revenue and margin bridge.", "MFE_90D_pct": 18.78, "MAE_90D_pct": -27.24, "score_return_alignment_label": "policy_theme_false_positive_bridge_gap", "current_profile_verdict": "C31 should not treat telemedicine or healthcare-IT policy beta as durable Stage2 unless policy event maps to direct installed-base demand, contract conversion, usage/revenue and margin evidence. BitComputer had an immediate MFE spike and then a long drawdown, making it local 4B rather than Green."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L78-C31-263700-CARELabs-DIGITAL-HEALTH-PLATFORM-POLICY-FADE", "trigger_id": "TRG_R12L78-C31-263700-CARELabs-DIGITAL-HEALTH-PLATFORM-POLICY-FADE", "symbol": "263700", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"policy_or_regulatory_score": 14, "direct_beneficiary_mapping_score": 4, "usage_transaction_score": 2, "contract_revenue_conversion_score": 2, "margin_bridge_score": 1, "relative_strength_score": 13, "execution_risk_score": 22, "source_confidence_score": 2}, "weighted_score_before": 48, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"policy_or_regulatory_score": 8, "direct_beneficiary_mapping_score": 2, "usage_transaction_score": 1, "contract_revenue_conversion_score": 1, "margin_bridge_score": 1, "relative_strength_score": 4, "execution_risk_score": 24, "source_confidence_score": 2}, "weighted_score_after": 34, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["policy_or_regulatory_score", "direct_beneficiary_mapping_score", "usage_transaction_score", "contract_revenue_conversion_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Cap policy-event scores unless telemedicine/digital-health policy maps to direct beneficiary economics, usage/transaction volume, contract conversion, revenue and margin bridge.", "MFE_90D_pct": 81.0, "MAE_90D_pct": -4.64, "score_return_alignment_label": "policy_theme_false_positive_bridge_gap", "current_profile_verdict": "C31 should not treat digital-health platform policy beta as durable Stage2 unless policy maps to appointment/transaction volume, hospital/clinic adoption, revenue conversion and margin bridge. CareLabs produced a sharp MFE, but then a severe drawdown path, so the row is useful as local 4B boundary."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R12", "loop": 78, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "TELEMEDICINE_DIGITAL_HEALTH_POLICY_DIRECT_DEMAND_BRIDGE_VS_POLICY_THEME_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 1, "positive_case_count": 1, "counterexample_count": 2, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "current_profile_error_count": 2, "diversity_score_summary": "+3 underused C31 telemedicine/digital-health symbols outside top-covered 112610/034020/336260/036460 set and outside loop-77 low-birth symbols, +1 telemedicine policy trigger family, +1 direct-beneficiary lifecycle candidate, +2 digital-health policy-theme local-4B counterexamples, no hard duplicate", "residual_contribution_label": "policy_event_bridge_guardrail_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R12", "loop": 78, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "axis": "telemedicine_digital_health_policy_direct_demand_bridge_vs_policy_theme_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C31 should split telemedicine/digital-health policy direct-demand lifecycle trades from generic policy theme beta. Stage2 requires explicit policy event plus direct beneficiary mapping, installed-base or usage/transaction evidence, contract/revenue conversion and margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["032620", "032850", "263700"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R12", "loop": 78, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "existing_axis_strengthened": ["price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "stage2_required_bridge", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C31 telemedicine/digital-health policy events need direct-beneficiary proof. UBCare shows a policy lifecycle MFE candidate after source repair; BitComputer and CareLabs show digital-health policy beta fading into local 4B when usage, contract, revenue and margin bridge are absent or stale."}
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
032620:
  name = 유비케어 from 2008-05-20
  corporate_action_candidate_dates = 1998-01-06, 1999-08-30, 1999-10-21, 1999-11-05, 1999-12-07, 2018-05-11
  selected window = 2024-02-01~D+180
  contamination = false

032850:
  name = 비트컴퓨터
  corporate_action_candidate_dates = 1999-06-22, 1999-07-16, 1999-11-15, 2000-02-25, 2000-04-25
  selected window = 2024-02-01~D+180
  contamination = false

263700:
  name = 케어랩스
  corporate_action_candidate_dates = 2020-07-16, 2020-08-06
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C31 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C31 rule-shape discovery,
but coding-agent promotion requires non-proxy telemedicine/digital-health policy evidence, direct beneficiary mapping, usage/transaction volume, contract conversion, revenue and margin bridge evidence.
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
telemedicine_digital_health_policy_direct_demand_bridge_vs_policy_theme_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 032620, 032850 and 263700.
4. Keep generic C31 policy-event weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - policy/regulatory event is explicit,
   - direct beneficiary mapping is visible,
   - installed-base usage, transaction volume or claim/workflow demand exists,
   - contract / paid conversion / revenue bridge exists,
   - margin bridge is credible,
   - MAE remains controlled or the signal is lifecycle-managed.
6. Consider local 4B-watch when:
   - the trigger is telemedicine/digital-health policy theme beta only,
   - usage/transaction/revenue/margin bridge is absent or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
7. Do not convert local 4B-watch into full 4B/4C without non-price policy reversal, contract loss, usage collapse, channel issue, margin collapse, financing or liquidity evidence.
8. Emit before/after diagnostics and reject if verified direct-demand policy lifecycle positives are overblocked.
```

---

## Final round state

```text
completed_round = R12
completed_loop = 78
next_round = R13
next_loop = 78
round_schedule_status = valid
round_sector_consistency = pass
```

