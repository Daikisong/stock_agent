# E2R Stock-Web v12 Residual Research — R12 Loop 80 / L10 / C31

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R12",
  "scheduled_loop": 80,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R12",
  "completed_loop": 80,
  "computed_next_round": "R13",
  "computed_next_loop": 80,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "fine_archetype_id": "AI_DIGITAL_TEXTBOOK_EDTECH_DIRECT_BENEFICIARY_BRIDGE_VS_EDUCATION_POLICY_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "policy_event_bridge_guardrail",
    "4B_non_price_requirement_stress_test",
    "education_policy_AI_digital_textbook_direct_beneficiary_mapping",
    "edtech_policy_theme_beta_boundary",
    "under_covered_service_sector_expansion",
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

Previous completed state in this interactive run: R11 / loop 80.

Therefore:

```text
scheduled_round = R12
scheduled_loop = 80
allowed_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC or relevant under-covered service/agri sector
selected_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
selected_canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
computed_next_round = R13
computed_next_loop = 80
```

R12 was routed to C31 because this is an under-covered education-service policy event bridge guardrail, not a normal consumer, platform or healthcare round.

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

This run uses three education-service symbols outside that top-covered set:

```text
289010 / 아이스크림에듀 / AI digital textbook policy direct-beneficiary lifecycle
095720 / 웅진씽크빅 / AI education policy theme fade
057030 / YBM넷 / online education / language-learning policy theme fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
No selected row has a profile-level 2024 corporate-action candidate inside the selected window.
```

## Research thesis

C31 is not “정책 테마가 올랐다.”

For education / AI digital textbook rows, the bridge must pass through:

```text
policy / curriculum / digital-textbook event
→ direct beneficiary mapping
→ school adoption or procurement timing
→ paid conversion or subscription revenue
→ margin bridge
→ durable rerating
```

정책 headline은 교실 문에 붙은 공지다.  
C31이 보려는 것은 그 공지가 실제 채택, 과금 전환, 반복 매출, 마진으로 교실 안까지 들어오는지다.

---

## Case 1 — Policy lifecycle candidate: 289010 / 아이스크림에듀

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is AI digital textbook policy, school adoption, paid conversion, subscription/recurring revenue and margin bridge evidence.

```text
evidence_family = AI_DIGITAL_TEXTBOOK_EDTECH_POLICY_SCHOOL_ADOPTION_SUBSCRIPTION_REVENUE_MARGIN_BRIDGE_CANDIDATE
case_role = policy_lifecycle_positive_with_later_high_MAE_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 4,085
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/289/289010/2024.csv`:

```text
2024-02-01,4085,4130,4015,4045
2024-02-06,4145,4695,3860,3890
2024-02-29,4525,5580,4460,4905
2024-05-07,3680,4025,3650,3700
2024-06-24,3300,3300,3195,3255
2024-08-05,2930,2930,2385,2530
2024-09-24,2490,3060,2475,2805
2024-10-30,2390,2395,2310,2310
```

### Backtest

```text
MFE_30D  = +36.60%
MAE_30D  = -9.55%
MFE_90D  = +36.60%
MAE_90D  = -21.79%
MFE_180D = +36.60%
MAE_180D = -43.45%
peak_180 = 5,580 on 2024-02-29
trough_180 = 2,310 on 2024-10-30
peak_to_later_drawdown = -58.60%
```

### Interpretation

This is a policy lifecycle candidate, not durable Green.  
The initial MFE was tradable, but the later high-MAE path means direct adoption and margin evidence must refresh.

Correct treatment:

```text
verified AI textbook policy / school adoption / paid conversion / margin bridge → Stage2-Yellow possible
bridge stale after peak → local 4B-watch
```

---

## Case 2 — Counterexample / local 4B: 095720 / 웅진씽크빅

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests AI education/digital textbook policy beta without enough direct school adoption, paid conversion and revenue bridge.

```text
evidence_family = AI_EDTECH_DIGITAL_TEXTBOOK_POLICY_THEME_WITH_WEAK_DIRECT_SCHOOL_ADOPTION_REVENUE_MARGIN_BRIDGE
case_role = counterexample_edtech_policy_theme_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 2,475
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/095/095720/2024.csv`:

```text
2024-02-01,2475,2510,2460,2500
2024-02-21,2530,2780,2495,2525
2024-03-06,2370,2395,2320,2325
2024-04-15,2140,2170,2090,approx_from_stock_web_row
2024-08-05,1822,1845,1641,1708
2024-09-24,1717,2080,1702,1866
2024-10-11,1856,2190,1834,2040
```

### Backtest

```text
MFE_30D  = +12.32%
MAE_30D  = -6.26%
MFE_90D  = +12.32%
MAE_90D  = -15.56%
MFE_180D = +12.32%
MAE_180D = -33.70%
peak_180 = 2,780 on 2024-02-21
trough_180 = 1,641 on 2024-08-05
peak_to_later_drawdown = -40.97%
```

### Interpretation

This is a C31 policy-theme false-positive boundary.  
The AI education policy headline did not validate durable adoption or revenue rerating.

Correct treatment:

```text
AI education / digital textbook theme beta
→ no verified direct adoption / paid conversion / margin bridge
→ local 4B-watch
```

---

## Case 3 — Counterexample / local 4B: 057030 / YBM넷

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests online education / language-learning policy beta without enough paid conversion, institutional demand and margin bridge.

```text
evidence_family = ONLINE_EDUCATION_AI_LANGUAGE_LEARNING_POLICY_THEME_WITH_WEAK_PAID_CONVERSION_REVENUE_MARGIN_BRIDGE
case_role = counterexample_online_education_policy_theme_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 4,680
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/057/057030/2024.csv`:

```text
2024-02-01,4680,4680,4500,4580
2024-02-29,4525,5580,4460,4905
2024-03-15,4360,4410,4260,4285
2024-04-16,4150,4950,4070,4100
2024-06-24,3620,3700,3540,3540
2024-08-05,3445,3530,2960,3100
2024-09-24,3345,4370,3340,4135
2024-10-25,3685,4005,3500,3505
```

### Backtest

```text
MFE_30D  = +19.23%
MAE_30D  = -8.97%
MFE_90D  = +19.23%
MAE_90D  = -24.89%
MFE_180D = +19.23%
MAE_180D = -36.75%
peak_180 = 5,580 on 2024-02-29
trough_180 = 2,960 on 2024-08-05
peak_to_later_drawdown = -46.95%
```

### Interpretation

This is a C31 online-education policy-theme fade row.  
The initial MFE did not become durable paid-conversion or institutional-demand economics.

Correct treatment:

```text
online education / AI language-learning policy beta
→ no verified paid conversion / institutional demand / margin bridge
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
full_4b_requires_non_price_evidence = keep
```

### What this does not justify

```text
do_not_raise_generic_C31_education_policy_theme_weight = true
do_not_treat_AI_textbook_policy_headline_as_Green_without_direct_revenue_bridge = true
do_not_convert_policy_theme_drawdown_to_hard_4C_without_non_price_policy_reversal_adoption_failure_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
AI_DIGITAL_TEXTBOOK_EDUTECH_DIRECT_BENEFICIARY_BRIDGE_VS_EDUCATION_POLICY_THEME_FADE
```

This fine archetype covers:

```text
1. AI digital textbook direct-beneficiary candidate → policy lifecycle Stage2-Yellow only after source repair
2. broad AI edtech policy beta without adoption/revenue bridge → false Stage2 / local 4B
3. online education / language-learning policy beta without paid conversion → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R12L80-C31-289010-ICECREAM-EDU-AI-DIGITAL-TEXTBOOK-LIFECYCLE", "symbol": "289010", "company_name": "아이스크림에듀", "round": "R12", "loop": "80", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "AI_DIGITAL_TEXTBOOK_EDTECH_DIRECT_BENEFICIARY_BRIDGE_VS_EDUCATION_POLICY_THEME_FADE", "case_type": "policy_subsidy_legislation_event_education_service", "positive_or_counterexample": "policy_lifecycle_positive", "best_trigger": "PolicyLifecycle-AIDigitalTextbookDirectBeneficiaryBridgeWithLocal4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C31 should allow under-covered education-policy rows only when AI digital textbook policy maps to direct school/customer adoption, paid conversion, subscription revenue and margin bridge. Icecream Edu produced tradable MFE but later high MAE, so it is a lifecycle candidate only after source repair.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy AI digital textbook / education policy event, direct beneficiary mapping, adoption/procurement, paid conversion, revenue and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R12L80-C31-095720-WOONGJIN-THINKBIG-EDTECH-POLICY-FADE", "symbol": "095720", "company_name": "웅진씽크빅", "round": "R12", "loop": "80", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "AI_DIGITAL_TEXTBOOK_EDTECH_DIRECT_BENEFICIARY_BRIDGE_VS_EDUCATION_POLICY_THEME_FADE", "case_type": "policy_subsidy_legislation_event_education_service", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / AIEducationPolicyThemeFadeWithLocal4BWatch", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C31 should not treat education/AI textbook policy beta as durable Stage2 unless direct beneficiary mapping, procurement timing, paid user conversion, revenue and margin bridge are visible. Woongjin Thinkbig had a small policy MFE and then a deep MAE path.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy AI digital textbook / education policy event, direct beneficiary mapping, adoption/procurement, paid conversion, revenue and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R12L80-C31-057030-YBMNET-ONLINE-EDUCATION-POLICY-FADE", "symbol": "057030", "company_name": "YBM넷", "round": "R12", "loop": "80", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "AI_DIGITAL_TEXTBOOK_EDTECH_DIRECT_BENEFICIARY_BRIDGE_VS_EDUCATION_POLICY_THEME_FADE", "case_type": "policy_subsidy_legislation_event_education_service", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / OnlineEducationPolicyThemeFadeWithLocal4BWatch", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C31 should not treat online education or language-learning policy beta as durable Stage2 unless paid conversion, institutional demand, subscription revenue and margin bridge are visible. YBM Net produced a tradable MFE but then a high-MAE fade.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy AI digital textbook / education policy event, direct beneficiary mapping, adoption/procurement, paid conversion, revenue and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R12L80-C31-289010-ICECREAM-EDU-AI-DIGITAL-TEXTBOOK-LIFECYCLE", "case_id": "R12L80-C31-289010-ICECREAM-EDU-AI-DIGITAL-TEXTBOOK-LIFECYCLE", "symbol": "289010", "company_name": "아이스크림에듀", "round": "R12", "loop": "80", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "AI_DIGITAL_TEXTBOOK_EDTECH_DIRECT_BENEFICIARY_BRIDGE_VS_EDUCATION_POLICY_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|policy_event_bridge_guardrail|undercovered_service_sector", "trigger_type": "PolicyLifecycle-AIDigitalTextbookDirectBeneficiaryBridgeWithLocal4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 4085.0, "evidence_available_at_that_date": "AI_DIGITAL_TEXTBOOK_EDTECH_POLICY_SCHOOL_ADOPTION_SUBSCRIPTION_REVENUE_MARGIN_BRIDGE_CANDIDATE", "evidence_source": "source_proxy_manual_verification_required:ICECREAM_EDU_2024_AI_DIGITAL_TEXTBOOK_POLICY_SCHOOL_ADOPTION_SUBSCRIPTION_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["policy_or_AI_textbook_event", "direct_beneficiary_mapping_candidate", "adoption_paid_conversion_revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "procurement_or_subscription_visibility_candidate"], "stage4b_evidence_fields": ["policy_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/289/289010/2024.csv", "profile_path": "atlas/symbol_profiles/289/289010.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 36.6, "MFE_90D_pct": 36.6, "MFE_180D_pct": 36.6, "MAE_30D_pct": -9.55, "MAE_90D_pct": -21.79, "MAE_180D_pct": -43.45, "peak_date": "2024-02-29", "peak_price": 5580.0, "drawdown_after_peak_pct": -58.6, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_education_policy_peak_if_direct_adoption_paid_conversion_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_policy_reversal_procurement_failure_adoption_collapse_revenue_or_margin_break", "trigger_outcome_label": "policy_lifecycle_positive_with_later_high_MAE_4b_watch", "current_profile_verdict": "C31 should allow under-covered education-policy rows only when AI digital textbook policy maps to direct school/customer adoption, paid conversion, subscription revenue and margin bridge. Icecream Edu produced tradable MFE but later high MAE, so it is a lifecycle candidate only after source repair.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C31_EDUCATION_POLICY_289010_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R12L80-C31-095720-WOONGJIN-THINKBIG-EDTECH-POLICY-FADE", "case_id": "R12L80-C31-095720-WOONGJIN-THINKBIG-EDTECH-POLICY-FADE", "symbol": "095720", "company_name": "웅진씽크빅", "round": "R12", "loop": "80", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "AI_DIGITAL_TEXTBOOK_EDTECH_DIRECT_BENEFICIARY_BRIDGE_VS_EDUCATION_POLICY_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|policy_event_bridge_guardrail|undercovered_service_sector", "trigger_type": "Stage2-FalsePositive / AIEducationPolicyThemeFadeWithLocal4BWatch", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 2475.0, "evidence_available_at_that_date": "AI_EDTECH_DIGITAL_TEXTBOOK_POLICY_THEME_WITH_WEAK_DIRECT_SCHOOL_ADOPTION_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:WOONGJIN_THINKBIG_2024_AI_EDTECH_DIGITAL_TEXTBOOK_SCHOOL_ADOPTION_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["policy_or_AI_textbook_event", "direct_beneficiary_mapping_candidate", "adoption_paid_conversion_revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "procurement_or_subscription_visibility_candidate"], "stage4b_evidence_fields": ["policy_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/095/095720/2024.csv", "profile_path": "atlas/symbol_profiles/095/095720.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 12.32, "MFE_90D_pct": 12.32, "MFE_180D_pct": 12.32, "MAE_30D_pct": -6.26, "MAE_90D_pct": -15.56, "MAE_180D_pct": -33.7, "peak_date": "2024-02-21", "peak_price": 2780.0, "drawdown_after_peak_pct": -40.97, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_education_policy_peak_if_direct_adoption_paid_conversion_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_policy_reversal_procurement_failure_adoption_collapse_revenue_or_margin_break", "trigger_outcome_label": "counterexample_edtech_policy_theme_local4b", "current_profile_verdict": "C31 should not treat education/AI textbook policy beta as durable Stage2 unless direct beneficiary mapping, procurement timing, paid user conversion, revenue and margin bridge are visible. Woongjin Thinkbig had a small policy MFE and then a deep MAE path.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C31_EDUCATION_POLICY_095720_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R12L80-C31-057030-YBMNET-ONLINE-EDUCATION-POLICY-FADE", "case_id": "R12L80-C31-057030-YBMNET-ONLINE-EDUCATION-POLICY-FADE", "symbol": "057030", "company_name": "YBM넷", "round": "R12", "loop": "80", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "AI_DIGITAL_TEXTBOOK_EDTECH_DIRECT_BENEFICIARY_BRIDGE_VS_EDUCATION_POLICY_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|policy_event_bridge_guardrail|undercovered_service_sector", "trigger_type": "Stage2-FalsePositive / OnlineEducationPolicyThemeFadeWithLocal4BWatch", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 4680.0, "evidence_available_at_that_date": "ONLINE_EDUCATION_AI_LANGUAGE_LEARNING_POLICY_THEME_WITH_WEAK_PAID_CONVERSION_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:YBMNET_2024_ONLINE_EDUCATION_AI_LANGUAGE_LEARNING_POLICY_PAID_CONVERSION_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["policy_or_AI_textbook_event", "direct_beneficiary_mapping_candidate", "adoption_paid_conversion_revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "procurement_or_subscription_visibility_candidate"], "stage4b_evidence_fields": ["policy_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/057/057030/2024.csv", "profile_path": "atlas/symbol_profiles/057/057030.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 19.23, "MFE_90D_pct": 19.23, "MFE_180D_pct": 19.23, "MAE_30D_pct": -8.97, "MAE_90D_pct": -24.89, "MAE_180D_pct": -36.75, "peak_date": "2024-02-29", "peak_price": 5580.0, "drawdown_after_peak_pct": -46.95, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_education_policy_peak_if_direct_adoption_paid_conversion_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_policy_reversal_procurement_failure_adoption_collapse_revenue_or_margin_break", "trigger_outcome_label": "counterexample_online_education_policy_theme_local4b", "current_profile_verdict": "C31 should not treat online education or language-learning policy beta as durable Stage2 unless paid conversion, institutional demand, subscription revenue and margin bridge are visible. YBM Net produced a tradable MFE but then a high-MAE fade.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C31_EDUCATION_POLICY_057030_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L80-C31-289010-ICECREAM-EDU-AI-DIGITAL-TEXTBOOK-LIFECYCLE", "trigger_id": "TRG_R12L80-C31-289010-ICECREAM-EDU-AI-DIGITAL-TEXTBOOK-LIFECYCLE", "symbol": "289010", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"policy_event_score": 13, "direct_beneficiary_mapping_score": 13, "adoption_procurement_score": 12, "paid_conversion_score": 11, "revenue_margin_bridge_score": 12, "relative_strength_score": 10, "execution_risk_score": 12, "source_confidence_score": 2}, "weighted_score_before": 72, "stage_label_before": "Policy lifecycle candidate after source repair", "raw_component_scores_after": {"policy_event_score": 9, "direct_beneficiary_mapping_score": 15, "adoption_procurement_score": 14, "paid_conversion_score": 13, "revenue_margin_bridge_score": 14, "relative_strength_score": 9, "execution_risk_score": 13, "source_confidence_score": 2}, "weighted_score_after": 78, "stage_label_after": "Policy lifecycle Stage2-Yellow after source repair + local 4B", "changed_components": ["policy_event_score", "direct_beneficiary_mapping_score", "adoption_procurement_score", "paid_conversion_score", "revenue_margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Cap policy-event score unless AI digital textbook/education policy maps to direct beneficiary economics, school adoption/procurement, paid conversion, recurring revenue and margin bridge.", "MFE_90D_pct": 36.6, "MAE_90D_pct": -21.79, "score_return_alignment_label": "education_policy_lifecycle_with_later_4b", "current_profile_verdict": "C31 should allow under-covered education-policy rows only when AI digital textbook policy maps to direct school/customer adoption, paid conversion, subscription revenue and margin bridge. Icecream Edu produced tradable MFE but later high MAE, so it is a lifecycle candidate only after source repair."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L80-C31-095720-WOONGJIN-THINKBIG-EDTECH-POLICY-FADE", "trigger_id": "TRG_R12L80-C31-095720-WOONGJIN-THINKBIG-EDTECH-POLICY-FADE", "symbol": "095720", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"policy_event_score": 13, "direct_beneficiary_mapping_score": 5, "adoption_procurement_score": 3, "paid_conversion_score": 2, "revenue_margin_bridge_score": 2, "relative_strength_score": 5, "execution_risk_score": 23, "source_confidence_score": 2}, "weighted_score_before": 44, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"policy_event_score": 9, "direct_beneficiary_mapping_score": 2, "adoption_procurement_score": 1, "paid_conversion_score": 1, "revenue_margin_bridge_score": 1, "relative_strength_score": 3, "execution_risk_score": 25, "source_confidence_score": 2}, "weighted_score_after": 32, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["policy_event_score", "direct_beneficiary_mapping_score", "adoption_procurement_score", "paid_conversion_score", "revenue_margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Cap policy-event score unless AI digital textbook/education policy maps to direct beneficiary economics, school adoption/procurement, paid conversion, recurring revenue and margin bridge.", "MFE_90D_pct": 12.32, "MAE_90D_pct": -15.56, "score_return_alignment_label": "education_policy_theme_false_positive_direct_economics_gap", "current_profile_verdict": "C31 should not treat education/AI textbook policy beta as durable Stage2 unless direct beneficiary mapping, procurement timing, paid user conversion, revenue and margin bridge are visible. Woongjin Thinkbig had a small policy MFE and then a deep MAE path."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L80-C31-057030-YBMNET-ONLINE-EDUCATION-POLICY-FADE", "trigger_id": "TRG_R12L80-C31-057030-YBMNET-ONLINE-EDUCATION-POLICY-FADE", "symbol": "057030", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"policy_event_score": 13, "direct_beneficiary_mapping_score": 5, "adoption_procurement_score": 3, "paid_conversion_score": 2, "revenue_margin_bridge_score": 2, "relative_strength_score": 5, "execution_risk_score": 23, "source_confidence_score": 2}, "weighted_score_before": 44, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"policy_event_score": 9, "direct_beneficiary_mapping_score": 2, "adoption_procurement_score": 1, "paid_conversion_score": 1, "revenue_margin_bridge_score": 1, "relative_strength_score": 3, "execution_risk_score": 25, "source_confidence_score": 2}, "weighted_score_after": 32, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["policy_event_score", "direct_beneficiary_mapping_score", "adoption_procurement_score", "paid_conversion_score", "revenue_margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Cap policy-event score unless AI digital textbook/education policy maps to direct beneficiary economics, school adoption/procurement, paid conversion, recurring revenue and margin bridge.", "MFE_90D_pct": 19.23, "MAE_90D_pct": -24.89, "score_return_alignment_label": "education_policy_theme_false_positive_direct_economics_gap", "current_profile_verdict": "C31 should not treat online education or language-learning policy beta as durable Stage2 unless paid conversion, institutional demand, subscription revenue and margin bridge are visible. YBM Net produced a tradable MFE but then a high-MAE fade."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R12", "loop": 80, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "AI_DIGITAL_TEXTBOOK_EDTECH_DIRECT_BENEFICIARY_BRIDGE_VS_EDUCATION_POLICY_THEME_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "current_profile_error_count": 1, "diversity_score_summary": "+3 underused C31 education-service policy symbols outside top-covered 112610/034020/336260/036460 set, +3 AI textbook/edtech/online education trigger families, +1 policy lifecycle MFE candidate, +2 education-policy local-4B counterexamples, no hard duplicate", "residual_contribution_label": "policy_event_bridge_guardrail_with_undercovered_service_sector_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R12", "loop": 80, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "axis": "AI_digital_textbook_edtech_direct_beneficiary_bridge_vs_education_policy_theme_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C31 should split education-policy direct-beneficiary lifecycle trades from generic edtech/AI education theme beta. Stage2 requires explicit policy event plus direct beneficiary mapping, school adoption/procurement timing, paid conversion, subscription/recurring revenue and margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["289010", "095720", "057030"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R12", "loop": 80, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "existing_axis_strengthened": ["price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "stage2_required_bridge", "direct_beneficiary_mapping_required", "undercovered_service_policy_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C31 education-policy events need direct-beneficiary proof. Icecream Edu shows a tradable AI digital textbook policy MFE candidate after source repair; Woongjin Thinkbig and YBM Net show education/AI policy theme beta fading into local 4B when adoption, paid conversion, revenue and margin bridge are absent or stale."}
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
289010:
  name = 아이스크림에듀
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false

095720:
  name = 웅진씽크빅
  corporate_action_candidate_dates = 2019-01-31, 2019-04-08
  selected window = 2024-02-01~D+180
  contamination = false

057030:
  name = YBM넷 from 2019-12-03, 와이비엠넷 / YBM시사닷컴 / 시사닷컴 before that
  corporate_action_candidate_dates = 2005-04-21, 2010-01-25
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C31 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C31 education-service policy rule-shape discovery,
but coding-agent promotion requires non-proxy AI digital textbook / education policy evidence, direct beneficiary mapping, school adoption, paid conversion, revenue and margin bridge evidence.
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
AI_digital_textbook_edtech_direct_beneficiary_bridge_vs_education_policy_theme_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 289010, 095720 and 057030.
4. Keep generic C31 policy-event weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - education / AI digital textbook policy event is explicit,
   - direct beneficiary mapping is visible,
   - school adoption or procurement timing is visible,
   - paid conversion or subscription revenue bridge exists,
   - margin bridge is credible,
   - MAE remains controlled or the signal is lifecycle-managed.
6. Consider local 4B-watch when:
   - the trigger is education/AI policy theme beta only,
   - direct beneficiary / adoption / paid conversion / revenue / margin bridge is absent or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
7. Do not convert local 4B-watch into full 4B/4C without non-price policy reversal, procurement failure, adoption collapse, revenue deterioration or margin break evidence.
8. Emit before/after diagnostics and reject if verified direct-beneficiary education-policy positives are overblocked.
```

---

## Final round state

```text
completed_round = R12
completed_loop = 80
next_round = R13
next_loop = 80
round_schedule_status = valid
round_sector_consistency = pass
```

