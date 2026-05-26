# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
repo_session = later_batch_implementation_only
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
current_stock_discovery_allowed = false
auto_trading_allowed = false
brokerage_api_allowed = false
```

- File: `e2r_stock_web_v12_residual_round_R6_loop_10_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md`
- Round: `R6`
- Loop: `10`
- Sector: `금융·자본배분·디지털금융`
- `large_sector_id`: `L6_FINANCIAL_CAPITAL_RETURN_DIGITAL`
- `canonical_archetype_id`: `C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN`
- `fine_archetype_id`: `KOREA_VALUEUP_ROE_PBR_CAPITAL_RETURN_BANK_INSURANCE`
- `loop_objective`: `residual_missed_structural_mining`, `counterexample_mining`, `sector_specific_rule_discovery`, `4B_non_price_requirement_stress_test`, `coverage_gap_fill`

This is not a live candidate scan. All rows are historical calibration / residual research rows. The study uses actual `Songdaiki/stock-web` OHLC rows as the price atlas and treats all score changes as shadow-only.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
before_profile_id = e2r_2_1_stock_web_calibrated_proxy
after_profile_id = proposed_sector_or_archetype_shadow_profile
production_scoring_changed = false
```

Current calibrated axes assumed as already applied:

| Axis | Current calibrated value | Treatment in this loop |
|---|---:|---|
| `stage2_actionable_evidence_bonus` | `+2.0` | stress-tested, not re-proposed globally |
| `stage3_yellow_total_min` | `75.0` | kept globally; C21 bridge proposed only as sector/archetype shadow |
| `stage3_green_total_min` | `87.0` | kept |
| `stage3_green_revision_min` | `55.0` | kept; C21 should not bypass Green without capital-return execution evidence |
| `stage3_cross_evidence_green_buffer` | `+1.5` | not re-proposed |
| `price_only_blowoff_blocks_positive_stage` | `true` | kept |
| `full_4b_requires_non_price_evidence` | `true` | strengthened by KB local/full-window audit |
| `hard_4c_thesis_break_routes_to_4c` | `true` | kept; no hard 4C case in this loop |

Residual hypothesis: the current calibrated profile is good at blocking price-only promotions and late/false Green, but it may still underweight financial-sector rerating where the evidence stack is not `contract/backlog/CAPA`, but rather `ROE/PBR discount + explicit capital return capacity + regulatory value-up framing + low credit/accounting risk`.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R6
loop = 10
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id = KOREA_VALUEUP_ROE_PBR_CAPITAL_RETURN_BANK_INSURANCE
```

Compression map:

```text
Korea Corporate Value-up policy event
-> bank / insurance capital-return rerating
-> C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN

Bank high-PBR growth-platform without capital-return execution
-> policy-event false-positive risk
-> C21 counterexample guard
```

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed calibration artifacts reviewed for duplicate avoidance:

- `reports/e2r_calibration/ingest_summary.md`
- `reports/e2r_calibration/applied_scoring_diff.md`
- `reports/e2r_calibration/calibrated_profile_report.md`
- `reports/e2r_calibration/by_round/R6.md`
- `data/e2r/calibration/md_registry.jsonl` excerpt/search

Known prior calibration corpus status:

| Artifact signal | Observed status | Implication for this loop |
|---|---:|---|
| discovered result MDs | `107` | calibration corpus is already broad |
| validated trigger rows | `1,940` | avoid global rule repetition |
| aggregate representative triggers | `1,376` | new loop must add independent signal |
| R6 representative triggers | `101` | financial/capital-return sector exists but still broad |
| R6 unique cases | `25` | add new C21-specific examples rather than repeat global axes |
| duplicate query for selected symbols | no hits for `105560`, `032830`, `323410` in accessible registry/search | treated as new independent cases |

Novelty gate:

```text
required_new_independent_case_ratio >= 0.60
new_independent_case_count = 3
calibration_usable_case_count = 3
new_independent_case_ratio = 1.00
loop_contribution_label = sector_specific_rule_candidate
```

## 4. Stock-Web OHLC Input / Price Source Validation

`Songdaiki/stock-web` manifest and schema were read before case work.

| Field | Value |
|---|---|
| `price_data_source` | `Songdaiki/stock-web` |
| `upstream_source` | `FinanceData/marcap` |
| `source_name` | `FinanceData/marcap` |
| `price_basis` | `tradable_raw` |
| `price_adjustment_status` | `raw_unadjusted_marcap` |
| `manifest_path` | `atlas/manifest.json` |
| `schema_path` | `atlas/schema.json` |
| `universe_path` | `atlas/universe/all_symbols.csv` |
| `calibration_shard_root` | `atlas/ohlcv_tradable_by_symbol_year` |
| `raw_shard_root` | `atlas/ohlcv_raw_by_symbol_year` |
| `manifest_min_date` | `1995-05-02` |
| `manifest_max_date` | `2026-02-20` |
| `tradable_row_count` | `14,354,401` |
| `raw_row_count` | `15,214,118` |
| `symbol_count` | `5,414` |
| `corporate_action_candidate_count` | `14,435` |

Tradable shard columns:

```text
d,o,h,l,c,v,a,mc,s,m
```

The manifest explicitly marks the atlas as raw/unadjusted OHLC and states that corporate-action-contaminated windows are blocked by default. This loop uses tradable shards for MFE/MAE and uses symbol profiles only to validate availability and corporate-action caveats.

## 5. Historical Eligibility Gate

| Symbol | Company | Entry date | Entry row exists | 180D forward available | 180D corporate-action contamination | Calibration usable | 1Y usable | 2Y usable |
|---|---|---:|---|---|---|---|---|---|
| `105560` | KB금융 | `2024-02-26` | true | true | false | true | true | false |
| `032830` | 삼성생명 | `2024-02-26` | true | true | false | true | true | false |
| `323410` | 카카오뱅크 | `2024-02-26` | true | true | false | true | true | false |

2Y fields are not used for quantitative calibration because a 504-trading-day window from `2024-02-26` is not fully available before `stock_web_manifest_max_date = 2026-02-20`. The 30D/90D/180D/1Y windows are usable for all three representative triggers.

## 6. Canonical Archetype Compression Map

| Fine archetype | Canonical archetype | Large sector | Why compressed here |
|---|---|---|---|
| `KOREA_VALUEUP_BANK_CAPITAL_RETURN` | `C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN` | `L6_FINANCIAL_CAPITAL_RETURN_DIGITAL` | Bank rerating is driven by ROE/PBR and shareholder return capacity, not contract backlog |
| `INSURANCE_ASSET_OPTIONALITY_CAPITAL_RETURN` | `C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN` | `L6_FINANCIAL_CAPITAL_RETURN_DIGITAL` | Insurance rerating may move with capital return, capital adequacy, asset optionality, and value-up framing |
| `GROWTH_BANK_POLICY_EVENT_FALSE_POSITIVE` | `C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN` | `L6_FINANCIAL_CAPITAL_RETURN_DIGITAL` | A policy event alone can falsely promote high-PBR/growth-bank names without capital-return execution |

## 7. Case Selection Summary

| Case ID | Symbol | Company | Role | Positive / counterexample | Best trigger | Current-profile verdict | Calibration usable |
|---|---:|---|---|---|---|---|---|
| `R6L10-C21-KBFG-001` | `105560` | KB금융 | `structural_success` | positive | `Stage2-Actionable` | `current_profile_missed_structural` | true |
| `R6L10-C21-SLIF-002` | `032830` | 삼성생명 | `high_mae_success` | positive | `Stage2-Actionable` | `current_profile_too_late` | true |
| `R6L10-C21-KBANK-003` | `323410` | 카카오뱅크 | `false_positive_green` | counterexample | `Stage2-policy-watch` | `current_profile_correct` | true |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_case_count = 1
4C_case_count = 0
minimum_positive_case_count = satisfied
minimum_counterexample_count = satisfied
minimum_calibration_usable_case_count = satisfied
```

The loop is intentionally narrow. It does not claim a global financial rerating rule. It tests whether C21 needs a sector/canonical-archetype shadow bridge that is absent from contract/backlog-heavy E2R archetypes.

## 9. Evidence Source Map

| Evidence family | Used for | Evidence handling |
|---|---|---|
| Korea Corporate Value-up policy event | common trigger family date | Used to anchor the sector policy rerating window; not sufficient by itself |
| Company capital return / shareholder return policy | KB금융 and 삼성생명 positive cases | Research-proxy evidence; must be verified from company filing/IR before production promotion |
| Valuation / ROE / PBR frame | C21 core component | Used as research proxy scoring component, not production score |
| Price relative strength | supportive only | Cannot alone create Stage2/3 evidence |
| High-PBR growth-bank without explicit capital return | 카카오뱅크 counterexample | Used as guard against policy-event false positive |

Stage evidence split:

- Stage2 evidence allowed in this loop: `policy_or_regulatory_optionality`, `relative_strength`, `early_revision_signal`, `valuation_repricing`, `capital_return_optionality`.
- Stage3 evidence required in this loop: `confirmed_return_execution`, `ROE/PBR repricing`, `multiple_public_sources`, `low_credit_or_accounting_risk`, `durable capital return capacity`.
- 4B evidence required in this loop: non-price evidence such as `revision_slowdown`, `valuation_blowoff`, or `capital-return-execution plateau`; price-only local peaks are not full 4B.

## 10. Price Data Source Map

| Symbol | Profile path | Price shard path(s) used | Profile caveat |
|---:|---|---|---|
| `105560` | `atlas/symbol_profiles/105/105560.json` | `atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv`, `2025.csv`, `2026.csv` | no corporate-action candidates |
| `032830` | `atlas/symbol_profiles/032/032830.json` | `atlas/ohlcv_tradable_by_symbol_year/032/032830/2024.csv`, `2025.csv`, `2026.csv` | no corporate-action candidates |
| `323410` | `atlas/symbol_profiles/323/323410.json` | `atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv`, `2025.csv`, `2026.csv` | no corporate-action candidates |

## 11. Case-by-Case Trigger Grid

| Trigger ID | Case ID | Symbol | Trigger type | Trigger date | Entry date | Entry price | Stage2 fields | Stage3 fields | 4B fields | 4C fields | Representative |
|---|---|---:|---|---:|---:|---:|---|---|---|---|---|
| `R6L10-C21-KBFG-T01` | `R6L10-C21-KBFG-001` | `105560` | `Stage2-Actionable` | `2024-02-26` | `2024-02-26` | `62,500` | policy option, ROE/PBR discount, capital return, relative strength | return execution needed, revision confirmation partial | local price peak later | none | true |
| `R6L10-C21-SLIF-T01` | `R6L10-C21-SLIF-002` | `032830` | `Stage2-Actionable` | `2024-02-26` | `2024-02-26` | `92,200` | policy option, asset optionality, low PBR frame, relative strength | capital return execution needed, volatile drawdown risk | none | none | true |
| `R6L10-C21-KBANK-T01` | `R6L10-C21-KBANK-003` | `323410` | `Stage2-policy-watch` | `2024-02-26` | `2024-02-26` | `30,150` | policy option only | no capital-return confirmation, weak valuation repricing | none | thesis weakness watch | true |

## 12. Trigger-Level OHLC Backtest Tables

MFE/MAE values are computed from stock-web `h` and `l` columns using `entry_price = entry_date c`.

| Symbol | Entry date | Entry price | MFE 30D | MAE 30D | MFE 90D | MAE 90D | MFE 180D | MAE 180D | MFE 1Y | MAE 1Y | MFE 2Y | Peak date | Peak price | Drawdown after peak |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|
| `105560` | `2024-02-26` | `62,500` | `25.76%` | `-4.48%` | `44.00%` | `-4.48%` | `66.24%` | `-4.48%` | `66.24%` | `-4.48%` | unavailable | `2026-02-13` | `170,500` | `-3.99%` |
| `032830` | `2024-02-26` | `92,200` | `17.68%` | `-5.10%` | `17.68%` | `-16.92%` | `20.39%` | `-16.92%` | `20.39%` | `-16.92%` | unavailable | `2026-02-20` | `226,500` | `0.00%` |
| `323410` | `2024-02-26` | `30,150` | `1.66%` | `-17.74%` | `1.66%` | `-33.50%` | `1.66%` | `-38.67%` | `1.66%` | `-38.67%` | unavailable | `2024-02-27` | `30,650` | `-39.67%` |

Score-return interpretation:

| Case | Backtest result | Interpretation |
|---|---|---|
| KB금융 | strong 90D/180D and strong full observed path | current profile likely underweighted C21 non-contract rerating evidence |
| 삼성생명 | high full observed upside but high interim MAE | C21 needs volatility guard; Stage3-Green should remain strict |
| 카카오뱅크 | tiny MFE and deep MAE | policy-event-only and relative price bounce must not become positive promotion |

## 13. Current Calibrated Profile Stress Test

| Question | KB금융 | 삼성생명 | 카카오뱅크 |
|---|---|---|---|
| How would P0 judge the case? | likely Stage2 / Yellow-late because contract/backlog components are absent | likely Stage2 / watch; Green blocked by weak revision/execution proof | likely Stage1/2 watch, not Green |
| Did P0 align with MFE/MAE? | partly, but likely missed structural speed | partly, but likely too late and high-MAE-aware | yes; promotion should be blocked |
| Stage2 bonus too much / too little? | too little for C21 if explicit capital-return evidence exists | too little but needs MAE guard | correct if not applied to policy-only case |
| Yellow threshold 75 too high/low? | globally OK; C21 bridge could reach Yellow with capital-return component | OK with volatility guard | should remain above policy-only case |
| Green 87 / revision 55? | should not be weakened globally | should not be weakened due high MAE | correct to block |
| Price-only blowoff guard? | appropriate | appropriate | appropriate |
| Full 4B non-price requirement? | appropriate; local price peak alone would be too early | appropriate | not relevant |
| Hard 4C routing? | no hard break | no hard break | thesis weakness watch only |
| Verdict | `current_profile_missed_structural` | `current_profile_too_late` | `current_profile_correct` |

Current-profile error count: `2`.

## 14. Stage2 / Yellow / Green Comparison

This loop does not weaken the global Green gate. It proposes a C21-specific Yellow bridge.

| Stage layer | C21 positive evidence | C21 guard evidence | Proposed treatment |
|---|---|---|---|
| Stage2 | policy event + low PBR/ROE gap + credible return capacity | policy only, no return capacity | allow Stage2-Actionable only when non-price evidence exists |
| Stage3-Yellow | explicit shareholder return / capital-return policy + valuation repricing + low hard risk | high MAE or still-unproven execution | allow Yellow bridge under C21 only |
| Stage3-Green | repeated capital-return execution + ROE/PBR rerating + confirmed earnings/capital adequacy | high-PBR growth-bank or policy-only excitement | keep Green strict |
| 4B | valuation/crowding/revision slowdown with non-price evidence | local price peak only | keep full 4B non-price requirement |

`green_lateness_ratio = not_applicable` for the representative rows because this loop does not establish paired confirmed Stage3-Green triggers. The calibration object is the sector-specific Stage2/Yellow bridge and the policy-only counterexample guard.

## 15. 4B Local vs Full-window Timing Audit

KB금융 provides a useful 4B timing stress test.

```text
Stage2_Actionable_entry_price = 62,500
Local_4B_candidate_entry_price = 101,000 on 2024-10-25
Local_peak_price_after_Stage2 = 103,900 on 2024-10-25
Full_window_peak_price_after_Stage2 = 170,500 on 2026-02-13
four_b_local_peak_proximity = 0.93
four_b_full_window_peak_proximity = 0.36
four_b_timing_verdict = price_only_local_4B_too_early
four_b_evidence_type = price_only
```

Conclusion: price-only local 4B was too early. The existing axis `full_4b_requires_non_price_evidence = true` is strengthened/kept. Full 4B for C21 should require at least one non-price deterioration signal: valuation blowoff plus revision slowdown, capital-return plateau, credit-cost deterioration, regulatory block, or capital adequacy constraint.

## 16. 4C Protection Audit

No hard 4C calibration row is used in this loop.

| Case | 4C label | Reason |
|---|---|---|
| KB금융 | `thesis_break_watch_only` | no hard evidence of capital-return thesis break in the tested window |
| 삼성생명 | `thesis_break_watch_only` | high MAE but not a hard thesis break |
| 카카오뱅크 | `thesis_break_watch_only` | weak rerating thesis / policy-only false positive, not a hard 4C event |

`hard_4c_thesis_break_routes_to_4c` is kept. No weakening proposed.

## 17. Sector-Specific Rule Candidate

```text
rule_name = financial_roe_pbr_capital_return_bridge
rule_scope = sector_specific
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
proposal_type = sector_shadow_only
confidence = low_to_medium
production_change = false
```

Candidate shadow rule:

```text
If large_sector_id == L6 and canonical_archetype_id == C21:
  allow a Stage2-Actionable / Stage3-Yellow bridge when:
    - valuation_repricing_score is high because PBR/ROE discount is visible;
    - policy_or_regulatory_score is supported by a public value-up or capital-return regime;
    - roe_pbr_capital_return_score is supported by explicit dividend/buyback/cancellation plan, capital adequacy, or shareholder-return target;
    - execution_risk_score is not high;
    - accounting_trust_risk_score is low;
    - price_only_blowoff_score does not dominate.

Do not allow C21 policy-event evidence alone to create Stage2/Stage3 promotion.
```

Expected effect: recover KB/Samsung-like missed structural cases as Stage2/Yellow without weakening global Green.

## 18. Canonical-Archetype Rule Candidate

```text
rule_name = C21_policy_event_without_capital_return_guard
rule_scope = canonical_archetype_specific
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
proposal_type = counterexample_guard_profile
confidence = medium
production_change = false
```

Guard:

```text
If C21 evidence is mainly policy/regulatory event + price movement,
and there is no explicit capital-return capacity / ROE-PBR gap / shareholder-return execution,
then block Stage2-Actionable and Stage3-Yellow promotion.
```

This guard is supported by the 카카오뱅크 counterexample: policy-event timing produced negligible MFE and deep MAE from the same entry date.

## 19. Before / After Backtest Comparison

| Profile | Scope | Eligible triggers | Avg MFE 90D | Avg MAE 90D | Avg MFE 180D | Avg MAE 180D | False-positive rate | Missed structural count | Late Green count | Score-return alignment |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `P0_e2r_2_1_stock_web_calibrated_proxy` | current global | 3 | `21.11%` | `-18.30%` | `29.43%` | `-20.02%` | conditional `1/3` if policy-only promoted | `2` | `2` | mixed |
| `P0b_e2r_2_0_baseline_reference` | rollback reference | 3 | `21.11%` | `-18.30%` | `29.43%` | `-20.02%` | higher, due weaker price/policy guard | `2` | `2` | weaker |
| `P1_L6_sector_specific_candidate_profile` | sector shadow | 3 | `21.11%` | `-18.30%` | `29.43%` | `-20.02%` | `0/3` with counterexample guard | `0-1` | `1` | improved |
| `P2_C21_canonical_archetype_candidate_profile` | canonical shadow | 3 | `21.11%` | `-18.30%` | `29.43%` | `-20.02%` | `0/3` with capital-return guard | `0-1` | `1` | improved |
| `P3_counterexample_guard_profile` | guard only | 3 | `21.11%` | `-18.30%` | `29.43%` | `-20.02%` | `0/3` | `2` | `2` | defensive but misses positive cases |

## 20. Score-Return Alignment Matrix

| Case | Weighted score before | Stage before | Weighted score after | Stage after | MFE 90D | MAE 90D | Alignment label |
|---|---:|---|---:|---|---:|---:|---|
| KB금융 | `74.0` | `Stage2` | `82.0` | `Stage3-Yellow-FinancialValueUp` | `44.00%` | `-4.48%` | `score_after_better_aligned` |
| 삼성생명 | `68.5` | `Stage2` | `76.5` | `Stage3-Yellow-FinancialValueUp` | `17.68%` | `-16.92%` | `score_after_partly_aligned_high_mae` |
| 카카오뱅크 | `60.0` | `Stage1/2-Watch` | `49.0` | `Stage1` | `1.66%` | `-33.50%` | `guard_after_better_aligned` |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| `L6_FINANCIAL_CAPITAL_RETURN_DIGITAL` | `C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN` | `KOREA_VALUEUP_ROE_PBR_CAPITAL_RETURN_BANK_INSURANCE` | 2 | 1 | 1 | 0 | 3 | 0 | 3 | 3 | 2 | true | true | Need C21 non-bank/insurance holdout, explicit 4C cases, and more policy-only false positives |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 1
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - financial_capital_return_underweighted
  - financial_policy_event_false_positive_without_return_execution
  - price_only_local_4B_too_early
new_axis_proposed:
  - financial_roe_pbr_capital_return_bridge_shadow
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: sector_specific_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated in this MD:

- Stock-web manifest/schema paths and manifest max date.
- Symbol profile existence and corporate-action candidate status for `105560`, `032830`, `323410`.
- Actual stock-web 1D OHLC rows for entry and forward-window backtest.
- MFE/MAE 30D/90D/180D/1Y calculations using raw unadjusted tradable OHLC.
- Sector/canonical-archetype residual hypothesis and machine-readable rows.

Not validated in this MD:

- Production `stock_agent` code behavior.
- Official company filing text for every capital-return detail.
- Live/current candidate status.
- Full 2Y windows from `2024-02-26` because stock-web manifest max date is `2026-02-20`.
- Any brokerage API or trading execution.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,financial_roe_pbr_capital_return_bridge,sector_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"C21 positives can rerate through ROE/PBR and capital return rather than contract/backlog evidence","KB strong MFE; Samsung full-window positive but high MAE",R6L10-C21-KBFG-T01|R6L10-C21-SLIF-T01,2,2,1,low,sector_shadow_only,"not production; post-calibrated residual"
shadow_weight,policy_event_without_capital_return_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"policy event alone produced false-positive risk in high-PBR growth-bank case","KakaoBank had tiny MFE and deep MAE",R6L10-C21-KBANK-T01,1,1,1,medium,counterexample_guard_profile,"block policy-only Stage2/Yellow promotion"
shadow_weight,full_4b_requires_non_price_evidence,existing_axis_kept,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,true,true,0,"KB local peak proximity high but full-window proximity low","price-only local 4B would be too early",R6L10-C21-KBFG-T01,1,1,0,medium,axis_stress_test_passed,"existing applied axis strengthened/kept"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R6L10-C21-KBFG-001","symbol":"105560","company_name":"KB금융","round":"R6","loop":"10","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"KOREA_VALUEUP_ROE_PBR_CAPITAL_RETURN_BANK_INSURANCE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R6L10-C21-KBFG-T01","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_after_better_aligned","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"financial-sector ROE/PBR and capital-return bridge candidate"}
{"row_type":"case","case_id":"R6L10-C21-SLIF-002","symbol":"032830","company_name":"삼성생명","round":"R6","loop":"10","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"KOREA_VALUEUP_ROE_PBR_CAPITAL_RETURN_BANK_INSURANCE","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R6L10-C21-SLIF-T01","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_after_partly_aligned_high_mae","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"C21 bridge positive but requires MAE/volatility guard"}
{"row_type":"case","case_id":"R6L10-C21-KBANK-003","symbol":"323410","company_name":"카카오뱅크","round":"R6","loop":"10","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"KOREA_VALUEUP_ROE_PBR_CAPITAL_RETURN_BANK_INSURANCE","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R6L10-C21-KBANK-T01","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"guard_after_better_aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"policy-event-only/high-PBR growth-bank guard case"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"R6L10-C21-KBFG-T01","case_id":"R6L10-C21-KBFG-001","symbol":"105560","company_name":"KB금융","round":"R6","loop":"10","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"KOREA_VALUEUP_ROE_PBR_CAPITAL_RETURN_BANK_INSURANCE","sector":"금융·자본배분·디지털금융","primary_archetype":"financial_roe_pbr_capital_return","loop_objective":"sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-26","evidence_available_at_that_date":"policy/regulatory value-up event plus C21 capital-return rerating proxy","evidence_source":"Korea Corporate Value-up public event; company capital-return proxy; stock-web OHLC","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength","valuation_repricing","early_revision_signal","capital_return_optionality"],"stage3_evidence_fields":["confirmed_return_execution_needed","multiple_public_sources_needed","low_red_team_risk"],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv","profile_path":"atlas/symbol_profiles/105/105560.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-26","entry_price":62500,"MFE_30D_pct":25.76,"MFE_90D_pct":44.00,"MFE_180D_pct":66.24,"MFE_1Y_pct":66.24,"MFE_2Y_pct":null,"MAE_30D_pct":-4.48,"MAE_90D_pct":-4.48,"MAE_180D_pct":-4.48,"MAE_1Y_pct":-4.48,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2026-02-13","peak_price":170500,"drawdown_after_peak_pct":-3.99,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.93,"four_b_full_window_peak_proximity":0.36,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":"price_only","four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"strong_structural_success","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L10-C21-KBFG-20240226-62500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L10-C21-SLIF-T01","case_id":"R6L10-C21-SLIF-002","symbol":"032830","company_name":"삼성생명","round":"R6","loop":"10","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"KOREA_VALUEUP_ROE_PBR_CAPITAL_RETURN_BANK_INSURANCE","sector":"금융·자본배분·디지털금융","primary_archetype":"financial_roe_pbr_capital_return","loop_objective":"sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-26","evidence_available_at_that_date":"policy/regulatory value-up event plus insurance capital-return/asset optionality proxy","evidence_source":"Korea Corporate Value-up public event; company capital-return proxy; stock-web OHLC","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength","valuation_repricing","asset_optional_capital_return"],"stage3_evidence_fields":["confirmed_return_execution_needed","financial_visibility_needed","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/032/032830/2024.csv","profile_path":"atlas/symbol_profiles/032/032830.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-26","entry_price":92200,"MFE_30D_pct":17.68,"MFE_90D_pct":17.68,"MFE_180D_pct":20.39,"MFE_1Y_pct":20.39,"MFE_2Y_pct":null,"MAE_30D_pct":-5.10,"MAE_90D_pct":-16.92,"MAE_180D_pct":-16.92,"MAE_1Y_pct":-16.92,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2026-02-20","peak_price":226500,"drawdown_after_peak_pct":0.00,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":null,"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"high_mae_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L10-C21-SLIF-20240226-92200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L10-C21-KBANK-T01","case_id":"R6L10-C21-KBANK-003","symbol":"323410","company_name":"카카오뱅크","round":"R6","loop":"10","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"KOREA_VALUEUP_ROE_PBR_CAPITAL_RETURN_BANK_INSURANCE","sector":"금융·자본배분·디지털금융","primary_archetype":"financial_policy_event_false_positive","loop_objective":"counterexample_mining","trigger_type":"Stage2-policy-watch","trigger_date":"2024-02-26","evidence_available_at_that_date":"policy/regulatory value-up event without explicit C21 capital-return execution evidence","evidence_source":"Korea Corporate Value-up public event; stock-web OHLC","stage2_evidence_fields":["policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":["thesis_evidence_weak_or_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv","profile_path":"atlas/symbol_profiles/323/323410.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-26","entry_price":30150,"MFE_30D_pct":1.66,"MFE_90D_pct":1.66,"MFE_180D_pct":1.66,"MFE_1Y_pct":1.66,"MFE_2Y_pct":null,"MAE_30D_pct":-17.74,"MAE_90D_pct":-33.50,"MAE_180D_pct":-38.67,"MAE_1Y_pct":-38.67,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-27","peak_price":30650,"drawdown_after_peak_pct":-39.67,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":null,"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"false_positive_policy_event","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L10-C21-KBANK-20240226-30150","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L10-C21-KBFG-001","trigger_id":"R6L10-C21-KBFG-T01","symbol":"105560","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":60,"revision_score":58,"relative_strength_score":78,"customer_quality_score":0,"policy_or_regulatory_score":82,"valuation_repricing_score":88,"execution_risk_score":18,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":74.0,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":60,"revision_score":58,"relative_strength_score":78,"customer_quality_score":0,"policy_or_regulatory_score":82,"valuation_repricing_score":88,"execution_risk_score":18,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":88},"weighted_score_after":82.0,"stage_label_after":"Stage3-Yellow-FinancialValueUp","changed_components":["roe_pbr_capital_return_score"],"component_delta_explanation":"C21 shadow bridge gives explicit credit for ROE/PBR discount plus capital-return route; no Green relaxation.","MFE_90D_pct":44.00,"MAE_90D_pct":-4.48,"score_return_alignment_label":"score_after_better_aligned","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L10-C21-SLIF-002","trigger_id":"R6L10-C21-SLIF-T01","symbol":"032830","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":44,"revision_score":38,"relative_strength_score":80,"customer_quality_score":0,"policy_or_regulatory_score":82,"valuation_repricing_score":90,"execution_risk_score":28,"legal_or_contract_risk_score":12,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":68.5,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":44,"revision_score":38,"relative_strength_score":80,"customer_quality_score":0,"policy_or_regulatory_score":82,"valuation_repricing_score":90,"execution_risk_score":28,"legal_or_contract_risk_score":12,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":78,"asset_optional_capital_return_score":82},"weighted_score_after":76.5,"stage_label_after":"Stage3-Yellow-FinancialValueUp","changed_components":["roe_pbr_capital_return_score","asset_optional_capital_return_score"],"component_delta_explanation":"C21 bridge raises Yellow only; high MAE prevents Green-like confidence.","MFE_90D_pct":17.68,"MAE_90D_pct":-16.92,"score_return_alignment_label":"score_after_partly_aligned_high_mae","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"counterexample_guard_profile","case_id":"R6L10-C21-KBANK-003","trigger_id":"R6L10-C21-KBANK-T01","symbol":"323410","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":28,"revision_score":25,"relative_strength_score":35,"customer_quality_score":0,"policy_or_regulatory_score":75,"valuation_repricing_score":32,"execution_risk_score":58,"legal_or_contract_risk_score":12,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":60.0,"stage_label_before":"Stage1/2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":28,"revision_score":25,"relative_strength_score":35,"customer_quality_score":0,"policy_or_regulatory_score":45,"valuation_repricing_score":32,"execution_risk_score":58,"legal_or_contract_risk_score":12,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":10},"weighted_score_after":49.0,"stage_label_after":"Stage1","changed_components":["policy_or_regulatory_score","roe_pbr_capital_return_score"],"component_delta_explanation":"Policy event score is capped when capital-return execution and ROE/PBR gap are not supported.","MFE_90D_pct":1.66,"MAE_90D_pct":-33.50,"score_return_alignment_label":"guard_after_better_aligned","current_profile_verdict":"current_profile_correct"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,financial_roe_pbr_capital_return_bridge,sector_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"ROE/PBR capital-return evidence explains C21 positives better than contract/backlog components","KB/Samsung positives; Kakao counterexample requires guard",R6L10-C21-KBFG-T01|R6L10-C21-SLIF-T01,2,2,1,low,sector_shadow_only,"not production; post-calibrated residual"
shadow_weight,policy_event_without_capital_return_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"policy-only event should not create C21 Stage2/Yellow","KakaoBank tiny MFE/deep MAE",R6L10-C21-KBANK-T01,1,1,1,medium,counterexample_guard_profile,"not production"
shadow_weight,full_4b_requires_non_price_evidence,existing_axis_kept,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,true,true,0,"price-only local 4B too early in KB path","local proximity 0.93 vs full-window 0.36",R6L10-C21-KBFG-T01,1,1,0,medium,axis_stress_test_passed,"existing axis strengthened/kept"
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R6","loop":"10","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":1,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["financial_capital_return_underweighted","financial_policy_event_false_positive_without_return_execution","price_only_local_4B_too_early"],"loop_contribution_label":"sector_specific_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"R6L10-C21-4C-MISSING","symbol":null,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","reason":"No hard 4C thesis-break case was validated in this loop; future loop should add credit-cost/capital-adequacy/accounting-break examples.","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
- Price-only rows cannot promote Stage2/Stage3.
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
next_round = R6_loop_11_or_L6_C22_insurance_rate_cycle_reserve
next_priority_1 = add C21 holdout cases with explicit company value-up filings and official disclosure timestamps
next_priority_2 = add C22 insurance reserve/rate-cycle cases to separate insurance-rate beta from capital-return rerating
next_priority_3 = add hard 4C financial cases: credit-cost shock, capital adequacy constraint, accounting/trust break, shareholder-return cancellation
next_priority_4 = expand counterexamples: policy-only financial names with weak ROE/PBR or no explicit return execution
```

## 28. Source Notes

Stock-web source files used:

- `atlas/manifest.json`
- `atlas/schema.json`
- `atlas/symbol_profiles/105/105560.json`
- `atlas/symbol_profiles/032/032830.json`
- `atlas/symbol_profiles/323/323410.json`
- `atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv`
- `atlas/ohlcv_tradable_by_symbol_year/105/105560/2025.csv`
- `atlas/ohlcv_tradable_by_symbol_year/105/105560/2026.csv`
- `atlas/ohlcv_tradable_by_symbol_year/032/032830/2024.csv`
- `atlas/ohlcv_tradable_by_symbol_year/032/032830/2025.csv`
- `atlas/ohlcv_tradable_by_symbol_year/032/032830/2026.csv`
- `atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv`
- `atlas/ohlcv_tradable_by_symbol_year/323/323410/2025.csv`
- `atlas/ohlcv_tradable_by_symbol_year/323/323410/2026.csv`

Allowed stock_agent research artifacts used:

- `reports/e2r_calibration/ingest_summary.md`
- `reports/e2r_calibration/applied_scoring_diff.md`
- `reports/e2r_calibration/calibrated_profile_report.md`
- `reports/e2r_calibration/by_round/R6.md`
- `data/e2r/calibration/md_registry.jsonl` excerpt/search

External historical policy-event notes reviewed for context only:

- Korea Corporate Value-up Programme announcement/guidelines coverage around February-May 2024.
- These policy-event sources anchor the common sector trigger family but are not sufficient by themselves for C21 positive promotion.
