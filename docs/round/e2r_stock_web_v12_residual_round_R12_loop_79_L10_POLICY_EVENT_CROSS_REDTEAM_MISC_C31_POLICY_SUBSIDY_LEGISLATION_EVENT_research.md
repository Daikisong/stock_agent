# E2R Stock-Web v12 Residual Research — R12 Loop 79 / L10 / C31

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R12",
  "scheduled_loop": 79,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R12",
  "completed_loop": 79,
  "computed_next_round": "R13",
  "computed_next_loop": 79,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "fine_archetype_id": "PUBLIC_UTILITY_TARIFF_NORMALIZATION_DIRECT_EARNINGS_BRIDGE_VS_ENERGY_POLICY_THEME_BETA",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "policy_event_bridge_guardrail",
    "4B_non_price_requirement_stress_test",
    "public_utility_tariff_normalization_direct_beneficiary_mapping",
    "energy_tariff_policy_theme_beta_boundary",
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

Previous completed state in this interactive run: R11 / loop 79.

Therefore:

```text
scheduled_round = R12
scheduled_loop = 79
allowed_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC or relevant under-covered service/agri sector
selected_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
selected_canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
computed_next_round = R13
computed_next_loop = 79
```

R12 was routed to C31 because this is a public-utility tariff normalization / policy event bridge guardrail, not a normal financial, grid, or consumer operating-leverage round.

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

This run uses three different symbols and avoids loop-78 telemedicine names:

```text
015760 / 한국전력 / tariff-normalization and debt-recovery bridge
071320 / 지역난방공사 / district-heating tariff and earnings-recovery bridge
117580 / 대성에너지 / city-gas / energy policy theme beta boundary
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
No selected row has a profile-level 2024 corporate-action candidate inside the selected window.
```

## Research thesis

C31 is not “정책 테마가 올랐다.”

For public utility / tariff normalization rows, the bridge must pass through:

```text
policy / tariff / regulation event
→ direct beneficiary mapping
→ fuel, heat or gas cost pass-through
→ earnings and debt recovery
→ dividend, capital policy or margin bridge
→ durable rerating
```

정책 headline은 밸브다.  
C31이 보려는 것은 그 밸브가 실제 요금, 원가 전가, 이익, 부채 회복, 마진으로 물을 흘려보내는지다.

---

## Case 1 — Policy lifecycle candidate: 015760 / 한국전력

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is utility tariff normalization, fuel-cost pass-through, debt recovery, earnings bridge and regulatory visibility evidence.

```text
evidence_family = PUBLIC_UTILITY_TARIFF_NORMALIZATION_FUEL_COST_PASS_THROUGH_DEBT_RECOVERY_EARNINGS_BRIDGE_CANDIDATE
case_role = policy_lifecycle_positive_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 19,720
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/015/015760/2024.csv`:

```text
2024-02-01,19720,20550,19660,20400
2024-02-19,21700,23350,21550,23200
2024-02-26,24100,24950,22800,24850
2024-02-29,24550,25100,24450,24800
2024-03-19,24000,24050,22150,22400
2024-08-05,19600,19610,18190,18400
2024-10-24,22250,23250,22200,23050
```

### Backtest

```text
MFE_30D  = +27.28%
MAE_30D  = -0.30%
MFE_90D  = +27.28%
MAE_90D  = -0.30%
MFE_180D = +27.28%
MAE_180D = -7.76%
peak_180 = 25,100 on 2024-02-29
trough_180 = 18,190 on 2024-08-05
peak_to_later_drawdown = -27.53%
```

### Interpretation

This is a C31 utility-tariff lifecycle candidate.  
The policy move was tradable and entry-basis MAE was controlled.

Correct treatment:

```text
source repair first
possible policy lifecycle Stage2-Yellow
later local 4B if tariff / fuel-cost / debt-recovery / earnings bridge fades
```

---

## Case 2 — Policy lifecycle candidate: 071320 / 지역난방공사

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is district-heating tariff, heat/fuel cost pass-through, direct earnings recovery, dividend/capital policy and regulatory visibility evidence.

```text
evidence_family = DISTRICT_HEATING_TARIFF_COST_PASS_THROUGH_EARNINGS_RECOVERY_DIVIDEND_POLICY_BRIDGE_CANDIDATE
case_role = policy_lifecycle_positive_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 32,450
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/071/071320/2024.csv`:

```text
2024-02-01,32450,35050,31800,34400
2024-02-19,34200,43350,34200,43350
2024-02-26,39450,51300,39000,40300
2024-03-20,37300,37900,36600,36600
2024-08-05,45750,46200,42800,43650
2024-08-28,52400,52700,50100,50400
2024-10-11,44900,45000,44100,44250
```

### Backtest

```text
MFE_30D  = +58.09%
MAE_30D  = -2.00%
MFE_90D  = +58.09%
MAE_90D  = -2.00%
MFE_180D = +62.40%
MAE_180D = -2.00%
peak_180 = 52,700 on 2024-08-28
trough_180 = 31,800 on 2024-02-01
peak_to_later_drawdown = -16.32%
```

### Interpretation

This is the clean utility-policy direct-beneficiary candidate.  
The MFE was large and the entry-basis MAE stayed controlled.

Correct treatment:

```text
verified tariff / cost pass-through / earnings recovery / dividend bridge → Stage2 possible
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 3 — Counterexample / local 4B: 117580 / 대성에너지

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests city-gas / energy policy and geopolitical beta without enough direct tariff, volume, cost pass-through and earnings bridge.

```text
evidence_family = CITY_GAS_ENERGY_POLICY_GEOPOLITICAL_THEME_WITH_WEAK_DIRECT_TARIFF_EARNINGS_MARGIN_BRIDGE
case_role = counterexample_energy_policy_theme_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 8,810
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/117/117580/2024.csv`:

```text
2024-02-01,8810,8950,8700,8920
2024-02-14,9150,9550,8950,9170
2024-03-12,8060,8080,7960,8060
2024-04-05,9540,10000,9330,9350
2024-07-31,9290,11200,9080,10200
2024-08-13,11450,12350,11350,11620
2024-09-09,8690,9030,8630,8970
```

### Backtest

```text
MFE_30D  = +8.40%
MAE_30D  = -9.65%
MFE_90D  = +13.51%
MAE_90D  = -9.65%
MFE_180D = +40.18%
MAE_180D = -9.65%
peak_180 = 12,350 on 2024-08-13
trough_180 = 7,960 on 2024-03-12
peak_to_later_drawdown = -30.12%
```

### Interpretation

This is a policy/energy theme-beta boundary.  
The move was tradable, but durable C31 requires direct tariff and earnings economics.

Correct treatment:

```text
city-gas / energy policy theme beta
→ no verified direct tariff / cost pass-through / earnings / margin bridge
→ local 4B-watch rather than durable Green
```

---

## Cross-case residual finding

### What this strengthens

```text
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
stage2_required_bridge = strengthen
direct_beneficiary_mapping_required = strengthen
full_4b_requires_non_price_evidence = keep
```

### What this does not justify

```text
do_not_raise_generic_C31_utility_policy_weight = true
do_not_treat_utility_tariff_policy_headline_as_Green_without_direct_earnings_bridge = true
do_not_convert_policy_theme_drawdown_to_hard_4C_without_non_price_policy_reversal_tariff_denial_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
PUBLIC_UTILITY_TARIFF_NORMALIZATION_DIRECT_EARNINGS_BRIDGE_VS_ENERGY_POLICY_THEME_BETA
```

This fine archetype covers:

```text
1. KEPCO tariff/debt-recovery bridge → policy lifecycle candidate after source repair
2. district-heating tariff/cost pass-through bridge → policy lifecycle candidate after source repair
3. city-gas/energy policy beta without direct economics → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R12L79-C31-015760-KEPCO-TARIFF-NORMALIZATION-DEBT-RECOVERY", "symbol": "015760", "company_name": "한국전력", "round": "R12", "loop": "79", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "PUBLIC_UTILITY_TARIFF_NORMALIZATION_DIRECT_EARNINGS_BRIDGE_VS_ENERGY_POLICY_THEME_BETA", "case_type": "policy_subsidy_legislation_event_public_utility_tariff", "positive_or_counterexample": "policy_lifecycle_positive", "best_trigger": "Stage2-PolicyLifecycle-UtilityTariffNormalizationDebtRecoveryBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C31 can allow public-utility policy rows when tariff normalization maps to direct beneficiary economics, fuel-cost pass-through, debt recovery, earnings bridge and regulatory visibility. KEPCO produced meaningful MFE with bounded entry-basis MAE, but later drawdown means tariff/debt/earnings evidence must refresh.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy utility tariff policy, direct beneficiary mapping, cost pass-through, earnings recovery, debt/dividend and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R12L79-C31-071320-DISTRICT-HEATING-TARIFF-RECOVERY-BRIDGE", "symbol": "071320", "company_name": "지역난방공사", "round": "R12", "loop": "79", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "PUBLIC_UTILITY_TARIFF_NORMALIZATION_DIRECT_EARNINGS_BRIDGE_VS_ENERGY_POLICY_THEME_BETA", "case_type": "policy_subsidy_legislation_event_public_utility_tariff", "positive_or_counterexample": "policy_lifecycle_positive", "best_trigger": "Stage2-PolicyLifecycle-DistrictHeatingTariffRecoveryBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C31 should preserve utility tariff normalization positives when policy adjustment maps to cost pass-through, direct earnings recovery, dividend/capital policy and regulatory visibility. Korea District Heating produced very large MFE with controlled entry-basis MAE, but the post-peak drawdown needs lifecycle management.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy utility tariff policy, direct beneficiary mapping, cost pass-through, earnings recovery, debt/dividend and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R12L79-C31-117580-DAESUNG-ENERGY-GAS-POLICY-THEME-BETA", "symbol": "117580", "company_name": "대성에너지", "round": "R12", "loop": "79", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "PUBLIC_UTILITY_TARIFF_NORMALIZATION_DIRECT_EARNINGS_BRIDGE_VS_ENERGY_POLICY_THEME_BETA", "case_type": "policy_subsidy_legislation_event_public_utility_tariff", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / CityGasEnergyPolicyThemeBetaFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C31 should not treat city-gas or energy policy/geopolitical beta as durable Stage2 unless tariff formula, direct beneficiary mapping, volume, cost pass-through, earnings and margin bridge are visible. Daesung Energy produced tradable MFE but also a drawdown path; without direct-economics proof it should be local 4B-watch rather than Green.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy utility tariff policy, direct beneficiary mapping, cost pass-through, earnings recovery, debt/dividend and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R12L79-C31-015760-KEPCO-TARIFF-NORMALIZATION-DEBT-RECOVERY", "case_id": "R12L79-C31-015760-KEPCO-TARIFF-NORMALIZATION-DEBT-RECOVERY", "symbol": "015760", "company_name": "한국전력", "round": "R12", "loop": "79", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "PUBLIC_UTILITY_TARIFF_NORMALIZATION_DIRECT_EARNINGS_BRIDGE_VS_ENERGY_POLICY_THEME_BETA", "loop_objective": "coverage_gap_fill|counterexample_mining|policy_event_bridge_guardrail", "trigger_type": "Stage2-PolicyLifecycle-UtilityTariffNormalizationDebtRecoveryBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 19720.0, "evidence_available_at_that_date": "PUBLIC_UTILITY_TARIFF_NORMALIZATION_FUEL_COST_PASS_THROUGH_DEBT_RECOVERY_EARNINGS_BRIDGE_CANDIDATE", "evidence_source": "source_proxy_manual_verification_required:KEPCO_2024_PUBLIC_UTILITY_TARIFF_NORMALIZATION_FUEL_COST_DEBT_RECOVERY_EARNINGS_BRIDGE", "stage2_evidence_fields": ["policy_or_tariff_event", "direct_beneficiary_mapping_candidate", "cost_passthrough_earnings_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "debt_recovery_dividend_or_regulatory_visibility_candidate"], "stage4b_evidence_fields": ["policy_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/015/015760/2024.csv", "profile_path": "atlas/symbol_profiles/015/015760.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 27.28, "MFE_90D_pct": 27.28, "MFE_180D_pct": 27.28, "MAE_30D_pct": -0.3, "MAE_90D_pct": -0.3, "MAE_180D_pct": -7.76, "peak_date": "2024-02-29", "peak_price": 25100.0, "drawdown_after_peak_pct": -27.53, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_tariff_policy_peak_if_direct_earnings_cost_passthrough_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_policy_reversal_tariff_denial_cost_shock_liquidity_or_margin_break", "trigger_outcome_label": "policy_lifecycle_positive_with_later_4b_watch", "current_profile_verdict": "C31 can allow public-utility policy rows when tariff normalization maps to direct beneficiary economics, fuel-cost pass-through, debt recovery, earnings bridge and regulatory visibility. KEPCO produced meaningful MFE with bounded entry-basis MAE, but later drawdown means tariff/debt/earnings evidence must refresh.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C31_UTILITY_TARIFF_POLICY_015760_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R12L79-C31-071320-DISTRICT-HEATING-TARIFF-RECOVERY-BRIDGE", "case_id": "R12L79-C31-071320-DISTRICT-HEATING-TARIFF-RECOVERY-BRIDGE", "symbol": "071320", "company_name": "지역난방공사", "round": "R12", "loop": "79", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "PUBLIC_UTILITY_TARIFF_NORMALIZATION_DIRECT_EARNINGS_BRIDGE_VS_ENERGY_POLICY_THEME_BETA", "loop_objective": "coverage_gap_fill|counterexample_mining|policy_event_bridge_guardrail", "trigger_type": "Stage2-PolicyLifecycle-DistrictHeatingTariffRecoveryBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 32450.0, "evidence_available_at_that_date": "DISTRICT_HEATING_TARIFF_COST_PASS_THROUGH_EARNINGS_RECOVERY_DIVIDEND_POLICY_BRIDGE_CANDIDATE", "evidence_source": "source_proxy_manual_verification_required:KOREA_DISTRICT_HEATING_2024_TARIFF_COST_PASS_THROUGH_EARNINGS_RECOVERY_DIVIDEND_BRIDGE", "stage2_evidence_fields": ["policy_or_tariff_event", "direct_beneficiary_mapping_candidate", "cost_passthrough_earnings_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "debt_recovery_dividend_or_regulatory_visibility_candidate"], "stage4b_evidence_fields": ["policy_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/071/071320/2024.csv", "profile_path": "atlas/symbol_profiles/071/071320.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 58.09, "MFE_90D_pct": 58.09, "MFE_180D_pct": 62.4, "MAE_30D_pct": -2.0, "MAE_90D_pct": -2.0, "MAE_180D_pct": -2.0, "peak_date": "2024-08-28", "peak_price": 52700.0, "drawdown_after_peak_pct": -16.32, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_tariff_policy_peak_if_direct_earnings_cost_passthrough_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_policy_reversal_tariff_denial_cost_shock_liquidity_or_margin_break", "trigger_outcome_label": "policy_lifecycle_positive_with_later_4b_watch", "current_profile_verdict": "C31 should preserve utility tariff normalization positives when policy adjustment maps to cost pass-through, direct earnings recovery, dividend/capital policy and regulatory visibility. Korea District Heating produced very large MFE with controlled entry-basis MAE, but the post-peak drawdown needs lifecycle management.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C31_UTILITY_TARIFF_POLICY_071320_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R12L79-C31-117580-DAESUNG-ENERGY-GAS-POLICY-THEME-BETA", "case_id": "R12L79-C31-117580-DAESUNG-ENERGY-GAS-POLICY-THEME-BETA", "symbol": "117580", "company_name": "대성에너지", "round": "R12", "loop": "79", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "PUBLIC_UTILITY_TARIFF_NORMALIZATION_DIRECT_EARNINGS_BRIDGE_VS_ENERGY_POLICY_THEME_BETA", "loop_objective": "coverage_gap_fill|counterexample_mining|policy_event_bridge_guardrail", "trigger_type": "Stage2-FalsePositive / CityGasEnergyPolicyThemeBetaFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 8810.0, "evidence_available_at_that_date": "CITY_GAS_ENERGY_POLICY_GEOPOLITICAL_THEME_WITH_WEAK_DIRECT_TARIFF_EARNINGS_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:DAESUNG_ENERGY_2024_CITY_GAS_ENERGY_POLICY_TARIFF_VOLUME_COST_PASS_THROUGH_EARNINGS_BRIDGE", "stage2_evidence_fields": ["policy_or_tariff_event", "direct_beneficiary_mapping_candidate", "cost_passthrough_earnings_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "debt_recovery_dividend_or_regulatory_visibility_candidate"], "stage4b_evidence_fields": ["policy_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/117/117580/2024.csv", "profile_path": "atlas/symbol_profiles/117/117580.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 8.4, "MFE_90D_pct": 13.51, "MFE_180D_pct": 40.18, "MAE_30D_pct": -9.65, "MAE_90D_pct": -9.65, "MAE_180D_pct": -9.65, "peak_date": "2024-08-13", "peak_price": 12350.0, "drawdown_after_peak_pct": -30.12, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_tariff_policy_peak_if_direct_earnings_cost_passthrough_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_policy_reversal_tariff_denial_cost_shock_liquidity_or_margin_break", "trigger_outcome_label": "counterexample_energy_policy_theme_local4b", "current_profile_verdict": "C31 should not treat city-gas or energy policy/geopolitical beta as durable Stage2 unless tariff formula, direct beneficiary mapping, volume, cost pass-through, earnings and margin bridge are visible. Daesung Energy produced tradable MFE but also a drawdown path; without direct-economics proof it should be local 4B-watch rather than Green.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C31_UTILITY_TARIFF_POLICY_117580_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L79-C31-015760-KEPCO-TARIFF-NORMALIZATION-DEBT-RECOVERY", "trigger_id": "TRG_R12L79-C31-015760-KEPCO-TARIFF-NORMALIZATION-DEBT-RECOVERY", "symbol": "015760", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"policy_or_tariff_score": 14, "direct_beneficiary_mapping_score": 14, "cost_passthrough_score": 13, "earnings_recovery_score": 13, "debt_dividend_margin_bridge_score": 12, "relative_strength_score": 12, "execution_risk_score": 10, "source_confidence_score": 2}, "weighted_score_before": 76, "stage_label_before": "Policy lifecycle candidate after source repair", "raw_component_scores_after": {"policy_or_tariff_score": 10, "direct_beneficiary_mapping_score": 16, "cost_passthrough_score": 15, "earnings_recovery_score": 15, "debt_dividend_margin_bridge_score": 14, "relative_strength_score": 11, "execution_risk_score": 11, "source_confidence_score": 2}, "weighted_score_after": 82, "stage_label_after": "Policy lifecycle Stage2-Yellow after source repair + local 4B", "changed_components": ["policy_or_tariff_score", "direct_beneficiary_mapping_score", "cost_passthrough_score", "earnings_recovery_score", "debt_dividend_margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Cap policy-event scores unless tariff normalization maps to direct beneficiary economics, cost pass-through, earnings recovery, debt/dividend and margin bridge.", "MFE_90D_pct": 27.28, "MAE_90D_pct": -0.3, "score_return_alignment_label": "policy_tariff_lifecycle_with_later_4b", "current_profile_verdict": "C31 can allow public-utility policy rows when tariff normalization maps to direct beneficiary economics, fuel-cost pass-through, debt recovery, earnings bridge and regulatory visibility. KEPCO produced meaningful MFE with bounded entry-basis MAE, but later drawdown means tariff/debt/earnings evidence must refresh."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L79-C31-071320-DISTRICT-HEATING-TARIFF-RECOVERY-BRIDGE", "trigger_id": "TRG_R12L79-C31-071320-DISTRICT-HEATING-TARIFF-RECOVERY-BRIDGE", "symbol": "071320", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"policy_or_tariff_score": 14, "direct_beneficiary_mapping_score": 14, "cost_passthrough_score": 13, "earnings_recovery_score": 13, "debt_dividend_margin_bridge_score": 12, "relative_strength_score": 12, "execution_risk_score": 10, "source_confidence_score": 2}, "weighted_score_before": 76, "stage_label_before": "Policy lifecycle candidate after source repair", "raw_component_scores_after": {"policy_or_tariff_score": 10, "direct_beneficiary_mapping_score": 16, "cost_passthrough_score": 15, "earnings_recovery_score": 15, "debt_dividend_margin_bridge_score": 14, "relative_strength_score": 11, "execution_risk_score": 11, "source_confidence_score": 2}, "weighted_score_after": 82, "stage_label_after": "Policy lifecycle Stage2-Yellow after source repair + local 4B", "changed_components": ["policy_or_tariff_score", "direct_beneficiary_mapping_score", "cost_passthrough_score", "earnings_recovery_score", "debt_dividend_margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Cap policy-event scores unless tariff normalization maps to direct beneficiary economics, cost pass-through, earnings recovery, debt/dividend and margin bridge.", "MFE_90D_pct": 58.09, "MAE_90D_pct": -2.0, "score_return_alignment_label": "policy_tariff_lifecycle_with_later_4b", "current_profile_verdict": "C31 should preserve utility tariff normalization positives when policy adjustment maps to cost pass-through, direct earnings recovery, dividend/capital policy and regulatory visibility. Korea District Heating produced very large MFE with controlled entry-basis MAE, but the post-peak drawdown needs lifecycle management."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L79-C31-117580-DAESUNG-ENERGY-GAS-POLICY-THEME-BETA", "trigger_id": "TRG_R12L79-C31-117580-DAESUNG-ENERGY-GAS-POLICY-THEME-BETA", "symbol": "117580", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"policy_or_tariff_score": 14, "direct_beneficiary_mapping_score": 4, "cost_passthrough_score": 3, "earnings_recovery_score": 2, "debt_dividend_margin_bridge_score": 2, "relative_strength_score": 12, "execution_risk_score": 22, "source_confidence_score": 2}, "weighted_score_before": 46, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"policy_or_tariff_score": 10, "direct_beneficiary_mapping_score": 2, "cost_passthrough_score": 1, "earnings_recovery_score": 1, "debt_dividend_margin_bridge_score": 1, "relative_strength_score": 4, "execution_risk_score": 24, "source_confidence_score": 2}, "weighted_score_after": 34, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["policy_or_tariff_score", "direct_beneficiary_mapping_score", "cost_passthrough_score", "earnings_recovery_score", "debt_dividend_margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Cap policy-event scores unless tariff normalization maps to direct beneficiary economics, cost pass-through, earnings recovery, debt/dividend and margin bridge.", "MFE_90D_pct": 13.51, "MAE_90D_pct": -9.65, "score_return_alignment_label": "policy_theme_false_positive_direct_economics_gap", "current_profile_verdict": "C31 should not treat city-gas or energy policy/geopolitical beta as durable Stage2 unless tariff formula, direct beneficiary mapping, volume, cost pass-through, earnings and margin bridge are visible. Daesung Energy produced tradable MFE but also a drawdown path; without direct-economics proof it should be local 4B-watch rather than Green."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R12", "loop": 79, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "PUBLIC_UTILITY_TARIFF_NORMALIZATION_DIRECT_EARNINGS_BRIDGE_VS_ENERGY_POLICY_THEME_BETA", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 2, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "current_profile_error_count": 1, "diversity_score_summary": "+3 underused C31 public-utility/energy-policy symbols outside top-covered 112610/034020/336260/036460 set and outside loop-78 telemedicine names, +2 tariff-normalization direct-beneficiary positives, +1 city-gas/energy policy-theme local-4B counterexample, no hard duplicate", "residual_contribution_label": "policy_event_bridge_guardrail_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R12", "loop": 79, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "axis": "public_utility_tariff_normalization_direct_earnings_bridge_vs_energy_policy_theme_beta", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C31 should split utility tariff-normalization direct-beneficiary lifecycle trades from generic energy policy theme beta. Stage2 requires explicit policy/tariff event plus direct beneficiary mapping, fuel or heat cost pass-through, earnings/debt recovery and dividend/margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["015760", "071320", "117580"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R12", "loop": 79, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "existing_axis_strengthened": ["price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "stage2_required_bridge", "direct_beneficiary_mapping_required", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C31 utility policy events need direct-beneficiary proof. KEPCO and Korea District Heating show tariff-normalization lifecycle MFE candidates after source repair; Daesung Energy shows energy/city-gas policy beta that should not become durable Green without tariff, cost pass-through, earnings and margin bridge."}
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
015760:
  name = 한국전력 from 1996-11-25, 한국전력공사 before that
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false

071320:
  name = 지역난방공사
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false

117580:
  name = 대성에너지 from 2011-04-08, 대구도시가스 before that
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C31 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C31 policy-event rule-shape discovery,
but coding-agent promotion requires non-proxy utility tariff policy evidence, direct beneficiary mapping, fuel/heat/gas cost pass-through, earnings recovery, debt/dividend and margin bridge evidence.
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
public_utility_tariff_normalization_direct_earnings_bridge_vs_energy_policy_theme_beta

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 015760, 071320 and 117580.
4. Keep generic C31 policy-event weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - tariff / policy / regulation event is explicit,
   - direct beneficiary mapping is visible,
   - cost pass-through or tariff formula benefit exists,
   - earnings/debt recovery bridge exists,
   - dividend/capital policy or margin bridge is credible,
   - MAE remains controlled or the signal is lifecycle-managed.
6. Consider local 4B-watch when:
   - the trigger is utility/energy policy theme beta only,
   - direct beneficiary / cost pass-through / earnings / margin bridge is absent or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
7. Do not convert local 4B-watch into full 4B/4C without non-price policy reversal, tariff denial, cost shock, liquidity issue, debt stress or margin collapse evidence.
8. Emit before/after diagnostics and reject if verified direct-beneficiary policy lifecycle positives are overblocked.
```

---

## Final round state

```text
completed_round = R12
completed_loop = 79
next_round = R13
next_loop = 79
round_schedule_status = valid
round_sector_consistency = pass
```

