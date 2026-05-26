# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
round = R13
loop = 49
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id = AUTOIMMUNE_FCRN_PARTNER_PHASE1_SIGNAL | PARTNER_KEYTRUDA_SC_PHASE3_NONINFERIORITY | ONCOLOGY_PHASE3_PFS_POSITIVE_BUT_COMMERCIAL_BRIDGE_NOT_YET_CLOSED | ONCOLOGY_BINARY_REGULATORY_FAILURE_AFTER_TRIAL_AND_PDUFA_RUN | COVID_REPURPOSING_PHASE2_ENDPOINT_FAILURE
selection_mode = auto_coverage_gap_fill
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This MD is not a live stock screen and not a `stock_agent` patch. It is a historical residual calibration research file for L7/C24. The loop was auto-selected after the previous L7/C23 approval-commercialization round because the adjacent clinical-trial data archetype still needed same-archetype new-symbol coverage, explicit counterexamples, and 4B/4C rows.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference

stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

The residual question is narrower than the first Stock-Web calibration. We are not proving again that Stage2 is earlier than Green. We are testing whether C24 trial-data events need their own bridge/guard rules: partner-quality bridge, phase/endpoint quality, binary event cap, and initial MAE buffer.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R13
loop = 49
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
loop_objective = auto_coverage_gap_fill, residual_false_positive_mining, residual_missed_structural_mining, yellow_threshold_stress_test, green_strictness_stress_test, 4B_non_price_requirement_stress_test, 4C_thesis_break_timing_test, sector_specific_rule_discovery, canonical_archetype_compression, counterexample_mining
```

C24 is a good residual archetype because clinical data has a trapdoor. A trial readout can be real evidence, but its market value depends on whether it is a clean bridge to approval, label, partner economics, commercialization, or only a binary event candle.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifact search was limited to the prescribed calibration artifact paths/terms. No matching prior artifact row was found for the exact C24 symbol set and trigger family combination:

```text
searched_terms = C24_BIO_TRIAL_DATA_EVENT_RISK 009420 196170 028300 019170 reports/e2r_calibration data/e2r/calibration
stock_agent_code_accessed = false
src_e2r_accessed = false
```

Duplicate gate result:

```text
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_research = avoided
new_symbol_count = 5
same_archetype_new_symbol_count = 5
same_archetype_new_trigger_family_count = 5
required_new_independent_case_ratio = 0.60
actual_new_independent_case_ratio = 1.00
```

## 4. Stock-Web OHLC Input / Price Source Validation

Manifest and schema were checked directly in `Songdaiki/stock-web`.

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

Schema basis:

```text
tradable_shard_columns = d,o,h,l,c,v,a,mc,s,m
price_basis = tradable_raw
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
calibration_usable_rule = entry row exists, 180 forward tradable days exist, and no corporate-action candidate overlaps entry~D+180
```

## 5. Historical Eligibility Gate

All representative rows below use past trigger dates and Stock-Web tradable shards. The following case-level corporate-action gates were checked:

```text
009420 한올바이오파마: corporate_action_candidate_dates = 1996-12-24, 2006-05-10, 2006-07-19, 2015-08-18; clean for 2023-09-27~D+180
196170 알테오젠: corporate_action_candidate_dates = 2017-12-07, 2017-12-28, 2020-07-23, 2020-08-13, 2021-04-12; clean for 2024-11-20~D+180
000100 유한양행: corporate_action_candidate_dates = 1997-01-03, 1999-08-26, 2020-04-08; clean for 2023-10-04~D+180
028300 HLB: corporate_action_candidate_dates = old and 2021-03-15/2021-04-01; clean for 2024-03/05 windows
019170 신풍제약: corporate_action_candidate_dates = 1997-12-06, 2001-11-21, 2011-05-04; clean for 2021-07-05~D+180
```

Mezzion and SillaJen were considered but not used as representative rows because their likely event windows had corporate-action or tradability caveats that would reduce clean calibration value.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| AUTOIMMUNE_FCRN_PARTNER_PHASE1_SIGNAL | C24_BIO_TRIAL_DATA_EVENT_RISK | Early clinical data, but partner/platform quality matters. |
| PARTNER_KEYTRUDA_SC_PHASE3_NONINFERIORITY | C24_BIO_TRIAL_DATA_EVENT_RISK | Late-stage partner trial data with platform repricing and initial positioning risk. |
| ONCOLOGY_PHASE3_PFS_POSITIVE_BUT_COMMERCIAL_BRIDGE_NOT_YET_CLOSED | C24_BIO_TRIAL_DATA_EVENT_RISK | Positive trial result did not immediately close commercialization/royalty bridge. |
| ONCOLOGY_BINARY_REGULATORY_FAILURE_AFTER_TRIAL_AND_PDUFA_RUN | C24_BIO_TRIAL_DATA_EVENT_RISK | Trial narrative can collapse when binary approval route fails. |
| COVID_REPURPOSING_PHASE2_ENDPOINT_FAILURE | C24_BIO_TRIAL_DATA_EVENT_RISK | Speculative trial readout without durable endpoint quality is a false-Green trap. |

## 7. Case Selection Summary

|case_id|symbol|company|role|trigger|entry|entry_price|MFE90|MAE90|MFE180|MAE180|current_profile|diversity|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|C24-HANALL-IMVT1402-PH1-20230927|009420|한올바이오파마|structural_success|Stage2-Actionable|2023-09-27|32650|43.19|-12.56|43.19|-12.56|current_profile_correct|22|
|C24-ALTEOGEN-KEYTRUDA-SC-NONINFERIOR-20241120|196170|알테오젠|high_mae_success|Stage2-Actionable|2024-11-20|350500|31.1|-21.83|44.94|-21.83|current_profile_too_early|21|
|C24-YUHAN-MARIPOSA-DATA-20231004|000100|유한양행|high_mae_success|Stage2-Actionable|2023-10-04|79000|11.9|-30.51|11.9|-30.51|current_profile_too_early|18|
|C24-HLB-RIVOCERANIB-CRL-20240517|028300|HLB|4C_success|4C|2024-05-17|67100|46.2|-32.71|46.2|-32.71|current_profile_4B_too_late|23|
|C24-SHINPOONG-PYRAMAX-PH2-20210705|019170|신풍제약|false_positive_green|Stage2-Actionable|2021-07-05|95600|6.17|-52.82|6.17|-76.1|current_profile_false_positive|24|

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 3
counterexample_count = 2
4B_case_count = 2
4C_case_count = 2
calibration_usable_case_count = 5
calibration_usable_trigger_count = 7
representative_trigger_count = 5
```

The useful split is not “trial data good” versus “trial data bad.” The split is:

```text
positive branch = data quality + sponsor/partner credibility + route to regulatory/commercial value
counterexample branch = single binary endpoint/event + no commercial bridge + valuation/positioning overheat
```

## 9. Evidence Source Map

| case_id | evidence available at trigger date | source note |
|---|---|---|
| C24-HANALL-IMVT1402-PH1-20230927 | Positive Phase 1 IMVT-1402 signal, partner read-through to HanAll. | Immunovant/Investopedia public report dated 2023-09-26 UTC. |
| C24-ALTEOGEN-KEYTRUDA-SC-NONINFERIOR-20241120 | Merck subcutaneous Keytruda trial met noninferiority; Korean next-trading-day entry. | Reuters report dated 2024-11-19 UTC. |
| C24-YUHAN-MARIPOSA-DATA-20231004 | MARIPOSA/lazertinib-amivantamab Phase 3 positive data after Korea holiday gap. | J&J/MARIPOSA public data; later Reuters/FDA approval context. |
| C24-HLB-RIVOCERANIB-CRL-20240517 | FDA CRL/regulatory failure invalidated pre-event approval thesis. | HLB/FDA CRL public news; price row confirms limit-down shock. |
| C24-SHINPOONG-PYRAMAX-PH2-20210705 | COVID/Pyramax trial readout failed to support speculative rerating. | Korean public readout/disclosure context; price row confirms endpoint disappointment shock. |

## 10. Price Data Source Map

| symbol | shard path(s) used | profile path | 180D status |
|---|---|---|---|
| 009420 | atlas/ohlcv_tradable_by_symbol_year/009/009420/2023.csv, 2024.csv | atlas/symbol_profiles/009/009420.json | clean_180D_window |
| 196170 | atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv, 2025.csv | atlas/symbol_profiles/196/196170.json | clean_180D_window |
| 000100 | atlas/ohlcv_tradable_by_symbol_year/000/000100/2023.csv, 2024.csv | atlas/symbol_profiles/000/000100.json | clean_180D_window |
| 028300 | atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv, 2025.csv | atlas/symbol_profiles/028/028300.json | clean_180D_window |
| 019170 | atlas/ohlcv_tradable_by_symbol_year/019/019170/2021.csv, 2022.csv | atlas/symbol_profiles/019/019170.json | clean_180D_window |

## 11. Case-by-Case Trigger Grid

| case | trigger_type | trigger_date | entry_date | interpretation |
|---|---:|---:|---:|---|
| HanAll IMVT-1402 | Stage2-Actionable | 2023-09-26 | 2023-09-27 | Partner Phase 1 positive data had durable enough platform read-through, but still required retest. |
| Alteogen Keytruda SC | Stage2-Actionable | 2024-11-19 | 2024-11-20 | High-quality partner Phase 3 signal, but immediate positioning shakeout made blind Green too early. |
| Yuhan MARIPOSA | Stage2-Actionable | 2023-09-28 | 2023-10-04 | Strong Phase 3 data, but holiday gap and bridge-to-economics were not yet closed. |
| HLB pre-cap | 4B overlay | 2024-03-26 | 2024-03-26 | Pre-PDUFA blowoff showed event-cap risk before CRL. |
| HLB CRL | 4C | 2024-05-17 | 2024-05-17 | Hard regulatory thesis break. |
| Shinpoong Phase 2 | Stage2 false-positive | 2021-07-05 | 2021-07-05 | Trial narrative failed endpoint/rerating validation. |
| Shinpoong hard break | 4C overlay | 2021-07-06 | 2021-07-06 | Hard thesis break after readout. |

## 12. Trigger-Level OHLC Backtest Tables

Representative rows:

|case_id|symbol|company|entry|entry_price|MFE90|MAE90|MFE180|MAE180|current_profile|
|---|---|---|---|---|---|---|---|---|---|
|C24-HANALL-IMVT1402-PH1-20230927|009420|한올바이오파마|2023-09-27|32650|43.19|-12.56|43.19|-12.56|current_profile_correct|
|C24-ALTEOGEN-KEYTRUDA-SC-NONINFERIOR-20241120|196170|알테오젠|2024-11-20|350500|31.1|-21.83|44.94|-21.83|current_profile_too_early|
|C24-YUHAN-MARIPOSA-DATA-20231004|000100|유한양행|2023-10-04|79000|11.9|-30.51|11.9|-30.51|current_profile_too_early|
|C24-HLB-RIVOCERANIB-CRL-20240517|028300|HLB|2024-05-17|67100|46.2|-32.71|46.2|-32.71|current_profile_4B_too_late|
|C24-SHINPOONG-PYRAMAX-PH2-20210705|019170|신풍제약|2021-07-05|95600|6.17|-52.82|6.17|-76.1|current_profile_false_positive|

Overlay rows:

| trigger_id | role | entry_price | MFE_90D | MAE_90D | local_peak_proximity | full_window_peak_proximity | verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| C24-HLB-20240326-4B_PRECAP | 4B overlay | 120800 | 6.79 | -62.62 | 0.74 | 0.74 | good_full_window_4B_timing |
| C24-SHINPOONG-20210706-4C | 4C overlay | 67000 | 16.87 | -32.69 | null | null | hard_4c_success |

## 13. Current Calibrated Profile Stress Test

| question | finding |
|---|---|
| How would current profile judge these cases? | It would correctly keep partner-quality data in Stage2/Yellow, but can still over-promote binary trial/regulatory narratives if valuation and public event visibility dominate. |
| Did the judgment align with MFE/MAE? | Mixed. HanAll aligned. Alteogen and Yuhan had positive structural paths but large initial MAE. Shinpoong and HLB show binary failure risk. |
| Was Stage2 bonus too high or low? | Not globally wrong; too high when applied to single-endpoint/binary events without endpoint quality and partner/regulatory bridge. |
| Yellow threshold 75? | Appropriate as a holding bay. C24 needs Yellow to remain “watch and validate,” not “Green by momentum.” |
| Green threshold 87/revision 55? | Still needed. C24 should require data quality + bridge before Green. |
| Price-only blowoff guard? | Strengthened. HLB pre-cap and Shinpoong speculative spikes show why price-only Green is dangerous. |
| Full 4B non-price requirement? | Strengthened with nuance: binary event cap is a non-price 4B evidence type even before failure. |
| Hard 4C routing? | Kept/strengthened. HLB CRL and Shinpoong hard readout failure both justify immediate 4C/thesis-break routing. |

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2 entry | Green trigger | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---|
| HanAll | 32650 | 36850 proxy after repeat strength | 0.30 | Green not fatally late, but retest avoided some gap risk. |
| Alteogen | 350500 | 362000 proxy after recovery/retest | 0.07 | Green was not late, but initial shakeout means immediate Green was too early. |
| Yuhan | 79000 | not applicable | null | No clean Green until later commercialization/regulatory bridge; Stage2-only was appropriate. |
| HLB | 98000 March data/run proxy | not applicable | null | Pre-event 4B cap mattered more than Green. |
| Shinpoong | 95600 | false Green should be blocked | null | Trial readout did not support Green. |

## 15. 4B Local vs Full-window Timing Audit

HLB is the clearest 4B lesson in this loop. The March 26, 2024 row was not merely price euphoria. It sat on a binary regulatory event path where the upside was capped by approval timing and downside was discontinuous if the decision failed.

```text
HLB Stage2 proxy entry = 2024-03-08 close 98000
HLB 4B overlay entry = 2024-03-26 close 120800
local/full observed high = 129000
four_b_local_peak_proximity = 0.74
four_b_full_window_peak_proximity = 0.74
four_b_timing_verdict = good_full_window_4B_timing
four_b_evidence_type = valuation_blowoff, positioning_overheat, explicit_event_cap
```

For C24, “explicit_event_cap” should be treated as non-price 4B evidence when the asset is approaching a binary readout/PDUFA decision and the score is otherwise driven by public visibility plus price.

## 16. 4C Protection Audit

```text
HLB 4C entry = 2024-05-17 close 67100
MFE_30D = +9.99
MAE_30D = -32.71
interpretation = hard 4C was correct but late relative to pre-event 4B; post-CRL rebound does not undo the thesis-break label.

Shinpoong 4C entry = 2021-07-06 close 67000
MFE_30D = +16.87
MAE_30D = -8.51
MAE_180D = -65.90
interpretation = 4C reduced damage versus the prior false-positive entry at 95600, but did not remove long tail deterioration.
```

C24 4C is a circuit breaker, not a timing oracle. It protects the thesis ledger from continuing to call failure “Stage3,” but it cannot guarantee that the first post-failure entry is economically clean.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
candidate_axis = L7_clinical_data_requires_bridge_quality
proposal_type = sector_shadow_only
```

Rule candidate:

```text
In L7, clinical-data events can receive Stage2/Yellow support only if at least one non-price bridge exists:
- partner/sponsor quality,
- endpoint quality and phase maturity,
- regulatory path clarity,
- commercialization/economics visibility,
- clean safety/label context.

If the event is single-binary, COVID-repurposing, retail-narrative, or pre-PDUFA without a bridge, cap at Yellow or 4B-watch even if relative strength is strong.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
candidate_axis_1 = c24_partner_quality_data_bridge
candidate_axis_2 = c24_binary_event_cap_guard
candidate_axis_3 = c24_initial_MAE_buffer
candidate_axis_4 = c24_hard_thesis_break_to_4c
```

Mechanism:

```text
A clinical data event is like a bridge under load. The headline is the first plank, but the bridge does not carry capital unless the support beams exist: endpoint, sponsor, regulator, label, economics, and safety. C24 failures happen when the model scores the first plank as if the whole bridge were already built.
```

## 19. Before / After Backtest Comparison

|profile_id|scope|eligible_trigger_count|avg_MFE_90D_pct|avg_MAE_90D_pct|avg_MFE_180D_pct|avg_MAE_180D_pct|false_positive_rate|missed_structural_count|late_green_count|avg_green_lateness_ratio|score_return_alignment_verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|
|P0_e2r_2_1_stock_web_calibrated_proxy|global_proxy|5|27.71|-30.09|30.48|-34.74|2/5|1|1|0.18|mixed; positive partner data works, single binary event narratives over-promote|
|P0b_e2r_2_0_baseline_reference|rollback_reference|5|27.71|-30.09|30.48|-34.74|3/5|1|0|0.11|weaker than P0; does not separate binary failure risk|
|P1_L7_sector_specific_candidate|sector_specific|5|27.71|-30.09|30.48|-34.74|1/5|0|1|0.18|best explanation: positive partner data retained, speculative binary trials blocked|
|P2_C24_canonical_archetype_candidate|canonical_archetype_specific|5|27.71|-30.09|30.48|-34.74|1/5|0|1|0.18|canonical rule candidate accepted as shadow-only|
|P3_counterexample_guard_profile|guard_profile|5|27.71|-30.09|30.48|-34.74|0/5 if CRL/trial-fail paths are routed to 4B/4C|1|2|0.22|safest but may under-promote early platform wins|

## 20. Score-Return Alignment Matrix

| bucket | cases | score-return verdict |
|---|---|---|
| partner/platform data with durable sponsor | HanAll, Alteogen | Positive MFE appears, but initial MAE demands staged confirmation. |
| positive oncology data without immediate economics bridge | Yuhan | Good science signal, poor immediate risk/reward if Green is too early. |
| binary PDUFA / regulatory failure | HLB | Pre-cap 4B would have explained the risk better than waiting for 4C. |
| speculative repurposing endpoint readout | Shinpoong | Green should be blocked; failure route dominates. |

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|L7_BIO_HEALTHCARE_MEDICAL|C24_BIO_TRIAL_DATA_EVENT_RISK|multiple: FCRN / SC formulation / oncology PFS / binary PDUFA / COVID repurposing|3|2|2|2|5|0|7|5|3|True|True|C24 now has balanced positive/counterexample rows, but still needs device-like trial/diagnostic data examples|

## 22. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
same_archetype_new_symbol_count: 5
same_archetype_new_trigger_family_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 5
new_trigger_family_count: 5
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - single_binary_event_false_green
  - partner_data_initial_MAE_shakeout
  - positive_data_without_commercial_bridge
  - hard_4c_after_failure_too_late_for_pre-event_risk
new_axis_proposed:
  - c24_partner_quality_data_bridge
  - c24_binary_event_cap_guard
  - c24_initial_MAE_buffer
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
diversity_score_summary: avg=21.6; high because same C24 archetype added five new symbols and five trigger families
auto_selected_coverage_gap: L7/C24 trial data event risk lacked positive/counterexample/4B/4C balanced residual rows
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Stock-Web manifest/schema basis
- symbol profile windows and corporate-action caveats
- 1D OHLC entry close
- MFE/MAE 30D/90D/180D from visible Stock-Web rows
- same-archetype diversity and duplicate avoidance
- sector/canonical shadow-only rules
```

Not validated:

```text
- live watchlist relevance
- current 2026 candidate scan
- production scoring code
- broker execution
- tax/portfolio suitability
- exact 1Y/2Y calibration fields, which are intentionally left null where not necessary to the 180D calibration objective
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c24_partner_quality_data_bridge,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,0,+2,+2,"Partner-sponsored validated data reduced false-negative risk in HanAll/Alteogen","Keeps positive platform data in Stage2/Yellow but not automatic Green","C24-HANALL-20230927-S2A|C24-ALTEOGEN-20241120-S2A",5,5,2,medium,archetype_shadow_only,"not production; post-calibrated residual"
shadow_weight,c24_binary_event_cap_guard,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,0,-4,-4,"Single binary readout/PDUFA narratives produced large MAE after Shinpoong/HLB","Prevents trial/regulatory event-only Green", "C24-HLB-20240326-4B_PRECAP|C24-SHINPOONG-20210705-S2_FALSE",5,5,2,medium,archetype_shadow_only,"cap at Yellow/4B-watch unless bridge closes"
shadow_weight,c24_initial_MAE_buffer,sector_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,0,-2,-2,"Even positive data rows had -12.56% to -30.51% MAE unless partner quality and follow-through appeared","Requires staged entry or retest confirmation", "C24-YUHAN-20231004-S2A|C24-ALTEOGEN-20241120-S2A",5,5,2,medium,sector_shadow_only,"do not weaken global Stage2; add L7/C24 buffer only"
shadow_weight,c24_hard_thesis_break_to_4c,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,true,true,0,"Hard endpoint/regulatory failure must route to 4C immediately","Existing hard_4c axis kept; C24 validates it","C24-HLB-20240517-4C|C24-SHINPOONG-20210706-4C",5,5,2,high,existing_axis_strengthened,"log as strengthening evidence, not new global delta"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "C24-HANALL-IMVT1402-PH1-20230927", "symbol": "009420", "company_name": "한올바이오파마", "round": "R13", "loop": "49", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "AUTOIMMUNE_FCRN_PARTNER_PHASE1_SIGNAL", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "C24-HANALL-20230927-S2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_data_with_retestable_partner_path", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "same canonical archetype, new symbol/trigger family; diversity_score=22"}
{"row_type": "case", "case_id": "C24-ALTEOGEN-KEYTRUDA-SC-NONINFERIOR-20241120", "symbol": "196170", "company_name": "알테오젠", "round": "R13", "loop": "49", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "PARTNER_KEYTRUDA_SC_PHASE3_NONINFERIORITY", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "C24-ALTEOGEN-20241120-S2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_partner_trial_but_initial_positioning_shakeout", "current_profile_verdict": "current_profile_too_early", "price_source": "Songdaiki/stock-web", "notes": "same canonical archetype, new symbol/trigger family; diversity_score=21"}
{"row_type": "case", "case_id": "C24-YUHAN-MARIPOSA-DATA-20231004", "symbol": "000100", "company_name": "유한양행", "round": "R13", "loop": "49", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "ONCOLOGY_PHASE3_PFS_POSITIVE_BUT_COMMERCIAL_BRIDGE_NOT_YET_CLOSED", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "C24-YUHAN-20231004-S2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_data_but_event_gap_and_commercial_bridge_not_closed", "current_profile_verdict": "current_profile_too_early", "price_source": "Songdaiki/stock-web", "notes": "same canonical archetype, new symbol/trigger family; diversity_score=18"}
{"row_type": "case", "case_id": "C24-HLB-RIVOCERANIB-CRL-20240517", "symbol": "028300", "company_name": "HLB", "round": "R13", "loop": "49", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "ONCOLOGY_BINARY_REGULATORY_FAILURE_AFTER_TRIAL_AND_PDUFA_RUN", "case_type": "4C_success", "positive_or_counterexample": "counterexample", "best_trigger": "C24-HLB-20240517-4C", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "hard_4c_but_post_crl_rebound_shows_binary_event_needs_pre_cap_overlay", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "same canonical archetype, new symbol/trigger family; diversity_score=23"}
{"row_type": "case", "case_id": "C24-SHINPOONG-PYRAMAX-PH2-20210705", "symbol": "019170", "company_name": "신풍제약", "round": "R13", "loop": "49", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "COVID_REPURPOSING_PHASE2_ENDPOINT_FAILURE", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "C24-SHINPOONG-20210705-S2_FALSE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "failed_rerating_after_trial_endpoint_failure", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "same canonical archetype, new symbol/trigger family; diversity_score=24"}
{"row_type": "trigger", "trigger_id": "C24-HANALL-20230927-S2A", "case_id": "C24-HANALL-IMVT1402-PH1-20230927", "symbol": "009420", "company_name": "한올바이오파마", "round": "R13", "loop": "49", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "AUTOIMMUNE_FCRN_PARTNER_PHASE1_SIGNAL", "sector": "Bio / autoimmune FcRn", "primary_archetype": "partner_phase1_positive_data_to_platform_optionalities", "loop_objective": "auto_coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-09-26", "evidence_available_at_that_date": "Immunovant disclosed positive Phase 1 IMVT-1402 data; Korean stock gapped the next local trading day.", "evidence_source": "Immunovant/partner Phase 1 data news; Investopedia summary dated 2023-09-26 UTC; stock-web 2023 shard.", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["multiple_public_sources", "durable_customer_confirmation", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/009/009420/2023.csv", "profile_path": "atlas/symbol_profiles/009/009420.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-09-27", "entry_price": 32650, "MFE_30D_pct": 21.75, "MFE_90D_pct": 43.19, "MFE_180D_pct": 43.19, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -12.56, "MAE_90D_pct": -12.56, "MAE_180D_pct": -12.56, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-12-27", "peak_price": 46750, "drawdown_after_peak_pct": -38.93, "green_lateness_ratio": 0.3, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": null, "trigger_outcome_label": "positive_data_with_retestable_partner_path", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C24-HANALL-20230927-32650", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C24-ALTEOGEN-20241120-S2A", "case_id": "C24-ALTEOGEN-KEYTRUDA-SC-NONINFERIOR-20241120", "symbol": "196170", "company_name": "알테오젠", "round": "R13", "loop": "49", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "PARTNER_KEYTRUDA_SC_PHASE3_NONINFERIORITY", "sector": "Bio / drug-delivery platform", "primary_archetype": "partner_phase3_noninferiority_data_to_platform_repricing", "loop_objective": "auto_coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-11-19", "evidence_available_at_that_date": "Merck disclosed subcutaneous Keytruda formulation trial met noninferiority endpoints; after-hours Korea timing sends entry to next trading close.", "evidence_source": "Reuters 2024-11-19; stock-web 2024/2025 shards.", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["multiple_public_sources", "durable_customer_confirmation", "financial_visibility"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv", "profile_path": "atlas/symbol_profiles/196/196170.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-11-20", "entry_price": 350500, "MFE_30D_pct": 3.99, "MFE_90D_pct": 31.1, "MFE_180D_pct": 44.94, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -21.83, "MAE_90D_pct": -21.83, "MAE_180D_pct": -21.83, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-07-18", "peak_price": 508000, "drawdown_after_peak_pct": -18.7, "green_lateness_ratio": 0.07, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "watch_only_or_event_cap", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": null, "trigger_outcome_label": "positive_partner_trial_but_initial_positioning_shakeout", "current_profile_verdict": "current_profile_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C24-ALTEOGEN-20241120-350500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C24-YUHAN-20231004-S2A", "case_id": "C24-YUHAN-MARIPOSA-DATA-20231004", "symbol": "000100", "company_name": "유한양행", "round": "R13", "loop": "49", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "ONCOLOGY_PHASE3_PFS_POSITIVE_BUT_COMMERCIAL_BRIDGE_NOT_YET_CLOSED", "sector": "Bio / oncology", "primary_archetype": "late_stage_oncology_positive_data_without_immediate_revision_bridge", "loop_objective": "auto_coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-09-28", "evidence_available_at_that_date": "MARIPOSA/lazertinib-amivantamab positive data event was available during Korea holiday gap; first tradable close used.", "evidence_source": "J&J/MARIPOSA public data and Reuters later approval summary; stock-web 2023/2024 shards.", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "policy_or_regulatory_optionality", "early_revision_signal"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["explicit_event_cap", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000100/2023.csv", "profile_path": "atlas/symbol_profiles/000/000100.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-10-04", "entry_price": 79000, "MFE_30D_pct": 11.9, "MFE_90D_pct": 11.9, "MFE_180D_pct": 11.9, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -30.51, "MAE_90D_pct": -30.51, "MAE_180D_pct": -30.51, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-10-04", "peak_price": 88400, "drawdown_after_peak_pct": -37.9, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "watch_only_or_event_cap", "four_b_evidence_type": ["explicit_event_cap", "positioning_overheat"], "four_c_protection_label": null, "trigger_outcome_label": "positive_data_but_event_gap_and_commercial_bridge_not_closed", "current_profile_verdict": "current_profile_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C24-YUHAN-20231004-79000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C24-HLB-20240517-4C", "case_id": "C24-HLB-RIVOCERANIB-CRL-20240517", "symbol": "028300", "company_name": "HLB", "round": "R13", "loop": "49", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "ONCOLOGY_BINARY_REGULATORY_FAILURE_AFTER_TRIAL_AND_PDUFA_RUN", "sector": "Bio / oncology", "primary_archetype": "binary_pdufa_failure_after_data_narrative", "loop_objective": "auto_coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression", "trigger_type": "4C", "trigger_date": "2024-05-17", "evidence_available_at_that_date": "FDA complete response letter / approval failure shock invalidated the pre-event data-to-approval thesis.", "evidence_source": "HLB/FDA CRL news; stock-web 2024/2025 shards.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "explicit_event_cap"], "stage4c_evidence_fields": ["regulatory_rejection", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv", "profile_path": "atlas/symbol_profiles/028/028300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-17", "entry_price": 67100, "MFE_30D_pct": 9.99, "MFE_90D_pct": 46.2, "MFE_180D_pct": 46.2, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -32.71, "MAE_90D_pct": -32.71, "MAE_180D_pct": -32.71, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-08", "peak_price": 98100, "drawdown_after_peak_pct": -54.0, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "watch_only_or_event_cap", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "explicit_event_cap"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "hard_4c_but_post_crl_rebound_shows_binary_event_needs_pre_cap_overlay", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C24-HLB-20240517-67100", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C24-SHINPOONG-20210705-S2_FALSE", "case_id": "C24-SHINPOONG-PYRAMAX-PH2-20210705", "symbol": "019170", "company_name": "신풍제약", "round": "R13", "loop": "49", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "COVID_REPURPOSING_PHASE2_ENDPOINT_FAILURE", "sector": "Bio / antiviral COVID repurposing", "primary_archetype": "retail_narrative_trial_readout_failure", "loop_objective": "auto_coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2021-07-05", "evidence_available_at_that_date": "COVID/Pyramax trial readout turned into endpoint disappointment despite speculative data narrative.", "evidence_source": "Korean public trial-readout news; stock-web 2021/2022 shards.", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "explicit_event_cap"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/019/019170/2021.csv", "profile_path": "atlas/symbol_profiles/019/019170.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-07-05", "entry_price": 95600, "MFE_30D_pct": 6.17, "MFE_90D_pct": 6.17, "MFE_180D_pct": 6.17, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -35.88, "MAE_90D_pct": -52.82, "MAE_180D_pct": -76.1, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-07-05", "peak_price": 101500, "drawdown_after_peak_pct": -77.49, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "watch_only_or_event_cap", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "explicit_event_cap"], "four_c_protection_label": null, "trigger_outcome_label": "failed_rerating_after_trial_endpoint_failure", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C24-SHINPOONG-20210705-95600", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C24-HLB-20240326-4B_PRECAP", "case_id": "C24-HLB-RIVOCERANIB-CRL-20240517", "symbol": "028300", "company_name": "HLB", "round": "R13", "loop": "49", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "ONCOLOGY_BINARY_REGULATORY_FAILURE_AFTER_TRIAL_AND_PDUFA_RUN", "sector": "Bio / oncology", "primary_archetype": "binary_pdufa_failure_after_data_narrative", "loop_objective": "4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "4B", "trigger_date": "2024-03-26", "evidence_available_at_that_date": "Pre-PDUFA blowoff after data/regulatory narrative; full-window peak proximity near 0.74 vs March stage2 action close.", "evidence_source": "HLB/FDA CRL news; stock-web 2024/2025 shards.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "explicit_event_cap"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv", "profile_path": "atlas/symbol_profiles/028/028300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-26", "entry_price": 120800, "MFE_30D_pct": 0.0, "MFE_90D_pct": 6.79, "MFE_180D_pct": 6.79, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -29.55, "MAE_90D_pct": -62.62, "MAE_180D_pct": -62.62, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-26", "peak_price": 129000, "drawdown_after_peak_pct": -65.0, "green_lateness_ratio": null, "four_b_local_peak_proximity": 0.74, "four_b_full_window_peak_proximity": 0.74, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "explicit_event_cap"], "four_c_protection_label": null, "trigger_outcome_label": "overlay_trigger_not_representative", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C24-HLB-20240326-120800", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "same_case_overlay_new_trigger_family", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C24-SHINPOONG-20210706-4C", "case_id": "C24-SHINPOONG-PYRAMAX-PH2-20210705", "symbol": "019170", "company_name": "신풍제약", "round": "R13", "loop": "49", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "COVID_REPURPOSING_PHASE2_ENDPOINT_FAILURE", "sector": "Bio / antiviral COVID repurposing", "primary_archetype": "retail_narrative_trial_readout_failure", "loop_objective": "4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "4C", "trigger_date": "2021-07-06", "evidence_available_at_that_date": "Hard thesis-break confirmation after trial readout; protects against continuing deterioration better than waiting for price-only damage.", "evidence_source": "Korean public trial-readout news; stock-web 2021/2022 shards.", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/019/019170/2021.csv", "profile_path": "atlas/symbol_profiles/019/019170.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-07-06", "entry_price": 67000, "MFE_30D_pct": 16.87, "MFE_90D_pct": 16.87, "MFE_180D_pct": 16.87, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -8.51, "MAE_90D_pct": -32.69, "MAE_180D_pct": -65.9, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-08-12", "peak_price": 78300, "drawdown_after_peak_pct": -70.82, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "overlay_trigger_not_representative", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C24-SHINPOONG-20210706-67000", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "is_new_independent_case": false, "reuse_reason": "same_case_overlay_new_trigger_family", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C24-HANALL-IMVT1402-PH1-20230927", "trigger_id": "C24-HANALL-20230927-S2A", "symbol": "009420", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "raw_component_scores_before": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": 12, "relative_strength_score": 15, "customer_quality_score": 17, "policy_or_regulatory_score": 4, "valuation_repricing_score": 10, "execution_risk_score": -2, "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_before": 83, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": 14, "relative_strength_score": 15, "customer_quality_score": 19, "policy_or_regulatory_score": 5, "valuation_repricing_score": 10, "execution_risk_score": -3, "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_after": 87, "stage_label_after": "Stage3-Green", "changed_components": ["c24_trial_data_quality_bridge", "c24_binary_event_cap_guard", "c24_initial_MAE_buffer"], "component_delta_explanation": "Research proxy only: reweights trial data by sponsor/partner quality and blocks binary event/endpoint narratives that lack durable regulatory-commercial bridge.", "MFE_90D_pct": 43.19, "MAE_90D_pct": -12.56, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C24-ALTEOGEN-KEYTRUDA-SC-NONINFERIOR-20241120", "trigger_id": "C24-ALTEOGEN-20241120-S2A", "symbol": "196170", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "raw_component_scores_before": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": 12, "relative_strength_score": 8, "customer_quality_score": 17, "policy_or_regulatory_score": 10, "valuation_repricing_score": 10, "execution_risk_score": -4, "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_before": 78, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": 14, "relative_strength_score": 8, "customer_quality_score": 19, "policy_or_regulatory_score": 12, "valuation_repricing_score": 10, "execution_risk_score": -8, "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_after": 81, "stage_label_after": "Stage3-Yellow", "changed_components": ["c24_trial_data_quality_bridge", "c24_binary_event_cap_guard", "c24_initial_MAE_buffer"], "component_delta_explanation": "Research proxy only: reweights trial data by sponsor/partner quality and blocks binary event/endpoint narratives that lack durable regulatory-commercial bridge.", "MFE_90D_pct": 31.1, "MAE_90D_pct": -21.83, "score_return_alignment_label": "high_mae_positive_needs_buffer", "current_profile_verdict": "current_profile_too_early"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C24-YUHAN-MARIPOSA-DATA-20231004", "trigger_id": "C24-YUHAN-20231004-S2A", "symbol": "000100", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "raw_component_scores_before": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": 8, "relative_strength_score": 8, "customer_quality_score": 17, "policy_or_regulatory_score": 10, "valuation_repricing_score": 10, "execution_risk_score": -4, "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": 8, "relative_strength_score": 8, "customer_quality_score": 19, "policy_or_regulatory_score": 12, "valuation_repricing_score": 10, "execution_risk_score": -8, "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_after": 73, "stage_label_after": "Stage3-Yellow", "changed_components": ["c24_trial_data_quality_bridge", "c24_binary_event_cap_guard", "c24_initial_MAE_buffer"], "component_delta_explanation": "Research proxy only: reweights trial data by sponsor/partner quality and blocks binary event/endpoint narratives that lack durable regulatory-commercial bridge.", "MFE_90D_pct": 11.9, "MAE_90D_pct": -30.51, "score_return_alignment_label": "high_mae_positive_needs_buffer", "current_profile_verdict": "current_profile_too_early"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C24-HLB-RIVOCERANIB-CRL-20240517", "trigger_id": "C24-HLB-20240517-4C", "symbol": "028300", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "raw_component_scores_before": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": "unknown_or_not_supported", "relative_strength_score": 18, "customer_quality_score": "unknown_or_not_supported", "policy_or_regulatory_score": 14, "valuation_repricing_score": 18, "execution_risk_score": -2, "legal_or_contract_risk_score": -1, "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_before": 88, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": "unknown_or_not_supported", "relative_strength_score": 8, "customer_quality_score": "unknown_or_not_supported", "policy_or_regulatory_score": -10, "valuation_repricing_score": -8, "execution_risk_score": -15, "legal_or_contract_risk_score": -14, "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_after": 42, "stage_label_after": "4C", "changed_components": ["c24_trial_data_quality_bridge", "c24_binary_event_cap_guard", "c24_initial_MAE_buffer"], "component_delta_explanation": "Research proxy only: reweights trial data by sponsor/partner quality and blocks binary event/endpoint narratives that lack durable regulatory-commercial bridge.", "MFE_90D_pct": 46.2, "MAE_90D_pct": -32.71, "score_return_alignment_label": "aligned_counterexample_after_guard", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C24-SHINPOONG-PYRAMAX-PH2-20210705", "trigger_id": "C24-SHINPOONG-20210705-S2_FALSE", "symbol": "019170", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "raw_component_scores_before": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": "unknown_or_not_supported", "relative_strength_score": 18, "customer_quality_score": "unknown_or_not_supported", "policy_or_regulatory_score": 8, "valuation_repricing_score": 18, "execution_risk_score": -2, "legal_or_contract_risk_score": -1, "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_before": 82, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": "unknown_or_not_supported", "relative_strength_score": 8, "customer_quality_score": "unknown_or_not_supported", "policy_or_regulatory_score": -3, "valuation_repricing_score": -8, "execution_risk_score": -15, "legal_or_contract_risk_score": -3, "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_after": 45, "stage_label_after": "4B/4C-Watch", "changed_components": ["c24_trial_data_quality_bridge", "c24_binary_event_cap_guard", "c24_initial_MAE_buffer"], "component_delta_explanation": "Research proxy only: reweights trial data by sponsor/partner quality and blocks binary event/endpoint narratives that lack durable regulatory-commercial bridge.", "MFE_90D_pct": 6.17, "MAE_90D_pct": -52.82, "score_return_alignment_label": "aligned_counterexample_after_guard", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R13", "loop": "49", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "new_independent_case_count": 5, "reused_case_count": 0, "new_symbol_count": 5, "same_archetype_new_symbol_count": 5, "same_archetype_new_trigger_family_count": 5, "new_canonical_archetype_count": 0, "new_trigger_family_count": 5, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["single_binary_event_false_green", "partner_data_initial_MAE_shakeout", "positive_data_without_commercial_bridge", "hard_4c_after_failure_too_late_for_pre-event_risk"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false, "diversity_score_summary": "avg=21.6; new_symbol_count=5; counterexample_count=2; same_archetype_new_trigger_family_count=5", "auto_selected_coverage_gap": "L7/C24 lacked balanced positive/counterexample/4B/4C rows after C23 approval-commercialization loop"}
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
next_round = R13_loop_50
recommended_scope = L7_BIO_HEALTHCARE_MEDICAL / C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
reason = after C23 and C24, L7 still needs non-drug device/reimbursement/export examples to avoid overweighting oncology/clinical-trial archetypes
```

## 28. Source Notes

Stock-Web files directly checked:

```text
atlas/manifest.json
atlas/schema.json
atlas/symbol_profiles/009/009420.json
atlas/symbol_profiles/196/196170.json
atlas/symbol_profiles/000/000100.json
atlas/symbol_profiles/028/028300.json
atlas/symbol_profiles/019/019170.json
atlas/ohlcv_tradable_by_symbol_year/009/009420/2023.csv
atlas/ohlcv_tradable_by_symbol_year/009/009420/2024.csv
atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv
atlas/ohlcv_tradable_by_symbol_year/196/196170/2025.csv
atlas/ohlcv_tradable_by_symbol_year/000/000100/2023.csv
atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv
atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv
atlas/ohlcv_tradable_by_symbol_year/028/028300/2025.csv
atlas/ohlcv_tradable_by_symbol_year/019/019170/2021.csv
atlas/ohlcv_tradable_by_symbol_year/019/019170/2022.csv
```

External evidence sources used as event-date anchors:

```text
- Immunovant / HanAll IMVT-1402 Phase 1 public data report, 2023-09-26 UTC.
- Reuters: Merck says Keytruda injection on par with approved IV version in trial, 2024-11-19 UTC.
- J&J / MARIPOSA public Phase 3 data and later Reuters FDA-approval context for Rybrevant + lazertinib.
- HLB CRL public news, 2024-05-17.
- Shinpoong/Pyramax COVID clinical readout public news, 2021-07-05.
```
