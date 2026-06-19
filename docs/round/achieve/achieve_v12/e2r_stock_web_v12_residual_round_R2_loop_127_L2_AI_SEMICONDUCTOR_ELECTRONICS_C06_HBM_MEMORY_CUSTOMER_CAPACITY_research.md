# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```json
{
  "research_title": "E2R v12 Residual Calibration — C06 HBM customer/capacity bridge versus qualification delay",
  "selected_round": "R2",
  "selected_loop": 127,
  "selection_basis": "docs/core/V12_Research_No_Repeat_Index.md",
  "selected_priority_bucket": "Priority 0/1 quality repair — C06 URL/proxy repair, positive/counterexample balance, HBM customer qualification delay split; selected after avoiding the latest C07 equipment-order run",
  "round_schedule_status": "coverage_index_selected",
  "round_sector_consistency": "pass",
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
  "fine_archetype_id": "HBM_CUSTOMER_APPROVAL_CAPACITY_MIX_BRIDGE_VS_QUALIFICATION_DELAY",
  "loop_objective": "sector_specific_rule_discovery; canonical_archetype_rule_candidate; counterexample_mining; 4C_thesis_break_timing_test; URL_proxy_quality_repair; complete_30_90_180_MFE_MAE",
  "price_source": "Songdaiki/stock-web",
  "stock_web_manifest_max_date": "2026-02-20",
  "new_independent_case_count": 6,
  "reused_case_count": 0,
  "same_archetype_new_symbol_count": 3,
  "same_archetype_new_trigger_family_count": 6,
  "calibration_usable_case_count": 6,
  "calibration_usable_trigger_count": 6,
  "positive_case_count": 4,
  "counterexample_count": 2,
  "stage4b_or_4c_case_count": 2,
  "source_proxy_only_count": 0,
  "evidence_url_pending_count": 0,
  "rows_missing_required_mfe_mae": 0,
  "current_profile_error_count": 4,
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "new_axis_proposed": "C06_HBM_CUSTOMER_APPROVAL_CAPACITY_BRIDGE_GATE"
}
```

- output_file: `e2r_stock_web_v12_residual_round_R2_loop_127_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md`
- stock_agent_code_accessed: false
- stock_agent_code_patched: false
- live_current_discovery: false
- production_scoring_changed: false
- shadow_weight_only: true

## 1. Current Calibrated Profile Assumption

This MD assumes the already-calibrated Stock-Web profile described in the execution prompt: Stage2 requires non-price bridge evidence, Stage3-Green remains strict, price-only blowoff cannot promote a positive stage, full 4B needs non-price evidence, and hard thesis breaks route to 4C. This run does **not** re-propose those global axes. It only tests a C06-specific residue: HBM customer/capacity evidence is unusually binary. Once a named customer supply or mass-production bridge is real, the right tail can be large. When qualification is delayed, generic AI-memory demand can become a false comfort blanket.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| selected_round | R2 |
| selected_loop | 127 |
| large_sector_id | L2_AI_SEMICONDUCTOR_ELECTRONICS |
| canonical_archetype_id | C06_HBM_MEMORY_CUSTOMER_CAPACITY |
| fine_archetype_id | HBM_CUSTOMER_APPROVAL_CAPACITY_MIX_BRIDGE_VS_QUALIFICATION_DELAY |
| round_schedule_status | coverage_index_selected |
| round_sector_consistency | pass |
| selection_basis | docs/core/V12_Research_No_Repeat_Index.md |

C06 belongs to R2/L2 by the canonical mapping. The latest visible root listing shows prior C06 files through R2 loop 126, so this file uses loop 127 for the same R2/C06 pair.

## 3. Previous Coverage / Duplicate Avoidance Check

The current no-repeat ledger reports 11,200 representative rows, 962 unique symbols, 36 covered canonical scopes, and a quality-repair phase rather than a simple row-count phase. It also flags large direct-URL and proxy-only repair needs. C06 has 215 representative rows across 58 symbols, with 28 positives, 54 counterexamples, and only 7 4C rows. That makes C06 useful for a qualification-delay / customer-capacity split rather than another generic AI-memory winner.

Recent visible outputs avoided in this execution: C05, C01, C13, C15, C10, C02, C16, R13 high-MAE, C17, C07. The duplicate key used here is `canonical_archetype_id + symbol + trigger_date + entry_date + evidence_family`. This MD uses 6 trigger families and no reused trigger-date/entry-date rows.

## 4. Stock-Web OHLC Input / Price Source Validation

| item | value |
|---|---|
| price_data_source | Songdaiki/stock-web |
| upstream_source | FinanceData/marcap |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| manifest_max_date | 2026-02-20 |
| schema | atlas/schema.json |

All trigger rows below use actual Stock-Web shard rows cached from the raw GitHub atlas. Each trigger has an entry close, complete 30D/90D/180D MFE and MAE, and a clean 180D corporate-action window under the symbol profiles.

## 5. Historical Eligibility Gate

| gate | result |
|---|---|
| trigger_date is historical | pass |
| entry_date exists in tradable shard | pass |
| entry_price present and positive | pass |
| forward 180 trading rows available | pass for all 6 rows |
| MFE_30D/90D/180D present | pass |
| MAE_30D/90D/180D present | pass |
| 180D corporate-action contamination | clean for all selected windows |
| live discovery | not used |
| production scoring change | none |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep path tested | scoring implication |
|---|---|---|
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | HBM3E sample / customer verification | Stage2-Actionable only until mass production or customer supply is explicit |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | HBM3E mass production / Nvidia supply | Stage3-Green can unlock if capacity, customer, and revision bridge align |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | 12-layer HBM3E follow-on capacity | Positive but late-entry MAE/valuation gate needed |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | HBM3E qualification delay | Stage4B overlay, not generic Stage2 optimism |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | major customer delay + profit miss | hard 4C customer-capacity thesis break |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | HBM-adjacent AI/server substrate | Stage2-Actionable cap until direct memory customer approval is proven |

## 7. Case Selection Summary

|case|symbol|company|trigger_type|trigger_date|entry_date|classification|MFE90|MAE90|MFE180|MAE180|verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|
|C06-127-001|000660|SK하이닉스|Stage2-Actionable|2023-08-21|2023-08-22|positive|23.35|-3.61|66.52|-3.61|customer_sample_bridge_positive|
|C06-127-002|000660|SK하이닉스|Stage3-Green|2024-03-19|2024-03-19|positive|55.12|-3.81|55.12|-9.68|mass_production_customer_supply_positive|
|C06-127-003|000660|SK하이닉스|Stage3-Green|2024-09-26|2024-09-27|positive_late|23.5|-14.25|62.4|-14.25|capacity_density_follow_on_positive_with_late_entry_risk|
|C06-127-004|005930|삼성전자|Stage4B|2024-05-24|2024-05-24|counterexample|17.0|-21.61|17.0|-34.26|qualification_delay_4b_counterexample|
|C06-127-005|005930|삼성전자|Stage4C|2024-10-08|2024-10-08|counterexample|1.82|-17.25|7.3|-17.25|major_customer_delay_profit_miss_4c|
|C06-127-006|009150|삼성전기|Stage2-Actionable|2024-10-29|2024-10-29|capped_positive|24.63|-12.23|24.63|-12.23|hbm_adjacent_substrate_positive_green_cap|


## 8. Positive vs Counterexample Balance

| metric | value |
|---|---:|
| calibration_usable_trigger_count | 6 |
| positive_case_count | 4 |
| counterexample_count | 2 |
| Stage4B rows | 1 |
| Stage4C rows | 1 |
| source_proxy_only_count | 0 |
| evidence_url_pending_count | 0 |
| current_profile_error_count | 4 |

The split is deliberately asymmetric: SK hynix validates the positive right-tail path, Samsung Electronics supplies the qualification-delay and hard-4C path, and Samsung Electro-Mechanics marks the boundary where AI/server substrate evidence is real but not enough to become direct HBM memory customer capacity evidence.

## 9. Evidence Source Map

| case_id | evidence family | source | directness | interpretation |
|---|---|---|---|---|
| C06-127-001 | HBM3E_NVIDIA_SAMPLE_VERIFICATION | https://koreajoongangdaily.joins.com/news/2023-08-21/business/industry/SK-hynix-aims-for-top-AI-memory-chip-HBM3E-with-help-from-Nvidia/1849608 | named-company media URL | sample/customer verification bridge; Stage2 only |
| C06-127-002 | HBM3E_8_LAYER_MASS_PRODUCTION_NVIDIA_SUPPLY | https://www.reuters.com/technology/nvidia-supplier-sk-hynix-begins-mass-production-next-generation-memory-chip-2024-03-19/ | Reuters with SK hynix statement | mass-production/customer-supply bridge |
| C06-127-003 | HBM3E_12_LAYER_MASS_PRODUCTION_CAPACITY_DENSITY | https://en.yna.co.kr/view/AEN20240926002700320 | Yonhap with SK hynix statement | follow-on capacity/density proof; late-entry risk |
| C06-127-004 | HBM3E_NVIDIA_QUALIFICATION_DELAY_HEAT_POWER | https://www.reuters.com/technology/samsungs-hbm-chips-failing-nvidia-tests-due-heat-power-consumption-woes-sources-2024-05-23/ | Reuters exclusive with Samsung response | 4B risk overlay |
| C06-127-005 | HBM3E_MAJOR_CUSTOMER_SALES_DELAY_Q3_PROFIT_MISS | https://www.reuters.com/technology/samsung-electronics-estimates-274-jump-q3-operating-profit-2024-10-07/ | Reuters with Samsung statement | hard 4C confirmation |
| C06-127-006 | AI_SERVER_FCBGA_SUBSTRATE_SUPPLY_MIX | https://samsungsem.com/global/newsroom/news/view.do?id=8642 | company official release | real AI/server substrate bridge, but HBM-adjacent cap |

## 10. Price Data Source Map

| symbol | company | profile_path | entry-year shard(s) used | corporate-action window |
|---|---|---|---|---|
| 000660 | SK hynix | atlas/symbol_profiles/000/000660.json | atlas/ohlcv_tradable_by_symbol_year/000/000660/2023.csv; 2024.csv; 2025.csv | clean for selected 180D windows |
| 005930 | Samsung Electronics | atlas/symbol_profiles/005/005930.json | atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv; 2025.csv | clean for selected 180D windows |
| 009150 | Samsung Electro-Mechanics | atlas/symbol_profiles/009/009150.json | atlas/ohlcv_tradable_by_symbol_year/009/009150/2024.csv; 2025.csv | clean for selected 180D windows |

## 11. Case-by-Case Trigger Grid

|case|symbol|company|trigger_type|trigger_date|entry_date|classification|verdict|
|---|---|---|---|---|---|---|---|
|C06-127-001|000660|SK하이닉스|Stage2-Actionable|2023-08-21|2023-08-22|positive|customer_sample_bridge_positive|
|C06-127-002|000660|SK하이닉스|Stage3-Green|2024-03-19|2024-03-19|positive|mass_production_customer_supply_positive|
|C06-127-003|000660|SK하이닉스|Stage3-Green|2024-09-26|2024-09-27|positive_late|capacity_density_follow_on_positive_with_late_entry_risk|
|C06-127-004|005930|삼성전자|Stage4B|2024-05-24|2024-05-24|counterexample|qualification_delay_4b_counterexample|
|C06-127-005|005930|삼성전자|Stage4C|2024-10-08|2024-10-08|counterexample|major_customer_delay_profit_miss_4c|
|C06-127-006|009150|삼성전기|Stage2-Actionable|2024-10-29|2024-10-29|capped_positive|hbm_adjacent_substrate_positive_green_cap|


## 12. Trigger-Level OHLC Backtest Tables

`30D`, `90D`, and `180D` columns are `MFE_pct / MAE_pct` using Stock-Web high/low paths from the entry close.

|trigger_id|symbol|entry|30D|90D|180D|peak|drawdown_after_peak|
|---|---|---|---|---|---|---|---|
|C06-127-T001|000660|2023-08-22 @ 116500|6.78 / -3.61|23.35 / -3.61|66.52 / -3.61|2024-05-16 / 194000|-2.78|
|C06-127-T002|000660|2024-03-19 @ 160200|19.48 / -3.81|55.12 / -3.81|55.12 / -9.68|2024-07-11 / 248500|-41.77|
|C06-127-T003|000660|2024-09-27 @ 183800|12.08 / -8.0|23.5 / -14.25|62.4 / -14.25|2025-06-26 / 298500|-5.86|
|C06-127-T004|005930|2024-05-24 @ 75900|14.76 / -3.16|17.0 / -21.61|17.0 / -34.26|2024-07-11 / 88800|-43.81|
|C06-127-T005|005930|2024-10-08 @ 60300|1.82 / -17.25|1.82 / -17.25|7.3 / -17.25|2025-07-04 / 64700|-2.63|
|C06-127-T006|009150|2024-10-29 @ 120200|1.83 / -12.23|24.63 / -12.23|24.63 / -12.23|2025-02-17 / 149800|-27.37|


## 13. Current Calibrated Profile Stress Test

| trigger_id | current profile behavior | residual error |
|---|---|---|
| C06-127-T001 | Correct Stage2-Actionable: customer sample bridge is real but not mass-production proof | no error; Green should remain locked |
| C06-127-T002 | Correct Green: mass production + Nvidia shipment + booked capacity bridge | no error |
| C06-127-T003 | Directionally correct positive, but follow-on capacity after a large run needs MAE/valuation gating | late-entry risk under-penalized |
| C06-127-T004 | Generic AI/HBM demand could wrongly offset customer qualification delay | false positive risk without 4B overlay |
| C06-127-T005 | Customer delay + profit miss requires hard 4C even before price fully validates | 4C timing needs earlier confirmation |
| C06-127-T006 | Real AI/server substrate evidence can justify Stage2, but not direct HBM Green | HBM adjacency overpromotion risk |

## 14. Stage2 / Yellow / Green Comparison

C06 is a switchboard archetype. A sample shipment is a wire touching the terminal; mass production and customer shipment are current flowing through it. Stage2 can start when the wire touches, but Green should wait until current actually flows: named customer supply, capacity allocation, and earnings/revision bridge.

| stage | allowed C06 evidence | blocked C06 evidence |
|---|---|---|
| Stage2 | named HBM sample, customer qualification in progress, capacity preparation | generic AI-memory demand only |
| Stage2-Actionable | sample + named customer / explicit capacity plan / near-term production target | HBM-adjacent substrate with no memory customer approval |
| Stage3-Yellow | production started but late-entry valuation/MAE risk remains | follow-on capacity headline after large price run |
| Stage3-Green | mass production + named customer shipment + capacity booked + margin/revision bridge | qualification not passed or sales delayed |
| Stage4B | customer qualification delay, heat/power issue, price already credits success | none |
| Stage4C | delayed major-customer HBM3E sales + profit miss / customer-capacity thesis break | mere rumor without company/Reuters-quality confirmation |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | four_b_evidence_type | timing verdict | 180D price path |
|---|---|---|---|
| C06-127-T004 | contract_delay / customer_quality_delay / positioning_overheat | good risk overlay before 180D drawdown | +17.0% MFE180 vs -34.26% MAE180 |
| C06-127-T005 | contract_delay / revision_slowdown / margin_or_backlog_slowdown | 4B watch hardened to 4C | +7.3% MFE180 vs -17.25% MAE180 |

The May Samsung row is not price-only 4B. It has non-price evidence: customer qualification delay, heat/power issue reports, and Samsung's own optimization-response frame. The October row is a 4C because delayed HBM3E sales and disappointing profit hit the evidence bridge directly.

## 16. 4C Protection Audit

| trigger_id | label | protection interpretation |
|---|---|---|
| C06-127-T005 | hard_4c_success | Entry after the profit/customer-delay warning avoided treating a weak rebound as structural rerating. MAE180 was -17.25%, while MFE180 was only +7.30%. |
| C06-127-T004 | thesis_break_watch_only | May signal was early 4B rather than hard 4C; subsequent October evidence completed the thesis break. |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
axis = L2_HBM_CUSTOMER_APPROVAL_AND_CAPACITY_BRIDGE_GATE
production_scoring_changed = false
shadow_weight_only = true
```

In L2, HBM-related evidence should not be scored like ordinary memory-cycle recovery. Named customer qualification and capacity allocation carry more signal than generic AI memory demand. The proposed sector rule: when an HBM memory name or HBM-adjacent component is scored, require at least two of the following before Stage3-Green: named customer approval or shipment, explicit mass production, capacity sold out or allocation, mix/ASP/revision bridge, or company-level profit bridge. If qualification delay or major-customer sales delay appears, route to 4B/4C before price validation finishes.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C06_HBM_MEMORY_CUSTOMER_CAPACITY
axis = C06_HBM_CUSTOMER_APPROVAL_CAPACITY_BRIDGE_GATE
```

C06-specific gate:

1. `Stage2-Actionable` requires named customer qualification, shipment, or explicit near-term mass-production evidence.
2. `Stage3-Green` requires at least two live bridges: customer supply/approval, mass production, capacity allocation, margin/revision proof.
3. HBM-adjacent substrate / AI-server package evidence is capped at Stage2-Actionable unless it directly links to memory customer approval or HBM package capacity.
4. Qualification delay, heat/power issue, or major-customer sales delay is non-price 4B/4C evidence.
5. Late follow-on capacity headlines after a large run get MAE/valuation gating even when the technology evidence is true.

## 19. Before / After Backtest Comparison

|profile_id|profile_scope|eligible_trigger_count|avg_MFE_90D_pct|avg_MAE_90D_pct|avg_MFE_180D_pct|avg_MAE_180D_pct|false_positive_rate|late_green_count|score_return_alignment_verdict|
|---|---|---|---|---|---|---|---|---|---|
|P0_e2r_2_1_stock_web_calibrated_proxy|baseline_current|6|24.24|-12.13|38.83|-15.21|0.33|1|improves_false_positive_filter_without_killing_SK_hynix_positive|
|P0b_e2r_2_0_baseline_reference|rollback_reference|4|31.65|-8.47|52.17|-9.94|0.5|2|overcredits_generic_AI_memory|
|P1_L2_sector_candidate|sector_specific|6|24.24|-12.13|38.83|-15.21|0.17|0|improves_false_positive_filter_without_killing_SK_hynix_positive|
|P2_C06_canonical_candidate|canonical_archetype_specific|6|24.24|-12.13|38.83|-15.21|0.17|0|improves_false_positive_filter_without_killing_SK_hynix_positive|
|P3_counterexample_guard|guard_profile|2|9.41|-19.43|12.15|-25.75|0.17|0|improves_false_positive_filter_without_killing_SK_hynix_positive|


## 20. Score-Return Alignment Matrix

| row | before | after | reason |
|---|---|---|---|
| SK hynix sample bridge | Stage2-Actionable | Stage2-Actionable | sample/customer evidence is real but production not yet confirmed |
| SK hynix 8L mass production | Stage3-Green | Stage3-Green | named supply and booked capacity bridge supported large MFE |
| SK hynix 12L follow-on | Stage3-Green | Stage3-Yellow/Green with MAE gate | technology true, but follow-on after run has higher late-entry drawdown risk |
| Samsung May delay | Stage2 false-positive risk | Stage4B | qualification delay is non-price risk evidence |
| Samsung Oct delay/profit miss | Stage2/Watch false-positive risk | Stage4C | major customer sales delay + profit miss is thesis break |
| Samsung Electro-Mechanics substrate | Stage2-Actionable/possible Green overcredit | Stage2-Actionable cap | AI/server FCBGA is adjacent; direct HBM customer capacity missing |

## 21. Coverage Matrix

| contribution | count |
|---|---:|
| new independent trigger rows | 6 |
| distinct symbols in this MD | 3 |
| distinct trigger families | 6 |
| positives | 4 |
| counterexamples | 2 |
| 4B rows | 1 |
| 4C rows | 1 |
| rows with complete 30/90/180 MFE/MAE | 6 |
| source URLs pending | 0 |
| source_proxy_only | 0 |

## 22. Residual Contribution Summary

```text
This loop adds 6 new independent trigger-family cases, 2 counterexamples, and 4 residual profile stress cases for R2/L2/C06.
loop_contribution_label = C06_customer_approval_capacity_bridge_vs_qualification_delay_quality_repair
do_not_propose_new_weight_delta = false
```

Residual errors found:

- `HBM_customer_qualification_delay_overcredit`
- `HBM_adjacency_green_overpromotion`
- `late_capacity_follow_on_MAE_risk`
- `hard_4c_needed_when_customer_delay_and_profit_miss_align`

## 23. Validation Scope / Non-Validation Scope

Validated:

- historical evidence dates,
- Stock-Web entry close rows,
- complete 30D/90D/180D MFE and MAE,
- clean 180D corporate-action windows based on profile candidate dates,
- stage label canonicalization,
- filename/metadata consistency.

Not validated:

- production scoring code behavior,
- live current candidates,
- brokerage/API feasibility,
- future post-2026-02-20 prices,
- exact customer contract volumes beyond public evidence.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C06_HBM_CUSTOMER_APPROVAL_CAPACITY_BRIDGE_GATE,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,24/21/19/15/12/4/5,24/23/21/13/10/4/5,0/+2/+2/-2/-2/0/0,raise visibility/customer-quality weight but reduce generic valuation/mispricing credit,filters Samsung qualification false positive while preserving SK hynix mass-production winners,C06-127-T001|C06-127-T002|C06-127-T003|C06-127-T004|C06-127-T005|C06-127-T006 ,6,6,2,medium,canonical_shadow_only,not production; post-calibrated residual
```

Interpretation: increase visibility/customer quality inside C06, reduce generic valuation/repricing and relative-strength credit when customer approval or mass production is missing. This is not a production patch.

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "C06-127-001", "symbol": "000660", "company_name": "SK hynix", "round": "R2", "loop": 127, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "HBM_CUSTOMER_APPROVAL_CAPACITY_MIX_BRIDGE_VS_QUALIFICATION_DELAY", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "C06-127-T001", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "current_profile_correct_but_green_should_wait_for_mass_production", "current_profile_verdict": "current_profile_correct_but_green_should_wait_for_mass_production", "price_source": "Songdaiki/stock-web", "notes": "HBM3E_NVIDIA_SAMPLE_VERIFICATION"}
{"row_type": "case", "case_id": "C06-127-002", "symbol": "000660", "company_name": "SK hynix", "round": "R2", "loop": 127, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "HBM_CUSTOMER_APPROVAL_CAPACITY_MIX_BRIDGE_VS_QUALIFICATION_DELAY", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "C06-127-T002", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "current_profile_correct_green_with_drawdown_aware_hold", "current_profile_verdict": "current_profile_correct_green_with_drawdown_aware_hold", "price_source": "Songdaiki/stock-web", "notes": "HBM3E_8_LAYER_MASS_PRODUCTION_NVIDIA_SUPPLY"}
{"row_type": "case", "case_id": "C06-127-003", "symbol": "000660", "company_name": "SK hynix", "round": "R2", "loop": 127, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "HBM_CUSTOMER_APPROVAL_CAPACITY_MIX_BRIDGE_VS_QUALIFICATION_DELAY", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "C06-127-T003", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "current_profile_partly_too_permissive_if_late_valuation_not_penalized", "current_profile_verdict": "current_profile_partly_too_permissive_if_late_valuation_not_penalized", "price_source": "Songdaiki/stock-web", "notes": "HBM3E_12_LAYER_MASS_PRODUCTION_CAPACITY_DENSITY"}
{"row_type": "case", "case_id": "C06-127-004", "symbol": "005930", "company_name": "Samsung Electronics", "round": "R2", "loop": 127, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "HBM_CUSTOMER_APPROVAL_CAPACITY_MIX_BRIDGE_VS_QUALIFICATION_DELAY", "case_type": "counterexample_or_thesis_break", "positive_or_counterexample": "counterexample", "best_trigger": "C06-127-T004", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "current_profile_too_permissive_if_generic_hbm_demand_offsets_customer_delay", "current_profile_verdict": "current_profile_too_permissive_if_generic_hbm_demand_offsets_customer_delay", "price_source": "Songdaiki/stock-web", "notes": "HBM3E_NVIDIA_QUALIFICATION_DELAY_HEAT_POWER"}
{"row_type": "case", "case_id": "C06-127-005", "symbol": "005930", "company_name": "Samsung Electronics", "round": "R2", "loop": 127, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "HBM_CUSTOMER_APPROVAL_CAPACITY_MIX_BRIDGE_VS_QUALIFICATION_DELAY", "case_type": "counterexample_or_thesis_break", "positive_or_counterexample": "counterexample", "best_trigger": "C06-127-T005", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "current_profile_needs_hard_4c_confirmation_before_price_validation", "current_profile_verdict": "current_profile_needs_hard_4c_confirmation_before_price_validation", "price_source": "Songdaiki/stock-web", "notes": "HBM3E_MAJOR_CUSTOMER_SALES_DELAY_Q3_PROFIT_MISS"}
{"row_type": "case", "case_id": "C06-127-006", "symbol": "009150", "company_name": "Samsung Electro-Mechanics", "round": "R2", "loop": 127, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "HBM_CUSTOMER_APPROVAL_CAPACITY_MIX_BRIDGE_VS_QUALIFICATION_DELAY", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "C06-127-T006", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "stage2_ok_but_green_cap_until_direct_memory_customer_capacity_bridge", "current_profile_verdict": "stage2_ok_but_green_cap_until_direct_memory_customer_capacity_bridge", "price_source": "Songdaiki/stock-web", "notes": "AI_SERVER_FCBGA_SUBSTRATE_SUPPLY_MIX"}
{"row_type": "trigger", "trigger_id": "C06-127-T001", "case_id": "C06-127-001", "symbol": "000660", "company_name": "SK hynix", "round": "R2", "loop": 127, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "HBM_CUSTOMER_APPROVAL_CAPACITY_MIX_BRIDGE_VS_QUALIFICATION_DELAY", "sector": "AI/Semiconductor/Electronics", "primary_archetype": "HBM customer/capacity bridge", "loop_objective": "sector_specific_rule_discovery; canonical_archetype_rule_candidate; counterexample_mining; 4C_thesis_break_timing_test; URL_proxy_quality_repair; complete_30_90_180_MFE_MAE", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-08-21", "evidence_available_at_that_date": "SK hynix shipped HBM3E samples to clients including Nvidia and targeted 1H24 mass production. This is a named-customer verification bridge before mass-production confirmation.", "evidence_source": "https://koreajoongangdaily.joins.com/news/2023-08-21/business/industry/SK-hynix-aims-for-top-AI-memory-chip-HBM3E-with-help-from-Nvidia/1849608", "stage2_evidence_fields": ["HBM3E_NVIDIA_SAMPLE_VERIFICATION"], "stage3_evidence_fields": ["mass_production", "customer_supply", "capacity_or_mix_bridge"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000660/2023.csv", "profile_path": "atlas/symbol_profiles/000/000660.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-08-22", "entry_price": 116500.0, "MFE_30D_pct": 6.78, "MFE_90D_pct": 23.35, "MFE_180D_pct": 66.52, "MFE_1Y_pct": 113.3, "MFE_2Y_pct": 203.86, "MAE_30D_pct": -3.61, "MAE_90D_pct": -3.61, "MAE_180D_pct": -3.61, "MAE_1Y_pct": -3.61, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-16", "peak_price": 194000.0, "drawdown_after_peak_pct": -2.78, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": null, "four_c_protection_label": null, "trigger_outcome_label": "customer_sample_bridge_positive", "current_profile_verdict": "current_profile_correct_but_green_should_wait_for_mass_production", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY|000660|2023-08-22", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C06-127-T002", "case_id": "C06-127-002", "symbol": "000660", "company_name": "SK hynix", "round": "R2", "loop": 127, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "HBM_CUSTOMER_APPROVAL_CAPACITY_MIX_BRIDGE_VS_QUALIFICATION_DELAY", "sector": "AI/Semiconductor/Electronics", "primary_archetype": "HBM customer/capacity bridge", "loop_objective": "sector_specific_rule_discovery; canonical_archetype_rule_candidate; counterexample_mining; 4C_thesis_break_timing_test; URL_proxy_quality_repair; complete_30_90_180_MFE_MAE", "trigger_type": "Stage3-Green", "trigger_date": "2024-03-19", "evidence_available_at_that_date": "SK hynix began mass production of HBM3E; Reuters reported initial shipments to Nvidia and fully booked 2024 HBM capacity. This converts the sample bridge into customer-supply capacity evidence.", "evidence_source": "https://www.reuters.com/technology/nvidia-supplier-sk-hynix-begins-mass-production-next-generation-memory-chip-2024-03-19/", "stage2_evidence_fields": ["HBM3E_8_LAYER_MASS_PRODUCTION_NVIDIA_SUPPLY"], "stage3_evidence_fields": ["mass_production", "customer_supply", "capacity_or_mix_bridge"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv", "profile_path": "atlas/symbol_profiles/000/000660.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-19", "entry_price": 160200.0, "MFE_30D_pct": 19.48, "MFE_90D_pct": 55.12, "MFE_180D_pct": 55.12, "MFE_1Y_pct": 55.12, "MFE_2Y_pct": null, "MAE_30D_pct": -3.81, "MAE_90D_pct": -3.81, "MAE_180D_pct": -9.68, "MAE_1Y_pct": -9.68, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-11", "peak_price": 248500.0, "drawdown_after_peak_pct": -41.77, "green_lateness_ratio": 0.65, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": null, "four_c_protection_label": null, "trigger_outcome_label": "mass_production_customer_supply_positive", "current_profile_verdict": "current_profile_correct_green_with_drawdown_aware_hold", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY|000660|2024-03-19", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C06-127-T003", "case_id": "C06-127-003", "symbol": "000660", "company_name": "SK hynix", "round": "R2", "loop": 127, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "HBM_CUSTOMER_APPROVAL_CAPACITY_MIX_BRIDGE_VS_QUALIFICATION_DELAY", "sector": "AI/Semiconductor/Electronics", "primary_archetype": "HBM customer/capacity bridge", "loop_objective": "sector_specific_rule_discovery; canonical_archetype_rule_candidate; counterexample_mining; 4C_thesis_break_timing_test; URL_proxy_quality_repair; complete_30_90_180_MFE_MAE", "trigger_type": "Stage3-Green", "trigger_date": "2024-09-26", "evidence_available_at_that_date": "SK hynix began mass production of 12-layer HBM3E and said the chip would be supplied to customers including Nvidia within the year. This is follow-on density/capacity confirmation, but not a first trigger.", "evidence_source": "https://en.yna.co.kr/view/AEN20240926002700320", "stage2_evidence_fields": ["HBM3E_12_LAYER_MASS_PRODUCTION_CAPACITY_DENSITY"], "stage3_evidence_fields": ["mass_production", "customer_supply", "capacity_or_mix_bridge"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv", "profile_path": "atlas/symbol_profiles/000/000660.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-09-27", "entry_price": 183800.0, "MFE_30D_pct": 12.08, "MFE_90D_pct": 23.5, "MFE_180D_pct": 62.4, "MFE_1Y_pct": 138.98, "MFE_2Y_pct": null, "MAE_30D_pct": -8.0, "MAE_90D_pct": -14.25, "MAE_180D_pct": -14.25, "MAE_1Y_pct": -14.25, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-06-26", "peak_price": 298500.0, "drawdown_after_peak_pct": -5.86, "green_lateness_ratio": 0.81, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": null, "four_c_protection_label": null, "trigger_outcome_label": "capacity_density_follow_on_positive_with_late_entry_risk", "current_profile_verdict": "current_profile_partly_too_permissive_if_late_valuation_not_penalized", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY|000660|2024-09-27", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C06-127-T004", "case_id": "C06-127-004", "symbol": "005930", "company_name": "Samsung Electronics", "round": "R2", "loop": 127, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "HBM_CUSTOMER_APPROVAL_CAPACITY_MIX_BRIDGE_VS_QUALIFICATION_DELAY", "sector": "AI/Semiconductor/Electronics", "primary_archetype": "HBM customer/capacity bridge", "loop_objective": "sector_specific_rule_discovery; canonical_archetype_rule_candidate; counterexample_mining; 4C_thesis_break_timing_test; URL_proxy_quality_repair; complete_30_90_180_MFE_MAE", "trigger_type": "Stage4B", "trigger_date": "2024-05-24", "evidence_available_at_that_date": "Reuters reported Samsung latest HBM chips had not yet passed Nvidia tests because of heat/power concerns; Samsung said customer optimization was ongoing. This is a 4B overlay against generic AI-memory optimism.", "evidence_source": "https://www.reuters.com/technology/samsungs-hbm-chips-failing-nvidia-tests-due-heat-power-consumption-woes-sources-2024-05-23/", "stage2_evidence_fields": ["HBM3E_NVIDIA_QUALIFICATION_DELAY_HEAT_POWER"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["HBM3E_NVIDIA_QUALIFICATION_DELAY_HEAT_POWER"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv", "profile_path": "atlas/symbol_profiles/005/005930.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-24", "entry_price": 75900.0, "MFE_30D_pct": 14.76, "MFE_90D_pct": 17.0, "MFE_180D_pct": 17.0, "MFE_1Y_pct": 17.0, "MFE_2Y_pct": null, "MAE_30D_pct": -3.16, "MAE_90D_pct": -21.61, "MAE_180D_pct": -34.26, "MAE_1Y_pct": -34.26, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-11", "peak_price": 88800.0, "drawdown_after_peak_pct": -43.81, "green_lateness_ratio": null, "four_b_local_peak_proximity": 0.7, "four_b_full_window_peak_proximity": 0.7, "four_b_timing_verdict": "good_risk_overlay_before_180D_drawdown", "four_b_evidence_type": "contract_delay|positioning_overheat|customer_quality_delay", "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "qualification_delay_4b_counterexample", "current_profile_verdict": "current_profile_too_permissive_if_generic_hbm_demand_offsets_customer_delay", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY|005930|2024-05-24", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C06-127-T005", "case_id": "C06-127-005", "symbol": "005930", "company_name": "Samsung Electronics", "round": "R2", "loop": 127, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "HBM_CUSTOMER_APPROVAL_CAPACITY_MIX_BRIDGE_VS_QUALIFICATION_DELAY", "sector": "AI/Semiconductor/Electronics", "primary_archetype": "HBM customer/capacity bridge", "loop_objective": "sector_specific_rule_discovery; canonical_archetype_rule_candidate; counterexample_mining; 4C_thesis_break_timing_test; URL_proxy_quality_repair; complete_30_90_180_MFE_MAE", "trigger_type": "Stage4C", "trigger_date": "2024-10-08", "evidence_available_at_that_date": "Samsung warned Q3 profit would miss expectations and said high-end HBM3E sales to a major customer were delayed versus expectations. This hardens the May 4B watch into a 4C customer-qualification/profit bridge break.", "evidence_source": "https://www.reuters.com/technology/samsung-electronics-estimates-274-jump-q3-operating-profit-2024-10-07/", "stage2_evidence_fields": ["HBM3E_MAJOR_CUSTOMER_SALES_DELAY_Q3_PROFIT_MISS"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": ["HBM3E_MAJOR_CUSTOMER_SALES_DELAY_Q3_PROFIT_MISS"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv", "profile_path": "atlas/symbol_profiles/005/005930.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-10-08", "entry_price": 60300.0, "MFE_30D_pct": 1.82, "MFE_90D_pct": 1.82, "MFE_180D_pct": 7.3, "MFE_1Y_pct": 65.67, "MFE_2Y_pct": null, "MAE_30D_pct": -17.25, "MAE_90D_pct": -17.25, "MAE_180D_pct": -17.25, "MAE_1Y_pct": -17.25, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-07-04", "peak_price": 64700.0, "drawdown_after_peak_pct": -2.63, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "4b_watch_hardened_to_4c", "four_b_evidence_type": "contract_delay|revision_slowdown|margin_or_backlog_slowdown", "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "major_customer_delay_profit_miss_4c", "current_profile_verdict": "current_profile_needs_hard_4c_confirmation_before_price_validation", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY|005930|2024-10-08", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C06-127-T006", "case_id": "C06-127-006", "symbol": "009150", "company_name": "Samsung Electro-Mechanics", "round": "R2", "loop": 127, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "HBM_CUSTOMER_APPROVAL_CAPACITY_MIX_BRIDGE_VS_QUALIFICATION_DELAY", "sector": "AI/Semiconductor/Electronics", "primary_archetype": "HBM customer/capacity bridge", "loop_objective": "sector_specific_rule_discovery; canonical_archetype_rule_candidate; counterexample_mining; 4C_thesis_break_timing_test; URL_proxy_quality_repair; complete_30_90_180_MFE_MAE", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-10-29", "evidence_available_at_that_date": "Samsung Electro-Mechanics reported package-solution growth from large-area multilayer FCBGA substrates for AI/server/automotive and AI/server FCBGA doubling YoY. This is HBM-adjacent AI infrastructure evidence, not direct HBM memory customer approval.", "evidence_source": "https://samsungsem.com/global/newsroom/news/view.do?id=8642", "stage2_evidence_fields": ["AI_SERVER_FCBGA_SUBSTRATE_SUPPLY_MIX"], "stage3_evidence_fields": ["mass_production", "customer_supply", "capacity_or_mix_bridge"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/009/009150/2024.csv", "profile_path": "atlas/symbol_profiles/009/009150.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-10-29", "entry_price": 120200.0, "MFE_30D_pct": 1.83, "MFE_90D_pct": 24.63, "MFE_180D_pct": 24.63, "MFE_1Y_pct": 108.4, "MFE_2Y_pct": null, "MAE_30D_pct": -12.23, "MAE_90D_pct": -12.23, "MAE_180D_pct": -12.23, "MAE_1Y_pct": -12.23, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-02-17", "peak_price": 149800.0, "drawdown_after_peak_pct": -27.37, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": null, "four_c_protection_label": null, "trigger_outcome_label": "hbm_adjacent_substrate_positive_green_cap", "current_profile_verdict": "stage2_ok_but_green_cap_until_direct_memory_customer_capacity_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY|009150|2024-10-29", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "P2_C06_canonical_candidate", "case_id": "C06-127-001", "trigger_id": "C06-127-T001", "symbol": "000660", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "raw_component_scores_before": {"contract_score": 8, "backlog_visibility_score": 5, "margin_bridge_score": 4, "revision_score": 5, "relative_strength_score": 6, "customer_quality_score": 9, "policy_or_regulatory_score": 1, "valuation_repricing_score": 5, "execution_risk_score": 4, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 1}, "weighted_score_before": 62.7, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 8, "backlog_visibility_score": 6, "margin_bridge_score": 4, "revision_score": 5, "relative_strength_score": 6, "customer_quality_score": 9, "policy_or_regulatory_score": 1, "valuation_repricing_score": 5, "execution_risk_score": 4, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 1}, "weighted_score_after": 63.7, "stage_label_after": "Stage2-Actionable", "changed_components": ["customer_quality_score", "backlog_visibility_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "Proposed C06 gate raises confidence only when HBM customer approval/supply and capacity conversion are explicit; it penalizes qualification delay and HBM-adjacent-only evidence.", "MFE_90D_pct": 23.35, "MAE_90D_pct": -3.61, "score_return_alignment_label": "customer_sample_bridge_positive", "current_profile_verdict": "current_profile_correct_but_green_should_wait_for_mass_production"}
{"row_type": "score_simulation", "profile_id": "P2_C06_canonical_candidate", "case_id": "C06-127-002", "trigger_id": "C06-127-T002", "symbol": "000660", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "raw_component_scores_before": {"contract_score": 9, "backlog_visibility_score": 8, "margin_bridge_score": 7, "revision_score": 7, "relative_strength_score": 8, "customer_quality_score": 10, "policy_or_regulatory_score": 1, "valuation_repricing_score": 6, "execution_risk_score": 3, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 1}, "weighted_score_before": 79.3, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 9, "margin_bridge_score": 8, "revision_score": 8, "relative_strength_score": 8, "customer_quality_score": 10, "policy_or_regulatory_score": 1, "valuation_repricing_score": 6, "execution_risk_score": 3, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 1}, "weighted_score_after": 83.9, "stage_label_after": "Stage3-Green", "changed_components": ["customer_quality_score", "backlog_visibility_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "Proposed C06 gate raises confidence only when HBM customer approval/supply and capacity conversion are explicit; it penalizes qualification delay and HBM-adjacent-only evidence.", "MFE_90D_pct": 55.12, "MAE_90D_pct": -3.81, "score_return_alignment_label": "mass_production_customer_supply_positive", "current_profile_verdict": "current_profile_correct_green_with_drawdown_aware_hold"}
{"row_type": "score_simulation", "profile_id": "P2_C06_canonical_candidate", "case_id": "C06-127-003", "trigger_id": "C06-127-T003", "symbol": "000660", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "raw_component_scores_before": {"contract_score": 8, "backlog_visibility_score": 8, "margin_bridge_score": 7, "revision_score": 6, "relative_strength_score": 7, "customer_quality_score": 9, "policy_or_regulatory_score": 1, "valuation_repricing_score": 7, "execution_risk_score": 4, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 1}, "weighted_score_before": 74.5, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 8, "backlog_visibility_score": 8, "margin_bridge_score": 7, "revision_score": 6, "relative_strength_score": 6, "customer_quality_score": 9, "policy_or_regulatory_score": 1, "valuation_repricing_score": 5, "execution_risk_score": 5, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 1}, "weighted_score_after": 70.2, "stage_label_after": "Stage3-Yellow", "changed_components": ["customer_quality_score", "backlog_visibility_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "Proposed C06 gate raises confidence only when HBM customer approval/supply and capacity conversion are explicit; it penalizes qualification delay and HBM-adjacent-only evidence.", "MFE_90D_pct": 23.5, "MAE_90D_pct": -14.25, "score_return_alignment_label": "capacity_density_follow_on_positive_with_late_entry_risk", "current_profile_verdict": "current_profile_partly_too_permissive_if_late_valuation_not_penalized"}
{"row_type": "score_simulation", "profile_id": "P2_C06_canonical_candidate", "case_id": "C06-127-004", "trigger_id": "C06-127-T004", "symbol": "005930", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "raw_component_scores_before": {"contract_score": 3, "backlog_visibility_score": 3, "margin_bridge_score": 2, "revision_score": 3, "relative_strength_score": 5, "customer_quality_score": 3, "policy_or_regulatory_score": 1, "valuation_repricing_score": 6, "execution_risk_score": 8, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 2}, "weighted_score_before": 36.7, "stage_label_before": "Stage1", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 2, "margin_bridge_score": 1, "revision_score": 2, "relative_strength_score": 4, "customer_quality_score": 1, "policy_or_regulatory_score": 1, "valuation_repricing_score": 4, "execution_risk_score": 9, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 2}, "weighted_score_after": 24.1, "stage_label_after": "Stage4B", "changed_components": ["customer_quality_score", "backlog_visibility_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "Proposed C06 gate raises confidence only when HBM customer approval/supply and capacity conversion are explicit; it penalizes qualification delay and HBM-adjacent-only evidence.", "MFE_90D_pct": 17.0, "MAE_90D_pct": -21.61, "score_return_alignment_label": "qualification_delay_4b_counterexample", "current_profile_verdict": "current_profile_too_permissive_if_generic_hbm_demand_offsets_customer_delay"}
{"row_type": "score_simulation", "profile_id": "P2_C06_canonical_candidate", "case_id": "C06-127-005", "trigger_id": "C06-127-T005", "symbol": "005930", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 2, "margin_bridge_score": 1, "revision_score": 2, "relative_strength_score": 2, "customer_quality_score": 2, "policy_or_regulatory_score": 1, "valuation_repricing_score": 5, "execution_risk_score": 9, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 4}, "weighted_score_before": 23.2, "stage_label_before": "Stage1", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": 1, "revision_score": 1, "relative_strength_score": 1, "customer_quality_score": 1, "policy_or_regulatory_score": 1, "valuation_repricing_score": 3, "execution_risk_score": 10, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_after": 13.2, "stage_label_after": "Stage4C", "changed_components": ["customer_quality_score", "backlog_visibility_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "Proposed C06 gate raises confidence only when HBM customer approval/supply and capacity conversion are explicit; it penalizes qualification delay and HBM-adjacent-only evidence.", "MFE_90D_pct": 1.82, "MAE_90D_pct": -17.25, "score_return_alignment_label": "major_customer_delay_profit_miss_4c", "current_profile_verdict": "current_profile_needs_hard_4c_confirmation_before_price_validation"}
{"row_type": "score_simulation", "profile_id": "P2_C06_canonical_candidate", "case_id": "C06-127-006", "trigger_id": "C06-127-T006", "symbol": "009150", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 6, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 4, "customer_quality_score": 6, "policy_or_regulatory_score": 1, "valuation_repricing_score": 4, "execution_risk_score": 4, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 1}, "weighted_score_before": 51.9, "stage_label_before": "Stage1", "raw_component_scores_after": {"contract_score": 4, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 4, "customer_quality_score": 5, "policy_or_regulatory_score": 1, "valuation_repricing_score": 4, "execution_risk_score": 4, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 1}, "weighted_score_after": 47.9, "stage_label_after": "Stage2-Actionable", "changed_components": ["customer_quality_score", "backlog_visibility_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "Proposed C06 gate raises confidence only when HBM customer approval/supply and capacity conversion are explicit; it penalizes qualification delay and HBM-adjacent-only evidence.", "MFE_90D_pct": 24.63, "MAE_90D_pct": -12.23, "score_return_alignment_label": "hbm_adjacent_substrate_positive_green_cap", "current_profile_verdict": "stage2_ok_but_green_cap_until_direct_memory_customer_capacity_bridge"}
{"row_type": "residual_contribution", "round": "R2", "loop": 127, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "new_independent_case_count": 6, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 6, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "hard_4c_confirmation", "full_4b_requires_non_price_evidence"], "residual_error_types_found": ["HBM_customer_qualification_delay_overcredit", "HBM_adjacency_green_overpromotion", "late_capacity_follow_on_MAE_risk"], "loop_contribution_label": "C06_customer_approval_capacity_bridge_vs_qualification_delay_quality_repair", "do_not_propose_new_weight_delta": false}
```

## Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 6
calibration_usable_trigger_count: 6
representative_trigger_count: 6
new_weight_evidence_candidate_count: 6
guardrail_candidate_count: 3
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<symbol>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<symbol>.json.

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
completed_round = R2
completed_loop = 127
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0/1 quality repair — C06 URL/proxy repair, positive/counterexample balance, HBM customer qualification delay split
next_recommended_archetypes = C14_EV_DEMAND_SLOWDOWN_4B_4C; C28_SOFTWARE_SECURITY_CONTRACT_RETENTION; C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF; C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes

- Execution prompt: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- No-repeat ledger: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
- Stock-Web manifest: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
- Stock-Web schema: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/schema.json
- SK hynix March 2024 mass production: https://www.reuters.com/technology/nvidia-supplier-sk-hynix-begins-mass-production-next-generation-memory-chip-2024-03-19/
- SK hynix September 2024 12-layer mass production: https://en.yna.co.kr/view/AEN20240926002700320
- Samsung May 2024 qualification delay: https://www.reuters.com/technology/samsungs-hbm-chips-failing-nvidia-tests-due-heat-power-consumption-woes-sources-2024-05-23/
- Samsung October 2024 HBM3E sales delay/profit miss: https://www.reuters.com/technology/samsung-electronics-estimates-274-jump-q3-operating-profit-2024-10-07/
- Samsung Electro-Mechanics 3Q24 performance: https://samsungsem.com/global/newsroom/news/view.do?id=8642
