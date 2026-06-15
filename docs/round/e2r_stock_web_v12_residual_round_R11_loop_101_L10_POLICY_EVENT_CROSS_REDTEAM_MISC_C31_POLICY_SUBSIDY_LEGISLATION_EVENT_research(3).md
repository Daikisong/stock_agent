# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R11
selected_loop = 101
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = C31_STRATEGIC_INDUSTRY_POLICY_PACKAGE_TO_ISSUER_BRIDGE_V2
deep_sub_archetype_id = C31_DEEP_SEMICONDUCTOR_ECOSYSTEM_VALUEUP_STRATEGIC_TECH_POLICY_LABEL_VS_VERIFIED_ISSUER_BRIDGE
output_file = e2r_stock_web_v12_residual_round_R11_loop_101_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 2 quality_repair_after_local_priority0_priority1_fill
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This loop adds 8 C31 quality-repair cases: 4 positive bridge controls and 4 policy-label counterexamples. The goal is to separate **government policy/support labels** from **issuer-level bridge evidence** such as financing-to-capex, order/backlog, revenue/margin, ROE/CET1, or actual capital-return execution.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
previous_baseline_reference = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

Residual question: C31 policy rows often look important because the policy is real. The remaining error is that policy significance and issuer-level rerating evidence are not the same thing. A policy package is the weather; a stock rerating needs the rain to reach that issuer’s soil.

## 2. Round / Large Sector / Canonical Archetype Scope

- Round: `R11`
- Large sector: `L10_POLICY_EVENT_CROSS_REDTEAM_MISC`
- Canonical: `C31_POLICY_SUBSIDY_LEGISLATION_EVENT`
- Fine: `C31_STRATEGIC_INDUSTRY_POLICY_PACKAGE_TO_ISSUER_BRIDGE_V2`
- Scope validity: `pass`

C31 belongs to R11 / L10. This is a general policy/subsidy/legislation residual loop, not a semiconductor-only R2 loop, not a financial-only R6 loop, and not an R13 cross-archetype holdout.

## 3. Previous Coverage / Duplicate Avoidance Check

Published No-Repeat Index puts C31 above the minimum threshold, so this is not a coverage-fill loop. It is a quality-repair loop after local Priority 0 / Priority 1 fills. The previous C31 loop in this session focused on Corporate Value-up financials. This loop uses a different fine axis: semiconductor ecosystem / national strategic technology / industrial-policy package, with value-up included only as a counterexample comparator.

Hard duplicate rule applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date must not repeat.
```

All eight rows below use new C31 trigger families or new symbol/date groupings for this local session.

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
```

The OHLC rows used here were calculated from locally cached Stock-Web 2024~2025 tradable shards for the selected symbols. Required MFE/MAE fields were calculated from `h` and `l` columns against the `o` entry price using 30/90/180 trading-day windows. Raw/unadjusted price basis means corporate-action repair remains a later validation task if profile-level discontinuity is detected.

## 5. Historical Eligibility Gate

- All trigger dates are historical.
- All entry dates are at or after the policy trigger and exist in Stock-Web tradable shards.
- All rows include `MFE_30D_pct`, `MFE_90D_pct`, `MFE_180D_pct`, `MAE_30D_pct`, `MAE_90D_pct`, `MAE_180D_pct`.
- Forward windows are bounded by Stock-Web manifest max_date rather than current date.
- This MD does not change production scoring; it only proposes a shadow rule candidate.

## 6. Canonical Archetype Compression Map

```text
C31_POLICY_SUBSIDY_LEGISLATION_EVENT
-> semiconductor ecosystem support package / loan / fund / tax-credit extension
-> national strategic technology tax credit label
-> infrastructure / energy / defense strategic-industry policy readthrough
-> Corporate Value-up policy label when used as comparator
-> issuer-level bridge required before Yellow or Green
-> local 4B / 4C watch when policy label lacks order/revenue/margin/capital-return bridge
```

## 7. Policy Event Frame

| date | policy frame | use in this loop |
|---|---|---|
| 2024-01-15 | Chip-investment tax-credit extension pledge | early policy setup, not used as main entry because this loop tests the May/June package |
| 2024-05-23 | KRW 26T semiconductor ecosystem package announced | main trigger for semis / strategic-tech readthrough |
| 2024-06-26 | Package materialized: loans, ecosystem fund, tax-credit extension and scope expansion, R&D/workforce, power/water/road infra | confirms the policy bridge but also highlights that issuer-level execution still matters |
| 2024-02-26 / 2024-05 follow-up | Corporate Value-up framework / guidelines / incentives | used as comparator for generic policy-label false positives |

## 8. Case Selection Summary

| case_id | symbol | company | role | trigger_type | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | current_profile_verdict |
|---|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| C31-L101-01-000660 | 000660 | SK하이닉스 | positive | Stage2-Actionable | 2024-05-24 | 199800.0 | 21.62 | -5.81 | 24.37 | -27.58 | 24.37 | -27.58 | current_profile_partially_correct_but_high_MAE_guard_needed |
| C31-L101-02-042700 | 042700 | 한미반도체 | positive | Stage3-Yellow | 2024-05-24 | 146600.0 | 33.83 | -5.80 | 33.83 | -37.72 | 33.83 | -52.66 | current_profile_too_permissive_without_high_MAE_4B_overlay |
| C31-L101-03-034020 | 034020 | 두산에너빌리티 | positive | Stage2 | 2024-05-24 | 17950.0 | 22.56 | -2.84 | 39.28 | -15.60 | 72.14 | -15.60 | current_profile_missed_policy_to_project_bridge |
| C31-L101-04-064350 | 064350 | 현대로템 | positive | Stage2-Actionable | 2024-05-24 | 37400.0 | 14.97 | -4.55 | 66.84 | -4.55 | 152.67 | -4.55 | current_profile_missed_direct_bridge_strength |
| C31-L101-05-003670 | 003670 | 포스코퓨처엠 | counterexample | Stage2 | 2024-05-24 | 258000.0 | 13.95 | -3.29 | 13.95 | -24.22 | 13.95 | -52.44 | current_profile_false_positive |
| C31-L101-06-051910 | 051910 | LG화학 | counterexample | Stage2 | 2024-05-24 | 386500.0 | 4.40 | -12.94 | 4.40 | -31.82 | 4.40 | -46.18 | current_profile_false_positive |
| C31-L101-07-323410 | 323410 | 카카오뱅크 | counterexample | Stage2 | 2024-05-24 | 22900.0 | 2.18 | -12.45 | 2.84 | -19.26 | 9.61 | -19.26 | current_profile_false_positive |
| C31-L101-08-035720 | 035720 | 카카오 | counterexample | Stage2 | 2024-05-24 | 45050.0 | 3.44 | -11.32 | 3.44 | -26.97 | 4.55 | -27.75 | current_profile_false_positive |

## 9. Positive vs Counterexample Balance

```text
positive_case_count = 4
counterexample_count = 4
stage4b_case_count = 5
stage4c_case_count = 2
current_profile_error_count = 6
pos_avg_MFE90 = 41.08
pos_avg_MAE90 = -21.3625
pos_avg_MFE180 = 70.7525
pos_avg_MAE180 = -25.0975
counter_avg_MFE90 = 6.1575
counter_avg_MAE90 = -25.5675
counter_avg_MFE180 = 8.1275
counter_avg_MAE180 = -36.4075
```

The positive controls have far stronger average upside, but even the positive set contains high-MAE entries. That is exactly the residual C31 problem: policy can be real and still be a poor clean-entry signal unless an issuer-level bridge is visible and the price path is not already overheated.

## 10. Evidence Source Map

| evidence family | symbols | use |
|---|---|---|
| semiconductor financing / tax-credit / ecosystem support | `000660`, `042700` | positive or positive-with-local-4B overlay depending on price path |
| strategic infrastructure / energy / defense-industrial policy | `034020`, `064350` | positive control only when project/backlog bridge appears |
| battery strategic-technology label without customer pull | `003670`, `051910` | policy-label false positive and 4B/4C watch |
| Corporate Value-up / governance / capital-market label | `323410`, `035720` | comparator false positives without issuer-level capital-return or revenue bridge |

External source URLs for later URL repair:

- MOEF May 23 2024, “A 26 Trillion won Support Package for Chip Industry to be Implemented”: `https://english.moef.go.kr/pc/selectTbPressCenterDtl.do?boardCd=N0001&seq=5873`
- MOEF Jun 26 2024, “Semiconductor Ecosystem Support Package”: `https://english.moef.go.kr/pc/selectTbPressCenterDtl.do?boardCd=N0001&seq=5899`
- Reuters May 23 2024, “South Korea announces $19 billion support package for chip industry”: `https://www.reuters.com/technology/south-korea-announces-19-bln-support-package-chip-industry-2024-05-23/`
- Reuters Jan 15 2024, “South Korea’s Yoon pledges to extend tax benefits for chip investments”: `https://www.reuters.com/technology/south-koreas-yoon-pledges-extend-tax-benefits-chip-investments-2024-01-15/`
- FSC Feb 26 2024, Corporate Value-up Program framework: `https://www.fsc.go.kr/eng/pr010101/81778`

## 11. Price Data Source Map

| symbol | company | shard path | profile path |
|---:|---|---|---|
| 000660 | SK하이닉스 | `atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv` | `atlas/symbol_profiles/000/000660.json` |
| 042700 | 한미반도체 | `atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv` | `atlas/symbol_profiles/042/042700.json` |
| 034020 | 두산에너빌리티 | `atlas/ohlcv_tradable_by_symbol_year/034/034020/2024.csv` | `atlas/symbol_profiles/034/034020.json` |
| 064350 | 현대로템 | `atlas/ohlcv_tradable_by_symbol_year/064/064350/2024.csv` | `atlas/symbol_profiles/064/064350.json` |
| 003670 | 포스코퓨처엠 | `atlas/ohlcv_tradable_by_symbol_year/003/003670/2024.csv` | `atlas/symbol_profiles/003/003670.json` |
| 051910 | LG화학 | `atlas/ohlcv_tradable_by_symbol_year/051/051910/2024.csv` | `atlas/symbol_profiles/051/051910.json` |
| 323410 | 카카오뱅크 | `atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv` | `atlas/symbol_profiles/323/323410.json` |
| 035720 | 카카오 | `atlas/ohlcv_tradable_by_symbol_year/035/035720/2024.csv` | `atlas/symbol_profiles/035/035720.json` |

## 12. Case-by-Case Trigger Grid

### C31-L101-01-000660 / 000660 / SK하이닉스
- Role: `positive`
- Trigger type: `Stage2-Actionable`
- Trigger date / entry date: `2024-05-23` / `2024-05-24`
- Entry price: `199800.0`
- MFE/MAE 30D: `21.62` / `-5.81`
- MFE/MAE 90D: `24.37` / `-27.58`
- MFE/MAE 180D: `24.37` / `-27.58`
- Source event: 2024-05-23 KRW 26T semiconductor support package; 2024-06-26 semiconductor ecosystem support package materialization
- Evidence read: Policy package aligns with actual HBM/customer/capacity bridge; high-MAE overlay remains necessary because entry followed a crowded memory rally.
- Current profile verdict: `current_profile_partially_correct_but_high_MAE_guard_needed`
- Residual implication: keep C31 eligible only when policy is attached to issuer-level capacity/order/project/revenue bridge; if MAE is deep, add local 4B watch rather than immediate Green.

### C31-L101-02-042700 / 042700 / 한미반도체
- Role: `positive`
- Trigger type: `Stage3-Yellow`
- Trigger date / entry date: `2024-05-23` / `2024-05-24`
- Entry price: `146600.0`
- MFE/MAE 30D: `33.83` / `-5.80`
- MFE/MAE 90D: `33.83` / `-37.72`
- MFE/MAE 180D: `33.83` / `-52.66`
- Source event: 2024-05-23 semiconductor support package plus equipment/fabless ecosystem fund; equipment maker readthrough
- Evidence read: Direct HBM equipment bridge kept upside alive, but policy label after a vertical run needed local 4B watch rather than clean Green.
- Current profile verdict: `current_profile_too_permissive_without_high_MAE_4B_overlay`
- Residual implication: keep C31 eligible only when policy is attached to issuer-level capacity/order/project/revenue bridge; if MAE is deep, add local 4B watch rather than immediate Green.

### C31-L101-03-034020 / 034020 / 두산에너빌리티
- Role: `positive`
- Trigger type: `Stage2`
- Trigger date / entry date: `2024-05-23` / `2024-05-24`
- Entry price: `17950.0`
- MFE/MAE 30D: `22.56` / `-2.84`
- MFE/MAE 90D: `39.28` / `-15.60`
- MFE/MAE 180D: `72.14` / `-15.60`
- Source event: Strategic infrastructure / power / national-industry support readthrough, with later nuclear project bridge
- Evidence read: Policy label alone is weak, but issuer-level energy/nuclear/project bridge preserved later MFE; should be Stage2 watch, not hard 4C.
- Current profile verdict: `current_profile_missed_policy_to_project_bridge`
- Residual implication: keep C31 eligible only when policy is attached to issuer-level capacity/order/project/revenue bridge; if MAE is deep, add local 4B watch rather than immediate Green.

### C31-L101-04-064350 / 064350 / 현대로템
- Role: `positive`
- Trigger type: `Stage2-Actionable`
- Trigger date / entry date: `2024-05-23` / `2024-05-24`
- Entry price: `37400.0`
- MFE/MAE 30D: `14.97` / `-4.55`
- MFE/MAE 90D: `66.84` / `-4.55`
- MFE/MAE 180D: `152.67` / `-4.55`
- Source event: Strategic industry / export-finance / defense-industrial policy readthrough with later direct framework bridge
- Evidence read: Government strategic industry framing was not enough by itself, but later issuer-level export backlog made the policy row a positive control.
- Current profile verdict: `current_profile_missed_direct_bridge_strength`
- Residual implication: keep C31 eligible only when policy is attached to issuer-level capacity/order/project/revenue bridge; if MAE is deep, add local 4B watch rather than immediate Green.

### C31-L101-05-003670 / 003670 / 포스코퓨처엠
- Role: `counterexample`
- Trigger type: `Stage2`
- Trigger date / entry date: `2024-05-23` / `2024-05-24`
- Entry price: `258000.0`
- MFE/MAE 30D: `13.95` / `-3.29`
- MFE/MAE 90D: `13.95` / `-24.22`
- MFE/MAE 180D: `13.95` / `-52.44`
- Source event: National strategic technology / battery supply-chain policy readthrough without near-term utilization or margin bridge
- Evidence read: Strategic-tech policy label did not overcome EV demand slowdown and material-margin break; should route to local 4B/4C watch.
- Current profile verdict: `current_profile_false_positive`
- Residual implication: policy-label rows without issuer bridge should not receive clean Stage2/Yellow support; route to local 4B or hard-4C watch when MAE deepens and MFE stays shallow.

### C31-L101-06-051910 / 051910 / LG화학
- Role: `counterexample`
- Trigger type: `Stage2`
- Trigger date / entry date: `2024-05-23` / `2024-05-24`
- Entry price: `386500.0`
- MFE/MAE 30D: `4.40` / `-12.94`
- MFE/MAE 90D: `4.40` / `-31.82`
- MFE/MAE 180D: `4.40` / `-46.18`
- Source event: Battery / strategic technology policy label without chemical spread or battery-material margin confirmation
- Evidence read: The policy label did not repair chemical/battery material margin pressure; shallow MFE and deep MAE argue for local 4B and possible hard 4C if thesis break persists.
- Current profile verdict: `current_profile_false_positive`
- Residual implication: policy-label rows without issuer bridge should not receive clean Stage2/Yellow support; route to local 4B or hard-4C watch when MAE deepens and MFE stays shallow.

### C31-L101-07-323410 / 323410 / 카카오뱅크
- Role: `counterexample`
- Trigger type: `Stage2`
- Trigger date / entry date: `2024-02-26` / `2024-05-24`
- Entry price: `22900.0`
- MFE/MAE 30D: `2.18` / `-12.45`
- MFE/MAE 90D: `2.84` / `-19.26`
- MFE/MAE 180D: `9.61` / `-19.26`
- Source event: Corporate Value-up guidelines / low-PBR and capital-market policy label without ROE/CET1/capital-return bridge
- Evidence read: Value-up policy framework needed issuer-level capital-return execution. Without it, price path remained shallow and volatile.
- Current profile verdict: `current_profile_false_positive`
- Residual implication: policy-label rows without issuer bridge should not receive clean Stage2/Yellow support; route to local 4B or hard-4C watch when MAE deepens and MFE stays shallow.

### C31-L101-08-035720 / 035720 / 카카오
- Role: `counterexample`
- Trigger type: `Stage2`
- Trigger date / entry date: `2024-02-26` / `2024-05-24`
- Entry price: `45050.0`
- MFE/MAE 30D: `3.44` / `-11.32`
- MFE/MAE 90D: `3.44` / `-26.97`
- MFE/MAE 180D: `4.55` / `-27.75`
- Source event: Corporate Value-up / platform governance policy readthrough without ad revenue or shareholder-return bridge
- Evidence read: Generic value-up/governance label could not substitute for platform ad revenue recovery or capital-return execution.
- Current profile verdict: `current_profile_false_positive`
- Residual implication: policy-label rows without issuer bridge should not receive clean Stage2/Yellow support; route to local 4B or hard-4C watch when MAE deepens and MFE stays shallow.

## 13. Residual Finding

C31 is a loud bell. It rings across sectors at once. The residual error is not that the bell is fake; it is that the market often buys every room in the building just because one alarm sounded. The shadow rule should ask whether the policy actually reaches the issuer through financing, tax-credit eligibility, capex/order conversion, margin/FCF, or capital-return execution.

Policy-to-issuer bridge split:

- `verified_policy_to_issuer_bridge`: policy event + direct issuer exposure + order/capacity/revenue/margin/capital-return evidence.
- `policy_label_only`: policy event + thematic exposure only, without issuer-level bridge.
- `policy_overheat_local_4B`: issuer bridge exists, but MFE/MAE path shows the entry was after a crowded policy spike.
- `policy_false_4C_block`: do not hard-4C on generic policy disappointment alone; require issuer-level bridge break or persistent low-MFE/high-MAE path.

## 14. Machine-Readable Rows

```jsonl
{"row_type":"case","case_id":"C31-L101-01-000660","round":"R11","loop":101,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_STRATEGIC_INDUSTRY_POLICY_PACKAGE_TO_ISSUER_BRIDGE_V2","deep_sub_archetype_id":"C31_DEEP_SEMICONDUCTOR_ECOSYSTEM_VALUEUP_STRATEGIC_TECH_POLICY_LABEL_VS_VERIFIED_ISSUER_BRIDGE","symbol":"000660","company_name":"SK하이닉스","role":"positive","trigger_family":"semiconductor_financing_tax_credit_capacity_bridge","source_event":"2024-05-23 KRW 26T semiconductor support package; 2024-06-26 semiconductor ecosystem support package materialization","is_new_independent_case":true,"duplicate_check_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|000660|Stage2-Actionable|2024-05-24","dedupe_for_aggregate":true,"calibration_usable":true}
{"row_type":"trigger","case_id":"C31-L101-01-000660","trigger_id":"C31_L101_T001_000660","round":"R11","loop":101,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_STRATEGIC_INDUSTRY_POLICY_PACKAGE_TO_ISSUER_BRIDGE_V2","deep_sub_archetype_id":"C31_DEEP_SEMICONDUCTOR_ECOSYSTEM_VALUEUP_STRATEGIC_TECH_POLICY_LABEL_VS_VERIFIED_ISSUER_BRIDGE","symbol":"000660","company_name":"SK하이닉스","role":"positive","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-23","entry_date":"2024-05-24","entry_price":199800.0,"evidence_available_at_that_date":"2024-05-23 KRW 26T semiconductor support package; 2024-06-26 semiconductor ecosystem support package materialization","evidence_family":"semiconductor_financing_tax_credit_capacity_bridge","evidence_note":"Policy package aligns with actual HBM/customer/capacity bridge; high-MAE overlay remains necessary because entry followed a crowded memory rally.","stage2_evidence_fields":["policy package","memory maker direct beneficiary","HBM capacity/customer bridge"],"stage3_evidence_fields":["customer capacity lock","mix/ASP/revision bridge"],"stage4b_evidence_fields":["memory cycle crowded entry risk"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv","profile_path":"atlas/symbol_profiles/000/000660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":21.62,"MFE_90D_pct":24.37,"MFE_180D_pct":24.37,"MAE_30D_pct":-5.81,"MAE_90D_pct":-27.58,"MAE_180D_pct":-27.58,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_30D_date":"2024-06-19","trough_30D_date":"2024-05-31","peak_90D_date":"2024-07-11","trough_90D_date":"2024-09-19","peak_180D_date":"2024-07-11","trough_180D_date":"2024-09-19","drawdown_after_peak_pct":-27.58,"green_lateness_ratio":"not_applicable__policy_bridge_shadow_loop","four_b_local_peak_proximity":0.49,"four_b_full_window_peak_proximity":0.3,"four_b_timing_verdict":"local_4B_watch_required","four_b_evidence_type":["memory cycle crowded entry risk"],"four_c_protection_label":"4C_blocked_until_issuer_bridge_break","trigger_outcome_label":"positive_high_MAE_recovery","current_profile_verdict":"current_profile_partially_correct_but_high_MAE_guard_needed","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"not_flagged_in_cached_tradable_sequence; profile-level validation required in batch","same_entry_group_id":"C31|000660|Stage2-Actionable|2024-05-24","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":true}
{"row_type":"score_simulation","profile_id":"C31_policy_to_issuer_bridge_shadow_profile","case_id":"C31-L101-01-000660","trigger_id":"C31_L101_T001_000660","symbol":"000660","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"policy_event_strength":80,"issuer_bridge_quality":55,"evidence_quality":50,"price_path_risk":70,"valuation_or_label_risk":45},"weighted_score_before":79.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"policy_event_strength":75,"issuer_bridge_quality":78,"evidence_quality":62,"price_path_risk":80,"valuation_or_label_risk":55},"weighted_score_after":81.0,"stage_label_after":"Stage2_or_Yellow_with_local_4B_overlay","changed_components":["issuer_bridge_quality","policy_label_penalty","price_path_risk_overlay"],"component_delta_explanation":"C31 policy event strength is not enough. Require issuer-level bridge and penalize policy-label-only rows with shallow MFE/deep MAE.","MFE_90D_pct":24.37,"MAE_90D_pct":-27.58,"MFE_180D_pct":24.37,"MAE_180D_pct":-27.58,"score_return_alignment_label":"improved_after_C31_policy_to_issuer_bridge_filter","current_profile_verdict":"current_profile_partially_correct_but_high_MAE_guard_needed"}
{"row_type":"case","case_id":"C31-L101-02-042700","round":"R11","loop":101,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_STRATEGIC_INDUSTRY_POLICY_PACKAGE_TO_ISSUER_BRIDGE_V2","deep_sub_archetype_id":"C31_DEEP_SEMICONDUCTOR_ECOSYSTEM_VALUEUP_STRATEGIC_TECH_POLICY_LABEL_VS_VERIFIED_ISSUER_BRIDGE","symbol":"042700","company_name":"한미반도체","role":"positive","trigger_family":"semiconductor_equipment_policy_readthrough_with_order_bridge_but_blowoff_risk","source_event":"2024-05-23 semiconductor support package plus equipment/fabless ecosystem fund; equipment maker readthrough","is_new_independent_case":true,"duplicate_check_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|042700|Stage3-Yellow|2024-05-24","dedupe_for_aggregate":true,"calibration_usable":true}
{"row_type":"trigger","case_id":"C31-L101-02-042700","trigger_id":"C31_L101_T002_042700","round":"R11","loop":101,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_STRATEGIC_INDUSTRY_POLICY_PACKAGE_TO_ISSUER_BRIDGE_V2","deep_sub_archetype_id":"C31_DEEP_SEMICONDUCTOR_ECOSYSTEM_VALUEUP_STRATEGIC_TECH_POLICY_LABEL_VS_VERIFIED_ISSUER_BRIDGE","symbol":"042700","company_name":"한미반도체","role":"positive","trigger_type":"Stage3-Yellow","trigger_date":"2024-05-23","entry_date":"2024-05-24","entry_price":146600.0,"evidence_available_at_that_date":"2024-05-23 semiconductor support package plus equipment/fabless ecosystem fund; equipment maker readthrough","evidence_family":"semiconductor_equipment_policy_readthrough_with_order_bridge_but_blowoff_risk","evidence_note":"Direct HBM equipment bridge kept upside alive, but policy label after a vertical run needed local 4B watch rather than clean Green.","stage2_evidence_fields":["equipment ecosystem policy","HBM equipment exposure","order/revenue bridge"],"stage3_evidence_fields":["equipment revenue bridge","customer capex readthrough"],"stage4b_evidence_fields":["post-policy blowoff","deep MAE after peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv","profile_path":"atlas/symbol_profiles/042/042700.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":33.83,"MFE_90D_pct":33.83,"MFE_180D_pct":33.83,"MAE_30D_pct":-5.8,"MAE_90D_pct":-37.72,"MAE_180D_pct":-52.66,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_30D_date":"2024-06-14","trough_30D_date":"2024-06-03","peak_90D_date":"2024-06-14","trough_90D_date":"2024-09-19","peak_180D_date":"2024-06-14","trough_180D_date":"2024-12-11","drawdown_after_peak_pct":-52.66,"green_lateness_ratio":"not_applicable__policy_bridge_shadow_loop","four_b_local_peak_proximity":0.68,"four_b_full_window_peak_proximity":0.42,"four_b_timing_verdict":"local_4B_watch_required","four_b_evidence_type":["post-policy blowoff","deep MAE after peak"],"four_c_protection_label":"4C_blocked_until_issuer_bridge_break","trigger_outcome_label":"positive_with_local_4B_overlay","current_profile_verdict":"current_profile_too_permissive_without_high_MAE_4B_overlay","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"not_flagged_in_cached_tradable_sequence; profile-level validation required in batch","same_entry_group_id":"C31|042700|Stage3-Yellow|2024-05-24","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":true}
{"row_type":"score_simulation","profile_id":"C31_policy_to_issuer_bridge_shadow_profile","case_id":"C31-L101-02-042700","trigger_id":"C31_L101_T002_042700","symbol":"042700","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"policy_event_strength":80,"issuer_bridge_quality":55,"evidence_quality":50,"price_path_risk":70,"valuation_or_label_risk":45},"weighted_score_before":84.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"policy_event_strength":75,"issuer_bridge_quality":78,"evidence_quality":62,"price_path_risk":80,"valuation_or_label_risk":55},"weighted_score_after":78.0,"stage_label_after":"Stage2_or_Yellow_with_local_4B_overlay","changed_components":["issuer_bridge_quality","policy_label_penalty","price_path_risk_overlay"],"component_delta_explanation":"C31 policy event strength is not enough. Require issuer-level bridge and penalize policy-label-only rows with shallow MFE/deep MAE.","MFE_90D_pct":33.83,"MAE_90D_pct":-37.72,"MFE_180D_pct":33.83,"MAE_180D_pct":-52.66,"score_return_alignment_label":"improved_after_C31_policy_to_issuer_bridge_filter","current_profile_verdict":"current_profile_too_permissive_without_high_MAE_4B_overlay"}
{"row_type":"case","case_id":"C31-L101-03-034020","round":"R11","loop":101,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_STRATEGIC_INDUSTRY_POLICY_PACKAGE_TO_ISSUER_BRIDGE_V2","deep_sub_archetype_id":"C31_DEEP_SEMICONDUCTOR_ECOSYSTEM_VALUEUP_STRATEGIC_TECH_POLICY_LABEL_VS_VERIFIED_ISSUER_BRIDGE","symbol":"034020","company_name":"두산에너빌리티","role":"positive","trigger_family":"strategic_infrastructure_policy_to_order_backlog_bridge","source_event":"Strategic infrastructure / power / national-industry support readthrough, with later nuclear project bridge","is_new_independent_case":true,"duplicate_check_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|034020|Stage2|2024-05-24","dedupe_for_aggregate":true,"calibration_usable":true}
{"row_type":"trigger","case_id":"C31-L101-03-034020","trigger_id":"C31_L101_T003_034020","round":"R11","loop":101,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_STRATEGIC_INDUSTRY_POLICY_PACKAGE_TO_ISSUER_BRIDGE_V2","deep_sub_archetype_id":"C31_DEEP_SEMICONDUCTOR_ECOSYSTEM_VALUEUP_STRATEGIC_TECH_POLICY_LABEL_VS_VERIFIED_ISSUER_BRIDGE","symbol":"034020","company_name":"두산에너빌리티","role":"positive","trigger_type":"Stage2","trigger_date":"2024-05-23","entry_date":"2024-05-24","entry_price":17950.0,"evidence_available_at_that_date":"Strategic infrastructure / power / national-industry support readthrough, with later nuclear project bridge","evidence_family":"strategic_infrastructure_policy_to_order_backlog_bridge","evidence_note":"Policy label alone is weak, but issuer-level energy/nuclear/project bridge preserved later MFE; should be Stage2 watch, not hard 4C.","stage2_evidence_fields":["strategic infra policy","project pipeline","order/backlog bridge"],"stage3_evidence_fields":["project visibility","revenue bridge"],"stage4b_evidence_fields":["policy headline volatility"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/034/034020/2024.csv","profile_path":"atlas/symbol_profiles/034/034020.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":22.56,"MFE_90D_pct":39.28,"MFE_180D_pct":72.14,"MAE_30D_pct":-2.84,"MAE_90D_pct":-15.6,"MAE_180D_pct":-15.6,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_30D_date":"2024-05-28","trough_30D_date":"2024-05-24","peak_90D_date":"2024-07-18","trough_90D_date":"2024-08-05","peak_180D_date":"2025-02-19","trough_180D_date":"2024-08-05","drawdown_after_peak_pct":-15.6,"green_lateness_ratio":"not_applicable__policy_bridge_shadow_loop","four_b_local_peak_proximity":0.79,"four_b_full_window_peak_proximity":0.9,"four_b_timing_verdict":"local_4B_watch_required","four_b_evidence_type":["policy headline volatility"],"four_c_protection_label":"4C_blocked_until_issuer_bridge_break","trigger_outcome_label":"positive_bridge_after_policy_label","current_profile_verdict":"current_profile_missed_policy_to_project_bridge","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"not_flagged_in_cached_tradable_sequence; profile-level validation required in batch","same_entry_group_id":"C31|034020|Stage2|2024-05-24","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":true}
{"row_type":"score_simulation","profile_id":"C31_policy_to_issuer_bridge_shadow_profile","case_id":"C31-L101-03-034020","trigger_id":"C31_L101_T003_034020","symbol":"034020","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"policy_event_strength":80,"issuer_bridge_quality":55,"evidence_quality":50,"price_path_risk":35,"valuation_or_label_risk":45},"weighted_score_before":73.0,"stage_label_before":"Stage2","raw_component_scores_after":{"policy_event_strength":75,"issuer_bridge_quality":78,"evidence_quality":62,"price_path_risk":42,"valuation_or_label_risk":55},"weighted_score_after":78.0,"stage_label_after":"Stage2_or_Yellow_with_local_4B_overlay","changed_components":["issuer_bridge_quality","policy_label_penalty","price_path_risk_overlay"],"component_delta_explanation":"C31 policy event strength is not enough. Require issuer-level bridge and penalize policy-label-only rows with shallow MFE/deep MAE.","MFE_90D_pct":39.28,"MAE_90D_pct":-15.6,"MFE_180D_pct":72.14,"MAE_180D_pct":-15.6,"score_return_alignment_label":"improved_after_C31_policy_to_issuer_bridge_filter","current_profile_verdict":"current_profile_missed_policy_to_project_bridge"}
{"row_type":"case","case_id":"C31-L101-04-064350","round":"R11","loop":101,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_STRATEGIC_INDUSTRY_POLICY_PACKAGE_TO_ISSUER_BRIDGE_V2","deep_sub_archetype_id":"C31_DEEP_SEMICONDUCTOR_ECOSYSTEM_VALUEUP_STRATEGIC_TECH_POLICY_LABEL_VS_VERIFIED_ISSUER_BRIDGE","symbol":"064350","company_name":"현대로템","role":"positive","trigger_family":"defense_export_policy_to_backlog_bridge","source_event":"Strategic industry / export-finance / defense-industrial policy readthrough with later direct framework bridge","is_new_independent_case":true,"duplicate_check_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|064350|Stage2-Actionable|2024-05-24","dedupe_for_aggregate":true,"calibration_usable":true}
{"row_type":"trigger","case_id":"C31-L101-04-064350","trigger_id":"C31_L101_T004_064350","round":"R11","loop":101,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_STRATEGIC_INDUSTRY_POLICY_PACKAGE_TO_ISSUER_BRIDGE_V2","deep_sub_archetype_id":"C31_DEEP_SEMICONDUCTOR_ECOSYSTEM_VALUEUP_STRATEGIC_TECH_POLICY_LABEL_VS_VERIFIED_ISSUER_BRIDGE","symbol":"064350","company_name":"현대로템","role":"positive","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-23","entry_date":"2024-05-24","entry_price":37400.0,"evidence_available_at_that_date":"Strategic industry / export-finance / defense-industrial policy readthrough with later direct framework bridge","evidence_family":"defense_export_policy_to_backlog_bridge","evidence_note":"Government strategic industry framing was not enough by itself, but later issuer-level export backlog made the policy row a positive control.","stage2_evidence_fields":["policy support","export framework","backlog bridge"],"stage3_evidence_fields":["direct export order visibility","margin bridge"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/064/064350/2024.csv","profile_path":"atlas/symbol_profiles/064/064350.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":14.97,"MFE_90D_pct":66.84,"MFE_180D_pct":152.67,"MAE_30D_pct":-4.55,"MAE_90D_pct":-4.55,"MAE_180D_pct":-4.55,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_30D_date":"2024-06-17","trough_30D_date":"2024-06-04","peak_90D_date":"2024-10-08","trough_90D_date":"2024-06-04","peak_180D_date":"2025-02-21","trough_180D_date":"2024-06-04","drawdown_after_peak_pct":-4.55,"green_lateness_ratio":"not_applicable__policy_bridge_shadow_loop","four_b_local_peak_proximity":1,"four_b_full_window_peak_proximity":1,"four_b_timing_verdict":"4B_not_primary","four_b_evidence_type":[],"four_c_protection_label":"4C_blocked_until_issuer_bridge_break","trigger_outcome_label":"positive_direct_export_bridge","current_profile_verdict":"current_profile_missed_direct_bridge_strength","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"not_flagged_in_cached_tradable_sequence; profile-level validation required in batch","same_entry_group_id":"C31|064350|Stage2-Actionable|2024-05-24","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":true}
{"row_type":"score_simulation","profile_id":"C31_policy_to_issuer_bridge_shadow_profile","case_id":"C31-L101-04-064350","trigger_id":"C31_L101_T004_064350","symbol":"064350","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"policy_event_strength":80,"issuer_bridge_quality":55,"evidence_quality":50,"price_path_risk":35,"valuation_or_label_risk":45},"weighted_score_before":76.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"policy_event_strength":75,"issuer_bridge_quality":78,"evidence_quality":62,"price_path_risk":42,"valuation_or_label_risk":55},"weighted_score_after":83.0,"stage_label_after":"Stage2_or_Yellow_with_local_4B_overlay","changed_components":["issuer_bridge_quality","policy_label_penalty","price_path_risk_overlay"],"component_delta_explanation":"C31 policy event strength is not enough. Require issuer-level bridge and penalize policy-label-only rows with shallow MFE/deep MAE.","MFE_90D_pct":66.84,"MAE_90D_pct":-4.55,"MFE_180D_pct":152.67,"MAE_180D_pct":-4.55,"score_return_alignment_label":"improved_after_C31_policy_to_issuer_bridge_filter","current_profile_verdict":"current_profile_missed_direct_bridge_strength"}
{"row_type":"case","case_id":"C31-L101-05-003670","round":"R11","loop":101,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_STRATEGIC_INDUSTRY_POLICY_PACKAGE_TO_ISSUER_BRIDGE_V2","deep_sub_archetype_id":"C31_DEEP_SEMICONDUCTOR_ECOSYSTEM_VALUEUP_STRATEGIC_TECH_POLICY_LABEL_VS_VERIFIED_ISSUER_BRIDGE","symbol":"003670","company_name":"포스코퓨처엠","role":"counterexample","trigger_family":"battery_policy_label_without_customer_pull_bridge","source_event":"National strategic technology / battery supply-chain policy readthrough without near-term utilization or margin bridge","is_new_independent_case":true,"duplicate_check_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|003670|Stage2|2024-05-24","dedupe_for_aggregate":true,"calibration_usable":true}
{"row_type":"trigger","case_id":"C31-L101-05-003670","trigger_id":"C31_L101_T005_003670","round":"R11","loop":101,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_STRATEGIC_INDUSTRY_POLICY_PACKAGE_TO_ISSUER_BRIDGE_V2","deep_sub_archetype_id":"C31_DEEP_SEMICONDUCTOR_ECOSYSTEM_VALUEUP_STRATEGIC_TECH_POLICY_LABEL_VS_VERIFIED_ISSUER_BRIDGE","symbol":"003670","company_name":"포스코퓨처엠","role":"counterexample","trigger_type":"Stage2","trigger_date":"2024-05-23","entry_date":"2024-05-24","entry_price":258000.0,"evidence_available_at_that_date":"National strategic technology / battery supply-chain policy readthrough without near-term utilization or margin bridge","evidence_family":"battery_policy_label_without_customer_pull_bridge","evidence_note":"Strategic-tech policy label did not overcome EV demand slowdown and material-margin break; should route to local 4B/4C watch.","stage2_evidence_fields":["policy label","battery material exposure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["customer pull gap","material margin fade"],"stage4c_evidence_fields":["EV demand/material margin break"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003670/2024.csv","profile_path":"atlas/symbol_profiles/003/003670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":13.95,"MFE_90D_pct":13.95,"MFE_180D_pct":13.95,"MAE_30D_pct":-3.29,"MAE_90D_pct":-24.22,"MAE_180D_pct":-52.44,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_30D_date":"2024-06-11","trough_30D_date":"2024-05-31","peak_90D_date":"2024-06-11","trough_90D_date":"2024-08-05","peak_180D_date":"2024-06-11","trough_180D_date":"2025-02-10","drawdown_after_peak_pct":-52.44,"green_lateness_ratio":"not_applicable__policy_bridge_shadow_loop","four_b_local_peak_proximity":0.28,"four_b_full_window_peak_proximity":0.17,"four_b_timing_verdict":"local_4B_watch_required","four_b_evidence_type":["customer pull gap","material margin fade"],"four_c_protection_label":"hard_4C_candidate","trigger_outcome_label":"policy_label_false_positive_to_4C_watch","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"not_flagged_in_cached_tradable_sequence; profile-level validation required in batch","same_entry_group_id":"C31|003670|Stage2|2024-05-24","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":true}
{"row_type":"score_simulation","profile_id":"C31_policy_to_issuer_bridge_shadow_profile","case_id":"C31-L101-05-003670","trigger_id":"C31_L101_T005_003670","symbol":"003670","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"policy_event_strength":80,"issuer_bridge_quality":20,"evidence_quality":50,"price_path_risk":70,"valuation_or_label_risk":75},"weighted_score_before":76.0,"stage_label_before":"Stage2","raw_component_scores_after":{"policy_event_strength":75,"issuer_bridge_quality":18,"evidence_quality":30,"price_path_risk":80,"valuation_or_label_risk":85},"weighted_score_after":51.0,"stage_label_after":"Stage4B-Watch_or_Stage4C_candidate","changed_components":["issuer_bridge_quality","policy_label_penalty","price_path_risk_overlay"],"component_delta_explanation":"C31 policy event strength is not enough. Require issuer-level bridge and penalize policy-label-only rows with shallow MFE/deep MAE.","MFE_90D_pct":13.95,"MAE_90D_pct":-24.22,"MFE_180D_pct":13.95,"MAE_180D_pct":-52.44,"score_return_alignment_label":"improved_after_C31_policy_to_issuer_bridge_filter","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C31-L101-06-051910","round":"R11","loop":101,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_STRATEGIC_INDUSTRY_POLICY_PACKAGE_TO_ISSUER_BRIDGE_V2","deep_sub_archetype_id":"C31_DEEP_SEMICONDUCTOR_ECOSYSTEM_VALUEUP_STRATEGIC_TECH_POLICY_LABEL_VS_VERIFIED_ISSUER_BRIDGE","symbol":"051910","company_name":"LG화학","role":"counterexample","trigger_family":"battery_chemical_policy_label_without_margin_bridge","source_event":"Battery / strategic technology policy label without chemical spread or battery-material margin confirmation","is_new_independent_case":true,"duplicate_check_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|051910|Stage2|2024-05-24","dedupe_for_aggregate":true,"calibration_usable":true}
{"row_type":"trigger","case_id":"C31-L101-06-051910","trigger_id":"C31_L101_T006_051910","round":"R11","loop":101,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_STRATEGIC_INDUSTRY_POLICY_PACKAGE_TO_ISSUER_BRIDGE_V2","deep_sub_archetype_id":"C31_DEEP_SEMICONDUCTOR_ECOSYSTEM_VALUEUP_STRATEGIC_TECH_POLICY_LABEL_VS_VERIFIED_ISSUER_BRIDGE","symbol":"051910","company_name":"LG화학","role":"counterexample","trigger_type":"Stage2","trigger_date":"2024-05-23","entry_date":"2024-05-24","entry_price":386500.0,"evidence_available_at_that_date":"Battery / strategic technology policy label without chemical spread or battery-material margin confirmation","evidence_family":"battery_chemical_policy_label_without_margin_bridge","evidence_note":"The policy label did not repair chemical/battery material margin pressure; shallow MFE and deep MAE argue for local 4B and possible hard 4C if thesis break persists.","stage2_evidence_fields":["policy label","battery/chemical strategic-tech exposure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin pressure","weak customer-pull bridge"],"stage4c_evidence_fields":["persistent margin break"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/051/051910/2024.csv","profile_path":"atlas/symbol_profiles/051/051910.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.4,"MFE_90D_pct":4.4,"MFE_180D_pct":4.4,"MAE_30D_pct":-12.94,"MAE_90D_pct":-31.82,"MAE_180D_pct":-46.18,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_30D_date":"2024-05-24","trough_30D_date":"2024-06-28","peak_90D_date":"2024-05-24","trough_90D_date":"2024-08-05","peak_180D_date":"2024-05-24","trough_180D_date":"2025-02-10","drawdown_after_peak_pct":-46.18,"green_lateness_ratio":"not_applicable__policy_bridge_shadow_loop","four_b_local_peak_proximity":0.09,"four_b_full_window_peak_proximity":0.06,"four_b_timing_verdict":"local_4B_watch_required","four_b_evidence_type":["margin pressure","weak customer-pull bridge"],"four_c_protection_label":"hard_4C_candidate","trigger_outcome_label":"policy_label_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"not_flagged_in_cached_tradable_sequence; profile-level validation required in batch","same_entry_group_id":"C31|051910|Stage2|2024-05-24","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":true}
{"row_type":"score_simulation","profile_id":"C31_policy_to_issuer_bridge_shadow_profile","case_id":"C31-L101-06-051910","trigger_id":"C31_L101_T006_051910","symbol":"051910","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"policy_event_strength":80,"issuer_bridge_quality":20,"evidence_quality":50,"price_path_risk":70,"valuation_or_label_risk":75},"weighted_score_before":75.0,"stage_label_before":"Stage2","raw_component_scores_after":{"policy_event_strength":75,"issuer_bridge_quality":18,"evidence_quality":30,"price_path_risk":80,"valuation_or_label_risk":85},"weighted_score_after":49.0,"stage_label_after":"Stage4B-Watch_or_Stage4C_candidate","changed_components":["issuer_bridge_quality","policy_label_penalty","price_path_risk_overlay"],"component_delta_explanation":"C31 policy event strength is not enough. Require issuer-level bridge and penalize policy-label-only rows with shallow MFE/deep MAE.","MFE_90D_pct":4.4,"MAE_90D_pct":-31.82,"MFE_180D_pct":4.4,"MAE_180D_pct":-46.18,"score_return_alignment_label":"improved_after_C31_policy_to_issuer_bridge_filter","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C31-L101-07-323410","round":"R11","loop":101,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_STRATEGIC_INDUSTRY_POLICY_PACKAGE_TO_ISSUER_BRIDGE_V2","deep_sub_archetype_id":"C31_DEEP_SEMICONDUCTOR_ECOSYSTEM_VALUEUP_STRATEGIC_TECH_POLICY_LABEL_VS_VERIFIED_ISSUER_BRIDGE","symbol":"323410","company_name":"카카오뱅크","role":"counterexample","trigger_family":"valueup_policy_label_without_issuer_capital_return_bridge","source_event":"Corporate Value-up guidelines / low-PBR and capital-market policy label without ROE/CET1/capital-return bridge","is_new_independent_case":true,"duplicate_check_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|323410|Stage2|2024-05-24","dedupe_for_aggregate":true,"calibration_usable":true}
{"row_type":"trigger","case_id":"C31-L101-07-323410","trigger_id":"C31_L101_T007_323410","round":"R11","loop":101,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_STRATEGIC_INDUSTRY_POLICY_PACKAGE_TO_ISSUER_BRIDGE_V2","deep_sub_archetype_id":"C31_DEEP_SEMICONDUCTOR_ECOSYSTEM_VALUEUP_STRATEGIC_TECH_POLICY_LABEL_VS_VERIFIED_ISSUER_BRIDGE","symbol":"323410","company_name":"카카오뱅크","role":"counterexample","trigger_type":"Stage2","trigger_date":"2024-02-26","entry_date":"2024-05-24","entry_price":22900.0,"evidence_available_at_that_date":"Corporate Value-up guidelines / low-PBR and capital-market policy label without ROE/CET1/capital-return bridge","evidence_family":"valueup_policy_label_without_issuer_capital_return_bridge","evidence_note":"Value-up policy framework needed issuer-level capital-return execution. Without it, price path remained shallow and volatile.","stage2_evidence_fields":["value-up policy label","financial sector policy beta"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["generic low-PBR/value-up label"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv","profile_path":"atlas/symbol_profiles/323/323410.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.18,"MFE_90D_pct":2.84,"MFE_180D_pct":9.61,"MAE_30D_pct":-12.45,"MAE_90D_pct":-19.26,"MAE_180D_pct":-19.26,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_30D_date":"2024-05-27","trough_30D_date":"2024-06-27","peak_90D_date":"2024-07-23","trough_90D_date":"2024-08-05","peak_180D_date":"2024-12-16","trough_180D_date":"2024-08-05","drawdown_after_peak_pct":-19.26,"green_lateness_ratio":"not_applicable__policy_bridge_shadow_loop","four_b_local_peak_proximity":0.06,"four_b_full_window_peak_proximity":0.12,"four_b_timing_verdict":"local_4B_watch_required","four_b_evidence_type":["generic low-PBR/value-up label"],"four_c_protection_label":"4C_blocked_until_issuer_bridge_break","trigger_outcome_label":"valueup_label_false_positive","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"not_flagged_in_cached_tradable_sequence; profile-level validation required in batch","same_entry_group_id":"C31|323410|Stage2|2024-05-24","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":true}
{"row_type":"score_simulation","profile_id":"C31_policy_to_issuer_bridge_shadow_profile","case_id":"C31-L101-07-323410","trigger_id":"C31_L101_T007_323410","symbol":"323410","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"policy_event_strength":80,"issuer_bridge_quality":20,"evidence_quality":50,"price_path_risk":35,"valuation_or_label_risk":75},"weighted_score_before":74.0,"stage_label_before":"Stage2","raw_component_scores_after":{"policy_event_strength":75,"issuer_bridge_quality":18,"evidence_quality":30,"price_path_risk":42,"valuation_or_label_risk":85},"weighted_score_after":55.0,"stage_label_after":"Stage4B-Watch_or_Stage4C_candidate","changed_components":["issuer_bridge_quality","policy_label_penalty","price_path_risk_overlay"],"component_delta_explanation":"C31 policy event strength is not enough. Require issuer-level bridge and penalize policy-label-only rows with shallow MFE/deep MAE.","MFE_90D_pct":2.84,"MAE_90D_pct":-19.26,"MFE_180D_pct":9.61,"MAE_180D_pct":-19.26,"score_return_alignment_label":"improved_after_C31_policy_to_issuer_bridge_filter","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C31-L101-08-035720","round":"R11","loop":101,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_STRATEGIC_INDUSTRY_POLICY_PACKAGE_TO_ISSUER_BRIDGE_V2","deep_sub_archetype_id":"C31_DEEP_SEMICONDUCTOR_ECOSYSTEM_VALUEUP_STRATEGIC_TECH_POLICY_LABEL_VS_VERIFIED_ISSUER_BRIDGE","symbol":"035720","company_name":"카카오","role":"counterexample","trigger_family":"platform_valueup_policy_label_without_revenue_or_capital_bridge","source_event":"Corporate Value-up / platform governance policy readthrough without ad revenue or shareholder-return bridge","is_new_independent_case":true,"duplicate_check_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|035720|Stage2|2024-05-24","dedupe_for_aggregate":true,"calibration_usable":true}
{"row_type":"trigger","case_id":"C31-L101-08-035720","trigger_id":"C31_L101_T008_035720","round":"R11","loop":101,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_STRATEGIC_INDUSTRY_POLICY_PACKAGE_TO_ISSUER_BRIDGE_V2","deep_sub_archetype_id":"C31_DEEP_SEMICONDUCTOR_ECOSYSTEM_VALUEUP_STRATEGIC_TECH_POLICY_LABEL_VS_VERIFIED_ISSUER_BRIDGE","symbol":"035720","company_name":"카카오","role":"counterexample","trigger_type":"Stage2","trigger_date":"2024-02-26","entry_date":"2024-05-24","entry_price":45050.0,"evidence_available_at_that_date":"Corporate Value-up / platform governance policy readthrough without ad revenue or shareholder-return bridge","evidence_family":"platform_valueup_policy_label_without_revenue_or_capital_bridge","evidence_note":"Generic value-up/governance label could not substitute for platform ad revenue recovery or capital-return execution.","stage2_evidence_fields":["value-up policy label","platform governance readthrough"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["platform label","weak revenue bridge"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/035/035720/2024.csv","profile_path":"atlas/symbol_profiles/035/035720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.44,"MFE_90D_pct":3.44,"MFE_180D_pct":4.55,"MAE_30D_pct":-11.32,"MAE_90D_pct":-26.97,"MAE_180D_pct":-27.75,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_30D_date":"2024-05-27","trough_30D_date":"2024-07-02","peak_90D_date":"2024-05-27","trough_90D_date":"2024-09-09","peak_180D_date":"2024-12-04","trough_180D_date":"2024-11-14","drawdown_after_peak_pct":-27.75,"green_lateness_ratio":"not_applicable__policy_bridge_shadow_loop","four_b_local_peak_proximity":0.07,"four_b_full_window_peak_proximity":0.06,"four_b_timing_verdict":"local_4B_watch_required","four_b_evidence_type":["platform label","weak revenue bridge"],"four_c_protection_label":"4C_blocked_until_issuer_bridge_break","trigger_outcome_label":"policy_label_false_positive","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"not_flagged_in_cached_tradable_sequence; profile-level validation required in batch","same_entry_group_id":"C31|035720|Stage2|2024-05-24","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":true}
{"row_type":"score_simulation","profile_id":"C31_policy_to_issuer_bridge_shadow_profile","case_id":"C31-L101-08-035720","trigger_id":"C31_L101_T008_035720","symbol":"035720","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"policy_event_strength":80,"issuer_bridge_quality":20,"evidence_quality":50,"price_path_risk":70,"valuation_or_label_risk":75},"weighted_score_before":73.0,"stage_label_before":"Stage2","raw_component_scores_after":{"policy_event_strength":75,"issuer_bridge_quality":18,"evidence_quality":30,"price_path_risk":80,"valuation_or_label_risk":85},"weighted_score_after":53.0,"stage_label_after":"Stage4B-Watch_or_Stage4C_candidate","changed_components":["issuer_bridge_quality","policy_label_penalty","price_path_risk_overlay"],"component_delta_explanation":"C31 policy event strength is not enough. Require issuer-level bridge and penalize policy-label-only rows with shallow MFE/deep MAE.","MFE_90D_pct":3.44,"MAE_90D_pct":-26.97,"MFE_180D_pct":4.55,"MAE_180D_pct":-27.75,"score_return_alignment_label":"improved_after_C31_policy_to_issuer_bridge_filter","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"aggregate","aggregate_id":"C31_L101_AGG001","round":"R11","loop":101,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_STRATEGIC_INDUSTRY_POLICY_PACKAGE_TO_ISSUER_BRIDGE_V2","trigger_count":8,"representative_trigger_count":8,"positive_case_count":4,"counterexample_count":4,"stage4b_case_count":5,"stage4c_case_count":2,"current_profile_error_count":6,"pos_avg_MFE90":41.08,"pos_avg_MAE90":-21.3625,"pos_avg_MFE180":70.7525,"pos_avg_MAE180":-25.0975,"counter_avg_MFE90":6.1575,"counter_avg_MAE90":-25.5675,"counter_avg_MFE180":8.1275,"counter_avg_MAE180":-36.4075,"main_observation":"C31 policy events require issuer-level bridge. Policy-label-only rows show much weaker MFE and deeper MAE than verified bridge controls.","calibration_usable_count":8,"promotion_quality":"shadow_only; source_proxy rows require URL repair before promotion"}
{"row_type":"shadow_weight","axis":"C31_policy_to_issuer_bridge_filter_v2","scope":"canonical_archetype_specific","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","baseline_value":"Policy/subsidy/legislation event can contribute to Stage2/Yellow if broad policy significance is visible","tested_value":"Require issuer-level bridge before Yellow/Green: financing/tax-credit eligibility -> capex/order/revenue/margin/capital-return. Policy label only routes to local 4B or 4C watch when MFE stays shallow and MAE deepens.","delta":"+1 canonical bridge gate; no global Green threshold change","reason":"Positive controls have stronger MFE only when policy reaches the issuer through a direct bridge. Generic policy labels underperform.","backtest_effect":"positive avg MFE90 41.08 / MAE90 -21.3625 vs counter avg MFE90 6.1575 / MAE90 -25.5675","trigger_ids":["C31_L101_T001_000660","C31_L101_T002_042700","C31_L101_T003_034020","C31_L101_T004_064350","C31_L101_T005_003670","C31_L101_T006_051910","C31_L101_T007_323410","C31_L101_T008_035720"],"calibration_usable_count":8,"new_independent_case_count":8,"counterexample_count":4,"confidence":"medium","proposal_type":"canonical_shadow_only","notes":"Do not loosen Stage3-Green. C31 should be bridge-aware, not policy-headline-aware only."}
{"row_type":"residual_contribution","residual_id":"C31_L101_RES001","round":"R11","loop":101,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","residual_error_type":"policy_label_false_positive_vs_verified_issuer_bridge","current_profile_error_count":6,"false_positive_count":4,"too_early_hard_4c_count":0,"too_late_4B_4C_count":4,"proposed_handling":"Add canonical C31 policy-to-issuer bridge gate. Preserve policy positives only when issuer-level bridge exists; route label-only rows to local 4B or hard 4C watch depending on price path and thesis break.","coding_agent_action":"batch review only; no immediate production patch from this MD alone"}
```

## 15. Validation Scope

```text
validation_scope = C31 policy/subsidy/legislation event residual quality repair
calibration_usable_trigger_count = 8
representative_trigger_count = 8
positive_case_count = 4
counterexample_count = 4
stage4b_case_count = 5
stage4c_case_count = 2
source_proxy_only_count = 8
evidence_url_pending_count = 8
promotion_blocked_until_url_repair = true
production_scoring_changed = false
shadow_weight_only = true
```

## 16. Deferred Coding Agent Handoff Prompt

```text
You are the later-batch stock_agent coding agent. Do not treat this Markdown as an instruction to change production scoring immediately.

Task:
1. Ingest this C31 policy/subsidy/legislation residual MD with the broader v12 corpus.
2. Validate all trigger rows for required 30/90/180D MFE/MAE fields.
3. Repair evidence_url/source_proxy fields using MOEF, Reuters, FSC, and issuer-level disclosures where available.
4. If enough independent C31 rows accumulate, evaluate shadow axis `C31_policy_to_issuer_bridge_filter_v2`.
5. Do not loosen Stage3-Green thresholds globally.
6. Do not count broad government policy labels as verified positive bridges without issuer-level financing/order/revenue/margin/capital-return evidence.
7. Preserve production default unless batch promotion rules decide otherwise.
```

## 17. Next Research State

```text
completed_round = R11
completed_loop = 101
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality_repair_after_local_priority0_priority1_fill
next_recommended_archetypes = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP, C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE, R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW, R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL, C31_POLICY_SUBSIDY_LEGISLATION_EVENT
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
