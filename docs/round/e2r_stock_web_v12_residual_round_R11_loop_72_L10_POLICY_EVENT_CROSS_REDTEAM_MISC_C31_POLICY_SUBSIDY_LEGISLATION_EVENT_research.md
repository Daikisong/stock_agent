# E2R Stock-Web v12 Residual Research — R11 Loop 72 / L10 / C31

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R11",
  "scheduled_loop": 72,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R11",
  "completed_loop": 72,
  "computed_next_round": "R12",
  "computed_next_loop": 72,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "fine_archetype_id": "EAST_SEA_OIL_GAS_EXPLORATION_POLICY_PROXY_BLOWOFF_VS_EXECUTION_BRIDGE_ABSENCE",
  "loop_objective": [
    "counterexample_mining",
    "residual_false_positive_mining",
    "4B_non_price_requirement_stress_test",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression",
    "policy_theme_proxy_guardrail"
  ],
  "price_source": "Songdaiki/stock-web",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "stock_web_manifest_max_date": "2026-02-20",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "handoff_prompt_executed_now": false,
  "do_not_propose_new_weight_delta": false
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

Previous completed state in this interactive run: R10 / loop 72.

Therefore:

```text
scheduled_round = R11
scheduled_loop = 72
allowed_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC or L1 policy-defense linkage
selected_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
selected_canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
computed_next_round = R12
computed_next_loop = 72
```

R11 was routed to C31 because this is a policy-resource event test, not a defense-export or grid-capex bridge.  
This file deliberately avoids high-repeat C31 symbols such as 112610, 034020, 336260, 036460 and UNKNOWN_SYMBOL.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Selected rows:

```text
024060 / 흥구석유 / Stage4B-Local-PolicyProxyBlowoff / 2024-06-04
128820 / 대성산업 / Stage2-FalsePositive / PolicyProxyFade / 2024-06-04
053050 / 지에스이 / Stage4B-Local-GasPolicyProxy / 2024-06-04
```

All three share the same national policy event, but they are treated as separate proxy channels:

```text
retail oil distribution proxy
industrial energy proxy
city-gas proxy
```

## Research thesis

C31 should distinguish policy execution from policy heat.

A national-resource headline is a match.  
A company-level bridge is the pipeline.  
Without the pipeline, the flame can flare brightly and still leave no fuel flowing into earnings.

The residual rule candidate is:

```text
policy-resource event + proxy equity MFE ≠ durable Stage2

Stage2 requires one of:
- confirmed reserves or drilling result
- named project participation
- offtake / tariff / budget / subsidy cash-flow bridge
- direct earnings, margin, or contract bridge

If absent:
- high or moderate MFE becomes local 4B-watch after the peak
- full 4B still waits for non-price deterioration
- hard 4C is not inferred from price alone
```

---

## Evidence event

Reuters reported on 2024-06-03 that President Yoon Suk Yeol approved exploratory drilling after citing possible large oil and gas resources off South Korea's east coast. The same report made clear that the project remained exploratory, with drilling needed to determine size and commercial reality. This is a policy/resource headline, not a company-level cash-flow bridge.

```text
evidence_family = EAST_SEA_OIL_GAS_EXPLORATION_POLICY_PROXY_BLOWOFF
trigger_date = 2024-06-03
entry_date = next tradable day, 2024-06-04
```

---

## Case 1 — Counterexample / local 4B: 024060 / 흥구석유

### Evidence

```text
evidence_family = EAST_SEA_OIL_GAS_EXPLORATION_POLICY_RETAIL_OIL_PROXY_NO_CASHFLOW_BRIDGE
case_role = counterexample
trigger_date = 2024-06-03
entry_date = 2024-06-04
entry_price = 17,520
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/024/024060/2024.csv`:

```text
2024-06-04,17520,20950,17510,19240
2024-07-26,12680,12830,12360,12670
2024-08-13,21650,21900,19940,20300
2024-12-10,11800,13020,11800,12870
```

### Backtest

```text
MFE_30D  = +19.58%
MAE_30D  = -21.80%
MFE_90D  = +25.00%
MAE_90D  = -29.45%
MFE_180D = +25.00%
MAE_180D = -32.65%
peak_180 = 21,900 on 2024-08-13
trough_180 = 11,800 on 2024-12-10
peak_to_later_drawdown = -46.12%
```

### Interpretation

The stock produced real tradable MFE, but the bridge is missing.  
A retail oil-distribution proxy is not the same as a confirmed upstream reserve-development cash-flow.

C31 should mark this as:

```text
local 4B-watch after proxy peak
not durable Stage2/Green
```

---

## Case 2 — Counterexample: 128820 / 대성산업

### Evidence

```text
evidence_family = EAST_SEA_OIL_GAS_EXPLORATION_POLICY_INDUSTRIAL_ENERGY_PROXY_WEAK_EXECUTION_BRIDGE
case_role = counterexample
trigger_date = 2024-06-03
entry_date = 2024-06-04
entry_price = 4,250
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/128/128820/2024.csv`:

```text
2024-06-04,4250,4775,4000,4010
2024-08-05,3740,3930,3110,3510
2024-12-09,3165,3180,2990,3000
2024-12-10,2965,3235,2965,3220
```

### Backtest

```text
MFE_30D  = +12.35%
MAE_30D  = -12.47%
MFE_90D  = +12.35%
MAE_90D  = -26.82%
MFE_180D = +12.35%
MAE_180D = -30.24%
peak_180 = 4,775 on 2024-06-04
trough_180 = 2,965 on 2024-12-10
peak_to_later_drawdown = -37.91%
```

### Interpretation

This row is the weaker version of the same error.  
The market tried to map the policy headline onto a diversified energy proxy, but MFE was small and MAE widened.

The model should not let a policy headline plus one-day MFE become Stage2 unless the company has:

```text
named project participation
or reserves/offtake/cash-flow bridge
or direct margin/earnings path
```

---

## Case 3 — Counterexample / local 4B: 053050 / 지에스이

### Evidence

```text
evidence_family = EAST_SEA_OIL_GAS_EXPLORATION_POLICY_CITY_GAS_PROXY_NO_DIRECT_RESERVE_BRIDGE
case_role = counterexample
trigger_date = 2024-06-03
entry_date = 2024-06-04
entry_price = 4,485
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/053/053050/2024.csv`:

```text
2024-06-04,4485,5480,4255,4305
2024-07-26,3215,3275,3200,3275
2024-08-13,4800,5470,4800,5080
2024-12-09,3175,3185,2890,2905
```

### Backtest

```text
MFE_30D  = +22.18%
MAE_30D  = -22.97%
MFE_90D  = +22.18%
MAE_90D  = -28.65%
MFE_180D = +22.18%
MAE_180D = -35.56%
peak_180 = 5,480 on 2024-06-04
trough_180 = 2,890 on 2024-12-09
peak_to_later_drawdown = -47.26%
```

### Interpretation

This is a clean policy-proxy local 4B example.  
A city-gas proxy moved on the policy/resource headline, but no direct reserve-development bridge was available.

The right diagnostic is:

```text
policy proxy blowoff
bridge absent
MAE/drawdown widening
local 4B-watch
```

---

## Cross-case residual finding

### What this strengthens

```text
price_only_blowoff_blocks_positive_stage = strengthen
full_4b_requires_non_price_evidence = keep
local_4b_watch_guard = strengthen
```

### What this does not justify

```text
do_not_raise_generic_C31_policy_weight = true
do_not_treat_policy_resource_headline_as_Green = true
do_not_convert_proxy_drawdown_to_hard_4C_without_non_price_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
EAST_SEA_OIL_GAS_EXPLORATION_POLICY_PROXY_BLOWOFF_VS_EXECUTION_BRIDGE_ABSENCE
```

This fine archetype covers:

```text
1. retail oil proxy MFE without reserve/cash-flow bridge → local 4B-watch
2. diversified energy proxy fade → false Stage2
3. city-gas proxy MFE without direct project bridge → local 4B-watch
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R11L72-C31-024060-HEUNGGU-EAST-SEA-OIL-GAS-PROXY-BLOWOFF", "symbol": "024060", "company_name": "흥구석유", "round": "R11", "loop": "72", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "EAST_SEA_OIL_GAS_EXPLORATION_POLICY_PROXY_BLOWOFF_VS_EXECUTION_BRIDGE_ABSENCE", "case_type": "policy_theme_proxy_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "Stage4B-Local-PolicyProxyBlowoff", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "policy headline generated tradable MFE but no company-level execution/cash-flow bridge; subsequent MAE/drawdown supports local 4B-watch", "current_profile_verdict": "residual_false_positive_guard_required", "price_source": "Songdaiki/stock-web", "notes": "C31 should not treat retail oil-distribution proxy exposure as durable Stage2 after an exploratory national-resource headline. High MFE exists, but no company-level cash-flow bridge appears, and later MAE/drawdown requires local 4B-watch."}
{"row_type": "case", "case_id": "R11L72-C31-128820-DAESUNG-INDUSTRIAL-EAST-SEA-ENERGY-PROXY-FADE", "symbol": "128820", "company_name": "대성산업", "round": "R11", "loop": "72", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "EAST_SEA_OIL_GAS_EXPLORATION_POLICY_PROXY_BLOWOFF_VS_EXECUTION_BRIDGE_ABSENCE", "case_type": "policy_theme_proxy_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / PolicyProxyFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "policy headline generated tradable MFE but no company-level execution/cash-flow bridge; subsequent MAE/drawdown supports local 4B-watch", "current_profile_verdict": "residual_false_positive_guard_required", "price_source": "Songdaiki/stock-web", "notes": "C31 policy-event scoring should discount diversified energy proxy moves when exploration economics, confirmed reserves, direct project participation, or earnings bridge are absent. Small initial MFE and widening 180D MAE make this a false Stage2 / local 4B candidate."}
{"row_type": "case", "case_id": "R11L72-C31-053050-GSE-GAS-PROXY-PRICEONLY-LOCAL4B", "symbol": "053050", "company_name": "지에스이", "round": "R11", "loop": "72", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "EAST_SEA_OIL_GAS_EXPLORATION_POLICY_PROXY_BLOWOFF_VS_EXECUTION_BRIDGE_ABSENCE", "case_type": "policy_theme_proxy_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "Stage4B-Local-GasPolicyProxy", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "policy headline generated tradable MFE but no company-level execution/cash-flow bridge; subsequent MAE/drawdown supports local 4B-watch", "current_profile_verdict": "residual_false_positive_guard_required", "price_source": "Songdaiki/stock-web", "notes": "Gas-distribution proxy MFE can be large after an oil/gas policy headline, but it is not a reserve-development cash-flow bridge. C31 should mark local 4B-watch when MAE widens and no direct participation/offtake/margin evidence appears."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R11L72-C31-024060-HEUNGGU-EAST-SEA-OIL-GAS-PROXY-BLOWOFF", "case_id": "R11L72-C31-024060-HEUNGGU-EAST-SEA-OIL-GAS-PROXY-BLOWOFF", "symbol": "024060", "company_name": "흥구석유", "round": "R11", "loop": "72", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "EAST_SEA_OIL_GAS_EXPLORATION_POLICY_PROXY_BLOWOFF_VS_EXECUTION_BRIDGE_ABSENCE", "loop_objective": "residual_false_positive_mining", "trigger_type": "Stage4B-Local-PolicyProxyBlowoff", "trigger_date": "2024-06-03", "entry_date": "2024-06-04", "entry_price": 17520.0, "evidence_available_at_that_date": "Reuters-reported presidential approval for exploratory drilling of possible east-coast oil/gas resources; evidence describes national exploration potential, not company-level cash-flow bridge.", "evidence_source": "https://www.reuters.com/world/asia-pacific/skoreas-yoon-says-vast-amount-oil-gas-reserve-possible-off-east-coast-2024-06-03/", "stage2_evidence_fields": ["policy_event", "energy_resource_theme", "proxy_equity_attention"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["bridge_absent", "post_peak_drawdown", "MAE_widening"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/024/024060/2024.csv", "profile_path": "atlas/symbol_profiles/024/024060.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 19.58, "MFE_90D_pct": 25.0, "MFE_180D_pct": 25.0, "MAE_30D_pct": -21.8, "MAE_90D_pct": -29.45, "MAE_180D_pct": -32.65, "peak_date": "2024-08-13", "peak_price": 21900.0, "drawdown_after_peak_pct": -46.12, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_should_fire_after_policy_proxy_peak", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_bridge_failure_evidence", "trigger_outcome_label": "policy_proxy_blowoff_counterexample", "current_profile_verdict": "local_4b_watch_should_precede_full_4b", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C31_EAST_SEA_OIL_GAS_20240604_PROXY_GROUP", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_R11L72-C31-128820-DAESUNG-INDUSTRIAL-EAST-SEA-ENERGY-PROXY-FADE", "case_id": "R11L72-C31-128820-DAESUNG-INDUSTRIAL-EAST-SEA-ENERGY-PROXY-FADE", "symbol": "128820", "company_name": "대성산업", "round": "R11", "loop": "72", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "EAST_SEA_OIL_GAS_EXPLORATION_POLICY_PROXY_BLOWOFF_VS_EXECUTION_BRIDGE_ABSENCE", "loop_objective": "residual_false_positive_mining", "trigger_type": "Stage2-FalsePositive / PolicyProxyFade", "trigger_date": "2024-06-03", "entry_date": "2024-06-04", "entry_price": 4250.0, "evidence_available_at_that_date": "Reuters-reported presidential approval for exploratory drilling of possible east-coast oil/gas resources; evidence describes national exploration potential, not company-level cash-flow bridge.", "evidence_source": "https://www.reuters.com/world/asia-pacific/skoreas-yoon-says-vast-amount-oil-gas-reserve-possible-off-east-coast-2024-06-03/", "stage2_evidence_fields": ["policy_event", "energy_resource_theme", "proxy_equity_attention"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["bridge_absent", "post_peak_drawdown", "MAE_widening"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/128/128820/2024.csv", "profile_path": "atlas/symbol_profiles/128/128820.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 12.35, "MFE_90D_pct": 12.35, "MFE_180D_pct": 12.35, "MAE_30D_pct": -12.47, "MAE_90D_pct": -26.82, "MAE_180D_pct": -30.24, "peak_date": "2024-06-04", "peak_price": 4775.0, "drawdown_after_peak_pct": -37.91, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_should_fire_after_policy_proxy_peak", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_bridge_failure_evidence", "trigger_outcome_label": "policy_proxy_blowoff_counterexample", "current_profile_verdict": "local_4b_watch_should_precede_full_4b", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C31_EAST_SEA_OIL_GAS_20240604_PROXY_GROUP", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_R11L72-C31-053050-GSE-GAS-PROXY-PRICEONLY-LOCAL4B", "case_id": "R11L72-C31-053050-GSE-GAS-PROXY-PRICEONLY-LOCAL4B", "symbol": "053050", "company_name": "지에스이", "round": "R11", "loop": "72", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "EAST_SEA_OIL_GAS_EXPLORATION_POLICY_PROXY_BLOWOFF_VS_EXECUTION_BRIDGE_ABSENCE", "loop_objective": "residual_false_positive_mining", "trigger_type": "Stage4B-Local-GasPolicyProxy", "trigger_date": "2024-06-03", "entry_date": "2024-06-04", "entry_price": 4485.0, "evidence_available_at_that_date": "Reuters-reported presidential approval for exploratory drilling of possible east-coast oil/gas resources; evidence describes national exploration potential, not company-level cash-flow bridge.", "evidence_source": "https://www.reuters.com/world/asia-pacific/skoreas-yoon-says-vast-amount-oil-gas-reserve-possible-off-east-coast-2024-06-03/", "stage2_evidence_fields": ["policy_event", "energy_resource_theme", "proxy_equity_attention"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["bridge_absent", "post_peak_drawdown", "MAE_widening"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/053/053050/2024.csv", "profile_path": "atlas/symbol_profiles/053/053050.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 22.18, "MFE_90D_pct": 22.18, "MFE_180D_pct": 22.18, "MAE_30D_pct": -22.97, "MAE_90D_pct": -28.65, "MAE_180D_pct": -35.56, "peak_date": "2024-06-04", "peak_price": 5480.0, "drawdown_after_peak_pct": -47.26, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_should_fire_after_policy_proxy_peak", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_bridge_failure_evidence", "trigger_outcome_label": "policy_proxy_blowoff_counterexample", "current_profile_verdict": "local_4b_watch_should_precede_full_4b", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C31_EAST_SEA_OIL_GAS_20240604_PROXY_GROUP", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L72-C31-024060-HEUNGGU-EAST-SEA-OIL-GAS-PROXY-BLOWOFF", "trigger_id": "TRG_R11L72-C31-024060-HEUNGGU-EAST-SEA-OIL-GAS-PROXY-BLOWOFF", "symbol": "024060", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"policy_or_regulatory_score": 15, "valuation_repricing_score": 12, "relative_strength_score": 10, "contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "customer_quality_score": 0, "execution_risk_score": 8, "legal_or_contract_risk_score": 4, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 64, "stage_label_before": "Stage2-Watch / policy proxy attention", "raw_component_scores_after": {"policy_or_regulatory_score": 8, "valuation_repricing_score": 6, "relative_strength_score": 4, "contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "customer_quality_score": 0, "execution_risk_score": 14, "legal_or_contract_risk_score": 4, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 49, "stage_label_after": "Stage4B-local-watch / no positive Stage2", "changed_components": ["policy_or_regulatory_score", "valuation_repricing_score", "relative_strength_score", "execution_risk_score"], "component_delta_explanation": "Downgrade generic policy headline/proxy momentum because no direct reserves, project participation, offtake, margin, or earnings bridge is visible.", "MFE_90D_pct": 25.0, "MAE_90D_pct": -29.45, "score_return_alignment_label": "high_or_moderate_MFE_but_bridge_absent_and_MAE_drawdown_expand", "current_profile_verdict": "C31 should not treat retail oil-distribution proxy exposure as durable Stage2 after an exploratory national-resource headline. High MFE exists, but no company-level cash-flow bridge appears, and later MAE/drawdown requires local 4B-watch."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L72-C31-128820-DAESUNG-INDUSTRIAL-EAST-SEA-ENERGY-PROXY-FADE", "trigger_id": "TRG_R11L72-C31-128820-DAESUNG-INDUSTRIAL-EAST-SEA-ENERGY-PROXY-FADE", "symbol": "128820", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"policy_or_regulatory_score": 15, "valuation_repricing_score": 12, "relative_strength_score": 10, "contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "customer_quality_score": 0, "execution_risk_score": 8, "legal_or_contract_risk_score": 4, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 64, "stage_label_before": "Stage2-Watch / policy proxy attention", "raw_component_scores_after": {"policy_or_regulatory_score": 8, "valuation_repricing_score": 6, "relative_strength_score": 4, "contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "customer_quality_score": 0, "execution_risk_score": 14, "legal_or_contract_risk_score": 4, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 49, "stage_label_after": "Stage4B-local-watch / no positive Stage2", "changed_components": ["policy_or_regulatory_score", "valuation_repricing_score", "relative_strength_score", "execution_risk_score"], "component_delta_explanation": "Downgrade generic policy headline/proxy momentum because no direct reserves, project participation, offtake, margin, or earnings bridge is visible.", "MFE_90D_pct": 12.35, "MAE_90D_pct": -26.82, "score_return_alignment_label": "high_or_moderate_MFE_but_bridge_absent_and_MAE_drawdown_expand", "current_profile_verdict": "C31 policy-event scoring should discount diversified energy proxy moves when exploration economics, confirmed reserves, direct project participation, or earnings bridge are absent. Small initial MFE and widening 180D MAE make this a false Stage2 / local 4B candidate."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L72-C31-053050-GSE-GAS-PROXY-PRICEONLY-LOCAL4B", "trigger_id": "TRG_R11L72-C31-053050-GSE-GAS-PROXY-PRICEONLY-LOCAL4B", "symbol": "053050", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"policy_or_regulatory_score": 15, "valuation_repricing_score": 12, "relative_strength_score": 10, "contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "customer_quality_score": 0, "execution_risk_score": 8, "legal_or_contract_risk_score": 4, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 64, "stage_label_before": "Stage2-Watch / policy proxy attention", "raw_component_scores_after": {"policy_or_regulatory_score": 8, "valuation_repricing_score": 6, "relative_strength_score": 4, "contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "customer_quality_score": 0, "execution_risk_score": 14, "legal_or_contract_risk_score": 4, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 49, "stage_label_after": "Stage4B-local-watch / no positive Stage2", "changed_components": ["policy_or_regulatory_score", "valuation_repricing_score", "relative_strength_score", "execution_risk_score"], "component_delta_explanation": "Downgrade generic policy headline/proxy momentum because no direct reserves, project participation, offtake, margin, or earnings bridge is visible.", "MFE_90D_pct": 22.18, "MAE_90D_pct": -28.65, "score_return_alignment_label": "high_or_moderate_MFE_but_bridge_absent_and_MAE_drawdown_expand", "current_profile_verdict": "Gas-distribution proxy MFE can be large after an oil/gas policy headline, but it is not a reserve-development cash-flow bridge. C31 should mark local 4B-watch when MAE widens and no direct participation/offtake/margin evidence appears."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R11", "loop": 72, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "EAST_SEA_OIL_GAS_EXPLORATION_POLICY_PROXY_BLOWOFF_VS_EXECUTION_BRIDGE_ABSENCE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 1, "positive_case_count": 0, "counterexample_count": 3, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 0, "evidence_url_pending_count": 0, "current_profile_error_count": 3, "diversity_score_summary": "+3 underused C31 symbols, +1 policy-resource proxy trigger family, +3 price-only policy proxy blowoff/local-4B counterexamples, no hard duplicate", "residual_contribution_label": "canonical_archetype_rule_candidate"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R11", "loop": 72, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "axis": "east_sea_oil_gas_exploration_policy_proxy_blowoff_vs_execution_bridge_absence", "decision": "candidate_observe_more", "proposed_runtime_effect": "C31 should cap policy-resource proxy scores unless the policy event creates a named execution bridge: confirmed reserve, project participation, offtake, drilling contractor exposure, tariff/budget cash-flow, or direct earnings bridge. If proxy MFE appears without that bridge and MAE/post-peak drawdown expands, route to local 4B-watch, not durable Stage2/Green.", "do_not_propose_new_weight_delta": false, "needs_more_evidence": true, "source_repair_required": []}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R11", "loop": 72, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "existing_axis_strengthened": ["price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "local_4b_watch_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C31 energy-resource policy headlines can create strong proxy MFE, but without confirmed reserves, direct participation, offtake, tariff/budget, or company-level cash-flow bridge they should not become Stage2/Green. The right label is local 4B-watch after the proxy peak, while full 4B still requires non-price deterioration."}
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
024060:
  corporate_action_candidate_dates = 1997-09-11, 1998-04-08, 1998-08-24, 2008-08-26, 2008-10-06, 2008-10-24
  selected window = 2024-06-04~D+180
  contamination = false

128820:
  corporate_action_candidate_dates = 2011-05-23, 2013-07-18, 2013-07-30, 2013-10-01, 2015-01-08, 2015-03-04, 2017-08-25
  selected window = 2024-06-04~D+180
  contamination = false

053050:
  corporate_action_candidate_dates = 2005-05-27, 2010-06-16
  selected window = 2024-06-04~D+180
  contamination = false
```

Data-quality caveat:

```text
The policy event source is non-proxy Reuters evidence.
The company-level execution/cash-flow bridge is intentionally absent or weak.
Therefore these rows are counterexample/local-4B guardrail rows, not positive weight rows.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.

Candidate axis:
east_sea_oil_gas_exploration_policy_proxy_blowoff_vs_execution_bridge_absence

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Do not raise generic C31 policy/resource weight from proxy MFE.
4. Keep Stage2 positive only when:
   - confirmed reserve/drilling result exists,
   - named company participation exists,
   - offtake, tariff, budget, subsidy, or project cash-flow bridge exists,
   - or direct earnings/margin bridge is visible.
5. Consider local 4B-watch when:
   - policy-resource headline creates MFE,
   - bridge evidence is absent,
   - MAE_90D or MAE_180D widens,
   - post-peak drawdown exceeds roughly 35%.
6. Do not convert local 4B-watch into full 4B/4C without non-price deterioration evidence.
7. Emit before/after diagnostics and reject if C31 starts classifying generic policy proxies as Green.
```

---

## Final round state

```text
completed_round = R11
completed_loop = 72
next_round = R12
next_loop = 72
round_schedule_status = valid
round_sector_consistency = pass
```

