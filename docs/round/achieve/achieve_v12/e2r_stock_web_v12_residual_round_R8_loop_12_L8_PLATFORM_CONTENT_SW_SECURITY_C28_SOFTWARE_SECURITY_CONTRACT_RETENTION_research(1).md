# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R8
loop = 12
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id = ENTERPRISE_SOFTWARE_AI_CLOUD_CONTRACT_RETENTION
output_file = e2r_stock_web_v12_residual_round_R8_loop_12_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md
created_at = 2026-05-25 Asia/Seoul
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This file is historical calibration research only. It is not current/live stock discovery, not a watchlist, not an investment recommendation, and not a `stock_agent` code patch.

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

This loop does not re-prove the global profile. It adds a C28-specific residual rule candidate: enterprise software / security / AI-SaaS labels should not promote to Green unless paid contract retention, ARR/renewal, enterprise seat expansion, or visible margin conversion is present. Price-only or event-premium software/security moves are treated as guard/4B rows.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R8
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_ids =
  - ENTERPRISE_AI_ERP_SAAS_RETENTION
  - AI_OFFICE_CLOUD_DOCUMENT_SUBSCRIPTION
  - SECURITY_VENDOR_EVENT_PREMIUM_COUNTEREXAMPLE
  - AI_HUMAN_SAAS_WITHOUT_RETENTION_COUNTEREXAMPLE
```

Selected objective set:

```text
coverage_gap_fill
counterexample_mining
residual_false_positive_mining
sector_specific_rule_discovery
canonical_archetype_compression
4B_non_price_requirement_stress_test
```

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed `stock_agent` research artifacts only were checked. The ingest summary shows 107 parsed result MDs, 1,940 validated trigger rows, and all R1-R13 sectors covered, but the direct search for `C28_SOFTWARE_SECURITY_CONTRACT_RETENTION 012510 030520 053800 047560` returned no result in the accessible artifact index.

```text
auto_selected_coverage_gap = R8_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
new_canonical_archetype_count = 1
new_symbol_count = 4
same_archetype_new_symbol_count = 4
new_trigger_family_count = 4
reused_case_count = 0
```

Duplicate/novelty verdict:

```text
minimum_new_independent_case_ratio_required = 0.60
new_independent_case_ratio_actual = 1.00
minimum_new_symbol_count_required = 2
new_symbol_count_actual = 4
minimum_positive_case_count_required = 1
positive_case_count_actual = 2
minimum_counterexample_count_required = 1
counterexample_count_actual = 2
```

The loop is not schema rematerialization. It is a new canonical-archetype coverage fill with positive and counterexample balance.

## 4. Stock-Web OHLC Input / Price Source Validation

| item | path | validation |
| --- | --- | --- |
| manifest | atlas/manifest.json | source_name=FinanceData/marcap; price_adjustment_status=raw_unadjusted_marcap; max_date=2026-02-20; tradable_row_count=14,354,401 |
| schema | atlas/schema.json | tradable columns d/o/h/l/c/v/a/mc/s/m; MFE/MAE formulas; 180D calibration usable rules |
| 012510 profile | atlas/symbol_profiles/012/012510.json | active_like; last_date=2026-02-20; corporate action candidates only 2002/2006/2009 |
| 030520 profile | atlas/symbol_profiles/030/030520.json | active_like; last_date=2026-02-20; corporate action candidates pre-2007 |
| 053800 profile | atlas/symbol_profiles/053/053800.json | active_like; last_date=2026-02-20; corporate action candidate only 2005 |
| 047560 profile | atlas/symbol_profiles/047/047560.json | active_like; last_date=2026-02-20; corporate action candidates only 2015 |

Manifest fields checked:

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

Important caveat: `price_basis = tradable_raw`, not adjusted OHLC. Corporate-action windows are blocked by default. For the four selected windows, the symbol-profile corporate action candidates are years before the tested windows, so the 180D windows are clean for calibration.

## 5. Historical Eligibility Gate

All representative triggers pass the 180D calibration gate.

| case_id | symbol | entry_date | entry_price | 180D forward window | corporate action 180D status | calibration_usable |
| --- | --- | --- | --- | --- | --- | --- |
| C28_DUZON_2024_AI_ERP_RETENTION_POS | 012510 | 2024-01-04 | 29100 | available_in_stock_web_by_manifest_max_date_2026-02-20 | clean_180D_window | True |
| C28_HANCOM_2023_AI_DOCS_OFFICE_POS | 030520 | 2023-11-24 | 15250 | available_in_stock_web_by_manifest_max_date_2026-02-20 | clean_180D_window | True |
| C28_AHNLAB_2022_SECURITY_EVENT_PREMIUM_COUNTER | 053800 | 2022-03-23 | 175800 | available_in_stock_web_by_manifest_max_date_2026-02-20 | clean_180D_window | True |
| C28_ESTSOFT_2024_AI_HUMAN_HYPE_COUNTER | 047560 | 2024-01-08 | 25650 | available_in_stock_web_by_manifest_max_date_2026-02-20 | clean_180D_window | True |

## 6. Canonical Archetype Compression Map

```text
C28_SOFTWARE_SECURITY_CONTRACT_RETENTION =
  enterprise software recurring/license/seat expansion
  + security software managed service/contract renewal
  + AI software only if paid conversion or enterprise deployment is visible
  - excludes event/control/political premium
  - excludes pure AI-feature demos with no retention/ARR/revision bridge
```

Compression decision:

```text
Duzon = positive enterprise ERP/SaaS/AI monetization route
Hancom = positive but volatile AI-office/cloud subscription route
AhnLab = counterexample; security wrapper but event/control premium
ESTsoft = counterexample; AI-human/SaaS language without paid retention visibility
```

## 7. Case Selection Summary

| case_id | symbol | company | role | case_type | trigger_date | entry_date | entry_price | MFE_90D | MAE_90D | MFE_180D | MAE_180D | current_profile_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C28_DUZON_2024_AI_ERP_RETENTION_POS | 012510 | 더존비즈온 | positive | structural_success | 2024-01-04 | 2024-01-04 | 29100 | 117.53 | -0.86 | 169.07 | -0.86 | current_profile_correct |
| C28_HANCOM_2023_AI_DOCS_OFFICE_POS | 030520 | 한글과컴퓨터 | positive | high_mae_success | 2023-11-24 | 2023-11-24 | 15250 | 152.13 | -10.1 | 152.13 | -10.1 | current_profile_correct |
| C28_AHNLAB_2022_SECURITY_EVENT_PREMIUM_COUNTER | 053800 | 안랩 | counterexample | false_positive_green | 2022-03-23 | 2022-03-23 | 175800 | 24.29 | -53.92 | 24.29 | -66.5 | current_profile_4B_too_late |
| C28_ESTSOFT_2024_AI_HUMAN_HYPE_COUNTER | 047560 | 이스트소프트 | counterexample | price_moved_without_evidence | 2024-01-05 | 2024-01-08 | 25650 | 94.15 | -14.81 | 94.15 | -56.26 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 2
4C_case_count = 0
calibration_usable_case_count = 4
```

The balance is important. C28 is not simply “software goes up when AI appears.” It is closer to an office building lease: the headline is the signboard, but the durable value is the monthly rent roll. The positive rows have a credible path from software feature/product to paid enterprise use; the counterexamples have price heat without rent-roll proof.

## 9. Evidence Source Map

| case_id | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence |
|---|---|---|---|---|
| C28_DUZON_2024_AI_ERP_RETENTION_POS | AI ERP/SaaS monetization route, customer/order quality, early revision signal | financial visibility, revision and margin bridge later confirmed | none for entry; later valuation fatigue watched | none |
| C28_HANCOM_2023_AI_DOCS_OFFICE_POS | AI office/document and cloud subscription optionality, early relative strength | partial financial visibility, not enough to relax Green without paid conversion | volatility/positioning watch | none |
| C28_AHNLAB_2022_SECURITY_EVENT_PREMIUM_COUNTER | relative strength only | none | event/control premium, positioning overheat, valuation blowoff | thesis did not become C28 contract-retention thesis |
| C28_ESTSOFT_2024_AI_HUMAN_HYPE_COUNTER | AI-human/SaaS feature headline, relative strength | none | price-only blowoff and positioning overheat | paid retention thesis unproven |

## 10. Price Data Source Map

| symbol | company | profile_path | primary shard(s) | profile status |
|---|---|---|---|---|
| 012510 | 더존비즈온 | atlas/symbol_profiles/012/012510.json | atlas/ohlcv_tradable_by_symbol_year/012/012510/2024.csv | active_like; clean tested window |
| 030520 | 한글과컴퓨터 | atlas/symbol_profiles/030/030520.json | atlas/ohlcv_tradable_by_symbol_year/030/030520/2023.csv; 2024.csv | active_like; clean tested window |
| 053800 | 안랩 | atlas/symbol_profiles/053/053800.json | atlas/ohlcv_tradable_by_symbol_year/053/053800/2022.csv | active_like; clean tested window |
| 047560 | 이스트소프트 | atlas/symbol_profiles/047/047560.json | atlas/ohlcv_tradable_by_symbol_year/047/047560/2024.csv | active_like; clean tested window |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | drawdown_after_peak | green_lateness | current_profile_verdict | aggregate_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R8L12_C28_DUZON_STAGE2_20240104 | 012510 | Stage2-Actionable | 2024-01-04 | 2024-01-04 | 29100 | 81.44 | 117.53 | 169.07 | -0.86 | -0.86 | -0.86 | 2024-07-08 | 78300 | -42.66 | null | current_profile_correct | representative |
| R8L12_C28_DUZON_GREEN_20240404 | 012510 | Stage3-Green | 2024-04-04 | 2024-04-04 | 53300 | 46.9 | 46.9 | 46.9 | -9.57 | -15.76 | -15.76 | 2024-07-08 | 78300 | -42.66 | 0.492 | current_profile_too_late | label_comparison_only |
| R8L12_C28_HANCOM_STAGE2_20231124 | 030520 | Stage2-Actionable | 2023-11-24 | 2023-11-24 | 15250 | 49.18 | 152.13 | 152.13 | -10.1 | -10.1 | -10.1 | 2024-01-22 | 38450 | -60.73 | null | current_profile_correct | representative |
| R8L12_C28_HANCOM_GREEN_20240110 | 030520 | Stage3-Green-candidate | 2024-01-10 | 2024-01-10 | 24750 | 55.35 | 55.35 | 55.35 | -17.58 | -20.28 | -38.99 | 2024-01-22 | 38450 | -60.73 | 0.409 | current_profile_too_late | label_comparison_only |
| R8L12_C28_AHNLAB_EVENT_PREMIUM_20220323 | 053800 | Stage2-blocked/4B-overlay | 2022-03-23 | 2022-03-23 | 175800 | 24.29 | 24.29 | 24.29 | -46.53 | -53.92 | -66.5 | 2022-03-24 | 218500 | -73.04 | null | current_profile_4B_too_late | representative |
| R8L12_C28_ESTSOFT_AI_HYPE_20240108 | 047560 | Stage2-blocked/price-moved-without-retention | 2024-01-05 | 2024-01-08 | 25650 | 94.15 | 94.15 | 94.15 | -13.26 | -14.81 | -56.26 | 2024-01-29 | 49800 | -77.47 | null | current_profile_false_positive | representative |

## 12. Trigger-Level OHLC Backtest Tables

### 12.1 더존비즈온 / 012510

- Entry row: 2024-01-04 close 29,100.
- Max high in 30D window: 52,800.
- Max high in 90D window: 63,300.
- Max high in 180D window: 78,300.
- Min low in 180D window: 28,850.
- Full observed post-peak low used for drawdown audit: 44,900.

```text
MFE_30D = 81.44%
MFE_90D = 117.53%
MFE_180D = 169.07%
MAE_30D = -0.86%
MAE_90D = -0.86%
MAE_180D = -0.86%
```

### 12.2 한글과컴퓨터 / 030520

- Entry row: 2023-11-24 close 15,250.
- Max high in 30D window: 22,750.
- Max high in 90D/180D window: 38,450.
- Min low in 30D/90D/180D window: 13,710.
- Full observed post-peak low used for drawdown audit: 15,100.

```text
MFE_30D = 49.18%
MFE_90D = 152.13%
MFE_180D = 152.13%
MAE_30D = -10.10%
MAE_90D = -10.10%
MAE_180D = -10.10%
```

### 12.3 안랩 / 053800

- Entry row: 2022-03-23 close 175,800.
- Max high in 30D/90D/180D window: 218,500.
- Min low in 30D window: 94,000.
- Min low in 90D window: 81,000.
- Min low in 180D window: 58,900.

```text
MFE_30D = 24.29%
MFE_90D = 24.29%
MFE_180D = 24.29%
MAE_30D = -46.53%
MAE_90D = -53.92%
MAE_180D = -66.50%
```

### 12.4 이스트소프트 / 047560

- Entry row: 2024-01-08 close 25,650.
- Max high in 30D/90D/180D window: 49,800.
- Min low in 30D window: 22,250.
- Min low in 90D window: 21,850.
- Min low in 180D window: 11,220.

```text
MFE_30D = 94.15%
MFE_90D = 94.15%
MFE_180D = 94.15%
MAE_30D = -13.26%
MAE_90D = -14.81%
MAE_180D = -56.26%
```

## 13. Current Calibrated Profile Stress Test

| case_id | current profile behavior | actual path | verdict |
|---|---|---|---|
| Duzon | Stage2-Actionable was sufficient; Green waited for revision visibility | strong 90D/180D MFE with tiny MAE | current_profile_correct |
| Hancom | Stage2/Yellow acceptable; Green should stay strict unless paid conversion explicit | strong MFE but high volatility and later drawdown | current_profile_correct |
| AhnLab | generic security/relative-strength reading could be too slow to mark 4B event premium | immediate blowoff then -66.5% 180D MAE | current_profile_4B_too_late |
| ESTsoft | AI/SaaS feature language could be over-promoted if relative strength dominates | +94.15% MFE but -56.26% 180D MAE | current_profile_false_positive |

Stress-test answers:

```text
stage2_actionable_evidence_bonus: kept, but C28 needs contract/retention evidence quality.
yellow_threshold_75: kept, but AI/SaaS wrappers without paid conversion should be capped.
green_threshold_87: strengthened within C28; Green needs ARR/renewal/enterprise deployment or revision.
stage3_green_revision_min_55: strengthened within C28; feature hype cannot replace financial visibility.
price_only_blowoff_guard: strengthened.
full_4b_non_price_requirement: strengthened; event/control premium is non-price 4B evidence.
hard_4c_routing: kept; no hard 4C row is trained here.
```

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2 entry | Green/candidate entry | peak after Stage2 | green_lateness_ratio | verdict |
|---|---:|---:|---:|---:|---|
| Duzon | 29,100 | 53,300 | 78,300 | 0.492 | Green is somewhat late, but not peak-late; Stage2 did the early work |
| Hancom | 15,250 | 24,750 | 38,450 | 0.409 | Green/candidate is late enough that Yellow/Stage2 matters |
| AhnLab | 175,800 | null | 218,500 | not_applicable | no valid Green; event premium |
| ESTsoft | 25,650 | null | 49,800 | not_applicable | no valid Green; price-only AI hype |

## 15. 4B Local vs Full-window Timing Audit

| case | Stage2/actionable price | 4B overlay price | local peak | full-window peak | four_b_local_peak_proximity | four_b_full_window_peak_proximity | verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| AhnLab | 175,800 | 175,800 | 218,500 | 218,500 | 0.000 | 0.000 | 4B should be recognized by event/control premium and overheat, not after price collapse |
| ESTsoft | 25,650 | 25,650 | 49,800 | 49,800 | 0.000 | 0.000 | AI feature hype should start as watch/blocked; local peak comes quickly |
| Duzon | 29,100 | null | 78,300 | 78,300 | null | null | no entry-stage 4B |
| Hancom | 15,250 | null | 38,450 | 38,450 | null | null | volatility watch only |

Interpretation: proximity is intentionally 0.000 for blocked entry rows because the overlay should not wait for a price-local peak. The non-price 4B evidence is the trigger family itself: event/control premium or feature-hype-without-retention.

## 16. 4C Protection Audit

No hard 4C thesis-break row is trained quantitatively. Labels:

```text
AhnLab = thesis_break_watch_only; the C28 thesis was never valid, so this is not a 4C from a valid Stage3.
ESTsoft = thesis_break_watch_only; product hype did not convert into contract-retention evidence.
Duzon/Hancom = no_4c_in_this_window.
```

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
reason = sample is concentrated inside C28; not enough distinct L8 archetypes to propose an L8-wide sector rule.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
```

Proposed C28 shadow rule:

```text
C28_positive_promotion_requires:
  one_or_more_of:
    - paid enterprise software contract / renewal evidence
    - ARR, subscription, or seat/user expansion visibility
    - managed security/service retention visibility
    - confirmed margin bridge from cloud/software monetization
    - customer-quality evidence beyond a product/demo headline

C28_green_cap:
  if AI/SaaS/security headline exists but paid conversion/retention evidence is missing:
      cap at Stage2-watch or Stage3-Yellow-risk
      block Stage3-Green
      do_not_train_positive_weight = true

C28_4B_overlay:
  if event/control/political premium or price-only AI feature hype dominates:
      attach 4B overlay
      do_not_treat_as_full_positive_stage = true
```

## 19. Before / After Backtest Comparison

| profile_id | scope/hypothesis | changed_axes | eligible_trigger_count | selected_entries | avg_MFE90 | avg_MAE90 | avg_MFE180 | avg_MAE180 | false_positive_rate | missed_structural_count | late_green_count | avg_green_lateness | avg_4B_local | avg_4B_full | alignment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0 | e2r_2_1_stock_web_calibrated_proxy | global calibrated proxy; no C28-specific ARR/retention guard | none | 4 | Duzon Jan04; Hancom Nov24; AhnLab Mar23; ESTsoft Jan08 | 97.03 | -19.92 | 109.91 | -33.43 | 50% if AI/security wrappers are over-promoted | 1 | 1 | 0.451 | 0.0 | 0.0 | mixed: positives strong, counterexample blowoff severe |
| P0b | e2r_2_0_baseline_reference | older baseline without Stock-Web stage2/4B fixes | higher Green looseness | 4 | same selected entries | null | null | null | null | higher | 2 | 2 | null | null | null | weaker than P0; kept only as rollback reference |
| P1 | L8_sector_shadow_profile | L8 software/security needs paid conversion or contract quality for positive promotion | retention bonus + guard | 4 | same selected entries | 96.03 | -19.73 | 109.91 | -33.43 | 25% | 0 | 1 | 0.451 | 0.0 | 0.0 | better sector alignment, still broad |
| P2 | C28_archetype_shadow_profile | C28-specific ARR/retention gate, event-premium 4B overlay | c28_retention_arr_visibility_bonus + c28_no_paid_conversion_green_cap | 4 | Duzon/Hancom positive; AhnLab/ESTsoft blocked | 134.83 | -5.48 | 160.6 | -5.48 | 0% on representative promoted positives | 0 | 1 | 0.451 | 0.0 | 0.0 | best alignment for this loop |
| P3 | C28_counterexample_guard_profile | Blocks AI/SW/security wrapper if no retention/ARR/enterprise renewal evidence | harder guard | 4 | only Duzon/Hancom can train positive | 134.83 | -5.48 | 160.6 | -5.48 | 0% | 0 | 1 | 0.451 | 0.0 | 0.0 | safer but may miss early product-led rerating |

## 20. Score-Return Alignment Matrix

| case_id | symbol | score_before | stage_before | score_after | stage_after | changed_components | alignment |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C28_DUZON_2024_AI_ERP_RETENTION_POS | 012510 | 84.0 | Stage3-Yellow | 88.5 | Stage3-Green-shadow | contract_score,customer_quality_score,backlog_visibility_score | strong_positive_alignment |
| C28_HANCOM_2023_AI_DOCS_OFFICE_POS | 030520 | 77.0 | Stage3-Yellow | 81.0 | Stage3-Yellow-shadow | contract_score,backlog_visibility_score | positive_but_high_volatility |
| C28_AHNLAB_2022_SECURITY_EVENT_PREMIUM_COUNTER | 053800 | 74.0 | Stage2/Yellow-risk | 56.0 | Stage4B-overlay/no-positive-promotion | relative_strength_score,execution_risk_score | counterexample_high_drawdown_after_event_premium |
| C28_ESTSOFT_2024_AI_HUMAN_HYPE_COUNTER | 047560 | 76.0 | Stage3-Yellow-risk | 58.0 | Stage2-blocked/4B-watch | relative_strength_score,execution_risk_score | counterexample_price_spike_not_retention |

Mechanism summary:

```text
Duzon/Hancom:
  evidence -> paid enterprise/product route -> revision/financial visibility -> durable rerating

AhnLab/ESTsoft:
  headline/event/relative strength -> no retention or ARR proof -> blowoff or violent drawdown -> guard/4B overlay
```

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L8_PLATFORM_CONTENT_SW_SECURITY | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | ENTERPRISE_SOFTWARE_AI_CLOUD_CONTRACT_RETENTION | 2 | 2 | 2 | 0 | 4 | 0 | 6 | 4 | 2 | false | true | C28 now has balanced positive/counterexample seed set; still needs more pure security-contract positives |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 4
new_trigger_family_count: 4

tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence

residual_error_types_found:
  - AI/SaaS headline without paid conversion can create false Yellow/Green pressure.
  - Security-company wrapper can hide event/control premium rather than contract retention.
  - Stage2 remains useful for C28 positives, but Green needs stricter C28-specific retention evidence.

new_axis_proposed:
  - c28_retention_arr_visibility_bonus
  - c28_ai_feature_without_paid_conversion_green_cap
  - c28_event_or_control_premium_4b_overlay

existing_axis_strengthened:
  - stage3_green_revision_min within C28
  - price_only_blowoff_blocks_positive_stage within C28
  - full_4b_requires_non_price_evidence within C28

existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - yellow_threshold_75
  - hard_4c_thesis_break_routes_to_4c

sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null

loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Stock-Web manifest/schema/profile access.
- Actual 1D OHLCV rows from Songdaiki/stock-web tradable shards.
- Entry_date / entry_price separation.
- MFE/MAE 30D/90D/180D for representative rows.
- Positive/counterexample balance.
- C28-specific residual rule proposal.
```

Not validated in this MD:

```text
- No live scan.
- No current candidate discovery.
- No broker/API/trading logic.
- No stock_agent src/e2r code reading or patch.
- No production scoring change.
- 1Y/2Y metrics are not used for weight calibration in this loop and are left null in machine rows.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c28_retention_arr_visibility_bonus,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,0,2.5,+2.5,Positive cases with explicit enterprise software monetization/retention visibility had 90D/180D MFE above 100% with controlled MAE.,Improves Duzon/Hancom promotion without touching global Green thresholds.,"R8L12_C28_DUZON_STAGE2_20240104|R8L12_C28_HANCOM_STAGE2_20231124",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c28_ai_feature_without_paid_conversion_green_cap,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,False,True,guard,AI/SaaS product news without ARR/renewal/enterprise seat evidence produced ESTsoft-style spike and drawdown.,Reduces false positive Green/yellow risk in AI software hype.,R8L12_C28_ESTSOFT_AI_HYPE_20240108,4,4,2,medium,counterexample_guard,"not production; cap positive Green only"
shadow_weight,c28_event_or_control_premium_4b_overlay,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,False,True,guard,"AhnLab shows security wrapper can become control/event premium; 4B overlay should override positive contract-retention interpretation.","Improves 4B timing; no positive entry weight.",R8L12_C28_AHNLAB_EVENT_PREMIUM_20220323,4,4,2,medium,4B_overlay,"not production; risk overlay only"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","source_repo_url":"https://github.com/FinanceData/marcap","min_date":"1995-05-02","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"inactive_or_delisted_like_symbol_count":2546,"markets":["KONEX","KOSDAQ","KOSDAQ GLOBAL","KOSPI"],"price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C28_DUZON_2024_AI_ERP_RETENTION_POS","symbol":"012510","company_name":"더존비즈온","round":"R8","loop":"12","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"ENTERPRISE_AI_ERP_SAAS_RETENTION","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R8L12_C28_DUZON_STAGE2_20240104","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"strong_positive_alignment","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Stage2 captured enterprise AI/ERP rerating before Green confirmation; clean 180D window."}
{"row_type":"case","case_id":"C28_HANCOM_2023_AI_DOCS_OFFICE_POS","symbol":"030520","company_name":"한글과컴퓨터","round":"R8","loop":"12","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"AI_OFFICE_CLOUD_DOCUMENT_SUBSCRIPTION","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R8L12_C28_HANCOM_STAGE2_20231124","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_but_high_volatility","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Positive C28 sample but requires contract/paid conversion guard before Green."}
{"row_type":"case","case_id":"C28_AHNLAB_2022_SECURITY_EVENT_PREMIUM_COUNTER","symbol":"053800","company_name":"안랩","round":"R8","loop":"12","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SECURITY_VENDOR_EVENT_PREMIUM_COUNTEREXAMPLE","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R8L12_C28_AHNLAB_EVENT_PREMIUM_20220323","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_high_drawdown_after_event_premium","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"Security label alone did not equal contract retention; event/control premium should be 4B overlay."}
{"row_type":"case","case_id":"C28_ESTSOFT_2024_AI_HUMAN_HYPE_COUNTER","symbol":"047560","company_name":"이스트소프트","round":"R8","loop":"12","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"AI_HUMAN_SAAS_WITHOUT_RETENTION_COUNTEREXAMPLE","case_type":"price_moved_without_evidence","positive_or_counterexample":"counterexample","best_trigger":"R8L12_C28_ESTSOFT_AI_HYPE_20240108","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_price_spike_not_retention","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Large MFE but even larger thesis-quality problem; should not train positive Green without paid retention evidence."}
{"row_type":"trigger","trigger_id":"R8L12_C28_DUZON_STAGE2_20240104","case_id":"C28_DUZON_2024_AI_ERP_RETENTION_POS","symbol":"012510","company_name":"더존비즈온","round":"R8","loop":"12","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"ENTERPRISE_SOFTWARE_AI_CLOUD_CONTRACT_RETENTION","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"software_security_contract_retention","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-04","evidence_available_at_that_date":"Enterprise ERP/SaaS AI monetization route became investable before full revision confirmation; price row confirms a low-risk Stage2 entry on 2024-01-04 close.","evidence_source":"public historical company/news/filing classification; OHLC verified in stock-web 2024 shard","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","early_revision_signal","customer_or_order_quality"],"stage3_evidence_fields":["financial_visibility","confirmed_revision","margin_bridge"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012510/2024.csv","profile_path":"atlas/symbol_profiles/012/012510.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-04","entry_price":29100,"MFE_30D_pct":81.44,"MFE_90D_pct":117.53,"MFE_180D_pct":169.07,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-0.86,"MAE_90D_pct":-0.86,"MAE_180D_pct":-0.86,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-08","peak_price":78300,"drawdown_after_peak_pct":-42.66,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C28_DUZON_2024_AI_ERP_RETENTION_POS_2024-01-04","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R8L12_C28_DUZON_GREEN_20240404","case_id":"C28_DUZON_2024_AI_ERP_RETENTION_POS","symbol":"012510","company_name":"더존비즈온","round":"R8","loop":"12","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"ENTERPRISE_SOFTWARE_AI_CLOUD_CONTRACT_RETENTION","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"software_security_contract_retention","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage3-Green","trigger_date":"2024-04-04","evidence_available_at_that_date":"AI ERP/enterprise software story had stronger price confirmation and higher revision visibility; this is a label-comparison row, not aggregate entry.","evidence_source":"stock-web row 2024-04-04 close; proxy evidence family classification","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","margin_bridge","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012510/2024.csv","profile_path":"atlas/symbol_profiles/012/012510.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-04","entry_price":53300,"MFE_30D_pct":46.9,"MFE_90D_pct":46.9,"MFE_180D_pct":46.9,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-9.57,"MAE_90D_pct":-15.76,"MAE_180D_pct":-15.76,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-08","peak_price":78300,"drawdown_after_peak_pct":-42.66,"green_lateness_ratio":0.492,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"late_green_but_still_usable","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C28_DUZON_2024_AI_ERP_RETENTION_POS_20240104","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R8L12_C28_HANCOM_STAGE2_20231124","case_id":"C28_HANCOM_2023_AI_DOCS_OFFICE_POS","symbol":"030520","company_name":"한글과컴퓨터","round":"R8","loop":"12","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"ENTERPRISE_SOFTWARE_AI_CLOUD_CONTRACT_RETENTION","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"software_security_contract_retention","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2023-11-24","evidence_available_at_that_date":"Office/document software AI and cloud subscription option was visible before the January rerating; evidence was sufficient for Stage2/Yellow, not automatic Green.","evidence_source":"public historical company/news/filing classification; OHLC verified in 2023/2024 stock-web shards","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","early_revision_signal","relative_strength"],"stage3_evidence_fields":["financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/030/030520/2023.csv","profile_path":"atlas/symbol_profiles/030/030520.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-11-24","entry_price":15250,"MFE_30D_pct":49.18,"MFE_90D_pct":152.13,"MFE_180D_pct":152.13,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-10.1,"MAE_90D_pct":-10.1,"MAE_180D_pct":-10.1,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-22","peak_price":38450,"drawdown_after_peak_pct":-60.73,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"structural_success_high_beta","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C28_HANCOM_2023_AI_DOCS_OFFICE_POS_2023-11-24","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R8L12_C28_HANCOM_GREEN_20240110","case_id":"C28_HANCOM_2023_AI_DOCS_OFFICE_POS","symbol":"030520","company_name":"한글과컴퓨터","round":"R8","loop":"12","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"ENTERPRISE_SOFTWARE_AI_CLOUD_CONTRACT_RETENTION","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"software_security_contract_retention","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage3-Green-candidate","trigger_date":"2024-01-10","evidence_available_at_that_date":"Explosive AI-office price reaction could be labelled Green only if paid conversion/retention evidence is present; here it remains comparison-only.","evidence_source":"stock-web row 2024-01-10 close; proxy evidence family classification","stage2_evidence_fields":["relative_strength","public_event_or_disclosure"],"stage3_evidence_fields":["multiple_public_sources","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/030/030520/2024.csv","profile_path":"atlas/symbol_profiles/030/030520.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-10","entry_price":24750,"MFE_30D_pct":55.35,"MFE_90D_pct":55.35,"MFE_180D_pct":55.35,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-17.58,"MAE_90D_pct":-20.28,"MAE_180D_pct":-38.99,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-22","peak_price":38450,"drawdown_after_peak_pct":-60.73,"green_lateness_ratio":0.409,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"green_candidate_late_and_high_volatility","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C28_HANCOM_2023_AI_DOCS_OFFICE_POS_20231124","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R8L12_C28_AHNLAB_EVENT_PREMIUM_20220323","case_id":"C28_AHNLAB_2022_SECURITY_EVENT_PREMIUM_COUNTER","symbol":"053800","company_name":"안랩","round":"R8","loop":"12","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"ENTERPRISE_SOFTWARE_AI_CLOUD_CONTRACT_RETENTION","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"software_security_contract_retention","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage2-blocked/4B-overlay","trigger_date":"2022-03-23","evidence_available_at_that_date":"Security-company wrapper existed, but the trigger family was event/control/political premium rather than contract retention, ARR, seat expansion, or confirmed margin bridge.","evidence_source":"public historical event classification; OHLC verified in stock-web 2022 shard","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","control_premium_or_event_premium","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/053/053800/2022.csv","profile_path":"atlas/symbol_profiles/053/053800.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-03-23","entry_price":175800,"MFE_30D_pct":24.29,"MFE_90D_pct":24.29,"MFE_180D_pct":24.29,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-46.53,"MAE_90D_pct":-53.92,"MAE_180D_pct":-66.5,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-03-24","peak_price":218500,"drawdown_after_peak_pct":-73.04,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.0,"four_b_full_window_peak_proximity":0.0,"four_b_timing_verdict":"event_premium_4B_should_override_C28_positive_promotion","four_b_evidence_type":["valuation_blowoff","positioning_overheat","control_premium_or_event_premium","price_only"],"four_c_protection_label":null,"trigger_outcome_label":"false_positive_green_or_event_premium_blowoff","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C28_AHNLAB_2022_SECURITY_EVENT_PREMIUM_COUNTER_2022-03-23","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R8L12_C28_ESTSOFT_AI_HYPE_20240108","case_id":"C28_ESTSOFT_2024_AI_HUMAN_HYPE_COUNTER","symbol":"047560","company_name":"이스트소프트","round":"R8","loop":"12","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"ENTERPRISE_SOFTWARE_AI_CLOUD_CONTRACT_RETENTION","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"software_security_contract_retention","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage2-blocked/price-moved-without-retention","trigger_date":"2024-01-05","evidence_available_at_that_date":"AI-human/SaaS language produced a violent move, but the trigger lacked paid enterprise retention, ARR, or repeat contract evidence; 180D drawdown confirms this should train a guard, not a positive Green rule.","evidence_source":"public historical product/news classification; OHLC verified in stock-web 2024 shard","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/047/047560/2024.csv","profile_path":"atlas/symbol_profiles/047/047560.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-08","entry_price":25650,"MFE_30D_pct":94.15,"MFE_90D_pct":94.15,"MFE_180D_pct":94.15,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-13.26,"MAE_90D_pct":-14.81,"MAE_180D_pct":-56.26,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-29","peak_price":49800,"drawdown_after_peak_pct":-77.47,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.0,"four_b_full_window_peak_proximity":0.0,"four_b_timing_verdict":"price_move_without_contract_retention_should_not_promote_green","four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only"],"four_c_protection_label":null,"trigger_outcome_label":"price_moved_without_retention_evidence","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C28_ESTSOFT_2024_AI_HUMAN_HYPE_COUNTER_2024-01-08","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C28_DUZON_2024_AI_ERP_RETENTION_POS","trigger_id":"R8L12_C28_DUZON_STAGE2_20240104","symbol":"012510","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":6,"backlog_visibility_score":5,"margin_bridge_score":5,"revision_score":7,"relative_strength_score":4,"customer_quality_score":6,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":2,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":84.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":8,"backlog_visibility_score":6,"margin_bridge_score":6,"revision_score":7,"relative_strength_score":4,"customer_quality_score":7,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":2,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":88.5,"stage_label_after":"Stage3-Green-shadow","changed_components":["contract_score","customer_quality_score","backlog_visibility_score"],"component_delta_explanation":"C28 paid enterprise contract/retention evidence receives shadow bonus; not global.","MFE_90D_pct":117.53,"MAE_90D_pct":-0.86,"score_return_alignment_label":"strong_positive_alignment","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C28_HANCOM_2023_AI_DOCS_OFFICE_POS","trigger_id":"R8L12_C28_HANCOM_STAGE2_20231124","symbol":"030520","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":4,"margin_bridge_score":4,"revision_score":5,"relative_strength_score":5,"customer_quality_score":5,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":3,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":77.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":5,"margin_bridge_score":4,"revision_score":5,"relative_strength_score":5,"customer_quality_score":5,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":3,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":81.0,"stage_label_after":"Stage3-Yellow-shadow","changed_components":["contract_score","backlog_visibility_score"],"component_delta_explanation":"Positive but no automatic Green until paid conversion/renewal evidence is explicit.","MFE_90D_pct":152.13,"MAE_90D_pct":-10.1,"score_return_alignment_label":"positive_but_high_volatility","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C28_AHNLAB_2022_SECURITY_EVENT_PREMIUM_COUNTER","trigger_id":"R8L12_C28_AHNLAB_EVENT_PREMIUM_20220323","symbol":"053800","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":1,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":9,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":9,"execution_risk_score":8,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":74.0,"stage_label_before":"Stage2/Yellow-risk","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":1,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":5,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":9,"execution_risk_score":9,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":56.0,"stage_label_after":"Stage4B-overlay/no-positive-promotion","changed_components":["relative_strength_score","execution_risk_score"],"component_delta_explanation":"Security wrapper is overridden by event/control premium and lack of contract retention.","MFE_90D_pct":24.29,"MAE_90D_pct":-53.92,"score_return_alignment_label":"counterexample_high_drawdown_after_event_premium","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C28_ESTSOFT_2024_AI_HUMAN_HYPE_COUNTER","trigger_id":"R8L12_C28_ESTSOFT_AI_HYPE_20240108","symbol":"047560","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":9,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":9,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76.0,"stage_label_before":"Stage3-Yellow-risk","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":6,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":9,"execution_risk_score":9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":58.0,"stage_label_after":"Stage2-blocked/4B-watch","changed_components":["relative_strength_score","execution_risk_score"],"component_delta_explanation":"AI/SaaS feature hype cannot substitute for paid enterprise retention or ARR evidence.","MFE_90D_pct":94.15,"MAE_90D_pct":-14.81,"score_return_alignment_label":"counterexample_price_spike_not_retention","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R8","loop":"12","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"new_canonical_archetype_count":1,"new_trigger_family_count":4,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_revision_min","full_4b_requires_non_price_evidence","price_only_blowoff_blocks_positive_stage"],"residual_error_types_found":["AI/SaaS feature hype without paid conversion","security wrapper event/control premium","Green late but acceptable when Stage2 is actionable"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"auto_selected_coverage_gap":"R8_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION"}
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
next_round = R9_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
reason = R8 now has C26/C27/C28 coverage seeds; next auto gap should move to mobility unless user manually requests another C28 pure-security-contract pass.
```

Suggested next C28 holdout, if staying in R8:

```text
- add pure cybersecurity subscription/managed-service positives, not political/event security names
- add one software company with actual ARR/renewal data but weak price response
```

## 28. Source Notes

Stock-Web source notes:

```text
manifest checked: atlas/manifest.json
schema checked: atlas/schema.json
profile checked: 012510 / 030520 / 053800 / 047560
price shard checked:
  - atlas/ohlcv_tradable_by_symbol_year/012/012510/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/030/030520/2023.csv
  - atlas/ohlcv_tradable_by_symbol_year/030/030520/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/053/053800/2022.csv
  - atlas/ohlcv_tradable_by_symbol_year/047/047560/2024.csv
```

Citations captured during research execution:

```text
prompt/source specification: turn296file0
stock-web manifest: turn297file0
stock-web schema: turn298file0
stock_agent ingest summary: turn299file0
stock_agent applied scoring diff: turn300file0
stock-web profiles: turn302file0, turn303file0, turn304file0, turn305file0
stock-web price rows: turn306file0, turn307file0, turn308file0, turn309file0, turn310file0, turn311file0, turn312file0
```
