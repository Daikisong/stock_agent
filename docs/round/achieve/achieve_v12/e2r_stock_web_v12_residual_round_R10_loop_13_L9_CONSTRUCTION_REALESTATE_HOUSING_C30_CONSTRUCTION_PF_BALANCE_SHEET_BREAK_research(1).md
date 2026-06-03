# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R10
scheduled_loop: 13
completed_round: R10
completed_loop: 13
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: PF_QUALITY_TRUST_BREAK_VS_BACKLOG_FALSE_POSITIVE_GUARD
output_file: e2r_stock_web_v12_residual_round_R10_loop_13_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
current_default_profile_proxy: e2r_2_1_stock_web_calibrated_proxy
previous_baseline_reference: e2r_2_0_baseline_reference
production_scoring_changed: false
shadow_weight_only: true
round_schedule_status: valid
round_sector_consistency: pass
```

This loop adds 4 new independent calibration-usable cases, 2 counterexamples, and 2 current-profile residual errors for R10/L9/C30. It also adds one narrative-only hard PF-liquidity case that is intentionally blocked from quantitative calibration because the stock-web forward path is trading-halt/corporate-action contaminated.

## 1. Current Calibrated Profile Assumption

The current profile is treated as `e2r_2_1_stock_web_calibrated_proxy`: Stage2 actionable evidence bonus +2.0, Yellow threshold 75, Green threshold 87, Green revision minimum 55, cross-evidence buffer +1.5, price-only blowoff block, non-price 4B requirement, and hard 4C thesis-break routing.

This MD does not re-prove those global axes. It stress-tests them inside C30, where the same construction headline can mean very different things: a real balance-sheet/trust break, a recoverable project-quality cost, a valid operating-leverage rerating, or a false positive from contract headline without margin conversion.

## 2. Round / Large Sector / Canonical Archetype Scope

- `scheduled_round`: R10
- `scheduled_loop`: 13
- `large_sector_id`: L9_CONSTRUCTION_REALESTATE_HOUSING
- `canonical_archetype_id`: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
- `fine_archetype_id`: PF_QUALITY_TRUST_BREAK_VS_BACKLOG_FALSE_POSITIVE_GUARD
- `loop_objective`: residual_false_positive_mining / 4B_non_price_requirement_stress_test / 4C_thesis_break_timing_test / canonical_archetype_compression / coverage_gap_fill / counterexample_mining

R10 hard gate passes because R10 maps to L9 construction/real estate/housing. C30 is the correct canonical compression for PF-liquidity, housing balance-sheet, construction-quality, and trust-break failures.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed stock_agent research artifacts were used only for duplicate and schedule context. The available registry shows prior historical R10 loops 1-9, but those files are older `e2r_stock_web_historical_calibration_round_*` forms, not the current v12 residual filename family. The registry also shows R10 repeated earlier with identical SHA patterns in several loops, reinforcing the need not to re-materialize the same schema. This file therefore uses new v12 naming and a new C30-specific trigger family.

Representative trigger rows artifact was empty in the fetched range, so duplicate avoidance was based on visible registry metadata plus the prior chat state: last completed v12 file was R9 / loop 13, so this file follows with R10 / loop 13.

Novelty decisions:

- HDC현대산업개발: hard 4C quality/governance trust break.
- GS건설: quality shock that should be 4B-watch, not automatic full 4C without PF/liquidity evidence.
- 대우건설: operating-leverage positive where PF/trust risks were not the thesis-break driver.
- 현대건설: contract-headline false positive under domestic PF/margin macro drag.
- 태영건설: hard PF-liquidity narrative-only case, blocked from quantitative calibration because of trading halt / 2024 corporate-action candidate contamination.

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-web manifest validation:

- `source_name`: FinanceData/marcap
- `source_repo_url`: https://github.com/FinanceData/marcap
- `price_adjustment_status`: raw_unadjusted_marcap
- `min_date`: 1995-05-02
- `max_date`: 2026-02-20
- `tradable_row_count`: 14,354,401
- `raw_row_count`: 15,214,118
- `symbol_count`: 5,414
- `active_like_symbol_count`: 2,868
- `inactive_or_delisted_like_symbol_count`: 2,546
- `markets`: KONEX / KOSDAQ / KOSDAQ GLOBAL / KOSPI
- `calibration_shard_root`: atlas/ohlcv_tradable_by_symbol_year
- `raw_shard_root`: atlas/ohlcv_raw_by_symbol_year
- `schema_path`: atlas/schema.json
- `universe_path`: atlas/universe/all_symbols.csv

The schema confirms tradable shard columns `d,o,h,l,c,v,a,mc,s,m`; MFE is calculated as max high over the forward tradable row window divided by entry close, and MAE as min low over the same window divided by entry close. Calibration requires positive OHLCV, entry row presence, at least 180 forward tradable days, and no 180D corporate-action contamination.

## 5. Historical Eligibility Gate

| case | entry row exists | >=180 forward tradable days | 180D corporate-action overlap | calibration_usable | reason |
|---|---|---:|---|---|---|
| HDC현대산업개발 294870 | yes | yes | no | true | 2022 window is after the only profile corporate-action candidate, 2020-03-26 |
| GS건설 006360 | yes | yes | no | true | profile corporate-action candidates are pre-2023 |
| 대우건설 047040 | yes | yes | no | true | profile corporate-action candidates are pre-2021 |
| 현대건설 000720 | yes | yes | no | true | profile corporate-action candidates are pre-2023 |
| 태영건설 009410 | yes | no clean continuous 180D path | yes / 2024-10-31 | false | trading gap plus corporate-action candidate blocks weight calibration |

## 6. Canonical Archetype Compression Map

C30 must not treat all construction headlines equally. This loop compresses five observed paths into one canonical map:

1. **Hard trust break**: safety/governance/regulatory event breaks investable thesis. HDC maps here.
2. **Quality-cost but not PF death**: quality/rebuild cost is severe but recovery is possible unless liquidity/accounting trust breaks. GS maps here.
3. **Normal operating leverage**: backlog/relative strength works when PF risk is not dominant. Daewoo maps here.
4. **Contract headline false positive**: large order lacks margin/revision conversion under domestic PF/macro drag. Hyundai Construction maps here.
5. **True PF liquidity crisis**: workout/liquidity break is highly relevant but can be non-calibration if trading halt/corporate action contaminates the OHLC path. Taeyoung maps here as narrative-only.

## 7. Case Selection Summary

| case_id | symbol | company | role | verdict | evidence weight |
|---|---:|---|---|---|---:|
| R10L13-C30-HDC-294870-20220112 | 294870 | HDC현대산업개발 | positive_protection | current_profile_correct | 1.0 |
| R10L13-C30-GS-006360-20230706 | 006360 | GS건설 | counterexample | current_profile_4C_too_early | 1.0 |
| R10L13-C30-DAEWOO-047040-20210311 | 047040 | 대우건설 | positive | current_profile_correct | 1.0 |
| R10L13-C30-HDEC-000720-20230626 | 000720 | 현대건설 | counterexample | current_profile_false_positive | 1.0 |


## 8. Positive vs Counterexample Balance

- Positive / aligned cases: 2
  - HDC현대산업개발: hard 4C protection worked.
  - 대우건설: positive operating-leverage Stage2 worked while PF/trust risk remained low.
- Counterexamples / residual errors: 2
  - GS건설: hard 4C would have been too early; 4B-watch fits better.
  - 현대건설: contract headline alone over-promoted score under PF/margin macro drag.
- Narrative-only hard PF case: 1
  - 태영건설: economically important but blocked from weight calibration by stock-web window contamination.

## 9. Evidence Source Map

| case | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence |
|---|---|---|---|---|
| HDC현대산업개발 | public event | none | legal/regulatory block | safety/trust thesis break |
| GS건설 | public rebuild event | none | cost/legal risk | watch-only thesis risk, not full PF/accounting break |
| 대우건설 | relative strength, backlog visibility | financial visibility | none | none |
| 현대건설 | overseas mega-order headline | weak margin/revision confirmation | price exhaustion, macro/PF drag | none |
| 태영건설 | workout/PF event | none | capital/liquidity risk | true liquidity thesis break, but non-calibration |

## 10. Price Data Source Map

| symbol | company | profile | tradable shard(s) | profile caveat |
|---:|---|---|---|---|
| 294870 | HDC현대산업개발 | atlas/symbol_profiles/294/294870.json | atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv | corporate-action candidate only 2020-03-26; 2022 window clean |
| 006360 | GS건설 | atlas/symbol_profiles/006/006360.json | atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv; 2024.csv | corporate-action candidates pre-2023 |
| 047040 | 대우건설 | atlas/symbol_profiles/047/047040.json | atlas/ohlcv_tradable_by_symbol_year/047/047040/2021.csv | corporate-action candidates pre-2021 |
| 000720 | 현대건설 | atlas/symbol_profiles/000/000720.json | atlas/ohlcv_tradable_by_symbol_year/000/000720/2023.csv; 2024.csv | corporate-action candidates pre-2023 |
| 009410 | 태영건설 | atlas/symbol_profiles/009/009410.json | atlas/ohlcv_tradable_by_symbol_year/009/009410/2023.csv; 2024.csv | 2024-10-31 corporate-action candidate; blocked |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | company | type | entry | price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | verdict | usable |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| R10L13-C30-HDC-4C-20220112 | 294870 | HDC현대산업개발 | Stage4C-Hard thesis break | 2022-01-12 | 20850 | 8.87 | -35.25 | 8.87 | -36.93 | 8.87 | -50.84 | current_profile_correct | true |
| R10L13-C30-GS-4B-20230706 | 006360 | GS건설 | Stage4B / 4C boundary | 2023-07-06 | 14520 | 3.86 | -7.92 | 5.03 | -12.74 | 19.83 | -12.74 | current_profile_4C_too_early | true |
| R10L13-C30-DAEWOO-STAGE2-20210311 | 047040 | 대우건설 | Stage2-Actionable | 2021-03-11 | 5720 | 26.75 | -1.92 | 66.78 | -1.92 | 66.78 | -1.92 | current_profile_correct | true |
| R10L13-C30-HDEC-STAGE2-20230626 | 000720 | 현대건설 | Stage2-Actionable / false-positive stress | 2023-06-26 | 40800 | 8.82 | -15.32 | 8.82 | -18.5 | 8.82 | -23.53 | current_profile_false_positive | true |


## 12. Trigger-Level OHLC Backtest Tables

### 12.1 HDC현대산업개발 / 294870 / hard 4C

- Entry: 2022-01-12 close 20,850.
- Peak inside forward path: 22,700 on 2022-01-12 high.
- The first 30 trading days included a low of 13,500; the 180D window later reached the 10,250/9,790 area depending on inclusive full observed window.
- Score-return alignment: hard 4C routing is justified. The price path never offered a durable Stage3 rerating after the trust break; it became a drawdown containment problem.

### 12.2 GS건설 / 006360 / 4B-watch vs full 4C

- Entry: 2023-07-06 close 14,520.
- 30D: MFE +3.86%, MAE -7.92%.
- 90D: MFE +5.03%, MAE -12.74%.
- 180D: MFE +19.83%, MAE -12.74%, with the full-window high at 17,400 on 2023-11-23.
- Interpretation: a quality-cost/legal event did not behave like an automatic hard 4C thesis death. It needed a 4B/watch overlay unless liquidity/accounting trust broke.

### 12.3 대우건설 / 047040 / operating leverage positive

- Entry: 2021-03-11 close 5,720.
- 30D: MFE +26.75%, MAE -1.92%.
- 90D/180D: MFE +66.78%, MAE -1.92% to the relevant 180D low basis.
- Interpretation: C30 should not become a blanket short/avoid archetype. When PF/trust risk components are low and relative strength/backlog components are high, Stage2 can remain a valid positive signal.

### 12.4 현대건설 / 000720 / contract-headline false positive

- Entry: 2023-06-26 close 40,800.
- Entry-day high: 44,400, but follow-through was weak.
- 30D: MFE +8.82%, MAE -15.32%.
- 90D: MFE +8.82%, MAE -18.50%.
- 180D: MFE +8.82%, MAE -23.53%.
- Interpretation: contract/backlog score without margin/revision confirmation can be a false Stage3-Yellow/Green in C30 when domestic PF/macro pressure is active.

## 13. Current Calibrated Profile Stress Test

| case | current profile likely label | actual OHLC alignment | verdict |
|---|---|---|---|
| HDC현대산업개발 | Hard 4C | aligned with sustained drawdown | current_profile_correct |
| GS건설 | likely hard 4C if quality event over-weighted | recovered to +19.83% 180D MFE | current_profile_4C_too_early |
| 대우건설 | Stage2/Yellow operating leverage | large MFE with shallow early MAE | current_profile_correct |
| 현대건설 | Stage3-Yellow risk from contract headline | high MAE and no durable rerating | current_profile_false_positive |

Existing global axes tested:

- `price_only_blowoff_blocks_positive_stage`: strengthened. Hyundai entry-day spike should not create positive Green.
- `full_4b_requires_non_price_evidence`: kept. GS has non-price evidence for 4B-watch, but not enough for full 4C.
- `hard_4c_thesis_break_routes_to_4c`: strengthened for HDC and narrative-only Taeyoung, but weakened as an automatic quality-event rule for GS.

## 14. Stage2 / Yellow / Green Comparison

C30 needs more friction between Stage2 and Stage3-Yellow/Green than a normal order-backlog archetype. The decisive divider is not contract size alone but whether the order/backlog evidence converts into margin, cash-flow, and balance-sheet safety.

- Daewoo: Stage2 worked because relative strength and backlog visibility did not conflict with PF/trust risk.
- Hyundai Construction: contract evidence without margin/revision conversion was not enough; a Stage2-watch cap is better.
- GS: 4B-watch was enough; hard 4C required evidence beyond quality/rebuild cost.
- HDC: Stage3 logic should be bypassed; hard 4C was the right route.

## 15. 4B Local vs Full-window Timing Audit

| case | 4B evidence type | local proximity | full-window proximity | verdict |
|---|---|---:|---:|---|
| HDC | legal/regulatory + trust break | n/a | n/a | hard 4C, not simple 4B |
| GS | legal/cost/margin slowdown | 0.00 | 0.00 | 4B-watch; full 4C too early |
| Hyundai Construction | price_only + margin/revision drag | 1.00 | 1.00 | entry-day exhaustion, not positive Green |

## 16. 4C Protection Audit

- HDC: `hard_4c_success`. Avoiding positive labels after the event protected against a 50%+ forward drawdown path.
- GS: `false_break_or_overhard_4c`. Treating all quality/rebuild events as hard 4C would have over-penalized a recoverable path.
- Taeyoung: economically a hard PF-liquidity 4C, but `narrative_only` because the stock-web path includes trading-halt/corporate-action contamination.

## 17. Sector-Specific Rule Candidate

No broad L9 sector-wide production rule is proposed from this loop. The better conclusion is C30-specific: construction names are heterogeneous. Overseas order winners, quality-event names, PF-liquidity stress names, and ordinary operating-leverage names must not share one global sector penalty.

`sector_specific_rule_candidate: false`

## 18. Canonical-Archetype Rule Candidate

`canonical_archetype_rule_candidate: true`

Proposed C30 shadow-only rules:

1. **C30 hard 4C gate**: hard 4C requires PF liquidity break, accounting/trust break, regulatory/safety thesis break, or forced restructuring evidence. Quality/rebuild cost alone is not always enough.
2. **Contract headline cap**: contract/backlog score cannot promote to Green unless margin/revision/working-capital evidence confirms conversion.
3. **Clean operating leverage allowance**: if PF/trust risk components are low, backlog/relative-strength positives can still score as Stage2/Yellow inside C30.

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | FP rate | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | 4 | 22.38 | -17.52 | 26.07 | -22.26 | 0.5 | mixed; two residual errors |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 4 | 22.38 | -17.52 | 26.07 | -22.26 | 0.5 | weaker; hard 4C protection less explicit |
| P1_sector_specific_candidate_profile | sector_specific | 4 | 22.38 | -17.52 | 26.07 | -22.26 | 0.5 | no sector-wide rule proposed |
| P2_C30_archetype_shadow_profile | canonical_archetype_specific | 4 | 22.38 | -17.52 | 26.07 | -22.26 | 0.25 | improves label alignment without global delta |
| P3_counterexample_guard_profile | canonical_archetype_specific | 4 | 22.38 | -17.52 | 26.07 | -22.26 | 0.25 | best guard profile for this loop |


## 20. Score-Return Alignment Matrix

| axis | aligned cases | residual cases | conclusion |
|---|---|---|---|
| hard_4c_thesis_break_routes_to_4c | HDC, Taeyoung narrative | GS | keep, but require explicit liquidity/accounting/trust break for full 4C |
| price_only_blowoff_blocks_positive_stage | Hyundai | none | strengthened within C30 |
| full_4b_requires_non_price_evidence | GS, HDC | none | kept; GS has non-price 4B but not full 4C |
| stage2_actionable_evidence_bonus | Daewoo | Hyundai | keep but cap contract-only evidence under PF macro |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative | current errors | sector rule | canonical rule | gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L9_CONSTRUCTION_REALESTATE_HOUSING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | PF_QUALITY_TRUST_BREAK_VS_BACKLOG_FALSE_POSITIVE_GUARD | 2 | 2 | 2 | 2 | 4 | 0 | 4 | 4 | 2 | false | true | C30 now has hard-4C, 4B-boundary, operating-leverage positive, and contract-headline false-positive coverage; still needs more small/mid-cap PF cases. |


## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 5
same_archetype_new_symbol_count: 5
same_archetype_new_trigger_family_count: 5
positive_case_count: 2
counterexample_count: 2
current_profile_error_count: 2
tested_existing_calibrated_axes:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - quality_event_full_4C_too_early
  - contract_headline_false_positive_under_PF_macro
new_axis_proposed:
  - c30_pf_liquidity_or_accounting_break_required_for_full_4c
  - c30_contract_headline_requires_margin_revision_confirmation
  - c30_clean_operating_leverage_low_risk_bonus
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - hard_4c_thesis_break_routes_to_4c_for_true_trust_break
existing_axis_weakened:
  - hard_4c_thesis_break_routes_to_4c_when_only_quality_cost_without_balance_sheet_break
existing_axis_kept:
  - full_4b_requires_non_price_evidence
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
diversity_score_summary: "same_archetype_new_symbol +20; new_symbol +15; same_archetype_new_trigger_family +20; counterexample_gap +4; residual_error +10; wrong_round_penalty 0; schema_rematerialization_penalty 0; estimated +69"
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- Stock-web manifest max_date and schema.
- Symbol profiles for 294870, 006360, 047040, 000720, and 009410.
- 30D/90D/180D MFE/MAE for the four calibration-usable representative triggers.
- Corporate-action window status at the profile level.
- Narrative-only block for 태영건설 due to trading gap and 2024-10-31 corporate-action candidate.

Not validated:

- Live candidate status.
- Current investment attractiveness.
- Brokerage execution.
- Production score implementation.
- Exact official disclosure timestamps beyond the historical event-date/entry-date rule used here.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c30_pf_liquidity_or_accounting_break_required_for_full_4c,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"HDC and Taeyoung support hard 4C only when trust/liquidity break is explicit; GS quality shock alone recovered enough to avoid automatic hard 4C.","reduces 4C-too-early false positives",R10L13-C30-HDC-4C-20220112|R10L13-C30-GS-4B-20230706,4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c30_contract_headline_requires_margin_revision_confirmation,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"Hyundai Construction order headline had high contract score but high 180D MAE without margin/revision confirmation.","caps false Yellow/Green from mega-order-only evidence",R10L13-C30-HDEC-STAGE2-20230626,4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c30_clean_operating_leverage_low_risk_bonus,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"Daewoo case shows backlog/relative strength can remain positive when PF/trust risk components are low.","preserves valid Stage2 positives inside a generally risk-heavy archetype",R10L13-C30-DAEWOO-STAGE2-20210311,4,4,2,low,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R10L13-C30-HDC-294870-20220112","symbol":"294870","company_name":"HDC현대산업개발","round":"R10","loop":"13","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_QUALITY_TRUST_BREAK_VS_BACKLOG_FALSE_POSITIVE_GUARD","case_type":"4C_success","positive_or_counterexample":"positive_protection","best_trigger":"R10L13-C30-HDC-4C-20220112","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"hard 4C label matched sustained drawdown and high MAE","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"광주 화정 아이파크 붕괴 사고가 장마감 이후 안전·시공품질·사업신뢰 훼손 이벤트로 공개되어 다음 거래일 종가 진입/보호 판단으로 처리."}
{"row_type":"case","case_id":"R10L13-C30-GS-006360-20230706","symbol":"006360","company_name":"GS건설","round":"R10","loop":"13","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_QUALITY_TRUST_BREAK_VS_BACKLOG_FALSE_POSITIVE_GUARD","case_type":"4B_too_early","positive_or_counterexample":"counterexample","best_trigger":"R10L13-C30-GS-4B-20230706","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"quality shock needed 4B watch, not immediate full 4C","current_profile_verdict":"current_profile_4C_too_early","price_source":"Songdaiki/stock-web","notes":"인천 검단 아파트 전면 재시공/품질비용 이벤트로 가격 충격은 컸으나, PF 유동성 붕괴·상장사 존속 위험까지 확정된 증거는 아직 부족."}
{"row_type":"case","case_id":"R10L13-C30-DAEWOO-047040-20210311","symbol":"047040","company_name":"대우건설","round":"R10","loop":"13","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_QUALITY_TRUST_BREAK_VS_BACKLOG_FALSE_POSITIVE_GUARD","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R10L13-C30-DAEWOO-STAGE2-20210311","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Stage2 operating leverage captured large forward MFE with shallow MAE","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"주택 경기/수주잔고/소유구조 재평가 기대와 함께 대량 거래가 발생했으나, 이 시점에는 PF 유동성 붕괴 증거가 아니라 정상적인 영업 레버리지 경로가 핵심."}
{"row_type":"case","case_id":"R10L13-C30-HDEC-000720-20230626","symbol":"000720","company_name":"현대건설","round":"R10","loop":"13","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_QUALITY_TRUST_BREAK_VS_BACKLOG_FALSE_POSITIVE_GUARD","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R10L13-C30-HDEC-STAGE2-20230626","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"contract headline was insufficient under PF/margin macro overlay","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"해외 대형 프로젝트/수주 헤드라인이 있었지만 국내 주택·PF·금리 부담이 margin/revision 가시성을 누르며 단순 수주 점수만으로 Green 승격하기 어려웠던 사례."}
{"row_type":"trigger","trigger_id":"R10L13-C30-HDC-4C-20220112","case_id":"R10L13-C30-HDC-294870-20220112","symbol":"294870","company_name":"HDC현대산업개발","round":"R10","loop":"13","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_QUALITY_TRUST_BREAK_VS_BACKLOG_FALSE_POSITIVE_GUARD","sector":"건설·부동산·주택","primary_archetype":"construction_quality_governance_trust_break","loop_objective":"4C_thesis_break_timing_test|counterexample_mining|coverage_gap_fill","trigger_type":"Stage4C-Hard thesis break","trigger_date":"2022-01-11","entry_date":"2022-01-12","entry_price":20850,"evidence_available_at_that_date":"광주 화정 아이파크 붕괴 사고가 장마감 이후 안전·시공품질·사업신뢰 훼손 이벤트로 공개되어 다음 거래일 종가 진입/보호 판단으로 처리.","evidence_source":"public incident/news; stock-web tradable shard rows 2022-01-12 onward","stage2_evidence_fields":["public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["legal_or_regulatory_block","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["accounting_or_trust_break","thesis_evidence_broken","regulatory_rejection"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv","profile_path":"atlas/symbol_profiles/294/294870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.87,"MFE_90D_pct":8.87,"MFE_180D_pct":8.87,"MFE_1Y_pct":8.87,"MFE_2Y_pct":8.87,"MAE_30D_pct":-35.25,"MAE_90D_pct":-36.93,"MAE_180D_pct":-50.84,"MAE_1Y_pct":-53.05,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-01-12","peak_price":22700,"drawdown_after_peak_pct":-56.87,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_full_4B_separate_hard_4C","four_b_evidence_type":["legal_or_regulatory_block","margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"hard_4c_drawdown_protection_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"HDC-294870-20220112-c20850","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R10L13-C30-GS-4B-20230706","case_id":"R10L13-C30-GS-006360-20230706","symbol":"006360","company_name":"GS건설","round":"R10","loop":"13","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_QUALITY_TRUST_BREAK_VS_BACKLOG_FALSE_POSITIVE_GUARD","sector":"건설·부동산·주택","primary_archetype":"quality_event_not_full_pf_balance_sheet_break","loop_objective":"4B_non_price_requirement_stress_test|counterexample_mining|canonical_archetype_compression","trigger_type":"Stage4B / 4C boundary","trigger_date":"2023-07-05","entry_date":"2023-07-06","entry_price":14520,"evidence_available_at_that_date":"인천 검단 아파트 전면 재시공/품질비용 이벤트로 가격 충격은 컸으나, PF 유동성 붕괴·상장사 존속 위험까지 확정된 증거는 아직 부족.","evidence_source":"public rebuild/news; stock-web tradable shard rows 2023-07-06 onward","stage2_evidence_fields":["public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","legal_or_regulatory_block","explicit_event_cap"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv|atlas/ohlcv_tradable_by_symbol_year/006/006360/2024.csv","profile_path":"atlas/symbol_profiles/006/006360.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.86,"MFE_90D_pct":5.03,"MFE_180D_pct":19.83,"MFE_1Y_pct":19.83,"MFE_2Y_pct":null,"MAE_30D_pct":-7.92,"MAE_90D_pct":-12.74,"MAE_180D_pct":-12.74,"MAE_1Y_pct":-12.74,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-11-23","peak_price":17400,"drawdown_after_peak_pct":-20.34,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.0,"four_b_full_window_peak_proximity":0.0,"four_b_timing_verdict":"non_price_4B_watch_but_full_4C_too_early","four_b_evidence_type":["legal_or_regulatory_block","margin_or_backlog_slowdown"],"four_c_protection_label":"false_break_or_overhard_4c","trigger_outcome_label":"4B_watch_preferred_over_hard_4C","current_profile_verdict":"current_profile_4C_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"GS-006360-20230706-c14520","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R10L13-C30-DAEWOO-STAGE2-20210311","case_id":"R10L13-C30-DAEWOO-047040-20210311","symbol":"047040","company_name":"대우건설","round":"R10","loop":"13","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_QUALITY_TRUST_BREAK_VS_BACKLOG_FALSE_POSITIVE_GUARD","sector":"건설·부동산·주택","primary_archetype":"construction_operating_leverage_without_pf_break","loop_objective":"residual_missed_structural_mining|coverage_gap_fill|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2021-03-11","entry_date":"2021-03-11","entry_price":5720,"evidence_available_at_that_date":"주택 경기/수주잔고/소유구조 재평가 기대와 함께 대량 거래가 발생했으나, 이 시점에는 PF 유동성 붕괴 증거가 아니라 정상적인 영업 레버리지 경로가 핵심.","evidence_source":"public order/ownership cycle context; stock-web tradable shard rows 2021-03-11 onward","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","backlog_or_delivery_visibility"],"stage3_evidence_fields":["financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/047/047040/2021.csv","profile_path":"atlas/symbol_profiles/047/047040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":26.75,"MFE_90D_pct":66.78,"MFE_180D_pct":66.78,"MFE_1Y_pct":66.78,"MFE_2Y_pct":null,"MAE_30D_pct":-1.92,"MAE_90D_pct":-1.92,"MAE_180D_pct":-1.92,"MAE_1Y_pct":-6.82,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-06-02","peak_price":9540,"drawdown_after_peak_pct":-44.13,"green_lateness_ratio":"0.23:Stage3 confirmation still left material upside but Stage2 captured most asymmetric leg","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success_without_pf_break","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"DAEWOO-047040-20210311-c5720","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R10L13-C30-HDEC-STAGE2-20230626","case_id":"R10L13-C30-HDEC-000720-20230626","symbol":"000720","company_name":"현대건설","round":"R10","loop":"13","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_QUALITY_TRUST_BREAK_VS_BACKLOG_FALSE_POSITIVE_GUARD","sector":"건설·부동산·주택","primary_archetype":"mega_order_not_enough_under_domestic_pf_macro","loop_objective":"residual_false_positive_mining|yellow_threshold_stress_test|coverage_gap_fill","trigger_type":"Stage2-Actionable / false-positive stress","trigger_date":"2023-06-26","entry_date":"2023-06-26","entry_price":40800,"evidence_available_at_that_date":"해외 대형 프로젝트/수주 헤드라인이 있었지만 국내 주택·PF·금리 부담이 margin/revision 가시성을 누르며 단순 수주 점수만으로 Green 승격하기 어려웠던 사례.","evidence_source":"public mega-order/news; stock-web tradable shard rows 2023-06-26 onward","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","backlog_or_delivery_visibility"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["margin_or_backlog_slowdown","valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000720/2023.csv|atlas/ohlcv_tradable_by_symbol_year/000/000720/2024.csv","profile_path":"atlas/symbol_profiles/000/000720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.82,"MFE_90D_pct":8.82,"MFE_180D_pct":8.82,"MFE_1Y_pct":8.82,"MFE_2Y_pct":null,"MAE_30D_pct":-15.32,"MAE_90D_pct":-18.5,"MAE_180D_pct":-23.53,"MAE_1Y_pct":-23.53,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-06-26","peak_price":44400,"drawdown_after_peak_pct":-29.73,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"entry_day_price_exhaustion_not_positive_green","four_b_evidence_type":["price_only","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating_high_MAE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"HDEC-000720-20230626-c40800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L13-C30-HDC-294870-20220112","trigger_id":"R10L13-C30-HDC-4C-20220112","symbol":"294870","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":15,"backlog_visibility_score":20,"margin_bridge_score":5,"revision_score":0,"relative_strength_score":5,"customer_quality_score":5,"policy_or_regulatory_score":20,"valuation_repricing_score":10,"execution_risk_score":95,"legal_or_contract_risk_score":90,"dilution_cb_risk_score":10,"accounting_trust_risk_score":75},"weighted_score_before":34,"stage_label_before":"Stage4C-Hard","raw_component_scores_after":{"contract_score":15,"backlog_visibility_score":20,"margin_bridge_score":5,"revision_score":0,"relative_strength_score":5,"customer_quality_score":5,"policy_or_regulatory_score":20,"valuation_repricing_score":10,"execution_risk_score":95,"legal_or_contract_risk_score":90,"dilution_cb_risk_score":10,"accounting_trust_risk_score":75},"weighted_score_after":34,"stage_label_after":"Stage4C-Hard","changed_components":["existing_axis_kept:hard_4c_thesis_break_routes_to_4c"],"component_delta_explanation":"Safety/governance trust break dominates; positive promotion blocked.","MFE_90D_pct":8.87,"MAE_90D_pct":-36.93,"score_return_alignment_label":"hard_4c_drawdown_protection_success","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L13-C30-GS-006360-20230706","trigger_id":"R10L13-C30-GS-4B-20230706","symbol":"006360","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":25,"backlog_visibility_score":35,"margin_bridge_score":15,"revision_score":10,"relative_strength_score":5,"customer_quality_score":15,"policy_or_regulatory_score":20,"valuation_repricing_score":15,"execution_risk_score":80,"legal_or_contract_risk_score":65,"dilution_cb_risk_score":10,"accounting_trust_risk_score":45},"weighted_score_before":41,"stage_label_before":"Stage4C-Hard_or_Red","raw_component_scores_after":{"contract_score":25,"backlog_visibility_score":35,"margin_bridge_score":15,"revision_score":10,"relative_strength_score":5,"customer_quality_score":15,"policy_or_regulatory_score":20,"valuation_repricing_score":15,"execution_risk_score":80,"legal_or_contract_risk_score":55,"dilution_cb_risk_score":10,"accounting_trust_risk_score":35},"weighted_score_after":54,"stage_label_after":"Stage4B-Watch","changed_components":["c30_quality_event_requires_pf_liquidity_or_accounting_break_for_full_4c"],"component_delta_explanation":"Event was non-price 4B, but 180D recovery argues against automatic hard 4C without balance-sheet or liquidity break.","MFE_90D_pct":5.03,"MAE_90D_pct":-12.74,"score_return_alignment_label":"4B_watch_preferred_over_hard_4C","current_profile_verdict":"current_profile_4C_too_early"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L13-C30-DAEWOO-047040-20210311","trigger_id":"R10L13-C30-DAEWOO-STAGE2-20210311","symbol":"047040","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":65,"backlog_visibility_score":70,"margin_bridge_score":55,"revision_score":45,"relative_strength_score":80,"customer_quality_score":45,"policy_or_regulatory_score":30,"valuation_repricing_score":50,"execution_risk_score":35,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":10,"accounting_trust_risk_score":25},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":65,"backlog_visibility_score":75,"margin_bridge_score":55,"revision_score":45,"relative_strength_score":85,"customer_quality_score":45,"policy_or_regulatory_score":30,"valuation_repricing_score":50,"execution_risk_score":35,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":10,"accounting_trust_risk_score":25},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow/Actionable","changed_components":["c30_non_pf_operating_leverage_can_stay_positive_when_risk_scores_are_low"],"component_delta_explanation":"High relative strength plus backlog visibility worked when PF/trust-break risk components stayed low.","MFE_90D_pct":66.78,"MAE_90D_pct":-1.92,"score_return_alignment_label":"structural_success_without_pf_break","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L13-C30-HDEC-000720-20230626","trigger_id":"R10L13-C30-HDEC-STAGE2-20230626","symbol":"000720","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":85,"backlog_visibility_score":70,"margin_bridge_score":30,"revision_score":35,"relative_strength_score":60,"customer_quality_score":70,"policy_or_regulatory_score":30,"valuation_repricing_score":45,"execution_risk_score":40,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":10,"accounting_trust_risk_score":20},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow_false_positive","raw_component_scores_after":{"contract_score":85,"backlog_visibility_score":70,"margin_bridge_score":20,"revision_score":25,"relative_strength_score":60,"customer_quality_score":70,"policy_or_regulatory_score":30,"valuation_repricing_score":45,"execution_risk_score":55,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":10,"accounting_trust_risk_score":20},"weighted_score_after":69,"stage_label_after":"Stage2-Watch","changed_components":["c30_contract_headline_cap_without_margin_revision_confirmation"],"component_delta_explanation":"Mega-order score was not enough; margin/revision and domestic PF macro dragged 180D MAE below tolerance.","MFE_90D_pct":8.82,"MAE_90D_pct":-18.5,"score_return_alignment_label":"failed_rerating_high_MAE","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R10","loop":"13","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":5,"same_archetype_new_symbol_count":5,"same_archetype_new_trigger_family_count":5,"new_trigger_family_count":5,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":2,"tested_existing_calibrated_axes":["price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["quality_event_full_4C_too_early","contract_headline_false_positive_under_PF_macro"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
{"row_type":"narrative_only","case_id":"R10L13-C30-TAEYOUNG-009410-20231228","symbol":"009410","company_name":"태영건설","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","reason":"workout/PF liquidity event has strong narrative value, but 2024-10-31 corporate-action candidate and a long non-tradable/trading-halt gap inside the 180D forward path block weight calibration","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration","entry_reference":"2023-12-28 close 2315 from tradable shard; 2024 rows show 2024-03-13 then 2024-10-31 discontinuity/corporate-action candidate"}
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
completed_round = R10
completed_loop = 13
next_round = R11
next_loop = 13
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Primary price source: Songdaiki/stock-web.

Fetched stock-web references used during this run:

- `atlas/manifest.json`: confirmed raw_unadjusted_marcap, 1995-05-02 to 2026-02-20 coverage, shard roots, and calibration notes.
- `atlas/schema.json`: confirmed OHLC columns and MFE/MAE formulas.
- `atlas/symbol_profiles/294/294870.json` and `atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv`.
- `atlas/symbol_profiles/006/006360.json`, `atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv`, and `2024.csv`.
- `atlas/symbol_profiles/047/047040.json` and `atlas/ohlcv_tradable_by_symbol_year/047/047040/2021.csv`.
- `atlas/symbol_profiles/000/000720.json`, `atlas/ohlcv_tradable_by_symbol_year/000/000720/2023.csv`, and `2024.csv`.
- `atlas/symbol_profiles/009/009410.json`, `atlas/ohlcv_tradable_by_symbol_year/009/009410/2023.csv`, and `2024.csv`.

The MD intentionally avoids live-candidate language and does not alter production scoring.
