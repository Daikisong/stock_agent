# E2R Stock-Web v12 Residual Research — R8 Loop 79 / L8 / C28

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R8",
  "scheduled_loop": 79,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R8",
  "completed_loop": 79,
  "computed_next_round": "R9",
  "computed_next_loop": 79,
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
  "fine_archetype_id": "AUTO_SW_SECURITY_CONTRACT_RETENTION_RECURRING_REVENUE_BRIDGE_VS_SECURITY_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "software_security_contract_retention_guardrail",
    "auto_SW_security_contract_retention_recurring_revenue_bridge",
    "security_theme_beta_fade_boundary",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression",
    "source_repair_queue_creation",
    "corporate_action_validation_queue_creation"
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

Previous completed state in this interactive run: R7 / loop 79.

Therefore:

```text
scheduled_round = R8
scheduled_loop = 79
allowed_large_sector = L8_PLATFORM_CONTENT_SW_SECURITY
selected_large_sector = L8_PLATFORM_CONTENT_SW_SECURITY
selected_canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
computed_next_round = R9
computed_next_loop = 79
```

R8 was routed to C28 because loop 78 used C27.  
This file tests software/security contract retention and recurring-revenue bridge rather than game/content IP or platform ad revenue.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C28 concentration in:

```text
012510, 053800, 263860, 131370, 030520
```

This run uses three different symbols:

```text
307950 / 현대오토에버 / auto-SW and SI contract-retention bridge
136540 / 윈스테크넷 / security maintenance / enterprise renewal bridge
192250 / 케이사인 / security/encryption theme fade with post-window CA caveat
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
192250 has a 2024-11-01 corporate-action candidate outside the selected 180D interpretation; extended-window ingestion must validate it.
```

## Research thesis

C28 is not “보안/SW 테마가 올랐다.”

The mechanism must pass through:

```text
software / security demand
→ contract retention or renewal
→ customer quality and project backlog
→ recurring maintenance / subscription / service revenue
→ margin bridge
→ durable rerating
```

소프트웨어 매출은 한 번 찍힌 주문서가 아니라 갱신되는 열쇠다.  
C28이 보려는 것은 그 열쇠가 매년 다시 돌아오고, 유지보수·구독·프로젝트 마진으로 잠금장치를 계속 여는지다.

---

## Case 1 — Slow positive: 307950 / 현대오토에버

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is auto software/SI contract retention, captive/customer quality, project backlog, recurring maintenance and margin bridge evidence.

```text
evidence_family = AUTO_SOFTWARE_SI_ERP_CONNECTEDCAR_CONTRACT_RETENTION_RECURRING_REVENUE_MARGIN_BRIDGE
case_role = positive_slow_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 150,000
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/307/307950/2024.csv`:

```text
2024-02-01,150000,155400,149100,151300
2024-04-30,170000,173500,154000,154000
2024-06-18,157500,163000,156600,161700
2024-07-11,177600,181900,175000,175000
2024-08-05,151100,154000,139700,144500
2024-10-31,139000,139000,134700,135100
2024-11-01,134100,134800,131000,131100
```

### Backtest

```text
MFE_30D  = +7.93%
MAE_30D  = -3.67%
MFE_90D  = +15.67%
MAE_90D  = -10.93%
MFE_180D = +21.27%
MAE_180D = -10.20%
peak_180 = 181,900 on 2024-07-11
trough_180 = 134,700 on 2024-10-31
peak_to_later_drawdown = -25.95%
```

### Interpretation

This is a slow C28 positive.  
The price path is not explosive, but it can support Stage2-Yellow after source repair because entry-basis MAE was not thesis-breaking.

Correct treatment:

```text
verified contract retention / recurring maintenance / project backlog / margin bridge → Stage2-Yellow possible
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 2 — Defensive security positive: 136540 / 윈스테크넷

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is network-security maintenance renewal, public/enterprise customer retention, recurring revenue and margin bridge evidence.

```text
evidence_family = NETWORK_SECURITY_MAINTENANCE_CONTRACT_RENEWAL_PUBLIC_ENTERPRISE_CUSTOMER_RECURRING_REVENUE_MARGIN_BRIDGE
case_role = positive_defensive_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 12,950
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/136/136540/2024.csv`:

```text
2024-02-01,12950,13090,12800,12990
2024-02-16,12840,13150,12830,13090
2024-07-24,14350,14450,14250,14370
2024-08-05,12820,12940,12000,12400
2024-10-31,12400,12500,12360,12500
2024-11-05,15530,15750,14770,15120
2024-11-07,14990,15140,14930,15050
```

### Backtest

```text
MFE_30D  = +3.01%
MAE_30D  = -1.00%
MFE_90D  = +13.59%
MAE_90D  = -3.63%
MFE_180D = +12.90%
MAE_180D = -7.34%
peak_180 = 14,620 on 2024-07-29
trough_180 = 12,000 on 2024-08-05
peak_to_later_drawdown = -17.92%
```

### Interpretation

This is a defensive C28 candidate, not a blowoff.  
It still needs non-price proof of contract renewal and recurring revenue.

Correct treatment:

```text
verified security maintenance renewal / enterprise retention / recurring revenue bridge → Stage2-Yellow possible
no bridge → RiskWatch only
```

---

## Case 3 — Counterexample / local 4B: 192250 / 케이사인

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
post_window_corporate_action_validation_required = true
source_repair_required = true
```

This row tests security/encryption/authentication theme beta without enough contract retention and recurring-revenue bridge.

```text
evidence_family = SECURITY_ENCRYPTION_AUTH_THEME_WITH_WEAK_CONTRACT_RETENTION_RECURRING_REVENUE_MARGIN_BRIDGE
case_role = counterexample_security_theme_local4b_with_post_window_CA_caveat
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 1,300
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/192/192250/2024.csv`:

```text
2024-02-01,1300,1308,1289,1303
2024-02-23,1400,1400,1312,1312
2024-03-26,1241,1614,1241,1614
2024-03-27,1721,1736,1487,1487
2024-04-08,1332,1423,1290,1290
2024-08-05,1032,1041,860,902
2024-10-11,955,966,954,957
```

### Backtest

```text
MFE_30D  = +7.69%
MAE_30D  = -1.85%
MFE_90D  = +33.54%
MAE_90D  = -4.69%
MFE_180D = +33.54%
MAE_180D = -33.85%
peak_180 = 1,736 on 2024-03-27
trough_180 = 860 on 2024-08-05
peak_to_later_drawdown = -50.46%
```

### Interpretation

This is the C28 security-theme false-positive row.  
The MFE was sharp, but it did not become durable contract-retention rerating.

Correct treatment:

```text
security/encryption theme beta
→ no verified retention / recurring revenue / margin bridge
→ local 4B-watch
```

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
contract_retention_required_bridge = strengthen
post_corporate_action_validation_guard = strengthen
full_4b_requires_non_price_evidence = keep
```

### What this does not justify

```text
do_not_raise_generic_C28_SW_security_theme_weight = true
do_not_treat_all_SW_security_MFE_as_Green = true
do_not_ingest_post_window_CA_caveat_rows_without_validation = true
do_not_convert_SW_security_drawdown_to_hard_4C_without_non_price_contract_churn_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
AUTO_SW_SECURITY_CONTRACT_RETENTION_RECURRING_REVENUE_BRIDGE_VS_SECURITY_THEME_FADE
```

This fine archetype covers:

```text
1. auto-SW/SI contract retention + recurring revenue bridge → Stage2-Yellow possible after source repair
2. defensive network-security maintenance renewal bridge → Stage2-Yellow possible, lifecycle-managed
3. security/encryption theme beta without recurring revenue bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R8L79-C28-307950-HYUNDAI-AUTOEVER-AUTO-SW-CONTRACT-RETENTION", "symbol": "307950", "company_name": "현대오토에버", "round": "R8", "loop": "79", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "AUTO_SW_SECURITY_CONTRACT_RETENTION_RECURRING_REVENUE_BRIDGE_VS_SECURITY_THEME_FADE", "case_type": "software_security_contract_retention", "positive_or_counterexample": "positive", "best_trigger": "Stage2-SlowPositive-AutoSWContractRetentionRevenueBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C28 should preserve software/SI positives when contract retention, captive/customer quality, recurring maintenance, project backlog, revenue recognition and margin bridge are visible. Hyundai AutoEver produced a slow MFE with moderate MAE; it should not be overblocked after source repair, but lifecycle 4B is needed if contract/revenue/margin evidence fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy contract retention, renewal rate, customer quality, recurring revenue, project backlog and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R8L79-C28-136540-WINS-SECURITY-CONTRACT-RETENTION-DEFENSIVE", "symbol": "136540", "company_name": "윈스테크넷", "round": "R8", "loop": "79", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "AUTO_SW_SECURITY_CONTRACT_RETENTION_RECURRING_REVENUE_BRIDGE_VS_SECURITY_THEME_FADE", "case_type": "software_security_contract_retention", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Yellow-SecurityContractRetentionDefensiveBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C28 should allow defensive security software positives when maintenance renewal, public/enterprise customer retention, recurring revenue and margin bridge are visible. Wins had bounded entry-basis MAE and later recovery MFE; it is Stage2-Yellow only after source repair, not a security theme blowoff.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy contract retention, renewal rate, customer quality, recurring revenue, project backlog and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R8L79-C28-192250-KSIGN-SECURITY-THEME-LOCAL4B-CA-CAVEAT", "symbol": "192250", "company_name": "케이사인", "round": "R8", "loop": "79", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "AUTO_SW_SECURITY_CONTRACT_RETENTION_RECURRING_REVENUE_BRIDGE_VS_SECURITY_THEME_FADE", "case_type": "software_security_contract_retention", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / SecurityThemeContractRetentionFadeWithPostWindowCACaveat", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C28 should not treat security/encryption/authentication theme MFE as durable Stage2 unless contract retention, renewal rate, recurring revenue, public/enterprise customer quality and margin bridge are visible. KSign produced a sharp MFE and then high MAE; 2024-11-01 corporate-action candidate is outside the selected 180D interpretation but must be validated before any extended ingestion.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy contract retention, renewal rate, customer quality, recurring revenue, project backlog and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R8L79-C28-307950-HYUNDAI-AUTOEVER-AUTO-SW-CONTRACT-RETENTION", "case_id": "R8L79-C28-307950-HYUNDAI-AUTOEVER-AUTO-SW-CONTRACT-RETENTION", "symbol": "307950", "company_name": "현대오토에버", "round": "R8", "loop": "79", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "AUTO_SW_SECURITY_CONTRACT_RETENTION_RECURRING_REVENUE_BRIDGE_VS_SECURITY_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|software_security_contract_retention_guardrail", "trigger_type": "Stage2-SlowPositive-AutoSWContractRetentionRevenueBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 150000.0, "evidence_available_at_that_date": "AUTO_SOFTWARE_SI_ERP_CONNECTEDCAR_CONTRACT_RETENTION_RECURRING_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:HYUNDAI_AUTOEVER_2024_AUTO_SW_SI_CONTRACT_RETENTION_RECURRING_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["contract_retention_or_renewal_candidate", "customer_quality_or_project_backlog_candidate", "recurring_revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "maintenance_subscription_or_public_enterprise_customer_candidate"], "stage4b_evidence_fields": ["software_security_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/307/307950/2024.csv", "profile_path": "atlas/symbol_profiles/307/307950.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 7.93, "MFE_90D_pct": 15.67, "MFE_180D_pct": 21.27, "MAE_30D_pct": -2.0, "MAE_90D_pct": -10.93, "MAE_180D_pct": -12.67, "peak_date": "2024-07-11", "peak_price": 181900.0, "drawdown_after_peak_pct": -27.98, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_SW_security_peak_if_contract_retention_recurring_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_contract_churn_customer_loss_subscription_collapse_margin_or_financing_break", "trigger_outcome_label": "positive_slow_with_later_4b_watch", "current_profile_verdict": "C28 should preserve software/SI positives when contract retention, captive/customer quality, recurring maintenance, project backlog, revenue recognition and margin bridge are visible. Hyundai AutoEver produced a slow MFE with moderate MAE; it should not be overblocked after source repair, but lifecycle 4B is needed if contract/revenue/margin evidence fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_post_window_caveat", "share_count_change_inside_window": false, "same_entry_group_id": "C28_SW_SECURITY_307950_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R8L79-C28-136540-WINS-SECURITY-CONTRACT-RETENTION-DEFENSIVE", "case_id": "R8L79-C28-136540-WINS-SECURITY-CONTRACT-RETENTION-DEFENSIVE", "symbol": "136540", "company_name": "윈스테크넷", "round": "R8", "loop": "79", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "AUTO_SW_SECURITY_CONTRACT_RETENTION_RECURRING_REVENUE_BRIDGE_VS_SECURITY_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|software_security_contract_retention_guardrail", "trigger_type": "Stage2-Yellow-SecurityContractRetentionDefensiveBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 12950.0, "evidence_available_at_that_date": "NETWORK_SECURITY_MAINTENANCE_CONTRACT_RENEWAL_PUBLIC_ENTERPRISE_CUSTOMER_RECURRING_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:WINS_2024_SECURITY_CONTRACT_RENEWAL_PUBLIC_ENTERPRISE_RECURRING_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["contract_retention_or_renewal_candidate", "customer_quality_or_project_backlog_candidate", "recurring_revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "maintenance_subscription_or_public_enterprise_customer_candidate"], "stage4b_evidence_fields": ["software_security_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/136/136540/2024.csv", "profile_path": "atlas/symbol_profiles/136/136540.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.01, "MFE_90D_pct": 13.59, "MFE_180D_pct": 21.62, "MAE_30D_pct": -1.0, "MAE_90D_pct": -3.63, "MAE_180D_pct": -7.34, "peak_date": "2024-11-05", "peak_price": 15750.0, "drawdown_after_peak_pct": -4.38, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_SW_security_peak_if_contract_retention_recurring_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_contract_churn_customer_loss_subscription_collapse_margin_or_financing_break", "trigger_outcome_label": "positive_defensive_with_later_4b_watch", "current_profile_verdict": "C28 should allow defensive security software positives when maintenance renewal, public/enterprise customer retention, recurring revenue and margin bridge are visible. Wins had bounded entry-basis MAE and later recovery MFE; it is Stage2-Yellow only after source repair, not a security theme blowoff.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_post_window_caveat", "share_count_change_inside_window": false, "same_entry_group_id": "C28_SW_SECURITY_136540_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R8L79-C28-192250-KSIGN-SECURITY-THEME-LOCAL4B-CA-CAVEAT", "case_id": "R8L79-C28-192250-KSIGN-SECURITY-THEME-LOCAL4B-CA-CAVEAT", "symbol": "192250", "company_name": "케이사인", "round": "R8", "loop": "79", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "AUTO_SW_SECURITY_CONTRACT_RETENTION_RECURRING_REVENUE_BRIDGE_VS_SECURITY_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|software_security_contract_retention_guardrail", "trigger_type": "Stage2-FalsePositive / SecurityThemeContractRetentionFadeWithPostWindowCACaveat", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 1300.0, "evidence_available_at_that_date": "SECURITY_ENCRYPTION_AUTH_THEME_WITH_WEAK_CONTRACT_RETENTION_RECURRING_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:KSIGN_2024_SECURITY_ENCRYPTION_CONTRACT_RETENTION_RECURRING_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["contract_retention_or_renewal_candidate", "customer_quality_or_project_backlog_candidate", "recurring_revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "maintenance_subscription_or_public_enterprise_customer_candidate"], "stage4b_evidence_fields": ["software_security_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/192/192250/2024.csv", "profile_path": "atlas/symbol_profiles/192/192250.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 7.69, "MFE_90D_pct": 33.54, "MFE_180D_pct": 33.54, "MAE_30D_pct": -1.85, "MAE_90D_pct": -4.69, "MAE_180D_pct": -33.85, "peak_date": "2024-03-27", "peak_price": 1736.0, "drawdown_after_peak_pct": -50.46, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_SW_security_peak_if_contract_retention_recurring_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_contract_churn_customer_loss_subscription_collapse_margin_or_financing_break", "trigger_outcome_label": "counterexample_security_theme_local4b_with_post_window_CA_caveat", "current_profile_verdict": "C28 should not treat security/encryption/authentication theme MFE as durable Stage2 unless contract retention, renewal rate, recurring revenue, public/enterprise customer quality and margin bridge are visible. KSign produced a sharp MFE and then high MAE; 2024-11-01 corporate-action candidate is outside the selected 180D interpretation but must be validated before any extended ingestion.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_post_window_caveat", "share_count_change_inside_window": false, "same_entry_group_id": "C28_SW_SECURITY_192250_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L79-C28-307950-HYUNDAI-AUTOEVER-AUTO-SW-CONTRACT-RETENTION", "trigger_id": "TRG_R8L79-C28-307950-HYUNDAI-AUTOEVER-AUTO-SW-CONTRACT-RETENTION", "symbol": "307950", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "raw_component_scores_before": {"contract_retention_score": 14, "customer_quality_score": 13, "recurring_revenue_score": 13, "project_backlog_or_maintenance_score": 12, "margin_bridge_score": 13, "relative_strength_score": 8, "execution_risk_score": 10, "corporate_action_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_before": 76, "stage_label_before": "Stage2/Yellow candidate after source repair", "raw_component_scores_after": {"contract_retention_score": 16, "customer_quality_score": 15, "recurring_revenue_score": 15, "project_backlog_or_maintenance_score": 14, "margin_bridge_score": 15, "relative_strength_score": 7, "execution_risk_score": 11, "corporate_action_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_after": 82, "stage_label_after": "Stage2/Yellow after source repair + lifecycle 4B", "changed_components": ["contract_retention_score", "customer_quality_score", "recurring_revenue_score", "project_backlog_or_maintenance_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified contract retention, renewal/customer quality, recurring revenue, backlog/maintenance and margin bridge; cap software/security theme beta when bridge fails to refresh.", "MFE_90D_pct": 15.67, "MAE_90D_pct": -10.93, "score_return_alignment_label": "SW_security_contract_retention_positive_with_lifecycle_4b", "current_profile_verdict": "C28 should preserve software/SI positives when contract retention, captive/customer quality, recurring maintenance, project backlog, revenue recognition and margin bridge are visible. Hyundai AutoEver produced a slow MFE with moderate MAE; it should not be overblocked after source repair, but lifecycle 4B is needed if contract/revenue/margin evidence fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L79-C28-136540-WINS-SECURITY-CONTRACT-RETENTION-DEFENSIVE", "trigger_id": "TRG_R8L79-C28-136540-WINS-SECURITY-CONTRACT-RETENTION-DEFENSIVE", "symbol": "136540", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "raw_component_scores_before": {"contract_retention_score": 14, "customer_quality_score": 13, "recurring_revenue_score": 13, "project_backlog_or_maintenance_score": 12, "margin_bridge_score": 13, "relative_strength_score": 8, "execution_risk_score": 10, "corporate_action_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_before": 76, "stage_label_before": "Stage2/Yellow candidate after source repair", "raw_component_scores_after": {"contract_retention_score": 16, "customer_quality_score": 15, "recurring_revenue_score": 15, "project_backlog_or_maintenance_score": 14, "margin_bridge_score": 15, "relative_strength_score": 7, "execution_risk_score": 11, "corporate_action_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_after": 82, "stage_label_after": "Stage2/Yellow after source repair + lifecycle 4B", "changed_components": ["contract_retention_score", "customer_quality_score", "recurring_revenue_score", "project_backlog_or_maintenance_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified contract retention, renewal/customer quality, recurring revenue, backlog/maintenance and margin bridge; cap software/security theme beta when bridge fails to refresh.", "MFE_90D_pct": 13.59, "MAE_90D_pct": -3.63, "score_return_alignment_label": "SW_security_contract_retention_positive_with_lifecycle_4b", "current_profile_verdict": "C28 should allow defensive security software positives when maintenance renewal, public/enterprise customer retention, recurring revenue and margin bridge are visible. Wins had bounded entry-basis MAE and later recovery MFE; it is Stage2-Yellow only after source repair, not a security theme blowoff."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L79-C28-192250-KSIGN-SECURITY-THEME-LOCAL4B-CA-CAVEAT", "trigger_id": "TRG_R8L79-C28-192250-KSIGN-SECURITY-THEME-LOCAL4B-CA-CAVEAT", "symbol": "192250", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "raw_component_scores_before": {"contract_retention_score": 4, "customer_quality_score": 3, "recurring_revenue_score": 2, "project_backlog_or_maintenance_score": 2, "margin_bridge_score": 1, "relative_strength_score": 8, "execution_risk_score": 22, "corporate_action_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_before": 46, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"contract_retention_score": 2, "customer_quality_score": 1, "recurring_revenue_score": 1, "project_backlog_or_maintenance_score": 1, "margin_bridge_score": 1, "relative_strength_score": 3, "execution_risk_score": 24, "corporate_action_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_after": 34, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["contract_retention_score", "customer_quality_score", "recurring_revenue_score", "project_backlog_or_maintenance_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified contract retention, renewal/customer quality, recurring revenue, backlog/maintenance and margin bridge; cap software/security theme beta when bridge fails to refresh.", "MFE_90D_pct": 33.54, "MAE_90D_pct": -4.69, "score_return_alignment_label": "false_positive_security_theme_bridge_gap", "current_profile_verdict": "C28 should not treat security/encryption/authentication theme MFE as durable Stage2 unless contract retention, renewal rate, recurring revenue, public/enterprise customer quality and margin bridge are visible. KSign produced a sharp MFE and then high MAE; 2024-11-01 corporate-action candidate is outside the selected 180D interpretation but must be validated before any extended ingestion."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R8", "loop": 79, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "AUTO_SW_SECURITY_CONTRACT_RETENTION_RECURRING_REVENUE_BRIDGE_VS_SECURITY_THEME_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "post_window_corporate_action_caveat_count": 1, "current_profile_error_count": 1, "diversity_score_summary": "+3 C28 SW/security symbols outside top-covered 012510/053800/263860/131370/030520 set, +3 auto-SW/network-security/encryption-security trigger families, +2 contract-retention positives, +1 security theme local-4B counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_and_post_window_CA_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R8", "loop": 79, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "axis": "auto_SW_security_contract_retention_recurring_revenue_bridge_vs_security_theme_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C28 should split verified software/security contract-retention rerating from generic SW/security theme beta. Stage2 requires contract renewal or retention, customer quality, recurring revenue or maintenance, project backlog and margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch. Post-window corporate-action caveats require validation before extended ingestion.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["307950", "136540", "192250"], "post_window_corporate_action_validation_required": ["192250"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R8", "loop": 79, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "contract_retention_required_bridge", "post_corporate_action_validation_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C28 needs contract retention, renewal, customer quality, recurring revenue and margin proof. Hyundai AutoEver and Wins show software/security contract-retention candidates after source repair; KSign shows security theme MFE fading into local 4B when retention, recurring revenue and margin bridge are absent or stale."}
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
307950:
  name = 현대오토에버
  corporate_action_candidate_dates = 2021-04-14
  selected window = 2024-02-01~D+180
  contamination = false

136540:
  name = 윈스테크넷 / 윈스 name-history ambiguity in profile
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false

192250:
  name = 케이사인 from 2014-11-11
  corporate_action_candidate_dates = 2014-11-11, 2024-11-01
  selected 180D interpretation = 2024-02-01~around 2024-10-25
  contamination = false if stopped before 2024-11-01
  post_window_corporate_action_validation_required = true for extended ingestion
```

Data-quality caveat:

```text
All selected C28 rows are source_proxy_only / evidence_url_pending.
192250 also requires post-window corporate-action validation before extended runtime ingestion.
This MD is useful for stock-web path calibration and C28 rule-shape discovery,
but coding-agent promotion requires non-proxy contract retention, renewal, customer quality, recurring revenue, maintenance/subscription and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R8/C28 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair and 192250 needs post-window corporate-action validation before extended ingestion.

Candidate axis:
auto_SW_security_contract_retention_recurring_revenue_bridge_vs_security_theme_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 307950, 136540 and 192250.
4. Validate 192250 corporate-action handling if any window extends beyond 2024-10-25 / 2024-11-01.
5. Keep generic C28 SW/security contract-retention weight unchanged until source repair is complete.
6. Consider Stage2 only when:
   - contract retention or renewal is explicit,
   - customer quality or project backlog is visible,
   - maintenance / subscription / recurring revenue bridge exists,
   - margin bridge is credible,
   - MAE remains controlled or the signal is lifecycle-managed.
7. Consider local 4B-watch when:
   - the trigger is SW/security theme beta only,
   - retention/recurring-revenue/margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
8. Do not convert local 4B-watch into full 4B/4C without non-price contract churn, customer loss, subscription collapse, financing or margin break.
9. Emit before/after diagnostics and reject if verified contract-retention positives or defensive security rows are overblocked.
```

---

## Final round state

```text
completed_round = R8
completed_loop = 79
next_round = R9
next_loop = 79
round_schedule_status = valid
round_sector_consistency = pass
```

