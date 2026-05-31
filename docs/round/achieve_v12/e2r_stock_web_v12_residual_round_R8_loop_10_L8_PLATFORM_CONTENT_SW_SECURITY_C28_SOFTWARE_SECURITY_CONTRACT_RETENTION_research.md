# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session: post_calibrated_sector_archetype_residual_research
scheduled_round: R8
scheduled_loop: 10
round_schedule_status: valid
round_sector_consistency: pass
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id: B2B_SOFTWARE_SECURITY_RECURRING_CONTRACT_RETENTION_MARGIN_BRIDGE
output_file: e2r_stock_web_v12_residual_round_R8_loop_10_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This loop adds 5 new independent cases, 3 counterexamples, and 3 residual errors for R8/L8_PLATFORM_CONTENT_SW_SECURITY/C28_SOFTWARE_SECURITY_CONTRACT_RETENTION.

## 1. Current Calibrated Profile Assumption

The baseline profile for stress testing is `e2r_2_1_stock_web_calibrated_proxy`. The previous profile `e2r_2_0_baseline_reference` is used only as rollback/reference. This file does not re-propose already-applied global axes. It tests how those axes behave in C28, where the trap is that many “software” names are actually AI-theme, election/control-premium, or one-off remote-work demand stories rather than retained recurring software contracts.

Current global axes tested:

```text
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

## 2. Round / Large Sector / Canonical Archetype Scope

- Round: `R8`
- Large sector: `L8_PLATFORM_CONTENT_SW_SECURITY`
- Canonical archetype: `C28_SOFTWARE_SECURITY_CONTRACT_RETENTION`
- Fine archetype: `B2B_SOFTWARE_SECURITY_RECURRING_CONTRACT_RETENTION_MARGIN_BRIDGE`
- Loop objectives: `coverage_gap_fill`, `counterexample_mining`, `green_strictness_stress_test`, `4B_non_price_requirement_stress_test`, `canonical_archetype_compression`

C28 is not “all AI software” and not “all security labels.” For this archetype, the durable mechanism is recurring contract retention: enterprise accounts, renewal, ARR/RPO-like backlog, customer quality, and margin leverage. Price can shout, but C28 requires the ledger to answer.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifact checked: `reports/e2r_calibration/by_round/R8.md`. It shows R8 already has 104 representative triggers and 27 unique cases with Stage2, Stage3, 4B, and 4C coverage. The accepted axes are cumulative/global, so this loop avoids repeating the global point and instead contributes a C28-specific split between real recurring-contract software and event/AI/security-label false positives.

Novelty gate:

```text
scheduled_round = R8
scheduled_loop = 10
wrong_round_penalty = 0
minimum_new_independent_case_ratio = 1.00
new_symbol_count = 5
new_trigger_family_count = 4
positive_case_count = 2
counterexample_count = 3
current_profile_error_count = 3
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest fields used:

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

Schema confirmation:

```text
tradable columns = d,o,h,l,c,v,a,mc,s,m
raw columns = d,o,h,l,c,v,a,mc,s,m,rs
calibration_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
```

## 5. Historical Eligibility Gate

All representative triggers use `Songdaiki/stock-web` tradable shards, have at least 180 forward trading days available by manifest max date, and have no corporate-action candidate date overlapping the 180D window.

| symbol | profile path | entry date | 180D usable | corporate-action window status |
|---:|---|---|---|---|
| 012510 | `atlas/symbol_profiles/012/012510.json` | 2024-02-05 | true | clean_180D_window |
| 263860 | `atlas/symbol_profiles/263/263860.json` | 2023-05-17 | true | clean_180D_window |
| 030520 | `atlas/symbol_profiles/030/030520.json` | 2024-01-10 | true | clean_180D_window |
| 053800 | `atlas/symbol_profiles/053/053800.json` | 2022-03-11 | true | clean_180D_window |
| 131370 | `atlas/symbol_profiles/131/131370.json` | 2020-03-11 | true | clean_180D_window |

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression rule |
|---|---|---|
| B2B_SOFTWARE_SECURITY_RECURRING_CONTRACT_RETENTION_MARGIN_BRIDGE | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | Keep when revenue visibility is tied to enterprise retention, account expansion, maintenance/subscription, or repeat contract conversion. |
| AI_OFFICE_PLATFORM_OPTION_WITHOUT_RETENTION_PROOF | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | Cap at Stage2/watch until retained customer and margin bridge evidence appears. |
| CYBER_SECURITY_LABEL_POLITICAL_CONTROL_PREMIUM | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | Treat as event/control-premium overlay, not positive C28 Green evidence. |
| REMOTE_WORK_EMERGENCY_DEMAND_PULL_FORWARD | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | Treat as Stage2 event until post-shock renewal/ARR durability is observed. |

## 7. Case Selection Summary

| case_id | symbol | company | role | core reason |
|---|---:|---|---|---|
| R8L10_C28_CASE_001_DOUZONE_2024_CLOUD_ERP_AI_CONTRACT | 012510 | 더존비즈온 | positive | Recurring B2B ERP/cloud/AI software bridge had durable contract quality and later margin/rerating support. |
| R8L10_C28_CASE_002_GENIANS_2023_SECURITY_RETENTION | 263860 | 지니언스 | positive | Security software account-retention proxy and margin leverage gave a cleaner C28 path. |
| R8L10_C28_CASE_003_HANCOM_2024_AI_OFFICE_FALSE_GREEN | 030520 | 한글과컴퓨터 | counterexample | AI office/platform optionality produced a violent move before recurring contract evidence. |
| R8L10_C28_CASE_004_AHNLAB_2022_CONTROL_PREMIUM_PRICE_ONLY | 053800 | 안랩 | counterexample | Security label was overwhelmed by political/control-premium flow. |
| R8L10_C28_CASE_005_RSUPPORT_2020_REMOTE_WORK_ONE_OFF | 131370 | 알서포트 | counterexample / 4B | Emergency remote-work demand had huge MFE but needed one-off demand and normalization guard. |

## 8. Positive vs Counterexample Balance

```text
positive_structural_success = 2
counterexample_or_failed_rerating = 3
4B_or_4C_case = 2
calibration_usable_case_count = 5
minimum_positive_case_count = pass
minimum_counterexample_count = pass
```

## 9. Evidence Source Map

Evidence is treated as historical research proxy evidence, not production ingestion. The only quantitative input used for calibration metrics is stock-web OHLC. The evidence labels are intentionally conservative:

- `retained_contract_customer_quality`: recurring B2B/customer account evidence needed for C28 Stage3.
- `AI_or_security_label_only`: Stage2/watch unless supported by contract-retention proof.
- `event_or_control_premium`: 4B/event overlay, never C28 Green support.
- `one_off_emergency_demand`: Stage2 event; requires renewal/ARR proof before Green.

## 10. Price Data Source Map

| symbol | tradable shard | profile |
|---:|---|---|
| 012510 | `atlas/ohlcv_tradable_by_symbol_year/012/012510/2024.csv` | `atlas/symbol_profiles/012/012510.json` |
| 263860 | `atlas/ohlcv_tradable_by_symbol_year/263/263860/2023.csv` | `atlas/symbol_profiles/263/263860.json` |
| 030520 | `atlas/ohlcv_tradable_by_symbol_year/030/030520/2024.csv` | `atlas/symbol_profiles/030/030520.json` |
| 053800 | `atlas/ohlcv_tradable_by_symbol_year/053/053800/2022.csv` | `atlas/symbol_profiles/053/053800.json` |
| 131370 | `atlas/ohlcv_tradable_by_symbol_year/131/131370/2020.csv` | `atlas/symbol_profiles/131/131370.json` |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | role | trigger | entry | entry_price | MFE90 | MAE90 | MFE180 | MAE180 | verdict | usable |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---|---|
| `R8L10_C28_TRG_001A_DOUZONE_STAGE2_ACTIONABLE_2024_02_05` | 012510 | Stage2-Actionable | 2024-02-05 | 2024-02-05 | 46,400 | 55.2 | -10.7 | 68.8 | -10.7 | current_profile_correct | true |
| `R8L10_C28_TRG_001B_DOUZONE_4B_OVERLAY_2024_07_08` | 012510 | Stage4B | 2024-07-08 | 2024-07-08 | 75,300 | 4.0 | -38.3 | 4.0 | -38.3 | current_profile_correct | true |
| `R8L10_C28_TRG_002A_GENIANS_STAGE2_ACTIONABLE_2023_05_17` | 263860 | Stage2-Actionable | 2023-05-17 | 2023-05-17 | 11,770 | 49.6 | -12.9 | 49.6 | -22.1 | current_profile_correct | true |
| `R8L10_C28_TRG_003A_HANCOM_STAGE2_ACTIONABLE_2024_01_10` | 030520 | Stage2-Actionable | 2024-01-10 | 2024-01-10 | 24,750 | 55.4 | -20.3 | 55.4 | -22.7 | current_profile_false_positive | true |
| `R8L10_C28_TRG_004A_AHNLAB_STAGE2_WATCH_2022_03_11` | 053800 | Stage2-Watch | 2022-03-11 | 2022-03-11 | 86,500 | 152.6 | -14.2 | 152.6 | -36.0 | current_profile_false_positive | true |
| `R8L10_C28_TRG_005A_RSUPPORT_STAGE2_ACTIONABLE_2020_03_11` | 131370 | Stage2-Actionable | 2020-03-11 | 2020-03-11 | 3,390 | 206.8 | -30.0 | 597.6 | -30.0 | current_profile_4B_too_late | true |

## 12. Trigger-Level OHLC Backtest Tables

Representative trigger averages:

```text
avg_MFE_90D_pct = 103.9
avg_MAE_90D_pct = -17.6
avg_MFE_180D_pct = 184.8
avg_MAE_180D_pct = -24.3
```

The headline average MFE is intentionally inflated by counterexamples. That is the point of this loop: in C28, a giant price path can come from event premium or one-off demand rather than true recurring-contract retention. The score-return alignment must therefore look at evidence type, not only return magnitude.

## 13. Current Calibrated Profile Stress Test

| case | current profile verdict | stress result |
|---|---|---|
| 더존비즈온 | current_profile_correct | Stage2/Yellow worked; Green should wait for margin and recurring customer bridge. |
| 지니언스 | current_profile_correct | C28-specific contract/customer-quality evidence explains positive MFE. |
| 한글과컴퓨터 | current_profile_false_positive | If AI-office narrative is scored as recurring software, Green arrives too early. |
| 안랩 | current_profile_false_positive | Security label without contract retention becomes event/control-premium noise. |
| 알서포트 | current_profile_4B_too_late | One-off emergency demand needs faster normalization/4B overlay after vertical rerating. |

Answers to required stress questions:

1. Current calibrated profile would correctly block pure price-only Green, but C28 needs a stricter non-price definition of retained contract quality.
2. Positive cases align when contract/customer-quality and margin bridge are present.
3. Stage2 bonus is useful but too generous if AI/security/event labels are accepted as software evidence.
4. Yellow threshold 75 is acceptable if recurring contract evidence exists; otherwise it is too permissive.
5. Green threshold 87/revision 55 is directionally right but should require C28-specific retention evidence.
6. Price-only blowoff guard is appropriate and should be kept.
7. Full 4B non-price requirement is appropriate; for C28, non-price 4B can be demand-normalization, contract slowdown, valuation blowoff, or event/control-premium exhaustion.
8. Hard 4C routing is useful after thesis evidence breaks, but RSUPPORT-like emergency demand needs earlier 4B overlay before hard 4C.

## 14. Stage2 / Yellow / Green Comparison

C28 Stage2 can start from public product/customer/account expansion signal. C28 Yellow should require at least one bridge from narrative to revenue visibility. C28 Green should require two bridges: retained contract/customer-quality and margin/revision confirmation.

```text
C28 Stage2 = software/security product narrative + relative strength + plausible customer route
C28 Yellow = Stage2 + public customer/account/renewal/ARR-like proof
C28 Green = Yellow + margin bridge or confirmed revision + low event/control-premium risk
```

Green lateness is not the dominant residual here. The dominant residual is false Green from non-recurring software narratives.

## 15. 4B Local vs Full-window Timing Audit

| case | local proximity | full-window proximity | 4B verdict |
|---|---:|---:|---|
| 더존비즈온 | 0.95 | 0.95 | good_full_window_4B_timing after valuation/positioning evidence |
| 한글과컴퓨터 | 0.99 | 0.99 | price-only local peak; cannot be full 4B without non-price exhaustion evidence |
| 안랩 | 0.99 | 0.99 | full-window 4B only if classified as control-premium/event overlay, not C28 Green |
| 알서포트 | 0.99 | 0.99 | good 4B after emergency demand normalization risk and valuation blowoff |

## 16. 4C Protection Audit

4C is not the main proposed C28 rule. The useful finding is that 4C should not carry the burden of protecting all event/software false positives. C28 needs an earlier Green gate and 4B overlay.

```text
hard_4c_success: RSUPPORT after one-off demand normalization broke
hard_4c_late_if_misclassified_as_C28_green: AhnLab political/control-premium path
thesis_break_watch_only: Hancom AI-office optionality without retained contract proof
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
candidate = L8 recurring-revenue bridge before Green
```

Sector rule candidate:

> In L8, product/theme labels are insufficient for Stage3-Green. Green requires evidence that traffic/product/security/AI usage converts into monetized recurring revenue, retained enterprise contracts, or repeat IP/software revenue with margin leverage.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
candidate = C28 retained-contract/customer-quality Green bridge
```

Proposed C28 shadow rule:

```text
if canonical_archetype_id == C28_SOFTWARE_SECURITY_CONTRACT_RETENTION:
    require one of:
      - renewal / retention / ARR-like contract evidence
      - enterprise customer expansion with repeat revenue proof
      - security software account expansion plus margin bridge
    cap at Stage2/watch if evidence is only:
      - AI product narrative
      - cybersecurity theme
      - political/control-premium flow
      - one-off emergency remote-work demand
```

## 19. Before / After Backtest Comparison

| profile | scope | hypothesis | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | global | Current global calibrated profile | 5 | 103.9 | -17.6 | 0.60 | Good global guard, but C28 false-Green risk remains. |
| P0b e2r_2_0_baseline_reference | global reference | Earlier looser profile | 5 | 103.9 | -17.6 | 0.80 | Too vulnerable to AI/security/event price moves. |
| P1 L8 sector candidate | sector | Require monetization/recurring bridge in L8 | 5 | 49.5 | -11.8 | 0.40 | Better. |
| P2 C28 candidate | canonical | Require retained contract/customer-quality + margin bridge | 5 | 52.4 | -11.8 | 0.20 | Best score-return alignment. |
| P3 counterexample guard | canonical guard | Cap event/control/one-off demand at Stage2/watch | 3 | 138.3 | -24.7 | 0.00 | Good guardrail; not a positive promotion rule. |

## 20. Score-Return Alignment Matrix

| symbol | current profile | C28 shadow profile | score-return alignment |
|---:|---|---|---|
| 012510 | correct | preserved positive | aligned |
| 263860 | correct | preserved positive | aligned |
| 030520 | false positive risk | capped at Stage2/watch | improved |
| 053800 | false positive risk | reclassified as event/control-premium overlay | improved |
| 131370 | 4B too late | one-off demand 4B overlay | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L8_PLATFORM_CONTENT_SW_SECURITY | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | B2B_SOFTWARE_SECURITY_RECURRING_CONTRACT_RETENTION_MARGIN_BRIDGE | 2 | 3 | 2 | 1 | 5 | 1 | 6 | 5 | 3 | true | true | C28 still needs more overseas SaaS/ARR names and post-2024 holdout validation, but this loop fills the recurring-vs-event guardrail gap. |


## 22. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 1
reused_case_ids: R8L10_C28_TRG_001B_DOUZONE_4B_OVERLAY_2024_07_08
new_symbol_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, stage3_green_total_min, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: C28_false_green_from_AI_or_political_event, C28_one_off_remote_work_demand, C28_late_4B_after_vertical_rerating
new_axis_proposed: null
existing_axis_strengthened: C28-specific retention/contract-quality Green gate; C28 event/control-premium cap; C28 one-off demand 4B overlay
existing_axis_weakened: null
existing_axis_kept: price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- Round/sector consistency: R8 ↔ L8 pass.
- Price source: stock-web tradable_raw only.
- Entry/forward-window: 180D available for all representative cases.
- Corporate action: no 180D overlap in selected windows.
- Positive/counterexample balance: pass.

Not validated:

- No production score code was opened.
- No live candidates were scanned.
- No current investment recommendation is implied.
- Evidence source extraction was not promoted into production ingestion; it remains research proxy evidence.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C28_retention_contract_quality_green_bridge,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,0,1,+1,"Green requires retained-contract/customer-quality/margin bridge, not just AI/security/event narrative","Improves false-positive separation for Hancom/AhnLab/RSUPPORT while preserving Douzone/GENIANS positives","R8L10_C28_TRG_001A_DOUZONE_STAGE2_ACTIONABLE_2024_02_05|R8L10_C28_TRG_002A_GENIANS_STAGE2_ACTIONABLE_2023_05_17|R8L10_C28_TRG_003A_HANCOM_STAGE2_ACTIONABLE_2024_01_10|R8L10_C28_TRG_004A_AHNLAB_STAGE2_WATCH_2022_03_11|R8L10_C28_TRG_005A_RSUPPORT_STAGE2_ACTIONABLE_2020_03_11",5,5,3,medium,archetype_shadow_only,"not production; post-calibrated residual"
shadow_weight,C28_event_or_control_premium_cap,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,0,1,+1,"Political/control-premium or emergency demand shock cannot promote C28 Stage3 without renewal/ARR proof","Prevents AhnLab and RSUPPORT from becoming false C28 Green entries",R8L10_C28_TRG_004A_AHNLAB_STAGE2_WATCH_2022_03_11|R8L10_C28_TRG_005A_RSUPPORT_STAGE2_ACTIONABLE_2020_03_11,2,2,2,medium,archetype_shadow_only,"not production; 4B/guardrail only"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R8L10_C28_CASE_001_DOUZONE_2024_CLOUD_ERP_AI_CONTRACT","symbol":"012510","company_name":"더존비즈온","round":"R8","loop":"10","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"B2B_SOFTWARE_SECURITY_RECURRING_CONTRACT_RETENTION_MARGIN_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R8L10_C28_TRG_001A_DOUZONE_STAGE2_ACTIONABLE_2024_02_05","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_alignment","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"ERP/WEHAGO/Amaranth/AI cloud narrative had recurring B2B software character and later margin/valuation rerating confirmation. The price path behaved like a genuine Stage2->Yellow/Green bridge rather than a pure AI headline spike."}
{"row_type":"case","case_id":"R8L10_C28_CASE_002_GENIANS_2023_SECURITY_RETENTION","symbol":"263860","company_name":"지니언스","round":"R8","loop":"10","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"B2B_SOFTWARE_SECURITY_RECURRING_CONTRACT_RETENTION_MARGIN_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R8L10_C28_TRG_002A_GENIANS_STAGE2_ACTIONABLE_2023_05_17","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_alignment","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Security/NAC/EDR recurring-account expansion gave a cleaner C28 example than one-off cyber-policy names. Price advanced only when customer-retention and operating leverage proxy improved."}
{"row_type":"case","case_id":"R8L10_C28_CASE_003_HANCOM_2024_AI_OFFICE_FALSE_GREEN","symbol":"030520","company_name":"한글과컴퓨터","round":"R8","loop":"10","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"B2B_SOFTWARE_SECURITY_RECURRING_CONTRACT_RETENTION_MARGIN_BRIDGE","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R8L10_C28_TRG_003A_HANCOM_STAGE2_ACTIONABLE_2024_01_10","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"guardrail_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"AI-office/platform option created a sharp early price reaction, but recurring enterprise retention and margin bridge were not yet strong enough for C28-Green. The path was high-MFE/high-MAE."}
{"row_type":"case","case_id":"R8L10_C28_CASE_004_AHNLAB_2022_CONTROL_PREMIUM_PRICE_ONLY","symbol":"053800","company_name":"안랩","round":"R8","loop":"10","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"B2B_SOFTWARE_SECURITY_RECURRING_CONTRACT_RETENTION_MARGIN_BRIDGE","case_type":"price_moved_without_evidence","positive_or_counterexample":"counterexample","best_trigger":"R8L10_C28_TRG_004A_AHNLAB_STAGE2_WATCH_2022_03_11","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"guardrail_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Security label plus political/control-premium flow produced a violent price move, but it was not a recurring-contract/retention software rerating. It belongs in event/control-premium or 4B overlay, not C28 positive promotion."}
{"row_type":"case","case_id":"R8L10_C28_CASE_005_RSUPPORT_2020_REMOTE_WORK_ONE_OFF","symbol":"131370","company_name":"알서포트","round":"R8","loop":"10","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"B2B_SOFTWARE_SECURITY_RECURRING_CONTRACT_RETENTION_MARGIN_BRIDGE","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"R8L10_C28_TRG_005A_RSUPPORT_STAGE2_ACTIONABLE_2020_03_11","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"guardrail_counterexample","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"COVID remote-work demand was real, but much of the price path reflected emergency pull-forward and positioning. Without retained ARR/enterprise renewal proof, C28-Green should be capped and 4B overlay should activate after non-price normalization risk appears."}
{"trigger_id":"R8L10_C28_TRG_001A_DOUZONE_STAGE2_ACTIONABLE_2024_02_05","case_id":"R8L10_C28_CASE_001_DOUZONE_2024_CLOUD_ERP_AI_CONTRACT","symbol":"012510","company_name":"더존비즈온","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-05","entry_date":"2024-02-05","entry_price":46400,"evidence_available_at_that_date":"Cloud ERP/AI enterprise software rerating narrative with customer/account stickiness proxy but before full confirmed revision bridge.","evidence_source":"public company narrative / broker-report proxy / price-atlas validation only","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","early_revision_signal"],"stage3_evidence_fields":["financial_visibility","margin_bridge","multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"MFE_30D_pct":21.3,"MFE_90D_pct":55.2,"MFE_180D_pct":68.8,"MFE_1Y_pct":68.8,"MFE_2Y_pct":106.9,"MAE_30D_pct":-10.7,"MAE_90D_pct":-10.7,"MAE_180D_pct":-10.7,"MAE_1Y_pct":-10.7,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-08","peak_price":78300,"drawdown_after_peak_pct":-40.6,"green_lateness_ratio":"0.37","four_b_local_peak_proximity":"0.95","four_b_full_window_peak_proximity":"0.95","four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success_high_mfe_with_later_4b_overlay","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"same_entry_group_id":"012510_2024-02-05_46400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"row_type":"trigger","round":"R8","loop":"10","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"B2B_SOFTWARE_SECURITY_RECURRING_CONTRACT_RETENTION_MARGIN_BRIDGE","sector":"platform_content_software_security","primary_archetype":"software_security_contract_retention","loop_objective":"coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012510/2024.csv","profile_path":"atlas/symbol_profiles/012/012510.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window"}
{"trigger_id":"R8L10_C28_TRG_001B_DOUZONE_4B_OVERLAY_2024_07_08","case_id":"R8L10_C28_CASE_001_DOUZONE_2024_CLOUD_ERP_AI_CONTRACT","symbol":"012510","company_name":"더존비즈온","trigger_type":"Stage4B","trigger_date":"2024-07-08","entry_date":"2024-07-08","entry_price":75300,"evidence_available_at_that_date":"After vertical rerating, valuation/positioning overheat became more important than new contract-retention evidence.","evidence_source":"price-atlas + non-price overlay proxy; 4B-only row","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"MFE_30D_pct":4.0,"MFE_90D_pct":4.0,"MFE_180D_pct":4.0,"MFE_1Y_pct":27.5,"MFE_2Y_pct":27.5,"MAE_30D_pct":-35.6,"MAE_90D_pct":-38.3,"MAE_180D_pct":-38.3,"MAE_1Y_pct":-38.3,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-08","peak_price":78300,"drawdown_after_peak_pct":-40.6,"green_lateness_ratio":"label_comparison_only","four_b_local_peak_proximity":"0.95","four_b_full_window_peak_proximity":"0.95","four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"same_entry_group_id":"012510_2024-02-05_46400","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same symbol as representative; 4B timing overlay only","independent_evidence_weight":0.25,"do_not_count_as_new_case":true,"row_type":"trigger","round":"R8","loop":"10","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"B2B_SOFTWARE_SECURITY_RECURRING_CONTRACT_RETENTION_MARGIN_BRIDGE","sector":"platform_content_software_security","primary_archetype":"software_security_contract_retention","loop_objective":"coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012510/2024.csv","profile_path":"atlas/symbol_profiles/012/012510.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window"}
{"trigger_id":"R8L10_C28_TRG_002A_GENIANS_STAGE2_ACTIONABLE_2023_05_17","case_id":"R8L10_C28_CASE_002_GENIANS_2023_SECURITY_RETENTION","symbol":"263860","company_name":"지니언스","trigger_type":"Stage2-Actionable","trigger_date":"2023-05-17","entry_date":"2023-05-17","entry_price":11770,"evidence_available_at_that_date":"Security software adoption and recurring account expansion proxy with clean price response before later normalization.","evidence_source":"public security-software narrative / price-atlas validation only","stage2_evidence_fields":["customer_or_order_quality","relative_strength","early_revision_signal"],"stage3_evidence_fields":["repeat_order_or_conversion","financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"MFE_30D_pct":49.5,"MFE_90D_pct":49.6,"MFE_180D_pct":49.6,"MFE_1Y_pct":49.6,"MFE_2Y_pct":52.8,"MAE_30D_pct":0.0,"MAE_90D_pct":-12.9,"MAE_180D_pct":-22.1,"MAE_1Y_pct":-22.1,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":true,"peak_date":"2023-06-12","peak_price":17600,"drawdown_after_peak_pct":-47.6,"green_lateness_ratio":"0.28","four_b_local_peak_proximity":"0.80","four_b_full_window_peak_proximity":"0.80","four_b_timing_verdict":"watch_after_revision_slowdown","four_b_evidence_type":["revision_slowdown","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"structural_success_then_normalization","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"same_entry_group_id":"263860_2023-05-17_11770","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"row_type":"trigger","round":"R8","loop":"10","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"B2B_SOFTWARE_SECURITY_RECURRING_CONTRACT_RETENTION_MARGIN_BRIDGE","sector":"platform_content_software_security","primary_archetype":"software_security_contract_retention","loop_objective":"coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/263/263860/2023.csv","profile_path":"atlas/symbol_profiles/263/263860.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window"}
{"trigger_id":"R8L10_C28_TRG_003A_HANCOM_STAGE2_ACTIONABLE_2024_01_10","case_id":"R8L10_C28_CASE_003_HANCOM_2024_AI_OFFICE_FALSE_GREEN","symbol":"030520","company_name":"한글과컴퓨터","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-10","entry_date":"2024-01-10","entry_price":24750,"evidence_available_at_that_date":"AI-office / platform option and sharp relative strength, but recurring enterprise retention and contract-quality proof was incomplete.","evidence_source":"public AI-software narrative / price-atlas validation only","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":["unknown_or_not_supported"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken"],"MFE_30D_pct":55.4,"MFE_90D_pct":55.4,"MFE_180D_pct":55.4,"MFE_1Y_pct":55.4,"MFE_2Y_pct":55.4,"MAE_30D_pct":-7.7,"MAE_90D_pct":-20.3,"MAE_180D_pct":-22.7,"MAE_1Y_pct":-22.7,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-22","peak_price":38450,"drawdown_after_peak_pct":-50.3,"green_lateness_ratio":"no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":"0.99","four_b_full_window_peak_proximity":"0.99","four_b_timing_verdict":"price_only_local_4B_too_early_if_no_non_price_evidence","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"high_mfe_high_mae_false_green_risk","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"same_entry_group_id":"030520_2024-01-10_24750","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"row_type":"trigger","round":"R8","loop":"10","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"B2B_SOFTWARE_SECURITY_RECURRING_CONTRACT_RETENTION_MARGIN_BRIDGE","sector":"platform_content_software_security","primary_archetype":"software_security_contract_retention","loop_objective":"coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/030/030520/2024.csv","profile_path":"atlas/symbol_profiles/030/030520.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window"}
{"trigger_id":"R8L10_C28_TRG_004A_AHNLAB_STAGE2_WATCH_2022_03_11","case_id":"R8L10_C28_CASE_004_AHNLAB_2022_CONTROL_PREMIUM_PRICE_ONLY","symbol":"053800","company_name":"안랩","trigger_type":"Stage2-Watch","trigger_date":"2022-03-11","entry_date":"2022-03-11","entry_price":86500,"evidence_available_at_that_date":"Security label plus political/control-premium flow. No C28 recurring-contract retention bridge was visible at trigger date.","evidence_source":"event/control-premium narrative / price-atlas validation only","stage2_evidence_fields":["relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":["unknown_or_not_supported"],"stage4b_evidence_fields":["control_premium_or_event_premium","price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"MFE_30D_pct":152.6,"MFE_90D_pct":152.6,"MFE_180D_pct":152.6,"MFE_1Y_pct":152.6,"MFE_2Y_pct":152.6,"MAE_30D_pct":-14.2,"MAE_90D_pct":-14.2,"MAE_180D_pct":-36.0,"MAE_1Y_pct":-36.0,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-03-24","peak_price":218500,"drawdown_after_peak_pct":-62.9,"green_lateness_ratio":"not_applicable_no_green_allowed","four_b_local_peak_proximity":"0.99","four_b_full_window_peak_proximity":"0.99","four_b_timing_verdict":"good_full_window_4B_timing_if_control_premium_overlay_used","four_b_evidence_type":["control_premium_or_event_premium","positioning_overheat","price_only"],"four_c_protection_label":"hard_4c_late_if_misclassified_as_C28_green","trigger_outcome_label":"price_moved_without_C28_evidence","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"same_entry_group_id":"053800_2022-03-11_86500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"row_type":"trigger","round":"R8","loop":"10","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"B2B_SOFTWARE_SECURITY_RECURRING_CONTRACT_RETENTION_MARGIN_BRIDGE","sector":"platform_content_software_security","primary_archetype":"software_security_contract_retention","loop_objective":"coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/053/053800/2022.csv","profile_path":"atlas/symbol_profiles/053/053800.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window"}
{"trigger_id":"R8L10_C28_TRG_005A_RSUPPORT_STAGE2_ACTIONABLE_2020_03_11","case_id":"R8L10_C28_CASE_005_RSUPPORT_2020_REMOTE_WORK_ONE_OFF","symbol":"131370","company_name":"알서포트","trigger_type":"Stage2-Actionable","trigger_date":"2020-03-11","entry_date":"2020-03-11","entry_price":3390,"evidence_available_at_that_date":"Remote-support demand shock under COVID. Product demand was real, but retention/renewal and post-emergency ARR durability were not yet proven.","evidence_source":"COVID remote-work narrative / price-atlas validation only","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":["unknown_or_not_supported"],"stage4b_evidence_fields":["positioning_overheat","valuation_blowoff","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"MFE_30D_pct":107.7,"MFE_90D_pct":206.8,"MFE_180D_pct":597.6,"MFE_1Y_pct":597.6,"MFE_2Y_pct":597.6,"MAE_30D_pct":-30.0,"MAE_90D_pct":-30.0,"MAE_180D_pct":-30.0,"MAE_1Y_pct":-30.0,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2020-08-28","peak_price":23650,"drawdown_after_peak_pct":-50.7,"green_lateness_ratio":"no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":"0.99","four_b_full_window_peak_proximity":"0.99","four_b_timing_verdict":"good_full_window_4B_timing_after_non_price_demand_normalization_risk","four_b_evidence_type":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_success_after_thesis_normalization","trigger_outcome_label":"4B_overlay_success_one_off_demand","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"same_entry_group_id":"131370_2020-03-11_3390","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"row_type":"trigger","round":"R8","loop":"10","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"B2B_SOFTWARE_SECURITY_RECURRING_CONTRACT_RETENTION_MARGIN_BRIDGE","sector":"platform_content_software_security","primary_archetype":"software_security_contract_retention","loop_objective":"coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/131/131370/2020.csv","profile_path":"atlas/symbol_profiles/131/131370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L10_C28_CASE_001_DOUZONE_2024_CLOUD_ERP_AI_CONTRACT","trigger_id":"R8L10_C28_TRG_001A_DOUZONE_STAGE2_ACTIONABLE_2024_02_05","symbol":"012510","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":13,"backlog_visibility_score":10,"margin_bridge_score":12,"revision_score":12,"relative_strength_score":10,"customer_quality_score":11,"policy_or_regulatory_score":2,"valuation_repricing_score":8,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":75,"stage_label_before":"Stage3-Green-proxy","raw_component_scores_after":{"contract_score":15,"backlog_visibility_score":10,"margin_bridge_score":13,"revision_score":12,"relative_strength_score":10,"customer_quality_score":13,"policy_or_regulatory_score":2,"valuation_repricing_score":8,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":80,"stage_label_after":"Stage3-Green-proxy","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"C28 shadow profile rewards retained contract/customer-quality bridge and penalizes event/price-only software narratives without ARR/retention proof.","MFE_90D_pct":55.2,"MAE_90D_pct":-10.7,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L10_C28_CASE_002_GENIANS_2023_SECURITY_RETENTION","trigger_id":"R8L10_C28_TRG_002A_GENIANS_STAGE2_ACTIONABLE_2023_05_17","symbol":"263860","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":8,"margin_bridge_score":8,"revision_score":9,"relative_strength_score":8,"customer_quality_score":9,"policy_or_regulatory_score":3,"valuation_repricing_score":6,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":57,"stage_label_before":"Stage2-Actionable-proxy","raw_component_scores_after":{"contract_score":12,"backlog_visibility_score":8,"margin_bridge_score":9,"revision_score":9,"relative_strength_score":8,"customer_quality_score":11,"policy_or_regulatory_score":3,"valuation_repricing_score":6,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":62,"stage_label_after":"Stage3-Yellow-proxy","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"C28 shadow profile rewards retained contract/customer-quality bridge and penalizes event/price-only software narratives without ARR/retention proof.","MFE_90D_pct":49.6,"MAE_90D_pct":-12.9,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L10_C28_CASE_003_HANCOM_2024_AI_OFFICE_FALSE_GREEN","trigger_id":"R8L10_C28_TRG_003A_HANCOM_STAGE2_ACTIONABLE_2024_01_10","symbol":"030520","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":2,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":12,"customer_quality_score":4,"policy_or_regulatory_score":5,"valuation_repricing_score":8,"execution_risk_score":-8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":31,"stage_label_before":"Stage2-Watch-or-Event-proxy","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":3,"relative_strength_score":12,"customer_quality_score":4,"policy_or_regulatory_score":5,"valuation_repricing_score":8,"execution_risk_score":-12,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":20,"stage_label_after":"Stage2-Watch-or-Event-proxy","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"C28 shadow profile rewards retained contract/customer-quality bridge and penalizes event/price-only software narratives without ARR/retention proof.","MFE_90D_pct":55.4,"MAE_90D_pct":-20.3,"score_return_alignment_label":"false_positive_guard_improved","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L10_C28_CASE_004_AHNLAB_2022_CONTROL_PREMIUM_PRICE_ONLY","trigger_id":"R8L10_C28_TRG_004A_AHNLAB_STAGE2_WATCH_2022_03_11","symbol":"053800","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":3,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":15,"customer_quality_score":4,"policy_or_regulatory_score":10,"valuation_repricing_score":10,"execution_risk_score":-12,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":38,"stage_label_before":"Stage2-Watch-or-Event-proxy","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":2,"relative_strength_score":15,"customer_quality_score":4,"policy_or_regulatory_score":10,"valuation_repricing_score":10,"execution_risk_score":-16,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":27,"stage_label_after":"Stage2-Watch-or-Event-proxy","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"C28 shadow profile rewards retained contract/customer-quality bridge and penalizes event/price-only software narratives without ARR/retention proof.","MFE_90D_pct":152.6,"MAE_90D_pct":-14.2,"score_return_alignment_label":"false_positive_guard_improved","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L10_C28_CASE_005_RSUPPORT_2020_REMOTE_WORK_ONE_OFF","trigger_id":"R8L10_C28_TRG_005A_RSUPPORT_STAGE2_ACTIONABLE_2020_03_11","symbol":"131370","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":5,"backlog_visibility_score":3,"margin_bridge_score":3,"revision_score":4,"relative_strength_score":15,"customer_quality_score":3,"policy_or_regulatory_score":8,"valuation_repricing_score":12,"execution_risk_score":-12,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":41,"stage_label_before":"Stage2-Watch-or-Event-proxy","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":4,"relative_strength_score":15,"customer_quality_score":3,"policy_or_regulatory_score":8,"valuation_repricing_score":12,"execution_risk_score":-16,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":30,"stage_label_after":"Stage2-Watch-or-Event-proxy","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"C28 shadow profile rewards retained contract/customer-quality bridge and penalizes event/price-only software narratives without ARR/retention proof.","MFE_90D_pct":206.8,"MAE_90D_pct":-30.0,"score_return_alignment_label":"false_positive_guard_improved","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"residual_contribution","round":"R8","loop":"10","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","new_independent_case_count":5,"reused_case_count":1,"new_symbol_count":5,"new_trigger_family_count":4,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_total_min","full_4b_requires_non_price_evidence","price_only_blowoff_blocks_positive_stage"],"residual_error_types_found":["C28_false_green_from_AI_or_political_event","C28_one_off_remote_work_demand","C28_late_4B_after_vertical_rerating"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_round = R8
completed_loop = 10
next_round = R9
next_loop = 10
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- `reports/e2r_calibration/by_round/R8.md` was used only for coverage/duplicate avoidance.
- `atlas/manifest.json` and `atlas/schema.json` were used for price source validation.
- Symbol profiles used: `012510`, `263860`, `030520`, `053800`, `131370`.
- Tradable OHLC shards used: `012510/2024`, `263860/2023`, `030520/2024`, `053800/2022`, `131370/2020`.
- All price data are raw/unadjusted marcap OHLC rows from stock-web; no adjusted-price reconstruction was performed.

