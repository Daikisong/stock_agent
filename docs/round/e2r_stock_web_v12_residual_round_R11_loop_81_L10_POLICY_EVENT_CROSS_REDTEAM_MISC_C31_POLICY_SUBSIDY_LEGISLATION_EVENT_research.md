# E2R Stock-Web v12 Residual Research — R11 Loop 81 / L10 / C31

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R11",
  "scheduled_loop": 81,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R11",
  "completed_loop": 81,
  "computed_next_round": "R12",
  "computed_next_loop": 81,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "fine_archetype_id": "LOW_BIRTH_RATE_CHILDCARE_POLICY_DIRECT_BENEFICIARY_REVENUE_MARGIN_BRIDGE_VS_BABYCARE_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "policy_event_bridge_guardrail",
    "4B_non_price_requirement_stress_test",
    "low_birth_rate_childcare_policy_direct_beneficiary_mapping",
    "babycare_policy_theme_beta_boundary",
    "under_covered_service_consumer_policy_expansion",
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

Previous completed state in this interactive run: R10 / loop 81.

Therefore:

```text
scheduled_round = R11
scheduled_loop = 81
allowed_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC or L1_INDUSTRIALS_INFRA_DEFENSE_GRID depending on policy-defense linkage
selected_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
selected_canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
computed_next_round = R12
computed_next_loop = 81
```

R11 was routed to C31 because this run focuses on a policy/subsidy/legislation event guardrail rather than governance tender-cap mechanics.  
This file deliberately avoids loop-80 R11 C32 tender-cap rows and loop-80 R12 education-policy names.

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

This run uses three different low-birth / childcare policy symbols:

```text
013990 / 아가방컴퍼니 / childcare policy direct-beneficiary lifecycle
159580 / 제로투세븐 / childcare policy theme fade
407400 / 꿈비 / babycare policy theme fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
No selected row has a profile-level 2024 corporate-action candidate inside the selected window.
```

## Research thesis

C31 is not “정책 테마가 올랐다.”

For low-birth / childcare rows, the bridge must pass through:

```text
policy / subsidy / childcare-support headline
→ direct beneficiary mapping
→ channel demand or sell-through
→ product revenue conversion
→ margin bridge
→ durable rerating
```

정책 headline은 유모차 위의 풍선이다.  
C31이 보려는 것은 풍선이 아니라 실제 매장 판매, 반복 수요, 매출, 마진이라는 바퀴가 굴러가는지다.

---

## Case 1 — Policy lifecycle candidate: 013990 / 아가방컴퍼니

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is low-birth / childcare policy, baby-product demand, channel sell-through, revenue conversion and margin bridge evidence.

```text
evidence_family = LOW_BIRTH_RATE_CHILDCARE_POLICY_BABY_PRODUCTS_DIRECT_BENEFICIARY_REVENUE_MARGIN_BRIDGE_CANDIDATE
case_role = policy_lifecycle_positive_with_later_high_MAE_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 5,200
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/013/013990/2024.csv`:

```text
2024-02-01,5200,5310,5070,5160
2024-02-14,5350,6170,5320,5790
2024-02-29,6090,6940,6090,6450
2024-04-08,4805,4815,4675,4740
2024-07-25,4315,4840,4210,4370
2024-08-05,3990,4065,3400,3455
2024-08-28,4500,4690,4390,4655
2024-10-31,4470,4520,4315,4495
```

### Backtest

```text
MFE_30D  = +33.46%
MAE_30D  = -3.08%
MFE_90D  = +33.46%
MAE_90D  = -10.10%
MFE_180D = +33.46%
MAE_180D = -34.62%
peak_180 = 6,940 on 2024-02-29
trough_180 = 3,400 on 2024-08-05
peak_to_later_drawdown = -51.01%
```

### Interpretation

This is a C31 policy lifecycle candidate, not durable Green.  
The MFE was tradable, but the later high-MAE path means product demand and margin evidence must refresh.

Correct treatment:

```text
verified low-birth policy / direct beneficiary / sell-through / margin bridge → Stage2-Yellow possible
bridge stale after peak → local 4B-watch
```

---

## Case 2 — Counterexample / local 4B: 159580 / 제로투세븐

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests childcare policy beta without enough direct revenue and margin bridge.

```text
evidence_family = LOW_BIRTH_RATE_CHILDCARE_POLICY_THEME_WITH_WEAK_DIRECT_REVENUE_MARGIN_BRIDGE
case_role = counterexample_childcare_policy_theme_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 6,670
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/159/159580/2024.csv`:

```text
2024-02-01,6670,6730,6480,6500
2024-02-14,6810,7400,6810,7140
2024-02-29,6750,7140,6700,6930
2024-04-11,5400,5800,5330,5590
2024-07-24,4910,5100,4910,5100
2024-08-05,4625,4760,3820,4035
2024-09-09,3820,4015,3805,4015
2024-10-25,4170,4210,4125,4130
```

### Backtest

```text
MFE_30D  = +10.94%
MAE_30D  = -2.85%
MFE_90D  = +10.94%
MAE_90D  = -20.09%
MFE_180D = +10.94%
MAE_180D = -42.95%
peak_180 = 7,400 on 2024-02-14
trough_180 = 3,805 on 2024-09-09
peak_to_later_drawdown = -48.58%
```

### Interpretation

This is a C31 policy-theme false-positive boundary.  
The childcare headline did not validate durable sell-through or margin economics.

Correct treatment:

```text
childcare / low-birth-rate policy beta
→ no verified direct beneficiary / product demand / margin bridge
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

This row tests babycare policy beta without enough customer demand, channel sell-through and margin bridge.

```text
evidence_family = BABYCARE_CHILDCARE_POLICY_THEME_WITH_WEAK_PRODUCT_DEMAND_REVENUE_MARGIN_BRIDGE
case_role = counterexample_babycare_policy_theme_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 10,070
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/407/407400/2024.csv`:

```text
2024-02-01,10070,10190,9740,9980
2024-02-08,10980,11200,10610,10810
2024-02-14,10700,11200,10640,10980
2024-03-20,9290,10960,9290,10150
2024-04-11,8110,8370,7940,8350
2024-08-05,7340,7490,5880,6070
2024-08-29,8200,8900,7110,7130
2024-10-25,6030,6050,5800,5820
```

### Backtest

```text
MFE_30D  = +11.22%
MAE_30D  = -11.02%
MFE_90D  = +11.22%
MAE_90D  = -21.15%
MFE_180D = +11.22%
MAE_180D = -42.40%
peak_180 = 11,200 on 2024-02-08~2024-02-14
trough_180 = 5,800 on 2024-10-25
peak_to_later_drawdown = -48.21%
```

### Interpretation

This is a C31 babycare policy-theme fade row.  
The early MFE was modest and did not become durable direct-beneficiary economics.

Correct treatment:

```text
babycare / childcare policy beta
→ no verified product demand / channel sell-through / margin bridge
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
undercovered_consumer_policy_guard = strengthen
full_4b_requires_non_price_evidence = keep
```

### What this does not justify

```text
do_not_raise_generic_C31_childcare_policy_theme_weight = true
do_not_treat_low_birth_policy_headline_as_Green_without_direct_revenue_bridge = true
do_not_convert_policy_theme_drawdown_to_hard_4C_without_non_price_policy_reversal_demand_failure_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
LOW_BIRTH_RATE_CHILDCARE_POLICY_DIRECT_BENEFICIARY_REVENUE_MARGIN_BRIDGE_VS_BABYCARE_THEME_FADE
```

This fine archetype covers:

```text
1. childcare policy direct-beneficiary candidate → policy lifecycle Stage2-Yellow only after source repair
2. childcare policy beta without sell-through/revenue bridge → false Stage2 / local 4B
3. babycare policy beta without product-demand margin bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R11L81-C31-013990-AGABANG-LOWBIRTH-CHILDCARE-POLICY-LIFECYCLE", "symbol": "013990", "company_name": "아가방컴퍼니", "round": "R11", "loop": "81", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "LOW_BIRTH_RATE_CHILDCARE_POLICY_DIRECT_BENEFICIARY_REVENUE_MARGIN_BRIDGE_VS_BABYCARE_THEME_FADE", "case_type": "policy_subsidy_legislation_event_childcare_consumer", "positive_or_counterexample": "policy_lifecycle_positive", "best_trigger": "PolicyLifecycle-LowBirthChildcareDirectBeneficiaryRevenueBridgeWithLocal4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C31 should allow low-birth/childcare policy positives only when policy attention maps to direct beneficiary demand, baby-product sales, channel sell-through, revenue conversion and margin bridge. Agabang Company produced tradable MFE but later high MAE, so it is lifecycle-managed rather than durable Green.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy low-birth-rate / childcare policy, direct beneficiary mapping, product demand, channel sell-through, revenue conversion and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R11L81-C31-159580-ZERO2SEVEN-CHILDCARE-POLICY-THEME-FADE", "symbol": "159580", "company_name": "제로투세븐", "round": "R11", "loop": "81", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "LOW_BIRTH_RATE_CHILDCARE_POLICY_DIRECT_BENEFICIARY_REVENUE_MARGIN_BRIDGE_VS_BABYCARE_THEME_FADE", "case_type": "policy_subsidy_legislation_event_childcare_consumer", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / ChildcarePolicyThemeFadeWithLocal4BWatch", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C31 should not treat childcare/low-birth-rate policy beta as durable Stage2 unless direct beneficiary mapping, channel demand, paid conversion, product sell-through, revenue and margin bridge are visible. Zero to Seven had small policy MFE and then a severe MAE path.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy low-birth-rate / childcare policy, direct beneficiary mapping, product demand, channel sell-through, revenue conversion and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R11L81-C31-407400-GGUMBI-CHILDCARE-POLICY-THEME-FADE", "symbol": "407400", "company_name": "꿈비", "round": "R11", "loop": "81", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "LOW_BIRTH_RATE_CHILDCARE_POLICY_DIRECT_BENEFICIARY_REVENUE_MARGIN_BRIDGE_VS_BABYCARE_THEME_FADE", "case_type": "policy_subsidy_legislation_event_childcare_consumer", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / BabycarePolicyThemeFadeWithLocal4BWatch", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C31 should not treat babycare/childcare policy beta as durable Stage2 unless direct beneficiary policy, customer demand, channel sell-through, product revenue and margin bridge are visible. Ggumbi produced a modest MFE but then a high-MAE drawdown.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy low-birth-rate / childcare policy, direct beneficiary mapping, product demand, channel sell-through, revenue conversion and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R11L81-C31-013990-AGABANG-LOWBIRTH-CHILDCARE-POLICY-LIFECYCLE", "case_id": "R11L81-C31-013990-AGABANG-LOWBIRTH-CHILDCARE-POLICY-LIFECYCLE", "symbol": "013990", "company_name": "아가방컴퍼니", "round": "R11", "loop": "81", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "LOW_BIRTH_RATE_CHILDCARE_POLICY_DIRECT_BENEFICIARY_REVENUE_MARGIN_BRIDGE_VS_BABYCARE_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|policy_event_bridge_guardrail|undercovered_consumer_policy_axis", "trigger_type": "PolicyLifecycle-LowBirthChildcareDirectBeneficiaryRevenueBridgeWithLocal4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 5200.0, "evidence_available_at_that_date": "LOW_BIRTH_RATE_CHILDCARE_POLICY_BABY_PRODUCTS_DIRECT_BENEFICIARY_REVENUE_MARGIN_BRIDGE_CANDIDATE", "evidence_source": "source_proxy_manual_verification_required:AGABANG_2024_LOW_BIRTH_CHILDCARE_POLICY_BABY_PRODUCT_DEMAND_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["policy_event_candidate", "direct_beneficiary_mapping_candidate", "sellthrough_revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "channel_or_product_demand_candidate"], "stage4b_evidence_fields": ["policy_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/013/013990/2024.csv", "profile_path": "atlas/symbol_profiles/013/013990.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 33.46, "MFE_90D_pct": 33.46, "MFE_180D_pct": 33.46, "MAE_30D_pct": -3.08, "MAE_90D_pct": -10.1, "MAE_180D_pct": -34.62, "peak_date": "2024-02-29", "peak_price": 6940.0, "drawdown_after_peak_pct": -51.01, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_childcare_policy_peak_if_direct_beneficiary_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_policy_reversal_adoption_failure_channel_demand_revenue_or_margin_break", "trigger_outcome_label": "policy_lifecycle_positive_with_later_high_MAE_4b_watch", "current_profile_verdict": "C31 should allow low-birth/childcare policy positives only when policy attention maps to direct beneficiary demand, baby-product sales, channel sell-through, revenue conversion and margin bridge. Agabang Company produced tradable MFE but later high MAE, so it is lifecycle-managed rather than durable Green.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C31_CHILDCARE_POLICY_013990_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R11L81-C31-159580-ZERO2SEVEN-CHILDCARE-POLICY-THEME-FADE", "case_id": "R11L81-C31-159580-ZERO2SEVEN-CHILDCARE-POLICY-THEME-FADE", "symbol": "159580", "company_name": "제로투세븐", "round": "R11", "loop": "81", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "LOW_BIRTH_RATE_CHILDCARE_POLICY_DIRECT_BENEFICIARY_REVENUE_MARGIN_BRIDGE_VS_BABYCARE_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|policy_event_bridge_guardrail|undercovered_consumer_policy_axis", "trigger_type": "Stage2-FalsePositive / ChildcarePolicyThemeFadeWithLocal4BWatch", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 6670.0, "evidence_available_at_that_date": "LOW_BIRTH_RATE_CHILDCARE_POLICY_THEME_WITH_WEAK_DIRECT_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:ZERO_TO_SEVEN_2024_CHILDCARE_POLICY_DIRECT_BENEFICIARY_SELLTHROUGH_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["policy_event_candidate", "direct_beneficiary_mapping_candidate", "sellthrough_revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "channel_or_product_demand_candidate"], "stage4b_evidence_fields": ["policy_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/159/159580/2024.csv", "profile_path": "atlas/symbol_profiles/159/159580.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 10.94, "MFE_90D_pct": 10.94, "MFE_180D_pct": 10.94, "MAE_30D_pct": -2.85, "MAE_90D_pct": -20.09, "MAE_180D_pct": -42.95, "peak_date": "2024-02-14", "peak_price": 7400.0, "drawdown_after_peak_pct": -48.58, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_childcare_policy_peak_if_direct_beneficiary_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_policy_reversal_adoption_failure_channel_demand_revenue_or_margin_break", "trigger_outcome_label": "counterexample_childcare_policy_theme_local4b", "current_profile_verdict": "C31 should not treat childcare/low-birth-rate policy beta as durable Stage2 unless direct beneficiary mapping, channel demand, paid conversion, product sell-through, revenue and margin bridge are visible. Zero to Seven had small policy MFE and then a severe MAE path.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C31_CHILDCARE_POLICY_159580_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R11L81-C31-407400-GGUMBI-CHILDCARE-POLICY-THEME-FADE", "case_id": "R11L81-C31-407400-GGUMBI-CHILDCARE-POLICY-THEME-FADE", "symbol": "407400", "company_name": "꿈비", "round": "R11", "loop": "81", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "LOW_BIRTH_RATE_CHILDCARE_POLICY_DIRECT_BENEFICIARY_REVENUE_MARGIN_BRIDGE_VS_BABYCARE_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|policy_event_bridge_guardrail|undercovered_consumer_policy_axis", "trigger_type": "Stage2-FalsePositive / BabycarePolicyThemeFadeWithLocal4BWatch", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 10070.0, "evidence_available_at_that_date": "BABYCARE_CHILDCARE_POLICY_THEME_WITH_WEAK_PRODUCT_DEMAND_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:GGUMBI_2024_BABYCARE_CHILDCARE_POLICY_PRODUCT_DEMAND_CHANNEL_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["policy_event_candidate", "direct_beneficiary_mapping_candidate", "sellthrough_revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "channel_or_product_demand_candidate"], "stage4b_evidence_fields": ["policy_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/407/407400/2024.csv", "profile_path": "atlas/symbol_profiles/407/407400.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 11.22, "MFE_90D_pct": 11.22, "MFE_180D_pct": 11.22, "MAE_30D_pct": -11.02, "MAE_90D_pct": -21.15, "MAE_180D_pct": -42.4, "peak_date": "2024-02-08~2024-02-14", "peak_price": 11200.0, "drawdown_after_peak_pct": -48.21, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_childcare_policy_peak_if_direct_beneficiary_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_policy_reversal_adoption_failure_channel_demand_revenue_or_margin_break", "trigger_outcome_label": "counterexample_babycare_policy_theme_local4b", "current_profile_verdict": "C31 should not treat babycare/childcare policy beta as durable Stage2 unless direct beneficiary policy, customer demand, channel sell-through, product revenue and margin bridge are visible. Ggumbi produced a modest MFE but then a high-MAE drawdown.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C31_CHILDCARE_POLICY_407400_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L81-C31-013990-AGABANG-LOWBIRTH-CHILDCARE-POLICY-LIFECYCLE", "trigger_id": "TRG_R11L81-C31-013990-AGABANG-LOWBIRTH-CHILDCARE-POLICY-LIFECYCLE", "symbol": "013990", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"policy_event_score": 13, "direct_beneficiary_mapping_score": 13, "channel_demand_score": 12, "product_sellthrough_score": 12, "revenue_margin_bridge_score": 12, "relative_strength_score": 9, "execution_risk_score": 12, "source_confidence_score": 2}, "weighted_score_before": 72, "stage_label_before": "Policy lifecycle candidate after source repair", "raw_component_scores_after": {"policy_event_score": 9, "direct_beneficiary_mapping_score": 15, "channel_demand_score": 14, "product_sellthrough_score": 14, "revenue_margin_bridge_score": 14, "relative_strength_score": 8, "execution_risk_score": 13, "source_confidence_score": 2}, "weighted_score_after": 78, "stage_label_after": "Policy lifecycle Stage2-Yellow after source repair + local 4B", "changed_components": ["policy_event_score", "direct_beneficiary_mapping_score", "channel_demand_score", "product_sellthrough_score", "revenue_margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Cap policy-event score unless low-birth/childcare policy maps to direct beneficiary economics, channel demand, product sell-through, recurring revenue and margin bridge.", "MFE_90D_pct": 33.46, "MAE_90D_pct": -10.1, "score_return_alignment_label": "childcare_policy_lifecycle_with_later_4b", "current_profile_verdict": "C31 should allow low-birth/childcare policy positives only when policy attention maps to direct beneficiary demand, baby-product sales, channel sell-through, revenue conversion and margin bridge. Agabang Company produced tradable MFE but later high MAE, so it is lifecycle-managed rather than durable Green."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L81-C31-159580-ZERO2SEVEN-CHILDCARE-POLICY-THEME-FADE", "trigger_id": "TRG_R11L81-C31-159580-ZERO2SEVEN-CHILDCARE-POLICY-THEME-FADE", "symbol": "159580", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"policy_event_score": 13, "direct_beneficiary_mapping_score": 5, "channel_demand_score": 3, "product_sellthrough_score": 2, "revenue_margin_bridge_score": 1, "relative_strength_score": 4, "execution_risk_score": 24, "source_confidence_score": 2}, "weighted_score_before": 42, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"policy_event_score": 9, "direct_beneficiary_mapping_score": 2, "channel_demand_score": 1, "product_sellthrough_score": 1, "revenue_margin_bridge_score": 1, "relative_strength_score": 3, "execution_risk_score": 26, "source_confidence_score": 2}, "weighted_score_after": 31, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["policy_event_score", "direct_beneficiary_mapping_score", "channel_demand_score", "product_sellthrough_score", "revenue_margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Cap policy-event score unless low-birth/childcare policy maps to direct beneficiary economics, channel demand, product sell-through, recurring revenue and margin bridge.", "MFE_90D_pct": 10.94, "MAE_90D_pct": -20.09, "score_return_alignment_label": "childcare_policy_theme_false_positive_direct_economics_gap", "current_profile_verdict": "C31 should not treat childcare/low-birth-rate policy beta as durable Stage2 unless direct beneficiary mapping, channel demand, paid conversion, product sell-through, revenue and margin bridge are visible. Zero to Seven had small policy MFE and then a severe MAE path."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L81-C31-407400-GGUMBI-CHILDCARE-POLICY-THEME-FADE", "trigger_id": "TRG_R11L81-C31-407400-GGUMBI-CHILDCARE-POLICY-THEME-FADE", "symbol": "407400", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"policy_event_score": 13, "direct_beneficiary_mapping_score": 5, "channel_demand_score": 3, "product_sellthrough_score": 2, "revenue_margin_bridge_score": 1, "relative_strength_score": 4, "execution_risk_score": 24, "source_confidence_score": 2}, "weighted_score_before": 42, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"policy_event_score": 9, "direct_beneficiary_mapping_score": 2, "channel_demand_score": 1, "product_sellthrough_score": 1, "revenue_margin_bridge_score": 1, "relative_strength_score": 3, "execution_risk_score": 26, "source_confidence_score": 2}, "weighted_score_after": 31, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["policy_event_score", "direct_beneficiary_mapping_score", "channel_demand_score", "product_sellthrough_score", "revenue_margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Cap policy-event score unless low-birth/childcare policy maps to direct beneficiary economics, channel demand, product sell-through, recurring revenue and margin bridge.", "MFE_90D_pct": 11.22, "MAE_90D_pct": -21.15, "score_return_alignment_label": "childcare_policy_theme_false_positive_direct_economics_gap", "current_profile_verdict": "C31 should not treat babycare/childcare policy beta as durable Stage2 unless direct beneficiary policy, customer demand, channel sell-through, product revenue and margin bridge are visible. Ggumbi produced a modest MFE but then a high-MAE drawdown."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R11", "loop": 81, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "LOW_BIRTH_RATE_CHILDCARE_POLICY_DIRECT_BENEFICIARY_REVENUE_MARGIN_BRIDGE_VS_BABYCARE_THEME_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "current_profile_error_count": 1, "diversity_score_summary": "+3 C31 low-birth/childcare policy symbols outside top-covered 112610/034020/336260/036460 set and outside loop-80 education-policy names, +3 baby-products/childcare/babycare trigger families, +1 policy lifecycle MFE candidate, +2 childcare policy local-4B counterexamples, no hard duplicate", "residual_contribution_label": "policy_event_bridge_guardrail_with_undercovered_childcare_consumer_policy_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R11", "loop": 81, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "axis": "low_birth_rate_childcare_policy_direct_beneficiary_revenue_margin_bridge_vs_babycare_theme_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C31 should split low-birth/childcare policy direct-beneficiary lifecycle trades from generic babycare policy theme beta. Stage2 requires explicit policy event plus direct beneficiary mapping, channel demand, product sell-through, revenue conversion and margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["013990", "159580", "407400"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R11", "loop": 81, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "existing_axis_strengthened": ["price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "stage2_required_bridge", "direct_beneficiary_mapping_required", "undercovered_consumer_policy_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C31 low-birth/childcare policy events need direct-beneficiary proof. Agabang Company shows a tradable policy lifecycle candidate after source repair; Zero to Seven and Ggumbi show childcare/babycare policy beta fading into local 4B when product demand, sell-through, revenue and margin bridge are absent or stale."}
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
  name = 아가방컴퍼니 from 2007-04-23, 아가방 before that
  corporate_action_candidate_dates = 2008-05-16
  selected window = 2024-02-01~D+180
  contamination = false

159580:
  name = 제로투세븐
  corporate_action_candidate_dates = 2018-11-13
  selected window = 2024-02-01~D+180
  contamination = false

407400:
  name = 꿈비
  corporate_action_candidate_dates = 2023-07-19
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C31 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C31 childcare-policy rule-shape discovery,
but coding-agent promotion requires non-proxy low-birth-rate / childcare policy evidence, direct beneficiary mapping, product demand, channel sell-through, revenue conversion and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R11/C31 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair.

Candidate axis:
low_birth_rate_childcare_policy_direct_beneficiary_revenue_margin_bridge_vs_babycare_theme_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 013990, 159580 and 407400.
4. Keep generic C31 policy-event weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - low-birth / childcare policy event is explicit,
   - direct beneficiary mapping is visible,
   - channel demand or product sell-through is visible,
   - revenue conversion and margin bridge exist,
   - MAE remains controlled or the signal is lifecycle-managed.
6. Consider local 4B-watch when:
   - the trigger is childcare/babycare policy theme beta only,
   - direct beneficiary / product demand / revenue / margin bridge is absent or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
7. Do not convert local 4B-watch into full 4B/4C without non-price policy reversal, demand failure, channel breakdown, revenue deterioration or margin break evidence.
8. Emit before/after diagnostics and reject if verified direct-beneficiary childcare-policy positives are overblocked.
```

---

## Final round state

```text
completed_round = R11
completed_loop = 81
next_round = R12
next_loop = 81
round_schedule_status = valid
round_sector_consistency = pass
```

