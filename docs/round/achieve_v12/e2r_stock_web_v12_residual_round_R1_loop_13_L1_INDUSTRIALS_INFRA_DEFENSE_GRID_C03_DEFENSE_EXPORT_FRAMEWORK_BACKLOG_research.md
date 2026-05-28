# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

- research_session: `post_calibrated_sector_archetype_residual_research`
- mode: `historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12`
- output_file: `e2r_stock_web_v12_residual_round_R1_loop_13_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md`
- round: `R1`
- loop: `13`
- large_sector_id: `L1_INDUSTRIALS_INFRA_DEFENSE_GRID`
- canonical_archetype_id: `C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG`
- fine_archetype_id: `POLAND_CHUNMOO_EXECUTION_CONTRACT|IRAQ_MSAM_EXPORT_ORDER|KOREA_TENSION_PRICE_ONLY_DEFENSE_THEME`
- loop_objective: `coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test`
- stock_agent_code_access_allowed: `false`
- stock_agent_code_patch_allowed: `false`
- stock_agent_live_scan_allowed: `false`
- current_stock_discovery_allowed: `false`
- production_scoring_changed: `false`
- shadow_weight_only: `true`
- handoff_prompt_embedded: `true`
- handoff_prompt_executed_now: `false`

This round intentionally does **not** recommend current stocks or scan live candidates. It is a historical calibration artifact. The selected gap is C03, because the available local v12 outputs were concentrated in grid/nuclear, consumer, financial, biotech, platform, mobility, construction, and governance paths while C03 defense export framework/backlog had no standalone residual file.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
previous_baseline_reference = e2r_2_0_baseline_reference
production_scoring_changed = false
shadow_weight_only = true
```

Current applied axes assumed for stress testing:

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

This file does not re-propose those global axes. It stress-tests whether C03 needs a defense-export-specific distinction between signed export/backlog evidence and price-only geopolitical tension.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| round | R1 |
| loop | 13 |
| large_sector_id | L1_INDUSTRIALS_INFRA_DEFENSE_GRID |
| canonical_archetype_id | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG |
| fine_archetype_id | POLAND_CHUNMOO_EXECUTION_CONTRACT; IRAQ_MSAM_EXPORT_ORDER; KOREA_TENSION_PRICE_ONLY_DEFENSE_THEME |
| sector | 산업재·수주·인프라·방산 |
| primary_archetype | defense_export_framework_backlog |
| objective | coverage_gap_fill; counterexample_mining; sector_specific_rule_discovery; canonical_archetype_compression |

## 3. Previous Coverage / Duplicate Avoidance Check

- Existing local v12 MD set had R1/C02 and R1/C04, but no standalone C03 file.
- C03 is not avoided merely because L1 exists; the novelty unit here is canonical archetype plus symbol/trigger family.
- Selected symbols are new for this C03 loop: `012450`, `079550`, `065450`.
- Trigger families are distinct: signed Poland execution contract, repeat Middle East missile export order, and price-only Korean tension theme.
- Reused case count: `0`.

```text
new_independent_case_count = 3
reused_case_count = 0
new_symbol_count = 3
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
new_canonical_archetype_count = 1
new_trigger_family_count = 3
minimum_new_independent_case_ratio = 1.00
```

## 4. Stock-Web OHLC Input / Price Source Validation

The price atlas manifest confirms `FinanceData/marcap`, raw/unadjusted price status, `max_date = 2026-02-20`, tradable/raw row counts, market coverage, and shard roots. fileciteturn1181file0L4-L45 The schema confirms the tradable shard columns and MFE/MAE formulas used in this file. fileciteturn1182file0L17-L28 fileciteturn1182file0L60-L68

| field | value |
|---|---|
| price_data_source | Songdaiki/stock-web |
| upstream_source | FinanceData/marcap |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| manifest_max_date | 2026-02-20 |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

Symbol profile checks:

| symbol | company | profile status | corporate-action window status |
|---|---:|---|---|
| 012450 | 한화에어로스페이스 | active-like; 1995-05-02 to 2026-02-20; 7,730 tradable rows | no listed candidate in 2024/entry~180D; profile candidates are old dates only. fileciteturn1191file0L43-L49 fileciteturn1192file0L14-L23 |
| 079550 | LIG넥스원 | active-like; 2015-10-02 to 2026-02-20; 2,547 tradable rows | clean; corporate_action_candidate_count=0. fileciteturn1193file0L23-L41 fileciteturn1193file0L105-L115 |
| 065450 | 빅텍 | active-like; 2003-02-05 to 2026-02-20; 5,676 tradable rows | clean for 2024; profile candidates are 2004/2008/2009 only. fileciteturn1194file0L23-L53 fileciteturn1195file0L4-L11 |

## 5. Historical Eligibility Gate

| case | trigger_date | entry_date | entry row exists | 180D forward window | 180D corporate-action contamination | calibration_usable |
|---|---:|---:|---:|---:|---:|---:|
| Hanwha Poland Chunmoo | 2024-04-25 | 2024-04-25 | yes | yes | clean by profile rules | true |
| LIG Iraq M-SAM | 2024-09-19 | 2024-09-19 | yes | yes | clean | true |
| Victek trash-balloon tension | 2024-05-29 | 2024-05-29 | yes | yes | clean by profile rules | true |

All three calibration representative triggers are usable for 30D/90D/180D analysis. `MFE_2Y_pct` is left null because the stock-web manifest max date does not provide a full 504-trading-day forward window for 2024 entries.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| POLAND_CHUNMOO_EXECUTION_CONTRACT | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | Signed export execution contract converts national-defense theme into customer/backlog/delivery evidence. |
| IRAQ_MSAM_EXPORT_ORDER | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | Repeat export order validates product exportability and backlog visibility. |
| KOREA_TENSION_PRICE_ONLY_DEFENSE_THEME | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | Negative compression: defense theme without export/backlog is blocked from C03 positive promotion. |

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger family | current_profile_verdict | reason selected |
|---|---:|---|---|---|---|---|
| R1L13-C03-012450-HANWHA-POLAND-CHUNMOO-20240425 | 012450 | 한화에어로스페이스 | positive | signed Poland execution contract | current_profile_too_late | Turns C03 from theme into backlog/delivery evidence, but with high initial MAE. |
| R1L13-C03-079550-LIG-IRAQ-MSAMI-20240919 | 079550 | LIG넥스원 | positive | repeat Middle East missile export order | current_profile_correct | Strongest clean C03: repeat order, known product line, low initial MAE then large 180D MFE. |
| R1L13-C03-065450-VICTEK-BALLOON-TENSION-20240529 | 065450 | 빅텍 | counterexample | price-only geopolitical tension | current_profile_false_positive | Price popped, but no contract/backlog evidence; should not train C03 promotion. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_case_count = 1
4C_case_count = 0
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
```

The positive cases share a clear mechanism: a public contract/order turns a broad geopolitical narrative into a concrete backlog bridge. The counterexample is the shadow opposite: geopolitical tension can throw sparks onto a defense ticker, but without export/customer/backlog evidence the sparks do not become a furnace.

## 9. Evidence Source Map

| case | evidence family | source note |
|---|---|---|
| Hanwha Aerospace | signed export execution contract / Poland framework continuation | Reuters reported the USD 1.64bn Chunmoo supply deal and linked it to the larger 2022 Poland package. citeturn448930news1 |
| LIG Nex1 | repeat export order / M-SAM system | Reuters reported the USD 2.8bn Iraq missile-system export order and noted the prior Saudi M-SAM II export route. citeturn448930news0 |
| Victek | geopolitical tension / price-only theme | Reuters reported North Korea’s trash-balloon incident; this is a tension event, not company-level contract/backlog evidence. citeturn173632news0 |

## 10. Price Data Source Map

| symbol | trigger row | stock-web row evidence |
|---:|---|---|
| 012450 | entry 2024-04-25 close 241,000 | stock-web 2024 shard shows 2024-04-25 OHLCV and subsequent 2024 rows. fileciteturn1196file0L13-L16 |
| 012450 | 2024/2025 peak path | 2024 high expanded to 425,000 by 2024-11-12; 2025 file shows later higher continuation. fileciteturn1197file0L44-L48 fileciteturn1204file0L28-L37 |
| 079550 | entry 2024-09-19 close 206,500 | stock-web 2024 shard shows 2024-09-19 OHLCV. fileciteturn1198file0L20-L24 |
| 079550 | 180D expansion | stock-web 2025 shard shows the later 2025 MFE expansion through 621,000/650,000 zone. fileciteturn1201file0L41-L48 |
| 065450 | entry 2024-05-29 close 4,725 | stock-web 2024 shard shows May/June price-only spike and later drawdown. fileciteturn1202file0L24-L32 fileciteturn1206file0L9-L15 |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | type | trigger_date | entry_date | entry_price | stage2 evidence | stage3 evidence | 4B/4C evidence | verdict |
|---|---:|---|---:|---:|---:|---|---|---|---|
| R1L13-HANWHA-20240425-S2A | 012450 | Stage2-Actionable | 2024-04-25 | 2024-04-25 | 241000 | disclosure, customer/order, backlog, policy | public sources, financial visibility, margin bridge | none | current_profile_too_late |
| R1L13-LIGNEX1-20240919-S2A | 079550 | Stage2-Actionable | 2024-09-19 | 2024-09-19 | 206500 | disclosure, customer/order, backlog, repeat export | public sources, durable customer, financial visibility | none | current_profile_correct |
| R1L13-VICTEK-20240529-PRICEONLY | 065450 | Stage2-Blocked | 2024-05-29 | 2024-05-29 | 4725 | relative strength only | none | price-only local peak | current_profile_false_positive |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | MFE1Y | MAE1Y | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R1L13-HANWHA-20240425-S2A | 241000 | 3.53 | -19.50 | 31.74 | -19.50 | 76.35 | -19.50 | 233.61 | -19.50 | 2025-04-14 | 804000 | -25.00 |
| R1L13-LIGNEX1-20240919-S2A | 206500 | 28.33 | -0.48 | 31.48 | -18.26 | 200.73 | -18.26 | 214.77 | -18.26 | 2025-06-23 | 650000 | -21.85 |
| R1L13-VICTEK-20240529-PRICEONLY | 4725 | 24.87 | -0.85 | 24.87 | -6.24 | 24.87 | -21.48 | 24.87 | -21.48 | 2024-06-10 | 5900 | -37.12 |

Interpretation:

- Hanwha shows why signed export contracts deserve early recognition, but not blind Green: the same event produced high 180D/1Y MFE and a meaningful initial drawdown.
- LIG Nex1 is the cleanest positive: repeat export order, low initial MAE, large 180D MFE.
- Victek proves the guard: price-only geopolitical tension can have a local MFE, but its post-peak decay and lack of backlog evidence make it unusable for positive C03 calibration.

## 13. Current Calibrated Profile Stress Test

| case | P0 likely label | actual alignment | residual error |
|---|---|---|---|
| Hanwha | Stage2/Yellow until revisions catch up | positive but high-MAE; earlier C03 recognition useful | current_profile_too_late |
| LIG Nex1 | Stage3-Green or strong Yellow | aligned | current_profile_correct |
| Victek | Stage2 theme-watch; risk of over-read if price is interpreted as evidence | false positive if promoted | current_profile_false_positive |

Answers to v12 stress-test questions:

1. Current profile handles clean signed backlog better than price-only events, but C03 needs more explicit positive/negative separation.
2. MFE/MAE supports that separation: signed orders produced durable MFE; price-only tension decayed after local peak.
3. The Stage2 bonus is useful for Hanwha/LIG but excessive if applied to Victek-like price-only themes.
4. Yellow threshold 75 is acceptable for signed-export cases, not for price-only geopolitical movement.
5. Green threshold 87/revision 55 should remain strict; Hanwha’s initial MAE argues against immediate unguarded Green.
6. Price-only blowoff guard is strengthened by Victek.
7. Full 4B non-price requirement remains correct; Victek is a price-only local 4B overlay, not a fundamental exit thesis.
8. No hard 4C routing change is proposed in this loop.

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2/Actionable quality | Yellow readiness | Green readiness | green_lateness_ratio |
|---|---|---|---|---:|
| Hanwha | strong: signed export execution contract | yes, but high-MAE | only after backlog/revision bridge becomes clearer | 0.42 |
| LIG Nex1 | very strong: repeat export order | yes | yes, if revision/visibility confirms | 0.29 |
| Victek | weak: relative strength only | no | no | not_applicable |

C03-specific lesson: Stage2 can be early when the evidence is a named customer/order/contract; Stage3-Green still needs revision or durable visibility. Price alone is a mirage: it has shape but no load-bearing steel.

## 15. 4B Local vs Full-window Timing Audit

| case | 4B evidence type | local proximity | full-window proximity | timing verdict |
|---|---|---:|---:|---|
| Hanwha | not_applicable | null | null | not_applicable |
| LIG Nex1 | not_applicable | null | null | not_applicable |
| Victek | price_only, positioning_overheat | 1.00 | 1.00 | price_only_local_4B_do_not_promote |

Victek should be stored as a 4B/guardrail overlay only: it calibrates theme-decay risk, not positive entry scoring.

## 16. 4C Protection Audit

No full hard-4C thesis-break row is proposed. Victek gets `false_break_price_only_theme_decay`, because the case never had a C03 thesis to break. It had only a price/tension flare.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = l1_defense_export_signed_order_visibility_gate
proposal = if L1 defense name has explicit signed export contract, named overseas customer, and delivery/backlog visibility, allow C03 Stage2/Yellow promotion earlier than full revision confirmation.
negative_guard = if evidence is only geopolitical tension or defense-theme relative strength, block C03 positive promotion even if local MFE is positive.
```

Rationale: In defense exports, the business event is often contractual before earnings revisions fully arrive. But the same sector also attracts tension-driven price spikes. The rule must recognize the contract while refusing the siren-song of theme-only price action.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
new_axis_proposed = c03_signed_export_contract_backlog_bonus
counterexample_guard = c03_price_only_geopolitical_theme_block
```

The proposed C03 compression is:

```text
positive C03 = signed export order/framework + customer quality + backlog/delivery visibility
blocked C03 = geopolitical tension + relative strength without contract/backlog/revision evidence
```

## 19. Before / After Backtest Comparison

| profile_id | scope | selected triggers | avg_MFE90 | avg_MAE90 | avg_MFE180 | avg_MAE180 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | global current | 3 | 29.36 | -14.67 | 100.65 | -19.75 | 33.3% | price-only defense theme still needs explicit guard |
| P0b e2r_2_0_baseline_reference | rollback | 3 | 29.36 | -14.67 | 100.65 | -19.75 | 33.3% | weaker guard; more likely to over-read theme price |
| P1 sector_specific_candidate_profile | L1 | 3 | 29.36 | -14.67 | 100.65 | -19.75 | 0% after Victek block | sector rule improves evidence hygiene |
| P2 canonical_archetype_candidate_profile | C03 | 3 | 29.36 | -14.67 | 100.65 | -19.75 | 0% after price-only block | best scope |
| P3 counterexample_guard_profile | C03 guard | 1 blocked | 24.87 | -6.24 | 24.87 | -21.48 | 0% promoted | blocks theme-only false positives |

## 20. Score-Return Alignment Matrix

| case | weighted_score_before | stage_before | weighted_score_after | stage_after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| Hanwha | 89 | Stage3-Green borderline but high-MAE | 91 | Stage3-Yellow/Green with MAE guard | 31.74 | -19.50 | positive, but needs high-MAE guard |
| LIG Nex1 | 96 | Stage3-Green | 99 | Stage3-Green kept | 31.48 | -18.26 | aligned |
| Victek | 55 | Stage2-theme-watch under P0 | 35 | Blocked: price-only defense theme | 24.87 | -6.24 | false-positive risk fixed by guard |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | POLAND_CHUNMOO_EXECUTION_CONTRACT; IRAQ_MSAM_EXPORT_ORDER; KOREA_TENSION_PRICE_ONLY_DEFENSE_THEME | 2 | 1 | 1 | 0 | 3 | 0 | 3 | 3 | 2 | true | true | C03 now has initial positive/counterexample balance; next gap is hard 4C defense contract cancellation/delay. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
new_canonical_archetype_count: 1
new_fine_archetype_count: 3
new_trigger_family_count: 3
positive_case_count: 2
counterexample_count: 1
current_profile_error_count: 2
tested_existing_calibrated_axes: stage3_green_revision_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
residual_error_types_found: current_profile_too_late, current_profile_false_positive, price_only_defense_theme_decay
new_axis_proposed: c03_signed_export_contract_backlog_bonus; c03_price_only_geopolitical_theme_block
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: C03 missing in local v12 output set; R1 coverage was concentrated in C02/C04.
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- stock-web manifest/schema/profile/shard basis.
- 30D/90D/180D MFE/MAE for three representative triggers.
- positive/counterexample balance for C03.
- price-only vs contract/backlog evidence distinction.

Not validated:

- no stock_agent source code was opened.
- no production scoring was changed.
- no live watchlist was produced.
- no current-stock recommendation was made.
- no brokerage/API/auto-trading path was touched.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c03_signed_export_contract_backlog_bonus,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG,0,+2,+2,"signed export execution contract or repeat export order with explicit customer and delivery visibility","positive cases showed avg MFE90 31.61pct while price-only counterexample decayed after local peak",R1L13-HANWHA-20240425-S2A|R1L13-LIGNEX1-20240919-S2A|R1L13-VICTEK-20240529-PRICEONLY,3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c03_price_only_geopolitical_theme_block,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG,false,true,+1,"geopolitical tension without contract/backlog should remain blocked from C03 positive promotion","Victek MFE was price-pop but 180D MAE and post-peak drawdown show theme decay",R1L13-VICTEK-20240529-PRICEONLY,1,1,1,medium,counterexample_guard,"price-only rows cannot promote Stage2/Stage3"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R1L13-C03-012450-HANWHA-POLAND-CHUNMOO-20240425", "symbol": "012450", "company_name": "한화에어로스페이스", "round": "R1", "loop": "13", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "POLAND_CHUNMOO_EXECUTION_CONTRACT|IRAQ_MSAM_EXPORT_ORDER|KOREA_TENSION_PRICE_ONLY_DEFENSE_THEME", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R1L13-HANWHA-20240425-S2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "export_contract_to_backlog_rerating_success_with_initial_mae", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "Initial MAE was high, so this is not a blind Green. The useful rule is that signed export execution contracts can upgrade Stage2/Yellow earlier than accounting revision if order quality and delivery visibility are explicit."}
{"row_type": "case", "case_id": "R1L13-C03-079550-LIG-IRAQ-MSAMI-20240919", "symbol": "079550", "company_name": "LIG넥스원", "round": "R1", "loop": "13", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "POLAND_CHUNMOO_EXECUTION_CONTRACT|IRAQ_MSAM_EXPORT_ORDER|KOREA_TENSION_PRICE_ONLY_DEFENSE_THEME", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R1L13-LIGNEX1-20240919-S2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "repeat_export_order_to_large_mfe_success", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "The positive path had much lower initial MAE than Hanwha because the export thesis stacked on an already visible M-SAM export product line."}
{"row_type": "case", "case_id": "R1L13-C03-065450-VICTEK-BALLOON-TENSION-20240529", "symbol": "065450", "company_name": "빅텍", "round": "R1", "loop": "13", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "POLAND_CHUNMOO_EXECUTION_CONTRACT|IRAQ_MSAM_EXPORT_ORDER|KOREA_TENSION_PRICE_ONLY_DEFENSE_THEME", "case_type": "price_moved_without_evidence", "positive_or_counterexample": "counterexample", "best_trigger": "R1L13-VICTEK-20240529-PRICEONLY", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "price_only_defense_theme_decay_counterexample", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "The price pop was real, but the evidence family is not C03. This is the guardrail case: geopolitical tension can move price, but cannot train export-backlog promotion without contract/backlog evidence."}
{"row_type": "trigger", "trigger_id": "R1L13-HANWHA-20240425-S2A", "case_id": "R1L13-C03-012450-HANWHA-POLAND-CHUNMOO-20240425", "symbol": "012450", "company_name": "한화에어로스페이스", "round": "R1", "loop": "13", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "POLAND_CHUNMOO_EXECUTION_CONTRACT|IRAQ_MSAM_EXPORT_ORDER|KOREA_TENSION_PRICE_ONLY_DEFENSE_THEME", "sector": "산업재·수주·인프라·방산", "primary_archetype": "defense_export_framework_backlog", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-25", "evidence_available_at_that_date": "Reuters reported that Hanwha Aerospace signed a USD 1.64bn deal to supply 72 Chunmoo rocket artillery units to Poland, explicitly framed as part of the larger Poland 2022 arms package. This was not just geopolitical attention; it was an executable export/backlog bridge. citeturn448930news1", "evidence_source": "Reuters 2024-04-25; stock-web 012450 2024/2025 shards", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "backlog_or_delivery_visibility", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["multiple_public_sources", "financial_visibility", "durable_customer_confirmation", "margin_bridge"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/012/012450/2024.csv", "profile_path": "atlas/symbol_profiles/012/012450.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-04-25", "entry_price": 241000, "MFE_30D_pct": 3.53, "MFE_90D_pct": 31.74, "MFE_180D_pct": 76.35, "MFE_1Y_pct": 233.61, "MFE_2Y_pct": null, "MAE_30D_pct": -19.5, "MAE_90D_pct": -19.5, "MAE_180D_pct": -19.5, "MAE_1Y_pct": -19.5, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-04-14", "peak_price": 804000, "drawdown_after_peak_pct": -25.0, "green_lateness_ratio": 0.42, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "export_contract_to_backlog_rerating_success_with_initial_mae", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_rules", "same_entry_group_id": "012450_2024-04-25_241000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R1L13-LIGNEX1-20240919-S2A", "case_id": "R1L13-C03-079550-LIG-IRAQ-MSAMI-20240919", "symbol": "079550", "company_name": "LIG넥스원", "round": "R1", "loop": "13", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "POLAND_CHUNMOO_EXECUTION_CONTRACT|IRAQ_MSAM_EXPORT_ORDER|KOREA_TENSION_PRICE_ONLY_DEFENSE_THEME", "sector": "산업재·수주·인프라·방산", "primary_archetype": "defense_export_framework_backlog", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-09-19", "evidence_available_at_that_date": "Reuters reported that LIG Nex1 won a USD 2.8bn Iraq missile-system export deal and noted the prior Saudi M-SAM II order, making the event a repeat-export/backlog framework rather than a one-off domestic defense headline. citeturn448930news0", "evidence_source": "Reuters 2024-09-19; stock-web 079550 2024/2025 shards", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "backlog_or_delivery_visibility", "repeat_order_or_conversion"], "stage3_evidence_fields": ["multiple_public_sources", "durable_customer_confirmation", "financial_visibility", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/079/079550/2024.csv", "profile_path": "atlas/symbol_profiles/079/079550.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-09-19", "entry_price": 206500, "MFE_30D_pct": 28.33, "MFE_90D_pct": 31.48, "MFE_180D_pct": 200.73, "MFE_1Y_pct": 214.77, "MFE_2Y_pct": null, "MAE_30D_pct": -0.48, "MAE_90D_pct": -18.26, "MAE_180D_pct": -18.26, "MAE_1Y_pct": -18.26, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": true, "peak_date": "2025-06-23", "peak_price": 650000, "drawdown_after_peak_pct": -21.85, "green_lateness_ratio": 0.29, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "repeat_export_order_to_large_mfe_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "079550_2024-09-19_206500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R1L13-VICTEK-20240529-PRICEONLY", "case_id": "R1L13-C03-065450-VICTEK-BALLOON-TENSION-20240529", "symbol": "065450", "company_name": "빅텍", "round": "R1", "loop": "13", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "POLAND_CHUNMOO_EXECUTION_CONTRACT|IRAQ_MSAM_EXPORT_ORDER|KOREA_TENSION_PRICE_ONLY_DEFENSE_THEME", "sector": "산업재·수주·인프라·방산", "primary_archetype": "defense_export_framework_backlog", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Blocked/Price-only defense theme", "trigger_date": "2024-05-29", "evidence_available_at_that_date": "Reuters reported the North Korea trash-balloon incident on 2024-05-29, a geopolitical tension event. It did not itself provide company-level export contract, backlog, delivery, or customer-quality evidence for Victek, so the case should remain price/theme-only rather than entering C03 positive calibration. citeturn173632news0", "evidence_source": "Reuters 2024-05-29; stock-web 065450 2024 shard", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/065/065450/2024.csv", "profile_path": "atlas/symbol_profiles/065/065450.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-29", "entry_price": 4725, "MFE_30D_pct": 24.87, "MFE_90D_pct": 24.87, "MFE_180D_pct": 24.87, "MFE_1Y_pct": 24.87, "MFE_2Y_pct": null, "MAE_30D_pct": -0.85, "MAE_90D_pct": -6.24, "MAE_180D_pct": -21.48, "MAE_1Y_pct": -21.48, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-10", "peak_price": 5900, "drawdown_after_peak_pct": -37.12, "green_lateness_ratio": "not_applicable:no_contract_green_candidate", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_local_4B_do_not_promote", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "false_break_price_only_theme_decay", "trigger_outcome_label": "price_only_defense_theme_decay_counterexample", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "065450_2024-05-29_4725", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L13-C03-012450-HANWHA-POLAND-CHUNMOO-20240425", "trigger_id": "R1L13-HANWHA-20240425-S2A", "symbol": "012450", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 18, "backlog_visibility_score": 18, "margin_bridge_score": 8, "revision_score": 12, "relative_strength_score": 8, "customer_quality_score": 17, "policy_or_regulatory_score": 13, "valuation_repricing_score": 6, "execution_risk_score": -9, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 89, "stage_label_before": "Stage3-Green borderline but high-MAE", "raw_component_scores_after": {"contract_score": 20, "backlog_visibility_score": 20, "margin_bridge_score": 8, "revision_score": 12, "relative_strength_score": 8, "customer_quality_score": 18, "policy_or_regulatory_score": 13, "valuation_repricing_score": 6, "execution_risk_score": -12, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 91, "stage_label_after": "Stage3-Yellow/Green with MAE guard", "changed_components": ["contract_score", "backlog_visibility_score", "execution_risk_score", "relative_strength_score"], "component_delta_explanation": "C03 shadow raises signed export/backlog evidence and blocks price-only geopolitical themes from positive promotion.", "MFE_90D_pct": 31.74, "MAE_90D_pct": -19.5, "score_return_alignment_label": "export_contract_to_backlog_rerating_success_with_initial_mae", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L13-C03-079550-LIG-IRAQ-MSAMI-20240919", "trigger_id": "R1L13-LIGNEX1-20240919-S2A", "symbol": "079550", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 21, "margin_bridge_score": 10, "revision_score": 13, "relative_strength_score": 10, "customer_quality_score": 20, "policy_or_regulatory_score": 14, "valuation_repricing_score": 7, "execution_risk_score": -5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 96, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 21, "backlog_visibility_score": 22, "margin_bridge_score": 10, "revision_score": 13, "relative_strength_score": 10, "customer_quality_score": 21, "policy_or_regulatory_score": 14, "valuation_repricing_score": 7, "execution_risk_score": -5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 99, "stage_label_after": "Stage3-Green kept", "changed_components": ["contract_score", "backlog_visibility_score", "execution_risk_score", "relative_strength_score"], "component_delta_explanation": "C03 shadow raises signed export/backlog evidence and blocks price-only geopolitical themes from positive promotion.", "MFE_90D_pct": 31.48, "MAE_90D_pct": -18.26, "score_return_alignment_label": "repeat_export_order_to_large_mfe_success", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L13-C03-065450-VICTEK-BALLOON-TENSION-20240529", "trigger_id": "R1L13-VICTEK-20240529-PRICEONLY", "symbol": "065450", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 9, "valuation_repricing_score": 6, "execution_risk_score": -10, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 55, "stage_label_before": "Stage2-theme-watch under P0; false-positive risk if price is over-read", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 4, "valuation_repricing_score": 3, "execution_risk_score": -20, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 35, "stage_label_after": "Blocked: price-only defense theme", "changed_components": ["contract_score", "backlog_visibility_score", "execution_risk_score", "relative_strength_score"], "component_delta_explanation": "C03 shadow raises signed export/backlog evidence and blocks price-only geopolitical themes from positive promotion.", "MFE_90D_pct": 24.87, "MAE_90D_pct": -6.24, "score_return_alignment_label": "price_only_defense_theme_decay_counterexample", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R1", "loop": "13", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_canonical_archetype_count": 1, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "residual_error_types_found": ["current_profile_too_late", "current_profile_false_positive", "price_only_defense_theme_decay"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false, "auto_selected_coverage_gap": "C03 missing in local v12 output set; R1 coverage concentrated in C02/C04 rather than defense export framework backlog"}
```

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c03_signed_export_contract_backlog_bonus,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG,0,+2,+2,"signed export execution contract or repeat export order with explicit customer and delivery visibility","positive cases showed avg MFE90 31.61pct while price-only counterexample decayed after local peak",R1L13-HANWHA-20240425-S2A|R1L13-LIGNEX1-20240919-S2A|R1L13-VICTEK-20240529-PRICEONLY,3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c03_price_only_geopolitical_theme_block,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG,false,true,+1,"geopolitical tension without contract/backlog should remain blocked from C03 positive promotion","Victek MFE was price-pop but 180D MAE and post-peak drawdown show theme decay",R1L13-VICTEK-20240529-PRICEONLY,1,1,1,medium,counterexample_guard,"price-only rows cannot promote Stage2/Stage3"
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
next_round = R1 / C03 holdout with defense export delay, financing failure, or contract cancellation 4C
next_focus = hard_4c_defense_contract_delay_or_financing_block
preferred_new_symbols = avoid 012450/079550/065450 unless using a new 4B/4C trigger family
```

## 28. Source Notes

- Prompt basis: uploaded E2R v12 prompt. fileciteturn1180file0
- Stock-web manifest and schema were checked before case construction. fileciteturn1181file0L4-L45 fileciteturn1182file0L60-L68
- Evidence sources are historical event sources, not current/live candidate discovery. citeturn448930news1turn448930news0turn173632news0
