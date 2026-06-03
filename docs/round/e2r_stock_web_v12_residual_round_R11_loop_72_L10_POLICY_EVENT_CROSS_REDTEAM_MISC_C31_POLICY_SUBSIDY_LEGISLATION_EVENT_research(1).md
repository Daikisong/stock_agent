# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
repo_session: later_batch_implementation_only
output_file: e2r_stock_web_v12_residual_round_R11_loop_72_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
scheduled_round: R11
scheduled_loop: 72
completed_round: R11
completed_loop: 72
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: NUCLEAR_EXPORT_POLICY_OPTIONALITY_AND_POLICY_THEME_GUARD
loop_objective:
  - residual_false_positive_mining
  - residual_missed_structural_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - sector_specific_rule_discovery
  - canonical_archetype_compression
  - counterexample_mining
  - coverage_gap_fill
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_agent_live_scan_allowed: false
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
round_schedule_status: valid
round_sector_consistency: pass
```

This loop adds 4 new independent cases, 2 counterexamples, and 2 residual errors for R11/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C31_POLICY_SUBSIDY_LEGISLATION_EVENT.

## 1. Current Calibrated Profile Assumption

The current default proxy is `e2r_2_1_stock_web_calibrated_proxy`; the rollback reference is `e2r_2_0_baseline_reference`.

Assumed already-applied global axes:

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

This MD does **not** re-propose those axes globally. It stress-tests them inside the policy-event archetype and proposes only shadow sector/canonical rules for C31.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R11 |
| scheduled_loop | 72 |
| allowed R11 sector choice | L10_POLICY_EVENT_CROSS_REDTEAM_MISC or L1 when defense-policy-linked |
| selected large_sector_id | L10_POLICY_EVENT_CROSS_REDTEAM_MISC |
| selected canonical_archetype_id | C31_POLICY_SUBSIDY_LEGISLATION_EVENT |
| fine_archetype_id | NUCLEAR_EXPORT_POLICY_OPTIONALITY_AND_POLICY_THEME_GUARD |
| scope logic | policy event + subsidy/tender/legal optionality; separates policy-only theme spikes from policy + contract/IP/legal de-risking |

R11 is not used here as a normal nuclear, EPC, grid, or construction sector round. The object is the **policy-event mechanism itself**: an official policy/tender/legal event is the spark, but only events with contract path, customer identity, settlement/de-risking, or commercialization bridge should promote beyond Stage2-Actionable.

## 3. Previous Coverage / Duplicate Avoidance Check

GitHub search over the allowed artifact domain found no direct prior R11/C31 v12 residual file using `C31_POLICY_SUBSIDY_LEGISLATION_EVENT`. This run therefore treats the selected C31 set as a coverage fill rather than schema rematerialization.

Duplicate-avoidance rule applied:

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

Selected rows are all new independent C31 policy-event examples in this loop.

| case_id | symbol | trigger_family | entry_date | duplicate_status |
|---|---:|---|---|---|
| C31_034020_2025_WESTINGHOUSE_REENTRY | 034020 | nuclear_export_legal_ip_settlement | 2025-01-17 | new independent |
| C31_052690_2025_WESTINGHOUSE_REENTRY | 052690 | nuclear_export_legal_ip_settlement | 2025-01-17 | new independent |
| C31_006910_2022_YOON_NUCLEAR_POLICY_THEME | 006910 | election_policy_theme | 2022-03-10 | new independent |
| C31_013990_2024_LOW_BIRTH_POLICY_THEME | 013990 | demographic_policy_theme | 2024-01-03 | new independent |

## 4. Stock-Web OHLC Input / Price Source Validation

`Songdaiki/stock-web` manifest validation:

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
markets = KONEX | KOSDAQ | KOSDAQ GLOBAL | KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

Schema validation:

```text
tradable_shard_columns = d,o,h,l,c,v,a,mc,s,m
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
calibration_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
```

## 5. Historical Eligibility Gate

All representative triggers are historical, have the entry row in the stock-web tradable shard, have at least 180 forward trading days available by the manifest max date, and have no corporate-action candidate within the entry~D+180 windows.

| case_id | symbol | profile path | entry_date | 180D forward window | corporate action overlap | calibration_usable |
|---|---:|---|---|---:|---|---|
| C31_034020_2025_WESTINGHOUSE_REENTRY | 034020 | atlas/symbol_profiles/034/034020.json | 2025-01-17 | 180 | none | true |
| C31_052690_2025_WESTINGHOUSE_REENTRY | 052690 | atlas/symbol_profiles/052/052690.json | 2025-01-17 | 180 | none | true |
| C31_006910_2022_YOON_NUCLEAR_POLICY_THEME | 006910 | atlas/symbol_profiles/006/006910.json | 2022-03-10 | 180 | none | true |
| C31_013990_2024_LOW_BIRTH_POLICY_THEME | 013990 | atlas/symbol_profiles/013/013990.json | 2024-01-03 | 180 | none | true |

Profile caveat summary:

```text
034020 corporate_action_candidate_dates = 2019-05-29, 2020-02-18, 2020-12-24; no 2025 overlap.
052690 corporate_action_candidate_count = 0.
006910 corporate_action_candidate_dates end at 2016-08-29; no 2022 overlap.
013990 corporate_action_candidate_dates = 2008-05-16; no 2024 overlap.
```

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | included symbols | compression note |
|---|---|---|---|
| NUCLEAR_EXPORT_POLICY_OPTIONALITY_AND_POLICY_THEME_GUARD | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 034020, 052690, 006910 | compresses policy-election/tender/settlement events into one C31 policy-event scoring channel |
| DEMOGRAPHIC_POLICY_THEME_GUARD | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 013990 | non-nuclear policy theme used as counterexample holdout |

The C31 rule is not a nuclear-sector rule. It is a **policy-event evidence-quality rule**. Nuclear export cases are included because the event path is clean enough to expose the difference between policy headline and legal/contract de-risking.

## 7. Case Selection Summary

| case_id | symbol | company_name | case_type | positive_or_counterexample | trigger_type | trigger_date | entry_date | entry_price |
|---|---:|---|---|---|---|---|---|---:|
| C31_034020_2025_WESTINGHOUSE_REENTRY | 034020 | 두산에너빌리티 | structural_success | positive | Stage2-Actionable | 2025-01-17 | 2025-01-17 | 21750 |
| C31_052690_2025_WESTINGHOUSE_REENTRY | 052690 | 한전기술 | high_mae_success | positive | Stage2-Actionable | 2025-01-17 | 2025-01-17 | 64500 |
| C31_006910_2022_YOON_NUCLEAR_POLICY_THEME | 006910 | 보성파워텍 | failed_rerating | counterexample | Stage2-Actionable | 2022-03-10 | 2022-03-10 | 6840 |
| C31_013990_2024_LOW_BIRTH_POLICY_THEME | 013990 | 아가방컴퍼니 | failed_rerating | counterexample | Stage2-Actionable | 2024-01-03 | 2024-01-03 | 5630 |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 4
4C_case_count = 2
calibration_usable_case_count = 4
minimum_positive_case_count = pass
minimum_counterexample_count = pass
minimum_calibration_usable_case_count = pass
```

Mechanism summary:

- Positive cases have policy-event evidence **plus** export/legal/customer path: Westinghouse settlement removed a nuclear export overhang and translated policy optionality into a more investable contract path.
- Counterexamples have policy-event evidence but lack company-level contract, margin bridge, or durable customer confirmation. The price candle runs first, then the thesis evaporates like steam without a turbine.

## 9. Evidence Source Map

| trigger_id | evidence_available_at_that_date | evidence source | stage evidence classification |
|---|---|---|---|
| TR_C31_034020_20250117_STAGE2A | KHNP/KEPCO and Westinghouse agreed to end the nuclear IP dispute and cooperate in global nuclear power markets. | Reuters, 2025-01-17, “South Korean nuclear power plant operator agrees with US Westinghouse to end dispute” | Stage2: public_event_or_disclosure, policy_or_regulatory_optionality, customer_or_order_quality; Stage3 later requires confirmation |
| TR_C31_052690_20250117_STAGE2A | Same settlement improved the exportability of Korean reactor technology, directly relevant to engineering/design entities. | Reuters, 2025-01-17 | Stage2: legal/regulatory de-risking + customer route; Stage3 later requires order/earnings conversion |
| TR_C31_006910_20220310_STAGE2A | The 2022 presidential election created a pro-nuclear policy regime expectation. | Reuters/background election-policy coverage; public election result 2022-03-10 | Stage2: policy optionality and relative strength only; no contract/customer/margin bridge |
| TR_C31_013990_20240103_STAGE2A | Low-birth policy theme repricing; national policy context later confirmed broader family-support and employer-childcare policy push. | Reuters fertility-policy coverage; policy-theme price row | Stage2: policy theme only; no company-specific conversion evidence |

## 10. Price Data Source Map

| symbol | company_name | tradable shard(s) used | profile path | price basis | stock_web_manifest_max_date |
|---:|---|---|---|---|---|
| 034020 | 두산에너빌리티 | atlas/ohlcv_tradable_by_symbol_year/034/034020/2025.csv | atlas/symbol_profiles/034/034020.json | tradable_raw | 2026-02-20 |
| 052690 | 한전기술 | atlas/ohlcv_tradable_by_symbol_year/052/052690/2025.csv | atlas/symbol_profiles/052/052690.json | tradable_raw | 2026-02-20 |
| 006910 | 보성파워텍 | atlas/ohlcv_tradable_by_symbol_year/006/006910/2022.csv | atlas/symbol_profiles/006/006910.json | tradable_raw | 2026-02-20 |
| 013990 | 아가방컴퍼니 | atlas/ohlcv_tradable_by_symbol_year/013/013990/2024.csv | atlas/symbol_profiles/013/013990.json | tradable_raw | 2026-02-20 |

## 11. Case-by-Case Trigger Grid

| case_id | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence | current profile verdict |
|---|---|---|---|---|---|
| C31_034020_2025_WESTINGHOUSE_REENTRY | legal/IP settlement; export cooperation; nuclear export policy | later price/volume confirmation and export narrative conversion; revision proxy not directly validated here | valuation/positioning overheat near Oct 2025 | none inside 180D | current_profile_correct |
| C31_052690_2025_WESTINGHOUSE_REENTRY | legal/IP settlement; engineering relevance to reactor export | later strong momentum; still high MAE before full rerating | valuation/positioning overheat after June 2025 spike | none inside 180D | current_profile_too_late |
| C31_006910_2022_YOON_NUCLEAR_POLICY_THEME | election-driven pro-nuclear policy theme; relative strength | no durable order/revision/margin bridge | price-only local peak; no full 4B unless non-price evidence added | thesis_break_watch_only after collapse below policy-spike base | current_profile_false_positive |
| C31_013990_2024_LOW_BIRTH_POLICY_THEME | demographic-policy headline; theme liquidity | no company-specific conversion | price-only local peak; theme overheat | thesis_break_watch_only after 180D drawdown | current_profile_false_positive |

## 12. Trigger-Level OHLC Backtest Tables

All returns use stock-web raw/unadjusted tradable OHLC, entry at `c` on `entry_date`, and high/low windows from entry through N tradable rows.

| trigger_id | symbol | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct | calibration_usable |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---|
| TR_C31_034020_20250117_STAGE2A | 034020 | 2025-01-17 | 21750 | 42.07 | -2.76 | 99.77 | -8.23 | 289.43 | -8.23 | 2025-10-16 | 84700 | -5.79 | true |
| TR_C31_052690_20250117_STAGE2A | 052690 | 2025-01-17 | 64500 | 17.67 | -1.86 | 17.67 | -22.79 | 88.68 | -22.79 | 2025-06-25 | 121700 | -31.72 | true |
| TR_C31_006910_20220310_STAGE2A | 006910 | 2022-03-10 | 6840 | 32.31 | -6.87 | 32.31 | -26.75 | 32.31 | -44.81 | 2022-03-25 | 9050 | -58.29 | true |
| TR_C31_013990_20240103_STAGE2A | 013990 | 2024-01-03 | 5630 | 27.53 | -10.48 | 27.53 | -20.52 | 27.53 | -29.93 | 2024-01-18 | 7180 | -45.06 | true |

Interpretation:

- C31 can produce excellent upside when policy optionality is paired with contract/legal de-risking (`034020`, `052690`).
- C31 can also generate seductive but fragile spikes when the only evidence is a policy theme (`006910`, `013990`). These are the dangerous mirages: the candle shines, but there is no cash-flow road underneath.

## 13. Current Calibrated Profile Stress Test

| case_id | current profile expected decision | actual MFE/MAE alignment | verdict | residual error |
|---|---|---|---|---|
| C31_034020_2025_WESTINGHOUSE_REENTRY | Stage2-Actionable accepted; Green waits for later confirmation | very strong 180D MFE with shallow early MAE | current_profile_correct | none; confirms C31 de-risked policy event can be actionable |
| C31_052690_2025_WESTINGHOUSE_REENTRY | Stage2 allowed, Green likely delayed by revision/margin proof | 180D MFE strong, but 90D MAE severe | current_profile_too_late | delayed structural recognition after legal-risk removal |
| C31_006910_2022_YOON_NUCLEAR_POLICY_THEME | if policy event is over-weighted, may pass Stage2 too easily | large initial MFE but severe 180D drawdown | current_profile_false_positive | policy-only theme over-scoring |
| C31_013990_2024_LOW_BIRTH_POLICY_THEME | if demographic policy theme is over-weighted, may pass Stage2 too easily | initial theme spike fades into deep drawdown | current_profile_false_positive | policy-only theme over-scoring |

Applied-axis stress test:

| applied axis | C31 finding | status |
|---|---|---|
| stage2_actionable_evidence_bonus | helpful only when policy event has legal/contract/customer de-risking; dangerous for policy-only themes | existing_axis_kept with C31 guard |
| stage3_yellow_total_min | adequate; C31 Yellow should not be reached from policy headline alone | existing_axis_strengthened for C31 |
| stage3_green_total_min / revision_min | appropriate for policy-only themes; can be too slow for legal settlement re-entry | existing_axis_kept with C31 settlement exception |
| price_only_blowoff_blocks_positive_stage | strongly supported by 006910 and 013990 | existing_axis_strengthened |
| full_4b_requires_non_price_evidence | supported: price peak alone catches local peaks but cannot explain durable risk | existing_axis_strengthened |
| hard_4c_thesis_break_routes_to_4c | supported for policy-only collapse after the theme loses sponsorship | existing_axis_strengthened |

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 entry | Stage2 price | Stage3 Green proxy date | Stage3 Green proxy price | peak used | green_lateness_ratio | interpretation |
|---|---|---:|---|---:|---:|---:|---|
| C31_034020_2025_WESTINGHOUSE_REENTRY | 2025-01-17 | 21750 | 2025-06-12 | 54600 | 84700 | 0.52 | Green captures only mid-cycle; Stage2 settlement signal mattered |
| C31_052690_2025_WESTINGHOUSE_REENTRY | 2025-01-17 | 64500 | 2025-06-13 | 104100 | 121700 | 0.69 | Green is late; most of the re-rating already occurred |
| C31_006910_2022_YOON_NUCLEAR_POLICY_THEME | 2022-03-10 | 6840 | n/a | n/a | 9050 | n/a | no confirmed Stage3 Green trigger |
| C31_013990_2024_LOW_BIRTH_POLICY_THEME | 2024-01-03 | 5630 | n/a | n/a | 7180 | n/a | no confirmed Stage3 Green trigger |

C31-specific lesson: a legal/IP/tender de-risking event can be a valid Stage2-Actionable entry before revisions. A policy-only headline should remain Stage2-watch or theme-risk, not Yellow/Green.

## 15. 4B Local vs Full-window Timing Audit

| case_id | Stage2 price | Stage4B proxy date | Stage4B proxy price | local_peak_price | full_window_peak_price | four_b_local_peak_proximity | four_b_full_window_peak_proximity | evidence type | verdict |
|---|---:|---|---:|---:|---:|---:|---:|---|---|
| C31_034020_2025_WESTINGHOUSE_REENTRY | 21750 | 2025-10-16 | 83700 | 84700 | 84700 | 0.98 | 0.98 | valuation_blowoff, positioning_overheat | good_full_window_4B_timing |
| C31_052690_2025_WESTINGHOUSE_REENTRY | 64500 | 2025-06-25 | 114900 | 121700 | 121700 | 0.88 | 0.88 | valuation_blowoff, positioning_overheat | good_full_window_4B_timing |
| C31_006910_2022_YOON_NUCLEAR_POLICY_THEME | 6840 | 2022-03-25 | 8370 | 9050 | 9050 | 0.69 | 0.69 | price_only | do_not_treat_as_full_4B_without_non_price_evidence |
| C31_013990_2024_LOW_BIRTH_POLICY_THEME | 5630 | 2024-01-18 | 6140 | 7180 | 7180 | 0.33 | 0.33 | price_only | price_only_local_4B_weak |

For C31, price-only 4B is useful as a dashboard warning, but not as a full thesis overlay unless the event also introduces legal/contract/regulatory slowdown, explicit cap, dilution, or backlog/margin deterioration.

## 16. 4C Protection Audit

| case_id | 4C proxy label | 4C proxy date | protection label | notes |
|---|---|---|---|---|
| C31_034020_2025_WESTINGHOUSE_REENTRY | none | n/a | thesis_break_watch_only | no 180D hard thesis break; use 4B overheat, not 4C |
| C31_052690_2025_WESTINGHOUSE_REENTRY | none | n/a | thesis_break_watch_only | post-peak drawdown is large but not a hard 4C inside 180D |
| C31_006910_2022_YOON_NUCLEAR_POLICY_THEME | policy_theme_break | 2022-10-13 | hard_4c_success_if_triggered_after_contract_absence | the loss of theme sponsorship and absence of contract bridge should route to watch/4C before price fully decays |
| C31_013990_2024_LOW_BIRTH_POLICY_THEME | policy_theme_break | 2024-09-09 | hard_4c_success_if_triggered_after_contract_absence | demographic policy theme failed to convert into company-specific financial visibility |

## 17. Sector-Specific Rule Candidate

```text
rule_id = L10_C31_POLICY_EVENT_STRUCTURALITY_GATE
rule_scope = sector_specific
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
proposal_type = shadow_only
```

Rule candidate:

```text
If trigger_type is policy/subsidy/legislation/tender/legal event:
    allow Stage2-Actionable only when at least one of the following is true:
        - named customer or contract path is identifiable,
        - legal/regulatory block is removed,
        - signed tender/preferred bidder converts to concrete negotiation or settlement path,
        - official policy maps to company-level capacity, order, reimbursement, or contract visibility.
    otherwise cap at Stage2-Watch / theme-risk regardless of relative strength.
```

Backtest effect in this loop:

- Keeps 034020 and 052690 in the actionable set after the Westinghouse settlement.
- Blocks 006910 and 013990 from false Green/Yellow escalation because policy headline and price strength are not enough.

## 18. Canonical-Archetype Rule Candidate

```text
rule_id = C31_POLICY_EVENT_DE_RISKING_VS_THEME_SPIKE_SPLIT
rule_scope = canonical_archetype_specific
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
proposal_type = shadow_only
```

C31 scoring split:

| evidence pattern | C31 action |
|---|---|
| policy headline + price strength only | cap at Stage2-Watch; no Stage2 bonus beyond minimal event recognition |
| policy headline + legal/regulatory de-risking | Stage2-Actionable eligible |
| policy headline + named contract/tender/customer path | Stage2-Actionable eligible; Yellow if margin/revision bridge follows |
| policy headline + no conversion after 30-90D + high MAE | route to 4C watch / false positive review |
| policy headline + extreme positioning/valuation | 4B overlay only; full 4B requires non-price overhang evidence |

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | selected entries | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | score_return_alignment_verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current proxy | 4 | 44.32 | -19.57 | 109.18 | -26.44 | 0.50 | 1 | mixed; too permissive for policy-only themes, possibly late for legal settlement re-entry |
| P0b_e2r_2_0_baseline_reference | rollback reference | 4 | 44.32 | -19.57 | 109.18 | -26.44 | 0.50 | 2 | worse; lacks cleaner policy-only guard and re-entry distinction |
| P1_sector_specific_candidate_profile | L10 sector shadow | 2 accepted, 2 capped | 58.72 | -15.51 | 189.06 | -15.51 | 0.00 | 0 | improved by excluding theme-only false positives |
| P2_canonical_archetype_candidate_profile | C31 shadow | 2 accepted, 2 watch/4C | 58.72 | -15.51 | 189.06 | -15.51 | 0.00 | 0 | best alignment for C31 in this set |
| P3_counterexample_guard_profile | C31 guard | 2 accepted, 2 rejected | 58.72 | -15.51 | 189.06 | -15.51 | 0.00 | 0 | guard effective; avoids 006910/013990 theme traps |

## 20. Score-Return Alignment Matrix

Research proxy components only; these are **not** production scores.

| case_id | raw_component_scores_before summary | weighted_score_before | stage_label_before | raw_component_scores_after summary | weighted_score_after | stage_label_after | alignment |
|---|---|---:|---|---|---:|---|---|
| C31_034020_2025_WESTINGHOUSE_REENTRY | policy 8, legal risk -2, customer quality 6, RS 6, revision 0 | 78 | Stage2-Actionable | policy 8, legal de-risk +6, customer quality 7, RS 6, execution risk -1 | 84 | Stage2-Actionable / Yellow-watch | aligned; strong 180D MFE |
| C31_052690_2025_WESTINGHOUSE_REENTRY | policy 8, legal risk -2, customer quality 5, RS 4, revision 0 | 74 | Stage2-Watch/Actionable border | policy 8, legal de-risk +6, customer quality 7, RS 4, execution risk -2 | 82 | Stage2-Actionable | aligned but high MAE |
| C31_006910_2022_YOON_NUCLEAR_POLICY_THEME | policy 7, RS 8, customer 0, margin 0, execution risk -2 | 76 | Stage2-Actionable false positive risk | policy-only cap, customer 0, margin 0, thesis risk -8 | 63 | Stage2-Watch / theme-risk | improved; blocks false positive |
| C31_013990_2024_LOW_BIRTH_POLICY_THEME | policy 6, RS 8, customer 0, margin 0, execution risk -1 | 75 | Stage2-Actionable false positive risk | policy-only cap, customer 0, margin 0, thesis risk -8 | 61 | Stage2-Watch / theme-risk | improved; blocks false positive |

Canonical component keys used for every row:

```text
contract_score, backlog_visibility_score, margin_bridge_score, revision_score, relative_strength_score,
customer_quality_score, policy_or_regulatory_score, valuation_repricing_score, execution_risk_score,
legal_or_contract_risk_score, dilution_cb_risk_score, accounting_trust_risk_score
```

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | NUCLEAR_EXPORT_POLICY_OPTIONALITY_AND_POLICY_THEME_GUARD | 2 | 2 | 4 | 2 | 4 | 0 | 4 | 4 | 2 | true | true | still needs non-nuclear policy-positive cases and holdout across other sectors |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 2
new_trigger_family_count: 3
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - policy_only_theme_false_positive
  - legal_settlement_reentry_too_late_risk
new_axis_proposed:
  - C31_policy_event_structurality_gate
  - C31_legal_or_contract_de_risking_reentry_bonus
  - C31_policy_only_theme_cap
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Stock-web manifest and schema fields.
- Symbol profile paths and corporate-action candidate windows.
- Entry-date close from actual tradable shard rows.
- 30D/90D/180D MFE and MAE from observed tradable OHLC windows.
- Positive/counterexample balance for C31 policy-event residual research.
- Stage2/Green timing contrast and 4B local/full-window split.
```

Not validated in this run:

```text
- Production stock_agent scoring code.
- Live/current watchlist behavior.
- Broker API or automated trading behavior.
- Exact sell-rule implementation.
- Full accounting/financial statement parsing for all selected companies.
- 2Y forward windows for 2024/2025 entries.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C31_policy_event_structurality_gate,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"Policy event must map to legal/contract/customer/financial path before Stage2-Actionable promotion","accepted 034020/052690; capped 006910/013990","TR_C31_034020_20250117_STAGE2A|TR_C31_052690_20250117_STAGE2A|TR_C31_006910_20220310_STAGE2A|TR_C31_013990_20240103_STAGE2A",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C31_legal_or_contract_de_risking_reentry_bonus,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"Legal/IP/tender-risk removal can precede revisions and still align with 180D MFE","improves 034020/052690 timing","TR_C31_034020_20250117_STAGE2A|TR_C31_052690_20250117_STAGE2A",2,2,0,medium,canonical_shadow_only,"requires non-price legal or contract evidence"
shadow_weight,C31_policy_only_theme_cap,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"Policy theme + relative strength without company-level conversion should not reach Yellow/Green","blocks 006910/013990 false positives","TR_C31_006910_20220310_STAGE2A|TR_C31_013990_20240103_STAGE2A",2,2,2,medium,guard_shadow_only,"strengthens existing price-only blowoff guard"
```

## 25. Machine-Readable Rows

### JSONL rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C31_034020_2025_WESTINGHOUSE_REENTRY","symbol":"034020","company_name":"두산에너빌리티","round":"R11","loop":"72","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"NUCLEAR_EXPORT_POLICY_OPTIONALITY_AND_POLICY_THEME_GUARD","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TR_C31_034020_20250117_STAGE2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"legal_de_risking_plus_export_path_aligned_with_180D_MFE","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"legal/IP settlement re-entry; strong 180D MFE"}
{"row_type":"case","case_id":"C31_052690_2025_WESTINGHOUSE_REENTRY","symbol":"052690","company_name":"한전기술","round":"R11","loop":"72","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"NUCLEAR_EXPORT_POLICY_OPTIONALITY_AND_POLICY_THEME_GUARD","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"TR_C31_052690_20250117_STAGE2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"legal_de_risking_reentry_worked_but_90D_MAE_was_high","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"engineering leverage to settlement; high MAE before 180D rerating"}
{"row_type":"case","case_id":"C31_006910_2022_YOON_NUCLEAR_POLICY_THEME","symbol":"006910","company_name":"보성파워텍","round":"R11","loop":"72","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"NUCLEAR_EXPORT_POLICY_OPTIONALITY_AND_POLICY_THEME_GUARD","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TR_C31_006910_20220310_STAGE2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"policy_only_theme_initial_MFE_followed_by_large_drawdown","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"policy-only nuclear theme; no company-level contract bridge"}
{"row_type":"case","case_id":"C31_013990_2024_LOW_BIRTH_POLICY_THEME","symbol":"013990","company_name":"아가방컴퍼니","round":"R11","loop":"72","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"DEMOGRAPHIC_POLICY_THEME_GUARD","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TR_C31_013990_20240103_STAGE2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"demographic_policy_theme_failed_to_convert_to_financial_visibility","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"policy theme without company-specific conversion"}
{"row_type":"trigger","trigger_id":"TR_C31_034020_20250117_STAGE2A","case_id":"C31_034020_2025_WESTINGHOUSE_REENTRY","symbol":"034020","company_name":"두산에너빌리티","round":"R11","loop":"72","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"NUCLEAR_EXPORT_POLICY_OPTIONALITY_AND_POLICY_THEME_GUARD","sector":"policy_event_nuclear_export","primary_archetype":"policy_legal_de_risking","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2025-01-17","evidence_available_at_that_date":"KHNP/KEPCO-Westinghouse settlement removed nuclear export IP overhang","evidence_source":"Reuters 2025-01-17; stock-web tradable shard","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","customer_or_order_quality","legal_or_contract_de_risking"],"stage3_evidence_fields":["multiple_public_sources","financial_visibility_watch"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/034/034020/2025.csv","profile_path":"atlas/symbol_profiles/034/034020.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-01-17","entry_price":21750,"MFE_30D_pct":42.07,"MFE_90D_pct":99.77,"MFE_180D_pct":289.43,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.76,"MAE_90D_pct":-8.23,"MAE_180D_pct":-8.23,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-10-16","peak_price":84700,"drawdown_after_peak_pct":-5.79,"green_lateness_ratio":0.52,"four_b_local_peak_proximity":0.98,"four_b_full_window_peak_proximity":0.98,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C31_034020_20250117","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR_C31_052690_20250117_STAGE2A","case_id":"C31_052690_2025_WESTINGHOUSE_REENTRY","symbol":"052690","company_name":"한전기술","round":"R11","loop":"72","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"NUCLEAR_EXPORT_POLICY_OPTIONALITY_AND_POLICY_THEME_GUARD","sector":"policy_event_nuclear_export","primary_archetype":"policy_legal_de_risking","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2025-01-17","evidence_available_at_that_date":"KHNP/KEPCO-Westinghouse settlement improved Korean reactor export path","evidence_source":"Reuters 2025-01-17; stock-web tradable shard","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","customer_or_order_quality","legal_or_contract_de_risking"],"stage3_evidence_fields":["multiple_public_sources","financial_visibility_watch"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/052/052690/2025.csv","profile_path":"atlas/symbol_profiles/052/052690.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-01-17","entry_price":64500,"MFE_30D_pct":17.67,"MFE_90D_pct":17.67,"MFE_180D_pct":88.68,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-1.86,"MAE_90D_pct":-22.79,"MAE_180D_pct":-22.79,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-06-25","peak_price":121700,"drawdown_after_peak_pct":-31.72,"green_lateness_ratio":0.69,"four_b_local_peak_proximity":0.88,"four_b_full_window_peak_proximity":0.88,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"high_mae_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C31_052690_20250117","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR_C31_006910_20220310_STAGE2A","case_id":"C31_006910_2022_YOON_NUCLEAR_POLICY_THEME","symbol":"006910","company_name":"보성파워텍","round":"R11","loop":"72","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"NUCLEAR_EXPORT_POLICY_OPTIONALITY_AND_POLICY_THEME_GUARD","sector":"policy_event_nuclear_theme","primary_archetype":"policy_theme_false_positive","loop_objective":"counterexample_mining|residual_false_positive_mining","trigger_type":"Stage2-Actionable","trigger_date":"2022-03-10","evidence_available_at_that_date":"pro-nuclear presidential election result and policy expectation; no company-specific order bridge","evidence_source":"public election result; stock-web tradable shard","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006910/2022.csv","profile_path":"atlas/symbol_profiles/006/006910.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-03-10","entry_price":6840,"MFE_30D_pct":32.31,"MFE_90D_pct":32.31,"MFE_180D_pct":32.31,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-6.87,"MAE_90D_pct":-26.75,"MAE_180D_pct":-44.81,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-03-25","peak_price":9050,"drawdown_after_peak_pct":-58.29,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.69,"four_b_full_window_peak_proximity":0.69,"four_b_timing_verdict":"do_not_treat_as_full_4B_without_non_price_evidence","four_b_evidence_type":["price_only"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C31_006910_20220310","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR_C31_013990_20240103_STAGE2A","case_id":"C31_013990_2024_LOW_BIRTH_POLICY_THEME","symbol":"013990","company_name":"아가방컴퍼니","round":"R11","loop":"72","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"DEMOGRAPHIC_POLICY_THEME_GUARD","sector":"policy_event_demographic_theme","primary_archetype":"policy_theme_false_positive","loop_objective":"counterexample_mining|residual_false_positive_mining","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-03","evidence_available_at_that_date":"low-birth policy theme repricing; no company-specific order/margin bridge","evidence_source":"Reuters fertility-policy context; stock-web tradable shard","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/013/013990/2024.csv","profile_path":"atlas/symbol_profiles/013/013990.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-03","entry_price":5630,"MFE_30D_pct":27.53,"MFE_90D_pct":27.53,"MFE_180D_pct":27.53,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-10.48,"MAE_90D_pct":-20.52,"MAE_180D_pct":-29.93,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-18","peak_price":7180,"drawdown_after_peak_pct":-45.06,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.33,"four_b_full_window_peak_proximity":0.33,"four_b_timing_verdict":"price_only_local_4B_weak","four_b_evidence_type":["price_only"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C31_013990_20240103","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C31_034020_2025_WESTINGHOUSE_REENTRY","trigger_id":"TR_C31_034020_20250117_STAGE2A","symbol":"034020","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":6,"customer_quality_score":6,"policy_or_regulatory_score":8,"valuation_repricing_score":5,"execution_risk_score":-1,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":6,"customer_quality_score":7,"policy_or_regulatory_score":8,"valuation_repricing_score":5,"execution_risk_score":-1,"legal_or_contract_risk_score":6,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":84,"stage_label_after":"Stage2-Actionable_YellowWatch","changed_components":["legal_or_contract_risk_score","customer_quality_score","backlog_visibility_score"],"component_delta_explanation":"C31 settlement de-risks export path without waiting for full revisions.","MFE_90D_pct":99.77,"MAE_90D_pct":-8.23,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C31_052690_2025_WESTINGHOUSE_REENTRY","trigger_id":"TR_C31_052690_20250117_STAGE2A","symbol":"052690","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":4,"customer_quality_score":5,"policy_or_regulatory_score":8,"valuation_repricing_score":4,"execution_risk_score":-2,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":74,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":4,"customer_quality_score":7,"policy_or_regulatory_score":8,"valuation_repricing_score":4,"execution_risk_score":-2,"legal_or_contract_risk_score":6,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":82,"stage_label_after":"Stage2-Actionable","changed_components":["legal_or_contract_risk_score","customer_quality_score"],"component_delta_explanation":"Legal/IP settlement is an early C31 re-entry bridge; Green still requires later confirmation.","MFE_90D_pct":17.67,"MAE_90D_pct":-22.79,"score_return_alignment_label":"aligned_but_high_MAE","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C31_006910_2022_YOON_NUCLEAR_POLICY_THEME","trigger_id":"TR_C31_006910_20220310_STAGE2A","symbol":"006910","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":7,"valuation_repricing_score":5,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable_false_positive_risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":3,"valuation_repricing_score":3,"execution_risk_score":-6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":63,"stage_label_after":"Stage2-Watch_themeRisk","changed_components":["policy_or_regulatory_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"Policy-only theme is capped because no company-level contract or margin bridge exists.","MFE_90D_pct":32.31,"MAE_90D_pct":-26.75,"score_return_alignment_label":"false_positive_blocked","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C31_013990_2024_LOW_BIRTH_POLICY_THEME","trigger_id":"TR_C31_013990_20240103_STAGE2A","symbol":"013990","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":6,"valuation_repricing_score":4,"execution_risk_score":-1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":75,"stage_label_before":"Stage2-Actionable_false_positive_risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":2,"valuation_repricing_score":2,"execution_risk_score":-7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":61,"stage_label_after":"Stage2-Watch_themeRisk","changed_components":["policy_or_regulatory_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"Demographic policy theme lacks company-level conversion and should be capped.","MFE_90D_pct":27.53,"MAE_90D_pct":-20.52,"score_return_alignment_label":"false_positive_blocked","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R11","loop":"72","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":3,"new_trigger_family_count":3,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":2,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["policy_only_theme_false_positive","legal_settlement_reentry_too_late_risk"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_round = R11
completed_loop = 72
next_round = R12
next_loop = 72
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-web files validated in this run:

```text
atlas/manifest.json
atlas/schema.json
atlas/symbol_profiles/034/034020.json
atlas/symbol_profiles/052/052690.json
atlas/symbol_profiles/006/006910.json
atlas/symbol_profiles/013/013990.json
atlas/ohlcv_tradable_by_symbol_year/034/034020/2025.csv
atlas/ohlcv_tradable_by_symbol_year/052/052690/2025.csv
atlas/ohlcv_tradable_by_symbol_year/006/006910/2022.csv
atlas/ohlcv_tradable_by_symbol_year/013/013990/2024.csv
```

External evidence notes used for narrative classification:

```text
- Reuters, 2024-07-17: Czech government selected KHNP over EDF for Dukovany nuclear units; South Korean nuclear-related shares reacted.
- Reuters, 2025-01-17: KHNP/KEPCO and Westinghouse agreed to end an IP dispute and strengthen cooperation in global nuclear markets.
- Public 2022 South Korean presidential election result: pro-nuclear policy regime expectation after Yoon Suk Yeol victory.
- Reuters, 2025-02-26: South Korea's expanded birth-support policy context; used as demographic-policy theme background, not as company-specific conversion evidence.
```

