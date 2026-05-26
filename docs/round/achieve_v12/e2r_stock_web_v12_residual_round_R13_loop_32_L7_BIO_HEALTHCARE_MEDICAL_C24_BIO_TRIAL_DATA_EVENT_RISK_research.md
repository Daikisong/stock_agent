# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
round = R13
loop = 32
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id = BIO_TRIAL_DATA_EVENT_BINARY_OUTCOME_GATED_BY_PARTNER_AND_COMMERCIAL_BRIDGE
output_file = e2r_stock_web_v12_residual_round_R13_loop_32_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This file is historical calibration research only. It is not a live candidate screen, not a recommendation, and not a repository patch.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
previous_baseline_reference = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This loop does not re-propose those global axes. It asks whether C24 needs a narrower shadow profile: binary clinical-data events can be real enough for Stage2/Yellow, but still too brittle for Green unless the trial signal is converted into revision durability, a named partner route, or commercialization visibility.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id = BIO_TRIAL_DATA_EVENT_BINARY_OUTCOME_GATED_BY_PARTNER_AND_COMMERCIAL_BRIDGE
loop_objective = holdout_validation;residual_false_positive_mining;residual_missed_structural_mining;yellow_threshold_stress_test;green_strictness_stress_test;stage2_actionable_bonus_stress_test;4B_non_price_requirement_stress_test;4C_thesis_break_timing_test;sector_specific_rule_discovery;canonical_archetype_compression;counterexample_mining;coverage_gap_fill
```

C24 is the “clinical data event risk” bucket. The useful distinction is not simply good data versus bad data. The more useful distinction is whether the event is a bridge, a checkpoint, or a cliff. A bridge can connect data to revision and commercialization. A checkpoint deserves Stage2/Yellow but not Green. A cliff is hard 4C.

## 3. Previous Coverage / Duplicate Avoidance Check

Prior C24 coverage already included 유한양행, 알테오젠, HLB, and SK바이오사이언스. This loop excludes all four from quantitative evidence. It adds four independent symbols: 한올바이오파마, 오스코텍, 신라젠, and 에이비엘바이오.

```text
required_new_independent_case_ratio = 0.60
actual_new_independent_case_ratio = 1.00
reused_case_count = 0
loop_contribution_label = canonical_archetype_rule_candidate
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
source = Songdaiki/stock-web
source_url = https://github.com/Songdaiki/stock-web
manifest_path = atlas/manifest.json
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
manifest_max_date = 2026-02-20
source_name = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
markets = KONEX; KOSDAQ; KOSDAQ GLOBAL; KOSPI
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
```

The OHLC rows used here are raw/unadjusted tradable rows. Corporate-action candidate dates from each symbol profile were checked against the relevant 180D window. No representative trigger in this loop is blocked for 180D calibration.

## 5. Historical Eligibility Gate

All representative triggers satisfy the historical gate:

```text
trigger_date_is_historical = true
entry_date_exists_in_stock_web_tradable_shard = true
minimum_forward_window = 180 trading days
high_low_close_volume_present = true
MFE_30D_90D_180D_calculated = true
MAE_30D_90D_180D_calculated = true
corporate_action_contaminated_180D_window = false
```

The 1Y/2Y columns are intentionally not used for weight calibration because this loop is focused on 30D/90D/180D event-risk behavior.

## 6. Canonical Archetype Compression Map

```text
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id = BIO_TRIAL_DATA_EVENT_BINARY_OUTCOME_GATED_BY_PARTNER_AND_COMMERCIAL_BRIDGE
maps_to_large_sector = L7_BIO_HEALTHCARE_MEDICAL
```

Fine-grained cases compress into three reusable C24 patterns:

1. **Partner-backed clinical data checkpoint**: Stage2/Yellow, not Green unless durable revision follows.
2. **Hard clinical failure or futility cliff**: immediate 4C, even if the entry row is already gap-damaged.
3. **Partner/license headline without clinical proof**: 4B/event-cap guard, not Stage3-Green promotion.

## 7. Case Selection Summary

|case_id|symbol|company_name|case_type|positive_or_counterexample|best_trigger|current_profile_verdict|notes|
|---|---|---|---|---|---|---|---|
|R13L32_C24_009420_HANALL_20230927_PARTNER_DATA_POSITIVE|009420|한올바이오파마|stage2_promote_candidate|positive|TRG_R13L32_009420_STAGE2_20230927|current_profile_correct|Partner-backed FcRn clinical data created a real but non-Green-safe rerating path; upside existed, but the later drawdown shows why C24 should remain event-gated until durable revision/commercial route is visible.|
|R13L32_C24_039200_OSCOTEC_20200921_DATA_POSITIVE_HIGH_MAE|039200|오스코텍|high_mae_success|positive|TRG_R13L32_039200_STAGE2_20200921|current_profile_correct|Trial-data/event evidence produced large MFE, but the subsequent data-disappointment/drawdown makes Green strictness appropriate rather than a reason to loosen the global Green threshold.|
|R13L32_C24_215600_SILLAJEN_20190802_PHASE3_FUTILITY_4C|215600|신라젠|4C_success|counterexample|TRG_R13L32_215600_4C_20190802|current_profile_4C_too_late|Phase-3 futility/thesis break is a hard C24 4C archetype: the entry row itself is already gap-damaged and further drawdown remains severe.|
|R13L32_C24_298380_ABL_20220112_LICENSE_EVENT_FALSE_POSITIVE|298380|에이비엘바이오|failed_rerating|counterexample|TRG_R13L32_298380_STAGE2_20220112|current_profile_false_positive|A large partner/licensing event generated early MFE but did not behave like durable clinical-data confirmation; it is a useful guard against treating all partner headlines as Stage3 clinical proof.|

## 8. Positive vs Counterexample Balance

```text
positive_structural_success_or_stage2_candidate = 2
counterexample_or_failed_rerating = 2
4B_or_4C_case = 3
minimum_calibration_usable_case_count = 3
actual_calibration_usable_case_count = 4
```

The two positive cases are deliberately not clean “buy-and-hold forever” stories. They are useful because they show the engine should not block C24 event risk entirely. The two counterexamples show why the same engine must refuse Green promotion when the only bridge is price action or a headline.

## 9. Evidence Source Map

| case_id | event evidence type | stage2 evidence | stage3 evidence | 4B/4C evidence |
|---|---|---|---|---|
| R13L32_C24_009420_HANALL_20230927_PARTNER_DATA_POSITIVE | partner-backed clinical data event | public event, partner quality, relative strength | partial multi-source confirmation | valuation/positioning risk |
| R13L32_C24_039200_OSCOTEC_20200921_DATA_POSITIVE_HIGH_MAE | oncology clinical data event | public data event, relative strength, partner/customer route | partial confirmation | later thesis-quality downgrade risk |
| R13L32_C24_215600_SILLAJEN_20190802_PHASE3_FUTILITY_4C | phase-3 futility / hard trial failure | none | none | hard trial failure, thesis evidence broken |
| R13L32_C24_298380_ABL_20220112_LICENSE_EVENT_FALSE_POSITIVE | partner/license headline, not clinical-data confirmation | public event, partner quality, relative strength | insufficient clinical/financial proof | event cap, valuation blowoff, positioning overheat |

## 10. Price Data Source Map

| symbol | company | profile_path | primary shard(s) | corporate action window status |
|---|---|---|---|---|
| 009420 | 한올바이오파마 | atlas/symbol_profiles/009/009420.json | atlas/ohlcv_tradable_by_symbol_year/009/009420/2023.csv; 2024.csv | clean_180D_window |
| 039200 | 오스코텍 | atlas/symbol_profiles/039/039200.json | atlas/ohlcv_tradable_by_symbol_year/039/039200/2020.csv; 2021.csv | clean_180D_window |
| 215600 | 신라젠 | atlas/symbol_profiles/215/215600.json | atlas/ohlcv_tradable_by_symbol_year/215/215600/2019.csv | clean_180D_window |
| 298380 | 에이비엘바이오 | atlas/symbol_profiles/298/298380.json | atlas/ohlcv_tradable_by_symbol_year/298/298380/2022.csv | clean_180D_window |

## 11. Case-by-Case Trigger Grid

|trigger_id|symbol|trigger_type|entry_date|entry_price|MFE_30D_pct|MFE_90D_pct|MFE_180D_pct|MAE_30D_pct|MAE_90D_pct|MAE_180D_pct|peak_date|peak_price|current_profile_verdict|dedupe_for_aggregate|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|TRG_R13L32_009420_STAGE2_20230927|009420|Stage2-Actionable|2023-09-27|32650|21.75|43.19|43.19|-12.4|-12.56|-12.56|2023-12-27|46750|current_profile_correct|True|
|TRG_R13L32_009420_STAGE3GREEN_20231227|009420|Stage3-Green-comparison|2023-12-27|44300|5.53|5.53|5.53|-35.55|-35.55|-35.55|2023-12-27|46750|current_profile_correct|False|
|TRG_R13L32_039200_STAGE2_20200921|039200|Stage2-Actionable|2020-09-21|46000|16.3|55.43|55.43|-16.09|-16.09|-32.5|2020-12-08|71500|current_profile_correct|True|
|TRG_R13L32_039200_4C_20210107|039200|4C-thesis-break-watch|2021-01-07|51000|5.88|5.88|5.88|-25.88|-39.12|-39.12|2021-01-07|54000|current_profile_4C_too_late|False|
|TRG_R13L32_215600_4C_20190802|215600|4C-hard-thesis-break|2019-08-02|31200|0.0|0.0|0.0|-71.15|-74.94|-74.94|2019-08-02|31200|current_profile_4C_too_late|True|
|TRG_R13L32_298380_STAGE2_20220112|298380|Stage2-Actionable-false-positive|2022-01-12|26150|33.08|33.08|33.08|-8.99|-26.58|-27.92|2022-01-21|34800|current_profile_false_positive|True|
|TRG_R13L32_298380_4B_20220121|298380|4B-overlay|2022-01-21|33050|5.3|5.3|5.3|-26.48|-41.91|-48.41|2022-01-21|34800|current_profile_correct|False|

## 12. Trigger-Level OHLC Backtest Tables

### Representative aggregate triggers

|trigger_id|symbol|trigger_type|entry_date|entry_price|MFE_30D_pct|MFE_90D_pct|MFE_180D_pct|MAE_30D_pct|MAE_90D_pct|MAE_180D_pct|peak_date|peak_price|current_profile_verdict|dedupe_for_aggregate|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|TRG_R13L32_009420_STAGE2_20230927|009420|Stage2-Actionable|2023-09-27|32650|21.75|43.19|43.19|-12.4|-12.56|-12.56|2023-12-27|46750|current_profile_correct|True|
|TRG_R13L32_039200_STAGE2_20200921|039200|Stage2-Actionable|2020-09-21|46000|16.3|55.43|55.43|-16.09|-16.09|-32.5|2020-12-08|71500|current_profile_correct|True|
|TRG_R13L32_215600_4C_20190802|215600|4C-hard-thesis-break|2019-08-02|31200|0.0|0.0|0.0|-71.15|-74.94|-74.94|2019-08-02|31200|current_profile_4C_too_late|True|
|TRG_R13L32_298380_STAGE2_20220112|298380|Stage2-Actionable-false-positive|2022-01-12|26150|33.08|33.08|33.08|-8.99|-26.58|-27.92|2022-01-21|34800|current_profile_false_positive|True|

### Label comparison / overlay triggers

|trigger_id|symbol|trigger_type|entry_date|entry_price|MFE_30D_pct|MFE_90D_pct|MFE_180D_pct|MAE_30D_pct|MAE_90D_pct|MAE_180D_pct|peak_date|peak_price|current_profile_verdict|dedupe_for_aggregate|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|TRG_R13L32_009420_STAGE3GREEN_20231227|009420|Stage3-Green-comparison|2023-12-27|44300|5.53|5.53|5.53|-35.55|-35.55|-35.55|2023-12-27|46750|current_profile_correct|False|
|TRG_R13L32_039200_4C_20210107|039200|4C-thesis-break-watch|2021-01-07|51000|5.88|5.88|5.88|-25.88|-39.12|-39.12|2021-01-07|54000|current_profile_4C_too_late|False|
|TRG_R13L32_298380_4B_20220121|298380|4B-overlay|2022-01-21|33050|5.3|5.3|5.3|-26.48|-41.91|-48.41|2022-01-21|34800|current_profile_correct|False|

## 13. Current Calibrated Profile Stress Test

### 한올바이오파마 — current_profile_correct

The current calibrated profile should keep the case around high Stage2 / Yellow rather than Green. The 90D MFE of +43.19% validates that the event was not noise, but the drawdown after the 2023-12-27 peak was -38.93%, so a Green label without a durable revision bridge would be too loose.

### 오스코텍 — current_profile_correct with high-MAE caution

The current profile should allow Stage2/Yellow because the 90D/180D MFE was +55.43%. The same row carries -16.09% 90D MAE and -32.50% 180D MAE, which says the bio data event behaves like a live animal, not a fixed coupon. Green strictness remains appropriate.

### 신라젠 — current_profile_4C_too_late

A hard futility / thesis-break route must override price-only hope immediately. MFE remained 0.00% while the 90D/180D MAE reached -74.94% from the already-damaged entry close.

### 에이비엘바이오 — current_profile_false_positive

The partner headline produced +33.08% MFE, but the same event premium later decayed into -26.58% 90D MAE and -27.92% 180D MAE. C24 should not let a license headline masquerade as confirmed clinical data.

## 14. Stage2 / Yellow / Green Comparison

```text
HanAll Stage2 entry = 2023-09-27 close 32650
HanAll Stage3-Green comparison entry = 2023-12-27 close 44300
cycle peak after Stage2 = 46750
green_lateness_ratio = 0.826
```

Interpretation: Green caught the story after most of the upside had already been priced. This is not an argument to lower Green globally. It is an argument to treat C24 data events as Stage2/Yellow when the evidence is real but not yet commercially durable.

```text
Oscotec Stage2 entry = 2020-09-21 close 46000
cycle peak after Stage2 = 71500
green_lateness_ratio = not_applicable
reason = no clean confirmed Stage3-Green trigger before later thesis-quality downgrade
```

## 15. 4B Local vs Full-window Timing Audit

For 에이비엘바이오, the 4B overlay is well behaved:

```text
Stage2_Actionable_entry_price = 26150
Stage4B_entry_price = 33050
local_peak_price_after_Stage2 = 34800
full_window_peak_price_after_Stage2 = 34800
four_b_local_peak_proximity = 0.798
four_b_full_window_peak_proximity = 0.798
four_b_timing_verdict = good_full_window_4B_timing_for_event_cap
four_b_evidence_type = valuation_blowoff; positioning_overheat; explicit_event_cap
```

The key is that 4B is an overlay, not a positive-stage promotion. ABL’s partner headline should create risk-budget pressure near the event peak, not a new Green label.

## 16. 4C Protection Audit

| case | 4C trigger | label | protection interpretation |
|---|---|---|---|
| 신라젠 | TRG_R13L32_215600_4C_20190802 | hard_4c_success_but_gap_damaged | The hard break still protects from further collapse, but the entry row itself is already gap-damaged. |
| 오스코텍 | TRG_R13L32_039200_4C_20210107 | hard_4c_late | 4C after the prior peak catches thesis deterioration late; useful as a protection label, not as entry calibration. |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = l7_high_MAE_positive_tolerance_requires_size_control
proposal = Add an L7 shadow overlay that allows Stage2/Yellow for real clinical-data events even when MAE is high, but forces risk-size and 4B/4C monitoring rather than Green promotion.
confidence = low_to_medium
production_scoring_changed = false
```

Rationale: biotech data events are allowed to breathe. A good Stage2 may still shake violently. The shadow rule should avoid turning volatility into automatic rejection, but it should also refuse to let volatility plus headline become Green.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
new_axis_proposed = c24_clinical_data_quality_gate; c24_partner_headline_not_green; c24_hard_trial_failure_to_4C
confidence = medium
production_scoring_changed = false
```

Rule candidate:

```text
if C24 and evidence is true clinical-data/partner-backed data:
    allow Stage2/Yellow if public event + partner/customer quality + relative strength exist
    require durable revision/commercial bridge before Green

if C24 and event is partner/license headline without independent clinical proof:
    cap at guarded Stage2 or 4B overlay
    do not promote to Green on price action alone

if C24 and event is trial failure/futility/regulatory clinical rejection:
    route to hard 4C regardless of price-only rebound potential
```

## 19. Before / After Backtest Comparison

|profile_id|profile_scope|changed_axes|eligible_trigger_count|avg_MFE_90D_pct|avg_MAE_90D_pct|false_positive_rate|late_green_count|score_return_alignment_verdict|
|---|---|---|---|---|---|---|---|---|
|P0_e2r_2_1_stock_web_calibrated_proxy|current_proxy|none|4|32.92|-32.54|1/4|1|mixed_but_directionally_correct|
|P0b_e2r_2_0_baseline_reference|rollback_reference|rollback|4|32.92|-32.54|2/4|1|worse_false_positive_control|
|P1_L7_C24_sector_specific_candidate_profile|sector_specific|l7_binary_trial_event_risk_penalty +1 risk; approval_or_partner_quality_gate +1|4|32.92|-32.54|0.5/4|1|best_guarded_alignment|
|P2_C24_canonical_archetype_candidate_profile|canonical_archetype_specific|c24_clinical_data_quality_gate; c24_partner_headline_not_green; c24_hard_trial_failure_to_4C|4|32.92|-32.54|0.5/4|1|best_canonical_alignment|
|P3_C24_counterexample_guard_profile|canonical_archetype_specific_guard|headline_only_event_cap; hard_negative_data_override|4|32.92|-32.54|0/4 for Green|1|strong_counterexample_control|

## 20. Score-Return Alignment Matrix

| case_id | P0 label | proposed shadow label | MFE_90D_pct | MAE_90D_pct | alignment verdict |
|---|---|---|---:|---:|---|
| R13L32_C24_009420_HANALL_20230927_PARTNER_DATA_POSITIVE | Stage2/Yellow | Stage3-Yellow-watch | 43.19 | -12.56 | positive but not Green-safe |
| R13L32_C24_039200_OSCOTEC_20200921_DATA_POSITIVE_HIGH_MAE | Stage3-Yellow | Stage3-Yellow-high-MAE | 55.43 | -16.09 | positive, risk overlay needed |
| R13L32_C24_215600_SILLAJEN_20190802_PHASE3_FUTILITY_4C | 4C | hard_4C | 0.00 | -74.94 | hard 4C alignment |
| R13L32_C24_298380_ABL_20220112_LICENSE_EVENT_FALSE_POSITIVE | Stage3-Yellow-risk | guarded Stage2 / 4B overlay | 33.08 | -26.58 | false-positive Green risk reduced |

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|_4B_case_count|_4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|L7_BIO_HEALTHCARE_MEDICAL|C24_BIO_TRIAL_DATA_EVENT_RISK|BIO_TRIAL_DATA_EVENT_BINARY_OUTCOME_GATED_BY_PARTNER_AND_COMMERCIAL_BRIDGE|2|2|1|2|4|0|7|4|2|True|True|C24 still needs more device-like diagnostic trial cases and ex-Korea approval/data readouts, but partner-headline false-positive coverage is improved.|

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus; stage3_yellow_total_min; stage3_green_total_min; stage3_green_revision_min; price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c
residual_error_types_found: partner_headline_false_positive; hard_trial_failure_gap_damaged_4C; high_MAE_positive_event_case; late_green_after_event_peak
new_axis_proposed: c24_clinical_data_quality_gate; c24_partner_headline_not_green; c24_hard_trial_failure_to_4C; l7_high_MAE_positive_tolerance_requires_size_control
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus; stage3_yellow_total_min; stage3_green_total_min; stage3_green_revision_min; stage3_cross_evidence_green_buffer
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Stock-Web manifest and shard basis
- Symbol profile availability and corporate-action candidate windows
- Actual 1D OHLC entry rows
- MFE/MAE/peak/drawdown calculations over 30D/90D/180D windows
- representative trigger dedupe
- current calibrated profile stress-test labels
```

Not validated:

```text
- No stock_agent source code was opened
- No production scoring patch was written
- No live scan was performed
- No brokerage/API execution was used
- External event timestamps were treated conservatively as historical public-event proxies rather than intraday audit records
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c24_clinical_data_quality_gate,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,0,1,+1,Partner-backed clinical data should remain Stage2/Yellow unless durable revision or commercialization bridge confirms it.,Reduced false Green risk while preserving HanAll/Oscotec Stage2 positives.,TRG_R13L32_009420_STAGE2_20230927|TRG_R13L32_039200_STAGE2_20200921,4,4,2,medium,archetype_shadow_only,not production; post-calibrated residual
shadow_weight,c24_partner_headline_not_green,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,0,1,+1,License/headline/optionality without clinical proof created ABL false-positive risk.,Downgrades event-premium-only cases from Yellow/Green toward guarded Stage2.,TRG_R13L32_298380_STAGE2_20220112,4,4,2,medium,archetype_shadow_only,not production; post-calibrated residual
shadow_weight,c24_hard_trial_failure_to_4C,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,1,2,+1,Hard trial-futility events should immediately override positive labels even when price has already gapped.,Improves 4C routing for ShinlaJen-like thesis break.,TRG_R13L32_215600_4C_20190802,4,4,2,high,archetype_shadow_only,strengthens existing hard_4c_thesis_break_routes_to_4c
shadow_weight,l7_high_MAE_positive_tolerance_requires_size_control,sector_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,0,1,+1,Successful bio data events can have high MAE; use position/risk overlay rather than blocking Stage2 entirely.,Keeps Oscotec/HanAll positives while refusing early Green.,TRG_R13L32_039200_STAGE2_20200921|TRG_R13L32_009420_STAGE2_20230927,4,4,2,low,sector_shadow_only,risk overlay only; not a promotion rule
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R13L32_C24_009420_HANALL_20230927_PARTNER_DATA_POSITIVE","symbol":"009420","company_name":"한올바이오파마","round":"R13","loop":"32","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_TRIAL_DATA_EVENT_BINARY_OUTCOME_GATED_BY_PARTNER_AND_COMMERCIAL_BRIDGE","case_type":"stage2_promote_candidate","positive_or_counterexample":"positive","best_trigger":"TRG_R13L32_009420_STAGE2_20230927","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_alignment","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Partner-backed FcRn clinical data created a real but non-Green-safe rerating path; upside existed, but the later drawdown shows why C24 should remain event-gated until durable revision/commercial route is visible."}
{"row_type":"case","case_id":"R13L32_C24_039200_OSCOTEC_20200921_DATA_POSITIVE_HIGH_MAE","symbol":"039200","company_name":"오스코텍","round":"R13","loop":"32","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_TRIAL_DATA_EVENT_BINARY_OUTCOME_GATED_BY_PARTNER_AND_COMMERCIAL_BRIDGE","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"TRG_R13L32_039200_STAGE2_20200921","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_alignment","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Trial-data/event evidence produced large MFE, but the subsequent data-disappointment/drawdown makes Green strictness appropriate rather than a reason to loosen the global Green threshold."}
{"row_type":"case","case_id":"R13L32_C24_215600_SILLAJEN_20190802_PHASE3_FUTILITY_4C","symbol":"215600","company_name":"신라젠","round":"R13","loop":"32","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_TRIAL_DATA_EVENT_BINARY_OUTCOME_GATED_BY_PARTNER_AND_COMMERCIAL_BRIDGE","case_type":"4C_success","positive_or_counterexample":"counterexample","best_trigger":"TRG_R13L32_215600_4C_20190802","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_alignment","current_profile_verdict":"current_profile_4C_too_late","price_source":"Songdaiki/stock-web","notes":"Phase-3 futility/thesis break is a hard C24 4C archetype: the entry row itself is already gap-damaged and further drawdown remains severe."}
{"row_type":"case","case_id":"R13L32_C24_298380_ABL_20220112_LICENSE_EVENT_FALSE_POSITIVE","symbol":"298380","company_name":"에이비엘바이오","round":"R13","loop":"32","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_TRIAL_DATA_EVENT_BINARY_OUTCOME_GATED_BY_PARTNER_AND_COMMERCIAL_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TRG_R13L32_298380_STAGE2_20220112","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_alignment","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"A large partner/licensing event generated early MFE but did not behave like durable clinical-data confirmation; it is a useful guard against treating all partner headlines as Stage3 clinical proof."}
{"round":"R13","loop":"32","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_TRIAL_DATA_EVENT_BINARY_OUTCOME_GATED_BY_PARTNER_AND_COMMERCIAL_BRIDGE","sector":"바이오·헬스케어·의료기기","primary_archetype":"bio_trial_data_event_risk","loop_objective":"holdout_validation;residual_false_positive_mining;residual_missed_structural_mining;yellow_threshold_stress_test;green_strictness_stress_test;stage2_actionable_bonus_stress_test;4B_non_price_requirement_stress_test;4C_thesis_break_timing_test;sector_specific_rule_discovery;canonical_archetype_compression;counterexample_mining;coverage_gap_fill","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","row_type":"trigger","trigger_id":"TRG_R13L32_009420_STAGE2_20230927","case_id":"R13L32_C24_009420_HANALL_20230927_PARTNER_DATA_POSITIVE","symbol":"009420","company_name":"한올바이오파마","trigger_type":"Stage2-Actionable","trigger_date":"2023-09-27","entry_date":"2023-09-27","entry_price":32650,"evidence_available_at_that_date":"Partner-backed clinical data/event became visible; treated as same-date close because the stock-web row already reflects the event move.","evidence_source":"historical public partner clinical-data event proxy; stock-web OHLC verified in 009/009420/2023.csv and 2024.csv","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/009/009420/2023.csv","profile_path":"atlas/symbol_profiles/009/009420.json","MFE_30D_pct":21.75,"MFE_90D_pct":43.19,"MFE_180D_pct":43.19,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.4,"MAE_90D_pct":-12.56,"MAE_180D_pct":-12.56,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-12-27","peak_price":46750,"drawdown_after_peak_pct":-38.93,"green_lateness_ratio":0.826,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_primary_4B_row","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_stage2_but_green_should_wait","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_R13L32_009420_20230927","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"round":"R13","loop":"32","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_TRIAL_DATA_EVENT_BINARY_OUTCOME_GATED_BY_PARTNER_AND_COMMERCIAL_BRIDGE","sector":"바이오·헬스케어·의료기기","primary_archetype":"bio_trial_data_event_risk","loop_objective":"holdout_validation;residual_false_positive_mining;residual_missed_structural_mining;yellow_threshold_stress_test;green_strictness_stress_test;stage2_actionable_bonus_stress_test;4B_non_price_requirement_stress_test;4C_thesis_break_timing_test;sector_specific_rule_discovery;canonical_archetype_compression;counterexample_mining;coverage_gap_fill","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","row_type":"trigger","trigger_id":"TRG_R13L32_009420_STAGE3GREEN_20231227","case_id":"R13L32_C24_009420_HANALL_20230927_PARTNER_DATA_POSITIVE","symbol":"009420","company_name":"한올바이오파마","trigger_type":"Stage3-Green-comparison","trigger_date":"2023-12-27","entry_date":"2023-12-27","entry_price":44300,"evidence_available_at_that_date":"The late confirmation/price-recognition point is compared against the earlier data-event entry.","evidence_source":"stock-web OHLC comparison row; clinical-data confirmation proxy","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":["confirmed_revision","multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/009/009420/2023.csv","profile_path":"atlas/symbol_profiles/009/009420.json","MFE_30D_pct":5.53,"MFE_90D_pct":5.53,"MFE_180D_pct":5.53,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-35.55,"MAE_90D_pct":-35.55,"MAE_180D_pct":-35.55,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-12-27","peak_price":46750,"drawdown_after_peak_pct":-38.93,"green_lateness_ratio":0.826,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"green_confirmation_late_vs_stage2","four_b_evidence_type":["valuation_blowoff"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"late_green_comparison_only","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_R13L32_009420_20231227","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":"same case label comparison","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"round":"R13","loop":"32","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_TRIAL_DATA_EVENT_BINARY_OUTCOME_GATED_BY_PARTNER_AND_COMMERCIAL_BRIDGE","sector":"바이오·헬스케어·의료기기","primary_archetype":"bio_trial_data_event_risk","loop_objective":"holdout_validation;residual_false_positive_mining;residual_missed_structural_mining;yellow_threshold_stress_test;green_strictness_stress_test;stage2_actionable_bonus_stress_test;4B_non_price_requirement_stress_test;4C_thesis_break_timing_test;sector_specific_rule_discovery;canonical_archetype_compression;counterexample_mining;coverage_gap_fill","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","row_type":"trigger","trigger_id":"TRG_R13L32_039200_STAGE2_20200921","case_id":"R13L32_C24_039200_OSCOTEC_20200921_DATA_POSITIVE_HIGH_MAE","symbol":"039200","company_name":"오스코텍","trigger_type":"Stage2-Actionable","trigger_date":"2020-09-21","entry_date":"2020-09-21","entry_price":46000,"evidence_available_at_that_date":"Clinical data / oncology event evidence became market-visible; same-date close used because event reaction is visible in the stock-web row.","evidence_source":"historical public oncology data-event proxy; stock-web OHLC verified in 039/039200/2020.csv and 2021.csv","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","customer_or_order_quality","early_revision_signal"],"stage3_evidence_fields":["multiple_public_sources","durable_customer_confirmation"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/039/039200/2020.csv","profile_path":"atlas/symbol_profiles/039/039200.json","MFE_30D_pct":16.3,"MFE_90D_pct":55.43,"MFE_180D_pct":55.43,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-16.09,"MAE_90D_pct":-16.09,"MAE_180D_pct":-32.5,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2020-12-08","peak_price":71500,"drawdown_after_peak_pct":-56.57,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_primary_4B_row","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE_high_MAE_event_case","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_R13L32_039200_20200921","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"round":"R13","loop":"32","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_TRIAL_DATA_EVENT_BINARY_OUTCOME_GATED_BY_PARTNER_AND_COMMERCIAL_BRIDGE","sector":"바이오·헬스케어·의료기기","primary_archetype":"bio_trial_data_event_risk","loop_objective":"holdout_validation;residual_false_positive_mining;residual_missed_structural_mining;yellow_threshold_stress_test;green_strictness_stress_test;stage2_actionable_bonus_stress_test;4B_non_price_requirement_stress_test;4C_thesis_break_timing_test;sector_specific_rule_discovery;canonical_archetype_compression;counterexample_mining;coverage_gap_fill","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","row_type":"trigger","trigger_id":"TRG_R13L32_039200_4C_20210107","case_id":"R13L32_C24_039200_OSCOTEC_20200921_DATA_POSITIVE_HIGH_MAE","symbol":"039200","company_name":"오스코텍","trigger_type":"4C-thesis-break-watch","trigger_date":"2021-01-07","entry_date":"2021-01-07","entry_price":51000,"evidence_available_at_that_date":"Post-peak data disappointment / thesis-quality downgrade point; used only as 4C protection comparison, not aggregate entry.","evidence_source":"stock-web OHLC row verified in 039/039200/2021.csv; clinical-data disappointment proxy","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/039/039200/2021.csv","profile_path":"atlas/symbol_profiles/039/039200.json","MFE_30D_pct":5.88,"MFE_90D_pct":5.88,"MFE_180D_pct":5.88,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-25.88,"MAE_90D_pct":-39.12,"MAE_180D_pct":-39.12,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-01-07","peak_price":54000,"drawdown_after_peak_pct":-42.5,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"4C_watch_after_prior_peak_late","four_b_evidence_type":["revision_slowdown","legal_or_regulatory_block"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"4C_late_after_large_prior_MFE","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_R13L32_039200_20210107","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":true,"reuse_reason":"same case 4C overlay","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"round":"R13","loop":"32","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_TRIAL_DATA_EVENT_BINARY_OUTCOME_GATED_BY_PARTNER_AND_COMMERCIAL_BRIDGE","sector":"바이오·헬스케어·의료기기","primary_archetype":"bio_trial_data_event_risk","loop_objective":"holdout_validation;residual_false_positive_mining;residual_missed_structural_mining;yellow_threshold_stress_test;green_strictness_stress_test;stage2_actionable_bonus_stress_test;4B_non_price_requirement_stress_test;4C_thesis_break_timing_test;sector_specific_rule_discovery;canonical_archetype_compression;counterexample_mining;coverage_gap_fill","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","row_type":"trigger","trigger_id":"TRG_R13L32_215600_4C_20190802","case_id":"R13L32_C24_215600_SILLAJEN_20190802_PHASE3_FUTILITY_4C","symbol":"215600","company_name":"신라젠","trigger_type":"4C-hard-thesis-break","trigger_date":"2019-08-02","entry_date":"2019-08-02","entry_price":31200,"evidence_available_at_that_date":"Phase-3 futility / trial-continuation thesis break; same-date close is used because the market gap is already reflected in the tradable row.","evidence_source":"historical phase-3 futility event proxy; stock-web OHLC verified in 215/215600/2019.csv","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","price_only_local_peak"],"stage4c_evidence_fields":["safety_or_trial_failure","thesis_evidence_broken"],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/215/215600/2019.csv","profile_path":"atlas/symbol_profiles/215/215600.json","MFE_30D_pct":0.0,"MFE_90D_pct":0.0,"MFE_180D_pct":0.0,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-71.15,"MAE_90D_pct":-74.94,"MAE_180D_pct":-74.94,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2019-08-02","peak_price":31200,"drawdown_after_peak_pct":-74.94,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"hard_4C_overrides_4B","four_b_evidence_type":["valuation_blowoff","price_only"],"four_c_protection_label":"hard_4c_success_but_gap_damaged","trigger_outcome_label":"trial_failure_hard_4C","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_R13L32_215600_20190802","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"round":"R13","loop":"32","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_TRIAL_DATA_EVENT_BINARY_OUTCOME_GATED_BY_PARTNER_AND_COMMERCIAL_BRIDGE","sector":"바이오·헬스케어·의료기기","primary_archetype":"bio_trial_data_event_risk","loop_objective":"holdout_validation;residual_false_positive_mining;residual_missed_structural_mining;yellow_threshold_stress_test;green_strictness_stress_test;stage2_actionable_bonus_stress_test;4B_non_price_requirement_stress_test;4C_thesis_break_timing_test;sector_specific_rule_discovery;canonical_archetype_compression;counterexample_mining;coverage_gap_fill","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","row_type":"trigger","trigger_id":"TRG_R13L32_298380_STAGE2_20220112","case_id":"R13L32_C24_298380_ABL_20220112_LICENSE_EVENT_FALSE_POSITIVE","symbol":"298380","company_name":"에이비엘바이오","trigger_type":"Stage2-Actionable-false-positive","trigger_date":"2022-01-12","entry_date":"2022-01-12","entry_price":26150,"evidence_available_at_that_date":"Large partner/licensing event became public and price-reactive, but the evidence was not clinical-data confirmation nor durable financial visibility.","evidence_source":"historical partner/licensing event proxy; stock-web OHLC verified in 298/298380/2022.csv","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["explicit_event_cap","valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/298/298380/2022.csv","profile_path":"atlas/symbol_profiles/298/298380.json","MFE_30D_pct":33.08,"MFE_90D_pct":33.08,"MFE_180D_pct":33.08,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-8.99,"MAE_90D_pct":-26.58,"MAE_180D_pct":-27.92,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-01-21","peak_price":34800,"drawdown_after_peak_pct":-45.83,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.798,"four_b_full_window_peak_proximity":0.798,"four_b_timing_verdict":"good_event_cap_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","explicit_event_cap"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"event_premium_failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_R13L32_298380_20220112","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"round":"R13","loop":"32","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_TRIAL_DATA_EVENT_BINARY_OUTCOME_GATED_BY_PARTNER_AND_COMMERCIAL_BRIDGE","sector":"바이오·헬스케어·의료기기","primary_archetype":"bio_trial_data_event_risk","loop_objective":"holdout_validation;residual_false_positive_mining;residual_missed_structural_mining;yellow_threshold_stress_test;green_strictness_stress_test;stage2_actionable_bonus_stress_test;4B_non_price_requirement_stress_test;4C_thesis_break_timing_test;sector_specific_rule_discovery;canonical_archetype_compression;counterexample_mining;coverage_gap_fill","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","row_type":"trigger","trigger_id":"TRG_R13L32_298380_4B_20220121","case_id":"R13L32_C24_298380_ABL_20220112_LICENSE_EVENT_FALSE_POSITIVE","symbol":"298380","company_name":"에이비엘바이오","trigger_type":"4B-overlay","trigger_date":"2022-01-21","entry_date":"2022-01-21","entry_price":33050,"evidence_available_at_that_date":"Local event-premium blowoff after a partner headline; marked as risk overlay, not as full thesis break.","evidence_source":"stock-web OHLC row verified in 298/298380/2022.csv; event-premium exhaustion proxy","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","explicit_event_cap"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/298/298380/2022.csv","profile_path":"atlas/symbol_profiles/298/298380.json","MFE_30D_pct":5.3,"MFE_90D_pct":5.3,"MFE_180D_pct":5.3,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-26.48,"MAE_90D_pct":-41.91,"MAE_180D_pct":-48.41,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-01-21","peak_price":34800,"drawdown_after_peak_pct":-45.83,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.798,"four_b_full_window_peak_proximity":0.798,"four_b_timing_verdict":"good_full_window_4B_timing_for_event_cap","four_b_evidence_type":["valuation_blowoff","positioning_overheat","explicit_event_cap"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_R13L32_298380_20220121","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":"same case 4B overlay","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L32_C24_009420_HANALL_20230927_PARTNER_DATA_POSITIVE","trigger_id":"TRG_R13L32_009420_STAGE2_20230927","symbol":"009420","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","raw_component_scores_before":{"contract_score":25,"backlog_visibility_score":10,"margin_bridge_score":20,"revision_score":45,"relative_strength_score":68,"customer_quality_score":72,"policy_or_regulatory_score":78,"valuation_repricing_score":54,"execution_risk_score":45,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable-high","raw_component_scores_after":{"contract_score":25,"backlog_visibility_score":10,"margin_bridge_score":20,"revision_score":50,"relative_strength_score":68,"customer_quality_score":76,"policy_or_regulatory_score":82,"valuation_repricing_score":54,"execution_risk_score":42,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":77,"stage_label_after":"Stage3-Yellow-watch","changed_components":["policy_or_regulatory_score","customer_quality_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"C24 separates true clinical-data confirmation from partner/headline optionality, adds binary-failure 4C routing, and requires durable revision/commercial bridge before Green promotion.","MFE_90D_pct":43.19,"MAE_90D_pct":-12.56,"score_return_alignment_label":"positive_alignment_but_not_green","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L32_C24_039200_OSCOTEC_20200921_DATA_POSITIVE_HIGH_MAE","trigger_id":"TRG_R13L32_039200_STAGE2_20200921","symbol":"039200","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","raw_component_scores_before":{"contract_score":35,"backlog_visibility_score":5,"margin_bridge_score":25,"revision_score":48,"relative_strength_score":70,"customer_quality_score":75,"policy_or_regulatory_score":82,"valuation_repricing_score":62,"execution_risk_score":55,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":5,"margin_bridge_score":25,"revision_score":52,"relative_strength_score":70,"customer_quality_score":80,"policy_or_regulatory_score":84,"valuation_repricing_score":62,"execution_risk_score":58,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":78,"stage_label_after":"Stage3-Yellow-high-MAE","changed_components":["customer_quality_score","revision_score","execution_risk_score"],"component_delta_explanation":"C24 separates true clinical-data confirmation from partner/headline optionality, adds binary-failure 4C routing, and requires durable revision/commercial bridge before Green promotion.","MFE_90D_pct":55.43,"MAE_90D_pct":-16.09,"score_return_alignment_label":"positive_alignment_high_MAE","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L32_C24_215600_SILLAJEN_20190802_PHASE3_FUTILITY_4C","trigger_id":"TRG_R13L32_215600_4C_20190802","symbol":"215600","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":10,"customer_quality_score":0,"policy_or_regulatory_score":-90,"valuation_repricing_score":15,"execution_risk_score":100,"legal_or_contract_risk_score":80,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":28,"stage_label_before":"4C","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":-100,"valuation_repricing_score":0,"execution_risk_score":100,"legal_or_contract_risk_score":90,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":18,"stage_label_after":"hard_4C","changed_components":["policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"C24 separates true clinical-data confirmation from partner/headline optionality, adds binary-failure 4C routing, and requires durable revision/commercial bridge before Green promotion.","MFE_90D_pct":0.0,"MAE_90D_pct":-74.94,"score_return_alignment_label":"hard_4C_alignment","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L32_C24_298380_ABL_20220112_LICENSE_EVENT_FALSE_POSITIVE","trigger_id":"TRG_R13L32_298380_STAGE2_20220112","symbol":"298380","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","raw_component_scores_before":{"contract_score":52,"backlog_visibility_score":15,"margin_bridge_score":25,"revision_score":35,"relative_strength_score":70,"customer_quality_score":86,"policy_or_regulatory_score":55,"valuation_repricing_score":62,"execution_risk_score":45,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow-risk","raw_component_scores_after":{"contract_score":48,"backlog_visibility_score":10,"margin_bridge_score":15,"revision_score":28,"relative_strength_score":70,"customer_quality_score":75,"policy_or_regulatory_score":50,"valuation_repricing_score":45,"execution_risk_score":68,"legal_or_contract_risk_score":30,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":66,"stage_label_after":"Stage2-Actionable-guarded","changed_components":["margin_bridge_score","revision_score","customer_quality_score","valuation_repricing_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"C24 separates true clinical-data confirmation from partner/headline optionality, adds binary-failure 4C routing, and requires durable revision/commercial bridge before Green promotion.","MFE_90D_pct":33.08,"MAE_90D_pct":-26.58,"score_return_alignment_label":"false_positive_reduced","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R13","loop":"32","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"new_trigger_family_count":4,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["partner_headline_false_positive","hard_trial_failure_gap_damaged_4C","high_MAE_positive_event_case","late_green_after_event_peak"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
next_round = R13_loop_33
suggested_large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
suggested_canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
reason = after C23 approval/commercialization and C24 clinical-data event risk, the remaining L7 gap is device/export/reimbursement durability.
```

## 28. Source Notes

Stock-Web files inspected for this loop:

```text
atlas/manifest.json
atlas/symbol_profiles/009/009420.json
atlas/symbol_profiles/039/039200.json
atlas/symbol_profiles/215/215600.json
atlas/symbol_profiles/298/298380.json
atlas/ohlcv_tradable_by_symbol_year/009/009420/2023.csv
atlas/ohlcv_tradable_by_symbol_year/009/009420/2024.csv
atlas/ohlcv_tradable_by_symbol_year/039/039200/2020.csv
atlas/ohlcv_tradable_by_symbol_year/039/039200/2021.csv
atlas/ohlcv_tradable_by_symbol_year/215/215600/2019.csv
atlas/ohlcv_tradable_by_symbol_year/298/298380/2022.csv
```

All prices are raw/unadjusted stock-web tradable rows and should be interpreted only for historical calibration, not for investment recommendation.
