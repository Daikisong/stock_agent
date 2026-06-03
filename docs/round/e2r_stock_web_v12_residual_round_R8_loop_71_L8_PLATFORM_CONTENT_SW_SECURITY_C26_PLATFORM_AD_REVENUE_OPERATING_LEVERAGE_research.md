# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R8
scheduled_loop = 71
completed_round = R8
completed_loop = 71
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id = PLATFORM_TRAFFIC_MIGRATION_MONETIZATION_REGULATORY_TRUST_SPLIT
output_file = e2r_stock_web_v12_residual_round_R8_loop_71_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md
round_schedule_status = valid
round_sector_consistency = pass
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_web_price_atlas_access_required = true
production_scoring_changed = false
shadow_weight_only = true
```

This loop adds 4 new independent cases, 2 counterexamples, and 3 residual errors for R8/L8_PLATFORM_CONTENT_SW_SECURITY/C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE.

## 1. Current Calibrated Profile Assumption

```text
before_profile_id = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
after_profile_id = proposed_C26_platform_monetization_and_event_cap_shadow_profile
```

The existing global calibration remains useful: price-only blowoff should not promote a positive stage, full 4B still needs non-price evidence, and hard 4C thesis break should route to protection rather than promotion. The residual issue in this R8 pass is more local: platform traffic, AI, creator migration, or commerce narrative should not be scored as Stage3-quality operating leverage unless the evidence ties traffic to monetization and does not carry unresolved control, regulatory, or trust caps.

## 2. Round / Large Sector / Canonical Archetype Scope

R8 maps to `L8_PLATFORM_CONTENT_SW_SECURITY`, and this file uses `C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE`.

The selected fine archetype is:

```text
PLATFORM_TRAFFIC_MIGRATION_MONETIZATION_REGULATORY_TRUST_SPLIT
```

Compression map:

```text
Twitch Korea exit / creator migration      -> C26 platform traffic migration
Google / YouTube Shopping commerce bridge  -> C26 platform monetization bridge
LINE Yahoo governance pressure             -> C26 regulatory control cap
Kakao founder/legal trust break            -> C26 platform trust-break 4C watch
```

## 3. Previous Coverage / Duplicate Avoidance Check

No stock_agent source code was opened. This run inherits the previous completed state: `R7 / Loop 71`, therefore the scheduled next state is `R8 / Loop 71`.

Novelty gate:

```text
new_independent_case_count = 4
reused_case_count = 0
new_symbol_count = 4
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 3
minimum_new_independent_case_ratio = 1.00
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

The loop intentionally avoids proving the generic Stage2 bonus again. It instead separates two paths inside the same canonical archetype: monetization-bridge positives and regulatory/trust-cap counterexamples.

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_data_source = Songdaiki/stock-web
price_data_repo = https://github.com/Songdaiki/stock-web
manifest_path = atlas/manifest.json
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
stock_web_manifest_max_date = 2026-02-20
source_name = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

Manifest-level validation status: usable for historical calibration. All four representative entries have a 180-trading-day forward window before manifest max date and no 2023-12~2025-02 corporate-action candidate overlap in their tested 180D windows.

## 5. Historical Eligibility Gate

| symbol | profile_path | entry_date | 180D forward available | corporate_action_window_status | calibration_usable |
|---:|---|---|---|---|---|
| 042000 | atlas/symbol_profiles/042/042000.json | 2023-12-06 | yes | clean_180D_window | true |
| 067160 | atlas/symbol_profiles/067/067160.json | 2023-12-07 | yes | clean_180D_window | true |
| 035420 | atlas/symbol_profiles/035/035420.json | 2024-05-13 | yes | clean_180D_window | true |
| 035720 | atlas/symbol_profiles/035/035720.json | 2024-07-23 | yes | clean_180D_window | true |

## 6. Canonical Archetype Compression Map

C26 is not simply "platform stock went up." It is the point where traffic, user migration, creators, merchants, or ad inventory passes through the monetization turnstile. The turnstile metaphor matters: people entering the platform are not revenue until there is a fee, ad load, commerce take-rate, payment volume, subscription, or creator monetization path.

```text
C26_positive_gate =
  platform demand shock
  + monetization bridge
  + non-price confirmation
  - unresolved regulatory/control/trust cap

C26_counterexample_gate =
  traffic or AI narrative
  + missing monetization bridge
  OR legal/regulatory/control cap
```

## 7. Case Selection Summary

| case_id | symbol | trigger_type | trigger_date | entry_date | entry_price | MFE90 | MAE90 | MFE180 | MAE180 | outcome | current_profile |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---|---|
| R8L71_C26_042000_CAFE24_GOOGLE_YOUTUBE_SHOPPING | 042000 | Stage2-Actionable | 2023-12-06 | 2023-12-06 | 22150 | 55.08 | -29.98 | 93.91 | -33.41 | structural_success_with_high_MAE_after_initial_rerating | current_profile_too_late |
| R8L71_C26_067160_SOOP_TWITCH_MIGRATION | 067160 | Stage2-Actionable | 2023-12-06 | 2023-12-07 | 76600 | 82.25 | -6.01 | 87.73 | -6.01 | structural_success_clean_traffic_migration | current_profile_correct |
| R8L71_C26_035420_NAVER_LINE_REGULATORY_CAP | 035420 | Stage2-Guard | 2024-05-13 | 2024-05-13 | 184300 | 3.42 | -18.01 | 3.42 | -18.01 | failed_rerating_event_cap | current_profile_false_positive |
| R8L71_C26_035720_KAKAO_LEGAL_TRUST_BREAK | 035720 | 4C-Watch | 2024-07-23 | 2024-07-23 | 38850 | 6.69 | -15.32 | 18.4 | -15.32 | 4C_watch_initial_drawdown_rebound_later | current_profile_4C_too_late |


## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 2
4C_case_count = 1
calibration_usable_case_count = 4
calibration_usable_trigger_count = 4
```

The positive side is Cafe24 and SOOP: both had an external traffic or partner catalyst that could plausibly turn into platform monetization. The counterexample side is NAVER and Kakao: both show that platform scale alone is a weak signal when the dominant evidence is regulatory, control, or legal/trust risk.

## 9. Evidence Source Map

| symbol | evidence timing | Stage2 evidence | Stage3 evidence | 4B/4C evidence |
|---:|---|---|---|---|
| 042000 | 2023-12-06 | strategic commerce platform event, relative strength | monetization bridge still needed | 2024-06 valuation/positioning watch |
| 067160 | 2023-12-06 -> 2023-12-07 entry | user/creator migration shock | creator retention and monetization conversion path | full-window 4B watch near 2024-07 peak |
| 035420 | 2024-05-13 | public regulatory/control issue | not enough for Stage3 promotion | regulatory event cap / thesis-break watch |
| 035720 | 2024-07-23 | public legal/trust break | none | hard 4C watch |

## 10. Price Data Source Map

| symbol | tradable shard(s) used | profile |
|---:|---|---|
| 042000 | atlas/ohlcv_tradable_by_symbol_year/042/042000/2023.csv; atlas/ohlcv_tradable_by_symbol_year/042/042000/2024.csv | atlas/symbol_profiles/042/042000.json |
| 067160 | atlas/ohlcv_tradable_by_symbol_year/067/067160/2023.csv; atlas/ohlcv_tradable_by_symbol_year/067/067160/2024.csv | atlas/symbol_profiles/067/067160.json |
| 035420 | atlas/ohlcv_tradable_by_symbol_year/035/035420/2024.csv | atlas/symbol_profiles/035/035420.json |
| 035720 | atlas/ohlcv_tradable_by_symbol_year/035/035720/2024.csv; atlas/ohlcv_tradable_by_symbol_year/035/035720/2025.csv | atlas/symbol_profiles/035/035720.json |

## 11. Case-by-Case Trigger Grid

| case_id | symbol | trigger_type | trigger_date | entry_date | entry_price | MFE90 | MAE90 | MFE180 | MAE180 | outcome | current_profile |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---|---|
| R8L71_C26_042000_CAFE24_GOOGLE_YOUTUBE_SHOPPING | 042000 | Stage2-Actionable | 2023-12-06 | 2023-12-06 | 22150 | 55.08 | -29.98 | 93.91 | -33.41 | structural_success_with_high_MAE_after_initial_rerating | current_profile_too_late |
| R8L71_C26_067160_SOOP_TWITCH_MIGRATION | 067160 | Stage2-Actionable | 2023-12-06 | 2023-12-07 | 76600 | 82.25 | -6.01 | 87.73 | -6.01 | structural_success_clean_traffic_migration | current_profile_correct |
| R8L71_C26_035420_NAVER_LINE_REGULATORY_CAP | 035420 | Stage2-Guard | 2024-05-13 | 2024-05-13 | 184300 | 3.42 | -18.01 | 3.42 | -18.01 | failed_rerating_event_cap | current_profile_false_positive |
| R8L71_C26_035720_KAKAO_LEGAL_TRUST_BREAK | 035720 | 4C-Watch | 2024-07-23 | 2024-07-23 | 38850 | 6.69 | -15.32 | 18.4 | -15.32 | 4C_watch_initial_drawdown_rebound_later | current_profile_4C_too_late |


## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | peak_date | peak_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | drawdown_after_peak |
|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 042000 | 22150 | 2024-06-26 | 42950 | 55.08 | 0.0 | 55.08 | -29.98 | 93.91 | -33.41 | -36.09 |
| 067160 | 76600 | 2024-07-11 | 143800 | 45.43 | -6.01 | 82.25 | -6.01 | 87.73 | -6.01 | -14.26 |
| 035420 | 184300 | 2024-05-16 | 190600 | 3.42 | -10.15 | 3.42 | -18.01 | 3.42 | -18.01 | -20.72 |
| 035720 | 38850 | 2025-02-10 | 46000 | 6.69 | -6.82 | 6.69 | -15.32 | 18.4 | -15.32 | -19.67 |


Calculation basis:

```text
MFE_N_pct = (max high over window / entry_price - 1) * 100
MAE_N_pct = (min low over window / entry_price - 1) * 100
peak_price = max high over observed representative forward window
drawdown_after_peak_pct = min low after peak / peak_price - 1
```

## 13. Current Calibrated Profile Stress Test

| case | P0 likely decision | actual alignment | verdict |
|---|---|---|---|
| Cafe24 | Stage3-Yellow after public partnership and relative strength | upside existed, but Green would have been late and MAE was high | current_profile_too_late |
| SOOP | Stage3-Yellow/Green as migration monetization became visible | aligned well; strong MFE with tolerable MAE | current_profile_correct |
| NAVER | generic platform/AI/commerce strength could over-score | poor MFE and sustained drawdown from regulatory cap | current_profile_false_positive |
| Kakao | generic platform value rebound could hide trust break | 90D protection useful, later rebound not enough to erase trust-risk lesson | current_profile_4C_too_late |

Answers to required profile questions:

```text
stage2_actionable_bonus = useful only if the case has a monetization bridge
yellow_threshold_75 = too loose for regulatory/control-cap cases
green_threshold_87 = acceptable; do not loosen for C26
green_revision_min_55 = keep
price_only_blowoff_guard = keep
full_4B_non_price_requirement = keep and strengthen with event-cap evidence
hard_4C_routing = keep, but allow earlier 4C-watch in legal/trust-break platform cases
```

## 14. Stage2 / Yellow / Green Comparison

Cafe24 and SOOP show why Stage2 can be valuable before clean financial confirmation. But C26 has a sharper edge than some industrial cases: if traffic is the river, monetization is the waterwheel. Without the waterwheel, more water only floods the field.

```text
green_lateness_ratio_Cafe24 = 0.59
green_lateness_ratio_SOOP = 0.34
green_lateness_ratio_NAVER = not_applicable
green_lateness_ratio_Kakao = not_applicable
```

Interpretation: early Stage2-Actionable is useful in C26 only when the evidence already shows traffic-to-revenue conversion. For NAVER/Kakao-style event caps, Stage2 must stay as watch/guard, not promotion.

## 15. 4B Local vs Full-window Timing Audit

| symbol | local proximity | full-window proximity | verdict |
|---:|---:|---:|---|
| 042000 | 0.94 | 0.94 | good full-window 4B timing if non-price overheat evidence is present |
| 067160 | 0.91 | 1.00 | good full-window 4B timing if retention/valuation saturation evidence is present |
| 035420 | 0.08 | 0.08 | event cap watch, not full 4B |
| 035720 | 0.03 | 0.00 | hard 4C watch, not 4B |

## 16. 4C Protection Audit

Kakao is the cleanest 4C-watch sample in this loop. The point is not that price never rebounded. The point is that legal/trust break changed the hypothesis class. Once the thesis moves from monetization to governance discount, the platform operating-leverage score should be capped until trust evidence is repaired.

NAVER is a softer 4C/watch case: regulatory control pressure was enough to block Stage3 promotion, but not necessarily enough for a hard 4C route.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
candidate_axis = platform_monetization_bridge_required
proposal = Stage2/Yellow promotion in L8 platform cases requires explicit bridge from traffic/user/creator/merchant growth to revenue, margin, take-rate, or durable retention.
```

Backtest effect:

```text
Cafe24 = pass
SOOP = pass
NAVER = fail unless control-risk resolved
Kakao = fail; route to legal/trust 4C-watch
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
candidate_axis = regulatory_trust_event_cap_guard
proposal = C26 Stage3 promotion is blocked when the dominant evidence is ownership/control pressure, legal investigation, founder arrest, accounting/trust break, or platform governance discount.
```

This is not a global rule proposal. It is a C26 shadow guard.

## 19. Before / After Backtest Comparison

| profile_id | scope | selected entries | avg_MFE90 | avg_MAE90 | avg_MFE180 | avg_MAE180 | false_positive_rate | alignment |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current proxy | 4 | 36.86 | -17.33 | 50.87 | -18.19 | 0.50 | mixed |
| P0b e2r_2_0_baseline_reference | rollback | 4 | 36.86 | -17.33 | 50.87 | -18.19 | 0.50 | too loose on platform narrative |
| P1 sector_specific_candidate_profile | L8 | 2 promoted, 2 guarded | 68.67 | -18.00 | 90.82 | -19.71 | 0.00 | improved |
| P2 canonical_archetype_candidate_profile | C26 | 2 promoted, 2 guarded | 68.67 | -18.00 | 90.82 | -19.71 | 0.00 | improved |
| P3 counterexample_guard_profile | C26 guard | NAVER/Kakao blocked | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | avoids false positives |

## 20. Score-Return Alignment Matrix

| symbol | before score/stage | after score/stage | score-return alignment |
|---:|---|---|---|
| 042000 | 78 / Stage3-Yellow | 84 / Stage3-Yellow watch | positive but volatile; bridge valid, Green not relaxed |
| 067160 | 82 / Stage3-Yellow | 88 / Stage3-Green with 4B watch | strong alignment |
| 035420 | 76 / Stage3-Yellow | 68 / Stage2-Guard | false positive reduced |
| 035720 | 73 / Stage2/Yellow border | 58 / 4C-Watch | trust-break protected |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | usable_triggers | representative_triggers | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L8_PLATFORM_CONTENT_SW_SECURITY | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | PLATFORM_TRAFFIC_MIGRATION_MONETIZATION_REGULATORY_TRUST_SPLIT | 2 | 2 | 2 | 1 | 4 | 0 | 4 | 4 | 3 | true | true | Need more C28 security/SaaS retention rows in later R8 cycles |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - platform traffic without monetization bridge
  - regulatory/control cap blocking platform operating leverage
  - legal/trust-break 4C watch in platform rerating
new_axis_proposed:
  - C26_platform_monetization_bridge_required
  - C26_regulatory_trust_event_cap_guard
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept:
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- historical trigger-level calibration only
- stock-web tradable_raw OHLC only
- no production scoring change
- no live candidate discovery
- no brokerage or auto-trading action
```

Non-validation scope:

```text
- no proof that these symbols are current candidates
- no claim that the public event source alone is a sufficient trading signal
- no stock_agent code inspection or patch
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C26_platform_monetization_bridge_required,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,1,+1,"Traffic/user migration alone is not enough; it must connect to ad/merchant/payment/creator monetization.","Improves positive selection: Cafe24 and SOOP pass; NAVER/Kakao do not.",R8L71_C26_042000_T1_STAGE2_ACTIONABLE|R8L71_C26_067160_T1_STAGE2_ACTIONABLE|R8L71_C26_035420_T1_STAGE2_GUARD|R8L71_C26_035720_T1_4C_WATCH,4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C26_regulatory_trust_event_cap_guard,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,1,+1,"Platform ownership/control/legal trust breaks cap the operating leverage score until resolved.","Reduces false-positive Yellow/Green pressure in NAVER and Kakao style cases.",R8L71_C26_035420_T1_STAGE2_GUARD|R8L71_C26_035720_T1_4C_WATCH,4,4,2,medium,counterexample_guard_profile,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R8L71_C26_042000_CAFE24_GOOGLE_YOUTUBE_SHOPPING","symbol":"042000","company_name":"카페24","round":"R8","loop":"71","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"PLATFORM_TRAFFIC_MIGRATION_MONETIZATION_REGULATORY_TRUST_SPLIT","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R8L71_C26_042000_T1_STAGE2_ACTIONABLE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"structural_success_with_high_MAE_after_initial_rerating","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Adds platform-merchant monetization bridge; does not relax Green because 90D/180D MAE remains large."}
{"row_type":"case","case_id":"R8L71_C26_067160_SOOP_TWITCH_MIGRATION","symbol":"067160","company_name":"SOOP","round":"R8","loop":"71","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"PLATFORM_TRAFFIC_MIGRATION_MONETIZATION_REGULATORY_TRUST_SPLIT","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R8L71_C26_067160_T1_STAGE2_ACTIONABLE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"structural_success_clean_traffic_migration","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"User migration is accepted as monetizable demand only when creator retention and usage conversion evidence exists."}
{"row_type":"case","case_id":"R8L71_C26_035420_NAVER_LINE_REGULATORY_CAP","symbol":"035420","company_name":"NAVER","round":"R8","loop":"71","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"PLATFORM_TRAFFIC_MIGRATION_MONETIZATION_REGULATORY_TRUST_SPLIT","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R8L71_C26_035420_T1_STAGE2_GUARD","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"failed_rerating_event_cap","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Regulatory/control cap overrides generic platform monetization bridge."}
{"row_type":"case","case_id":"R8L71_C26_035720_KAKAO_LEGAL_TRUST_BREAK","symbol":"035720","company_name":"카카오","round":"R8","loop":"71","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"PLATFORM_TRAFFIC_MIGRATION_MONETIZATION_REGULATORY_TRUST_SPLIT","case_type":"4C_success","positive_or_counterexample":"counterexample","best_trigger":"R8L71_C26_035720_T1_4C_WATCH","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"4C_watch_initial_drawdown_rebound_later","current_profile_verdict":"current_profile_4C_too_late","price_source":"Songdaiki/stock-web","notes":"Legal/trust break should route to 4C-watch even when later price rebound creates a false comfort signal."}
{"row_type":"trigger","trigger_id":"R8L71_C26_042000_T1_STAGE2_ACTIONABLE","case_id":"R8L71_C26_042000_CAFE24_GOOGLE_YOUTUBE_SHOPPING","symbol":"042000","company_name":"카페24","round":"R8","loop":"71","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"PLATFORM_TRAFFIC_MIGRATION_MONETIZATION_REGULATORY_TRUST_SPLIT","sector":"platform_content_sw_security","primary_archetype":"platform_ad_revenue_operating_leverage","loop_objective":"residual_false_positive_mining|sector_specific_rule_discovery|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2023-12-06","entry_date":"2023-12-06","entry_price":22150,"evidence_available_at_that_date":"Google/YouTube Shopping strategic investment and commerce traffic-to-merchant monetization bridge became visible; event created a platform operating-leverage path beyond generic traffic.","evidence_source":"public strategic investment / platform partnership event; stock-web price rows: 042/042000/2023.csv and 2024.csv","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","capacity_or_volume_route","policy_or_regulatory_optionality"],"stage3_evidence_fields":["repeat_order_or_conversion","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/042/042000/2023.csv","profile_path":"atlas/symbol_profiles/042/042000.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":55.08,"MFE_90D_pct":55.08,"MFE_180D_pct":93.91,"MFE_1Y_pct":93.91,"MFE_2Y_pct":null,"MAE_30D_pct":0.0,"MAE_90D_pct":-29.98,"MAE_180D_pct":-33.41,"MAE_1Y_pct":-36.79,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":true,"peak_date":"2024-06-26","peak_price":42950,"drawdown_after_peak_pct":-36.09,"green_lateness_ratio":0.59,"four_b_local_peak_proximity":0.94,"four_b_full_window_peak_proximity":0.94,"four_b_timing_verdict":"good_full_window_4B_timing_when_non_price_evidence_exists","four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success_with_high_MAE_after_initial_rerating","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L71_C26_042000_2023-12-06_22150","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R8L71_C26_067160_T1_STAGE2_ACTIONABLE","case_id":"R8L71_C26_067160_SOOP_TWITCH_MIGRATION","symbol":"067160","company_name":"SOOP","round":"R8","loop":"71","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"PLATFORM_TRAFFIC_MIGRATION_MONETIZATION_REGULATORY_TRUST_SPLIT","sector":"platform_content_sw_security","primary_archetype":"platform_ad_revenue_operating_leverage","loop_objective":"residual_false_positive_mining|sector_specific_rule_discovery|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2023-12-06","entry_date":"2023-12-07","entry_price":76600,"evidence_available_at_that_date":"Twitch Korea exit created a measurable creator/user migration route into AfreecaTV/SOOP; the evidence was a traffic-supply shock with direct ad/donation monetization optionality.","evidence_source":"public platform migration event; stock-web price rows: 067/067160/2023.csv and 2024.csv","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","capacity_or_volume_route","customer_or_order_quality"],"stage3_evidence_fields":["durable_customer_confirmation","repeat_order_or_conversion","financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/067/067160/2023.csv","profile_path":"atlas/symbol_profiles/067/067160.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":45.43,"MFE_90D_pct":82.25,"MFE_180D_pct":87.73,"MFE_1Y_pct":87.73,"MFE_2Y_pct":null,"MAE_30D_pct":-6.01,"MAE_90D_pct":-6.01,"MAE_180D_pct":-6.01,"MAE_1Y_pct":-18.41,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":143800,"drawdown_after_peak_pct":-14.26,"green_lateness_ratio":0.34,"four_b_local_peak_proximity":0.91,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_timing_if_supported_by_non_price_overheat_or_saturation_evidence","four_b_evidence_type":["positioning_overheat","valuation_blowoff","price_only"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success_clean_traffic_migration","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L71_C26_067160_2023-12-07_76600","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R8L71_C26_035420_T1_STAGE2_GUARD","case_id":"R8L71_C26_035420_NAVER_LINE_REGULATORY_CAP","symbol":"035420","company_name":"NAVER","round":"R8","loop":"71","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"PLATFORM_TRAFFIC_MIGRATION_MONETIZATION_REGULATORY_TRUST_SPLIT","sector":"platform_content_sw_security","primary_archetype":"platform_ad_revenue_operating_leverage","loop_objective":"residual_false_positive_mining|sector_specific_rule_discovery|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-Guard","trigger_date":"2024-05-13","entry_date":"2024-05-13","entry_price":184300,"evidence_available_at_that_date":"LINE Yahoo governance/regulatory pressure created an event cap; generic platform AI/commerce narrative could not be treated as clean operating leverage without ownership/control-risk adjustment.","evidence_source":"public LINE Yahoo governance/regulatory pressure; stock-web price row: 035/035420/2024.csv","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["legal_or_regulatory_block","explicit_event_cap","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/035/035420/2024.csv","profile_path":"atlas/symbol_profiles/035/035420.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.42,"MFE_90D_pct":3.42,"MFE_180D_pct":3.42,"MFE_1Y_pct":3.42,"MFE_2Y_pct":null,"MAE_30D_pct":-10.15,"MAE_90D_pct":-18.01,"MAE_180D_pct":-18.01,"MAE_1Y_pct":-18.01,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-16","peak_price":190600,"drawdown_after_peak_pct":-20.72,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.08,"four_b_full_window_peak_proximity":0.08,"four_b_timing_verdict":"event_cap_watch_not_full_4B_unless_regulatory_control_risk_is_explicit","four_b_evidence_type":["legal_or_regulatory_block","control_premium_or_event_premium"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating_event_cap","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L71_C26_035420_2024-05-13_184300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R8L71_C26_035720_T1_4C_WATCH","case_id":"R8L71_C26_035720_KAKAO_LEGAL_TRUST_BREAK","symbol":"035720","company_name":"카카오","round":"R8","loop":"71","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"PLATFORM_TRAFFIC_MIGRATION_MONETIZATION_REGULATORY_TRUST_SPLIT","sector":"platform_content_sw_security","primary_archetype":"platform_ad_revenue_operating_leverage","loop_objective":"residual_false_positive_mining|sector_specific_rule_discovery|counterexample_mining|coverage_gap_fill","trigger_type":"4C-Watch","trigger_date":"2024-07-23","entry_date":"2024-07-23","entry_price":38850,"evidence_available_at_that_date":"Founder/legal trust-break event around SM market-manipulation investigation changed the platform rerating problem from traffic monetization to governance discount and event-risk control.","evidence_source":"public legal/trust-break event; stock-web price rows: 035/035720/2024.csv and 2025.csv","stage2_evidence_fields":["public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["legal_or_regulatory_block","positioning_overheat","explicit_event_cap"],"stage4c_evidence_fields":["accounting_or_trust_break","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/035/035720/2024.csv","profile_path":"atlas/symbol_profiles/035/035720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.69,"MFE_90D_pct":6.69,"MFE_180D_pct":18.4,"MFE_1Y_pct":18.4,"MFE_2Y_pct":null,"MAE_30D_pct":-6.82,"MAE_90D_pct":-15.32,"MAE_180D_pct":-15.32,"MAE_1Y_pct":-15.32,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-02-10","peak_price":46000,"drawdown_after_peak_pct":-19.67,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.03,"four_b_full_window_peak_proximity":0.0,"four_b_timing_verdict":"hard_4C_watch_not_4B; price_rebound_does_not_repair_trust_evidence","four_b_evidence_type":["legal_or_regulatory_block","control_premium_or_event_premium"],"four_c_protection_label":"hard_4c_success_90D_risk_reduction_then_rebound","trigger_outcome_label":"4C_watch_initial_drawdown_rebound_later","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L71_C26_035720_2024-07-23_38850","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L71_C26_042000_CAFE24_GOOGLE_YOUTUBE_SHOPPING","trigger_id":"R8L71_C26_042000_T1_STAGE2_ACTIONABLE","symbol":"042000","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":5,"relative_strength_score":9,"customer_quality_score":8,"policy_or_regulatory_score":3,"valuation_repricing_score":8,"execution_risk_score":5,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":6,"relative_strength_score":9,"customer_quality_score":9,"policy_or_regulatory_score":3,"valuation_repricing_score":8,"execution_risk_score":5,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow_watch_for_4B_overlay","changed_components":["platform_monetization_bridge","regulatory_or_trust_guard","4B_or_4C_overlay_routing"],"component_delta_explanation":"Adds platform-merchant monetization bridge; does not relax Green because 90D/180D MAE remains large.","MFE_90D_pct":55.08,"MAE_90D_pct":-29.98,"score_return_alignment_label":"structural_success_with_high_MAE_after_initial_rerating","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L71_C26_067160_SOOP_TWITCH_MIGRATION","trigger_id":"R8L71_C26_067160_T1_STAGE2_ACTIONABLE","symbol":"067160","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":6,"relative_strength_score":9,"customer_quality_score":7,"policy_or_regulatory_score":1,"valuation_repricing_score":6,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":7,"revision_score":8,"relative_strength_score":9,"customer_quality_score":9,"policy_or_regulatory_score":1,"valuation_repricing_score":7,"execution_risk_score":3,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":88,"stage_label_after":"Stage3-Green_with_4B_watch","changed_components":["platform_monetization_bridge","regulatory_or_trust_guard","4B_or_4C_overlay_routing"],"component_delta_explanation":"User migration is accepted as monetizable demand only when creator retention and usage conversion evidence exists.","MFE_90D_pct":82.25,"MAE_90D_pct":-6.01,"score_return_alignment_label":"structural_success_clean_traffic_migration","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L71_C26_035420_NAVER_LINE_REGULATORY_CAP","trigger_id":"R8L71_C26_035420_T1_STAGE2_GUARD","symbol":"035420","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":6,"revision_score":6,"relative_strength_score":3,"customer_quality_score":6,"policy_or_regulatory_score":2,"valuation_repricing_score":5,"execution_risk_score":5,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":2,"customer_quality_score":5,"policy_or_regulatory_score":1,"valuation_repricing_score":3,"execution_risk_score":7,"legal_or_contract_risk_score":7,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_after":68,"stage_label_after":"Stage2-Guard","changed_components":["platform_monetization_bridge","regulatory_or_trust_guard","4B_or_4C_overlay_routing"],"component_delta_explanation":"Regulatory/control cap overrides generic platform monetization bridge.","MFE_90D_pct":3.42,"MAE_90D_pct":-18.01,"score_return_alignment_label":"failed_rerating_event_cap","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L71_C26_035720_KAKAO_LEGAL_TRUST_BREAK","trigger_id":"R8L71_C26_035720_T1_4C_WATCH","symbol":"035720","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":3,"customer_quality_score":6,"policy_or_regulatory_score":2,"valuation_repricing_score":4,"execution_risk_score":5,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable/Yellow_borderline","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":2,"customer_quality_score":5,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":8,"legal_or_contract_risk_score":9,"dilution_cb_risk_score":0,"accounting_trust_risk_score":8},"weighted_score_after":58,"stage_label_after":"4C-Watch","changed_components":["platform_monetization_bridge","regulatory_or_trust_guard","4B_or_4C_overlay_routing"],"component_delta_explanation":"Legal/trust break should route to 4C-watch even when later price rebound creates a false comfort signal.","MFE_90D_pct":6.69,"MAE_90D_pct":-15.32,"score_return_alignment_label":"4C_watch_initial_drawdown_rebound_later","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"residual_contribution","round":"R8","loop":"71","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["platform_traffic_without_control_risk_guard","legal_trust_break_not_routed_early_enough","monetization_bridge_missing_in_positive_cases"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 71
next_round = R9
next_loop = 71
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
stock_web_manifest_max_date = 2026-02-20
manifest = atlas/manifest.json
profiles =
  - atlas/symbol_profiles/042/042000.json
  - atlas/symbol_profiles/067/067160.json
  - atlas/symbol_profiles/035/035420.json
  - atlas/symbol_profiles/035/035720.json
price_rows =
  - atlas/ohlcv_tradable_by_symbol_year/042/042000/2023.csv
  - atlas/ohlcv_tradable_by_symbol_year/042/042000/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/067/067160/2023.csv
  - atlas/ohlcv_tradable_by_symbol_year/067/067160/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/035/035420/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/035/035720/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/035/035720/2025.csv
```

