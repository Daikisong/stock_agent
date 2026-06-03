# E2R Stock-Web v12 Residual Research — R8 Loop 72 / L8 / C28

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R8",
  "scheduled_loop": 72,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R8",
  "completed_loop": 72,
  "computed_next_round": "R9",
  "computed_next_loop": 72,
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
  "fine_archetype_id": "CLOUD_SECURITY_CONTRACT_RETENTION_ARR_BRIDGE_VS_PRICE_ONLY_CLOUD_AI_BETA",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
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

Previous completed state in this interactive run: R7 / loop 72.

Therefore:

```text
scheduled_round = R8
scheduled_loop = 72
allowed_large_sector = L8_PLATFORM_CONTENT_SW_SECURITY
selected_large_sector = L8_PLATFORM_CONTENT_SW_SECURITY
selected_canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
computed_next_round = R9
computed_next_loop = 72
```

R8 was routed to C28 because loop 71 already produced a C27 content/IP file.  
The goal here is to test software/security contract retention rather than platform ad leverage or content launch beta.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat already shows C28 has top-symbol concentration in names such as 012510, 053800, 263860, 131370 and 030520.  
This run avoids those top-covered symbols and adds:

```text
079940 / 가비아 / cloud-hosting AI beta without verified contract retention bridge
136540 / 윈스 / network security maintenance-renewal slow positive
294570 / 쿠콘 / financial data API recurring thesis with weak retention/margin bridge
```

Data-quality note:

```text
All three rows are stock-web calibration usable.
All three rows are marked source_proxy_only=true / evidence_url_pending=true.
This file is a source-repair queue plus stock-web path calibration, not immediate runtime weight evidence.
```

## Research thesis

C28 is not simply “software stock went up.”

The correct mechanism is:

```text
software / security / data API product base
→ renewal, retention, maintenance, ARR, enterprise/public contract evidence
→ recurring revenue visibility
→ margin or cash-flow conversion
→ durable rerating
```

A software name without renewal evidence is like a locked server rack with the fans still spinning.  
There is activity, but not yet proof that customers stayed.

The split is:

```text
C28 positive:
  contract retention / maintenance renewal / ARR or enterprise-security renewal
  + controlled MAE
  + recurring revenue or margin bridge

C28 false positive:
  cloud, AI, data-API or security theme beta
  + no retention/renewal bridge
  + high post-peak drawdown

C28 local 4B:
  large MFE but renewal evidence stale
  or small MFE with severe 180D MAE
```

---

## Case 1 — Counterexample: 079940 / 가비아 / cloud-hosting AI beta

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The row tests whether cloud-hosting / AI / security beta is enough without renewal, ARR, enterprise contract, or margin bridge evidence.

```text
evidence_family = CLOUD_HOSTING_AI_SECURITY_BETA_WITH_WEAK_CONTRACT_RETENTION_ARR_BRIDGE
case_role = counterexample
trigger_date = 2024-02-21
entry_date = 2024-02-22
entry_price = 17,540
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/079/079940/2024.csv`:

```text
2024-02-22,17540,18380,17400,18310
2024-03-14,23100,24350,20100,20200
2024-07-03,14500,14790,14390,14520
2024-08-05,13700,13700,12300,12310
```

### Backtest

```text
MFE_30D  = +38.82%
MAE_30D  = -8.55%
MFE_90D  = +38.82%
MAE_90D  = -17.96%
MFE_180D = +38.82%
MAE_180D = -29.87%
peak_180 = 24,350 on 2024-03-14
trough_180 = 12,300 on 2024-08-05
peak_to_later_drawdown = -49.49%
```

### Interpretation

This is the C28 trap.  
The first move looks like a software rerating, but the later drawdown shows that a theme candle is not a retention model.

The rule candidate:

```text
if cloud/AI/security MFE is high
and no ARR/retention/enterprise contract evidence refresh appears
and post-peak drawdown exceeds roughly 35%
then route to local 4B-watch rather than durable Stage2/Green.
```

---

## Case 2 — Positive after source repair: 136540 / 윈스 / security maintenance-renewal

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests the slow C28 security route: network-security maintenance, public/enterprise renewal, support revenue, and contract retention.

```text
evidence_family = NETWORK_SECURITY_MAINTENANCE_RENEWAL_PUBLIC_ENTERPRISE_CONTRACT_RETENTION
case_role = positive_slow
trigger_date = 2024-04-10
entry_date = 2024-04-11
entry_price = 12,400
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/136/136540/2024.csv`:

```text
2024-04-11,12400,12490,12330,12490
2024-04-16,12150,12170,11930,12100
2024-05-17,13230,13270,13110,13240
2024-06-28,14620,14950,14620,14670
2024-08-05,12820,12940,12000,12400
```

### Backtest

```text
MFE_30D  = +7.02%
MAE_30D  = -3.79%
MFE_90D  = +20.56%
MAE_90D  = -3.79%
MFE_180D = +20.56%
MAE_180D = -3.79%
peak_180 = 14,950 on 2024-06-28
trough_180 = 11,930 on 2024-04-16
peak_to_later_drawdown = -19.73%
```

### Interpretation

This is not an explosive software winner.  
It is the kind of slow, low-MAE path that contract-retention software/security names should have.

The rule should allow a slower Stage2 if non-price evidence confirms:

```text
maintenance renewal
public or enterprise security contract
recurring support revenue
margin conversion
```

---

## Case 3 — Counterexample: 294570 / 쿠콘 / financial data API recurring thesis

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests whether a financial data/API recurring-revenue thesis is enough without retention, renewal, take-rate, or margin conversion.

```text
evidence_family = FINANCIAL_DATA_API_RECURRING_REVENUE_THESIS_WITH_WEAK_RETENTION_AND_MARGIN_BRIDGE
case_role = counterexample
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 22,000
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/294/294570/2024.csv`:

```text
2024-02-01,22000,22500,21100,21300
2024-02-02,21550,22900,21200,21800
2024-06-26,15480,15840,15220,15800
2024-08-05,14510,14510,10180,12690
```

### Backtest

```text
MFE_30D  = +4.09%
MAE_30D  = -15.00%
MFE_90D  = +4.09%
MAE_90D  = -30.82%
MFE_180D = +4.09%
MAE_180D = -53.73%
peak_180 = 22,900 on 2024-02-02
trough_180 = 10,180 on 2024-08-05
peak_to_later_drawdown = -55.55%
```

### Interpretation

This is a hard C28 false-positive shape.  
The idea of recurring data/API revenue is not enough. The model needs proof that contracts retained, renewed, or converted into margin.

For C28, a recurring-revenue label without retention evidence should be capped.

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
do_not_raise_generic_C28_weight = true
do_not_treat_cloud_AI_or_data_API_beta_as_Green = true
do_not_convert_local_4B_software_drawdown_to_hard_4C_without_non_price_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
CLOUD_SECURITY_CONTRACT_RETENTION_ARR_BRIDGE_VS_PRICE_ONLY_CLOUD_AI_BETA
```

This fine archetype covers:

```text
1. cloud/AI/security beta without retention evidence → false Stage2 / local 4B
2. network security maintenance-renewal with controlled MAE → Stage2 possible after source repair
3. financial data API recurring thesis without renewal/margin bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### trigger rows

```jsonl
{"row_type": "trigger", "round": "R8", "loop": 72, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "CLOUD_SECURITY_CONTRACT_RETENTION_ARR_BRIDGE_VS_PRICE_ONLY_CLOUD_AI_BETA", "case_id": "R8L72-C28-079940-GABIA-CLOUD-AI-BETA-CONTRACT-BRIDGE-FAIL", "symbol": "079940", "company": "가비아", "trigger_type": "Stage2-FalsePositive / CloudAIBetaLocal4B", "trigger_date": "2024-02-21", "entry_date": "2024-02-22", "entry_price": 17540.0, "mfe_30_pct": 38.82, "mae_30_pct": -8.55, "mfe_90_pct": 38.82, "mae_90_pct": -17.96, "mfe_180_pct": 38.82, "mae_180_pct": -29.87, "peak_price_180": 24350.0, "peak_date_180": "2024-03-14", "trough_price_180": 12300.0, "trough_date_180": "2024-08-05", "peak_to_later_drawdown_pct": -49.49, "case_role": "counterexample", "calibration_usable": true, "corporate_action_contaminated_180d": false, "evidence_family": "CLOUD_HOSTING_AI_SECURITY_BETA_WITH_WEAK_CONTRACT_RETENTION_ARR_BRIDGE", "evidence_url": "source_proxy_manual_verification_required:GABIA_2024_CLOUD_HOSTING_SECURITY_RECURRING_CONTRACT_RETENTION_ARR_BRIDGE", "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "round": "R8", "loop": 72, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "CLOUD_SECURITY_CONTRACT_RETENTION_ARR_BRIDGE_VS_PRICE_ONLY_CLOUD_AI_BETA", "case_id": "R8L72-C28-136540-WINS-SECURITY-MAINTENANCE-RETENTION-SLOW-POSITIVE", "symbol": "136540", "company": "윈스", "trigger_type": "Stage2-Actionable-SecurityMaintenanceRetention", "trigger_date": "2024-04-10", "entry_date": "2024-04-11", "entry_price": 12400.0, "mfe_30_pct": 7.02, "mae_30_pct": -3.79, "mfe_90_pct": 20.56, "mae_90_pct": -3.79, "mfe_180_pct": 20.56, "mae_180_pct": -3.79, "peak_price_180": 14950.0, "peak_date_180": "2024-06-28", "trough_price_180": 11930.0, "trough_date_180": "2024-04-16", "peak_to_later_drawdown_pct": -19.73, "case_role": "positive_slow", "calibration_usable": true, "corporate_action_contaminated_180d": false, "evidence_family": "NETWORK_SECURITY_MAINTENANCE_RENEWAL_PUBLIC_ENTERPRISE_CONTRACT_RETENTION", "evidence_url": "source_proxy_manual_verification_required:WINS_2024_NETWORK_SECURITY_MAINTENANCE_RENEWAL_PUBLIC_ENTERPRISE_CONTRACT_RETENTION", "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "round": "R8", "loop": 72, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "CLOUD_SECURITY_CONTRACT_RETENTION_ARR_BRIDGE_VS_PRICE_ONLY_CLOUD_AI_BETA", "case_id": "R8L72-C28-294570-COOCON-DATAAPI-PRICEONLY-RETENTION-BRIDGE-FAIL", "symbol": "294570", "company": "쿠콘", "trigger_type": "Stage2-FalsePositive / DataAPIContractRetentionWeak", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 22000.0, "mfe_30_pct": 4.09, "mae_30_pct": -15.0, "mfe_90_pct": 4.09, "mae_90_pct": -30.82, "mfe_180_pct": 4.09, "mae_180_pct": -53.73, "peak_price_180": 22900.0, "peak_date_180": "2024-02-02", "trough_price_180": 10180.0, "trough_date_180": "2024-08-05", "peak_to_later_drawdown_pct": -55.55, "case_role": "counterexample", "calibration_usable": true, "corporate_action_contaminated_180d": false, "evidence_family": "FINANCIAL_DATA_API_RECURRING_REVENUE_THESIS_WITH_WEAK_RETENTION_AND_MARGIN_BRIDGE", "evidence_url": "source_proxy_manual_verification_required:COOCON_2024_FINANCIAL_DATA_API_RECURRING_REVENUE_RETENTION_MARGIN_BRIDGE", "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "case_id": "R8L72-C28-079940-GABIA-CLOUD-AI-BETA-CONTRACT-BRIDGE-FAIL", "symbol": "079940", "baseline_current_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"eps_fcf_explosion": 3, "earnings_visibility": 4, "bottleneck_pricing_power": 4, "market_mispricing": 12, "valuation_rerating": 5, "capital_allocation": 1, "information_confidence": 2}, "diagnostic_flags": ["software_security_contract_retention", "recurring_contract_or_retention_bridge", "price_only_cloud_or_api_beta_weak_bridge", "local_4b_watch", "source_proxy_only"], "expected_current_profile_stage": "Stage2-FalsePositive / local 4B-watch", "profile_stress_result": "C28 should not turn cloud/AI hosting price beta into durable Stage2 unless recurring contract retention, ARR/maintenance renewal, or enterprise security revenue evidence is visible. The price path generated high MFE but later high MAE and deep post-peak drawdown."}
{"row_type": "score_simulation", "case_id": "R8L72-C28-136540-WINS-SECURITY-MAINTENANCE-RETENTION-SLOW-POSITIVE", "symbol": "136540", "baseline_current_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"eps_fcf_explosion": 8, "earnings_visibility": 13, "bottleneck_pricing_power": 4, "market_mispricing": 12, "valuation_rerating": 10, "capital_allocation": 1, "information_confidence": 2}, "diagnostic_flags": ["software_security_contract_retention", "recurring_contract_or_retention_bridge", "bridge_present_after_source_repair", "stage2_candidate_slow", "source_proxy_only"], "expected_current_profile_stage": "Stage2-Actionable after source repair", "profile_stress_result": "C28 should allow a slower Stage2 path when network security maintenance, renewal, public/enterprise contracts, and recurring support revenue are verified. The price path has moderate MFE but very controlled MAE, fitting a retention/maintenance software archetype rather than blowoff."}
{"row_type": "score_simulation", "case_id": "R8L72-C28-294570-COOCON-DATAAPI-PRICEONLY-RETENTION-BRIDGE-FAIL", "symbol": "294570", "baseline_current_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"eps_fcf_explosion": 3, "earnings_visibility": 4, "bottleneck_pricing_power": 4, "market_mispricing": 12, "valuation_rerating": 5, "capital_allocation": 1, "information_confidence": 2}, "diagnostic_flags": ["software_security_contract_retention", "recurring_contract_or_retention_bridge", "price_only_cloud_or_api_beta_weak_bridge", "local_4b_watch", "source_proxy_only"], "expected_current_profile_stage": "Stage2-FalsePositive / local 4B-watch", "profile_stress_result": "Financial data API recurring-revenue thesis should not be treated as C28 Stage2 when retention, renewal, take-rate, or margin conversion evidence is weak. The stock path showed tiny MFE followed by severe 180D MAE."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R8", "loop": 72, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "CLOUD_SECURITY_CONTRACT_RETENTION_ARR_BRIDGE_VS_PRICE_ONLY_CLOUD_AI_BETA", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "four_b_case_count": 2, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "current_profile_error_count": 2, "diversity_score_summary": "+3 underused C28 symbols, +3 software/security retention trigger families, +1 slow retention positive, +2 price-only cloud/API beta counterexamples, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R8", "loop": 72, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "axis": "cloud_security_contract_retention_arr_bridge_vs_price_only_cloud_ai_beta", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C28 should split verified recurring contract/maintenance/ARR retention from price-only cloud, AI, or data-API beta. Stage2 requires renewal, retention, support revenue, ARR, or enterprise/public contract evidence with controlled MAE. Weak bridge and high drawdown should route to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["079940", "136540", "294570"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R8", "loop": 72, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C28 should not be a generic cloud/AI/software beta. The positive route needs renewal, retention, maintenance, ARR or enterprise/security contract evidence. 가비아 and 쿠콘 show how cloud/API beta can fail without bridge refresh, while 윈스 shows a slower but lower-MAE retention-style security path after source repair."}
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
079940:
  corporate_action_candidate_dates = 2006-11-15, 2006-12-15, 2007-12-26, 2008-01-29
  selected window = 2024-02-22~D+180
  contamination = false

136540:
  corporate_action_candidate_dates = none
  selected window = 2024-04-11~D+180
  contamination = false

294570:
  corporate_action_candidate_dates = 2021-12-20
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C28 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and source-repair queue creation,
but coding-agent promotion requires non-proxy company-level evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R8/C28 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair.

Candidate axis:
cloud_security_contract_retention_arr_bridge_vs_price_only_cloud_ai_beta

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 079940, 136540 and 294570.
4. Keep generic C28 weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - renewal, retention, maintenance, ARR, enterprise/public contract evidence is explicit,
   - recurring revenue or margin conversion is visible,
   - MAE remains controlled.
6. Consider local 4B-watch when:
   - the trigger is cloud/AI/security/data-API beta only,
   - MFE is high but bridge evidence fails to refresh,
   - MAE_180D <= -25% or peak-to-later drawdown <= -35%,
   - retention/renewal bridge is weak or stale.
7. Do not convert local 4B-watch into full 4B/4C without non-price deterioration evidence.
8. Emit before/after diagnostics and reject if C28 overblocks verified contract-retention positives.
```

---

## Final round state

```text
completed_round = R8
completed_loop = 72
next_round = R9
next_loop = 72
round_schedule_status = valid
round_sector_consistency = pass
```

