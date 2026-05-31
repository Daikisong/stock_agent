# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R12
scheduled_loop: 15
completed_round: R12
completed_loop: 15
next_round: R13
next_loop: 15
round_schedule_status: valid
round_sector_consistency: pass
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: PUBLIC_HEALTH_AND_SUPPLY_PANIC_EVENT_CONVERSION_GUARD
output_file: e2r_stock_web_v12_residual_round_R12_loop_15_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This loop adds 3 new independent cases, 2 counterexamples, and 2 residual errors for R12/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C31_POLICY_SUBSIDY_LEGISLATION_EVENT.

## 1. Current Calibrated Profile Assumption

The current proxy is `e2r_2_1_stock_web_calibrated_proxy`. The already-applied axes are treated as live assumptions, not re-proposed as global deltas:

- `stage2_actionable_evidence_bonus = +2.0`
- `stage3_yellow_total_min = 75.0`
- `stage3_green_total_min = 87.0`
- `stage3_green_revision_min = 55.0`
- `stage3_cross_evidence_green_buffer = +1.5`
- `price_only_blowoff_blocks_positive_stage = true`
- `full_4b_requires_non_price_evidence = true`
- `hard_4c_thesis_break_routes_to_4c = true`

This MD only proposes C31-scoped shadow rules. It does not patch `stock_agent` and does not scan current/live candidates.

## 2. Round / Large Sector / Canonical Archetype Scope

R12 is treated as the residual “misc/service/agri/event” round. The chosen pair is valid because R12 may map to `L10_POLICY_EVENT_CROSS_REDTEAM_MISC` for policy, disaster, or cross-event residual work.

```text
scheduled_round = R12
scheduled_loop = 15
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
```

The selected canonical issue is simple: a policy or disaster event can move prices immediately, but only a subset turns into durable revenue, margin, or EPS. The research therefore separates **event visibility** from **conversion visibility**.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed `stock_agent` research artifacts were used only for coverage and duplicate avoidance. No `src/e2r` code was opened. The prior generated state in this session was R11 / Loop 15, so the next sequential round is R12 / Loop 15.

No prior C31 R12 Loop 15 result MD was found through repository search. This run therefore selects C31 and three new symbols:

- `096530` 씨젠 — public-health authorization converted into testing revenue.
- `065950` 웰크론 — COVID/mask demand event created high MFE but weak durable conversion.
- `277410` 인산가 — Fukushima wastewater/salt-buying scare created a sharp event premium but faded.

## 4. Stock-Web OHLC Input / Price Source Validation

`Songdaiki/stock-web` manifest fields checked:

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

Schema validation assumptions:

- tradable shard columns: `d,o,h,l,c,v,a,mc,s,m`
- raw shard columns: `d,o,h,l,c,v,a,mc,s,m,rs`
- `MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100`
- `MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100`

## 5. Historical Eligibility Gate

All representative triggers satisfy the 180-trading-day requirement and use stock-web `tradable_raw` rows.

| symbol | profile_path | 180D window | corporate_action_window_status | calibration_usable |
| --- | --- | --- | --- | --- |
| 096530 | atlas/symbol_profiles/096/096530.json | available | clean_180D_window; 2Y contaminated_or_unavailable | true |
| 065950 | atlas/symbol_profiles/065/065950.json | available | clean_180D_window | true |
| 277410 | atlas/symbol_profiles/277/277410.json | available | clean_180D_window | true |

## 6. Canonical Archetype Compression Map

```text
C31_POLICY_SUBSIDY_LEGISLATION_EVENT
  ├─ public_health_emergency_use_authorization_to_export_revenue_conversion
  ├─ public_health_mask_supply_shortage_without_durable_revision
  ├─ fukushima_wastewater_salt_hoarding_supply_scare
  └─ event_cap_4B_4C_overlay_for_panic_inventory
```

Compression rule: C31 should not classify “policy/disaster headline” itself as structural. It should classify the bridge after the headline:

```text
headline/event → procurement / authorization / quota / subsidy / repeat order / pricing visibility → revision bridge
```

## 7. Case Selection Summary

| case_id | symbol | role | trigger_family | current_profile_verdict | new? |
| --- | --- | --- | --- | --- | --- |
| R12L15_C31_SEEGENE_COVID_EUA_REVISION_SUCCESS | 096530 | positive | public_health_emergency_use_authorization_to_export_revenue_conversion | current_profile_correct | yes |
| R12L15_C31_WELCRON_MASK_EVENT_FALSE_POSITIVE | 065950 | counterexample | public_health_mask_supply_shortage_without_durable_revision | current_profile_false_positive | yes |
| R12L15_C31_INSANGA_SALT_PANIC_FALSE_POSITIVE | 277410 | counterexample | fukushima_wastewater_salt_hoarding_supply_scare | current_profile_false_positive | yes |


## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_or_4C_case_count = 2
calibration_usable_case_count = 3
new_independent_case_count = 3
```

The asymmetry is intentional. C31 is dangerous because the first price move often looks like Stage2 success. The two counterexamples are therefore more important than another positive: they define the guardrail boundary.

## 9. Evidence Source Map

| case_id | stage2 evidence | stage3 evidence | 4B / 4C evidence |
| --- | --- | --- | --- |
| SEEGENE | MFDS emergency-use authorization; COVID testing demand | production/export/revenue conversion | price-only local 4B was too early |
| WELCRON | first Korea COVID case; mask/protective-material demand | no durable revision bridge in trigger window | local event peak and later deep drawdown |
| INSANGA | Fukushima wastewater fear; salt-buying scare | no repeat-order / margin bridge | event cap, positioning overheat, later thesis fade |

Source notes:

- Seegene emergency-use authorization: MFDS authorization for Allplex 2019-nCoV Assay on 2020-02-12, as summarized in public company/history sources.
- Korea COVID timeline: first case announced 2020-01-20; domestic spread accelerated in February 2020.
- Fukushima wastewater / salt-buying: South Korean consumers rushed to buy salt before the expected treated-water release in June 2023; later protests and official monitoring continued.

## 10. Price Data Source Map

| symbol | company | price_shard_path | entry rows checked |
| --- | --- | --- | --- |
| 096530 | 씨젠 | atlas/ohlcv_tradable_by_symbol_year/096/096530/2020.csv | 2020-02-13, 2020-05-15, 2020-07-10 |
| 065950 | 웰크론 | atlas/ohlcv_tradable_by_symbol_year/065/065950/2020.csv | 2020-01-21 |
| 277410 | 인산가 | atlas/ohlcv_tradable_by_symbol_year/277/277410/2023.csv | 2023-06-08 |

## 11. Case-by-Case Trigger Grid

| trigger_id | entry | price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak | profile verdict | aggregate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SEEGENE_STAGE2_2020_02_12_EUA | 2020-02-13 | 31450 | 264.07 | 349.6 | 924.48 | -2.54 | -2.54 | -2.54 | 2020-08-10 / 322200 | current_profile_correct | representative |
| SEEGENE_GREEN_2020_05_14_REVENUE_CONVERSION | 2020-05-15 | 118400 | 2.87 | 172.13 | 172.13 | -13.6 | -13.6 | -13.6 | 2020-08-10 / 322200 | current_profile_correct | label_comparison_only |
| SEEGENE_4B_2020_07_10_PRICE_ONLY_LOCAL_PEAK | 2020-07-10 | 172500 | 86.78 | 86.78 | 86.78 | -6.9 | -6.9 | -6.9 | 2020-08-10 / 322200 | current_profile_4B_too_early | 4B_overlay_only |
| WELCRON_STAGE2_2020_01_20_FIRST_CASE | 2020-01-21 | 4900 | 118.37 | 118.37 | 118.37 | -4.49 | -4.49 | -4.49 | 2020-02-21 / 10700 | current_profile_false_positive | representative |
| INSANGA_STAGE2_2023_06_07_SALT_PANIC | 2023-06-08 | 2600 | 69.04 | 69.04 | 69.04 | -17.31 | -26.35 | -32.69 | 2023-06-16 / 4395 | current_profile_false_positive | representative |


## 12. Trigger-Level OHLC Backtest Tables

### 12.1 Representative aggregate triggers

| symbol | entry_date | entry_price | max high used | min low used | peak_date | MFE_180D | MAE_180D | drawdown_after_peak |
| --- | ---: | ---: | ---: | ---: | --- | ---: | ---: | ---: |
| 096530 | 2020-02-13 | 31,450 | 322,200 | 30,650 | 2020-08-10 | 924.48% | -2.54% | -33.77% |
| 065950 | 2020-01-21 | 4,900 | 10,700 | 4,680 | 2020-02-21 | 118.37% | -4.49% | -52.8% |
| 277410 | 2023-06-08 | 2,600 | 4,395 | 1,750 | 2023-06-16 | 69.04% | -32.69% | -60.18% |

### 12.2 Key OHLC row anchors

- Seegene Stage2 entry row: 2020-02-13 close 31,450; 2020-08-10 high 322,200.
- Seegene Green comparison row: 2020-05-15 close 118,400.
- Welcron Stage2 row: 2020-01-21 close 4,900; 2020-02-21 high 10,700.
- Insanga Stage2 row: 2023-06-08 close 2,600; 2023-06-16 high 4,395.

## 13. Current Calibrated Profile Stress Test

### 13.1 Seegene

The current profile is correct. The event was not just “COVID headline + price strength.” It had regulatory authorization and production/export conversion. The Stage3 Green threshold was not too strict here because the price path still left meaningful upside after conversion confirmation.

### 13.2 Welcron

The current profile is too permissive if it allows public-health event strength alone to become actionable. The 180D path produced high MFE but the same event failed to become a durable rerating. This is not a reason to weaken price-only blowoff guard; it is a reason to add a C31 event-conversion guard.

### 13.3 Insanga

The current profile is false-positive prone if salt-buying fear is scored as policy/event optionality without repeat-order or margin evidence. The 69.04% MFE was followed by a -60.18% post-peak drawdown, which is exactly the pattern C31 should cap.

## 14. Stage2 / Yellow / Green Comparison

Seegene is the exception that proves the guard:

```text
Stage2-Actionable entry = 31,450
Stage3-Green comparison entry = 118,400
full observed peak = 322,200
green_lateness_ratio = (118,400 - 31,450) / (322,200 - 31,450) = 0.30
```

Interpretation: Green was not too late. In most prior calibrated loops, Green lateness was the core problem. Here the residual issue is different: event-only names should not get promoted to Green at all. Seegene had a conversion bridge; Welcron and Insanga did not.

## 15. 4B Local vs Full-window Timing Audit

| trigger | local_proximity | full_window_proximity | verdict |
| --- | ---: | ---: | --- |
| SEEGENE_4B_2020_07_10_PRICE_ONLY_LOCAL_PEAK | 0.91 | 0.49 | price_only_local_4B_too_early |
| WELCRON_STAGE2_2020_01_20_FIRST_CASE | 0.71 | 0.71 | event peak reversal, not positive training |
| INSANGA_STAGE2_2023_06_07_SALT_PANIC | 0.81 | 0.81 | good event-cap 4B timing but negative-entry-only |

This strengthens the already-applied global 4B guard. Full 4B still requires non-price evidence. C31 adds a more specific idea: even when the event itself is “non-price,” panic inventory and public fear are not durable thesis evidence.

## 16. 4C Protection Audit

Insanga provides the cleanest 4C thesis-break/protection example. The June event spike lost its basis once the market moved from scarcity fear to normalization. The protection label is `hard_4c_success`: after the event-cap peak, later entry protection mattered more than trying to train the spike as a positive signal.

Welcron is classified as `thesis_break_watch_only` because the event was a demand shock, but no separate hard cancellation/approval failure occurred.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
```

R12/L10 is too broad to promote a sector-level rule from three cases. This should not change all L10 policy/event scoring. It is better represented as a C31 canonical-archetype shadow rule.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
```

Proposed C31 shadow rules:

1. `C31_conversion_bridge_bonus = +1`
   - Apply only when policy/disaster event has procurement, authorization, quota, subsidy, export permission, or repeat-order evidence.
2. `C31_panic_inventory_no_green_guard = true`
   - Panic buying, hoarding, infection-count headlines, or risk-perception spikes cannot cross Yellow/Green without revision or conversion.
3. `C31_event_cap_4B_overlay = +1`
   - Event expiration, official reassurance, supply normalization, or positioning blowoff should train risk overlay, not positive entry weights.

## 19. Before / After Backtest Comparison

| profile_id | scope | changed_axes | avg_MFE90 | avg_MAE90 | false_positive_rate | alignment |
| --- | --- | --- | --- | --- | --- | --- |
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | none | 179.0 | -11.13 | 0.67 | mixed: Seegene aligned, Welcron/Insanga require conversion guard |
| P0b_e2r_2_0_baseline_reference | rollback_reference | rollback only | 267.67 | -11.13 | 0.67 | weaker guardrail; too permissive for event-only Stage2 |
| P1_sector_specific_candidate_profile | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | event_conversion_required_for_green; panic_inventory_cap | 267.67 | -11.13 | 0.33 | better: blocks event-only false positives without weakening Seegene |
| P2_C31_canonical_archetype_candidate_profile | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31_conversion_bridge_bonus +1; C31_event_panic_no_green_guard true | 267.67 | -11.13 | 0.33 | best candidate: explains why Seegene was real while mask/salt spikes were capped |
| P3_counterexample_guard_profile | counterexample_guard | panic_event_stage3_blocker | 93.71 | -15.42 | 0.0 | strong guard for negative training; not a broad promotion profile |


## 20. Score-Return Alignment Matrix

| case | P0 verdict | after C31 guard | score-return alignment |
| --- | --- | --- | --- |
| Seegene | correct | keep promotion path | strong; conversion bridge explains MFE |
| Welcron | false-positive prone | cap at Stage2-Watch / 4B overlay | better; high MFE was not durable rerating |
| Insanga | false-positive prone | cap at Stage2-Watch / 4B/4C overlay | better; event panic faded sharply |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | PUBLIC_HEALTH_AND_SUPPLY_PANIC_EVENT_CONVERSION_GUARD | 1 | 2 | 2 | 1 | 3 | 0 | 5 | 3 | 2 | False | True | C31 now has public-health positive + mask/salt panic counterexamples; still needs non-health subsidy/tax/legislation holdouts |


## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - event_only_false_positive
  - panic_inventory_no_revision
  - price_only_local_4B_too_early
new_axis_proposed:
  - C31_conversion_bridge_bonus
  - C31_panic_inventory_no_green_guard
  - C31_event_cap_4B_overlay
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: []
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_green_revision_min
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

- historical only
- stock-web `tradable_raw` OHLC only
- 180D representative trigger calibration
- C31 canonical-archetype shadow rule only

Non-validation scope:

- no live candidates
- no current watchlist
- no stock recommendation
- no broker/API connection
- no `stock_agent` source-code inspection
- no production scoring patch

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C31_conversion_bridge_bonus,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,+1,+1,"EUA/procurement/export/order-conversion event should receive Stage2 evidence credit only when conversion path is visible","Keeps Seegene positive while avoiding generic event promotion","SEEGENE_STAGE2_2020_02_12_EUA",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C31_panic_inventory_no_green_guard,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,false,true,+1,"panic buying, hoarding, infection headline, or fear-driven supply scare cannot pass Yellow/Green without revision or conversion evidence","Would cap Welcron and Insanga false positives","WELCRON_STAGE2_2020_01_20_FIRST_CASE|INSANGA_STAGE2_2023_06_07_SALT_PANIC",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C31_event_cap_4B_overlay,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,+1,+1,"Event caps and public panic expiration should create 4B/4C risk overlays, not positive entry weights","Improves drawdown protection after salt/mask event peaks","SEEGENE_4B_2020_07_10_PRICE_ONLY_LOCAL_PEAK|INSANGA_STAGE2_2023_06_07_SALT_PANIC",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R12L15_C31_SEEGENE_COVID_EUA_REVISION_SUCCESS", "symbol": "096530", "company_name": "씨젠", "round": "R12", "loop": "15", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "PUBLIC_HEALTH_AND_SUPPLY_PANIC_EVENT_CONVERSION_GUARD", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "SEEGENE_STAGE2_2020_02_12_EUA", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "MFDS emergency-use authorization created a policy-event bridge into test-kit production/export revenue; Stage3 confirmation was not merely price momentum.", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "MFDS emergency-use authorization created a policy-event bridge into test-kit production/export revenue; Stage3 confirmation was not merely price momentum."}
{"row_type": "case", "case_id": "R12L15_C31_WELCRON_MASK_EVENT_FALSE_POSITIVE", "symbol": "065950", "company_name": "웰크론", "round": "R12", "loop": "15", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "PUBLIC_HEALTH_AND_SUPPLY_PANIC_EVENT_CONVERSION_GUARD", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "WELCRON_STAGE2_2020_01_20_FIRST_CASE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "A COVID/mask-supply shock produced very high MFE but never built a durable revision bridge; the move behaved like event inventory panic rather than structural rerating.", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "A COVID/mask-supply shock produced very high MFE but never built a durable revision bridge; the move behaved like event inventory panic rather than structural rerating."}
{"row_type": "case", "case_id": "R12L15_C31_INSANGA_SALT_PANIC_FALSE_POSITIVE", "symbol": "277410", "company_name": "인산가", "round": "R12", "loop": "15", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "PUBLIC_HEALTH_AND_SUPPLY_PANIC_EVENT_CONVERSION_GUARD", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "INSANGA_STAGE2_2023_06_07_SALT_PANIC", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Fukushima wastewater concerns and salt hoarding created a sharp event premium but the price path mean-reverted without repeat-order or margin evidence.", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Fukushima wastewater concerns and salt hoarding created a sharp event premium but the price path mean-reverted without repeat-order or margin evidence."}
{"row_type": "trigger", "trigger_id": "SEEGENE_STAGE2_2020_02_12_EUA", "case_id": "R12L15_C31_SEEGENE_COVID_EUA_REVISION_SUCCESS", "symbol": "096530", "company_name": "씨젠", "round": "R12", "loop": "15", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "PUBLIC_HEALTH_AND_SUPPLY_PANIC_EVENT_CONVERSION_GUARD", "sector": "policy_event_misc", "primary_archetype": "policy/disaster/supply-panic event with or without conversion bridge", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2020-02-12", "evidence_available_at_that_date": "MFDS emergency-use authorization for Seegene Allplex 2019-nCoV Assay; public-health emergency route existed before full earnings confirmation.", "evidence_source": "MFDS/Seegene EUA reported 2020-02-12; COVID-19 testing literature and public-health reporting.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/096/096530/2020.csv", "profile_path": "atlas/symbol_profiles/096/096530.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2020-02-13", "entry_price": 31450, "MFE_30D_pct": 264.07, "MFE_90D_pct": 349.6, "MFE_180D_pct": 924.48, "MFE_1Y_pct": 924.48, "MFE_2Y_pct": null, "MAE_30D_pct": -2.54, "MAE_90D_pct": -2.54, "MAE_180D_pct": -2.54, "MAE_1Y_pct": -2.54, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2020-08-10", "peak_price": 322200, "drawdown_after_peak_pct": -33.77, "green_lateness_ratio": 0.3, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_entry_trigger", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; 2Y contaminated_or_unavailable due 2021 corporate_action_candidate_dates", "same_entry_group_id": "SEEGENE_2020_02_13_CLOSE_31450", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "SEEGENE_GREEN_2020_05_14_REVENUE_CONVERSION", "case_id": "R12L15_C31_SEEGENE_COVID_EUA_REVISION_SUCCESS", "symbol": "096530", "company_name": "씨젠", "round": "R12", "loop": "15", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "PUBLIC_HEALTH_AND_SUPPLY_PANIC_EVENT_CONVERSION_GUARD", "sector": "policy_event_misc", "primary_archetype": "policy/disaster/supply-panic event with or without conversion bridge", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression", "trigger_type": "Stage3-Green", "trigger_date": "2020-05-14", "evidence_available_at_that_date": "Export/sales conversion was visible enough to mark confirmed revision route; this is label-comparison against Stage2 rather than aggregate representative.", "evidence_source": "Contemporaneous COVID test-kit export/revenue reporting and Seegene price row.", "stage2_evidence_fields": ["public_event_or_disclosure", "capacity_or_volume_route"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "multiple_public_sources", "repeat_order_or_conversion"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/096/096530/2020.csv", "profile_path": "atlas/symbol_profiles/096/096530.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2020-05-15", "entry_price": 118400, "MFE_30D_pct": 2.87, "MFE_90D_pct": 172.13, "MFE_180D_pct": 172.13, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -13.6, "MAE_90D_pct": -13.6, "MAE_180D_pct": -13.6, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2020-08-10", "peak_price": 322200, "drawdown_after_peak_pct": -33.77, "green_lateness_ratio": 0.3, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_entry_trigger", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "green_not_too_late_in_this_exception", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; 1Y/2Y contaminated_or_unavailable from 2021 corporate action candidates", "same_entry_group_id": "SEEGENE_2020_05_15_CLOSE_118400", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": false, "reuse_reason": "same case, Stage3 Green lateness comparison", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "SEEGENE_4B_2020_07_10_PRICE_ONLY_LOCAL_PEAK", "case_id": "R12L15_C31_SEEGENE_COVID_EUA_REVISION_SUCCESS", "symbol": "096530", "company_name": "씨젠", "round": "R12", "loop": "15", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "PUBLIC_HEALTH_AND_SUPPLY_PANIC_EVENT_CONVERSION_GUARD", "sector": "policy_event_misc", "primary_archetype": "policy/disaster/supply-panic event with or without conversion bridge", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2020-07-10", "evidence_available_at_that_date": "Price/volume local peak looked stretched, but full observed-cycle peak was still ahead; no hard non-price thesis break yet.", "evidence_source": "stock-web OHLC row; price-only local-peak timing audit.", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/096/096530/2020.csv", "profile_path": "atlas/symbol_profiles/096/096530.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2020-07-10", "entry_price": 172500, "MFE_30D_pct": 86.78, "MFE_90D_pct": 86.78, "MFE_180D_pct": 86.78, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -6.9, "MAE_90D_pct": -6.9, "MAE_180D_pct": -6.9, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2020-08-10", "peak_price": 322200, "drawdown_after_peak_pct": -33.77, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.91, "four_b_full_window_peak_proximity": 0.49, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "4B_too_early", "current_profile_verdict": "current_profile_4B_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; 1Y/2Y contaminated_or_unavailable from 2021 corporate action candidates", "same_entry_group_id": "SEEGENE_2020_07_10_CLOSE_172500", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "same case, 4B local/full-window timing audit", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "WELCRON_STAGE2_2020_01_20_FIRST_CASE", "case_id": "R12L15_C31_WELCRON_MASK_EVENT_FALSE_POSITIVE", "symbol": "065950", "company_name": "웰크론", "round": "R12", "loop": "15", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "PUBLIC_HEALTH_AND_SUPPLY_PANIC_EVENT_CONVERSION_GUARD", "sector": "policy_event_misc", "primary_archetype": "policy/disaster/supply-panic event with or without conversion bridge", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2020-01-20", "evidence_available_at_that_date": "South Korea confirmed its first COVID-19 case; mask/protective textile demand narrative appeared immediately in price and volume.", "evidence_source": "KDCA/public COVID timeline; stock-web OHLC.", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/065/065950/2020.csv", "profile_path": "atlas/symbol_profiles/065/065950.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2020-01-21", "entry_price": 4900, "MFE_30D_pct": 118.37, "MFE_90D_pct": 118.37, "MFE_180D_pct": 118.37, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -4.49, "MAE_90D_pct": -4.49, "MAE_180D_pct": -4.49, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2020-02-21", "peak_price": 10700, "drawdown_after_peak_pct": -52.8, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": 0.71, "four_b_full_window_peak_proximity": 0.71, "four_b_timing_verdict": "event_peak_reversal_but_no_positive_green_training", "four_b_evidence_type": ["positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "high_mfe_failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "WELCRON_2020_01_21_CLOSE_4900", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "INSANGA_STAGE2_2023_06_07_SALT_PANIC", "case_id": "R12L15_C31_INSANGA_SALT_PANIC_FALSE_POSITIVE", "symbol": "277410", "company_name": "인산가", "round": "R12", "loop": "15", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "PUBLIC_HEALTH_AND_SUPPLY_PANIC_EVENT_CONVERSION_GUARD", "sector": "policy_event_misc", "primary_archetype": "policy/disaster/supply-panic event with or without conversion bridge", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-06-07", "evidence_available_at_that_date": "South Korean salt-buying concern ahead of Fukushima treated-water release; event was visible, but evidence was a panic-demand shock rather than durable channel reorder.", "evidence_source": "AP/Reuters-style Fukushima wastewater and salt-buying reporting; stock-web OHLC.", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["explicit_event_cap", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/277/277410/2023.csv", "profile_path": "atlas/symbol_profiles/277/277410.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-06-08", "entry_price": 2600, "MFE_30D_pct": 69.04, "MFE_90D_pct": 69.04, "MFE_180D_pct": 69.04, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -17.31, "MAE_90D_pct": -26.35, "MAE_180D_pct": -32.69, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-06-16", "peak_price": 4395, "drawdown_after_peak_pct": -60.18, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": 0.81, "four_b_full_window_peak_proximity": 0.81, "four_b_timing_verdict": "good_full_window_4B_timing_but_negative_entry_training_only", "four_b_evidence_type": ["explicit_event_cap", "positioning_overheat", "price_only"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "false_positive_event_spike", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "INSANGA_2023_06_08_CLOSE_2600", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L15_C31_SEEGENE_COVID_EUA_REVISION_SUCCESS", "trigger_id": "SEEGENE_STAGE2_2020_02_12_EUA", "symbol": "096530", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 4, "revision_score": 8, "relative_strength_score": 8, "customer_quality_score": 10, "policy_or_regulatory_score": 18, "valuation_repricing_score": 0, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 73, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 4, "revision_score": 11, "relative_strength_score": 8, "customer_quality_score": 14, "policy_or_regulatory_score": 20, "valuation_repricing_score": 0, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 81, "stage_label_after": "Stage3-Yellow/Actionable", "changed_components": ["policy_or_regulatory_score", "+customer_quality_score", "+revision_score"], "component_delta_explanation": "C31 conversion-bridge bonus recognizes EUA plus production/export path before full financials.", "MFE_90D_pct": 349.6, "MAE_90D_pct": -2.54, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L15_C31_SEEGENE_COVID_EUA_REVISION_SUCCESS", "trigger_id": "SEEGENE_GREEN_2020_05_14_REVENUE_CONVERSION", "symbol": "096530", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 12, "revision_score": 32, "relative_strength_score": 13, "customer_quality_score": 15, "policy_or_regulatory_score": 18, "valuation_repricing_score": 5, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 88, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 12, "revision_score": 35, "relative_strength_score": 13, "customer_quality_score": 16, "policy_or_regulatory_score": 18, "valuation_repricing_score": 5, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 92, "stage_label_after": "Stage3-Green", "changed_components": ["revision_score", "+customer_quality_score"], "component_delta_explanation": "Green is supported by conversion evidence; no relaxation of global Green threshold required.", "MFE_90D_pct": 172.13, "MAE_90D_pct": -13.6, "score_return_alignment_label": "overlay_only", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L15_C31_SEEGENE_COVID_EUA_REVISION_SUCCESS", "trigger_id": "SEEGENE_4B_2020_07_10_PRICE_ONLY_LOCAL_PEAK", "symbol": "096530", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 16, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 20, "execution_risk_score": 8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 72, "stage_label_before": "Stage4B-Watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 16, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 20, "execution_risk_score": 14, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 66, "stage_label_after": "Stage4B-Watch", "changed_components": ["execution_risk_score"], "component_delta_explanation": "Price-only local blowoff looked close to a local top but was too early versus full-window peak.", "MFE_90D_pct": 86.78, "MAE_90D_pct": -6.9, "score_return_alignment_label": "overlay_only", "current_profile_verdict": "current_profile_4B_too_early"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L15_C31_WELCRON_MASK_EVENT_FALSE_POSITIVE", "trigger_id": "WELCRON_STAGE2_2020_01_20_FIRST_CASE", "symbol": "065950", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 20, "customer_quality_score": 2, "policy_or_regulatory_score": 14, "valuation_repricing_score": 0, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow false-positive risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 14, "customer_quality_score": 2, "policy_or_regulatory_score": 8, "valuation_repricing_score": 0, "execution_risk_score": 16, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 63, "stage_label_after": "Stage2-Watch/4B-overlay", "changed_components": ["-policy_or_regulatory_score", "-relative_strength_score", "+execution_risk_score"], "component_delta_explanation": "Mask panic has event evidence and price strength but lacks procurement/revision bridge; cap positive promotion.", "MFE_90D_pct": 118.37, "MAE_90D_pct": -4.49, "score_return_alignment_label": "negative_guard_needed", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L15_C31_INSANGA_SALT_PANIC_FALSE_POSITIVE", "trigger_id": "INSANGA_STAGE2_2023_06_07_SALT_PANIC", "symbol": "277410", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 19, "customer_quality_score": 1, "policy_or_regulatory_score": 14, "valuation_repricing_score": 0, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable false-positive risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 13, "customer_quality_score": 1, "policy_or_regulatory_score": 7, "valuation_repricing_score": 0, "execution_risk_score": 18, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 60, "stage_label_after": "Stage2-Watch/4B-overlay", "changed_components": ["-policy_or_regulatory_score", "-relative_strength_score", "+execution_risk_score"], "component_delta_explanation": "Salt-hoarding supply scare has no channel reorder or margin bridge; route to event-cap overlay.", "MFE_90D_pct": 69.04, "MAE_90D_pct": -26.35, "score_return_alignment_label": "negative_guard_needed", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R12", "loop": "15", "scheduled_round": "R12", "scheduled_loop": 15, "round_schedule_status": "valid", "round_sector_consistency": "pass", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "current_profile_error_count": 2, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["event_only_false_positive", "panic_inventory_no_revision", "price_only_local_4B_too_early"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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
completed_round = R12
completed_loop = 15
next_round = R13
next_loop = 15
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Stock-Web manifest: `atlas/manifest.json`, max_date `2026-02-20`.
- Stock-Web schema: `atlas/schema.json`, `tradable_raw`, raw unadjusted marcap.
- OHLC shards used:
  - `atlas/ohlcv_tradable_by_symbol_year/096/096530/2020.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/065/065950/2020.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/277/277410/2023.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/277/277410/2024.csv`
- Profiles used:
  - `atlas/symbol_profiles/096/096530.json`
  - `atlas/symbol_profiles/065/065950.json`
  - `atlas/symbol_profiles/277/277410.json`
- External historical event checks:
  - Seegene COVID-19 emergency-use authorization, 2020-02-12.
  - South Korea COVID-19 first case, 2020-01-20.
  - Fukushima wastewater / salt-buying public concern in Korea, June-August 2023.

