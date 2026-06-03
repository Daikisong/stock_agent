# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "output_file": "e2r_stock_web_v12_residual_round_R8_loop_12_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md",
  "scheduled_round": "R8",
  "scheduled_loop": 12,
  "completed_round": "R8",
  "completed_loop": 12,
  "next_round": "R9",
  "next_loop": 12,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
  "fine_archetype_id": "B2B_SAAS_SECURITY_RETENTION_VS_AI_POLITICAL_THEME_BLOWOFF",
  "loop_objective": [
    "coverage_gap_fill",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression",
    "counterexample_mining",
    "residual_false_positive_mining",
    "4B_non_price_requirement_stress_test",
    "green_strictness_stress_test"
  ],
  "price_source": "Songdaiki/stock-web",
  "stock_web_manifest_max_date": "2026-02-20",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "handoff_prompt_embedded": true,
  "handoff_prompt_executed_now": false
}
```

This loop adds **3** new independent cases, **1** counterexample, and **3** residual errors for **R8/L8_PLATFORM_CONTENT_SW_SECURITY/C28_SOFTWARE_SECURITY_CONTRACT_RETENTION**.

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

This file does not repeat the global claim that Stage2 is earlier than Green. The residual question is narrower: **inside C28, when does software/security narrative become durable paid-contract evidence, and when is it only AI/political/theme beta attached to a real software brand?**

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R8
scheduled_loop = 12
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id = B2B_SAAS_SECURITY_RETENTION_VS_AI_POLITICAL_THEME_BLOWOFF
round_schedule_status = valid
round_sector_consistency = pass
```

R8 is constrained to **L8_PLATFORM_CONTENT_SW_SECURITY**. Loop 10 already covered C27 content/IP and Loop 11 covered C26 platform/ad operating leverage in the local artifact set. Loop 12 therefore fills the C28 gap: B2B software, cybersecurity, document/productivity software, AI feature monetization, paid conversion, and contract-retention guardrails.

## 3. Previous Coverage / Duplicate Avoidance Check

Only research artifacts and local MD registry-style filenames were used for schedule and duplicate avoidance. No `src/e2r` code was opened or inferred.

```text
observed_prior_R8_loop_10 = C27_CONTENT_IP_GLOBAL_MONETIZATION
observed_prior_R8_loop_11 = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
scheduled_round_after_R7_loop_12 = R8
scheduled_loop_after_R7_loop_12 = 12
selected_canonical_gap = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
same_symbol_same_trigger_duplicates = 0
same_entry_group_duplicates = 0
new_symbol_count = 3
same_archetype_new_symbol_count = 3
new_trigger_family_count = 3
minimum_new_independent_case_ratio = 1.00
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest fields used:

```json
{
  "source_name": "FinanceData/marcap",
  "source_repo_url": "https://github.com/FinanceData/marcap",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "min_date": "1995-05-02",
  "max_date": "2026-02-20",
  "tradable_row_count": 14354401,
  "raw_row_count": 15214118,
  "symbol_count": 5414,
  "active_like_symbol_count": 2868,
  "inactive_or_delisted_like_symbol_count": 2546,
  "markets": [
    "KONEX",
    "KOSDAQ",
    "KOSDAQ GLOBAL",
    "KOSPI"
  ],
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv"
}
```

Validation:

```text
price_data_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
stock_web_manifest_max_date = 2026-02-20
validation_status = usable_for_historical_calibration
```

The inspected Stock-Web manifest confirms `price_adjustment_status = raw_unadjusted_marcap`, `max_date = 2026-02-20`, `tradable_row_count = 14354401`, `symbol_count = 5414`, and shard roots under `atlas/ohlcv_tradable_by_symbol_year` and `atlas/ohlcv_raw_by_symbol_year`.

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | 180D available by manifest max_date | profile CA overlap in 180D | calibration_usable |
| --- | --- | ---: | ---: | --- | --- | --- |
| R8L12_C28_DOUZONE_AI_ERP_RETENTION_2023 | 012510 | 2023-11-03 | 28,900 | yes | no; CA dates stop at 2009-12-09 | true |
| R8L12_C28_HANCOM_AI_DOCUMENT_SOFTWARE_2023 | 030520 | 2023-11-20 | 14,240 | yes | no; CA dates stop at 2006-12-05 | true |
| R8L12_C28_AHNLAB_POLITICAL_THEME_SECURITY_BRAND_2022 | 053800 | 2022-03-23 | 175,800 | yes | no; only CA candidate 2005-03-31 | true |

The 30D/90D/180D fields are calculated from inspected Stock-Web `tradable_raw` rows. 1Y/2Y are intentionally left null in machine rows unless explicitly recomputed; this MD is a trigger-level 180D calibration research file.

## 6. Canonical Archetype Compression Map

```text
C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
  ├─ ERP/accounting/enterprise software installed-base retention
  ├─ document/productivity software AI feature upsell
  ├─ cybersecurity brand/endpoint security retention
  └─ AI/political/theme blowoff guard when contract-retention evidence is absent
```

Compression rule: **C28 should reward durable paid software conversion, renewal, retention, enterprise deployment, or ARR-like visibility; it should cap theme-only AI/security/political price moves even when the underlying company is real.**

## 7. Case Selection Summary

| case_id | symbol | company_name | case_type | positive_or_counterexample | best_trigger | current_profile_verdict | score_price_alignment |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R8L12_C28_DOUZONE_AI_ERP_RETENTION_2023 | 012510 | 더존비즈온 | structural_success | positive | R8L12_C28_DOUZONE_T1_STAGE2_ACTIONABLE_2023-11-03 | current_profile_missed_structural | early installed-base/paid-conversion evidence captured much more 180D upside than waiting for later Green |
| R8L12_C28_HANCOM_AI_DOCUMENT_SOFTWARE_2023 | 030520 | 한글과컴퓨터 | high_mae_success | positive_with_4B_guard | R8L12_C28_HANCOM_T1_STAGE2_ACTIONABLE_2023-11-20 | current_profile_4B_too_late | early software installed-base + AI optionality produced large MFE, but peak required 4B overlay because retention evidence lagged price |
| R8L12_C28_AHNLAB_POLITICAL_THEME_SECURITY_BRAND_2022 | 053800 | 안랩 | false_positive_green | counterexample | R8L12_C28_AHNLAB_T1_PRICE_ONLY_BLOWOFF_2022-03-23 | current_profile_false_positive | real cybersecurity brand did not equal new contract-retention evidence; price-only/theme blowoff created severe MAE |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_case_count = 2
4C_case_count = 0
calibration_usable_case_count = 3
calibration_usable_trigger_count = 5
representative_trigger_count = 3
new_independent_case_count = 3
reused_case_count = 0
```

The case mix is intentionally not all-positive. C28 needs both a positive path and a false-positive guard because software/security names often carry credible product narratives while the price move is actually theme, politics, or AI-label compression.

## 9. Evidence Source Map

| case_id | evidence family | evidence timing rule | source handling |
| --- | --- | --- | --- |
| R8L12_C28_DOUZONE_AI_ERP_RETENTION_2023 | enterprise software installed base + AI/ERP paid conversion | Stage2 uses close on 2023-11-03; later Green confirmation uses 2024-04-09 | public earnings/software narrative + Stock-Web rows |
| R8L12_C28_HANCOM_AI_DOCUMENT_SOFTWARE_2023 | office/document installed base + AI feature optionality | Stage2 uses 2023-11-20 close; 4B overlay uses 2024-01-22 close/peak period | public AI document/productivity narrative + Stock-Web rows |
| R8L12_C28_AHNLAB_POLITICAL_THEME_SECURITY_BRAND_2022 | cybersecurity brand but no new contract-retention trigger | representative row uses 2022-03-23 close; 4B evidence comes from 2022-03-24 peak | public political/theme period + Stock-Web rows |

## 10. Price Data Source Map

| symbol | profile_path | tradable shards inspected | corporate_action_window_status |
| --- | --- | --- | --- |
| 012510 | atlas/symbol_profiles/012/012510.json | atlas/ohlcv_tradable_by_symbol_year/012/012510/2023.csv; 2024.csv | clean_180D_window |
| 030520 | atlas/symbol_profiles/030/030520.json | atlas/ohlcv_tradable_by_symbol_year/030/030520/2023.csv; 2024.csv | clean_180D_window |
| 053800 | atlas/symbol_profiles/053/053800.json | atlas/ohlcv_tradable_by_symbol_year/053/053800/2022.csv | clean_180D_window |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | symbol | company_name | trigger_type | trigger_date | entry_date | entry_price | current_profile_verdict | trigger_outcome_label |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R8L12_C28_DOUZONE_T1_STAGE2_ACTIONABLE_2023-11-03 | R8L12_C28_DOUZONE_AI_ERP_RETENTION_2023 | 012510 | 더존비즈온 | Stage2-Actionable | 2023-11-03 | 2023-11-03 | 28900 | current_profile_missed_structural | structural_success_high_MFE_clean_180D |
| R8L12_C28_DOUZONE_T2_STAGE3_GREEN_2024-04-09 | R8L12_C28_DOUZONE_AI_ERP_RETENTION_2023 | 012510 | 더존비즈온 | Stage3-Green | 2024-04-09 | 2024-04-09 | 57800 | current_profile_too_late | late_green_positive_but_missed_upside |
| R8L12_C28_HANCOM_T1_STAGE2_ACTIONABLE_2023-11-20 | R8L12_C28_HANCOM_AI_DOCUMENT_SOFTWARE_2023 | 030520 | 한글과컴퓨터 | Stage2-Actionable | 2023-11-20 | 2023-11-20 | 14240 | current_profile_4B_too_late | theme_plus_installed_base_success_but_needs_4B_overlay |
| R8L12_C28_HANCOM_T2_4B_OVERLAY_2024-01-22 | R8L12_C28_HANCOM_AI_DOCUMENT_SOFTWARE_2023 | 030520 | 한글과컴퓨터 | Stage4B-Overlay | 2024-01-22 | 2024-01-22 | 35150 | current_profile_4B_too_late | 4B_overlay_success_high_MAE_after_blowoff |
| R8L12_C28_AHNLAB_T1_PRICE_ONLY_BLOWOFF_2022-03-23 | R8L12_C28_AHNLAB_POLITICAL_THEME_SECURITY_BRAND_2022 | 053800 | 안랩 | Stage2-FalsePositiveCandidate | 2022-03-23 | 2022-03-23 | 175800 | current_profile_false_positive | false_positive_green_high_MAE |

## 12. Trigger-Level OHLC Backtest Tables

Representative triggers:

| trigger_id | symbol | entry_date | entry_price | MFE_30D_pct | MFE_90D_pct | MFE_180D_pct | MAE_30D_pct | MAE_90D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R8L12_C28_DOUZONE_T1_STAGE2_ACTIONABLE_2023-11-03 | 012510 | 2023-11-03 | 28900 | 6.4 | 94.81 | 170.93 | -2.6 | -2.6 | -2.6 | 2024-07-08 | 78300 | -27.08 |
| R8L12_C28_HANCOM_T1_STAGE2_ACTIONABLE_2023-11-20 | 030520 | 2023-11-20 | 14240 | 11.17 | 170.01 | 170.01 | -3.72 | -3.72 | -3.72 | 2024-01-22 | 38450 | -48.89 |
| R8L12_C28_AHNLAB_T1_PRICE_ONLY_BLOWOFF_2022-03-23 | 053800 | 2022-03-23 | 175800 | 24.29 | 24.29 | 24.29 | -46.59 | -53.92 | -66.5 | 2022-03-24 | 218500 | -73.04 |

Audit-only triggers:

| trigger_id | symbol | trigger_type | entry_date | entry_price | MFE_30D_pct | MFE_90D_pct | MAE_30D_pct | MAE_90D_pct | green_lateness_ratio | four_b_timing_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R8L12_C28_DOUZONE_T2_STAGE3_GREEN_2024-04-09 | 012510 | Stage3-Green | 2024-04-09 | 57800 | 13.49 | 35.47 | -9.0 | -9.0 | 0.585 | late_green_after_installed_base_signal |
| R8L12_C28_HANCOM_T2_4B_OVERLAY_2024-01-22 | 030520 | Stage4B-Overlay | 2024-01-22 | 35150 | 9.39 | 9.39 | -34.99 | -43.87 | not_applicable_4B | good_local_4B_overlay_but_not_4C |

## 13. Current Calibrated Profile Stress Test

| case_id | current profile likely action | actual OHLC result | verdict |
| --- | --- | --- | --- |
| R8L12_C28_DOUZONE_AI_ERP_RETENTION_2023 | Delay until confirmed revision/Green | Stage2 entry had MFE_180D +170.93% with MAE_180D -2.60% | current_profile_missed_structural |
| R8L12_C28_HANCOM_AI_DOCUMENT_SOFTWARE_2023 | Could over-promote AI/software narrative and under-apply 4B | MFE_90D +170.01%, then peak drawdown -48.89% | current_profile_4B_too_late |
| R8L12_C28_AHNLAB_POLITICAL_THEME_SECURITY_BRAND_2022 | Might over-credit security brand + relative strength | MFE_30D +24.29%, but MAE_180D -66.50% | current_profile_false_positive |

Answers to required stress-test questions:

```text
stage2_actionable_evidence_bonus:
  helpful for Douzone/Hancom only if the evidence is paid-conversion or installed-base linked.
  too generous for AhnLab if relative strength is not backed by contract-retention evidence.

yellow_threshold_75:
  acceptable for early C28 Yellow, but needs C28-specific evidence quality tags.

green_threshold_87 / revision_min_55:
  too late for Douzone if Green is the first investable stage;
  too loose for Hancom/AhnLab if price or AI/political theme substitutes for retention evidence.

price_only_blowoff_blocks_positive_stage:
  strengthened within C28.

full_4B_non_price_requirement:
  kept. Hancom/AhnLab are overlay/risk rows; not thesis-break 4C unless non-price evidence breaks.

hard_4C routing:
  kept. AhnLab is a theme unwind, not a hard software-contract thesis break.
```

## 14. Stage2 / Yellow / Green Comparison

Douzone is the clean Green-lateness audit:

```text
Stage2_Actionable_entry_price = 28,900
Stage3_Green_entry_price = 57,800
full_observed_peak_after_stage2 = 78,300
green_lateness_ratio = (57,800 - 28,900) / (78,300 - 28,900) = 0.585
```

Interpretation: Green captured some upside but spent more than half of the available Stage2-to-peak move. C28 should therefore allow a **Stage2-Actionable / early Yellow** when paid conversion, installed-base quality, and enterprise software visibility are present.

Hancom is the opposite audit: Stage2 was useful, but Green should be capped until retention evidence appears. A price move from 14,240 to a 38,450 high was real, but the later drawdown argues against treating AI feature/news as full Green.

AhnLab has no valid Green trigger in this C28 sense. The price surge is a 4B/false-positive guard case.

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | four_b_evidence_type | local proximity | full-window proximity | verdict |
| --- | --- | ---: | ---: | --- |
| R8L12_C28_HANCOM_T2_4B_OVERLAY_2024-01-22 | price_only; valuation_blowoff; positioning_overheat | 1.00 | 1.00 | good_local_4B_overlay_but_not_4C |
| R8L12_C28_AHNLAB_T1_PRICE_ONLY_BLOWOFF_2022-03-23 | price_only; valuation_blowoff; positioning_overheat | 0.805 | 0.805 | price_only_local_4B_should_block_positive_stage |

The key is not to turn every price spike into a sell signal. C28 4B is a **risk overlay**: it blocks positive-stage promotion when contract-retention evidence is absent, but it does not become hard 4C unless non-price evidence breaks the software/security thesis.

## 16. 4C Protection Audit

No hard 4C route is proposed in this loop.

```text
AhnLab = false_break_or_theme_unwind_not_fundamental_4C
Hancom = thesis_break_watch_only
Douzone = not_applicable
```

This is deliberate. The loop strengthens 4B and Green-gate behavior, not hard 4C. Hard 4C should remain reserved for contract cancellation, retention collapse, accounting/trust break, regulatory rejection, or verified commercial thesis failure.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
rule_name = L8_C28_SOFTWARE_SECURITY_RETENTION_QUALITY_GATE
candidate = true
```

Proposed sector rule:

```text
In L8 software/security, Stage2-Actionable may receive an early evidence bonus when:
  - installed base is visible,
  - paid conversion/renewal/enterprise deployment route is plausible,
  - financial visibility or margin bridge is not purely narrative,
  - and the trigger is not just price/political/AI theme.

If the evidence is only price + theme + brand:
  - cap below Green,
  - route to 4B-overlay watch,
  - do not treat as structural software-security rerating.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
candidate = true
```

C28-specific proposal:

```text
C28_green_retention_min_gate = true
C28_installed_base_paid_conversion_bonus = +2
C28_price_theme_4B_overlay_guard = -10 to positive-stage score
```

Mechanism: a software stock is like a subscription staircase. The staircase is valuable only if users keep paying on the next step. A product demo, political association, or AI label is more like a billboard: it can attract eyes, but it does not prove renewal cash flow. C28 should pay for stairs, not billboards.

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | score_return_alignment_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | 3 | 96.37 | -20.08 | 121.74 | -24.27 | 1/3 | 1 | 1 | mixed; misses early B2B SaaS and over-credits price/theme security brand |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 3 | 96.37 | -20.75 | 121.72 | -24.27 | 1/3 or higher | 1 | 1 | weaker because price-only blowoff can masquerade as C28 strength |
| P1_sector_specific_candidate_profile | sector_specific | 3 | 96.37 | -20.75 | 121.72 | -24.27 | 0/3 after AhnLab cap | 0 | 1 | better; keeps Douzone early, caps Hancom Green, blocks AhnLab false positive |
| P2_canonical_archetype_candidate_profile | canonical_archetype_specific | 3 | 96.37 | -20.75 | 121.72 | -24.27 | 0/3 after Green cap | 0 | 1 | best explanatory compression for C28 |
| P3_counterexample_guard_profile | counterexample_guard | 1 | 24.29 | -53.92 | 24.29 | -66.5 | 0/1 after guard | 0 | 0 | strongly improves false-positive handling |

## 20. Score-Return Alignment Matrix

| case_id | before score/stage | after score/stage | return alignment |
| --- | --- | --- | --- |
| R8L12_C28_DOUZONE_AI_ERP_RETENTION_2023 | 76 / Stage3-Yellow not Green | 84 / Stage2-Actionable early structural Yellow | Better: captures +170.93% MFE_180D with low MAE |
| R8L12_C28_HANCOM_AI_DOCUMENT_SOFTWARE_2023 | 79 / AI theme could over-promote | 76 / Stage2-Actionable only, Green blocked | Better: keeps upside but flags 4B drawdown risk |
| R8L12_C28_AHNLAB_POLITICAL_THEME_SECURITY_BRAND_2022 | 83 / false Green risk | 58 / 4B-overlay, positive-stage blocked | Better: avoids -66.50% MAE_180D false positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| L8_PLATFORM_CONTENT_SW_SECURITY | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | B2B_SAAS_SECURITY_RETENTION_VS_AI_POLITICAL_THEME_BLOWOFF | 2 | 1 | 2 | 0 | 3 | 0 | 5 | 3 | 3 | true | true | C28 now has positive, counterexample, and 4B overlay coverage; hard 4C still under-covered |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3

tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence

residual_error_types_found:
  - current_profile_missed_structural
  - current_profile_4B_too_late
  - current_profile_false_positive

new_axis_proposed:
  - C28_installed_base_paid_conversion_bonus
  - C28_green_retention_min_gate
  - C28_price_theme_4B_overlay_guard

existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence

existing_axis_weakened: null
existing_axis_kept:
  - stage3_yellow_total_min
  - stage3_green_total_min
  - hard_4c_thesis_break_routes_to_4c

sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null

loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- scheduled_round / scheduled_loop consistency
- R8 -> L8 round-sector consistency
- stock-web manifest max_date and price basis
- symbol profile availability and corporate-action candidate dates
- actual stock-web row values for entry/peak/low anchors
- 30D/90D/180D research-proxy MFE/MAE for representative triggers
- same_entry_group_id dedupe behavior
- positive/counterexample balance
```

Not validated:

```text
- no production scoring code
- no src/e2r access
- no live candidate scan
- no broker/API usage
- no current recommendation
- no automated full-ledger ingestion
- no 1Y/2Y quantitative calibration beyond marked null fields
```

Before batch implementation, the coding agent should recompute all MFE/MAE from full stock-web CSV rows. This MD supplies the research rows, cases, and expected direction of the C28 shadow rule.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C28_installed_base_paid_conversion_bonus,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,0,+2,+2,"ERP/document/security software with visible installed base and paid conversion deserves earlier Yellow before full Green.","Improves Douzone early capture without promoting Hancom/AhnLab to Green.","R8L12_C28_DOUZONE_T1_STAGE2_ACTIONABLE_2023-11-03|R8L12_C28_HANCOM_T1_STAGE2_ACTIONABLE_2023-11-20",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C28_green_retention_min_gate,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,false,true,+1,"C28 Green should require retention/ARR/enterprise deployment or renewal evidence, not AI feature news or security brand value alone.","Blocks AhnLab false positive and caps Hancom theme phase while retaining Douzone Yellow.","R8L12_C28_HANCOM_T2_4B_OVERLAY_2024-01-22|R8L12_C28_AHNLAB_T1_PRICE_ONLY_BLOWOFF_2022-03-23",3,3,1,medium,canonical_shadow_only,"not production; Green gate candidate"
shadow_weight,C28_price_theme_4B_overlay_guard,sector_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,0,-10,-10,"Fast price/political/AI theme blowoff without retention evidence should route to 4B overlay and block positive-stage promotion.","AhnLab MAE_180D -66.5% demonstrates why this should be an overlay guard.","R8L12_C28_AHNLAB_T1_PRICE_ONLY_BLOWOFF_2022-03-23",3,3,1,medium,sector_shadow_only,"strengthens existing price_only_blowoff guard within C28"

```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R8L12_C28_DOUZONE_AI_ERP_RETENTION_2023","symbol":"012510","company_name":"더존비즈온","round":"R8","loop":"12","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"B2B_SAAS_SECURITY_RETENTION_VS_AI_POLITICAL_THEME_BLOWOFF","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R8L12_C28_DOUZONE_T1_STAGE2_ACTIONABLE_2023-11-03","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"early installed-base/paid-conversion evidence captured much more 180D upside than waiting for later Green","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"C28 positive case for B2B ERP/SaaS retention and AI upsell."}
{"row_type":"case","case_id":"R8L12_C28_HANCOM_AI_DOCUMENT_SOFTWARE_2023","symbol":"030520","company_name":"한글과컴퓨터","round":"R8","loop":"12","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"B2B_SAAS_SECURITY_RETENTION_VS_AI_POLITICAL_THEME_BLOWOFF","case_type":"high_mae_success","positive_or_counterexample":"positive_with_4B_guard","best_trigger":"R8L12_C28_HANCOM_T1_STAGE2_ACTIONABLE_2023-11-20","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"early software installed-base + AI optionality produced large MFE, but peak required 4B overlay because retention evidence lagged price","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"Positive price path, but not a clean Green without paid retention."}
{"row_type":"case","case_id":"R8L12_C28_AHNLAB_POLITICAL_THEME_SECURITY_BRAND_2022","symbol":"053800","company_name":"안랩","round":"R8","loop":"12","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"B2B_SAAS_SECURITY_RETENTION_VS_AI_POLITICAL_THEME_BLOWOFF","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R8L12_C28_AHNLAB_T1_PRICE_ONLY_BLOWOFF_2022-03-23","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"real cybersecurity brand did not equal new contract-retention evidence; price-only/theme blowoff created severe MAE","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C28 counterexample for theme momentum masquerading as software-security rerating."}
{"row_type":"trigger","trigger_id":"R8L12_C28_DOUZONE_T1_STAGE2_ACTIONABLE_2023-11-03","case_id":"R8L12_C28_DOUZONE_AI_ERP_RETENTION_2023","symbol":"012510","company_name":"더존비즈온","round":"R8","loop":"12","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"B2B_SAAS_SECURITY_RETENTION_VS_AI_POLITICAL_THEME_BLOWOFF","sector":"enterprise_erp_saas","primary_archetype":"ERP SaaS installed-base retention with AI/Amaranth conversion route","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2023-11-03","entry_date":"2023-11-03","entry_price":28900,"evidence_available_at_that_date":"Enterprise software revenue and profit recovery was visible before the later AI/ERP rerating; the thesis was not just AI theme beta because it had an installed ERP/WEHAGO/Amaranth customer base that could convert into paid software renewal or upsell.","evidence_source":"public earnings/enterprise-software narrative; stock-web rows 2023-11-03, 2024-01 to 2024-07","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","early_revision_signal","capacity_or_volume_route"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012510/2023.csv|atlas/ohlcv_tradable_by_symbol_year/012/012510/2024.csv","profile_path":"atlas/symbol_profiles/012/012510.json","MFE_30D_pct":6.4,"MFE_90D_pct":94.81,"MFE_180D_pct":170.93,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.6,"MAE_90D_pct":-2.6,"MAE_180D_pct":-2.6,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-08","peak_price":78300,"drawdown_after_peak_pct":-27.08,"green_lateness_ratio":"not_applicable_stage2_base","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success_high_MFE_clean_180D","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L12_C28_DOUZONE_2023-11-03_28900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":4,"margin_bridge_score":10,"revision_score":12,"relative_strength_score":6,"customer_quality_score":12,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow / not Green","raw_component_scores_after":{"contract_score":8,"backlog_visibility_score":8,"margin_bridge_score":12,"revision_score":14,"relative_strength_score":8,"customer_quality_score":16,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":84,"stage_label_after":"Stage2-Actionable promoted to C28 early structural Yellow","changed_components":["contract_score","backlog_visibility_score","customer_quality_score"],"component_delta_explanation":"C28 gives more shadow credit to installed-base paid conversion and renewal visibility before the later price rerating.","score_return_alignment_label":"after_profile_better_alignment"}
{"row_type":"trigger","trigger_id":"R8L12_C28_DOUZONE_T2_STAGE3_GREEN_2024-04-09","case_id":"R8L12_C28_DOUZONE_AI_ERP_RETENTION_2023","symbol":"012510","company_name":"더존비즈온","round":"R8","loop":"12","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"B2B_SAAS_SECURITY_RETENTION_VS_AI_POLITICAL_THEME_BLOWOFF","sector":"enterprise_erp_saas","primary_archetype":"confirmed AI/ERP monetization and financial visibility","loop_objective":"green_strictness_stress_test|canonical_archetype_compression","trigger_type":"Stage3-Green","trigger_date":"2024-04-09","entry_date":"2024-04-09","entry_price":57800,"evidence_available_at_that_date":"By April 2024, the market had stronger evidence that AI/ERP monetization and earnings recovery were not just a single quarter bounce. Waiting for this confirmation, however, consumed a large part of the upside from the November entry.","evidence_source":"stock-web 2024-04-09 row and subsequent follow-through","stage2_evidence_fields":["customer_or_order_quality","relative_strength"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012510/2024.csv","profile_path":"atlas/symbol_profiles/012/012510.json","MFE_30D_pct":13.49,"MFE_90D_pct":35.47,"MFE_180D_pct":35.47,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-9.0,"MAE_90D_pct":-9.0,"MAE_180D_pct":-9.0,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-08","peak_price":78300,"drawdown_after_peak_pct":-27.08,"green_lateness_ratio":0.585,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"late_green_after_installed_base_signal","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"late_green_positive_but_missed_upside","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L12_C28_DOUZONE_2024-04-09_57800","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":false,"reuse_reason":"same case used only for Green lateness audit","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"raw_component_scores_before":{"contract_score":6,"backlog_visibility_score":8,"margin_bridge_score":14,"revision_score":16,"relative_strength_score":12,"customer_quality_score":16,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":88,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":8,"backlog_visibility_score":10,"margin_bridge_score":14,"revision_score":16,"relative_strength_score":12,"customer_quality_score":18,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":91,"stage_label_after":"Stage3-Green but late","changed_components":["contract_score","customer_quality_score"],"component_delta_explanation":"Confirmation remains Green, but the lateness audit argues for earlier Yellow when paid conversion evidence exists.","score_return_alignment_label":"green_late_but_valid"}
{"row_type":"trigger","trigger_id":"R8L12_C28_HANCOM_T1_STAGE2_ACTIONABLE_2023-11-20","case_id":"R8L12_C28_HANCOM_AI_DOCUMENT_SOFTWARE_2023","symbol":"030520","company_name":"한글과컴퓨터","round":"R8","loop":"12","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"B2B_SAAS_SECURITY_RETENTION_VS_AI_POLITICAL_THEME_BLOWOFF","sector":"document_productivity_ai_software","primary_archetype":"office/document installed base plus AI feature upsell","loop_objective":"coverage_gap_fill|4B_non_price_requirement_stress_test|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2023-11-20","entry_date":"2023-11-20","entry_price":14240,"evidence_available_at_that_date":"The stock began to price AI document/software optionality before the January 2024 blowoff. The positive part is installed office/document software distribution; the guard is that AI feature demos alone should not be treated as durable contract-retention Green.","evidence_source":"public AI document/productivity software narrative; stock-web rows 2023-11-20, 2024-01 to 2024-07","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","early_revision_signal","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/030/030520/2023.csv|atlas/ohlcv_tradable_by_symbol_year/030/030520/2024.csv","profile_path":"atlas/symbol_profiles/030/030520.json","MFE_30D_pct":11.17,"MFE_90D_pct":170.01,"MFE_180D_pct":170.01,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-3.72,"MAE_90D_pct":-3.72,"MAE_180D_pct":-3.72,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-22","peak_price":38450,"drawdown_after_peak_pct":-48.89,"green_lateness_ratio":"not_applicable_no_confirmed_retention_green","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"theme_plus_installed_base_success_but_needs_4B_overlay","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L12_C28_HANCOM_2023-11-20_14240","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":6,"relative_strength_score":14,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":14,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":79,"stage_label_before":"Stage3-Yellow / could over-promote on AI theme","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":6,"relative_strength_score":14,"customer_quality_score":10,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":76,"stage_label_after":"Stage2-Actionable / Yellow only, Green blocked until retention proof","changed_components":["valuation_repricing_score","execution_risk_score","customer_quality_score"],"component_delta_explanation":"C28 caps AI feature/theme rerating unless paid-seat, renewal, retention, or enterprise deployment evidence is present.","score_return_alignment_label":"after_profile_better_risk_alignment"}
{"row_type":"trigger","trigger_id":"R8L12_C28_HANCOM_T2_4B_OVERLAY_2024-01-22","case_id":"R8L12_C28_HANCOM_AI_DOCUMENT_SOFTWARE_2023","symbol":"030520","company_name":"한글과컴퓨터","round":"R8","loop":"12","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"B2B_SAAS_SECURITY_RETENTION_VS_AI_POLITICAL_THEME_BLOWOFF","sector":"document_productivity_ai_software","primary_archetype":"AI software positioning overheat without enough retention evidence","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B-Overlay","trigger_date":"2024-01-22","entry_date":"2024-01-22","entry_price":35150,"evidence_available_at_that_date":"The move had become a fast AI-software rerating. Because non-price thesis break evidence was not yet present, this is a 4B overlay rather than a hard 4C, but the later drawdown shows why C28 needs a retention/paid-conversion guard.","evidence_source":"stock-web 2024-01-22 peak row and forward drawdown rows","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/030/030520/2024.csv","profile_path":"atlas/symbol_profiles/030/030520.json","MFE_30D_pct":9.39,"MFE_90D_pct":9.39,"MFE_180D_pct":9.39,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-34.99,"MAE_90D_pct":-43.87,"MAE_180D_pct":-44.1,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-22","peak_price":38450,"drawdown_after_peak_pct":-48.89,"green_lateness_ratio":"not_applicable_4B","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_local_4B_overlay_but_not_4C","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success_high_MAE_after_blowoff","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L12_C28_HANCOM_2024-01-22_35150","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same case used only for 4B timing audit","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":20,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":18,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":84,"stage_label_before":"Stage3-Yellow/possible false Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":18,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":18,"execution_risk_score":-12,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":74,"stage_label_after":"4B-overlay / Green blocked","changed_components":["execution_risk_score","customer_quality_score"],"component_delta_explanation":"Fast theme rerating is separated from paid retention evidence.","score_return_alignment_label":"4B_overlay_improves_drawdown_control"}
{"row_type":"trigger","trigger_id":"R8L12_C28_AHNLAB_T1_PRICE_ONLY_BLOWOFF_2022-03-23","case_id":"R8L12_C28_AHNLAB_POLITICAL_THEME_SECURITY_BRAND_2022","symbol":"053800","company_name":"안랩","round":"R8","loop":"12","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"B2B_SAAS_SECURITY_RETENTION_VS_AI_POLITICAL_THEME_BLOWOFF","sector":"cybersecurity_endpoint","primary_archetype":"security brand plus political/theme blowoff without contract-retention evidence","loop_objective":"counterexample_mining|residual_false_positive_mining|4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositiveCandidate","trigger_date":"2022-03-23","entry_date":"2022-03-23","entry_price":175800,"evidence_available_at_that_date":"The stock move was dominated by political/theme and price momentum rather than new enterprise security contract-retention evidence. C28 should not promote this as software-security Green merely because the company is a real cybersecurity brand.","evidence_source":"public political-theme period; stock-web 2022-03-23/24 and forward rows","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/053/053800/2022.csv","profile_path":"atlas/symbol_profiles/053/053800.json","MFE_30D_pct":24.29,"MFE_90D_pct":24.29,"MFE_180D_pct":24.29,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-46.59,"MAE_90D_pct":-53.92,"MAE_180D_pct":-66.5,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-03-24","peak_price":218500,"drawdown_after_peak_pct":-73.04,"green_lateness_ratio":"not_applicable_no_green","four_b_local_peak_proximity":0.805,"four_b_full_window_peak_proximity":0.805,"four_b_timing_verdict":"price_only_local_4B_should_block_positive_stage","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"false_break_or_theme_unwind_not_fundamental_4C","trigger_outcome_label":"false_positive_green_high_MAE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L12_C28_AHNLAB_2022-03-23_175800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":4,"relative_strength_score":20,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":18,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":83,"stage_label_before":"Stage3-Yellow/false Green risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":12,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":-18,"legal_or_contract_risk_score":-4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":58,"stage_label_after":"4B-overlay / positive-stage blocked","changed_components":["relative_strength_score","valuation_repricing_score","execution_risk_score","customer_quality_score"],"component_delta_explanation":"C28 distinguishes real cybersecurity company quality from investable contract-retention evidence.","score_return_alignment_label":"after_profile_reduces_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L12_C28_DOUZONE_AI_ERP_RETENTION_2023","trigger_id":"R8L12_C28_DOUZONE_T1_STAGE2_ACTIONABLE_2023-11-03","symbol":"012510","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":4,"margin_bridge_score":10,"revision_score":12,"relative_strength_score":6,"customer_quality_score":12,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow / not Green","raw_component_scores_after":{"contract_score":8,"backlog_visibility_score":8,"margin_bridge_score":12,"revision_score":14,"relative_strength_score":8,"customer_quality_score":16,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":84,"stage_label_after":"Stage2-Actionable promoted to C28 early structural Yellow","changed_components":["contract_score","backlog_visibility_score","customer_quality_score"],"component_delta_explanation":"C28 gives more shadow credit to installed-base paid conversion and renewal visibility before the later price rerating.","MFE_90D_pct":94.81,"MAE_90D_pct":-2.6,"score_return_alignment_label":"after_profile_better_alignment","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L12_C28_HANCOM_AI_DOCUMENT_SOFTWARE_2023","trigger_id":"R8L12_C28_HANCOM_T1_STAGE2_ACTIONABLE_2023-11-20","symbol":"030520","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":6,"relative_strength_score":14,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":14,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":79,"stage_label_before":"Stage3-Yellow / could over-promote on AI theme","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":6,"relative_strength_score":14,"customer_quality_score":10,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":76,"stage_label_after":"Stage2-Actionable / Yellow only, Green blocked until retention proof","changed_components":["valuation_repricing_score","execution_risk_score","customer_quality_score"],"component_delta_explanation":"C28 caps AI feature/theme rerating unless paid-seat, renewal, retention, or enterprise deployment evidence is present.","MFE_90D_pct":170.01,"MAE_90D_pct":-3.72,"score_return_alignment_label":"after_profile_better_risk_alignment","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L12_C28_AHNLAB_POLITICAL_THEME_SECURITY_BRAND_2022","trigger_id":"R8L12_C28_AHNLAB_T1_PRICE_ONLY_BLOWOFF_2022-03-23","symbol":"053800","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":4,"relative_strength_score":20,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":18,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":83,"stage_label_before":"Stage3-Yellow/false Green risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":12,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":-18,"legal_or_contract_risk_score":-4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":58,"stage_label_after":"4B-overlay / positive-stage blocked","changed_components":["relative_strength_score","valuation_repricing_score","execution_risk_score","customer_quality_score"],"component_delta_explanation":"C28 distinguishes real cybersecurity company quality from investable contract-retention evidence.","MFE_90D_pct":24.29,"MAE_90D_pct":-53.92,"score_return_alignment_label":"after_profile_reduces_false_positive","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R8","loop":"12","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3,"new_trigger_family_count":3,"positive_case_count":2,"counterexample_count":1,"current_profile_error_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["current_profile_missed_structural","current_profile_4B_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row.
Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

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
completed_loop = 12
next_round = R9
next_loop = 12
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-web files inspected:

```text
https://github.com/Songdaiki/stock-web/blob/main/atlas/manifest.json
https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/012/012510.json
https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/012/012510/2023.csv
https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/012/012510/2024.csv
https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/030/030520.json
https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/030/030520/2023.csv
https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/030/030520/2024.csv
https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/053/053800.json
https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/053/053800/2022.csv
```

No investment recommendation is made. This is historical calibration research only.
