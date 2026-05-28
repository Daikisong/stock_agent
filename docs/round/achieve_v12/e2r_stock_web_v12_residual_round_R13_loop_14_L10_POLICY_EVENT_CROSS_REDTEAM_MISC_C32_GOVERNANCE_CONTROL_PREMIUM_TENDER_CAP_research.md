# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R13
loop = 14
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id = HOSTILE_TENDER_CONTROL_PREMIUM | COMPETING_TENDER_WAR | PRIVATIZATION_PREFERRED_BIDDER_NO_TENDER_SPREAD | LEGAL_CONTROL_TRANSFER_LOW_LIQUIDITY_NO_TENDER_SPREAD
output_file = e2r_stock_web_v12_residual_round_R13_loop_14_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This file follows the uploaded v12 prompt contract. fileciteturn368file0

## 1. Current Calibrated Profile Assumption

The current profile proxy is `e2r_2_1_stock_web_calibrated_proxy`. Existing global axes are treated as already applied and are not re-proposed as global rules. This loop tests whether C32 needs its own event-premium grammar: a cash tender/competing bidder is not the same thing as a vague sale process, preferred-bidder headline, or legal ownership cleanup.

```text
existing_axis_tested:
- stage2_actionable_evidence_bonus
- stage3_yellow_total_min
- stage3_green_total_min
- stage3_green_revision_min
- stage3_cross_evidence_green_buffer
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence
- hard_4c_thesis_break_routes_to_4c
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
loop_objective = residual_false_positive_mining | residual_missed_structural_mining | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | canonical_archetype_compression | coverage_gap_fill
```

The selection intentionally follows the previous C31 policy-event loop but moves one gear downstream. C31 asks whether a policy or reform agenda exists. C32 asks whether that agenda becomes a priced control-premium mechanism: tender offer, competing bidder, binding sale, control cap, or hard failure.

## 3. Previous Coverage / Duplicate Avoidance Check

GitHub search over the allowed `stock_agent` research artifacts for `C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP`, `010130`, `041510`, `011200`, and `003920` returned no direct matching calibration artifact in this run. No `src/e2r` code was opened, no production scoring was inferred, and no live candidate scan was performed.

```text
auto_selected_coverage_gap = R13/L10/C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
selection_reason = C32 needs positive/control-premium and counterexample/no-tender-spread coverage after C31 policy-event coverage.
new_independent_case_ratio = 4 / 4 = 1.00
```

## 4. Stock-Web OHLC Input / Price Source Validation

The stock-web manifest reports `source_name=FinanceData/marcap`, `price_adjustment_status=raw_unadjusted_marcap`, `min_date=1995-05-02`, `max_date=2026-02-20`, `tradable_row_count=14354401`, and `calibration_shard_root=atlas/ohlcv_tradable_by_symbol_year`. fileciteturn369file0

```text
price_data_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
```

Case-level profile validation:

- `010130` 고려아연: no corporate-action candidate dates in profile; 2024-09 to 2025-06 tradable rows cover the 180D window. fileciteturn370file0 fileciteturn371file0 fileciteturn372file0
- `041510` 에스엠: old corporate-action candidates are in 2002/2005 only; 2023 tender-war window is clean. fileciteturn373file0 fileciteturn374file0 fileciteturn375file0
- `011200` HMM: profile has a 2023-11-10 corporate-action candidate before the selected 2023-12-19 entry; the tested forward 180D window is marked clean after that candidate. fileciteturn376file0 fileciteturn377file0 fileciteturn378file0 fileciteturn379file0
- `003920` 남양유업: profile has a 2024-11-20 corporate-action candidate outside the 180D window from 2024-01-04; 1Y/2Y are not used. fileciteturn380file0 fileciteturn381file0

## 5. Historical Eligibility Gate

All representative triggers are historical and have at least 180 post-entry trading days within stock-web's manifest max date. All quantitative calibration uses tradable shards only.

```text
calibration_usable_case_count = 4
calibration_usable_trigger_count = 7
representative_trigger_count = 4
blocked_for_weight_calibration = 0
```

## 6. Canonical Archetype Compression Map

```text
HOSTILE_TENDER_CONTROL_PREMIUM -> C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
COMPETING_TENDER_WAR -> C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
PRIVATIZATION_PREFERRED_BIDDER_NO_TENDER_SPREAD -> C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
LEGAL_CONTROL_TRANSFER_LOW_LIQUIDITY_NO_TENDER_SPREAD -> C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
```

Compression rule: C32 should not ask only "is there a governance/control story?" It should ask "is there a priced mechanism that can force marginal buyers to reprice the stock?" That mechanism is strong for cash tender or competing tender cases; it is weak for non-binding preferred-bidder or legal-finality-only stories.

## 7. Case Selection Summary

| case_id | symbol | company | role | best trigger | alignment |
|---|---:|---|---|---|---|
| C32-KZ-20240913-MBK-YP-TENDER | 010130 | 고려아연 | positive | TRG-C32-KZ-20240913-STAGE2A | confirmed hostile tender/control premium produced very large MFE with shallow initial MAE; generic revision/margin model would under-rank it |
| C32-SM-20230210-HYBE-KAKAO-TENDER-WAR | 041510 | 에스엠 | positive | TRG-C32-SM-20230210-STAGE2A | control battle/tender-war evidence captured the event premium before operating revision evidence existed |
| C32-HMM-20231219-HARIM-PREFERRED-BIDDER | 011200 | HMM | counterexample | TRG-C32-HMM-20231219-STAGE2A | preferred-bidder news spiked first but failed to create durable control premium; 90D/180D MAE dominated after deal failure |
| C32-NAMYANG-20240104-LEGAL-CONTROL-FINALITY | 003920 | 남양유업 | counterexample | TRG-C32-NAMYANG-20240104-STAGE2A | legal-finality control transfer did not become a tradable tender premium; low liquidity/no spread produced poor score-return alignment |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 2
4C_case_count = 1
new_independent_case_count = 4
new_symbol_count = 4
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
```

The positive cases are explicit priced control-premium events. The counterexamples are governance/control stories where price moved, but evidence did not close into a binding tender spread.

## 9. Evidence Source Map

| case_id | evidence family | source quality | source note |
|---|---|---|---|
| C32-KZ-20240913-MBK-YP-TENDER | hostile tender / buyback / regulatory fight | medium | Public Reuters-style event coverage used; implementation should archive exact URL and DART/KRX filings. |
| C32-SM-20230210-HYBE-KAKAO-TENDER-WAR | competing tender war | medium | Public AP-style tender coverage used; implementation should archive exact tender filings. |
| C32-HMM-20231219-HARIM-PREFERRED-BIDDER | preferred-bidder sale process, later failed | medium-low | Secondary event summary used; implementation must corroborate with KDB/KEXIM/KRX/DART. |
| C32-NAMYANG-20240104-LEGAL-CONTROL-FINALITY | legal finality / control transfer | medium-low | Secondary company/court-event summary used; implementation must corroborate with DART/court filings. |

## 10. Price Data Source Map

| symbol | profile_path | representative price shard | corporate-action window status |
|---:|---|---|---|
| 010130 | atlas/symbol_profiles/010/010130.json | atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv + 2025.csv | clean_180D_window |
| 041510 | atlas/symbol_profiles/041/041510.json | atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv | clean_180D_window |
| 011200 | atlas/symbol_profiles/011/011200.json | atlas/ohlcv_tradable_by_symbol_year/011/011200/2023.csv + 2024.csv | clean_180D_window_after_2023_11_10_candidate |
| 003920 | atlas/symbol_profiles/003/003920.json | atlas/ohlcv_tradable_by_symbol_year/003/003920/2024.csv | clean_180D_window; later 2024-11-20 candidate outside 180D |

## 11. Case-by-Case Trigger Grid

| trigger_id | role | symbol | trigger_date | entry_date | entry_price | MFE90 | MAE90 | MFE180 | MAE180 | peak | current verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| TRG-C32-KZ-20240913-STAGE2A | representative | 010130 | 2024-09-13 | 2024-09-13 | 666000 | 261.41 | -1.65 | 261.41 | -3.45 | 2024-12-06 / 2407000 | current_profile_missed_structural |
| TRG-C32-KZ-20241031-4B-WATCH | 4B_overlay_only | 010130 | 2024-10-31 | 2024-10-31 | 998000 | 141.18 | -35.57 | 141.18 | -35.57 | 2024-12-06 / 2407000 | current_profile_4B_too_early |
| TRG-C32-SM-20230210-STAGE2A | representative | 041510 | 2023-02-10 | 2023-02-10 | 114700 | 40.54 | -23.63 | 40.54 | -23.63 | 2023-03-08 / 161200 | current_profile_missed_structural |
| TRG-C32-SM-20230308-4B-CAP | 4B_overlay_only | 041510 | 2023-03-08 | 2023-03-08 | 158500 | 1.7 | -44.73 | 1.7 | -44.73 | 2023-03-08 / 161200 | current_profile_correct |
| TRG-C32-HMM-20231219-STAGE2A | representative | 011200 | 2023-12-19 | 2023-12-19 | 18430 | 26.42 | -22.68 | 26.42 | -22.68 | 2023-12-20 / 23300 | current_profile_false_positive |
| TRG-C32-HMM-20240208-4C | 4C_overlay_only | 011200 | 2024-02-08 | 2024-02-08 | 18380 | 7.29 | -22.47 | 13.17 | -22.47 | 2024-07-03 / 20800 | current_profile_4C_too_late |
| TRG-C32-NAMYANG-20240104-STAGE2A | representative | 003920 | 2024-01-04 | 2024-01-04 | 590000 | 9.32 | -20.68 | 9.32 | -20.68 | 2024-01-05 / 645000 | current_profile_false_positive |

## 12. Trigger-Level OHLC Backtest Tables

Representative aggregate results:

| case_id | entry | entry price | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | interpretation |
|---|---:|---:|---:|---:|---:|---|
| C32-KZ-20240913-MBK-YP-TENDER | 2024-09-13 | 666000 | +131.68 / -1.65 | +261.41 / -1.65 | +261.41 / -3.45 | direct tender/control premium; large event-spread success |
| C32-SM-20230210-HYBE-KAKAO-TENDER-WAR | 2023-02-10 | 114700 | +40.54 / -6.45 | +40.54 / -23.63 | +40.54 / -23.63 | tender-war success but 4B cap needed |
| C32-HMM-20231219-HARIM-PREFERRED-BIDDER | 2023-12-19 | 18430 | +26.42 / -2.33 | +26.42 / -22.68 | +26.42 / -22.68 | headline spike, failed durable rerating |
| C32-NAMYANG-20240104-LEGAL-CONTROL-FINALITY | 2024-01-04 | 590000 | +9.32 / -9.49 | +9.32 / -20.68 | +9.32 / -20.68 | legal finality without tender spread; false positive guard |

## 13. Current Calibrated Profile Stress Test

1. Current calibrated profile would likely under-promote KZ/SM because the main evidence is not EPS/revision/margin; it is priced governance-control premium.
2. Current calibrated profile would likely over-promote HMM/Namyang if all governance/control headlines receive the same Stage2 event bonus.
3. Stage2 bonus is directionally useful but too blunt inside C32.
4. Yellow/Green thresholds are less relevant than event mechanism quality: cash tender spread versus non-binding story.
5. Green revision minimum is not a suitable hard gate for C32 positives, but its absence should be offset only by explicit cash tender/competing bidder evidence.
6. Price-only blowoff guard is strengthened, especially for SM post-Kakao-cap and Korea Zinc post-squeeze.
7. Full 4B non-price requirement is kept, but Korea Zinc shows non-price 4B evidence can be too early for full-window exit.
8. Hard 4C routing is strengthened for HMM once deal failure breaks the thesis.

```text
current_profile_error_count = 4
residual_error_types_found =
- current_profile_missed_structural for explicit cash tender / competing tender
- current_profile_false_positive for preferred-bidder / legal-finality no-spread rows
- current_profile_4B_too_early for Korea Zinc regulatory/dilution watch
- current_profile_4C_too_late for HMM if sale failure is not routed hard
```

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green revision trigger was used because C32 event-premium cases are not primarily operating-revision cases. Therefore:

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

Research implication: C32 needs a parallel event-confirmation route, not a blanket waiver. The route requires a priced tender/competing bidder/control premium cap. It does not apply to preferred-bidder or legal-finality-only cases.

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | entry | local proximity | full-window proximity | verdict |
|---|---:|---:|---:|---|
| TRG-C32-KZ-20241031-4B-WATCH | 998000 | 0.379 | 0.191 | non-price 4B watch was real but too early for full-window exit |
| TRG-C32-SM-20230308-4B-CAP | 158500 | 0.942 | 0.942 | good full-window 4B timing because announced tender cap matched observed price cap |

C32 therefore needs two 4B lanes: `event_cap_full_4B` and `regulatory_dilution_watch_4B`. They are siblings, not the same signal.

## 16. 4C Protection Audit

HMM's 2024-02-08 sale-failure row is the cleanest 4C row. After the thesis break, 90D MAE from the 4C entry was materially lower than holding from the prior event spike, but still negative. Approximate protection label:

```text
four_c_protection_label = hard_4c_success
protection_interpretation = avoids part of post-peak drawdown, but not a fresh positive entry
```

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
reason = the sample is all L10, but the mechanism is narrower than the whole policy/event sector.
```

A sector-wide L10 rule would be too coarse. Disaster events, subsidy laws, geopolitical restrictions, governance fights, and tender offers are different machines. This loop supports a canonical-archetype rule, not a sector rule.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
```

Candidate rule:

```text
if C32 event has explicit cash tender spread OR competing bidder OR binding control-premium price:
    allow event-premium Stage2-Actionable / Stage3-Green-Event route even without operating revision,
    but require 4B event-cap audit once price approaches announced tender cap.

if C32 event is only preferred bidder, privatization rumor, legal-finality owner cleanup, or governance narrative without tender spread:
    block Green promotion;
    require watch-only or guarded Stage2 until binding tender/closing economics appears.

if 4B evidence is non-price but full-window proximity is low:
    classify as 4B-Watch, not full 4B exit.
```

## 19. Before / After Backtest Comparison

| profile_id | scope | selected entries | avg MFE90 | avg MAE90 | false-positive effect | verdict |
|---|---|---|---:|---:|---|---|
| P0 | current_default_proxy | all representative triggers | 84.42 | -17.16 | 50% if preferred-bidder/legal-finality rows are promoted | mixed; misses explicit tender positives and over-trusts weak control-transfer rows |
| P0b | rollback_reference | all representative triggers | 84.42 | -17.16 | 50%+ | worse false-positive discipline |
| P1 | sector_specific_candidate | KZ/SM promoted; HMM/Namyang watched | 150.98 | -12.64 | 0% among promoted | better, but too broad if applied to all L10 events |
| P2 | canonical_archetype_candidate | KZ/SM promoted; HMM/Namyang guarded | 150.98 | -12.64 | 0% among promoted | best explanatory alignment |
| P3 | counterexample_guard_profile | HMM/Namyang removed; KZ/SM still require manual event override | 150.98 | -12.64 | 0% after guard | safe but still misses C32 positives |

## 20. Score-Return Alignment Matrix

| case | P0 verdict | P2 C32 shadow verdict | observed path | alignment |
|---|---|---|---|---|
| 고려아연 | missed structural | promote event-premium | +261.41% 90D MFE, -1.65% 90D MAE | improved |
| 에스엠 | missed structural | promote then 4B cap | +40.54% 90D MFE, -23.63% 90D MAE | improved if 4B used |
| HMM | false positive risk | guard no tender spread | +26.42% spike but -22.68% 90D MAE | improved |
| 남양유업 | false positive risk | guard no tender spread | +9.32% MFE, -20.68% MAE | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | positive | counterexample | 4B | 4C | new independent | usable triggers | profile errors | canonical rule |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 2 | 2 | 2 | 1 | 4 | 7 | 4 | True |

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
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - missed_structural_control_premium
  - preferred_bidder_false_positive
  - legal_control_finality_false_positive
  - 4B_non_price_watch_too_early_for_full_window_peak
new_axis_proposed:
  - c32_confirmed_cash_tender_or_competing_bidder_bonus
  - c32_no_binding_tender_spread_guard
  - c32_event_cap_4b_overlay
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C32
  - hard_4c_thesis_break_routes_to_4c within C32
existing_axis_weakened: null
existing_axis_kept:
  - full_4b_requires_non_price_evidence, with 4B-Watch vs full 4B split
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest metadata
- symbol profile availability and corporate-action candidate windows
- representative entry date and entry price from tradable shards
- 30D / 90D / 180D MFE and MAE estimates
- peak date / peak price / drawdown-after-peak estimates
- positive vs counterexample balance
- C32-specific residual rule logic
```

Not validated in this run:

```text
- exact official filing text for each event
- DART/KRX primary disclosure timestamps
- intraday publication timing
- 1Y / 2Y quantitative fields
- production scoring code
- live candidate applicability
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c32_confirmed_cash_tender_or_competing_bidder_bonus,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"cash tender / competing bidder should override missing operating revision when price spread is explicit","promotes KZ/SM while preserving 4B caps","TRG-C32-KZ-20240913-STAGE2A|TRG-C32-SM-20230210-STAGE2A",4,4,2,medium,canonical_shadow_only,"not production; event-premium path"
shadow_weight,c32_no_binding_tender_spread_guard,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"preferred bidder or legal finality without cash tender spread behaved like false positive","guards HMM/Namyang","TRG-C32-HMM-20231219-STAGE2A|TRG-C32-NAMYANG-20240104-STAGE2A",4,4,2,medium,canonical_shadow_only,"not production; guard false control premium"
shadow_weight,c32_event_cap_4b_overlay,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"announced tender price cap/competing offer ceiling can be full-window 4B; non-price regulatory warning can be watch-only if full-window proximity is low","separates SM good 4B from Korea Zinc early watch","TRG-C32-SM-20230308-4B-CAP|TRG-C32-KZ-20241031-4B-WATCH",7,4,2,low,canonical_shadow_only,"4B overlay only; not entry promotion"

```

## 25. Machine-Readable Rows

### 25.1 JSONL rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C32-KZ-20240913-MBK-YP-TENDER","symbol":"010130","company_name":"고려아연","round":"R13","loop":"14","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"HOSTILE_TENDER_CONTROL_PREMIUM","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TRG-C32-KZ-20240913-STAGE2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"confirmed hostile tender/control premium produced very large MFE with shallow initial MAE; generic revision/margin model would under-rank it","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"Direct tender price plus hostile-control path; later 4B/4C risk is overlay, not entry invalidation."}
{"row_type":"case","case_id":"C32-SM-20230210-HYBE-KAKAO-TENDER-WAR","symbol":"041510","company_name":"에스엠","round":"R13","loop":"14","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"COMPETING_TENDER_WAR","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TRG-C32-SM-20230210-STAGE2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"control battle/tender-war evidence captured the event premium before operating revision evidence existed","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"Kakao tender cap later became a clean 4B event-cap overlay."}
{"row_type":"case","case_id":"C32-HMM-20231219-HARIM-PREFERRED-BIDDER","symbol":"011200","company_name":"HMM","round":"R13","loop":"14","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"PRIVATIZATION_PREFERRED_BIDDER_NO_TENDER_SPREAD","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TRG-C32-HMM-20231219-STAGE2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"preferred-bidder news spiked first but failed to create durable control premium; 90D/180D MAE dominated after deal failure","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Sale optionality without binding cash tender spread should be guarded."}
{"row_type":"case","case_id":"C32-NAMYANG-20240104-LEGAL-CONTROL-FINALITY","symbol":"003920","company_name":"남양유업","round":"R13","loop":"14","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"LEGAL_CONTROL_TRANSFER_LOW_LIQUIDITY_NO_TENDER_SPREAD","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TRG-C32-NAMYANG-20240104-STAGE2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"legal-finality control transfer did not become a tradable tender premium; low liquidity/no spread produced poor score-return alignment","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Keep as residual counterexample with evidence-source caveat; price window itself is clean through 180D."}
{"row_type":"trigger","trigger_id":"TRG-C32-KZ-20240913-STAGE2A","case_id":"C32-KZ-20240913-MBK-YP-TENDER","symbol":"010130","company_name":"고려아연","round":"R13","loop":"14","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"HOSTILE_TENDER_CONTROL_PREMIUM","sector":"materials/governance-event","primary_archetype":"hostile tender offer / control premium","loop_objective":"sector_specific_rule_discovery|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-09-13","evidence_available_at_that_date":"MBK Partners and Young Poong launched a priced tender offer for Korea Zinc, creating direct hostile-control premium evidence.","evidence_source":"Reuters/AP-style public event source; later implementation should retain URL in calibration ledger.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":["multiple_public_sources","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv","profile_path":"atlas/symbol_profiles/010/010130.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-09-13","entry_price":666000,"MFE_30D_pct":131.68,"MFE_90D_pct":261.41,"MFE_180D_pct":261.41,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-1.65,"MAE_90D_pct":-1.65,"MAE_180D_pct":-3.45,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-12-06","peak_price":2407000,"drawdown_after_peak_pct":-73.29,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"structural_success_control_premium","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C32-KZ-20240913-666000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG-C32-KZ-20241031-4B-WATCH","case_id":"C32-KZ-20240913-MBK-YP-TENDER","symbol":"010130","company_name":"고려아연","round":"R13","loop":"14","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"HOSTILE_TENDER_CONTROL_PREMIUM","sector":"materials/governance-event","primary_archetype":"hostile tender offer / control premium","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B-Watch","trigger_date":"2024-10-31","evidence_available_at_that_date":"Share-issuance/regulatory controversy added real non-price risk, but full observed-cycle peak had not yet occurred.","evidence_source":"Reuters/regulatory coverage; verify exact filing/court timeline before implementation.","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["legal_or_regulatory_block","dilution_or_cb","capital_raise_or_overhang"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv","profile_path":"atlas/symbol_profiles/010/010130.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-10-31","entry_price":998000,"MFE_30D_pct":141.18,"MFE_90D_pct":141.18,"MFE_180D_pct":141.18,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-10.02,"MAE_90D_pct":-35.57,"MAE_180D_pct":-35.57,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-12-06","peak_price":2407000,"drawdown_after_peak_pct":-73.29,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.379,"four_b_full_window_peak_proximity":0.191,"four_b_timing_verdict":"non_price_4B_watch_too_early_for_full_window_peak","four_b_evidence_type":["legal_or_regulatory_block","dilution_or_cb","capital_raise_or_overhang"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_watch_not_full_exit","current_profile_verdict":"current_profile_4B_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C32-KZ-20241031-998000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same_symbol_new_4B_timing_path","independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG-C32-SM-20230210-STAGE2A","case_id":"C32-SM-20230210-HYBE-KAKAO-TENDER-WAR","symbol":"041510","company_name":"에스엠","round":"R13","loop":"14","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"COMPETING_TENDER_WAR","sector":"content/governance-event","primary_archetype":"competing tender offer / control premium","loop_objective":"canonical_archetype_compression|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2023-02-10","evidence_available_at_that_date":"HYBE tender offer opened a control-premium route; Kakao later raised the cap with a higher tender offer.","evidence_source":"AP/public tender-war coverage; verify exact tender documents before implementation.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength"],"stage3_evidence_fields":["multiple_public_sources","durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv","profile_path":"atlas/symbol_profiles/041/041510.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-02-10","entry_price":114700,"MFE_30D_pct":40.54,"MFE_90D_pct":40.54,"MFE_180D_pct":40.54,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-6.45,"MAE_90D_pct":-23.63,"MAE_180D_pct":-23.63,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-03-08","peak_price":161200,"drawdown_after_peak_pct":-45.66,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"structural_success_competing_tender","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C32-SM-20230210-114700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG-C32-SM-20230308-4B-CAP","case_id":"C32-SM-20230210-HYBE-KAKAO-TENDER-WAR","symbol":"041510","company_name":"에스엠","round":"R13","loop":"14","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"COMPETING_TENDER_WAR","sector":"content/governance-event","primary_archetype":"competing tender offer / control premium","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B","trigger_date":"2023-03-08","evidence_available_at_that_date":"Kakao tender terms created an explicit event-price cap near the observed full-cycle peak.","evidence_source":"Public Kakao tender offer coverage; verify exact tender period/price before implementation.","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["explicit_event_cap","control_premium_or_event_premium","valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv","profile_path":"atlas/symbol_profiles/041/041510.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-03-08","entry_price":158500,"MFE_30D_pct":1.7,"MFE_90D_pct":1.7,"MFE_180D_pct":1.7,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-44.73,"MAE_90D_pct":-44.73,"MAE_180D_pct":-44.73,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-03-08","peak_price":161200,"drawdown_after_peak_pct":-45.66,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.942,"four_b_full_window_peak_proximity":0.942,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["explicit_event_cap","control_premium_or_event_premium","valuation_blowoff"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C32-SM-20230308-158500","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same_symbol_new_4B_timing_path","independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG-C32-HMM-20231219-STAGE2A","case_id":"C32-HMM-20231219-HARIM-PREFERRED-BIDDER","symbol":"011200","company_name":"HMM","round":"R13","loop":"14","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"PRIVATIZATION_PREFERRED_BIDDER_NO_TENDER_SPREAD","sector":"shipping/governance-event","primary_archetype":"privatization sale preferred bidder","loop_objective":"counterexample_mining|residual_false_positive_mining","trigger_type":"Stage2-Actionable","trigger_date":"2023-12-19","evidence_available_at_that_date":"Preferred-bidder control-sale optionality existed, but no binding cash tender spread or closing certainty existed; talks later failed.","evidence_source":"Secondary event summary; implementation should corroborate with KDB/KEXIM/KRX/DART.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["explicit_event_cap","contract_delay"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011200/2023.csv|atlas/ohlcv_tradable_by_symbol_year/011/011200/2024.csv","profile_path":"atlas/symbol_profiles/011/011200.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-12-19","entry_price":18430,"MFE_30D_pct":26.42,"MFE_90D_pct":26.42,"MFE_180D_pct":26.42,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.33,"MAE_90D_pct":-22.68,"MAE_180D_pct":-22.68,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-12-20","peak_price":23300,"drawdown_after_peak_pct":-38.84,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":["contract_delay"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"failed_rerating_preferred_bidder_spike","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_after_2023_11_10_candidate","same_entry_group_id":"C32-HMM-20231219-18430","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG-C32-HMM-20240208-4C","case_id":"C32-HMM-20231219-HARIM-PREFERRED-BIDDER","symbol":"011200","company_name":"HMM","round":"R13","loop":"14","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"PRIVATIZATION_PREFERRED_BIDDER_NO_TENDER_SPREAD","sector":"shipping/governance-event","primary_archetype":"privatization sale preferred bidder","loop_objective":"4C_thesis_break_timing_test","trigger_type":"Stage4C","trigger_date":"2024-02-08","evidence_available_at_that_date":"Sale negotiations failed; preferred-bidder control-sale thesis broke.","evidence_source":"Secondary event summary; implementation should corroborate with KDB/KEXIM/KRX/DART.","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":["contract_cancelled","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011200/2024.csv","profile_path":"atlas/symbol_profiles/011/011200.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-08","entry_price":18380,"MFE_30D_pct":4.57,"MFE_90D_pct":7.29,"MFE_180D_pct":13.17,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-14.04,"MAE_90D_pct":-22.47,"MAE_180D_pct":-22.47,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-03","peak_price":20800,"drawdown_after_peak_pct":-31.49,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"4C_success_thesis_broken","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C32-HMM-20240208-18380","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":false,"reuse_reason":"same_symbol_new_4C_timing_path","independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG-C32-NAMYANG-20240104-STAGE2A","case_id":"C32-NAMYANG-20240104-LEGAL-CONTROL-FINALITY","symbol":"003920","company_name":"남양유업","round":"R13","loop":"14","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"LEGAL_CONTROL_TRANSFER_LOW_LIQUIDITY_NO_TENDER_SPREAD","sector":"consumer/governance-event","primary_archetype":"legal control transfer finality","loop_objective":"counterexample_mining|residual_false_positive_mining","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-04","evidence_available_at_that_date":"Control-transfer legal finality resolved owner-risk but did not create a live cash tender/control-premium spread.","evidence_source":"Secondary company/court-event summary; implementation should corroborate with DART/court filings.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["explicit_event_cap"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003920/2024.csv","profile_path":"atlas/symbol_profiles/003/003920.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-04","entry_price":590000,"MFE_30D_pct":9.32,"MFE_90D_pct":9.32,"MFE_180D_pct":9.32,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-9.49,"MAE_90D_pct":-20.68,"MAE_180D_pct":-20.68,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-05","peak_price":645000,"drawdown_after_peak_pct":-27.44,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":["explicit_event_cap"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating_legal_control_finality","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; 2024-11-20 candidate outside 180D","same_entry_group_id":"C32-NAMYANG-20240104-590000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_c32_shadow","case_id":"C32-KZ-20240913-MBK-YP-TENDER","trigger_id":"TRG-C32-KZ-20240913-STAGE2A","symbol":"010130","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":70,"customer_quality_score":0,"policy_or_regulatory_score":80,"valuation_repricing_score":65,"execution_risk_score":0,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":70,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":85,"customer_quality_score":0,"policy_or_regulatory_score":95,"valuation_repricing_score":90,"execution_risk_score":0,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":88,"stage_label_after":"Stage3-Green-Event","changed_components":["policy_or_regulatory_score","valuation_repricing_score","legal_or_contract_risk_score","relative_strength_score"],"component_delta_explanation":"confirmed_cash_tender_route_plus_hostile_control_premium","MFE_90D_pct":261.41,"MAE_90D_pct":-1.65,"score_return_alignment_label":"positive_alignment_after_C32_event_override","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_c32_shadow","case_id":"C32-SM-20230210-HYBE-KAKAO-TENDER-WAR","trigger_id":"TRG-C32-SM-20230210-STAGE2A","symbol":"041510","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":80,"customer_quality_score":0,"policy_or_regulatory_score":70,"valuation_repricing_score":65,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":72,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":85,"customer_quality_score":0,"policy_or_regulatory_score":90,"valuation_repricing_score":85,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":87,"stage_label_after":"Stage3-Green-Event","changed_components":["policy_or_regulatory_score","valuation_repricing_score","legal_or_contract_risk_score","relative_strength_score"],"component_delta_explanation":"competing_tender_war_promotes_without_revision_requirement","MFE_90D_pct":40.54,"MAE_90D_pct":-23.63,"score_return_alignment_label":"positive_but_needs_4B_event_cap","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_c32_shadow","case_id":"C32-HMM-20231219-HARIM-PREFERRED-BIDDER","trigger_id":"TRG-C32-HMM-20231219-STAGE2A","symbol":"011200","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":55,"customer_quality_score":0,"policy_or_regulatory_score":75,"valuation_repricing_score":45,"execution_risk_score":0,"legal_or_contract_risk_score":50,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":45,"customer_quality_score":0,"policy_or_regulatory_score":55,"valuation_repricing_score":30,"execution_risk_score":0,"legal_or_contract_risk_score":80,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":62,"stage_label_after":"Stage2-Watch-Guarded","changed_components":["policy_or_regulatory_score","valuation_repricing_score","legal_or_contract_risk_score","relative_strength_score"],"component_delta_explanation":"preferred_bidder_without_binding_tender_spread_gets_guard","MFE_90D_pct":26.42,"MAE_90D_pct":-22.68,"score_return_alignment_label":"false_positive_reduced_by_guard","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_c32_shadow","case_id":"C32-NAMYANG-20240104-LEGAL-CONTROL-FINALITY","trigger_id":"TRG-C32-NAMYANG-20240104-STAGE2A","symbol":"003920","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":35,"customer_quality_score":0,"policy_or_regulatory_score":70,"valuation_repricing_score":40,"execution_risk_score":0,"legal_or_contract_risk_score":45,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":20,"customer_quality_score":0,"policy_or_regulatory_score":55,"valuation_repricing_score":25,"execution_risk_score":0,"legal_or_contract_risk_score":65,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":58,"stage_label_after":"Stage2-Watch-Guarded","changed_components":["policy_or_regulatory_score","valuation_repricing_score","legal_or_contract_risk_score","relative_strength_score"],"component_delta_explanation":"legal_finality_no_tender_spread_low_liquidity_guard","MFE_90D_pct":9.32,"MAE_90D_pct":-20.68,"score_return_alignment_label":"false_positive_reduced_by_guard","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R13","loop":"14","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"new_canonical_archetype_count":1,"new_trigger_family_count":4,"tested_existing_calibrated_axes":["price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["missed_structural_control_premium","preferred_bidder_false_positive","legal_control_finality_false_positive","4B_non_price_watch_too_early_for_full_window_peak"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.2 shadow_weight CSV rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c32_confirmed_cash_tender_or_competing_bidder_bonus,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"cash tender / competing bidder should override missing operating revision when price spread is explicit","promotes KZ/SM while preserving 4B caps","TRG-C32-KZ-20240913-STAGE2A|TRG-C32-SM-20230210-STAGE2A",4,4,2,medium,canonical_shadow_only,"not production; event-premium path"
shadow_weight,c32_no_binding_tender_spread_guard,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"preferred bidder or legal finality without cash tender spread behaved like false positive","guards HMM/Namyang","TRG-C32-HMM-20231219-STAGE2A|TRG-C32-NAMYANG-20240104-STAGE2A",4,4,2,medium,canonical_shadow_only,"not production; guard false control premium"
shadow_weight,c32_event_cap_4b_overlay,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"announced tender price cap/competing offer ceiling can be full-window 4B; non-price regulatory warning can be watch-only if full-window proximity is low","separates SM good 4B from Korea Zinc early watch","TRG-C32-SM-20230308-4B-CAP|TRG-C32-KZ-20241031-4B-WATCH",7,4,2,low,canonical_shadow_only,"4B overlay only; not entry promotion"

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
next_round = R7 or R8 undercovered sector
recommended_next_canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION or C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
reason = L10 now has C31 and C32 coverage; next useful residual research should broaden away from policy/governance event loops.
```

## 28. Source Notes

Stock-Web source fields and OHLC rows were read from `Songdaiki/stock-web` only. External event evidence was used for historical context, but the implementation phase should prefer primary DART/KRX/company filings wherever possible. This MD does not recommend any current or future investment action.
