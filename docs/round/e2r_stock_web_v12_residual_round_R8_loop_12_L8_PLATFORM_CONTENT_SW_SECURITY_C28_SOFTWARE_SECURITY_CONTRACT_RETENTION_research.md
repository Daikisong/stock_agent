# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R8
loop = 12
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id = SOFTWARE_SECURITY_CONTRACT_RETENTION_RENEWAL_SAAS_MARGIN_BRIDGE_VS_THEME_EVENT_PREMIUM
output_file = e2r_stock_web_v12_residual_round_R8_loop_12_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This MD is historical calibration research only. It is not live candidate discovery, not an investment recommendation, not a stock-agent code patch, and not an auto-trading artifact.

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

This loop does not re-propose the global changes above. It stress-tests whether C28 needs a narrower contract-retention gate, because software/security can look structurally recurring even when the actual price move comes from a one-off theme, political premium, or policy headline.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| round | R8 |
| loop | 12 |
| large_sector_id | L8_PLATFORM_CONTENT_SW_SECURITY |
| canonical_archetype_id | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION |
| fine_archetype_id | SOFTWARE_SECURITY_CONTRACT_RETENTION_RENEWAL_SAAS_MARGIN_BRIDGE_VS_THEME_EVENT_PREMIUM |
| loop_objective | residual_missed_structural_mining / residual_false_positive_mining / sector_specific_rule_discovery / canonical_archetype_compression / 4B_non_price_requirement_stress_test / coverage_gap_fill |

C28 differs from platform ads and content IP. The central mechanism is not traffic or fandom; it is renewal, maintenance, SaaS conversion, attach rate, gross retention, net retention, and whether that retention is visible enough to create OP/EPS revision.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed artifact review found that the prior calibration corpus covers R1~R13 and loops 1~9, with 4,951 raw trigger rows, 1,940 validated trigger rows, and 1,376 aggregate representative rows. The repeated global axes already applied include Stage2 actionable bonus, stricter Green, non-price 4B, and hard 4C routing. This loop therefore adds new post-calibrated coverage for C28 rather than repeating those axes.

```text
required_new_independent_case_ratio >= 0.60
calibration_usable_case_count = 5
new_independent_case_count = 5
new_independent_case_ratio = 1.00
reused_case_count = 0
loop_contribution_label = canonical_archetype_rule_candidate
```

## 4. Stock-Web OHLC Input / Price Source Validation

| manifest field | observed value |
|---|---|
| source_name | FinanceData/marcap |
| source_repo_url | https://github.com/FinanceData/marcap |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14354401 |
| raw_row_count | 15214118 |
| symbol_count | 5414 |
| active_like_symbol_count | 2868 |
| inactive_or_delisted_like_symbol_count | 2546 |
| markets | KONEX / KOSDAQ / KOSDAQ GLOBAL / KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

The stock-web schema defines `d,o,h,l,c,v,a,mc,s,m` for tradable shards and states that tradable shards include only positive OHLC and volume rows. The profile-level corporate-action candidate windows are blocked from weight calibration.

## 5. Historical Eligibility Gate

All representative triggers below satisfy:

```text
entry_date exists in stock-web tradable shard
forward_window_trading_days >= 180
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
MFE_30D / MFE_90D / MFE_180D computed
MAE_30D / MAE_90D / MAE_180D computed
corporate_action_window_status = clean_180D_window
```

No case in this loop uses raw shards for quantitative calibration. Raw shards are not used to train weight deltas.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | inclusion logic |
|---|---|---|
| SOFTWARE_SECURITY_CONTRACT_RETENTION_RENEWAL_SAAS_MARGIN_BRIDGE_VS_THEME_EVENT_PREMIUM | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | Contract renewal, maintenance, SaaS conversion, security software retention, and license-to-cloud margin bridge |
| POLITICAL_SECURITY_EVENT_PREMIUM | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | Included only as counterexample guard; not positive promotion evidence |
| METAVERSE_OR_POLICY_SOFTWARE_THEME | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | Included only as theme-event premium cap / false-positive test |

## 7. Case Selection Summary

| case_id | symbol | company | role | positive_or_counterexample | current_profile_verdict | best_trigger |
|---|---:|---|---|---|---|---|
| R8L12_C28_012510_DUZON_CLOUD_2020 | 012510 | 더존비즈온 | structural_success | positive | current_profile_too_late | R8L12_C28_T001 |
| R8L12_C28_263860_GENIANS_EDR_2023 | 263860 | 지니언스 | structural_success | positive | current_profile_missed_structural | R8L12_C28_T004 |
| R8L12_C28_136540_WINS_CONTRACT_RETENTION_NO_EXPLOSION_2020 | 136540 | 윈스테크넷 | failed_rerating | counterexample | current_profile_correct | R8L12_C28_T006 |
| R8L12_C28_053800_AHNLAB_POLITICAL_EVENT_2022 | 053800 | 안랩 | price_moved_without_evidence | counterexample | current_profile_correct | R8L12_C28_T007 |
| R8L12_C28_030520_HANCOM_THEME_PREMIUM_2021 | 030520 | 한글과컴퓨터 | false_positive_green | counterexample | current_profile_false_positive | R8L12_C28_T008 |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 3
4B_case_count = 2
4C_case_count = 1
minimum_positive_case_count = satisfied
minimum_counterexample_count = satisfied
minimum_calibration_usable_case_count = satisfied
```

The pair that matters is `012510/263860` versus `136540/053800/030520`. The positive cases show contract-retention plus margin/revision bridge. The counterexamples show that security/software labels can be durable businesses but still fail as E2R rerating triggers when the price move is theme-heavy or the earnings bridge is absent.

## 9. Evidence Source Map

| case | Stage2 evidence | Stage3 evidence | 4B/4C evidence | evidence timing note |
|---|---|---|---|---|
| 더존비즈온 | cloud/ERP demand, enterprise customer base, subscription-like renewal | margin bridge and financial visibility | later valuation expansion | trigger treated as next tradable close |
| 지니언스 | NAC/EDR security renewal base, small-cap relative strength | repeat order / endpoint-security visibility | later sharp correction watch | trigger treated as next tradable close |
| 윈스테크넷 | security appliance/maintenance durability | insufficient EPS acceleration | no full 4B | retention alone cap test |
| 안랩 | relative strength only; event/political premium dominates | none | price-only blowoff / event cap | counterexample, no positive weight |
| 한글과컴퓨터 | software/license theme, policy/metaverse premium | no durable SaaS margin bridge | 4B then 4C watch | false-positive test |

## 10. Price Data Source Map

| symbol | company | price_shard_path | profile_path | profile caveat |
|---:|---|---|---|---|
| 012510 | 더존비즈온 | atlas/ohlcv_tradable_by_symbol_year/012/012510/2020.csv | atlas/symbol_profiles/012/012510.json | old corporate-action candidates before calibration window |
| 263860 | 지니언스 | atlas/ohlcv_tradable_by_symbol_year/263/263860/2023.csv | atlas/symbol_profiles/263/263860.json | old 2018 corporate-action candidates, no 2023 window block |
| 136540 | 윈스테크넷 | atlas/ohlcv_tradable_by_symbol_year/136/136540/2020.csv | atlas/symbol_profiles/136/136540.json | clean 2020 window |
| 053800 | 안랩 | atlas/ohlcv_tradable_by_symbol_year/053/053800/2022.csv | atlas/symbol_profiles/053/053800.json | old 2005 corporate-action candidate, no 2022 window block |
| 030520 | 한글과컴퓨터 | atlas/ohlcv_tradable_by_symbol_year/030/030520/2021.csv | atlas/symbol_profiles/030/030520.json | old corporate-action candidates before calibration window |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_type | trigger_date | entry_date | entry_price | role | current_profile_verdict |
|---|---|---|---|---|---:|---|---|
| R8L12_C28_T001 | R8L12_C28_012510_DUZON_CLOUD_2020 | Stage2-Actionable | 2020-04-24 | 2020-04-27 | 88700 | representative | current_profile_too_late |
| R8L12_C28_T002 | R8L12_C28_012510_DUZON_CLOUD_2020 | Stage3-Green-label-comparison | 2020-09-04 | 2020-09-04 | 126500 | label_comparison_only | current_profile_too_late |
| R8L12_C28_T004 | R8L12_C28_263860_GENIANS_EDR_2023 | Stage2-Actionable | 2023-01-31 | 2023-01-31 | 9900 | representative | current_profile_missed_structural |
| R8L12_C28_T005 | R8L12_C28_263860_GENIANS_EDR_2023 | Stage3-Yellow-label-comparison | 2023-05-17 | 2023-05-17 | 11770 | label_comparison_only | current_profile_too_late |
| R8L12_C28_T006 | R8L12_C28_136540_WINS_CONTRACT_RETENTION_NO_EXPLOSION_2020 | Stage2 | 2020-04-24 | 2020-04-27 | 15650 | representative | current_profile_correct |
| R8L12_C28_T007 | R8L12_C28_053800_AHNLAB_POLITICAL_EVENT_2022 | 4B-overlay / false-positive-check | 2022-03-16 | 2022-03-16 | 87500 | representative | current_profile_correct |
| R8L12_C28_T008 | R8L12_C28_030520_HANCOM_THEME_PREMIUM_2021 | Stage2-theme-premium / 4C-watch | 2021-11-17 | 2021-11-17 | 28400 | representative | current_profile_false_positive |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | symbol | entry_date | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| R8L12_C28_T001 | 012510 | 2020-04-27 | 88700 | 38.9 | -4.1 | 49.9 | -4.1 | 53.3 | -4.1 | 2020-09-08 | 136000 | -26.5 |
| R8L12_C28_T002 | 012510 | 2020-09-04 | 126500 | 7.5 | -13.8 | 7.5 | -21.5 | 7.5 | -22.9 | 2020-09-08 | 136000 | -26.5 |
| R8L12_C28_T004 | 263860 | 2023-01-31 | 9900 | 17.5 | -5.96 | 33.1 | -5.96 | 78.2 | -5.96 | 2023-06-13 | 17640 | -37.4 |
| R8L12_C28_T005 | 263860 | 2023-05-17 | 11770 | 49.9 | -4.6 | 49.9 | -6.2 | 49.9 | -6.2 | 2023-06-13 | 17640 | -37.4 |
| R8L12_C28_T006 | 136540 | 2020-04-27 | 15650 | 17.6 | -4.5 | 17.6 | -5.8 | 17.6 | -5.8 | 2020-05-07 | 18400 | -19.8 |
| R8L12_C28_T007 | 053800 | 2022-03-16 | 87500 | 149.7 | -5.9 | 149.7 | -7.4 | 149.7 | -29.1 | 2022-03-24 | 218500 | -71.6 |
| R8L12_C28_T008 | 030520 | 2021-11-17 | 28400 | 21.5 | -12.3 | 21.5 | -32.4 | 21.5 | -46.5 | 2021-12-06 | 34500 | -55.9 |

Representative aggregate rows only:

```text
representative_trigger_count = 5
avg_MFE_90D_pct = 54.36
avg_MAE_90D_pct = -11.13
avg_MFE_180D_pct = 64.06
avg_MAE_180D_pct = -18.29
```

## 13. Current Calibrated Profile Stress Test

| case | current profile result | actual path | verdict |
|---|---|---|---|
| 더존비즈온 | likely waits for stricter Green confirmation | Stage2 captured much more upside than late Green | current_profile_too_late |
| 지니언스 | small-cap security evidence may remain below Green/Yellow | Stage2-style evidence preceded strong 180D MFE | current_profile_missed_structural |
| 윈스테크넷 | capped at Stage2/Yellow due weak revision/margin bridge | limited rerating despite durability | current_profile_correct |
| 안랩 | price-only / event premium blocked from positive stage | blowoff then major drawdown | current_profile_correct |
| 한글과컴퓨터 | may leak into Stage2-Actionable if software label overcredited | theme spike followed by deep drawdown | current_profile_false_positive |

Answers to required stress-test questions:

```text
Stage2 bonus: useful for Duzon/Genians, but too generous if contract retention is inferred from industry label only.
Yellow threshold 75: acceptable if component evidence is explicit; too generous for Wins/Hancom without margin bridge.
Green threshold 87 / revision 55: generally appropriate, but Duzon-like enterprise software can look late if renewal-to-OP bridge appears before sell-side revision catches up.
price-only blowoff guard: strengthened, especially for AhnLab/Hancom.
full 4B non-price requirement: kept; C28 needs non-price 4B evidence, not merely local price peak.
hard 4C routing: kept; Hancom-like theme fade should become 4C watch only after thesis evidence breaks, not before.
```

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2 entry | later Yellow/Green entry | peak after Stage2 | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---:|---|
| 더존비즈온 | 88,700 | 126,500 | 136,000 | 0.80 | strict Green misses most upside |
| 지니언스 | 9,900 | 11,770 | 17,640 | 0.24 for Yellow, ~0.81 for full Green proxy | Yellow useful; full Green late |
| 윈스테크넷 | 15,650 | not applicable | 18,400 | n/a | no confirmed Green |
| 안랩 | not valid positive Stage2 | not applicable | 218,500 | n/a | event premium, not C28 signal |
| 한글과컴퓨터 | 28,400 theme trigger | not valid Green | 34,500 | n/a | theme premium cap required |

## 15. 4B Local vs Full-window Timing Audit

| case | trigger | local_peak_proximity | full_window_peak_proximity | evidence type | verdict |
|---|---|---:|---:|---|---|
| 안랩 | R8L12_C28_T007 | 1.00 | 1.00 | price_only / positioning_overheat / event premium | good overlay but not positive-stage evidence |
| 한글과컴퓨터 | R8L12_C28_T008 | 1.00 | 1.00 | price_only / event premium | 4B overlay then 4C watch |
| 더존비즈온 | later valuation expansion | n/a | n/a | valuation / revision slowdown needed | no new full 4B rule |

## 16. 4C Protection Audit

| case | 4C label | protection interpretation |
|---|---|---|
| 한글과컴퓨터 | thesis_break_watch_only | Event/theme move faded without a renewal/SaaS margin bridge; 4C should be watch/protection, not positive weight |
| 안랩 | thesis_break_watch_only | The security-company label never became contract-retention evidence, so the row is 4B/event guard rather than 4C positive training |
| 윈스테크넷 | not applicable | No thesis break; rather insufficient rerating intensity |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = canonical_archetype_specific
rule_name = c28_recurring_contract_retention_gate
candidate_delta = +1 for qualifying C28 cases only
```

Proposed condition:

```text
For C28 positive promotion above Stage2:
    require at least two of:
        - explicit renewal / maintenance / recurring contract base,
        - SaaS/cloud conversion or subscription mix,
        - customer retention / repeat-order evidence,
        - OP margin bridge from software mix,
        - confirmed revision or financial visibility.
    price action, policy themes, political themes, DID/metaverse/security headlines alone cannot satisfy the gate.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_name = c28_theme_event_premium_cap
scope = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
effect = cap at Stage1/Event-watch or Stage2 non-actionable when evidence is only theme/event/political premium
```

This rule compresses security-event, metaverse-software, DID-policy, and political-security false positives into one canonical guard: do not let a software/security label masquerade as contract retention.

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | missed_structural_count | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | global proxy | 5 reps | 54.36 | -11.13 | 64.06 | -18.29 | 0.20 | 1 | useful but C28-specific residual remains |
| P0b e2r_2_0_baseline_reference | rollback reference | 5 reps | 54.36 | -11.13 | 64.06 | -18.29 | 0.40 | 2 | too permissive for software/security themes |
| P1 sector_specific_candidate_profile | L8 | 5 reps | 54.36 | -11.13 | 64.06 | -18.29 | 0.10 | 1 | improves event cap |
| P2 canonical_archetype_candidate_profile | C28 | 5 reps | 54.36 | -11.13 | 64.06 | -18.29 | 0.00-0.10 | 0-1 | best explanatory fit |
| P3 counterexample_guard_profile | C28 guard | 5 reps | 54.36 | -11.13 | 64.06 | -18.29 | 0.00 | 1 | strongest false-positive control |

## 20. Score-Return Alignment Matrix

| case | weighted score before | stage before | weighted score after | stage after | MFE_90D | MAE_90D | alignment |
|---|---:|---|---:|---|---:|---:|---|
| R8L12_C28_012510_DUZON_CLOUD_2020 | 82 | Stage3-Yellow | 88 | Stage3-Green | 49.9 | -4.1 | aligned_positive |
| R8L12_C28_263860_GENIANS_EDR_2023 | 74 | Stage2-Actionable | 79 | Stage3-Yellow | 33.1 | -5.96 | aligned_positive |
| R8L12_C28_136540_WINS_CONTRACT_RETENTION_NO_EXPLOSION_2020 | 67 | Stage2 | 66 | Stage2 | 17.6 | -5.8 | correctly_capped |
| R8L12_C28_053800_AHNLAB_POLITICAL_EVENT_2022 | 61 | Stage1/Event-watch | 49 | 4B-overlay-only / no-positive-stage | 149.7 | -7.4 | counterexample_guarded |
| R8L12_C28_030520_HANCOM_THEME_PREMIUM_2021 | 68 | Stage2-Actionable | 55 | Theme-event-watch / no-positive-stage | 21.5 | -32.4 | false_positive_reduced |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L8_PLATFORM_CONTENT_SW_SECURITY | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | SOFTWARE_SECURITY_CONTRACT_RETENTION_RENEWAL_SAAS_MARGIN_BRIDGE_VS_THEME_EVENT_PREMIUM | 2 | 3 | 2 | 1 | 5 | 0 | 7 | 5 | 3 | true | true | C28 now has positive/negative balance; needs holdout on more SaaS/security names |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - current_profile_too_late
  - current_profile_missed_structural
  - current_profile_false_positive
  - theme_event_positive_stage_leakage
new_axis_proposed:
  - c28_recurring_contract_retention_gate
  - c28_theme_event_premium_cap
  - c28_margin_bridge_required_for_green
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - stage3_green_total_min
  - stage3_green_revision_min
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Historical OHLC row availability through stock-web tradable shards
- 180D forward-window availability
- clean 180D corporate-action windows by symbol profile
- trigger-level MFE / MAE / peak / drawdown proxy
- current calibrated profile stress test
- C28-specific positive/counterexample balance
```

Not validated:

```text
- exact production score from stock_agent code
- live stage labels
- investment suitability
- official adjusted-return series
- intraday evidence release time
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c28_recurring_contract_retention_gate,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,0,1,+1,"Promote only when renewal/maintenance or SaaS retention evidence combines with margin/revision bridge.","Raised Duzon/Genians while keeping Wins capped.","R8L12_C28_T001|R8L12_C28_T004|R8L12_C28_T006",5,5,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c28_theme_event_premium_cap,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,0,1,+1,"Political/metaverse/DID/security headlines cannot inherit software contract retention score.","Reduced AhnLab/Hancom false-positive positive-stage risk.","R8L12_C28_T007|R8L12_C28_T008",5,5,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c28_margin_bridge_required_for_green,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,0,1,+1,"Green requires renewal-to-OP or SaaS mix margin bridge; contract existence alone caps at Yellow.","Prevents retention-only Wins-like cases from reaching Green.","R8L12_C28_T006|R8L12_C28_T001",5,5,3,low,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R8L12_C28_012510_DUZON_CLOUD_2020","symbol":"012510","company_name":"더존비즈온","round":"R8","loop":"12","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SOFTWARE_SECURITY_CONTRACT_RETENTION_RENEWAL_SAAS_MARGIN_BRIDGE_VS_THEME_EVENT_PREMIUM","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R8L12_C28_T001","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_alignment","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Cloud/ERP retention and subscription-like renewal visibility produced an early Stage2 opportunity; strict Green would have waited until upside was mostly consumed."}
{"row_type":"case","case_id":"R8L12_C28_263860_GENIANS_EDR_2023","symbol":"263860","company_name":"지니언스","round":"R8","loop":"12","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SOFTWARE_SECURITY_CONTRACT_RETENTION_RENEWAL_SAAS_MARGIN_BRIDGE_VS_THEME_EVENT_PREMIUM","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R8L12_C28_T004","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_alignment","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"NAC/EDR security renewal base plus endpoint expansion created a small-cap structural software rerating path; score should distinguish contract retention from one-off security headlines."}
{"row_type":"case","case_id":"R8L12_C28_136540_WINS_CONTRACT_RETENTION_NO_EXPLOSION_2020","symbol":"136540","company_name":"윈스테크넷","round":"R8","loop":"12","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SOFTWARE_SECURITY_CONTRACT_RETENTION_RENEWAL_SAAS_MARGIN_BRIDGE_VS_THEME_EVENT_PREMIUM","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R8L12_C28_T006","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_alignment","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Security appliances and maintenance are durable, but the path lacked the SaaS/renewal-margin bridge needed for EPS rerating. Retention alone should cap at Stage2/Yellow."}
{"row_type":"case","case_id":"R8L12_C28_053800_AHNLAB_POLITICAL_EVENT_2022","symbol":"053800","company_name":"안랩","round":"R8","loop":"12","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SOFTWARE_SECURITY_CONTRACT_RETENTION_RENEWAL_SAAS_MARGIN_BRIDGE_VS_THEME_EVENT_PREMIUM","case_type":"price_moved_without_evidence","positive_or_counterexample":"counterexample","best_trigger":"R8L12_C28_T007","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_alignment","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Security label was overwhelmed by political/event premium. Price-only spike had excellent local peak proximity but lacked contract-retention evidence; it should not train positive C28 weights."}
{"row_type":"case","case_id":"R8L12_C28_030520_HANCOM_THEME_PREMIUM_2021","symbol":"030520","company_name":"한글과컴퓨터","round":"R8","loop":"12","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SOFTWARE_SECURITY_CONTRACT_RETENTION_RENEWAL_SAAS_MARGIN_BRIDGE_VS_THEME_EVENT_PREMIUM","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R8L12_C28_T008","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_alignment","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"License/software theme premium produced a fast price move, but renewal/SaaS margin bridge was too weak; subsequent drawdown argues for a theme-premium cap."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"R8L12_C28_T001","case_id":"R8L12_C28_012510_DUZON_CLOUD_2020","symbol":"012510","company_name":"더존비즈온","round":"R8","loop":"12","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SOFTWARE_SECURITY_CONTRACT_RETENTION_RENEWAL_SAAS_MARGIN_BRIDGE_VS_THEME_EVENT_PREMIUM","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"software_security_contract_retention","loop_objective":"residual_missed_structural_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2020-04-24","evidence_available_at_that_date":"public evidence available at or before trigger date; timing treated as next-tradable-close when intraday time was unclear","evidence_source":"historical public filings/reports/news summary; stock-web used only for OHLCV","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","backlog_or_delivery_visibility","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","multiple_public_sources","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012510/2020.csv","profile_path":"atlas/symbol_profiles/012/012510.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2020-04-27","entry_price":88700,"MFE_30D_pct":38.9,"MFE_90D_pct":49.9,"MFE_180D_pct":53.3,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-4.1,"MAE_90D_pct":-4.1,"MAE_180D_pct":-4.1,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2020-09-08","peak_price":136000,"drawdown_after_peak_pct":-26.5,"green_lateness_ratio":0.0,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L12_C28_012510_DUZON_CLOUD_2020_2020-04-27_88700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R8L12_C28_T002","case_id":"R8L12_C28_012510_DUZON_CLOUD_2020","symbol":"012510","company_name":"더존비즈온","round":"R8","loop":"12","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SOFTWARE_SECURITY_CONTRACT_RETENTION_RENEWAL_SAAS_MARGIN_BRIDGE_VS_THEME_EVENT_PREMIUM","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"software_security_contract_retention","loop_objective":"residual_missed_structural_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|coverage_gap_fill","trigger_type":"Stage3-Green-label-comparison","trigger_date":"2020-09-04","evidence_available_at_that_date":"public evidence available at or before trigger date; timing treated as next-tradable-close when intraday time was unclear","evidence_source":"historical public filings/reports/news summary; stock-web used only for OHLCV","stage2_evidence_fields":["early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012510/2020.csv","profile_path":"atlas/symbol_profiles/012/012510.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2020-09-04","entry_price":126500,"MFE_30D_pct":7.5,"MFE_90D_pct":7.5,"MFE_180D_pct":7.5,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-13.8,"MAE_90D_pct":-21.5,"MAE_180D_pct":-22.9,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2020-09-08","peak_price":136000,"drawdown_after_peak_pct":-26.5,"green_lateness_ratio":0.8,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"late_green","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L12_C28_012510_DUZON_CLOUD_2020_2020-09-04_126500","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R8L12_C28_T004","case_id":"R8L12_C28_263860_GENIANS_EDR_2023","symbol":"263860","company_name":"지니언스","round":"R8","loop":"12","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SOFTWARE_SECURITY_CONTRACT_RETENTION_RENEWAL_SAAS_MARGIN_BRIDGE_VS_THEME_EVENT_PREMIUM","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"software_security_contract_retention","loop_objective":"residual_missed_structural_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2023-01-31","evidence_available_at_that_date":"public evidence available at or before trigger date; timing treated as next-tradable-close when intraday time was unclear","evidence_source":"historical public filings/reports/news summary; stock-web used only for OHLCV","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","early_revision_signal"],"stage3_evidence_fields":["multiple_public_sources","financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/263/263860/2023.csv","profile_path":"atlas/symbol_profiles/263/263860.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-01-31","entry_price":9900,"MFE_30D_pct":17.5,"MFE_90D_pct":33.1,"MFE_180D_pct":78.2,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.96,"MAE_90D_pct":-5.96,"MAE_180D_pct":-5.96,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-06-13","peak_price":17640,"drawdown_after_peak_pct":-37.4,"green_lateness_ratio":0.0,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L12_C28_263860_GENIANS_EDR_2023_2023-01-31_9900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R8L12_C28_T005","case_id":"R8L12_C28_263860_GENIANS_EDR_2023","symbol":"263860","company_name":"지니언스","round":"R8","loop":"12","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SOFTWARE_SECURITY_CONTRACT_RETENTION_RENEWAL_SAAS_MARGIN_BRIDGE_VS_THEME_EVENT_PREMIUM","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"software_security_contract_retention","loop_objective":"residual_missed_structural_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|coverage_gap_fill","trigger_type":"Stage3-Yellow-label-comparison","trigger_date":"2023-05-17","evidence_available_at_that_date":"public evidence available at or before trigger date; timing treated as next-tradable-close when intraday time was unclear","evidence_source":"historical public filings/reports/news summary; stock-web used only for OHLCV","stage2_evidence_fields":["customer_or_order_quality","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","multiple_public_sources","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/263/263860/2023.csv","profile_path":"atlas/symbol_profiles/263/263860.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-05-17","entry_price":11770,"MFE_30D_pct":49.9,"MFE_90D_pct":49.9,"MFE_180D_pct":49.9,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-4.6,"MAE_90D_pct":-6.2,"MAE_180D_pct":-6.2,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-06-13","peak_price":17640,"drawdown_after_peak_pct":-37.4,"green_lateness_ratio":0.24,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"late_yellow","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L12_C28_263860_GENIANS_EDR_2023_2023-05-17_11770","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R8L12_C28_T006","case_id":"R8L12_C28_136540_WINS_CONTRACT_RETENTION_NO_EXPLOSION_2020","symbol":"136540","company_name":"윈스테크넷","round":"R8","loop":"12","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SOFTWARE_SECURITY_CONTRACT_RETENTION_RENEWAL_SAAS_MARGIN_BRIDGE_VS_THEME_EVENT_PREMIUM","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"software_security_contract_retention","loop_objective":"residual_missed_structural_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|coverage_gap_fill","trigger_type":"Stage2","trigger_date":"2020-04-24","evidence_available_at_that_date":"public evidence available at or before trigger date; timing treated as next-tradable-close when intraday time was unclear","evidence_source":"historical public filings/reports/news summary; stock-web used only for OHLCV","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","backlog_or_delivery_visibility"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/136/136540/2020.csv","profile_path":"atlas/symbol_profiles/136/136540.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2020-04-27","entry_price":15650,"MFE_30D_pct":17.6,"MFE_90D_pct":17.6,"MFE_180D_pct":17.6,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-4.5,"MAE_90D_pct":-5.8,"MAE_180D_pct":-5.8,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2020-05-07","peak_price":18400,"drawdown_after_peak_pct":-19.8,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L12_C28_136540_WINS_CONTRACT_RETENTION_NO_EXPLOSION_2020_2020-04-27_15650","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R8L12_C28_T007","case_id":"R8L12_C28_053800_AHNLAB_POLITICAL_EVENT_2022","symbol":"053800","company_name":"안랩","round":"R8","loop":"12","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SOFTWARE_SECURITY_CONTRACT_RETENTION_RENEWAL_SAAS_MARGIN_BRIDGE_VS_THEME_EVENT_PREMIUM","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"software_security_contract_retention","loop_objective":"residual_missed_structural_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|coverage_gap_fill","trigger_type":"4B-overlay / false-positive-check","trigger_date":"2022-03-16","evidence_available_at_that_date":"public evidence available at or before trigger date; timing treated as next-tradable-close when intraday time was unclear","evidence_source":"historical public filings/reports/news summary; stock-web used only for OHLCV","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","explicit_event_cap","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/053/053800/2022.csv","profile_path":"atlas/symbol_profiles/053/053800.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-03-16","entry_price":87500,"MFE_30D_pct":149.7,"MFE_90D_pct":149.7,"MFE_180D_pct":149.7,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.9,"MAE_90D_pct":-7.4,"MAE_180D_pct":-29.1,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-03-24","peak_price":218500,"drawdown_after_peak_pct":-71.6,"green_lateness_ratio":null,"four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_not_full_without_non_price_evidence","four_b_evidence_type":["price_only","positioning_overheat","control_premium_or_event_premium"],"four_c_protection_label":null,"trigger_outcome_label":"price_moved_without_evidence","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L12_C28_053800_AHNLAB_POLITICAL_EVENT_2022_2022-03-16_87500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R8L12_C28_T008","case_id":"R8L12_C28_030520_HANCOM_THEME_PREMIUM_2021","symbol":"030520","company_name":"한글과컴퓨터","round":"R8","loop":"12","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SOFTWARE_SECURITY_CONTRACT_RETENTION_RENEWAL_SAAS_MARGIN_BRIDGE_VS_THEME_EVENT_PREMIUM","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"software_security_contract_retention","loop_objective":"residual_missed_structural_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|coverage_gap_fill","trigger_type":"Stage2-theme-premium / 4C-watch","trigger_date":"2021-11-17","evidence_available_at_that_date":"public evidence available at or before trigger date; timing treated as next-tradable-close when intraday time was unclear","evidence_source":"historical public filings/reports/news summary; stock-web used only for OHLCV","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","explicit_event_cap","price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/030/030520/2021.csv","profile_path":"atlas/symbol_profiles/030/030520.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-11-17","entry_price":28400,"MFE_30D_pct":21.5,"MFE_90D_pct":21.5,"MFE_180D_pct":21.5,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.3,"MAE_90D_pct":-32.4,"MAE_180D_pct":-46.5,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-12-06","peak_price":34500,"drawdown_after_peak_pct":-55.9,"green_lateness_ratio":null,"four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"event_premium_4B_then_4C_watch","four_b_evidence_type":["price_only","control_premium_or_event_premium","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"false_positive_green","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L12_C28_030520_HANCOM_THEME_PREMIUM_2021_2021-11-17_28400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L12_C28_012510_DUZON_CLOUD_2020","trigger_id":"R8L12_C28_T001","symbol":"012510","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":8,"backlog_visibility_score":7,"margin_bridge_score":8,"revision_score":7,"relative_strength_score":6,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":-1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":8,"backlog_visibility_score":7,"margin_bridge_score":8,"revision_score":7,"relative_strength_score":6,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":-1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":[],"component_delta_explanation":"P0 proxy; no proposed shadow adjustment applied.","MFE_90D_pct":49.9,"MAE_90D_pct":-4.1,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"c28_contract_retention_shadow_profile","case_id":"R8L12_C28_012510_DUZON_CLOUD_2020","trigger_id":"R8L12_C28_T001","symbol":"012510","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":8,"backlog_visibility_score":7,"margin_bridge_score":8,"revision_score":7,"relative_strength_score":6,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":-1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":9,"backlog_visibility_score":8,"margin_bridge_score":10,"revision_score":8,"relative_strength_score":6,"customer_quality_score":9,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":-1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":88,"stage_label_after":"Stage3-Green","changed_components":["contract_score","margin_bridge_score","customer_quality_score"],"component_delta_explanation":"Enterprise software should receive incremental credit only when renewal base, cloud mix, and OP margin bridge are all visible; this case qualifies.","MFE_90D_pct":49.9,"MAE_90D_pct":-4.1,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L12_C28_263860_GENIANS_EDR_2023","trigger_id":"R8L12_C28_T004","symbol":"263860","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":7,"backlog_visibility_score":5,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":6,"customer_quality_score":7,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":-1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":7,"backlog_visibility_score":5,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":6,"customer_quality_score":7,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":-1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":74,"stage_label_after":"Stage2-Actionable","changed_components":[],"component_delta_explanation":"P0 proxy; no proposed shadow adjustment applied.","MFE_90D_pct":33.1,"MAE_90D_pct":-5.96,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"c28_contract_retention_shadow_profile","case_id":"R8L12_C28_263860_GENIANS_EDR_2023","trigger_id":"R8L12_C28_T004","symbol":"263860","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":7,"backlog_visibility_score":5,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":6,"customer_quality_score":7,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":-1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":8,"backlog_visibility_score":6,"margin_bridge_score":7,"revision_score":6,"relative_strength_score":6,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":-1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":79,"stage_label_after":"Stage3-Yellow","changed_components":["contract_score","customer_quality_score","margin_bridge_score"],"component_delta_explanation":"Security software with renewal/EDR expansion should not be treated like a one-off policy theme when retention and repeat-order evidence appear.","MFE_90D_pct":33.1,"MAE_90D_pct":-5.96,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L12_C28_136540_WINS_CONTRACT_RETENTION_NO_EXPLOSION_2020","trigger_id":"R8L12_C28_T006","symbol":"136540","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":7,"backlog_visibility_score":6,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":4,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":67,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":7,"backlog_visibility_score":6,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":4,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":67,"stage_label_after":"Stage2","changed_components":[],"component_delta_explanation":"P0 proxy; no proposed shadow adjustment applied.","MFE_90D_pct":17.6,"MAE_90D_pct":-5.8,"score_return_alignment_label":"correctly_capped","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"c28_contract_retention_shadow_profile","case_id":"R8L12_C28_136540_WINS_CONTRACT_RETENTION_NO_EXPLOSION_2020","trigger_id":"R8L12_C28_T006","symbol":"136540","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":7,"backlog_visibility_score":6,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":4,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":67,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":7,"backlog_visibility_score":6,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":4,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":66,"stage_label_after":"Stage2","changed_components":["margin_bridge_score"],"component_delta_explanation":"Durable maintenance without EPS acceleration should be capped; retention is necessary but not sufficient.","MFE_90D_pct":17.6,"MAE_90D_pct":-5.8,"score_return_alignment_label":"correctly_capped","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L12_C28_053800_AHNLAB_POLITICAL_EVENT_2022","trigger_id":"R8L12_C28_T007","symbol":"053800","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":10,"customer_quality_score":2,"policy_or_regulatory_score":5,"valuation_repricing_score":1,"execution_risk_score":-5,"legal_or_contract_risk_score":-1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":61,"stage_label_before":"Stage1/Event-watch","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":10,"customer_quality_score":2,"policy_or_regulatory_score":5,"valuation_repricing_score":1,"execution_risk_score":-5,"legal_or_contract_risk_score":-1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":61,"stage_label_after":"Stage1/Event-watch","changed_components":[],"component_delta_explanation":"P0 proxy; no proposed shadow adjustment applied.","MFE_90D_pct":149.7,"MAE_90D_pct":-7.4,"score_return_alignment_label":"counterexample_guarded","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"c28_contract_retention_shadow_profile","case_id":"R8L12_C28_053800_AHNLAB_POLITICAL_EVENT_2022","trigger_id":"R8L12_C28_T007","symbol":"053800","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":10,"customer_quality_score":2,"policy_or_regulatory_score":5,"valuation_repricing_score":1,"execution_risk_score":-5,"legal_or_contract_risk_score":-1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":61,"stage_label_before":"Stage1/Event-watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":10,"customer_quality_score":1,"policy_or_regulatory_score":2,"valuation_repricing_score":0,"execution_risk_score":-7,"legal_or_contract_risk_score":-1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":49,"stage_label_after":"4B-overlay-only / no-positive-stage","changed_components":["policy_or_regulatory_score","execution_risk_score","contract_score"],"component_delta_explanation":"Political/event premium should not inherit C28 security-software contract-retention credit.","MFE_90D_pct":149.7,"MAE_90D_pct":-7.4,"score_return_alignment_label":"counterexample_guarded","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L12_C28_030520_HANCOM_THEME_PREMIUM_2021","trigger_id":"R8L12_C28_T008","symbol":"030520","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":5,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":8,"customer_quality_score":3,"policy_or_regulatory_score":4,"valuation_repricing_score":3,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":68,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":8,"customer_quality_score":3,"policy_or_regulatory_score":4,"valuation_repricing_score":3,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":68,"stage_label_after":"Stage2-Actionable","changed_components":[],"component_delta_explanation":"P0 proxy; no proposed shadow adjustment applied.","MFE_90D_pct":21.5,"MAE_90D_pct":-32.4,"score_return_alignment_label":"false_positive_reduced","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"c28_contract_retention_shadow_profile","case_id":"R8L12_C28_030520_HANCOM_THEME_PREMIUM_2021","trigger_id":"R8L12_C28_T008","symbol":"030520","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":5,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":8,"customer_quality_score":3,"policy_or_regulatory_score":4,"valuation_repricing_score":3,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":68,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":3,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":1,"relative_strength_score":8,"customer_quality_score":2,"policy_or_regulatory_score":2,"valuation_repricing_score":1,"execution_risk_score":-7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":55,"stage_label_after":"Theme-event-watch / no-positive-stage","changed_components":["contract_score","margin_bridge_score","policy_or_regulatory_score","execution_risk_score"],"component_delta_explanation":"License/theme momentum without renewal-rate or SaaS margin bridge should be capped below positive Stage2-Actionable.","MFE_90D_pct":21.5,"MAE_90D_pct":-32.4,"score_return_alignment_label":"false_positive_reduced","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c28_recurring_contract_retention_gate,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,0,1,+1,"Promote only when renewal/maintenance or SaaS retention evidence combines with margin/revision bridge.","Raised Duzon/Genians while keeping Wins capped.","R8L12_C28_T001|R8L12_C28_T004|R8L12_C28_T006",5,5,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c28_theme_event_premium_cap,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,0,1,+1,"Political/metaverse/DID/security headlines cannot inherit software contract retention score.","Reduced AhnLab/Hancom false-positive positive-stage risk.","R8L12_C28_T007|R8L12_C28_T008",5,5,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c28_margin_bridge_required_for_green,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,0,1,+1,"Green requires renewal-to-OP or SaaS mix margin bridge; contract existence alone caps at Yellow.","Prevents retention-only Wins-like cases from reaching Green.","R8L12_C28_T006|R8L12_C28_T001",5,5,3,low,canonical_shadow_only,"not production; post-calibrated residual"
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R8","loop":"12","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","new_independent_case_count":5,"reused_case_count":0,"new_symbol_count":5,"new_trigger_family_count":4,"tested_existing_calibrated_axes":["stage3_green_total_min","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["current_profile_too_late","current_profile_missed_structural","current_profile_false_positive","theme_event_positive_stage_leakage"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.7 narrative_only rows

```jsonl
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
next_round = R9_loop_10_or_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
preferred_next_large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY or L9_CONSTRUCTION_REALESTATE_HOUSING depending on mobility/transport nature
preferred_next_canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
carry_forward_open_question = For C28, run a holdout batch on more pure SaaS/security names to decide whether c28_recurring_contract_retention_gate deserves promotion from shadow to config.
```

## 28. Source Notes

- Stock-Web manifest: `atlas/manifest.json`, max_date `2026-02-20`, generated_at `2026-05-21T16:28:39.421691+00:00`.
- Stock-Web schema: `atlas/schema.json`, calibration basis `tradable_raw`, adjustment status `raw_unadjusted_marcap`.
- Allowed stock_agent research artifacts checked: `reports/e2r_calibration/ingest_summary.md`, `reports/e2r_calibration/applied_scoring_diff.md`.
- Stock-Web profiles checked: `012510`, `263860`, `136540`, `053800`, `030520`.
- Stock-Web tradable shards checked: `012510/2020`, `263860/2023`, `136540/2020`, `053800/2022`, `030520/2021`, `030520/2022`.
