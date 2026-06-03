# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
scheduled_round = R11
scheduled_loop = 75
completed_round = R11
completed_loop = 75
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = COVID19_DIAGNOSTIC_EUA_EXPORT_POLICY_CONVERSION_GUARD
output_file = e2r_stock_web_v12_residual_round_R11_loop_75_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
price_source = Songdaiki/stock-web
stock_web_manifest_max_date = 2026-02-20
round_schedule_status = valid
round_sector_consistency = pass
```

This loop adds 4 new independent cases, 2 counterexamples, and 2 residual errors for R11/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C31_POLICY_SUBSIDY_LEGISLATION_EVENT.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This run does not re-prove the global Stage2/Green/4B rules. It stress-tests a narrower question: when a public-health policy event appears, does it carry an issuer-level conversion belt, or is it only a theme balloon? The balloon can lift quickly, but without a belt to earnings it drifts back into the wind.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R11
scheduled_loop = 75
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = COVID19_DIAGNOSTIC_EUA_EXPORT_POLICY_CONVERSION_GUARD
loop_objective = sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill|4B_non_price_requirement_stress_test
```

R11 is a policy/event checkpoint. The selected canonical archetype is C31 because the trigger family is public-health authorization, emergency response, and policy-driven demand rather than a normal sector earnings cycle.

## 3. Previous Coverage / Duplicate Avoidance Check

Existing local/session R11 loops already covered Value-up policy, nuclear export policy, Poland defense export framework, and low-birth-rate policy themes. This MD uses a new trigger family and new symbols:

```text
new_trigger_family = covid19_diagnostic_eua_export_conversion_vs_mask_theme_beta
new_symbols = 096530 | 084650 | 065950 | 012690
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
new_independent_case_count = 4
reused_case_count = 0
wrong_round_penalty = 0
```

## 4. Stock-Web OHLC Input / Price Source Validation

Manifest fields verified for this run:

```yaml
source_name: FinanceData/marcap
source_repo_url: https://github.com/FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14354401
raw_row_count: 15214118
symbol_count: 5414
active_like_symbol_count: 2868
inactive_or_delisted_like_symbol_count: 2546
markets: ['KONEX', 'KOSDAQ', 'KOSDAQ GLOBAL', 'KOSPI']
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
schema_path: atlas/schema.json
universe_path: atlas/universe/all_symbols.csv
```

The schema confirms `tradable_raw` calibration columns `d,o,h,l,c,v,a,mc,s,m`; raw/unadjusted marcap prices are used, and corporate-action contaminated windows are blocked.

## 5. Historical Eligibility Gate

|symbol|company|entry_date|180D_available|corporate_action_overlap_in_180D|calibration_usable|profile_path|
|---|---|---|---|---|---|---|
|096530|씨젠|2020-02-18|True|none|True|atlas/symbol_profiles/096/096530.json|
|084650|랩지노믹스|2020-02-18|True|none|True|atlas/symbol_profiles/084/084650.json|
|065950|웰크론|2020-02-03|True|none|True|atlas/symbol_profiles/065/065950.json|
|012690|모나리자|2020-01-23|True|none|True|atlas/symbol_profiles/012/012690.json|


All representative triggers have at least 180 stock-web tradable rows available after entry and no profile-listed corporate-action candidate inside the representative 180D window.

## 6. Canonical Archetype Compression Map

```text
COVID19_DIAGNOSTIC_EUA_EXPORT_POLICY_CONVERSION_GUARD
  -> C31_POLICY_SUBSIDY_LEGISLATION_EVENT
```

The compression rule is:

```text
policy_event_positive:
  public-health policy / authorization headline
  + issuer-level diagnostic/export/order/capacity route
  + financial or demand visibility
  -> may promote to Stage2-Actionable / Stage3-Yellow-Green shadow

policy_event_false_positive:
  public-health policy / shortage headline
  + price-only relative strength
  - issuer-level revenue/margin/order conversion
  -> cap at Watch / Stage2-only; no Green promotion
```

## 7. Case Selection Summary

|case_id|symbol|company|role|pos/counter|best_trigger|usable|current_verdict|
|---|---|---|---|---|---|---|---|
|R11L75_C31_096530_COVID_DIAGNOSTIC_EUA_EXPORT_SUCCESS|096530|씨젠|structural_success|positive|R11L75_C31_096530_20200218_STAGE2A|True|current_profile_correct|
|R11L75_C31_084650_COVID_DIAGNOSTIC_EXPORT_SUCCESS|084650|랩지노믹스|structural_success|positive|R11L75_C31_084650_20200218_STAGE2A|True|current_profile_correct|
|R11L75_C31_065950_MASK_POLICY_THEME_FALSE_POSITIVE|065950|웰크론|false_positive_green|counterexample|R11L75_C31_065950_20200203_STAGE2A|True|current_profile_false_positive|
|R11L75_C31_012690_MASK_POLICY_THEME_FAILED_RERATING|012690|모나리자|failed_rerating|counterexample|R11L75_C31_012690_20200123_STAGE2A|True|current_profile_false_positive|


## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
calibration_usable_case_count = 4
new_independent_case_ratio = 1.00
```

The positive side is not “COVID theme went up.” It is “diagnostic authorization and export capacity converted the policy shock into an issuer-specific revenue path.” The counterexample side is not “masks were irrelevant.” It is “mask-theme relative strength alone did not survive the 90D/180D drawdown test.”

## 9. Evidence Source Map

| symbol | evidence family | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence |
|---|---|---|---|---|---|
| 096530 | diagnostic authorization/export conversion | public_event_or_disclosure; policy_or_regulatory_optionality; customer_or_order_quality; capacity_or_volume_route | multiple_public_sources; financial_visibility | later valuation_blowoff overlay | none |
| 084650 | diagnostic export/order conversion | public_event_or_disclosure; policy_or_regulatory_optionality; capacity_or_volume_route | financial_visibility; multiple_public_sources | later valuation decay | none |
| 065950 | mask theme / public-health shortage | public_event_or_disclosure; policy_or_regulatory_optionality; relative_strength | none | price_only_local_peak | none |
| 012690 | mask panic / consumer hygiene proxy | public_event_or_disclosure; policy_or_regulatory_optionality; relative_strength | none | price_only_local_peak | none |

## 10. Price Data Source Map

|symbol|company|entry_row|peak_row|profile_status|shard|
|---|---|---|---|---|---|
|096530|씨젠|2020-02-18 c=35,550|2020-08-10 h=322,200|2020 clean; profile candidates only 2021 or older non-window|atlas/ohlcv_tradable_by_symbol_year/096/096530/2020.csv|
|084650|랩지노믹스|2020-02-18 c=7,460|2020-07-31 h=57,800|2020 clean; profile candidates in 2022/2023 outside window|atlas/ohlcv_tradable_by_symbol_year/084/084650/2020.csv|
|065950|웰크론|2020-02-03 c=6,600|2020-02-21 h=10,700|2020 clean; profile candidate 2006 only|atlas/ohlcv_tradable_by_symbol_year/065/065950/2020.csv|
|012690|모나리자|2020-01-23 c=6,230|2020-02-03 h=9,790|2020 clean; profile candidates before 2003|atlas/ohlcv_tradable_by_symbol_year/012/012690/2020.csv|


## 11. Case-by-Case Trigger Grid

|trigger_id|symbol|type|trigger_date|entry_date|entry_px|MFE30|MAE30|MFE90|MAE90|MFE180|MAE180|peak_date|peak_px|usable|aggregate_role|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R11L75_C31_096530_20200218_STAGE2A|096530|Stage2-Actionable|2020-02-18|2020-02-18|35550|297.75|-10.27|297.75|-10.27|806.33|-10.27|2020-08-10|322200|True|representative|
|R11L75_C31_084650_20200218_STAGE2A|084650|Stage2-Actionable|2020-02-18|2020-02-18|7460|259.25|-5.63|362.47|-5.63|674.8|-5.63|2020-07-31|57800|True|representative|
|R11L75_C31_065950_20200203_STAGE2A|065950|Stage2-Actionable|2020-02-03|2020-02-03|6600|62.12|-8.64|62.12|-23.48|62.12|-23.48|2020-02-21|10700|True|representative|
|R11L75_C31_012690_20200123_STAGE2A|012690|Stage2-Actionable|2020-01-23|2020-01-23|6230|57.14|-26.89|57.14|-39.0|57.14|-39.0|2020-02-03|9790|True|representative|
|R11L75_C31_096530_20200810_4B_OVERLAY|096530|4B-overlay|2020-08-10|2020-08-10|310700|3.7|-31.32|3.7|-31.32|3.7|-31.32|2020-08-10|322200|True|4B_overlay_only|
|R11L75_C31_012690_20200131_4B_PRICE_ONLY|012690|4B-overlay-price-only|2020-01-31|2020-01-31|9130|7.23|-51.48|7.23|-58.38|7.23|-58.38|2020-02-03|9790|True|4B_overlay_only|


## 12. Trigger-Level OHLC Backtest Tables

The representative aggregate rows are the four Stage2-Actionable entries. 4B rows are overlay-only and excluded from aggregate promotion metrics.

| aggregate bucket | symbols | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | interpretation |
|---|---|---:|---:|---:|---:|---|
| diagnostic issuer-conversion positives | 096530; 084650 | 330.11 | -7.95 | 740.57 | -7.95 | policy event became issuer-specific revenue/capacity rerating |
| mask/public-health theme counterexamples | 065950; 012690 | 59.63 | -31.24 | 59.63 | -31.24 | price-only beta had MFE but poor drawdown profile |
| all representative rows | all 4 | 194.87 | -19.60 | 400.10 | -19.60 | current profile needs conversion split, not broad promotion |

## 13. Current Calibrated Profile Stress Test

| case_id | current profile likely decision | actual MFE/MAE alignment | verdict | residual lesson |
|---|---|---|---|---|
| R11L75_C31_096530_COVID_DIAGNOSTIC_EUA_EXPORT_SUCCESS | Stage3-Yellow/Green if issuer conversion recognized | very high MFE, limited early MAE | current_profile_correct | policy score is justified only with issuer-level diagnostic conversion |
| R11L75_C31_084650_COVID_DIAGNOSTIC_EXPORT_SUCCESS | Stage3-Yellow if export route recognized | very high MFE, limited early MAE | current_profile_correct | diagnostic/export conversion should not wait for fully confirmed Green |
| R11L75_C31_065950_MASK_POLICY_THEME_FALSE_POSITIVE | Stage3-Yellow risk if relative strength + policy headline over-weighted | MFE existed, but 90D MAE -23.48 and peak drawdown -52.80 | current_profile_false_positive | policy-only theme must be capped |
| R11L75_C31_012690_MASK_POLICY_THEME_FAILED_RERATING | Stage3-Yellow risk if shortage headline over-weighted | MFE existed, but 90D MAE -39.00 and peak drawdown -61.18 | current_profile_false_positive | price-only panic demand is not durable policy conversion |

Existing axis handling:

```text
stage2_actionable_evidence_bonus: existing_axis_tested
stage3_yellow_total_min: existing_axis_tested
stage3_green_total_min: existing_axis_tested
price_only_blowoff_blocks_positive_stage: existing_axis_strengthened
full_4b_requires_non_price_evidence: existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c: existing_axis_kept
```

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 entry | Stage2 price | Stage3-Green proxy | Stage3 proxy price | full-window peak | green_lateness_ratio | interpretation |
|---|---|---:|---|---:|---:|---:|---|
| R11L75_C31_096530_COVID_DIAGNOSTIC_EUA_EXPORT_SUCCESS | 2020-02-18 | 35,550 | 2020-05-14 | 128,800 | 322,200 | 0.325 | Green is somewhat late but not terminal; Stage2A captured the conversion earlier |
| R11L75_C31_084650_COVID_DIAGNOSTIC_EXPORT_SUCCESS | 2020-02-18 | 7,460 | 2020-04-24 | 24,350 | 57,800 | 0.336 | Green is somewhat late; conversion evidence justified earlier actionability |
| R11L75_C31_065950_MASK_POLICY_THEME_FALSE_POSITIVE | 2020-02-03 | 6,600 | none | n/a | 10,700 | n/a | no confirmed Green; price-only theme should remain capped |
| R11L75_C31_012690_MASK_POLICY_THEME_FAILED_RERATING | 2020-01-23 | 6,230 | none | n/a | 9,790 | n/a | no confirmed Green; headline demand did not become durable rerating |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | symbol | 4B evidence type | local proximity | full-window proximity | verdict |
|---|---|---|---:|---:|---|
| R11L75_C31_096530_20200810_4B_OVERLAY | 096530 | valuation_blowoff; positioning_overheat; price_only | 0.96 | 0.96 | good full-window 4B timing as overlay after extreme rerating |
| R11L75_C31_012690_20200131_4B_PRICE_ONLY | 012690 | price_only; positioning_overheat | 0.81 | 0.81 | price-only near-peak overlay worked, but cannot be full 4B without non-price evidence |
| R11L75_C31_065950_20200203_STAGE2A | 065950 | price_only_local_peak later | n/a | n/a | representative entry; later price-only peak supports guard, not promotion |

## 16. 4C Protection Audit

No representative row is a hard 4C thesis-break row. The 4C label remains `thesis_break_watch_only` or `false_break`. The contribution here is a Stage2/3 promotion guard and a 4B overlay split, not a hard 4C routing change.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
rule_id = L10_public_health_policy_event_conversion_gate
candidate = true
```

Rule candidate:

```text
For public-health emergency/policy events, do not let policy_or_regulatory_score + relative_strength_score alone create Stage3-Yellow/Green.
Promotion requires at least one issuer-level conversion field:
  - diagnostic authorization/export route,
  - confirmed order/customer channel,
  - capacity/shipment route,
  - financial visibility / margin bridge.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
candidate = true
```

Canonical guard:

```text
C31_policy_event_conversion_gate:
  if policy event is broad and issuer conversion is missing:
      cap positive stage at Stage2-Watch
      block Stage3-Green even if relative strength is high
      allow 4B price-only overlay but not full 4B without non-price evidence
  if policy event has issuer conversion evidence:
      allow Stage2-Actionable and Stage3-Yellow/Green shadow promotion
```

## 19. Before / After Backtest Comparison

|profile_id|scope|eligible_trigger_count|selected_entry_trigger_per_case|avg_MFE_90D_pct|avg_MAE_90D_pct|avg_MFE_180D_pct|avg_MAE_180D_pct|false_positive_rate|missed_structural_count|late_green_count|avg_green_lateness_ratio|score_return_alignment_verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|P0 e2r_2_1_stock_web_calibrated_proxy|current|4|representative Stage2A rows|194.87|-19.6|400.1|-19.6|2/4|0|2|0.331|mixed; positive diagnostics good, mask themes over-promoted|
|P0b e2r_2_0_baseline_reference|rollback|4|representative Stage2A rows|194.87|-19.6|400.1|-19.6|2/4 but weaker conversion handling|2|2|0.331|worse for diagnostics|
|P1 sector_specific_candidate_profile|L10 public-health policy|4|positive conversion only|330.11|-7.95|740.57|-7.95|0/2 after mask-theme cap|0|1|0.331|better|
|P2 canonical_archetype_candidate_profile|C31 conversion gate|4|policy + issuer conversion|330.11|-7.95|740.57|-7.95|low|0|1|0.331|best|
|P3 counterexample_guard_profile|C31 policy-only beta guard|4|mask themes blocked|59.63|-31.24|59.63|-31.24|0/2 selected as positive|0|0|n/a|best for drawdown control|


## 20. Score-Return Alignment Matrix

| symbol | before_score | before_label | after_score | after_label | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 096530 | 84 | Stage3-Yellow | 90 | Stage3-Green-Shadow | 297.75 | -10.27 | aligned positive conversion |
| 084650 | 84 | Stage3-Yellow | 90 | Stage3-Green-Shadow | 362.47 | -5.63 | aligned positive conversion |
| 065950 | 78 | Stage3-Yellow false-positive risk | 61 | Stage2-Watch-Blocked | 62.12 | -23.48 | guard needed |
| 012690 | 78 | Stage3-Yellow false-positive risk | 61 | Stage2-Watch-Blocked | 57.14 | -39.00 | guard needed |

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|L10_POLICY_EVENT_CROSS_REDTEAM_MISC|C31_POLICY_SUBSIDY_LEGISLATION_EVENT|COVID19_DIAGNOSTIC_EUA_EXPORT_POLICY_CONVERSION_GUARD|2|2|2|0|4|0|6|4|2|True|True|COVID diagnostic conversion vs mask policy-theme false-positive split added; still needs non-COVID disaster-policy holdout|


## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus; stage3_yellow_total_min; stage3_green_total_min; price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence
residual_error_types_found: policy_theme_false_positive; issuer_conversion_vs_policy_beta_split; price_only_mask_theme_4B_overlay
new_axis_proposed: C31_policy_event_issuer_conversion_gate; C31_policy_only_theme_stage3_cap
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- actual stock-web tradable OHLC rows for 2020 representative entries
- entry_date / entry_price from c column
- MFE/MAE 30D/90D/180D proxy calculations from stock-web OHLC windows
- clean 180D window status from symbol profile corporate-action candidate dates
- current calibrated profile stress-test labels
- positive/counterexample balance
- 4B local/full-window split for overlay rows
```

Not validated:

```text
- no live candidate discovery
- no 2026 present recommendation
- no broker/API/trading action
- no stock_agent source-code inspection
- no production scoring change
- no raw shard weight calibration
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,policy_event_issuer_conversion_gate,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"policy headline must have issuer-level order/export/capacity/margin conversion","keeps two diagnostic successes while blocking two mask-theme false positives",R11L75_C31_096530_20200218_STAGE2A|R11L75_C31_084650_20200218_STAGE2A|R11L75_C31_065950_20200203_STAGE2A|R11L75_C31_012690_20200123_STAGE2A,4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,policy_only_theme_stage3_cap,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"mask/public-health theme beta without issuer conversion should not become Stage3 Green","reduces false positive rate from 2/4 to 0/2 for policy-only themes",R11L75_C31_065950_20200203_STAGE2A|R11L75_C31_012690_20200123_STAGE2A,2,2,2,medium,counterexample_guard,"not production; post-calibrated residual"
shadow_weight,price_only_4b_overlay_non_promotion,existing_axis_strengthened,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,1,1,0,"price-only local peak can be a risk overlay but cannot promote positive stage","supports existing price-only blowoff and full-4B non-price requirements",R11L75_C31_096530_20200810_4B_OVERLAY|R11L75_C31_012690_20200131_4B_PRICE_ONLY,2,2,1,low,axis_strengthened,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R11L75_C31_096530_COVID_DIAGNOSTIC_EUA_EXPORT_SUCCESS","symbol":"096530","company_name":"씨젠","round":"R11","loop":"75","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"COVID19_DIAGNOSTIC_EUA_EXPORT_POLICY_CONVERSION_GUARD","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R11L75_C31_096530_20200218_STAGE2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"issuer-level diagnostic approval/export route aligned with very high MFE and controlled early MAE","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"COVID-19 diagnostic authorization/export conversion: the policy event became revenue-visible through issuer-specific kit capacity and export route."}
{"row_type":"case","case_id":"R11L75_C31_084650_COVID_DIAGNOSTIC_EXPORT_SUCCESS","symbol":"084650","company_name":"랩지노믹스","round":"R11","loop":"75","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"COVID19_DIAGNOSTIC_EUA_EXPORT_POLICY_CONVERSION_GUARD","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R11L75_C31_084650_20200218_STAGE2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"issuer-level diagnostic/export route aligned with high MFE despite later post-peak decay","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"COVID diagnostic conversion positive case; public-health policy shock converted into order/export optionality rather than remaining a generic theme."}
{"row_type":"case","case_id":"R11L75_C31_065950_MASK_POLICY_THEME_FALSE_POSITIVE","symbol":"065950","company_name":"웰크론","round":"R11","loop":"75","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"COVID19_DIAGNOSTIC_EUA_EXPORT_POLICY_CONVERSION_GUARD","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R11L75_C31_065950_20200203_STAGE2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"policy/mask shortage theme produced MFE but high MAE and post-peak drawdown without durable issuer-level conversion","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Mask/public-health policy theme: relative strength existed, but no durable company-specific conversion was visible enough to justify Stage3."}
{"row_type":"case","case_id":"R11L75_C31_012690_MASK_POLICY_THEME_FAILED_RERATING","symbol":"012690","company_name":"모나리자","round":"R11","loop":"75","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"COVID19_DIAGNOSTIC_EUA_EXPORT_POLICY_CONVERSION_GUARD","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R11L75_C31_012690_20200123_STAGE2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"headline/panic demand had sharp MFE but later drawdown overwhelmed the non-confirmed thesis","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Consumer hygiene / mask panic proxy: a broad public-health shock should stay capped unless issuer-level revenue/margin conversion is confirmed."}
{"row_type":"trigger","trigger_id":"R11L75_C31_096530_20200218_STAGE2A","case_id":"R11L75_C31_096530_COVID_DIAGNOSTIC_EUA_EXPORT_SUCCESS","symbol":"096530","company_name":"씨젠","round":"R11","loop":"75","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"COVID19_DIAGNOSTIC_EUA_EXPORT_POLICY_CONVERSION_GUARD","sector":"policy_event_cross_redteam","primary_archetype":"policy_subsidy_legislation_event","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2020-02-18","evidence_available_at_that_date":"COVID-19 diagnostic authorization/export route and issuer-specific molecular diagnostic capacity were visible; this was not a price-only pandemic beta row.","evidence_source":"public health emergency-use / export-authorization reporting; stock-web OHLC row 2020-02-18","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","customer_or_order_quality","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["multiple_public_sources","financial_visibility","durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/096/096530/2020.csv","profile_path":"atlas/symbol_profiles/096/096530.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2020-02-18","entry_price":35550,"MFE_30D_pct":297.75,"MFE_90D_pct":297.75,"MFE_180D_pct":806.33,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-10.27,"MAE_90D_pct":-10.27,"MAE_180D_pct":-10.27,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2020-08-10","peak_price":322200,"drawdown_after_peak_pct":-33.77,"green_lateness_ratio":0.325,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_for_representative_entry","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"policy_plus_issuer_specific_diagnostic_conversion_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_R11L75_096530_20200218","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R11L75_C31_084650_20200218_STAGE2A","case_id":"R11L75_C31_084650_COVID_DIAGNOSTIC_EXPORT_SUCCESS","symbol":"084650","company_name":"랩지노믹스","round":"R11","loop":"75","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"COVID19_DIAGNOSTIC_EUA_EXPORT_POLICY_CONVERSION_GUARD","sector":"policy_event_cross_redteam","primary_archetype":"policy_subsidy_legislation_event","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2020-02-18","evidence_available_at_that_date":"COVID diagnostic test/export optionality was visible at issuer level; public-health policy shock had a company-specific conversion path.","evidence_source":"public COVID-19 diagnostic/export reporting; stock-web OHLC row 2020-02-18","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","capacity_or_volume_route","customer_or_order_quality","early_revision_signal"],"stage3_evidence_fields":["financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/084/084650/2020.csv","profile_path":"atlas/symbol_profiles/084/084650.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2020-02-18","entry_price":7460,"MFE_30D_pct":259.25,"MFE_90D_pct":362.47,"MFE_180D_pct":674.8,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.63,"MAE_90D_pct":-5.63,"MAE_180D_pct":-5.63,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2020-07-31","peak_price":57800,"drawdown_after_peak_pct":-51.12,"green_lateness_ratio":0.336,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_for_representative_entry","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"diagnostic_export_conversion_success_with_later_decay","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_R11L75_084650_20200218","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R11L75_C31_065950_20200203_STAGE2A","case_id":"R11L75_C31_065950_MASK_POLICY_THEME_FALSE_POSITIVE","symbol":"065950","company_name":"웰크론","round":"R11","loop":"75","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"COVID19_DIAGNOSTIC_EUA_EXPORT_POLICY_CONVERSION_GUARD","sector":"policy_event_cross_redteam","primary_archetype":"policy_subsidy_legislation_event","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2020-02-03","evidence_available_at_that_date":"Mask/public-health shortage theme had relative strength, but no durable issuer-level order, margin bridge, or policy allocation evidence was visible.","evidence_source":"public mask shortage/social-distancing theme; stock-web OHLC row 2020-02-03","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/065/065950/2020.csv","profile_path":"atlas/symbol_profiles/065/065950.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2020-02-03","entry_price":6600,"MFE_30D_pct":62.12,"MFE_90D_pct":62.12,"MFE_180D_pct":62.12,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-8.64,"MAE_90D_pct":-23.48,"MAE_180D_pct":-23.48,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2020-02-21","peak_price":10700,"drawdown_after_peak_pct":-52.8,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_for_representative_entry","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"policy_theme_false_positive_high_drawdown","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_R11L75_065950_20200203","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R11L75_C31_012690_20200123_STAGE2A","case_id":"R11L75_C31_012690_MASK_POLICY_THEME_FAILED_RERATING","symbol":"012690","company_name":"모나리자","round":"R11","loop":"75","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"COVID19_DIAGNOSTIC_EUA_EXPORT_POLICY_CONVERSION_GUARD","sector":"policy_event_cross_redteam","primary_archetype":"policy_subsidy_legislation_event","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2020-01-23","evidence_available_at_that_date":"Public-health/mask panic demand had a policy/event headline and relative strength, but no durable issuer-specific conversion evidence was available.","evidence_source":"public mask-demand theme; stock-web OHLC row 2020-01-23","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012690/2020.csv","profile_path":"atlas/symbol_profiles/012/012690.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2020-01-23","entry_price":6230,"MFE_30D_pct":57.14,"MFE_90D_pct":57.14,"MFE_180D_pct":57.14,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-26.89,"MAE_90D_pct":-39.0,"MAE_180D_pct":-39.0,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2020-02-03","peak_price":9790,"drawdown_after_peak_pct":-61.18,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_for_representative_entry","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"policy_theme_failed_rerating_high_drawdown","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_R11L75_012690_20200123","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R11L75_C31_096530_20200810_4B_OVERLAY","case_id":"R11L75_C31_096530_COVID_DIAGNOSTIC_EUA_EXPORT_SUCCESS","symbol":"096530","company_name":"씨젠","round":"R11","loop":"75","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"COVID19_DIAGNOSTIC_EUA_EXPORT_POLICY_CONVERSION_GUARD","sector":"policy_event_cross_redteam","primary_archetype":"policy_subsidy_legislation_event","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill|4B_non_price_requirement_stress_test","trigger_type":"4B-overlay","trigger_date":"2020-08-10","evidence_available_at_that_date":"Local/full-window peak zone after extreme rerating. 4B overlay is timing/risk only, not a negation of the earlier Stage2 entry.","evidence_source":"stock-web OHLC row 2020-08-10 and post-peak drawdown path","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","capacity_or_volume_route"],"stage3_evidence_fields":["financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/096/096530/2020.csv","profile_path":"atlas/symbol_profiles/096/096530.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2020-08-10","entry_price":310700,"MFE_30D_pct":3.7,"MFE_90D_pct":3.7,"MFE_180D_pct":3.7,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-31.32,"MAE_90D_pct":-31.32,"MAE_180D_pct":-31.32,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2020-08-10","peak_price":322200,"drawdown_after_peak_pct":-33.77,"green_lateness_ratio":0.9599,"four_b_local_peak_proximity":0.96,"four_b_full_window_peak_proximity":0.96,"four_b_timing_verdict":"good_full_window_4B_timing_with_valuation_and_positioning_overheat","four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only"],"four_c_protection_label":"false_break","trigger_outcome_label":"4B_overlay_success_for_risk_reduction_not_stage_promotion","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_R11L75_096530_20200810_4B","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R11L75_C31_012690_20200131_4B_PRICE_ONLY","case_id":"R11L75_C31_012690_MASK_POLICY_THEME_FAILED_RERATING","symbol":"012690","company_name":"모나리자","round":"R11","loop":"75","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"COVID19_DIAGNOSTIC_EUA_EXPORT_POLICY_CONVERSION_GUARD","sector":"policy_event_cross_redteam","primary_archetype":"policy_subsidy_legislation_event","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill|4B_non_price_requirement_stress_test","trigger_type":"4B-overlay-price-only","trigger_date":"2020-01-31","evidence_available_at_that_date":"Price spike near the local/full observed peak with no non-price issuer-level conversion evidence; it works as risk overlay, not as full 4B thesis evidence.","evidence_source":"stock-web OHLC row 2020-01-31 and peak row 2020-02-03","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012690/2020.csv","profile_path":"atlas/symbol_profiles/012/012690.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2020-01-31","entry_price":9130,"MFE_30D_pct":7.23,"MFE_90D_pct":7.23,"MFE_180D_pct":7.23,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-51.48,"MAE_90D_pct":-58.38,"MAE_180D_pct":-58.38,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2020-02-03","peak_price":9790,"drawdown_after_peak_pct":-61.18,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.81,"four_b_full_window_peak_proximity":0.81,"four_b_timing_verdict":"price_only_local_peak_near_full_window_peak_but_not_full_4B_without_non_price_evidence","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"price_only_4B_overlay_success_but_not_positive_stage","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_R11L75_012690_20200131_4B","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L75_C31_096530_COVID_DIAGNOSTIC_EUA_EXPORT_SUCCESS","trigger_id":"R11L75_C31_096530_20200218_STAGE2A","symbol":"096530","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":5,"relative_strength_score":8,"customer_quality_score":7,"policy_or_regulatory_score":8,"valuation_repricing_score":6,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":84,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":4,"margin_bridge_score":6,"revision_score":7,"relative_strength_score":8,"customer_quality_score":8,"policy_or_regulatory_score":9,"valuation_repricing_score":6,"execution_risk_score":1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":90,"stage_label_after":"Stage3-Green-Shadow","changed_components":["policy_or_regulatory_score","customer_quality_score","backlog_visibility_score","margin_bridge_score","revision_score"],"component_delta_explanation":"Public-health policy event is promoted only when issuer-level diagnostic approval/export/order/capacity evidence converts the headline into revenue visibility.","MFE_90D_pct":297.75,"MAE_90D_pct":-10.27,"score_return_alignment_label":"positive_policy_conversion_aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L75_C31_084650_COVID_DIAGNOSTIC_EXPORT_SUCCESS","trigger_id":"R11L75_C31_084650_20200218_STAGE2A","symbol":"084650","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":5,"relative_strength_score":8,"customer_quality_score":7,"policy_or_regulatory_score":8,"valuation_repricing_score":6,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":84,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":4,"margin_bridge_score":6,"revision_score":7,"relative_strength_score":8,"customer_quality_score":8,"policy_or_regulatory_score":9,"valuation_repricing_score":6,"execution_risk_score":1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":90,"stage_label_after":"Stage3-Green-Shadow","changed_components":["policy_or_regulatory_score","customer_quality_score","backlog_visibility_score","margin_bridge_score","revision_score"],"component_delta_explanation":"Public-health policy event is promoted only when issuer-level diagnostic approval/export/order/capacity evidence converts the headline into revenue visibility.","MFE_90D_pct":362.47,"MAE_90D_pct":-5.63,"score_return_alignment_label":"positive_policy_conversion_aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L75_C31_065950_MASK_POLICY_THEME_FALSE_POSITIVE","trigger_id":"R11L75_C31_065950_20200203_STAGE2A","symbol":"065950","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":10,"customer_quality_score":1,"policy_or_regulatory_score":7,"valuation_repricing_score":5,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow_false_positive_risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":4,"customer_quality_score":0,"policy_or_regulatory_score":4,"valuation_repricing_score":1,"execution_risk_score":10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":61,"stage_label_after":"Stage2-Watch-Blocked","changed_components":["policy_or_regulatory_score","relative_strength_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"Policy/mask shortage headline without issuer-level order/margin/capacity conversion should be capped; relative strength becomes risk evidence after a price-only spike.","MFE_90D_pct":62.12,"MAE_90D_pct":-23.48,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L75_C31_012690_MASK_POLICY_THEME_FAILED_RERATING","trigger_id":"R11L75_C31_012690_20200123_STAGE2A","symbol":"012690","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":10,"customer_quality_score":1,"policy_or_regulatory_score":7,"valuation_repricing_score":5,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow_false_positive_risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":4,"customer_quality_score":0,"policy_or_regulatory_score":4,"valuation_repricing_score":1,"execution_risk_score":10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":61,"stage_label_after":"Stage2-Watch-Blocked","changed_components":["policy_or_regulatory_score","relative_strength_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"Policy/mask shortage headline without issuer-level order/margin/capacity conversion should be capped; relative strength becomes risk evidence after a price-only spike.","MFE_90D_pct":57.14,"MAE_90D_pct":-39.0,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R11","loop":"75","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","scheduled_round":"R11","scheduled_loop":"75","round_schedule_status":"valid","round_sector_consistency":"pass","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"new_trigger_family_count":4,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":2,"diversity_score_summary":"new_symbols=4; new_trigger_families=4; counterexamples=2; residual_errors=2; wrong_round_penalty=0","tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["policy_theme_false_positive","issuer_conversion_vs_policy_beta_split","price_only_mask_theme_4B_overlay"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules

- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate large_sector_id and canonical_archetype_id.
4. Validate novelty and reuse fields.
5. Deduplicate same_entry_group_id and reused cases.
6. Aggregate by large_sector_id and canonical_archetype_id.
7. Update sector_shadow_profile and archetype_shadow_profile only.
8. Preserve global calibrated profile unless explicitly promoted.
9. Report new independent cases, counterexamples, and residual error types.
10. Add tests that duplicate low-value loops cannot change weights.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R11
completed_loop = 75
next_round = R12
next_loop = 75
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
price_source = Songdaiki/stock-web
manifest_path = atlas/manifest.json
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
stock_web_manifest_max_date = 2026-02-20
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
representative_shards =
  atlas/ohlcv_tradable_by_symbol_year/096/096530/2020.csv
  atlas/ohlcv_tradable_by_symbol_year/084/084650/2020.csv
  atlas/ohlcv_tradable_by_symbol_year/065/065950/2020.csv
  atlas/ohlcv_tradable_by_symbol_year/012/012690/2020.csv
profile_paths =
  atlas/symbol_profiles/096/096530.json
  atlas/symbol_profiles/084/084650.json
  atlas/symbol_profiles/065/065950.json
  atlas/symbol_profiles/012/012690.json
```

